

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZM6HQJEB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEBDfP%2FT3oUxODU%2FMInOjF8%2Fv1rGZWeCxBd92W%2F202XgIhAJSN68zsOoHfOcEQgaJhDc%2FgaMp2P4iAukko9vK1mp6OKv8DCBcQABoMNjM3NDIzMTgzODA1Igw8IwasDp9lCUkgdfkq3ANvnhh0uaP2bHOcuv12g8EMfKefop03zRZF7tPg8R0hRL5%2BQ8FnW33jkqfMv4lFHTnTYB%2BOQOE0nffoqqNjcbzTR6%2B7kccyqA%2BgwcOR9b1OD%2BWCUhCGpZ6QsY%2B88AyGv4fTWtZaPd3dPJ0GXuU0eLQAwTDczYSTARnbQ%2B9VyKhu7O6Scv%2Ffr6WJubowcYL6n%2BJqn2pworQIET9nHPuzIPLlh08M9TArSAfTWYuDBv14fx8myiefWhOA2QHMqxe6FbcT%2BJfeXLmxRdo%2B7ql1SOumD8gsTrCqkWBm6dI1qsOM4awOMtnbda4Aod0i0hBobY024Ej5KjDTy%2Fhk7sXjg%2Fp64bHxBZATLvJ9Pd%2Bc%2BMVu5UT7pVpKHaDOQJcJo%2FxAm%2FloxIJS2gDtIOSeE2SrxXd4T%2FvwZxjfcSddP0NsGqhGbUzu2%2FGPSMpdrc3Rfdzps0aeaM9jFKWGzENAxkL5DNOK9CCIf7Z6hRy2HKtu%2F1kn%2BJa%2B28le2%2B7cXJPrPXmrvqc0kf0tnY0m3I1FBXRR9F8lkUgAwWkGppPzqmohQBLQFaFXOLodhrajoxN%2BlC03lI6%2FqFRYKQvAAInUjdcFSbA%2Fgpr09qRLmRWsz9lUSmRXTLLeqjS9JiXhsOTfYjDAjYO9BjqkAZlNPC%2Ffqri%2F7uNwXrjhxLDvq2mU6CMX%2BY8Xvu%2FTixhT7j5xsh4xA%2Fx8SC3OXIFbBdajT14RwTcZFCThnI2C%2FPp4WFPZ10fkFe9xsQNIOjWwEjeijZEwHbJ50vXf3x9fdIidUe9RScMwsEyPpfDnT1wUNdYJZP2qWc%2BDllb76ba7PnFY5HJ3bJGfiPwr5wBujxqglpRBMs%2B7xONCtchBYUOWwgsN&X-Amz-Signature=68de6904949a0cc662d85cb0746f0f382490fe8c0d98f5d470b4adb1700acf20&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNYK5Q6E%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBOJ1ZYS%2Bm5z%2Bck%2Fl6GQOvCyx%2B8ihkfIaobeQTFdHsSQAiBmQBh6Gf2iZRNyDTrFIeQIUFg9loynFrF4swHs0PQlVir%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMf76gImxVgiyyhVXrKtwDdqGiUc%2F66Mxxe9NAdnuS8FehhljMFvWlcMkfWipHLYED7QIIKphzXZPlIzZlmJ0p%2FXw7jNklF%2BsZ6mceplxDPkHn7Vz6NkziEHhDjItPV8UvYkH7txUgt5PDyAXQSsG2yuunvAX4mS%2FH00Zfk1gjsENxJzD%2BEAuNj0cFz%2FLBf3BTfYoVHeZCecBpmgHM1DravFaZcBOjtYCoNabJXP6uePfxzCejIU1ew52bG5SCwsPFF25vRHUlyeuGjOFX2OuByyO1LI8TZojdZA0gYA7ss249Fk0Jy%2BDjZjo8C2u0T4o9PyV8KJfue%2FQ%2B30HRckzumJ2QLQpaOgsjFD6PLUPqpwS92wJS1otFXMfE%2FK2NXEgkHpinoc5HHfpZMD52JYwQN5CRABsVjtLxVQrxe0AcZ5ZVlt2Wvzg2CCz6guRfyPH3yCG2bfUt7%2BZ%2F8iHyBKGGsCosji%2FzNT5VlzLlisKUNntyzMULbE%2F9QpB7%2FnYpOb6kp9%2BANgE37ZavfoLMkaI%2BamxVGnygw5xvz95qM8pgq3oaqrTmQgdHX6EjW4OZ5iNOiAOKtKv0CgYXRk%2BYl%2FYD9DqodTDgPKKol5aXqCXL0lsYJ9s30kw%2FK%2BjAJaIVb3hNyEqPTdS7JriV%2BaYwo46DvQY6pgEE%2FwDN%2FunPJEHiP1wPCvGd9BZplsYqE92HFEZcWEpd8wZ%2BPDdmUZWWudDPiXMGHv7l1gywsKVfPJD0jxQcSfni1uiiciIWbl395fIcVeyWRGQRzW8C3zXCPLkTLc0%2BtmbiH%2BMAFfETaKtCTWBiXXEZSW4XSPH%2FHkyz9wsO2BVr1WnNsIOWdcOH4jKaWuUNbrCswii3ComgD0z05Cho5uNZMBo2h1FK&X-Amz-Signature=c0257f73296a187802abf223660d7d79b57e598fe4333a55b2df309dcfa81d2b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C47NTYV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFUZqXVWP0XEqKuyUluf3LVjQjt2%2FjSxhaqWMk5eU06wAiEA6623n5Q%2BvuZL4Haq2ZeaWksKd6dF%2B4SPwERTo%2Fe6ApYq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDKkyRWrWsoicXxUpryrcA3ypYPO%2BmTcqmIXFMsbP1kmmSYkrOMiYfhcWMExCzd3qLqx%2B2RKSzfpQshiHMaCDY8fe1cxk7kTXTluoOTNHDzRkwHEsN%2Bo8wbzYv8%2FdOeRq76hr6SstKfgB3rvMBlKnyOIfPtxCcvhmOn%2Fe4Ert5wKe1owiVB%2FyUevho38MWDxL8RVjYvLGilyveawVeUUSpHlPeT4YtFWBiQO0My405lcVYbuxkIb5QM1pvD%2FMRqNzX4CG7kjqAzfnCaDp4CxXmUGnHKnNKWg4CHIvQzKEXeU7d0XAX6f0s5%2FYk5Md5qibw9czZrU94DNGJ7F%2FOWfRPqWKX50wvJLkm4Sx1pzAjck7TUnel0G5KiQjMPk9CcbOIPaUk%2FYsdtBXOuYwPQn3LGTO6LSNGL2l8yfwUYkbSCq4ml1YcsKT%2FJIEE82OdsDX4xYhawlZv0rnGorI9SBfzVTdRuw1XxxSUz5h5nQbXobn3eAqVK8iyQIOHCBXlWSdVWi9Y95xPu%2FUZjLggLfNjR%2BDMT91bA1a4TzM4hzuQ3ejGDybtNcJaUdz38W8KeX6bcG6YfaNOi1UZrbbVc3%2FuDf2l5orlu%2Bum0%2FrkCjwfBDHS4JY16m9yvOicfkguY4Vr3hDu2%2BR9%2BXkof3MMO2Ng70GOqUB%2BziL1jI7MQ0%2F%2F%2Fi3qlF2fFVsjaTweK3pp9MSnighPoAo9kPjhPdFAzlRRLv17dsmSQGIg%2BNG16Aikr85bgKhbTIM8UJKa5oWph4eijpQw0B0NYUNQC6A1sItr0pcGa55gZoj6N8h6CutFlIM75V1IiQeKzUYqhBZwqIntqBMnJULbzof%2FzyHCbe7BhKNXeGuXRtAIsQQB5tGtd834%2BJCtHv%2Baxsb&X-Amz-Signature=8610b76a2aa21b36dbc4ffe5312eb83ad2a34e2c15ddb9caed726536cc3d0ca0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYBQXODB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB29NrrjCBbS39Fe0KGetX6YXjWe4wRG7zVpN7gdKlSkAiEAt%2FiMCi38tfthz90O%2BJ35YKWyZFQZkrPfhWGYEzi8Lisq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDI7ggCgIuwSDT6Z9oCrcAxmMtfB%2FcEcM9EK8O3DhuppZxmqt4tthl2rhre2KdcwIAYtFPXJXb11AqFhH3sYhkhJBD3%2BbGp3ZXg0IIELzO8qP3Fgjc%2F4QpI%2BbSMLZWRZPHnOeBJ9XLCRJa%2BVXa9%2BT0oxrzv1SrCJjqz92asRPaQZmf0H1OgAIZ%2B%2Fjrol3VEnH5Vp3sFE1aWs8XXwN98SHKtlQDkBqrOCNoHMhhgCSP9VcV3ZkS7H%2BOHXP7brmj2lhxl9cMAJrNk2OX4D1l4TBCTrBfT8UwIwpmA3D24JXY%2Fpl%2Fh1tPqh%2B2XcDt87pVMzamb14PVsAWM9sQHLx%2F6cgXzs%2FSj%2FhaFuVajmJTciC5OJ0JY83Qjb6LesNTiNQ%2B9WiZlNIJqfj6qNClztuAKljcQ095OmwkG57Gnzi3UPEJGBUcovtfjF0hADdlAfeosAE7GDeueABOFVjiNDuP1oyZUCM7%2FVWBI5ipSkG1hQ%2FD%2B4G7hCVsb6rsZh8VF66ATYK7hvugth4zOdyAv5KeHhNUvqS%2FYITJmYT9zm0lBv8D%2B1MqV6m6i7hxtxXDgsu%2Bra3pmOLmroB%2F9TvJcAP8toCZvv1Ye26%2B%2FMCMGIumc6KWn7LB%2FBb2mZa3dOG56O6%2B13LaTiKJH42pFW7lqQBMOyNg70GOqUB9y%2BIGzVdjP5N0PfHH5L833zYN8zFYzgjqIo3M0Vnx4cWgzoNynUewyeBp8oO3xc4QlE55v5i7sYWwbOEeN2T%2BIznzEbuC2NdDF%2FZTDAiJHnKCIoGFTMtxIycwubTJ4LUb3S2AFfa3dOXpTUbyZlNT5biSYCAYS65FY3QGk8UlYbGLxMknqnDtwcwUwJDqy%2FJLZRKPFDoH%2F0iYWqwnieHJDrl8Hfx&X-Amz-Signature=81688b388525f1a1cee18b0f4bfc1aac03d2870ef095691cee4afa2f3c1671fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MOVIZHX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDyMZyItqzgIDDUgqCSk3aAI%2F0DsU6z6CNtiBShNy1L9AiEAqH6awOrSyGf2Y6%2FfK8EtZe%2BhHzmp%2FZf03HIetEhwYJoq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDErPL8DF3x22U1t%2FTyrcAzsnvu2Jr7BXfIDM2mGfBzC7vkfy%2F61YZv6fTP0vXdzUvUkGbaFSH4W953uAN81xiAvI4ejXi9kAAWAJ%2FI2lcHjYLEAgL13%2BH16elbvo3ejZxGbA1rU782G%2BW8mOFZ6DNn7LzeIGWmAPXrYtbMY%2Btwfuw1UZt5lbbotvmDAj6Dl3Of6uucl1q5AR4M2wQYuyy3YeUTbemWgYgURsgDYI%2FcHxhGrC%2F2NcHKHqCuUs4cXsqP1mSLmp0r74hZQ%2BH28PD5tMAV3kGl9InZpxYffnDwcVFyCw18WIEtqaC65iis8cZLVi38tlmZKGsF7YFQrQGMIFCItASSsErrhZIIQwHBiPHiWxGIFZpYMPksciCsiv9b1z2OX6MyUNa1bRhuR%2BMeuIlijxNIZ9cZDEMe1xGVg0LOfktTz7krcvZnMOowmXa0aNE9XnZhE7F%2FQJmsN1Mpa6AYIlWt10v%2F5Y6JVIMVZ6Sqo3jQ7X1Y1BindVCQebAHN9TRIukqy8JRBw0fEApLDQNSajm6FM6aAQobdmwQJzcyFlBOGmP1fE%2BHizLFURVDRRxa6jmZfJomvqKv3P%2FnnyY1uKTU1454csOCobYKD3g3zzJzfbEjl%2FHASoj%2FGdRpkhb3CM0qvWGi98MP%2BNg70GOqUBALII3hOtXWwMxW5hNr7E88XY%2FZctyaluTeoq2U%2BSKadYNSDpUHfZQ7iNM8HODYXcqZjbrki%2Fm%2FYZWTGu6sz7Osz05hGKGTu4X5E6CanKrvUL26TdhcjgDtp6%2FJsXMr2MQVJKPo2VPQg7Ot3EhYUm1yXv49kF44Vmmg7J2pwKsWydhHVbbQX8TZ7G5jU2AzUdBNHhS6jHFBqeiz6bKTXYU0fTCG48&X-Amz-Signature=19499be55abc435d2216c742b6083a8ccbe8eb369f7607cb0dfe325fdc294e0a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VXDW2DH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7RGIaqe6duTpGnwC95t%2FMmKKhGGWYyQfamgdWlNT11AiEAhhbT9HNM5R5ONjBYJoPatBPx9irtf4HDLZO8YB8Cqy4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDLokfux4JXFVIqp5FCrcAxP%2BqRmCVz%2FAt1ZW2siU5KI%2FvBfjvWbdkDKpk%2BALAI%2BvYvjyIo8n7nLbSGBZ%2B1TQG4SIhwx4TtRWKOVlXTEr33J%2FduKd754%2FWgasgO4Sx%2BxL0OTIkbLnRyy3IxG%2FnBV%2FJe03srCYwRMd6nLbeuJUAlGhrhzLed0aHqQ463%2B7BLUGbbSRC1bxVxO7S%2FdP4J27cD08TZGiqKXX%2FBATZf2X%2FJLL%2BV7qwb%2BJzNc0o7MIMIUg6T0lw93AQCRbBRrsmxL3A15OY5cA8YBgccJY7%2BoWzr9IqYDZEm0Gqx8JcF%2BR6Bw1LXEYniiLhq1VSwtj17m2wr9wGh0hE4xAX6gMlACSiP64%2BuoeB9Jc0f7oweLXFwEOlHcb5VbN7J8NncTLziQI2ZKISxvBTbO8l5KblOonJZ7if7DxR5emtrDpm3J3TybWhNa6QMxrLZ1SsMh1qRCUS6WA1KZh5rEY9Gpr3eAush%2BxyUn8D1qQkuDGwhpU7aaWnibyu2h1W4ds2400wj%2Fl452Fz8BWM7aRIz92KpcOpXq80YulOTOQBOVutuK3uzEtVscXENxCLhQFgh96yOJUf%2BwNggFZCX6UcCw2y0iTgpVVAr7K7tg2nYYs8%2FxZ%2F3dihBq47tgaYJAEA4puMJuOg70GOqUBTDS87SCtHOg30ma6tG3kR6YfJCbclcaGmh0zTFkbU%2Bds55flUJbL83%2FR7jvxwkCCzplI9SMoxuwltXYG%2BpwAmmdc08Cr2YSAeo2oOEtRXfrURR9Z1brfLjHAUO4JhCAhgeMt%2FTpMZ7BAKzJUAPr8xElPKloEcztkwYrHtQ%2FqouI515li82BFxaz5wCfPJGTKWkIq3krNMZ9k9InKY4mKflUMoKVj&X-Amz-Signature=83f150f5f36a9217af054aeab4605247c0eb07f03b44a3294ce18c2bc59ac134&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBBDMCFO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHye5Vb6gJ%2Fk94Ewj6vYKjgT%2Fhi%2F4ZMGXyciZ9ft3BnwIgQj6O58%2FEr2uVf5w%2FY%2BD2DVFCAWvyB7QaGxe7198B82sq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDG7FFt8CY6DmCZoQLSrcAzkIr0sQM%2FJpQrKy9mR7cTYKIgIj8ILMTENN7nUS6xT1GIn7qgm%2BzDZRAFDNkOLcVayslByBTBDobuAQKlgDjb4YgwqBWvoUYD9DFrLfNpGQ92lHaEPcazyrOz7PxXwnoxOhU2zYzVgSZD23DgAtnBYy7ZcHZh5QAUtj5srfEKFArjepNPxhVw6RRdzjE%2BokvAiDuHh9c0Sq3JmUm6XFj0ycQQhrnGVeYUpz3zoYcVRPfLjd%2F54ceiEfFAXMvxYO9OZtOUnhnXkJ4tu6ndn96bqXu7MQAAEwG9VHer4hmZY93gWHjzY5PlpV4XLUIibT6CRWHLu6w5Cd%2FR5a8XaGGO4brM6%2FUmkqeW9kz%2FvEF3xQxqgG%2F9b11tXPAdDCXt6PAkKuKIV4qC3fa2KIBc4EJD5MWPKk2cLi%2F7w4d5U%2FI%2BW6TT9gzYhsr1wJYVFMm9L4MVPmIe800M6NvprtghaZ38RWG7%2BWrbfuuwl%2BOYAkppbSPciQ1zIx8PFr%2FL2wLeZ5zwXnnZFveAAzZyapzMFoQ4OsU%2F82%2F5tcNpW6qPueQyW5RKaiiWfKsLTNR%2B%2FXCG7TQef4RxPdan3eF0%2BsT4eLhdklvwdX683ZSs3hPnZZSVOY5INmyp5nP4vDzccBMMiNg70GOqUBC9pjW%2FpkYDNIrIaxWNcPrK5Gy579PjpgvidtXuK3nsNu2g0FlAr7pk4wJ83h%2FnNCEiKH1EQmbREbgFP535O%2F%2BxbV050IS4Rt4Q3cRUTBSp463mHqLk8RoWxysJP5wmZBiRzZIQp2WABKifrxjZqmre606itgfvy8N%2BsuamJJ7O5SRFmrQl%2B6nlPBPxDJOW60XevK5IdxkjH9KUHE5wppOfZcU%2BHP&X-Amz-Signature=28dcc73845078092162ea0d0cd61ed46d0110255765f591b41c1c44601dffd91&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646RFJQLL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFcw5O9g7NCp7HXPP9oThkVNpcZ3aIJCKT5jg43eYrZLAiEA5kN%2F%2FHH%2Biy61TD1zpI1sZeZZgJ%2FoxsGgPxAis%2B%2FfRHkq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDLnGvEam9Co5HLsa4ircAw4qM%2BDqyTihfLPpp9EIKZ3YiLWet7eZBzQWtFTTk7VS5NQgwev0ptskntC6Pv5SOQzOG2yr8vVBNzpl9g8Ar5gFNc9iNJazveJZkp25tBFbJ%2F0IH4wU4MR1ArQeU2l6J6pigQg1fKwL%2FUaQjkI%2Ff%2BqUBQ7UD4n6s0y8YoG4SN9O732%2FK%2BPrZA4eEcnlsvwKEOo9WOiEqske1M%2B0GZi%2FH6L3tKKdyrIcFoFHgM9F8cIKpObSa05J8vgvu9A9ManpwhwYx4vB51YTcABjqxxzoLGjNoHt6%2ByVqLBVrwD%2BzEs1WkMB00%2FufIUdR0s5M1Dc4Z%2Bx%2FkTyVBHP4b9IWHp4ingsJcYtVkGsa5qE1MKAHvgEKGmoV%2FCmC989JgaxyZtTg5C8v4y1tmUk1jdDz5wnUVDIPZVvC8SdQEgukGvbP8wJyxOYbYOHuCCNCWz5F6LjX9iTjXy%2FraHM8jQvMXHXobdtNLOjC4HZLWBJ%2B5exT%2BmcsEaCx1BWNgSjA0YKf1AWqmiiExYu459zM0h3KAwDWFJO6Ryzlyoh8S91vRDwutIX6xnHytzrE1Sxd4VA8YF9vFD9METCRLsklVTmp7n68uG0r8vISC6QXovDQXTJfYXvp9JBZ4rSyDHXJoUeMO6Ng70GOqUBW7kqkXYT52PG%2BxZ0x3TUieXNyaqridsPbT4btBqTzV7nw8xkLMpqXh6LsLUfY7cuIg21jZeKsmxxVC3qQFP2BmupBtbd2Co2oLblEpx7qithAfIaKgdicWzHOzEtgMHNEl0yyd0ZEmevs5y7fjBTosuk10jZ9gw0IE7%2FpcS13ROH76K3eQj9uPAHu9v0qpssiBB5HC4NW9Eh5Hw4PVm5s5KV%2BHml&X-Amz-Signature=620c1c3c825bf18f9e22b65b60a99c3b8c72729d59c79a00bbe1c94ca2560b6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MOVIZHX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDyMZyItqzgIDDUgqCSk3aAI%2F0DsU6z6CNtiBShNy1L9AiEAqH6awOrSyGf2Y6%2FfK8EtZe%2BhHzmp%2FZf03HIetEhwYJoq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDErPL8DF3x22U1t%2FTyrcAzsnvu2Jr7BXfIDM2mGfBzC7vkfy%2F61YZv6fTP0vXdzUvUkGbaFSH4W953uAN81xiAvI4ejXi9kAAWAJ%2FI2lcHjYLEAgL13%2BH16elbvo3ejZxGbA1rU782G%2BW8mOFZ6DNn7LzeIGWmAPXrYtbMY%2Btwfuw1UZt5lbbotvmDAj6Dl3Of6uucl1q5AR4M2wQYuyy3YeUTbemWgYgURsgDYI%2FcHxhGrC%2F2NcHKHqCuUs4cXsqP1mSLmp0r74hZQ%2BH28PD5tMAV3kGl9InZpxYffnDwcVFyCw18WIEtqaC65iis8cZLVi38tlmZKGsF7YFQrQGMIFCItASSsErrhZIIQwHBiPHiWxGIFZpYMPksciCsiv9b1z2OX6MyUNa1bRhuR%2BMeuIlijxNIZ9cZDEMe1xGVg0LOfktTz7krcvZnMOowmXa0aNE9XnZhE7F%2FQJmsN1Mpa6AYIlWt10v%2F5Y6JVIMVZ6Sqo3jQ7X1Y1BindVCQebAHN9TRIukqy8JRBw0fEApLDQNSajm6FM6aAQobdmwQJzcyFlBOGmP1fE%2BHizLFURVDRRxa6jmZfJomvqKv3P%2FnnyY1uKTU1454csOCobYKD3g3zzJzfbEjl%2FHASoj%2FGdRpkhb3CM0qvWGi98MP%2BNg70GOqUBALII3hOtXWwMxW5hNr7E88XY%2FZctyaluTeoq2U%2BSKadYNSDpUHfZQ7iNM8HODYXcqZjbrki%2Fm%2FYZWTGu6sz7Osz05hGKGTu4X5E6CanKrvUL26TdhcjgDtp6%2FJsXMr2MQVJKPo2VPQg7Ot3EhYUm1yXv49kF44Vmmg7J2pwKsWydhHVbbQX8TZ7G5jU2AzUdBNHhS6jHFBqeiz6bKTXYU0fTCG48&X-Amz-Signature=29ba8f50fbc276146ee96a7f7c1e648a520277aef0841337e67b1e2583d8416c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBKYAEF3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGcG8pH0t3ww9Uo8n%2FiZPgJv5eavXtftLA%2B0CX2onBSIAiB%2FuUdC%2BJ7L8lwwBJYL7K0bfIHcv47rN0C%2Fs%2FCWA2lwNSr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMIcOaZVngYuokTqYYKtwDGqgGI0QFlKux4to3ow0ulQmH3gp3Ly4CJHt7tLdRestZmNnJOV7Tv7XtvI%2BsLEw4pVpcJp%2F5eGnPJsON7rfgeOJGdHiTbi3BviJc%2BnmVFieKO1pIX4Hbnb34S5LCISIDw16xI0OdGLfPpaReTM0nefvmhCQjGbIWp3z4eaVQ9dn%2FUulV6amvh2vbJPG0j51AQV5NLaE0O4%2BNyGRrV473sY7M8ZpYWHd5GIgqx%2BrF4l5Kc1w4kmmDkugkFXup7gAGm760E7XSCWrKXPkshMdOyqVZXZWL0ZueZk5%2BelDzp5uRD1sx207JrFrKtHwdQvrtzTzOmdZbOb3RMfamCuVJsPQg6U7dozbXm2FEq%2BKb0WIRLCK95nuSTkL8RfAAmPdTU0bqCdstIEQrosGgbE3AqZKuDYVlBgbFKb0RaleOnRVWwBkF4ISUHEMb%2FAi65m6%2FPhLsCB8nN%2Bi1TvP6feVYS6SRQgJdvpqvPQm5ZCdJ8yJLXQQysCB7%2FLd5NU4tuv5j%2BzXWKNsGYqMbyuXcV6zADuRYJVUxPW3vdAlTcbByUunK64ZmKaSjI7SEgb7%2Fqk7%2BEcTwZUBtBiwjI5LCMYX%2Fp1JklgHiv8KcaGJY0N0f5TQKahVyYwAsUHDzLdows42DvQY6pgEet%2BeDdZlPkEPUYQl%2FeAu%2BIX3cm%2FehcLN%2FlvGge1IeOyWUn124awnmV4YSCuqMBfMy6ZEks8n5DjGmsctRUVoFhsr7K1dWNxDMMcsNsyu63M5B0Gq7QXx9cabl0aaw1MStkn3AcBL24BWspVakn2ovcq3DU7HPW0MFhurqxYkQt54eWclnnK4Fn3zPXUQ0gfPIBRvwkqpRmUxXNNoy3Tk8A9jz%2FndD&X-Amz-Signature=6ebba6771df9cd6a9ce8d6510794ff98d990d0d275667d6221fb39a9a5ebc9df&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBKYAEF3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGcG8pH0t3ww9Uo8n%2FiZPgJv5eavXtftLA%2B0CX2onBSIAiB%2FuUdC%2BJ7L8lwwBJYL7K0bfIHcv47rN0C%2Fs%2FCWA2lwNSr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMIcOaZVngYuokTqYYKtwDGqgGI0QFlKux4to3ow0ulQmH3gp3Ly4CJHt7tLdRestZmNnJOV7Tv7XtvI%2BsLEw4pVpcJp%2F5eGnPJsON7rfgeOJGdHiTbi3BviJc%2BnmVFieKO1pIX4Hbnb34S5LCISIDw16xI0OdGLfPpaReTM0nefvmhCQjGbIWp3z4eaVQ9dn%2FUulV6amvh2vbJPG0j51AQV5NLaE0O4%2BNyGRrV473sY7M8ZpYWHd5GIgqx%2BrF4l5Kc1w4kmmDkugkFXup7gAGm760E7XSCWrKXPkshMdOyqVZXZWL0ZueZk5%2BelDzp5uRD1sx207JrFrKtHwdQvrtzTzOmdZbOb3RMfamCuVJsPQg6U7dozbXm2FEq%2BKb0WIRLCK95nuSTkL8RfAAmPdTU0bqCdstIEQrosGgbE3AqZKuDYVlBgbFKb0RaleOnRVWwBkF4ISUHEMb%2FAi65m6%2FPhLsCB8nN%2Bi1TvP6feVYS6SRQgJdvpqvPQm5ZCdJ8yJLXQQysCB7%2FLd5NU4tuv5j%2BzXWKNsGYqMbyuXcV6zADuRYJVUxPW3vdAlTcbByUunK64ZmKaSjI7SEgb7%2Fqk7%2BEcTwZUBtBiwjI5LCMYX%2Fp1JklgHiv8KcaGJY0N0f5TQKahVyYwAsUHDzLdows42DvQY6pgEet%2BeDdZlPkEPUYQl%2FeAu%2BIX3cm%2FehcLN%2FlvGge1IeOyWUn124awnmV4YSCuqMBfMy6ZEks8n5DjGmsctRUVoFhsr7K1dWNxDMMcsNsyu63M5B0Gq7QXx9cabl0aaw1MStkn3AcBL24BWspVakn2ovcq3DU7HPW0MFhurqxYkQt54eWclnnK4Fn3zPXUQ0gfPIBRvwkqpRmUxXNNoy3Tk8A9jz%2FndD&X-Amz-Signature=47736693b2130629890dee6e2cae1cf7ad117532d6bb5edf62d0f781d00be7a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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