import random

def roll():
    return random.randint(1, 6)

def pig_dice_game():
    player_scores = [0, 0]
    current_player = 0
    winning_score = 50

    print("🎲 Welcome to the Pig Dice Game (Max 3 Rolls Per Turn)")

    while max(player_scores) < winning_score:
        print(f"\nPlayer {current_player + 1}'s turn:")
        turn_total = 0
        rolls = 0

        while rolls < 3:
            roll_val = roll()
            print(f"Roll {rolls + 1}: You rolled a {roll_val}")
            if roll_val == 1:
                print("😵 You rolled a 1! Turn over, no points added.")
                turn_total = 0
                break
            else:
                turn_total += roll_val
                rolls += 1
                print(f"Turn total: {turn_total}")
                if rolls < 3:
                    choice = input("Roll again? (y/n): ").lower()
                    if choice != 'y':
                        break
                else:
                    print("🔔 Max rolls reached!")

        player_scores[current_player] += turn_total
        print(f"Player {current_player + 1} total score: {player_scores[current_player]}")
        current_player = 1 - current_player

    print(f"\n🏆 Player {player_scores.index(max(player_scores)) + 1} wins with {max(player_scores)} points!")

pig_dice_game()
