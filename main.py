#Olukemi Odujinrin
#Tuesday January 9th 2018

from datetime import datetime
now = datetime.now()

print "Welcome to 241Pizza Sales and Ingredients Managing Calculator App."
print "These are your products and their prices."

products = {'Small pizza' : 6.99 , 'Medium pizza' : 8.99, 'Large pizza' : 11.99, 'X-Large pizza' : 13.99, 'Party Size pizza' : 19.99, 'Slice pizza' : 3.99, 'Beverages' : 1.29,'6pc wings' : 5.99, '10pc wings' : 8.99, '15pc wings' : 12.99,  '20pc wings' : 16.99, 'Garlic Bread' : 4.29, '6pc knots' : 4.99, '5 donuts' : 3.99, '10 donuts' : 6.99, 'Deliveries' : 2.99}

while True:
  print "PIZZAS"
  smpizza = int(raw_input("Small pizzas sold this week:"))
  mepizza = int(raw_input("Medium pizzas sold this week:"))
  lrpizza = int(raw_input("Large pizzas sold this week:"))
  xlpizza = int(raw_input("X-Large pizzas sold this week:"))
  pspizza = int(raw_input("Party Size pizzas sold this week:"))
  slpizza = int(raw_input("Slice pizzas sold this week:"))
  print "BEVERAGES"
  drink = int(raw_input("Drinks sold this week:"))
  print "SIDES"
  chick6 = int(raw_input("6pc chicken wings sold this week:"))
  chick10 = int(raw_input("10pc chicken wings sold this week:"))
  chick15 = int(raw_input("15pc chicken wings sold this week:"))
  chick20 = int(raw_input("20pc chicken wings sold this week:"))
  gabrd = int(raw_input("Garlic breads sold this week:"))
  print "SWEETS"
  knots6 = int(raw_input("6pc knots sold this week:"))
  donut5 = int(raw_input("5pc donuts sold this week:"))
  donut10 = int(raw_input("10pc donuts sold this week:"))
  print "DELIVERIES"
  delivery = int(raw_input("Deliveries this week:"))
  print "TIPS"
  t = raw_input("Were there any tips this week? yes/no:")
  if t == 'yes' or 'y' or 'Y' or 'Yes':
    tips = float(raw_input("How much tip e.g($2.00):"))
    
  else:
    print str(0)
    
  def pro_cost(quantity, price):
    return quantity * price
   
  sm_cost = pro_cost(smpizza, products['Small pizza'])
  me_cost = pro_cost(mepizza, products['Medium pizza']) 
  lr_cost = pro_cost(lrpizza, products['Large pizza']) 
  xl_cost = pro_cost(xlpizza, products['X-Large pizza']) 
  ps_cost = pro_cost(pspizza, products['Party Size pizza']) 
  sl_cost = pro_cost(slpizza, products['Slice pizza'])
  dr_cost = pro_cost(drink, products['Beverages'])
  c6_cost = pro_cost(chick6, products['6pc wings']) 
  c10_cost = pro_cost(chick10, products['10pc wings'])
  c15_cost = pro_cost(chick15, products['15pc wings']) 
  c20_cost = pro_cost(chick20, products['20pc wings']) 
  ga_cost = pro_cost(gabrd, products['Garlic Bread'])
  k6_cost = pro_cost(knots6, products['6pc knots']) 
  d5_cost = pro_cost(donut5, products['5 donuts'])
  d10_cost = pro_cost(donut10, products['10 donuts'])
  de_cost = pro_cost(delivery, products['Deliveries'])
  
  def pizza_cost(small, medium, large, xlarge, party, slices):
    return small + medium + large + xlarge + party + slices
     
  totalpizza_cost = pizza_cost(sm_cost, me_cost, lr_cost, xl_cost, ps_cost, sl_cost)
  
  def sides_cost(drinks, chick_6, chick_10, chick_15, chick_20, garlic):
    return drinks + chick_6 + chick_10 + chick_15 + chick_20 + garlic
    
  totalsides_cost = sides_cost(dr_cost, c6_cost, c10_cost, c15_cost, c20_cost, ga_cost)
  
  def sweets_cost(knots, donuts_5, donuts_10):
    return knots + donuts_5 + donuts_10
    
  totalsweets_cost = sweets_cost(k6_cost, d5_cost, d10_cost)
    
  def extra_cost(delivery, tip):
    return delivery + tip
   
  totalextra_cost = extra_cost(de_cost, tips)
  
  def semi_total(pizza, sides, sweets, extra):
    return pizza + sides + sweets + extra 
    
  semitotal = semi_total(totalpizza_cost, totalsides_cost, totalsweets_cost, totalextra_cost)
  print semitotal
  
  def taxes(part, thirteen):
    return part * thirteen
    
  tax = taxes(semitotal, 0.13)
  print tax
  
  def total(part1, part2):
    return part1 + part2
    
  grand_total = total(semitotal, tax)
  
  print "These are your sales this week"
  print '%s-%s-%s' % (now.year, now.month, now.day)
  print grand_total
  
  exit = raw_input("Would you like to exit the app? yes/no:")
  if exit == 'yes' or 'y' or 'Y' or 'Yes':
    print "HAVE A NICE DAY!"
    break
  else:
    print "Okay"
  
  

    

  
  

