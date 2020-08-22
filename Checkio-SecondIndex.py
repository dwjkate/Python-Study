"""
You are given two strings and you have to find an index of the second ocurrence of the second string in the first one.
Let's go through the first example where you need to find the second occurence of 's' in a word 'sims'.
It's easy to find its first occurrence with a function index or find which will point out that 's' is the first symbol in a word 'sims'
and therefore the index of the first occurrence is 0. 
But we have to find the second 's' which is 4th in a row and that means that the index of the second ocurrnece (and the answer to a question) is 3.

Input: Two strings
Output: Int of None
"""

my_text = "sims"
letter = "s"

def second(my_text, letter):
    #먼저 my_text안에서 같은 글자가 두번 이상 나오는지 부터 체크하기 - count사용할것
    if my_text.count(letter) < 2: #text안에서 letter의 갯수 세서 2개 보다 적으면
        return None
    first_letter = my_text.find(letter) #첫번째 등장하는 글자의 위치를 찾는다.

    return my_text.find(letter, first_letter + 1)

answer = second(my_text, letter)

print(answer)