lines = open("words.txt").readlines()
revlines = [i[::-1] for i in lines]

open("reversedwords.txt", "w").writelines(revlines)
