

# 1. Reverse a string

# a. Write code that takes a string as input and returns the string reversed

# b. i.e. “Hello” will be returned as “olleH”

word_to_reverse = ("Hello")       #index-Returns the index of the first element with the specified value
final_result = ''


for index in range(len(word_to_reverse)-1, -1, -1):     #range()-(start, stop, step)  # len()- function returns the number of items in an object.
    final_result += word_to_reverse[index]

print(final_result)



# 2. Capitalize letter

# a. Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

word_to_be_cap =("hello world!")      #.title() Converts the first character of each word to upper case
word = word_to_be_cap.title()
print(word)



# 3. Compress a string of characters

# a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

string_to_compress= ("aaabbbbbccccaacccbbbaaabbbaaa")  


#txt.find("") ???

# Nested for loop


# Create a variable called "counter"
# Create a variable called "final_result" and set equal to an empty string (will build up the final result over time)

# Write a for loop that loops over each letter one by one (lets say we call the index for this loop "outer_index")

    # Write a nested for loop that does the same thing
        # Check letter in the word at outer_index and see if it is eqaul to the letter we are looping on in the inner loop
        # If they match, increment counter
        # If they don't match, add counter and lettter value to final result and resent counter and exit inner loop



# 4. BONUS CHALLENGE: Palindrome

# a. A word, phrase, or sequence that reads the same backward as forward i.e. madam

# b. Write code that takes a user input and checks to see if it is a Palindrome and reports the result



def palindrome():
    user_input= input("Please give me a word to check if it's a palindrome: ")
    final_result2= ""
    word1 = user_input
    word2 = final_result2
    for index in range(len(word1)-1, -1, -1):
        final_result2 += word1[index] 
    if word1 == final_result2:
        print ("that word is a Palindrome!")
    else:
        print ("That's unfortunately not a Palindrome")
palindrome()




# def check_word():
#     palindrome()

#does the users word read the saem front to back and back to front
#make function to reverse word and 
#make a bool to see if true
