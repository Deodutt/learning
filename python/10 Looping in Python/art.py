# MY SOLUTIONS

# for num in range(1, 11):
#     print("\U0001f600" * num)

# num = 1
# while num < 11:
#     print("\U0001f600" * num)
#     num += 1

# code along solutions
# for num in range(1, 11):
#     print("\U0001f600" * num)

# times = 1
# while times < 11:
#     print("\U0001f600" * times)
#     times += 1


# for x in range(3):
#     for num in range(1, 11):
#     print("\U0001f600" * num)


for num in range(1, 11):
    count = 1
    smiley = ""
    while count <= num:
        smiley += "\U0001f600"
        count += 1
    print(smiley)