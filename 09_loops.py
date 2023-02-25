#while and for loops 

#while loops

# x=0
# while(x<5):
#     print(x)
#     x=x+1

# x=0
# while(x<10):
#     print(x)
#     x=x+1

#for loop

# x=0
# for x in range (1,9):
#     print(x)
    

#arrays

days=["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]

for d in days:
    #if(d=="Saturday"):break     #stop loop 
    if(d=="Saturday"):continue   #skips d
    print(d)
