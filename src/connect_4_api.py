import flask
from flask import request, jsonify
import json
from game import *


Players = (PIECE_ONE, PIECE_TWO)
Winner = None
Board = create_board()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/game/4connect/start', methods=['GET'])
def api_start():
	reset_board(Board)
	return jsonify("READY")


@app.route('/game/4connect/move/1/<col>', methods=['GET', 'POST'])
def api_player1_move(col):
	col = int(col)
	if(col < 0 or col > COLUMNS):
		return "INVALID"
	else:
		possible = drop_piece(Board, col, Players[0])
		if(possible == False):
			return jsonify("INVALID")
		Winner = find_winner(Board)
		if(Winner != None):
			
			reset_board(Board)
			return "{} wins".format(PIECE_COLOR_MAP[Winner])
		else:
			print_board(Board)
			return jsonify("VALID") #jsonify(Board)
	
	

@app.route('/game/4connect/move/2/<col>', methods=['GET'])
def api_player2_move(col):
	col = int(col)
	if(col < 0 or col > COLUMNS):
		return jsonify("INVALID")
	else:
		possible = drop_piece(Board, col, Players[1])
		if(possible == False):
			return jsonify("INVALID")
		# check the winner
		Winner = find_winner(Board)
		if(Winner != None):
			# return(jsonify(Board))
			reset_board(Board)
			return "{} wins".format(PIECE_COLOR_MAP[Winner])
		else:
			print_board(Board)
			return jsonify("VALID")#jsonify(Board)

def main():
	"""
		Use localhost:5000/game/start/ to create new game
		Use localhost:5000/game/move/<player-no>/<column> to play the move of the player-no on the specifed column number.  
	"""
	app.run()


if __name__ == "__main__":
	main()
