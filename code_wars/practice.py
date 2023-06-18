def count_sheep(sheep_list):
    # a variable count is initialised to 0. variable will keep track of the num of sheep present
    count = 0
    for sheep in sheep_list:
        if sheep:
            count += 1
    return count

sheep_list = [True, True, True, False, True, True, True, True,
              True, False, True, False, True, False, False, True,
              True, True, True, True, False, False, True, True]

sheep_count = count_sheep(sheep_list)
print(sheep_count)  # Output: 17




