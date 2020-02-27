'''dress = ["jacket", "blazers", "gown", "jean"]
print(dress[2])'''

#simple calculator
'''num1 = input("please enter a number, ")
num2 = input("please enter a number, ")
result = int(num1) + int(num2)
print(result)'''

#adding stuff to a list
'''grass = ["lemon", "carpet", "elephant", "tanilum-triangulaire", "foilage"]
animals = ["dog", "cat", "skunk", "rabbit", "mouse", "squirrel"]
animals.extend(grass)
print(animals)'''

'''def dance(name):
    print("azonto" + name)

dance(" etigi")'''

'''def say_hi(name):
    print("my name is " + name)

say_hi("Skibii")'''

'''A piece of code that returns the name univelcity after passing some arguments
def call_me(name, address):
    print("my name is " + name + ", I am located at " + address + ".")

call_me("Univelcity", "42 Montgomery road Yaba")
'''

'''name = "Staticmajor"
for letter in name:
    print(letter)'''



#Using the map function and lambda to iterate through a range of numbers to show true for even numbers and false for odd numbers
'''    y = range(1, 10)
 z = list(map(lambda x: x%2==0, y))
 z
[False, True, False, True, False, True, False, True, False]
>>>
'''

'''
This is an if conditional
dog = False
cat = True

if dog and not(cat):
    print("this is a dog")
elif not(dog) and cat:
    print("this is a cat")
else:
    print("This is neither a cat nor a dog")
    '''



# Using a while loop to loop through numbers
'''i = 0
while i <= 10:
    print(i)
    i += 1

print ("Done with loop")'''

# A simple guessing game using the while loop(2:23:30hrs)
''''secret_word = "Bread"
guess_word = ""
guess_word_count = 0
guess_word_limit = 3
out_of_guesses = False
while guess_word != secret_word and not(out_of_guesses):
    if guess_word_count < guess_word_limit: 
        guess_word = input("Please guess the correct word: ")
        guess_word_count +=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You lose!")
else:
    print("You Win!")'''



#Using a for loop to calculate the exponent of a number(raising to the power)
'''def to_power(base_num, exp_num):
    result = 1
    for i in range(exp_num):
        result = result * base_num
    return result

print(to_power(9, 2))'''

# This is how to read a file in python using the open function and it is also a best practice to always close the file
# that you have opened when you are done reading from it 
'''factorial_file = open("factorials.py", "r")    
print(factorial_file.read())
factorial_file.close()'''


# Using a for loop to loop through the items in particular line in the file that is being read
'''sample_data_file = open("sample_data.py", "r")
for datum in sample_data_file.readline():
        print(sample_data_file.readline()[1])

sample_data_file.close()'''


#MultiChoice App
'''class Question(object):

    def __init__(self, prompt, answer ):
        self.prompt = prompt
        self.answer = answer


questions = [
    "What colours are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colours are Bananas?\n(a) Teal\n(b) Magenta \n(c) Yellow\n\n",
    "What colours are Mangoes?\n(a) Green/Yellow\n(b) Red\n(c) Orange\n\n"
]

question1 = [
    Question(questions[0], "a"),
    Question(questions[1], "c"),
    Question(questions[2], "a")
]

def test_questions(self):
    score = 0
    for i in question1:
        answer = input(i.prompt)
        if answer == i.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(question1)) + " questions" + " correct")

test_questions(question1)
'''