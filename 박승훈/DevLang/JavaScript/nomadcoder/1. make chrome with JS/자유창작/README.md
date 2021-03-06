# 첫 번째 토이 프로젝트 : 숫자야구 게임 사이트 만들기

<br>

## 왜 숫자야구였는가?

- 노마드 코더의 JS 웹사이트 클론코딩 중 배운 내용을 다져보자는 취지였지만, **따라하기보다는 배운 내용을 기반으로 뼈대부터 바꿔서 새롭게 익혀보고 활용하고 싶었다.**

- JavaScript의 프로그래밍적 요소인 계산이나 넣고 빼는 것, 반복문, 함수 정의와 호출 등을 활용하기 좋겠다고 생각했다.

- 이왕이면 웹사이트보다도 재미있게 즐길 수 있는 게임적인 요소가 있으면 좋겠다고 생각했고, **내 수준에서 구현할 수 있는 로직이라고 판단**해서 결정하였다.

<br>

## 신경 썼던 점

#### 원한다면 새 게임을 시작하고, 이전 게임을 이어서 할 수도 있어야 한다.

- home 화면을 따로 만들고, 새 게임과 불러오기 버튼을 만들어 다르게 동작하도록 하였다.

- 기본적으로 모든 제출된 답안이나 정답의 경우 localStorage에 저장해서 **불러오기 버튼을 누르면 localStorage에서 모든 정보를 받아와 화면에 표시**하고, **새 게임을 누르면 localStorage의 기존 정보를 초기화하고 완전히 정답도 새로 만들어 localStorage에 저장을 시작**하는 방식으로 해결하였다.

![bandicam-2022-03-19-19-49-26-274](https://user-images.githubusercontent.com/86189596/159118040-ec5acce5-e39a-47d3-8f58-10bf48d7e4fd.gif)

불러오기를 누르면 기존 정보를 로딩하고, 새 게임을 누르면 같은 답안을 제출해도 전혀 다른 답이 나오는 것을 통해 새로운 답이 생성되었음을 알 수 있다.

<br>

#### 이전 답안이 history에 계속 저장이 되고 보여져서 게임 중에 참고할 수 있어야 한다.

- 숫자야구 게임은 이전 답안과 함께 비교하고 추측하여 정답에 가까워진다.

- 때문에 이전 답안에 대해 게임중에 계속 확인할 수 있어야 한다.

- logPart를 게임 화면 옆에 따로 만들어 이전 답안을 계속 확인하는 구조로 제작하였다.

- 직전 답안과 결과를 답안 기입란 위쪽으로 크게 두어 표시하였다.

![image](https://user-images.githubusercontent.com/86189596/159116102-e4e16469-7f9c-49c7-8e5d-a99ec8492310.png)


<br>

#### 도움말 페이지가 있어야 한다.

- 나는 군시절 동기들과 자주 즐겼기 때문에 규칙을 잘 알지만 모르는 사람이 있을 수 있다고 판단했다.

- 게임 화면에서 도움말 페이지로 이동할 수 있는 버튼을 만들고, 도움말 페이지에서 다시 원래 화면으로 돌아갈 수 있어야 한다.

- **각 View의 id를 설정해 toggle로 hidden 클래스를 넣고 빼며** 이미 구현되어 있는 도움말 페이지를 보이고 안 보이게 하였다.

![bandicam-2022-03-19-19-52-57-575](https://user-images.githubusercontent.com/86189596/159118188-4e57ec66-7404-4533-a8df-38c402d92c45.gif)

<br>

#### 새로고침을 하더라도 진행화면에서 달라지는 점이 없어야 한다.

- 새로고침을 할 때마다 메인화면으로 돌아가는 문제가 있었다.

- localStorage에 현재 바라보고 있던 페이지를 페이지 전환 때마다 변경/저장하여 새로고침 시 localStorage에 저장된 페이지 지표를 보고 시작하는 방식으로 해결하였다.

![bandicam-2022-03-19-18-47-23-521](https://user-images.githubusercontent.com/86189596/159116309-87acf08f-0eba-474f-b892-faf13374482f.gif)

<br>

## 어려웠던 점

### JS 문법 자체의 실력 부족

#### 반복문

최초 입력한 답이 실제 답과 맞는지 확인하려는 로직에서 4개의 수가 모두 수와 자리까지 맞아야 하기 때문에 인덱스를 이용해 for문으로 반복을 줄여보고자 하였다. 

```js
function acceptSubmit(event){
  event.preventDefault();
  const answerInfo = checkAnswer();

  // 정답 확인
  let ansArr = JSON.parse(localStorage.getItem("ansArr"));
  let check4 = 0;
  for (let i=0; i<4;i++){
    if(parseInt(answerInfo[i+4])===ansArr[i]){
      check4++
      }
  }

  // 입력 값 4개가 정답이면
  if (check4===4){
    playView.classList.toggle("d-none");
    answerView.classList.toggle("d-none");
  } else {
    // 게시판에 결과 쓰기
    writeBoard(answerInfo);
    // 로컬 스토리지에 결과 저장
    saveLog(answerInfo);
    // 답안을 위의 공간으로 올리고 입력 공간 비우기
    moveInput(answerInfo);
    // HISTORY에 결과 반영
    writeHistory(answerInfo);
  }
}
```

위와 같은 로직을 짰고, if문을 4번 돌리며, check4가 4번 ++되어 4가 되면 정답이어서 정답 화면을 보이게 하고, 아니라면 답안을 localStorage에 반영하고 화면에도 반영하는 방식으로 작성하였다.

그런데 check4를 인식하지 못하는 것이다.

```js
function acceptSubmit(event){
  event.preventDefault();
  const answerInfo = checkAnswer();

  // 정답 확인
  let ansArr = JSON.parse(localStorage.getItem("ansArr"));
  let check4 = 0;
  if(parseInt(answerInfo[4])===ansArr[0]){check4++}
  if(parseInt(answerInfo[5])===ansArr[1]){check4++}
  if(parseInt(answerInfo[6])===ansArr[2]){check4++}
  if(parseInt(answerInfo[7])===ansArr[3]){check4++}

  // 입력 값 4개가 정답이면
  if (check4===4){
    playView.classList.toggle("d-none");
    answerView.classList.toggle("d-none");
  } else {
    // 게시판에 결과 쓰기
    writeBoard(answerInfo);
    // 로컬 스토리지에 결과 저장
    saveLog(answerInfo);
    // 답안을 위의 공간으로 올리고 입력 공간 비우기
    moveInput(answerInfo);
    // HISTORY에 결과 반영
    writeHistory(answerInfo);
  }
}
```

그래서 위처럼 하드코딩에 가깝게 작성했는데 check4에 제대로 반영되서 원하는대로 돌아갔다. 이에 대한 이유를 알 수가 없었다.

<br>

#### 함수 위치

최초에는 메인화면 로직을 구성하는 mainView.js, 플레이화면 로직을 구성하는 playView.js, 도움말화면 로직을 구성하는 helpView.js, 결과화면 로직을 구성하는 answerView.js, 그리고 HTML element를 구성하는 makeHTML.js 파일로 나누어 index.html에 연결했다.

그런데 다른 어떤 함수가 정의되지 않았다면서 특정 함수가 실행이 되지 않기에 js 파일을 모두 합쳐 main.js 파일로 종합하였다. 그럼에도 정의되지 않았다는 일이 생겼다. top-down 방식으로 위에서 먼저 정의된 함수여야 되는가보다 했다.

그런데 함수를 기능별로 묶으려면 이러한 순서를 완전히 지킬 수 없을텐데 어떻게 이를 해결할 수 있을까 고민하였지만 방법을 알 수 없었다.

<br>

### JS로 생성하는 HTML element의 중복

- 새로고침을 할 때마다 기존에 DOM 트리에 추가되어있던 HTML element들이 사라지지 않고 남아있는 상태에서 새롭게 들어가며 element가 계속 누적되는 문제가 있었다.

- element를 모두 지우고 다시 create, apppendChild 하여 추가하는 방식을 사용하였다.

<br>

## 아쉬운 점

#### 고정형 웹사이트

- 부트스트랩을 사용하면 훨씬 편하게 작업할 수 있다는 것을 알지만, 프레임워크 없이 순수한 언어 자체로 작성하고자 해서 부트스트랩을 사용하지 않으려 했다. 

- 그런데 순수 CSS로 Grid를 작성하는 방법을 잘 몰라서 반응형 웹사이트를 만들 수 없었다.

- 반응형 뿐만이 아니라 사이트 내부적으로 레이아웃을 구성하는 것도 고정형 px 방식과 %를 일부 사용하였다.

- 다음 프로젝트 때는 `Grid를 직접 구현`할 수 있도록 CSS에 대한 학습도 겸해서 해야겠다고 생각이 들었다.

<br>

#### CSS와 JS코드의 중복

- Github Blog를 이용하면서 jekyll에서 사용하는 SCSS를 많이 다루어보았는데, 순서 CSS에서는 mixin이나 nesting이 안되다 보니 개체 하나하나 CSS 코드를 작성해주어야 하는 불편이 있었다. 무엇보다 불필요한 중복으로 가독성이 많이 떨어졌다.

- 그래서 부트스트랩처럼 클래스로 css 코드 뭉텅이를 적용하는 방식을 사용하여 mixin을 대신하였다. 다만 이렇게 되면 특정 element에 특정된 디자인을 구현하는 것이 상당히 아쉽다.

- JS 파일 같은 경우도 불러오기, 새 게임 버튼을 눌렀을 때의 실행 함수는 상당 부분 많이 겹치는데, 이를 모듈화해서 중복 코드를 제거해보고자 하였지만 아직은 많이 부족함을 느꼈다.

<br>

#### id selector의 사용

- 클론코딩 과정에서처럼 특정 element에 id를 부여해서 js 파일에서 변수로 설정하여 하위 작성에서 편의를 두었다.

![image](https://user-images.githubusercontent.com/86189596/159119295-9285742b-cab6-4cd7-ae5d-9a0206b4916a.png)

<br>

- 그래서 id를 이용해 css를 하나하나 이렇게 구현해주었다.

![image](https://user-images.githubusercontent.com/86189596/159119247-580e4213-8272-4c32-8401-9e8444dd72d7.png)

- 하지만 구글 같은 경우 특수한 상황이 아니라면 id를 사용하지 않는 것으로 안다.

- id는 사이트 내에서 절대적인 우선순위를 가지므로 지양하는 것이 좋다는 것이다.

- 때문에 다음 프로젝트 진행에서는 되도록이면 class selector와 first-child, last-child 등 순서를 이용해 특정 element를 확인하는 방식을 많이 이용해보고자 한다.