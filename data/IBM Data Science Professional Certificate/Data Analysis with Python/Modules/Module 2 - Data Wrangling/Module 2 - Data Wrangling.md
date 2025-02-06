

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q527RXKQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCwfntQT7cMul6aGpTmCxd4lb9tYwwVf%2FWko4RBxbZ3TgIhANV8%2BEoDj5dftRuxBpJsnvw88Z3%2BXU4%2FW74baQs%2BQzKbKv8DCFEQABoMNjM3NDIzMTgzODA1IgxARPmGytq0gh%2BuM8Qq3AMZjlFOYSsN5Nm390LauoxlyD3SAW1byGxKyAfVLFPQNMRAJW2IUX6BL5lS0M30I%2FY%2B3EPFmtNKrT7mP3MukE3LcJHLW8KDwNNzNL%2F3DEFfsUYpXv91GDh%2FScGuN2qGk9WfH78jiwDof1Ucb9NTIR26rNm392F2iLmY%2FUtrBpZX1SmP88q8xeTQ3cgEGEzTYf00fTxWj0TCa0rqB5y%2FXK%2BCBq23sAL13msdfZIOfRgbXoSuxGVYw3vdgs3Qhj6cRoE49F%2BTw0WmpOFOf0VxFR7u8ia%2BF%2F3syK4On78Uo9dT4Jdc%2FlsCbttoWDCvJ9Lm3RBW%2FY98gjeo0GiKcyNthJY45lwzPZGpsb1BjarI%2FM4BDjLBrNPKzvP5lYzVsugcUTLM%2FubPCThCMj3Q%2Bwozh%2FuY9IcEhOeCHoBmf77LjG6aMNL0KTtcZdl7rLt4MOQQ3ZtJLQ6Q2fir4pZjO8SHmqCNd%2BSQvX5CPKYzAsxMzxyN62lHjc5XnJfwQifyGcChL%2F7AI6Toe%2BxXwkB3z9Pfmywz6eNcr1RTDWGZOXO8tkrwidJJpGMmO1CGQSOPulcf%2Bka9BD5uwMQslOAzY5Vf2uaJ4Y1WjNEMHLzWVfOIDlMlPaQfi9%2FnhfX%2FxHxv1zCX64%2B9BjqkAfNXiPGlqyqaG6wKoX0q966Yoaf5iLKjlFFfIuY8ckPw0ndwC0p7ZHzl9ed13Fxe96%2BwARX5bz9DTrYeDh6YFadLPI2sNDa%2BDHVqg5aUpUJDCL%2Bnpu1heC9ppxXajKehiEDeQEh4WAzO%2Fm6vornTa43YUpuCJ%2BsZBDZtYwoXMNRzrEVAVnd2fZ15u7mTpCum1mWpaFndKa7%2BSCZqqkqaXlo67jmJ&X-Amz-Signature=e803df23a454e5d91e629da7482d330651c1a90dffa41c7d937db07cbdc2fdba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUV55PCC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBNrGtgMJM90Ta1Jos4H38z4gSbbQZA1g5rzg3rz8pHRAiEAmCz9q9iIoCXm18ZGQl5nkD5TO62QXf6p3YtbLmnVixYq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDOApCb2JvjEkM%2FEXlCrcA8e6D8MlpEeQtTgZw9WDDygoSgWjB83tDYC0EuTEJbiYBGpqDf%2F1%2BKr0NQeIych16pqX4sbsh4Xgwr9qyhmxhgQAyRtGKW3kR2heJ8qBCAPZSqtTcwpU82WCRGsXz5gn%2BZAHO%2B4976elTycyKoeTs7Zb7CFrDRRK3y%2BPtAu%2F3X1YiQvCdJzuopUXZMW7uiYkMg6OOcNkZ%2FViGAQZvjGZ7aJRY5U0RRoVICXHquzV3SXa6tLlmaffzcTfy4XNkLLW%2FJVzQJMZLgMp0eC%2FhAVhZqPZfJy6xojmBS6vL3wftp9comJqYahd%2Ftw8Vcj7ziz8lJKKTEAyeplZyiu0Cv74kguiB0k6c9ERGdF8l1zaHM85EA6ymKYrfIZpFxkWVLBLp7PIxjf0SW3iiwvo4Gk%2BB2AxfwfKLKMFJX6cpMmbCOo8yl1BmjQwz0J%2FXri%2BqTACXV8KBoQEYgJrDR1g5N0ePrEnpbcW0Nt5c%2FZ2WG1WF%2BR1kQP0iacZ9UQWxT7oV7afSsq7NqNO2xzXd82oBnLCC5t%2BDEGzP37r4iECmKIfmJB2haTSafxN79o%2BJiDmnESa3GgWj04qVEZuJDY7eKJ%2BWZRt9QHeq9pMo07TR8Qo7%2BlUVqq4depDCnyQI78PMMnqj70GOqUBuGxPM540pc7rr%2FgzqB8dgquRaoFEoL%2BVaRiAHFr2WTg1oyKMWdRVfNXyIsEq9rYrJ56tAMUVBs2ALXhuy0D%2BU8yoxkhhExRmQ3gsKpMYicAgo0wErN6t6I%2BcU%2FMknsPPwFru9KgmiPyqS7nN%2F7pG1eWT8sQfcjx%2Fwe9fsLtdqyWZUWQl8qkI%2BoAiWnUAj4bdUpnD0JF6u6ZrMyYeRTokB6INQB3M&X-Amz-Signature=c99edce953b4b913f9777a5883be1600d3db96cabed5d8969e298de3e66e5b91&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7GNTNQD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCt62RHAKy%2BeYwR93s04BMHWe2xOh0Cf8%2BSSvPolOUM5gIhAKABdQZd%2FxuPKtpNzTGpCuYHQWyzm1TkyINQrgs1I5tSKv8DCFEQABoMNjM3NDIzMTgzODA1IgxsiWO%2BRlZNuUMbk4Mq3ANL%2B7YS0dUws1Kw3kpQ1q5MgKv%2BIlTK06w6gclw8jL%2BToljr3ZgBA0L9AFUAPjES8b3W4mwoe3BQg4Hhoee55IJFmqUdmYkybmIhs0dJq276QOShT1bPziA1SqdWfUoI%2BgEqt1XshebzS4znOSJjxABPHEClQql9VgqvpV3Cl5BSXn0%2BNbqXE7BvQbiMutqQ9xtDj8ZoHQk%2BLbLvcbyh8T5TixFX8YJ2xVg4y86QoUW%2Bix9B%2Fp%2FjTrBuxBRBlkU5cPmsI6vYKiLa630EfGsyKyRovMMgraHgcviEa125DQZVsIpt3SDXYI7jxr6%2B79mkP7PT6rduAejYOXFTiXgXXBeGGgwYWk27oB2wTBOBT9%2Fyc2TSdinEjbmXLmCl2UAwv2DJv1McvqiZRpkX7hKnQaKNhPx4b9EU7r7wz7gzk%2BNnOzHWnWZIYHJOjWhSUZ3qkoSFZyanrBBN6jL%2FRmpzKBw0I0GrDB47jj21MuPuSBc7DMDU4PMI%2FUt0jZIvLja1WoNwKljCyMKZ8bRxyj4IhkArXi1k0%2B4w21uXyOLWOmb%2FTw8Clr5vSZVr2Wvdi8N5fizvlFnws0wodu1yEOXxdadQyNflcIQ5IINHMn05aj%2Bpl0lf3sCFVCbkT54%2FjCV64%2B9BjqkATuwzr9uEWam%2ByXOjjLYqcYk8R00fcNABbeWGYYgwxLE2%2FD6wkK1QDO7KvviwZ3aoFpkcv9nXZV66EmRBzmc%2B89Cpgj5VXPNgQ2KXVREvdEGXj1wS9FSD%2BMQBDzcV%2F91W3nKOySyEKqAJl7IGg5sXQV5XwI9DIDaFwHpF6KH6b9aupG7l2lJrY5TgaRLVRANcT5DskXnCUT72y1S39%2BzuqY5yOTY&X-Amz-Signature=16939f370ce70e464485c1623be98831d702549fcdc28b9469701cb4b5a8a2a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMWGM46F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDiDgOKCyzcscEWPwTCCrC4qP1YwufqmoQfHDzw8E6OOQIhAMgWzcX2urQ283zSTkyhXMV9k7On4pt%2F70%2FpVf%2BA5Y2wKv8DCFEQABoMNjM3NDIzMTgzODA1IgwxLfFTfkQC5OGsS5Eq3AO3tpkubGvMHOHPPPCCzQl75c%2Bpg%2Fr9YkVajmk%2BFH1u1pdqLuDLnG1uZXzL148FSOmB2EKwrSQicgpoVRi3FhTY9DvaQhAfhr1H6JCdPhvTH0mMMzmUGqMJMQ4yVyVV1w%2BvwPmSb7xTe%2B7AGgaGCB3BOcby3w82OthxAMNCJjXLSuCduazLGqflPq4GcEP60A4t7Yj5DaCyqw50Zsq%2BT15CU%2BFgQzsAdM2lxMrk5ypWf5xcMKN%2FEhDFH02Y3%2BHXbBGAL4WZ1ErijecjYDclq3XI8lMpKEqGOJpTH7ThGatpPCwRhVZoBqHnjVo5HyLTcJp68O5RWZBcTGpZ6DVVLw4htuNJ%2BlM3o9r1B2NVyMb45JtfxhaYuA596RYz2HiCX4wycgyUd8P19RO1PTt2I4OOofMVufJSZlrjzWWTWpkVVAZrQmwoDWCk%2BnLLyoirv8fvsy%2Fmz62GMUr1ZE8a4RiDdXn42kGaMjme3S%2F8B0nPFHCHb14W%2BG9kZKECYPfLIu6cEQrA2RmfTWvBzDcP7Ub%2FJjT9tZdSzl%2BauaAeFRqoTLvkXnRApRrjQYpmdiQ60DY8oXBkFjPXGiAb4AKSA%2BvNLG7ktJjdtLYvxaY9GcC1l%2BG6IQeiD%2BXjE06ddDCV64%2B9BjqkAZjgOxbvuXJtvFeN5kVixYuZA%2FDNXO9IfeWaIlk99qiJPZXerSziQ02IqDjfMqRlqwfwUUlinjkHO%2BNPl2SR4xpPE%2B3zqxJFa1qTBybf%2ByAHOEq%2BwAiDHpadkiTUqQNRNto4bzyuOkyF1sfVVkFupOdBsBw%2FC1ppb3qKayRhD1FhwITI2%2FR4Yn2T5iqnJnGaYdGrF3o%2Fv64X2L9zJWdvIE72iiIm&X-Amz-Signature=a486c38840de0fdb6195e80b506ce65e52cc8ed7613b774d78e054a9682399eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBAVSDB5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIE9i%2BfN1kfERWQkcNO6jPxAh3zxFp%2BnCF4U8ekpbQ7a9AiADqiVhS8mp8i1wr8%2BTEHUsLnzALBrCreSF9cvCx%2B1FDyr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMS3u7bA2JsOCBL%2FmUKtwDei5soeR%2BowDw2Mc2OEmsHHEIwnyTodaZ67ltKuIb7yjOeIKb7AHR2qpPXEuKBzfDK1F3fP0u3Q0W2V62Fa%2BN1OW%2B94t7kdc%2BuV0xZPlpyhApUzyLMygaOdifi5upg%2BZsHHGdQNIn750h%2ByB9LaUhecZzT9RnbCn%2BEznPuNZplgZQPrxGv2rDrE8gvycJHWVVanhdf5bYzwty4SD7XD%2BZjypyVLbSh7h7K86laaBXAFvoSaFk4Z5GNLgaMOGKZiUJCLpu6dqYL%2BpDDp2vm5GXLQ%2Fpd5J%2BiAb8WBHhLu4Ya3sm1ysFIoOAUy4%2BnUYy3ZS%2BR%2FgcIWF1lx7VK50WZ77O8z5gYJMb3t%2B6es37SaUB85Qae0J98OHTojaEEZxlRltlj8pUcDjPJgHl1E13RkAUTzo1sFnM1ns%2B0nMJO4Pz0Cs%2BPEycyoFDwMYZJ64mpg9tDKUGe0USuIaJpMkbzzY%2BfF8x2TeAvapaQhfRMQS41MLyxbptkMh9L8e7xmu3MCXqfw4QEsuCAI7RnAthYFS6AdJLyjZbFTv3uGTHfwrmUYpcTKsVZBwEvmKGOhr1DFAtucsiVRyQVFEb4EDq6x%2BbkkMyo3EE4ckjs6UL1dwYQYkhaL%2F%2F83vAK2R9%2FMEw1uqPvQY6pgE0%2B%2BYMo7mwhStjLbfbhHY0tksqg2JUod0a0tkcVHejOtRQAyPGgSp6nbrT41NruscgqAzUoj1m7NAV0%2B6NKxTnvAyZcZm2yUnpo4TFsQnceVUoVbPs0aMjjl%2Bgkvt%2BqYc47SUXSLCBYQejBLabiTRKLo6AzxJtQfNSsoKLwIDeofFt4RFQ2YuXo8ECEF0yVLWGZ6Q532QLdAaha%2FDWHDpaaUoKu7Bm&X-Amz-Signature=4f980db1986a6923a86650c3c30ab1f6a0cc18d23f42b8f5c4980d45e9ba1e78&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5ARXG2P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIBEGOowiTI4tM%2BQITkoCDMOH45XTawBnt9jCdHM0%2BXoYAiA0U2gt9I5QR%2FIYSWeMoucoHpyT3TI4KGZ1%2FK9tMzdSvSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIM0PobqHCfZutqLqxeKtwDOjW%2FgDBKTFZP7o%2Bu0oGP5cWmt%2BompbGvRmJYxIMaow9r%2Fy%2Fo6dRPx8i6L%2BOe0QyuPhNEnA%2Fn5qKX4PWWRxDTZmPraZYAsWLY6EfB1XP9FjpESS2y18YLHKWjkIdDhRHIn56tPNf8HvFDaCqyhkEZntIVk97RqsGLGzh%2FOoz7rsnCJNpPOj5oge%2B1IvXG8XY9%2BcM%2FKKkJCxM170cLJ7qGySHTT6JFGUK%2B74Wzs01cC0DlrXrZSuxXThfWGZO8tmTRSGsCsp2OQMwmleixINSfCEAFrwjuEUfzyLhCbAlzq%2BlImIys4uzE6UG43%2FKiF0pb1FFhEyE%2F2HpYmAK5x640DXyCd5U0XHMsOgC%2FlbnCAJnpJHN3NgWnbztsg2dVrg5%2Fc4evVM1xWnOAhVWPy9fTXPzwBIWE10mcnAq4Qe3bWUTEIZq1q2pL0WeCrnMj9IOqgA%2FQFSKwG26K%2BGoO4s%2FuOGHDftwPsjvJ06g%2BoCfBnlRxEUJLLaO6pwT2U81PLc0a%2Bn1V5kpNr708Al3Y2fiCLCLeDc1jjw0tIgZmfoHmZaOq4hDAmO9WuL4eymOHbcoYiRzH5l4kPR7NMVsqkygCrCWC2muCJegQX6ID5H4n3F0CmwYcgyIY9DbpPU0w8uqPvQY6pgG2tlLk8mTc25XZeMkeeTcCd%2B0qzB7F12L0L1swChNV3m9Wmm5xJvlSZmTO2lbEw%2BLlTi5W3BFS4qUZyFhWVdwgoG9JDn5GFKEUWdnj%2BqEeCqXNNo7Mukoun11pqXp5lnoUMfkvFipyujoGeq89BeibpZTlayvPZP4NgUVpgSS2DmC3NWOgO8vzC7%2F6ZcF2Nr%2FC83f2eyWfKfOTIh3BfvSBZPILmhoJ&X-Amz-Signature=7df0798cca658dfa9c58a0344dfd8748c263a54b9558576cc1398fec3f05aa83&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URKSF56C%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF0J7r2g8TIFULK74aVn%2BK3QIbAtLaLruSTXoE%2BrGPXNAiB25PKuGgvRtZzrKMKTjcm5s%2B%2B4VEelqo3iFiGG7%2FGGDir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMwe0nMC5FVzEqIkncKtwD%2BN5Ik5TNz1f%2F6s6vTtE3kOebp3G8p7FHC%2F%2Frjr2Zx3r6VsKY4UC%2BZpoC2YPGD7O443eAuxsPy4ECGJm20zdLs2Wroa%2BBuz%2BnDY04L9qUdPZVnk1jwqrDmGnDT5Hant%2FM4cg%2FgeqY8GKoPzaYPAnAXw1%2FT8Y7YclO21cQi0lDvg30PvwWn7yrWw%2FJ5W4%2BKJx9ipKoTY8kRoSQDut9pcixP6zX%2FCm%2B%2F7ghoV9znq3hfAcp9%2FTWyC%2FdumJP6ekbD3ucGjLj0FDv9b6Wf0SplHnOS%2BnvEkXRWFeSZkK6RpsiV5qAqcjNpdTfkmT7Nxyjg8IYNcAIEAi098Fn5XgIl8G8ONNDjOKTYnlyeKfF7%2BSSdJ0yAj9a0NpTtFZEQAWL3ZDVqV1r3ToI1pibAefyXZ4BqOIPx%2Fnm8n9k14Q67SLHy3K6QG7DBTJQXtyrJSbT6OyBtWByRNWy01oviN%2BJTMJWIh2iE4doTAWoy0LYT9i6kOfny6Vu9Nb7sbrNcW88k7tojUPIOa%2FibK%2FMRLNNBuOHlA6zVOfQRZpqfNfKKe9EfysjWsHxAt%2B%2BfdJUnaL5%2BU1fQJ5uO0vAz6IX%2BlP7XE1nW%2BYNW4awrp8gknp%2BcLXFPzA5Dr28FbiXjuWQIQgw2%2BqPvQY6pgGCIvdV5Z4w47m4%2FzK7PDj3ktDiLvIzwYmedW83AxINhCaak%2Bc9%2FwvlNpJAufV995fcuBxH46g2yjJmeJAAW%2FUmE6pWsJs46zD0TZJ0OkXoGEYKRei5Dq9uCwD5gKZeOSi7%2FTysn6NrW8Ek1%2Bb6IjUt56LKx3yD9wGF4LZuJK5xtvepUuPNgULGXyIgSA02B5Za21akRLHzL%2BCAezXrcZA%2Fhzo5orwq&X-Amz-Signature=76f0f539187401e1d4fd66477ddd3c1bfffc9c6945ae86c29543dc1e44f8a418&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ACPAR6B%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDrVUacOU40Bq2IT8rf9uGcScYZnKoFcsb2UWtFYszWlAiB7pILu1njJ3Shk3Gc6gvaG%2BSwlM8O8zpp45TLJRFFdSir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMdEf32RqgYTm1aCcyKtwDljgB0Bcb8d4%2FO%2BFdJq8cbY6C%2BK6KaYMKMidlkgPzm0zs1hE%2FZWezfXiZtdgLZewCX49AsqnfVfFZkZO1XLr0Zr3LW0YvaAgENk2FVWcbQHxNdkBqhGrQlbsCa3liT%2FMN%2BPJzM05OFxvFzhVTcko03odYO0orw83wKNXo76X%2BjR4hDEwJYQV%2FlDKDRW%2F5nVZcZsXWM5%2FmWImzHiBXWAq%2F4Br21LlcJx6ErT2zExbGLl%2Fm7oGoFwebVKSc0Tm7TvPABY0pJGdtrQUHtY7OElIyMqkF81F26T4YwPQyzTONHo59%2FrAl3s2GFOIxMNaiIvIWVUViGeEQ4R4YNVSU7bbOw1WUYdMQtiIFGltYNDjBPfhjn5q7y2gRO48BNWvhPZuv%2B1%2FuAstrLRkKk7cNuPNTRdOiflDbZ1M2l7uaD53Vr5Lh5%2FvbSAO1g1CBsc56rJ3jZLQYha9viYGkYf70WtKYXwCGpInNbB46qfI5UDHlQmZ%2FZ75GdJYMDpIo5lMUo6pg7dJkWSJ3pKuD1JjjUw8GI4VFF1IKPCvr%2FYr6WZ8iX4Nf1a6g73%2FBzvL0GcAf%2B1DN7xR9mJ1tGutVL3S6W48dMTnGg%2BMr8qEcY7NXZT1RLoOQVrZrsz4CYBVC%2FLsw%2FOqPvQY6pgHfOU2dmYchoAhM14PjL3L2AvDrEZipPheqf4TTBPpfDkhknVjrcdNGs0qKxbbjFabcr4QwuAK%2FYiZWGdb%2BFmyVtr2ZCQKJGRcLhc6gv1BSr9ci1MWZBqSwp20S4hcqieEBB31PJqBq5X6wu1N44XXwXphXzaQTny8YjySQSSgzlLZfHTNktPSTABoDBr27beXv%2Bmybjb1%2FSbXGC7f3vZHwTRVMSfvg&X-Amz-Signature=708ef9f2eb28f606b1f004d9e1f56cb5a1fa8f6ec7ac456c2ca8ef0fb42e9f51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBAVSDB5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIE9i%2BfN1kfERWQkcNO6jPxAh3zxFp%2BnCF4U8ekpbQ7a9AiADqiVhS8mp8i1wr8%2BTEHUsLnzALBrCreSF9cvCx%2B1FDyr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMS3u7bA2JsOCBL%2FmUKtwDei5soeR%2BowDw2Mc2OEmsHHEIwnyTodaZ67ltKuIb7yjOeIKb7AHR2qpPXEuKBzfDK1F3fP0u3Q0W2V62Fa%2BN1OW%2B94t7kdc%2BuV0xZPlpyhApUzyLMygaOdifi5upg%2BZsHHGdQNIn750h%2ByB9LaUhecZzT9RnbCn%2BEznPuNZplgZQPrxGv2rDrE8gvycJHWVVanhdf5bYzwty4SD7XD%2BZjypyVLbSh7h7K86laaBXAFvoSaFk4Z5GNLgaMOGKZiUJCLpu6dqYL%2BpDDp2vm5GXLQ%2Fpd5J%2BiAb8WBHhLu4Ya3sm1ysFIoOAUy4%2BnUYy3ZS%2BR%2FgcIWF1lx7VK50WZ77O8z5gYJMb3t%2B6es37SaUB85Qae0J98OHTojaEEZxlRltlj8pUcDjPJgHl1E13RkAUTzo1sFnM1ns%2B0nMJO4Pz0Cs%2BPEycyoFDwMYZJ64mpg9tDKUGe0USuIaJpMkbzzY%2BfF8x2TeAvapaQhfRMQS41MLyxbptkMh9L8e7xmu3MCXqfw4QEsuCAI7RnAthYFS6AdJLyjZbFTv3uGTHfwrmUYpcTKsVZBwEvmKGOhr1DFAtucsiVRyQVFEb4EDq6x%2BbkkMyo3EE4ckjs6UL1dwYQYkhaL%2F%2F83vAK2R9%2FMEw1uqPvQY6pgE0%2B%2BYMo7mwhStjLbfbhHY0tksqg2JUod0a0tkcVHejOtRQAyPGgSp6nbrT41NruscgqAzUoj1m7NAV0%2B6NKxTnvAyZcZm2yUnpo4TFsQnceVUoVbPs0aMjjl%2Bgkvt%2BqYc47SUXSLCBYQejBLabiTRKLo6AzxJtQfNSsoKLwIDeofFt4RFQ2YuXo8ECEF0yVLWGZ6Q532QLdAaha%2FDWHDpaaUoKu7Bm&X-Amz-Signature=253b3e6388404b0f1e4af613a7a0550dd57765022e1e1c25d4989e471e251937&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RILND53E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIGlsdC8FOftwpjGpjXqNuMALL0s9BvMcQr16sZSb6kuQAiAPAGHpfh%2BgsiHYDTNyYCadGjLQ1KcvvA%2BUH02xex77tSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMrfeHpkdwY9VipAvpKtwDEeu8OPmHUAOc5O7%2FH07wQf%2B9%2BKW8UsVluF7b1qFLp40VF2p5hFBTCGHmZZ15ihjob1z5Qky0zayC35Lce0MFrDFmjWGR1rVrwChfAwjKvWe6eX69OgDpGchqBM0q4bapPdUg%2Bb8RULwGILoiv8PDF21obT0FKbcKp%2BvSE8U9sJvZ5NQ9nJ%2FKIUJB2BpCJA2WgEYnHlgYPZ9uyECo3a6Ue2a5T42oVNI%2BYy7kIm4Ru%2BEm3Tyjh21l%2FbI8OcR58iBXapx%2FSxQnI0JHke0Ij5zpkU7ctM4QuOlZ0kBZZU75o3D5OKRdgoI3B%2FwlNlyyp%2BCbTtuUOc3V%2Bkg%2B9H9culOZCA%2BFP%2F%2Blz25pm7lykvCVi5PyGGw440%2B0ks8fhViGZNwrgqSPxZnUbk4nt%2FD6Lby3UB5GMFlCdN%2BSECoF8%2B8OGWb%2B7ieH3GNKllpL84p8Qfl8T6StgWNv4okaGHqbDennxg4oXyPKWZgt4Wikq8cwvIUJk1qrvPkj57ygUtoMjF9QHg0Pxi%2FkCxUdqzZsD0Sn5uJ9%2BBG8WhLPBkARcPwSIsWJbn5TqmQeJDWK5lDAhaueGLYNUZoTk4FbQCkM3Ul%2FIG4WHmLgZsKv1KGAgOC1lKQ8j%2FH%2BGZHKP93HAFIwvuqPvQY6pgFnDlltqBWOQ%2FE1KX6WLC0wMRHQQ77l0i3OipjNHxSDR4pemu7mwSRCUMz4rs6grliWXJxcmIZmyCCFh24fY56bxczGEG1bLSQm2onZrQdegd7ewrrsfsf%2BTd94ihDpC1V%2B0KfppZUig0NFzbJDW3MOImDoyQTWYoEeCGsSgN%2F42sQOJpsaY8EP8wQuovTqlnwTOWJ9WqRmVW%2F%2BMVsAgTyYgZ0FuNGw&X-Amz-Signature=a9786d002cec747a5188acd41dc985ef206b1069f9807984949b9e0b42cc24ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RILND53E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIGlsdC8FOftwpjGpjXqNuMALL0s9BvMcQr16sZSb6kuQAiAPAGHpfh%2BgsiHYDTNyYCadGjLQ1KcvvA%2BUH02xex77tSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMrfeHpkdwY9VipAvpKtwDEeu8OPmHUAOc5O7%2FH07wQf%2B9%2BKW8UsVluF7b1qFLp40VF2p5hFBTCGHmZZ15ihjob1z5Qky0zayC35Lce0MFrDFmjWGR1rVrwChfAwjKvWe6eX69OgDpGchqBM0q4bapPdUg%2Bb8RULwGILoiv8PDF21obT0FKbcKp%2BvSE8U9sJvZ5NQ9nJ%2FKIUJB2BpCJA2WgEYnHlgYPZ9uyECo3a6Ue2a5T42oVNI%2BYy7kIm4Ru%2BEm3Tyjh21l%2FbI8OcR58iBXapx%2FSxQnI0JHke0Ij5zpkU7ctM4QuOlZ0kBZZU75o3D5OKRdgoI3B%2FwlNlyyp%2BCbTtuUOc3V%2Bkg%2B9H9culOZCA%2BFP%2F%2Blz25pm7lykvCVi5PyGGw440%2B0ks8fhViGZNwrgqSPxZnUbk4nt%2FD6Lby3UB5GMFlCdN%2BSECoF8%2B8OGWb%2B7ieH3GNKllpL84p8Qfl8T6StgWNv4okaGHqbDennxg4oXyPKWZgt4Wikq8cwvIUJk1qrvPkj57ygUtoMjF9QHg0Pxi%2FkCxUdqzZsD0Sn5uJ9%2BBG8WhLPBkARcPwSIsWJbn5TqmQeJDWK5lDAhaueGLYNUZoTk4FbQCkM3Ul%2FIG4WHmLgZsKv1KGAgOC1lKQ8j%2FH%2BGZHKP93HAFIwvuqPvQY6pgFnDlltqBWOQ%2FE1KX6WLC0wMRHQQ77l0i3OipjNHxSDR4pemu7mwSRCUMz4rs6grliWXJxcmIZmyCCFh24fY56bxczGEG1bLSQm2onZrQdegd7ewrrsfsf%2BTd94ihDpC1V%2B0KfppZUig0NFzbJDW3MOImDoyQTWYoEeCGsSgN%2F42sQOJpsaY8EP8wQuovTqlnwTOWJ9WqRmVW%2F%2BMVsAgTyYgZ0FuNGw&X-Amz-Signature=a51b1967e2d723362259c4d7dcbd7f25b630dcaaeb5ceac3193471c798e877e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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