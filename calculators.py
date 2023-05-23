a=3
b=4
# 덧셈 : +, 빼기 : -, 곱하기 :*, 나누기 : /, 몫 : //, 나머지 : %
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

# 자료의 형변환
# 숫자 -> 문자, 실수 -> 정수
a=10
b=20
#결과값이 1020이 나오도록 덧셈을 하여라
print(str(a)+str(b))
c=23333.33333
# c의 소수부분을 잘라서 출력하라
print(int(c))

# 제곱, 제곱근
# 2의10 제곱을 출력하라
print(2**10)
print(pow(2,10))
import math
print(math.pow(2,10))
# 1024의 제곱근을 구하라
# 제곱근은 math라는 라이브러리를 import해줘야한다.
print(math.sqrt(1024))