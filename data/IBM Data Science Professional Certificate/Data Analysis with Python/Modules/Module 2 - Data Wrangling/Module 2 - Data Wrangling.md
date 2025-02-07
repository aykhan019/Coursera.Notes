

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZM3DSLI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQD3hSKMS1ENeKNEDCfjCix6VmOJl7kP3GK8Wz6FhPZJgQIhAKOZc4EkKSgbvRi6uxX%2BHQLP99E9Imy9gWjHY7Q0G615Kv8DCH0QABoMNjM3NDIzMTgzODA1IgxZGiLFjjDHWBjFUx0q3AMdyRRyu0XyfJmWy2NMOMiHH5sKZNMZUTpZPpe88a%2FZ5mW4Lzc2USpvmgwVuL8WoxjjdiF%2BBudKAUdY%2B%2BXEFehlpxbOzPW82ViDlWxbWRi%2FIz6%2Bg0Z4E%2FaRObnJ5Xk%2Fufp9WcgdpkwUeznqlEI9oLOCdZgpUUH27vZ%2BL8int%2F%2FLQcFoMnOaYmFYkmhdfIGP8LJU8mH3RglV3QyhlUki4952RRqbP3HdAsSkNu2rntabKdqIQ1ugW4xf6waTQejHQXMMOvxAQHAZs0xbIYS5nlA5bpfZyRKdM8dNEJvuXv1QguhCA8VWOx9PASKz9N7TLzfMoG87SkcoZ23h4c9PBri2KSSoRW3O3jinOV5c%2BwxI%2BeTGR8yrTTWoVYW4eKlLDvcXejsYBftkU31nyC7t7qBgQtZ7FXe4etqVu6BDFODkDxzp%2BV2eCnVR0SXOyb8g4HtaUA%2FRJGHLjTEo3cxm7hErMnCpjqOv6iIJ%2BwOlR5mZZK%2B1qpBe9yY2o%2FSqaDZWfCZs%2FfUToC8CJbBQdjfzptJ3GhwnkvcB%2B0IZyml6BYh2%2FEQxbBKEY4tJKYYhMKIk5%2FqDC1B1ARit8sb2ETfF%2BFtinEQUVMhJLB%2F9%2Frvgz8fbXK4CQvcpuBBbA4M1fzCk0pm9BjqkAek8zmnOa8jC%2BAf2jw%2FCZyySBvftZRhhLyyg2YDDX%2B8dXukiJdVAv2NA7P6zzf5lAjLG5vGt2qHuwVfN%2FdVpAfbvoSZab1HteYHtn47JF12ckA5OI%2FTQEX%2F4A0%2BtFSGQn%2FVmjMZCEJNd9cAjIlx21BzjQL9DBmDuAB25EZIp7pPaD0WPR%2BJa7Ih%2FNVgHqHPMEHNwQsu4OeBYPtYgyuP6KuJTyAUS&X-Amz-Signature=616606e3676fa049524eda7ddd70c08d1624e424b421d96f8d61292b015ecc2a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T45GCNC4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCHTu8vxfE0cXCxF%2Byle2zaBKZMtdH7n94qv%2FFOwRuLEQIhAN17nXSEel4hGHvBeY%2BJFw1BB%2F1EHhlkSg6dpNAYRWHEKv8DCH0QABoMNjM3NDIzMTgzODA1IgyoSVjSLJH%2FfpXTKXQq3AOCX6TIkS2Kr0iRqCOUxMtHtAtDRqKFwMx7gkj%2BcnZZEcK3K1gTLyvPZFHTIyrI1rPY9iX3Pz8kflsS9ykfILpubQoQFUorer4P2w1InHYP0qvyiqmVbA1LNB2IzycWbUH3ik5DGuL0OayMtMT7qt5K2m69oKSqlA4LSmS2QJNZsiXviIJeRoxLcJ0LQLSRPU4eAN6ztxN%2B6I9ChvESZwt%2Bab9r2ucCY7VV7eTUKy%2FwEuP0Xu0r3WvKi5hCOWlqNlfsysQt7jv5P1tqQvbdF005CwhfykFwxMpnwWYHq%2FRcdbSKrbm%2B5mfS1jpeT2V90jRCmH9lpaNMwH10PMsxoRE0sax9ZzwKnj5Fwqxyjsu%2Fxof7QUHn8McAiSNTIxJC2JcCdpTN55ald16kp1Ck2jWtQvxvTWY4Z%2FGxXRX8cnxIFVpgr%2BaSe33Hs95k3ULRxzw48UljI7Vfn6KoWD%2Bh7tx3hhCYX1XvQGEAME%2BoMrnQWrd4XwxPEqXXLNWpVXfhOCFORib1jxPnZPYOrWN8MM2r9VpLlN4qUOX2Mfrl6ChQ6dOWjnlexr1g9h%2FUim2VLlkisLkUDRbLVoR5sKR0IRUrPY%2FHzm6xCfcgAiwm51d76uHE0uxTTssOZe269TDA0pm9BjqkAa%2BX5Xt1zOhVvqO1VVNNYfvtPNnyrBxuly1i7qAdblcFAQ7hOwlO2SRO%2BNW7PgrUQSUNy45zcrYWCjSZ9zfEgVPSSFT8dQ6js7RNboPWAdJ6JvdDS90gtVW1o5hMuYwdlLuTTS8Sr3NbLSAOQvtlrKzyvUG6zwftOS7tdA6wYMGw6X%2BMU096VonGAsQ211cLPEOv%2FdolOgJQ17ZA%2BxZt9VC1wWOZ&X-Amz-Signature=3a8cfa71cc3688412432e8031ea2a692e7d4677d86f83936194d229927a8f64d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWRKCHMA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQC4VM%2FAgsQxmOF76qB9GT2gMZxXybp7ns7as%2FbeVI4VxgIhAIy8NQPZi73dXlOfC9Lmksm4gE0MEl6W%2FNkAeo03arNtKv8DCH0QABoMNjM3NDIzMTgzODA1IgwQQxELV%2F0%2BGt47lsUq3AOI6fTAA3jbe22vNKkrWJ1EP5FORgpSK%2FkH3Q3wThepBb9bpwchBzpxbKbIMin2cjwqGCLjW0UvialrM2JyrDbyYRToIdVMYn77aIDopxlsbaj1grh6lADKUHTif8P5WncwDGzrsC5506tcotVlVNbQOI%2B%2F628WHDYpIPlneTL6m4gAv%2B8To3pA4Gup0hvnhIHVshhikybEMkrZckcTf4nPsPhxZFiW3TwhtHfVrluakQ%2F7kOVHLkZbozLLFzEsCHO9DQrr2oSn3gY6URTOWAb8xGW3lPleWZdfPBzHUSQNC3k0%2FNh1eU9nzUkAIjKpHCmkGdlb93%2F%2Btdq3kRAtIZRse7VR5cqBw9VDyHs%2F%2BYO8PqU4q17mss1zj9nikv9fYcLSTHEuCvX50Jy9Ygjn8FPG3JPBi1wYDk38TRX9KCBrtOrxpOZ74DIp77tyLEAcYIaRoUO51d%2BANltfzGH82CAvpF0898nHUUporVg%2BliWLaNaw8LCIrxvchMfvLoq3gUNTV0w4CWPgDGenUTqtDix%2FKUv9vOgKFIgMblXG6SyTNSOoNFX6UVyxVapJvfejHXNZU21eyNKUIELg8AU7TXm56cXaeyHgvLfBsIK4BO5s%2FVUukdgXc1PVrZGVtjDo0pm9BjqkAa7nLWySTFAAnCPRGDtgnsVqKVI58SiY5JoKmKjLIgmsIKebjbCl8HhZcEZN9%2BaUg1dMb7KCyxCWM%2F5LeOxybWTrmVAXgkccWQjqDTALyo%2F8%2BZH2ANr5HOpgDytxmnrIfED5r42xwn%2FCnZFHgm%2F6CvqN3FInsaHStdHEvCm%2BO74eDvw6S4mzFugnRM%2Fa5%2B%2F16MvKMRlbZuwLZKCFB3OOoV83rd5Q&X-Amz-Signature=7096538643505ae907f674b1b65d5cfd7e765e46ec0efc7b7cba06fec0508fb1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDZZ2V2T%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDW9NG38TZG9DK3Kbqwy3BEC50ySCzbOLkEWc993WVyfgIhANy4COwQJBhbO%2BV%2BQEIHolsQdDkofwDY119dHpWygjvRKv8DCH0QABoMNjM3NDIzMTgzODA1IgzYOemxp6PDPLi8NZAq3AMumM5xMUHDk6KNk%2BDiAsaNH2JUQQxKpFH9ykydwGq4ZrMvXqtJ1CBvsTK4TO%2FpJ6wzh5f9IbRfhLbO%2BybT0YpLmb3WToW%2BrZ2Y9E65kRFrTeFpkYv3Fpb78E1YinXm9TzyGcSbvrsor3tdGcHtRrfDHfTJSHcs627vUYLHhjxpLCDvn1%2FHTqF%2B8y%2B1D7nZps6eLuubTuMN47%2B5NM7HfMjT20FbD%2FJGF6T3q%2Bw8w7ojTpaWvrDpqZmE5edCg7yjBxDmjd%2FwHB0LR9UTDoDcZ%2FWzCoce1aGJe1uCv6VZMIHsbf5h1%2FJg6qAQcpiSTY9jiZeQVPGG3o4N9FlS%2BVwbn%2BSGmal6zcMW24pGYFfNY6fHG3m62psL9oWK0H4GBXrdpqHLQZqiF8Zc5KDgule1xDnsq2KuzSApqj8E%2B6xl8fjPQbi2b7rae9n48nJ2O8BL1zrCAMSXsD1n%2FT1nyx9zlh9kpAjnkicFnuD%2BNSqBcgkhGREOZmGiYO8V1yyXiRt5opAebeV4isckexHSbuVIpIe3BBzvUT41lOxnF1iW1Pqgp1J1%2BUAH8LBUANBcqHVbasyiQ0C1sVNdlPLtkrikjQUv7Bq7%2BsePoZZkVBIYlUA%2B%2F5ddr4euSNGKsOyKZTCs0pm9BjqkAaydoz4Ck2yUgRsVrSte2Qr5s0imYdEUue8mI5C3rG4hb2HpKZbxMYIdqq6ZJZw2ZZrdM8tTrWSKemBLwWBN7w4KsDERcTxedjLuAs8LsW%2FsdeClVyDdakwCLmjxeTTyjBFPSwgpji%2BdrotNHGBqUjOKOYey%2B0JCehg2srred56KtXEpGP33mj%2BQzmeZhkVfusJqQR%2F8dlUm%2FuEiUiRTruQTVCsu&X-Amz-Signature=f3c31000fa5fbbb3feb94340b8ba42b4e71f390bf0188fb94a0e662e9f263ccf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UF3UC4C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIBncWVkgR77yF%2FtIUFjFPLfyzEfqiDqOQL%2BiOnp8vVWRAiEA3wfRqjdzqropntEXZYe%2BcCJpkraI4ko%2B7lmsU9k3Smgq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDw4qSr4PDIiPkBuKyrcA9xquMmcI0Hv4ZamUGpbbE8LBJS3OUrBAdHv9pPcxKjv5owAyfWKV%2BFbOhKJyM337zz6R9rN0UXh1jRqaZ%2B82rtWH7XZLV%2BmBL8Py4lAEDaXkxiNTe%2Fav6okwspg5aoopmG0Qmo2viPODEu6ANwfFqDIaOXLf5CxnmOEYRaC%2FKErTPmcyN8ZDioiwex0vLxA6ZRM8yBCSkpP9yFyRwLoWjY2x97y1ImM54zo7waR3jTgPhzZOldYrR92zKQHl77eRs27zKyqrqoKA6wMqgsaEjOcF%2FAg2VzpiQELuTjQpZmwCf1jwt9HmdZJjFrY9%2BcItvbMsxjCCI8RB9SNu3cc4GB1lu57UWigUITc5EpK93nDbqfWvzSHQ%2BXDGem0SVlhPyoOTuiYnuT%2Bb1uxubFRNatVcLhlxbcR7PXf6p1ZaEeO6oSPNbI9mpK3YDSb6SjkwZBVZOjBRqQrYvTDBD%2F8gs8BkhkWGcCJKRpFy6LqYzJyL%2FdOSinBLXTKzTWDZJFuB1NwXnxZufJ4UaVzjwToxZpNuK2S2i9SNAuBaCdlDi%2BcH2M%2BdOAqdiWUwtL7E2u%2Fi5B1bH7opuMlyCqJfXE4KYF1RnGCFyU5XPBOsNxnoJgn%2BqylbkPYU7ZypCNgMPDSmb0GOqUBpNkABMhbPDbfSI4DMUEXC93KtQZeJgM9YMYIWHO6em8PEdamRJBBbl3f8qmI8Xf8BvZrIonR962m0pEZwj2zv%2BVd1eBuyJkxcojjs%2BFPcBqBXBV6EPf32vSy9FXyUnIL7m5JxlT0InyDdyzOAIcnyLlOqtCr1QOUfIxdAe049qqFWFCm1qnN8yKZOz5%2BQ5psDwObS7QlbivLgAGGedmgBhNYobbL&X-Amz-Signature=2af90cfb43e070122fd55eecd0e2e81c06549bd1c0c5cba28fc4d55a125cd99a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6MBQU36%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIHjEyq7FDgqK%2BZP3TOBKlr54ELrrj5OANte2nCs0dvmTAiEAsKBb8XZ%2FABNUvKn0esB0iDT5F%2BHkccIVvt4bhBBZ3P4q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDO7YyXXD4xJeXpX0ayrcA7Lt86G2OHSuus0kwH0r3VlTpr%2BhGNl0CPDyyaFaZEEQF5ZaJ60y%2FAbAg8am7RsJEbVPjcJSrb5UMliQm72f3GvixtxLtvhbciQHVc5bBuSEQPi0X4OwN%2Fzm9PP0CDgDU2YJ0bSGfeJI%2BhaJHVIf9AIsJHEi0TYswSKpcCU0evoJgtbjDyF%2BYPZxGa8J3dtUEMmX6Lc05b%2BaQGE1yWv1V%2Flxd6xMmyhek1tKEArNNpcxE4fovTIKM7DN6gfaJ8KHeyywKieVyLTU2ySVoh90Sde7CGbnoJUm8ASsON4iZ7I8YelajHChf4I6OOCWUBmJ26SGTXc0rt6ZDdKEbpa8UQ0mLOUU3h8dmVSaMlHRFBHtxJR1dk1RI4yIhELY874ZcVGHBgevvXsvtcF5TLXpUpWzr9I21KP1x%2F3DYUosTAn2w%2F3kLxhahJMUCbAxb9npobguepbrf%2FeCt9y78PRzdudIu%2F%2FQRP7cIK3QhiJh6HjAax2kq8xZuzJ51V41zj0dXnofouMQAxR2GK61NgHIDN9Vu8knO91QMWNtkXibMs%2BW4RzQtj8zdpHJh1aywD%2FthSWcD8bo38Ow%2FRkHXDmaIqJUTBW32Czyb2Zu%2FSUas9JCKKeeDAV8Kokx2wtaMNG1mb0GOqUBJ7ABcHLRoo0aHRLDKq%2BuulSRY2R4RLkr94wtJWwfwAaANH414Na5xjcg1GIsG4is0cR4R7m4tI%2Fi3MhhMe8wXVHYwe03HhKvSVCJZ%2FwqhZiVMCyzjNTl5zkVJzLJ4ucwF7R5jaNY%2BnLWIrfl%2Bdb5iCBjNrSf2wKg9lz1vnC70eO3GD7fCbEcPIHn%2B93Gh0VHBscRbj%2BaXdbutG%2FnWijWA7S8xyF7&X-Amz-Signature=696d01c9a07e1b5d6dfaf821ebb73da748d4c6c49b2cfb5aea7bbfd3800e9fa7&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRJ5RWY4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCmUIddh2rJVicQQT9gUvlZQwP6cQ9QByzfzYcGG9n0QQIgNumw5AJJyyUJAHZ%2BWs8AkygAhXiE%2BTPVngclYsex%2B30q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDMqHMa4wgPe7XN%2F3myrcA5iMjtsXgn1xu1XouhkB6UboFVA7AMTV%2Bc3wxPpSMnkFUr9Rl5xsaALhawJ4fwBLvx6WZhGZFPpx7wmHlWdrsiSmLT%2FzhgEYXj8%2Ffe56rpg0MMEzvmJGL%2FGhPMW5cZLVlyZl9ojyC1OaaLcpaNBo6ILVDjG4Kz9UDd4CHAyRhkjx5QD%2Bwo87USU7drgxLQ4WWMoeQUIePxZXsEqtvR%2BmqkhcKpcebGeAtplwoFwkyRR2HXEa6xoo8N9i0CXOdVRWnn6n9AOxMwi1xPwM09qJBSmoA7NhUKbR97mKfGGtcCRbxuRSiu2RoPJoW7NCEpzaT%2Fl1THl5unQ18nNkw4kpL4544GXAt3SJ1Zss5%2FhDNi4fInPB0DCTJ7SQYuo4CDv4gHnARFaDjoYP0efFV2kew0Z0ca%2Bc4o%2FFptn0OwXEy%2BE4bkXUdfOMc4VENBH3pk4iFxHczAuCyW9F5gJKx%2FJtVtlnI%2FFHiZbYofBRSpkDaieRg8BA3OxYuzevcgF6CjfW8orF5M4gsmLytslb82k793nuBtXiPlJDXkoP1y%2FyHLPWgfBAj%2BgkLE%2BXmVDZ1ZgqYB2feWeDM3pGyHHtEkiZKznkIbPWG3E1J3tfxtWkSYSs5KUmGc8HDoeAzbRTMLfSmb0GOqUBWyu4TVMrQYDMeWtjRnYyQGsQngcakw8pp%2FFhyN4dUhxHCJt8MHQUXk61uvdE3nQAawr%2F197YTz4yfSB3cz7V0uux2qobhQeCfenh%2F%2FCPyLy0IQUwnW0Pmua6xYON9fP%2BLRjr6euA9pS0RLlnKTtbqYpBlQWzVkCoS9%2FLKwPE5dlWxGIAivEFnCYAGwx0NGABkEOrYIptBvPD9rscI5bPfLcfGMnW&X-Amz-Signature=610a51bfe559f8b636117808762bc56261d5a6b93477f96cc828db3a43cf3a48&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DX7PGEF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIHmFnGz1gBy%2BzJEKcuRdMdrxl3i7ur5PWbbFJuu6kxGQAiBXjFJSdcyNy5TayYScTPOJEarKHMhiFcR51Wm4%2BhcS5Sr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMuNoBotnj4COCve7rKtwDaND59BGk1gat6AoMEgHaYegrXePpVDpDiuXclwyG09hiTrWu8eXtr3MsopPiqszRfcCUrvObz6XiBPgX%2FLcetqSI7n%2Fw07B7hzzmW%2FJw1gB5OC%2BZyzR%2BbL%2B4bh9QNUg6VNTjvTprfYffh%2FjJD%2B9S8DWKlT3PZZQNTqYgwdRxqsVyEgbEgPdNrUjoQqFCIotZilenM1YvKxkcx3SlvXBypO1BsesveNQSE%2FD6uvIui5aHPmNQNJ%2FcLK7Z4GtWv7FFnhdh9q9nUIPFzFeuhmGmiMLlakC%2F3zxy0FYB8WCCO6L7IvcN3K00kmhCRXmMnisBm3hQnnynkaF2UGbxJaQGhvcSi5Fwh3n%2FBqOy9oo1A4NsEZ418uXNx66JiPtXGc2%2FY1%2FlQ5uhhpygu8JQgYUsmPy2c2xvYrQ5UhHtjuMWYq%2Fy0y1CwTdJQFJvgY3gHM%2B44fDRxuTB1e2EM3VJYARMle7YIsF0rkgq%2FNldZvi0NXThjLo%2FE7J9e%2F1ZKUCjCOAzeoq994W02NIWcZcdKoYNpI5xEujh%2BUNCUgEkWwsqCFbXew03LpejHn4H9A0%2BFJ4nJxu4GAJ%2BTw%2FSNEopev8z4ekcPrvbyD3RlACkkG4BkPPZHBUOrmqt%2BkzVL4gw1dKZvQY6pgFDI8I0kYPxc3aJ5HO9stFvO%2Fbeht7cf9FHiP5%2FlpUiCY784Mz2BCXx1XK85Iqzz6xMHao5Jd3dv3SrguZJU%2BKFgSBdDWFuU5GxuLPjg0M1uinyhl2Lc9YLXQDlaEc7Brrk4%2FFp%2B6%2B7BZh4SZ4vkPsLvhoKXx%2BimkRNBNmwKuSNx3ssoTqybu9wenO54hxvDq4eI4GuTlmpyI46svvN24boEuRLEuWN&X-Amz-Signature=ae8b2b15902ac5de4ac591380afc5ceb89f75109713ae8c248e133e7db5d7571&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UF3UC4C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIBncWVkgR77yF%2FtIUFjFPLfyzEfqiDqOQL%2BiOnp8vVWRAiEA3wfRqjdzqropntEXZYe%2BcCJpkraI4ko%2B7lmsU9k3Smgq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDw4qSr4PDIiPkBuKyrcA9xquMmcI0Hv4ZamUGpbbE8LBJS3OUrBAdHv9pPcxKjv5owAyfWKV%2BFbOhKJyM337zz6R9rN0UXh1jRqaZ%2B82rtWH7XZLV%2BmBL8Py4lAEDaXkxiNTe%2Fav6okwspg5aoopmG0Qmo2viPODEu6ANwfFqDIaOXLf5CxnmOEYRaC%2FKErTPmcyN8ZDioiwex0vLxA6ZRM8yBCSkpP9yFyRwLoWjY2x97y1ImM54zo7waR3jTgPhzZOldYrR92zKQHl77eRs27zKyqrqoKA6wMqgsaEjOcF%2FAg2VzpiQELuTjQpZmwCf1jwt9HmdZJjFrY9%2BcItvbMsxjCCI8RB9SNu3cc4GB1lu57UWigUITc5EpK93nDbqfWvzSHQ%2BXDGem0SVlhPyoOTuiYnuT%2Bb1uxubFRNatVcLhlxbcR7PXf6p1ZaEeO6oSPNbI9mpK3YDSb6SjkwZBVZOjBRqQrYvTDBD%2F8gs8BkhkWGcCJKRpFy6LqYzJyL%2FdOSinBLXTKzTWDZJFuB1NwXnxZufJ4UaVzjwToxZpNuK2S2i9SNAuBaCdlDi%2BcH2M%2BdOAqdiWUwtL7E2u%2Fi5B1bH7opuMlyCqJfXE4KYF1RnGCFyU5XPBOsNxnoJgn%2BqylbkPYU7ZypCNgMPDSmb0GOqUBpNkABMhbPDbfSI4DMUEXC93KtQZeJgM9YMYIWHO6em8PEdamRJBBbl3f8qmI8Xf8BvZrIonR962m0pEZwj2zv%2BVd1eBuyJkxcojjs%2BFPcBqBXBV6EPf32vSy9FXyUnIL7m5JxlT0InyDdyzOAIcnyLlOqtCr1QOUfIxdAe049qqFWFCm1qnN8yKZOz5%2BQ5psDwObS7QlbivLgAGGedmgBhNYobbL&X-Amz-Signature=e2ece5bddaa2a6806cdb061bc2b6b4d40a14d19af526356141b523b8ca867341&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOWF75OI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQD769n8SW2nkyUADtbbOXXk5uzq9bTotdJsgb%2FvLRp99wIhAPRMwziBwepAef9fDLpOtuvxQquLyVvn8NKbdgM5faYmKv8DCHwQABoMNjM3NDIzMTgzODA1IgywjX8CMjb9%2BCB4ddYq3AMudgCA9y1H9tC53SQ%2FEgIpI53L9xLaUuPgqL7DyRpcZglUms7C6hxulrOKBcR86bQkc6jbDggvQmBWGphL7o8b0TzZvS1Irj2thItbE022mqqULL52ttXsqeLe11LlWv3DmotxOyerIqqySe3Kguy%2FsSkpQ2dTgim%2Fn5YoTR84ki6LTxbCgV7hnYqneZ7ymso7BM8cdgh0gbAAaBEyxkoMboXRnQ%2FC82BGRwt9qhJdays1XVkd1etq8gRXRyEoBVbPiurjohDbEnW1wfD9n5OD3Sw5%2FX1EIeBVon%2FfraBF%2BIFXtGS729D1LNDAqg1SQlmIeuc0vHvqCazkSzmwEW%2B2alb2Veb3JwAjs1ZaK%2BhIjkpatXXWPRDAWUyV40oCJgqbQdB6FfAV8oNWiQW0FO8jiTiPNmNu%2B4GYN0kXhQHzuGPmmRypMKaFruy1eEhSo0oWE%2BaenmL4DHLJH8ANMCZpUgGk30JjTbU3hdxfglZLXvf2vJHIuWD0ysarZoLQy6NvwTItSiBTaBUm%2FAEyIZvHxjZG8g5kKKEt8%2Bt5Slx%2FteYolBgPe1URm7uSbuyEc3gYpSN%2BRI06YL9FP4LgbSCC5ZLXRsjdoJl8UEDWWITZGVAsaQ9Dmj31jBgdzDDotZm9BjqkASAT46O673Ax81aSepjtY97XKFQC0x1wTm8II8umWmSEOxaAaBQDDoA%2Birk0XjrBVzo5NCOoBEIVYu%2FDhtUt2Yvvob6MwUAvpZnhOyWQ%2FFKKkoMjy9ja2yuFhTAJMLlqrO8yPNaRmlVSgIZvrtlmCPraCeFp497Gl5PqIYrBpoJ1%2B9ynhCSYZhglK4NUpufjQrNIFf9CAdjFqH9vHYa8liLaCLON&X-Amz-Signature=fc5da4a7747d5e00c13aedecd0d130f8fc90717f6175c0ad9f72c50b1602915c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOWF75OI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQD769n8SW2nkyUADtbbOXXk5uzq9bTotdJsgb%2FvLRp99wIhAPRMwziBwepAef9fDLpOtuvxQquLyVvn8NKbdgM5faYmKv8DCHwQABoMNjM3NDIzMTgzODA1IgywjX8CMjb9%2BCB4ddYq3AMudgCA9y1H9tC53SQ%2FEgIpI53L9xLaUuPgqL7DyRpcZglUms7C6hxulrOKBcR86bQkc6jbDggvQmBWGphL7o8b0TzZvS1Irj2thItbE022mqqULL52ttXsqeLe11LlWv3DmotxOyerIqqySe3Kguy%2FsSkpQ2dTgim%2Fn5YoTR84ki6LTxbCgV7hnYqneZ7ymso7BM8cdgh0gbAAaBEyxkoMboXRnQ%2FC82BGRwt9qhJdays1XVkd1etq8gRXRyEoBVbPiurjohDbEnW1wfD9n5OD3Sw5%2FX1EIeBVon%2FfraBF%2BIFXtGS729D1LNDAqg1SQlmIeuc0vHvqCazkSzmwEW%2B2alb2Veb3JwAjs1ZaK%2BhIjkpatXXWPRDAWUyV40oCJgqbQdB6FfAV8oNWiQW0FO8jiTiPNmNu%2B4GYN0kXhQHzuGPmmRypMKaFruy1eEhSo0oWE%2BaenmL4DHLJH8ANMCZpUgGk30JjTbU3hdxfglZLXvf2vJHIuWD0ysarZoLQy6NvwTItSiBTaBUm%2FAEyIZvHxjZG8g5kKKEt8%2Bt5Slx%2FteYolBgPe1URm7uSbuyEc3gYpSN%2BRI06YL9FP4LgbSCC5ZLXRsjdoJl8UEDWWITZGVAsaQ9Dmj31jBgdzDDotZm9BjqkASAT46O673Ax81aSepjtY97XKFQC0x1wTm8II8umWmSEOxaAaBQDDoA%2Birk0XjrBVzo5NCOoBEIVYu%2FDhtUt2Yvvob6MwUAvpZnhOyWQ%2FFKKkoMjy9ja2yuFhTAJMLlqrO8yPNaRmlVSgIZvrtlmCPraCeFp497Gl5PqIYrBpoJ1%2B9ynhCSYZhglK4NUpufjQrNIFf9CAdjFqH9vHYa8liLaCLON&X-Amz-Signature=70c8a12d28cb615e6a05e8add817d3afc7fba1c3a5822e58d9ca0c58342c6b2c&X-Amz-SignedHeaders=host&x-id=GetObject)
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