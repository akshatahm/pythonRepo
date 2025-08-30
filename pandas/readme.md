1. **Pandas** is a python library used to work with **tabular** data, also its sued to manipulate and analyze the tabular data.

2. Imp functions:

- Reading Data:
   - pd.read_csv('file.csv')
   - pd.read_excel('file.xlsx')
   - pd.read_json('file.json')
 
 - Inspecting Data:
   - df.head()       # First 5 rows
   - df.tail()       # Last 5 rows
   - df.info()       # Summary
   - df.describe()   # Stats
   - df.shape        # Rows x Columns

 - Selecting  Data:
   - df['column']            # Single column
   - df[['col1', 'col2']]    # Multiple columns
   - df.iloc[0]              # Row by index
   - df.loc[0, 'column']     # Specific value
  
 - Cleaning  Data:
   - df.dropna()             # Remove missing
   - df.fillna(0)            # Fill missing
   - df.rename(columns={'old': 'new'})
   - df['col'] = df['col'].astype(int)
  
 - Filtering & Querying Data:
   - df[df['Age'] > 25]
   - df.query('Age > 25')
   - df[df['Name'].astype(str).str.contains('A')]
  
 - Grouping & Aggregation
   - df.groupby('column').mean()
   - df.pivot_table(values='val', index='row', columns='col')

 - Merging & Joining
   - pd.concat([df1, df2])
   - df1.merge(df2, on='key')

 - Visualization (with Matplotlib)
   - df['Age'].plot(kind='hist')
   - df.plot(x='Name', y='Age', kind='bar')


### Others:
1. datatypes:
   ```python
   df.info()
   ```
   
2. duplicates:
   ```python
   df[df.duplicated()]				  # gives single rows
   
   df[df.duplicated(keep=False)]   # gives duplicate rows
   ```

3. empty:
   ```python
   df[df.isna().any(axis=1)]
   
   df[df.isnull.any(axis=1)]
   ```
   
4. convert datatype of column:
   ```python
	df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'], format='%d-%m-%Y %H:%M')
   ```

5. extract date, month, hour from the type'datetime':
   ```python
	df['date']=df['InvoiceDate'].dt.date
   df['date']=df['InvoiceDate'].dt.month
	df['date']=df['InvoiceDate'].dt.hour
   ```
   
6. Example of filtering:
   ```python
   sales_grp_top5_index=sales_df
			.groupby(['InvoiceNo'])['TotalPrice'].sum()
			.reset_index()
			.sort_values('TotalPrice', ascending=False)
			.head(5)
			.InvoiceNo
   sales_df[sales_df['InvoiceNo'].isin(sales_grp_top5_index)]  # filtering
   ```
			
7. After filtering or groupby, weneed to get the columns view back:
   
      ```python
      .reset_index()
      ```
					
9. Stacked bar graph:
   
	1. need to create a pivot table,
    
	2. then do stack
    
	
10. in/not in(~)			:
    ```python
    products = stock_df['StockCode'].unique()
    exits =sales_df[sales_df['StockCode'].isin(products)]
    ```






