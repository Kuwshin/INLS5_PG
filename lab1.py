import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1000, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FONT = pygame.font.Font(None, 36)

paddle_width, paddle_height = 100, 15
player_x, player_y = WIDTH // 4 - paddle_width // 4, HEIGHT - paddle_height - 15
ball_width = 20
ball_x, ball_y = WIDTH // 2 - ball_width // 2, HEIGHT // 2 - ball_width // 2
ball_speed_x, ball_speed_y = 6, -6

paddle_speed = 8
score = 0

game_running = True

btn_restart = pygame.Rect(WIDTH -90, 10, 120, 30)

def reset_game():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, score, game_running
    ball_x, ball_y = WIDTH // 2 - ball_width // 2, HEIGHT // 2 - ball_width // 2
    ball_speed_x, ball_speed_y = 6, -6
    score = 0
    game_running = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if btn_restart.collidepoint(event.pos):
                    reset_game()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= paddle_speed
    elif keys[pygame.K_d] and player_x < WIDTH - paddle_width:
        player_x += paddle_speed

    if game_running:
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_y <= 0 or ball_y >= HEIGHT - ball_width:
            ball_speed_y *= -1
        if ball_x <= 0 or ball_x >= WIDTH - ball_width:
            ball_speed_x *= -1

        if (player_y <= ball_y + ball_width <= player_y + paddle_height) and \
           (player_x < ball_x + ball_width/2 < player_x + paddle_width):
            score += 1  # увеличение счета игры
            ball_speed_y *= -1 

        if ball_y >= HEIGHT - ball_width:
            score = 0
            game_running = False

    window.fill(WHITE)
    pygame.draw.rect(window, RED, (player_x, player_y, paddle_width, paddle_height))
    pygame.draw.ellipse(window, RED, (ball_x, ball_y, ball_width, ball_width))

    pygame.draw.rect(window, RED, btn_restart)
    restart_txt = FONT.render("Restart", True, BLACK)
    window.blit(restart_txt, (btn_restart.x + 5, btn_restart.y + 5))

    score_display = FONT.render("Score: " + str(score), True, BLACK)
    window.blit(score_display, (WIDTH - 120, 50))

    pygame.display.flip()
    pygame.time.Clock().tick_busy_loop(60)

