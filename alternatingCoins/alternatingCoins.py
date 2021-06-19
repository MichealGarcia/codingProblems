# initialize list with 0's and 1's representing heads or tails on a coin
A = [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0]

# define function to find least # of flips to create alternating coin pattern
def leastFlips(A):
    # initialize list values, there are only two possible starting values.
    # Need to use strings to add into list, and convert later
    s1, s2 = "0", "1"
    # loop through input list and create comparable lists for two possible starting values.
    for i in range(len(A)):
        # Add 0 if i is an even number and 1 if it is odd
        s1 += "0" if i % 2 else "1"
        # add 1 if i is an even number and 0 if it is odd
        s2 += "1" if i % 2 else "0"
    # Use the map function to change the values in list s1 and s2 to integers
    # If you do not add the list function you will not return a list while using the map funciton
    s1 = tuple(map(int, s1))
    s2 = tuple(map(int, s2))

    # Using List comprehension, I am using the zip finction to do a side by side
    # comparison of my input list A and lists s1, s2. Then applying the sum function
    # to add the total number of differences in each comparison. 
    compare = sum([1 if i==i2 else 0 for i, i2 in zip(A,s1)])
    compare2 = sum([1 if i==i2 else 0 for i, i2 in zip(A,s2)])
    # If one list has less differences, it is eqaul to answer.
    if compare > compare2:
        ans = compare2
    else:
        ans = compare
        
            

    return s1
leastFlips(A)