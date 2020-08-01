#홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.
#과목	점수
#국어	80
#영어	75
#수학	55

#변수지정
Korean = 80
English = 75
Mathematics = 55

#그냥 숫자로 간단하게 평균내기
avg = (Korean + English + Mathematics) / 3
print(avg)

#함수로 구해보기
def average(Korean, English, Mathematics):
    return (Korean + English + Mathematics) / 3

# 함수쓸때는 꼭 input값 같이 넣어주기
print(average(Korean, English, Mathematics))