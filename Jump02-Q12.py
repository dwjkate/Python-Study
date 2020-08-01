"""
파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 
다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 그리고 이런 결과가 오는 이유에 대해 설명해 보자.

>>> a = b = [1, 2, 3]
>>> a[1] = 4
>>> print(b)
"""

a = b = [1, 2, 3]
a[1] = 4
print(a)
print(b)

#둘다 모두 1,4,3이 출력된다. 메모리에 있는 어레이를 a와 b에 포인팅하고 있는 것 그래서 a가 어레이를 바꾸면 b도 바꾸는것