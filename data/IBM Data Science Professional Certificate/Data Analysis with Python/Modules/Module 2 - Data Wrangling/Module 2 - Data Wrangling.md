

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCTFODCW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQC16gttToZ1BYhbn5fXy3pUzx1F39V3XEQ5XOViXRH0RAIgPdfDHjKkB4VzaF0zjQjlplVV%2Bs1NLmL5HhwoXvGgX18q%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDAA4rRln4o5R1FTvKyrcA1HwMM9azjM8y%2BQfI7QcCfabdLnOXdGheDYbM6YpWUqTnYELwmuXlEFh4eCtw7Ux0Jq%2BOuJETSQ%2Fs0%2F38xRCx2UR1V0%2BC6VAUwLXDTqDvbQEgLmhkLSdYBvm2hPqNHs8XXD8h9TkfKmkDOmQbKobWZyeP6Ifg5g4Vo15bw8u4WbQYPky%2FhwDucc%2FJEg2bhE7WSCd%2Bx3seqinci9M%2F567RmQ69E5BdNQSN309D3TtDTd8IxruyvY%2FYcyVxbGNT34LiJ0o6nKr%2Bd7SMubxsb3VILkFqr1e6gPJunv5stw10nWb83PGrmVHwgNF2b3IRhvzALzx4B98CvHYE%2FCI8OxJ1LrnE39QE4e9JoiJ00JuIjJQxas%2BsuHKtO0QmQAzG0RmroUtIUjfwoVchlZ39dH1PL0QEfcn%2BTdfxDe9iwNp8wodEx0iJJFzCkiXuUQK8h4FxoIDONVaMU%2F11QCRjLyn7%2BWx1IO3LG4%2F4nQc965CJ4Qw56AgX1kNhhJqvge9Q3aB%2Bri3ncpfh%2Fbx%2B0yueoKGbSGkc5GgrtmKBHky5elSw70RtzzURErJ%2FR4E%2F6Hu5UMsVeQdTlTpV7vaIxVKdtMIzSNsVVbW2pE3Cvtzbav6lC2mcOXwSWasv%2BkFD%2FErMJ6zjL0GOqUByl7J%2BM6rIpf0Oz9baaBw2%2FAcYJK5vjAOn%2BAoS%2BWuSUyrd0E0KL3f%2FMQ%2B%2FKNCBrkWG2ez6KOeaVpQlnZ7haY%2Fdhy6AHAXnyJXTbSDe52Pv1HDFL9slGg7QmZovuNYKZpfqTGyeTZKwonAyDx358X0geMjFoGQdxoClzY4Q1IMxXpqWTSgd0iKKla8lq7OU9DZZFsIXhDxlaAj9thVYkfT6HP0LXyJ&X-Amz-Signature=85bfc7f62cd148f658923d4173278b5836b04c0a103404893a767961e972715d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZXTQEJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIC9QxhXf0jQoakWR8vKA%2BHFH0C9WIBxHNemZEQ7jBBAaAiEAnYBoOYby7ItP6AjmK9yPmtUBIZ%2Bf5f0HpTQl6HNrJMUq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDL3yWi0lMo1sTRuXoircA1VqSRFso5%2FlgnAH6ed2AN6bV52HSOni7vmygPeqooJZ7LmI2UProeajSobtDUqK%2FM5GZJuWh9qgLugvJpqqnWdoVGvlfnxG1Ft39Z95yuLNOBERVY1r3q1QI0%2FrnmkeSUafxRu%2FIF2BSmRiGWqQRduw2wjBxMIEibEDY78jubQl9M%2BZjwq8sYSv9lJUqcjcE5BypRNRtZELogPXa62GXoVVxdAS%2FxDszLEsvom%2FEnafimTGh32DxA%2FBf5TN9IrT6w3dpcVPHdo5FClZ3z6b9%2BSIlWEvMtQkT%2Bv3Ywsv4VL3vu%2BrIGpSdjiqfSmxeXjMNth%2FYte04WviLfJiZpFTV7cSb3SeTZKJGgAGYeHfSvN4WyPTcrXwumygK8BlI58llP9rswcTYDj11ljnvoyqYH99PlMXBPjMZHk1vfYb0hLp7MPfKhVYQJ8wAAIHimR%2Bkq4dJoBJdkmy%2BczyVsyQKj02MwuQJ5j6faY%2BErErAzbsc7O0TFMKaRswnln8%2FZTvQQwFzYMt4%2BTVxbO4AF9iuEyl9zKKgjZUQ2UtbB0FwQwAgqWA5bMyjgX1Shl5c%2BlU%2Bpf6jFNs7GnMz7PF3kPKjJDCkVFbAVDGedF3BQWJ%2FZDjFDx4emucpw%2BCQnKtMIy0jL0GOqUB0eJx6LsSpWr%2B%2F9t%2FekbtqBlYVX8hrH%2FBjVhUGv9GRnJGDYbipYFEmpC2D57nXvOcziLaNNZ5cxi1IjC%2FvGwAZsGxFsI9ic3I5EECCkur6ZxXBbsxtD7X5fMEkv7FJnMXzOBiOKjxhOPVPyMr%2BECtgCFGPQtgUTavKWAc8YN2HivYlknYQpNBtP0qYxdf%2FkvtIOTMa%2F%2Buddfmn8QftrfMGfqBr459&X-Amz-Signature=43089779e6cb77153f331506f58d1926ac585d83688936a4d277c4e19843df47&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNKSKC5I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQDkd0nInvbnGyVAQoBogowvywc1cc4QcjATnNAcLlxDLQIhAOG1tg%2FBSJ3GGLJRXgapzFkYcVrV6pSBoxRp96Ef3%2BRWKv8DCEEQABoMNjM3NDIzMTgzODA1Igz%2F7JgDBeYf44DnF%2B8q3AMyvMwxVfkbYETju5XDcMBBbXgUBtI2dRrBzNpUZ%2F4UUZ%2BeRIyMzKdLsJSYrt2VdE2jJXzJSd7tE33PMh8ItINWYvP1EhNP%2BKyE6A1pWzuwM6CVu8bySiZqbjgMCMZ%2FUxod7qGl3H9%2FqQd%2Fnk9tt6nT44Yct%2Fl64p2dnj4MOP3XpxPHYSzVgH8AVHh6PhN9KlHSfBWncIOnA1r%2BtJZhzFvbHJccu6kO51n3%2Ff88Ce88%2BMcr70LQEE8RQSprC14WULVRcrGZ9xp%2FO6F2lwAbU2b3MX6RrZz1appgyf9lypqYDkmDQ65w7s37m%2F2E5Z8%2FlOk9lOn0GRs%2BIvM4KWPrFrL7u8g%2Bq%2BS%2FuhGZaK8vvzhj8OJx3KCHtLaqT%2F7eQL9WG1twUWVkOjQaqJlPzSVtmZFDsgdqw0%2FTOzmyaHU4Ja5YlH3c9nm7A%2FVV5duuc7I1DYpqSHb4LUyphPJZZIN1hbwg3rpexTYnZREJcgvg%2BL8hezF5FNpOQNGD2KyHlIgEdXmkaK2%2FC1ZQ4bffVHqD3rdC21TRFDkwp3Ywo7XwYygnasoFqInWq5S1%2BnogCzz7xL8G0YN0zR5XeVwDl%2BVRWWaz7y1w3Lu%2FkHaa%2ByLY7EEQIcB%2FXpTVw2bhQRSuDDD7s4y9BjqkAXHAMG2iSJ08pKbBJA48gSCeSiT9VViVT%2Fx71SxqTKtbOAowU5HX8X%2FAE2cTwBYAD%2FiV%2FTJcRxOiQtphwfp1O%2FBLiV1bYKaJB3Ba64h69ttHW%2FX2GubH29WgVFpyCa2P%2B7fbetq73p8wpY1JKoHzNJry6D4ywpNmD0UpurCtEA1qkxO8nOulYCfRpgSV%2FrCk5pgxCYjqEj0c%2B41ilXKskgZ3BtpG&X-Amz-Signature=b653a9539e00e401e969422aef112fc8f0919eba3c0e50dd9332553f0120e87f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCINCMN4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIDk%2BhCkwGQ7ZLEOKmVDzPFCHzN1yBxZzXPMy%2FU1p4ji3AiAtQ881Tkop%2FZmRngKdB3BaDtAMruZIFehuxzOqFjRksir%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMsWBT87cVdPP%2FDCeyKtwDv3PvTDsP0mIs7D1uwJOpBoubSpw9oynsy66RP65dDSVX4UDMP8bkJwMbpTCJkuaQe9tPiE1068DUqIGrswYeLeC%2F8NjCDbTM7dMi2NOfMbpGSXXlPcH3reVY4zTpx1wVQw%2FNebOYcosERR9gsEbHCqZXXOUnoDeO%2Fb3CrNs2gtzp8ld%2BIwbbR7g68M%2FUUzDEMxQtAup68tla6%2FVDdKQWuMGIZh6kokOZ0MEtz3OkRN0N7wLYpbItFqMYaktt5qtMWcUFuJnk%2BqpuMfIOrYSD%2FG%2BVvsVTuVldDtpXIKtp9WpLOUm8PMtCN%2BM%2FKtToHiRAhe5OJve2Wahmy38TJGJ02QKAPGjEuF19QX6Ol1f4oX8Bo%2FyD0ZVa9WGrY5CHxsqpKb7KPID9pJChLrjABlutl0Fh8enDADQEpCA88skhW6I1XafQEAVMn9UOa80PNGm%2FqabOSQYLUJdwGlBu%2Bld%2BxQKgelmJXYyUvpBgDJYI62uLg1Ov3Zf67TDDsGZvvnhuOc6cfzTy%2FP4Ak7bmXSyQDL%2BmgqJhqTQsUQxX5WwSd8XA2SSDrq5URBnzT4Muouc9NdnQAow1%2FyQhCcUIGpebFdmAMU3YwIgbrK7GcXu6yfHeqfJFosX7fsimPogw27OMvQY6pgHfTl1cG5U2cGnhPYRorphsziqdyyP3NL%2Fz8XbXQE%2BlRDi39NSP8RMkxj1%2FFQ5CkYsxYGTgRKH4w1muybBfJ0k423flb%2B6JiLCV5W3tDfsVTQ46jWFlpWxx%2FP0dv5gj2IHfz56BAuwRNxuqncj5gvKl7YIlJqIMivAkO4dvPqWJ1y9dncOLlNcV9zp2sukd8ciz5miRcBcGM7ols4WmYXPQZYnIyJ%2BQ&X-Amz-Signature=d6aab5c62f944ecc876951aab906abb8870d93c20a7ea274ed8b93944448d832&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Q7LLXSA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIBa8OuBbN4gLmHt8UtzGbDa0QAm06ksm93ZmdRtWHk%2BFAiEA7%2FbQ4I88xcQPsSidmEB1RuPLRV6cymV4XrNvs1qm%2FWMq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLWqmJCcG1%2FI1ZqWcircAy6f4Ngh%2B8DkoNQFVzxEv4urRXlMCgO7VECOaqczRjR4MySoDhCe%2B9lc1FhyCjVXAXK4bV92d%2FH9dmKGeiliR16MSwt5qHJ0Z5jsmeoLWyHU7pzpjyvDDl%2BvJohYhFdBHWvGg6M3k%2Fgeu%2Bf0EoXFzNz6FMOuivN%2B1fMFnNVHRVx%2F5sOgBRZOoqcnQ2Buku8LjUcSMI0wu7EqXaAYtZJ2h7pLDPMvJ34m%2FnL6XEcn%2FMvhJq1vbZ4uL8jQL6%2BA559B6OKD7ZLygblvYPFi7i%2Bjqa3WirSU8P3ypYf2SFwilET8H9yRBV2bTjCYggNT1lFELJduV7uf44BZU6Zwn%2BmHmCLyD006CVsfqKbY%2FzGoG7BvZacKvmAgiRk1bAWUn3GmtUnilYoPZLM4bcgCQ7wQlij5JK6cGveisqvnhq4UeIdZGcMDwJgpOxkZb5htWnzwIE3twOa%2BBTE4%2Foe7tzYpCSLub4CMhel6bso%2FNjprFepuS9wm8wjvbU9CYBfJax1xpZBEjqIoIUt8rrzG4ZbT03yhVhTf8IYfZth4ah9C20MY5%2FbhVXc36HTQP%2BOeAbFe3WpL2FtQEw34V8duNIgeMo75wTJfq%2FNKZ14PoBUxvU7%2FDq49H37cV3w6s6tgMMuzjL0GOqUBo6rsjFK79V5XVlF3GoulI39r9WRi3X1aiK%2BR8gY01PY0XgIgP6W0IFPO0AThCajcXrmGQYXCtYafp9W7cH3s2LC2U47LS2ey%2FCbDgCawLO7USPIMmkwt4VWE4OW3amH%2FbMYwsyMDNoaSUGKs%2FUyPQUfZcI5lin4FBSJGoewxzgjZAhym2V9C%2FwM1zHstsoPp8SkGvoV6geJF9SwFfruOwhc4Z4N3&X-Amz-Signature=1946d6937c9a3d3b4e1260a9178f095ef1a35db287c44fb939bf2dbe6c75c701&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QMLZGSH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIEQfIUIceb7h3B%2FUNGvI1pMx9sZwfl%2FeBM4heXamR0e1AiBVCsJ%2FpA79V%2FP7RHjzJqLMrW%2B0jb%2B516rpE3G8gRT4lyr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMqP2d4jiZR6Ka6SjWKtwDshx8wHz25xXG%2BOv5PJqedF9SZdW903lgBP%2B%2FRI7OuI8vOiz1RCMkJ7MnL8tuzkKovh4AAmmojc5gBMc78HKEx70JRHKHxF7yDPxDSNL1eHOu7ISUsLSYBLFy5yuRLt%2FmZL0Q9i4NCvVZOBILarGCH9mVy6tn%2FAWB%2BP0qFyOgiouVxUqpM%2FQfG4RINVkig2S1ujYxqF7jGVd4510GGQ1v2pGE2eFjwQe4xRfZvuke4CjbfX6vvDZ3dZm5DzsrVgiFJuPbCyZrYi%2B6z288Pey5lCOKKk3RW4gpUVv4IhRjHdAaFR4LjMUQPDwhuh3tfWe9fZprHOYgepc7OkBb8ixkq3aJm4lbJRCrZAUcBUYy%2BlgJfS9Y%2Fmhwx%2F7koGVyFiIB6XV9sYhYdzx3w%2FUyUZxdRZ0EvFMHFs7Jxwa2jMUZnEqTfrsN3%2FKCD7%2FyMm0nrGp1XkKUNsakHTGfUL2bC%2BdkgKnoK6FyFpDT%2F79fhi2P2C4baKoQAfpMjDd%2By6diZkJLuvXuqoTXaTXpoO1w5Qcx0RIYxm7lgy64CuszcfizX8aGuS8jEMPmEkDap3K3lh3vycSZnwPpWsvF1RrCnMz5ERRfB%2FLxDUV%2FsbIu4QKOrnlT7jM9DmGkTl0rBRgwr7OMvQY6pgGKajfdz8t1jHq839aHA%2F58%2FuNxyUZnMuNd9JJtfkFpgWZzqJUo3bA25YC5VDtyYwD%2BJ00KxAohUC1EMW8M251DcyVjg56wijBqi%2BkBb%2FF8t2cOcadUkA%2BZsmZ9WYPOffJoVfO90Ky%2FpB9nIhbCeFyEa%2FVBovW4lW%2Fe4A6VdM78bkgnjpKZoQXgUFoZ5xcRCWInzq3OAnoSNY63Vwik3ELxMLdfROJa&X-Amz-Signature=68924babc9e21bcafb4f073a828afcd73ff87611fa179f992ef4187d6613a928&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHXCJ5S7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQDlJtJ4CM47eiDNvIxxtKM90Z4rc5kX7i710iC3xi%2FL8gIhAKbr6ShjTnu8o7eng%2BrpiC3krI0wlqRD3Ps8A8BiCbRjKv8DCEEQABoMNjM3NDIzMTgzODA1Igxj4BCe4tc%2FoAfTcioq3APIXYCCUwh5cXld4KWXy6lFFJSIO7q68mZ1UBZePOqRYwy7CZTxDM9nw%2F2vrb6UFbm%2FaE1ofXlkWWuWBhcKT5pYfFHYosxsBRhH1IauIr15her40pbtmpTN9c%2B%2B3Dg2A7LU5uSEFsFwP5RlJnyn6vNV4vz3ysb9Z2j%2Fa63zaRkfWGRGF4DcgkbkIEnJYNSRkA5wQOaQK2V7BBsFqj%2F9AWPbwjDSkk53i%2B8W4%2B8XEkGxDIaHhqC9S94czFxhmgiQaL7Tw3njj4HjwCYIVTljwBQiB857I%2F1Hj%2FosY2ivqyy43Pn8sQYz5bW5m9Eb4CN7DRpiVVPxNXMwJ2aDdAV37vkzDEqlFbAB7diVkpxjXmqzr2gCiFbB0bVoaF%2BNWDd42rLwDhH%2B3ymBESPXDtzG1c8e9DD0coLO8WxF%2B3BqskhK86gxQ5ssrCLek%2FEdiWgKDtpux1nYb8QVHB4nmeMUQ0MK3%2BaBM%2FyBBNtnz%2FrEjdvcARnK9eReLdxSRXCeBE9xp0aCUtXOFkBM5F72AZp0dnx%2Fjdp0pdnf0GYss4YFjY0A1u1RJVQIA1tBopTEOQETpRSErzC%2FmShKsfJXJE%2Biywn%2FcCIQa%2F1abNFJSN5odfz9AKd6Vehlwr3LRajuIDCWtYy9BjqkAQONDEBURg8bh0GjCiDXVNOLi1IliPCSOrjWHGu9vL5mp6I%2F8qD55EbAvLRy1waCKAQS5m2%2BxAVSRPb1YVf0uPpT%2BhoOzTIy9ODJALCUVZxM8oNIdQLYKz1jBvW%2F17I0RHHumz3%2BFGOqbgF3nYTPR3Das%2FoRyf6isJApjHJ4nOvvDCmgLYrSgP24I8mgxSjQh%2B9WXQKaiJjfb4ySZmGjgN2k3Cts&X-Amz-Signature=2c9a8955098437467f32380423c857f825be9ae2d74988619d1c6b7193f21150&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2CJ2PD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIC8e9aPn8CEhVk4CEC0MKxW9ud1KtwXuow3JVRqGYBDnAiBz0qCDpjkW935EWwHdFjxWwe6igphI6JkRkPs4qymwNir%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMb4wyae1GafBPqVTxKtwDnVi1WgKtlC%2FpcF%2FPBZgTY1iIupVnPfkYODxWRdmoqwcv%2F4jmds4Jxvpy%2BReiczcyGnjHwAGoXkjeLX8%2F0Q3k8pZtYQ7bkb2fskbmI2lV6Jtu3twBfGjZ61chdM0Cmrf79IkjGCBIz4HwBr7sbS1hdqiUTE%2B0AiioQAlM%2Fvzy21fUoC4JoXJgY56eK4fCIAvujM1kO17oerCqwMBdtNGLyzCfGE7Fy%2BqkFsBX31bYpxi6lbeEa4OHJjffEppkMuly9WK12HfoaYSmAz0bzGORjDEKvxKNIm9AIab2J%2BKMHoVlY5yiG6eb%2FSh%2FOAGg3%2FWpH6p9qOdCVULl25ZbH6QFttPHJRIOVgD6P0Cjx9ZNQtetTD4wvQFZZj9aYDXe9sLOE6SCTU7QUNI0dK6gLLSb3OuU1P7UO1jgg%2BrhxgZ6Js6k2%2Fz%2B%2FzR26weBTe5TxnryY6z2MfRRQn7R5QI9WUcf9ftCIyk4i8IrDNCh2664KzPC7oW%2FO59BkMu3FJ5IVLCYRvNa%2B33D78GsHmdcRj3%2B%2BX%2BxRCjTJ5PVMLEobQWy1dKEXWMJE22ZXdFJWsSjzu%2FekKTR5yOmbSk84PImWoBfgtGa1Lkilc4MC29KBQxpzp17uzQNttEeNSgZre0wyLOMvQY6pgGihjknH4X0DMO8g0qOSNhl3zf2bXHmXEsviURMX9awVChTN78TCqDGWFMq3lm8ak4XRmPGIxS04v4QYWY5zQg0xK%2Fr1nmScKn18HeBbNYJLD8PHDJ4u9SBuajaEsKA%2Bc4ng5R%2B7us5P6SJZS8PH5L75apIRfYemV%2F6xfKaIZmqyY%2BShu1iiyqh%2FT0SBXz9SdNG2XG4IngPWY35lHn%2ByrbHqyvG1sU8&X-Amz-Signature=d6199dc3e704beab7901950bf0b39420f8c60a580f9855d420ba37866b5736a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Q7LLXSA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIBa8OuBbN4gLmHt8UtzGbDa0QAm06ksm93ZmdRtWHk%2BFAiEA7%2FbQ4I88xcQPsSidmEB1RuPLRV6cymV4XrNvs1qm%2FWMq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLWqmJCcG1%2FI1ZqWcircAy6f4Ngh%2B8DkoNQFVzxEv4urRXlMCgO7VECOaqczRjR4MySoDhCe%2B9lc1FhyCjVXAXK4bV92d%2FH9dmKGeiliR16MSwt5qHJ0Z5jsmeoLWyHU7pzpjyvDDl%2BvJohYhFdBHWvGg6M3k%2Fgeu%2Bf0EoXFzNz6FMOuivN%2B1fMFnNVHRVx%2F5sOgBRZOoqcnQ2Buku8LjUcSMI0wu7EqXaAYtZJ2h7pLDPMvJ34m%2FnL6XEcn%2FMvhJq1vbZ4uL8jQL6%2BA559B6OKD7ZLygblvYPFi7i%2Bjqa3WirSU8P3ypYf2SFwilET8H9yRBV2bTjCYggNT1lFELJduV7uf44BZU6Zwn%2BmHmCLyD006CVsfqKbY%2FzGoG7BvZacKvmAgiRk1bAWUn3GmtUnilYoPZLM4bcgCQ7wQlij5JK6cGveisqvnhq4UeIdZGcMDwJgpOxkZb5htWnzwIE3twOa%2BBTE4%2Foe7tzYpCSLub4CMhel6bso%2FNjprFepuS9wm8wjvbU9CYBfJax1xpZBEjqIoIUt8rrzG4ZbT03yhVhTf8IYfZth4ah9C20MY5%2FbhVXc36HTQP%2BOeAbFe3WpL2FtQEw34V8duNIgeMo75wTJfq%2FNKZ14PoBUxvU7%2FDq49H37cV3w6s6tgMMuzjL0GOqUBo6rsjFK79V5XVlF3GoulI39r9WRi3X1aiK%2BR8gY01PY0XgIgP6W0IFPO0AThCajcXrmGQYXCtYafp9W7cH3s2LC2U47LS2ey%2FCbDgCawLO7USPIMmkwt4VWE4OW3amH%2FbMYwsyMDNoaSUGKs%2FUyPQUfZcI5lin4FBSJGoewxzgjZAhym2V9C%2FwM1zHstsoPp8SkGvoV6geJF9SwFfruOwhc4Z4N3&X-Amz-Signature=2f5df3303181821d76c8d0b535db924cb41fee2dfdca74a0a6344917bd30a1ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWBCJHUH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIELytvwMsqi62Y2v6SSfxSRrM3UkVizWheV%2BWYpVdKYcAiEA1gzwSeRN7LPojKrxXcbtWMtQdXAp2ofWYSxA%2FD3orPUq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLWihm1uVMvMX6W1%2FCrcAw1naQSp15%2Fq1dLawToT9O0n6sDJQmXCFRdgNMe%2FrwKH%2BPiwKy28wRoLzNrEZLy2T1prq81UfXwom13vLyL2taCjIaj1uLbY2SRzAClNLMw7p7x97TbyRcwjZLzhPSeZjahUUokF1nza8THm9%2FXZI%2F0QALgln%2B5Aj%2BFHMQ2vWpP4Ezw%2BYn6U%2BtrZGopluzQBi%2Fj2En0G%2FyBpObqAzie9XXZvE9uoD%2Be3xWgf5YVBLx5018CG08KYNTqTakf7apIeXmbBMY47nSvDGuEZ3u9yKohzbu377wr79VyWT9CAyRTD2wn2IHLYAO7J8lYuLPleYEjwD%2Fkv%2F6Qy7EpjrcR3jopC7gE278rDfFmISvaGcQ4AqYuCxIZ4rAA3zgCxkw2j3qMgMLgatmpeOzFuwwz4GIg59gnzXMrp4sPwG4krk2fNONL6B%2Ff2ylWwaoKWKJNurDBZTAPnd4yrStX5NrjNoGCvpa1jGkbSz2n5pnxVDlQ%2Bay%2BS%2F8dz8EPLeE3ffGllvvfzTsx6IoVZZMaFUNrOIe319WtaAdqLYHSvTzPj0RNCCIp3fj656%2Fk4T2EkErEs8gk22v%2F%2FgLL7PDb6HmcAx7YrlM2A8yboBuk9L52WXQVdTewA2gRDkePZhpXvMPKzjL0GOqUBu07y0%2BByUBsR%2FQZplcn1fSBgk9wh110zwm%2FJI0lPibAPDbFej4zurTXHVhACoN7RzoJ%2Bq6W4yY5BYiusZw5yKL8HZ0ALEjU0DX85HyAPHhi%2B2TGJwAu5dITd3wH8NUCvqOXHTFoBc1nsj8CPJqQcsYtLv%2FuOgoUMS217OywZBiHuPrRV2x29UW6jLC5NlAO0vwsH7fRxWvtHU9UyStjrTxI3B3R%2B&X-Amz-Signature=3e64e1d4a4ec8987aa0ceb9ef33ada0df1563d8cd6cfe88a1b3378ec2e6d948f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWBCJHUH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIELytvwMsqi62Y2v6SSfxSRrM3UkVizWheV%2BWYpVdKYcAiEA1gzwSeRN7LPojKrxXcbtWMtQdXAp2ofWYSxA%2FD3orPUq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLWihm1uVMvMX6W1%2FCrcAw1naQSp15%2Fq1dLawToT9O0n6sDJQmXCFRdgNMe%2FrwKH%2BPiwKy28wRoLzNrEZLy2T1prq81UfXwom13vLyL2taCjIaj1uLbY2SRzAClNLMw7p7x97TbyRcwjZLzhPSeZjahUUokF1nza8THm9%2FXZI%2F0QALgln%2B5Aj%2BFHMQ2vWpP4Ezw%2BYn6U%2BtrZGopluzQBi%2Fj2En0G%2FyBpObqAzie9XXZvE9uoD%2Be3xWgf5YVBLx5018CG08KYNTqTakf7apIeXmbBMY47nSvDGuEZ3u9yKohzbu377wr79VyWT9CAyRTD2wn2IHLYAO7J8lYuLPleYEjwD%2Fkv%2F6Qy7EpjrcR3jopC7gE278rDfFmISvaGcQ4AqYuCxIZ4rAA3zgCxkw2j3qMgMLgatmpeOzFuwwz4GIg59gnzXMrp4sPwG4krk2fNONL6B%2Ff2ylWwaoKWKJNurDBZTAPnd4yrStX5NrjNoGCvpa1jGkbSz2n5pnxVDlQ%2Bay%2BS%2F8dz8EPLeE3ffGllvvfzTsx6IoVZZMaFUNrOIe319WtaAdqLYHSvTzPj0RNCCIp3fj656%2Fk4T2EkErEs8gk22v%2F%2FgLL7PDb6HmcAx7YrlM2A8yboBuk9L52WXQVdTewA2gRDkePZhpXvMPKzjL0GOqUBu07y0%2BByUBsR%2FQZplcn1fSBgk9wh110zwm%2FJI0lPibAPDbFej4zurTXHVhACoN7RzoJ%2Bq6W4yY5BYiusZw5yKL8HZ0ALEjU0DX85HyAPHhi%2B2TGJwAu5dITd3wH8NUCvqOXHTFoBc1nsj8CPJqQcsYtLv%2FuOgoUMS217OywZBiHuPrRV2x29UW6jLC5NlAO0vwsH7fRxWvtHU9UyStjrTxI3B3R%2B&X-Amz-Signature=8b6c7964ce36a7e207b0980892d61f33402030cc4829eac12b4421fc73a77176&X-Amz-SignedHeaders=host&x-id=GetObject)
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