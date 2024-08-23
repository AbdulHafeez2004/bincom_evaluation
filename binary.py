import random
binary_no = [str(random.randint(0, 1)) for no in range(4)]
binary_string = ''.join(binary_no)
print('Generated Binary Number:', binary_string)

no_in_base10 = int(binary_string, 2)
print('Converted Base 10 Number:', no_in_base10)