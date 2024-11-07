numberOfDays = int(input("Enter the number of days: "))

# Calculate the seconds of a year

Seconds = numberOfDays * 24 * 60 * 60
if numberOfDays == 365:
  print("There are", Seconds, "seconds in a year.")
else:
  print("There are", Seconds, "seconds in a leap year.")
