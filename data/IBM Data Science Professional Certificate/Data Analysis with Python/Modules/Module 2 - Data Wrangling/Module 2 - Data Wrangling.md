

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE7Y2BB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHkpZ8qKcIDOioQFarfNNcNy1dKDZTGorZrcjxQL1R2rAiAWNrdckUWtubFn%2F5q6%2B8m%2BDLoWLRdrOIvgNO7ih0AleSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIzsaY5Fa0TkRRFcOKtwD0YATxugWt6%2BgmBrGPv0odJDbkGWMCiNFhL5xnWj6hIAdtzXP2dTLf8E0l5%2FyNeHHZCaHzJlaisuctSOxCO582LXESbsBMqapGl7aW7G1qEB35AZRR6FPhKVrVOoOjdE8i%2BFrdiUdOqr1rccnYmwKZQe0PreXFYnn4vCKOCtfg3i0Iosf%2FU1yAPerEi7m9c2K%2Br9J%2FbL8yQymoOTe%2BMJkd%2BXt1HwMiBl20OD2YK7QeRf5zlqPf7ad2IgrKTUHynKXq5%2FvCxin8iapgpp4OujojQc42MY6Zkod0PiGYTcPvn3XA4wwlYOVqygRamKNIhoVjOuOLhc6dmeFzu3pziPOwfNXZut1%2F%2FFiJ8FPlfO%2FKip0WgAXsKg9k8VwNgbRoWVoqZr%2BLXSAF3d6j2EPLDCbS53GF8X0YWFB7bX798GLSJhX2TvKXEvS5jD%2F%2BdGZBM%2BQVFzktSKE3uuisLhD83oVrZYMwPkXj8fl6qA%2Bk5mW9tFIiXSXpcr33oqrzzZaEHyhnh29eP5qyuWNrEzcpag%2Fo0%2FOKkxGkiRJu0g%2B2UXjP7gSMSfcAKUC%2F%2FDT7BvJ4gdinHUsh3%2Bic5v2A67zreV3qjKJ8BIjhoN%2F%2F19TAJi4iMS%2BsgToTAlfaxjpkWUw1cD9vAY6pgEbZPAI8vTZHDHB%2B49Q28PMFJibbUWzEx9eP7d%2F8mUA0ZYEG1OREnGnk6yq%2FRBS6lZa9JtCseedI6L4outiRO1h870iQMD0T2MW1MkRtUT7ufC1K%2BEYHtPKP%2Fz0kAgkSZDHEknQtXaF%2BQ%2Bxu%2FnWBm6OL%2F9oc%2BExJCdDEbPiv8A8PshiZ%2FoYCX64bqpcnhjIVOpdOKDyiRAVFbILk%2FKMAmDcPv4GvfUr&X-Amz-Signature=473b295a6a7a4d2cea572cae23e2ea16101574842b1a73aaec07208d9a00fac9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNKOAVCL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZUHVD1TYoRAoTd6TH%2FBSKK8L17zV%2FCljTMJ%2FHrPW30gIhAOrwD1gyX1V%2FF6Op2e%2BJj7hrk7s53ZVmGn%2Bb38evvzOpKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxkmOi4B3tbz6I%2FPg4q3ANDDvHmR0hh5xADAkiSNAQdeBKgoIO3%2FO4KXQRHdssPkMrTgEzYaMqU1HECEykz04m0JE3t96idQr5zfwOJxU8ahN5jTRqqA%2FOu8vS9lgybou4rWfF1tr%2FTx11QFihENCTtkx5raW8VSeOuRWZ56NCqNNWPBTymI3nWBHqWnkxDKQv5xrVWilT1cNPBQd8YGnhVyy3IiJx9TBneHri4Hy6lxyHd3UDTdq1wyqyaWF4SA%2FFq1ZnoHxgCxrJ6lYcwXYN0%2Fm7AaFfWXeZM2I2k7AOm%2F5x6jFLxCOFv%2BUivJty%2B%2B%2BpZu1cRdYP66I7pR8SMYLECnp3TS4%2BlaAFx6O8zy0rJpgtGmK1ERnAnviZy%2F3is8OUDLHhN1QUVCueIpTpVQPqXjz6RUnb8trjFCYnUr33dtF4JNeV4n%2BIA4nHgm%2BVYlpe0IHDDz%2FKROUiPUP%2FWlYc5bGevh3NvXVJR2B9x0OthIzCReBbqsO6rSMlr4uUu1nxyrCLs1OXkOMgHjwrFNUSNxlsE1QTcci3PLi8818%2FsHM7RrONbd9qV3b8vR1C8TA4HqZZNteQCCk4Oa2mV37QERG4killNU4VBSRWvFgmVdsBGFjQ3Jw3s%2Fj%2BOrqAeLppfBR5vmznuaJEyKzCwvf28BjqkAc8jPLjUuL5OLTXktxfqYwZFGQR37ozB7m4aTfh14sI2X%2FV0ZxQQKMUJMc7mYceSullWdwoo5SduM8p%2F8D9BUl52o5aklCuiZzlYI5yzxPERrRSXvCJTmEExcSVrDpisE%2FzJLkaR1iz8WOsxN5fgojgzNbEWOULBeV5OHS6kZ9JCUmaV%2FT1WtipAmNh1q4cAP4TtX%2B%2B3FceaxKu8uBk59rIMhU94&X-Amz-Signature=f56049da62490f67bcb7838ccedab94288e4c47ab343e664c6a534379479c8d2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDHH6MIM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDu9sC0h9w0obsXulj0Q2elCbEk%2BmDiYKorA%2FCwm8JpLQIgS3P1CkKXZREm1Ub81lHi8Unuii1753eyX0mycauelbAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhuul8rcvhVxKrECCrcA%2Bz8HCMJvVELiMpXdw4K6BnEyXeKQQzphBsn8O33wY4mNfi%2FX5tUe6PgTIifSpHCiaj0EWJNE2KF1q2fZzxYF6s5x2hZ4e0z93EZqCaiAiRKwtNgktogkqVrknnqcrAO%2FwbSfz4%2FcWVzxkhCgs70RC0e8uBJMGFGhA1bPY8IIrBvH%2BsgzvmMdAbtg62WA23y6XWvZTq%2FZ0B4CoF9m5JC4TPAfk4M%2F%2FIknYVcH8EOxqoUS1sFn88Z1fKuVshecyvMacEUsMoFWp3D%2Bzh0g%2Fwzo1C6ZBmSRHMFJ6JT2I8txKZp84hdnnQkW0XL5nkcxKkCsOHpWhARmoUvhu8qlmBHq6H4H%2FSadlGXY19nTH5GjgHfPdNdvwVh9RjQ43yMj7gYhInvI2N5WB%2F%2Bg%2FgJ5Y4sXUTannpp2mt8MwwU20pQrtQ10ONzkOzGJf37WjeKl9GEaj36KxeNWMoFEVzi3fTs%2FVWFYnPxOKPWTzt2WIL1uVpQpXcrB57XCrMMJ42QsjRq79IT30BlZmHDFI1QQlngfJbJXVSOKs9W%2FgOUN4q1uQimYYccTn%2FClNENOA%2FxtsQO4qya5GpGLoKC7jl6H33keT%2Fb41i%2Bhu2ATxAtZCvXJfTMN5fGN%2BhxHZjoFg%2BHMNi%2F%2FbwGOqUByPqwHil8O3W2vVXfqPXAwQphJQZDB%2BRZh%2FnoigBMwhcsXw%2F7Jb0BfOJ5EhAmXW352hD%2B8Z9AckDfmwJPntuktooR9NGf6iDg1yh9RJe2YHS%2BH4VEZjNMnVOTHk1FO9Jv1f5CRD%2Fd83%2BQsw%2FHL1s8vVimTKYFxO3E%2Bsa85wCT9O%2F8ulLdzBg%2BwCV95B6EZqCgI3AZQI1Kv6dk0cgoY%2FKktD5uYfc3&X-Amz-Signature=2a8e8ee48b6a04db195f69e6e5a51ef7a0865ccb5a9a6ede753e3dcc2231daad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2AC4ZPD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLfM9TJjA462hJYQVvNNu%2FBTCV6pvZ2Z5ZaUKq9%2FZGJgIgYUIcJ4ez%2FxRdKXj%2BaM1Bk6agbgvIQCx3GupgIRfdIhsqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOIixE5vLZ7QL3JnAircAzIwOeZ%2B9eog7lfugWm8UZhnoLzaEa8OkiVa%2FtR%2BdzKGcysUeXkjBYfc3c%2Fng4Oe1jjMNJt94g2nsAfkjm4EVLb%2BTRDLPkku4en%2Ff5JO3A5njyH4yaczN%2BNEKMRN5FJ182SSBfH0ZZJeufH01rCrAHheCMFI22GhrgtGoJHlvMZVEwmhx%2BDNoeeJdraj8%2Fg3mhBL2XrGc9w%2FsFqpZaF3GXn9HTsG%2B4M5ThUCAm2MGW4VnyVhACNCaSkT%2B21bgq2BOm53bgcg3tynLxCM%2FsQ%2B8vz2DO%2BQZRyAtRpYfCpzwGdHB5Nq6%2F1SqUfn0v0nGdZkmLoFNNYfBGFAmy6UMcw9D8MfXllxuUY7GCA4k0ADlTm%2BRwsUEEOVXE9NMxQn7t%2FzQeCEFmpsvkyNZmYV6IN9kTnakAjpu9SDofHSSGsOaRoEX6wZKF7J%2BIAzYDFgY4vwQSbs4ONF%2FyZOLLUo4cwvvN%2BryKi2vyg7XAqQ%2FOEJ%2F8qh4hJM507fnOTj5cLA2MFEXcghSBBP0cXslSGS94rb%2FFaOkeW9uEYiv93MAFEynlTtVJ%2F6ruW%2Fi4apTvDYeh1h4sda1jCqtIVtaJu7DtewlHmCqufsRKTAVikeoPf5tys7X0HVEoK4uzTjpokWMLG%2B%2FbwGOqUBVBjf%2BppJlzThVEYsSv8w6g7rBh8%2BySrQmDVff5W4pVLnjWvgSXboB73K9yEQjRPd5n6QitowBihvyKYFddk7Cot9rPF%2FKhOOkUUaKNiR4ionDabkIp22JIN7T0uWiMTeEHDKMOrU%2B4BjepkRmE0NsYhcODSZYrNnIn5fDUU9PAtAXQLkdxUuEmYDqHDq8L8TQt9JV44tJoV43NyiEpLyeAOs%2BgCg&X-Amz-Signature=14ad4e773ea1d43778a24501ea35a523b8db1ba14c325a1046743ced7172809c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VZ5VDLN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJfaoBlRx5gUHTCnWue4GFPjTZJUZZeXr8uRnNXxNNqwIhAOnI%2FqBgqttJgusNtMfmGzr9av%2BSpqXF0aMcIswVDiAzKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlHHVV7Kk8pB%2FZXiYq3AOwKbkZQ3Ec1PhpWXspvTNeTmtWcnleN0HgJqdGhjLpTT5zEmSR%2FC0RbHK0sjGzmP1kkgGuvHDzgWkEDu2uvvxPufzD86S0pm1VI%2B4U7D4207isTGzTl3%2BH9C7bUuw53a131gnw9bRpBvGMUFBfU74Cq8PbgXp1bBOr2bozVKmec2TnF5YHYNODZjHbVQASIH%2BqG%2BSEB1umFC2vYdc9iUSclYvl1CVbUnQcbHT%2BkmGowC10f7HQi41tBtzGyc7Wav%2FHezyHAHO2PbSIgZoP%2FY1rrCnzLnPKp2oXne60V0k%2FFckLxgxRPO27I2392BZyHVu1VPrL2plQs2cFrRPnIQr1isVMPrpvarOCyOYzgGrBQo2BIvv4IIskMF2KTI%2Fq3dakjUc2CPqctwaiyuLYlASCH0wQcCAjvTyRpdqMB9zCUyXAc4ihmDQXvRiMSCuX3KD3kVN893aJ0ItR3TEcXiIKotbTtTv3myVRqaIp9B9awACZbUP1LwTNvXK3EAIHLRnqRBtBMt3NKFRliXZL2A7rCahRF4eBN2PFl0srpkkbnd6Q5ImDBZx0bdh2Ql8B95nzR3dlVNuwZrLJleUzsvuh0T4kX%2FZExadRq8JqG2fVwBsX23XjjGzdBjJ%2FVjDSu%2F28BjqkAdpCUVFqgOme3nCk59tcpxfIJm4NxagKwdK0MM0aA77H76JnF2GdcvgcDcVUOuUnQ2jzZ5sJDuHGQJCHuZhI%2BwSErAhrGdgumR3fgI%2FSF9bE%2FImWErOhoeXak3%2FSeqcrrpQ1WeE8zWRyFlzJJ1yPmfF%2FUmoprRK6bR78YRupQJoGK6F1dALZjZYZcI7saKgPgLRvXM2NjwWWG9OgH8dzffyQlniZ&X-Amz-Signature=0e3e618a61db317751cac112ec0914ac96864cf45fb71029cd0ffcbd8724e50a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666AZNV3C%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC6uYKTKvLpAMLqDOWrl4TaApEaTixcVRE6%2BoZMMyQLuAiA3rEheuXeGOe2%2B2sxECN0NX65uC2P%2BKfo5fyufWf6vTiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNUY4es1CTRK4H%2B6SKtwD%2BpxT8EmiZ%2BcqlzOrx%2Fm9WgtOg521sRrtGzb%2F1o3aZth2UUeaQnhZgySVxTvZvix3Mtq3PGBHscTwivI%2BD6ekyrifyKQcwvb5hRcdk0ma2QXAp69cMW9iZtk00aTiyJmFejF6CqCCepFU2%2FrfEwCd9DWnW72d17wdH%2B%2Bk4BhRwkbZx2ZiL6mQX7aAto9JvSgWhtFEB%2BTlYeZDzA7fJIyR7HnJwey5L8EnEJNqv7DbZoLZJMrfr3FOvaQDqZYRsChWpcs9F6RnnY2Zx2Ey5S5kPm7TGME2rXs6mRYt2zh%2F8oWXlTdjrhxssmg1aOs39mD7KTsee0jSFJuyWYAQyn5nJdudNlis8mKpaL0TKvnBvsaVUE8BIO6MG4H%2Fr%2BFEUJRn48bjDzB79j%2Fuedyu%2BVafK0%2F3ngdIahlic8KLOCQRtwx5Teqo8VXOeOhTc7%2FuXOu4uMBXMeOPZLlwKNRgG1w9nmr71%2BUJWJIeoywcd21zxeMImPVvxzISRR9CExsBvetzgAjAaeGPrsb65trNzO1llF6HNVcAPfJsx9f1FIYD9IHykUdaVULSJGkMEzVg2en%2FmGHWGfpdHltYiD7k7nZRtAejQWx%2FruSvoTLQBQVplRuSLyJsA%2ByZ6Y4UxW4wm779vAY6pgGj5d6zNTf2ScOwGCOaQik6s5tIsrgRi2t05Jbu%2BslKfPR5NUGbkgV9HGSe3Nn3hrs9pyY7QfGK2NEYp5zICZiqL8NbFI5Mqaf4CMjsRFWNQfRPa8LkYdccQt%2B3lM4qjoIISzBN%2BpZxLbo0ISa99w1fuwmmmmVczYcQv%2BrdA6JvHWlNaVsMs7MionbBLO8Z2bdA0pmbTVIahHW6zTzP30oNEOp%2FXaaE&X-Amz-Signature=a37cac8ef0d90af0d0153d49b69fc67793ac2c8cff840e9b94b72011cb336814&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XTLSNTV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcg4aD7%2FioiTx%2BHs5tY6RIv5UU%2FxOuPLpRq2CFUcanRgIhAODR497sB8L3Lx2ZnSd139O9lHuJ7DmNIfYXnEetOjhTKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzXNYtL26p2AWN7AXcq3AOMdTBL1WKaQPHCFHDnPKxo%2BQ2iMil35S%2BMkYEnG5ua8AjBh%2FqraCw1tkRwRdIuk0F%2BG6w2%2FlyEKUa1zNa7QUNnrL6c5rZfn%2BF26t0NyLBET5F5WnRC3bkFzgynUJk9m79%2Fm%2FcgUT%2F7dHTmZe8cUFWL3X9hE7TP%2BrZEIDtQY7Dc%2BSLMV11AFqt%2FDmvsbsGeqf6pwe6t53Rf95SUeydCBSa7I9DqEQ0g9tZyT5yFU0pc2CgZPmNSnkdCX6xyH647XcWlVhD4L4sMxdm9kW9DShk3miFFG4Mb%2FN%2FsCKnMAhVzj8jQIiLb6i8HiBpEvnOdDeNaC7drJHQYQrF5UgXayFSRouvlXTRQkF6pRIE9VIYS1BybsZyna7hXM2elhphtS1YRdtQFLJzTb1gZO%2FDk0%2FjXAVhxEc3z0YPc24IgdFYuxQsu50yGhTMZkYCXmuErTiQLJVQ0Xlc4j8714iXifwDl3%2BqtAf2OrfobXdpcKH0gqhJ2KwK7AVTxtCIdUr8Ylnjr%2Bk3%2BePiOsiyqL5ZVlp09G%2BrqT7tEs9GyxQdytMyImI277mDZ%2F2Ut1EaBfNWykIYXTM1MHakzKDnQjfiUKXR%2FL936vaN6UE56L7NKMDxQKAKDMWDvPJmKxkkJujDbtf28BjqkAf5H2mzCvcyhLpnH6txglzCGCRJNL7JdPzz40WSoEhHWV6mPZVgcSWO4DrLNrvb5bf6qTNNQmcjE1z%2Ftv5y1ACj1hiPZRt04%2FpcXBkB1VHTceKa2v1DvyH4mo%2FXwBpCg%2BbTnaVOnrQXka9UtA3r%2FnzdV1KhgGwhP61uhKUGuoPYHCdigjHNyiZydOL6Jsun22KMEoinvNYc6LJ%2FH9jQg3btQvpug&X-Amz-Signature=a812b483af75eae4362faea919379fdec6e83885b1f9ea2f5cb50889e8caf67a&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646TC3YUY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHW8RccZzB23eZUZ%2BzSuf1m%2BDnha%2FSQfa3JRomoY28siAiEApyTV%2FhsdDlzMoTpfocYYlHA9tbyZdurULkZvo2qX8fsqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVf0HoalRhO9978jSrcA3CmxjlIA3KofWd4YtYLtejUE1JPXqEveJgPuQ2YThGU%2B6CnUfmOKVW59iTwSuV1uTSeL1ZYJuTm%2FOQe%2BEIE47rNOJZ1D0NdfOAkiWVhjWs%2Bmw3gHPZUtGoB8eZD254q5mtteHfLfT4nVlHpeH57GkRn9A%2Fykjl84nkUdpns5HhwsDR3ZSKrg8o99oRk0q5OMr5xYxMzspH0qgNVlVpxJIZTMlADMLHtSrR5R7XrErbi7bAE4j61DFTx2qv%2FxgeQPBya4EjZcjEBlokIEkM748shYs7QB02KoMVeCOSCUzm57s0sncSfe94Q9u92QMyH5Oz%2B2JfH4Ck0ng9V2r6yRmM%2BXmEB6HzI4Dht3%2FXPVFlH0KOwUJwfWPYVPyu2HhOt1Nlp2jyAeEVB9xp1Kh1R5Ypj9kneqmWp6KBwaY9K1%2BMubCIWzRf2nYP%2BwCgyxRpew4bAqpKyzBAwHM0TLSk6cgA63ZE0kLA4nz1BoMP2zdads9iBd5D%2FL4j1IZ%2F4C3AUUuJJ1C6MMZq8cN76WnYFVqClc9VGAZP3EdCTQzbNuXR4YbJtMwzdkc4x7dV5eNmHUWoNVikZhgQwx%2FHEJmU6foo8uzSIb6eQ4tjNReGm8Np02G6mN4SNCYyDtlFeMO%2B%2B%2FbwGOqUBaoaYd%2FEZgxP0%2FxxUKXJ0kzFiN8JamTmxrMiAPzHIJcRj9gFf4MN9jMr7Y%2FVp4GLoJnglwYo9Q58rWPYdlGAiu36IvAIxcYUnH8lRIbjuoWTQi1%2BZBJ3j%2Bzs7CV%2BAI%2F%2Bn9g1YxrBXlYEegsoKpWmgff4y%2B8niyOlvG36Hmd0hmGWcg88WzH%2FTYz2kFjkOoUHW8EYMCa4PuNn63psO2CW9fNRPP1l%2F&X-Amz-Signature=a17e496c1335fe1f92c9197c2f62539c5d7c3a56c95950a30da3f9f873718dd7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VZ5VDLN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJfaoBlRx5gUHTCnWue4GFPjTZJUZZeXr8uRnNXxNNqwIhAOnI%2FqBgqttJgusNtMfmGzr9av%2BSpqXF0aMcIswVDiAzKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlHHVV7Kk8pB%2FZXiYq3AOwKbkZQ3Ec1PhpWXspvTNeTmtWcnleN0HgJqdGhjLpTT5zEmSR%2FC0RbHK0sjGzmP1kkgGuvHDzgWkEDu2uvvxPufzD86S0pm1VI%2B4U7D4207isTGzTl3%2BH9C7bUuw53a131gnw9bRpBvGMUFBfU74Cq8PbgXp1bBOr2bozVKmec2TnF5YHYNODZjHbVQASIH%2BqG%2BSEB1umFC2vYdc9iUSclYvl1CVbUnQcbHT%2BkmGowC10f7HQi41tBtzGyc7Wav%2FHezyHAHO2PbSIgZoP%2FY1rrCnzLnPKp2oXne60V0k%2FFckLxgxRPO27I2392BZyHVu1VPrL2plQs2cFrRPnIQr1isVMPrpvarOCyOYzgGrBQo2BIvv4IIskMF2KTI%2Fq3dakjUc2CPqctwaiyuLYlASCH0wQcCAjvTyRpdqMB9zCUyXAc4ihmDQXvRiMSCuX3KD3kVN893aJ0ItR3TEcXiIKotbTtTv3myVRqaIp9B9awACZbUP1LwTNvXK3EAIHLRnqRBtBMt3NKFRliXZL2A7rCahRF4eBN2PFl0srpkkbnd6Q5ImDBZx0bdh2Ql8B95nzR3dlVNuwZrLJleUzsvuh0T4kX%2FZExadRq8JqG2fVwBsX23XjjGzdBjJ%2FVjDSu%2F28BjqkAdpCUVFqgOme3nCk59tcpxfIJm4NxagKwdK0MM0aA77H76JnF2GdcvgcDcVUOuUnQ2jzZ5sJDuHGQJCHuZhI%2BwSErAhrGdgumR3fgI%2FSF9bE%2FImWErOhoeXak3%2FSeqcrrpQ1WeE8zWRyFlzJJ1yPmfF%2FUmoprRK6bR78YRupQJoGK6F1dALZjZYZcI7saKgPgLRvXM2NjwWWG9OgH8dzffyQlniZ&X-Amz-Signature=55fef926bdd4a70d218e9fae5a734ec5bf97caafa4625dd75fb118390bff6541&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNZBJPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmEcIVCNsimvbNZ%2FQVTDIosK6s%2BV94aA2yvfnP9f7dAAiA3xgzFnMHAFtfgS8Onz0S6d1E8TcKky1YytLvx4KNygyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp2wllEZRc9CNIymiKtwDVV7iEinZyafGWvyRdNzlfj4qHFuH1vlxnlI6KkWQhISc6kX%2BS%2Fs4LqM0kuSMOmluldMd6PBsSfd7LWOG%2FdAOox%2BbLhhSdWl2OsrGwvKJNnVrFBXyYW%2Bi3K8qJR7RNt5aIdrFkIj3DAGNzVx3zX7ayXn7KRFuACPwA1fwxnhNxOiVUATRsGNvmD48miYkkGOsj7pWd0cWQA%2Bc17RWQD653W%2Fvkom09LGBv3AOsyTrk%2F%2B%2FnNTBpuDdmVZAYzc3cjc7P8Z832GTEYgf%2B1qoeuZMb2Kvti7Lxcvr0S5GDAUZvQ7BLDgeWZRUwcfWHwQO%2BDtAaxbAqo%2F0nSj%2Bc3P1JyNRUxxC7O%2BtfQBHmqMnxSzaqIuxdWmf8iJtk3wr%2FP0YJoh3BxwAmQijwLskVeDUl28ayTvxsCVDxrAbasLcxXkr6CuPkQQw5TmYRYNHyxg36INTeq7y79G5j1ZH4krlkifX4HZTIC%2B0G2wPEd8Bks%2FQRLhq4JRhllqPcFpRHCQc9cibJhEX6A2HalFU%2Fkasu%2BMCWNFZ3kFlEq0Uw8RP%2F5qI6zUKw%2Bc2k9XnH89DaKftu%2BpZjC46QxiXKWduCBqArpzMYFfEJB2pxsHJxtbxuwYWvfCXdkKqq7pRYbdKb0owxLb9vAY6pgGkW3EACeLxGFJwh%2BC%2B8ip%2B%2BMbd%2FLj0SwL8jRl1EiGggBX5O1EKRSUg2qPSsaDFnKkV5hGr8tqPeJATRKONpEphWQEYbXbdJaFnFMeMM8JVM7ADEi2mvCdeYy%2B08xXzDiFEAD20Tnx1N8rM%2BelDj0Oj9b%2FwgHnd%2FN4DQ0CAsQQvMeHZIvHSyLceU1Iuqy%2BgkpPkYnsvHLCgwekr5VWb90RdNW2HSHEH&X-Amz-Signature=f08e67d1b19e8bd8c4669e430342ce58a03b5956a4e976c22b4cb8fe6420934f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNZBJPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmEcIVCNsimvbNZ%2FQVTDIosK6s%2BV94aA2yvfnP9f7dAAiA3xgzFnMHAFtfgS8Onz0S6d1E8TcKky1YytLvx4KNygyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp2wllEZRc9CNIymiKtwDVV7iEinZyafGWvyRdNzlfj4qHFuH1vlxnlI6KkWQhISc6kX%2BS%2Fs4LqM0kuSMOmluldMd6PBsSfd7LWOG%2FdAOox%2BbLhhSdWl2OsrGwvKJNnVrFBXyYW%2Bi3K8qJR7RNt5aIdrFkIj3DAGNzVx3zX7ayXn7KRFuACPwA1fwxnhNxOiVUATRsGNvmD48miYkkGOsj7pWd0cWQA%2Bc17RWQD653W%2Fvkom09LGBv3AOsyTrk%2F%2B%2FnNTBpuDdmVZAYzc3cjc7P8Z832GTEYgf%2B1qoeuZMb2Kvti7Lxcvr0S5GDAUZvQ7BLDgeWZRUwcfWHwQO%2BDtAaxbAqo%2F0nSj%2Bc3P1JyNRUxxC7O%2BtfQBHmqMnxSzaqIuxdWmf8iJtk3wr%2FP0YJoh3BxwAmQijwLskVeDUl28ayTvxsCVDxrAbasLcxXkr6CuPkQQw5TmYRYNHyxg36INTeq7y79G5j1ZH4krlkifX4HZTIC%2B0G2wPEd8Bks%2FQRLhq4JRhllqPcFpRHCQc9cibJhEX6A2HalFU%2Fkasu%2BMCWNFZ3kFlEq0Uw8RP%2F5qI6zUKw%2Bc2k9XnH89DaKftu%2BpZjC46QxiXKWduCBqArpzMYFfEJB2pxsHJxtbxuwYWvfCXdkKqq7pRYbdKb0owxLb9vAY6pgGkW3EACeLxGFJwh%2BC%2B8ip%2B%2BMbd%2FLj0SwL8jRl1EiGggBX5O1EKRSUg2qPSsaDFnKkV5hGr8tqPeJATRKONpEphWQEYbXbdJaFnFMeMM8JVM7ADEi2mvCdeYy%2B08xXzDiFEAD20Tnx1N8rM%2BelDj0Oj9b%2FwgHnd%2FN4DQ0CAsQQvMeHZIvHSyLceU1Iuqy%2BgkpPkYnsvHLCgwekr5VWb90RdNW2HSHEH&X-Amz-Signature=24c97dff80ee8d48018d833160ede269ebf61d5918fd87238fef7e8bb08e8823&X-Amz-SignedHeaders=host&x-id=GetObject)
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