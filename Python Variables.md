[[Python Syntax]] 

## Variables
Variables are containers for storing data values.

---

## Creating Variables
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.

### Example
```python
x = 5  
y = "John"  
print(x)  
print(y)
```

Variables do not need to be declared with any particular _type_, and can even change type after they have been set.
### Example

```python
x = 4       # x is of type int  
x = "Sally" # x is now of type str  
print(x)
```

## Casting
If you want to specify the data type of a variable, this can be done with casting.
### Example

```python
x = str(3)    # x will be '3'  
y = int(3)    # y will be 3  
z = float(3)  # z will be 3.0
```

## Get the Type
You can get the data type of a variable with the `type()` function.
### Example

```python
x = 5  
y = "John"  
print(type(x))  
print(type(y))
```

## Single or Double Quotes?
String variables can be declared either by using single or double quotes:
### Example

```python
x = "John"  
# is the same as  
x = 'John'
```

## Case-Sensitive
Variable names are case-sensitive.
### Example
This will create two variables:

```python
a = 4  
A = "Sally"  
#A will not overwrite a
```