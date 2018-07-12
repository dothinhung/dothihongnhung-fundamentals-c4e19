bacterias = int(input("How many B Bacterias are there? "))
time = int(input("How much time will we waits (minutes)? "))
rep = bacterias * 2 ** (time//2)
print ("After {0} minutes(s) we would have {1} B Bacterias".format(time, rep))

