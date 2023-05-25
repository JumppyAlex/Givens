#List,Tuple and Dictionary
#List -Can store mmultiple items at home 
apps =['Whatsaap','Facebook','Tiktok','Twitter','Linkedin','Pinterest']

print(apps)

#Accessing Items at Indexes You count from 0
print(apps[1]) #Facebook
print(apps[2:5]) #Print upto Index 4

#Can we add Items in a List ? Yes 
# Can we remove Items from a list ? Yes 
apps.append('Netflix')
apps.append('Instagram')
apps.insert(0,"Messenger ")
print(apps)

apps.remove('Tiktok')
print(apps)

# Can we randomise /Shuffle ? Yes 
import random
random.shuffle(apps)
print(apps)



