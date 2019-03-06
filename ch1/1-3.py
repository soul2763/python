"""
날짜 : 19-01-14
내용 : 파이썬 XML 데이터 출력
"""

import urllib.request as req

url = 'http://www.naver.com'

data = req.urlopen(url).read()
xml = data.decode('utf-8')

print(xml)