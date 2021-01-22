import pygame
import random
import time
import math
import pyautogui
pygame.init()
pygame.mixer.init()
display=pygame.display.set_mode((700,700),pygame.NOFRAME)
pygame.display.set_caption("Pong Game")
running=True
# _____________
boll_speed=7
player_speed=15
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
bollX_V=boll_speed
bollY_V=boll_speed
# _____________
# _______________
player1_score=0
player2_score=0
play=False
# _______________
# pygame.mixer.music.load('1.mp3')
clock=pygame.time.Clock()
# _______________
def distains(x1,y1,x2,y2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist
# _____________________________________________________________________________________________
def player1(boll_position_x,boll_position_y,line_position_x,line_start_y,line_end_y,line_width):
    global bollX_V,player1_score,bollX,bollY_V

    if distains(boll_position_x,boll_position_y,line_position_x,boll_position_y)<=line_width and (boll_position_y>=line_start_y and boll_position_y<=line_end_y):
        # pygame.mixer.music.load('2.1.mp3')
        # pygame.mixer.music.play()
        bollY_V=random.randint(-10,10)
        bollX_V*=-1  
        bollX-=10
    return 0
# _____________________________________________________________________________________________
def player2(boll_position_x,boll_position_y,line_position_x,line_start_y,line_end_y,line_width):
    global bollX_V,bollX,bollY_V

    if distains(boll_position_x,boll_position_y,line_position_x,boll_position_y)<=line_width-5 and (boll_position_y>=line_start_y and boll_position_y<=line_end_y):
        # pygame.mixer.music.load('2.1.mp3')
        # pygame.mixer.music.play()
        bollY_V=random.randint(-10,10)
        bollX_V*=-1  
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
    while running:
        moues=pygame.mouse.get_pos()
        display.fill((0,0,0))
        if bollX>700-10:
            # pygame.mixer.music.load('1.mp3')
            # pygame.mixer.music.play()
            player2_score+=1
            reset()
            gameStart()
            # bollX*=-1
        if bollX<10:
            # pygame.mixer.music.load('1.mp3')
            # pygame.mixer.music.play()
            player1_score+=1
            reset()
            gameStart()

        if bollY>700-10:
            bollY_V*=-1
        if bollY<10:
            bollY_V*=-1

        if player1Y >600 or player1Y<0:
            player1Y_V=0

        if player2Y >600 or player2Y<0:
            player2Y_V=0

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False
                    quit()
        bollX+=bollX_V
        bollY+=bollY_V
        pygame.draw.rect(display, ((255,255,255)), (bollX,bollY,17,17), 0)
        pygame.draw.line(display, ((255,255,255)), (player2X,player2Y),(player2X,player2Y+100), 5)
        pygame.draw.line(display, ((255,255,255)), (350,0), (350,700),2)
        pygame.draw.line(display, ((255,255,255)), (player1X,player1Y),(player1X,player1Y+100),5)
        if bollX<350:
            if ((bollY-50)-player1Y)<=0:
                player1Y_V=-10
            if ((bollY-50)-player1Y)>=0:
                player1Y_V=10
            if ((bollY-50)-player1Y)==0:
                player1Y_V=0
            if ((bollY-50)-player1Y)==0:
                player1Y_V=0
        if bollX>=350:
            player1Y_V=0

        if bollX>350:
            if ((bollY-50)-player2Y)<=0:
                player2Y_V=-10
            if ((bollY-50)-player2Y)>=0:
                player2Y_V=10
            if ((bollY-50)-player2Y)==0:
                player2Y_V=0
            if ((bollY-50)-player2Y)==0:
                player2Y_V=0
        if bollX<=350:
            player2Y_V=0

        player1Y+=player1Y_V
        player2Y+=player2Y_V

        player1(bollX,bollY,player2X,player2Y,player2Y+100,19)
        player2(bollX,bollY,player1X,player1Y,player1Y+100,19)

        text_screen(f'{player2_score}',((255,255,255)),270,10)
        text_screen(f'{player1_score}',((255,255,255)),390,10)
        clock.tick(60)
        pygame.display.update()
# _____________________________________________________________________________________________
def gameOver(windata=0):
    running=True
    global score,player1_score,player2_score
    # pygame.mixer.music.load('1.mp3')
    # pygame.mixer.music.play()
    while running:
        display.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                quit()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RETURN:
                    # running=False 
                    player1_score=0
                    player2_score=0
                    reset()
                    gameStart()
                if event.key==pygame.K_ESCAPE:
                    running=False 
                    quit()
        if windata==2:
            text_screen("Gameover",(255,255,255),50,200)
            text_screen("PLayer2 win",(255,255,255),10,300)

            text_screen("Exit:Esc",((255,255,255)),0,10)
            text_screen('Play:Enter',((255,255,255)),400,10)

            text_screen(f'{player2_score}',((255,255,255)),165,400)
            text_screen(f'{player1_score}',((255,255,255)),515,300)

        elif windata==1:
            text_screen("Gameover",(255,255,255),410,200)
            text_screen("PLayer1 win",(255,255,255),365,300)

            text_screen("Exit:Esc",((255,255,255)),0,10)
            text_screen('Play:Enter',((255,255,255)),400,10)

            text_screen(f'{player2_score}',((255,255,255)),165,300)
            text_screen(f'{player1_score}',((255,255,255)),515,400)

        pygame.draw.rect(display, ((255,255,255)), (343,350,17,17), 0)
        pygame.draw.line(display, ((255,255,255)), (350,0), (350,310), width=2)
        pygame.draw.line(display, ((255,255,255)), (350,700), (350,400), width=2)
        clock.tick(10)
        pygame.display.update()
# _____________________________________________________________________________________________

def gameStart():
    global player1_score,player2_score,play
    if player1_score==10:
        gameOver(1)
    if player2_score==10:
        gameOver(2)
        
    running=True
    global score
    while running:
        display.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                quit()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RETURN:
                    play=True
                    gameloop()
                if event.key==pygame.K_ESCAPE:
                    running=False 
                    quit()
        if not play:
            text_screen("Exit:Esc",((255,255,255)),0,10)
            text_screen('Play:Enter',((255,255,255)),400,10)
            text_screen((f'Player2={player2_score}'),((255,255,255)),0,100)
            text_screen((f'Player1={player1_score}'),((255,255,255)),400,100)
        if play:
            text_screen(f'{player2_score}',((255,255,255)),270,10)
            text_screen(f'{player1_score}',((255,255,255)),390,10)
        pygame.draw.rect(display, ((255,255,255)), (bollX,bollY,17,17), 0)
        pygame.draw.line(display, ((255,255,255)), (350,0), (350,700),2)
        pygame.draw.line(display, ((255,255,255)), (player1X,player1Y),(player1X,player1Y+100),5)
        pygame.draw.line(display, ((255,255,255)), (player2X,player2Y),(player2X,player2Y+100),5)
        clock.tick(10)
        pygame.display.update()
        time.sleep(1)
        pyautogui.press('Enter')

# _____________________________________________________________________________________________
def reset():
    global player1X,player1Y,player1Y_V,player2X,player2Y,player2Y_V,bollX,bollY,bollX_V,bollY_V,player2_score,player1_score,play
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
    bollX_V=boll_speed
    bollY_V=boll_speed
    play=False

if __name__ == "__main__":
    gameStart()











