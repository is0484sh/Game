import pygame as pg
import os
import random
import time

pg.init()

Screen_width = 1080
Screen_height = 800

velocity = 2
mass = 2

i = 0

# 폰트 생성
font = pg.font.Font(None, 36)

# 캐릭터의 움직임
to_x = 0
to_y = 0

# os 쓰기위해 기본
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,r"C:\Users\PC_1M\Desktop\Pythonworkspace\game")


background = pg.image.load(os.path.join(image_path,"배경.png"))
screen = pg.display.set_mode((Screen_width,Screen_height))
pg.display.set_caption("총 게임")


# fps
clock = pg.time.Clock()

# 스테이터스 창
status = pg.image.load(os.path.join(image_path,"status.png"))
status_info = status.get_rect().size
status_width = status_info[0]
status_height = status_info[1]
status_x_pos = 0
status_y_pos = Screen_height - status_height


# 바닥 배경
ground = pg.image.load(os.path.join(image_path,"땅.png"))
ground_info = ground.get_rect().size
ground_width = ground_info[0]
ground_height = ground_info[1]
ground_x_pos = 0
ground_y_pos = Screen_height - ground_height-status_height

# 캐릭터 제작
character = pg.image.load(os.path.join(image_path,"캐릭터(좌).png"))
char_img = [pg.image.load(os.path.join(image_path,"캐릭터(좌).png")),
            pg.image.load(os.path.join(image_path,"캐릭터(우).png"))]
char_info = character.get_rect().size
char_width = char_info[0]
char_height = char_info[1]
char_x_pos = Screen_width/2 - (char_width/2)
char_y_pos = Screen_height - char_height -ground_height-status_height
char_attack = 100
char_hp = 100

# 캐릭터 정보
char_level = 1
char_exp = 0
char_needed_exp = 100

# 캐릭터 hp바
char_hp_bar_length = 350
char_hp_bar_height = 30
char_hp_bar_border_width = 2
char_hp_bar_border_color = ("orange") # white
char_hp_bar_color = (255, 0, 0) # red
char_hp_bar_pos_x = 150
char_hp_bar_pos_y = Screen_height - status_height/2

# exp 바
char_exp_bar_length = 350
char_exp_bar_height = 30
char_exp_bar_border_width = 2
char_exp_bar_border_color = ("orange") # white
char_exp_bar_color = ("yellow") # red
char_exp_bar_pos_x = char_hp_bar_pos_x*2 + char_exp_bar_length 
char_exp_bar_pos_y = Screen_height - status_height/2

# 무기
weapons = []
weapon = pg.image.load(os.path.join(image_path,"총알(좌).png"))
weapon_info = weapon.get_rect().size
weapon_width = weapon_info[0]
weapon_height = weapon_info[1]
weapon_x_pos = Screen_width/2 - (char_width/2)
weapon_y_pos = char_y_pos + 10

weapon_img = [pg.image.load(os.path.join(image_path,"총알(좌).png")),
              pg.image.load(os.path.join(image_path,"총알(우).png"))]

bullet_speed = 0.2

weapon_remove = -1
enemy_remove = -1
direction = "None"

# 점프
jump_speed = 0.5  # Adjust this value to change the jump speed
gravity = 0.03  # Adjust this value to change the gravity


# 적 캐릭터 제작
# 적 딕셔너리 제작을 해봅시다
boss= pg.image.load(os.path.join(image_path,"boss.png"))
boss_info = boss.get_rect().size
boss_width = boss_info[0]
boss_height = boss_info[1]

enemy= pg.image.load(os.path.join(image_path,"적.png"))
enemy_info = enemy.get_rect().size
enemy_width = enemy_info[0]
enemy_height = enemy_info[1]

enemies = []
for i in range(5):  # create 5 enemies
    enemy = {
        "name" : i,
        "enemy_pos_x": random.randrange(0, Screen_width - enemy_width),
        "enemy_pos_y": Screen_height - enemy_height - ground_height - status_height,
        "enemy_img_idx": 0,
        "enemy_current_hp": 100,
        "enemy_max_hp": 100,
        "enemy_hp_bar_length": 50,
        "enemy_hp_bar_height": 10,
        "enemy_hp_bar_border_width": 2,
        "enemy_hp_bar_border_color": "white",
        "enemy_hp_bar_color": "green",
        "enemy_attack": 1,
        "to_x": random.randint(-10, 10)
    }
    enemies.append(enemy)

enemy_images= [pg.image.load(os.path.join(image_path,"적.png")),
               pg.image.load(os.path.join(image_path,"boss.png"))
               ]

enemy_surface = pg.Surface((enemy_width, enemy_height), pg.SRCALPHA)

# 적의 hp 바
# Enemy's HP bar
for ind,val in enumerate(enemies):
    enemy_x_pos = val["enemy_pos_x"]
    enemy_y_pos = val["enemy_pos_y"]
    enemy_hp_bar_pos_x = val["enemy_pos_x"]
    enemy_hp_bar_pos_y = val["enemy_pos_y"] - val["enemy_hp_bar_height"] - 5
    enemy_hp = val["enemy_current_hp"]
    enemy_hp_bar_height = val["enemy_hp_bar_height"]

    boss_hp_bar_pos_x = Screen_width/2 - val["enemy_hp_bar_length"]/2
    boss_hp_bar_pos_y = val["enemy_hp_bar_height"] + 40
            

# 캐릭터의 속도
char_speed = 0.2

# 캐릭 정보 업데이트
def update_attack(level, attack):
    attack_increase = 2*level
    updated_attack = attack+attack_increase
    
    return updated_attack

def update_exp(level, exp):
    if level > 1:
        exp_increase = 50*level
    if level == 1:
        exp_increase = 0
    updated_exp = exp_increase + exp
    
    return updated_exp

# # 적 추가
# enemies.append([enemy_x_pos,enemy_y_pos,enemy_hp_bar_pos_x,enemy_hp_bar_pos_y,enemy_hp])

running = True

while running == True:


    fps = clock.tick(60)         

    # 적의 움직임


    # 점프


    to_y += gravity * fps

    if to_y >= 0 and char_y_pos >= Screen_height - char_height - ground_height-status_height:
        # End of the jump
        to_y = 0
        char_y_pos = Screen_height - char_height - ground_height-status_height


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            elif event.key == pg.K_LEFT:
                to_x -= char_speed
                direction = "left"
            elif event.key == pg.K_RIGHT:
                to_x += char_speed
                direction = "right"
            elif event.key == pg.K_x:
                if direction == "right":
                    bullet_speed = 0.5
                elif direction == "left":
                    bullet_speed = -0.5
                weapon_y_pos = char_y_pos
                weapon_x_pos = char_x_pos + (char_width/2) - (weapon_width/2)
                weapons.append([weapon_x_pos,weapon_y_pos,bullet_speed])
                pg.time.delay(10)
                print(weapons)
            elif event.key == pg.K_q:
                enemies.append({
                    "enemy_pos_x":random.randrange(0,Screen_width-enemy_width),
                    "enemy_pos_y":Screen_height - enemy_height - ground_height-status_height,
                    "enemy_img_idx":0,
                    "enemy_current_hp":100,
                    "enemy_max_hp":100,
                    "enemy_hp_bar_length": 50,
                    "enemy_hp_bar_height" : 10,
                    "enemy_hp_bar_border_width": 2,
                    "enemy_hp_bar_border_color" : ("white"),# white
                    "enemy_hp_bar_color" : ("green"), # red
                    "enemy_attack":1,
                    "to_x" : random.randint(-10,10)
                })
            #     # enemies.append([enemy_x_pos,enemy_y_pos,enemy_hp_bar_pos_x,enemy_hp_bar_pos_y,enemy_hp])
            elif event.key == pg.K_SPACE:
                if char_y_pos == Screen_height - char_height - ground_height-status_height:
                    to_y -= 0.03 * mass * velocity**2 * fps
                    
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                to_x = 0
            if event.key == pg.K_SPACE:
                to_y = 0
                    


    # 적 계속 움직이기

    # 끝에 닿으면 안가가게 하기

    if char_x_pos >= Screen_width - char_width:
        char_xpos = Screen_width - char_width
    elif char_x_pos <= 0:
        char_x_pos = 0

    weapons = [[w[0]+w[2] * fps,w[1],w[2]] for w in weapons]
    weapons = [[w[0],w[1],w[2]] for w in weapons if w[0]<=Screen_width and w[0]>=0]

    # 캐릭 움직임 업데이트

    char_rect = character.get_rect()
    char_rect.left = char_x_pos
    char_rect.top = char_y_pos


    # 적 캐릭터 움직임
    for enemy_idx, val in enumerate(enemies):
        enemy_x = val["enemy_pos_x"]
        enemy_y = val["enemy_pos_y"]
        enemy_health = val["enemy_current_hp"]
        enemy_max_health = val["enemy_max_hp"]
        enemy_img_idx = val["enemy_img_idx"]    
        enemy_attack = val["enemy_attack"]
        
        enemy_rect = enemy_images[enemy_img_idx].get_rect()
        enemy_rect.left = enemy_x
        enemy_rect.top = enemy_y

        if char_rect.colliderect(enemy_rect):
            char_hp -= enemy_attack
            print("남은 체력: ",char_hp)
            if char_hp <= 0:
                running = False

        for weapon_idx, val in enumerate(weapons):
            weapon_x = val[0]
            weapon_y = val[1]
            

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x
            weapon_rect.top = weapon_y


            if weapon_rect.colliderect(enemy_rect):
                weapon_remove = weapon_idx
                enemies[enemy_idx]["enemy_current_hp"] -= update_attack(char_level,char_attack)

                # print(enemy_name + "의 체력: ", enemies[enemy_idx]["enemy_current_hp"])
                if enemies[enemy_idx]["enemy_current_hp"] <= 0:
                    if enemy_img_idx == 0:
                        char_exp += 50
                    elif enemy_img_idx == 1:
                        char_exp += 1000000
                    enemy_remove = enemy_idx
                    # 초기화
                    # enemies.append([enemy_x_pos, enemy_y_pos, enemy_hp_bar_pos_x, enemy_hp_bar_pos_y, enemy_hp])
                    # print("적 인덱스: ", enemy_idx)
                    # 래밸업
                    if char_exp >= update_exp(char_level,char_needed_exp):
                        char_level += 1
                        char_exp = 0
                    print("캐릭터 레밸 :",char_level,"경험치 :",char_exp)


    if enemy_x_pos < 0:
        enemy_x_pos = 0
    elif enemy_x_pos > Screen_width-enemy_width:
        enemy_x_pos = Screen_width-enemy_width

    char_x_pos += to_x * fps
    char_y_pos += to_y * fps
    

    # 텍스트
    char_hp_text = font.render("HP : ", True, ("black"))
    char_level_text = font.render(str(char_level), True, ("black"))
    char_level_fixed_text = font.render("Lv. ", True, ("black"))
    notification = font.render("If you eliminate every enemies, the boss appears",True,"white")
    notification_to_summon = font.render("Press 'q' to summon enemies",True,"white")
            

    if weapon_remove > -1:
        del weapons[weapon_remove]
        weapon_remove = -1
    if enemy_remove > -1:
        del enemies[enemy_remove]
        enemy_remove = -1
    if enemies == []:
        enemies.append({
            "enemy_pos_x":random.randrange(0,Screen_width-boss_width),
            "enemy_pos_y":Screen_height- boss_height- ground_height-status_height + 50,
            "enemy_img_idx":1,
            "enemy_current_hp":1000,
            "enemy_max_hp":1000,
            "enemy_hp_bar_length": 300,
            "enemy_hp_bar_height" : 40,
            "enemy_hp_bar_border_width": 2,
            "enemy_hp_bar_border_color" : ("gold"),# white
            "enemy_hp_bar_color" : ("purple"), # red
            "enemy_attack":5,
            "to_x" : random.randint(-15,15)
        })

    screen.blit(background,(0,0))



    for x_pos, y_pos,bul_speed in weapons:
        if bul_speed < 0:            
            screen.blit(weapon_img[0],(x_pos,y_pos))
        if bul_speed > 0:            
            screen.blit(weapon_img[1],(x_pos,y_pos))
    if direction == "None":
        screen.blit(char_img[0],(char_x_pos,char_y_pos))    
    if direction == "left":      
        screen.blit(char_img[0],(char_x_pos,char_y_pos))
    elif direction == "right":
        screen.blit(char_img[1],(char_x_pos,char_y_pos))


    screen.blit(ground,(ground_x_pos,ground_y_pos))
    
    screen.blit(status,(status_x_pos,status_y_pos))

      
    
    # for enemy_x, enemy_y, hp_x, hp_y, hp in enemies:
        # do something with the enemy coordinates and health

    for idx, val in enumerate(enemies):
        enemy_x_pos = val["enemy_pos_x"] + random.randint(-10,10)
        enemy_y_pos = val["enemy_pos_y"]
        enemy_hp_bar_pos_x = enemy_x_pos
        enemy_hp_bar_pos_y = val["enemy_pos_y"] - val["enemy_hp_bar_height"] - 5
        enemy_hp = val["enemy_current_hp"]
        enemy_hp_bar_height = val["enemy_hp_bar_height"]
        enemy_hp_bar_length= val["enemy_hp_bar_length"]
        enemy_hp_bar_border_width = val["enemy_hp_bar_border_width"]
        enemy_hp_bar_border_color = val["enemy_hp_bar_border_color"]# white
        enemy_hp_bar_color = val["enemy_hp_bar_color"] # red
        enemy_attack = val["enemy_attack"]
        enemy_img_idx = val["enemy_img_idx"]
        enemy_health = val["enemy_current_hp"]
        enemy_max_health = val["enemy_max_hp"]
        enemy_hp_bar_bg = pg.Surface((enemy_hp_bar_length, enemy_hp_bar_height))
        enemy_hp_bar_bg.fill(enemy_hp_bar_border_color)
        enemy_hp_bar = pg.Surface((enemy_health/enemy_max_health * (enemy_hp_bar_length - enemy_hp_bar_border_width*2), enemy_hp_bar_height - enemy_hp_bar_border_width*2))
        enemy_hp_bar.fill(enemy_hp_bar_color)
        enemy_hp_bar_bg.blit(enemy_hp_bar, (enemy_hp_bar_border_width, enemy_hp_bar_border_width))
        screen.blit(enemy_images[enemy_img_idx],(enemy_x_pos,enemy_y_pos))
        if enemy_img_idx == 0:
            screen.blit(enemy_hp_bar_bg, (enemy_hp_bar_pos_x, enemy_hp_bar_pos_y))
        elif enemy_img_idx == 1:
            screen.blit(enemy_hp_bar_bg, (boss_hp_bar_pos_x, boss_hp_bar_pos_y))
        

    # hp 바

    char_hp_bar_bg = pg.Surface((char_hp_bar_length, char_hp_bar_height))
    char_hp_bar_bg.fill(char_hp_bar_border_color)
    char_hp_bar = pg.Surface((char_hp/100 * (char_hp_bar_length - char_hp_bar_border_width*2), char_hp_bar_height - char_hp_bar_border_width*2))
    char_hp_bar.fill(char_hp_bar_color)
    char_hp_bar_bg.blit(char_hp_bar, (char_hp_bar_border_width, char_hp_bar_border_width))
    screen.blit(char_hp_bar_bg, (char_hp_bar_pos_x, char_hp_bar_pos_y))
    screen.blit(char_hp_text,(char_hp_bar_pos_x, char_hp_bar_pos_y - 30))
    screen.blit(char_level_text,(char_hp_bar_pos_x+50, char_hp_bar_pos_y - 60))
    screen.blit(char_level_fixed_text,(char_hp_bar_pos_x, char_hp_bar_pos_y - 60))

    
    # exp 바 

    char_exp_bar_bg = pg.Surface((char_exp_bar_length, char_exp_bar_height))
    char_exp_bar_bg.fill(char_exp_bar_border_color)
    char_exp_bar = pg.Surface((char_exp/update_exp(char_level,char_needed_exp) * (char_exp_bar_length - char_exp_bar_border_width*2), char_exp_bar_height - char_exp_bar_border_width*2))
    char_exp_bar.fill(char_exp_bar_color)
    char_exp_bar_bg.blit(char_exp_bar, (char_exp_bar_border_width, char_exp_bar_border_width))
    screen.blit(char_exp_bar_bg, (char_exp_bar_pos_x, char_exp_bar_pos_y))
    
    enemy_surface.fill((0, 0, 0, 0))  # clear the surface

    # notifications
    screen.blit(notification,(0,0))
    screen.blit(notification_to_summon,(Screen_width-350,0))
    pg.display.update()

    clock.tick(60)
pg.quit()
