LP= eval(input('Length of loan period in years: '))
amount= eval(input('Loan amount:'))
AIR=eval(input('annual interest rate as percent: '))

MIR = ((AIR/100)/12)

MP=(MIR*amount)/(1-((1+MIR)**(-(LP*12))))
INRT=amount*MIR
prin=MP-INRT
bal=amount-prin
Tot=amount*MIR
print('No.','Payment','Interest','Principal','Balance','Total Interst')
for i in range (1,LP*12+1):
    print('{:2}{:8.2f}{:10.2f}{:10.2f}{:10.2f}{:10.2f}'.format(i,MP,INRT,prin,bal,Tot))
    INRT=bal*MIR
    prin=MP-INRT
    bal=bal-prin
    Tot=Tot+INRT
    
    
 
    
