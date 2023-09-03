# a user will input a sentence
# the user can change the sentence

sentence = input('Enter your sentence: ')
print('Your sentence is: ',sentence)

# we want to replace word or words in
# in a sentence
word1 = input('Enter the word to replace: ')
word2 = input('Enter the word to replace it with: ')
print(sentence.replace(word1, word2))
