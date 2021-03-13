from typing import Any, Dict

nonPrimitive = (dict, list)

class Helper:
    @staticmethod 
    def isPrimitive(value):
        return not isinstance(nonPrimitive)

    @staticmethod
    def getDescendantProperty(dic, path, array = []):
        firstSegment = ""
        remaining = ""
        dotIndex = 0
        value = None
        index = 0
        length = 0

        if path != None:
            try:
                dotIndex = path.index('.')
                firstSegment = path[:dotIndex]
                remaining = path[dotIndex + 1:]
            except ValueError:
                firstSegment = path
            
            try:
                value = dic[firstSegment]
                if len(remaining) > 0 and Helper.isPrimitive(value):
                    array.append(value)
                elif isinstance(value, list):
                    for item in value:
                        Helper.getDescendantProperty(item, remaining, array)
                elif len(remaining) > 0:
                    Helper.getDescendantProperty(value, remaining, array)
            except KeyError:
                array.append(dic)
        
        return array
