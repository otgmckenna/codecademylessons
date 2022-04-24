#Provided lists below
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Original code begins here

#Combining letters and points to form letters_to_points dict
letter_to_points = {letters:points for letters, points in zip(letters, points)}
#Creating a key:value pair for blank tiles (tiles without a letter/point value)
letter_to_points[""] = 0

#Defining a function score_word that will calculate the point total of a given word
def score_word(word):
    point_total = 0
    for letters in word:        #for loop that checks the score of each letter in the given word
        point_total += letter_to_points.get(letters, 0)         #adds the point value of each letter in given word to point total
    return point_total

#test word to make sure above function works as intended
brownie_points = score_word("BROWNIE")
print(brownie_points)

#New dictionary mapping the words played by players. Spaced out to be easily read
players_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"], 
    "wordNerd": ["EARTH", "EYES", "MACHINE"], 
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
    }
#creating empty dictionary that will eventually host the points for each player
player_to_points = {}

#creating for loop to iterate through players' words to total the score of each
for player, words in players_to_words.items():  #for loop to being assigning keys:values to player_to_points dictionary
    player_points = 0                           #sets default score to 0
    for word in words:                          #for loop to check each word in the values of the players_to_words dictionary
        player_points += score_word(word)       #calls back to the above score_word function to calculate the score of each word
    player_to_points[player] = player_points    #adds the above points to the dictionary with player as the key and player_points as the value

print(player_to_points)     #prints the updated player_to_points dictionary with the correct point totals