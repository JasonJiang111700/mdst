"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if(num%2 == 0):
        print ("even")
    else:
        print ("odd")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    random_number = random.randrange(1,10,1)
    user_input = input("Guess the number: ")
    while(user_input != "exit"):
        if(int(user_input) > random_number):
            print("Too high")
        elif(int(user_input) < random_number):
            print("Too low")
        else:
            print("Exactly right")
        user_input = input("Guess the number: ")


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    palindrome = True
    for i in range(0, int(len(string)/2) + 1):
        if(string[i] != string[int(len(string))-i-1]):
            palindrome = False
    print(palindrome)

def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    encodedBytes = base64.b64encode(username.encode("utf-8"))
    encodedUser = str(encodedBytes, "utf-8")
    encodedBytes = base64.b64encode(password.encode("utf-8"))
    encodedPass = str(encodedBytes, "utf-8")
    file = open(filename, "w")
    file.write(encodedUser)
    file.write("\n")
    file.write(encodedPass)
    file.close()
    
    
def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    file_object = open(filename, "r")
    encodedUser = file_object.readline()
    encodedPass = file_object.readline()
    message_bytes = base64.b64decode(encodedUser)
    decryptedUser = message_bytes.decode("utf-8")
    message_bytes = base64.b64decode(encodedPass)
    decryptedPass = message_bytes.decode("utf-8")
    print(decryptedUser)
    print(decryptedPass)
    file_object.close()
    if(password != None):
        part4a(filename,decryptedUser,password)
        


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
