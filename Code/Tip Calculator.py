#Lihla Saisi Shiribwa lihla.saisi@azubiafrica.org Group 4

def tipcalc(Food):
    tip = Food * 0.18
    sales = Food * 0.07
    grandtotal = Food + tip + sales
    return grandtotal


Food = float (input('How Much was your Food Bill: '))
Tip = Food * 0.18
SalesTax = Food * 0.07

print ('Tip: Ksh {:.2f}'.format(Tip))
print ('Sales Tax: Ksh {:.2f}'.format(SalesTax))
print ('Total Bill: Ksh {:.2f}'.format (tipcalc(Food)))