scores = {
    "riazi": (17, 3),
    "olom": (20, 3),
    "ejtemaei": (14, 2),
    "farsi": (12, 2),
    "arabi": (7, 1),
    "zaban": (19, 2)
}


def score_status(score):
    if scores[score][0] >= 10:
        print(score, "Passed")
    else:
        print(score, ": Failed")


def average(scores):
    nomarat = [i[0] * i[1] for i in scores.values()]
    vahedha = [i[1] for i in scores.values()]
    avg = sum(nomarat) / sum(vahedha)
    print(avg)


# ----------------------------------------

# Ghaboli
for i in scores:
    score_status(i)

# Miangin
average(scores)
