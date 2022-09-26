from database import add_entry, view_entries


menu = """Please select one of the following options:
1) Add new entry for today
2) View entries
3) Exit

Your selection:"""
welcome = "Welcome to your daily work diary!"

entries = [
    {"content": "Client meeting today, discusses infastructure needs.", "date": "02-02-2022"},
    {"content": "Updated product roadmap to reflect new application.", "date": "02-12-2022"},
    {"content": "Created training documentation for all team members, initialized the first training session.", "date": "02-13-2022"},
    {"content": "Completed monthly report.", "date": "02-14-2022"}
]

print(welcome)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        print('Adding..')
    elif user_input == "2":
        print("viewing")
    else:
        print('Invalid option. Please try again.')
