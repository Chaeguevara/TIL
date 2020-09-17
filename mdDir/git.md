# Git

> Git은 분산형 버전관리 시스템(DVCS) 중 하나이다

## Git 사전 준비

> 최초 커밋을 남기는 사람에 대한 설정

```bash
$ git config --global user.name '{username}'
$ git config --global user.emai '{email}'
```

- 추후에 commit을 하면, 작성한 사람(author)로 저장된다.
- email 정보는 github에 등록된 이메일로 설정 추천.
- 설정 확인 하기 위한 명령어

```bash
$ git config --global -l
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
filter.lfs.clean=git-lfs clean -- %f
user.name=Chaeguevara
user.email=dfso2222@gmail.com

```

> git bash 설치[링크]()

## 기초흐름

> 작업 -> add -> commit

### 0. 저장소 설정

```bash
$ git init
Initialized empty Git repository in D:/Users/dfso2/Desktop/test2/.git/
```

- git 저장소를 만들게 되면 해당 디렉토리 내에 `.git/` 폴더가 생성
- git bash에서는 `(master)`로 현재 작업중인 브랜치가 표시된다.

### 1. `add`

> 커밋을 위한 파일 목록(staging area)

```bash
$ git add . #현재 디렉토리의 모든 파일 및 폴더
$ git add a.txt #특정 파일
$ git add md-images/ #특정 폴더
$ git status
# 마스터 브랜치에 있다.
On branch master
# 아직 커밋이 없다.
No commits yet

#Staging area 에 위치한 변화들
Changes to be committed:

  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt
        
# Tracking 되지 않음 = Working directory에 있다.        
Untracked files:
	# Staging area로 보내려면, add 명령어 입력.
  (use "git add <file>..." to include in what will be committed)
        b.txt

```

### 2.`commit`

> 버전을 기록(스냅샷)

```bash
$ git commit -m '커밋메시지'
[master (root-commit) 969b991] Test2 commits
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt

```

- 커밋 메시지는 현재 버전을 알 수 있도록 명확하게 작성한다.
- 커밋 이력을 남기기 확인하기 위해서는 아래의 명령어를 입력한다.

```bash
$ git log
$ git log -1 #최근 한개의 버전
$ git log --oneline #한줄로 간단하게 표현
$ git log -1 --oneline
```



## 상태확인

> git에 대한 모든 정보는 status에서 확인 할 수 있다.

```bash
$ git status
```

## 원격 저장소 활용하기

> 원격 저장소를 제공하는 서비스는 github, gitlab, bitbucket 등이 잇다.

### 1. 원격 저장소 설정하기

```bash
$ git remote add origin {URL}
```

- 깃아, 원격(remote)저장소로 추가해줘(add) origin이라는 이름으로 URL을

### 2. 원격 저장소 확인하기

```bash
$ git remote -v
origin  https://github.com/Chaeguevara/git_test.git (fetch)
origin  https://github.com/Chaeguevara/git_test.git (push)

```

### 3. push

```bash
$ git push origin master
```

- origin 원격저장소의 master 브랜치로 push

