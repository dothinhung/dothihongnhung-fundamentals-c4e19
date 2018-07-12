def rabbit(month):
    if month == 0:
        return(0)
    elif month == 1:
        return(1)
    else:
        return(rabbit(month-1) + rabbit(month-2))

month = 5
number_of_rabbit = 1

for i in range(month):
    numb = rabbit(i)
    number_of_rabbit += numb
    print(" Month {0} : {1} pair(s) of rabbit ".format(i, number_of_rabbit))