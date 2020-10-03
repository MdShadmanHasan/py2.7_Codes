def computegrade(score):
    if score > 0.0 and score < 1.0:
        if score > 0.9:
            return 'A'
        elif score > 0.8:
            return 'B'
        elif score > 0.7:
            return 'C'
        elif score > 0.6:
            return 'D'
        else:
            return 'F'
    else:
        return '\nBad score'
try:
    user_input = raw_input('Enter score: ')
    user_input = float(user_input)

    function_output = computegrade(user_input)
    print function_output
except:
    print '\nBad score'
