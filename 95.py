import datetime

now = str(datetime.datetime.now())
time = now.split()[1]

print(time[:5])
