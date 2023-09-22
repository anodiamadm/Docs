pos = -1

def search(list, n):
    l = 0                                          # LOWER BOUND
    u = len(list)-1                                # UPPER BOUND

    while l <= u:
        mid = (l+u) // 2                           # MID VALUE

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1                        # SHIFTING MID VALUE
            else:
                u = mid - 1

    return False

list = [9, 2, 45, 67, 5, 10, 1]
n = 67

if search(list,n):
    print("Found at ", pos)
else:
    print("Not found")
