from problem_set_1.ps1a import load_cows

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    remaining = sorted(cows.items(), key=lambda item: item[1], reverse=True)
    trips = []

    while remaining:
        trip = []
        limit_left= limit
        new_remaining = []


        for name, weight in remaining:
            if weight <= limit_left:
                trip.append(name)
                limit_left -= weight
            else:
                new_remaining.append((name, weight))

        trips.append(trip)
        remaining = new_remaining

    print(trips)



if __name__ == "__main__":
    filename = "problem_set_1/ps1_cow_data.txt"
    cows = load_cows(filename)
    
    greedy_cow_transport(cows)
