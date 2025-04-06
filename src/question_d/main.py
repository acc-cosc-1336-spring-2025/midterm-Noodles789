def get_assessment_value(value):
    return value * 0.60

def get_tax_assessed(assessment_value):
    return (assessment_value / 100) * 0.72

while True:
    try:
        Land = float(input("Enter value of property(or 0 to quit): "))
        if Land == 0:
            break
        assessment = get_assessment_value(Land)
        tax_assessed = get_tax_assessed(assessment)
        print(f"Assessment value: {assessment}, Property tax: {tax_assessed}")
    except ValueError:
        print("Error: Enter a valid number.")