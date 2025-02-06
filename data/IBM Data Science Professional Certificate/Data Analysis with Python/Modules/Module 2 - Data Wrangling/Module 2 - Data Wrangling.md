

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ICLAUFA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIH38vXusfqult4pdvprgYPLcyv6vwp9TcE1C4Sr%2ByXIEAiBGDDio2S8EiUjr3bUmGNw9FqZLEpsThn9jGZOsH%2FdRHir%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIM6nSzkucWFVar7qH4KtwDcLNL%2BXo1ShB64Wq01YDJGZfYO%2FF0DEuUUGD9X5hSwIiPcVFuMsODmriJ8xbTDcMnTtwme7XMk8HIm4CXZqAai7TMNC1A3eO0YT1GIXi32ncxMo4CKIHrg0t9Ooa9CtBB13yxGGsgUS5rcHi854tJAce1RyUYt1vIYYCpkyqDIlU3FMUdRh67I1T25egJwDoiYDPN6sZYpTKtNAjm7Q2HagAcFK0N1TZ3jvNfiaCwNMICbCwe5tM6%2B0zoQmTbjHpH01DV6qzRBVgZvOJ85crXxH%2Ba0xCNt5R%2BSVinVYAwkstSUtwFroUDuMbz7BDvxPt8ifdam1IuKxHVEHjQ53O7c3pcYydCXY0JxrfcLxGL0f4V%2F9GnRQqIpxPd78dE%2BObWG1aagVAgdZLON%2BdpTtvuTU4clOAvMVFvqrltycVkE3fik5RN9Vy%2Bw2Ddu2rNWmPNKEKbZrEjqkKS1F3Bea0ITUb4%2Fc0MRnzWNgvVSc1og5Rny4QGAb5nuVG6LpNhpvY7jqGRj7%2Fv4wIzRZWMR8u7EUGDKlckuYZw2L%2BZtPZe7Jroky%2FJrmepr0toqfbBW5goGu4u6trGtBM4kfbR3GSca8gqTp07Z7X8SL7%2F2%2F1m6iAsHmYDNje7CpfjDWww4dGRvQY6pgEsHEOryDpORUjJ%2FLzWlbWarxkIorDmaCp%2B1MO%2BgKk1AdvqhnwmIear5ys8nqBVM82wGDaljMp5LtJ3ai3%2BCQ6BaImgb3LjZRbP0PZkplhX3ryXxmaSYk8%2Bax6JMREUZFjKxDgD3pazKe8pvzJ2oNwyRXrl%2BoTbUPEYxncyGxYdknE%2BgPwiaeU3HSGO1NeSX55ZvNhkPGG5GyY%2Ff2VcHj3%2BzkSwStVO&X-Amz-Signature=67cc4c3a991d00a9e7fac1c1ab1c9eee4989f7ffe24d33ed81b96f5dc4e52feb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVFZZIQD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCQhyuqU9p7WVFofpDNR3PXgWgyAK1%2FcOw%2FUCMPYONsSAIgBAzGROIhONojpEVmHchi47CtVu6BJAM4HJcudr7tHdsq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDMQnLZkKvPXP9cFEvSrcA29j%2FvXTaHWhXIPpoMGkAjjUWGdQMoyDLW0doybYrAP1CqJc%2F9xwXDzp%2BBXmyPBNAeJXNOT%2B2WEFbVUHfrjzErVSqkhNVZS80D75bt0v77NdCzx8UVbDYyInj8TNmwwjHmVrQHMnNRJFb8Nn2MDlowNHF4aKgrM7ONTlmGMnpckvr4wR5EbHXy9q0YIRxBz6og7a55pEsX47fgjbPZ7t53G09NtMxcZk541mb%2FgMsB%2FyYH%2Fc5%2BtAFyShOex7olhWAbDsmcGHpoMzpW8d%2B0emOsbN7De4cmRs%2Fghq01qSE9qJuaTlk8i8AZjqFBj8W2QEOA5rYeVDoJRNhqdDlQMQv0VYqhrdGy80NJyjvzxkadDW4V0S%2F4ipK4jUKho5El1KIRUs13szdSomckyPLtOCZY3pNcu5BzcHhzTka%2F1QKuTdROK6ethkRutb73SDZDZ8Bg%2BJS1Q7v7SrA5VaovQUk%2FvnfcUJqaa1D9mgVuPi4XimwPWRcgAekD1lbQbf1fOjcq66U8o2NEqBzNeA9YGEDp%2BeVOPre8Phg0m5Eccyg4wrSQl9jSu5r7BBtIxI0Kjw6E59rh62qfACcfrJH2c9LDmwywxZvNoDTsrrtcOoWie1DElCy1oy7PmOogEFMLHRkb0GOqUBfNCVMpBWeZibxNiLYVOBGh6cMAqOK%2Ff5OtIbfwi8obrexzLnCJQYsopzNcTaHakEyVHR0uZThXXE2mB0vFfh9TmAJtB3sEhU%2B2EySgrf7CZc%2FvFJPuWcAUqMrpYEy%2BVtQ3xmRvNCXjtf2BvNQbh3AYuu9qo25BrQRbgDcr0UAytl%2B0f28zkM2CBBFCQXp0gampouP%2F6d7RV1GCksLHrVYBBppDsf&X-Amz-Signature=62542a59fc62e66027d4bbb32d54626a32b945c793a63caae9736f8c4fcc5cfc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5NZ5UCJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQD%2FJHxnjX3Jq0%2FD3e9ZAS5%2Bj%2BDMe9aUeF1XhXRMM3SCuAIhAKn4ZV9rXFkuFyWLffy60%2B2J2MGyrNFa1shXxVBw3I73Kv8DCFkQABoMNjM3NDIzMTgzODA1Igwa3l%2BeytLNtxj53J0q3AOaF7s%2BIKw1y%2BM4yRUdcOtlxltf%2FFuVXM1fhkE9S2RkmlqESP60sBxAKvrvQqEv67G5tLnHo6EdHlWUZxKHbd1Ed9qljpibHj18BhUUk3GmPadauZqohbJBg%2FLST%2BoQGLgY7jykb4MV3NhhAlaTQ91ijfdyD9VWyuyu8ciJLqH3jmkhfgcRERE7gUvN0d3eCQLoQF%2B%2FdlmucDVg5J4czaLxKw%2F4sxTvDZ8PLXQ%2FkmWmAJ8Kdf%2BSsHeMiNPJ0bPVpWg%2BBOH3odZr1yGG%2F1QJyKpbjX1vMfufWGLXQA%2Fgk2SavfKeH9trAJPB0V7eIzsJVQr1bu17HUnRBRlcGcbOqnG1qApbj5VFmkzi35Ek56Yd8fmkmhfwxhmXMQpLSzrYLSexV%2BESxejaQyb%2Bc9VJGVbN7qpKvGGxn6u2L3YKUvjwrNE4JIUalDF4pKi81uDdVvUA99Nn0XWYr8tdG4gQ0wD7ib5rwkVChdFTL5jfqvOFtd3MbxsyEsUsPlMZYJdqfq0J3V6p4X10WNYwhGNKBzInCMwksKr2F7SXHuyaHgo1cnr1GAn%2F8DvcyoAjPnBKjS2EG%2FLCGFv4fZz5SEjFgB0ZdRuKXHPMpkgnmkRBSH2TAhqHbppOiuCzgrTiCTDh0ZG9BjqkAS5mT2iQpg54DobeGPdglBrLgyXTO7fKw7qHLDAPP4QKxTtr0SF7s%2BFZvhCXAmuz%2BXOZ1FpLcAFqLmmBnqg0f4BlnOGMpLkVNQIDL9QJkTWkKJqmPw7obBLUKEJ5bIo9SG0th6nmJkPigc84gQbSAF78yy3NoiQJn2QQZg2INUibKwFNhUCPy756DXR3J7HlFfalYAXRvTrTzJ4g32%2F3yJLn0TBr&X-Amz-Signature=789557827a5ba3384bd2e79a38780e63710f6a43fc8bdcbc937535c5a8f0e4d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMWQI6ZM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAQy2TuD95lG4eIkNxvfLd9ihuqcud7jOxU3jIuohWugAiEA3AKAw0bABeNoQQhSd7H7WlSPhgmNLzTLz4FiZSgVp4cq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDJj0P4bUWX4jMb52JCrcA9HjrZIUGHlYFSm1BTLsPknj1z3LqZ0a0t%2F3zXovgCJ%2Fe7vGuxGZCkCmt9eMEwTGTgNqew4zrPpuYKhkmzt9pnga2eypcEcoIgjp40Tq%2BGxbaqUFNHECp7Iq0pc7WHwQx8U8s4Yv8g5p00xa3Qvr%2BU5IeXEv0SnL3gVLF7dND3hJThxvggKwrnRXJ1eJk8GfdTM6klL2yfry%2FRnKQ1KVECKADtb8BjPxZDRvnCTu0TSP%2BVlUqIKUXCBrROT3AUynR%2FwjOHpJ5%2F7kiL88StMPKXnS0birqLz8CgM1MINH6nZdjBwiwmawa13u%2B3%2FUAegO%2FfO69athZ0Ql889vC0c2Rk2zvVXtBw6nytCeYWNoT%2BlPDiZ6GDOm%2BouM45Mtvev0E%2FoYcNN14OgB0%2BoZC8cYAofRr3nxnirrDIuuYnGdes0%2B8itOWe00GS8x8XtUFtr%2B9X21Pauu1waFr2AgTKy%2FLLJy2BorsSinT3TbaBnwd6ouFvoxbeFIRTVxQoAkQ89OdSAGFzWywqQ8jU1567ik4Ca18O0YxwwFU8GXxtrHR%2BvvM13P%2Fq9Wd7%2B9viVXQpHjnI1LvEf2LLKVeVmhQm8NAyoA0abFzsrSFD97nvbCjWmQCqXcj1sB7l8GJHIGMKTRkb0GOqUBXi42Khvra719%2FjWDkVUFPYfrQaFDRI7J8d7bFozuXjDNYNB2TIruAKw6vjRno79cnzqx6L3zIrZWAeZSPQPbuRaQwsYpDgze6V8TYRN2KbgQb80Dj5HjWDBcpGeYTxX%2FWvPXW%2BRgtOpuvQlgldojeeXRSHWCKH%2FBCQ2PLEOnDh1q0nFdrkXzmBopHNYZ19U%2FXdPz%2BeIGc%2BmLRLEcqmp2ST5YKphu&X-Amz-Signature=ec3ed7a8806f5e0351a0d177fd88652bb2be98a5c61b2c245c06b57deb1dd5e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6QU4BHA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIFo%2Fb32IBfi64Q1HA2%2BUsIOEsVmc8JC4u3C%2B7OEK5HsVAiBqnQ7NXvnA%2BoIozK3AMRBdK25ycKG3V1cVNX7ZufS9ESr%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIM7OPTL10sVKwYwV4JKtwDqDGf4WpSV%2BUV7i%2FbcKzdvdv8HJ4zCv3LohXgE2hz2jsZkcpNURXwfpvi5%2BGa%2FRXm78%2BOq1WfPEfGjmLL2Dq460TNsFl3EK%2BDKM0DnYIHLJvFU3QflveTzHPSLJuIyqwHQiN9XGx%2FtA4aBufLdHkExh0TNrWY%2ByVgVZeBrRQqTD5bp5EkMsmImF8NlUVW6TbksVhY%2BnX7Jnr6%2F8KUVcbLRmllyfndZ%2Ft5iH7x1%2F3wvcqiAYroQijrbajnoiF5KaEKBo3tHxdxUMag5DgOFo1sxU2ZYRmMACWWcfhHHCxuGeF%2Fru5aCN%2BfhJGsj2lbpBVuQbTawM1a4ZeGtiJpeZ9YbeBW5mVvrPcbXWtOXEvqhIIMWEjPM0hvvXD0PzP7r5sMF9dg4WXLGX9A%2F6nT0aw4B3U4vu%2FThR3x6ib5cmXtd0mXu87EiHvXqakVTYcRc5kuno%2B%2BG9jMgDyz%2BgyQ5rTm%2FE5h0d6e%2BnW7%2BRswsXCwihRKlV9%2BEAAvSjpUoneF3q221DXqX7TPv6HIntJd5lxzTPVotPM8i5UVpLi%2Fok8O8xe9Pf9HUzthKs%2Fn4bhIwrBJ1Kd%2BLAZ9RmyYJfs2wwa%2BL%2B1SVtGPBHx4DMpNAssyxxPPQv%2FAJJGpTAA4kUoww9GRvQY6pgGFEPoRtwka5h9nEPIruqXIRrL9oI7LdezGTZS4DBsw73Rfxdsjf%2FUjpP%2B8oMN%2BW1uX%2FhqDP5yWf2E8OVG0eITFsss5S2V7iEmZFRQYRz8pmUtO4%2FzZmTi4AblHKaGaJ3%2B4t7vSGj1yzeQUDq8EOgKDbQa0hbOBVd2yPIIPKu2j6QhHCn%2FXaoa%2Fj4%2BIfbOoIIADCAAP0KZ927JnqMUtWQU8lzZ35XKD&X-Amz-Signature=c2029a7c8ecba949eb89c2b8c42669987318ba86e69aa53c00dd7fa5b66c658a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AVOE45L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICYBxVPu3hy1e1qnXkIBPmRsD%2BDl05Sv4m%2B9v1INfPzyAiEApU8rSZJMMEkimByopM6BYSdNEpIcQcomum3XlORr1PAq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDDOXgYsbHw0FDsVBDyrcA97jCToG1n269v4npJ%2FQHW5IS0jmkRhSQ1UcamZQdX7b2Mpkfc9qygmR8P3CxZl2iRx7vyyDlqqBFG2mgwXa6AWVCtCJFRKM%2Buf45s%2BfwtcrKOrw41gw0u03oqIA9iZsbixlNRCsbi3A48DNCJbesmGsFKTP5xDwJ2N5mSixugsObA8s3aQ5%2BD34AvAbcADTCIyjiJx1cuABLJpCt8uJvXJxKF%2FzvhhSsTSGqjtjmksa5bDOkrIxirLwCxBJ1%2FonBytaJqssPh1WdgU2YA0cMOxggVbmqnJ%2FUb5Q0HUzGukD77FMVbVR3syITf2iHr3mfqBFV%2FRsGFFpyIYIQWQ3kJNHVhdq67K6VY5S2lEWyIUVmQmTrx87XVUKk98feV01bUxTYWGYCbt46ztluBewdClsZPEMxi1%2BFCZtctf6kKOMlumegWOZaTVBrgzJDS4ACUCiU3vQj3Y50RPVMlb2ZuigKe6ysKNITEqezzqFsyGRsPyPv12BkKMVDJq13EW8ZcgQFQ4hATi1cbTH29SLB9OX9eGQ2aHay7wp1iYHNHJcfmXoANTe0qs0bZyUkeAOgYFaq%2F%2BhfnKbLK5SWyzcMxhP33Z%2BB2vWjsIYtyGZUpG09T9RVoQBU75ZW5nQMMrRkb0GOqUBLn8WnIjjcLjojCuvWmJU1PdHzOiQ1DLXPmb4Pq1WswWuDT9mo8XUHyfb0BlPPqC8q1LFsO81Nm0mwsK4R75k23fFMT%2BINIsCfi2kHEocNiKeQVeCYpKLsQY7OqtOhjngmFKKWPrX%2BkS4YijhRLuBEzAejoUf7rOtpJMQ8hrc7TRNdJ4nMaQ5nhUSKz4WMzFVLVND8NKHFoWorb2h0tkkNpZksAsl&X-Amz-Signature=4ff88fe72521f5a748b2a0d90594adcb46cae576f4f6de421001fe7a947ae002&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZ7A3TOC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCVcAPqnpQdU0FTpGe255o6awbkLKrvMDgznpjOANtUeQIhAM%2BOFyC7%2FQ6xJ1UgymHO0lhSE948UIVt1olITVSjPH%2BSKv8DCFkQABoMNjM3NDIzMTgzODA1Igx4vko7KNSUwZa1t2Mq3AOkZTCUhSAl%2FJaL4kf0qb3XlgBQD0DKtZLDcYL1Pvhg6OSSO2Jgf1OySj6dZFpe7PgoWIKEifTXIvuHQ7ozP6vdGM6RzSPil0ShPOyMJoEH6rCzfpLg%2BXceXUz7MJ%2BtxIIJRhA9epnnCaVxwmi9UhCYiXcV3Tk11Eik0DZvJUJ11xgbrEn5xtqCnKFmCMefPABKuSFlUA5TaEln%2BjiLF7cmsadeUgvRWVhsEPy03dn6gWQf%2BNH%2FbIQYwkq8RxZ%2Fye7XTlzARG%2B5JB%2BHqIHnMzpdKGqB9QpLxFzLQGZJQfd1p6K4nUsgAR8VWmpccdwoxdwHt49Po7Ni0gUHLc5RRZYP3NgWMLSpHZ0cuAQ8E0PoiI9neUP8WUSaTZUHfpObJ3rv0yV34K9bMbLUZ4pHSShiPh8yfx8guw6HCZ9wcou%2F9crIrKugsx7imBOSLu9Q3VwRCRdvjbccr%2FB8OOtdPD%2BR%2F6rsHN8Btk7LR7dcDVeQT1W%2FVYlBOP114Mm8omRkujzYiCAp6b3GUFmaF2lusfLdaEI9Q%2FAcO1M6om63EXrNx3QoX2PXXZFRH5jkbeQPm02DbWiMOq%2BHjssL0nbJeNfci6%2FL6Ji2FnptnleVsl%2BaL1B1S%2FkhiJkHVu5VyjD90JG9BjqkAbKSMdHWe5YGdQVjVeWDa0ucsV3HoCFVQ52QHz0CbDEy%2BRQrZGjcdtq%2BhZ7kYQYPJg1VDocIjePPfANH5ST%2Bvi69GsERa4S3N04LlXKuK8rRjgZaSLbsBHgVAhY43tAC4bSmGLYV7yXKXQzxZFG2w127Mq0gsLtGQ%2B6Yjzs%2BkgDzc0oMObkkzYdBkkH9tHzg0hgSuoQDPr%2FpkT9Xnn2Ip94c7fv0&X-Amz-Signature=28b5de52f2f7c33159adeea9709f338cd4fb016c62765bcc6d60a31887469852&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QW337B6T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCGa5bQCJl6pRvu1BbAPG21nn9fxfB8EaDlFjDU4oZy9QIgIgW%2FKEmOQ81QPzNvf0WB8v%2Bn%2BKV763izTSBNJ8K%2B7asq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDJWpjTdHVHhKO57%2BhSrcAxOrezZuL4ZNBQlkaku1MSEgNOq6GUFci5TKjrQjMbRPmRRHqNgSSfuh6MbvSHPv0vghgLbncaAQ2Z6kYNEIIkJAMDvbxy2UbocTv%2B2NBADyvg%2BKZK6Y101TYayGmYPtWLZ4ayA9V2HPD65kmP1xTrp3r4UfWAnJs0nn3xDHBL6vXcTsgdqMVdnO2njf5XcJ7ekwjBMdIblnb7xzZK6TGJmQ9taHZP%2F%2BZnfxYrvab0popM7Fo2c0Bjqwy0AK%2FDmxM7PYVQ9FTSePwQ%2BC3nlFUASHojeVFOTe1N%2F15emFDDK6h7TUistwSINkZZiDHBJ5iM4LAHhCEJN70GQ05Nbio99yHv%2BIbCPhTFR52L%2B9nFFw9SxECdlWP3uoJp5p5ar%2Bn9FIzSqVy3pV08mfTQ2ANkyiaWIlOQ4PB%2BkIkc1BGTB4OtJl0%2F9VpfZQa4NhWFToHIfYIEeBBfgbpabOnVDL%2BddeGoImeJkq%2BbivrslQED09U%2FZfSaVnaCLUZkTsIsp67%2F6k6dpBptzxv6FVnaSsUDswHCfe%2FwaKHeib2PQRn0450szGN7aoKZh4IsFCWWLwdxCdZlfkosh6BwWd4XcWi9HOxbf9pnwy2LHlXHZa5hO%2FCFNfuHDySp%2Bh2%2BrjMLrRkb0GOqUBulC1Lg%2Fp4q5LDHTg2hGP82Khs8bYkDLCjjy0IVmajGHFINB95%2B1axA0wz%2BupxyJ1pXUU%2BfnVTtLVUSVZa%2FPB1Lvfk7oJwyhe35P7BqvhdsI0LZCjEG6m%2FojSflkGN2cstovgqpsLw%2BXjvTD25ACrRBwX4cBnZdmDIaJIklOlo1sFxM1gcyHSess6VAOxGeYpESiixkWvdkoZV8ZXVofqlhcvmv%2Fy&X-Amz-Signature=28127ccd81c135bd14bb75064eea0573040c82963fd02af339f7b56e0d9a182d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6QU4BHA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIFo%2Fb32IBfi64Q1HA2%2BUsIOEsVmc8JC4u3C%2B7OEK5HsVAiBqnQ7NXvnA%2BoIozK3AMRBdK25ycKG3V1cVNX7ZufS9ESr%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIM7OPTL10sVKwYwV4JKtwDqDGf4WpSV%2BUV7i%2FbcKzdvdv8HJ4zCv3LohXgE2hz2jsZkcpNURXwfpvi5%2BGa%2FRXm78%2BOq1WfPEfGjmLL2Dq460TNsFl3EK%2BDKM0DnYIHLJvFU3QflveTzHPSLJuIyqwHQiN9XGx%2FtA4aBufLdHkExh0TNrWY%2ByVgVZeBrRQqTD5bp5EkMsmImF8NlUVW6TbksVhY%2BnX7Jnr6%2F8KUVcbLRmllyfndZ%2Ft5iH7x1%2F3wvcqiAYroQijrbajnoiF5KaEKBo3tHxdxUMag5DgOFo1sxU2ZYRmMACWWcfhHHCxuGeF%2Fru5aCN%2BfhJGsj2lbpBVuQbTawM1a4ZeGtiJpeZ9YbeBW5mVvrPcbXWtOXEvqhIIMWEjPM0hvvXD0PzP7r5sMF9dg4WXLGX9A%2F6nT0aw4B3U4vu%2FThR3x6ib5cmXtd0mXu87EiHvXqakVTYcRc5kuno%2B%2BG9jMgDyz%2BgyQ5rTm%2FE5h0d6e%2BnW7%2BRswsXCwihRKlV9%2BEAAvSjpUoneF3q221DXqX7TPv6HIntJd5lxzTPVotPM8i5UVpLi%2Fok8O8xe9Pf9HUzthKs%2Fn4bhIwrBJ1Kd%2BLAZ9RmyYJfs2wwa%2BL%2B1SVtGPBHx4DMpNAssyxxPPQv%2FAJJGpTAA4kUoww9GRvQY6pgGFEPoRtwka5h9nEPIruqXIRrL9oI7LdezGTZS4DBsw73Rfxdsjf%2FUjpP%2B8oMN%2BW1uX%2FhqDP5yWf2E8OVG0eITFsss5S2V7iEmZFRQYRz8pmUtO4%2FzZmTi4AblHKaGaJ3%2B4t7vSGj1yzeQUDq8EOgKDbQa0hbOBVd2yPIIPKu2j6QhHCn%2FXaoa%2Fj4%2BIfbOoIIADCAAP0KZ927JnqMUtWQU8lzZ35XKD&X-Amz-Signature=d3616b3e27c31bf44325d539426eeed405244fde995913f6098d87cf89c8ede0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVVLDJP5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAG5w%2Brgy8Wu2LxqSfsMa0%2BxXijDH0sWmQGREAbewUlQAiEA44d4wb2JAO49CBIqBoMnHrkbRmkgxqdnW9jkpTqF3Fsq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDCZN7iIFi8%2BLuPxynSrcA%2BPYnIk3sMXCrFW4lwhxqa3UhEK1PnR%2BUhwxAULuZNCwEF7I17KobT1%2BWK3SfwWJ%2BtMdHhSbO4h6Pa8glEUgVHHpdP%2Bc%2FWhfUbknQOpkp5MStd3Ls9OxFdMovBsaV50Mf1T2bGffzO8cVBAmOYGwS3XrtEKvnnZI00XQ7%2Fg5dt9jZ2%2BVuBjLnzMIpL4iU5ooIsOWJAlUu0xqmXLjGtknnmDnXRWMsb3QJbKD%2FqX2QQ54a8lxifXdpK41WJiw%2FmimRcQXCHpcIbg4px7sfe9BfZYuS4IH%2B4OCAySuoN41DmHNVL12SzA49hTnYP4Vt7LimKfJY9beLQEc9dTzWKEYMkcJBHFxVOikjTNoeh7QyDL0fwVCstQ8LVdRxyFe4lU4WgHPTX%2F5%2FjlSa8%2FNXbcjsOKS0zv9inuDNYvDWk4jI5vSFiltpkGItYraIwmx0PuaaZ1grabilhBBZ8AturkKMwzWwIUfptD6CHp2Fa8rI4wDPXPMZANJ2d13ZD%2Fz6ogwpRyRay7RwDDlLGC52zZ%2BoExpvhjHn%2FE5%2FAl5WSiu1%2FTMvgsTP0OcH8yLVjsl6kmkLj%2Fv%2BkpScGXhkkhtsiuDILJFcaFI6kC%2F9rvJztsowhh5a%2FOKNdROq7Ra4uETMLnRkb0GOqUBPl%2BHSObGXJqVWTob7CI9iz2TyBATTgrQJKBcq6qAJWC6XDLUazje4VBbN3VGZ5YOjFL0SSt3zy1KH1Atehxl4nm9Y%2FoXj0MK2tp%2FXIHnc9ubNx5gpJ7UmN62jySuEStoC8jfTZFk51U%2F%2BKVvRFS%2BqT3luEvv10bViEzJPJaAPREs%2BGdVsw%2FT1nN07Nut%2B6SvWglhC0wqPX5zdjSM9LB1IjxDGc3p&X-Amz-Signature=51ccf4bcc4ecfc61c64ab9918f5865f90fb094680379db19ceeb6dec86303c52&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVVLDJP5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAG5w%2Brgy8Wu2LxqSfsMa0%2BxXijDH0sWmQGREAbewUlQAiEA44d4wb2JAO49CBIqBoMnHrkbRmkgxqdnW9jkpTqF3Fsq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDCZN7iIFi8%2BLuPxynSrcA%2BPYnIk3sMXCrFW4lwhxqa3UhEK1PnR%2BUhwxAULuZNCwEF7I17KobT1%2BWK3SfwWJ%2BtMdHhSbO4h6Pa8glEUgVHHpdP%2Bc%2FWhfUbknQOpkp5MStd3Ls9OxFdMovBsaV50Mf1T2bGffzO8cVBAmOYGwS3XrtEKvnnZI00XQ7%2Fg5dt9jZ2%2BVuBjLnzMIpL4iU5ooIsOWJAlUu0xqmXLjGtknnmDnXRWMsb3QJbKD%2FqX2QQ54a8lxifXdpK41WJiw%2FmimRcQXCHpcIbg4px7sfe9BfZYuS4IH%2B4OCAySuoN41DmHNVL12SzA49hTnYP4Vt7LimKfJY9beLQEc9dTzWKEYMkcJBHFxVOikjTNoeh7QyDL0fwVCstQ8LVdRxyFe4lU4WgHPTX%2F5%2FjlSa8%2FNXbcjsOKS0zv9inuDNYvDWk4jI5vSFiltpkGItYraIwmx0PuaaZ1grabilhBBZ8AturkKMwzWwIUfptD6CHp2Fa8rI4wDPXPMZANJ2d13ZD%2Fz6ogwpRyRay7RwDDlLGC52zZ%2BoExpvhjHn%2FE5%2FAl5WSiu1%2FTMvgsTP0OcH8yLVjsl6kmkLj%2Fv%2BkpScGXhkkhtsiuDILJFcaFI6kC%2F9rvJztsowhh5a%2FOKNdROq7Ra4uETMLnRkb0GOqUBPl%2BHSObGXJqVWTob7CI9iz2TyBATTgrQJKBcq6qAJWC6XDLUazje4VBbN3VGZ5YOjFL0SSt3zy1KH1Atehxl4nm9Y%2FoXj0MK2tp%2FXIHnc9ubNx5gpJ7UmN62jySuEStoC8jfTZFk51U%2F%2BKVvRFS%2BqT3luEvv10bViEzJPJaAPREs%2BGdVsw%2FT1nN07Nut%2B6SvWglhC0wqPX5zdjSM9LB1IjxDGc3p&X-Amz-Signature=19fe70bc441bae03ddf89a345af19c9c91975d7c562becc9db79ce5f9466e9ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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