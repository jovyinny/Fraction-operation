import re,time

def add(first, second):
    ans=int(first [1])* int(second[1])
    final= int((int(ans)/int(first[1]))*int(first[0]))+int((int(ans)/int(second[1]))*int(second[0]))
    for i in range(1,ans):
        if ans%i==0 and final%i==0:
            ans=int(ans/i)
            final=int(final/i)
            if ans == final:
                ans=1
                final=1  
    time.sleep(1)
    print("The addition answer is {}/{}".format(final,ans))
  
      
def sub(first, second):
    ans=int(first [1])* int(second[1])
    final= int((int(ans)/int(first[1]))*int(first[0]))-int((int(ans)/int(second[1]))*int(second[0]))
    
    for i in range(1,ans):
        if ans%i==0 and final%i==0:
            ans=int(ans/i)
            final=int(final/i)
            if ans == final:
                ans=1
                final=1
    time.sleep(1) 
    print("The subtraction answer is {}/{}".format(final,ans))
    
    
def multiply(first, second):
    ans=int(first [1])* int(second[1])
    final= int((first[0]))*(int(second[0]))
    for i in range(1,ans):
        if ans%i==0 and final%i==0:
            ans=int(ans/i)
            final=int(final/i)
            if ans == final:
                ans=1
                final=1
    time.sleep(1)          
    print("The multiplication answer is {}/{}".format(final,ans))
    
       
def divide(first, second):
    ans=int(first [1])* int(second[0])
    final= int((first[0]))*int(second[1])
    
    for i in range(1,ans):
        if ans%i==0 and final%i==0:
            ans=int(ans/i)
            final=int(final/i)
            if ans == final:
                ans=1
                final=1
    time.sleep(1)
    print("The division answer is {}/{}".format(final,ans))
    


def start():
    try:
        print("Welcome to fraction operator made by Jovine....")
        pattern=r"(\-?\d+)(/)?(\-?\d+)?"
        user_frac1=(input("Enter first fraction: "))
        user_frac2=input("Enter second fraction: ")
        first=[]
        second=[]
        match1=re.search(pattern,user_frac1)
        match2=re.search(pattern, user_frac2)
        print("Enter.....")
        time.sleep(1)
        print("1 for addition........")
        print("2 for subtraction.........")
        print("3 for multiplication......")
        print("4 for division..............")
        print("0 for all operations......\n")
        user=int(input("Enter option for operation: "))
        if match1 and match2:
            first.insert(0,int(match1.group(1)))
            second.insert(0,int(match2.group(1)))
            
            if match1.group(3)==None:
                first.insert(1,1)
            if match2.group(3)==None:
                second.insert(1,1)   
            if match1.group(3) != None:
                first.insert(1,int(match1.group(3)))
            if match2.group(3) != None:
                second.insert(1,int(match2.group(3)))
                

        if user==1:
            add(first, second)
        elif user==2:
            sub(first, second)
        elif user==3:
            multiply (first, second)
        elif user==4:
            divide(first, second)
        elif user==0:
            add(first, second)
            sub(first, second)
            multiply (first, second)
            divide (first, second)
        else:
            print ("Invalid input....")
        time.sleep(1)  
        print("Good bye......")
    
    except (TypeError,IndexError):
        print ("Error.....")  
    
    
start()