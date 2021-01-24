import random

def create_outline():
    """
    TODO: implement your code here
    """
    #1. Create a set of topics for the course
    #2. Create a map(dictionary) of topics to it's list of problems
    #3. Create a simple tuple structure to try out how to show the progress of\
    # a student for a list of problems
    #4. Traversing, sorting and printing the various structures
    topics = {"Introduction to Python", "Tools of the Trade", \
    "How to make decisions", "How to repeat code", "How to structure data", \
    "Functions", "Modules"}
    topics = list(topics)
    topics.sort()
    print("Course Topics:")
    for i in topics:
        print('* ' + i)
    # pass


# def problem_set(n):
    problem_list = ['Problem 1','Problem 2','Problem 3']
    student_map = {}
    for a in topics:
        student_map[a] = problem_list



    print("Problems:")
    for variable1, variable2 in student_map.items():#returns the keys and values
        print(f"* {variable1} : ",end='')
        if problem_list != problem_list[0] or problem_list[1]:
            print(f'{variable2[0]}, {variable2[1]}, {variable2[2]}')
            #* => unpacks the values in a key {dict}
    #pass
    # return problem_set()

# def student_names():

    name = "Nyari","Adam","Moloko","Dom","The Wolf","Katlego","Alex","Jessica"

    status = "[STARTED]","[GRADED]","[COMPLETED]"
    student_tuple = {}
    student_progress = []
    counter = 1
    print("Student Progress:")
    progress = str()
    count = 0
    for y, i in enumerate(name):
        count += 1
        progress = (f"{count}. {(i)} - {random.choice(topics)} - {random.choice(problem_list)} {status[y//len(status)]}")
        print(progress)

    pass


if __name__ == "__main__":
    create_outline()
