def find_max_min(numbers):
    if len(set(numbers))  == 1:
        return [len(numbers)]
    else:
        return[min(numbers),max(numbers)]
