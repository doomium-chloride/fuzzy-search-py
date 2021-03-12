from Helper import Helper

class FuzzySearch:
    def __init__(self, haystack = [], keys = [], options = {}):
        self.haystack = haystack
        self.keys = keys if keys != None else []
        if not "caseSensitive" in options:
            options["caseSensitive"] = False
        if not "sort" in options:
            options["sort"] = False
        self.options = options
    
    def search(self, query = ""):
        if query == None or len(query) <= 0:
            return self.haystack
        
        results = []

        for item in self.haystack:
            print(item)
            if len(self.keys) <= 0:
                score = FuzzySearch.isMatch(item, query, self.options["caseSensitive"])
                if score != False:
                    results.append(( item, score ))
            else:
                for key in keys:
                    propertyValues = Helper.getDescendantProperty(item, key)

                    found = False

                    for propertyValue in propertyValues:
                        score = FuzzySearch.isMatch(propertyValue, query, self.options["caseSensitive"])

                        if score != False:
                            found = True
                            results.append(( item, score ))
                            break
                    
                    if found:
                        break
            
        if self.options["sort"]:
            results.sort(key=lambda item : item[1])

        return [result[0] for result in results]
    
    @staticmethod
    def isMatch(item, query, caseSensitive):
        item = str(item)
        query = str(query)

        if not caseSensitive:
            item = item.lower()
            query = query.lower()
        
        indicies = FuzzySearch.nearestIndexFor(item, query)

        if indicies == None:
            return False
        
        if item == query:
            return 1
        
        if len(indicies) > 1:
            return 2 + indicies[-1] - indicies[0]
        
        return 2 + indicies[0]
    
    @staticmethod
    def nearestIndexFor(item, query):
        letters = [letter for letter in query]
        
        indiciesOfFirstLetter = FuzzySearch.getIndiciesOfFirstLetter(item, query)
        indiciesLength = len(indiciesOfFirstLetter)
        # init the array
        indicies = [None] * indiciesLength
        
        for loopingIndex in range(indiciesLength):
            startingIndex = indiciesOfFirstLetter[loopingIndex]
            index = startingIndex
            indicies[loopingIndex] = [startingIndex]

            for letter in letters:
                try:
                    index = item.index(letter, index)
                    indicies[loopingIndex].append(index)
                    index += 1
                except ValueError:
                    indicies[loopingIndex] = None
                    break
        
        indicies = list(filter(lambda thing : thing != None, indicies))
        
        if len(indicies) <= 0:
            return None

        indicies.sort(key=lambda thing : thing[0] if len(thing) == 1 else thing[-1] - thing[0])

        return indicies[0]
    
    @staticmethod
    def getIndiciesOfFirstLetter(item, query):
        match = query[0]

        letters = [char for char in item]
        letterLength = len(letters)

        preFilter = [None] * letterLength

        for index in range(letterLength):
            if letters[index] == match:
                preFilter[index] = index
        return list(filter(lambda thing : thing != None, preFilter))