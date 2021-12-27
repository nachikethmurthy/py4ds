#!/usr/bin/env python
import argparse

def say_it(greeting,target):
    message = f"{greeting} {target}"
    print(message)

if __name__ == "__main__":
    greeting = "Hello"
    target = "Joe"

    parser = argparse.ArgumentParser(description="Greeting the User")
    parser.add_argument("name",help="Name of User")
    parser.add_argument("--greet", help="Greeting Word") # -- : optional argument

    args = parser.parse_args() # parse the arguments
    if len(args.name) > 0:
        target = args.name
    if len(args.greet) > 0:
        greeting = args.greet
    
    say_it(greeting=greeting,target=target)

#./ex_4.py John --greet Bonjour