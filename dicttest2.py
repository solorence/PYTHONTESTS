sales = """Paracetamol, 25, 1500
Amoxicillin, 10, 3000
Vitamin C, 15, 2000
Paracetamol, 12, 1500
Ibuprofen, 8, 2500
Amoxicillin, 5, 3000"""



def analyzeSales(sales):
 productSalesInfo = {}
 productSalesCollection2 = []
 labels=['product', 'quantity', 'price']
 productNames= ['Paracetamol', 'Amoxicillin', 'Vitamin C', 'Ibuprofen']

 productSalesCollection1 = sales.split('\n') 
 
 for index in range(len(productSalesCollection1)):
  productSalesCollection2.append((productSalesCollection1[index]).split(', '))

 print(productSalesCollection2)
 
 for prod in productSalesCollection2:
  for name in productNames:
   if name in prod and name in productSalesInfo.keys():
    productSalesInfo[name][labels[1]]+= int(prod[1])
    continue
   
   if name in prod:
    productSalesInfo[name]={}
    for i in range(len(labels)):     
     productSalesInfo[name][labels[i]]= prod[i]
     if productSalesInfo[name][labels[i]].isdecimal():
      productSalesInfo[name][labels[i]] = int(productSalesInfo[name][labels[i]]) 
   
 
 print('\nproductSalesInfo'.upper(),'= ', productSalesInfo)
 

 analysis = {
   'total_items_sold':0,
   'total_sales': 0,
   'product_sales': {}
 }

 for name in productSalesInfo.keys():
  analysis['total_items_sold'] += productSalesInfo[name]['quantity']

 for name in productSalesInfo.keys():
  analysis['total_sales'] += productSalesInfo[name]['quantity'] * productSalesInfo[name]['price'] 
 
 for name in productSalesInfo.keys():
  analysis['product_sales'][name] = productSalesInfo[name]['quantity'] * productSalesInfo[name]['price']

 print('\nANALYSIS= ', analysis )

 

analyzeSales(sales)