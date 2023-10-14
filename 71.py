def transform(x):
    if len(str(x)) == 1:  # shart payan
        return x
    else:
        digits = [int(i) for i in str(x)]
        x = sum(digits)
        return transform(x)


print(transform(345345))
