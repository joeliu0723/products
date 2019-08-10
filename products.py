#讀取檔案
products = []
with open('products.csv','r',encoding = 'utf-8') as f:
	for line in f:
		name , price = line.strip().split(',')#已經list有兩欄,所以直接將name與price一起被指定. 等號後面是先去掉換行符號(strip),再切從有逗號的段落切斷(spilt)
		products.append([name, price]) #以二維list的方式將兩欄直接加進list裡
print(products)
	
#寫入檔案
while True:
	name = input('請輸入品名: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	products.append([name, price])

with open('products.csv','w',encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' +p[1]+'\n') #用+的方式將字串組合一起,並用逗點分隔,最後換行
	