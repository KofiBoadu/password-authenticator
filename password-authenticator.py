import re

print("PLEASE CREATE A PASSWORD BELOW")

print("must include special characters and more than 5 characters")

attempts= 0

while attempts < 3:
    
    
    password= input("create a password: ")
    
    special_char= re.compile("[@_!#$%^&*()<>?/\|}{~:]")

#checking if special characters are in my password


    if (special_char.search(password)== None) or len(password) < 5:
        
        attempts+=1
    
        print(f"failed !! you tried {attempts} times make sure you check password requirements and try again")
        
        
        if attempts==attempts:
            
            print("Too many attempts cant create password !!")
            

        
    else:
        
        
        
        print("PASWORD CREATED SUCCESFFULLY ")
        
        break
        
        
        
           
            