import pygame
import random

# 게임 화면 크기
width = 500
height = 500

# 색상 상수
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 초기화
pygame.init()
window = pygame.display.set_mode((width, height))
window.fill(WHITE)
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

def get_random_position():
    x = random.randrange(0, width - 10, 10)
    y = random.randrange(0, height - 10, 10)
    return (x, y)

def grow_snake(snake_body):
    # 지렁이의 꼬리 부분 좌표
    tail_x, tail_y = snake_body[-1]

    # 지렁이의 꼬리 부분을 몸통 좌표 리스트에 추가
    snake_body.append((tail_x, tail_y))

    return snake_body

def game_loop():
    # 초기 설정
    snake_x, snake_y = 0, 0
    snake_dx, snake_dy = 10, 0
    snake_body = [(snake_x, snake_y)]
    food_x, food_y = get_random_position()
    score = 0

    # 게임 루프
    while True:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # 방향키 입력
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_dx == 0:
                    snake_dx, snake_dy = -10, 0
                elif event.key == pygame.K_RIGHT and snake_dx == 0:
                    snake_dx, snake_dy = 10, 0
                elif event.key == pygame.K_UP and snake_dy == 0:
                    snake_dx, snake_dy = 0, -10
                elif event.key == pygame.K_DOWN and snake_dy == 0:
                    snake_dx, snake_dy = 0, 10

        # 지렁이 이동
        snake_x += snake_dx
        snake_y += snake_dy

        # 경계 처리
        if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
            pygame.quit()
            quit()

        # 먹이 먹기
        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = get_random_position()
            score += 10
            snake_body = grow_snake(snake_body)

        # 지렁이 그리기
        pygame.draw.rect(window, BLACK, (snake_x, snake_y, 10, 10))
        for body_part in snake_body[1:]:
            pygame.draw.rect(window, BLACK, (body_part[0], body_part[1], 10, 10))

        # 먹이 그리기
        pygame.draw.rect(window, RED, (food_x, food_y, 10, 10))

        # 점수 표시
        score_text = font.render("Score: " + str(score), True, WHITE)
        window.blit(score_text, (10, 10))

        # 화면 업데이트
        pygame.display.update()

        # 초당 프레임 수 설정
        clock.tick(15)

if __name__ == '__main__':
    game_loop()
    pygame.quit()
    quit()

