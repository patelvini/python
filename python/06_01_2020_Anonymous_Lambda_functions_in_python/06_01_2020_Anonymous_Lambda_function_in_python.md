# Anonymous / Lambda Functions in Python

**lambda** is an alternative way of defining function. You can define function inline using lambda. It means you can apply a function to some data using a single line of python code. 

It is called `anonymous` function as the function can be defined `without its name`. 

They are a part of functional programming style which focus on readability of code and avoids changing mutable data.

### Why should we use lambda functions?
We can use lambda functions as anonymous functions inside any normal functions of python. This is the actual superpower of lambda functions. Because of its simplicity, you can write a lambda function with no hassle. 

![](https://qph.fs.quoracdn.net/main-qimg-43b4eb0d62e60001ae3c15c9e90c8421)

### Syntax:
The syntax of lambda functions is shown below:
>**lambda arguments: expression**

![](https://www.educative.io/api/edpresso/shot/6565495459282944/image/6707306488135680)

Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called **“lambda”.***

Lambda functions take any number of arguments but only has `one expression`, the result of this expression is returned.

**Example:**

![](https://0xbharath.github.io/python-foundations/img/lambda.png)

### What is the difference between lambda functions and normal functions in python?

![](https://miro.medium.com/max/980/1*5Q43ntrN1TmBYOm3DU-lNw.png)

### Python Lambda Functions Examples

First, let us see how to write a lambda function to add two numbers. As we already discussed, the lambda function can have more than one argument. To add two numbers, we need two arguments. Those two arguments have to be written after the ‘lambda’ keyword as comma-separated without any round brackets.

    f = lambda a, b: a + b

    #main() function
    res = f(6, 4)
    print(res)
    
    #Output:
    10

Consider the below-given code where the built-in function ‘format’ formats the given input number to a hexadecimal value.

    #Lambda function to format the given input number to a hexadecimal value
    f = lambda a: format(a, 'x')

    #main() function
    res = f(12)
    print(res)
    
    #Output:
    c
    
### Use of lambda function with Filter, Map and Reduce

![](https://cdn.techbeamers.com/wp-content/uploads/2018/09/Python-Lambda-A-Function-without-a-Name.png)

**_more detailed examples will be given further in filter, map and reduce_**

# Filter Map Reduce concept in Python
Map, Filter, and Reduce are paradigms of functional programming. They allow the programmer (you) to write simpler, shorter code, without neccessarily needing to bother about intricacies like loops and branching.

**map(), filter() and reduce()** are inbuilt functions of Python. 

These functions enable the functional programming aspect of Python. In functional programming, the arguments passed are the only factors that decide upon the output. 

These functions can take any other function as a parameter and can be supplied to other functions as parameters as well.

## Map
The map() function is a type of higher-order. This function takes another function as a parameter along with a sequence of iterables and returns an output after applying the function to each iterable present in the sequence.

### Syntax:

>**map(function, iterables)**

Here, the function defines an expression that is in turn applied to the iterables. The map function can take user-defined functions as well as lambda functions as a parameter.

### User-defined functions within map(): 

The map() function can take user-defined functions as parameters. The parameters of these functions are exclusively set by the user or the programmer.

**Example:**

    def newfunc(a):
        return a*a
    x = map(newfunc, (1,2,3,4)) #x is the map object
    print(x)
    print(set(x))

    #OUTPUT:
    <map object at 0x00000284B9AEADD8>
    {16, 1, 4, 9}

As you can see, `x` is a `map object`. The next part output displays the map function taking newfunc() as its parameter and then it applies the a*a to all the iterables. As a result, the values of all iterables are multiplied by themselves and returned.

_**NOTE: The output is not in order of the values of the iterables because I have used the set() function. You can also use the list() or tuple() functions.**_

**Example:**

    def newfunc(a):
        return a*a
    x = map(newfunc, (1,2,3,4)) #x is the map object
    print(x)
    print(list(x))
    
    #OUTPUT:
    <map object at 0x00000284B9AEA940>
    [1, 4, 9, 16]

**You can pass more than one list of parameters as well.
Example:**

    def func(a, b):
        return a + b

    a = map(func, [2, 4, 5], [1,2,3])
    print(a)
    print(tuple(a))
    
    #OUTPUT:
    <map object at 0x00000284B9BA1E80>
    (3, 6, 8)

Now let us see how you can use lambda functions within the map() function.

### Lambda functions within map():

Lambda functions are functions that do have any name. These functions are often supplied as parameters to other functions. Now let us try to embed lambda functions within the map() function.

**Example:**

    tup= (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
    newtuple = tuple(map(lambda x: x+3 , tup)) 
    print(newtuple)

    #OUTPUT:   
    (8, 10, 25, 100, 57, 65, 80, 26, 76, 64)

The above output is a result of applying the lambda expression (x+3) to each item present in the tuple.

## Filter

The **filter()** function is used to create an output list consisting of values for which the function returns true. 
**Syntax:**

>**filter(function, iterables)**

Just like map(), this function can be used can also take user-defined functions as well as lambda functions as a parameter.

**Example:**

    def func(x):
        if x>=3:
            return x
    y = filter(func, (1,2,3,4))  
    print(y)
    print(list(y))

    #OUTPUT:
    <filter object at 0x00000284B9BBCC50>
    [3, 4]

As you can see, y is the filter object and the list is a list of values that are true for the condition (x>=3).

### Using lambda within filter():
The lambda function that is used as a parameter actually defines the condition that is to be checked.

**Example:**

    y = filter(lambda x: (x>=3), (1,2,3,4))
    print(list(y))
    
    #OUTPUT:   
    [3, 4]

The above code produces the same output as the previous function.

## Reduce
The **reduce()** function, as the name describes, applies a given function to the iterables and returns a single value.

![](https://ucarecdn.com/dd8ea9fe-af3e-4ebb-ba9a-f1f01b5158d6/)

The syntax of this function is as follows:

**Syntax:**

>**reduce(function, iterables)**

The function here defines what expression needs to be applied to the iterables. This function needs to be imported from the functools module.

**Example:**

    from functools import reduce
    reduce(lambda a,b: a+b,[23,21,45,98])
    
    #OUTPUT:  
    187

In the above example, the reduce function consecutively adds each iterable present in the list and returns a single output.

**The map(), filter() and reduce() functions in Python can be used along with each other.**

### Using map(),filter() and reduce() functions along with each other:

When you do this, the internal functions are first solved and then the outer functions operate on the output of the internal functions.

Let us first try passing the filter() function as a parameter to the map() function.

#### Using filter() within map():

The code given below first checks for the condition (x>=3) to be true for the iterables. Then, the output is mapped using the map() function.

**Example:**

    c = map(lambda x:x+x,filter(lambda x: (x>=3), (1,2,3,4)))
    print(list(c))
    #OUTPUT:   
    [6, 8]

If you filter out integers greater than or equal to 3 from the given tuple, you get [3,4] as the result. Then if you map this using(x+x) condition, you will get [6,8], which is the output.

#### Using map() within filter():

When you use the map() function within filter() function, the iterables are first operated upon by the map function and then the condition of filter() is applied to them.

**Example:**

    c = filter(lambda x: (x>=3),map(lambda x:x+x, (1,2,3,4))) #lambda x: (x>=3)
    print(list(c))
    
    #OUTPUT:   
    [4, 6, 8]

#### Using map() and filter() within reduce():
The output of the internal functions is reduced according to the condition supplied to the reduce() function.

**Example:**

    d = reduce(lambda x,y: x+y,map(lambda x:x+x,filter(lambda x: (x>=3), (1,2,3,4)))) 
    print(d)
    
    #OUTPUT:    
    14

The output is a result of [6,8] which is the result of the internal map() and filter() functions.

# reduce() vs accumulate() 

Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. But there are differences in the implementation aspects in both of these.

**reduce() is defined in “functools” module, accumulate() in “itertools” module.**

reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a list containing the intermediate results. The last number of the list returned is summation value of the list.
reduce(fun,seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.

    # python code to demonstrate summation  
    # using reduce() and accumulate() 
  
    # importing itertools for accumulate() 
    import itertools 
  
    # importing functools for reduce() 
    import functools 
  
    # initializing list  
    lis = [ 1, 3, 4, 10, 4 ] 
  
    # priting summation using accumulate() 
    print ("The summation of list using accumulate is :",end="") 
    print (list(itertools.accumulate(lis,lambda x,y : x+y))) 
  
    # priting summation using reduce() 
    print ("The summation of list using reduce is :",end="") 
    print (functools.reduce(lambda x,y:x+y,lis)) 
    
    #Output:

    The summation of list using accumulate is :[1, 4, 8, 18, 22]
    The summation of list using reduce is :22
 