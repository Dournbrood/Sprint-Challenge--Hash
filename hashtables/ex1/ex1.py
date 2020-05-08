def get_indices_of_item_weights(weights, length, limit):

    cache = {}

    for index, value in enumerate(weights):
        if limit - value in cache.keys():
            print(sorted((cache[limit - value], index), reverse=True))
            return sorted((cache[limit - value], index), reverse=True)
        cache[value] = index

    return None
