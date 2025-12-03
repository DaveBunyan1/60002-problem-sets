# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    data = {}
    with open(filename) as f:
        for line in f:
            name, weight = line.strip().split(',')
            data[name] = int(weight)

    print(data)
    return



if __name__ == "__main__":
    filename = "problem_set_1/ps1_cow_data.txt"
    load_cows(filename)
