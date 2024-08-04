import pygame
import mfunctions
import mmodel

def try_to_play():
    while True:
        try:
            number_of_balls = int(input('\nWith how many balls do you want to play? '))
            points = int(input('\nAnd how many points are necessary to win? '))
            game = Play(number_of_balls, points)
            game.play_game()
        except IndexError:
            print('We don\'t have that many colors for that many balls, please choose a maximum of 7 balls.')
            continue
        except Exception as e:
            print(f'This error occurred: {e}. Please try again')
            continue

class Play:
    def __init__(self, number_of_balls = 1, points = 5):
        self.number_of_balls = number_of_balls
        self.points = points
    def play_game(self):
        clock = pygame.time.Clock()
        frame_count = 0
        (left_paddle, right_paddle, balls) = mfunctions.make_paddles_and_balls(self.number_of_balls)
        screen = mmodel.Screen()
        scores = [0, 0]
        while True:
            frame_count += 1

            mfunctions.quit_when_close()
            mfunctions.quit_when_winner(scores[0], scores[1], self.points)

            mfunctions.move_paddle(left_paddle)
            mfunctions.move_paddle(right_paddle)

            # Balls should start moving with delay
            for i in range(len(balls)):
                if frame_count > 2*(i/len(balls))*(right_paddle.x-left_paddle.x-left_paddle.width-right_paddle.width)/abs(balls[0].speed_x):
                    mfunctions.move_ball(balls[i], left_paddle, right_paddle, scores)

            mfunctions.draw_everything(screen, left_paddle, right_paddle, balls)
            
            clock.tick(60)