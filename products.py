import os #匯入作業系統模組
#讀取檔案
def read_file(filename):
    products = []
    
    with open(filename,'r',encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #跳過有商品價格那欄,直接往下執行
            name , price = line.strip().split(',')#已經list有兩欄,所以直接將name與price一起被指定. 等號後面是先去掉換行符號(strip),再切從有逗號的段落切斷(spilt)
            products.append([name, price]) #以二維list的方式將兩欄直接加進list裡
    return products 

#使用者輸入品名價格
def user_input(products):
    while True:
        name = input('請輸入品名: ')
        if name == 'q':
            break
        price = input('請輸入價格: ')
        products.append([name, price])
    return products
    print(products)

#寫入檔案
def write_file(filename,products):
    with open(filename,'w',encoding = 'utf-8') as f:
         f.write('商品,價格\n')
         for p in products:
             f.write(p[0] + ',' +p[1]+'\n') #用+的方式將字串組合一起,並用逗點分隔,最後換行
#主要執行檔用function表示
def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#檢查csv檔在不在資料夾內,以免crash
        products = read_file(filename)
        print('找到檔案了')
    else:
        print('找不到檔案')

    products = user_input(products)
    write_file('products.csv',products)

main()
