#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    route = []

    cache = {}

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    current_ticket = cache["NONE"]

    while 1:
        if current_ticket == "NONE":
            route.append("NONE")
            break
        route.append(current_ticket)
        current_ticket = cache[current_ticket]

    return route
