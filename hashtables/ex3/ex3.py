def intersection(arrays):
    """
    YOUR CODE HERE
    Create a hash table whose keys are the numbers in our lists, iterate over each list and increment an integer at that key by 1 every time the same number is seen.
    """

    result = []

    cache = {}

    for array in arrays:
        for number in array:
            if number not in cache:
                cache[number] = 1
            else:
                cache[number] += 1

    for key, value in cache.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
