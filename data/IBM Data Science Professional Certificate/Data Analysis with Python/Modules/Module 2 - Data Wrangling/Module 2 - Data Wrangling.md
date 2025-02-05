

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666I2WNRGR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIC50Wivkp2pvQ5nD8nyMSG1xnSatyVlTH9zNlnSxcK87AiA8mTAU99nNSk4SM8Igf9SJInwD0fCSNHnNWO8hW3Oanyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMqTwf7CllMX%2F7rBk3KtwDNWwnLzc81HAzUFC6VRYGafbOrPxPZsdlGdFGFA7P7rZglO7hZgAVUDjLkUvhcMAYrQ1vmGkEu3ix3uO1p%2BMJAQxx4nE%2FK6%2Fu6O3EO0Fn1TmJwG04oCxTiTSUFqXBBDfnkU%2FUGsFPEDcZobIDhRm%2Fvao2UDm%2B7hAYUG%2Fq2wFIlvuBsjFkcMObjJMUzM8hxarNnKw5tqp0dfSk4hHJCs0wHm%2BTijjO4gR43XAf88EauTgSZbJJDEunZD7%2F4m0iec370%2FM3GjM5fnSF9V58h9UJMKNMioh8Calhhjj6CJFTxO5aJAZuJr7QgvfRmmrSADGTdIEGNJAxVoEgB0CpO6%2BC3MLeIbYeyJRbbo61XGV4dzE6PZSVvnnpOh6KxDMbPY6C%2FFcM8x%2B7pH0cn%2FI8oOJNPoxlJD2qLh0gEzYExhEu%2B0v4rS45svPHj%2Bh6pWubD8IUe%2F4vrxWraBjRVlCJiikyn4sJpVFsONnHVfZDzhUnEPWra2BvoL5YoNEVgFY01odasfg3t%2FcJCa8ggtQ8e6%2FGTIx2sD1duBba%2FokQezwp7YVyhqiY72ZP5FwYRjmfBw7b4fVjIXDpwgxfZ9S3u6Jpwujy0Civ1CSy%2B7oE%2BBwEmGH%2Bxo%2F4U8PBggY8gzgwr4uNvQY6pgH%2BNdpGjZxylXEZcGzgaKcIR6oM%2FxOArJJolaTD8XC3QagU9lcKWDCDn0spYt6ZxcoXNyR1fjD5WU%2FcIJUhgUKOxSBxb3pLwQt5%2BEkqnvKk3Lfkxl%2BLbeLR2ilkzAMxBPdGQxjBVrOPdU8Oqi%2BBlIFU5ZZRPG87jiqUQKqVxB1r6K7HmWfL7xzduzVVY9XRBBDlY%2BK6vaSR4k4cxkXM2clfnEhqqmol&X-Amz-Signature=2bc82431c2fe70ed276701026b3447998e9f805c9219fe65e0847848edf1a41a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BIJ4X2Q%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCpi8L7CcblLCZv%2BFVQDkfh0sWEl7gVi72oseowDaoU8AIhANw9JpMRk6UJRnpnuRpZKbO4Q59I6CkuiDVhgIhDSycxKv8DCEQQABoMNjM3NDIzMTgzODA1IgxfsdEoaioig7p311oq3AM2wm3OkH9PaGNi3re%2BDqqgsbaWC7EhDY12KoZIR0C3%2B3%2FsvkdwZwLadDio%2Fg2Q9l7fB%2B8ixZW7IjtLGbzOXAwixHADsZUiHrUM8gDajB2aaJoVLaLSoZ3IX3%2B9ddbYl%2Fcz9MmFZBTgQNzBwHDQQO2J9VVCK%2BsYOFIXzrlou1lqPTGLAoRzMSrjj%2FBjmTHFs4I%2BhjrYlIJ0%2Bj0DC6t%2BBVgxLv01gLCDa6nnGHgVEH2dk6hYhb5KcxG7u3aUOv%2FXsDPrz5XyvgDxcyMJdykOaFgaxXin1lgq735%2BWnMyOrUr6%2FgDhW7Zf53zep0hEEZk6gntvBA%2BvptMI105xI5Oz%2Bd0KNML%2Bg4tA2P89cQg2W2Mr81s9DP0fQFv%2FNZn%2Fcq9iuDZDt%2FRe4D19x%2FWFKDkc74PVj9zNVNhKQ9ZWD3HUnR3OV2eWEBU7dxS7uyvy250z3p1wGgqEtCgg67iJ5ZhVWqOTBY2%2BResy9vamZQyCqL4omLIIQ585cfvEVRVMn60ZhVkvRiFNeH7Rnj7RH1tQbpikfmMq4ET7wUe5thq4g9eDMkh80VrRChauJvr9eqDnwjGaAvQT%2FMhmxLuLbttJQOZITYKUL1AnwHXATot7wpKS1Yg3PgHTl6kNNpArjCFi429BjqkAT9e8xR5nDEy98n6OmhV8LQjHE5ggyRRe5UkWjNSLeEpTPl6LqbTmnf74CYZbLfhkdSkoEPDaPvn17FL4xQh0282fqcCPKQJBn0rB9wKyyKNNW6hpcSAAIEPNiu5MQAbRrOQYCwLuFDq6taoM%2FKp%2FyQf6uNgi97u17X26hXHy4cFBVWkGnifrQrlPPtxqBop908BcZJsEXgWJGgMKHLo9afYJva5&X-Amz-Signature=5a1cdc43ae828bd5f13e799e32821324361e1383453ea723eb329099dbb7ac81&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UH6WMY2G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD8Vp6prY09uPpDj3L0HLfKCj1ScB%2B1SXxtSvNzPe2H%2FQIhAIjngnoMyoyUTggpT8NfgfseYct6D%2FPKQe5FWvqcmsOYKv8DCEQQABoMNjM3NDIzMTgzODA1IgwfDbArOzAmXqT0Frwq3APIHX6mBldkHAjQAg9we91M42OsPxUWdKC8yxyf1za62dz05Dp8IxQJu0e8fBJR%2FAxXEuuNwIOhU7uW7p6A1XEqf0eatJZi%2BFCAFuC8kQv9QhlyoyVvvP5oTuKwGB94cBzV9yfsYc6tBWdGBUpSHrstqSj8eS6IODi3ooy0nQsXbZaiL9ceKJsaPUFbK0q4iaGFplGK5NPDTFb8o%2BNMpUc0%2FPRXz1FMDuKZvfkx8tiANDiVHjfu6fKMrCzILKW8Njg0mr2BnEBzwLy1EyqIbQRhNF7ZMjETwrUWTkGEgQX%2BCiM%2BE21phmLenLOXxqLOxYPg8Ab2euyYn0JxiaXwyW3nJO82JQWkjKEYCEDvZxbr8W3P2NfBSSIHwZTc%2F3CsZ%2B4nJWHXEXKvTb5DDyoJGPoE1lF0ftClJiTLP6%2Bqt5Avj7vhHDurTxK9lOqeya4u7rlyvap1PTcdo9xx%2B02mE41a72RBFaPQbNbVGK5Idmtn%2F6aHx2%2F3KRf%2B6Bhbtd%2BHe8mNcmKoCOGD11AaAnqvSCVgRi0QseGJo8ws2pqUPfkLmyx%2BuPFU7gsmBE101TsxxquB6N%2BN%2F9qX%2F3vhuFrxvhWzBAUvIzBhs6AAP2DZz9lgM9sMaa8WbGBRRyPpdjDeio29BjqkAfBx%2FMpkRgSlHXwKYEZyW874v40DsodgeHHVGgVLbALJn5MVbfFy3cxqsB4t4LCHMB3t4eSBpYrQu68OW8bBIVjvabgoLKHfs%2F1hfOzFJ95H7Jf4suRCv98EStprpCbgRoLlh8n2Xt%2BWuteVWVVvNwWj5HstBj%2FJmm4HNpqkONx4LT47YiSUz847VOMSqwK%2B%2FYeNz6uN3e%2FCec08R20O7Zxer4w9&X-Amz-Signature=f136a41b62c264eae71e6c801113eb3d1ebd9e5c083d26f87f0c7172fd9d931b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPQBNEMT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDhQOv0QavtRjTXbmiAqFXl%2Fa4Q%2F17oB0POEVI8Ntcl%2BQIhAKDm6L1zWvqSQ2rNv%2FyvM36AIP887CReOyct5k%2ByrqzFKv8DCEQQABoMNjM3NDIzMTgzODA1Igw%2BwIxChz3%2FsvK1ujQq3AM8nym43hNVkTHaXAR0deH6q3O5oZsAFdnlSivAdCVNBkmrqjGXYO3cMUa0vaUw5Rff3avxIuaCd0qRFkx1XHyETpvbwQ58ZXORBQOD1yDBruc7E9QRIaGf3NuScjhZYlc54GOb2%2Fh3HgABxol%2FJvDGDiNRjUA%2Fnhwl%2F0JTcsaDpYwQ2VnW2qKnicgwAJw9lGixVqvciiB9n10YdLh00qE%2Fy0yD%2B0FfXoB99YNPKFwKRy4RBaNa89rZEKfcTC%2BZraipXbVQmnprb7bi3xIuXum0rM2IpTRL5pizom4SnaPRSQe9Sit%2FWXzYr0OGHA3pManao8u%2BtiVAMxSj4b2tnQWNh1oyFtExbFr6aTRYCk97VMbNzYFQLbDc%2FlKoGYVwgp9%2F86OswVLwq1dYONHhb8D59LdxnSpCAL17eprseArSBzfDbLB921Di5dpSzFOiv3ZVAXWSmEXWbkX%2BlU5MYJzj2Pmcm8KTd1tS2lIGqSsAZ4yuB4wktnrHZn8MydN9gT2h8XSlRhNLuW55hC%2BmucpvSIPl0wZ0TiapEJn9go%2BpeXiBcHHZvcToTJWdoakGWu6G%2B4dvr13ucRDcbYnBwPpYXH%2FJil%2B2H68KPQM%2FXQMPuU2MrYEuxLPCNQlzojC1i429BjqkAalxzyraOLk5cRwixyhQGb6WExIWH7sqG2rlyDmq7NOZgO246Je7H43a6YS%2FGoz3DaqUaw8%2F3j8QBFBdHnK0F13CxXIYbIV1ZI1FEvE30FRNQvGlegTqkUL0AD9vLpvuPi8ysbtMnwGeKBL%2BS5LOQ7wGPJ635TsvlkDwRnwaLTQXqrNb7XGnaMRYtxlRgeNO5GO0GASpY3Vq1uqoQJYqbg4R8EVE&X-Amz-Signature=7a091e9090211591b60dbb8f9f125c156a2b33c20036c04ed58ab9e12ceedde1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RT3YHTG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCd0mrQxpXhDAemGSijf%2Bon5YG%2BHz2SdzLGAH8N5mxcTwIhAJ%2FuJST1EjpM1u4Yacgh3Yp%2FGU6lg%2FnzsFcbog3xfxlNKv8DCEQQABoMNjM3NDIzMTgzODA1Igy894I6QcN7BOfbyGEq3ANeW2xdU%2F0xWOgKrUpqdaujIc543B5yjKUc24gwKY6%2F%2FK9ReSbWtiHo9387dyof8EYoxkY4BeIVeAqV17ot6uPai19ggL5LbM6%2BAFMrmXR5xhrQ6fN3rOSZUfq10h7E2fgYj%2FIG36A29BaKsV2fz7VVYW0V8ODb5WUhtpxvjQHJqC8GoAiiKc4Hfj9Fnu8OaOgKXvHclryhm9VuOOOigum2JG78BFeR8FebgAFIQ%2BKkwUvix3kWpQX3I9uLzjsA4XZmgi40wA56hwPblh9xtiLAMR7WOnaioaXoO8e0QTRfHvarFq3fSbWkUcL5xaDWG68qjjgNWgLN2AZktR%2FjFifQgYfno14ksHaav4pE73ISdwO%2BYz333vXrAnGYAmXIcHE%2F8RHjs8wCsnUWt8E6CLoh984CUxeasBXlVPfSdjyev0pLnocUQ9EuaRWw4GPbnuH4fTT6Bva0rsD9t56wGdygZ4vnxFjXlkqT40i8T2wSminXAU78n4etpzT1MmUoCbA9niCLMqA3p7MUgvpNZ9ioWsShnzV%2BCQ2Oucl4DD%2FzvN0fbjcadE6b6Ny%2FKrtCv6XuhxF4s%2FFh3APuINJdtvqPfCKwFAR%2BcMbdRJTkYU0%2FYMadRApBRlQyrwkkdDCdi429BjqkAXnn14hN7sFOEyD3P34JnyY8ven02W%2Ft40L9HDkb7DOAtSOxbPjQm7cEmcLwOzFjbDeFIYJY83yL6tG06ZR7EaBrnzJgxDZ7Wi2itJPvrfxgImqgQ7FTEwIqGZYBKi9hbKYZcMwYCwk7SUSlBy2npb8LhaAhAsa3V630dDs%2F6GQax7WRMijtj2FkYCwdP5KGT8CAgNr3Td5SSiXspEP%2FiIpLn72X&X-Amz-Signature=661e4982aabe85393516fc099c5de57f193dab20e295c4fa7f044f709f5a73e8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4WDHYFM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIBBL7ZIN44hYpb%2FgQn51H4f9HIddpDOitjc5UKwXssCwAiBj8TcSDD%2FrqMyw9ka29EimIiCoWLfjzw1tWsy9PR0meSr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMrDb7CZZ5qtHlEW1CKtwDH42NHnTBFINWHaKmtlBMvYypLVp09vXT50VQo%2B6e%2FSMmftQ2TWdJaQLFgZHtS8tRMqQ%2F7H4bSeaI0EAilJeakrexVeo4QlP61LbqgPigqB052ahgnRNtPHNHEKPKJzfDWpB4IZM0i9ZhiUqOfdFEM91tz9imbFgZuDlqUS2JToJE2VVGihQWu5i7TkttyJomvZkE%2BvLO4xeqlsXi0Gv8mfBDZgIyoFFHITyB6PBIi560yi6Yv65UFrq%2F68ulHMl4U04KMdSfxU3Vk%2Fs%2FcEGhN%2Fj2b3MZoFx0eFqjUMJHQe84CroXFYTC9QDrrVdabUXfZA20nhX1NIDxmRu4o0f2FVisq0UfjCPMdy%2BRocwlh9AzK4mPav3tSrllykJ300J2hgG0uHly9iKQedOiEAqpbpKPGBVbVAKRXZeck1tdlT8cJI29FV1rSF9WkqHSnOMHj1LxLF8F76NJ7aD1D7%2FjbV17Y6uN6o1i0orj8q%2B5npLNNRu%2B5cATckc22wUcVfzv4kejqkqF8PnsRVuWHy0dVkGhANw39ChGcaXHjRZGn%2FvmF0nuF1yR0BhdhgkEwHJD4CaO%2Byi8MjCqvBaQGTeU2C%2FGiLLEUdxZj4oaI4uu2DdNhGCuXA%2F5lfbz2IAwnIuNvQY6pgF2oYu6qYdhHtRJwtdssYPYUfKNkdSJFKPnqhjGDeqJbu6U%2FeCPq%2B8lIN%2FYHm0oZkIsCArAUx7IhudOOOyiq%2BD5M7LyXCMq89Woo0tKLTzRDVVSaAP9HAI76OzYFS57z88qH%2F1yNAtl0x3hNkKgmAet9BvRwjUagQulnCmbWRQlodOAOlquxSvX7OlOYUhJwKtuAqFLtAFVm%2F58JgI5YpixiCJLjW9U&X-Amz-Signature=b846f455b732f9d88c7d2cd8260da360bb641ede3105fa2b82dece03dac1e16d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466227BRN64%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIHU3oQ12KKa%2BbutJWQKpKtVBRfG4%2F49YtYq3j6DYdQAPAiEA9IdCQflVA5asq15BQzde8dnQAMqImeqNWJM7jC4xv6Eq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDOOUeaoEl5H3T6wI6yrcA0xP9H4Y8xlB2TbYoWUeHix%2ByFGVMHN9xmfHgACE8W0iVhpD4I5hptczheYNuRfNVZp3Lam0%2FnPEry4dmQItA3Y0reo5PAxwPk%2FBAnZ1Hu9D3N9zfbuwMF2SNUq3gFqPIdTx2%2BUWy88HCnRR4i%2F8e51AnP1qro7CsNicAXc4DgW83To6tglkCYPZf2W3gWp1516ZWuYrU3fGVcqqoSDE0bAuNAvyYlZDFSB%2Bxn3NebgL2GJRgAB5flzPQeeuEnBLcm0WfeEYFsVF7kf3rt2qEwD2xYygGEXaTA9K1GDNCDP6U3HYRCbO24Wcs8hrSn6B1Qq%2BncxSrejqMZEIMMGZaD1Wgu0NnnGrV95XSDJ%2Bx2FyxkOOKf8YnJNujy8U05sJyysOaPRBp9p82fpc%2BSGtrFInXpvIJOc3MalZKv5SO6Lz4dpsmmOB8FASeCLaOVB%2B9wS%2FWsJY7NYn83oeubiS8NuUlhulk5S398bOgH4fU5cfx4SsaReLzEpaxVdKjd7YkAajJdReqY6vqOEfebYHRkWT8fsK60g6yg4658M51bSF000lJGU8WIA95FiXGYtq%2FHFIUXfqFUo3BX3VIZx2bXM2I4RcgCkzDHPjyVAzcORYhzRz19EU9L5G606SMPGKjb0GOqUBsKzOzaxWfY8%2F%2FcYWKMK%2Bo%2BkxxFkFuvPSbEsushqTKkBwJ8rKFavWRDs4WxCYVcUMRgI62hKbflkwRzH7MISb7uYc29rmmq%2F7fM2UBnSAdnL%2FPcrAK4av69gOV1tOqAY%2F%2Fq0JVRjX7X9DrTVuLk5lydrg8yw5boQdaxefky3xWYdeaaDc3grGMfUtDvO%2B5tKAEzQzYCv03J3IWCRHL3L2W8SgZNsb&X-Amz-Signature=29fb789480132d10f145134c4c791d53b5b97b9574d0725a42d6a2d8888be5d6&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636IOA77M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCICGElByScXpwejRgeu0ZnyGWJ6%2B8BvMFLekxeNTrZR%2F6AiAPCLNFlCybBA4Nei9yRQrVfPY3UARJz%2FJ9oiGEeHalmyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMi7V%2Fy6COfV6yDw0aKtwDQu28twuMvnlZoZU97p8uiszKEeHlkMKlu%2FDy%2Fl0xrULZRoTt2mVixng505iR6gRwGhjYLi82Teic3UnyMVqjeLVIyhhnC3Lcbo%2BoJ1roJRTKDWgtGD6mL1ScAOI%2BtOxFW95cbpRk59h75xjX5G%2FSIXVhYyCr7Z6hIS9rdCtfi2ykGOwVdMtwIGQVMy14PEvA9bWlAcI4fdrIRsspg5P4RlRBZyNXQQE8mdcCPDqDHvMDTP51WKdONIw71vidAMTL4B%2FYOaA9Ph1QXzLnFyQ00vY0WQinGwegofT3E70PwFApI7CE3UySIxYNfW4HfhhcST0hIBNDxmQmsa0j0u1VFSM5%2BEd4xV4hrBHTi134CVmj%2FE4zEatfJPy10sna%2BG20jd9BqlpTlJSIylSH7PSzW29vG7K2CE9XyB91CdaUZ4OlYFDlWQns8OtJru1srZZG0XwdRHHpsFjccKP3BrFc5C564O0TCUSwyCyCDaPtqHzrxc1IRzCAorY%2BhptZlEyk220zg0%2FIAIBhhwtOKXciVQaHg8NsHx%2FvAiuZi9zyVNl7BV47YCVim8r09VGL7EwlM1Z1WLEamQiVMaT117tajp8hGxI9s6uo8T0m7w3vqOR64geIY5C3%2BE7FKqwwuouNvQY6pgED2C1xq9g9FqmCXuUPqxdiPwiZhm5LbHjIlgijqhoWUy8aDxUp8fkO5nFZozVbiRclMzlMJ4xNWzkaebd5jT3CLzt5HNqtkbaMl1%2B8hfRxSYP%2FWwpho0qBGYQswqoYlcALcsQ%2BrAk3y4vYkZkV2mAQG2bs%2FXzKfr85VufbGUSkKG9Ft2F98ppWmEa8%2BNH3qGPca30wobiW1LL%2FKbOY1ZgSxuVpCfw5&X-Amz-Signature=8356228a476e99e209b8186a84d9c5728c02d62dcd656c39027fc242b8ffa754&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RT3YHTG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCd0mrQxpXhDAemGSijf%2Bon5YG%2BHz2SdzLGAH8N5mxcTwIhAJ%2FuJST1EjpM1u4Yacgh3Yp%2FGU6lg%2FnzsFcbog3xfxlNKv8DCEQQABoMNjM3NDIzMTgzODA1Igy894I6QcN7BOfbyGEq3ANeW2xdU%2F0xWOgKrUpqdaujIc543B5yjKUc24gwKY6%2F%2FK9ReSbWtiHo9387dyof8EYoxkY4BeIVeAqV17ot6uPai19ggL5LbM6%2BAFMrmXR5xhrQ6fN3rOSZUfq10h7E2fgYj%2FIG36A29BaKsV2fz7VVYW0V8ODb5WUhtpxvjQHJqC8GoAiiKc4Hfj9Fnu8OaOgKXvHclryhm9VuOOOigum2JG78BFeR8FebgAFIQ%2BKkwUvix3kWpQX3I9uLzjsA4XZmgi40wA56hwPblh9xtiLAMR7WOnaioaXoO8e0QTRfHvarFq3fSbWkUcL5xaDWG68qjjgNWgLN2AZktR%2FjFifQgYfno14ksHaav4pE73ISdwO%2BYz333vXrAnGYAmXIcHE%2F8RHjs8wCsnUWt8E6CLoh984CUxeasBXlVPfSdjyev0pLnocUQ9EuaRWw4GPbnuH4fTT6Bva0rsD9t56wGdygZ4vnxFjXlkqT40i8T2wSminXAU78n4etpzT1MmUoCbA9niCLMqA3p7MUgvpNZ9ioWsShnzV%2BCQ2Oucl4DD%2FzvN0fbjcadE6b6Ny%2FKrtCv6XuhxF4s%2FFh3APuINJdtvqPfCKwFAR%2BcMbdRJTkYU0%2FYMadRApBRlQyrwkkdDCdi429BjqkAXnn14hN7sFOEyD3P34JnyY8ven02W%2Ft40L9HDkb7DOAtSOxbPjQm7cEmcLwOzFjbDeFIYJY83yL6tG06ZR7EaBrnzJgxDZ7Wi2itJPvrfxgImqgQ7FTEwIqGZYBKi9hbKYZcMwYCwk7SUSlBy2npb8LhaAhAsa3V630dDs%2F6GQax7WRMijtj2FkYCwdP5KGT8CAgNr3Td5SSiXspEP%2FiIpLn72X&X-Amz-Signature=3e2c944e224c824c842471714971905a7d0af190b5379584dfdee368874c2f71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GBSIH6N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIDslhYX0BgqWENmitESY%2FQdlKM8y0HEt6fEDnTCBMj3%2FAiB9QnpHMWhoEfDM5%2FpAxLNYQIou87ormthrV8xdeOsWSyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMBs9%2BebrVY5lSX9%2FfKtwDJokwhLvPgJUE58KXdg7IbHlAkVhlVBylLckSGYUENsSjyn6oKr2pugxubim6T9dILletIG2%2FkRxUxbqFhoFTRSvpZFg6QXY61VvIdQQrKFAAeVPjCyeG9a5eIJ%2B8NBh6iAakq6JqavIcxH%2FlTCjVOfwSWZSmzMvggXNRFko4zcnqT1egrJE1NXg8UPdTabKfhqXGeHDmCtvA7La12EuA6auq%2Bcik2zSpu8CUXEhx2RvBFazbGORV8U%2FduMeyowFLEHsOo%2Ba2%2BGeRzijssHiLeRe1OIqU8rGltaXEERVeem5Qsrf5%2FjgPJRj6DUJNMrXcKpjLX8GksHteXIqx%2FalasdXth6%2B%2Bso5t9zUIEeMhe06r2KBxmtjykPPx0Zkvn6Q8t%2BNSp%2FxYjviCgvxOUVjJ%2FdgtQUr4ShOdD4xLh47ho1WfwdjAc3YWV61AebGJdIqiATMHXfvHALDveeRon%2FEHTJL7ivrk21iWCw8ylEySRJsZsXup3qCqV2b0zIZfNzATzfS7Msj2%2FtNsqe7WJ0Z4MPw4a%2FdprFkP0IZE4zXm0iKuOJOlen5uYCoBpsOq6xbyIdzAGooTPRFU4EMEPiZcMt6W0LbwKcAlUKVkIIu6g8yvqRZB3MQzRwip8vUw3IqNvQY6pgEuUkd568I5IWQgS1J%2Fb37aM7vsSwwjmxE3%2B8jZLrXQ%2FCrK70pBVWC0%2FG%2FjfVGrGTYH7DONUmslXjHDtNm%2BNHV5Jxsf7qWFHGzWAvui8eMeFxsXwZmex8t99lM5%2BFZz%2BFDgmHcb9RznCwCwJmKMNwE2tfaTyCc92jUG5TUmN2i2%2BE8YXwc%2BvJAzlKyfW5lQQI%2Fi6Vnd%2F8nXh0no4YtDYfe3MY9M8LZC&X-Amz-Signature=2b921a7ff8c0b376f9fefe5724c032d0e0d32a27e95e980582ded0734ce84a25&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GBSIH6N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIDslhYX0BgqWENmitESY%2FQdlKM8y0HEt6fEDnTCBMj3%2FAiB9QnpHMWhoEfDM5%2FpAxLNYQIou87ormthrV8xdeOsWSyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMBs9%2BebrVY5lSX9%2FfKtwDJokwhLvPgJUE58KXdg7IbHlAkVhlVBylLckSGYUENsSjyn6oKr2pugxubim6T9dILletIG2%2FkRxUxbqFhoFTRSvpZFg6QXY61VvIdQQrKFAAeVPjCyeG9a5eIJ%2B8NBh6iAakq6JqavIcxH%2FlTCjVOfwSWZSmzMvggXNRFko4zcnqT1egrJE1NXg8UPdTabKfhqXGeHDmCtvA7La12EuA6auq%2Bcik2zSpu8CUXEhx2RvBFazbGORV8U%2FduMeyowFLEHsOo%2Ba2%2BGeRzijssHiLeRe1OIqU8rGltaXEERVeem5Qsrf5%2FjgPJRj6DUJNMrXcKpjLX8GksHteXIqx%2FalasdXth6%2B%2Bso5t9zUIEeMhe06r2KBxmtjykPPx0Zkvn6Q8t%2BNSp%2FxYjviCgvxOUVjJ%2FdgtQUr4ShOdD4xLh47ho1WfwdjAc3YWV61AebGJdIqiATMHXfvHALDveeRon%2FEHTJL7ivrk21iWCw8ylEySRJsZsXup3qCqV2b0zIZfNzATzfS7Msj2%2FtNsqe7WJ0Z4MPw4a%2FdprFkP0IZE4zXm0iKuOJOlen5uYCoBpsOq6xbyIdzAGooTPRFU4EMEPiZcMt6W0LbwKcAlUKVkIIu6g8yvqRZB3MQzRwip8vUw3IqNvQY6pgEuUkd568I5IWQgS1J%2Fb37aM7vsSwwjmxE3%2B8jZLrXQ%2FCrK70pBVWC0%2FG%2FjfVGrGTYH7DONUmslXjHDtNm%2BNHV5Jxsf7qWFHGzWAvui8eMeFxsXwZmex8t99lM5%2BFZz%2BFDgmHcb9RznCwCwJmKMNwE2tfaTyCc92jUG5TUmN2i2%2BE8YXwc%2BvJAzlKyfW5lQQI%2Fi6Vnd%2F8nXh0no4YtDYfe3MY9M8LZC&X-Amz-Signature=9b752895072c71584757f2dedc417ea95a704634f2972ad40337f031d89abf69&X-Amz-SignedHeaders=host&x-id=GetObject)
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