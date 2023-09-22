def shellsort(elems):
    #sorted_elems = elems.copy()
    sorted_elems = list(elems)
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(sorted_elems)):
            temp = sorted_elems[i]
            j = i
            while j >= gap and sorted_elems[j - gap] > temp:
                sorted_elems[j] = sorted_elems[j - gap]
                j -= gap
            sorted_elems[j] = temp

    return sorted_elems

def assertEquals(elems, sorted_elems):
    assert elems == sorted_elems
    
def shellsort_check(elems, true_sorted_elems):
    res_elems = shellsort(elems)
    assertEquals(res_elems, true_sorted_elems)
    return res_elems

#shellsort([3, 2, 1])
shellsort_check([3,2,1],[1,2,3])

assert shellsort([9,1,0,-1,99,123,2]) == [-1,0,1,2,9,99,123]
assert shellsort([9,8,7,6]) == [6,7,8,9]
assert shellsort([]) == []
assert shellsort([8,9,10,5,5]) == [5,5,8,9,10]

def is_sorted(elems):
    return all(elems[i] <= elems[i + 1] for i in range(len(elems) - 1))

def is_permutation(a, b):
    return len(a) == len(b) and all(a.count(elem) == b.count(elem) for elem in a)

def check_shellsort(elems, res):
    assert is_sorted(res)
    assert is_permutation(elems, res)

import random
for i in range(1,1000):
    elems = []
    length = random.randint(1,10)
    for j in range(length):
        elems.append(1 + random.random() * 10000)
    sorted_elems = shellsort(elems)
    check_shellsort(elems, sorted_elems)
    print(elems)
    print(sorted_elems)
