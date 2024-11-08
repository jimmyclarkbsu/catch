import pygame, simpleGE, random

"""
Jimmy Clark
A slide and catch game
Slide and Catch Part 1
"""
class Meat(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("meat.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        #move to top of screen
        self.y = 10
        
        #x is random 0 - screen width
        self.x = random.randint(0, self.screenWidth)
        
        #dy is random minSpeed to maxSpeed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Wolf(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("howl.png")
        self.setSize(90, 90)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("spider.png")
        
        self.sndBite = simpleGE.Sound("bite.mp3")
        self.numMeats = 10
        self.wolf = Wolf(self)
        
        self.meats = []
        for i in range (self.numMeats):
            self.meats.append(Meat(self))
        self.sprites = [self.wolf,
                        self.meats]
        
    def process(self):
        for meat in self.meats:
            if meat.collidesWith(self.wolf):
                meat.reset()
                self.sndBite.play()
        
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
