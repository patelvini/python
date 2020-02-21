# Command Line Arguments
Python Command line arguments are input parameters passed to the script when executing them. Almost all programming language provide support for command line arguments. Then we also have command line options to set some specific options for the program.

There are many options to read python command line arguments. The three most common ones are:

1.  Python sys.argv
2.  Python getopt module
3.  Python argparse  module

Let’s look through simple program to learn how to read and use python command line arguments.

### Python sys module

[Python sys module](https://www.journaldev.com/17243/python-sys-module) stores the command line arguments into a list, we can access it using `sys.argv`. This is very useful and simple way to read command line arguments as String.

 Let’s look at a simple example to read and print command line arguments using python sys module.

	import sys 
	
	print(type(sys.argv)) 
	print('The command line arguments are:') 
	for i in sys.argv: 
		print(i)

The output of a sample run of above program is as below:

	$ python3 CLA.py A B C
	<class 'list'>
	The command line arguments are:
	A
	B
	C
	

### Python argparse module

Python argparse module is the preferred way to parse command line arguments. It provides a lot of option such as positional arguments, default value for arguments, help message, specifying data type of argument etc. 

The argparse module makes it easy to write user-friendly command-line interfaces. It parses the defined arguments from the sys.argv.

The argparse module also automatically generates help and usage messages, and issues errors when users give the program invalid arguments.

The argparse is a standard module; we do not need to install it.

A parser is created with **ArgumentParser** and a new parameter is added with **add_argument()**. Arguments can be optional, required, or positional.

#### Argument Actions

There are six built-in actions that can be triggered when an argument is encountered:

- **store:** Save the value, after optionally converting it to a different type. This is the default action taken if none is specified expliclity.

- **store_const:** Save a value defined as part of the argument specification, rather than a value that comes from the arguments being parsed. This is typically used to implement command line flags that aren’t booleans.

- **store_true  /  store_false:** Save the appropriate boolean value. These actions are used to implement boolean switches.

- **append:** Save the value to a list. Multiple values are saved if the argument is repeated.

- **append_const:** Save a value defined in the argument specification to a list.

- **version:** Prints version details about the program and then exits.

#### Optional arguments:
| Argument | Meaning |Description|
|--|--|--|
| -h | --help | show this help message and exit |
| -s | SIMPLE_VALUE | Store a simple value |
| -c | |Store a constant value|
| -t|  |Set a switch to true|
| -f |  |Set a switch to false|
| -a | COLLECTION |Add repeated values to a list|
| -A | |Add different values to list|
| -B |  |Add different values to list|
| --version |  |show program's version number and exit|

**Example** 
The following example creates a simple argument parser.

    import argparse 

    parser = argparse.ArgumentParser()

    parser.add_argument('-o','--output', action='store_true',help="shows output") 
    
    #An argument is added with add_argument(). The action set to store_true will store the argument as True, if present. The help option gives argument help.

    args = parser.parse_args();
    #The arguments are parsed with parse_args(). The parsed arguments are present as object attributes. In our case, there will be args.output attribute.

    if args.output:
	    print("Example for optional argument in argparse module ")

**Output**
    
    C:\Users\vini.patel\Documents>python argparse1.py -o
    Example for optional argument in argparse module

    C:\Users\vini.patel\Documents>python argparse1.py --output
    Example for optional argument in argparse module

    C:\Users\vini.patel\Documents>python argparse1.py --help
    usage: argparse1.py [-h] [-o]

    optional arguments:
        -h, --help    show this help message and exit
        -o, --output  shows output

The example adds one argument having two options: a short -o and a long --ouput. These are optional arguments.


#### Positional Arguments:

The example expects two positional arguments: name and age.

Positional arguments are created without the dash prefix characters.

**Example**

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('name')
    parser.add_argument('age')

    args = parser.parse_args()

    print(f'{args.name} is {args.age} years old' )


**Output**

    C:\Users\vini.patel\Documents>python argparse_pos.py Vini 21
    Vini is 21 years old


#### Required Arguments

The example must have the name option specified; otherwise it fails.

**Example**

    #argparse required argument
    import argparse

    parser = argparse.ArgumentParser();

    parser.add_argument('--name',required=True)

    args = parser.parse_args()

    print(f'Hello {args.name}')


**Output**

    C:\Users\vini.patel\Documents>python argparse_req.py --name vini
    Hello vini

    C:\Users\vini.patel\Documents>python argparse_req.py --help
    usage: argparse_req.py [-h] --name NAME

    optional arguments:
        -h, --help   show this help message and exit
        --name NAME


#### argparse dest

The program gives the now name to the -n argument.

**Example**

    import argparse
    import datetime

    # dest gives a different name to a flag

    parser = argparse.ArgumentParser()
   
    parser.add_argument('-n', dest='now', action='store_true', help="shows now")

    args = parser.parse_args()

    # we can refer to the flag
    # by a new name
    if args.now:
        now = datetime.datetime.now()
        print(f"Now: {now}")
    
**Output**

    C:\Users\vini.patel\Documents>python argparse_dest.py -n
    Now: 2019-12-30 12:21:06.533669


#### argparse type

The program shows n random integers from -100 to 100.

The -n option expects integer value and it is required.

**Example**

    import argparse
    import random

    # type determines the type of the argument

    parser = argparse.ArgumentParser()
   
    parser.add_argument('-n', type=int, required=True, 
    help="define the number of random integers")
    args = parser.parse_args()

    n = args.n

    for i in range(n):
        print(random.randint(-100, 100))

**Output**

    C:\Users\vini.patel\Documents>python argparse_type.py -n 5
    -71
    -92
    7
    -14
    5

        	

# Input Output in python

## Reading Input From the Keyboard

Programs often need to obtain data from the user, usually by way of input from the keyboard. The simplest way to accomplish this in Python is with input().

    input([<prompt>])

>Reads a line of input from the keyboard.

input() always returns a string. If you want a numeric type, then you need to convert the string to the appropriate type with the int(), float(), or complex() built-in functions

**Example**

    >>> n = input('Enter a number: ')
    Enter a number: 50
    >>> print(n + 100)
    Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
    TypeError: must be str, not int

**Solution is**

    >>> n = int(input('Enter a number: '))
    Enter a number: 50
    >>> print(n + 100)
    150

**NOTE:** 
_raw_input() in Python 2 reads input from the keyboard and returns it. raw_input() in Python 2 behaves just like input() in Python 3, as described above._

## Writing Output to the Console

In addition to obtaining data from the user, a program will also usually need to present data back to the user. You can display program data to the console in Python with print().

o display objects to the console, pass them as a comma-separated list of argument to print().

    print(<obj>, ..., <obj>)

>Displays a string representation of each <obj> to the console.

By default, print() separates each object by a single space and appends a newline to the end of the output:

    >>> fname = 'Winston'
    >>> lname = 'Smith'

    >>> print('Name:', fname, lname)
    
    Output: Name: Winston Smith

Any type of object can be specified as an argument to print(). If an object isn’t a string, then print() converts it to an appropriate string representation displaying it:

    >>> a = [1, 2, 3]
    >>> type(a)
    <class 'list'>

    >>> b = -12
    >>> type(b)
    <class 'int'>

    >>> d = {'foo': 1, 'bar': 2}
    >>> type(d)
    <class 'dict'>

    >>> type(len)
    <class 'builtin_function_or_method'>

    >>> print(a, b, d, len)
    [1, 2, 3] -12 {'foo': 1, 'bar': 2} <built-in function len>

As you can see, even complex types like lists, dictionaries, and functions can be displayed to the console with print().

#### Keyword Arguments to print()

print() takes a few additional arguments that provide modest control over the format of the output. Each of these is a special type of argument called a keyword argument. 

**The sep= Keyword Argument**
Adding the keyword argument sep=<str> causes objects to be separated by the string <str> instead of the default single space:

    >>> print('foo', 42, 'bar')
    foo 42 bar
    
    >>> print('foo', 42, 'bar', sep='/')
    foo/42/bar

    >>> print('foo', 42, 'bar', sep='...')
    foo...42...bar

    >>> d = {'foo': 1, 'bar': 2, 'baz': 3}
    >>> for k, v in d.items():
        ...     print(k, v, sep=' -> ')
        ...
    foo -> 1
    bar -> 2
    baz -> 3

To squish objects together without any space between them, specify sep='':

    >>> print('foo', 42, 'bar', sep='')
    foo42bar

You can specify any arbitrary string as the separator with the sep= keyword.

**The end= Keyword Argument**
The keyword argument end=<str> causes output to be terminated by <str> instead of the default newline:

    >>> if True:
        ...     print('foo', end='/')
        ...     print(42, end='/')
        ...     print('bar')
        ...
    foo/42/bar

For example, if you are displaying values in a loop, you might use end= to cause the values to be displayed on one line, rather than on individual lines:

    >>> for n in range(10):
    ...     print(n)
    ...
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

    >>> for n in range(10):
    ...     print(n, end=(' ' if n < 9 else '\n'))
    ...
    0 1 2 3 4 5 6 7 8 9

Any string may be specified as the output terminator with the end= keyword.

# Variables in Python
Variables in python as the name suggests are the **values that vary**. In a programming language, a variable is a memory location where you store a value. The value that you have stored may change in the future according to the specifications.

A Variable in python is created as soon as a value is assigned to it. It does not need any additional commands to declare a variable in python.

>x = 10

>variable is declared as the value 10 is assigned to it.

A variable is a container for a value. It can be assigned a name, you can use it to refer to it later in the program. Based on the value assigned, the interpreter decides its data type. You can always store a different type in a variable.

![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2019/12/python-variables-2-1.jpg)

### How the memory is allocated to variables in python ???

![](https://miro.medium.com/max/716/1*aj7wuuq_KYMxOS4m2HNlfg.png)

In python everything is considered as an object. In python we do not have variables  instead python has names. When we declare a name/variable in python it stores the name in the memory. Every python name/variable points to its **reference** in the memory and reference points to the object. 

Let's consider the example code "a = 100" , "a" is name and it's points to the reference "31365024" and the reference points to the object "100" which is in binary format. A name is just a label for an object. In python each object can have lots of names.

Python has stack memory and heap memory.  Stack memory stores the state of the program. Private heap memory stores the  objects and data structures. Python memory manager will takes care of the allocation of the private heap memory to the names/variables. Python manager uses the concept called Reference counting, whenever a new object is created it will update the reference count of the object.

    # case1
    a = 100
    b = 200
 
    # case2
    a = 100
    b = 100

Lets consider the above code.

In "case1"  python memory manager will create the two objects. "a" points to the object "100" and "b" points to the object "200". The reference count of the object "100" is 1 and the reference count of the object "200" is 1.
 
In "case2" python memory manager creates only one object i.e "100" and reference count is "2". Whenever a new object is created pyhon manager will checks the memory for the object. If object already exists python manager will not create new object instead it references the name to the object and increases the reference counter of the object.

Every python object holds three things

1. object -> type 
2. object -> value 
3. object -> reference counter 


**Reference** is a name or a container object which points to another object. **Reference count** is the number of references.

Memory table for "case2"

| type | int |
|--|--|
| **value**	| **100** |
| **reference count** |	**2** |
| **references** | **a, b** |

We can get the object memory location with python built-in function "id"

    a = 100
    print(id(a))
    # 10914336
    b = 100
    print(id(b))
    # 10914336
    print(id(a) == id(b))
    # True

**id()** will return an objects memory address (object's identity). As you have noticed, when you assign the same integer value to the variables, we see the same ids. But this assumption does not hold true all the time. 

See the following for example,

    >>> x = 500
    >>> y = 500
    >>> id(x)
    4338740848
    >>> id(y)
    4338741040

What happened here? Even after assigning the same integer values to different variable names, we are getting two different ids here. These are actually the effects of CPython optimization we are observing here. CPython implementation keeps an array of integer objects for all integers between -5 and 256. So when we create an integer in that range, they simply back reference to the existing object. 



### Variable naming rules in python
- variable name should not contain a space.
- variable name should starts with a letter or an underscore(_).
- special symbols **(~, !, @, #, $, etc.)** are not allowed in variable name.
- variable should be short and meaningful as per the data stored in variable.
- If we want to use multiple words in a variable we can use underscore(_) to separate the words. 
  - **Example,** variables "student_name", "account_number", "phone_num1", "phone_num2", etc.
- Python is **case sensitive** language so, it treats the lowercase letters and upper case letters differently. 
  - **Example,** variable "Student" is different from the variable "student".
- We should not use python [reserved variables/names](https://docs.python.org/3/reference/lexical_analysis.html?highlight=keywords#keywords) as varibles though we are allowed to use it.
- It is better practice to use lowercase letters instead of uppercase letters.


### Assigning and Reassigning Python Variables

To assign a value to Python variables, you don’t need to declare its type. You name it according to the rules stated in section 2a, and type the value after the equal sign(=).

    >>> age=7
    >>> print(age)
    7

    >>> age='Dinosaur'
    >>> print(age)
    Dinosaur

However, age=Dinosaur doesn’t make sense. Also, you cannot use Python variables before assigning it a value.

    >>> name
>Traceback (most recent call last):
File “<pyshell#8>”, line 1, in <module>
	name
	NameError: name ‘name’ is not defined


### Multiple Assignment
You can assign values to multiple Python variables in one statement.

    >>> age,city=21,'Indore'
    >>> print(age,city)
    21 Indore

Or you can assign the same value to multiple Python variables.

    >>> age=fav=7
    >>> print(age,fav)
    7 7

### Swapping Variables

Swapping means interchanging values. To swap Python variables, you don’t need to do much.

    >>> a,b='red','blue'
    >>> a,b=b,a
    >>> print(a,b)
    blue red

### Deleting Variables
You can also delete Python variables using the keyword ‘del’.

    >>> a='red'
    >>> del a
    >>> a
>Traceback (most recent call last):
File “<pyshell#39>”, line 1, in <module>
	a
	NameError: name ‘a’ is not defined

This is How you can delete Python Variables.


### Special Variable

The `__name__` variable (two underscores before and after) is a special Python variable. It gets its value depending on how we execute the containing script.
Sometimes you write a script with functions that might be useful in other scripts as well. In Python, you can import that script as a module in another script.
Thanks to this special variable, you can decide whether you want to run the script. Or that you want to import the functions defined in the script.

#### What values can the `__name__` variable contain?

When you run your script, the `__name__` variable equals `__main__`. When you import the containing script, it will contain the name of the script.

Let us take a look at these two use cases and describe the process with two illustrations.

#### Scenario 1 - Run the script

Suppose we wrote the script `nameScript.py` as follows:

    def myFunction():
        print 'The value of __name__ is ' + __name__
    
    def main():    
        myFunction()
    
    if __name__ == '__main__':    
        main()

If you run `nameScript.py`, the process below is followed.

![](https://cdn-media-1.freecodecamp.org/images/PljpjxnM1OMMW7IkexNxVfwrKhP0RH-isapH)

Before all other code is run, the `__name__` variable is set to `__main__`. After that, the main and myFunction def statements are run. Because the condition evaluates to true, the main function is called. This, in turn, calls myFunction. This prints out the value of `__main__`.

#### Scenario 2 - Import the script in another script

If we want to re-use myFunction in another script, for example `importingScript.py`, we can import `nameScript.py` as a module.

The code in `importingScript.py` could be as follows:

    import nameScript as ns
    ns.myFunction()

We then have two scopes: one of importingScript and the second scope of nameScript. In the illustration, you’ll see how it differs from the first use case.

![](https://cdn-media-1.freecodecamp.org/images/k9OxzvJAP-s5qeZg88jUCOCVy1syrQu4oKds)

In `importingScript.py` the `__name__` variable is set to `__main__`. By importing nameScript, Python starts looking for a file by adding .py to the module name. It then runs the code contained in the imported file.

But this time it is set to nameScript. Again the def statements for main and myFunction are run. But, now the condition evaluates to false and main is not called.

In `importingScript.py` we call myFunction which outputs nameScript. NameScript is known to myFunction when that function was defined.

If you would print `__name__` in the importingScript, this would output `__main__`. The reason for this is that Python uses the value known in the scope of importingScript.

# Operators
Python operator is a symbol that performs an operation on one or more operands. An operand is a variable or a value on which we perform the operation.

![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2017/12/Python-Operators-2.jpg)

### Python Arithmetic Operator

These Python arithmetic operators include Python operators for basic mathematical operations.

![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2017/12/Python-Arithmetic-Operator-01-768x402.jpg)

The following assumptions variable a is 10, b is variable 20:

| Operators | Description |	Examples | Output |
|--|--|--|--|
| + | Plus - two objects are added | a + b | 30 |
| – | Save – get a negative number is subtracted from another number | a – b | -10 |
| * | Multiply – multiply two numbers or returns the string repeated several times |  a * b | 200 |
| / | In addition – x divided by y | b / a | 2 |
| % | Modulo – returns the division remainder |	b % a |	0 |
| ** | Power – returns x raised to the power of y (x ** y) |	10 20th power |  100000000000000000000 |
| // |	Take divisible – Returns the integer part of the quotient |	9 // 2, 9.0 // 2.0	| 4, 4.0 |

### Python Bitwise Operator

![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2017/12/Python-Bitwise-Operator-01-768x402.jpg)

| Operators | Description |	Examples | Output |
|--|--|--|--|
| & | Binary AND - It performs bit by bit AND operation on the two values|	binary for 2 is 10, and that for 3 is 11 | 2 & 3 = 10 (Binary of 2)  |
| \| | Binary OR - It performs bit by bit OR on the two values | OR-ing 10(2) and 11(3) | results in 11(3) |
| ^ | Binary XOR - It performs bit by bit XOR(exclusive-OR) on the two values |	XOR-ing 10(2) and 11(3) | results in 01(1) |
| ~ | Binary One’s Complement - It returns the one’s complement of a number’s binary. It flips the bits |	Binary for 2 is 00000010 | Its one’s complement is 11111101 |
| << | Binary Left-Shift - It shifts the value of the left operand the number of places to the left that the right operand specifies | binary of 2 is 10(2<<2) | shifts it two places to the left. This results in 1000, which is binary for 8. |
| >> | Binary Right-Shift - It shifts the value of the left operand the number of places to the right that the right operand specifies |	binary of 3 is 11 (3>>2) | shifts it two places to the right. This results in 00, which is binary for 0 |

### Python Relational (Comparision) Operators

![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2017/12/Python-Relational-Operator-01-1-768x402.jpg)

The Relational operators (Comparison operators) are used to evaluate expressions that can only have 2 results, these results are true or false (true or false) and are the following.

The following assumptions variable a is 10, b is variable 20:

| Operators | Description |	Examples |
|--|--|--|
| == |	Equal – compare objects for equality |	(A == b) returns False |
|! = | It is not equal – compare two objects are not equal | (A! = B) returns true |
| <> | It is not equal – compare two objects are not equal | (A <> b) returns true |
| > | Greater than – Returns whether x is greater than y | (A> b) returns False |
| < | Less than – Returns whether x is less than y. All comparison operators return 1 for true and 0 for false. These respectively special variables True and False equivalence. Note that these variable name capitalization |	(A <b) returns true |
| > = |	Greater than or equal – Returns whether x is greater than or equal y | (A> = b) returns False |
| <= | Less than or equal – Returns whether x is less than or equal y |	(A <= b) returns true |

### Python Assignment Operators
![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2017/12/Python-Assignment-Operator-01-768x402.jpg)

The assignment operators are used to basically assign a value to a variable, as well as when we use the “=”.

| Operators | Description |	Examples |
|--|--|--|
| = | Equal to, is the simplest of all and assigns to the variable on the left side any variable or result on the right side | c = a + b, a + b operation will assign the result to c |
| + = |	Addition assignment operator, adds to the variable on the left side the value on the right side | c + = a is equivalent to c = c + a |
| – = |	Subtraction assignment operator, subtract the value on the right side from the variable on the left side|	c – = a is equivalent to c = c – a |
| * = |	Multiplication assignment operator, multiply the value on the right side of the variable on the left side |	equivalent to c * = a c = c * a |
| / = |	Division assignment operator, divide the value on the right side of the variable on the left side |	c / = a is equivalent to c = c / a |
| % = |	Modulo assignment operator | c% = a is equivalent to c = c% a |
| ** = | Exponentiation assignment operator | c ** = a is equivalent to c = c ** a |
 |// = | Take divisible assignment operator | c // = a is equivalent to c = c // a |
 
 
### Python Logical Operator

![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2017/12/Python-Logical-Operator-01-768x402.jpg)

| Operators | Description |	Examples | Output |
|--|--|--|--|
| and |	If the conditions on both the sides of the operator are true, then the expression as a whole is true | a=7>7 and 2>-1 | False |
| or | The expression is false only if both the statements around the operator are false. Otherwise, it is true | a=7>7 or 2>-1 | True |
| not | This inverts the Boolean value of an expression. It converts True to False, and False to True | a=not(0) | True |

### Python Membership Operator

These operators test whether a value is a member of a sequence. The sequence may be a list, a string, or a tuple. We have two membership python operators- ‘in’ and ‘not in’.

- **in**

    This checks if a value is a member of a sequence. In our example, we see that the string ‘fox’ does not belong to the list pets. But the string ‘cat’ belongs to it, so it returns True. Also, the string ‘me’ is a substring to the string ‘disappointment’. Therefore, it returns true.
	
> pets=[‘dog’,’cat’,’ferret’]
 
> ‘fox’ in pets

> Output: False

- **not in**

    Unlike ‘in’, ‘not in’ checks if a value is not a member of a sequence.

 > ‘pot’ not in ‘disappointment’
    
 > Output: True

### Python Identity Operator

These operators test if the two operands share an identity. We have two identity operators- ‘is’ and ‘is not’.

- **is**

    If two operands have the same identity, it returns True. Otherwise, it returns False. Here, 2 is not the same as 20, so it returns False. Also, ‘2’ and “2” are the same. The difference in quotes does not make them different. So, it returns True.
	
> 2 is 20

> Output: False
	
> ‘2’ is “20"

> Output: True

- **is not**

    2 is a number, and ‘2’ is a string. So, it returns a True to that.
    	
> 2 is not ‘2’

> Output: True


# Precedence and Associativity of Operators in Python

**How Does The Operator Precedence Work In Python?**

When we group a set of values, variables, operators or function calls that turn out as an expression. And once you execute that expression, Python interpreter evaluates it as a valid expression.

See the below example which combines multiple operators to form a compound expression.

	Multiplication get evaluated before
	the addition operation
	Result: 17
	5 + 4 * 3

However, it is possible to alter the evaluation order with the help of parentheses (). It can override the precedence of the arithmetic operators.

	Parentheses () overriding the precedence of the arithmetic operators
	Output: 27
	(5 + 4) * 3

**What Does The Associativity Mean In Python?**

The associativity is the order in which Python evaluates an expression containing multiple operators of the same precedence. Almost all operators except the exponent ( ** ) support the left-to-right associativity.

For example, the product (*) and the modulus (%) have the same precedence. So, if both appear in an expression, then the left one will get evaluated first.

	Testing Left-right associativity
	Result: 1
	print(4 * 7 % 3)

	Testing left-right associativity
	Result: 0
	print(2 * (10 % 5))

As said earlier, the only operator which has right-to-left associativity in Python is the exponent (**) operator.

See the examples below.

	Checking right-left associativity of ** exponent operator
	Output: 256
	print(4 ** 2 ** 2)

	Checking the right-left associativity
	of **
	Output: 256
	print((4 ** 2) ** 2)

You might have observed that the ‘print(4 ** 2 ** 2)’ is similar to ‘(4 ** 2 ** 2).


| Precedence | Associativity | Operators | Description |
|--|--|--|--|
| 18 | Left-to-right | () | Parentheses (Grouping) |
| 17 | Left-to-right | f(args...) | Function Call |
| 16 | Left-to-right | x[index:index] | Slicing |
| 15 | Left-to-right | x[index] | Array Subscription |
| 14 | Right-to-left | ** | Exponantiation |
| 13 | Left-to-right | ~x | Bitwise not |
| 12 | Left-to-right | +x, -x | Positive, Negative |
| 11 | Left-to-right | *, /, % | Multiplication, Division, Modulo |
| 10 | Left-to-right | +, - | Addition, Subtraction |
| 9 | Left-to-right | <<, >> | Bitwise left shift, Bitwise right shift |
| 8 | Left-to-right | & | Bitwise AND |
| 7 | Left-to-right | ^ | Bitwise XOR |
| 6 | Left-to-right | \| | Bitwise OR |
| 5 | Left-to-right | in, not in, is, is not, <, <=, >, >=, <>, ==, != | Membership, Relational, Equality, Inequality |
| 4 | Left-to-right | not x | Boolean NOT |
| 3 | Left-to-right | and | Boolean AND |
| 2 | Left-to-right | or | Boolean OR |
| 1 | Left-to-right | lambda | Lambda expression |

# Numbers in Python

Python provides number types that can be used to manipulate numbers. Although it has been discussed under Python Data Types, we would do a brief review of the four Python Number types.

A number is an arithmetic entity that lets us measure something. Python allows us to store the integer, floating, and complex numbers and also lets us convert between them. Since Python is dynamically-typed, there is no need to specify the type of data for a variable.

## Types of numeric data

Python 2.x had four built-in data types (int, long, float and complex) to represent numbers. Later Python 3.x removed the long and extended the int type to have unlimited length.

### The Int Type
The int type represents the fundamental integer data type in Python. The plain integer in Python 2.x had the maximum size up to the value of sys.maxint.

While in 3.x, the int type got promoted to have unlimited length and thus eliminated the long.

    >>> x = 9
    >>> type(x)
    <type 'int'>

### The Long Type
An integer number with unlimited length. Until the end of Python 2.x, the integers were allowed to overflow and turned into a long. This behavior changed since 3.0, where the ints replaced the longs.

    >>> x = 9999999999
    >>> type(x) # In Python 2.x, the type will be long. While in 3.x, it is int irrespective of the size.
    <type 'long'>

### The Float Type
The float represents a binary floating point number. Using a float variable in an expression automatically converts the adjoining longs and ints to floats.

    >>> x = 9.999
    >>> type(x)
    <type 'float'>

### The Complex Type
The number of this type has a real and an imaginary part. For example – The expression **(n1 + n2j)** represents a complex type where both n1 and n2 are the floating-point numbers denoting the real and imaginary parts respectively.

    >>> x = 3 + 4j
    >>> type(x)
    <class 'complex'>
    >>> x.real
    3.0
    >>> x.imag
    4.0

- **Coefficient to the imaginary part:**
 Here, 3 is the real part, and 4j is the imaginary part. To denote the irrational part, however, you can’t use the letter ‘i’, like you would do on paper.

        >>> a=2+3i
        SyntaxError: invalid syntax

    Also, it is mandatory to provide a coefficient to the imaginary part.

        >>> a=2+j
        Traceback (most recent call last):

        File “<pyshell#33>”, line 1, in <module>

        a=2+j

        NameError: name ‘j’ is not defined

    In this case, a coefficient of 1 will do.

        >>> a=2+1j
        >>> a
        (2+1j)

- **Operations on complex numbers:**
     Finally, you can perform the basic operations on complex numbers too.

        >>> a=2+3j
        >>> b=2+5j
        >>> a+b
        (4+8j)

        >>> a*=2
        >>> a
        (4+6j)

    Here, *= is an in-place assignment operator.

### Python Numbers – Key Points
- The number types are automatically upcast in the following order.
**Int → Long → Float → Complex**
- While integers in Python 3.x can be of any length, a float type number is only precise to fifteen decimal places.
- Usually, we work with numbers based on the decimal (base 10) number system. But sometimes, we may need to use other number systems such as binary (base 2), hexadecimal (base 16) and octal (base 8).
- In Python, we can deal such numbers using the proper prefixes. See below.

    | Number System | Base |Prefix to Use|
    |--|--|--|
    |Binary	|Base-2	|‘0b’ or ‘0B’|
    |Octal	|Base-8	|‘0o’ or ‘0O’|
    |Hex|	Base-16	|‘0x’ or ‘0X’|

**Example:**
    
    >>> x = 0b101
    >>> print(x)
    5
    >>> type(x)
    <type 'int'>
    >>> print(0b101 + 5)
    10
    >>> print(0o123)
    83
    >>> type(0x10)
    <type 'int'>

If you want to test the class type of a number in Python, then you should use the **isinstance()** function.
> isinstance(object, class)

Here is the example.

    >>> isinstance(2.2, float)
    True
    
### Python Conversion Functions

![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2017/12/Conversion-Functions-01.jpg)

- **int()**
	The int() function can convert another numeric type into an int. It can also convert other types into an int, but in this tutorial, we focus on numeric types.

		>>> int(7)
		7

		>>> int(7.7)
		7

	As you can see, it does not round the number 7.7 up to 8; it truncates the 0.7.

	However, you cannot convert a complex number into an int.

		>>> int(2+3j)
		Traceback (most recent call last):

		File “<pyshell#22>”, line 1, in <module>

		int(2+3j)

		TypeError: can’t convert complex to int

		>>> int(3j)
		Traceback (most recent call last):

		File “<pyshell#23>”, line 1, in <module>

		int(3j)

		TypeError: can’t convert complex to int

	We can also apply this function on representations other than decimal, i.e., binary, octal, and hexadecimal.

		>>> int(0b10)
		2

		>>> int(0xF)
		15

- **float()**
	This function converts another numeric type into a float.

		>>> float(110)
		110.0

		>>> float(110.0)
		110.0

	Like int(), float() can’t convert a complex either.

		>>> float(3j)
		Traceback (most recent call last):

		File “<pyshell#26>”, line 1, in <module>

		float(3j)

		TypeError: can’t convert complex to float

		>>> float(0o10)
		8.0

	Here, we applied it to an octal number.

- **complex()**
	The complex() function converts another numeric type into a complex number.

		>>> complex(2)
		(2+0j)

		>>> complex(2.3)
		(2.3+0j)

		>>> complex(2+3.0j)
		(2+3j)

- **bin()**
	The bin() function returns the binary value of a number.

		>>> bin(2)
		‘0b10’

	However, you can’t apply it to a float value or a complex value. The same is true for oct() and hex() functions too.

		>>> bin(2.3)
		Traceback (most recent call last):

		File “<pyshell#49>”, line 1, in <module>

		bin(2.3)

		TypeError: ‘float’ object cannot be interpreted as an integer

		>>> bin(2+3j)
		Traceback (most recent call last):

		File “<pyshell#50>”, line 1, in <module>

		bin(2+3j)

		TypeError: ‘complex’ object cannot be interpreted as an integer

- **oct()**
	This function returns the octal value of a number.

		>>> oct(8)
		‘0o10’

	We know that 8.0 is the same as 8, but the function doesn’t think the same. It is a float, so it cannot convert it into an oct.

		>>> oct(8.0)
		Traceback (most recent call last):
	
		File “<pyshell#59>”, line 1, in <module>

		oct(8.0)

		TypeError: ‘float’ object cannot be interpreted as an integer

- **hex()**
	The hex() function returns the hexadecimal value of a number.

		>>> hex(255)
		‘0xff’

		>>> hex(0)
		‘0x0’

		>>> hex(0)
		‘0x0’

### Python Decimal Module
Let’s try out adding 1.1 and 2.2 in the shell, and let’s compare it with 3.3.

	>>> (1.1+2.2)==3.3
	False

Why did it return False? Let’s try printing the sum.

	>>> 1.1+2.2
	3.3000000000000003

Woah, how did this happen? Well, this is duly attributed to hardware limitations, and is not a flaw of Python. Because the hardware stores decimals as binary fractions, it isn’t possible to store it very accurately. Let’s take an example.

	>>> 1/3
	0.3333333333333333

When we divide 1 by 3, it doesn’t return the full value, which is 0.3333333333333333… Python does provide a solution to this problem. It has the ‘decimal’ module, which lets us choose precision. We will learn about modules in a later lesson.

	>>> import decimal
	>>> print(decimal.Decimal(0.1))
	0.1000000000000000055511151231257827021181583404541015625

Did you see what happened here? The Decimal() function preserved the significance.This was the Decimal Function Python number type.

### The fractions Module
Another module that Python provides, the fractions module lets you deal with fractions. The Fraction() function returns the value in the form of numerator and denominator.

	>>> from fractions import Fraction
	>>> print(Fraction(1.5))
	3/2

It can also take two arguments.

	>>> print(Fraction(1,3))
	1/3

### The math Module
Another essential module is the math module. It has all important mathematical functions like exp, trigonometric functions, logarithmic functions, factorial, and more.

	>>> import math
	>>> math.factorial(5)
	120

	>>> math.exp(3)
	20.085536923187668

	>>> math.tan(90)
	-1.995200412208242