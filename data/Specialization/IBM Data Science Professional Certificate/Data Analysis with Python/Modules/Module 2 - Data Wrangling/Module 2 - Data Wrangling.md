

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDLIRX7I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHS8rd%2BEIyLO%2BN3tHk4KnVBMXo51b2oxwOre%2FFrPkeb1AiB3rJNyCIgiLg%2BPBrVxRkLxh%2BoBzvkfIwPApn7IWgXncCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAHNw30pupLhqQWC5KtwDky1MnZodDk3kdEtFrdtsF77FHPA3bAt4i9O3d2dVC8oGH%2B%2BUEzPhpLmghq%2BgxXeyfbAiEkqtKuxszaGinUAsmJAvpA8SUbQfvy4cFNUvKK%2BlykVc6ebXOrY4lFE%2B3Qh%2FFWTK2%2FU6Jr21tri1P31KYGm%2BOtLChs35hQ%2FumrXGpHltS%2BpkLmp%2F7tMXup8kXfn%2FqstJiEX0nIodtuOBffMlrOt1kcsSoQxiPoTLY3JDeJy5tu0It8fP61MLC2h8CHKL%2BnqCcdWqun6nj88pKFRss0PnuVA91P48%2F1HOpPkjC1ow%2BwuJ17LAjQTJwcsT2Vg0ZaXFYRqXYuhDVkoR%2FV7tb%2FaB%2Fy5QiJN9j9dsv3f%2BCFr9nZXzqNAH%2B5L0p2s5sZJwBg7aiFMusC%2BCnWzn7yv%2FJz0cmcctCA%2FZpIoSZLcJsAdWSditlA%2FOnNwN4bZPGF98O67pJ7yEYp%2FufuQZyPwP4eyo98bWSEBazXExxVFZ0%2FbbOC%2Bbb2FHtpbxH%2Fjm6JA9kE88hdygCmNPsVMGQGamySNGO6AzODFTn82dgTGheHjUzOYKhIXzENP0jYYmcA%2BTMDns2DmdGm7VGRTjZNkxzAcgVvgtqeboWKo6IwOsMN%2B2mEAWQx6B5%2FSIqTEwubLrvAY6pgGBXEAFc98gX38IkxZacTj3eAweS%2FwVHCN7XR44Q1abVY7I3ezXP2vkSKgW3z7wR7DASoLxCJzP0V%2BC2ve9i2fBAOKBV0lTmCA3BdYuoZsR70tgEC0fdWrbj32%2FBJDxMZRjfBc1JsLxTR%2Bred5mopV%2FQavDfuUsoyICaI7ndwtnPiGiHcFak2Aurt2eDFvAYr%2FzTeXQVRU%2B8vD%2BY%2BhF9YRWfMcdr3Fn&X-Amz-Signature=c99d4392b3e1475ff157358ffc390fc5908fc21e244cf2b293621954c6598831&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6L7D7XY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEBgZpwrInV4odaA8gfHF8LWiTuI7vDSyO%2FIeCwxvE6mAiAR0oJkAC8BZFNw%2BKG070oMJVWD7xgTCTzME5YdVvtAxyqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXPDQqLU0h%2BH%2BiLrrKtwDfHHI3U9vCt7xuKBCnatqth7VDdv5AiJh0iLJhGa9r%2BBq7HtYIVrnpbPYQfHqbYihaxNh7M3PIBQqff92Th8ARDm1EJOHR2Gh9G7AP7xDZMXfdeUVbhPvvykbxtpLoFq7zaJQYNstXvZx9a0FAu1XmgWuU4RY2DFv7MWLFfULM%2FOLFBhfBA2fFnlxRJ1d4YNoFw4hKT1kjZ9J7xjXV%2FMs1TmqONS5tdb3DlNOMq9h%2FaOtSvasEA3XmYuASZMvYg7yCN%2BIXFl3aw11TWLkX68qWq7KJqtLPGo%2FKstJoKtESudnyo2TNXCiSxY1lAY1jYUD8NNI2TQIGDI63OrCpFQXipztLMI9CyYkywHg2oaEWo8LZepapZ0WNAM%2FtFFe5HcBI2D%2FkHQANyLcPrRA47gOJevIeKDeWZKZvdoEgVCRifMjTWgrdbci7Fq%2FYgRzvdFsnVqNlE2V%2FbjfngHEF%2BveM%2F10V%2FzLp7xWfy5WAZJfyf2uXrNnobSxmFd6%2BwawHJT5HUftDwqhIGQBZkMU6G%2BDG%2B4SOvdzivV1sO1J99hM5vtrWBpNyK97onmuSsT2ciBrpb5zt3z8srdrl1KIqVl3jnVWN7rSMKZrtcSE2J0LfYKbw8gg9wWXzrmTmvwwmrLrvAY6pgHvnxSgdufkzyP23Za%2FCJhy3PPcOeXs1Mhk6G%2FhTeAhCpZYVjb5Yyy60m5Z8KbLbgVVqpoXfS2q7VfadkGzKfjWO2GP376XYeiV4rBbzuYACuD38TC71S%2FftiFvBPhDNgohBYQRJ35OROYRz9Oo5kNT3OlBFPkE%2FCIezEHg5W1lUKtOPfo2%2FaXfHQWZcgzyzfTbeAs6uhrZ9522WM4O5TJ7mGJdi4I1&X-Amz-Signature=bbf8f19a651aceb48288415334b5dbd0096b5e79663e2df0c3d6ee2730ad2230&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVT7UYLX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFD8FV21%2BGLrolXwwpI6QFkSI2yF%2BAAPtcqOFgZeUozgIgHdaCvz2zBC7E%2BpU0541cuFJuShEfQg%2BJ%2BhI%2F4Xta8%2FUqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDV2IRvJiOm2Mye0dCrcA3p4Bgfm042M4DbsNVSumD5%2FkhVZYgK%2FJdS71UB2agalfZH%2FaJUsQlmNKGhHk1QbQvWjpT2aSqaVdN6PgSRX5xPrHfh0qbF4SGU2j01y7iXlOvr21wkUy4glIwQwDnB4amudrbxOUutzLqPQ2WRuPPnLJhbsX262DgW3JKosbec8Y6WZrkgeJlBJefB2%2FDnjyqtlawIbhxZEGTd%2B3d7XhL%2BsUO9pSGPga6Hg7b1Kd69jugrkxziEUnFjncAAkkLNDo06Dj2pcKhT%2F7KdHlsAnP7pYTA0T%2B3kJ4VxCUJGuBRcvJ5IhRMbMVq%2B5Z6ZL74VpHtCHvpXt6RpWfjUwF54P3Q9uC1x%2B9zQxLaPE%2FBg0ujDnqANSsicVL6fOIk%2BNb%2F6QVWd2slIZ6IUtAtfc6gtHRNuusD%2F6dxdDkbgXB6ZIeJZq2XensKDX%2FLhhKCrlmAWmRd3vmAHdT2gO%2FT1mSg4J3mlvtehAMg5fhZt%2F8NnebmNeL%2FPprz9uU4VdULTtD8N%2FsG3HOIvNtwRNS1AQa%2BYkDR9H%2BuVqMf6jybxRGciEfDViNDXWWI3cO434Ou2BHnik6TPYxAHgk%2BP7VY5EUU9vZW3W%2BeaoBwnKzM8kJDCkcRD9zywwMFZv2c2jOGHMK%2By67wGOqUBcx64Hb1Na44pjLrDL9RaDhAgk3CzQb0KVsa1Mxgw2RC4edIbHl74doZO0wDAza8UuhDd%2FoIE9f6zUMfCd3cugAD%2FcEHSRAEimG4vhJiIIwEEfDLaCZsXmmYXesGnmicU4tqxufimZl9yZ4bhTm%2BsJvIqamBQexXlUgydL8KOUh%2Fzv0aVdaAHu1LOA1NhpTYWEx2fhAUJvLUoLOeB43AsnsyKC5XL&X-Amz-Signature=afbd1b41cac074d1f00bbe8666a6269f4514dfdff699c11398b67354974da2d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XS4A3ZQZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZE1n97GEoKgfwTVm5dnbQ9PK2OySzvLc1Tb%2Ff1tozygIgYL4imyb80LuR9FictQkC31oUSsx1ApMdhvsexalIgpsqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFV5zZF%2BYBP0cRAdnyrcA7xudHbJJZi1QfyxuXSp54HyCcrfZEB9AVnHx9AiGzunhtiNm3r1g3QXkS39cnNJ2OeCkJdzj%2BqcEkxJKtup4oMJ1GtEnbCeNxC7IlXQT20Hfd2w13%2BuscDA95q0Ut0ZYmltGRUhm%2Bm0K2mL0AC00k1HXOwglQZ5izPTLh1N4BrXKHoNR88eIKGzEiVPjIAAMSxpLNZ9rkVJNL0IwEPscBD9T9TuiIRo1c9rN73nHn5rnnhTQChcjcwfWIw%2ButVdxvjVRg66PBnmYg5tUE7kawl6mZS0RsgC4QsWRFtw3rAgWdzYplyi9UPyh%2FRT6xUX6ZEMa5Mr8xON6M0Q8936qgNS5WcVjFlJsXQH7fg3vwZ1UYori1Lf8AttwfAUvgwF8X3Yz0I90JH%2Fc%2FvYWBDjdpTxr%2BnWlERBneKLzcD%2FXffAhV8R6xucMeKvajHaN0Zd3xbiMjnnppmGXYM2mdAIFMPCapX07BGpj3oIkYQ18CdARpBbKbd4CGQUXDYvNGkSqKVFw9%2Bx2toIjTt9eoY2jmWOIw5m5HuYbhdyTDFPpwpbuC7bk7FEDJto2Yb6ycsKoVSIi58eYFmb76fjYP5hrQUHiUaVO04NkcTtp50CJXYEDO3qfxpqlkQeCuNlMPyy67wGOqUBldL2nvpn3qp%2FcRoTc7BlMrg8taHb8LJXBibGCXOa82KH14FmM9%2Fyaa23Vy2GB3H8qEOLvnip6xSe%2F5L6RIbN2XhaqkX32A5svmGFUXGG4Nu7rAWHzgA4XINlq5w%2BLWJ02ruFA7eLzUbW3y9Z30VT9Ty4HXZ0pVxWbIzFTBZTtykhHbtE%2FAbpjSbbI8f7y7hWS7rd0Sjpeno2Nhh9tr61ndmeLxQT&X-Amz-Signature=e20b718f979f25ef2c5ae70b1f0d2109deab82748ba632aa0f41be387a088df4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YL34TQ6T%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG370%2BJuXqKd6N7CZln6nzZO%2B4Yj0yjY%2B0r3FRGSbkh1AiEA3zIlqJoubFtQduPXsxKpfX5j4AeiKYx4tBg1iS%2BbL90qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPdEMFhrS9E9%2FIIvRyrcA1JSfXwSsDwKXP%2FcbtItOl5UWAlkIM4a6Ic18rpaEi96YOSfelo5Z6mqRJLj7Iflo35c7wBb7%2F%2BYNyPn7rZDByEKYJ7v5E9YmUXZsnyUzLLC7wIkhIT01GNm%2BM2VSwT2YvEPgq5YxBNwQ39o8gSTgUlH8BEe9PpKEQlKhDUvg%2BCQkwCRfav0uoIookX8C1fHkHDJlKu9Y13h3h7uUKXpPDmowVUVx9DRlEC8ek%2Bc9dcwiVUG0TDwOkYxAyj9YJ%2FKFKLEQRoLxixbO6frft915BaOKgRk1sjOjM2sVs5zerhcxXjdFjRsFaKnZpLEwP0MdHDeBziUtBXPBwuM5mfujYQh9Vjx0v8qdS%2BF%2B8qJCogq7yhO4STNMwxghPmpyNhOyK%2Bqog%2FoWghwbQIY4d7f1OcqdZVvpdfftJGrpyBu7FB4TvanWX5pq5VbFDdqGZQo6DfRxcHT7ITVXUJ6ERD79kxWtOmrvtPikVcwgIpGOiKxFO%2B8ea%2BwXLNTmDeYAK%2BRSzdUHiw3hVm7UbgmsWrqmGBhGtLvi1jk3vnrfc4GDXoxSfwHzu%2Bu1MqEjXsU7t0G6qBqXWtC9xsrViI7FW8p8CXc2GBGxrdxjBoZ%2FxZdfaR07PovCdW%2Fo2XG3JZyMOWx67wGOqUBABgSiXk6FAABSyHAPqv5ZA03EVjch6HVza79UXdrNULBG5rbI%2Bk3e1uxzE%2FpCVtZczy7FGtEK%2B%2BUpOi7rnKwo5dUuLKLONohAgykkFjHnGqfSWsto%2Bm6%2FBpJZEfTbMstHQD0i5frnahFfVefu4uPe2Wu78EbrMHwyNrBCraKGkixIer8iecQGyl6RMnmyMhjWgfoDH3RWBh4jgrqT6R91hSNijPV&X-Amz-Signature=88a4078be896914e97f4fbcf409b45556187ca105609e7137a135edbe8f02bd0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MS6AUYF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBA2JbEAq1DmH4bGDhmumnDapJnmcW%2FxBvWjxw5llKwRAiEAhDfLL8pywVb4%2BVcIr%2FI3xNZLTctLr%2FjQ0F8%2BcP5dkckqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFqUxl6gYThAyx%2FLhircA%2Btro3OK0jqZPG2SGezdqFaLKBi5HIC49J8%2B%2FNpWQ8JIrRA2t%2BClWmAGtbjQGwVmM4JxVeemeet7MqU9YXgPSU%2BEt7rG9G3MOtrUNJ%2BF9Kc5uQPOpm7%2B3TL096gXJDJ2QB5I9SwANuJqWLEvwY5Y352CXcLYSKAXCATlrkN2GbihSCwNyAB19VXtkKoMnVY9n%2BSm4GYXGAD2nIrg8daP1qrFj58Wu8ZbSF3lBVdi7KVTlaI8QPvmiSmXWHBSz0PP%2BdCLdabQW%2FjoOI6XmyYPJm8kCBUFaN7gMTh5TLx7GXYLheS66r7bW82FLLh0PS1oHVwSR5BKO6khwvIRNYcFnrspf7TX%2FyP5O3fg89p1E8mfY2rlofSarovInfj5O5kzf7mEdfgjTdRevzBmh1xpPuEfG6NA2zygYGTKZEXQ5NdMm1u4RFdEgvc2b%2BLP4pcU%2FzCIdeWz7pmTPSrz%2FquhjL7OGcuPNyVeaoXjFhg%2FJlTvbWZJ61ZE49OEiIi43WW7x4f6FDp8khgAjmPoG3YewkcaWGs3bz3WfzcVDWrI%2B3AvQRtLxgNNakcrAeA4c5gttBcBEBMjgTSTG9SecgZ2WJ%2FuBRfB4YxPEuM9XcADD%2FmkKWZrTkGnc3nBluXsMNqx67wGOqUBeuTzSHqYSJaI4dI3rkJVA7RBT7AIeFt9L4njGzKekQcC9H%2B1ecE3zURJMGVBVV1bvypQO%2BfY6ehHwiCl1LxlYiTO0TqoKtJl%2FQv9c2yjixJUc8b%2FCYnQK7DSr294oDIhCAHkQgEWUS6t8K9ypoouAZTl0dniKewnw1rkXNuRSQbzHs6ylUGmCCJhaDzwtAfJymIy%2FIu3XlT4luzThpI%2BNPvpT9zI&X-Amz-Signature=bcd07f447ec9ba206aacf246e3d1df8d90499663a692bc1512c3081556299f8e&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FZNFPT3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9fOIEmmqLfEJEbGaaFhftFG5Hx%2FEWXu%2BjP09hIu7UlQIhAM2nsbKHopjJ%2FN6i4gTCNOXb3sVJJ4w07CB%2B%2FBK5IG3%2BKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhZReW9%2BiMyeXuqTIq3APdQtf8bkn0TtMLINn1fgbCuyRGFssYJgzB5KE5N7V52MQ7FoamTF3PQmV%2BcGegHgLaqbE85l1xUnA%2F%2FFyvdhY%2BF58XH%2Fpkcy6UISffahXFSznyA1%2FMHF7ehDWCxc2%2B8Sy0edAPUOMzOgashZ5I6azV4ic2Gzp5MwaNkmQlpwc7ImVuuQOT2N9Fr645W2IFMkNQE2F5X%2FMyWaB%2B19Q2y72EWOT6sdwA5UQ2H%2B18Xso%2F1GEURAdB9tBcHTIwjPSJGT56mCbbb3rCsFewbK9ZFVEcTGz8dKsX7KjItZbtknUi626dG2XbdZ6f74cCipW3%2FhDBVJxck4WNRlj4PnGs3QcXzA2j%2BiSHr4J7F%2B08RbluKCbkWbEW1Nil75L0pZ63Pu%2FZqhl0e6zM4KTx1f1y0e9R1N72%2B4XfWO0mWe1dizDkGkzF4ib4J5JhE9DengPbAl4%2BdUX6Yhzf4grF3RL%2Bu3txZZ9gttGrzFnCCDvv8UCOqT6sAwwgYbcqtOX8T3mWxz3bu6%2FfrXIkcJxxIZQ8uwr8hzkGj4BwFyymvLZAFVJRjuL%2FuE8aeKFdSBv0h%2BBA0IgWqEHImH7O0H%2FMnfrBWn00sjE41TsCET3efx%2Br45ZDPTX6ASwceachbCmwKjCGsuu8BjqkAehjGlnHIEjro2%2FZmMhiKJwLRYzrJYl3z3Y93myeKXv%2FrC88UetPVEC2ZvU2iP2j5xrJcpfgptkMNxLIh0iJjrk2vWuTZqNU9WlynV67EW2U26suT2UJow732owt%2BQKe5%2B7AxDrl1xH630k7QlV7ZqnxkD5pD1ESyU7FfIffitIEtz%2BTfhEbTrrWM7bQa%2B8WUWUlthgW7mPc0nI6xA9s61eiHFCu&X-Amz-Signature=c188c9a06ac2cc9d5770202ae053e08afd9b8e5de96b1a0a31aec4cfaa438d65&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZULZZSY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGCjuGZj6wIQOoF0Ig6XixShdieghlf6l842yAcJgOdkAiEA5DFJOB4dKU%2B4BtZ3fSnp%2BtNp%2FM9f6WioheWvIl04FSoqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKuYx%2B%2BAtHCiMfULNircA5BMC7UJ7exR9J0Wu%2FJKuI7lPdloymYFFpq5MlrJ1nlbOwe59nTaaL1jJbsksWmF7qYmnnW4Ph9GgdgWcI8WqVWOyBJZSlXtKowrDjiU%2F3045pPx8s2eboTSxTEXDDz3aEjAlyfIsb9x%2FnAH03Nj4ugZNIapVvaNhJWDPDTyqowbitlARXAC1lBGbakSet31%2FAwpPHsMc7RhyaymnRBsc%2Fx7x5iaHEcVY7EB542CO8vOv4OThOUBXJxqy6v0D4%2FCbHyaFraY9K5idOilPPlrkJ7vLq6ry6pBXSz26KDbXht1EPDUkCyBrk45drD0a%2FZTEWXwANAYByLd2ZsgGpeM3fl6loyEfxs3dzFJrNoxyGbaSk%2FyQd6PmqF%2BWwHpQzJmirdIbJKaF%2FQTbDMySHO7AHV986U2lygPZxOORb8uLjL4gvsUtUg64gsx8TLKV6K6yOKi8QgZ1G92Nw3YLY1SO%2Frx2BJZB0zKkpuYFdeDfSVKjgpvds3ogtKRqKv67Do4G2CtOTdmfDLOyLnO9%2F4cwn2HB%2FL9z60O6zWju6zyUAGTBdtWtGEiRpzepSQWlruVCmoDh%2BU2t0TKf4by22Wl63%2FWYRV%2FzL8TdVvGw5CxX%2FLgMgcyF7xOb3l2I8BqMOOx67wGOqUBpdyZrHMfq8gQfcA3TDAPZa%2B8wjPJ5VqN4536siODamT1NAt5rWXB68exe1f9xlfNFL1S7J5BXRMvCUaUUd2pAHMSdG45x7EGX%2BnveuI6QH2SxCU27e6HPoXfAi4a%2FoV3lAPjk6mQTH48c890wMUZPtKn%2Ff2W2hRKd9C2AvWCb2fsEDGIYeG%2B6XURSY3XyIGf3lY2dnu8QRk30zO2%2BXevo%2FZA96w2&X-Amz-Signature=af640c4118e28ce3140a8e0a94983d217529a8dfb73050b4fb1f69f2034db033&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YL34TQ6T%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG370%2BJuXqKd6N7CZln6nzZO%2B4Yj0yjY%2B0r3FRGSbkh1AiEA3zIlqJoubFtQduPXsxKpfX5j4AeiKYx4tBg1iS%2BbL90qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPdEMFhrS9E9%2FIIvRyrcA1JSfXwSsDwKXP%2FcbtItOl5UWAlkIM4a6Ic18rpaEi96YOSfelo5Z6mqRJLj7Iflo35c7wBb7%2F%2BYNyPn7rZDByEKYJ7v5E9YmUXZsnyUzLLC7wIkhIT01GNm%2BM2VSwT2YvEPgq5YxBNwQ39o8gSTgUlH8BEe9PpKEQlKhDUvg%2BCQkwCRfav0uoIookX8C1fHkHDJlKu9Y13h3h7uUKXpPDmowVUVx9DRlEC8ek%2Bc9dcwiVUG0TDwOkYxAyj9YJ%2FKFKLEQRoLxixbO6frft915BaOKgRk1sjOjM2sVs5zerhcxXjdFjRsFaKnZpLEwP0MdHDeBziUtBXPBwuM5mfujYQh9Vjx0v8qdS%2BF%2B8qJCogq7yhO4STNMwxghPmpyNhOyK%2Bqog%2FoWghwbQIY4d7f1OcqdZVvpdfftJGrpyBu7FB4TvanWX5pq5VbFDdqGZQo6DfRxcHT7ITVXUJ6ERD79kxWtOmrvtPikVcwgIpGOiKxFO%2B8ea%2BwXLNTmDeYAK%2BRSzdUHiw3hVm7UbgmsWrqmGBhGtLvi1jk3vnrfc4GDXoxSfwHzu%2Bu1MqEjXsU7t0G6qBqXWtC9xsrViI7FW8p8CXc2GBGxrdxjBoZ%2FxZdfaR07PovCdW%2Fo2XG3JZyMOWx67wGOqUBABgSiXk6FAABSyHAPqv5ZA03EVjch6HVza79UXdrNULBG5rbI%2Bk3e1uxzE%2FpCVtZczy7FGtEK%2B%2BUpOi7rnKwo5dUuLKLONohAgykkFjHnGqfSWsto%2Bm6%2FBpJZEfTbMstHQD0i5frnahFfVefu4uPe2Wu78EbrMHwyNrBCraKGkixIer8iecQGyl6RMnmyMhjWgfoDH3RWBh4jgrqT6R91hSNijPV&X-Amz-Signature=4373d808fb47349bea76526e7e13eca473d95b86c868afbfd6b38e989cc82f09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFT5HJZI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG9pmAO0K5dcCRK4vxEfxuAH0NXsuGlv26sS76DpG4wSAiEAwX6IQMfexMhsWVsNrx0ZFYYf2EMDyyC8cI8N8pd66iEqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNOWlhbcCXnYIOxEESrcA39chdJLH24MHeB9KRkvz9%2BQs0tOGtmJG6RQS7ggjsggAYNHWyXXOzrNWCVRW2820Z5CyPLC37nF%2B5ePdZM8%2BS9ojuNmm8ZkuYlmsWLMyYTLI9Hgnq6n2HNUuJeBG1mEFtK3CQYeywn923lHC8A7ozXz2cdZn0eaQ5XcwIiUVNE6u7ptIYqhgpTO5f0NLaLCG1zEARtHYzHjZjDGN%2Boi6smBaYkOEeX6PXzoOoWS3lbnSlQfywx2wQrRMZ2q9QprgnOlpCydCEpZnzvS5wQI5jKdd6MFj42neem7JSpTGNOzBnjPYi89GzJVo89Ar%2F3hYSSnslWz20nZEakJHZziWSGoyTwOcsa6Kj%2BUwIlC7I9qDu2qYrIQPdT2Ma7IAr47YDVyOpuFj1Q16M9xnfmiAoFmGXaGTcHacT%2BG8ohAt7p7Rcqct%2Fut8dnW4AB7ifwX7%2FRHPt1Ym%2FcO4GoF75ruLMoc0pHZb3%2BSqvJsRH9hKJ2LF7MoMdwA%2Fsm%2FBwe0LTDKCrYc3%2FGwsKVXUY4TyWOt1wFViIkrjaEjg8mfKEMVl6tkWQZPi936PFd3w3SvPMpJZQZ%2FtCT1X318vUQxEe2UoDzoUQDtkZ%2BrSarUcGb0tpdHpG8WBt6ZwAAh8GrXMIGy67wGOqUBN3WSzzb3kr2D8D2ajoVkhhjqDdvNaiv3nliIQ5rOp0YeyIwfvpUU3qmCfQbVMTligOL8w5s21JPMGnsDHQ6a9X8ZtAcDh8hrVzFM11chpKCbpP8csMdlNKBZtO4Wbu6RUAvFjjKGWT9e7OvrM2TGDrJJ8LpSS9iBD54Dm5I4HmTZUeDuiIz8aekbX2MVb5iqF%2F7%2B2wtjr%2BNKKiyew%2Bm%2BcMsLSfPv&X-Amz-Signature=5a86ae9c041814a41d1e8a767489857271a02e6f0fd2a10656aa77102a12ba2c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFT5HJZI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG9pmAO0K5dcCRK4vxEfxuAH0NXsuGlv26sS76DpG4wSAiEAwX6IQMfexMhsWVsNrx0ZFYYf2EMDyyC8cI8N8pd66iEqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNOWlhbcCXnYIOxEESrcA39chdJLH24MHeB9KRkvz9%2BQs0tOGtmJG6RQS7ggjsggAYNHWyXXOzrNWCVRW2820Z5CyPLC37nF%2B5ePdZM8%2BS9ojuNmm8ZkuYlmsWLMyYTLI9Hgnq6n2HNUuJeBG1mEFtK3CQYeywn923lHC8A7ozXz2cdZn0eaQ5XcwIiUVNE6u7ptIYqhgpTO5f0NLaLCG1zEARtHYzHjZjDGN%2Boi6smBaYkOEeX6PXzoOoWS3lbnSlQfywx2wQrRMZ2q9QprgnOlpCydCEpZnzvS5wQI5jKdd6MFj42neem7JSpTGNOzBnjPYi89GzJVo89Ar%2F3hYSSnslWz20nZEakJHZziWSGoyTwOcsa6Kj%2BUwIlC7I9qDu2qYrIQPdT2Ma7IAr47YDVyOpuFj1Q16M9xnfmiAoFmGXaGTcHacT%2BG8ohAt7p7Rcqct%2Fut8dnW4AB7ifwX7%2FRHPt1Ym%2FcO4GoF75ruLMoc0pHZb3%2BSqvJsRH9hKJ2LF7MoMdwA%2Fsm%2FBwe0LTDKCrYc3%2FGwsKVXUY4TyWOt1wFViIkrjaEjg8mfKEMVl6tkWQZPi936PFd3w3SvPMpJZQZ%2FtCT1X318vUQxEe2UoDzoUQDtkZ%2BrSarUcGb0tpdHpG8WBt6ZwAAh8GrXMIGy67wGOqUBN3WSzzb3kr2D8D2ajoVkhhjqDdvNaiv3nliIQ5rOp0YeyIwfvpUU3qmCfQbVMTligOL8w5s21JPMGnsDHQ6a9X8ZtAcDh8hrVzFM11chpKCbpP8csMdlNKBZtO4Wbu6RUAvFjjKGWT9e7OvrM2TGDrJJ8LpSS9iBD54Dm5I4HmTZUeDuiIz8aekbX2MVb5iqF%2F7%2B2wtjr%2BNKKiyew%2Bm%2BcMsLSfPv&X-Amz-Signature=7648e908fa291ab0653392e6a6dcad5b4a17ab7acc6360b417e6d9bc63bee73d&X-Amz-SignedHeaders=host&x-id=GetObject)
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