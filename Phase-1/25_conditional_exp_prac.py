# marks1 = int(input("Enter Marks 1:"))
# marks2 = int(input("Enter Marks 2:"))
# marks3 = int(input("Enter Marks 3:"))

# total_percentage = ((marks1+marks2+marks3)*100)/300

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("You are passed:", total_percentage)
# else:
#     print("You are failed", total_percentage)


# in keyword to check 
p1 = "haha"
p2 = "babe"
p3 = "meow"
p4 = "baby"
p5 = "buy now"

message = input("Enter your message:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message) or (p5 in message)):
    print("This comment is a spam")
else:
    print("This comment is not a spam")