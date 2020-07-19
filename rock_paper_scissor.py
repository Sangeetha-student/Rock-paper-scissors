import sys
user1=input("Whats your name?")
user2=input("And yours?")
user1_answer("%s, Select Rock Paper Scissor?: ",% user1)
user2_answer("%s, Select Rock Paper Scissor?: ",% user2)
def compare(u1,u2):
    if (u1==u2):
        return("It's a tie!")
    elif u1=='rock':
        if u2=='scissor':
            print(user1," wins!")
        else:
            print(user2,"wins!")
    elif u1=='paper':
        if u2=='scissor':
            print(user2," wins!")
        else:
            print(user1,"wins!")
    elif u1=='scissor':
        if u2=='rock':
            print(user2," wins!")
        else:
            print(user1,"wins!")
    else:
        print("Invalid input try again!!!")
        sys.exit()
    print(compare(user1_answer,user2_answer))
        
    
