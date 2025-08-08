import sys

current_word = None
current_count = 0

# reading each line from standard input
for line in sys.stdin:
    # strip white spaces
    word, count = line.strip().split('\t')

    # convert count to int
    try:
        count = int(count)
    except ValueError:
        continue  # skipping invalid data

    # if current word = prev. word, increment count
    if current_word == word:
        current_count += count
    else:
        # if processing a new word, output the previous word and its count
        if current_word:
            print(f"{current_word}\t{current_count}")
        
        # reset current word and count
        current_word = word
        current_count = count

# output the last word and its count
if current_word == word:
    print(f"{current_word}\t{current_count}")