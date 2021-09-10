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
# , add a function with instance variables for the animation
# , keyboard input: A, D + run animation
# , mirroring for moving left and right
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
    global vikings, amiri, current_action
    # noSmooth()
    imageMode(CENTER)
    colorMode(HSB, 360, 100, 100, 100)
    size(640, 320)
    viking_sheet = loadImage("viking.png")
    amiri = Viking(100, height-70, viking_sheet)
    vikings = []
    vikings.append(amiri)
    current_action = "idling" # what is the viking doing?
    for i in range(9):
        vikings.append(Viking(i*64, 0, viking_sheet))
    
    # without delays, the first frame will never show. Sad ; ;
    delay(500)


def draw():
    global vikings, amiri, current_action, current_action
    background(220, 79, 35)
    
    if current_action == "idling":
        amiri.animate_idle()
    
    if current_action == "running":
        amiri.animate_running()
    
    if current_action == "death":
        amiri.animate_death()
    
    if current_action == "jumping":
        amiri.animate_falling()
    
    amiri.show()
    if not amiri.on_ground:
        amiri.apply_force(PVector(0, 0.07)) # but only if you're in midair!
    amiri.edge_check_floor()
    amiri.update()
    
    # this stuff is for many vikings among Amiri, but we just have her.
    # for viking in vikings:
    #     # viking.animate_idle()
    #     # viking.animate_running()
    #     # viking.animate_falling()
    #     # viking.animate_attack()
    #     # viking.animate_block()
    #     # viking.animate_death()
    #     viking.show()
    #     # viking.apply_force(PVector(0, 0.1))
    #     viking.update()


# if we press A or D, we'll move in that direction! There are also a bundle
# of other hotkeys for different actions.
def keyPressed():
    global vikings, amiri, current_action
    
    if key == "a":
        amiri.apply_force(PVector(-0.1, 0)) # to give a sense of motion
        current_action = "running" # if we're animating something else, stop idling!
        amiri.mirrored = True

    if key == "d":
        amiri.apply_force(PVector(0.1, 0))
        current_action = "running"
        amiri.mirrored = False
    
    if key == "s":
        current_action = "death"
    
    if key == " ":
        amiri.apply_force(PVector(0, -2))
        amiri.pos.add(PVector(0, -1))
        current_action = "jumping"
    

# if we release any key, we'll stop animating and vikings will idle.
def keyReleased():
    global amiri, current_action
    if key == "a" or key == "d" or key == "s" or key == "e" or key == " ":
        current_action = "idling"
        amiri.vel = PVector(0, 0)
