import pygame, sys


pygame.init()

HEIGHT = 500
WIDTH = 500

#screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Tic Tac Toe Game')

#load img
dir = r'C:\Users\ADMIN\Documents\python_tkinter\GAMEKHONGHAY\caro\img'
def load_scale_img(path_img, sizex, sizey):
    img = pygame.image.load(f'{dir}\{path_img}').convert_alpha()
    img_scale = pygame.transform.scale(img, (sizex, sizey))
    return img_scale

img_bg = load_scale_img('bg.png', 300, 300)
img_replay = load_scale_img('replay.png', 40, 40)

# font
font = pygame.font.Font(r'C:\Users\ADMIN\Documents\python_tkinter\GAMEKHONGHAY\caro\font\BLOCKSS.otf', 100)
font_result = pygame.font.Font(r'C:\Users\ADMIN\Documents\python_tkinter\GAMEKHONGHAY\caro\font\BLOCKSS.otf', 40)
font_score = pygame.font.Font(r'C:\Users\ADMIN\Documents\python_tkinter\GAMEKHONGHAY\caro\font\BLOCKSS.otf', 18)

#load sound
sound_click = pygame.mixer.Sound(r'C:\Users\ADMIN\Documents\python_tkinter\GAMEKHONGHAY\caro\sound\click_jump.wav')
sound_restart =  pygame.mixer.Sound(r'C:\Users\ADMIN\Documents\python_tkinter\GAMEKHONGHAY\caro\sound\chọn.wav')
sound_win = pygame.mixer.Sound(r'C:\Users\ADMIN\Documents\python_tkinter\GAMEKHONGHAY\caro\sound\win.wav')
sound_draw = pygame.mixer.Sound(r'C:\Users\ADMIN\Documents\python_tkinter\GAMEKHONGHAY\caro\sound\draw.wav')
'''
#1  #2  #3

#4  #5  #6

#7  #8  #9
'''
scorex, scoreo = 0, 0
text_o1, text_o2, text_o3, text_o4, text_o5, text_o6, text_o7, text_o8, text_o9,result_text = '', '', '', '', '', '', '', '', '', ''
class Object():
    def __init__(self, rgp): #object X or O
        self.rgp = rgp
    #vẽ 
    def Draw(self):
        object_render1 = font.render(f'{text_o1}', True, self.rgp)
        screen.blit(object_render1, (120, 50))
        object_render2 = font.render(f'{text_o2}', True, self.rgp)
        screen.blit(object_render2,(220, 50))
        object_render3 = font.render(f'{text_o3}', True, self.rgp)
        screen.blit(object_render3, (320, 50))
        object_render4 = font.render(f'{text_o4}', True, self.rgp)
        screen.blit(object_render4, (120, 155))
        object_render5 = font.render(f'{text_o5}', True, self.rgp)
        screen.blit(object_render5, (220, 155))  
        object_render6 = font.render(f'{text_o6}', True, self.rgp)
        screen.blit(object_render6,  (320, 155))
        object_render7 = font.render(f'{text_o7}', True, self.rgp)
        screen.blit(object_render7, (120, 255))
        object_render8 = font.render(f'{text_o8}', True, self.rgp)
        screen.blit(object_render8, (220, 255))
        object_render9 = font.render(f'{text_o9}', True, self.rgp)
        screen.blit(object_render9, (320, 255))
        # kết quả
        result = font_result.render(f'{result_text}', True, self.rgp)
        screen.blit(result, (220, 10))
        # score X
        scorex_ = font_score.render(f'Score x: {scorex}', True, self.rgp)
        screen.blit(scorex_, (10, 200))
        # score O
        scoreo_ = font_score.render(f'Score o: {scoreo}', True, self.rgp)
        screen.blit(scoreo_, (400, 200))

player = Object((105,105,105))
#variable
done, o1, o2, o3, o4, o5, o6, o7, o8 ,o9, turn = False, False, False, False, False, False, False, False, False, False, True
# turn true là x đi
# turn false là o đi

# kiểm soát người chơi nhấn 1 ô: nhấn 2 lần 1 ô thì sẽ không được
click1, click2, click3, click4, click5, click6, click7, click8, click9 = 0, 0, 0, 0, 0, 0, 0, 0, 0

#loop
while not done:
    screen.fill((192,192,192))
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            key = pygame.mouse.get_pos()
            # xử lí nhấp chuột các ô
            if 100 <= key[0] <= 200 and 45 <= key[1] <= 136:
                o1 = True
                pygame.mixer.Sound.play(sound_click)
                click1 += 1
                if click1 <=1 :
                    if turn == True:
                        text_o1 = 'x'
                        turn = False
                    elif turn == False:
                        text_o1 = 'o'
                        turn = True
            elif 200 <= key[0] <= 300 and 45 <= key[1] <= 136:
                o2 = True
                click2 += 1
                pygame.mixer.Sound.play(sound_click)
                if click2 <=1 :
                    if turn == True:
                        text_o2 = 'x'
                        turn = False
                    elif turn == False:
                        text_o2 = 'o'
                        turn = True
            elif 300 <= key[0] <= 400 and 45 <= key[1] <= 136:
                o3 = True
                click3 += 1
                pygame.mixer.Sound.play(sound_click)
                if click3 <=1 :
                    if turn == True:
                        text_o3 = 'x'
                        turn = False
                    elif turn == False:
                        text_o3 = 'o'
                        turn = True
            elif 100 <= key[0] <= 200 and 145 <= key[1] <= 240:
                o4 = True
                click4 += 1
                pygame.mixer.Sound.play(sound_click)
                if click4 <=1 :
                    if turn == True:
                        text_o4 = 'x'
                        turn = False
                    elif turn == False:
                        text_o4 = 'o'
                        turn = True
            elif 200 <= key[0] <= 300 and 145 <= key[1] <= 240:
                o5 = True
                click5 += 1
                pygame.mixer.Sound.play(sound_click)
                if click5 <=1 :
                    if turn == True:
                        text_o5 = 'x'
                        turn = False
                    elif turn == False:
                        text_o5 = 'o'
                        turn = True
            elif 300 <= key[0] <= 400 and 145 <= key[1] <= 240:
                o6 = True
                click6 += 1
                pygame.mixer.Sound.play(sound_click)
                if click6 <=1 :
                    if turn == True:
                        text_o6 = 'x'
                        turn = False
                    elif turn == False:
                        text_o6 = 'o'
                        turn = True
            elif 100 <= key[0] <= 200 and 245 <= key[1] <= 340:
                o7 = True
                click7 += 1
                pygame.mixer.Sound.play(sound_click)
                if click7 <=1 :
                    if turn == True:
                        text_o7 = 'x'
                        turn = False
                    elif turn == False:
                        text_o7 = 'o'
                        turn = True
            elif 200 <= key[0] <= 300 and 245 <= key[1] <= 340:
                o8 = True
                click8 += 1
                pygame.mixer.Sound.play(sound_click)
                if click8 <=1 :
                    if turn == True:
                        text_o8 = 'x'
                        turn = False
                    elif turn == False:
                        text_o8 = 'o'
                        turn = True
            elif 300 <= key[0] <= 400 and 245 <= key[1] <= 340:
                o9 = True
                click9 += 1
                pygame.mixer.Sound.play(sound_click)
                if click9 <= 1 :
                    if turn == True:
                        text_o9 = 'x'
                        turn = False
                    elif turn == False:
                        text_o9 = 'o'
                        turn = True
            # xử lí nhấp chuột restart
            elif 158 <= key[0] <= 185 and 354 <= key[1] <= 389:
                pygame.mixer.Sound.play(sound_restart)
                text_o1, text_o2, text_o3, text_o4, text_o5, text_o6, text_o7, text_o8, text_o9 = '', '', '', '', '', '', '', '', ''
                click1, click2, click3, click4, click5, click6, click7, click8, click9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
                o1, o2, o3, o4, o5, o6, o7, o8 ,o9 = False, False, False, False, False, False, False, False, False
                result_text = ''
            else:pass
        if event.type == pygame.MOUSEBUTTONUP:
            pass

    player.Draw()

    if (o1 and o2 and o3 and ((text_o1 == 'x' and text_o2 == 'x' and text_o3 == 'x') or (text_o1 == 'o' and text_o2 == 'o' and text_o3 == 'o'))) or (o1 and o4 and o7 and ((text_o1 == 'x' and text_o4 == 'x' and text_o7 == 'x') or (text_o1 == 'o' and text_o4 == 'o' and text_o7 == 'o'))) or (o1 and o5 and o9 and ((text_o1 == 'x' and text_o5 == 'x' and text_o9 == 'x') or (text_o1 == 'o' and text_o5 == 'o' and text_o9 == 'o'))) or (o3 and o6 and o9 and ((text_o3 == 'x' and text_o6 == 'x' and text_o9 == 'x') or (text_o3 == 'o' and text_o6 == 'o' and text_o9 == 'o'))) or (o7 and o8 and o9 and ((text_o7 == 'x' and text_o8 == 'x' and text_o9 == 'x') or (text_o7 == 'o' and text_o8 == 'o' and text_o9 == 'o'))) or (o2 and o5 and o8 and ((text_o2 == 'x' and text_o5 == 'x' and text_o8 == 'x') or (text_o2 == 'o' and text_o5 == 'o' and text_o8 == 'o'))) or (o4 and o5 and o6 and ((text_o4 == 'x' and text_o5 == 'x' and text_o6 == 'x') or (text_o4 == 'o' and text_o5 == 'o' and text_o6 == 'o'))) or (o7 and o5 and o3 and ((text_o7 == 'x' and text_o5 == 'x' and text_o3 == 'x') or (text_o7 == 'o' and text_o5 == 'o' and text_o3 == 'o'))):
        if (text_o1 == 'x' and text_o2 == 'x' and text_o3 == 'x') or (text_o1 == 'x' and text_o4 == 'x' and text_o7 == 'x') or (text_o1 == 'x' and text_o5 == 'x' and text_o9 == 'x') or (text_o3 == 'x' and text_o6 == 'x' and text_o9 == 'x') or (text_o7 == 'x' and text_o8 == 'x' and text_o9 == 'x') or (text_o2 == 'x' and text_o5 == 'x' and text_o8 == 'x') or (text_o4 == 'x' and text_o5 == 'x' and text_o6 == 'x') or (text_o7 == 'x' and text_o5 == 'x' and text_o3 == 'x'):
            if click1 <= 1 and click2 <=1 and click3 <=1 and click4 <=1 and click5 <=1 and click6 <=1 and click7 <=1 and click8 <=1 and click9 <=1:
                scorex += 1
                pygame.mixer.Sound.play(sound_win)
            result_text = 'x Win'
            #không bấm được khi win
            click1, click2, click3, click4, click5, click6, click7, click8, click9 = 2, 2, 2, 2, 2, 2, 2, 2, 2
        elif (text_o1 == 'o' and text_o2 == 'o' and text_o3 == 'o') or (text_o1 == 'o' and text_o4 == 'o' and text_o7 == 'o') or (text_o1 == 'o' and text_o5 == 'o' and text_o9 == 'o') or (text_o3 == 'o' and text_o6 == 'o' and text_o9 == 'o') or (text_o7 == 'o' and text_o8 == 'o' and text_o9 == 'o') or  (text_o2 == 'o' and text_o5 == 'o' and text_o8 == 'o') or (text_o4 == 'o' and text_o5 == 'o' and text_o6 == 'o') or (text_o7 == 'o' and text_o5 == 'o' and text_o3 == 'o'):
            if click1 <= 1 and click2 <=1 and click3 <=1 and click4 <=1 and click5 <=1 and click6 <=1 and click7 <=1 and click8 <=1 and click9 <=1:
                scoreo += 1
                pygame.mixer.Sound.play(sound_win)
            result_text = 'o Win'
            #không bấm được khi win
            click1, click2, click3, click4, click5, click6, click7, click8, click9 = 2, 2, 2, 2, 2, 2, 2, 2, 2
    elif o1 and o2 and o3 and o4 and o5 and o6 and o7 and o8 and o9:
        if click1 <= 1 and click2 <=1 and click3 <=1 and click4 <=1 and click5 <=1 and click6 <=1 and click7 <=1 and click8 <=1 and click9 <=1:
            pygame.mixer.Sound.play(sound_draw)
        result_text = 'Draw'
        click1, click2, click3, click4, click5, click6, click7, click8, click9 = 2, 2, 2, 2, 2, 2, 2, 2, 2
    screen.blit(img_replay, (150, 350))
    screen.blit(img_bg, (100, 40))
    
    pygame.display.update()
pygame.quit()
sys.exit()