# django로 만든 프로젝트를 DRF로 변환한 프로젝트


<br>

## 1. 프로젝트 소개
개발은 초기 세팅부터 전부 직접 구현했으며, 탈잉의 기능(여행 및 액티비티 리스트, 검색 필터링, 호스트 등록 등)을 대한민국의 실제 여행 및 액티비티 데이터를 모티브로 만든 프로젝트입니다.

---
<br>

## 2. 데이터 모델링
<img width="776" alt="스크린샷 2021-09-15 오후 2 38 45" src="https://user-images.githubusercontent.com/81137234/133376890-0b243a3a-15dd-44a0-b025-662fb4044182.png">

---
<br>

## 3. 엔드포인트 API 문서화
링크 : (https://documenter.getpostman.com/view/16450899/U16oo3QC)

<img width="1264" alt="스크린샷 2021-09-15 오후 3 45 15" src="https://user-images.githubusercontent.com/81137234/133383978-9b24f9e5-cd14-466f-b363-86d9e4e1033c.png">

---
<br>

## 4. 구현 기능
회원가입, 로그인, CRUD, Filter, q 객체, Eager Loading을 적용하였습니다.


### 1) 회원가입
- 헬퍼클래스인 UserManger를 사용하여 일반 user 객체를 생성하는 모델을 작성했습니다.
- AbstractBaseUser를 상속하여 DRF의 기능인 password 자동 구현 기능을 사용하였습니다
- AUTH_USER_MODEL을 settings.py에 입력하여 migration 시 발생할 수 있는 오류를 방지했습니다.
- 회원가입 시 입력받은 데이터 검증을 위해 validated_data(유효성 검증)을 통해 User 객체를 생성했습니다.

### 2) 로그인
- rest_framework에서 제공하는 JWT token으로 사용자를 구분하였습니다.

### 3) Product CRUD 기능
- 글 생성 시 id 값을 자동으로 부여하기 때문에 id 필드는 작성하지 않았습니다.
- 객체지향적으로 코드를 작성하기 위해 model 디렉토리를 생성 후, class 객체를 나눠서 작성했습니다.
- ViewSet에서 사용한 create메소드의 커스터마이징이 필요해 perform_create 메소드를 사용해 기존의 create 함수를 재정의하였습니다.
- Filter, Q 객체를 사용하여 사용자가 조건에 맞는 결과를 조회 가능
- Eager Loading(Selected_related) 사용하여 Query hit 감소

### 4) Like 기능
- perform_create 메소드를 사용해  ViewSet의 create 함수를 재정의하였습니다.
- 사용자가 이미 좋아요를 눌렀으면 좋아요 기록을 삭제하는 기능을 추가했습니다.

---
<br>

## Reference
- 이 프로젝트는 탈잉 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무 수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.

<br>