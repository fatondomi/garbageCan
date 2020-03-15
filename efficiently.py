
#
#   add returns the a multidimensional list with dim dimensions
#   which can be used to add numbers without adding them
#   
#   add3Numbers = add(1,3,3)
#   print(add3Numbersp[1][1][1]) #prints 3


def add(min, max, dim):
    #
    #   new list is used to group elements together into a list,
    #   dimCounters is a list of counters used to iterate through 
    #   the multidimensional list with dim number of dimensions to  
    #   produce the different values of the list  
    #    
    newList = []
    dimCounters = []
    shuma = 0

    #   each dimension gets a counter which starts at 0
    for i in range(dim):
        dimCounters.append(0)

    #   this loop produces all the values of the list
    #   which in this case are the dimCounters sum
    for i in range((max + 1) ** dim):
        # shuma is used to store the sum
        shuma = 0

        #   checking if any of the values of the dim counters
        #   is less than min in which case it will make it 0
        #   as it will never be used (only min to max are used)
        for dimValue in dimCounters:
            if dimValue >= min:
                shuma += dimValue
            else:
                shuma = 0
                break
                
        #   appending all the values of the n dimensional list
        newList.append(shuma)

        #   refreshing the counters
        for j in range(len(dimCounters)):

            if j == 0:
                dimCounters[j] += 1

            if dimCounters[j] >= max + 1:
                dimCounters[j] = 0
                if (j + 1) < len(dimCounters):
                    dimCounters[j + 1] += 1

    #   sublist is used to group elements together in lists, 
    #   switch keeps track of which list (sublist or newList)
    #   we are going to use to regroup the elements in
    #   listGroup holds the temporary group and counter
    #   counts the number of elements inside listGroup
    sublist = []
    switch = True
    listGroup = []
    counter = 0

    #   it takes (dim-1) regroupings each time increasing the dimension by one
    #   to make the final list dim dimensional list
    #   the elements go from numbers to list of numbers to multidimensional lists
    #   and finally the last grouping is returned to the user
    for i in range(0, dim - 1):

        if switch:

            sublist = []

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


#
#   filter returns a multidimensional list which can be 
#   used to filter data or graph to other data by the function
#   the user inputs
#   
#   def
#
#   filter3 = filter(1,3,3,filterFunction)
#   print(filter3[1][1][1]) #prints 3 if filter function was adding the three inputs

def filter(min,max,dim,filterFunction):
    
    newList = []
    dimCounters = []
    shuma = 0

    for i in range(dim):
        dimCounters.append(0)

    for i in range((max + 1) ** dim):

        shuma = filterFunction(dimCounters)

        for dimValue in dimCounters:
            if dimValue < min:
                shuma = 0
                break

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
    listGroup = []
    counter = 0

    for i in range(0, dim - 1):

        if switch:

            sublist = []

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
