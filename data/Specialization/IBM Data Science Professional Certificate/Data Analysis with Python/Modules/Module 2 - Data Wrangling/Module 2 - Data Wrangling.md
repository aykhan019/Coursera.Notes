

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKWVOB4M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCby7PTkbEDo4DH52eWNfHOfyas4mS65g4CJH03fJHzmwIgdHrw3m6QMVUucrFosq%2B8px1OuiOCtZpg7ieTKFCEusoqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKdvE5O9JIEVR9diESrcA6adx3jPzZ6r2jEpwNSclh66rAisr224ErlhuU%2B8AdB1%2FToreflg9if%2Bii0yzPRoW8XSDhUuvojbE%2BeqIsCb7bYgEpxTObWCn8Nu%2FCOMtBVLBuJlWS7z6TFvYjD7Kd%2BKg305iIf7laVZbUuSBT%2BlIBrRhw5cBZi5F6lNwWWqUQNs9jC6atl782p%2FP8ya6LlT99Hv3URVBoS4rOIvzPoyQhfscO8SVe34YNnQJ77k3kUE9v1cJb2sXkn0MqmlufOzqvkaJvjhcqUikMoCqngrco3czP8VkKCAS2byCqegyef3XA%2BJSvqM50j%2BTmaECWh8qu0mj%2BpPCSeGnYaPSMbEpfscRCS8Zd6%2B4h9VMelPjO33i4EhwtIqfX8aIX4dur02Sw3tcVdcEDh40FjxC9IyEOmdkvBUpoqfysYTjD72VcexEonHVMCaYyQqF0e2dcFn54%2By2u7DiB8Ejp%2F8i6zJqfTMQHK6dHcD5nkSwjE1gbZQQNcDBJq4%2B%2FgGtCeagV%2B2KKpqfL4Nj4eLWCSO4eVtCmDynNwvT8eiKOx8q2HL0T8%2B5FzdnsIOsGPNaMGlmMKG%2BPGOnmMODW1IGCtA%2FuybWXynDKCm%2FCmSUf2derT2Esfztmo9VIGju8tkOdQOMLWQ57wGOqUBhzzcedlhFOBb5sHGyjjN8JiX676GFFT4W9dm05Rkz0B765lh1GAOXSdEbJooIwNwflmQL43UUOsga%2BXj2dLL421rchoFxKEnL8jgy2FhWDLa53UZdoB0swbZ%2FXh4i2mMbpZnTah6va1ZBu59jEdw77EH6RHFT%2B6k%2FnqIs%2FCTRZj8Os7meNrjTzBcQp%2Fm7JdnPt8NbDC7PtWTe1d55bFfHlihF%2B%2Be&X-Amz-Signature=c3b7d543faad07951efda9b6076aa648407bcdd7775d28cc58cf09abfe776202&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLLEZNCB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQC2%2Fre8LzKxUKJkWa8xYJuGwmuKuVF34O1wK%2F3EmIZG6wIhANK2j%2FHqMbn6yKtoeEL5%2FJDuKJx%2BL5B3c%2B2at%2FAK3789KogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxe6duXs%2F%2BX1aZjGyIq3AOgR3qqFCjMqlJoigak2BO6OcI1M4s9%2BriJf0Y49Qv%2BAo2DGzb8yN1f%2FxtUZrfZjQzFN9JjZyU19ez5Owj2RYDqZw30D2zpJvUVgu6u5OruGSLQeJW%2Bz91C5i8ErFTpFjmVn3c9j6NoRsrWN1tezF75N0%2BMvQfhW4ekD2X%2FcJE4BkWpNfv2LWuabKIYKsEkLyzZIKKUQLgDTt44pVwROS7QLSi7etZpoHGH456n%2BqOKtGKl0pD7WhodCzAIiGfT%2FQU0QX80nGwBJ%2BSf01NRMPwFJpynnw3IEVZotYOG2q7fsNQVzVbrZCV2b1JBtqs9d0cc4u8ah%2Bz0MT%2Bj311YWn4ScK4cuJTRfRs8Uus8Q4sT1rMKtf8ZhadB7SI1l2la4oByDEySMaLaqDRfdNJ2oRPoCRmQWywUDuPcmKFC0FI54EMshtqudbopPSBAcH%2FTI8Z8F4eTIs33ng5tY4MsYPZH6Qrhw5ky39kNqZfGtovUZ7VPhn1JEyeobP2%2Fsjyb68DWjWim5xvleXojDrbvWIL5j3ZEKxr1uEDMrsMu%2BjK1bqivirBNrKhqShgIKN1lVrx4iJBxdb8rqvCAhx5VeiIb7zR4zZpenBkNEJf6DFi%2BXMPPNxLwvXZBflMJUjCvkOe8BjqkAZ7CuzxGo7rBxWsUzJ1xSSPcSzQj99JGsRHZ5fg%2BSKqf1TMzEjGCmi5AuYF7rDLpkh09EI%2FYN3krdPgm1cBFcCKKshrD49HU5ygr6Hs5sokJ3kgTnD3HJSRqimS%2BrNlhr09JvRE0eQKtHUn2pedFG6zNNQC9CP9LWciSEGYIeVDjSIs5D%2Bevxg2VB9lV546JXMYq7k1BTsK7qewF0an2OhYQ3GrG&X-Amz-Signature=e952e179cf8df3565e413a2021f23906c32be45e519291f8f7f4b508eb6f4f24&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657VUHZ4O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIHtwHSLcJ08SPHROQsc%2Fz28L8YsFeHMWzsV%2BRNAsBwfVAiA5q7mfXmcRQLUqOf6T08SSYYP%2BO%2FrOBlzaf7hy78Z31SqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3wOEP8ZPtW7x7QCDKtwDGNlI3pVn6%2BbPJRWk5JxDzvLopXcGBlB6gdvJmR5gGognpN38C7N6B3joUchkIIZs0qY4pLcyhGHSptIp2BDSkFtBoRcRGkMbGuoXmyHEKCRMz9IrioOrAYi06t6tLN4l3DQ%2BKGOpq7bbOWFG7R7FJC0MOOA8QQlHydcBkOth67BAvKQ%2BbokelYwRW7CrOhP79x%2Fu0JnOSVVth0hN%2FbDact8R%2FiCTFV%2BnicsQlszkzrRMw%2F1v1rupF%2Fd4VoIAw3EmWxx2JcNNxjWzER8kUf2oWjvZJdGdKxpWB5vcMiTLWBq7%2FyD7NO%2BGOC3jLn5zmh9U2UqvHZ%2BvBiaNU4sdkkxEEkyUkLsqeNh1KfqO%2FO2BFAALoyCeOxI3Eij2LZi%2B7I1zYjDZul4deU5oQDuU%2FscbvYVvygAA6Z5HI8RMCK8yWJEZKCnOL5FwDtw3WN7uwRbeut6fG2hcSRp9vQDknDoJ7nBiUbFnObls4GuE65qHVQCv99suwiHBXsrx0bXqBdb518NGIzb13dG%2FyTDUhrkOepov8RqXKKnM8UdajxJGGjbIHakcAoO%2FHJAcoTeQS0iXzhbj4IP6DRlWR5ESh1O6AT052uBGmsGm%2FZFsOS93JkhSh2AmplyBMjPPBlcw1JDnvAY6pgEQ21zb138epK82R1scrFip8ypV%2BVZwBcMviXM9eyvmeC2XlPtoLAzvNENd13jomzdQTq2vAzVeLbhDF5uDd1LAlMXEC2mNLbOMrQtI4dz7ZOPHzCEap6jfnK6J3tIOGDPjqXCKh%2FAGmdleA630HapSzItb0u0gPlEuQN1T1nLVdpXIEiYQb2vGwPuoJl124ILXbeh%2Bl5MiRvF6i9dmsT2TIvF8mw59&X-Amz-Signature=fe591b76ea967dc2f5218e5098420e0f4d978120fcb1ebc53a45accc5fd3fd82&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AWY7MZT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQD%2FGoV91zNbj3XYMt2gdFDRkDeZc1csQ30YI7cHCxPI%2FAIhALaWSPl%2FUvUVTgmLn4vOAyFNhaLYU7gIxNycEHSozPvOKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhfhFmwtykQBC0Pj4q3AN9pHnP55IEIvOQqiBCwty1YUC9iZm4Rq9o6FdMpsdDa9nVl5EkODLSKTdIaBNGf2ivlq1vbDIFw8ZdsYfYbrFQaWNF2y4uAnlZv%2FK3kKBmQwjqnh%2F%2BDdKwU4HjyX%2BIEd%2FZSQ%2B8kA0JAhvOx7nauH1yuMFQtTa5ra8gzb7OpOBIeO%2F%2B5xzDhklQLUrTc0aDg9t48pLgJnOeHAI%2BjmWDKVZZl55XjVBzMVK6hFTKXjDei265QyzekFaGUN3GWdrkwOHrRivW%2FBNtRKGNtegKXyVDhbKxaRpPp41RZZ9AwdZXjzYbs1FVD84X8Y4f5cwSpYLBsuo5aLjdjlxLIGEWsMarDM%2F%2Fm2YD5TnMgtyWffdf5SUybuZFBPrtwmOvcjmoDMgg96utZpCDhTFH4NxONUMu7ozeQ4rgTblY3JWSaeHNzgp1wjj53QyP1AtJO4LRQ131UY%2FaFo3nnEHNMvqUYnRbom6vcoT7w8Vo%2Fb8%2BS1ES28NXEIR0xWn7hZUTzxZ7UEiMTojumCTpuv%2Fp7hGYJXJdym8%2Ft0ZmmgMwdwloGQCXXuBWAEF0hbNfqwNPs3E8gLXS3Byzg2cHa44%2Bb9t5Eg%2FCxbeJG3Uvq6u%2BMssmO4TpN58Ea8ONj%2Bi0amD%2B9jDXkOe8BjqkAZ3BiPJ2OCib1IGOih0gLsYGgF%2BMDXtobqC8OpEpChqU6CKPjSOIzPV9ERS79GuQlsJsLUGT4M%2FCuMuIT7El%2B0u4cctHsYLl7yNTi%2FmJN5IPYhPngUMGLJWzpzLm6adNP0DG%2Bem3AP1Suti%2Bb6sV9bkYEpAkcW2JizdAMTIMOzKA1zod6OMY3JdC1NHnlLkiXpZEs1ZNGEKRMasAf4tZM7UJEZ6J&X-Amz-Signature=b6a7bc216c6e12e2e956ecaee1761866c96dd7586f12d60afb660e88829829bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TK2ATHRA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQCZcyBY4lctUoSKITtqBmvVtBca0v8s5jGHv5H1%2B2oaeQIhAO9Uxr5t7Oc4jNM8REyzWunUOT%2Fpu212hHr0%2BDVbA%2FrxKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJgpcKvxzVAoR4Wssq3ANci28tjYl4bZeOpXq%2B7LWoIoGZoTxrZVBrOCylawBfiMmGgrsnPoD%2Bmk0lK8M0aAv3t1%2BU2OWSaZO7CRmCzYvWeVnXwBr9h9ftgqbJ6nscCaFpNs8bBIrqNWXdxlBq820hYxUA6fM8KiZE%2BfsdRM8gcMk1Wwz2ov6the%2FMtKOeaUcZx%2Fu1r6%2BdaauCUdmpUev3Fj6RpNclELr%2BWvm09chJiD2nO7LNdX%2BDtmvBan5H2lmBNzGUXPSBA48vamDCfmXeIRehL3ED7lmLp6v8WA4tm6nU2fNSKzAf1du3%2FUSQsoFyiuEa9%2F6vGLZz5lxks%2F2XWFLd2gsXHYNUwkJT3xz1lc6F3hvzO3y8hociz9r9IfvIuSK2A23Bu1CyS7OSR8buIsQ6CcJ4o1aB7htoN1dDn%2Buvh5I%2Fx%2BUDXbUrOmtNvfQ%2B5TxR9Zx3SSGpcBTLLaIhP6QLo3obo5uzVVLlxOLTdgoFwK5cQ5M%2Fofrqrg7JVglcbPNin%2BuVFtMOEx%2BLVWPqCNnjWI3p%2BR0YUR3BGyg2OX43uSxfaO3F5nkbB5ZIIsBZH0y0oKIXX%2FCh7mcbWeddjWoBngHl6TV0XN9Sf%2BKymmnTRu%2BzMLRnnBNhYY3tGQo4L%2BffAS7FXlw4azD7kOe8BjqkARZqbWRO2LitYfbI0wTF4YRHLR4oFDNt1xxz7iw29p0lD%2FcXg53Yqp0IBUf3%2BNnfivGD1%2FHW8cHIqN7VuHe%2BH5uMkz1HDTTsHS3uweVuJiRCyfjnZguGQQ4eLUB6lP3hXVf8OworX1nsXrZEHCROecXPnW1Q7eboNjOCctCU0u9%2BL8fQl5aFsJdqAIhDsbGfpYSidXcW0lfcNguiQq4y8BRVebqb&X-Amz-Signature=d322b41856ed824ab75109f4a7a283439cc735a862ac4fce54130134b264b23c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UCNR5XH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQDd8ILKwXGgW0qBK6fV5Z67SMVzi3y%2FkzaBgFdjFHkITwIgWaZqRR%2BkzRHfQzkuEm5fqEJ5IaUguwMldcuos4ESkYYqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM3a1euijcdKttX4NSrcA%2Fa%2B0nUoLFAuH6K%2FkIUC%2BvLwd%2FNVUW0fuTwnVyqvYLxxsVLCfgaCFf%2BeVc7QN5Vsz%2FZ%2B37mI78ocMMkkDo3mW2mmN3OyLqbnTq8zF%2FPB%2FpNkHWEQONfbTURva4NcVku1Q84DgpTPlqHMVmiFS7nbm1EU87xhnYFB%2B%2FSOLCuE0dWHalcZxMN%2FCVCJhWYLsouZBmGBu2Y0n9eE6cSMVI63wk%2FdjleL%2FnP11yXp2rWSIhIQCdM8Ad24jruiokY9KFgr%2FQmtWpwxeR4%2BiXRK9xRiHxkEi42BeYdeJIHkM%2BqieWbH78aJFouSaXIQ%2Bk9shxm5hPt5HjHftaH1g7L0wruAL1oWKVhrF7M5fOwL7Y7ZgY3IbUkacCuSKG1jMiPyYVX5Ad5dv9o%2FAUQEQ0cpQ%2BXXoOJuQ2pXZbLQA17uCJmqkuHTYMaE1fxwFKy1eVlmKj0x8qRM0hSK3P1pHldd0feJQBX5otBe0v5IQfwvsiuOgY1WzbmzN2f7hS87sMokXKQ7QOeCsDZCfvWKC7pqVu%2Bw3EcGB5Bi9f8iORz55vSllTksdUxXjJMRq%2BSrrpzd7lyOczbPrPbOJ7W4O%2FPqwNyCoLPHleXTEm3Djjm1JnDf%2BxdZWfQUpAfk9Tkz%2Bt0VMJCR57wGOqUBWVPU8WpIjgnkx3kAmG3lwcIuR1OJzKLvd4p510vD0ITl3%2F1LwOkRuG%2F%2BrmDv%2F7FzSKPpUsQ1Q1FwbBwx7nE405jIo%2Fh2sDFP3%2FqJltYDx%2F9L81gBExvyRNFB%2BFuxAaiQ97POiPi9TFBg25DubzY%2FRX%2FR75bNRgwBsEO%2BNyTed1zydJXdaqNOUgsliZuXhXa5EgKUXbVRVwdXFp00UjU2g6nFv40g&X-Amz-Signature=33bc03cd78015ade8c47e158d2b2be43b82a158517608b102d1975b71db56ec1&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEVM447I%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQD325bqePmPueSotEKMw5S6yPjOIpr8b9QjcdDXtB7DQwIgY7GALnRXLyHqAiPO8V7EYqSL6wXQ7boJoXG0gU67pf4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA3k2NbcC0DKX5j8ICrcA9BUaKAiEYNrvYyL1awpVT7kX%2BrovLzIR92CeLLoqVEsNfgIJ7n4BPQzSeD4TK%2FTWKtUZpJCb2yM1FkLux2B6YyqcRGqqxVkW6fec701Bz7OdTMePnZK7fA5cIi0hsJ2cR%2Fm6IG6HkqN%2FISViZQ81zCeOxHNOFj29VrB2Hp0YkinLdjttcEEzAm%2F4TwGcqaPpi2I6vwjO8Wvz6%2B6xtQ9r5HoLIx3wt1HJLHWih1Yt7K72QOyvG3UUcX53NL4EJpKqgK9yvhaPA1GxEvio6fbZv6cDfLhSDrL1nqUokAacEHjuHDAaUqINtA6Pkn459r8Ww%2F6pILpZk1ktOpBQzUK58Duxe1ZdoKI%2FL8%2FotKMRDEgBKDwT5efN1cJYFb0PqWY9TnBRsi3o3dSqMXrdQBWjh%2Blg%2BUbgtaqUHvhLQrECVqc8ZTs9fwiKdd1GfS8Z07KZVsh0qQecyROYH7tA1gd%2BHj48ZKB4PdmOdwbe4fhUoqjQ34npUMA004%2Brp4PTua%2FA6OUC6qfrufSb3zweE6WznF%2FRxJV8YxtSLdvgyidEihn16gUa0nRb%2BQ2lY9y1K4q1AOntaLLnndInid3Q2q%2Bm4Mbgu66IBOwuoszugp5u1DlX4Z851890AMa6EIaMNSQ57wGOqUBPAN6sXyAEV0rBM7Sa5vO4e%2BUOrdQOu9PdaYChrp9N2dwiJrYpoUEI0wFPBhvPNU2bhThxoc6G%2BBaQdCXeyrBTn%2F8BdDp%2FQcbR6n9t21p4zPrUY%2FzWwvaN59Wd7FeIJ2btIRneZhDPhssjH1icl9DKeTzIHchxhI0juE8I7uIqr1x6pY5tDONNhNGqMxE5fXrH95gnBcrGOlw%2B4%2B%2Bipvu%2FoodjYai&X-Amz-Signature=e04341a1557f7fa870075d1601ca34380fb8205168128b50a47339179e95f7d8&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEHTWWLF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQDBYVC39Thz%2F0N%2Bw9aIfLs93EcawaI76mH8W59yxla9qQIhAPBgZX7BvDKadGMKBM%2FKg%2FlGzmRK2gCFrZtsISZaT%2FB%2FKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwz70x7Q9XPP0ARJXsq3APZmEFxfYqhe2R2Q%2BTehTHLxmA5Qv0e1qA2VgEEpL%2FcKMsQjsbBFRs4FG7qoXrR8bNBECtmkQ5BEirOo6JZO8LUwOuglb6fVNlySIf1whWuXED6tQaRU%2FttCGMWzMENgt%2F%2FtA7jOXxAdVJRQ%2FKQmtMGYJyK2PDB%2FnWBTo6XZT4TrywdctQ%2F7JjCRjiZbICLx3%2BI4bn1O1WApxz9RH10oEUUvwOR8vobmpwS%2FmfAkZ4SQ36e6nqmG9TKlTFuCsczHgrmltDCXXZTQ6rvZJK%2FSz2MHPfZz4EbIWqEs9VL2yl0KhHgrMZXTLlbQlQRlzLodft6t4WwFDwj8y%2BEvJ%2B5dibpk3k8SUDMntFsruWay5YvAHXbjfUit0i%2F4cQXDpAfMdWaIc7ypippTIT6B5qqfXl6r%2BFKnfHm5iCygiY5QOFIlOf50wqdAHNzPcmIhTAgO5BP58C3ZPvGPbT9CAw0U8vdW8ZULqK2inwkZoCFXgMayArZ1OFN5ppmYmbaug9l%2B%2B3BNZ9ZZYyNxpPxxXIvMiRhjbNII%2BTrAK3ppA893Nv7WmBkUQOJL3aVGqsv%2FokBogOQ%2BccZe9mZRYMUXNx8Xl1xXU%2FgdeqESnRIG3ExtLe7v1FtjwgdWjTfAznv9DC5kOe8BjqkAUiCcAIk7LJFOXcdzNY7W%2BvZhaJndZ%2BvWvtTHPBxAVGBPd0u6L2yhpuR9NpFXl6SgY%2F6EwxqPwMYHC%2FGCQpfvvGmExiJOdi1OW9yoogA0cK9oBSZBJyuhAOIqVhiv74GbWgCCYhTzkbeW5xMsPi0oBnjKCD2E3pp6BBmyR9lFUb6WLGz71qb00%2BcLdE9wqG51TqqRkmGuvis0ckN63NqS%2Bsv7TjY&X-Amz-Signature=4cf3887b8e9deed970f035a8450d84ceedcd6f85ebdb5d513ead69873d5e7173&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TK2ATHRA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQCZcyBY4lctUoSKITtqBmvVtBca0v8s5jGHv5H1%2B2oaeQIhAO9Uxr5t7Oc4jNM8REyzWunUOT%2Fpu212hHr0%2BDVbA%2FrxKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJgpcKvxzVAoR4Wssq3ANci28tjYl4bZeOpXq%2B7LWoIoGZoTxrZVBrOCylawBfiMmGgrsnPoD%2Bmk0lK8M0aAv3t1%2BU2OWSaZO7CRmCzYvWeVnXwBr9h9ftgqbJ6nscCaFpNs8bBIrqNWXdxlBq820hYxUA6fM8KiZE%2BfsdRM8gcMk1Wwz2ov6the%2FMtKOeaUcZx%2Fu1r6%2BdaauCUdmpUev3Fj6RpNclELr%2BWvm09chJiD2nO7LNdX%2BDtmvBan5H2lmBNzGUXPSBA48vamDCfmXeIRehL3ED7lmLp6v8WA4tm6nU2fNSKzAf1du3%2FUSQsoFyiuEa9%2F6vGLZz5lxks%2F2XWFLd2gsXHYNUwkJT3xz1lc6F3hvzO3y8hociz9r9IfvIuSK2A23Bu1CyS7OSR8buIsQ6CcJ4o1aB7htoN1dDn%2Buvh5I%2Fx%2BUDXbUrOmtNvfQ%2B5TxR9Zx3SSGpcBTLLaIhP6QLo3obo5uzVVLlxOLTdgoFwK5cQ5M%2Fofrqrg7JVglcbPNin%2BuVFtMOEx%2BLVWPqCNnjWI3p%2BR0YUR3BGyg2OX43uSxfaO3F5nkbB5ZIIsBZH0y0oKIXX%2FCh7mcbWeddjWoBngHl6TV0XN9Sf%2BKymmnTRu%2BzMLRnnBNhYY3tGQo4L%2BffAS7FXlw4azD7kOe8BjqkARZqbWRO2LitYfbI0wTF4YRHLR4oFDNt1xxz7iw29p0lD%2FcXg53Yqp0IBUf3%2BNnfivGD1%2FHW8cHIqN7VuHe%2BH5uMkz1HDTTsHS3uweVuJiRCyfjnZguGQQ4eLUB6lP3hXVf8OworX1nsXrZEHCROecXPnW1Q7eboNjOCctCU0u9%2BL8fQl5aFsJdqAIhDsbGfpYSidXcW0lfcNguiQq4y8BRVebqb&X-Amz-Signature=7ad78cc617ddcd28f1c0c1765550c3d3cfc6e6163b5b0ac4149b7b3fac9324fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3YCJGAC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJGMEQCIB6bxs7zYw2WlcyUCtguR0SnbWJUOQEjiRufFPxjKEQQAiBPztk88n0yJy3BkmU6wmXSLfxY2di%2FI3%2FwFD4B5YTJnyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBm7Ljay462pvXnIXKtwDymGds5Lij8zu4S0X5qy1LPeeID5apgx5ePajSyKCiw%2BOcQalDmWRVqMaTNFc1jbyTPXWCaUOeu6i5tXO3vP9bn%2B8Y%2FE8Ysjcwad2uLWPgIGmL01EsZKXlHbUKZZy4xQySAb7hlvCBlPC3XKfVMD%2FCg5JCOWuXyqOPiBsbYt9MTUBHBhuP0PpVOcPVs1HVXpNSp%2FhlFq8Vlk1RNBfVyTp5BC%2FXA7w3BIVC8qgNhQH8vL0XZNUJYvV3CQefI2UwywhNNgH5f1W6Evs4HBnDG1p0aEUX6dBnLGFfxm65jJAQS3TNfikChYrBF4NpUQEch4THTkwq73OBV7em7%2B1flge9%2FfwVbsPLG7XQU%2BEy4TqDKVMVH%2BWXOUhx%2BOZf%2BZ%2BpKnRJANxn1a1BPqq6NdFgewYVckbPbdJWv9ZdP9h2WzS%2BoDy%2F49kNVdYbXZDm%2FSzYk7aPHL747ZFQhenn%2FSxpls7vkRrEwFKiaD%2BESDwC9RNLhpAkLkc1Qa05YTvd4RKjB4o0hDz2xZs2Ams0iaWU3zcv9nLkcLsPUQfFjw4GgIBt8KBCttNZiJYWiNlYKrGEvKJAjBBp%2B%2FI6YCAPTON9weRTms8oEDXVJA%2Fj822ouNmDKLPEc18sSNHvBFAtcgwhJDnvAY6pgGOc11QgHMfEwwSNXofo5hauKhBBu1gYG%2FdTgK6sux%2BapJApFG%2BBzcbopW1Y8YVr0Bj8zCakPlJs1px2DXrA9u4iwZkjMqwPjFuq03jfrzz0w4QQI7sGg4sYSzRTkEYLL2uleO%2Bk7KEq10lkG4VFumSJjxpVDOG%2BFsbWNiIkQ19iqtiZ6Yr56%2F1Sgeh8NDLX3A08ngZXW5QdP8U8rtBy%2BhrdKgTXOpc&X-Amz-Signature=bdadd98c3becee4e6273df1f89d8284fe60e7f773573eef82a1ba1dca102fb73&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3YCJGAC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJGMEQCIB6bxs7zYw2WlcyUCtguR0SnbWJUOQEjiRufFPxjKEQQAiBPztk88n0yJy3BkmU6wmXSLfxY2di%2FI3%2FwFD4B5YTJnyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBm7Ljay462pvXnIXKtwDymGds5Lij8zu4S0X5qy1LPeeID5apgx5ePajSyKCiw%2BOcQalDmWRVqMaTNFc1jbyTPXWCaUOeu6i5tXO3vP9bn%2B8Y%2FE8Ysjcwad2uLWPgIGmL01EsZKXlHbUKZZy4xQySAb7hlvCBlPC3XKfVMD%2FCg5JCOWuXyqOPiBsbYt9MTUBHBhuP0PpVOcPVs1HVXpNSp%2FhlFq8Vlk1RNBfVyTp5BC%2FXA7w3BIVC8qgNhQH8vL0XZNUJYvV3CQefI2UwywhNNgH5f1W6Evs4HBnDG1p0aEUX6dBnLGFfxm65jJAQS3TNfikChYrBF4NpUQEch4THTkwq73OBV7em7%2B1flge9%2FfwVbsPLG7XQU%2BEy4TqDKVMVH%2BWXOUhx%2BOZf%2BZ%2BpKnRJANxn1a1BPqq6NdFgewYVckbPbdJWv9ZdP9h2WzS%2BoDy%2F49kNVdYbXZDm%2FSzYk7aPHL747ZFQhenn%2FSxpls7vkRrEwFKiaD%2BESDwC9RNLhpAkLkc1Qa05YTvd4RKjB4o0hDz2xZs2Ams0iaWU3zcv9nLkcLsPUQfFjw4GgIBt8KBCttNZiJYWiNlYKrGEvKJAjBBp%2B%2FI6YCAPTON9weRTms8oEDXVJA%2Fj822ouNmDKLPEc18sSNHvBFAtcgwhJDnvAY6pgGOc11QgHMfEwwSNXofo5hauKhBBu1gYG%2FdTgK6sux%2BapJApFG%2BBzcbopW1Y8YVr0Bj8zCakPlJs1px2DXrA9u4iwZkjMqwPjFuq03jfrzz0w4QQI7sGg4sYSzRTkEYLL2uleO%2Bk7KEq10lkG4VFumSJjxpVDOG%2BFsbWNiIkQ19iqtiZ6Yr56%2F1Sgeh8NDLX3A08ngZXW5QdP8U8rtBy%2BhrdKgTXOpc&X-Amz-Signature=84ee29ee3105699f7efa1af4967398217a85a92af51ff8ed96bc2393832cd5ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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