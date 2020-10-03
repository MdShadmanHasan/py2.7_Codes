try:
    hours = raw_input('Enter Hours: ')
    hours = float(hours)
    rate = raw_input('Enter Rate: ')
    rate = float(rate)
    if hours > 40:
        extra_hours = hours - 40
        pay = extra_hours * (rate * 1.5) + (40 * rate)
    else:
        pay = hours * rate
    print '\nPay: ', pay
except:
    print 'Error, please enter numeric input\n'
