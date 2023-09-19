import pygame
from pygame import mixer
import random
import os
import math

pygame.init()

# layar
W = 600
H = 600
layar = pygame.display.set_mode((W, H))

black = (0, 0, 0)
red = (190, 0, 0)
green = (0, 200, 0)
lavender = (230, 230, 250)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
# Caption & Logo
pygame.display.set_caption('PENYIHIR VS VIRUS CORONA')
logo = pygame.image.load('assets/Logo.png')
pygame.display.set_icon(logo)

# Penyihir
penyihirImg = pygame.image.load('assets/witch.png')
penyihirX = 40
penyihirY = 260
penyihirY_berubah = 0

# MUSUH 1 : CORONA
coronaImg = []
coronaX = []
coronaY = []
coronaX_berubah = []
coronaY_berubah = []
jumlahcorona = 5

# MUSUH 2 : RAJA COVID
rajacovidImg = []
rajacovidX = []
rajacovidY = []
rajacovidX_berubah = []
rajacovidY_berubah = []
jumlahrajacovid = 3

# PELURU
peluruImg = pygame.image.load('assets/sihir.png')
peluruX = 40
peluruY = 0
peluruX_berubah = 10
peluruY_berubah = 0
peluru_kode = "siap"

# SKOR
nilai_skor = 0
font = pygame.font.Font('assets/freesansbold.ttf',40)
textX = 10
textY = 538

# EFEK SUARA
mixer.music.load("assets/Blazer Rail.wav")
mixer.music.play(-1)

# TULISAN-TULISAN
over_font = pygame.font.Font('assets/Mystery.ttf',45)

for i in range (jumlahcorona):
    coronaImg.append(pygame.image.load('assets/corona.png'))
    coronaX.append(random.randint(480,568))
    coronaY.append(random.randint(0,430))
    coronaX_berubah.append(45)
    coronaY_berubah.append(0.5)

for i in range (jumlahrajacovid):
    rajacovidImg.append(pygame.image.load('assets/rajacorona.png'))
    rajacovidX.append(random.randint(480,568))
    rajacovidY.append(random.randint(0,400))
    rajacovidX_berubah.append(0.3)
    rajacovidY_berubah.append(50)

latar = pygame.image.load(os.path.join('','assets/citybackground_gothic.png')).convert()
latarX = 0
latarX2 = latar.get_width()

waktu = pygame.time.Clock()

# FUNGSI
def penyihir(x,y):
    layar.blit(penyihirImg, (x, y))

def corona(x,y,i):
    layar.blit(coronaImg[i],(x, y))

def rajacovid(x,y,i):
    layar.blit(rajacovidImg[i],(x, y))

def pelurutembak(x,y):
    global peluru_kode
    peluru_kode = "tembak"
    layar.blit(peluruImg,(x+80,y+30))

def rajacovid_mati(rajacovidX,rajacovidY,peluruX,peluruY):
    jarak = math.sqrt(math.pow(rajacovidX-peluruX,2)+(math.pow(rajacovidY-peluruY,2)))
    if jarak < 25:
        return True
    else:
        return False

def corona_mati(coronaX,coronaY,peluruX,peluruY):
    jarak = math.sqrt(math.pow(coronaX-peluruX,2)+(math.pow(coronaY-peluruY,2)))
    if jarak < 25:
        return True
    else:
        return False

def tampilan_skor(x,y):
    skor = font.render("SKOR : "+str(nilai_skor),True,(255,255,255))
    layar.blit(skor,(x,y))

def game_over_text():
    over_text = over_font.render ("GAME OVER", True, (255,255,255))
    layar.blit(over_text,(50,200))

# KUMPULAN INTRO FUNGSI
def tombol(pesan, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(layar, ac, (x, y, w, h))
    else:
        pygame.draw.rect(layar, ic, (x, y, w, h))

    tombolteks = pygame.font.Font("assets/freesansbold.ttf", 20)
    teksSurf, teksRect = teks_objek(pesan, tombolteks)
    teksRect.center = ((x + (w / 2)), (y + (h / 2)))
    layar.blit(teksSurf, teksRect)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if 110 + 125 > mouse[0] > 125 and 470 + 50 > mouse[1] > 470:
                if click[0] == 1:
                    intro = False
            elif 370 + 125 > mouse[0] > 125 and 470 + 50 > mouse[1] > 470:
                if click[0] == 1:
                    pygame.quit()
                    quit()
            else :
                break

        layar.fill(lavender)
        largeTeks = pygame.font.Font('assets/Bing Bam Boum.ttf', 55)
        TeksSurf, TeksRect = teks_objek("PENYIHIR", largeTeks)
        TeksRect.center = ((W / 2), (H / 6.2))
        layar.blit(TeksSurf, TeksRect)
        TeksSurf, TeksRect = teks_objek("VS", largeTeks)
        TeksRect.center = ((W / 2), (H / 3.9))
        layar.blit(TeksSurf, TeksRect)
        TeksSurf, TeksRect = teks_objek("VIRUS CORONA", largeTeks)
        TeksRect.center = ((W / 2), (H / 2.7))
        layar.blit(TeksSurf, TeksRect)
        storyboard = pygame.font.Font('assets/Earworm.otf',22)
        TeksSurf, TeksRect = teks_objek("Mari bantu penyihir melawan Virus Corona !", storyboard)
        TeksRect.center = ((W / 2), (H / 1.95))
        layar.blit(TeksSurf, TeksRect)
        TeksSurf, TeksRect = teks_objek("Tekan Tombol ATAS atau BAWAH pada Keyboard untuk terbang", storyboard)
        TeksRect.center = ((W / 2), (H / 1.80))
        layar.blit(TeksSurf, TeksRect)
        TeksSurf, TeksRect = teks_objek("Tekan Tombol SPASI pada Keyboard untuk melempar mantra", storyboard)
        TeksRect.center = ((W / 2), (H / 1.68))
        layar.blit(TeksSurf, TeksRect)
        penyihir2Img = pygame.image.load('assets/witch2.png')
        layar.blit(penyihir2Img,(50,60))
        rajacovidImg2 = pygame.image.load('assets/rajacorona.png')
        layar.blit(rajacovidImg2, (473,195))

        tombol("MULAI", 110, 470, 125, 50, green, bright_green)
        tombol("KELUAR", 370, 470, 125, 50, red, bright_red)

        pygame.display.update()
        waktu.tick(60)

def teks_objek(text, font):
    teksSurface = font.render(text, True, black)
    return teksSurface, teksSurface.get_rect()

# MAIN
speed = 30
game_intro()
run = True
while run:
    layar.fill((0, 0, 0))
    layar.blit(latar, (latarX, 0))
    layar.blit(latar, (latarX2, 0))
    latarX -= 1.4
    latarX2 -= 1.4
    if latarX < latar.get_width() * -1:
        latarX = latar.get_width()
    if latarX2 < latar.get_width() * -1:
        latarX2 = latar.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Tombol
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                penyihirY_berubah = -6
            if event.key == pygame.K_DOWN:
                penyihirY_berubah = 6
            if event.key == pygame.K_SPACE:
                if peluru_kode == "siap":
                    suarapeluru = mixer.Sound("assets/sparkle.wav")
                    suarapeluru.play()
                    peluruY = penyihirY
                    pelurutembak(peluruX, peluruY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                penyihirY_berubah = 0

    penyihirY += penyihirY_berubah

    if penyihirY <= 0:
        penyihirY = 0
    if penyihirY >= 430:
        penyihirY = 430

    for i in range(jumlahcorona):

        if coronaX[i] < 0:
            penyihirX = -200
            for j in range(jumlahcorona):
                coronaX[j] = -200
            for k in range(jumlahrajacovid):
                rajacovidX[k] = -200
            peluruX = -200
            peluruY = -200
            game_over_text()
            break

        coronaY[i] += coronaY_berubah[i]
        if coronaY[i] <= 0:
            coronaY_berubah[i] = 5
            coronaX[i] -= coronaX_berubah[i]
        elif coronaY[i] >= 430:
            coronaY_berubah[i] = -5
            coronaX[i] -= coronaX_berubah[i]

        coronamati = corona_mati(coronaX[i], coronaY[i], peluruX, peluruY)
        if coronamati:
            musnah = mixer.Sound("assets/virusmeledak.wav")
            musnah.play()
            peluruX = 40
            peluru_kode = "siap"
            nilai_skor += 10
            coronaX[i] = random.randint(480, 568)
            coronaY[i] = random.randint(0, 430)

        corona(coronaX[i], coronaY[i], i)

    for i in range(jumlahrajacovid):

        if rajacovidX[i] < 0:
            penyihirX = -200
            for j in range(jumlahrajacovid):
                rajacovidX[j] = -200
            for k in range(jumlahcorona):
                coronaX[k] = -200
            peluruX = -200
            peluruY = -200
            game_over_text()
            high_score = 0
            break

        rajacovidX[i] -= rajacovidX_berubah[i]
        if rajacovidY[i] < 40:
            rajacovidY[i] = 40
        elif rajacovidY[i] > 400:
            rajacovidY[i] = 400

        rajacovidmati = rajacovid_mati(rajacovidX[i], rajacovidY[i], peluruX, peluruY)
        if rajacovidmati:
            musnah = mixer.Sound("assets/virusmeledak.wav")
            tawapenyihir = mixer.Sound("assets/tertawa.wav")
            musnah.play()
            tawapenyihir.play()
            peluruX = 40
            peluru_kode = "siap"
            nilai_skor += 10
            speed += 1
            rajacovidX[i] = random.randint(480, 568)
            rajacovidY[i] = random.randint(0, 400)

        rajacovid(rajacovidX[i], rajacovidY[i], i)

    if peluruX >= 600:
        peluruX = 40
        peluru_kode = "siap"

    if peluru_kode == "tembak":
        pelurutembak(peluruX, peluruY)
        peluruX += peluruX_berubah

    penyihir(penyihirX, penyihirY)
    tampilan_skor(textX, textY)
    waktu.tick(speed)
    pygame.display.update()
