def show_pn(pn):
    if len(pn) == 11 or len(pn) == 10:
        if pn[0] == "0":
            pn = pn.replace("0", "+98", 1)
        else:
            pn = f"+98{pn}"
    else:
        print("Phone number must have 11 digits")

    print(pn)


show_pn(input("Enter your phone number : "))
