
# -*- coding: utf-8 -*-

"""
mp3 처럼 음악 재생 플레이 리스트를 만든다.
"""

"""
dictionary에 정보를 저장해서 이 정보를 토래도 mp3를 저장하고 파일을 실행시키는 연습을 하자
좋아요 순으로,최신 듣던 곡,날짜순,이름로 순으로 각 각 구현해보고 각 순위에 맞게 리스트를 정리해
"""
#dictionary
#key,value
FIFA = {"title":"FIFA1","list_num":101,"location":"/home/at05/FIFA1.mp3","like":1088880,"name":"FIFAonline4"}
FIFA2 = {"title":"FIFA2","list_num":102,"location":"/home/at05/FIFA2.mp3","like":80,"name":"FIFAonline4"}
KartRider = {"title":"KartRider1","list_num":103,"location":"/home/at05/KartRider1.mp3","like":18000,"name":"KartRider"}
KartRider2 = {"title":"KartRider2","list_num":104,"location":"/home/at05/KartRider2.mp3","like":800,"name":"KartRider"}

music_list = [FIFA,FIFA2,KartRider,KartRider2]
a = input()

if(a == 'list_num'):
    for x in range(len(music_list)):

        for i in range(len(music_list)-1):

            if(music_list[i]["list_num"] < music_list[i+1]["list_num"]):

                music_list[i],music_list[i+1] = music_list[i+1],music_list[i]

print(music_list)
if(a == 'like'):

    for i in range(len(music_list)):

        for x in range(len(music_list)-1):

            if(music_list[x]["like"] < music_list[x+1]["like"]):

                music_list[x],music_list[x+1] = music_list[x+1],music_list[x]
print(music_list)

import pygame
import time
pygame.init()
pygame.mixer.music.load(music_list[2]['location'])
pygame.mixer.music.play()
time.sleep(60)
















































































































































































































































































































































