#### Imp functions:
|# | Function Type         | Function name                  | Description                 | Example below (y/n)         |
|--| --------------------- | ------------------------------ |-----------------------------|-----------------------------|
|1 | Create nd-array       |  `np.arrays()`                 | creates nd-array            |n|
|2 | Shape/dimesnsion      |  `np.shape()`                  | **dimension** of nd-array   |n|
|3 | Mean                  |  `np.mean()`                   | **mean** of nd-array        |n|
|4 | Shape/dimesnsion      |  `<NDarray>.ndim`              | dimension of nd-array       |y|
|5 | Slicing               |  `<2Darray>[:, 0]`             | fetches all row's first element |y|
|6 | Assignment            |  `<2Darray>[:, 0]=9`           | assigns '9' to all row's first element |y|


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
 a_2d         # [[9,2],
                 [9,4]]
```



