"""
For the input of your function will be given one sentence.
You have to return its fixed copy in a way so it's always starts with a capital letter and ends with a dot.
Pay attention to the fact that not all of the fixes is necessary.
If a sentence already ends with a dot then adding another one will be a mistake.
Input: A string
Output: A string
Example: 
1. correct_sentence("greetings, friends") == "Greetings, friends."
2. correct_sentence("Greetings, friends") == "Greetings, friends."
3. correct_sentence("greetings, friends.") == "Greetings, friends."
"""

#upper함수와 endswith 함수 이용하기
my_text = "greetings, friends"
print(my_text)

def correcting(my_text):
    my_text = my_text[0].upper() + my_text[1:]
    #여기까지하면 맨 첫글자 대문자로 만드는거!
    if (not my_text.endswith(".")):       #이거는 맨끝에 .으로 안끝나면 한번 더해주는거
        my_text += "."
    return my_text

answer = correcting(my_text)
print(answer)