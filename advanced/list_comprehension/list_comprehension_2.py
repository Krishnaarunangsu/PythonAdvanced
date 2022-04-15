# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.


# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ['apple', 'banana', 'cherry', 'kwik', 'mango']


def get_fruits_a(fruits_mix: list):
    fruits_new = []
    for fruit in fruits_mix:
        if "a" in fruit:
            fruits_new.append(fruit)

    return fruits_new


fruits_with_a: list = get_fruits_a(fruits)
print("Without List Comprehension:", fruits_with_a)

# With List Comprehension
fruits_a = [fruit for fruit in fruits if "a" in fruit]
print("With List Comprehension:", fruits_a)
