import pygame
import sys
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
import menu_functions as mf
from pygame.sprite import Group
from scoreboard import Scoreboard
from button import Button
from screens import Info_Screen
from screens2 import Info_Screen2
import game_functions as gf
from powers import Powers


def run_game():
    pygame.init()
    pygame.mixer.init()
    bs=pygame.mixer.Sound('data/laser.wav')
    ad=pygame.mixer.Sound('data/al.ogg')
    dead=pygame.mixer.Sound('data/dead.wav')
    theme=pygame.mixer.Sound('data/background.wav')
    click=pygame.mixer.Sound('data/click.ogg')
    go=pygame.mixer.Sound('data/Game_over.ogg')
    power=pygame.mixer.Sound('data/power.wav')
    power.set_volume(0.8)
    theme.set_volume(0.1)
    theme.play(-1)
    go.set_volume(2)
    bs.set_volume(0.6)
    ad.set_volume(0.2)
    dead.set_volume(0.5)
    ai_s = Settings()
    black=(0,0,0)
    blue1=(30,230,230)
    blue2=(47,150,150)

    screen = pygame.display.set_mode((ai_s.scr_w,ai_s.scr_h))
    background= pygame.image.load('data/background.png')

    pygame.display.set_caption("Alien Invasion")
    icon = pygame.image.load('data/spaceship.png')
    pygame.display.set_icon(icon)

    #Button(ai_s,screen,msg,width,height,x,y,rect_color,text_color,font_size)

    play = Button(ai_s,screen,'Play',200,40,0,-50,blue1,black,48)

    infos = Button(ai_s,screen,'Info',200,40,0,50,blue1,black,48)

    back = Button(ai_s,screen,'<',40,40,600,-330,blue1,black,48)

    buttons = [play,infos,back]

    down = Button(ai_s,screen, 'Bonus',200,40,300,300,blue1,black,40)

    title = Button(ai_s,screen,'ALIEN INVASION',0,0,0,-(ai_s.scr_h/2)+150,0,blue1,120)

    game_o = Button(ai_s,screen,'Game Over',0,0,0,0,0,blue1,120)
    
    
    

    info = Info_Screen(screen)
    info2=Info_Screen2(screen)
    stats=GameStats(ai_s)
    sb=Scoreboard(ai_s,screen,stats)
    ship=Ship(ai_s,screen)
    alien=Alien(ai_s,screen)
    bullets=Group()
    aliens=Group()
    gf.create_fleet(ai_s,screen,ship,aliens)
    po= Powers(screen)
    a_bullets = Group()
    
    while True:
        pygame.time.delay(15)
        screen.blit(background, (0,0))
        if not stats.game_active:
            mf.check_events(stats,buttons,info,click,down,info2)

            mf.update_screen(ai_s,screen,buttons,info,title,down,info2)
        if stats.game_active:
            if sb.power_status:
                sb.count_down(power)
                
            gf.check_events(ship)
            gf.fire_bullet(ai_s,screen,ship,bullets,bs,sb)
            gf.alien_bullet(ai_s,screen,aliens,a_bullets,sb,stats)
            gf.update_a_bullets(ai_s,stats,screen,sb,ship,aliens,bullets,dead,go,game_o,power,a_bullets)
            
            ship.update()
            
            gf.update_bullets(ai_s,screen,stats,sb,ship,aliens,bullets,ad,po)
            gf.update_aliens(ai_s,stats,screen,sb,ship,aliens,bullets,dead,go,game_o,power,a_bullets)
            if po.status==True :
                gf.update_po(po,ship,sb,power)
            gf.update_screen(ai_s,screen,stats,sb,ship,aliens,bullets,po,a_bullets)

run_game()
