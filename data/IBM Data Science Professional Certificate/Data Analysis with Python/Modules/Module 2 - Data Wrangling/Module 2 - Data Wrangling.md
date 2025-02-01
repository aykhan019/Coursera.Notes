

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3QE3YGL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFQ5zx7p5wEiIojbXGaRpSXM0dh4GcDOPH7ZJid9PS9NAiEAwEMExtwF%2B3qt77ig9s%2BtDq0i50Fz5yXQsO7eo8w0sWYqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNI8lnLa09auGoDy8CrcA%2B0QdHLwCY376JtOVyY09iHW5YtL6amKoGaPBUFxCiz4YYOQKSQplhthpOx0RU9YwDCXiOHRw911gP0mV45KlVd5aI%2FQtDvvsF2OSgxuLW5UAfegqc16RxQZAvIhULhMp%2BI7Qtqec%2FlI%2FZsjsfF0EOfH8d4zu3YUYWFeTJRb55eTR9uwAzvDjOCEodFOIqxn%2F0CRHQQ6iCStlkpvvHGNh%2B8IHg3kH4QE4Iv5AEYouxgf1og%2B6xPjP7526km%2B36C9cwFWn4Kkl5wVmR%2F5ktfH4YgLT%2BQ1Iad9Y5KMV9Z9WP9ytUNtR2f1VPuRXO4BmWUvc1sLRh5UAHGFasIxqQEP8N1C1%2BnzGq%2Fx41CaLPyZvD0r9ZjBwaXfgAgp1RBPDFoEp6%2F4pPjGVwlhGyo2B7w2VAFZrA9ogtZ1DFYwBhQmQ3rueOQydVPZTfyGqc%2B4xiuh8Vq1KUWg1rUSuO6J2il2muiCiG5N6h88uwoRFJ342hgO5TwqOmmSN2kJwNfx4PBVRalZYS97cS9TqZRoCpBZFRezW%2BvZGx1wuwSDJKFR5vHd3IzkRIYX6eoylNc7izap0l1TCX9saHu9Gb2UUC7S0DEWrMAR7xKEpHXvoc22LZvmIWCXF1rPruzV%2Fa0pMMax%2BrwGOqUBzxZlipauo68Kdj%2FXcLn5T1ALSv2yiYFLrEyugX5Quk6bWkv4EC7jsQMj6vjruPrePaVA%2Fm0QR%2FhbRBnZfpl17RpqLmr6uUSgsRNd%2Bnz7HrZ9s1GPTYoAe0PlJveeFqD2%2FMdJg18AQfee7tjDvqm78Rb5fKN1ezgGZCm7OdII%2BeGJVbCVAwWJrtw2d47LAyOf0oxev6INKwm9wiTBzHOxpnPDSTeL&X-Amz-Signature=6552b8b253941217585f11675cac277dedb08ee70bde38613b2480f0337baf85&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U7HFIGE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDHZIkXrqYgniZtI1OjSmUSaAmRljLJLYYOfDQsQcGm1AiEA98RHZb0cPcYdufAtdnL7768FPvM7aXDrPeBRee1HBrEqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPGydCp5b7yY1tDh4CrcA8PIjz8fhSj6kCKcFr43ZxqX2LqcWREA0ms7OZSgpzMhi5Z7Ewzi%2B81%2B%2FlEquQcgYswxj6xO3DSm06onsZQ9JKheksDEz8rk9oaCrZiuedDOeK5Lo%2BkzIOVMf0UxKDwA5PfHfTlWAhVLKXBfJThfeP9S%2FboXv3lFiu%2FMJDIaMDSZE8TRVdUchlRHlhGxbn5QASDQybwxVRtZQMn0Kr8j0vu666P%2BKMTDoKBVBglwHFFVitSYwak4SqXe9Jgli3bYY8e%2BsVRSw5%2BJiTiXZrK3zEjw%2FNuMG5d39sRgTESHu0Ei18Ap9sNM50GNX%2Bjb5tm3x1P40ywQcK7pCOUTZ4nF7wuLQTgg55%2FLHWOHiklEtQHtcP3aytiBJiJo%2BpGo8DWRM%2BrKniFOo7GijaDYcicGTeu4r3HLDDeledTwzjRBWriU1VI%2BeWs3u9GMcBvQqvjwd6QYDpRYo%2BUhQpjF4KajumaR1CBD%2BD4mVKHNH8orgp5u1YVxDtb7hbOhLXxrYaLpjYbIf87Gtl0T2HiDABEfKNpHRn%2BILlYApEHecDII8nsU84VFTcdZP0VC1e9T3ZuRGdWqUA7EREeSOAMIeLWlB5Ayyen9fU29ALPmLTQcjCyx4LqD5xTCNYMXKS4dMIGx%2BrwGOqUBTYb09MTdGy4pTRnUDy9dofMS98FKpNm8BjUaG%2BWuYIWpQwN6nwdneBaeHyICDaZEYfz2mCy0jxsQhvhNf%2BwqMb%2Bl84K2BWRVYP0FWLQ9HzTrCt6VidhG6YRXPr%2B9fzmDG%2FJmOCT23m1CB2iUtvP0m3aE7fSUDPVRx%2BT2x74tRva4CaWCKw3XtncvIBuULBb0hWNgoQ6k9FFXdO7saX%2FHpr9B%2Bx6Q&X-Amz-Signature=6745e64daaa282b945095713876d3d153923f055f725acb65e97f81fe145e94c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYRDLJKQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZZ7sLmWj7cdYiG0yvas260DBLzjVAbFsbG4PQpE1IAQIhAMKFFxiSnzAjvAVEOGmpt65SQMACg5pSYVTwdruGQAyyKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2jkM4sSBFg2NCt2Qq3ANYJyFXJgaV9pnfjXYLUdEzTobYsr2HyXgmbSAQZd81lI1GAUL4cna%2BRFUKyjnmaEpO%2BQvyh%2Fb%2B0EiQujo0dSi6jtGcSwJtGjjYFPxfLh9NUEvG1vr3lrS9GKGwRVCRBNgdi6kyEjVz%2BsFkrsYWcbwevgNUvfVyQpSy2qYnSb2OTXhbtJweN0stu%2Ba8PDJ5VrBdQaiv4u1Qb2HK%2FBA4PTk3Ae75%2FgUgkhiKkMsnXFdI6S3pdj15szt9PMSB2XIMon5C9%2B0k5M5T1AaVzTixd7GIWJAzaaqCCWyrQlWg5kJmrcJJLA9MJiMLlGy%2BsmlSK4RQ4jCMtlLGd7aWvVRAD9QpEGncAChpNRCaHvEqGiOev%2FXnv267DKFGDRNqslYW%2F9VDW%2BRrfFq7wb6%2FIOpIWEbQAD4rHr7FP8uVpDZpS24QIMufKGP639MplI4ayG5K%2BdFsoa5GhBStrMuSIjJztUaveWHhSACZWJVTX1i7q%2Foo0sNigDJOiNd6h%2FA94sc51hsN2uODBJ9c0V4V0kt3m4V0OlGZoZXeWSGqteLULpHH6JVynRXXUsrewLsoRGksSND3bvx5oAgX0h6FXDM1h18vT8%2BcuYKjVH58y5a4jSHPbEmiV5C1K8mTZNmFkTDIsfq8BjqkARYG58dKe6mDQGwih7CnYCVlmLu2zZgM2Y%2F8Kwvvl9DheE%2FybX9xyVEAiH7Uul%2Fd4ADJTJwT15NYANMvl4%2FpdgigP3elHd5rzMg7sPCijm%2FSPGof9k%2FR3uP50qFyIubIey%2FD%2B3ZYFXVD4tfLXmBWmB8X97r3sd5htZv%2FNV42%2BAGjZmIoSyHDIlo1SF4VZCP8Kdfi%2B%2BcYzEAi6DAL2kD%2FFgi0Zw%2FL&X-Amz-Signature=0a13cda15057f16691b93fb9c1dffb7e56cb2c6376ae7c70851b027dd7ef02be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AWGVDLM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsJaKP1hgWBUD8PVhOCNowLwAGkymuyvnKpe65zlPG%2BgIgBXeRDHgw3Oem4prEkY8PQHGOTwbv9eBEi5cSOAkVN1AqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2BlKUeusm%2FBYRCAwircA0JczuZRCnhvXCm%2BeLdtSC3HEzUkdTdMbyOA6lcuFPuuGUZSV8aprvn4i%2BHs1wb%2FhUkHw8NGFaswm8Ccjtg9b8N%2Beipu4ri6kD1IKjDtcHe1UJRE2ILbdaT%2BVYPOXfO7YYoD8VXQWPOWX1rtGmuUjGzE%2FUBHsxqMh25KRJkOGhHDzzo0v71PTZZUrsjnlXDUc8MMk3Ig6SnpvErMRuP%2FJqDoINvW5dAJPG4kTqVOEoATzjkVjSrJPX1TEDTx24TlubZbJEMdeho%2FFZChhuPoNPZ0f9E7qqoPkvMG5tMlDVLWHKdE7K7eeYKt0MXBIx2nSWNtnp%2F9nwyTQ08vIUnSQsk5knXUnfDUBGu74lQnVc%2Faj1DuNRrUIYfXgJwdb%2BaQ1sQB8FuSgw5PLtzxWF6bxMNVN1EEk7vemtGuy7bHJFqT1eir5GW%2FzdsKqHbBC4b6BqSss7cZA7%2F%2F%2FtTEYMeXQKDP46kpnzklIX3ueyueG2xnBBlJJxXO9VcGKqOefnFjOoewPed2d6%2FufbXggArxCJfIfbUjz2WJgUPk26%2Bovdpj0uvlSt8q5oEOaDGhIL%2BMzKSHvClbUQpmpn7eat8uH3i3e2Ci%2BcXPrrYGVfFPUq3UWZMcSiT4agE8GuL3MMGx%2BrwGOqUB%2FU8nye6EEBfontt7TPPCka%2BgiWrH6K3%2BzeuQxQX3YnUTpM8AuMAXZxl0266x7DlAfjZ1WCdRn3tySiSFBSpBMyLf8UUELeGoi59CvAB6lN8moZjQn5Q8akMdD5xUDghpHoOnorsKMxs9Z%2FK6Vl6xyu6AB%2BmJxaSQf0SVZu9Z90LAhHaMyH%2FeuY2Lj2PiJED3RYG4cCJHFgcikv6ad3P0Ui9p8Teh&X-Amz-Signature=652d04ce3cdd4700981d27e8574a3812f5b7538f6c1effc64638bd45ac7223b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQXLDXTS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFb1IrqWCJaJPdDbApaRj60GxJeRUmZmT5%2BwNlkfKj5iAiEA5bwVu%2BT1%2BopjdWuUtaUe2dLkzknvkrjiFmVOq%2B9rIE8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDVClFx%2B6Jm8EDUreSrcA9vNMpRSW%2BMno2JXmMJzvhO9mCc7WlREmXMXnalW4B8fbsiQ%2F2pNghNjRPsKRdF2whgfS9H3LtWykD4BlYoJUqnUfFI8x7sowHgdcZ0z0t1uF%2B4M4t9xfyQi1jd%2BycU%2BN%2BI%2B%2B5QOvovehZu3jl10%2FqAZWG3uSMpnkEImO1bDQMC6uT09y058Hi7wSQYQH3OrEY%2FQh7UFagAyJDeASMBGkkNJ7fqVVoM1xdRxfb9xX%2F3%2BBBdmlMzP6TJC9RHFdRKJfruapjKivYgeaveTNQjpkPJ34EMqv0WU8p50saKsJbMeZJAYKsBK79zdcoGSOwn0Ra2aBmd3b6ieRUZ7nWhNNpw8JZ%2BxWOyTWFMMZ46w7PV4JLt3nf79F%2FiMty6gtwB%2BXHSJ%2FQNGFypL7Lfsm1hFR1lrCH01pXDDGwk2RDJGEtQxGm%2F7tDMl2hpAfSDYEkJ7yoGogQNA2XXUa9f2bdcf%2FC4m4w9Rmd37SLnbMLNtxi4u31USFmgiBJH%2Bwt2s3fxIH0jX%2F%2FTDdnl0vOAw5L9i%2FTqVC4xtqJV1oQXw%2FltqUIzZlTvwtYmZ138QF8P5fg9JZ%2BehC5MbbmTEi5mR5%2BoAUbE2LuWySJZJcmsy%2Fk80DFU95ktAkdQF369%2FQH4eMMix%2BrwGOqUBSRN2Q%2Bw1UlYSvxtjwxIILI1WKFhz8Ny7WjDdTbdiLqpNNSfdffu2yvBojyUpIr5jG%2BuBvHrh7j3dZSyoUjlkbKSWMVjb7VPj6FrD%2FIpQiVcjXlzJjT4L1rmsWohbzs7hz4v%2FfU8xZaE%2FNEZKqil8IwytM0QUhs1sHif1d2qwHMn3mtl1P9pJcmKjhu9tIE5%2BKff14HAw9hBwVgmbTPjFWQzf6IpO&X-Amz-Signature=ddac66f6539291c2fb7b05f288e703a338160633e489cc6f37ffececb39a81f8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWNSWCCT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6wqnPchACSqx9xnK3aApDq50RPdEUM%2B9z9mlz3SuT%2BAIgDovsETNz2%2FF3XQe4qubZZ9PV%2F2E0iNSLbw5MHm%2Bzl5EqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNjeu9Hd8YTWNJ14%2BCrcA6bLt3KWNmnUQPLOhQLbaMv%2BZH3rZICIzNe6U69LJENz6ryattzKbTGWLadokeUbAo0d6zp9qeS446E2MikaWe1o4pkia3mnN8rLf4C7SHRX%2BGHO6CSGFEdjhuNy0Ym7fkByCZ2RyQ6GbTX0LNkbHu7j9BGQSc%2B7tnXU5OFkxXyYju7xZgL6Rx8hVgO%2Fmr3%2FPl0Xl832Pzg9%2Fx%2B7G7A6VvVsQqnggeAnn03icuHJF3Ju643VIKutn0GwHXt5PzJtIOWVqPrQHeGfwaZjCzvKh9U8b%2B4cMAsmePXHwyavG6nYuLLFC7bEw5XvUmO1F2BTj18Puw1u1yELmdAkglqs9S7oP%2Fovm74SaA%2Fmb%2F3QN%2Fb4G3SDIdn6is3Ad09J43NCKz39mNmAzZ%2FWj%2FJMzQu2nHOW2PXZd5XhmU1nEbaNRZ75An3nI4G8NgU09ipKpgcePjnnXHSdXqPuMtbTMyBtFP411CI0kc5cyRP%2BXf0hj%2FTtBS%2FjTQzrRswdfxB9NDSnBGYhCZnikuQw3fmdSAzrlo5asj3l%2BBZ3D1Vd9BR0lhYDoxt9PxRHd9Se9p33nKoIc7uRbBH2D6iG6eV7g0sOYMENodvfJ%2BGMyQgOXELp2kIRyqhxDAKDctDhzc1dMMax%2BrwGOqUBJ8EvB%2BAbtzjb0%2BrJR5tyWRlqcWlk9iiF4U1iEoXSA1K8No0NQ95g42xQw1FOwJFFu%2FcjZTb7tB%2FEybI6YxDThHk00V19npvB4bcpOPmp2BfojiTUK3MsSxcuvgJgH3cRgY0XGCplROWNRgx0k9DrpYaUYfBciFZcx8AnP1C8epgpzWuye0LVaFgT8893%2BaW6fRxZtFr5mPec%2FfQc7xB8XNFnQD9F&X-Amz-Signature=bc973c194122e02558259917ab675d45ed6c0d6ef2389617389acd269fc59a7c&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN6TQUKL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0VGN85xoZddxdH6ULJM2JhpoLHRHFWb4mhgNZSisJVAiBaIcsfvFc0ziDwFgtrXFLewwm0er8eJxi%2BPruNupIcjCqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJ5CmUEYYDyoLLXPZKtwD7q9cIlmmhWyzvi3YN3cVHNI6JDmGW1UyVZFBeg8KjEmnJSj3o235ZKpUgQ7dRh8ti0uKhMmNyCpnekIDCUmPo8cSxNmWUs%2FXjh8Nyei%2B6yc3zqWE5%2BwCcMU5CKyGt7jYmHNYVI%2F6w%2F4fQOzqH5syANZUrpjTFSW6%2FQKJ1nghWAVIJGCyR6LYNgLKgAyJAxXaIgc3UbixubyITwiGlQG1JJdmjIrcluHUvmplCxefkdZfPhM4XfN5mWtNVtx9TsfJZtgrot5pgUHw%2BHhwiXwkdo6OZW2EsLBf%2Ft4c%2BrHQRIRt9N0zT1plNnH7e1SMyOqNFdg4YYMMHmtLUbrBdvQ9Xj8R2%2BESp9SMkyySqQJygJlHnWzDJ%2B4iPvizCk%2BMkSRHeCC%2Fz%2BFU21jvnHHAaWmCrgOOGv9IKq0SoYO7PZPGwGhSwebe723%2F7oGkURIyaNMGxtasVQuWeWj7i3i6MYg6P%2BQSyYswydHdmxw1vLWV81zDGoxQ5xbowVQfR0eGOb8wKVLVjKMvzAD7rFBTy%2BRPAPbLcbsY9944vge3owELjCh%2FZXD8Sgge0gr4o845Z6nwTH7yboIf8xaeQesjsANcS9pK3hl9LsUgao4UPd6Oo6ECb8ULmCN0DH9uYTcwx7H6vAY6pgHIVsnLsbTqw7NvrZJLG9ifySHyFWijzfwiG%2FkruNoRfQyHr1Uf6WPvlaPv12Q16vnmIwjFXmHBNpfFAhILfrdCkWUHRJ90wo6srmFWx3rK6fvjQFiuu%2FYNh%2BidZYBp0LKlK7rajRSYIZfvNlqH1Ci%2BofemollrobwwbTZCL5ub%2B6tdgu6xdYFjMDoNw2fWhg%2FS4kZxO3jXYvu91GPybGPyLgmMWedX&X-Amz-Signature=8927538c1a471eb32dc9672ea2b1157ae8940287f1735a978c9a54a8ec398f1b&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US6T3B6Y%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC55MqEzi10x6RJwmbewfEB16SjBqCDbr5m%2BwUNYjIYRAiEAm06p1aRHeTPRwBUqr%2FdgRrCnH53SjnkXvvYJd5cZIAYqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3ZUGpJNWBRpq%2FGdCrcAwhT53eKGBb38pGe5jAF4X830fTXm4qnZNrDXEm4%2FhBpTIwi0cIyD2U3k21oVXAwDbXQdPABgiHcpYPlHmOUrSzpx7Q%2BsvHU4KDa1tNblTM8TbXA2WEsqUn3QTjpLDezwYs6E8Gs2GXt%2ByQ%2B8IdkK8YvK0vP3KDWKCK7G9W89F79ogPBYdrRGy6tBahiSHyIGCXa8kyXE2FmquIH47F4zSa5hyiWatlBb9f9Pbxz0yAYnRDf2fBB9QomhL4uSmvJZob97WMNlZkhpCiChaYnv6MOSsdMxbRz0xkaIrkTTTUP5LztEMjTJpZLOJLmXnPLLiLACfyhIbNUWiBH%2BcwzxmlxSDtgzgWoape18Aa8wRB4nSji7%2F0nbTH0LJTjEmaxjeGtYxmIV6bQnq8ipIjW8m3DlFiofqzZJVvuIhrAf6s8tCrrcZNSG3B1LHKttxhxBcGY3Dq%2Ba69Qjm%2BXfosYPLxehmgGw4JXxxGHwiyBLl%2B%2FIgyyNd1HTqsqUjvMj%2B9vt86LSdDq%2FyRl6TdFpe9OW6c53bmcOiPhI%2Ff2vuYL3SGD5OjFkuMImh%2FcW12J1YHH4jjfEHjGU0ecr9nrIrN3uopBXv1J2nB%2FKmmRArvUgaGQm741Sub3L2%2F%2FxOMeMP%2Bw%2BrwGOqUBvMlmsK7Pq34mckmWN9mKJnuCZ59RaF0zJr1Noh9PKUBH%2FSero9aJabv8dP6sySmXxE%2BrXu6sondZ9v5ULnwoTp16hHmO5xMUdOwkue4DCnO726CsMW3f9LKjNKQ%2Fu3WnWbcKb6K2gLCWf6jocZO9jCqU49T2CaeLpvrO51GK45z73b%2B1R7i6m2RlsndLsELqmwOjyRqeJ2Xx0Pjk1Jkrx5QIf6z9&X-Amz-Signature=5a82e826f4d47f784c928848835116e27599c056e69e5b678a033f9dbaf8b822&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQXLDXTS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFb1IrqWCJaJPdDbApaRj60GxJeRUmZmT5%2BwNlkfKj5iAiEA5bwVu%2BT1%2BopjdWuUtaUe2dLkzknvkrjiFmVOq%2B9rIE8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDVClFx%2B6Jm8EDUreSrcA9vNMpRSW%2BMno2JXmMJzvhO9mCc7WlREmXMXnalW4B8fbsiQ%2F2pNghNjRPsKRdF2whgfS9H3LtWykD4BlYoJUqnUfFI8x7sowHgdcZ0z0t1uF%2B4M4t9xfyQi1jd%2BycU%2BN%2BI%2B%2B5QOvovehZu3jl10%2FqAZWG3uSMpnkEImO1bDQMC6uT09y058Hi7wSQYQH3OrEY%2FQh7UFagAyJDeASMBGkkNJ7fqVVoM1xdRxfb9xX%2F3%2BBBdmlMzP6TJC9RHFdRKJfruapjKivYgeaveTNQjpkPJ34EMqv0WU8p50saKsJbMeZJAYKsBK79zdcoGSOwn0Ra2aBmd3b6ieRUZ7nWhNNpw8JZ%2BxWOyTWFMMZ46w7PV4JLt3nf79F%2FiMty6gtwB%2BXHSJ%2FQNGFypL7Lfsm1hFR1lrCH01pXDDGwk2RDJGEtQxGm%2F7tDMl2hpAfSDYEkJ7yoGogQNA2XXUa9f2bdcf%2FC4m4w9Rmd37SLnbMLNtxi4u31USFmgiBJH%2Bwt2s3fxIH0jX%2F%2FTDdnl0vOAw5L9i%2FTqVC4xtqJV1oQXw%2FltqUIzZlTvwtYmZ138QF8P5fg9JZ%2BehC5MbbmTEi5mR5%2BoAUbE2LuWySJZJcmsy%2Fk80DFU95ktAkdQF369%2FQH4eMMix%2BrwGOqUBSRN2Q%2Bw1UlYSvxtjwxIILI1WKFhz8Ny7WjDdTbdiLqpNNSfdffu2yvBojyUpIr5jG%2BuBvHrh7j3dZSyoUjlkbKSWMVjb7VPj6FrD%2FIpQiVcjXlzJjT4L1rmsWohbzs7hz4v%2FfU8xZaE%2FNEZKqil8IwytM0QUhs1sHif1d2qwHMn3mtl1P9pJcmKjhu9tIE5%2BKff14HAw9hBwVgmbTPjFWQzf6IpO&X-Amz-Signature=293589120f931e63b825236c15ed3cfca85c9ac27a391c5c64dfee90768749cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URGBANYH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBm5WPNAu1zdVj2xFCUESSEnq2x8g9by%2FBY1kGGQNa7MAiBJHWGnouV0q0F8xXOEHsIbttAo%2BgkIAvObb22inPlhfyqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMpwDT%2BH9SBvJFwRpKtwDWaqMNX7ydUz3FShcEML1IllAA5gDSwM2u1ZzCBk8w7nN3UR5OePVgL1ZwsA31lrZ%2Btk61Eqq%2B6bW1mPzuzGm0jOlu0vHFspUUt7WphtGnt%2Fu%2F5IC5zyLWh1t5v2ogAeKJt54Wg8TFGdiZAnt63pZi2ORDNJZJK8TlElun%2BiFWKw5SlrZl3%2BtYWMHt6VAjWqh%2B7OO9RZk%2F7bKEXe3osRwpds7ekAZgyxXTml5I%2BL9iNEMTJ8h6z5v6HXX0ayckHyFx5KVcYcfd%2B4hhImk%2FJlwtOJKy1Cqs%2BhEnft9LXKCLlYxPNBcVRQbBOFKxyD1uDO4gR1GHVVq9YSW9y7sM7YCi3AG96%2Bllf%2BozDJ4e7qPRF9szpjuoZ6yfiRiiBl2nm1d06XV6yuBpU02fZDxJlv8A0OOlNqb%2FeYoN%2BL5YJie432ZdqhDfzWyYk4gOBiXl%2BEqF1M5UQugFKWv3WiiCitKvA0Q8j6Oal9VLFIm%2F55254gKyE8fsVuRArHZPY1pV1PkP%2F4tCDfHFX0%2B%2BEF0JEhcKkIZ2UgT%2FwmjemOHXCjKV4foK1TLcblcttzKTXXhR8HYlhp4RI4mUGPwRpVvwiACcV5lg3xNBFIKuHbOrqGNIuj1%2FXVZ%2FvNjcsrhl%2BQwtrH6vAY6pgGcNflrK9zQs0mjP596T1Q7fqkL0L5FFLecqhCbn8BHXPLdIR%2FcjBpJJH9x8WzLzTeMdEIHQFa2JSPi9FFixi3nVXk8eQQSznW6K5h64OjtJFpudrWIoufjiXiWHui%2BE90%2F%2BQzuaUlB%2BKhWSh4PZC4%2B41OKfSJDYj7NrpU4Lj0YNj09rTl8zwzOatFt6tOj64P%2BQbmZIMY7wNyJXu2UcdB%2FtNIO%2FDPb&X-Amz-Signature=0a799625f6c4ea764ed8e40b77a34f24e9bd0e4db1ca53635fcb5edafcaf20b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URGBANYH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBm5WPNAu1zdVj2xFCUESSEnq2x8g9by%2FBY1kGGQNa7MAiBJHWGnouV0q0F8xXOEHsIbttAo%2BgkIAvObb22inPlhfyqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMpwDT%2BH9SBvJFwRpKtwDWaqMNX7ydUz3FShcEML1IllAA5gDSwM2u1ZzCBk8w7nN3UR5OePVgL1ZwsA31lrZ%2Btk61Eqq%2B6bW1mPzuzGm0jOlu0vHFspUUt7WphtGnt%2Fu%2F5IC5zyLWh1t5v2ogAeKJt54Wg8TFGdiZAnt63pZi2ORDNJZJK8TlElun%2BiFWKw5SlrZl3%2BtYWMHt6VAjWqh%2B7OO9RZk%2F7bKEXe3osRwpds7ekAZgyxXTml5I%2BL9iNEMTJ8h6z5v6HXX0ayckHyFx5KVcYcfd%2B4hhImk%2FJlwtOJKy1Cqs%2BhEnft9LXKCLlYxPNBcVRQbBOFKxyD1uDO4gR1GHVVq9YSW9y7sM7YCi3AG96%2Bllf%2BozDJ4e7qPRF9szpjuoZ6yfiRiiBl2nm1d06XV6yuBpU02fZDxJlv8A0OOlNqb%2FeYoN%2BL5YJie432ZdqhDfzWyYk4gOBiXl%2BEqF1M5UQugFKWv3WiiCitKvA0Q8j6Oal9VLFIm%2F55254gKyE8fsVuRArHZPY1pV1PkP%2F4tCDfHFX0%2B%2BEF0JEhcKkIZ2UgT%2FwmjemOHXCjKV4foK1TLcblcttzKTXXhR8HYlhp4RI4mUGPwRpVvwiACcV5lg3xNBFIKuHbOrqGNIuj1%2FXVZ%2FvNjcsrhl%2BQwtrH6vAY6pgGcNflrK9zQs0mjP596T1Q7fqkL0L5FFLecqhCbn8BHXPLdIR%2FcjBpJJH9x8WzLzTeMdEIHQFa2JSPi9FFixi3nVXk8eQQSznW6K5h64OjtJFpudrWIoufjiXiWHui%2BE90%2F%2BQzuaUlB%2BKhWSh4PZC4%2B41OKfSJDYj7NrpU4Lj0YNj09rTl8zwzOatFt6tOj64P%2BQbmZIMY7wNyJXu2UcdB%2FtNIO%2FDPb&X-Amz-Signature=8a144e830229071e1460f3b338236f2626f11378f5ec1da6f8cc30670e7e2024&X-Amz-SignedHeaders=host&x-id=GetObject)
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