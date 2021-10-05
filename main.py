from datetime import datetime
from application import salary
from application.db import people
def main():
    print(datetime.now().date())
    salary.calculate_salary()
    people.get_employees()
if __name__ == '__main__':
    main()
