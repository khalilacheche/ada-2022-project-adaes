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
