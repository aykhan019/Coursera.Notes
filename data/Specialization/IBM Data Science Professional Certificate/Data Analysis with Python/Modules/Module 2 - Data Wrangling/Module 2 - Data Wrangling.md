

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TLAPSKH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjM%2B59UiebU0MlX4kKCwWf0P9Ze9co2jfBxlaMkdpMhAiEAklxHmJTL83QNsHAqH3hyK1oQeMWEUvxyemgKNGp%2BLmIqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDbL%2By%2FcyAlB1zjRFircA2wp%2BXuTlKflU26rfc2hom5IWPkgL7WESXVRRB96hvSYLkA6tkDHQ9lM%2FjhkXx1e%2BUXBLaY37Ed25nf0H2bFAnQM72EbZH2gwTcQ4rxxv%2BoDOPFKULlQ0MaRcd68udiIeHudRIQzuzVUoiepbfP%2Bqpp5R3%2BehGCgpDeCFVnzSc%2BUMgHN%2Btr49DoFmTYabcU9jrRCw3U2aE7789I%2Fe4dhsQxudHzHjGweoVIZEzEyUIbz%2B2SlqGjxj63LeCZYQMqUYHXINXvuGZp5d441D4%2Fzdk9CmfdglB06D6G8NvEtcJhUWvZ5mQLTDPJIp2j0FQ7Rl9bqjPPd4%2FngTUIy4oixbRUhASH6oPw13l2%2FSY%2BL%2BsWS2mVaJy%2BjYDwOxIbW0InvisRCrDU9Cb8QNgHfdt376U3hGNk3oxVFtazux8hIAMLdhdClXYE1dlMQQS%2FqBqyan44HP3OF6KL%2Bq9rNcK5%2B7nHaGmjGln6Kq0HBdCzcmPaVQRlHwEVNsCCM0ZL2KkerLonPiL3lZE1pB1h3iAYJ6RqWY4DzJVcJviAy1Ykn8PwJgzpmQx17nYkHIjrUfIiIFO3SyOFPePoJucDBRVn52QPH1GPWfW7LMa5hSyAV9Y0F%2FCc0p%2FcmfpE0mE%2F3MK2E6bwGOqUB%2BT9Hs1T3dnFmYGKx%2FScAEgTSXBimlAUVi2epT3D3jdLwju8CYk7I9guEnoeuqG9ssp2Wbq37Db4CAWxWGer%2B2oFqP%2BEzHF3PDf26Vubg5vldETW0J7SQPIqjhP1N%2BGjZyhxkkY%2Fsemv3srxxXkTFKEIsGcMFyJIXgPrwoQu1F4i9QMuYQX2%2FGvJjTznAVREC4gMjgSzwZloYxfA9rRTYuQkj4Yd9&X-Amz-Signature=3a6f7ba56e067febbb67d46858694b699e0f9d5595779d55cd977435e6c2e034&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQZLK54L%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1yEBEvx7hoZm9cmig5cV%2Bpe2aEeduSHqGMZaLRf7NhgIhAM863zHfvmfhwMfvqx%2FPVl4Zf7fvLUQoyMhCIhi1dMfXKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTGWEN%2F7%2FdzocXlXsq3AMM3XbTGYZ2CWMd8Ff5eauqGunYkmbQxFUhHaUx3jmbfEVxRcVXtKTIzJkUaUj3hlyRluvLE7O0BCXT1J0RlDDI0SU0DReI204BmYF%2FwciOxFVMkz%2F3GlwoSZo1i6Umq2MnuxZCkxPLYZB51cvkEGblpzuFsJGAgHhBcPqcVZL%2FTckc0IZQieVaRpSxTHb9Tw70lm5nN04VCpJuEL1V2yQ%2BNDufW8GZ32gLqC0PqhZSngYWEocgeSDMxLxzQQnsnMgg%2BOHIxK%2Bso0UskAqj5xsiFBPMIuGu%2Bs1icLOcy2B3SL8cWXJpNnEvq2du%2BhIz2bWxYffYWXpIYotTFgqtL95CnJl8%2BhpaZCh42A3JTzRmABqvtppT%2FLjAkZkMCnzTbKlyUk1P86tgcA6Bs4bp9BsTkhGO64Q37xvrlePoEzGybsGpjwPImjoK5Z10vtJdAZVdZczNwoPW9CmkYmIZuphsYnO7NwqDXsIJ9phXY7%2FmUEzXJKm02yM8J%2FfqJchvXKQ2HTRQ4FbvX1WjapV2qJ5LX1I9Q6se5fooPdwYvW2ekyxL1kkoi9P47kU5P4OAtnBrPFUPwOKnJ7Dr2POYn8Z7ZaqABXTyimERmjs%2BEEwZkiBKbZvFthrdWc5isDDig%2Bm8BjqkATlPQ2ebx5W37R4qDLM9Cs7jbqcy6Ymn3qemlrTtptn%2BKqCScOket%2FR00A2aFR1w9FE89dHS2Y6ezviCXF5SBhS2roKHoTC2JTHc6dfWya5%2Bjsf4xLL%2FgL6C7OupHOF1p4TtPXjJX1XQuANDHGFPV6e1XQBomhp3TEFPfFKVJZNZSzDMC9EQGXpXAxZDGZOY1LL1VkDBIEu7b07ADoTVUKGSBqzA&X-Amz-Signature=d7a76079fafc71e08ef21b7ad31ddc8977cb441daeb5e819408ff8964d2d9f6a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TRQCSEC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSaJEsGewmoqaTg%2Fjk%2Fx94MR95Fh7Z2v8qdi79ZEtaswIgbgCEHq0KKE43Fqn5TETXk7DX5P7Lh9oj3O%2FjIzWUM%2FkqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOKw%2Bd7Y6Dll%2FByFyrcA2RnhE%2FOpwCH9BEso6JUmPXBByQCNAXPuG0uyuHkGuSTKduP2mMrujFeuHTYX33koHJ7Vc9I1bQ%2FSzHZADIwTGgpRpcYLWmGdnAy4GHBt0%2FgFw5gCkc%2FDvW2AOEroTL%2FyE58aVcL9t%2Bw3t0hvC%2BxgcFBaiUEF46tmuvjb5ok98mwMvkmcF6%2B9kokprqbq9C%2FCOVm0tDKc7MTvIO3HH6ovnY8WNWxvEfMkD2sRhhAZ0o5kWdX7lJ4IcwS2R45EyoXSWXoGY8dY1Rv1g6TrR5tGWQ7qd5E%2FsTDS5LZe3yLxpKxb%2B33shZs3ynIu74m3At%2BxPvuswhZMmh9FhAMNgs818fPTY03Um5yGjZJfJKlkbZNuYpxndyzA0FNS%2FBs1nk9OZCr8iLMNM7ZAzXEi86deRUi03cNHneBzqZBb3U8hxC5tMd6tdEsWKPwF%2FO8A63z2OBc0rnc5l4i%2FzjEaTxJHHdIcoQmNcF60%2F8aT5%2BWdfaE6991vxuoXyFUmhjReWgX4i0IGiATrpAn7vA9wsIErxlMFcYathxlUUqooZGb767c9zmRvs90DwpVlrLDj8elS9xqnPAENOt7rFrugB5WkeKU7DALKIXK5mFjCwat2qekGScYyewi2IoqerLhMLOE6bwGOqUBPLVIxbw6yZBnPPduOvlqnunoGW5mknVN5n%2FpypSfMoovUXjRt%2F5F5vfdwCGi%2FLpR8YiDCskCnNrNkhdO3jsgpdCASOqFT4H%2Bo9NU%2FQjvZW1FijvlT%2BZw9qMVgkkUJCdYqwWzZqC8%2FSEMOStmrF%2Bknf9Wp%2BHoh4Gn19m9UjNwlsgJM%2B%2FoF%2B7AARFr2urFZpnwztfpIvJDWREQomJ2HncGAHZglMfb&X-Amz-Signature=64f7ad6d5c154ba27faf17e6f05adf08963fe5a0958fb4b985ad6d0cc0894b62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPY2BWUE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDag0ZOOjfV16P0r%2Bho59Etvugwpzgkh%2BZtYHd0wJITBwIhANtJ7Y%2BSGk3%2FNccGGoynCYN%2FPysGudhwtrBKzA6kHrNPKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwOWEfMlrH9sI3sIMUq3AOxub1nmmTZuNcLmr9kzMdJLmyviUCo4a2%2FkQy5R3YZ4bgQIE8KGdlPxe485%2F%2BvQ3PHwo%2FL0gvC0y%2F9V%2FuQt7jHOxheAHjANFaoAnrk2hDLHnh%2F3PR1MiDaDVD8tF122mlS8uGdAZAjNJ%2FkVItqY7WRMHdirlV2vHvgqNb5PHivGUqgLLwg8dImLCH2llcaBjahKt5nX6XGKTU3dUKrQvz%2BBl1kkjWrkRlStj2lvJXgwZQKzSWn1ZQsmR9Kuq2X1ho3JgfOFDsIlSEQtxEC%2F8pAryMRTa%2FFYBnmalGUOyfDkMeq8lTjMV8DxHQVv12oyBIOmGqJGlwe1hLXeHE%2F0EazlIXIjk%2FFxpMrpy6rTtJgCVnrM2HNTWTMD3ocJUAscIp1moavDvTuW1%2FOSrIwPeqNIS%2B12inzizR0DCA3D5qWMePZlQUGRxsIVjoyeBoTa6lCMb89hR9KnGlQbGyeoSNEjfHoNSndoqq2C%2BxzNIPLeRRspCDS1d0CSOUixL7Cp3QDss2UrOrXvj7AFW4dY%2FhZV19BrsC4BriTmP6QeYcfED%2Fhx%2FEJLcVtU20bL3zzsTDlKmJ1iFBrfBrS%2F70d5MC%2FiuRGjKmoYqObhu2MsZIpw%2Fq0G%2BQbs2L05uumjTCog%2Bm8BjqkAa0e2adPFHOifZX%2Ft%2BtjoFUCzDMISg4NxC7zZjB%2B3pvyaEtpmY%2BMH%2FxMvPVz4%2B34dNgw1gzwQN8mjTT3iOyzY6HnLztEL9EkSJMfv91IUcnFY4nLOAArFYPu783wb%2BYyqE%2BpZG8U2uVnwJN%2Bs75bXpVpoqxNV8brJNRW2JLH5u3MEMuXNmuF1zkCvUcKkQ14d9EoEkireegfzsC1Kx1ycViGlDB4&X-Amz-Signature=9a3a305df44fec72b6c3aa28a2d94f3c6c9ff1e5b167f6100a6d12de64cd0aea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4BB4BNM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzStyOUX8Ya44sH6PEUgQ09PYUzON3m9aIV41AFaWkIAiEAmg%2Bbm0vX%2FvaZutRL%2FOIq9iZULkIe%2BmfYlwDBIUL7dawqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIvZH2NgG4%2BYWAptryrcA5ksp5lJiJQOrPO3tyFytHYoFjE012gtTulPOB%2FbsgjjhEuvj7egDPCGs1begUWUXMpb1V6WVt3ZGquVWvOyIdrjS2n8H8QwH7%2FgMe%2BUTMRXZcLXkLnf%2FuvU9x6oKWluiqK4ZMlWBRJp0rIBF8jb37D7rUBB%2BwqHXQEBMRLd%2BE3Uyamg7Q4EH3gyb7Zv2MYhJgoog0c9inXqJH03yb%2FLDRqNoZAPmpfpA1PAIZMhEbTW6aa4HXdHacqlR2mOA2FVGDhrtxn3xpBCsCaE8VWIoQcHC24S%2F2MEHJPwd6%2FrnJ%2FXmN31A6GnM40rhKRcAdm7y7UFO8%2BKqmceNWNa3bawK11%2F5x7wvcpuXxXez7FnPa6huileJQb5QAFtydOMG3PwQeMi%2F9faApEC%2BAiE1jVvPzvRB9hT7SkC4%2FzUT8QXUaywKWGuR1lLcEJ8CoxLXm%2FLpZhJpajRSRbwixJbdp8wPRm3OupJFp1rHReo7%2B4Za5jT%2BrU%2FK2aB1hMo%2BbRbgEHi%2FEo75t660hcWLZePJNdX04ayVajKqguhe6IunGieaoKWrskjG3mcTxFtiacx8qL%2Bmuta0%2BYBpjumI244Qa56pmi5VAmA9X5mTOn05KIA6UQNvzPRWbxgEh%2BdUsS7MIGE6bwGOqUBPwd2B84%2FWwnT%2Bu9ipmKFtMcjL%2BOycD9%2FJPPJN65xljFZOAi4Yano5igETQ9N31BIYPq14xdTm2Yz1HWVvlG2W1bX0TFPByx%2FAlYs2XkRqkyucgg%2Fp%2BZUxThM9VfR9gYyAJSOFncidFIggowy39DnIjrjGVmeJkDo1f%2Bi6a78%2FQmcVGS9lEITv2uA4FMgxwtjD4Z8TWrO4tIB5vdpunzKVWaQzvs9&X-Amz-Signature=d8fdef6db703637d5e4e459cca3a9f656c6c3a1d9fcae66ddf3c29f9d2f39fbf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4JTHRII%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3OJfq00B4ualKQcO2tlDGSLq8cm8uYf%2FkUUUbKM3EkgIhANsV25OkPJ%2F%2BUfzh4iA0xx0%2BG8WW1iXe%2BzZcsqY9WwWWKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuI4pL%2FrEVfMtEP7kq3ANKtuuKktAUq0IZju82K5ZlOBAlR88GIfZw5ZZPLu9A%2FSJOlbxgVLn8ZgBEXLGODFC7nwmP76NQpYUUeHJnp%2FIGg4G%2BdqRvbrSsYeO%2BmGim1%2FEv2jCArq3fexK%2B6HdAiir0CDFUbsQjHA67u3wwK9w0eEv9jQyz3%2Bf4aVEa0l6A0VyOPOBca1Gwle84BNBJ80aztmMFBG%2BX7WTXGvykd2nOuGL9o2ZLaBvCyGVvkM8T1h0HKPeykGm64qOLKhwMYkFEpUO4J0q4fezLkoD2iAk6gChFTIBiAGeAQewCehIl9FUWbtLk6GKWg2Y7WfdkIW7Swg0mHZVBl9mp%2B30fGf7II%2FTnUhZ2ubbCAkVq4MS5koPrZ%2Fhv0%2Fk46UnVFQ2GCqHSau5XvKMQNcQDLndbQdskPHLbqwud%2F9t%2B6wcLvFrF0D4Ti%2FnVFdviT2CmSaUKfA%2BVZ5FV7JDmNcJ%2F5zrBIE%2BlNQrZIGaytJs3YSe1FHF34esYRDBt5ogcF86qhj3jUaTwrNvUJALvPN%2B09G9mLLxqAZpfA9j7%2FXBBLV9yghwqq%2BOnFHW04N0Cs2VRJCIEkK3pyAJrEAGBUAEyKETVG%2Fdb8dUvnUUAld9S0dL7vd1usvRxBmxDN3FTHSi%2FmzDVg%2Bm8BjqkAZC9HpFbnSEckEos8ZUiKMj3qBBU6NiXLawuiyXsHS9zd5rpNZBUp%2BwG4k4IWkDPil%2BKh2hbmmR7oG%2FClK6P3Un%2Fet%2FJQPYSxb1nhYpjcH9LWl6E0laabUOk1qqBJFu9UQlzcdAWWRzu8acBIlTe7T%2F7ZEHymVjk06J4%2F71kuHN2Ft7D9EjFZv5DP4lbOJh0YLqGLXsd7Ac9qHnSEEPatRFSdlo1&X-Amz-Signature=38f25bc541fe6bd2603962a78bda3aea285dbaa017d8ff948fa25e3dce9c42a0&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVTRMZI5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDneDR22lkW845XtpWbr85a0OGjT8snt6DM5lD76a1F5QIhAOlTUYcLzQufFJFpy5hnNp5I9Z9U9iKAMyzxD3girxx3KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBQhaYp1U7QAizB50q3AMDy%2FSzUoNrDpcby6ejtL%2FWQU4FKD37M5mCy%2F5Hm32C4dp1ROTpVD%2Bt7F8zjz223NIfdohODVJ2JbD3ONpS2GEwny%2F7ApDffgO4TeEp9UQq2IKlaZt9y%2F4fXc1jIkHWeporjsDSPF39n8n6w7jToYsBvkIK%2FN3MG9JBG7%2BCOCvieGZfZHPqgqiYlaebL62a9V4ti8k5v7oiqZCuwDF4%2F7iRf93wVKZ4udgQszxqIu2LDXONu3JBt9A88IqzSVEyafzDk6ZC%2FqiMPzs9aR3iG3tDPgIYVLm9J%2BChwCYGNILfrMi9bCoTGAD%2Byp%2F%2F5zX0OMeQeuSePnlyhDFETr0UskOngOejz%2BhZ%2FZIgOQlMeQ1mTZ5r5Q22qT1jdtO56Y5uncoqzqbr40YGic%2BPLgp%2FbIsl07aV%2BS%2BlTqe3q9XE0jTue2wL495ZFInIosNb%2FlpUyUiw%2BGni2TFWj%2Fivb5Jd7%2FlDvHv5zSRI7TtQ1qgrU79S9eK3cr9EeoqEuruq1lLJv%2F64L2Y%2BF5rLvPK5RwP89SFcBfwxfouuHvKeLdNVOBmb2SkfiNoB%2F38Cc92rAh14vvw0PFwrPMp3X16LwE9EoDLOpxPUHrQO277BnYnqb6WfVg0UJRgdkCYyKEjtfDD7g%2Bm8BjqkAad9c9EEbQ5VyG1QN0DPv2LQODfnfpJA1x1eOTS8SdPn0Rts67VQYJjk15tQoN7hed%2FutGqgAH9D6Zu1%2BJ8x4Uc868CDvbSBkJHY0LPQ5Go7Gxfu79pcLVQtB%2FaeDqRyp8W2daD%2Fq7VBDtQX8%2B2Hu2kGO%2Bt2kyPyyt101rn%2Fw2JmDaPdl2Mi%2FiBGjIZRgH%2FIT8PNsMf44q8PhiFa1qxCTVOsxeyV&X-Amz-Signature=d289c203cefa8661bddbcd26f6baa3d4f8cab309dd7288a64d08c3eaeca641dd&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USL4NIU4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDeaXNKIhBtdIc6PshOwuoCHTwSfZoekN7WcniUmCC1XQIhAKAGXZo9RkLeIYjVA8cUMbDEsgNWlqZahybfVUeDyFZYKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGy6Pc%2B%2B3ebpOZ%2FkEq3AOyqg7WsvWoGyC74xjgCCc%2FwUMVO36kijl%2Bp5yLIoq6TMJqrGlGnRAAbLKZNUNZi7wUTuWlOyVsAT%2BdGPu2BLiLPPXGOTl3kkI%2BfRMotm%2BtULY8EZXwk%2FyZRFQXt8%2BV1gkwZbNCTcHztpyqFQO%2BUmX6VWv%2BVsQZhtxLJMNluYQkA7UQDNtu%2Bi3J89FNIATJbMVcdo4PPdFBvkTIPnpY9invVl9534iQ%2BI%2FOhtDPiGUwjlxN37GIa8k4FvhTphJkANuoy0M2K9OJUNh%2BrbR36Zu94t9OJK1QfxGA442eFaDcRpWxO1ZtYurNJ6nkabnojhMU97KJSyKuyDmOwBv6OHDLrAR9vMDJFFoypFOx9Q%2Fbj4bQGudxZtFt4dbEa3flH4lZOryoXUbIAGF09l8AbIy7qjlm32MSUsvL5zMTGgtAtKaYlAxQVcVhiR9UizPY3BWR1GR3nLbi%2F5xCdvIgbNQLAVjU20hPwQGEz%2FH3x3xlqQB9c8J2S1CG0hVwpWKwcKNGBI9s8ofU0p9amc4%2Fuhf2J0QlvvkqEWyQ06KeB1KNvRQQKTdlYSJR7JhLYzGDudqj5k6r5VPKlOm1i51Z0KCK5BDqE6U3knZiYgwaQ%2BWijwFWbOuoF7lhVIQpvDDCg%2Bm8BjqkASTSqe%2B3dDMDe2%2FEOyz%2Fhvi2I9mMgJRaUgMZya5sX1p6tbOf%2Bev219mMiIi%2B6YDZ8vEjtUoX%2FUYmd2KyGDNvz%2FKqxq4u%2B9Y2gbrLQ3f0u6rpY9CVDliheWixaCp8VmQKprpWC%2F2huiW%2BeFLDxOtQ81RkbWqFnhACXS8Zty1OIfujH3JCrUiMf35Y1FxSK%2F794sc6lRTq6Yw1EKL7sZRA9m2Q5dHr&X-Amz-Signature=e5839383a1224808349b04919fa4e560b96c15e84c875434def53d5a4bb4b0c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4BB4BNM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzStyOUX8Ya44sH6PEUgQ09PYUzON3m9aIV41AFaWkIAiEAmg%2Bbm0vX%2FvaZutRL%2FOIq9iZULkIe%2BmfYlwDBIUL7dawqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIvZH2NgG4%2BYWAptryrcA5ksp5lJiJQOrPO3tyFytHYoFjE012gtTulPOB%2FbsgjjhEuvj7egDPCGs1begUWUXMpb1V6WVt3ZGquVWvOyIdrjS2n8H8QwH7%2FgMe%2BUTMRXZcLXkLnf%2FuvU9x6oKWluiqK4ZMlWBRJp0rIBF8jb37D7rUBB%2BwqHXQEBMRLd%2BE3Uyamg7Q4EH3gyb7Zv2MYhJgoog0c9inXqJH03yb%2FLDRqNoZAPmpfpA1PAIZMhEbTW6aa4HXdHacqlR2mOA2FVGDhrtxn3xpBCsCaE8VWIoQcHC24S%2F2MEHJPwd6%2FrnJ%2FXmN31A6GnM40rhKRcAdm7y7UFO8%2BKqmceNWNa3bawK11%2F5x7wvcpuXxXez7FnPa6huileJQb5QAFtydOMG3PwQeMi%2F9faApEC%2BAiE1jVvPzvRB9hT7SkC4%2FzUT8QXUaywKWGuR1lLcEJ8CoxLXm%2FLpZhJpajRSRbwixJbdp8wPRm3OupJFp1rHReo7%2B4Za5jT%2BrU%2FK2aB1hMo%2BbRbgEHi%2FEo75t660hcWLZePJNdX04ayVajKqguhe6IunGieaoKWrskjG3mcTxFtiacx8qL%2Bmuta0%2BYBpjumI244Qa56pmi5VAmA9X5mTOn05KIA6UQNvzPRWbxgEh%2BdUsS7MIGE6bwGOqUBPwd2B84%2FWwnT%2Bu9ipmKFtMcjL%2BOycD9%2FJPPJN65xljFZOAi4Yano5igETQ9N31BIYPq14xdTm2Yz1HWVvlG2W1bX0TFPByx%2FAlYs2XkRqkyucgg%2Fp%2BZUxThM9VfR9gYyAJSOFncidFIggowy39DnIjrjGVmeJkDo1f%2Bi6a78%2FQmcVGS9lEITv2uA4FMgxwtjD4Z8TWrO4tIB5vdpunzKVWaQzvs9&X-Amz-Signature=fc1087cf7d5e466df43aad8b2d48f5ff5d461d70d426f69760a1174c2eeca893&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BAJTQU6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3bu22tW85hFEfm1dYjMQWJHC08k2X058BPgg1Fwzy8wIhAOdyfF4qzkbUwU9yxoFPjF4qCMrgvR8IJxy0XyNbjHQIKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBlKgiyv5lVOoTrCwq3AOIaAqR0qTJXT%2Ffx4%2BxHWRDVdx%2FfT1l0x5i6i0Iltoyd3nUWrnjMKBgdXZbaI5dhx%2FImxhKUP9XhAgK8QeFnEt7aLEXEkyhOLc%2FGvdBRui2MqoDB1EmB1oaMPI0BMzGSi6s4h0E1iyjycvQ%2BldbyzdELGKtXZ3SSG7Nruq%2B6nzCCwd1NwBSksrjdVBwcQcf6ZjOLkwnc6KflvZw45wqzqPqVozrDCQDrNUyz7YYlX4xclLBFCqEUEu1mZVTI6J6d61dzuGwmMJeH3nyrSo4iNQVYeieHD%2Ft3OnCDTPoKWehAFqiP8ZumDS0IQla4e6cP4aScHhQjMfKEdvnjzl0LMtjq3vkMK5UCDt6f1XchrUlK4YRwd%2BgD5YM7Yx%2F3%2BXYJkHW5WWZT1UHNW7H311pzysgYIaKk7ez9kadzoSWz5o%2FlxH3MuL67CmJ11y1QrMA3p6LX8uwQNSluUuHxLb%2F1sSBzNVvNJPqrTnfruiQvyVkjFTYd0T4TaPvNaG1%2BbDHUyNEP4siCbZQtYV4tWGVM4vWlvnkq5JIgmfqacG75mpB1yYmqLNsIRMIAGYuu9Q0zqDw%2FRrB08AuZEthTNPfR6x9VS8rv7HrG9TJHio7O%2BQTIsWiEjl3FcszhF8UcjD6g%2Bm8BjqkAQvjGwz6CVf3MmFQC16BDgtPeLKc1KE0Y%2FG%2Bg4hEvXIDXKyz1u0RLm7NycBNjxQJz3q8xfftjX7sDNClER2eFMlcSUnQoLvNVYB1qKmis5ZQEEbpGCRsjnlvA57K1qFurdUF1yP9RBDsY41cCe%2FrD0sATGSKm%2Btr3YDr3m6hkol%2FMXKI250L2gh%2FGguszw7tNdMy5mmGpuIGTRR%2FYt9N55IsnncL&X-Amz-Signature=2842c860d8380a73e1445fef66032a7bb7033fe1cbdda0c870ee21e395de985b&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BAJTQU6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3bu22tW85hFEfm1dYjMQWJHC08k2X058BPgg1Fwzy8wIhAOdyfF4qzkbUwU9yxoFPjF4qCMrgvR8IJxy0XyNbjHQIKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBlKgiyv5lVOoTrCwq3AOIaAqR0qTJXT%2Ffx4%2BxHWRDVdx%2FfT1l0x5i6i0Iltoyd3nUWrnjMKBgdXZbaI5dhx%2FImxhKUP9XhAgK8QeFnEt7aLEXEkyhOLc%2FGvdBRui2MqoDB1EmB1oaMPI0BMzGSi6s4h0E1iyjycvQ%2BldbyzdELGKtXZ3SSG7Nruq%2B6nzCCwd1NwBSksrjdVBwcQcf6ZjOLkwnc6KflvZw45wqzqPqVozrDCQDrNUyz7YYlX4xclLBFCqEUEu1mZVTI6J6d61dzuGwmMJeH3nyrSo4iNQVYeieHD%2Ft3OnCDTPoKWehAFqiP8ZumDS0IQla4e6cP4aScHhQjMfKEdvnjzl0LMtjq3vkMK5UCDt6f1XchrUlK4YRwd%2BgD5YM7Yx%2F3%2BXYJkHW5WWZT1UHNW7H311pzysgYIaKk7ez9kadzoSWz5o%2FlxH3MuL67CmJ11y1QrMA3p6LX8uwQNSluUuHxLb%2F1sSBzNVvNJPqrTnfruiQvyVkjFTYd0T4TaPvNaG1%2BbDHUyNEP4siCbZQtYV4tWGVM4vWlvnkq5JIgmfqacG75mpB1yYmqLNsIRMIAGYuu9Q0zqDw%2FRrB08AuZEthTNPfR6x9VS8rv7HrG9TJHio7O%2BQTIsWiEjl3FcszhF8UcjD6g%2Bm8BjqkAQvjGwz6CVf3MmFQC16BDgtPeLKc1KE0Y%2FG%2Bg4hEvXIDXKyz1u0RLm7NycBNjxQJz3q8xfftjX7sDNClER2eFMlcSUnQoLvNVYB1qKmis5ZQEEbpGCRsjnlvA57K1qFurdUF1yP9RBDsY41cCe%2FrD0sATGSKm%2Btr3YDr3m6hkol%2FMXKI250L2gh%2FGguszw7tNdMy5mmGpuIGTRR%2FYt9N55IsnncL&X-Amz-Signature=31ebad15e20d8568052fc67a21176c905b4ca9376f8f992b8177037047099175&X-Amz-SignedHeaders=host&x-id=GetObject)
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