

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBYDS6TI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIFz4SpPQyKvp9%2FLJl%2FC9ZFwl9VqaMkahEqLVn%2BftUIVfAiEAgco%2Bht18NakigR%2BUNHYrzAyOM6OkUVQTmgnwb%2BEw%2B84qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJis9G1dzv67qkgAlircA7P0aDWFl%2FiNp8tX2PfmvkQNdvTgx%2FY2SFMkDZdZddHVWaj118NuUdEePq%2FPyOAq8A0hXmAWYW7rQxQLutUgnhbWehsmH%2BWr1KhFHOfmzGpBczLgAQJfoL%2FAog6XUoYO61v%2BluJIUF%2BoKuIYD%2BSm7GVgFj78ich7yyQ%2B3DNBlMzfEkhhb5KUHQVsR5CfHvXxVUUD0KXfpviIqrROktV1axy%2BWvGWM9bcZhLr8hSZ4LpaNp1PgakwwojdXCUMKqMGFKaLixdYp%2BkdES2AVlnhwZi7S7NREvqGeM6YdHIIJHr84lo4I0We4kjKxpkK42Z6Mg9gJwb8yTSGjVc8u82oiJ%2B1CJZD5SbNUjLRwdEz1DqC5FZoyeOSUpbNMGuZtsEYfczpOmN3KNKug%2BRa7pGICbr98TFGcfsGEyfYygMKaZ68VQNtTcG%2FOnT%2FFXAT0Z30Fhfoba9qE%2BC4Z%2B8fQsnWjFYYxWN4wiq7BBZoLyag8oBTXMbcmbVS340A1VMjXsxtHjxQirmSVNylpuZCXzyBOe7fv6Bo4w5WP2aOEfZOUMn3cru6nNwxlD9JqNfIQmBrWuX4ANqma9BOYMx1nscpjglifvRECxwwDuBzV4oNf9JZpSur5C%2FkOEiUschQMOKym70GOqUBrpqHsRmy%2BUFTnMlqeCeN8SXFF2qJ%2BT257Ze5RIYClx0tYdJIA6kSV3DFC5sGv2Z2Xa2r0hhXE%2FHqeZlMmb6qQHEyALQe2fN6p4UVhrN6N3eGc7By8UeqUIzEwFjcnIHMTzjIDb%2FpAtuFzR%2FknAtEQFoCDKZCCSS6dI9mK77ysM%2B8ob2L7YdZPEucZvBqLq35JShugEGboj3t4L7Nul8ubThd%2FqY5&X-Amz-Signature=55a184d9add2333c07b0935f6d3fb64bada442a77f3b0befe00d814d6c514adf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627YMO5DV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIC5QpQFD4Clnp6TXjGMqgNxP8fB%2BhXyc8%2BJvZyAn5e2gAiAZEG3eAmaUOf2U8BJ%2BykEaYuYd%2Fo1kG6l89gljCwLsoCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqLJfY12M%2BL0skue4KtwDah9J%2FWiTurEuWmyDLIp0i%2BzZyl8SBzNNzf%2F0Y4F80qkAhUh1vxDADkVLLcGI7WwvPKxxByJhMRla%2FQQgKYAz%2FXbrU1nBH6wAjKzyHlxSdGDvzqj5wbdr60%2BZwg6f%2FU8bkSGXiqo1ZuH8%2F7G4FCaKVkvHz4pnO9GcuoPlBtnUb2EI4TbDMIsdgA5F7dezESJ6GpSMvrErq%2Fywxsy9h48dLcSdzx21gCMvqZM81y6m708KaVWLiWAY4%2B8WsLgKfIBuxyea0rbLphIqnm3Npd8O8A4bPu9WaZ6I8Vsgh5er4iP%2FouUbFqqReJtJMDJURm3xfDuji2qGkHLCxS5kf6oVOBKFOeUwXWHpdSKMwnOsSeeM%2Ba09rUqgo55OpDRrDR8NO%2BBfdzxSogn6XBHytWvMQovXw%2FVtmNvYr8z1HKV2yikRZyBs3ASV18a0nmAWP1rD1Dfq%2BejGBIFXJozKwEslHuKN8dj4GcA3rtkKpWLTB4ExtUXLc69gbj%2FM1ic0h84cv2lUBPpslx6zqphd7nEh9XXfjHNSqQJfjB9czgmWbCDWHLaBA9rr0H7lIJ23ZZ0lqK43DLV4IbySErpMtUlGuh%2BRWKGl1dVHb4gEFNa1hSK9mSWUdCtEO5ty6v0wz7KbvQY6pgGrQLTkst0f%2FRCNySUl1mq6FIodhBSmttq4FAUaT%2FpSA1ry0CjzXzk9j%2Bx7iK2LI%2FcVX8KY0Fb7xc2GlEFJ6iHYRwS6ssgzFBYAVm8tt6I%2BG77mf%2FBbQQX1auL%2FSjRDm16Xf1V69x1E62H6ntCHP2ffCwXbYwqIE1UaJG5iQ%2Bzu%2FW8LZnTHV%2FtQlF4rYsG%2FmyGQgn6bjuiClI0dhNbgtgdYLQx0Q6qw&X-Amz-Signature=4a5648f07f540cba6d5cdda7d97a5d54f8bf84b5ebb996cdec24d7b45bebe5ce&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLY6AYMK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZmHRJMSZvUmQTQ8juGWhIqmGjj2ZOVU7lv4WPYan%2FswIgXRN7bS4hdBr9pUrlsmBjWWhfPM1hXTwPcJHzQb%2BKSt4qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB2AbpHhe9MFYcFHxircA2g%2BYnCrb%2BbJJUubco3i5vTo2Y4kOWbviqITs64oAk9ugJVSyW9g%2FWUcUUBRukgemNnRU1R%2BF9kTYpKfHsDJhnd510a%2B0B7QxdYIZ4oDiSw3h17kh8qp2Ssf8Lwgv4EJ9Udm1N9rNfvxRPMfcV9CAZ%2ByDUSd6IcTaObgNzhGjbuQ%2F18T241daEpNqrRK8sDc7qSzqTg8TLJtjIn1%2F8%2Fjs1lMXzLgnsZh8sVnCjn4dJ9ng%2BRP6zhvghiEy6izi675K9VXPYqwUlhD%2Ffg2QD4AMwuc7K%2F4t70oAiEhlF3KMy66RcCh4G%2FajDmWcAQ3Kx9Q1ccFpO5EBt5YrOpQe2AYc6tnE%2FYTyH5jSlAPNJ5mKl5VNfRL2lUUf11yx4Q71YLDbUoYQcRu%2BzwR08BCLdSejuxAGsfgKgd8h2ybdlrfR69KPfX5e6jjp2SIjtkgTWYb0TF3daGr2MO4jXNxpuL5blq%2FiYsIfUpsfNeSOUbTHib3a0nSVzK9ULOY8UwRB7cVFxWPaMxrwUVO2PXUslMYRlauREXsYr1DcaTz0i4u7KbOhziTXIrmHvzxLSBffQNnqyqPrNh8YIpWlgR0JorvxNEt7WTOogPlwuj6aWl2yCfMnWibIYGl9qIe0%2FuWMJyym70GOqUBWWFNowjhNpv%2BqgBH2rxPF5F1ZSJpRfxQssFkWP3%2F5l3h86aLnKzm3BBDX6%2F14pjqD%2B68w5IlwuUsxJNRQJIUldT27ox82vdGEYtNGdpDD22UsyOVqzx6902YJwSMrE957agj3ddwYh0%2BzHCDmTB8tdES9f4ykqgWWZTAydkoaBs%2Fl9AtT2i2t9yHOvg%2FLEnoEPP1X5lfWN%2F09koU199dolxOXSfg&X-Amz-Signature=40a3919c3949966cf58a5be622c16aeaa89ee4aaa965df4fc40b8265a4150341&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SELHJ74I%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIHDcwOehdOsMkr7wDLwJ3770xDc%2FzSHC8fVFqIfhuGEGAiAfWuF4kGRQevYGOlMw9OLUhilxQf1DjQ9b%2Frg%2BQq5AeSqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH9b9p%2BQCYezoQqJMKtwDKshDOubvnLu0%2F%2B3Qakz%2BfzvWop%2BRp4ZV5KWKjKGoPCf0PjYe6RqVnn4%2BkGl8FGQFXnFfxkP4LurBYareBYlOHlcyHjMevSt3OOVa5v7Iv60tvbNCRG7HjBs0WM3ZDAjO%2ByupyDMpXYVe42LcQohgaNTxBJCNRc28mEXYryqW137wc6efLfZWJdyA8G0SIhLlWVYr9MkHaNYQCATbzY6vqrNBcFVnuhRWAWGRx18HzTNvPg1kBUi1TRLBLLmTNd8j2pblJtuEeCgPQ9r6xevO%2Fm%2BKpypqrxtJiL%2FMPQx58TeEqIvFjgVl7YaHOWGjtgJ4T9tCNjNVg1xGlsYbeBbJcQpFsQaTZKv0VAi6yTQTT%2F2F6ctLYU8pU4EXK8Zf7ohPA61zYyC4iPoKBO2h2WZiCS86GRS1fv%2FIhAV1rVIWd0VQijbcex2o4R3XwLEJeqCNmno9nJ4i3Ov8qX0AmhL08b%2FAmUne54lBnHgolzXtgAyVf%2BV5itC3Fl1rRuJLVImjlKdwvXGH0SRbf03V2z8xFTn0PqNsEzD6sPk%2FotP9qULVw4JXoAa%2FZwzlRrDsrk9HaYapFr3Kqcyi%2BjtKs69H7BulvWEErU6H1ZM4cEO7DiqWiYM2opEyAjSy1F4w3LKbvQY6pgErtSvNT0jMutXtxVn%2Bve7wIoYut55FPKo8Nfsh430jDMSjPZQMlxeS059GiiuUFg7FXFA97TrwNLv1w15dwcwQroBR%2FaTBVHRVWLcHQAnMxwnZSgToyZAWWz8euX63NsALP4tOTzGS699LbwLimY5PbHfPvp3nlEb6DQW%2FETfDHQfk%2Fn7Qii%2F9yh%2F%2B4QJX40ehFUhbGntUlw%2Fh5vVHkNo6WLENaYu%2F&X-Amz-Signature=6d12a9941fa5e64efe6baf70c98484fc8f71b50338b1882d747fbbb0c1eb5f8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2ZG5GYP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDV1RvcgevScJeNZXWOKdj98DFuf%2Bm5p%2Bl429B6Ks3xsAIgeWN39xSuPjHlFWcr6nP7Jnm%2BXHp6vWoplmsDYCK6ONkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZ65OhzNYsnjImsKyrcA1e0FXNtONaJC9oSuhUHGM0Lh7e%2F2pyC93EsqnOSPO5pqEAPcm6uX8Wuu6Vt9pFH%2F8dHkcCeNvOLBdaNlldx9u38sRddUIPHFnpP44rxcZvbbVpIGJ1iqzkaj%2BixcbOq262lFjnjOirNzy3hR9UMbyikffDtITwohd5BZrXKuCVeST%2FHB%2FvUo1MoC8Sl6zvWxPkcSHOj6m1mD7%2F627%2BbfX%2BlLWtwLJMQwCwQELMNhiVjsnYyqW0SIMh57Twq1bkcJXaNfOoXJ4f3Wv0W4CiyBkM6EFEEaWCeeLI2yoOfmkXKnyJnkuOPJ8ixPt3W6%2FPFf9u%2FQC42mapMEhjeCe69dj9UHfVCdJg3%2Blqs1bzzrHn45CT%2FkG9hmWjadJZjc%2Bd8zhvrCJnp95ON7GE22DpM4kCbcRrSF%2BdbQDT3SIUp3sC6GiI8uEUf5DFVh%2BQKrfjBJYLlOPTV2mE7v1N9pNqSYAt%2FjKQp6qSH30b%2BFCN%2BDJb1gE2v%2FSaynWOXReV61wFgSegS7n9XUPkZEAlNsJbwZVPYLsJsmbNmiM%2FIbYzdh5t8faGxIQwmpiS1hCeWvuis1C2XPhK%2Bdos1o8dV7DJLXkfOR%2BaJ%2BhXPSlwk6Zm%2BJwQuL1mUQzcPhDKW%2Fe8%2BMLuym70GOqUBR4NIyKhDFDXtZeOe42ul3gVl0SKapYvxZgBPu8XqCASHOqpoXFaxfJwZXG0unagvHU8103%2BRv%2F72k8ME9ELWkQ5uW20DfrxyqseGrizkB%2Bcyc1WsGmiDAjpCpNyegzRAeVS5JMS1xzyFcQiOiOxnGM4K%2BLDOxnYu9JKQbPPVyWpvPyO0crYKGG8QPS5eFGd2STthlByUggoOJy9Zq6Z1snPk5Z3P&X-Amz-Signature=423a4174e7fc88e29686e2c5b9ffe43dd4141f41c397290bd5687105ec427cf7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM3LIJ53%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIB%2BcbwsLhHtWzvNu8kNOf8COb9VRBVNcFdRdvjjfmvtcAiEAswCTy%2B9wVHM0lxfz%2B9q9dEM1s5gaGZocfIw6CuDyisAqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOjVzjgBAeSrX8NKSSrcA%2BN5fHUZYbk%2BBVMbgIEvopQllvzUiKLx64qdU5pwsHsl%2Bkh7xswl476s9lepMP2lYBW9CxlbeUq9qQYpN7Ok9oLhXZch9kSrxXkY2ea03X%2FVDiLHWUpWD6eA%2Bp52QGkfD5GL%2FmRAWnk9HNbrQqTIX9veqpe8usKI8%2BwuS2%2BaY6iYZHFSPa7b2kCQ1Y2yL8c9bzSlyUbutCuQZsT2SPXEI8yY%2FCUn6f8z%2FOdkFmtLPvH1uVpX5VQOdM%2Fs6iUMfVKB1EvvMJJ9MrWbwFUaIP7sUgbvwY7A6%2BoGh65YQaRHlybOFJh9WdETuwGQfPQb5vOGR2%2BqdgHiAddT4265UxUGahuWsAqc8Iwhp8SJHFwNn49dxw7LOiXBG8zVqBh7Tp5iI%2FxlYb5PEzUzfLQjiZOpuqyq%2F%2FJAI0jHftCq134FjpKc5r7Q2x6EOtu6RkKCwOg4XUpmyXCloGqYgXGDVShrvBW6jekMfe6RlD%2FhIDGtOHcm5Mj2%2B%2BvAfA%2BOlimSZhfuQ78fDQ1cLg63JxyRX6nwccdiBaFzvqFUfEt%2FvdLRi5akWoov6nlfl53suDZY%2FDLE3Y%2F2T%2FlmhUC7QziZP%2BxbgFO%2FHU%2BKw6RAhxETCxVXFqnC7pRt9d2RWqXcCBfIMJaym70GOqUBUBAo1cqaGD5dvXYjzfsPgG9%2FRfH6Madl1hSB%2BZzaotr0dwW7foJIJrAcix9CidhLowPGUpU6uveN%2FmGlzDWu6xBx8Gcqnz3%2FBtvO2ffRT0H2hl0188rDwW6V%2BF569GpIvlDhxGJW8EhMHRY0rb5CUHs3qrdQnnp%2FfQSBba7CFR9AV%2Fxh6CmJicl1xcO1vp9viQ9K%2F6AO2NxB7fQQh%2FYF8OZo0mmN&X-Amz-Signature=10b6e31beb4459d8a74fb25f4bdd588b65e25f62e79e946862862e12621eb131&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UERBV7NK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCmE4Hjs%2F5xaHSajBDi6%2BdrgUBNk6omJKFHGvpTi9UTrAIhAMXWirkbLEz60xwqJ4IV1Fa04INl99QHCQk8xUmiDQ7qKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyi2HOKZ40HtWEPThcq3ANkGeZGsdcqDjP9W8cJlTh3vzgTsQKvZ7WY3VoOmAS05LRf%2Fuq8SjhLqWrpq6JhAeWqKo4qrpuELoeGgbR21RtxZMNNkAZTCAHEoZjMeE%2FpLz2fIshTT%2BBaAjhUAahLYI25SXmiovSBnnxoTqEwMy7UfgmnaWMDL5V4QLZeIQnu0NF87T1g6%2FvHQ8KyW32bawDhOMJq3wp8AxSYoIYeZYeCEjXODCGQM0FJhflWMvvXip%2BoVc72M%2Bgww66GPJaFeiI9wi%2FdkZ%2F9AA70pu3p6wGPKcJizOPuCR6shI2OUDBAxIhChiJasFJAtxn1driB0df3IX6uuoxUcPKPoRgMmvgTuDYjDowavGR0Ot%2FlpCx6SVhC79oAgoC4IXQs6epDEOJ3kVzmae0Ta4vdJ8SpDadsUeLfF85qTjA7ZJ6phJTmy%2F4OiU%2BPurzzb5gUlcUFpe9OC8J1R%2BdZrsDsmGin3iCs3aMbjLjrCqkF3lONyLM67%2FM3n4acn07%2ByC81QqZbZMcmJAgxk0bNvFbn1EkosoTA7TpkydrrU%2FpPB28%2BBJrqh96bzRtxT5Jj6aAGAg2RTQGnIiJ386jVit7UbnXQKAE5AfPorie3LBVlEo%2BA6gf3YJ%2FbjPRhGj9GHx9KKDC7spu9BjqkAbupWuV7ppEpPLVEkG7D5agN%2F1fum9fd5o%2Bs3qRhOcHIl3SXdNpfFvH21Vzd0Ci%2B5n5DOWIlfPBQMhr0bdMYKipIpufhpGhmfImy1VVtVcVrGJc%2FmBjQnyIQGf476vM8yAASa6DYnlZVljcZgBewce1DavMDNO6hLFIrAbAD9h3ArKDc4CnqbHhCMn5gEs2G7L%2B2u7KPmHLR0mtLYLSIzuiB8UzW&X-Amz-Signature=248848c5f0c02931e5ce5dead239398ace4085a205fc56a62f3d650599ac542c&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5TCNR2F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDYC2nOX7N34VyGNj%2FGKPFeXkf36x%2BRd1GivXl3KtcZwwIgTn8vBNSxdft56hIE2%2B8aOdZ7ExfAgfn0ACIkevLnQgIqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMVac6%2BGLT8Nao1NwircA%2Br4tM8jEZYIRoG0p5%2BisCrtCHpv5ckBjX%2Fl3OzAhVaJ%2F8bA1pVXyaCooVwfrDS76xiMgj7LcpEd49AUzeGKYZbu90oR4wlXCJRBHIc1JWaTmKGtlEgV5i0ojaRXcaG91ymCr9Kupnpcl8%2BUlTlxhIOb%2BRBFMxo8mP4F0QxqS4P2Pa9EKKumq26hkQHh6YWhT0GpfQnxsj9SvHnl2PzhaIpLjgaSSGECgTVtdtvBVMPfAaFqKA1Pu0JFkqCDnBdVGUUgF%2Fn%2F1cTXVd4zF1u99iXgwIVNNZocx649cZfPwiCizUGUV111YgGqtNpALP1q06oPBQ1J945lblITRZVaaGZjc9j6g8YIzFZuZqtQdUUWwSm8hI%2F5r2u%2F3q5mniG1j1lSr39f3FsYoRXr%2FY2VzztgTAnRTbutM4e4Pxw%2B9Y7XX5jVydG6CNVgnz6KlmFFWiPvLZgkStOynqlCxzPiZ8XrKCRedM5bCs4IdAEZPtsECrdBO5DflQxvi374CuSpmYMkq89aUK056R3d1tjlBzzCCVe6mP8QHu5ogP3NJ%2FifflsHz%2FqvOFT4r79Kyv3ipnLjawDUN3j9rRMI5LVRBpSgNxfEm1JD3mVufIGHOhNsB9skHtRpuBjbf%2F08MN%2Bym70GOqUBvVlY4%2F48QbaMkbOzLJ2p0amz7B4TEhzbTdoIPit6f9es5VIPHHQYwh6qsRg%2FM5dB5sETqw4mda1d98XvyLvFMZX4N6aQUj73%2BLyAc2ynwDlBl8E2SiPW1rqrY1Y1VdT5ajYs1lSB%2Bz%2BXiU3be1FQqwAVWVHbot0vjAQsjxNQVTTL7znQWuPtFHfGRZ6PfSvRgPrOz3hszAM5vMrkFSQd68icUEM2&X-Amz-Signature=6491cc91b7fa3ced1f5ef1d2a2b784322e52cac049e04e142aa678e99af23728&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2ZG5GYP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDV1RvcgevScJeNZXWOKdj98DFuf%2Bm5p%2Bl429B6Ks3xsAIgeWN39xSuPjHlFWcr6nP7Jnm%2BXHp6vWoplmsDYCK6ONkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZ65OhzNYsnjImsKyrcA1e0FXNtONaJC9oSuhUHGM0Lh7e%2F2pyC93EsqnOSPO5pqEAPcm6uX8Wuu6Vt9pFH%2F8dHkcCeNvOLBdaNlldx9u38sRddUIPHFnpP44rxcZvbbVpIGJ1iqzkaj%2BixcbOq262lFjnjOirNzy3hR9UMbyikffDtITwohd5BZrXKuCVeST%2FHB%2FvUo1MoC8Sl6zvWxPkcSHOj6m1mD7%2F627%2BbfX%2BlLWtwLJMQwCwQELMNhiVjsnYyqW0SIMh57Twq1bkcJXaNfOoXJ4f3Wv0W4CiyBkM6EFEEaWCeeLI2yoOfmkXKnyJnkuOPJ8ixPt3W6%2FPFf9u%2FQC42mapMEhjeCe69dj9UHfVCdJg3%2Blqs1bzzrHn45CT%2FkG9hmWjadJZjc%2Bd8zhvrCJnp95ON7GE22DpM4kCbcRrSF%2BdbQDT3SIUp3sC6GiI8uEUf5DFVh%2BQKrfjBJYLlOPTV2mE7v1N9pNqSYAt%2FjKQp6qSH30b%2BFCN%2BDJb1gE2v%2FSaynWOXReV61wFgSegS7n9XUPkZEAlNsJbwZVPYLsJsmbNmiM%2FIbYzdh5t8faGxIQwmpiS1hCeWvuis1C2XPhK%2Bdos1o8dV7DJLXkfOR%2BaJ%2BhXPSlwk6Zm%2BJwQuL1mUQzcPhDKW%2Fe8%2BMLuym70GOqUBR4NIyKhDFDXtZeOe42ul3gVl0SKapYvxZgBPu8XqCASHOqpoXFaxfJwZXG0unagvHU8103%2BRv%2F72k8ME9ELWkQ5uW20DfrxyqseGrizkB%2Bcyc1WsGmiDAjpCpNyegzRAeVS5JMS1xzyFcQiOiOxnGM4K%2BLDOxnYu9JKQbPPVyWpvPyO0crYKGG8QPS5eFGd2STthlByUggoOJy9Zq6Z1snPk5Z3P&X-Amz-Signature=c72ec538257b6711ec3672a7d5499521b03a28913f45e4309fc2ab419eeb167b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3NTGKWA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCCBBWNnkKxsVawbq5wccBsKAo9RXlXY%2FgCCJGurHJjcgIhAPnCTtFXc%2BnbyIVeUv2A9av3vgHUFleCeE9pw%2BdMkuH%2BKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVJk1yOJTz2FoKxxkq3AMELX8RpPerl6wDXa551tYJ4MdXgrf48hbS1x4T%2BN8SFttPcolMeVuC2fi3XqYoIRcqv7iAKhb8iwoaht0FEjSILYWT48ejFQ2Fnm0LITT80xCw5XIAVjUolPir5FuOBEq2%2FU%2B8S3eNicDGZNXlu6iZlFmN3ktOMRAEqv2uTCHu0glE5U4O%2FiCWtmwDBEtys11K9hJmskT7m%2FSJTKIRiDPbpepcSPtOxx3TIA6iyLgy8LX8mkfQ7NsaLBf9Ie9BXNDvC4NRRRVFI3UcG9jq7uPv4fEk2Dr4D2g8YYSjJq9KoRJllHsn1hg6M9SFM09d%2Fcm6eBqQ2JSdKfeo%2BQqnGwzW9%2FIyIL45PENAL5oRx1I2KrI7yFV0b5doZ30KSGS1RbrpR0uWj9dY85BPLbngochwerVEVIxiurt6cSKHc3NsvQhbI0yyJM0PMcEXb8UE6fGjxWY7B1mnah5g9A1dg8c6FU54lJsYAFTOACEYDz6lZAqheOLw%2BWigAOTQYCsVtw57kiw8F%2BHp70BJvEQgW1liopEn3uupTsG923LiFyujaNiNNXVhzNQ129DFfShvZsNs6JjP24IA%2BeECgm%2F0HghAeQTzApgls7bG99xiR3xh88I%2BRAmAjpFiByLDojCNs5u9BjqkAb%2Fvw%2F2vTg2cKrIQu%2B06QVafrnuDVipTFtHKO3SM9zr%2BoDSp7RAxAHPCKKaN%2F6hiXjOsRAAZbtxpc%2FnlJ2FqCp9qPw2NuhuDoJ%2BqcsiJKlhzo%2BTDBsKS%2BWGvBGqLHvnF4V8M75D%2BCPVMrcdxAt2NR1yExWVtcUCjQ0nZsAvGMRieygY4p2cPvgG8y3Mt%2F3Azt3KUbs%2F65CcnFhHoxrsOt0E7XOcj&X-Amz-Signature=535e05cb71d6f9a5140bd87b4f50200f9c6feaf1fa9e452666896faa5484ddf7&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3NTGKWA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCCBBWNnkKxsVawbq5wccBsKAo9RXlXY%2FgCCJGurHJjcgIhAPnCTtFXc%2BnbyIVeUv2A9av3vgHUFleCeE9pw%2BdMkuH%2BKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVJk1yOJTz2FoKxxkq3AMELX8RpPerl6wDXa551tYJ4MdXgrf48hbS1x4T%2BN8SFttPcolMeVuC2fi3XqYoIRcqv7iAKhb8iwoaht0FEjSILYWT48ejFQ2Fnm0LITT80xCw5XIAVjUolPir5FuOBEq2%2FU%2B8S3eNicDGZNXlu6iZlFmN3ktOMRAEqv2uTCHu0glE5U4O%2FiCWtmwDBEtys11K9hJmskT7m%2FSJTKIRiDPbpepcSPtOxx3TIA6iyLgy8LX8mkfQ7NsaLBf9Ie9BXNDvC4NRRRVFI3UcG9jq7uPv4fEk2Dr4D2g8YYSjJq9KoRJllHsn1hg6M9SFM09d%2Fcm6eBqQ2JSdKfeo%2BQqnGwzW9%2FIyIL45PENAL5oRx1I2KrI7yFV0b5doZ30KSGS1RbrpR0uWj9dY85BPLbngochwerVEVIxiurt6cSKHc3NsvQhbI0yyJM0PMcEXb8UE6fGjxWY7B1mnah5g9A1dg8c6FU54lJsYAFTOACEYDz6lZAqheOLw%2BWigAOTQYCsVtw57kiw8F%2BHp70BJvEQgW1liopEn3uupTsG923LiFyujaNiNNXVhzNQ129DFfShvZsNs6JjP24IA%2BeECgm%2F0HghAeQTzApgls7bG99xiR3xh88I%2BRAmAjpFiByLDojCNs5u9BjqkAb%2Fvw%2F2vTg2cKrIQu%2B06QVafrnuDVipTFtHKO3SM9zr%2BoDSp7RAxAHPCKKaN%2F6hiXjOsRAAZbtxpc%2FnlJ2FqCp9qPw2NuhuDoJ%2BqcsiJKlhzo%2BTDBsKS%2BWGvBGqLHvnF4V8M75D%2BCPVMrcdxAt2NR1yExWVtcUCjQ0nZsAvGMRieygY4p2cPvgG8y3Mt%2F3Azt3KUbs%2F65CcnFhHoxrsOt0E7XOcj&X-Amz-Signature=bb0f03ea7b86b23d3f69dbdbb6d78976b4013a0e02402b94c1e83543f924eca1&X-Amz-SignedHeaders=host&x-id=GetObject)
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