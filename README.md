# 🎯DOCUMOVE (ongoing)

환경다큐멘터리 정보제공, 후원 프로젝트
<br/>
<br/>
환경 다큐멘터리와 후원기능을 연결하는 사이드 프로젝트입니다.  
다큐멘터리 정보를 제공함과 동시에, 도움이 필요한 관련 후원 프로젝트를 연결지었습니다.   
상세페이지에는 댓글의 작성/수정/삭제가 가능한 기본적인 커뮤니티 기능이 포함되어 있습니다.
<br/>
<br/>
필수적으로 구현해야 하는 기능과 서비스 차별화 간의 공존을 고민하였습니다.   
"영화 추천에 무게를 두고 기능을 구현할까?"   
"좋아요 기능을 달아서 그 데이터를 기반으로 추천할 것인가?"   
"혹은 회원 가입할 때 좋아하는 장르를 입력받을까?"  
모두 식상하게 느껴졌습니다.
<br/>
<br/>
권장 주제인 영화에서 벗어나, 큰 사회적 가치를 창출하고 싶었습니다.   
가치있는 일을 한다는 믿음은 때로 힘든 순간을 견디는 버팀목이,  
프로젝트에 몰입하게 하는 촉매제가 될 수 있음을 경험한 바 있습니다.
<br/>
<br/>
궁리 끝에 어릴 적 보았던 `planet earth [BBC]`와 `해피빈 [네이버]` 를 이을 수 있는 플랫폼이 있으면 어떨까 생각해보았습니다.  
메인페이지는 `Netflix` 프론트를 참고하여 영상 썸네일을 카드 형식으로 제시하고,  
상세페이지는 `Youtube`와 `해피빈` 프론트를 참고하여 영상 컴포넌트를 후원 프로젝트 카드로 대체하였습니다.  
<br/>
<br/>
이를 통해 "재미있는 다큐멘터리 없나?" 하는 사람에게 사용자 경험을 제공함과 동시에,  
환경후원 프로젝트와 직접적으로 연결지어 실제 후원으로 유도하는 것을 목표하였습니다.  
사용자의 머릿 속에 찬 위기의식과 감상이 빠르게 휘발되기 전에, 자연스럽게 후원으로 유도하는 것이  
`documove` 서비스의 조용하지만 강력한 경쟁력이라고 생각했기 때문입니다.  
<br/>
<br/>
아이디어부터 실제 구현까지, 우리가 고민했던 시간들은 본인에게 새겨져 또다른 사회적 기여를 고민하는 우리 자신을 만들 것입니다.


## Contributors
이성우 `seanwoory`, 최태호 `cho1taeho`


## Requirements

- Vue.js, vuex, vue-router
- Django

frontend, backend 폴더 내의 package.json, requirements.txt에 필요한 모듈이 명시되어 있습니다.


## Getting Started


### 각각의 폴더로 들어간 뒤 터미널에 명령을 입력하세요.

- backend 폴더에서
  - `python -m venv venv`
  - `source venv/Scripts/activate`
  - 최초 실행할 경우 꼭 수행
    - 데이터베이스 생성
      - `python manage.py migrate`
    - json 데이터를 DB에 dump
      - `python manage.py loaddata movies/fixtures/tmdb.json`
  - `python manage.py runserver`
- frontend 폴더에서
  - `npm i`
  - `npm run serve`


## Note

Youtube API를 발급받으신 후, frontend 루트 디렉토리에 .env.local 파일을 만들어 주세요.

```
.env.local

VUE_APP_YOUTUBE_API=your_youtube_api_key
```