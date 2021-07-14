import os

startgame = True

game_model = {'moves': []}

flag = [True]

def clearConsole():
	command = 'clear'
	if os.name in ('nt', 'dos'):
		command = 'cls'
	os.system(command)

def move_translate(param):
	try:
		if int(param) < 10 and int(param) > 0:
			game_model['moves'].append(str(param))
		else:
			print('Wrong input. Try again.')
			return 'error'
	except:
		print('Wrong input format. Try again.')
		return 'error'

def game_state(firstMoveImmutable):
	if len(game_model['moves']) >= 5:
		pieces = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
		board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
		for move in game_model['moves']:
			if firstMoveImmutable == True:
				pieces[int(move)-1] = 'x'
				firstMoveImmutable = False
			else:
				pieces[int(move)-1] = 'o'
				firstMoveImmutable = True
		piecesIter = iter(pieces)
		for x in range(0,3):
			for j in range(0,3):
				board[x][j] = next(piecesIter)
		for y in range(0,3):
			if board[0][y] == board[1][y] == board [2][y]:
				if board[0][y] != ' ':
					return board[0][y]
			if board[y][0] == board[y][1] == board [y][2]:
				if board[y][0] != ' ':
					return board[y][0]
		if board[0][0] == board[1][1] == board [2][2]:
			return board[0][0]
		if board[0][2] == board[1][1] == board [2][0]:
			return board[0][2]
	return ''

def game_controller(param,turn,firstMoveImmutable):
	if param == 'r':
		return game_view('r',turn,firstMoveImmutable)
	elif next((x for x in game_model['moves'] if x == param), None) == None:
		if move_translate(param) != 'error':
			if turn[0] == True:
				turn[0] = False
			else:
				turn[0] = True
			return game_view(param,turn,firstMoveImmutable)
		else:
			return ''
	else:
		print('This position is already occupied!')

def game_view(status,turn,firstMoveImmutable):
	clearConsole()
	pieces = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	if status == 'r':
		return 'end'
	else:
		for move in game_model['moves']:
			if firstMoveImmutable == True:
				pieces[int(move)-1] = 'x'
				firstMoveImmutable = False
			else:
				pieces[int(move)-1] = 'o'
				firstMoveImmutable = True
	

	rules = 'If you want to resign - input "r"'
	info = '| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |'
	board = ['| '+pieces[0]+' | '+pieces[1]+' | '+pieces[2]+' |', '| '+pieces[3]+' | '+pieces[4]+' | '+pieces[5]+' |', '| '+pieces[6]+' | '+pieces[7]+' | '+pieces[8]+' |']
	answer = board[0] + '\n' + board[1] + '\n' + board[2] + '\n' + rules + '\n'
	answer = answer + info
	if game_state(firstMoveImmutable) == 'o' or game_state(firstMoveImmutable) == 'x':
		answer = 'Win!'
	return answer

while True:
	if startgame == True:
		clearConsole()
		print('Welcome to the game of tic tac toe !')
		if next((name_key for name_key in game_model if name_key == 'player1_name'),None)=='player1_name':
			pass
		else:
			print('Enter your names to start the game!')
			game_model['player1_name'] = input("First player's name: ")
			game_model['player2_name'] = input("Second player's name: ")
		print(game_view('',flag,True))
		startgame = False
	else:
		answer = game_controller(input((game_model['player1_name'] if flag[0] == True else game_model['player2_name']) + "'s move: "),flag,True)
		if answer == 'Win!':
			print(answer)
			print('To start a new game input anything.')
			input()
			game_model['moves'] = []
			startgame = True
			flag[0] = True
		elif answer != 'end':
			print(answer)
		else:
			print('Game is over!')
			print('To start a new game input anything.')
			input()
			game_model['moves'] = []
			startgame = True
			flag[0] = True