import random
import string
def generatePassword(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)]
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)
def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numPasswords) + " passwords")
    print("Minimum length of password should be 4")
    passwordLengths = []
    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + ": "))
        if length < 4:
            print("Password length too short. Setting to minimum length of 4.")
            length = 4
        passwordLengths.append(length)
    for i in range(numPasswords):
        password = generatePassword(passwordLengths[i])
        print("Password #" + str(i+1) + " = " + password)
main()