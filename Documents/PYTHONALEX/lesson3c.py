# Dictionary: uesd to store data in key - values Pairs 
# Dictionary is changable -mutable, no duplicates 
# Uses {} to hold item
student ={'name' :'Jane',
            'age': 26,
            'adm': 10000,
            'county':'Tana River',
            'gender':'Female',
            'maths': 56,
            'english':89 ,
            'social':90 }


print(student)

# Accesing items in dictionary uses keys to access 
print('She is ',student['name'])
print('She Lives in',student['county'])
print('Her Maths Score',student['maths'])

# Add/Update/Delete an item 
student['age'] =18 # Update -Existing
student['biology'] =85 # Adding - New Entry
del student['adm'] #Delete adm
print(student)

#Dictionaries 
#1. Uses {} to hold items
#2. Can be Updated - Mutable 
#3. Items are added in key value pairs i.e ' name':'John'
#4. Access Items by using keys i.e student['maths']




