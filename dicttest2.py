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
   if name in prod:
    productSalesInfo[name]={}
    for data in prod:
     print(data)
     for i in range(len(labels)):
      print(i)      
      productSalesInfo[name][labels[i]]= data
      print(productSalesInfo)   
 
 print(productSalesInfo)
 

 #{
 #   'total_items_sold': {},
 #  'total_sales': {},
 #   'product_sales': {}
 #}


analyzeSales(sales)

 

 

 