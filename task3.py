import sys

arguments = sys.argv[1:]

uppercase = [char.isupper() for char in arguments[0]]
uppercase_count = sum(uppercase)

lowercase = [char.islower() for char in arguments[0]]
lowercase_count = sum(lowercase)

print("Uppercase letters count: ", uppercase_count)
print("Lowercase letters count: ", lowercase_count)