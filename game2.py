from random import randint
import pgzrun

WIDTH = 1000
HEIGHT = 500

class player(Actor):
    speed = 5
    p.pos = (WIDTH/2 , HEIGHT/2)
    def movement(self):
        if keyboard.left:
            self.x -= self.speed
            
        if keyboard.right:
            self.x += self.speed
        
        if keyboard.up:
            self.y -= self.speed
        
        if keyboard.down:
            self.y += self.speed
        
        if keyboard.space:
            self.angle += self.speed
        

class Enemy(Actor):
    speed = 2
    e.pos = (-100 , HEIGHT/2)
    def tracking(self , p):
        if p.x > self.x:
            self.x += self.speed
        if p.x < self.x:
            self.x -= self.speed
        if p.y > self.y:
            self.y += self.speed
        if p.y < self.y:
            self.y -= self.speed
        print(f'player {p.pos} enemy {self.pos}')
        if self.colliderect(p):
            exit()

class Fruit(Actor):
    
    x = randint(50 , WIDTH-50)
    Y = randint(50 , HEIGHT-50)

    def relocate(self):
        self.x = randint(50 , WIDTH - 50)
        self.y = randint(50 , HEIGHT - 50)


p = Player
