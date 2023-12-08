def score_card(card):
    # Extracts winning numbers and card numbers
    winning_numbers, numbers = card.split("|")
    winning_numbers = winning_numbers.lstrip(":").split()
    numbers = numbers.split()

    # Count how many winning numbers are in the card's numbers
    matching_numbers = sum(1 for num in winning_numbers if num in numbers)

    return matching_numbers

def count_cards(all_cards, card_index):
    # Base case: if the current index is beyond the list length, stop the recursion
    if card_index >= len(all_cards):
        return 0

    # Count the matching numbers for the current card
    next_cards = score_card(all_cards[card_index])

    # Count the current card
    total_cards = 1

    # Recursively count the cards for each next card
    for i in range(1, next_cards + 1):
        next_card_index = card_index + i
        if next_card_index < len(all_cards):
            total_cards += count_cards(all_cards, next_card_index)

    return total_cards

if __name__ == '__main__':
    with open("Input_1.txt", 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    total_cards_counted = count_cards(lines, 0)
    print(total_cards_counted)
