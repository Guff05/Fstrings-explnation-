# format Specifiers = {value:flags} format a value based on what 
#                                       flags are inserted



price1 = 3.14159
price2 = 987.65
price3 = 12.34
#Things like 2f changes how many decimals are to the right of the number 
#A zero in the front of the number tells you how many zeros are in the front
#
print(f"Price 1 is {price1:>10}")
print(f"Price 2 is {price2:<10}")
print(f"Price 1 is {price3:.010}")
