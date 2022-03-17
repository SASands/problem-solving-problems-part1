from itertools import count


# 1. Reverse a string
# a. Write code that takes a string as input and returns the string reversed
# b. i.e. “Hello” will be returned as “olleH”

# word_to_reverse = ("Hello")       #index-Returns the index of the first element with the specified value
# final_result = ''
# for index in range(len(word_to_reverse)-1, -1, -1):     #range()-(start, stop, step)  # len()- function returns the number of items in an object.
#     final_result += word_to_reverse[index]
# print(final_result)


# 2. Capitalize letter
# a. Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

# word_to_be_cap =("hello world!")      #.title() Converts the first character of each word to upper case
# word = word_to_be_cap.title()
# print(word)


# 3. Compress a string of characters
# a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

    #1receiving a string of characters in a function----DONE

    #2setup for loop to iterate of a string indexing characters with range()
        #2a-keep track of current character
        #2b-keep track of next character
        #2c- keep track of the character with a counter
        #2d- keep track of final_result string (intial value "")
    #3-if current character is the same as next character 
        #3a if they are the same increase counter by one
    #4-else they are not the same
        #4a-stringify counter and concatenante with current character
            #4a.1-concatenate with final result
                #restart the counter at 1
    #5-return final_result string
#txt.find("") ???








def receive_characters():
    previous_character = ""
    next_character = ""
    character_count = (str 1)
    final_result = ""
    string_to_compress = ("abbbbbccccaacccbbbaaabbbaaa")  
    for current_character in string_to_compress:
        # if previous & current letter is different:
        if previous_character != current_character:
            final_result += character_count
            final_result += previous_character
        # if previous & current letter is the same:
        elif previous_character == current_character:
            character_count += 1
        # what about the end?

        else: 
            final_result
        previous_character = current_character
        print (final_result)
    return final_result
    # final_result should equal "1a5b4c" etc.
receive_characters()



    





# def iterate_string():
#     keep_count_of_current_character ="" 
#     string_to_iterate= ("aaabbbbbccccaacccbbbaaabbbaaa")
#     for character in string_to_iterate:
#         if character == character:
#             character += character
#             iter (range(len(string_to_iterate)))
#             count (len(string_to_iterate))
#             print (count)
# iterate_string()





# def str_indexing():
#     characters= ""
#     string_to_index=  ("aaabbbbbccccaacccbbbaaabbbaaa")
#     string_to_index.index("aaabbbbbccccaacccbbbaaabbbaaa")
#     for character in string_to_index:
#         print (character)
# str_indexing()









# def counting_characters_in_string():























# counter = "amount of letters in string"




# def string_character_amounts():    
#     final_result3 = ""  
#         for inner_index in range(len(string_to_compress)):
#             final_result3 += string_to_compress
#             if outer_index == inner_index:
#                 print(final_result3)




# 4. BONUS CHALLENGE: Palindrome

# a. A word, phrase, or sequence that reads the same backward as forward i.e. madam

# b. Write code that takes a user input and checks to see if it is a Palindrome and reports the result



# def palindrome():
#     user_input= input("Please give me a word to check if it's a palindrome: ")
#     final_result2= ""
#     word1 = user_input
#     word2 = final_result2
#     for index in range(len(word1)-1, -1, -1):
#         final_result2 += word1[index] 
#     if word1 == final_result2:
#         print ("that word is a Palindrome!")
#     else:
#         print ("That's unfortunately not a Palindrome")
# palindrome()




# def check_word():
#     palindrome()

#does the users word read the saem front to back and back to front
#make function to reverse word and 
#make a bool to see if true
