[[Python Syntax]] 

# Python Comments

---

Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.

---

## Creating a Comment

Comments starts with a `#`, and Python will ignore them:

### Example[Get your own Python Server](https://www.w3schools.com/python/python_server.asp "W3Schools Spaces")

```python
#This is a comment  
print("Hello, World!")
```

Comments can be placed at the end of a line, and Python will ignore the rest of the line:
### Example

```python
print("Hello, World!") #This is a comment
```

[Try it Yourself »](https://www.w3schools.com/python/trypython.asp?filename=demo_comment2)

A comment does not have to be text that explains the code, it can also be used to prevent Python from executing code:
### Example

```python
#print("Hello, World!")  
print("Cheers, Mate!")
```

## Multi line Comments

Python does not really have a syntax for multi line comments.

To add a multi line comment you could insert a `#` for each line:

### Example

```python
#This is a comment  
#written in  
#more than just one line  
print("Hello, World!")
```

Or, not quite as intended, you can use a multi line string.
Since Python will ignore string literals that are not assigned to a variable, you can add a multi line string (triple quotes) in your code, and place your comment inside it:
### Example

```python
"""  
This is a comment  
written in  
more than just one line  
"""  
print("Hello, World!")
```

