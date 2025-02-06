

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZSN2E3B%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQChl0wM4s%2BHvInhw5pEx%2BDhvt%2FEyW678AJiQ0M8CATGKgIgAozEiC7ivcOTmR2l4NVDbWc%2BvcFpUVNMnI%2BrVHYEnj4q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDBBpFxuLmyekFSBovSrcA9PyLszXVEJYdGDghcSzfoyB3y8aczAOMIMaCj5O5Rr4z4hE1pHEtoT4cO3bzHhUT4UUhTVZxJb7yJ%2F8zBptZQJm87WKOrsfKC4iJrKA7jRHXzRuELRskYcsvCKBayl8kUlS67%2Bqq7ADNiNUKy99g6gAZL7nGDZD8EDJFh2S3nkyJGBgZi7HnO5VT%2Fy258cCrFBLs816STd08JtEVuVKDxtXjWcZ1z0WQFiBONfNEMagItykQgNuAbZdQs3J9GGDWeasogbWEQ2r5AupgQwP2tso%2Bt2h7cFi8Og%2BCVGHQttexd7Y6t75XO%2BXvFiUvk6XjdOX1JNjM6f2UuMNa5OM54YsgDwMiozrvwIiGuoLvGrglXbrJmx3kfAfHG0ULiyO%2F0zl73u4YrtkdBAch%2FnTKbmJs95Qdj9h1NSXtwHBU6ie8Hr81M2iyE%2FGF03QvpMgd59oqKSCxBqHnlvXjKsgbTnLTn8Vc3zoy%2BYilf%2Fy8xg3OJET6oIz31qOViMuWGEnAkJkQkB6D0kiv7PVkCc9xDZMlgSBiDhAgQU4D%2FbuOBjOu19uAFUUBKJIBkhwUeUkfHUYdzVllC8QCLoKA%2BfnZSt8lNkpRaL01zw6jHXbewIxIUv3%2FYm%2FwxuIZK8%2FMIrRk70GOqUBklxAUaPRgJDFYimaXjATu%2BzlX%2B8RRTVrdIC%2FQsk5QFQViEJxxux5bTqad%2FbqekbyKq%2Far9uXWcWVmKuWHZ0%2B7jxknYICMEIvwZXE5RuQ1QH2X%2FnWw3emjsb9RO%2F7fh3VSyVu0XDqbNkYubKjxuW7CW3VpQmklm6QWf10CJ0k9adZojqNUehhgA2fECggNlbEJzu%2BnOrrsRzVpQctvRTXn7OarK5K&X-Amz-Signature=292a3380d9dab0c8c3549d336c8fbec04e12fc84ff5b02c1ac451c1517807a8a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q56CLVSH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCNOCqqhs5dJ1VF4vRrNemw4VDXPjdDQI1tfM%2BEAsmxIAIhAPqYFVVrq4bs%2Fpan5V3vIgiMqiQ1XM5q215u5CyB1B4KKv8DCGIQABoMNjM3NDIzMTgzODA1IgxhImN7Ssrv3rAE%2FW0q3ANuOdNftnrO4npbGHVWnn3BmPrebZNVOSoA5WPl4QlFOK%2BRNIz9v7h2x9rDml02e577ieqHj4I1amTzk2c6bhtMe2fjzr7x0h3%2Fv3B7SU%2F1jV%2FC7jNLZAb7KEuebnL13OLRqfOVloIB7ASrwQbTVnLQfkLU0f1%2FOkZOLjrRO7S2lPz225ED1VIyqWkorp%2BU1hsLOspHL49pFrW8U56DqPBlucw1eU%2BXmrJ%2BfmlNYqiF1EjZE1NOpGFcXxBTuJ%2BWMWU%2F3Hg1CTUAAniVLEW8f%2FGdpDPoNINRAHjI3cgXPr0GG%2FKiICKTreTMHbo3yLwgXmCwBeT56%2FZDtlp3UKo%2FiXQZPnGOTfpCQz4BogpeRtw75LrxHMXGwkrXNsnvW2k9VE9FxOx2KigMBz7MBaJz2KmvKT9MXGOIaZVhWG9L%2B7GlE5fjA4N0v%2FBqTV2QJwUHmjVAZs4PxmITnR86rf44tWd%2FmbyxGYUi3mFtX%2BNhSlXpXKAEc9x%2FeZUnhrInKIvtEAPVDwCCEY5sBmxD4bcPwhjwoEL2L6%2BJWA8eFqxM%2B%2FCR4jFmymKDHBJMzPCHmH2OfSjqbHvHcGSWFgLnI1TXFCEiSuH67IkSV5bfgF%2B91%2Bz5HqNNeCTTLXV4GWgqJTDI0pO9BjqkARt%2FJfNkY6xWd9Vl8nKva%2BTL7rs7oR%2FjZyfyjs3iS%2Fjb%2FIV7FVbKqp9c0Yw7pHBbAtIqdIlQLWhIGHbNnYJcEmcjBhas0GyAbTmTyyMd1wuGqwHTbjRT5stylgncSWA3fZSUZpwhVbQoBijnYIKRauhaG1pZJN57ajg46IEvIBLJ4lfBWuwIVEOz8FIo9W1GOaaxTPIFzDCE%2Bn7ZZ5PVcSMgTsEC&X-Amz-Signature=6707a0a1c59f014b29fe46888e56c052d56a1fc85bbea3394dce2520ff8cc5f3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPD5T736%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIGrW1%2BEoiZiPXsnuhLX3xMDpzYFuE0H%2FqHQw2b%2BdtGHDAiABM%2BztdOniyGGQqJLQEBUzceElg1wNXoxSyeMUfNjaMir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM%2BPiil1V7TQzjebadKtwD4VZZyOI81p0sNCo6nZfqjA2WOhbmRVncf7HqamA%2FPiSiO2BYvDrdfseuoLsEC85d1vrXrbYBC4hYjwrVYdakx2nKTUCuJh6kq6HBqVyTU1H%2B27biYS5o82ru%2Bb1xVUTCHC5%2FdzBTrRoJTB3CeEAGltUVLDLIsjV3MjfgecQqE7GB31DqMVicKrdZ%2FI0UNi55HBXSkGyYPYNSLWop7gJ%2FFwpz3QLgpvWIrjb2yTM%2FaGTaC4g4tlvOfBx39ruNPumjV7K5MYx8Who7JiEaeMkVVW3qdDu4IaZNsCYu6R08nNB51HKU86rTulrzmDtJkfvBY0fyMl6MDl3ci7vlulzzURH%2By4TdpNPEmtRBVRzOA99etgVMa4HPuwn55iqiBTaEDc546p60HauLYNzA2ol45WNAPRHFPqf7SpoMRkYHscm7Lm1%2B%2BkBKXjuoSJpBL%2BmdL36rUB3px93IYxxEohLuM6VfwcDGgPK6ak75gaHQdYdDP5EotY6ltFVL8NjLBdhxTRlyuk6J3IM5SsPssjmctv5U8TC%2FLzyW2Bago4fWLQ14YsSAZEmEHUw8x6DBMA0q7YAfyoEUKov1u8JxeEN7WazVriTgYFvkk%2F4apqboVYMv1DhgOalcpY6TplAwgdKTvQY6pgEO%2BGQJSb9oVBUFQx76A0corvQludP0dal7uYBOYE4Z1WWcj4DT8tvwBhub%2FSmUK5weM2SMbqrMu3a4wlPzkVHSRCYk3WW%2Bikpa1rep8OeZVWXTgdVwHRm64HjVSi%2Bcz9n676OqpsEsTs%2FTFLOOCW%2FKS38OMg%2F5mO8zfpOm7JCexD3Q05sANmJGr2tAaU8EO%2BJCmj6%2FN5Pu9k5xPsgGKkWpU4dUt7jb&X-Amz-Signature=ddfa8320e0bef6a3a39a5a6810156f1cc3200c86e06d37629a3cd30fa9fbbc8e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466775SECJN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIEV9VEc5RulhlF3y7s4sMAUVQr2OvJ7yf%2BGY7EiknNpcAiEAmPBHQM3Sil3IaQ5QfTED4flraOLvU5W2RIPopNUH6%2Bgq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDEoQ65e0jRgkV%2Fl6QSrcA2oKH2hLySElbBYuOE7CtZOBQoLLJK8R9COPZdXDdWNdzI%2FdnZESqbgv57rFDkdkL%2FGEO1MJTRV0gQB3mTj7wDUcN0Tg1UXmqeuCC%2FQIamCQ9eh0wA%2FmMOQ3EfxTRV2rN6w9N0%2Foa496ew%2B1wf6SW9zmv7MiSVo%2F%2B0FcUkNn%2Fzr2vpKiogFCl0L3bkErwMnEeSBT7PE1ks77XLxTxkI7YcphLq9DfGq%2Bd5EgAmkZUl%2BxlrHmLl0yhejNtYuTDqR9lc0%2BGaKhTr2a9GvsTtRVyLRuSAPORJCQOICs%2FWnD6mlctEVOTN21b%2BOn%2F0ditDoRkrj9%2FUEFJDtcb%2FA1yquXDvXlftZKNg0V5FDp9FBToBENF4rvbsEoi9GXwlCwKC308uR49bIPuNpm1GC39CMpFAMrk8TA5Xr59EwF6%2FTcVKWRgq6WmALzGDIXIdOZ9E4vojpmcHgodRhXKrQz1YhtlxrOah%2FglSR6sVtoZUjCGVa2KyzEwijWW3d%2Bfvt8VZ%2F6Pus%2FahqH9rjVqYJsj9BJFajpX%2Br%2FEk6t2HbFAL0t%2BPCJ6Y38uCjYG1BvqwWUjydrTlyYRlUAexlZdLVKsENxQvcExt6doI0rX4NQAEAT5JthzbClL1yRnxhU9cqbMN7Rk70GOqUBr1Q7LpYAXB73pHncsIvUhQqWAqUpIen5ERt2CjlsGNs4mh4mRnZ9ugsdYF4CsiiuEddDX0oChScmdio6UyKibxp75%2Fw%2FBJYmUsGA765dCCgiRxgTomrDpUop9onvH9tS9BXV%2FweZ0bZ2jCF7qLe1zRzABDXA%2BPQCWm4JCgBd1UXBiMME7NhthebciwsiICAKAXDldRyi8r3iz0qA8asIrPfBHaCW&X-Amz-Signature=daba00d3d52628152e1d495e275e17062a6e32833bd981131d7b1acd03d54dd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XY7HZACL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIEA8gAhXSPyKVd8zIaejH3iQvSsOjDzJhG7CzLnI%2BSMlAiEA14cHJ6ggalrnXwHRBVeuRBAns5T8Fasq%2FKIXleGy8Qkq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDAQxfSOWHqtDmpKupCrcA05t20Tkk8KK6aKQHXSBiNphxOARgAuIihy%2B6yNRVl7bn%2ByvPS%2FBMjuUzXlQvOp4jqTqlhjI5ekW9pzBvkQoM8ZF2oex3vJzJR%2FjLHncI6TI9cHsq%2Fg%2BIvx8jHjgNPks%2F1RStqB7b5Tn3jZX9JoSD1L5pkiNWEg4lyL90z8WebZQaiipWia6dn7UPl%2FWZayUE9xuZo%2FELjD59ktIJqHow33IskLYOLHoxt2E3ce8SnCEnAIVK32bDZeluGB6v06Y9CidYzb41r4Z%2FTYMIvxij3XqV60QYtQ%2FDDpqxUbDh5H%2F%2BzgXU4U64UP2pPnxOL7icRe2kifNa2qI0oWVu3R3Mrpmu4R9wSsZ72pK7ZjHYWdildEN7mhcpVUyXoHjT6iJHvBK%2BnBZKoWqiv4jaAC%2FkXe46t%2Ba7kyAYIyCJBEBYzwVqDfjEVUaWbf4AJIC5VytsjNAZi3%2BpYen7rir9EU%2FvK5b2hFenuxmkDZ8kI6LQvefozCJmU%2B%2FNxV7gKhhCGOVZkmUbDUEOeOTHLNFH17karhqABVEvNKiHHE%2FgrSXJxELgHzZhdZA%2BpwgYYTbzQltCW9DLZ5leUJKiAUr82sWKklR4%2FDWsjGVhffRQWKx7qYtYyy33JWYmNtrcxxnMMvRk70GOqUBIzgzNHGmDkWs6tlfMTMDHep8A%2FA8FEfUX7fYHzuCrx6fbwKvE2QBqyCCfH0IQEU3%2B8pCVvBZOrMUjUuOA9GnCiH9uF3x0P8CvMqHz2tUiK3PCMED2H8vHF9SAl6kKk%2B9ysh%2Bfp2XmJ1p6%2F6mBxj8l7WqztdpQYmAQnOlC3xMtpEn%2Foww0dP3DYN7CliJMr2VYEeT4vN7Q7%2BxoztUkqGfA9YAv5zD&X-Amz-Signature=ebf2f86c1abe051a973264de11d9a4643223101daa290b111b253d8fe9743120&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3DP63M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDQDfTvjuKsXRAIf7dxCq6%2BFf2bYK57soDg5e5OmBcw%2BQIhAKvu4b6Xtn6APX%2Bbi%2BNMveLPVpk1qo0Svqy0h%2FaQ3DOBKv8DCGIQABoMNjM3NDIzMTgzODA1IgxL7uXs9jmjehet3BYq3APMVcrAoqP7VMdPZovkffzcPYXGVcVc6%2B587ibDf34sxzC5iSXik%2FXVh1T7f9JP%2BroBUwPlRrXeB8r%2BCehxexAuE0pQ2LtVPay%2Fg0Q9qUGjPSBleR3Jl98fDk%2BhTocEE%2BqQy0LFhllRQ5PbvxE%2BJBJGlAxKc6ba129mz0Fn6Y%2B9hyruc%2FWa917Fvud2ei0sqYpyyV61hEN5eSp1UfoWr3N7iY775fq5jJbBSUaaRH74pK1Q40IU6cKbZEatjiATzKJleKtYakBGRJtC50JnA1%2BWPQPjJWDEoBaJxxvZ10WhtfuKXoAh8g8aD0j67cyaBxox26DWRbYVfC8AyzlK44XId8V5op%2FWKZu0XuSlyuzQI3EvTyimn6lzb7dvBm5lhLAPuifZLqEmLCS6Nfk9fB0zEimvAEWXkYhVKy%2BiSYhw2uzJSvgoqEql5osbnyCPOwhCkblnkH0pWMynE462mcrq%2BWKxVDs3pJ349qffVkSIH64ZaU9tSZ%2BM3q5x5ysIAIsgXmmkc%2FbiA52iJ7%2FYHcL83mRN6fcaz6w1mgIxh9QTAxGPAdRBSK1KAaGi1F3xKckniK5Cpf99QSEeukwgN9hTaej0UOOiXpYz2t3REt4n4PoimyUGJWQtbded9DDC0ZO9BjqkASRBqlu1nfSEwNirVRoaV7llfbmW7RZFFzRfLISpYugf09haxzUgCzDGqaPuycrLQhqOOeLHfeBu5ZiKQZsU1CqgHNTTqbr4DqaA55NJHiv6VVu6Gffp1I3SyHkATyFqXf1flj%2BgFq9RRWQDD6uSTxrfubkyvhpekVFsxDTn0Ol7OBesRQ9O3u%2FZ%2Fvu9g08TerBLtpG598%2F03fHWorTor203mtvA&X-Amz-Signature=e2b72038dedb2f0718c6fe7060b5bca211f3500c3db4755143eb2c9c1ab3ad2a&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNY46MDI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIG4ReTQewo%2FExbkJfVmqD2q0Asvz4FwqheITazh%2F%2BRChAiEAnYB24bbDhDhoe%2F1wmQuy7WQ6SJlA25PYE78t4t9qX3Iq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDFRaHE7zwW5xH%2FRX5ircA%2F3b0ClsBE82gqUjNKDbfqFAiZxNnPwvICL4YjEVwnmj3qzMjvTcP4wrhHh%2BXMHPNnPBaDQGXdwdSdoozz%2BzZS8r2HMDqERRZ4lgoxyG9Vwwm2ssIIeB7Mdu25CfNrkHgK56xDvUGdON31pTBdbzG6eHnvcdZw93yIo0yZ9zNhdEHu4sR0khBT%2F9mSDylA9Xg9Gn6J5jA5zkph3Sa5JL6hDYXjr7jtizU8JB%2FD3%2BlxckZw%2FG2Lb8fDRBKa0wEd8h2sF3RdzAZwzadgrJJMR%2BdZyuboUOP2H%2F0wyTCO4rncCgKVbfQyMU6DCvkRigksOjn6q97n%2FQV2G1bS65wDoO14yG2nb%2Fo4ZdExEXZfkNwWZcWha7XiZOVz%2BAGADOgYKz4%2BWo5ABg58xykcS99kDn28E7U53GPntrUfMDGXob0GtKcP058oy%2Fb33qL83%2B%2BNVFm0pXpajmATaglc6nwaXlVdl%2FibUOA9VVQM5cIAf36yb%2BQobwlpNPjx6s14SwZKyvz0Ivla3lrRv8MTgCuQdv%2BkcC4UYYiLXvDTeJ99us%2BqyYnyHsjVIjDjgqRPTjqwRiiDyS4WmbuAhA1TwYCxi08SPwduTu4GyzDPtB9Cm%2B6eHPXjWtGZpqKZKMSDWSMJvSk70GOqUBuTi9pZYetvOaMZ9mCtaHTw9FuEnKIdYPRt%2BN%2Fy3272rVSgBbQB%2FWvn%2BOj4m%2FZXMIIFVT4m71iRHUxAwtqwhZ6g4FVLm%2F3bOKwdSlJOT9eiXZwzmGO6tkZ4Yow5u2%2BIxuF6iKiABwyqLyok8A7X8J7Z4uBdv3qhTKNX8NEOyZV5q5uVCwK0LfwWUKaXlKsF5Xg%2BCZ6i9WZYMTsa7Ok%2BHgqnLuN1wH&X-Amz-Signature=b264b0eb445349414fd437bf83d520ab744b3504e91fa61253d8ed41183c0840&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X34DZ3VD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDIdB6h7whiUTpUf9iYvFlvMH8AOdm%2BozYsxBxNdfTV5AiATae0%2BDN3nDmIEZvur0pJ51bSpTK%2BqXblf3FRGdVW65ir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMApMRXAdl%2BJ0%2F9T2gKtwDJDj9E7vvtbiX08Gk0kJdbCbW58VKtU0T9nxjC9CZI6E7e90U64qNciosjLB8dWd6zVRk%2Bv%2Beea458nPqiPa4I589wSGuit1aKQm%2FCWYyeuZop792gawXhZNiqwPLzftRLuRIcpeV6GCLVhPlKFZLQuupyJnBAN1Jl8VHzURoAeNRQ1MSCReuyML9SgYden59ekjlw59CyVOvSRKmt%2BsKzemf7zrCFYBvU6JZ0l%2BbrtABeZSE0y8uZz3QX2VU%2BFTH%2FqTo8Sd1FRBM4yQgdDv6lHkV2H%2BViEcKiBJ0G51GK9oewSe5GkhhEFb8zxKFR0XdQXNCNGfDyPn06e2VNm2E2qZDS1gvfRc9k5zbs2UbI4fSL2xrGKrL3PygysxypqfhQoDPpBAoN%2Fte%2BqSIkY4hENSMLRGx7DoS25jorvXBq5%2FnDHBsybDtSktrwIE8Bh0ECHM0usmguyF%2BBXKNIAx4q%2F8cb%2F2LsZSzqO3VFmODHIsiZ3kPHsMNRIRZrhrprGl2kTNBoMif7GNaOq%2FEKtzkExho3CqEvIn11bZs2QDvC6yNUNX8S%2By8G1oBvtver%2Bvm4F%2FBHiukZlu23GSHMIeWatWAx%2B43OCvqnamaURiVkla%2Bq%2Fd%2BboR%2FnjAE2akww9KTvQY6pgEop%2F3AuelX7A8ZyV%2BXxitoKgcXFDC1A7Lc812%2BkLQORYu75OEbAnjdZ08bxIrhZJ9kvir8BUbvnUiZaeIA2OT%2BSCHzPQCmqZ9fzDYlgBFI82lnmG40RdNwqZofip5Td8HKZyuXPI7%2FmF0GbVyZVwxxhaoYVJRP%2BnmrvG6CZf%2Bpb0i%2FLcfSdpiPn60%2Fq%2B1WmvxzPX1IS%2BoCgzBdvvJhh%2FYnpK3qmSxZ&X-Amz-Signature=0515a5e5105bf2118fbd9a26a08af43782f22e1c6df532d67c56c8e9991dac45&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XY7HZACL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIEA8gAhXSPyKVd8zIaejH3iQvSsOjDzJhG7CzLnI%2BSMlAiEA14cHJ6ggalrnXwHRBVeuRBAns5T8Fasq%2FKIXleGy8Qkq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDAQxfSOWHqtDmpKupCrcA05t20Tkk8KK6aKQHXSBiNphxOARgAuIihy%2B6yNRVl7bn%2ByvPS%2FBMjuUzXlQvOp4jqTqlhjI5ekW9pzBvkQoM8ZF2oex3vJzJR%2FjLHncI6TI9cHsq%2Fg%2BIvx8jHjgNPks%2F1RStqB7b5Tn3jZX9JoSD1L5pkiNWEg4lyL90z8WebZQaiipWia6dn7UPl%2FWZayUE9xuZo%2FELjD59ktIJqHow33IskLYOLHoxt2E3ce8SnCEnAIVK32bDZeluGB6v06Y9CidYzb41r4Z%2FTYMIvxij3XqV60QYtQ%2FDDpqxUbDh5H%2F%2BzgXU4U64UP2pPnxOL7icRe2kifNa2qI0oWVu3R3Mrpmu4R9wSsZ72pK7ZjHYWdildEN7mhcpVUyXoHjT6iJHvBK%2BnBZKoWqiv4jaAC%2FkXe46t%2Ba7kyAYIyCJBEBYzwVqDfjEVUaWbf4AJIC5VytsjNAZi3%2BpYen7rir9EU%2FvK5b2hFenuxmkDZ8kI6LQvefozCJmU%2B%2FNxV7gKhhCGOVZkmUbDUEOeOTHLNFH17karhqABVEvNKiHHE%2FgrSXJxELgHzZhdZA%2BpwgYYTbzQltCW9DLZ5leUJKiAUr82sWKklR4%2FDWsjGVhffRQWKx7qYtYyy33JWYmNtrcxxnMMvRk70GOqUBIzgzNHGmDkWs6tlfMTMDHep8A%2FA8FEfUX7fYHzuCrx6fbwKvE2QBqyCCfH0IQEU3%2B8pCVvBZOrMUjUuOA9GnCiH9uF3x0P8CvMqHz2tUiK3PCMED2H8vHF9SAl6kKk%2B9ysh%2Bfp2XmJ1p6%2F6mBxj8l7WqztdpQYmAQnOlC3xMtpEn%2Foww0dP3DYN7CliJMr2VYEeT4vN7Q7%2BxoztUkqGfA9YAv5zD&X-Amz-Signature=3d7f419e065163195cf68f64dcc0cee79dfa32690e202abccc7c26cde823bd18&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPUWYX47%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIQDr1ldnyh%2B9aTh4cjOJKJXzq8l4Ysa6%2FqYbu2y1BSk5HwIfLqZ6vf1xplf3bG8hhNe9TiLJT8rT9OgpK%2BrW4m2uWir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM9MAYgW6RbmYfTqioKtwDrNGaV7sOSnmB4RiHKR4N29YVdO4oUtGxIlanoimleDnXeROmYV5jFQtqxhN3mk4ch6ST9%2Bmj%2FnchmkEcvoR86YJLrl8E94hfWDYGVwsO4Jgmix3HvHEKlwNz%2BuAcEj4kyQ5ps1q%2FE1fO8%2BD1i%2FdgpnS4Npfh%2BfV2OxaYdTF%2FLnv3nqBjQ4m2%2FjQTqdyONugB%2FMJHoXoqoJexn9PXS%2F9ewbrDPDImJlm2IvJUkDjaDIw59ULoO%2BbMHrIXfR2Ww35q6YxW%2FjdoQRjV9FILaAD9boeM4Zs%2FFz5bSx08UPYWZVsjhN47NR94trgedCO8f69l6bRI9aNxaLSS2xOpFTrK571lhgrym76P7VbAVCovrm6gec%2Be%2FhSjLtE9kucJHfVQ5hcXxlZBLSqaeawvxEN%2FMRAxkJzB7K%2Bc8Mmn2tIOnmSrQxaxCLEY4s%2FwsvVN55sGT4liu0vJ9Bq6W6dbsH5n%2FpIWgJ5PFceDnqd%2B9vJeErAswLVaWp0OJ%2BW0faGoLVSTmeSlkssIVoklznNqpAeRrHVGwZf4w15ZZApsFCDYWkBtUmwwRLlMGV9gNAa9wujW3dSEw2axO8DNOyX%2Bl%2FwC%2BUZR1gEh1RabImlTQyFft21U9Y9liiuCbnF6im8w0dGTvQY6pgG01VDIcOz%2Bfkb7pduQVCvQ%2BSU1BNpgX8fTng5sbgdwJfckwMSG1qt9BVytsCVOZt%2BVLx8mlFhWmWSFKtpMaX1HrhfJzZpoOybCk1GJkEJfAJlUp%2F7MT%2FjJSasiwnbkewirAMGknSV80NbNTBrIKjZy7pHjNrWOU0Leuqh6GUgbOVHvFqeRMfPgNW02tXoBOKpaYPWbrPWP870%2Fno%2B79tsJOtVeQgmA&X-Amz-Signature=a5fd488ac604da844e3d7e87a1748dfe43bfd774ac9decbb779758facc327e69&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPUWYX47%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIQDr1ldnyh%2B9aTh4cjOJKJXzq8l4Ysa6%2FqYbu2y1BSk5HwIfLqZ6vf1xplf3bG8hhNe9TiLJT8rT9OgpK%2BrW4m2uWir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM9MAYgW6RbmYfTqioKtwDrNGaV7sOSnmB4RiHKR4N29YVdO4oUtGxIlanoimleDnXeROmYV5jFQtqxhN3mk4ch6ST9%2Bmj%2FnchmkEcvoR86YJLrl8E94hfWDYGVwsO4Jgmix3HvHEKlwNz%2BuAcEj4kyQ5ps1q%2FE1fO8%2BD1i%2FdgpnS4Npfh%2BfV2OxaYdTF%2FLnv3nqBjQ4m2%2FjQTqdyONugB%2FMJHoXoqoJexn9PXS%2F9ewbrDPDImJlm2IvJUkDjaDIw59ULoO%2BbMHrIXfR2Ww35q6YxW%2FjdoQRjV9FILaAD9boeM4Zs%2FFz5bSx08UPYWZVsjhN47NR94trgedCO8f69l6bRI9aNxaLSS2xOpFTrK571lhgrym76P7VbAVCovrm6gec%2Be%2FhSjLtE9kucJHfVQ5hcXxlZBLSqaeawvxEN%2FMRAxkJzB7K%2Bc8Mmn2tIOnmSrQxaxCLEY4s%2FwsvVN55sGT4liu0vJ9Bq6W6dbsH5n%2FpIWgJ5PFceDnqd%2B9vJeErAswLVaWp0OJ%2BW0faGoLVSTmeSlkssIVoklznNqpAeRrHVGwZf4w15ZZApsFCDYWkBtUmwwRLlMGV9gNAa9wujW3dSEw2axO8DNOyX%2Bl%2FwC%2BUZR1gEh1RabImlTQyFft21U9Y9liiuCbnF6im8w0dGTvQY6pgG01VDIcOz%2Bfkb7pduQVCvQ%2BSU1BNpgX8fTng5sbgdwJfckwMSG1qt9BVytsCVOZt%2BVLx8mlFhWmWSFKtpMaX1HrhfJzZpoOybCk1GJkEJfAJlUp%2F7MT%2FjJSasiwnbkewirAMGknSV80NbNTBrIKjZy7pHjNrWOU0Leuqh6GUgbOVHvFqeRMfPgNW02tXoBOKpaYPWbrPWP870%2Fno%2B79tsJOtVeQgmA&X-Amz-Signature=baba27b5919b8a42d1e5b16652c73127bc14c63d9c4856d15ef8fd0e696bd64a&X-Amz-SignedHeaders=host&x-id=GetObject)
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