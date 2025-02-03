

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUJZQ26H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDkWJx4NF%2BDW%2FSAWP5nBmXnCddIeGgEMyW5Km%2FinuqPNAiAG0N%2F599uUMbahTfxxfFA1MdBX3UslscDD%2Fbrb2QN8NCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMZdEhGC3hEk6vrHaZKtwDKEkk%2FqC24j8q3r4o0D8oYu5tVH86BAgXg%2BiDmFADVbpEadLhUYqMzkK%2BDaH4gruuoQ7vrLs8Tj0M8Q1FjunBk0i6j%2Fxtsdnk5ouN7BzB28d29eXuyiPAlNmfDT5J4awLBX0%2B6HBZeBxjEzAoCAttoXRVpzjAB6Q4mXXbewGQLp9mhJigYvqfsxDwqa9yyYauNf%2F8SGSpneaP6sequJWz2vxelIJQ8Yp3%2BAJHQMRObGvwK28J2js8RRu2mdgkRApG7iezSb9bbPcWGsc2vJLJv2%2Bj34cGYnfaMisSDWrqaD%2BVZ%2FnPeUjHucorNgLQBvHVDvC0fX3Hx%2Bip9RpIXxybiVKMV1%2F7FE7zjd18HJsPYp6tfBnYtettPOQeaDlw1oH9Z1CXeOIe81Nhk3Aw5l6TRhdrQjbJvQju3IGmXsMOjW0AvaiTLCMcljYDXSCFbQhZrYfP2xuNCEuaLB7QVrMLkoGe8YkhTJYltxJhRxT41KsGA6sDsOX4jeCoUJNgMnTtVVbkspGI98nR3XxbDYoTlpcmbaiMsUuQMjaL%2FX%2F1yCCt9MIPwtUR83%2BZPqY21YKP3PseSmpu7rzIyPX%2B5wLuFtE5Nb8Bl2p7TO7OKMiT23I27s3EdSMy58K%2FFSYwsPOBvQY6pgGkJ3DYl%2BP%2FeejAwADspXCzDsQuS%2Bw9Zma4v2t3xYwld018fDHX8lDjFpAolLNsqBGkD1xHDAJKukLb%2BDx7eqobk1dqW0rCUEujEUhZN4BheMxxsxfHH1S76aM7Fl2rAvQcWm2NjkXfoD2GNcipdws81%2FZJQ6eTrA7UDq2xEt1pIxBTeL8tj44IcrnHj7uMWyAqMnELZrXzKSIHwIW7nUBfn2BBBtsH&X-Amz-Signature=0e8d24d886bcca2ddbcae0f073680ab95afb225eb416efa9091b45115010510c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664SQHTDK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC0SPacgS%2Fur28fAtx1U124dTkurxZCcbhwRyHOWITRhAiAR9RcAQugqTy77jOJLJHgXrP3acqPrdhq81AvOLiJLnCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMBx09M5Fo2frjtYIyKtwD%2BVt52iG438C5h2uPQqKmg1MwDH%2F0xD9yn2%2Fk5YtDED%2Fc5nilxCIBhPPhNFpbcNUKixU%2FxAQ3yeOxlkBVbKcOtpCQoCqb01PQYanJMw9UqkMmdTU6TRLhheyhuVda7QWFz21V%2FYSyyfC22laltUeFsJFFBv%2FWSSSX%2BNzluMo%2BtbdX1B7zfd075FWbsrFP%2FrWgZIV9Rfv%2BNREOUMS4aYBu2kmDrUc6h2J5fGdJnZi4yu4LnX8jRlK62Y7Ro7A%2FZvCkGWWyd8OVndOlg%2Bp0quIehuyk%2FHj17BSbwoLE%2BvVdcrkbjzP%2FwURPBCrnEvt2LvVOikXOGAdMeedXnPlVUw5V27A7PzqdUnC9D49Wuyh5U4F%2Bidj9O3oVOnqJDbHdzeBOoDDKs4fKQ3clWZVrgwH581LYsObQ91fqYCZHiYrdFkPeEMZfsNQcxP4B%2B1I1XBy9Y%2B36czgpUAKmM%2FTPMc3EQ78On33%2BpJ%2Fww7f1p9lJNoOrT7mGoWlOtIGUWGfZN6r7wCc2d6UbvjbudoeSMQs1y0%2FQSROr0S8IzItNQbhI9dmHqeHfQ4JqHGb2nt%2BA3vAMDG1a6fPAygsiZiDj9mTNA0VpNvmzf7pD5QhQJLyFO2HjhAJVP%2FDsTlhI3Acw1%2FOBvQY6pgErKW4BmR45S01oZcg%2BalUK60IJQYKDtqyMl68vgB8qUb8ygOXUtr0GkXmYmMOW0gyVRi1oVMAEyYVxPYV0CQ24fjV8C0JB4k%2FkJ1pEEW80wjnHCp89FvxtNkCVZ%2BkrUvw5k%2B90IFwG0p5xTp4hydifDfnkjUJRxXLcVvFhU7pZBxmH%2BiNOCYRzqaH3etWRQhp5tCerFvKr3W4mLZgzof9cRoGm%2BXYt&X-Amz-Signature=0fbe1b0af57a1a362dc9e111aba29af488aa268dd006e30b8400f779b2f7a4dc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOWNELN5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEs2WPt028x0YKA4cj80luDauELg%2FQK%2FGaQNogf2Rw%2F9AiBQqmY578dBb0xJDBEkILGQTMMuEsBpC4SwCe%2BNF7saGCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMMCNYuBL9O1k%2FADceKtwDD3witLgKvuiDR5W5Qh6ApqFXb%2FRywmplbtSCrdUCW%2BpuUwa8Hhj5tJONM1bC7q5zlYxfNjfL1Pr4kiXxboZiqHIjCHoDu%2BN%2FSdg46PHD1Jp85LVtE%2FbWqt4kKNS0NMMf%2BbL2n0lAqesldd5rCkflsDTzofzuX9WPEOTrd4%2FcEwoF1StJnzc36v1PGPgD5DE%2BXCP5mruRpGvNkGGwtR8wmKWpo5R%2BFGlhb3jpYAGHQFe1cel%2BMmG0Z33OBJUA64SFDqsnK9w%2BMamwoetqSPZkAxpt95pC2d0TKvxUtAXU4HooWJgfMBncRFiTjWD5Faw06drhEPh7n%2FLGqo%2F1ZpgyG15OZ6qW0%2BTqVcIeUoUnrHzeLaJ3GoIPR5IH7ogNF792CDp5C1udRE6FxlGFM%2FSMKkqdxARclAFRlRQJ039SomDqrTva19BKGbNfm%2FxWIZ5Tr4ZlD4ClJkFXK3FnRs%2FBG1P45f%2Btke%2FQjS1mhrp%2BaGDolL83CPXK9KDz%2Bi3Wn3G3Znkv3Y%2BQgvpr4vPw8kzmtdFlraQVKNtkcv12mlwvRPYPxpFw65fCEZxlAMEr%2BOxb5EMTC94Q%2Fl4wRW3HREWb4Si71ppnFqil1fqT7CZmFP2yAO3wjC2uKaeF00ww6fKBvQY6pgFSvSQQRE6pZXezfSUTyK7G8kAFOFBVY8sPNws7eO2bKsRsLDDIErauC2imWVToIDvsWqb35ZhqbP1R8xnU1AtQbllmIkWKitQKDlRrxkKcSuKooYH6HVFQgm%2FztedXy9qK7y6mXLDKnDwIxwDRbDbHQ09Q6FHg%2FvqTLJv528qAwKxJYQBPe86pDzZNdqmggTr90tk0bUEyOD7cY%2FNHYCUN9cw%2BUzW7&X-Amz-Signature=a97430740a83f5497f244fc66f4d7490e59049564c167768dcce4c816936215d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHSBRLOE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDitNHLErtQmUOo1tTcWDafpCRwm0LwbHL%2FBLJOMwtzWAIgY9B8SSW3udItsGTFgsRONCPGyPUCn3rNOudZ3YuV2PUq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDO5zpt0rvBwU4MB2fircA6BsJyFWFYajjBOnCo3YiH2ObCaWdJSzhCmjMkFW97hLCLj3670LYRqx4KmEX4MusnY7u25iQY7py7bLX6C0zjtte20Pa8hIG66zMJMjasJXe9FXjULNwLSap%2BTgN33Fzq35hiFz5E0A8f64RT5esrjJI5fCLvDfTSN4v%2F8FmkBjrgy%2FBMJ9s6wYh1QuQ2hG9SKGAkqHd0YWMSwFmp2LhXpy3Yv%2FCDqbvvoTxme895C4HYAZRlDCXVLkK%2Bu%2FfUpwAZO4G9jsFluFx3Dic3fR7yw45IGpSifXX6YBqjoSSh6U5N%2FncxTInxWUt3NothkIjVSzfeUo9T9Ah1YYJgkqvtkxjFXdkBMIr8k9JImvmoB%2FbOEKfYtHcjos%2BMwLwq0%2Bar49yrGep8bIH9WvmHl20h%2BtfAnnOwrPBmcQuHCZvzQiT4eEuCv7ar4rj4ChLcQKYdtnsukmpZf%2FMsgUQVT5%2BorkGUPlYAJIdhGW90BiDw%2B8hqVJDdY2n034mpcHrnPt0mVfx%2Bd2Z6ApRYNNItr%2BX1QRG0nFOVNrLeCTLVu1bBy%2FcLqEhEIDHWMqaEwB61h4zZosApCJatPOwuMj9u1Yda1bC8qBkOD3Wc3Zt9USZHaEOXJE7MuHKQaWCLdPMLLzgb0GOqUBmDnsJlmjHr0Ol7aTXbwKl5G%2F2WmZ2F%2F7G%2FWvWlFJIUUYwicdFi0v%2F6mWhZJ8CjbsG6%2FjFr3Arb6%2Bpxgo2u3iowjavEq9OCFXEJFZOpsaBUQJ4NVvOeWLwe3TgYtP40su9FDGNlc3dGvL0KmQx8gH7be34oFuTI3RvONyDwLu04dShk3%2FvC6XZN%2FQkJS3a5wmUm9oKriznWP7MVVAwAoB2YOPUxPS&X-Amz-Signature=dea6d125c1dcdbf5c3e9d27467f24ea2d44e8f3d40f90c204ff12dd523797a9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAXHPADH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkYSmfG%2BYAnz6P0bdmNR1FadKYpSertUu%2BeLwFu9RBbAIhAOndFQu0YtmYANvT7Wo%2BoDfAlPQUIN%2Bz6SEpef3Chj2DKv8DCBEQABoMNjM3NDIzMTgzODA1IgwT%2Fl50WH88NC%2Fb2ooq3AMsU%2B%2BvfzjVnEqcV2%2FzRvfkPASUeEwiMnLEWP9ufsJfqGHS35l1KqeL2EHW7I2HteMs8it6u%2Bc8%2BOHMDuI96ob6lyvAe1%2BjT8Vt5BSeugZlK9xrdiOG2r63zx74Tm0UBncYoB%2F10mQWWHlPGsAj2XOXXTRigvjZEs40tK0sDKyACo3CW1LUjFV9ZFl5W75POkvCW3QUvhEpZylWo3yYQBwmLcB8w8%2FhdQKdhC7RhtaN2QYvMa1TIQHFA2o7IHJaBoT3tHrzkj0Ohipo28UQHyFJokEk7NG4IwtQN5vKCbhNbB0nZfBYxDZOxkblG953uvBvLdVdLSlWpbC%2FjT%2BA%2F1axRYk9L%2BmTWk%2FsmDpr53QPhYO0Tnv2llIdKg22MvOd1%2FyFPPURI3XLR110R4po8CkFIJUcLgofTNOa79Aak9DD4F55AR8K6ZRA2n0K13FdivmlHzQjLVb8r20k7RSf3WbfFj%2FQ%2FQfLxpfZEIubl8FkuUzihe3MBy8a69rh0RQT61RjfnTlCl26XLkphm60SXV94J8qAtwyEqI7AhbS1N%2BgXNPR2sEkwlZHxTNkfm4TDFsUUtq0TL3gxN%2B5w%2Fv2HqG2NS1hZddUcxPxd9TmXzsOd70x86e8HbWfDaLesDDR84G9BjqkAYz3SqFUa68twtgTbIwr31p10NNyLkA8%2BIL7kkrpMaQIcMQBAt9uI0VQaI16AUaaq1LEx5SOlk%2FiF1nldkKXhoXMUSZ%2FYZo%2FtUlKY7zdxaWx5UEe%2BvqKMmRjtxrrrfMY%2FG8muBfopGNV%2B%2FtUIy9lNEg4xXajAPn35M87iOc9RYnqwSv9yPcLoBr%2FCchN4wD%2FwcQHgdjFbuMLwR%2BisQYj4aGRSbV0&X-Amz-Signature=baf77ee7ef138cfe4013168905c06cc51d302cd96b74b05d26b1b36eb8912c6f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WN24WHJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFqncDgEJDzaoZC%2FvikRGl84%2BCDYtheHJlsiDNdXGmIqAiAlERcrnPCFTXzAv3uQTAqEH5xHkx7CGuVjyWdqLZzSeir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMTYM14jBjpDGnhVzMKtwDikQBwpsumCMQep4%2BDMK1%2BlvE%2F8ZuZR1X4VA3x1DSoYfavkGvNsyVIBYYMntJo%2F0HpCksGznnpvkXfdsdV5qM0g0pSQeAAwZzOnGHrgFwcdHq%2F1JQPkZTW3ESjl8c5vBiM9452W0E%2FlTSxUr%2FPk%2Fhxeu1i9H%2FYspKGZPcm%2B6WVS%2F%2BKB1fjL4XWpQHYw7BnhjBM3DSV1UTggd9yPZBk54De%2BDtGI9d91psB3f53JVsjX01P5PSJ4XytPNCZDU%2B0LtFEMMjZLbtp6wc23VNoX7JRocQrK6kNX%2F5AxwpJPekCour2xsgk1mRjSU2iqCfRUoRkBVNLC4lz46LUl%2BmPIoILxSBw1RnaA7sJcu4LKmspmsTemJY6733kG5oLZYkYzdtyWela5Hkyry0AeTZeb6HzB1U6PrUvLF0E%2BtBITv5HjYsmmQOjLrY%2FXge5mX9Igg30sAIsTI7Ut9ZXxy39jBQCzW7c5CfphidKqEq263HHp0p2hbD5Bt81%2BqsqA4njpzRpHW8a9NDChoQsada74AeZUCJVxf7hwtuuGi9Liaj6RIWUuD8HNIckGjPltGo%2BnfQbMInUYPgQ9H5z7Lc1sQet0q1eGzz5O7d9idHGDdP4uODe15rk4wVlrFvwiowtvOBvQY6pgFxyo%2B8UW%2FlksIn2TLUntGj00JAMEl5%2F2NUaXGG%2Fz1oCqIs3JLiAbkooFQqYiu0P5u3T4KdKm4ixVe6Rby1LgH63z30%2BfzOaRuDytmNbp6TXGs6f5WkrDNb4lX7h1oeTnAyM9LvjSsy7yoqu%2F8Wfym6VVF0WoTzaxpJrWUIxpXQzDGgduy3AqZasoCG5IeI%2Bp%2B4qIaxIbyFdcaTcGYAsB10HboFolbL&X-Amz-Signature=a49df2c3334eab20e7a146905ddf2a0d8c18ab6a65aac66baab1d5cf3df3ec3e&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2L5EAV4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE%2Fkar3HIdVZZT62LhjWHs2kYUv5eDahmkVxjKKWXTplAiEA0Tbe%2Bp794RiC9a4sD%2BQCBQFEqkz39psFMAL6WF%2B5B0sq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLHI16y5Sf5EKKzxrCrcA%2FOYbuWEa4EOJbhd0LkFOicqCHKv2Ajzinb3FSmGeVykB0dzah0KP37RrNmOsAFrOB3wAfITYk%2FbVo12XeZlpyNC4it%2BSE6ISbln6A5W%2Bil2BugZNjFZgipS0T1EZGK9VZvLDEuL8gttpzFEfLl4kJcMgGZ28oZWL77HTTqPRWW9qXy9v21H7oEX4BuAQj3%2B4NvnZFWJ0JmxVYYJVMPtRBAPVFBCtvP1JgQLN9JHxGRxwTv24CxHgD6AIGOz7rpVTif8NTPqzwU54y12llHm5Qwg35%2Bkg83C5SGxvtkTDd%2Fk%2BI5WxjzRR%2BuDNcmtGhnbinTrHmOFAD%2Fp%2FnEnb%2BXrhOsRQxWb2YHEiRCuX1qkBlXfTxSqadBId7uABTaS0iPFr0lVbyDfpUvBEQozKhKeD5F0yVgHLKHXxZKKicoj5q1mgChv4v6Mes5NnPPqfQxsDvVrPwp30YKYXgVf%2BGaWjL3qW0IPkf8C2PGT9UwOM74pfoqdHV1Qf6f4t2nnq1NBEMtxndrNOM8djMpFQUuXRk7SlEvcoS5dsmUFIYfyVNJUv%2BPq1jI%2Fb9QkBiXyBcZz93Pp3lGwFJYp5PUu5RJ8EVJlp7Dw%2FvbB40xjIEgJkPzuLKuFLPa%2BJNmw8KjFMLTzgb0GOqUBjnBaOZQ64AuwHxBu7DzBTGF2I97xUkg4gkqVmMdBQdcahlIpuqIPplogylbZIRNFCFrBzcWyAVEh63h6EGWZ7CADB0TAa8FNPzwy7nBjLTjMnCOpIY4WromnT5UcL83kpaQUwEsmRG8KVYX7hLb2sG923F08bmmF%2Fm4zRm%2Fl9G2s%2BLtc1fCYp6m4L9Ds3WbU77PiWDb9msiDeQxs85gC5bKaeN7b&X-Amz-Signature=f61bbafd7c10d01f08aa7e108909f79097bd102a6ff5c66a1600d90cb17e9518&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMVSNGR6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoQJeXMNCHLKL7GBxNGJjjnbntSNtoPlQJ5%2BGfCf0MRwIhAJjUmID1%2BApZUwUmRbZsDPNLipet%2FcW%2Bxpi208H1WI7oKv8DCBEQABoMNjM3NDIzMTgzODA1IgwNLuTWPqp3BAc6wAcq3AN7CqME6owVyj8AOnhlZEJtSnmeQu5HuJQ5FXdd0C7G36XIBWg1b9LTVvfaNc22Y38JYBCRqLBi9S5f2W%2FVdXbmYvoGyERDtlB0FyWQ2nMM9mzhJSb0kmlu7X66ZTv0eSiYyELY75e5mne0FqX97fz0G3Co5Z2JL664G0D2dFHUF3LuUAcgydbazUuTGN4YcLrMoECcZXW64gnI3LbhACq%2BzXarCi6rgs8rFh9kDcYyOHmQtAFFFXA2RSLDd6rvZDv%2BzfK5Ji8LNh8lkatsFLWatMgJg5iW7xQVDXFDZiu56c1YnvEkIRm%2BLFdYoD3JRwru7wiNddDUaaWMSFglC%2FaK4mRe8RdkMKE4mbpw2XMqM7JhtIjB2HCiWb5v%2FtNHF8QTtb4jsMHFwsKqqJqSqpQDmHQe4ha%2B0lSeNgFXNJbw7RLpxj%2BAJ9c8iHXqciA0woPgWJ7AF2SheuLEBkUIgflNAJ9A%2FTd209nzpDz6uJroLD%2F8E5ZRkeCpbpaR57kShFkseNq4rw7Mm1sO%2BJkZUT97Enpl9KNrcUJdm1BErmlbTm%2BRdKri%2FAfULqVt%2FFgTHXz3BD%2BdaQBAXbmx3gOBJrBHeBis%2Fl%2BMKdVohi0D5AsDkyDqtWqw9DqpXUWE6DDm8oG9BjqkAWrBgO0tq79RfzIEPSEx2WOWz9fIKP6KYZGuuYxN%2BdbYfmKpRiDxbgLKNlP%2BjMG%2FLJcvUoLOY%2FzEH810rikQP3hAABshGDmRNF%2BkAXosTfQbpWTQJCsNh8n6gmk70LcORALjMNYYcokHWr7P1wzklSPzm9cfEq0JhDDowJB%2BLu0oEuqsmz9JwckEHAUmkOLFqRTQVY%2BpL0JS840bHQ1b%2FYJMfuFj&X-Amz-Signature=98c5c682d62f038e4fa4162a42c49d87395dce66190784293b0eec298538521c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAXHPADH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkYSmfG%2BYAnz6P0bdmNR1FadKYpSertUu%2BeLwFu9RBbAIhAOndFQu0YtmYANvT7Wo%2BoDfAlPQUIN%2Bz6SEpef3Chj2DKv8DCBEQABoMNjM3NDIzMTgzODA1IgwT%2Fl50WH88NC%2Fb2ooq3AMsU%2B%2BvfzjVnEqcV2%2FzRvfkPASUeEwiMnLEWP9ufsJfqGHS35l1KqeL2EHW7I2HteMs8it6u%2Bc8%2BOHMDuI96ob6lyvAe1%2BjT8Vt5BSeugZlK9xrdiOG2r63zx74Tm0UBncYoB%2F10mQWWHlPGsAj2XOXXTRigvjZEs40tK0sDKyACo3CW1LUjFV9ZFl5W75POkvCW3QUvhEpZylWo3yYQBwmLcB8w8%2FhdQKdhC7RhtaN2QYvMa1TIQHFA2o7IHJaBoT3tHrzkj0Ohipo28UQHyFJokEk7NG4IwtQN5vKCbhNbB0nZfBYxDZOxkblG953uvBvLdVdLSlWpbC%2FjT%2BA%2F1axRYk9L%2BmTWk%2FsmDpr53QPhYO0Tnv2llIdKg22MvOd1%2FyFPPURI3XLR110R4po8CkFIJUcLgofTNOa79Aak9DD4F55AR8K6ZRA2n0K13FdivmlHzQjLVb8r20k7RSf3WbfFj%2FQ%2FQfLxpfZEIubl8FkuUzihe3MBy8a69rh0RQT61RjfnTlCl26XLkphm60SXV94J8qAtwyEqI7AhbS1N%2BgXNPR2sEkwlZHxTNkfm4TDFsUUtq0TL3gxN%2B5w%2Fv2HqG2NS1hZddUcxPxd9TmXzsOd70x86e8HbWfDaLesDDR84G9BjqkAYz3SqFUa68twtgTbIwr31p10NNyLkA8%2BIL7kkrpMaQIcMQBAt9uI0VQaI16AUaaq1LEx5SOlk%2FiF1nldkKXhoXMUSZ%2FYZo%2FtUlKY7zdxaWx5UEe%2BvqKMmRjtxrrrfMY%2FG8muBfopGNV%2B%2FtUIy9lNEg4xXajAPn35M87iOc9RYnqwSv9yPcLoBr%2FCchN4wD%2FwcQHgdjFbuMLwR%2BisQYj4aGRSbV0&X-Amz-Signature=d7c24589497ef9286124fa48921b3776eeb28dcc5cb1f63d41526a38e1a6d268&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZECNIH4V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHbr0WCTxl3D%2Biy%2BWpEPeJBu0Vev%2FevvTSFWyq6%2Blo2qAiAJZSJI2jWYzgptvU9LbH0bH6kHp%2BB64%2BP3KhDpLTMjbSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMq6u8wSbEPxKccip8KtwDh4vjn3MlKArJKysNDvol6uG%2BfI6mDuvGpba41BY%2FnPhrc9i3hGgN%2FGqbJj11MC0xA%2F%2FDP7IyEF%2FG5i1G%2Ftke1PObI5U0nmi1svHYWkegyqCTL48vN4C4Uyt%2B%2BgSIvxTIZbf6qglfXh8n0%2B8dBaPWte2%2BdDHN3hixtNSMJHKT0AMqSE80B3G2Z37WsgU2FO9x%2BUvabpNFrHx29xBasNctfXDblN2EqopbVqe5PdgqYiC9878YiH0ARN6A3L61bVYhFxq%2FwXksBRDZDRHJhf1BZR%2BmwWk3vJNnvVwB6lkUwFCcxMyCSn2NxxZTdZfVq8RXrQahC%2BwRiCRu7VpgpV7Lr427omvJ%2BX6wB%2Fqk4UGCQ%2BtjB%2FK9Y26OvB2ltI6CGu6H7krghTOsxlasYks4m1%2BF4fhOVJcuTIAvtveIXqmDOYralSi72xSdQLCCguFTMFd%2BZgfveflsMj1or3crcJHLp5UHc%2Fr5L7zFgKFUE7cT%2Ffz2aXus%2Bl%2F4ZewPZ7HFuvL%2BEtpmYxzf0znuE8GZjvsPx2xUpz1%2FldN5m0HnTyHzhoCvM0fO8MeZTVtl6P9XIglukqy3L2ZNbT%2B3kjAHN0wT%2FMof1%2B6HUGtynE9WDSzIn4ZQr4R1r0aT8tPB9acw5%2FKBvQY6pgEE8GKJz2IEqh2wcoNU1kkUe8AxPSLGETY3gCQhnxJvpNVVH7PhcI790EYMUfyPJ%2FCtgybYTCQX%2BzUoyKKv8oggvktqitdAOZyUPKWamvh49g8Uda8SXlLcyoHxZOK121Zn3MIE9mzZJXTOOjQI%2Bk%2FFQP1hog0mYwoZQ%2BxDoe7LrT0Kb9s2bAE0PgZkcDjl%2BDj2i94x1WlhuHN%2BgIAJR76BGsM0D6R4&X-Amz-Signature=547dafc02c28e3ec10f945fcff4602b0662dbd37422047ffc5d7be1fcb003df4&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZECNIH4V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHbr0WCTxl3D%2Biy%2BWpEPeJBu0Vev%2FevvTSFWyq6%2Blo2qAiAJZSJI2jWYzgptvU9LbH0bH6kHp%2BB64%2BP3KhDpLTMjbSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMq6u8wSbEPxKccip8KtwDh4vjn3MlKArJKysNDvol6uG%2BfI6mDuvGpba41BY%2FnPhrc9i3hGgN%2FGqbJj11MC0xA%2F%2FDP7IyEF%2FG5i1G%2Ftke1PObI5U0nmi1svHYWkegyqCTL48vN4C4Uyt%2B%2BgSIvxTIZbf6qglfXh8n0%2B8dBaPWte2%2BdDHN3hixtNSMJHKT0AMqSE80B3G2Z37WsgU2FO9x%2BUvabpNFrHx29xBasNctfXDblN2EqopbVqe5PdgqYiC9878YiH0ARN6A3L61bVYhFxq%2FwXksBRDZDRHJhf1BZR%2BmwWk3vJNnvVwB6lkUwFCcxMyCSn2NxxZTdZfVq8RXrQahC%2BwRiCRu7VpgpV7Lr427omvJ%2BX6wB%2Fqk4UGCQ%2BtjB%2FK9Y26OvB2ltI6CGu6H7krghTOsxlasYks4m1%2BF4fhOVJcuTIAvtveIXqmDOYralSi72xSdQLCCguFTMFd%2BZgfveflsMj1or3crcJHLp5UHc%2Fr5L7zFgKFUE7cT%2Ffz2aXus%2Bl%2F4ZewPZ7HFuvL%2BEtpmYxzf0znuE8GZjvsPx2xUpz1%2FldN5m0HnTyHzhoCvM0fO8MeZTVtl6P9XIglukqy3L2ZNbT%2B3kjAHN0wT%2FMof1%2B6HUGtynE9WDSzIn4ZQr4R1r0aT8tPB9acw5%2FKBvQY6pgEE8GKJz2IEqh2wcoNU1kkUe8AxPSLGETY3gCQhnxJvpNVVH7PhcI790EYMUfyPJ%2FCtgybYTCQX%2BzUoyKKv8oggvktqitdAOZyUPKWamvh49g8Uda8SXlLcyoHxZOK121Zn3MIE9mzZJXTOOjQI%2Bk%2FFQP1hog0mYwoZQ%2BxDoe7LrT0Kb9s2bAE0PgZkcDjl%2BDj2i94x1WlhuHN%2BgIAJR76BGsM0D6R4&X-Amz-Signature=08d663c08a4fd7827e88edacf5984f906e337f5eb4d47f97c03b95685ddf3200&X-Amz-SignedHeaders=host&x-id=GetObject)
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