def shorten_to_date(long_date):
    s=0
    for i in long_date:
        if i !=',':
            s=s+1
        else:
            return long_date[0:s]

print(shorten_to_date("Monday February 2, 8pm"))
