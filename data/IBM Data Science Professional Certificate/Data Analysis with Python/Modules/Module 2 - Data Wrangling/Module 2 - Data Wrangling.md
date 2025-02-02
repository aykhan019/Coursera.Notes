

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623HZNVWB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8edGRd4HMnyaWlxMimMWBr35xj1TTU8J6ue5lQGCdEAIgHbvgJkHlp7Pq2OPfIxqG7q2senD6rZqtG7nfANd16AIqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPY9mjPHN5h%2FYpSjnSrcAywkpPe1yTUfHdMFBQS4OORcUunPCXRNpnz7FulXf2a4gC0gkMwUc6CnnKA2%2FTCfS8l6M6u9cjD3NwBMS0J5ivazk9cZEZvcOxLv%2BYUZopYNyytMPPm%2FWy8a1JXBQjsp9jCtxZ%2BFvbzMJE58wvFhmAiTQhWD4IdK6GPaYh3jyvyBfgmSl78rC7eCfC66RBtCIsQMfJIeSXuX9BdpjIMr1PpMYvRCmi400V%2F3IyceLXmnmwBghYAELs8nnI3TvZ%2FOcOeiswnmQtip5%2B11agak5n1cx6LzNJznYnSgNRfgjhHSbG%2BFKO0u%2FZFOr7vte%2Bpoz1JgBze7G1pD7s%2FnGs4lJPM7cqvW%2F2gCKiNGZ1ZMYALsGpor5nUlSrhraqeCD6ugYx3hnfP4mY%2BSPV8Oh%2FT7jrhmQjlsDrpedogNo7AhTO93IunjWfWL6kXodrfjSNiQGRPBRMpNf1fGN%2FDGdh6HEGLvImcO3%2B6e1nb9BClafre5W%2FlLtedk98y6E7omNY%2FkuFSD%2FlcC4Zo9qD90I33%2B823Ttsx%2BaEZlQAW4KLr9CDcvuL3CuFVVysyTB5k5HZDsD6oV5CBTz5E1TOrd3tgu9CpepXYsQ%2B4ucKUL1IOa0H5Or7zVx4lqgJYio%2BiGMJLv%2FLwGOqUB9YizQIjhauhQeGllp2W4Rt5QYeYFoQMfpbayrqoIN3dcqkrl0c5CZWRhlkctPKeROm%2FyOImvOxROxN4keZn%2F%2BAeJXLVl%2B%2F63Nsatk3uMse92YblHXSOfpWiOgfHTmJKIF5%2B6%2FBd9PpEA2Eld31CnLrLxDgeSTeGZkR0FTPQK79ntOZ7vXeHAaFw%2Bf7Mggfrq2rI%2BujGR54nc2qkJUr8fpQXo7HM6&X-Amz-Signature=a8fd65d742cc7337cd602b8d367a2703e10f923e0766e409ef5b5cd2f57a4034&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ4NFOH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvMmnNLUDPjb8kUrjfTzIi8N1CmReC4hix3VnrXWjxhgIgGjRly8rou0S4KatdiFuwiAny5MaSmt828%2FKLPA91OyEqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC2udHogxL7XOvkYsCrcA%2FMZpJE6%2FEadUcyglB4c3uPayP8bgRIA8GftNlhNtSNziWrSzWixBJnazKP49ekYv1QuZmAEcYUwI8oR4M%2FalUmIwmFXbx3A3HOGfGnAnstu5XzG0PxZxFXYagyXhTGljc5P4jBvxmeSZMpad71SUNe1od6kHPbE8wzeEdcR2OE5pGbep2NguRIQUOG%2B%2FWSkQsBNFyvgZ74fqR0xZ%2BdKuZMdQqKWxybpguTRSNkZZsntM%2FuCwUyFj8TKmUHI363Xa2kMKq0uqxnKsCmuzU%2FPX%2FRoY5oWkcGUYSJ9pCVsViQ9l9yx1crguR2aSwFXCx1oqCel8MZaXadoi2fqX0D%2BxMX0NAxCJvnQxuLTYRgcBzoVcS8OghGJA7Kygbz9O8rjUtdostvq2WFqubBegKPoUaCqd%2BJUC1NqQL7HIoe4NnuvZfg6O%2FbHHpfj25SRbSctemsj2pV%2BxBslIcQc113BpWxdCZWwP7fGXJcqZuDG0v1Qf2AAri84Ub4naOP5DI%2BBSq%2BI2SUmgcfof%2FNcw1jERU%2BbTWOmzdGDXWM3DhtF1NTKRZn50UYAOT9y03808cPjqhPqYpuQalvy%2BftwXHg%2FYBPE6bzl5azy%2FwRuKokovDJE5Y5Bf%2FWlWggy2g%2F9MO2b%2FLwGOqUBnuOgNJhnT3NDSrsEvTnW2K259kxTwPJXoIoPw%2B6MuGvytmI4K6Z%2BSiCUs23G9%2F4RYQBkJYhuaZMPabuvLRuPQYQCVS8%2FFfQCCb8tyh0rUi7u%2BlyaRL5lwPnP%2BMNrmQsYIyQElWsuj5e3owRrO7z1lSvXl3bMbBKCJdQcuSATXGJ8DR6GOsiqm4ARsEkr54w1PNjIddwSR7RZVDQKiXTvRR4iV3s%2F&X-Amz-Signature=19872df9f6e6d4978c1f25c3a1a8893cdd9b1a2f408529659ece08dd2e91b332&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT3GR2TJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCp4jf80S9iM418eQ7L9S6TGwFEe02XwAN8nY6D1JUQcQIhAJNYum%2Bq4HABlmVTKqfkL70KqPspNpMF1FTodPco6rxyKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw43VfgfXXc0zLh7Nsq3AMZiQ0WIQzLOOQXkvB1bjafEEaPYi5cCTuPQIj458XInNyankjtecfj9AR7QGb99AWocIO%2FQN%2Fj%2BOnBwlmPmO2xGq9NRsh1vWHv9BNWAAwCS%2B7Es%2BDNVF7chll65uXbik0EWGcN2Vy96cK%2BB7SlEccX8lyzy%2BbHf1h8B6oWwy4QNd4RxdRMC%2FQMwmicmN7EKrRYTe6qiDqmmDfimBYhfMmxqK9Doy406q3R9uEF6f%2Fq3g%2FOfLJvnnGtPygVWEzkJnTHzP9%2Be4pvK%2FckJyYIqTo0T2X2GXWLJAjtFhv%2FPmQIxDrQMMpGvKhQpLcRHMrQu15qIygiONucOCxEyWiZ0nwn5MINrBkYdAVwHMMg6AXEignKcsDp8Pb3qXAIFRcfQQv47ZWbQcqGzVoKGr%2BIh6vovazaXd2W%2FdRkBhBCxBDrxnNe1wIhrewJOQN4F%2B81IEAqQOreDlhEGY%2FUbuQrrbLfcYxeB83rvsADFH5wlJ4oMUA0Qjt9lPZnnfX10W1zALJrCqkf6hJEf0fQoupYN3vXVjXBid3K%2FMFS4whg3QFWJWTfrWzAMU%2BU05RbDctd83A4gw%2Fi8BPOMqUuxHlJ1Da7SzV02WV3khzQFWKhLMd92hcYsWSJKGru%2Fb6sSDCXnPy8BjqkATgjikvjzncyz5PVZZzTzCEqnu5IHI2v4YORKLJ8XZ1HZXKsf9PDZv3B5gqzE7LQD9xl0cBQF6UX1LzuSc0wz5P2mleXTe1gf%2FktU%2FN3JOqWTp1YQHU%2BC2QxWtEj0hlwrMId7HTJqzzdkYcCxOi3onajNeoP15aa3%2BZx3pKF0QCOGVBfYF4XHdjBJg%2BHX2bE2CV2GU2StUrJyUFLAA3LmflshHqh&X-Amz-Signature=b2157262c92c6c4e730682b168b5ecc73bd1f23e5299efaadb7b7c7ac4c797c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBGISASY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGD7hn0XoVPko7baj5Ul183XwAubnpfaK%2FjM8YxB2wq%2BAiEA3pwLe%2FMZrKkjR%2F0ki%2FAdo3fKGAQCIgbXrB8mdJb6WhAqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnqwWqpW0CS54IrzSrcA%2F0VHrTRx%2FrlFBwSzfVFs7zSViD7ZiOThSd63pnal2ytExeI5%2FGEtGVrgQT%2FVem7E1pJ93mqWPWRnLENYGqP%2FX0s5uQH0i66Xo6jZdok7ifF%2BTF5n418l%2FRxj4Q%2FywgWJ5pLPDdylts5p8JBdnes5YHKpHVbBxZCXBR84nDVIFQfH7D9o79cLZgZRbl9hs7EGEg5J6WgJBKOVj0oiRJEP1%2F00rY%2FAgiRqcOXGDzbjmpNeoRZySWBeSLRzYmA9KfiSIO8SZkW9FdpQBYleHMcOmiXVhgIAZva1aA9SpxFAjHkrpLuL7UG2gPaVL36zVh2DLP8C2%2FQbk84N7UtNhi1%2Fi6MBt1VAIHzxWrtoavK4ILto2ZWbpOBPWnqLf2eATH3wPx%2BreecBkyeWgK%2BnGjpkuqQBCp1DRHsnN3HvApQ%2BR0EJqvqVPWW31hRbwZobqunHiUdCsRDI9ItzoBLvq4fPOkFJdurZCS%2BRIvn558EbAjPBEyQQBYZItsPI1C96hmjt0lluk9IW%2BYIeaOf7JHp6%2BdklbEfKYfh0S%2B89rVTo331hDSFgU0%2BvPgrbdLrkM4UDd3w8B2JWnjmYXsHclY1sXDBlCUczUOZ8Sv5Gs%2Bs8fjeVfXJYdrs7dPYHlKxMOKb%2FLwGOqUBBNps1RAHHToBMpj3kn4w2tudlJu9yXkxYGf6J7jr38IM0V65Om25bv9qotC8FIQH0eRtkdsgbUzynOSi%2F4f9WZ2qe9n1%2Fm289c%2B51RUljxQFTb214ljc%2BX7nE%2FN4Mwv0RJr8bd0hDe0S5zju%2BLbYgqX4WY29nugB0TDFpfuFHrszC%2BtbpJnV2LLkM2jY2yF3pAP4SQkJA2fQ4FndgXeH2hpE2ZOT&X-Amz-Signature=05d73998dc1cffe89164b33d419e22a22066a392ddd85b561fbdfea0383dbc2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB5Z6GDG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUx5Z1dRTbRI7%2Bgwbj3dx37Y%2FtYTDulWivbmKeKj7YlgIgCtfUSa%2F%2FkLVJ2jmm97NjMiQLE%2Frk7HucMMo6u2Qi5ZYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCfk2o2ql%2FG41eiSSrcA9OCajHrqPXJeta5NGCW8P3oKakcWOexbbQX5hzBR2lsnLTfFL7WOXW64yIW07vG%2F5o%2F%2FZE1HXqEfG8iHETexbkROdxSYu8wgbIuQGyPu4%2FsKAnJzc5OwbyvgNhki6rX9aahyjejLCZm%2FKTaGFhVcb7a8%2BOCITQ4slCW9Zngyft028Mn5ZlCNiZrWLOHh55B4KeIXOi3xPwbxzx7RYudJt7h8A7LwOSeLffnTZg0WBEPlRGi9mvUEI3IcgXmneMkLsm9luE1v%2Fg50yj9%2BK60e0K%2B71x1aoVG0vEG5w73y6jpRSJWSPHg4uluqH3Vv0bDAcM1OjTY5MzK0zER3ZvcIHDsOy6OVSOLqocTH%2BYdKcPBpBNMpuCb3lhEwmYmCDhryumDxuSn%2F8ma%2FQ4ezjaoKO7K2MRHEGvHJNx8ZYsMGPpQrQwMTcFVWWk%2Fj%2BolDn5gBXLP011YAMC0VAQE7h4lYT2eeH82oYjWlB4ZffjKazFNMUJLawDAVza1IT63GAB6wUZBT%2Bu4lyjIOp2j7%2F60%2FpxXsMkOxbNnXJDbtzTJsfc7r105i7BMyw1VExmkX5QFCf%2B4zvB5cPRBYimeiq826oUFK21yUzw02O4lhh%2BXUKiqhy5ngujaGES%2BOzEkMJSc%2FLwGOqUBJSUCsvgdTRsFb4cyH5eC3scNlhGL93FuvIeA6AiHpKg7lvYO8mX3eyX5JCMicBLvTrc4nWduOsPNdMRXxA5UpVE%2FVnmxEp%2BP2SOfIgS4kAy7CCSie%2BqnFE0K5GMg%2BixPDo16TeB%2FqnlisHP5wFPF3y%2Fpb9MYw8E87ojip4BXm%2FgynkVHA8Qao7zvz7zuyk2kWdfWhl%2FYv3v6zDITAHMhUWhmGsup&X-Amz-Signature=fafc469a407fe965f9d4f4920e8d384ffa067c22d8d506b7903ae0988f3e6edd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULUO2U75%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDIv%2ByVnA58xDluSi0acHLO13Gayy8%2F76b9aDgsx6PTQIhAN70%2BfVxRE8B2XVmI0gqARa5IXGdJL5mg7WKh80QkiVPKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHgD5wUr2ExKWjYmAq3AMRB4xGufnKMrBPi0w8hKXH7uh9bJHrDBtYksvR3y3r%2Far4ec%2Bi8rh4Car5ecmcseXJAuvA%2B52Ht%2Fn62Uzst61eDovgAXcOPKia0%2F4SR5ydabmzIWybbbkc7BXJ57em7apA2BL6S%2Bmj64nXVKKZmNpV19eaAPQlSlFxjbF11y1QG%2FfGbWnq9GtBKacoE6AYlKHBW7SUQQQno56XlDOLTkSFF6%2BITduKYXg4RbZVynlyqbxASooG7XkLPPvF710Ij8%2B%2BA3gfMDAoYkF8ryvbZ5a8KnJi%2FD%2BayMmankZCL8u84nmbSZKSscGdva%2BCQfG%2BWeT88ZjycJET16oXiQ2ROPyCWs8ull5xen9oHH6dypRS0L3cP2Hskbkt49x%2FqND9NghNnpe4lATEiagQs7azwRqlDvzfJQc%2BfIVvwYrZrKBIhJxYpm%2FIejyovzH%2Fw%2FzxfZ%2BJenOuepGDvfzN3AUOHnOY5vH9obizBz0vOnvzxNhquIRBaZTbugAgSdJ%2BqYY7wC9cLGy0XQnagnRMC8V15zpGPhDCIe0Z6OMjCNWPSz3l%2Forl83o9QOAjukRqsNx%2FNm%2BOfxV7%2F%2Fw3UJZKlQNnF5MsDwRSZOJvrDQDb48GDcZfwMHILc28s50icb3OczD3m%2Fy8BjqkAVfB8hUYys7fH9PtbaTLjHSdr8Pt%2F3i%2BaYDJwjVERkatHwuL9P5wuJrXXkKNKrQKd6vx3h7VDQfsKeXJi%2BFQtSYvkSiHzs4nifdPOGlnGWCaRYiLFI9cQiCbaRifKEBCBbNibrGF4DqvGJBWuQRCb7epmw5tV1CUcV%2FXf%2FRfoewIo3Br2fP%2BU8kzs%2FYFO8dyNF%2FPmwQzOkpgPe0um8QMwFRVvbzC&X-Amz-Signature=3f3e3951c1735bb45fc27c1cb48e232b3f28038bb7db1a2cc0085238835bb2a6&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GDPIJVA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG%2BbPFK30%2FLVVwA360RopfTE6qNBj3WttQ1C%2FAzsRcBvAiEAk63M6O2kiEr2RuYz5op3j1R2DQ6ZibK%2B43XV%2B2W6h6cqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPFtUpK%2FvlPaUqR0oCrcA9BvxB14wUbqHOpQYTdDQ21h18pSZzmNFf7F758f10o%2F25P8WI48NF3ai%2FMi2Vir0BFh9yokHt1ddSwfP25Ugv8JSgl15qlxyoT%2F9e6Bb6E5Pd%2FNcblPUJJRTL6OSlxYtH2G7fGodoeUdg7jIFG7ay043H2pb8Sw7M%2BjirKwBGsxBDFQGNEDOeEXrIWLREjWmHkVb%2Bma7t7hKbD0U3lmPaZMIAxxHgpG7aPx5QuW0Zo4coeb9K3Ro62pZTdDXnD1OVSrQKaKamc6EX3Kq8%2FAEJk4zgW%2Bnf9rpnsvIN3wCWzyAr8TRB3FJO7yWIKFxRwLAWF0rUXjq9W3A2k%2FXaUmgqdfNl1%2BZene%2BhRs2WMO6vjAJs%2FI8tPqryNcvmGX6rrxBc4%2F%2FrB20stPGVpI4et%2FdpYIM5mXpBaa%2B0kFtwv%2F9oymhIJmnLLNG6TJxBWPDojOs0%2BMwV1Yurw8L0L4y3v9v7axzQ3q4jZL7UIr1tY7LIhxnPubQ4K7dXeEjZbOvh8FbknEyM3aWGwetOsAYvVGXvyagQU1X%2ByLbgPrXlOn%2BsQybEZwOYppwDpRmzR5B5GwBH95P87O9cv0m1GzdpNSJ0jdMH7LSEWmBz4toaM9osnkKlJZQN8Uaw0l%2F2gWMOub%2FLwGOqUBx1D98lCOlkcqGUCDortWvPf5%2F4KS8j9C5jpRIBxiU1O0j28f%2B14ruOqXoEA%2B90TtBiSM1pM9JCNffqe2WVFEirgrgCiEwCKZUNyISscMAzl0hb7z8go%2FW%2BYgCO59QsyzRtEso4tCSDm0aLmPb0DFx0qxexN0thqrsJ0DZjhyfqxKSsQtFcXsh7LVfQ1sn6%2Fn3x1WTAgaYW2zMqCy7x3mx%2FMqMQQc&X-Amz-Signature=89f2776634bf84a0b5b5fc0a404c6cd2d7e927660e0303e853835d1748682120&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNYL5R3P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIqotl4uQmcLVbo7CqGcQDBr00n5FVxHE3%2BYPzm42LBAIhAN0JZvnRrDG03kfhtXgCeAOY9dOqP%2FYOVhWFqrCMktH6KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxrMbPEgzuA6Knj%2B0q3AP6vJNqQXh7P007pynrC322OrPu%2BiDN3aku%2FP6WCRJdULL1ZsgJsJf%2BYDw98eNNdp9HmtgC0o1WEmqMrLCbhKgv48NyU4jUolD3u4bsCB5Gx%2FWUcIvngOBeOUCn6CNkv9MqIw1KRO0%2FAtSvcByuSoTbZtm10WvUh%2FgRNyczH4JAuZMoYOuz77W9FC2%2BztMNakiJtmmi8geLniMGjNyPSJOTvucT6DD485OraGXpUv%2BrVM5%2BzJvbvNFXaFaMXCRC9KWansajl3HDeO2oWa4pZX%2Fz8uwKxZTmWGGA%2BXA5K%2FnmacUg5Z%2BSIC%2Fdfm0oNr9GYhnbUzEhNidOoUogeFT%2BH2q1WrbebAoJOCXWDmARuVVDE%2FnvP1na212yixMBjpmTmEyufNHkWcOJr9dFC6kfHSmLuAzUm5awj2sn4sktxgINdp%2F%2Bdp6Ggxs1viP2%2Br5%2BvlZkvwAW8IKQrliUxgsk3NDfQHkrBHRyXPMNhLwZcc1E2%2FOv%2FayL5w4WHNXW5ahRnDHgdE3wTEDgpP%2BcTiVFsbqMBi%2FLXdj3VRbG2b0OlWeXJ%2BcuiOWCyCCd1WW%2BRXH9byHjRHE1HAPqyDxnJHmJ0kcDIQWZLOSWPDd4BvyOfiAX%2FibTADOAx2OvPRFnLzCLnPy8BjqkASX8%2BEuJbSALzfao5Ta4JJ20HrdUDCZm9c%2BXYS8bzqPIH7fDsYlWDbTDiyc0Wc8C%2BwQOy2cd0abySXMjH7M1S7yqvVGVNd9HQM5X6rrReORCmMhDcQyQjfprBUuUaD%2FJAa23piTEUxDJN1ShL9Z4%2FiyKwayCOalRsn3Sk0hCYjigQX9Dj%2BnATEAWzewIrdXGqd%2BrIaQXxYFwUAJnI78N7LS8cDwM&X-Amz-Signature=189bba643fa341ac69ab98ae9153815f9b6798b30ad6fb956eb49ba2496ad995&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB5Z6GDG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUx5Z1dRTbRI7%2Bgwbj3dx37Y%2FtYTDulWivbmKeKj7YlgIgCtfUSa%2F%2FkLVJ2jmm97NjMiQLE%2Frk7HucMMo6u2Qi5ZYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCfk2o2ql%2FG41eiSSrcA9OCajHrqPXJeta5NGCW8P3oKakcWOexbbQX5hzBR2lsnLTfFL7WOXW64yIW07vG%2F5o%2F%2FZE1HXqEfG8iHETexbkROdxSYu8wgbIuQGyPu4%2FsKAnJzc5OwbyvgNhki6rX9aahyjejLCZm%2FKTaGFhVcb7a8%2BOCITQ4slCW9Zngyft028Mn5ZlCNiZrWLOHh55B4KeIXOi3xPwbxzx7RYudJt7h8A7LwOSeLffnTZg0WBEPlRGi9mvUEI3IcgXmneMkLsm9luE1v%2Fg50yj9%2BK60e0K%2B71x1aoVG0vEG5w73y6jpRSJWSPHg4uluqH3Vv0bDAcM1OjTY5MzK0zER3ZvcIHDsOy6OVSOLqocTH%2BYdKcPBpBNMpuCb3lhEwmYmCDhryumDxuSn%2F8ma%2FQ4ezjaoKO7K2MRHEGvHJNx8ZYsMGPpQrQwMTcFVWWk%2Fj%2BolDn5gBXLP011YAMC0VAQE7h4lYT2eeH82oYjWlB4ZffjKazFNMUJLawDAVza1IT63GAB6wUZBT%2Bu4lyjIOp2j7%2F60%2FpxXsMkOxbNnXJDbtzTJsfc7r105i7BMyw1VExmkX5QFCf%2B4zvB5cPRBYimeiq826oUFK21yUzw02O4lhh%2BXUKiqhy5ngujaGES%2BOzEkMJSc%2FLwGOqUBJSUCsvgdTRsFb4cyH5eC3scNlhGL93FuvIeA6AiHpKg7lvYO8mX3eyX5JCMicBLvTrc4nWduOsPNdMRXxA5UpVE%2FVnmxEp%2BP2SOfIgS4kAy7CCSie%2BqnFE0K5GMg%2BixPDo16TeB%2FqnlisHP5wFPF3y%2Fpb9MYw8E87ojip4BXm%2FgynkVHA8Qao7zvz7zuyk2kWdfWhl%2FYv3v6zDITAHMhUWhmGsup&X-Amz-Signature=aaa9688f327614a9857a655e2e4542afe2fd31ad26209b34a504fe46c690e9b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FH65D5M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBApePaxchLG3h5jlXNjYmUxlH59cUfiUL96x7dxCIByAiBCts7hB41d0SleG%2Feouco9FM6ArSQ3S6yWjcUo3b69MyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsiownGTwt9G14kHDKtwD%2B4blR2ZpljBPkThFI%2FZ%2FooeeWcssLW5Ix%2F4I5PB8sYk2M27nqdLonV%2FI8TfRRqxSDZDg4qc1SkfkjNY4Uuamme1P7VdpRrT7LvqZ6segvNJ%2BjA1sNfaBSX4VWJ0fj4zEeaOW1k3zivQ0rtaylqIMh59OeaxYu0B2UZQf2W2bTGa%2BHOC85m4CHnVnu4TM7OOu9nHylORLaPIjnCWJcS7YFvO7NqwXnmQjL2L0G2jZRFoDW1Ge%2BdnQUPVmjiFj1eaQafWZ6V0bufgWtg3DiId1PhXOViHNh5%2F6OEm%2FEDDKBlo8RaQ6cc0VohuKzItp6Lg2ioPmpOddyWBhHAtxfpbscybFoTvXnpZ8RA0dntbabnAYPTQ7dlF0SgjBP%2F3%2BgPzCzSNMV9H9KUT76v563KXAA4p5sBjw7AwkoH8yiqR8trJOY7a%2FIwfQNQTUYIhmTxxyLQmsSzW3jzWAajQ7%2B8AeYV%2FNZ8OhA75ldlEmv8M2%2F%2BfMp1oo8E7B4cFvVduv6A5ZcpmxhXhehmRlOFYxTyCkmJrQz0aoDNGHajxxlPe%2BY1Yvu4b%2Fyq8F8AEGq3L86YWdQH9gOmG%2BjIML3nFJj9IYnXYEmkYi9perj9HTg8O%2BCEv8WSYNECj7Nt0Vnbww2Jv8vAY6pgFJF10sqcMFjP3sx3lLMxp33XB73S5rLVzsSbYttCQD%2Fw9ZlFnTiqlPPIszdh5y2P%2BOzKJ2zAMGpy4jmuBmyWmkJlvPCJASvgc5cAsIHGggfeL%2Bqn1jB%2BI41kA2KoPDuqsR%2FHv%2FpRrLHuNIREd4ySlVDYZ%2BupaavGMAOYzFt1%2BFNpqD6uvAGBAT1VexQlW2Yw0vTClQ4zYsrRy%2BB3TPegQntj51w%2Bfu&X-Amz-Signature=e979e5d434c5eda6cb8355e40b8c3701d5e39903d4aa339ad09006870e2fd426&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FH65D5M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBApePaxchLG3h5jlXNjYmUxlH59cUfiUL96x7dxCIByAiBCts7hB41d0SleG%2Feouco9FM6ArSQ3S6yWjcUo3b69MyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsiownGTwt9G14kHDKtwD%2B4blR2ZpljBPkThFI%2FZ%2FooeeWcssLW5Ix%2F4I5PB8sYk2M27nqdLonV%2FI8TfRRqxSDZDg4qc1SkfkjNY4Uuamme1P7VdpRrT7LvqZ6segvNJ%2BjA1sNfaBSX4VWJ0fj4zEeaOW1k3zivQ0rtaylqIMh59OeaxYu0B2UZQf2W2bTGa%2BHOC85m4CHnVnu4TM7OOu9nHylORLaPIjnCWJcS7YFvO7NqwXnmQjL2L0G2jZRFoDW1Ge%2BdnQUPVmjiFj1eaQafWZ6V0bufgWtg3DiId1PhXOViHNh5%2F6OEm%2FEDDKBlo8RaQ6cc0VohuKzItp6Lg2ioPmpOddyWBhHAtxfpbscybFoTvXnpZ8RA0dntbabnAYPTQ7dlF0SgjBP%2F3%2BgPzCzSNMV9H9KUT76v563KXAA4p5sBjw7AwkoH8yiqR8trJOY7a%2FIwfQNQTUYIhmTxxyLQmsSzW3jzWAajQ7%2B8AeYV%2FNZ8OhA75ldlEmv8M2%2F%2BfMp1oo8E7B4cFvVduv6A5ZcpmxhXhehmRlOFYxTyCkmJrQz0aoDNGHajxxlPe%2BY1Yvu4b%2Fyq8F8AEGq3L86YWdQH9gOmG%2BjIML3nFJj9IYnXYEmkYi9perj9HTg8O%2BCEv8WSYNECj7Nt0Vnbww2Jv8vAY6pgFJF10sqcMFjP3sx3lLMxp33XB73S5rLVzsSbYttCQD%2Fw9ZlFnTiqlPPIszdh5y2P%2BOzKJ2zAMGpy4jmuBmyWmkJlvPCJASvgc5cAsIHGggfeL%2Bqn1jB%2BI41kA2KoPDuqsR%2FHv%2FpRrLHuNIREd4ySlVDYZ%2BupaavGMAOYzFt1%2BFNpqD6uvAGBAT1VexQlW2Yw0vTClQ4zYsrRy%2BB3TPegQntj51w%2Bfu&X-Amz-Signature=d27f22f494694a7ca1e8ed9ccbc82fdcb29d172d8b56b54011836900f61b36ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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