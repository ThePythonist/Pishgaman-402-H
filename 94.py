def make_files(number, ext):
    for i in range(number):
        open(f"file{i+1}.{extention}", "w")

    print("Done")


number = int(input("How many files do you want ? "))
extention = input("File format : ")

make_files(number, extention)
