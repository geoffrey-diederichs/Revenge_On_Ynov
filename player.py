class Player:
    def __init__(self, x: int, y:int, char: int = 1):
        self.position_x = x
        self.position_y = y
        self.width = 16
        self.height = 24
        self.imgSrc = 'img/player.png'
        self.frameX = 64
        self.frameY = 24*2
        self.frameRate = 0
        self.framesX = 8-1
        self.framesY = 2
        #1=robot, 2=girl, 3=boi
        self.char = 1
        self.sprint = 0
        self.totalFrames = 60

    def animate(self, pressed: bool):
        if self.sprint == 0:
            self.totalFrames = 60
        elif self.sprint != 0:
            self.totalFrames = 30
            if self.frameRate > 30:
                self.frameRate = 0

        if pressed:
            if self.frameRate == self.totalFrames:
                self.frameRate = 0
                if self.frameY >= self.height*self.framesY:
                    self.frameY = 24
                else:
                    self.frameY += self.height*2
            else:
                self.frameRate += 1
        else:
            self.frameY = 24*2
