my_list = [5, 6, 2, 8, 98, 65, 45, 33, 12, 61]
my_list.sort()
print(my_list)


def search_me(target, left, right) -> str:
    print(target, left, right)
    if left > right:
        return "not found"

    center = int((left + right) / 2)
    print(center)

    if target == my_list[center]:
        return f"found your item at index {center}"
    elif target > my_list[center]:
        print("left")
        return search_me(target, center + 1, right)
    elif target < my_list[center]:
        print("right")
        return search_me(target, left, center - 1)


my_item = 6
index = search_me(my_item, 0, len(my_list) - 1)

print(f"max lenght of object: {len(my_list) - 1}\nitem position: {index}")


