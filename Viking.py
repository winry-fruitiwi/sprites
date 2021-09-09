# Basically has a sprite, only it's a viking with particle code.


class Viking:
    def __init__(self, x, y, sheet):
        self.pos = PVector(x, y)
        self.vel = PVector() # same as PVector(0, 0) or PVector(0, 0, 0)
        self.acc = PVector()
        self.sheet = sheet # a sheet of the class's animation.
        self.index = 0
        # keeps track of what part of the sheet I want to animate
        self.y_pos = 0
    
    
    # applies a force to a particle using Newton's Second Law of Physics
    def apply_force(self, force):
        # F = ma, so a = F/m. However, m = 1, so a = F.
        self.acc.add(force)
    
    
    # updates the particle so that it can move
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        self.acc.mult(0) # same as resetting it to PVector()
    
    
    # animates the Viking so that it appears to be idling.
    def animate_idle(self):
        self.index = frameCount//10 % 7
        self.y_pos = 0
    
    
    # animates the Viking so that it appears to be running.
    def animate_running(self):
        self.index = frameCount//8 % 5
        self.y_pos = 1
    
    
    # animates the Viking so that it appears to be in midair, much like it should be here.
    def animate_falling(self):
        self.index = frameCount//12 % 4
        self.y_pos = 2
    
    
    # animates the Viking so that it appears to be swinging and jabbing its sword.
    def animate_attack(self):
        self.index = frameCount//8 % 9
        self.y_pos = 3
    
    
    # animates the Viking so that it appears to be jabbing its weapon and blocking an attack.
    def animate_block(self):
        self.index = frameCount//10 % 9
        self.y_pos = 4
    
    
    # animates the Viking so that it appears to have taken a fatal blow.
    def animate_death(self):
        self.index = frameCount//15 % 9
        self.y_pos = 5
    
    
    # shows a Viking. Can be animated, mirrored, or rotated.
    def show(self):
        sprite_frame = self.sheet.get(32 * self.index, self.y_pos * 32, 32, 32)
        sprite_frame.resize(96, 96)
        image(sprite_frame, self.pos.x, self.pos.y)
