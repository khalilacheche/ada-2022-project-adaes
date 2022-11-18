import numpy as np
from numpy.random import default_rng

# for a given series of visited pages, this method removes the nodes that are not in the final path in O(n)
# by folding the back characters ("<") with the page preceding it and removing them from the path
def remove_backs(l):
    # Sanity check on the number of backs performed in the path
    num_backs = len([a for a in l if a == "<"])
    num_pages = len(l) - num_backs
    assert num_backs <= num_pages
    # the idea here is to consider the reverse of the path
    # and count the number of successive backs
    # skip the elements of the path that should not be considered
    l.reverse()
    res = []
    n_to_skip = 0
    i = 0
    while i < len(l):
        elem = l[i]
        if elem == "<":
            n_to_skip += 1
        if n_to_skip == 0:
            res.append(elem)
        elif elem != "<":
            i = i + n_to_skip - 1
            n_to_skip = 0
        i += 1
    res.reverse()
    return res


# this function returns the values of y_s and their relative times (considering the time) that are upper and lower bounding
# the times corresponding to x is a sorted list of values
# x : between 0 and 1
# y_s: a list of values
# returns:
# the xs returned are  between 0 and 1, and y is the uppeer and lower bound of the values of y_s
def get_bucket(y_s, x):
    x_s = [i / (len(y_s) - 1) for i in range(len(y_s))]  # standardize the times
    upper_arr = x_s[1:]
    lower_arr = x_s[:-1]
    i = binary_search(lower_arr, upper_arr, 0, len(lower_arr) - 1, x)
    assert i >= 0
    y1, x1, y2, x2 = y_s[i], x_s[i], y_s[i + 1], x_s[i + 1]
    return y1, x1, y2, x2


# Performs a binary search to find the index i that satisfies lower_arr[i]=< x <= upper_arr[i]
def binary_search(lower_arr, upper_arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if x >= lower_arr[mid] and x <= upper_arr[mid]:
            return mid
        elif lower_arr[mid] > x:
            return binary_search(lower_arr, upper_arr, low, mid - 1, x)
        else:
            return binary_search(lower_arr, upper_arr, mid + 1, high, x)
    else:
        return -1


# returns an estimation of the inbetween value that we will get in the "game" sequence
# by doing a linear estimation
def get_estimation(game, x):
    y1, x1, y2, x2 = get_bucket(game, x)
    return (x - x1) * (y2 - y1) / (x2 - x1) + y1


# Method to calculate the evolution of a particular value
# by averaging over the multiple instances
# it takes an array of a series of values where each series can have a different length (but must be >1)
# and returns an array of length the given number of samples representing the evolution of the average of these values
# as well as the corresponding confidence intervals (sampled with a bootstrapping method) and the time component of each value
def get_value_evolution(games_path_values, num_samples=100):
    points_x = []
    points_estimation = []
    points_upper_bound = []
    points_lower_bound = []
    for x in range(num_samples):
        x = x / num_samples
        points_x.append(x)
        estimations = []
        for game in games_path_values:
            estimations.append(get_estimation(game, x))
        (ci_low, ci_up), mean = get_CI_and_average(estimations)
        points_estimation.append(mean)
        points_lower_bound.append(ci_low)
        points_upper_bound.append(ci_up)
    return points_x, points_estimation, points_lower_bound, points_upper_bound


# returns the mean and the confidence interval of a sample using a bootstrapping method
def get_CI_and_average(X, nbr_draws=1000, confidence=0.95):
    rng = default_rng()
    values = [rng.choice(X, size=len(X), replace=True).mean() for i in range(nbr_draws)]

    CI = np.percentile(
        values, [100 * (1 - confidence) / 2, 100 * (1 - (1 - confidence) / 2)]
    )
    average = np.mean(values)

    return (CI, average)


# Method to reduce the Topics
def reduce(s):
    s = s[::-1]
    index1 = s.find(".")
    return s[0:index1][::-1]
