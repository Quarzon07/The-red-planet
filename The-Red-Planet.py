from ursina import *
from time import sleep


app = Ursina()

speed = 2.5

def update():
    
    hit_info = player.intersects()
    
    if held_keys['w']:
        player.y += speed * time.dt
        player.texture = "sprite1runB.png"
     
    if held_keys['s']:
        player.y -= speed * time.dt
        player.texture = "sprite1runF.png"
    
    if held_keys['d']:
        player.x += speed * time.dt
        player.texture = "sprite1runR.png"
        
    
    if held_keys['a']:
        player.x -= speed * time.dt
        player.texture = "sprite1runL.png"
     
     
     if hit_info.hit:
         speed -= speed
         sleep(0.1)
         speed += speed
    
    if held_keys['escape']:
        quit()
    


player = Entity(model = "quad", texture = "sprite1still.png", position = (0, 0, 0), scale = 2, collider = "box")

tree = Entity(model = "quad", texture = "Tree.png", position = (4.3, 0, -1), scale = 5.3, collider = "box")

level1map = Entity(model = "quad", texture = "map1st.png", position = (0, 2, 1), scale = 16)


app.run()