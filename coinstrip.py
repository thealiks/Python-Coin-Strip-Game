"""
Name: Alex Singh
UPI: asin374
ID: 687195036
Coin Strip Game

How to play: select and move a coin to the left, and try to be the player to get all coins in positions 1-4
"""
import math
import random

def create_game_string():
	game_string = " $ $ $ $ "
	for count in range(0,7):
		game_string = jumble_game_line(game_string)
	return game_string

def jumble_game_line(game_line):
	random_position = random.randrange(0,9)
	game_line = game_line[: random_position] + game_line[random_position + 1 :] + game_line[random_position]
	return game_line

def display_game_string(game_string):
	count = 0
	game_string = "  " + game_string[count] + "  |  " + game_string[1] + "  |  " + game_string[2] + "  |  " + game_string[3] + "  |  " + game_string[4] + "  |  " + game_string[5] + "  |  " + game_string[6] + "  |  " + game_string[7] + "  |  " + game_string[8] + "  " 
	output = "||     |     |     |     |     |     |     |     |     ||"
	print("")
	print("    1     2     3     4     5     6     7     8     9")
	print(output)
	print("||" + game_string + "||")
	print(output)
	print("")

def get_user_position_num(player_num):
	print("PLAYER NUMBER: " + str(player_num))
	position = int(input("Enter position number: "))
	return position - 1

def get_num_to_move():
	num_to_move = int(input("Enter number to move: "))
	return num_to_move

def move_dollar_to_the_left(game_string, position_number, to_move):
	new_position = position_number - to_move
	game_string = game_string[:new_position] + game_string[position_number] + game_string[new_position:position_number] + game_string[position_number + 1:]
	return game_string

def get_next_player_num(player_num):
	if player_num == 1:
		return 2
	return 1

def congratulate_player(player_num):
	output1 = "=" * 25
	output2 = "** Y O U H A V E W O N **"
	print(output1)
	print(output2)
	print("     PLAYER NUMBER: " + str(player_num))
	print(output2)
	print(output1)
	print("")

def check_game_finished(game_string):
	first_four_symbols = game_string[0:4]
	if first_four_symbols == "$$$$":
		return True
	return False

def play_one_game():
	player_num = 1
	game_finished = False
	game_string = create_game_string()
	while game_finished == False:
		display_game_string(game_string)
		position_num = get_user_position_num(player_num)
		move_num = get_num_to_move()
		game_string = move_dollar_to_the_left(game_string,
		position_num, move_num)
		game_finished = check_game_finished(game_string)
		if game_finished:
			display_game_string(game_string)
			congratulate_player(player_num)
		else:
			player_num = get_next_player_num(player_num)

def display_menu():
	print ("1. PLAY COIN STRIP")
	print ("2. EXIT")
	select = int(input("Enter selection: "))
	return select

def main():
	selection = display_menu()
	while selection == 1:
		play_one_game()
		selection = display_menu()
	if selection ==3:
		hello()
	print()
	print("BYE FROM COIN STRIP")

def hello():
	lst = [4,16,64,256]
	for num in lst:
		op1 = (num * math.log(num, 2)) + 6 * num
		op2 = (num * num) + (2 * num) + 1
		op3 = 25 + (10 * num)
		print(num, op1, op2, op3, sep="\t\t")
		
main()
