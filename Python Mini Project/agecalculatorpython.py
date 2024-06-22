"""Age Calculator is an amazing application to create as a beginner in any programming language. To create an age calculator, you need two dates:

today date
date of birth"""

def shreyasagecal(year, month, day):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(year, month, day)
    
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        months -= 1
        days += (dob.replace(month=dob.month + 1, day=1) - dob).days
    
    if months < 0:
        years -= 1
        months += 12

    print(f"You are {years} years, {months} months, and {days} days old.")

year = int(input("Enter your birth year (e.g., 1987): "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day (1-31): "))

shreyasagecal(year, month, day)
