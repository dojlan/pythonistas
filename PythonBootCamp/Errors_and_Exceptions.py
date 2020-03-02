try:
    # Trying out code with errors
    result = 10 + 10
    #result = 10 + '10'
except:
    print("Hey, it looks like you aren't adding correctly")
else:
    print("Adding went well!")
    print(result)


try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("There was a type error!")
finally:
    print("I always run")


try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except:
    print("All other errors!")
finally:
    print("I always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes, thank you")
            break
        finally:
            print("End of try/except/finally")
            pring("I will always run at the end!")

ask_for_int()

