

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMSILGML%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQD7l12gVjZ1uSDMJNj48N0X47Mo6Hnk46W7e%2F7yZ0xqEwIhAJGYIEq8a%2Fy5d3FD%2FFeiSLDZE13aKx%2FOWMEx2XdiFcf%2FKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjScqd%2F3d%2BIIccRrIq3ANlRrWBTNskwcH%2FJVeARLb87sc7fDHhJqeBSnPpOuUCWKHzuX91tQV%2B0doO%2FhoBiMEAm%2BXc9k2nD%2Bx4DVu%2F0elPCHSTvMj9i0ePwbaK%2B6TrZ4Uno5p5VbHC9L5%2Bx27DKROlM0eiKZ8a59QHsqblegMaz5zqOJzD%2Fh%2FuImgv9awQByfY0%2FGKwno6ETwSYW0WeOMowhm%2Bd9xmfjS2HFsyWT2SHldDCK88Sm6Nuxuy5iXyLpdvOIGy078WJ%2Fpd0ITMvFzENPoIa1R2554We%2BJmnSkADqz9X7JhvQ9uKCRRsAfwggIsYKI8iyuriwa7CD4PTjIadwoMax9XKmxatqOu2%2BDh9R5AV94fGG4R4wH2cWuUyIDzBmrCUKJBI1i5e%2F%2BavtJuRKPYRGHdR%2BLZGq%2Bd7jcFMkFUKtJVXl5wMAgy0%2F4Aum8eW%2FTl1O36FkRbewpKULlxVMdCkAJnhHVD3xpAvkLKvX26mn0AMBhTOzxIrLPfBO%2FkXu5Y4dJgeCnw%2BECoR22iY1pbEeNTsRX9l0u0UIhLGe6dbUb5E4yPTSCyEydfdc4F6KaS8FCuLR%2B3GWOl0jPXExsVuJokBVyPrbOBbFUi0fNMT5VzAKwQJTy32bykgXhv13CsSH2lxfNT3DCihZ29BjqkATdTyDee%2BF8QTcAMpw8g53FFtn5aCoiJG%2BnA751TvyYNtFNb7bNlnzPwEg2Ma5qIBqJ4rYngzJHuZLfFw%2BWkS%2F3oBAkRZomFF1o1UNj1QLUgHJ6tKZWAxzADslkcgOEpUKbbQCjbW8bPytzHubaUFpQxl5iG6dPs%2BGBwO9EfHqgGVYByGGCPG8%2BZs9pfwhylW0mfGVcPaEwUFSIPOvFtlPcPGIOF&X-Amz-Signature=4cc09ae3638b4611eeae08b2ee60a0a85bb3725e1ba2204172ba02a06febcc2f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664P44OYJ2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCGEBJs9Ih9z5cZpLzZafuSmh8bYOrfF8TgtdikRa3AXAIgEagat8k6emQ%2Bk2bTSSTbZetGaPeu1jKMUxQZapFXlXcqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFpWXfgDK87Z2N5WjyrcA67Jgla3L6x2G2%2F9r%2BsvCM1U0jxLvTIr9j8xp21RbcDTkpfFJibyX2bO6cDa%2Fs4ARMtYoZU7NyQ%2BTBqzkzNKCWqUoAjkYvOLYvULZb%2F6n%2Fqm4hVzeUzrpU6j2NQaQPuK8x%2BR0Kox1R0x4lAKKH2jY%2BPurJv7slfWNTflZNBULsHZXLdV0Z4uL3tNcioGBQC9JDa2UhBLNkJytJOe88QDUMFiAVOmpGujRRaNS32J%2FqKgIe0kqNWcQabwNwMywU57fouSV6YCCj3Em938nXtzNGFA7CAJirdzS2cNVhY1dPkHkC1yrUFlu2wMnMTkd42F7%2B6DtGi510iulCzfC8Wk3AAgT%2BKZOz%2FaCl8gxx2NYOg8iuJ3SGmYfK%2B8BIzKivsyeZCukariklTtmy9v9yvGE7QW3rUP38CvkHSgFtH7Un81MorA1cKjk9%2BGoVam7VeKG5l8VMLt8nnpUFCL3kyvW0HfAhjtBZkLwUaACob2iDXAVhfTU6FEan9vSCWa01cGaPRFn49udoWar%2BxJWfETOaFmvu1ZcTx%2BDQabnJnPyy%2FP%2FwmCQFC8q5B58eOYi5lUKpoRvgUVPFKvfifMji%2BPJK3EqxgoH4cJhdGug0RRpsQFA2xHP5pP%2BX4zJ6NHMI2Fnb0GOqUB%2F1KAMsbIdZA6xP%2FzHLZLrSOroHCC%2B%2FYtbp6DooFyXLIZq0V3DpMLcCLm%2BuXtBNZmBfRFizN8TG2WgBG14lqTee40A92V4qe78PMBKZ5lPjFtUcY46%2FEKAbXB0LjoC2K2%2BGChiJ%2BnsbSPDLb5sXDxHDZVlqfdqWYoWE6nh4A1%2BgUpuZ%2F06PTY%2BwbV6rFQAIO%2FOG5HgKelKgGRPQqSHLBII2GhOg9c&X-Amz-Signature=a7495131520636f504137e8ff91aaec27a00937c520d59a15230b43b1c7f588a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQJJUL5J%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCfwiN2S7ME7vVWDJkN9KLEt53SJiRuXgOv92ktvKh6MgIgcy3k9Ai%2BHiytCfBa1piYX708MrxNwFE9yvtEwGI26M4qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdjPmvGHibO%2FSh9gyrcAyzmfy%2Fr1PA2hj4ONm%2BVFM%2FWMC2S6p5Me5eDlT42rOeoWnTBjJvMFW9GjJvEYhDhfU%2FZ5wqLp3nxSgIcWWRkLtpbJ3PdGuj0QmQUSg8FruP8kdQUloBubGd6bpY4X%2FyKmM1%2Fwt4c%2Bf4ywWw43tQMIqXrIiSN7ogiPsIclR%2BvtOxlBGOJjG96kTiLEAGnNRKtkw3rtVhdjdZruTgBCqAcJUF83iCrxlDBqMeLl3pVaz699RM7IklX9Zss6Dxwe1cKIrkskBeimgs0pUzUCQxHjmGp3zi7pcy93VV5%2FmxH82TvYX%2FUzinfBX%2FvXsSt%2BCXKEjv1mgG4vll%2FsUGZIH6ypmn3VrYHNOh%2BGdpSjOUKuSScPx4X2kZVUT6dWMSRUE0FvGVXponY%2Bn8v%2BvXLa9%2BnyJZDe0a7zpA%2FQdlkm5vL191kSWnUh53EG2wTq4rPnZPBEo%2BFacFgmcjZYkgo1NYd1BjJWrWnAhH0FQg%2BKbhwpeXAbmJHGEcLL2LVUM5B64IpFRWqJVDugn48q7Ln3tKQnoVAwkgkY7NzuD%2B5MQbVUoU1U0AlfrlXVSsbRk1ElagM2HRG1XyVgPUMrFa%2Fk02kTaIfRB7z1OKghxMRW8ZhmlwevNSwK7lN0ymJ7YvCMLWFnb0GOqUB30yAG7I78St8QhUpAz3I%2F7uIY3YEWwTUGbvXHEPl4uMZF9iUWKyDUmj5VThamXl0h8sWnDglpgQzjmMna%2FM8Cjz5EjgdJOwytuPtF1kYR8spZq%2BUMS%2FERD7F77KEUx0886UlaVQFE1%2FPHjDUZuUHYMrumjtjjVyzfqQr0pcGATq%2F2a%2BLi49VfYo4DrRxfcM%2BUmAa3hD6XxAYxnnTNTFZg%2BQLFrPu&X-Amz-Signature=2be7c26808a53184905158c6bafacc715a6309c9191e461e912585b9023bfed6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QHQTT5A%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIDxJoxhNT107z3YCZCX4duohQP65iRHhW9eU2kh2YXtAAiBSUP%2FWCuNsoaSp2B1jptvVkiADu14ZONqGJW%2BCcgsVnSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9xV2owEjnPIrH%2B5zKtwDZAgR%2B34o8maEQbQKJCNQc1g5jCJy0ZFjpIblk8xnJ8VkEL3KV%2FSK3fSneYJ16KxGRzem2iAu1SRWU7nDECE7hV4fRmtOs7O5OBEDA%2BqF4eJNClV%2B8MOlEtSfW3FZx40nygHnsK%2F4LJ5K%2BDQ95Jps0E1l6WEbwMbrRm9xgiY6XSVy2JIhcSwVP%2Br3BJUKfF0YBjujynrfpHFd%2F6BO4lIjNDxcKy75Njjv3r9707O9t7pZlZ1gqeMEwBHzvh2pXaLLd5icUvLUn3Ls6EfwhKlRAz26ZndTcOLsD403hINBJd5cnfNwLQEALG3tqoD3VrUPUJ1myXeXpOhxRWyXtsL4qkyouaLEr4f2lzWLcI9HY2Xxtzf08Pb5dsyZgdsJbhJWMkt%2FjckZmjMoa9j9OvjS1DsDPzxPFTeo2yS2jrg3Uhcp7knJastCLanTxr0iKuNFMHhRPUsejcXB%2FPapLqlGxGbrIl%2FxkpGV7xTOKp1lakcoFZAGBxJ0%2FsLZyAJE8J7afjGsGPvkCUn%2Bfqcgp9zQdBoHR4lugiu7ZSdEbo985flkfLW3%2BXCAQEYZQIHOJzHzYDQU%2BTFZi0LZqk0n7HMUaA4Tvr7HJrGif5YHYTMoy00FFFJxlBnYKsZkzH8w14WdvQY6pgHE9NMtB9574YCbM%2F1BW7rA0qsdgFTYYQQBbj8HhJvm9DAaEknCBc4ZEJVJFc26N91dgCLP9VMTpFD3QD43%2BDgWMY%2BJGnzLibRC9RO2e7BSxVIF09Woww4NXbLs57IS9jnABmDgRcJgJvHQVjVqX%2FEIajW7L9tuiqcq8Yai2pp9CcaykoVDnkcSp6g10h0JXhoRrxHzE8UMDi8dYBZrRL6JhKFMdAoT&X-Amz-Signature=eebed3ac9f782b8f6e1c1dcd15c2a8ae148fe12d1c2ef8b897901e68c528d3fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUNL7KOW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIHzqx939Jwz5SpArjIWHoKZqFTav3clKd7HxY5XrTlp9AiBty7d1HY6xUOSYXTSOhHzIMRU9sb4UvSGdd%2Fc7UvG29CqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwfZvG4Ohufh5Op7KKtwDacUTYpnGLFrarSrvInUBORxivU4WBEoHKZ8zWxXHpbhIaXOiD1hb1BB2Mam6CqpDDwLoke%2BOtoNE5H4KvLGfOq3DmtvqHHm6yXVcTpvwfH9W3TZF9Xj6yuNFARwomgKqoV9DIYwa8fFH3F2vu5iGAuE0G%2B5XZIQ8nLpdSwiH6LpPpvSoFDJS5dGQiR4HlHBQ%2BtHYCBJVNwOJIeRUX%2FriEjGOtsHaerNazxLDfS7LC3Bqv2Uxa25ReR5q42mHMeOPLKxwTk1102tLdVgelmLbggEe0L3g256FZzV%2Bo1tftPheWLriz%2FnibMW%2BUnic3hv9Q2XfwLqrE7LukYleLwL9xycWR3Nbpmsw8F7nrIsNzK%2Bvv9ombRuJUE2ZVsXWbj5yvHSEoyaTQy9%2BxNv8YrBPaZDgfuIsxrGBoJuSumbDrnPyfmkEfEUyi%2FjBaFsMV0GY9jquT3xFbiYMg8uq5igxnrKiex%2BgcsU8PnzpY8Ojbp5pRCKb4%2BAY9sZnKu2qSA5KwjFVx0xPCl%2BmcyfyRq1bAZcOSGy209G5bojOWH8Zrx26fLaM4w%2Fw5%2Bn5A1jgJ09Y2c9pRl7SxZN6k6mdCwoeBnsdgsgSOx8F8HijUT9qxHCZ3lriQHflU3z7CYkwsoWdvQY6pgGtH7iP94omFPJSxRTkNPLJVPCTGyc0xRGo02N6KOCk%2F4%2Fj1o1ZWF2kXRF1cQ3V%2Fz79o9%2FfjFcQkWMQNHNf1njD3c%2FpfmaK9gVQIjUWvrOTiG1Hi2rzVN7MwxL9S%2BjvvxYQ3eJHz8yw39nu4yOB2CUlJEXYksICXVsCG%2FhgBQMoIq1S3VpWBTdG57juS1UgyFawK4GwtUfNuXZKgbImuUL6S1ED1crN&X-Amz-Signature=e1ebf070948f58ad97274e5d27350ccbf1b688f585c4b1f2311a769c19900619&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W54IUTVS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFkm7oTA3YRmj4jMGSqIE1IJKmVd36rnSlF6mU4lzCU9AiAAxAbNqJwI9%2BHXb%2BaPhLt2I5Bsch31SkagB4%2BBJxprvCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmXqAMYZsSpol5FRoKtwDRjdah2osXe%2FD9xMx%2F6fpbPP5uje%2BuIOdiDcno3QxZ3eGIyByvpFoCKtl17o8Xs728k6FAhnIuqxQegWjyadaV3a%2F4RnOgUmzj7UB2jaY8oTSbJEZQpqKSalTXYRbKoPo0hQkh9zJbx7cVbhGvDywM%2B1qwaontHaB%2B2Z9EBAhxhakmfWyLr1Vj1Lx2WWeLhHi4j4ViLcAsNhDufXnqD8e5zKdoGClj1p0lz6AwJHeBrzIWNVTxmDP%2FdP3k%2BWgMwFIMLfr2SlzrEsSrzh0nN1OmI4wLkMYX93O2yVenweJtV%2Ff9fd7U4ro8Rut71uDXZnYqHsUsWxANp6gT7eF3fsmM%2BuOlaYytFjKy8k35PjU4xigVPUgNHqO7qsTo9xkZQdqC9iCTaJ5BKCTPMzfKoPu3cyOppPdCHYauPUSe3IVuYtuVVk%2FfQNu7%2BBF8Di3lsz%2Bxo8eAWwQ2DkQxsD0XQZXYanEw90yrCYKoiuPtHLMKbkiOSRuSHXuLlvxz75x7U5dnX0C6U0QM5Yj6r2pMVOawyBOu2CVv%2F5AC9DZSx%2Fas52pjcGZtuWgPLcePf46dmqerOFpmOt8Zr%2BbrngVbrRz9py46L0YkB7LIOLl0BKR3N2SWKtY2CHLPfVIk4IwhoWdvQY6pgFeiE8NOZBUF06sdsQDGuGACFvh3LzEHv0NPJgepx2FcjOBLysz5EGmP%2FAoSQsk377wTF7oQH883KAjZfYdFfgdcmqjjrc8clanxYwcSFwTX%2FLwu7EHZJi4IQjxwwAio%2FK5qXt9QTcQqWYcEw9jnzskjx1YpD8VrQuyiQ0zuzC8QiyAPYVMwSzKe7pJzBmP2H2R%2FOvMSmnoZUGMZ2UG7%2Bi1bUN32eUZ&X-Amz-Signature=9d7b4163d02e7fbad15937bc31553cb7a42f5758253e8decaf7f1711c174c173&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XBVF2M4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIEuf1dWDs7I8Gs85Mrd9TeAQzf2Doz0ygq6Siv5FnssLAiA6KxfFnT1iQo8QIApT%2BN1p4KI9kvVAUKVaXmkHW1kNeiqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq0JRRYrNAyX5Qd1zKtwDT2AYCx9%2FyfnPKdx8h15q1OmqwwuIh35Pv98RzAMKz%2BK04DVRizUACrRgsmUpuXdnc6hr9%2FjntaM9d12neMDIdT%2BD5D060%2BcGbjQULSk8M7va2zF6h4iKTmSZolo9pJauYUfLWKHhN15sIPBz0aHyYQ5coWrsqHmCxiWDD%2F1ilCRPbaZ%2BGDyMHNOlDE3hfIMHapH3k7Tlhz5aoBjsHfgNZXHwR8h%2FaIoQXdXRCJouJ5je9ip44IlIs2Xs75F6sYw0Tn%2BaLw%2BnhhXsRUslt4BrRxtfww%2BXIUQ%2BftnhJ07Z7oEwnuPO5NiwO6%2FLJfOyxT7uevHvhQCX%2FDlGHISeqbeIJUP3YF8GEL%2FaJUIjCXctUj10iE36R5ItEXn%2Bf1VssjhuEBP7jAMPt4WVZc%2FIlkBjXeDiU0NYaEbzdNP3%2BPWTFsCmPBynzZayAD0U%2BaL4BqvruXTtcxR7cvyQPE8QP16epSzRlo%2FluP0QH3SWeFD8ytYuZZJaRe3Xdm1bmPLr9qjCqzKTGOmISL8sCcLssaDxPQJmKKsf49UgyJFLYAgU7qRQ53u8ZAIbrkRvhz3TD1Z99ZAxJMfQ%2FNHyOp0bdKhyGsLmhuZ2DAa14E8s%2FJVUSet%2FJkV5nP2ZJR77jLgwzIWdvQY6pgH8W7cGhLxA6cWTZBsBoBfwdkgQE5yhJPfBMfkdypUKkIjW9eOKAQCOm1gwhkmJRfzJE9Evcn%2BVCeZerIfFGYqG2PxwvVD2eYnEphseKUdHGg6PeKxIc8c7w5yeHFfUVFYvPyGRnMfwr%2FAJkqCRnTXxRXxHj9ZyS7NQI%2BKQVaiuA0xTJUt%2BO29nyxXfFJA3KIr60EX2Q8DhnkB5JQgbjawWjQCQNvnj&X-Amz-Signature=2cf805b780593a8f3827fda958b899039a902a6f1cb79802ea3c6850fd5e6c8c&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFLJ57RT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDxe4Z2QucrMyiD%2BqYFAkt%2BgQtkqJ3xloH%2FFwCb%2BcN%2BGAIgPbd5eGIAfU%2FAPcvvFD%2BJKHbkS0YqX2If5AIcIin%2BNYYqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLAiVm7QilUsAIkA%2FyrcAy7ZPHCTkVjOHx3%2FnaAZzEl5%2FyvulzOHfKfyKjyreOk%2Ff7VlLVjOou1rR%2FuGRPywly7FC9u%2FkVEbtD0POtxGINziS2JcnMxsQCiRo%2Fy3xnVP10uoUD1u0k%2F7heQ%2FPHblFj1eIP6SqkmVF9O4n5rmIKScYdVP3b%2F2bIJHGfgoHxA8glaFlNk7DgbL8Ob8EvY4tgzzpImOYk%2FS8DelULou%2F3kJ51LjdtiPb06O3o%2Bjh31fz%2FbCFudPuUD4FP2PxMWAPxUQ1H6D7P920EfcSkRO9y%2FHNqe8ChLyawuaue3ggIbh%2BNGSlPQhMVax91%2BxbL0bFqe6Y5wzqHROVC1KX3%2FPPu5AUdk36NThfRJfhEFUCzCI5ZqLL%2BoMYtPcw4PUa1V6HM3e%2B9mdjgfUnbQiHnv096kaJcjgnzgVRdZ6d10u4MFrXo69zgC49nuVE27vXPABpO87p9awGF5SsqvBW5xPWXLf77IRx94Nek4DSwqW3BBAJ8h2diRjyCHoD4cCazc15SVaZPp8WnAfW0eD3ZU4Xwz%2BvLsXfRClB8mX%2FJ%2FHMnLN5wKEBujs5ygMmUS4V%2BivBjYoEUs2RvdpUjN%2FAbEm30SBvvjIjKg1%2F4Wrw7ZZM3AdRXRoxsRvAxM3wIiyMI2Fnb0GOqUBQNIXtlhQKu0je6jeF05FRthpZDmF3Rhl2hSxW2x0iJAZbOb16eO0VeyzgRvpa7JqwLqT3G%2Bh7qIj3Vj2FbKF5lSRTYNUHJV0N6OGr7WOIv7RJkhS5KI211BlsKRQLuVUa%2FtDWBE56oIBbzm8QzcwQku5GkvYFAIVnfLW%2FWSEFtl96Cp6UkoiJiEliU9qwYNMBuo3r5KceqEJPnMAp5KwaLD5OP0G&X-Amz-Signature=a4dc111315c50dfe62ff0e5b796d6e0be4f2fd4fc6213a6260e0704d7ab734ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUNL7KOW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIHzqx939Jwz5SpArjIWHoKZqFTav3clKd7HxY5XrTlp9AiBty7d1HY6xUOSYXTSOhHzIMRU9sb4UvSGdd%2Fc7UvG29CqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwfZvG4Ohufh5Op7KKtwDacUTYpnGLFrarSrvInUBORxivU4WBEoHKZ8zWxXHpbhIaXOiD1hb1BB2Mam6CqpDDwLoke%2BOtoNE5H4KvLGfOq3DmtvqHHm6yXVcTpvwfH9W3TZF9Xj6yuNFARwomgKqoV9DIYwa8fFH3F2vu5iGAuE0G%2B5XZIQ8nLpdSwiH6LpPpvSoFDJS5dGQiR4HlHBQ%2BtHYCBJVNwOJIeRUX%2FriEjGOtsHaerNazxLDfS7LC3Bqv2Uxa25ReR5q42mHMeOPLKxwTk1102tLdVgelmLbggEe0L3g256FZzV%2Bo1tftPheWLriz%2FnibMW%2BUnic3hv9Q2XfwLqrE7LukYleLwL9xycWR3Nbpmsw8F7nrIsNzK%2Bvv9ombRuJUE2ZVsXWbj5yvHSEoyaTQy9%2BxNv8YrBPaZDgfuIsxrGBoJuSumbDrnPyfmkEfEUyi%2FjBaFsMV0GY9jquT3xFbiYMg8uq5igxnrKiex%2BgcsU8PnzpY8Ojbp5pRCKb4%2BAY9sZnKu2qSA5KwjFVx0xPCl%2BmcyfyRq1bAZcOSGy209G5bojOWH8Zrx26fLaM4w%2Fw5%2Bn5A1jgJ09Y2c9pRl7SxZN6k6mdCwoeBnsdgsgSOx8F8HijUT9qxHCZ3lriQHflU3z7CYkwsoWdvQY6pgGtH7iP94omFPJSxRTkNPLJVPCTGyc0xRGo02N6KOCk%2F4%2Fj1o1ZWF2kXRF1cQ3V%2Fz79o9%2FfjFcQkWMQNHNf1njD3c%2FpfmaK9gVQIjUWvrOTiG1Hi2rzVN7MwxL9S%2BjvvxYQ3eJHz8yw39nu4yOB2CUlJEXYksICXVsCG%2FhgBQMoIq1S3VpWBTdG57juS1UgyFawK4GwtUfNuXZKgbImuUL6S1ED1crN&X-Amz-Signature=76f494e5aa07a0d75afd903192e82ae39edabe55bb38e339708f84754d7aca72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJAHYFJR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDjNTgQsINztD2DcSXf04MKYzj1pa0Xw504%2BqtiLcBqngIhAMS73KB%2BCdv4uFCTVLXf8Pud%2Bvj53CYYnVS8ZeFv1aKlKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1f0k1Wm0ki4qEt4Yq3AO0u1oOmix%2FAxLOIOxWKd5y8vhz8eqx8ErMFs1J9149qfAFfNJ%2BgDsEqAruR1FmqD2bjlXJGy6KgBdvzEkSUayNHleduZOV3tkQqZsfxL7yJ%2BlStX9Rkk%2F8qwg1YHThIoZ8jCchaJd6R4QZXkH0HIb%2BdLB1ZHfZcyLg7tPaI4RdChKSvoFaI9iX2pA9kE8g1CLxsPwlA6eAaTAVVqikLcleXOLKXb3nXNvqg%2BM6nX7MpWnfLQXbDYhJV4Wn80ALNnE1hTCjDkGTrGDsvF15azFXS%2BWX6CmQuZcmcPA7ExUbHH2nh6xTcdmvHi9uaqGmRpOOn%2FWWvyqXriSmSJEYPzruaMAQA6bQoEGCeYQlJxHj%2FGt54S4Sd6KgRT%2BEe7mQY4cvAnTSClWuGhxPO0Z9ZVNWW3btk6nKVbfb6Y0yMBIIGfbIZkQ0fvKJ00tssVzjFKM9EdQaNZ9AT5fCmQPoQ6p7I8EbEPaQXFI9LxY1xvaCKxzJzTat24UZsR4VdqIGnSWkSXqtcZmtO3fDUe%2BN1T3tF5nJuPyC9NzBFCkGAB35MAeY0jiyjB%2BBhG%2F0v76F4yXCelPca7bNdzEMoLOhjU03gKDBfxnU%2Fk3wBz9pB3Aoljozn4oVY1ophbSnXTCQhZ29BjqkATukVpYJ0yKaivqIzjYdVvhHSS4n%2BTLt66sovFM0apXLaMDnOhdd7qoUyRax9BzCbyB2VVlqbU4xrsahb8dfoebqR3WZmcucJ3aI8Z8Lld6%2BY%2FOr516gcQmCp1oO2GJ1K%2F7d1rSl1R5awFJSH18mVLGtlNQ2Unw%2FhoVUw4eXejOLTEUf3m3HJrljpqn84VBTwDmoi1vaDFgFf9wrb3vwiy9Z6vTk&X-Amz-Signature=26df89ddfe53bc073a7bf3323348df5cae2c098a983c26b05cb6bb895f8f3828&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJAHYFJR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDjNTgQsINztD2DcSXf04MKYzj1pa0Xw504%2BqtiLcBqngIhAMS73KB%2BCdv4uFCTVLXf8Pud%2Bvj53CYYnVS8ZeFv1aKlKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1f0k1Wm0ki4qEt4Yq3AO0u1oOmix%2FAxLOIOxWKd5y8vhz8eqx8ErMFs1J9149qfAFfNJ%2BgDsEqAruR1FmqD2bjlXJGy6KgBdvzEkSUayNHleduZOV3tkQqZsfxL7yJ%2BlStX9Rkk%2F8qwg1YHThIoZ8jCchaJd6R4QZXkH0HIb%2BdLB1ZHfZcyLg7tPaI4RdChKSvoFaI9iX2pA9kE8g1CLxsPwlA6eAaTAVVqikLcleXOLKXb3nXNvqg%2BM6nX7MpWnfLQXbDYhJV4Wn80ALNnE1hTCjDkGTrGDsvF15azFXS%2BWX6CmQuZcmcPA7ExUbHH2nh6xTcdmvHi9uaqGmRpOOn%2FWWvyqXriSmSJEYPzruaMAQA6bQoEGCeYQlJxHj%2FGt54S4Sd6KgRT%2BEe7mQY4cvAnTSClWuGhxPO0Z9ZVNWW3btk6nKVbfb6Y0yMBIIGfbIZkQ0fvKJ00tssVzjFKM9EdQaNZ9AT5fCmQPoQ6p7I8EbEPaQXFI9LxY1xvaCKxzJzTat24UZsR4VdqIGnSWkSXqtcZmtO3fDUe%2BN1T3tF5nJuPyC9NzBFCkGAB35MAeY0jiyjB%2BBhG%2F0v76F4yXCelPca7bNdzEMoLOhjU03gKDBfxnU%2Fk3wBz9pB3Aoljozn4oVY1ophbSnXTCQhZ29BjqkATukVpYJ0yKaivqIzjYdVvhHSS4n%2BTLt66sovFM0apXLaMDnOhdd7qoUyRax9BzCbyB2VVlqbU4xrsahb8dfoebqR3WZmcucJ3aI8Z8Lld6%2BY%2FOr516gcQmCp1oO2GJ1K%2F7d1rSl1R5awFJSH18mVLGtlNQ2Unw%2FhoVUw4eXejOLTEUf3m3HJrljpqn84VBTwDmoi1vaDFgFf9wrb3vwiy9Z6vTk&X-Amz-Signature=a2041711825dba719593110006284b9ec81a9b53bfc52b57d0947f5c5e2e0997&X-Amz-SignedHeaders=host&x-id=GetObject)
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