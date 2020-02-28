# Introduction of Python

![](https://www.python.org/static/community_logos/python-logo.png)

**Python** is a widely used general-purpose, high-level programming language. It was initially designed by **Guido van Rossum** in 1991 and developed by **Python Software Foundation**. It was mainly developed for emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code. The inspiration for the name came from BBC’s TV Show – **‘Monty Python’s Flying Circus’**, as he was a big fan of the TV show and also, he wanted a short, unique and slightly mysterious name for his invention and hence he named it **Python!**

## Implementation of python

![](https://uploads.toptal.com/blog/image/128/toptal-blog-A.png)

#### CPython:
The default implementation of the Python programming language is Cpython. As the name suggests Cpython is written in C language. Cpython compiles the python source code into intermediate bytecode, which is executed by the Cpython virtual machine. CPython is distributed with a large standard library written in a mixture of C and Python. CPython provides the highest level of compatibility with Python packages and C extension modules. All versions of the Python language are implemented in C because CPython is the reference implementation. Some of the implementations which are based on CPython runtime core but with extended behavior or features in some aspects are Stackless Python, wpython, MicroPython.
Stackless Python – CPython with an emphasis on concurrency using tasklets and channels (used by dspython for the Nintendo DS

#### Jython:
Jython is a Java implementation of Python that combines expressive power with clarity. Jython is freely available for both commercial and non-commercial use and is distributed with source code under the PSF License v2. 
**Jython is complementary to Java and is especially suited for the following tasks:**
- **Embedded scripting** - Java programmers can add the Jython libraries to their system to allow end users to write simple or complicated scripts that add functionality to the application.
- **Interactive experimentation** - Jython provides an interactive interpreter that can be used to interact with Java packages or with running Java applications. This allows programmers to experiment and debug any Java system using Jython.
- **Rapid application development** - Python programs are typically 2-10x shorter than the equivalent Java program. This translates directly to increased programmer productivity. The seamless interaction between Python and Java allows developers to freely mix the two languages both during development and in shipping products.

Here is an example of running Python code inside a simple Java application

    import org.python.util.PythonInterpreter;
    
    public class JythonHelloWorld {  public static void main(String[] args) {
        try(PythonInterpreter pyInterp = new PythonInterpreter()) {
            pyInterp.exec("print('Hello Python World!')");
            }
        }
    }

Here is an example of using Java from Python code
    
    from java.lang import System # Java import

    print('Running on Java version: ' + System.getProperty('java.version'))
    print('Unix time from Java: ' + str(System.currentTimeMillis()))
    
#### IronPython:
IronPython is an excellent addition to the .NET Framework, providing Python developers with the power of the .NET framework. Existing .NET developers can also use IronPython as a fast and expressive scripting language for embedding, testing, or writing a new application from scratch.

### PyPy:
PyPy has been used to mean two things. The first is the RPython translation toolchain for generating interpreters for dynamic programming languages. And the second is one particular implementation of Python produced with it. Because RPython uses the same syntax as Python, this generated version became known as Python interpreter written in Python. It is designed to be flexible and easy to experiment with.

To make it more clear, we start with source code written in RPython, apply the RPython translation toolchain, and end up with PyPy as a binary executable. This executable is the Python interpreter.

Double usage has proven to be confusing, so we’ve moved away from using the word PyPy to mean both toolchain and generated interpreter. Now we use word PyPy to refer to the Python implementation, and explicitly mention RPython translation toolchain when we mean the framework.


# Features of python
There are many features in Python, some of which are discussed below –
- **Easy to code:**
Python is high level programming language. Python is very easy to learn language as compared to other language like c, c#, java script, java etc. It is very easy to code in python language and anybody can learn python basic in few hours or days. It is also developer-friendly language.
- **Free and Open Source:**
Python language is freely available at official. Since, it is open-source, this means that source code is also available to the public. So, you can download it as, use it as well as share it.
- **Object-Oriented Language:**
One of the key features of python is Object-Oriented programming. Python supports object-oriented language and concepts of classes, objects encapsulation etc.
- **GUI Programming Support:**
Graphical Users interfaces can be made using a module such as PyQt5, PyQt4, wxPython or Tk in python. PyQt5 is the most popular option for creating graphical apps with Python.
- **High-Level Language:**
Python is a high-level language. When we write programs in python, we do not need to remember the system architecture, nor do we need to manage the memory.
- **Extensible feature:**
Python is a Extensible language. we can write our python code into c or c++ language and also, we can compile that code in c/c++ language.
- **Python is Portable language:**
Python language is also a portable language. For example, if we have python code for windows and if we want to run this code on other platform such as Linux, Unix and Mac then we do not need to change it, we can run this code on any platform.
- **Python is Integrated language:**
Python is also an Integrated language because we can easily integrated python with other language like c, c++ etc.
- **Interpreted Language:**
Python is an Interpreted Language. because python code is executed line by line at a time. like other language c, c++, java etc there is no need to compile python code this makes it easier to debug our code. The source code of python is converted into an immediate form called bytecode.

- **Large Standard Library:**
Python has a large standard library which provides rich set of module and functions so you do not have to write your own code for every single thing. There are many libraries present in python for such as regular expressions, unit-testing, web browsers etc.
- **Dynamically Typed Language:**
Python is dynamically-typed language. That means the type (for example- int, double, long etc) for a variable is decided at run time not in advance. Because of this feature we don’t need to specify the type of variable.

# Versions of Python
![](https://media.geeksforgeeks.org/wp-content/uploads/20190502023317/TIMELINE.jpg)

# Toolchain of python application
Toolchain of python is all about how python application internally works.

Python first compiles your **source code (.py file)** into a format known as **byte code (.pyc file)** . Compilation is simply a translation step, and byte code is a lower-level, and platform-independent, representation of your source code. Compiled code is usually stored in .pyc files , and is regenerated when the source is updated, or when otherwise necessary.

The bytecode (.pyc file) is loaded into the Python runtime and interpreted by a **Python Virtual Machine** , which is a piece of code that reads each instruction in the bytecode and executes whatever operation is indicated. Byte code compilation is automatic, and the PVM is just part of the Python system that you have installed on your machine. The PVM is always present as part of the Python system , and is the component that truly runs your scripts. Technically, it's just the last step of what is called the Python interpreter. And this is how the process is done (very general). Of course, there are optimizations and caches to improve the performance.

Each time an interpreted program is run, the interpreter must convert source code into machine code and also pull in the runtime libraries . This conversion process makes the program run slower than a comparable program written in a compiled language. Python do something clever to improve its performance . It compiles to bytecode (.pyc files) the first time it executes a file. This improves substantially the execution of the code next time the module is imported or executed.

![](https://3.bp.blogspot.com/--gMhzeZWr8M/VdDrUsbdl4I/AAAAAAAAIxI/MSTaj_B_GRY/s640/python_inpreted.PNG)

Now, here one question arise that,
#### **How we can see .pyc file ???** 

So, when a module is imported for the first time, or when the source is more recent than the current compiled file, a .pyc file containing the compiled code will usually be created in the same directory as the .py file. When you run the program next time, Python uses this file to skip the compilation step.

One reason that a .pyc file may not be created is permissions problems with the directory. This can happen, for example, if you develop as one user but run as another, such as if you are testing with a web server. Creation of a .pyc file is automatic if you’re importing a module and Python has the ability (permissions, free space, etc.) to write the compiled module back to the directory.

Running a script is not considered an import and no .pyc will be created. For example, if you have a script file abc.py that imports another module xyz.py, when you run abc, xyz.pyc will be created since xyz is imported, but no abc.pyc file will be created since abc.py isn’t being imported.

If you need to create a .pyc file for a module that is not imported, you can use the py_compile and compileall modules.

The py_compile module can manually compile any module. One way is to use the py_compile.compile function in that module interactively:

    >>> import py_compile
    >>> py_compile.compile('abc.py')
This will write the .pyc to the same location as abc.py (you can override that with the optional parameter cfile).



# Build Process of Python Application

So,if we are talking about the build process in python then there will be question in our mind that, Is python compiled or an interpreted language ???

**Is Python compiled? Yes. Is Python interpreted? Yes. Sorry, the world is complicated...**

An important aspect of Python’s compilation to bytecode is that it’s entirely implicit. You never invoke a compiler, you simply run a .py file. The Python implementation compiles the files as needed. This is different than Java, for example, where you have to run the Java compiler to turn Java source code into compiled class files. For this reason, Java is often called a compiled language, while Python is called an interpreted language. But both compile to bytecode, and then both execute the bytecode with a software implementation of a virtual machine.

Another important Python feature is its interactive prompt. You can type Python statements and have them immediately executed. This interactivity is usually missing in “compiled” languages, but even at the Python interactive prompt, your Python is compiled to bytecode, and then the bytecode is executed. This immediate execution, and Python’s lack of an explicit compile step, are why people call the Python executable “the Python interpreter.”


# Installation of Anaconda Distribution and other python IDE 

## Installation of Anaconda

1. Download the Anaconda from here -> [Download Anaconda](https://www.anaconda.com/distribution/#windows)

![](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1528926570/1_anacondaWebsite_RED_lqqmky.png)

2. Double click the installer to launch.

![](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1528926571/2_WaitTillDownloadDone_RED_rscmes.png)

3. When the screen below appears, click on Next.

![](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1528926579/3_OpeningScreen_RED_t9x3rr.png)

4. Read the licensing terms and click “I Agree”.                                                                            

![](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1528926834/4_SecondOpeningScreen_RED_u48y44.png)

5. Select an install for “Just Me” unless you’re installing for all users (which requires Windows Administrator privileges) and click Next.

![](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1528926866/justMeAfterI_Agree_RED_xb0fpf.png)

6. Select a destination folder to install Anaconda and click the Next button.

![](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1528926571/6_InstallationLocation_RED_hbx3zj.png)

7. This is an important part of the installation process. The recommended approach is to not check the box to add Anaconda to your path. This means you will have to use Anaconda Navigator or the Anaconda Command Prompt (located in the Start Menu under "Anaconda") when you wish to use Anaconda (you can always add Anaconda to your PATH later if you don't check the box). If you want to be able to use Anaconda in your command prompt (or git bash, cmder, powershell etc), please use the alternative approach and check the box.

![](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1528926970/AnacondaOptions_e8jugh.png)

8. Click on Next.

![](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1528926583/8_Completed_RED_q2idx4.png)

9. Click on Finish.

![](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1528926585/10_finished_RED_ugje2b.png)

## Installation of other python IDE (pycharm)

1. To download PyCharm visit the website -> [Download PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)
![](https://www.guru99.com/images/Pythonnew/Python2.5.png)

2. Once the download is complete, run the exe for install PyCharm. The setup wizard should have started. Click “Next”.

![](https://www.guru99.com/images/Pythonnew/Python2.6.png)

3. On the next screen, Change the installation path if required. Click “Next”.

![](https://www.guru99.com/images/Pythonnew/Python2.7.png)

4. On the next screen, you can create a desktop shortcut if you want and click on “Next”.

![](https://www.guru99.com/images/Pythonnew/Python2.8.png)

5. Choose the start menu folder. Keep selected JetBrains and click on “Install”.

![](https://www.guru99.com/images/Pythonnew/Python2.9.png)

6.  Wait for the installation to finish.

![](https://www.guru99.com/images/Pythonnew/Python2.10.png)

7.  Once installation finished, you should receive a message screen that PyCharm is installed. If you want to go ahead and run it, click the “Run PyCharm Community Edition” box first and click “Finish”.

![](https://www.guru99.com/images/Pythonnew/Python2.11.png)

8.  After you click on "Finish," the Following screen will appear.

![](https://www.guru99.com/images/Pythonnew/Python2.last.png)
 


