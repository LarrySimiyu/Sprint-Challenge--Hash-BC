#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)
def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    """
    YOUR CODE HERE
    """
    # We add all weights to our hashtable
    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)

    # We search for the two keys that sum to our limit
    for i, weight in enumerate(weights):
        result = hash_table_retrieve(ht, limit - weight)
        if result is not None:
            if result > i:
                return (result, i)
            else:
                return (i, result)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")