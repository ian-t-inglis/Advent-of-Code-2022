# Problem - Calorie Counting 
# Link - https://adventofcode.com/2022/day/1
# Author - Ian Inglis

## Verbal breakdown of problem:
# Import list of numbers
# Split total list where there's newlines 
# Sum the items between newline characters
# Return the largest value 


# This section imports the text file and splits the values to be used more easily
Calories = open('input.txt')
Calories = ''.join(Calories)
Calories = Calories.splitlines()

# These lists are created to assist with the loops further in the code
# They allow for storage of values 
Calories_Sum = []
Value_Store = []
List_Store_Int = []

# This for loop recreates the original list, appending everything with a type of 'integer'
# It also then replaces the empty character spaces with a 0
for enum in range(len(Calories)):
    if Calories[enum] == '':
        List_Store_Int.append(0)
    else:
        List_Store_Int.append(int(Calories[enum]))

# This loop loops over the entire list of integer values
# It loops over ever non-zero value and appends it to a list
# Once a zero value is found, it sums all the values appended and stores this in a new list
# It then clears the previous list, ready to accept new values with being affected by previous values

for x in range(len(List_Store_Int)):
    if List_Store_Int[x] != 0 and x == (len(List_Store_Int)-1):
        Calories_Sum.append(sum(Value_Store))
        Value_Store.clear()
    elif List_Store_Int[x] == 0:
        Calories_Sum.append(sum(Value_Store))
        Value_Store.clear()
    else:
        Value_Store.append(List_Store_Int[x])

# This returns the largest amount of calories carried by the elf
print("The elf carrying to most calories is", max(Calories_Sum))


# This sorts the list in reverse order, starting with the largest and working to the smallest
# A variable is then assigned with the top three values 
Calories_Sum.sort(reverse=True)
Top_Three = Calories_Sum[0] + Calories_Sum[1] + Calories_Sum[2]
print("The total amount of calories of the elves carrying the most calories is", Top_Three)
