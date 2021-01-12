import os,time
def randomNumber(top):
    number = os.getpid()*time.time_ns()%top
    return int(number)


print("random numbers: ")
print(randomNumber(45))
print(randomNumber(89))
print(randomNumber(1111))
print(randomNumber(18546))
print(randomNumber(454))