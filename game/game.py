import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardDeck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
        else:
            print("Card not found in the deck.")

    def draw_card(self):
        if self.cards:
            return random.choice(self.cards)
        else:
            print("No cards in the deck.")
            return None

card1 = Flashcard("What is the capital of France?", "Paris")
card2 = Flashcard("What is the tallest mountain in the world?", "Mount Everest")
card3 = Flashcard("What is 2 + 2?", "4")
card4 = Flashcard("What is the capital of Japan?", "Tokyo")
card5 = Flashcard("Who wrote 'Romeo and Juliet'?", "William Shakespeare")
card6 = Flashcard("What is the chemical symbol for water?", "H2O")
card7 = Flashcard("What is the largest planet in our solar system?", "Jupiter")
card8 = Flashcard("Who painted the Mona Lisa?", "Leonardo da Vinci")
card9 = Flashcard("What is the powerhouse of the cell?", "Mitochondria")
card10 = Flashcard("What year did the Titanic sink?", "1912")

deck = FlashcardDeck()
deck.add_card(card1)
deck.add_card(card2)
deck.add_card(card3)
deck.add_card(card4)
deck.add_card(card5)
deck.add_card(card6)
deck.add_card(card7)
deck.add_card(card8)
deck.add_card(card9)
deck.add_card(card10)

while True:
    input("Press Enter to draw a card...")
    card = deck.draw_card()
    if card:
        print("Question:", card.question)
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == card.answer.lower():
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", card.answer)
    else:
        print("No more cards in the deck. Exiting...")
        break
