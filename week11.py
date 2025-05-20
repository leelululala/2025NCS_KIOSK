import requests

# url=f"https://wttr.in/incheon?format=%C+%t"
url=f"https://wttr.in/incheon?&0&Q"
response=requests.get(url)
# print(response)#객체형태로 상태코드가 프린트 됨.
# print(response.status_code)#얘는 상태코드 숫자만 프린트.
if response.status_code==200:
    print(response.text.strip())#strip함수: 양쪽 끝에 공백 제거해줌?? 쓰는 거 추천
else:
    print(f"상태 코드: {response.status_code}")