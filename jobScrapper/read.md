# Python으로 web scraper 만들기

# Module 0 - Introduction

## 0.0 Why learn Python

- 컴퓨터 프로그래밍의 모든 부분에서 활용할 수 있는 강력하고 아름다운 언어이기 때문!
- 조화롭다.

## 0.1 About this course

## 0.2 Requirements

## 0.3 How to Ask for Help

- 질문의 4가지 단계
  - 문제의 목적이 무엇인가? ( 프로젝트의 목적 또는 프로젝트를 해결해 나가는 과정에서 이 단계에서의 목적 )
  - 문제가 정확히 무엇인가? ( 정확히 어떤 에러가 있는가? )
  - 문제 해결을 위해 무엇을 해봤는가?
  - 정확히 어느 부분에서 문제가 발생했는가? ( 정확히 에러의 부분이 어디인가 - 디버그 )

## 0.4 Code Python Online

- repl.it을 통한 python code를 online으로 작업

# Module 1 - Theory

## 1.0 Data Types of Python

- Numbers
- String
  - "~~~~~"
- Boolean
  - True / False
- Float
- None
- python에서의 변수 이름 규칙 - snake case
  - ex) super_long_variable

## 1.1 Lists in Python

## 1.2 Tuples and Dictionary

- sequence types
  - list
    - [] 대괄호 사용 - ex) days = ["mon", "Tue", "Wed", "Thur", "Fri"]
    - mutable sequence,
  - tuple
    - () 괄호 사용 - ex) days = ("mon", "Tue", "Wed", "Thur", "Fri")
    - immutable sequence,
  - dictionary
    - {} 중괄호 사용 - ex) variable = { "key": value }

## 1.3 Built in Function 내장함수

- function은 기능을 반복할 수 있는 것
- 내장함수는 python에 내장되어있는 함수

## 1.4 Creating a Your First Python Function

- python에서 들여쓰기의 의미
- function 정의하기

```
def func_name():
  print("hello")
  print("bye")
```

## 1.5 Function Argument

## 1.7

## 1.8 Keyworded Argument

- Argument
  - default argument value
  - positional Argument
    - 위치에 의존적인 arguement
  - keyword argument
    - parameter의 이름에 의존하는 argument

## 1.6 Returns

- 함수의 결과 값을 반환 -> return문
- return되는 순간 함수가 종료된다.

## 1.9 Code Challenge

## 1.10 Conditionals part 1

- if / else

## 1.11 if else and or

- Boolean Operations 참 거짓 판단
  - and, or, not
- if / elif / else

## 1.12 for Loop

- 사용법

```
days = ("mon", "Tue", "Wed", "Thur", "Fri")
for variable_name in Array_items:
  print(variable_name)
```

## 1.13 Modules

- 다른 언어의 library 같은 것
- 사용법
  - import (module_name)
- 특정 module 가져오기와 이름 바꾸기
  - from (module_name) import (module_name)
  - from (module_name) import (module_name) as (~~)
- 다른 파일을 작성한 후 불러오기도 가능하다. - 직접 module 만들기

# Module 2 - Building a Job Scrapper

## 2.0 What is WEB Scrapping

- web scraping: web상의 데이터를 추출하는 것

## 2.1 What are We Building

- 일자리의 이름과 회사명을 가져오는 web scraper

## 2.2 Navigating with Python

- 1. 원하는 페이지에서 Job Scraping을 하기 위해서 url을 긁어와야한다.
  - python 내장 모듈로 가져올 수 있지만, library를 설치하는 방향으로 진행
  - requests2 - url의 정보
    - .get / requests.text - html 파일
  - beautifulsoup4
    - data 추출 / BeautifulSoup(~~ ,"html.parser")

## 2.3 Extracting Indeed Pages part 1

- request2를 사용해서 url에서 html 정보를 가져오고
- beautifulSoup4를 사용해서 필요한 데이터를 탐색하고 추출함
- list slicing
  - list[0:3] -> index 0 ~ 2 -> [0, 3)

## 2.4 Extracting Indeed Pages part 2

- soup을 이용한 가져온 정보에서 text만 추출하기
  - .string

## 2.5 Requesting Each Page

- 함수를 파일화 시켜서 분할관리하기 ( 분할 정복! )
- & 분할한 파일의 함수 호출
- page URL에 맞는 형식으로 return 받기

## 2.6 Extracting Titles

- URL에서 일자리의 이름인 html 태그를 찾아들어가서 뽑아오기

## 2.7 Extracting Companies

- if/else를 통해서 <span> 태그 안에 <a>가 있는 경우 없는 경우를 나눠서 스크랩

## 2.8 Extracting Locations and Finishing up

- 일자리 세부정보 페이지까지 크롤링
- 함수의 각각의 기능에 집중하지 말고 각 함수가 어떻게 연동해서 동작하고 어떤 태그를 통해 어떤 attribute를 추출하고 있는지에 집중할 것

## 2.9 StackOverflow pages Scraping

- job Scrapper 만들기 단계 다시

  - 1. page 가져오기
  - 2. request 만들기
  - 3. job 추출하기

- 두 웹사이트 모두 동작하는 pagination 함수 따로 구현 해볼 것

## 2.10 StackOverflow extract jobs

- get_text()
  - strip=True 옵션
- stackoverflow job-id 가져오기
- \*\*\*\* soup과 request의 이해

## 2.11 StackOverflow extract job

- find_all( , recursive=False) 태그안에 태그를 받아오지 않게 하기위해 사용
- unpacking value???
- get_text(strip=True).strip("-")

## 2.14 What is the CSV?

- CSV란? -> Comma-Separated Values
  - comma로 열(column)을 나누고, new line으로 행(row)를 나누는 excel의 문서형식
- open file mode
  - encoding = utf-8-sig -> file 저장시, 한글깨짐 현상 해결
  - newline="" -> 파일 저장시, excel 파일에 라인 하나씩 띄우는 현상 해결

## 2.15 Saving to CSV

##

Module #3!

##

# Module 4 - 2020 Python - Job scrapper with Flask

## 4.0 Welcome to 2020 Update Flask!

## 4.1 Introduction to Flask

## 4.2 Dynamic URLs and Templates

- Dynamic URLs
  - page를 생성하고 복잡한 url연동을 flask는 decorator @app.route()로 해결한다.
    - decorator, @ : flask는 @를 통해서 함수를 찾는다.
  - flask의 기능을 활용해서 정적인 url을 사용하는 것이 아닌, 동적으로 변수를 사용하듯 url을 변경해서 사용할 수 있다.
- html Templates
  - html 템플릿을 따로 생성해서 flask의 render_template()을 사용해 웹 페이지를 추가해줄 수 있다.

## 4.3 Forms and Query Arguments

- html <form> tag
  - action
  - method
- query Argument
  - web에 데이터를 보내거나 요청함 / data를 넘겨주는 방식
  - request
  - request get

## 4.4 Scrapper Integration

- 사용자 예외 처리
  - 입력받은 문자 소문자로 바꿔서 받기, word = word.lower()
  - 아무것도 받지 않은 경우 home 화면으로 돌아가기, redirect
- 기존의 job scrapper를 수정
  - 사용자의 입력을 받아서 job을 찾아주는 기능으로 바꾸기 위해서 코드 수정
- Flask를 사용한 웹 페이지에 기존의 Job Scrapper를 통합, 함수조정

## 4.5 Faster Scrapper

- Fake DB ??
