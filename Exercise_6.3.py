def count(input_string, search_letter):
    count = 0
    for letter in input_string:
        if letter == search_letter:
            count = count + 1
    print count
usrstring = raw_input('Enter the String: ')
thechar = raw_input('What letter count are you searching for: ')
count(usrstring, thechar)
