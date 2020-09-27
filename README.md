# Connect4-game-API
# How to run:
	-- run the python script connect_4_api.py

# Install the dependencies:
	Install the dependencies using following command:
			-- pip install -r requirements.txt
	



# Start the game
	To start the game:
		-- call the api -- "http://127.0.0.1:<port-number>/game/4connect/start"
		--normally the port is 5000 so the link will be like --"http://127.0.0.1:5000/game/4connect/start"

		--Hit the api link above to start a new game

		--Once we hit the api we get a response "READY" stating board is reset and we can start new game

	To make a move:
		--call the api -- "http://127.0.0.1:5000/game/4connect/move/<player-number>/<column-number>"

			player-number varies from 1 to 2
			column-number varies from 0 to 6

		--This returns the response for the following cases:

			(1) when either of the player wins, the respose is : "<Player-color> wins".

			(2) when the column number is invalid or the board is completely filled and no further move is possible, the response is -- [ "INVALID" ]

			(3) For each valid move, the response is "VALID" , and board is printed on the console.
