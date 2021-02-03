#pyalarm
import time
from datetime import datetime,timedelta
from playsound import playsound
time_now = datetime.now()
def GetTimeAlarm(error=0):
	if error:
		print('Вы допустили ошибку.')
		GetTimeAlarm()
	print('Введите на сколько поставить будильник в формате day,hour,min')
	print('Поставьте 0 если не надо менять значение.')
	time_alarm = input('Time: ')
	if time_alarm:
		try:
			time_alarm = time_alarm.split(',')
			count = 0
			for x in time_alarm:
				count +=1
			if count == 3:
				return time_alarm
			else:
				print('Не правильно введены данные. Попробуйте снова!')
				GetTimeAlarm()
		except:
			print('Введено 1 число')
			GetTimeAlarm()
	else:
		print('Вы ничего не ввели.')
		GetTimeAlarm()

time_alarm = GetTimeAlarm()
time_alarm = [int(i) for i in time_alarm]
sounds_delay = input('Введите задержку между звуками: ')

if time_alarm:
	if time_alarm[0] > 31 and time_alarm[0] < 0: GetTimeAlarm(1)

	if time_alarm[1] == 24:
		time_alarm[0] += 1
		time_alarm[1] = 0

	if time_alarm[1] < 0 or time_alarm[1] > 24: GetTimeAlarm(1)
	if time_alarm[2] < 0 or time_alarm[2] > 60: GetTimeAlarm(1)

	if time_alarm[2] == 60:
		time_alarm[2] = 0
		time_alarm[1] += 1

time_play_alarm = time_now + timedelta(days=time_alarm[0], hours = time_alarm[1], minutes=time_alarm[2])
timeplay = time_play_alarm.strftime("%d/%m/%y %I:%M")

def PlayAlarm():
	while i < 3:
		i += 1
		playsound('alarm.wav', block = False)
		time.sleep(sounds_delay)

print( time_now )
print( time_alarm )
print( timeplay)
while True:
	time_now = datetime.now().strftime("%d/%m/%y %I:%M")
	if time_now == timeplay:
		print('Alarm!')
		PlayAlarm()
		break