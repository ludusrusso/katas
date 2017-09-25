def ssum(num_string):
    delimiter = ','
    strings = num_string.split('\n')
    if '//' in strings[0]:
        delimiter =  strings[0][2]
        strings.remove(strings[0])

    numbers = [int(x) for string in strings for x in string.split(delimiter) if len(x) > 0 if int(x) < 100]
    negs = [x for x in numbers if x < 0]
    if len(negs) > 0:
        raise ValueError('negatives not allowed',negs)
    return sum(numbers)
