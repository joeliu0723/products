products = []
while True:
	name = input('請輸入品名: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	products.append([name, price])

with open('products.csv','w') as f:
	for p in products:
		f.write(p[0] + ',' +p[1]+'\n')
	