def score_card(card):
    total = 0
    next_cards = 0
    card = card.split("|")
    winning_numbers = card[0].lstrip(":").split()
    numbers = card[1].split()

    for i in winning_numbers:
        if i in numbers and total != 0:
            total *= 2
            next_cards += 1
        elif i in numbers:
            total = 1
            next_cards += 1

    return total, next_cards


def get_card(all_cards, card, current_card_count, total):
    current_total, next_cards = score_card(card)
    for i in range(1, next_cards + 1):
        if i + current_card_count == len(all_cards):
            return 0
        else:
            total = get_card(all_cards, all_cards[current_card_count + i],current_card_count + 1 , total)
    return total + current_total


if __name__ == '__main__':
    f = open("Input_1.txt", 'r')
    lines = f.readlines()

    sum_totals = get_card(lines, lines[0], 0, 0)

    print(sum_totals)