

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VTWFYX4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBjte9GgUxxVAhiZFSghJxKclYKZqekZmfViIW7a5zBhAiBiW7P%2FmqxcA2GINcNp8HdOzK5xvEBpSf%2FAZOEE7uH5TyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiSwJEZCX3cQJ2WiOKtwDTDeXpOl4kqMWssPEjGebx8uD9isGLQ%2F5rn56CLET7bQh6wkyMjbMTsoEZYCcIOfEc2h%2FsDDYcxIw6k%2BaUkp5%2BQAiBGG0JmZWvG8tryiZM4wwTM%2BFVzcgGLxiOULhGCGnTbPVXd6vS6znKyudOpCVb8eHlzlbBMkrFSgGHjKTg%2B3XxwXhC7mI0zXYTjyRRqOQJfUFJNqw4WcE2A8CXisEF4%2F4yXlGzi8O8nuMZVbCc9daFbeyRX2%2Fi9t9FKOG0uKE3caKBAUqwoUzgNAvDH3AY%2BZ1CA9pIR3X%2BrfAgTJAlUpVgNs208qWrMnleuvWpkFvfJHbvlONVQkB4PuZqItuZntBJDIaykJ9IYCA9n%2BnTI0vEGNQwKN4X1ecvsMb6j65y5nTWMQGo9MsNd0%2BSevGDTRD94h9AE6VSzDLnvmqOw58aoqqQt6SSdlR7qvqL7P1x9NYhdTKcXENwcNGtpJobthqtz%2B6H8uZiLR%2FKSNaVbALcmZEvIhub6KM6e7tuAPEQWHX3B3aw2nh3GVG2e8ArVNlnUiDI0%2F2dpK8gcNXy0adyPKlGPVCRArYSwho3R3tpjB%2F9SFzD0i0yIzCDv9MbUIO1VrKTBwkZ8COT1hQ2FzEMdUwZIeV2BGhuJUw0aX2vAY6pgEbwaHLNovBshPQfT2wt%2B6GEvZwrIFHNUTiACcCY%2BtFTQh3fhIIGmmy690pMbF3jsVVlm4yjtJIuypDEMmZxRvSOpdzyehCSh48ojovdaDeyMXNf4t06ZSOj2T2NG4QwzfIAXIxjjeHrUWbF%2F%2BScnKTbbIYfa3G59%2Fzpk0%2FPLgCn97omm13eWydZ5s%2FMbhKeZ2NlKjXHBzn7%2BVYSjvlRm1cqjxwhD%2FR&X-Amz-Signature=b0e9fd597c4c14cd9dbfb12c0b83baccec35a51889240e26631b97e7d70322c4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WFXZGRA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUJLrK9wY586DDGBhRup4s0iKcNhPiCHOADQkc%2BxYHfAIgJJM6rQ2VPSoEsut5kkjjTfGwgtKu9YMMBLMXIhNzCPcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFxP8ODssv9%2F8HejICrcA%2F%2BFT99JH59Qunpb02IrJIzsazMv1FhImHTUcoGY8rnbtEb8BdXD3P5qF3GAlYwJ%2BUWYI1UOEFojXVYVQDw0PFiBiNbU3x670mkXwAMkCwO5z7CQd1ZNgfJmLVWBaQqNBWaG%2B8rwXibGVO49HdBvZbBePMy9pA%2FPvlg4%2FLwFZgBPhITVRFDcxVW8RvWknuNvC1YesVvbQXHNzc4DdGXqlMlO1%2FirXehe%2BI%2Fa4MNYXGqBub2pLXr7fwPPj4FkYiiuP0lCisJsr4ttrCWvwc2qDy5gAs9AX7iIiFRl5B8%2F%2FVzGnkxoOfgl9R38zM8MLHBhyoKnXSMa7AchcKUl6vX2Vr0PLkvRbV7xCADyTo%2FGk0%2FL53VRgJH1KkmTr9qE%2BcmyTbQWAj1GFTFEAvaqe7AVMk7OtULjeTEGZm4RYrnx5PYcedpocWn6REcTUQV5ehq5jzscrYkZxftTuPPW2VCR0FqtqOL%2BUSgqKb%2FTjGX7kWIZD0JeYzjq9EdGgQZ9zy4Y%2F%2BKBOfbxmgmfeWs0il%2F0ZoriPRMQgDtdiC%2FcQZnGP9VWHH5obrWpdwUf2xH8KYszhdZVCgWd8FZqf5qmbsSg8tb5CRxOiHYnofBcDbfTsuiVLgSrETQSF%2FhN%2F7LqMIum9rwGOqUBDW6TISAALDEolQju6RdTvg%2FAvqO7PJ%2ByArQh2eOw64iBAJhqX6XtSzDzhJmbcQd%2BUN7i%2B9orJUIalCyCHPKwW2YZsgajwPc%2BkkfkkaJJngUs86pKOZbLE7SsLPKNqjB5qVYNfV8A0QVlcv%2BOeoBKP70x1Q6coTIsOwOC0EvdcgzKXhA6IzLvolE2HM2WK8qdiu9bySDyb21ubyTnf7Pe%2Frx7RgKC&X-Amz-Signature=f443fedbde20756843cd1e2a7024de9db46aca4c7170c611c70bdb1705f1ea78&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663J2YSMBV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB74nZdyOR9sssfj8KlKy690nFmsf3sJNFP1f2Ik5DfkAiEApQ04yphYcbnwxnLabdM0Px8OuX5z8NQUu0sVy4betZUqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGB%2FTmX57XPIsnKqByrcA086BxsHRw3U2Sd%2B21mVPHPFfhckztXZdUEGFYZ920lU2Ds8PtFQd3Qm613T2P7BAGcRl9sCyn2Pb9bY6NY5lKd93U5e4Pcwjo5RKsWIBvO4AuMXNwubOgpvcucBXu7COF9uvSZdhKsukYhTYZsbs%2F7Z1stHh8H9qA1oLnns%2FO%2FZfYTqqDvOpo49xxsbhfc4qV3GeRyhycC5fnBmcDVRPfgYOlqNzjvDyDZDn65yAkJfPUZ9X5KDrlP29nIKqsWv0icEsBxQBoIGFC7IMjK9aYEzevqmizvDISnB3yOCKYlRwStZZBeOheziRMVwsFtLlASCQi69ohgl8vHPKULf0HmylpQhJ89WDTRZ%2FZVyaQ2ju8xn1jb1z59sfAN8uCKgsgqKWgJr%2BumP9I%2Fpfy5KU2eZNYOqfhr0I8sDaxcCRp88N6Fg%2BrS5e6OF%2Fr37lx9cTYnsiCatMhF%2F7zUrmoR8Ns39eDfEkPnXZ5tLXbiXif5SDAQHCTz2C4Vq8WQgbhoUXpgkmFGAWb5r0BGL00PWChJhXHuxYZ6iuK8sjsDsJFUjmonDDfBcCXA7y%2FGFCjkJp2UTJ%2FRk3VkqbRVdc4wEu5cT4aN54JpTrXHuSA751DOrSRC4liSpMIgtvafxMNOl9rwGOqUBZY4q3VNmGPmia7SqAu5kmEKSXWk7cTzRfjewIA25wZ7gsC1xwvZqRsBiK4PVuVX1EYyXf6eZ8%2BNEG6lowD2%2FnBj0MgwjT7oK5wbnsIy6qscUzJ6JnNTvzusDJUXD8aE34VZPzyEKluNpIqB4p94shS%2Fn5fEmz8yGDNE2dewQMZP1MwFq8SHk%2B%2B2hg2yqU7lII12vPf1d%2BrR52KvVbKmD0fXztnXA&X-Amz-Signature=4c65a9f3f7a5e6fb1a2480b76c10fbb8a53880557bd419b308fdfd418ae768b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7AFCQDP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICBL7S3xyyWg%2BEXpvgVWIpVHeF3EMNh%2B70jHuEK5Vm%2BkAiBvHCuJLvzBQA2lvrLiiGAieTBcEdA%2FTD2wjB7sHNgtLiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMezv1AEAr5et8XxjyKtwDiazyHrEWBNhHZcuainw9tJMXWWxEm%2BytJrrPyLEYL7uTYkUQgoufiMuFD%2FZ2byDs%2BMChb%2BBHFY5mcSTRF4xZJWbdn%2B6bAYdi5o2rtrpahniR7MP5t%2FaKPynEVvfXHAmZ%2F3Mg%2BYS%2BZEhFbR5olhWFNAsaVfRQTquuxAU%2FBHS0a6GmckytK8DgpLkA1cJ189YMZHLC39Qnx87d2b%2BPfhrCye8kC8LEaLIKPOr1ObqZPLZ8Al%2BwaUEMroEFfh8M0Wo8%2FW5moSf9N83rG3LT7pAFTyrFHhiuRASl7sc8oQ%2FvcKv3HHYc1Apw3LeUYooQRQXJeOJ6JqoRIAg%2F1SyIhcpbGq5sGfmOzwrijrfcVK7eYsXh%2B1Z7lbsxGubP6%2B9j%2BK7Ab1ZrKwkhRvWjwY1xvlgEEDz7RW8hbPPYDgCh4j6vJ70t0Lk%2BsTUuULkIFgyemb58B9UtvBnhm7SyDVm19bDM7kyPdyJEXzniX0gopVjdpxmi5wOhdlmSKJTYxamDf%2F1%2B4NYKrnVknk7ylZAlvMXVMiy3JsvvFTONZI18mkbKO464Ufu4bmoq8Hf46lQCFb9vZwcFaWkivQJBUNy1mGd5HExkwdqOg5OzBTIILJxzWAWdZDGiDkY2Yu641hUwyqX2vAY6pgHTOBy7w5O1K0wPY4SiEBvVgWKqX6UecpUeTwN1C5SZi6ZMHj%2FPkAur9%2BTaUTWuzmT%2Bh3cR4d6M5Sh2tqzwLSywbGzp4vvc4X0A0FN91SkPtIPPe%2BgXdjIE7siFR3RHUoNNybSkxz11oJHIhA6HU1lJCFxzB7auDvPLDA2g5SkjoPaP%2FKon2QITqj8DQwJdgogDiOD2p47XoHHq864VGAYG3SWwk0jP&X-Amz-Signature=cead109fe3e8e4740f81fcba62c1b27d6fada0d2372df96f3b2f6fe8e18ae1e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL7UBOWB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIx7qKzbszgbr2nKrfnQxTmltmZDgJEP5r9ASCzOH0tQIhAJKNYoS5SK5FHRkCiLECUhWuX%2FWfBVK7U5oWpAfK9ACuKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyiPbPQOMDOi%2F%2F3TdEq3AMxd%2FXfOdy%2FAaPUEqwzYoFsKxLf1d2Mvytk0Fw%2FwKJXlOJck45OLy5lbXDXYs560BdDB8fAmdOnRWoVwWlxF%2Fo34qOYKBh6cQMt%2BY6D8kYpALbBOB8tx9asHChUpROLJr1PKgSaWI78WN%2BLWWzaQwyBxLo8jUy6m63Rf%2BbAZarAGa8Q5fK1BlmIPYZogEs83BrrjnNe4HFFL4r%2F1Rys00glAI7YJ7A7KqT%2FN%2FEOH2JgMDna6p7eEzIPiikErqhlqAV%2BVAyUzHb1Ab%2B58%2Fzq1o9GkYL%2BW4oey50qMNlA5iT%2Bg7sCeQQP5g1CdKOGDRAePN3EvZu9EXWBHvVPVwuBoy6ghwjoWfyR4jvthvJksOJKJocu7tnsP0a3GUA3Z3z0d1%2BkTRKq29vPmFHwqNESe8FRHW0mj%2F7Sw85bxf4MFqmWs6voQCpekYR%2FWK6dGXPyG2trqxTyZEWP51okZvk88JriSDYiF7g4%2Fdl%2BrBHPammQ4VSm2jy65Zg%2FeaW%2BGpi04l%2BCh8EWkhCW18KQTxKW3sAGh8hAv74Kj3BcvZ0T65I%2Fmx0h6p03pDJNk0OSZW1bYxRgpzuqX11jnO%2B8Q9t%2BM6uaj8HU1xFWt1nqEdtYwSxyiQ330W5%2F3HLgO6dyeTCKpva8BjqkAQ7wSa%2FneYvk9lsaYMdGAJ%2BmvNxw9%2FhEyJ%2FE4LO0vwzAq6G3DzoSsVPVJV9SRqKyp8iKH4uyXrsIqtn5mAJPXnzgHo%2F1Beia%2BXQEEEtos4pIYhaE2LysrtxQMM72WmR2NSFyFT%2BxhYOE31E6EqJR9%2BE0G4PG4DufkW24bXsCxWDKXBG6QHtMdCGFpZBIvg6VmoL8IyqN5PYDwsmkmfqlXWlINENj&X-Amz-Signature=b4f81baf0e810e78ed8724502a4a922bed3b11bc85dd83823b5071f12e3ebac2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662B5EGKCZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdT302H9N02T3kF0Y5etkInX633SrX99P5Vf5KMtA1OgIhAIx49NK2Cdv27XhP834DiThGwHWCByIynIJfyIMApWfsKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPs0BUEYe2gOYPCmQq3APvQ1Ib5Ljxn7vRi0i%2BBorFlPHG22IdinW3SJxTUKmhTuiiTnCHveKjs%2B7t6IwnTC5ju7RKYpjb0xdUhcNh0V8RTvaBiJzg67AVT8FOGm9DoZl%2Bkm62yNL1nemaa%2F%2FCFKrh18FyEnhy9%2FLIrI%2FCW2EOYmy19%2FZVxMmLsc1TrRT55OPPlXLxDsl4Skk%2F59yhrWxX%2BdFy44BpVxDABR6D%2FtzxPhzbkTU%2B6YR%2F1iuW8SPi3X32BbVXAoN9xuq8q4jQq6%2BFPFNs4bJVOl8QOWFjgUJLFuV4oCD9oiAMD0gdbi%2FsZyIGiTfeQ4lEVk3FbNCFTlaymMR0xx%2Fc3nyrgGKBNcXScWWfNNU%2B0feKrNIhLJg%2F1oJqQGaKlNm9OIIcX9wHsHZUINmoOtUweCdqvzZwJMvqJTEXgvHN1kZQisI3QdoJ3nzTyK49F2OX2l6wKGDIuJE9xjCdHX2dJdBIxatSHrR6tjZBTg4RAWu0HsArPtB%2FlLfr%2BzWXGSzQkDjnBd5D4KTxIopCT%2Ba7MtPtQpQLe18dY64TvsrgUhG09DBJ7GpQgDZ1Hjjn%2Fl%2B%2FhmJqPFxrMnCiryuMUbtX3SEbpjugxrPFMnrYNKMbvqRCUMK17CBjlkPJYCNmLkENE%2B74xTCApva8BjqkAYBWpqny79r7DARU5z9o406c7gsHFLhZW73m%2BhuVqneIvBLrXF1BTtOz70%2FTiuXC%2F9Q4MaVZExKOp%2BanMsCPY%2BSdUaf8y7qegyWzlqeKFGCl%2BXSyudwPORqkccDY0jwNiAUsafK8XX7N0ufzoLKN0YscveVyyMcnC9jTDS%2FsZ8ESN4sVdruo02yFBi1C09chGub5DbxFL0jgL9RTUqkx%2Bvt5PJ3E&X-Amz-Signature=2406826d8b5088f097e7302b692c7b48f718046d1dc0960cc264c5bb2276bf1e&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZD23L%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3CBvdOtzM0QklTnNWyOEHxx2UlURJfRLb8QusfNHeVQIgFxHS4u7gL6cGMJJa2GqzzSWtSBvNHLS4yDZ%2BWh2wvu0qiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvMkL219qiKyYGpLyrcA20yUzOKjJcVjjbFwC%2BvlBWBy9%2FNyCS4mPt8mOURLrRcsZKP3dwPb7JvkBNHbUZD1hhOyIa6KzRc16FRq7T4P1v3%2Box33lEpE4CTED435gF%2FtccDrcR2%2BFY%2B7PVlHiPHswgcgXOEyqIVCCYVBJVyCRkkMWzwUJLJZMNp9ixP71G0XQNpuMkTehZ6aKGP7kv%2Bf%2FNqUujjEJ%2Br3160HZH6DXGI0Eh%2BptWyx3jTpMSgDXBdJJhF9eM0Y5zp9d2E7lXx6soN64uJ2AXbRHPldh5w%2FdAbCnEN7h6Ylqe592q3oYOyU8ikswkTrVtSFUA2THsq4wtk0VYnGTKOuPNpiY6cVbpRBeVnvFIsp96nVKxOGYj8LybJV3%2FfaOYb%2FKFhJHhx%2FPj8DEvLy1ox2ldigT8hhp3A%2FPFg%2F7hGMHqkwgitq9bLflSx6%2BgD0CI0au%2BWmkuiXCp5IJt60moGPNgr3f91iTvarmmisxEqKlF2p75LySrfd6GMVd3RG6MUayUB1BfYqxHQuXRsArdrDBGoWnScxIZxymrI6J8aZ%2BiUJkbOHf6bwXGL%2BqTdr6LYKRh74iUnPZgoCFBP4mU3OGd2NErbEpjhy%2FxjRlULXISf0p4zjUErA2zUklyXKpehSHRwMNul9rwGOqUBCEhfDmlgYDyqYUaa9tDKBkHSRy06sikpCZ8VgHrzA95XUKKzc7%2BfYKqJVwLHIGKLV7pU%2Bk%2Fj%2F0Wn3J4OL%2BVm0xR%2FAGeGVw7eb%2F6oS1ck11yetpBlKlRlXpkn75XvOwWgOZxUPdJpn%2B3PwgPn1yztJs4TcYBjlytUbgHo7yLgEmWt2mnVxmmNtH6MKx0N8Q9AMoNdzAtfJMJBkPVdVNGh9uQ4oGxy&X-Amz-Signature=8fad1213cdff50981bd4318f95a07dc0b81c368b4ca9c04f0edfca77c78aee7f&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SFJCTFZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1yJOBbpETd7c8rnNAd4WYzh%2F%2B%2FwZG9IGOCaHcbyUzeQIhAJ64iOw1DoGKRWfMyo31Uau5hiaAZowp4x17MyIZle2zKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXo0oymd07L%2BCU900q3AN0WniSBs%2BoRd%2BPTjLGh2huo28mutmrI0G4leRxbozn2nOpl%2BgkXZNxHId6VstJky4h3PyS9v%2FEDPEOR08OoOTlxtgTsWXFr4DpSoytw2jaX6wRSzhWArmjroT5QvExQtzji%2BILKaHhNpOKNlKMcF46TnbGR%2BX0LA5%2F6o8QD5MYzfPWivfWjxyyln1Q9X9QcOo1HDiV3rzJPyFd6MrYvK6nfnGhxRdZueUhTcm4WPX4lMBFjBqoYusSEOhiCncnJkxlxVYIZhw2ZNGhrN5aIpTaPqJsss0HSv0dpmSzoz6tfghTKHvG3WxSxDP5KgDlL3vL9DGaIS3h5rmK71xYfcYOxKCQbhTeCCG%2FXQLz3qhfmZfjbyoRK3tikTcVCtW%2FuSjn%2BQY85j5GArQscXaINm%2Bi3OVEiBfReIMmnc69VSdejImeI1Ne3bO5GMFmrhnFgn6HGPGNCi6qIIhUhuCyElj%2BvgNiL%2BH2DJu10M8ZKHQ0brxV7g5yjXrk4kTYpR3152nk7%2FlhZJmde5PvSA8RiMcEKRlkDHhlsBZAg2yZhdO%2BzGCDzr9kqV8z82toD4qGoBooJPzqhlKQfMu3wH0GH5qF4at53HmAaimpk7aWxuHHe%2Bq5yapZud9L1Rp4VjC5pva8BjqkARz%2BKFi6yXziJxRtDvBr2UpuzEAn69m2qIcjsDyT0T7cMhV5aRNzkOGLhPvcnbq7Z3UPPANA588D14KMXj9jjvQsnSmM0vrXce12dbu%2FUaeVSm0l4nfjPReNiDwJQST5K8Nzv%2FsOHtQjyMBH9%2FFDEzqb7Lf%2FJFVP8xscKuFuyjorqp0h7KmX9IKISJWCaN3WoE2n4gKNyS4QGSRotiLOBHTh1cHq&X-Amz-Signature=bd4273fec0666868cbfac022dbd9b3b01830190d7a026477eb713867f0b17359&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL7UBOWB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIx7qKzbszgbr2nKrfnQxTmltmZDgJEP5r9ASCzOH0tQIhAJKNYoS5SK5FHRkCiLECUhWuX%2FWfBVK7U5oWpAfK9ACuKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyiPbPQOMDOi%2F%2F3TdEq3AMxd%2FXfOdy%2FAaPUEqwzYoFsKxLf1d2Mvytk0Fw%2FwKJXlOJck45OLy5lbXDXYs560BdDB8fAmdOnRWoVwWlxF%2Fo34qOYKBh6cQMt%2BY6D8kYpALbBOB8tx9asHChUpROLJr1PKgSaWI78WN%2BLWWzaQwyBxLo8jUy6m63Rf%2BbAZarAGa8Q5fK1BlmIPYZogEs83BrrjnNe4HFFL4r%2F1Rys00glAI7YJ7A7KqT%2FN%2FEOH2JgMDna6p7eEzIPiikErqhlqAV%2BVAyUzHb1Ab%2B58%2Fzq1o9GkYL%2BW4oey50qMNlA5iT%2Bg7sCeQQP5g1CdKOGDRAePN3EvZu9EXWBHvVPVwuBoy6ghwjoWfyR4jvthvJksOJKJocu7tnsP0a3GUA3Z3z0d1%2BkTRKq29vPmFHwqNESe8FRHW0mj%2F7Sw85bxf4MFqmWs6voQCpekYR%2FWK6dGXPyG2trqxTyZEWP51okZvk88JriSDYiF7g4%2Fdl%2BrBHPammQ4VSm2jy65Zg%2FeaW%2BGpi04l%2BCh8EWkhCW18KQTxKW3sAGh8hAv74Kj3BcvZ0T65I%2Fmx0h6p03pDJNk0OSZW1bYxRgpzuqX11jnO%2B8Q9t%2BM6uaj8HU1xFWt1nqEdtYwSxyiQ330W5%2F3HLgO6dyeTCKpva8BjqkAQ7wSa%2FneYvk9lsaYMdGAJ%2BmvNxw9%2FhEyJ%2FE4LO0vwzAq6G3DzoSsVPVJV9SRqKyp8iKH4uyXrsIqtn5mAJPXnzgHo%2F1Beia%2BXQEEEtos4pIYhaE2LysrtxQMM72WmR2NSFyFT%2BxhYOE31E6EqJR9%2BE0G4PG4DufkW24bXsCxWDKXBG6QHtMdCGFpZBIvg6VmoL8IyqN5PYDwsmkmfqlXWlINENj&X-Amz-Signature=c8c2efc776b9075416e111f8da21bf75f85c6739e2b4f082de5c30ae4cdd6841&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUFLHDM2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCCkJUZOE%2BYgdf3GMaqdlHVcVmI2rxlo5%2Fd4f2%2BmCAGtAIgMnQocYYKQAr8VnEvce7tpr5Mnmx1YXW6Izrs%2FL%2F%2FxWQqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA7H1%2FMOb8JaGDbUWyrcA53k7CStNwUXoeQBrzKVQXDCtqweEdk7SeMYf0P9bBFYu%2BP7zDUum6aTbWXESfWhOv5bobf8NNY4dOq1uiOYypQw7yR2%2F%2BMbKnRDxGACq7bIqqPNAMaPwWaw0RUV96zxrCn1dIjFvlVrZdPYwD%2FhyLmN5X%2BcQTiQDPBtnVsRX1DhAhXBeI%2F4levshC%2BviR5BAiXiSNn9BMCxj46DRQ%2FXaKQuPh9dhYA8%2F2aVrGhbLK6235UihRvZJ4ekceyLyxB6lRdvcXBjXOwvuuQBLfsCL4RW0HZTN3S0WJO717cptP6cCph1IdhHQ51%2FYDT8SkmlXmU3GQQlFOkV9XRfqx3tZwWK8taNtUTzSuYD8dydBIi3853crF1K4u3AIOC5pKd5f9xhXSlkctqIZf68kbSShuBZP%2BcJ0YJZbXXjYifST1qcujM8hrVe0DFsmOc6tNFJSBdKxyILpmt4f7ym%2FW%2BbrRyRIziqzbGLnRHifmZH7XWmZtHOOz2TWyPigCSTEToJML0dDivaMlF5nxRU019PR3mFXBGLgqzqCyT%2B2ca7FkLwje4Yr5Fg101Vwya%2FRwjTnTXQ05bINkWHF1tbG3Uu7sOlVQJ%2FygB%2BFfpHaeLnqi8M%2FluDNTtS1gL2pZeeMMum9rwGOqUB0b83JRhGzQ7E2Bh%2FmPFdG%2BOBG9WEF1No21vWER0TgxfER0a1iddmgZz67Cbe6Zlnm48G1o3uEZARItvT7ojCIjMPKaAslIbNfYu5QaUJ2qVOSxo7GR7roaKzGQ6869Uck5iB1l9Tjqfr8fNZcpkl9theyp5DYEgtVQufncuzEL8AcMerYTai3Fe0trK%2BbT3Z30vB0A0OsDDImQE613koVgFnOwoC&X-Amz-Signature=39e53d39910aa88ff2ef460b77b1155609037d5e24bba82135bbd49cf3d26fc6&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUFLHDM2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCCkJUZOE%2BYgdf3GMaqdlHVcVmI2rxlo5%2Fd4f2%2BmCAGtAIgMnQocYYKQAr8VnEvce7tpr5Mnmx1YXW6Izrs%2FL%2F%2FxWQqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA7H1%2FMOb8JaGDbUWyrcA53k7CStNwUXoeQBrzKVQXDCtqweEdk7SeMYf0P9bBFYu%2BP7zDUum6aTbWXESfWhOv5bobf8NNY4dOq1uiOYypQw7yR2%2F%2BMbKnRDxGACq7bIqqPNAMaPwWaw0RUV96zxrCn1dIjFvlVrZdPYwD%2FhyLmN5X%2BcQTiQDPBtnVsRX1DhAhXBeI%2F4levshC%2BviR5BAiXiSNn9BMCxj46DRQ%2FXaKQuPh9dhYA8%2F2aVrGhbLK6235UihRvZJ4ekceyLyxB6lRdvcXBjXOwvuuQBLfsCL4RW0HZTN3S0WJO717cptP6cCph1IdhHQ51%2FYDT8SkmlXmU3GQQlFOkV9XRfqx3tZwWK8taNtUTzSuYD8dydBIi3853crF1K4u3AIOC5pKd5f9xhXSlkctqIZf68kbSShuBZP%2BcJ0YJZbXXjYifST1qcujM8hrVe0DFsmOc6tNFJSBdKxyILpmt4f7ym%2FW%2BbrRyRIziqzbGLnRHifmZH7XWmZtHOOz2TWyPigCSTEToJML0dDivaMlF5nxRU019PR3mFXBGLgqzqCyT%2B2ca7FkLwje4Yr5Fg101Vwya%2FRwjTnTXQ05bINkWHF1tbG3Uu7sOlVQJ%2FygB%2BFfpHaeLnqi8M%2FluDNTtS1gL2pZeeMMum9rwGOqUB0b83JRhGzQ7E2Bh%2FmPFdG%2BOBG9WEF1No21vWER0TgxfER0a1iddmgZz67Cbe6Zlnm48G1o3uEZARItvT7ojCIjMPKaAslIbNfYu5QaUJ2qVOSxo7GR7roaKzGQ6869Uck5iB1l9Tjqfr8fNZcpkl9theyp5DYEgtVQufncuzEL8AcMerYTai3Fe0trK%2BbT3Z30vB0A0OsDDImQE613koVgFnOwoC&X-Amz-Signature=31ac984589f7748f21ff62c6c7ea2e6a32fc7488ba819d796c552d7c504913fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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