import requests
from parse import compile
from urllib import parse
import os


def releaseDownloader(body, workingDir=None):
    if workingDir is None:
        workingDir = os.path.join(os.getcwd(), 'hwpx')

    assert os.path.exists(workingDir)

    URL = 'https://www.msit.go.kr/ssm/file/fileDown.do'
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    res = requests.post(URL, headers=headers, data=body)

    assert res.status_code == 200

    p = compile('attachment;filename="{}";')
    _filename = p.parse(res.headers['Content-Disposition'])
    filename = parse.unquote(_filename[0])

    outPath = os.path.join(workingDir, filename)
    assert not os.path.exists(outPath)

    outFile = open(outPath, 'wb')
    outFile.write(res.content)
    outFile.close()
