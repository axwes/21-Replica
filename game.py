"""
Authors: Tan Yin Cheng
"""

import time
import random

def display_rules():
  print("""
  _____________________________________________________________________________
  Twenty One is a game of chance where players take turns rolling two dice every 
  round until they decide to stop rolling and lock in their score or end up 
  going bust with a total over 21. The objective is to be the closest to 21 
  when everyone is done rolling.

  Rules are as per follows:
    - Players begin with a score of 0.
    - Each player has one turn to either roll or stop rolling each round.
    - Players can only do a regular roll of two dice until they 
      reach a score of at least 14.
    - Players with a score >= 14 have the option to only roll one dice.
    - If a player scores more than 21 they go bust and are out of the game.
    - The winning player is the one with the score closest to 21 when everyone 
      has finished rolling.
    - If all players go bust, no one wins.
    - If more than one player has the winning score, no one wins.
  _____________________________________________________________________________
  """)
  input("Press enter to go back")
  return


def display_main_menu():
    print("------------Main Menu------------")
    print("Welcome to Twenty One!")
    print("1. Solo")
    print("2. Local Multiplayer")
    print("3. Rules")
    print("4. Exit")
    print("---------------------------------")


def int_input(prompt="", restricted_to=None):
    """
    Helper function that modifies the regular input method,
    and keeps asking for input until a valid one is entered. Input
    can also be restricted to a set of integers.

    Arguments:
        - prompt: String representing the message to display for input
        - restricted: List of integers for when the input must be restricted
                    to a certain set of numbers

    Returns the input in integer type.
    """
    while True:
        player_input = input(prompt)
        try:
            int_player_input = int(player_input)
        except ValueError:
            continue
        if restricted_to is None:
            break
        elif int_player_input in restricted_to:
              break

    return int_player_input


def cpu_player_choice(score):
    """
    This function simply returns a choice for the CPU player based
    on their score.

    Arguments:
    - score: Int

    Returns an int representing a choice from 1, 2 or 3.
    """
    time.sleep(2)
    if score < 14:
        return 1
    elif score < 17:
        return 3
    else:
        return 2

# ======================= TASK 1 ========================
def display_game_options(player):
    """
    Prints the game options depending on if a player's score is
    >= 14.

    Arguments:
      - player: A player dictionary object
    """

    print("------------" + player['name'] + "'s turn------------")
    print(player['name'] + "'s score: " + str(player['score']))
    print("1. Roll")
    print("2. Stay")
    if player['score'] >= 14:
        print("3. Roll One")


def display_round_stats(round, players):
    """
    Print the round statistics provided a list of players.

    Arguments:
      - round: Integer for round number
      - players: A list of player-dictionary objects
    """
    print("-----------Round " + str(round) + "-----------")
    for i in range(len(players)):
        print(str(players[i]["name"]) + " is at " + str(players[i]["score"]))

    return (round)

# ======================= TASK 2 ========================
import random
def roll_dice(num_of_dice=1):
    """
    Rolls dice based on num_of_dice passed as an argument.

    Arguments:
    - num_of_dice: Integer for amount of dice to roll

    Returns the following tuple: (rolls, display_string)
    - rolls: A list of each roll result as an int
    - display_string: A string combining the dice art for all rolls into one string
    """
    ##    raise NotImplementedError
    
    die_art = {
    1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
    2: ["┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"],
    3: ["┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
    4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
    5: ["┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
    6: ["┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"]
  }
    
    rolls = []
    for dice in range(num_of_dice):
        roll = random.randint(1,6)
        rolls.append(roll)

    display_string = ""
    for i in range(len(die_art[1])):
        for roll in rolls:
            display_string += die_art[roll][i]
        display_string += "\n"

    return (rolls, display_string)


# ======================= TASK 3 ========================
def execute_turn(player, player_input):
    """
    Executes one turn of the round for a given player.

    Arguments:
    - player: A player dictionary object

    Returns an updated player dictionary object.
    """
##    raise NotImplementedError
    
    if player_input == 1 or player_input == 3 :
        if player_input == 1:
            print("Rolling both...")
            roll = roll_dice(2)

        elif player_input == 3:
            print("Rolling one...")
            roll = roll_dice()


        
        score = sum(roll[0])
        print(roll[1])
        player['score'] += score
        print(player['name'] + " is now on " + str(player['score']))
        
        if player['score'] >= 14:
            player['at_14'] = True
            if player['score'] > 21:
                player['bust'] = True
                print(player['name'] + " goes bust!")
        
    elif player_input == 2:
        print(player['name'] + " has stayed with a score of " + str(player['score']))
        player['stayed'] = True

    return player


# ======================= TASK 4 ========================
def end_of_game(players):
    """
    Takes the list of all players and determines if the game has finished,
    returning false if not else printing the result before returning true.
    Arguments:
    - players: A list of player-dictionary objects
    Returns True if round has ended or False if not. If true results are
    printed before return.
    """
##    raise NotImplementedError
    highest = 0
    stayed = 0
    busted = 0
    for player in players:
        if player['stayed'] == True:
            stayed += 1
        if player['score']<= 21 and player['score']>highest:
            highest = player['score']
        elif player['score'] > 21:
            busted += 1

    total = busted + stayed

    if busted == len(players):
        print("Everyone's gone bust! No one wins :(")
        return True
    if total == len(players):
        winners = 0
        winner = None
        for player in players:
            if player['score'] == highest:
                winners += 1
                winner = player['name']

        if winners == 1:
            print(winner + " is the winner!")
            return True
        elif winners > 1:
            print("The game is a draw! No one wins :(")
            return True

    return False

# ======================= TASK 5 ========================
def solo_game():
    """
    This function defines a game loop for a solo game of Twenty One against
    AI.
    """
##    raise NotImplementedError
    player = {'name': 'Player 1', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}
    cpu_player = {'name': 'CPU Player', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}
    rounds = 0
    players = [player, cpu_player]

    while True:
        display_round_stats(rounds, players)
        if player['bust'] != True:
            display_game_options(player)
            if player['score'] >=14:
                player_input = int_input('Enter an option: ', [1,2,3])
            else:
                player_input = int_input('Enter an option: ', [1, 2])

            player = execute_turn(player, player_input)
        
        if cpu_player['bust'] != True:
            display_game_options(cpu_player)
            cpu_move = cpu_player_choice(cpu_player['score'])
            cpu_player = execute_turn(cpu_player, cpu_move)

        players = [player, cpu_player]

        if end_of_game(players):
            break
        else:
            rounds += 1

        
# ======================= TASK 6 ========================
def multiplayer_game(num_of_players):
    """
    This function defines a game loop for a local multiplayer game of Twenty One,
    where each iteration of the while loop is a round within the game.
    """
##    raise NotImplementedError

    players = []
    for i in range(1, num_of_players+1):
        player_name = "Player " + str(i)
        player = {'name': player_name, 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}
        players.append(player)

    rounds = 0
    while True:
        for i in range(len(players)):
            if players[i]['bust'] == False:
                display_round_stats(rounds, players)
                display_game_options(players[i])

                if players[i]['score'] >= 14:
                    player_input = int_input('Enter an option: ', [1, 2, 3])
                else:
                    player_input = int_input('Enter an option: ', [1, 2])
                player = execute_turn(players[i], player_input)
                players[i] = player
            else:
                continue

        if end_of_game(players):
            break
        else:
            rounds += 1

# ======================= TASK 7 ========================

def main():
    """
    Defines the main loop that allows the player to start a game, view rules or quit.
    """
##    raise NotImplementedError

    while True:
        display_main_menu()

        choice = int_input("Please enter your option: ", [1,2,3,4])

        if choice == 1:
            solo_game()
        elif choice == 2:
            num_of_players = int(input("Please enter the number of players: "))
            multiplayer_game(num_of_players)
        elif choice == 3:
            display_rules()
        elif choice == 4:
            break

main()

