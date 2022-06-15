# TASK 1 ----------------------------

# QUESTION 1

# is_it_raining = input("Is it raining outside today? y for yes, n for no answers only please.")
#
# if is_it_raining == "y":
#     print("Take an umbrella.")
# else:
#     print("You don't need an umbrella.")

# QUESTION 2

# the correct code for question 2
#
# my_money = int(input("How much money do you have?"))
# boat_cost = 20 + 5
#
# if my_money < boat_cost:
#     print("You cannot afford the boat hire")
# else:
#     print("You can afford the boat hire")


# QUESTION 3
#
# def find_century(year_written):
#     if year_written[:2] == "18":
#         return "Nineteenth Century" # NB - there is a mistake in the Question - 1800s is 19th century
#     elif year_written[:2] == "19":
#         return "Twentieth Century" # NB there is a mistake in the question, 1900s is 20th century
#     else:
#         return "We do not stock books in this century - check again"
#
# def find_decade(year_written):
#     if year_written[2:3] == "0":
#         return "Noughties"
#     elif year_written[2:3] == "1":
#         return "Tens"
#     elif year_written[2:3] == "2":
#         return "Twenties"
#     elif year_written[2:3] == "3":
#         return "Thirties"
#     elif year_written[2:3] == "4":
#         return "Fourties"
#     elif year_written[2:3] == "5":
#         return "Fifties"
#     elif year_written[2:3] == "6":
#         return "Sixties"
#     elif year_written[2:3] == "7":
#         return "Seventies"
#     elif year_written[2:3] == "8":
#         return "Eighties"
#     elif year_written[2:3] == "9":
#         return "Nineties"
#     else:
#         return "Something has gone wrong - please check year format is in YYYY"
#
# book_year = input("What year was the book written in?")
# century_written = find_century(book_year)
# decade_written = find_decade(book_year)
#
# print(f"{century_written}, {decade_written}")

# TASK 2 -----------------------------------------

# QUESTION 1

# shopping_list = [
# "oranges",
# "cat food",
# "sponge cake",
# "long-grain rice",
# "cheese board"]
#
# print(shopping_list[0])

# QUESTION 2

# chocolates = {
# 'white': 1.50,
# 'milk': 1.20,
# 'dark': 1.80,
# 'vegan': 2.00
# }
#
# chocolate_type = input("Which chocolate are you selling?")
# print(chocolates[chocolate_type])

# QUESTION 3

# import random
#
# def prize_awarded(number_of_matches):
#     if number_of_matches < 3:
#         print("You have not won a prize this time.")
#     elif number_of_matches == 3:
#         print("Congratulations! You have won £20!")
#     elif number_of_matches == 4:
#         print("Congratulations! You have won £40!")
#     elif number_of_matches == 5:
#         print("Congratulations! You have won £100!")
#     elif number_of_matches == 6:
#         print("Congratulations! You have won £10000!")
#     elif number_of_matches == 7:
#         print("Congratulations! You have won £1000000!")
#     else:
#         print("Invalid number of matches")
#
#
# lottery_ticket = [3 , 5,  34 , 20 , 19 , 42 , 12]
# random_numbers = random.sample(range(1,60),7)
# print(random_numbers)
# match_count = 0
#
# for ticket_number in lottery_ticket:
#     if ticket_number in random_numbers:
#         match_count += 1
#
# prize_awarded(match_count)
# print(match_count)

# TASK 3 ---------------------------------------

# QUESTION 2

# poem = 'I like Python and I am not very good at poems'
#
# with open('poem.txt', 'w') as poem_file:
#     poem_file.write(poem)

# QUESTION 3

# import os.path
#
# lyrics = "You could never know what it's like \n" \
#          "Your blood like winter freezes just like ice \n" \
#          "And there\'s a cold lonely light that shines from you \n" \
#          "You'll wind up like the wreck you hide behind that mask you use \n" \
#          "And did you think this fool could never win? \n" \
#          "Well look at me, I'm coming back again \n" \
#          "I got a taste of love in a simple way \n" \
#          "And if you need to know while I'm still standing, you just fade away \n" \
#          "Don't you know I'm still standing better than I ever did \n" \
#          "Looking like a true survivor, feeling like a little kid \n" \
#          "I'm still standing after all this time \n" \
#          "Picking up the pieces of my life without you on my mind \n" \
#          "I'm still standing (Yeah, yeah, yeah) \n" \
#          "I'm still standing (Yeah, yeah, yeah) \n"
#
# with open("song.txt", "w") as file:
#     file.write(lyrics) # writing the lyrics to a new file
#
#
# if os.path.isfile("song.txt"):
#     print ("File exists")
# else:
#     print ("File not exist") # checking the file has been successfully created
#
# with open("song.txt", "r") as file:
#     for line in file:
#         line2 = line.strip().lower()
#         line2 = line.translate(line.maketrans("", "", '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
#         if " still " in line2:
#             print(line) # printing the lines with still

# TASK 4 ----------------------------

# Question 1

# import requests
#
# list_of_pokemon = ["1","2","3","4","5","6"]
# endpoint_without_number = "https://pokeapi.co/api/v2/pokemon/"
#
# for pokemon in list_of_pokemon:
#     endpoint = endpoint_without_number + pokemon
#     response = requests.get(endpoint)
#     data = response.json()
#     pokemon_name = data["name"]
#     pokemon_moves_list = [dictionary["move"]["name"] for dictionary in data["moves"]]
#     with open("pokemon.txt", "w") as file:
#         file.write(f"\n \n Pokemon Name: {pokemon_name} \n "
#                    f"Pokemon Moves: " + ", ".join(pokemon_moves_list))

# Question 2

# import requests
# from pprint import pprint as pp
#
# amount_questions = input("How many questions woud you like?")
# endpoint1 = f"https://opentdb.com/api.php?amount={amount_questions}"
#
# response = requests.get(endpoint1)
# data = response.json()
# pp(data) # print to see the output data

