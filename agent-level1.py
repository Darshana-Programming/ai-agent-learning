
def teaching_agent(question):
    question = question.lower()

    if "python" in question:
        return "Python is a programming language used in many fields."

    elif "database" in question:
        return "A database stores and organizes information."

    elif "algorithm" in question:
        return "An algorithm is a sequence of steps to solve a problem."

    else:
        return "I do not know this topic yet."


print("Welcome to the Simple Teaching Agent!")

while True:
    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        break

    response = teaching_agent(question)
    print("Agent:", response)
