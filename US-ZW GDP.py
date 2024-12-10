USA_GDP = 3000
Zimbabwe_GDP = 2

USA_GDP_growth = 0.025
Zimbabwe_GDP_growth = 0.05

year = 2000

while USA_GDP > Zimbabwe_GDP:
    USA_GDP = (USA_GDP * (1 + USA_GDP_growth))
    Zimbabwe_GDP = (Zimbabwe_GDP * (1 + Zimbabwe_GDP_growth))
    year = year + 1
    print("США: " + str(int(USA_GDP)))
    print("Зимбабве: " + str(int(Zimbabwe_GDP)))
    print("Год: " + str(year))
