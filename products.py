products = []
while True:
	name = input('請輸入品名')
	if name == 'q':
		break
	price = input('請輸入價格')
	products.append([name, price])

print(products)
