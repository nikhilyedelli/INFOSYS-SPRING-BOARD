# Declare the necessary variables
i = 5
d = 3.3
s = "Hello, "

# Read 3 lines of input from stdin
int_input = int(input())
double_input = float(input())
string_input = input()

# Perform the required operations
int_sum = i + int_input
double_sum = d + double_input
string_concat = s + string_input

# Print the results
print(int_sum)
print("{:.1f}".format(double_sum)) # format the double to 1 decimal place
print(string_concat)

    


    