current_users = ['Alice', 'Bob', 'Charlie', 'admin', 'John']
new_users = ['Jaden', 'Bob', 'Mike', 'Alice', 'Sarah']

lowercase_current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in lowercase_current_users:
        print(f"Sorry, {new_user} is not available. Please choose a different username.")
    else:
        print(f"The username {new_user} is available.")
