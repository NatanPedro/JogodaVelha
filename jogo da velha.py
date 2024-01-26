from random import randrange

def display_board(tabela):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(tabela[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def enter_move(tabela):
	ok = False
	while not ok:
		move = input("Faça o movimento: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9'
		if not ok:
			print("Má jogada – repita sua entrada!")
			continue
		move = int(move) - 1
		row = move // 3
		col = move % 3
		sign = tabela[row][col]
		ok = sign not in ['O','X'] 
		if not ok:
			print("Campo já ocupado – repita sua entrada!")
			continue
	tabela[row][col] = 'O' 

def make_list_of_free_fields(tabela):
	free = []	
	for row in range(3): 
		for col in range(3): 
			if tabela[row][col] not in ['O','X']: 
				free.append((row,col)) 
	return free

def victory_for(tabela,sgn):
	if sgn == "X":
		who = 'me'	
	elif sgn == "O": 
		who = 'you'	
	else:
		who = None	
	cross1 = cross2 = True  
	for rc in range(3):
		if tabela[rc][0] == sgn and tabela[rc][1] == sgn and tabela[rc][2] == sgn:	
			return who
		if tabela[0][rc] == sgn and tabela[1][rc] == sgn and tabela[2][rc] == sgn:
			return who
		if tabela[rc][rc] != sgn: 
			cross1 = False
		if tabela[2 - rc][2 - rc] != sgn: 
			cross2 = False
	if cross1 or cross2:
		return who
	return None

def draw_move(tabela):
	free = make_list_of_free_fields(tabela) 
	cnt = len(free)
	if cnt > 0:	
		this = randrange(cnt)
		row, col = free[this]
		tabela[row][col] = 'X'

tabela = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
tabela[1][1] = 'X' 
free = make_list_of_free_fields(tabela)
human_turn = True 
while len(free):
	display_board(tabela)
	if human_turn:
		enter_move(tabela)
		victor = victory_for(tabela,'O')
	else:	
		draw_move(tabela)
		victor = victory_for(tabela,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(tabela)

display_board(tabela)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")
