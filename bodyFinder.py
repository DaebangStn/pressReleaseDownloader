import requests
from bs4 import BeautifulSoup as bs
from parse import compile


def bodyFinder(nttSeqNo, bbsSeqNo=94):
    URL = 'https://www.msit.go.kr/bbs/view.do?bbsSeqNo={}&nttSeqNo={}'.format(bbsSeqNo, nttSeqNo)
    res = requests.get(URL)

    assert res.status_code == 200

    doc = res.text
    soup = bs(doc, 'html.parser')
    tag = soup.find("span", "down_btn").find('a').get('onclick')

    p = compile("fn_download('{}', '{}', 'hwpx');")
    result = p.parse(tag)

    body = 'atchFileNo={}&fileOrd={}&fileBtn=A'.format(result[0], result[1])

    return body


