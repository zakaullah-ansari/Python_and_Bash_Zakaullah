# 1. Grade Checker


"""
Take a score as input and print the grade based on the following:

1. 90+ : “A”
2. 80–89 : “B”
3. 70–79 : “C”
4. 60–69 : “D”
5. Below 60 : “F”
6. Use a basic if / else statement to determine the grade.Here is a simple Python code that takes a score as input and prints the corresponding grade based on the specified criteria:

"""

def check_grade(score):
    
    """Takes a score and returns the corresponding letter grade."""

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Get user input
score = float(input("Enter the score: "))
print(check_grade(score))