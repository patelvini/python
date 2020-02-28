# Function and Function Caling in Python
### Python function definition
A function is a block of reusable code that is used to perform a specific action. The advantages of using functions are:
- Reducing duplication of code
- Decomposing complex problems into simpler pieces
- Improving clarity of the code
- Reuse of code
- Information hiding

Functions in Python are first-class citizens. It means that functions have equal status with other objects in Python. Functions can be assigned to variables, stored in collections, or passed as arguments. This brings additional flexibility to the language.


### Python Function Types
There are two types of functions in Python.

- **built-in functions:** The functions provided by the Python language such as print(), len(), str(), etc.
- **user-defined functions:** The functions defined by us in a Python program.

## user-defined functions

#### Importance of user-defined functions in Python

In general, developers can write user-defined functions or it can be borrowed as a third-party library. This also means your own user-defined functions can also be a third-party library for other users. User-defined functions have certain advantages depending when and how they are used. Let ‘s have a look at the following points.

- User-defined functions are reusable code blocks; they only need to be written once, then they can be used multiple times. They can even be used in other applications, too.
- These functions are very useful, from writing common utilities to specific business logic. These functions can also be modified per requirement.
- The code is usually well organized, easy to maintain, and developer-friendly. Which means it can support the modular design approach.
- As user-defined functions can be written independently, the tasks of a project can be distributed for rapid application development.
- A well-defined and thoughtfully written user-defined function can ease the application development process.

#### Writing user-defined functions in Python
These are the basic steps in writing user-defined functions in Python. For additional functionalities, we need to incorporate more steps as needed.

- Step 1: Declare the function with the keyword def followed by the function name.
- Step 2: Write the arguments inside the opening and closing parentheses of the function, and end the declaration with a colon.
- Step 3: Add the program statements to be executed.
- Step 4: End the function with/without return statement.

**Syntax**

    def functionname( parameters ):
        "function_docstring"
        function_suite
        return [expression]
   
The def keyword is followed by the function name with round brackets and a colon. The indented statements form a body of the function.
The function is later executed when needed. 

### Calling a function

**To call a function, we specify the function name with the round brackets.**

We say that we call the function. If we call a function, the statements inside the function body are executed. They are not executed until the function is called.

>myfunc()

Defining a function only gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code.

#### call by value
Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from the Python prompt. Following is the example to call printme() function −

    #!/usr/bin/python

    # Function definition is here
    def printme( str ):
        "This prints a passed string into this function"
        print str
        return;

    # Now you can call printme function
    printme("I'm first call to user defined function!")
    printme("Again second call to the same function")
    
    #When the above code is executed, it produces the following result −
    #output:
    I'm first call to user defined function!
    Again second call to the same function
    
#### Call by reference in Python
In Python, both the parameters and the arguments point to the same memory location. So, any changes made to the parameter inside the function definition are reflected in the arguments of the main() function.

However, there is an exception in the case of mutable objects since the changes made to the mutable objects like string do not revert back to the original string.

In the below example, the list is appended with the elements 5 and 6 inside the function definition and the same has been reflected inside the main() function also.

    #defining the function 
    def reference(list1): 
        list1.append(5)
        list1.append(6)
        print("List inside function: ", list1) 
    list1 = [1, 2, 3, 4] 
    #calling the function 
    reference(list1)
    print("List outside function: ", list1)
    
    #Output:
    List inside function: [1, 2, 3, 4, 5, 6]
    List outside function: [1, 2, 3, 4, 5, 6]

But in case of strings, the changes made inside the function will not be reflected inside the main() function as shown below.

    #defining the function 
    def reference(string1): 
        string1 = string1 + "Prep"
        print("String inside function: ", string1)
    string1 = "FACE" 
    #calling the function 
    reference(string1) 
    print("String outside function: ", string1)

    #Output:
    String inside function: FACEPrep
    String outside function: FACE

**We can consider main four types of functions based on the argument and return value specified : **
1. Function with no argument and no Return value
2. Function with no argument and with Return value
3. Function with argument and No Return value
4. Function with argument and Return value

### Function with no argument and no Return value

![](https://www.tutorialgateway.org/wp-content/uploads/Types-of-Functions-in-Python-programming-1.png)

### Function with no argument and with Return value

![](https://www.tutorialgateway.org/wp-content/uploads/Types-of-Functions-in-Python-programming-2.png)

### Python Function with argument and No Return value

![](https://www.tutorialgateway.org/wp-content/uploads/Types-of-Functions-in-Python-programming-3.png)

### Function with argument and Return value

![](https://www.tutorialgateway.org/wp-content/uploads/Types-of-Functions-in-Python-programming-4.png)

## built in functions

![](https://ci4.googleusercontent.com/proxy/PsxWifYBeA47eYEynjOwNJshUXx14pfOpqMVpV011WQTs_K2UUpyGeuVEaWpPY1MdFf2n6yCzxcfoM1eDuvbeOKKsG3Y3sNoqFGWnqlNMudmuXo=s0-d-e1-ft#http://www.trytoprogram.com/images/python-built-in-functions.jpg)

The Python interpreter has a number of functions that are always available for use. These functions are called built-in functions. For example, **print()*** function prints the given object to the standard output device (screen) or to the text stream file.

### User Defined Functions (UDF) versus built in functions

The first function you come across in Python is the print function and its famously known to print(“Hello World) when you learn to code. 

_Note: That is Python 3 syntax, for Python 2.7 you drop the parentheses and type print “Hello World”._

Other functions, I quickly came across were also other built in functions like range(), sort(), str(), and min(). These were already defined in the **Python library framework** and all I had to use it was call them and pass arguments through them. 

A user defined function is first started by the keyword def. It makes sense that it is a user defined function because, I could name the function whatever I wanted after writing def followed by a name, parentheses, and then a colon. 

**For example,**
def clean_room(room):
    #body of the function


# Recursive function approach

Recursion occurs when any function calls itself.

This means that the function will continue to call itself and repeat its behavior until some condition is met to return a result. All recursive functions share a common structure made up of two parts: base case and recursive case.

![](https://www.educative.io/api/collection/10370001/5102090441457664/page/6362672020848640/image/5087704570134528.png)

To terminate the recursion, you must include a select statement in the definition of the function to force the function to return without giving a recursive call to itself. The absence of the select statement in the definition of a recursive function will let the function in infinite recursion once called.

**Example :**

![](https://ci5.googleusercontent.com/proxy/zlzwTlmQznR4b2-e0R5xJCS6YDTIyax7auGfVqu6IkEio0ixUtRVIR9et--1Vga7p-SYpQs8jKIMMvgmLWkK_OTA=s0-d-e1-ft#https://www.decodejava.com/python-recursion.png)

Let us understand recursion with a function which will return the factorial of the number.

    def factorial_recursive(n):
        if n == 1:                                    # Base case: 1! = 1
            return 1
        else:
            return n * factorial_recursive(n-1)       # Recursive case: n! = n * (n-1)!
    factorial_recursive(5)
    
    #output:
    120

In above code, the statement in else part shows the recursion, as the statement calls the function factorial_recursive( ) in which it resides.

![](https://www.mathwarehouse.com/programming/images/recusion-factorial-code-animated-gifs.gif)

### Advantages of Recursion
- Recursive functions make the code look clean and elegant.
- A complex task can be broken down into simpler sub-problems using recursion.
- Sequence generation is easier with recursion than using some nested iteration.

### Disadvantages of Recursion
- Sometimes the logic behind recursion is hard to follow through.
- Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
- Recursive functions are hard to debug.

# Inner function and its calling techniques
In Python, the concept of closure is applicable only to Nested Functions. Closures in Python are the inner functions that have access to variables declared/initialized inside an outer function (enclosing function) even after the outer function has been executed completely or removed from the memory. 

Whenever we print any variable inside an inner function, the Python interpreter searches for that variable declaration/initialization until four scopes. First, the local scope of the inner function, then the local scope of the enclosing function, then the global scope and at last the built-in module scope. So, the inner function can access the variables declared/initialized in all these four scopes as shown in the below example.

    def outer():
        b = 20  #variable inside the outer function
        def inner():
            c = 30  #variable inside the inner function
            print(b + c)
        inner() #call to inner() function
    #main() function
    outer() #call to outer() function

    #Output:
    50

**Execution order:**

![](https://i1.faceprep.in/Companies-1/closures-in-python.png)

Here, since the inner function is called from the outer function, the Python interpreter starts the execution of the inner function before the outer function completes its execution. The above-defined function becomes closure when we return the inner function instead of calling it from the outer function. 

### Defining Closures
Let us consider the same example, where we rewrite the function definition by returning the inner function from the outer function instead of calling it as shown below.

    def outer():
        b = 20  
        def inner():
            c = 30  
            print(b + c)
        return inner #returning inner() function

**Note:** When returning the inner function, there is no need for round brackets after the function name.

Since we are returning the inner function from the outer function, we need to declare a variable in the main() function to accept and store the function returned from the outer() function as shown below.

    #main() function
    result = outer() 
    print(result)
    print(type(result))

So, when we execute the below code, we get the output as,

    #Output:
    .inner at 0x7fadf75000d0>
    <class 'function'>

Here, the inner function returned from the outer function gets stored in the variable ‘result’. So, the variable ‘result’ has modified to a function and the same is evident in the result. Now, ‘result’ acts like a function, using which the inner function defined inside the outer function is called as shown below.

    def outer():
        b = 20  
        def inner():
            c = 30  
            print(b + c)
        return inner #returning inner() function
    #main() function
    result = outer() 
    result()

    #Output:
    50
It is assumed that a function completes its execution whenever it returns 0 or any values. Here in the above example, the outer() function returns the inner function. So, it has completed its execution. Once the outer function has completed its execution, we are calling the inner function from the main() function and still the inner() function is able to access the variable initialized inside the outer function. How is this happening?

Well!! When the Python interpreter detects the dependency of the inner function on the outer function, it stores the variables declared/initialized inside the outer function even if the outer function completes its execution (deleted from the memory). 

A function that has this property of accessing a variable declared/initialized inside the outer function even after the outer function has deleted from the memory is called a Closure.

#### When & Why do we need Python Closures?
Python Closures are used when there is a need for data hiding. Also, they are used to bind the data to a function. For instance, in the above code, we have returned the inner function from the outer function and stored (bind) it to the variable ‘result’ to call the inner function further. Similar to this we can bind any data to a function and use that function wherever required. 

# Returning multiple values from function

### Print/Return the result

The function can either print the result in the same function or return the result to the main() function from where it is being called.

|function having print statement|function having return statement|
|--|--|
|![](https://i1.faceprep.in/Companies-1/functions-print.gif)|![](https://i1.faceprep.in/Companies-1/functions-return-file.gif)|

Python functions have the ability to return multiple values. This can be done by separating the return values with a comma. Generally, Python packs multiple return values in the form of a single tuple and returns it.

Let’s understand better with an example, where the function concatenates the given two strings, repeats the first string two times and returns both the results using a single return statement.

    #program that returns multiple values to the main() function in the form of a tuple 
    def func(str1, str2):
        return str1 + str2, str1 * 2
    res = func("Vini", "patel")
    print(res)
    
    #Output:
    ('Vinipatel', 'ViniVini')

We can use multiple assignments to unpack the elements of the tuple as shown below.

    #program that unpacks multiple return values using multiple variables
    def func(str1, str2):
        return str1 + str2, str1 * 2
    concat, repit = func("VINI", "PATEL")
    print(concat) 
    print(repeat)

    #Output:
    VINIPATEL
    VINIVINI

Here, the result after concatenation is stored in the variable ‘concat’ and the result after repetition is stored in the variable ‘repeat’. 
