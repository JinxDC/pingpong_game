import arcade
import random



WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600



class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/ball.png", 0.1)
        self.center_x = WINDOW_WIDTH/2
        self.center_y = WINDOW_HEIGHT/2
        self.change_x = 9
        self.change_y = 5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.right > WINDOW_WIDTH or self.left < 0:
            self.change_x = -self.change_x

        if self.top > WINDOW_HEIGHT:
            self.change_y = -self.change_y

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/bar.png",0.1)
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = 0
        self.change_x = 0

    def update(self):
        self.center_x += self.change_x
        if self.right > WINDOW_WIDTH:
            self.right = WINDOW_WIDTH
        if self.left < 0:
            self.left = 0

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball()
        self.bar = Bar()
        self.score = 0
        self.game = "game"

    def on_draw(self):
        self.clear((0, 100, 0))
        self.ball.draw()
        self.bar.draw()
        arcade.draw_text(f"Score:{self.score}", 50, WINDOW_HEIGHT-50, (0, 0, 0), 16)

        if self.game == "lose":
            arcade.draw_text(f"Game over", 0, WINDOW_HEIGHT/2, (255, 0, 0), 70, WINDOW_WIDTH, "center")

        if self.game == "win":
            arcade.draw_text(f"You win", 0, WINDOW_HEIGHT / 2, (0, 255, 0), 70, WINDOW_WIDTH, "center")

    def update(self, delta_time: float):
        self.ball.update()
        self.bar.update()

        if random.randint(0, 10000) == random.randint(0, 10000):
            self.ball.bottom = -10

        if arcade.check_for_collision(self.ball, self.bar):
            self.ball.change_y = -self.ball.change_y
            self.ball.bottom = self.bar.top
            self.score += 1

        if self.ball.bottom < 0:
            self.ball.stop()
            self.bar.stop()
            self.ball.kill()
            self.bar.kill()
            self.game = "lose"

        if self.score == 20:
            self.game = "win"
            self.ball.stop()
            self.bar.stop()
            self.ball.kill()
            self.bar.kill()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.bar.change_x = -10
        if symbol == arcade.key.RIGHT:
            self.bar.change_x = 10

    def on_key_release(self, symbol: int, modifiers: int):

        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.bar.change_x = 0

        if self.game != "game" and symbol == arcade.key.SPACE:
            self.restart()

    def restart(self):
        self.ball = Ball()
        self.bar = Bar()
        self.score = 0
        self.game = "game"








window = Game(WINDOW_WIDTH, WINDOW_HEIGHT, "PingPong")






arcade.run()