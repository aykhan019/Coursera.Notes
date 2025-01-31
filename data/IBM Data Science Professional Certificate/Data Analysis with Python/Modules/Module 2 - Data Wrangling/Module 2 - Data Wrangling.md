

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FSOG746%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtKqgIBhL7768gVJwTeJiYs41ldQ6BLddEUzLm%2BL5fngIhALzunj%2BJ55dyAidR8LUvRkF03tU5PhYbbWcbHs%2FI6mkCKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYu4ul%2FwYT1oUfLuoq3ANM%2FWliq6Ht%2FR4Zyche1QodLhD9Y6x6j3JEQCNFr2TiY0%2B%2BES2whlF9vXFW6ffxEVJut9A4uTeTn2mHIx2rtXz2heLuoYnKWUrzq1fC9h27SPRqmxBrcRl9CdDUraORrQNCvpmjBIhwzdHfduXgoRxRvjTDqzepsYyUK3uAG1COcCk5dGtOrKNl2vkzuBb3IW6uM%2FHKS%2BMrLt%2FkQ53YsjLibF36sWCkax7eot%2FYxS%2B5pJDM2OTAFqp3eNTF83%2BbGogeVoENIaoSaMKkrwO1P8BhAAvuYJJFuCMpt%2Ft42CJ2nx6gnNbC5ZZBZJ1zYexF5lJkq21Bkr%2Bh4hNYq%2Fe37ud6dzmT1bIlg5CDJRNcnkzGI%2BkTH8dfmHK3%2FZmOX9LdFehIwaFIbil%2BCmzAKWGB%2Fl85juEWNDJZutiocpOZIEeMY%2FYMuPKcMVYNibu%2Ban9HA8nQi2RJLqdgM0noYM4fZWsvUTB9QqXKCoZWHT15yClIsZ%2BEW98GAcFeJw0ynfWsb2o%2F7QtLPKtHKlCo7ZXrQ4LwprW8mJPyOk5row6ATdH528kv5%2Fw5w%2BRFAkAJFTHUz2%2Br8MGDJGqAQJnOV5f39pszigK%2FkSQl2zq%2BP5xqVWwGgyD2epB%2BnzfBZciJ4jDhrPO8BjqkAZHh12VlpAUN%2FbW7z4IQA4UC0872IeGBqwjS1266%2B09Jfh%2BqpnLE63MzXIjWWOzlT0oybVg%2FyaMoC8xNW7gdMaBzh7AjNuAyznDCPAJDy8L3jHSZGrprollpO3qtbmZ5FyKL8obuka3jPgykROkAmea2wqMPys%2BYbhMSnVpkMaBwBSQi6q5xSJ9%2FD1QG61Qha0kZGlC1VN8l0vyCrawY6Vr8lKow&X-Amz-Signature=c7cf8fbf3410da5b5551d01d6db36a25449d694f2db201c5b741de0c3ece88b1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XSU7YPV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICj1kPWTCWvEysfBgsB78jllXfAt1ec9YbbTQbDlflyjAiEA9uxDFXukZTwTL0Plamh45m7JiPuwM0RRgzlxdFkS%2FGcqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQuTAgnqsah4NqqnircA2%2BMYR4XHyqQA3b9E0PXuEBBmTOgNpTNBqVkuifUEyZ1g%2B%2BcWxuBi%2FmNP4kMZ3Eb5omsfup%2B7bWv8cJ%2FFirMGQIaOidsyTWpR1Ew73LasjapHDWkxcnYioERVGvgesYODsoe8Hsr6hlLpw1S85yZTajxObkg%2FV1UtR2eNKE4WXY%2FIIA%2FZD7uOCVP7aRmcN0%2BpUhEDvf1Jj2kOGaOk1kfkLBtR1Kog5U8eNmo1J2TBN9mZPhu4U2RJeQyU7qU5RwFr7y2L0zWGS8HdteBkqZU3LV%2BDOBYyIGKBDMtqaGU1CpZSXStFn1Hs0T%2Bk6CQEww3LwJnWpL6ss4vEXZwibEKgVueiA9M9CEW2XOF8yRGGWbA0qnYDYtXWyARMkUp4f5xLQvqT9AeOCyPugb%2BfJ9GyFk55lmPAt6NXClOmmPWWpfkFhTz1NeOj%2FU4GXu6YR2Ju837QSr9Pv6zEOFDRE3YIleTAIDSPXDgYp047N%2Bq2XWodM9JeaA3GJkQxZBCsU7qZtb09wyIYxwjBNwLj3W%2BB5iNOpGYMnlTQxBuzsNhQHxZliHsP9hYq4GofobYixrUbLwjAKQWTXxDIpTIsj7cLK5iuQqpBk2W0oEoOpn7RRSQapCQjUogkhcoXugTMM6s87wGOqUBsfHZRAT9gHWSwtk02RmBCBb2kMKbvtlicUvBQxGPBz8FTqm3pdcCXughFrdkIQqxCEwliBiOUBi%2FKndGgMu1qakSGNUi4zAxbWvqalVaylLJ60NTsxzhjdv%2Frxnpn7h4xth%2FCAzVx0BeZKMosHOCVA554oCgxOeEc3JihvpIDXzbV0bGRFaFe04iXZB4MJme2uCCBItKvvIeUw345E8fP5kegFPb&X-Amz-Signature=e99c1d97b422fc35d74b563d4eddfd1e1e313a3725d25e2c008cd84995af661c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JFASGWR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICRdv5nuYOFKzBd3RFUFe3Y8pD1DJ9A4S%2F0Phhre%2BRNRAiEAw2%2FEz0ROfT3nMLo%2BIW%2BUKOJM27aoxmJO6tl2nZo9LRwqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCvi1QNw7VjhA2Wv6CrcA6OeQaGggKEau2whM1Bv3mcmWT8He6iHg0lhzJs26E7BvG9rULj003iTpU%2B3GCDToE5%2BUrTQnSDdEPBZs%2BgQWpZR1NNOeHKkrWwp%2Bz1GsEGO1I9JOYiYKOtjwLSneZ5fTMCZjeGtlMRvXwRkq7TXfk5DjhCSmPtiWpJmF3WWU4OHr9XeuXMJq5rJ8PfbBJLnQ%2FiPv12aF7rvOK%2F2TN7XalatawG%2FVvZghfXuAOXIRFQK8lv%2FCKhJGDJ8kl6oZ8%2FkzcbrVLB242gsKfC79SXiTTPZOxLQBT64oszyJ3iVPJsq7EdCBq1eNoUjKHzAYW3eKvu3YIr7P711p9RTxJFuyfB9s9%2FhOQrUWfuvXRp4zrE1kgQYLmraSEucx6XZfv5L%2FgzquarVs4r0s1luhh7X7wWchB%2FKjpObd3YFArMiNJolQEsVQcFFKlmQVOgIQs0t32bl4R45h1dvVCdxO2PImTbitff1Med%2BctpI4b%2FeL1r0r4ivPl5aMDzAqvDb311MKWRzvDNMAM%2B5SxTS1ExaMxuAeWDIUD8AWAqi8Fs0JbjASyiQrQvYbU9LqEGLvqzFxzU45QA5FZ2aoPPmA5mO%2Fc7YsS1iyV%2FZvzb8d%2FLgQQkvkARfMXkPr%2BHlSp5cMK%2Bs87wGOqUBehwTsiSEk6SBNY8eCJm3k1KItrVeIm%2Bag763kafJ4NI0kWpbILzZHuJcHmn%2Bldsuxg8YPhY7upv5rYooVINsiPbDHhMx2GG3H0B5JBz3Jqd6XyOC11C%2F%2FS%2FJ%2FaZK9OUww7ZWhCIRYE4nN%2Fucnqj6JmIuh8eyS8Sp%2F%2BdPqXqt2MBstUZwZyZYa8j9%2BW8bPRh3%2Fl9KlL3wsFnZizcltbThPCD8dBbj&X-Amz-Signature=2264180d535d8470cf0ad3928407c938934c77e7779dc4fdd1d452d0df8a1949&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TKRX7L3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAeM4uafX1qMqJSGPpXJjmZpJ3kAX2kJbmlf4ExuqB9sAiEAk4ql%2FnEMkuGw%2FtpLgS3wzsFxaMvcVfaAZQSKyPRrUEYqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJdod8ndoNHcN3SKYCrcA3EsJ%2BWXd6A7q6sKHTVR3h2DzJaWbwDPd8OQt8xLy8XhBHFnfrApPbwn8PpVF4uBuUzk%2FivN%2F1jZ9V0aLjRZD%2FlCdNx0GztpE%2FtcXhuaTIG7tFKQ%2BDenifDdNZfifN3%2B4TbmHAtj4iX%2FH%2BUC57LaGwDfdKO8ucxDItPFXbxYa6V8%2F0rBd6z6an41nldWaqt%2BPZbMHH7qgyqJFDN7fZlWQhI%2BYvcf7u%2BeLSU7P0KwQCQiLd940bdVOEV5XcOAEfnQxqF7JJ8VHURRm7X%2FefaZt9Mhd8FcbIxdtaDx2KjdlrCaoKALwapN%2BXacaeQsM%2F2LnT4UBEr8dA%2FqIyj2IRpv04ltDsmEms4wDm%2Fa%2FmUyq%2BQ4yVaITp%2FSZo8MdQSB78R9XcnCWTL6WMxL7aeZqWSWlje9QBrx91CeyW7k3FklfG4QUEeC6kCg%2BPjUTdnn3go%2FEiS1PZx3mzq43hKPTPYFJlgtB7K%2Fr1ydN09PT0pw8ivq2Y6SNST75GMNCLUeRX6qzwq3d6tSPe%2Fdj8%2F9rhH8VVdDzGYGeLZ2uiX1dmPt5%2B9RX%2FoEIXhLDdmVzrqoGctQCzrkpmAhr%2FHIk9VU2LCH%2BJ8l8AAeIb8CVYTcZLId3lVciLrIuzmcdGnnZ0L5MLus87wGOqUB6FBinq70TbiIUg9j1kVa3sq%2B1jy6JN0xEanw7KGQALrJNh08Zl0D1at1wfdP002GAkvKi1LTlEaedC70WTchYSjjNhrd%2B5BItPzEotkAxvAEh%2BWpxEp4qcvwUoomrAa2dUVAbT8F7itjsjedXwrvnQ70AZiqkq5ySVcVjVZeHjydf2BDZ2ftFB6j%2B35wh7nAM0lbOL1I2GILoVIjB8KpM8WTzQU6&X-Amz-Signature=37c5082107cc3c81c5c0b786d3674627a315a974dae40fb6fbdebbf3d8a1f7e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5YYP2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfkPRWUnoUg3fZHKAwZPPCawkkHgOKQ1%2Bkm%2B2b1vgmPwIhAMdOumvNpyOGy%2BM5V%2FDgRXuDx%2BNmIZg1UDIa2FwqJYMaKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMUEipphfuZkE3tfQq3ANZSQHkz3WW71hsZXa4m2Qii8vLQcCJQz3Dwz812Gv3%2F7r%2BjSaMIvEqKqzvYMVnCk8pbfMuonCEPiN2yvWqIKGb2w6TLbcXtiTsOBzasNcTCZ50sdrA%2BobLLkaMtylqvVq1gjyWrE9dQM%2BAPBZtvmAp7v7MUns6IkEqda0TxDoOjN%2FSKn40WRm9tcbgWyooWA3GzxIwTKyyKNLmlvAb3aLOt3CJ72icByfWnAFCSK8K83VoQmUKOyf%2BjqZNL7VoT2uiAw6wkWWZ4gAbY2yuWPQ3GX3GSK9gTGzotM0sICiwkah5g2XXZaj%2BOBLxoXm57Hmwaa%2Bx%2F4ukDLX5YZbfA3MkgYXlOvDd88QHnyI1D4GK9JosyU%2FCi%2BaQwEkxJS6GmgngdSElqP9l5nyF0N8GQ1Rgz8wnfuZHOiJ54GEQazbjdGZkijH0HEVFn7HzFH1pOeIHMis1ObMnMmrzIDRukPDEitPJHYR8B5tQ9bFKEoVUkb%2FIVUZjLMPMNv1OzkopjKXMMQxWD1jo6SJHdNQBUeIPQ4GIiOQSCK1Kvjexfa2f6YZqHbdmr9F9bLsd92NKHpPxR5agdtKpShEuagFnp9rCfTiPFe7BS6oubdt6UWy2O2ZXFBlEx3nxfsZHZzC7rPO8BjqkAR3tuYM6gThoWkhiiGOPzu2TqJKLBZn%2BxFhMNc89c2STsJyebn%2FcSikihlT5tDq5j%2Brr4rw3Qir%2Bd%2F0YqgdvBKBiTkXlhP73O1UsBXsvYgr6z19iQXbQvy4YJP%2F57jN%2BMzf1%2FXDdAie39jH21pGFwfnA7jZMs%2BMAoKz89W4rPNIfLr7LC%2FwHl%2BZf7I7Z5QCckKnM2HdzaOmlGoEwcYdz3Tq1SgIM&X-Amz-Signature=33bc983841441b2ca9ff5f37b3abc00c9729043b44dbe7fee8636930acb301c7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMGGPI47%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCxFKcyhCSQX0dx46%2FCHgKuZWPVNSxb08y%2FY7oTvI6aRgIhAJ9Mv3bU16MO%2FXcf87sVBVFb0Do6MF2gXYkefkYuE%2BZkKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxnpLbc73JcXrgZmAq3ANIixy72iNvsb%2BniFBTVdqC77wS929iE3pCJF64q1F0tXHmVB3560qg2vfMCP9%2F0ugvhEk05nWk5JS0eXWy2MKusGWn4Zqqf3VY1TTl4K3e9JoLcBCn93pfUK9leez%2FXjo636xrm23gfeizIJgrwRKYie2CwG69PFtK4pFK5oMGYszJXWxVHWh3JVkSSnHbXX%2Bnrxu6O7mmHPTQWsg2nbsJgMr%2B0clanUNfzLpt50Ike%2BhJiKw4LATASwMeHZEAxGUMYMV79Kp3EgU7gsJkp9HyXhCTNiQMiil%2BIJVtAvIHg1GQOpsTFegokCuDYPJVKhMiEHza0xeD3v1XeE15h8snKC1Z2aCW9thN5mZbvRTpPkWRb%2FBykDHFjAWwveLA4zUSAxm8D5m7rykm2OlUT20pvBgZEs6cxraV7KGSNPqMvyEKMg9EOD3%2FUM7F9FIkBM4Tn3j1SNHt9%2F9C87GEzzGQQtUHJpWFIHU%2FEl%2FHsks9g5KtEa9rjf6218lFbu5BN6lJBv1R0C1vbIJ4VbzARCINXtYBLdbaGWNcYaTTlHY1x%2FNYCl27HXkbP0YPXI%2FiOvsCfvcNrAROwNN8FJDh32mjX3wyhpiFlmwqpcwkXPEJRklZkOZlAu5I%2Fm%2FZvjD5rPO8BjqkAVUtQo9oM9k9WZXflOyvfke1JLiHPvC3Me99zYOD33SH0N%2FEXfEKfos%2Ftezymj665KPw3SY6o4krR5ts8Y0XHAQUpH6r3C0kbGJffDF5J654wMgZ%2Fl8kRskxV7vJ53Q96Oet0FIeNRk09JqFeohs9BMtR08pVE0y9hwSjWpysMX44zIOgqYBz3I%2BgcdvfwfyGBQVxgA4bck50SlNNNZn3UmhrqRF&X-Amz-Signature=9955442366ccf598e99f87c71eecb46332d36c62a18b13f2067f64cd40ac9ce3&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLOLFUFQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEE2wa97DQIYM%2FdjzfA%2BHmjuA1g7HIRZS%2BSYkE0flOcpAiEA1kmEctohfxDViv37k54kXOJAogqw9wnArH37whfKFwcqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFcgtXYR5Xaqw%2FMCkircA6g3mqfjcfQHOaGbdjdM2pjgHV4QW5eptmN%2ByJRll7xGOgCk8G5BpfrtW7HNJHIJ225%2BlNyFG6C1e3eCvltTzxW7t2dLmC8HOxphhEuOqTUp9tqH3tYLhQNLPQelFJv3iGsw8S0Ul2oS1bpCgdP9LdCRzNyGs7wYG4lccBkJoi%2BdGM5dKVhSHMwySzA6IbofF8lK%2BsFqNTiOlEhTTqB4wxiyWFMjgKLF5mBPIw%2BWqjmRmyugzYs71%2FWKYRR6A%2BB0wwm5nWnLjpJa%2BjSX%2FVC9c%2FELJJoTHA4qCM8cbBB6XKISDbuAAxH1KbQZ77hqYVkNgFvG2Z%2BlZiieLHnlZKlnboVd1N6llfq0G5WegAg2Npygnh7s%2FSnq1qDnayXOxVzqKjfaXgppaZFbDhO%2BVsv4jEy47L%2BclsAaSK2QZfngXxfL2LzlsG071rul7%2F78r2qkyfFjCC93RQ2rVSq47Z84AGclskc4M0mWliu7BpY0O9IS4%2BUgjYKrzZuJDbXEGhrS5HZaYut6DlOKjCaorKU6Y6W4a4x37%2BOs%2FoLjyzmV%2BQeOaRgYj1MfUMgiMQ%2FXBfd80safXmTYsEcUVqwkL8dJNSoOZc9xADzyleGSZGJ95qTyzAhnNI31r641uPCDMOys87wGOqUBJpHGrWtPo0HPw7mSeHssGc0lS90GxdTQZsiRYBO63JGt7dYVmOXGQyYV8AgAMMsJbW1DpOzE6LRqpKbhlhC2X4hY9NCrzvR9A8BTSotuf7vMOspyESWbSKaNeGzpJJFLD0fIE1MPQ8HS9WoFKaanl%2Brs5xTQOndnP6AfpxJONQ43Sokezd1hGhvKqnScqKx2lrTr1WL%2FzeedPZtvSlT7HB8LSvjC&X-Amz-Signature=a407ca1f1beac5ca2b57e0b8c1246065ea174cfbc110d9839c1b15455997883f&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCZQGUCE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCy0O8ZrZdOadd%2FAPkfwPrybwpTi3Lj5TwcSQfFGXZsOAIhALg0RIZtqoT82LaXV7zqKGZruwagXo6%2F5MZMzdH3HlGlKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgVYpEyLb9t99u%2Bn4q3AO7VjlNhKisKzlXHE69EQtEdO0ag%2F2sovL79WokkDj6m%2Fk%2BesyQOBlaRuijlHAwVwqlfRRTVovtecAHwdx8K072Ln0i03VoHgMI2%2Bu36PAlvQuRINRQfqndrNK0%2Bpx5KBE6V0XZzXtYcmfHUx9BheOOntRXV2l1%2FQ5n0ah2Wmk0VNQQ58NMmmlbCusY5VlReSnpqq0Qw98UhZiWEneV0nauPwYlTWoeJ0KdOSkkD4nST6llIV3tcJW2zfvQfMoU7ZIi8vb5JP7yUejd6uDcJO1smHO9NW6Fvg6aVZmLxtEFzE93m%2BIvrNz6FonyEhOjaJV8%2FAer4EYf27pGhwB5zI1rGv%2F4WDPXOM%2F9n4vZPhYJhD4bJd9khrjxF8c6EZ2kirNkKCcr4MXihPm4cKwlEvX1BpMsCjHFe7wocBjVVkmHzAnqGK2QLERuM7HB8VBASC%2FdR5bRNqu9aMYG%2FoI3EZ4icnlxQ5OqMJVjAMVqmkF1ziuuaC9m44Mh4Gm3usPP8CodPwTtMZy6fLljR7FMy2xAfcr%2BCaJGkcaHhy%2FBLnvb6rq%2B0NLPI%2B%2FTktfds2dyRJ2zhIYAncIj97n21heRSgg0G9fAJJwR8vxv7%2FO%2FrfLU632L5t2dF340rgwZ%2BDDrrPO8BjqkAXBjXwWfSWlreREBlGOEtHYkwIJf1X0Gb4byahjuPTESOwRvJbED%2F5X05KdyXmN8%2FEgslbFzMiiIMGtLLxxHKjxdPFMwV%2FZEfLfjquh6TXOPqnnhN6RP3cnDas6DrzaRAQxKLrMt1sYJBtbxpkBFq8Aa6iMf6zvf2xs8pbn4MyM%2FovxlNUmRua%2BELMsgREvykFxEyCgtOoDuHFPeW9i1x8bL11fF&X-Amz-Signature=06b101844da162a773c49d614406f783c2d1289117c292f04358371436964efc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5YYP2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfkPRWUnoUg3fZHKAwZPPCawkkHgOKQ1%2Bkm%2B2b1vgmPwIhAMdOumvNpyOGy%2BM5V%2FDgRXuDx%2BNmIZg1UDIa2FwqJYMaKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMUEipphfuZkE3tfQq3ANZSQHkz3WW71hsZXa4m2Qii8vLQcCJQz3Dwz812Gv3%2F7r%2BjSaMIvEqKqzvYMVnCk8pbfMuonCEPiN2yvWqIKGb2w6TLbcXtiTsOBzasNcTCZ50sdrA%2BobLLkaMtylqvVq1gjyWrE9dQM%2BAPBZtvmAp7v7MUns6IkEqda0TxDoOjN%2FSKn40WRm9tcbgWyooWA3GzxIwTKyyKNLmlvAb3aLOt3CJ72icByfWnAFCSK8K83VoQmUKOyf%2BjqZNL7VoT2uiAw6wkWWZ4gAbY2yuWPQ3GX3GSK9gTGzotM0sICiwkah5g2XXZaj%2BOBLxoXm57Hmwaa%2Bx%2F4ukDLX5YZbfA3MkgYXlOvDd88QHnyI1D4GK9JosyU%2FCi%2BaQwEkxJS6GmgngdSElqP9l5nyF0N8GQ1Rgz8wnfuZHOiJ54GEQazbjdGZkijH0HEVFn7HzFH1pOeIHMis1ObMnMmrzIDRukPDEitPJHYR8B5tQ9bFKEoVUkb%2FIVUZjLMPMNv1OzkopjKXMMQxWD1jo6SJHdNQBUeIPQ4GIiOQSCK1Kvjexfa2f6YZqHbdmr9F9bLsd92NKHpPxR5agdtKpShEuagFnp9rCfTiPFe7BS6oubdt6UWy2O2ZXFBlEx3nxfsZHZzC7rPO8BjqkAR3tuYM6gThoWkhiiGOPzu2TqJKLBZn%2BxFhMNc89c2STsJyebn%2FcSikihlT5tDq5j%2Brr4rw3Qir%2Bd%2F0YqgdvBKBiTkXlhP73O1UsBXsvYgr6z19iQXbQvy4YJP%2F57jN%2BMzf1%2FXDdAie39jH21pGFwfnA7jZMs%2BMAoKz89W4rPNIfLr7LC%2FwHl%2BZf7I7Z5QCckKnM2HdzaOmlGoEwcYdz3Tq1SgIM&X-Amz-Signature=4d732d8dabe2ce7d61c4949fc9dbe3c6ff606eea189eed5770a1bfddc3250ef5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOMODNUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFDWGyZwGRe07HBmbApatfHEvipwwPHA4eMXjEhOXoGVAiEAvCWtVSyLUcyGuwpNZa%2FJmBm8XQHpcG2WY1FS6pyApREqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHR8TeP6d6KHq6LN8CrcAzSrKR%2FdeqoEebzPvMoaK0dxxJZsxpb7Ah3FKU6bJwkM5LHJgcXbZq66isny9GXuib15WrVyEiYgOtLuBsLjy0SldX%2Fq%2FuWQZj3RUIfPqawSIAQkFp4uwRxyHvElxJ8%2BDBf9UgT0WK4c83MvGdolTKR6BA6rvqN6xEbnybL5hh%2B%2ByrSWi4bn0yLmi12qEUtCmBx6jnN36KLdGwD22zM7LGEfFN%2B8U8j4R1M7oOXQbJYXxR%2F7KwhZUXvmYvLLSkXJXKl7Gy5kxCMPUpFpbMJTvKlz63sjeZDuLCAb%2FDZgSCizdYVEBM1uCRu%2B0x%2FVGi%2FGA5vhd5BSImxz9F0pKv1GGdb9Q4igCxzgSyCYr%2FwkF1tKr4e7B6raL%2Bk%2FoOeGi5yy%2FGEgYTEjleNHIppX41OJuTwl6fA1xba029jHIEgvvdD%2BCWc7eF1%2BC5mgp2t50q%2Fc8NdKBIB6zaKLSMc0whnlKXfI3OqGq2LiRwXoO0nxZ8RhBj%2BCkf5gk7YKOmwyWsMB%2FFF4sYqut%2BFgSHX%2FSs%2B2dJbmVjuYqCaAIp%2F6FMySJkb3KYKHjDODH9714FsyUrG5jVKrJR1lILRktGQHrMuleKegde0OoqxX%2BmT7Qrmv4aoj%2Ff8tKY9SMRR7cF0uMMOs87wGOqUB9M3EkeAHFkJ2BBqimHbnIbc1MSX72moDcEpKGTuMbqKFW%2FDpgg1N4nyQ9Ru8D8UP5tRSsZSOfpvehdlBHuXHCt84nwZhciGRNRfpABx2DH4A%2Bg6nq60N3LoIp6422Y5fUDBX9SRsY4xqgDN4czRACfKQHc0A6b477Qmy9zkPjsJDfO72Jsr%2B08ZeszxxENZwfyno07GwBm0vetQ3SM%2BRWW6mMJNX&X-Amz-Signature=26a1e04dcdf54e26c00a5ed9aaaa0c692ffad8554909a2d8ef160e3eeb9d818c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOMODNUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFDWGyZwGRe07HBmbApatfHEvipwwPHA4eMXjEhOXoGVAiEAvCWtVSyLUcyGuwpNZa%2FJmBm8XQHpcG2WY1FS6pyApREqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHR8TeP6d6KHq6LN8CrcAzSrKR%2FdeqoEebzPvMoaK0dxxJZsxpb7Ah3FKU6bJwkM5LHJgcXbZq66isny9GXuib15WrVyEiYgOtLuBsLjy0SldX%2Fq%2FuWQZj3RUIfPqawSIAQkFp4uwRxyHvElxJ8%2BDBf9UgT0WK4c83MvGdolTKR6BA6rvqN6xEbnybL5hh%2B%2ByrSWi4bn0yLmi12qEUtCmBx6jnN36KLdGwD22zM7LGEfFN%2B8U8j4R1M7oOXQbJYXxR%2F7KwhZUXvmYvLLSkXJXKl7Gy5kxCMPUpFpbMJTvKlz63sjeZDuLCAb%2FDZgSCizdYVEBM1uCRu%2B0x%2FVGi%2FGA5vhd5BSImxz9F0pKv1GGdb9Q4igCxzgSyCYr%2FwkF1tKr4e7B6raL%2Bk%2FoOeGi5yy%2FGEgYTEjleNHIppX41OJuTwl6fA1xba029jHIEgvvdD%2BCWc7eF1%2BC5mgp2t50q%2Fc8NdKBIB6zaKLSMc0whnlKXfI3OqGq2LiRwXoO0nxZ8RhBj%2BCkf5gk7YKOmwyWsMB%2FFF4sYqut%2BFgSHX%2FSs%2B2dJbmVjuYqCaAIp%2F6FMySJkb3KYKHjDODH9714FsyUrG5jVKrJR1lILRktGQHrMuleKegde0OoqxX%2BmT7Qrmv4aoj%2Ff8tKY9SMRR7cF0uMMOs87wGOqUB9M3EkeAHFkJ2BBqimHbnIbc1MSX72moDcEpKGTuMbqKFW%2FDpgg1N4nyQ9Ru8D8UP5tRSsZSOfpvehdlBHuXHCt84nwZhciGRNRfpABx2DH4A%2Bg6nq60N3LoIp6422Y5fUDBX9SRsY4xqgDN4czRACfKQHc0A6b477Qmy9zkPjsJDfO72Jsr%2B08ZeszxxENZwfyno07GwBm0vetQ3SM%2BRWW6mMJNX&X-Amz-Signature=82349f99374f6e247eaed04b4d00373169957430f14ca709b3e1234ef7f9c9de&X-Amz-SignedHeaders=host&x-id=GetObject)
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