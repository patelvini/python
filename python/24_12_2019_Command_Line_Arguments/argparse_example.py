import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a','--addition',action='store_true',help="Add two numbers")
parser.add_argument('-s','--subtraction',action='store_true',help="Subtract two numbers")
parser.add_argument('-m','--multiplication',action='store_true',help="Multiply two numbers")
parser.add_argument('-d','--division',action='store_true',help="Divide two numbers")
parser.add_argument('-no1','--num1',help="get 1st number",type=int)
parser.add_argument('-no2','--num2',help="get 2nd number",type=int)

args = parser.parse_args()

if args.addition:
    print(args.addition)
    add = args.num1+args.num2
    print("Addition is :",add)
elif args.subtraction:
    sub = args.num1-args.num2
    print("Subtraction is :",sub)
elif args.multiplication:
    mul = args.num1*args.num2
    print("Multiplication is :",mul)
elif args.division:
    divi = args.num1/args.num2
    print("Division is :",divi)
else:
    print("No arguments given")




