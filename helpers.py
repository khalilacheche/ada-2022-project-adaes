import numpy as np
import matplotlib.pyplot as plt

# removes the nodes that are not in the final path in O(n)
def remove_backs(l):
    num_backs = len([a for a in l if a == "<"])
    num_pages = len(l) - num_backs
    assert num_backs <= num_pages
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


def get_bucket(game, x):
    x_s = [i / (len(game) - 1) for i in range(len(game))]  # standardize the times
    y_s = game
    arr = list(zip(enumerate(x_s[:-1]), x_s[1:]))
    i = [
        k for ((k, low), sup) in arr if (x >= low and x <= sup)
    ]  # binary search would be better than linear search
    i = i[0]
    y1, x1, y2, x2 = y_s[i], x_s[i], y_s[i + 1], x_s[i + 1]
    return y1, x1, y2, x2


# x between 0 and 1, game is a list of values (list of out-edges or smthng)
def get_estimation(game, x):
    y1, x1, y2, x2 = get_bucket(game, x)
    return (x - x1) * (y2 - y1) / (x2 - x1) + y1


def get_value_evolution(games_path_values, num_samples=100):
    points_x = []
    points_estimation = []
    points_std = []
    # sample 1000 points
    for x in range(num_samples):
        x = x / num_samples
        points_x.append(x)
        estimations = []
        for game in games_path_values:
            estimations.append(get_estimation(game, x))
        points_estimation.append(np.mean(estimations))
        points_std.append(np.std(estimations))
    return points_x, points_estimation, points_std
