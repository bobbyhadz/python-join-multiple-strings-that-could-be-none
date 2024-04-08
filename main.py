# Join multiple Strings with possibly None values in Python

str_1 = 'Bobby'
str_2 = None
str_3 = 'Hadz'

result = ', '.join(filter(None, [str_1, str_2, str_3]))

print(result)  # 👉️ "Bobby, Hadz"