# List Comprehension vs For Loop in Python

# Iterating through string Using for loop
h_letters = []

for letter in 'human':
    h_letters.append(letter)

print('Without List Comprehension:', h_letters)

"Iterating through a string Using List Comprehension"
h_letters_comprehended =[letter for letter in 'human']
print('With List Comprehension:', h_letters_comprehended);
