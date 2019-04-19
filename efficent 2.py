
class efficient:

    def add(self, min, max, dim):

        newList = []

        dimCounters = []

        for i in range(dim):
            dimCounters.append(0)

        for i in range((max + 1) ** dim):

            shuma = 0

            for dimValue in dimCounters:
                if dimValue > min:
                    shuma += dimValue

            newList.append(shuma)
            
            for j in range(len(dimCounters)):

                if j == 0:
                    dimCounters[j] += 1

                if dimCounters[j] >= max + 1:
                    dimCounters[j] = 0
                    if (j + 1) < len(dimCounters):
                        dimCounters[j + 1] += 1

        sublist = []
        switch = True

        for i in range(0, dim - 1):

            if switch:

                sublist = []
                listGroup = []
                counter = 0

                for i in range(len(newList)):
                    listGroup.append(newList[i])
                    counter += 1
                    if counter >= max + 1:
                        sublist.append(listGroup)
                        counter = 0
                        listGroup = []

                switch = False

            else:

                newList = []
                listGroup = []
                counter = 0

                for i in range(len(sublist)):
                    listGroup.append(sublist[i])
                    counter += 1
                    if counter >= max + 1:
                        newList.append(listGroup)
                        counter = 0
                        listGroup = []

                switch = True
            
        if switch:
            return newList
        else:
            return sublist

effObj = efficient()

addMatrix = effObj.add(0,3,3)

for list in addMatrix:
    print(list)


