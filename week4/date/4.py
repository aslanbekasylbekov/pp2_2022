import datetime
date1 = datetime.datetime.now()
date2 = datetime.datetime(2022,2,27,18,33,30)
difference = date1 - date2
print(difference.seconds)