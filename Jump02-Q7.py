#['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.

#※ 문자열의 join 함수를 사용하면 리스트를 문자열로 쉽게 만들 수 있다.

my_list = ['Life', 'is', 'too', 'short']

#스트링 자료형에서 조인함수 사용해서 각각 단어 가운데 스페이스 있는걸로 연결
result = " ".join(my_list)
print(result)