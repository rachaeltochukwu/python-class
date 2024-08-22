def get_user_response(questions: str) -> bool:
    while True:
        response = input(questions + '[y/n]').strip().lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print('please enter y for yes and n for no')

def zombie_identifier() :
    questions = [
        "does the subject have a glazed look?  "
        "is the subject moaning?  ",
        "is the subject missing any limbs?  ",
        "does the subject have pale or gray skin?  ",
        "is the subject on fire without showing pain?  ",
        "does the subject show little response to objects in its paths?  "
        "is the subject limping?  "
        "is the subject wearing a jacket with shoulder pads? "
        "does the subject crave brain and its not the first full week of october? "
    ]
    count_yes = 0
    for question in questions :
        if get_user_response(question) :
            if get_user_response(question) :
                count_yes += 1
        percentage_yes = (count_yes * 100) / len(questions)
        print(f"percentage of yes : {percentage_yes : 2f}%")
        if percentage_yes >= 50 :
            print("TARGET IS LIKELY A ZOMBIE")
        else :
            print("TARGET IS LIKELY AN ALLY")

def main() :
    while True :
        zombie_identifier()
        repeat = input("DO YOU WISH TO IDENTIFY ANOTHER TARGET [Y/N]")
        if repeat != 'y' :
            break

main()




