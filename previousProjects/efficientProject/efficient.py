
class efficient:
    
    def passList(self,listToReturn):
        newList = []
        for element in listToReturn:
            newList.append(element)
        return newList

    def add(self, min, max, dim):

        list = []
        subList = []

        for i in range(0, max + 1):
            subList.append(0)

        for i in range(0, max + 1):
            list.append(0)
        
        switch = False

        for i in range(0, dim):

            if switch :
            
                for j in range(0, max + 1):
                    subList[j] = self.passList(list)
            else:

                for j in range(0, max + 1):
                    list[j] = self.passList(subList)

            switch = not switch

        if switch:
            return subList
        else:
            return list

effObj = efficient()

addTwo = effObj.add(0,2,2)

for list in addTwo:
    print(list)

#print(addThree[1][0][0])
