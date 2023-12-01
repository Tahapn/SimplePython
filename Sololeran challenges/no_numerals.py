#### problem #### 

# You write a phrase and include a lot of number characters (0-9), but you decide that for numbers 10 and under you would rather write the word out instead.
# Can you go in and edit your phrase to write out the name of each number instead of using the numeral?  
 
# Task:  
# Take a phrase and replace any instances of an integer from 0-10 and replace it with the English word that corresponds to that integer. 
 
# Input Format:  
# A string of the phrase in its original form (lowercase). 
 
# Output Format:  
# A string of the updated phrase that has changed the numerals to words. 
 
# Sample Input:  
# i need 2 pumpkins and 3 apples 
 
# Sample Output:  
# i need two pumpkins and three apples

#### solution ####

number_to_words = {'0':'zero','1':'one','2':'two','3':'three',
'4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten'}

text = input() 
words = text.split(' ')
final_text = []

for i  in words :

    if i.isnumeric():
    
        final_text.append(number_to_words.get(i))
    else:
        final_text.append(i)


print(' '.join(final_text))