

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJYWFX37%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBmcJfIsZeXey6KvOTK7I7JPBIzICw5nEGhxZrXcmJaiAiAxCUjJRPZ8MmXTxAcSPFLBGRIPRkapFma0uE2af%2FCdHCr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMitZSC1%2BFanUnlET4KtwDh%2BwdbwYNDZCi3TTj2OMQ%2B0vahrQqno0%2F8ARLyZzq4hamg69vzrypacJta9HoB1H9XPDekWrtpC%2FU%2FF8pMD0ZV%2F1tMANrW0h3jv2Rl673Wt4aHwdC%2B6g608yYXkqwXVikW1QWUV95bOAKwsY%2BuCswLWOVS58qVJd%2BCpIaXALVHjb5dv8%2BuslHeZeTOy1YtPuOFkcxziSs60mS%2FIXORwUyr4rkd%2Bi8bYtIZHNEWiIjwdJ6%2FAV5VJVdd887LLAmED6Dn6E59GP1CqPLe3oHJ%2BHyIw%2BlWc7jtXKg8GMNqU0hNOhwjkLx19%2BluAPNIwS3tY0WA805zjyyar8Kpv44WJwturr1QdcF64JxYWFcZRcBn9fj%2BsWe4yCZAQ44u%2Ftnu4zGaEgWs4U6hauzZNUwADYNnyR4RLufa5Z1lcO8HlrUWJrka7q8yEfaxgHjugxurcBdPReDpLQrfDl%2FzGV2gFNiSSWsXrm5AV1IRqNldU6PyKeiFjhYCOQYuFJq03lCxgetDyAFyXOePPlNLwv1srALDh4WDUIzZ7d5AOU7OnuN5O%2Bejt7dGc3PS9%2BGmoJ9m5TG3KqDxXhNmHjzAN6WJHBEZ1qE9GlO2MNJYdv0d6nA05mYeqDDOzJk9fmwDcIwr5mZvQY6pgHBcSxKYuys3qlnWtWggh%2BOOaE4w9jtvNW5YIHq7Itzc5OHtA8VfkDf8HZOF6ttau0Lm22F4qOaoPz6Fp5X0kmqYI1pMogl4UBH6nkt9BZ8nRn2RZa2g65%2FfWPeIUZUUO1l%2Bj3ddJilDbyCTuXO6eIVBADjxNjrhNAluMRAbp%2BvYWpANEMT4HbhhwZqmuDCLjALFqIVOOizjsA34E0dmutPV1Eaeh%2Fk&X-Amz-Signature=9eea822e63144592edafcaf36794ecc90009d8f9467e929cf696ae28a5e5ff3b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLIY2QKQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIAdTFCKrnN6DRw2S22%2BD5HiMhCZgABM16YgfVxxvmF9zAiEArTubnCYJWHwS4MoEy2RjXQqZOgPi8fbk1dvM%2B1ukBhcq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDCvLP%2Bu7OAGQmnLvfCrcAzmm87lWDL511PoTcHX%2F4ygddyQRtGcRLusrpaGLCiFuysd3JmCUgmG7f1YgTGmUL%2B0ETyiKHNbCWPlldBo8RjGbCgf%2BayD9UOEI4BMTgBHHxKA6eUXT74JMD9JWWuVVOBFHr6adobAQVPINlph6IR722%2BrajPWKP36fFAao%2FvzujvsnIYVlcGxCfvwGqJSBC2WmOCjayNcZmsCaqIVhk3f4mbtUnIrPBz%2BuLpsdB%2BYJYnI1TIi6KAp%2Bby%2Bi5juOkgzzw2s1qYwumkur9sFvD5uKXDUlN3pr56nlS8Ga3NPh3QvrUh3keL28xHq9OvR0KwKd3usRpKx1jwB39Ld2LwqYgG9BgnkXHChD88Kt3EXovkGlLV%2FDnlM3ObVSlK66eM1i%2FhkQG4wdMu350T7Szs%2Fc8KUKNF1n%2F%2FCEsQdRPaSvjhHFGX%2BiG6VB%2F4uTsJnn2JJjxFN9%2Bo4sgEaHVII96W9K8cJNYKGhKoZhkI%2BMYdi7ECOTcAKGoWWoWuiK9BM5X1ttckpm%2B7w8LtMy21Bp%2BbnAmBPEok0H%2FA4ukGA9%2FkRhfYdvvb2GCfV0HKE3Q%2FD9dFiKO0myg76fR3mHckm4u3smhBtXPzi%2FoKExB%2Bfj5q2nUzffojkmLEh26uD4MJqZmb0GOqUB2ExvRL2IXiCsnlpXhcnP9B4RZULUCm6UX0RJ9cRNdHOTIyVc4ylVjXGc7dUFavoyyHKRwfDwSS%2FfHDqRBMuD0YJzSyF5MLUW7eyJSBFjnnVY6bv7pR59%2BRKRCQ7znMy9OZGti3o0oR3nj6tgPgqrriypI0zV8VE6JBfxpuQ0i%2BOVpx4zwme4aay9uuXFB3O8Sjsqq8WKdx6mk61uoKcoANBPv4sL&X-Amz-Signature=073b680eac0437ec0dbb7d86a34f26700aaa694fc4ffd24733b033bfd7742dc0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNAOKPCK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCvVXS5nGSo%2Bjt5FoDkI3h6B6DH2fKIh4qzy7FMgaGXDwIhALhWoBSP5GNdocQ1AhWB9pDxWMXYVpwUzzfcm%2B9%2F2WEwKv8DCHsQABoMNjM3NDIzMTgzODA1Igx2Zl6mwcCtZTplIaEq3AMjP7ZnOrbpPAf0RbwFQLEv08ck9TLx9OlcC3yafkkboYKP5%2FkhQ3H13k0R1CwZBNPrGDM%2BKKKidR0EMqG7T0D%2BXstpGcqsojx7gEyavsE9Z%2BUZtgwVF3kjtdn9Te%2BQoHhMB%2Fr1qRyGfI8qyfutIfL9O%2BPWbVgU8tEYznF6SXnDdY9DS9hvcIV9aNA2PxWs4Mo%2BVgMjhdniALHGeN%2FWkCZ1VQneEyTk3WPuaEk%2BYAboAhznTZRjda38bh8dUhnZJ%2FXFV7d3CnKnls2nMeKlgd2ytihjfIZCZd7ZfDjB4socY2Re1ICTE6wiM%2Bgp7xSYdMRhwMBCwHY2MEfdiSdeDSC9dX0b2%2BvoNXFXLWhRGy9U5%2B0BcmwVXnVDP%2FKcJ5eE9kZPl0d2JBQ0Yf1kQ8jpWVeKwHqvZxvb2oLgPH4QJatF372P%2FZhIr8EQmPHypg7P0MmTQYzC3b7W%2FD8k6NvWOsrqvRq7MKww75XLILsQ4b%2FaTPaSdVQMUklg5NWdjTtjO4ln6Ge93OsuvQ7pNg8LKkL1a7N8XBkm%2FeqBQ7qncdVo1qahogaGBUCf3G0%2BIr5AcsdLURU4G6q65tzjoR0ayhkX0mGFWkKi0kw18FtZjVMYml5r2z7nx95oBaMFhDCbmZm9BjqkAZ%2FILkmUA7ZgK6gepx3Tt567J%2B2hwqQARlOborIVEpTAlMQUznVK1Ai%2FFLAjVTu3xHOQDGWauqyqSumIuKzplDWyXkxxTQy5wkhMUSOx%2BWMyfieegYxMHMBC7t0zLwgoJAjJBk0mJVXPq7oKrKrZAcNqXXiK81Te%2Bj4dcpV8os8%2FK0XTZfPxcRQJ3HTUlzc%2FnrmCiQiBNJJ%2FxcMhk89%2FiFNuT23Q&X-Amz-Signature=5179aaa2115d4ef7a0aee4f7e79a3a23f9e0680c2d3a92ea059210df497518cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPHK2PYO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDeD4yap8pqwqy%2B9O99wMoqLgQwxJyO68cuWny28xtfCgIgd%2Bk30ot8v1LsE0czPTMhHM9Xl5EWogiLHhp0mHhRH40q%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDKUwT69uNVwR1o94nyrcA%2B0pdJX6vkvTYam55SwLA8PyEBSG2UwRe%2BCBqVB1IHV7JmloQ3WWmXWmTNOUDz5Woql%2FYni9vtpbg%2BM3cEKL1S1K3nIwj41lew3X%2BUVmCa1avIW4VWSf5CstW%2FlGNLT4WvxUR05Wn1LaGNDk8LB9UO45lNdgaMhJJqPQkBm7ZGoL7piYLrFa0e8tle3tAIaeHTE4mzUrsAYDwh1WJyHK4aCI2PBmbkwqx63lkfuAnUcAgmv%2Fbi51QLx%2FZmmvMPymmYX4zyR2oKE%2BZzGA5Z2fniK5289rBGnKhxzPxHQf4aKsu0ApCGjZs1Q1U4%2BZBt2%2Fqkw74U9F5THyc9BEz%2Bbi1vNASefJC5YVnyaFk4NE3nE3g1PDgrxtiMAGpnDr2lopb5z97rz4EygbQKsvgCtrA8fzm%2F5qPko4bRbyL%2FMzmVtpYysc32wgmwLDCCFniynF6veXHwpSSEpj7R8NChDrlQxlbjzmJXf6rFmm%2Ff2zkmTKCYgnkQvivkWSLjrsm0jAyVdGRMQQjrFZeFNOZaev9uQiEl57m6ITryXEdUZh2Gbk7wa4m3rr3Chd0yGSodDnyVmiB%2FcIThCXpn8sosOiFZjB9nxN9RvwfX%2BeCcl18D%2BRBumZc0okA4XhkrNvMK%2BZmb0GOqUB3SSTaCkeVhf60keRhrKSp6OT8LiQqQrTPwahuylQ5JS1Gt23Ko0TXpemBgYcIZmHPwdk8tG5mRiSO1kcKyDwXWKmutIQdrVoHVOvIHzZdNPpjkezCk%2BnuuLQS%2B7ISqAbIjb1%2Bcgy7fvptVor80sf8d8d5ir%2FMffSYz%2BNa%2B8HbaVL%2BXyMcErF6V1%2BzZFlQBQ77hubJcV6XfvQjU56crHYrMkv5Pmm&X-Amz-Signature=488b014934e63a35ed30ab861e372a1597b5ca71bbd2c7916147e1d9ce36ef4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTMU5K6X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIAWMFmi10nzXlguSeBVfzMRTpatM9N6AjB6ikAERQ0qgAiEA1Nn8zjrSmHRhONl%2BXuf5SaOU43Xt%2BL4dUyyr6EufAygq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDCuAwGcx75YHnWe3tircA5aaWIPsoyqYef0j4JqqaTjeozW5Bc4oeFQdTmUO48iNciwvjBv%2F%2Fufq7TfQDRFc7oiJDoemP0G0XGLueR8emvMZF4%2B0yJke4UCGNqiDPufhwGHavLeIbunzMbCMnzEjZ7O7OgAIC0mYIq0IGHf2ng9tkj7XeQAVDB8zC1E8BkmuZRmiq9P7G0ZAyU%2BKM5d%2FVq6jXPuPdDsrnKQjAjnv2VnDZHyg5HDOyv7PZio6PHX%2BOvtP52bGGOSC3KA9xqWGDCoXCd0muxou0fY9BjS847cDjll7GWBkD4XrDzl%2FFBOtMbpUUXILwVtJG2AtVON%2BUWkAjbTCi2RNI%2FySYMBYTAB1fQk5%2BvW5GBK8%2B9PJmLq2TyqW0eMVsC3ZnjbBimwf9wHmErTXwBjfrW4L0yYHKkEJ3nqKrXTMClEXt2Fe3IU0qjOn3AlUZ3hnOVZ4zrNyEghk0x2G5ML0yLOqNxTI3hHuVKqM1SN3VpknNPDCJMV58loXOYt%2BslIIdVESbMs%2BvTtBZXfHgeN8MXML9JCTiV28qfLJGpoGPpQXQXb0Jw1OndPw2W7MLMIS9inBfRpdVcqI9j7ZKadi4Yps4jySrKSm3aCBDmhw92yFJKdTAIRoP0EExse2cmkH50BoMOaZmb0GOqUBoh8dxhVI6nA0nKV3hPDj8G41tyViTlEa%2FKLJGuSEZ9UpVabYSalk%2F%2B%2BdiU%2B5uFS7Rk9UUzxQiHMLarIRxfNXhS9ekE4qTL1aVVpudHKH5oO44e8Q04kbg3wEoCWPwq6P81MqCvtvVF3m5kfWhPagyxIC60ObbnabN7OFBpaBzAQiQFa008VUfkfEJapmua7lUA1%2B%2FI1Qo3h5yVeZV4OdQOid5ckD&X-Amz-Signature=81cb3aa062b3478899cfb4d9d74a53758fc84f525f3b76ea4d1678784df99af3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU5ZB6LF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDhpBQhQwBe2rENmeyHuSLblkzlWwpErE10SOJzv%2BeVtgIgdmXnc0vvGzCBQ13ZTRAHZJWZIKMk2bLiFuMtNNEiTEkq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDG8%2F1pj4LGaI04e8aCrcAwTI5kPfBU10sAT7aZHnKKTkCD9uwWLWZqBiWjPpHsICHktkvzWV%2BlagmwJ6dI%2FScOesPpvXCC5eoYIAaxEAC5rqCoeQxRsgWNL7dKmKfCmBUWqLIjUVmDUp5WGdXnsuY8NkpeeOLC99bDQpnoHmbd5E%2BhSG9ZO8FE8KijtftKil04aUqu16wqDYS6r3yim2GyUwAP5c8PfyENlM1Dk1n2gqr9DwaTWrvaTKdiAaZ2De7YLtUNKe3dkex3MqQ4n35R66gxCLGFzbTHVVcALy733zwVW4eiypIFbYzYM2nMd%2Ff3Wv1FpIYxYL8EYQ%2Bva2WYhkYTv%2F0euJ8NLPWQ5dq1QliuIutjZ8D%2BgYIQxifUh87tAGrMNPb2UsXTp7mn7OMJZ%2FP8YaxEjugEc0ZORWpKtM1GdfweVMsAMWEGNtMRBek2%2Fa0SUaoTi1%2FZ4EGs2xb0SGT%2B%2B%2FQ4nOCm9dYU8atDUGeXN0wXDkjj80pqtqpDKwTRqQUct8Q3RLiDACMnN%2BByKGQYSvy2vHvqdMMKF7J7P9JIVYgFgcV5OtSrm6C3LjeZQ9pQpeOiO0CzR%2FFG9KADp61OzeAmLoCLZYbetSzndxV2CQIsIGwwDd8ZlmQZn1JgbmJOFFA8%2BROz0%2FMI%2Bamb0GOqUBLqZTG5ZpSV46wn8RzWe%2F4426y2iOd%2BQ9TyPjtieUCgelr%2BWLqKY6bDIzAxwrBhPKcB3AumwTcv4KoXeJ%2Bt9PohuTyI40w9L4vYoWdaGkFcku%2Bdhpk%2Bn2vB%2BHd%2F4JWvAC%2FP12NK7Am9gZ08J%2BnIcCdWyOSPjPRB%2Fv2dz%2F3v4hDgCp2KdupUoutAvve2YV3ZDXnYn1amkjHErB90YCyWXGVg4vh0IT&X-Amz-Signature=4dcdef7e11d28a2b8909c42bad27670c9859e34d182b992119adf4222889655d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP2BZB7W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCfm9Q4aLPzXldP5Pe2cqSRbJo5GlAUHP5%2BKjtyGabM8AIgE55uYuGTOeAfN%2BmEzRxAgwxhQAnF5MYU%2FodG5R6wyisq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDBHL9BB1b13DkHnu7SrcA3m7LMbYwxe%2FXj2THJhgsh8V2ICCZdFWigfqhvsyu8Qtopn7Txp%2BxXszI7cteJskFbMeSIZ0%2BGTH5m8x%2FZeS13mf2EyT%2FKuTbPHlu5Uq7VXvH2ocathhzJjhO0Lzpq9hDWaPgG3usyGTRtwW8R1kBwyvye57EDu6gVvQCpYJ2%2FNMvbUX5v9jpO5av5qTXVDGrzMVYUCmY%2BJTnLcBNLOm6t9Sn619id5XMnWWhisWuRPNvdXwMEKe8GILRRSklcZL%2Bymfwr%2BVKmDI2HA29%2FiY2wKFZgrYWpzbkAyctHfXNcMaE6B1SV2nA3XnBlUK%2FgWPHDdtcAWvdChLfpNrTY8gzX7l1mnTcJwgvZm0%2F8offORJ6QEwh2NA4NyXbuE%2FnOHAxRAePpAw7IW8ci6eRgFrLZaL4%2B31KIvR7M8YcNwToDmrDz8%2Bd5Ed7km96Biz%2BZzwaZ7VHbtS5cwGASo%2BEXmEcdOhUY5NmEmUv08SsKUaXgEd4X2gYyQOtNH8yVLzi7kJK1W%2BH9eCRzdYeh%2BTezpA9Cvjh4TI3R3AWJagOJsrHQDmIHe7UqYXawt9KFzZ%2FTr4d4JqsEMRUZaQ5RPx2veE81kcoAt0H87d8Qdy5ZY0rX5YQnMRVyez3wPdGdBlMJiZmb0GOqUBAsNXgU9QPHf1oYXK73Vz0SfcEgJNlJ9OdiBIzBsM5mtiuTs8juSqEOCtiWudmdguxFZ09TGdZpIS3lv%2Bpov%2BvGrqmTn79ugOpI3mDm8XTkr%2FrmcaeWYKkFKrdtEKlK3a6pW%2FPEENCPCstUuztkvoBclblr1A%2FbPEsVM1juI56u9ZfEjDW90StbwMDYntcJldDlVK0eAV9OEjWwUsTshN84Ys1Zjc&X-Amz-Signature=ea75aca7ec6b1b30b6dfef474ef8256e8e728fc56dc2213d7e068f472d3d7d1c&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPZJ5Y44%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDCYzb8jh5wPBp%2BWb4CdRUz0o1ECnB6iD7iiJscbw%2FTlwIhAItvDZ0z5UOlmFz41TbibFOxaD5bcAMa6DEpOxML71ofKv8DCHsQABoMNjM3NDIzMTgzODA1IgwN%2B4DJfRudYqD5nH4q3APhka69sqIp3SU4XcZxML%2BJzZ7k%2FJ%2FnPDAmNolW9fs%2FCUkk3diFcnDKGr6exPwQ3oQD%2BLpNX7jdxmD94HUD9zvqGdpJuUBBqMH9hiUBVfAg0UxiqP%2Fs0admAIfJOJVWMPzgzdNCX8wM3QTKERjiP13ttU1zM9OEkTFTifCUuw1fhxEHR6I7WXpQtplq41dohP4GRfD8s3GjqK3f%2Bbb97hrAcbSLtMBgQI7TVByVLn9TEVbBagooR0UyaNhiREBq7sdXeZnMBjptdenR8%2B27HJT8lwJgJ2ZSZepRuxTssiMCBNFy%2BXw%2BjyGNmoUxl5%2FMTU3gkZE0APndZwgtP60wt3g9zRMk0MAq8XSTIZgQIH%2B7u47PfgDe8lOuFfirHXMJq7cABHmb43DSyuU%2BBfa1NS9cA78fCYbOXcFWRurq%2FiENd8VJQ4Q4DZ3f974oUwTiN0UBruEayU5We6x2rGEAnZWhxGNtpOXJ42dAp2uYJuUXhNvUd4bulosymnfxtEAqheYak%2BaDAzjFA1BbGV9nHATk0w%2FMv6782LEhyYv0%2FqMBqLdB9%2Fx5ELn3nIWDYzc9sm%2B%2BWqUeZmExwkbJ1UcPqjDXvWz0%2F1kmkWhJBCFBO0QtRDuG9L6XPXQSelOYXTDMmZm9BjqkAYT%2B6YYSIh%2B2cMvO1%2BEOIcemCRpH%2FSKLdd%2BS8I1DibLvltpup2GsqVDYabAPRImu3HEFV1xG%2FOlMVq2RVRnLVzhct7ZnSnuB6zckFt5pFGkAmxrr4UiRqnZKfWsAl1ASX3DMt8FssAvNTEy8rzDEf5l60%2BZLmUOUQXltXEG75EpFZhICJlP3HgHDu9mGWhwY7L%2FB%2F19BqpAd7V7GGK40ggXeupIN&X-Amz-Signature=b6e2d148d591ed221ddb734c776c34cba818a05acd1bde4f36052e14f4547be2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTMU5K6X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIAWMFmi10nzXlguSeBVfzMRTpatM9N6AjB6ikAERQ0qgAiEA1Nn8zjrSmHRhONl%2BXuf5SaOU43Xt%2BL4dUyyr6EufAygq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDCuAwGcx75YHnWe3tircA5aaWIPsoyqYef0j4JqqaTjeozW5Bc4oeFQdTmUO48iNciwvjBv%2F%2Fufq7TfQDRFc7oiJDoemP0G0XGLueR8emvMZF4%2B0yJke4UCGNqiDPufhwGHavLeIbunzMbCMnzEjZ7O7OgAIC0mYIq0IGHf2ng9tkj7XeQAVDB8zC1E8BkmuZRmiq9P7G0ZAyU%2BKM5d%2FVq6jXPuPdDsrnKQjAjnv2VnDZHyg5HDOyv7PZio6PHX%2BOvtP52bGGOSC3KA9xqWGDCoXCd0muxou0fY9BjS847cDjll7GWBkD4XrDzl%2FFBOtMbpUUXILwVtJG2AtVON%2BUWkAjbTCi2RNI%2FySYMBYTAB1fQk5%2BvW5GBK8%2B9PJmLq2TyqW0eMVsC3ZnjbBimwf9wHmErTXwBjfrW4L0yYHKkEJ3nqKrXTMClEXt2Fe3IU0qjOn3AlUZ3hnOVZ4zrNyEghk0x2G5ML0yLOqNxTI3hHuVKqM1SN3VpknNPDCJMV58loXOYt%2BslIIdVESbMs%2BvTtBZXfHgeN8MXML9JCTiV28qfLJGpoGPpQXQXb0Jw1OndPw2W7MLMIS9inBfRpdVcqI9j7ZKadi4Yps4jySrKSm3aCBDmhw92yFJKdTAIRoP0EExse2cmkH50BoMOaZmb0GOqUBoh8dxhVI6nA0nKV3hPDj8G41tyViTlEa%2FKLJGuSEZ9UpVabYSalk%2F%2B%2BdiU%2B5uFS7Rk9UUzxQiHMLarIRxfNXhS9ekE4qTL1aVVpudHKH5oO44e8Q04kbg3wEoCWPwq6P81MqCvtvVF3m5kfWhPagyxIC60ObbnabN7OFBpaBzAQiQFa008VUfkfEJapmua7lUA1%2B%2FI1Qo3h5yVeZV4OdQOid5ckD&X-Amz-Signature=6c32dbd9454d555580d215e63202e39f4ae25bf4fd6e53baf9788f4e42fabe83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FDM2CMH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQC60ZPrESWUV4idZG4sEZMsj3iqcVBKj73BX8NAVLLjdwIgCp%2FmfFUZN%2Fg4l4FGAIwPmp1saUz65oV1GEHvJ9IdXqIq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDK0NlakWyAJnLwNVaircA1hd7VEBGSubSbMsK%2BinT8LJV9LGwhneg5AZeGGHjI%2FR6o3Vai%2Baek6czLmIWOdzD3i0kwjcWICflXk1S4u%2FRcoQ5DTlEsMKD4LUj%2BPseqVJhg38fhQxxCoHx%2FEw%2BMAi%2F7GeUhnnqhNqSCKo%2FQcLHLAb5%2Fv%2B6mqjzsStiSaEctFzLFpcHe%2BZn2NCAoj6hj5%2BEFuIcZWJzInnBkP7vo1V2ZzhiXvgfRL4aohQimlFTgDZP8ulSqlg24CQwBSQ6oC9xvZAIcPzClMN00yCy8QzKVFfQU669HHZt9u5uCk%2BKqxyuKmxsH3weD3hqK5GOyApPj4cAKMo1eCm9CYKVRQCr99Ol5IAKAtpDwEW0ukxI9XHQqePKmMaxmhwz5ByB7P0VzUwVyNUXDan0%2FMRPkhxpMZIZBX7Q51M3Y8L1uKQttK0WucUbTHxN%2BVaVwRgqIT9gp8lbU%2F1%2Fu%2FnyHAQ2ERsXlj3BHAP5PJ126d5g2EZXkFhz8ebQ6DyyG6HNGUPWhzdk3zACmWC%2FNrPzeabod%2F0dmRCWK1OA5dn%2BR0bq3Ek%2BQCQqnC87OLyLBmJTu0S%2BU8pejAhw4ppAbGW3m%2BzN0MN1DRGI%2FtMBFWxo9e9WR5H9DQeHIkv6G2OOxth8XP0MNSZmb0GOqUB215RUwdEvwtbrSRrtwHFTLfubeZNAzyhbeZYa%2Bnod7PpE7yZmceHqhmp1x5fAMm5WsypMRqgmUmX44fsVbKbXMI7VRBoByMkP3v4Y3Y8vvW7e69WTcgsjTM2L9S3JILfUQep%2BmT6eNDcf7D4xdm6eEDf2on7UJoNvnfIIso8q4Rl90Z5EJEBm2nliBiSo7l%2BFrsmXaRE8dK7A%2Faw0SINN9zGuQJf&X-Amz-Signature=f053d1053e1ae510a642869fad6eef3f3a41dddabc06c5166cf82110b601347a&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FDM2CMH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQC60ZPrESWUV4idZG4sEZMsj3iqcVBKj73BX8NAVLLjdwIgCp%2FmfFUZN%2Fg4l4FGAIwPmp1saUz65oV1GEHvJ9IdXqIq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDK0NlakWyAJnLwNVaircA1hd7VEBGSubSbMsK%2BinT8LJV9LGwhneg5AZeGGHjI%2FR6o3Vai%2Baek6czLmIWOdzD3i0kwjcWICflXk1S4u%2FRcoQ5DTlEsMKD4LUj%2BPseqVJhg38fhQxxCoHx%2FEw%2BMAi%2F7GeUhnnqhNqSCKo%2FQcLHLAb5%2Fv%2B6mqjzsStiSaEctFzLFpcHe%2BZn2NCAoj6hj5%2BEFuIcZWJzInnBkP7vo1V2ZzhiXvgfRL4aohQimlFTgDZP8ulSqlg24CQwBSQ6oC9xvZAIcPzClMN00yCy8QzKVFfQU669HHZt9u5uCk%2BKqxyuKmxsH3weD3hqK5GOyApPj4cAKMo1eCm9CYKVRQCr99Ol5IAKAtpDwEW0ukxI9XHQqePKmMaxmhwz5ByB7P0VzUwVyNUXDan0%2FMRPkhxpMZIZBX7Q51M3Y8L1uKQttK0WucUbTHxN%2BVaVwRgqIT9gp8lbU%2F1%2Fu%2FnyHAQ2ERsXlj3BHAP5PJ126d5g2EZXkFhz8ebQ6DyyG6HNGUPWhzdk3zACmWC%2FNrPzeabod%2F0dmRCWK1OA5dn%2BR0bq3Ek%2BQCQqnC87OLyLBmJTu0S%2BU8pejAhw4ppAbGW3m%2BzN0MN1DRGI%2FtMBFWxo9e9WR5H9DQeHIkv6G2OOxth8XP0MNSZmb0GOqUB215RUwdEvwtbrSRrtwHFTLfubeZNAzyhbeZYa%2Bnod7PpE7yZmceHqhmp1x5fAMm5WsypMRqgmUmX44fsVbKbXMI7VRBoByMkP3v4Y3Y8vvW7e69WTcgsjTM2L9S3JILfUQep%2BmT6eNDcf7D4xdm6eEDf2on7UJoNvnfIIso8q4Rl90Z5EJEBm2nliBiSo7l%2BFrsmXaRE8dK7A%2Faw0SINN9zGuQJf&X-Amz-Signature=e1a720badec7b5f4da2cde64b2d83f46333fd73e5cf173df2302cdbbfc73740d&X-Amz-SignedHeaders=host&x-id=GetObject)
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