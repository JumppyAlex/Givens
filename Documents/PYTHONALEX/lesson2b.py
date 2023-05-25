
#Method 2
#Formula :PRT/100
#Dynamic variables - Allow someone to key in
principle =float(input ('Enter Principle Amount KES?:'))
rate =float(input('Enter Interest Rate?:'))
time =int(input('Enter Time in years?:'))


#Do some arithmetic
interest =principle*rate*time/100
print('Yearly Interest is Ksh.',interest)
