#_*_ coding: utf-8 _*_
import pygame
import time
import random

#초기화
pygame.init()
#게임의 화면 크기를 조정하는 변수
display_width = 1024
display_heigt = 768
#RGB COLOR 를 지정해준다.
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bright_red = (255,153,153)
green = (0,128,0)
bright_green = (0,255,0)
block_color = (53,115,255)
blue = (0,0,255)
bright_blue = (0,216,255)

#자동차 이미지 크기(폭)
car_width = 73
gameDisplay = pygame.display.set_mode((display_width,display_heigt))
#게임 제목 설정수 하는 함수
pygame.display.set_caption("KartRider")
clock = pygame.time.Clock()
#이미지를 불러오는 부분(나중에 절대 경로로도 해봐야 한다.)
carImg = pygame.image.load("race.jpeg")
def things_dodged(count):
    #이미지의 폰트를 설정하는 함수
    font = pygame.font.SysFont(None,25)
    #어떻게 표시할지 설정하는 함수
    text = font.render("score " + str(count),True,black)
    #실제로 이미지를 화면에 띄우는 함수
    gameDisplay.blit(text,(0,0))
#방해물을 만드는 함수
def things(thingx,thingy,thingw,thingh,color):
    #좌표를 입력받아 물체를 그리는 함수
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
#자동차의 이미지를 그리는 함수
def car(x,y):
    #자동차의 이미지와 x,y의 좌표를 입력받아서 그린다.
    gameDisplay.blit(carImg,(x,y))
#문자를 어떻게 표시할지 정보를 가지고 있는함
def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()
#어덯게 문자를 화면에 띄울지 결정하는 함수
def message_display(text):
    #font,크기를 결정하는 함수
    largeText = pygame.font.Font("freesansbold.ttf",115)
    #text object 함수 만든것을 이용해서 어떻게 표시할지 정보를 가져오는 함수
    TextSurf,TextRect = text_objects(text,largeText)
    #텍스트를 가운데 맞추기 위한 설정 이 부분을 변경시키면 글자가 다른 위치에 띄워준다
    TextRect.center = ((display_width/2),(display_heigt/2))
    #실제로 화면에 그려지는 부분
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    #2초동안 멈춘다
    time.sleep(1)
    #그 다음 실행될 함수를 설정해 준것
    game_loop()

def crash():
    #충돌 날때 문자를 화면에 띄워준다.

    message_display("crashed")
#버튼을 클릭시 작동하는 함수, when button click action function
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #마우스 클릭 이벤트가 들어왔을때 처리하는 함수
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if(click[0] == 1 and action !=None):
            action()
    else:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf,textRect = text_objects(msg,smallText)
    textRect.center = ((x+ (w/2)),(y + h/2))
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms.ttf",115)
        TextSurf,TextRect = text_objects("KartRider",largeText)
        TextRect.center = ((display_width/2),display_heigt/2)
        gameDisplay.blit(TextSurf,TextRect)
        button("!!!Go!!!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        button("button",0,0,255,bright_blue,button123)
        pygame.display.update()
        clock.tick(15)
def button123():
    message_display("button")
def quitgame():
    pygame.quit()
    quit()


def game_loop():
    # x,y 는 차의 초기 위치를 설정해 주기 위해서 만든 변수
    x = (display_width * 0.45)
    y = (display_heigt * 0.8)

    x_change = 0

    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thing_count = 1
    score = 0

    gameExit = False
    #game 이 나가기 전까지 반복문을 돌면서 해당 명령어들을 수행한다.
    while not gameExit:
        #키 입력 받는거에 따라 해당 명령어를 수행하는 코드를 짠다.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        gameDisplay.fill(white)
        #방해물을 만드는 함수를 적어준다.
        things(thing_startx,thing_starty,thing_width,thing_height,block_color)

        thing_starty += thing_speed
        #차의 위치를 변화시켜주는 함수
        car(x,y)
        things_dodged(score)
        #화면 위치에 따라 차가 충돌이 일어났는지 안일어났는지 판단하는 부분
        if x > display_width - car_width or x < 0:
            crash()
        if thing_starty > display_heigt:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            #점수를 증가 시켜 주는 부분
            score += 1
            #물체가 시간이 갈수록 빨리 나오도록 변경 시켜주는 변수
            thing_speed += 1
            thing_width += (score * 1.2)
        #물체와 자동차가 충돌이 일어났나 안알어났나 확인하는 부분
        if y < thing_startx + thing_height:
            print("y croosover")

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print("x crossover")
                crash()
        #frame 마다 화면을 갱신 시켜주는 부분
        pygame.display.update()

        clock.tick(60)
game_intro()



"""
숙제
1.변수 변경해서 게임 작동시키기
2.30계단 1문제풀기

선생님 메일
tompx@naver.com
"""

