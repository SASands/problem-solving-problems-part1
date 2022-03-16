# 1. Reverse a string

# a. Write code that takes a string as input and returns the string reversed

# b. i.e. “Hello” will be returned as “olleH”

word_to_reverse = ("Hello")       #index-Returns the index of the first element with the specified value

for index in range(len(word_to_reverse)-1, -1, -1):     #range()-(start, stop, step)  # len()- function returns the number of items in an object.
    print(word_to_reverse[index])


# 2. Capitalize letter

# a. Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

word_to_be_cap =("Hello World!")      #title() Converts the first character of each word to upper case
word = word_to_be_cap.title()
print(word)





# 3. Compress a string of characters

# a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"



# 4. BONUS CHALLENGE: Palindrome

# a. A word, phrase, or sequence that reads the same backward as forward i.e. madam

# b. Write code that takes a user input and checks to see if it is a Palindrome and reports the result
