

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY4AKL5R%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDLzIb0BpgbpmI0UnwsitrK%2BJd%2B5ADhYd4YFdiJctVgIhAO4gUsjrQwdDImWhTZrTvp0lFLTG2IMMA%2BOdF1Nz%2BtLQKogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwKHQyEdCgseR689aIq3ANVpz0LoTQ2HEbx5KavxKt7xiw6LpBgA7zv6U4p5viRjI%2FDU%2BIsNWWziC5SHGp9v%2BXwCfrQZdsKErqfgKyW%2B3cn5kXC7EsCkBS4ziyy0CjOUmF4q7GnRe0mr4%2BClYsUAZ3P9gZGjvQmxO6kfgyOY5cAD%2F%2BzTZxJsJ7f3todULeHP92XEc%2F3ma6k7a5AuY8TL3GwHQ1AWhzLcg2wEoxYueTLxao2YOvOF4o0ZpfhSKYduCR2Fng7Rkgc%2BqBAJ4iM%2Bao7M87%2FEnz6Ll0%2FPg8sdS1m7YNqtKL3i0VXtGy02naQJKIoRS32LZmwF0MnCnM3cllvNRH8ugUwhR6kqORMeMrSVvT5%2FS%2BAomrDkMQLrYI8501AiYIL0MaiHw5XTLiZZlmY4fPpRbrD970GHRwAR3xtDi7aUhaEwL3SQtSPJH655jIjQcqbUnNo71mveBX8oI9kDsyv2N3nFoDtGcL26i75yXUm1K1IaCcG2O79wkl9biYQ2LOuq%2BNcgOQ%2FjKd8NWzcA%2FdOqBl2n4BrVbyM9xcN1pnND0PEsa2Ab%2Bopx%2Bd1VN8eT1UwKMNs%2F3DPPZM00hElPmzb%2FidL0AnmUADOOSLjl%2F5V8ct8RTjy6m0gKRGjq5BrUFXBGcw2sCYmBzCY%2B%2B28BjqkAV6IXSV5NIMouWmVuW%2FShVhbs6a2qH4xCMUzEoD1E6AIj9DnEv5RfzxHSr6nrunysc0GwRGmPYKvG8HeKDAL%2FiL4RpoCu9c6DPPhFGfqW8i5is6zhi2cmtkLDiTVS3x5I2u27%2BwMt9C6V5fZ8gOh6%2BRkDS513%2Fi8QdR%2Fp7l5ihrfepTT0qSNk5QlQH4nl4k35MYkvuPDna4KQAws4LpSJmOCR1XI&X-Amz-Signature=abd50a5d44e0b5e5c3d840bd37e5e815844bd0263330f1aec78d8fb13585a7b6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZFJLJRM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHgMOJDFrFqbGWO0tx76ssbvQKo2h1gpQvgC814YaPTwIhAMfLfK2y1GOUyTHpiLHNOUq3LMUnFOeNp6TMVoGMx0ogKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxvIxSrgUo0G6rOK94q3AMQGFHRZPMVoavQ90F%2BXMz7zNRPky7Va8wW%2FdzxR4Y07I1P2N4qVNqC37ItEjVYdAiCU7hNzmNgVRb9rJdVbfU2QJC32HNux5Iv2U1wKuLeO%2Bh%2FDtncDV%2BF%2BlWlqAxt9l91GvUYZZ7RqwqT1j8pE7Dh6wrEIy6BGzoTrqmBiStFCdc%2By90nlT4%2FJB3kyBNGaOHlCSbPsW%2BEUCM02sAZPwZFNS%2BopIfI34SgPypzSTf%2FaEWkHWQb6MKqicgGYAVJ4REMKEAq2XVZcfD3E3REnCv%2FMjNY1J%2FrgM1MMl9gfeV0I%2Fj1Zd2tn%2FH6%2FcylJqFhvtfmtK8pfsrtP78jMucW4vzJalYUTqhKTAP7R1rNSeUqRslP%2BLw7fYeBaVuJrLp%2FmBnkIS2W3neLabulFYD13ufjp1UNMgnceorVNSLZtU7w6Hb6s1HufPw%2FW6KbKk6GfnqPvcVoL653PJqhF8m%2BsEFD3wi%2FiYz0eXXGLpxG%2BJTYYYvnmQgdCSmIbYfzvJMFW2aETZWHEr8moclsK48k8COuOOLAugU2ocoK974hj%2FkJAApLjHGqdEqB2CEkZwqx8hzyzYW10%2BjqbtcNHyG%2FMa%2FWNmPBm%2Fy%2FVVH3s9XfukbSL75QJg6TD1ApZui3mjDp%2Bu28BjqkAd0kHUMm8WY10%2B2A%2FoHdGgj0kmN4Na%2BG3l6kuO6OSZ%2FJj2NfKBZWaGDKjCxkhQOkpiSh6cCoX%2B7p9UoQCjWpzp821%2B4yhyM6dik7fnbsMEjGvTfmpbRK4sTyO9RilaINaN30YeRu8FU6ktm%2BsENnZ60%2BG%2FjgIRS4%2FFZ%2FCjKFenXCgIHg0Lm0sCbuk1iULRmPa652Mw%2F55gCxiPvSGk%2F8ReevEnHo&X-Amz-Signature=ccea28ee0fe067e378ce5208dcecb1e0a4591ffd649fa269af7f663519f93092&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN4BEU4Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDV6MVrk65CBr6vub95i4Kxe0bWYPxL6wRVhY2ZqnezXwIgVGUp9QaOcpM3BWcvS9F5JtAWb%2FW3A3Di1yUhE596ekUqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqt2q5w2z65Rj4b3ircA2fkpGp4mtihazsQQqONXBCNF9FEqCHgXIXLa8Cvlo%2F0fsKrfXIXk3vGZlvEzFgQ9hJrYj2D7RcG88RbOsN5Ix%2Bz078lycCBFP0YrMx%2BLRPyeoy5TWDm9uiKnt7YEuaswUZIfyuadFgRLgNsfdV6egEdJUR%2BN5YUmP64sLqYYAES8FBSleXZJd92Yh7eAsXknbLsYIYfXNwirLWyl3ycM%2FbCET1RdluwrC7840nCzy6Mev6EBoj7Tu1Y0Sqi3S5Xjp1ze%2BVQKMdlClkX99dXSAIQdoFSYWk5ZhzVJuj9biCxGKdpPbDypLw8wj0rzbz6%2FzWpEJ0706jEZ1r%2FJzRSxCz0w9C120esDIHUYp83iQVcVFVIGCJOT%2B2k%2F6ocNTjmyj6AiFsfoA8KnxmKN2VTZbd61RcoI4a5k%2F7qn%2BDTXKnR3barEjACvEN76yqHqw1oKowle5%2FOcoPDeDi376xIhnHTVHs3N6JfW4nPuQN%2BJENnaGaNMM779ZNCgHevNvhPrryvwVgPi2bJw%2FzN2tP8qc2Ol2kZuHlU3jqzthpan5AfqbOToogfrjyQ8YJMx8GoXyZBLH3puPI3MF1L5%2BT0aHCa4x9aScQ4E2XEb9W8YXNcmTUAQmkTA0fGLgVuMNH67bwGOqUBJzs%2FU2XB4Q47vRQ3wNxzqwYPRVHQOEXNgkK5a%2FASCV0oNPtOHSwoEfwC4fEeCBr6CXytvc%2B6xcVBccsIEWbY2g1BftpRZ7Mke4GlxnhCAPWXV%2F3WALjjWGvcfTqyE3uOFKthdTMMzyZE1caytngcpSBN2KjhvbAg1DyG2NDV%2F85Sn1o8IIbo0E3IM6RQZMQbXC%2Fy7albG1hznoZtTwnPm0CDQYE6&X-Amz-Signature=fd60f4acc4e2d832176b0d2bad9da73538a782567da235dcb4009c81a2b16b56&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYOEWP6X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGGKs%2F3tk9e79xiOgo4EQZ4Lei1q%2Bc8jrl43X7Czkm6NAiA%2F%2FQsC4h03t1y8dElrf339BA%2BcfTdOPTuGCJPalkMFySqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnjW%2BTh3azdAKXxS4KtwDm%2FHOC6OrCyl9zXd%2F5r%2FlivI9WHi0QKFmrLlY0u0l5p9bzCefxK%2F%2Bk8JRwimtV6rF6YXKjm%2FFyw0%2FLSAoiAm7YEiEflqcElEBR5%2BOAi0VHZAXYLWrWSrQVDZX%2BH79Vj0irlqW51%2BPoEOp7O2%2FF6dznF0KbUeWLZgybLBjpty4ubfeSgRqTTIKh%2FTvP6yadoewMHg3%2FyifhsjGiaIDo1SfqZcUr3O0IQyR3WxDrLpSTWRn1txdaPDp56OJmWrgUN1kUFYM6662yew4cQfRa7ChIvNguNfcMyGIaZ%2BmvN3UPwBV%2F18%2FvPvjqlzQrUkc0YU2uig0CMujMz7xVCFC5lhdx%2B4NtiORg5oEXcrGkZDd1Vq1Jd9fJjzN8V9j5qJ%2B4jMimnQQF0gx8E%2BSQgnd9y9z2cKe7VxtyQG%2B6fgLlygkrnwpoGdLpPqaDnE69%2BffIMTFXkLhrToATunB04NPFJUyUBdNqlJmXFl7Oay6roBpbi2%2BnUXq9xhb%2FQijrVIueOWp5iypayep%2FdlLZMo5TZmvXu2ygHHjUS9g%2B0WdtgdtrkXrUnubhDNHbVbh7u3qDQbLuVoCNPYgQ4m9fOoMJoFJn47hJvHOLi0wg6N4GOSWXU02%2FC1%2BwE1Ka0hoOfgw1frtvAY6pgFwjupQnaHcSaBYi6s00S7P6hNhVtgEsupwwrXRPwdkogVgFOCHy2DRzRxSj1KDwcRaCUQqbJUkrtAYBZkHSc540JuvHvjjHuUDQKfHNDPL9yMjL6cElFYPr8Aeu3%2Bo2AI3X6ZRgFDlNn2RtRRIl5As7aVmgVMkwbTNB7OnFQWT6d1xU%2Bo7KnzMw0%2BgLDZ56gV1bmkzJkwmuUS%2Fo3%2FdPKh1DUBdvNMX&X-Amz-Signature=f311f2d156e9e79b3b820ba1028035fadfca773d94ab497a5571655f3226340b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AVD7KTD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcpReRjmh%2B4SEfqWcqo5ajsCpc1bPtn2HFyUGWjQeoXQIhAJ%2BFCuFWeQ8MxVDD0kzHOkhsO0%2BDiLGxURb2fKgpXZWCKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxvzPTGVFkL9dqT2Uoq3AOcm0Ue%2FR5iy0AvT1Os%2BaeS7zqzE93%2BO5fXM87QI1eSkMw0gxgQ%2F%2FNJvFTU1I4g%2FPsws5cg8zwzMYAcczsfPNAdEai1ZFeS5F34%2Fafy4lJySHmyUvWn66gwH7pSjuPTd%2B6pM4N8v84jlwiWyf%2BVkA3CUi99YeYWfn0vVCvD6sbA2cdp00P3fL%2FW5KBP2sf44UYewfkT%2BYKafTx%2BzPcMvn8%2BsKLBe0qksZYouKGas4J3Y7qmOLKdl3WjDgOiK0D9qL6PNCV9AfovJckY8VbIFHp%2FJR72I00nMky319zgMtfhakvCCES9LyDJQ2gDA9lN%2FTGVZe%2FEgSAsYbk%2FWUVq0%2B2VGV%2BRjt415qqO8Vermsze7Exjbt5D3hcdIpNkNB9yvKWldr%2B3%2FtmuaTVfcrkksG6su7UFA5jabK%2F2Ff%2F8EJAn%2F5sN48EjCrMXeAdI4TbXbJUc5XxYdqRbWKdBELRaHqIAIepRx87wjF1eYj300QoZEeosvV1NUVgw0cw3ZlA09Bnb4DHlqm%2F5orRpS2FuYfFEW0g8IDLru6KqEWQqCPZExrXlt2U2riSmG%2BJ%2BXL0JdDk6A11UPFBb25uQqSDMx0gRdEe%2FfkuQEDffhbrmZTH7weEAXdWd0GtIo9cICzDu%2Bu28BjqkAW%2Bs3NMyvQOEhhTFHkyM8bnOR%2F6FOLPEG59Mp1IkE4q6hKvEFF%2BP4DCQ5I3yZ7OwjHZURFMDpDLhzM9yUy6CnBjSZ9IvsFjXdnDPCD4HzsLmEyWsPNGY6DNHYdJ3IOtFz9U4DcopyyzvpsSbYSRL%2F2Ldy7zqCT31WiqLwd9todkvPKR1k9QVL8PtyaXuytaEOV7RQXAB%2BZIVoYELimK0BO4q96Ha&X-Amz-Signature=67e129a5c4a21302365592dfd68ba1a6c93729806f325a7d3e41766aac927198&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGPGKROF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzld4cEGbtTN2xTi3ZccQK%2BRgteAowCTEc3T8g%2F5%2FbAwIgHtHZeFBvpvZ5Qb1ZK7KM381nda7Dov4VdXCw%2FjpFiZoqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiR9Ig%2FnM01VenvGyrcA54PAX0SABGimO2%2Bc8f4rwtRWv0rFR12iJBJ75nysstYyQiDVCxE8HSF4HM8YqncB4ZXTSsfSovMXDmg6%2BTXA7bOphNg1sYY0AWoQMMDq3H%2FGl4U9cU7rCeY6XWr87Hd10Bpcx%2BHof5DgPwkTTbt2uIP1B729U1CS2u4G5psZVHC9BKBG%2BWzXTgRQwXK8yzaareqBs3t9XTUECbLwRwIVDTYDzfXk%2FKEIIM3Z6XhRgedO1bK%2FCKhBp6vCkhWnHnLLCV9UXFTFKyMXmvzBZCEAdjF%2BFQfGb5cZUKse9YiQK7qZp7eERill%2BUsSPnMPv9gmPdbTvc5ALzF2UOMF1GOnP5Arolq0KPHuYah2O2pOPk52QoVyhtx3HkINIUMewr%2BalsyPFXORSPAmibtvzwBKsEjeqzE34b5uqGAl7Wyk5TU35qi6PABxxWCWNH78L9q63frx8KoAQ9VWyFXNpadz%2F2Qz%2BZZy8ZZDAZDYmsRbIYMHTqQ4UCKwNZ7phKcvqgXUjeqYdkj5sq4Eroat%2BigKo64miButG4SvbqinZJfXvjz1FKO64eldGwUva6yMTXo%2FjeULsXM1wp%2F0KdJRPolrjwHSkeuxI9kih5rvFL3gSe21O758xRLl9YI4cAeMPb67bwGOqUBBuCWPVq%2FrAk055cRhXj1Zi99JBtUscADyy76kIOyAWUgTOAKcViScKYuqUhkvFOQwlX6ldazeBaaG%2BPbb%2FIoBrHT5CODVxvYFTajpJrCK4B%2B%2BbwZAfLT81VcFF1zD7bJYyMlJYFlat5AEZ5NX9ImPeRb5gb%2FaSip86%2BYcoUuT94v1hmwB%2Fbq3N9ISkE6NzX9tnaXQxmR8lIMzw7Dau582yZ0ddpF&X-Amz-Signature=db8fa8bde844a72dd1f0c373c1b8f324b234132b53f0dc3b7ef08e6c6d91e3bf&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SRDXUMN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIByoHaRfK8gajh8kNcEKkvba7D%2Fk%2FPAdjZzSF35a%2BQ6nAiEAsKyiNrYSgHt64rsfRaOzVgOWquzhoH0c91W83dIHw40qiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbaTDq6yEfcgV2TmircA%2F%2FOxcEHZlBmYIAndfF4XFAuBVhdJsee%2Fi3vuSG6hnMMk3IGJer9ysrz0z4%2FwdfuRk1ACTJ1hwCSjhcuIqVBWoHbSMYA0p%2BB4IL7Kj2cjij2nM0gvW%2BQ5IO2yak5oNGEQMM16iruL4QMbhXO0d%2BgUjgcyqVQiyThkCZ4ua6R15dZtZopNQDHSy7zbLzfcoE16OhCfaml0pLa%2B0hFzmCbbQtDgZv6nBmwj0gdnnC%2BvTsciicDhIp7rt%2FgzuaS7vdXyJGfcS3MLhZfEne56t6Y%2Bsfo4Z4RlQtXoYG6YnWs2Q%2Bw1pzJeemhQEATkHNCiaF133aysSGqwIW%2F64jAXHePP7JNCNQLq6%2BL4sLn0A5%2BaAt2vHDXlHgdqAubjL9kaaNj1WqGZjAFjtAvU8%2B7i041FyYvDmOogm4gSrmDeKAExuBAMpnkx9xT9ht4pekgaW0MAo4hzFhOLkdTOtQlP3uAEXFhr7NI2nqqPsuS750KBYZ6jHC7SbFtORY92KR1LSC0c6FxcznhgsNY8CTLVMxFzE%2FVQT2jYsdJPlJeHL1rDf%2B58i6DK%2BgpZIwm0M333gPN9LdcACH%2FX7IUFP6L4dV9kuwyePMfk2BhrbOWg3Wp1AYOtBJ5wrSw3n7Llw6BMMP67bwGOqUBAES%2Fdvy6tSz03TI5Uc05CYX46iClAia0UYqWVBlusEoGV2h3zGM1plhfAGvHFszk5ugOICIaQ%2FEtgiRPf6VmRTJcWy3aWw79qDms7he43p%2FJACn8XqeFiKleAU%2FjdGICqpBmLNbtXOpEZxXJeYZNLhLMNUIriHmWJq7D1c6ZfHMxU5cJf4a%2Bj8vCwF%2FkK5epDY%2FdqKWUSGbdu7uW%2BUn7lbJ6hjDw&X-Amz-Signature=0bec9eded41b7beaf8e0019711f1a1003fa2412c4cb1d02e8762babde4173bbc&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C767C4P%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYJvdVn44WM%2Boi02T4nKv6U7K%2FfasRnbLX%2F7If1%2Fr5hgIgX4qVMq3TkyAV6QoNhXLQuLvlHBSDyxHx0VStUPfW2gQqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBOFZaEdy%2FqwJLIUdircAxwHmvwyLsTsiKcE18w%2BvOkXwIAI4MRwlq2BoArbetyV9UXAjVUqy9%2FMbWiXDOhb3cCRdKcwt9gQQudFe4xxOQsYmrGwhonS%2F8IH6FLgS3Zxgx%2F9D0C6sJrlS8NsCZa78FhwdEYB9aUpdQUy3Z6wQDteGkUgjIppy0CWneZ0A4V8YLLjL3XtVK6CmT%2FJjhI1vK9mRfoAWhF1ImSAmq%2FkrMwczCKOKLOI%2FGVeqE%2FtYP1n3HjvjOY66r9d4QJq%2FZ4LbVjltrvW2AH7DKJ5mqpEbmx7NQRJdd8vp8gHKoS4r17IXZebLz9v3IAN8LKl6yN78DwQ8nDbHyuGFgoV5TZPcRl2rttxVrW%2FyVHbBE8GKxucmFL2FmoZ5Zvl18alo0QZzHC78xzJCPICwnOa8Ubz2Wmgq77O5IVYTUmAq7PLZAEGey7fkjuIfuIJUYKw54pOvSo7ydG3dVWZXmKY2bWpaC38JJDzSg1ArZVHlhBG6JXr9Us01%2BvALSVkIFsMAgxE5MCr293OsBixKOYZtkqqGULXqbDbzuNUPL%2Fui4hU%2BmVokEYteZyO%2FA6y0qvjEGp0O846mZSurdMCriQQ%2BKsCadIkkJCWm6dC9UcQDd85oczPBUIbduO2zgagKTdSMP%2F67bwGOqUBeyKWTOk3LdnEIh9ngW5mAOKsxZil1KaVN4vg9kyThDatEFAOgc9OYgqXWjyd9V4Rw%2B18CPTXjZnKx%2BdiaVa2LByh5iKtr%2FiDfFf0eHvNJtPowmFtn4WQlD9TtBZLqHztj0s8%2F33wvvY5i1OVivIc0%2FdrqK65ctt%2Fi0kadZbVmXcLJ8sYrFF%2B8QxjreuX6YUC8V1PFW%2F%2FU2wAhTP476CQe05AqART&X-Amz-Signature=24253a3bec57117b04dea0f091657f6a6a31f93687d09da0b5f965ddc2467041&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AVD7KTD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcpReRjmh%2B4SEfqWcqo5ajsCpc1bPtn2HFyUGWjQeoXQIhAJ%2BFCuFWeQ8MxVDD0kzHOkhsO0%2BDiLGxURb2fKgpXZWCKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxvzPTGVFkL9dqT2Uoq3AOcm0Ue%2FR5iy0AvT1Os%2BaeS7zqzE93%2BO5fXM87QI1eSkMw0gxgQ%2F%2FNJvFTU1I4g%2FPsws5cg8zwzMYAcczsfPNAdEai1ZFeS5F34%2Fafy4lJySHmyUvWn66gwH7pSjuPTd%2B6pM4N8v84jlwiWyf%2BVkA3CUi99YeYWfn0vVCvD6sbA2cdp00P3fL%2FW5KBP2sf44UYewfkT%2BYKafTx%2BzPcMvn8%2BsKLBe0qksZYouKGas4J3Y7qmOLKdl3WjDgOiK0D9qL6PNCV9AfovJckY8VbIFHp%2FJR72I00nMky319zgMtfhakvCCES9LyDJQ2gDA9lN%2FTGVZe%2FEgSAsYbk%2FWUVq0%2B2VGV%2BRjt415qqO8Vermsze7Exjbt5D3hcdIpNkNB9yvKWldr%2B3%2FtmuaTVfcrkksG6su7UFA5jabK%2F2Ff%2F8EJAn%2F5sN48EjCrMXeAdI4TbXbJUc5XxYdqRbWKdBELRaHqIAIepRx87wjF1eYj300QoZEeosvV1NUVgw0cw3ZlA09Bnb4DHlqm%2F5orRpS2FuYfFEW0g8IDLru6KqEWQqCPZExrXlt2U2riSmG%2BJ%2BXL0JdDk6A11UPFBb25uQqSDMx0gRdEe%2FfkuQEDffhbrmZTH7weEAXdWd0GtIo9cICzDu%2Bu28BjqkAW%2Bs3NMyvQOEhhTFHkyM8bnOR%2F6FOLPEG59Mp1IkE4q6hKvEFF%2BP4DCQ5I3yZ7OwjHZURFMDpDLhzM9yUy6CnBjSZ9IvsFjXdnDPCD4HzsLmEyWsPNGY6DNHYdJ3IOtFz9U4DcopyyzvpsSbYSRL%2F2Ldy7zqCT31WiqLwd9todkvPKR1k9QVL8PtyaXuytaEOV7RQXAB%2BZIVoYELimK0BO4q96Ha&X-Amz-Signature=6c425313894902966c4fffdd05a92dee1461fe374306d54f7237d9d64216bd6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZP35G2J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICa7CbryE3OfwIx6CduOmzy6oJ%2Bub2MqYqXbOLe7QPVIAiEAmQXIikwM8aJzuYXxWU4EP0K903Zw8HcxtLizG8RwJ58qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDVL5i7HjyLoURvK%2FSrcA8yWv2Alp2ISsjnxIx%2FOeZ7bUXNAx7Jk6susvAFnvbk8EL021zLQ8mNfUn3pbPu3T9WmGsPJEX%2BmVFJ7Vx68S%2Fq0aidcM%2BYygDzrTJbKw%2FMjtiENvUuDlKOpFwm7vkXUAwTu6Heyik5SEpxUniBi03a1wQaNQt6rRs5ZdmsOSLUABxblEDaILEu2FoHoF5785h062Zm2Zb1Sv5NjmiGs2g9gvg304ddrSg%2BqAbnZe4MANoPI6ZX83EciXclonJGHN9b2qljw%2BBPDLrF5p4XNCROCDngdhwOlqOICrtwWAXCN64JAw25SkTvdAWh01THU0QcNWOmZdUqArya5idQN1RUTPzw0ymDQRks58TVMYfzMHcffA3pGnLLo1bKsMwf9KH21fcENBjQC39QJ42CYkjC%2B7Tq%2FAgFww31OvSoXdkFDNPI6iucHcApkhNYkVER4bjxu%2FZOu84ypRbFPx%2BFixPJ5x%2Fxlzx%2FQaFKeUFhqv4IOGHR8goXmnHKohXjEMbxSCyeDE4wTFxpJ8VQhAD8COBhJLmw8XKIh8UDTkB3eHI1BMIv17d0T6rrt7jjLtTL87R1jpTaHWj%2F1AUNhS%2FOvsmLObvUwt9qM%2BaaFPrYfUHfcCWzCGejY0N%2Fn0OmLMNj67bwGOqUB8r0aBehEU0nPuSVaJ0jIBOGMkIXHK6SHRVbef5xcPt2JkBR18MrlVWPVilzv363myROcbr2lecNjqLmy7ZOliRG9txiCmzqzGdbFHjGIAjWqTGqLQtCbKitC%2Bm1Nm5IdFAPd58WlJcXFuiiYBseBXsV8gzj1GRF4HWBEfRoon8Z37IEW631cjTX38clISObGE1EFRqz5uPqT75BusNJTwCLHkmKO&X-Amz-Signature=ea13f72b1b1a47c7e441b85811c233bcae9eccd310281a3a43199e192aa5a9aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZP35G2J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICa7CbryE3OfwIx6CduOmzy6oJ%2Bub2MqYqXbOLe7QPVIAiEAmQXIikwM8aJzuYXxWU4EP0K903Zw8HcxtLizG8RwJ58qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDVL5i7HjyLoURvK%2FSrcA8yWv2Alp2ISsjnxIx%2FOeZ7bUXNAx7Jk6susvAFnvbk8EL021zLQ8mNfUn3pbPu3T9WmGsPJEX%2BmVFJ7Vx68S%2Fq0aidcM%2BYygDzrTJbKw%2FMjtiENvUuDlKOpFwm7vkXUAwTu6Heyik5SEpxUniBi03a1wQaNQt6rRs5ZdmsOSLUABxblEDaILEu2FoHoF5785h062Zm2Zb1Sv5NjmiGs2g9gvg304ddrSg%2BqAbnZe4MANoPI6ZX83EciXclonJGHN9b2qljw%2BBPDLrF5p4XNCROCDngdhwOlqOICrtwWAXCN64JAw25SkTvdAWh01THU0QcNWOmZdUqArya5idQN1RUTPzw0ymDQRks58TVMYfzMHcffA3pGnLLo1bKsMwf9KH21fcENBjQC39QJ42CYkjC%2B7Tq%2FAgFww31OvSoXdkFDNPI6iucHcApkhNYkVER4bjxu%2FZOu84ypRbFPx%2BFixPJ5x%2Fxlzx%2FQaFKeUFhqv4IOGHR8goXmnHKohXjEMbxSCyeDE4wTFxpJ8VQhAD8COBhJLmw8XKIh8UDTkB3eHI1BMIv17d0T6rrt7jjLtTL87R1jpTaHWj%2F1AUNhS%2FOvsmLObvUwt9qM%2BaaFPrYfUHfcCWzCGejY0N%2Fn0OmLMNj67bwGOqUB8r0aBehEU0nPuSVaJ0jIBOGMkIXHK6SHRVbef5xcPt2JkBR18MrlVWPVilzv363myROcbr2lecNjqLmy7ZOliRG9txiCmzqzGdbFHjGIAjWqTGqLQtCbKitC%2Bm1Nm5IdFAPd58WlJcXFuiiYBseBXsV8gzj1GRF4HWBEfRoon8Z37IEW631cjTX38clISObGE1EFRqz5uPqT75BusNJTwCLHkmKO&X-Amz-Signature=02e69f0b0f1b4e73cc393858335a25d6e985a63767c91092408e9e45d79e76f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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