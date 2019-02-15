"""This uses 2 modules- timeit and random. The name of a food item is generated, and the user needs to guess it. """
from timeit import default_timer
import random
d=["shawarma", "biriyani", "burger", "donut", "lasagne","spaghetti", "steak", "sushi", "quiche", "croissant", "parfait", "cupcakes", "kebab", "omelette", "noodles", "turkey","cheesecake", "risotto","sambhar", "waffle", "pancake"]
name=input("Enter your name")

def start():
    print("Welcome to Hangman, ARE YOU READY")
    print("A.Yes, OFC I am :D\nB.LOLNO!")
    user_choice_1 = input("Enter your choice :))")
		
    if user_choice_1 == 'A' or user_choice_1 == 'a':
	    print ("WOE BRACE YOURSELF")
	    maingame()
	    
    elif user_choice_1 =='B' or user_choice_1 == 'b' :
	    print ("Thank you")
	    exit()
    else:
	    print ("Enter a valid option")
	    start ()

def graphic(guess):
   
        
        if guess == 1:
                      print("""                                  ________      
                                    |  |      
                                    |  0      
                                    |             
                                    |             
                                    |             """, "You have 5 wrong guesses left")
        elif guess == 2:
                      print("""                                 ________      
                                    |  |      
                                    |  0      
                                    | /       
                                    |             
                                    |             """, "You have 4 wrong guesses left")
        elif guess == 3:
                      print("""                                 ________      
                                    |  |      
                                    |  0      
                                    | /|      
                                    |             
                                    |             """, "You have 3 wrong guesses left")
        elif guess == 4:
                      print("""                                 ________      
                                    |  |      
                                    |  0      
                                    | /|\     
                                    |             
                                    |             """, "You have 2 wrong guesses left")
        elif guess == 5:
                      print("""                                 ________      
                                    |  |      
                                    |  0      
                                    | /|\     
                                    | /       
                                    |             """, "You have 1 wrong guess left")
        else:
                      print("""                                 ________      
                                    |  |      
                                    |  0      
                                    | /|\     
                                    | / \     
                                    |             """)
                      print("0 turns left.Better luck next time! :)")
                      print("The right word is ", mainword)
                      print("GAME OVER!")
                      print()
                      print()
                      print("_____________________________________________________________________________________")
                      start()
def clues():
        f=input("Would you like a hint?(y/n)")
        if f=="y":               
                if mainword==d[3]:    
                    print("Its a sweet dish, usually eaten as dessert. Comes in many different flavours")
                elif mainword==d[10]:
                    print("It is a sweet dish.")
                elif mainword==d[11]:
                    print("They're just like cakes")
                elif mainword==d[16]:
                    print("It is a type of cake")
                elif mainword==d[19]:
                    print("They're are eaten throughout the world, particularly in Belgium, France")
                elif mainword==d[1] or mainword==d[17]:
                    print("It is a rice dish.")
                elif mainword==d[18]:
                    print("It is primarily eaten by Indians, it is a curry")
                elif mainword==d[20]: 
                    print("It is usually eaten for breakfast. It is made out of eggs and flour and usually eaten with something sweet.")
                elif mainword==d[13]:
                    print("It is usually eaten with bread.")
                elif mainword==d[4] or mainword==d[5]:
                    print("It is a part of the French cuisine")
                elif mainword==d[6] or mainword==d[12] or mainword==d[15]:
                    print("It is a non-vegetarian dish")
                elif  mainword==d[7]:
                    print("This dish is primarily eaten by the people of the South Asian countries")
                elif mainword==d[9]:
                    print("It is a form of bread")
                elif mainword==d[8]:
                    print("It is sort of like a stuffed tart")
                elif mainword==d[0]:
                    print("It is a part of the lebanese cuisine")
                elif mainword==d[2] or mainword==d[14]:
                    print("Almost all the fast food chains sell this")
        elif f=="n":
                   print("Great!Keep Going!")
        else:
                   print("Enter valid option")
                   clues()
def maingame():         
    s=random.randint(0,20)
    global mainword 
    mainword="uhh"
    sym=[]
    l=len(mainword)
    for i in range (l):
        sym.append("?")
    print("""
             ________      
             |      |      
             |             
             |             
             |             
             |             """, "You have 6 turns left")

    
    print()
    
    first= default_timer()
    print("The word is")
    for i in sym:
            print(i,end=" ")
    print()
    global guess        
    global guessed #wrong guesses 
    guessed=""
    global correctguessed
    correctguessed=""
    guess=0
    while 2:                
        n=input("Enter a letter you think is present in the word")
        if n in mainword and n not in correctguessed:
            print() 
            print("Yes that's right, that letter is in the word")
            print()
            correctguessed=correctguessed+n + ","
            print("The right guesses:", correctguessed)
            print("The incorrect guesses are:",guessed)
            for i in range(0,len(mainword)):
                if n==mainword[i]:
                    sym[i]=n
            for j in sym:
                print (j, end=" ")
            print()
        elif n not in mainword and n not in guessed:
         if guess<=6:                                
            guess+=1
            print() 
            print("Uh-oh, try again")
            print()
            for j in sym:
              print(j, end=" ")		
            print() 
            guessed=guessed+n+ ","
            print("The right guesses are:", correctguessed)
            print("The incorrect guesses are:",guessed)
            print()
            graphic(guess)
            print("________________________________________________________________________________")
            if guess==2:
               clues()
        else:
            print("You have already guessed this word")
            continue                          
        if "?" not in sym:
                print()     
                print("Congratulations! You've got the word. :)")
                duration=round(default_timer()-first,2)
                duration=str(duration)
                print("Time taken is ", duration, "seconds")
                print("SCORES")
                print("NAME"+"       " "SCORE")
                f=open("score.txt", "a")                
                f.write(name+ "       "+ duration + "\n")
                f.close()
                f=open("score.txt", "r")
                print(f.read())                
                n=input("Would you like another try?(y/n)")
                print() 
                if n=="y":
                       maingame()
                else:
                    print("Thank you for playing. :)")
                    exit()
start()      
