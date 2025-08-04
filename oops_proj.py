class Chatbook:
    def __init__(self):
        self.username = ''
        self.password =''
        self.loggedin = False
        self.menu()
    def menu(self):
        user_input = input("""Welcome to chatbook!how would you like to proceed?
            1. Press 1 for singup
            2. Press 2 to singin
            3. Press 3 to write a post
            4. Press 4 to message to frind
            5. Press 5 to exit. 
            User:""")
        
        if user_input.lower() == "1":
            pass
        elif user_input.lower() == "2":
            pass
        elif user_input.lower() == "3":
            pass
        elif user_input.lower() == "4":
            pass
        else:
            exit()

obj = Chatbook()