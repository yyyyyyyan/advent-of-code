def scratchcards(puzzle_input):
    cards = puzzle_input.strip().split("\n")
    result = 0
    for card in cards:
        number_sets = card.split("|")
        winning_numbers = set(number_sets[0].split()[2:]) & set(number_sets[1].split())
        if winning_numbers:
            result += 2 ** (len(winning_numbers) - 1)
    return result


def scratchcards_final(puzzle_input):
    cards = puzzle_input.strip().split("\n")
    cards_amount = {}
    total_cards = len(cards)
    for card_number, card in enumerate(cards):
        cards_amount[card_number] = cards_amount.get(card_number, 1)
        number_sets = card.split("|")
        winning_numbers = set(number_sets[0].split()[2:]) & set(number_sets[1].split())
        if winning_numbers:
            for repeated_card_number in range(
                card_number + 1, card_number + len(winning_numbers) + 1
            ):
                if repeated_card_number >= total_cards:
                    break
                cards_amount[repeated_card_number] = (
                    cards_amount.get(repeated_card_number, 1)
                    + cards_amount[card_number]
                )
    return sum(cards_amount.values())
