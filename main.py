from bodyFinder import bodyFinder
from releaseDownloader import releaseDownloader
from depFinder import depFinder


if __name__ == '__main__':
    nttSeqNo = 3181890
    depName = '뉴미디어정책과'
    nttList = depFinder(nttSeqNo, nttSeqNo-80, depName)
    for ntt in nttList:
        body = bodyFinder(ntt)
        releaseDownloader(body)
