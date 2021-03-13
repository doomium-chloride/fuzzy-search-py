from typing import Any, Dict

nonPrimitive = (dict, list)


def isPrimitive(value):
    return not isinstance(value, nonPrimitive)


def getDescendantProperty(dic, path, array = None):
    if array == None:
        array = []
    firstSegment = ""
    remaining = ""
    dotIndex = 0
    value = None
    index = 0
    length = 0

    if len(path) > 0:
        try:
            dotIndex = path.index('.')
            firstSegment = path[:dotIndex]
            remaining = path[dotIndex + 1:]
        except ValueError:
            firstSegment = path
        
        try:
            value = dic[firstSegment]
            if len(remaining) <= 0 and isPrimitive(value):
                array.append(value)
            elif isinstance(value, list):
                for item in value:
                    getDescendantProperty(item, remaining, array)
            elif len(remaining) > 0:
                getDescendantProperty(value, remaining, array)
        except KeyError:
            pass
    else:
        array.append(dic)
    return array
