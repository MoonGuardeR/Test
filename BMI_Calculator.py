weight = input('Please enter your weight (kg)')
weight = float(weight)
height = input('Please enter your heigh (m)')
height = float(height)
bmi = weight/height/height
idea_weight = 24*height*height
slightly_fat_weight = 27*height*height

if bmi<18.5:
    print('Too light!')
elif bmi >= 18.5 and bmi < 24:
    print('Normal')
elif bmi >= 24 and bmi < 27:
    print('Slightly fat')
elif bmi >= 27 and bmi < 30:
    print('Mid fat')
elif bmi >= 35:
    print('Too fat')
else:
    print('Error')

print('Idea weight for you is',idea_weight,'kg')
print('Slightly fat of weight for you is',slightly_fat_weight,'kg')