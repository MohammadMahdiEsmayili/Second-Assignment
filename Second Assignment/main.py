users_name = []

number_of_users = input('Enter users count:')

for x in range(int(number_of_users)):
      name_of_users = input('Enter user name:')
      age_of_users = input('Enter user age:')
      user = {'name': name_of_users, 'age': age_of_users}
      users_name.append(user)

search_name = input("Enter name to search: ")
found=False # variable for detecting user
for users in users_name:
    if search_name == users['name']:
        found=True
        print(users['age'])
        break
if found=False: # if cannot find user with given name
      print("There is no user with given name!")
