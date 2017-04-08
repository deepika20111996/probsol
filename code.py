
f=open("input.txt", "r")
li=f.readlines()
#opens file "input.txt" and store lines into a list named li
NC=int(li[0])
#converts the char in first line ->li[0] into int and stores it in NC
for j in range(NC):
        n=int(li[j+1])
        #n=no. of questions in each context
        if n%2==0:
                m=2
                print(n-m, m)
        elif n==1:         
                print(0, 1)
                #1 has no prime factors so it can either be (1,0) or (0,1)   
        else:
                i=1
                while(((2*i)+1)<=n):
                        if n%((2*i)+1)==0:
                                m=((2*i)+1)
                                print(n-m, m)
                                break
                        i+=1
       
