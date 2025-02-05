#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    #Hash each ticket
    for ticket in tickets:
        print(ticket.source, ticket.destination)
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    
    # Find location
    locat = hash_table_retrieve(hashtable, "NONE")

    # Retrieve value using location
    for i in range(0, length):
        route[i] = locat
        locat = hash_table_retrieve(hashtable, locat)

    return route 