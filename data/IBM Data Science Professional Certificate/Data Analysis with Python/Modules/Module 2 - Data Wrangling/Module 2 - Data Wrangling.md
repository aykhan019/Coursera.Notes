

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IXLSNIN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGrIY4%2BQqM3jIT4E4pxm5J8Ph8JxjnggzB8E5OH6LI%2FMAiBKZE2HdRfMXPFMemqqJVNzHDjUeWewe82ZWNMTkCQ6lSqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUo3OOx%2Fj9tVDG1%2BmKtwDOK3dbEVAT0geiDGv5iovT8RJ4s35dsgj75cQkVvqz%2FyXLf3QfLTNqH1Pkf5VdeXGA4D60tZJjHRUH6IdSoYiHfZbydKX%2FZwfttQdq87cKsiMexOGeuaqX7urAGGf%2Fh7a9s4ymT2H6AXjxYi8NQm6KuGE8mW55CxttLk4VFdoDezzxx0urS4ECPuCa4fGuHhKG8dVpgxkPV4dLryxTUk2zAK63h5oOfLDGVIt4zTqYhcwlu1hJ5GWllcK%2B%2Bw3rw%2Fa362NbUEQzYYW%2B2Jl8DWBeqEeMPX72mHQu1Sxk6ubLZAWlX6eCHMbd0HG%2Bf2fo3%2FYH%2FkFQky1y3CqyuMX1H7%2FMuIbkj7YBVvwbJgE%2FjDsrC1ztQ%2FBOkF3Sm8PCxwpXzq5eOrfd61PC4ChEHPQcShr5CbxbmPKB45aQGK8dnCoWHHjD1Rgty7iOVjvkBaCbzVToAXiJ63S1WiDnRfRuMj2tIsrGCSP7lYIYu%2FNg%2B0nY%2BY569%2BqYPiWhdGZvr2goWum%2F5MqBi2seOxN6izsXCS%2FLR4NTiOjBPIgOwJZq3pYm0dc5pKhrk46DqES4x2y8I8MKEkwmj7d3JnULzvopU4cRXTDMt85DjUANa%2B2DOwK1Gmkts95Uh05vMYHa20wic31vAY6pgHuLJPuyLJsWhYalOzc2qj%2FW9g892hRBoLmN4afOOJkQ8Unf6k0cZdxg%2BQSraKlc13LJp4CEiP%2FQqXA57CZlgSkbiU2S3aIX2gIEX1P6Lhn3PO9cRVZqoTLvnoInVnA%2FgcViF5XIylTzDKAljW4mCNeHML%2FfX0jpjW1dLtGOClfELNIvlskOCb9foCnj4mYS385aQRMTKaMRC9XsBIJgLr6JrTG5Gf8&X-Amz-Signature=f8c02c76b1b2e73f6be8265419f38b3cb710d2c455b3055dd3304e9e1d125a08&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KUMDRL4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpTulYJ8uD%2FcHpnQdLRKNiFD8Oxj8sRBJqiu5cMmm3NgIgewvUVoud4KC2Hd4XXLHXuzXE8z284q7Pz%2F%2BW9jEqzWIqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIwk4fTbcWPbLDYOCrcAx6YGSeJE9SpstMxDWjkMfJxYf5ys21ff4XP%2F7lUzsdBeYfYYXbq9MmCvOg2W757ebPTrS9NW%2BYNP25d35%2FSiBbEub5yZ0LBX9uxZIzZGg7LfcOxuwDAzty0AD4ih3tGoX0Ao%2BY73p6%2F2OFe3smDj7PzevQ5fj0lFTE0ViR0ieEjnZu7jbBEg%2FBDu9C8ucju4v7x3l%2FqHV59Qb20Sv2wmHemLcko99VCf%2FFSsF3r5qCPQCiBrYf%2B6PaO0gKQyK2KqCDcCjB5ZZQ6FbkjuFxJrXv4cs%2F3riIrx47h4nOEDnB062lqVaDwKpdiiK0qjJVczUmZA97YQKVwGV7C0d17fvJ%2BsUk6TeawZbOXrElaulcjqRlKBz8nNXUWQE6EF9cvZcKWDp1t6UWv66wCDX4F4OP7bD7UC%2FpYRUB0pqWhcdjfbhJpQxsLdjYpCWlD%2FEsagfQGAivyvMbxUoTbaswGdj9T7HBhBi%2BdqWwS7vNHgrDEsaHt%2FKfEpifQe3sB3dsmxLr5lOg4o35wH1vSumRzpunCCxhMrF1tacEzrIwKMY7WI8BcN6zx1YIg0B%2Fu9bf2%2FEtMxGR7s%2FjyF8Mf0mndoMxSUBLwRjK1Ozs5iPBgKUfjgAJ5wwKfdfaJpAV9MPnM9bwGOqUB7VJ8uODJVZTkcy6yZpT%2BFVNr%2FKi6CsufTc0a25HVssYDDJypf1JIDrdssVLbNPzKyT0k9xt8PomHZ%2BbiUxt7hQCKo%2FxJ0DebflTabLSW%2FrLdFq6J6l9o0Dehp8HtYiXGZ3U1T1jlKD46AG4k9RETmWMdNGY1vBxT6vxTH30LKrr0Vqcj0UI12vUyKd1nQBaMiC5JNuMZctKL7eXelvnYzSlrVI%2BH&X-Amz-Signature=b77007bb394fba5cfe6489f9b6e487f5d5ed23f27ffc1e5e137ac93eb684692c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTO45726%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjRVRVtXMPUEQA3H8gpgFrINjmBdROr1X7l0MyIcG0RAIgWi4nBIjAmbFbdjitgSqXUMeQiXhf59Rug5o1GotY0qoqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSKr1%2BMUnpXT9nleCrcAxBEHLR1z4yGVv5tlvLRLHD2pkzdAJ5jhBecHYJdxtM7CTUrBsV%2BPXg5SdAezA3sh2Gqgd44M%2Fvstgc9UxA8X5gro0AeFWs9eS8t7YRzYJ8P0sEUtLXyBybdJiFCJHlREZOBUedHh492ET9zarVk5vl7Z3yumEpAdCo86n0K1o32BfJmVdbgmhDvZxeA26IYOl4ctwkTQ%2B5D1gHBPd9ef8mfG326CASkVZ%2FFSYbPuaqKgmxvMwzT%2B2saI4k0FpYUCOBP6rpgAWNHZItOKD%2FYNLukso%2FKxs8zgKJgoUa%2FYTYcQjQDI5vM6J9kHGsr%2BykBffT%2FHtnTFqSf8GMpnh5rnllrzfVHAqWAWf1n7xCfy136%2FCuTt7srNgZU9eCmf7OkgYUC4ZUF7U8phvUAkYkBFFvwlk6ypEGF4plCr6vWiWCUb8J4HprhXo8uAusJRR1ruddkQqrYaXmS8raQ8C4aWFZrJAy0INPUdPoRTpOozyrsHCHgAaTjqtyGo8CSV082F5uxR7%2BLWyItx3%2BvlV4e6KbMeUFOSNk0UqUg1BfQrxlgFth%2B6hfLKhhmxmt%2Bl%2BW3JNTAO%2FIyR4qJMVz%2F014FguQ%2FmsJU6cpHc3g16ZVQNRB1sgV9sPeBYqaKBvYdMJnN9bwGOqUBm8Cu9rO0nkg%2BlNtfVpw3YOZfgb4nMzHfDimwvkhJWoik%2BLygEnZQCeHnlUCwl3KCwYZuIFFICPBGvcX%2FSogWirkwbpQEZk92yNCsPMqg9kpsqvn%2BqxqT9qMAh07O%2BWgi16Yd4DlUeF0vCWqZ0skV7fbllhvcZko%2FUsydkIpZxPAmI%2BpZ%2BpyzhnZiM6v9b%2BpaqzDxLVmI9FIbzIv4f4c1QKiTpQum&X-Amz-Signature=64dc8872bf229b3ec180fba54de4485e48e51735807bcfaf2c63163e8d616182&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU7JE6EY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaUzqbIPg6SRhUTB0h12xU5%2FeCei5bDDyvOofJW1crMAiEAwRZ2pfd9G4vSleOHWYbNvp4g0YEzt443cUHnTAWiII4qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCFH%2BOVFuE9JVCiAYSrcA%2BeM3qHIVok94WtClXdoFeHOGqnRbTV3OACDgZgQfcsNz3RWu94%2Bh9Sys0q%2B4Yl%2BU%2BJWsdi7HqNDNIZ3hiBujjQeFqeL164636reYA8gds8jIRR7KIXxEG%2BzlLu1IQjZ5bMcrLJhfACDTNPwbH1z465WeRhy16Pbgt6yI9s%2F2IpVpFpA9cVEd2X2ZUqYWhwXXjCCJ8zww2qsyyLglxvdzoYAcL5t5W%2B0HIYqIgRlP19iteub4FOiPnatpKfy3wng%2FnRKVKGVnMmtxWclt%2FHxd4YbbiWUa9tARmtlGqrSSPgwpoz7X%2FR7cMH2ZuBIAxmSIehTdgbhO%2F2GkJgVMMN%2F2Kqgl0T6uqPhVC%2FZZPAiqOwSkYc18FWPRXbkuxh7Y6Inl2yg4ZLek6r2yAP%2BUo1U0q4KfuihYxQaVavXiJlXZGKWOL8E2i0Gf64kILH%2BdFQA7zsdAzaFqLSoZIa1V3StXYpR%2BH%2BAL1Z6I7SHe%2FAOMdykmmD0Nm0PqN9Dw3yHHPlrkXcfopiwQjQazZFvYMlJgALJOPkrCt92TmgqXUE2mMTHhAG0jNQIGCHRVx57YkAdsieEIl1UeARtP455mU1I4A7%2FZ9fPEWW4rjectVznb5Bq0lDHNEPd%2BxjMNtQpMIvN9bwGOqUB4aRjR65MNtQi4kQixNbKTPd3S%2FD30ZTO9TpQFhscEHDoplDSmusDlwgHtvbbAK2wuPDiceqsRPgGdbPwGyXrOWVF0SSl6JxroZd1QOiJzd9%2FTIlHjhdZCKwHoMKURwEFvP8ThXnMW41KGZoB4J%2BL9QaCGuOQaln3M%2FUVQxKmZZUVCKJbIE2ow%2FAswyXXbtcY%2Fnp2ykzKfG04sHEfupVigLoSIxOn&X-Amz-Signature=0d8cd4f947001ab62b4b80678d4e550267f638930f60a207eb3ad1000c25ed11&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QHLNINK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCffC1%2FeWXyEXwcVDSl6fHhA2A%2F8OyI7bbAdDGlNbbCpgIgQeXpGD3XKaga8BcIYMVdqFD32f1vXVYpO2Y8VHjiWfwqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7mi133C54WcaACtyrcA9eJ22wcD0gZpoQlIYEk73odkTE5TTJ43lcY%2FgCBtc9RPOPaRsJiHmODtG3RneEmpqe6gYBh9NiJq%2Bz8t8Ed8Wg67A%2BBlmIM07DnMKzLIxEEjLVYmU2pBp9Qe0CRcn3XdoKwk14dYpegRbyf8uUsPwKbGMRY60xXA8areYMLOJ1CnWgo6NG6485Uos6NewGkhz%2FkbSxUp0v%2FKM5yEbNIGmT6UI6AcOg4gxFiY2ScIXr%2B1qgyEoJsqAudfo39f8Zrsdx4kLtUJVWAB6iy4eVxf6MsqFJscqGUso2jYNMFeHu%2FZ3rcOHSz6w3EWO3OSXmKCYNZYrqsH0JehA3IS97zelozZ%2BsOyIc8K94xofJrC24vO8lkAkJT24I2xf1Ca5jtq0bPJmgTqeKDMcgGhvDrzwk5AZv4mI2qM2QXSwXSBaIYSKqFJLKNE0teXIEkNf7eQxVHmYL3mPAN3EnL4YXMyl8Bdh5%2BZxm8CGOTEjf6vCPff5gcINo%2FX7uHGIHdhAs8w8H4kl01kf7YIDcp2Ip3t74xNiyctHRRimF%2B1wFDvlXLVEbaE%2BBXfFyKDIq%2BNyhSgTE2MoMTJ6tpOnpm988pTbvTCvaUXNb%2BCkyKZRQB38uGxWqCAiw76dd1YhwZMNHM9bwGOqUBPNOriRJtLomt%2BZdU1ooq6b8FD13nXUOvTCPGHzypGiprBGSAKzBRFGjpTYmXOgVa2VcKsKcKXrDZT0MP5kp%2FV3gMpQJLBWovjAd1C76lhcR4eBNbozNWzUgOriU73TvjSqQTNlOiPrJpJ779nNPl5m%2BoEXMblxtf7%2FzjQjUCFTFtn6lGnFttYDxhxa59m9tyoWwp%2FDt567rNN5%2B8x1lnM4eluF8z&X-Amz-Signature=c16621a4f6db6e71af9fed676ffbba5142949b58eaacc4f3bacd7edc4c41ca8d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVIPL5IS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGReGeEIp2Qi6xybxFtbI%2BXGl8JChE8EBNJOujlo9h2PAiBPPlelss2O7qjGrSCWd4riy7qgNpbSVmu4HuJfn8wnVSqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMguSrgqbpKw9S0zemKtwD7S3wiCL8Va5yDuPeJmhPMDPKwCKjzy0%2FutZtjB1ry0LtVnbZ0Ot%2Bp%2F2q7ESkoZczIytT7rdU9l8mM45NGKr3PrAi5gZimPPoJFnoTM5%2FYg7no3NWkBg271o4cnnLpNGVALgl3euitPEydtYCgH4BL7wC3IgjDhVgW4cxyORLhkekyUDWqLtjmOPOv0Q%2FEolwJz9tvpxEFvKD7UqzWamWVeODHTOxwJD6ofzm1kzrJwDoOTGRC8KL57A2ycGefGJ%2FDAn9KD9E83SE1tw2n9CYZkkDFu5qUV8Vo2oozGV%2BaLGp1kpR18J9HwOdAkuuzb7VIeRqmOPIadYzbkr0gdGS3EsxwcyrtW6yzFWXQLuO7PCJiJ26nE6M1RdFG484QFkGyWS%2BGLWEMhOT9aL7bnpmnezbmV6G1a0TKqSQm%2FD0PIBViWROgMRPn%2BREOT0ZVmU2L9dN6en3GEM6ZeZxE9UbxQ4LYrez3%2FD9CbmVeQT%2B8NFf01HK9r4MDV7AjzjgTDW%2BQ3w53tfagJDqnfs4vmKrtyE5CSBziBYA70LLDKClOBwwoio9SFE5G6FGZRtoe7PQ7FKJQj6OFOaBcbO0LJcMg4%2FrvP55fBcCn7aqTHcxSCbYrAWKuakbaLSXrggw8831vAY6pgHLrGJyiBa1dpnkbjfZFbG5LxZwq%2BxGj%2B18GUjZiPaeDcX8FuZHYOeFfvbsOE0Pc5AiWRdWAvQ7GU%2BIaGZfY4xKXOEK21NgVGDqKU9WUzTuqnqaY8NL4S9TpxMSze1BF6Kvv%2FkPhVw09iu7bnGbV24%2BQQNAu0cf0NAmhwkbNVM%2BQjt%2FoDgBaDZuPjGK6lrBFr1qmKlsivRUpNp5G6ivG%2BDuBEmKwa%2F4&X-Amz-Signature=697de8dcd2aee5689dc3cece0e936b85ce875b01324f37fe4ed5259e3ebb4b58&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMVRCU5G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqzfHmAsuSSIHy33cQgacM%2F9SUrWqhKo9M6qpaTMA1DAiB2sle%2FqLkUhV1Vn4s8QkJ8W5S5edD4LFjniMhaa%2FGU%2FSqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMID%2FAtUdZgryxMnZmKtwDjFHFaZqUoA%2FZWCczHii9UnJctqTRtrrvO%2FDtunz3x6B4nHejnuXaRF2rk4hJM84t7zr4pef8AIUE4vDaYu5jS0UjheC9poUxjTq%2FHN2FrN2CNTQYFQ10ZWGkjPed8tYy8mNYHKAQxJDWalIhcC3uGruM23WTTkx2fm%2FheSn%2FR%2Bv7I35gnQh2utkhiyVbgaj%2BftEt3Aok34EINKOADzIqXFHuAqAEhQwpApKcWHyoBlXqbpQF0%2BnGICDzjWmUWxFofR5zPIDpzSXnIUjNQg2wmbIM1lilN0lHwNV9lCmz%2FnAAgMRrn%2BRnZqAq3kiS7RZ1Op6REuHARRxLOPauXjexMROPLFaQYWWHXEesU4G2WVoVSU0VnsUnCNssS9QfZL8btXj0Ny3ZN4eI5BO5IdOCK%2FCdEExOQgW7jL78gjK6iZ%2FShydJ6YHJj8dpynHO27AgjXEZFsUdawY7MlIXynxiIx5Rync8pWziD0QSBChip3yOlq2dRQq5en3BgLk3IsfLb1QJXwkbpJoFyRQGiLrhws0OeGZ4pMA1XrkpeSSirqnIFGliBWwR1rXRAlPS5%2F5UEP4GuNFeI61pu56OdaidSC8h3uCz8b4aKyi7%2FoBx39RRGCyXcAqhIkyakpIw%2Bcz1vAY6pgGHLkrQVsvQb2x2xR9JyKf6mc6C9wgCIt8COZabVl%2FSxheRq9ppueqXXfUnVU43FbyzbXOarVHOYcOkOOohzTZcRLM%2BXzvkVrgY5r7B2xTBaYRTedLRQFVVh6EWQNLMEb095y97HEfny%2BIMJvtYuU8RGl%2FqvPYt62vbgXye2n0WGATNNHBNjcEAlZXnQaNk0QJG6Vox9OC3oVl0VSXy5coOkywGCC5d&X-Amz-Signature=3ebb4ebb74730210f1b1241d2cf780ced29f83250e77e44de14180fef08d9144&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DMDCLCC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvl76mHcAc%2B%2FIBsF0%2BhAXaqu36LbjYTIErpDzXqbmPqAIgDV9bUYUHQK%2BIvK5Am8ICgr6SyY3c%2FNvWnBNCFjk8axQqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFJwmuWoTxbUbJEl1CrcA1Zjdq1nZbT8v%2FpxSM20aNLT2gQjOKr5EDJQ8K1mNxypJ5EwRTfwnqxASEUIHMzPHTBtnQb5U%2Bz4zNrKaBqJNPwvvwzmplsIT2%2FLMg9CH1HisS0b5bpOxtZ6IEKyzN5cmTUNu3zFVbG%2BTZtRabsd6uBJenzUUlHC0Da7cn3mBc1LDAAYoOdZ8reqdqfy%2FPDnicQz8rF6luu8DKch2P6cMSB4dR5zPSXDUC0qo2nDvnsRkA4hVc%2Bh5Vfy9MtugqFcY1qwPztfqJEyyGscR%2BIwUVjoMWMLY88022Raw%2BBa1cGsupjIeTuyZgP4mFI1EOkn38tJ%2BtxJAfviYY%2FKnHH9pLnIMEIp8lCHjTRSBIZ6bVOK%2F%2Bkac93P2asJVChdTikL9JszQifvFUk9cUyCVhDbTq8GrU7KncKpo66eBxVlvOi%2BjGA5WuzONfQRrf8Zi7gkl4mzq27sbIQ0dvKYLRfhX5GGwycj7dS9vK360F80HDyw5D5HR6qPNV6GxuHaksNBiDJ01GbYxTsnYAo8f%2B8RilXjth1L9OF0ObaPHOdnc0ULuZVPqGipN7uZpJpoUEpS2iKewDHCxWeIP74NL8ncCWt79nSZYGPp8%2FTDG75kzQJNyvKb5UzbN0a5eLPDMPnM9bwGOqUBEwkW9oNqWZdt5n1wo9BzzjhmBmlMaRu6qEolshCh9nmiGfc3BRpGRjA1R7eFEFaLjr12PqN9mYwnlBpG8bcSlIuUQqSAWOsRMspnkPgjrvKW9RhQEMeHnmnCoc%2FjJn9yiSrM4OeAJE0C4kU7AGntb9S0%2FmR257rv9bXkXBuh3%2Bx%2B0zvzsQ%2FDaCd94q1IySk4NGbago%2FS9R8H5U5UJUnzkQmPidrb&X-Amz-Signature=e63e778dec200dbc18a4df7a06c83482969e831ebf5e9a0f7f99640c96dee5fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QHLNINK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCffC1%2FeWXyEXwcVDSl6fHhA2A%2F8OyI7bbAdDGlNbbCpgIgQeXpGD3XKaga8BcIYMVdqFD32f1vXVYpO2Y8VHjiWfwqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7mi133C54WcaACtyrcA9eJ22wcD0gZpoQlIYEk73odkTE5TTJ43lcY%2FgCBtc9RPOPaRsJiHmODtG3RneEmpqe6gYBh9NiJq%2Bz8t8Ed8Wg67A%2BBlmIM07DnMKzLIxEEjLVYmU2pBp9Qe0CRcn3XdoKwk14dYpegRbyf8uUsPwKbGMRY60xXA8areYMLOJ1CnWgo6NG6485Uos6NewGkhz%2FkbSxUp0v%2FKM5yEbNIGmT6UI6AcOg4gxFiY2ScIXr%2B1qgyEoJsqAudfo39f8Zrsdx4kLtUJVWAB6iy4eVxf6MsqFJscqGUso2jYNMFeHu%2FZ3rcOHSz6w3EWO3OSXmKCYNZYrqsH0JehA3IS97zelozZ%2BsOyIc8K94xofJrC24vO8lkAkJT24I2xf1Ca5jtq0bPJmgTqeKDMcgGhvDrzwk5AZv4mI2qM2QXSwXSBaIYSKqFJLKNE0teXIEkNf7eQxVHmYL3mPAN3EnL4YXMyl8Bdh5%2BZxm8CGOTEjf6vCPff5gcINo%2FX7uHGIHdhAs8w8H4kl01kf7YIDcp2Ip3t74xNiyctHRRimF%2B1wFDvlXLVEbaE%2BBXfFyKDIq%2BNyhSgTE2MoMTJ6tpOnpm988pTbvTCvaUXNb%2BCkyKZRQB38uGxWqCAiw76dd1YhwZMNHM9bwGOqUBPNOriRJtLomt%2BZdU1ooq6b8FD13nXUOvTCPGHzypGiprBGSAKzBRFGjpTYmXOgVa2VcKsKcKXrDZT0MP5kp%2FV3gMpQJLBWovjAd1C76lhcR4eBNbozNWzUgOriU73TvjSqQTNlOiPrJpJ779nNPl5m%2BoEXMblxtf7%2FzjQjUCFTFtn6lGnFttYDxhxa59m9tyoWwp%2FDt567rNN5%2B8x1lnM4eluF8z&X-Amz-Signature=18c1b070fd1232d269a9834d3b868eb2fff5131a8d26712fdff03649bcf49710&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2XLQ3L2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH6zD8v2b3HE3R2vqc%2FbT1bKvboBqkW%2FG8IzEo5HhpFsAiEA71SBI1UZhhFrEU%2B89bkEv7Vkd9ZSIbt3R3OVUuWL3ZUqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDALrZr2saVY%2BgakqHCrcA09%2FW1lJwWS07DYr2oCD3wx6H2sRn5ZXKzjjGPGMzv%2B8uHzL5cWsKLp9FdxLv%2F5%2BH2LJCRZ06dpku2abn%2F29hkgBwvQ%2Bq%2B%2FE0HMfU4DC2JoU2NPsS2ZRsg7ZwYNJKpLoBw8On6jNEt%2BafSZDUOqiAE7TQhLu2%2FWin0ATATxsPmJZgbEkD5jvBLpBk5D66XAU%2BhzvLbSzSjgUSZVFtE%2BCO34KD4Ax3B%2BSj5TmALSRzyP0ngWcQjjVrdkv1waA6W9%2FOWPdJKveawXH2NyAhuQ33ezRQYTvuIoQd5lb72Hm3Ewg%2FVbXBAB0g%2BX9%2BzqXIgbYV1kXDj257prLscVw27h6LqsbQI55Vt2JAgVzX2x5MiBj3VDenXKwjPsTcbqFLXg0d1B%2FcIZ82z%2FwT5EwBk41FhBkUeU0hRxCnf4SB2ukF5uJutktlFlAY0OXNWALqlAokeYr86T3o7L%2FaVFQmndAKEsD0TLN2igCJv62OLF%2F8VbhllCbpj0YpnbKZqPsgUT1Be6BlVTzi%2F%2Big8J4Bg3taeRmplXqKMaE5grstycNg%2Bp2tOoElAZ9C0l1W3GuVdnsnD5rVmhE5F2S9OFaeQm2s2oBnHhFnqq2bMkEfqe94VZMZZoFjtDBln%2B0%2B2LxMNDM9bwGOqUBJIhVeTSJacPdjcEM01Q0hRR9uuJZHVMjRchHZPi9xGrqhcMRhkO7L1SadPlBCYUZK2TeGS2AFEiGx9gARwTHNNM%2BLoSUKUwD6bWEC4fUg64y7zHPcVH%2B7OgBC2KXkvo3W0MtNfLWI2lOUfIlCvU8RS1kASwc%2FzrsIhOU0gmAM7BLJTUCyDgGausytflKFKnjSm%2BbrVRUt4wMuBMX06WYyySI3LbN&X-Amz-Signature=9d5529e580589414980bc1388ef0bee5071917fb1e1b3dc745c896014d0a8afc&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2XLQ3L2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH6zD8v2b3HE3R2vqc%2FbT1bKvboBqkW%2FG8IzEo5HhpFsAiEA71SBI1UZhhFrEU%2B89bkEv7Vkd9ZSIbt3R3OVUuWL3ZUqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDALrZr2saVY%2BgakqHCrcA09%2FW1lJwWS07DYr2oCD3wx6H2sRn5ZXKzjjGPGMzv%2B8uHzL5cWsKLp9FdxLv%2F5%2BH2LJCRZ06dpku2abn%2F29hkgBwvQ%2Bq%2B%2FE0HMfU4DC2JoU2NPsS2ZRsg7ZwYNJKpLoBw8On6jNEt%2BafSZDUOqiAE7TQhLu2%2FWin0ATATxsPmJZgbEkD5jvBLpBk5D66XAU%2BhzvLbSzSjgUSZVFtE%2BCO34KD4Ax3B%2BSj5TmALSRzyP0ngWcQjjVrdkv1waA6W9%2FOWPdJKveawXH2NyAhuQ33ezRQYTvuIoQd5lb72Hm3Ewg%2FVbXBAB0g%2BX9%2BzqXIgbYV1kXDj257prLscVw27h6LqsbQI55Vt2JAgVzX2x5MiBj3VDenXKwjPsTcbqFLXg0d1B%2FcIZ82z%2FwT5EwBk41FhBkUeU0hRxCnf4SB2ukF5uJutktlFlAY0OXNWALqlAokeYr86T3o7L%2FaVFQmndAKEsD0TLN2igCJv62OLF%2F8VbhllCbpj0YpnbKZqPsgUT1Be6BlVTzi%2F%2Big8J4Bg3taeRmplXqKMaE5grstycNg%2Bp2tOoElAZ9C0l1W3GuVdnsnD5rVmhE5F2S9OFaeQm2s2oBnHhFnqq2bMkEfqe94VZMZZoFjtDBln%2B0%2B2LxMNDM9bwGOqUBJIhVeTSJacPdjcEM01Q0hRR9uuJZHVMjRchHZPi9xGrqhcMRhkO7L1SadPlBCYUZK2TeGS2AFEiGx9gARwTHNNM%2BLoSUKUwD6bWEC4fUg64y7zHPcVH%2B7OgBC2KXkvo3W0MtNfLWI2lOUfIlCvU8RS1kASwc%2FzrsIhOU0gmAM7BLJTUCyDgGausytflKFKnjSm%2BbrVRUt4wMuBMX06WYyySI3LbN&X-Amz-Signature=7eedac4f0b9362ab9978837f4935586d2ce295eec5f61e822c0c8ad4588533d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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