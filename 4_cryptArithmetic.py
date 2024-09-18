from itertools import permutations

def crypt_arithmetic(puzzle):
    left, right = puzzle.split('==')
    words = left.split('+')
    
    letters = set(''.join(words) + right.strip())
    
    if len(letters) > 10:
        print("No solution found: More than 10 unique letters.")
        return
    
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        
        if any(mapping[word[0]] == 0 for word in words) or mapping[right.strip()[0]] == 0:
            continue
        
        left_value = sum(int(''.join(str(mapping[letter]) for letter in word)) for word in words)
        
        right_value = int(''.join(str(mapping[letter]) for letter in right.strip()))
        
        if left_value == right_value:
            print("Final Solution:")
            for letter in sorted(mapping.keys()):
                print(f"{letter} = {mapping[letter]}")
            return
    
    print("No solution found.")

puzzle = input("Enter the cryptarithmetic puzzle (e.g., SEND + MOST == SENSE): ")
crypt_arithmetic(puzzle)