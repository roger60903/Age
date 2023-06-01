D = input('請問您有沒有開過車? ')
if D != "有" and D != "沒有":
	print('只能輸入 有/沒有 ')
	raise SystemExit
age = input('請問您的年齡? ')
age = int(age)
if D == "有":
	if age >= 18:
		print('您通過測驗了! ')
	else:
		print('奇怪，您怎麼會開過車? ')
elif D == "沒有":
	if age >= 18:
		print('您怎麼還沒考駕照，您可以考駕照了! ')
	else:
		print('很好，你再過幾年就可以考駕照了! ')