

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXXKEYNF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCP3U6NMUj%2F2huwfr%2BNL2kTmDwhAaZZ%2BKfcWvNxUeQiDQIgRf%2BVVXsSzd6jnr5iuQd3iGVCbWNLtuzm3wt%2Fi9nJK2Uq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDA%2FhkAHlGQpBYl5W1ircA5MFisT%2BJxriKLKlurBnH2adKjlme%2Bt%2FeZAtap8slDED95jliQjRsOkwPoDvI71qW1ica1OGEg2DSEn34nV7gjQzJxQBxPGOsh9wF4pO0FEpqVehszewZMpXYk3tHA02kl0zdB3igIMzF6WSCPJbCXUn2%2FiW%2FtwAw3ss9VPwnRxoBoVwxKm18W%2FU8YFcdXgMjhQPgyu46tOnopAmgRLLnI54LA4Zx%2B7nm3md5lCMDSOQXs6wNQxdr4zbVnKIS8dz0R001%2FFwKDVkVuemWmj2eoAWVepNjPdB7SVV4Tb7bAGvTUZ7plhG7VhheK47A03eFZ3S%2BYzb%2F%2Fi8VUV7UdzfWqCXLly8JYpMrG5xXbMoyGIzxmZaayksmwsw4dZGwWVFXljn1QKUOa%2BZMcCiEZXG9k%2BPfAeB9aMdbpmHNl%2BjJEv6iMB25Wp9Ibv6WXf4kDKuKtyjfR3p92SAiWESOsjBVX56v3CcYTyCeHDIcK2Ewx2HA0MyBOgUwqJMgMRgrozJDsuXWO9gndDhWT0h2ytBu1ouJJ7KLmoxt3hLFy%2FcGEffmkf3ExYsm2GOPc1WyyHLhcgrGnfmGbbEB6Gf5s6N7VeuaECe1fBA5liWpUFj%2B9OMvuHrRwNiLBm8KQRcMMzKh70GOqUBFQGX4MYn8QBjijiJ60xz2NwcAGo2SHgY1PpP3KmAoGRTWTN2w4gmgsA6QMqTbTQbObTEs4m5WrhaBwiNF7RL3rLAV8I0iPETWnSK%2FNHRasQ2ZM6P0WfsNiANjc8gXix7iydsoF6EQDU3l52Z1B2d8QKyXaQ5yYvUevnTvjq6TiGFYgZ3Cm2005tV2ZCRoNPBTB0cVsoguYNZo5RiagVTPwzU3hmM&X-Amz-Signature=9939dd9a61ace601b8f46100b259ae5dc2c364178788b40fce88ff8275f1cde1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M4OTF7A%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDFgvHlN3xOp4vw27AKw1p0yO9Qe2BENBO0Zi4D1IK3bQIgIgJcIxngHsBzChbDu9cXw2pelop72sYmzTDXTJHGgDIq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDAm%2Fzt4KSBaBVpvujyrcA63pyM3s79RdrG%2B8%2F9aiOZMgLKHzLu0XXh3SxcM5epOMMd%2BsVx6ik59jZRwh9ZBI9tSu3d0k8bKfUowYGEUzUudH9znArtYqq%2FrJqPp69A2ShsB7uYFd2WnJA%2FppFw3E5Q4psNLuXaL5p%2BDMlrbjasKEBJGyIi5Xskm8Y%2FF7WWN5ZI28xPnsatHZHYWkLJiHTw7SIUJN0VUfrV2TavOT8xwyYYTZfTjmdifryKxrxUppcoImCmrldMkMSxZ8Mhnw67DcoOjsHJgG%2FByHRvoi%2B1S77OFxYAkj6yAVE%2FYpeQJ8kjhNMF0Ow8GVkuT1Ivm90Rx2Qec09kL2OsQ41oWM4Ajm0F1%2BrjVXT0BzSCHqtU%2FTvQTRc8q2NOW7flmaKfO7MpjDOSBVpVHgcezBw8BrnveGXlNAQ868iW%2FkQFskwHsKkJGNKw1%2BkLpWg3vVhdKonP%2B5GWQMPE3SQJ%2BaBQGfJV%2F4b%2F3XhDvCE192lUXwD5vX7l9IEOUFApQ1JauueTXkP0sZIZ6YKMPD165u90ST%2FS0fXhPBfslti%2FQ7lMV1d2Pky4GkCAsUGDGVGxN9kKk%2FL4ZUYkMIzp3tmrrPB7ry5tERmeSZIIZqmv15PTziUo%2FoBIAS0M8YEG64QWtQMIXKh70GOqUBMco5ukWHuy6egTDK1j3hZKAH83dlTpGjywyPdQ8qqs7qH1aTZxzSUTkFhAJVzYnl9aDNdFdd35WYZc1aat7TnrT8xpORYHqrlncVPMR22iOQQa%2B1dkPD5BbWjKVBw68mcHjuE5oNMowKjGH39VXc%2B18NpYguqQtBE436UbO5EkCg6SUqff%2F65O25Kvvye25GWEM%2Bhw9m7ETnIf%2FdtogmpOi1dCUu&X-Amz-Signature=4dcd5db55f1c84f59178c9a889b67bef8f24779c509284afae0f6ac1f927c198&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G2Z4EH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDn9RLPSbInxnfM3toe4JWESYr8zL5A6PDYBDZyRFkClAIhAKo2mXXIsjKr2h0mxFfRxQiLbY2WEgGc2B%2BmrJ4bmsM5Kv8DCCsQABoMNjM3NDIzMTgzODA1IgyQK%2F6tKxn%2FsK%2FI8qUq3APTpqPiCFOFRE2e2qSGxLO4Q70EBK92zW0nuOHKcW044RLUuJp10Ax7VjPE7FYegN3jIkw%2FzB9XwjqLduhxqsklfJBvM6C%2BSH0ANKMVhd2eiL%2BEBWCvhW7cKdlu4zN6aoVdXdlzI5cwYzqraf96r4yX%2BlxvyUwwXAvGg%2Bfs4Zxp2JggmXTc0ZMbZHtg0dGHYqTstszgcIWut9%2FqV2GiL5abQjWppJxgSbHkN3VJJl8eidTLfxP%2FfnaOFusr9d8aeBstM1dsX2g8RZOGnqtOkvA6qMdt95HYCWb9SYKa4gq42X6mo17CboYaVlJ5yjiEhH4fVsExVTXaCTkzBypmYOMdaCWBfSg9LIn5a88DuXMkHM5%2FxnJGksDzTN8Z3za9c1HT0C0JplqSDumEaeiV6jHdTdWlr%2F1XduyLl%2BXvF23oJNq3pRy%2BHcJuI7cQgNdqp3wpYlnaedQYfVqqx8okQEhxVXvISWf2%2B1Ha2itaiYFuawg9FhlRI4zgw6oF07Ib9sPYQFNlVAOzdEtqWY7X8DNmTEtQor2P%2BclzaWbW5YgoRVHZhq3oXDhqfQ7yiUhabSnLreKS1x5posUC0xGeUxxfMeDkSV38FUIvZC58zVoYxWkdtRlKKKPQLkkX%2FTCkyoe9BjqkAXUOBsY7RK9CjcALRInegOTr9q4l7ljk7UqGlaHmquAW7CXXRWUqgAzIqsDwXekpG8coE%2BM3xR8gDMGYme%2BfaHt%2BgE4z%2BjcO3mWCkHARGcE0tLnlzxKXIjOVawEvIjvIjYxz3L4nsaD3F5kpV7w7ouzqPZExlRQWtHOBGMXVZd5ggEOl2HnmcUZAb45R7x3vVJwdscPRkMYFWKPFvQ46OosvWtS0&X-Amz-Signature=3223a692293db1bb8f1d7c888395336341fcac3a88753cc7eaabd74194a059c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627KWASGW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCBnCnsM2jm6OEb2%2FxSdqS7AXxQ3hjKkfPkPnaJU8LK%2FAIhANcoJqhOzwvQFFwLVUAwCDVUb5ZDC8KaGnQsKfZbjMtzKv8DCCsQABoMNjM3NDIzMTgzODA1IgxXa%2F4lJdtwWXUUwqsq3AMkwAp%2F5Sa783RUpn8a0lclNUnD%2BhBVDLn5KDX5f1P34wV0E3H3omDhAf5jVVTj8%2FYYlXfMUIsaOIYy9Q9osI3GqaE90l3sA0MCHpV7A5grkTW1RUb5a4Ey2yJkOKsR7fMgUHnVMXY0tnwiPlRn408u%2BiG7XEPEj9LVcIJOwBnLBaCZj64rTeIbgSRo1xpTlct2KjrvyCFqVOZLfo3Hb9r4BmBTe0GTAhSHFyfO1kPNPykpO0L%2F%2B0%2F5eh4pOT%2Bg%2B%2BUrE1Y2wI71ZU7R3W9U9hzU%2BVioT9XA2OJhWkwu%2BBxMV%2FXkyfR4wM6zBQSMDfGdo8gPNLVdfVj1pUd5H4jWZGDoJvCoikGKcloPYQmRG3%2FgX%2BHUii6cgwBbf1WASpgqxVLt6Q%2BMSHU6D8%2FP1kgDA5U2s3ByjrtlSvL9Ez3kooV0o57A2bGcy%2BKZs0AU%2FsdjTwjRBg%2FSnGQj%2F1ZD8h83Do4418auuyCKhCt17xDyuv%2BgIeenAao6k5LftXVMtAtJIy3t0SVygqna6b6WOWP3rGSDFyHriIRM5e9BmXgJ%2F2KNWd9EupMWAhamxwCYrCQBirD%2F%2BQONEAPjZAFYCwjXNfHbjnDynFLeTbEY0VaPsDYbPu945nLXOusOqDYqwDCFyoe9BjqkAYpMLBhethCItatH1UviciUnBbQDDOn218T5KIZsGbS%2BQoI9zQvG%2Ba%2Be6wNW%2FD2%2FI7hpAbebYfGyCpzDF6Uz7OgwTXVEVEbCebd8qHPhqt%2BelbVBuR9mqb9hrEs1tBysOhzPwEzrOB3d6hvNWoUEAW5B4BaG9H5%2BGyaZWqNGXnMIfR78tWpAEIAWT1VUB7wclkscMM77tDhtFrUUAr2FRycVTTVo&X-Amz-Signature=ac70bff168d06bb6ce3f48858e8b0c9ad75e75839e673b09e72cc514a7034301&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4QDYHJN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIDjQ4Vnauwbd29Ofn2LOXicmg%2BGu3ZS4dG5hIkLGnh5OAiEA6O126nvrsCSojgGPUP2TZryPAd45PS3WlkuWaLR3XZcq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDD4L%2FHw2doOxBsgU2SrcA3bx%2ByvkikQ2i%2F9vii9uotLCBodKE0VY2vAkIwBGHnokjJGjWlzXh%2BbNBbhT5cb%2BB8axyLlhL2kF4nGqel8p5vjvyDLWHv5k7yzNKDnZNxTLelvcXVYwYhNouGnmDL5HY8eZoIZvgFTJhueK5mXYGQOeYjUkS%2FIWQvt%2F0jCAX8%2B2tgUHVt6kMCElJ4oVgb8rMrDMkljQXe7zTcQfBcvfxvWLmxqjMpd9EgbnLhhSsK8DwquNcss7xpHnOR2xfAxh%2FupGu3HV1wta5cJL%2BLmj0EEpgOYAbqAOmIfMTQ9qBsVQYpV44FyVyW1NTBpcekc1JUfudQvjXxapbgPh154cgbfyjjQ9Xei7P2kb1zQi8D9koarG8pvLdCvlzIrAdBJ6y3czz8InKv%2BDAlxo4wgVMR5PerptlCmVKukYcqzlm79jpvP3KBZtpc%2FCQwjIW7%2BBkTXO3CD9lVd2n8JmJ2RpEHXpO67wZyRsSmh8gO31NXYJQNjddb3OMiWMma%2BvOH2jmumq6clxWFw2sdbqCBLSSUc3CxA4LIQ1afmuh4AYLBo%2BRVJLAABQ0t%2BJtPEbte7zDHjJm9opDrljhLoHiLw8JbndEChejeVAL6XY1sUfPx5B5quvv2fhtfTgKEzrMNnKh70GOqUBkC2%2BzZqJQBxJ8aWF6wE55Gdwa6dSFUEVcr0Rx7BC6ntzRc95CZfKdFoVvRcnvQVbeMOpC%2Bm2bkczTTNRbYLN7yRsDayOB0Fe3oox4GEGC42G9CHi4%2BMMvGzCkUTzMr%2BiYhPEXpu5rS8bMjUznzW%2BacELfrQLd17%2Fq7Y0%2BaizCh3NWgsfVHpmLMUH0imfhbsRWsI8l3xYe22K%2BO5zGIk649fJgnlz&X-Amz-Signature=dd6816136c956032e2675bb706d2bb125ec5179663f310079cfcd4231433af4f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674V5Z7ZS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIAHFOB%2FS5nkBvSS1UN7BPqXaVhwqFTyMjYnesZuMfwdsAiEA2pM%2B0SpbP%2FS40XOHr5Npu%2BGeqGqes%2BmqIO7hUeJ5Ob0q%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIB9Y%2BgcjJi35dcJuCrcA3CRqOQNc3h8jo7Zj%2FD8O2FpP0DH32gfQciL55I1aUQq49Y712IHUhR%2Fo%2FQTkjLGpWcj2XbXJ98wPHt%2BK1kTBsX5%2B0U8mERCWWE%2FINZl4bBupsB4ybPUNG0l9J7ipqfEPt0j33IhM8r4zkL0jQWrGr0X22sxEniUQC3Zwa0sbvBnaO3ttU0kbVGHhiRLlf73j%2FrT%2F5GutGGW98YgcikPMEgDqKdW8ll4fa3Z6HGFAzAriZpUcIRfdj5q%2FP2uc5mZgqRjTf1tQJHiIIvA%2FpyKSJfuE9ebK7H0rUzlYb%2FnRoqrBxRMMwjUP9Q0Yx8MLzxlaGiSq4Rgor%2Fz0BIYo7dIXL2vPBgJO9ecLsk%2FCnnCXJFrZiuZeDLHUa27qcY2T82U1DerQfJfuTUIuS253QpmM9CLcm9jODaS%2BK2Gz%2FrrUgbRF4a4sxHqfBzlwcjZVAeEDg10yRtC3l4Gu%2Bp2PZuGF71T%2FnH2XX8T17Pk8j%2FE2vvHh8LlDF0KWKS%2Fad8v44ll8t08g2BhXiLZorAjUtO2fKnlSUFppJo6JLBYcBftvVA6AjtHeHCxMomzaTjdEiMipT7nTm7yBaxb5B3TMa8KRoTJkjSqDkg3hn3FUIWn%2BbxqJPW9Ogz0q14uDuB5MM3Kh70GOqUBlLylKT8xiGBisnYK7fVwVbh8LoW66xhYKduhagIsKJ0bdihzX%2FRaUiddldM8aQPt4TuHJR1AZk2eIkr7AKTCxKlIhMScd2b%2BcSoG9EBGw75TmjW0QxpY%2FWB96OKJoiLyU2JZxn04aIIRnELtab0DCZHZKiH9e3GqbTmI8GIvQLAP0PlWw3sG3i7YUj8IKtJK%2B9A98xWi3k3eyKbJZKpSksbNxt9l&X-Amz-Signature=47dbd9ca225977b7d258e484ace924268b3ad4c2e3838c3e86d78d2b768f32d0&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGBJMN5B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDNOFeO48udw0bxeZWdK84yX%2BXvPbhZZ7%2BY1xssnEuWlQIgdm2M%2BAB4mTyOZjYrZp74kVYA6vUJH%2BhqHVC7VikKbmcq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDKge2kT%2Fi3pEIXnI6yrcAyxB%2BiE3Io%2F0HQ%2BdkP8Wi38Dhud0JVY69yam3YQ0Yf1dv5m1o3m1JzismFSYt21RgpuAkHvNCDqp2QFj22dx3wGyrAsJaYgFxCGnKKYT768YaGdsJk7mjYHY3jlZwRByCtOOu2UmRQwi%2BNbJSVwZU1p7eycfErOgig7PNkjvGrU84EnNlnAS%2BJGvOnbV7m7RRp4KzXCSURpQ5PD9r4Wh5VY1ql4Xqn8WFu9xjdRSWyF4rhLLH38ndCAjoYR3W6kdk5KWgvL8bLvvBUFYhrYTdNO5rQnGUrCNxeCTpoDi%2FKsQfHTD2bcz3G9mtF8SpYaIfF7TXoqDZi3WDVvdmNjVUU0rUpk0hop3Rgt5l8%2FuHt3oZkJ53Ng4f679I3lLrIKXlm%2BqKaYp7ggc9Lq%2FIxegLgKUK1%2Fhdo5r87hKGsO9xLoPnhYWgRVci9aiz0rYMZjfKA3wIWf7HLXZz6I7aTUdgHgSYKclICcJhKU7eaUnUa5DkFBsCD8FfbMqE6k33q2q6Ex4M41bFyQ1fS98q%2FWiw067%2FODn7%2FF4IbF8TwDA1H93ZSSzzcrq42eKW3rM7sh%2B166NwXLOgEahPCXY1imsYlJ%2BZ6WZ9CpUgngJulHfOwCpLDAWyTYPeW%2FwDpEsMJnKh70GOqUBc2uXY%2BIwiFyUv%2B7yei0dX3mPV8aNM2ye4449m02kJmfuqeS0sa2zIVhEHCSnTm%2BY%2FFPgcqFTne3AZxfuAwvt013jG30SsEB%2BBdz%2BtoCJOeTXui6sDtZm%2F%2F5oub4tjE%2FfL4ogiLnlBgM%2BYAJKVAam%2FGvWbOfriDU0eSK9QYjxxO7UO3%2FavylNcJ0zKflO3NeyQMfd3XCBhiDif68jmU%2FFMzK9cWYd&X-Amz-Signature=b9799c947290f6a2cdc0e29d4474c5f0e7d9d2bff5a461de495cc0d314b58480&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIEXAZEG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIDuSbtG%2FqN%2Bdr7VEnqNKRwIFpvLB%2BRtfaDAo5f3Kvd0zAiEAm4NaBx5IC8%2B5%2F0yZd9jDh8UH7uza%2B7j%2F2MS%2BjroGClwq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDPPi8mV47QOvZ0UV3yrcAzxxbKUPtf3FSHV03gSw8ht05chzIv7Hn%2B7suXn1Lr5%2FgKaVxS1LK69mL%2FpszV3WoJGLd7c%2BoN8d%2B2gI9Is%2FA9tBn6M%2B4BQUV4%2B1rn3fOUIQ1FxthaOfJMrSaneML%2BMnPs3M0wPqXliA0SnxT0cky4nO4nXSgxRwzXufXMW14UkNQkkGpKi9yS%2B%2FTaZcOd8yuLIpFdkfbu03Q8k8RXKEIcBP7%2FjTYuNFPP2Um8CkCcw2tUFyHKKqECAJeCInAlZ4efw1jCBXfloNfktqJglHHsGIhkXusgVZN6jmJBftPX2OVPyAJSuvrDgPGTXGzs642AfioR%2FtTuuz8%2FyyJBeFqr0vJzwwWxf0JTfFUAc3s3IMaJoQz8EsRRkCXxEpzc2vNXetkGJF%2BARYdeKgQP56JrHauztCXH6NNDwXOffjC8nTLn9SzsbSnXzube15ytqY0BR5nSEzK1uX2juYFn5p0lXm%2BQtXARqiejoQCt1RTVO6hzXOyBn81dcK%2FPleOdItNbZOxoSaLAR%2B6kfuvzIheHHYZYnkZlG65JHFiZtDHIjF1L6zSHp3RB1%2FAxe4aeXXXZz2Yz5vtFQW1jOzVT%2BdTS8KzEBYf9tK0uMCBbkpSHO994kkYDaNhX%2BqYgM0MP7Kh70GOqUB1vb%2BXAb3uFQp43ZpLw%2BLgdbU81Qe7q1oHM1ti2C2eoNWDqt69GaAklP2ZMYOKH363iUgmwWd4O9YtyghGOYfURGBP%2B0KmXjMO1T9cO8cJ3H4QbmH6OghKcE0hxTchGFyJfl1IVBpZ%2F2h0UCPg3e82I%2B6XUJxrD1SWs%2FkfRN5DLzovBfiSVI%2BTqGyYtuBR%2B26WQY9rHkTXH1qbnkTMoluIw2oIXxG&X-Amz-Signature=62ba60d185d3e5cc4eb3c4d347f267a6a8914497aca8db0b18fd8856938f6b6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4QDYHJN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIDjQ4Vnauwbd29Ofn2LOXicmg%2BGu3ZS4dG5hIkLGnh5OAiEA6O126nvrsCSojgGPUP2TZryPAd45PS3WlkuWaLR3XZcq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDD4L%2FHw2doOxBsgU2SrcA3bx%2ByvkikQ2i%2F9vii9uotLCBodKE0VY2vAkIwBGHnokjJGjWlzXh%2BbNBbhT5cb%2BB8axyLlhL2kF4nGqel8p5vjvyDLWHv5k7yzNKDnZNxTLelvcXVYwYhNouGnmDL5HY8eZoIZvgFTJhueK5mXYGQOeYjUkS%2FIWQvt%2F0jCAX8%2B2tgUHVt6kMCElJ4oVgb8rMrDMkljQXe7zTcQfBcvfxvWLmxqjMpd9EgbnLhhSsK8DwquNcss7xpHnOR2xfAxh%2FupGu3HV1wta5cJL%2BLmj0EEpgOYAbqAOmIfMTQ9qBsVQYpV44FyVyW1NTBpcekc1JUfudQvjXxapbgPh154cgbfyjjQ9Xei7P2kb1zQi8D9koarG8pvLdCvlzIrAdBJ6y3czz8InKv%2BDAlxo4wgVMR5PerptlCmVKukYcqzlm79jpvP3KBZtpc%2FCQwjIW7%2BBkTXO3CD9lVd2n8JmJ2RpEHXpO67wZyRsSmh8gO31NXYJQNjddb3OMiWMma%2BvOH2jmumq6clxWFw2sdbqCBLSSUc3CxA4LIQ1afmuh4AYLBo%2BRVJLAABQ0t%2BJtPEbte7zDHjJm9opDrljhLoHiLw8JbndEChejeVAL6XY1sUfPx5B5quvv2fhtfTgKEzrMNnKh70GOqUBkC2%2BzZqJQBxJ8aWF6wE55Gdwa6dSFUEVcr0Rx7BC6ntzRc95CZfKdFoVvRcnvQVbeMOpC%2Bm2bkczTTNRbYLN7yRsDayOB0Fe3oox4GEGC42G9CHi4%2BMMvGzCkUTzMr%2BiYhPEXpu5rS8bMjUznzW%2BacELfrQLd17%2Fq7Y0%2BaizCh3NWgsfVHpmLMUH0imfhbsRWsI8l3xYe22K%2BO5zGIk649fJgnlz&X-Amz-Signature=c8d973eaf24974748c2e69eef04d86e8ab00c041a6452fae6bc31e507bb01582&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RLKZ4WN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIAWema0rrYE0emwl67dlPB59RLdreN2aQkDzKEfeKlb4AiEA0JqshCJk%2BLtbGTxyzMaL95DZv6HGhOs%2FQbObZ%2BKvz%2B4q%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDPIsYJYwdhA6BLcwlircA5d5a7t2qMpSxtMKh0T2im0FlRNa%2FkTbn9l3bzMH3cJATSUvPa3swplZmPSwWCSM1k%2Fp%2Bw5OPHQpE%2BO%2FJIKizFcr4RUe%2BhASocOtKGU%2FSf1ilO4z8P531uUgL2%2FcBicTs8t5RvuIraVdVeIkcnMymh5m6TrX%2BRiHTxAF2yNT2YNcjwwl%2FFfPYtgmEbG0U3kacDnYzrqjSY8g%2BLju1aLE80W4hzJ6SQmtBvWhh%2BxnsCfaBIVRq6MjNWSU2aDUwbB6JVSrCx8Kubs7kySrRU760EOgcDecq6Pcx34HHlYplzIYj6PozNk2WWixcrQJIjnCucGN9zrYc%2BebB2OdA6QCKiG1WdjGNu5hZBGPI5fggBWcNOX4VWZq9NjRMp1r584A8saCzeCFxY8GLKgU4XuZP9zg7aLNvV0ikOGAE%2Ff5kqVgQLJcNTZQu2DtvTNOfvh1wovuYg%2BdLRpL%2FxCBDx%2FGhxhqTbFi7dLYhkFQAjnun4UUtHD0t2BRM8dnKPUtHwZ0aeIPKRYWxfME9LPNqYWgLcr2muOCHq%2FFjrk6%2FTWEwtdjfbg9Efz6qEf6OqS7fFNi5%2BuFMzQMyZZhYzJv%2FiQo0Gxf5DU6wwv6jblXeSY6vLAYN8ATHomNNnzSf6waMIzLh70GOqUBF0NEF%2FYXGLZZCWT9TLQbNZAqgBlOydFTB2O4i%2BGiAqiP%2Bh3bnpGDgWEq2vj77tFYIUjsFctVpK%2F1fdzAT99N9nsCC6ftUMU5bxHSo19Gatxp82TDIs6d%2BPm5X1k%2BYo6vg93XPdbBR56Cn4F3RChI4ITT5AnVeb8r47KMmQ2LotIfxNXpFwGM9Z4z6LwyfniCItD8LSMZRJG8sfEqCQnraAxKBuXl&X-Amz-Signature=d2c8e346e3c2ea43747df30a4add69d4132226d34b6771219490a5dd7381317f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RLKZ4WN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIAWema0rrYE0emwl67dlPB59RLdreN2aQkDzKEfeKlb4AiEA0JqshCJk%2BLtbGTxyzMaL95DZv6HGhOs%2FQbObZ%2BKvz%2B4q%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDPIsYJYwdhA6BLcwlircA5d5a7t2qMpSxtMKh0T2im0FlRNa%2FkTbn9l3bzMH3cJATSUvPa3swplZmPSwWCSM1k%2Fp%2Bw5OPHQpE%2BO%2FJIKizFcr4RUe%2BhASocOtKGU%2FSf1ilO4z8P531uUgL2%2FcBicTs8t5RvuIraVdVeIkcnMymh5m6TrX%2BRiHTxAF2yNT2YNcjwwl%2FFfPYtgmEbG0U3kacDnYzrqjSY8g%2BLju1aLE80W4hzJ6SQmtBvWhh%2BxnsCfaBIVRq6MjNWSU2aDUwbB6JVSrCx8Kubs7kySrRU760EOgcDecq6Pcx34HHlYplzIYj6PozNk2WWixcrQJIjnCucGN9zrYc%2BebB2OdA6QCKiG1WdjGNu5hZBGPI5fggBWcNOX4VWZq9NjRMp1r584A8saCzeCFxY8GLKgU4XuZP9zg7aLNvV0ikOGAE%2Ff5kqVgQLJcNTZQu2DtvTNOfvh1wovuYg%2BdLRpL%2FxCBDx%2FGhxhqTbFi7dLYhkFQAjnun4UUtHD0t2BRM8dnKPUtHwZ0aeIPKRYWxfME9LPNqYWgLcr2muOCHq%2FFjrk6%2FTWEwtdjfbg9Efz6qEf6OqS7fFNi5%2BuFMzQMyZZhYzJv%2FiQo0Gxf5DU6wwv6jblXeSY6vLAYN8ATHomNNnzSf6waMIzLh70GOqUBF0NEF%2FYXGLZZCWT9TLQbNZAqgBlOydFTB2O4i%2BGiAqiP%2Bh3bnpGDgWEq2vj77tFYIUjsFctVpK%2F1fdzAT99N9nsCC6ftUMU5bxHSo19Gatxp82TDIs6d%2BPm5X1k%2BYo6vg93XPdbBR56Cn4F3RChI4ITT5AnVeb8r47KMmQ2LotIfxNXpFwGM9Z4z6LwyfniCItD8LSMZRJG8sfEqCQnraAxKBuXl&X-Amz-Signature=090474c9188dc1b6f647634efc0ccca4fc751d22514a3ff13bb9e9609a148889&X-Amz-SignedHeaders=host&x-id=GetObject)
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