show_instructions = ""
while show_instructions.lower() != "xxx":
    #ask if user have played before
    show_instructions = input('have you played this game before?').lower()
    #if they say yes, output "program continues'"
    #if they say no, output "display instructions"
    #if the answer is invalid, print an error
    if show_instructions == "yes" or show_isntrutions == "y":
        show_instructions == "yes"
        print("program keeps running")
    elif show_instructions == "no":
        print("display instructions")
    elif show_instructions == "n":
        print("display instructions")
    else:
        print("please answer yes/no")