#### word counter ####

text = 'the quick brown fox jumps over the lazy dog'
words = text.split(' ')
counter = {}
for word in words:
    if word in counter:
        counter[word] += 1
    else :
        counter[word] = 1

print(counter)


#### upper the whole word if there are 2 capital letter in the first four letters ####
def upper_word(text : str):
    upper = 0
    for letter in text[:4]:
        if letter.isupper():
            upper += 1
    
    if upper < 2:
        print(text)
    else:
        print(text.upper())

upper_word('HEllo world')
upper_word('Hello wrold')


