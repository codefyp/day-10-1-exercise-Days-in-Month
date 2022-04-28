#function to find if its a leap year
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True  
  else:
    return False
#function to display the days of the month
def days_in_month(year, month):
  #check if input is valid  
  if month > 12 or  month < 1:
      return "invalid month"
  #list with the days each month    
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  #if it's a february then it has 29 days  
  if is_leap(year) and month == 2:
      return 29
  #return the correct number from the list    
  return month_days[month -1]    

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
