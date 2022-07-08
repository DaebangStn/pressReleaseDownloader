import requests
from bs4 import BeautifulSoup as bs


def depFinder(nttSeqNo_start, nttSeqNo_end, depName, bbsSeqNo=94):
    if nttSeqNo_start > nttSeqNo_end:
        nttSeqNo_start, nttSeqNo_end = nttSeqNo_end, nttSeqNo_start

    nttSeqNo_list = []
    for nttSeqNo in range(nttSeqNo_start, nttSeqNo_end+1):
        print(nttSeqNo)
        URL = 'https://www.msit.go.kr/bbs/view.do?bbsSeqNo={}&nttSeqNo={}'.format(bbsSeqNo, nttSeqNo)
        res = requests.get(URL)

        assert res.status_code == 200

        doc = res.text
        soup = bs(doc, 'html.parser')

        try:
            tag = soup.find("form", id="search-view-form").find('span', 'con')
        except Exception:
            print('[Error] There is no page')

        if tag.text == depName:
            nttSeqNo_list.append(nttSeqNo)

    print(nttSeqNo_list)
    return nttSeqNo_list

