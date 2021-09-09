# Python Typing

https://docs.python.org/3/library/typing.html

## Basic Types

Int
```python
length: int 
length: int = 10
```

Float
```python
width: float 
width: float = 100
```

Strings
```python
name: str 
name: str = "rectangle"
```

Boolean
```python
is_square: bool 
is_square: bool = False
```

## Collections

### List
- ordered
- changeable
- allow duplicate values

```python
x: List[int] = [1, 2]
a: List[float] = [1.0, 4.6, 9.1]
```

### Dicts
- ordered*
- changeable
- not allow duplicates.

* Python 3.7  dictionaries  are ordered, Python 3.6 and earlier dictionaries are unordered

```python
x: Dict[str, float] = {'length': 10.0, 'width': 100.0}
```

### Set
- collections 
- unordered 
- unindexed
  
```python
x: Set[str] = {'rect', 'square'}
```

### Tuple
 - ordered
 - unchangeable
  
```python
x: Tuple[str, float, float] = ("rect", 10.0, 100.0)
```

## Other

### Any
```python
a: Any
a = None    # type: Any
a = []      # OK
a = 2       # OK
```

### Union
```python
def add_two_integers_or_floats(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y
```

### Optional

```python
aux : Optional[str]: #Union[X, None]
aux = None
```

### Aliases
```python
F = List[float] # Aliasing list of floats
a: F = [1.0, 4.6, 9.1]
```