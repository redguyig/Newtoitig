def Menu_Driven_Program():
    print("MAIN MENU")
    print("Select any one from the following tasks to be performed:")
    print("1.Write Contents to the file")              
    print("2.Reading all the Contents from file")              
    print("3.Copy data to another file")              
    print("4.Delete records of product whose quantity is less than 5")
    print("5.Exit")
    a=int(input("Enter your choice:"))
    def Write_Contents():
        f1=open("Product.txt","w")
        N=int(input("Enter the number of records:"))
        for i in range (N):
            Product_Name=input("Enter the product name here:")
            Product_ID=input("Enter the ID here:")
            Quantity=input("Enter the quantity of product here:")
            Cost_per_product=input("Enter the cost of product here:")
            Total_cost=input("Enter the total cost here:")
            data=Product_Name + "\t" +  Product_ID + "\t" + Quantity + "\t" + Cost_per_product +"\t" + Total_cost + "\n"
            f1.write(data)
        print("Data has been succesfully written in the file")         
        f1.close()
    def Reading_all_contents():
        f2=open("Product.txt","r")
        S=f2.read()
        print(str(S))
        f2.close()
    def Copy_Data():
        f3=open("Product.txt","r")
        s=f3.readline()
        while s!="":
            l=s.split()
            if int(l[4])>=50000 and int(l[4])<=70000:
                f4=open("ExclusiveProduct.txt","w")
                f4.write(s)
            l=[]
            s=f3.readline()
        f3.close()
    def Delete_Data():
        import os
        f3=open("Product.txt","r")
        f5=open("File.txt","w")
        s=f3.readline()
        while s!="":
            l=s.split()
            if int(l[2])>5:
                
                f5.write(s)
            l=[]
            s=f3.readline()
        f3.close()
        f5.close()
        os.remove("Product.txt")
        os.rename("File.txt","Product.txt")
        print("Records of products deleted successfully")
    def Exit():
        quit()
    if a==1:
        Write_Contents()
    if a==2:
        Reading_all_contents()
    if a==3:
        Copy_Data()
    if a==4:
        Delete_Data()
    if a==5:
        Exit()
Menu_Driven_Program()
