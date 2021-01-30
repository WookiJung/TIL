# Git 명령어



## 처음 만들때

1. touch .gitignore
2. init
3. add
4. commit -m ''
5. remote add origin (처음만)
6. push origin master



## Git 명령어 in terminal

초록색 - commit된거랑 똑같아요.

빨간색 글자 - stage에 안올라간거에요! or 수정사항이 stage에 안올라갔어요!

VS code에서 편집기에 M - Modifed가 있다는것!



- git status 에서 (use 'git restore --staged 파일명' to unstage)라고 적혀있다

  - 해당 명령어를 쓰면 unstaging됨.

  

- git reset

  - -h : help, 무슨 명령어를 쓸 수 있는지에 대해서 나온다.
  - reset --hard : local파일들을 reset시점으로 돌려버림.(origin / master가 찍혀있는 시점까지만 됨)
  - HEAD -> master
    - Master : Commit들 중에 최신판!
    - Branch : branch하는시점에서 나눈 경우의 수가 평행세계로 위상이 갈려버리는거야.
    - HEAD : 내가 지금 있는 위상을 표현한다고 생각하면 돼.

- git branch

  - '*' 가 있는 곳이 지금 있는 세계야
  - branch를 **바꾸려면** git switch {위상} or (git checkout {})(구버전)
    - switch와 만드는거 한꺼번에 하려면 git switch -c {위상}
  - branch를 **만드려면** git branch {위상}
  - Merge 시켜준 뒤에 갈린 위상의 branch는 삭제를 권장함.
    - git branch -d {위상} : merge한 뒤에 지우는것. 그전에는 오류뜸
    - git branch -D {위상} : 쉬프트 딜리트

- git merge

  - master와 branch의 위상을 같게하는 과정이야.
  - 2가지 시나리오
    - Fast-foward : Branch가 간 길을 고대~로 따라걷는 것.
      - git merge home-page(앞에있는 스텝을 쓸것, 즉 branch이름)

- git reflog 

  - git에서 입력한 명령어들을 시간 역순으로 보여주는 것.



## Git push를 파헤쳐보자

git push origin master



origin = 'remote add로 추가한 origin 주소'

master = 'branch name'



### Remote

| Local     | Remote  |
| --------- | ------- |
| Learn_git | git_hub |
|           | git_lab |





