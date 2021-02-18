# 뷰 : 기능을 담당(페이지 단위) - 로그인, 쇼핑 페이지
# 화면이 나타나는 뷰( 템플릿이 있는 뷰) - 로그인 페이지, 화면이 없는 뷰( 템플릿이 없는 뷰 ) - ajax 로 콜하는 뷰 등, 비밀번호 검증 등
# 화면이 있건 없건 주소가 있어야 한다.

# 뷰 동작하려면 ?? 함수 또는 클래스, 와 url 필요

# 뷰의 코드 형식 : 함수형, 클래스형
# 함수형 : request 를 매개변수를 받음 requests 는 사용자 쿠키 등 정보 담겨있음
#         내가 원하는 대로 동작들을 설계하고 만들고 싶을 때

# 클래스형 : CRUD 등 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고 상속받아서 사용한다.
# 장고의 제네릭 뷰를 많이 사용
from django.http import HttpResponse
from django.shortcuts import render

# 함수형 예제
def index(request):
    # 어떤 계산, 데이터베이스 조회, 수정, 등록
    # 응답 메세지를 만들어서 반환.
    # html 변수 대신 템플릿 가능
    html = "<html><body>Hi django</body></html>"
    return HttpResponse(html)

def welcome(request):
    html = "<html><body>Welcome to django</body></html>"
    return HttpResponse(html)

def template_test(request):
    # 기본 템플릿 폴더
    # 1. admin 앱
    # 2. 각 앱의 폴더에 있는 templates 폴더
    # 3. 여러분이 설정한 폴더
    return render(request, 'test.html')  # 뒤에 .html 은 템플릿 이름

# 함수형 뷰 만들기, 템플릿 만들기, url 연결하기, 브라우저로 접속해보기