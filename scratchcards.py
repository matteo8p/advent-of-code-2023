def parse_scratchcard(scratchcard): 
    scratchcard_splits = scratchcard.split(' ')
    winning_numbers = []
    your_numbers = []

    on_winning_numbers = True
    for i in range(2, len(scratchcard_splits)):
        scratchcard_splits[i] = scratchcard_splits[i].replace("\n", "")

        if scratchcard_splits[i] == '|': 
            on_winning_numbers = False
            continue
        if scratchcard_splits[i].isnumeric(): 
            if on_winning_numbers == True: 
                winning_numbers.append(int(scratchcard_splits[i]))
            else: 
                your_numbers.append(int(scratchcard_splits[i]))

    return winning_numbers, your_numbers

def num_matches(winning_numbers, your_numbers): 
    count = 0
    for number in your_numbers: 
        if number in winning_numbers: 
            count += 1
    return count

def scratchcards(): 
    scratchcards = open('data/scratchcards.txt', 'r').readlines()

    score = 0
    for scratchard in scratchcards: 
        winning_numbers, your_numbers = parse_scratchcard(scratchard)
        matches = num_matches(winning_numbers, your_numbers)
        if matches == 0: 
            continue
        score += 2 ** (matches - 1)

    return score


def main():
    print(scratchcards()); 

if __name__ == "__main__":
    main()