

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBHLKKO2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDf74Q86dvA3qSRKOCCAAun30odXXGqftsKJTNqRmCDRgIgZi6HljfURAao5O7G%2B10xxCWYdxsYM0ToTPDcUEw%2FRo8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDO7dq%2BcMfFUAKX3sXircAzB2RIaRM0fY0eHDiJoD7REOvjMeQm2mugxy8lEq2kUcMVF1SMasCTW%2BsRfVgIcmtZxPrFVQg1LS4SK1I4SrrL34etdJvYqgISE%2F19G3UwBshbROrsJUf9cIQ5HhBRIGhVIbSdEIbS3DP4SFF61ZhBva42sRk3EJckfZ2dnM5XLNoR7SxTHWmizPtVZFLz4sCManlfDe7VlWK4TBQwzB6tsG6YBmrY5gXftwrsVbhBRlw3G%2FC5VblAYDqg8LSS4OQRTgKvrHW3cWKckGcDIEHXF8mnZS9%2F85vP5EkagY1q4c%2FJS669poFRLgTdGsdyj57g7rqzrZ7DOoxf%2FmyRi9Os62PeTxpLAJuGgUlsStqTTPiGL9YvWERVqa5Tbv3HYAwAeMG%2BHfGBFff%2FSLDGKS9v%2FAYUWvecjrUOw16ElETHDi2Zo06inbFHwutUSW8ke63xEjA66gRQXhnsqFgSYajJmmDKgFriIAufXd5hRkPD9KxT6Fb0vp2HjzLoCAmhLBoU4%2F27zy6r23KcispeTtci92Bg1vHiVnDvUYdAD5W2ZBl3IabfVMAdekXJ%2B3OwvddIlhVghz1dppls%2BBf0M0phtdZ%2Fs7oBGihMtQL3gj%2BkRh1cixN7bWVG35AfWrMJialb0GOqUBmOXTBUpfcJdOA9Vdz2lsUdQ%2FBVg88U7qPMqSg%2Fk3bEV7ivzm009Ol6QeNP3Zyj6iGmplSRKrKsjvJrTh2z7sDCJQIqWKm0LDvugVMWjM%2BfdEU7GMnYGH32q4%2FqBIu6n7QrQUq8%2FTqxoWIVG7cAkbeFOmsMIPF1zKikWEJm27nKK0mD5ylg0qfjeRzaCh1%2Bs6zuaWAYEl9N1awSpNKO6bj76FaCX7&X-Amz-Signature=e75e50432376ffe517349c446fda5d31f6c26708c3f8174fabf849891ec0dd9c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466537MZ3I7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDYi3FDbBednDNrQC%2B8d2Wg4hLWGFCBWe9x2c3TlU8LDwIgBwIvnPZJPfSukmXMmgbV76mw9hCRWRsx0OJ7E1CrND4q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDY8ExhlFdEuDy%2BYkircA5KKz32gcxEc59K%2F09F1xfxSJTF%2FPwdrLfs5xdLvrdMLeTgXjufAEdMar5ECPjKI6jZXoujVhyfwXH9ZcOwFZ782x%2BkkpUN78NA%2FNx%2BVG9YcyggHe%2FMqF0ZcfEW%2FpTYkREwVMOatgAN5m1BxoMXn9MO8Lsrw0jP0oVaiGQrgJdBuWid0w2iZMyfo3xbOQtyE1kIEgWo5E0SB6jA4p6GZLxDMnUpmc1OWYVl6uEibYwUxcftICS%2BUpSJpIg50LuQksJcbNyv25ObCgl2Z7PiTALUMrwxK%2F8k8Zc2zYq6sVYf7mWCWt8egfhU%2FM199aoFr5jQ5kKfxETA510PCISEW%2FHH3077kiMNYb89A7A40WiaZI9btVxfxZBSGAsQIbp28%2BTnl3YCgKY%2FLWEhnSX5J7PqnBA3L919CQo3YFpXgrdCKABJ7%2B%2FfB8vsi0PiqIVQLg1LUph4RDdRzEr1ImdyXjjeX596Ze8%2BIY9XstGi8qDH0AGE8DeYbFztY6cY8Hkx1CYT6kp48TgwNxJ3C4OAO4pbYFAlI%2B%2F%2FHUJUb%2B16QHLQQVIqQPkP8F4AAsAz79Y91eTEVmAPsUf9fhhoyCwoQWVk5Qekp9CNVZD4JiGoAZdH38WNjx1Em3jtITyd%2FMPuZlb0GOqUBt1PgAfvYjLG6Y2eLRCAwS043HM%2FaND9rR8z%2BA4C%2B2X2KQNVhdjX6vh696Af8T6AAIjwYuYf3Pu0qHUPciXm941RIpf7IXLoCJy55kOVGbxRi83n9qpG2CZE3dwYPrS0lLgTAoG%2BoOUCL9kMb1Z4JUqmUyArq%2FnJarNSyMBfugjbI9tWu%2BIeoStN%2FGmyBXrv8qkT%2FSnL9IOEpwkkb7jrEy0Rx17%2Bb&X-Amz-Signature=e12ff68355a51f2f132e3f139aaa29f931262adeed1b43331628f16cb8c2a57b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BLUZJJ2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDMq%2BdWPFKYYtPpKODAWQ%2BE0uapGzADN7OcR2Uhx5sLXAIhANW167KUzlL2KPd4TnUMmCoOIcK9G1ME2jNTckJEVetyKv8DCGkQABoMNjM3NDIzMTgzODA1IgxZR05z%2F6w3NlIAF9Eq3AMUx%2BjggWhunQJvNbh4bVxNnd4sI9pY4rfEdsD01FAP3BUkfawTrV20%2FFk5Unm8H1r5DAKmKIZl06QV66fd4gd1RiGz18aet5Xb4yHAawsd98rKZaKZVRAP43jYfIzXtQHF0FKNqYWk0Qc7YACL8yQry6VsUo67EG%2BaaK%2BkzLIVtbl3hHhtWMKUv%2Fkl43fEqf1igqbv1kZtlX0oklFV%2BFldjRgxvCi5b1kf9oP5ErYUu0ibtYLuxo47PfRV7uX4xbtY68hWcBLKV9%2BA8izScJy%2BviCpI7aBUDtuCgLgKKLfU4XSrz9lPPvGEJGFMnuq1%2FkQ4Stsmv4wecszIgUXblvxYob0e3RtTVE%2BWfnlu5bIPBDI18PRDxeysMdm8EZN%2FeIY3%2BKJzsoCQ2SrmqKojtTRJAZrASpVr1cfvAf1kQhcruEgUFYKkEHn%2BSQ2bT5blkFvHvFKvahzUnbCsnRjuzKFOByN3rOAd75mw%2F%2F66CKSAoNdnS2QiH5AUqjEmm0TtNwh7S423UowOi6Y8XitnEpbknYJfBoc6TgphGsRsz7SzchTwKNs8zJObgpifHRpfsx3q8%2F0olfAVOjjSaQw3gkkjqZm90AGFzZoA%2BGzj77UOTg53krRsJ7ngvPw8jDKmpW9BjqkAd%2FXyfQYJ1xWZXq2ySJdVlUlrP%2BF0VRL7n6fBjG2k1soYfsqcuS8vrqY0m1BqsRYpe7Jc97rvjTKaC%2BNYt%2BMMEaf6VHIXKiWIGuDrDEv0fX%2F40dW9iwOZV%2FJeKV%2B0mMbxgMoqhg7Hk2jEx887zy3ciObakEpua4Aasi%2F1VFhdmmWGaRhwypvilfyctEgLpMo%2FpmhVUU4SOphPhz2aKN36WlSkL8K&X-Amz-Signature=7659d16528db3d497e9cbff63214e709971c981c721e7ce4b2d93b01a699b608&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXCILLKT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIEeaABf2cnvfJzudWPMefQ5KuREP4Wi4MHv59KJH9R%2FZAiBscWLT7fUgkdibrxXOYfRNNT9YLfLXDTnXbPMkNeklcyr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMr%2Fo2p2G9SxA2ehVlKtwD7zhOzPBtWsoSlq%2FRJZGNBKK6cT%2BwdtTmb6ZSSDnNyF5OBpOZBnwNFYkWyrSZRMdrLJjE%2FZ34fynnirPsXBhFr0jpyKEXDtoBhFl5LIhfSsPNJ0zkAWw9wKTQXxBaC6wxVjbuOLN4%2BKh6%2FhvzHYu94DOLmM7urhdKHH9npOp501io9mZsSOiIQZAO%2Bi4%2BujOmrN0zGDf4bL4vQRJ7pmwTy%2BBn4Q8WS3Y%2B1dKHhWb2Q9PymSGYT%2F2j8di9ivwv5lTbXVpgGBjLXt98TOinQnM%2F7FXT82nyr%2FY94U0BCzCM1PfyFtKljVY6GuJOh2xj6pWgFVbeAiv45NBEZoN%2Bdj9mawyL4IGfKOEqDDMLDLGCX4vduacTOS86lJbnoulEDBNy8iZQNsh%2FM2vQ81TPMO3YA4AZvNixLyUra7SAXGImrepv2c2FI3iPnN%2BNpKbefdPzmlxvkR3THgkDMxhRFA1DY1T7ZBzGWb5ElgJdnjcLo%2Bv13BjC5g2hwgX9hkGoFJR8RiTbftVLR8o8Ig3GnKQHKc092D8iJTqXhMCGvEbYNtKKpod8iPTdaVALNcKcxKKmurD4IJqxDdBxkYR4DT%2BI%2B8Y4CH9p846Yd%2FAh4SczdqYzuzhO3WmwYIYb5Bow%2FZmVvQY6pgHMDhL7M5lv9EzephLKAPsoVbwN%2BJad4Ai%2BpDN5QE5%2FXXsH0y9ty%2FgPKNnvxwdNbs5yWplpUFYCiwgjpF97vkgMNxlkzuMV3L2scyhtZiq5Jj53w3mIFQdg%2FWaROXlWCum5rMZK%2FJ601nKQM7v9Md%2BMENzffOY8nr0TkTB5X%2BQ%2BTxXxkEJpOBUTtm6LqBscsVTuOinxf%2Bcr9%2FUbdOVYAOUH1jacfFiL&X-Amz-Signature=f38e8f98ebb0d507b018c565e78841c3ca1da5b28c0c5c61c23fdf2590d4cc44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UFRVKWU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FtnGB%2B1QMM6CzIF1wc3qBjVwgmnJphZJ44LnbKinKgIhAO4kBY3ut1G8XGSxYU%2BYZ6XSziR4LS%2BTJettJhjjQsMPKv8DCGkQABoMNjM3NDIzMTgzODA1IgxihR3Nbe9nLaZqQyIq3ANPKpnLRQUgpUEVJMZyK8PfwUsn5Wx8pzXMNBlKOiNqXCegj4jfCAgL0GIh%2FmQ8SlYWMen2%2FNRTOUtg0x4Q5itH0JKpJf7%2FytkM8eDljzVgINF3UadsXOdzemb4dgVBJJa%2BLhayq%2BeISEnpL0DJGp8ggaSfO%2ByumPTHlfuIfhjj5L0I1OeTT%2FgcA5l%2F76yJ%2FpHFZeAcXXenYJVz%2B36cTZ8SjxeZzHC1lH93Ns4piqzPK0MSwKmSMnMX%2Fo0%2BY388Nw5YXIWXDgdiXIM1%2FXb%2BHGW4OZZzBQeOeIfu9ACzS44sWJ03Ll888ftRDY9xj6RTrY52ba7vxbod6eJEPDMnASAj4FTWze98xqvqWaJ20NB5TKLhCIOd3eghO9Y5MAreeJdlIwEvdKWh1qWE0hWh5ky4RmjbJwJXLLqyKpuIyX1HLzBjUh1WZemDyfdmHjanM07V%2BjRmTzhGVFxLinnRZJz6kPxrxpILCVPWP%2Fjn26GWUYFUN%2BnPwYeth4fQbu%2B0d5jIiUaxHCErRikIT8ZbjHnxieYrZkJ1LyksrV4J9Wyls3PnuFgwj3Vq2mIaBUUfyVaIQMISXtJPIRXBJY8U2khpKGwrkUzWb%2FbsBmmLtxYF9qUrY7ni6KouRfqfIzCPmpW9BjqkAQslmdBdnqx8QathKvzxfu6BQ%2FQkdsvpvysDt0xJK1xOLWimNc9JQAEdaVNWk8wHfqKC1XKt%2FmBO98cH1UUWkS%2FOCXpnNr1ZnABVJpy8%2ByPLhoI7SiDzV3iLQ5wFUxsEHhkJAZ36YLW8rZrtmOzSx8%2Fy526a8jHvdJ%2B2eNyaamjqtLkwcIWHRmroT5P89keLSKw5fKtRDafIvFPtHr4pHu19mFCp&X-Amz-Signature=e2327eb8f60432cf32d2401078bac856444c299fee69b76cc24e9c6682521215&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUDUI7UU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCq0XcGrMywHdyy59OtitAN5sTJE7P%2FnfRDhIZEPWCKeAIgOC68gb8OTABaU6KZUld9WCHbNFQqWqpn1P0Uk9gU7VYq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDEtj8zvdT%2BPmK9m%2F9ircA9DuO7LoOusXOlLt0bEUD9wQtqT4LQnO5oPv3qBkZqAQEb4phjnT1Py%2F9T29VO0qwT8%2BSvRG6W2Cr%2Fvil7opk%2BbZf6XlQTiZUpsvEMSf%2F5I%2FDYmnY0IRcC3BHiafdCPmfIUMLZEO%2Fi4Ggprj8E0H9rlcwTx%2BQpzuHc83E4g2VTWLPRwQBI3kC8dBhVf%2BnIirFNc%2BMKdyW5ub0T%2BWhYqH0mRNQUH7gy8jS8L7Y67NDXLn0OEncOQNpBLb4RjMe%2FujmoDvqKp6O%2FaR6NItPXHPLcPq4WW%2Bio2iuT9F9k0yOVAiqoysKSCUBKObW%2Brf41Nv%2FckVHeCWtl6O%2B%2FCDwmbnKMyyE8efECB44a6irP2xcvBgP%2Fbl0pjxJvqroyxFsK4NVRndy0qvIxGwhQ8wgsU7NcgsbyFmVzf0fj%2F7MUimAiG%2FcwIoTm33yiSVSYa02vGtpkLe1abAk5jCMiHvk4d8v%2BPPFvamd8PaPT9J9rPESYASdqFFnKY%2Bxb%2FNmuoBSmKe1Eq7L%2FB%2BJlSfhPPQsjcv8aScT5Y4TCeol0ZfuIawbwbEhX5IaCBYchiiuhpIsEBp44yDKfjrYNHEkRONsKeAwp3kGw%2FaFt2sDLzLxhb0%2BR5HXGIQqgmZtAlSuJ9%2BMJaalb0GOqUBAKCDk1DEsS7BcB%2FHXlQcFhLtj1MgygYL7l8CCoHZYuurEHBxqexdxN%2BdzNSP2P5y6nT583%2FNxM9zlEEkY7hiNx9nzlrTo%2FWdjK6akXg%2Fcq87J18NILOrEIj4gNyR52rExg6ITLfv4T9Sv2fJQxd2nGH6zb9gmF0z2ZzMNDzD7IShRUIv0k1tjBHYH6EFJFgCkho9Zjd4a5yQkC6nvHDekxFRYU5J&X-Amz-Signature=acd2854e34bfc9b6aaf200ba3299fa756f2e760403ee2e8d6f03b31a1369f70a&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYKSF3VT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDDK6%2BKGfGuc8NcsnVu9NtRTY3D8oGIyhL0Z4TrWMUSkQIgMU3yQHdAlfIv%2FRi3nEYhack9KVKoAQrw5a6FxddRWQsq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDMidvLIl3M62RWqiPyrcA770smc5u4l1WTJPPxve7zJESCG4exB%2FyCYf2L9I5DmULtIUafWmkgehU7NX00kwAO%2F3shY3F2iDRu%2FFe%2FGd03H8VTWg9ozhCJ1WtZxlNycN80jHQLfew3lMw7wDe%2BawuP4Umr%2FeCOtz%2FcAhG0BD%2FB5Lf1FM0bn%2F%2B6pKcpXMvr1O0PlIKp1xl7TUql5AaFzGpXs3h5ZBkPrJmkNrudL2S7fzgOESgWWNvWY8DrYaocJnOSjB8D1g4uc50lhk8dizIlP2casxFw%2BIlExzIFTHaz9KA5pT6ZO6AdhjymZPYvtnfRj1mPKISktUDcleWVyQMo7nRd5MLB8G5G%2BhcF%2FP40Kf%2FWVvhMVSUCrEhTSxwqUG583pTdLnKtWNrzz3oAYschWGnt8aU%2BKzwDETdg770H9oNrBkesPdLg1Bj3LfOen90XK4EniyheP2mjokLSfYlkT2QH%2BgGUdWF1B8WsekUYapagm3gQ%2BxgxJA4LuD4C6bpD2Trfvhp%2BAmcY%2FTjSIqNpEiSMsFPFf53XPoXPmwkUUPT6hQKmLv65MD8DovGH6d1M8J2D9Gb3AZ3pTeG3mYS9ld2%2BdGGWXmUfh0wXPACRWvot2ZHjJFHb%2BzidOM9NOf1AYOq8vhhiyxu1j6MLOalb0GOqUBcaajGA6ug0LrgFawBm9v4bm7FzzHUeeJotKVLNv1ZoUYDFoQgw8RLmKuIz0oPLQpX55YA9aRt34bL2vaZ5QMHSMPctRB3zHMqZGq7D5ZMzI5pGqxDVFUUgAVaKjNMAfllv9snz2uuaYhgxkx7Z%2BMzzg6J4TaZbgJZlRAIAiaVV9%2BwSnJPufaqLwaRNA1dj353C9gVNglUOyNwVJ7DdGgZ2S9vWdp&X-Amz-Signature=a007f7f749952d97e2243dc66a59378ecb5f015a981a1cf6e3d6e3500d92431d&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RT32TH3Z%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDJUUdu5SsxAz1sRJitIcCDhEhGLcmjCsF%2BVNGEXNwplgIhAK%2Fj5yFiJ0WtcTMPKKfaujoNYkdJR0y%2B7guANec9gyxIKv8DCGkQABoMNjM3NDIzMTgzODA1IgzeYd0DZvEXd8UDH0oq3ANu9qi9FHGC7U%2F%2BkEGeJOPN9aPDT%2F%2Fzw34RvT1zuv3M%2FzuCQNkfR4XwhyCBJ8KRHP1YXVtWyhjQD0QnLLqcZ4aJAjF6FLAkFytsT6rEoJV55stu9ARuF4mWMo745rfiys3b0aEyEEEG9Sxt7Qv1o%2F5qmb5Ghlfg45ECSUR8P3nnskmmQ2cMumeiN7Dls%2FvUD5kB4tmfrSiWvsS0KTNETwktjkJXRfGXXjLPW%2BPgVokbhzsMRnZgE%2FMDCncvF600cpe6yJlpvpLPlEowsici1%2BBPO%2FgMgVmE5IFWFSbI3vienIslgn1QRH8%2BJcRmFzt4Fk8ePdxT4zqa5UWtHvV6w6ftW7o1tLqh7TKF963nUpMo6Koq94ZcR%2FNoTdUKCP5D7x6cn419Yq4kRvQcwG%2BEoK2G2LI4AwjphB31MaP8ww1XeYwd6bIniS3KILVp1PD%2Bb9Q9nHh8zVKuDUDB8eA%2BIizOFbNZdA9V%2FVAqh0XfG2H8YXyl%2Bw2FmNOIiLDDhWjfe8RSsaVJfs3R7HLI0CaHwQnrqooGz2VBHx6crOXlWPSSomhQNF2TgSVtlrkK357JcZtY6lagk5FJRuL%2F9HN%2FfYDFN6FS3I78WbuLWYOcb1jHOGyEcd8Am5jBU1q%2FaDC9mpW9BjqkAZQkeCJD7SMUUZDaKyjZwyhQXnA4AlbNTb2dMevcigZXVNRmzskBheVj9Hz5eh%2FNLXAS3H0N%2BwP75K4fhE%2FwimcPURebcdgY6exMz6mLrGnNjkOW8gw0lTnmrWK76pS%2BaWqphFabykPJPnhZUTYrfrVaXpKSb3Nb0qRekcQlSKqVHhIWXhM0Y%2F44wyMe12ur8cZnazkwekIb5JORhyj%2BDR0GUK4W&X-Amz-Signature=577500b61730b040b701bdd680e1e02b7dbcca300c4deebbf387639244f52a58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UFRVKWU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FtnGB%2B1QMM6CzIF1wc3qBjVwgmnJphZJ44LnbKinKgIhAO4kBY3ut1G8XGSxYU%2BYZ6XSziR4LS%2BTJettJhjjQsMPKv8DCGkQABoMNjM3NDIzMTgzODA1IgxihR3Nbe9nLaZqQyIq3ANPKpnLRQUgpUEVJMZyK8PfwUsn5Wx8pzXMNBlKOiNqXCegj4jfCAgL0GIh%2FmQ8SlYWMen2%2FNRTOUtg0x4Q5itH0JKpJf7%2FytkM8eDljzVgINF3UadsXOdzemb4dgVBJJa%2BLhayq%2BeISEnpL0DJGp8ggaSfO%2ByumPTHlfuIfhjj5L0I1OeTT%2FgcA5l%2F76yJ%2FpHFZeAcXXenYJVz%2B36cTZ8SjxeZzHC1lH93Ns4piqzPK0MSwKmSMnMX%2Fo0%2BY388Nw5YXIWXDgdiXIM1%2FXb%2BHGW4OZZzBQeOeIfu9ACzS44sWJ03Ll888ftRDY9xj6RTrY52ba7vxbod6eJEPDMnASAj4FTWze98xqvqWaJ20NB5TKLhCIOd3eghO9Y5MAreeJdlIwEvdKWh1qWE0hWh5ky4RmjbJwJXLLqyKpuIyX1HLzBjUh1WZemDyfdmHjanM07V%2BjRmTzhGVFxLinnRZJz6kPxrxpILCVPWP%2Fjn26GWUYFUN%2BnPwYeth4fQbu%2B0d5jIiUaxHCErRikIT8ZbjHnxieYrZkJ1LyksrV4J9Wyls3PnuFgwj3Vq2mIaBUUfyVaIQMISXtJPIRXBJY8U2khpKGwrkUzWb%2FbsBmmLtxYF9qUrY7ni6KouRfqfIzCPmpW9BjqkAQslmdBdnqx8QathKvzxfu6BQ%2FQkdsvpvysDt0xJK1xOLWimNc9JQAEdaVNWk8wHfqKC1XKt%2FmBO98cH1UUWkS%2FOCXpnNr1ZnABVJpy8%2ByPLhoI7SiDzV3iLQ5wFUxsEHhkJAZ36YLW8rZrtmOzSx8%2Fy526a8jHvdJ%2B2eNyaamjqtLkwcIWHRmroT5P89keLSKw5fKtRDafIvFPtHr4pHu19mFCp&X-Amz-Signature=1c320424dd942a642a0099e61ef8cd317451523837d082529ec4bd4ee2033d10&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKKH72HP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCPz4ZbJ9o%2FxDykl1SIlLWhDfFGFFdKZYDzBUhEb9w9dQIgNKh1YdiLJ3jsBtuza%2F21Iqq8BpxJDiHYW5IxUQfmWRwq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDElNTN24%2Bew7FQ%2FnUSrcA21JFU%2Fy2bCDY9u78eYx8MdJFWLew1UaB%2Bfc0kZiNtgFkYweUG%2BTromIQrW8bXi4aMZIsmjdsqr2kvAPhqrpC6G2Wc9B1r7GEl3qI0akJ7ECibXoggXBAqZBzK8tuo%2FOtz1PBshhimIBX%2BWD1Pa8ACrXChFc9fPmYY3rrNVezFGZdKhz9AaZCoLahe7VZ2bkFUaaP0rK%2FQiYx45cv8kF0TfdosyEMxU5J2xAPpICtyBWEe0wp6Zjo2XithLC0vNe6YXC29BPvjBimGAt6CN%2BNKN62AlyDbFlh2EUefLJ1jsfwWZ3kITwW2QMs3R3MaLZF8duy1xrNy71efpX6EUVhrKpVtLq3bpZsbWhp1aiqoJyzIm8xmA2XcCzLc14H3418MWn23DkJnVQBtvaM%2FB%2FA0AofBDhMwXHamnnxbBFzaALfzkb33VypcnWhhy6nhK%2Bs8ygGHtzSzY4dvmrgSctm179aUaYgu9LSrIN99p6XGVQwwjzjGnVK1C%2By%2Fx6LxEqdw5j2HC7G9XEwtpnAaV98rtbf6AqW5O2BQMC5syGRZiRaEBS4gTgojvngQsp92v%2FOKcniIa9cqSWkiMFlfmvTQrCynPYBlxhej38MeD1%2BZm2mrUkI6bdew4PfDwOMOaZlb0GOqUBN6axD5Xw5nM485wXK7KSslIonLyBWignasugM03hYVyiSFrDBGntcjBC0NGy%2BWIUVVTEwQaVQj5i1AiJjPMdPC%2FM0VXr7FrQz91xTUMp%2BULhpENpJN11M8sbEAQVDJSWL3qQYb3aP9Gjwm%2F8eDjjZYmPEP2PWVCTRokhVM%2FcTqxPDQshoDspeZ8e2hxhvIjmoGIXdXYK%2BiS0tDZzgZjo90andOoq&X-Amz-Signature=3991069ca183b4f0029ffb9a57e77cd3e81a3ced1c26c1d705cef7220075a05c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKKH72HP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCPz4ZbJ9o%2FxDykl1SIlLWhDfFGFFdKZYDzBUhEb9w9dQIgNKh1YdiLJ3jsBtuza%2F21Iqq8BpxJDiHYW5IxUQfmWRwq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDElNTN24%2Bew7FQ%2FnUSrcA21JFU%2Fy2bCDY9u78eYx8MdJFWLew1UaB%2Bfc0kZiNtgFkYweUG%2BTromIQrW8bXi4aMZIsmjdsqr2kvAPhqrpC6G2Wc9B1r7GEl3qI0akJ7ECibXoggXBAqZBzK8tuo%2FOtz1PBshhimIBX%2BWD1Pa8ACrXChFc9fPmYY3rrNVezFGZdKhz9AaZCoLahe7VZ2bkFUaaP0rK%2FQiYx45cv8kF0TfdosyEMxU5J2xAPpICtyBWEe0wp6Zjo2XithLC0vNe6YXC29BPvjBimGAt6CN%2BNKN62AlyDbFlh2EUefLJ1jsfwWZ3kITwW2QMs3R3MaLZF8duy1xrNy71efpX6EUVhrKpVtLq3bpZsbWhp1aiqoJyzIm8xmA2XcCzLc14H3418MWn23DkJnVQBtvaM%2FB%2FA0AofBDhMwXHamnnxbBFzaALfzkb33VypcnWhhy6nhK%2Bs8ygGHtzSzY4dvmrgSctm179aUaYgu9LSrIN99p6XGVQwwjzjGnVK1C%2By%2Fx6LxEqdw5j2HC7G9XEwtpnAaV98rtbf6AqW5O2BQMC5syGRZiRaEBS4gTgojvngQsp92v%2FOKcniIa9cqSWkiMFlfmvTQrCynPYBlxhej38MeD1%2BZm2mrUkI6bdew4PfDwOMOaZlb0GOqUBN6axD5Xw5nM485wXK7KSslIonLyBWignasugM03hYVyiSFrDBGntcjBC0NGy%2BWIUVVTEwQaVQj5i1AiJjPMdPC%2FM0VXr7FrQz91xTUMp%2BULhpENpJN11M8sbEAQVDJSWL3qQYb3aP9Gjwm%2F8eDjjZYmPEP2PWVCTRokhVM%2FcTqxPDQshoDspeZ8e2hxhvIjmoGIXdXYK%2BiS0tDZzgZjo90andOoq&X-Amz-Signature=b7b36eb1a856f2682c6baa21ffd5474f56f49be8566abd126aec8db2233e3461&X-Amz-SignedHeaders=host&x-id=GetObject)
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