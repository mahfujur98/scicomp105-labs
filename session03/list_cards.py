#!/usr/bin/env python3
# list_cards_instructor.py

def init_deck():
    deck = [None] * 52
    for card_pos, card_num in enumerate(deck):
        deck[card_pos] = card_pos
    return deck


def card_name(card_num):
    suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank = ["Deuce", "Three", "Four", "Five", "Six",
            "Seven", "Eight", "Nine", "Ten", "Jack",
            "Queen", "King", "Ace"]

    name = (f"{rank[0]} of "
            f"{suit[0]}")

    return name


def display_deck(deck):
    for card_pos, card_num in enumerate(deck):
        print(f"The card in position {card_pos}"
              f" is the {card_name(card_num)}")


def main():
    deck = init_deck()
    display_deck(deck)


if __name__ == "__main__":
    main()
