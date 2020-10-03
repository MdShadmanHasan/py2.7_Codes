#while True:
#    numberlist = []
#    numinput = int(raw_input('Enter a number:'))
#    numberlist.append(numinput)
#    if numinput == 'done':
#        break
#print numberlist
count = 0
total = 0
average = 0
while True:
    user_input = raw_input('Enter a number: ')
    if user_input == 'done':
        break
    try:
        total = float(total) + int(user_input)
        count = count + 1
        average = total / count
    except:
        print 'Invalid input'
        continue

print int(total), count, average
#oh god finally! done! After so many tries! But still feels good to have solved the problem!
