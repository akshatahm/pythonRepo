|# | Dimension             | Name(Mathematical)             | Example    | 
|--| --------------------- | ------------------------------ |------------|
|1 | 1-D                   |  Scalar                        | 5          |
|2 | 2-D                   |  Vector                        | [5]        |
|3 | 3-D                   |  Matrix                        | [[5]]      |

<br>

#### Imp Basic Numpy functions:
|# | Function Type         | Function name                  | Description                     | Example below (y/n)         |
|--| --------------------- | ------------------------------ |---------------------------------|-----------------------------|
|1 | Create nd-array       |  `np.arrays()`                 | creates nd-array                |n|
|2 | Shape/dimesnsion      |  `np.shape()`                  | **dimension** of nd-array       |n|
|3 | Mean                  |  `np.mean()`                   | **mean** of nd-array            |n|
|4 | Shape/dimesnsion      |  `<NDarray>.ndim`              | dimension of nd-array           |y|
|5 | Slicing               |  `<2Darray>[:, 0]`             | fetches all row's first element     |y|
|6 | Element-wise assignment|  `<2Darray>[:, 0]=9`          | assigns '9' to all row's first element     |y|
|7 | Element-wise addition |  `<2Darray> + 2`               | adds '2' to all elements individually     |y|
|8 | Element-wise addition/sub/mult/div with 1d and 2d (having same rows) |  `<2Darray> + <1Darray>`     | 1d and 2d can be added/sub/mult/div if they have common columns |y|
|9 | Element-wise int to bool conversion |  `np.array(NDarray, dtype=np.bool)`               | converts all elements individually to bool    |y|
|10 | Element-wise int to str conversion |  `np.array(NDarray, dtype=np.str_)`               | converts all elements individually to str    |y|


#### Examples:
|4 | `<NDarray>.ndim`      |
|--| --------------------- |
```python
 a_2d = np.array([[1,2],[3,4]])
 a_2d.ndim    #2
```
|5 | `<2Darray>[:, 0]`     |
|--| --------------------- |
```python
 a_2d[:, 0]    # [1, 3]
```
|6 | `<2Darray>[:, 0]=9`     |
|--| --------------------- |
```python
 a_2d[:, 0]=9
 a_2d         # [[9,2], [9,4]]
```
|8 | `<2Darray> +-*/ <1Darray>`     |
|--| --------------------- |
```python
import numpy as np

ls_1d = [1,2,3]
ls_2d = [[4,5,6],[7,8,9]]

a_1d = np.array(ls_1d)
a_2d = np.array(ls_2d)

a_2d + a_1d      # array([[ 5,  7,  9],
                        [ 8, 10, 12]])
a_2d * a_1d      # array([[ 4, 10, 18],
                        [ 7, 16, 27]])
```
|9 | `np.array(NDarray, dtype=np.bool)`     |
|--| --------------------- |
```python
 a1 = np.array([10,20,30,0], dtype=np.bool )
 a1               # array([ True,  True,  True, False])
```
|10 | `np.array(NDarray, dtype=np.str_)`     |
|--| --------------------- |
```python
 a1 = np.array([10,20,30,0], dtype=np.str_ )
 a1               # array(['10', '20', '30', '0'], dtype='<U2')
```




