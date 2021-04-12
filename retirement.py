def calculate_retirement(user_age = ' ', annual_salary = ' ', percent_saved = ' ', retirement_goal = ' '):

    #take user information
    if ((user_age == ' ') or (annual_salary == ' ') or (percent_saved == ' ') or (retirement_goal == ' ')):
        try:
            user_age = int(input("Enter your current age (Ex: 25): "))
            annual_salary = int(input("Enter your annual salary rounded to the nearest dollar (70000): "))
            percent_saved = float(input("Enter the percentage you plan to save (Ex: 10.5): "))
            retirement_goal = int(input("Enter your retirement goal to the nearest dollar (Ex: 500000): "))

            #calculate yearly savings
            savings = annual_salary * (percent_saved / 100)
            e_savings = savings * .35
            yearly_savings = savings + e_savings

            #calculate age to reach goal
            total_savings = 0
            goal_met = False
            
            while (total_savings < retirement_goal):
                user_age += 1
                total_savings += yearly_savings
            
            if (user_age >= 100):
                print("Goal not met before death at age 100. Goal of", retirement_goal, "dollars would be met at age", user_age)
            else:
                print("Retirement savings goal of", retirement_goal, "dollars met at age", user_age)
                goal_met = True
            
            return [user_age, goal_met]
        
        except ValueError:
            print("Invalid data type input.")
            print()
            calculate_retirement()
    else:
        try:
            user_age = int(user_age)
            annual_salary = int(annual_salary)
            percent_saved = float(percent_saved)
            retirement_goal = int(retirement_goal)

            #calculate yearly savings
            savings = annual_salary * (percent_saved / 100)
            e_savings = savings * .35
            yearly_savings = savings + e_savings

            #calculate age to reach goal
            total_savings = 0
            goal_met = False
            
            while (total_savings < retirement_goal):
                user_age += 1
                total_savings += yearly_savings
            
            if (user_age >= 100):
                print("Goal not met before death at age 100. Goal of", retirement_goal, "dollars would be met at age", user_age)
            else:
                print("Retirement savings goal of", retirement_goal, "dollars met at age", user_age)
                goal_met = True
            
            return [user_age, goal_met]
        except ValueError:
            print("Invalid data type input.")
            print()
            calculate_retirement()

   

