[[Python Variables]]

## Many Values to Multiple Variables

Python allows you to assign values to multiple variables in one line:

### Example

```python
x, y, z = "Orange", "Banana", "Cherry"  
print(x)  
print(y)  
print(z)
```

## One Value to Multiple Variables

And you can assign the _same_ value to multiple variables in one line:

### Example

```python
x = y = z = "Orange"  
print(x)  
print(y)  
print(z)
```

## Unpack a Collection

If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called _unpacking_.
### Example

Unpack a list:

```python
fruits = ["apple", "banana", "cherry"]  
x, y, z = fruits  
print(x)  
print(y)  
print(z)
```

