def binary_search(array, find):             # where array is the given array and find is what we are looking for
    i=0                                                                     ########## INFO ########## 
    low = 0                                 # the starting lower bound
    high = len(array)-1                     # the starting upper bound
    while high >= low:                      # we will keep running until we run out of possible sublists...
        i+=1                                                                ########## INFO ##########
        mid = (high + low) // 2             #   define the middle of the list to be the item at the index of the average of the lower and upper bound
        if array[mid] == find:              #   if item is in the middle of the list... we found what we are looking for!
            print(f"took {i} iterations")
            return mid                      #       therefore, we return the index of where we found the item.
        elif array[mid] > find:             #   if item is less than the middle of the list, this must mean that the item is on the lower half of the list
            high = mid-1                    #       therefore, we set the upper bound of the search to be the last item of the lower half
        else:                               #   if item is neither less than or equal to the middle of the list, this must mean that the item is on the upper half of the list
            low = mid+1                     #       therefore, we set the lower bound of the search to be the first item of the upper half
    else:                                   # if nothing is returned by the time the while loop ends, that means item MUST be missing from list
        return False                        #   therefore we tell the user that the requested item was not found

array = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100 ]
find = 82

result = binary_search(array, find)

if result != False:
    print(f"Requested value {find} is present at index {str(result)}")
else:
    print(f"Requested value {find} is not present in array")
# Expected output: Requested value 83 is not present at index 82
# you can see how efficient this is, only requiring 7 iterations instead of {insert number of iterations going 1 by 1 would take because im too lazy to calculate it}