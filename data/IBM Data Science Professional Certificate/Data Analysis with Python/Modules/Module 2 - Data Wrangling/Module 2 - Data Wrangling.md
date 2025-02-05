

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQLLWXKG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIGqvL4OKAWefPYFZ%2BGIJe61xLAGpaROmxqo7gcTfGNydAiAiVtZrrtukCf%2BOVOcmvdtue2Z3OykaTq6CqSIsQstmCyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMp4eqaVKKtL1vlCyTKtwDBlK7RPuIUiPU9Kb4T%2BccKvg0rdWBy0mluwjsZ3witR%2BhlhpRKxFjRdR1s7D%2BS5GW7V6ZeHIuOrEGRJEkyJAdAq7pi495%2FyC5t0BG2mGFTmmZlgadtyLhrZCeQdzr5BC8AIuxbqS%2Bu%2BilpDscWTGfyXoTgCW%2BWiMUZ6UwTBwpldstcZHnX0afaW%2FwWJcMNqGPd8lpE2f3EOkw1%2FV5Ang45O96nmUZM57Qvf8TanOIIZBGv48NzKGgCtbV2C9BOt%2FclPuj1w2dgPuWLPPAtSERL%2BhVOlUItV9n8SL9K8Oub8VUpgPg68l%2B%2Bp2EBmhsADzDsMj6kIKrjngZe9wOskamyrk9AtzD%2FFccktdpAgfqsz7R4ZGUj61hab9KtmnMCkYoUE6b5sx9y4mOc7SjjHXLgjnbYFZe2Hx%2FiJf5V3ZH5abRBp4ZJCZ9%2BS3PaQKhPIEkqb0TrnEpPdHfNlSbesMCsCZTiEfIcvmYziUckAZzCawp7QR6gVWzTt1rUp6zL8EQWr027uu5AuzS30KEQH74AB8RnbGq6%2FuuXDu0UB36%2BPQucOGD1jUiebOJCvH4K9D2NQOiBNosPwig1o75fbYRMyT84GXXhWl8317SVQ1lZ4q0vtBhuDIqu9KN7hswuLqOvQY6pgHjDlwhCevbiaz7Y82xnEhWPQP4z5FDnB50Nh1WwYr0YPW3IE%2FJVYScFiYBwUVpFt5qx%2FJaa8zvZs91t3WvnIacRPI%2B1USFKfNcDVQIprGlC71NG5P6%2FTTBe6bYATFd%2BVDB4R9GVjMYBZ59%2FfX4X7OSlfy4GM5AQDtkOXhkqJI9xBpabyoS4ixz7TkkCGrtldHSlYcdk1cXItodGZNXtmIQggRdWN8S&X-Amz-Signature=a13e2210cdd9c56f991fbe8ccc38a0a52b5d72f0c3373e184bfd8eaefdbf8da1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVWF2UJS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCICod4BPsm1Z3RUv%2FHxdSZtlfL8NfXvEAcOATOVXIGIeRAiAkTE35D9X0Rp3wsK4hE%2BJMuf1jRHIkmK75p9B9n7qlRCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMhDsA%2F9Xl1CJZttJTKtwDgkZADWChG4%2BLVCkxvTr3c33DEvABvbht3dTw08%2Fai%2FTSyY7K4F2T8DPETD2fqIOSj2UU1IrhPeL1f8EF%2Fl95Wgm%2Fin7GEQCwKTIU9wbZSTg32OuzEKTJyxO2gSmo%2FKXcK5QXwQ23ahFWl3vGY1LkI40dTBdCXg9pzZcBg5dRflu79lAlAvMyJowyNfdNjiuHrV4lEddydGaD6A7iGzoubyoHDoQGNIcdMp5GL%2BukI2bMOw4BEeoQFY4YCklnH%2FRledYpmeLDRuzP6nWRg%2B4TJYlAaotI5gCYbu%2FHYTQvPEIKROQPWjlS%2B6SlYakIW2WTe57luSdT2JZloM7ANETYYKyNkWLmYkdd9xJY3sQVcH%2FpZYmiw3UeiL1QdOAVdD9KEeyZXX29Zjl7DVh76EEvKlm%2F3Hk4%2FLrK4hmoYt%2Bytsr5%2BAFTNizzvm5ThIQOCb%2FoORLgyNF3I4PqtBEk%2BRKrhlDOxcdrCNpSOLm5zLbTE5TQgL9bqZ0%2FCIC9H50SAspN5CC4gYK6zcWhlCc6o3%2FErJ2lpiKdwpfU4nOtBgm%2Fg1x9PVVBKq73%2B%2B1C6OcqK68mrKFDr5qOmZmNFqXeop6BB0VgeWQhHEkleHeR6LCs4DVf09m6HBgTQEGOTj8wg7yOvQY6pgHSXp5bt%2FsPle5Lne9hk7ho%2F8U%2ByMjDR7XjgB%2FdJilh0Aw6DNX58YtOm7Hea4huCRy8WzSZSmf4k64MX%2BnrYf4qNikBUAh%2F2s%2FRGT4cehRcYakzPs9LllQfCAYsGtWgtVsq5PeTrhPqenWlJCgQzDuYSXTQLeg0hTkPrC5juU1q8bA9BZ213elc1I035Uyq9t%2BO%2BjCEqu8LKVN7DP258sMZ61n6fap1&X-Amz-Signature=bf01749ff1ab2b872acc434ff6bbda10e3001dd6dd2939001a193ce2a000790c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627QKJLT3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHd4LicBrO7QYOTJFRp%2BBttfy9Li%2FBMdGmRw6jfBiKGQAiA4HSQLrfINLa5p3h0dEGmisv6mgfcf%2F1rHTiYCWse%2BVSr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMTtOTDNGFf8%2B1kK%2FqKtwDO7YE6z4SBhXAfGb4KrF5iHSTEznJRZVdWoHYB0kTfz3SZyymGuB%2FxyrVgj9q2TV23h9XkojAi3Rm6MgQZhaFfvAcRGWu0JJj%2FMq02tsRypO6BB%2FbXZi%2BpF5eRnCCsnyeKr%2FluSPA3lK2NUxlhRuWmwZdWgmfBCkmq4s8C%2F7TCh2MyfKmRcFiDZfKvc9lAz1oM3erHk0s%2FfXuPiT9Lp%2BvKOgW0fAV6P0A6hmoI9mh6SjlCWgszcbEKAHXqjl%2F6qsNs9meA%2FQPXL028PYSuScsalo8TWKaZLjqnhsHQejk%2FRE9p7621lSJf4mj18Bn64ftyzt8I7aCK6BqitJY9I1GQRCreG%2BcIXd8S%2B21zZxrZdFMMkmOvfQcIiP6sqOk70xVCPfC%2B48zBm%2BU5hd%2FuuvTcWpr6vvdI0jh%2FDlm4qMZEevKG9MsXVMBIMbGsi%2BeErtx%2B2ttxuHp84DvG17gMU3enKg%2F9KCjWDeAOo32jaqEnzfjfBIvUZ0MvRUzjxupQt3o8JHwoQb12wf9HnfY3Sch0ghmSh0QyC%2FxP78%2FGsLNPtfDUT8NQNM2txnVOj6dLGOtQuGWq6%2FyDMGSqMdreG9ZDWKC2IyulfYGhRjMlzvNMYVaUY6D%2FIWZHO6mEYQw1LqOvQY6pgHqwKpWCBd6UraiCg75fzPA5Tt7S%2FbAL2w6JVR165ZrPg9vVTKP9MQiDDYn%2BCz%2BCHRL%2BN0hSMHS%2F94%2FtwXfVZFmR6cjroU0yVoZPb4DGmiakPVA3R7JFZ7ANMwycUlNWp6DtzqC%2BcA5wnakbPSXT010Pu%2Bx6HnGRUfloKGgVaCBCc%2BoPoajiyCyO4AxHLci686e4P4DgR%2BEeu7uON%2BDC8%2BfWyiurtIh&X-Amz-Signature=b804164a00796d3ca28c848e4801fecb9054b68aeb55999243362942e7d52889&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIDIHLDB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCICE1DiV%2FSR5nf5LHG55V76A8wQDI7%2FXMDFU0b0F1MoHfAiAPYr8njBrJgNp%2BhiAGLREXt2S3CBLo%2BgwbqfsAnxECcir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMSRDG%2FHCrZ3CKnHewKtwDxfZjwipHWhf6uxWgNWTfJ9utpreI%2BD3Aaa4wYTvwNIxF%2F%2FQMLGjnuli4pI1gPczFCOwzOCYbxGx2GkbrlboNhn4O%2F6fVBLYPzCWK0ajQiIFKTr7tJOODzJSWaycymcBqNC5dHs4akD9mSYJ5S3J6PCM%2FImJWNrl9eIDgjJc1ZRjkUx3dl8BJyxmnXqahnWWSVqsZAaM1vHnU0jKcs1S1c%2FF03XQESIEqRzhi%2B89Vf%2BZyNbr1sD6ofYYUFICYvNtbYJlrKOkVlZ7vDbQaAq6PIKUjqcsUTtzPdQjzcpYTO%2BgfjZLxY3TKpCF%2BzxQZpTESaDCuLkkmZ9mDTO0M8nEoIH07TMih90LjKMnr7VkY%2BX07PNU24w0BGB%2BLKZFzKEhUaFz3oPNMCDlSFBMrT%2B4uehBSpxytJK4hcgzoVQ7kOGYTBuX%2F9dEbTJ%2FhxQ2%2B0Uzj1s00Y4x%2F50Wga%2Fpryyz9a%2Fup4G%2FQmap2RR4%2BstCvuXhCCJBUctXmfIMv%2B2jaI%2FmI3BYHsrtzKN%2FgUW4Wl9ehgHWrpHK4tzntvE758y7WKNuPfnxbDGKkuNYHQ9%2FB3IEcwicVRlnvtB5BesmiTJVKO1XODMcEQgiC9%2F6Oqt%2B42ptPy8BvG7OWpf8ul6YwnLqOvQY6pgH3wSKeaM4TDD3nRGwJ2XMZD1DS3CrSeqrg9Ipm%2FD1O8C%2Bt4BfpF7TmJ5Daw2RismeOjnmcsOWCwDnHY2vyS0%2FA0COZ4eD7evLzbA8L9flpWP4C26cUMKSd0bqr8CjCzo02j3pR5glLtKOIRJiRekF2yeZbW8CDdzDHhrniFu8PQHR4DtXAfCnZvK6mJIAy%2BcsVXuGRw%2FqAWwEE5euIDB5KRH%2BG1PMU&X-Amz-Signature=758bdd15790f47fcf578d5324a7ec42b9174a886b9b8114255d878550b3fa568&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VVYPHOW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQC8obT06eW6uXGbbwewTtuT5cg0Jp5Er%2F15hQfj8fIg6gIgd2XQ1t%2FHvrOnUWSTHEzS0WKhdgngVRBqQ19LsTuiRXoq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLQDY2Mj1dNLKJcuYyrcA%2BHrie293eJ1%2FyWoYm2t9rpnoyqNnapVJPhks7yALogtBYO%2B2hPDSny4EA%2BgoU%2BQ3mStoi3i4%2FgeW0Cby%2F9GMaux4LkJApYtJ1D%2BOAygUswwGB0OYa8H0g4aXss5zdGc0SHSone0pSUpK%2BmH0DU%2BjeHEzHlprmIX%2Fo%2FSHEn%2BKxYFGvH2Ub90slL55m3FANzH7cA0YC%2FCqRdEHYt%2FIKRvdojS3nvO%2FCwj%2FYOQGhGeS5t0%2FaOg05OBMDxYDhL4lT1szEPOeBofBjmlSoaU7kg4PNU3IiaJu8GZhN5xt0SUQfm9Q%2F%2BZ5fgfsYW%2F%2FKUmBOPIW6iEzeL3tnsAZ769eIfFOIpPBHi8WwFGvHBZk0XVpH0GsQaA3qqUID2F9ryYc520aKwh8Odb2gjjETlDCVxVHBlxqaJETJX%2FeXAyQdxs7WNHDkq%2F%2Bf7UdsHeFEcSjhka1gAvSIvg%2B6Hf6eH6wUMqHXOaeDgjs50q1Gz9dOWeMM1%2FrWnCcTj%2F3luB%2FDNyXvxyb25nOgItNqXDM5JaX%2FsJndIQaJGGN4%2Bz5qLX1C6e4JGMF5Owye%2FawJykAIOvsSFVtu9s6pjPApref3ZOys2Q6wWRwaqRSooCKCf3qFCyJOnH%2FLHOqnGG4vWVIuBdMMu6jr0GOqUBSXxRl5Pg20Yhh1AcKrhrxoWWmOFcnyNnAwc%2BEWSGxsEByV2wnBZ3ZFJD4i71dj%2Fwu2ee5kLMQXWN9Goa51c4UzTzb8i6UVhIhqKsVHyEdnp7g2lRYcR%2Fijwo%2Bh%2F4IFhzJCTq12MqL9%2BSxn10PmS4LR3p41yg7Tpz7TjMFPr40HPS4XJoUzXc6Mje8wvPeGfVRNEH7jcSNykPxNzNQrwcqwpV5H0R&X-Amz-Signature=549a9d6dbb1fa6380c5dc8b6dab0a48af90b2e109b53a5b013cc5f80b9fc0f59&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWHPKYPL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBRlu5CoeFWHZRLwwEqwvdbO%2Bh0u1cXYkSEvl8%2Ba27lUAiBMhWtAmjsrz3Hu8qY7i4qvI%2F1SSEZYbpTe38ao2z86Gir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMQ3YRCQyD1ZtTb8fKKtwDRVG7lKoG88%2FrnlHie%2BwBNeu3Io3%2B9VVshE4gzKFbaFnHnDIUA4rJf4kGY63CD8uNWmdbTWPcgWh4yCtKOUmjzdDN6qPE18%2FyhhNQv1SxDEMDQhzwRMVs99S0VEcwrE2rzvWeH%2BxqWl5rkqXfpk4VDrxownRtwQGi1RTbzjWYGXDU1q6baQd28NQ5WTxtECESrUpiRV9ZRKi7sotXd7%2B4tm%2Bh0TivJXITivd13hleNbA6t87Cv6MqvWX%2FqdvB3EvfaV4UO9RBc%2FOP5INPf5wda7Me2SxfdLptDd95CqNrWB6rL%2BybPMf4FNLnubgKnRr%2FaJXZz9omFvjl2lI%2FFcazQv%2FpB0a14XsuoeF8jWF2pbopSjPpn%2BuBq185BzYFDJgx0ReqES5acYCC1dQ9bBilOBKA35yjv8xRzsTrtqqj%2FpsFGWz4feJJEYvEVQmuT7%2BPzme1t8fP8s46vBTtaPSaJo9QJa2UVAf6XQv6Vn8AWDzTCf9a%2F%2FnNFo1T51qvLl06HccmQm9gThzWCRxgIkr8PSS5JuCyvsAozFphefnQnz%2BZ1UROSqFcvfd93fOqqK%2BqdCT35Rd4d399EjRm3emeyX7Uyyh1hOvjGXGtnAfVHPqz0Opez7HxA1%2F%2BCVcwmrqOvQY6pgFuAiEPI1Lc9WTmnuvjYHz0BIwDbebbTi6ZL1u9%2B0D3S7AInhVde179BTnnGkrqlEGdnxCQGq7Yrw0J2PR8iDb%2FpuVOerwp1phrxpRagVPpF6%2BECIpMSq5HpztJ%2FuFrleUidL61qPzZ2keTVuNeI965SWXuUgbAS1OxgVDV9emdGPZ07UsKZmCpPnGzsFljZJ15CzT7FhW7jf3I%2FseimS16czwBDZIT&X-Amz-Signature=433b87b40abf090898c912dd8ab497624aceab175d930adc8a64ebf3208cc8b2&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JK6UVLU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQC09gv3SrOFkcC2qKP5Lu06qH6FJpv0T7GRLtASoWXSWgIgLYOkSaBh3l%2BRMgvO2EipN12D9kaFTR77OPIk8JVrNvEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBdz9xW5o%2Ffs0tAOTyrcA%2BWiyO%2FgMJ97iO6jV6q02hxc1ICV7AWVNo4kTv9pJetK78Okc9ywyEYHcA1bTsx2K6s4YPGF1drtGuxaoilAVw9moq8hmSlQhx%2FXCSoa0J5gpX%2F5RTgeGCcP7wCXM6VdEqutB2yIR%2FFsGNf%2Fv6560BH4VrcQs8%2FDwxAhRKq4Dszdxvn5cyT4QU%2BECBL2D4L7wfKdTt5UM7zkLvfIld6scwy2AnQETlQO8DUML677DxdZ%2FnGzeGUiFTr%2BLPi3rmWv53nKBk9vHJpSKm%2BQge5s3%2F2RjEEsywYdnJZBkJAxBBWPrtDerBN0m1VBAgz%2FcL2oGwgwvSpCWYqxvt2%2F4ViYgBTyvIYXDYc9Cpj%2FETe1MSigZUxWvDGmVag4WGsK4ALZlFV8TsinPBSTNVPgj9ulW3nZtswD9oIE%2Fi7UULv2cyZrZDyeUU4OAeSRjTChRw%2BCyuZwrPGYGszY%2BeGxwlzKU2xrUDdxzviA5Q8QRQkako8d8ECZvi6lU0Lp5iDpNobVLRkb%2B8U0u23uvUlWVOym2lHbKKCmrqkZsGfSJ3gYFdj94IdqFx3SzXaAxi%2FygClJp8SzoP29zwRSjnwwBzSzvijkiYQhtJjOiaFoPRLxDgiAa9OmYt2TSM1rZlKQMKy7jr0GOqUBTAnKDyvrx82F%2FTqGj9SPOI6xIBRyAqoWlFwDBokukbcT%2BWLDqf8HB1G65jox1PuJIf7Kq4Y2BpmfRBsUxNUb%2B1tIQIm0smPPKLWcGVYfbjPQrXe1OI5G34TGKZyWkDMMVty7qrHcp246hGRep%2BsmxzdX7Ft0P0A5pfsiACgCehoCzJmR02Gi3%2Bix%2BEHukjxDm7zRf%2BC2h1%2BZ5FOqEqUilwWd5Ma2&X-Amz-Signature=ebed794c4edd2ea0e2550b4291be0cd06d3155112c4ab2793362147e5502ca13&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675W5H66M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGn6I5idptX%2FYOi4r7Ix%2F8mtL20KD1baLkTuIVIgmmecAiBv6lpZxsTCHwBM7z9iveuPc6Yc7t7SJ6KzSHYzY0jj8Sr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM0PAkTkfrVvoon2NUKtwDKzEHmI%2B2zq6nqmqkc2Q2ckBmjllFYr2Z3YOFFIqORtRdT1ooiZO%2BAGOE2pUbOeTTRzpDnCH30MUEGgdCIz4KBSxpGF%2F95JgB7W2V%2FmtdkDR89ssMJyY5%2B7aAwHVTfAfjr4%2FMlUkkAc%2BpIeQSgdFKvpoZ69Jn1v9nZVXe9%2FLrXLbzcIUNX%2FDRC%2FR4ZfUbZfL8PP7KmgQ6Z5ybgO7PpMyuSkZEoEycskvJ9q9rXmbGgPC2rVrahsto7nUcuodV7AKeg4TQFv9tKelFHmrsYmDpRyYfYq05MFG6y14do6z2MGefuMXOL2XdjbNw7xQn3fyAI2HZIDhNvDGWVJFWOKIGbcItrO%2FQ2TQiLT2BGzom3bLqNZma1iJDgMPpr7aTfk34BOhWfgk91Be9dee2k0uILxfnZTg5KyUYli3qhNrgtxoKTWo4qBPA2bmF0d%2FA%2FejzXt66RnKbBFoWS90EUKeE%2Bqu3O7GCH%2Bi%2BgOp0nygIaQdEPsOY6K5Ei%2F%2Bld78wExeT60xojeF4pVpFyIQx%2BsKkplvrDHd9F2P9qNSQCj0aTjPGIvxAeEOjeZrmujfdCzo21VxSilWukozNeRbILERTUKL7vjldadYhQCylQyRMAFCnxwXz%2B4mVmQfXGgow57qOvQY6pgHJQhF%2FeolbK0UjsBxdZhltqSufANFKazyaIjliC8QpBm8xk7eP%2BKBsgceNcm4S0bWCsXIr%2FybB16oY9oduyyWxuGRx7s5FOkI2byhJ0sSJ1%2FbkWfChrT9bQg7o3frVqeREMn71OaQUszD%2BHzPx3eWcMtOzRrt940qN38Cd%2FskiUxHDhYEFa6GVfKEoEGOBh8s1WP%2FCNn3C0EcZ9yERHvtzNC8Js2Uk&X-Amz-Signature=49d7be08d08239fdb5db6d512efd99f6c74a74d31067ebc80d4af8b1a17932d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VVYPHOW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQC8obT06eW6uXGbbwewTtuT5cg0Jp5Er%2F15hQfj8fIg6gIgd2XQ1t%2FHvrOnUWSTHEzS0WKhdgngVRBqQ19LsTuiRXoq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLQDY2Mj1dNLKJcuYyrcA%2BHrie293eJ1%2FyWoYm2t9rpnoyqNnapVJPhks7yALogtBYO%2B2hPDSny4EA%2BgoU%2BQ3mStoi3i4%2FgeW0Cby%2F9GMaux4LkJApYtJ1D%2BOAygUswwGB0OYa8H0g4aXss5zdGc0SHSone0pSUpK%2BmH0DU%2BjeHEzHlprmIX%2Fo%2FSHEn%2BKxYFGvH2Ub90slL55m3FANzH7cA0YC%2FCqRdEHYt%2FIKRvdojS3nvO%2FCwj%2FYOQGhGeS5t0%2FaOg05OBMDxYDhL4lT1szEPOeBofBjmlSoaU7kg4PNU3IiaJu8GZhN5xt0SUQfm9Q%2F%2BZ5fgfsYW%2F%2FKUmBOPIW6iEzeL3tnsAZ769eIfFOIpPBHi8WwFGvHBZk0XVpH0GsQaA3qqUID2F9ryYc520aKwh8Odb2gjjETlDCVxVHBlxqaJETJX%2FeXAyQdxs7WNHDkq%2F%2Bf7UdsHeFEcSjhka1gAvSIvg%2B6Hf6eH6wUMqHXOaeDgjs50q1Gz9dOWeMM1%2FrWnCcTj%2F3luB%2FDNyXvxyb25nOgItNqXDM5JaX%2FsJndIQaJGGN4%2Bz5qLX1C6e4JGMF5Owye%2FawJykAIOvsSFVtu9s6pjPApref3ZOys2Q6wWRwaqRSooCKCf3qFCyJOnH%2FLHOqnGG4vWVIuBdMMu6jr0GOqUBSXxRl5Pg20Yhh1AcKrhrxoWWmOFcnyNnAwc%2BEWSGxsEByV2wnBZ3ZFJD4i71dj%2Fwu2ee5kLMQXWN9Goa51c4UzTzb8i6UVhIhqKsVHyEdnp7g2lRYcR%2Fijwo%2Bh%2F4IFhzJCTq12MqL9%2BSxn10PmS4LR3p41yg7Tpz7TjMFPr40HPS4XJoUzXc6Mje8wvPeGfVRNEH7jcSNykPxNzNQrwcqwpV5H0R&X-Amz-Signature=bd6cce9bb2d4edbd23836e0e49cfcb63307d25b771433fb5e324948926f97fcf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GT4GAOU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDfZOKxw8rmyptFfxMDbsWQL3zhC1RaSI7atKCq%2B%2FaI8AIhAJpsFViUVFeZ58LSX%2F6gKzFGByAfGbUkYYee9S%2FelCC6Kv8DCEoQABoMNjM3NDIzMTgzODA1IgzeZwD6D9iyh6gToKkq3APqZPEMIW9jT9V8PNjmRbk%2FOTrSI7BfzPcSX5M9vP37%2Fn6S9JDRgdFY5S6axcmmrATdufFDXEfbl8iZbJLbUxZOaCbN3Yl2o56fDEIQucdyl%2FzA7gow5iArWk6z33LRF5NaOn4NGL7tjdEwTGDvIgzOh%2F%2BNnP7j2uqb%2FiZT15E0bzkOtlEvpT7lv5VWBW3X7qDt5CS0gGG34BWMjm%2BZ0I%2FimuGEUaEQCltVEDMKgPq%2BGkT4R5FHJ0713nbSbQLLI4AJuHBgI74wZrCUw7Rod%2Bo8QwNhXNQOryqjRBwhEgPKgQMbe5Fh%2BLSNA%2FmbQaDgQkvjNhbRBYY1FRgI%2Bdwpi8KHVvlq%2FFbn1EIrHDTs0hwXH1Y83VkFbGPXSj5xrMm8MbOiwGlZHFoHd%2FlfpnmWCZBFJ%2FlLaUgcq0jdc0KmO5yAnmVe%2BDhF8VEyFQ9aPm%2BCBxCeyNfdKvtpEd0622Ay%2BGscUBXc6xQMNYdGTZ5BNEP%2Fui4Huv4lrMkpq4RlXQD30fIR85kZhwebf4j8dD3l1TNm8ln1m1%2Fa6g09wiNsntXPwzJ3pnbwYx677sUl0AdQ%2FVw3JRnoruXb3i0ZDI3Bw3YUmwMTduay4uASHakb2JM%2Bh7nCaixbs8KnDCmAGjDNuo69BjqkAcLsTC99FilyD6LxK%2BEi01mk5fRBFLEazRIkpFLhn09xZYLqc2Sb37gH3zfNdl1g56EoqMXcGWEaxdSJcTANSTaGxztN3YJw4HYCyPm6DZInA9jk4rAsbLSp2lXPwswUqp65xuCgY1PU822g10gRmHFs9VY6nZhgm3bAzop4ZNglSBb4DW8EsFQu%2Bj2LDGyQHKBjgum0lkmok2LYikJIE3IiSL%2FC&X-Amz-Signature=219b945d0dc39abdb9534749f2179e544e72d977d0b8aa8d90953b798043ec68&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GT4GAOU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDfZOKxw8rmyptFfxMDbsWQL3zhC1RaSI7atKCq%2B%2FaI8AIhAJpsFViUVFeZ58LSX%2F6gKzFGByAfGbUkYYee9S%2FelCC6Kv8DCEoQABoMNjM3NDIzMTgzODA1IgzeZwD6D9iyh6gToKkq3APqZPEMIW9jT9V8PNjmRbk%2FOTrSI7BfzPcSX5M9vP37%2Fn6S9JDRgdFY5S6axcmmrATdufFDXEfbl8iZbJLbUxZOaCbN3Yl2o56fDEIQucdyl%2FzA7gow5iArWk6z33LRF5NaOn4NGL7tjdEwTGDvIgzOh%2F%2BNnP7j2uqb%2FiZT15E0bzkOtlEvpT7lv5VWBW3X7qDt5CS0gGG34BWMjm%2BZ0I%2FimuGEUaEQCltVEDMKgPq%2BGkT4R5FHJ0713nbSbQLLI4AJuHBgI74wZrCUw7Rod%2Bo8QwNhXNQOryqjRBwhEgPKgQMbe5Fh%2BLSNA%2FmbQaDgQkvjNhbRBYY1FRgI%2Bdwpi8KHVvlq%2FFbn1EIrHDTs0hwXH1Y83VkFbGPXSj5xrMm8MbOiwGlZHFoHd%2FlfpnmWCZBFJ%2FlLaUgcq0jdc0KmO5yAnmVe%2BDhF8VEyFQ9aPm%2BCBxCeyNfdKvtpEd0622Ay%2BGscUBXc6xQMNYdGTZ5BNEP%2Fui4Huv4lrMkpq4RlXQD30fIR85kZhwebf4j8dD3l1TNm8ln1m1%2Fa6g09wiNsntXPwzJ3pnbwYx677sUl0AdQ%2FVw3JRnoruXb3i0ZDI3Bw3YUmwMTduay4uASHakb2JM%2Bh7nCaixbs8KnDCmAGjDNuo69BjqkAcLsTC99FilyD6LxK%2BEi01mk5fRBFLEazRIkpFLhn09xZYLqc2Sb37gH3zfNdl1g56EoqMXcGWEaxdSJcTANSTaGxztN3YJw4HYCyPm6DZInA9jk4rAsbLSp2lXPwswUqp65xuCgY1PU822g10gRmHFs9VY6nZhgm3bAzop4ZNglSBb4DW8EsFQu%2Bj2LDGyQHKBjgum0lkmok2LYikJIE3IiSL%2FC&X-Amz-Signature=7588e6fe14e8673bb9aeb1b232fed760dea79c40ea5f7f7c1f4f717a013684db&X-Amz-SignedHeaders=host&x-id=GetObject)
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