x = 10
formatted = f"I've told you {x} times already!"

guess = 8
print(f"your guess of {guess} was incorrect")
print(f"your guess of {guess + 1} was incorrect")


# the tried and true way .format method
x = 10
formatted = "I've told you {} times already!!".formatted(10)

# The old way % operator
x = 10
formatted = "I've told you %d times already" % (x)