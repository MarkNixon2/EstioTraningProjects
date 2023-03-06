DavidAttenborough = {
    "Age": 96,
    "Birth_date": "8-May-1926",
    "Birth_Place": "Isleworth",
    "FirstName": "David",
    "LastName": "Attenborough",
}

x = DavidAttenborough["Birth_date"]
print(x)

y = DavidAttenborough["Age"] = 97
print(y)

z = DavidAttenborough["Middle_Name"] = "Frederick"
print(DavidAttenborough)

w = DavidAttenborough.pop("Birth_date")
print(DavidAttenborough)

