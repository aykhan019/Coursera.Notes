

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMXYAB63%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCHXZCk0XCy1DYs8fUsa3W8AO1ubpFNYCcoW%2FLiL8yCNwIhAJ5BKqE5agJJKxtU7eVMr89TvUBkbbgJYHF%2BzgvcO3RbKv8DCGkQABoMNjM3NDIzMTgzODA1IgwLdn2kjE0Zu%2FlLihwq3AOhkPBEBA%2Fa9DZfJ%2BkOS7NGiT6%2FOeEdg%2BR5uIzg%2FelOybNul01%2FBMv3Ins5VuEGhIPXX6T3nCU0IGwAnsvwAZ7r%2BVOcaHMt1rKfJcAhFT7V2bxpqR%2Ful2uTBiHbkS7j3B05mly5O30jZQD%2FsZIG%2FVJwfEYd75Yp6ciGGATRlGOzybwIh4E4EBW6Q50eKQgU4Rqqjgo%2FsoeV4ffAnbLuIo5w0hyf36x7PE%2BeC4NtElZmoXejSAfW0WNqfvkaM50Vh7483G59LBX2mEneCoIedhGWN%2FL%2FTiJrf7%2FVnhzWfCL10wgonLgWG37vvm1gWVr1sA9INb3QR4kgomVGMNo6f%2FD8qcne4rh6P0dOVUPyhQQ7mSrhYP5CF7nbK3RHnV206w8tto%2FiMXnAqLKeWF9Ggu%2BpCmcil6emJUUyvH1%2BtiuZVWTJAgXeF7DVt8lrO1LbUcWj0I%2F7bkdVDpU1Abc4iwsRD47j3W6t8%2B4rVNHJ8glQ9Px1et%2FnKCSCi2rnGbdwzvU107sCHVsbZZ0BbRW15xQECGiNgSqTtJWDbxydsMPcwvkXJrc2aeoyB9x%2BxlLY5roPdUVKZpxEw9LV8%2FFg8Yc8Kh%2BfTNe4PEMcA5LEb9v04AEtYx3FoSOuR7EWsjDumZW9BjqkAcSw0fclPaEhfwmRvDA4sloetnl9ZcnxQUFrBFs%2BlRUcL5H580XNC1xN1D8IP8ZPLtDLS7E305xIvT06kcU3sSWNMeBLA52dlgT1IwhwnPjzC0hHXqcDUMsZjRUS788asZz31SxWGQWyQk22UfwuhVR7pA1gnCvauhLrGLGIT26ytxB%2BfkFxakrvZz1JfBjUQ%2Ba5T6mcaMam4OXrLsdi%2FyfgkvcO&X-Amz-Signature=1f579fa36134317e2c167be6489caa55caf33e1a8893dedd1d9733d884aa62c6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LK37YI4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIBnHFXkXcMunDcZLDdOZs4Ci4OUh9f1jY2uGkzBsh2thAiBWSpMhNgmohqkCP%2Fd1ZuQZ5T8Qgs90oUdDrd6%2BDn23QCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIM2%2FubzzPOlOmIm2RMKtwDFXvsrS2DGdDu0h%2Flq20nB3cxFJW5Ww%2Fn7Bs8ZsCgDcNZQ9Oy%2FwG%2BROTBvKPDC4IGUfoMrVNWUcwFKK0Q%2BZ5VbcqQfYniCsq7YAmVex8z9cvVx%2FYuq2biYwWuPeB2l5LRFCcjW7k6beWBQA3ios0334mGjuPAbT76usuLNqXJtbh3qNnOCT1xtI2jGactuTFtkyFYrYTyapKyl2HohLiF7UnTAEvjiRy0vLJ6VSrWW1t3F2Iy%2BMfDEDh223GMNGDalTn1fEjKFGJZqbQKJOmL%2FkyeeDjnGgHtjTbLXHHuL0aL7uwqHYnEo9q%2FhfSGVKYKzhKZV7y90WBBfUctOILybgXOzuURoPbzBWQjYjI0m32qhCAFOC5H2UiQkUoAG81rjUHkQyevFhzB7rjSRgABn4u2J0oaEf1slCE857PsZXeJk8YxeucDlyz9FMzDTo%2BfEvZnbRuW5lIGRT96rjWg4C%2BqojcgmLi%2BR57c1G0sLO6oWWoHWT%2FMoAHoOGrPhNE036LyMWaXt%2Fqsnp8%2Fn3LjBzM9zcGN0usLljbpCaepOedlfuW7zcBnoLDrPWFALtxflFEPcCIh3NyyXEZrpkHd3DzArUOdcef0wh7Jk4mBJgCN2rElbHub4VB5tBow9pmVvQY6pgETlauqJhozfIVrz%2BlhBQRRlx9jS92D%2FPozh3hNmdJQpweCUQsDfNv5JHTEnPvbX24e4MjOorPUOICvqZlpqmw4taf04K3oezcd5HoDMcQ5b7OAYT%2FlwrlGHLgp90cpzIXbOy5NW8VOG6XDiPeMAesjl7a%2F1CCxktD%2FHA5fq%2FqkIPopnHfPii6obf0EQk1Sr2BB0f65wHH%2ByS6Jj5IT4PAn%2BmXworXD&X-Amz-Signature=dbcf019ce6d564bfe584642f5f068eae7747283740ca60cb3a917901052d7b1a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCO4VEFD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD6FeWIxPQe8EpYDSDhiTdgAbUK4q%2FP%2FnivuJCPf0OMEgIgGuAvt2YFj5BYmd269qqw5J2bH4homSmdKmIzlvjLn5Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDLzNzVdIoK1jp7VUWSrcAzqnWH%2BhKT0QuSbZo9USU6rCTYND5J2ogFuE9qI%2BByy4BydQvNzE4tlqXeGkATCwvxkRyOxhcMeBFo43Rr3sjDSX7vuAaYwEvzQQqQHRHg1ZY9bE5DkOkLA4C83DXda2ruQ3sf2ZRq0K54PW5o9iNx7yOaE%2FDLnQU5AtlT4C1pDCPO2P0Wb0iZIItlp2os7KRR6Xe1%2FRYU%2Bl0HkjloXWt547a0UIMAOMOqo7waA6ZZvAwHCqu7hE5ktf1NJ1BHmbDEQr7qlk1ExWT49gV5DyuxdQ0jgPKFclHSgVFVCVs5Ga2YCrDlHVkMQDIwmIyvxn4K0R6GA61yANue8bSnHqhRBCVA4vAGSJ0grTXwAGEeS%2BaFc9pF6NJ7eVXvEf5GN2%2BGnTGdHehMiGMj%2B5rqSFfS2Y1Ce818nZ0jZPpM62ckhAxbjOAohEpTg1RNRB1jiYI4O%2BP1bnfCkKqEfQWLpSTAkLg5S%2BJBQQaSfda%2Fs6fuSfezheMCh1JQFUla%2BUOrgNaKPqcrGO9jOUvEv2%2BpQjR1OwEm66T%2BqUc14Y8UFsCnp%2FTijJzp78pjVrARyYDW2%2B117XxuwGtWmP2lCUoW7DKQ6i8eBpDpA%2FB8s6RcCKVbWk9SA7Y6SVJOCeEeiHMIKalb0GOqUBmXi%2FUapkiw34VH%2FmVUU5G1aCmjkWRkAY0jSAWg61mnYd%2B2MXaFz9lnaEQRCH8JW8bXsq7uvKvF1nJ9L0zSPTw78WAQugdlgkeN7ya3XsxzrgbY6ZYyzBAGgd9i9BurqvHtrOcsmmDNd5e2lV7JqWJAdiiAZGYqF9bTDNpNtwRDRgGZHcdckfExyaQY2Rz55xT15WmTaB9IrMtY1TnfY2A4x5LFsx&X-Amz-Signature=7d5318273944ecd84020009ef034721fb6e935c7f202d722ff884778bceafca9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUQ2MHSB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIEV%2BCazFuzu2CMeXNn6SPV9v0e40vMqudzPFOYE1rtCMAiAZzwxgJ6Cp%2Bmddz6dwatTTsgVZHURjAAm%2BQw%2BopJLd9Cr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIM%2Bf9%2BYWuSw64dUGALKtwD86XVwS8pUE4n%2FKyrDS5%2BGXHfn44AUGfY7sWqMVAV66lUOaL6fpy5UlOpxoi%2BAKeI9YTUP65L5VWx23uFqNHEAng9%2F4NbZJQk9dNqDzR7wO6npkvl8W0%2FZd4%2BLIGI8qochgBAnLpwJbOrBDbtjJe927W%2Bo%2F8TDpZDee3Wy%2B5%2BrOyM%2FBSbHZSxljHY4IdXKW3Sdi4dJ4baQ4Y5MxrZ%2BqANubPgs1KVthQhc60Vsytz4o9Yw%2BGse4COhFLhwPaHo31H75jW5iLVJgzAn43is43i%2F%2FRIll6bpNmzWR2QzhmovxrtoTYjalxMoGkch3BG5fF4hxbsEO3vCOy7G811EwrYS4HUgZMh6V4Wk6hB1rzE5G3wKfK4Cs4sC25S1baL1K6W9DryyXsfDkCgPme2WWtik2yWtw%2F3noI8cAgAVHBX8THk2ggA%2BBFhSoMZzT%2BIUaPOwoIXWYqCkKGJL38aQY%2BlS1qMeIM%2F5PEIJYX7nkMnrOPc7NHcyAmwKHlmtSGhKS3FJNQ%2B24zRurgSoJgA7F0ISUMPROGfETHV%2BPqGhcxMByxDIMeIfmaRqODpLLpWgQkVmgSvjAQRVZJMveFc44Ub4VaM6yoOoi6vzBVF5EdqFHRC7dALojNlzCLj7HEw5JmVvQY6pgE05e60VUq8Qi2sXJi55UTNtEOjcKVpd2CIYel5kLk0kfwbG1RhT9pMmyitzhTpi2LYmHynrP%2FTP2TkvpExx%2Fdk78gl5DwMZmmau7SRlsr%2BUdoUBI57Ln5cB7NDf6IacrPFeTBs4XygtBSRj293QatmN0X5n4F8AAqxOYbej4NHMeVRVl4%2Bhoc0k4MtErdFT7w1qLv0MSp%2FDcBcXQ9RAUpKpMSnLxwp&X-Amz-Signature=4da383d4d9b12c5eb8c8fa92fc505ac00329f11787c0dc9e1b18549931500f63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3VWY6G%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCICVPFA9L251ApFL7cYZS8AkCLS3L2vXJRNdW2Yojs6kqAiAaq9Adz42618%2FcvhOora%2FUuQmIvwE0dG%2Fio2FzR5kn0yr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMb%2F6goyZ%2BhQ%2BYL9DLKtwDy3mvLgXSL8VD%2BxqksoX5E3KakKv5ugTyBTfAYjB6hZ3CXoASycIzfknAR5jIwlL6dcTVJewRHAvNdrs7QIV7%2F1nDrpoT34907KNVWbaYKBIzS9QUIupmT%2Bs67hoYtXIWY91tt1bv%2B8xUi7CYH2oaflvHqOrcGZpLyeyCsuI9jolu%2F7arnlnQpwHONKp519UM%2BSqGq%2FIDBxNQNHKH4sdc39AlJGbybXUhr4M6CIZRhXtGn%2Bxk7h97I%2BEW5KYVbrzgfWDMVOI8omodYoz9XvUcQM6ezUZZmKxR%2FE1m7nE4RxZcXcpXmMUlSBQOcVcgb01w%2Bd94tGqDVhNvl7t%2BBzZZQqq09yn3F6xIoBry9QGyPvg7GwswUgPucCM4arVPGd5crYKw9RvFBhbw4TdqWMYLsF8WAstN1uyZgB4tpUil6HD1VleECOd3BK12zBNqrcIbZK2WbmQo1RfCAe6DWgbKmbjjW4JMD7VHcsAAJ6%2FMi8lxKxVwQPdB0QpeKQMpUJRPk%2FMuDjAZ1U%2BtejcweaCsK1x67SC2ZNBkXS5x0K5zLPFDKHol9pu%2ByQuqblzKavRqxYBjNo%2Bfv9IBEbEeL0Ofc15JFfj52A%2FgN%2Fua3w1Brnm5OWNkugXG52wr48cwi5qVvQY6pgF43EaEohvmXaPeQOTrcer4C%2BEJ3b2Qcg8DpExPzXYU12%2Bqf4XqRQpclGlRYKPwG%2FOzO2pqOy5HmKpT6kBpPN0UoA8YmOO5yAUqdNdUxcvrYy9abb0qJrtqXImtEPJ97LjaV%2BmcrnzVXtjTDHydlrGUiPaP%2FqHRXO4BiegS3%2Fcruu7AOaC6fIP%2B4a6pv10Ey6otHJ2j2sNFfEbYazdRS3LpuKHgVDRd&X-Amz-Signature=76f33d558f68407cec69707243c854db366711fb99cf539a3dac09c7e39ea72d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIQZZR3V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIAtwgaoMHlKGN8h9rL2FejhRSgoA89jQT8YS5vTZOmsTAiEAqQc0X9E9NL9l8Xl3gle4tNzCp1mV7Bk63oK34IxPwA4q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKP5k0vN4ATGzfx16yrcA9KDbqM66vNWdQ6HNdCe2FFCcnrpi9t9Mo9ZxeRwam3bvU6wS8ZUayFW4tf0fL6YQ3EnbJD0YF8iA5jfJWWLtfJxNmjy2qiUPbfFFz5HRQUHzq0cchc%2BH67R2Akc6gNByL206CPhsVgZHl9YqLR0NDXJCwAQAqMkqIBnLFStHJCaw0M%2BJ19PkOZFCg6xf0nbH%2F1dH28FRCIjP67gYgCiF8tJ3CtwFL5OWuMD0Ri%2Fqq0x3J2iNSgfDck6GwyP8hFVf8LVgE2B0mJ4%2BU5NbhXuDjZ%2Bg4XQ30sCQ6L2MamFB3YqI046naXgWBoFH8WnWhZb%2BQ%2Fnn0%2FfXakQcWxlaEQjJY3XGFi5q4WxEh83BHoYwE0oiG94nnG7PYPM033Wc8BKfE56xUQnZUxBMYASmhhzSoLTNdT%2B7i1xkOac25nC40UtKSc1FfUN4Ib0D1x7GYHoGy6SiE6N3%2B%2BIdgSMD2ynpOb3n3TwwT0%2FO4GI7ybKgW9Amt%2BOOLJ2adiKTVCkBbWU4KMJGl%2BsvQorNwjEcD81pWODOVKFCo0yWybgxKiFtk3R6vww7rt7qZBqWgjUjyjqxvccLn0ueYcyfp9IHqdw8avpHd%2F69fhcvjitI9Ul02P08S1%2FxSPzpK41Wn80MLWalb0GOqUBjmjOMx2%2BUrjJFgQ8FJ7FDEpJcmREHu3ZOuSlnqkZyU0VEbhz9JcWSTgjspRDAXSsnTJy%2FpYFxw8TlUiGIF9FZ6c5R7g%2BXaoql8TlVo%2BRPYE8EQjLYxo4ttGF8Ey2zqbL1gct0LoTnijCWz7pv0SmKLt7cMu0wHnpY38%2FzAKKZqFgZp9ywvqQGGPWNf79Ckv3grw6gMBpA0tEWjTEHy4IX5lfw9J0&X-Amz-Signature=9f93e963376651bb8be0d94c1ec3195b18f4e4cc03f5812beff5f7e0f47c3700&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YANCNTG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIG7gBAYEyse%2Fkn6Ysx9QSSUmZe8bFvULZLgmTDKCSPU%2BAiAMu3bApXr4pbutRB1i6KkRLGk6euHjChUjfIbcUhlYWir%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMP1B%2BkjBx177sGVfjKtwDLFkaLs9pp6nfh%2FUddpscsRdARsHjdbUnePKcSIig0k94Zm5ssYnIVRQhhlJ0aN2A5lq%2BehTRb1VWFjoFzy%2B3xnaqAGXAMvVGK5KKX%2FIePk8OzDtqPHPpYijqOJo4YMkGISQMtlvTBzqAM%2FPX3Uor7BUf%2FK%2BSOj4BF4D0OXiwIVbh5QAfCPzz8rfHzEyka8u5nRO3HWVf5ajHf0RBQ0OMmmaujOSqRvKHw9YTji9RvdEauo5cIa71VUo%2FowQw3c1df18kKNDHHmzNK7i96oTY6AgnV%2B1tZyA%2F4XGiiz4o%2FLnxG4mZrdN0C2GWma6avyf2IXhedxaV81F%2Fh1%2BnVRgu8LcNlOL%2F0GH6SgntxtlyvybJG7v4x44Ozz4RiJ%2BI%2FZ6%2B3FBibVjmYZUFHPXL584Kdqpns9dbS9jD1UzH35GplDTN8Q0EPvYtY0jL1tX1gw0AIz1qIlHHIekN6SyjFA%2Fl41qJq7xhCXFA0DR0qDExCOQlHmtF9NrU%2FvDRH2SusDX58%2BZA6ZaFXYZ%2FQM%2BA6cBwkF02adYxLZxzFOcwmGbr0sR4t9YZ5sd48BCJ222WAZMKlef2cpsxD9dty4AE0EOFX5BM4IuujnWyP8O22HSHi7KGGDTPq1CW9Af9dT0wg5qVvQY6pgH9liszJY2PM%2Bck%2BmtWNnJDurr8g%2FQZo9ajQHzbDhXLdZ5XY5JPZ%2F8ey7BHP4dw75jZkoN2txyNzkKBjJtMNBttVTtVjbUJHw1GOI%2BsuWjakKMkz8yraxQZ6EkLGfbpWl5xjpdXEMiQhXmHvYXTD3F%2FpKfN3tdcqqQ1neMIeQ2ovLg3KS%2FbliB72I9w%2F6r9fkv6ip1XvEb5fH0T22TPAJzoTuLN3OBa&X-Amz-Signature=d06d44eab1b32368cde5a60b628e60169cdd4b664d96ce90f6508630c65c7dda&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663G4XKTYT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIFGeESWBXQ7Glfq3pOGd3aom8Qw5tWZVlUPELs1IoobmAiEA66nr3dLA%2FlGX%2F4NXnZRl6JunON7TpKH7VOxN9iDHRIMq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDJhBiOxnXMNKxevbVircA2dur%2FHqsIa%2Bb7agk%2Fw8pttHmT4HS9hhfWramybgNEtwL5I%2FQ7QiKHbbzDtMQ1PBESozOvWFyN8tV14GuVFOb%2FrrNSAUxcGnX6jAPO1r%2F6WyhgQ%2BaKuh7rhywIamXTnWAP1p1Fm%2BpBwDLe5K2DbZuxUsOgGEIxGzRiYlZ%2BKqPq3x2seu8jtPwW1gw5Zr3EB3bDS7ZhTY5DsAahy4q8PlzbOnTkO4TX%2FwyFCRBVuQUH%2FnAH5Hktu2b%2F0dKWGj0wtjveFUY9%2FW8qpuwenou1zUNL4z42WVQvjEOGcQoOsQ7go7da4Ed4nSLvfIo7t3hO8dBPXVoeb8GumtMIv256iHwsJd2UI84CW5qq%2Fw%2Bs1b0N3KI1I0ESUyRKpHwi2UWMlGv6%2Fl%2FEHaeNVlBBQRP%2BjNjuHVeQLg0v9TX5HJ0Ep3yeRVkdZ3ldPst1bqI%2Fu9ymejL3f9d%2Bxk9SU2f8dMA26YxDyx66b5o9HK5D9ZtbsHzsjiRqSa%2F2KfKDAdLWIEi0%2FuSNnpoaW4BrPAkvYrH7JXFnnwLVT0MXFeKUjKyckryWyC0kkGCqR%2FM8KwunaZYaWmZqhWWzfZaRGH6BWBOK9t5vYpMF%2Fa1SQEERNthhaO9YFuZ45mDxaxMJesAyyhMPaZlb0GOqUBkwO5dTMqkZI8YJCIj7firJxPJuFr4%2F6i4n%2FgGzCXHOXdM%2BK7S93OordaudrxILig52kncn2rCLyL7rm0K%2FglQPjCGDNTxzME2%2FWZbs5z%2FYcV0BHBwWppfmbHG30sPMsLXxaDhh9ZwWH1%2FRruLAIrkgB1Kkb%2BrFe1nQNxcEKARiOBYfqDn9sadaLMxhKLnRpTtZtFkme8KSRNV%2FrWchFw29MH22a1&X-Amz-Signature=aad8267d4e7975fc0cf7c7d7a30877764f901e9118d3a36de951516fd37570a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3VWY6G%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCICVPFA9L251ApFL7cYZS8AkCLS3L2vXJRNdW2Yojs6kqAiAaq9Adz42618%2FcvhOora%2FUuQmIvwE0dG%2Fio2FzR5kn0yr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMb%2F6goyZ%2BhQ%2BYL9DLKtwDy3mvLgXSL8VD%2BxqksoX5E3KakKv5ugTyBTfAYjB6hZ3CXoASycIzfknAR5jIwlL6dcTVJewRHAvNdrs7QIV7%2F1nDrpoT34907KNVWbaYKBIzS9QUIupmT%2Bs67hoYtXIWY91tt1bv%2B8xUi7CYH2oaflvHqOrcGZpLyeyCsuI9jolu%2F7arnlnQpwHONKp519UM%2BSqGq%2FIDBxNQNHKH4sdc39AlJGbybXUhr4M6CIZRhXtGn%2Bxk7h97I%2BEW5KYVbrzgfWDMVOI8omodYoz9XvUcQM6ezUZZmKxR%2FE1m7nE4RxZcXcpXmMUlSBQOcVcgb01w%2Bd94tGqDVhNvl7t%2BBzZZQqq09yn3F6xIoBry9QGyPvg7GwswUgPucCM4arVPGd5crYKw9RvFBhbw4TdqWMYLsF8WAstN1uyZgB4tpUil6HD1VleECOd3BK12zBNqrcIbZK2WbmQo1RfCAe6DWgbKmbjjW4JMD7VHcsAAJ6%2FMi8lxKxVwQPdB0QpeKQMpUJRPk%2FMuDjAZ1U%2BtejcweaCsK1x67SC2ZNBkXS5x0K5zLPFDKHol9pu%2ByQuqblzKavRqxYBjNo%2Bfv9IBEbEeL0Ofc15JFfj52A%2FgN%2Fua3w1Brnm5OWNkugXG52wr48cwi5qVvQY6pgF43EaEohvmXaPeQOTrcer4C%2BEJ3b2Qcg8DpExPzXYU12%2Bqf4XqRQpclGlRYKPwG%2FOzO2pqOy5HmKpT6kBpPN0UoA8YmOO5yAUqdNdUxcvrYy9abb0qJrtqXImtEPJ97LjaV%2BmcrnzVXtjTDHydlrGUiPaP%2FqHRXO4BiegS3%2Fcruu7AOaC6fIP%2B4a6pv10Ey6otHJ2j2sNFfEbYazdRS3LpuKHgVDRd&X-Amz-Signature=efcc30777fb18bcef5d3aeb6ec28a082e35bf692b77b7ec1d770af26796f2a91&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMDAL56R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCokcS9DIdi6ho8ok0s%2B%2F7Q%2FQID%2FXLNjqoEQVETbORx6wIgUV%2Bl%2F5n4U2HmJN%2F3FxQzdVmo16hsDi2V07%2BdQAC%2Fy7sq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPIbMcBaxGLcozH0CSrcAxQtdHc3zoyFJDjoYls8Hb66zzDGrZCN42QwkDduQNac5uJLAuDj2ryBwnmUOjSfmq%2BnUwEov4ZVCD1P552isFqr5zJHJqZvBwX0SpNs%2F2IvIBVetQoTZijXxwbFDZFcz7egNsMijh8V8pAe7xGIUiq1LvwNV2NU2Wc6OueE%2BdAviBS7BMGfku%2FS5%2Be2469QCmTbj19CYKIRnYOpDJsyBF1BY%2Bw2W4VNqOc1slfJdo%2BZXTNQjf3D4088H8oFNyjqM1fEnA89DMiHY6sG8V9pMbM88t3dxe8xGa044jAJQHNThOzbv4BnOhiiM51w59nGzwlTzb947xV3Se579E8gBdweoPudevkdxLP8wh2X2TxUPAAHVFC9YnxsNb0UzdOgbyuUQ9VtIRYdswObt9d91R3PkutLpeSyc%2BIixfKDbvn2DKbSY43fOl5%2Faq%2B5eZ8jvdMsevQVwDMiGxueKsy2K9kThFgCJHpsaiaiDZ27wEyhPcZR3cXCp4VOno4UnjpCD8Ffs1i9N4GmK43Ps7VGG6d2tykRG2ib7GMas%2F8Zg7VH6lnShUSx%2BQEkPLLo5yhtTbXAPJR5H%2B1LnRQikz7qlgk00DT%2FBzrQdrjDh%2BQqtOaTzWT1Wo7f7g3cg4LoMKWalb0GOqUB7prfYwF1xUzck9kvwGj4zYCj0LdKYkhFqKEci9Pe23Pr43F1vo9th89d9ezOcnq9Hl00PRQChpFh12%2FXXtf70OzRKAaDJJvrLRC6s%2FDBwXSJlZTwWYNvSZr%2FBFUXvzO18w%2F4dBOndOKTPOQ7OHdAg8M0ALtdYdBp297iipN9cNKAR153eIfmHB3ep57fbyxrOR6unF6pgABRCynDIh74GHczIb3d&X-Amz-Signature=e5ce394d2128db820889b4098fc53553ed4b79d750429fe909ef730fd7ccea94&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMDAL56R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCokcS9DIdi6ho8ok0s%2B%2F7Q%2FQID%2FXLNjqoEQVETbORx6wIgUV%2Bl%2F5n4U2HmJN%2F3FxQzdVmo16hsDi2V07%2BdQAC%2Fy7sq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPIbMcBaxGLcozH0CSrcAxQtdHc3zoyFJDjoYls8Hb66zzDGrZCN42QwkDduQNac5uJLAuDj2ryBwnmUOjSfmq%2BnUwEov4ZVCD1P552isFqr5zJHJqZvBwX0SpNs%2F2IvIBVetQoTZijXxwbFDZFcz7egNsMijh8V8pAe7xGIUiq1LvwNV2NU2Wc6OueE%2BdAviBS7BMGfku%2FS5%2Be2469QCmTbj19CYKIRnYOpDJsyBF1BY%2Bw2W4VNqOc1slfJdo%2BZXTNQjf3D4088H8oFNyjqM1fEnA89DMiHY6sG8V9pMbM88t3dxe8xGa044jAJQHNThOzbv4BnOhiiM51w59nGzwlTzb947xV3Se579E8gBdweoPudevkdxLP8wh2X2TxUPAAHVFC9YnxsNb0UzdOgbyuUQ9VtIRYdswObt9d91R3PkutLpeSyc%2BIixfKDbvn2DKbSY43fOl5%2Faq%2B5eZ8jvdMsevQVwDMiGxueKsy2K9kThFgCJHpsaiaiDZ27wEyhPcZR3cXCp4VOno4UnjpCD8Ffs1i9N4GmK43Ps7VGG6d2tykRG2ib7GMas%2F8Zg7VH6lnShUSx%2BQEkPLLo5yhtTbXAPJR5H%2B1LnRQikz7qlgk00DT%2FBzrQdrjDh%2BQqtOaTzWT1Wo7f7g3cg4LoMKWalb0GOqUB7prfYwF1xUzck9kvwGj4zYCj0LdKYkhFqKEci9Pe23Pr43F1vo9th89d9ezOcnq9Hl00PRQChpFh12%2FXXtf70OzRKAaDJJvrLRC6s%2FDBwXSJlZTwWYNvSZr%2FBFUXvzO18w%2F4dBOndOKTPOQ7OHdAg8M0ALtdYdBp297iipN9cNKAR153eIfmHB3ep57fbyxrOR6unF6pgABRCynDIh74GHczIb3d&X-Amz-Signature=db79d6b09183587526fc5c5e38eef33dc731e2f58453b989e5e5a1dd49b22e46&X-Amz-SignedHeaders=host&x-id=GetObject)
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