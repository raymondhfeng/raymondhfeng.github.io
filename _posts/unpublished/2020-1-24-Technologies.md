---
layout: post
title: Technologies 
published: false
---

Taking a step back to look at the "big picture".

- Scala
- Ruby on Rails
- Django
- redis
- Google Cloud Platform
- AWS S3

- Pytorch

- Python
	* Explain `join()` and `split()` in Python and how did you use it in your last project?
		- I usually use `join()` and `split()` to convert between strings and arrays, as you cannot modify a string by index. For example, writing a custom `MyString` class would probably necessitate these functions, as modifying your string by index requires `split()`, and then returning back to string requires `join()`. 
	* How did you use `del` and `remove()` in your Python projects? Feel free to highlight couple of instances. 
		- In an array, `del` removes from a certain index, whereas `remove()` removes the first matching value.
	* What different file processing modes have you used in your Python projects? (hint: define your project here!)
		- `r`,`w`,`rw`,`a`. I mainly use the `w` mode to write to csv files. One project that I used this on was a model to predict if the Cal Football Team should go for a fourth down coversion.
	* When and where did you work with `try`, `release`, and `finally` in your Python work experience? 
		- Input verification. When you don't want to crash the program when checking for null or invalid inputs, you throw and exception, and catch it higher up in the call stack and print out the proper message, and terminate the program. 
	* Have you ever used the enumerate() function in Python? If so, where and for what?
		- When I need a convenient way to number off elements in a list, I will use the `enumerate()` method. 
	* Have you deep copied a list in Python? Was it different than a shallow copy? Please explain with your project examples.
		- When I want to concatenate two arrays, I'll make a shallow copy because I don't need to copy the objects, just their pointers. However, if I want to make a complete copy of an object, I'll use deep copies, such as when I am copying a custom defined data structure. 
	* Have you dealt with memory management in any of your Python projects? If yes, what was the scope and functionality of the memory management?
		- I have only dealt with memory management in C, which I will use if I need higher performance code. 
	* How have you used a 'generator' in your Python projects? Explain with an example.
		- I've used generator's in Java when working with databases, especially when working with streaming algorithms such as joins, where all the data cannot fit into memory. 
	* Explain List, Tuple, Set, and Dictionary and provide at least one instance where each of these collection types can be used.
		- A list is a data structure that allows for constant time accesses, usually implemented using an array. A tuple is an immutable list, and is useful for returning more than 1 values for recursive calls. Sets are lists with no order and no duplicates, and are useful for storing visited nodes for tree/graph traversal algorithms such as DFS. A dictionary is a mapping from keys to values, and can be implemented in a hash map. Dictionaries can be used whenever you need a mapping.  
	* 
- Java
- C
- C++
- Go
- Scheme
- Perl

- HTML
- CSS
- Javascript

- MongoDB
- Postgres
- SQLite

- MPP databases
	* Redshift
	* Teradata
	* Vertica

- Agile methodology

- AWS Services
	* S3, Lambda, Kinesis, Sagemaker
- DevOps Tools
	* Jenkins, CircleCI, Docker
- Mobile App Technology
	* IOS, Android, React-ndative

## Software framework
- An abstraction in which software providing generic functionality can be selectively changed by additional user-written code, thus providing application-specific software. 
- Frameworks vs normal libraries: 
	* inversion of control: flow of control dictated by framework, not caller
	* extensibility: user can extend the framework
	* non-modifiable framework code: can extend framework, but not modify code

- .Net framework
	* Large class library called Framework Class Library
	* Language interoperability: each language can use code written in other languages
	* Programs operate in a software environment as opposed to a hardware environment. The software environment is called CLR, common language runtime. 
		- CLR is an application virtual machine that provides security, memory management, and exception handling
	* Thus, computer code written using the .NET framework is called "managed code". 
	* CLI, common language infrastructurejonn

- MVC (Model-View-Controller)
	* Software design pattern. 
	* Commonly used for developing user interfaces
	* Model: central component, the application's dynamic data structure
	* View: Any representation of information such as chart, diagram, or table
	* Controller: Accepts input and coverts it to commands for the model or view
	* Advantages: Simultaneous development, high cohesion, loose coupling, ease of modification, multiple views for a model. 
	* Disadvantages: Code navigability, multi-artifact consistency, undermined by inevitable clustering, excessive boilerplate, pronounced learning curve, lack of incremental benefit.


## Finance
- Overarching theme of my undergraduate studies: the intersection of math and computer science, specifically focused on the lucrative aspects of computational finance. 

