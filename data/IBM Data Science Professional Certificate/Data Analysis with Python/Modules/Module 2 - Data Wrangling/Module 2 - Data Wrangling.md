

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SK3CI76E%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVpr0o0aKtJSbabRQvFo9oG%2FbWaNb6VnomOvF5a%2FlpcAiEAgWUeu%2BmUnwIeFJE4%2FTqcdFAf5ZSzrl523Gw0Rks18wkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDH6zX6Af2GQHBegMKSrcA%2Fbbwh916j0tKYhVgwUo7E%2Fqf3Y3w7DleleHS%2BuS1jsRDPY5RkqACV7lyIGYw0e6Y9TPAhNKqt9mXElAyF%2Bpbi8L8YtmL5k0U6vQ%2FF0AMVab2TN4l6R1Slakun7%2Bhx97UW6KOOy7ZueDUM9UFp%2BKqyO0NoVBIDiSBjDDXZF8Sx07whZsp74Bg8UX5%2BjseoQU8Sug3D2x3NSxcLwnEAjNAZaB%2FoXLC%2BxoET%2BTsBBhlhV1NXhb7NBeW%2BH7Sj0u905KDnmC%2BMeJwpyacOQdzvm3kVG9r77EQ1wssQMV4qnPPfn87YJFnIfDIU15Wg0P7TQkq0qx6Yr0l89DueIdv6F4pzjE1g%2BXR32Ra9pXrq4O%2BWqEGNPRrxhd3N0U7MK4j7y9QJkBqGFAyJxUtxvERXisFVwL%2FsX5BeCk0d3gcIR5vHnbFcEfDmioU3KFk59VNnkKIjy12VBCfDUoV9Kh6N6IUR%2Bsjh%2BZoenB5yv6D8D4SB4aPQrqpW9%2BV3rxIaqWnLVEamn5EQv2OdgdKP9gbOjLbiZbs8yxeYUDuoIFpNYC3OLeKS1435%2Fhds1JfdnGbts0rjZ0gDXC2shjWOSc%2BLvVBCXO%2BF34Yze9Gf0CADIRPhEo%2FWNdyc1wdC9ViY%2B2MJDzgb0GOqUBxSKTFLzMfBJ41fbPjBzcaNr1dkL9EcD77UzKzcyQWzX1FWLS52hOJjMZzY8MkQVd6m72XrALqOezc9BkByndYfPJ5V06Vr%2BmKCcIX8%2BRdBxOcB8uMUCFBl0i%2FI%2F6pqr7bn6JC7Bob5lHkq5B%2B7olCvo%2B8NrgEqryDVGO7Kkm5aEb%2FpvsUFNCNDOm46AzqzxW%2BfkeaRhN5DedjlGY%2Fliu8wGfmK9J&X-Amz-Signature=50fc37f7c08875f42732737b72bbdfbca6780d3c97557cd5b203490e1b97239b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYRX47BD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FghZB9WkA2GmpHR8wz0vfMhb2MntlhJkDFTaq5r%2FB1AiBTNeDaalaq2UYpNM6k0d%2B5Ip%2BSXj1hlYIMAOnoNY1tNir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMylu23z8JSdVzzMpaKtwDwu07%2FakSk6bi6eHFKLlGxfYZcrNoPYE5d3lkuguG%2Ffi%2BlPupRxNVUyeUtUQ5u73%2BF4056WRgiKg0SGFlK4eaDeOlBEFCN6gUDB3RcKcEwqc3El%2BHaVVDtoLuZZgMFMUZz%2FRQGnuBBTk4wJ7qqUTFgA7eCKdXTa6i58KdNFUheXTl%2FweFJvMWMv4uxZNV7GoKzMJcigzrFyFo%2FJ3nBxR2EKOKAXqBLmI7PRp6a85UQmd75Sg781z%2FBit5mxegHZqDwOkvM%2FpClVEQUpCi0SplnS%2FAObGQFPuduNZMhsGUJal1MzE2kC15FTQoa8cWZeOoC0Oq6bR5EHJW1zu105lkGiM%2B48sONnyDPBzgrW7gY5sOi%2B9G3f55fw1b%2FyrCB9XBkdrTA8sbKKDuOCS85P7U6j%2BzPHQ8YV9RCbdZqkOYafz6Ev6hy6KQUjmhjN46WcsCy7K1pMAOP79%2FmFeun8SYHIRMOQ3mAow%2B%2B1CFYQgCq2GI7%2FJ5B9FZfzT5sZdze%2BAi8Vh%2FjZ1bSlU2Y64bhn5LJcylZQC1ub99VpOdLeoPpCMk8AusTfOkwQFHaOB4Qyes1GKlmZM2fsry3aVbhDt1rWhVPYv935wXpbAqR%2FL9enC33qP5Js1j2gUJMKowtfOBvQY6pgG8ldSxANEXNASGYRjTm7orNT1QayOSys9dawCbDvCmI56Xo8JhhbKKD96aMnOA86I88Aw3zosqXm8XeguQItR%2FVEbcDXE6YuPbGlE6EBzA1rZwNXtdq01e%2FYqvaUrxYQhacptNV0iNBtR7zvnQQc4GoLsBOh26ofhJwFkB22Ek6XVUrNlMr27TBEu5UZLz9zCHbhhPPM4yA3Uo9n5mXvGmjzV9i6Fp&X-Amz-Signature=9578ddb489b9b15b10912a52b12d9a562bf38b86307018431e81d914dcbf9505&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X3WQCOY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcsqhg28ggTBhb30vK0nHAYuOBR1zn8SJWVZjhVvNx8gIhAKzRd7REFIpKJ5JwgW8PcnfxnRxV41GXYZYsUx5GJBxOKv8DCBEQABoMNjM3NDIzMTgzODA1IgyxZZ8MehN%2BXObC5uQq3AOrmTBstVpWT6gm%2FsnSgPiDWZR3hDdPr1dfi2ZJObgQ2S2oStY6IVjBaaIL0mhJRHiududse9iWuQlFJRPnVocwhn8bPaP5lCteogy2x2%2FmAOQwzUrLCKv0UM3xu7hgZ5cmRbbcbgN18qbr5MCmF%2FUpXr5ASLnlLACEaFHl6e7uarTGQQGDqNegWJIbW2dH7eBzYLSk%2FtywnXGPzqK%2BfrCar5SKQNY3Z0fx%2BQ7KK2ezZ%2BqUkQyG8Hb0fw3DFL%2Fkz6O5Qd%2FL4ulN8mkTQ1gENe4Pb3iLleXZlDeXX86pNsQnYRshYQQLBcCRBfyop0pOJe7hhl7y64VD83Ld9umYzdTmLNJuW1BEpvLBB9TqVIxOXBZFA1hXSjbAGiOzefXevO79jfTqAGphl6F5JU1SIQyZk3llrof7O7WlUhaA08G6VwQwQ8Oy6THBDDXhOHw75N2oxUh%2BwKYoCUKQYRz5y%2BSCHowYza2BeSRpGQ5OJzvear31L6zScopean7D11UPtsgKJrZDQspixK9jOrPo8vMmP0rn1rKHCvTfHGIzMBDUVcYnzYFWXDUIvTmIGosS3wKGPAZhecJrvJPdzaUfXXpxEwk%2BauBzdwUAVV%2B2eyVHvDlFZJYaLCO9xWo5ZzDv8oG9BjqkAafr3GitzmlvqA2WUfUDlbYyER2x8MHeRw91Ky8hFD5bDkLiczrBVT0EpqMVqiuhv5q3pb3ZhSKuBWoK1olEGV8GOgHH35Xr%2FNcCTHEl0%2BrR91M9g1rZnU%2FLila%2Bntj%2Bc%2FRCPG6qT0B5uLCA03cyxfdKmkAZFi6Uif3sgEPzx9DysF7%2BYwYchYOD3OJDPp%2BQTHsX3FKClXeYR1DSKpjnhXYnOFLd&X-Amz-Signature=a995cf143d9d32f686e6f5f153ef3ab9233c56b79a4a5c04d6f79fbe12d113de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3HMPQPY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAfSSSdYYyXZVVXDJZg3EIAH2dDPO%2F4bgqECPXAHk7aWAiBSTQJRX1ZnTmo2zfeT39xoyJdLEHuAj6ds9%2BfT9BT0KSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMOfyNmsst6aSUd3FgKtwDIel6gQpGEvbmA51XRzaS%2BAr6t4wnn8EdLDZUUIcg27acDs0qgQbzqOJK40SL%2BT16ym%2BwqlIH%2FqJCpXfTCmrujR1upue28wIHquqrbLKnPnDnCC%2BLiJ6XNbuBz3w7vGYKtYPd2QJuQqMCcSGeMVc%2BG9O3%2BFm4qEwOyb62ZmWRk6RMO3jIaRmF0onjlf8tP6e4HYdIIKhRCLVcqkxSbjJL6VTyYgE1ZzKlq%2BadWqiAk8r3OnUeXMBsPw0oXgWuAJ5JfdGY7ue7SJnNNiqGK6iSkDgNVjBTBY6nHNawbLrNxl5LmfA1r%2BPGF45U%2FhaabxyBd6NVpEm5t7sXK23jCaOYFV3HghGxiCIDiQKniu0Nw9JSkbkialPvUMV44S96pkqLTP4kyf%2FKFJxrRvo8Xg3ED%2BS5rdjdjnXbRaKmQbR9FY52NRTgF9JQOzxbvula2Dv46SH%2FmV7yx0wp%2B2Pad8Z%2BYkMOatkmYUXMDIqu0vC4h8q85h1HEHb%2FsvSOeDquxXqMH915AYaIKJ8AJYMHFvHJt2hq7SDta7KnCJGX%2BugoYHeFHwIk7gVAOMSZKBXrnN7M08O%2FDBPkJQm0izZPiGArrB7kto0gEDI5Q5MMkdlL2OxjEDGmnAL0dfO4Dm8w0%2FOBvQY6pgHOgD4iku3nQlKG%2Bw5tkMDzk3Oz6f29Bd8A0HJbi0Hw%2BDjuVjuEEjPnm83D6oRx0uFgkBm3OCo5hpkgSgIsaUXnZZTy1fMgW1jBa7DDBi9auRxI3xC299PV7QjC4DsXsypLDSBdMF1xdSDmctKk%2BdqTY3HvLo3GMCSJzAZ0ohjpecnca2ti%2FgBOfhdHT1Yen7S0EvAelrz2ng%2BZXiavoC3SL9ATdC80&X-Amz-Signature=08efa691b7c7fe75f566f5967fdf439cba3a1bcbdeb1e4621e9be0b0aff38f31&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKCEQD7T%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD67HhHBp2bQMIxbYtzXbjgTxXdmYgt3%2BzvqWOS1P908QIgbh9jGnuytwAKSYxKyEE6CSpufs6fRqhhbL%2BjkNZ6m3Iq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDF1cnLNNhIKr6FKGASrcA9i1ZWX89u4PHz1lC1vF8%2FMsIM%2FT3H5yt1B70DO56S5gWnflow7C5nz9lwLgW6kFP%2BSGZCpO2j%2Bfsjw8AhhjjsdkLt7owxf1FNQFRuNAc7DHgEoi3J9Kr3vzEM8H5Mo8Ve1sZZmYInBH8CW%2FWg1EHX%2BeEUsqAUp37MF%2FllbddBGmubR%2Fg5CpxrC1m8dodLS1GCHv%2Fu2qcTmunV28FZq%2B5H7sSXeJljpZgZPT6TGYPtEeByW80oqghklzFqGPIAqP3p1HVuMCKN8ZAR547XNaCMcvFJ%2FWS0uwX%2BR9Y6JZRgZsjELNG1NM2SzDSxJNsz0RHm6g0mY2vVH%2FhGW7nXLfwmCw337ouP6llsZvVshOUSvey0FpVl1nbl9nOC3cTJyzwppn7F7lfjww6SzcFLzgt1fMFfNhUmXvNOY%2B9WMU05uYABmrtm%2By8rWAb%2FzyzX68MtqW8DZlDAg%2B04MEGB3PvLB86SyOhA82%2F6wveU5Sp589VvQMQiIRXBegsFkaAtiATaiUoweZAxo%2BdSHEaQqNk3%2FoSjp4pmnwoaFEqCeYGST2Mp6w%2FaDeS0%2FCL3ZXgaba8UZAZN1g1Lac1HUDEeqYDteU%2BFdrWGkXeEtLyLrmCwRvLu%2Bn%2FLrYeF60azhkMObygb0GOqUB4INk25XMdR3BPjqleuaqwl1GfOAjI8hL%2BFE0BND3Cj%2BdhdSlKqU30VAq%2FaQ69h5Cr2ZwgfRvTAM012HXofg%2FXRFbdmX9GKZ0%2FqsJlHgq%2FYiDUZbJbeXGMegJGscWdEb9%2FVXGQNCr07A5uYXZ9I3L9PoELj8IciippvAtDvar90M28mRQksN0DKHYDexnffFzeddBlIAonCGiKT%2Bnpp3g1w3HGcLv&X-Amz-Signature=70c892d4678e0106dc3a878bf65b345116c3c1bd79d5bdf9d1575519b1a37b0e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LJBHLRW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGVM%2BfAgJ62YafBwJkdYhsKaGtfBIP6%2F7gOOY59S5E1AIhAIGjoUPb5z%2FbaqNx4oagAmrr%2Fvnva20UvOCSghkNkXUmKv8DCBEQABoMNjM3NDIzMTgzODA1IgwjGQ1g%2F%2BSY8A11Mf4q3AOLnKUz03G0KMRUJtbn37CStnjb322iziG3b2KcAocTIt6%2FKy6oyoyEczqSEjgZM4YTVtS2QMJU2O94ON9rja4%2FwhtzRqT6awemC9u9ujiBEXWwy4ZtUZy%2F7r9w9tSQcIuxawkVV5NoZOvk6FstTDUkpCHG0VxHQwJG1aEpJOqIL1%2F1gXLr40shvER5xiq%2BayuKlrQbLsC1mr3pgMB5AmOylfipPaDlWqwU1VLPv4LKLI7SjSIYTJI0ImwNse0mMljqSNjMGJcVGv0UHao7nNtYAN%2FbZwgpikVBO%2BdAPwDgvpKWkMIxlsvAQq%2B8Nj5luAN9gtF2Okb8XJIcKIV99Ej4zPWHWVg7p9rBsB6K9IQ78STbFMxIUCBC4fvvPbNR5AbYKETRCLPwLjsfIqseg04xcU7%2BFA1Q140qpiLIPYw09x1S1sEOKK9i%2BvKiOl0bu8xUfO90MpEg%2BlwGaXY9N5n5hoM3u4Yt9mXnZQ6LYVRIOi81lkINIzLzMFQGw%2BaD3oUd0AN6OHfYQ3PfAmkdY4yLCvgSg6sVFzXsOmuWLKMTfK0nQDML9tVFCLckVPt5AewJGkg7ScUUt9H7XLQc1fCzhhVrIDIW7Xqodzv0%2BgvSBvDFPOd0AY6RhaFTFDDn8oG9BjqkAeHUgeYEYQ1dN9ExJI6YA%2FrWctqAm%2FnuAl8Y51FpKfHg%2BRckOotne8Qn%2BRKikRqmIp5V8%2Fp6pyDSmYUvupyqvNu3Z1HzrefZfHI9WqJScb5TRNHRsyGmpoHujE%2B9MmHYAgRjZf%2BodLVOGS8dYgojOT1UD1S4jEyt92rzhbDBP2SFrDqx8ITDsGIYRV3%2FHWKanAnhFoTM7BxgWJTzIVA%2FKMlIGtH4&X-Amz-Signature=18e59bfab575d28f27c2d51e93aea4c4b63a58d92e4f1a699df13569596e88c1&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R57SRMYR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC5ETx9ElgIhiI7bCzu0dv15zDfuqT6ddE2YPRoOn%2FGZAiBmc7hIymVrn8GRqysiclR9AjQEWnH9Bi43qDIsQIIQCCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMn4FK6Hlywk04aU%2FhKtwDV6vHYbRZ%2FFYz%2FgXMNNz%2FDIXk%2BlUjX8JDESD16p5Q%2F2cCm3Qg6yUlMQEnCwm2BSg42yXJLEQ%2BgCHREBg1UNRP2wSRFdlGMSraI1%2Fg8YmRPeErpCUKuMZnv%2BXxjFAxNS8P9HPuEsFSbNenJeySf69BlB4xKUvjg%2FJ1p1BgyHVgWIrpjOvjvDqBJirIWhIHiqa2JQEa4qo4KwjwZkZmlJgFj9wTyzUddEINaO3NxPpftNR28Pi5EGOX%2BQP4uwLffsGKqVEP4y%2B0kV6aVtT210ZLlGNaC9D4kXRaNek2M7LhqwA7yWscxfPZGjd0av%2BubMN0VHfqMm%2F2tis20rTs3YL215lPB%2BIMtGMlKo8tHgA8ESrrg4nJatwAuvUTZnRVrwnA2u5n6Zzv4iViY2yXWQ08J7cOCvFyb8C0PKIxEmrQhgYGXAbykxGeS%2FzTnFHVJYBtCaPevQpnXefCrEstG78v63y8SXRt3%2BQtTS9YdMJWZvibuPcGHQEB1yjsXEPG9zfIrxUe69dh%2BLXz2m2l74ZBITwWIXU1c5ToILdFFH2F9SjxFo7pKx5MTS6AVgpzVh1CamgrNgfZGEyhmH6HhfUO6FgOyF98cj3G%2ByT76uMhJQxD0WgDj2R93TIxvhkwmPOBvQY6pgEW9QQKUM%2FnVwrKVe1cshNbdbLn7RWUJMbZ5tyZ5Mn0JaffwE6526%2BIvAGaZinBcBMYEaVKySRT6oc3MWg%2Fk8KbjrP0m5gJNdGjRy65Dk30MN5a1Q20EkYsU2%2BqnNIkVc50lfDbWx4ieLxVnKMbV2tVJCw05dyzvCU5KAw10PmY30OgQZnqcgF%2FJUj9bMThGpKn8smfFEa7guF2ayuzuKCe2XTTnexX&X-Amz-Signature=5611d43d071a83d7ffa61c1cbc3e25b5e151237ab7f836ee8e3377d656c62f3a&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673Y6CXXL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGG48hO%2Ba37glN0wOvEMtIHx1Kpkb8NJRGBdYXAWXTUvAiEAxHs%2BatAZNbOAHjvZI4lpBEvjNYFKD%2F1NX0o61S3BF8Iq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHE%2BGvuga3iCY4X%2FYCrcAzOEdfZc3spFt%2F45ExPCKB8IiZDvweoke%2FRrnCD%2BQt7zvIONaEgpTvNedxYs9jDbvPeyZpYk%2F2vYExSujVwpiVBOlo1tYQZ6E227ggFo3f62K%2Fp1CJ%2FMmloLJwv2UGoyagrG9Tc%2FyNPyZYPoO2Z6Epyt8Egz1l0MfdZ9ZUVxy2Bkc5%2BcGb4kXEwp7hNK1AzC4usSyXqkOfDNH8SK%2FhCpcCCxDTK%2FHifrx19uQxgJLb6X4AVxjzwH4BPce9j71AAeVptRLL80a3nAs%2Fp1ohcAOeISUO473AyIrq8G2dYxtgI6yt1fEbLNotXYuCSj8y%2FO2pj87lFtU5Cged5WfJMQyVuo%2FMYrCkhqUYuFz%2Fla%2FnCKtQODB%2FGRFynVcrlkVJerX%2FoxaA9CfFTcK8Cd4DOov4sJO95XAfrdT4QoFglkSJuYJpyOIg4Ffk8bd2KXsZL3jfW0SHpHmQBjPNLQrOt0%2FemtxFeC15yXp5WZ62sezDIQSu6aH97dfbMYQKextiigrix0fHIk9AUAEdPdiNm5RKy9WWhSfCzvfEdv2WvQAnc3l9Hu9220yoioE3rqZSjxBP2zyrh82tUPzs97ADpIfTJuxpaQZZf3%2B5LzY6tjnZ%2FYXimsS1wBqxr02KW%2BMNPzgb0GOqUB8EPrJGsJFLS9oU1er%2BTAEvYmRYX9k24Cy%2FcxH4tzehjQCu5mjGmjb8auBFkSNti5kRazr0ZgDYSv%2FNo7HtSornZn4Q%2BHViL98IXHvjZVQ%2F1ZKylBZxcTtnD77ZGpVy%2BMS8FgHkEOSRXXOuwwkRwOwKngw7bHg2wE90aEU68HlFiFdm3UnBZVsL1bcr4Znd%2FnOjdWmHzdf6WGFmJKJZnF0tvTbPsc&X-Amz-Signature=473f757e998d1776ad6f866e12082d799d8c892ebaae5ef2b2eb41f8446f08dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKCEQD7T%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD67HhHBp2bQMIxbYtzXbjgTxXdmYgt3%2BzvqWOS1P908QIgbh9jGnuytwAKSYxKyEE6CSpufs6fRqhhbL%2BjkNZ6m3Iq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDF1cnLNNhIKr6FKGASrcA9i1ZWX89u4PHz1lC1vF8%2FMsIM%2FT3H5yt1B70DO56S5gWnflow7C5nz9lwLgW6kFP%2BSGZCpO2j%2Bfsjw8AhhjjsdkLt7owxf1FNQFRuNAc7DHgEoi3J9Kr3vzEM8H5Mo8Ve1sZZmYInBH8CW%2FWg1EHX%2BeEUsqAUp37MF%2FllbddBGmubR%2Fg5CpxrC1m8dodLS1GCHv%2Fu2qcTmunV28FZq%2B5H7sSXeJljpZgZPT6TGYPtEeByW80oqghklzFqGPIAqP3p1HVuMCKN8ZAR547XNaCMcvFJ%2FWS0uwX%2BR9Y6JZRgZsjELNG1NM2SzDSxJNsz0RHm6g0mY2vVH%2FhGW7nXLfwmCw337ouP6llsZvVshOUSvey0FpVl1nbl9nOC3cTJyzwppn7F7lfjww6SzcFLzgt1fMFfNhUmXvNOY%2B9WMU05uYABmrtm%2By8rWAb%2FzyzX68MtqW8DZlDAg%2B04MEGB3PvLB86SyOhA82%2F6wveU5Sp589VvQMQiIRXBegsFkaAtiATaiUoweZAxo%2BdSHEaQqNk3%2FoSjp4pmnwoaFEqCeYGST2Mp6w%2FaDeS0%2FCL3ZXgaba8UZAZN1g1Lac1HUDEeqYDteU%2BFdrWGkXeEtLyLrmCwRvLu%2Bn%2FLrYeF60azhkMObygb0GOqUB4INk25XMdR3BPjqleuaqwl1GfOAjI8hL%2BFE0BND3Cj%2BdhdSlKqU30VAq%2FaQ69h5Cr2ZwgfRvTAM012HXofg%2FXRFbdmX9GKZ0%2FqsJlHgq%2FYiDUZbJbeXGMegJGscWdEb9%2FVXGQNCr07A5uYXZ9I3L9PoELj8IciippvAtDvar90M28mRQksN0DKHYDexnffFzeddBlIAonCGiKT%2Bnpp3g1w3HGcLv&X-Amz-Signature=bf41d02983ffe21af6be6327a99b0a1cb88684a7d5b305426c792b4919950e26&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDTSHFTM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCywQg8SlXkGeJyfZTfZpTpEW7wb0JG5ePdmLG%2BnEgctQIhANavRS1FHxVwlSVeiJEBvx3KbK4I5AaGGECxp%2FhaVGW1Kv8DCBEQABoMNjM3NDIzMTgzODA1IgyKMOkTcOvHLaugp1Aq3AOJONS39EO0zhl2IBgrDJoVQoxgc5HYuguyfyiovV6oxWnHsh7jnlNaTegMp%2BTRlh3CLm3JZK7EjoVbn0mEzZVp4xif0WRAqyzfesdSd4ayuns2J8tOXZmjX3gYMficFwbn2rociSDgCqFIbKFt1oiL%2FspgFS4lM94HiOBDE8rgt0FNIdU5c57uDb0KCupEcM%2B8LYos%2Fu%2Fy0wneTXzHUjA%2FnjSSt9VHBh0GTbSEE4L6mS%2BzqHl2%2FqG0ADckdWXR%2FbKcw5bQL0sALx9pg221uiPM%2B21%2Fx4TY7yyBhzepFUkARl298G021vyhJ9dyBxYeBiyAG1F13nEzLm0Tc32a3EtiudTlPHQ4gBKvncprMlzpFkzR4%2FwUsbwENpbfnbO6J6YChxRs55LoqGY5KIub9oVRpbpYqUB2Mv5kTgz2fGAfIjqrdwaIfqeubtxAXVyUXhIFhlS0inKvk%2F2qKl9gZbBPj2YCcHS4Qzw7iutMG2oavtJBc2COmVmyH4r%2FZdqZYCz3uFtBQi3u%2BwYQ8EsmBPgrMfGVsRAyZRNCDgNVs6PglAc0rrvW6GbZons%2BpN8BbILrGJpY4ld9KF0vID3JH3grDLmJ15%2BWaELAiNX2qRLVbzKMmbqYt%2Fc0xmklsTDd84G9BjqkAYqFlTlA3qO54WKBneYVeqAFfNUBUDJcBFnwEGT%2FMvqHWwmS4d3e7B0tIpReVQ%2Bya6uUNatrerZEPIyRgrRRiHlp4IHPWqpnpiT7EIfrFcgUlpTivptQt87Sh%2F%2BBiJrvM58c1d0Bhik6gIXtEBSKxpXXNXngMMmHX9TggvgBsugj3XE%2FcYcMKYYvYsu%2FNUZ75EhFUJDGEODI1S5%2Fp41Mno6pmnsg&X-Amz-Signature=cdc149225f244fad723827a9073175a31f8a5ae5059458a9f22da4ddde730ed2&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDTSHFTM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCywQg8SlXkGeJyfZTfZpTpEW7wb0JG5ePdmLG%2BnEgctQIhANavRS1FHxVwlSVeiJEBvx3KbK4I5AaGGECxp%2FhaVGW1Kv8DCBEQABoMNjM3NDIzMTgzODA1IgyKMOkTcOvHLaugp1Aq3AOJONS39EO0zhl2IBgrDJoVQoxgc5HYuguyfyiovV6oxWnHsh7jnlNaTegMp%2BTRlh3CLm3JZK7EjoVbn0mEzZVp4xif0WRAqyzfesdSd4ayuns2J8tOXZmjX3gYMficFwbn2rociSDgCqFIbKFt1oiL%2FspgFS4lM94HiOBDE8rgt0FNIdU5c57uDb0KCupEcM%2B8LYos%2Fu%2Fy0wneTXzHUjA%2FnjSSt9VHBh0GTbSEE4L6mS%2BzqHl2%2FqG0ADckdWXR%2FbKcw5bQL0sALx9pg221uiPM%2B21%2Fx4TY7yyBhzepFUkARl298G021vyhJ9dyBxYeBiyAG1F13nEzLm0Tc32a3EtiudTlPHQ4gBKvncprMlzpFkzR4%2FwUsbwENpbfnbO6J6YChxRs55LoqGY5KIub9oVRpbpYqUB2Mv5kTgz2fGAfIjqrdwaIfqeubtxAXVyUXhIFhlS0inKvk%2F2qKl9gZbBPj2YCcHS4Qzw7iutMG2oavtJBc2COmVmyH4r%2FZdqZYCz3uFtBQi3u%2BwYQ8EsmBPgrMfGVsRAyZRNCDgNVs6PglAc0rrvW6GbZons%2BpN8BbILrGJpY4ld9KF0vID3JH3grDLmJ15%2BWaELAiNX2qRLVbzKMmbqYt%2Fc0xmklsTDd84G9BjqkAYqFlTlA3qO54WKBneYVeqAFfNUBUDJcBFnwEGT%2FMvqHWwmS4d3e7B0tIpReVQ%2Bya6uUNatrerZEPIyRgrRRiHlp4IHPWqpnpiT7EIfrFcgUlpTivptQt87Sh%2F%2BBiJrvM58c1d0Bhik6gIXtEBSKxpXXNXngMMmHX9TggvgBsugj3XE%2FcYcMKYYvYsu%2FNUZ75EhFUJDGEODI1S5%2Fp41Mno6pmnsg&X-Amz-Signature=12df2c4a17625aa39bfbb60eee5ea807774e90f8c1bacd0a03aed66f97ba8c09&X-Amz-SignedHeaders=host&x-id=GetObject)
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