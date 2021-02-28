# ask for age
print("How old are you?")
age = input()


# if age != "":
#         #18-21 wristbands
# age = int(age)
#     if age >= 18 and age <= 21:
#         print("You can enter but need a wristband!")

#     #21+ drink, normal entry
#     elif age >= 21:
#         print("You are good to enter and can drink!")

#     # too young, sorry
#     else:
#         print("You can't enter little one!! :(")
# else:
#     print("Please enter an age!")


# if age:
#     age = int(age)
#     #18-21 wristbands
#     if age >= 18 and age <= 21:
#         print("You can enter but need a wristband!")

#     #21+ drink, normal entry
#     elif age >= 21:
#         print("You are good to enter and can drink!")

#     # too young, sorry
#     else:
#         print("You can't enter little one!! :(")
# else:
#     print("Please enter an age!")

if age:
    age = int(age)
    # 18-21 wristbands
    if age >= 21:
        print("You can enter and drink!")

    # 21+ drink, normal entry
    elif age >= 18:
        print("You can enter but need a wristband!!")

    # too young, sorry
    else:
        print("You can't enter little one!! :(")
else:
    print("Please enter an age!")
