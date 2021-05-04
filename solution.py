def solution(D):
    x = None
    output = {'Mon': x, 'Tue': x, 'Wed': x, 'Thu': x, 'Fri': x, 
        'Sat': x, 'Sun': x}
    day_tuple = list(output.keys())
    
    for date, val in D.items():
        tmp = date.split('-')

        yyyy = int(tmp[0])
        mm = int(tmp[1])
        dd = int(tmp[2])

        day = date_to_day(dd, mm, yyyy)

        if output[day] is x:
            output[day] = val
        else:
            output[day] += val

    for i in range(1, len(output)):
        if output[day_tuple[i]] is x:
            output[day_tuple[i]] = 2*output[day_tuple[i-1]] - output[day_tuple[i-2]] 

    return output

def date_to_day(dd, mm, yyyy):
    c = int(yyyy / 100)
    y = yyyy % 100

    if (mm <= 2):
        y -= 1
        mm += 10
    else:
        mm -=2

    day = (dd + int(2.6*mm - 0.2) - 2*c + y + int(y/4) + int(c/4)) % 7
    day_tuple = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
    
    return day_tuple[day]