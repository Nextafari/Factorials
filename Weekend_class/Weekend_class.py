'''name = input("Enter your name: ")
age = input("enter your age: ")
result = ("my name is " + name + ", I am " + age + " years old")
print(result)'''

#The reverse function only works for lists, any other thing being used with the reverse function returns an attribut error
'''word = "ganja planter"
word_list = word.split()
print(word_list)'''

#The three examples below are examples of a for loop
'''for numbers in range(11):
    print(numbers)'''

'''name = "Olympus"
for letter in name:
    print(letter)'''

'''for i in range(100):
    print("Damian Marley")'''

#Using the reverse function by first converting the string to a list and reconverting to a string
'''word = input("Enter a word: ")
characters = []
for letter in word:
    characters.append(letter)
characters.reverse()
new_word = "".join(characters)
print(new_word)'''


''' 
Demonstrating the use of While LOOP 
'''
'''value = input("Begin Chat: ")
while value != "because":
    print("why?")
    value = input("Enter message: ")'''


word = None 
while word != "end":
    word = input("Enter a word: ")
    characters = []
    for letter in word:
        characters.append(letter)
    characters.reverse()
    new_word = "".join(characters)
    print(new_word)