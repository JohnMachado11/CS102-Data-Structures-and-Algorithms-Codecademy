


def linear_search(search_list, target_value):

    matches = []

    for i in range(len(search_list)):
        if search_list[i] == target_value:
            matches.append(i)
        
    if matches:
        return matches
    else:
        raise ValueError("{} not in list".format(target_value))


tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"


print(linear_search(tour_locations, target_city))