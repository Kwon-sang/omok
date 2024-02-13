# CLI 오목게임 (Python)

## Project Backgrounds

파이썬 언어를 처음 배웠을 당시, 언어를 활용하기 위해 간단한 오목게임을 만든 적이 있다.
당시에 나름 열심히 프로그램을 작성하였으나, 지금 생각해보면 참 많이 부족했다는 생각이 든다.

각 기능에 대한 모듈화를 고려하지 않았으며, 절차적 방식으로 구현하였다. 
하나의 파이썬 스크립트에 모든 로직이 존재하였으며, 프로그램 제어를 위해 for문, while문, if문이 뒤섞여 있었으며,
이러한 제어문의 깊이 또한 깊었다.

'잘 짜여진 프로그램' 보다는 '돌아가는 프로그램'이 목적이었기에 코드의 수준은 엉망이었다고 회고한다. 
다른 누군가가 그 때의 코드를 본 다면, 쉽게 이해하기 힘들었을 것이다.

시간이 지나, 공부를 하며 그 당시보다 더 나은 코드를 작성할 수 있을 것이란 생각이 들었다.
따라서, 다시 한번 해당 프로젝트를 해보기로 하였다.

'그저 잘 돌아가기만 하는' 프로그램이 아닌, 기록으로 남길 가치가 있도록 아주 세심하고 정교하게 주의를 기울여 해당 프로젝트를 진행하고자 한다.
요구사항 설계, 요구사항 분석, 기능 설계, 기능 구현, git 커밋 메시지 등 하나하나 세심한 주의를 기울여 프로젝트를 진행하며,
작업 하나하나 의미를 가질 수 있는 것이 이 프로젝트의 목적이다.


<br/>

## 1. 요구사항 설계(Design of Requirements)
- CLI(Command-Line Interface) 기반 오목 게임.
- 사용자는 2인으로 구성되며, 각 사용자는 자신의 정한 닉네임을 설정할 수 있다.
- 오목판의 크기를 사전에 설정 가능하다.
- 각 사용자는 오목판에서 자신이 둘 바둑판의 위치를 'x y'의 형태로, 공백을 두고 입력하여야 한다.
- 입력에 문제가 있는 경우, 에러메시지와 함께 다시 입력할 수 있어야 한다.
- 게임은 중간에 종료 가능하며, 종료 커맨드는 'Q'이다.
- 오목의 성공 여부는 '오목 달성'에 국한하며, 이외의 33규칙 등은 제외한다.
- 사용자의 오목 달성 시, 게임을 재시작 할 수 있어야 한다.

<br/>

## 2. 요구사항 분석(Analyzing Requirements )
- UI(User Interface)를 고려하여, 게임의 각 과정에서 터미널 출력은 연속적으로 이어지지 않아야 하며, step별 필요한 화면을 보여주어야 한다.
- 사용자가 바둘돌을 둘 위치를 입력함에 있어, 이를 위해 터미널에 바둑판의 현재 상태가 출력되어야 한다.
- 사용자가 바둘돌을 둘 위치를 쉽게 알 수 있도록, 터미널 UI에 위치 인덱스 정보가 존재하여야 한다.
- 오목판의 크기를 설정함에 있어서, 유한해야 하며, 최소크기 제한과 최대 크기 제한이 존재하여야 한다.
- 사용자의 입력에 대해 적절한 유효성 검사 로직이 존재해야 하며, 예상치 못한 실행흐름이 발생하지 않도록 한다.
- 유지 보수의 목적에서, 코드 내 문자열(String)은 하드코딩이 아닌, 관리가 가능해야 한다.
- 재입력과 같이, 반복이 발생하는 로직은 '재귀' 방식으로 구현하지 않기로 한다. 이 경우 무한히 반복될 경우 예상치 못한 동작이 발생하기 때문이다.
- 오목 달성여부를 검증하는 알고리즘은 전체 오목판을 하나하나 조회할 필요가 없다. 이는 불필요하다. 해당 사용자의 '마지막 위치'를 기준으로 알고리즘을 적용할 경우, 보다 효율적으로 계산가능하다.


<br/>

## 3. 기능 설계(Design of Functionalities)

> 목표 : **Low coupling** / **High cohesion** / **Obvious responsibility**

### 3.1 게임 로직 분석
    1. 게임 시작 
    2. 바둑판 크기 설정
    3. 바둑판 크기 검증. if not -> 2.
    4. 사용자1, 사용자2 이름 입력
    5. 사용자1 바둑돌 위치 입력
    6. if command is 'Q' -> 게임 종료
    7. 사용자1 위치 검증. if not -> 5.
    8. 사용자2 바둑돌 위치 입력
    9. if command is 'Q' -> 게임 종료
    10. 사용자2 위치 검증. if not -> 8.
    11. 오목 완성 여부 판단. if not -> 5.
    12. 게임 재시작 여부. if yes -> 1.
    13. 게임 종료

### 3.2 객체 or 모듈 설계
- 사용자 입력 모듈
  - 바둑판 크기 입력
  - 사용자 이름 입력
  - 바둑돌 위치 입력
  - 입력값 포맷 검증
- 바둑판 모듈
  - 바둑돌 위치 데이터 관리
  - 바둑돌 위치 데이터 관련 유효성 검증
  - 바둑판 데이터 UI 출력
  - 오목 검증 로직
- 메시지 모듈
  - 문자열(String) 데이터 관리
- 메인
  - 게임 로직 흐름 제어(Logic controller)

## 4. 기능 구현
 dsdf

