###################################################
################# Name : Houman Ebrahimi
################# Due Date: 2020/06/23
################# Description : tetris (neon edition)
###################################################

#########
#########
#########
from tetris_class import *
from random import randint
from random import choice
from time import perf_counter
import pygame

pygame.init()

HEIGHT = 600
WIDTH  = 800
GRIDSIZE = HEIGHT//24
screen=pygame.display.set_mode((WIDTH,HEIGHT))
GREY = (192,192,192)
score=0
level=1
mult=0


intro=pygame.image.load('intro.jpg')
intro=intro.convert_alpha()
intro_resize=pygame.transform.scale(intro,(WIDTH,HEIGHT))

background=pygame.image.load('background.jpg')
background=background.convert_alpha()
background_resize=pygame.transform.scale(background,(WIDTH,HEIGHT))

inst_back=pygame.image.load('instruction_window.jpg')
inst_back=inst_back.convert_alpha()
inst_backR=pygame.transform.scale(inst_back,(WIDTH,HEIGHT))

arrows=pygame.image.load('arrow_keys.jpg')
arrows=arrows.convert_alpha()
arrows_resize=pygame.transform.scale(arrows,(150,80))

space_B=pygame.image.load('space_button.png')
space_B=space_B.convert_alpha()

endScreen=pygame.image.load('endScreen.jpg')
endScreen=endScreen.convert_alpha()
endScreen_resize=pygame.transform.scale(endScreen,(WIDTH,HEIGHT))

background2=pygame.image.load('background2.jpg')
background2=background2.convert_alpha()
background2_resize=pygame.transform.scale(background2,(WIDTH,HEIGHT))

font=pygame.font.SysFont(('Snap ITC'),20)
font2=pygame.font.SysFont(('Snap ITC'),15)
font3=pygame.font.SysFont(('Snap ITC'),100)
font4=pygame.font.SysFont(('Courier New CB'),20)

music_Button=pygame.image.load('musicButton.png')
music_Button=music_Button.convert_alpha()
music_Button_resize=pygame.transform.scale(music_Button,(50,50))

pauseWin=pygame.image.load('pauseWin.jpg')
pauseWin=pauseWin.convert_alpha()
pauseWin_screen=pygame.transform.scale(pauseWin,(WIDTH,HEIGHT))

tetris_logo=pygame.image.load('logo.jpg')
tetris_logo=tetris_logo.convert_alpha()
tetris_logo_resize=pygame.transform.scale(tetris_logo,(70,70))


playX=50
playY=520
playW=100
playH=30

instX=300
instY=520
instW=160
instH=30

play_button=pygame.image.load('button1.jpg')
play_button=play_button.convert_alpha()
play_button_resize=pygame.transform.scale(play_button,(playW,playH))

button6=pygame.image.load('button6.jpg')
button6=button6.convert_alpha()
button6_resize=pygame.transform.scale(button6,(playW,playH))

inst_button_resize=pygame.transform.scale(play_button,(instW,instH))

button3=pygame.image.load('button3.jpg')
button3=button3.convert_alpha()
button3_resize=pygame.transform.scale(button3,(playW,playH))

button4=pygame.image.load('button4.jpg')
button4=button4.convert_alpha()
button4_resize=pygame.transform.scale(button4,(playW,playH))

button2=pygame.image.load('button2.jpg')
button2=button2.convert_alpha()
button2_resize=pygame.transform.scale(button2,(playW,playH))

button5=pygame.image.load('button5.jpg')
button5=button5.convert_alpha()
button5_resize=pygame.transform.scale(button5,(playW,playH))

neonBorder=pygame.image.load('neonBorder.jpg')
neonBorder=neonBorder.convert_alpha()
resize_neonBorder=pygame.transform.scale(neonBorder,(200,HEIGHT))

border=pygame.image.load('border.png')
border=border.convert_alpha()
border_resize=pygame.transform.scale(border,(200,HEIGHT))

pauseWin=pygame.image.load('pauseWin.jpg')
pauseWin=pauseWin.convert_alpha()
pauseWin_resize=pygame.transform.scale(pauseWin,(WIDTH,HEIGHT))


special_block=pygame.image.load('block.jpg')
special_block=special_block.convert_alpha()
special_block_resize=pygame.transform.scale(special_block,(400,GRIDSIZE))

land=pygame.mixer.Sound('land.wav')
land.set_volume(0.6)

rotate_sound=pygame.mixer.Sound('block-rotate.wav')
rotate_sound.set_volume(0.6)

mouseClick=pygame.mixer.Sound('mouseClick.aif')
mouseClick.set_volume(0.8)


clear_line=pygame.mixer.Sound('clearline.wav')
clear_line.set_volume(0.6)

space_hit=pygame.mixer.Sound('force-hit.wav')
space_hit.set_volume(0.6)

lose_effect=pygame.mixer.Sound('lose.wav')
lose_effect.set_volume(0.6)

illustrater=pygame.transform.scale(background,(150,200))
illustrater2=pygame.transform.scale(background2,(150,200))

selectMapWall=pygame.image.load('selectmapWall.jpg')
selectMapWall=selectMapWall.convert_alpha()
selectMapWall_resize=pygame.transform.scale(selectMapWall,(WIDTH,HEIGHT))

songs=['Theme.mp3','Theme2.mp3','pauseMusic.mp3','Theme3.mp3']
next_song=choice(songs)
pygame.mixer.music.load(next_song)
pygame.mixer.music.play()

tetris=False
back=[background,background2]
scored=False
#---------------------------------------#
COLUMNS = 14                            #
ROWS = 22                               # 
LEFT = 9                                # 
RIGHT = LEFT + COLUMNS                  # 
MIDDLE = LEFT + COLUMNS//2               #
TOP = 1                                 #
FLOOR = TOP + ROWS                     #
#---------------------------------------#
timer=100

def intro_window():
    screen.blit(intro_resize,(0,0))
    screen.blit(play_button_resize,(playX,playY))
    screen.blit(inst_button_resize,(instX+20,instY))
    screen.blit(music_Button_resize,(670,510))
    screen.blit(tetris_logo_resize,(360,340))
    graphics=font.render('Play',1,WHITE)
    graphics2=font2.render('Instructions',1,WHITE)
    tetris_words=font3.render('Tetris',1,WHITE)
    screen.blit(graphics2,(instX+45,instY+5))
    screen.blit(graphics,(playX+20,playY))
    screen.blit(tetris_words,(220,200))
    pygame.display.update()
def instructions():
    screen.blit(inst_backR,(0,0))
    greet=font2.render('Welcome',1,WHITE)
    screen.blit(greet,(WIDTH//2-50,30))
    screen.blit(arrows_resize,(100,100))
    arrow_instructions=font4.render('move left/right and up/down',1,WHITE)
    screen.blit(arrow_instructions,(300,100))
    screen.blit(space_B,(100,300))
    space_ins=font4.render('force hit',1,WHITE)
    screen.blit(space_ins,(650,300))
    screen.blit(button6_resize,(WIDTH//2-50,550))
    play=font4.render('Map',1,WHITE)
    screen.blit(play,(WIDTH//2-15,560))
    level1=font4.render('Level1',1,WHITE)
    screen.blit(level1,(70,450))
    level2=font4.render('Level2',1,WHITE)
    screen.blit(level2,(400,450))
    level3=font4.render('Level3',1,WHITE)
    screen.blit(level3,(700,450))
    slow=font4.render('Slow',1,WHITE)
    medium=font4.render('Medium',1,WHITE)
    fast=font4.render('Fast',1,WHITE)
    screen.blit(slow,(70,500))
    screen.blit(medium,(400,500))
    screen.blit(fast,(710,500))
    pygame.display.update()
    
def pauseGame():
    screen.blit(pauseWin_resize,(0,0))
    pause=font.render('Welcome to pause screen',1,WHITE)
    screen.blit(pause,(WIDTH//2-150,50))
    play=font.render('Play',1,WHITE)
    screen.blit(button5_resize,(650,550))
    screen.blit(play,(660,550))
    pygame.display.update()
    
def choose_map():
    screen.blit(selectMapWall_resize,(0,0))
    map_selector=font.render('select your map',1,WHITE)
    screen.blit(map_selector,(WIDTH//2-70,30))
    map1=font4.render('neon',1,WHITE)
    map2=font4.render('galaxy',1,WHITE)
    screen.blit(illustrater,(170,100))
    screen.blit(illustrater2,(500,100))
    screen.blit(button4_resize,(190,400))
    screen.blit(button2_resize,(530,400))
    screen.blit(map2,(550,410))
    screen.blit(map1,(210,410))
    pygame.display.update()
#---------------------------------------#
#   functions                           #
#---------------------------------------#
def redraw_screen():
    score_print=font.render('Score : '+str(score),1,WHITE)
    screen.blit(back,(0,0))
    screen.blit(resize_neonBorder,(600,0))
    screen.blit(score_print,(630,70))
    time=font.render('Time : '+str(timeInGame),1,WHITE)
    state_level=font.render('Level : '+str(level),1,WHITE)
    screen.blit(state_level,(630,200))
    screen.blit(border_resize,(0,0))
    screen.blit(time,(40,300))
    screen.blit(button3_resize,(640,450))
    pause_button=font.render('Pause',1,WHITE)
    screen.blit(pause_button,(655,450))
    shape.draw(screen, GRIDSIZE)
    nextShadow.draw(screen,GRIDSIZE)
    floor.draw(screen, GRIDSIZE)
    leftWall.draw(screen, GRIDSIZE)
    rightWall.draw(screen, GRIDSIZE)
    nextShape.draw(screen,GRIDSIZE)
#####################################################################################################
# 11.  Draw the object obstacles on the screen
#####################################################################################################
    obstacles.draw(screen,GRIDSIZE)
    shadow.draw(screen,GRIDSIZE)
    ceiling.draw(screen,GRIDSIZE)
    add=200
    for i in range(200,600,GRIDSIZE):
        pygame.draw.rect(screen,WHITE,(add,1,GRIDSIZE,GRIDSIZE),0)
        add+=GRIDSIZE
        screen.blit(special_block_resize,(200,1))
    pygame.display.update() 

def draw_grid():
    """ Draw horisontal and vertical lines on the entire game window.
        Space between the lines is GRIDSIZE.
    """
    add1=25
    add2=200
    for i in range(225,800,GRIDSIZE):
        pygame.draw.line(screen,WHITE,(225,add1),(WIDTH-225,add1),1)
        add1+=GRIDSIZE

    for i in range(200,600,GRIDSIZE):
        pygame.draw.line(screen,WHITE,(add2,28),(add2,HEIGHT-27),1)
        add2+=GRIDSIZE
    pygame.display.update()

def endGame():
    screen.blit(endScreen_resize,(0,0))
    game_over=font3.render('Game Over',1,WHITE)
    level_indicator=font4.render('Level ' +str( level),1,WHITE)
    screen.blit(game_over,(WIDTH//2-300,50))
    score_indicator=font4.render('Your score was '+ str(score),1,WHITE)
    screen.blit(score_indicator,(WIDTH//2-50,550))
    screen.blit(button2_resize,(600,550))
    quit_word=font4.render('Exit ',1,WHITE)
    exit_game=font4.render('Play Again',1,WHITE)
    screen.blit(level_indicator,(WIDTH//2-40,570))
    screen.blit(quit_word,(620,560))
    screen.blit(button2_resize,(100,550))
    screen.blit(exit_game,(120,560))
    pygame.display.update()

            
    
#---------------------------------------#
#   main program                        #
#---------------------------------------#    
shapeNo = randint(1,7)
shape = Shape(MIDDLE,TOP,shapeNo)
floor = Floor(LEFT,FLOOR,COLUMNS)
leftWall = Wall(LEFT-1, TOP, ROWS)
nextShape=Shape(LEFT-6,TOP+2,shapeNo)
rightWall = Wall(RIGHT, TOP, ROWS)
obstacles=Obstacles(LEFT,FLOOR)
shadow=Shadow(MIDDLE,TOP,shapeNo)
nextShadow=Shadow(LEFT-6,TOP+20,shapeNo)
ceiling=Floor(LEFT,TOP,COLUMNS)
#####################################################################################################
# 10.  Create an object obstacles of Obstacles class. Give it two parameters only - LEFT & FLOOR
#####################################################################################################
intro=True
inPlay = False
pause=False
inst=False
map_selector_window=False
instruction_check=False
end_screen=False
while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:         
            intro = False
        (x,y)=pygame.mouse.get_pos()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if x>playX and x<playX+playW and y>playY and y<playY+playH:
                mouseClick.play()
                intro=False
                map_selector_window=True
            if x>670 and x<670+50 and y>510 and y<510+50 :
                pygame.mixer.music.pause()
                mouseClick.play()

            if x>300 and x<300+instW and y>520 and y<520+instH:
                mouseClick.play()
                instruction_check=True
                intro=False
                print('hello')
    intro_window()

while instruction_check:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:         
                intruction_check = False
            (x,y)=pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if x>385 and x<385+playW and y>560 and y<560+playH:
                    mouseClick.play()
                    map_selector_window=True
                    instruction_check=False
        instructions()

while map_selector_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:         
            map_selector_window = False
        (x,y)=pygame.mouse.get_pos()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if x>190 and x<190+playW and y>400 and y<400+playH:
                mouseClick.play()
                back=background_resize
                map_selector_window=False
                inPlay=True
            elif x>530 and x<530+playW and y>400 and y<400+playH:
                mouseClick.play()
                back=background2_resize
                map_selector_window=False
                inPlay=True
            
    choose_map()
while inPlay==True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:         
            inPlay = False
        (cursorX,cursorY)=pygame.mouse.get_pos()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if cursorX>640 and cursorX<640+playW and cursorY>450 and cursorY<450+playH:
                mouseClick.play()
                inPlay=False
                pause=True
                while pause:
                    for event in pygame.event.get():
                        (x,y)=pygame.mouse.get_pos()
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            if x>650 and x<650+playW and y>550 and y<550+playH:
                                mouseClick.play()
                                inPlay=True
                                pause=False
                                print(pause,inPlay)
                    pauseGame()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotate_sound.play()
                shape.rotateClkwise()
                shadow.rotateClkwise()
#####################################################################################################
# 8.  Modify the code so it uses rotate_cntclkwise() method when collision is detected during rotation
#####################################################################################################
            if event.key == pygame.K_LEFT:
                shape.move_left()
                shadow.move_left()
                if shape.collides(leftWall) :
                    shape.move_right()
                    shadow.move_right()
                    #shape.rotateCntclkwise()
                    #shadow.rotateCntclkwise()
                        
            if event.key == pygame.K_RIGHT:
                shape.move_right()
                shadow.move_right()
                if shape.collides(rightWall):
                    shape.move_left()
                    shadow.move_left()
                    #shape.rotateCntclkwise()
                    #shadow.rotateCntclkwise()
                    
                

            if event.key == pygame.K_SPACE:          
                while not (shape.collides(floor) or shape.collides(obstacles)):
                    shape.move_down()
                if shape.collides(floor) or shape.collides(obstacles):
                    space_hit.play()
                    shape.move_up()
                    obstacles.append(shape)
                    shapeNo=randint(1,7)
                    shape=Shape(MIDDLE,TOP,shapeNo)
                    nextShape=Shape(LEFT-6,TOP+2,shapeNo)
                    shadow=Shadow(MIDDLE,TOP,shapeNo)
                    nextShadow=Shadow(LEFT-6,TOP+20,shapeNo)
                    #obstacles.show()   # printing the blocks is done to visualize the process remove it afterwards
                    fullRows = obstacles.findFullRows(TOP, FLOOR, COLUMNS) # finds the full rows and removes their blocks from the obstacles
                    obstacles.removeFullRows(fullRows)
                    #print ("full rows: ",fullRows)
                    if len(fullRows)>=1 and len(fullRows)<=3 :
                        clear_line.play()
                        tetris=False
                        score+=len(fullRows)*100
                        obstacles.removeFullRows(fullRows)

                    elif len(fullRows)==4 and tetris==True:
                        clear_line.play()
                        tetris=False
                        score+=len(fullRows)*300
                        obstacles.removeFullRows(fullRows)
                        
                    elif len(fullRows)==4 and tetris==False:
                        clear_line.play()
                        tetris=True
                        score+=len(fullRows)*200
                        obstacles.removeFullRows(fullRows)
                    #print ("full rows: ",fullRows)    # printing the full rows is done to visualize the process remove it afterwards
                    
    timeInGame=round(pygame.time.get_ticks()/1000,1)
    
    while not(shadow.collides(floor) or shadow.collides(obstacles)):
        shadow.move_down()
    if shadow.collides(floor) or shadow.collides(obstacles):
        shadow.move_up()
        
    shape.move_down() 
    if shape.collides(obstacles) or shape.collides(floor):
        land.play()
        shape.move_up()
        obstacles.append(shape)
        #obstacles.show()   # printing the blocks is done to visualize the process remove it afterwards
        fullRows = obstacles.findFullRows(TOP, FLOOR, COLUMNS) # finds the full rows and removes their blocks from the obstacles
        #print ("full rows: ",fullRows)    # printing the full rows is done to visualize the process remove it afterwards
        if len(fullRows)>=1 and len(fullRows)<=3 :
            clear_line.play()
            tetris=False
            score+=len(fullRows)*100
            obstacles.removeFullRows(fullRows)

        elif len(fullRows)==4 and tetris==True:
            clear_line.play()
            tetris=False
            score+=len(fullRows)*300
            obstacles.removeFullRows(fullRows)

        elif len(fullRows)==4 and tetris==False:
            clear_line.play()
            tetris=True
            score+=len(fullRows)*200
            obstacles.removeFullRows(fullRows)

            
        print ("full rows: ",fullRows)    # printing the full rows is done to visualize the process remove it afterwards
        #obstacles.removeFullRows(fullRows)
        shapeNo=randint(1,7)
        while timer!=0 and inPlay:
            timer-=1
            #print(timer)
        if timer==0:
            timer=100
            shape=Shape(MIDDLE,TOP,shapeNo)
            nextShape=Shape(LEFT-6,TOP+2,shapeNo)
            shadow=Shadow(MIDDLE,TOP,shapeNo)
            nextShadow=Shadow(LEFT-6,TOP+20,shapeNo)
    redraw_screen()
    draw_grid()
    if score>500 and score<2000:
        pygame.time.delay(65)
        level=2
    elif score>=2000:
        pygame.time.delay(45)
        level=3
    else:
        pygame.time.delay(80)
    if obstacles.collides(ceiling):
        lose_effect.play()
        inPlay=False
        end_screen=True
    
        while end_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_screen=False
                (x,y)=pygame.mouse.get_pos()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if x>600 and x<600+playW and y>550 and y<550+playH:
                        mouseClick.play()
                        end_screen=False
                    if x>100 and x<100+playW and y>550 and y<550+playH:
                        mouseClick.play()
                        inPlay=True
                        end_screen=False

            endGame()
        
pygame.quit()
       
