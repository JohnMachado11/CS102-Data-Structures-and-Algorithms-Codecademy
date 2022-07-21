
def flatten(my_list):
    result = []

    for i in my_list:
        if type(i) == list: 
            flat_list = flatten(i)
            result += flat_list
        else:
            result.append(i)

    return result

planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets))