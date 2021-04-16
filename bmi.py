def calculate_bmi(feet_height = ' ', inch_height = ' ', weight = ' '):
    #take user information
    if ((feet_height == ' ') or (inch_height == ' ') or (weight == ' ')):
        try:
            feet_height = int(input('Enter height in feet (Ex: 5): '))
            inch_height = int(input('Enter remaining inches of height (Ex: 11): '))
            weight = int(input('Enter weight in pounds: '))

            #convert weight to kilograms
            weight = float(weight) * .45
            height = (feet_height * 12) + inch_height
            
            #perform metric conversion on height
            height = height * .025
            
            #square the answer
            height = (height**2)

            #caluclate bmi to one decimal place
            answer = weight / height
            answer = round(answer, 1)
            print('BMI: ', answer)

            #find category of bmi
            if (answer < 18.5):
                category = 'Underweight'
            elif ((answer >= 18.5) and (answer <= 24.9)):
                category = 'Normal weight'
            elif ((answer >= 25) and (answer <= 29.9)):
                category = 'Overweight'
            else:
                category = 'Obese'
            print('BMI category: ', category)
            return [answer, category]
        
        except ValueError:
            print('Invalid input. Please enter an integer greater than 0.')
            calculate_bmi()
    else:
        try:
            feet_height = int(feet_height)
            inch_height = int(inch_height)
            weight = int(weight)

            #convert weight to kilograms
            weight = float(weight) * .45
            height = (feet_height * 12) + inch_height
            
            #perform metric conversion on height
            height = height * .025
            
            #square the answer
            height = (height**2)

            #caluclate bmi to one decimal place
            answer = weight / height
            answer = round(answer, 1)
            print('BMI: ', answer)

            #find category of bmi
            if (answer < 18.5):
                category = 'Underweight'
            elif ((answer >= 18.5) and (answer <= 24.9)):
                category = 'Normal weight'
            elif ((answer >= 25) and (answer <= 29.9)):
                category = 'Overweight'
            else:
                category = 'Obese'
            print('BMI category: ', category)
            return [answer, category]

        except ValueError:
            print('Invalid input. Please enter an integer greater than 0.')
            calculate_bmi()
    



