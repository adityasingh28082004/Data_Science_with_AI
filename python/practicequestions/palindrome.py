# palindrome check
# a plindrome is a number that remain same when it reverse
word = input("enter the word :")

word_reverse = word[::-1]

if word == word_reverse:
    print('palindrome')
else:
    print('not palindrome')
