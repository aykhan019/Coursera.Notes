

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCXGM5Y2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMXb1Vqg0bkBSkeTcY67%2BXANDl74WR2vg26nkpTj0jVwIhAKNcDhLaX1mcjCTKW4V67h0zy1NUuYEYKt%2BrCqwcLZ4%2BKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwEYe4IilRmZLP1U48q3AN2IvnmYCyqUuxF8sWDxeLE8ClSX3XDpDxKoLeNc3onhU5D0bMGhawAtNAbX%2BemxSyMZw6G%2FDcGyJYPQvT3cRG4wdSgMIL3uYWiEGSdMYjNGV57ol4k2AfERokd4lOM8RXHK%2BS%2BPEAFToLKgNAoyBXnRSIi56rtaBIOl1Ae8HYy0yMfyiRhUqof727KJg3wga6O7AhHGVZqP4qzb5wQLh%2BQwC2eT4E7iWfsYC0KVjKv9kwwp9qlkUYBlOAl7l5Xusz2bx46%2FxIZ2FNANkzi6Lx8jE%2B%2FlDhGG1OC9DRlpdr9UFVsN4XlGE2g5kxbFFEI0otZkOdXbgXJI%2BOVL9iuPYNRk%2Fv1KcQ%2BsASHAFALDHpnWnJPoyHgHGI2uKjEEnBPaVhGKjjkhRe3faOjJLePU%2FJmF2YYLXdc7GRqfRPDJEDWKJBVvRwNK%2F9k8yo1IQ7QGrylw5x6BfMnqaA%2B3ecuoLUBQd5lecsgI6iNzP1R1NbtnHRojCIGMOSZYmNNymJw6SKzgZ5RSn1dhocqudacZ1TnFfsoqzNgkkoiq2LJU4udFekdh0cTK5v0ouNoDHmuIFoml4MTRyG%2B0U4ATVISnI9ZTQWgXOCC4ymvy1T6eDAk1zRMuW2X2BDBq2%2BQGTC97PW8BjqkAcgN8a%2BPMw8MW8GTIG1CjyzLJ%2FQOdgMX%2FNfHgqqDHJ%2F%2Bq673vWB5hpPjiPzZTXwDpJSyuNDf%2BnaB3lhnZEFNqEs8wq2IUIntdY3yIq7hvXQemMv4XqZOXCl0QQYGFJQaY7fA5ImcSXAyYhjCVSK5QF%2FQdKJxeWwwGhticDkkcoJRRxh3bl%2BvG4pVZ5nXMdV0wesI2ghyAnMQWeKjNYyRRTfozsz2&X-Amz-Signature=bce9002c66c5d34d4ac39daa6549196d91765cb681f769a08f84719b8c66d76d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZMNOX47%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fe3kI4VvvKKtP6IC2EHXscZspcdpuNrZVosYdA3NGVgIgQDeqN10zezPkLkqIMkXvT0HkX9gOgFicf1r0u0T3O9gqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkIZqp09Jjq4PKvVCrcAzl4AWB%2Bl1Pb59jImuxU9nn45EIXMc8KfCar4owi4ZR5eS8hXB6txi4AM8wCy%2BIzQaHGOXTH%2FsoxjPy8Nj%2FYhwwaQWhOmQLYoAHm43Pu0mBCIXaw03PfMMIa%2B5u4SEQ42j6HABSdncTmkXhu4VjG3TQtLg5g6V5SrC2C7WKC5IC%2FvgeKzHiK23HkM%2FzEqsYCyN2sx6LI5DHJXpGuehqkNLDDhUe5QMu1xP4lOOk3TdzB2ZsVQPy77sBv%2BsoWbljEjchVcXnjFGJtavCS%2BpWaJ%2BDmduZSQGRNXwoxMtEU5pVjB8Q6jKwPGyR92wmlgBfbR6kBhFoZIFmb2daou%2FclJb2ORVKs4fYG1ZIc%2BNTDb5wje9ON%2FC8hJkV9sHxDlSiQ4MLs8Df8byvfPRv8tM38xaisnkSPHaPVbCCVm1RZISKdFFNoofDumwPbA9UmTJjkGtVwtxo6XRxGwrq63Juh37v0JQkCFH%2FctG9Nx3BswpLuhhZ79I9DaXfhZL0uFTmFOUJDDWbRUywCLn46u1MfhuR%2BpwYAjUeLXPxrOiDJpNsQ2Q2Y%2Fr4nrW%2BeHDBG5RVvkFU1iWo2FyBFb6uObSXVmRwlgmRF%2F2CJhnbdDhcUgyn0OqBH081xAFNdEeIwML3s9bwGOqUBDm4sCBtV199Q1M5miwwO1I7OZbuBDGipje2EKHVixMwc08m%2BQF7ClgoSV1vDCwJJDYLEhd1s%2BCZd65zmaA3GpNpOe41Ta%2FXRTpBwovaMmI1M0tPRpDOGnL1VsaLhaNh3yflhVH6n3UtN7HzrSzOvyA2JLJwXqQm5eLAgopj3cW6Cd%2Bu%2FmHkevXp%2BZIkCYVCKg0UU5n%2Bsz0CpQRnW1vuHsYy%2Fyd5C&X-Amz-Signature=7775c46eff114c59f4dad961f9fcb69a162e7cdaea624284d7720c7825eda22b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ATAW45F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGiTYIDKjhMBNP1vtFc0y2MlbjnD8lYzExXs%2Bdb4VS8SAiEA3SN3R7Rr7lCQmSVfD5wa4nLs%2FYEmnRbLuVsXV1KHNIgqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDXWKJgWIuf2uaczCrcA9rATOVLpaUoOrk1EumX6E6n63kzYxkfd19Lnl3aoTYUoD2Jc6MWHxWTTJs5sXXa7Nat1BweKTDLUXPt06DldZ8miRqHDME0BMGxRGBVhzZ9EB7edvAbPQ3E7Otp89AFnfdGH5BuCx73HGARC8HAQrT%2FwAY6haO5OQ10wYGjUBSdHJExGznHJH%2F9BUvAgjS8icubRBRQyMOOlcW1wmdTEhQ%2BLZZyOBvHiNbEQ9GI4HWeT2hossnvLwOje%2BfrcLBwiJYa9JISu0cZc4IpjueRrOx0oT4P54UOEvmPE0sgtLHKZEeCvaR3cpVR4kK64rnTg9jO8OTr7DrI90cLoXfI75V2LZMhRHK3dplcDBiCo%2BAuhl7FHQ4DicAU04vd2IlPq0sQIPp0nI3kdykExN9AUxUOfVWBkeCnsTmCnYXLOoms1LfAyKf6lwb6kX9vwnj51Fv5tFcurPcHLFO1FBUclGzjVKPRHLsMZ%2BJEYfZB0ebVjoATQnv3jnq1QXddpUGY%2FJx2I1O2UKp8j9%2B0WMOH0rgq50A4QxYSdcouFRNSF6%2Fi1Vf03YR%2FSGve%2FxuuAMBNaaMdKI95%2BUoLgMIs0fvtja0zpQd1%2BxKLhaO8Htx%2Fuj0cZJJlAyF5AlXNzFoxMMbs9bwGOqUBrYk6OZz41R%2Fq3h55RCXx5KFUE5Zn15O9KaXjm%2BwV6N%2B8zvaGqwDZgOnj3VbHqQ5AJaY%2Bq5sr020rZPai5oLP7YTjrZ4y0DYkdJSMK%2FZ9eNrpeWi%2FoVPlbtyFnw2myubcfcr6ijL17HKAYN3upaLdsR%2BUI%2BWvVDALV5bPFES8hQKaIBsS4LJpz8zRu90wGwFlqHSTaG5ex1CZVBg6H00RkXLtQOix&X-Amz-Signature=19328ed43f72595d55f8efce3852b51d066c90419881a172d8f78a9681badbfa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXIGMA3M%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBt%2B7BfYVzq3zUFFgYb4UNYY2vAXpRqzN65Uy8h2AEzIAiEA2uKKjyGUJ53gwC19XZHPIPYXcjKpP%2FV6HNXbMy4bqtIqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHFUAKxpY7Aq%2FRh7lyrcA8hNP8YCiDLr77iMquw9eBcwYsjIX5kqGaZweQQBAI6J5Rq2pkaZm0Kow9oH778nYPsYVVYdqRvRtB8muubOQbhfnpj1PlmOl6rkmoXcYCNIEIqc4j4gXP1YP8mperlQYFB6BvadjLTLr1NqRZM0N4T5Uwm31VwY6u5sSd5YjxBTHHnXyI7EHCjTf6qx3PS%2F1GFHbsn4putTWX0nzW5q786QMpV5iROp%2BT61ywJ10zaGC8CJJlz5fNPI6dv1KVNkqgM0jmNYP7TGi3ZNt5XX1h%2BLMPu9k1nqdDRTJl6fn4Ckm2dYEqBjKF4Vhi7Qxb8GwwGMknt4FYl3gsjgtHDFcv4eJfh5nEvrrmDCOL%2BDS7Gt4W9quWl3iTPYnepYfYVo%2Fm0m50D4LDz1Z5Ved5DapHk%2BHolIdXLeicZkKvdzYOiKC2DUd3C5U%2BTGkMISv1%2BevCETsLgSmEhBv%2B9gsRINW%2FTZYsMHjaaQWzTa6twnjw7%2BaxpnBHaucM%2FXL0Q8UgCYQ3Aa9X8BYKyRs9n%2BxR5Czl0VhA5lMJGlifhnjQkvQeNNG6bg1QBsrZF3mnNnluH%2FvpaF%2BBjh3qCAp%2FOHHSySXgVabeZUaNnnmcv7Q6dP%2FTm2cooU16W0xhmwehjHMM7s9bwGOqUBaUP7CJFnPX7SxhdERdEIENi1ZKid73APz2lrEMfNUzXp%2BatqbhsywGhRKZjRZn%2BiRwFmtSv7P%2Ffn1m%2FGmgbDU%2BBUel3%2Fo7q4yD6GbZCLgnw%2BDYgjXNfmlV7lb1kjYnIhIh7h3fXNN0nQl%2F1JSGSTL8dKXZGDYj1%2F%2BjZXQJpSShqNgC4ytSOPZAVcO58p9w1qQ7VLwALQHqD0PM4ThSjo%2FWlKrCr9&X-Amz-Signature=f34cba184cf14ff6ec6d519d5f25cd92e8dd500f72a7e5c37db0a3c77e52d7d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCUJJGKW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJsf2IFOMQ3hPWe1jv9xuLRgyE7NIICkuhmt5h04TG%2BAIhAIarvOADY9cq2ZbA4vvE791bwzRfxakyVoV7Eqy6YhkXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwrVQazpaEIDC%2FABhcq3APyOlzBOWDzhBKshxsSYXtIEvCPqn%2B9WNVklknX0sqapB%2BXxQ6cazXgPuOhViF1KYgZT68D%2BVDKv%2BxjYmYMCB8iwnvk9hbhyXQV69SHDdzrdT0Y0dkuqwNcwU7iwyHW7yhjNx0lGbVL68SxMfWMc0hpC7nhH7Mo3qm5AVh02IDrOc2kuuEmjlzEnRh4%2B%2Bfg6G63TYtPIntdzX4D46zUJmZcL5r%2FDNu%2BxYTfYRljfKn4S8fUsdituZL5xXknAOibVQ8iLjgW411ptFv4t1JVs9wqJHmgU%2FaJXpQ56Y1grGE0eHGqyPMVBrUKmZ0G6ORiD9f6Bn0I38fj86kVS7lgUqVTc5PqWXHA3m2I%2BisyOaASfhuCcKMMfJ0xpKuT9jeHWSY56xNTdQzIRaQJdim5v4iCrogc%2FPvv3KB2zUUNPj2f3KZhHGqyUEnpdR1%2FOOe0an7WxBwFdshVHf%2FHVDIR87OlzUX4LeCzWVNTbrW4FnNb57i9AwmxwsykkZ7SVlggjDzGgYqyuapPPqNrQkpxRQHPQmWxM7XdsZTmN%2Bu3p0BibEosXy57pyRv3uaYFapuf2SPMb0YpfafLR0wxqYVp6z6O3SYUSvIzLCTPiLQX5b56RQSpwJSKs34I1xYBTCF7fW8BjqkAQCf9Ao4QAHq2ELUzSNLB5v%2F%2B2demDwTPFGJqng0dM3NTWh6EsYJlTlmCh53mgfjgaydlYmALwKsqawLA%2B0Ss1s9VAq%2FhOqb1QsPbYBjH2CfzcQXJ%2B6LUa99aP5hg%2BK7YYLgemU5x2T7J8HjEafl9f6GhW%2BdIP64ZafkGQGbhi%2FsMjmQh8etVLLD2VYncdzopSioSdiiBD8x%2By8y8nynBt6EYsfR&X-Amz-Signature=7f9e0556a86ce7b7ee71cf2e40983487d6ec0543e3daba38d99710da64728a40&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCTQJTRZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9d4ccY%2BJ%2FyvFpQWRXm9%2B1ZKxEWv0Y1qAGl3MTpIwmngIgBGQRyBLJzUzdcg%2BK8zLDaQFgqGk2plpkIF5tUJtqDUQqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGOB8ac9H64HQ27uFSrcAzg9RgugwOeAtp16gY0Cxr3w7UEtkSkr1TPFSoujhXVG00ZXLuRuVzyv7wrQ0Xv8bOyE1EsCoENOTmay6KhuNSbkPPuH%2FbuVUVgqAI%2BrOxFK2XYVjBvFvIGDHJGBEo%2FoU88%2BUDtZzbZk3qVzLvghasq50v6A5MciTXGiCfffH1ZtyzZNajxpqr6nINKKecCiHZMtcxqMJKpgR%2BQPMsKm7T2Hh7qd12oNCBU0vbjasmQK7bjBR9HZz3jfOnCCn%2B9XyjEAFapJtVrx%2BwnmHxltg19joYsDiCiXdyJhFoe%2BQgH%2BxTjEmZHXJ3WGA6jEOC0VilgSVVv8x6NWyYm2ZPcvdslr7UMS3vnn4CODCPsboj1K2k6f%2BdsLLJjPFPACqXRXb3AIdfyciN%2FExwIaAVR0X0iNytwuH%2F1QU5tyBFk5vQ7tjh%2BGkO2W62G38M%2F4oiDmOakseLC2a4XLRq9m5v5VUL%2Fizrlop2b05NHm4dwalSIwOpf%2BdpTt60P57DmBKMMONOlXV0OcKU%2B%2F5qK5SxLPgMGW%2FDG%2FseoMHQ37GxXsptQUV6CfvjQEtdV2N0buby5g9I2KSysU1zy%2BzmlyCHDkmab0lFCH4J9G3XDYIG7e8QoFrI9Df8mqiJ877lkzMKrs9bwGOqUBFBFg02qLMwCv2w7%2FFREvj1ewK9smKEyIh4u065alKVJLeCFdBxmwYMlCTlGAx4z%2BceC5x8MSWBuwPd4zLsoavxTa33UxZN%2BEdmbjgrLYboPvtKfBXdWOPeCK9phXqWF2gpZ%2FTUN8jQPTVzm9PdrKf6cNovsng9yC9UTG2plPZNZ6bHgynGauGWARqMhXKj%2F1E0Oqo1iNVSKLjzwiuPnfb83ZDyw6&X-Amz-Signature=e5f7ce9f159ceac3f38efab483f97e3e9f0218e28bcf52e3aaad65118add73eb&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2VIHU4M%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx2WFB2L8kJZdfa%2B2YX%2FCAEDpyqVaU6TTMPH2p9h%2BQrwIhAKT%2FCOZAGT%2BGLfd76dr4MXh%2BeeLc102bqiwt75nVgpBMKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzltWHlqZ%2BNWQ7U%2Bm0q3AP%2Bb9HO00pCDt6J8E6TK67oM%2FeCDGhnmhVAzpXFWJslmymfgCZVki72rBdSPB2CQwajMU%2BHaOPfZTeBD%2Fyg4HGkVqxV6vE38LSLUiz89iAwo7Wxx2VYzF%2FrxLYepN9ESm5ojmSJDOq2n62gaJoQbhLHJALfl20iRc2f3uwm%2Bs57%2Bwgkk0HW7vZAl2HYbPuZ%2Fo0XvTCoVSLmFm4980IS7qbUBHj0TxldiJx0aZ8vVc6nFO8mWdIP7w83go3hNu3Sn9GVkCZIoKlWvWHBqnFZZ02SQEWaClIX3fLzfRmNPH%2B67c%2BsSN2RCP0TjUpfKhbLt098eG94ZMG63A0A9YNZxy4PfWVRtCN3zs%2B0vO8hbKrTYA90zY%2Bz39YEiMpG8FUglFAjUEhixhyQK0Rwk1RwD%2BVy7huN0eBvi1UeRmKwnNZSHaE%2FohsZcx2EXaHo8eAIRZ%2FTASzaRbzqzG6%2BW%2FsWjtGsZhQBAzk14Na7pm5C1u02uoGrcVsiOJECmaZY6o1Dxdaprk5%2FmXo0SPV4lQzFgXJSohz%2BbkJxOw9xocYY5zzbCeUhlRJ6twOxXyBBibzPfGBBeuGmXQD%2F5Ma2cnPwlsAD0%2FEfkKQp9eJQNOk%2BB68%2BmlFeC4lx1lmsjzwr0TDD7PW8BjqkAaJ13eypkpuIMHjhSpUnlnS%2BmLBhEe30XVBM3EZH0dwy9dL5dkq37W6zjRp5DlhlkpKrnELC6d7jUMcWlypqfEivlmxtiHR9msEupSoYFBpOnoSt4OVSZTZkQW08cRgBRhuqdUeOjRMNrYjUHIggNZ3SiPrNpb2OMmUJQNbQLouPkhNoD8ZvcDqSPndM%2B%2Fl%2FmxTIsmeTeqxB9PklNWJcUNlGKBD8&X-Amz-Signature=6d0bb6fdd9650cebb97a46b2e766364716bbc6ebc2803a627c3c06c01a7d4b27&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWUK5OFE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpN0eo%2BtO%2B%2F4KOJ8z0kontByjEAvGiXRUhkcck9vM2KwIhANntmm%2FTr1%2FdFpg8dU9xw1R3KiVdoGTXKvIjuLZGEubxKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwC4D1rViRejI5tJzsq3ANt6qb5po5UbTMJbn2VgaD5%2BWwssv547JJOrik2%2BwktKefCSjPOc5URNdzwqaDE5Ndl4Ob4%2B45LGw1QkyMxPRg2GkZR8W4fEMKsis8XR7suuXgCNXwcVlU8krwRM2X6TkXHZdSqyHRj9OQ3yTvEtN8OzmMtj7IJQ7HJSPKQhrwZKQRvXKJ0wrUpjsWZzPc5AbEYaSu1pwnp%2FXslWlhvSqMHxz1BkYt2Y7gkgmDqc4s8Rw%2F1N%2BxX%2FuI36XtCjo7fq%2BcSiAEfN5530c85EUv2igKKgicuQJARtCmm9xt%2BfEW9puPmvLT6OumGsx%2FvGMx0sim2nZ1bBXlka2TosssALDIC570W5VRtn27cMRTpJpbo5puu%2F%2FvE%2BNgRG0i7p23OeGCb0etS1M3OqFGudUsg81d3hFJrmA%2B%2BgzG6IcbWkWcWas%2Ba0MLwO0abQbwc4aWpHXTxt%2Fy7ZGQ3LarHKDXO7m6T0RnPsvO9gCMh%2FlzO61PzROFJvh6kyqtcO%2BI8lR4xwiiOTXGOYyq7V7axz5hpx0RDDYOvySyUVnuN0Hfq9k%2BBLnIfYnRm0AtB9s%2F5deqeC0rErcAuGmIjUeWQJA5bdM3Lz13X5BE7bhcZSH80Oa8YYadNcZM07soOG2lJ%2BTCd7PW8BjqkAaOYPhGccyF4GOaBNVKkDPYVoIiENyyxljDIAUMfQ9kwep4Zp7wrgrbWb%2BGA2tgb7fuIhJvKVzQCD1f2bzI0dA9aybHEWUJwcHyDUmpG1KEVtTtdfW9pdGX5PSlxHaYDZRV3VIqmXi4x4lsWWNxuVA0ThVXu8uPgDcFFgVjGZIUwSP0hTAnR%2BRi3lnpIaLJhY4aqqYoGD8JtqDJ3UHpXxjwPivno&X-Amz-Signature=3ddf9a1d5c737dd10ff580ff80adc2f485e71cf93f988a37a473a6bebb726b39&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCUJJGKW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJsf2IFOMQ3hPWe1jv9xuLRgyE7NIICkuhmt5h04TG%2BAIhAIarvOADY9cq2ZbA4vvE791bwzRfxakyVoV7Eqy6YhkXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwrVQazpaEIDC%2FABhcq3APyOlzBOWDzhBKshxsSYXtIEvCPqn%2B9WNVklknX0sqapB%2BXxQ6cazXgPuOhViF1KYgZT68D%2BVDKv%2BxjYmYMCB8iwnvk9hbhyXQV69SHDdzrdT0Y0dkuqwNcwU7iwyHW7yhjNx0lGbVL68SxMfWMc0hpC7nhH7Mo3qm5AVh02IDrOc2kuuEmjlzEnRh4%2B%2Bfg6G63TYtPIntdzX4D46zUJmZcL5r%2FDNu%2BxYTfYRljfKn4S8fUsdituZL5xXknAOibVQ8iLjgW411ptFv4t1JVs9wqJHmgU%2FaJXpQ56Y1grGE0eHGqyPMVBrUKmZ0G6ORiD9f6Bn0I38fj86kVS7lgUqVTc5PqWXHA3m2I%2BisyOaASfhuCcKMMfJ0xpKuT9jeHWSY56xNTdQzIRaQJdim5v4iCrogc%2FPvv3KB2zUUNPj2f3KZhHGqyUEnpdR1%2FOOe0an7WxBwFdshVHf%2FHVDIR87OlzUX4LeCzWVNTbrW4FnNb57i9AwmxwsykkZ7SVlggjDzGgYqyuapPPqNrQkpxRQHPQmWxM7XdsZTmN%2Bu3p0BibEosXy57pyRv3uaYFapuf2SPMb0YpfafLR0wxqYVp6z6O3SYUSvIzLCTPiLQX5b56RQSpwJSKs34I1xYBTCF7fW8BjqkAQCf9Ao4QAHq2ELUzSNLB5v%2F%2B2demDwTPFGJqng0dM3NTWh6EsYJlTlmCh53mgfjgaydlYmALwKsqawLA%2B0Ss1s9VAq%2FhOqb1QsPbYBjH2CfzcQXJ%2B6LUa99aP5hg%2BK7YYLgemU5x2T7J8HjEafl9f6GhW%2BdIP64ZafkGQGbhi%2FsMjmQh8etVLLD2VYncdzopSioSdiiBD8x%2By8y8nynBt6EYsfR&X-Amz-Signature=50c81a3d3ccb8a65948963bb42f52047f569c005be7a561708040a135c848d6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BDMYBK2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNP4S8pohpRirjEkoF05P085SiC6LcWANRpeyZvwNvdgIhAKEzQsOHFvDkLjj1jD6qOajrNTsltGxs4XoJ%2BEGFyt6AKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwMk3IVEAfYUDSNRQIq3ANdILSHivRnjFEuO4XZznj4afto202D376LUIPh0wRxHD8Xd9LTNm8Gb6J8YiwFr%2FudfCKibrdSJruUrpC1Q2Or%2BJb6qedmE3UOO9eCfECC8v7vACo%2FObatbeUtyi3JnPFqtRAT8%2B8eNbsV2MJmpgETBn0gP10Wqfe7CiWQwMgnmwKJK5u1%2BFgE%2FsMWgFnT71UDq7eNvJAE7fIkP3uSe%2BdL0aKYW4T8FuvxpYWqpzULz9caWqDbERj7jnjQyiyErhxj0K3fKjtNIQ%2FOBwTIfs9r%2Baqgo34YJdBY2w7NqBaCcn%2Fx%2BwUcGY2cI%2FboWd3%2BYGSEIIZakdmGy%2BshyuXz4oJn1GnAXk9Oenfiw1Q45K8oJ74q7GSjPfLrA3GTbzMvoQKwvml4St7zFgyVUUfXnCKDD9H64hziXeCii4cTs2d5mgrOnqOVuFDuExw56zyHLcLaXR6kgjy%2BFTkCO8GtpAyr6nNVb%2BuBg2jwSWpIT9XYZ0zqE1FK7Zd2toyPrnV7LqjTUiMP8d43j0yARAIW6bPXKr%2FEMuJJ%2BbKHdHSy5CBLZ4YgKzjORgh3oT3eQPfW%2FgKvJr43pk9gu76dJgdnK6dErgY5vNC1oDyD9r5M5I8yge5S1YUEHLFgTaT36DCa7PW8BjqkAYucs%2Bjl9Y3nooR89GJn7Wwpg1%2BbImcaPnTk6FIZrc50PcfzJXOiE2eirrBlPlc9AaWRigOkUXhV%2BzK2QAQTIjEmIa%2BP%2BOSzGAR6Po%2BiyI049MbF77jcYyYojVmAvpoF4vapywefWeodCfIL9Rgnr%2BJIOKsiJS1xIbE%2BmaIClDlJBmGVE2bhQCEEiN5y3q7XtypJCtaC6vNi8UfXGE0MH9nD9b7C&X-Amz-Signature=4be744563ecaf1c3d5131c886ad6308ba301fa48bbd490d1831ec9d24ff69545&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BDMYBK2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNP4S8pohpRirjEkoF05P085SiC6LcWANRpeyZvwNvdgIhAKEzQsOHFvDkLjj1jD6qOajrNTsltGxs4XoJ%2BEGFyt6AKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwMk3IVEAfYUDSNRQIq3ANdILSHivRnjFEuO4XZznj4afto202D376LUIPh0wRxHD8Xd9LTNm8Gb6J8YiwFr%2FudfCKibrdSJruUrpC1Q2Or%2BJb6qedmE3UOO9eCfECC8v7vACo%2FObatbeUtyi3JnPFqtRAT8%2B8eNbsV2MJmpgETBn0gP10Wqfe7CiWQwMgnmwKJK5u1%2BFgE%2FsMWgFnT71UDq7eNvJAE7fIkP3uSe%2BdL0aKYW4T8FuvxpYWqpzULz9caWqDbERj7jnjQyiyErhxj0K3fKjtNIQ%2FOBwTIfs9r%2Baqgo34YJdBY2w7NqBaCcn%2Fx%2BwUcGY2cI%2FboWd3%2BYGSEIIZakdmGy%2BshyuXz4oJn1GnAXk9Oenfiw1Q45K8oJ74q7GSjPfLrA3GTbzMvoQKwvml4St7zFgyVUUfXnCKDD9H64hziXeCii4cTs2d5mgrOnqOVuFDuExw56zyHLcLaXR6kgjy%2BFTkCO8GtpAyr6nNVb%2BuBg2jwSWpIT9XYZ0zqE1FK7Zd2toyPrnV7LqjTUiMP8d43j0yARAIW6bPXKr%2FEMuJJ%2BbKHdHSy5CBLZ4YgKzjORgh3oT3eQPfW%2FgKvJr43pk9gu76dJgdnK6dErgY5vNC1oDyD9r5M5I8yge5S1YUEHLFgTaT36DCa7PW8BjqkAYucs%2Bjl9Y3nooR89GJn7Wwpg1%2BbImcaPnTk6FIZrc50PcfzJXOiE2eirrBlPlc9AaWRigOkUXhV%2BzK2QAQTIjEmIa%2BP%2BOSzGAR6Po%2BiyI049MbF77jcYyYojVmAvpoF4vapywefWeodCfIL9Rgnr%2BJIOKsiJS1xIbE%2BmaIClDlJBmGVE2bhQCEEiN5y3q7XtypJCtaC6vNi8UfXGE0MH9nD9b7C&X-Amz-Signature=a753cd42ced6d4a2e006750db9c2a37e99a752834c5d3d87317b3e36d238d6cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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