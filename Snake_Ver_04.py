import pygame
import time
import random
import sys
import os  # os 모듈 추가
from q import main
# 폰트 파일의 절대 경로
font_path = os.path.join('../PySNAKE/font', 'Gameplay.ttf') # 모든 컴퓨터에서 실행이 가능하도록 위치 설정을 변경
# font_path = os.path.join('/Users/macbookpro/Downloads/SnakePRJ', 'Gameplay.ttf')

# 초기화
pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 512)
pygame.font.init()

# 폰트 객체 생성
font = pygame.font.Font(font_path, 32)  # 폰트 파일의 경로와 크기를 지정

# 시작 메뉴 창 설정
white = (255, 244, 238) #창 배경색

# 이미지 파일의 절대 경로
image_path = os.path.join('../PySNAKE', 'images')  # 모든 컴퓨터에서 실행이 가능하도록 위치 설정을 변경

titleImg = pygame.image.load(os.path.join(image_path, "메인로고.jpg"))  # 메인 로고
startImg = pygame.image.load(os.path.join(image_path, "시작버튼.png"))  # 시작 버튼
quitImg = pygame.image.load(os.path.join(image_path, "종료버튼.png"))  # 종료 버튼
clickStartImg = pygame.image.load(os.path.join(image_path, "시작버튼2.png"))  # 마우스 가져다 대면 바뀌는 시작 버튼
clickQuitImg = pygame.image.load(os.path.join(image_path, "종료버튼2.png"))  # 마우스 가져다 대면 바뀌는 종료 버튼

# 메뉴 창 크기 설정
display_width = 640
display_height = 480
gameDisplay = pygame.display.set_mode((display_width, display_height))

# 창 크기 설정
window_width = 640
window_height = 480
start_xpos = 100
start_ypos = int(window_height / 2)

grid = 20
grid_width = int(window_width / grid)  # 32
grid_height = int(window_height / grid)  # 24

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
surface = pygame.Surface(screen.get_size())
surface = surface.convert()

# 색깔
RED = (255, 0, 0)
GREEN5 = (4, 194, 45)
GREEN4 = (2, 179, 76)
BLACK = (0, 0, 255)

# 방향
NORTH = (0, -1)
SOUTH = (0, 1)
WEST = (-1, 0)
EAST = (1, 0)

# 시간
clock = pygame.time.Clock()
# 스코어
score = 0
running = True

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(gameDisplay, color, (x, y, width, height))  # 버튼 그리기
        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # 마우스가 버튼 위에 있을 때
            pygame.draw.rect(gameDisplay, hover_color, (x, y, width, height))  # 버튼 색상 변경
            if click[0] and action != None:  # 버튼을 클릭했을 때
                time.sleep(1)
                action()
        font = pygame.font.Font(font_path, 20)  # 폰트 크기를 20으로 설정
        text = font.render(text, True, (255, 255, 255))  # 텍스트 렌더링
        gameDisplay.blit(text, (x + (width / 2 - text.get_width() / 2), y + (height / 2 - text.get_height() / 2)))  # 텍스트 그리기

def startgame():
    main()
def quitgame():
    pygame.quit()
    sys.exit()

def mainmenu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)

        titleimg = gameDisplay.blit(titleImg, (30, -50))
        startButton = Button("Start", 270, 300, 100, 50, (0,0,0), (0,255,0), startgame)  # 'Start' 텍스트 버튼, 초록색으로 변경됨
        quitButton = Button("Quit", 270, 370, 100, 50, (0,0,0), (255,0,0), quitgame)  # 'Quit' 텍스트 버튼, 빨간색으로 변경됨
        pygame.display.update()
        clock.tick(60)

mainmenu()

