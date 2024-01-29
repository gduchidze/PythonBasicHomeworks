# import random

# player = 0
# computer = 0
# rounds = 3

# while player < rounds and computer < rounds:
#     user_choice = input("შეიყვანე ქვა ქაღალდი ან მაკრატელი: ")
#     choices = ['ქვა', 'ქაღალდი', 'მაკრატელი']
#     computer_choice = random.choice(choices)

#     print(f"კომპიუტერმა არიჩია {computer_choice}")

#     if user_choice == computer_choice:
#         print("ფრეა ")
#     elif (
#     (user_choice == 'ქვა' and computer_choice == 'მაკრატელი') or
#     (user_choice == 'მაკრატელი' and computer_choice == 'ქაღალდი') or
#     (user_choice == 'ქაღალდი' and computer_choice == 'ქვა')
#     ):
#         print('მოთამაშემ რაუნდი მოიგო')
#         player += 1
#     else:
#         print("კომპიუტერმა მოიგო რაუნდი")
#         computer += 1
    
#     print(f"შენი ქულა {player} და კომპიუტერის ქულა {computer}")

#     if player == rounds:
#         print("მოთამაშემ მოიგო")
#     else:
#         print("კომპიუტერმა მოიგო")




#2

# number = int(input("Enter an integer: "))

# for i in range(1, 11):
#     for j in range(1, 6):
#         print(f"{j} x {i} = {j * i}\t", end="")
    
#     print()




#4

# while True:
#     user = input("Say something: ")

#     if user.lower() == "quit":
#         print("Parrot says: Goodbye!")
#         break
#     elif user.lower() == "hello":
#         print("User Said Whaaat!?")
#     else:
#         print(f"You said '{user}'")



#3

# balance = 3000
# spending = 100

# while True:
#     try:
#         cost = float(input("შეიყვანე ღირებულება : "))
        
#         if cost == 0:
#             break

#         if cost <= balance:
#             balance -= cost
#             print(f"{cost} GEL. ბალანსი: {balance} GEL")
#             if balance < spending:
#                 print("მიღწეულია ხარჯვის დონე.")
#                 break
#         else:
#             print("არ არის საკმარისი თანხა.")

#     except ValueError:
#         print("შეიყვანე დასაშვები თანხა.")








