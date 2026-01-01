# Smart Health Monitoring App - Health Risk Prediction
# Branch: modify-loop

num_users = int(input("Enter number of users: "))

for i in range(1, num_users + 1):  
    blood_sugar = int(input(f"Enter blood sugar level for user {i}: "))
    
    if blood_sugar > 140:
        print(f"User {i}: High risk of diabetes")
    else:
        print(f"User {i}: Normal health condition")
