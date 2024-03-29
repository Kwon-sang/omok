# CLI 오목게임 (Python)

## Project Backgrounds

파이썬 언어를 처음 배웠을 당시, 언어를 활용하기 위해 간단한 오목게임을 만든 적이 있다.
당시에 나름 열심히 프로그램을 작성하였으나, 지금 생각해보면 참 많이 부족했다는 생각이 든다.

각 기능에 대한 모듈화를 고려하지 않았으며, 절차적 방식으로 구현하였다. 
소위 프로그래밍 언어를 처음 배운 이들이 처음 프로그램을 작성할 때 하곤 하는 하나의 God-class를 통해 구현했었다.
하나의 파이썬 스크립트에 모든 로직이 존재하였으며, 프로그램 제어를 위해 for문, while문, if문이 뒤섞여 있었으며,
이러한 제어문의 깊이 또한 깊었다.

'잘 짜여진 프로그램' 보다는 '돌아가는 프로그램'이 목적이었기에, 지금 처음 작성했던 코드를 회고해 보면 코드의 수준은 엉망이었다. 
다른 누군가가 그 때의 코드를 본 다면, 쉽게 이해하기 힘들었을 것이다.

시간이 지나, 공부를 하며 그 당시보다 더 나은 코드를 작성할 수 있을 것이란 생각이 들었다.
객체와 객체 지향에 대해 많은 고민을 보는 시간이 있었으며, 파이썬의 다양한 기능과 코딩 스타일에 대해 배우게 되었다.
프로그램을 만드는 '나'의 관점만이 아닌, 코드를 보는 '타인'의 관점 또한 고려할 수 있게 되었다.
typing 모듈을 통한 파라미터 type hint와, docstring의 중요성 까지 말이다.

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

<br/>

## 4. 기능 구현
 
#### `user_input.py` [click to Code Page](https://github.com/Kwon-sang/omok/blob/master/src/user_input.py)
- `size() -> int` : 바둑판 사이즈 입력 및 입력 포맷 검증.
- `username() - dict`: 사용자의 이름을 입력. 사용자1과 사용자2의 이름이 같을 경우 예외 발생. 유저1과 유저2의 상태 정보를 담은 딕셔너리를 반환.
- `position() -> tuple[int, int]`: 사용자의 바둑돌 놓을 위치를 입력 및 포맷 검증. x, y 위치에 대한 정수 튜플을 반환
- `re_game() -> bool` : 게임 종료 시, 재시작 여부(Y/N)에 대한 입력 및 포맷 검증. 불리언을 반환.
- 재입력 요구 기능은 `decorators.py` 의 `@repeatable` 데코레이터를 통해 가능하도록 구현.

#### `board.py` [click to Code Page](https://github.com/Kwon-sang/omok/blob/master/src/board.py)
- `Board` : 바둑판과 관련된 메서드 및 속성의 집합. 바둑판의 위치 값 세팅, 입력값 검증, 오목 판별 메서드 존재.

#### `decorators.py` [click to Code Page](https://github.com/Kwon-sang/omok/blob/master/src/decorators.py)
- 사용자의 입력 오류에 대한 재입력 반복을 Decorator 문법을 이용하여 구현.
- `@repeatable` 데코레이터 적용 시, 함수에서 `ValueError` 발생 시 재 실행 가능. 사용자의 입력오류에 대한 재입력을 해당 데코레이터를 사용하여 재입력기능을 구현.

#### `settings.py`[click to Code Page](https://github.com/Kwon-sang/omok/blob/master/src/settings.py)
- 문자열 기반(입력 문자열, 출력 문자열, 에러 메시지 등) 값 정보를 관리.

#### `main.py`[click to Code Page](https://github.com/Kwon-sang/omok/blob/master/src/main.py)
- 게임 실행 흐름 로직

<br />

## 5. 게임 화면(Click to title)

<details>
    <summary>바둑판 크기 입력</summary>
    <img width="866" alt="image" src="https://github.com/Kwon-sang/omok/assets/115248448/8a765ef8-f33b-48f3-a54b-481cda756493">
</details>

<details>
    <summary>바둑판 크기 입력 오류 </summary>
    <img width="864" alt="image" src="https://github.com/Kwon-sang/omok/assets/115248448/5178e940-a17a-4a7c-991d-4a96d167d106">
</details>

<details>
    <summary>사용자 이름 입력 </summary>
    <img width="863" alt="image" src="https://github.com/Kwon-sang/omok/assets/115248448/b05a6d6e-c5fc-4253-ae72-92ffb86a9cb6">
</details>

<details>
    <summary>사용자 이름 입력 중복 오류 시 </summary>
    <img width="866" alt="image" src="https://github.com/Kwon-sang/omok/assets/115248448/def4056e-f7da-4f61-b9ce-1749116fdb3d">
</details>

<details>
    <summary>오목 게임 화면 및 바둑돌 위치 입력 </summary>
    <img width="860" alt="image" src="https://github.com/Kwon-sang/omok/assets/115248448/024fc52d-e7a4-42a6-bf53-377c77cb2d65">
</details>

<details>
    <summary>오목 게임 화면 및 바둑돌 위치 입력 오류  </summary>
    <img width="863" alt="image" src="https://github.com/Kwon-sang/omok/assets/115248448/ff500f32-a640-4a17-9eb2-d48d5c15cd30">
</details>

<details>
    <summary>오목 게임 화면 및 이미 존재하는 위치 입력시 오류  </summary>
    <img width="863" alt="image" src="https://github.com/Kwon-sang/omok/assets/115248448/06fc0f3b-7880-4b35-91f1-6bb5d783588e">
</details>

<details>
    <summary>오목 완성  </summary>
    <img width="866" alt="image" src="https://github.com/Kwon-sang/omok/assets/115248448/d5638ad5-b58d-4a25-b2f5-57b286e461b3">
</details>
