"""def painter():
    return"I am a good Painter"
painter()
print(painter())


def painter():
    return"I am a good Painter"
msg=painter()
print(msg)
"""

s_username="PRIYAKUMAR_023"
s_password='123'
 

user_name=input()
password=input()

def validate():
    if(s_username==user_name and s_password==password):
        print("Correct")
    else:
        print("wrong")
validate()