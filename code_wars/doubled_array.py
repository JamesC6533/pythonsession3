# def maps(a):
#     # initialises empty list in variable this stores the transformed values
#     solution = []
#     # iterates over each i element in the array a
#     for i in a:
#         # multiplies i by 2
#         i = i * 2
#         # appends the element to the 'solution' list
#         solution.append(i)
#     return solution

# defines a function named 'array_diff that takes two lists a and b as arguments
def array_diff(a, b):
    # initialises an empty list called 'solution' to store the elements from a that are not in b
    solution = []
    # for loop iterates over each element x in list a
    for x in a:
        # checks if the current element x is not present in list b
        if x not in b:
            # If the condition is true, the element x is appended to the solution list using solution.append(x)
            solution.append(x)
    return solution


a = [1, 2, 2, 2, 3]
b = [2]
solution = array_diff(a, b)
print(solution)  # Output: [1, 3]

