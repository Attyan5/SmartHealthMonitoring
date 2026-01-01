# Smart Health Monitoring App - Health Risk Prediction

num_users = int(input("Enter number of users: "))
for i in range(num_users):
    blood_sugar = int(input(f"Enter blood sugar level for user {i+1}: "))
    if blood_sugar > 140:
        print("High risk of diabetes")
    else:
        print("Normal health condition")
