

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIRP3RS6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZfxEe0chHpfoIkwXBIfKTBuKM5wMlAdjyF4lV0IYxGAIhAPVe6MoQORZrtbHLO72Sh%2BISIJU0gnfOKKNQwP%2FmGCbNKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxQxaIKKpRfh9EKzUsq3ANcILqq6TjB5qcKC0Wthdo5AnVRhAbVRIjE52wvuD%2FqPBrXqdX48okJrs1k8b%2BpccZD704s2SPoYb9kzsiO1Q%2B6i3pXIMf5QSbFq%2Fr8%2F2bLbgNscbsysSFO%2FSnmUDnHRoYs2StNTysEiYeB5Gx10f73XmI73SrQlS7swKnjv5I2CdGHGpXXQeLtdkHdUtnyqZUf21fitIalvHoLIsYY06w2H04b1GO6DvWPjGmr9bZodD9pU5vmHDqDQLDmNtZ1I94vm41OjPHOKq1u5CAlD5gDuEM9DgpywcLFnx3Mr%2FVmtRP2VTDQrZBH8tv3WGFyJz6afbQ5bOTx0wDQI4RHqveicAtYFVgqunTYl3JFXgYpTxOUhGkN1F2AZy%2FTeTDCVr64xqFrialMmP%2BGDR%2FUEGnCUMI%2BvaqD8rj0Zb445dRFTs2w4Q48lG7GKBE7YohsDna2BNg3Dqg7dUDcqoXP24NGDDdm%2F2F%2BxuG4CFCzE%2BbgTdZWaK%2FsjIatqHXihzwDZ9%2Bz1GS0gld4164YJkAt1S0%2FtPf8MhA2OQOH8ezN9cD8x8RQv2fCE2gzowuJsoU49gMJBLTjbjIFAciImkCc0ET6vik0VwcXDxzEsOzZwn4ku1p2kAVIYpk71d0ZNjC92v68BjqkAS1NvK4J8yEqTV7DyEi8rsD41okTbrj2J1Ufhcz3avj1jjd4BVO7mXZJ%2FnSTQVMZRnZM%2B1hC7jzX4ubWnZ3wQn2txz0NaHF%2BymB4IRpTSAD3%2BgU17OXAwd7ZH4MHbDCQJ%2BMDqbr0XbHA%2BNU09e3UexmV%2BmttS%2BegqarPtzutR%2FT5OwNuFu5BUPYXH5fLYVOMiy6uArLlmV2KBafJpjbK%2FfZEO09d&X-Amz-Signature=2d98a64f5d729caf37bb64b886846b713e656056135a2b8a39bd60bc62a01917&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DISG4NY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDN2SvOHMYmAx7VqnnGdzahWgIxyOld1LlnO8aDsg7dOAiBYevuDaopp0MBPOUHKOKQZ8xwgMYIvJKvT84y8o9%2FdlyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FdrMFwxP6lIxOf4nKtwDB%2BSaiSyUy63nxdzel%2Foq50l1%2FPa9mdRB8YmcFolFUIhC8Yx7YkpRjmXLC%2FY9hMaGoQ3S%2BzUp1vjWEPuS9opAedZ2xEF8X8iMIFVBUSUzMDokMV8J9pkBTmuDGSANJFqMi%2BRDZQ9zKoEyFS78KfrOHGETb24lbHlrbzv3q9T5vINXM%2F9k4HJAJhaSPQqsKdEdbLT2sbUGfW67M0CKaICDFQcpBEFzPDfRolbdikcj%2Bu4QDMUj5%2FguwAaKRs4tinPdR6ZTh77KtPJ8eSD5lyu6Uypsa6hFMOkY8Utc41ciM8xng9aVSEJmkKLKdahoBWPuQY1OMCFXS6CTtfD9Atd5De%2BjS6YtAINaEFfDLyFabvF5LCF%2FCvqg%2FObeZiGie6kPe4rSAUTq0ku7e09nhDaZxFax8WwyGjpfKITW%2Fh1O6KrbZ8VR%2BG23Hky8uyJfmP5kUlQG2icjUgnBhffCAmjqdLOP04Lu6oIfDJbrvvoVDOSGhfy0pvKrGgYiQ5hH6%2Fhae2irvFTSKTcElb0sBuHYC1PsOr07CfIZycF%2FH4K5jY%2BoD7xdLDmymql6nw1hTqpwdxLjvBvvfN9FmbirYp7mkiGHCKxWRKzUDOInLH6N5AK7HiUFXcHFtzR96eIwz9b%2BvAY6pgGUpwy0Z5eegZJItxVzCWZf%2BBvcj2mUyhVJEqTF2aX581ZMLW5dbNjaRW7eP2Oj9lcvOkH43TDhpJZEFzelQqWc3M71ILp6X0UM2%2BF0gXhEY5Po1xVaBKKVGAUTdVRJhlnwiG5hgZACZpeHQhuWi3GEgqtyudO3YUdXDyI4rdrLS%2FGRASwrePzKLtmSBnaFrEC4T6RgWhGDXSOXpunnFV0BiItOzzlV&X-Amz-Signature=e9a20394a4dde978e57c91d1493306c146daed065abde8fdf0062d8500ab92f0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RRHEOYB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFEOws8E5TyHOxE1L3m8P1m02rLkyl19%2Bwd5A%2B54tIZeAiBq%2Fh8lZNnQoBH6tnwn%2BrtyVcvY4zsq9ibEO%2B9exXzXDyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM50tqyz2RsI98%2F7wgKtwDdxX31TDNRhNPNHheyE8pP8K86fwLdFCuRTG0FrHQE8Cnbu%2FusViY0zuAqPY096ZAeFniGMQxtZYElw2kkosZJDDNT6%2FsOviRPSNSuiDeB%2F8WW9MpbYA5XuvosLo9Yfb%2BPp%2FhUs68a%2FyO6cNx4fMsXkrGv3E%2BKfZeJsCQ0UJap3kNCZGE0zKf1gtDETLlf2oV%2FH6aMPguwm3j57YNVgA3EQEfdEMQH80sY1KNwTsf4lgr7hTD7wZG5RMbP9PrwYBrf7YBisw%2BK53JASpHe47%2FLcPPYsuMvU50cZry3VCqn2Xd4g5ByGU05dQAj8ZNQOu%2BLgxqsot8UZcbCtzE7gcFcVqkIMt0ncb1zClvFnMOJDILzfTvSuG%2BnD3BxEI%2FFntAaoPM7daMNXb3R5jaW3QGLGJwt0XxJVkfwPo268oZpf9G7bYHU1E4U%2F6h51guJIJRcelokJMKgAgvjKS%2F%2BdTCh0Q%2FD%2FeM%2FTdGR559n%2FxaXxpC29kJJTBsdRpZOaNxsouOUuhgC%2FCO81Hgcb8SfkYUgeusJ0mbnPVPBOrKPiY2%2FFHijzQ7%2FJjU%2BFfOfEUGdHLMM0ooyq2X1ZFNwW4e6LCUkPH0JsNtEGmzEIlMUUw3GsTzAwwztOvHlTL0M%2Fcww9j%2BvAY6pgGnPNnsGSZaVK8pXnxRwSnMAc21YWbfFRVFHwtC3tvd1SBtB%2FhWW5Ede73uCsCapyGwjw%2FiO4wOwUJDC9BbalB1jXo86%2FSqTVMnCL6JjJ2ezgr%2FZyGuqh17Vy7BJlyfgAkOEHNcPngvIPHZBXcdeoqOPpMVW49l2ZGwicv%2BmGuOCrZqGMQivY7fb0Fylpv4aI6i9vzIrJC2igIeco18%2Bjx210AMwDwn&X-Amz-Signature=fe8b73467cf57ad38fe362df0eec1e4e45a6afc92f6f1bfb1dc29638ac8e7148&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P3EDK23%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnFgEcd6d5C0sUJIfiywe%2Fw%2FJfrG8nvPy838343HfkowIgXS3dmvsY8h4jeU4UcG44uxlFEj8Dy0L5EZWOgKvmousqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKU4mkRgmqRa9wBLmyrcA3m90eM%2BXAqnVusqtUhxs1df8ooDypzK3UUt%2FTJHsNt6d9Ayq%2BYg1nWdcLywbtw%2BFK3Ooz%2FjxMP6zPqFPfywrvV0K2Suj%2FL0aj6Y6o3QWcg4MWNAVoJs3fyoDOr%2Fxa38DndJ2ZpYEgvkLn31QPJh3DE1W454Qn%2BRcJ%2BEuQpqNSn2zRoU%2FJEJYhrTV%2Bl9WnkHSVLeww8MOYDDlMPClgeUiD81rMn8KBp4EIfHxddT5%2F0nnA4pB7wJpkPkg1wBMAN4wUO7dVRbGwrewJlPWYiCQU54hMG5Jmroh5mWD37CpgZNXSNZ%2B8TfE6PQIlQDXeaSBf1L8ptR4%2FagzICJpu3TwIVOwenwAaF5ZjibU7RBn7MeYIdOSvkOGujHrFALMjanj%2BiAVw033MtZxZpUJSQwcrWv843Iexu0rybS3iUJy71JXO4nhc3dw3tyPpUclybGvsmxABSa%2Bgx2GtDIPUrTcq8WA1oTneq3wyNm4FfkFRZVZ9pX3KRUkR9%2FJUCwHgumRTHIPIJgfPIEScQkAg1xST%2FqKEnH8FcNGSTUWmWW7ov9xlln%2Fl%2BrltQ42lyB7NJDrtgTnto92YDFn9lbCH0gRtkfXZgZEACl%2B2ourcsItVvgb4kuMIXf%2F814EYC4MNPd%2FrwGOqUBXlFDwKgEgQtce2pI85jIc%2B15GT%2Faw6r9lEKDUtk9hnmz72DwonzW20nxPc8UuzSP0w1RhDyIsC31u6iXcrvJCWO%2B9J1M3BNCMCIUT9vIP%2FwWbQSYaWTGfvHPoisxtWO53VMncakGwS72emGVIu7Yn6c4aYwdhObWV1QXdJF8%2BckcVbv0PgQc5wt0loIc0mR8qdTj8lJBrUDJjfZ%2BmuystHv808n4&X-Amz-Signature=c102b49b9d526177ec9f20113dd6184c3291b9b5641740a4bfa2d5d267ce999a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZX353CB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDw4txOvy3go%2FAKsaqtX4bLCF2N%2FeooBQ1SgFcSzFT86gIhANLozPdbbgRBHBT8oC2hBOi6FpPAdS2XrecA02YiSz7QKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwyKSKQxEIlq6uk3lgq3AM0zRulRxWul914TEUDpA48OONO7rtiYFESIc2DYEUJeSZkQ2tbdX9uxhlDLf3%2BZUrAUbvkJU0qcjY2dyRw1EqFQ%2FhazEznTOIAUxUgfmLgxF6oHXlX%2FPkBocKvNlb1fbf%2FgxDVUJgQg05o0VGwdLjNHSqY3dLPQaS2L9nWYQbUfchWNmqBs4XGke3JHgsynEF4l6Owb4xD%2FdfAXqczVggD3iht87SFzyRj0IrQR3jCCH89dwJ01Z8bsuf%2BvdqKe5CeSuwlZVkg%2Fb1zgGJ8%2Ff9fWkdeKRf8s0TfSXEb3s2FD%2FhXHsKPmhWcvzGt1skhRvwo1p%2FXvbgFfhQEaEbgIljWcts%2FCHitXRM8uLPOQ6nxrXkl7Gqqi71ifuUng6rTdVlVLib%2BCAzsnU%2FTS9mjMICwJPhU8vO3fqsp2pkkm4MlpDT7GDrTSNnL1O1mSnpuvcdmYJ96QOBUAIEN8pWmHD5lwUtf82a%2Fm4j1CRpdK8Y4xG7tJTVeeisAK%2BR%2Fi0gAeKEkgVQGdkEIbKuUAuk6bwR%2F5qTW5P%2FErQ4l4fEg04UbA8M45aW9oOqFu4hts%2B5EergyClxlH1MMNNwcIwpw%2F0KJJZ8hbiX2jlbPvy4gGObrnAGNGlxUhdfY7E2GLTCE3v68BjqkAZ2MuzV8k4L7gpcDxfiUtZZ3cF4STDJRak2celPgDBIzdOpH6OhO14tDihaADCpwuZ9qrtqVLpaEHDKI4uobns255g%2FYP5pq4yuhGSn9f5yiL%2BH6rOhWWP9CGPIP0S75xjD261DtBu%2FaZ7B19SHsVQAU%2B8cDGYEndhAHYkT6W9AbAU%2B1%2FnxC4WmZh0T17u8U1wzy%2FbuFBI1c%2FebrwcKNus1CcwLo&X-Amz-Signature=a19d9e0f7290478cc7c5c6fc7576d5790e8233580f1a30523a9981c1662112b6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRDCGXD2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTbVCoKOPfnicXZgGvBNlAf8KlImEZd%2BdJj8FIBbhXyAIgOajpQwMreQZ0%2B8LAzllNLq%2B4SemMVOufEr6YZZzx6OEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7ZdR5yU19V8Ak2HyrcA1yKDWALQHimaT9Ebc8gZAUSByzkzUWE1BSFywGMDnwoi6GVc%2BFtb5cTHPVQ20aVNij8zLBPVFl46WQ4IlictRkzeG5YDThgP01mSODu7tn4ODe9c1UJD7naGujmnLRGAVfd1fF%2B7SYQQnuQLVSRGnPovlLg3s0%2BF2hrxlMIYmqanktSF0QpFALEt0kJfkv4l6eUeDoVnLMoAIK1EUXy3fMp62exH90YeltckhkgzHEWb2zOy5Rv%2F3u6Dif%2BK%2FO32WtiuycVXlNORVHLmrD%2FFimffaIGSfLNy0qUJOpYuNwQHNyWCNH87G8fRcjny3mVKwA5i43q2B9KtksWcqHs3xCLCTeg%2BFiIJ48nJ0j3NreUYvDtxD3Hq6C2xDV81x46yPLKmTB2Ks1kZeXq30hO4VV52jd2ctAbGAJ5BYGTnp8LwrZdsn%2F9mDECOSRkAB%2FGYh34ipe1v6q8jgVJ4%2BTrbagLMoJr9%2FeQ4U3K8009BjnYGjLxn9MD6jlxf1JzmoOBR2aQVquaz8psw0Mma9z2QIW7AhF5B9yZOMPGQjWF6tMx3oOk6PdTSMzozbTgQsjEb3q4yEILLpV0QpFxMmzfiD9K7Q3sZ8VA%2FtdITOJjtiqGGsuv13pxfBnK7EuvMN3e%2FrwGOqUB1DYA3AUxZloK8qcPZi4V04WKIsLMaPWVVQUT0gwe%2F%2BQoC8hMpLvAA9f691i61Zpl2upTwexMZLfxGeJi5k8zS71%2FV7uaVrRoqpk%2FqFCA8%2Bn8tfb1nY1E55q9dj910O6aMOsB5BZq5C60dkmeVhFC55vqa%2B3uN%2FMZoQ5y8T61zaM9KaLpFOJgigZdvaa1SRF4yfkLI0vtNxKDLL11G%2FpZYMF1DqH6&X-Amz-Signature=ce704ddcb203ebb35d4b527133e02e76b2ed86343bb5506974dc38e1946719d3&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUT2CIER%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEfgYCzahsvsjglfth%2B4mnshb6OVHAObF7b%2B%2BHbSDeRdAiEAmG%2FiXpAxwpMgQ1mDSzY3WnN2wPmpAi3wLE6U2JJldioqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNfutWXO5kv96h%2BcRSrcA%2Fjba3qY3WpFYD1oBOJxVleadjfNsgG%2FpppfSYIi02J%2Bf%2F14t99gBsAxoZlpoV1yIJeHeRbhO6ogyCOYrpkxcZGQIpGJg1OaB%2BESGTgTm1HnV%2BVJS80dqd2GnWzMyBhKduLbnYUjXufj7MjmNpzWYyBCeZ5tiIRAfXL4Fjx7HCz5E5PKPTshi9DyZf4cZttVJZ9rlTnbj%2BkLla%2BdtOXG6pKWhET2%2FIGdXWaaTCkbhlKb0X0%2Bv6DimXIOkyPMYsMM5LifpP1r3W8DRClH6oadhWvwVvKEAnwtwXxRH8f4vltCQ2CSVWNXQBJR9JWIOMpwcuVhWelz2Zoke11Rac4xm3gwp98HoQra7%2B1COSwt%2FqT9FyxhCqK1itGgqzMDL1zY8o2d1WbcJ%2Fyir50O0mKu%2BsFz7X566aULGlV0WstQEIsnw%2BvbwbAxs4TgqEtrj4PQl8otyur0dbkICN%2BpUr9Ju2O3Ubx4yjd6d8wq6WY1%2BIxkknTb%2FewD57x8%2BfLyQBmlwbj4hWGoC%2BtxxCOV1nxTbsTZX4hyVyvTxsmXumWIgH4pyiNCna8nYjq68bmX5%2FHYk1HU968OkRwRQH%2BkQqO%2FHZdw6bHR2qbwg0g32jquQ9xGCGMEvdxSN9VfAYB1MJDh%2FrwGOqUBpMN4PMsaYgwTPYj1xNYm7KxdL5SGcWCwL5vd%2BejCrJ%2BemsG49mqB1jEkcOERkO5RfxXh1RRuVcdinGSQ8jk0s2xO0Eikn2XJikOwRj4O85oHLTrut90p1u4o60kYNlzvNX6SDt07QpPgx0PChbLmQoKypjKU8N4hhLzzzHb4JCdEAgsswmGtjCsBhVH25j9RJM3nGZVyyB784AWGHnpxY9qDjEvt&X-Amz-Signature=6003bf77f5e47c2c0d7112947af74072f0590a44267a20588d323ab1e970a3c5&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FN5FWMZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIB5Mtxr13%2F7Ne%2FsCG1ezyK6Y%2BxTb2LNzIcTmzPsm0cAIgZUS4gO14nr2k4TODuaZK738Ca5c4yVb64rMJsJSquT4qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAwHKd9dxMlfCnHmlSrcA7kma60aCRltidRlyoH2IUTGrOiUJogzn4lrwdDuNYzHfy1O9%2FjescKBF9pu2C1ccI3YlCGOFTFjtyltRnK48iZVZcLKB9E3wzvhjKYnM9mkKoEXStQgFpEQtAAuGA9JNwpa1Fo9NGH9m5iQAdoEnPqU1zdvDZQrHxkj8HJYdxJk1cTHPdYxrnO3TWNUdRFi4e%2FxdE75c2Xrp9vJdwzcHc7M72TVKR%2FD0iHVqlGzNbwNooGxrNvFLcNwt6H01CFmgesbyw4iIeXkkgqDTZmTsfy8cdZQHVUlbjjNiGSRK0uD0PgHLgaB5s%2BcQ6m8SOFLQgITOlpOFpMaqnsCCVd6JGxEhfmguMoC4hKxBPFeOiLmF0B4r8PeCoedvaYZg1c4exVz4eCZTZK%2BTB5UljEwhsLkbo%2BmL0LKoWxoczrRTqtGwMzqfkCaoNH8PM4%2Bx9aW5cy%2BuwXCLUwE2Eh0nzteCTlN8MgblXOoZsME42wGM5N%2F6%2F60Ieg2OAO2ebRjITUCgTbwSMqcUOr8F8aC2GiUmkZLnSejSfM%2FkboYOFy%2FVJfz3Pdk1H%2Ff6AzTFcYpBZFg7rCuQdIWWODTJ%2FyHSYgQBFecPvMI9GO6Ivn27jMNHMdb6Aqpud7KwbMp%2BUuQMMHg%2FrwGOqUBtcI6Ya6oxtivgL7Bz%2Bd7JqprrenQEp%2BVeuVg7uwEDpPi5%2BUroiZRtdpXWmR6G2v2k9BvloD1Ho2Sgacn2WaH4jkyeZvO1Pf1hIHV5malSP33QXKKMTWXlWXU7Zwo1lob2TzASlsW9%2BY8vCMSZcXiA24Kg9aBDRBi8erB%2FSNtQK%2BRJRl8oEsPG9UsS%2BFEyjqTawAzj%2Bght%2BU6g2Yr0E1SLy88slWM&X-Amz-Signature=10f263768adf773d9831f5250bbe39dcada97208e4220226c9e8d700202f2285&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZX353CB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDw4txOvy3go%2FAKsaqtX4bLCF2N%2FeooBQ1SgFcSzFT86gIhANLozPdbbgRBHBT8oC2hBOi6FpPAdS2XrecA02YiSz7QKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwyKSKQxEIlq6uk3lgq3AM0zRulRxWul914TEUDpA48OONO7rtiYFESIc2DYEUJeSZkQ2tbdX9uxhlDLf3%2BZUrAUbvkJU0qcjY2dyRw1EqFQ%2FhazEznTOIAUxUgfmLgxF6oHXlX%2FPkBocKvNlb1fbf%2FgxDVUJgQg05o0VGwdLjNHSqY3dLPQaS2L9nWYQbUfchWNmqBs4XGke3JHgsynEF4l6Owb4xD%2FdfAXqczVggD3iht87SFzyRj0IrQR3jCCH89dwJ01Z8bsuf%2BvdqKe5CeSuwlZVkg%2Fb1zgGJ8%2Ff9fWkdeKRf8s0TfSXEb3s2FD%2FhXHsKPmhWcvzGt1skhRvwo1p%2FXvbgFfhQEaEbgIljWcts%2FCHitXRM8uLPOQ6nxrXkl7Gqqi71ifuUng6rTdVlVLib%2BCAzsnU%2FTS9mjMICwJPhU8vO3fqsp2pkkm4MlpDT7GDrTSNnL1O1mSnpuvcdmYJ96QOBUAIEN8pWmHD5lwUtf82a%2Fm4j1CRpdK8Y4xG7tJTVeeisAK%2BR%2Fi0gAeKEkgVQGdkEIbKuUAuk6bwR%2F5qTW5P%2FErQ4l4fEg04UbA8M45aW9oOqFu4hts%2B5EergyClxlH1MMNNwcIwpw%2F0KJJZ8hbiX2jlbPvy4gGObrnAGNGlxUhdfY7E2GLTCE3v68BjqkAZ2MuzV8k4L7gpcDxfiUtZZ3cF4STDJRak2celPgDBIzdOpH6OhO14tDihaADCpwuZ9qrtqVLpaEHDKI4uobns255g%2FYP5pq4yuhGSn9f5yiL%2BH6rOhWWP9CGPIP0S75xjD261DtBu%2FaZ7B19SHsVQAU%2B8cDGYEndhAHYkT6W9AbAU%2B1%2FnxC4WmZh0T17u8U1wzy%2FbuFBI1c%2FebrwcKNus1CcwLo&X-Amz-Signature=01a6ab27b90e694077d5d7cd4ef1a96a4aa9069a36d95ba9fdce0ee1d211c15c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNMRKHC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFq9y1LPsqazjM6%2B2dbcIW2bB30r6RE9hZTqb%2FgQjnziAiEA%2FwynZxoWtkR0Q1retSP1x1BvbzsAAeLd%2BRxe1LcCwaIqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEd4mD11%2F1C3yP6c6yrcA9frn%2BGxQsTtm0ahag0tYXonT8ltMr7L%2FaA2YxH8bYvRWdjvkd9a3HNPoyE%2B16iyYUCNbb1bd4TtP7yWLAQqKJf9%2B0miNjNb%2Ff2E%2FKOT5gBwwcrOssRf8Rh9EuXxuaENNpGSQKfMzAZ4Bwavg6z613%2BkCHzpmhS%2FMYizy8hnAgiSg8x51y%2FWVzQvWnp5hCHCDEkpcFYK7GL7wFoxosm%2Fg1UNTZW0SE%2FTvDdYcC3Y8ImUSAi7%2FK8Uo0AiBbBuyZgLxJGEvuwP%2FMcWl4gj1E1Ir1%2FL5k63J4cVaKx00BnJb%2FSWvocclkajgXO%2Ba1AXRa4PTSKIeU2Dz4jbTaNP84wtRsd2ORERbf1WqxtmQdsZztno1UXkpvM7F2HVSlJd7JiIHA8AbyPRr8sla%2Fuo1pHCokPo7PRPH1wFGBSkET5Mc3NBW%2FDbWdXOD8n3P3WusSqAay0dohP6hcsaamnZFrLi8JoFhTl0zFyRZIDYh8spG6FRhUT8K%2F50Q1gXJfEIlUAzq2XXbfXQf4wSGSpixrDZe7uPPQ%2B%2FG6JLs6wbGRfwrVoaL9%2Bin6EhFddVJs7lUYBf2FWWMx3A1aZ7UGYpr35DHkBY6HjuI1Q%2FK0v6aOyNinQSdAZGSNrsOix%2Flf6SMJ7i%2FrwGOqUBkg8cgSRpWG%2B4027Wn972%2BzZMEOFULHbFPLBvOIvWKAoSvzQwfHMHV%2FFseNke0N3Jlh7r%2FK2Z3GNeDRX4e3VR6Pz2OIt7maYVz7v%2FvGVpoXSioU1lFUe4RbHEObDgO5KMnVTo5QwbFXoyEn%2FdRvvx9oIA1RK%2FI%2BgRJIKh8P3w2XMyOcD2cVjcMNryEsILjvpBzxZ5LG1ND9i4NN0qOw%2F13ltiVbRp&X-Amz-Signature=439dd83356268e9c9c2254d701a5b96b95db82500a1b0986fa447839a6f096b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNMRKHC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFq9y1LPsqazjM6%2B2dbcIW2bB30r6RE9hZTqb%2FgQjnziAiEA%2FwynZxoWtkR0Q1retSP1x1BvbzsAAeLd%2BRxe1LcCwaIqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEd4mD11%2F1C3yP6c6yrcA9frn%2BGxQsTtm0ahag0tYXonT8ltMr7L%2FaA2YxH8bYvRWdjvkd9a3HNPoyE%2B16iyYUCNbb1bd4TtP7yWLAQqKJf9%2B0miNjNb%2Ff2E%2FKOT5gBwwcrOssRf8Rh9EuXxuaENNpGSQKfMzAZ4Bwavg6z613%2BkCHzpmhS%2FMYizy8hnAgiSg8x51y%2FWVzQvWnp5hCHCDEkpcFYK7GL7wFoxosm%2Fg1UNTZW0SE%2FTvDdYcC3Y8ImUSAi7%2FK8Uo0AiBbBuyZgLxJGEvuwP%2FMcWl4gj1E1Ir1%2FL5k63J4cVaKx00BnJb%2FSWvocclkajgXO%2Ba1AXRa4PTSKIeU2Dz4jbTaNP84wtRsd2ORERbf1WqxtmQdsZztno1UXkpvM7F2HVSlJd7JiIHA8AbyPRr8sla%2Fuo1pHCokPo7PRPH1wFGBSkET5Mc3NBW%2FDbWdXOD8n3P3WusSqAay0dohP6hcsaamnZFrLi8JoFhTl0zFyRZIDYh8spG6FRhUT8K%2F50Q1gXJfEIlUAzq2XXbfXQf4wSGSpixrDZe7uPPQ%2B%2FG6JLs6wbGRfwrVoaL9%2Bin6EhFddVJs7lUYBf2FWWMx3A1aZ7UGYpr35DHkBY6HjuI1Q%2FK0v6aOyNinQSdAZGSNrsOix%2Flf6SMJ7i%2FrwGOqUBkg8cgSRpWG%2B4027Wn972%2BzZMEOFULHbFPLBvOIvWKAoSvzQwfHMHV%2FFseNke0N3Jlh7r%2FK2Z3GNeDRX4e3VR6Pz2OIt7maYVz7v%2FvGVpoXSioU1lFUe4RbHEObDgO5KMnVTo5QwbFXoyEn%2FdRvvx9oIA1RK%2FI%2BgRJIKh8P3w2XMyOcD2cVjcMNryEsILjvpBzxZ5LG1ND9i4NN0qOw%2F13ltiVbRp&X-Amz-Signature=395e3c57ac1262f292cd04dff3a789643ca7f09f850827bb5bc8af9fae7a923d&X-Amz-SignedHeaders=host&x-id=GetObject)
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