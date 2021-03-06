'''
排序
'''



def select_sort(origin_items, comp=lambda x, y: x < y):
    '''简单排序'''
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items




def bubble_sort(origin_items, comp=lambda x, y: x < y):
    '''高质量冒泡排序'''
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 -i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j-1], items[j]):
                    items[j], items[j-1] = items[j-1], items[j]
                    swapped = True
        if not swapped:
            break
    return items







if __name__ == '__main__':
    l = [3, 2, 5, 9, 10]
    # r = select_sort(l)
    r = bubble_sort(l)
    print(r)