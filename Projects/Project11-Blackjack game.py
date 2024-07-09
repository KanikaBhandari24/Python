import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
#ACE=11, JACK, QUEEN, KING = 10 EACH
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal():
    """RETURNS A RANDOM CARD FROM THE DECK"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card    #FUNCTION WITH OUTPUT

def calculate(cards):
    """TAKE A LIST OF CARDS AND RETURN THE SCORE CALCULATED FROM THE CARDS"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🤷‍♂️"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😢"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😔"
    elif computer_score > 21:
        return "Opponent went over. You win 🤩"
    elif user_score > computer_score:
        return "You win 🤩"
    else:
        return "You lose 😢"

def play():
    user = []
    computer = []
    game_over = False

    for _ in range(2):
        new = deal()
        user.append(new)
        computer.append(deal())

    #FOR THE USER 
    while not game_over:
        user_score = calculate(user)
        computer_score = calculate(computer)
        print(f"Your cards: {user}, current score: {user_score}")
        print(f"Computer's first card: {computer[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True   #GAME ENDS
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ")
            if user_should_deal == "y":
                user.append(deal())
            else:
                game_over = True  #GAME ENDS

    #FOR THE COMPUTER SO THAT THE DEALER COULD FOLLOW THE STRATEGY
    while computer_score !=0 and computer_score < 17:
        computer.append(deal())
        computer_score = calculate(computer)

    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? 'y' or 'n':") == "y":
    play()
    



