# @author Winry
# @date 2021.09.07
# experimenting with sprites! from Hajileee's Fantasy Characters Pack
#     https://hajileee.itch.io/hajileees-fantasy-characters-pack
#     https://www.youtube.com/watch?v=xFEKIWpd0sU
#
# , version comments
# , shell with setup, background
# , create Viking class with particle code including apply_force
# , idle animation: loadImage, spritesheet.get
# , idle animation: Viking.index, .frames, %
# add a function with instance variables for the animation
# keyboard input: A, D + run animation
# mirroring for moving left and right
# methods to create the other 5 animations stored in Viking class
# looping vs not looping animations
# gravity and jumping
# ...
# double jump
# particle effects
# collision detection
# projectile weapon with emitter

from Viking import * # imports everything from a file/list

def setup():
    global vikings, amiri_the_viking
    # noSmooth()
    colorMode(HSB, 360, 100, 100, 100)
    size(640, 320)
    viking_sheet = loadImage("viking.png")
    amiri_the_viking = Viking(0, 0, viking_sheet)
    vikings = []
    vikings.append(amiri_the_viking)
    for i in range(9):
        vikings.append(Viking(i*64, 0, viking_sheet))


def draw():
    global vikings
    background(220, 79, 35)
    
    for viking in vikings:
        # viking.animate_idle()
        # viking.animate_running()
        # viking.animate_falling()
        viking.animate_attack()
        # viking.animate_block()
        # viking.animate_death()
        viking.show()
        # viking.apply_force(PVector(0, 0.1))
        viking.update()
