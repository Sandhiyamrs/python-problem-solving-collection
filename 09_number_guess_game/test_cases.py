from solution_optimized import NumberGuessGame

game = NumberGuessGame(1, 1)
assert game.guess(1).startswith("Correct")

print("Number guessing game tests passed")
