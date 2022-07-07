## 과기부 보도자료 다운로더

과기부의 컨텐츠 url은 다음과 같이 되어있다. </br>
https://www.msit.go.kr/bbs/view.do?bbsSeqNo={}&nttSeqNo={} </br>
여기서 nttSeqNo =94 일때 보도자료를 표시한다. </br>
현재 프로그램은 main.py에 bbsSeqNo가 지정되어 있다.

### **programmable 하게 보도자료를 다운로드 하기 위해서는 bbsSeqNo를 바꾸어 가면 된다.**

과기부의 컨텐츠의 다운로드 하는 url은 아래와 같다. </br>
https://www.msit.go.kr/ssm/file/fileDown.do </br>
POST body에 컨텐츠를 지정하는 문자열이 들어있는데 이는 컨텐츠 url에 지정되어 있다.


