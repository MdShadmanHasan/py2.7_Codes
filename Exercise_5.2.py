count = 0
total = 0
average = 0
max_input = None
min_input = None
while True:
    user_input = raw_input('Enter a number: ')
    if user_input == 'done':
        break
    try:
        total = float(total) + int(user_input)
        count = count + 1
        average = total / count
        if max_input is None or user_input > max_input: #something is wrong here
            max_input = user_input
        if min_input is None or user_input < min_input:
            min_input = user_input
    except:
        print 'Invalid input'
        continue

print int(total), count, average, max_input, min_input
