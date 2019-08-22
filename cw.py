
# ### Problem 1:
# Create a program that prints the user input until they enter 'q' to quit.
userInput = input("Enter a word.")
while userInput != 'q':
    print (userInput)
    userInput = input("Enter another word or q to quit.")

# KENN SAID SKIP
# ### Problem 2:
# Ask the user for their name. Then ask the user for a number of times they want their name printed.
# Print the number of times the user want their name printed. If they enter a negative or zero, tell them to ask again.

#
# ### Problem 3:
# Create a program that takes user input in a while loop. If they enter 1, print 1.
# If they enter 2, print 2. If they enter 3 print 3.
# If they enter ‘q’ or 0 (yo ur choice), quit. Else, print “ERROR”.

userInput2 = input('Enter 1, 2, or 3 or q to quit')
while userInput2 != "q":

    if userInput2 == "1":
        print (1)

    if userInput2 == "2":
        print (2)

    elif userInput2 == "3":
        print (3)

    elif userInput2 == "":
        print (ERROR) # you should print error if they enter anything other than 1-3

    userInput2 = input("'Enter 1, 2, or 3 or q to quit'")


#
# ### Problem 4:
# Create a program that takes the user input until they enter 'q'.
# You should store all of their input and separate the input with a comma. Once they enter 'q',
# print all of the comma separated words they entered.
