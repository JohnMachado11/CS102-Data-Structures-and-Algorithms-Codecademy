
def move_to_end(lst, val):

    result = []

    if not lst:
        return []

    if lst[0] == val:
        result += move_to_end(lst[1:], val)
        result.append(lst[0])
    else:
        result.append(lst[0])
        result += move_to_end(lst[1:], val)

    return result

gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))
