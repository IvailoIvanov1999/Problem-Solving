number_opened_tabs = int(input())

salary = float(input())

salary_after_a_fine=salary

for i in range(number_opened_tabs):
    type_of_website = input()

    if type_of_website == "Facebook":
        salary_after_a_fine = salary_after_a_fine - 150

    elif type_of_website == "Instagram":
        salary_after_a_fine = salary_after_a_fine - 100


    elif type_of_website == "Reddit":
        salary_after_a_fine = salary_after_a_fine - 50


final_salary=salary_after_a_fine


if final_salary <= 0:
    print("You have lost your salary.")
    exit()

else:
    print(f'{int(final_salary)}')



