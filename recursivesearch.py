def recursive_search(number_list, target, index=0):
    if index == len(number_list):
        return -1
    
    if number_list[index] == target:
        return index
    
    return recursive_search(number_list, target, index + 1)

number_list = [int(x) for x in input('Enter a list of numbers: (please seperate numbers by space)').split()]
target = int(input('Enter a number to search for:'))

result = recursive_search(number_list, target)

if result != -1:
    print(f"Number found at index {result}")
else:
    print('Number not found in the list')