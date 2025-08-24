import logging

file_handler = logging.FileHandler("Quiz_Game.log")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(name)s - %(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

console_log = logging.StreamHandler()
console_log.setLevel(logging.DEBUG)
console_log.setFormatter(formatter)

logger = logging.getLogger("Quiz_01")
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_log)

try:
    print("******-Welcome to my Quiz Game-*****")

    Question_Bank = [
    {
        "Text": "The ability of one class to acquire methods and attributes of another class is called _ _ _ _ _",
        "Answer": "A",
        "Explanation": "Inheritance is the mechanism in OOP where one class (child) can acquire properties and methods from another class (parent)."
    },
    {
        "Text": "Which of the following is a type of inheritance?",
        "Answer": "D",
        "Explanation": "Python supports Single, Multiple, Multilevel, Hierarchical, and Hybrid inheritance."
    },
    {
        "Text": "Which type of inheritance has multiple subclasses to a single super class?",
        "Answer": "C",
        "Explanation": "Hierarchical inheritance occurs when multiple subclasses inherit from a single superclass."
    },
    {
        "Text": "Which is the depth of multilevel inheritance in Python?",
        "Answer": "C",
        "Explanation": "Python allows unlimited levels of multilevel inheritance."
    },
    {
        "Text": "What does MRO stands for_ _ _ _",
        "Answer": "B",
        "Explanation": "MRO stands for Method Resolution Order, which is the order in which Python looks for a method in a hierarchy of classes."
    }
]
    Options = [
        ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Object"],
        ["A. Single", "B. Double", "C. Triple", "D. Multiple"],
        ["A. Single", "B. Multilevel", "C. Hierarchical", "D. Hybrid"],
        ["A. 5", "B. 7", "C. Unlimited", "D. 10"],
        ["A. Method Recursion Order", "B. Method Resolution Order", "C. Main Resolution Object", "D. Multiple Recursion Object"]
    ]
    Score = 0
    def Check_Answer(User_Guess,Correct_Answer):
        if User_Guess == Correct_Answer:
            return True
        else:
            return False
    for Question_Num in range(len(Question_Bank)):
        print("*********************************")
        print(Question_Bank[Question_Num]["Text"])
        for i in Options[Question_Num]:
            print(i)
        Guess = input("Enter your Answer (A/B/C/D):").upper()
        Is_Correct = Check_Answer(Guess,Question_Bank[Question_Num]["Answer"])
        if Is_Correct:
            logger.info("Correct Answer")
            logger.info(f"Explanation:\n{Question_Bank[Question_Num]['Explanation']}")
            Score += 1
        else:
            logger.warning("Incorrect Answer")
            logger.info(f"Your correct Answer was {Question_Bank[Question_Num]['Answer']}")
        logger.info(f"Your current score is {Score}/{Question_Num+1}")

    logger.info(f"Your final score is {Score}")
    logger.info(f"The average of your score is {Score/len(Question_Bank):.2f}")
    logger.info(f"The percentage of your score is {Score/len(Question_Bank)*100}%")
except ValueError as e:
    logger.warning(f"Please enter valid input:{e}")
except Exception as v:
    logger.error(f"An unexcepted error occured:{v}")