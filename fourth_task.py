def bubble_sort(array):

    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def finding_no_number(array):

    for i in array:
        if array[i+1]-array[i] == 2:
            return array[i]+1
        elif array[i+1] - array[i] > 2:
            return f"Correct list!!!"

list1 = [9,6,4,2,3,5,7,0,1]
print(f"Given list={list1}")
sorted_list = bubble_sort(list1)

print(f"Sorted list={sorted_list}")
print(f"No number inside list={finding_no_number(sorted_list)}")
