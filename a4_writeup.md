# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?

Making the check diagonal function as instead of the col and row functions where theres a pattern, (pos, pos + 1, pos + 2) for row and (pos, pos + 3, pos + 6) for col, the two separate diagonals don't have a perfect pattern, so I had to make two seperate cases split with true or false.

2. Explain how you would add a computer player to the game.

Write an if statement for when turn is what the computer's turn should be, and instead of asking for a move the computer would think of a move and use the make move function to carry it out.

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.

First, check horizontals diagonals and verticals to see if two of the computers squares are in there, if there are, computer plays in the third square and wins. Then do the same thing but for the opponent, where it see if two of the oppenents squares are in horizontals diagonals and verticals and if there are, the computer plays in the third square to block the loss. Finally, look one of the computers piece, find a row column or diagonal that has no other pieces and is connected to that piece, and place computers piece there attempting to make a chain of three. If none of those work, just pick a random empty spot and place the piece there. While this system is not perfect, its very effective and much easier to implement than something like simulating all outcomes and picking the move that has the highest chance to lead to a win after every move (something like minimax).