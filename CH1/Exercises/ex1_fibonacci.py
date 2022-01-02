#/usr/bin/python
import argparse


def fibonacci(number: int) -> int:
    if number==0: return number
    last: int =0
    next: int = 1
    for _ in range(1, number):
        last, next = next, last + next 
    return next


def main():
    parser = argparse.ArgumentParser(description="Command Line Fibonacci Number Generator")
    parser.add_argument('--num', type=int,
				help='An integer number')
    args = parser.parse_args()
    number = args.num
    for i in range(1,number):
        print(fibonacci(i))

if __name__ =="__main__":
    main()