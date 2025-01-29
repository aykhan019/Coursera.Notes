

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NWCR5TA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXHAP5OIQYMpG0l29ASFXw7OBrjjJobghQ3c%2FW1fIXMAiEA1exsqbfQoTTghUvLCN5BAJcAbLylMnITGe6cjgjLfh0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkOirenNy1zqf%2FxMircA2UToVBDcfo7V%2BGk8Pbca3nmV9StklXx4eR%2BVoS8MkrGY0FPLQCZ2VZSTbtXPp4qucxCAGzWion7wTcLdXbael6KNdAJ%2BG7UIhe6mU%2BqONh4SzBjPdJ3Rvu5ZhVXJKWuh3LsUi8TEZZjFNvs4%2BHB42okbOOMPlITI2aFQchLGcTNezzxfScuAqSs6d%2B9%2BQN5HoNCxVqasUnCZ3XIIqXN2aeup3acZdnRiCedJQx5ajGROMBBnu5Qh9Z9QI5sSK9QlI1Xz%2B2mkqN%2Fap1XfCBEGwxTh7HMCk1Rr8r9Y8%2BTJbJHroLUrgG4q2zJ2BFDjVfBnclQOBz%2BFgSH0Q%2BxT7Zoihuc%2BEXFQ2rwVziafoW1mRdl6QQYKdWCGxqybihZmMwMlTHW2vjZFT4pblbgfENx0XhuwfM8gaOJUabMyFMdr9PHkaKDmM%2BtLa1BiiAv3AY4fneOi4kyV2cPbqa84w7q3pWsDEIL4hjXpyBa7cfqwi5UXWhaOCw7Lo12r1YMbh1fQkn2BBVPMRRJbCfHMejt6FKDWZN0Ll41iHVbt6mF1ZpsEWJ7bulr0ESOvGU7zHr%2B0Ry1%2B2WEV3Pxa7gT1OdoMzG5Z%2Flv1pLHI6sQUjlIZrYoNvF%2BZq8KyB5%2BhfGnMJX16bwGOqUBs72pLKksili%2FfE7DZ%2BdphsNjGRVD1%2FCXHQj7GlA%2BglBGb9PSpC59VzBNOB4cXiIhFpITHPlPxRas3Q7uvC16BpyxeeFxEhyDAGus88hcnIeXuakq7uQAdaFh4z6JWNxpWZYyWzIcwFBwbjUooEuGcvjtxpqZ6B8IQZBwB8K%2BXXwHUydcVQhmcwP3W9n6ZhAjnzEPQ7iaxIgEmkrgB7JtTLvEv5Gm&X-Amz-Signature=2707e5b5f0d8faf175792972e687cea5e2a394369e1715249f158e35d6757926&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJSCT4K4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1vGv2FvGjmKQQtz%2FRb58Y63HEmhGvbKJO9hQuxyQahAiEAz8V8NeOp5GzjnpBnBKn4jigPTSwyBk43WQTYFJGO8vgqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFd5b8UjdpwM%2Bar8ZCrcAwNYClcQLyffbAwLE8QkSBhuAd91JH37Do%2FYuNzatnaZE%2BLKuIqBp3DLSgh4wMIPyXLsHpx4JpP36gPzRF36tJZRyIAVA%2FEYTb%2F5fHwgkAq5mc9gw%2B5xOKHfqV4XYbVSqTXr%2Bks7zB5mUwgvoeMbRg%2FNaP4boTISad%2BMRAcU9MSnfa2%2F1S9nflFvML%2FsJW4yPnP2Ac3G24DMOFeDpN0z3sAUkaPcP7GVN3rJqN00fUaBZa0BWiNMfoBtCfWurQk7aRvhpTG%2BysmXRjFVWguOrtuaQz6OjJbhGsrsLcDasrJ%2FPbsY2QZGasZergVoAJReMRIaUUx9FgpGf9l%2Fk%2FrgHnHmywedFXON4NYLd0BmpZYMTpQQWAWQuzX5PIi9yaSdyoVYI4y22IfEoRDVq5vX0XKj7jmaCfakPXvylaRw%2BGiMsKJTqD7N7Cf1ydqUKemzBWYHNqJBeJwEKQgE3sJAvTKCbw7fDQPohp5WPlJ6Uaj%2Bbn1voi8Uzo%2FphyO9PeROtXxS0vK8XDwIF%2B9Xjk%2Fr%2FdARsiSkv5tUNyFh78hu6Sl4s5JFD0TtlM9DGf1a%2BKtBVSYlwPHNh%2FkT6fHv2tE2m6PWbu8vhdsz3KcBdQhLL8HfEIpFvMwQYpxhI0XbMJv16bwGOqUBvLL8Z0J%2BSqaUBonjZyaC9igVaxB%2BqQ1z0S3pWgRXC9fckNyLE%2BYWL%2BMrueHz3Ht5ERUZLSpRIdceivcKDersPdVin7qtySUDqfwxCFA%2FAz7PFG2WQ6QfTXOYhAvfb%2FEkq4muHEwkrU2rQdxnaXvQ0H2o6KE%2FTz%2BN5FC2nuwdDn5SvRGNvwGe57ct1kL%2B%2BYM4uIo3800JtvQgXSm0EpT3Nxmsu2Zu&X-Amz-Signature=a221e3f5394123aa0804eb46a19cc8a638b71d314f7cbeb1f40383bd673eb2ad&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CBO2G67%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8XwqFx%2FVgh5iMBUORIWHMMgE1476Q%2BK0MDHVjKr8fqAIhAKgZe2s8QrtMd3SebKxggiMSSrMcapFSjx9MvksTy6f0KogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTVdbFXIYn11322EAq3ANk2ArbqS3DKN6rvjYNAkNzVyhhECmFcdyBwKkOWxUh2jRFYuYqlobUM%2FphIz%2FtcF8lVJWTkaUUnjXAv5Udjl5pAEYpqbH%2FTYcTHGRizmXTAa4hES0%2BKwOSUTyLDJduPfVj9n%2FiHjuvumIsB9%2FvH1H6tXr69rUiCLPybt2YWVWyMVpU6Hkn4icRak1qsqw%2FABO9p%2FCYhoohP1P%2BrVnJkAoxZ81O3lDiGwAFAVqWcdcb5adaiumxK9cpmeVABt36i6RuxLEDozfpWbiL4y2fkdlaHWOuCJ4mFTNjJI61gfVirZQqd%2B8kbLqtB4CH6OQjE2m%2FOI5O7voX8dvwetWznQkBlS26%2FhGJKKm%2FxqmKpGSfuc7gGzUeBycVVQf0BywbtpEg4tGrsKUl90tRhZOiL9EQw%2FhaaWEyAmyeV1jReZgVgzBkZpfpC%2FYxtAUPKuRtQbvEzOGro52F0LU0I4lry%2B1%2FAc9pz8XrhriP%2Fy7uV1VeRM0EyQGkTdsEzLQiI3v6onRNtJ1yw%2FOp5AA45oHqwtgtrmKuPRS4IjWp7GWmncWZAtpqw%2BDSSe8c6QXv3TIO94CxKJzTwfMAPccVsHEbLzJlorj6Frp4nJqa4ZbHsnxAQTZs2%2FFhZgd9G9Ok0TCQ9em8BjqkAfqoCKivrPZwfoDnX9RBDV4uXYlgewiy%2FuJDuSDymU0d4ErqtN9zeDBouIGs3ghJFodt9rmKlCSJFzW6CuDKUd%2BQJB0OFT2yd%2B16nsOR8IRuQdWD%2BGsfm%2BFyxPJ%2Bxc8N7ldmCoW4FtlUlG64Ft3ocWJ1gRNWJsIg6xSauNRX%2B90xQ5NfBwi%2FVThJ32L750f1AEPuGejAfTSljrwkyv%2Bi5w2zmaLK&X-Amz-Signature=250943f0c28328b034021e1fdff0d2144a020ed6c2bf25e1e35555b362d0f67d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZMRHD6K%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGIef34K4wuReOTTICEnP3hqeuOB7BOsTpYi6WR3NHpcAiAbcYesTIVszHqhJs4Z4shObQDZeqUBRt%2FGo0JlibuVTiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8okneRtXTvL%2F7T9rKtwDy1%2BAXAPMADhiHtsu28ycDs64NFqseKxY4SPQY9axMaP9s4iH6LkGXvTpYrnLYSJOXElgWa%2FygYWv0thE5ijp81IXny7yhF5zC3t1vfB8KWB9pSm9Quw%2FzXIcHnCpPN%2FTBpOYFX5W9lgh0dMFn30Psz4ogTgClIr4NmMDnBEp467EAx7ixBAUajlhpe5toL23T9erR1ioB6ueJp2yF%2FMF%2ByedXMK7TI%2FJL7Ai4zhtSmckt1nAZYvteALBLhYLEyvbBCqZPiYcuML9tbcv2AmFKZ0kBa1dLxD4YH2VCEtHZR5JdXzBwMtBzyl4jeb8A0kKydOltJ3CgeYJIeVHq%2Bj2YkOsXSx3r2orXj4ci3GpDEQxjRY8k%2F2NjL2ltejSsnhU3uWBerd25iGRqyUL3aJm6QG9UtR7AN9EzmSjlUc%2BhhBoyVVE54iG27%2F%2FAOnnp3OOaeauSEkOamPFePiflmEDKDW%2B252Bdvzu2rfqO30Ycy4XwcnZpuKelloanJQfQc4jXOSyRoNW7ml7KbcATPqGg5FutDFH6oB%2FiPfuKgM94wlMX2nwLZLygth%2BedzOgCOq2qE5EqseyfGQK%2F4ZFo27BS%2FeLVKswFhtXWnH0w%2BNKpvOXTx%2FbBb8uV5PpFcw%2BPTpvAY6pgHNcIZFe9SMFBkzieDzN6HM0hHBldnjcOltNlG1Bbpg9ssKKoRcvfQX9Umv%2FMTdC7n87fN5%2B7H3aoSoSQMFvkY%2BEhI5e5xN1bJz6oqkCapjnj7fjBnrp7ayFh6DZXGQpV1sLqih5sOMwajkD2F4BHpOpTHr8DycVxTjTemjS4cakLJQYBA9EeRcbKGqDIjRL8Chmy0w%2FNKUyV2zaRXLZuCcrudGwDe4&X-Amz-Signature=beace165f7ad714b2e8d55069e528e84d960dd5e3fc9adaf1f02138b6aef7444&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643QSPKOA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGepgVtB2NgQDARQewsDHIS8PffeTlAw%2BYAAylu7WClpAiAr0DsM9gXBMdIt3dp8pV4s7ENZyOgNkj3kz3FOUIxcbCqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlJ%2BsUc4pVz7hD8J%2BKtwDNIx5EDXbmF%2F%2BpQLhFBIT04iMcgcFojWO4EhxOO9%2FyZIM2FT1FREJBHx%2Fug25AOg6PRLx%2FJn8ydMU8af9ygIXl6Q94NpLPu9KdUocMnnPAbRneU3qRxJra0gHnBjbHk0rw0spoChwB18Hy9gWcGyyqo1PtP08IUHPhx4s27T0n45gbm5Yi5%2FlKn9QFy4jSATI5Ucy8UWYos3PI%2Fo08UCU0wOFaMjVQ2iaRnMRJZ5Ut%2BPaVkDpmKX8FSefhKMUY09EEZEM6HqdWijf%2Bt%2F%2FT5Hsg46epmEPdtoclNbyakJ0aVETV3YEUQHQFEsyqE%2B8Uge5pRw%2FNC7h%2BQjWMiQfyDiuY%2Fr5%2FjSnC8RoJzzCkoFuk4cCf6S2Iz%2FwxZtCILIXbexw37fvV6ckxYyryV5NNZePvGKJX%2FGa2CA8oJqz%2FkITHG2fSmKVczWUnaCzoNKygevVBzgCO5RxPlEnCGPUpRhth6F95FgDXV2WdtKqy4KklyqkvIyHqt1Xnj%2FTWhim0deimyjV493AX4zM5Ls1AJDSbXs0g7zmA5QBO7A5IZsqFGBFiAEs6o4NnxfSnUkYwuz6Ieagwyn013gdIyaagGq%2B4HlayhGa0%2Fdltvm9gGbgAiZz9vWi%2BBCj3tpVxX4wwfXpvAY6pgHqRXI7cUSTFiCie6rlE45NbsSMgOXusp61DZwPkI5NxqHEVwE7kcK2%2Fr3y4iQ8I%2B330iMHKY0HrAbbZKE6fiBbavKvckc0WzGBs%2Bv8ryIm4tY9eP1rub1%2BJb%2BUgqAmeYR2A7VI3n1j4IV1OM4Um3XoP0k%2F9vmbu5APdjk7uZi6Wc5qaScHGmMQ36BGbdM9k5dG5vlT8DxYJr7svyB6IVtGznaCAe%2FG&X-Amz-Signature=1c1045349df4db371d532af9f682c902672c68284c7e666af846fc02c88c9e2e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632QYHVUY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdiIe5L%2FcHSNLdQTLQGo8szS%2BNcM1rPQZ25hxgOl5EKgIhAJK%2F3D5UX6vzFLBNgphYJn%2BHHWpj652Ut2B9Tl1AMQBxKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybkcfyiUpqZFmf%2F8Yq3ANh60t0TJpjexRboB0SAKRsucTQ7IE01PVZ7t11nwiKcZH2Vnp1%2FhJNnv%2BfqUfKZy9b1bjUNyswps8hy3VOwQdSeAqchp360dcJqTumS2WXKONZ1hQQ9XnjTAJ2UOwgXO%2FwtOpYfK8K2L%2Fc9fl7rh9QPxI8jvIEzaMkW2HkMpv02qXg8C000pfdoqTFZ5jq2q3RsKQdFiXZqSF2kGEVHGU60Ulx96GDfCArGwaKzXh1p%2FUW0i29rRXA%2FM32VE%2BuO3jKZC68Mnf5ItiXXKueXYJKJLwJbJKwLfQkHyHVAdeUiWkC8rw%2FWJSQxcMOz49U6daDgnGnsRKZ0uSgIklsuDdLzEZCm0pJAO9DFQL3jDczDjNCspNUKCqybX%2BQRQmt0NZF98KEOH2IGOlOHVOWJHem5lHON2RXIux3Im55JXpPDEdHM4KzywnR%2Fibli6Qk30J%2FWeXLsSEA2j794DKFz2guc4dCmw4wXLWSKA3%2BRjN7Y9WLk6Pyfvb1iAaNj7KGFvNd%2FYwXjlJP7ns1PhkZoASmKMkPZDxx0b4gsA7g927sRY5w96A3eug8aMqcyTgFAjSjpedDC6XnzojewXsBDwHvEbiwUrTS36GMrR%2BOPynINt4ZeK%2Byzgzaog66PjCr9em8BjqkAa%2B0Fpp7ULUB05%2Fpwz2WcRpSczTnacYvapsebWQ8LypkaSd%2BYMYwjVBIKsHMFhMdztfMco8ugOZayO%2BkqlmbUewQP%2FxmdIAK9gL5FCOqs0wH9z8J1kdXKcwZfK4F0o4hHGIrEkLguNpSehNl51VulPKnWMDfduu5iwNWahsM8UMLGJJAz4rRebkpDxj9qKDwRuY7KijE31XvemI5BSp1lW11wFt0&X-Amz-Signature=07006c560581df16d6b859f63e0b5e7d437243864b5dc44d458af4d8acbf22f6&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BKQBUCN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDyMDneEO1hDyq81HNJNSfe6XjusvGye2L5cCZZxhOEWAiB2u9HF%2FksYrpG9Skm6fYx7rFcT4XnaesqsoIkDtX9piSqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMevMpg3Et55TCuNuIKtwDZjNbWLwqtiwYch7QI1cSOjgEOLzBiED%2By4lLIVePg7gDO8Af90sKCDFka%2BRfcu8ZPNy0jJmEfJzKAAoC4%2FKG2XH08jVkWJkANDELkIUPv3LmtNKR9T898WczbX2mIrI5%2FkMixXeFEz3ErmKWrkeF048YjSmqYMmGNH%2Fhpx85qjoYZlZUw30BzMTNE3ISR2%2BGrb%2BTjiU01ptX4EiPZzFwPZZBvxS2JUVD37XBmZWQ3Mm92sib8QnN5N1CSCnb2j2gC5BqpYqd2NVLphicOg1hXxwHqVJB0vQdKpDy%2FeqopcSvNk2LeCZaN6TZZ5VpsJBH8NzZyhgtYnidzLyUTdKviUZiqQzWTO%2FerNVEc06AMwCEc%2B32%2Bj2LRPC3zPd78VWXbn%2F2o2XlMxn8Apq3aPB%2FviAhAeW6XlUF2G9FjZ9psuN8R5KmINfGiuZws9I9Ih6q8fKtGKHqETRnRCIm5h6z3wmGgBgscxTXgC%2FxjY4%2B5lb80TtZCCUZrFvZ0PQUkCzDk8qP%2FIDBP4Vc0n3bnAZq14yiHHkreugRQ2qJBXuvTQflUjI98dGTAC%2FRQl6I3UNeGPn1TpNDw7VFG7zRfJ5HzOIb6N9CX6b9lsktskGidTGlxcpljrxDGg%2FljB4wmvXpvAY6pgFGMo2iD1d02ljEl8%2BzROXZFOsyu%2FStqMahbx4GxUmVJrZ9Dti1fB4G82r43F04LU5l3Bbyn2YONMPF5ht0Hbfc1UZ%2BvXqH6vsEAzD1wJWg5r8s2fTKNAgSKBRu7HnfvCLYs27OVOMKIWqjkG34QUHMJmCOmtc1Xke3pahcavJRctJIPowiJVFTO27%2F5SSZPOfac7op14zJoh6VZCX7%2BNt8PQUixbSu&X-Amz-Signature=0994d80094363fbae330ce59077eb41af550a8ec7f8063414ef2126a0de9d57a&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRK3G5ZI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDUUL5YJ1XIOt2GHIrO%2Fv5bcSSHzZ0tLtSJ5cL6nr0WAIhAN8FbI6571bywWycEKfG0AFB80uDXE2dkVpZu%2Fu29c7fKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzDwCJdhwSFrvK74cYq3ANKDkbZIuz4sB6lkh9unYWcXWJtCvSGIncAA%2FUIkZHwIeX67RTvecwRRpNm5OTAegR30i5IBRcj38lUgS7%2Ff%2FyjoUnHogbirAE%2B0byePpVmXmpmv%2FhIzerNU9kwGwC005gcPrjwJ24h1XCw1obTyzOguHUunPpYcye9Gue9wH8SPXFlKaiWL2juwWhBA0k0wmaHkKA%2BWm5VIYbIdhgD062wo5%2FxMxlTsrNsCvaF22W7g7vgG5nLVMur%2Fz2sREaOpzjJssN8doQFcQJqwC%2B1HUpUwLasx1YKFdipOXV69dpl8wGOFalbvTmTzXLrFrs0CbrIEG7ByWljhM%2FcIeNYf0UZZc1YRLYFztPxqHSPlkOYteJsr02gzFN%2Fj7JOUDSyDdFO4URybuW%2FbbDc6wBCqNJBYqeUnyHpyuXHR%2BLWHWdUCiMZjPmMo8M58aiXEuREYTTAbqbf6A2nkO%2BFiumBnIX6HDmXyCAuoUoULfDm1f5EquafxxFFtTERoYsh7cVbj0EU7chGw%2FJqYxbtOOWwlA1dKUefV%2Fry5PeDAjiHrTCkHTaV61r1MxuLq%2FY6c9TJdfYwGWOy%2BgdH7M5y6EBPfsml8HZwSpAPS06ERGZY%2FIXIM9ASBtbOqhto%2FJyb8zCK9em8BjqkAapCklsm8%2Bxt%2B0cNKlbLpUxT93TZgR9SGe4AcyxmzExJTFC3f2AXPPCOXzM9%2B2k%2FKSPv%2F7wnEYI1OHWTgE%2FXsSAQCkJTUBW0qaffqEgKfdGBxH7CXTggxiJtSLDlZ6E1XNyTTUhYvhItIEhDQdjHa4uONpGFaEXt%2Fzxwo4WHmWQPA89%2F8U6uVTG%2FOKjkvesWx%2FpIVVYdB20nUh2KymAy8unQIL2p&X-Amz-Signature=92d43df5805c2260404b3f52230827f2b3b1969523c5a2121f0be467566f3237&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643QSPKOA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGepgVtB2NgQDARQewsDHIS8PffeTlAw%2BYAAylu7WClpAiAr0DsM9gXBMdIt3dp8pV4s7ENZyOgNkj3kz3FOUIxcbCqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlJ%2BsUc4pVz7hD8J%2BKtwDNIx5EDXbmF%2F%2BpQLhFBIT04iMcgcFojWO4EhxOO9%2FyZIM2FT1FREJBHx%2Fug25AOg6PRLx%2FJn8ydMU8af9ygIXl6Q94NpLPu9KdUocMnnPAbRneU3qRxJra0gHnBjbHk0rw0spoChwB18Hy9gWcGyyqo1PtP08IUHPhx4s27T0n45gbm5Yi5%2FlKn9QFy4jSATI5Ucy8UWYos3PI%2Fo08UCU0wOFaMjVQ2iaRnMRJZ5Ut%2BPaVkDpmKX8FSefhKMUY09EEZEM6HqdWijf%2Bt%2F%2FT5Hsg46epmEPdtoclNbyakJ0aVETV3YEUQHQFEsyqE%2B8Uge5pRw%2FNC7h%2BQjWMiQfyDiuY%2Fr5%2FjSnC8RoJzzCkoFuk4cCf6S2Iz%2FwxZtCILIXbexw37fvV6ckxYyryV5NNZePvGKJX%2FGa2CA8oJqz%2FkITHG2fSmKVczWUnaCzoNKygevVBzgCO5RxPlEnCGPUpRhth6F95FgDXV2WdtKqy4KklyqkvIyHqt1Xnj%2FTWhim0deimyjV493AX4zM5Ls1AJDSbXs0g7zmA5QBO7A5IZsqFGBFiAEs6o4NnxfSnUkYwuz6Ieagwyn013gdIyaagGq%2B4HlayhGa0%2Fdltvm9gGbgAiZz9vWi%2BBCj3tpVxX4wwfXpvAY6pgHqRXI7cUSTFiCie6rlE45NbsSMgOXusp61DZwPkI5NxqHEVwE7kcK2%2Fr3y4iQ8I%2B330iMHKY0HrAbbZKE6fiBbavKvckc0WzGBs%2Bv8ryIm4tY9eP1rub1%2BJb%2BUgqAmeYR2A7VI3n1j4IV1OM4Um3XoP0k%2F9vmbu5APdjk7uZi6Wc5qaScHGmMQ36BGbdM9k5dG5vlT8DxYJr7svyB6IVtGznaCAe%2FG&X-Amz-Signature=e4d0e37862c469b88bbd3ddb448cfe8867252e90c175274851f21da80f0ada17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJVAUCPH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAwCkM6g52%2Fx%2FBjXP1dghojkQWIN7LVPWcvGhnu%2F0ABQIhAMKeqNEZeabbSQDjpfznipFSueA%2BaZ5pEOeCYGTmY%2FkqKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx2waZIHLGJfZNZHIYq3AOI56oZLSpRYzkzKG6QR2DDRngI0sLqdS9cOUYmyAHg8XwpUYbIt5Nd%2BN9pKZTwqPrp8C003cCKj%2B7a6jeYyXWJ7sTRguE%2BLF5upS66EEa4Z90sloGskttoxAjMRklJWOKrXz502OCf0RKGz7T0nJRphdDLNg6aX1L057pW1nr3kWBAeZhGo7KalCuunkRc34fPD0Y3udNgN%2B%2BWTeSV1LTxXgKhNB%2BHVjjs8AvE%2Bx8ih9oS1GYQgrwi6vE86PKMDFslUURXNQzZWQimMLx%2BSBLeD8jbIP0bNyv9zu55t2NOpPEWuqVGMIrz4SaPe36YxzhSyV9%2FVjTcxqPS0ReMv8ZKTyOJVqEO0zka1Qr7YwDvezP4okgWufeJ3K%2F5ikf3ZpFlLQ6eocidboLKL7%2F%2B0cW2yZfzhIuljbJbeT27zS9P9PIuqmAjtEJnN6rXJ1UmesSHWlg4OXoI9wPjFIv7dEfivazS%2FJuWmXGqlpB6C1%2FOFFM03klT2zyG4FG5r%2BwF%2ByBtKflBAwpeVMzItxtOSTQ8NPXXcjgbOnK%2BolfpSODD8N8QcRiGiFu3g%2FAT14otKN4ubn45XrIwHtUNzoxi%2FgVcy5YJTv0Vw3deVeIzts458dPnjK8eLqgYUdmTsjDA9em8BjqkAU3BsZ5gRaowQAjoZ2C5q79GQSL83nvNjBlNu5%2FvMlZMHhxoi0ohcUBGN%2BeU416SKbcFtE9T3FRyyXRgXzBY9AlXCAbUn1oov3YCnsh44wAu0ul39f6QsEA1vdT4Da7iHnry9E3n11htBpUhktTIUG%2B%2FitM%2B4qZEVBJWXAzrkgyyadVYyg3VlR6wn3OfDlJInN0JK6nui8r9lOEVxdtnnNlXgrw6&X-Amz-Signature=3c9520457c372e2c1b821e42a5782cce149f11c98b675deab96be107174c59c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJVAUCPH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAwCkM6g52%2Fx%2FBjXP1dghojkQWIN7LVPWcvGhnu%2F0ABQIhAMKeqNEZeabbSQDjpfznipFSueA%2BaZ5pEOeCYGTmY%2FkqKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx2waZIHLGJfZNZHIYq3AOI56oZLSpRYzkzKG6QR2DDRngI0sLqdS9cOUYmyAHg8XwpUYbIt5Nd%2BN9pKZTwqPrp8C003cCKj%2B7a6jeYyXWJ7sTRguE%2BLF5upS66EEa4Z90sloGskttoxAjMRklJWOKrXz502OCf0RKGz7T0nJRphdDLNg6aX1L057pW1nr3kWBAeZhGo7KalCuunkRc34fPD0Y3udNgN%2B%2BWTeSV1LTxXgKhNB%2BHVjjs8AvE%2Bx8ih9oS1GYQgrwi6vE86PKMDFslUURXNQzZWQimMLx%2BSBLeD8jbIP0bNyv9zu55t2NOpPEWuqVGMIrz4SaPe36YxzhSyV9%2FVjTcxqPS0ReMv8ZKTyOJVqEO0zka1Qr7YwDvezP4okgWufeJ3K%2F5ikf3ZpFlLQ6eocidboLKL7%2F%2B0cW2yZfzhIuljbJbeT27zS9P9PIuqmAjtEJnN6rXJ1UmesSHWlg4OXoI9wPjFIv7dEfivazS%2FJuWmXGqlpB6C1%2FOFFM03klT2zyG4FG5r%2BwF%2ByBtKflBAwpeVMzItxtOSTQ8NPXXcjgbOnK%2BolfpSODD8N8QcRiGiFu3g%2FAT14otKN4ubn45XrIwHtUNzoxi%2FgVcy5YJTv0Vw3deVeIzts458dPnjK8eLqgYUdmTsjDA9em8BjqkAU3BsZ5gRaowQAjoZ2C5q79GQSL83nvNjBlNu5%2FvMlZMHhxoi0ohcUBGN%2BeU416SKbcFtE9T3FRyyXRgXzBY9AlXCAbUn1oov3YCnsh44wAu0ul39f6QsEA1vdT4Da7iHnry9E3n11htBpUhktTIUG%2B%2FitM%2B4qZEVBJWXAzrkgyyadVYyg3VlR6wn3OfDlJInN0JK6nui8r9lOEVxdtnnNlXgrw6&X-Amz-Signature=941747b2e49a8d82cfa191f4fee23fc69f7b483f4f01f854920c9bf3f01956fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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