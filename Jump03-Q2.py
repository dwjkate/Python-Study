"""
while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
"""

my_num = 1
answer = 0
while my_num < 1001:
    if my_num % 3 == 0:
        answer = answer + my_num

    my_num = my_num + 1
    
print(answer)