#!/usr/bin/env python3
# dealer_bogus.py

import random


def init_deck():
    return list(range(52))


def card_name(card_num):
    suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank = ["Deuce", "Three", "Four", "Five", "Six",
            "Seven", "Eight", "Nine", "Ten", "Jack",
            "Queen", "King", "Ace"]

    card_name = (f"{rank[card_num % 13]} of "
                 f"{suit[card_num // 13]}")

    return card_name


def display_deck(deck):
    for card_pos, card_num in enumerate(deck):
        print(f"The card in position {card_pos}"
              f" is the {card_name(card_num)}")


def deal_cards(deck):
    for card_pos, card_num in enumerate(deck):
        new_card_num = random.randint(0, 51)
        deck[card_pos] = new_card_num


def main():
    random.seed(2016)
    deck = init_deck()
    deal_cards(deck)
    display_deck(deck)


if __name__ == "__main__":
    main()
