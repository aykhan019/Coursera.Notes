

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GQPTHMK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFlfHOIikSpeLKyl4TkRTLH%2F4C7DI667FUIaFLy33tfsAiA0z8aQ697SE%2FtQP8itfkdc1E7hz1eBLd10AwcxDlaMmSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwDfxdwDZlODTW5MoKtwDNAXqfEIPxDRcp3DkuIwVGbO7P0IQjJZ0%2BHkoE9rueKJeHiR5QqSf7XroSVChMD9Dqy4U5MFPyMfyxAajYRIsAlDUOy1zhM2nqk4LW0rIrvM7m3AVq%2Fi%2BQSD4bYvi%2FxTP6mYVwkguMHr7CBbjFcAoT58mqgBpy8VslViNSNr6Wwnp%2FMXPT39z%2F0eQgO8M9zANzb6VedkhgBOlk5%2Bcsl4bS9wUdrQI57SVLnonyFC8MgsPe0kcEzrMntW9gUqyJBgI0QLUf3wb0W3ug2eLNmdULvEUL87jRdeSUOZAzU%2BTbOpGvtG3ogmjJxlPEJop7p%2BxII%2BqjPp5ya3StReWRXmmw7o0si5tLVcaJmWEFHhgmsvTiOzgALca9eEcMdtf3tyMFg3LvFM1tDGOmPp%2FNmRTvb043E4WUu09sYQai9Fbw5slwQPsN%2Fw89Ux7fUolJwJG2O9FxcxN42rScw2oRjGX2o36fxw7MVUOzq89ry2QkvHDYR0LILUGGT2yyedhUsFtpyzOAFxBHp8LEuUxhJfoEHMkTh6AQHT0oHiLsH5NovxANLa7b36kmxDl57qc6iOAPN3IpKg%2FXa0MXokPvXk5aVd64n9YCVSPmjKpTGLObgRkxIEU%2Fk8omj4rMRAwnMb4vAY6pgGNV5quXVVfDGOBKNgU9trBa6REmLpR3F4X8x07sPtS2T8h5FSOqDAU12NW9K8NoStjpYMytmNUBefvyfawmZLAYBy0YtGdR%2FxJm2wce820%2F%2BE49VMeeAMM9OKUgnfrls0D%2B9sOlpSulHf%2F%2FnBGSh0amLTAHYU9NWHHHuttneCvQfSO5euwNMWyPnwKPROdf%2FcYIMfwiDi4oGMPCPZKyasj3kRAiYTE&X-Amz-Signature=70468942a97eac6a33e623b756bba527d0f9f65b7694271fde4e8c1f02b7087a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676XKQ2VG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGbMFj7EqzRsiwsVlLlm8sunNjWWgrP1aJBJEQH00YrvAiBteA0PDwL0S8dp4Y6nbiVxkwU2vkm36hLmlYSfdavhcCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzxC%2BXRYoQ47telzpKtwDvODKcYGxToACse1mJSFvbKwg%2Bpz6NysmhiVkORGSvkJmZ63z9hJ6ib75U0Is%2F7sA1tlaJDIeA0JWxq5ot1ScNC1lDPkePZqAdbL%2FP38LiHve0fVrHJNrgD9Lfvq5DbbA2C4jIba8cL%2BqzxIC02oEACJ5vB%2FsWaBo9XjGl%2Bqjth7kfY9RPLtX8VNjzH682NTP4uM4%2BHvvfaJx6wf78z0LzOIT2ZKbHgWllKdtDv0DXYJksZEKEyU9PkGEyN1g0vqXC9Sz5qTzvMYx1nAdNCw1yOxt4QfXtgopb%2BWthiACIZLmhXLm%2BqhlGktZxNt1u4ZzKdFzpGciF5my0eFTic32nmU%2B1dhhwL5VEsnNd%2BVAPCTvIR13jaP6pvKH3%2B90dIsJ%2B0xw2LrDJQ9ddRcOkHL5af4dbdDKHLIwCyncv1otImGvs3n0%2BXmrFk5PjP2Fmoosxv%2FM75OAmM9O8h6hI5EKTo2XKJ3qN0o6MBUyIQBQY4%2FMfF1FecTOoOI8HyFyyaLX9xqBJnlrzI25egayYyHBgyHUfVY%2BkdNIFoUZ4ODLQ2Xsqn23RS09amibQEfsKOxbG9uPKMxBqZa97oEomUEhYSCelPJ2LnVL5%2F0ujnftBvqP%2FfyKc0m3eIQ%2B5YQw9Mf4vAY6pgGRO3jizl%2BYqts2AHRXXy3jSfKeFYegSy2AcOyVDKotFoKZAFeE%2FNkvj7t8q9XV%2Fzc54QKLtzYUKitLKi5UiruiUTn9q506vccvBdOWcEcMM5hx%2FQCTa%2FWHNJ7J3KatirwlJf3jGWD%2BYOj%2FAVY5y95lt9P8xpVvDd9wrzw6yrQhKSL6y2oLGK%2FiqtKzPnYMn6nmByxdrsHO8WPySuuuH4oI3IX7GA1f&X-Amz-Signature=bca8025e6d84ef4d5d0966bcd3455738a300c97fc83ecc2053ef965ab569aeb2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656L2YBNY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhOnSAMuwpff%2FGRyV6EcCU5mkv5eOl9aNBYHvT5rwJ9wIgR29OU8UaXv2RuQhm3Z2M%2BjmmxsTFKRlksJDe1dpOY9oqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFRfd6fTUx0G60KayrcA8i72%2FicLrEzVrNU%2FOOYn3MJYmy8GV3VQe8JG9WXdHWcjQz3LjPp0CxMV5jSA5ZyuV5h%2Bk56YXbkDBCcOhbLoOQquzknAhOltFEZXkl6f6wyibcFpkpM1BStd7ybKamEbUqkR5x7Lp3%2BHv0e5NZTtYwBbFb8WygNPsEipB0oL4bJwf9vJpuXdohUF4p11kAXYfS5XdpPAIJNrgOtYcoyqgI7J6J3KT3Xf65zzF9B3Oh7EzkbgqhLR6d%2F594vMREkcCLGXUS%2F1ClEC3eEqykvi4MsM9Y%2B6PSJEUI9bCR1Ro9q2uan9QcypbAzZAwm0KtuvNow3sBmxrEt8KbKnsM%2BwRgcMI1XJfMRX3dZPymoxx4BSV6q4CzbUij0u%2FHDMaD%2FBWhS4szRZa15KSCb4kkGiwxyy1WjXUL%2FJn47axi3zZRyuh6%2BfS%2B1c1gUYaJ9qjx5g%2BfCmLl%2BmHGL7I5yUDCO2CfaSL3%2BUrKFc3kP3aBemdNoDd8pPsi1iTVhbtks8KDCUEZLJfciIFkO25IvP1qLDvaM2a4kJMKLQ8JmPkDfsNj4F4YQ32fODE1yIS7foH5%2Bi5vBE8BWTmtHw5X0997mL3U9fTy365pjwmeVGaAUld0Cjy5dx8WR09nrwfBfMLbA%2BLwGOqUBtWh1Z35ieM6UuvRiJMdvqGD5jb6BJSmyBD5k1H%2FfMZrfpcwJGfm%2BVn6ARkgwDZk0z2TwIF45u91w1fvtlqLaqfdAUfoyU6q%2FHwT%2FofdAWHPJZKc2%2BQNejxAcrDCO80C0YDze1j4QjPCHxKJ9zGH6S23HLXV1w6%2B6BDXC1kQ4oO5KTzTfM7PDjOnDC4kSUIU4i5L4Q3wjtLuTs7lByIFmK9NM4eCn&X-Amz-Signature=d0a9c67aa71fa7ee9a59d1cdba27c8290992c195b4f782310642357815ce4ba5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYD5C2WM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkXccC5UjBdbOYtagqm3wAp38bm3AYFnzR5csvaOEHYgIgSU2OQnaPq6YrlFPBMTBK35zv9R1bafEp2bvP1PlPRLMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL9HykgiNNYT%2BknUOCrcA16HhgejO6Uv6xblZnXF2S1rsQpfiilp4UlDadoeGwjG3ppAxscmVoqP%2FFfyN4Spo9kfOOkHZM9BiJLmgTd2zGUKedB%2BIC2t4i3IuAzQdua7XUVMu0fJkKNu35lvlL0m1BYTb0yGvL2SU1JhXHD8IAoCoJoVcLH75u9JvfVHQw9T9XmT%2FMjqCIGW5ZGRzYB2ASUV5qkJsFG30f%2BTLp8r164R7RCb2v1Fa6ZzLRbx8kV2wfPID5UVIbkIWQanO2vdMItRFyxwXbnf94QcOE2mg62lNlOBw4W1jAzr3mvvtjyfMrNNdhUZJnkkXZgGu8klGwNs%2BX0f9x4WI5aip07xzxECa%2FsvwcvDWvkKMBRpSKlFerThqyggluN5UjhaCEBbzfqbfNT3GsIn%2B2SWJu7bhFG%2BgkdYtFLkcGPa6GGaUeLC9O%2Bm%2BYjjXUZI9mp62NdqbxUprrd96TAJKx8PbaylavhuysYebDAuxecNrx4vQf6PQIxJ7S5dWQyLtgrxWoASueD0WAcHAGCY2vjNEK2ecspmAwhwD2XWMCUZMA02E%2FwzaaWSmStamY3IK7Zz2j8jj9BcDTOJit8C%2FBlpQXaeC7UWEgVjkfbxgHXBckogU9KX1a7dgU4LfpnTk2kjMJzC%2BLwGOqUB4fxrJzI5%2BdFZWxIArl0KR0GMDBj3cGNQxamjhh%2BhqOGNWaGsrc3%2FEcxDB8hP49nkWYOc3jFs0ly2fNbHTdUOXlbS1kVnZzFYesEU4TNv0ZXHvLDcw8Uzol9kkXUM6oxtMbvBVYWEXQUt5hJf0Y%2F5VU2V4wjC2IZOiVuyLqpCE6YCR5Lrig4z9lDXdQUnUU0eJK8k50UwB%2BZx3r%2Ftc6zl5jIJNHMB&X-Amz-Signature=81dfe4882f28aaae3255cb475497abec8db4f6374e904220d098d09dee478251&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2VFSRIW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBurHhP601LPKmt2aUoxzImJiLYPPRUwmfHKjlaTS%2BR0AiA2%2BohP9SdySvTC2EM0of7cCc3aUoPjW7FaUOnDVvSRZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2YtTTENcnf2GDkGtKtwDFAI6KiwE%2BrKmDqxVFtI9YUekfwRrgvnAK4bkb%2BgBD4ARM3VxheMHu5Jgv99Ar4Sg21TtebLqxhlMaSPPhFZEXeC7pNnCApk8e0rHBAK4olcfkEaKJN49GhUiMP7tS8zFOig9HvtJHEOYg4oIh5KXdVtynoxGi24ejWkG%2BF8mhmEEJMys4CObthU98aEJJznVpHrDSAtDUJUkX5OJvVO4aMM7kuOtc6rDwju6JH43p1qk8D95i7z9yi5f4byxQA%2FTWakov6fQM9SoT9GlsK%2Fet3uvTg2J69wPc%2BAQe4wH1VeaYD%2FUH6unNxb%2B1RL8jvbFjxSljRYX2GsTGs%2BlSABTM9ZuJMlrDRdsHvkcPdbpIRIY0hW60DH6RPG4PfedqoR6heAuNdqkWfbEu519z0qKnszeGVRDGm7tRgTwHGklpitq1p%2FC%2BGrvanTGBLH6HmUb9ThBZx7sgqgmU5wP15BIF4PBSTGyg0JSZecdnTocYyQFGnv0c%2Fq908OaEe%2FV0%2FxiwXGGt8mg7U5yHuG2C%2FDSxNM15Yv7mPnjwG%2BQmzhIRh0gqMgBkiK1ygXpllCKkNZs%2BLHMKnHa%2BfW5tfS8ma%2B4v5k4T4DXP1GPBi5qdyN79VzbGeVUbjH8A%2B3EOgwwo8H4vAY6pgGymVtSlSt65oD83ANJwRLC7JwgAyKbYzZ1BhzYvI57s4z5FlcSfDbLewUVEWVWtA6KY8obKGF2Z7l3eLqDMaenIdtEuTq10d3DC5aierbgv34zUk0CFm7uc5aeuGY2v%2BOIN1k7CPFK1mG4aAAKhoKSEQ3tVol%2BuNnPty4nxYQ0rSgO58SZQoUWbdFFwwV5Wpfz1fGCKIzJHMcEUNpKgF61xPTj048a&X-Amz-Signature=f80e6ad143722e057374fdb8e582021b0872c11a3239adf034eb5a6e5bbb650e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KM7MT36%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHnsvdP4d%2BwCwfqU7FzHZjpW9VOET6Pb6wU8czYTgdlJAiApw5CWHMEXfJ1qi%2FPMi7uAUzQaB4J1WWyHdDPT4Lik1yqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT2YJ0HyQLfA3yQT1KtwD9lRy34Dl%2BlsVn0hKNuiRZX22qNWswiDu76ua9EKXEn4%2BdJws%2FoYiTpj3JG60dORy5DA7%2BlY6CvvIivC2n1j8q1HboCRF4A3MHVUD22s85W6%2FvhERv%2BlubglcVP1kKMdQpNtV3XE77cN8G0nhP%2FxZu%2BrI0EEaNpBKZ64RHVbyhC6dd8iY6gkDO9kKu%2Bq6%2F7vLNWndf1kTuxRS8F4OfQeebBm2yuaLiJ33rAWGHf3ByY9PQQrbf2HZVLn%2BvbXvMVEgF6ie7G4JuWYS6m6VBEXbo4jONvxfEkva421C5mIBHqHbXxpyH6G8IcleXAITJutzPD4W%2B4uhoK9LE9cP4OEPrDd9MuZBWQFz9QXnzVbycplE11u9izzFplo7Jfa%2BBEXrujOlaIPf%2FOMbB2MGqwQ8743YdKBUHt7SH%2B9VTiV4aY7xHKQ7YmB9fs6yc0JKoNhuBLOhxFcChh6uBm%2FRCrZRn%2FyMxrGajYU%2FB6hQl97Xjd0xBtLpHDt%2Fg2lI1aLqDRfpUV%2BURKYoKK5EkqNd7uSpvZAYOFwkjRr0mmMvCscXIdNh169kV14E%2FCqts7FqiZLKM7%2FUePVrmS%2FIpk5F3Y0FjjlELuwefaHUJrUGDwoQf%2BnJDyQ%2B7uXkjw2G23wwtcr4vAY6pgGktlxY5XwGQ9sy6UB%2FyUtw1%2Bx17MWhnZmXP%2BLbCfJVthOenCBVmevF6uEuCUobbfk36TOx%2BM7jzpmkzGPFEwgNcIDM2Jf9Az5z4AmGyod4tCgNUNJNZ7mFdpvzrRkCbS8Vs3z0LKoiHvuK39Ke8t9vNvNYI2n87cZjRe5rrBfnyqmj7LMs08o3LQ2yX%2FzqS81UPa6Ma%2Bg%2BHw0mXI1CKDyGzczAqPpG&X-Amz-Signature=074a3bf0f07d949999801cb7d285cc41afda12dd81c632b74eea735c36818439&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBSBA25I%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAr8Z1tGezX9NxHytD0XvUKroili1V0si7EJN6LCcV1QAiEA63i4CXhOP6VYVNkSwYmVNndpC95plJcdQutB%2Fgc8QOUqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPjH%2FGlOJzaq5XVuCSrcA%2Bl4XvYBwUc8NBOTQ0xWkFoexHrJwI%2BCcSoJ3GADW3jWE%2FRJNMAeH9HaZ7KRAlQyWfx5D%2BrpiGyxrFphwL2Vu35cwnCCD5L%2Fes%2F58PwFOg8PS1CQTpD52RxYqkPbmDaE8zhaE2n5JuZmZTFS3nfPh8MUUT9RI6zEm%2FT55dLYwPnz0Fldd18lvwjfjbBTm6xhVcwbfBORjsFWiAKKMy0uBQ2Mw2DJWZ9G8X%2B2Y6oXzredEvkmC6g1AA2pcp%2BuWe8YUyfklq7jZgS2io4D6NVNlu0yJupkyI3wDVLGNTejEawLk2VmGfPKqDYcZc3YYhSrntJ%2FXMvafY8%2FdMWyVisBtBAaLoeZGc9QHOPEs%2FeG7rfRyrAihNddInk7SZi4TERYUYEz4mPx1piigIMt6UKNeZMEZspUuvInRbt%2BM8ZjV%2FV5nR6mRDlwyMceEbuJBwokJwxRoiPgA%2B%2FX%2BtOV45y5E8cmgpuNSLm7qJEC1yee87GnFzunYVVKLdts579sPaQYy1qgA6vNXS7eqlClQ1HAALhDzqGWrXQifdWN5pBoLQv6laHBbMlZk3H8D0p%2FJSTooUhANya0DFB02JKORmc6n6V4ni48BTk6UEv8mym%2F0jcfQOv02MTuaWwr1fuTMJPG%2BLwGOqUBBGgDQklB0wzMZiT29OEMSA2VvULb4dbwp9yn2YYxINpCsd0nVeON61h%2BC4YAhys7rknxprCnC4Uiq6alBoEcjHxomyYadcmIjerrmQgKeGwnGJmVG2bB8rGRZ3swagpChwLn%2B84YIqoXmK8HtssdvxhSyePbp4DMX8Jr6kql8Ob9RLhkKmvZ1F7RTFRw5YZMq4IcOLg5yX6l276CHp5hQx1Mg%2Bql&X-Amz-Signature=fa3bf03cf731e4ff0854821f2d27b747f4508e4a9d4f34c34b462e49d5ac6ce1&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS46EMJV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUnHL3E5dA0J9LlJSx0b0AYjUAaAcXIYmO6OHV84r%2FPwIhAKK5PfBrt%2FYVIgcGg6M%2BeYNOhc%2B9ndH9uRfOKoro0k4oKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYmA2JOCR%2FPBJrl6Mq3AMJe0Av8Z8kGHWpuClbapu86CWY0ACqW%2BWQDQWmyl6zFyKByjXPyPevEv%2FnUy9Fog%2Bd2Utkd8CW6TbxRm6uRSNzZ4Jjr8ziCiLxOe5CV6LIuK8rNt9aY7pvhVsUSjVUIROAuzblf8Ia31pOa78ls1AuzdjS21SKSZX2loMZTxIb6eOCI0KrMEMrVdQMQ%2F683xhnqhNO1FJ3pjcjsXZfXVAbNBsyoVbOoGqWvdklOtmPiwghErU4Vy9KGpZdGSyVRgwd8ChPuM2sOSDdbCnGAlTYvAKMyhXIajy%2Ftgay6b%2BFwevyVXF9F84HImVVM2S2yOEgepxNqg9bZVlnKo47h%2B%2BS0fELtNmC3311JAf4Rh%2BDJ6W5fcZyxTrR1LEWYWnP4Z676FPS7ms2WlUGKrIMwl0V0zi%2BlOrDnXaEmbaAjAIzCeWzh3kNa9Q5pCdHFpTjYvnXw4gREcZLxGQUL29e7Eiufi%2FWwKWust%2FngR%2FhMXm9FMuk3sKleyR3DBNDVjTABocv%2BtaDyTqB19VPBeUIw3fiUAfpHAVHCSHw5XfYu2v1m3cqRBcycqPHzP5YEDJkBMUQpgSJLwpFD%2Fs7I9qUsx3toKtfboIqZEe6hQRre7vC6qQAbOWmSxYzjTpmnDDKx%2Fi8BjqkAQbQlWA2Qm9jXF4oF%2BXtJdEaeVwixMk560LvNYyob6hoXuJZTFRuqZaTnMfVev3Qi%2BrKJ3YjvlxA%2BgH1Twk%2FlB5nBfIiTB2gpiEETWJIocE%2BDuFtAYERWrrRWzBqq0r5Hrsn23V2%2FSdtuc7HRcHXtBYLXtYj2CM4eDFYykjPYdkcrbj81b9SWljdtnOn3Pql1ehgzPZsjj27m7uy%2F1FFKwHuJz2h&X-Amz-Signature=154df5a3b0c51bcace8473fbeb3151188cd2cdcaec24141895a32c14d423380a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2VFSRIW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBurHhP601LPKmt2aUoxzImJiLYPPRUwmfHKjlaTS%2BR0AiA2%2BohP9SdySvTC2EM0of7cCc3aUoPjW7FaUOnDVvSRZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2YtTTENcnf2GDkGtKtwDFAI6KiwE%2BrKmDqxVFtI9YUekfwRrgvnAK4bkb%2BgBD4ARM3VxheMHu5Jgv99Ar4Sg21TtebLqxhlMaSPPhFZEXeC7pNnCApk8e0rHBAK4olcfkEaKJN49GhUiMP7tS8zFOig9HvtJHEOYg4oIh5KXdVtynoxGi24ejWkG%2BF8mhmEEJMys4CObthU98aEJJznVpHrDSAtDUJUkX5OJvVO4aMM7kuOtc6rDwju6JH43p1qk8D95i7z9yi5f4byxQA%2FTWakov6fQM9SoT9GlsK%2Fet3uvTg2J69wPc%2BAQe4wH1VeaYD%2FUH6unNxb%2B1RL8jvbFjxSljRYX2GsTGs%2BlSABTM9ZuJMlrDRdsHvkcPdbpIRIY0hW60DH6RPG4PfedqoR6heAuNdqkWfbEu519z0qKnszeGVRDGm7tRgTwHGklpitq1p%2FC%2BGrvanTGBLH6HmUb9ThBZx7sgqgmU5wP15BIF4PBSTGyg0JSZecdnTocYyQFGnv0c%2Fq908OaEe%2FV0%2FxiwXGGt8mg7U5yHuG2C%2FDSxNM15Yv7mPnjwG%2BQmzhIRh0gqMgBkiK1ygXpllCKkNZs%2BLHMKnHa%2BfW5tfS8ma%2B4v5k4T4DXP1GPBi5qdyN79VzbGeVUbjH8A%2B3EOgwwo8H4vAY6pgGymVtSlSt65oD83ANJwRLC7JwgAyKbYzZ1BhzYvI57s4z5FlcSfDbLewUVEWVWtA6KY8obKGF2Z7l3eLqDMaenIdtEuTq10d3DC5aierbgv34zUk0CFm7uc5aeuGY2v%2BOIN1k7CPFK1mG4aAAKhoKSEQ3tVol%2BuNnPty4nxYQ0rSgO58SZQoUWbdFFwwV5Wpfz1fGCKIzJHMcEUNpKgF61xPTj048a&X-Amz-Signature=3e9f47c0af1233893c0d3f1e81a7e292b3445d53968b214e1e25f752c223083e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPU2PXZ6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUgfl70QqAbGTkhQ0o2JBWQl3UTb0d30%2BgAPug73F9TgIgNuxUCY9DH2UFd14WeFG4Ev6ZMwWYrVcOpUWviAEFsLkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM09e1ubhKUv23sm3ircA8kC2RcXA4XhhIq%2BjS0gz2cdSHxeM6QJ5X4J%2FsbVmUZSTDaCXk9DxF6sECgSRBa1JS2X1QondJOwhgmfMezRxO33EwFNMAYEO8k4txRBYA8cTDhXxsdgToyYXSETHnKZSdc5HelUV%2Fy8FC8iuFMOk%2FEzyurS876bwxGHRo76dI4YPsgPA4LPLLIul1aRl2ECxZrSyotV24SEhrlIVYcluDH2zt5myFHhl0GSihiHFLhWBiUgtTi87Me8NTLC%2F1ZWxPradPJhmrawm4PazjE%2Bv5984rrrG0IqzsjGd28nP2otW89JjGjcoLTcrQJHlaCRERH3KKDVA4W0InWPxFIUySs6uQZZr1mIBIxv2P5mwX5duU%2F%2FoG05lxMS%2FmUlkP0iBHr1q8MQRHedynxotqR7wUm8TwTa0vnrbf%2FF0WYF58LkTBt0xQ01Uai%2FuFmmsyPDFmnRtF32M0mZ0Rxw2oyuL6CfVyXPcco0gyLCzq9Ut7RJn9NexHiImYViNnDQ1hL0JhcePoKv%2Fbd7GW7tLOAPkn%2FlJMhIcJQFv%2BsePvbIKRJ7U58%2FbjpUtxlMkb%2FIfs5KY40jb95dBok9EvT0Mg21YOKsgWttG437qOiFXcVN9vRwpRztg%2Fg3Y7JgnRfXMJDI%2BLwGOqUBz4DBFh2ATj3QxCrGk9gc5kXDsOYWEJfVzIGPUipZqbXS33SEhAdctu7VNb%2BXO7PedkluGlkKnHbAx%2Btp862WpQhj1acwLOf7sObCgTCt2P96b1iBVr9AD017de6OLLdjOIdQliw10vUWXFiLBnII3upUdmmBDQMWCWQJ0ArEF%2F%2BRsMwHqVKGBVYrTautekqFOoyINi7iykA2FqgCDuXdWU%2B%2FIY5u&X-Amz-Signature=ad59fefa2ab9fdae155ea359e2fd366e9f6da13a0cac82f2ff251add2627180d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPU2PXZ6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUgfl70QqAbGTkhQ0o2JBWQl3UTb0d30%2BgAPug73F9TgIgNuxUCY9DH2UFd14WeFG4Ev6ZMwWYrVcOpUWviAEFsLkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM09e1ubhKUv23sm3ircA8kC2RcXA4XhhIq%2BjS0gz2cdSHxeM6QJ5X4J%2FsbVmUZSTDaCXk9DxF6sECgSRBa1JS2X1QondJOwhgmfMezRxO33EwFNMAYEO8k4txRBYA8cTDhXxsdgToyYXSETHnKZSdc5HelUV%2Fy8FC8iuFMOk%2FEzyurS876bwxGHRo76dI4YPsgPA4LPLLIul1aRl2ECxZrSyotV24SEhrlIVYcluDH2zt5myFHhl0GSihiHFLhWBiUgtTi87Me8NTLC%2F1ZWxPradPJhmrawm4PazjE%2Bv5984rrrG0IqzsjGd28nP2otW89JjGjcoLTcrQJHlaCRERH3KKDVA4W0InWPxFIUySs6uQZZr1mIBIxv2P5mwX5duU%2F%2FoG05lxMS%2FmUlkP0iBHr1q8MQRHedynxotqR7wUm8TwTa0vnrbf%2FF0WYF58LkTBt0xQ01Uai%2FuFmmsyPDFmnRtF32M0mZ0Rxw2oyuL6CfVyXPcco0gyLCzq9Ut7RJn9NexHiImYViNnDQ1hL0JhcePoKv%2Fbd7GW7tLOAPkn%2FlJMhIcJQFv%2BsePvbIKRJ7U58%2FbjpUtxlMkb%2FIfs5KY40jb95dBok9EvT0Mg21YOKsgWttG437qOiFXcVN9vRwpRztg%2Fg3Y7JgnRfXMJDI%2BLwGOqUBz4DBFh2ATj3QxCrGk9gc5kXDsOYWEJfVzIGPUipZqbXS33SEhAdctu7VNb%2BXO7PedkluGlkKnHbAx%2Btp862WpQhj1acwLOf7sObCgTCt2P96b1iBVr9AD017de6OLLdjOIdQliw10vUWXFiLBnII3upUdmmBDQMWCWQJ0ArEF%2F%2BRsMwHqVKGBVYrTautekqFOoyINi7iykA2FqgCDuXdWU%2B%2FIY5u&X-Amz-Signature=7f88b4fc8831fca736526e7ad359060f6e6045d0e71d21ca8afba7cbd792c7fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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