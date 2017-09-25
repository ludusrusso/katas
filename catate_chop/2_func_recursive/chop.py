def chop(num, array, pos=0):
    if len(array) == 0:
        return -1
    elif len(array) == 1:
        return pos if num == array[0] else -1
    else:
        mid = len(array)/2
        if array[mid] == num:
            return mid + pos
        elif num < array[mid]:
            return chop(num, array[:mid], pos)
        else:
            return chop(num, array[mid+1:], pos+mid+1)
