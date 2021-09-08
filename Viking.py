# Basically has a sprite, only it's a viking with particle code.


class Viking:
    def __init__(self, x, y, sheet):
        self.pos = PVector(x, y)
        self.vel = PVector().random2D() # same as PVector(0, 0) or PVector(0, 0, 0)
        self.acc = PVector()
        self.sheet = sheet # a sheet of the class's animation.
    
    
    # applies a force to a particle using Newton's Second Law of Physics
    def apply_force(self, force):
        # F = ma, so a = F/m. However, m = 1, so a = F.
        self.acc.add(force)
    
    
    # updates the particle so that it can move
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        self.acc.mult(0) # same as resetting it to PVector()
    
    
    # shows a Viking. Can be animated, mirrored, or rotated.
    def show(self):
        sprite_frame = self.sheet.get(0, 0, 32, 32)
        sprite_frame.resize(64, 64)
        image(sprite_frame, self.pos.x, self.pos.y)
