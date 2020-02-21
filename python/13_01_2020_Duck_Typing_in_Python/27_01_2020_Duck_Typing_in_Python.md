# Duck Typing in Python

Before we started with **Duck Typing** lwt'a have a look at the difference between static type and dynamic type.

## Dynamic Typing 

**In Dynamic Typing, type checking is performed at runtime.** 

**For example,** 
Python is a dynamically typed language. It means that the type of a variable is allowed to change over its lifetime. Other dynamically typed languages are -Perl, Ruby, PHP, Javascript etc.

Let’s take a Python code example to see if a variable can change type:

    ## variable a is assigned to a string 
    a ="hello"
    print(type(a)) 

    ## variable a is assigned to an integer 
    a = 5
    print(type(a)) 

In Python, we don’t really have a good idea of what are the types that this function deals with and also what the type of the return value is going to be.

## Static Typing 

Static Typing is opposite to Dynamic Typing. **In Static Typing, type checking is performed during compile time.**

It means that the type of a variable is known at compile time. For some languages, the programmer must specify what type each variable is (e.g C, C++, Java), other languages offer some form of type inference(e.g. Scala, Haskell).

With Static Typing, variables generally are not allowed to change types.

Let’s look at a simple example from a statically typed language. Consider the following Java snippet;

    String a; 
    a = "Java is good"; 

The first line declares that the variable “a” is bound to the string type at compile time. In the second line, “a” is assigned a value which is not a string object. 
For example, if we say, a =5, the compiler would raise an error because of incompatible types.

## Duck Typing 

Python’s `duck typing`, a special case of dynamic typing, uses techniques characteristic of polymorphism, including `late binding` and `dynamic dispatch`. 

The term `“duck typing”` is derived from a quote of writer `James Whitcomb Riley`: **“When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck.”**

The use of duck typing is concerned with establishing the suitability of an object for a specific purpose. When using normal typing this suitability is determined by the type of an object alone, but with duck typing the presence of methods and properties are used to determine suitability rather than the actual type of the object in question. `That is to say, you check whether the object quacks like a duck and walks like a duck rather than asking whether the object is a duck.`

`Polymorphism` without `inheritance` in the form of `duck typing` as available in Python due to its `dynamic typing system`. 

This means that as long as the classes contain the same methods the Python interpreter does not distinguish between them, as the only checking of the calls occurs at run-time.

    class Duck:
        def quack(self):
            print("Quack!")
        def feathers(self):
            print("The duck has white and gray feathers.")

    class Person:
        def quack(self):
            print("The person imitates a duck.")
        def feathers(self):
            print("The person takes a feather from the ground and shows it.")
        def name(self):
            print("Vini patel")

    def in_the_forest(obj):
        obj.quack()
        obj.feathers()

    donald = Duck()
    vini = Person()

    in_the_forest(donald)
    in_the_forest(vini)

    #The output is:

    Quack!
    The duck has white and gray feathers.
    The person imitates a duck.
    The person takes a feather from the ground and shows it.

 Duck-typing emphasis what the object can really do, rather than what the object is.


# Decoratoers in Python

### What Is Python Decorator?

`Decorators` are a callable entity in Python that allows us to make modifications to functions or classes. The decorator works in an `abstract style` to extend or completely replace the behavior of an object.

By understanding how to create decorators, you make your `code extensible and more readable`. Also, you get the functions tailored to your needs without even changing their definitions.

#### Decorator Syntax

Follow the below style:

    def decoratorFunc(args):
        # Code to you want to execute
        ...

    @decoratorFunc
    def existingFunction(args):
        # Code that you want to decorate
        ...

Alternatively, you can try this way:

    existingFunction = decoratorFunc(existingFunction)

### How Does Decorator Work In Python?

- Mainly, decorators are a construct that wraps a function, gives it a new functionality without changing the original code.

- They return the output which may differ from the original behavior of the function.

- They are good to use when a function has to operate differently in different situations.

### Create Your Decorator:

A decorator is a function that may or may not return a function object.

We place it on top of the function that we want to decorate and pre-fix it with a `@ sign.`

So, let’s first create the decorator function.

    def decoratorFunc(fn):
        return 10

The above decorator function returns an integer instead of a function.

So when you apply it to a function, it would get `overridden` altogether.

Check below how to specify a decorator to a function.

    @decoratorFunc
    def existingFunc():
        print("Hello World!")

Let’s now bring all the pieces together.

    def decoratorFunc(fn):
        return 10

    @decoratorFunc
    def existingFunc():
        print("Hello World!")

    existingFunc()

When you run the above code, the following error occurs.

    line 8, in 
        existingFunc()
    TypeError: 'int' object is not callable

It is because the decorator replaced the existing function and forcing it to return “10” which is an integer, not a callable object.

**_NOTE – the decorator’s return value replaces the function, i.e., existingFunc._**

By the way, if you want to run the function that we decorated, then make the decorator return it. Check the below code.

    def decoratorFunc(fn):
        def callExistingFunc():
            print("%s was called." % fn)
            fn()
        return callExistingFunc

    @decoratorFunc
    def existingFunc():
        print("Hello World!")

    existingFunc()

In the above example, our decorator function is returning a function which prints the name of the decorated function and executes it.

The result of execution is as follows:

    <function existingFunc at 0x0000000000705158> was called.
    Hello World!

**Flowchart:**
The following diagram attempts to simplify the decorator concept for you.

![](https://cdn.techbeamers.com/wp-content/uploads/2019/03/Decorator-flow-in-python.png)

![](https://ci3.googleusercontent.com/proxy/dAxONStvWLsxZaj8P2Gy9dWmYQ9HKOwK7x6O-Y3qODXoMXJPzdkhH3AyKiJdonCFI3iBvb0ug0sXwQJSAyuEp6IUOp0=s0-d-e1-ft#http://kleiber.me/img/decorator_tutorial_code.png)

## Chaining Decorators

We can decorate a function as many times as desired. In such a case, the decorators create a chain effect.

Typically, the decorator at the top hands over the control to the next, and continues in this way.

For illustration, check out the following code:

#### Display Multiple Lines Using Chaining:

    def Chaining_of_decorators(func):
        print("This is an example of chaining of decorators implementation.")
         
    def Decorator_demo(func):
        print("This tutorial is about Decorators.")
         
    print("This is a decorated function.")

    @Chaining_of_decorators
    @Decorator_demo
    def hello():
        print("Hello World!")
    
    hello()
    # Output:

    This is a decorated function.
    This tutorial is about Decorators.
    This is an example of chaining of decorators implementation.
    
# Practical Use of Decorators 

Python’s decorators allow you to extend and modify the behavior of a callable (functions, methods, and classes) without permanently modifying the callable itself.

Any sufficiently generic functionality you can “tack on” to an existing class or function’s behavior makes a great use case for decoration. 

This includes:
- logging
- enforcing access control and authentication
- instrumentation and timing functions
- rate-limiting
- caching; and more.

#### how decorators can benefit you in your day-to-day work as a Python developer. 

**Here’s an example:**

Imagine you’ve got `30 functions` with business logic in your report-generating program. One rainy Monday morning your boss walks up to your desk and says:

>“Happy Monday! Remember those TPS reports? I need you to add input/output logging to each step in the report generator. XYZ Corp needs it for auditing purposes. Oh, and I told them we can ship this by Wednesday.”

Depending on whether or not you’ve got a solid grasp on Python’s decorators, this request will either send your blood pressure spiking—or leave you relatively calm.

Without decorators you might be spending the next three days scrambling to modify each of those 30 functions and clutter them up with manual logging calls. Fun times.

If you do know your decorators, you’ll calmly smile at your boss and say:

>“Don’t worry Jim, I’ll get it done by 2pm today.”

Right after that you’ll type the code for a generic @audit_log decorator (that’s only about 10 lines long) and quickly paste it in front of each function definition. Then you’ll commit your code and grab another cup of coffee.Decorators can be that powerful 🙂 .

I’d go as far as to say that understanding decorators is a milestone for any serious Python programmer. They require a solid grasp of several advanced concepts in the language—including the properties of [First class functions](https://dbader.org/blog/python-first-class-functions).

# Exception Handling

![](https://hub.packtpub.com/wp-content/uploads/2019/12/image2.png)

Just like Java, exceptions handling in Python is no different. It is a code embedded in a `try block` to run exceptions. Compare that to Java where `catch` clauses are used to catch the Exceptions. The same sort of Catch clause is used in Python that begins with `except`. Also, custom-made exception is possible in Python by using the `raise` statement where it forces a specified exception to take place.

### Reason to use exceptions

Errors are always expected while writing a program in Python which requires a backup mechanism. Such a mechanism is set to handle any encountered errors and not doing so may crash the program completely.

The reason to equip python program with the exception mechanism is to set and define a backup plan just in case any possible error situation erupts while executing it.

#### Example with try & except:

    my_dict={1:'Alex',2:'Ronald'}

    try:
        print(my_dict[3]) # 3rd element is not there 
    except :
        print (" some error occured ")

    #Output is here
    some error occured 

We can catch some specific error and display appropriate message.

    my_dict={1:'Alex',2:'Ronald'}
    
    try:
        print(my_dict[3])
    except (KeyError):
        print (" This is a key error  ")
    except :
        print (" some error occured ")

    #Output is here
    This is a key error

#### finally

The code block within finally code block is executed in all conditions ( error or no error )

    my_dict={1:'Alex',2:'Ronald'}

    try:
        print(my_dict[3])
    except (KeyError):
        print (" This is a key error  ")
    except :
        print (" some error occured ")
    finally :
        print ( " I came out " )

    #Output is here
    This is a key error  
    I came out 

#### else

If there is no error then code block within else will be executed.

    my_dict={1:'Alex',2:'Ronald'}

    try:
        print(my_dict[2])
    except (KeyError):
        print (" This is a key error  ")
    except :
        print (" some error occured ")
    else :
        print ( " within else ")

    #Output is here
    Ronald
    within else 


#### else with finally

    my_dict={1:'Alex',2:'Ronald'}

    try:
        print(my_dict[2])
    except (KeyError):
        print (" This is a key error  ")
    except :
        print (" some error occured ")
    else :
        print ( " within else ")
    finally:
        print ( " I am wihtin finally")

    #Output
    Ronald
    within else 
    I am wihtin finally

##### Examples of exception handling

We will separate integer part from a string.

    my_str="Welcome to 45 town "
    my_list=my_str.split() # Create a list using split string method
    for i in my_list:      # iterating through list
        try:
            r=1/int(i)     # Generate error if i is not integer
            print("The interger is :",i)
        except:
            print ("not integer : ",i) # Print only if integer 

    #Output is here
    not integer :  Welcome
    not integer :  to
    The interger is : 45
    not integer :  town

#### User generated exception by using raise

In the code below there is nothing wrong with syntax but user can create its own exception by using raise

    x=13
    if x >10:
        raise Exception ('Value of x is greater than 10 ')
    else:
        print('Value is fine ')