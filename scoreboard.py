from turtle import Turtle

FONT=('Bold Courier', 24, 'normal')
ALLINGMENT='Center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(x=0,y=250)
        self.color('white')
        self.score = 0
        with open('https://github.com/KalapalaGIT/Snake_game/blob/931661467be79c4135f7b21c22b470ff54ad5862/highscore.txt', 'r') as f:
            self.hightscore = int(f.read())

    def Update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}  Highscore: {self.hightscore}' , False, ALLINGMENT, FONT)

    def add_point(self):
        self.score +=1
        self.Update_scoreboard()

    def Reset(self):
        if self.score > self.hightscore:
            self.hightscore = self.score
            with open('Day20_Snake _game/Snake_game/highscore.txt', 'w') as f:
                f.write(str(self.hightscore))
        self.score = 0
        
