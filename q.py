import pygame
import time
import random
import sys
import os  # os 모듈 추가

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


# titleImg = pygame.image.load("images/메인로고.jpg ") # 메인 로고
# startImg = pygame.image.load("images/시작버튼.png") # 시작 버튼
# quitImg = pygame.image.load("images/종료버튼.png") # 종료 버튼
# clickStartImg = pygame.image.load("images/시작버튼2.png") # 마우스 가져다 대면 바뀌는 시작 버튼
# clickQuitImg = pygame.image.load("images/종료버튼2.png") # 마우스 가져다 대면 바뀌는 종료 버튼

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



class Snake:
    def __init__(self):
        self.length = 3
        self.positions = [(start_xpos, start_ypos)]
        self.direction = EAST

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        # 새로운 머리(몸통) 생성
        new = (cur[0] + (x * grid), cur[1] + (y * grid))
        if self.length > 2 and new in self.positions:
            gameover()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, BLACK, (p[0], p[1], grid, grid))


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        x = random.randint(0, grid_width - 1) * grid
        y = random.randint(0, grid_height - 1) * grid
        self.position = (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface,RED, (self.position[0], self.position[1], grid, grid))


def draw_grid(surface):
    for row in range(0, int(grid_height)):
        for col in range(0, int(grid_width)):
            if (row + col) % 2 == 0:
                rect = pygame.Rect((col * grid, row * grid), (grid, grid))
                pygame.draw.rect(surface, GREEN4, rect)
            else:
                rect = pygame.Rect((col * grid, row * grid), (grid, grid))
                pygame.draw.rect(surface, GREEN5, rect)


def draw_Score(surface):
    global score

    font = pygame.font.Font(font_path, 23)  # 변경된 부분
    text = font.render(f"score:{score}", True, (0, 0, 255))
    surface.blit(text, (20, 20))

def draw_timer(surface, start_time):#추가!!
    elapsed_time = pygame.time.get_ticks() - start_time
    font = pygame.font.Font(font_path, 23)
    text = font.render(f"Time: {elapsed_time // 1000}  s", True, (0, 0, 0))
    surface.blit(text, (window_width - 140, 20))




def gameover():
    font = pygame.font.Font(font_path, 50)  # 변경된 부분

    text1 = font.render("Game Over", True, (0, 0, 255))
    screen.blit(text1, (160, 190))

    font2 = pygame.font.Font(font_path, 15)  # 폰트 크기를 30으로 설정
    text2 = font2.render("Press Enter or Space to Restart", True, (0, 0, 255))
    screen.blit(text2, (167, 260))  # 텍스트의 위치를 조정

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:  # 엔터나 스페이스를 눌렀을 때
                    main()

def main():
    global score
    score = 0
    start_time = pygame.time.get_ticks()
    pygame.mixer.pre_init(22050, -16, 2, 512)
    pygame.init()
    pygame.mixer
    snake = Snake()
    food = Food()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake.direction != SOUTH:
                        snake.direction = NORTH
                elif event.key == pygame.K_DOWN:
                    if snake.direction != NORTH:
                        snake.direction = SOUTH
                elif event.key == pygame.K_LEFT:
                    if snake.direction != EAST:
                        snake.direction = WEST
                elif event.key == pygame.K_RIGHT:
                    if snake.direction != WEST:
                        snake.direction = EAST
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        if snake.get_head_position()[0] < 0 or snake.get_head_position()[0] >= window_width or \
                snake.get_head_position()[1] < 0 or snake.get_head_position()[1] >= window_height:
            gameover()

        surface.fill((0, 0, 0))
        draw_grid(surface)
        snake.draw(surface)
        food.draw(surface)
        draw_Score(surface)
        draw_timer(surface, start_time)
        screen.blit(surface, (0, 0))
        clock.tick(15)
        pygame.display.flip()
