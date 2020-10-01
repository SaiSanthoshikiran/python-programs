#"quiz using dictionaries with skip and quit options showing final results"
n=input('enter your name:')
print('Hello',n,'welcome to the quiz')
q1="""what is the capital of Andhra Pradesh?
a)Hyderabad
b)Delhi
c)Amaravathi
d)None"""
q2="""what is our National Anthem?
a)sare jahse acha
b)jana gana mana
d)vandemataram
e)None"""
q3="""what is our national animal?
a)Tiger
b)Lion
c)Giraffe
d)Deer"""

questions={q1:"c",q2:"b",q3:"a"}
score=0
for i in questions:
    print(i)
    skip=input('do you want to skip this question(yes/no):')
    if skip=="yes":
        continue
    ans=input('enter answer(a/b/c/d)')
    if ans==questions[i]:
        print('correct answer,+1 mark')
        score+=1
        print('current score:',score)
    else:
        print('wrong answer,-1 mark')
        score-=1
        print('current score:',score)
    quit=input('do you want to qiut from quiz(yes/no):')
    if quit=="yes":
        break
print('Final score is:',score)
