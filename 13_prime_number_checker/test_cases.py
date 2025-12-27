from solution_optimized import GuessGame

game = GuessGame(5, 5)
assert game.make_guess(5).startswith("Correct")
print("Guess game tests passed")
