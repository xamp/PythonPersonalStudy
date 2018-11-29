from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('https://movie.daum.net/main/new#slide-2-0')
res = urlopen(req)
html = res.read().decode('UTF-8')
#print(html)
bs = BeautifulSoup(html, 'html.parser')
tags = bs.findAll('div', attrs={'class': 'footer_link #footer #etc'})
tagss = tags.find_all("a")
#all_ps_in_ex_id_divs = tags.find_all("a")
#tags = bs.findAll('ul', attrs={'class': 'list_movie #movie'})
print(tags)
for tag in tags :
    print(tag.a)
    # 검색된 태그에서 a 태그에서 텍스트를 가져옴
 #   print(tag.a.text)

