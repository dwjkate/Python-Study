"""
In this mission you should write a function than introduce a person with a given parameters in attributes.
Input: Two Arguments. String and positive integer.
Output: String.
Example:
1. say_hi("Alex", 32) == "Hi, My name is Alex and I'm 32 years old"
2. say_hi("Frank", 68) == "Hi, My name is Frank and I'm 68 years old"
"""

#문자열 포맷팅 사용하기 (문자열안에 어떤 값을 삽입하는 방법)

name1 = "Alex"
age1 = 32
answer1 = "Hi, My name is %s and I'm %d years old" % (name1, age1)
print(answer1)

#포맷 함수를 이용해서 포맷팅 하는 방법

name2 = "Frank"
age2 = 68
answer2 = "Hi, My name is {} and I'm {} years old".format(name2, age2)
print(answer2)


#if함수 사용해서 해보기
name3 = "Alex"
name4 = "Frank"
age3= 32
age4 = 68

if name3 == "Alex" and age3 == 32:
    print("Hi, My name is Alex and I'm 32 years old")
    
if name4 == "Frank" and age4 == 68:
    print("Hi, My name is Frank and I'm 68 years old")




