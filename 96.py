import datetime


# def show_age(birth):
#     now = str(datetime.datetime.now()).split()[0]
#     thisyear = int(now[0:4])
#     age = thisyear - birth
#     print(age)
#
#
# a = int(input("Enter your birth year : "))
# show_age(a)

def show_age(birth):
    thisyear = int(datetime.datetime.now().strftime("%Y"))
    age = thisyear - birth
    print(age)


a = int(input("Enter your birth year : "))
show_age(a)
