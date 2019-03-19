def bubble_sort(items):

    '''Return array of items, sorted in ascending order

        args:
            an array of items of a single data type

        returns:
            the array sorted in ascending order

        examples:
            >>>bubble_sort([1, 7, 3, 9, 10, 13, 8, 12, 15, 19])
            [1, 3, 7, 8, 9, 10, 12, 13, 15, 19]
            >>>bubble_sort(['yak', 'humble', 'bumble', 'bee'])
            ['bee', 'bumble', 'humble', 'yak']
    '''
    #declaration of variables
    item2 = items.copy()
    length = len(item2)

    #pass through all items
    for i in range(length):

        #pass through items from 0 to length-i-1
        #if one item is greater than the next, change them around
        for j in range(0, length-i-1):
            if item2[j]> item2[j + 1]:
                item2[j], item2[j + 1] = item2[j + 1], item2[j]

    return item2

def merge_sort(items):
    '''Return array of items, sorted in ascending order

        args:
            an array of items of a single data type

        returns:
            the array sorted in ascending order

        examples:
            >>>bubble_sort([1, 7, 3, 9, 10, 13, 8, 12, 15, 19])
            [1, 3, 7, 8, 9, 10, 12, 13, 15, 19]
            >>>bubble_sort(['yak', 'humble', 'bumble', 'bee'])
            ['bee', 'bumble', 'humble', 'yak']
    '''
    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

    #declaring index variables
    i=0
    j=0
    k=0

    #for each case, taking the 'less than' values and placing in front of the list
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            items[k]=lefthalf[i]
            i+=1
        else:
            items[k]=righthalf[j]
            j+=1
            k+=1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i+=1
            k+=1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j+=1
            k+=1
    return items


def quick_sort(items):

    '''Return array of items, sorted in ascending order

        args:
            a list of items of a single data type

        returns:
            the list sorted in ascending order

        examples:
            >>>quick_sort([1, 7, 3, 9, 10, 13, 8, 12, 15, 19])
            [1, 3, 7, 8, 9, 10, 12, 13, 15, 19]
            >>>quick_sort(['yak', 'humble', 'bumble', 'bee'])
            ['bee', 'bumble', 'humble', 'yak']
    '''
    #base statement for cases where the list is empty
    if len(items) == 0:
        return []

    #the function recursively moving through the list
    return quick_sort([x for x in items if x < items[0]]) \
        + [x for x in items if x == items[0]] \
        + quick_sort([x for x in items if x > items[0]])
