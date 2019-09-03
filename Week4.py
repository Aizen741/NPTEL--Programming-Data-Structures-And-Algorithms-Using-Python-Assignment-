def frequency(l):
    unique_l = list(set(l))
    freq_list = [l.count(x) for x in unique_l]
    min_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == min(freq_list)]
    max_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == max(freq_list)]
    min_freq_list.sort()
    max_freq_list.sort()
    return (min_freq_list, max_freq_list)


def onehop(lst):
    data = lst
    data.sort(key=lambda tup: tup[0])  # Sort
    ans = []
    for ele in lst:
        x, y = ele  # Storing Tuple value in x and y
        for ele1 in lst:  # For finding next hop for all destinations
            if ele != ele1:  # To check if it's not the same element in loop
                xx, yy = ele1  # Storing another tuple's value in xx, yy
                if y == xx and x != yy and (x, yy) not in ans:  # checking conditions for adding to ans.

                    ans.append((x, yy))
    ans = sorted(ans, key=lambda tup: (
    tup[0], tup[1]))

    return ans