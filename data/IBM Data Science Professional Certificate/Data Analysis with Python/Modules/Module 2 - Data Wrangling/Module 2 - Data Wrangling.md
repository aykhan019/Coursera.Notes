

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW3OHA26%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFxOZo%2FdLgYlA64E4CQWv0pcMvJZuca5VTlHSqDMSDUkAiEA8USRK%2BI1qFPFtXZMX8txmo95wALJb4pfIk%2BymSXS0PwqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDud837Ha54FS4lKCrcA1hpifhnIIc68KQemZHfGa92vJKMyXDbTmSLsvPzQmJAbi%2FIT7DveDa8xb8H5TXFgmQCBPe1gEoPT62RjNsAsM9ejMS8TBrRzryE1iezNxoSED77zP7z1IdRCGSO0rKlfG%2FX4eQkZ2GSTZ7jUGGOT%2BKv13C2tTc188S5ePxU9%2FkPTkjKKCPIqsAbPEjDPiweUlc%2BtoQLQroD%2FsVY1PZ%2FF19Mra%2FwSBE9mjJzeFDplh%2B7UMYDJLGAppXYToYSw0nOzGje8Rx7RkRDFrUqa6FeTWr0Catt94JnLc54v47C1tclYraUd6n5uhpICbdQa%2BMgzosZ2AyR3wW9hahmrG%2BtGSC00Q%2B2iaR3JJxYFs0xkvRy8dDuYK6HeFivQfqXGBbPegrxQpCDixn%2FRL%2BDbkdxZ7haXZyh522P8mHmWtq1Y0HRxnhAs%2FPeESNGlZI4yHtE3Li%2FKochPN39Ue2Kys%2B4jlaVBBApZFlsehwLo0kLSwhLBhWH1K5oy%2BzJrxsVLbM2oYRMYril9gTxsdr3vXTXUEAzo06nVsnMWl1%2FxAaFv%2BcFGgP3d56a63xGSF9PuJjQ0ijXa1f%2BOrcqoLNlYWSHaxLKKC5gpKqNvbannT%2FqIOcyn7HFYnmB3HpSZstOMJq5%2FbwGOqUBkaUX5sdDujJ2WMDIo5hD8iiTAOswvmHcdI%2Fq3upe9hB9YrLdTzL2Qjlm%2Bn7wUO14B4APypZvdc%2FdLji1LcX6bEY8Pwv1hHa8ruERJhtl60VnWn7%2F0otBzoPFahwU01VzA57D3eQ0bhmHOTguiZF5e7PMTSsEmNo4X2VLUAvh%2B5RkZYLVa8LFpCWDOZ%2FTNmH%2BkchK5EJ2pvTKhwpXVbH%2FMiC%2FXsCf&X-Amz-Signature=b348b37c8fa5d1d5760a63215321776487c7acf5991d651c102a55026c6af684&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SELO7U3G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9UbWE7%2BZCA57Tb2vDYzqrnw7TupLqOEmwuQF0TgymdwIgZgBLJdinb8adUQ74YREvoQmK2q6S6vd4vA%2Bfw%2BVniDkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJPmFksGGi7q9msJoyrcA0PSdQ3MZ8doHOjpWjcagOISSdcsMMC9AHAtgKYgXormoVVhRyq%2FWo0BAbd9kH4MbHephuuJXz5iSTKY3b27TWJrq%2F26y2u%2BaxV0CAop6qXFBZuUopFCe4ZIimD9i3dDvD0buuN4c1Yr0lADOP38QAtWt%2BaTj83cH0KipkFIkdPD6xYTbTyfDyqOZcVXEUZfGwiN6n7CN0mTl3jSr19QekFxoXgxORB65SxjSoiUPaKcO8JtmFzoUlS%2BiX%2BmioGUHcgDxBuLzz4HaG1z%2FwIe%2BE%2B%2BNmA1WX9MTYLn%2Fdpf85rfQEhieuJNL7yXew4wYkGKtvqXZlfl5etDVdUoSGlNAzfQlfWF%2BNgcgiJzy7Jb0LYGMnj2i0aVtX%2Fgk7yIVOKhyWf68TsSTF0djODL79uynHx2bhl5zdNNiQJyIV1gY%2BmZv3QM4qpBSWogHsiFTSgqM0IoLPipJELKl4ULaKwf91quqHdBWTgIMc9wfrjNEH4tVb7pp9CUwYtDt6Qr4AgbaCb5bbfQqpc6%2B68N%2FuNdwtsEcVjGClCHnI17V%2BLPX0X9obyMswjjpXyE4cENePBFKJdwg953ZyCekp7DhZAUtH5yPQZlQSQp0fb5bYXLA2U0Xuc%2FNVRc2xJU9ORGMMO2%2FbwGOqUB6owYZUnNi7vWJNejnb5PjSjasYhVrl75dxJW56xzePmIv%2BEQzsI%2FnzUoQeGxhhqKw0PqeHn7QiEILBQSGCaGk604CqBOSpA73gKY75Grb%2Fj5rIUsDnaIe7axvkiiCahSdeQp48dKU9z8whD0DuF74b0KmzH4bCn2levgwdBlcAuF%2B63L6BKzquh7KReWnQUEIR6z5v74d7QoGbV%2FqsTMFmkAEeO5&X-Amz-Signature=6a574cdbb8d06992dc5f3826bdede96a99338188f42547c94b52609b3580e962&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULVKHX4D%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBsCoMc8FmAfrlx0ZbnuhFWFrbBS6NYARBtdjgcVmidAiBgQ28UsWnNla6PMKdSS5JKYkSSN5WJc%2FgfEXmvOuBdlSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgPCaW3xEkKZrQ8u4KtwDbHTckWBW2cLxmr15LRI%2FLQx%2BeJ2HVXhPfiAs8Yx%2FQg6a2v1udlJ1DeR9U5pj40RnO890ZW3%2BaML70AYu%2BE2Lk5tMm7nH7PuwyQaOOS%2Bl32hXe674lqVBhRTFmz2AlJAZEJtGyYXYzAzzDBzRsicfBnPScwkeSjW8r8GenDpTWQk8xdhNm5jOvI3i4ofsbHhA%2FkJfEOV8%2Bm2P6L%2BrdgypXOJEq%2FF%2FiQMd5juHJTxTFFP1Yv0ACIsCkkDc5MrPBWBaTEq%2F%2BGFEhdV3yNy0gjJYBc%2FzC1EXbLSdjIxfbZa8zz7ljkk4BNRtuuUndGb7OYiNAKpEjZVoXu7uiAt%2B87x3jELjUdF2DW6%2FWYnndMEOR7JGICmseW%2FZiD4qf3C7vSGgH3OuaHhAEHuvMA3b6WI6eNRju%2BN%2FQGvye3burqH2dVewZu7MuJ%2FXBF7Dxud7%2BAJ8Phsj4TqYy21YryHZPOwfyPO4EdRY33Izt%2FRfI7%2F9trhX46N3F19ulMSTUeh7ysJXKw9tB7ia%2BYqinjhRbBvCYOL%2F5xjpjAD%2FsX6RkvHZ%2BMpyd0KSg5mTNnmhpDCEetxkyXCPNpoS8Dt4Dsib4%2BtRd3lycyofIT0rnrSIK5dp0e2oDnUcwTCJ7ifD0w8ww7b9vAY6pgFm%2FBJh%2B5fgcqKtcAsB4Xo5AbxrKudGAzMb7i9Qbiy1WZoYpaeqHo7oladKja8wkJGSKIcX4%2FHEYC9VrqKH79KleUL%2Bfkx%2FuoNGZdtzLHT0Rbhb5y34I7C89R3kwRNX4Kk8qffR2xoRMv%2BsAQKs3F%2BKh1eMwU7%2FoyxnzjXQVEwB%2BxVOnAufzv0i8o7y0WKSDo8q1sRzG%2BKSsottTubCBqvSp08mASIa&X-Amz-Signature=bb99f13b65fa567d0be5a5bfb904e86a8a4220179f223c6442ac5a7bacc71fb8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3PFLPC4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGq3BuW%2BfRIkUqwR9LSlaDqhMoiA%2BlIctIpomhSS0wMCAiAI2w36MZ0df0sRdVqDNGIZYZS2sotfW5SYiOgMEHvI%2FyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgv4nUbqslge57rDWKtwDmm0SbuMDz37lNyxY4q2y%2BmIRxCnqqM9nn96%2B1hC689WruNjnT6cjtKyaBJCBTWHoOCuGxVPfCN9B4vZ2%2FA%2FPxiBMf78hIFV49NSVhkt06i%2F%2Fl0KaHvHV6gZ9%2B8zHafJvUcRfjpKxzuJ5xKx0M28%2Bda1ZlvDgZWhoqU25fVv1q3RxGv9GZht6VqfYMSXnCEU4uwq3tGZLkbZ4%2FlmaChNCiChlKXi6bdfBVJGXN1KP%2BG8x1Wy2sz35%2B8C5QfVmxWHj1Q8gah4TWCClqMitm7wjHQTMXD%2B1yz5Q8fQi7v2IQm5ef5W3ZK%2F%2BKK3n1LWT2YzNJ%2Fzr6LzByBL7v3Z3skif3wiWVHX6IoiBXOjafqkvB%2BPJH9akVmgr%2FZTKzaoCW6ZiWNF8TJ%2B2QkkpL3qjWjSvZ8j4pgaQD3LNL1QDeKoiN6NOcsIGzmXpI%2FmNy92azAWoVAAIBqvF0yy8lSaJTy1TYWNMYfCxXQSk3ULySRL%2Fudai%2B86pkr2YzNxhx9a9FA%2FSrVzFfVvKBCDaMvIQtZSiWTEEXuzCJdewf21U%2FbkRHL5B59atRIUVfJvmrUgVqAh5MJlLXdC%2B0QewAUjsJZqjcNW8gtcuF5L%2FlmEkOrELduoZo0geA8Ua9TiddHkwkLn9vAY6pgF85VQEGNZ%2F3Ht1Kb3Fbz4kwhOEiyzZS%2Bkj6bcN3nE7vruj2nB6c%2Fj1gsDEkIprxdYb3ViP05cACfqBUdJZ1q6hYlLS%2Fc0CJnHnYtawnHgZnoLSLxGJJPf2vcPSVZ9neB4NeUlXYQm9nqhjehTZ29zxX2I9oszN%2FBh%2BXO8unrCNX03Dkz8gsKeLd6lOvFda3axP5sPH%2BCHqF0dQ7BWSUpTn66qF7zu%2B&X-Amz-Signature=c259c674c06aea8c6dd808e72d9166701f5afebfbe41784a49ffed3c08a5eceb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGUGFHBP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFXZfwDI2xBHP1iwVAB71Ob%2FbWl2OKC2HN%2FJyNpdGJI1AiEAxdaH%2Bu5xl%2FCVVmk4AoFQ%2BGMDg%2F08wqU0In%2F2RTOJEf8qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL8SkBk5cNqCBJnj5CrcA2XqE6RHg%2F%2BfreU0F6ff2U%2BypgoOqR2qvdlYAJzcOKYcyYC5zvHDHvaRy7T%2F%2FHZgupZ8Ve0DRxT%2BLuX9jU7YL8ZU6AFnnT9R8YUNtrwD%2FS9DMK345gwVRjq6hRN4J9eJwV72S6OUaGjsjls619INZ8YIi9woeqMBopO%2BwD6CAT5A6gTBi8H4rp1%2BdBZVInTeF7TI5x2njyh%2Fra15WPE%2FNLZXlVnJTmpFimvd%2FObn6GfuzrHSqoHKNNuiticvCpGjtA0DNqY9AAQBtRVQdZuw47KmlNcEDm86PbHxpOZHQ7Qiz74UttSugpshY9i1ltKFuxMwarnxGYHSSdxEIRkxrvSUXZ%2Fldat7MaZe0xTRpkT52T6sZid7W1FHAI5mseP%2FhkEclZtqRfuYVnhgxqFyaL7A%2Fkkr8BFqc0pxrS7%2BGysi052YmQhHVEqD01%2FqpmrFSBRe0U7JCiQVUKPuncvEutNrNuQeQ5gUv%2F677zQwCZHVb%2F59tdpZ2KxtwVXkaXgPvFbtmqugxFX2UyPglqIzdN8bziIhCUuoETGIlTHuKsjPpphKu4YloNz4tjZlJp1EVPbupRowVLA4AX13UqxHuwwoexo7ZKIurt5WNKkR0mx89B%2BTz2l99qdTUMH5MKnB%2FbwGOqUBFeGi8DAR8gTOcgX2PJ1hwUwzVZBlfiHuTQNRUuDcvTtLP%2BVwUiNt2Y8%2BWEeU2BgNMaF694dbKKTQfx7EMMYJjsjHouEaGePLtlFvkzjpP7UNud9OSWUQnClh%2FkNZ%2FK%2BBMN7uT6Sa%2BzBQLeiW5WRRwGoKudGHMs4UYFymr4UtiF%2Fi3Nkh8LxsdHE%2FG354pgDjLhWSIpPcgJ4RjIAkr48cOowM6pFe&X-Amz-Signature=ace24f05533f29df0be1313bbc39fcd639434d99caa23ae93a76bf5f990ce26f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674DSN2V7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICgwBYQ61M6Z9mPhO4Ux14FQe8owGsc9AcID4UEuGJMzAiEA9GbcDoamvkW9pp2ME6FKyrIERv2B4vl3vUNPkCpl4oIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE8jgeX6LCWpQkxXoyrcA6lkRHd4mv2n5r8rrUlEYjOSBSTUF%2BWFqkyxcOqJEfcMQoy7bPj3d%2Fj2kimsmWc4MzbLwxLMYEtgk2NZrzle8cGAmMTHf%2B0fKamlvMHDmeJqYQC37QAHOqEEdEd3B47QQ0SR%2FWVnoW46DCazJ%2FT%2BxgcOP0HVKE2QjrI7Akg31w6x%2FmFKHxbLRu2QLJf%2BDkVqOBO%2Foe%2BQMGbzbm6%2FJyfXSUM4fSTj7Awo9SRNadPSDgsxSD9WBLyxHSi4yFqpvf%2FrR1Ns2QbDgEPbXRzsbT5w98IIxmE6ZB5mpLEvfXSE2uVAPKMi%2F4%2FyEusO5MjGtj0MzyB8Viea8faZA0sKyd8eiOhhnHBB3Lkd2jrTXlJrbBIyiNFedzuD47q4aj91eqDsmgQlGcBrsnuZp5kYhqaWTN5CFXfnotvKsr6RniMvFIPaZnLIWxEMhzk5jV%2BlcXgcSrbgkmB6EIsljjIPG0oHnBcxy44PCDGilr4MYGv%2FhQuR89pVi7UVTf7hnSJr1b56ion52RbC7Jy4Dn29wjAdsbFhC6R2icSRq0SUvaS5RBkPI8Rw6Bx7B1XBIpMGS3GQh2SW03R6hE0CI8C0xmUYa3S8RF6o7XcUkLGyw2Oqd79Da9TwQGiR0g7YGN9mMI%2B5%2FbwGOqUBGwEz5PBo5Pvxw9SfQlCgWa3Ys3z1gkAUl8pYcLp2gcbuU1cuMeFh%2Bkw99l3r%2BLrpN04ysBK89NckYdxDy55zWwnl504JyI5uxCTK%2Bql%2FXePcTrZm9uSyKED9BqAH1fO7Y%2FgBmzxEz8HuTAInq%2BmFWJzHHooN0E1nTDfmzFhcPSy8TYNsaNc154veZmrGedm7Qace7abs033LJxu%2BRYUz%2BkFdgXuC&X-Amz-Signature=e26770b3b7328d1bc1b2048768981681f392ebdaeaf0f7460ed506e22202a997&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IOTXEMV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIXLu5rYA7qRw%2FKp7ebN97vCxtLXx86m2h2r%2BqdK3eJAIhAPUEyzgOEI%2FMrZZezcUrv5NoGQg5cy2WfuvA4sBwoWwsKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzWmjix7A9TzRAJ2D0q3APZPp9E4oZ2V%2BR2gANznZ0yNCuTwGuR91USn%2FFHYBgf8JnmEBlJS2wQ8Q%2BKYoHuAPR8cMfmM6KhC4se%2BDO%2FmB%2BZjXbcUOUytGy4xyoiaB4mVOfQ7BNBD1jjG0woO906hfoOK0e5c42f4Ydn2gWgxczCjddj2cjNncGljx%2BsQzT8FOmTm2jfssb7O%2B4Ye%2FZSZuCGPAGtqCn9wEY09tsSD2vujcKvKlbu5pqSjwGJd%2FDXImEDPxKFraPpgxUcOYgwxOItk%2FPncGJ6zuEUuTYKXRdqZFxYeagPdgYEpjPTZf9u7E5fnas55wVQMtWAUXT9OgMmVSLuyPSqCfWi5cRvNdpj8cgvzuD%2BDfsT2I8D1VM%2BwLTvBfkKkUl2uTSK1PC56hak2CHu3gvYvoKcJj7qmCxots5y5dNFxeLUaaVqUowW2Wkt6i%2FPKkUtjGLCzkCNSfEDdkuj9d7kLu%2FTa8SQrbElYsFaaLkv60ST0rlS8VauXG9JviGppf4bUhupOtD8K9Ze7W4VfLCp7vazrQnlnGcGje%2BPhV18tyOygRahh28J0HTXedu8g%2B5CD7bnGz8RmpWVcUg99qdcKl1BLv3TDTkPs3QoH1ku1HSsEsiliyrVDY2%2FG%2BOpMfc5Qd9MczCQuf28BjqkAeKjbNX2EwZbfiS4%2FG6yfXCqK3baBXVPBSP92SALfJxM8ITJC9JgxNmMDAsyERVIn4x4LiaThEtzvwTllQl%2FABhjodxDDMH%2BehmhUuPNsjO7RrEdt311Jkbz6lexXsjigyd4Y6v58HBtcUljOV5Ic%2Fiv2r216XJ4gPP1CCALVZ2VOzAulahFS6YUF21rdM8%2BXxEm81ua8LA2NIs1czhJTegLsPqD&X-Amz-Signature=09945b22fe3956073eba6c788c9f80fa3498ce81ad80211a8cbae1d690e8404d&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYR4BJKX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAaJ%2FncDLNFZ14NjLl4J0cTlXwEAx1%2B6%2BtUfgwprC2p0AiEAnDWV6a5IWLhWO2MkZqmIDDzzD%2FUT%2FG%2FUW%2Fsy%2BpfSUqgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGC%2B7i4KrEbUOdT9HyrcA%2Fei77sGCtktkhjiE83LpBWjcdj3jrvHHjFrzg8oxqRYKixHpDrfcxYA8P%2B4biaOg%2BfRPBAqyWQrhEcTplySJ3jDDUwaxUv5GmBsrrUMkm%2BnuaoXVGbaTFcXfD9%2Fvo6uF5avSvZfwQSasxAcvo7vjN0ulEKymrlp1%2FLTKKL43pTKI9FitQ6lpfJT4ZCKqgrnQNkFP3LTDKtLb2OVvKyGIviKNA6nSneiII49S3iFqPJFc1HHqGqeGeORiRSyWofNHvMwKArG9qh5nP6%2BMO%2BXlAIHpRR3lZhRcB3iTkheSdVlrHsle7rAVqkftHiDglbR9CxY%2FgL2Y9jbKAAnb3BvmqWtvh%2BHAMXDF%2FKGzGj4djfSFynLp3izJNWnz468cbG03pXteN3a68fDnoxQNOlE1PHzjduEWc2p2N3WmGAFkyPUE5pxX9SSSpy2Cwoi5BGaHIpNZb1cmkZj8r8gar4HIvpFKuv0ZT%2Bf55dHF0WiH6wIXIwXM2gqNBDgEnNBUS%2BKUqU%2BSl1JePDbq6YUEEYmMG3DXoyl6Xltk9xFefqMJKz96rKqvcpmLm6MHbCjN9qQiU%2FWMQeBMOBREXB2Wu%2BJigSeNfGKZFAuGSQ4CfP3eSgHI4qzmtQA8a4rlbKTMNzC%2FbwGOqUBnytPBFP%2BetN%2FSicf9A%2FZIBfRglTaymuxYVRA%2FJnLQ9eWLA5KIRk5HqqAcIMEOHPNglYLzWAAuqO77TjhSOVYywBjP5DJCjMADM%2BpVAZb5IvunWyNrNy3%2BEkTaksHZAZ3mofolUpuXvcJhU1wdSPhtU9aXefCYMqtyKvAnz4MCvYmtL3PiqaznT3YLqGV7fXCbDq7q0b57Ik44iDyg%2F7c4EPb7%2FAv&X-Amz-Signature=4ac71017354c2a3bc8306a177ad00644deb36bcd4d65527a8cbc1c4e43ef516e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGUGFHBP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFXZfwDI2xBHP1iwVAB71Ob%2FbWl2OKC2HN%2FJyNpdGJI1AiEAxdaH%2Bu5xl%2FCVVmk4AoFQ%2BGMDg%2F08wqU0In%2F2RTOJEf8qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL8SkBk5cNqCBJnj5CrcA2XqE6RHg%2F%2BfreU0F6ff2U%2BypgoOqR2qvdlYAJzcOKYcyYC5zvHDHvaRy7T%2F%2FHZgupZ8Ve0DRxT%2BLuX9jU7YL8ZU6AFnnT9R8YUNtrwD%2FS9DMK345gwVRjq6hRN4J9eJwV72S6OUaGjsjls619INZ8YIi9woeqMBopO%2BwD6CAT5A6gTBi8H4rp1%2BdBZVInTeF7TI5x2njyh%2Fra15WPE%2FNLZXlVnJTmpFimvd%2FObn6GfuzrHSqoHKNNuiticvCpGjtA0DNqY9AAQBtRVQdZuw47KmlNcEDm86PbHxpOZHQ7Qiz74UttSugpshY9i1ltKFuxMwarnxGYHSSdxEIRkxrvSUXZ%2Fldat7MaZe0xTRpkT52T6sZid7W1FHAI5mseP%2FhkEclZtqRfuYVnhgxqFyaL7A%2Fkkr8BFqc0pxrS7%2BGysi052YmQhHVEqD01%2FqpmrFSBRe0U7JCiQVUKPuncvEutNrNuQeQ5gUv%2F677zQwCZHVb%2F59tdpZ2KxtwVXkaXgPvFbtmqugxFX2UyPglqIzdN8bziIhCUuoETGIlTHuKsjPpphKu4YloNz4tjZlJp1EVPbupRowVLA4AX13UqxHuwwoexo7ZKIurt5WNKkR0mx89B%2BTz2l99qdTUMH5MKnB%2FbwGOqUBFeGi8DAR8gTOcgX2PJ1hwUwzVZBlfiHuTQNRUuDcvTtLP%2BVwUiNt2Y8%2BWEeU2BgNMaF694dbKKTQfx7EMMYJjsjHouEaGePLtlFvkzjpP7UNud9OSWUQnClh%2FkNZ%2FK%2BBMN7uT6Sa%2BzBQLeiW5WRRwGoKudGHMs4UYFymr4UtiF%2Fi3Nkh8LxsdHE%2FG354pgDjLhWSIpPcgJ4RjIAkr48cOowM6pFe&X-Amz-Signature=7c615812ac1a2bd54d42e045f358591cb1b0b20fd600a495334dd868bd43b8e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMAHKHSE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHdA0TFQVu2hTVh14JTIOdaKGGRraJq%2FEzDVaR%2F00WpAIhALpDZ3IWWQckEfeeOkvaFYRFEbFxuY%2BMs9WPzhOfRJFRKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySQTdkLREAvMWLeGcq3AOFLlYNM2wlDm0qZ1UkbojMgOqQwdFbcMDC1LEeIhgYxn7ZNwPxRHFubAe4DMy0oeMKSdvu92KyTkKTirKfZOUjpKrDabo%2BhxRF1Lm92QUiPcHgF1XIcAdBMDQX1BMnv3Pl8aw0FBARiQnL1ZKkalTzieLtDGvheqfKgL25kAcBvLL0hjPKP7P5aNtFbbuCN2RQTAh9%2BtpbLXtHYOxgupFT0UflrSjxL59fSi%2F%2BDIgmL%2Fo3ohh8pMhMjzJ%2BCEVFMEXjxy0UFdQyNa0PW7iO%2B8sVQL1v6OAmW%2Fh5ba%2BoDPgJ03OZPexIu%2FojKbr2QvLVq6BkCABLdHdRwgCL0gejDD0IeeTRbZI4z8H%2B7Jlt7ZqTsKkVsk4E7iOoaUULcDSM1azjnpp29%2FFBiGD43sgHmWnyb3zMfW2onVza%2BTOlwbQu4sp0KC0smUlGqsQ0EM7EO3dbbMrZvgIHhg2r7xX5uk0ePx00q9E%2FSiGsuXUIvTBvKr8G44mXTJHQKvdQs34ThRPAoueLgwsIyyvELo0ojhSf78u6BJhYvheTT4tgYAXL8yyRVM8xIsWTh7Re1l0PyKljru8xPwkCRvSnaNsQdcgfNIAQBaEbIe9Qn8MkG7XI6oltUpIa7fpu32RH3zCjwv28BjqkAYIXMkEWgAHTdmMVzZAw7Ls0gINcYPSNUBEqsDj9gCYI6XcnHI4RjQd6KiPU2L5U8AK9kuq26sStK8wVBDi01pCnWuxtcgqOoxu2f4rCc%2FBe6ozmIUwOMnDa%2BxX0lTBawsZ5FNIEUfhJekjZSiU7hmSDQBxL7O0e%2FZ0G5CgkaBBBmtCS2SaLcqqk7i36QUcSpefQS3Whl8vbxufX2xJwZz4lPNaQ&X-Amz-Signature=8477706e0a25eb4cb33bf5e411971f1084d39f11c7d10494bedfcd64c7e0d48d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMAHKHSE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHdA0TFQVu2hTVh14JTIOdaKGGRraJq%2FEzDVaR%2F00WpAIhALpDZ3IWWQckEfeeOkvaFYRFEbFxuY%2BMs9WPzhOfRJFRKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySQTdkLREAvMWLeGcq3AOFLlYNM2wlDm0qZ1UkbojMgOqQwdFbcMDC1LEeIhgYxn7ZNwPxRHFubAe4DMy0oeMKSdvu92KyTkKTirKfZOUjpKrDabo%2BhxRF1Lm92QUiPcHgF1XIcAdBMDQX1BMnv3Pl8aw0FBARiQnL1ZKkalTzieLtDGvheqfKgL25kAcBvLL0hjPKP7P5aNtFbbuCN2RQTAh9%2BtpbLXtHYOxgupFT0UflrSjxL59fSi%2F%2BDIgmL%2Fo3ohh8pMhMjzJ%2BCEVFMEXjxy0UFdQyNa0PW7iO%2B8sVQL1v6OAmW%2Fh5ba%2BoDPgJ03OZPexIu%2FojKbr2QvLVq6BkCABLdHdRwgCL0gejDD0IeeTRbZI4z8H%2B7Jlt7ZqTsKkVsk4E7iOoaUULcDSM1azjnpp29%2FFBiGD43sgHmWnyb3zMfW2onVza%2BTOlwbQu4sp0KC0smUlGqsQ0EM7EO3dbbMrZvgIHhg2r7xX5uk0ePx00q9E%2FSiGsuXUIvTBvKr8G44mXTJHQKvdQs34ThRPAoueLgwsIyyvELo0ojhSf78u6BJhYvheTT4tgYAXL8yyRVM8xIsWTh7Re1l0PyKljru8xPwkCRvSnaNsQdcgfNIAQBaEbIe9Qn8MkG7XI6oltUpIa7fpu32RH3zCjwv28BjqkAYIXMkEWgAHTdmMVzZAw7Ls0gINcYPSNUBEqsDj9gCYI6XcnHI4RjQd6KiPU2L5U8AK9kuq26sStK8wVBDi01pCnWuxtcgqOoxu2f4rCc%2FBe6ozmIUwOMnDa%2BxX0lTBawsZ5FNIEUfhJekjZSiU7hmSDQBxL7O0e%2FZ0G5CgkaBBBmtCS2SaLcqqk7i36QUcSpefQS3Whl8vbxufX2xJwZz4lPNaQ&X-Amz-Signature=69ae2ff54311fadb24e87b9ea5536c43c9615bd45950b77b37c6f8e2b761a69d&X-Amz-SignedHeaders=host&x-id=GetObject)
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