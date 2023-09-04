nums = [34, 45, 65, 78, 98]
print("Value at Index #3= ", nums[3])
print("Values from Index #3= ", nums[3:])

names = ["sam", "ram", "tom"]
muldim = [nums, names]
print("Multi Dimensional array of different types of variables: \n", muldim)

nums.append(78)
print("Appending at the end= ", nums)

nums.insert(3, 89)
print("Inserting value at Index #3: ", nums)

nums.remove(45)
print("Removing the value 45: ", nums)

nums.pop()
print("Popping the last value: ", nums)

nums.pop(2)
print("Popping the index 2: ", nums)

del (nums[2:])
print("Deleting from index 2: ", nums)

nums.clear()
print("Clearing the entire list: ", nums)

nums.extend([34, 45, 65, 78, 98, 12, 9, 304])
print("Concatenating 2 lists: ", nums)

print("Max of all items in list: ", max(nums))
print("Min of all items in list: ", min(nums))
print("Sum of all items in list: ", sum(nums))

nums.sort()
print("Sort items of list: ", nums)

nums.sort(reverse=True)
print("Sort items of list in descending order: ", nums)
