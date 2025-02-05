

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSEXZHS7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCURSq5MU7dAR2MEmhGfBWispGQ2%2FYinVbyK98BXE1A3gIgPuZ9jerbOXPfcOxhqvq11La7EWK1IYTs6pwSTmccN1Eq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCF3AEnGwJ1ruMFaKyrcA3XnjpFyYHAE6LgYx%2BbRvHQBCeA93IpMyweSvqApzG4V0x3PRYFDWuihqE7N5bV7MByX%2BwKIKCL%2Bv0tOiSC236%2BPyS0end%2FIvGYYr54Otgu84dkve6pb5ff%2F3D8PjYY%2FODvwtHBNWaknb5hYw8omLJo98V3O%2BH2vq1mp%2F1GQ%2B%2BrMZ%2BmSm%2B6wj1W0HCDe8NLR%2BnoRMdh65W6%2F2Cl1X7xKVXGZc%2BkvoNBI%2FkUYuMraJ6xRQzQ%2FVtQTVsR2Xl7Iv87nB0kaF6IS42PiCDYQytgoAfgGOAaoaZR4YljKuUzlk9WWwy%2Fth%2FR1S2fBSVy7mxSoob9%2BToJkmWmDmUhDdLqAO1z8X7Bvzpo1fXWRj%2F1AfNqjRloi42EXJoUy2WafeMIrIfK9NCLEOo7asDNVKj6M4aDmSjl2Sl3keF24%2Fob14HFXNNZSof7W%2BeqAsuOftdKZle2vjAUkOhd8KOgRE1PtXLYxEK%2FBsgVr47CX7KhFmFNeeqVfSeK%2Fb%2BjYNTuyOIeiXEF%2FK9l3g4bFlp0o5BXR8Z5ofnQ884staCmilEBK17VazeZp68naS0glJKP9woCRJD9ql3PjBI02hXYA9pZMrkr4un%2FNtmSEMBs%2F8Yvlkqzvvae7NSUgQDUDbLmUMNaAjr0GOqUBzSYoqJiN6TUjpx3xRqnENyICSd1xzAd2ruTdfdAiCcobrTqxGaoG4oNyStcviWESES%2F7is0BqiNRW813HS7%2BVbep1ZwacXa8zPI4PIPspq185je9Fy27kBRiasjYdp4JembDlqyhjMrP2aZ0qr7clMzPt5uj8vkot6wAuSbX9RK11QRE3PHqPoTKGkAikPP4BBvT7nYwkCIczPskEhRs3Qhb4uc6&X-Amz-Signature=7683b53c7cc35dc870ce4bf575679c2525a596f521b3acffc15db61c8c2ca371&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUY6NKUK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDC1mNZCJX5M6a0MPPXsP2jvcgzs1%2BaaQ7Cc8bTCNFARAIhAL4yJ55JCpj%2Fu7KbYA5Zby5KuGxz3Np2HCYrNHHrrxbLKv8DCEgQABoMNjM3NDIzMTgzODA1IgyQcbODWYpeV2vUKk0q3AMrFYaBnAxKygQn5Y2gBxi8MXxDF56fTMrcyi1SIvMpVB0JeA78HqP%2BhQcfTMEB63W%2FMYuPms7EfRd2%2B%2FvGbTkEEL0tE%2FPcHBCtnekiWavFbhPhsS%2B97hNr0qUWcX0fAFFoSsal26hUTpwwYGoI2HptV5WvkFvxOcItZ7TfF023DhQ7HvPTsOupTVkJtzIvqPpcOBhMHO83v%2FRgx1f0vnwsUc7vgZc2xZ%2Bn%2B%2FlVwi8SsLllGzaoSLbbHq5IXKie%2Blf5yZ%2B0D5%2BvihtPJf9cR1LCNvfV8AZOYj6NS%2F6p%2B3aw0hj9gkQeMp03GaWDeYEKV1KAPWwuqYcNjqj1XOU%2BSLWKN5ibWCd8vLDxdubPm4FMrMLVUGUSLuQ5XeyQeW5X9SaAhllCoSW%2BPBznOIQZ4qzOaTYzZcStP2HkUo8dzp64n%2BCMYMndNJlbYXV%2Bz60k1TavVO3hLHRgSDtzHiaLlOfMBgn2izYs1B46DRD%2B8HnZvM0LVEF3kDJUsR7MgHcluN5IBKDUb66X6a14M8hmaCH2gR%2Ff5QNAT7HaaGjB9quJwCrG8meoWcPvz5JjHHdzg4469yXxRPrDJcEdYmwCYkpxCMbUK3YNVwETaitUX3r2EiM1YMejPkMCbgw0kzCAgY69BjqkAZY0tK0ppH0%2FgKqmUp4BLSj3%2B%2BVV3dvtwLt%2B%2B%2FbNAqtfFebZMdFZ6cRS23qWJKz0HuVYIp19VsKTb8cjMR%2B624BpbSOv6mJWBaH76%2B4Wx2sR%2FW0aH8aBRaJKPtMQItQRoJwD7OWYBVSilu5%2BnW8D0oe52abRn0BlqnHNipdzBcFFUjmoc2Er4XQRgOQJguEpY53efTvpKJo4D%2FhabraKUqKg7L7G&X-Amz-Signature=c4d9093f8952b06d43f383a48f6a6c9d067d19e0241474199561da18479dc5aa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SZVRQBF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIH7WxgrIMHs3BSW7JrG8lu%2B9rofy2jnhORIs0RSatSUeAiAxBYyRdnpAGstFCrN6CPYgIbArNXMK3KbVMUQGKyjs2ir%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMk0JVsgHd3%2FIfznXVKtwD6%2BqeZSS3wIHiC2wfo1HremnN9HWZ1qEomqq1%2BRtrCS0uSdC3DyEso5ODO2p3r%2BIbzkPeVdos8l4X5INwcXhK4x%2BEm9d87A1%2BB7r1o7B%2FTGfr7GuK4XCPLbPxvFRLYoylyliP9IEYLQcPa8nscoRXsSQpO5eqfQtQOGHntFQ81IRDtPq%2BZXl2UTZN4TbdAa7XU3xNX0QcFjG%2BEURSNjbETeJkuJfHDPfZUXXI2nBeaqTWFiFAdBfLRjBGhHWgVr34pHKDOscQ524hwAEaoC%2BVwQABkifgcXiYNQzxKTUrGbrjDriNk0YPzsUXpIu2tZDRIr%2BvlGFTWrOdMqKPJCVNYZTiJ3dosWd%2BexPPcA%2BSCz8K04d9rjq44q7JFEtrh%2BOtiUamlPQPQPq8AxX0wIx3hvNcax5LPY11Oc%2FC33cxUsGrJ5TrmCPcfDcn3yxJNH0LmQImxfmchl%2B1dx3I%2BzkjK9fVN8Ns7QvCVhPCDyISJVUd9%2FMBZrXXmXLZNL6IJqtIAJTiqXXkTlfYEK63WPpyyX4if%2FcvqvuavilWWEH0%2BJNPqDNkh4ouPROS7jNwhaNLcfcEz4G4MN4lq2A9fC2s4NZdmA4cRCibFeQAtvZYy0ZOsTzbtvck%2BGc0w6Ywi4GOvQY6pgGhk8D6QFgZK%2FkCrtbW1a%2Fd7Li7wrUnDN5k7l5S1eXKrC%2Bfza5dC4zPXCRbbIscgS1gxbZ5duKM6hPgyf5IdyY%2FuFs%2BMkWJH416z2AdpIc6MwrhmYz0gn8VbwbFlHPNhR6YNXB7a6ChDRxZPODr%2B%2Fc7cG9tYwv99XPoAd%2FpVg6KuWbIG4PtP3nwz2su6lgmiQ1BmAW%2BEXIS3C%2BWZQZyB6e6XfiihVSL&X-Amz-Signature=dfe09f7aa9ca3223edbdb4bdc941e89f186219a5b5d1c5b8d2dfb414542f875d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667L3WTOR7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDoOigukM0%2B1%2BOtEqUoCzZ9lxqCd6tW598hhRqnmGlxSgIgTMOGGtk1JSJ05Ln65zllF5JFXzxEx3N5U3cryXU2%2B1cq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDFeewbHlc9K8tior4ircA2m6BPrR5EHfp%2Bk172bF3t%2BQX2EcHKRfn0ZDolqIUfV5g9Jhn3GmILCrVxnIQfMk5BieaS%2FLRv5F4sxZqKLddKWGNVNzgKGWoowmhVVNBI7LFSZeGa3h%2FotUcRRwDBMLXtKmf0OMq96YcukPK%2FXhKjEX8s0AJdRlNqolSQVRVWbLKDPoncMyE0v0e4Pw%2Bbqk0%2BlfCMRQpGjY%2Fw%2Bb6N4n3wMp1xAuIyuUg2QeoTLE0c7S4WARf6458aum9uoLNya%2BFSGu3ASbBQxPWOVdBwyMO4AxcwToz1X0mDLEgzg7hA8A13yICvkSO3LQfCHo26oU6f0ZeWk4X0V4qldUkBmg09homOEX%2BPl%2FF2oB%2B1lV02s53%2F9%2FRFxHe0U9Gd3mRgpoXpwCoa%2BjmEOqvNnnz8PyG8gjdx%2B4EfRbMgUFmrbHrA7eTCoW%2B1zdcLfzhxY8QOJIdrnYm9FUpsEUKB3CCKKtBADr3WctbEYj3s2tdjd2EAsSkTcDUh2Y%2BKpvSO7fiM4pMNmMhXMCZS5VbcrpEu5ymBS%2FCElLzQBMxRNdIxTR1b0vB6x7aV935ZVSbcvcQ6BL9RGbVhwyvMIt9f0hXq%2FxZ74LpxmKKdUps5wSpY5NxDnbTyKTo5CkL%2Fa%2FKF0NMIGejr0GOqUBN4iwGv%2BZDTs3uOdBoNW0J9pSg8ktd7tKACKgAagmDu3YPe%2Fnk6%2Fl3FuZSIuFrAJCOM%2FZK2MH%2FqUdYiILjpYtHcVkD5pc3%2ByHad3sJETPlakuEy0nahN%2BUb9CwS27MX8WBMonMn2ExOHmT%2B8Axe0NmMCt3XhH2clQFbLrJPHR9RSk1awMVSJ9rHmyNT2cTTjuLs%2F2Ih%2BUsyWUpYC90M6emdZ8xnuZ&X-Amz-Signature=1a7c6627a5a5655fc9fe1aae3119062a538960ce155de8d2b6c02b72884d2b55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNYK6EG4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDdWiTOtoaz8BoyWLz949IZ5kW%2FIYmaUn%2Bfy8uWZMSCxAiAMn5FIKFUEl1GVOMgb38E%2BldZcZYTFPMIjq4KHtas0jir%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMkoAFzWGPDhaGFm%2BuKtwD0GXqp6CcK3cdCOywKjIJHUKSU4RgC4HbOSvwafdlFtgH7LJ1Bq4OOnBLJuMg862WrnqD6%2FDIsi7OxPZJEojmj6dMwEme2d5LDcfrLd37MdqgOQxzFvSv8CG19DMxHRdiyETP0zegcnjtdJbT1D2IdEgxFViuQBg%2Bi1PeBckbk6Mz57zXmTzwi7aEBtSK9IFI2zI2ayaIhhGioe5RL5nDaXH9DMZZCmbpRTzDQRiVOGqYRPvG9CPx3B%2FWGOcF2VJnAfvYfdzIIyDETTjEOswhIUqUKkgW2Id94nqvhJcYQZo4H7rZwfyCQ1n0F%2BAhsiSP2whl6pcRho%2FkZ2ijtqD0pWZvYmz%2By3z8C6w97ROYW2In5voqXOVtzS62FusbfC1JKnECKznyimoKsthKsUw9FqHVpzFL4QONIlvE3PeyhLN%2FEbhO6zdZ2PjiziesBqhVUZy1wgVVv7ezohm%2FPGEP9CEeMrCxh3XgsYBP4U7ioh3Suuoz9ID216P4DPb3AmRV3YMbHCXsjxsnBDCX%2BUwYLWWpZRvtaU0%2BoiIaapKhgtSurV2O0yJyCdvnr%2BpzZMmnXx5er6Q2fNjtB8RB5rPF10ZvUI4XIpa8zlbnZPVFbiuBfeYJnI7yfViaL68wyYCOvQY6pgEtJwdehJ1V3DlKfQUQnnT9rdtCqVVmUsT5Fbwa5lfYB7JxmaIaKoU6onEdcrrrnDTIbemMkb7wfosd%2Fytdq%2B1CnUSRglOtfPVKLjhVvBie00Tmt8Ky8w0Xu1bWDchYCPaIrdy9C9f1qe%2BtrqZ0w0UGL0Axm9avXWlFrS2xT3JDvgoLrq8eXrTCAl6Qh16XtlB%2BzEq6CGQ%2BqB1a%2F43slVOoQkDpi7RD&X-Amz-Signature=65f2c47a6573a45ffa0067c1f46abb455a064c697a12c96d2f1f3400532c1fb2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674UMNF6H%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDm5dJhFOu6is3YZrEmZUgNgm3ecphATKcLBnE5hGoLcAIgM0dZwiUGKFJCHwtjPrZmmymrMarmvnxYauZY7NFmYqcq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDAYCJDysGUfd%2BEqx8SrcA5kPmJgUJUV3XiMO5i9KHbTylHZ0brjVYLC5rH40tnyKycqtR35qkHcxnWRi6B%2BX5Wkcai4V5wdjOvFrM%2FJxhz5WBqlrrZxkq0oy%2F4LfqpfsIzKZoOAwc2MjLJcE0HZRKQGDImhljMQaUyd0fxgVUfnO7yJ8R%2B3yxhPu%2BokotMesBDzyhgU0urEQKhEJ3py0gGFuvTImt4HxalaqTZOA55XQaQjpJWCsLhCklMECpPSjkzwDpYoy7mnlIIu2N8fXxQAaV2LbSdFdaQpncqH8RW4vqJCJLAqwRMaA4kEzx4NpEfV%2BGqOVzoNLg92zjgMtfOfcMDsAsnvPJ3NBXkgzUNCv8TAU9gPqXvZmas4PZa%2B0rEmJlck4RNEl2s3lsLxVQLZglYK0k03Hiw7vAnHS3L3qgPEOl%2BMXkuDQT3m8IPi%2FVVcXklbuvPm8Aqr2S52YdWheWttXBzNlZKZqXPrkVvKctOyRciRoKY9xjAkHtCRLa7UkgnrNcD%2FQ3zsCdWFeqfqlaikB2moPPdcKpGyUjkqpb9qyuTwdB8QHVCdrLdKJJpFMHYgObARx%2Fry31EsflK2u6yc2ocxxzJFpWWsHrChwL3eewDf19MddPV7J6MZFCV17Ie3EeaTOdxZfMLGdjr0GOqUBiOjclGH0bC2Tef8fqMsn0ueis1P8CLt%2BE4VDOux6%2FNDW87Aj3wzym19FC%2FZ3yiFy1kR15enJld3GXVfRDKgkTdZMGR929PzAqSWuGeF2SRS%2FSy%2B3qSeVPdErkAtbiqcAOSsQNQB0Kgufr%2BBnzIZismXl7Gm5PRPtLmnOsK9AFlNZ1ByCpJbj9s%2FsHeJ0nW%2B%2FwuVesUpnChvJtTlDC%2BCLDKNKYT7S&X-Amz-Signature=45c50da6057629b810e40c5d3cb7c9c5293517261fbda86d6405259a527c0564&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PD5QBKH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIAQy85pYtQfaURIfdqZdYpdAD%2FhfD5s8KWtguZoazOtXAiBKIoMAKjZHH8UiMWPzpbsklY5gofQqI9Zp1eugO4dxzCr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMLuMl13PA8qC8Y9PyKtwDGdnK7AwR0cVtGWvXK3OyDj4%2BX%2BAqF12V2Hnms1hdoaQ8rzafA%2FGWCg%2FneLsFxTFt%2BRnc9%2F9PdYftbEeEX0zMOz9x5Y1x10eWiCo2fCZ%2FHQAr%2B5%2BncH5bPvRSjzkOis78vApEEhuGqseudQpsaK4ma4w9j0giuJmC5w7zwd2de0bOlV%2F7CyHe%2FOdgwxS27MIjwhmDFJMb17wFNdHa15o1Yxsa%2BJXJ%2FLaEglrCsE8t7oOfLiaKPBpuY1fEv6SU5ta%2Fsz12rELzaOuaZlPP4Yy0z%2Fvw5CBaibwUzGVoVNM1SpoFzkREhOuYWI%2B%2BF%2B9FUP6kq8tnpCJFB%2FyDMs9oFkryHI0QvooeUtzA8BxzPAQckYhU0anNln6cDDo5cNgdmSRXwPdksx1IPkvHvcUTRC37Fajn0wMams8fxsIBr%2F%2FWQAP%2BGy0kVkCf0%2FbAij9%2FgN396yq0YxlG0IB7%2FS7tOx4YHAQEaIqrfriyjYCxiGqcWRAIusp0vmv4yGvDrZjXh63m16e8w4H%2BHIyw8TcSCVy3weFKERohJD7%2FBiOVhWofI5CF%2FmwvTw%2FehxikhqeqxOugKG9n7qnlmzl716EHfUYDEKx7dxN%2BPN0v7wWiL5TyH4HIDgRlVF%2FhlQfZH4Ewg4GOvQY6pgGvkNcbe5vaHf3PRfHo5R%2B35R%2B1afjfpL2WkTcvAbhMSq5FXBisj8b5SCSPCKQnde1FX4MmCkb1F8Dyf%2FdOMzVcMxDDcqG9PnUpiKdy0A14y4rmp7Oi7EfFXPE%2FFtPqRWfcVZGlHeiUChovN5Mr0Xb%2F0Hy5ryGJctOQIIOMcOKp%2BitZ5zMLdSuCceaonoS70AlRoUJx1Xoe4mbZzu81E%2BktT%2Bx%2By4Y6&X-Amz-Signature=5c92c5b399883f99ad3d59d65d1cddc22cfdceeac6b8dcc2ddfee370a3630dbb&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SQNVAU2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCeJVexRDdld%2F2hqW7E7zbfFW9ZxUcUbM4VWlUOg%2BJt7AIgF1Fi1RoW5TuKYQa1jVJU3HmUpJ%2FlnIwCheT9cI7zR3Uq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDA%2F%2Fd34eVY5FWPvsCircA0UhhAVUWROnDcwE72qDZ3J6%2BSK8uOvzADH7vh%2FUKHsHrdmHDxSWvaX4p3xTHt6RoREAy01vf%2BczkLl%2FU0EYA9CEbsNx7tQZ1k%2BKIVfH%2BA9lRIYzNCksVPGx%2Bqd7IhRY1s3C%2Bg3VPLG1uIt54PWzYSf2oEcyMe2nQZrievciTRoFLy1Eml5BTLg1z6rXMy7TD1yb23ntoaJrgDClA7prMWmyvZ4B7HxEEXBAqoVdk%2BPweP1EEf0EHOImDDgB7498W50jL1gVEumlw3mW6WRwI9QG2fKFQh7IzfaGi9xa1%2FLeH0Ak46G7IJwlEEEHl4tMYboabCd81AkIBSHYURaWCoHfgXxsjESQ1S4pfu23NXfl06%2B%2BHjGRHp0%2BsFpcJoh28EcJvUIyedUp5%2FdBGsakKw2gtPwe0RswcS%2FYcUom8jXsULG48f6ZKMczfRHAptjnBhRv56cA55qYxggwgYGV7jKzVTVU%2FaakGzNBEdUQQpOdoij7QdspBid8ML%2FTIo%2FPDGr2KeaURkw6SYTHd597r54wBXqj9G%2Fe7cKBSxwXDm%2BWFKz4ZDZO%2BgerWbe11tQEcdczcE%2FG6VD4GKbFCTIv6KPxQuGbfwoPbKkTqg9gTTNKcJ%2F%2BBSkGbMSU%2F01ZMIKCjr0GOqUBUxXTionpsHUhH4yYF5AL20D5KurXJ%2BFa6O7%2BUJozTzSfjjOdU6NI46RQWOVDBSX6SUI7rU7iqDDoUbT8%2BEEV4ncw9JRxWjKmmOW6vsZkoWeJydWrvTQ9aKVVN2aONAJEXC3X%2FoDD%2FtAxn9KnX2%2F2XS0AxARSK8e5RNzARhxL28xWRNRWjb9kv6LHLpgjYjNNnVCrSXPfEFz5yZO3I8JQHHgKCym6&X-Amz-Signature=af5be657da218c36a78558262005ae81c1c9973389aa1ca883e169eab9fc1213&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNYK6EG4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDdWiTOtoaz8BoyWLz949IZ5kW%2FIYmaUn%2Bfy8uWZMSCxAiAMn5FIKFUEl1GVOMgb38E%2BldZcZYTFPMIjq4KHtas0jir%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMkoAFzWGPDhaGFm%2BuKtwD0GXqp6CcK3cdCOywKjIJHUKSU4RgC4HbOSvwafdlFtgH7LJ1Bq4OOnBLJuMg862WrnqD6%2FDIsi7OxPZJEojmj6dMwEme2d5LDcfrLd37MdqgOQxzFvSv8CG19DMxHRdiyETP0zegcnjtdJbT1D2IdEgxFViuQBg%2Bi1PeBckbk6Mz57zXmTzwi7aEBtSK9IFI2zI2ayaIhhGioe5RL5nDaXH9DMZZCmbpRTzDQRiVOGqYRPvG9CPx3B%2FWGOcF2VJnAfvYfdzIIyDETTjEOswhIUqUKkgW2Id94nqvhJcYQZo4H7rZwfyCQ1n0F%2BAhsiSP2whl6pcRho%2FkZ2ijtqD0pWZvYmz%2By3z8C6w97ROYW2In5voqXOVtzS62FusbfC1JKnECKznyimoKsthKsUw9FqHVpzFL4QONIlvE3PeyhLN%2FEbhO6zdZ2PjiziesBqhVUZy1wgVVv7ezohm%2FPGEP9CEeMrCxh3XgsYBP4U7ioh3Suuoz9ID216P4DPb3AmRV3YMbHCXsjxsnBDCX%2BUwYLWWpZRvtaU0%2BoiIaapKhgtSurV2O0yJyCdvnr%2BpzZMmnXx5er6Q2fNjtB8RB5rPF10ZvUI4XIpa8zlbnZPVFbiuBfeYJnI7yfViaL68wyYCOvQY6pgEtJwdehJ1V3DlKfQUQnnT9rdtCqVVmUsT5Fbwa5lfYB7JxmaIaKoU6onEdcrrrnDTIbemMkb7wfosd%2Fytdq%2B1CnUSRglOtfPVKLjhVvBie00Tmt8Ky8w0Xu1bWDchYCPaIrdy9C9f1qe%2BtrqZ0w0UGL0Axm9avXWlFrS2xT3JDvgoLrq8eXrTCAl6Qh16XtlB%2BzEq6CGQ%2BqB1a%2F43slVOoQkDpi7RD&X-Amz-Signature=63e3fff2dde39871a867e28b0fc26071e7114aed8ce7d3daef5a37a178a27457&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NF7U6GG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIHNpk0mowCuOuu5mBXftaj%2BEE6BLZHcozAm0PHbOG77UAiEAoWoDIbbJDWJ%2FTq3OQTnJ7cJ9AUuK1x5xvauoBGV1LvAq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPn9SZrXrO01u%2BBTAircA4n%2BvfUmQtYpr2QW6E3c0Mg5SVK%2BCBg%2BF7gj5D5GhuFAJ2HQIyao6f8wuYnwkeVKROz5SJLJp8Uyl%2Bgw59P94UzGFWjfMZK0DPG8L2V7aHcOphepyaeEMB3X3NWloOtc31qUYTp1M%2BQk8y2%2FrEkbniZXdj%2FJXAPYkUeB2Xs3taeVyQFdu8vwvWfeBpAxKdPljo%2FVq9Ah0%2B5D5xCfAiLhOvJNY2V%2B8%2Bmt77o1gfEcKqcGE8uYk9msPN7EBUhkFQwCv01XkBiEJ318kEHfZilaGUfBJcluax5eUo96lN5u5MUlsDVWt6OJo8rn73K7BLJ3NqmpUvgxvxg6AnrGqB3UD%2FZRR6pJfm4GF2eaYcPAxOR2vz9BpEf%2Bu6U0huQlhHc0SFnsEJZpDpgFOa5%2BUrGm0QuOjl7%2BKSeZgP53bR88Psc3vGAXZbL9x2103BS1kN0TAbpS6nxa7I9rLVQjMf5bCY2BIx9I3n99WPXOMFeEa5uumlp28OCMrmVp35BS9HsnwwmS%2BTI4A8TEDWIGcazRSTu8h1tL8XmVcN4CRwUCAUGhQYZ50ZLSmfroSf0bfvvTRRJ0ueDc6B%2F8aMG4YiUw3uf884i%2B1sel1%2B1iTqBcKamEZ7ODtxVENllJkUBfMK6djr0GOqUBIH6L4RsxurgaG1%2BdqAatP4aB3H6W6U7INjohmYMABACepDy4VUyVYPUIXpj8AOxy5duQQszKpBgMgnpzDJh5DAQhx%2FbmQUVHjWG89f9hf45idBkPwaezoqIeLlP3rzFkrJ%2BRMc%2Bs8cjpuP5U%2B1KvrB0HtIS2dYgi9PDgX8ZclZBKtByingxHF275lrs0KK0yllupGk5m9e2nK71zxJ1ekEEi%2BrdT&X-Amz-Signature=914ab635b217a8dbefe5823f8fd731ce84c01d2941247d5a0871f440a16f3da2&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NF7U6GG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIHNpk0mowCuOuu5mBXftaj%2BEE6BLZHcozAm0PHbOG77UAiEAoWoDIbbJDWJ%2FTq3OQTnJ7cJ9AUuK1x5xvauoBGV1LvAq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPn9SZrXrO01u%2BBTAircA4n%2BvfUmQtYpr2QW6E3c0Mg5SVK%2BCBg%2BF7gj5D5GhuFAJ2HQIyao6f8wuYnwkeVKROz5SJLJp8Uyl%2Bgw59P94UzGFWjfMZK0DPG8L2V7aHcOphepyaeEMB3X3NWloOtc31qUYTp1M%2BQk8y2%2FrEkbniZXdj%2FJXAPYkUeB2Xs3taeVyQFdu8vwvWfeBpAxKdPljo%2FVq9Ah0%2B5D5xCfAiLhOvJNY2V%2B8%2Bmt77o1gfEcKqcGE8uYk9msPN7EBUhkFQwCv01XkBiEJ318kEHfZilaGUfBJcluax5eUo96lN5u5MUlsDVWt6OJo8rn73K7BLJ3NqmpUvgxvxg6AnrGqB3UD%2FZRR6pJfm4GF2eaYcPAxOR2vz9BpEf%2Bu6U0huQlhHc0SFnsEJZpDpgFOa5%2BUrGm0QuOjl7%2BKSeZgP53bR88Psc3vGAXZbL9x2103BS1kN0TAbpS6nxa7I9rLVQjMf5bCY2BIx9I3n99WPXOMFeEa5uumlp28OCMrmVp35BS9HsnwwmS%2BTI4A8TEDWIGcazRSTu8h1tL8XmVcN4CRwUCAUGhQYZ50ZLSmfroSf0bfvvTRRJ0ueDc6B%2F8aMG4YiUw3uf884i%2B1sel1%2B1iTqBcKamEZ7ODtxVENllJkUBfMK6djr0GOqUBIH6L4RsxurgaG1%2BdqAatP4aB3H6W6U7INjohmYMABACepDy4VUyVYPUIXpj8AOxy5duQQszKpBgMgnpzDJh5DAQhx%2FbmQUVHjWG89f9hf45idBkPwaezoqIeLlP3rzFkrJ%2BRMc%2Bs8cjpuP5U%2B1KvrB0HtIS2dYgi9PDgX8ZclZBKtByingxHF275lrs0KK0yllupGk5m9e2nK71zxJ1ekEEi%2BrdT&X-Amz-Signature=55ffa8ccf84cb929b2c5ca8e3152c80312b8155749f7342de8bfe6a841205f79&X-Amz-SignedHeaders=host&x-id=GetObject)
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