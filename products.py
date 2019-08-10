products = []
while True:
	name = input('請輸入品名: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	products.append([name, price])

with open('products.csv','w',encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' +p[1]+'\n')
	