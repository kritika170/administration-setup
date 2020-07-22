import csv

def w(info_list):
    csv_file=open("student_info","a")
    writer=csv.writer(csv_file)

    if csv_file.tell()==0:
        writer.writerow(["name","roll.no"])
        writer.writerow(info_list)

if __name__=="__main__":
    
    condition=True
    num=1
    while condition:
        student_info=input("Enter some student information #{}: ".format(num))
        print(student_info,type(student_info))
        student_list=student_info.split(" ")
        print(student_list)
        print("\nThe entered info is: \nName: {}\nRoll.no: {}\n".format(student_list[0],student_list[1]))
        choice=input("Is the entered info correct:yes/no")
        if choice=="yes":
              
            w(student_list)
              


            condition_check=input("enter yes/no: ")

            if condition_check=="yes":
                condition=True
                num+=1
            elif condition_check=="no":
                condition=False
        elif choice=="no":
            print("\nPlease re-enter the values: ")
