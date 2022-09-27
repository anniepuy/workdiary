from database import create_table, add_entry, get_entries


menu = """Please select one of the following options:
1) Add new entry for today
2) View entries
3) Exit

Your selection:"""
welcome = "Welcome to your daily work diary!"

def prompt_new_entry():
    entry_content = input("What did you do today?")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)

def prompt_get_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


entries = [
    {"content": "Client meeting today, discusses infastructure needs.", "date": "02-02-2022"},
    {"content": "Updated product roadmap to reflect new application.", "date": "02-12-2022"},
    {"content": "Created training documentation for all team members, initialized the first training session.", "date": "02-13-2022"},
    {"content": "Completed monthly report.", "date": "02-14-2022"}
]

print(welcome)
create_table()

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        prompt_get_entries(get_entries())        
    else:
        print('Invalid option. Please try again.')
