"""
날짜 : 19-01-14
내용 : 파이썬 파일 다운로드
"""
import urllib.request as req

url = "http://chhak.com/py/img/puppy1.jpg"
req.urlretrieve(url, './puppy1.jpg')

print('다운로드 완료')