print("Welcome to Love calculator".center(70,"."))
name1=input("What is your first and last name : ")
name2=input("What is their first and last name : ")

up_name1=name1.lower()
up_name2=name2.lower()
combined_name=up_name1+up_name2

T=combined_name.count("t")
R=combined_name.count("r")
U=combined_name.count("u")
E=combined_name.count("e")

L=combined_name.count("l")
O=combined_name.count("o")
V=combined_name.count("v")

ones=str(L+O+V+E)
tens=str(T+R+U+E)
score=tens+ones
print(f"Love percentage is {score} % ")