def insert(sorted, value):
    i = len(sorted) - 1
    sorted.append(None) 
    while i >= 0 and sorted[i] > value:
        sorted[i + 1] = sorted[i]
        i -= 1
    sorted[i + 1] = value



def insertion_sort(input):
    sorted = [input[0]]
    for i in range(1, len(input)):
        insert(sorted, input[i])
    return sorted