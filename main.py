import turtle
import random
import time



#arkaplan ayarlamaları
drawing_board= turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch the Turtle")

#turtle tanımlamalarım
hedef = turtle.Turtle()
hedef.shape(name="turtle")
hedef.penup()
sure= turtle.Turtle()
sure.penup()
sure.hideturtle()
sure.goto(100,200)
skor=turtle.Turtle()
skor.hideturtle()
skor.penup()
skor.goto(-250,200)



zorluk=0.65
kalansure=30
skor_puan= 0

print("Oyunuma hoşgeldiniz..")
print("Zorluk derecenizi seçtikten sonra oyuna başlayabilirsiniz..")
print("1)Kolay,2)Orta,3)Zor")
secim= int(input())
if secim==1:
    zorluk=1
elif secim==2:
    zorluk=0.65
elif secim==3:
    zorluk=0.45
else:
    print("Hatalı işlem,default ayarlar girildi..")




def tıklama(x,y):
    global skor_puan
    if hedef.distance(x,y)<20:
        hedef.hideturtle()
        skor_puan+=1
        skor.clear()
        skor.write(f'Skorunuz = {skor_puan}', font=('Comic Sans MS', 20, 'normal'))
while kalansure>0:
    skor.write(f'Skorunuz = {skor_puan}', font=('Comic Sans MS', 20, 'normal'))
    hedef.onclick(tıklama)
    sure.write(f'Kalan süre = {kalansure}', font=('Comic Sans MS', 20, 'normal'))
    x = random.randint(-300, 300)
    y = random.randint(-300, 200)
    kalansure -= 1
    hedef.hideturtle()
    hedef.goto(x, y)
    hedef.showturtle()
    time.sleep(0.65)
    sure.clear()
    if kalansure == 0:
        hedef.hideturtle()
        sure.goto(-100, 0)
        sure.write('Süre bitti!', font=('Comic Sans MS', 30, 'normal'))
        skor.clear()
        skor.goto(-100, 100)
        skor.write(f'İşte puanınız! = {skor_puan}', font=('Comic Sans MS', 30, 'normal'))
        break

turtle.mainloop()


