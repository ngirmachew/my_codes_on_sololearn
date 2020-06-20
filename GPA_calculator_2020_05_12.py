grade_scale = {'A': 4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3, 'C':2.0, 'C-':1.7, 'D':1.3, 'D-':0.7,'F':0}
print(f'This program computes your GPA \nPlease enter your completed courses \nTerminate your entry by entering 0 credits')
allcredit = []
allgrades = []

while True:
    credit = int(input('Credits?:' ))
    if credit == 0:
        break
    grade = input('Grade?: ')
    prod_grade_credit = grade_scale[grade.upper()] * credit
    allgrades.append(prod_grade_credit)
    allcredit.append(credit)
    #credit = int(input('Credits?: ')
if sum(allcredit) == 0:
    print("Unable to calculate GPA for 0 credit"
else:
    print(f'Your GPA is: {(sum(allgrades) / sum(allcredit)):.2f}')
