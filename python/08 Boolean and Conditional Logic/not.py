# age = 10
# age < 4 #false

# not age < 4 # true

age = 21

#age groups
#2-8 : $2 ticket
#65: $5 ticket
# $10 for rest
        #true because not           
        #false                      #false
if not ((age >= 2 and age <= 8) or age >= 65):
    print("you pay $10 and are not a child or senior")
else:
    print("you are a child or senior!")