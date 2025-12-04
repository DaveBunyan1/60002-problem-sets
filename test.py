from problem_set_1.ps1a import load_cows
from problem_set_1.ps1_partition import get_partitions


# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

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
    if not isinstance(cows, dict):
        raise TypeError("cows must be a dictionary.")

    best_partition = None
    partitions = get_partitions(cows)

    i = 0
    for partition in partitions:
        valid = True
        for trip in partition:
            weight = sum(cows[cow] for cow in trip)
            if weight > limit:
                valid = False
                break

        if valid:
            if best_partition is None or len(best_partition) > len(partition):
                best_partition = partition

    return best_partition if best_partition is not None else []


if __name__ == "__main__":
    filename = "problem_set_1/ps1_cow_data.txt"
    cows = load_cows(filename)

    brute_force_cow_transport(cows)
