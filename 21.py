list1 = [1, 2, 4]
list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]


def mergeTwoLists(list1, list2):
    for item in list2:
        list1.append(item)
    list1.sort()

    return list1


print(mergeTwoLists(list1, list2))
