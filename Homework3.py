name_surname=input("Please write your name and surname\n")
midterm=input("Please enter your midterm grade\n")
final=input("Please enter your final grade\n")
attendance=input("Please enter your missing lecture hours\n 20h(max. lecture hours)\n")
grade=(int(midterm)*0.3)+(int(final)*0.5)+(((20-int(attendance))*5)*0.20)
print("Your avarage grade\n", grade)
new_file =open("studentgradecalculation.txt","w")
print("Your name and surname","\n",name_surname,"\n","Your midterm grade","\n",midterm,"\n","Your final grade","\n",final,"\n","Number of missing lectures (Out of 20h)","\n",attendance,"\n","Your average grade\n",grade,sep="",file=new_file)
new_file.close()

                 
