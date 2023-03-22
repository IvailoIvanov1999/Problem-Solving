data_inputing = input()
companies_d = {}
while data_inputing != "End":
    company_name, employees_id = data_inputing.split(" -> ")
    key = company_name
    value = employees_id
    if key not in companies_d:
        companies_d[key] = [value]
    else:
        if value not in companies_d[key]:
            companies_d[key] += [value]

    data_inputing = input()

for c_n, e_id in companies_d.items():
    print(f"{c_n}")
    for el in e_id:
        print(f"-- {el}")
