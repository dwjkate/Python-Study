#주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 
# #주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.

#>>> pin = "881120-1068234"
#※ 문자열 인덱싱을 사용해 보자.

pin = "881120-1068234"

#인덱싱으로 숫자 뽑아내기
sex = pin[7]
print (sex)

#남자인지 여자인지 확인
if sex == "1":
    print ("Men")
else:
    print ("Women")