

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H4NI35H%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFVjsaFtmKSvY8iRUx1y0OW0yPXQ%2FSu5GW7YSxSOy0YYAiAdrl%2FnltSkGEmxnm0el9tJKPdn4SYA7YZNwbjnQ4yvVCqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2V4fW11ZzHTQwOObKtwDBI3bF2bHDDlpKGoCQMWyVvB6jfnMHFiMwW58sSkkhtg8Dm8U85Vs3XWLX4KVEtln4%2BJGHlChaRTalTWY2OB8fNZPzap2Bgh71XVmWD%2FHzG9XVEgFML2SmUTUoQh4vZAbG6aDBsPIa6KalWlfKaSUF4KAZzJecKgstCL%2B0lq0rP0EJbY%2FQcGe30jVEgnKChHWELVgOy281RnmJxU9rCrBIh5WagbQ5%2Fwlh1HKLLGt%2Bk8HrnmZ%2F7Wv1KKjoptFskHMmZcoKQuvzj4w7CA9baqBqBq7qP8uVOkdnUmwp5MFEKLXGiqfwG2dvyNhnblbPHXeAEVMbWt9xemoMzO2%2FI44sY33Qu6cDulA00%2BJaX8DdCoOO3e4vwhWp2VCU6G%2F26ZPE%2Fq967Yy5kdev4kLVGkYyVm21N5b5V5sDiCdP2tcqCQBTVmrBFxqJ3cJ0PbG8CYnVMKJgCafISILGATeflekI7%2FJE17c76ML97PRQlAUrzNtI2TC1d392NKCsgQc75OFtfK3HlwEGTzs8MglNBYV47kB6pH2iAim%2FiRCYLXL1mFbPmA6LeEzzEo6rJmn2hgrYJzgVOmo%2BQu9geJPJMsdK9u3JrXOVwpV2Kvn4agWx3FHmu2IW8J%2F7QnGFykwh6rvvAY6pgGPke845DCTe8z7%2FXDa9atu7GLl%2BljQR60jfOnPKjoUxfuSzY0J45d0LJ2JelKC2ehq1GtBjJakjJ%2B5GEs2V63JTG0YcjJT5lOt%2BzdZ3FeaNFzwSUxexupiJdx9zRSMOCoYPVNluUrdnEuMLUa4ptvmdg3FwMzPHHBBd7eeCg15CBhW%2BeIGKltQh1oGP%2FNgs%2Fj4UflInLaQIYrIG4Ng6J4Vlsw2kQ35&X-Amz-Signature=f9269d6a8aa10bb2d1f5cbc954078967535fe158b5d9209edbc9ab442721c8f7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BMUHSKX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDC%2FCNiHrIJV%2FtEtlBzEMR%2FgtstJZSswJSqOntvGQN1awIhANk9abLKQk2NAj4zRdjEghP2wKVe8F1OzgC4qBdCo4g3KogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyytgIwLJrWcCioDLoq3AOkAIHVEIK4HMwWF3oLXY12UnbQPuVNKTVw99O1lGa%2FsXOhTyoKzOMmxPUgV1YEFR6lVeYyl7TvsE0csuw4WPVVamiC%2FNuXf%2F3CyYK%2FkkHp6lJOCujQIDEiihCr3cV0XeH5mBgwtOahyQJBK%2FFNDT8qCMTKGwqXdcJeR%2BoZiGs7HknQxYeTuzu%2ByxNcQtAzvskUNZx%2BobYahnn3%2FohLXAOlEK56rh0TLhNEw%2BnCGWc9wrv%2B0pAUeKuKB%2F2hAwwKGehGOe9C90FCfqRbN3SJQPK2wWZ0I54aQ9%2Bx1RMqrGrQboTz1H%2Bi6Oi%2BBMBX4cxyyPvWcf4%2BtIbDmJrL4p1NfZeeX%2F1KLhVgxO7E9HX3%2FX8s31E1N9mdEfFmzHaHHSHXUQAULyuKWYgTNjwHfnN7LmzSjW3Wa3oedhiSGPqJpU8pGPgCJpGkZsNMIJ9ROU%2B91%2BHcEQzdfK2orYm1hpOoN6UqOa9TJNw9AGduwzhwjgfK180MPYqgTDfL6ePoVOPRmBN1gILAQvPCowEe%2BMhNWQ64mnq1lVBFqx4i%2BMtBWsTiKc8HUlKbOGglTUjnzBDF5nt1zF5FUjTHPTwAXyNuHQYRu8rr79G0huSbaeTCcRnZASrVtAPmAuTOhqDedTDaqe%2B8BjqkAXyFlrALxyYCP9o1K1dD10ERcSndBxiDUXoEeL94XYwF7FQd2iEMkfdnoLIC3qYlTcqG03zwzfDp0%2Bu5YHLV2NtJOPWafMf0cMq1Wz%2BOJiGrE%2FhTtzlXaFq1D7pS3NshC62zy%2BATI%2FjWeafPcl0eb1%2FBlyEfVQ3ZKbZYVSTHY%2BVWUf2wgECcXiZngX7c%2FEyZvMavzH6RCsRx4Y11GANWC8UsPq7m&X-Amz-Signature=3f55a98af38038cb3f70e26d8420f97babc50d32a936d0f8ddfe1f10d5b717f1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMJRJP6W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGosQhJVF2q9AB9k8Jf26HXEBNdL6XLdDUrJwLaUq6qiAiBwLzW8F%2BPrZ13i4j1T7FbVs14Kt0Gj74Kd1a6RqqxHgyqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyaWp%2FJM8oxz1TlYUKtwD2mNS0fPAqZXnRjW%2FUGUOS1ojbmrXLviomrRM%2BXVNs%2F9xYI8AvzbZY3dOX0JVYpJWKXjZsG2c4wN8Cxa4%2FGYX3pi%2BeG%2BYgLljNaTMz3qJmGY7NhuOO1RvsM%2BOxFizhaflFYTQ8POkKRLbdiGO0VDq1Kkv5I6Kipl9qa%2BRtmsumz3bOoaXb6G4o%2FBBjgi%2B1sqg%2B5wnMqZTJQqZoC1zyBiciBD1QLs%2FQ6yDK50cq2NRzNK8w%2B2J3pK%2F2hSANfbD9Pi6vTZjReb3%2FuJuB%2FNyoEzQQX583nsBWMwgiw4HR7y0WnUxkvNBx8m9NmOuGh%2FiPodiyipyaSQL%2F5HXF9%2BkFdLKc79VStqpd7Bh1JZCNgLvChay67SR0vz5NSHjuFu9ZEWMqfzbQwj33Hv5j9Qfylm8nC5yRO9scDhJruq%2F%2BIFX%2F8QnoeRVT%2FxR4I5khZ3d6jKS%2F%2F%2F4MtiDSXp3279Xr2Pi%2F70TPHQnfVvk3%2F4Yf3I7jasJ6LPp8uUWIRg%2Fy0ge9s%2FvhjLadJekVkfB3Kx37EPb0XEmP6sGX9%2BA7cf%2B9ETuF4nSvFAkOI3CBrl2RWFszUwWWLhSyM%2FD2WsJ0QG%2FVH7tdlEn%2BEWvTZuF%2BkChNVX6NOldRZyH0TRTO204n%2FYw9anvvAY6pgEFmWWsiBRlYDqpavtld19cS7ElBVQSdWqSKVlzffR98mfxivHu0wjW4Yke5r2AwXD5vksNanTJRInpVZqTZ79PpMNm0%2FVtfyW0Fvn1hTSHsaBdoPI%2BBqpsaUuCFAONTBlVlheZiOaLrsb%2B2QPm6Eh4wqfOFiyRxzw0qKe7BuoYYp41igrwhSjWOOCD3JUVYWlV%2B%2FS3j9xV1I6QfzbK9WzUEfewOaTS&X-Amz-Signature=65ba033837ab93e4d001876e5767a02747d0254de4ded0f543bd6aba96a0ad27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CSQJT24%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDQz8ByjJZkWe9IwC8rCKKviBbFsos1RxT4L%2BzYAun0gIhAKaFgfJOcpo9QolDkIahl%2BDgqzfCYnyxqGHRjd6kCW5RKogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyX1OkhpncoceELj%2Fkq3AMgQoaTa4OqqJcZ6866g8vdWEWX8BGD9BDZLfhgYXtsCkm2%2BNRvKf8uqhQ48vB83Z%2F%2BfrfxLVM9JWKMf3ncWw6TsEewjyPFoHe1LLuZ4jymA5Vl43VxRNWthE8v5GqzCPxLeTD7H0A7Nz0%2BF%2F2ZWzlXcKY4H4PPTN3lcLFW89e0mjxogMVnL%2F4JtW2biO2UrkaOYyr4Se88EPvBUwykfF8XjZBd17mkrxfAvCYpwBZk2AUqxlMQuiKOffi0rNPsVHna4jOZvj%2FOcJzqSc4vO0oa%2BUmnNJptc7zB2hEAierGKvsZH5NVnf%2BgjJPSUGFjf03aMFatcC6XZ9UC9h%2BB9iYAF0gCvwmTG53ULx1NfvXSo%2B365yO2S%2BxGDlQ5hjRr4nsUuWEbFd5OJ7gMt2q%2F7G5jBloiURaJFIdREMdQ7KNL1%2B5vhnjSRq0VLC9%2BAE2aMsQjQayb7761sFPU2zVLTHC39R%2Bdv1xRl4JkkJNcW4TZer954PfdzkDsJ%2F1eoxiqoxY1ce1oRMl5StOEcGW88ueJzibTFnD%2F3px%2BP%2BqdYUcYrOjYGRRdKiqZRGQxuBaa1Ztkep9lHb4S2KUm4RYvtKie6Y80%2BW013%2F236w1H2sBXK320R5tyS2lO8pQ0rjDxqe%2B8BjqkAbl46%2F3P0qnJ1h6%2F9Hm%2FB3gRQeP6nLXLccuRyzUgyYM3scpMbOM9eZDWqD8yUf1jKCHaDWrMXRf0Lkp3HN1iE3Gt66vJ%2Bh0dZpRI0b9LC3cvdDiUxKQb9y0mw94og5r%2BinRjKv9rxqfw6NQKI6h3JFlYN%2BT8t%2FfvnTL0esfADv%2BQF%2FJKtkQ91LpJfRaaR8y07VVTv5kOkpdkVDagwZVDOOmNCUlS&X-Amz-Signature=b5ae00b5e0750a84bf96051d474eb01bdb7eea1dd9bcd5aa6973b7ab44150e03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665A6VAKS6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGhBwcHfaQHsxONsumvpdvDRu4tipQZRi8glC9QpoP0xAiBoYSkz3KHgqKmG1j3%2FEMeF1Zp7QH3%2BDJB64MSRsDF9WiqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeEgh4HNFLhp93YAuKtwDnJmr3bQQt0Ksu7LZF%2Bdfo%2BUmq8kqR3iKNrCIjsGma5OfcKGxaatuXHrOrrGtB3%2Fg1ZsE8iiu%2FtWu4SqyzuCR6SZZu%2BJZ8aaa7zcSIxiEMbVQ%2Fe%2FFTU%2F5AbFfnR%2FSTAr4W7RPqOITXXHbOzQoyWOpIp2UwmRf0qWbVYQXRhqds7o0%2FSsV1Uao6nYfO4le41zM5stUN34t65w0bffG4FnLzVtQbBwK%2FjBhzTVv7ldtSdWvxUwZH9WGuAPLsDIQQzXHvB1pKjzOA4EswKWWr1Z1YxKLqjqHBCKGgixwEQHfkqJ8EDPZq2L7iFR3c7kyNOmk64FClkvKC3H2QS6%2BRM6PAhQWvROxnHUZJVSbkaAB%2B%2FP%2BtTN9%2BW59M7N7qCpYvSFxVIHBTPkCuWV57Xk9%2B96YlWMGOifKgWhuHZKJhwxp6U8Mx9k3WDn7GFVPPaqofsyw4kcP0%2Flfh6cG2KP0kjdd9r7xguv58xWGdbhEN0lauybXEZtJQ28H1oKJQyddFB2qH3F4gLdfpKIqpFZnFyf%2FWiwO1E%2Fry7rqDxJOwEAWMPsz%2FenOOprdeTV5VSBx%2FmToziIAeaoB6E%2F4pCJgyZU7CNLhhomBtgUZljFKcPYZroeBUarNdG2skJJPFNEwnKrvvAY6pgHxw%2BnEv7PUIHLZ5UWdJlI2nTeXXeL3eY%2Fe7BBMHeXXsGpVmlUrSfzsHPtRZXUCL14bLVXKDz5BY4XdkJiERjEtVcku9%2BgxKaHWrVGqlG4DauhdOggSv6EXv9XF2U8OVtgIuSXwQ9NmgQyVBogwZCNfBkLUEXT9ZxJ8fP4jl845hMmYts3%2FxWrT%2FFRtrM7pSXfUezy4NbYaf3N%2BuYmkPhYoCbuV4jxT&X-Amz-Signature=01771eb1ad5217cfc0185e3633a39c6dc61972ed0711bda29be342f3ef342ef7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BKNVM6Q%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBs0fNKMgoNF5qD3CXmiXt7jvir6R9hw%2BvjszdiajOCnAiEA85WEVr3PKL1BEWmbXJdKQyGnJScHOLv1Za%2FWsUf23HIqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDCSADJV7XCH%2BFz2%2FSrcA%2FhgFP44qi7VUzCegB6nyiOE7WDthnzAmBeFzuYQ6n2ugHXSnOuJPnIX5cCldyvVr9Nb9S8Y6HiL38HuetyrWfooAe%2BaYX8NBwaWxcpuO8JE1WFc5TGRsXLMhUiZBLJQDgDaRzB0lozpQ7WzvDwkPvbDLOLplyyKVUGX9o1vRGFcmfmRAxZ%2FAe1RLK9krnPOQ6E91foY%2FKbFenIURI0UhQxdGhNr8nPGM7THdNrHCk6ClKTJSwZBAyMNiSalARvd%2Fo1zBJb30Q1SEnTpfoQ4dBjjlETkOftEyvxhONYMaEG8wqqCBuueGtsusgg6%2FrmFvUgZzY6c2TVrskECYh8lIWa9v1iDyjooZ%2FLEvLfibU700dnl1uVvQjyFJbQBbGLDjfuKZGpNl3W1hISk3yPnzhOMcOx1ZnjeCea3yPf9iJa%2FfN2TYYLl7U2aWJQE7fpZ3E1R7sTraeKIUN26WGnAOG2JcrsHvjZ%2BCZI4CsC0AqHxeECkht05DxmRdwB6DeLWL6TB8jL4W6DOTK6ltutYPBDNzCPM%2BpWnD%2F27Ut1yScaoEUZNdtC46ZmsWzQUzEOkjTHclzc%2B4P5V0n9HEJdkjeginqe2k85ScJ4GyCEVbppJprQW%2BFtf1%2FchRftlMJyq77wGOqUBhYVV9MNTlSPu8P75LQphs%2FayT0DMVnvfEDkrLDNxISKD1E7Lxzgn2V1GaS142b7C6%2FJO9uxV%2B%2FYRCRCsxJOou6xgfrg%2FiNjMPCHdbAAWvS6FriW9exNYTO4vBhYmrdAUxa2e%2BcthsacOD0ODBCW49kaNfmFghApVFeh%2FckcBKuph0NgVS9TDJkegUD1tbPHqP5onuo9ffLNhvQsVws3W%2FkI4VZN%2F&X-Amz-Signature=18986507773885d741b8e383c4053f37419e2bfd234d1fcf5a580e7963412bb9&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O7MTBYG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFxzeC%2Fn39lz9AS%2B%2F6tNu4YEsOlzA7%2FIOJQNhXrFE9jgIgf%2By3GLYQU40HdQW04ELhXYGGoX3jiG4L701QH%2BYaKb8qiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMoTjeI%2BcYbttBg9nSrcAxpTvNOj9Mc%2FNSHBoQG1tWp90Hn1XHZD5OoPPVW%2BU5lzEbkU2lmzgqVGhfliRzPLS1VHVJ03AOflFu43kRTRPCmAh%2F7z71FtpvZfUEUhtpf7ZOnPQyChQnzAqg1yTGeLMYik%2FHH%2F6hMc8P9jN9H%2B8x1oVE2Jr5pEyzgaVPdf2wAHj7Orl%2BOgXdKZEjALaDO48oLXepDpn63WU3Mr7nwB2pODWorzH9pxIPcss8Cfr9sZ8CswXWg5VTE1Xl7ICTmTijuqoG%2BzLsK%2BTREsf4%2FA3KRiXidZTFgBszdG%2BF0oq7K%2BRRXBF12PszyzxsQDcnkEimVipfc1YMLQxyNWJ2vlWPaSQPulhjZl9V8%2BogqhKBhtP5KFR9s0r2olYGEWC6Ekacpxe97rFAO4A6YWypIXluLOKcO4X9ySWNtH%2F50hruRF%2B2xUf%2B8YJcKMpe5OMYosxIonpxDKHLQtUz%2BphNMfpXB18UqNd3YVbbPYIg%2BgRbx5zN0x9R2G0omKTScjM2s9U2TXyt3eYq59Dl24y6KiaX1HtO1S%2BBlJDV0CUAlF1PdXIEkByPHZkOhvsx7pUUv9iGNYgIgyZgrBSnSmnUMNcPgjOFA2pzqzvgy8jm1%2B8%2FNpjAtVxjt3httc4HShMO2p77wGOqUB351fFm6zKKb%2BrEXBJ3%2BN3OtUflZxB6AIuOH0wMIJwxoSHMPHa2T5bVFVoDwij1qZFgfYSE%2BLunQhONxIXJf6lYoUj%2Fr6k7nfD7ErW1hp5k7b10Vuxk56Qmb5CkhnO7EA2E3YF79GWp2PCYgqQo11AS1qXg0uDilAqTAn5L9S3KrwPqW8IWorHM53OAIM3VabFdIWIwqsRJzhCLrTBH5vNt%2Ba%2B7NB&X-Amz-Signature=1d0b342b69b84ee90eff67449fe429f83bc53577f6349be29243b8bb034ba84e&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6F3LTNE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICOWumWm5%2BSor%2B%2Fpp6VXjaS2nQn3QFzcAek9vEnuRROtAiEAwUlRq8w9Ii3sOE%2B8n43OtZY3YbyzdGCZoFSktOQPOT4qiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXi6WnWXRLyMLNPQircAylFjwqVusvUUxzD908bcX84cxG0EwEPbwgsgyn1mwg%2BAlryfyC%2FW0zzryfFNPsxnXzuBjh0SNIGG%2BOCLNLmrGOFHDdLLd7jyaQSrUqRwLt6PsaCHwrL5oy0vb7aH4jSaYoMoZuvfsRxKrWst6FLMNu%2B5LftSd26rXcsb7eW%2BTmaBz%2FidFjIUXXFBuKXWYuKat9UbY1mFEzZEtNWfLzMXENeJ2LgHLEAJZsjKdOjmCyMyv%2Bz%2FUbJE1j4sCFEJxmpH4uEzwFsub7%2F2qW3RZNNOdbxgajFy6gvgMJjXS7pIFld2zv27k2CYjegIRb405XW1xsqzsiuLv%2B38YfJ7cWpG7D%2FvLQFBuOrs7KtD6Fkoi%2BNLPjEka%2BYOtRna4W6DqLwHCtVzi1JQDAPwllHfySXv7Dd1WFTwcU6KRSXuKQDMoHhdomen6drJwYUmk2d8cQKLdlhRYKmccUmZd48%2FXfiFCsukSZv9Jdc30PyFhW3ihBvZIdl1BbVUpzcaIqLv%2FvXtZEfzWuRFmf9sb%2BGyDuE20WtCI%2F5hAzg790cX7vaZ9huH0Q0iJ3ejPxuyQqALgyA%2FRINO8J1ciuBNc8CLJq4Ml3vOtZTycS6QZ24nrbnEIiXDl1FzFRnnRX%2FBc20MMWp77wGOqUBcpk095nh3HOIEtBcrROfOKT3N69N%2B9BdJI3VRwDcCABu7ZIV9I2MQZuOts1fBtTs864aGXPa1wGrN1xAvs%2BlDsM8ixLFUav3cmR3aWMsV2fu5Aj8rxs5q0bXsmwEYbRX4vbKjtPTNHrDIyA8buxOZFXfA1KraWevs0CXKHv7DSw3qJvvBaOYdRBs%2Fd0e958Xm89YgZ%2FDFb9Ks7%2Fv4Ft8nv7l83VC&X-Amz-Signature=429eb883fd3fa0eb6b2d51107e4b63126122ebc9e7012bbc35e590ca0ed3bec4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665A6VAKS6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGhBwcHfaQHsxONsumvpdvDRu4tipQZRi8glC9QpoP0xAiBoYSkz3KHgqKmG1j3%2FEMeF1Zp7QH3%2BDJB64MSRsDF9WiqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeEgh4HNFLhp93YAuKtwDnJmr3bQQt0Ksu7LZF%2Bdfo%2BUmq8kqR3iKNrCIjsGma5OfcKGxaatuXHrOrrGtB3%2Fg1ZsE8iiu%2FtWu4SqyzuCR6SZZu%2BJZ8aaa7zcSIxiEMbVQ%2Fe%2FFTU%2F5AbFfnR%2FSTAr4W7RPqOITXXHbOzQoyWOpIp2UwmRf0qWbVYQXRhqds7o0%2FSsV1Uao6nYfO4le41zM5stUN34t65w0bffG4FnLzVtQbBwK%2FjBhzTVv7ldtSdWvxUwZH9WGuAPLsDIQQzXHvB1pKjzOA4EswKWWr1Z1YxKLqjqHBCKGgixwEQHfkqJ8EDPZq2L7iFR3c7kyNOmk64FClkvKC3H2QS6%2BRM6PAhQWvROxnHUZJVSbkaAB%2B%2FP%2BtTN9%2BW59M7N7qCpYvSFxVIHBTPkCuWV57Xk9%2B96YlWMGOifKgWhuHZKJhwxp6U8Mx9k3WDn7GFVPPaqofsyw4kcP0%2Flfh6cG2KP0kjdd9r7xguv58xWGdbhEN0lauybXEZtJQ28H1oKJQyddFB2qH3F4gLdfpKIqpFZnFyf%2FWiwO1E%2Fry7rqDxJOwEAWMPsz%2FenOOprdeTV5VSBx%2FmToziIAeaoB6E%2F4pCJgyZU7CNLhhomBtgUZljFKcPYZroeBUarNdG2skJJPFNEwnKrvvAY6pgHxw%2BnEv7PUIHLZ5UWdJlI2nTeXXeL3eY%2Fe7BBMHeXXsGpVmlUrSfzsHPtRZXUCL14bLVXKDz5BY4XdkJiERjEtVcku9%2BgxKaHWrVGqlG4DauhdOggSv6EXv9XF2U8OVtgIuSXwQ9NmgQyVBogwZCNfBkLUEXT9ZxJ8fP4jl845hMmYts3%2FxWrT%2FFRtrM7pSXfUezy4NbYaf3N%2BuYmkPhYoCbuV4jxT&X-Amz-Signature=eadaabfa7c5829bb97f7bc7c9cddbcb70eb34d964fc22880af849791811ccf62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJVRUVOK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICZZshjx0uNO2qGQz24S8crR1JI4Jh4sbmjgCZvNEzQkAiEA%2FOHohNcr4AyEbm2RPV%2F3lUK%2BwqliW96z49rMlMJjbV4qiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBDIWRpIacmGXl2lCrcA3kbTF02KQbimoaPlpdXXYQIkkaXMipCyWWAw%2BULcEdU8Myg4X%2F6lr3QwrDF96%2BD0dCQq6wY5lCg8KD%2BgnvnjlZpbZUnPcRbelSz2txwngvA86sDY6%2BVaNTT8i12BbZpsefgdL6znBu%2F%2FQDZwIQz9rJoxH6e1BR2I7qcCzShMTV2y0gvVXBeqCJpEbFKSnNYqmXrVIRLtKgwC5T1X0jJ%2Fp5xY6SKmvb8ghcpIDWW8bg2Du9QqRJ3QxkeyIY3wXZKydChULTB%2BAM2uADmub6se%2FTqQgviPIU1CL%2Boab%2FRTuvw8yCko5HFW%2FJbK0nouGi244kIiddtXAC8yz%2BptmBkEEpA98L2AJ7%2BXyM3SrkcT%2FT1W6Z7%2F%2FW6mZK093coqnZt7VONCy3EaskALMW3z1jReaIiawefNMxInI2nanaSq7RQ2n2TIyBPxsNLirnCcwIo%2F%2BGbNxoI3kFdNZdKFCiYUGDIzBWh%2BsGNxDpyDdvR4n%2FXjxbRbLhFGQk8GtN4aWlC0RUMAeXCOLiREdCiDnq65DGeM8Wzwvgthc3yUI9ZptqgnN%2FJYGShYiSayYhquv7jZXgIo2ciyuev43VBsHWnr8X17xg5gvuY6kNQgqMTuwWx7Dgc5E%2BMIvVG6DcFMPep77wGOqUBlavOU0InP4GPJklgu6i0i80vPsm0nIpi8cF%2BoB6rPNsAi4LqbEimaoYIjmf%2BbOPGoIr7r1ZUfbAjW%2FVqAUo6nL5ZNMCWn03QxGXrrY6hWjksdvRUbxEctNYtwTqMR33u8Qn0JVvJZUzxaB1r9Utp2fcryI8eIWd4LMTBw2Iv%2BSF24JH7Qw898wcoGPsy%2FXFZgTzEnl9yXPH3y0O242JY5R6Dou%2B6&X-Amz-Signature=83ac01b2761d3806420d1de985d80b7cdc8374fa3a3e8ecd1115172e2c8a4940&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJVRUVOK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICZZshjx0uNO2qGQz24S8crR1JI4Jh4sbmjgCZvNEzQkAiEA%2FOHohNcr4AyEbm2RPV%2F3lUK%2BwqliW96z49rMlMJjbV4qiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBDIWRpIacmGXl2lCrcA3kbTF02KQbimoaPlpdXXYQIkkaXMipCyWWAw%2BULcEdU8Myg4X%2F6lr3QwrDF96%2BD0dCQq6wY5lCg8KD%2BgnvnjlZpbZUnPcRbelSz2txwngvA86sDY6%2BVaNTT8i12BbZpsefgdL6znBu%2F%2FQDZwIQz9rJoxH6e1BR2I7qcCzShMTV2y0gvVXBeqCJpEbFKSnNYqmXrVIRLtKgwC5T1X0jJ%2Fp5xY6SKmvb8ghcpIDWW8bg2Du9QqRJ3QxkeyIY3wXZKydChULTB%2BAM2uADmub6se%2FTqQgviPIU1CL%2Boab%2FRTuvw8yCko5HFW%2FJbK0nouGi244kIiddtXAC8yz%2BptmBkEEpA98L2AJ7%2BXyM3SrkcT%2FT1W6Z7%2F%2FW6mZK093coqnZt7VONCy3EaskALMW3z1jReaIiawefNMxInI2nanaSq7RQ2n2TIyBPxsNLirnCcwIo%2F%2BGbNxoI3kFdNZdKFCiYUGDIzBWh%2BsGNxDpyDdvR4n%2FXjxbRbLhFGQk8GtN4aWlC0RUMAeXCOLiREdCiDnq65DGeM8Wzwvgthc3yUI9ZptqgnN%2FJYGShYiSayYhquv7jZXgIo2ciyuev43VBsHWnr8X17xg5gvuY6kNQgqMTuwWx7Dgc5E%2BMIvVG6DcFMPep77wGOqUBlavOU0InP4GPJklgu6i0i80vPsm0nIpi8cF%2BoB6rPNsAi4LqbEimaoYIjmf%2BbOPGoIr7r1ZUfbAjW%2FVqAUo6nL5ZNMCWn03QxGXrrY6hWjksdvRUbxEctNYtwTqMR33u8Qn0JVvJZUzxaB1r9Utp2fcryI8eIWd4LMTBw2Iv%2BSF24JH7Qw898wcoGPsy%2FXFZgTzEnl9yXPH3y0O242JY5R6Dou%2B6&X-Amz-Signature=3a5a3e40e155051e3c5e4db0f2b72b4429e2fe49ce888ac4c70cf6844d5443bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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