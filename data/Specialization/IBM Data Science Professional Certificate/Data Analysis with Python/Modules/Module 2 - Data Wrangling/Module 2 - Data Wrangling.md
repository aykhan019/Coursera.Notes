

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DPELDX3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BDVFt45QKbvR4W%2FKvyj6XwGRs4XbOLIQxqXoO%2BnDqLwIgIZptGqIOCX526erXPt91Ym4tRxT7lYUqG26J7b9qDVkqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFlu5XBW81QeXm6P6ircA%2B03i9hTXq0n%2Bl2er%2BPA2ZzLcvT1x7UuFWfBjtseifjr2vsMG2VWhUkEadrzD2qkEETxfVMu7kXbOmr3%2FcNaGFwLqEAb49FcOeGPvJKWgkTAoHX72C%2FkcDGO621j9q9%2BreqBkd9MdS74jFBr%2FuHnAxkI4g1KhbdM2bORu74idCyw4tz7xCjg7DRHT44tKB0IUC6STlSycPnA8jMzyQe87efv6SDjZlK58dwStKNdivwK9XyrsxSjGx5ZuRcIvWfs7HfxN4%2B9bLc37D1XG%2FoBofNA5k1EW%2ByRawVu1cGksj4Oh%2B6DU%2Bxg1eXs%2FoC22xUJODduV6QxtLd0dw81i2RLKsAagAZ61PxasgAmM57dKcHoLVhKzabSBvIB2LVD7hMZTRkv3LNwlYtYlG4MeSaDjzM5EjUZRMwjwo2ebZfuOklcQG07MO7xzHxW0Ckk4iNE5erxQqt%2BuDPR39JQAybs2armbTivr7WvKp23s1p5qyJkzGMC821Cn%2Bg7lHcbFRKllcsmGMtwq0eyyarRSg%2FFC25LH70lrcgX6EBylCPN%2BvFoET0i%2BNLL4qHlMfYaii8uUx8K7tVaoptHemuRKLS6791RFdHa%2BV8kBgwvdadusK6ztjg8L7ryakTRzjLYMIeA6LwGOqUBpe0iXcy8sVDUdRjetYdenk%2BSEzBZ5D78uk%2BprudP5vIlqsCNqqaagKLwz98XlfDSpJF7uToQC1E7wV9Cby4szUf9pa5tB8x%2BmAoVDq50LiCLr9EluJAOtxM1KicEJjKn0PnR%2BRFbhn6Q4%2Bgx5xDbI8Hju4l8RWjZp3Cfi9fbrGh0JcnBXycQfZ74wpOx06jidg1Kgl854BOieWVvj5d6dI54S4H5&X-Amz-Signature=383317d56f8f7a24073c768703636ac4b7294523668b59c9dc2af54e368a9016&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAZKZGCL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPzGBWQGxMdZ%2Fk%2F6IB8S3Nhx2MQhQn%2B8odoLg8BsLDqQIgAsRhmijOvK1%2FnuiPGL0zALy4F4kT2s86S0UkRbStFhYqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf1TKUvb3Xn%2FcxjmCrcA%2Bb66vuvrdYrNwEqcKrqIpjJXhI0ZLgXF7eVbS0VcQ0988V3ktP7LA56OtpLfKwI3tPcqqJkbthcN7iPH9cfHqSas4NqskV%2BzloIBV43NsPggPQUyyCnIRvetCB1fW%2FLkecNpKkhPWEs2gNVZPLU56I%2FMjgOyQA1BYullMRUdsg9rLDMB3Vh8gAeOKvuWVkEMfBaDcF5Lk3ue%2FnnMqlPE2l3uDyStMS9exiCkIqEydOGpJYTls3EGZ7G525erIrhxaBi4cjiDSGVJptUSedJUSPwLcvP2TmEB%2B65kEGTEf7Rbn0THopA%2B9U82c7XHc13HWPVwbjky4WVP0FFuAZ3gc%2BC26o%2BQNymjCx4cbqRn8Y8R4gJ60TcNJr0UPvkFW9nlmHJ0Kmt5BBi7e5rCJGTzQtR4XusobHJe7H%2BHN7swaeZ%2BGu3Dr0q58F9UKqk4HNl2bvJdkG0IuOteG5HglzQCDb7lgOskvwEoWEzZ6TIYoShLqVL2zsiOD47Sqq5Th%2BysMRVZ%2FKsH3zl9gP6UDLKBnwcFBNP8n8Mn9KQd8eWDM6AmrmZjUR9tjk4Hoy3EmqFmfqLUvVG%2Byjy6vFEK2bVHFf4HPi7QxF9xE%2BugIYMWtdB6bTriiZ9gInnXXpHMKf%2F57wGOqUBPv5nZyPnIR12I1Gyfjh7XepWTjJ5PLvvS0iHtcrH00r2Hh7dmD6otepZAqBSUiFQ%2FN1CaMsnarWTj%2BQsTGV0ZnPjs1s61kAv%2FeZ2Sh3yTSraYUlVhralfhsyzG60yoqsPlG71v8sBOaT4qyDnCh%2Fqe0sLBFrrHvwl%2BtYG22Yv0YfgFel1SqTiHZ2ngkEstWliwj4gebPqtX7Lw84pDKf2Kc98IBs&X-Amz-Signature=cb76e30d7ade236b660c8d2b34b61424a1635f93691f8e3c269ebcc872c501ac&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6UFSREU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeVcUGjwOKJmBS21hNnClYBYmtp69ndp8pNRsGHFvHsAiEA60dMfUhGWL3mkVBQODh2RofTHVj%2F6se4Mh4ppKMxQpkqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLV7JsOv%2BoPfdIVWSrcA4E%2F08o6Zb80qFNy5R6kug8uW0Jebkh9%2B1fuQQ6KR4RtTUPiTmsYaZR%2F1K%2FrRYnCPcP4NAUjqy75F2ZwrJN76erfUu2AMPwLz9UPmE5VYeS%2BgKoiCAqJdEYMwAJU8Gjxys7zLCBEVWpPqP%2FOqX1Cg7c1JXig05gYLq2UM7FwhH7TeT80lBmVE4MuGqWsDSmoQUQo2FVVbLRdq0dr%2BoKYMvdzJhhk0rbXWxkOWI74XilWTCQYR1nACbT41Z4oeNiHo6CfYnniAzB%2BN9Glq7uyJ5YNLagSDobvEktQ89XsbmcfmM3Xnb%2FNs4heiFwAxJrW0bpUD%2Ba6uSXvFQMAK0J2XodIsfjKH0Qk0VJrOkpfnBbOIz5OzQNom%2Fgr3eFC36ixYuQC6NDlbykd6dDjkCeRDkDBbPn7WvrzKT666tbtcLEYuqGVwa%2Fn%2FhjR2Q%2Brs2%2FdBbSe1qmi9Hvr9QsMS%2BCCsZTQUEmuUCJPu991eOzIiesz%2F4DiLfB0txIwXIl7rKJpyMeA2hPyOSjSsQUhJ8dN%2B4KExtRfb9qtZb0AMDygHGp%2F34CSyymdJeEgeGFAcFU4XtgddqxEgpLRC0hfsOSh9bR%2BLAp399AieE8SQM%2Fi1xQvEiz7HDQes6pCZKbzMIP%2F57wGOqUBbt9K7xEFFb28xDiKIbRnff5dpc%2BguQRxDo07CWpdYLE4GGGVAPG6X1IP%2BQ6yfWN5G9z%2Bj%2BkewrEh2VtVvbmu6fMSNndlsngZrZY5uQLU%2BwwrrfnCw9lzradULcwhEbwE5xheHQxab4qwwf85ujcyn%2BxTZ9F2n40GZKejJ8GLY%2FsBIN%2FwibUgIofcveER9Cpv9K92WSlRF%2Bn645o9%2FtatWGB2viTW&X-Amz-Signature=6d6fd1c455a48f97f0196f6a46e7360ccccb8982e9080713e7030301138c76c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNUVTTLY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FWpcegMRrEEg%2FsEhFp%2FaPXC1hDxv6RsA5BLiLjvozNgIhAJpShGwYfrqItL3mg5rKa3O19pcRyMshbmAJLhSbe1w9KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjCiFiACZoqOcKaAQq3AObnIkRma73rC7jtlc7P6GJiAI6Ih%2F85R1wcQoOlAIOPhvdI8YiAImDMwxDyWNaCBodB6bQH%2FCWUaG7i83vE92M01pGcoyynd29466hdTRyxsvswmddvg%2FdNaSpao6de8HdWgBKztZK3F7RjgrllDSn4f55d2jfYkvZANDv3ilCKWaOszlOt7ltT%2FG%2BDWO1grBIPbIikYLNqLnmweYhYTMLTyBCKOjuEb2WnXQF5d%2Bfx%2BD%2FsFZI7y%2FfIdkYjr4GpZegdk7Gn6geJ78nAggiGZwfaHEU%2F7cX%2Bs3WWsp2kKqLe3y782w7qgFMVD99Dz9LDSbRBsPHpsNqOAD7Y9BeGDePtqBLCl8D3FTl5woPGt%2FuaY5HtrcRhjeeUei5PnS3qFqf3duo8Su8Ni9VyBTn1Gw3Z1a9Lbcd9n6jDm9Mpb%2FxLkAjagIw9WfKFs7b5yYGDQop9JpC9vH2vDc3GE3Om73nYuR9un3srX8lsEMkwjQE6Mv5jmTU%2B%2BhATdWTw9VvjbKND93xZRRbKXroKrOzrLq%2FWla3KoPghyYco6lcy4py1GNwrBCnNLTtvyxWFJ7nPsX2bA6pH43E%2BS2yXwrOjggQt7nnTgrMC2YbxxnJOHSGItgAgc1drdDFORZ45zD5%2Fue8BjqkAVnFN28S67Iq2nNPkUQgjvGFfh%2Fev5hkLfcIOcV5kd5yuryMoiV2d7KtMI8jBo8WKbKgD%2B26%2FvxGioROKUSb8sSs3hvOKrT6dYmHSnhPxUsWMaLffFXSsSCyYriz4QPbqIOfq82EahhEaZ%2FdWkAQiuEKQM%2FRyAS78kQElLKnS%2B8Y2rRazzBQcuo2ncKZukMnYtQczKdVs6UKAocAjbm%2Babl%2BHG48&X-Amz-Signature=51a21e80e1e89caa1419e956775ab550578b0783f8aee64ded797c002a5f856e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USDYYA7K%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZpZ1qcZEM7BWf82HID%2F0podVDY%2FpLxi41uex86XXtRgIgb6FdrAe6YmGlOiZAkCwQcaLo6mrkB4z8tqlVRbhdEswqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDtGhHc0%2F5GLdYKbeCrcA2M6oM9wqQIPdrRPFGE7ByFoPqIT3J9QB1xdXiR904TmS6TtppMEgyZ09AB29iFZCgTy5h1rdT10z%2B4RSDQbipXzgFXsp8uJFtrWolfp4kybfDM81wPBFoSIshM9Xzs2bF0sdQqeVxG%2BLZUqMzLMmJOT0%2FQQrx7THGQbl9bda1OWZ8U9k5KDzqRDbDdzTDa6cNUIa%2BLIc4YzrZozb5AA3Iu1frXbiK85O43k2ckiUupVqpj4GmkgM6m0ci%2ByRRTbiy0Qy15%2Bws71dyDpMFFC15nWDxaA9rk9WHiAP6%2BhMJVXe32Q8rMx1izPp8p7U4Hioo2hD%2BWCU1NBPNuXejFfA6X%2FiZKBM66QoOmAUVDygsIYardKwxFWCYA13GXev2w5pcDAnpRJyBhvscGtm1dp3QQeGExdW4VvglhKMSbcuwGgOjn3ND0AIlwCrmgcPLj7uLk%2BzfMI%2BsvkONTqzZF1XA%2BFpGaAGEiNrupFTOpitoEXzCjhNssQBRxgVsAIqlU18rUmQPUaJCimzDU16BqgTLgG3RiRXzFCYJUg%2FKwlYX53LimSeqespeHST2DNcVbxd8hodHBEBAsglC34e4eK3c0KnCTHklGr4LMW3CDyrMBzO%2F8LW%2BcNN0vPg9JSMIX%2F57wGOqUBoHz4sGGuUamcqgAtoAmGRC3wSeqNd397aDPWAUCNj1koZTIz8QtRU%2FtHTKcnNlBh1AmWWEIjuPhEuvTUONFDaLEPnBnmxZNErB5UUei7r3Tokmtzk6iec%2BvGEq%2BJbCWaesWz%2FsH6tcTVFvMRMqcD0XYeFnQWOklFeHHnl%2F3qbZYSOVQLd3W0zvKu1UzZt7QF8BPhPX%2ByRt43N5HtkjZuBgVDRnZl&X-Amz-Signature=c8cde1c63c8bc23a2cd257a5b3df27111ee2730c5c26d3eafe63da63dca03ed2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UUMO5M6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxtF7mkaHzWU3%2FL%2BfquYlMYzycy1rzExT8AHCh%2Bn2ZUAIgWe756sxfYpaxI6ESK57GC7ama2GpYATnI0LYLZKG%2FD0qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKJX7twsOU3CpUNgtircA3ERrkoJ4%2FLV%2FCqEn4U6v4K1Ilc4ui6Z8r0qdZx39yiZ%2B0ULkAognt2mbKm4EsuknXkvMSR8Ft6pxg%2F1uwSmMSvI%2BuXRYXfop8q6fT3k8WI0MzQaYfB5OyOpsBmVzajimDOv%2B5aDDYOSDY17BEqojqdoMkXpW8cvyec0xShM2T%2FytOoINazj90dU5UPl326%2Bt6rSqvMPiqzLnzallPz9EnTs6z3k3p0Cn58afc5RVsw3tLHdC1nCYYtyZF7Ejd55WHPG3O2ZuWuLavswYCf6%2BXqVGAc294Yg%2BmYXzHh2Ol92qJ06bO8ALPudJYkQdM%2FKxm4aAlNWHzCx70%2FUnTAZfMFd33tI0zuo6IeVE63sQ8gXFlFdYP1yeHrIwQtDJhDT%2FUREyC9b4sQA5NftawXblw8z%2BoEQmIDmKjrmKKPMwnIyeAHH5ezxQXFGD3OaG273LdvWJzJar0vZ9YiVKxr6RrkC8lipc%2FPxhgIcTiXOBBfnDrOabcNZsNPWmr8Q%2FhFdTH2tFh2O0TsJ1utfLnAwmwBBqUqapwh4gXg3yAEUAIrk8eZN9YNfGF46VaB8zzfF55uLojTCpV62ql34yvF7uj7zamwVzBuBx4GVCccP4ZLv%2BfD%2BJ3bHz00i9py3MPn%2B57wGOqUBDWxFvRAUvUNJrr3VlkwCFvV1kmtbkR2%2FKe7ZZqa%2Bzja%2BxGHMpdkypERY5uhTzT7M2fR5SwJroZXl9C0Go3MihYvn%2B1npmKSNpdFOTd%2FHKYGBVOilJTsjiqJlvucIKuagqqZ41DzxdzfPbHLSGhWA%2BS1IRBV3VmDD7is2p04ucsZo5jCIPThAgx4JTE%2BAhkvxM%2Feg2lz%2Bu%2BrYRGSRApCRh2JLPwQp&X-Amz-Signature=2832ce76d5d26190ec2f5c3541442c19e6487964524a44e08bc017ffe608a4fe&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFPLT3RG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8LOkXFPNC1ifiD1trxLiQXpTzkmkpXZKh0FpxM1PzcQIhALljXsc2Y%2BsaUnKbJKnCiU0gbNm3VHnBjkZjQIcgI4tOKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDg0eK%2FL8IPZCB9j0q3ANMSYpbboSzUp8aDEh%2FegugIKgYoWajMtDA1INh2ctZEKvYTB2ioZHXmW2BQ72FCkUeY92kElJP2qz35qQZoIgBnyCd%2BbhX%2B5CxR6R5fkZ%2BASECkUaOcyHkNSk1WtG9t2nRNuy7LdUku3RLdXUrPgF0AS3RiqtIgg4Wzd0caOpfhbRLYJpYnYATILS22k5Wk7TK6XSharOH%2BJrupAoxlYS%2BshNZAbHop67xndQ%2F%2F5eBTVXKodTkriBUk8J88HgCAsvfGessuFrmf5oplb96F3mKvxZ%2BRX8q2K%2FhlPw8L26mn8TFueBpGOwRwemeXsyLfF3SSJWyt6elbbxuD4lH8TovYb4mmrRwIEMuPLjTl2QtkCKDHoXSt3P%2BFxTqR%2FCxt1zklVt277VV0TURmo3G0%2BWveYd3lBuvDHc7ajKSbarDpTV4PzdV246eGwT1u5Fs8WpyhVhdK%2BdW%2FHH4mG9o1D1QleOCbt9%2FmlBy18ig6vOLOvqKNo3NubCTlxDiBwSyd%2FLyv1aER7NyRB%2Fvb86KJ8%2BTg9BHeUzHrlxnIPGH4xRZ318iIqkOPxvZnNPkiB7SfysEdJsuU7aHTSNZFjwY8qEccTRMU39mUgCJhSWjVOIIdjy2KgspB4mtlEV5vzCe%2F%2Be8BjqkATFUfmNcynEMAKWqzMGKpuQUyIZBd%2BdU5nHEmpRfdJvVcb5oMKnmbS0bAXViW%2BugsgYZ5R79AHt7vsh2C%2FzumXEQ12w%2BopORMrkY85fYcfJAEA2ZJXqxLkRCkOJ8tuf7yvUGUGmxMvGANLZoosJJo08FM9acpj2uYF1Hcpb6VDjw8oOP0FVR16cSYrt4suJGRdhowW%2BOZaC%2B0%2FWAIIBV9QtRuwCd&X-Amz-Signature=a458dbc8b80e6178281b84a4afe034622b6fb3318eb75d19fab17203fd2e42db&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636QU6FVM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIASPlfeD%2Bw9%2FfyFGfiF8DJ0sjBiusv077wRfyFHpSaVoAiEA92R5JG5vMVk7nDbOI%2FL91fEonvV7rt8G4BfIeuoZPM0qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMJvaDn6Gz1Qw5i%2FvircAxz01rNKkgot2k48S5ba%2FzDyH%2BJh5YTY70CHmmP15DE3bhHFA3fHdPKtGIJTGVBDr30MpLmEg9xNv9%2Bbbmhmov0HfdbinwRPxrk2wOUO7mfvRMRYC%2FA91PmLzUitRjOgFVZ9ah1ErSgrE8mCUcLYSVVdhasDiIiaOh1BL4j3MXMj0jMr9spVHjPjQqLX8I0vHU8vVtdEBrsHDCfYpKC49FIIouAEhlnoLH8W%2F58WTIoOwyZ%2BNckKVnzFR7MwbZndNIJCaQfpsVHLWL2C9es3jMoYCebj6lOVze51uzg8cCngIlSx70R%2Bc0oo6OLWgedAVIkCQEFxf86GOTIGSkw2yzqmonI0Jd7aFDPHacB60l3ZqYWvWrkOxlNjt%2F%2B%2FihHMKa%2FRpalup0D0ZcPELp01P8flPHiCFxnfBFMuqB00DvvY%2Bmor8AZ801kCygOkEgbc%2FodfWtmyGQxwlmT4opautxvQmdV9I6sjHe1kFRSWX4llTakTkcBSPNDUqshb5DohgeHuhPO%2FcELlMngkUdMcD9d0EBJ%2B7cM37J3SRfu%2F8n8u7ILtZecmXxHr%2BFgo3%2Fe4vRlcLfVE8SnMJXumTxZAPWs%2FP9Nwh2zW53dMuHY6DxK4Z5vrgRpuKDbx%2FOHPMPH%2B57wGOqUBb7spsQ7PJLnqx5%2F4t1eS11KWBqq81jRK%2FKpeR0ZVg1hhFjBonSnY4KrHYqlYW8FtDPfAr5EcT2TYTWdj14iw7MZlFxqzMUD8B0zuEPM5%2FKT%2BT1anrQp2P6PYUWG5P5%2BfdX1SOSE3nAAJ2x5UDk%2BfhOGM0j%2Fpqx42kkeOoF4j1UQRemBdrMNBUhG50NQm8c1HUQl4YXZZkmPh05wnjCE06StKamac&X-Amz-Signature=a9099f34eee2a79751e8c03d79212791b609d715e094fdfb6340689aff2de846&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USDYYA7K%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZpZ1qcZEM7BWf82HID%2F0podVDY%2FpLxi41uex86XXtRgIgb6FdrAe6YmGlOiZAkCwQcaLo6mrkB4z8tqlVRbhdEswqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDtGhHc0%2F5GLdYKbeCrcA2M6oM9wqQIPdrRPFGE7ByFoPqIT3J9QB1xdXiR904TmS6TtppMEgyZ09AB29iFZCgTy5h1rdT10z%2B4RSDQbipXzgFXsp8uJFtrWolfp4kybfDM81wPBFoSIshM9Xzs2bF0sdQqeVxG%2BLZUqMzLMmJOT0%2FQQrx7THGQbl9bda1OWZ8U9k5KDzqRDbDdzTDa6cNUIa%2BLIc4YzrZozb5AA3Iu1frXbiK85O43k2ckiUupVqpj4GmkgM6m0ci%2ByRRTbiy0Qy15%2Bws71dyDpMFFC15nWDxaA9rk9WHiAP6%2BhMJVXe32Q8rMx1izPp8p7U4Hioo2hD%2BWCU1NBPNuXejFfA6X%2FiZKBM66QoOmAUVDygsIYardKwxFWCYA13GXev2w5pcDAnpRJyBhvscGtm1dp3QQeGExdW4VvglhKMSbcuwGgOjn3ND0AIlwCrmgcPLj7uLk%2BzfMI%2BsvkONTqzZF1XA%2BFpGaAGEiNrupFTOpitoEXzCjhNssQBRxgVsAIqlU18rUmQPUaJCimzDU16BqgTLgG3RiRXzFCYJUg%2FKwlYX53LimSeqespeHST2DNcVbxd8hodHBEBAsglC34e4eK3c0KnCTHklGr4LMW3CDyrMBzO%2F8LW%2BcNN0vPg9JSMIX%2F57wGOqUBoHz4sGGuUamcqgAtoAmGRC3wSeqNd397aDPWAUCNj1koZTIz8QtRU%2FtHTKcnNlBh1AmWWEIjuPhEuvTUONFDaLEPnBnmxZNErB5UUei7r3Tokmtzk6iec%2BvGEq%2BJbCWaesWz%2FsH6tcTVFvMRMqcD0XYeFnQWOklFeHHnl%2F3qbZYSOVQLd3W0zvKu1UzZt7QF8BPhPX%2ByRt43N5HtkjZuBgVDRnZl&X-Amz-Signature=3ca7576af7f5e96e1259ab0a987dc72ca70546c0b515ce38726fe052f3f3acbf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA3P6CXK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBltLQFXPxD%2BFOghWmHMip6c%2FktpzR3vTQgIhkjx7qICAiEAmdFFVSFCLgYz0%2FR%2FTFbP%2BHWrdM2pvFsO%2BHeW3m9qNMcqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOY%2BPuZ0oIjKb8E7%2FyrcA9bNg43pGXcFuX9VmrTwLPquaIqTNcUbM0XsGHmrwvihsM4%2BE%2B1GaorBOQFd8Q3dJviNZsazbgFLlYqxuilDH89HSgVouoMFD%2F0E16Ee6cGheRHN79Jlf58xpJG05g7iQQVno63cW%2FM7q2z5Ww3Hjx3MsfUKP7miZVywyJcPOoyGPtdrRjjALcwwUL66eYqLOgAYo9SDCmC7bsJuCOtzykmul9OrEWt9hIzSw0utLShjGAAzj7jfDOe%2FmowWrKXIm3%2Bk%2F%2BqJ7VbLGB2dIv6ZUm7h6%2F5y1W1BYjQ4r%2F7%2BKLFG5S4Pna5nhMBae9%2ByopT18JaT4uGs4KZNSGpYipSXmJ2jpQBOf3a0PE3I2gdadLvn319qNoSJrNs3qSXecLwXJugElv8PBQwDhgLGW1tX20TXoya5ZLKXHIiQQwZ9N1YfUwIjby39qGFLh94yIBf8Aet%2BtzA8kDmloddPH78pN%2BQCoEArtDw79quPdjyZ0QqyutnkJrSBHb4QfH6nceaw6XeQjRMr53NnXbaLIFryiDyKpXWfrBdn1tlwr5LBtIfXfzdvWOZ0rMNyjA3sE3zIN1kIMuYFi3b%2BstaduZvXUlpYwjY4DpvmvxZSHkUZPc6FKq0zowwPkqT6bbzJMMH%2F57wGOqUB7IGL0GN4rqlCLgRq7B%2Bv7elc2sBWwjB%2FVNiFT7%2FJB332jgJxYY2XD9%2F2cByqir1I6Em%2Bt5Ucc8MMH6%2FyCRobHKv7yusJhiAkL9epa1jnEjm7rq3xWk7nCUBqIkbUadBeurnQBmdAGGGEWHIGdSlonkbnAk6NjMdsYwYfJrptBfpOqUusEhw04H%2FwEkrypHjilNE1nWnruL%2F0RTi4HqHq7qklQq6b&X-Amz-Signature=d7b620a4bdca3270ef650030edaba8c37ac2d2592b9bf0b2d5cbda7e785f6502&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA3P6CXK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBltLQFXPxD%2BFOghWmHMip6c%2FktpzR3vTQgIhkjx7qICAiEAmdFFVSFCLgYz0%2FR%2FTFbP%2BHWrdM2pvFsO%2BHeW3m9qNMcqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOY%2BPuZ0oIjKb8E7%2FyrcA9bNg43pGXcFuX9VmrTwLPquaIqTNcUbM0XsGHmrwvihsM4%2BE%2B1GaorBOQFd8Q3dJviNZsazbgFLlYqxuilDH89HSgVouoMFD%2F0E16Ee6cGheRHN79Jlf58xpJG05g7iQQVno63cW%2FM7q2z5Ww3Hjx3MsfUKP7miZVywyJcPOoyGPtdrRjjALcwwUL66eYqLOgAYo9SDCmC7bsJuCOtzykmul9OrEWt9hIzSw0utLShjGAAzj7jfDOe%2FmowWrKXIm3%2Bk%2F%2BqJ7VbLGB2dIv6ZUm7h6%2F5y1W1BYjQ4r%2F7%2BKLFG5S4Pna5nhMBae9%2ByopT18JaT4uGs4KZNSGpYipSXmJ2jpQBOf3a0PE3I2gdadLvn319qNoSJrNs3qSXecLwXJugElv8PBQwDhgLGW1tX20TXoya5ZLKXHIiQQwZ9N1YfUwIjby39qGFLh94yIBf8Aet%2BtzA8kDmloddPH78pN%2BQCoEArtDw79quPdjyZ0QqyutnkJrSBHb4QfH6nceaw6XeQjRMr53NnXbaLIFryiDyKpXWfrBdn1tlwr5LBtIfXfzdvWOZ0rMNyjA3sE3zIN1kIMuYFi3b%2BstaduZvXUlpYwjY4DpvmvxZSHkUZPc6FKq0zowwPkqT6bbzJMMH%2F57wGOqUB7IGL0GN4rqlCLgRq7B%2Bv7elc2sBWwjB%2FVNiFT7%2FJB332jgJxYY2XD9%2F2cByqir1I6Em%2Bt5Ucc8MMH6%2FyCRobHKv7yusJhiAkL9epa1jnEjm7rq3xWk7nCUBqIkbUadBeurnQBmdAGGGEWHIGdSlonkbnAk6NjMdsYwYfJrptBfpOqUusEhw04H%2FwEkrypHjilNE1nWnruL%2F0RTi4HqHq7qklQq6b&X-Amz-Signature=dff2d81d0ef851559f3b2d59fd44769f97cd05c4d6fec16532cc60749001f263&X-Amz-SignedHeaders=host&x-id=GetObject)
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