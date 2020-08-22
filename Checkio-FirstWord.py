"""
You are given a string where you have to find its first word.
When solving a task pay attention to the following points:
-There can be dots and commas in a string
-A string can start with a letter or, for example, a dot or space.
-A word can contain an apostrophe and it's a part of a word.
-The whole text can be represented with one word and that's it.
Input: A string
Output: A string
Example:
first_word("Hello world") == "Hello"
first_word("greetings, friends") == "greetings"
"""

#replace strip split사용하기

my_text = "greetings, friends"

def first_word(my_text):
    my_text = my_text.replace(",", " ")
    my_text = my_text.replace(".", " ")
    my_text = my_text.strip() #양옆 공백을 지워준다 - 근데 두개이상 스페이스 일때 하나로 지워주는 기능이지 하나만 공백 있을때는 안지운다
    my_text = my_text.split()  #공백기준으로 나눈다
    

    return my_text[0]

answer = first_word(my_text)
print(answer)