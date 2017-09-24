def chop(num, array):
    min_p = 0
    max_p = len(array) - 1
    while min_p <= max_p:
        mid = (max_p + min_p)/2
        if array[mid] == num:
            return mid
        elif num < array[mid]:
            max_p = mid - 1
        else:
            min_p = mid + 1
    return -1
