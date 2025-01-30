

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4DC2WBV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlq5xgmbQbXIpg4k8iq%2Bbm8nMsYuIbqPE9syTi9x%2FPvgIhALS%2BWofbP6nWj%2BD2oWGPKG5KO55JNONDjkU3iDVolHFkKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw7uFgJ%2F122dcqCdyUq3AOpAdLrNxVVArHRpCptKHujQvdKai0pzBSNfDgZ5kvYm%2BeXhYSNc4NchRd6gFEuveKXnLFKVzdAvN5VVJhmp6uBQOb2m5p%2FBcX1aqwPBdg4%2BDQs7lArh1zW5ISPKjhm1cdWE%2BfENFVaa9nvOarWK4OCsADzesIDTUrwAjK6MOETZ2VKZZQiU5LUl4X9qpWrX2vKISwz%2BauMtCiX5%2F7CucRHmHbzHkDroQ3fL2jLk7%2BDtIuI20uXo0j%2FQhV7F%2B%2FRpJhPONqwL7NqhAdfGQZPFdSICB%2BfRr4C8A1JHB%2FoNK23mavlgyMgjUerdom7YvsqzwCgnTFrc6xpIfhYaV9eyek5ew6zW4lbOfP0jn6NElw%2FFBOisqFHxmlUFQdtFoKnTpD6%2FXVL9F%2FJpNKvfdk6%2FYtMwE2E%2BG%2BuaKcKylQmk8CoPpO51Hq4LondYx4tr%2FdraskxkHtZUOWowgF7y1t5sBkQkKUoRDZd9mZybhpMRv779bvYy2ySfm%2F84thMS9WSe3%2FVX25tvNvQSK3Y%2BkVNtrqCaV3%2BG82MumRTJl5sYRtvy%2Bb9RJz3InUixAM1Ik3tL84JLIGuJc8kq8KfjYdymjDNhIegXvK5fDNbYJud2ilJVSdQtEpTkeInc0eQ%2BzCUo%2By8BjqkAXQEQg75GOxC4ee0F6i53aAzWrUtN68WolMjddEjzZyJ6cfg%2FVJDH7erWQqI%2Bv8dx91PXqm%2FgFDRYbLTH5aTNX%2FZb9nTEGY4a6P1vweOXlSODyoYd5c0SJJkBjnIhgGnhjaMOc%2BKH%2BsEi5%2BnVTTzkRhlZnn2%2BQrYjTmm6WB08XtWXzmj0FNVu530gFbrxudSLxP2gnrGjYlU54317TJaQwt28pF0&X-Amz-Signature=dd43bf31bbe4e33662f78105ea1411bc0a77b3807275450535e4ac73847d1f9b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X64UCCCR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFmhLGyuVAEWiZEqdgS6aXmLwd45vZAKxhPuONCh1nLxAiEAvTLq3HThAGhXbMXOP%2BSSYY8RAbjaQLuxRHu%2FVlwPIqQqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNfBYByO8zZjGjXRZSrcA7Vp3pHgwdQFOJm3rRu9dLptJOCK9TLQyNtQINvf6kdi%2BlkSe5tVbNQcDTc7cGMI087V1puF3692%2FJlqh5cIIjDSWWfDf%2FzyyBeqRzfqIPFf0iRUIbhjl5lo%2BOJc9b39jr1lIUtEY0KCC502XKY6ELhMwBq5V3W%2Bz5WzOU7mwdbMmZYVwvb%2FqKRt25p%2B8WGiKX0vzoDU2%2FCwzTJBYHvaVnWNUMMZUGdB5HjU%2FV%2Fc93EdMtSjeYlXoUKVoyjUcrEbmn2S0G5ngWoqG2MA7UkeXpnXwvZIsRqRWu8wxhWBYyZ80NnUv3xrJQEggTVaiBr6ZXfTotABfqtqT%2FLXeD47SLSj2ExvSbmZ6FeC0yIpHxmdSkqriqkD%2FnpP74YJOOBAbDZ6rUhHIsyS3UIx%2F4EeopCmqIQP4XKmb3PTpI3j25Fv%2F%2BLs1KgHo8ONtu%2Fydz8AzYmdWBDabG9%2BbWjyb2%2BdT4MLu7Fgh1JPsG1wzzoyslm7yyqztj6K9sFgbIuHSpIWRIDF4OKRrWSvms5D5P2zHjdbXuJ%2BKMpzMiGF%2BIMvFdvi33b0ORY%2FuLNuI6CmgoB91h82rM85TZcjSPloD0ldlbYwRMdoFISIX1ocVjF0K8iAMHjljrWV7bnHxojuMISj7LwGOqUBX50KdVCUwhW7Bly93lYrEBSxbEDmB0Gxlmql66LOGn0PoiNL2mr9dBVGm1tJ%2BjjEslSeWhSDyLaLjH3K4aJFu%2FouyPNMKKDqCQ7brBaulnw%2Fw%2FyaoXVRE54wUul%2B6FUZBOzWmeSdwUBSqp7lMR%2FMPC9QBBovdlpp74lK7v%2FQPhN%2FUwpDFEnB4Uyw8x31ZK%2FGN1G%2BXVn4mxAT3WH1%2F6cuzqAcHV49&X-Amz-Signature=c42e2c430156883ba8311f6f0fcd8963fff8a4de0a4357690e63711b5415b614&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVAHH7YW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQyGcuPVS9QcrJO8QNOZ2a8vDeKP34Ts2KAIDMTqgLNAiA4VOXMx7DnqP7tIonxWUpQSNi85N%2B%2BbwT9yGuOoqMo7CqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRvYLtXFzcxP4nkIiKtwD36zJNGCEwNFCw4NgBeBgnL45rpY%2BCD74AlwXE3Wy4bSAzRJ7BVjsajbBfqqv%2FlP%2FORS8%2FP%2BDHtSong62OnBqiltKisdvQ8nXmzIQ%2F58ILAXeNlVl4tUOQgcgmunv%2FyPqBTF1XCLxjFU8ovoZnvGWDky1HrXq6TCrL4vYg%2FqBjoZ%2Fomv6WPTQBTloLc4r9J96idioYR03h8PHXWJrzi3sBhQOCnKh2LHz%2BGuQbLHMg6BKBixU1zVME2jc4zOVECofY6rn3Ix9%2Frv03rzgvtMOUnsBdAKU7SV%2FN51UB5akUfWLNHhZz3y9PB42U9gvGrk8YSZ8XED%2FHnDs1n8%2FzVbP9JcKyR40ukC8srdeURKuX8t4cGfjG%2BoEIbtmKvOBdjL2rMVG5cm9YIgrMGrQQDNUL0ewnV%2B4hfynjk%2FCBjBouIueoqgN0DxzoUMxsmVB0AXN4khI2xfOYS%2FcXaqDvjxDqocY68uFgD8%2FYyYF%2Fzm8opQP5RgfbKi1jLmb%2BFg2UDEqZykA9d13l0eWOYrgD8HvM219udKO%2BBVF8TbhJOYOZWkz2numr0FYhw2Q93HHzxa1iLvXWX48hQ5BhpvIlfBdsQZLORE55aS7GjydKdIYKZivcl%2B9c9PHywEEIq8w06LsvAY6pgGGG9PWihh8HDteTIDKlb6rIMgjKg1u2lZ3Gr88pJxm%2F3dEbGnano668VWm52Df75XJHf0DFdRTkiMeXntmuroEGzvRjesQWKBQk986UKDdK01EZ3qb8V8djeM37eWsu78VHEV%2BdUBdTGRt6TNC0Km2m9rz0xlTNkqc6AdR2mZenBvLPHgmHll228viMPHtmRbUINdv2Iu1owaNholTj%2FRQ5h3mFJo1&X-Amz-Signature=2b4352d5d854eb77a49496680fad7b6fe4c1e5329233310f434968cc34b3c261&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTPTGB6I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEoqsM5TbrlBdiC0LVeR35IykRdG%2FtjuBgZLTv0YmkdzAiEAyr3QLlZSrokNpT4OnjC3hy0km6EVYEnwJjsb2INl8%2FsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIvL74ntZSzNGTaVLircA2%2F9Jpsj3T9uzYOiSnWu%2BsArKouwuUwhPxgebB7yMw0LhVxnafwYLqqpYL5mt9unS9ZAe4ARdLrJrz7P5oQbo9PoDjl8tuUm8qNMPNRhQa00dL8ubskH4FPSfcL7IoDDj%2BGRfFLylmTNZZtIHlrkWSlUK6750fovAxm0Qu3OllbMA1KTwyTnw86ZTKKar%2FngGNbEexBx8QbWlr1TdhvSRIeB14EUtF0nAMhhDzvUpehp9dX%2Bu1Y1hP5GTMPpqeeObClLpGUpG8zF%2FyJ6mkbDNx7fJitX%2BLgRd4UzKJKIdwvWLfP2RHX83N%2F6wYv8M%2BuKqK50A%2BrQe0SyXuN%2BROMTHdvl2Ny6oGaqOeoaAxNZJkCp4cv6kLvGrY4472PoVIeL%2F6IYvxNpMT7bfrRMyW1jtjFhLhetnKG2vrta5oXgYnl%2FPjge8%2Ba3FbSs85STkbwVL%2Ba%2BrLlk6scVXqtKy1n31DD7yBTqtp4iWxMxtLy0C3UfgIDnZeGvi98iyVC%2BqhsnuFNRm%2FxzKlJ13B3y6QpuvTSvUkyrTlb4cdKU%2F1r%2FsIBGna0%2FULPPtCi1FyR3lvaCoW0pwgaUHgYUjpTIULnD9QJCuwOfhV9ZEe%2B2Ls7gg%2BofBwC9zJZPP465u7liMO6i7LwGOqUB4gmaFMuTHUJsqrRerY3XfbSnWUv9sKrA8OmJKdk8YL0odeUHB7X4CuLxVqmOZ%2Bao47%2F1XNBhegZd0A%2FnKWWSbP3AaIE2bRMAFY%2Fp5K7iiqbp%2BM9Khm1iJTW%2BTf8xV4UrKzYIPOLTa40Z%2BXBZNmqvbWGsx8P3aCOHu32RoRejwmGkgiETh1cxFlIZGZqkv1zsg9%2B2KOWzMDAQVwZRiD%2BlDpjVbLo1&X-Amz-Signature=722d52638a8e1a0c277dbc2cfdb9b6136f4366c1ea5de7de0a78a19a791f9e12&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOHPRFFV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkmowcNUHYmtxXp1xhkZJSP7OiVoWiqB1o39pjk2QQawIhAL14Zl3hZXu2N%2F1nuKUx0BCbpgEA2W7qmhWAJCFkNsUAKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOkJaxP0JmwWKjTGIq3APiDhmUUf%2BXcRglLi%2Fl7SZZffT8w8KK5Bbepdur4xXgxzLs7j0gHDVP7RKL93sV6IGwpOS8yb1iavzbDVE64MyV4w%2FyDJTDwY3SuiWtSOOi5%2FLIaa%2BbAeL8qgWPc5c6RW%2FANZEXYs3OvGsyCyz%2FqbCazKlJMbQYyKGUQEUslyNRLJUPi7TrTThtXWZ0pawtktsXsRm7NiFFPOtdaz13R7463UBsfE16vneVFPezT3UitFEGZlVtf%2BsJ%2BBPEM33pQrlK0nfRJXtdQGvNIyVgbHucMF88AX1F0UD1s7HsxcsRDzJNyUS1q9GkACdB9qOduCsvH63iI5xiekrMKPhQtW1YUwmvBNxGCDlyNrK%2FMt13w0uTBSkOpq27TLgBurV%2Fm1Lq6tGIcEGxDaLQcBfHXkecZIUYLlLRi%2FesCNMN%2BNYp7ZsWwRae3vs3vyt4HuKsJryBPLbl6GPQ%2BunH2Cn5S0ReIfKfDr5U%2F8LbBV4pW1wmoNRPcxgMqcLBye3z37ZS%2BxHkQhNhVx9nM2D%2BkxmeJJr1f9nQ6prBKmC%2BA%2FqkkyCUKV5xjAUxmIjgE9iaflK4RB7V7%2FBtOZaRQk9uFqlwV1rSAf%2B4r%2FsUzKcU0tRkqP3L3hk1RYehGwyouLzvHTC9o%2By8BjqkAas1JrmJ%2Bv542CFOz6nsihMlJMnhfDsDQ%2FH9q5yyy0vuJSVGAJ8%2FVpMQKCuNLKiJuONURj8hzW3gGIryJ2FFnMHaSMb%2BAX6rTwI5RVGqrR574pWWsIlQWg0CwGq7cUX72gA26PBUU6t1PVkyWLPBNk%2FFSMc%2Bx18eL90py6ydTUriTbNFRGHSPoJ9OizZLWFg4SLn1eQ44nZ3SW12TtpU22BczwZK&X-Amz-Signature=5523802809eb2d7255f1750f3a5fcba7a898f6684a1aebdbc6d45241e2919efc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL64Y7XP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8svW5Cp52qYCc3VAAYLf6pmz%2F1kUYtjD80sYJu52U%2BQIhAJCPbnsQkNTUrpu8rzf3GVzJCRZ6lyQVdtI6Xrd7HuewKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIsaYtprcwxxpWQ7Aq3ANPD8MsyWcNJOJKVw9vqS68vx5%2FalskMAWQgOmA7miyKRTuZ%2BrbhcLGp0tRwJzpHioX6Cc%2Fbf7C4SirSYl8rUkIYtMHgWw1%2Fhxv7dnjdkXRB7McLSBquqHa%2BKlSLALv%2FKajUfxrZi5K34umsXfj36ejdy%2B82tlbIBGR2SwiRe0eRwcxqV%2BKW80MENnlzW1PVGaUaqdy9phuCOp0iG0j%2BXGfa7NEWqsRn6WFIXinHlmZSeruP67NRVdvtBRJsJJ3as19Dg5SBguiYja6ePAWX%2FbpoCyZrZUXNCQ5coyU1OvAerhppEbwMrImMnFQO6REy%2B7GuAJ6GUykMl%2FZ7Dit5DhEmgTSfN1HK4mStWZdAZeON23PfdloOaqmAFbfE6sjV6xOHukvWxHyu3HCZFvWiSwGs3c2NP58I9c7PorLBphHKGbYvDAV3NBiV8qI3fcyp9zPo0OwxAOQ%2FMqrymwHkUx1a7zKAmnuQq%2BwWR1EsvpiDC1mnYklSMZqvQScgglGidqBzcXX5v4hR97ek%2BqS%2FcufYmzVZj3Y42Jgseu0BrxJLJPcRgisW7rIwP%2Bdwa3%2Bx8WaIvfFA9gCdkgTd4%2FYClENBGPrdxercBV2GWySlpDLxtVwAULDKkIImjDVXjDTouy8BjqkAa9%2FYIC%2BpLLo212LXNppUX1OjvyOXxTPy8VK2PyUDMJDt9K0XeaNmc4xJOJnDzjeryHphuAC6f9CJwGUg8evvdt7y43pfnMW48m8%2FK7pXY8B3Qvemxw8R3pLdjVHjjxc8FmIYrsfVckQHndKaOqqoOUlaIOkYjxYQDas7pzlwgVYLjvjY42oKpijCjsSOJsUhAN%2Fp0Xtc5gc75KL81bmuXk2YsbV&X-Amz-Signature=6b856c8404f8270e8f9eef9489228892db51168c501d7fdaca4214dacdb864ad&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HRXCCRN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEFhpvadYZKxHAUXFtFLCsjcl4mgZ2FdJjnDawxhPEeAIgJ7QfOxcnzeChQFsbDYa%2FKHpICpd8qgezJUwMx9zVsgcqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGVolbBxTCpPnxA4nircA2%2B7EtZOp6OdtaJUoRMh5o%2BZy%2B6eI9U%2FLRmN9gvSu9DvPPuueQ85%2BYEayVpg1Fo6am1XuWyPVdC7%2BdzUN2rRxFrgXMiKYJebJPPSrr6jWga2hphCAh7yoylynfatnIK%2FXsGTEAHoLzTiH4geZGAQvmi7j62A4PEr7NW%2B%2F6CrIvf3fHD781sig5I7KZiMTbfZPfJ7pt32qmgo9FeZUiWp%2F0r%2Bb18z7OgxbgH4BAqNT897KVWuzn3HS38bZxgK7KpEir5XXffTA6KABIdOpaUPnAONbct7ke5LFMdpKw%2BNDABPOaZXE7UlzLvWvGp%2Bjas%2B%2BynjswN1D1YYoNV3CCPYSUQo2MjmShLfhDUfdgpxuXt%2FMBenisoG8iotY3u3CDDQ17xGoLqacA%2Fv6XfVgPFBdH7f5bMskmP4nhjr5qfDr6Yq72lmr2mnFvFFIDg3j36oVAl6HtEx5CUy66WlrW1XwKuKht8GpUeeWD4TbnWETwMHn2frzr8Es6d4uxddQdcDbsln91Bgjc7S0dTkr2cPTG0xuD3ZhC%2FG323OP%2FqAd9FLjKdW5G4hOHmtgbQ2LsQrcPNEbBWY%2BztzB84QAxdAKJ4T%2FuYX5TkXpVMPz3tfA7FY1n9m1WuTn3LJumvZMO6i7LwGOqUBC0AccSKtmCm28yY12IiRGfQoBfbkzk9Jvvhj9v7F3dAkzKT5yvdTws6X6dmF9l6WV9davLchI%2BgBih%2BLd%2FfaoerUcl3AjnqhcPWm8wZ9Be6yRnuSxkvAInuKRTTyeT74IMR%2BVXwHOYZTERazjuMJbEGn8NyAqGow%2F9yk0EqZifhMyxgEotsdFSvMN0kN0pyA88jh4NckpsF7Sl7eyenZ6ow5dmC0&X-Amz-Signature=4dc6a8e576bc7790dfe3f259d8587baa20c6a5767b954796a2af380d6e8e39fd&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTFT43FC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBCKTOFdi2nes6N0a4M8NZbp38JVEDRbCmWOf%2BJPPSyTAiEAtHT4eLcoxkmY3msLFS7gkV%2FROeFyqTbYukUbVVeWBGkqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN1VCBKOhHrSkAcacircA0CKNm9dYbGO%2BbetDywRGEPZqNxQYEptD0qblyezG%2BXT%2FlFxQhNIRSik0qlUdxSuvW%2BFn%2B3o8X71ECHqD16C1PLhzbX99c7h3TR49aca34xk%2BJOlMOLhy2UTTA%2B44HcEtLy4T0T62csEMMu0NP31LLgU1NolmZ081lg40vdOGXnBrnGts2aru77D4H2rXHTAnzw9%2FdHfgc7jVsWPYDI6b%2FuBz8dAK5MBg9NtbnS8yvy3qOtl%2B9%2FHQgNuoZ%2FIdwU6lNAKv0Tpe%2BxHQ%2B8sOulCsJwbEq8O%2Fkkw3fqgJIPITw2w4T1wnBq4HF354Vixlhq5wNIIipqK8bD3hrrjWh1p0%2FrwEnLBfcBjD4wCOiOaE%2Bf30wTWCx%2BaZ0mIi5GmrvHSTYA38o7LIOwIidglbGvadUDfplSwcFFSGE2Wm8xYofGha2p7A9O1reHzPq68v4cNYc6Id3Z0kNtFunpc9zKNHuzBBfH9S8t3i%2BP%2B%2FZi9EIcjsS06Hf01%2BeMxA0WK%2FNtztCtpvO4%2BIArcfTyaai6SVRiR6an6gRxR2%2BWSmYA1LSIOJqmDstXCLeCfJRnaZeY7DmXy%2F7Ga2HwC1OSAnUy%2FDwq8OOTGhL7BdavwaJ1akOsI65CvUp24hybyGjEMMJWj7LwGOqUBK85ijwmEy%2FYpLrjVkZRP1Z1ZtZxdoJsZV0kit%2FzRpWsGvotzSEtuJoDSRTgcgvICcnvHYX6IBM5m4wvi2yXR%2Fy2Ss6TWZdT35nz%2FTPoId%2FILdPdzDdF6etM0cc33%2BWpr6RhfTkgoF7JgFqX4fawcOoF2wtGfTl6vIJX36bDsViS6fyTorqp7kUYhVbPcaAyYwXlLiEBXZ638t1dIrvB4x9YEKtEs&X-Amz-Signature=6e1e31a4ceecea5b4009af48eef71586983611d4b80c8f727e74717142b33486&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOHPRFFV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkmowcNUHYmtxXp1xhkZJSP7OiVoWiqB1o39pjk2QQawIhAL14Zl3hZXu2N%2F1nuKUx0BCbpgEA2W7qmhWAJCFkNsUAKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOkJaxP0JmwWKjTGIq3APiDhmUUf%2BXcRglLi%2Fl7SZZffT8w8KK5Bbepdur4xXgxzLs7j0gHDVP7RKL93sV6IGwpOS8yb1iavzbDVE64MyV4w%2FyDJTDwY3SuiWtSOOi5%2FLIaa%2BbAeL8qgWPc5c6RW%2FANZEXYs3OvGsyCyz%2FqbCazKlJMbQYyKGUQEUslyNRLJUPi7TrTThtXWZ0pawtktsXsRm7NiFFPOtdaz13R7463UBsfE16vneVFPezT3UitFEGZlVtf%2BsJ%2BBPEM33pQrlK0nfRJXtdQGvNIyVgbHucMF88AX1F0UD1s7HsxcsRDzJNyUS1q9GkACdB9qOduCsvH63iI5xiekrMKPhQtW1YUwmvBNxGCDlyNrK%2FMt13w0uTBSkOpq27TLgBurV%2Fm1Lq6tGIcEGxDaLQcBfHXkecZIUYLlLRi%2FesCNMN%2BNYp7ZsWwRae3vs3vyt4HuKsJryBPLbl6GPQ%2BunH2Cn5S0ReIfKfDr5U%2F8LbBV4pW1wmoNRPcxgMqcLBye3z37ZS%2BxHkQhNhVx9nM2D%2BkxmeJJr1f9nQ6prBKmC%2BA%2FqkkyCUKV5xjAUxmIjgE9iaflK4RB7V7%2FBtOZaRQk9uFqlwV1rSAf%2B4r%2FsUzKcU0tRkqP3L3hk1RYehGwyouLzvHTC9o%2By8BjqkAas1JrmJ%2Bv542CFOz6nsihMlJMnhfDsDQ%2FH9q5yyy0vuJSVGAJ8%2FVpMQKCuNLKiJuONURj8hzW3gGIryJ2FFnMHaSMb%2BAX6rTwI5RVGqrR574pWWsIlQWg0CwGq7cUX72gA26PBUU6t1PVkyWLPBNk%2FFSMc%2Bx18eL90py6ydTUriTbNFRGHSPoJ9OizZLWFg4SLn1eQ44nZ3SW12TtpU22BczwZK&X-Amz-Signature=7f3a2a0b3ebd196c6c1fe262103bd696108000f3eff930953c0d0dc5834438cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFM2MBVV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJtZDwjtnKpDqFmbHP12Z0xXM%2F1lya0OSBwMrqj3uvewIhAOEJQXg1qUq%2Fz59OiBcEO06f%2BaQ6P3lyHneS%2Fav7sk%2F1KogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyFZom%2BIzbL3v5ik4q3AM93JD4Dh2lJpxBXwsyUiIMY7t70kK8lZ7iSjJxtEUH%2BGdKLMTv9WK4HtKbff4tbM1fYsQDlC09qUaxR1XdQQgC9E2YlOSH7ljWTADHulgnOPfhZ7TlmCEoJCHJHNXYdiyHs9SYd8JaUTQbNk62KezC8GBzbKf63ud8%2Bbt%2FWJqjLOzm4qv3ADG5U2xNmn7y2%2BR4shwUvaZT87TNhULA6N9sXCPcBpfWxJdCAh%2B%2FxENHbPOrhNwxrX1abFX7yNXK%2Bgild93rsmXKPe2JYGBzVtPXEO%2Ffz21WkU%2F7cJvNmdcjbnCKsxnal1w3TKXcgRhRgOKZHtTTcoqSamckxdGa3sdSntDndeA5wc4VE0%2Bv%2FleYNe8ZvkniFsihDXhA2SGNNtvQzYajf0AL1QuYPOw8MFq4KVUb3RSK8F17pBZAZHlJBZqxr3bXWY7%2BEe1fW833yCkesdgp2mDHdPVot%2BeScxvGA7MQZVZKnlYf2YNJj0bJ3szpFA81KYc1SmsbMOIqy9M4JuR6IdAQlZ1ZKcBul7wRHIpwMFWjYqx%2FFBL%2Ba%2FDy61KSKssJov55rX%2BZsgNvw3afKs%2BqwgQappKGYQlHYY3kKNJwa37ZL1fthyDtuSfuKs%2B6%2BEFnC9xYdlFqFDD7ouy8BjqkAbhpsDv3tMhtk96jP1x8Uyicc8wm2t1E31cOxLVeuTH07iseUJ6rR4WlVRi6%2B2qXtMc7UqKsKKXr8EY4LLPcu4F%2B70dS9nwALNoeJk3aUpNenzEDz%2F%2FQl1PaWRS5bmEtXPYiZgByukwprFz5ggqsUX1ReEw3cviQMdrwVxMEvYA6bzGiD8SfU5INNzpIfwpDEqlnAncV94Wijp7s1wILe%2BVP8htw&X-Amz-Signature=0529805e8e0689d12e546ddf62dcf886c4f4614bdcdcf0b87a8c594ef5e917ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFM2MBVV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJtZDwjtnKpDqFmbHP12Z0xXM%2F1lya0OSBwMrqj3uvewIhAOEJQXg1qUq%2Fz59OiBcEO06f%2BaQ6P3lyHneS%2Fav7sk%2F1KogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyFZom%2BIzbL3v5ik4q3AM93JD4Dh2lJpxBXwsyUiIMY7t70kK8lZ7iSjJxtEUH%2BGdKLMTv9WK4HtKbff4tbM1fYsQDlC09qUaxR1XdQQgC9E2YlOSH7ljWTADHulgnOPfhZ7TlmCEoJCHJHNXYdiyHs9SYd8JaUTQbNk62KezC8GBzbKf63ud8%2Bbt%2FWJqjLOzm4qv3ADG5U2xNmn7y2%2BR4shwUvaZT87TNhULA6N9sXCPcBpfWxJdCAh%2B%2FxENHbPOrhNwxrX1abFX7yNXK%2Bgild93rsmXKPe2JYGBzVtPXEO%2Ffz21WkU%2F7cJvNmdcjbnCKsxnal1w3TKXcgRhRgOKZHtTTcoqSamckxdGa3sdSntDndeA5wc4VE0%2Bv%2FleYNe8ZvkniFsihDXhA2SGNNtvQzYajf0AL1QuYPOw8MFq4KVUb3RSK8F17pBZAZHlJBZqxr3bXWY7%2BEe1fW833yCkesdgp2mDHdPVot%2BeScxvGA7MQZVZKnlYf2YNJj0bJ3szpFA81KYc1SmsbMOIqy9M4JuR6IdAQlZ1ZKcBul7wRHIpwMFWjYqx%2FFBL%2Ba%2FDy61KSKssJov55rX%2BZsgNvw3afKs%2BqwgQappKGYQlHYY3kKNJwa37ZL1fthyDtuSfuKs%2B6%2BEFnC9xYdlFqFDD7ouy8BjqkAbhpsDv3tMhtk96jP1x8Uyicc8wm2t1E31cOxLVeuTH07iseUJ6rR4WlVRi6%2B2qXtMc7UqKsKKXr8EY4LLPcu4F%2B70dS9nwALNoeJk3aUpNenzEDz%2F%2FQl1PaWRS5bmEtXPYiZgByukwprFz5ggqsUX1ReEw3cviQMdrwVxMEvYA6bzGiD8SfU5INNzpIfwpDEqlnAncV94Wijp7s1wILe%2BVP8htw&X-Amz-Signature=e2f6b8155eeb6145ff48b8f07e48a7c5d3fbc0515772c4e95648e2619f1957c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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