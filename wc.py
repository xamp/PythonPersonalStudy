from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
res = urlopen(req)
html = res.read().decode('cp949')

bs = BeautifulSoup(html, 'html.parser')
tags = bs.findAll('div', attrs={'class': 'tit3'})

for tag in tags :
    # 검색된 태그에서 a 태그에서 텍스트를 가져옴
    print(tag.a.text)

