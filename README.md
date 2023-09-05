# 오목 게임

> CMD 콘솔 기반 오목 게임

<br><br>

## *게임 실행 화면

<p align="center">
  <img src="https://github.com/Kwon-sang/omok/blob/master/%EC%98%A4%EB%AA%A9%EA%B2%8C%EC%9E%84%20%EC%8B%A4%ED%96%89%ED%99%94%EB%A9%B4.jpg">
</p>


## 1. 요구사항 설계
- 게임 시작 시, Player1 과 Player2 의 이름을 설정 가능하다.
- 바둑판의 크기는 오목 정식 규격인 15*15이며, 돌을 둘 수 있는 위치 또한 이와 같다.
- 바둑판에서 각 행과 열의 위치를 알 수 있도록, 출력된 바둑판에는 **행과 열의 인덱스**를 포함해야 한다.
- 사용자의 입력은 정해진 **입력 포맷**을 가지며, 잘못된 입력시에는 에러 메시지와 함께 **재입력**을 요구한다.
   * 바둑돌을 놓는 위치에 대한 입력은 공백을 기준으로 '행인덱스 열인덱스'의 형태이며 각 인덱스 번호는 숫자만 가능하다. ex)'3 4'
   * 바둑판의 크기를 벗어나는 위치에 돌을 둘 수 없으며, 이미 돌을 둔 자리 또한 돌을 둘 수 없다.
   * 바둑돌을 놓는 위치에 대한 입력에서 Q 혹은 q를 입력시, 즉시 게임을 종료할 수 있다.
- 각 플레이어가 돌을 놓은 후, 화면에 바둑판의 상태를 출력해야 한다.
- 각 플레이어는 번갈아가며 흑돌과 백돌을 두어야 한다.
- 오목을 검증하는 로직을 구성해야 하며, 플레이어의 오목 달성 시 플레이어의 이름과 함께 게임 승리 문구가 출력되어야 한다.

<br><br>

## 2. 모듈

[`main.py`] (https://github.com/Kwon-sang/omok/blob/master/main.py)
  : 게임 실행 흐름을 제어
  
-- [`settings.py`] (https://github.com/Kwon-sang/omok/blob/master/modules/settings.py)
  : 바둑판 기호, 입출력, 에러메시지 등 텍스트 변수 관리

-- [`views.py`] (https://github.com/Kwon-sang/omok/blob/master/modules/views.py)
  : 게임 화면을 위한 로직
  
-- [`board.py`] (https://github.com/Kwon-sang/omok/blob/master/modules/board.py)
  : 오목을 위한 바둑판 정보와 사용자 변수 등 오목에 대한 핵심로직

