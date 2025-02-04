

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAVA5D5O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCwrxjm%2F7CL2F5b67xWb5%2BWmZWQvHOfKxCGtBOPi9cs5QIhAJet%2Bs889E3Gzz0GBBUwgdIBFdtyaU6Bq4seXJUf1aQfKv8DCDcQABoMNjM3NDIzMTgzODA1IgwIjIzTTFGARFduXVUq3AMrra6%2B2EptadV1RgHuoFHOKFuMNAYDrkmnrCwHoYEfJ%2Bt0BsW0z9IzX1X0jtU3rB%2B4osupfzxikMX3z57FFD99OCYht869Edpg0ahUyJ2yCCktv2jvFzi7%2FwfjMJbL%2BMEA2bxnHxStV7K%2FhEooqP60uADyyoASbe5eMXTluQV1HwWbPijNt0qbK5hymRDefghRI%2BOo6EjDoT%2BfWLjT8dN9f%2BYJXaQgBy87GjX%2BAuUk2y0CpCkhMPe1yOTzn5L8Sho37NnJZlNqU3IJRSbdntWtmJudbapxf0tpM3dTbyfMBdN%2BhcLgebfBuefQ77aXnSmWhpuLR73hZphD1g%2FO%2BlS84sGDOuC6wgWxaI1WaaOjpfYeiEZPSvP1GMSJEKUBaFtuYHKtWA4bGj7%2FXRIox28d3Gc79c4EkeVGM6eZpsFmffpVTbzvy8xgMob%2BuVkX9o6JsMARGasHXk2HwcIa0y9wMFVtqw7UDHl1QvlKrfZzLx5%2FQmloPEq065YsOzGIRaB6gV9EWkJn4Y5jJYOtC7aX9NrYAx1LtEF0o4ED8Z3ndDTWKHv3U7rN6idVk3jDW3Qy8uckJ%2Fqs8if47fMHQJ1zs4YK5qLD4XEY0VFDQ01Nu9Ttva6yKKQPc8BCFDC0lIq9BjqkAeAe%2F%2B6yJjMttryrzAmi1NKMWX08AwAVkQTPbg6tvjltNaiE9F7MXwHW9rsYTPWjFwtg1qHQ3WRRhvpSFZI7vnBDoTd96fzyoWO31IRrhTHIkCXMZzSPhMIpVz4F7IR8%2B4wCM%2BAfWFNQBb6Ef7g3OwCoz7CaVKw4VNVvxLlfxj%2F4kB%2F1EEyvLzLut9cueqSKZl2VFToXJkdjvY6EoQk2Za2LnFhj&X-Amz-Signature=1f48e78f9c95b8ed85f3b4e849e73d6da628f0a043d5aa2fd8d7da734bf016ae&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VU5GO3D%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICRt7TTyvDQf%2F7sLHArYAfsb2YzuDb%2FYKLrGMB4lH5rOAiEA9PSlYCdJCWK6V2pAx%2BTLQDKR%2B0yGaj%2BOx67q%2B3Txmnoq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDKGV9uPMO%2FYhVgz1ayrcA2C5zZsR5hXfLFumnL75U8P9BFYRJ5WNhGtsh5OxJdmby9aE0m3KuWWBPBWx3Ho8Aosphl9mQtNlSbhFzZOU6S3YUR6%2FrRKDvDenNgp3HLEl5%2BZhHVFuvDfHtRc3GCrUJqFfuODiLrE52RiKhkYGmRquzX5aeU1ZzDh6Pmv4SGQ6L8n2Lg2uuK2C4rPr0IvuLBCwce1fQSJyzhSFZ3Pqzfu%2B2DPM7F1zvLEkrPGCbtYMa7wqT6MNbhhHBOTc4eWMu0j2Yiij0s3R%2BNe49bbya1TnVX%2FxafTHaT1AKRUoeMQ%2B%2F%2B%2FleZ6rAhxMte8JAKw2WNbjH7lLAl%2FIhEPc9LRNHDIRPkGcRPJ6UhZ%2FvhyG6kyNZbvDBKhSvbr9T3Uee83VqUiWyKKkpIqIc4jUSSKakf6t7Jge9lk%2FHUZ9fkGqMRj%2BxeKRtq4xIauYgAy1uFu%2BaxNsydKLqd636FMIYcOnDox%2Fai18Qy6xy%2FdGcDkidLppbYIJLtNmVykl8jkcvtLYj4vFZvXMgSwmK8r4dq1EBQQG0bosA1uJtMLYC0So6ChTKXwDnzDHx4wimoVZYYAmN735D1OQX1pm2tGrB1uLcqqdTGl1X1Nzqlrc5SBVb8Pm7LWz8%2BfwwF1DX%2Fe3MPeTir0GOqUBw%2FuU%2B1cVxV1ouGIi0mLYtiobfKjhgNXoKAFRf5b72Cc%2FWLZmmuMumgyrs1AVHtBn43QMcLU9x6CjK8JY5OiP4SKFufk6sHj72A1xokBRyXUXclCnJUqHdXMuLeseH7qt4%2Fb3Z85o%2FWhUW1csNqD48%2F6nfl8gsdzwN02MxUBbUHikp5PuRJFM%2Fv4HxNouJIonnICgj1TfpMi8sax7mxuAt2EvhD3M&X-Amz-Signature=f204942a83b07fdef4a5dde98cab5e2c459499755f88bf2a1623f219c5227775&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIRLGVX4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIHfgV9YhIk5Hu9hnHmdxfjCvq4b6EFQm9ZmxTZstAQOoAiEAi8fzrswbugEdpx6wS1MJgW0cJ0UgQ6FmXw8ylsxs8oQq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDF%2B%2BiNSLPFtUnvP25SrcA6xAhNaDH3UeKGy05sviMS21liJTI1mbZ0vQUtl%2BW7dTlDevA%2FSM76ymBWroFcUigh1AtPZU3CSd%2FGLZQ5Zx82q065wV62ptFxUiy2TtyLeNnoM0LefRwq5e9bVMofnYpo%2Bg9b4nD6V7HG3GMpTp8682ODnqT1Jqh%2FoE6U0weTjutAbDMoOIaeiPQkV0LZ2Xrexbuk%2BYYCbUxPXp7QCgHeM4Kq4ZqrpTBHS8nCykg3YEqz2Bs7o0oVgpfE4%2FXO8buWxv0pNuLJNBXJ4aGRJav1AY6%2B2%2BNQm5quY9B%2F5f7572SCe8B%2BncoAjKkRPQTaMJ4pspujY1y%2FNCUaCLJvwuvzXtDUPxrWTk6aMxiIrkW2wrugUGcwxbWTLZi2osgDDLROlBMjFg3oNXWc8lWymRQFNIP2yQ0OIu7xxMWPMgYXLgW90Hm1bUI%2F2hBfzfpaCbUUwHnzXoQIjjAY3FyoF9%2BfWSlN8pTwdzm%2B7U2ZIf0wRXowx%2F2FlOJGELVy6xGMUlmYZ3yu24YOEk9KFrIs44mcEwJi87FkTdWtLeGWSKYJc7jYNjMPm%2FRaJ7DG2pP2Atw5cXwyIPD528wriCOVfVGvUziYbgSCzTsNljiURQ1WCVMv5MAwKEyJktTWOVMJSUir0GOqUB7ZsxGvwFSqKL6IA7sVSJxMu1GaTO5T5Ltf8pHDT9wgYj4tYNhEqYRCjdaw9rOFF6PsX%2BgZxd3M%2BZt4Cmff11qbxD8vxjRpECFouV0IRmn8qBjLazQyzVriIQCreUo68QpmqkoGdE0ooa0BeL8jrdxAVrfyVZhqFD%2FfbWBzsz0844a%2FC0rZ8cnK3WwLSo4i967eP8ex8BwHIYeW%2BrD83mVz5LC1sr&X-Amz-Signature=207823bc3fe0ebe7c01efee8503191ce77d0fbb5b75cbbacd27384f2b2c233a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5OWLP6Q%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDlwJCeE7eAdsnK9Rk64EE4CsKTxVcSZpt4tkjTFVuptQIhAK3igczed2KOye1uLrEp%2F89i37uZtjTnndPCYFJMoByuKv8DCDcQABoMNjM3NDIzMTgzODA1IgwwvvmC0kdv65UjXC8q3AO%2FYGqdpODLnLUJw6xfw%2FP1Ux3kX8BJfUwtsHGBikeO%2B%2BQObKaW81D5kpf4tprSm5JPn%2B6N0anLUMI3MAO9h6aVNfP3N4%2BXwRWuHMngkYYP0zYnHwlJOmie34AlqmIUSSg37hL6njnBoSKmAD5gqxmh1gGOg1zFwenVt2YSjkVSJuZEYgDoQZQZOVyDP5d6011QyMeEorwNBNWa7bFfkG8%2FvGtyqY8afCQhSWmYP1CT4HGascM8nlVHTtkAa%2BTg8UmOk6vu6tLp3u%2FnjZE77fJ5VvnLvYbarGYfv8MYobqpoCp8C%2B3lbZhh1%2FYbQJVHyKeS%2BZjAojRLF28SSkt4vJD8wRugvkMVgmMxCbyQ8z%2BvcSFCMfPkrMUkQ%2FgEmqRtSMq4khmRg5%2BMn6giLBZxDj3I%2F6DKO1U4j36HqIdhKXhbAOMtvm39zgNU%2BvG%2BFl%2BR3bst%2Bygbl8I%2B79yJVNWIfMdHs4PGMsbMWgwDhJWWtjNBVte8ACT3J2TfKn9v4Y9cVjY8YsZUgjkXHL4%2B73vfaZ7xYRHNEePSPp9Sz8GWgCKzk%2BMi5R0LUpLgE3tDv1PzrO6WdKvlX8S3LirCi%2ByaCLB%2BS9PAwFC3%2BRjgh%2Bzl5hBEtFol7TbxSN%2B9TM7GvTCUlIq9BjqkAatAYLhXc3g64RpNOf4gVgXcAl3wcrLRtaaj9B8QcJWhueK%2FTA2AQcVuLPaUVwE9GRf97Rhq2AGOUIB6JQLgHDvORrbRNB0CZoc4J1MGcRKkNUzQ%2FOHJYg6ebrq5v6b%2Fr3m27R6%2BaRzlk7FX1FEaO5fbXl4glmfWJJPhDVrO%2BOxslZ1cTRmCsQqbwgPGqvj3Gex7%2BGtCHTtKgSLVlyjLqT3kyxVc&X-Amz-Signature=8c94faf3b54b0bb77bf7974473ac8afc729049e7f86d1e3cd76b3c0d9169c785&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZGGAZGK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCICR2giGxDYBSbLAkPS6WPpQ%2FgaBcOOZDLigumz0UtiyvAiBXhpghznoIIBHQ%2BiY8laG4BRvYmreRcLP3xPs3pJW%2BAyr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMDsrtiBFC614gZAg9KtwDHpTD20BHg7lWu9RryTgOtGyHDa%2BkyjJL7M2%2BtBxpSDcU81pIRRh6kIdIA7m5sLZDS50veVImLOVtezXgEh6vcMNk1NfH0g3XkSZCL4boQiIgqpNuA%2BjxWiIF2ub222ExmyggDSTMIhtr%2BJlwJoyfx%2FBjXkNoJY4lDnXvq6Ww1JKWzs%2BElZBFGuCXC1yuB0tfTMTXp1U2fAifOMWyP%2BlQOrMC%2FltD5sglIGzbvoBcKllU2bcwb2bXJX1KwrFl%2BNrA4o8UKM7Z5J2YLS367maEebGNs7fGczOk%2Ff%2Fqtu6JQmeQJydVaVM6JAdGp8p7wczeSWZlaS7hIZRSYT1F7RDnX8lShkTAzut2KYgafObHibRDdTpPdBGIbw5RkukA62KpzGHKgp3I%2Bs1th1nl1LhAS49OZnkp0mbqmLO9LpASi0vGnmeuzobQvaBaJf9OqPUUZQzf7y0bGVuasP10%2F4md5%2BxBqgssF2nP2KYI9zahjAVzBP62Xd0LwBJGCQzY0E7%2F2rrQzgvDIX8taVQZn%2FwjeGLyTyTTuwHiMe1LPUB%2FNGzy4%2FDT6E8OBR6IvFwwTgVUdGu1mbqp4o6xnMn34TaavFuKbGqL1B5SyZEpcuVFWSXZC849tWkAPRCUqvswlZSKvQY6pgHfsd1YOJEWT2myC%2F8muWUKZeYcC8ADKPXZ72ztFHsvqsDd34VuytZfBkfuRg3wFijq527kHhvSgXEA3Y2HjpxRvLlWVjTzEPPFunNd8VqlEKM89Uyv3oPRxPbcAVJrN4vJ0M2TFEbY9ygIsnDkZ4HVCFB3E5RQUBkMFaKhKqFj8QD2HLPHZpEZkzGc0Bd8ZpmoNjIn92zcC05CSxBSKZmeATQfePo8&X-Amz-Signature=9423c097160b18ff3d1c0e0473435fa891887ac9982fda0a1e5c0a4917648532&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFFF36HR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDLsC%2Flu5hHVO8V8dhN2iNJSQV8YbMYgFguLIINMOp27AiAaPYMxSNMGRNe8pEGKjPyd4tf5QpFBqbg5LxUcN01nGCr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMHYREcyjkEo%2FHWMHoKtwDxD27sGT2sZmrrUwDfirDKOKDKdTdHZpqUJnPaB0Jq8GXHYIqcPALvOAua97NfRfVWFUEpBvxbYLqdGqNT2TtDexq3J3piZqY2OBwrQ7WHQjetOp8jaAU3G5E9C4r%2BXWR4axH%2Bcwzdirf71NHqoMZHZMCr5f4INEyYacC7Pt4i6%2F4vtHvtQMg%2BZpmDv59YAqsf4nA9wi76opoj2%2BT75K%2BtF%2F0H0hXT1Hwaq152%2B8%2BFCzBBCjvM0BfWkOlEY1x2VO3PJdmCAkJlihyvq0uV54YAMEYRRp7XYVVMdgdJCu6abG5WSyBjHzitmqQ5kJGt8IR3wSmbfRwhh5smyOhAqhhcnCYxISuLfQEIIBxxp%2BS3QH7Zw2uVP0XTuOLjcQxTXMjAJIpMDv%2BXD7HRRwe4daagy8JccY791aaWzsxjL0kTJv0qMNiUcVdeGMxzICvyWKmNjS12%2F9mitqjzjaPThW0SgToUxjYM7zCfOsOutQJOhrgtzvixKIJZNHnB2JwwVIQA73BN7F9SEx3x80BZaTCk8jw7fDJE5rpzeoV2qgNqkOQPGm6vynYQa8drvIO9Qxplg9Nj68FZZ8QWocrSAYzLL%2Bj5%2FWLBpC1PIywXCfE9Lv1tlSLpvKiMlU8a8gw8JOKvQY6pgEOpI7JWDL%2BRQAoAa%2FP4Olyb4ICEamh7eJ0i8uH58x9DOno7e65Si5rpnT4OPG12vW2Zp%2B9pfeLuw%2Fl%2F8asvuXdGttBcvZzS5dVtnFr0oiN%2BANEBe3UsUR903reJouEr%2Fxzsv3%2F56r8bfzPfbKf2MM7oIYzZqsvc0clwxg8Bzm%2FHShWeUnD8OZ61Uvaby7rbvsIm38uBF9ncWPP3zgneAJOIXtNv2Np&X-Amz-Signature=7daf252643b579849682c251b78df1d8342953c5af41ca1e9bc4550c5ff5081d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZWLXZCP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDL2Rcs5uQkhNbTzDhm6u150tbKMV7bJKK6IacIPEnc0AIgVFWvqe0CBw99ilJtJo3s240KoYr03S3w9QncC8MSg%2B0q%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPwTkHxclM%2BQjgxAiSrcA4EHxaP7MgJF1Qkb8KLHqbuzhDLer7D2u5rdnUVn0csPfnBDYremeyL4nCSuNVwGw8fJoiU%2BvK762V2eUDZzZaAIPExbRG%2Bb1n5S0seJ6R2DzNjA5U%2F4eYL5lCi0NHfjKkSnZhVEP%2BCg0XofexQMuV1N%2FNNmCbPoAfHnbpn2ypKIckuLZ16VlY6M6I9K8iiIgxnBYtGAVU8XzyWFYXDTPrQe9RP1Io1wxeo7OWHTyoiScP4jyKwpKYxVujjV4OrmrcSSIDPam2MgnKZRszzoGyez1wuP%2FvNzQ%2BGjAHicxBtfELlV9VKKdWOBetxfe2TnZOuINwtCyWC1cZ2IaQ41d67pHDy5%2F9VJsbK%2BuLFoHcQnXRn1zephgUIP8%2FpQwFkrYYlUtWA7GFm%2FTRiBaHj%2FJoUWF6ZbKHKknZaYreSPxaOTmRSK0gdgkXfbYGcabgIuYgjyhHf%2Bv1DNrIVWGBIZ%2Be%2BIkupJLm525jAsW4IUOkm%2FA7kfkwaBo2zWK2Hi2T%2F30bIq0QpZ3z%2B%2BsLH0MK5r4PdQr5Gv978AbC8HDJi1ntabYKxTQk8GomAeoIkx0N5nnqDItNElaVPFvbcENAqTT2WPn6AhZKqib37qSiOG6XvEcw6X8st8Z96m2E3QMJWUir0GOqUBeBMqCLxbhMkuqx1XO3emmTFXuNFEkc3PVA%2FSxwsPQkB3p9v4fXRvJI8sKrVCc5Z%2BHdZmn7XppIDb7hGEZnL1c%2Ft6rPcwnzMlfaY%2BiGd2%2BCZzy3Js9bitFL%2BeWWcRED%2FgRPv7kU9L8L53TJPF4zdgT943ylg9ouy5UwB79WlavcEy5RT0MU7joVFgje3VRDekNliJZCedXzWYH18S8OFNCoCBuCen&X-Amz-Signature=861537bf6e29f412c121c6870cf31878868a3d923da72a914bc6e69ea9149730&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNVLDLG4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQD2RYwaSolr7%2FpapRJqU6DXHahvXfa4De%2FH28csulMIhAIgPBLWKBNqzdg3JTXhZZBQiEZqrNnehVaz%2B70LG2eEWdMq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDGDI6gf%2FC3pMEqfqNyrcA88LrOrIM%2Bhjbkkb%2BNug%2FTJS%2FXmAputcuD2FJexz5N8ur9XnmSBLF%2BVhxK0xhTDs9oRNyzemQEz%2FSV9ce1MB03Hk92ruN1LwEB27qOaV6c4Lj5grsmQ6if9BbfuG7iXwVk8sXywgFsYACPhrsI1wCudE8CHO%2FZkbBARVc%2FseAySL%2FTZZ1nwZxFncgYNgSwdORKEUavS%2B60dazxuVyCoTsObcMKYx%2FSz6zYSXYO5nKWa%2FTRCthBLNOtuxwkecYcn9RzpV9CNuJR1D6tG0yb5OAAa3wt5xYiq76TS4CZ4eCcPv8Xx69gIQQfTyZHKX58nArfz72OSNL3eqpjjkoH8a6491Muj3Z0JQDZXsoNbfbIvke9pISbjMVGN27kRCZL4kpAjnVR60agz9U3eYGJLT5g2z%2Bqbr7JZKcxwM5ORRUMqz5c9wUys2D2RoTtuw7HhszrBUIBVHLh7ZM1s0xVNLdu9N3qGyZzMIdSlzNJWIOCEe0puHt2hYRDN9loRcPwujpKLpMsjdRdUaXDZmr%2FXUTC6e2wvHnNX9TFoGYCJgRh0qua7AwowAxnEHGF3g%2FGMVhPw8BuEAgbskDZ0bTiKAnYLWI2Dqyfct8TQsLZNux7mRINVJanzMj%2FlBv37QMIOUir0GOqUBwcZe2C%2BGM86XxIQJAlT%2F%2F5nsNEpN9IjlvhEE8w1d6c2MJ1uO98AD3HTcwTL9iBA%2Byhw9A8n6cNnBEYEQpCO1GIf7ORKxKdSWm063RgKuXjLVZW%2FQCY%2FF1QPqBhjI17R4Nd0%2FnxsAuinmECMKznH0C0Q1jV3NZGVa6t%2FizZ4alOw0viPxVShXk6L3CfA%2FsVDHpAWLFgICqXWqLNVhallSmh7ta57f&X-Amz-Signature=9975ee44971312efb906467bf6ca3eb41eadbab792715ac90afb1e469d547d78&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZGGAZGK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCICR2giGxDYBSbLAkPS6WPpQ%2FgaBcOOZDLigumz0UtiyvAiBXhpghznoIIBHQ%2BiY8laG4BRvYmreRcLP3xPs3pJW%2BAyr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMDsrtiBFC614gZAg9KtwDHpTD20BHg7lWu9RryTgOtGyHDa%2BkyjJL7M2%2BtBxpSDcU81pIRRh6kIdIA7m5sLZDS50veVImLOVtezXgEh6vcMNk1NfH0g3XkSZCL4boQiIgqpNuA%2BjxWiIF2ub222ExmyggDSTMIhtr%2BJlwJoyfx%2FBjXkNoJY4lDnXvq6Ww1JKWzs%2BElZBFGuCXC1yuB0tfTMTXp1U2fAifOMWyP%2BlQOrMC%2FltD5sglIGzbvoBcKllU2bcwb2bXJX1KwrFl%2BNrA4o8UKM7Z5J2YLS367maEebGNs7fGczOk%2Ff%2Fqtu6JQmeQJydVaVM6JAdGp8p7wczeSWZlaS7hIZRSYT1F7RDnX8lShkTAzut2KYgafObHibRDdTpPdBGIbw5RkukA62KpzGHKgp3I%2Bs1th1nl1LhAS49OZnkp0mbqmLO9LpASi0vGnmeuzobQvaBaJf9OqPUUZQzf7y0bGVuasP10%2F4md5%2BxBqgssF2nP2KYI9zahjAVzBP62Xd0LwBJGCQzY0E7%2F2rrQzgvDIX8taVQZn%2FwjeGLyTyTTuwHiMe1LPUB%2FNGzy4%2FDT6E8OBR6IvFwwTgVUdGu1mbqp4o6xnMn34TaavFuKbGqL1B5SyZEpcuVFWSXZC849tWkAPRCUqvswlZSKvQY6pgHfsd1YOJEWT2myC%2F8muWUKZeYcC8ADKPXZ72ztFHsvqsDd34VuytZfBkfuRg3wFijq527kHhvSgXEA3Y2HjpxRvLlWVjTzEPPFunNd8VqlEKM89Uyv3oPRxPbcAVJrN4vJ0M2TFEbY9ygIsnDkZ4HVCFB3E5RQUBkMFaKhKqFj8QD2HLPHZpEZkzGc0Bd8ZpmoNjIn92zcC05CSxBSKZmeATQfePo8&X-Amz-Signature=c6fedd4965917eade00dd69741f5f6e95eabc0b7adbea637ca12af32defbb0e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SWXJJTQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQC7T9Zn%2BlocpmyN%2FH8e9aon5smCAeZE%2BzXDBCpnmFQ8ygIhAODkrKTEdA3saA6tCM8hc%2Fq9P%2FipNPmKaHGMSv2ikjL6Kv8DCDcQABoMNjM3NDIzMTgzODA1IgzLfcrdF%2BLe7g5IFJ4q3ANdDpodi%2BA7NHjKqnYdHENPZ%2F7GdtBJYb4mNWywKF2XL58Z9pYLymUjsfCKRqo5JwLDpdv%2Flw4rDHzk3BC5M5LEwvty2ksfuwq%2B9mo6V405Kjf49TsXHba3wGz0ceC1jS2jzJ1culTrGsvGJjcxHRNXxqWN4eFr85LLZOK0HNIyq1XzIabIr8LSiEC0Bw1XCmNOxgXIE6wkOmhl%2FfV3dsQMh73cq34I4yELrMldmA6s6CajPeGzKJvvmtMsZkfmipHWUfozDVwGwNCQim9ElnHqebgF1Cl1KNdXBb2jBF165yEErx3Khl5k%2BT%2Fjw8fAFawIDaFCPke2JvyWdaQqu%2BpdA%2BlN06aHY9iMcQCWX0Q6jnXR26mcSkyl2%2FO%2FmO0sS8mCGnyg6e%2FQST%2Btlb3jv7nyjDzVA8CMNvI77StLnTjJMIGNb3J8qzItAA0WYveAW8PFgHw7sVHkf9inMtArBw8Svi7VjPkwmk%2BU5hL9sT9JyIMXidtQRGFsJYOe4TzFxnTAeljkUrnhp8MKubsaT2l%2FuxnUnDW4YuQoG8%2BUOz3DVHtC%2FbSMSHmEXqHZfIPpucTcdlhZ%2FezZz3xiJ6Jop909f5DodpdQlfVUgEcoSD2qoNHc2kcLNT%2F4p%2BLu1jCLlIq9BjqkAYghFZSd2PFoieQYcoMGedX5rce32AYXV%2BGVwXGoyEyay7EzWMB%2BptTaym2lq0gd7KDMN0VXCNLoTStQYLq%2BlxYtOx8oZg6zQHmaOLLmtWJAKAa8zoXgl7IQ48JndCkhDi0hhx5sNQedgLNq5N%2BEuq%2FWCd5womxkZJFuKvFT4Eipt8I3%2Fr68qxufbh%2FYVFu2DlF0zYgTthg6ky09tNPLj2BZ7F10&X-Amz-Signature=5c154aed85107c224ad587ee766a080b7af28a5941b74a0a44b919785ef2d9c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SWXJJTQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQC7T9Zn%2BlocpmyN%2FH8e9aon5smCAeZE%2BzXDBCpnmFQ8ygIhAODkrKTEdA3saA6tCM8hc%2Fq9P%2FipNPmKaHGMSv2ikjL6Kv8DCDcQABoMNjM3NDIzMTgzODA1IgzLfcrdF%2BLe7g5IFJ4q3ANdDpodi%2BA7NHjKqnYdHENPZ%2F7GdtBJYb4mNWywKF2XL58Z9pYLymUjsfCKRqo5JwLDpdv%2Flw4rDHzk3BC5M5LEwvty2ksfuwq%2B9mo6V405Kjf49TsXHba3wGz0ceC1jS2jzJ1culTrGsvGJjcxHRNXxqWN4eFr85LLZOK0HNIyq1XzIabIr8LSiEC0Bw1XCmNOxgXIE6wkOmhl%2FfV3dsQMh73cq34I4yELrMldmA6s6CajPeGzKJvvmtMsZkfmipHWUfozDVwGwNCQim9ElnHqebgF1Cl1KNdXBb2jBF165yEErx3Khl5k%2BT%2Fjw8fAFawIDaFCPke2JvyWdaQqu%2BpdA%2BlN06aHY9iMcQCWX0Q6jnXR26mcSkyl2%2FO%2FmO0sS8mCGnyg6e%2FQST%2Btlb3jv7nyjDzVA8CMNvI77StLnTjJMIGNb3J8qzItAA0WYveAW8PFgHw7sVHkf9inMtArBw8Svi7VjPkwmk%2BU5hL9sT9JyIMXidtQRGFsJYOe4TzFxnTAeljkUrnhp8MKubsaT2l%2FuxnUnDW4YuQoG8%2BUOz3DVHtC%2FbSMSHmEXqHZfIPpucTcdlhZ%2FezZz3xiJ6Jop909f5DodpdQlfVUgEcoSD2qoNHc2kcLNT%2F4p%2BLu1jCLlIq9BjqkAYghFZSd2PFoieQYcoMGedX5rce32AYXV%2BGVwXGoyEyay7EzWMB%2BptTaym2lq0gd7KDMN0VXCNLoTStQYLq%2BlxYtOx8oZg6zQHmaOLLmtWJAKAa8zoXgl7IQ48JndCkhDi0hhx5sNQedgLNq5N%2BEuq%2FWCd5womxkZJFuKvFT4Eipt8I3%2Fr68qxufbh%2FYVFu2DlF0zYgTthg6ky09tNPLj2BZ7F10&X-Amz-Signature=ba900a2086c40db57de2b9e0056eb02c642056a1c3eeefadbd2b7c9ce1f04b6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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