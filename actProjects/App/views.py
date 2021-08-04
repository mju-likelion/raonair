from django.http import JsonResponse
from django.shortcuts import render
from . import models

import base64
import os

# Create your views here.


# 홈페이지 공연 추천
def home(request):
    return JsonResponse({"request": 'searchPage.html'})


# 검색결과 페이지
def search(request):
    return JsonResponse({"request": 'searchPage.html'})


# 검색결과 페이지, 더보기 클릭
def search_detail(request):
    return JsonResponse({"request": "detailpage.html"})


# 극단 개별 페이지
def troupe(request):
    return JsonResponse({"request": "listpage.html"})


# 연극 개별 페이지
def play(request, id):
    play = models.Play.objects.get(id=id)
    star = models.Star.objects.filter(play=id)  # 데이터들의 리스트
    staff = models.Staff.objects.filter(play=id)
    like = models.Like.objects.filter(play=id).count()
    comment = models.Comment.objects.filter(play=id)

    # 별점 갯수
    star_count = 0
    for i in range(len(star)):
        star_count += star[i].star

    # 별점 평균 리스트
    avg = star_count/len(star)/2

    # 찜 갯수
    # like_cnt = 0
    # for i in range(len(like)):
    #     like_cnt += like[i].like #찜 갯수 컬럼 없음

    # 리뷰
    review = []
    for i in range(len(comment)):
        review.append({"nickname": comment[i].user.nickname, "comment": comment[i].comment})
    # "date": comment.date}) # date 컬럼 없음

    # 관련정보더보기 링크 리스트
    link = []
    if play.yes24_external_link is not None:
        link.append({"name": 'yes24', "link": play.yes24_external_link})
    if play.interpark_external_link is not None:
        link.append({"name": 'interpark', "link": play.interpark_external_link})
    if play.playdb_external_link is not None:
        link.append({"name": 'playDB', "link": play.playdb_external_link})
    if play.culturegov_external_link is not None:
        link.append({"name": 'cultureGov', "link": play.culturegov_external_link})

    # 배우 및 극단 프로필 리스트
    staffs = []
    for i in range(len(staff)):
        staffs.append({"name": staff[i].person.name, "position": staff[i].role, "photo": staff[i].person.photo})

    return JsonResponse({
        "data": {
            "play": {
                "name": play.title,  # 연극이름
                "poster": play.poster,  # 포스터 링크
                # "like_cnt": like_cnt,  # 찜수
                "star_avg": avg,  # 평균 별점
                "star_cnt": star_count,  # 별점수
                "time": play.running_time,  # 공연시간
                "start_date": play.start_date,  # 공연시작일
                "end_date": play.end_date,  # 공연시작일
                "external_links": link,  # 관련정보더보기 링크
                "staff": staffs,  # 배우 및 극단 프로필
                "review": review,  # 리뷰 및 커멘트
                "location": play.location,  # 위치 theater로 바뀔 수 있음
                # "context": {
                # "like_check": boolean,
                # "rating": number | | null,
                # }
            }
        }
    })


# 로그인
def signin(request):
    return JsonResponse({"request": "listpage.html"})


# 회원가입
def signup(request):
    return JsonResponse({"request": "listpage.html"})


# 비밀번호 찾기
def password(request):
    return JsonResponse({"request": "listpage.html"})


# 연극 찜하기
def playlike(request):
    return JsonResponse({"request": "listpage.html"})


# 극단 찜하기
def troupelike(request):
    return JsonResponse({"request": "listpage.html"})


# 별점평가
def star(request):
    return JsonResponse({"request": "listpage.html"})


# 커멘트 달기
def comment(request):
    return JsonResponse({"request": "listpage.html"})
