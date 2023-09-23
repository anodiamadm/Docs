
# BUBBLE SORT

def sort(nums):
    for i in range(len(nums) -1, 0, -1):                 # NEGATIVE ORDER
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp                       # SWAPPING VALUES


nums = [10, 6, 9, 8, 4, 7]
sort(nums)
print(nums)


# SELECTION SORT


def sort(num):
    for i in range(5):
        mpos = i                                   # VARIABLE FOR MIN POSITION
        for j in range(i, 6):
            if num[j] < num[mpos]:
                mpos = j

        temp = num[i]
        num[i] = num[mpos]
        num[mpos] = temp


        print(num)                                 # OPTIONAL IF YOU WANT TO SEE LIVE


num = [10, 6, 9, 8, 4, 7]
sort(num)
print(num)
