

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WK7EOQRV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDVe%2F1VFTUchkgd1uDSp6Ekd%2F6KkgI5njajZymK1DIrMwIgYIgwl4E4OV7UMpx2AQSuUjcVF1dWK1Uwys6fKbqMl9Uq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDMngTNCJ5ccUz5oukSrcA01QfsO7uE%2FqOU1CGV3dHY2IEio5A0Bv4HmUHRdrFvqSt7gPuW07bK%2FmaQCq1R5L61A8UhfrLpDN6tQBz79UMsBHKen0BnVmSEpaDDnN0wgZ0T5LeO%2FLRK911QfxmzjDw%2BLfcrY10722RqrFgMqYca5qEI0yXnBpTZxb9VCX28y4EF1d6blJ69f8Btynvjiws5aCamWWUD51XKjNmF5OGasIHvtxiL87R9kDjhUcvHcPln0pHmwqALA%2FI1Zv28wzY5vzpNF%2BkyfH8DmjCXLJfrahM9BefQadHzvFIgfvA2lGMas1CnO3SzdYFbkICT3qU56ZOEomvMJ%2BAESlsyybdJTFWbxODlRgbOr8wGIwXQcgstaLSdd5HrjD7HacuCwyT3uQHc%2FReE%2Bda8tr1Sd70vDmi3qeXpNjKOc7BuIzQyJ4DoOTb3ZVUSFWj6rvB%2BsaFMjPO4gC1NySVuWgFFQ6SPZB79vEDKrjTP4oh%2BfXiau2a%2BRYOleukIs2gosIK8fm7nonl7ifhlMu9rWoKIRwPZQKs5OzPUTLx8Uo8rggNfjSBQ2z9%2FpBFrAGdjOXWOLGlIIUeaUuGG9jNuglcmTvKUJs28%2Fs11H2lLyYQ4owlOoORroE39aX9tNujt2iMNP7k70GOqUBz%2BMfZymsHVzUBUAl4v7s%2BSdmmgjLQn7EGuvGY%2FOk%2B83m8i0%2F17ANdJtjD8k%2FTembrddvyZEaCRI5aAIQBqAx4fBEeWjmNiZenGehEMbYOnAJrEUDTWxoFpCBpgUwctIkRYjqlwdtAOyiLc612JuRow6nMRwdb34B5c%2BAdlQKhUEsBLAiRhwRmj1D53pDR9oYhxRDgZ7H3A0KydjFEh4LVqLi3wTx&X-Amz-Signature=7eccfc3c697825d2d0f836fec86a9048bb4f6753e97dd90ecd7cf99d08a9b386&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNIIKXNB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQCdV1mCA4ZkvtzPwIgyhAihXfEk4taH3hhk51xxvjyaOwIgVGeVNwcoOT6%2BY9V4uJV4elAzGon60vK4%2BM%2FbyuL3Ol8q%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDPlMP86%2FxS8MKB7UUSrcA%2BH%2FJ1HWF4UjGyDeXw%2BBNKixU7K7ApV4W9OV4KBKUpIagYEXSmJ1p66eAjWuV%2BO7PROI1aS%2FD%2FREge4ypjxVmNaeTnRJk63nYoQeOYKf2oQc8VZDGQGDQ5CAAABalRJHYsMLziFGykTaH8Ybhk0XYxW7dBFn4Pr7oIQep7gbzn1ca9feISPx%2FT12ta6XVqkleWnvXxHQUuBbSmNSw6wHvtvcoJ98k5X0LGS6wdb7HFv%2Bda81L3Ihc11MBjC8MIBM8HlqgkcPWXSva1VaqTDcer9GChV0KP0riXSzkpVpc13K%2F51HG9FXkMa14R%2BWJYD3U5zUQs6HUxf%2F2GNgoWI6kw9NpRLqLtr99vfz4P6jfi2RX6lAekZs4%2BhPp4WbwKqJvNMTFpsDaKxWEViN5V13aeJUH6f75yH9gkAug04cx4g2j2ck6vJXoHWCLs6RNDbMH5fUi%2Fm2EXk906URw2QRz7IefelWvNCV9c2ru762YZCHJMcgszDM%2Fw6N9rccyQue4j0DPD0UFgQbQKjaUNV6CZRxb%2FSeEimG%2B4cyPYRz0pAvgosuBVjECjC1CgejWu3ZmUlbdiisRIQAuhlxy3dpp0srTphF46lVvYJAjN5qSH69xHTkqmn8nmRIYfIDMNH7k70GOqUBJN30wfRAoq4amSFeNm%2BtXg9ZrbnGPCaoPl6k4t1oHWXtW0P1UCDxb5VXymO%2BD6TyKTq5ChyJJ0V3QGADt4QEUYsBSyhqDYnk7%2FhibxnGWrC1BAJuly3dd3N%2FzoEI1H4V5e0z6vaTFv84es%2BTz3Atwph3sryCgEsBz4RsmH%2BOUik5%2FhkBNCBvp2M%2FuzQffjgkIq7L4wL0B6Z0bZAY8ogzVuZ%2BLxkl&X-Amz-Signature=a7e11b57272a5f811af842c42452a9d9ca60d65f150fcdcaf18d7e0127a06d4d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VZJSQS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIAG9VKFC8uQKdA1%2FmO2owKqb%2Fqt6h4O%2BJ51nYLmN9zmRAiEA4AtseZkqmGvWu%2FVpglGRDAQyxXFLwtBlPQO3ouwEibkq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDFG22xv3Kk6e%2FDV4BCrcA6vmDgSqbul3YyfIVtFzhzBYZEiXjCzljPlgIBF0dvchRLoETiHvj3jxdBhjQkGEUkSSQj2K0ykQ1mx8EApRg3xqhS%2FQRRPjs5JIFAoVJWdx3pyGPKdtE6PcysUr0EI3Cv1gO70OFJpaNpcGY%2BI7YMiYV0LxRrfx9eEwCQafZk%2B0azCPox1u2ODSQZvY1u8oo%2F3QJXKT5dcSrAVJic%2FgKfIPgwS9T8UMuCKZSjnPr7DrUY0Bb4rYZU5Q5LTrZJD9bNR2ACaS5AEZV6pa4tJI7c%2Bj0ZT%2B91pXex%2BfuARbdJ87AocJy0bYLRzNPAotHAE%2FYsrZ%2FjVFIYnVMfOYBkGJzDIK8CkOkVQ4Xa9PqtHwbz3OIgbxjUGPe8QxpahNNVgQn7GhSZwxmCDGAkfe1Lu2tNDcVbvLOAuWRq60UjzXnZTMSEg3l94tBe22A3AJlUvwME%2B6V6MbCH4OyHSKtZ9dfRZzcMrt3d6md%2FxKzp0DJkB%2FvXP6V8EV5QaBJEe0zQlvwTvxefsbPRXYn5kjeRz3%2B0OFu54I7f%2FiGHLyAXIakj680fufemlBgxCtPAddQHaV%2FTaQu8uZ40LTbqVawqtSSmERlk9EuvDkuj%2F2qHgNAxZo51C2Un4V0OLel6RRMOP7k70GOqUB8e9h3yjUMXre79kbzbAFcA3LvX2GUw8xw8xZH6GzPt%2B2iOoflyC%2FlYo0Y9YOvE7YwIxFph8fpvz3YQgh1hZS5zAL4oY5OjIsku60ceWhfCUmRrNIJyMZ82ZOis1VEawTMjrh6H4W9HY3VBGhOoLjSpBpqGEDKIOFKeDnqcroEyE%2Fkjh6f3z4CTRBdkBoyChtFH6yuptsCGLg6RyeVY%2FPMM1qh1Bs&X-Amz-Signature=460f03fc93b09ef054714ebb4819bdff883142499c09401590006994f7376ea2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3RUEGCI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCuvIXr9JjtW1uhGH6KdhXZoNMFExGrwiyfAPzHnSiKuwIhAPR63tbGu6lf7gdQwp84OviQfXohLzrEy8iA5kPypYH8Kv8DCGMQABoMNjM3NDIzMTgzODA1IgxSXi3bUGxzVHl0B0gq3ANSD4c3G6TYkzYGk7l%2FsniqKAcp7aMeT5dpGGY5MVLouS3WOUEroPFsaFiugVn%2BxJ%2BId%2BYW9ZjBwTXUlvwzLX9khU7QQT%2Fv9ecYO8xTetAcOo99dq4a9TlMheQE3%2B9KY6kSmfmJGA7vp4b7hKwJyuk2CoiHAQVJuUFPl1Qezgze7ouKcA6EQ0OOVX3ZlfpkeYueILtt2%2F7Gh5ptWB6wNyr3JnTe%2BrljVRV2GHOO8BjrvKt9c1pQnVbszZKNS1MV47ti1L9XDQ0wTsb3CpJaVkjnolPRiwU5FKLqAf4x8i1XYnAeKNwXpzDcTqvCuAHpR9%2BfTnMYV5k9Q%2FB%2BhkSwoQNolLxLsohRDrzxCiBUFoDvbe6HmiUSnaqPXLDXOlHKd3u4hjKN8%2BltVw1BTz73uZZ4z0eLUc3p4xpuu1RMQlyCBakGCV73Ek3VdIj5%2FbsWFA3p1wWrs78MycGxuILNixNB7sP34%2BUZksHMGGKQJTkchfiQzcCVDFmYVFrXbhGK7%2BBWdgQtB5fNG9TN6QhdYRbbAVa5sU7APEY1SWBmMNWpBhMPBfe%2BOQoUKpSUj26dZxLcNBndDUMZjx4y%2FrqGux%2F9%2FdsWqu7B1UqxUR0hWhqr3W%2FfNKMfCo3xEY2TvDCM%2FJO9BjqkAVck2VY9%2F%2Fbs%2FTnqkJDbRjZTctHEkj8hf%2FwdXW%2FYDX%2FCdQUjLBic0HnoxOMTQNnCuqeJGV7944H9pZWMiOcZBlt4Zreik0GTuc0r2klE%2F2BhxAO6flfBFnP81ABv%2BfZ3XIciMOva%2BaO9Q5cN8deLuPDbWznk2EDdtLazDpxU09OiSA8AhZxYvXNW%2FVSSuMguC1exoqUCMumTUbwSRx%2FooZliy8uE&X-Amz-Signature=8bb049eb6d1c0a5bee7498b10b98ad8718dd0a3f1e2c3a1f97890da1103e33d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZPHIXHD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCICnnv0hkXnk4xMghfaGYATUeVWD%2FDpL2YqpPyseKSv8lAiBQ0PzRdQNYFDNopzUEyePub2oSvqYINAbzwKw1itmWRCr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMZwJE7bkouEmbAMywKtwDCrM2ihWepV0g1qLCTFFBeS6jxBSVPt2w7dUhgTEsv%2BTvgXnaGms%2Bo14UaYV%2BYw8ScswhX0JLit5kpbsIAiyo%2FGuSFZ0WvdUpUUlFaOG%2BKyne5qV4ylmSPpRiayrwLBwun%2Fi%2BsIgZ494uW%2Bo0rYxyDOrQwcemTZQWi9jaSgK5%2FJak%2FfuIatRuNMVfNwKDt8nPLieJJkpCFrY3BuqJnj8ZCudJA0vBhumnotiO3A701Z3uFRBuGReaWCSELa21vA9LaJly%2FCb2M6lstzHUiSxeGun431GREcR6A8puebJfNegHQ7v4YB6Pp2iy4ZudOqqJTqzEuJXZzWvRXdr0dLTLBfZ%2B5mIUqLQRyF8GrrcYCbr53yFP8X%2FTm2jtTXMU83gOc6vHQ8H2Z%2F%2FhDwVGb0%2FJgoGB1qFl5944NOm5wCVKxjAXENWJdPXRTHXjYzoMMsSGWdnK6M6D5f7Ap4iKjav8ozCTBXq%2FGV4xxaub4NUIZ%2FB3fJWzqTGTqFh1zl0dxBqTsgfzdPjjsg%2B5UeTGeyRJ1cw6E5TJv9WWcZopGoMvPPMDNxChb35iJ0O1ykNVr5u3CVgX9XI6f%2BD5%2FmLRqfKavn02Z7r44TaZsKKwo4IAadEvOez4PKxEKAj5WRgwwfuTvQY6pgHrW%2B5FVq8fRVx2bNiIb3HFAwZqvxqA9soqYcLyjAwcxqaMEA7mjfQapy0eJ%2Bo3vcIwSYqUTZGbdAfRRDNFtk7q%2FJjly7CBdFwPZm87ei6NpZondp4KJbs2ar1k27NCryiB2ryaAdR1YdT7Pl4iYDrNr%2FauSlSio5ePQAFLH7UQvX0hF%2BReRIPmZu44LCd7uU10X%2FQ68MZ75k8FA8eEAQtMFZCmK4FG&X-Amz-Signature=698464be73847dcec399409962fb415885360edbc77ab04b4d53070a1cf1fca2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G675Z2D%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDZHiTpD1LND3OdNl%2BLOHVv4Pxz9xPp%2BwJA0ZXZ5ef1SgIgEcEooIlMseKpWpGk87JYAihkQ8zoBwCunwrX%2F%2BT2up4q%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDOVWpbtMcDVHteQu0yrcAz7I1XOptNk0L%2FkjSJ0WBHkrHpL2LwxawDvSluKkHRYT908gw3kvQhXtnhUBmqRUP9l5e35OKhu4lwwWE3ESdOVo%2FM%2Bb%2BSIK8yiYyg6GinabOTRsIlaMq9chsuIhnG2XBChNNEjy9P1J0OIFP2n4RxQXLznt%2B%2F7zsNJpiIdJ3sBRXfjHeWi%2BY7EeOjQqJ6zWLTiUZwlG5FYA89nusuSnVSzPsnUx5Neo9D6h%2BI7iuntSWGZIiGumpCcwH1T4eV4z0yuiTDbm45M1%2Bv0qax6MfM6FQiYau9%2BumHNQ9pRmusfrjyQ0hasqDr6nTyIedA261SvvPicNyq3x%2BM7mGXtw%2FEcJNddz4Qtk%2BC2%2FmxP%2BZb3jlYobOYOF0gk8Hxm2u8p96OpVME1nkBF8dZtDb4Sdi7Qx6y%2BSvMhiF1dEa2VlgkIWAxrpA4INlePIWUqlSJaNQq7CJDhCPG%2BaGz5IKWd4ElX7ex5vYYTYoWthFXidyVy3b2oYst%2FILzRs0z31s0zoq%2BbmItRq6T2fgYeFdypWY5yYSBDCUSIWqIlGTWC2T7F%2Blw3jaDZXD3i8uwNU8xJJvUFWy4VY1tG1nkL%2BInAHm0RvLPI6ZgNRTHTvMDeQsh7wRDijtcjtU2SWGoHUMK%2F7k70GOqUB7Uc48Py1%2Fl4%2F0BuXfj1NLtTMEndjM%2Fa7cnOty1QVSDGuSupc92y%2FOoh6%2BPB3pvRR%2FFFP1Fw8%2F5l1SWbtwsM15tWIVJ1t8txDxtj0FRFLG8WqucGDsTXRoTbBKZOS8kBb2eD%2FDxmxgV4YQsl6MuW7K9rpBkiR0yQ3gGgQUXwYL95Z9ZfcEwheD%2Fm989eRwMWomuceMzpSDQt8jzbgvHwJV7EiLaUh&X-Amz-Signature=f1d0d3888455ca702fc4d2510b5ba9d633fa3d6e46fc78de8b0f9b010520a808&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFLDO6AD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCX0xcOJQ8zZdYU6U1QepBc%2F4bA64cnN6TCbHyxjkoaAQIhAO8CEKEm%2FkFAYPiPDEu%2FWGxUMM%2FDp7oerr9YxNvb727rKv8DCGMQABoMNjM3NDIzMTgzODA1IgwVNioH6t1YXSsjqpUq3AONDHCtI%2Btu02f21Wd54FfFYY3F4dGYIlSM6yfvN1VlIcAyITzerPwqijaHj4NMeZSMpDDKWro4StNNf8coDaXc6Z2n81vFBG44aaDIEV41Ua66MA56jFQl6TII8ky1B4jXaKv6E0xMXRJ5q%2B%2FvBTybkZu9uvgaTcW%2F508s048G6mXVsc2svBS2Q7vuaGwoKb%2FyEf4CXfdI9aL7CS%2BcRSBO5v%2Br%2B39HdAeSsvg3UaQ962QS7ENapJkNN8%2FN8Avo%2FSbu9DIJmQGyNupCmSMtudkXhIc3hE0e%2B%2FivXISyg1LihlBxzFGnN9Dn8Yym7xzL15jgGljLF3MCJGsriKqovHLbY5dudhK4xcQyWjvXqCfp7yl4swDxbUrz%2BHaiBZ19Ogt%2BYRRy5o2%2F1wcBo6rfYub2fJ89neRIp%2BeZnndmLbHi%2BUbxRrqCvS5Xzzjugplh2cs8MLTMfS8K7DlCHa6iT2lV%2BaN1Jp2IcuEDPU9LISpRqCcwyiQEsnAgzshyVQoPy7tzUvI2EfMQoU%2FcCjBDCJhWXGRj28fwxlxgqZrVP6x%2F1mFht3U8hv5%2B0MuN3XPTBK6r1oEVHo%2B781mEsK4bW9epqEWRLlo1nYa9ygc8nRjgo%2BnL845Ftc8D8pRtczDL%2B5O9BjqkAeIe5%2BQCf4NTj24A7vHJTeZv2SqntrM2YgXTZ9JjxgZE8QJoQwTt2FsmbmFpBr9BOb8kQ9AAutAj7W%2FMemgmniCxG5%2FVIRzoel%2BKjFbbnmqdKWRNRYWFjCqflnSiXyEljJy3mUBaPb6qchKxJzLfg0o%2Fnp%2FrXhApqV2lHA%2F4Wj38z89p4rP4NhJhQXffSoDYC0MaVaOgOMAzWRU7zvh%2BPFh1twwL&X-Amz-Signature=509d5297ec8553556a93d599165b750a436e172fb4a66f262ee6d721d9b63bd3&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGOKZ3VB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDnbnZi3Pa2%2BrVk4AOGYpnIah%2F38mYoRtgSVLMrItXoAQIhAK4Fl2suXE1FcKDTPXaNRPadpqbB9wp5lQISRRB1fxQqKv8DCGQQABoMNjM3NDIzMTgzODA1IgxP518eJ9p0NczWewsq3AM5TiJPPHxjkmETNpbyctP9jmhjCIng%2FUah21Rs6%2Fjfzm44fR5DHtzYTGaa44eGuUHvA1iX5p7aL1P8e0adPsJDCf5ljavq1i22DTRk9oYD%2F3RslRntDOSq8PoP905O%2B1AdZiCL8Or1XJzH7gJkyrRAM37PObgC5toqdz7BybJiEF%2FsxROp%2BCiWSjp1ZzM9PcVfMoXcjKOcESlMuvvPtuai3%2BVX35qpqNTqwJ9%2BHo3RhJqkcX9c8CIpR3Se69ouNvOUV2V6NvYDGJFiLerlggWMGL0K8l0e3kvuns6DNQTXHdT6Z3aVSmMrTRuXgnq8BxxZdyitdj3PPi6lly6lXxPQKaOLmwz%2BVyuIpNXoWEgOA%2B7eip1Ry%2F1xRAc4M7IwXtZym0ZDos7ZvWXxw0%2FVDWRTADEmPcb3JdywsgIzdsSxTh2cHRvj2%2BSgHl570GlWaS1ZccL%2FyvDO1xNA6Zc97rQuRtXLXzJiiEsk%2FU%2BgYJpbwIbDniwWaFLKIPdmpsRS%2BntXlv68bW4fnwEkorlnzalUfc%2Fy5AyZrnzqwv2Dtw%2BXMJCenty%2BzvuvMR6cGkDj23O2rE%2Bm1IedYr%2BUczOZHZf2incdS7PvzwHA7pRrOvQSdzFsJ3F0zkTK4I9vlTD%2B%2B5O9BjqkAZV3r27s6zNtdEr4cmW6mq215sk4MHdK2jChHv1DksFXI1Qj1u4ANH1cLSj%2FHGIh%2B3K5Vi7%2BNZbQWvnWzmZoujrzKSnLnAvrM1lCOEZ5jrO%2FNC8qR9UyP8%2FSirxyAKhzHkcuJ3w8UBng901O0FOltF7CpumAO7vi8b2quq%2BjFTQaDEwt61zcV08QKrjL1ZlNN8x1y3tidR6wwdCjGROcrlbC9SzI&X-Amz-Signature=bc4a18c56b7c1a049152ff8b7516b48d71eb74135805e4979f38fdca1c4c6c99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZPHIXHD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCICnnv0hkXnk4xMghfaGYATUeVWD%2FDpL2YqpPyseKSv8lAiBQ0PzRdQNYFDNopzUEyePub2oSvqYINAbzwKw1itmWRCr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMZwJE7bkouEmbAMywKtwDCrM2ihWepV0g1qLCTFFBeS6jxBSVPt2w7dUhgTEsv%2BTvgXnaGms%2Bo14UaYV%2BYw8ScswhX0JLit5kpbsIAiyo%2FGuSFZ0WvdUpUUlFaOG%2BKyne5qV4ylmSPpRiayrwLBwun%2Fi%2BsIgZ494uW%2Bo0rYxyDOrQwcemTZQWi9jaSgK5%2FJak%2FfuIatRuNMVfNwKDt8nPLieJJkpCFrY3BuqJnj8ZCudJA0vBhumnotiO3A701Z3uFRBuGReaWCSELa21vA9LaJly%2FCb2M6lstzHUiSxeGun431GREcR6A8puebJfNegHQ7v4YB6Pp2iy4ZudOqqJTqzEuJXZzWvRXdr0dLTLBfZ%2B5mIUqLQRyF8GrrcYCbr53yFP8X%2FTm2jtTXMU83gOc6vHQ8H2Z%2F%2FhDwVGb0%2FJgoGB1qFl5944NOm5wCVKxjAXENWJdPXRTHXjYzoMMsSGWdnK6M6D5f7Ap4iKjav8ozCTBXq%2FGV4xxaub4NUIZ%2FB3fJWzqTGTqFh1zl0dxBqTsgfzdPjjsg%2B5UeTGeyRJ1cw6E5TJv9WWcZopGoMvPPMDNxChb35iJ0O1ykNVr5u3CVgX9XI6f%2BD5%2FmLRqfKavn02Z7r44TaZsKKwo4IAadEvOez4PKxEKAj5WRgwwfuTvQY6pgHrW%2B5FVq8fRVx2bNiIb3HFAwZqvxqA9soqYcLyjAwcxqaMEA7mjfQapy0eJ%2Bo3vcIwSYqUTZGbdAfRRDNFtk7q%2FJjly7CBdFwPZm87ei6NpZondp4KJbs2ar1k27NCryiB2ryaAdR1YdT7Pl4iYDrNr%2FauSlSio5ePQAFLH7UQvX0hF%2BReRIPmZu44LCd7uU10X%2FQ68MZ75k8FA8eEAQtMFZCmK4FG&X-Amz-Signature=4cb3580de7744d4084cac9fc10a47e283a0ba69d6262c67034aedb90b7a239be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GMW2VKC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJFMEMCHw03y%2BUAlgzV6uWGRGcds4P6HHJ7i%2BKpm1PSST%2BWfHoCIGUzlxWDWlTRgXzgjLocsXyYZE8iPjb%2FS90g6X7PMN2AKv8DCGMQABoMNjM3NDIzMTgzODA1IgxUwQ3GZspHHOjcsqsq3ANsRdlQ6ZGp6g2IERsDgQuniWDF28sEWM2y5TJ%2FKr3H2v2Lg3gBRDtEIT%2FDCzmuvodqiueLlnVRFsxuxrEtzup7ba3QseqXuBeKUVEa5TMyMdgDVgowVPNDRkb8JIGw76nsolSTniZjEz4%2F23sK%2FD1fdTTLjRFYgbxCSy34hZMpkVG0h8oB0T%2B90dr%2FY%2BrnazVk9%2BsI96tC2WC5jI1%2FthsN4cGNJ%2FxGuM13n19PVJGlBf4%2Ft%2FQLhq%2FWQYrHSq%2BwlCfqfAy5q%2F%2BZmnSbZ3Ph5%2FWftdzBOd%2FDFpxM57wRlyhoob7nxKaedruGXR2ie8bEAop3PwXSpku8lNvM2KguEEpGkH5EGgA2rj%2FOITkIU5IT90Rwyx3F7%2BuXO3WUrQomHgqopUMTpkTj7aVRFeurQjaN1ip29gDta%2BYQtREXtaQbSSPhwlT1EQdcQBVWkxGjvzu7AQlf1ODtd5PgagOARF9Oww%2FYYkd1GF2OOHxZMM6hNk4Fris3p1GOZrVva0RS%2FJztYP8yHMQDP%2BL35MIOCHvJqKCIeDt4DGvU5Q%2FfrTJY1Qy4nWnkQsjVm1siRM81wpyyLU1bUOIV%2BTGsuGcsP6oWjSAeevfMrHMEfIMkkgczGF%2BvjaoDfolFdAdHRzDD%2B5O9BjqnASfRJoABQQQbu7PO0LGusLdPQlYhSxCGwrGwvQVXdGltZfZDQtge7KpLPV%2BnCHqxKOfziXPp5ZSeMrGiRHCeGHVpMeaXUwmmeE4F0JCbHHzvhKIOYicLr5FvBwse%2BgnwXbxQe5xoL%2Fb%2BxF%2Fi952FfF1dkTfJZP6rZwEo96%2FZCUjW8sLB6lXUAwvxI0Td0Te6pSLOC62ctrCJ8XdaZBLAX9hXt%2F%2F1A2F0&X-Amz-Signature=65ce65c4303ff010bc9b9767ab6aabd614553eb2c9ac5cbd186f84712b27f66d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GMW2VKC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJFMEMCHw03y%2BUAlgzV6uWGRGcds4P6HHJ7i%2BKpm1PSST%2BWfHoCIGUzlxWDWlTRgXzgjLocsXyYZE8iPjb%2FS90g6X7PMN2AKv8DCGMQABoMNjM3NDIzMTgzODA1IgxUwQ3GZspHHOjcsqsq3ANsRdlQ6ZGp6g2IERsDgQuniWDF28sEWM2y5TJ%2FKr3H2v2Lg3gBRDtEIT%2FDCzmuvodqiueLlnVRFsxuxrEtzup7ba3QseqXuBeKUVEa5TMyMdgDVgowVPNDRkb8JIGw76nsolSTniZjEz4%2F23sK%2FD1fdTTLjRFYgbxCSy34hZMpkVG0h8oB0T%2B90dr%2FY%2BrnazVk9%2BsI96tC2WC5jI1%2FthsN4cGNJ%2FxGuM13n19PVJGlBf4%2Ft%2FQLhq%2FWQYrHSq%2BwlCfqfAy5q%2F%2BZmnSbZ3Ph5%2FWftdzBOd%2FDFpxM57wRlyhoob7nxKaedruGXR2ie8bEAop3PwXSpku8lNvM2KguEEpGkH5EGgA2rj%2FOITkIU5IT90Rwyx3F7%2BuXO3WUrQomHgqopUMTpkTj7aVRFeurQjaN1ip29gDta%2BYQtREXtaQbSSPhwlT1EQdcQBVWkxGjvzu7AQlf1ODtd5PgagOARF9Oww%2FYYkd1GF2OOHxZMM6hNk4Fris3p1GOZrVva0RS%2FJztYP8yHMQDP%2BL35MIOCHvJqKCIeDt4DGvU5Q%2FfrTJY1Qy4nWnkQsjVm1siRM81wpyyLU1bUOIV%2BTGsuGcsP6oWjSAeevfMrHMEfIMkkgczGF%2BvjaoDfolFdAdHRzDD%2B5O9BjqnASfRJoABQQQbu7PO0LGusLdPQlYhSxCGwrGwvQVXdGltZfZDQtge7KpLPV%2BnCHqxKOfziXPp5ZSeMrGiRHCeGHVpMeaXUwmmeE4F0JCbHHzvhKIOYicLr5FvBwse%2BgnwXbxQe5xoL%2Fb%2BxF%2Fi952FfF1dkTfJZP6rZwEo96%2FZCUjW8sLB6lXUAwvxI0Td0Te6pSLOC62ctrCJ8XdaZBLAX9hXt%2F%2F1A2F0&X-Amz-Signature=7dac79e0eee2636d751d423c514c48d2274edd0ac95650779e86b5929dfc36a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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