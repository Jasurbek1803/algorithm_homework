def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [i for i in array[1:] if i < pivot]
        right = [i for i in array[1:] if i >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

def binary_search(array, number):
    if len(array) == 1:
        if array[0] == number:
            return 1
        else:
            return 0

    mid = len(array) // 2
    if array[mid] == number:
        return 1
    elif array[mid] > number:
        return binary_search(array[:mid],number)
    else:
        return binary_search(array[mid+1:], number)


list1  = [1,6,2,-9, 3,-3,6,9]
print(f"Given list={list1}")
sorted_list = quick_sort(list1)
print(f"Sorted list={sorted_list}")

number = int(input("Son kiriting="))
result = binary_search(sorted_list, number)

if result == 1:
    print(f"Son ro'yxatda mavjud")
elif result == 0:
    print(f"Son ro'yxatda mavjud emas")
