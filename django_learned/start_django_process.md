# django 프로젝트 만드는 순서

1. 프로젝트를 생성하려는 디렉토리에서 `git bash`
2. 빈폴더(프로젝트 Root)를 만든다.
   1. `.gitignore` 생성
   2. `$ git init` 으로 REPO 초기화
   3. `README.md` 생성
   4. 원격 저장소 생성 후 연결
   5. `add` => `commit` => `push` 
3. 해당 폴더로 이동해서 `$ python -m venv venv` 명령어를 통해 가상독립환경 폴더를 만든다.
4. 가상독립환경을 활성화(`$ source venv/Scripts/activate`)한다. (or vscode 로 열기) 
5. `$ pip install django (+ a)` 를 통해 필요한 패키지들을 설치 한다.
6. `$ django-admin startproject <PROJECT NAME> .` 명령어를 통해 프로젝트 초기화
7. 프로젝트 vscode로 열어서 진행



## 프로젝트 열기

반드시 프로젝트 Root 폴더 => 우클릭 => Code로 열기



## 프로젝트 독립환경 설정

1. `ctrl` + `shift` + `p`
2. `>python: Select Interpreter` 입력
3. 자동으로 가상환경 폴더(`venv/`)안의 python을 잡지 못한다면
   1. `Enter interpreter path` => `find` => `venv/Scripts/python` 을 선택
4. 완료 이후 좌하단에 `Python 3.8.x 64-bit('venv')` 문구를 확인
5. 터미널 프롬프트에 `(venv)` 반드시 확인 후 진행

