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





