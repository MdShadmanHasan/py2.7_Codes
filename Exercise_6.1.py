input_string = raw_input('Enter the string: ')
last_index = len(input_string) - 1
while last_index >= 0:
    letter = input_string[last_index]
    print letter
    last_index = last_index - 1

for character in input_string:
    print '\t', character
