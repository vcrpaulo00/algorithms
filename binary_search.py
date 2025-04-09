'''my_list = ['apple', 'pineapple', 'orange', 'blueberry', 'graps']

def Binary_search (list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

print (Binary_search(my_list, 'blueberry'))
print (Binary_search(my_list, 'graps'))'''


my_list = [1, 3, 9, 7, 5]

def Binary_search (list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

print (Binary_search(my_list, 5))
print (Binary_search(my_list, 1))


'''my_list = 'Hello world'
print(len(my_list))'''