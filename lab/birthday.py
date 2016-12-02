from random import randint

def gen_date(month):
	if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		return randint(1,31)
	elif month == 4 or month == 6 or  month == 9 or month == 11:
		return randint(1,30)
	elif month == 2 :
		return randint(1,29)
	else:
		return "invalid month"

def no_of_pairs(persons):
	birthdays=[]
	number=0
	for i in range(persons):
		# month=randint(1,12)
		# date=gen_date(month)
		# birthdays.append((date,month))
		birthdays.append(randint(1,366))
	for i in range(len(birthdays)-1):
		for j in range(i+1,len(birthdays)):
			if birthdays[i]==birthdays[j]:
				number+=1
	return number

persons=60
trials=1000
count=0
for i in range(trials):
	count+=no_of_pairs(persons)

pairs=count/trials
print(pairs)
