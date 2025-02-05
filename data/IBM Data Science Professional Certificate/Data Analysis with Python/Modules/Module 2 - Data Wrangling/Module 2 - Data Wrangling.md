

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFMRK5A7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQD3zEX0BQkFvh7aPJ3JX6%2BCByp%2B%2BAoqr8twQt%2B3fOkhrgIgZ2ebUcL2464YMReg3qD5yT1MNSVSjq6Sak56QgfyBjsq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDPOQwosE2bfGt2kKyircAxW3WuHC3w3%2BuUyr2DWDAaODB4SU7mWG22RvVoNEmAvB0Yy32IVHNapcNXxjR5zrtoSv0F%2FPLbkXEoBU3APus10VZeqRGiKsq1C%2F%2BGboZKBFYNbMwPQ0bra6Ceyk5ba18dhJ5knaL0kvBN6rX%2BErM8EwZammuoZ4jgtRsqkI6xJ5MH8dndDFZli3l6VtNyAhOUrtil24H%2BQ3rAPGRv3G%2FPmt55Wq7YeWvYUbOtAAnm17UKSzWrJTj4Z%2BFeyQ04QG%2BSZT37TaP7kmmgRFYDh6gfb5Wkeih5XMWlHzLVbqKxNCsIXbotNf8MUtQ81RfZ9%2FKcIaxXrnNh9NYpQjNLjgKjIAflvtKaqesBhOFmQAj5umXyP6AMmrXBuG1OzQeJrvj%2FO9S9skr7mVi3cFJbk4f%2B%2FHZCzHjkQ%2Bfxt9m5La89CtshrWKo2PzLVVZ%2BoJ8VyBpQVIxXKmYszDUGPz4ALwnhhxnxlJFS9CjEzSGMPM9g5ceqQa9EE%2FYCdamQx%2BFiZAKaBH6KIwZtD7o%2BsBcvjCKayprTBTFDrW4ZK51TAAGNzadAQYpIZL05PU9UbF7uWDWMO9Ah%2FPa%2FnQUM7AKrQ8RdRHk4lvq6iKBdrHOYOnxR7Ih1%2FuWKh5oAn55R1QMLDjjb0GOqUB6Wfl%2FBKvB9tAtQfudxxuvWEnq0tQ8ZFhvIfjewfxSpZLBCE4x6nSJIsTYPA4sxvkj4Z6ICOqdaKp2XLADfhBwrNpt%2FUBYXVrdYK7kmRxxMZhN0cSTgidyd67G9ZqW4vsD4Cmy%2BkL9vF%2B2b0mxVUbi9tbZAHzQQM0WgyqbmNdzi7mvNwLxmWbsy7JF4%2FhbA2KAOUCz35Wa9zVBL7VcZi1fKnYtBeE&X-Amz-Signature=fa655a9e205a808874fc9b2e3094f6c4c047916ee4daf43466eb7d7441dd9794&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ5CDFFB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIBrNzlItJAb4eQ1o3ZHPbOo%2BhfPNukGd9q%2F4CarK2g68AiAf5ZPEq7M1TiF9XUDU59i5z2o9qCvDs3tJZceIKo9Elyr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIM05OO3iZMAkSXnlvZKtwDPYN25PTxIK6I8MQpqea0v8BU5vZOgyvdQjgwNyboEomXqxCVIrf2iHIKj5chMYPtw1U98FPlEUAAE99VtM%2F%2B0SOVkLCy01IvOvjwNXbrAh6SrjCyRw9yR7XYW72c1CiG75HR8okupJZy8eIUgfaiCQwuwFX5%2FnuNatm0Q23lXxCWkf3kMfFLX69koZd6pOSrR04Njgt7p20vTqKPC6Ek8q1%2FQd4PtcGiIcVCbcQVFSbD%2FogAmDasDluT8eX8sS%2FpOLY%2Bc%2BT0KgAsgEaO45mGdpOppSEn0m6KdYfwtV2zAOQBNBrvyUEgrpudx83Dqb49tlJhrtoaM2eYfF8W88dm94pooaaCNWxzZ5nCYAtAI1VmXM%2FzUm7OFeY%2BCZIR6BpLc5YmTRmgqRBg09rPYkoDvVPzZuANRYumQbVfBFVoJASlelSyZdKcftem5VSXu%2F94xEl0xhjAnfXi1FxrV1jS%2FOispzyJuf7mZ9VpOOtslkM5KA8C2PEUrry2k9yjTNUUCiagWCdE2EVwOYpHLZ%2BCb1GU%2FRcElRD8tmeld2sZcrtIDC99rdHxX6DRSlIHLhS1E0P9yp%2FASpiaKSonZi%2BlXOTRQXByN5h0Y%2Blt4iWOIbO9TRopHM9sC1Inf7kw1eONvQY6pgG63LNfwNa5dV7ax37twiwLH1YITYVGl9wmdr3QBh2CKe5CBv0bRdp7nhfxPmw%2FGMfI6itr0CJzufhihyztiUxlmSwhCzUj95bFxjWcywwsugANyWUakRMfsWOkcN%2BLXCumExgbB2SI6jN7QSxlt%2FFe%2Fdjz%2F2e8kVUKc6z4l1gokqd6OmCA1%2B8TB1Cu9bGdogVU8EaxkdxGN2h58uHm2XQ1h1UWZKXh&X-Amz-Signature=3245e57647aa7168d9332277a83f7d70e38480e0fd8c52be647b24d6f9311416&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAEKJP2J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQDJHfnSkkY6svDdSde0lt%2BdtED2HaUPeYVAaOo7ZyVWkwIgSp%2BHo86WHUW8nBdycfFCAUwYAFWfRFgcKgKyC6tAF%2Boq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDGglPFv0zThd%2FVCEQircAz%2FQPbHdG5MIYrENzfoVKGMmT0O%2FfABNoXrh9Pnb25fb2mUR0VQJLTZib4oufj7ecIW%2FQqL0lqdOy%2BZbPmjU89Tz17c%2FVzJF3b9x7BzAVvWd0%2Fk%2F%2BjLc%2FsiL%2B1sjE5EsjJkzZ23n3yT%2FpR%2F5vAaE%2B5b04NGbN%2Fd8RQF9t8dQKFtyegD2bZvs%2BC0N361SgYJDzh%2BvZFN1MM2xtwIVHvUvamk%2B82QpGrPhpcXxewsiQDPpvaUd5%2BuDtZAHpHDdWZEXBNzzMT8jGhxoem62iEXk9IpUUxTYL8%2B2TpLHfHHwaClcRDZmlGX71q%2FY7mEtiN10R6iFgXreqKUHVRj1nRvbyU0CoKY1X4emMJCiV0vptQM3%2B8QnO%2Bt6aoAvli%2B%2FKShmWB466qn1djuxf%2FLcC0QFYkBfwYlUPXcbrMtDe8IdzMYtJkntstfDe8t0FJ4FjoeRzBcC1R2L8DLJlM5G2HdRk07Kj4PpCp%2BX4qz1KLV7OYAj9rBn41qBrNurmuWkuio2SWuc2W4UPggX%2BWN2UQ%2FtNdvzbS4bW8SAycDLkdkireoEJNyCitcjum1kTcEJgji9hkjh56mPp%2Fw98cWcpqPngLgaaTfIM%2Fcyh7Dbref68DtdKasSwzmu0EeIGtkMMLfjjb0GOqUBpAU4IvqiM12VIYcBozT1GTb%2FSMRfrKzqlNewIBfN45JcrhXfD2m9aXDIbE71%2FlxErTZIY0yiO7HijhpPjBlKxpDs0TPCjxYhTa5XIC3EYhGANTg2hRZDvXKYUS01rqpoxkEb09B%2FHNKyXC6DuhERAmS%2BBuS1jf61OvggIqPviE3iL4N5lqtVg88%2BQtFo0h3fS%2FcNWsyyCMe6ocXVxQBTSF50EC90&X-Amz-Signature=335ffa304023b6c64fa505338d2f47cdfab80ab48db8e82e43e6e3456d71855e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ETDHIXJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIHJuxWUiWfxghCfk7TTo3nS1aJ11CGMqxfxyw0CEugR5AiEA60F1ktDbxFZv9cD%2BEUcTzbmRy6Gnz5uFB6v9hHWTqXcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDJ4ZN1Zxhf6BmST30ircA8dV0zs2aFuggUynNbEps0qJZS%2BBg56LMSSNexgr7ucqhwbDKfXirlEUzwLf%2B1Tht%2FszNxX81mlSNfpYe%2BTfQ3VD5w0fPuFt2%2BRd5%2FZhGp75xgoWoLplfS%2F3T0pTWHYu3kPFTcSeVzduUlWebAWnNgR%2BlPwYM1L9AKWXb1AbpeSxkPHX%2Beh9O5D0kG02G898dSJLykhHIfm8cKrvQVwf87dnN6se26wr%2FVbSh0g8lWBg%2Bd9%2F00g5TxmE19ztkba2%2B3K1cAbqZICCYc0kDHfQMPs5GaPDRRmlqrZ76XYRtoeI8l%2Bg8nv66XXNqzaeI2hbV2tprPjUDIOVLHkCvdOqqrcZ%2F81VBepDzc8kYJ9aOKGpwlW%2B%2FoK0V6M7FZy668fDamVoNWyFkIKv6dxJGKfHWcWtRWn42jgs%2Bvb7%2FIsHfwAfTW8O6UvMiqJPvtPbY4eoWg34Q%2BeOBV53mTy7kNtceOsOgDzq9V2%2Fq8yEAKqS4aEzPrHicUHXRJHljE7jFLFP%2FDUyM8gIFghoUhagqVRLuKS9zWMjKU0DPND7uM6hEmRY5kyXUAHLONzXWq5qOqEt9CZUH24LHJADlBoyPcUM9eJo%2FJxjLZk4ufFvN6j%2BpQX%2BcB%2Bpc%2BiSSndh8VSwMK%2BLjb0GOqUBU%2BZMZKt6p18d8PLCeBSQKGI02xjkRdu4awS9Z97FPFu7NhYhEGhurSRpdKLSut5UxUxejvOoMlQqdutjMGOldHSKAHeS%2BtAg1XE%2F60OHblEx8Zxz5s8OXGPbUUPlzQno9wHS%2Bwg50PoY0PEvorlAGmgKH8vzp7rXDTYOaJ1PT2XKJYkeddssUZR262zNxQazaVSkXKQEE%2BMlhfsyxrcI97tfAorc&X-Amz-Signature=b347c4d7f1f64ace06ef79a7bfd92116e029d88d006f5f75e13884278fb61ea1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUOW6I7G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIB0tc47tKRZDqcs0fPBqCjAl8PB1Qr4%2Benn3A8kFvQ8qAiB4K5bHY9VYLdAiNbreeZ17XalZIwDHOJti%2FbXqWNDjQCr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMEG1eIZx%2FrBQHZ3LoKtwDb%2F%2Bd2q0qlN2b5Fq13ZtoZsq27TOOlT3fri%2BhsvD7Tdju8N%2FxI7UJ5KCo3qFNZinQK5fVwfzQHUNI%2F2aGiQYhG%2F9eCcxFWlEGX2lNy2irM6IHOKCFCC4FqxfcPRixhGgW4e9INc60UZLq3yE8i9e2eafUDM01q%2BBW%2BOeQZ9f1js7ZCyNeHTSgcrFt65vbfM6dnFOgtsJZ2EOYLI2fiNV%2FEZy7H18q4Q%2BgmLMi4MDJ01TnBbiOUR4DPhdoe5AehPXQ1uypGqoFe6ayelQ6nD353J4j2c9IKTYUcqIaLUw8QJDGt%2Bvq9ZYvZZn4lLr7dxYmLH2qFs5AeoYVmkAfOuUKsE5awtfMj4bOco3dfUnDkjeTdnFFQ57zeiekcsla4JEq6iI%2FwhPY315jiW%2FAaSlDVMjxuUFmUol%2FMa4R1pcCVIKxCEH2D2HOdqeikbojMfh%2BpHI6SeLGUz3mUYcRuuCIEhkf2k1NlqcZE6%2FOnu0kvsynnj6yyg9bka6Pj67wPyiQD2IAuWQMFRlqTSc4FDAbOvv3%2FqHV3HQ55bUVrmC%2FFtRxNuhzZkzwfw671WX2%2FXyaVqHbIWpBm68s%2BsqA%2BzVC0P%2F7%2BtXICTfWTQEjRdSKjJXUfvu3n%2B3Nd4iolvwwruONvQY6pgFVM6TtpARx%2B1oi%2FA1rwAs29F%2BVKB4EQn2lyJlIFUjjfmgYEjd5y1si9A%2FUNq7yZDvOS%2FXBDumOFFqjLKytK%2FUlhjUtc4vQOYH3RfKFeFghDjLhHgiTc0fGarCeQ4Xz8USEk3Ve5oubzEgIMQe%2F%2BzHG%2BnUJkq1Fty52QnEYJhtNN3UpU1aaBYUlE1s%2BJXq%2FQOAW5vyaY3ibetYUiXHL4oNxD91f6uuy&X-Amz-Signature=43fed8d905191b7c2cdfa532ec730cd69761e82eec0c3c3590a445a1505265cd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ESHJSH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCH3EB1Ran0Njfd2rIumbEmsA4%2BpHlenq3ek0S%2Br4VWegCIQCXbDKP35ImWdM063G0hmhtTho3BF93qEyrpiuqAQzFVSr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMZNPpVLiDsSZb4EmnKtwDBZWjf0u8do8DEKInWTkpbPhM5ct4gxNXxG144uuTHuvZcooLDXHxJ3lBDKClMmcmCuwcxTMEXrdsx4UcaTOru1HkBX8AZc8ce8H2n6dtDzAy7LOIAWLB3srnWA2nXSRLMJ7387vplIQUAIVNB2LRmCnG5tT5Fk8wD%2BbmWYPMO4ElPkyqUW6nxdTGL%2BgI3S%2B2EoRs0AUMgMn9DOLquAS3ElOI9oARdqyDekaRkud4gtlVKUKU%2B1DtXs92HOwP2xV0kPZqQAH9jZXOJ4%2Fx0nH3cyDa6Y74qV8hFSaxRog97v8CPi4ah8cRpDLAwwnYnug79Jjyx8kCc5mfYve0muTO%2BrI%2BZvAtwbJR1PY%2FXsox3D2tBUF49dcmm8re%2BXeZhurMrH5Tedzu9IzKnwL6J8bVQOHebRvWaUclGCfjw4JRh71HevBBik8q%2FoPc5tKamLkEWnDIfRzdm6yvgaLEJGVc8OfjOwlegaZHSsizFVLvLbe1xzhezDKIYf1VfSCEcuf8o69YxpZUxQQwcasRapeNqYjp4vonmhVE8i0TX6ljCLBw6yvuuOX%2FcQUBUCZGP3pXjzf0MAQSCSuegOa2DdlAG3OWnMNE7XVkAa20cTC35iYnJ9NzvqADjfcMcegwsOONvQY6pgEKCG8h1l0KXwJTBRm%2FtRBHlC%2FcqIzf190TA6T5xhFSfNAiV67KbFSIQIQ55ZiyX0GqVxLmHVlM%2FnfQK5yAw%2FZ57ANb7X3T7QOEjHdZv%2B2DcIyP96y1wD53oUoll9g3sKBzfNj6t%2FqaQrv%2FV0ZiwRiXRD2lQpQArwBclh0YZc72834V0C3j5XdUqu%2B5cNPR%2BhdihrpncR3H2hXzQaRgx%2FE45S8OmOG1&X-Amz-Signature=2a02b767773c084024a272fb1b987eff706d0beab3d8593cac478e1e8d2f018c&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KENF76K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDuYrhOag5P3yO2AOPd%2Fq77JjTFK422qS6jeDPRserf5AIhAOu%2FcrndQot2IR3Xh%2Fu8eLsSCc8TpyNG%2BOev7JXZE1jpKv8DCEQQABoMNjM3NDIzMTgzODA1IgwdKfQbSxEJFqMmkXgq3APPsM%2BUBt9fTzp%2BUp%2F8VZFJHGuMuj4q2Ung94lVkiARJhhSMpjaOdbUWCzt6uSG9sUbIbRBs0UydBSuLM4%2FfcBDxDSrzTE78%2FtBgUhnghTvbL6%2B5CIpP9q0LBP2tHSrKohHGrk9LNY%2BGsJGUQhb40qXcMfTVtA24P%2B0tTInY2IFGI218mJTe%2Bhz8blTVvullJbf01X1xTqvY3Q2so2OpsyjnGVpiYPzIQmXLRWVplT07bTcsdAlRxP07ecStcGL8e47DozIFhq2l%2Bpzx9zJhlQiw9je67idH0W1VOI%2B0CwbAAKaIxgt5NFxevV%2FoC7BD0LJSPX7Uudb0GuZVv4XBoWYxpK5rZ913mDRgtkA%2BJlCBkmYt39H%2FvIM2Bri3OglH3UbcFjVAsunCoh6FwVWGtb5AVOeroOVE3Zth043Ruw5juutcL1veQ8Yxb1h5ox1Y9zRcdPjqTYv51ggUH2vLb%2BQ0N2wukYvwEu7Yn5K0n5UNZHaBfaY0r%2BqXJst2WbgvMLZxFMJQ60NEmMNj6tuGAq2lwDfoIXJfkdry%2BqAKnBFPdCT9xuWuD2Z7jEMquU5J4dG2P6E%2BSjIBFf948AIi6pMpwMwcKQoIb370E7h%2Bf0tCtOG2K7sTkM%2B2PzEszDrio29BjqkAfOZNK8R7eZPENHPkqHDOyF2T21P0hjrv9c1b4IDhFwZ8wQaTyR0GTxavmGTbpJ1OqfD5WeCRh70vIXFrTVezM0fyVwFCm5HS7jBGXxQWJ3T%2B7DvuhVXO01lA0zNDpoNZEbj6r4305JJ34AB21NzbO0OicZPmg27zfv4%2BiF0%2BNRCF%2BdZCpiOA1Il8Sn%2B%2FVRSlJVHqxwYgJ39B5alD0zkxur5%2Fxk1&X-Amz-Signature=5e39f25748d3bf606c2e154e0fb1613c0d14a38aa427d5dd133c39d7b90f5104&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN2VSWQN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDxSm7jKqkv66FmCbayOe7EaCrK9uibuR6mx1UAhxezpgIgK4MPYj%2Biql6YM8HjsF%2BQr12SUqwdC6h0fqyQEJr8dUYq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDKIeAKe3LluJ8aI6VyrcA9NMPs%2BNBRVQ74aiIeCcSdA0qIt18er6gLv7leekdw376rlUqka0apeu%2FEMYlFs7VuF9iaKMhiPOPo%2BNRa4l0qH1w0E1WE4zUvFwWp1y98WJWZ5tb1fovjYUun%2BVe%2FCZQozpWYdyRi42%2BS4ajfYo0SmwJehbjObD5BLLJNn28TLqCC5LQ3Sx%2FEAXCG4mcpvKJE16QchCrVOdhOlmpGGHdBi8E0pm3YF0W%2FGYodmXqGhiPMDu8Q1iXbLqtWN1yNXdYtaGFkV%2FHzBzCaJw4cnk%2BIh7tYKyFEr1WDQ%2FVZCTsLnFohEtX8cELdc7wJL24bxIU5DqRNFYg14PZer58Lo8d9ioSQlYKOV35AWm6kSA8OIK16vv8tBO5Z4y9ZCCHaWrEXl0JfFst4hdGWBQiQMDMAb9oVEckL0l8kqcEBKzOQw%2BGiHxiePtRqPf60NXCxM2iKapevYtsyqWsyrSuGQ84vGLevYECeOVaOZIWVafAu9e7B8P6XUO1saNVjTOUguXZFovUxM83g8rsFAbufNugf4IEJXRZcT09gFRzuh6BYvMgI1XTUgKgT6vsUIjuyreBTtHk78SwZy2u4kETcPTm%2F01cmntHChvLXwWvlrnwEO920OQaYa7VMlrF9BOMPOKjb0GOqUBToVfTc3T0E%2BBRYobhcnfsBVwYiiEkcaxx8h4mhWjCz0zlqu%2B2JRoxfWXttI0UgGNTjrj55tA2MUTcILZCsj1e0NoxLSZ1l3rgbHs%2BADm05HmrsMQG6F3eRq2oShjk9yzqtJJf%2FjCn04ymIoE7S%2BMR%2FGaZJAsv77cdOelnq4QUBOgjg6lMld7tWdzUZeGnwf%2BvoEMXThuYzXweR6N3zZXd58uhTdr&X-Amz-Signature=391e6ab627ab5293cd556e7a6a4e98dc5ddc2a82ba9a63dec6e5c74c11711f00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUOW6I7G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIB0tc47tKRZDqcs0fPBqCjAl8PB1Qr4%2Benn3A8kFvQ8qAiB4K5bHY9VYLdAiNbreeZ17XalZIwDHOJti%2FbXqWNDjQCr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMEG1eIZx%2FrBQHZ3LoKtwDb%2F%2Bd2q0qlN2b5Fq13ZtoZsq27TOOlT3fri%2BhsvD7Tdju8N%2FxI7UJ5KCo3qFNZinQK5fVwfzQHUNI%2F2aGiQYhG%2F9eCcxFWlEGX2lNy2irM6IHOKCFCC4FqxfcPRixhGgW4e9INc60UZLq3yE8i9e2eafUDM01q%2BBW%2BOeQZ9f1js7ZCyNeHTSgcrFt65vbfM6dnFOgtsJZ2EOYLI2fiNV%2FEZy7H18q4Q%2BgmLMi4MDJ01TnBbiOUR4DPhdoe5AehPXQ1uypGqoFe6ayelQ6nD353J4j2c9IKTYUcqIaLUw8QJDGt%2Bvq9ZYvZZn4lLr7dxYmLH2qFs5AeoYVmkAfOuUKsE5awtfMj4bOco3dfUnDkjeTdnFFQ57zeiekcsla4JEq6iI%2FwhPY315jiW%2FAaSlDVMjxuUFmUol%2FMa4R1pcCVIKxCEH2D2HOdqeikbojMfh%2BpHI6SeLGUz3mUYcRuuCIEhkf2k1NlqcZE6%2FOnu0kvsynnj6yyg9bka6Pj67wPyiQD2IAuWQMFRlqTSc4FDAbOvv3%2FqHV3HQ55bUVrmC%2FFtRxNuhzZkzwfw671WX2%2FXyaVqHbIWpBm68s%2BsqA%2BzVC0P%2F7%2BtXICTfWTQEjRdSKjJXUfvu3n%2B3Nd4iolvwwruONvQY6pgFVM6TtpARx%2B1oi%2FA1rwAs29F%2BVKB4EQn2lyJlIFUjjfmgYEjd5y1si9A%2FUNq7yZDvOS%2FXBDumOFFqjLKytK%2FUlhjUtc4vQOYH3RfKFeFghDjLhHgiTc0fGarCeQ4Xz8USEk3Ve5oubzEgIMQe%2F%2BzHG%2BnUJkq1Fty52QnEYJhtNN3UpU1aaBYUlE1s%2BJXq%2FQOAW5vyaY3ibetYUiXHL4oNxD91f6uuy&X-Amz-Signature=0e98c952add82c6a56122456f6d8d69203a91d6a24f9878a1f2cd22908388163&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL4WQ3X4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD%2BStnwjvaBSDf1MRRbfJI8IudrKNAGjmYm%2FclAsSdcAgIhAMfuztxOoeKYN2mRpmZtrRAdCzUVleblnWYeCahAbZUGKv8DCEQQABoMNjM3NDIzMTgzODA1IgzwhwGl8TYWQrY8VuYq3APUcskvD7xPBhvz%2Flmdx9FUmOGn21hQ0076YotAbpdfRtnRtCOOM1fNDROaEN4ynk5vlaQirvnOqocNSTbkRKotdnL3WJfOK%2BL8Pys0asXJ9%2FguvZPEHZVf2mbVoqB2HKLDH9Xg9Qs6s1bWGIDnNh0URiRiJnnRt9ZG4yPs1ljMji2nQCandpscRTaYqlEQ%2Bohztb2GlChV7Z1kszUNcm3YIFoSUGWEVvj1IzuSbdtFiF3GZUbv3xmvH0wMJpJ3V0wyKAqPgHpMb5Asw%2BJnJvJ4WWpTQKeA15PiGEGGwxgCneuTp6P5Nur4BS7o5DIIUT%2Bt2rgebQbwE3QwHs5G4dvwvWZLVwOkHsViQmxu4RG7D8xuPFwGljWKjltF7vCiXdV%2FPMqBEFc3fJZ0z%2BMPPpb5y2zm%2BJlxxDMH4BNhJTTlmV%2Fa7VNdw%2F8T8FnlIUngOEv8HNVSTw6MKlsZw5uhuMANSrwgwnECHnzJcFKY0p4DPU%2FGGe%2F6cWCrTeCxy7oNkhsUqj6ra1CmXIWTTtXg%2FdoyyTi9MpndMLVI%2FsGcTLLwfar9HYCpGoY17usMeRnvTgZtTM6y2BCI0DdhPeUB6jhkE3FXpsKDOruuZUjCF4QeyqwNRkdbtue9Q3fdnzCzi429BjqkAYs2H%2F5eefU1TKbyXG2JRJ2UydAruGEpNdNBdLH7FchXJta6JpCPJVO5oC8bg7W25kOigx8RQCGktqogVd%2FpJmNkRDwWgcOAJ8%2BcylSsNG74TFHSNhJLE1PhL61NmNCEwBxCqnxn2cJmNdCLhTXSTiiGJEnUng4quypGtYnWz4P%2BbzV1TpwdDICS2DZS4SUFMet8hp%2BeulociPiVnex8MojION6j&X-Amz-Signature=e040c7dfa64bfd3b5878a5f866af95a4ce90d4f598bfe3a939de0784bef027c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL4WQ3X4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD%2BStnwjvaBSDf1MRRbfJI8IudrKNAGjmYm%2FclAsSdcAgIhAMfuztxOoeKYN2mRpmZtrRAdCzUVleblnWYeCahAbZUGKv8DCEQQABoMNjM3NDIzMTgzODA1IgzwhwGl8TYWQrY8VuYq3APUcskvD7xPBhvz%2Flmdx9FUmOGn21hQ0076YotAbpdfRtnRtCOOM1fNDROaEN4ynk5vlaQirvnOqocNSTbkRKotdnL3WJfOK%2BL8Pys0asXJ9%2FguvZPEHZVf2mbVoqB2HKLDH9Xg9Qs6s1bWGIDnNh0URiRiJnnRt9ZG4yPs1ljMji2nQCandpscRTaYqlEQ%2Bohztb2GlChV7Z1kszUNcm3YIFoSUGWEVvj1IzuSbdtFiF3GZUbv3xmvH0wMJpJ3V0wyKAqPgHpMb5Asw%2BJnJvJ4WWpTQKeA15PiGEGGwxgCneuTp6P5Nur4BS7o5DIIUT%2Bt2rgebQbwE3QwHs5G4dvwvWZLVwOkHsViQmxu4RG7D8xuPFwGljWKjltF7vCiXdV%2FPMqBEFc3fJZ0z%2BMPPpb5y2zm%2BJlxxDMH4BNhJTTlmV%2Fa7VNdw%2F8T8FnlIUngOEv8HNVSTw6MKlsZw5uhuMANSrwgwnECHnzJcFKY0p4DPU%2FGGe%2F6cWCrTeCxy7oNkhsUqj6ra1CmXIWTTtXg%2FdoyyTi9MpndMLVI%2FsGcTLLwfar9HYCpGoY17usMeRnvTgZtTM6y2BCI0DdhPeUB6jhkE3FXpsKDOruuZUjCF4QeyqwNRkdbtue9Q3fdnzCzi429BjqkAYs2H%2F5eefU1TKbyXG2JRJ2UydAruGEpNdNBdLH7FchXJta6JpCPJVO5oC8bg7W25kOigx8RQCGktqogVd%2FpJmNkRDwWgcOAJ8%2BcylSsNG74TFHSNhJLE1PhL61NmNCEwBxCqnxn2cJmNdCLhTXSTiiGJEnUng4quypGtYnWz4P%2BbzV1TpwdDICS2DZS4SUFMet8hp%2BeulociPiVnex8MojION6j&X-Amz-Signature=2875e328140f88063aefefb9352eb553dd63af6459aaa4d453834d5ad933bc81&X-Amz-SignedHeaders=host&x-id=GetObject)
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