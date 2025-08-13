1. Creating pd-Series (creates a key -value map, for list default keys = 0,1,2,3... for dict its actual key-values):

    - creating Series from a list:

      ```python
        s1 = pd.Series([10,20,30])
      
        #0    10
        #1    20
        #2    30
      ```

   - creating Series from a map/dict:

      ```python
        s2 = pd.Series({'A':['Apple','Ant'], 'B':['Ball'], 'C':['Car','Cat','Cabbage']})
      
        # A           [Apple, Ant]
        # B           [Ball]
        # C           [Car, Cat, Cabbage]
      ```
      
2. Fetching an element in Series:

      ```python
        # fetches the values for key: 'A' in series: s2
      
        s2['A']
      ```
