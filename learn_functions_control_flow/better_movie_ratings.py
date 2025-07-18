# Improve the movie rating meanings with user prompting

# take user input for film rating but allow invalid response
def take_input():
    possible_film_ratings = ["universal", "pg", "12", "12a", "15", "18"]
    print(f'Possible movie ratings are: {possible_film_ratings}')
    film_rating = input("What is your film rating? ")
    return film_rating

# take user input for film rating but only allow options from list
def check_input():
    possible_film_ratings = ["universal", "pg", "12", "12a", "15", "18"]
    input_good = False
    while not input_good:
        print(f'Possible movie ratings are: {possible_film_ratings}')
        film_rating = input("What is your film rating? ")
        if film_rating in possible_film_ratings:
            input_good = True
        else:
            print("Please pick from the list.")
    return film_rating

def rating_info(film_rating):
    # use an if statement to check for "universal" rating
    #   IF STATEMENT GOES HERE
    if film_rating == "universal":
        print("all age groups can watch this film")
    # check if film rating is "pg"
    elif film_rating == "pg":
        print("General viewing, but some scenes may be unsuitable for young children.")
    # check if film rating is "12" or "12a"
    elif film_rating == "12" or film_rating == "12a":
        print("Films classified 12A and video works classified 12 contain material that is not generally "
              "suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless "
              "accompanied by an adult.")
    # check if film rating is "15"
    elif film_rating == "15":
        print("No one younger than 15 may see a 15 film in a cinema.")
    # check if film rating is "18"
    elif film_rating == "18":
        print("No one younger than 18 may see an 18 film in a cinema.")
    else:
        print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")


end = False
while not end:
    film_rating = take_input()
    rating_info(film_rating)
    good_input = False
    while not good_input:
        another_rating = input("Would you like to check another movie rating? Y/N: ")
        if another_rating.lower() == "y":
            good_input = True
        elif another_rating.lower() == "n":
            good_input = True
            end = True
        else:
            print("Please enter Y or N")