from ursina import *
from playsound import playsound 

game = Ursina()

#playsound('GameTheme.m4a')

window.fullscreen = True
window.fps_counter.enabled = False

levelNumber = 1

wall = Entity(model = 'quad', 
	          color = color.green, 
	          scale_x = 0.5, 
	          scale_y = 4, 
	          position = (-5,0),
	          collider = 'box',
	          enabled = False)

leftPlayer = Entity(model = 'quad', 
					texture = 'RED', 
					scale_x = 1.2, 
					scale_y = 1.2, 
					position = (-3,0),
					collider = 'box')

rightPlayer = Entity(model = 'quad', 
					 texture = 'BLUE', 
					 scale_x = 1.2, 
					 scale_y = 1.2, 
					 position = (3,0),
					 collider = 'box')

mainWall = Entity(model = 'quad', 
			      color = color.green, 
			      scale_x = 0.5,
			      scale_y = 10,
			      collider = 'box')

redFlag = Entity(model = 'quad',
	             texture = 'RedFlag', 
	             position = (-6,3),
	             collider = 'box')

blueFlag = Entity(model = 'quad',
	              texture = 'BlueFlag',
	              position = (6,-3),
	              scale = 0.8,
	              collider = 'box')

upBound = Entity(model = 'quad', 
	             color = color.green, 
	             scale_x = 15, 
	             scale_y = 0.2, 
	             position = (0,4), 
	             collider = 'box')

downBound = duplicate(upBound, position = (0,-4))

leftBound = Entity(model = 'quad', 
	               color= color.green, 
	               scale_x = 0.2, 
	               scale_y = 10, 
	               position = (-7.3,0), 
	               collider = 'box')

rightBound = duplicate(leftBound, position = (7.3,0))

def update():
	global levelNumber
	global wall2

	#Left side
	if held_keys['w']:
		leftPlayer.y += 3 * time.dt
	if held_keys['s']:
		leftPlayer.y -= 3 * time.dt
	if held_keys['a']:
		leftPlayer.x -= 3 * time.dt
	if held_keys['d']:
		leftPlayer.x += 3 * time.dt

	#Right side
	if held_keys['w']:
		rightPlayer.y -= 3 * time.dt
	if held_keys['s']:
		rightPlayer.y += 3 * time.dt
	if held_keys['a']:
		rightPlayer.x += 3 * time.dt
	if held_keys['d']:
		rightPlayer.x -= 3 * time.dt

	#Collision
	if leftPlayer.intersects(mainWall).hit:
		leftPlayer.x -= 3 * time.dt

	if rightPlayer.intersects(mainWall).hit:
		rightPlayer.x += 3 * time.dt

	#Next level
	if leftPlayer.intersects(redFlag).hit and rightPlayer.intersects(blueFlag).hit:
		playsound('Win.wav')
		levelNumber += 1
		#print(levelNumber)
		leftPlayer.position = (-3,0)
		rightPlayer.position = (3,0)

	#upBound collision
	if leftPlayer.intersects(upBound).hit and held_keys['w']:
		leftPlayer.y -= 3 * time.dt
	if rightPlayer.intersects(upBound).hit and held_keys['s']:
		rightPlayer.y -= 3 * time.dt

	#downBound collision
	if leftPlayer.intersects(downBound).hit and held_keys['s']:
		leftPlayer.y += 3 * time.dt
	if rightPlayer.intersects(downBound).hit and held_keys['w']:
		rightPlayer.y += 3 * time.dt

	#leftBound collision
	if leftPlayer.intersects(leftBound).hit and held_keys['a']:
		leftPlayer.x += 3 * time.dt

	#rightBound collision
	if rightPlayer.intersects(rightBound).hit and held_keys['a']:
		rightPlayer.x -= 3 * time.dt

	#Level 2
	if levelNumber == 2:
		wall.enable()

		redFlag.position = (-4,-3)
		blueFlag.position = (6,3)

		if leftPlayer.intersects(wall).hit and held_keys['d']:
			leftPlayer.x -= 3 * time.dt
		if leftPlayer.intersects(wall).hit and held_keys['a']:
			leftPlayer.x += 3 * time.dt
		if leftPlayer.intersects(wall).hit and held_keys['w']:
			leftPlayer.y -= 3 * time.dt
		if leftPlayer.intersects(wall).hit and held_keys['s']:
			leftPlayer.y += 3 * time.dt

	#Level 3
	if levelNumber == 3:
		wall.position = (3,2)
		wall.scale_x = 4
		wall.scale_y = 0.5

		wall2 = duplicate(wall, position = (-4,-2), scale_x = 0.5, scale_y = 2)

		redFlag.position = (-5.5,3)
		blueFlag.position = (3,-3)

		if rightPlayer.intersects(wall).hit and held_keys['d']:
			rightPlayer.x += 3 * time.dt
		if rightPlayer.intersects(wall).hit and held_keys['a']:
			rightPlayer.x -= 3 * time.dt
		if rightPlayer.intersects(wall).hit and held_keys['w']:
			rightPlayer.y += 3 * time.dt
		if rightPlayer.intersects(wall).hit and held_keys['s']:
			rightPlayer.y -= 3 * time.dt 

		if leftPlayer.intersects(wall2).hit and held_keys['d']:
			leftPlayer.x -= 3 * time.dt
		if leftPlayer.intersects(wall2).hit and held_keys['a']:
			leftPlayer.x += 3 * time.dt
		if leftPlayer.intersects(wall2).hit and held_keys['w']:
			leftPlayer.y -= 3 * time.dt
		if leftPlayer.intersects(wall2).hit and held_keys['s']:
			leftPlayer.y += 3 * time.dt

	#Level 4
	if levelNumber == 4:
		wall2.disable()
		wall.position = (3,-2)
		wall.scale_x = 2
		wall.scale_y = 0.5

		if rightPlayer.intersects(wall).hit and held_keys['d']:
			rightPlayer.x += 3 * time.dt
		if rightPlayer.intersects(wall).hit and held_keys['a']:
			rightPlayer.x -= 3 * time.dt
		if rightPlayer.intersects(wall).hit and held_keys['w']:
			rightPlayer.y += 3 * time.dt
		if rightPlayer.intersects(wall).hit and held_keys['s']:
			rightPlayer.y -= 3 * time.dt

game.run() 