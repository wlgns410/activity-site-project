# iltal Django-Rest-Framework Project


<br>

## 1. 프로젝트 소개
개발은 초기 세팅부터 전부 직접 구현했으며, 탈잉의 기능을 재구성해 여행 & 액티비티 사이트로 바꾼 프로젝트입니다.

---
<br>

## 2. 데이터 모델링
<img width="776" alt="스크린샷 2021-09-15 오후 2 38 45" src="https://user-images.githubusercontent.com/81137234/133376890-0b243a3a-15dd-44a0-b025-662fb4044182.png">

---
<br>

## 3. 엔드포인트 API 문서화
링크 : (https://documenter.getpostman.com/view/16450899/U16oo3QC)

<img width="1263" alt="스크린샷 2021-09-17 오전 11 24 00" src="https://user-images.githubusercontent.com/81137234/133714208-8f4e76dd-c694-4267-8ec9-33cd46663c73.png">


---
<br>

## 4. 구현 기능
회원가입, 로그인, CRUD, Filter, q 객체, Eager Loading을 적용하였습니다.


### 1) 회원가입
- 헬퍼클래스인 UserManger를 사용하여 일반 user 객체를 생성하는 모델을 작성했습니다.
- AbstractBaseUser를 상속하여 DRF의 기능인 password 자동 구현 기능을 사용하였습니다.
- AUTH_USER_MODEL을 settings.py에 입력하여 migration 시 발생할 수 있는 오류를 방지했습니다.
- 회원가입 시 입력받은 데이터 검증을 위해 validated_data(유효성 검증)을 통해 User 객체를 생성했습니다.

### 2) 로그인
- rest_framework에서 제공하는 JWT token으로 사용자를 구분하였습니다.

### 3) Product CRUD 기능
- 객체지향적으로 코드를 작성하기 위해 model 디렉토리를 생성 후, class 객체를 나눠서 작성했습니다.
- ViewSet에서 사용한 create메소드의 커스터마이징이 필요해 perform_create 메소드를 사용해 기존의 create 함수를 재정의하였습니다.
- Filter, Q 객체를 사용하여 사용자가 조건에 맞는 결과를 조회 가능하게 만들었습니다.
- Eager Loading(Selected_related) 사용하여 Query hit를 감소시켰습니다.

### 4) Like 기능
- perform_create 메소드를 사용해  ViewSet의 create 함수를 create, put 메소드 기능을 하게 만들었습니다.
- 사용자가 이미 좋아요를 눌렀으면 좋아요를 해제하도록 만들기 위해 delete를 사용했습니다.

---
<br>

## Reference
- 이 프로젝트는 탈잉 사이트를 참조하여 학습목적으로 만들었습니다.

<br>
