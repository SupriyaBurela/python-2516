student_name=input("enter studentent name:")
grade_level=int(input("enter the student grade level:"))
tution_fee=int(input("enter the tution fee:"))
#discount_percentage=float(input("enter the discount percentage:"))
academic_topper_status=input("enter whether the student is academic topper or not?(yes/no)")
if grade_level>=1 and grade_level<=12:
    print("the grade is valid")    
else:
    print("the grade is invalid")
    discount=0    
if grade_level>=9 and grade_level<=12:
    if academic_topper_status=="yes":
        discount=20
    else:
        discount=10
elif grade_level>=6 and grade_level<=8:
    discount=5
else:
    print("no discount") 
if grade_level==10:
    discount=23
elif grade_level==12:
    discount=25  
else:
    print("no discount")
calculate_discount_amount=(tution_fee*discount)/100
final_fee=tution_fee-calculate_discount_amount
print(f"student name:{student_name}")
print(f"grade level:{grade_level}")
print(f"academic topper status (yes/no):{academic_topper_status}")
print(f"tution fee:{tution_fee}")
print(f"dicount percentage:{discount}")  
print(f"amount saved:{calculate_discount_amount}")  
print(f"final fee after discount{final_fee}")                    
        