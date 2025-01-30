

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLEN3YHK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGjn7ljOd2J1XQ2IqZvFE9cgvOeEciA9nWmtFieitcebAiB7RNU15E2R1amIPKwkblTvkrnWXxxjnVIl5ufgIyYZ7SqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaL%2FQnGEmZ3iVEMrKKtwDEpkRaJsZOJga7Mjk8FqG3JlGDKSR8A5RBigyGVteQzO6y2WTddx45mpPb%2B0kwMiFZRavR8gp%2F%2FAiNnFCmEVSkpKejGkTHL0u1FKvixBhzspKHXGVRyYSv20Hks3InaIBXO%2BjW958BkyIQaDukBHfIqZvAuT%2B46UxAwMHxWtHQGOVPPPo09TajM5UYlGYl7V6m97ktQYu%2B82fRDV0wQOoYJOc9%2FE4CigBTL8ILquhV1MyR2g7N3OpuZbsieVaGYbZxr5OEHvtdWi1JQkKW%2FO0Irskl7iaQ7stcnw4EOnZzcbhPLPO9rZ9rO5F9EgXIOSjCXDXFkyKXPb2ae%2BMwJo8Mt0FoP4Pzaj%2FOMITw1lY8thpwLBNL0l%2F5NsY3gKv%2BWvUkPvr9uXrljDsN1Owx3YidmKwc3sT1TrY0Lprl539j4a8e8ByFTuzApu870lgcCRpP3RXupeHdsqonMzyUsiaVBz6Rpdpz91XfeC7FtqariW1ZWfNFZYo%2Bd1F5i34LGSDF672U0sI8RoU%2BZdx5eL4r493rhLw9JroMTBUYMzTl4Q5n64nkqi%2FztfJF4ilvW3twZKqFAebxt44KwzSGPAaQRHcq06jwLwMti0gsn6UNXapdcGVq04f4x1LAcYwy8XvvAY6pgFVm5hI%2FRje7uyiRwplcvbrvH9njgTALnshV6zm9Ayv%2BdGSWrx3HhOferye%2Fb%2BFx9tv9CfDDh%2B1cVwY2GtiULcIcjZmb8cEWm4Ueae6e%2FNYE5R2ADRCfPlzqXmmI%2FsDLlR4rOddSfWFUsMNzRaFM3Kglbr1L34nZllt55jV9fzkqksr0B5ui1pfq0jZU1hOxrYzbcPX3oGc1POfVNTS42s1RRK5Tdn1&X-Amz-Signature=2e349be3b139e172c665bcd7743b84be75c4dc018576aacbb7854c81dee92501&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OYLMST3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDSSC1teL2%2F%2BMhRc6bB92my%2FWM0MMNJFtfJzbHhqEAgGQIhAPCSzykCgeFWmtZniv0%2BEpSucytwlF6J0UuOwWPlVjlCKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyyNY11aEfIuSyW7dQq3APOpvDNjaqFo8Vmi9OAtjJzP7ypc4m3281UkXmkPDuwd4Lk918Ancq6DXsBysYE0nSeeZ7PqTG0oYac9Gi9vKHjxh%2BCbLMesL5abfDpvO7ZFcOhRMC1sPPOtpc%2BDP1QM0G1wZhE7X21wVAd8qVhPMZdFVdhXJuLuHBlsoZvRP87nv4bwbxPf99eCKATrNmevudsrEp%2FFqg2jbRJDtULfOh4BV%2BCMLYYOaevWWJ6fmNnvIGvZPPM%2BTnL%2Bl%2FNuor9eWqAbp1%2B%2BFve5d%2FrPxs%2BIZGJj9YwPJ8t5744egHZE41qCT6noRD9ADnMMuQnnB9BaGMKLLDVf94Rp2IQAHApIq5KddtL2DY3L8TA9PEKSEwSHtGnMclu3XTbu9ElPf%2FwZZc9x6i5eDMfH7IBDppd1iXGPucqWs4e60PgYh9tSii0q9KyT41TXbGsNyl6Mn1xBTO5aoTmMo3E5a0R66zeBl3riEbNW7OSloAwcgR4eEIKxA5%2BxeKvJ5YNgHoxaVAjdEDetOvSiOXJIwzyjXCdy1tRMdLJVoZ%2FL5YiJpMU96g0WKAPSSghLdulKaqNyXWmst9VCQWOOwXpT0tVc4UCPXBaT3o1OlhaiyZkjGq054noUqw5y8fESz9%2FRMHGmTCCxu%2B8BjqkAfFL7wkSDXIc79Ggebq5Pi9CDD0mZcrdypWhpJtHS2N5SlRREiUPQwzs2gjiyycx1t%2F89tDc6yuzUYwfiE6UkHNF8rYaj92nGf716oOWQiQzGsQ%2FKazZd%2FHK31xqLZP9vsNYkgV%2FStNz50sTjdg%2B6bB4PCEBUgi%2FmDxtdut3kmZwHvUXM3ldz2uIeqJj8pKZxSAif3totDFVBZZqrxXHuu%2F21%2BdZ&X-Amz-Signature=8ab3e1fce3b6e7e34aa88f5faf4e0a6e60ba87c35742aa874133acbbac045791&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REOUWQ6T%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICqQNvAaGI0lf%2BLry2uWsusr0YXtKq2%2FOmeH69hc608HAiEA2IAyKW%2FoHFUrZ1qnZvAd0TA5Wx4pCizWaEvkbpy1piMqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCV4KNdfQR58CgN%2BwCrcA1OriIAqufotGS5kNDqAt9Ofaad8SOjWjqiZ6Cr%2FIDlS8c0W54FSwj6lSKcQQySjt%2FDybU3NfEghYMRsxArpomj%2FEKtmE4Qbuq9isXHvFJ1wp5n%2FZQt9%2FeL0Mp1RFySht0UhFaI7lSXnAew6MG9k7AqU0GRNyXQgwj2iG58kJ8iW7IUQACjk28cP2YtlUMRe%2FiefTji9BDDm%2Bzq%2B9owDGsVoHIsk0qGxQwNu0xFNVzXLhTI2iIZvfQlh%2B5LxDAlTrdr5qlENJYWBVBOx4NnKMcGWnKg%2Fzs6SP1xvvt6qeY9%2FSDYvgVfhqmEWGpDBGHeMshpMwOWbNgjrNsyv3FzwzHbytyHmlec2Wd%2FimW1emmRkJnigNSiD8DOU7zRftEqXI%2FmG2GL0z2r4quYIr4%2FtGPqCQq3xjyOv6ugsXxsVqH4Th05fpRryXqy00T3KMJbTqfUf0bcscde60%2B4NbvGAYXJZ9K4bDiMKvDdnPp2GKTQw1wcxWU1epu3YRGeGWMt2NrKpe0dUMvKSFcpVgT5ksd0BePiX934KqaepPz0v7X2oW27fvJmU6Rvna%2BxFM2ZbH760yGElZdE3RR8eim97xL%2B%2FxA8qXYyW4jmL5TmO37aM6E85%2FC9NhDlj9kS1MJDF77wGOqUBIqp8tF2l6jB2b%2Bx7%2BBCcx8STFccqKmmWuzc3CXJtQ199w9%2BFAF8hRaUxhXhOD1p6TZb8cqFjmkb6p4J%2BQT9HDpTcgZE5LqP8YcoupithYUFfT7sE9oHIsLQMeWEbxdRDPSpnXwscc1fgwzCi9viPisY%2FHGBX91%2FeA2D1ZuOmf2IVl3c2%2BUrvjTjYNjELLalanCGhBJtqC6wfkaUvicYsfT8iLVzA&X-Amz-Signature=409bbcf7c29829f18325181642fc87062b2abcf2ae24ad3aaf440329d83a22f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTBBMALZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDesDEVv6CaNDjpcGTdO3rz%2BYgprU7rKGy%2FRaIuFeS5EQIgPNSNcFIVRYpkJuE4NRqifw6N6owOFRPD1z4fPoIOGLMqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMD7qE0HAZ61ogZPSrcA%2B2srspnnOUeB3X%2FFe0X2DH5pXfWMLAt4uLgxIbIZOVZcWv82RJmk8SwjmgXPIHBT%2BCMln0ojpR2MUyWeeD4jVhvB8a%2B6zkwfJw6pDQGJNw%2Fs9QFdDHaMakYSxxLVEJ8xIEn7x%2B9cj4G%2Bb8p8p%2B5kzJQlGkI9I7hep9uvGZEYXAqwEgBN9%2FRXXhrriDzVSnHyZdocceFO%2FJFbOmwbBkmCEdvi%2BfBhY0w%2FLOO2BAHLDKIniOBcEJ%2Bg19HQMnir37WRu5NpphJ6cF9r04SKlXFHcg92nP6PD3l3k8ao3d8cE94S4r3udwSvMS3nxeNpiAAYdP%2FoYJ7GhN6OB3Qo8%2FcuW23DM%2BaNhJEpZCjdPgVFITJpM%2F0gT6irS6yCz1zb3OLoJmCj82vdYi%2BpgMzKUSlZL6pjluAiZ09CjwJ%2FtSaXjeTqQn2sEVoJ33pHVYuOs%2FMDUPfMj8l%2FVFt3cICjmFh1quJhTBomMJGDEa4DqfqxL5GRlsdSvsS%2BpVIbWFikOkG4g40QGEi6W3vwK9gYV3uPhM%2BvxohQS4RsdDC8PqkdpVdC7UU%2FlPue1nW4O5auYGZf4zotESix%2BGwHP9RUriklLXUcK0ba7%2FDE%2FqhxQpSe4mnGf6Am43Qlb8B9UIqMNvF77wGOqUBVZt1TouWVJPfW4n0DOEv6Of0IuoWtXSy5RVg0DUGe%2FOsS1no3nzz18onGyBnz2%2FATgoBYFeUx8L0zsuF6XWRTlpuyhdrTd5Z8jinqEfs4iQ7Otwx%2BNp49pKIyzbqHaTgikrez%2FpMa5jmkphoGQSO9ojjN%2BWGwrjHIec4181hYN7xZwck8vynnZP9i2udVOKgw9psCy0f3uj%2BNj9rNbo15uTxXmfT&X-Amz-Signature=757bc65010d2b33b058f9cc8e9d60af5a47998fd71f9c3573fc46e0fb4065ac3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WSISJDQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFdKTUMhFCJ0%2B8kjgQjZl1HBRXUXMNH%2FuOJcTGzFstdUAiEAmRoGemUR0UvtbS9H4BIcQus%2FCJi3KNgtfyCGHuQuToYqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIuikbcIdNiblge%2FwCrcA6GETYKZd53ZW7nv%2Bf2aUrmjxn1RNUd%2B5Azhq4Qa%2BpOVF4vwaRJ40Hucjn55fK9RSkvsdUz6xWolKZDw8%2Bq7V8UDkUpy0Src0uJFvJKTMawVWFWtRalmTD3xhNkeUiRhCK7t4sUpoh568sNlsB3edIIYU6XqmcNP%2BxLGIH79wXQgTDVmnqnbuqEOMEsXovEfLm2rIhDjf2Mx9SifB8n5a4mphcrAeyu0BmrgIoNUlePr2JCbJGe9nDSuhQS3PtXs%2FnnUeRKMy5pwvTDfCm1UtzKo0EXhdCWvVkQ0EHFtbtujcVl2b%2FMiqiMhYsWnvSRBrAhJ8pM%2BhbcygY%2F8rfxM7J1PC5kNfS7vqgzV%2B95IpIpuUNjvtLvJiaDH6%2Boklc5m1IbsZ3iAuI2NggrYdbpvcO4JPltlCn1ix8F9k%2Bw0oudbtQM8w1xHsTIEaAyPDoOWHCzyMaUzc6OZR5vLSuJcVN0SAALNCVq3VtuGvR%2FARXVOd2EYXb3c%2BuQujZbiETyu%2BEwZj0%2BxqODH41dYp%2Fn5wvZ%2BhMB6%2BDy3vtYP2VGPnsvPddQ1pkWcb2xaq4gwdE6aAn0c2u5nMANYP%2FKVmLHXoZMroCMIMLtT4S11CSFrJhvOuvO7LCU2EkHn1ftbMJPF77wGOqUBT23D4fSZNY4zZHI5P06GISElzGCFz5FWzylMxkt%2BE28XZy9%2BG6hK7gg8nafEjWxa0br1Zeh2ipsXbv0%2FQMR%2FxBi8NDoVn2ThuhycNC90WSTDe06ZNvv8k0s%2FipyKhgc4mWeqC3VbkfwqMVe1hwpnc3QyPbtrlkBzFXr4KYIGy%2FPCBGYqDHh9AKyQE67JTnopMNHHeUq%2FTPcCB%2FhHbKDpGbiVYhaC&X-Amz-Signature=42056a003bb9380e8dc6c218449ba1283cc4efb3eebb619f0193e24c5835fec1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C5OE32X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAMraYe8IdQClimF%2Bal%2FlLpRFjAJMXAeDeiFuP%2BVPRV%2BAiBGB19JgCVpG5pRYNtVaZ2W9IsEpYEliPqFkhHX5eU%2ByyqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Buiwnq3nlqpmKt1FKtwDSAOBOGqmjBJMVzaodbw37tdTNDtQyHAhmvvQ6OxpbJ%2FL0OF%2FjzLr0eeH70T9SfrsZgEqsgLQ65ewEM1xQmuSmBYcPNRZQjX1HHMXNcShIwWAhaU6RE0V6yoCb8kZ6eto%2ByXe3hgZkAnlw%2F%2FBxRB8jOogEb1J4gNqgvlIojN0pXzfibXGRr7PhfrFvnW%2Fgftsb7ib6sWxLIWBCbzVPbyof44sI277jFiz8Z%2B%2FvUNCJ9AvbLkBADYYOAHHJ5qHSYaW6IDTY8JeAkEBDqaJCy4p0%2BKxf33%2BSTXx8B7e57wREZp3rfb4YrYdCMiTwLPPWEFgxRKfCoBNYBRjmcL%2F6ur5fugxRAOzBVXiy9HHFVVZUfP3%2BELxUweMNSsYcEXSzm%2FUkzhP5f4XyJBRXAZEr9ju3USpFsz9VvzVZ7wRO1Y8%2BpDaQQX8Nz%2F6AVfbCN28jzDMGruqmjGi7WGYhx6JBwH8FfmoGhIEW7AqibtgPxIAhdmfkd1Y0COQHsAmsRSjiKCFgO%2BNLiJsgdAiSoy1AREoPk6da6Aw%2Bj%2F7immD15oeo7da1VYAdxmN4r2qDpKL84CdKq77D8eazgj7NbcpX2SVzdqG8b6pgaKMwsOho4smhLXlfHwqtVpZBzs8lWEwysXvvAY6pgGV4x1XqYVxTpiiTImdJr6NLI%2BdHesOdTeSJ2cT9vbiDlAYAwK%2F14BZEBuOuNN%2BqGYf6SCfrEznEmhirmOcNxsQB2DBnC2wwjLA4zMDRrJ6Ah8ED1bVz7yYnrzsA4iQzfKyMKUK47KJQpkGcfanVTXgjPFtg%2FVJf8NodVZ4SDVbx2Ymt43NK1mE%2BGji4ywd%2FfzbBX9rdZ6gfvQG%2FLqvAy3homwW%2Bp8W&X-Amz-Signature=58888e73c2f0ee66aa3a91f40555de9f2dba7f1feb13755cc03f3fa3b1245dcd&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDHBM6G2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcfppFZWD%2FWJkSmpUctqFhvNHnxUk%2Fqmst5meKBKBQTwIgMLhGfjKY%2BF99rLdQQn4FtUprrp2LkXhPNinGQ%2FzarjIqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjxzx1sE2wAJ8jtHircAwuvj5QmXLRrphVoVOPmVz8xS1kCrXR5PQHqfWYUrWlt9RKxrNY4JIViONn2GK4TrkjOlnrEy9S5O4bBQlgCCJpahsbBhZPrTxMxWOXu0BAva1VdqdM9wSsWQfX0EaV%2FOTI9Qnk%2F3USzoSRLpiEgraZo3gADZkLBnA1hkhUnUad%2F1fabK3h62Z3A49%2FfZ3IA5662ch6WvNU3MJXnZekNeRWqHw8CPbSUaYcxGU4WSjE07q1jqK52AV8ECRWXN7yj5F8oTAxykzSCpCs6tZnG3HiHflVACbfFhCi8QJNyHKu%2FJ489Ieki%2F5asjVba9riPMZA%2FgE32njo7F5OOmKZWXh%2B0exOZw24kyY%2BvW12oOt%2BuA3%2FqXUFK25d2qeOezMY5mWAC8DZspCHqQusEfX%2FC%2Fju7vUvfBO6fedHhgFZ8impwNcj%2BsWVenwY98sa764kAwZNoTwzzmkzCycQ6VSF6wvjRtwFOMGzlrt7%2FcNCe%2FwJfdYDFZZ%2FabsswvGjmkdC8e0sv7IQNCcEkwVGxyoahxUFVXoXShwrIygm%2FCOq4BZ3I8UR3mTCpFeP5WRGhL7smil8GRrsE5G0GK%2Bv8Rh3OnFRtDlr2ITUT1dPCIGOg2ugJ748NmdPIhhN9Q0CiMNbF77wGOqUBNXWH0EG6OcLjw2LCNv7TY2Hyti3h9bT%2FbHElsKnsu8hislUuEUbgd0tsrAxvT%2BNiW4cM3BNj5tINeJhalFXpUvAFTkkCJ49WlVmU494krPaHfed3pat2Hcxgpx5wBtO18FUTfodexMd4tTn4EIwRkGAE7NHFJ7ebTE5KimhRlD1%2FzZajn6guQy%2BrWsoRsGcWPtIgFmAOZdp%2FYpUcCGUFQ2CxfPfh&X-Amz-Signature=2cf765f9c5d6cfb0b96bf7f65aa3433ab2b73dfc02beb1bbc320829acc3251ef&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJRSXS5S%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICTK0Zhsk6e9hw5X8mZElXL4Xza1l%2FR%2FPTW7Qfy3cwI2AiBFROx2XMTYf6KWR8nbfdZ4i4%2BB8TwgFxSywgSFBh9B0iqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMAmAe7dFu7NTrGLhKtwDHwawZPo0jk9zH5nIXeZB8yDDLoDzdI4aK%2BuvqbmWkrAgFWAIh0E4WY9kW0wLQcclZt8JQMcdh%2FgRFc5s0rRy3fKvETAVppgj9nNV3B07CVuqG0Sg%2BHm1WlGsYwotd2ZCCrYq4BV0%2FVWYTk8pnNfDX1jz865xXa6w6jYLYAjSlKOAzypnjrfMEIOk%2BrBDHYqssU57ouXcs%2Ft3LPSnjgecdYUw9BitrFbMH9frpFv0xH8VBN7Inv9YWyUZZxRfSnOKUDfyGiUHuWSNuZQZgDN8Hx7jTU6%2B7kKFw%2B2wL6tCNLFYx7wt8njBh0wFQsF8BYLFhrqN%2FbYytK6cvz9PysCAxXdq%2BC9d6xS8vdoy1W%2F719%2BjfQJIxZW1dnE45TsgKWgQUawlk8ZcskiA5O9152DNSvsD%2FuyKNrY5mBrEMtdp6S83%2FBxl5napF02OOR8sf6ltRKWVtHi%2BdCQdN6OblrSN9HVwHUoTeJp0yjJa4xooUM%2F1a1F9GVKMOAOZZfcqg7yf8r6COIR8kPVVgVc%2BO01FMaZt6XA5Kn1FcpSSuo8bJJVwWLCDGhQS2KBv7irr8VLl602pqztiZTT0%2Bm3dJULBb%2Ftxa6aiHg67fC2iRcHjKxPeNiIFPazCb7roBqYwx8XvvAY6pgHybtRUzjbPUGxmZXtovYc4eTzcqp5WP%2Bm9CR%2BDTzLUbRiF%2FmzQ0Bs5KYj%2BXB%2F7BHqwFmHLmTiEtjv1RVU4grjNAP6j%2Bvqqg3EbFdUihY1zWhb6NibmW1DS3wbV%2BZXzdh5JqQuTb6WC3JPVN%2FW5bmTyijeHWb8t71lnuNkzlcreTXNL%2BCVR%2FzMM12MgS0hNDYIxUxBoNa985ZxdOAblWxUMCSJ2J%2FRa&X-Amz-Signature=f698325a51367f779f6aa9ac4e05fd663c282122afa48f8ee4f4c9fc8092c6a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WSISJDQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFdKTUMhFCJ0%2B8kjgQjZl1HBRXUXMNH%2FuOJcTGzFstdUAiEAmRoGemUR0UvtbS9H4BIcQus%2FCJi3KNgtfyCGHuQuToYqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIuikbcIdNiblge%2FwCrcA6GETYKZd53ZW7nv%2Bf2aUrmjxn1RNUd%2B5Azhq4Qa%2BpOVF4vwaRJ40Hucjn55fK9RSkvsdUz6xWolKZDw8%2Bq7V8UDkUpy0Src0uJFvJKTMawVWFWtRalmTD3xhNkeUiRhCK7t4sUpoh568sNlsB3edIIYU6XqmcNP%2BxLGIH79wXQgTDVmnqnbuqEOMEsXovEfLm2rIhDjf2Mx9SifB8n5a4mphcrAeyu0BmrgIoNUlePr2JCbJGe9nDSuhQS3PtXs%2FnnUeRKMy5pwvTDfCm1UtzKo0EXhdCWvVkQ0EHFtbtujcVl2b%2FMiqiMhYsWnvSRBrAhJ8pM%2BhbcygY%2F8rfxM7J1PC5kNfS7vqgzV%2B95IpIpuUNjvtLvJiaDH6%2Boklc5m1IbsZ3iAuI2NggrYdbpvcO4JPltlCn1ix8F9k%2Bw0oudbtQM8w1xHsTIEaAyPDoOWHCzyMaUzc6OZR5vLSuJcVN0SAALNCVq3VtuGvR%2FARXVOd2EYXb3c%2BuQujZbiETyu%2BEwZj0%2BxqODH41dYp%2Fn5wvZ%2BhMB6%2BDy3vtYP2VGPnsvPddQ1pkWcb2xaq4gwdE6aAn0c2u5nMANYP%2FKVmLHXoZMroCMIMLtT4S11CSFrJhvOuvO7LCU2EkHn1ftbMJPF77wGOqUBT23D4fSZNY4zZHI5P06GISElzGCFz5FWzylMxkt%2BE28XZy9%2BG6hK7gg8nafEjWxa0br1Zeh2ipsXbv0%2FQMR%2FxBi8NDoVn2ThuhycNC90WSTDe06ZNvv8k0s%2FipyKhgc4mWeqC3VbkfwqMVe1hwpnc3QyPbtrlkBzFXr4KYIGy%2FPCBGYqDHh9AKyQE67JTnopMNHHeUq%2FTPcCB%2FhHbKDpGbiVYhaC&X-Amz-Signature=47bf5bf57ea3e9c2f698e4ce390c488295044ad7fe8bbd480f9fd90ca7273b1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCUSOKKR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDERhnshAgHD07kfDXXSaWcrn%2FuPnPTElvTCEFJYxgP%2FAIhAJkOZCJ%2FCzDwn1EgfrpDJGeL1MheZjyXgSCww7gXTDUCKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVs8bRWHORSBpVoJEq3APTRIaedaE5%2Bv%2B8VbDE3ozm1MKIl8m2ViMJEJhRBJ6AtH5%2BHJUZp9OCr6oyeIpKwbZpxO58pwj5P48%2BUv6UDyEwzPiL62gmg9EAdDYn1jLCMhRyXy16SXu8zVDbi7pECmkGVjmuQpIdcu7CUiXIrFv1x4zUDVOG5fQ43tw1ag4YR8P87ZRFFeVuvpFFdMHYWfZrWILyiZ%2BtV0OcHhnfpNjr7bSUZT2iS4cdABWkvZLXWDCIzs13IxyDvQe%2BhSL%2FvUh4pPDfknjEkEa5d5vJ563NlolY059XM3GYfzAWHUeDZsZ2%2FyABNkNqeTp68G7W5RAKQnTZ9Ze1yJjoZ4bBRuZ7VpNnw5SCSDkvxTbKo%2FhIiOSJicpi5cVWpwl9mSeq6t0EMV4r7Y3RCP%2FwyPMhUzf%2BsxCPOiqXk000L%2Fei%2FMEcOXYIrPKGJpb81O6WwpdJVsKKZyf0htK1OGZdJvfQ7lKqbJW7Yyl1bQjaCxvtM1OxxdCAQE1eQI8Lgz7UtuU0d2aZ2O8LMfoBgr0h0zl0T0vrReU0hVC6f%2BA7WaEVTxKzI0M7Q5h0GIwo2K%2FM221bzbvZPw2z1UCjGQVeDYGzMtWeTMpRTTqpbavIinTGDT0kP2ojQ%2BiFyEz%2Ful%2Fj0TCIxe%2B8BjqkAcwLHNKkA0CZj9WtEgRdNDpwtEs7JYUYH7jJK324AiucoNuy10GgQ4VDjHvs%2B3N5fsei1kET4l74LFFyb%2FgMQVvISJ8FFNDSnuLJTLadWQ6ZPFZCLhi7JqHVYkQ37wQpDSyRLPPQY7VgIkeR%2F0X%2FmpRV0285wHX%2F9hCOq4zH5P46YgL9KU9aIl56YEgqXLLq1FvSHiTcJOAIwV8bJn1TbG3%2Blhlq&X-Amz-Signature=513ba61f8a7d42aadfa18acb6998e3cff10270b4cd4aeef4c49b06b10bd89431&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCUSOKKR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDERhnshAgHD07kfDXXSaWcrn%2FuPnPTElvTCEFJYxgP%2FAIhAJkOZCJ%2FCzDwn1EgfrpDJGeL1MheZjyXgSCww7gXTDUCKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVs8bRWHORSBpVoJEq3APTRIaedaE5%2Bv%2B8VbDE3ozm1MKIl8m2ViMJEJhRBJ6AtH5%2BHJUZp9OCr6oyeIpKwbZpxO58pwj5P48%2BUv6UDyEwzPiL62gmg9EAdDYn1jLCMhRyXy16SXu8zVDbi7pECmkGVjmuQpIdcu7CUiXIrFv1x4zUDVOG5fQ43tw1ag4YR8P87ZRFFeVuvpFFdMHYWfZrWILyiZ%2BtV0OcHhnfpNjr7bSUZT2iS4cdABWkvZLXWDCIzs13IxyDvQe%2BhSL%2FvUh4pPDfknjEkEa5d5vJ563NlolY059XM3GYfzAWHUeDZsZ2%2FyABNkNqeTp68G7W5RAKQnTZ9Ze1yJjoZ4bBRuZ7VpNnw5SCSDkvxTbKo%2FhIiOSJicpi5cVWpwl9mSeq6t0EMV4r7Y3RCP%2FwyPMhUzf%2BsxCPOiqXk000L%2Fei%2FMEcOXYIrPKGJpb81O6WwpdJVsKKZyf0htK1OGZdJvfQ7lKqbJW7Yyl1bQjaCxvtM1OxxdCAQE1eQI8Lgz7UtuU0d2aZ2O8LMfoBgr0h0zl0T0vrReU0hVC6f%2BA7WaEVTxKzI0M7Q5h0GIwo2K%2FM221bzbvZPw2z1UCjGQVeDYGzMtWeTMpRTTqpbavIinTGDT0kP2ojQ%2BiFyEz%2Ful%2Fj0TCIxe%2B8BjqkAcwLHNKkA0CZj9WtEgRdNDpwtEs7JYUYH7jJK324AiucoNuy10GgQ4VDjHvs%2B3N5fsei1kET4l74LFFyb%2FgMQVvISJ8FFNDSnuLJTLadWQ6ZPFZCLhi7JqHVYkQ37wQpDSyRLPPQY7VgIkeR%2F0X%2FmpRV0285wHX%2F9hCOq4zH5P46YgL9KU9aIl56YEgqXLLq1FvSHiTcJOAIwV8bJn1TbG3%2Blhlq&X-Amz-Signature=624d67e54016538cfad322a3f1a91327b0f57fe13c9951f88707eb839983ee0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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