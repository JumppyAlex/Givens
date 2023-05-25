#Lets assume students Project marks were given 
#Create a program that takes the mark ,and decides ;

#If student has fail ,below AVg ,AVg ,above AVg.
marks=float (input('What did you score?:'))
if marks<= 30:
    print('You scored ',marks)
    print('Failed')

elif marks>30 and marks<=40:
    print('you scored ',marks)
    print('Below Average ')

elif marks> 40 and marks <=60:
    print('you scored ' ,marks )
    print('Average')

elif marks > 60 and marks <-100:
    print('you scored', marks)
    print('Above Average')

else :   
    print('Invalid')
