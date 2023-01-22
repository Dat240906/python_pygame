import pygame
pygame.init()

#biến chiều rộng và cao của màn hình
WIDTH = 600
HEIGHT = 300

#set FPS
clock = pygame.time.Clock()
FPS = 120

#set màn hình
screen = pygame.display.set_mode([WIDTH, HEIGHT])

#set tên 
name_windown = pygame.display.set_caption('T-rex Game')

# font, score game
font_score = pygame.font.Font(r'GAMEKHONGHAY\T - rex\font\font.ttf', 10)
font_gameover = pygame.font.Font(r'GAMEKHONGHAY\T - rex\font\font.ttf', 40)
score = 0
high_score = 0
score_plus = 1
    #update score bằng mili giây
timer_interval = 80 # 1 seconds
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, timer_interval)

    #hàm hiển thị score
def setScore():
    score_render = font_score.render(f'0{score}', True, (28, 28, 28))
    rect_score = score_render.get_rect(center = (WIDTH - 40, 20))
    screen.blit(score_render, rect_score)

     #hàm hiển thị high score

def setHighScore():
    high_score_render = font_score.render(f'HI 0{high_score}', True, (28, 28, 28))
    rect_high_score = high_score_render.get_rect(center = (WIDTH - 100, 20))
    screen.blit(high_score_render, rect_high_score)

    # hàm hiện thị màn hình game over
def setGameover():
    gameover_render = font_gameover.render('Game Over', True, (105, 105, 105))
    rect_gameover = gameover_render.get_rect(center = (300, 100))
    screen.blit(gameover_render, rect_gameover)

#load âm thanh (sound)
jump_sound = pygame.mixer.Sound('GAMEKHONGHAY\T - rex\sound\jump.wav')
get_point_sound = pygame.mixer.Sound('GAMEKHONGHAY\T - rex\sound\getpoint.wav')


#load ảnh 
dir_ = r'GAMEKHONGHAY/T - rex/img/'
def loadImg(nameImg):
    return pygame.image.load(dir_ + nameImg +'.png').convert_alpha()
img_bg = loadImg('bg')
img_ground = loadImg('ground')
img_dino = loadImg('dino')
img_ino_run1 = loadImg('dinorun1')
img_dino_run2= loadImg('dinorun2')
img_tree1 = loadImg('tree1')
img_replay = loadImg('replay')

#hàm vẽ chung
def draw(img, x, y):
    screen.blit(img, (x, y))

#dối tượng có hiệu ứng chuyển động
class object():
    def __init__(self, img, x, y, surface):
        self.surface = surface
        self.img = img
        self.img_ground_scale = pygame.transform.scale(self.img, (WIDTH,15))
        self.x = x
        self.y = y
        self.width = screen.get_width()
        self.speed = 3

    # vẽ đường    
    def drawGround(self):
        self.surface.blit(self.img_ground_scale, (self.x, self.y))
        self.surface.blit(self.img_ground_scale, (self.x + self.width, self.y))

    #di chuyển đường
    def move(self):
        self.x -= self.speed
        if self.x < -self.width:
            self.x += self.width
Ground = object(img_ground, 0, int(HEIGHT/1.2), screen)


# đối tượng dino
list_ani_dino = []
dir_dino = r'GAMEKHONGHAY\T - rex\img\dinorun'
def addIMGvaoList(list_img, dir_, max_index_img):
    for i in range(1, max_index_img + 1):
        img_get = pygame.image.load(dir_ + str(i) + '.png').convert_alpha()
        list_img.append(img_get)
addIMGvaoList(list_ani_dino, dir_dino, 2)


class player():
    def __init__(self, img, x, y, surface, list_ani):
        self.surface = surface
        self.i = 0
        self.img_noAnimation = img
        self.list = list_ani
        self.img = self.list[self.i]
        self.x = x
        self.y = y
        self.movement = 0
        self.movement_plus = 12
        self.jumping = False
        #biến check khi chưa thao tác
        self.sleep, self.jump = True, False
        # self.img_ani = list_ani[self.i]
        self.img_dino_scale = pygame.transform.scale(self.img, (40,40))
        self.rect_img = self.img.get_rect(topleft = (self.x, self.y))
        self.rect_img_noA = self.img_noAnimation.get_rect(topleft = (self.x, self.y))
        self.time_bandau = pygame.time.get_ticks()
        
    #vẽ 
    def draw(self):
        self.surface.blit(self.img, self.rect_img)

    #hoạt ảnh khủng long
    def animation(self):
        cooldown = 100
        self.time_sau = pygame.time.get_ticks()
        if self.time_sau - self.time_bandau > cooldown:
            self.i += 1
            if self.i >= len(self.list):
                self.i = 0
            self.img = self.list[self.i]
            self.time_bandau = self.time_sau

    #jump
    def Jump(self):
        self.rect_img.centery += self.movement
        if self.rect_img.centery >= HEIGHT - 70:
            self.rect_img.centery = HEIGHT - 70
            self.jumping = True
            self.sleep = True
        self.jump = True

Dino = player(img_dino, 90, int(HEIGHT/1.48), screen, list_ani_dino)

#biến chơi lại
replay_bySpace = False

#biến check để thoát của sổ
done = False
#trọng lực
p = 0.4

#tree
class Tree(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        #  DÙNG KHI CÓ NHIỀU VẬT THỂ TƯƠNG ĐỒNG
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 3
        self.image = img
        self.collide = False
        self.width_img = self.image.get_width()
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.left -= self.speed
        if self.rect.left < -self.width_img:
            self.rect.left += screen.get_width()

    #xử lí va chạm
    def check(self):
        vacham = pygame.Rect.colliderect(self.rect, Dino.rect_img)
        if vacham:
            self.collide = True
        return  self.collide
Tree_ = Tree(img_tree1, WIDTH, HEIGHT - 100)

#biến check khi đang chơi game
on = True

# main loop
while not done:
        #điểm cao nhất
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            done = True
        # update score bằng mili giây -. tăng lên 1 score
        elif event.type == timer_event:
            score += score_plus

        if event.type == pygame.KEYDOWN:
            #nếu đang nhảy sẽ không nhảy được nữa
            if Dino.jumping:
                if event.key == pygame.K_SPACE and Tree_.collide == False:
                    Dino.movement = 0
                    Dino.movement -= Dino.movement_plus
                    pygame.mixer.Sound.play(jump_sound)
                    Dino.sleep = False
                    Dino.jumping = False
            if event.key == pygame.K_SPACE and Tree_.collide == True:
                replay_bySpace = True
                Tree_.collide = False

                 # kiểm tra nhấp space và replay       
                Tree_ = Tree(img_tree1, WIDTH, HEIGHT - 100)
                Tree_.draw()
                Tree_.speed = 3
                Ground.speed = 3
                score = 0
                score_plus = 1
                Dino.movement_plus = 12

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pass
    # kiểm tra score để tăng tốc độ game
    if score == 100:
        pygame.mixer.Sound.play(get_point_sound)
        Tree_.speed = 4
        Ground.speed = 4
    elif score == 500:
        pygame.mixer.Sound.play(get_point_sound)
        Tree_.speed = 5
        Ground.speed = 5
    elif score == 1000:
        pygame.mixer.Sound.play(get_point_sound)
        Tree_.speed = 6
        Ground.speed = 6

    #set hoạt ảnh khi va chạm
    if Tree_.collide:
        Tree_.speed = 0
        Ground.speed = 0
        score_plus = 0
        Dino.movement_plus = 0
        
    #vẽ background
    draw(img_bg, 0, 0)

    #ảnh hưởng của trọng lực
    Dino.movement += p
    #vẽ, hoạt ảnh của đường đi
    Ground.drawGround()
    Ground.move()

    #vẽ cây
    Tree_.draw()
    Tree_.update()
    Tree_.check()

    #vẽ score
    setScore()

    # cập nhật high score
    if high_score < score: high_score = score
    setHighScore()


    # nếu có va chạm sẽ hiển thị gameover
    if Tree_.collide :   
        setGameover()
        draw(img_replay, 260, 140)
    #player
    Dino.draw()
    if Tree_.collide == False:
        Dino.animation()
    Dino.Jump()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()