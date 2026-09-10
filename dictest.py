'''sales = """Paracetamol, 25, 1500
Amoxicillin, 10, 3000
Vitamin C, 15, 2000
Paracetamol, 12, 1500
Ibuprofen, 8, 2500
Amoxicillin, 5, 3000"""

salesProducts = {} 

textListOfProducts = sales.split('\n')

def listOfProductToDictPacking(listofprod):
 for product in listofprod:
  productname, productquantity, productprice = product.split(', ')
  salesProducts[productname]= {}
  salesProducts[productname]['name']= productname
  salesProducts[productname]['quantity']= productquantity
  salesProducts[productname]['sales']= productprice

 print(salesProducts)
 

listOfProductToDictPacking(textListOfProducts) '''


sales = """Paracetamol, 25, 1500
Amoxicillin, 10, 3000
Vitamin C, 15, 2000
Paracetamol, 12, 1500
Ibuprofen, 8, 2500
Amoxicillin, 5, 3000"""

salesProducts = {} 

textListOfProducts = sales.split('\n')

def listOfProductToDictPacking(listofprod):
 for product in listofprod:
  productname, productquantity, productprice = product.split(', ')
  if productname in salesProducts.keys():
   salesProducts[productname]['quantity']= int(salesProducts[productname]['quantity']) + int(productquantity)
   salesProducts[productname]['sales']= int(salesProducts[productname]['sales']) + int(productprice)
  
  else: 
   salesProducts[productname]= {}
   salesProducts[productname]['name']= productname
   salesProducts[productname]['quantity']= int(productquantity)
   salesProducts[productname]['sales']= int(productprice)
 
 print(salesProducts) 

 for prod in salesProducts.values():
   print('\n'+ prod['name']+':')
   print('   quantity = '+ str(prod['quantity']))
   print('   sales = '+ str(prod['sales']))
 

listOfProductToDictPacking(textListOfProducts)

