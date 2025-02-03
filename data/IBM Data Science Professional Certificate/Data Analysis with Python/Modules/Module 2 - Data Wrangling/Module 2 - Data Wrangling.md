

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FVJCU3I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHlxfB2lhR6yTT2v%2BOjf7Cq1%2BoJL%2FzeqlJ0qkqfS0n5mAiEAgoyuAMrHUTtjnGy1Q4hOeByUTHCZURqt4xvBKOjZpmQq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDNz1NGoZ2TmhSPy6%2ByrcAyl9eDq25t%2B5WYIvt8Dx9oYvcg1Ga9FTJVqgMt0BpVB52us5p1spDHN5QKNbeFZMQRpyfNjDSGUPlLTt4TCXSuFy%2F57LFPFiUq%2FRnoEyQP8rON7WvNfRYTPEl3zLyO0%2FC597UIPQ6rz5C%2BD48E5z93xVB1aX2wWESesjVJH6IRfHXBNQb2PvXJ3%2FmovTiIQdGbpxX3W0tB1pvAFGMUM%2FMxebIXXSOCQkERrJ5aMadl%2FYsqeuLjydV5wJ1o7FDIxo87W8diOTITeojEa5Lk%2Fm%2FpbIHBsN4XqURLsW4tBxMSheu2nvx02jGtm6a7WbiAZuxIlTyYjDcNCIKDiMw5EHUciRfe%2B3VQF4viuTix9Ri%2B5Q7oOIwmzq0iQARNMrNpH6dJSB5m0FH3fub%2B5wBwC2eMFC432h2c5B5BTX2wvf7Sx69ZbMzYA5AaER2Tt90CxDEPcvJ%2B4D7L5R2xPgeNTDGCYWjRcxYxyWZUEaRW4b3BUf6Z1DkROolRFCUYMq0WuDFTcT41JKx6b7n3jd%2BRs4hKnw3tJDNV2zM9fJgam8zXQaOrdrQkNHf8djvhwsQeGAePA6T0%2Bnd6acSdTbsuFmZw2jOPwEAk5n3dbwAyfyJsBqhIDP4cJb8HmHRiDDMLPWgb0GOqUBMDHH9LZDnqSOl77plNbThw%2F4%2BxAXvCVVqKS9F%2FfeJ%2F3%2BICotra02VqWVdGJ5tGe%2BKOGtWaJMKazMdW30YKpsy071JdfmhqF3BJHPczwVlr77eyHwBZ8dfBYSrxgXA5edLeWD3SHSf1vSRNUuWX8W5tMLBHduP0lVBtICIeXDZXGaxPQtPDVBeUuQB7gg0gMHBObEKkx6RTldQzGp88e5ir1qSsCK&X-Amz-Signature=191c08416b513be0e964bd68e16f278eb2ba67e2e014ed685f99d259d5c4cde8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5FXTVZP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN8RjTdyy0AdSIK2WTfB0ystnw91tCDVhUnppHhDAijgIgU3LMlxeB0205aaA00%2B%2Fg0IkL621%2Fa%2BB%2BGn%2BmrKi7QC0q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDI3%2B6Jf5fkhFh3xHzSrcA%2B7JboiGBHMyp%2BQ5GTiZDd2xXxxwSRrxajofKf0ZwA5u06hJA8Z4hYteoB3MgrYvTgl5RHaz79NqKwE2WJ9K2CIlkaX8pBSFGzSjeZR2xsIQ%2Fgrryh9Om9uy26kaYsn6n7RLxKWL9wX0UePYnsYv7frESRmkf1Hx5dG2e%2FyIcOUolIcOHDTGYwJnPgz7c3c1L0cTCIB%2BWklDmi6HVJko%2Bgg0VLm7qoLpEC%2FiSX3ed%2BtObYPg7%2BY5JRulCV6sQBpLwxS4rmfvJ9zIGZLVI4z7u%2F5OWPokLTAlZddKJZxjBGDXXJ0Ol9HxwJYdmHHjI7SBz68W1tvdF0ETAaIRvIA7ArMnvxjSjt%2F87DdKp5oFi2sYLSeg8KGes9NCc6oREaIrjLiRWh9whOqT12zHzhjcEXa%2FKT5P566sWO1HOgelGibRPP3DjaCybIph8Ha%2FwcEd2Y4qwMk1lQ9xwW9%2FqcFXMq1pIcTmUEt%2FYkDM5AW1yp7CcxHQLAlTbuY8PGANfudLlb6cCDyi9uNxcyfkZOwpa2Tv1%2F3tcgSi08dEwgfKIQJF3Qti6XG64cvyy0OWXO5trH0WUtsJjeEQLIi3pQE%2B0qm3g5pYzmRbYBuW9eeDEOFhEtpUjXz4i3X9aInFMKzWgb0GOqUBUhZHyyTe98bwJ3dDWSLcwNwj9jRh8iKXvrQObXl6AzHDaINlZ0Scw2%2BUXvxcskor%2B%2Bm%2Fp%2B51MMIe0tFA%2Fe34RCOMSp83XWMQTC9rxVxkp5kLak5G4RodhoF22hEvo0RIuzhIrBCs0ESPqZahfB8EaJP7spoUDnXIEsaVPGjK%2FKUmWZzkoU5iWXspBVqBhcmhPcHkj7a6iXvq2Em5O6Tyt0p4nxyE&X-Amz-Signature=31c2b798b097d96a4d9230e13d68499d11fb4caf4cd09050cd18cafe93237402&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TN5B5OF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZPt92NfyuCFJ8poQIozEgogGa1obimImXL0IsjI41cAiBImtSV1kNcC2NPJvWiTUxmjkrMwpykemJA3gGgcV1XYir%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMSmtWpUJ1wklkZPeKKtwD6WHzAhDHfd%2Bsn7%2FKgSF%2FThpe8%2BowKVsntKQwJWvU0W8A3jpBPzsUgelmvTyYdBxPS67uZhxzyYxjp50ex5cytFfrWmqtsZd%2FZwvCSJK%2FuXdD4wb4W2zYcj1wPYfDUGj4QXgDykZG7JsTQirPOllNnklS%2FxeEgIUmFYWh9aH8ZwFvYpMAZcAFOaYydcY99p7GbA13cuFNkf0e1MVb1GYcuk6t0MgN0qs%2FqHunpQ3s%2B5CnvbJL7kBxw%2FKk%2BK5Ft8fbrz4RK7aYo8ieh%2Bde6JqoKj5ww%2F9oYISdAX30OxTL1uePQOWBVKGIFhY3RPdSkLWLTlgSLWoa9QtkN7STCW0Uq9Ob40RsDXv0S2bloHdCB5L3RgUOdVqB0KLIfIxQrosI2t7uIfvEe6iFGNzfp1LrSQjIIxER1ampX%2FstPK9VphwFcW3FTEiqmG8ISCrhTqgAKDLRe95yqd0cJ4NROOLtxWsG6QwGAUqGKnVzH460CuCl9%2BIuBw3r%2FIOHZSAnhdpwPYB0wayBP2XXguXyM5MutSCwDdrXtZUXmLecAcM0Y%2BBWr2RWlaUVsgmaG1X%2FxlJ4v2f0kBYYCJ6BCF8hsFpOKOHmHmVpB55fyVzJ0J18b%2B2rxP%2Fibst%2BClkY2gsw%2FdWBvQY6pgFC6HN1dMR8U%2FlLYcV3el0jnHoHmERJ4GckgBtTx9QE%2BD11P6uHNixJjSV3krF8rbw9OenuP6YIWGw5T8jNfksxvdAyH3d58PSIuwZQnWWY2K0akQLuQOHGCemFV%2FaVlzXpSn2jKMRFbFFUeLCZ4DoXb3daZwFaVwCrsVkvE5uGSHe6xJ6poplbE4Wl3Cg9wGF5ZQQ7TEq0MamVIyOVHc2sG9Gbqjf9&X-Amz-Signature=e6ef6ba63c0e72d82fe65c91191d37e234c9f72fd7fcd3a3f7e13d0107bbae07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DWQBRCW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7z3%2BJrTc69H%2Bs9a%2F6vhl9eifeFV13trlRR%2BLOB9AZnAiEAox5LmWiVfo58Al2vD7EzkkxKj8JAwjrVBt9YXBKsLxYq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDORB89rV23ocJiqeZyrcA1MTmyqCcjaczXfBzEu%2FwfJ4c9YxrK93mdmylyj8suFeR6qGXXQ226StBDPrgVoTBIP7TvEwIUIzxUVD56cAip5dSonnh8dZXcM0EAtdIX8sEvcnliHC559Qd%2FzC3H5JzqdwJuKeO%2BHTmI09OM9UuZ8vGoPgVzf4QRLsaLzT%2BICJetlSJ4ayT6ULgC3F2OK5Ne63aIhxLlErxFUKSeNjBJp9iaTujF5ixyDOboch%2BflpxMryG0ohj6%2FZ8y7lSDtf20cU0CBm%2FNENd%2FO0mz1zmTOPeuWihqFO%2Fuz3SgOBBrJM6l2v1fXDnVb4S1IOn5j0oQCmaMdxmiuNGndNvvl72K24MJtHOk14W6munjZdWqfIcC1kBUEfHQugCZV6nurdEAYrWdNX6KrMPX5wmqTbNCFFmGxW4f9mIdzoLeLAy%2Bssu0BXleFjNTw5Rc0h%2FHFhsXG%2FtZ994IdoZ%2BzV9gHX2ED8V6%2BQ01QJ8s8J89%2Bol5J1sKvL7o3tWT2GmnIJC05dG796pK2CtCwqUkG%2FUsHEGOeWwITgLQOuOMpp87sQOhK9BQpAjmBrffBvh6qKzUH6SVXPThSA5ltjSMlaccLAy3Yja5rWNldQ1WRU3Osw30XowNkceUmw2RFROQJUMPrVgb0GOqUB5XiYmjzzkCfxXZu3iaTnekKWVHFs1DIU8h9rQoZU5igZc2Ozqwk78einnuKDAv%2FrN9weLomhoP6A7F5fO9xH01K2SbW5tl1%2F8WvlofrMskMovn0vEhH69%2F52SbpPANG0YWta5r8J6DnArNxLhgDCZ3xq2T8eEZ6mc35BQ9UrSHS42z7gNj6p0QWktACesvg%2BezH0TGvh8%2B0e3ek3b04GzFbipp%2Fz&X-Amz-Signature=90cae8943255d97486aec9f623becf4b94f76003062febff18f86088d3ed1767&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YD4GM4K%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDL1zZfYW92p2J6NpNAgYBi%2FNI%2BG4VdMfDG44b9wvNuWAIgCPeGhoVgXBguDfZ0Z9kU%2B8l7Z7vD9QMGQQjCZDyeoTYq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJiNbnwlAXcKvfe8qyrcA854g3eGTrIYbMZ%2FBHU%2B9%2FmoXPRNbFT24FxhyoddFHhLiecR3aweWQ%2FHvdVui4BETG2e7BJan1%2Bu6GIJXyq0kWNJT5VrEoohKYnX4HvHbyyELGWT%2B%2FOVNMDMMWjtmSxbdvFm9yB8ce11T0A22welVx8I6hHNJ0w4Xp49bUmASh3LI%2FCcIVtu6j5e323SMLJOKPA7Nej0fyIwHgf81WcEC4Edc5qgENWfPwvhJ01ZNhQab7QVVDh5DhFsKDW3QbnEw8%2Be7IS506X4rG2QyxA%2FUs1zj0B28nG7lt4RJGyiAMEpw2JxdmHcjGhdf4iWqsmloWRw3q0Hv8HcnxcpoMJAUnz9ZRa8T8HL2VS57yugiucd%2Bsg3HTgcsJcKfqhVY1rvrNC%2BFjJXOD9vtiy1Xj3X98GrzQQsEwWOhAgpFzPd5rCvtF17KXUuLqiAeBX%2BZlxz9%2FOU7pkKUWesZRcss8F7%2FJlcxi4Vk4TpL%2BmB%2F6pftHL49OZiNF8D0qb0J3gvWE8GZO7tObKaaQRdLwzK8BROkcXN7pCjxqk0Sc99YiLWQtENZGJRnQKK2cpBRvQwB1fuIR2Ar5t8v%2FL8oPXGaX0yke8ZFIlY75Z6HoJMFQr548cOyfOHo%2FcRcP6HO5DVMJ7Wgb0GOqUBAPGfRcOOzQUfTnnC0zGE8wE89cAi0pT95l85aye0Ay%2Fbgd65Xl%2FkX0RUavj7hruJgy2KC%2BICjNmDk7%2FHXXXHollYn7QOez32nY1FJBxXdHTE0z1Q8DMSkvVfaJSKbCp7gx%2B7JFXAMdQJR96pv6Z70UVoHVz1aXTPpCHS1eof4qzehpittJDSRb1Q39mwxNE%2BPirZ5tZfkEwTtKGnFmYNH0jmrMIu&X-Amz-Signature=ec5b2fdf526b00cb12430c27c7e81955979c2d87c0a3869ba319a408ce6fd64c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQED7JKC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICyJA0KT8RnCvjrwnQ757EqhNvE2R8uKHy7y5t1HTwrUAiADwFzzjYyzsqqGZRJnWYgKxEaKArvAkU4DfQcmtGvo5Sr%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMtEKaMn7eaER2K%2BufKtwDyRInFYUAS6SxKHCUrruKLj5oG7wJWpW9osIkSX%2BKFVAFiziPT7FeBNGUv9Ms4d2N%2FpRHzqmm8im8edo8wRyZte%2BnYy6wCdvgre6bM48h%2B%2BN1M4ZzgcS6nCpnIhOP%2FF2EL4kY8%2B%2BUFJcqnvJUTaGSHZi5uxJvsYeWDnK08PTJyBLa%2BcZhbEpWTixLawX6IT4DzxDhit8uZC45S6POf%2B0sK5vpofmyLgQ9F%2FK4dlUuXb6K2NRcYPzGZolWqz9ewQjw5RjYIYIVHprf3tlf1nuz0tnajRSVRZGSPaR4q4xIs1ocLaPJoDlIHErxaMTk8I%2FaAxefY%2FkACvc2ucp0yDzIYQMNPd331J0rKDxsLxwWDPz1M8cDzoWhEMzCtX9pwwoMr%2BQgfxLoXQ2D4jN2EepUbl1r1iogfwNgfj8FmIwdCP6YYsLX%2FBkGSZhfIV7qBUKckcdzoNNZ7eBumX72jpxDKP%2FWsh0JDzWj%2BTbwbQIxdY6%2FMqaIgJmAlE3FkJedJFArEXpyD1YpKhbipU3I3501yv7Rzxpe6gI1F6OlAtoLLDzxYRFz402x4PzneYDrrYvshcm5fYH3Hpa8j7qWID%2BAfvpnGVSHcZv%2FtNMCnTw8mO%2FNR8ovj6SNxRKRIUYwrteBvQY6pgEcyps2Umzka1%2FML4vlOX2rfuICqko6tjxIRWG0bPUv8tFLLFaXJq0cGYjoi59iIKNnQZnajZXt214txu0T91VUC0lJakhAKeanxdeVUdPldB02cfyzu%2Fp%2FvAtH18NKfHimlwa3bdw%2BnCjsKn6x1G400fBlxgrhLYUZp5aI%2B9E0%2B31J6fXEaAY4APgtHPOR6Yu1R1oLVW%2F3aHgv4ndjav27%2BT80DZ%2Bb&X-Amz-Signature=f6702c698bf6f1e18fc35f41269be07a14797b736825b003a5cdc792f82142b6&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCAYOANY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvw4erJJ4jwGSSNtnKtDaglPgKIVsZ%2FnTZ5%2BNlFtp4RwIgFy%2FE3a%2BFYrfT1vPHP53s5%2F%2BHdLmDTtRYOWykBLDd0vUq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDG%2Bjj4RlbuY%2BrgI%2F2ircA8Gp%2F7nfcCeeP9zWNElvnEFMzWXE45wKqoQM4BJ0QzrFmr59p4GSDdGCarCLmMZJHN04FrWkATipzzpUD9iv24%2BV97TsifcA2pzDE%2Ft69EXmHd6HCCOTvzNCzoeUpxE%2FM1puIgHUWorlxOSsbx78iz2NxwdA7yk0hIrV5djrd0gLWKj0xHdjmgeBc2lV7yuj59wQpcnZxNbvOCHIISBqhVkqnfWCTwju4iOQF5Z4U2VfTYimiW%2Fgu8Ifj49WYZhDbRxBRdy2x%2B7rr0uZ1nzmII%2Fbq0oIqYPg3gcZqeP5WSks7Gf8SBGRCnZxboG3MtYWaL4hRln47Emc%2FCqnMcFIrPEdOq8gODhX7DrIWmxrOoXenv4NT304jlM0%2B%2Fm6ucCzwYL8NIlm2bl%2FYr6VmbX2%2B6%2FHvJj76VSe78B6cmLHSjCaLw9ea69T10dpzPLgfe1zFXsTkrP2f8WrsGrks4se9B6fnpJithM2OxEhVEhAavz8UECqw5Gh%2FcTDdJYIj90TuKWOi1%2Fsb2%2BgywtJd41QScxHSZdEA%2FGYfUcEYZnGF6WOlBJGzBDPfPYgK%2BDPrg3zoBjxekxk5an0%2FXhPQjlla606d3shMHkUeqkXiPzQ%2F8I2h%2BU0%2FxF3DpI5nJRGMKXWgb0GOqUBZF%2F9b20cwVKwOWPd%2BcnQ2VeG03Q2IVtP%2B7NMD1OHdog2AW1L%2FfvVOsJrPGCQ9vk06DC0mPDKze48Y9WhvgfMP%2FMFeynVyfwvcZYZLg1Kbg%2BppoHkQajzKC5GCZ6hIAjU%2BMhEkj%2BAaUkgkHiJ8Es3isrdTy1f5g1W7OLVNTNgVYNxEx0v82SI%2FJA82lcffHLt7lc%2BoWM4BMB8EnF0iBbgqSAQESGW&X-Amz-Signature=47b2b1389f6be9d8e53cd7f09e1b6a3f7430d4c62c76e25e0d907b9bf50df396&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBMUP7YM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsJ6FwTgtTcxGitHuKtZbAsjTLZ%2FAXeczZqueNP4OfkAiEAlXfxY2o%2BvNr0ftAc5ps%2BDmSJ3a56o4Uzz9MN05R8Wa4q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDGFbgQrB2wK2FeVevircA%2Fj7Kakt19MIoJBXWbqMjAHO%2BfHug1aBPVDLdKFf4sLkX6e8UG8phy2XWW%2Feoo%2FkeIHAoUEhpRP3aMNKRdq3KWjqJ0ZzfmBQ9CZI69F1dG87TjIuVaTrM%2Bva%2Fd6wIcKOOIC%2FqJYXkPAFcEpgIz1JHp8CoVwGqQKKThXG924CWLpjOVyssi%2B1aX%2BkaIDFxQys5y5Mpry6N1TANZEgmk6eFJjs%2FpDnG5L%2BfJZ34ntONpjdgAwG1unX3q2%2FX7csRj2vJwEB%2BVgHhT7g1fhjm%2Bd1HPRkdyuf6JhKCoegJ3YQye32q0y45s4Q7GBKPHG%2Fv7%2B8zuzBCXgfR6a1pCX5Rx5g5ca7fJ00nHy4z8qI9zFZc%2FzoDmb2p2yEcJKF1PyxCThFLtSieZIQfPhAV1sYbugKdUZ3fw0OmpNXz2a01Qzs5PcUKwhSDfXPtkZDb0WwhZ1PdPnqFLU3mSuNw3k8lMLKcWMBd5fe7r4Ga%2BHXJ0TzLdhTObptt71no65r3jHMY1KiWMUqJ4bEySVdcACYgp4IsLsVUZSRaaVt0OJtun07BZdwEPUGxXt63m8Y5Z0uTDDT2OnNvl4qGX%2F2Ua0JhJHUYF%2BS5lnvRZgWrlRguETjjfisGEj9EBFNEFdB9UJ2MPrVgb0GOqUBVCpsMneXOpcYM6OWyMtDRrwMEmgK0MqjHaKdYGU3KyjfZt8%2BweMoeRtlikVEH4PpMgycLtZXmPCVNV%2BNnPbLMd2MQYCWZ%2BqZZ2Y2xkMW0OuGt8piTGg9W%2FzMjCi27r1UV2JPr%2F4Q%2F8%2FwYcJaGw7nejZLlx%2FhwqcS2Wa%2BUBjECxZmoz5N50lZ6w79E98QrZlZk8ViFPH%2BAyMDeeA3RezNtGM7czNn&X-Amz-Signature=89578003fa3bf75c6861e0d3c764c6325377d2ecb5e59845c717adf3706cf637&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YD4GM4K%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDL1zZfYW92p2J6NpNAgYBi%2FNI%2BG4VdMfDG44b9wvNuWAIgCPeGhoVgXBguDfZ0Z9kU%2B8l7Z7vD9QMGQQjCZDyeoTYq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJiNbnwlAXcKvfe8qyrcA854g3eGTrIYbMZ%2FBHU%2B9%2FmoXPRNbFT24FxhyoddFHhLiecR3aweWQ%2FHvdVui4BETG2e7BJan1%2Bu6GIJXyq0kWNJT5VrEoohKYnX4HvHbyyELGWT%2B%2FOVNMDMMWjtmSxbdvFm9yB8ce11T0A22welVx8I6hHNJ0w4Xp49bUmASh3LI%2FCcIVtu6j5e323SMLJOKPA7Nej0fyIwHgf81WcEC4Edc5qgENWfPwvhJ01ZNhQab7QVVDh5DhFsKDW3QbnEw8%2Be7IS506X4rG2QyxA%2FUs1zj0B28nG7lt4RJGyiAMEpw2JxdmHcjGhdf4iWqsmloWRw3q0Hv8HcnxcpoMJAUnz9ZRa8T8HL2VS57yugiucd%2Bsg3HTgcsJcKfqhVY1rvrNC%2BFjJXOD9vtiy1Xj3X98GrzQQsEwWOhAgpFzPd5rCvtF17KXUuLqiAeBX%2BZlxz9%2FOU7pkKUWesZRcss8F7%2FJlcxi4Vk4TpL%2BmB%2F6pftHL49OZiNF8D0qb0J3gvWE8GZO7tObKaaQRdLwzK8BROkcXN7pCjxqk0Sc99YiLWQtENZGJRnQKK2cpBRvQwB1fuIR2Ar5t8v%2FL8oPXGaX0yke8ZFIlY75Z6HoJMFQr548cOyfOHo%2FcRcP6HO5DVMJ7Wgb0GOqUBAPGfRcOOzQUfTnnC0zGE8wE89cAi0pT95l85aye0Ay%2Fbgd65Xl%2FkX0RUavj7hruJgy2KC%2BICjNmDk7%2FHXXXHollYn7QOez32nY1FJBxXdHTE0z1Q8DMSkvVfaJSKbCp7gx%2B7JFXAMdQJR96pv6Z70UVoHVz1aXTPpCHS1eof4qzehpittJDSRb1Q39mwxNE%2BPirZ5tZfkEwTtKGnFmYNH0jmrMIu&X-Amz-Signature=3d5951f938a3749e8192799b83eb71e0468f663225cfdcb99ec2afaa29ce679f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RE5K6JO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAdWypNyLhC8uVRMCiqeWKqJnq%2BOa%2B%2BJEijOMlINmELvAiEA%2Bl9umztGwetsqTHml2OSIoEMSLxYFHyjG9Hbeb9BQ54q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDNeXuHwfJqc%2FLBLHcSrcA0598gTph8iR7hFKLGhqDJYxxsRDL%2FvtBVSwPhgzPH6Ky3qS3qZaYa%2BlgdRYhQWW1qdq%2FuHRGR2j9o%2BUyOkEXZ8FrJi65LkntBaNnIJifRGyIySQ2iR6zOp1yc5KXBMKLgK0mcruldr8gIfQNEtA2TeFhzvrrbROeI06ppbSnIbigbKyFop1poTqvR2Z03%2B0P6QCIDaeQ14BWqy8wq%2F2kdxuLWOqpL3anDRS%2FzyVXsqeNQ%2FfTJPa6AGtGnTNGnvRJXmg9BIiUyNSeCNjy1Z21sPOv7Ej4YAm2t1OoZLXPRtA5jiNubun%2BRz8X%2Fn6UbZbyO%2B2NQM2vbcLi68ClIoYLrfbvivQDEnaL65CfYCkwQC1d270%2FZ3J%2BdT4huY9a6O%2F2%2FNkPNzmcvYv56Jk2hvuRNAQHsfsemm7cclZB77XGdTD%2BquNv36s8TCRKjbju%2Fp4mR0nXWGqq3wqsq7n0NDOJcJdZpt29EkJzTSbi8IhRbn7xf%2BP2WNzQP1KYkxHF7iNbHdTYzrBBNn6glDVZE6sALsqQ1ynSuRBVFqwDgf3P3QpwEXmBmnXR7b%2FRdBFfu8Xq2uUIwibh8az8yFkoJ%2BLma%2Bvuf2fwR%2BQNDJ%2F8QnuaNjYEexaUPjB4khmLzTvMJ%2FWgb0GOqUBHySVr28XaFQyno6BV3XLsy%2B79R3I%2BYiW4DKpPD4SPJ6fKBepdBuUkLwZ54Bfmhz2EslT8KPvfjWchEYOvdFCIqI92GOhS3jgVqywRwA8CSEIoBwZW%2FWM%2Bm0TyRqYEFl4jm9jYikZ%2Bi2z1VQm1f61jDiEQbMB3ymj0x6KwmxrNsF9dAauajfa389vnHp2o5onELVI36A3zwhEVEkD5oIXxO8Oe%2FzC&X-Amz-Signature=8c8b9974073f28a91b0c81511a29d06b45ccb6e3ca7ebb67c7096f81487effb2&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RE5K6JO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAdWypNyLhC8uVRMCiqeWKqJnq%2BOa%2B%2BJEijOMlINmELvAiEA%2Bl9umztGwetsqTHml2OSIoEMSLxYFHyjG9Hbeb9BQ54q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDNeXuHwfJqc%2FLBLHcSrcA0598gTph8iR7hFKLGhqDJYxxsRDL%2FvtBVSwPhgzPH6Ky3qS3qZaYa%2BlgdRYhQWW1qdq%2FuHRGR2j9o%2BUyOkEXZ8FrJi65LkntBaNnIJifRGyIySQ2iR6zOp1yc5KXBMKLgK0mcruldr8gIfQNEtA2TeFhzvrrbROeI06ppbSnIbigbKyFop1poTqvR2Z03%2B0P6QCIDaeQ14BWqy8wq%2F2kdxuLWOqpL3anDRS%2FzyVXsqeNQ%2FfTJPa6AGtGnTNGnvRJXmg9BIiUyNSeCNjy1Z21sPOv7Ej4YAm2t1OoZLXPRtA5jiNubun%2BRz8X%2Fn6UbZbyO%2B2NQM2vbcLi68ClIoYLrfbvivQDEnaL65CfYCkwQC1d270%2FZ3J%2BdT4huY9a6O%2F2%2FNkPNzmcvYv56Jk2hvuRNAQHsfsemm7cclZB77XGdTD%2BquNv36s8TCRKjbju%2Fp4mR0nXWGqq3wqsq7n0NDOJcJdZpt29EkJzTSbi8IhRbn7xf%2BP2WNzQP1KYkxHF7iNbHdTYzrBBNn6glDVZE6sALsqQ1ynSuRBVFqwDgf3P3QpwEXmBmnXR7b%2FRdBFfu8Xq2uUIwibh8az8yFkoJ%2BLma%2Bvuf2fwR%2BQNDJ%2F8QnuaNjYEexaUPjB4khmLzTvMJ%2FWgb0GOqUBHySVr28XaFQyno6BV3XLsy%2B79R3I%2BYiW4DKpPD4SPJ6fKBepdBuUkLwZ54Bfmhz2EslT8KPvfjWchEYOvdFCIqI92GOhS3jgVqywRwA8CSEIoBwZW%2FWM%2Bm0TyRqYEFl4jm9jYikZ%2Bi2z1VQm1f61jDiEQbMB3ymj0x6KwmxrNsF9dAauajfa389vnHp2o5onELVI36A3zwhEVEkD5oIXxO8Oe%2FzC&X-Amz-Signature=d4d8cd1b99592706b4816202db1100fac9d71e3d911ee076cf859d82ca3c0ca5&X-Amz-SignedHeaders=host&x-id=GetObject)
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