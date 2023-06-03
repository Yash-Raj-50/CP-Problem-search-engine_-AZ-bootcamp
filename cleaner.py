import re
arr = []

with open("lc.txt", "r") as file:
    
    for line in file:
        arr.append(line)


def remove_elements_with_pattern(array, pattern):
    new_array = []
    for element in array:
        if pattern not in element:
            new_array.append(element)
        else:
            print("Removed: " + element)
    return new_array


arr = remove_elements_with_pattern(arr, "/solution")
print(len(arr))
arr = list(set(arr))

with open('cleaned_problems.txt', 'a') as f:
    for j in arr:
        f.write(j)