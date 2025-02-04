

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDCGJJOC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCmaTrq6vSRCi7qumsGop4PnNuYW6vLV6n%2FQFPmIWh5LQIhAPfJZMLPpo2zgzWvTU2l935y7%2Bj5ppx1l2%2BpaehmvoJ7Kv8DCDIQABoMNjM3NDIzMTgzODA1IgyGDw8m6cWDN3dbaFIq3AOEVTdmbLZcbo4yWaS6diAw1iEu%2Boahae5durCtx%2BQZBzS%2BTJEzZlqXTkK%2Bcfam1qI6syZ0SuoJdtkLkqw0fbQz6OGBpFyERVsFxBZojy2%2BEI7otca0zBj6XzuY6QWzZMMPIdzGQR1w7czJ9NVI9C8q7KzmiAddPE9bupH5Y2M72dGfBKhGbhSor5WMqheT65LxiDyWWJbzBd9v8FuzUHLqcsnwaKBAQo4g7F2RCJCTZIU%2BeEuMzrtpg%2FRvTpZmmciKWf%2FRwseHkIOH3dyN5yuTu%2FF0H11oPZBd4Uywe8Pfas0O%2FTzlRoPWftJu1H3fBM2BXhabjAvXEerQ6gdI3CJyK2oPfLWan03liQpPcWQ7EgcZT2WZ%2Fn7HGzrTjQqWrucZ54VyZ8d0ueLEJV5VTVActstkTdJNX5v9PjIUFaQJXurt5xGB35hhccQ9aqadcIcZb1bmsJAqlygGTYErLAJSNHzMEsaWIeSvpWIhRlily2833GHsJU3SIYXnvZHRQesizwLERhRJEBxDqAOJDsfTr2Dsvqvru%2FHjJbJVDH7CLlBjZtaZCwUb66P7QPyzGiVRoDJ5lfOCqzYA%2BrM5Mm5Di0wJqRx%2BhONSbKurbB9NuJZAlpCJmROUGC1R3TCzhYm9BjqkAZGjupqO1XBKxfRRCXyz3YwrKOZIT5%2FmzqBrkW3pRtBXWhymZxrVJD%2F9BtZGiNNTGNRAgoTQVovI2OmpxTsTnaKkapEf600yvvLaH5%2FfFm0YVV8vkSJR%2Bza70xjMrq09YF1hT3JIhmkGGpJ7EOO0BCPHGrtUTOrRHOTX%2FBZ6aQyoJYUApQiuCLJ8icDLAJ42IAUP3o6aKK0oXHgHro6GdQRx1yIV&X-Amz-Signature=f9fee6eedb7d6af6789fec4f497a2cafb496005e82429fab50578c230e24f44c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMYAYMON%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQD1GHcC%2FRdOsffXrEbwvom3fNwhf1rt7rv%2BIYNkJjRT1AIhALDy95zhHQQVEG1RMU4YME1PFjq7EYR%2FCwnffIkYqI4UKv8DCDIQABoMNjM3NDIzMTgzODA1Igxo%2BlTiC7vWbwPGc2Eq3AM%2FlZ31ji6dCI6%2BfTGYXytiSVBde6jD6cDgwHo9yjEFRdQJ7Jtqygf0zHescaieNNVf7jNQzYzAlr%2F%2BUWJ4mxX%2FpncqbaxJtLpWCBVJ%2F9fOMxZ9jvFwjU5t22YEMV7kEbpk4bh6n16a9N2x0cNyg5LydbOWv4IiC8YK9zd9YXWm4AghfOZMyvou1nWIeeK%2FVw7D6kCIuk1WVAX8SE4sv7oJGXH28yUr%2BnJgVekOJfhYFjR5uhY9whVxw54GPRrgGc43QRHzXI5%2FaDP0o0rMp95xoIKuyupSq3AHQxBEMYS7QZTg%2FEs%2BHkp8k670IZcH2siy46UaoBeOM6QvlvJZH%2Bpx46fCNKr4dxa6k0yRoIrnO42qkk7B32Gay3JaNbHnwp%2FKeAsH7i%2Fzirfh%2BtXobhcHmEZyvVZ2VTZ1QRc%2Fq78oVhHLC7oTsCSZnenvkh8OiIIaBzKztdzCTeFmL51SXMhOShtm4Kf5080oQ8N8YYyofkHJ2UzrO5cf6eMBLrfhYBs0W9X5JP%2BqY8%2BBKzAZZ0oIhoL1FXJ9KFITVJJBva%2B8t0YWVBTKuZUceq9AlYgvxa0Otysd6%2B3XJAn9T90UqaHyUo3fmdeME8ycpnWwDKxuekQpZ0%2BiDGn1o%2FquqzCQhYm9BjqkAZo2ty%2BtCRqeTgV4usvdSawrq8jmSufwIfn%2BIspyJBNKnDX6%2Bqg3VEnJxGbNv3OfM1dH%2Ba58A%2FIl%2BGPCg04J81HSKPSrOi%2FjelsonEeDF%2BZE4IMygzW6Mi%2BB2ahd7AlxlzEfowK33g7MAJmkHCAm4rx3iImu2o8m36fpKwnGdEBxjST6iz73QIc9NjXUfcpKDsRF2XoelL4EHFlw4G8p5i1B4%2FtX&X-Amz-Signature=585a9b497f4acb3fc92e86f2cb1f0b0c7ae9e47d0d46643b70b2583122528317&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPMWKHRP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDOvse4QWeZTp0kPPkWFNLg0v8uvr6a8phxYabsStRaAAIhAMJNgfFerlOCAbm7cO1sBIYlli9jTEU5Qhe9mrR3QjgcKv8DCDIQABoMNjM3NDIzMTgzODA1Igwx4KSbTdPFtHEoV6Aq3APe7OZzhN1UEJ4RJiuUoW12Q%2BJMxlCIgXRAKb1Zq%2BmYmu2cgCZONSM313s9gkawHglLFoc6xoNKrX%2Fvz3PV8DhR5vnT6I19nT7%2BU%2BH63KetySQKGgdE%2BxCfR1K0FuwMgYKl3NDBAun9XBOrfbm7Kvkr8S2fk1kBcYKNSi%2BB0pLjprOy2wJZX3Acqtd8PQZ42%2FeQhVgDghvZhaHpMxmT5FC2Lo%2Bq6XucGicM0nFPr5SyK%2FnwWFmliZOdptyCbN1H4GIaqHwwxz1zKMtbFH6ZEJMTQgVGzNKdPwTDOU88vO0U3I4XV5cpAXJ%2Fn3pc6%2BegKAjixxzYrXhaEZVeNAFVODZFaeXRyYXx%2FqiVyiY6vuAu3NkfuW8WBZh6BMwg6mcSH8R6wop7Up3iH8%2FHK1p8KLf7MbWLTPgdzaksOEaiIfXrBEyrOQ%2BHt89Pw0nnp%2F1JBbtj%2BuZ%2B4nXlvfYknucnmsQHQeyai5okyXdpxjtQgew%2BbHiDv%2FW2TdIjPyKCoHrXPeSNE1Wx1THt91E0UxlpIXblChtyxgYLdAt57Dmip3cp7E2fUNQiePWss3vJJBxbeyAVz0jOXW01NjjSOcJYsTfgdTqkJUlkN0hz34Arop6Dt6I5dHWSnqIscPbkdjDWg4m9BjqkAd7P43aJS6nMMnJLG6cVCyrXrWH1wlGwR2lPMZz8t9dpwO0KZAuNuEvarWbEy4Od04xHZ%2FRLpele8QvTs%2F2LV%2F1QI8BoFw3g8c0R1CSGWYqowF2s2073BtSSqyEuce7b7N1ED%2F1gHj02J2xB5c%2Bw7nfsaq8R39c6y35tJSMErrVZwB3VhrORQx8ZBCCokDJI%2FJDEmyIcZ29biolEtlXS%2F9pIQ5OR&X-Amz-Signature=82042dc2e5ebd397ba2caf200384131d12765bee1b398b0c8df8473bc4b28720&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657PM2IZR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCICuJfwuVUHjbRSvCM0LWbupv93O%2B0HK1jdRRMPWKmcVJAiBlzoGQBog8vbeuJdu0GrbFkLbv3d6TyXY%2BnrYrX3zuyir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMhAUpAg4GELmPM%2B5pKtwDBUETxjaottdYfK%2FRXONbGVoSfkf3y5YbMXg5qkGFw8xb7x2i2NbC7hRdNS7hX5L2gv7JgzV%2FWjLh%2FMALvh478xvAj3t0ceEOQntMnq6nuz%2BK7ZYBCpcCYxOn2C2cRY4RLHbqNewT7vR5TJZMTFnbGssRmdg%2FgHV0Wu43jHt11N%2FR1qSpz7iKM%2FB1odJW0n1A%2BErECzgx4OihJDs7V1dQYoAspkjHsOAYhy2HTKYImcPmFUyl6eJNQlY1QPCo6A1U59jcrums%2FkLDIfmI7pHt6Q8QUvP30psisE%2FWW33AZbq8Dt1u6FqfgzjO4tjlDPiMRlK6ItQkUzCPvzjot4vHm%2B%2BbpkuV7b1x10jH1QmJ4%2FMgLeIRW0z7UmwktesYugLzSy7892keL5vG38wdxgYpqsiwRN6X1%2BBgyQNN5dQqn9O2Z%2F8RKrE0LBnLS8hNSqiOQ7hq1vAxG3vt6%2B6H%2B3Hs%2BOIKadFyrD5xc3gblo%2F7sOVNnY1%2BDXR3zryDvUNPDessKlPEywtBnr6waeOeqdsyVrsI0b%2F3IwBiuUjuI7LEeK4r%2BQHweE6e7ujK5%2BoNtxCXYJaQ8xiJcGERKJSD3zt2gGgxCd00Uz%2BIQtNZxyf0PHg%2BVIq%2FjeOdeKuXQHIw4oOJvQY6pgEFnGps6zpWHOBHavfsTNIDgH8hokdkABVv4BxgpnZ9L80%2Bykzhimz%2BCKc64AmskOSLlPOljELkM%2FUSFEo4OPIHKiJZyOH%2BJN%2Fm7hXPgdjY9jVuytvNC1NhTp1VqfTp7ByTsH7Ovk2NNkx9i4d6Dt2usAyWAHBOEFFw2pdnZYcNVgJr5ASqJOeVD%2Bt8N5SgIlmmtHqpW0xZNQUf0gPwjnWPr1E8Ei2w&X-Amz-Signature=5391b9ef609ca83f3e9796054f310d2cb2975846a85f86210975b24ecb1856b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D6GVP54%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIH%2FuRCdwcKeIgbTHXSKgL2o9mQ6pJTUg2q3EcCWZrxLXAiEA2itkjv1IgSSA6sFV48L6XITx5Eyu6PlyPVj7zzi%2FnbEq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDMS0AOlsGJrDNuPY2CrcA7WZiV2HdsOwlXJbLs%2BttzJMaKJ8Y3mINgjhLCyw6IrCmE3%2FkMftGIvIFflDfovr5kXVh4aj5fELLomUrDGuBCMu6qaPHfA%2Fqezz79AEsSiYso%2BjIupwr38B3wSIpyGyMgx1K7reMs1XrhZfCafrNc1fwjTcINAk245yKp55TszyNuy5BHq6EBaNMOSm%2BCUC9k1JvU4FC%2BY3iLJ4sblUjEJx6yed8j6F%2FxTGkXiakGP%2B%2F3%2FgzOq4NrRwm2lqjae7pU%2BVKnfGV6oJo%2BIkTAIWDSiS6BhURMfUQ7AZciz%2FBnaYswNPg4u%2FjD5x6IeT4ick5QfPaWzHCoeoaflticfVmCwRGP%2Bb%2BALghkSSRem7qVmbw6vmDfPhHZKa7JQ%2Fnp0LqM69WF%2FzI2823aXCS%2BDk8tnGZiya2MbdpSRoJ2SedAZ7%2BYMEJhaU5xa0pshWmazbGU56JAfmO%2FtmXJ6e5D516Y6ZVRioHhVMPMF1%2FWbJuhn6fBc7Kzo8alYCAam9%2BTtwWKtsOH1lRINhlqAKeZQPwBOxhKAd35dVOztufgePjUNmfPI%2FUEph%2F8UltJMlFmWNzBUGSI2euvCBDbxvVxbLDRdD7EeENjAKIW3J1IZN%2BEoBevku3qPdP0w3gO3AMOGDib0GOqUBjoBtMWbOEgwzvpqAGRzP%2FORLgR7xpfiRn%2Bcz0iBRoC4iPMorx%2B3ESpfU%2FICBkX%2BXSV0tUx8NRR8%2BGl%2Fyd5bsjM%2FPEUFiKAUNBaE%2Fcsblogom6ap6RYKl%2FbcWFxErw0YZ6cxx1kaAY4K7LhKzcqynFhHq%2FSPpPTUNouirh6JbMVdXVCkJetBGrp%2FgYak0Ax1rDIhxrsShakxs2V5SIgR5PfDNPcb1&X-Amz-Signature=9c5bdde867ee376209d906a98e64c0412ba1445b6e3de626653a10c7c16a69f0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655YAKCIU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQDfY%2BeRB%2BLcCdL3F17700S7sXUVYGPnl7ICMmnFmpiX4AIgRqzf62CL1q4w8ugnhaz2vRC5MRCIJCO2l1xAoYcQTeYq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDEsbGTMdQUTfhOI8YyrcA1o7%2BkhFiTcCpnqR9frYAPt%2BVnmpqtl%2FD0FucqJFJmFrsOsezd8bsVSgA9ODSTzaEzGsjR2DotxyCa1qvQdFFDQ8SJMdCCvTAJzcoUtVwVJ8zwxaj3vny6vP0q9CvGM589gumACEB%2F3acTXNFqIjDMfLEfgEJFDqOwL7ehVms3vRljthm7BVDxIICthyiW4py1uYcat5dSzsTHF0dDcMAURLWXNkj%2F%2Fgzx9xiAnfwOUf5SOUVxijO9n9G%2FuUypwOw%2BCTOmOx5Ra%2FR7jQvKQzKxTtzBTCq5DQ82zowHg6XNBmEYtz9ru6dWYUamour56YTpux6CU9HUoIFi9NZ2k8Wm3Mn2yvZy40twxYxg1fmsLWWzZ83Mwf9kDvcfQMe5kSB%2F%2F6Crwb3a6HpUi9QegbhBbhdHvd518rdGDv2bKif6Llefmsb4hn2S5opahtz0%2Brt4G2%2F%2BBpAEoSIK%2BSxEODGs9zoZP9dqXvXvBLv3EBQNnyqc3JOIcJrX1tRjuc1dWixlC6C7BOGZkjncf04%2F%2BSLiOfgz%2FEBOoAJzRAymxPRvgEBAcfbaNLszCZfYhmtiBoMFmrOJEehEDRggLDqdX8MyQqKXKCJ3hu%2BPFvnXQ2zz9Q0kErH06qF3l4mAxrMNSDib0GOqUBPWRvq85Q03PF7fapluEfr2TwlmPnLQfO9RCf1nNDMRT0bFVK8eSSGi2rdBT5oduXfrdZXWeMVZerV%2FrLnR2DbRvTTpHHJDBBlyFTwgRoRSgfcE1bDvV9vXYtJIuljhH60y5iT0mSNmEDoOgQpjY1aix4MPDyD3wy61JYnMEo5Qu2t5LsZyLoNSUzoKgdxPERCtHs%2FhclhFl6HQMLUrQ%2B1qtCv1IN&X-Amz-Signature=b4ac5389f16692c14da459879e8ed273c866b80920c9445d8fb097af78e0c49b&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKPHRMS2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIHxC17nWHph6yBKfmycR8EszlUML%2BgW1Yz72gmvsME5WAiEAitepI23ccaYez9J%2BcyBlphKVlEuypR%2FXlMyOEZcbYYkq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDLVUoFBi8xTcA2CbEyrcAx3p%2Ft7wEglD%2FEbrpkNRKOWtHVeshNJGOSmg2OgCc5ekmsskyduqqwqQu9qmIXaTdmV4XO2vpvXeV%2BhBOd41EkIpHAhdl18pxzlpaJiMfZuSRYrZNaZ%2FaMi%2FiZbFMe9whBhGPFy5qTDO30L7NmT14UrMBQi4Af717ruus2nHNCiEnFWSPfwXs%2FHPz%2BP8UOwgjxjAFK5cyGrMKsqlvkZNQn2m3Sy5bXzvuvxA6enOVPNwW%2FcVmsrpDu0jcpAPMA7sevK19bKQBYLGjN2oegyAexuVf1773SeJZ1KR5At%2BWrnWuU8YNRGp8jLwvUSkq6eYSuglVSnMAkj%2FSI8hdS2q3sR98CvXuHW1d4q9irOv6%2FPpFRfY2vsd76RTG9cr05KihhGp40DNXbEP%2Bh1PNJPWBJshyGsst6Uzi85v%2FsVAuUFL5Ufs31KFG0pZLCbEULq8CEZAyjRkkXZdc%2FmK3AcIJ9YNqsXSS2onEjvUqwOrzfenuhc9qm1yDtVFoZCXmhGeQIMY9oB4dmqBQNg11IP9zCgzjfuRted3EGuiANYv0XSBZ2v2pV3ZapDhuoJrN9VLKOaRLFUurCo6IZUe8F%2FP6Em1IPPW7d7TIPfGaJDHJpH6adR0nhLt2XKXpvZFMIiEib0GOqUB2YS1pKtWvSy2Q%2FUwET5AoBoWcCYREiVZBWRvn6F%2FdqwOvs3N5NH7loHY7101DbVs3o4jdL8BpiwgF1yq%2BOn7jsIjbxSSrCua9kEBKnswN339HAgrmKTy%2Beb3IFj8AT4FOfVpoZNGqObxz5KbGi4xLtBCs5U8det4IDUtjMo0HfJAy0MsZh0fxZaA5iDHR79jFXTfx%2FaMG%2FW3%2FTFpjAuwGksETLvi&X-Amz-Signature=a969b05add174fa2f4a2a1cf5433a44786426cf3b8af8396810068a929bec882&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTXD3WZP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIDW8Nx0%2FvrdxY7qfym4hhgEilGGkrN8Q43%2BfbtO1JN4jAiEA7enEwW6zxkxjAIf9fd3O9vUxQsQ%2F4aGj23dABvpaoxEq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDK7NTghYrUkNayT7gCrcA7FpxLOsedCglM7KT2q%2Fyqh0OiV7sijDRLua7WGyxY3mVU1Cl%2F4oPd7QOqQuQ0cFgeXPRLA1UhDoj9S5mmfocmBIsP3M8EU4vyx2DxXdycK4jOSTmGWYEXjc9nVzOQ%2BQM6eRGFako3Ql7tPcGRfzKEUeL9wpHGWGWh14ep9b%2FKiC89P44xYcqjtz8opy3Bt4P3HN2sf5txSOpEhwm5zoIsKB9CUZuSqBKIrQiNX3P6E2aSlkibKvpehdVxktzApGYgJsCqG12%2BxZwTUo4RK1SMXj3xi%2BmI8SqiK3Et57FGwq4%2BUEmKWIZVcllncLVXfWlEIy4aUD6tEjkqoLQPP9Oo863OcJlyYxV6JvJb9lzyDZihOwl9OwB0v7fGrPk0sntSmh14tRqnlO%2BG2pzlpMGUXxvBqCi7BsL88LDBUnzrrLXOO0zsKNOBrPyMp6A5W4q5%2Bo6j0qlDkV2ndLzIPRHSA0Pp2vGliUVil26ED%2F%2BdhvIVT4HWeR50ukMAteSFaGDEGmxZ4D1T2muCT0tExYZMThykoNKbmTASfCcJecGvihLkrneOZWXnVDuwQOHzmIp5EI0pNP6wKUpR2qDLn1KASNxCxqYXCqc2lxpVDiosb6phb0A4F8ZE7bzR%2BcMLSFib0GOqUBwIwpvmkg5uUS6wPFnqaBexr27AegJWOb9Oh5v08%2FUzFqR6C1HBO0dFJL0bQ232AcVYA%2BUTHTpihfuB3A3FsOv3hwmTGoYobU3m0XI5cP1Tv5f%2FChG9uLyo%2FfTlHOdYApe9QYfHe7pqSp4t4nnuMFPmSEf6xKfglSh1o5TsZlQeeXMFsmqMcJJyIif3StzbRCGFXo5sM5KKtrAG%2BiDpcjxyf3%2Byjz&X-Amz-Signature=cecc64361f7b7f46052adf632fd540d5e9bf14c29bc41b31b1f07f2213217cf4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D6GVP54%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIH%2FuRCdwcKeIgbTHXSKgL2o9mQ6pJTUg2q3EcCWZrxLXAiEA2itkjv1IgSSA6sFV48L6XITx5Eyu6PlyPVj7zzi%2FnbEq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDMS0AOlsGJrDNuPY2CrcA7WZiV2HdsOwlXJbLs%2BttzJMaKJ8Y3mINgjhLCyw6IrCmE3%2FkMftGIvIFflDfovr5kXVh4aj5fELLomUrDGuBCMu6qaPHfA%2Fqezz79AEsSiYso%2BjIupwr38B3wSIpyGyMgx1K7reMs1XrhZfCafrNc1fwjTcINAk245yKp55TszyNuy5BHq6EBaNMOSm%2BCUC9k1JvU4FC%2BY3iLJ4sblUjEJx6yed8j6F%2FxTGkXiakGP%2B%2F3%2FgzOq4NrRwm2lqjae7pU%2BVKnfGV6oJo%2BIkTAIWDSiS6BhURMfUQ7AZciz%2FBnaYswNPg4u%2FjD5x6IeT4ick5QfPaWzHCoeoaflticfVmCwRGP%2Bb%2BALghkSSRem7qVmbw6vmDfPhHZKa7JQ%2Fnp0LqM69WF%2FzI2823aXCS%2BDk8tnGZiya2MbdpSRoJ2SedAZ7%2BYMEJhaU5xa0pshWmazbGU56JAfmO%2FtmXJ6e5D516Y6ZVRioHhVMPMF1%2FWbJuhn6fBc7Kzo8alYCAam9%2BTtwWKtsOH1lRINhlqAKeZQPwBOxhKAd35dVOztufgePjUNmfPI%2FUEph%2F8UltJMlFmWNzBUGSI2euvCBDbxvVxbLDRdD7EeENjAKIW3J1IZN%2BEoBevku3qPdP0w3gO3AMOGDib0GOqUBjoBtMWbOEgwzvpqAGRzP%2FORLgR7xpfiRn%2Bcz0iBRoC4iPMorx%2B3ESpfU%2FICBkX%2BXSV0tUx8NRR8%2BGl%2Fyd5bsjM%2FPEUFiKAUNBaE%2Fcsblogom6ap6RYKl%2FbcWFxErw0YZ6cxx1kaAY4K7LhKzcqynFhHq%2FSPpPTUNouirh6JbMVdXVCkJetBGrp%2FgYak0Ax1rDIhxrsShakxs2V5SIgR5PfDNPcb1&X-Amz-Signature=7e792ca585a2e524ce28383c9ff7bba41d3eef6efb7bf0d1a0c5de6813e93af5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQBLNJ2W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGRakGUrG4zRVrYqORHXmD5IRU59KAkb0GnNrmisYDpMAiEA55w%2Fk9vRNetU7Bs6I5oFUaMP9Fcb2StSBl7RYRUeXUYq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDHFetiUQGJpgNR0o9CrcAwv8Kd3eqCQmcNFq39TCRHqv%2Fq9eAltwtX5hSGgk%2F8dB5biQe8P6Xixlril7LY2gQnXNETjnh%2FBdaTO7sfiyvx66xBrFKaiRW13H5SQ4YGH7BtULbHOL3qIhfmxGzGMelVkU6t89x5vXYMS1O%2FQfvtLAsPRv7FrJyZlYtJchkDRoyIT6Jb9M2cHx5RHSK7lVovgXFSAHuDodeTgYnK0lDdImpgW%2FpspmIbXFOD6DUhIROpsAZX6udh7Lonpl1c3D249sOimxEbtIAzvme%2Fn9fmAnM7DneaHmYoM%2BNG6qqwAn1bU%2FRdpg6ygAYtT6VHF8AEwFljJkB5z1c0sVOroUwfEFUsC6SGe2Ap4OgO8QrpN3BGFniF0FXVtucP9yNW5QF%2BzYVL2kNR5E%2BBCgs8eurdKvcwvHwTCNSWmTXXNGWGbuAMvmwOvXXhDdkc3pQnd002F4KJEQvx6IsTrshKF5M5Fu5Fzz3NbBVgEvEzjraXxMQtyHHxlUPqcY9uk0yRgIsp3ZtzTfIQLoobUtQAfS6mSAgFkJT%2FupDLW83znD0ErylfOS6w3oIl5aX%2FE4PJGt8vhUuoTYAKj%2FzWoN3vJiHuMVWE7ty1tkCDGjvVLFNPzIRmw5Gw1kSReJm5zTMP2Dib0GOqUBElyYSBdPmTk1LcZfma1ShiaRVFy583kleP%2FzwGURsaMLLzDqNg%2FwSH%2FPEXjprH8p%2BVbdx7uAR5MSxQNWRXHLlJizf7TBobeHjEIregMggInmXe6hWWDf72BdvsPnbgErX6EZWztwZNUTFxHkQnxaj8NyArEy5%2BoWpvrzIfdzMxL3WC1s5Opo%2FYD4WGFtfqq12GaUo9RfRvY4saAH16i71cZdgjqZ&X-Amz-Signature=0011aec30e394d42c05fb2b656ca13ebe0bd351d51391ae217d931c205b21b05&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQBLNJ2W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGRakGUrG4zRVrYqORHXmD5IRU59KAkb0GnNrmisYDpMAiEA55w%2Fk9vRNetU7Bs6I5oFUaMP9Fcb2StSBl7RYRUeXUYq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDHFetiUQGJpgNR0o9CrcAwv8Kd3eqCQmcNFq39TCRHqv%2Fq9eAltwtX5hSGgk%2F8dB5biQe8P6Xixlril7LY2gQnXNETjnh%2FBdaTO7sfiyvx66xBrFKaiRW13H5SQ4YGH7BtULbHOL3qIhfmxGzGMelVkU6t89x5vXYMS1O%2FQfvtLAsPRv7FrJyZlYtJchkDRoyIT6Jb9M2cHx5RHSK7lVovgXFSAHuDodeTgYnK0lDdImpgW%2FpspmIbXFOD6DUhIROpsAZX6udh7Lonpl1c3D249sOimxEbtIAzvme%2Fn9fmAnM7DneaHmYoM%2BNG6qqwAn1bU%2FRdpg6ygAYtT6VHF8AEwFljJkB5z1c0sVOroUwfEFUsC6SGe2Ap4OgO8QrpN3BGFniF0FXVtucP9yNW5QF%2BzYVL2kNR5E%2BBCgs8eurdKvcwvHwTCNSWmTXXNGWGbuAMvmwOvXXhDdkc3pQnd002F4KJEQvx6IsTrshKF5M5Fu5Fzz3NbBVgEvEzjraXxMQtyHHxlUPqcY9uk0yRgIsp3ZtzTfIQLoobUtQAfS6mSAgFkJT%2FupDLW83znD0ErylfOS6w3oIl5aX%2FE4PJGt8vhUuoTYAKj%2FzWoN3vJiHuMVWE7ty1tkCDGjvVLFNPzIRmw5Gw1kSReJm5zTMP2Dib0GOqUBElyYSBdPmTk1LcZfma1ShiaRVFy583kleP%2FzwGURsaMLLzDqNg%2FwSH%2FPEXjprH8p%2BVbdx7uAR5MSxQNWRXHLlJizf7TBobeHjEIregMggInmXe6hWWDf72BdvsPnbgErX6EZWztwZNUTFxHkQnxaj8NyArEy5%2BoWpvrzIfdzMxL3WC1s5Opo%2FYD4WGFtfqq12GaUo9RfRvY4saAH16i71cZdgjqZ&X-Amz-Signature=3a56c3840dec538e1b807c28c0e7844b005b9e5fb17bf29c5170b7c17d6730ba&X-Amz-SignedHeaders=host&x-id=GetObject)
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