# Problem - Rock Paper Scissors
# Link - https://adventofcode.com/2022/day/2
# Author - Ian Inglis

## Verbal breakdown of problem
# Assign values in the input to Rock, Paper, and Scissors
# Allocate these to points
# Determine the winner of each game
# Assign the points based on wins, losses, and choice picked


# These dictionaries define the inputs from the players and their corresponding game values
Player_1 = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

Player_2 = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

# This dictionary assigns points to the options
Score = {
    "Rock": 1,
    "Paper": 2, 
    "Scissors": 3
}


# Creating lists to store points and choices
# This can be done better, however this works for now 
Player_1_Score = []
Player_2_Score = []
Player_1_Choice = []
Player_2_Choice = []

# This brings in the input and splits the values individually 
Strategy = open('input.txt')
Strategy = ''.join(Strategy)
Strategy = Strategy.split()

# This breaks up the input so that the first column is player 1's choice to throw and the second column is player 2's choice to throw 
Player_1_Choice = Strategy[::2]
Player_2_Choice = Strategy[1::2]


# This horrible if/elif block allocates the points based on who wins
# I 100% believe there is a more efficient, and easier way to do this, however this verbose method gets the results needed 
for x in range(int(len(Strategy)/2)):
    if Player_1.get(Player_1_Choice[x]) == Player_2.get(Player_2_Choice[x]):
        Player_1_Score.append(3 + Score.get(Player_1.get(Player_1_Choice[x])))
        Player_2_Score.append(3 + Score.get(Player_1.get(Player_1_Choice[x])))
    elif Player_1.get(Player_1_Choice[x]) == "Rock" and Player_2.get(Player_2_Choice[x]) != "Paper":
        Player_1_Score.append(6 + Score.get(Player_1.get(Player_1_Choice[x]))) 
        Player_2_Score.append(0 + Score.get(Player_2.get(Player_2_Choice[x])))
    elif Player_1.get(Player_1_Choice[x]) == "Paper" and Player_2.get(Player_2_Choice[x]) != "Scissors":
        Player_1_Score.append(6 + Score.get(Player_1.get(Player_1_Choice[x])))
        Player_2_Score.append(0 + Score.get(Player_2.get(Player_2_Choice[x])))
    elif Player_1.get(Player_1_Choice[x]) == "Scissors" and Player_2.get(Player_2_Choice[x]) != "Rock":
        Player_1_Score.append(6 + Score.get(Player_1.get(Player_1_Choice[x])))
        Player_2_Score.append(0 + Score.get(Player_2.get(Player_2_Choice[x])))
    elif Player_2.get(Player_2_Choice[x]) == "Rock" and Player_1.get(Player_1_Choice[x]) != "Paper":
        Player_2_Score.append(6 + Score.get(Player_2.get(Player_2_Choice[x])))
        Player_1_Score.append(0 + Score.get(Player_1.get(Player_1_Choice[x])))
    elif Player_2.get(Player_2_Choice[x]) == "Paper" and Player_1.get(Player_1_Choice[x]) != "Scissors":
        Player_2_Score.append(6 + Score.get(Player_2.get(Player_2_Choice[x])))
        Player_1_Score.append(0 + Score.get(Player_2.get(Player_2_Choice[x])))
    elif Player_2.get(Player_2_Choice[x]) == "Scissors" and Player_1.get(Player_1_Choice[x]) != "Rock":
        Player_2_Score.append(6 + Score.get(Player_2.get(Player_2_Choice[x])))
        Player_1_Score.append(0 + Score.get(Player_1.get(Player_1_Choice[x])))

# This prints the values to get the answer required
print("Player 1's score is", sum(Player_1_Score))
print("Player 2's score is", sum(Player_2_Score))








