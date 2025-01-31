

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMMACR4D%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKa8ncrT9fIcOy3MSdZL08ewO8Ya42BiUo2f3dSs20JgIgQSveX%2Fkuslm403hB8bsWWJMmECtokF9ZaXGqiHaKrOkqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2F4qqeOGOMAYCpbPyrcA%2BXEoHoBB2J3WhsDGjBCC1wzQVsh9SbF187uHB7%2Fx3ogc3JGDjUCYKkmMrtuoBSY72FeYNdgj%2FlDC88z%2Be301LdFN2ePBLglKU63Yq6%2F6SKFz6A6kt%2Frof90w80VJN204SA0DlOsKusmzdSlcTuQLZhApZtZtIXlEizUvqwyh5l3UWw2h04ijxOrza3Jeth6jR%2Blhu9TcwVwpqKk1j2ab7S%2BborWoMMe8%2FTcmoS%2BxohvoNZQ1Lh4IsXbU3DSyXYfYNKlAvEnoO%2B71ZFDgqLerHrgHyjiE5wDmqtvbgrGerhBAMN3xMeOj2n1yt5OV7Z21yx3hiqN9wRxzBQpONl2QBuRH2fv6cTMHlBwsWC82RaHQ0gXX7Em1krT3KBCmzusT62INSWUhZmTc7I501DjRREMLrhrA4cgIDqETGYeLcD4t5FVzswBeIlc4EIQAGaO0mk2%2Bm4spkvM1ounBVZLW8NytNqoI45yzluqoBW849K0t9jXPqgOwRg%2FpgRInQpghowrXhUx6Ss0eGaqNXyp609socDaS69LkZUbL1G9JO0z4Y5B0ycvPqtClDZOYlDEloAeCAWhw5nDqufdPW5gemf4WcoVR%2FyDCI9HtruDXI6MNgl7BcIGxQ9l7YSWMKq18LwGOqUBLV2c3EYQRtY%2F2kmehNscMRgEgMvi1BFpYlTHRWKiXG8vTgwRJVqEbQYge3fQT%2FLxcTPCE8RvpjccFhItTv7A1POGj2aUbxrySNaQENLh9s8KDR9W1AZpZg62XRQu9TOpR6Zhk0GKMzPmg9zREWKARGCl%2BVP5S%2Fy54ohgjo%2BeYEoaBNKlY3M7C%2FRZ4iAQeLlKUrW8q1eF%2FyJlv0Z4tdjR0JS0byrd&X-Amz-Signature=28b5682da693481213946c90e888a3ea2914d0212aa7ba792c9897ea97fa5ca0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFD36EW3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH%2BjbKNaCHm%2B7mBy6imPr88rqnuza5c8mpVED4rRnpVpAiEA8LzqabqNlhBzgGQXMxrgtVh70JTMxKJfh8r7EnLhZjAqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNg1wJHewyDuxq5XuSrcA3%2BJA8VUVHyWKt9TDADbnBrUDsLv6ghMe9uR5XkUl4T9bO5Hy9UTiOXT%2FBcg8v7Sx1vpyFbBuCNVMhVApWkwbQj2m3icKbvE1uJsPOQsge51hN%2BaZv6QqcCWlchd76eW612s9g1XYrTVUn2wwVM3MY%2FquW2IpQzrAqV8OLGCrBE2NfavySvcgAVjfUvQ30QKvjz2OKhhjRsXfbg7Uq%2BpRAvRB264X8HL9i2ucZfqi1yVHi%2BjZfajSp1OVXkyOgdEbE05yU%2F5Pp5H7ip5dUdWBYsAj1rVLXt2jlSmKQamjhWot%2F1wyWLStHV0mv0kAuFyZlqFRmmvs5FVR0C2GnDnGxZXOjKcZgZeuPCJS90fTNptAoLf1J4qBRjq1UbX59pc3iEIf3%2FlEPBVGr6%2Bwei%2FONr%2F7Z99xhYGX38IFnUNgoq%2Be%2BPcJqRh87NfDFvFejjlTffMwSFPrYEH11a1KQSpqzZheJepZq26RznJ2yOvcfNKI7BJFPdMI7ytsRBg4jCtgGiEL0BfAgp5vDeZKhdZFtlvbt%2FlklRiDAGqXtTBfj6BwznQMTqQzDoHAYiIHLCwnoT0%2F8Mk4kOfihVl%2B%2B1uezdLqwD4lGBAFoSVk9S9VFCJhwcC5ugWp7LtdfSjMKO18LwGOqUBeAaoMARhmOOU2LXypB%2FBaYftycQRotmhYEJofsjpm9FjRabOwA45Az5QrYoH8%2BxuoX2FP8lvYefP5qe3NhXrkEcw8rLo52ok0G3aYYVyDJgeJr%2BK81TppwkXAeYBFsdIMrJnHnfysb0XIgqntq9caDCswv9dH6LkS0yKcQ0Hc1zwFJQnCiYDWb%2B6fzO2l18eF7IP78OSXGmkW8ikSRQt442LL2ym&X-Amz-Signature=ecc206ac6053aae04a4c3dc13c41b41dc2f1d8425c4888af35448e84460f5197&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJSTMZGD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtSWjHSHrlBHR92G1M0vABsfRejh1gz4rh1s4TAYtV5AIhAJA8dlWKp11%2Fj0%2FKk6hX%2F5fVEs0LPLHqV0w2k%2BN6%2FbaGKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbcdL2Ex%2BuO3vJSUYq3ANbNKoCKdLqB0NAEJekqBX%2FsvV0PkblPcLlM15X7FXDgKexL5HinOli48m5uebLIKEm%2F92yap3ytwgZJkOOHGTJ0fMLMO4tbue4WBQNPKkWajUex8nEEgd1zBvSYA6PhRsn4%2Bx0a%2BS%2FhpJzZOxDGZQxkAstDRgXTn%2B4VCtKxMWIwaVbQkLK2Gzk5Rx2MkgiJFVV4S9nKe8SoCiRRGKM4%2Bdkmt6etNiQ4ras0QR6T3ji15tLkIQ%2B1Sbu0UBGFhS49F353NJj1iT0%2Bsy9wEy8bRPtkzmZm0%2BQRmqXlHrpimaqog5FCFD8Wc1spJorrnUjeRQ5uruRNKB0fYshA76yBt0M%2BlnC%2Ff%2FapBtxiwlMn0kCWdxAzcWbi3wa1fK5CMFPF5nWFLhq2%2F3R2XPcAB5GDsAmsZ3Wno8IzLokMqV6AZm2hf219H2QI790rZGS1M0G85SB5V2PPGtX8bcwD5%2FxDjYleu0nGdl3K4Z6R5g%2Fthi8OUHIM%2BUyXkKTaaLyNnE50vhvZJ4Zh11trMkvX65HvQMsc%2BUp%2BZ6X5%2FtA0uvQuUYJ7H4XNQ7zkDgFJUf21kQa%2BhxotIEHOV2g1w8CQJaFtDAPmNApApvZj99FUpm5hCqYCw%2BLGt%2B0B6XIMqVUTTCItfC8BjqkAdk3v3NsWgbpds1mL2CPAf7rXC2GHWw6X6l5CFbNjQEXu9OCazvdirFY8Fr90jlQK5tHpQWEX3M9UtWI5iTnZ%2BhL5lBcOXTumhfxxDFUL1zCDaqIVq5yPoaj0d3j5ovyvur0nMrBzcs%2FM6E6zhB5zDNodEBAWUh2PeWjs0ypkzcrAvL862F54YCmgISybW%2FxvGnQq0yVzdASgCQ%2F9M942Grslsxs&X-Amz-Signature=166c01872a0dcd19d31088d243631b77a8dc0262757bf59fca8256a35261567d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJOL6A3O%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2rZ%2F15pJTkL0H4tPI6CwY%2BFm6irJqUh9YcWlu%2FeM4ZgIhANnLTc4lTvdj0uiQDWFXlsjkUgwEJsTnvjz%2BvepWiT3KKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwI7NQZs%2FhALlWKtgQq3APobeBNiLkccYyv7k0QtLLDuslYH6J8NavZTFCYULqp0RdbCd7VbrOxTSP%2BC5cejF3xsZJCpMHwUqtD%2FktnmzJ8OXsBmV9MNqLu1fc1qHhUmWDp%2BwjevV0iSnho36BtJ%2FPLYvTu%2BzqKIrkdrH4MuRyBBkygqCVmemYzAhYVNaMqVExLbVf17UGIKLFsrJy0GPoNelzangIjZA8En%2FNpPCwvhM9Y19w9HUdgvPxDSjgCDaL%2F%2BAJ%2B%2B8CY13CruBbXSqnz%2F05YQWXX5s1GUABPrmiGJviwxCYEmV7xjAW4j3p6Cl2%2FhuLxI7T34dHKvNmzr%2BVXvNYk%2FsM8Sz68CVAvtHG7%2B9hcppgVd0jjqLdtEkbVPdvfT1AKnlJlRXr%2Fo81Q327FCXAUSbVnu9zo9ebQ3CUlYkquxTtEo4%2FavLedh03fWmnsrOyKtRB8OQF19pRO9rLWzoAggl2drs5CiRdFUzqhXpuQglX9B9SRLOYgq6ma22TigdZ9AVJ70RBdgbYbkx9DUhdRO%2BiDIOaTGtIjern3B0amksYFmHtbV1ocoIVJZKmCUpNinkPw9fZZx2TPatCt8WTmw7pgv4oKcUTx3KP%2BC3KkItFD%2FgI4leUCjJ4ifmWJzqHVQJ681xgitTDVtPC8BjqkAcecVROgM4nxVLsPXMwahhRuYyeiA4QhCRt2hSjwZz6oxsm855UkQNy9kF5Sakk%2F82JSHTnLiqM2HX5DGCeLo5P7jjMTnUZgI7TW9toiVv5eSuL3slIBQv6HwnljdBkxp1ky3lqVPRkk1w%2F0xDKmCgQ9EGgOgErcA2C%2BC1ZMu%2BDRi%2BWb0grUv1mPvChxMlBsfny1QsR%2FhKi0vxyJivG6DJ%2FSFMem&X-Amz-Signature=89df8e9c9e29ae3946b97cbb2c1556cc79b42faf56ce6e2a26fc951f053d503f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIZGA7UL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDy0yH6M67bLmLkb0Y1B1GbGKZA%2FDOqBZ0dVsQduDsRhgIhAPecMW1U0S1zdEPBQ4zpOukt%2Bl36yEGTYyXPN8S%2B2IFSKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzP0Gb96Q3SMgoh7Joq3ANNlOMoQVzIaRXwiXz9F5OinVDZMq5LOtk6aLUGGzEp522XnaQL5joyLvx065WluHNp1B9BuT5YyUOpwHMmZUROO5Cz2f2VUjQmbfSzp9k%2B%2FmTzCTXkyCmYBAaVzzlz4P1YUGAglAK4mngou52Qg%2BpuR1D6AjW2DiKORW%2FP98P%2FNe8g6iR%2BFaKDVzmy6mSkouK5c9tQ%2FFgO8NWbd3YVIq3fwYz0W95%2B4E52FlALPnUD74CDdXb6xlROvxs04HphQcRhd4BuPcUjEzmIiIXdvsmC0gBelNrSES8nwv4TrZQAArTritNHyqHV5ERHG6QPbb4ST4T6AYeKtULVGFoizLu%2BfB%2BN2LhG3GvMgSU04892MwrmvSCX8Fs2EPIkSBJBbo%2BFSr65lF1Oj6upmZldZGGEx0yGOaOoSVSs8IoxW%2BVWrfgMy9sYL6Qyw18eZJN5Xzli0YpeqXSSvy3BnzW%2F%2B1ZrjjZefkLdytJ6jEA0%2BRnas5iiHetlAZyFG692LNh38LcyoDw4TXORVeWHWo9IgkyPeahGufH9CGd3v9XIelD%2BOl1vI7k7kdiPh673U6yZwDZxTfiG8nW10VcsmGZnScgi92ISOT%2FaYX1Mionl2%2B0mqxX5%2FdXCXWwj0j%2BvFTDhtPC8BjqkATJNuOnyxtv7oOZnyXTFCS6rHFCH2vVbknN%2BHTROG2VlnMDs%2FTNEl%2BjLyD1ItJI6%2FGaiTcOfTpq%2FipXczB8OuMQTN%2FsAIGs%2FwPUH1TPjzLrCBqgva1bMWoX9kzU2ZFdclAS4Twn5WSY6tjWIXCU9%2Fi6WXFiwG4twNitY5qjpUi30NuJ60OFZ9OLXLF5NU0YcE4yJcb9nTLVyQIKA9TaXoz82VaN6&X-Amz-Signature=95aef52b38420ddda53df7be4703de3f41644e66a0bc41b07611ba4ee854cf80&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIGGGXED%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCH3s2RcN5M%2FG3Q%2FNQL6PWAJZqBzMeR0QJwuXKQg9hsz8CIQD3ekY8IwAgnQVudiQvmDuakKbzKYfjRLWLRukmcuHfOCqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvWrYJZv75CKgE2PtKtwDap9ZIQxAwxG8zY3JFZISHp0J44HQvMBgNgC6iGwgQPLIcMANS8ICB9r2aDuJ7vwng1HdTvJoVGBssK4muUYb5xCz7lycPtNFP2Oin2z0SfM6NeqiWgJhaAI%2FnUHGA4HCpz3nyxpZQ%2FPgaKGdxPmnfYWNnjf8TDk%2FUFe0zoB5FHl58k9VSNXRepIAR4wpUJEAyxtudayfaOBY8EfJPonyBlC3N%2BRmer0RHidHCl2Hi72ICzltORR1fsWKzr3d4g0pWSZKkpt4idjc4e7ws7vzl9Fz%2F7J8HFMouSzh1wgX%2FuL8ribVBJ6BxkoVZksx%2F3lK2%2FZCClzi4zRtfuS6SCDJywI18xuY%2FP15%2FWHfilC2DZLzdGBsQH%2F2e18w%2BKQ5QTji4u2867ADMDVCgAEa2QPQDXttqwD16zB9QKc0GJ83XhGn5BU6MveuvOPAKWBvwPdZ9IDr0HByil8aR2Yo18wonS1JtaswL37SXzDTXWdWnV4Gx0yiV735U26N5w7IFoXL2poBtQ3GEVY8ORr2F9hUiHoNNkRJvLn%2FVVyIFshXZrr8mVMuVg8HV1zM%2F0sL36c%2BwcnfsuhywSD0cS836w5oCQ1Tugq6vexHxkk0YpevMxIID%2BzTF%2B%2FFZjkfrhgwobXwvAY6pgG075SrzMdD8TkmPml65gxZSoTaFk9VCmBtmdZ77hs%2FhDGyH2dVZTqt3%2BsiF2eI41VY8LA31xdS6EfzOWRVjvQfi5TBglcR0NUqQcqyxNPBpKFEHQ0cVEJ3OFvzGF2yVoAAALuKgqDcG%2BH1cuhuHTdwNqMAn6pux1B3taJn0COwhbC1BP2N7OLWIn3y3wS9MWhJ2XP%2B7cAyCDwZprDAd2rYvv1e%2B7As&X-Amz-Signature=cecc763c237608f63e7f2ed88f6f76f6b85e91e854f13c630d1cc29eb2caca6c&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX25TQQF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrf81TXqfXRpU7d0aE2KTmaT6oiR9evjwBizwpJLOyVwIhAMueaEXspM1hcMcV7%2FoE0GeO9%2BAxE3%2FHAHl0S%2FneNIyyKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfIAO5glXO%2BRDNvkAq3AO4LNyrOLQ%2Fc2VlgHpsLZ05CePOMpfjCUl1pijQaR%2FXGX%2BOC9UlTJrXILJXWV9757z6fLlKx913KJKCnT4bDDobj2CGyhfJM7n%2Fv2IAQ1YsoqQ9PA%2BN3Jl0yQzjUNAFiPM4wOpkwFjsB9x%2BFBlYeyK5PR0h%2BiuGsb%2BIPetdXvPwgW%2FWV6Mb1zGmTEOK9eGIifGsDOywLxIk8KUCGMAuhyWwWKn3TEtm2sDDOujWybPS%2FK3MJLvx%2FJzWCe6xUIekHHd5EiF5JSDhifKWalFWbVKyfROPdaFugNH9PolEtBeDPV3LO20abkCDsRThDGzmIdYLfM%2FYkypj7sFT4PoHJw2CiMOqXZwzkW1G2kRDfs%2BGFaMX0blpy%2FkB4%2FRztbeWwansfijpdotI58vG5dxceSjUSC7aQCREdgyQE6KzjucPTb%2F5qPt%2B5Jo3zJgVODXWDvaRKs%2BKAs%2F85shewifs8i5w4PjxgICOSMFt9qwNcwV%2Ft5czzcy48HzwqJ9vpt15vF1JitkSWdLWULrvyt4uOPJS9iZszxOpblOJ%2BY%2Bj92ksK6QqHW%2FoUtzWtw2489a%2FpJ9wR3Eo3xInrQbbtlKKU1cGdRLbl1d%2Fl%2FlGgzE5qsrmy0niVG0y74tJRp7iZzDptPC8BjqkAU%2BJYhpucZlOTvqGvHUc5ChsI0%2BMJnffn9AmFuaq4YumIOsbj8CRwRmpS5TxNKzQDGq3GE4XO82kStXbl1XkVH5J7zXWq2LSOh10vputmcw5FWUzwFFHZnCeUWkc%2Fv0g%2B9DNLltmiZ0k1yv%2FuPe2TqpjiSxeBcsc%2BDpdT0NlloyWATiZCtvzswPmBWqK0tevWJ1hlemRaBgcdtMJwgjF5pjNSD3R&X-Amz-Signature=e9117a9e949496fc9c969299f8201a357eae7c84f3e312f2346206fb01179232&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYP4GFG5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZXUdIxJis6adJjHt7HqWRs2CoOv5k8ZGrerXd%2FjSJYwIhAPMDGA1f676VdHbdHGU7R2rAPcNKltgwgOq2%2B%2FoL86DHKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzaafaAbWgg1iHlj0gq3AM6000Ej%2Fzh%2BhJOX7NOx3Y59U0%2FmYtbyfTGPRrnSdGiycusNdNyxbqg0bgAbeOnCvwdx1mb75lMqQtiwcGH1DF0vqpXZCnZZRImHHvSt5XSrMtrzrbrME%2FlKNMI8n2HwMxt7Z34Sj%2B%2FrFUAI3grsyDEhnUchekUyf2hIjPoN3RGQt61o2FGgHcFJdl1A6M4ebymQkMByMqRosAEVlCSv4NWXMwdBDnbNmIb2JYIp9ohL3AkYajBvONmt%2FobWs9zgiEXctJRLwfzfLwtGHq58gtg2g%2FQHwA61hXR1NUYinOoYkOeagu67WZuLdB9x%2Bw4dnbhrBnj8SwR5FDiX%2FBeLbDxiZEpyMfS1jM4g9hWGrbJfjt28XZsFZdOkar2vKADuiToOssn4iM3nVQ0Th1lG0DjXCAJdhTU3TfY2nuRPa7FxJ%2B5D%2FPwqtc7oewasgfa33oDttLrYtHio9kEtECtqzEtZkeDOuXn7mWHRvNpYwyNoviC4rR23ZeSeWpSoJ%2BMl0HLr6xvMicg2trofToKYbnQh8ccpP6%2FjHL7birZhRG%2FfNtUiGj%2Fl%2BjP9UuJKLDLR1vRW746q98soWFVo3Sp262XtWWZpYGSNlYZf3Na1EoArY1tk%2BS1H0zpbPuvnDCrtfC8BjqkASnT8Q8Y0Ta%2F%2FyCXgzuOT1FdcIdQ5B3eNSlcemWmTcHqytoLEL0P%2B7Wro2QHLQCnpY3q%2FOQTYAuZHohsXhqvSbOGLhX4OuEFaZJovf6dow5j6eD5cHmmTKkcl4IfKBDnAlK1n1Y42Svgv2mOJnWiTZ%2BINm0sxAdtGKoP5I5MKGHbyFk9GdzvEQ9FGzIsffycM4JLZVqVETfY2XxrDhQTP1GxOmsw&X-Amz-Signature=c9abcf8ce2c6abcf27039e1de5f3290622ce821884284a3fde16ab00f4b7f4c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIZGA7UL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDy0yH6M67bLmLkb0Y1B1GbGKZA%2FDOqBZ0dVsQduDsRhgIhAPecMW1U0S1zdEPBQ4zpOukt%2Bl36yEGTYyXPN8S%2B2IFSKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzP0Gb96Q3SMgoh7Joq3ANNlOMoQVzIaRXwiXz9F5OinVDZMq5LOtk6aLUGGzEp522XnaQL5joyLvx065WluHNp1B9BuT5YyUOpwHMmZUROO5Cz2f2VUjQmbfSzp9k%2B%2FmTzCTXkyCmYBAaVzzlz4P1YUGAglAK4mngou52Qg%2BpuR1D6AjW2DiKORW%2FP98P%2FNe8g6iR%2BFaKDVzmy6mSkouK5c9tQ%2FFgO8NWbd3YVIq3fwYz0W95%2B4E52FlALPnUD74CDdXb6xlROvxs04HphQcRhd4BuPcUjEzmIiIXdvsmC0gBelNrSES8nwv4TrZQAArTritNHyqHV5ERHG6QPbb4ST4T6AYeKtULVGFoizLu%2BfB%2BN2LhG3GvMgSU04892MwrmvSCX8Fs2EPIkSBJBbo%2BFSr65lF1Oj6upmZldZGGEx0yGOaOoSVSs8IoxW%2BVWrfgMy9sYL6Qyw18eZJN5Xzli0YpeqXSSvy3BnzW%2F%2B1ZrjjZefkLdytJ6jEA0%2BRnas5iiHetlAZyFG692LNh38LcyoDw4TXORVeWHWo9IgkyPeahGufH9CGd3v9XIelD%2BOl1vI7k7kdiPh673U6yZwDZxTfiG8nW10VcsmGZnScgi92ISOT%2FaYX1Mionl2%2B0mqxX5%2FdXCXWwj0j%2BvFTDhtPC8BjqkATJNuOnyxtv7oOZnyXTFCS6rHFCH2vVbknN%2BHTROG2VlnMDs%2FTNEl%2BjLyD1ItJI6%2FGaiTcOfTpq%2FipXczB8OuMQTN%2FsAIGs%2FwPUH1TPjzLrCBqgva1bMWoX9kzU2ZFdclAS4Twn5WSY6tjWIXCU9%2Fi6WXFiwG4twNitY5qjpUi30NuJ60OFZ9OLXLF5NU0YcE4yJcb9nTLVyQIKA9TaXoz82VaN6&X-Amz-Signature=28bbff64331c006524974491e94ef01dfc4984d2810a23bb92713ece02261285&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663454YPOS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFJFJZx1afXYTAmq4RWk4eqMiVB1KOwRSFOUEalt6E32AiEAxwa2D1vqRFjFPookI1EFybjdS%2FWtyA29Z%2B%2FmSb%2FxtrAqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB9N5jwuqjOv1QOOfSrcA4tse5q11BxVAELUHVSi5DQ4jKPXFXl2oY4YbBUck9BMuvbhno9H9uisMOfUHNNxNfY%2FeCtSjSpm9x2fnIA0V%2FPjKWr%2FlzzQKICduU8zNSwpueDUOqEuE9km8g%2Fd1ToDmDUPD1aTQIULHMKrJ%2FiY1Zxfxe%2FQ6QVL7tXgJoghqVnH%2BAQSjjowmiDBN9UULKR1Kai7axksrLRQZusSBQ4q6ZmnwaOJY5k%2BNpf8YbHgKZMXZDcCqBLdjqreVLl0xTIc0az5wfwI8WoopTwoEuthKIoIkhajpSGfHHr5BS8XcmpfBPEMD76yTNK1%2B3JBCiAPtkkog23ZsRBUEtxN9UBY5Wrt1WnX8hEmEGIskMz74WPxX8GK7kK8PWYgVwjuvAWbs7qp2HGs4iKgyMjjjThL32GMNWF3iWqaWx%2BNQVbzQG7%2B7O8UNNi9iRujea9v1zmtXp3ldwcqsYwaDNTgElL7raDZNafbp0R9Q9FatjLdq7j6pvbWnUflIVn1bCWn6n%2BkHJ8TSYKuJOe8nOnHHGtBqRhCZucEePdgFKTN9QGB0k9dI7O2t4wZjaeV5Yx8LA%2BQSXb4imIQ7dOnOZ8dRmugkfxMGispnYljq8lCT%2BelWP2UW%2BTyde7n43MEw5ytMNW08LwGOqUBFw0iHJtaHfJuRHGPVVBEFhOePVMEJsv8lNJ1MEiTm%2FEuOyur%2FWAzWINkZ4dX77GGoMmUf0vkWoV9MArHxgmLE9nYgBECiEFdNPkVp%2Bc36y%2BaZ1X7iMkBde%2B2rZRd1%2Ft7KF%2BcvYT7x8U846YwgBooJTFjQF5QJpupPAUDxk3gowt8R9e4ttZSv%2FEWAU%2FV5pPp%2B3T9fVuOP8vYk3siIZqXWvBEdJwn&X-Amz-Signature=027f3002f18c65b97da97619439a95636063219ddf0645f0fb37d80b6f7b2c90&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663454YPOS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFJFJZx1afXYTAmq4RWk4eqMiVB1KOwRSFOUEalt6E32AiEAxwa2D1vqRFjFPookI1EFybjdS%2FWtyA29Z%2B%2FmSb%2FxtrAqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB9N5jwuqjOv1QOOfSrcA4tse5q11BxVAELUHVSi5DQ4jKPXFXl2oY4YbBUck9BMuvbhno9H9uisMOfUHNNxNfY%2FeCtSjSpm9x2fnIA0V%2FPjKWr%2FlzzQKICduU8zNSwpueDUOqEuE9km8g%2Fd1ToDmDUPD1aTQIULHMKrJ%2FiY1Zxfxe%2FQ6QVL7tXgJoghqVnH%2BAQSjjowmiDBN9UULKR1Kai7axksrLRQZusSBQ4q6ZmnwaOJY5k%2BNpf8YbHgKZMXZDcCqBLdjqreVLl0xTIc0az5wfwI8WoopTwoEuthKIoIkhajpSGfHHr5BS8XcmpfBPEMD76yTNK1%2B3JBCiAPtkkog23ZsRBUEtxN9UBY5Wrt1WnX8hEmEGIskMz74WPxX8GK7kK8PWYgVwjuvAWbs7qp2HGs4iKgyMjjjThL32GMNWF3iWqaWx%2BNQVbzQG7%2B7O8UNNi9iRujea9v1zmtXp3ldwcqsYwaDNTgElL7raDZNafbp0R9Q9FatjLdq7j6pvbWnUflIVn1bCWn6n%2BkHJ8TSYKuJOe8nOnHHGtBqRhCZucEePdgFKTN9QGB0k9dI7O2t4wZjaeV5Yx8LA%2BQSXb4imIQ7dOnOZ8dRmugkfxMGispnYljq8lCT%2BelWP2UW%2BTyde7n43MEw5ytMNW08LwGOqUBFw0iHJtaHfJuRHGPVVBEFhOePVMEJsv8lNJ1MEiTm%2FEuOyur%2FWAzWINkZ4dX77GGoMmUf0vkWoV9MArHxgmLE9nYgBECiEFdNPkVp%2Bc36y%2BaZ1X7iMkBde%2B2rZRd1%2Ft7KF%2BcvYT7x8U846YwgBooJTFjQF5QJpupPAUDxk3gowt8R9e4ttZSv%2FEWAU%2FV5pPp%2B3T9fVuOP8vYk3siIZqXWvBEdJwn&X-Amz-Signature=b5989f0082c51cb3dc226832d8a10e17a504aeff219ef87f453a50e1d53decbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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