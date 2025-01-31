

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662STYRZ36%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjEyngynOVGTQFeXoLQF89gFuOYFNGWGjoGLEerTz3YQIhAOkoU%2FFBaplmsJEJZFUqcvGZD6udDTdySTGN%2B9M7lbXpKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBdv%2BVW536Fk89ypsq3AOBMhZHYm%2FRXDZxO%2FaY7uEnO7XoMT06m5AOTu8Wx2XqZWLkN4FB8mRmZC3xWbixyagUKsWqPmr6Ny8w%2Fa%2B%2F7cjK7RUqRSrxlHz%2BI7iG7V7l%2BPwdV%2FpcHTpGpu35C%2BAvWQE1r7TF1iP%2Fk%2F0udPtJoBi3ofa9dXIEA4vhSppn9YYLjILtm2c22FNlh7gkOpXb4kaPqkov1y%2B6kILYoV%2FEwwWJ3zcOUQW2vx%2FXxi9gozLvsGOLv9uiNsm3c9VHRQ3DhgGMjWX%2F7hqcKFqedNiIPTmjkCiq37MicA1kE53H7PEYdCbWEHgcPYiopKcg9UPQdZ6ZafP9CD%2Ft3Sdwp74vixudyauZlMur9CJKJ%2F7SbBsm9eG0jTFKJi0WGewCHKPmXC9YH1%2FjZxN3CnvUsuAlzP4O9FkkA3rRlVfnbWZKqrVnGHy3Qx2Cued8hqX23LDIzBSoj18zxH2zdNoOGjzdRf57vm47Qn0vFn84aOizCiOJo%2BaMCyCp575KiGnv4CTS91Ha8DUOkt1pTOsyhf7%2FfZ06bNgK%2F0MZcbVm5lYOjrd4tQVILyTNtCUFKPcGaT6xPLvEYnpBBQDjwwk9JHLPpoyllyRtakeBybBlqnJEhTtzTi8qBo%2Fq3y5eFoqZXDDi0PC8BjqkAXg8707qWJbOESfTWxu%2BBx87Q5fj%2BMSq%2B7ZWyrwO8D0tYxXjKlVNnOK9gibjzThBSGxmaSLYV8W9n6Raku5ifbyrECykrglJGf5jG4hDBP6uF6MdrOChTIlEGqZtbVNZ4BdPvqMOcEZBcfTBWM%2FtHMTLqQHOZeSQVQI7gIVQxyvS%2F2TUpTvXun%2B8%2FW1mjMxLSCSzKPE%2BuVrnFC6Nchoa%2FsyRJY%2F5&X-Amz-Signature=4b0fe6a8d860cc43beea9c86a821298961ddb33c53b920e8a9bab580dd2412d2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNKEOVHQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDu%2FZZloWxmQ%2BiKpVq9BvDe0k6to%2BfBK1Rx6wfam8dX1AIhAJTAhJsQ%2Bv8ldtgdN82Rp1%2Fg7iLLyrIgVH3vK945zYudKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw63PcFrXgwDQoqrA4q3AMcLM3T6JMaAjX8%2FlbsD0T%2BL5i4cPrqqYTRppmd6H6NpqZ%2FNKGo4xl2ZnV97dXEMyunJ8ssTArRQUeufDoBdwXrt5cKJLDx3zquMPXdl2H5Lkx1mV9kdhgmazI2yWZkPBJOGz1QB4Y5SNWhaagRiEe%2Bz1wE%2FjpeWYRKoQGsVf%2BU8qV1bCx%2FZvvAm8eI5aTyPAAme9t5NxKOROja5JfhTT5z6uE7BwFgFFdX%2BzPXIAqbEtv7y1aObup7iWt6kYrnvBtagR8qWOU4cng%2Bf%2FQj%2F9ElIU5BYOg3bEVJXDGUvj4wjn1JUin8vYtnbpRP1gT8yhOJIZVV1GuX8L%2Fzj33IT7zmzU2mHHEcY6LT4MbVpohioPb%2B7s28fNLUWbuAcPYlVDh2slzzPe7Ad969fI8kXE%2BR%2FF%2B6Nn%2F36%2BZpuJW23m%2BHg8ma3Gi0uCRZ5i4C%2BoOmoiSnPRSYCx04P67ndO%2BFiyjREBTUwTYixqyYExNw2dQdrPnC74d2awZgdlNvkXjObePYrR%2B7u%2Fe6VLIn2dgRY3Cr7it9LDq7CGNZoa2ZRY9BFHl4BI2m%2FTf6Xu9qqKYBnRt3hW6wtY6GFUbFrJrH0nyShiA1GMC4%2B2rUdYNoK%2BV71EI3a9VFkJQwbkS3oDC90PC8BjqkAcKdjySZ%2FIcJ1X8d%2FbdPYYCJnHdtd82whndPCBmvj8%2BzcgeHO6anrmrGb3aVKknTcdsOljaIF5ayNgUNOtzA81K6y%2B85H%2BKP8V6BF2QBr%2F4xE3ysB%2BvUz%2B%2BMZfbM%2F%2BE2caE8RC0KenfCgI%2BU3ic2SNGgFqU5J2Vsf1rSecrdRYAyPIGyv9BV39qgUf%2Fh%2FoT0XQMvenlO5Env7pr%2FSMyStcVlwhMO&X-Amz-Signature=ee0adf74b99a26d5b594bac2e37d026e8a8899d158a99debc42f44ac803ecea6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLCYY6YX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDCT94IpiS7SGBZXICn8PoYlBe%2BK4RZJgiWI4F8M5II7AiEAq71D3GqoVHPVoC%2Fra71cL79fIpdijk%2FzkpliTmduUXcqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJJuroZYwWUJlwnqAyrcA9bTmeIdzuuhR3E6%2BI2%2BuwvxYUMjkEB651tjaFZ6m%2BPrSBlo0OxtdEtl6GV34RLRG%2FpDVQlrz2trhgt4m55%2FYLevHJrtGbx9oBz636QsrEQgJoT%2Fbir3wSmmESJqEOTYBL6qV2UQ4yKVO60ysA4j5UhFN3p94o757x7zyTCEhL8h8G70qv3262k%2F01CJnW7OVOJTt0YxYYpWV6aK%2Fbkx8T4FLMiaVMy1uHmCc1hIMH5zbp01Z3OPjH4RcCGlo9kpp78o9S%2B9xdxuJ20xDJm%2BePLfk08au4CQFJPC4UfP5md5IPaIBo9xC%2BuUExrVXtEI5BqwrQNuiWJUyH4j9ETCBWSEdi8bZpjlNX%2FyPzfpQmPo8OuqcgmTaN%2FOvbOnChCI7vhklkfY7dV8nUBe3kk923milm9Z7NLv8JzJfUeK12x6Mv43S2bR%2BipJd3lSqPQZVqcwMH6kzarRyDlBSjYB0uun34%2FtzqnJIiFqZyjhLz%2FRRuNmkVgH2e4ksWOK9hFLA3Wrdw3pBdRWutvoODJCx%2FqAcCGrc9acWT0Qb0zC%2Frwn%2BxQ4SUR4rNx6f7X7XcUv4Os3lxEsEoxFClWwUXBBa8DQ7Boa%2B2BR8z9iu9r6WJXKbpIBZtLH%2F%2BGS%2BZuEMN%2FQ8LwGOqUB4JRajPN6ZPU6Mk2di9hwFiOYRQw7rZODyKcRe1gZrPhnvZ8Qwnlu%2BauI2fVPoG620cMidmiNpKBzpYw%2BAOc78WHBwHk2RiYAf0rnIGB4f6793QhYF2Gcz4IPVkGiHZdfju1dDGhG0p%2FhQ22OOmKUrUGm%2BmpQ64bzevG8W8A46AIy6aa8S8uNKQ%2B%2Btqzba2eu66H9S7KgUbVzYzXW3tbJ3QRQ0N%2FS&X-Amz-Signature=7b40d8a5491dfed7ca42a62fae9f610d876370cd9507f7ec7da4c39c501b646a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JB3TSLO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjY51nEubpK2SYop6YVw14rITLlPHVa3pvGvRBQtHdcAiBSGkaOIv08M7waDPtrt1PA0WxA2n%2ByY3BLsjm72I9f2yqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8SuWN7Zlbjc8d95NKtwDFaDXCIcmFyBPdRhESxQmWVSfQArhjLAWGl2bLFtr9duksyP27Xe1DKbbQLWlTJWO1K6I5HEW%2Ben%2F2YxrC31hVzSvUqcarNXj3cG9%2BpA4u4L39CLHB%2F3YYIDYER7DqLYXYH0QH8HSXUfh%2BKKXi1Pxvulyn%2B9Llfy7qH90di%2FYXs9xcNwyyXfPfU9Ie4FJY8zhaS9KS8lgLgcVX63genrQrbETO7r0axcYzVdHOka7jmPuFYbofr%2FYkAb2XC1ylEDdsirjnndmhNk6kZs7RxqcW88az9QvQWvNyXQfzQLtZ3vG6Q%2FFtO%2B%2FexeT1XP6ncO5qlhSGR1M8D%2FFlc6VNBfgjT8VBNLao25C9kHwVMmfApjqq%2FpQjxLtRz4XlEgbeJo0j9EtF9GZZuIdfUz0mmcBn9yoaw7elRysC%2FNc%2FoW%2FcAHRoOA2KCBZwxLTcFhjEPeGvH96jxe7ktQAVfjtAAJwN6lZtrUTUmmUC9Gj7YOerF7F6r76s8bX%2BzeeM8dXXT8QPg9zaHtMU2tPL%2Few7WaX8C9ZQlB6LV1Mre8hEt3Np8d5QEpDtYG8VlNS%2Fgz8I05JnIljhWCVAB3Zvi6WFeL3rv2lfb3Uz5h%2FQD3zKDA2VQIXjWCWLMe8lGDWINcwiNDwvAY6pgH%2Bi206e7wNQNRjdvE0dYlF%2BsAfz4xqCbEu8FnkK8fXt2xkgtGnIybdD5wg0FYgDrYZqZJQjBzJkxc%2F4AQysXIGc81bgiNIKIEv4SaQ54Klj8eeoW%2FvBvCaLNknbMRLR5BvkYSDiB%2BKb0LYxnG6P2tVhzIzD8zCwGAvZoHV7nexFnrBxjRAnPRBSNOT7s%2B6wfFz38hJNdOU75cP8e3STA6sMtTrK1FH&X-Amz-Signature=acc7fdc48cb4e36f5b6386327d2edf09da571281cccea64706f89ea9f7a6799e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UL2VDLU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLnlmG3sdz5XKrpHtynC%2FTMjtNVfZRdnYYn6AsDKwKXgIhAPU5oV2e6%2BU66dVocNe7jgLaAgg0QIn53kxKK0JBYFcJKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsgVe4f68we17wPFUq3AOnjsDO9Pc%2BAGIYZoBh4Gm%2BQBmKVOutzsri53TH7k%2BcugZJtHw8vVW2HN1npM2qYec1lpe1bqtEWxOOSfIiFQ%2BsrbR0CRxXplPIib%2Bs4GJUUDErnlOW4FNlS1%2ByfNUJmqhCE3YPsjkPUU4ZdSCu49lg%2FW%2FpP98Z3aFcHVkKSQjVlfE%2B9MI2xMBS3%2BTy4SFFQn1yj9wxONCLmDjjsLfORQcWHWM1coiVcB6dipGCfgotNM5bAYP0cBIOItuYT8dJclr%2FKyvAWgAMEM6wZJKIgmpCvZNMGrqcrYVcxWo0WIaqlFgOi%2FOOanOJfn4Xm3Xv42ujpCK4lB8%2BC%2FEaZHh9ZucPzS0%2BkWibpclH7cAycOJjz9twvQ9fw7KYp2l8GtfNzNmt3tQayM%2FOsVpFsuuxj4vU8mDKlk9obolabOG1hgfyJBQOwa%2F%2BUsBtNVsppHxV8tPRmG3ejmM1be%2BtVwF3nnXy41W4Uz5iFPYqXTwMXTwmxiGc6DPVktaFPsVEAv0a4FT2oEbj7i22SANrzZfceufQ2hc9RknISA4SKaVrfAsT5scZKYgiIdmgd8J0VX82%2BkGxFX2FI0alhMA4DzJt6T1qw9Vl%2BN3P9m%2FhtjwDF89XaA1XzoHmiAC3s%2B%2B3ejDS0PC8BjqkAW49O%2F%2FvRrtLFWnnbjCtCuWmv5xhIEJxnp2yb6E6X%2BEaZ%2BQBEZPCYJs75BLgmQ0L2FCS%2BxHE%2BiLcXgnWoBvctDLHdNPV3V9w6egdLk%2BrAq57XB%2BLA8c%2B8cFMxVU1jCPVKZGDeeuJ5ee9a8ndoz2a5dKK94g%2F0DWl8HxyEmDUz8a%2F630mCf%2F%2BpeMmByoC2C35nUsmhvQSCHbGPC%2B%2B0W%2BqbDmGv2tz&X-Amz-Signature=97bbdbf5c8429fb1b1828120b22eac9da2798fb12e83fa8f2a2cbf6b8c348504&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHN2RNU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGTyBTYdtlZYYNSrlaYZqP5ZgRiNiB2AGfdm3gVVcNmTAiEAy%2F%2B6OJmIZjwM2oSkTH%2Fi6Uy92t8dNcWvZga7xfMn5osqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGkF0dFfdr5T6mKAvircA8cwJSB7xWskOnXGtTuvzcnwoGiCQXME%2BTbRDQUKEHOY2fRSgNI%2BS9S0waKpTXbytrkMJrzhatHb14I%2BtupKkSiHcQjyBPscGIbtihJP3UfLc6EpDbV7f0mnhtdLyaULGCUX3ZDoDF11N8uoxZNOmc%2FZwT9FzztvEoRK2iuJ8wkFohmlwLUvhGhMpLW8iZO2QDFRKz8SCrdkihfcBqmwb7wp0aEmdQhHXC1Ku69w%2B1Pjv4qLC8l3kwS1RF4bU6339FVzpteL0Adcw%2FiHISDP8LknYkJ1x6vOL7KRDy2kgJSPHTezyAmHG8RZ1eIr%2FwcfEKGLAqug05kFY2WwnsbKfwKUiQcNfsNbkwpq%2FlO9%2BcEkB5FidUP5av5qqqDpktHhhMaEugxeVOf80HCZ4fYzpoZj4FRnjeYCOcNUlkRwPZtxdxachLNEy06BQjohuEXgdWP2LSOPx3eTQEIzHUM5NsyfkcTKTKKVhji2pwpwVk8zSB6ARDRvCHb3STe7P44Ih%2FoDZdufnVB9x6QmimhJleKPLvWdmq%2BRxx8drFKFonVxJrpXsTRYongZu9URSQbuKa5FGbYxzXYG5Nenp5sc6CqBRqJPJzXfSf7ThVZisTzEUpb7w5qK2FyamXGQMI%2FQ8LwGOqUBlImoi%2BeAfe4%2F1zwje8wu%2BFzva%2B%2FbD%2FmoMDdv13qXv2uo1H%2BAie3QYduILLD8rLVjQWTRvNVJD8eMNqHt8P%2Bz5HbSNdGfH6iNaT5QFRsuP9trMYu1clOt1A9yit6BKehuoeUwPzolNz18Eehxxn0f1%2BOk4chKKVkrsixM8cXCx5qxFcbY%2FB33yay1mWgABb2swoyuokg6C1oGf6y%2FsLwbAh1SuID0&X-Amz-Signature=19a141a94ed956e266696daa2f6a8f4808b7546a3d6ac99ba3c989530a9de32d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7XEIDKO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCebrl5UwLJ2DER3mBWurlm8gla13i87ixnAxFN0KdQOgIhAPBW3G%2B%2BV5Y83dle9PEX9M10gHTt6dU7ag8fnAmLx%2FoLKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzslVKVCvtVT%2FeA8Doq3AO5KZyl9h8epUFkdZGoKZTBKq93x%2Bx2FxCViE%2B21%2Bdt1T6BUP9s0s%2BcF2SbluMvB9xSxOiYFbxH7q2AQYfcq%2BRLr9YzYDRbXYL0ujKLaooYnzumEhfi40hp6aibomQwnsc33nZ%2ByoF812AeqwmrYvdGvDzO%2FJkLFsGLyKaZhCR%2BZHsg8rtMBRSQg%2FxJAXRZlraOTblXItNq2P%2BC5uJU3Q%2FICVRKzj7mXLSO10FVHHkofyrLoF0jHquOeVYqPxKIL7OYk73p6J6z2M4aCIrc6dW4nNZD53Tvq14d%2F8UdgYH1oK9BfTWlssruX3A6uAk1OrXCmsaG6sdxI261GBfcQACTJ42ydEDSikeQ3K%2B%2Bm0ysgo1adGZ73qNVWfnIXGcSOYmLtQT1jGpar%2FuzX8YGu8HMk8QcOJ3P6hDZJwmM43%2F9nTv2qg%2FBV5bYxE2hTUJptZqzWAUcUyljXFHKvy%2FaabqdUcrdTMh9mPsnchA4yAcMSwBBTmcIOukkH0s18V5usmiFlOFKDmggo265vroiFJwjlVs0hpPbZcY57uxmqzzR%2FmWq9Z0pd9ar4foW%2FZLvuOafSQ5MhtqMnMIdY%2FU9IxmvHuhY2%2BHaoBq3TafwvXOSmEugKsS3YW2t9PdmvTCp0PC8BjqkAf4IYgc8OS0Herw2x3PJu6Boh%2BQLULNIw503mVh8e2hafZK2PZhggRlrkUjFmkwQ5M%2BuUT19pw1dWaXlO8EFBqdOBx9PUG3fHakYcNmRJELoDgA5wVhz79ORHXNR6DtGctdYnol5uigFJ1ZG8OWHjrVbeVjgKS2eTN5ubPRjxKCGIuDRgI0ZFpRTuNpSbF81%2BcSA4qNIiVbhJHw22eHgdxl4h6Ov&X-Amz-Signature=32302c1afbcda0e4de04f7af4cc38c2c3da97a2b52d4ab697784d2024bd974ff&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK7S7GA3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRtl1exrSZBLzQUqFMogw%2FuyZTSDhkjEDJq2ih%2FXRBLAIgTP14ryDVtxbkBa5mDom6uWmtfifOO%2By9pRAJ7sSXT%2BQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIrDEQpoD334besMySrcA12JCakXdxiIcRKjRsf9CGTJ%2FOEYvx40XwKvXlYw61YIdlp5p0RJxpqohYI2JJ%2BS%2FrU3SKScILJ7W8PUGo2X98h3suTUrN0ZlMqk4k8YFr%2F1bN%2BZZFMj7h88mFTPbhnBk1jqBDey7PMEkljXw1Bm%2FyjlBe5ryF%2B5MBjSbLmPALkFA2mcKlVkIEUrmJKrG%2FSTSyCtZjNrhMMOkF8aUiWZJ1V38aWwoP6AfZmfPZVzIaZNDe8oW8CjGI03IEcvGRgWfov%2BQ52wypsOFp5PPPhnHyzd%2FTnnCk%2ByJADkQPWl%2FD943TjMXBAnYlMVTtpIKSBQxrWo9qygj5v7QVgHfquS%2FGMoQ7CJ11cwtrZNiultdpoYZO6v2BGNBUz4FEb7ELEMvpO%2BiQ%2FQ6vxoOa15bc1kXwfBrqqgVwj7tYKVJOqXdueGCYgce%2F%2FNS0d5YM2ybGI3bM2ZVU7kARVOTc5tbNW%2BBCQ%2FR5iyGKoD%2BkCR85GaX6xoWdCJbP6dVPF4zS7g9kFKLhDYtIj6FeawVjoSszXwT%2BGxJxokcT5OT7a8f5v2eYhrK1lW9btg2GOQVnnm9XpC3SmYfTFXca7KV7pYO2i3%2BV7%2FnBtYg7rRRnOKWtES48O1EyfSkC8mZO%2B6RqumMMjQ8LwGOqUBgvrc2R4TZetSKZw6kLv58jzImVbB2Cw2WIdp0i3STf3DfBImXZtTvygtSS7On%2FdhSrzxp6V0gFabaBbXeQLzoi08tihNyFyCvpl%2BcjMWkVjkqu9lcallD46ZbFQWsUHDGppgcjhy3q9XBVu%2Fy0pheZIpkGZPropI%2BuKFLo9gzEGfk3MhOyJEUD%2BTcLbwktblkYpbPaOE4D%2FgtCA59kTAzZLI1ROI&X-Amz-Signature=368be70d16046ab014a6b4369cfafd1275c240228dd6e5a3676d4807c5c11d17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UL2VDLU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLnlmG3sdz5XKrpHtynC%2FTMjtNVfZRdnYYn6AsDKwKXgIhAPU5oV2e6%2BU66dVocNe7jgLaAgg0QIn53kxKK0JBYFcJKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsgVe4f68we17wPFUq3AOnjsDO9Pc%2BAGIYZoBh4Gm%2BQBmKVOutzsri53TH7k%2BcugZJtHw8vVW2HN1npM2qYec1lpe1bqtEWxOOSfIiFQ%2BsrbR0CRxXplPIib%2Bs4GJUUDErnlOW4FNlS1%2ByfNUJmqhCE3YPsjkPUU4ZdSCu49lg%2FW%2FpP98Z3aFcHVkKSQjVlfE%2B9MI2xMBS3%2BTy4SFFQn1yj9wxONCLmDjjsLfORQcWHWM1coiVcB6dipGCfgotNM5bAYP0cBIOItuYT8dJclr%2FKyvAWgAMEM6wZJKIgmpCvZNMGrqcrYVcxWo0WIaqlFgOi%2FOOanOJfn4Xm3Xv42ujpCK4lB8%2BC%2FEaZHh9ZucPzS0%2BkWibpclH7cAycOJjz9twvQ9fw7KYp2l8GtfNzNmt3tQayM%2FOsVpFsuuxj4vU8mDKlk9obolabOG1hgfyJBQOwa%2F%2BUsBtNVsppHxV8tPRmG3ejmM1be%2BtVwF3nnXy41W4Uz5iFPYqXTwMXTwmxiGc6DPVktaFPsVEAv0a4FT2oEbj7i22SANrzZfceufQ2hc9RknISA4SKaVrfAsT5scZKYgiIdmgd8J0VX82%2BkGxFX2FI0alhMA4DzJt6T1qw9Vl%2BN3P9m%2FhtjwDF89XaA1XzoHmiAC3s%2B%2B3ejDS0PC8BjqkAW49O%2F%2FvRrtLFWnnbjCtCuWmv5xhIEJxnp2yb6E6X%2BEaZ%2BQBEZPCYJs75BLgmQ0L2FCS%2BxHE%2BiLcXgnWoBvctDLHdNPV3V9w6egdLk%2BrAq57XB%2BLA8c%2B8cFMxVU1jCPVKZGDeeuJ5ee9a8ndoz2a5dKK94g%2F0DWl8HxyEmDUz8a%2F630mCf%2F%2BpeMmByoC2C35nUsmhvQSCHbGPC%2B%2B0W%2BqbDmGv2tz&X-Amz-Signature=ce3ac9b481ec1a701fa9cb75f646971a073b63d97edcf83931dcb674f1922183&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCKL6THL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCesTpI8Elp6oWLJHGWPM94hBZ3cOxERLdvZSmOfaSPwIhAIC0njwf6UhnoYl9ykzcOFRMM0NABZo0g6Bg2OuQCky6KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5i1M2aht8boaIyToq3APALPI5yuzb8mfpiAPAg%2FyAqydrUvCDknPm48nvyTJoSiiH1NsvhMYqSEB594FcyeGmXip%2FeYt0xENNEZRGu9rMD8ABCh19VUeJI4vdb2FTCkeEb%2BdEYTzvKwfjytf7xbfPldCKHXASmVgWtEmVYj7%2Fe%2FLvdgOy92o6%2FWMvXW2uJJQRxxflewZXvpvzbV%2FdxwJhw7CGdx%2BsSUyZ0TiIE4ByEzj4uddgqXxGiRb7bE1x%2B2bKILK%2Fj6bih8YG8If%2Bm3yLAmej%2Btu0GoksP6KwaKS1QfCawAjKtoSZhhHANvuELVgYXwLBo97dcjiUkhwMPJGUcDsjJOM%2FzyWXK7pesfMCJwFs89EZY%2BlkHs1kCR9q8fiuPdnwKvONku3S5BWf%2BXeMFM0XWuIFBZ3low7WBVWln9sYih0FCzuH4rHcfh3dgfrhvr5gGLyfPNiLYHBtqn%2BYMeL3gvNpihZ4KuQtD27VLPPmq9kHOBN6FHb4b7KyafSGLHlgIYyc53jFfZ3eZHN0WspRmquKkRMNrkJAAS3NmWY12zFBRlq2Q9XPvpORoIqkOdGvEsog5ksRqUSrlVBY1gt37sXZk77PGo2We%2FXKOegBbW49jTRiS9z3SeY19IGOOzO6SlmCO9nQbDDV0PC8BjqkARXY3ectiDXLyf59DRz6DglR428YzK%2FX2NIPXMzYuRZkVQRHfA9Tcd8pwI%2BlQAg2nHk78QuIC66iRSBXoiCKbQ0IdkYxZtjU4J6Y4WTcaIXsoE1TjWYakq0dAX26un0q5ufGCuO19m2UM0XtICPE2rUUmTENv%2FNbXRgCzTxofe0lUFby2GizoM1eOnUSW%2FxUrEGjQzwjDVEn%2BCN7DDpNvbIK2Nuq&X-Amz-Signature=f29d3eb70b46c1de3dc50c77d241dcfa796aa4e73bf19f5b2525da386c753890&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCKL6THL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCesTpI8Elp6oWLJHGWPM94hBZ3cOxERLdvZSmOfaSPwIhAIC0njwf6UhnoYl9ykzcOFRMM0NABZo0g6Bg2OuQCky6KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5i1M2aht8boaIyToq3APALPI5yuzb8mfpiAPAg%2FyAqydrUvCDknPm48nvyTJoSiiH1NsvhMYqSEB594FcyeGmXip%2FeYt0xENNEZRGu9rMD8ABCh19VUeJI4vdb2FTCkeEb%2BdEYTzvKwfjytf7xbfPldCKHXASmVgWtEmVYj7%2Fe%2FLvdgOy92o6%2FWMvXW2uJJQRxxflewZXvpvzbV%2FdxwJhw7CGdx%2BsSUyZ0TiIE4ByEzj4uddgqXxGiRb7bE1x%2B2bKILK%2Fj6bih8YG8If%2Bm3yLAmej%2Btu0GoksP6KwaKS1QfCawAjKtoSZhhHANvuELVgYXwLBo97dcjiUkhwMPJGUcDsjJOM%2FzyWXK7pesfMCJwFs89EZY%2BlkHs1kCR9q8fiuPdnwKvONku3S5BWf%2BXeMFM0XWuIFBZ3low7WBVWln9sYih0FCzuH4rHcfh3dgfrhvr5gGLyfPNiLYHBtqn%2BYMeL3gvNpihZ4KuQtD27VLPPmq9kHOBN6FHb4b7KyafSGLHlgIYyc53jFfZ3eZHN0WspRmquKkRMNrkJAAS3NmWY12zFBRlq2Q9XPvpORoIqkOdGvEsog5ksRqUSrlVBY1gt37sXZk77PGo2We%2FXKOegBbW49jTRiS9z3SeY19IGOOzO6SlmCO9nQbDDV0PC8BjqkARXY3ectiDXLyf59DRz6DglR428YzK%2FX2NIPXMzYuRZkVQRHfA9Tcd8pwI%2BlQAg2nHk78QuIC66iRSBXoiCKbQ0IdkYxZtjU4J6Y4WTcaIXsoE1TjWYakq0dAX26un0q5ufGCuO19m2UM0XtICPE2rUUmTENv%2FNbXRgCzTxofe0lUFby2GizoM1eOnUSW%2FxUrEGjQzwjDVEn%2BCN7DDpNvbIK2Nuq&X-Amz-Signature=187b041b3dc8898b4d26b59355f9d89a0b213bb475d29a05e669275ab727ae2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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