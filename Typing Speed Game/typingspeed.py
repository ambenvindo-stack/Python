from ftplib import error_reply
from time import time

from prompt_toolkit import prompt # to record the time


# now to calculate accuracy of input prompt
def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1] == words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors =+ 1
            else:
                errors =+ 1
    return errors

# now to calculate the speed of typing words per minute
def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time

    return speed

# calculate the total elapsed time

def elapsedtime(stime, etime):
    time = etime - stime                   #etime is the end and stime is the start time
    return time    


if __name__ == '__main__':
    prompt = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido Van Rossum and first released in 1991, Python's design philosophy emphasizes code readbility with its notable use of significant whitespace. Its language constructs and objects oriented, and functional programming. Python is often described as a \"batteries included\" language due to its comprehensive standard library."
    #this was the paragraph which you have to type to check your speed
    print("Type this:- ", prompt, "")

    # checking to input Enter basically it will see
    input("Press Enter when you are ready to check your speed!!!")

    # recording time for input
    stime = time()
    inprompt = input()
    etime = time()

    # collect all the information returned by the functions
    time = round(elapsedtime(stime,etime), 2)  # round off the time
    speed = speed(inprompt,stime,etime)
    errors = tperror(prompt)

    #printing all the required data  to see result

    print("Total time elapsed: ", time, "seconds")
    print("Your Average Typing speed was ", speed, "words per minute (w/m)")
    print("with the total of ", errors, "errors")