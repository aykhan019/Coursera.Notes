

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673TDBROP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGPdXrbJT1TQ5R5WYea42ZMFLvm0LGqlAotgk807%2BWkqAiEA40%2BbxliJ93m0f45Yrab8nFgYaX6i06r1bzspB4lfqTEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2zuwb5IgNwOF0iOircA2rd9xHC3aHMBAHxoPzKz6QeFhUBAqUdxK49MOXT4VVnCSKjy79zVUQiQDkaA7SkHthtkF%2BeKrlrda5d7C2AF6cCuNgXYqX5FhLq5hOvu99kmobasKG8OQSoY4NfncMbJ4rJTdrM6ZB8WMg8etysmdP2RVA6QtCtqH7BlazQckzXfRjey9FcrdkIehArAFMzMKZSvvFT21fsRS6nrX%2FDvT2g5IYhtsTQVBsqXUSJ1tG8RhO5kKJZyRFSFmWYNVkj03OqhKjAKGH7NK%2B12G%2BrIElsLHi7JtsKUGtj3KEzg6DY5b7UxE5%2BIXCAmiEzc9v9wxPuu7ylReIzHsY4AspoBjN6oClGky0sPVIQBP0BpAgj6zHNnVXINPkGCtV%2Bmh4XQQW5NANZl6eUokJ%2B8GKFNdJiCGo1zssSo277by0rYADwcaTcKeYRLwjjGcTqrlgcloTrCI175c5sj%2Bt9Z%2BJHepkY%2BZT1VeloVw%2FjMlQj3orf70EvdfoVS7KapV2DZr1CIOBU83tgz4MwRSr%2F6URc2um%2F1mygBPfVRj8sfVJVsIcIblBcKdy7TVoSBbjHrCQ5K3RmAR93cQkz58offm4NyFbR0TvdGQxU4sipx2oz%2B7vTxR9R9gr0haXUU%2F6VMInQ8LwGOqUBDOllaNnhddLx9tK2%2FmDgUldwgRGrK5NdBeSA0kR5W9%2BJKBIx4DrdNAJmA1ksxeBJpElKaFlzWzKI7HU8FhbwHRmBfCHRSGC86FE0XDR2JWpte%2FCOZIFe6c9%2Ber%2FmtCc60t%2BTw%2FlQD7JAeocNklpo5g%2FK9Vguqp7DgirksLA3shGMt0RblY6GqeFCE3ofMoBuPG8yc7bbqaxqfUpfQcaV44B%2Fn2ws&X-Amz-Signature=3a16fab78db6439c12ab9a99771d34e06212e6d30f2290a773057c3bf4c5324b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673KVPE5W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA4FyNBtc8%2F7lq%2FdzeY6P1hlG2jmMgTq8xqutcJrEDUoAiBwEcqxeWsAnNmJCjUodDEgrw2QlbZx9fXlt7b1fdkCLSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBqVT0KZrlHVZFLdUKtwD2nkw1M%2FabKN6uRoi%2FsFIj4Gy19uIesnPxyJfuQoIXvP3f00KhshC0J6Z%2BD7AW2PsUM%2BqngPfgXh6U3yrOdnKrAjUHUiLjc1D7PUrl8Pz6uicGPhmiBki2tRnwR5Z6dWKbW2quGYW%2F3lXGmU8KQgho3IJwH1goMbcQPinWwf15vegeykaRKCLFTCMFsxGq3oOa%2BkOi4iGs%2FD7NJUODt%2FMwkJVYP5Qw9jjHgTOih6FUViSqhw%2BkDetDgb6FKqJ3%2BXi6mGCRVsu8l84matesNB%2FXdLQFv3zDYlbNq%2FzLhBOq5MacjimXkTCQ9%2BHIIYEta3SIqCectcdxohtSxufsmZtJHljkk6W2JIGKmI6BxrzNHZVYClL%2FvP%2B2nN7bhrjrOdZuCnaDZE9Od5KZFg31vP%2BEQ59rROklNKOiRlQnFwVZhoy6rxwBp%2F8JAjOUDRzXnlvhTeieRDKN3WbvHWiDWRW%2FpPNDQeqnP0D0IdAbTd2Zwdaq3lgsWsEhXIbDRjVhFnfHko3FJydwmRZIFA%2B2NHE5FHG%2F2qrQ%2BiwYyXq927qMW9XQdNDsXOOFPu9iiNS5kwvel6lbcJ%2Ffd6nn%2BIkJSzq3ngkBWSt3xFseRjuBkR3sawcSnfb01Hu2HrDhc0wvdDwvAY6pgEhgEiwJWW1VdrYE0WzmjygjWW0ED4%2FKuPaVwFkOdwMR2CxPJq2%2BnYb4851Zltp8ZSHZgGT2xzZ84nciTfx7HUZVt3tiSvFKKngPiZXdv8JO6IlP5nFJg76i1lBEePZHr%2FHP0%2B9frq8Um23uTNzf31k2PcZD%2B585n7FIf6NOd9BdQXtjj2AyOruNZtJzHU%2FfzT5QVLOb%2BV%2FJPJ9NdTEb5U7GgEBX%2FmF&X-Amz-Signature=4c91327b2c44bf38176fb47f70fd37c4541a02f7d5f6ce2c14fd6141d28c1091&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMF5IEEL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDubaQiMki2yZrvLag6NrT5jvm6VESB3OxtQU9WuZpeJQIhAKjWtGWeYgjdtxpkOsMV75VdKXp3nYVpjUYZlCXCuyE6KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxSjMJfm95KhU1EuTUq3ANGHHVUJKP1rvBqITPFkMFe5q5KshcajZrrcOQfWUCydNCsNpc7VeTDFBXched0OPRJnxejuPcPla6SwZkRBwXBPzHsWxlRfFamM7HVNGE18jazN8fOrVRY42n26TzvAO8ER6PPMYpDz3FwBXZ1Ox9sNCInMe%2Fn7KHV3rOYQPvn7Z8C%2BnVQjsZptQW9ybDILItP3fB8bhcJtD9r6eEfz6F4OoUQfjZrEx3IUrrXyh9ZTZVO0qQLw2zLgWAwcaXS4fKN4s%2F7SuvV8L5ZdHXvL53wmBXjMhtke%2BXGkuwKsHvZdXnCQFAE%2Bvassf54Br%2BcX2TMtPBsx7vRRE%2FquGZkuRAR0HUup5P6JQZRKME2Pska9bPpyEyLYBKpzYDzPAD4AZIM5czULSufn7fG9fTSBk%2FYr%2BKzftIl0K%2BTP4ZleKNiYR7oKJ7im1bW1CBMKXRd1eJ7S3rNpCfqvqWqMmofqHZiYMQIScE9oel27V%2BbM4rYGZ7%2F3rfCm3zXMCBEF4Zwb6cORQpl21WB51UvqM%2BtLyR6thHGzb8QfDLGMi02gFQrwL%2BaZaNwbGg6kmMA9Vl%2Bn92yQr%2BOMJTOCEZJfWPrswzBONWwDno7J442wA3wnvOfHTqB9W7P1GajJNKVozDV0PC8BjqkASJJpM39wXWWvc6HDo1BUu5cxZLYmaJKT3cfd81tFfQUap7YgmvE3oAXWEVmpeZY%2Fb6BRZQTp7Ty3WvYtLYxnFBIlnoA0SfXeIQWOgvdEjxFy2q2wKtvlcLmgLzTHc5M6HAHJG71YuYAPZImaSy%2B5e9i%2BTevxZ9uc8i1qhy4XTDeqiHGkPbG%2BF70cl7wgPAPjizzgWGlwCSjndzyMJNpjtzAq9ju&X-Amz-Signature=124423b71405df41b1c2c1670393a0acebd1b952bf50d4519700b5a1eedc4610&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YGTEBVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQvpMS9AE2%2BLia5yGrEeK%2Bt2CnASaIiT1OlNqh18foigIhANsiwl8MtJSBD26s03X%2F%2FSHnOoRGIp46BXx40tp8i%2FIWKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7%2Bp7Wnt3%2B8K9Vphwq3APCfnJPJ2jnDIbfZKdDqzQi7s12iSyRp%2FrUb2UnhCBB1gU7P9meQH0TuPS7Pb38dUFHHaijp2pjWpczybwZdEt7MrO5yt%2Fjo1mO4P%2FjulhGM1nkey%2BiOnehi87Noj7My6vYHOckOaWX%2Bs1P5gtsh4kMQmuneJXqLVeWG6%2Fwn%2F8frhOIt9rmsdRhlPJPy2Q8Q2gIJ7qAA%2BT2b6n6%2BicLYNLhOcg%2Fxm%2Bm6Rsi%2BK9UU%2Fldkj4iJqW4lEnGsxEUC80jUM%2FdY7x8f8jjwPeTEGTTIIg0VZYg5wVVmSy9OoUSbjpHnfut51tOaCNuA4A5hSXUPKl%2Fea87UZ4YYBrwpaEKr0PrvliIaKUkcT1gdXZ%2BMJ55cBxQpiJMwJD1voEXRB9DVmgU2LC3KD7n8Yup3tNhewyKVgrtKBUfWb4%2B%2BsgrJsiJKvV3V7Ess21stFGISRJWKLA7R%2FU170S1LI3dkGeI0HRckTdZTOCcJAsFMhCYDEcw%2FViez%2BmnjGx0MZ0U6qwfTGLzum7%2FQhR8rtUFLPedXG15csHmwGYIn7pKTfyFlm8eD9PHottCKnanXeUfHy3s4qs8t7eF%2Bagx4RhacfSlUWuohHcupMpoDSzMODo5ZXg9IHePuibpJHoehi57mTDg0PC8BjqkASYNJc6oKL87KboRi%2FT5%2FxTK%2FlidfQ9mY63zx1sLS3yP9hqXjwzhchPAp1birsv3B2fh%2FrzjYcfVL7mr1o66%2Bv%2Fmaf0gHk276lMZI66Qqh3by5c%2B9P%2FUNJmTTtwOr7IvpiasAMna3HKwSwhiHkalhHokIOn5llbXldeoZRd2LhAiOU%2F%2FzvE0zf0VnJzt1mVPDvqf2HXWVj8xh8s7oMDerwRT9P3M&X-Amz-Signature=3d4e4df6d63a8744928f365d7b912890f09a9374b9dc9784d790a2d676eefb77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R553GJTC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhJSj4lSSPQL23IKojfzfDXz1%2F2r3%2FJEWOPbhVr%2FIYrAiEAnCeHWQPLIMCRrjeVXREShOpFn%2FLShtWFzeWkec4PhzYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPTnn2VMSR%2BzgDNevSrcA3n6%2FLcIx6uDi%2BtLqLFKodGHoA2gBPnhBOGqj5YRDT42LknOTUrtI7nWuuZ2Ozwd817%2BDpbQtNuf2LLGgGgy0lxvzCdOymquF1Cz%2FjE1khPkc0QikcT1qhulvhm4AT2zEZfIV6nRjZKiE3%2FmWDbafweh9PS6TMrjlTsKvIr86j50gmoXcpYnJcwsCD%2BUII306nYgIbyz8RPHknWVmi4yX17IhjOBzF%2BigOelLdr9VqTqx7WZgiZUMY%2BJTlouTssvjiFVH0Oo6UmuSElyMj5R%2FElDgs5Y%2Ffh01E7xPn1WioV1JJA2qjfbSe3Sb3dmm5kr%2B%2FAYDGLkA2%2F3AdgR1X3dnNradhnQg4sldDYnlGY4dvoADPdEpVMOKDJMALSbChWOylV5X0d%2FzzeMq43Z0uWpfY36GOci7MpBjLXcB5%2BC9y9oj8MG26IkGe%2BDBjhlYtueYVW60VRVEPCIwDZHfEEe9tH6T82FLuxJggIXPhdtffTee4NPRJRhphokfQYOuY%2Bf8xYrFD%2BecCVjtGtrDnOMhXQFprk3aJkU%2FDkZC%2FefXWKgjjgEOXErd7G8%2BGc5Xp8JEOUqLYF%2Bivbz%2Fm78YrFCG7HplH3YVXudifAvu30VO%2FgQuGgo%2BEUoQrCHD%2BG%2FMMrQ8LwGOqUBZ%2BnritDXcgN5u5C26CmiDdo8O6CpX7PjIEEk0eSecnrjsaSiZpe4a11dt2FU%2B7o4JgfU%2B%2BEmc%2BpjBdagzxs7Ao31is4SukhAFkelaK2jm%2FXntwIVFhRSyX3fjx1EuFfM0aG8kYh5YawFfyWuFqY9mYY9kUBZ0w1k2MNNf9QOj6XVKff%2FcqzzkIv0NQSDJa2NDDpRpGXIb%2FNtH2eU%2B9UGEa%2FoDjk8&X-Amz-Signature=1de2789c4f9e607c01d41593aa22c7d5ac99f4b9088e46eb341d636d24ae5e9a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBEEGYK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXxKU%2FR2WJ7%2Bw1C8JBR9dmB951QI8lKjx1RBkwTZSv1AiEArlW0q9rKWUxmw%2Bs1RRKDofi3ryKq4s3JXV1Mw%2F8IZv0qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLTmDXzq8PZnRRqUACrcA1Voedj7ANv9mMAwMqAqKAfz6JP7Vq5T8k6VqRLDDP5K2w5KoOaNfAn7VXBluFbMdfN3hhrgglEqHB78KBxIjpADGUZ4M%2B5bGQ9WYdrLxQA6IIIpyHnENnzDMmAro%2FOjl82Ww1fY9YrMrKOBk%2BKThh7RWMxqKRUMKF8A19RnzrKs8zZy4y7ZLcyCgegJKp88Yqu3YY8qS%2FZiAnnNSNu3E0AvvWC4mBnRWMWh%2BuUn0%2Fp5c9HC9gsDYfm60%2BfpdSbQc07gDwK9VpOw4s9NM9AiQOykNXhuCpltwK1hdbIBpKuorsWydjE2JeNbP%2Bbn%2BBIW84b0kma2bJxHiuMz5AOE13%2FluDFRnQvaRCUnFxrcT6nnLgYP93R%2BtDoxwSAEs45smWBZL6ODCxhKMXrS0IY6%2B6Vj0Fk%2BFhpQ8nPNMpEODZs5IWySkCx2AaeveKSWfG6YLmsSpO8n0V8DpTJ2ZfQgohk720KhkEHLPgPwsfYbZKx4R97VeCvRXMh4i6z4ixMhEWJQj4YKXB8HFerS0qUCWsL%2FInIO8LJ4NGTFGXsdY%2FEIDRnGGursyh0UDPAu49sWAwy9VEtvb%2Fu6lgVS%2FFk69Y3MEtMT4ITT%2BMVRXXh1PJ2gyFz3rdvYDC8ncOEtMLTQ8LwGOqUB2W79YwV9v5GpyzCM20V9tnNbQkL2OD%2F3lGlYxLyXFO6UU5u5tRQVDM4dZSOJCW1t%2FthRkFc7mGkwQJ0n%2BRTj%2F9WnbE4C%2FNQL6ZxL3POcZ2Jxq0zugga%2B%2B8tuOjflwciXA45YlwZ8gjqVex8IATZP8JAYlsww3V%2FPebvzx49IAj7KxDSNXBsBflgr81P%2B%2FHEzfFllk5DZtNg1xMrXy8QMaceeb1TH&X-Amz-Signature=3767e81d51fc0a9031b3afdae9a6c50f66ee2e2c541d207425ea29b944be64bc&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3G4VPFV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzXi5vZj9f0UrID6ciK1%2FjIijjT82W6fFM32uQfF9wHAiEAukPnEYGmUozKD9GTNGdDRMjw3aT%2FlSLWxxaDJO2k1EsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDACZzy0EERPyxQUceircAyKsERR5XJ9ibUlBoiS8z3aY2Xb%2BTPHdALQc32c6Pk7ehxZhbuvcTVnz8O%2FGSuG8rskTcFk%2FJrjmJ9ViGS105pkdRnMaFdiR3TeZqbMBgv1Dij0TqxMH3ojzk12hOF1Dd%2B8W7lDe2sLK0anr1AKD7AVnp%2FKRiimMsnAEN12J86EjkZdspvTwugQcDeOW%2FVNZWxtZIseoYHDqLj%2FMfuPg00Y0s%2FI6U47%2BEao0WqfErKGP18gtOu2rAOMEYsCI%2FiS3m0W2GMBRbog4bX69lqHcNvrwQSvd2EPDzxJBFNil93h8%2BSwCKym09uNsWB1q%2Fo1fbEchWiO%2FVoA3fYnC6RR5HtAFHNWXb1lR3%2B%2BD6lhFD%2F9j672TXX6hyLjcYU8oktYA%2BTj4TzSdWBECgHpZkJ1QwMl5d3OTMwL%2FW3E0EVC6u6Leh396gS7dGGFb6T6wdZ1mohv1niAQzlezzu8BthpiIbA69DjQNW8gG2Of8H302g5hHkJC0KC9PLIo5HtY02JqIHuTPlXDOFyLYBeyEhrRE4uGkZYH260I6Q5yItBenEyNidMjFqjg9laAlw1c1jV6jJ46pWrW%2B8hkY%2BHQ0YqwSfR4w6fZrvrlweBbODSe9IiE019fHqO4NqH7PkQCMJPR8LwGOqUB8durKMCVZdjsx8hmvOiT9RRthl2Y1CBH%2BDDz626aRqUqsgFUUAyUn0XknxvG8yqX9XcpMBsv6etjo0c4%2B9JDb%2FL0Bexh6ydMmT0b0sfayI8Dnc6FxbPuvwT2GE3nfBjX7dEm2KmlV5896a8FJRi%2FdNIlEdF%2BEHoZkdCkDQfYGLAzdqLkLXNe2STnwJbucntbEDblaxXl20VnEy4ISewIdI2c7lHe&X-Amz-Signature=2df861f9747565cdcfff85fc1679c7de5bbc934fc37aab27fd573e575eb3decb&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YSGX2MP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCz3jk9o41PSEGtVPBC9a0NQy2GfPPs%2BoxjO1amaBWk3QIhAIva4peqhwYStujlncA8woh1UG22tUNtyQRPBnIDsbFuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwKqlxkmyCSs%2F51OEYq3APNNvBiFqDdPZAiHUbN3F2XUYVAM6iTfkBJhbZo%2FbN8JOVuN5lcIYYYm9GhI0eSluTsKqWrxvSYltC3lfWi8fy%2FXdzcHDLws%2BrJbGR7GDEmZqr22Vol6NqQxJDMU0PzWmJNSTe4%2FU1dRIg2bEfpD0sO4eZEpMOKKQi4oRTgTUNHQn2veJhK2cBxKl2ee4iCsk000QeLXUEGdtsLNTq6CQf6EtRaWTJ2HEqWRh0NkrPQ5dOJZMBcK7QuG%2BR7maUpO78yx4b%2Fg7URi6cLV%2Fp8zVjvhAfkcveAXRddw8iV4YToikGoJIETc0Rw2mf47%2Bh8tCNjdUATvbYlBNT9lqFs9xKo2JES0QbVI%2BwlM8QNOcqRM9IfpTiRsNnXeG30P11vGm2JBcW5usuUjhAJJgSbWqDI6Do3CwxffSwX5EimgZuEbUgyb%2FeUYyqxxtsUEaXjjl6AHuMDhKl6SbSFJcirTL%2FpYqp0k3TnQn7QgnnjgJPYzYg5BsPXZRg1Fpptw8D2Mol0MGuJvO3jTMpInqHu7wKuFWfcpn%2FeRnEyeagC2DDSFOV1bmnXfj%2FQ3JMeIpPUNlnQzOiAI4bY%2Bu4j3k7HprbC%2BKsOpFsQzn5SjVJnhAgOqpdVb99Cp75NZtGpkzDx0PC8BjqkAWOQqkKtKlHGzmMeNCoviOBTlN%2Ba9ofJl9mF1z2tEt73SO1nImQuRvH6UsPGhQejwbZULgPm4j0UEuM5sWAIR5lGjvAPtOII9VMNmUiDAvf%2F1uMNjz5vI5uNLquy5YzeUg5FzWG51%2F11TlLPo5klwxdc2J6xcrMW%2BhgDsJjrEB5%2FRU9RLbTDocYIHQfWSAbgodvIoZ%2FEOp8aa41YgTZKDw6bLoew&X-Amz-Signature=145ec10d0cca1a2c586fbfd637e55e9a667dceae50d5ad873163ecb337dfe0d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R553GJTC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhJSj4lSSPQL23IKojfzfDXz1%2F2r3%2FJEWOPbhVr%2FIYrAiEAnCeHWQPLIMCRrjeVXREShOpFn%2FLShtWFzeWkec4PhzYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPTnn2VMSR%2BzgDNevSrcA3n6%2FLcIx6uDi%2BtLqLFKodGHoA2gBPnhBOGqj5YRDT42LknOTUrtI7nWuuZ2Ozwd817%2BDpbQtNuf2LLGgGgy0lxvzCdOymquF1Cz%2FjE1khPkc0QikcT1qhulvhm4AT2zEZfIV6nRjZKiE3%2FmWDbafweh9PS6TMrjlTsKvIr86j50gmoXcpYnJcwsCD%2BUII306nYgIbyz8RPHknWVmi4yX17IhjOBzF%2BigOelLdr9VqTqx7WZgiZUMY%2BJTlouTssvjiFVH0Oo6UmuSElyMj5R%2FElDgs5Y%2Ffh01E7xPn1WioV1JJA2qjfbSe3Sb3dmm5kr%2B%2FAYDGLkA2%2F3AdgR1X3dnNradhnQg4sldDYnlGY4dvoADPdEpVMOKDJMALSbChWOylV5X0d%2FzzeMq43Z0uWpfY36GOci7MpBjLXcB5%2BC9y9oj8MG26IkGe%2BDBjhlYtueYVW60VRVEPCIwDZHfEEe9tH6T82FLuxJggIXPhdtffTee4NPRJRhphokfQYOuY%2Bf8xYrFD%2BecCVjtGtrDnOMhXQFprk3aJkU%2FDkZC%2FefXWKgjjgEOXErd7G8%2BGc5Xp8JEOUqLYF%2Bivbz%2Fm78YrFCG7HplH3YVXudifAvu30VO%2FgQuGgo%2BEUoQrCHD%2BG%2FMMrQ8LwGOqUBZ%2BnritDXcgN5u5C26CmiDdo8O6CpX7PjIEEk0eSecnrjsaSiZpe4a11dt2FU%2B7o4JgfU%2B%2BEmc%2BpjBdagzxs7Ao31is4SukhAFkelaK2jm%2FXntwIVFhRSyX3fjx1EuFfM0aG8kYh5YawFfyWuFqY9mYY9kUBZ0w1k2MNNf9QOj6XVKff%2FcqzzkIv0NQSDJa2NDDpRpGXIb%2FNtH2eU%2B9UGEa%2FoDjk8&X-Amz-Signature=7f37b102c2188f80cb60da692be66a14b777df3806cf7a2e3423392bd5f43467&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGSMCX2P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRQVLgeY18kQf3HEMSMQYHewrd1ZtS5UVshRdTBRHRkgIhAI4Qt6vO%2BHa4IWtziNwnxRUDBPI8r2nAENlqICB0%2Fhf9KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx3rJR%2BU25Fv7m95pAq3APe4esxpEvBVWKQkhYAJjRQjjw0J6ewfisqATmCc2EcMgaQxIN%2Fqu6DDR%2F%2FUNJER6y%2BYX6M4F%2BltDumU01b6XO7%2FlUeUkztyVRuZYpzgD4S3dkoGnP0AGMSbTWj38ZZ5jj461kjNOdFivNQA0LbqRmMw75KIIZuek7eS0DtPY7gdhqUuskPkykWFxsupVEsN8efs5aMlT8WLlu4FvDR0YCXQ%2FktVTu1bU38pQQIUnTAg%2F3Jv0E7utSdqFh1CMzU8oYgY6plm8uf5mSlgBSO9PZwPv2ATmg52E4%2Blu0AZufKt8%2FvrTvHYOxMC7mtsC%2BNOODGP4jfAWBNopV1fIdUqHgq88E4%2FFKRi0uLTQ63tmuu7%2FvlSQwL4rgg9SjsSx9xnVfc4kGo%2BIRS0tl5rgB5L0vybYueBR2dcp0561bu%2BDmn%2BKlHB1O%2BmlsWWnb2A6qs0jXREWyOD8BDyMykS5wIC5H7LAkNVi7S5lLhsSSmljvs2Bl1c5lGm2T8rjLrH227W0loqy%2F1edRf1E9E66jBD6ici%2BgQx%2Bur3kkjaHESmyf5fP%2FnmmEuGJggTG%2B0vMd%2Biqqu%2BKLt6fwB2B9CdqJv6%2FxLOeQo8BWOmuqnI5WqbqA0qZUYWbSIcyfBzBRPcDDP0PC8BjqkARBsr9f1v%2BHX5NzS3SRfjVS72ZRSOQokx%2B6Jrbg2M5uaSwJS4l9sqZaYGvwqe2%2BVmHxwwm9ZJOJgcyC80HE%2BEh1tcJYDBXfYSFsHY7WpiVLHmpWfyfSYUSfPaLFTbllAP6KsCHtNjSaiCtfnDbHQciA3itTY8j4%2FDRBxQliiPNl3aXBboFkzn3X1wACc7PGPZS9dcOA9dcwGh5loe84BwCLXa%2FNF&X-Amz-Signature=c65fc8fb3e732706cb53d101feace663c6755ebb9b0b80d505cdc4c1f5232bdd&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGSMCX2P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRQVLgeY18kQf3HEMSMQYHewrd1ZtS5UVshRdTBRHRkgIhAI4Qt6vO%2BHa4IWtziNwnxRUDBPI8r2nAENlqICB0%2Fhf9KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx3rJR%2BU25Fv7m95pAq3APe4esxpEvBVWKQkhYAJjRQjjw0J6ewfisqATmCc2EcMgaQxIN%2Fqu6DDR%2F%2FUNJER6y%2BYX6M4F%2BltDumU01b6XO7%2FlUeUkztyVRuZYpzgD4S3dkoGnP0AGMSbTWj38ZZ5jj461kjNOdFivNQA0LbqRmMw75KIIZuek7eS0DtPY7gdhqUuskPkykWFxsupVEsN8efs5aMlT8WLlu4FvDR0YCXQ%2FktVTu1bU38pQQIUnTAg%2F3Jv0E7utSdqFh1CMzU8oYgY6plm8uf5mSlgBSO9PZwPv2ATmg52E4%2Blu0AZufKt8%2FvrTvHYOxMC7mtsC%2BNOODGP4jfAWBNopV1fIdUqHgq88E4%2FFKRi0uLTQ63tmuu7%2FvlSQwL4rgg9SjsSx9xnVfc4kGo%2BIRS0tl5rgB5L0vybYueBR2dcp0561bu%2BDmn%2BKlHB1O%2BmlsWWnb2A6qs0jXREWyOD8BDyMykS5wIC5H7LAkNVi7S5lLhsSSmljvs2Bl1c5lGm2T8rjLrH227W0loqy%2F1edRf1E9E66jBD6ici%2BgQx%2Bur3kkjaHESmyf5fP%2FnmmEuGJggTG%2B0vMd%2Biqqu%2BKLt6fwB2B9CdqJv6%2FxLOeQo8BWOmuqnI5WqbqA0qZUYWbSIcyfBzBRPcDDP0PC8BjqkARBsr9f1v%2BHX5NzS3SRfjVS72ZRSOQokx%2B6Jrbg2M5uaSwJS4l9sqZaYGvwqe2%2BVmHxwwm9ZJOJgcyC80HE%2BEh1tcJYDBXfYSFsHY7WpiVLHmpWfyfSYUSfPaLFTbllAP6KsCHtNjSaiCtfnDbHQciA3itTY8j4%2FDRBxQliiPNl3aXBboFkzn3X1wACc7PGPZS9dcOA9dcwGh5loe84BwCLXa%2FNF&X-Amz-Signature=e57a23477baf7cd6ac1b1cf20069cd0ba44cb2e0806f2d110ec8b8eae23df270&X-Amz-SignedHeaders=host&x-id=GetObject)
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