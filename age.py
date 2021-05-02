driving = input('你有沒有開過車?')
if driving != ('有') and driving != ('沒有'):
    print('只能回答"有"或"沒有"')
    raise SystemExit
age = input('請輸入年齡: ')
age = int(age)
if driving == '有':
	if age > 18:
	    print('恭喜你!通過測驗了!')
	else:
	    print('未滿18歲怎麼會開過車呢?')
elif driving == '沒有':
    if age > 18:
        print('成年了可以考駕照了')
    else:
        print('再過幾年就可以考駕照了')