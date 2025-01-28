

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RA5QG5H7%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIBVH6qlbmKSGpbdVDYpEyvOBXYk%2BJ5ZUUwkfx2Q2C2wwAiBiz6c3I503NgVK9PUj5MHrLiaH49dCHeyuFHjOOm%2BXjSr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIM4%2B2vjbf%2FACyvbYRxKtwDPSkLtvnJLNC23RVmkcIC32FY5AJK%2FKY%2BjwMBYRhc3VYFwX%2FYcQWxtjOlPqSnhzPqaekh5%2FxsCJCs91vTstLiqbeDHstbKKuVaVo5MWgrCEyaCGcKeLg6Ysi%2BKlAW5hf7aO6tEnEvvfy3l%2FqrCjr7KdZNFS2T5OEmcvSrYeA1fxB3ZpUGyp97z6RzaMz3QLD2n00IZDMsfbt4Vku5wgLsDPc3XxWBYD22vMV%2F%2BK%2FQlBTUp4gfNRFV1ClTfgpOa1wAALesHBtmtw%2Bx5jbjmoeoIh6SJBEjFlHLwkJjGvlfMhJcewcnX%2FQ17oygjFtAsFjv%2FwtszW%2BxOzy7DSSuDC0FAY3Bhc91NIFNZcf1rSMF43zFkPgK%2BrgE8lP0lxiFGurh5sRBNxEYHsNHbGF0TbGNo%2BRT3ecQvrsDKYLCl%2BrFWhyCwMzRdW77PtlQyXZGJzG4U0bV0izJHaVoqe6rfNM%2BUvuedni2mb6u9aKa%2F6NLjwtc37HGc%2BufH9lxCr74bb4L5QXAUI6oHKy7ZN4PFTPPrYHHjhArUp%2FNoNEm0fin3PRC7TSQzzyCxuWwwqPEGkNSP%2BVX7JNM%2FW4DLRYGo%2F7nEfw2htXYh5%2Fso0cvZcxUTlQS1XfN63%2Bb9dhjLicw%2BfnkvAY6pgGsi34FIeFdzzIASjvjzubrb6hs2lkmKCUI54j02kZ9i1Ku%2FMNWuX2aAUvDYVN1IEVerlAqh5dFrwj8eusIL4PXDjJnXDH6je3%2BNxd1KOsK6XuKT9cwCW9IVYxbwbTWT%2FiyRpRshE9f9DrILznutFyfJbYY2Brpr0TpWXBqeOr7Reckzo9GxRs63o9zwvLYk8LgxbYl5kvANdUempve0lLS0HnD7%2BZH&X-Amz-Signature=2a0cce0719d1d8cb288c940484c8cc415f43dc84ae6bc0f637b0292aa47d84ca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGPIPCLC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQCLv9NQn7j7dBNHi0dzU2WgacqrenIdItrtudYQ%2F8XR%2FQIgQTDCB1vYckQ9yBqwWXWFsncTH77aw%2FGMZ8rGFNUq%2FfAq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDKrBmSi0UTnoP0OD%2BCrcA3%2Fie%2B%2Fi1yxHMJphV3Xywvrii0oqaZeeyWRgJi25dzdc7C7EYP01Jp5z%2BNSiss%2FjlTkxFvuRLZz0%2BRSIhAzE23GYO4Os6BuwBNsTiiwQi7OuXU2yC57rEG%2BePQcBzp6bBqekt4vqH5Hem7WNN7uddEdVnwNm2qzUl%2B%2FAidMvnz09sro2v3fQQgmH%2F95nQvsvp%2FH2DtpZ5%2F9z5sa%2BFNudjzxkuY3MmtdwINTZRVVH6fPR1iqU7Vom%2BiKvLWGVnLyYg%2BrlX7YueGph%2F3HJchZYRs0g9LQf66dR7ywNCfBbiWj0mXmyHXnRDUCTLqCTVBgWmZIaajuxHx6qcBzX4QBvIaHEf8ls4Z1Cp6D6B680Tu7L2VVBb2Va3O7QCvo90PoDOV4AVvgXsSVYt2MRmHdt2KFmW3UpR0vFtlutJ3GKQlTrqe5YB1NJdsR09uTUl%2Bm0FL6fiJP6zZRrly7U5Rreg7A2ytoR3RstWdUfxpOy10K9h1OS9xH8%2B2LTKQgf3ETAytftgPhFxhYYWCBlrCp27w249OH0dgV1K870ukiWBwXr8XhMAhggdJ9%2B%2BU5pQdZLaUesciwqVupHcbHAYTZcb7fXDrNw3SsRDY2v1AafOn571RWUk2vMxfwEldwsMIv65LwGOqUBEyxWtj3g3DYDvg%2FE8vBm6VZgGjb3DPrLoaeA3IqcsVwuzSad7yMdxZmunO%2B2LwU9Cxgt61l5FrLo2Xcku%2B0dGtokWUW%2FjKodNotfTFKRWyEF5a9xZyisKhMBdroS8aGtNcEZC7%2FuA1ET%2But7lIkP2lSFr0eCR1SQYFDzKj7zEMKWNFxNOqQG%2F%2B5HmHScyXGXMuMjS5oF5w56wR06gKXer0XnScs%2B&X-Amz-Signature=78bb6d76bb8351b580607210bc3700f7c02b16f1e334807cba056929aad13a7d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V46RCIL7%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQCEEWywDkqpMAJ9pQIfb9CZT47IeEsrb4zhh0fHXpyj1QIgVfSyUwtopIODnc5YD1dlLSYgKF9XKfvDJcUcuQT9OREq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDPxHpX2scBrCwZ1FDSrcA8hOzxs2eqrnv4sF6%2Fopd9Jl7GslE%2B9bhxtEa6Nnpc0IhryZtWjGtN6PH5O%2FQOt4IInv0bZEof6MdljfG2WMT5I3geAs9agslQXGQEtzCQdkKmilSxZ3uU%2BjHewSZG5TiqeO1LB0a3D8xUioYO9zndWQIe1UABzXjNZND3SEQt00A%2FhatCucGjLjFagIwQAvJ6r%2FmPy8cdaJunhBO6Jq9VkZPJ%2FtUup%2Fszgugyb9yWvF2CAHD8qRZDkBi2pimru%2FODhTE9iyOB2gELmq2UlTAxQIMbFGnC4m0%2Bum3P2ri%2Bht%2FBgIaTWfKHAF2ZjJ2L5Z2yQjQZb%2FUn6Oa69Lte%2FIrje%2BGWKuCH4BxM12N9wwF9ssYSBwjPIfYMMiBdOc8GVYTLpn%2F5n9ux5T%2FLKQFu6U6CYuqDdfHAHBLbK3CBPRzS5WfrTli52%2FOyA1EEzZ3MqUfseZMVjeltRIfodEYVhSox5xwU0fxMjVTMIHVOBNRxs9PYzSt0SaQbP1QyWilNXHrKVTnzHHVf0XHXS6gMO8eREujiM%2B2GTbcsTBU765JKTSBvAFRN6bDGPQKP5Wp1Ju4zeU7obl70iWoL%2F5h1U3C%2Ft1ssMTGrwnsUIrqLkbcKQ6mxs5BXxPo1jbJLrNMJ%2F65LwGOqUBpSysGchTJXDPY7RlQHlEwrNL7ML67OBIWhitAFoZYUocSffZBMagHsdM7muvPXA2q2ObxOjfop3u5KIISxSOBhwmxqlYCRKgyejh01nsy66FKPfhQXJ6hikCCeUHix%2FtqvxN5raDrIIHnz3w%2BkJo0ct4QxShe29p3emv0xaVug6QLcOwHcmAk%2B%2BGdsBEtb%2BsDgvZ9L9DhOKAUIhDHLjU6kUVgk%2FS&X-Amz-Signature=de670c11c6c43e95cea482fb7fc2e33631995c8ee897fdbc16d683aa110137f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G3PZAT6%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQCLNxXNhnFGCUSAdApyESgIUh%2BAbvhhB7wkWCo2FtJRiwIgSHbuR3yNBCP64i4nYuJeq2WGnnTUhB4ObWtPBSNy1SYq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDF5bieoDZ2f%2BwP4huircAyUPStO%2FvIa38RWOvg2jERH0EwwjlA9UatPMPKTmpySsz7aXJKZN4wLsBgpEw7WlEphV9WoWAaucguhwMfn2htBzBR2Te1Kl0fnDsbVx40DnYE5u4y%2BBRY6XOX8A%2F9eZJ%2BIizQNfmE37Zy4aOZNTSIFrvYm0zPEKPOF1Iv%2F33jFqn7v%2Fju5CbJLTVmDkWmce%2FvE2MHjSc7DzlTT23oOX1JJZLmmoWcY%2BfWOvB%2ByQuBaHxdAJudjrMiwiaBEj3o1qEwAQ1vw4UYwwqNZBbnBvvjvn90jU3s4QiHHMA1LBIDSFZsrGjI9v18nTrPEX8UoBOIiYe8Fu4AqaqrSzgGlpDihEjADr09piMyacSu8tQ4nvd8Oh9upqavfip87%2BWNylbeLNU0HiS%2F6USyUNdYt3jQFKiFi%2FnzRU9WJUJqhgqpTXPmhvx2cQNkhcVY47a2swh8VQ0Y%2B9MQ4JHOccZ14h54qv%2FgihjE0pIXr5okTQRstSUZ9iQ%2BHxxko%2BIRVVg74QA3WUz0TZiL8zeSd%2Fb5FzCgsnKEGEQ8tgTNg5pJppwTUpKTiHmBtcAxJD4iB%2Fn61LLxWgQTUu5DwYJLiSpgkJrkLYfELbM9sRiWu%2F4eJi78wGH8YjFF%2FLCInYHoUPMIP65LwGOqUB9wwZcEzuNCFGkH3EW8Ph4UPEVaHp3vSqn%2Fk4fEcby05qqgL1Mh4undMxzemvZTlDq%2FLWSN2wJKDZWzqlXvbU%2B5mcCjruvdVP5fv6nk5NsGjS%2B005uYfd%2BIFa80nbtuQN3RgVVf6utuwU8GF1trpEo43qAX9ClbBCSjrSLfDYxa3adbs%2FyOeEAqX%2F5VdenQs7OOp62dbSP4rgxF6J7Jw5MbxeOzbf&X-Amz-Signature=8a45321c7bade52551403cbe2140e9b54ca76bc3bfa7ab32f587243904b8c302&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIMTCTJZ%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIGSXDm%2FYnwnP3pJfa%2B%2Bwt13DmIKKE5huQn%2FxdhTjbuLeAiAnKh0cxzsMG1uIo3B%2BAX%2BR%2BWOXrhuhxILoEgXOvO2MTSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM8RoNiTBqt6IxgT22KtwDysoBLF44LdozlVuu9qR0jtHYwwyjmwY9Y08U0XTcJcGgU%2BdmfwaulqwxES6e1rRkO%2BRB1IsRI4tozvVlwHXF9kyUPAOTMUpVbNABSAqUxd0anFwT4b%2FAqqZDcpRkEE48gANXLGg%2BHTRwSP7YIpHpIoHBisYBNwa6bxsSV3XVhqjnrE1IhDl6SP2b9WvRxf%2BteZGBZadawX9RSFvdNWtV3kNQVV8U9K7b1iITkkDCii6Cu%2BBbirw2E%2F1bX8wJWFHbTqgyixYZo8V6PyXG3xuwwYDFvn%2B57Cok%2BSmNk85qXWw5TDqDDQr%2BMNXexSG%2BDsarg%2Bi9zg9LkTWmxUB2w97uBb7BEQZUQj4UphDZmvcfc45LBmPPY0HGknt%2BOODkzTc7aIbup%2FdCIDrdtGfp%2BAjkjnnpnNrH5LY2FpJC9l3ZqX2yS8MKPKg6plFtuPTwxsiWJnFF0UfP%2FJpKfx%2BhdN7eBFbC3evdPJX7PBDcnxj%2BtZfUGlgWDMhMgA456dVP8OnOjMjU6zWrXwSuAWsRNrEYUj8tI%2FCWCtUUlo%2FK12Rz1lEe6r0rnxouNiOO3PyRprNyR3Q8AXu%2FZeRoGuHfSkGyJgo3RLbzcsOxLNgIBCcuNzpDEj4jaool7k9IyU0whvrkvAY6pgEHu%2BxYOuVLf9KHLIyMC7MmawTqTyPtPdKtPV4tZ3Ox3YGzaIdJXllnuT1cu2omJtHp1gC%2B%2Bo2OzT0luO6DPDpaTG9xrU7QLU0CsnIg5seOkyOjIaava8K582hmG0VVOkIBCTVGeUqXj86JgKxAOy0ddfPksja9Wh5gj6a3%2BnBPCq7VbB1mPkY90szVSzKUdxsNiRsVckQLxwU5ZtRxeZDzkpoC0yjq&X-Amz-Signature=28c9ae5b169712804f5f10bbf6ac8182eace43a4439821271bccb94b613e1390&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZL5HU4GC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCMiAR%2FkAe2KpQtuIsNuMESeN2Kxf7EjbyPqYOUKt4dngIhAKTflFUPHtxFi02iE%2BRK9UZg9t3E1u80eQWRUK3XBO%2FJKv8DCH0QABoMNjM3NDIzMTgzODA1IgyB5IyOIqUNCEVbPgUq3ANUe2sYlpSsv7mgQ%2BtgZMdQj95akyGh4e2ummr%2BZk03YNIAmRN3d%2FHF5xfij2FImrmRNvgvGksLwQLwR0SXz9638A64uwPeD7LBP3b25a8PZzJqJFdqnSPZu8%2Bce0AUqQNO2LTATnTTjFuSiJk%2Fx5I3KWDEg7Q03bnKCelmhI2GyMIu2KBUxehxr%2FwLS8%2FmsQvAwkFxZdDQvq11gnkwyrDQ197hCbRCB%2FO9H6DWi49IvZAwSxlZjwv209F4DQJxPMsn9FK7CFjXLSGOm9PgjKIkKjxwCECYfIY9QvJa7nE3rsSd61nCNsCQsA0r3MmN%2F8SeZGmuRRRs1xBmD58rEdR5HMaw%2F17FLLvrAO4%2BqaS9BJISGuDfOz%2BsUS3SWePT%2BQvfCwxyUqZR4BE7hCfo4BRqf7RbKyyRMJ17qi8Ffraw8InjoGBm6ZTSe0Op7pZxU%2B4lfc1hDxh2ABT4FMuSt%2F6az%2FDqjO9x5SPe4zLZbYtGQBbcyICYEIdtpbquLtUh%2FEOba91zBcjFe5pVmtCa1VcNB8yhAblsLZM%2FbrNM%2F3jNwEVi2ObGX4Ch2yMBG2jxfOeDK514QA1KL7j%2BbwkvamvAuyTXTka94MhYUQwG%2BcHwE6Z0RCa8VoTYDprCIjDA%2BeS8BjqkAW%2BZkrbuK2kFWI3FVC6hRYI1VN1VsEHQxxGXLwyy%2FmZy0pgjVVuZNgCqSPauPh9gTsLN1tAYoy9W6%2FmWbC0s00R6jskaeyG%2FumYaiCBkvIJ6hrAS049rmDpn4GnY8SnPmiGs4vQ0SqA9V3ziRVJ%2B3irNqwl1HTlRk7Ip7NUpFaoQCxVSsXyfx4CFzp44sEYSn5hzjvDAa7I8Bvc905OdDAOXPlxr&X-Amz-Signature=f70a6e890269094ab2d5c90323d279ac4ddb9f6118b5301d8d1a7741a4f982aa&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AJCMDAC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIFiVJS9hqRPPFmyjXhurzlqRRkHuvqAN9NtbSo8QpsI8AiB832GrXaeeT%2F%2F9XsFmpoc9sKx2sgw3v2GGyP0QXbv6VCr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMLLuKKlSSXEvpTfReKtwDMzro9zBu2%2BvjnyG7W3InapRoIn14GDjHmB3I6YDgs8yJ0JmDWWa3q%2BFytuP5%2Bqdq38UHBbw9FfZWHJBgZa9stU8Dfpa2cdo%2FC1t%2BkdGgbLESD3sgvXb9ClgxXTiyYv%2FObphtfYfvVnSSmRNNP6h772%2B9h6vKcES%2BnmQ3Qdra4kBccMfWzp0JP7iZnuKsWdI41OyxATtT0%2FMIXsk309F1%2Bs3LYY97740FnBoOfBWUpANoj6344x5SHeMRkmNJDPi7j8dn5kmbW33n1KFTgBpfS4QYRpWgd0OhzFV%2F7Eq6kjnX5%2F%2B%2B13IWMJaVXC5BtIjLBuRkd%2FhiEeXqge%2BbxQSPvF5tNPcS0bLHtbNrm6NNb0%2FQeTC%2BH3b4TOhKhUDAf6MOBv43MV13pkeqT36fjAhd%2F%2FUuVgWEsMxXPtYxsrCjLOnJjXIt5uys8H4stcmBm4G8%2FSPz%2F54ZmLaKo6aMm1Mo9XZNbXwPIF7zxrplGZCAORiyexDykMfPuNYmfxXmKT3HwwepcobFCIKJYxAPMg2ISEAOlS9mPPM%2BG4GUqBaiq0Xx8JTpBaig4VqEtrVbr4oOliDfFO%2B0on%2F489b328KhjwqUEyoRwGHkjWHKMHPBaG3o8Th99TNylaZSr5UwyvnkvAY6pgHPsVoO5DjAkULRPtF66P2mVhgZvdUBwj1McQupcdNyBGZF1MUhP66SGnhprILE2YY04ht%2FAlzhlAsbnEgvNzr0sqQUu468WZjInuC1Dgs2O0dguDIhCoL569DV8yyB8Mm%2B7n99KY7YUfTNaW7Lqy41C15goTjFaM5ZLtGcAeyhfnYAkFu84z4Q0ba9AdnyulJGMJIuoHrI0k50go9muxEjxOIsxeOR&X-Amz-Signature=979a08200aa74f5ffaaca7af664ba6451c9f6f8433a8a692340e33cb7e0fefe1&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TDCQPYY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQCopV15xJ5IbLVdvcDm%2FuKd4O8yxqM7j%2BqmiHg1gEEVOAIgW4Uo3r%2Fe%2BtESjxdeuPlGgOiRYf8CCtZcSbT6taTFsZ0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHeoUIIE2oMzU%2FlzxCrcA6UAAX0A38LG9oULKFzy8f8fojcEykmkudMCcD9RwRCBML2tnBJXwPTYVjmTH5hNsLKQAO2iElG7FsUYEyL8Apn0hsOV4IPX%2F79eoilAtW9assxAZBu7Z43T4zTn7NyKhKJpZg1QYQt896zw6%2BIArJEZYTTSHyGCfAozZJHL%2BMdfkUFU6kTqbiRBWUy9yJdpZUK9Vvy9PVkQ7iGoSsFp9C7rjzM4KsESt5eAGlFuKNX3TkjhnAQGoGMUDpmqV9mtS2qUof3F5PrXXK5dG9GqxpYxLyuSXN0XLnyHYiYEMpi4mYShv4c6cbzVb5ixcoL3cbc2PRdMLOB8hPXAznV99F%2BzN78dSgYbkQF8KIRFEFUQYjXdsfZ7ze4S%2BjvsSGOwQa7Ro%2FTnzR9s8VKdyychUPrD%2BS5I%2BGHRS37gx1laX7cicP58LN6lOb2en5VVGQUWLqKyx6wzPeH7fMTjD2K%2BixyiEDjytSuOtJ%2BVBqBt%2BEQYkcbyftAiDv8SDGnQ0ZRYF4l%2FF7aTnr2FUBkenHUsj50I56H%2BcIbN%2BDcx2uu0MQ7TpJ3hg6Rel1%2FzZ2RtBBDBupGneQRq6AgzFKtBff%2BecajJpsPqNumDOvPzaYWOsPOpLtu7%2B3l7rxvu1B1WMOn55LwGOqUBIzfl%2FapCmGEViRiQAd5OUme1WFgwCQ3QZjHb1W1RjOXzPFvqt1maeKPzINtvj8fW50NiIEiYdOSQgrN9rKFErmTSnkZSzvJ6XP2udniEaZOM9PieruCdmofGwMGdf555zW%2FpoFb5DyCEiOYBTFB11iVOI4Od5xG8FQNogL5oVg%2BzRaYq4KKxWYWwJ12rhKfVRLV4Of2efUPXIu1i2yZQNe1kxqai&X-Amz-Signature=e99bb05594e7e48a5dd10ad3c69e252baa706bae8fb9326bd0925c0880ee30f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIMTCTJZ%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIGSXDm%2FYnwnP3pJfa%2B%2Bwt13DmIKKE5huQn%2FxdhTjbuLeAiAnKh0cxzsMG1uIo3B%2BAX%2BR%2BWOXrhuhxILoEgXOvO2MTSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM8RoNiTBqt6IxgT22KtwDysoBLF44LdozlVuu9qR0jtHYwwyjmwY9Y08U0XTcJcGgU%2BdmfwaulqwxES6e1rRkO%2BRB1IsRI4tozvVlwHXF9kyUPAOTMUpVbNABSAqUxd0anFwT4b%2FAqqZDcpRkEE48gANXLGg%2BHTRwSP7YIpHpIoHBisYBNwa6bxsSV3XVhqjnrE1IhDl6SP2b9WvRxf%2BteZGBZadawX9RSFvdNWtV3kNQVV8U9K7b1iITkkDCii6Cu%2BBbirw2E%2F1bX8wJWFHbTqgyixYZo8V6PyXG3xuwwYDFvn%2B57Cok%2BSmNk85qXWw5TDqDDQr%2BMNXexSG%2BDsarg%2Bi9zg9LkTWmxUB2w97uBb7BEQZUQj4UphDZmvcfc45LBmPPY0HGknt%2BOODkzTc7aIbup%2FdCIDrdtGfp%2BAjkjnnpnNrH5LY2FpJC9l3ZqX2yS8MKPKg6plFtuPTwxsiWJnFF0UfP%2FJpKfx%2BhdN7eBFbC3evdPJX7PBDcnxj%2BtZfUGlgWDMhMgA456dVP8OnOjMjU6zWrXwSuAWsRNrEYUj8tI%2FCWCtUUlo%2FK12Rz1lEe6r0rnxouNiOO3PyRprNyR3Q8AXu%2FZeRoGuHfSkGyJgo3RLbzcsOxLNgIBCcuNzpDEj4jaool7k9IyU0whvrkvAY6pgEHu%2BxYOuVLf9KHLIyMC7MmawTqTyPtPdKtPV4tZ3Ox3YGzaIdJXllnuT1cu2omJtHp1gC%2B%2Bo2OzT0luO6DPDpaTG9xrU7QLU0CsnIg5seOkyOjIaava8K582hmG0VVOkIBCTVGeUqXj86JgKxAOy0ddfPksja9Wh5gj6a3%2BnBPCq7VbB1mPkY90szVSzKUdxsNiRsVckQLxwU5ZtRxeZDzkpoC0yjq&X-Amz-Signature=c5692e8167aa39281b98fcc5f66273309f863970b44f9feeaecad28121144e2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVKGIENH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIE3yAfAMfWR9eoxqLl0YstbWnI0LzkOnehqQu2EEoTLXAiEAuZF879cRpm1pMtAcEK6kPwJUcVzqotxsRDCIVFYE6mcq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDFGIO4XtWlIqstNqPyrcAwIgU8yH5WlKrUzcl%2Fiqx8cpBjqhC%2BbokxzKJm6PSGI6QJG01oWbH0D9dp4HidjlZfIq8D2HCi5Zt86TuOd6MxP2bU0xplUs5%2BoUCkCUybw0MYFypHE%2BgOo3eavhSYG4mnG8vP%2BBnoM4aY%2BO7hd%2BCWQJvq9WzhBibrfHQA0HwYldFbudhw1ED6nEPefGe5MMa6TfJ5jxxwp6oDdvmFW4DWiTRIR%2BozSsdPgU30gWMWITNMy9m85b%2FyJIRV73BJTh3B52mEG75E0O19boS4nXJ7aWfA1sxhaxPhVDRMtXcsdpbjpdabaxRdkZVQMp6KKveRa2htzKBk%2BTAd5EdslfV7Uh433ClnNcOVq9ebCXegObzqCMIsDuJTXrc05cFLE0c5LxIROU6sv3DDa3V31sU6O3plivVRu1YdEsjGxUpXoOkr%2B2fbLxhcUP5zpNLgx29LWe1mF1ZVM7rAInp%2FDqWRNbPyxyD8hX6jkx9fZcZQ%2Btn4Chhu8VCGA%2BQHDIU6afh%2B5i%2FW5%2B8ljw%2FqzgOqreBD6FNGnzoQhxIqOBG1l5O5l%2BzT2TmC%2FagyGfaftp1CpM6lyNNVUn5s8hAG74L7p5dmwITBLbnaxR9040rVSBNJSaf9sHCfRoWlXo%2F7eAMIn65LwGOqUBXttJw7GtbfO9m38ESHGTxjsh2UP%2FLEHtKLtMfqQZLLDugtrz5%2BMqQgl8doaQ9Ljys7QMYgKygwjeDUppl0FZTxG9fAbJsht%2BbPHyGIrqsTyUOQ6%2BpUNVLKEj3gG2TTZPcegwDOL2b8Z4FRaf28D5epQo577L%2F%2FeMzUTuoWSHvoBPBL%2F%2FiibVahdz7FvisHHbTuIlZm1GxWnMG53ZJqCc5z0GE7kR&X-Amz-Signature=eb0681a9acbefd38c78ff95ed0e4f7635b465c638eed7a28f6632bf59ac40e56&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVKGIENH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIE3yAfAMfWR9eoxqLl0YstbWnI0LzkOnehqQu2EEoTLXAiEAuZF879cRpm1pMtAcEK6kPwJUcVzqotxsRDCIVFYE6mcq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDFGIO4XtWlIqstNqPyrcAwIgU8yH5WlKrUzcl%2Fiqx8cpBjqhC%2BbokxzKJm6PSGI6QJG01oWbH0D9dp4HidjlZfIq8D2HCi5Zt86TuOd6MxP2bU0xplUs5%2BoUCkCUybw0MYFypHE%2BgOo3eavhSYG4mnG8vP%2BBnoM4aY%2BO7hd%2BCWQJvq9WzhBibrfHQA0HwYldFbudhw1ED6nEPefGe5MMa6TfJ5jxxwp6oDdvmFW4DWiTRIR%2BozSsdPgU30gWMWITNMy9m85b%2FyJIRV73BJTh3B52mEG75E0O19boS4nXJ7aWfA1sxhaxPhVDRMtXcsdpbjpdabaxRdkZVQMp6KKveRa2htzKBk%2BTAd5EdslfV7Uh433ClnNcOVq9ebCXegObzqCMIsDuJTXrc05cFLE0c5LxIROU6sv3DDa3V31sU6O3plivVRu1YdEsjGxUpXoOkr%2B2fbLxhcUP5zpNLgx29LWe1mF1ZVM7rAInp%2FDqWRNbPyxyD8hX6jkx9fZcZQ%2Btn4Chhu8VCGA%2BQHDIU6afh%2B5i%2FW5%2B8ljw%2FqzgOqreBD6FNGnzoQhxIqOBG1l5O5l%2BzT2TmC%2FagyGfaftp1CpM6lyNNVUn5s8hAG74L7p5dmwITBLbnaxR9040rVSBNJSaf9sHCfRoWlXo%2F7eAMIn65LwGOqUBXttJw7GtbfO9m38ESHGTxjsh2UP%2FLEHtKLtMfqQZLLDugtrz5%2BMqQgl8doaQ9Ljys7QMYgKygwjeDUppl0FZTxG9fAbJsht%2BbPHyGIrqsTyUOQ6%2BpUNVLKEj3gG2TTZPcegwDOL2b8Z4FRaf28D5epQo577L%2F%2FeMzUTuoWSHvoBPBL%2F%2FiibVahdz7FvisHHbTuIlZm1GxWnMG53ZJqCc5z0GE7kR&X-Amz-Signature=bfa2e372a7c94139ee4fee0d67c35108acf8e843b582d8a2eab1de4d68200579&X-Amz-SignedHeaders=host&x-id=GetObject)
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