def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(5))


def remove_every_other(my_list):
    result = []
    for index in range(len(my_list)):
        if index % 2 == 0:
            result.append(my_list[index])
    return result

my_list = ["Keep", "Remove", "Keep", "Remove", "Keep", "Remove"]
result = remove_every_other(my_list)
print(result)






