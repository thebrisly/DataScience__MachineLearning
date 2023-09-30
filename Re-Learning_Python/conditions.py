import sys

message = "You've got a secret message"
error_message = "Oops, you don't have the right code"

if len(sys.argv) != 2:
    sys.exit("Not enough arguments")
else:
    x = sys.argv[1]
    try:
        x = int(x)
        if x == 42:
            print(message)
        else:
            print(error_message)
    except ValueError:
        print(error_message)
