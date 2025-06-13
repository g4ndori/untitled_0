#UI Updating-2_25/06/11

import pygame
import random
import math

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()

size = [400, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Untitled_0")
clock = pygame.time.Clock()
bg_img = pygame.image.load("background_img.png").convert()
bg_img = pygame.transform.scale(bg_img, (size[0], size[1]))
bg_img_y = 0

class objc:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    def put_img(self, cd1):
        if cd1[-3:] == "png":
            self.img = pygame.image.load(cd1).convert_alpha()
        else:
            self.img = pygame.image.load(cd1)
        self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))

def crash(a, b):
    rect_a = pygame.Rect(a.x, a.y, a.sx, a.sy)
    rect_b = pygame.Rect(b.x, b.y, b.sx, b.sy)
    return rect_a.colliderect(rect_b)

font = pygame.font.SysFont("malgungothic", 15)
large_font = pygame.font.SysFont("malgungothic", 30)

def draw_health_bar(value, max_value, x, y, width, height):
    ratio = max(value / max_value, 0)
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.draw.rect(screen, (0, 255, 0), (x, y, width * ratio, height))

def game_over_screen(kill_count, gold):
    button_restart = pygame.Rect(100, 400, 200, 50)
    button_exit = pygame.Rect(100, 470, 200, 50)
    while True:
        screen.fill((30, 30, 30))
        title = large_font.render("Game Over!", True, (255, 0, 0))
        kills = font.render(f"Kills: {kill_count}", True, (255, 255, 255))
        gold_text = font.render(f"Gold: {gold}G", True, (255, 255, 0))
        pygame.draw.rect(screen, (100, 100, 100), button_restart)
        pygame.draw.rect(screen, (100, 100, 100), button_exit)
        restart_text = font.render("Restart", True, (255, 255, 255))
        exit_text = font.render("Exit", True, (255, 255, 255))
        screen.blit(title, (130, 200))
        screen.blit(kills, (130, 250))
        screen.blit(gold_text, (130, 280))
        screen.blit(restart_text, (160, 415))
        screen.blit(exit_text, (160, 485))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_restart.collidepoint(event.pos):
                    return True
                elif button_exit.collidepoint(event.pos):
                    pygame.quit()
                    exit()
def main():
    cndrur_img = pygame.image.load("ufo_shit1.png").convert_alpha()
    cndrur_img = pygame.transform.scale(cndrur_img, (400, 300))

    
    game_started = False
    running = True

    #나 소개
    screen.fill((0, 0, 0))
    loading_font = pygame.font.SysFont("malgungothic", 20, True)
    loading_text = loading_font.render("Made by g4ndori", True, (255, 255, 255))
    text_surface = loading_text.convert_alpha()

    #페이드인
    for alpha in range(0, 256, 5):
        screen.fill((0, 0, 0))
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, (size[0] // 2 - text_surface.get_width() // 2,
                                size[1] // 2 - text_surface.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(20)
    pygame.time.delay(1000)

    #페이드아웃
    for alpha in range(255, -1, -5):
        screen.fill((0, 0, 0))
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, (size[0] // 2 - text_surface.get_width() // 2,
                                size[1] // 2 - text_surface.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(20)

    screen.fill((0, 0, 0))
    loading_font = pygame.font.SysFont("malgungothic", 10)
    loading_text = loading_font.render("Loading...", True, (255, 255, 255))
    screen.blit(loading_text, (size[0] // 2 - loading_text.get_width() // 2,
                               size[1] // 2 - loading_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(2000)


    while not game_started and running:
        #배경
        screen.blit(bg_img, (0, bg_img_y - bg_img.get_height()))
        screen.blit(bg_img, (0, bg_img_y))

        time_ms = pygame.time.get_ticks()
        angle = (time_ms / 50) % 360
        rotated_img = pygame.transform.rotozoom(cndrur_img, angle, 1.0)
        center_y = 400 + math.sin(time_ms / 200) * 2
        rotated_rect = rotated_img.get_rect(center=(size[0] // 2, center_y))

        screen.blit(rotated_img, rotated_rect)

        back_title_font = pygame.font.SysFont("malgungothic", 32, True)
        title_font = pygame.font.SysFont("malgungothic", 30, True)
        #control_msg_font = start_text_font = setting_text_font = pygame.font.SysFont("magungothic", 20, True)
        title = title_font.render("Untitled_0", True, (255, 255, 255))
        back_title = back_title_font.render("Untitled_0", True, (255, 255, 0))
        #control_msg = control_msg_font.render("← → : 이동 | S : 상점", True, (180, 180, 180))

        screen.blit(back_title, (115, 248))
        screen.blit(title, (120, 250))
    
        button_setting = pygame.Rect(125, 370, 130, 50)
        pygame.draw.rect(screen, (0, 0, 0), button_setting)
        setting_text_font = pygame.font.SysFont("malgungothic", 20, True)
        setting_text = setting_text_font.render("Setting", True, (255, 255, 255))
        screen.blit(setting_text, (button_setting.x + 30, button_setting.y + 15))

        button_start = pygame.Rect(125, 310, 130, 50)
        pygame.draw.rect(screen, (0, 0, 0), button_start)
        start_text_font = pygame.font.SysFont("malgungothic", 20, True)
        start_text = start_text_font.render("Start", True, (255, 255, 255))
        screen.blit(start_text, (button_start.x + 30, button_start.y + 15))
        

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_setting.collidepoint(event.pos):
                    screen.fill((0, 0, 0))
                    setting_font = pygame.font.SysFont("malgungothic", 15)
                    setting_text1 = setting_font.render("Left Key / Right Key : Move", True, (255, 255, 255))
                    setting_text2 = setting_font.render("S Key : Open/Close Shop", True, (255, 255, 255))
                    screen.blit(setting_text1, (100, 100))
                    screen.blit(setting_text2, (100, 140))
                    pygame.display.update()
                    pygame.time.delay(3000)
                elif button_start.collidepoint(event.pos):

                    screen.fill((0, 0, 0))
                    loading_font = pygame.font.SysFont("malgungothic", 10)
                    loading_text = loading_font.render("Loading...", True, (255, 255, 255))
                    screen.blit(loading_text, (size[0] // 2 - loading_text.get_width() // 2,
                                            size[1] // 2 - loading_text.get_height() // 2))
                    pygame.display.update()
                    pygame.time.delay(800)

                    screen.fill((0, 0, 0))
                    loading_font = pygame.font.SysFont("malgungothic", 10)
                    loading_text = loading_font.render("Checking...", True, (255, 255, 255))
                    screen.blit(loading_text, (size[0] // 2 - loading_text.get_width() // 2,
                                            size[1] // 2 - loading_text.get_height() // 2))
                    pygame.display.update()
                    pygame.time.delay(400)

                    screen.fill((0, 0, 0))
                    loading_font = pygame.font.SysFont("malgungothic", 10)
                    loading_text = loading_font.render("Done!", True, (255, 255, 255))
                    screen.blit(loading_text, (size[0] // 2 - loading_text.get_width() // 2,
                                            size[1] // 2 - loading_text.get_height() // 2))
                    pygame.display.update()
                    pygame.time.delay(1200)

                    """screen.fill((0, 0, 0))
                    loading_font = pygame.font.SysFont("malgungothic", 30, True)
                    loading_text = loading_font.render("Start in 3..", True, (255, 255, 255))
                    screen.blit(loading_text, (size[0] // 2 - loading_text.get_width() // 2,
                                            size[1] // 2 - loading_text.get_height() // 2))
                    pygame.display.update()
                    pygame.time.delay(1000)

                    screen.fill((0, 0, 0))
                    loading_font = pygame.font.SysFont("malgungothic", 30, True)
                    loading_text = loading_font.render("Start in 2..", True, (255, 255, 255))
                    screen.blit(loading_text, (size[0] // 2 - loading_text.get_width() // 2,
                                            size[1] // 2 - loading_text.get_height() // 2))
                    pygame.display.update()
                    pygame.time.delay(1000)

                    screen.fill((0, 0, 0))
                    loading_font = pygame.font.SysFont("malgungothic", 30, True)
                    loading_text = loading_font.render("Start in 1..", True, (255, 255, 255))
                    screen.blit(loading_text, (size[0] // 2 - loading_text.get_width() // 2,
                                            size[1] // 2 - loading_text.get_height() // 2))
                    pygame.display.update()
                    pygame.time.delay(1000)"""
                    game_started = True


    if not running:
        pygame.quit()
        return

    while True:
        background = objc()
        background.put_img("background_img.png")
        background.change_size(400, 700)

        ufo = objc()
        ufo.put_img("ufo_shit1.png")
        ufo.change_size(60, 90)
        ufo.x = round(size[0] / 2 - ufo.sx / 2)
        ufo.y = size[1] - ufo.sy - 50
        ufo.move = 4
        ufo.hp = 5
        ufo.max_hp = 5

        bomb_img = pygame.image.load("bombb.png").convert_alpha()
        bomb_img = pygame.transform.scale(bomb_img, (5, 15))
        bomb_size = bomb_img.get_size()


        enm_img = pygame.image.load("enm.png").convert_alpha()
        enm_img = pygame.transform.scale(enm_img, (40, 40))
        enm_size = enm_img.get_size()

        shield_img = pygame.image.load("shield1.png").convert_alpha()
        shield_img = pygame.transform.scale(shield_img, (ufo.sx + 10, ufo.sy + 10))

        leftMov = rightMov = shott = False
        bombList = []
        enList = []
        damage_texts = []
        shot_cooldown = 250
        speed_upagrade = 150
        min_shot_cooldown = 50

        last_shot_time = 0
        bomb_shot_count = 1
        shield_count = 0
        speed_upagrade = False
        triple_shot = quadra_shot = penta_shot = False
        gold = 0
        shop_open = False
        kill_count = 0
        start_ticks = pygame.time.get_ticks()
        hit_flash_time = 0
        hit_flash_duration = 300
        shield_flash_time = 0
        shield_flash_duration = 300

        MainEv = 0
        while MainEv == 0:
            clock.tick(60)

            current_time = pygame.time.get_ticks()
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        leftMov = True
                    elif event.key == pygame.K_RIGHT:
                        rightMov = True
                    #elif event.key == pygame.K_SPACE:
                        #shott = True
                    elif event.key == pygame.K_s:
                        shop_open = not shop_open
                    elif shop_open:
                        if event.key == pygame.K_1 and gold >= 300 and bomb_shot_count < 2:
                            bomb_shot_count = 2
                            triple_shot = quadra_shot = penta_shot = False
                            gold -= 300
                        elif event.key == pygame.K_5 and gold >= 1000 and shield_count < 10:
                            shield_count += 1
                            gold -= 1000
                        elif event.key == pygame.K_2 and gold >= 800 and not triple_shot:
                            bomb_shot_count = 3
                            triple_shot = True
                            quadra_shot = penta_shot = False
                            gold -= 800
                        elif event.key == pygame.K_3 and gold >= 1500 and not quadra_shot:
                            bomb_shot_count = 4
                            triple_shot = quadra_shot = True
                            penta_shot = False
                            gold -= 1500
                        elif event.key == pygame.K_4 and gold >= 3000 and not penta_shot:
                            bomb_shot_count = 5
                            triple_shot = quadra_shot = penta_shot = True
                            gold -= 3000
                        elif event.key == pygame.K_6 and gold >= 2000 and not speed_upagrade:
                            if speed_upagrade > min_shot_cooldown:
                                speed_upagrade -= 20
                                if speed_upagrade < min_shot_cooldown:
                                    speed_upagrade = min_shot_cooldown
                                gold -= 2000
                                speed_upagrade = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftMov = False
                    elif event.key == pygame.K_RIGHT:
                        rightMov = False
                    #elif event.key == pygame.K_SPACE:
                        #shott = False

            if shop_open:
                screen.fill((30, 30, 30))
                shop_title = font.render("상점 (S로 닫기)", True, (255, 255, 255))
                def item_color(purchased):
                    return (144, 238, 144) if purchased else (255, 255, 255)
                item1 = font.render("[1] DUBLE SHOT (300G)", True, item_color(bomb_shot_count >= 2))
                item2 = font.render("[2] TRIPLE SHOT (800G)", True, item_color(triple_shot))
                item3 = font.render("[3] QUADRA SHOT (1500G)", True, item_color(quadra_shot))
                item4 = font.render("[4] PENTA SHOT (3000G)", True, item_color(penta_shot))
                item5 = font.render(f"[5] SHIELD (1000G) | {shield_count}", True, item_color(shield_count > 0))
                item6 = font.render("[6] - UNNAMED_0 -", True, item_color(speed_upagrade)) #shot_cooldown = 100
                player_gold = font.render(f"현재 G: {gold}", True, (255, 255, 0))
                screen.blit(shop_title, (100, 100))
                screen.blit(item1, (100, 130))
                screen.blit(item2, (100, 160))
                screen.blit(item3, (100, 190))
                screen.blit(item4, (100, 220))
                screen.blit(item5, (100, 250))
                screen.blit(item6, (100, 280))
                screen.blit(player_gold, (100, 310))
                pygame.display.update()
                continue

            if leftMov:
                ufo.x = max(0, ufo.x - ufo.move)
            if rightMov:
                ufo.x = min(size[0] - ufo.sx, ufo.x + ufo.move)
            if current_time - last_shot_time > shot_cooldown:
            #if shott and current_time - last_shot_time > shot_cooldown:
                for i in range(bomb_shot_count):
                    bm = objc()
                    bm.img = bomb_img
                    bm.sx, bm.sy = bomb_size
                    offset = (i - (bomb_shot_count - 1) / 2) * (bm.sx + 2)
                    bm.x = round(ufo.x + ufo.sx / 2 - bm.sx / 2 + offset)
                    bm.y = ufo.y - bm.sy - 10
                    bm.move = 20
                    bombList.append(bm)
                last_shot_time = current_time

            for bomb in bombList[:]:
                bomb.y -= bomb.move
                if bomb.y < -bomb.sy:
                    bombList.remove(bomb)

            elapsed_seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            enemy_spawn_chance = min(0.005 + elapsed_seconds * 0.002, 0.05)
            if random.random() < enemy_spawn_chance:
                en = objc()
                en.img = enm_img
                en.sx, en.sy = enm_size
                en.x = random.randrange(0, size[0] - en.sx)
                en.y = 10
                en.move = 1.5
                en.hp = 10
                en.max_hp = 10
                enList.append(en)

            for enm in enList[:]:
                enm.y += enm.move
                if enm.y > size[1]:
                    enList.remove(enm)

            dbombList = []
            denmList = []
            for i in range(len(bombList)):
                for j in range(len(enList)):
                    bomb = bombList[i]
                    enm = enList[j]
                    if crash(bomb, enm):
                        enm.hp -= 2
                        dbombList.append(i)
                        if enm.hp <= 0:
                            denmList.append(j)
                            gained_gold = 9999999999#random.randrange(1, 30) #골드!
                            gold += gained_gold
                            kill_count += 1
                            damage_texts.append((enm.x, enm.y, pygame.time.get_ticks(), gained_gold))

            for i in sorted(set(dbombList), reverse=True):
                if i < len(bombList): del bombList[i]
            for j in sorted(set(denmList), reverse=True):
                if j < len(enList): del enList[j]

            for enm in enList[:]:
                if crash(ufo, enm):
                    if shield_count > 0:
                        shield_count -= 1
                        enList.remove(enm)
                        shield_flash_time = pygame.time.get_ticks()
                        break
                    else:
                        ufo.hp -= 1
                        enList.remove(enm)
                        hit_flash_time = pygame.time.get_ticks()
                        if ufo.hp <= 0:
                            MainEv = 1
                        break

            background.show()

            ufo.show()
            if shield_count > 0:
                screen.blit(shield_img, (ufo.x - 5, ufo.y - 5))
                shield_text = font.render(f"{shield_count}", True, (0, 255, 255))
                screen.blit(shield_text, (ufo.x + ufo.sx - 10, ufo.y - 10))
            for bomb in bombList:
                bomb.show()
            for enm in enList:
                enm.show()
                draw_health_bar(enm.hp, enm.max_hp, enm.x, enm.y + enm.sy + 2, enm.sx, 5)
            draw_health_bar(ufo.hp, ufo.max_hp, ufo.x, ufo.y + ufo.sy + 5, ufo.sx, 7)
            gold_text = font.render(f"Gold : {gold}G", True, (255, 255, 0))
            screen.blit(gold_text, (10, 10))
            kills_text = font.render(f"Kills: {kill_count}", True, (255, 255, 255))
            screen.blit(kills_text, (10, 40))
            gotoshop_txt = font.render("S : Shop", True, (180, 180, 180))
            screen.blit(gotoshop_txt, (10, 70))
            for entry in damage_texts[:]:
                x, y, start_time, dmg = entry
                now = pygame.time.get_ticks()
                if now - start_time > 1000:
                    damage_texts.remove(entry)
                    continue
                alpha = 255 - int(255 * (now - start_time) / 1000)
                dmg_text = font.render(f"+{dmg}G", True, (255, 255, 0))
                dmg_text.set_alpha(alpha)
                screen.blit(dmg_text, (x, y))

            now = pygame.time.get_ticks() #적과 충돌
            if now - hit_flash_time < hit_flash_duration:
                alpha = int(255 * (1 - (now - hit_flash_time) / hit_flash_duration))
                red_overlay = pygame.Surface(size)
                red_overlay.fill((255, 0, 0))
                red_overlay.set_alpha(alpha)
                screen.blit(red_overlay, (0, 0))

            if now - shield_flash_time < shield_flash_duration: #보호막 깨짐
                alpha = int(255 * (1 - (now - shield_flash_time) / shield_flash_duration))
                blue_overlay = pygame.Surface(size)
                blue_overlay.fill((0, 255, 255))
                blue_overlay.set_alpha(alpha)
                screen.blit(blue_overlay, (0, 0))

            pygame.display.update()
            if MainEv == 1:
                restart = game_over_screen(kill_count, gold)
                if restart:
                    main()
                    return
                else:
                    pygame.quit()
                    exit()

if __name__ == "__main__":
    main()
