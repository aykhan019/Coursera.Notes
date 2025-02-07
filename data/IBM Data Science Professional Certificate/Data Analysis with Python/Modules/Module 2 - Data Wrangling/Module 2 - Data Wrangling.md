

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAJXSNIN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIDyG9VmbeXHe%2FG%2BLv0WlZvt%2Fyj4960ObjOxEaMOHm71HAiB%2FJmrYCBjcIQU53w8qGtUn8mFbJoA96J5p0PNl1cqwUCr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMyf7IrIU2%2BhT8tD3BKtwDySsN7FOFjCXFnida1orvLwnaHOK88CVqZx9Kd9ekITM1qITLCNaDVjEQ3uTYAdwor5YmOhOaE2xML2ZX4Lpx7QzAvPy%2Fc3zhtrcd4reP8xuOUn%2Facp79%2FpHV573AQSzhq9ukAfBWgpAgzk8g8hvKN9Hn4aVIKVu%2FtQCGwd9utuKeDReaXeFPNnrfii6vvo47Is1ioHxLLVP5tk5zHREZhimldMl%2FNShbgft8XPP4eawkDJ6klILT6KhtK1yUbdW6yNLz7T1aSPTEtqn6L%2FrkAeNDhhyp8TNhJorMtWJ3aeYNW1JLn4B31cyneTeo88VW9VNZBrvLL4sGZtVYlR3XliT%2FPbGaBWXKwxDVD4rIcJYGSUqud8m7mbwW6BvWcvATfNjjMr5ll%2BX6hYwCkbeDPdJ5T67BFmOAAlZQA9O30BqGWqXFGQQ1GPpKtZFoClu%2F7RfAAPoqG1qnzq2EuFwfjhSsd4rDP1HwDvsn4NOmwxgS464jQ7zBYPEMtvyGSA6epnB6m%2FXm%2BlCX94Gww7iDkL%2FnzXiU7Wnf5sxcJVjY81tweg24LQ0NL03Rg%2FLJtDOEWMKKLZN6%2FQPRydW26%2F3ZVK3zgAw3RryruQRE42SikOsxwrSrn5qcUAB%2FkJgw7YqYvQY6pgHcwRScUHdRcywdrewxaC2PpRnttHvRv3tHTUPgGSxyn8Pa6y39Nhp4tU99TXuNNxhHvX3FgGJq72UBqq%2F3witN%2BJPsSYppd38%2BV3%2FFWEZ429yMEJMfWVFWcdCFoZ2hOYjbRJ1LBbH%2FUsX3W2qSoCvaVhTFe5d00s0nrBzIgWtIgSZE%2Fzzhophie72TAmp%2B%2BMz0orRSp%2B1g9UO5eHhoMg1MmtxW8SdP&X-Amz-Signature=14b00daf3f031740311cd8685d11fd7836c2cf9739d57b9260240a771acb582c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2V36SM5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQD3VzYrEF9rNx9arwe%2BmweyVGvRqNE6LKsdVgRXB4ordQIgYtNKnTvsZYoqiym4Elt0cYAjTZVCRhO05agb6ml1dBIq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDH%2B9sgxyvc2Iw1lR6CrcA17Cws3Csvyq6zll6m2uGV9X11kZ3IlBqlhFe%2FDIaZ5UR3M9duks8amtEylQIEK77swrNAc0R7FLXBFOpoK%2BhUd1lX%2BdSza%2BzgZ5A%2B3tPkmHgTR%2FHVX8zMX5Lpjfl85cZbY5aMA90Evw3BCeJeXqXlXGOxmgHdhl0XZVP7gHrl2A8GKA%2FT16TkINxWAD2oKic7iUl8U9678MIRGRQleWE3G16Ri18ObsUxE%2BZS02iKqsfttTLEzKoB%2BseB1oCBdr%2FUhYqIlPMA2leQOHkIxSBT8MqgYFlVnccoS1vJuEDQfDH%2Fbs5P%2FU3mQ%2Bo4fQjZeE7ZDGX%2F7mU%2FLltigTTuu4QPXIxfB4KvcRDWzXeHNdRfAf88DV%2BdnY7VpKxIgT%2F%2FwZkSW0%2FHm%2Fx%2FCnxdDvEuCzsiD8OjxzA8iRtoZVPE6dBpsH6Fnpx30jZcEdGh0WhcSyEynmMo4dFP9q2IYLldEFQN9c9D2C8ARI0RPcLZHx76PCGk%2FPiDmvDjzU7mZPEZZ0ECHgy99PB9WshTteA%2BOeN0PQ%2BU6Evu9SANb6yvu%2FBT23KhDVcpxzgXMVQ7oBQqvhohtEB2mG8UZkoGHwhQ%2Fxu3UWcaw4785v5qEO6fJYaKOFjGpK%2F9bWBad24MYOMMeLmL0GOqUBBcQnVqhuIg9E%2FoRriWjS14qtZ3mShLHA5mZwGwYghmIKx8aujKGiVrJq3we7YZ%2BXqcYIPbd%2F68ZUbZTBtwgE0tugKVb%2Bqs9l%2F3dPonUab4WHylAzIadSGZDmv70RAWBmDnfFlBnIrOfpOwvJg7qAScXEfCmH5t135YImDCMruXyMds%2FH9ZYG9erKGDsXqbfWHiQO7VMnH3T6Du%2FJAd2OyA3URCVq&X-Amz-Signature=15e976e150889a6f6df5a85468419495a692598ffd266d0783199d33db540545&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRONDBIN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCICDKNR95KWZ%2B%2Fgapx5GMz1IR9I3PEKQFiA6nCLs6k%2FoNAiAzJbJMzTmSZjoNzR9Py3cin%2BNk5HkFTD3VbRontpX0tyr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIM4jnHN2tCKExCJ8ThKtwDS0wOGxCy%2B9unr%2F4pIGQnU43bDpQZUkWWr3bWiE95G2yoOxkLPZxykhkw2UOTtse%2B8gvleGRIX56dE1koVmMjMk%2B8GLhngFiUME59SIHFmQT964R0jY6Jh27bxGXcpTKJ1Hx1elPO4k30mTBLv44fVSdlqCrSuJQJn6pfj5s4hziR9j0qo4Q8xXQlAz%2BFJ%2B7InD2Mr90Nly1zNKSQjC0Zq%2BfUtkhI4S0J2dw7OxaH%2Fsd%2BII5DGFPDU9aO7NIhwiBDm8YaXOftaL3BnrxxGwmbjYf3%2BpMWrUiIZ211zSMI1upwhuRXeV977JcGv8VSNOeI%2BBiRtqQ5q8npYG24rqXTrpTdYQ8AsvoZYdcPAp%2BzqB3JcBNGCvwkNmb%2B7MNaphltWvOshharOJaLiNAOlN542ELtdqqy7wLARAf%2BJCkU1ogqllxr%2F6FibrkyZ63w%2FVt2P1h1ziGr8tHQLBNovuUvLJwJ4UKmsDBHGTvDn%2BbH4G4m9yXpCFLCgdlmKfgEOGMJS8ubMFnLmTNuAhNVGBfnjntiWBkpAiNx1zxU8dCMgYdzx7EA1F2jXt1dLUdxq77dwKg7wX%2FKxN8EbDa7fokdheZZBdwjUwFkgEzUgaiqw9HRQ%2BtHYBHn2PiitXww4oqYvQY6pgGZZ8KClCQyCoZsFcld0s6YugW67fkOUkGWvB84PY2MWTXsnDB2Q%2FiXRmY7kxGk6rhDOyCVw64DLYUNbIbVZK0kHbfBICheIsdZeFyhedJxCdLz6C8GHO0DOx9S42O85YEazd%2Brb6HPuHbXeY2b3og7jWyRS9o3TuGgKXoSpJqiYrThO40e%2FmasG1llfIThfqzJ%2FuHXLStuA3XSxCZApgpVwKbX9K3U&X-Amz-Signature=9e8d0caa7342f036df5b6775e7730747ecabb30a7e148a942cd2e5b5de5288e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UK4GLINB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGg7QQYRZLFKQMsJ1Hirq59arp%2Bbo%2B1vgc%2FRY%2FRNyY4SAiEA02Z3J%2FM0aPwLfJ6Hr0QYxd1%2FIl9rJObx%2FGGbeZZJmtgq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDK%2B3TI%2BpAF2nIapViSrcAxDeiHGrq8uZBE6ctw7pOHC%2BmX6eauKUoV7fbs4OUh%2BT1y70dpIA1Hg1uADciW8VcDmZGv%2BDtEbxV9OoJWDf%2F5QBZaoL0p3aCITzClHB%2FNylikdviLSFr7yO4QQzkkAyLFcNNv6qfk8i8nOr4ixT9mLuLldF8QzCWDJG8WaA%2FEutk76LYno3fuHjOzBomIKR%2FI6M2Zs17P77YBWcKQKT8zAvhN4n8YflxS23aSIKtAWe%2Bx2yiGOI%2BPLq8OqUfoRm069ydfTkO%2F3MTseJ9%2FLpe%2BKX7lxEoz4IwVxcOKOq8w1W2Rd%2B74qyC8D80CtB29r8cU3yLylMevTsWrMVpd08jgQUpGz6xyfUDAMZuRJ8tj79xr1MRcqnTR5jjXOaIWRGG20DPAX2Tq6RJU%2B1AUlDYMof9mPq9vJjRbzmxDTcOUYf4iMszIXyhSuIKOZbx7OF4RxOlj4Tc36TbCsfilIQEC7vd%2Fe047hkjuvkv9OyNQtJ4JT0UD%2Fm6dKo2Fm61EhLVigKIYq%2F8LQlO0Ey2PBR7Y9mgPolqf0WhiVsIAcdc5vANMH5NoYGyVQu292NcAtM1tIwOAeSW6p%2FLvyiYau%2Fvx6I1QBYRnl5C1CUg%2FzMhhOFp9IgAU%2BMi34gsCeBMOGKmL0GOqUBqQroF%2FkpGHTrxbmGLx2lfrnov2Lj4Y0vl91At1YJBOEiRha1%2BA7k%2FWNoBUhgZTJjLrUR%2BNd24QByKEulj3F0PFMpCbaRCh38PD9lwzfsZ4jGZ3HB%2BEVHwJg0KpkrX3hPa7JNWYyaCV70G9CyLb85noX4U6QQOPO3ebeKdH0wRD33WDMvNyaGPw1zWpav0ZmqwbxzfhNqae0kOPXf6E2jsmoSW4VU&X-Amz-Signature=d8996543094f799524dc8752b7cd3f392c81a5fe65d06447ba50361c047f3312&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623YXGSL5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDBOrCEElhvwh%2FP%2Fozm9Bad%2FGJVC5aJw30bN7j6b6mOTAIgPPvTFKkVTNFApAZXXgizbQFjHT%2BqZvwXDDisP6NaFZ8q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDF4SnkF7aRVGqjJcoSrcA8KsjetLj0W0jUig3F00R%2BgDx3C913SqqMi%2FJ0iKsUsU5G70QxOKl7cNslTysLbkxOZG0HRN4WOKW72TV1UjCkiw5LWyyiR8%2Ffb%2FY8wSGkDoo6EPKqZTf43%2FHRH6QJ33prf12P%2BMPpUouQOFbkffx4077L6yAT7cO4YM2We3iXlgI2nakI1m15XnhrO1znPZA855vUR8yC7uNGHysrjJSgf0raTKchNc7ASP15rUFgANA28TGjChOXYs%2Bl2HrDX9UcX5P%2FmtTYYyIEumdOcg1NMhX272CU3tQYAp2hJK3Reu4Z6RfEP0xuNAdwneE4LLIts8Xb50m%2FKFQP50CinKDajfOQsiehKkFMIkK0JnDcFw5YDg5wifYOktx0NExnHzMg%2FJOWQm9zbHlLcC9OZAiloJt%2BHLiozlv3RRhweeAzzty4U56Y789k07qJX%2Fmu%2FyjGOeusyfUmCejsIgnic5RpdUMtEr5G5jEq1SzUL3yz%2BNjQybqYlLQhViwpe5ScyP3uxlM8jWNIVmgR8%2BxTtSYpQZwkzEJqjwma9anRn0pdnZZcgoYeSfZNHWFyQWbxHUdtEP0M51Nkmi5%2Fy7%2BxB07B8n8%2Bh59ZhIRN8%2Byh3eZ177DcM9tvJRgzkLq28mMOuKmL0GOqUBdU9ibryjgVpboFka1ukNewJDbNKkoTe3pgi4HASV0HuVkAuCjmMqpp1%2ByX5%2FqpvNxTfEbN%2Bt5DzV50QonIgywBJnaGxXSI4Z%2FMLMBEMgMuw9%2FYCMzk0TOcgyRRDNQItCEY%2FjxldIqdDfDr4ddd2Rdo2UUzAToSGTy2Ho90269LobVJX%2By54VrfYYznmJJQdpjVNGjCOGzFfOUfyPEiWEaUN2%2BOP0&X-Amz-Signature=2afadb4aa98d86e437398a6cdb4b518c6d91f2376d731460e1d2dc564940bfa4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NPJCHTJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDmH23q7Qtuk998O8t2I%2BBis8I7Skq%2FX2SbDut0TM1EfAiEAuFlv%2FutF%2FKSL19jUROT4nUPViAdpuyUH9GIxeIuEx4Iq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGx1UmXOtT2wniU59CrcA55M5KXNfAwyPP09RrUJzhdp14GCYVlKFR6EVPyoslD61pKrKSViYhRhGFolYUP6medlS93F0O3tVrZDu3gBa5JhkDHIbNIAWWT5wa4G3gfY8ipyV%2FBFJPLk8jJRx7kwPaNKrQ4Mn%2FdbQC1cKej8WuChkBukIEjJyWee2EMK6LZ1FpaqX%2Fighar%2B86i6nyTet0LUxK7GADP%2FjZFhnFuH6dQnmVvbCp%2FTkMCTWpnE%2FiNKiEujUSChtE1llyc7BlPzQy6%2Fphg8Zs8lQK%2FshNu7Pdh9EKn7cMaCpRITbLGJETystCC3ZxhAXfwNpuXrEzENRKHxjfaNUaIflGT1VQjae7HgH9CJ%2BCp8W4C4GyOJlj%2FVFJGLZNazREeDIlF8osv%2FGf0NrA959h0B7YrjLnIlkYt%2BatrhFCKT6%2BwtvBFss3B9StL%2BRgjtiag2dN%2Bag0se2aGprhRj7%2BGWsFNS3o2tZ1YjIobBr8%2BvWeg8efE67Moy5ytS4vHgLqEwCIdP0hAQSj4L6x4FLsLU%2F3SrymSdG4Jns3np6kZ5e9%2BWdW3WnCO3AzvESbNAGBOJtwScTj8suKsL1bNWoi8Vn3I5w21O8moNMdO0OuMEA34yPsAN4YF8rXP9Qh8QAJK2BaNsMLiLmL0GOqUBwM3jV2hYPFDN1anjALCjJTfsnkBGgRh0cqVq3aB%2Fslo5lmXeQ2IWG4%2BzurBz9CgctbZgzSA9dP3U7i30lOuM9fLqs3jn7yDrgqWKjPfuaJuXphrayfEOzpXSdFgrxZPadnbR8yhoO27i91U2uLHTST28mDQvCPOaqRli1FZAh5XvAoZ70tHk%2BYU%2FCKv%2BHgqRu6yerWOIdb4af4NbXtJewOEEtYgR&X-Amz-Signature=14a0b5fbc52035bbfb3f9b32841aaf15f82ebe2c3bf03f6abf98512f07bad44e&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOU2OQDB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCNLGyEu08WKrLWey5gH4ZyL9feiqT%2FgA04oM2YL2t3bwIhAIGW9xNHSVSE9Aiz4HTn1J%2FhNF%2FEOWWr9dxFhvVMTMyIKv8DCHYQABoMNjM3NDIzMTgzODA1IgwxOIzYWpFwFOQFIZoq3AMYqDrUE0dRcgcDe3LPd7zf5nzrxgnToY3QdFTvxbdtury05w%2BnG0s6qac8tP8JJg197x2MMfFhtGNj5auvKDwMeVD9m1J56S4d5Nnuoe5MFJWAQPu9amG6xk9Rlzk7N6XYB72%2F3845km5b%2BJ%2BU5NQuiSGTXz4VSKXBXPBf3mhUItwIs5tEMrvbRGbjt1hSbo34iBO9pU1%2BExZ1IQ9X%2FE08HZrsMvXv6FKtmjjJip01gMXqkrq6sdzHR6CuIdrZJUtFtNKLCBETco8eujwjK8cV29X3GihvkhpEy26eZ5KftCqPoCLxiu4GtQnX6%2BDrUPmo0zSG9QyOBEr6I4pHBwFw1YjyVOtx2yd2jZFxcZlecXOhwmf4kGu4NMFaIRQjL0Ue3oB4eOY%2FtJF5%2BUvt0FVEHS7wRtASlch%2BBVTybRMuRTQsHhQIAJHbMVn%2Fak%2BEZY4SwzuVeRw7IEIP4TMIXx%2BYOyYzO4hZnBgm%2FlXu8lXF1D6duTjlg0qGAShCIGCQ9zo%2F6zBeg6zd%2B0f0TVmL3ju7WE4on3%2FSy6I2GzNQ1BAdlBdahq0BHAYvjvWJMdOlNSD1wKIbzFCaffpi%2Bq73zp1%2BormIAPnUC9rHaODMjYeq4BA0loI7gEJcr4uw8zDgipi9BjqkAW3LUp3QTLqzRJ5QV4ZyjylASazWSAxjVqDDTPLr3j%2BzaCoejcFPfAUmcL24rbrhkcRI%2F7wAnMANGAnYs10JljD7RWAwaPo7Ut7rdNakLZ0jMJ5N%2FMb2VT3eezmTMNLIOE8eTv8eouj5SpjrZ2XdJeHmKpzBbBcbETMQyyh6LBDWCWkSA0Gll7blUgOYIjaripXXP%2Fg9iacG1oPY%2BvvbNW%2BOKcOx&X-Amz-Signature=53899c890be1f978e86e2888a66625b1e20e3705007b6161e89850b4190b29c2&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCNIQWAK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFyVqBJIrGAeRDVLaNb%2BMn0OeSTKlEPWqkpspX6%2FlnvjAiBZJ2rQPsN0oSkYl1%2BNvdlzvisxAQmHFgFUMTfMzOnl3Sr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMdO88ZPmqJow0Kng1KtwDiV5QeylCEu432FBDzkws9Z7bl8cUpXygcmR8cd0f8dD%2BGIYQ8hhGN8wHvrVlhlnSvhrCFz1SAL6dwCX51iHGLPx9ep4YvNL%2FdW4ffaFKwiX1UilDK7VS2XsUEid2d0j7zqcOJffeofITTIOVkAUvE4Q2UhxC8tT354b0rIZU5qWIHxHju%2BJTccuRJls%2BRIL5rh1bMRQ3I8Uf6hPeugWCleuF%2FshfTpOllqjdiDIz7JzzkKd%2FhBvfQfF8iFFXvS2WpIlIsQXJAdBmGt%2F1Fq6NdKkh6I%2FXXSy5EFdWZHF7pmDJy6LyCk0G4cVI%2BduiWsmEoQ%2F4iRK4f7FkuX4ze1N8aMPs9FbQ4nDAXsLypilEvNLFCYdc3%2FEN2wPpTN3k6nuTXNPUmtKUkcFdMsNUOE%2Fj9KroOuiFOfqJGa%2B0v4VgptAwDxQd2hYBVMAVuVyL9DRp6sxwgB82JRqLLLg4DGKU%2Ftr0Tu0kKDH0Tstte6%2BZchG5JvQJ0fWb8KTES8%2FMtPcRy5eoZAPiZCrY0Htvot9NMNibOpSElCDOfFcQGITqzgKjtGlf2vR468P9Sj7vfPjwOGF9q44IkH0IoHJq%2BQFlfzGB0cagFoQEcN7bHHtWOKFPguCJqWvqr96Dkc4w4IqYvQY6pgHFUqhD%2FqUbfma4q6bA5R808Wh5i83gDgl4Q0FK%2FDJc8THCxdt9aAQl172CdYS92pxAly0XavQrujwQgM7wLTRqzbOc6Rd%2Faw2LzFjQm%2BFIu1UptriQ37z8EJNNasZjlXlX5EWT%2Bppk%2B45GxPPhwER%2FyrLPbq9C1r3vKEC2TTeULJcHZoE8rxcyeFAl%2B3ILLNj7Tx4vJXh%2BnYalu8sfN7t02RY70dW%2B&X-Amz-Signature=7519966d63478c283edc96f9c1343ef624818ee6a819072ad8e42d87ad579f9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623YXGSL5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDBOrCEElhvwh%2FP%2Fozm9Bad%2FGJVC5aJw30bN7j6b6mOTAIgPPvTFKkVTNFApAZXXgizbQFjHT%2BqZvwXDDisP6NaFZ8q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDF4SnkF7aRVGqjJcoSrcA8KsjetLj0W0jUig3F00R%2BgDx3C913SqqMi%2FJ0iKsUsU5G70QxOKl7cNslTysLbkxOZG0HRN4WOKW72TV1UjCkiw5LWyyiR8%2Ffb%2FY8wSGkDoo6EPKqZTf43%2FHRH6QJ33prf12P%2BMPpUouQOFbkffx4077L6yAT7cO4YM2We3iXlgI2nakI1m15XnhrO1znPZA855vUR8yC7uNGHysrjJSgf0raTKchNc7ASP15rUFgANA28TGjChOXYs%2Bl2HrDX9UcX5P%2FmtTYYyIEumdOcg1NMhX272CU3tQYAp2hJK3Reu4Z6RfEP0xuNAdwneE4LLIts8Xb50m%2FKFQP50CinKDajfOQsiehKkFMIkK0JnDcFw5YDg5wifYOktx0NExnHzMg%2FJOWQm9zbHlLcC9OZAiloJt%2BHLiozlv3RRhweeAzzty4U56Y789k07qJX%2Fmu%2FyjGOeusyfUmCejsIgnic5RpdUMtEr5G5jEq1SzUL3yz%2BNjQybqYlLQhViwpe5ScyP3uxlM8jWNIVmgR8%2BxTtSYpQZwkzEJqjwma9anRn0pdnZZcgoYeSfZNHWFyQWbxHUdtEP0M51Nkmi5%2Fy7%2BxB07B8n8%2Bh59ZhIRN8%2Byh3eZ177DcM9tvJRgzkLq28mMOuKmL0GOqUBdU9ibryjgVpboFka1ukNewJDbNKkoTe3pgi4HASV0HuVkAuCjmMqpp1%2ByX5%2FqpvNxTfEbN%2Bt5DzV50QonIgywBJnaGxXSI4Z%2FMLMBEMgMuw9%2FYCMzk0TOcgyRRDNQItCEY%2FjxldIqdDfDr4ddd2Rdo2UUzAToSGTy2Ho90269LobVJX%2By54VrfYYznmJJQdpjVNGjCOGzFfOUfyPEiWEaUN2%2BOP0&X-Amz-Signature=bfae0bda6dd32fa522fbd5b47739e5e875757c187ee839572431baa819f3d8df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWHRHYVN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCFyuo%2FGqbN6jM3mjM39Xruow%2FONs%2FXilx39f2jTG%2FTOgIgTL%2B7j9ioDU18kLVpwVqbxAiBomjBHQe35xloe05p%2FH8q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDFVmNz%2FUsHEShuwUcyrcA%2FKo38Z0ohNAtd0NBVXyrT3%2F9e39uaNEBlvaUY1nNw%2FOmK9eettMBm3wB7WwZGvULQQRLQ7pfiTtdrWn3jl270CV5Umyow3hI2%2FpBrvGJAf8hgtLBDZ%2F37CRbMKGtM8FBH%2FaPD40ksIqgFVnz0EHoLOlq87SWhRHVKEwrNiBZk%2FjnebM%2FqdyAG0INtd0JZ4%2Bs%2BoyoyennjqJgHmckn3hlYQoU9e7gnbIgmimp6g8QwD8mq8kY7mqZyvwDX9cXWdIkNaag%2Fd3NPySF5gGYlAjj6goqh8KwFiwJzwsYZdhl8xnCCMC357CCFy5dlnYIekIO%2FzNPCN8peE6alNboQ9eJ%2BL4rtlA1HtbFA8%2FQmpf6oCRHaj%2BwzhEvrlBdCEpp8qug%2FiBcJaClJ3SzGHPps4o13ZuPjnMzYAzY1bZAOwqSlqHSSSkoRRsxNKNnwazOlPylOHBZR85IQG1e0SikHO%2BFgSZlPT1z1AVheG0byfIq1leeWaX6lx2l64Tx9b93lKKSMJEPu%2BA7HvWnALzTB3Sr7V1yWiTPHGtGn8OaTr5Qs89ef%2Bt1cjJKJ95bc8B1D6hnASC9lLs3XVjRefNVH5qFIzZIrnMNCsxwAL6g1y9A9I1TBeJ5dfYlZBDBdz6MNaLmL0GOqUB%2FN77Z7GrVkhP%2BZ0xB5E4DxYOEps9EyZw%2FHMJLNKsP7z7zdggKDNhRw5PjmR6YlNq5b64ta9M%2Bx5CXdxONEEd8A%2BBshgMimJQjmL%2BHTqwrfYrpRR7aqlbRALBXEx%2B0IcrR%2BSU%2Bk%2F7Qvs%2FJZHh%2FCzdATA9IjvIsV7jq8XuGpmUGfsSezUjSp2nnZzu%2BNV7xm8uR5Ld%2FNZWOfC3yVp8BMC37C%2FzwWIe&X-Amz-Signature=79e08a807f0a2ad5e6e46d48f5c64da5130aadbde1b45594d92c9645ea3dd4b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWHRHYVN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCFyuo%2FGqbN6jM3mjM39Xruow%2FONs%2FXilx39f2jTG%2FTOgIgTL%2B7j9ioDU18kLVpwVqbxAiBomjBHQe35xloe05p%2FH8q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDFVmNz%2FUsHEShuwUcyrcA%2FKo38Z0ohNAtd0NBVXyrT3%2F9e39uaNEBlvaUY1nNw%2FOmK9eettMBm3wB7WwZGvULQQRLQ7pfiTtdrWn3jl270CV5Umyow3hI2%2FpBrvGJAf8hgtLBDZ%2F37CRbMKGtM8FBH%2FaPD40ksIqgFVnz0EHoLOlq87SWhRHVKEwrNiBZk%2FjnebM%2FqdyAG0INtd0JZ4%2Bs%2BoyoyennjqJgHmckn3hlYQoU9e7gnbIgmimp6g8QwD8mq8kY7mqZyvwDX9cXWdIkNaag%2Fd3NPySF5gGYlAjj6goqh8KwFiwJzwsYZdhl8xnCCMC357CCFy5dlnYIekIO%2FzNPCN8peE6alNboQ9eJ%2BL4rtlA1HtbFA8%2FQmpf6oCRHaj%2BwzhEvrlBdCEpp8qug%2FiBcJaClJ3SzGHPps4o13ZuPjnMzYAzY1bZAOwqSlqHSSSkoRRsxNKNnwazOlPylOHBZR85IQG1e0SikHO%2BFgSZlPT1z1AVheG0byfIq1leeWaX6lx2l64Tx9b93lKKSMJEPu%2BA7HvWnALzTB3Sr7V1yWiTPHGtGn8OaTr5Qs89ef%2Bt1cjJKJ95bc8B1D6hnASC9lLs3XVjRefNVH5qFIzZIrnMNCsxwAL6g1y9A9I1TBeJ5dfYlZBDBdz6MNaLmL0GOqUB%2FN77Z7GrVkhP%2BZ0xB5E4DxYOEps9EyZw%2FHMJLNKsP7z7zdggKDNhRw5PjmR6YlNq5b64ta9M%2Bx5CXdxONEEd8A%2BBshgMimJQjmL%2BHTqwrfYrpRR7aqlbRALBXEx%2B0IcrR%2BSU%2Bk%2F7Qvs%2FJZHh%2FCzdATA9IjvIsV7jq8XuGpmUGfsSezUjSp2nnZzu%2BNV7xm8uR5Ld%2FNZWOfC3yVp8BMC37C%2FzwWIe&X-Amz-Signature=75ff6e73be6a76ab36e31492ccfb91d7076b9589a4e169eaa1b8baac5d66613f&X-Amz-SignedHeaders=host&x-id=GetObject)
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