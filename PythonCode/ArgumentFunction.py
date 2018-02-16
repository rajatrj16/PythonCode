def studentScore(name,score):
    print(name,"Scored", score,"Marks")
studentScore("rajat",30)


def studentScore(name="Rajat",score=70):
    print(name,"Scored", score,"Marks")
studentScore()
studentScore("Mark",64)


studentScore("king")
studentScore(score= 994)


def studentScore(name,*score):
    print(name)
    print(score)

studentScore("Rajat",64,44,56,10,90)


def student(*name):
    print(name)
student("Rajat","Rjt", "rajt jain")

def name(*name):
    print(name)
name("a","b","c")
