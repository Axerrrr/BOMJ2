from time import *
from random import *
from colorama import Fore , Back , Style , init
import os 
seed(clock())
init()
print('Выбери 1 из 4 классов : Воин , Рыцарь , Вор , Ничтожество')
a = input()
if a=='Воин':
	print (Fore.GREEN+'75 hp' , '15 dmg'+Style.RESET_ALL)
	hp=75
	dmg=15
elif a=='Рыцарь':
	print(Fore.GREEN+'100hp , 10 dmg'+Style.RESET_ALL)
	hp=100
	dmg=10
elif a=='Вор':
	print(Fore.GREEN+'50hp , 20 dmg'+Style.RESET_ALL)
	hp=50
	dmg=20 
elif a=='Ничтожество':
	print(Fore.GREEN+'30hp , 5 dmg'+Style.RESET_ALL)	
	hp=30
	dmg=5
input()
i=0
gold=100
while 1: 
	HP=200
	H2P=60
	os.system("cls")
	a = randrange(5)
	if a==0:
		print('вы видети  шаткий мост над обрывом ')
		q = int(input('1-пройти по нему\n 2 - пройти мимо по дорожке\n 3 - Покинуть мир '))
		if q==1:
			dmg=dmg+2
			print('Вы нашли магическую руну силы' , dmg)
		elif q==2:
			dmg=dmg+1
			print('Вы нашли деревянный меч ' , dmg )	
		elif q==3:
			break
	elif a==1:
		print('Вы нашли вход в пещеру ')
		q=int(input(' 1 - Войти в нее\n 2 - уйти\n'))
		if q==1:
			hp=hp-25
			print('Вы попали в ловушку , у вас отнялось 25hp ' , hp )
			dmg=dmg+10
			print('Вы нашли железный меч' , dmg)
		elif q==2:
			hp=hp+25
			print('Вы нашли целебный фонтан в лесах , вам добавилось 25hp ' ,  hp)
		elif q==3:
			break
	elif a==2:
		print(Back.RED+'Вы наткнулись на дикого кабана'+Style.RESET_ALL)
		q=int(input('1 - ударить\n 2 - пройти мимо\n '))
		if q==1:
			while 1 :
				print('Вы атакавали  ')
				H2P=H2P-dmg
				print('Вы получили 2 урона ')
				hp=hp-2 
				if H2P<=0:
					print('you win')
					break
				if hp<=0:
					print('you lose')	
					break
					continue
			gold=gold+5		
			print('Вы получили 5 монет ')
		elif q==2:
			 print ('Вы прошли мимо и не получили ничнго  ')	
		elif q==3:
			break 
	elif a==3:
		print(Back.RED+'Вы нашли Огра '+Style.RESET_ALL)
		print(HP ,' 15 dmg')
		q=int(input('1-Сражаться\n  2-Отступить \n'))
		if q==1:
			while 1 :
				print('Вы атакавали ')
				HP=HP-dmg
				print('Вы получили 15 урона ')
				hp=hp-15 
				if HP<=0:
					print('you win')
					break
				if hp<=0:
					print('you lose')	
					break
					continue
			gold=gold + 30		
			print('20 монет')
		elif q==2:
			print ('Вы отступили')
		elif q==3:
			break
	elif a==4:
		while 1 :
			print(Fore.GREEN+'Вы нашли потайной магазин'+Style.RESET_ALL)
			q=int(input('1 - Зелье регенерации\n 2-Зелье силы\n 3-Выйти из лавки\n 4-Сохраниться\n 5-Загрузить\n'))
			if q==1:
				hp=hp+50
				if gold>=100:
					gold=gold-100
					print('Зелье успешно купленно',  hp ,'hp' , gold ,'gold' )
				elif gold<100:
					gold=gold
					print('Недостаточно средств', gold ,'gold' )
			elif q==2:
				if gold>=200:
					gold=gold-200
					dmg=dmg+2
					print('Зелье успешно купленно',  dmg ,'dmg' , gold ,'gold' )
				elif gold<200:
					print('Недостаточно средств', gold , 'gold' )
					gold=gold
			elif q==3:
				break
			elif q==4:
				save = open('save.txt' , 'w' )
				save.write('hp '+ str(hp)+'\ndmg '+str(dmg)+'\ngold '+str(gold) )
				save.close()
			elif q==5:
				break
	input()	
if i==i+1 :
	print('Game Over')
elif hp<=0 :
	print('Game Over')
		



