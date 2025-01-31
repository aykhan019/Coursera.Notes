

# Module 2: Data Wrangling
## Introduction to Data Pre-processing Techniques
Data pre-processing, also known as data cleaning or data wrangling, is a crucial step in data analysis. It involves transforming raw data into a format suitable for analysis. Here are the key topics covered in data pre-processing:
#### Identifying and Handling Missing Values
- **Definition**: Missing values occur when data entries are left empty.
- **Techniques**:
	- Removing or imputing missing values.
#### Standardizing Data Formats
- **Issue**: Data from different sources may be in various formats, units, or conventions.
- **Solution**: Use methods to convert and standardize data formats.
#### Data Normalization
- **Purpose**: Bring all numerical data into a similar range for meaningful comparison.
- **Techniques**: Centering and scaling data values.
#### Data Binning
- **Purpose**: Create larger categories from numerical values for easier comparison between groups.
- **Technique**: Dividing data into bins.
#### Handling Categorical Variables
- **Issue**: Categorical values need to be converted to numerical values for statistical modeling.
- **Solution**: Label encoding and one-hot encoding.
#### Manipulating Data Frames in Python
In Python, we usually perform operations along columns. Each row represents a sample (e.g., a different used car in the database). Here’s a quick overview of basic data manipulation:
- **Accessing Columns**: Columns can be accessed using their names. For example, `df['symboling']` or `df['body_style']`.
- **Pandas Series**: Each column is a Pandas Series, a one-dimensional array-like object.
- **Example Operation**: Adding a value to each entry in a column.
```python
df['symboling'] = df['symboling'] + 1
```

These techniques ensure your data is clean, standardized, and ready for meaningful analysis and modeling.
___

### 1. Handling Missing Values in Data Pre-processing
Missing values are a common issue in datasets and occur when no data value is stored for a feature in a particular observation. These can appear as question marks, N/A, zeros, or blank cells. Effective handling of missing values is essential for accurate data analysis. Here are some strategies and techniques to deal with missing values:
#### Identification of Missing Values
- **Common Representations**: NaN, ?, N/A, 0, or blank cells.
- **Example**: The `normalized losses` feature has missing values represented as **NaN**.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S72GEFL7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGdbyqDk862oosMD0a%2FpWy5AM23hDyFmeGPoV5MytAFBAiAVjgrwjqNT6SQ6SIN1de4Ia8LSGwplAfxGrOzMWrgArSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYQgn57XlqwBw%2BkfdKtwDDoJZzU1nfiRoHuXy5FsAtlk3%2FissH75NK3NGC0kBVCYMZfGx3sIxMcRT4CFoI5M%2FSwVe1gJs0YfnOM7s74RVjLhZB1ukUJNvm2XtN3p%2B93UwaP%2FMSwDf5jqvDEppghQU3Stn2FhzQvLxPnhP7tNds1YQ3bTh7EmL39z1b36379OiAxmh4CJMsKJwgbhFAQDlpPFsCt02OxnGP4IFkPsI6nNQDv1FVKROTqrAE8OU1M7ih46hcP9oVaKouuSnWAkF8FYn5AqHxmyH3LrXXQB8e62mxJ01mSjdhNps965chWaw4SNzoD6g6kwC6d%2BjGdvzkE6DLJNIfJ0%2BcxjWI0rv%2B3GSPFm7W62AaBRmrsxZiG59OEV1bTxo0RkEuhbw0mIdaozMpdOORejOdRZWIdS5%2FUhBg%2BWUup9VMiqzw2%2B4SyWaDFuOPf4UxjS11OVsrXHJ3pNNhOzGSNhYVFFwqUHFZHD7IIKAzQSMhfaU8r8d%2B30DMPNt7TR92qn5ZkBtJkJGg5%2BRBhLYOtca2hEI9wNVeL4T4ZZIXO%2FPHvbm1WcMXtakOJl1nwXEeCRVreedFSZ8M%2FHBLXpPXuQin8wcBA3h3gkBk7yAEdABQ1QthiEWE%2BV6%2FGMHMl%2BmsyncRVgw6vj0vAY6pgFQH0iJ0TbzJKVL%2F4oRxDIP07frthabl7d9v%2BKxv8%2BucRYvmIYv7QHItqTG04RHnPaLDjXeVlMogb4nbw8crtJsgR9AXVi6ABWkdWYkABp0lu3vMw5C%2FPq48RXO%2BPnI99g%2BQ6TSWU3pduIGIjYzX8%2FqsNrSooe2b6EZ5F7ZU8thibXb4oFXKFlD1LAFIHVT7fJq4geHta0i8Bml4mzQ4UnLm6Jt4o82&X-Amz-Signature=e0470f04e403bc75460d85b553e1e1be7c26a953d2a2f184b557eb8751ac1ed9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q6RYYNC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0WWVepl%2F%2FqfH0gyrKcPGBKqOrb%2F3q6FK93uIlrxX33gIgHfrQm5sO%2FQ2AlQ4UeWYocSadynWaKGQwNWT6lpvkSZAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFWpyAq5CVjoTgz%2BaircA8WWUMPCmZdOl52Uz0NhT4TPXlsjz1J1zbYK1whoQAATLB2rqNNTNHu8JTuXWpuw8F%2B6zXMoApeU9J29doHtVy6MeYghYwmuqr48RXmo2pfn7QK4%2BV%2F%2B9LLrAW9Y1oOeHHEFbp0pocaDxop1ay3Ofjew2lTSifOGOn7aLAo0HC0ft9gN0yLS9rI5WWKETQxRZ8g3JOh%2Fue9pcX7sj6CxZuXAJycCMweGmN12hozRxIt%2BSytGYBxNWZ05zyvq4ZSgomwrpD3a3mNdLLpysZmUFR5%2FOFe3F8CCzf5OnxlzP2PcvpcxZ96mftNSsrgRh9QoJzv2Zm9Haf8I93Z%2BIpT9uRpDXyRbWAYZwlaHG7hLWrzkr%2FABKqfq53elITcS1pAP10S13ay%2FZniDSyeRwW0e3OkGS%2FTyGMK539G2RHI0ToOo2%2BdR4fSqVYhbgTIVsJrWYWNwpnz%2B%2BrldPbAXZL3N4zfRt9xJn%2BwUQw39WgCw4R7saylPghAbVxuiO3nqCi32%2B6dEiw4eGqp1rNq2S9LkzV8NJqOodzqqT2%2BfsfMp8BzHTGhKEkm9OdvdkWRI%2FN6KWL44ctqw2rfe%2F%2Fvvhnj8Mfmlb8usDPpzPI9s8EvEKgc%2BMPnV%2BnlaAceu%2FjRmMOr49LwGOqUBekNp2rDS9H7zrcMuwTjYdN74au21L%2FKAUICVXSGoYvX6WKLxcCMtnMyhfzO7iU0NFJotk8heEQGk4s8BMXIo1wWFIu07EMcnAJKqfjYzkJR%2FpmVNC90iJPp432nrlBVJHjC4avld5JpdT%2FJTxbggdYc7QU0bVXeT6WvYd3cUHrpOze0mkJYl4XsmfRcec8MtOofeyIlM73AiFhzvN18yIphJZ9cw&X-Amz-Signature=6a7b1496738d0889792f575e8a99c24a148c4feacc6ca0f3a9f3656d40317b27&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAZXVCEB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVYNLZ21qJ%2FYNxcDvwEx2h7ICIr4nAfmWDzXUuIpYfIAiEAybOlUFfriZQbs0h4dmyqicmswI5xBkPIJqx8HoqjYdwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIAUAbvX23FO4MXdUircAyE4PSyS9NXw0TvpNdZrb5DZOkuuyZWgF4P6B2XTVj3pMnzVnsMn5frOykCuD1YERKXnTpk2MtlmorFKLP%2FvOu7vRh4LJEqvEoSrWmRm%2FauoM%2Ffk6wa6iMW5VdbCnfBDOMxI3EehrRfgh2VUWIJxCCQyBFBamKs96zgsuokhkWyRxNqJOGgk6mngRrmnbUkv0MpvFuLX9gYBjdr2zrbr7CdfTGAVOibhQYwsA3zowSf%2FBXJgYYN2XXRPAec7BMUvFPFqaIB4QVCUMb%2B%2B4JAg1oSxRXKQL2TCgLlMSO16yDxhKtAlOcE2bExmI1g%2B37ll%2FrjKot6XG0%2BzV9Piy2IMH3w5W%2BufY8eIXLOQUOSFJjQe7hJGsp%2FpfutrTIyP1q7WhptsW5jAAl8Bge1GGvIELTiBD2kjg5vLAefDhPFNuOiJ19dGVEW7vf2P2gbnhwzR4PJMhbEGXKamZg5Sa5gCXil1Kq%2FHH7Eb%2BULMqsBhH1lxmRR5XqRMxoZgfk2tTUgzibTTknxsDzLWBzp4FPf5qoJqLIVMWEQRsEsKO82nf3izki%2FRI%2BqYeiKfTiSi%2BrWPR3SkD4I8XRYWRXsMofpZGsF%2BVrAzhq1o2dDV5%2FrMqWu0CdNU3hRQ6%2BOBMDBcMJD49LwGOqUB1b9AZcTBvEDOO%2BCFEusNseJ3LRonoaPh2qQckBeBaeYsgnzSM53XFK65YJ9%2FxXUqBB95CJX5mYWcUL9SGRu%2FOx1xtWnXN5htYMS9fgCWhU1ksnBN1H4KtQsxOpUo5ElmIccLwVwB8OI7YU5SIM5XwOMNjhzd4suTLO7Rq%2BuXc0MOatlozbMx97qngg3DaS9egLx2vyby8UTy7MSwGnKz7DsHM8dh&X-Amz-Signature=aded89b22ee96fca8d49d797c6179b57da8e89341a1a693e228162f9140f8890&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Pandas Method**:
```python
mean_value = df['normalized_losses'].mean()
df['normalized_losses'].replace(np.nan, mean_value, inplace=True)
```
	- **Other Techniques**:
		- Use group-specific averages or other statistical methods to impute missing values.
		- Example: Replace missing values based on the average within a subgroup of data.
4. **Leaving Missing Data**:
	- In some cases, it might be beneficial to retain missing values for specific analysis needs.
#### Practical Implementation in Python
5. **Dropping Missing Values**:
	- Drop rows with missing values in the `price` column:
```python
df.dropna(subset=['price'], axis=0, inplace=True)
```
6. **Replacing Missing Values**:
	- Calculate the mean of a column and replace **NaN**s:
```python
mean_value = df['normalized_losses'].mean()
df['normalized_losses'].replace(np.nan, mean_value, inplace=True)
```
#### Conclusion
Handling missing values effectively is crucial for ensuring the accuracy and reliability of data analysis. The methods to handle missing values can vary based on the nature of the data and the analysis requirements. Using techniques like removing, replacing, or even retaining missing values with the right approach can significantly improve the quality of your data and the insights derived from it.
___

### 2. Handling Data with Different Formats, Units, and Conventions
Data collected from various sources often comes in different formats, units, and conventions. Data formatting is essential for ensuring consistency and facilitating meaningful comparisons. Let's explore how to address these issues using Pandas.
#### Importance of Data Formatting
- **Consistency**: Ensures that data is standardized for analysis.
- **Clarity**: Makes data easily understandable.
- **Examples**: Representing "New York City" consistently as "NY" or converting measurement units for uniformity.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPKCHRES%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnd7iALr3uG9CWdim8fERCtB3xru5uK%2FewftaSYc3WIAIgeHeezschdtM5nr89xYHmVHhlMpsWmE7XX7hNzRGm5AYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1hUS%2FGe1%2BM2KOaRSrcA%2FRqaAj%2FELJ0gJfU1Fk1lPuBBIuPvM2%2FqGX8ZaMzts4jdPDYFmBOeqZUbC%2FHtRQX357ss1nNb6NKgPqe5%2FVau1l4bZOycaikZtaFKDoo1IegR3C85zk2%2F4BV1GLZzTbtvTJR%2B6nGAqHFhrZcbxGEbg2F9XIttSCv4wHnDtUxXqlYQxqo%2F8BXui%2Fr27v2SqUXp9A4kdol0ZvHGkGiyzGfbVG6CpYKB6Mcrdq%2B1vMnfLjK9SBvXgTxhChXE1o%2B8W%2F2J9du4FD8t2cRR2Wg%2Fy4HsCq0dwJVEVx7LmaRyP3YvDw86SWPx7Qy7uT7kdra9ui42Ylo9xYRDj7BO4aXemCOqVUDtitbcgRP5kGCLFXL6LZ34bzx7LdrhhRehUBqR8s6z9UoHCSx6GRq9yaV499P3NUiQWWEfV4rG8CZgdV6RkslO3NBV4OSm%2B16drtIn5AH%2B5FIr%2FZL1WgXD3MCIHWeSNA1FvtxduakgLa4DaVJeMS%2Bsd0am5odTfwpJHDnx5CmE5MMrkh6xSdYRfVF50LSSIvk5YBC1ZbNgxmHwg65KJBSX0%2FS9hY21rE1xRnLd5uvLp1eWT%2FeSfmNhbAVIPs%2FUzSx%2B3HpUPLTNWg5%2F6kZbGxMv5NjWu3W2m6xpDWyMLL49LwGOqUBFH7CXY26IRsZZq3qOa75zy7%2BIRf61MojrUlv1mabKzjHZQPgebG4oHJYt5Vu%2BU8h2ZJVbGkJI5OOtSi7qn6dr1ILZP4bGNWSrOGmpzJvA38M%2FNbsJ54ulrJJ6SqesvfzaYDaSX76iNXcfCeo8pvqWQOP%2BPqUC6Rh6yHcSC2oy3fcsGV1So1Kl%2F67QdPiC4OMLiyKQUy7QU2MHsHDdcw3kBqvaE9I&X-Amz-Signature=3bd2896204481af8f11cf21ae19b09825a1c459775e679ee351964d577b568c2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Common Issues and Solutions
7. **Inconsistent Naming Conventions**:
	- **Example**: Different representations of "New York City" such as "N.Y.", "Ny", "NY", "New York".
	- **Solution**: Standardize these entries to a single format for analysis.
	- **Pandas Method**:
```python
df['city'] = df['city'].replace({'N.Y.': 'NY', 'Ny': 'NY', 'New York': 'NY'})
```
8. **Different Measurement Units**:
	- **Example**: Converting miles per gallon (mpg) to liters per 100 kilometers (L/100km).
		- **Conversion Formula**: `235 / mpg`
	- **Implementation in Python**:
```python
df['city-mpg'] = 235 / df['city-mpg']
df.rename(columns={'city-mpg': 'city-L/100km'}, inplace=True))
```
9. **Incorrect Data Types**:
	- **Example**: A numeric column imported as a string (object) type.
	- **Identifying Data Types**: Use `dataframe.dtypes()` to check data types.
	- **Converting Data Types**: Use `dataframe.astype()` to change data types.
	- **Implementation in Python**:
```python
df['price'] = df['price'].astype('int')
```
#### Practical Implementation
10. **Standardizing Entries**:
	- **Scenario**: Different representations of "New York City".
	- **Code Example**:
```python
df['city'] = df['city'].replace({'N.Y.': 'NY', 'Ny': 'NY', 'New York': 'NY'})
```
11. **Converting Units**:
	- **Scenario**: Convert `city-mpg` to `city-L/100km`.
	- **Code Example**:
```python
df['city-mpg'] = 235 / df['city-mpg']
df.rename(columns={'city-mpg': 'city-L/100km'}, inplace=True))
```
12. **Fixing Data Types**:
	- **Scenario**: Convert the `price` column from string to integer.
	- **Code Example**:
```python
df['price'] = df['price'].astype('int')
```
#### Conclusion
Data formatting is a crucial step in data pre-processing, ensuring consistency and accuracy in data analysis. Using Pandas, you can standardize naming conventions, convert measurement units, and correct data types efficiently. These practices help in preparing the data for more meaningful and accurate analysis.
By addressing these common data issues, you can enhance the quality and reliability of your datasets, leading to better insights and decisions.
___

### 3. Data Normalization
Data normalization is an essential preprocessing technique used to standardize the range of independent variables or features of data. This ensures that each feature contributes equally to the analysis and is crucial for computational efficiency and fair comparison between variables.
#### Why Normalize Data?
13. **Consistency in Range**:
	- Features like length, width, and height might have different ranges (e.g., length: 150-250, width/height: 50-100).
	- Normalizing ensures consistent ranges, facilitating easier statistical analysis.
14. **Fair Comparison**:
	- Different features might have varying impacts due to their range differences (e.g., age: 0-100, income: 0-20,000).
	- Normalization ensures each feature has an equal influence on the model.
15. **Computational Efficiency**:
	- Prevents features with larger ranges from dominating the model (e.g., in linear regression, larger value ranges might bias the model).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662P63IU5M%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDH4z61qBJlg8lYn3v3n2pXk7L2idSa3IZCDIme%2FOP0LQIhAJMxxBshpAOE%2FG6z%2Fu0njgj78luxmV3rm2yKHNv1EBvpKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDkDhhsGCOni4IKn8q3AOlZUYwSfeQf9OX3dGXfmXFCty2jSZxyy0b%2BIFdm8bWru8zgRsOxwiTWnB08c5gU7%2FpTHZ6PEDDzGC2c0flA5EYDMsc3dmHcIurr77JhDXXc%2FUP63ml6a%2Bfa2JBg98WVrDK4HwYKkd7gw6Qfl%2F1jX7CkIxKOA7qI8gWltwUutP2pnARn8K%2FRzZFDpp4D2Ukq4GCrWV4KTIktXrkkaQlQKRUMCQpcheyj%2BQcBauNisqw%2FVA%2BOw1tvhi7CZCyJ%2Bpvl0AY%2BVTSDfy9TiwqJJu5x%2FvCW8kXRQcU6D2spG91cNVXNd01H2WbKAQyq3l%2FlXV%2BBUG1c%2BO%2Fvrt03sT1ktZq7sMAxfkA0Ua0gEOQ7F%2BMD%2BqrHt7oeB%2BqsljKa8A4AcKVCENPoyXNyJCOy2hkkUuh6qFtS6L3gcdpyqRTNLAB103U3YEphwYTGNtycb8Cau%2FpflBPAm3eBxlNzmltW2ODCa6EHTtHU8K0tvmsLHfwZFfoAE8O7n4mNBsCeRHkMM8X798d1BBwuRvASeAc89eLcHJtybrSYP76bPQacU3SDsRFOgh3XymiFl1w%2FflgC0%2Fy1XAWVAKgkHdyWkq1wDy7t8VurQ%2BOPQ6%2BkFDsIOSI5HS187N62WR9J5WQoEv%2BbDC6%2BPS8BjqkAdo1%2Bh3NwRwgKn7S2xSMxgpHFgcX1mrUuR7Jcx65%2FRtK%2F3gA2D6VbsVVmI717p8fa027Gw51%2BU3KIBzZaJF1o0mjqPEx%2FoaJakmHQcQ4HQ3myMwMcEtIZvSyiRXBFnmK6y9RF3vzAkmOOYYWdXCduOUSlFqaVFqZy8%2FwPNOmwlaCeNcXiUtmfsLBKGWTolbUpfR7LDNdW15%2Bnt3V1cu0jgc3aGKr&X-Amz-Signature=6cc840d661296c047a1a50f804b71826d40257ff041d2a2aef6463502433d799&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNF6LMWU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKugTiXWd1Nmi5SkYq7WEorFoO4CE5r2QEXSxIH8eTSAiBFtwsIyZ06bhulgkmUyDcksqvNxV0Bn4eh5v7LtNbwESqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr4bJmgxjBRwKBcfbKtwDO%2BctGFnYxZHvv%2B09Jd7cqZgiS649CH7MIOgCadPIt2%2FVieycAkLxN6hgo%2BZ4z6BsVZkXXGmihnEyQdt5noPBGf7qQAzFksEACVdD47g%2Fi7iYkETzqTbaidNCKyIP4ub1m3Oah8QZLkiIyL0WjtqFs7iLSk7BBlhUx%2FKPfV4eFN2diSGXRve%2BRJflbc%2FPQkzK1vzRUSpBUtcA7dxlnyh5FB28vtcMd8QlQQX883rQM6eD1LXkfMraR9s9HHsGRE6Uy5UofOv%2BS09jMW0jpLOpjJbfcnmmYqyPEzGlWzft15jDd695EjfW8LJcgKkPC4WHU5j5JQodDhrAeLs8G7Nu1LxWElu5103uqd8jg1%2Bgfgm7BVDMXBOKB0HUSM2%2BOusVNPsvbu5IXy%2Bcp3XYOfJT418i9DxuYXg8Ngv9YkM5pLQAkuKff4mEH7gPy9N6QhrmOKe3qG96sC2QexBPhvqJW%2Bqh2TlVTqTc%2FSBuQh1X%2BFDYSOKgSLOfTcK7JhfFBAR8CdOsmpUXBluFNrY2Z0p8MHsWn%2B64A4Jj5L3pOEcqnxFjb2LIY1q3lSmvQAw%2B6YC5SyVsa%2BFiKl5qzgo91dmq3IsgYjy8QZlqpgfoDmw7s8MuJ5qp8WQ158UyTkUwr%2Fj0vAY6pgFQTq5u5CeXvQWPYnE5I8SI%2Bo4QcO0fNUh2VkqMWEGRP1uPlGQpiZKwpaRwRAlKcHttBxRxWsTr8i%2FytzdC4Tn8OwAJs6nNAkM%2FTwbjQD9l9LCkTXriwDZmYSklT9Bc0aQfibS4zGufoD8HqENMOrvPU%2FoYx8WVBA8TQs%2B9wXL18DZ2a4hYhVOOtMtKXd3%2FXPTGQnuArtuLY9neauI%2Bbo4zqyF%2FexgV&X-Amz-Signature=75690666f5d9ac768734c98afbfb6815b10136ea4489e1091fa90cf10f33b32f&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWVXZLC7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGF6PT1fBF%2FqQlb2VhYMdzcE0i0FtSLASPthWUU3FtE0AiAovYp1rdsaX5dbjy6%2BfnuQqyD34PhG6Yd2SsSV1MUJxCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8E2%2BGnJR320hpKKdKtwDU9lDCcNT8RcauVE5DfdD8wwNNA1MVmT999Ie0gq668iRI7vcUEXz%2FoX%2F4sszOa%2B5ULo3o%2B9H6KY6Yf7qKui8nroCWb1adrtZg%2FfvgPxxgvc%2BB83B77G1j2518WaMUlUyFwHYAf6KtbGIHTfp87BrmAHKgINzJju7EfE1h2JLlsNSFtkTflG1%2FNMg8yiIwGSgBICw6cu3WmDoZeN4CfVB8Mo0b2iHzAQk20gcBXaBpKJduregK9sybinxfyutw0m0Hxm7p26N0dbovlY3y91x3U3K0h2FUxkEmj4YLmJwiZbZBEk8vS%2BxYJy%2F1D3616vOAdKMM3yWuv20rQ9heV6RT0%2B2zaaFDZLm79oKBcv%2BdPfriNVO%2BwTbfvye2zv0WQaBPpb3pG0uDPJ35i1ENtTvy5d75dv%2FDFFsaT4CLYlGjcDo73fTR8hBsfqLii13YDT4tVNuTXPAUIukBFc1XhX7i5wKdshfGOC6U%2BTIL6mnO2j2tB2UVnrZ5Un%2F3elIWYCxgeeimbNz9iaylsb6TISkGwj3MZtwHKxqr13VQr%2BzIk%2F8JB1bKjdyiG8aJ7EOXuYwlZ3%2BzxTg1bVBwFVkp7jsreXyI1ay4sXx6MrdN%2BnBL33CTAKGS1ASen24UjEwrvj0vAY6pgEFCuC9%2FKRiHR0UapBoLf8YeMF6iQjSo5NRFNwLnX%2FlW9qQvrALpzOV8%2FGhvlwAz91kMJ3nS2M%2BNg%2FzmpWoTXwbzcYkZ7BRtTfB9Nf4wMOh9lA9nDqcveVvRArY6dfu6PVvLnTyaTe56H6JpcYaKpMXWiqTUGZ2OhZzzapmMgdrZN%2FCiza57Unpj9yngim6nq4LRzKpx8k64fBjLUtMHTde18M7LP2W&X-Amz-Signature=d86e6db45110793714fd5d1948f686d5c793319401616f4e343bfdf77e09ea67&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WHWYROD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEdp83unfMYrG70Ew2QLp47qDdgmQ5lMk%2BvoPHSRWZx6AiAtWzXgwQgqsOp8da0cvwuatMNx4j8IDrv6OkNtc17yeiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVTXoY5MB26JQX%2BKpKtwDoJXs0mdBpdLlTk9pJQpTSVLw7UyN7%2BPyg3O5NieTnmVrm6W3qfi9bCwYtEUEWgyKsbrgavdRtHH6uTzsUUh%2BFKKwRvPb2Z1%2BUXizq%2BH34r5N05%2BHBNcHH79tzVW%2Fua%2F4RSohzKCHkgfENVJb%2FKs1SK1yzoVCDUmqDmqh0vU2fAUo2gA1vJlIO8UW7PuPMjefXuwWDZRmNQKA%2FHKs%2FXQ%2FMuE1iubEK4EPT5lRIQuiRg6R3sWuh3ChR9SBtN3txscFIEBQ74K6Vv%2BDzXdA7I%2BWeP5iCbMZCxVo8mJku9%2Bd29jeQu0J7XC4GHWyh9Myo96Mi0EMZQL5DX%2FNgvTHRc7kiPPWYg0cukUJyhNg92fRt6%2Fq57%2F8bxudIUL1vCPIzSh1eUD8qqyPTuisdj1YLWmr61n%2B0KWglGvTh5kzMcuIRmzSlUURAWVED7JLqb1wf4oea2sU6HBG8yUaxmKSw5yhhOD7zQ92%2B07EvdFBQEdawYaN0dPkYF6Ivg0YNROzyKMsT3Z5n7oryMBdgUtfKnGQSAtWLlZzZANFjIpjlyR9YoE1yrZ4AWuib%2BdLJS0RG%2F5ZBKHXlH%2BUckeF3nfjc9xwkf2SoEWWTF0DaBPuksB3vw2ams11FOTjwcpqIE4wkvj0vAY6pgGr%2BkRkeBCZZ3K%2FK6erPO6cdI1B%2F0Xk6MTefNei%2FFuPo%2BKEE2mHtdHHjqoc8PD66v1TkKJECIM3oBrdrUWleO%2B%2FXSxWY31K%2BQyKr59%2BCxjSxd9V7HGb3uZZF2mcv3gM0EjdbI%2BzFqeEBOvI7pbAoPYEEZEw5dqEHHvSci5PnJZNeKfoBZTXjVlvP9LX76k%2BYRsVmQ4w6JNfYDEdnQp%2FM%2FsyU4cLXaIx&X-Amz-Signature=30ff7582e2fbe338fe427cfe57989f95f36f9ffa141f103a73fe850ee62eec8d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example Implementation in Python
Given a dataset containing a feature `length`:
19. **Simple Feature Scaling**:
```python
df['length'] = df['length'] / df['length'].max()
```
20. **Min-Max Scaling**:
```python
df['length'] = (df['length'] - df['length'].min() /
				       (df['length'].max() - df['length'].min())
```
21. **Z-Score Normalization**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
#### Conclusion
Normalization is a crucial step in preparing your data for analysis, ensuring all features contribute equally and improving the performance of your models.
___

### 4. Data Binning
Binning is a data preprocessing technique where numerical values are grouped into bins or categories. This method can enhance the accuracy of predictive models and provide a better understanding of data distribution.
**Why Bin Data?**
22. **Improves Model Accuracy**: Grouping values can sometimes enhance the performance of predictive models.
23. **Simplifies Analysis**: Reducing the number of unique values can make data analysis more manageable and insightful.
**Example**:
- **Age Binning**: Grouping ages into bins like 0-5, 6-10, 11-15, etc.
- **Price Binning**: Categorizing car prices into low, medium, and high.
**Application on Car Price Data**:
- **Range**: The price ranges from $5,188 to $45,400 with 201 unique values.
- **Binning**: We categorize prices into three bins: low price, medium price, and high price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662P63IU5M%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDH4z61qBJlg8lYn3v3n2pXk7L2idSa3IZCDIme%2FOP0LQIhAJMxxBshpAOE%2FG6z%2Fu0njgj78luxmV3rm2yKHNv1EBvpKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDkDhhsGCOni4IKn8q3AOlZUYwSfeQf9OX3dGXfmXFCty2jSZxyy0b%2BIFdm8bWru8zgRsOxwiTWnB08c5gU7%2FpTHZ6PEDDzGC2c0flA5EYDMsc3dmHcIurr77JhDXXc%2FUP63ml6a%2Bfa2JBg98WVrDK4HwYKkd7gw6Qfl%2F1jX7CkIxKOA7qI8gWltwUutP2pnARn8K%2FRzZFDpp4D2Ukq4GCrWV4KTIktXrkkaQlQKRUMCQpcheyj%2BQcBauNisqw%2FVA%2BOw1tvhi7CZCyJ%2Bpvl0AY%2BVTSDfy9TiwqJJu5x%2FvCW8kXRQcU6D2spG91cNVXNd01H2WbKAQyq3l%2FlXV%2BBUG1c%2BO%2Fvrt03sT1ktZq7sMAxfkA0Ua0gEOQ7F%2BMD%2BqrHt7oeB%2BqsljKa8A4AcKVCENPoyXNyJCOy2hkkUuh6qFtS6L3gcdpyqRTNLAB103U3YEphwYTGNtycb8Cau%2FpflBPAm3eBxlNzmltW2ODCa6EHTtHU8K0tvmsLHfwZFfoAE8O7n4mNBsCeRHkMM8X798d1BBwuRvASeAc89eLcHJtybrSYP76bPQacU3SDsRFOgh3XymiFl1w%2FflgC0%2Fy1XAWVAKgkHdyWkq1wDy7t8VurQ%2BOPQ6%2BkFDsIOSI5HS187N62WR9J5WQoEv%2BbDC6%2BPS8BjqkAdo1%2Bh3NwRwgKn7S2xSMxgpHFgcX1mrUuR7Jcx65%2FRtK%2F3gA2D6VbsVVmI717p8fa027Gw51%2BU3KIBzZaJF1o0mjqPEx%2FoaJakmHQcQ4HQ3myMwMcEtIZvSyiRXBFnmK6y9RF3vzAkmOOYYWdXCduOUSlFqaVFqZy8%2FwPNOmwlaCeNcXiUtmfsLBKGWTolbUpfR7LDNdW15%2Bnt3V1cu0jgc3aGKr&X-Amz-Signature=8aa1eb87412fe85871369cb307942f610104e13248a6a02760f9ed61eb48bca8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Steps to Implement Binning in Python**:
24. **Determine Bin Dividers**:
	- Use NumPy's `linspace` function to create equally spaced bin dividers.
```python
import numpy as np
bins = np.linspace(min(df['price']), max(df['price']), 4)
```
25. **Create Bin Labels**:
	- Define the names of the bins.
```python
group_names = ['Low', 'Medium', 'High']
```
26. **Apply Binning**:
	- Use Pandas' `cut` function to bin the data.
```python
df['price_binned'] = pd.cut(df['price'],bins,labels=group_names,include_lowest=True)
```
27. **Visualize Binned Data**:
	- Use histograms to visualize the distribution of the binned data.
```python
import matplotlib.pyplot as plt
plt.hist(df['price_binned'], bins=3, edgecolor='k')
plt.xlabel('Price Bins')
plt.ylabel('Number of Cars')
plt.title('Histogram of Binned Car Prices')
plt.show()
```
#### Example Code:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
df = pd.DataFrame({'price': [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000]})

# Binning
bins = np.linspace(min(df['price']), max(df['price']), 4)
group_names = ['Low', 'Medium', 'High']
df['price_binned'] = pd.cut(df['price'], bins, labels=group_names, include_lowest=True)

# Visualization
plt.hist(df['price_binned'], bins=3, edgecolor='k')
plt.xlabel('Price Bins')
plt.ylabel('Number of Cars')
plt.title('Histogram of Binned Car Prices')
plt.show()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPZA57FW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFm6bQqNE4Hv8kiVTK7ItNJ1xcxaN2qNEpQbYv0T%2FTUgIhAIryVXKTNESNVANq3nJDo4rzFrELacQEUH6ThutWaLe9KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxz03tCh3wEhQlhmQIq3ANSjlVNLRvuYjhwF613jN1LnLPju50NdhBDOX3c4u8mdNsfLpEjvY%2FM6%2FMQWFsBuD2OfBUJ1jXA1QksVeXUvbDC33zNkR1WxCOL54T%2FfwZynOoF9IorCQZ%2FqIw4fWI%2FO0JlcrPUeouB15ITV27%2FeV5JgXzJewP1jIrYej4TV21NdQGuaBYGB0wIXNsSU%2FPl6BnbMTTCTu0ZlLPcNR6sHUsGo0cIZxyRqNMPYx%2F6xOZugTqpoYEFAkSU%2Bh91Bx3rkC4Rk57smWlpIQk92y22pO5qjtU0mZt%2BISIBTeTP53yapl7t4eiIGC6zkwz59mMp9Ga4Kiu63ZegCcgCVdGYNW1OKsO4RRUvVrWDDaDTKrM9ifJSwZ0JN4Tm%2F8BllKin2wWbvNqgpyVDzel1RN4vxmD0gZpXI%2Bt5VmFhX1a6df55WlLeUzUXMhXML5QPh05xCIMWoavgAPTAdyS6LhtKTuqy63RC1vyowaTR711tK0lmia2b2R0mSZ3tQxISmr6uTMeE5k2sE5zzw05ZwKvSfKjxajXuwmoTsZdx3dbr7JRfujNejeI0QjDJ6n6aeTFDvSaZN%2FDswRTakNqrPBMqBHGTe5X9uu%2BkM%2B7w6RmXKxRAHnmO3FeHJH0B5nygLjC1%2BPS8BjqkAWHMwWqvzCTgup0SM4Hlr84F3Y4nhSKkAPMXqcHUbA3orB%2FCAHRZHRbnNf2L90M%2BxwIheKpS%2BSC29Hw4IB9qT5JVDE%2BJwzrjS4%2FERQ3AzpR8up2oqa%2FLvfTzfdhMigbZKv%2FpGLEyn3T3K0zKtE90oRDGYIIJJji2u4z86OpC8Aa4XU4Er39IpOqukW3Cnk4lY2aFEGs9lrzIzW5QvJYi%2FbwzzrP5&X-Amz-Signature=1d6c4e389e7a79d4ffd290136f03ad73c4bc10f3f8256e9dfb6c0ea6f78e358e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Conclusion
Binning is a powerful technique for simplifying data analysis and improving model performance. By categorizing continuous variables into discrete bins, we can gain clearer insights and more effectively leverage statistical methods.
___

### 5. Transforming Categorical Variables into Quantitative Variables
In data preprocessing, it's essential to convert categorical variables into a numeric format that statistical models can process. This process is often referred to as **one-hot encoding**.
#### Why Transform Categorical Variables?
- **Statistical Models Requirement**: Most models require numerical input.
- **Improved Analysis**: Converting strings to numbers allows for better analysis and model training.
#### Example: Fuel Type in Car Dataset
- **Categorical Variable**: The fuel type feature has values like "gas" and "diesel".
- **Goal**: Convert "gas" and "diesel" into numerical values for model training.
#### One-Hot Encoding
One-hot encoding involves creating new binary columns (features) for each unique category in the original feature. Each row is marked with a 1 or 0, indicating the presence or absence of the category.
**Steps**:
28. **Identify Unique Categories**: For the fuel type feature, identify unique values like "gas" and "diesel".
29. **Create Binary Columns**: Create new columns for each unique category.
30. **Assign Binary Values**: Set the value to 1 if the category is present, otherwise 0.
**Example**:
- **Original Data**:
	- Car A: gas
	- Car B: diesel
	- Car C: gas
- **One-Hot Encoded Data**:
	- Car A: gas = 1, diesel = 0
	- Car B: gas = 0, diesel = 1
	- Car C: gas = 1, diesel = 0
#### Implementing One-Hot Encoding in Python
Use the `pd.get_dummies` method from the Pandas library to perform one-hot encoding.
**Example Code**:
```python
import pandas as pd

# Sample data
df = pd.DataFrame({'fuel': ['gas', 'diesel', 'gas']})

# One-hot encoding
dummy_variable = pd.get_dummies(df['fuel'])

# Combine with original dataframe
df = pd.concat([df, dummy_variable], axis=1)

print(df)
```
**Output**:
```plain text
     fuel  diesel  gas
0     gas       0    1
1  diesel       1    0
2     gas       0    1
```

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPZA57FW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFm6bQqNE4Hv8kiVTK7ItNJ1xcxaN2qNEpQbYv0T%2FTUgIhAIryVXKTNESNVANq3nJDo4rzFrELacQEUH6ThutWaLe9KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxz03tCh3wEhQlhmQIq3ANSjlVNLRvuYjhwF613jN1LnLPju50NdhBDOX3c4u8mdNsfLpEjvY%2FM6%2FMQWFsBuD2OfBUJ1jXA1QksVeXUvbDC33zNkR1WxCOL54T%2FfwZynOoF9IorCQZ%2FqIw4fWI%2FO0JlcrPUeouB15ITV27%2FeV5JgXzJewP1jIrYej4TV21NdQGuaBYGB0wIXNsSU%2FPl6BnbMTTCTu0ZlLPcNR6sHUsGo0cIZxyRqNMPYx%2F6xOZugTqpoYEFAkSU%2Bh91Bx3rkC4Rk57smWlpIQk92y22pO5qjtU0mZt%2BISIBTeTP53yapl7t4eiIGC6zkwz59mMp9Ga4Kiu63ZegCcgCVdGYNW1OKsO4RRUvVrWDDaDTKrM9ifJSwZ0JN4Tm%2F8BllKin2wWbvNqgpyVDzel1RN4vxmD0gZpXI%2Bt5VmFhX1a6df55WlLeUzUXMhXML5QPh05xCIMWoavgAPTAdyS6LhtKTuqy63RC1vyowaTR711tK0lmia2b2R0mSZ3tQxISmr6uTMeE5k2sE5zzw05ZwKvSfKjxajXuwmoTsZdx3dbr7JRfujNejeI0QjDJ6n6aeTFDvSaZN%2FDswRTakNqrPBMqBHGTe5X9uu%2BkM%2B7w6RmXKxRAHnmO3FeHJH0B5nygLjC1%2BPS8BjqkAWHMwWqvzCTgup0SM4Hlr84F3Y4nhSKkAPMXqcHUbA3orB%2FCAHRZHRbnNf2L90M%2BxwIheKpS%2BSC29Hw4IB9qT5JVDE%2BJwzrjS4%2FERQ3AzpR8up2oqa%2FLvfTzfdhMigbZKv%2FpGLEyn3T3K0zKtE90oRDGYIIJJji2u4z86OpC8Aa4XU4Er39IpOqukW3Cnk4lY2aFEGs9lrzIzW5QvJYi%2FbwzzrP5&X-Amz-Signature=0b9b19efc1f4ebe0550c2409f70f9e6276acf5239ad3593c3ed7a82ff0e76687&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Indicator Variable
**What is an indicator variable?**
An indicator variable (or dummy variable) is a numerical variable used to label categories. They are called 'dummies' because the numbers themselves don't have inherent meaning.
**Why use indicator variables?**
You use indicator variables so you can use categorical variables for regression analysis in later modules.
**Example**
The column "fuel-type" has two unique values: "gas" or "diesel". Regression doesn't understand words, only numbers. To use this attribute in regression analysis, you can convert "fuel-type" to indicator variables.
Use the Pandas method 'get_dummies' to assign numerical values to different categories of fuel type.
#### Conclusion
Converting categorical variables into quantitative variables is crucial for statistical analysis and model training. One-hot encoding is a simple yet effective method to achieve this transformation, allowing categorical data to be used in numerical computations.
___
## Cheat Sheet:** Data Wrangling**
### Replace missing data with frequency
Replace missing values with the mode (most frequent value) of the column.
```python
MostFrequentEntry = df['attribute_name'].value_counts().idxmax()
df['attribute_name'].replace(np.nan, MostFrequentEntry, inplace=True)
```
### Replace missing data with mean
Replace missing values with the mean of the column.
```python
AverageValue = df['attribute_name'].astype(data_type).mean(axis=0)
df['attribute_name'].replace(np.nan, AverageValue, inplace=True)
```
### Fix the data types
Convert columns to the specified data type (e.g., int, float, str).
```python
df[['attribute1_name', 'attribute2_name', ...]] = df[['attribute1_name', 'attribute2_name', ...]].astype('data_type')
```
### Data Normalization
Normalize values in a column between 0 and 1.
```python
df['attribute_name'] = df['attribute_name'] / df['attribute_name'].max()
```
### Binning
Group data into bins for better analysis and visualization.
```python
bins = np.linspace(min(df['attribute_name']), max(df['attribute_name']), n)
GroupNames = ['Group1', 'Group2', 'Group3', ...]
df['binned_attribute_name'] = pd.cut(df['attribute_name'], bins, labels=GroupNames, include_lowest=True)
```
### Change column name
Rename a column in the dataframe.
```python
df.rename(columns={'old_name': 'new_name'}, inplace=True)
```
### Indicator Variables
Create dummy variables for categorical data.
```python
dummy_variable = pd.get_dummies(df['attribute_name'])
df = pd.concat([df, dummy_variable], axis=1)
```
___