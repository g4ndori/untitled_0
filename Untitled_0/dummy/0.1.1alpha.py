#0.1.0beta shop price & attack speed modification

import pygame
import random

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()

size = [400, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("날아라 김 모 씨")
clock = pygame.time.Clock()

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
        title = large_font.render("게임 오버", True, (255, 0, 0))
        kills = font.render(f"적 처치 수: {kill_count}", True, (255, 255, 255))
        gold_text = font.render(f"획득 골드: {gold}G", True, (255, 255, 0))
        pygame.draw.rect(screen, (100, 100, 100), button_restart)
        pygame.draw.rect(screen, (100, 100, 100), button_exit)
        restart_text = font.render("다시 시작", True, (255, 255, 255))
        exit_text = font.render("게임 종료", True, (255, 255, 255))
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
    game_started = False
    running = True
    while not game_started and running:
        screen.fill((0, 0, 0))
        title = font.render("날아라 김 모 씨", True, (255, 255, 255))
        start_msg = font.render("ENTER를 눌러 게임 시작", True, (255, 255, 255))
        control_msg = font.render("← → : 이동 | S : 상점", True, (180, 180, 180))
        screen.blit(title, (100, 250))
        screen.blit(start_msg, (80, 300))
        screen.blit(control_msg, (80, 330))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_started = True
    if not running:
        pygame.quit()
        return

    while True:
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
                item1 = font.render("[1] 더블샷 (300G)", True, item_color(bomb_shot_count >= 2))
                item2 = font.render("[2] 트리플샷 (800G)", True, item_color(triple_shot))
                item3 = font.render("[3] 쿼드라샷 (1500G)", True, item_color(quadra_shot))
                item4 = font.render("[4] 펜타샷 (3000G)", True, item_color(penta_shot))
                item5 = font.render(f"[5] 보호막 (1000G) | {shield_count}개 작창", True, item_color(shield_count > 0))
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
                            gained_gold = random.randrange(1, 20) #골드!
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

            screen.fill((0, 0, 0))
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
            gold_text = font.render(f"G : {gold}G", True, (255, 255, 0))
            screen.blit(gold_text, (10, 10))
            kills_text = font.render(f"적 처치 수: {kill_count}", True, (255, 255, 255))
            screen.blit(kills_text, (10, 40))
            gotoshop_txt = font.render("S : 상점", True, (180, 180, 180))
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
                    break
                else:
                    pygame.quit()
                    exit()

if __name__ == "__main__":
    main()
