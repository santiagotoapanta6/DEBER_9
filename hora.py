import time
hora = 0
minut = 0
segu = 0

for h in range (0,23):
	for m in range (0,59):
		for s in range (0,60):
			print(h + m + s)
			time.sleep(1)