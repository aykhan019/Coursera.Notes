

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VIG5RBY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIHL4D4W9aO6kK2rIUScwh6vVgcnoPLIKdI5XkTBMIKl0AiA33%2FtpNZO1OG%2ByD6buDJSS3uIMYq21OjKZDVpXDobeNyr%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMdFjwQbEOB5UFixd6KtwDHHmy46OGuV90s9WgMx97x7oFK2fmZW3OpB8a17s1wgpQlh%2FMK9gKKmOp1dWC6PzA95H7aFbVJK2IxiMFKCVAnUW1zH%2FvioP7Ps%2B3xQAbe8kUyZwIfP9gu25j4JyVnnB6MaUwFjOOZjinuoFYnK9099ShHCH1m%2F9dEhgHH21AGaOrLgKVw0YOb7bxmNdLaeB4mqO%2BQ8UUV4tWBr32K%2BQw%2F1X2QyekF9itIy%2B9fL4GYGN5pDOu7MRBV5Ic%2B4ao9q3BZWTumXZz4uw6Sdgm0HwFSoaPV4SN1NeyjqXSgT5b7cmw36csN5gz%2FI7xwQGMX7a8NwJvXMM4%2BPutC0YPkIYm7umBEBRuLXGvyZ%2FnFm6A7%2B1P%2FwdfvrhJw2mGfEdZYEfauX9Hn2GZhd2c1nzOdwfmoflMYIN0MSrqqRzSFVkLaEsxjApxrfHZPLO9AlnYSniAGvPqWWLGwBLeEZpO2D3GjH4lKa1UnRX01ywv4t2hMMWTyiDUK9%2BthDMPyG9pLPVFS4zyVLtUVjTXnqck%2BVFqU9qSWcPnrWIU7pRZDqYNXVDIV9ewRGd510TwH%2BymWkX1M8QVtvZRfuM9Wm2NZo7IinMKRl1ettPp2hle3T3yRveRGvMxwfE97uH%2BQYgwxeCYvQY6pgEWclt13Z15QXDNfOR73oqgEG1nu90MZa74Lk4PitX0jFYTSSlHa9M4x5Xo4xQG4nxNBV5%2FpTLBfO21DvHP%2FvrHS%2BnugD5CT634XOFWak5sD%2BcdjcWITytYyVHmnm%2FWL5zQNoDqqwEYuZQtF%2Bk68yO1cn7CHwuBgOh40QvDzyybfjilv3PNtTD5kICPm%2FVgCRMHezVEe9E2dXReet0VmxOeCQXobmZ2&X-Amz-Signature=8a91f66c731033c1e5b899742180738682bec774f9f01f906bc437c073295ea8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHIRAYL7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIEw7AoQTuIAe5NP%2BjdRvxwoX0ZwzhgqgXyCoCyJPTHf0AiEA7bXUxyRKuHGBb1R3DhzfhTRvBhDEG%2FETiP1WtqCBtMIq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDBAzW5cDBUvJLYoG%2FCrcA6XhNRU6%2BHh%2BjNBILhueQ0ONgUQU0mb53Z1JK2dWsV34pxKpxYal6qi7As%2BU%2B9gXhJnHu29tUw7P%2BcVID5MfMLMMbd%2F53Ohki2ttlCUhQ77SLVLOsaE%2FbBU4JlVhKpXyeepVurFV7YVYF4EACYaQeKwKosMvlWWqXgA24cdrexnK7%2F%2BIwfjfL43J48T11iU8jH%2FDVBtYifpbXHW15RxmdnT%2F9aVlSMX5QaP5vj9YgdbPu%2FFjRKduWpxvxse3R0duukl0anbld%2B%2F34%2BujgII%2FrvrQPQ0mDDOvqGvQE9VRwVEioEZOu67e26N2YSf%2BY8vsh9ZGhNuGCI%2B62%2B7d%2FAeAiwGoPZ9hiYeYdzwN4Wp7v30NSSgLZ9LMy%2FhCVm9qj%2BD%2Fg9fKbbYCv7aGh0ROSGDxJqGqfaKkUlGYFjo%2FZQRYSNp9cX%2F%2Bg0Hkitmr9r0eN3fqaFxWEnYxb02gwkKQA9NXsX4kkynMWvyu%2FJDtkS9068JxL6eGvPbY6U3SX4ibP6yoHHjDY7vwRguCt0xLhnPNPQt%2BofCjgbhWB9wkP6P8lQo5u4Ve2CxJTHTeFEs6bEKv1lvTvf9UP4dKvsSSL%2B6jVKrbWeA6SYq7OC%2B9GAtxQOBlmstTxaDISG3lM196MMXgmL0GOqUBcAZXvNC%2FiJDcWnlE5swTHRhrbM6E6ziWebsSYsuzXoWkbxvilJl7E8LrhmkAly6ya%2FIqP0DmymQdme79xwv0Rk3%2FqXz7HWD3yFG%2BgY%2FfSrJKgFuxkQHfQJ9MoBa07JDxdfImvcW4KI0o5INf3t1Ov7sWO9p%2BMTSY%2BWftnk93pnVL52F3PHNhPfC1EFChmGigh%2FPVFoJ94c1wJHcNubKGNtb7XHb2&X-Amz-Signature=e1d3e4ba71582b45b5a010c28b623646b76d3bd66e97f5632e540964212dcacb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQUDPK67%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIEOYsFmDBSWjz6z5mycr4eRiWJG3%2BOLbUWWtUNl2flV0AiBei1TTwJ5hccP1WBqbA9bRgPvhjcYUkxmgMR5f09dELSr%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMOW1RVwXlhWSdKaZjKtwDTXNceL9jdQ3O2%2BLief8upd0X1d6z39OxcgN9qEKvC%2F9mfoIWaARPHO%2By%2BEEy5iDUYUEewUVgY1K3eWPfWuC%2FfsScqYUqsen4urmwJHXZlaxL%2FleecV6K6XNHZ6SuUY5kYkZCXk7Y7m7%2BJ4AkSD%2BMlMc4mOiDwKmE%2F%2FH2uI2n5kpA512l697g5mNiycsHwa2pQWEZ%2BvNom%2Fg%2BUFTUPcLinYL7psdKe2swvsISvjE1vnY0xIyW%2FtN5uxc4v3E7h0NkBci2cF6MDGlr%2FTJ0hGU%2Bs13VXKJ0wJ60ZNV%2FlOZyBVzQQkMaP11bTtRcHzdRNqY8hwBDtTqj9nyAmg2uCVoWNFJFzDaeZLz3GacBc%2BOE26r8fCjzTC6sXzn8F%2FQ1l%2F1J4deVQWZGRu9s9bK2pEEF6Xyp0H7kqyYiskhfexGY6M%2BUhu%2FPCiy487v%2FU7xX8dC6%2B7uXaw0%2FdHju%2B7s%2FK9Wx6xWV9yKp%2FMVZ6eoz3qAJzBhvp9Bg8bb%2FQtOB1LjN0QIQzEaMRJtrEiWhB2ec0k7jtvmY07JjHNcrTYkEikGp0StsS4rpvLNMzfBhE2atAnQyT%2BpSE9xiHE6SZHFq2y5%2B%2FZhg6JyUyEU14k7CWIEj8f2NbMDD1FpprUNTLZUwv%2BCYvQY6pgHyr8aA6NwsNfM4Y%2FYxJl6zZlKYml2%2BOVHbdm%2FvxzdFyy%2FAm%2BHjBWpZoi0nebztyIw%2FuZHcRx4e5BrLwqCcFMISd86dcdlS0y%2B%2FpIl7pXhtCsS88xqlNv1jSVmC%2FV7xvUvx%2F4FI0uci2T9fl8Dyq6Db3OmYalGIIxrBpaWJBxaN9ESrfgorTnyPfURRz4jp0S70fEewAtzYfjF2h9eaWL6KuTQDj0FI&X-Amz-Signature=a87b54510aba3feee63db9b67e7183adef8f8d9a7abb656ed8c372fb6f40c424&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTKLCRR7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCkopD22hsSLbSJLDaACB5cOew6YHZz9naKFc7pA6NDzwIhAPtBmEZ%2FGbU1VheX61Hk%2Brd3Ck5duszeX%2B%2B7%2FiOsWNByKv8DCHkQABoMNjM3NDIzMTgzODA1Igxo96LSBdGtHLvJsXAq3ANeGtQ7nIpvXW4jgyl0XWLmmIou0yfMKQeub%2FUAI1OfW2kdY46coUtzNvoNISWd1vsKA7YBcBSjq5xApjJE7%2BeCshHron5DIeuZ2XqhxQknUVHuH7HGoLUsMPQdlx8ypKN%2FMaWJZ446h%2BaaVwh66ZpenDNY1vRfcmM%2BuopYlE3LyUWpZzWPoZAly0c10Pwfoxau%2FHr0AjbJ8YmthKPyAwPSqm6AonhUSTBrk%2FgEWvX9XD1bRlhB2Nd5AJcQR%2FprSuiF%2B1RZwqLAuAMIeACSd%2B%2FTi6iPt6Sj9i3cmiGed3akIRf7KIOT7ZnYj46LpxvVQOP9yD1z3XeUM2wo17M17D%2ByobSjrjZE0EbUZ4YSRt7ceb2En4EBlq28mZ2fjbD8EOJJPUwiTStgi5uwTdg6AnGCV4aM58wbxun1XScsajL0iWKXbT2WprkUhAnZEBjg5J62rQQah3yIlIErn54kXYtFPpRU%2FWKPS9qVvlvi82ZOWbA4LFlr%2BCSNiteV4mz9GdIkF8racG1enk8nTBCvHhySOHrB9E5d130QEeR0lFUh1qTDdzFgQuFw820iNlI8p8X4UEybiRNSzUdzBX848n%2BdyjH6sk%2B3TZgrIGkEzd8W9tX1N%2Bi5V%2FtEiNbHoTDI4Ji9BjqkAVKr%2B3cZL8%2Fa4ahVKPULXjoh91KfNa2Yd1vHS9oEI%2Frz2DZzbNsd3ulyjsTxGgjT9Hmf6OOoFzvNHYb8Q%2BSu8HHSG3%2B%2BEpIWJ7Ntc1ByLgEstPvm14XhN%2BOBygC%2BytfNJtZ%2FYmFna%2FbZCwNhiT5kXMJsMgL3jYZ6jzR0hgMIX0muXDPZgYabxrfsknv%2By7fmXwSaOtfDbtjs8nxceRHXBzTf2G8m&X-Amz-Signature=030aa1f4272880f38f734a813479707fbae7784257e15a9035ffee80b1cbb39a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5K4H6ON%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCLq7fg0WZ9Zxd1knRmO6fZxmC57yGTWnglyX6XWtvt5QIhAKGao2SxsYMg2aIlLNcinPI5pN5yvn9hLN0LMP6RUgz9Kv8DCHkQABoMNjM3NDIzMTgzODA1IgxAGjSRTqEFAIOLxXIq3AP3eUCZwWo%2FKTrZAFoJ9vTT2p4%2FptKAa2gAuQUWEmFh8%2BMBYozc4QHIqfrKoJ1ZqEFZVPCUIbqzYinwNXXGAF9D10HfwaMnuEK5BA%2Bw5xi8vKakPptBso%2F7Lgw%2FJlWefCVfiHKjDWaki%2FjKTFiNoyxzzAkrdHvUqjZ8JfBmDHt4QVJNVO0qbM4%2FbBPRfS8mBAYjE2xL%2Fw7sDLCwVEXGI1XaLrbtcHO1x8A1GXwrmaG%2BXx%2BXSveZJbR09UqXP95%2BnCKrhWk1Zu5KwPgIrKXteNLVASTxpEAXHRyvOL%2FAy3oX8Tn8HA8SMBeFpELrbFMUS3bBOT5BzBS%2Bcv2euthxwsZNywdOYTmbXGXXzjoLy0cMKlj4OEuzbL90Rv9DNM5jl6jNuqtLpEm9YxE8P5WCTwkaxheBIgmWJgQhXZ2g2br0SNZAG1JI%2B%2Bi36HYUlU%2FXNxMOT1T2%2Bwz0AvNlhtjc4wXJ08qTZho43Xk4z2zEJujqPHMrTt6ui8ZPM23MoZPPBtuI0dMRwCGxhKrHyrqkccTQ4eUxARBdZ0Ce7UE4846ThbIKUvLItT1QZEbdx9exT5NJ8yH0f%2BL1myj5YaAn4sewDySpYLa07nEB%2FrpiitwCYmdKd273qfN9gRYxVzDG4Ji9BjqkAdeI6jbYbrnweYkQGHxMKHR3IWNV9rQ%2BrxTQN2VJXEx3PdXffrtf%2FiDlfPnP5i9dum5T7PPkiQ%2BHT0EUSsBi9E5SX8%2Bd%2B1ZKxq7lxDuJDq1pcRvI3QnocuiQ4fQR0lPXrN1mVodcOJwp%2BLyTouMIrnmkVYfwmRTIMdSGV50NB%2FBmr9olWJR2D71YOEKOzLwM9fmYRlY6nFf5xhtS1J2Q%2FSfJ87hD&X-Amz-Signature=a67f088d376b745e29c5d6d08e84f03f8a672c47800d5a861c9cd9f26f4216ca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFVLCSW5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIFDSrA1TnxpyodM2pSwsJ9lm1rGhlMyglW4qoUdgmqm5AiEAzGaot2gTz8fa2Ifw9TLiAtcxtVqBzhGCbGeCZU52fN0q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDFuKc7iJnfD1gtLu0CrcA1PCI%2FmsgOLTR2fMX0u0TS9kfn2T5sb4zSaxsEWI2eihuyoHT%2FGSMuDezY%2B7YVVhYg100H3K6UHNYzStJM47vLVl%2BGnndNtUIC9cAdJ5jmIIvM%2F2SaLdNYkJNzlRKc0YXVZ3A28%2FifrpojMaaYVBtpJMWpTmAor%2B%2BLbCtWK7kgXXxMnJnlb64PATAITHFAox%2Bud7WY0UN8HahnfmQn6JmsEIYWqN4HOa4pyqbY7%2FkOmtlmvZ%2F4YdW9Dw8n0nzUzxcb35QwggmN87wFogHQSLDeRB2flztRBLJFiiWcET2JEFqXR8SutY3fPf87RsPwE7cPIIE2uM7e5j%2FLCX6vL1qyg1T%2Fa%2BJWWjCmy43QHeV4VEAo%2BEmFiULr834tfxrIVOjsuqcHgwZIt0mZHedt5cclBakyUY26cIYEC9GrhrdUETvocnPJXn9CxjzDF14rzjry0eLuRwX%2FOZSrkyyVDers1y0RCavDEP%2FRawBk0E2aiYL0FpjCh9VloQ79U5LucSoEM44R5QI2eKq0EUq47ETKkUKubRXASEysagocs64YV1%2FI7vPjeHkeZFQmxOXFIRBhiMabXpUTNmwyo5GG1X%2B%2Fym1E1Vvl0j3i2HaGuC7FQ29TJEmTo9zSCbB8ZwMNzgmL0GOqUBf6J73cDlxJmjVwNSGWMLtdN5jJwfD%2BgKpgWjeEUnkGoBpojBlsDpPIrHZ7AMMYnkoPykY2ytDqwT7536LgeaY11%2FEzOs36pLo5%2FxWIwE6FdHCNBUgkgHuw6fei%2F3Vrw1VMLsqXpnvCsWG7RYrm0NqPLEeH8Yop%2FnQuyMaf026q8INTxMf%2BnXt9Q5smRCA2J3MV3LOLGj9fYgmrVdncqVznu4ttiM&X-Amz-Signature=bc631794a02df0b3d0a680a09b26ab160cfc96d621c2ca1f18202b8070c94cce&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S25X6FMI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIBLwTs4JwXZNzYSmlNnZlPlKa%2FBVM6Xg%2F6kMmxGLtkbJAiBiCz%2FnFvk8c6Eic%2FBkzd6YK%2B9zBkjWivFJoBDQBtqebyr%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMlcSJ%2BK6e8uilpg1%2BKtwD6LhiW9PgGG8Ewp0iux7%2FHcws%2Fw5K3PmCGaJ3iEhC1nDpB1JmRTxKGz2BHT4Bnkqsd99NS3PuzSJfdG4zOo8hfRoEuKVqLexbjbJMet8P82ldv3FIQPEVeOp9%2BoH8w5AOARqi8WxmA2jD%2FbDoQxny9C31LNXMP1ea12N%2BQlf5uUZQ718TYjxgRUc8Z3EoDiQ7taYkAl%2BCdjISfphrm74zEMwjsn2WeWHKwVuWU7OXcqUYYiX1f5HnSU9N9%2BOHmDLmUZMOAy05s7MrX2F7W06XijNfdiqae%2BYewH9b9T%2B5LWMziwurgxOdht95hTMfq%2FUVPd69YxVYSI7Eqdrr6ZaDdDf0Lk221c3MmuHrr9NgdV%2BWenVXPcBuzuEnETn%2BU9dFjIkkBm0DOpZ0PTSZMBo2%2BuCoNPo2oT2I71XbRCR5AmJKg7yc4zEeMjagjtPdvuijDIYw3a%2BVqmc5bEQOl0AoB%2BU6rKHmDVao%2FhG7dB8dppzqFH9KL%2BUW77Hj3R8BmO4CAufXVhplJotgxumbH7d872a%2B27WMc77SvO%2Fe02G1OEUE4TEqutjP1XV2UvH3EB6B1Im8DwSRSBWyNZIEowZSrtQWPoY1RRFjDR03CQsWORxADXlaonAoIVE97PAw4eCYvQY6pgFwYuQD434o4T%2BbZpPxHXfZhiQeiRbJRtpEux6n73IRa8pG%2BoVp7dhngSZRvPu1PE5omyIjDhVPiuaCA6ki%2F33CvUaLknWJB%2BcY733kHehX%2F7epri%2FgRNV9IR0JMwjq%2F0unnMppwAVHPH4v4zfaOw83qflxO9e7UcmEhd%2FdvjPZCS8TteObmk%2FH7IbOVNqMGXQjaqSaACQYlXFKZghkv80Gic12eZdA&X-Amz-Signature=e4b94a2e80c8f711a0779ff68b058a4f2ddd855b6e9850f0f1339d94cf5eb4bd&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5TU65SH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDHaqm3Pb9XZx3pSoXTHPOsGXhuXiS0p2Ok7WobE186tQIgU%2FVxR26gczoIivL0njLapupwynTCfi%2FTx2E3OIy1JrAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDP1Pe0X0m1pihnjMfSrcA5JJotHad%2FMJM2VfWYHCLx8SsKtVxOMcVnUTBAeooL7%2BJvNljdhC4ckmwCyehyC6uEGl%2FktdtoaTLD1AzOzC%2BvkzH37%2FGYXC5Kn6PwIgHy6O6kDbPwuQ7A723Mv25CWiOTBc4aWjwPqK1KBbOpDag4d6fNZ8bIzEMoQYbdsx7m%2B0FAP4sH9xH2RgkQIQvAEiL6bHP%2FFIsPKlV3ukpNDwqsdwpUY7cjVT3%2F7kVAfMexFdxH4qakTo1bqoAupM%2Fbz4ZsQ28i3OGyl%2FQ8yWTFYug02KQtnFUdayckcImQs%2F0JkvRnwacS0vcpHk5lfdUzttJQ4C8jDj1%2F0jxHsk3NOuCitmQ8W1Ugkq0FrgTUJmSvAYxkkAxseB8tiPxzCuIK%2FdTK%2FR43CgJmY5lvv5hJHhv%2FHvB3pvoVpisLMfljv%2BjhXaKyGK9Evm3vT8wmgE41wXDJqQpEnt6kjYDo4khxK%2FEopZunk9yubax5JAEPTUu0E1mXp%2BsaBXDKb%2F%2ByRMpTDz3WuXyCTtZXerciBUH%2F9Y6H5hGZxYTOh0mtj%2Fouv6qyeM8FYZNHjvNO%2BDpXP4qg71U8VAzVBbwjicE1caZqR2TWEYnNkOlZG38NLg9kiAIokvm2mvWn9i2jt1RWuLMMngmL0GOqUBYiOM4vXOH4dK%2FRUmHpF6vcAy4rrDVnCGEq684yeIC%2FWDYFD75rXYLdmfg%2BiEIekkCU5SNlXvueMOWl7Zqvocvi%2Bnjn%2BI0u2NPBj%2FemgjfSvQcAzmUXrdEgWfAJIhz50H4A%2FPXlF4R2UHFiQSv7KirFkJjtid49qR7dc%2BAM4VYuIq%2Fi3NAQZZ1hx4uif3mUS8eFqG0y0Au%2FYIWBKu9OiHSCaOqE84&X-Amz-Signature=c2bb7324dc662350bf420a34a912cb5e1964b3e675189600ce16ec65a3bd8ec6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5K4H6ON%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCLq7fg0WZ9Zxd1knRmO6fZxmC57yGTWnglyX6XWtvt5QIhAKGao2SxsYMg2aIlLNcinPI5pN5yvn9hLN0LMP6RUgz9Kv8DCHkQABoMNjM3NDIzMTgzODA1IgxAGjSRTqEFAIOLxXIq3AP3eUCZwWo%2FKTrZAFoJ9vTT2p4%2FptKAa2gAuQUWEmFh8%2BMBYozc4QHIqfrKoJ1ZqEFZVPCUIbqzYinwNXXGAF9D10HfwaMnuEK5BA%2Bw5xi8vKakPptBso%2F7Lgw%2FJlWefCVfiHKjDWaki%2FjKTFiNoyxzzAkrdHvUqjZ8JfBmDHt4QVJNVO0qbM4%2FbBPRfS8mBAYjE2xL%2Fw7sDLCwVEXGI1XaLrbtcHO1x8A1GXwrmaG%2BXx%2BXSveZJbR09UqXP95%2BnCKrhWk1Zu5KwPgIrKXteNLVASTxpEAXHRyvOL%2FAy3oX8Tn8HA8SMBeFpELrbFMUS3bBOT5BzBS%2Bcv2euthxwsZNywdOYTmbXGXXzjoLy0cMKlj4OEuzbL90Rv9DNM5jl6jNuqtLpEm9YxE8P5WCTwkaxheBIgmWJgQhXZ2g2br0SNZAG1JI%2B%2Bi36HYUlU%2FXNxMOT1T2%2Bwz0AvNlhtjc4wXJ08qTZho43Xk4z2zEJujqPHMrTt6ui8ZPM23MoZPPBtuI0dMRwCGxhKrHyrqkccTQ4eUxARBdZ0Ce7UE4846ThbIKUvLItT1QZEbdx9exT5NJ8yH0f%2BL1myj5YaAn4sewDySpYLa07nEB%2FrpiitwCYmdKd273qfN9gRYxVzDG4Ji9BjqkAdeI6jbYbrnweYkQGHxMKHR3IWNV9rQ%2BrxTQN2VJXEx3PdXffrtf%2FiDlfPnP5i9dum5T7PPkiQ%2BHT0EUSsBi9E5SX8%2Bd%2B1ZKxq7lxDuJDq1pcRvI3QnocuiQ4fQR0lPXrN1mVodcOJwp%2BLyTouMIrnmkVYfwmRTIMdSGV50NB%2FBmr9olWJR2D71YOEKOzLwM9fmYRlY6nFf5xhtS1J2Q%2FSfJ87hD&X-Amz-Signature=42e562f98d7a38b22e74f07373360039174f081d89a0cd11ffef67092898b5e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5EG5PBD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIBFCAYXrEQxma4d5%2B9ZPtEnrFFLdh%2Fy08JJ7NUQFjMsbAiAax5MgrTz3z18JkhQuZFHHXSJYyTIxI6aPm1C2cEdUnir%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMXe5lWcj6CZ%2BQANMeKtwDGD5TIDVYUgcKCXQg0%2Bh5X8pMB7TOygAlwD9KJrx%2F95Fq5BHtuMAdfZnIFWg1vQmE%2Fa5ELDjzHIcRfsvhJHZpP2Lea5opXx%2BOB4S1XqrhdbgOH%2BAnKsxLs3NvCokC%2Bobsb0GuZJpEuCuSrw80%2BzPzhDa0uJk905O%2Bg2aCaxzHHnjy%2FxiJvLMFZpwFbYDX3cgnxT%2FP52W61Fpg9Hc4yhNvjT8ORxznqvRgKeBGr9B%2FbCgJbyptRVZ%2Fwkhx4D3xDOWBxP0QNxu8eyI%2BCd%2FAk2APtVIS0xbAO0ol%2BqgATTGXPyIzcZItXxCcdr1EnM3Q3gzhjEpaZ1oaqDNfQYp4Gi8EKfUB5T0qyvy0aGylWlWfFlDUl1o98HL1%2FJbwBfo7yhZtFlj8XbPsurrwoFRqbO%2F0BvWLVS%2F5RvmoeQGLXMEvOUgRbm6USIkSo4r5v1lrT6f2aYOgm944HqowJGcydkLb%2BP7td3qd7vtDCP9ccLKYefB1nLWGnWXE1TsbOUWgdnpZdMdPQSGBAM6Zv8ljEHMs5jsYnxQSbtlF9xv48j28E90YpYDKk0dfDbMdC7b6YViOeeaFoKoUGUIJfk1pKaJLqIaKrH7nehHsVr83JZm9hnK1ZAv24d90S0vmlY8wp%2BCYvQY6pgEcwQaLsTHqNh8COkh%2FKppYzF0VHrWCQMT%2FdtKhLdWPJJda0c1NMRbfD6nWDtKJ8sH35gX8DKdJJ2FnGBxzlcksND9q%2BfNwSDsB8L8mvPTt4Mb6I6DAvPKnMoerMLaWUWmQfUQr29MooOZ%2BtbrH%2FTHKcvb%2BNL7z2%2BMQUTX5PsZx8F71S4Ma2xV4ckUJ9wrXl6c8mNCj%2Bzo57FhQ7mWItOUTZmRS1Mgt&X-Amz-Signature=d72592c5f4752e3ef28c9bcabc82c683cac12a3dd6bee250c815f92e70b418e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5EG5PBD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIBFCAYXrEQxma4d5%2B9ZPtEnrFFLdh%2Fy08JJ7NUQFjMsbAiAax5MgrTz3z18JkhQuZFHHXSJYyTIxI6aPm1C2cEdUnir%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMXe5lWcj6CZ%2BQANMeKtwDGD5TIDVYUgcKCXQg0%2Bh5X8pMB7TOygAlwD9KJrx%2F95Fq5BHtuMAdfZnIFWg1vQmE%2Fa5ELDjzHIcRfsvhJHZpP2Lea5opXx%2BOB4S1XqrhdbgOH%2BAnKsxLs3NvCokC%2Bobsb0GuZJpEuCuSrw80%2BzPzhDa0uJk905O%2Bg2aCaxzHHnjy%2FxiJvLMFZpwFbYDX3cgnxT%2FP52W61Fpg9Hc4yhNvjT8ORxznqvRgKeBGr9B%2FbCgJbyptRVZ%2Fwkhx4D3xDOWBxP0QNxu8eyI%2BCd%2FAk2APtVIS0xbAO0ol%2BqgATTGXPyIzcZItXxCcdr1EnM3Q3gzhjEpaZ1oaqDNfQYp4Gi8EKfUB5T0qyvy0aGylWlWfFlDUl1o98HL1%2FJbwBfo7yhZtFlj8XbPsurrwoFRqbO%2F0BvWLVS%2F5RvmoeQGLXMEvOUgRbm6USIkSo4r5v1lrT6f2aYOgm944HqowJGcydkLb%2BP7td3qd7vtDCP9ccLKYefB1nLWGnWXE1TsbOUWgdnpZdMdPQSGBAM6Zv8ljEHMs5jsYnxQSbtlF9xv48j28E90YpYDKk0dfDbMdC7b6YViOeeaFoKoUGUIJfk1pKaJLqIaKrH7nehHsVr83JZm9hnK1ZAv24d90S0vmlY8wp%2BCYvQY6pgEcwQaLsTHqNh8COkh%2FKppYzF0VHrWCQMT%2FdtKhLdWPJJda0c1NMRbfD6nWDtKJ8sH35gX8DKdJJ2FnGBxzlcksND9q%2BfNwSDsB8L8mvPTt4Mb6I6DAvPKnMoerMLaWUWmQfUQr29MooOZ%2BtbrH%2FTHKcvb%2BNL7z2%2BMQUTX5PsZx8F71S4Ma2xV4ckUJ9wrXl6c8mNCj%2Bzo57FhQ7mWItOUTZmRS1Mgt&X-Amz-Signature=bf70ebefcc601db7fe9d579b3aebced080720e89f42f7c2350ee30cc7beb4bd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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