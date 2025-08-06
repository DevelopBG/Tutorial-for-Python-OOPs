class Chatbook:

    #static vaiable
    __user_id = 0 

    def __init__(self):
        self.id = Chatbook.__user_id # static id cannot be accessed by self, only by class itself. 
        Chatbook.__user_id += 1
        self.__name= "default name"
        self.username = ''
        self.password =''
        self.loggedin = False
        # self.menu()

    def get_name(self): # getter method
        return self.__name
    def set_name(self, value):# setter method
        self.__name = value
        return self.__name
    
    @staticmethod
    def get_id():
        return Chatbook.__user_id
    @staticmethod
    def set_id(val):
        Chatbook.__user_id = val
        return Chatbook.__user_id

    def menu(self):
        user_input = input("""Welcome to chatbook!how would you like to proceed?
            1. Press 1 for singup
            2. Press 2 to singin
            3. Press 3 to write a post
            4. Press 4 to message to frind
            5. Press 5 to exit. 
            User:""")
        
        if user_input.lower() == "1":
            self.signup()
        elif user_input.lower() == "2":
            self.singin()
        elif user_input.lower() == "3":
            self.user_post()
        elif user_input.lower() == "4":
            self.sendmessage()
        else:
            exit()

    def signup(self):
        email = input("enter your email:")
        passwrd = input("enter your password:")
        self.username = email
        self.password = passwrd
        print("You have signed up successfully\n")
        self.menu()
    
    def singin(self):
        if self.username=="" and self.password=="":
            print("Please sing up first")
        else:
            usrname = input("enter your email:")
            pwd = input("enter your password:")
            if self.username == usrname and self.password == pwd:
                print("you have singed in successfully")
                self.loggedin = True
            else:
                print("Please input correct credentials")
        
        print("\n")
        self.menu()

    def user_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here:")
            print(f'Your post has been done- {txt}')
        else:
            print("To post, you need to signin first.")
            self.menu()

    def sendmessage(self):
        if self.loggedin == True:
            txt = input("Enter your message:")
            friend =  input("Who to send this message:")
            print(f'Message has been sent to {friend}')
        else:
            print("To post, you need to signin first.")
            self.menu()




if __name__ == "__main__":

    user1 = Chatbook()
    print(user1.id)
    # print(user1._Chatbook__name)

    # user2= Chatbook()
    # print(user2.id)
    # user3= Chatbook()
    # print(user3.id)

    # static method is directly accessed from the class directly.
    Chatbook.set_id(10)
    user2 = Chatbook()
    print(user2.id)