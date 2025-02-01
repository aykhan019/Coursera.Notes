

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTBC7J7I%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnWV3p619v4x62vPM%2BPHmfkHYphz0zGwSfZ5zvBaMS3QIgJlE8HWHKjBojrdIgOFCEG5GoeMRl%2Bq8i7BZmWf2ZL4AqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHczDamM2aCVi7DY3CrcA%2FhbjjsfANo6W%2F1S6wPfE3BpANHyQQOWsNtPM7M1dRr%2BN7mtzRNNpmNSVmdAFR8aA%2FiA3auyQkvZxXtUcXSQb8tWeoQmmNsiBOwvj36oBGOU%2BmXYCyNOezbPSLTokGmeJAhun8vtvcjAsZa3%2F99mrLOIheKvwUvqr4xYGBC460e0xGaYaEnthgCxFyWMnon5ZB5XlVvXh%2F4AWNvR8CcnmdgJsU4HYPY5K0CicU3IxEIio9Y%2F2sXm8SKxFGSSZdPejcsNN8UE9eKec0PbvR9RVTTQ%2FppJ2wwOa0TbHNeKXvCSsAUhiSC00qI35%2BLwtX4qRT8725XjI3W1CO5JGdfOpKAy3%2BFg%2Fm7fy%2FnCCUloiWgRmDCNrT2FHXHHPih%2FbB6KhYiMrYcsFB6YZDC%2B4hiLipR3Slc1IxYRD5x8icJlZxvEAA9GIDLA48nbQ%2B%2BkrfbSnO4hVCDI0hkML%2F26keplC%2FBBf8mCcf3TQDHVvd8fW88olTUqxeGTnUhoyTaNzBWC4VHMmKf9EOrPDl04CFbRrpbM8xVdwgPDsRImLDm9dRrenz6GzUQBgGvmiSjkjLDy93yyxVam3Kj%2BEa1NBy89fup5vfP3TdeUtezFi7w%2FHuLOXdgPgqMPQKCEP90rMPKT%2BrwGOqUBMFW87xRufNimQhk1ioC2tTCoH3ier84pAQwMNrhwfS%2BQB7eLhs7uywZeDSqFAi8sd5l7cyu3lbZbeeU6%2BXLEB0lIuUZRsNLFMQhTSgXIbo1pCxL7KJyxccz0DoTOa5VLa6BxTop5OnirFLy%2FOO8knqBkeBijS4dm%2BHld%2B5mAzW%2FKhVzXTNkGkIz3eiJOuXipqfehQPctjwbV2szWM4NztHF%2FxklS&X-Amz-Signature=97334acdde1f33154309a2addaf74b826eb9a917b4e3c183158d35cea8c7a022&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJT2HD4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6eTf009JtXtBw3r%2F768LAx5v%2FbL0%2B7powAoKxMEDZqAIhAM00Z33ZneXFWNw92HNewu9jd%2BcdIdt58s0sFwlijwJMKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyQc6wXooun2D8DiDIq3APaCUsBdvAxR3fhwvucUnDLKFWis%2BRndNSbj64LvrGL7orJvWyz3tXSLGFsxokF1PYqZGI%2BioJ8INWucVegFDtkmYXwCBrJ0vjkaqkD2DMQuE3IMG2FeNBdf1AoKwDC8240dug%2BVsBOKfYwC8pac2c7LpH%2FXXpmSEonIJWyzQ3Ue4l5Xkru0BbLXCVluy382o3wJ17U0rqv9E8bd4L6Hg5r9D45kpvGpK4SfOPd6I0T1HTznsSfHkNvmX3FXYwfpyMP48vSuUOykZn1SzsPE1U9PjzFUo%2BF9OqU1%2FVRF6zLdKsqVLNcG4C067YvYee6niMJCfrEZ67j1zTHqQblkB3XvGz%2FSdXPRxyKjIBe7TwhYi8zwyffJrBfvCxdjmUym2cDxjLLOeYrbrdgyrMfyPFGUOFKtR5TYecKKDg5mkQ%2BxyIbYYmq7iwHzWLtcqKmE%2Bg%2BmKQS3hy9mGeWXGMjOdSyo0%2B0AXP5WpGExI5%2F8J0natjMD9n%2B6Isd7fwAlc8kcJl%2FIWEBCN3s2jrM%2FlQBaYaFSj1QD1zEpDPhSye9a3ev9eKwN3QjaYTBxeWE%2FYXQMpdnxClLwvKJk8rQvbu809rXq94IzYhBzEmDzKafd5blrZpS9%2BFF%2B9XFDZk8wzCRlPq8BjqkAUle6IqBlJRL5rIFh0d5AobIcyrZPzAb49B5mhZwlFBuj0WqJfabh4E%2FuVjeGySb7qoQlikXQC427GWOjl17dg%2B3%2BYp5ZXh6NY8XxUNhEjFALdAaAWeAfWK1GtsQz%2BnIuJkRDcR8eDt5t%2Fat4PVw0e3jg6qqUTVZtMrOiRllemBgMw8%2BBQCcbuIoDM5xEZ3ClOgLvFWjPrliTF6ajkyTpZIsHd9W&X-Amz-Signature=34df374ddfc354cf0c09a82f525cf88b8bfc87bd304cd273286751a7c4eada19&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW75IOVV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG1MjEAZp%2FPIlV7T%2FtSj6Zy6WK%2BvkWVlpuNIHMwdlEZFAiBBboEHwB2Sv8VDn%2FNs13jvCSVpN7P3FA0L1yULLITjhCqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFamJkhglhdvwhceVKtwDzNVmDxDDgIE%2Bg2ZSwVH5FnRN5AVtOC6pzW5t8zs9LPKmnLk5aJuUXlZGjXlNNho%2F7WTPbXG4ZT%2F0FqM3j7bHstuMRPUYvGtNv4AZFdkB1M77fYudey6%2BZfH%2FNxvQFmrzeEPnkDYM96ABuRIvPu%2BcnJLYc312j%2BS9td5QcL1hpMTzESF%2BiXS56yeh7FToY1AxEJFBtVvw5MK0GIGPJujRVW02UUl6RxnPD0aOp8A5HvN7UjnyDZVv8fHEyYmpgQOitu5fKgPkhWHSdMxX3f8vVa9isWxiVLDHUzFd4NEUYRTyFx%2FKV3h%2FjlBhvawcbhT5y8oMgv9PsG4WZr0To4ed%2B20LQH%2B5jReoa6xea%2FzIr3jGFor0dmuWJZG1ubsR%2BxPXLlvDXRDZSk3VJhF%2BSaMeZOZ%2Fwy07vpYNOkasdN0dwc0mtif6vDMKe3hm2PKRdH76y1FVWP73gz5LLrn4oeZDHh%2FVIlQyOam4cbKdCgdA5sUFtHIbYAzRqBO01y7jcadtsgdbktpSbfeQdTLlb5FJYnLnGwRBUlMgxLM3cNDDHJNco7iGNizYmca6xJyVdTg6VLGL1ridRbXhpsfAALQcmo%2B01VDlcNM0Qw7dWi4QeJ0NuXKr%2FWQzrppEyJQwkJT6vAY6pgEeU8SOvdhh3z0DZN%2BArJmD%2BtxmeQGJgncDnaWzNkRZU5zzKSp89Ly%2BTcurZf9iB2u1uQjcPrKWEgXZ8DYQkXkE3pAqw2KQJxziyUWeDarCZVWTQ9O0D6zd3Ek2Zx52VchSjjocHXEKMktq89cmY6bvmzFOZ5RGJ6P4DsLZP7yHM9UAK2%2BWc1nhHoOrMSANNogNbTTcUtHLo4MBvq0qURY8%2F2TVzhxd&X-Amz-Signature=730ef78b3dbe4b3e09fb229d05d6082dbac3f672da4725868e6a3f6544807f51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSFSYETK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUAQDCpcahGbkVBFozKpbfW52mQrYTlC83G4FOXzl7SgIhAO4UiMTxTcyi%2F3yg%2FOxDxiK7T%2FG1oh8tS7zURFjjkHnaKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwiGKFho3kZNNinKb0q3AOuSZaaQL7whGS5VjczTKc%2F%2BgSHkBAHHCzYTKCxu5uU8bqWNE1wgXvJhYO2FMLwNn34bjUfngttZt2r8zl3g0PyNwBi55AbVI7igWMMS2aBfLllVDa0R7HvbUjtpiEVKKkeXLl%2BJCnL8zyv4BE7LjLw7yxpn%2FFh%2FRvbbOGI6oX4guroCEXX0TL%2FF5J4GLw90CTkBZd0POFWXFSHSMA9ITjD4OyDgquegrshzOYoX36BcwWRwbC30GFvRADIX%2B78eXaNR6w0ZDSLFv7rpg0FHc7n0wsYVMeREhY5VFQB2hXkOtMvsy%2Bod2vneH5iZipQIFnNAfHGaGelS1De%2FoimQwdkb5U38ptjKnLHQc7lTdzM2%2FHcIxbPrDiuzMYxA0K851ueQCAUI7P8jxAPYT7OWO%2Fj6AiBBLNblVtgPGgOFwYgpyooSOpcv%2BCgPisLogwRO2njIdF752Z11dLjPKNyGr5cmMwZ47qOGTJiWNrc23SfJBcqm2Wzu%2FyETpxyShph0HwNKzDMpQSsTXjtA3v4B6bcuc71VQbMBhN%2BS1jU3WS4dWD5hBbIGCwyMcCfDPnvWjSNNT4tReG8USa8MuPhBO%2B%2FRmuE3OWCwUXXP8nTMhZjq%2FqrhQtzngj%2BqT973TD1k%2Fq8BjqkAXJkzpacKWvCA4179ywtn%2FvNXPuHB9gJbkutY0Ca4bYL%2BNaIQhL3%2BWIlkZzVShe7hJzNh7mBAZf2lE58jDaMMIDtyVm3UcwGPwlUt1xx0FiAj%2BR9POkWN2yx4sQ5j01qPvDaSiN5wfI1Ximt8tvjRsVnfCouvIe56ZkwIcleLp3%2BeGakF6%2FkiyxCzXO1paltEvnesyvSOLkEXDL%2BPYYLsf3L3Cmh&X-Amz-Signature=18995021655d1dd93d4cee29540162b6f9b84375cf03ea7e52909035468022a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667D2V6YKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDymk6dCl%2BkeNQmEqTjt3VE5C%2Fm9w3mAwTeW9JcdjZzAAiAwvq%2BR9czIuZy0VjrtBhAJ6qHRq81vWfNnkb7hdudwPSqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9pGjzpXM4Chx%2BqYxKtwDboGw3LzEdNAUXRf%2Byi%2BtjlGSeAhZf0Sq57nm7rJ%2FkXB%2BeJRDlrZEQP3cvAck9LCF9oGka%2Fxw5Gy4KslTd6A3S5EmYJkpOn%2BjqfJDfj0x1LmXXWBaWt8jWOXRDeoisfOitSiuSeig0lq8pdFk%2F%2Bu1OBPD7Wpvh7Bd5jzGriwldDHgbzdFejAj3OaT2VY9RlGa%2FV1%2BJMXyXWdekaWyaorm8xBpYRk6i%2BYU0kyA9IPu2%2BFzn22Vjr0xd1ZVd2%2FwVi7ezY5fR75gceg4kO0zd0sxnmPF%2FDaW177PG870sEJC0nZQdpqD3nevGrK6Rpp%2FLvUv4w5tlFF4oh%2FejSxG65f0leIvVyrYoTEImr4jISsf7wchNQu30dMV%2BGduvhfyMhHvZNALg1Vad9QBPqGqzZwxE19vhqgSWxi9%2FJp%2F1fBWGKn%2FgHTlfFsIdGAfuDuX27ZFuifJtKlKvNImRtpk8iC%2Fzc7NApFqcSWnG8e38lf4YiVkm2lrFrgW9SRpSRg0Dxb4oOKKcUBQEtLAkhgHu8wpparJrehhS9qRxbXXuUbFJTBjgg1ZwzBcXtYfLJSbu4Fe8RR07m4jEtzJkaFUBCtt7mppZINWM2FvusXUI%2BqoSkvPYDLQe7t9jw%2Fpv4kw2JP6vAY6pgHL08xRYViYdi5q38VR%2FBDfvfaIi1lPXyn7yexKDW%2Fpbdq4pOkhPP0WhRdUGszBdso7exNZ1mbwpxRVDngrNalPmWBcMtZN3gZQRVPppck%2FFuVVA21RoGXgV7xHsj55PfLrkv4MPGRImwXvZMGMgI71aX52QMG6d9e%2BTEGJyvs7GCSPvPheHnKe0k%2FFc8wlsIbafahJO4DEuvOKVdeWeiRq%2F%2Bkbdc1t&X-Amz-Signature=9b63785c3cb7d72f3e5fe374b7e516c4a1896a1a4b1db4d1480ca0e3d06db777&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OISNFR4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCf8FA3dlb3QD%2BT5a9l%2FiDPQwoQJ%2B5%2FHm5bOfC2CI5lFAIhALpB%2B6eRtH%2FnbiZQ68FD53dPba9VZoBdBr6YyHWjjIbtKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4aComnDHaSG7totkq3APYkdrvz02IARrbkIcA0tF1fY5FchmX1f%2FZvzwAptODjRfB7Q8C81aNEAB%2BQH2xMd1Rrixw7JJQyrWa9ouZeFylARCrasDOINb8jp3QyAuGIFU%2FX9%2FdANC6D5CU8s78dRxIXUbZfIOpFgK97tTrB6Ytsdjlx6vXLf9gS148K9RlZ4JzrV5VV3t%2BkOi%2FSSD82F8bsVfMSQ5L19aODhAxkqDL%2BP%2FObCJU8VhXKW9cp32OoH9oIVt9WaxB79iZ76MN39W943S3IShhBcepTAGS%2FXx3dwEwyboABLothJk4tnnk6tQz853b3T3a6HFrzaTANAfR9iE3319fhclGwQrNwF3pob%2Bt8bQgjFa42nk8O9ekf0HwNB%2B0UpMlwLBC6UbtP87p9Vigp7nd594b7SRrXug1KoFdrgHy4gi6El9RULIt84HbQu46zectiU76GAEs%2B1AEVgamCXoByWM3TqRwZDfqbE%2Bz9z4lVOVtRJZJLwYjqTgBPR3Ih3eLgT32lwHPpYmBSzOgnTiwzuP16gfbIvDcPpg73PLMLLxnh3CIQIiH9myvURHAWS5TmBg%2BMtHCIYuCFTsR5MEtAArv%2B6rFUyRlNTw36ZMkdwZ1c1wTUT3dk221JUeYKtwwoncuzTC5lPq8BjqkAWTzHPq6zb1JIKVKBvMU%2Bednhzvy%2BgTgqk8Tib8EgmJia296ZunIYnuFdpHkrezQCB4lYeF5mnXlEWRo0pHPSnsBM67G11o%2BbUh9DsLJ9x7POrgycKebKD1Zd14i1JOEiYvApg9xTC26CnQpwgGELVv%2FJ9NjzmqqpZUfrL8uQu2febloT2VVOH5sFK52zwXWnewn168P6zERqxlt%2B0HYu0pDdeFR&X-Amz-Signature=e8af03b50c655e43fead754365e18cdefdb4246d75c24848ea27b8802d03c6f7&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCYODXRR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA5YRF81di1qkfpDt6gd3ST8UV2QHpKg5QxCyy70tWCTAiEA60L2davjbJOknJpLan%2FFCbQMr%2FPfYwyA8bjhv0Hh73MqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKOwVFNV8WYGLlHnvSrcA6iVwN%2FakOL5pQ1Qu4g3G93liEKjld9mHF1sxdunOskFNvBqVYSQ6U4RC5C5N%2FAqDiFFAhm2KUdz1qW%2F7GY20hmQXGXpPo108YWqkgu%2FIAq35W6ZbSAU4zhdFfaScnHkEL5kGBbkYb4aDgfrpkP0lSoh02CWu3l4gWRfrfSc436FYEcLHw537NNrQDqEUg9U6aMxdI1fAwaIj7cn0k6%2FApBRq8HDcaRWPlqi5GOp0Aue7oQNDXOtuZhNd46fihbL8D01kaF01hgDkYMYIxQz3BmKPq5kxvKtRW330oRJKc%2FVsMGn1eSnAqDpSeX%2FhlI6XpVqRZ%2B1PjJIu3O5AZ1HN0KMI9YuJXMUqkrS4g9D1IT3mlGMYggwDPeLEs3TT3uPZuKPZ6n%2BWWZZsXVjbVLsvxWNg41%2FMRoV2nXmQIySHvevuv2XOkcyWtMWGSu4JpsBX0of3%2BWl7Z66UU4ps4VbDMBehMhq3qCh%2FpHn%2BJBMRkS74mMH5C7a%2B%2Byavq51uY96HXxA9bzPqAsuvKHJOT7qigtvd%2FcDw2bhw83xSdLbhNmbigoIqJwY1LLQpI%2F6zM0Sd43Z7kFoZ3NuZbkUU8zmHO%2BCUD7W6skKYKQcikpzbxwZR2dYss8M3GsBNEjwMP2T%2BrwGOqUBS7I%2F1ri%2BOr5ZFsT33%2Fl0pr0OWrKK%2BTjiExnbhd%2BkEJoBVKZUoB3d71pE20Th86peMNgaReNHrz%2BWtuURUb52zITgSbDaPcsNWjFvLQC5YhL3emYKRqBBoh35ZtQEIKM5hsbOrI1WF0FC3RTJ%2BUmcjYheI3p8q65QgP6ktHl%2BB2mo3AorZiN%2FnLbqA1ScRWmjI93d%2B%2FH6XS5VYTu8s1NSxwDxI948&X-Amz-Signature=c8fb706024598d4f968115e6a0f525a26a4f2c67a4613dd6095af97f26d6b310&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SBIMBYK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEGEYhhtITl%2FfTAFrb17nn5PTTD2i0Rucv9NWyk3UeUwAiBBdex2%2F6VAJoYoZfV5FvjX7LZh2bZ5BzCw20iuMHnWvCqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl%2FWJTMhoyPJeRdOCKtwD0VDl1afqz1ydJ2UZRmfqRaRuOyZ%2Bn0yxmcsp0baOHvMwlK3bTA7gesKOpvGnYIE%2FUHCUtUX699DwR9901mBo97ArktkJsVyqX6mRrbhoOio1kAsF8NgHfv%2FgWNiJB%2BuC%2BLD5U3bHEC6pe3Iu6XfQCQe4mcI02taXEbUun3mdiVf8CAs8WPKVeGl7VlQu4oEGB5CzF%2FnA126tKsvjR7XrLruAEWtc2XDvrlZ2sGwdoCzoX5Dc0exi286iG2lDuz8EQ%2BVV3sHt2XKOkXFnFs1Jv2gJsu8BLpjQcJAPhYLSVL3UK5mTLe8N6r8QCw%2Bj5uU20uHBwQVoKXDGROlY%2FTLtPFpOXb9%2FCHvgUTmpnNOTXqRuQsdWlEoeuzpBQO%2BYA1ezNxQiSKDfHDEeh2vP2g9dtp57oi0idJJ%2B8TNewqkjNU2PmHh%2Fom3WVHaNpcgJITLVljmmpxn%2FSU60epXyUiI9AFe0qXbn3%2B3cqAtcnhPvBIbWEljtDxNSysWYr4H1RWvAeYm%2BCkDi8DFDuxmCF33lR1kkW1B5M2%2F%2FQe7qX1s5Pi%2BjfGNi7O6iLKsu2IQa6MMRB5smvH7ct9rItf18m14TgfDx4r8t74V1AUu4JeHz4Q0Ud4sux9WuOm13ZegwgJT6vAY6pgE9u1PsfgB0%2FPw3efrPDCn0vMP8xR2OqB%2BHsG44NVihPcy81HnmQS4NskwH%2FFOxo6jxN23xKR7VEVY95gneczqKwZ52rJX%2BkxycW8C7jqi2YDLf7SfL3a1ZdRLzGgxlfd0CsxC6rbVR7gJHVkZ%2Fq2e7Pm6cS%2Fp%2FuS1cWBdvVYO10Y%2FEf69kOgPvVcI2FYPONyrdf7E3HGT8TkjK%2Bbu%2B5d843c3gD7cs&X-Amz-Signature=00d485e7edb80cf0af5600e05f4f45533126bb3e5fb04801d416f1cf1b0b1ce7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667D2V6YKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDymk6dCl%2BkeNQmEqTjt3VE5C%2Fm9w3mAwTeW9JcdjZzAAiAwvq%2BR9czIuZy0VjrtBhAJ6qHRq81vWfNnkb7hdudwPSqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9pGjzpXM4Chx%2BqYxKtwDboGw3LzEdNAUXRf%2Byi%2BtjlGSeAhZf0Sq57nm7rJ%2FkXB%2BeJRDlrZEQP3cvAck9LCF9oGka%2Fxw5Gy4KslTd6A3S5EmYJkpOn%2BjqfJDfj0x1LmXXWBaWt8jWOXRDeoisfOitSiuSeig0lq8pdFk%2F%2Bu1OBPD7Wpvh7Bd5jzGriwldDHgbzdFejAj3OaT2VY9RlGa%2FV1%2BJMXyXWdekaWyaorm8xBpYRk6i%2BYU0kyA9IPu2%2BFzn22Vjr0xd1ZVd2%2FwVi7ezY5fR75gceg4kO0zd0sxnmPF%2FDaW177PG870sEJC0nZQdpqD3nevGrK6Rpp%2FLvUv4w5tlFF4oh%2FejSxG65f0leIvVyrYoTEImr4jISsf7wchNQu30dMV%2BGduvhfyMhHvZNALg1Vad9QBPqGqzZwxE19vhqgSWxi9%2FJp%2F1fBWGKn%2FgHTlfFsIdGAfuDuX27ZFuifJtKlKvNImRtpk8iC%2Fzc7NApFqcSWnG8e38lf4YiVkm2lrFrgW9SRpSRg0Dxb4oOKKcUBQEtLAkhgHu8wpparJrehhS9qRxbXXuUbFJTBjgg1ZwzBcXtYfLJSbu4Fe8RR07m4jEtzJkaFUBCtt7mppZINWM2FvusXUI%2BqoSkvPYDLQe7t9jw%2Fpv4kw2JP6vAY6pgHL08xRYViYdi5q38VR%2FBDfvfaIi1lPXyn7yexKDW%2Fpbdq4pOkhPP0WhRdUGszBdso7exNZ1mbwpxRVDngrNalPmWBcMtZN3gZQRVPppck%2FFuVVA21RoGXgV7xHsj55PfLrkv4MPGRImwXvZMGMgI71aX52QMG6d9e%2BTEGJyvs7GCSPvPheHnKe0k%2FFc8wlsIbafahJO4DEuvOKVdeWeiRq%2F%2Bkbdc1t&X-Amz-Signature=629166ef2700c242b4d119c3c49539dd4d18e9d3425ea1629933811df12ffec2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663VV3XEO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDZ117b356Ii27H3uI%2BaHI8jSLNzYCkI6cBrjcfPq3DLAiBT5U4kmy%2BBCIKke7fm9a15McPkHbaIgDkMQp38kQn22iqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM80d7GxAQ4wFV0WCNKtwDZNIam%2BvRew%2Fnbyh3iWhJvw2b509JZkCqbbTYT4CVGdleM5tuG6aWnWlmguN2bl4jmccpVZjkRIUERMFAsTSlqTcGrFjG2rn0VEdTFi6C5JlIn4IM4T9B0Mh5%2FzU8odF3pte251uyHyItuWYDSZhzH9wNX2YDWLcM5zzgu75pIPcy3HwoEWhjZyMbRh4gI3QJnIGK8ZDXVoZeOk%2Bu0aS4P8eJgwc5CEAzPvEcbiEc9%2Bsm32QImOb7qKleB8uVcx6K4dvrpLmQdKyY5kOXpeGju49KoZCyyR4DNNj7625R5tCxNXG%2FXghpNq7TqpqrkZB1qqiSthxojP6GkROC1XQboTFWGDCQruOaUFc6N9RtvS1zkRlMI96x7zsXP3SL77wxe%2F5FNscduN62gUBInlB9y5ztayFo3V3%2BD2lA%2BAR0nZ5eg4q7Gxk2WYviPAy3HcoAYidwAlUSIO%2B2QWRZIbjdCdakjY5P%2BL7T85GxVFF82wVJTsnbvgI5ybFhC3IrQV3J2Nq07tiHkW89DXqGVz3PpkHUQIIuiXzHzQKGO%2FvDDWDPHs%2B5pwI9O0vmKAmc7ZtTAdouZ%2F1pyyZKm%2Fmw7HxrgOam82yKDlfwbTMwksa4s4kzeNRX0PHOy7zaLJsw9JP6vAY6pgF4VqpGXdUqDM64r2zGAV4Nch4oLPZlkJWXAyjBUySEJFDmYwuKfrxVnFILATsmuAJsBAjj89IKET%2BxPwk0AvdMe0jKjXGgCa8vtA1bXc0uxFUA2BcZc54UNgCkIE5Lk%2FiA0XhRCdSWRhB7lRnjbWnoe8S0XZZnI0Qop5ET8wAoBIN2d8gNldpvarcQOHMTdJ%2FSjt86Wn8gwNCgVoADTjhzbvatasma&X-Amz-Signature=8769cbe23e04752a8db28fe1a10b5d4dffa3460ceced6d2efea3deafc2f637e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663VV3XEO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDZ117b356Ii27H3uI%2BaHI8jSLNzYCkI6cBrjcfPq3DLAiBT5U4kmy%2BBCIKke7fm9a15McPkHbaIgDkMQp38kQn22iqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM80d7GxAQ4wFV0WCNKtwDZNIam%2BvRew%2Fnbyh3iWhJvw2b509JZkCqbbTYT4CVGdleM5tuG6aWnWlmguN2bl4jmccpVZjkRIUERMFAsTSlqTcGrFjG2rn0VEdTFi6C5JlIn4IM4T9B0Mh5%2FzU8odF3pte251uyHyItuWYDSZhzH9wNX2YDWLcM5zzgu75pIPcy3HwoEWhjZyMbRh4gI3QJnIGK8ZDXVoZeOk%2Bu0aS4P8eJgwc5CEAzPvEcbiEc9%2Bsm32QImOb7qKleB8uVcx6K4dvrpLmQdKyY5kOXpeGju49KoZCyyR4DNNj7625R5tCxNXG%2FXghpNq7TqpqrkZB1qqiSthxojP6GkROC1XQboTFWGDCQruOaUFc6N9RtvS1zkRlMI96x7zsXP3SL77wxe%2F5FNscduN62gUBInlB9y5ztayFo3V3%2BD2lA%2BAR0nZ5eg4q7Gxk2WYviPAy3HcoAYidwAlUSIO%2B2QWRZIbjdCdakjY5P%2BL7T85GxVFF82wVJTsnbvgI5ybFhC3IrQV3J2Nq07tiHkW89DXqGVz3PpkHUQIIuiXzHzQKGO%2FvDDWDPHs%2B5pwI9O0vmKAmc7ZtTAdouZ%2F1pyyZKm%2Fmw7HxrgOam82yKDlfwbTMwksa4s4kzeNRX0PHOy7zaLJsw9JP6vAY6pgF4VqpGXdUqDM64r2zGAV4Nch4oLPZlkJWXAyjBUySEJFDmYwuKfrxVnFILATsmuAJsBAjj89IKET%2BxPwk0AvdMe0jKjXGgCa8vtA1bXc0uxFUA2BcZc54UNgCkIE5Lk%2FiA0XhRCdSWRhB7lRnjbWnoe8S0XZZnI0Qop5ET8wAoBIN2d8gNldpvarcQOHMTdJ%2FSjt86Wn8gwNCgVoADTjhzbvatasma&X-Amz-Signature=2ac5ae06d236faae467373c18260f4828946b5a868c1e452aadc98d5af34d13c&X-Amz-SignedHeaders=host&x-id=GetObject)
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