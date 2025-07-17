# Use 'while loop' to verify user 'age' input

# SET VARIABLE user_prompt TO TRUE
user_prompt = True
# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt:
    age = input("What is your age? ")
    # PUT IF STATEMENT HERE TO CHECK IF age IS ALL DIGITS
    if age.isdigit() and int(age) <= 117:
        # SET user_prompt TO FALSE
        user_prompt = False
    elif age.isdigit() and int(age) > 117:
            print("You're not that old, try again")
    # ADD ELSE STATEMENT HERE
    else:
        # TELL USER THE PROBLEM WITH THEIR INPUT
        print("Please enter a number")

print(f"Your age is {age}")
