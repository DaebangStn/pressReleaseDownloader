from bodyFinder import bodyFinder
from releaseDownloader import releaseDownloader


if __name__ == '__main__':
    nttSeqNo = 3181860
    body = bodyFinder(nttSeqNo)
    releaseDownloader(body)
