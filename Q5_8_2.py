data = [
        ['01', '0001', 'Male', 'Yamada', 'Tarou', 25, 'Tokyo'],
        ['01', '0002', 'Male', 'Satou', 'Takeshi', 27, 'Kanagawa'],
        ['01', '0003', 'Female', 'Tanaka', 'Yuka', 25, 'Saitama'],
        ['02', '0001', 'Male', 'Smith', 'Mike', 22, 'NewJersey'],
        ['02', '0002', 'Male', 'Turner', 'Tom', 27, 'Kansas'],
        ['02', '0003', 'Male', 'Jackson', 'David', 25, 'Florida']
        ]

members_dict = {}
for kioku in data:
    kuni = kioku[0]
    number = kioku[1]
    key = (kuni, number)
    value = kioku[2:]
    members_dict[key] = value
for key, value in members_dict.items():
    print(f"キー: {key}, 値: {value}")
