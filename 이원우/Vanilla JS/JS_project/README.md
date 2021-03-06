# Toy Project # 1 - Vanilla JS

- 느낀 점

> 지금까지 배웠던 Vanilla Javascript를 복습하기 위해서, 시험과 과제가 있는 와중에 일주일이라는 짧은 시간 내에 다양한 기능을 구현하고, 아이디어를 구체화하는게 쉬운 일은 아니었습니다. 하지만, 아직 조악한 수준으로 HTML의 요소들을 JS를 위주로 요소를 추가해나가 결국 완성했습니다. 직접 만들어보는게 얼마나 도움이 되는지 알게되었고, 역시 코딩은 학습과 실습과정이 병행되어야 진정한 내 것이 되는 것을 깨달았습니다.

### 1. 아이디어 구상

- 간단하고 스스로가 가장 평소에 자주 이용하는 컨텐츠를 생각해봤습니다.
- 제가 음악을 생각보다 많이 감상하는데 음악을 고르기는 애매한 상황이 많았습니다.
- 그래서, 간단하게 아래의 기능을 가진 웹을 만들어보고 싶었습니다.
  - 로그인 기능. (서버X)
  - 차트 내의 랜덤 음악 제목과 가수를 매번 접속 시에 출력
  - 음악을 재생하고, 볼륨, 일시정지 등 음악 컨트롤 기능 구현
  - 맘에드는 음악 리스트를 입력해 저장하고 삭제하는 기능 구현

### 2.  구현 과정

**Bootstrap 외의 요소들은 id를 지정해 자식태그나 부모태그를 JS 파일에 불러와 조작해줬습니다.**

#### 1) HTML

- localStorage에서 input 시멘틱태그를 이용해 입력 값을 받을 수 있는 form 태그 작성
- 차트 5위 권 내의 앨범을 bootstrap의 crousal을 이용해 자동으로 넘어가며 출력
- a 태그를 이용해 제목 클릭 시에 음원사이트로 이동, 가수 이름 클릭 시에 가수들의 정보 사이트로 이동
- audio 태그를 이용한 음악 재생 기능

#### 2) CSS

- 고유의 id 값들을 부여해줘 하위 태그들에 각각 css를 통해 가운데 정렬 및 글자 폰트, 글꼴, body 태그의 배경 등을 바꾸도록 해줌.

#### 3) JS

- `login.js`
  - 로그인 ID를 입력하면 setItem을 이용해 localStorage에 저장하고, 로그인 성공 innertext를 넣어줌.
- `bg.js`
  - 간단히 배경화면을 구현하기 위해서 id를 통해 가져와 백그라운드 이미지를 넣어줌.
- `favoritemusics.js`
  - 가장 개인적으로 구현하기 어려웠습니다.
  - 저장한 음악 리스트로 활용할 ul태그에 리스트 태그를 삽입
  - localStorage에 저장하고 직렬화와 역직렬화 과정을 통해 배열의 형태로 바꿔서 저장 후 다음 새로고침 후에도 넘겨줘서 지워지지 않고 목록이 남아있도록 함.
  - 정보를 쏴줄 때, 리스트의 정보의 id와 text를 고유한 현재 날짜로해서 지울 때 해당 id 주소를 가리키는 목록 삭제.

- `recommendations.js`
  - 제목, 가수 정보를 리스트 형태로 저장하고 인덱스를 `math.random`을 활용한 랜덤 음악을 출력하고, 해당 인덱스 순서로 들어간 음악 URL또한 같은 인덱스 순서에 같은 음악이 들어있으므로 audio를 통해 재생.