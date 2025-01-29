

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSQ3EPHJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCL%2Fk3Zdj8VciCeD2Wzo4u1uR%2FoA6kyXv2K3m%2BFaBsWaQIhAL1NZlfsQU%2B0hT%2BJ%2BGXAWsImo998Pj%2BDAY%2FkIuKc5l6IKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwebzHDVThrIiVhpwq3ANqP0Rj5NGnGpQ1F7qPnmDYKXyOth1nqMDhXboKKEANGxumBCUR8MU7cFQvjpXq%2F9N6%2FXAQLU6C80eHYsLMDcv%2Ba3nciYgxLUZ2%2BKFNwGUl3UXPWiKAj41mJeTsyMZf%2BdLOt6N5%2BjgRUbEcTbQThCx9byQZkEk2IJOBrKr1%2Fy0R8ZPTrX8Z2it9Dxi39if1UEc0euha%2B2m1mDMvuNxEFd8%2FeOE8Jk1hzXHQs9Pd9ErKszK%2BUv7CZkxZQcUQ6MvQZQRTCjwed4Q%2FoTObKywD06UGiZYIlsnnoxTuovxejyIhnF1oeDAMIZd4mHuJcDVxrFftI%2FkisPAMLGAAscykx7BoQIeJwpqFyY0asJYNXHkqPWWoYQlEgipWNj5nxYZWM7IAVmA6aDfA3FF%2FjuPqOoiXItNYspVfsHqv6%2BDmkLSoiEdSIO%2FuXGGsWbiJu94oSB8HXtsKykTfrZ2TSG8TJhZOJ4lvy%2B09f7wAAUAkQ1mxfaeArC6uZTHMsw%2BE%2BHvvaebeIaqI8tLzjp%2BezNbhmxyaI2TPKAAZfJjtdCNNJeH1kAFCYvmZxxfvltaaDHq9Vet2BhsEBYnrOhWBBaDexa5Aux56b1%2Flg1diG0ZUiBWPXHgniPyaqHaOBwGlljDRn%2Ba8BjqkAacN%2FPlLyXmR8trTQkM1zW3WGb7H2ExrR62gtX%2BrIRgsJvrC87q4iuXiSbSHCVlIqJsaPdIkMOTOmO1sz9o%2FLYEZT03zKDGPAZTe%2FAXFFnCPIcSlN8zF4tD78gb1dNpo%2Bjqzt%2F1q282msKrQ0AycLgCuzFBzF57dWjQiqEpmyP0vgtdBniPo74JLm%2F9uXe879%2Bu%2Bq7og%2Fo1kvdD7b0AIrwWE2RMK&X-Amz-Signature=051b1a10a70acc0dfceaf46a0050ed8263c8f68497ff8467405cd16a3e982565&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YYDK2F5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDbqKOquiCgS%2FNwEmJvxpvYHOF%2FE6VylolDJpHejRb6lAIgWTnB%2BW8vuXQ%2BUTn%2BqQJL2bzafwGCpG6e6I9CmrY1GQcqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3zT%2FGGSdCQu3dvoSrcA97o1GmFOvoU681Deho7%2FmHauWUMvc508XgXtECDupfaIZ9HOmQlhkklyRy9ia2FtEz4MIXs5L6sqQnWT8GO%2F0V7jRaSm%2FaQon%2BgsDM8wSBN0BYW4eCN0nuk34HAlunez1cpLYL8GsIXyNUb7RFGtO0%2B7I2TP%2Bq7HsyrOklRTk7SdEmiM7%2BeGFK2hVuxZJZQmIFyqbj77vbnd2Z6oZ5v83nud%2FBGYup30gGGh%2BS0NFQyFlCWC9uM4d0D%2F0v0rZ16nHG133kjh4VilKUH2zCNm7gxeQoKRa60KYU5LPnsNLdyWjDQn5pCPbTq7qt5nNMj74z2DXcw%2FsWuroPUDXOO23fglMFgd3QqP%2Fv9u1yjSv1P5EsilacHxC%2By%2Fj16fwf0VY7AEDIWhPDxVC9XPDvaDB7xRyRlyCRzO7oyZ6wwG1KKQjbAgHLIkjj%2FHvYi7ghEuKIdZhE%2BwuEaU2lnjTmqL4oRBYWipdzaIJ407HfSqpixOWfb83EmCo9GTeLg4IEQ3iKu0Qs7R7TXfpKWgju5kOfJ6Qd6tVpYk6RCYa8GYMzPVyff%2FyM%2FOyUQp%2Bxadlvk8eIbXPPzZu2jD9WI0nL5J%2FD1K0zvjHANOksnoA7R2KAR5FyP6%2BoV5T9PRzNAMLWg5rwGOqUB5vhj0sF9wFdoKh8hUnPjV7KzeGWAxnGyKTrYB8GWN6lBI8ZyLOGgQWE0pC2LSQ3cHpzPHtsSLG6FlF3bsAmv91bo93vOCY7dAf0ee5xOkY7gyKHXnvZ3es55H3CTMGLKrUWJKu7%2BSUNgMUCgQgheSQduQJSNnBXngnCvMtVPNoRZUVyA99Yrxv65USPkfCymDi62qYy9evryphpQ9ztQryRGgTWX&X-Amz-Signature=3173f8827d153c3c0214df679312bc68cb6ec75a7fa615eb761f05e500cac001&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAU3PMLQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCdHC1hT2cl8esvBQDLGwajb7w4z2XPIXPlcf%2FtuELrwAIhAP0jdl7y%2BjUMhRKgUlZRFyr8y1k%2BgArhWKV5IAo0wJMrKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjfgT0qSETyVPSIGcq3APXbUCuaZT32%2FN4L1VjxEo6m2zk%2FQJLUWaklWRO4RO5rPcrH80apIao%2B2vFzrfpWsVUqPf%2BsS%2BfjxwQ%2FaAY0Y3cNmrSQfNG2rd5PKI81lvPjNtFDE%2F9zz4EWDK0X11tB%2B3BC3bnqamc9F7HUlqBRFPyHZqY9hWoQfLgcsHQrB3Mk%2FRU%2Fmfiiev146EECX8Wnhj57EQRJO31RxpfWxTFHIOapNSi%2BDM7qB8Py49A4%2BpMy1Zg6lPCPYrIhoge%2FoPZeD3fLgwWuImRbua2jGCgdOSciSlmkuE8H5A5vgyBv2l5y54Becmdlg2F1VmsWdl6Fu%2F%2FIQ2xpF4EB681pcfASylWUrXH4N6WHTw5bfK7vdbHFIVFz1MVkmGEAEK1T39n%2BPXpNb%2B3gn4b%2BumzKQRmmC6ItLXXhhv0rO34%2FhBzElDM%2BmYnyLgjhF8S57Cw3smjljEp2KxffhsbnOnOZOc9MxCLKeiG6ZwW4NaA0c37AtfjKibNmMSJi8htz9IHZ%2F3yzlw9BzWdeo%2FGhfEazZyvhHfBKDQ%2FZkl96240oNQPuZhlp8JGx8V9ZAMa0WGgTl3jGPx6izxl%2BUpDDaOY3PvE5c%2F5QMyyc7IJ44baysKFH1um5MXF7rJjV4i6eVFtYjDXn%2Ba8BjqkAWAPw5j8Vqq4JJpPXIyK6sgoqILe3OZfEPF8aWqiasqiPbmAO4nfMUpUHPmaSeZAlvLsJxOAMf3T04neASmhm5dbKOQXvLbx9Gfd3Ywcq1TkK0qP830%2BLG8sSFsQm5FIYHvFg6YU2nfir0Rg5qMDxPhfHOOD1NSOLbiTWl%2BuhaJr4tE3T84VpHvUEE7O0n311yq7qZ3%2FX6iUaYfl5%2BTZiTotc5Nr&X-Amz-Signature=bc7e359093504d0431cf49e12ccd139cc14867d7ce84d73548bb521c1e0f81c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBUJ3E5H%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCiWZIPGRsI2QYaJgzfvwf2cRL0pshv%2BSCH8ZkJGDS5PwIhAJDpijrgx%2BZgTTpxxVJ4f3UpCP5urfHL%2BpgLKa1g1j8GKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyjpTD5IgOjoriDvc0q3AMLlAyWV5jKOrhcswsS%2FVJdcSeGVmCBt5btjhyWb9uJIEgbb28nCQhud%2BsJQwl%2BcNyHLHBBsAqBRL2XXO0vShvJga%2F%2FabpvRreavaRB75p7ur0A7YYSwCQY5cpYGGq4riZ9OpQjeiWxcG2zHtMXhBqPXMB9P%2BCnJgF6Q4PvDbFH3Yw2wDz5f3vdFvylgAUA3o58p%2Foz0iLDs4I0s2qD1CHTbGjnHocMmIScgUW5Xn7W%2FL%2Fg4nuywTy6XF6RS9GpHOAG6NLxUvEoGw55raNsJzD%2BZ%2FtO39yHJZWf391Nn4DazSi9zb9lPvgLXS8ZfQDlS3OzUqePssSim65uiFNM%2FJ1yT1DG%2FNEn65uUFzmHM5JHcf79vv0GrODaxNeniijhD45V9rTU0VturaPWJ%2BUFmFCUCNBOsUdjI85n8VXMyJ8OIAZElzb8DqyyqXAr3jc6IZdzS4wOlWtmni7X5J5vEF4Ca%2FHW7a%2B2SJmAash1gA7R10YWw4pF2YbcFIX%2BlfqQYvOOcjzKWy11wiXXBitp2pvNhc5wLB7XTnDsFdERRR3G0o988F5v9XeI4CRAuL%2BFrvd8owM1hHhN7aYTFaaBNujYx0Cg6ax6nAYX4F6dDNH1Av6DKxpYvZiOH0QfLjCCoOa8BjqkAUKpu3UD6SjPrk1l80%2FqinmDzWu8giemGNQETZCqlxJz2254K5z%2FuBT9CqXAnCLsBgeJ8ydGGzhxU%2FYA4nFsM2uM8gJfnXXL4OeGZ6627JE2Xqf7RDcudVtiVA6Eslr6F%2FPP0E6h0QyIvE1JCfHV6eKGjmI6pV%2Bu4Ab%2FmKNfHv6yJaejXi%2BXTVno%2FTRMpXCn0FXMOUAMqUMyZ7nFwvkMvbKMRjke&X-Amz-Signature=009673ae7f47f7e96a25038c56b4c72d407df402b19517781408429065810440&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QG4LTIEJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCDVdIDwgbobkMJd5QngyCb3TCFerymRV6%2FixBQIOomHwIhAPH7SLW1wj8dtBnOhOA9scmNePOYKfzHMxM4cbcHIlhqKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRQfhwCB5H2H80tMgq3AOoFy%2B9wpH7xRbPNTby%2BaflI7SRu0E5efcaPKzpavKeQlMVi3oUcSD6oeNLJKC4ChhsfLbAcgEK6cm2otyPPDJYfLkONUfxTnA%2BG0DShdHhiUupbL5044cMF00eOH7ZtMmoVilxdbkeH2nVg%2FfhX7uRdYgG7jLiV63cYXtWpDKw9TfwCiu2kKoJVfBcPMaKWIOAMhAkdzmARZo5pW%2BEeaRcDy%2FEHp0KN9g6SnZ2rf8z%2BhiEPe4XKq7eeC14OEniBnex77MtU5jB4tTyIfQFG5HkYqqs9LOaSP9aH0YHw6uJKtaPJus4vI7LKy0fg7b2epDkjCHo9lsBe9jwMarN7Ku9wuhdPkdtNYXB96EIVnLmCO1HBkdgP6h3PYGKr%2FwICHNkJNidvO4YcTGAL27Q8axld9nITtb4td%2FydCeSLcGncrY%2BAtdLl637WONwuOiaOEbdXDE6%2FPGHjGvXM08EXZoyrYE28dMVrDIPnzbIR6eGZZfwU6AczOmaOvapkUcRMmLsM5AsAslJt95hJAJhUBQ4Q41WIadUxjKieA5bTVw8vDL60ua15um1RIWabcfU%2FhcRd3qpdHJF8zHYlsL%2BCT46bDad6%2FphF0VR9aSC4X%2Bq6P2TVREMUwfcLrk9pTDrn%2Ba8BjqkAQiYPw0udAb7n2hz4T4lflohS5fCkEZ2RMjSN8NiqmaAu7eGPpVj8EJulfLaiQl8cTqTcWtRik0ei2pOzHtAB3dSNdj9Jtff5Pd2%2BNK7n50Yn5gfX8mcgQkO%2FNJeCUbMDhPMtRPF8qnOrf7AJsjOJEa7CqmB5yzkKJ1Piv%2BlkzuSHp0pShD%2B%2BbjZvITSIVGmPbbS7w81bKx7OmOhMXM10sQLQsdn&X-Amz-Signature=0a6e3582f348fcac2e56f2f184473f853757959abd209d40484d0627e130039d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZTQRHJJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCVr0YodXEmXhDgrodn1qtjwGYM029pa838OzuOWebCfgIgUJb9bD2GJMsY58NgIdWwoSxPv4uOQW2ow8Ef8mkJDEwqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBY89CeC%2FJ66NnVQ1ircAzx3yoVpBSjLDmO8na3ILt%2FeUJyfmRIm%2F6MsmevR8tk1MSSlz9drPKzqVYouF942%2FZaJziRzVzdd3iU9YM03577MPBCTavryz3tyB7m3ppCmwdrULnD3unYIL0iBi52PBHXeUo1ZbZAniYvI4OROIkLkbFm6k9GNFrdYzsVWhT9cJbeGW3YxJfjYF3AHCivTCHWeMdNejK2iaxO63u4tIsjishMqozWlaBMJwKqcGRL0jiRUw9%2Bw3TcmHFTRB5qImIsGZV3W5RlrrCNp6kwL2Lr%2BkF8zK9fPjgqLS8qi0YgCRmWykmTSQgvcpGmntLiJsH6M0zjpO8RBL0J8WijKjJxAPnrpGVwGuXJAC50GKjdRDTrsAzYhAGDgcfuH%2FeQJCLywzpL1EozA1g%2BHY9Z%2BUljr9Y7aXWa%2BxNwWwQgx4Txx7V%2BKAQb3n4iRjKkYv7P1o7WH7rWBXScUBXu%2FH8%2FVww7PrSxv6egCeaBWCtg6Zg87ur1czAaPCyFz5mrT06V%2Bksu2koGpAKPMk6ydcL2GfRstFvu3QJQxfibMKQkd8ZuIcMDdmRo1O18rYeoRwfZVtxMiiuBy5Opt0xtm0chRipNLssVXEdib%2B3w7fnHKWX4%2B51vx2OXEPove5aprMNef5rwGOqUBhwvLBudjemNnhJ%2FUeZ6JrC6BiDXzjIf3EjG28wcYF11qnEa7xo3RVe%2BtT%2Bgf41flaChygiUvF6AHphnrQefbT%2FZm14gp53h6NI2n06raxDkHJZ%2BEprcuuYzEO4glaXZR8RU4zC3i0QAYVniK0GzpnUEzaFy1lGVM0mO0DmzKHZUmoQiRhTT6IzelJ3jzDLPTjMJUNlAh1ig9p2ZnKWoVuCZUizqs&X-Amz-Signature=626b62693c0535d4f93a578a09c47f68562191f6087cb85128b5fdf4d25547d7&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPI74WCQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQDldSQJps5qbHyIfAyjzssLDo57Hz6Ryma8iQD%2Fkl31MQIhAPVY7RUrIDHFAl53Cdqpa3VyAD%2FntbUKexpYZT2ctnXVKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzrKL202%2FQpKx6K6jUq3AMGnin9cVYCoYqk9Z8wsYyzfvkBElxhdLWqx65CHaIPJd8TfuifUg0n21HIY2d94RqiPxLpr1NZN%2FRZX%2BLXJmTKdUVKiDjDrhEOJCcSgtTnzz%2Bl0%2BQdVujJsv1GTOzFt1JWzn3%2FujpH5SfhpbUXh70e5j97qDcETCqSTrcBv832y3CIvzmWCUluGiYISgfslWUA7CwQTaMOzn4zFL5%2BHxoAsRYLKbbg5CVrpb07C%2BZKHVP7OWCGvYeogxEJl7%2B5IQ3YSzf1G52s5SnHFzmK%2BhhTw8x%2BaxVljNw5Z%2FAc%2Bw5yuLZFdHiha4hbmbn8fPsMP8ZFj8JDI9Kn%2B64AEki%2F4K16yZbH%2F10aXPRM2H9x%2BFFouVSaIXYSiN5cAPAZ6261SK2NIL3qrn83iYsjfO%2FvsdExboMUuhfVYU4QZB5ozIxm0TiMWpwRSz2kgHHnCjafENxZFKJU9QHI%2FN17xV2aeJrecR7aX7MT5xUkSNr9jgAW5vCQhh12NGzI1hgJIxhrRhiFiQLDCsUdDxU7gg82cFofBwqIknApRo%2B0V9%2BnAqXzB0Uey%2FGcXU3Mq38dOpMhOIM9zD66eiYJhtom%2Fp3mrj%2BDUj88BJKepXu5BZBsWoy8xc8A4NDYcFazgAdTLzCkn%2Ba8BjqkAUH6SOrCHGACv5ecgQraZk3aO00chq%2Fm4FDfYAMY%2Fv9Dlme%2FZvuwE0R6QNnQNA%2BDCaCwgmsoTp55VcyQKcejXOduKZyZ2zbv%2BGRUooRTwRJLjEIPzC6J%2FS7oXeOUhiYmAAAuzME68VKdx1kHES5fNj0YuuwZ5mq72GYI%2BGw2e5NxHOpbqo2Muomg2U%2B28UirlMPZmi5ZWIpWRYvDwzlBVoXq0prk&X-Amz-Signature=59d118b892be0bb2f1e1729c1bde337efae860874dd5477f3247dced39bdf303&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TKFMRQK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIBIP%2F0SO8FgpcjF7Hd4b8pEYVOVkKMW3305ZJuKn1wmiAiBppYEWNwKIbQ%2BUyv4%2BWHFQT96UgFL%2FnEM2MCRQwyd5JyqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM75tDlIUAJo3PQJrZKtwDXNz0Zwd%2FbkL8S8hy4eg0b8OrDaC6%2FWq3vMZxlPwVVcZE%2F998qiNqdHMRd%2Fglvl%2Fist2n4ORdeHlHD%2BXb9o8NSUDjM7ngHDKEVddTup%2Bj4VwZTcU2Cr4rDojoETZj3NQH54jK8AovR040XrAd927sjpcemzEipIxwfpvM5KibvFtdWjZsTrFuurC2kbaLzOWWGW8hWclP3D53zsuRl9Y9FQBkHJrDETDsh4fPXIYwcLroGC%2FiSzTDL3cYjV1%2BFpv1nMsavxZ6N5bZMNCENgG09UGWdV5USXPcH3kOLdxVbFz%2BD%2B6CNLMpF0Gy2XekRKP8jBFN3DFrwVVJqMek6EN%2B3I9UPKrLE7zt6vjPcVm6gWBnssgI8NlIl5TuAaA%2FTbfdOHMV8AXNPXrqC7XbHQz3lF2QtrI6dMd9b7tddVycwvgkV9ZGJnbooskBy%2B6%2Fn5zt1V23ddINDFsvP6MjV1NSQSdZv0blsC9bP3TuqSczyakZjZFebG2iOJN28GZWXF2a4kWUDaJakw3CzDe2fSa7EDLvUk1lqE0zr%2BrPE8YpdqWsH6fbsIufyO%2F3lnzL2XVOtOpNAg8X9HWURB59ujSp8pzNEPTrnwpnF4Ir49mQcGKQZ%2F3DSSf8S3oHU2Ew8J%2FmvAY6pgHG5dYiu6dZOOw%2FGwk%2FdWcnkUBPPJI3iFJyf7uAM2ngAT53K%2FT11uEgNidAKpQXV5EXVV7EOgjoGuJ6BQxxxl%2Bo2sJ%2FK7RvY%2BjX1gW7TRuaQZGAkHFCCz0n023rWg7rjHVhySUzVE8%2FXM8d47ZvYnq95GhIMAJbgjaEj8gobI3Xny7YGes7CuV80z8I1WXdsCfGQgkqAOcx%2FTHP64CDh4t%2FHtEXu0jl&X-Amz-Signature=1efda54179269087af0cb20ddd8c38b04370abfa1a8acf63b5cc4151705c2a07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QG4LTIEJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCDVdIDwgbobkMJd5QngyCb3TCFerymRV6%2FixBQIOomHwIhAPH7SLW1wj8dtBnOhOA9scmNePOYKfzHMxM4cbcHIlhqKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRQfhwCB5H2H80tMgq3AOoFy%2B9wpH7xRbPNTby%2BaflI7SRu0E5efcaPKzpavKeQlMVi3oUcSD6oeNLJKC4ChhsfLbAcgEK6cm2otyPPDJYfLkONUfxTnA%2BG0DShdHhiUupbL5044cMF00eOH7ZtMmoVilxdbkeH2nVg%2FfhX7uRdYgG7jLiV63cYXtWpDKw9TfwCiu2kKoJVfBcPMaKWIOAMhAkdzmARZo5pW%2BEeaRcDy%2FEHp0KN9g6SnZ2rf8z%2BhiEPe4XKq7eeC14OEniBnex77MtU5jB4tTyIfQFG5HkYqqs9LOaSP9aH0YHw6uJKtaPJus4vI7LKy0fg7b2epDkjCHo9lsBe9jwMarN7Ku9wuhdPkdtNYXB96EIVnLmCO1HBkdgP6h3PYGKr%2FwICHNkJNidvO4YcTGAL27Q8axld9nITtb4td%2FydCeSLcGncrY%2BAtdLl637WONwuOiaOEbdXDE6%2FPGHjGvXM08EXZoyrYE28dMVrDIPnzbIR6eGZZfwU6AczOmaOvapkUcRMmLsM5AsAslJt95hJAJhUBQ4Q41WIadUxjKieA5bTVw8vDL60ua15um1RIWabcfU%2FhcRd3qpdHJF8zHYlsL%2BCT46bDad6%2FphF0VR9aSC4X%2Bq6P2TVREMUwfcLrk9pTDrn%2Ba8BjqkAQiYPw0udAb7n2hz4T4lflohS5fCkEZ2RMjSN8NiqmaAu7eGPpVj8EJulfLaiQl8cTqTcWtRik0ei2pOzHtAB3dSNdj9Jtff5Pd2%2BNK7n50Yn5gfX8mcgQkO%2FNJeCUbMDhPMtRPF8qnOrf7AJsjOJEa7CqmB5yzkKJ1Piv%2BlkzuSHp0pShD%2B%2BbjZvITSIVGmPbbS7w81bKx7OmOhMXM10sQLQsdn&X-Amz-Signature=4b538af58193da0375a95befabc1c22ff0ba363aec9bf2183337ed7722a2472a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEEZ7SE3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCjC1HAELPHhOPEmrH5ecigJ1qGKGWO2lH0aR0iHi8PFgIgfLa8Ds9E2N8FO8xGS1E1VCQnZWuc39LQUL5QdgeWnyAqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEC1z6wg3lA367kxDyrcA9ccMe%2FtwxaIoupQIcsGoxp5hDYbnHT8suxgGvT5XjvZIt%2FmWTCo1gEpAxavYPV%2BEI4H2MYqGiYgJAWJqWpWSiwTRJ5Yr07ukd8Ng74m%2FdFSdHLs%2BrakNYctG5n1HgMtOcV1s4ph7jtNJ%2BkUh%2BvQz2H%2BVrB7YwwbkUdSK06RCmtT54BPIU4teTo%2BhheyIg0taaJyXjR7FdCcQZTay1qI0v1e3CxykEu1bcO8vrnyfvz8M3OZI5Anagj%2BaStneWh5WjONxAGZATa73Tik1qZS2hxE7KH4sNZ5qViNZG7KculsA1LzIHpn4M9c7SguhwVQvX1Hp0qYUDbcBlNGk2CXt8qgbJAHa6Ba2mqs5bFcIWSL2lhgwBKB29bOBIxUNoDlS0LgBaMBgZeXB10rTWDbz20Ygd7Pv7gRRo3wS6ytKaHdsQkvd%2BJkZ3bsPmjrG3WU3DJqA1Bw%2FzNksYcYpCRVOa3Fh%2FqB2O9GEBI5Y1i5QhWkyAEidVrn08FW4ymhs%2BT4h0k16Z8pyr83eMfqxakpZtcDBxHpsFBpSXQaunjUfWZKpsJL61v80m6qCLfBFEk9HI4RlFi4WAYC77C%2Fx1XYeEUxjzc5lLEr%2F96hfqfZYI6zmPQV68oKZTczUEq%2BMN2f5rwGOqUB%2FL2daU5AuPD3rlZkr0ZWQlG%2FW%2BapcCF7rcuJQmGh%2BpfIFWOfqG5cgFOTejix6SQm0TY7%2FbzhKt%2F3kN62Rb2H72C%2F21HkNGSjtHGjFIZiIOvpVcfTnOAA26e10pDPIRITt%2B1iQNXkRZdHo0rXZ6JW9bqs8asGIGtkI5Hw8BQZWaUW18zc7SM1KH0RNwuz%2BDGfmlFuT2FsQ5dMsaVYDuw3B099Y9yg&X-Amz-Signature=bc8cf66d7972350c5b05a9f120e00404c5528980d7b733c53bb8cc473054783e&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEEZ7SE3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCjC1HAELPHhOPEmrH5ecigJ1qGKGWO2lH0aR0iHi8PFgIgfLa8Ds9E2N8FO8xGS1E1VCQnZWuc39LQUL5QdgeWnyAqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEC1z6wg3lA367kxDyrcA9ccMe%2FtwxaIoupQIcsGoxp5hDYbnHT8suxgGvT5XjvZIt%2FmWTCo1gEpAxavYPV%2BEI4H2MYqGiYgJAWJqWpWSiwTRJ5Yr07ukd8Ng74m%2FdFSdHLs%2BrakNYctG5n1HgMtOcV1s4ph7jtNJ%2BkUh%2BvQz2H%2BVrB7YwwbkUdSK06RCmtT54BPIU4teTo%2BhheyIg0taaJyXjR7FdCcQZTay1qI0v1e3CxykEu1bcO8vrnyfvz8M3OZI5Anagj%2BaStneWh5WjONxAGZATa73Tik1qZS2hxE7KH4sNZ5qViNZG7KculsA1LzIHpn4M9c7SguhwVQvX1Hp0qYUDbcBlNGk2CXt8qgbJAHa6Ba2mqs5bFcIWSL2lhgwBKB29bOBIxUNoDlS0LgBaMBgZeXB10rTWDbz20Ygd7Pv7gRRo3wS6ytKaHdsQkvd%2BJkZ3bsPmjrG3WU3DJqA1Bw%2FzNksYcYpCRVOa3Fh%2FqB2O9GEBI5Y1i5QhWkyAEidVrn08FW4ymhs%2BT4h0k16Z8pyr83eMfqxakpZtcDBxHpsFBpSXQaunjUfWZKpsJL61v80m6qCLfBFEk9HI4RlFi4WAYC77C%2Fx1XYeEUxjzc5lLEr%2F96hfqfZYI6zmPQV68oKZTczUEq%2BMN2f5rwGOqUB%2FL2daU5AuPD3rlZkr0ZWQlG%2FW%2BapcCF7rcuJQmGh%2BpfIFWOfqG5cgFOTejix6SQm0TY7%2FbzhKt%2F3kN62Rb2H72C%2F21HkNGSjtHGjFIZiIOvpVcfTnOAA26e10pDPIRITt%2B1iQNXkRZdHo0rXZ6JW9bqs8asGIGtkI5Hw8BQZWaUW18zc7SM1KH0RNwuz%2BDGfmlFuT2FsQ5dMsaVYDuw3B099Y9yg&X-Amz-Signature=cbdc8bbfb177d32c00619f4e46ea2d4cbf6f0e6351ab8ea66a5fa816953f7703&X-Amz-SignedHeaders=host&x-id=GetObject)
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