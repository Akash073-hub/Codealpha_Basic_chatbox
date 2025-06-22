def Basic_chatbox():
    while True:
        user_input = input("Enter the questions: ").lower()
        if(user_input == "hello"):
            print ("hi")
        elif(user_input == "how are you?"):
            print( "I am fine, thank you!")
        elif(user_input == "bye"):
            print ("Goodbye!")
            break
        else:
            print("I don't understand your question. Please try again.")
            Basic_chatbox()

Basic_chatbox()
