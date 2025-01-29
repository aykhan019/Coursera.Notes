

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQPCXZSH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDp33KwmWJKzdzDArzq7bm5PSu5Aekj7XAwF7A3wu%2BhagIhAMMuWc%2Fk3W9QwAgvxQgsMDeW3yVILc1KCI3aAB%2Fz1G8DKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsFW4W%2B%2BF3N1mJBIq3AOiJf4%2FsgDE4WwmrIISnU5%2FfmmkBKIvltPTvSLcyixSqL4fIPrOjnFfG7ZkqOz01DOjZyVJi4l7h6%2B54sMTLipyjnnWDjVHR%2F19i7IPPBIaiKDQc64GbN0lRA9z%2FuGipE19k9eKQotnRjPyNLnzfJ69%2FOVIN6pk2I7K2j5igR7KYh9fG7ZKNk6PQ0gRtMGMRNNt0uHigmphkrLD%2FIsXfpG8D9U8JEDara4s4X7PMGjwGR46V1kHrjTdQs%2FobwqJzhZzkqgyzNZMSXaKPq0dQFnXjyO3PPbWQZAh7rH8l%2FqmWkzfkw2WBktrEyUJgYqDMQ8v9iB8whzu%2B3xzf%2FNMoGPlI5DenRmbbwRF956pZQbNnJ6U7iHgUd1LSBpWMYSI7zd1sBk308tELy%2F4pKmsNLnQ8IQT4AeEKI9oAvB6PLUHeV2v4fJpLaCIMROgmfDbyRA6rB5mzKm9MX4WeOOj0mNpdMCAP%2BNfGV4wHNxb%2B8p2P8vyMyazxNfrG3nog89AJr4d4kqqAcqlcturnTZuwZjePmhQiEgezpN5d%2FHvVDtWtsMgGyszR4SQ62wr8n5nZdzquUZ4flYgN4NOTpW7OFJlRKuUsFvcrRydfKrgKoLgJASoVy0k6ImRecIpWDDLx%2Be8BjqkAYz5KLjcSYaCXRFWv4qsSGGTg3gygM3li6c5y%2FVq6J8TR%2Fi4KZMzhTLDQYGgCsOqS9T5cAxYQ5%2Bpit8VWQStQ7PXaQsE%2B9K1BQvdXsOpR%2BFqTqKZ70JlUKhQBqpaD9xKZ9hFa6RbDcKtFzVy94EOHcsXY%2Bqnzl6bPSZ4IODmPPdDCQ56S7b9L%2Fe4I4KPhltDEK5UqSTnpj0Jx0n3n7%2FLx6FjFXRA&X-Amz-Signature=fabec312868437c3ac1e78d7c5c23f6cf1449037b92de700227e642089626c9a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SA5B2A6U%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnj3iPL4z8wyDxIc9oOkd3hDL3icMR4THG0b%2BLojBiVQIgCDotzb71t0xE338F809n3i8s436oBffJFaE8TmuYj3UqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNVpe5sHSPZU4z27hyrcA9dyKMJCtcXJVd2JJqVqj%2FRkOIquTt%2Fcko3YmpMopt5n%2BZuzPKdpDtUkn62ZiJT2BrpTreqgeLMgv26eXiqM%2FFlvjtBEcFcYNgPJ1OD4JfjFsTwVY%2BlkW8u2b6i0IIWzMjLpCw%2Fw9uu1NOvRVky9%2BSRJ6GeOj26WGA1gF4V%2BGih%2Fs%2FHonroSNrqZx%2BuKEEvvmZgCmmuKxVzRzC%2FzI4Gol8gU7BOCGJREwEMC8QLcwKEjf1FFEO7HXOp23y0NN9hGBqxqsNT7t2z96DWRfXJb3SNXaeiVVgxzwJlsKXG3prPeuN4qx7W%2BgLJDkTLkTOGVv1oOvW15tKhgYBa8f4JDWK5ra2gqXVi57J0HaJ87u4jx04uZp7yB9v%2B1MxlNUgYcCg2i8W%2BH3nBTx1XQnvIq0flpay420alaQ6X3rrRaxKibFALAy%2Fft7%2FBp5nVfIElMBkWUW%2BXdxpLy47WhZgoofd4%2FDpxDYO3P55Ru4tq9wk1FcmDbyxHyYNs8xUKpRkggtk9kjmsp2TUENKx9LRsSKGLeVzsOibvSB0%2FVgZpKpUPQHEC1gUVWpswPjygPuFV8HxosRQlFYCUg1jULf7YhNhZCSZx4%2Bnzx0uahXx%2FR8gBFCv%2F8sst4Qnkk%2FKb5MJrH57wGOqUBW3cAWuIQ%2BZajwFM4CIzmkZWT47iPNhoc2Zd3EhGRQkEeAlm30XY0KHwh24EDmGInbQryyFLhKWikcMdk1VFWvB%2BJc%2FgryGxR1fF5hR13xKhzjoSEewX%2BqaPCUR3WFvQy2ZqjXk0sig8QdE5TmlYpTAvHXePFRtXXc5u1WUEbbzHFf6VtoA4X0mAvZZF4OtVE1TnTlO2cyBu5r8pMPHI7X5Uh%2Fr2X&X-Amz-Signature=e3610dc4a423dbe6373f688a2158b761ed4828d19f8092b3c24da38fb45d53e5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XDOR76N%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC6Ip%2Bxlx1oyeo%2FkXt2akjreqrvGxwQE36q1qcKX3na5AiAwcKiGosMPd1fYmviC6DU7wHR%2B7XHGTknD5UahXprPSiqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAamiOgbHekovil5kKtwDEBxxoYQ62LoRfM1XlLgPVTTml3sn2cmDAzssrCS6pDE%2F3JE10nxg30oAIpmUyDoo7fE%2BFF3jujsaIGz1IwUBJVNd1cx6HFjrJK7%2FjnRWmTI5GlB3vX2ssu2RVJ79m316mYmw4DXbwWF1bih6uN9SqdedjpDlJ404Mn6%2FLuDjAWQEScRhpnmskuGkHQcegMPWgfOKpm8qCFHV%2BhEaq4905snHWUMsC%2BSe1qJuizN7JXRm1idXc2iAqRAVLV6WUq3kxDShUwSZmuThScYgHe12S1VequRPeqAv514Qyr%2BUwlcRov9QklttCPRcHhTyCxx69bI%2FlLY13bYRyr8oCBcRTTCvhS7FZXL6IRWyADs%2F04xUgWPeq8SA%2B0e9F23fhecn6hrjdZ649XodDsCmh9O4XqEsMX36XDbFONc0zHSx%2FwdNjRsHOlWRYwoXClgR7mIaG%2F%2Fi6BwYzBYViZzorv4qa9rFCutWWwYsEazedYtA1UJvC0iVsEwXmyf4aavasmsKauoPSpWfnr0R4cC8A6GSmAnY2fp2Ry5WSGNUUdWe4JUxXgPlIFyeul7YIC3PCcnz%2BeGs6iduYGwmWZeYc3Hd9Rvdl9kbvr58tKZWDqOmByC3Tnd0rD34s%2BabvgQwy8fnvAY6pgGsIKMiS7vpJn3yADCXHd%2FDDySgP0FW2vRPQWWmWE4NEg38uK%2F83IM2v1tumNTfJ5eE5aNnPPO1yXrLL5iMB4PeaNxEPev8O%2BUg%2FRfhcIsTXnaio5Uh9Z7bE5zvt8i8CzWRiJ%2BjUFoL5Ob3wEDJSzoKlj%2BTHCu93KjW0yFG%2FHy%2FcdalP5ZNfPX6DX7qqNdmVoQPldbQQbdTSp60mmQR7JzfMoZX7rNz&X-Amz-Signature=1cb7875958379b8272494628339040acea4f62448f7c65e34213db46db17fe97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6CPRP3N%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAVGCDUjhq29KQl6x2RSRHErRY5yrPBMrY9pR7v1YBEiAiAFNS3csB%2Bq34anJwtmtlPCM%2F4K6e5A%2Bl6i79fr9M%2BugCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxXy7yX6EH8vkyXReKtwDrnrsTdhNAGURP0KmXzTi%2FIhrQFLj98C9LRBKnlUi3GUxtjl7M1V2zMwB8AFJECea14EBDtvlLW%2BruF53lTdeAK7EmmhhpMmyCAZsm5JMyW63PvAvGFLsVB01ApckDxr56%2Fs3Z%2FE1dUefN8PdfYjlTyIYVxjBPxyQ7QlR0XLIWt8QzcsHeB72FQJxZKd8tDFeZBQn7EHtlC50avc4b4ybuz%2FFvLZadIqBDz93OrsF%2Fxp%2FBdMh7DhAZpxfTdiYmlWaHTncp2UboAiuGh2bQem91OJgdZpjmZXaV%2F%2Fbb4PdrJYJzzyZPtENgssQwRccfY0Mj9o8Wrpuk21HSKeQizweXL2i%2BnuruVm9bbNdln%2FEpUZm6sHlQfwdxF8LNL%2Fdj%2FBRhfES7LTM7YlEERN5RHkXZai3z8TnOHHiBpZwtMZ6EXd%2F5%2BpQxQYzjUloSxzPKW6Pz2ppW%2BnzXuCuUdUc%2Bhur%2BoUkHtZp9q%2F8C0ZcZ22rEg3lGtBzbv%2BoXGSXk1gm02fQoEGUngax5NKWZApMJMNzVr9aADUaewkTa9%2F1OEZN8jiCTao4gPXyTfpmVEIqBSKpxqyWYtQ8oiloXHoes%2BobwBqK1JbdoVjB%2BCmfrWFd%2FeK7echIKyp5O%2B7%2BxV0wwsfnvAY6pgFy%2FCmJEfXDs0KZdw%2B9oCccZJnxtR6jOGzBFO%2BWw6YP2DPyzapSrUBBwxUgXCYv4Igm5IWxlZRlyD4LySoa%2B%2BpntUNxJ%2Bp5iIUhcWeIafehoY8Mq53V4XV3cx8DENDs1YLxB1%2FZj%2BCg8OEiEy%2BFp%2Fa5zAxYpQ%2Fw%2FIiafVgSXfPHuY0cDPQRHyIqrNhM98SHIEyBgcb%2FNZDPt5GqfvMZqtLsGnecFE7V&X-Amz-Signature=4dbf52ecf76863f78cb6c3f2df1c47ca48dba4a833fa20d77084840d73885215&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IKNAHDZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1GtcyiJxAPWfk1GuY2YFL5XvdiwLR4MK%2FQFtlzeTAbQIgap%2FRf0bMuiruzfiRYJVdCsAehpw1RvbjerBeXn4ZXVoqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIyHT5C5LVoLuDVpHircA2HEtLASAUkQ0PhCFbcGM6ndRUffZa8280yMDjn36j9DE5SwG5%2B2%2BxX0V5WAyxaoapF%2BWyMWDA1UY%2B1SbOihCM%2FdE%2BIEAMHJAoxV6J2noB1By%2FV%2FxFlUP9T%2BeYy40QNam3M7OKdCNS%2BX7aM2Y19Tuw2CHUdxOW%2Fb7GVKaXLXvK3miwQBnO3CYnqTskdHjmETAwOpG1xiGNcFeDxjKS3YJP4FShMeG9EeC8y42ktyX41RtFI4d%2BpEVotGHokQw%2FXgHm8lBTLB5IHB6tgzlAayJinOkmABeSXaWCH8fad%2Bo4dewGLgJuH3noQfHTjt2vvFpS1cHvQD9U98A1jmSGALtNiVfSBSJFMJCwwsmgGm04ieB10rg08dYZ38BpgERkSnsR8ovJBmtwXZHhQ%2FAf7T5ClJi8iR4ZXRJml0JRXu5X0ooWOpphM1XvXYGEcOWTRkhNBX8TBr55J7K2Ong32XLa4MtV75u%2FJ0DwDnA7pV9hwQ%2FQ3Di4Ha3vAYWdHsHHdbAJHT90kx2hEJUd9bCQ3qRPvWGcbqwt7msKIjvJnoRq%2F024VTDNDgbEaK%2Fhq6NJ%2Bp6OaQIRp8FINj1HO9Lsh2pg4Jb3jSF%2BAwITO42okTes8HmK3xs3DZWigTNKDRMK7H57wGOqUBllK2B37uAPNK5zESCjMNToT%2BXGGDe%2FP7osslOK5sjd2MI3rV%2FiF7rNh8k4GR%2FDdQDFNMgD%2BeDWkvqsYzJTzBq7KE6coMFImLA%2F%2BEhW1zXNUgSAKsqcNiFIizzX8HgeXd2idfpfIHsamk%2FkUdPoky83dlB907XYvjluy7%2F3BxP5k40MnpaO1KFjo5Ltbt5XbCipgKKqJeNZu4xxAlWGwjLkD6Lbel&X-Amz-Signature=538587b3be60f074c4dbad20860bdb5e3086d1ed51d8c05d77df30c57d9974c2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664S2O6ONM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIDFYrPVqEw%2FdOyqPmtFWqHOvBEGGy4S%2FS45xi2j7bdwIhAO5fB1D7d8raXf8QfbNir5peMj%2BGp8l66I1qRVxCaTluKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzndz5aedmQTD7fH%2B8q3ANkHqDQrkWkuQHcQh8pThISeXEVcc1HpECkaNHUEoMihhgBs%2B67PPkW2g5Eomgockmtw3ssW6jLq6EKA%2BLKDFeAldeSKxGrcLoBPS4UwVtz2TUMHBZPXESqCP6d4NasG5oWhHHXz%2FDOaOdqjgvmKRd%2FQQMyfv4ujbuSZ0fdBhMgIBDDEKbaSGiQU5lIE57tYMOwzs5%2B4m%2BVH%2BDc8ndDohlDwv4JRZGDXVkdzBYEwwucIeJOp8M6rhlRM8W56Slig3fqba3fg50WOYnv5mV8aaMd76E3uPHEeKrijD%2FwSYBrOxa9G%2BDjhvwRO%2BVsBbZmOikQxOfUvSF2MUSZKdkF3hhjyzQMCsWEiMIg8nitnXSEB6aVhWngcLcOFY7wWxDwAFoy4wwxPZhT2mwP%2BRieMszVFRG7KCrQqSLJvOzZdORTbG6O4Lxb0RsKQC7nyx8SWEwRIus8DFGcp3FD6ft6J94iagxDrytkX8uJxcjN7HLbkq2C4tfzWSWxTDQe%2Bkn0Lw7uxrTS%2FdR8wJfBebALv7foAjNLMO35ezddaKJCxSf%2B0EWY3GSqsXad588xD0rR8Lky1K0S1JYARqeZLL5H2BcmRKw8UFiKZwVWRIDF9WDj5MnNVPWtknBK7hxeOjDAx%2Be8BjqkAfpgYZsxCz4OUxtp14Sm1wFI9F33Ap4XqPCbAaen8naIDaQHTpnY53yOQ0SEXipN5SX96UhLeRlCLU6ets8qaHk%2BSfUWArSop0MCsch62T7KGm6sLcNoW7bTNxa26UEFnkNUBkvUwFi7i9eB4iU6mXkMy8oyeEkP3utoaxb6MEYMMW7hIBwK48bgfnQ0H%2FVDe0QjWCjZ4ugX97wdQO%2B87GqzuCZ%2B&X-Amz-Signature=4a81d6b10c2cbaa3793cda898d2275a9c2f254a12e0a7732bca6b4260c699358&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBFAWRH4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTe3ZsxE%2BScMwBNxc7aZAE3%2BG6%2Byz%2FpJyXIo2jc5GNngIgDVHGqdWAc%2Fvm0qZG3t9GgrsxCx3x9%2FRVpn%2BQ6lg8KvMqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuNWdLEns%2BdSSvRiircAxJGqTUBHpMlx%2BOsT4pg%2F9IrkoRaygGZC%2BODpp7U2GXc1r7Szzr6Ku%2BvV%2F%2Ft%2FnCdQAuLlmcq2%2FVpdqzYOypmXGc%2B4g1vy%2B7Dqt2j2nuKTT2v8bv8vBikwTPFypFGZCRtDHxPxQ5Xtbkvvl1jQoWpG3PPAgBDWY18ikaa1BzFDpLZavDStK6r44pV5QYcWllWFsIvB0TCa6nGWeGVwCeV9a%2BboPSERYX80dXonIYut2mIlTYsGsZtomfvUV%2F9AHAnSbcTj90vDQglH7ci3WArqaoMfsX%2Bv5bTLIDEobNPuxGlLPjUdSLCJ24HnsCOYyA4hp3F9%2ByUh5nCpipcTsPu8AGC0dKvIuocaVv6PRQyaxsVUjxT%2FeIfgHyD8S2ZuaWyt8RZBIURc0Pgvw3CeAuEWPBO6L2kukvMVJV6CiHtBl5%2FqvT5TY8VdMLt2XV4IirIWPZgAQ2OYlWksD0r2vwTPKsETxTkiXV0PF%2FEhO%2F9jxgl6k2cmMwi3aH%2FQfdVINXdrexO8jB7jwBw3%2BHn0ZKASi2LDe3IPl1aj7ZKRwi9cBwH8zl99D8WexItTQnTYHZ9FIWfU3o1V%2BvFeOGoWSFan6tv3nm5zrmadaewMcQPhBlcCGna%2FSPcPg5ygGlrMM3H57wGOqUB%2F4dIKjdle8OvmFvhhv53O9DG45eURRo6omk3OU%2FlHiQ%2FYOfm0yzn7Cokncf0%2BhuoowSwv5CI6%2Bq0k%2BwKO0zyC6ywrE182RSw1c7B86GLzFikgvdm9t2YR8wf8PR8TsjuYSeGT127Wu7sPI8vkswDjTWW0OPJ%2BgKgGWlRiycKw0h4cB4erxwg63O%2FOYwYIZNNk%2FLIPnIWfW1xUKkRrNoCYTwblsQI&X-Amz-Signature=a3e944853abf8425a2c48b76f6c732c99dca7fa1cd7e5f90a022823e96a3b2e5&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654CMQIPK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCxmNBoQLJ0Rqb5D%2BsC7kQwsVklYxJaPkNPhtG3yWMQgIhAIm0FujPJ7pUxcHuEha6KgKHnPPUzjsVUv4qRtnupCkvKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyqmRZ1lN2I2pmTJvgq3AONuPFJ6wiHurZ20u4MsZclkCk6759C%2B8UVrOHK4F4Ph46LQNIiahSVgtSn0osXv5AoKBCSajr0DOlYW8v7qf5M9BW%2BOBxHsw7S2NifDOrPF1SG73HhC%2Fd5xgFYLEZm%2BzcF%2FlP22ZOaHoq6I0X8atPNXEIafdiTpnubguaQ24kGNa8TB%2BQZs%2BhRplkbLPPjd2tYJmK3JEUJufyGcJXMJTBTLCfpY91TeEPZhkQ7LklVIuFUzXDtitBmW%2FTum5YNj2UoBanoYldyJXthTQo%2FvaJvhBTICvoJs2c1DI4gzSKeT7%2Fe1oh%2BzqYtDnSUW4hHMd4fhbeEBG7SlcmkDT8hgEXiEonW0%2BOPPRo9D723R9%2B3C9zfv7vTWyZ5tZcXaSjO55zpSFR4JWq0vHOU76nj17R4cG2%2BMvnxT9of8KXPcqD90MSve2RwJUSHv7qKpHHqVRL%2B0NxQjRDGDnQCeDIDFynamgYhNVpP2UMXCpCERlHWUKJpmeYGwft7Pgag45Aci1UGFHFIwdp2PtA%2BkW0iXXdbgJvoB2pU0Oksdep2y81jP138NKnw5xjF3fwvMhepfud4ymL%2Fz3lQQ3lk4e6byQT9gewN7msjBO5ADoCJBP8FL2Ht4KLZ799A3g666zC1x%2Be8BjqkATC6WyfAEMT0o0x3I4ehfhJ8jB48kKnQaUkrFldlp8evkdDRC%2BMy73X9eE5F0QFosHQP%2B7QF3WX6aQwGGuszi3XlflbK9vwFYKldOJM4zQpCb8Nyb3ILeSHFzP%2BUNlJFQPdndnCmsHcsgJubYbkDyUatGz1J7TqBGV5AsyBKaJDBBzBoCkbSJiiu0g%2Bxo6TJZWzz6QiwZsU6CVY2u%2FHXBuwY9pxm&X-Amz-Signature=344de96d5417b8eca7bd3decf6c76447888583fe3552aac18cd354b819abb9b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IKNAHDZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1GtcyiJxAPWfk1GuY2YFL5XvdiwLR4MK%2FQFtlzeTAbQIgap%2FRf0bMuiruzfiRYJVdCsAehpw1RvbjerBeXn4ZXVoqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIyHT5C5LVoLuDVpHircA2HEtLASAUkQ0PhCFbcGM6ndRUffZa8280yMDjn36j9DE5SwG5%2B2%2BxX0V5WAyxaoapF%2BWyMWDA1UY%2B1SbOihCM%2FdE%2BIEAMHJAoxV6J2noB1By%2FV%2FxFlUP9T%2BeYy40QNam3M7OKdCNS%2BX7aM2Y19Tuw2CHUdxOW%2Fb7GVKaXLXvK3miwQBnO3CYnqTskdHjmETAwOpG1xiGNcFeDxjKS3YJP4FShMeG9EeC8y42ktyX41RtFI4d%2BpEVotGHokQw%2FXgHm8lBTLB5IHB6tgzlAayJinOkmABeSXaWCH8fad%2Bo4dewGLgJuH3noQfHTjt2vvFpS1cHvQD9U98A1jmSGALtNiVfSBSJFMJCwwsmgGm04ieB10rg08dYZ38BpgERkSnsR8ovJBmtwXZHhQ%2FAf7T5ClJi8iR4ZXRJml0JRXu5X0ooWOpphM1XvXYGEcOWTRkhNBX8TBr55J7K2Ong32XLa4MtV75u%2FJ0DwDnA7pV9hwQ%2FQ3Di4Ha3vAYWdHsHHdbAJHT90kx2hEJUd9bCQ3qRPvWGcbqwt7msKIjvJnoRq%2F024VTDNDgbEaK%2Fhq6NJ%2Bp6OaQIRp8FINj1HO9Lsh2pg4Jb3jSF%2BAwITO42okTes8HmK3xs3DZWigTNKDRMK7H57wGOqUBllK2B37uAPNK5zESCjMNToT%2BXGGDe%2FP7osslOK5sjd2MI3rV%2FiF7rNh8k4GR%2FDdQDFNMgD%2BeDWkvqsYzJTzBq7KE6coMFImLA%2F%2BEhW1zXNUgSAKsqcNiFIizzX8HgeXd2idfpfIHsamk%2FkUdPoky83dlB907XYvjluy7%2F3BxP5k40MnpaO1KFjo5Ltbt5XbCipgKKqJeNZu4xxAlWGwjLkD6Lbel&X-Amz-Signature=ec4559a7095e1d86c84a7514d11bec73e9d74bb4960a0c3875a3ab2ccd6a2931&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2MW4AQC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEaR7tlwKR9dhjNNT9y%2FvIQQMcWhGmhuwVKkNqJmwV%2FMAiEAwn902%2BLr5QoxyFdA%2BQYAzbv1aGhe96Zfr5GZLPc3mEMqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK8ZR3zU7MdREKiS8yrcA%2FgEvjkpViM0%2BTpD8T7q9BCWEieMUIkc2KfpbkABwDbn8sl9naGv2d7uj1kFUYxcFLm%2FmfCQQnPExelinDs4eGxOGgpDQhbn9A%2F%2BYWngRMMzNcrRrLjA%2BVBW2ntXx%2FsnP9pjHFP4ag27%2FrQjFM6HJTLXzUhQVNsMhyAl0FfewXd214DFbrTTjAisq8fuBr5CEVU7rUnFd1A%2BtiIh9S7UX0k8FTro9vgJloq37G52KX6IoODHQEkUQzZmANvz7LsHRbQsIDr5CFuGhWQCV9%2FBxYRMNEnQ4JU8F8IIYs8b%2BVxx4CK8PuWkz6ECZJDclmAyV85%2B06uFL55O%2B57iVNOYaLkOBeQSCugahiavi5Crg65hs%2FmVUJOtvlKM61NWg2qL9iGvYGA0Ilv3THxO15ZLOR4rWX0yzKSTW4S2tLWvits7j98QmK9TQbRyGAk7DwhiL5jRaT2zK5II2cS6hCjwOtUlRBQ8IL2G6RZ%2Fw6rNfn7WZeS78x0f5VcMdqcALJzqLhEOwHWKkuTT1WV7%2BovXeB4M%2B8V5J2aUSVVIwYmQ8saZSbnMBUUFdFu8nrBLUOL5meGmcwOt%2BXXiuRMs9ghMM2A3rKjrkchCIwpCN0K9JBn%2BNUu6o8Z0vvqhSLSBMPXH57wGOqUB9Qag8S5dxv1GEJ9Aif6og6l1bLN5XG8a%2F2aishyNEYhxSu2xT0Akycjr39bpJft%2BQwbrZMnMEfrq2nJHF7xkX4xnXYxEDI3a%2F4QzvugV92TnFWScyvf6uyof93TcZratm%2Fo%2FHL%2BS0lSPZXjqynhcKEOcifp2mLUn%2BQ%2FBjm5iKvSV5dtBncfOpMhEyyCD7sij214rKq%2BiG2oSez7A4fUKDcN4Bsei&X-Amz-Signature=f01964351837abbbc66d4b44bcf6d4d913fcb774976c1d04b44e2f5f23d50c76&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2MW4AQC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEaR7tlwKR9dhjNNT9y%2FvIQQMcWhGmhuwVKkNqJmwV%2FMAiEAwn902%2BLr5QoxyFdA%2BQYAzbv1aGhe96Zfr5GZLPc3mEMqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK8ZR3zU7MdREKiS8yrcA%2FgEvjkpViM0%2BTpD8T7q9BCWEieMUIkc2KfpbkABwDbn8sl9naGv2d7uj1kFUYxcFLm%2FmfCQQnPExelinDs4eGxOGgpDQhbn9A%2F%2BYWngRMMzNcrRrLjA%2BVBW2ntXx%2FsnP9pjHFP4ag27%2FrQjFM6HJTLXzUhQVNsMhyAl0FfewXd214DFbrTTjAisq8fuBr5CEVU7rUnFd1A%2BtiIh9S7UX0k8FTro9vgJloq37G52KX6IoODHQEkUQzZmANvz7LsHRbQsIDr5CFuGhWQCV9%2FBxYRMNEnQ4JU8F8IIYs8b%2BVxx4CK8PuWkz6ECZJDclmAyV85%2B06uFL55O%2B57iVNOYaLkOBeQSCugahiavi5Crg65hs%2FmVUJOtvlKM61NWg2qL9iGvYGA0Ilv3THxO15ZLOR4rWX0yzKSTW4S2tLWvits7j98QmK9TQbRyGAk7DwhiL5jRaT2zK5II2cS6hCjwOtUlRBQ8IL2G6RZ%2Fw6rNfn7WZeS78x0f5VcMdqcALJzqLhEOwHWKkuTT1WV7%2BovXeB4M%2B8V5J2aUSVVIwYmQ8saZSbnMBUUFdFu8nrBLUOL5meGmcwOt%2BXXiuRMs9ghMM2A3rKjrkchCIwpCN0K9JBn%2BNUu6o8Z0vvqhSLSBMPXH57wGOqUB9Qag8S5dxv1GEJ9Aif6og6l1bLN5XG8a%2F2aishyNEYhxSu2xT0Akycjr39bpJft%2BQwbrZMnMEfrq2nJHF7xkX4xnXYxEDI3a%2F4QzvugV92TnFWScyvf6uyof93TcZratm%2Fo%2FHL%2BS0lSPZXjqynhcKEOcifp2mLUn%2BQ%2FBjm5iKvSV5dtBncfOpMhEyyCD7sij214rKq%2BiG2oSez7A4fUKDcN4Bsei&X-Amz-Signature=4d77dd8fb7a9e128973b7fdcdf11dc1a6fc47da4c44b53f723c2566fe76cf795&X-Amz-SignedHeaders=host&x-id=GetObject)
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