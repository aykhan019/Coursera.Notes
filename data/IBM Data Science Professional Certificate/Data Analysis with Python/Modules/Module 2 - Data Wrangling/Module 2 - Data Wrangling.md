

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667B3THYYH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0zK3jbWl89Fqk0iO9trrOuZopnnf%2BbAjsPvAsmRP7RQIhAPD2gcKbJKQGV1c3U0NyJ1Dx685cLXZJL5AkYGgB%2B5P3Kv8DCBcQABoMNjM3NDIzMTgzODA1IgxdBDXhbv0NuzI15qQq3ANn5Bz3ftPyxVDzzHXLrlpUry5KRKqQzuvTl7n5zSGx7DCDSAa%2Bn%2Bjt%2FrXtZJTh9JwUbYFsFnpSRI5umEHwTzn5mePjDX1QelJ06fs2gyy7Gz2qxf5WTxYgVfW4iJ0%2BgCNYlGPjAhhgC93KoU7Hnvc%2FdQSn1%2B2u%2FvZYN7SAx%2BfhKwwPKOW5oYLNd%2FWNfUx77RyVks3dYBfiLLuY94%2BBwhv0Hsd6Bvc6c1IYm2JDIyLfrz2%2Fh76MieCJJCojUlFAE2OIfnzMPyi4M1yJwszlYVf0rU0Gk%2Fj2rEBCNkcYqvPcQwhpNweCexoRIzJERJSauO8gOzV3hbDiOqyPHq3CWw6%2Bv9hKvf3v%2BpVosgl8MJydHwv7g8p0DtGCoO%2F8gqzOq4hFyM6imr5Vlpmv6iP70C%2FVZksWcGjhldRpPimBgLltdVESJ4vwk8R36A20K2fm%2FQoN15jZv4JRl6VFnLLPAyVMCV7pghh3pQy%2BuOE7iPRH31jEBUAkW9dAQXYgNvm1z%2FyboyJFZxNeocKI2rOgj4RiZeKA4P9A7K5CO1SbrxWoDrUAOP8AMPvmRqGyeGmhpWgz%2BcXhT2PH3uLBRoxuuHGgNDBBdPJdBx2A92pogEGWsLM%2BxXTjzUorJS%2FMOTCBjoO9BjqkAVZvzbfsYl4Z%2BuXmMLt4bOnPyKJWY%2FgyX0etCSDeohp9OLQROzlEKl4eFwlfnKfpj%2Bqm3HLmY%2BlTygEz1Gw85w9WGq4BOQytjQXVQi%2Bg26tcJsgVKlos%2BWOVdBNAyyikeHLu6CDHMYjSb9kMULWneU3slNBt%2BTILC646xCvOn4aAkZLMqkgVNAOIEs9iVuQHgJx8uYALGK%2FZwKcA8Opsb8umhzBg&X-Amz-Signature=8c3bd41e46a30fb3dbd01ca099a8faf3ad3f09d8ec6a6c1071c28b4cdce0d5a9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624KHYIZD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC31vzdkoImch%2F1b3kPjowqBX4K15D%2F21lNMqTfS%2BWd9QIhAM86KlZbhMCOuWINT16Vk%2BhDF%2FGlMafsJRWk6x3N6zAdKv8DCBcQABoMNjM3NDIzMTgzODA1IgwVyMmyFzFtUEHQY3wq3AMtmSQQEoqJXbskGgU8TeDiF5vsoyO2jrB5Y1b3taAoKsbiIyAj0PN97ZGa9fomcTbn9mZzg8xmciPV77ibRwR5ip4xwYpYF9m4arDFduzM7%2FigORs3%2BY9iocGJ%2BQ7%2FDtmfB8FYQpsdR4A7salP7LJr9n2gQQPCcFxHwgVTgWQIRcpKaM%2B3oQvybkNG45pDeieIfmJ9g3aOkZ6GEk%2FK9r%2F3fP4CLduuMiEEhlWmM5qrSyaLNBDORrBLLW%2BoioCaP0w8UOBw2eqaIT8KSnOZVfyi6RGIkKQnOTZlx0anagTCh%2Bbd1rRQldJg0Tmb25Aee79Y3AIvpPEpbAy0tbU5Un1PMtMJ2lcDvoA9ujjFnvfGX%2FqFAwpM58XMhtFOHFgWytquZhyhMO%2BiG2WK%2FN9JMLVEu3LEz3eJP1LyYcK0waVMvOi63%2BP7HWPS%2FKkeQ5BFvm8jud7DTq4i69zlbtM6IiqeKrnchz5Yg5EU%2FLMEhJPnEKbxAO9Prk4qm0pxHqtXiz0YvKsmixQWiXLt%2FR3iAW9TVP62VqLyF1YfrAqE8T2g5NegaXQlld9NiAgUAoFca6TaVjRRI6PExq2st%2BSfv2Xh1rabcWJZsdrfn%2B8fkmXVOgE4BN61hAcpmRhgKDDLjYO9BjqkAR6jsTpwTUfHuRiKBRqZdJ%2FonS3IFpE803kkR5xEny%2Bul799o%2FeGtFCUu%2FZiLAyRHpa2FjNMkANo6kSCgJwNpGg4dh%2FlVeC1%2F9Y5TOQfKuerga7jID3YeCn%2BODyt5NcVeIIkD4p2J4OUM8cK9lfwp4kkCismxKXkDfagMDSO96%2BIrWNWUu7PdL0C3UaPOepGbVl1gSNwxHPGsb1AGHdc21xCNqhc&X-Amz-Signature=72880b82bf147ac6c4458a493d7a91600e3217e6fd9e61c43256bb9e12af8a3b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6WVFOIV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFLSHW7or6BqBA4Foxr5%2FNTcZBgnYxhEWTbUg5YXF3FtAiEAhF3iKIjJ2xN12r%2BDvXpDt2ifDVIPci%2BEI%2By9ISAGIjoq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDAQNvGoBL2JJANyBrCrcA9Fk1IXIOTZx3Vx7EHwo9L2OF9CLqd4oGL5rYV75LKCuPMSNdrThjoMRZkq1YogYwrXn%2FdaLD%2Fp%2FGJ80BHajLCEFcOp78nreMK%2B%2BijLNp1f2DqejHPwrxRbPxCcmjzvT34aLvnz5D3TQ7xHNtS0VeSF90gE98K7Ktle2Mke6U96EDHkxSZKbAu4cIHrN7khOw0wyJZP9QLWKtgtn5eDfETGQPneOP5TUeEmIOqHnI1z7EXOO%2FFOGNDa5XowM5o%2B1iKi3Pwg6Ao2RpnHywLfDavp3OlfmcvSyRS5VYrtuf7FqT7fE1K%2B8dRnl6h77ysWnY8pGXlk5LCmqO1%2BK61TUSDm2K4KekzO28EPl0nxW7vEZa%2FQMcMrt4yfUNlCPqc7VsAaQIi5niGlat12Bky1gXt3REdPUtX4ScDUKwmbJVZisoFkCtuCdUzyDGBsRyaay61kBKtS%2Bmmg2kVLTOLCi%2FF3SloLts1dTQChFbfCqRMz0xyk0Pbmm6MUIN5t8oQpB1Y2cVLSK1BOtOAgLBxHcQJUfMnN0ksLw%2B7M2k0jpxlYhCgNuTfT7gI3CI8QR5fXqd1nvrXvBVBesHmiZ2YZ%2FKZfJLND7JaPE%2BPY1bQ5un3ueX8M8xgoy4KUNfYbhMLKNg70GOqUBub7OBpRgYdKV0h9ixsr6jWZuLmab2uTZcvT1Eepj5UfyUQJtEqIKKE9uFhAPFjmM11MN3HJQSJ7bGcMxrv2hY%2FUzyYCEj8RCjWd3Znv%2FmKWWRN7RNAdkdU9UKeM%2BVjKtiuVjKlapY%2FPTu0lpcDI63Uq4u1vpYJ5D7%2Bttcgefsw1QVtl9oEvPsuGtzqyRZsC5c3Ve20QGjXa%2FSkiiTJ3FSjexwfZW&X-Amz-Signature=f74ff5fc604e2bb879f9b05d732e10bc868e6920918212a8de5003914318d920&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2VFASFN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET9I4q%2BQoyBFN%2Fchshd1tC1JwUrNbSgA2TrYKfrUvWrAiAHRJ%2BobqJddCBvLNrp8ye%2FMrq7KoHnYvPIxWY%2FmUWd6Sr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMAItu4EEdNOvwIYieKtwD5fSQ6DnBXv4ivXUJsruAi7aNMIc493BZvgChE7RAzGBgJZTSm6s080q022Xw%2F7PIFmIKy7TjXdaYor%2ByPD3aA3%2B8T0lqhOw4mpvSLdqKjN1H9kr8BsyGyfcEsBrlta%2BkgL6DjWS2XvCLW1LMLkBXyYdbc5pGFG%2FFCBqia005IE7eWqjaLlBDpVVoj8h6HN7svUtKxpIV1%2BmTpbkgRV1VE4kriG4ldqUB%2FAn%2FEuAaFH0RsLOPoKD5fLWS0RFHpZeYhz6SHgKqvRW9t4GGOdGAEZgAbnhi4T1NB2ln3mSa0xAYw8xvKUvLKtXVG4ZVHrgZrVJAC4TKR49QiRoR7RCU05W2cwLcaLOOKppeH%2BE2aE6Qzu7YZVuAUcRNQzkX1WA1RRJjP0B1Owkxn5x5Rmfgm6HwYfcMw2%2BSETbGFSXA7g4Xr%2F8cM%2F4BFFd13B6STJk8bxMHyLAY2BoNNhORwhfQfyTbP1cKpLoWOsK2KrSHmTkYbX7eUPH%2BKmX8AjBx1FxBeQcIuC9m2g2rSA6I1WqkjPBbam2eUuMCBXR8vgrkhX1EsD4owAbUp%2Fodqvfdp1tleCZ6ZOZYpMVQhE3K7GVY3waOGlOMN2SsVeYKO8ZFPGK27X%2BN%2FdtfF5UF1scw9o2DvQY6pgFzjLwACSCWAlM2BgsGWpIVwqD0L5CZK5w%2Bq4UD0Jb%2FYge%2B%2BH2nJBN3DxHZfULU4A0kILH4rxA1EjGo2rnd01qOW8QIqsntjeXsYX2KmNK9v1ZMSlHnEC1m%2BWOVBLjmX5b32xqxpr%2BiH6ds8CJQ7sv0dEAzmQV1%2FoVxS9dPLI%2BGuSdIfz9hZGxk9KsS64%2BrlOhE%2FN304yMZT8djXDkkhiGlgKgePOWo&X-Amz-Signature=10cd0883b9309bb648d4f37679b463002e17d6bca42188da1298fd0df1b41bb0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3SG5DSU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGtVXOn6QNwCl3cmlyqPm929dgJSz7yJVHhTUjj8oo3AIhAKYrV2NsOMgrRnUfOmN4GSX14uhob9wB01S78LfyqK5VKv8DCBcQABoMNjM3NDIzMTgzODA1Igy83tPxISWvsPLLMAcq3APNBRDF2xZDcwwS%2FgkerhICxlKdX%2FHxt4LsdT6TPapCkfzLJr9c2tjbTGEn1NOY6wa0r%2FT1SZWx1jwd8bVrXqON0vn0uIrTk9XJHAdFj%2FbfHl6zdPg4oAca91%2F3jEsnWDrGDN6kIpjfTBPt4VErLIKqHBh391oPFS7n1bAeHtDNZ4hhOI0N1j7Wz6ypAz3%2BH9%2BkQNk63oGy%2BA27WypEr3hge1w7%2B4RYoSpih3pHt8Yd8fPWcG0hDN3Qq1sKfM5WNdiIJ2FBhsCakE8j6XE3kh5qC8zfy0jk6FUQHPz1bTlCp4WBVOPnfGdz8S7KeUIBubmu9CD5OxqO%2BAOP6JMPnsGa%2F9Wjh0%2FQjXDxDtmGR93XfNHWakydkQ4NxEKgNtE4fDzd4DObHRtj%2Ff6tpsCUiLvBf35y5BbvNTSxr5euiNnVQ1a6hg0p8KB8czQWg9rRkbJr72n1SEkWkJJc7V275DMAZyzvtQITA0qAUwGKiOXHcSZJi2z%2F0vhQK3PJV3xkLcnbMtb76Qe2GY4BXWntqejknHUIspupD0ioaie%2FnEiLDJYZoRWFX5XX4r0kb7DdAgNygiU9HvJzegDFYETJYG9bx96iRVFk7UzlNyct%2BS3wcC%2BE5EvL5a%2Bsz709%2FDDIjYO9BjqkAdiO7JcbHHlxPkeBNIie%2Fq4Z4bCrsCERemgRG6LOb%2F3VxK5ujJsr22%2BXo55eGThnPJQrfHEUQ5ogwYM6GNgi%2BHIMoDmDHVQcQiFosdRZ6CnfjCXNHwFB6v5OJkJ2j1IjLIsj2rSsxcm%2BLMrt38CcEOFrqDbGfNbJ2v4qjiIMO%2ByAEMCDKOt4R30dnQaq9PBC5%2Bh8d1vmJvUhazE58h3%2BT5cc5fMN&X-Amz-Signature=d8f3c3832ae00fb2bcaa992cc63e0fd09a1c7e727655db2faed499dd5247767d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T46EY7UL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVzFE7h1%2Bthcgvhyrm2FaFgf0%2F019ezB8g1XPWLpqrCgIhAOnoJt3C%2FpsGhUYKObKtN5lERi7QTiziyTxBhidbgt5GKv8DCBcQABoMNjM3NDIzMTgzODA1IgxsIBmpuaBPdyqL%2FMEq3AOLcz2pyWE3mMA%2FEvkA%2BMvlYHMm9jfN75uzaJ7rznwFNzYVvzNstNYG9u%2BI5Z6t64tSFdQt5iuwMrH8ZmzUVI1U0flXz4gZLrCnvJGB%2FueGk1nXseYRlYqVs25qXzfY2WqyhaOIS0lJ7wuQh3WL67ZZ3pZ1YKk0rTebgLmAfwI85NzN0NuTxxEU8MbmiqeDz7Euk28Ejzq8IQV%2B9h5B%2Bns372vEhpeWEplg2BvwH2aabiIdQlZ7%2FK8k70ptkHEjmGwt4tTuhbYRgoyFrK0UmDWAHRsfD7PBbuuH7ExCiI%2BA7epjZs1v%2BxO3v2DyRyad%2FD2W6pOq0%2FKagrU7lItUjHIPl527uCPYOnlKdVBrtyzR95YFta7fnhDng4vt0W5kw7ND9u%2FTyr0xdr0juqMtEyXU95%2BZ0z6azzv2L8WcC4Zbe5EY5BFwVglJlrZIGpQnQQSZp2lOnttyGwj9EtepT0vMUGWhGJBdaNFM9W7tw7fQUdC%2FNUbV0OWP%2BFjydioHwD%2FZBbt5TQo4O%2Bml5K1EDmodrlH2xoFIiDiuHOfP54KhZIXnXyAzPVGGZhZvKoiU3Ttnb6PncAxY4wpBuyfS6oZELc8%2BzfZowkHZH6KuepdquoETH7DUs1w6Mp1kQTDcjYO9BjqkAS68Evlyj4qtnPltGOuUirv7kSykBaJm%2Fx6fAo6chynfRwHk1rciL00bobtjqFqdG7yYrGj14Jn%2B0Rr0k2oHkQyDKPT8CH7UanR2q1Dz0zhHdfKupQyw1DBtmUj%2BvSbZ4NESLG%2Fs%2BxYcWabIZq%2B49jzHdqPeTdlNAuShefk%2FQ2YjoZaRYcEIgpzr5tU9v1hrg2DWYaKUGpAvhaaZNkdf13iRx1Nz&X-Amz-Signature=29913ec89838205f51eba5831ef77b4c3c418757ce4526913622574274bc3980&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GVPGK7S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ4XQ8BM67gr0HZPKyyk80SmFTZoOqBSU2doD89wZ4fAIhAMQaPcZfb%2BdsOo4cdrKbF0GddAsqYfHSD7rBYbCn5fE6Kv8DCBcQABoMNjM3NDIzMTgzODA1Igy7gkI9IqCghiVbF0wq3APDAtOMgQ65tv8ig%2FpyfVkzYoOYg8PYGqOQ3Nzhw19ul8ry9Ljp1piPujGWtpPYkHA9%2F98TrFAK%2B4%2FfrP%2BxTTX5YR3Sx6fioX4v1QeXlCbC52ruVdoT7lQEDnZKLktVIjtSxXb7naZbaVajqVgbFWiMcHsHnOIBMWcqC1JrKzpu6ciy6%2B3F0oVjTD7o4hwxcD3%2BUYqVEzndFrZT7h%2FgH%2Bfz1asDcMphFv%2B80MgXU%2B6J8Fuh58XDK1i313dDi5iRuoNEpJZ7n9bV5uGRFPI%2BDGg22Lkrdy5o6gZLi%2FPk8Dhk0AiyeQuzhsm8I32L3oZP%2FiLRqLGMMb%2FPXmOis3elIctxaIEGT%2BGMHra7Rr7QUyL5kXbYYVMmzKAkgOKhfFh2FNf4mKIOnoRfORk5VG1CoqNu64tIpO9poBJ81esZ%2FUwD6uGOHOohUx5bM1HV3P%2B24XswCzUJ6C0QIyTEITgc5E%2FhMNljoy81Mn%2BGcSIhbUHAHQ8famq%2FktyNyQGBEjTdt3Qyitj8RcNPAtNgsa0QLWWYhOvXo%2Fi%2FBA%2BtNPwQ4rFelK7LsweDgx7GFm9xFTntDTGIsYX9WUMczrz3sUvScl1qrFJFY3a880bOEXCj8lthvUd%2FEPpZyMzRjz2kMjCjjoO9BjqkAaEcXfaUmKQevQ2ErBZdN0X1vRSMIaIshL1AMyWmhlWLqz6Mu13%2F3AFIxjqkSxhGArgYlWwwstj6Z8xNtj6%2FA%2B4dBiS08P0uN0P%2B3xcHlAdUk3%2BsJOhGUiAruZ0EwomR6FuJ0qeAkoHurnqm%2Feqi47NFOOJ39aPwgyeU2EGDXAqIAJdEXUaSeCw5YpRp0TPwPctRpaKvAJUi8Tqb9jyjHmoCHVGe&X-Amz-Signature=328e75d9331b57136c0e4bfa50f279ab96eb0885d582b4c474dc553e0bd56732&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBCZQXSS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICa8MEq9TT%2B3%2F3hjH9G3bzsohNwc2kxuhFE6gF2pQxpLAiEAn7qo87HERB7z6XAS5PfVg%2BPqsD5TX%2BTHIvX5uSTqYeUq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDC3wM0rMQiPvcFwbPyrcAxRR3QfSkcoq6Dbiin2Mj90zkfwJP6qXFWKww0%2BH0dDs%2BRiv8JaD%2FZVFML4geKFEYiM7cZjviFY%2BnjXSN5ejw7q%2BL3%2Fc32fbNa0zg8ECMQfaosNp0h5oLASzQn9k4NaYyVOzNTvVzrVk3%2B2EVUnnwGLet7X98tEVg9ngnjiXjyiPz%2BJkWLJQJUI4x2uo%2BEutq3Zwfmm90p1hpAgc7QOBGqEFKZC55wWMtMjI46z9%2F1Hbw5j3EZi1GKia01N%2Fyll2Ecvi%2F8Nf0ZnhSLGdFZImO3pBcfxfjO49NtWILinxnJevn9GNfq8716j33jQTF0AfHKFvuMJoVnJ4TwKhe3huxMvdpTDgpLPwXRibAjtvaQsQoGRyGFFWSxhcfrwSdKgFiHyxJEB6IYdXVsfJRh9iRrypTgCPj5I7DeAzHiKpxQNZKqLO8kdzXmhxO%2F0Ts96pvJ%2Fob4Tzs1xCMlCfiLwL5Eaydd0RxxBlXcfrLB2ngkq7FVtW2mcLK%2BZkFPdLcEdwBplpvEPsWN%2BZZQ%2Fht%2BLbIhRCoyWOpZex%2BUgxVPKy6H6Zy7oYxwSvsvAXz3mL6%2B5E3UfV8hT5qOI0VvuK1RJCtU%2BrlCI3QIF1Sbnh5TwWTmd%2Fx8yM%2FOsdUmpIt0t9MISOg70GOqUBG4GE3tkQdmXhpwmPRM7jyJ9Q8XyEH7d6S45EhkGubCNYrW5jJlJEdK92DzZsvEe1NAhin1%2FSbUUQz9BnqaaeqGGoZKXNxsln8em9JhYfkbgXwMASot3GuMGk90YIwUjCDJ%2BXyqNHk5J%2BJlgis18Q%2F78jxR4ckQSuXJAUawNQhMMfKL4C0UhYYkiU9W7%2BEdmf328lUwssvaXbNRI847AAxREUyAfO&X-Amz-Signature=34fd3559b1943a9a7dd6eea4af3a81e5e8f59efc8b7c4e7f3f166955e096939d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3SG5DSU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGtVXOn6QNwCl3cmlyqPm929dgJSz7yJVHhTUjj8oo3AIhAKYrV2NsOMgrRnUfOmN4GSX14uhob9wB01S78LfyqK5VKv8DCBcQABoMNjM3NDIzMTgzODA1Igy83tPxISWvsPLLMAcq3APNBRDF2xZDcwwS%2FgkerhICxlKdX%2FHxt4LsdT6TPapCkfzLJr9c2tjbTGEn1NOY6wa0r%2FT1SZWx1jwd8bVrXqON0vn0uIrTk9XJHAdFj%2FbfHl6zdPg4oAca91%2F3jEsnWDrGDN6kIpjfTBPt4VErLIKqHBh391oPFS7n1bAeHtDNZ4hhOI0N1j7Wz6ypAz3%2BH9%2BkQNk63oGy%2BA27WypEr3hge1w7%2B4RYoSpih3pHt8Yd8fPWcG0hDN3Qq1sKfM5WNdiIJ2FBhsCakE8j6XE3kh5qC8zfy0jk6FUQHPz1bTlCp4WBVOPnfGdz8S7KeUIBubmu9CD5OxqO%2BAOP6JMPnsGa%2F9Wjh0%2FQjXDxDtmGR93XfNHWakydkQ4NxEKgNtE4fDzd4DObHRtj%2Ff6tpsCUiLvBf35y5BbvNTSxr5euiNnVQ1a6hg0p8KB8czQWg9rRkbJr72n1SEkWkJJc7V275DMAZyzvtQITA0qAUwGKiOXHcSZJi2z%2F0vhQK3PJV3xkLcnbMtb76Qe2GY4BXWntqejknHUIspupD0ioaie%2FnEiLDJYZoRWFX5XX4r0kb7DdAgNygiU9HvJzegDFYETJYG9bx96iRVFk7UzlNyct%2BS3wcC%2BE5EvL5a%2Bsz709%2FDDIjYO9BjqkAdiO7JcbHHlxPkeBNIie%2Fq4Z4bCrsCERemgRG6LOb%2F3VxK5ujJsr22%2BXo55eGThnPJQrfHEUQ5ogwYM6GNgi%2BHIMoDmDHVQcQiFosdRZ6CnfjCXNHwFB6v5OJkJ2j1IjLIsj2rSsxcm%2BLMrt38CcEOFrqDbGfNbJ2v4qjiIMO%2ByAEMCDKOt4R30dnQaq9PBC5%2Bh8d1vmJvUhazE58h3%2BT5cc5fMN&X-Amz-Signature=7d6d101ac474df8d50ab0d9ee5fc89faa689176b12447cfa424957b5d10df65a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPOM7W55%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOKJGeayzx%2B3W8eyHTB5l%2ByAm0P7QBsKtlNLjqwm99fAiA%2FqZXELlVPcrZePaE6Oht0YlwZQFsnRpn0FKizBQbVzir%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIM%2FXkx0qR7COyZ7Ru6KtwDTiwpwp8APa0HLRNj0qAR4W1mNURIAuMjqAGNyewf3msNsJzYznuOOHjeMrweuGoPc2r9bW24IU%2BO16q%2FEcnQyoWOKJO3YsCtc3FLOp0VQyvN9ISnUSrk25zpw%2FuEpSg7ocyiWSb8y722GTdH%2BfpCYwBQ%2Bu1F1vUWnP3E2shfqltCpltO9lG07s5t6TYMSRIeidw7H7QVSZhJrQIdRRNzCJ%2Bx3f6CR%2FRycxtEUBRjzHzPknp0zMI%2BUv3R29EtWpavELjExV4CmCFMKemHWYCETGvby1Ma1l6PLPfYVN6e%2FmW0lmkHq4P2wUCWPFNajX9DhIs1dnf8mgevmhTllNaocElbDZ3FlLpvGE7EieGmvmZzXgqB1uUS8JuLVVXavku63%2BGFEINQBL0Z%2F%2BjzkfuAhgS4ZcGj3CXMuymFlB1KqaSyXrj3HTl%2F7Hgxn9GoHDl%2BxotEZ4vHJgXYgSk1ZBqDixXlb%2FBbOTXtJfQUrKLzPdF4SMD4LoKHXp8SWtzvglnzQI8RfCjUf%2Fq9cSPpenSVv10cfndnLBiU%2BV8zdcl0R%2Fb6cKsBBljVo%2BJEdPvuYaJ78NP0d51X722C0aPfSt9WEuz3wWY7VbH0GKYHSUHnMFqWAcxF3QGWUi3E%2BQMwyY2DvQY6pgE0ZKcgC6sa6KVezoJeJX0BYt68vN%2FcTQ3kiPwS82HtFLrE43G4%2FKcogY5935hAYShRKcwjdNQCpNqIboSfadu9BBdX5rV%2Fp6UrXqnfUesfnNWGnNnLZ4F5hX%2FPcackRcIpjG02nQW9Yd3lYsv7NxJHJWptoO1yLeiO60Nz5hCQ6auIMnIUAbKO6ILw4GA3lc7OQe3Yaa7N8gRBhqVDsYBYNAKALx9I&X-Amz-Signature=6cf902b920d0e55ba0c6b83bef28e5e5dce20748eb06841e630a883a4f02dfbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPOM7W55%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOKJGeayzx%2B3W8eyHTB5l%2ByAm0P7QBsKtlNLjqwm99fAiA%2FqZXELlVPcrZePaE6Oht0YlwZQFsnRpn0FKizBQbVzir%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIM%2FXkx0qR7COyZ7Ru6KtwDTiwpwp8APa0HLRNj0qAR4W1mNURIAuMjqAGNyewf3msNsJzYznuOOHjeMrweuGoPc2r9bW24IU%2BO16q%2FEcnQyoWOKJO3YsCtc3FLOp0VQyvN9ISnUSrk25zpw%2FuEpSg7ocyiWSb8y722GTdH%2BfpCYwBQ%2Bu1F1vUWnP3E2shfqltCpltO9lG07s5t6TYMSRIeidw7H7QVSZhJrQIdRRNzCJ%2Bx3f6CR%2FRycxtEUBRjzHzPknp0zMI%2BUv3R29EtWpavELjExV4CmCFMKemHWYCETGvby1Ma1l6PLPfYVN6e%2FmW0lmkHq4P2wUCWPFNajX9DhIs1dnf8mgevmhTllNaocElbDZ3FlLpvGE7EieGmvmZzXgqB1uUS8JuLVVXavku63%2BGFEINQBL0Z%2F%2BjzkfuAhgS4ZcGj3CXMuymFlB1KqaSyXrj3HTl%2F7Hgxn9GoHDl%2BxotEZ4vHJgXYgSk1ZBqDixXlb%2FBbOTXtJfQUrKLzPdF4SMD4LoKHXp8SWtzvglnzQI8RfCjUf%2Fq9cSPpenSVv10cfndnLBiU%2BV8zdcl0R%2Fb6cKsBBljVo%2BJEdPvuYaJ78NP0d51X722C0aPfSt9WEuz3wWY7VbH0GKYHSUHnMFqWAcxF3QGWUi3E%2BQMwyY2DvQY6pgE0ZKcgC6sa6KVezoJeJX0BYt68vN%2FcTQ3kiPwS82HtFLrE43G4%2FKcogY5935hAYShRKcwjdNQCpNqIboSfadu9BBdX5rV%2Fp6UrXqnfUesfnNWGnNnLZ4F5hX%2FPcackRcIpjG02nQW9Yd3lYsv7NxJHJWptoO1yLeiO60Nz5hCQ6auIMnIUAbKO6ILw4GA3lc7OQe3Yaa7N8gRBhqVDsYBYNAKALx9I&X-Amz-Signature=2cdaca51281e8b1ebf3ca97d6cdc0f46bb3efbefba19f092f19ee521f114b8e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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