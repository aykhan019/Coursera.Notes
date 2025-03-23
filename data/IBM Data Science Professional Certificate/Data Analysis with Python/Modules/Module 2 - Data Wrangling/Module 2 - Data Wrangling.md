

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DDCPNSI%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQC6Gt5FuOznux9Lr2bXnRNueSJ0BuKl8Oy87ilXS3Z08wIgfhEWPJbce0KdnUGU0pgOYErD%2B%2FhTM%2BUPnIjzM3n2%2Fp8qiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNKLyPktBnAe6UCzmircA1K%2FtAAy6bSB8ZQ5rloUxu18W4S2Utu1G8eA6fg5HruMtEo7Cw2Wd0Qlmycw7tZxasPYb%2Bok5xzVS8DBxtENfbtYdybqPpELaoyzOf%2FNk1Sn%2FBbb7YCXzktcso1y17oOBLbwz324ch5QYKA%2FSOtviO5oKidpX7FR2jIBTNVBsWFYRzzjp7EaakWDvZq3%2BhGhbjMG8Bvm31BU65gbOjv7%2FKlVMiFAWJPSSbv0uWxE3NvwwyioNdqr2RT73Cg2%2FFevGgJPI9yu%2FutP3OK8W7TpcJQnyhoPidR5XkK982G5tfziWgqLgZfRff7%2FZpB0rrUFtTIWl5gJsTuk%2BgWCjgK9MPmzC%2BkVP2d%2Bw5dO1VCulyI57pvlELeYVx5UbFw2AngvTnT1jePIZAVcqVVlPa%2BSqOb%2F3fYeGV3vQNn6DTnqHvx9cRvEIVoLzTWdX%2F%2BHYr9s7nRGNYTh%2FNiJ34Au6KT2HivuXSM6a5dXf7L0r52Is6YTY03G5mJVJHOga9ADrN%2BnpyrXE3LbpaRXtNri8biR7a%2FA7APEkt3Dhdh%2Bgn6AsKTyjB4NAWChMX9EkbOi4gFRSaCwyFqakEFq1J3dDUrjk75i0whBD8qrLNC8pJwr%2F5WJXVEAohg%2BqfWDagGoMKzo%2FL4GOqUBzAJ6AYwiQqItiN5yEYnvHnNJGTmso8SpzpeDaScqlzg3XHfwa7QNGC6pvZ1sQarSuDhngOLH97GyPB3ZvK4uHRXjT0c4HH0k0WzWnnDMuL2407%2Fkrud%2Fn7XJeIeMQ02RK8y0JJ6tVVtRV3kIcki1O%2Fs%2Fg5EKGo3F1iw7rgLDGffa1Y6Or37xuBhjAAjoqMxC0dIYJkQVyMojp0fBEhDwSvgW8pst&X-Amz-Signature=89080dbc084741fde1f0c05c3d8f44026bddc75ae474c757b202554864713ed7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SV4L64AP%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIG6zLfsc%2BqNXDyzcZWDV9gJAZT1kCoH02nOmHZzjJ5I7AiA7vQWE6y9Efhuk6KDCTYaHewveZSgFindXTwucU2NfJyqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM347%2BFWTUUA1G2DlVKtwDtHd9Gz79GsmgPRIrbZo124duJSei5%2FQEvwkiysctyPa5d5OAvC%2FYWy80%2F6hYbs4Izw%2F7ilSwUdB9sO3YvKnf8SpYPXRt0%2BXJ29r9dpi8vZqo8mlWWd76WrM44es6Dv3H0yCouwtudmdb7WvyZPdomOol7zev6fdBfCphGZcvUe9ZLXqA4w9UH0k1Zh9jbxlSqh835B%2B4rMgeRCt1XC18fAyNBYqlGbDOTOmPxfEwvyTWlkQc1YpPMxGzi7oBHkswyu8bzC6ZYIr8pOAk%2Bl%2BB44MXImLxSFiqafgrpt0GFxI64edO%2Bs4%2F4BS6KCzdHDQ0%2BQnyR6ohCMpvcKxx0dnT%2BHxHG3ZeaCz%2BkfyOzRPRtAMcjPFWaeWItiOnc5l1o93pEtltFyHJ%2F8j2t9arVzVwPFMHzlrKTod2Mw9BGgeclTf%2FXM87scN%2B15GsxSLUfzjKhpCi97MuKW%2BP7A9B4vSARocVj8ZxeNCdL379VS2AEbWNHCylF9hpsVgDMLf7zaJjp%2BgAIVlXhxexy0pgnnvk%2Bhdl23FnvpNaCwhcZVv9Zy4s7XJOaMoPw1beTH5lwNendnw0vSKeN6PlxSOoX4BYyZumc1ANglIg%2F7XwSGAcPYMYyQyqgU9sjCKypUow4rT8vgY6pgFsqHFiv6il%2Fy9svqRE0T2gbaG0QOUCUhMM1Nt%2FPjt8eC58%2FIBIbDBp9VmmWpIYljljw6pwbCzTWH9lQB%2F%2FydwvvaegZVX8fkjHOjL1jNnVs7RtVlZJDgyy90OGYCwb1j3LOfzLjRRHoi7CWEmOl2MngVGkaQADTZEZATCpJ3a758LCCzf7I1XBr0UbMPnwc5rKjlbHiKj0NdeXssoeRrjwfREAYF1M&X-Amz-Signature=2fd742bfbb927c23ac85e3d4ad59ad4b1eb86a28f8866f1357dcc8d61c19f931&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNHS4ORH%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIAwwqetaWvGF3YALWM2bBDNdtLhogswtcNalD%2Fb2p2RAAiEA1td0ZdNmy4sCB7i5JlOKdKIuyRngQU4LasOG8Jk%2Fu3wqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGR5FSyN1a%2F0VzodBCrcA9YWSkU%2FJe3MthHQaZyiHNz393HUmWPE%2FAiFInXO891pdtvqUu1Ca6Kc8mkZ5MF7pPnSd0xzFHPvLgTwUJ5ymk8e8YGm7ImqUK9cnPnCOeWARDy8WTgo3v6%2FyfvGH7Stgu51%2FodGpTaMtt7Tkt75E7Xw2Gs46jAMPHOderbJvP8ZJKXq7zBMgNwhRVXa%2BhQy2YyO8Xynh%2FohlnIG8NJhJfbKkIeIk9MOukZ7QwVy3w1wyqiPEJ0ZCzFSVebb1g9lgY0E5sVDIR74oWzxveGUrDnGOvizJ1gEw3wOOe7TMZfG6dJE3UklV4xzOSRhVabzfWujrUWiLVTaeCZ0z6I%2FO%2BZli9dCRC77XRVmFd9oQnRcq6ehZgkY1t6pk8MJ1vrQ4h8DgNU54msKGGsRrlhEfMBcX9EzHAVMG2XZc%2B5kYwFRuw%2FeR7M%2FBpXnv0pjbrCt8QchU0h8X8SMpnKBKDhiFYzwf%2FNdRuViVzbFo%2FfDnIqQEna2CQ%2B9kodKpjpez3qcz7WPPjl2wNZtDPjomYB9uyAGs6qeHOKzyK%2F0h3XEVVgIIpyVzKTJqgSY3aCiGPvNoqpIYkgpZbJBuei%2BMSKwQ23U%2FFJSWLBjx47zkjNy1lrnOT8RBlaYvHtC%2BzuJMOW1%2FL4GOqUB3jrz9pEjnigWZpuhz0uqxs58oSVH2hIdTBJvCxBGCSLZ2iIExSkgJoE5NSR56Hj0jrlqqDI6BNa%2FVJ8tSh505e4O6gOVJrlm0U3SFLF6odK5Kpzgh04elYWHJwYBfKq8gYlLNXiopv5pgLCqWgvYOWO5DuHHwMIYmd2eqk%2BI%2F%2F3naqL07RER%2BnkqSM7WJ6JzmV0cGSbhKChrhRVGbYsWe8Cjxjcg&X-Amz-Signature=8036a62fecfff64ccefed56b8e9b98c9b926091cb6658c5cdfd39ba21eaf162c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PDAXCYG%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDp4tFgBD%2BESY6D2VgVrXd8ewKh7VaM5sIpcCj3D7AzyQIgLmrBg8i24zGna%2BIErBqwAEhphCIKQ%2FG7FIfid66JIjEqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH4YYL%2FbEiBlIF0M0yrcA4s58jxa1rSfOdjHFpuBMEwg9oQ7VOlrJgSGaHcCY9Ybyb22T%2Fieueih%2Bx%2FmFA%2FsuMjCJ7FklorVOmetfx5%2F8X36PK3pDlC8M6bLWIsCdqaB5AApQ7vS0%2BwN06j7mo0H49tE1bWVzKLO3%2BB5UziCWzwpFj7xxN1v7vK1KI%2F%2FwUNg8yOak96kH8s02UW4XlLJtdPgowIIkdqvFWvVUc3Q7Uwr%2BhY295Zrl6VpMl1czJoyRdu14ygqTw5vt5yhy%2Bg5ZD3zjV5xSPttrdRfkcDMHPBbOlO9yhkuSACFsQcJ1Kp0110Z%2BlPYBECY6KQYfSR00fkgQYbQ3jFP6tSPq9R32fb5WF1%2B2JxqLuTYGkZVmKTD8Okb%2FjgkM%2FRo86I7FRglI9KHG10K1I0ixQFcIZQ%2F1OkJMZUNCWsoqSPaGb%2BObxoWXLJObP3eRbZuU7PmMYGZwqnWGpD7%2BqPLnKXJJn7bs%2Fj2QbNr6ig3radPAS2xq%2FleHkxn1k8ot7DiS%2FgN7MsyfavVo0TZXnoy3A1jfoyinkR4pq2G%2B7GI0rchkkoyiPLI7szi%2F5eWgzoAxoTZwjddGO2L36RVUAe2dX3Pld47Buo359pK4OQ%2FfOq8BLFfYz45S1gASwQlxctMp6SsMI61%2FL4GOqUBqtJk2KL%2FehA5O5OXB9nKHd16Cb0s9jC3eGlWRL3uribW3HqaNsmzV4BSTr3CAnjE%2BPH1ppzLoW1d2k3nXR09l4qTMM7TF52zPO7Sm7iX98nNgHepv0nYL4mCP6yn%2BhaUvioc3eJ4cRLWlZ61L80nxHT1iBfBKVNlbhcCTBapuv8Bs%2Blh1QWZZQUnFq9ewlocV7BUetWQrCNb6TDeL97vyyxFz2n5&X-Amz-Signature=87ad9bc13eeff4c92be81712c40f40fe1bcb978e04381d3bebeabd13f38e51ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAOLOJIF%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJIMEYCIQDW9RGYfJh1JXg0Mtnc88BWYwsaZr41Km2M2%2F7rJhx2kwIhAIF%2BcdrHCbh0Hbw0H08%2F7fNcp47%2Bd1emHQXzg%2BE48OFkKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxydml5qR43zBHKgTMq3ANzDwpav8xekZi6h8IrySCFpw3oyv74hPzG%2Bdvy5K0qouedrdCbl4zkVPfqDipLMmzfu0oSG2O2GmjyP58BWWsgyVGI%2F%2B2VXN7wZ%2FW5abDJJINfSpXtscDIpq6YBWFBwgjbTQNUrcNzn2E2QkXsoa9DYwNcYpNsPRPlZQ9IzCm38z9IQFJplqfGKgu%2F53uP9eJxJF46Z2sIwbcP%2F8PMpvfXTLrTYOAfFx9xDizuXJmyx3aYzTW5VAlV6OgGGvpmXGWI2hwTooe4IoYWB4QDq0NUy5k7OJtjZnSIamRj%2BuvEaUMNPxAGFvtdafUEcxhgF81Ncl1%2FmXyrWmKHzk7CKJ7TKcZreddrVznKyDrIuuLWnCrciBYQwOG8C%2BtBNQZNgQlrmWEFvWvscRseoNqVrAiryFf9ptKH%2FOeW8co0aRBnEQ%2Fg3siWS%2BkdH1Kx%2BfExIGVi8GQ9zvUfMiVPrdeFgUKc0jbA3WoG4QIMs0vbkS79MZw7XPDmg0bLpjWdyNhpY2Mt3SQILJSshN14C8LzKHiERCsu3t87D0cxR2r2wNtMdivh2ZQXYiIppnIWRmQVcnA6aMC%2FE6JDGGjrzDqGlU0qdzbtKSINjWbk2cJRIq%2FVnqxX87nJW4sA42EsfjCbtvy%2BBjqkAVfQZxozz4QXLzrTiH1891pwMN5%2B1n0oAtzW6BdV9%2BUxSyoHAii8Ba%2FaAZfAyifJCJ4V805xw2RFpGXGVxX3NlE3h1LFckDqz0s0Im62J%2BnUzWbfu2tnpFXlcne2KQH0uz0ZHO4s2fGT3d4s8r5bUCvcAn1KlJOGl9rqM7CWYuGVuyLlM2TChTvIte8M3fXqhAOmeDu%2BRfZOF9dptUTOMltX1%2BxH&X-Amz-Signature=309ee4923f4791a2953bf8af3de7a743bb6b672178a9456350dab2046c891874&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRHFVUPW%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIDh9%2B%2Bng1gKmV%2BcRc4v%2FWBRcjCB8I0koldjTf4f%2FcFlmAiEA2ZY13saKWngWgfQmtG2l818gbqYRCtmbHheonR8UtTEqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNLctcCMUXnSwlpWLyrcA8rYxk5Yu%2FLQZfoHck0W8Q7Um7dix8jEYRlPpvuIG2BS9WRntop%2BHiAQHZxJ8h2OJ5ikdQWOrWwPKFTue2dCKgHWtCb0XOdJwET%2FNqbD0Inxk9kqswZ9dLgW%2Bb%2FWm6dRZG8nuGmIuIO6tp%2F%2FFLSVIS2LflVaVtAbzVcKtT1DPRIGgdLnl1SgulYk7gF%2B9Pes34YrnmRX1ZxNgIvZm8PY%2FZnszLcseptJ%2FZQt8osJAnoSrx2nua9jRTX0u9jzoPgpm1Kmj3OPY4QSfkLGZdufc8Y07fU0kprE8Yrb8TfLEzBxJebtDTB01rNEhxDZih5qw5HZ2jHCC%2FoyWsUu8EhsIjGixMDKyfqeXXwTPJcYtJ9EKW2Y7APi3%2FhQJrKrxYKy21x7oTBKuveb31pmSnPHfnHL6dyIgGjj550IzM6i4%2FTKPcISIqNBStUj%2FNTdmM8YcjGaBaOfwlYYYbez%2F8tf4iEpruud%2B0gbEFWudjKkqGu%2FmtUQ03zbWZ9E9OHB11%2FXeUx2bBt6VxuqXhc8IyEyFytOAlNPjlNMkkXaoEhcfhoT8lqPCiVYQEm5iEbgRzQGGO5hwFcgktgPTEQjGQi%2FfzrkTyUeFRYFAnu9Fg5BqhofRw%2F0nzddd9U3K940MI61%2FL4GOqUBRQUpF%2BHQo8gZLnyAQo8ZdxFtU5RZBDVA8g2O0ECn1nCAE6HWUYpUKvkNrz6a8F3u7q9nv3EvK9%2BZcbHCHLR9SKzXJ28TENBUEAIpXQFqKayagS3kFH5DRZXDkWtyzaJmNeqj8MkUBy3fvhCDODCeAPZLGXhgIVL%2F3kZDmQu7dylJEp1q2LHs7JVx8N94EbnQV7HNPq6cy4fYi2%2FqU7VKgAE6k38%2F&X-Amz-Signature=d695ae7ada34294b70a89e669d21279057c47bfd0c7476eed7763d0717ce4de3&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKHR3P4Z%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCFG6ZEYQkJIev%2B6KqpRN2i%2FfDPpx6usTuBzcW6PJq6KQIgTXKkuoVJ4kTWLPxzYCuOkIhbOCavgiW4wxPCW2lG5v0qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCR5LJjOAI6yuqv3uCrcAy%2B30SFWQY2zzS5oH1yxuAEmQuv7XQfqy2xabznej2DGVNTEG86NXlceA3BNjJ07UO421sygKJLCL6J7LE3fLm9mERxVSskmg7J6ZlSrIzvNUTFY5lmOB0ZoBljV8IP55wGZZSTfO6LtMi%2FwJEu5cHEpL3HbbKD3qCq%2FlA0d88sG2q9ecO6sENFzQa9%2BXM%2B6IlBbzTr1cgtOBVd%2FCABjhsN7cMlEWLROEKMxoIbEwQzQFEpc8LTHv%2F251yyXmjm14xi8LLeidZstSqEvUJxi%2FfLBVe13LXk%2F87ww4Vmr%2F4tLsWUoUjw1jWeGnF7fcFU7aW4eK2l4qeZPo52akpFnfTKbyhjjLQl95Lx8oqN0P3buhlorsdA9XYN950xI0TkpCTqqiBncbOkwE7amAaHhShtcv2G9zIEnKYRWL4uiSw93uk%2B3enxl3DrI73o7p91qnvJxlGAoOAGRzgOzVXoZSIvl0XzXWC3EkY6t7xRaGfjRtb052zBwv3Qpn3B8rQhusnnmJDjbooPzfaMccEiS7hPDgiGBEpmrN5iDUyQwj4wXsbkYR3wRherMHdGVZc0HRNMg4DC5T0PNaO5DkHSUwbo7bwjtQ39L0TrdEoU4Wnk18HD3lxM3yP5F86rHMP20%2FL4GOqUBbTX3wjvlrlm332OkNSLKkiU%2FRAYQ%2By6RNhEIwzdnfchkKacuKxYxkMq%2BpDGMbA7cHUmRwdSWyWhpE97N1DVadcBYGzfRZ1VhGGiGH9G8dtHeNPM%2B8aVdpnLcYHuSD5UuK8XA6LrISNKIssNK0Y3q1Ds9Xoh3X3VyMoi1Q3PAGH2MhAMkR4%2Bt9v9cAeyRvL4b5zQHGdyR4%2B%2BLLhaGIYcFkA0yfByH&X-Amz-Signature=2d63ce13d6b883125400764207e2377ce9d92335ae6bd7f843638711a8289671&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y6OZWK4%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIQCIhCFkW1%2BUDXgOAto9XoTaj%2BULVDaJEc9ZeCEer3JbjwIgX8UQaMTAhBxYJiOx8%2Fs8lnJIg%2BEQ7FDTsAdFCpi6Ui4qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDAANKWglLOUEr5e9CrcA%2Fhm1xjH3TF1B4IH8BH%2BbAOjRJ2NuvoQxYzWtMt%2FvdVQxBKGOlB9LQQdqVo1KDSIUHVaxlzdiMWlPWGfL%2BAEn6WDAfvrCRYwkmouzfagMVn6CwfNTSdVKl%2B6ciEV9lyJUnIp%2B2jCYuhv7TF%2Fk76UF3%2Fucv6pVZI2LNaUO8nPOKPcvKSqL7qBkkQ%2F1HH8O80WCt9QcDPbPx4giY5QZo8vVA5aTHBG45CrUhAZjhMWiX6ZrxykQuieoTYItDtInYhwNq6fIluhGaBRFVGf4UC%2BDkohDaQUwseCfBxe3EmZAkT5KZN4xASqKZl7picpOJKCTxdS14IQCh1gC%2FYAIh%2BYVcpedzLw3fxUmFHnL6HPhhUcqrZ9ww5wDCPYF3bj%2FaLclPVVwN5IQN4OqVqwnOQykiOv%2FtZ9MTZKM1bQr%2BI3JunPrFNup%2FGAyBwZ%2BGc1RzBVh2vvsty4Bu0bREoQbDygUVbtaa7I5%2BeFJbg0v7mVCWocuHhFY0hDzesCCOilZFZvhk%2F2tQqQCBieaDGz6yuq0%2Fq8cU43n6USKaCkJK7eyvHNrpjnGsBEneT3A%2Bq0T2Ottaipd1fCrfk%2Fmg%2B9Pfh0z0WxtenjGoDuXfUgQBfO%2Fdl%2FVVtR7qiS8f%2BC9hPHMJu2%2FL4GOqUBtMY4pAc%2Byg8VAXZILmukZw8jAbiJhQgwi3BzvMSh0UCmYjw1dMdErv248ipsclQc8Vr5kj4Bhi2ebzQ0gwAnpeFdREHvf%2FBNlPk0Ob09W9CTFanVYRQmdmim9uQCGjRRjuzzrwo9%2BFb%2Bk9pbHDzun%2Bwgz1aq5UY5krSbRwcPlAKP2uvXrQhNPKH%2Fn9KuaYyxRwJ3LI0odaiqVG7L1M3LdB6kC64n&X-Amz-Signature=8e4c248221353d4ce1446ee2b6a792da79c9878ae7a6da30e5e7f4d057f86c38&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAOLOJIF%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJIMEYCIQDW9RGYfJh1JXg0Mtnc88BWYwsaZr41Km2M2%2F7rJhx2kwIhAIF%2BcdrHCbh0Hbw0H08%2F7fNcp47%2Bd1emHQXzg%2BE48OFkKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxydml5qR43zBHKgTMq3ANzDwpav8xekZi6h8IrySCFpw3oyv74hPzG%2Bdvy5K0qouedrdCbl4zkVPfqDipLMmzfu0oSG2O2GmjyP58BWWsgyVGI%2F%2B2VXN7wZ%2FW5abDJJINfSpXtscDIpq6YBWFBwgjbTQNUrcNzn2E2QkXsoa9DYwNcYpNsPRPlZQ9IzCm38z9IQFJplqfGKgu%2F53uP9eJxJF46Z2sIwbcP%2F8PMpvfXTLrTYOAfFx9xDizuXJmyx3aYzTW5VAlV6OgGGvpmXGWI2hwTooe4IoYWB4QDq0NUy5k7OJtjZnSIamRj%2BuvEaUMNPxAGFvtdafUEcxhgF81Ncl1%2FmXyrWmKHzk7CKJ7TKcZreddrVznKyDrIuuLWnCrciBYQwOG8C%2BtBNQZNgQlrmWEFvWvscRseoNqVrAiryFf9ptKH%2FOeW8co0aRBnEQ%2Fg3siWS%2BkdH1Kx%2BfExIGVi8GQ9zvUfMiVPrdeFgUKc0jbA3WoG4QIMs0vbkS79MZw7XPDmg0bLpjWdyNhpY2Mt3SQILJSshN14C8LzKHiERCsu3t87D0cxR2r2wNtMdivh2ZQXYiIppnIWRmQVcnA6aMC%2FE6JDGGjrzDqGlU0qdzbtKSINjWbk2cJRIq%2FVnqxX87nJW4sA42EsfjCbtvy%2BBjqkAVfQZxozz4QXLzrTiH1891pwMN5%2B1n0oAtzW6BdV9%2BUxSyoHAii8Ba%2FaAZfAyifJCJ4V805xw2RFpGXGVxX3NlE3h1LFckDqz0s0Im62J%2BnUzWbfu2tnpFXlcne2KQH0uz0ZHO4s2fGT3d4s8r5bUCvcAn1KlJOGl9rqM7CWYuGVuyLlM2TChTvIte8M3fXqhAOmeDu%2BRfZOF9dptUTOMltX1%2BxH&X-Amz-Signature=f50a5131514fa61e695c430249a8ac8c7fdff82cd4a0f6b6c92f022e4dc4ac3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJAXRFEJ%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDbyywcJFhIKApBDbB94L7QfN6l2E%2FNdQ1B54oY1ythnQIhALGhLeEAGfbEvzPs26OsLMDvetVDbv8G9tTobYCZUWhvKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpvGiw68O3rC%2Fqltoq3AMvBzdKri8Hxo2pvY2LC44Mib%2FLBJXQ38OHHBCAEDsntT6e88M1wBpx3tD5kANdU5AjsDRB2HBM26LPcvbIFH6yev4CgMB%2F0038%2F24AUwA%2BRWt7MS0cq%2B1QnuERufIYHsDmdvizmB3ekwVItQDv34%2BTv2E7XTPcffEGBJV%2BiFkja8t0%2BNenHCdgIMUYXuH94wigUOf37ykLu8864cvnxn5kNmm1INoRTTVt45uj9tYjC0HNByiaago5bbK22UA939xNM%2BjXrOhp%2F6jHFeAsLic67GvdZM7vsvhyHapzJqn8Y1e5Fr6ChFffadFqM0e3Kwtab1q4MdIRLv5Mw4%2Ftc0YTIe8etU8uWz25%2BdWsugHrDYJJwXDp4J4jJ3A7c2Pf%2Brz95i7OyMfNzDHOGE4CdhCp%2FMglvcy2u2wEypseP0wWj4b%2FijQi5lnDJthIHCa4bcRm1KcdcYgFf9wQ46BwyIxKpyefgWxK%2FntWzEUIhuNrz%2BwF18qmDX4Xo1qW%2FiBMT9GJeJlCBue07M5NT7Ik3yxqh3VrpkDpmJz9dEY%2B%2F%2FhBaC%2B2r881bBlrja2cyb%2Fd5gASg93eCaRiYIb%2FkUmypcYNM5%2BY6p4aUv%2FAJXh881otTtHY9Ddofugns7dN5jCbtfy%2BBjqkAQhEUBdlUfKJ4rhOP2UsNclivgNCzHXVzZ0BrxgH6o2UOGHVR0mHuxHwpfRpQWA8u1Uf3cwJvGLnD37idx9OhWs9idxvisj60H3fnXiNgNBtgi%2FK0Cq8raBKgkhgXaMDjXJbZkpohimhldERTDbdq6l61PKRoGaUopIqXpypkZNLoACNC%2F4aTr9O9t%2FBrtEQJK6QL4wq%2FP0s1qJFrlcmM%2BKhm4Zn&X-Amz-Signature=2b402653776d95b357f259dfef60c66589722984be879d017908442167e81343&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJAXRFEJ%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDbyywcJFhIKApBDbB94L7QfN6l2E%2FNdQ1B54oY1ythnQIhALGhLeEAGfbEvzPs26OsLMDvetVDbv8G9tTobYCZUWhvKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpvGiw68O3rC%2Fqltoq3AMvBzdKri8Hxo2pvY2LC44Mib%2FLBJXQ38OHHBCAEDsntT6e88M1wBpx3tD5kANdU5AjsDRB2HBM26LPcvbIFH6yev4CgMB%2F0038%2F24AUwA%2BRWt7MS0cq%2B1QnuERufIYHsDmdvizmB3ekwVItQDv34%2BTv2E7XTPcffEGBJV%2BiFkja8t0%2BNenHCdgIMUYXuH94wigUOf37ykLu8864cvnxn5kNmm1INoRTTVt45uj9tYjC0HNByiaago5bbK22UA939xNM%2BjXrOhp%2F6jHFeAsLic67GvdZM7vsvhyHapzJqn8Y1e5Fr6ChFffadFqM0e3Kwtab1q4MdIRLv5Mw4%2Ftc0YTIe8etU8uWz25%2BdWsugHrDYJJwXDp4J4jJ3A7c2Pf%2Brz95i7OyMfNzDHOGE4CdhCp%2FMglvcy2u2wEypseP0wWj4b%2FijQi5lnDJthIHCa4bcRm1KcdcYgFf9wQ46BwyIxKpyefgWxK%2FntWzEUIhuNrz%2BwF18qmDX4Xo1qW%2FiBMT9GJeJlCBue07M5NT7Ik3yxqh3VrpkDpmJz9dEY%2B%2F%2FhBaC%2B2r881bBlrja2cyb%2Fd5gASg93eCaRiYIb%2FkUmypcYNM5%2BY6p4aUv%2FAJXh881otTtHY9Ddofugns7dN5jCbtfy%2BBjqkAQhEUBdlUfKJ4rhOP2UsNclivgNCzHXVzZ0BrxgH6o2UOGHVR0mHuxHwpfRpQWA8u1Uf3cwJvGLnD37idx9OhWs9idxvisj60H3fnXiNgNBtgi%2FK0Cq8raBKgkhgXaMDjXJbZkpohimhldERTDbdq6l61PKRoGaUopIqXpypkZNLoACNC%2F4aTr9O9t%2FBrtEQJK6QL4wq%2FP0s1qJFrlcmM%2BKhm4Zn&X-Amz-Signature=e828bee004e648c209fba0f86ce8363fba4c6affded2490ec3ad522f15ac05e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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