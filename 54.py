ages = {
    "meysam": 20,
    "saman": 40,
    "helia": 32,
    "hossein": 43,
    "kian": 17,
}

oldest = max(ages.values())

# for i in ages:
#     if ages[i] == oldest:
#         print(i)

for k, v in ages.items():
    if v == oldest:
        print(k)
