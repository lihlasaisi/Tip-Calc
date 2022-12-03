#Lihla Saisi Shiribwa lihla.saisi@azubiafrica.org

def mortgagecalc(Principal, rate, years):
    n = years*12 #number of monthly repayments
    r = (rate/100)/12 #monthly interest rate
    MonthlyPayment = (r*Principal*((1+r)**n))/(((1+r)**n-1))
    return MonthlyPayment
years = float (input('Input years of Loan: '))
rate = float (input('Input annual interest: '))
Principal = int (input('Input the Loan Amount: '))

print ('Monthly Repayment: Ksh {:.2f}'.format(mortgagecalc(Principal, rate, years)))
print ('Total Repayment: Ksh {:.2f}'.format(mortgagecalc(Principal, rate, years)*(years*12)))