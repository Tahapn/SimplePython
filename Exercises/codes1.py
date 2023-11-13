#### swap first name and last name #####

name = input('Please enter your full name : ')

words = name.split(' ')
words.reverse()

print(' '.join(words))


#### sort numbers ####
numbers = input('Please enter your numbers with \',\' between them : ')
list_numbers = numbers.split(',')
list_numbers.sort()

print(list_numbers)


#### odd or even #####
number = int(input('please enter a number : '))
if number % 2 ==0:
    print(f'{number} is even.')
    
else:
    print(f'{number} is odd.')


### turn the first four letters to lowercase ####
word = 'PYTHON Dev'
print(word[:4].lower() + word[4:]) 


### function that swaps the first and last letter in a text ####
text = 'Hello World'

def swap(text):
    print(text[-1] + text[1:-1] + text[0])


#### function that calculated sum of three numbers. if two of them are the same number it return 0. ####

numbers1 = [90,10,11]
numbers2 = [10,10,2]
def sum_of_numbers(list_of_numbers : list):
    sum = 0
    for number in list_of_numbers:
        if list_of_numbers.count(number) > 1:
            return 0
        else:
            sum += number
    return sum

print(sum_of_numbers(numbers1))
print(sum_of_numbers(numbers2))


#### average of few numbers ####
nums = [1,2,3,5,4]
def average(numbers : list):
    sum_of_number = sum(numbers)
    number_of_members = len(numbers)
    return sum_of_number / number_of_members

print(average(nums))


#### fibonacci sequence with a given number of members ####
def fibonacci(lenght):
    sequnce = [0,1]
    for _ in range(lenght -2 ) :
        sequnce.append(sum(sequnce[-2:]))
    
    print(sequnce)

fibonacci(7)

