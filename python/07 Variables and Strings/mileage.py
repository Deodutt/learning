print("How many Kilometers did you run today?")
# kms = float(input())
kms = input()
miles = float(kms) / 1.60934
# turn KMS into a float

miles = round(miles, 2)
print(f"Your {kms} km run is equal to {miles} miles")
# print(f"That is equals to {round(miles, 2)} miles")


# round(thing to round, how many decimalpoints to round it)


# to round the decimal points