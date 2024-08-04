import sys
import pygame
import mdesign
import mmodel
import random

def quit_when_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def quit_when_winner(left_score, right_score, points):
    if left_score == points:
        print("\nThe left player won!\n")
        pygame.quit()
        sys.exit()
    if right_score == points:
        print("\nThe right player won!\n")
        pygame.quit()
        sys.exit()

def move_paddle(paddle):
    keys = pygame.key.get_pressed()
    if paddle.side == 'left':
        if keys[pygame.K_w] and paddle.y > 0:
            paddle.y -= paddle.speed
        if keys[pygame.K_s] and paddle.y < mdesign.screen_height - paddle.height:
            paddle.y += paddle.speed
    elif paddle.side == 'right':
        if keys[pygame.K_UP] and paddle.y > 0:
            paddle.y -= paddle.speed
        if keys[pygame.K_DOWN] and paddle.y < mdesign.screen_height - paddle.height:
            paddle.y += paddle.speed

def move_ball(ball, left_paddle, right_paddle, scores):
    ball.x += ball.speed_x
    ball.y += ball.speed_y

    # Ball collision with top and bottom
    if ball.y <= 0 or ball.y >= mdesign.screen_height - ball.size:
        ball.speed_y *= -1
    
    # Ball collision with paddles
    if (left_paddle.x < ball.x < left_paddle.x + left_paddle.width and
            left_paddle.y < ball.y < left_paddle.y + left_paddle.height) or (
            right_paddle.x < ball.x < right_paddle.x + right_paddle.width and
            right_paddle.y < ball.y < right_paddle.y + right_paddle.height):
        ball.speed_x *= -1
    
    # Ball goes out of bounds: put it back in such a way that the interval between balls arriving at paddles stays the same
    if ball.x <= 0:
        ball.x += 2*(left_paddle.initial_pos + left_paddle.width)
        ball.y = mdesign.screen_height // 2
        ball.speed_x *= -1
        ball.speed_y = random.uniform(-7,7)
        scores[1] += 1
    if ball.x >= mdesign.screen_width:
        ball.x -= 2*(right_paddle.initial_pos + right_paddle.width)
        ball.y = mdesign.screen_height // 2
        ball.speed_x *= -1
        ball.speed_y = random.uniform(-7,7)
        scores[0] += 1

def draw_everything(screen, left_paddle, right_paddle, balls):
    screen.display.fill(mdesign.black)
    pygame.draw.ellipse(screen.display, left_paddle.color, (left_paddle.x, left_paddle.y, left_paddle.width, left_paddle.height))
    pygame.draw.ellipse(screen.display, right_paddle.color, (right_paddle.x, right_paddle.y, right_paddle.width, right_paddle.height))
    for ball in balls:
        pygame.draw.ellipse(screen.display, ball.color, (ball.x, ball.y, ball.size, ball.size))
    pygame.draw.aaline(screen.display, mdesign.white, (mdesign.screen_width // 2, 0), (mdesign.screen_width // 2, mdesign.screen_height))

    pygame.display.flip()

def make_paddles_and_balls(number_of_balls = 1):
    left_paddle = mmodel.Paddle('left')
    right_paddle = mmodel.Paddle('right')
    balls = []
    for i in range(number_of_balls):
        balls.append(mmodel.Ball(color = mdesign.colors[i]))
    return (left_paddle, right_paddle, balls)