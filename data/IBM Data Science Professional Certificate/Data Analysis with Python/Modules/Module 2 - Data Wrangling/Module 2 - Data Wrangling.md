

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZQZLHG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIFJ5nfRqx1T92EWraIDPiX7Sm9sL8kRHtn3As61D7rRqAiATc5yTX8DMyZhakyoj4DPu1eMC3zWyAPw2gomr2P%2F%2F0SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BTyAH3zLLNlaC1siKtwDJK9J5xG5vG49OB2K9I%2BWGfI9QRDgNfa1b3IC9VRQ%2Fl%2F0%2BZFk8m4r8GMgzI%2FAm2hsqjR9dlk%2BU%2BTWJE8%2FrIrvuVze%2BQ9%2FWV3hWwRgQP8cl1R7qpQcMGi0dROoXbkuVG4Ac3pQ%2BlEm0UpSm6BFZUbLEDdtVl2ctD45CsaeOjFF9cQ07c4KB8wyaFQMV9gN3Bz1xG4BMxQeYaisNtiT8uEEZCG6HfVTwMwLk8%2FstpP%2B5hQugVoYzLo4cRcYM7B6ZlUXcfeK9kruRCJ1ZF8VksYdVeDoD43dofvXFby7ikxL4hqSjf0kg3h%2B4JWWEkTxoIK%2FPYSLr8UF9dMWtpTPOV3ixedU4bGYh%2FEKkTm7DoEYaNakIB1KhNAj4myOUsflE5vl87pptcztd3TmPUwmolMiIMrn2AtICE%2Fwf2XuN4xbS8rsruATKm3%2FEo0nfp08KF0HYSKecHVBy7ay%2FzKV5fdoq4tkBLKnoqeRZtXKGblO7vz8ApZNL6SLSc5p9J28AjeQeBp3KuvQw6OBtq9hOoR%2BeOX7PrfbKWwoO35XE4pMFGGR6WNNDXVX0yYS4yzFnmpfYp4aNvntn1o2avn%2BUDDt0%2Feg2ZPLRHs3KeDave0CyTzFFO5erzFZd1UmjrQw1Y6cvQY6pgH4sH6enPBr1r3ilEuJP0DtfGVjZhCevPLN%2BbNAK25bi8b0mLhPElv2lKFgMdW4fK%2BxbdV%2B%2BPDTG9rKRqhwhJg3kRzSacscAKE3MBGi%2FSUMTM4PpX1k%2B0CdvbkvEc3VFX%2F1UDZjKvYdMomjPG9jhgiVm4b3ZzuKMNR2XUoDqyjw1Px11TjF%2BbjrgdDX1XuXLvU2kSeGhH%2BniXoSdI0%2BXI2p5gjL6Wl3&X-Amz-Signature=d9762211d589aa4a75f30d9b4c09fa8b29923291a44ba8698ff8c30f1c07c324&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664T2Y725P%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIAcXL7aV%2B8yuxZvpH785hGiBGKCYodJOPd%2FB0G%2B%2FAvqjAiEA2LKyMrCxwQYt6axCnKa3Zoz4FvT9JWJFEJVSpiFTiJkqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLKtDjpf1a830FG%2FmyrcA%2Ft5x%2F5VRtiGx9XKauI2zsO0joVrS0HbBmohAY8dDbG4TsdWsB0uqhrx85vXSgeAL9PaAzExDkyqIwkKzIo8sQvBprnEAQc5MmYqDDXBe3uxQ8lDkj5S9dqIhXvYrm9KsQrInNN%2F611TIyGJhidnN8rmy5AJXG6hR58HOLgiy51UVJcEepl9LYZDptO3jqsJQivVrUwColbSTV8dyCHP1f78guobeM3MG7tTsJSEIttGSAMKhnJsSTKhDWLMjEKJVGYurXqnKYkFgQyEkLVtBKDn7KZGftb%2FzO8QdrAiqvW6eiTEsyQAAGidy98MDt0Iz7OmM62QELBBcw%2BkJ2izBgxW5YT4hxWoAbE6vPMBgPbsNIvuaH25UkZBRbFY0jxGOeTAOKvGNEAdqfn29FDVCYUxfQoOVnLwVtPFS3SCIlM%2BG1C0qDTqoM4QYV8%2FyA3eiZcRRNq6cIXR5QwLLOfupftecDIvHNgWzNyDxHwA3veBrBa7u7rWJ3iBQ%2BktM6L31KwYcSPvo09wuH7cxSLzVN7ZziB6BNCW5JGxilY04hjU7Nag%2F07dkuRi78XkR%2FXzEgZ7HQ5Itde5k0iweohnkP%2BmX8NFO3T3WvPhwBXmP%2F%2FH4boUa%2Fw6pQyzew%2FGMNSOnL0GOqUB%2Bg%2FUvG65xz2HkSo7PgIl7lZqVLQNiux8rvA9U3XLsF4O0GWdVIx0DyMU1TYdQrIDx%2F0PQDgJ2qKmUoT8nLeof1WBEIo%2FOiynncWatgNuVliudjDQfnXUA2INvrqIc9AEOG708rQIigfKQ%2BbJM7NTjTtmrREXQzENb3zxq1eTcdNh5hDtq0uBlXlLf6KueKvj1CEOHqAQnMEMgeC7zkwvgGBf5iSA&X-Amz-Signature=c2b70693ac8ceb6c0efdc12e3bb5e958ea99d22c8ea394477ff207983ddef7e0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662P2CNUF6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIBNJumYU0pVZLfXWuU%2BTSE0wfkeutjbXIRCgj%2F0JOSf5AiEAuQPBeup6BEjYSvRvEenbNVKYTuKRuqXK1M%2Flm%2F2DujEqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCxdPbwnihmEoTo7LCrcAyOSo%2BpUehK8Vn3lZsuUB2dx5N1WKG%2FEpPDGNmojGxzx32kwSMYCd%2FOuB6XnHuVO03iZBKZ%2BGsKaqAGuxdJlgsRdjlzkMk8cQjFDvjwyG8NWGOz%2FmvFBJIPSX7C8d%2B%2Bcwz0hSJ1SJqt1nZ04L6LbClrSmg0FBoZG5b9j1whH7ug5qhPYmexy%2BL4LGyBo%2FD69WAxk3aaLUo4GkzfjbyNLMV49oyOUvo7iqxJSw5EmzDSd96dSPgHWxPnMbKJ%2FNOUiWh49FoZl73kRH23zd0kWyerecjFTW%2FjPoFbBLaMhVFSYgpli%2B%2BWTJ9CS59TsOOyqeQbdi3YX4nwdUC0fI9W7tlzhmdrfzLsdhPhl8zflOeHXITe%2BAGOEFdOSyMVQjbY8bQEKLlxkzqePa7ZC3F4Otej%2BT0BzIl0o6MwVRTn%2Fi0mpeZpAfhhGrwBQPr94agRzmeTuTqzP56bIAt3V6FgGubQ%2FEuqGTZHCgFRuNZ%2BY2DmiFFOLTbktFyFoXTgKneUXkI36FddEJwIChDVzcL%2FYGZ3FDQaUPWDcdaVeHakM9Nk1vI9zEvl5fkcp916L%2FQe7qJczenv8VNg3O9CuxQpvKMUbKIJRLZHn%2FFIAsX%2B0xYKq0hm3Ty9Hy%2FInEiVHMK%2BOnL0GOqUBJkMNNwibpNddaA%2BEIQt1cikiVOQ9ZMkBhow7C2UcyeoDg5cHiYeMmsnW2N4I2RxxdDiMdWKdhT4TyI0i896WQaji3E4iUFR6Y1iXTu1bZ6Sedi8S3oiLwbFQ%2FoLwmkbldfsK49Mj5OvveRnH1ha2jceLi%2ByKkJWrSNZ4NHpRPqi4sItpQDuI0rPdA9Nry4jOKOBkSjE3IXX3%2BClUYY2GFzD%2FRd0x&X-Amz-Signature=b5aacff4d3a4f6da39ac0e5792228db07a47e11356633f5604d8a1d6040278f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z425VPKQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDnt4pRbNpZPee2ZQxwNyCFA1pauyC51fm98Bc%2B%2BjgIdQIgekzyytMrHEYvdOuC7TFzCbWN8WrJ8lOAns7LSNp%2F6NwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRIh%2B%2FQXTNbYLRFNCrcA%2FDH%2BRkGAw%2FqoD%2F%2BCj3WNjs%2BC6iXMA90%2BxuZZnNxmvOmZK1jTkrLq0jSPHb%2F5%2BeuXfwz4mbt83njdYqqO%2FAPU32LTSudlLm5ZTQazRh7GCfvgekgXzyqs27xrg6%2FReAy7uhk%2FqS4YbWp8bnPMtMoVVOEJoOrnn3Ntgy%2FP4qqydkBtb2zVN9KI1Etp80YMyppNEwmRpA9sSoRB72lChnXsOM8hc7Z3BsYhw%2Fdui2meVcXyZaIvDdWn6yVo%2Fwv6yjN9ERHHEYpw8i68Rvqlu%2Fv3jF0XighT2ivcw3jO%2FB4oztnYN81r%2FRSl07de4z3IKAB0pzX3NQ4AqfpsRWKffTHQs1Fw178hPWF7rdzovKbgfzSwmFs0Svl6L3JxDTbVnihsSFKGGCugRjn3SISXH50qBDYd%2Fbsr8nLhOeJ4W7z1KZtMmvFmUYIwiNqn0UEYzJpLrrGyyE3SEo84WvZKneC8pe32fb%2BVcsq4P9rk9Q09MFNppyAauCmHnCHpttFlZKts0SaEEW27roFEGD9fQJ9oFTc57e5iHweiD0U3SvCLGnUsMKzMb5yo40eyElpCu%2BR2%2FI%2BlQ%2F8I31s29nv%2By7q27c9l1ZOnLgDNYivki3nKEq7tlbDWS4CPQ%2Bo38cNMNmOnL0GOqUB0jPKRvXXr2eKhLxuAu9n2ljcB906wFvCd7LX%2FWPfucYW514nrA8s5%2F%2BUq%2FLYI230BrwuBVxNRTQi1LcazOtMvRtq8retUXuJ4kM5OZ916SAibU%2BxqVnmAUZs3d2B7o%2FPum146SRF9%2BX6gONljAJ%2FRsvxU7L59AV7U%2FtzrW%2BoDLbtJEfX3VMC%2F8tsIscWlvyeGjBvnm1Nh4kA4vkppaPUGveK2i0p&X-Amz-Signature=74a7afdbdcef44296220f124a3726b1ecaf63de556382c1d44d8e9a6fe51e08a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULALID2H%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCdx3yGqoFfFXgwedxjY6mPeVrzBis0WX3q0BWS4uhKgwIhANdpwXD9lctP%2Bk94NgWSYxWJ1slzgSqFlw8Sw0zMsT53KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJb5UaZbd53oxd82Aq3ANx384QRRR1nWd9PGJUDG0UrW%2FSzGZoJeBED6qGOZrHhQ2Uz2MMAOTrtbdYauZ7dApgdJ9vz7gC%2B1bEq%2FUmjDmM%2F70%2Bd8fb%2FOObLNi8k3OTRj2kqcQxYahzyqQJAOS%2FIA3VGa0ZMlHEzIcv9Oo%2FF8yu9ed9eqc9EGQ%2FnM1Rq59UN1r7MHJ0jGPi0v%2BEY%2FV%2Bmvyw3Wj%2FxmGcNXr9t5gn%2B17%2BjVsAyCpzkQfUB%2F%2FLnGNa5ef1a3PfMU%2FtTaq8Jwcjw2vq%2FCynt1UN841hKjrDXORO6YzK4%2F46BMqTFDXJHjwtshQliTqjDjssW9cgjUcjkdtLN%2BnkM03TMJjEXHwd%2FRdt8bGQ6%2Fe%2BYsKvWniLwNoxBiCnL7C%2BrmO5HW4UhVzgAv%2FCwNkhJQoTQNdaK0tR5A3eDa36pMBtACu5KXXuuXM2c%2BtWNrNCSALlTRsPhTGRNQDQOKpyqTwqhlMEmC61PNNBAaSC3GjdcjJXatchVptEaED9mHbKqg1wz5X6QTr%2FiD3URE1bUvDk1yNhyhpVkhXYuLm%2BCVv104KISbh6uY%2BshlmpmDbAtraBTALwm%2Bz5GoO45X%2FHjzATsKcH%2F45uRPukoaVaqO3tkq1whPekKOrGV6IUIpQ4dTGoUBzOPDCBjpy9BjqkAV%2F6dtQaXa8ytz%2BMDmU3i%2FVkPfb4jZ6Z7RHhdVIxcPcl6I7nnII0tEtATbCbGCxJsgcqmBdbTOFXOdmdDwMWX6XIZ9x09%2FujCMd3ggeLk3DI4bZmVQtZZ6F7Kk8hswUuWCslRQ%2BhAku2eXkCW1ETUStJYsZ43qLktrEFmTGiUEg9YVvaraH2Zp2pYA9twjizFI2KexTXb6IJ9lbo94mHdtM%2BIaMj&X-Amz-Signature=7b16b2776be4e60b540e805d1b06f176dd5904fe2dfb5b15739b42ce30965482&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TH57HTW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDEt%2BHk1u3oXV7ngUfs80gJIl%2FbsU%2BHAfyV70r3kELVMgIhAPrzYh%2FcKXSk9XttnbRGQbY8QgK8CejKcNEbK4pzpZ0AKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzgYXM%2FdczI11%2FRRmIq3AM7SAcMOo1HfAPAoiwAXuS01l6btkFepWwxniHQjwf4H2h5tuX486suvfpLWwE25Qs36OJdd89pk1g16ShICtVjIK3juhwhPUc9w%2BHM%2FgghRrSSUTb6gworu5MsR9yGBanjaMCGrvY4uvfV9AYldGiLdfkZpnpZ67Xy2%2B89ItknBVe6LLfyutpnrDJu6HC7vhAbHiXI8m0KQV5EzLb3PIPIe5wOQdMEJ3zQXgzuFDJz%2F4XGEffuohgH6tHtIwqMEYiNy5%2BlXlUcn6Ssz1Y39hPoh9MNfG4psNhJir%2Bbdw9OSgZtBREnYRmoxxeXeTwt9%2B0WOTvGueF1MceGb6GRu2dw7RWeNz3%2FVJrQSgTgcizIeQMJ5opW6mZkCbRXzbhz2YjMghCxAu3RRTNXa0DnX9LfcxKpMLboHsgIZzZLyk4pemDgR%2BPTIHmn8mDzNUgKZKtfHoxmzKKI8EOTP4tGTwaOTIeYIJDtsnQYrTRtBzElKkZwUclIZcWT3QI6%2Fcl1hyUAT8LVlTNGyqXGPlPnWPI2H02HEljZVcUyLJ6DeaOMVht%2FFo3ce0uVrI5HwbtjvpA%2Birbx0zgy0ScD5ZrfG00KF92OSq0L5xpdW5q5ya9lF%2Fxi65FNICUPU%2BQcEjDZjpy9BjqkAes%2FAbkeYdqtKC99bPS8UN4V55DQODuyTgwIgwZ7qkZO8SZDDH%2BpmHBkdXi7vnv1745sc72r5O%2B8NK4nzpYbJqAnvcDyq4WKAvBscmXRSnEaEdnNNXyEYX5igh2o3yQzw3qgSQGdxzzvBoCGp8BkoiahrHvcjGLJgdqlN77G3sHf3gWPxXoIy3m79dTZCDUBezR%2Fh2zKWqurQrPmdC990eiUQn8Y&X-Amz-Signature=ea704c6f56b13a9bfe4753db245bd21c789ca6d68f69a3c07c9210ee387b81ad&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE7HRWHW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCwIlW2CzHpNZ0WKWU7vbaR0jH6B9jiiBzExuijNoxz%2BgIgUMgv6%2FWhQ1CLwKhtxNWfA5Yqv1BLx4cfar1kQwnSCB8qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA4sfdN0eqFJ9%2FLLEyrcA5VxPamRs36QjS353KtTPFwSbuM8nJKIlnBYauhQKbhcd4PKrNm%2Bbw7gYZuAkTyl9sVTdD7L5YLfJkeT1cn8V89sUnOVWF24j475CtCDx5QiIWmZr09VnikQzLhBlxS50jqgBuIVR%2F4hfcilaIZOYmJk%2FnAXsMLu4bm6JlVFrIFaTis6glK5M7EZ5jVcPfKUjFFHV7USAJnqmwtJQ7kJLI6NHOkiC%2Fd%2FE4l0ntjHUhAzkchEM%2BemFed0pkMr7VgyMIU2ay3uCD441ZZ6mtFxbgGFz9fABh5KFyBShRu5Of1RJImMhWfRD8pBZTw3aiS%2BqZyBLbtyXiuLPet6RqwkdjVAOxoXRAv6jRx050IXJQc26bKmuta%2FrMe74t%2FpnjMyEyzPCPl1xNHE4bMV9M0xgsbna%2FhcZPWw91CXgCGd2%2Fqdr7fGmOYUv1baGAXjHpbngODeyLq%2FMlDeT7wdCRolwuGGBeRCtmLpShPdH5n6bUHuj2xdjShwQ%2BZBC4Osdss%2F9EPMtViqNP%2F02XT94EhTR5gUersQA5N0x7yJfvxTEPAf%2BmgRlfIphz9VOtTKgAjl2ho%2BkB6rY3NiR%2Ffbxgifx9N0zsXjv45K%2F6X4kXU8m421iGYQpiL6NZJdsNk8MKKOnL0GOqUBbrB9DIuyR7%2FlcL0J%2BQFknpXkqihbmfYq%2BQpYo0su4dYkFeEPBnitqhv3HkGlDqPQvgQ0OSrXDZIHyuvAhKBZgJQkWfbUkIv4aFDAaS2B63xxXkaq4eTc7aWYtfP8h3V8UnZV%2FoI5F6IldRdu020LF%2Bvu6P7XohlvPR8MROnSKcd%2FtLc3yTFRlQgq6RpyAGQckfBu%2F5p54VIsS1t%2FkRHnMibhjMZH&X-Amz-Signature=8fa5b239f63c0713d2a7728ef376a8071c59418968635052e3c029ca073cca66&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJAFN6HG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIE1H2f93pfLJ03EPadMnpx3tdY6pU079RpB5qgZv32nmAiB9iSNyTUgOPsZrk%2B9hSIUWngtoYq03mhLB8ozFrswuzSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMheF5%2BSQ%2FdCMjgv7pKtwDJuB2r%2FXtR3na4VYm1IFt3HCHmuklkEdPOxZ6zCSdWfCc%2F5MO%2F2hLoEaUt40s7aHIe9jgxWO43izNudPZAT5LRseOYWv6wNaCzljg6tlxURfPbjuV8VJm%2FMbaKHFK%2BY4ujjmUO54WqzgTphbx%2BaNqf4y1r5HxcvmiSNRRpP5DQZgRLFYnSszPXJ1Pnt982VVTrzfgCgtKzoWXUuTXc6%2FvEq6s9A%2Fq6%2BeZ%2FFZSXEcjkqAJkjVVwgIW8VcMjymz9I2zEK2aJtt8noqfFz62l3V1kee4Ya9Mcwoa4XnekDxniwjj6sG5%2F8mWxwI%2FCDiPX%2F4jakGmZ9l53M7Vn3H85GnbFfqP2YZYuDnwCRr5Vu%2BSMgDnb8zvRWTNYL7EkFJIcZWzmOFmTh55CRDhrv2v%2F9q7ABhNHxtcHPDrbRCt%2BnwMnPpTLVSY6V2JvogjsjzgsH69CHy4CYYwoFyVteWu6w%2FXo1Fj3eDBJ5P%2Bz8OREZo2M8nKLgjcp31SsoG7A0eHy76YB0orANR8bEa%2BWi6E35wAL1tfWHvE2S8S2gCp17dwMYeJR23%2FTlPlHc9VidtWkvDwK5hc6AR6oPZtX2Ow6EZsRu4zTEArK0bNZXvDnmmMSb%2Flekzk4TbEeLW24lowv46cvQY6pgE5ZC5fjk6nRNX%2FkB4P5C2Ldx23LrHhSm4CkgQVyDp3Q7BiYQaSgmJfrHtoYSe%2BLIHwpICne5At76t%2FG3diQw8Qb5ZrxK8P3vZM47ttWGGbfNtSEFrTlQd7lOzoJeFIndbYc26ocY%2FoetR8KquU7Q8CtC5B9d2hHe4E2QpqHRoj%2FXu8dgY9MSPbVbTWh8I16HYFBGMRBS2OuccQ%2B0L5K%2BzleAD5etjm&X-Amz-Signature=26f49d12f273ccc81d94797fe4d73e13a75ea54633829fb6c689efb89b5a24b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULALID2H%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCdx3yGqoFfFXgwedxjY6mPeVrzBis0WX3q0BWS4uhKgwIhANdpwXD9lctP%2Bk94NgWSYxWJ1slzgSqFlw8Sw0zMsT53KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJb5UaZbd53oxd82Aq3ANx384QRRR1nWd9PGJUDG0UrW%2FSzGZoJeBED6qGOZrHhQ2Uz2MMAOTrtbdYauZ7dApgdJ9vz7gC%2B1bEq%2FUmjDmM%2F70%2Bd8fb%2FOObLNi8k3OTRj2kqcQxYahzyqQJAOS%2FIA3VGa0ZMlHEzIcv9Oo%2FF8yu9ed9eqc9EGQ%2FnM1Rq59UN1r7MHJ0jGPi0v%2BEY%2FV%2Bmvyw3Wj%2FxmGcNXr9t5gn%2B17%2BjVsAyCpzkQfUB%2F%2FLnGNa5ef1a3PfMU%2FtTaq8Jwcjw2vq%2FCynt1UN841hKjrDXORO6YzK4%2F46BMqTFDXJHjwtshQliTqjDjssW9cgjUcjkdtLN%2BnkM03TMJjEXHwd%2FRdt8bGQ6%2Fe%2BYsKvWniLwNoxBiCnL7C%2BrmO5HW4UhVzgAv%2FCwNkhJQoTQNdaK0tR5A3eDa36pMBtACu5KXXuuXM2c%2BtWNrNCSALlTRsPhTGRNQDQOKpyqTwqhlMEmC61PNNBAaSC3GjdcjJXatchVptEaED9mHbKqg1wz5X6QTr%2FiD3URE1bUvDk1yNhyhpVkhXYuLm%2BCVv104KISbh6uY%2BshlmpmDbAtraBTALwm%2Bz5GoO45X%2FHjzATsKcH%2F45uRPukoaVaqO3tkq1whPekKOrGV6IUIpQ4dTGoUBzOPDCBjpy9BjqkAV%2F6dtQaXa8ytz%2BMDmU3i%2FVkPfb4jZ6Z7RHhdVIxcPcl6I7nnII0tEtATbCbGCxJsgcqmBdbTOFXOdmdDwMWX6XIZ9x09%2FujCMd3ggeLk3DI4bZmVQtZZ6F7Kk8hswUuWCslRQ%2BhAku2eXkCW1ETUStJYsZ43qLktrEFmTGiUEg9YVvaraH2Zp2pYA9twjizFI2KexTXb6IJ9lbo94mHdtM%2BIaMj&X-Amz-Signature=cf9bdc3ca4fb8ef9fb160b8e3a71e70ffc6ee65ce20d02434a3be5f2fda9a4de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466474JTNWX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCUUxAypctHSR%2FDQIH2l0H2PGpgtgG32OrvWo6KwJ8cjAIgTxaw99cuInXP26mu00LPzoOpjjlwFSZjCSQD50pTOJsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEik7JWGTDeqxFTa0SrcA0x%2FQDQkgO6NxYNMRYqJ0cQ9mzxNasG0X6Fe%2BvaVWAfWnRnUcHnEZFWVDAm%2Bh7VsK%2BqtgYZq8WZwRxiueq4TWYuckc08Zyfc6IbYLqmO%2FGkzK0qsQLL%2B%2BNOTkPAALNuRyVKoaJdd4L%2FQEEi0kolozBvnKeCAnEKU8C4XjHfowKZ%2Bv1PjNA7Toigk7QecZaSZEmUMjdKYehWmCjSliymyxK3tdx2BEUcrFnEh9L0EO1zCwRD0gxK8GpsrLiJzHMH3SwU95IIv1tHMtQYEuCL5DR7iugzh6kmqxIJcUUMdicjN%2BgF3zm1H0BXqjm6DruOSD0CoiKi67fl9UKjoEMSTsbRNGx%2BVNTfKLPxm8wH4J7j%2BupBe%2FmXrL6mg9NiDc6MT7SRvg7LEx77WNU5nhyNp1mPfeQ3WLZm7ZmOvdVKCrDAxEP5iJiKWm50%2BGQoSfoyocv0WvljGl8Mv07GulmdQPgYfAIbey4TYg6KtdPYzAP1PpKwAFvnbU6vj6dhit3MYXQ5S4kx7qzQaxIQpsra6sONE8eyIxUhKFWcD%2BmUARGxnT2niqO64Snqbf6ggU5w32QUAMNXjSwOcBI1HSQYV5XsnK9nBAmHKI4Hd621jx1Rne5m3RESelLVY2Hj6MKSOnL0GOqUB%2FzJV%2BzXGF5gsx%2BRSgcK9S%2FATiy7ZaD7FvqH12RLvArXWXZ%2FV10YbTLoiTLVDQdzVcvSdxqV6v7J6Bb4WoeOQBiBFls6ogjGCppNnGlEwLRpPeu747ILeg0xCoWchGubMCyt%2BLXnMMQ%2BMy9MoPRmRAMd25Q9eT%2F05mDXQX0Fal8D0O4BxvZ48miV0H8RsNqMuWB6%2FoQoOYWI2U%2B53zedFTMeV3J8r&X-Amz-Signature=db1cd139c71e41f7b41c9deaf0d16bc7413d31f38ac7bfef9d46c1f6f954e132&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466474JTNWX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCUUxAypctHSR%2FDQIH2l0H2PGpgtgG32OrvWo6KwJ8cjAIgTxaw99cuInXP26mu00LPzoOpjjlwFSZjCSQD50pTOJsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEik7JWGTDeqxFTa0SrcA0x%2FQDQkgO6NxYNMRYqJ0cQ9mzxNasG0X6Fe%2BvaVWAfWnRnUcHnEZFWVDAm%2Bh7VsK%2BqtgYZq8WZwRxiueq4TWYuckc08Zyfc6IbYLqmO%2FGkzK0qsQLL%2B%2BNOTkPAALNuRyVKoaJdd4L%2FQEEi0kolozBvnKeCAnEKU8C4XjHfowKZ%2Bv1PjNA7Toigk7QecZaSZEmUMjdKYehWmCjSliymyxK3tdx2BEUcrFnEh9L0EO1zCwRD0gxK8GpsrLiJzHMH3SwU95IIv1tHMtQYEuCL5DR7iugzh6kmqxIJcUUMdicjN%2BgF3zm1H0BXqjm6DruOSD0CoiKi67fl9UKjoEMSTsbRNGx%2BVNTfKLPxm8wH4J7j%2BupBe%2FmXrL6mg9NiDc6MT7SRvg7LEx77WNU5nhyNp1mPfeQ3WLZm7ZmOvdVKCrDAxEP5iJiKWm50%2BGQoSfoyocv0WvljGl8Mv07GulmdQPgYfAIbey4TYg6KtdPYzAP1PpKwAFvnbU6vj6dhit3MYXQ5S4kx7qzQaxIQpsra6sONE8eyIxUhKFWcD%2BmUARGxnT2niqO64Snqbf6ggU5w32QUAMNXjSwOcBI1HSQYV5XsnK9nBAmHKI4Hd621jx1Rne5m3RESelLVY2Hj6MKSOnL0GOqUB%2FzJV%2BzXGF5gsx%2BRSgcK9S%2FATiy7ZaD7FvqH12RLvArXWXZ%2FV10YbTLoiTLVDQdzVcvSdxqV6v7J6Bb4WoeOQBiBFls6ogjGCppNnGlEwLRpPeu747ILeg0xCoWchGubMCyt%2BLXnMMQ%2BMy9MoPRmRAMd25Q9eT%2F05mDXQX0Fal8D0O4BxvZ48miV0H8RsNqMuWB6%2FoQoOYWI2U%2B53zedFTMeV3J8r&X-Amz-Signature=d4f4dbe82f36d81364cc290527bc5e0aada868a7e3d766f6878dd6754cf9d536&X-Amz-SignedHeaders=host&x-id=GetObject)
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