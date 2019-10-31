number = 2134
number_str = str(number)
number_str_dob= str(number)
#1
dob = int(number_str_dob[0])*int(number_str_dob[1])*int(number_str_dob[2])*int(number_str_dob[3])
print("Product of number '2134'",dob)
#2
print("number '2134' in reverse order:",number_str[::-1])
#3
number_sort = ''.join(sorted(number_str))
print("sorted number:",number_sort)
