function CalculateBMI(){
  var height_ft = document.getElementById("height_ft").value;
  var height_in = document.getElementById("height_in").value;
  var weight = document.getElementById("weight").value;
  var category = "?";

  //convert weight to kilograms
  weight = weight * .45;
  var height = (height_ft * 12);
  height = parseInt(height) + parseInt(height_in);
  //perform metric conversion on height
  height = height * .025;

  //square the answer
  height = (height**2);

  //caluclate bmi to one decimal place
  answer = weight / height;
  answer = Math.round(answer * 10) / 10;

  //find category of bmi
  if (answer < 18.5){
      category = "Underweight";
  }
  else if ((answer >= 18.5) && (answer <= 24.9)){
      category = "Normal weight";
  }
  else if ((answer >= 25) && (answer <= 29.9)){
      category = "Overweight";
  }
  else{
      category = "Obese";
  }

  document.getElementById("bmi").innerHTML = answer;
  document.getElementById("bmi_category").innerHTML = category;
}

function CalculateRetirement(){
  var age = document.getElementById("age").value;
  var salary = document.getElementById("salary").value;
  var saved = document.getElementById("saved").value;
  var goal = document.getElementById("goal").value;

  //calculate yearly savings
  var savings = parseFloat(salary) * (parseFloat(saved) / 100);
  var e_savings = savings * .35;
  var yearly_savings = parseFloat(savings) + parseFloat(e_savings);

  //calculate age to reach goal
  var total_savings = 0;

  while (total_savings < goal){
      age = parseFloat(age) + parseFloat(1);
      total_savings = parseFloat(total_savings) + parseFloat(yearly_savings);
  }
  if (age >= 100){
      //print("Goal not met before death at age 100. Goal of", retirement_goal, "dollars would be met at age", user_age)
      document.getElementById("goal_met").innerHTML = "not be met";
      document.getElementById("by_age").innerHTML = "by the age";
      document.getElementById("retirement_goal").innerHTML = goal;
      document.getElementById("retirement_age").innerHTML = 100;
  }
  else{
      //print("Retirement savings goal of", retirement_goal, "dollars met at age", user_age)
      document.getElementById("goal_met").innerHTML = "be met";
      document.getElementById("by_age").innerHTML = "at the age";
      document.getElementById("retirement_goal").innerHTML = goal;
      document.getElementById("retirement_age").innerHTML = age;
  }
}
