print("-----------------ONLINE TEST------------------")
print("\n\n")
wh=int(input("if you want to coninue press 1 else press 0.......  :"))
while(wh==1):
    print("***********Student_DETAILS FORM***************")
    print("\n\n")
    name=input("Enter you name : ")
    id=int(input("Enter your Id : "))
    dept=input("Enter your department : ")
    cname=input("Enter your collge name : ")
    place=input("Enter your place : ")
    q=int(input("press 1 to go to questions... : "))
    if(q==1):
        print("1.python is an____________.\n")
        print("a.compiled\nb.interpreted\nc.both of them\nd.None of them\n")
        f=input("enter the answer : ")
        print("\n\n2.which is the most population country in the world :")
        print("a.china\nb.India\nc.america\nd.Russia")
        s=input("enter the answer: ")
        print("\n\n3.(a**2 +b**2=")
        print("a.(a=b)**2-2ab\nb.(a+b)**2+2ab\nc.(a+b)**2-2ab\nd.none of these\n")
        t=input("Enter the answer : ")
        print("\n\n4.python loop's are ") 
        print("a.for loop\nb.while loop\nc.both a and b\nd.do while")
        fo=input("enter the answer : ")
        print("\n\n5.who is father of physics ?")
        print("a.albert einsten\nb.cv Raman\nc.brook brothers\nd.none of these")
        fi=input("enter the answer : ")
    print("\n\n\n")
    print("**************************************************************************")
    print("**************************************************************************")
    print("---------STUDENT_DETAILS---------")
    print("*********************************")
    print("STUDENT ID   :",id)
    print("STUDENT NAME :",name)
    print("DEPARTMENT   :",dept)
    print("COLLAGE NAME :",cname)
    print("\n")
    print("----------------RESULT----------------")
    print("\n")
    print("ANSWERS : ")
    print("1.correct")if(f.lower()=="b")else print("1.wrong")
    print("2.correct")if(s.lower()=="b")else print("2.wrong")
    print("3.correct")if(t.lower()=="c")else print("3.wrong")
    print("4.correct")if(fo.lower()=="c")else print("4.wrong")
    print("5.correct")if(fi.lower()=="a")else print("5.wrong")
    print("\n\n")
    if(f.lower()=="b"):
        qi=1
    else:
        qi=0
    if(s.lower()=="b"):
        qe=1
    else:
        qe=0
    if(t.lower()=="c"):
        qr=1
    else:
        qr=0
    if(fo.lower()=="c"):
        qt=1
    else:
        qt=0
    if(fi.lower()=="a"):
        qy=1
    else:
        qy=0
    total=qi+qe+qr+qt+qy
    print("\t\t TOTAL MARKS  :  ",total)
    print("**********************************************************")
    ans=input("If you need answer y/n ? : ")
    if(ans.lower()=="y"):
        print("1.b.interpreter\n2.b.India\n3.c.(a+b)**2-2ab\n4.c.Both a and b\n5.a.Albert einstein")
    else:
        print("ALL THE BEST.............")
    
           