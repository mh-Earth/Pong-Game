import pygame
import random
import time
import math
pygame.init()
pygame.mixer.init()
display=pygame.display.set_mode((700,700))
pygame.display.set_caption("Pong Game")
running=True
# _____________
speed=7
score=0
# _____________
player1Y=300
player1X=50
player1Y_V=0
# _____________
player2Y=300
player2X=650
player2Y_V=0
# _____________
bollX=343
bollY=50
bollX_V=speed
bollY_V=speed
# _____________
# _______________
player1_score=0
player2_score=0
# _______________
pygame.mixer.music.load('1.mp3')
clock=pygame.time.Clock()
# _______________
def distains(x1,y1,x2,y2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist
# _____________________________________________________________________________________________
def player1(boll_position_x,boll_position_y,line_position_x,line_start_y,line_end_y,line_width):
    global bollX_V,player1_score,bollX

    if distains(boll_position_x,boll_position_y,line_position_x,boll_position_y)<=line_width and (boll_position_y>=line_start_y and boll_position_y<=line_end_y):
        bollX_V*=-1  
        bollX-=10
    return 0
# _____________________________________________________________________________________________
def player2(boll_position_x,boll_position_y,line_position_x,line_start_y,line_end_y,line_width):
    global bollX_V,bollX

    if distains(boll_position_x,boll_position_y,line_position_x,boll_position_y)<=line_width and (boll_position_y>=line_start_y and boll_position_y<=line_end_y):
        bollX_V*=-1  
        pygame.mixer.music.load('1.mp3')
        pygame.mixer.music.play()
        bollX+=10

    return 0
# _____________________________________________________________________________________________
font = pygame.font.Font('PressStart2P-Regular.ttf', 30)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    display.blit(screen_text, [x,y])
# _____________________________________________________________________________________________
def gameloop():
    global running,player1X,player1Y,player1Y_V,player2X,player2Y,player2Y_V,bollX,bollY,bollX_V,bollY_V,player2_score,player1_score
    # if player1_score or player2_score==10:
    #     gameOver()
    while running:
        # moues=pygame.mouse.get_pos()
        display.fill((0,0,0))
        if bollX>700-10:
            player2_score+=1
            reset()
            gameStart()
            # bollX_V*=-1

        if bollX<10:
            player1_score+=1
            reset()
            gameStart()
            bollX_V*=-1

        if bollY>700-10:
            bollY_V*=-1
        if bollY<10:
            bollY_V*=-1
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False
                    quit()
                elif event.key==pygame.K_w:
                    player1Y_V=-10
                elif event.key==pygame.K_s:
                    player1Y_V=10
                elif event.key==pygame.K_UP:
                    player2Y_V=-10
                elif event.key==pygame.K_DOWN:
                    player2Y_V=10
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_w:
                    player1Y_V=0
                elif event.key==pygame.K_s:
                    player1Y_V=0
                elif event.key==pygame.K_UP:
                    player2Y_V=0
                elif event.key==pygame.K_DOWN:
                    player2Y_V=0
        bollX+=bollX_V
        bollY+=bollY_V
        pygame.draw.rect(display, ((255,255,255)), (bollX,bollY,17,17), 0)
        # pygame.draw.circle(display, ((255,255,255)), (bollX,bollY), 10,0)
        pygame.draw.line(display, ((255,255,255)), (player1X,player1Y),(player1X,player1Y+100),5)
        pygame.draw.line(display, ((255,255,255)), (player2X,player2Y),(player2X,player2Y+100), 5)
        pygame.draw.line(display, ((255,255,255)), (350,0), (350,700),2)
        player1Y+=player1Y_V
        # player1Y=moues[1]
        # player2Y=moues[1]
        player2Y+=player2Y_V
        player1(bollX,bollY,player2X,player2Y,player2Y+100,19)
        player2(bollX,bollY,player1X,player1Y,player1Y+100,19)
        text_screen(f'{player2_score}',((255,255,255)),270,10)
        text_screen(f'{player1_score}',((255,255,255)),390,10)
        clock.tick(60)
        pygame.display.update()
# _____________________________________________________________________________________________
def gameOver():
    running=True
    global score
    # clock=pygame.time.Clock()
    while running:
        display.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                quit()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RETURN:
                    # running=False 
                    reset()
                    gameStart()
        text_screen("Gameover",(255,255,255),235,340)
        pygame.draw.line(display, ((255,255,255)), (350,0), (350,310), width=2)
        pygame.draw.line(display, ((255,255,255)), (350,700), (350,400), width=2)
        text_screen(f'{player2_score}',((255,255,255)),260,10)
        text_screen(f'{player1_score}',((255,255,255)),400,10)
        clock.tick(10)
        pygame.display.update()
# _____________________________________________________________________________________________

def gameStart():

    if player1_score==10:
        gameOver()
    if player2_score==10:
        gameOver()
        
    running=True
    global score
    # clock=pygame.time.Clock()
    while running:
        display.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                quit()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RETURN:
                    # running=False 
                    gameloop()
        text_screen(f'{player2_score}',((255,255,255)),270,10)
        text_screen(f'{player1_score}',((255,255,255)),390,10)
        pygame.draw.rect(display, ((255,255,255)), (bollX,bollY,17,17), 0)
        pygame.draw.line(display, ((255,255,255)), (350,0), (350,700),2)
        # pygame.draw.circle(display, ((255,255,255)), (bollX,bollY), 10,0)
        pygame.draw.line(display, ((255,255,255)), (player1X,player1Y),(player1X,player1Y+100),5)
        pygame.draw.line(display, ((255,255,255)), (player2X,player2Y),(player2X,player2Y+100), 5)
        clock.tick(10)
        pygame.display.update()

# _____________________________________________________________________________________________
def reset():
    global player1X,player1Y,player1Y_V,player2X,player2Y,player2Y_V,bollX,bollY,bollX_V,bollY_V,player2_score,player1_score
    # _____________
    player1Y=300
    player1X=50
    player1Y_V=0
    # _____________
    player2Y=300
    player2X=650
    player2Y_V=0
    # _____________
    bollX=343
    bollY=50
    bollX_V=speed
    bollY_V=speed
    # player1_score=0
    # player2_score=0

if __name__ == "__main__":
    gameStart()











