### Overview:
1. Creating nd-array:
   - **np.arrays(list)**
   - **np.empty([3,2])**
   - **np.ones([3,2])**
   - **np.zeros([3,2])**
2. Describing size:
   - **np.shape(arr)**
   - **np.ndim(arr)**
3. Combining 2 arrays:
   - **np.vstack((a1,a2))**
   - **np.hstack((a1,a2))**


------------------------------------------------------------------------------------------------------------------------
1. Creating nd-arrays:

    - creating nd-array from a list:

      ```python
        # create a nd-array from list
        ar1 = np.array([1,2,3,4,5])
      ```
    - creating nd-array (with random values):
      
      ```python
        # create a nd-array of size 3x2
        ar2 = np.empty([3,2])
      ```  
    - creating nd-array with 0's:
      
      ```python
        # create a nd-array of size 3x2 with 0's
        ar3 = np.zeros([3,2])
      ```
    - creating nd-array with 1's:
      
      ```python
        # create a nd-array of size 3x2 with 1's
        ar4 = np.ones([3,2])
      ```

2. Fetching Shape and Dimension :

    - shape of nd-array:
  
      given a3 = [[1, 2, 3],
                  [4, 5, 6]]

      ```python
        np.shape(a3)
        # (2, 3)
      ```
    - dimension of nd-array:
      
      ```python
        np.ndim(a3)
        # 2
      ```

3. Combining 2 nd-arrays:

   - vertical combining (one below the other):

     ```python
        a1 = np.array([1,2,3])
        a2 = np.array([4,5,6])
        a3 = np.vstack((a1, a2))
        # [[1, 2, 3],
        #  [4, 5, 6]]
      ```
    - horizontal combining (next to each other):
    
         ```python
            a1 = np.array([1,2,3])
            a2 = np.array([4,5,6])
            a3 = np.hstack((a1, a2))
            # [[1, 2, 3, 4, 5, 6]]
          ```
