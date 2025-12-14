import random

# --- Game Setup ---

# 1. Choose a game type: Guessing Game (The Guessing Game🎮)

def start_game():
    """Initializes and runs the main game loop."""
    print("🔮 Welcome to The Guessing Game🎮! 🔮")
    print("You must solve the riddles and guess the secret numbers to escape.")
    print("You have a limited number of attempts per level. Good luck!")
    print("-" * 30)

    # Dictionary to hold the secret numbers for each level
    levels = {
        1: {'number': 7, 'range': 10, 'attempts': 3, 'hint': "It's an odd prime number and near to 10."},
        2: {'number': 25, 'range': 50, 'attempts': 3, 'hint': "It's the square of half of 10."},
        3: {'number': 144, 'range': 200, 'attempts': 3, 'hint': "The number of eggs in a gross, or 12 squared."},
        4: {'number': 1024, 'range': 1500, 'attempts': 3, 'hint': "A common number used in computer memory (bytes/kilobytes)."},
        5: {'number': 512, 'range': 1000, 'attempts': 3, 'hint': "The smallest power of 2 just greater than 500."}
    }

    current_level = 1
    max_level = len(levels)

    # 2. Define the game rules and logic (main loop)
    while current_level <= max_level:
        level_data = levels[current_level]
        secret_number = level_data['number']
        max_range = level_data['range']
        attempts_left = level_data['attempts']
        
        print(f"\n✨ Entering **Level {current_level}** of {max_level} ✨")
        print(f"I'm thinking of a number between 1 and {max_range}.")
        print(f"Hint: {level_data['hint']}")
        
        level_complete = False
        
        # 3. Use conditional statements to manage game flow (inner loop)
        while attempts_left > 0:
            print(f"Attempts left: {attempts_left}")
            
            try:
                # Get user input
                guess = int(input("Your guess: "))
            except ValueError:
                print("⚠️ Invalid input. Please enter a whole number.")
                continue # Skip the rest of the loop and start over
            
            # Check the guess using conditional statements
            if guess == secret_number:
                print(f"🎉 **Correct!** The secret number was {secret_number}. You have mastered Level {current_level}!")
                level_complete = True
                break # Exit the inner while loop
            elif guess < secret_number:
                print("Too low! The Enigma whispers a larger number.")
            else: # guess > secret_number
                print("Too high! The Enigma demands a smaller number.")
                
            attempts_left -= 1
        
        # Check if the player failed the level
        if not level_complete:
            print(f"\n💀 **Game Over!** You failed to solve Level {current_level}.")
            print(f"The secret number was **{secret_number}**.")
            return # Exit the entire function/game
        
        # Move to the next level
        current_level += 1

    # If the player completes all levels
    print("\n👑 **CONGRATULATIONS!** You have conquered The Guessing Game🎮!")
    print("You are a master of logic and intuition!")

# 4. Test and debug the game for correctness (calling the function)
if __name__ == "__main__":
    start_game()