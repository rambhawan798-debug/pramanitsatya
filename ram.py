# yeh hamari main integration file hai: main_app.py

import ai_logic



def main():

    print("Pramanit Satya AI system start ho raha hai...")

    user_boli = "hello"

    print("User ne input diya:", user_boli)


    
    # ai_logic file se response mangwa rahe hain

    resp = ai_logic.generate_response(user_boli)
    print("AI ka jawab aaya:", resp)



if __name__ == "__main__":

    main()