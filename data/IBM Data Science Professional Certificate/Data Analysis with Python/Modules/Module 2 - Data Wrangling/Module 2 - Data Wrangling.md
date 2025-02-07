

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UT2GZJBY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQClRYQroLpk1WmDLdg8iT7o3pYNvnyE%2FNZ5r0ItJnarXgIhAIe%2FCXuDDSbWnAIUnC%2BK%2BBrQntOhzAmdVTIC9CM2UvU1Kv8DCHUQABoMNjM3NDIzMTgzODA1IgzQ0B51BigX5e0gdacq3ANpVHDqdSfNByj5y4lwF6bck8y9ESeV0Mh4lIm9xER8u1GwnBwWPSrIHEXyVl2P12mgEgeUmnPF8YgzDJZmx9WilMDJexbguV%2F0%2Bm8DorWew1JtgMQ6PYtayIBTwYXDRBEUOSwyxDgL4aM2bjrcjSLZf5XNJwpUId9hbO2%2BObPBp4AjRh%2FzQ8X%2F%2BEw9dn6A9HdWFHTjwEH66oB8isk3LOp2R5ej8GvzCLFEVPkw9PkT02YKaGHqkTPT8ACN2mhnkr%2FOOURvIhuwjEXEfJOGzMm9XrikvdDhpGxI52VZzrQyRMfatGhHIoscpC1t9DqIm%2FHK%2FYLC%2FcK%2BSirllQhTR5MZH4rShAGtuvySqrpEhzReb%2FguCUGHQMdrXLtruk5618dnzi5%2BkstDvWkz044UXQ5x0EHoopb6D%2FAUduOs5KvmKQXbT6ER9yJDrmTHbOeU3%2Fnk0OSmOwAIsm6xm3r3IZ1nKa7b0bFVSRR6YpumD2WmjBzy28mLtB3Rw9BPBbWGOol6%2FgmBPISUmfSy37%2BXh212VVRPjycnhcyWAmIZIBspUm9OPH8wOfwZmS7v893vhm2de5ZA4X5thPgo45pSUnkF4l4Ty1ovlDdajescDxy7E97prrbFMQkCFQjFbTC575e9BjqkAe6SgsB6gMWgVW8BR4JFtLYLYqDOoyIQAqQlprePncg4TT6DRBZiN4snJugirB1HsRBQ5Nw8dPw1%2BcbENrOdRmYnjrMfiY7WN2XIioe%2B%2Fv%2FGDEAYraed5k2PWm2C8jLKLie2UYGKW%2B5fkwcYTVjSd2h%2BL8Wn%2BBKGP1FoRhLsdwCvjq%2FhE9g1YptoxhmwfPuvMddpaVYSt5I%2F1CjLtgoBNI%2BuEGY5&X-Amz-Signature=594bb4b05f3cf5057a560983d414fc6f5dddac1a66c653a287a37c58e101434d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NANO37W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQCESTqSgRBxw80J4wNIkPuksDpkPvN6cSY4Jon92D2TUAIgEFsk2ZDyvpYEDv%2FSTxl8TdCVOkxTxuMrLGDCCtSPwGcq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDDAdljYtYwTpA6owxircA0lUuymBNsiLM7lEbt68d0LWEIbj3H0rNpNlYjkKZGV0XuULLKhbcvrVoZ6TzKDoZp2Q%2F6flZHldHPBFii%2FnQpldAq1%2Fcpi1katVjSjMWKRkNtYwisHUm6EgfCB66U9esf3KsMOTL1KPjs4iFllAL4U7Myk4Nv%2FAJXyDxK8RWxGmJs3iaYZ5pd4eNzBaQguJWxhO14bT3e0gj5lpkDjttPRnTzpW67UdAGZC%2FAs%2BxPdZtpedLDeurIU3VN1Eguak8V2CJzG3RPGU3KzAM6bRXe3NcX%2BeCa8tbKjjgtKE1a6K%2BxVnqhelW0JDAuXA1CXXw9NCiWh0M%2FCabqwdIBqlEiMkhYUns%2B6eyqmXwHmAwfbQVgz63fGAuGPGhcj3anw0YAEI%2FfNJWg0s4bmimqBhbpH6CJ8f2Mu36yT69CvTOYvWETp20d0wwlocRo97agB9CSnNGxuiYkHrYt03OsWyaU9oWLMW%2Fc5NKdwC7zmD0puGiFS9pa7qd7sLVBnC36QEzSWlgwqwb42aUn4prvd3X248JOJe9PycX%2B%2FuJidTMb63mDjViqwKNJUirG4XoSrnEvpmQq1lE%2BudJ3jtBQXbV1PRK4bScdjwhKLVhI%2F9mGsjS7ke3iHBrR7fj2RNMI3wl70GOqUBXgIH4Xa1y3G4d9LdgwYEFSVLkuTNjH4SM3NKEi3CK3Zso59gntTHjA95jPn0ZPROsHX6iMbVoV0cO%2B9GGeW6sUda1%2FAuFlbuD0kusW0h5%2FNF3eIQmk58kJBZMk8yTieyczpLamLsS5n%2BHY1IpGiWHp5OiWiK0o%2BoDUfcVhDRxe%2B6a8Ucbhxpm6mJdmC5jXaaRRQfqbdyFrEKJh3gOk9SXXEVGjIx&X-Amz-Signature=82d564e20088413e33bbeaf37d29a9c288f51f0aea3064c7a589fcaba894fd5e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUORA5GB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQC0udoatI8KLAhyDF%2BSJUed6rrQFfH9pL2G8FpDtWeNXwIgF8bxmwbiJ41OvQye%2FPDXmVYDuNEsbDnyR5Fts9wNPEAq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDFinASG7Gq79IdMtdyrcA0D678SnM8q%2BlKCAfxUAVpBBKmTuHEX80yJCdWdxlLUVEmPxOD7U7pTS%2FNxpQ7LAoi%2BUQEzWH9iZknifkxbWVFFXn%2BcjCYKr6mgKJ0vDAgszlk8g1KArzZqIQjR%2B7ODPn6mMz2%2BhnZa1LXRH%2FVHgRiBqz08kG%2BgOO5RNHWVmrtv763Wk3zcVMD7eybXO%2FM0dRgA1N665bWdiEsFhtEedwryDHkRs2Oxi0Gl%2BWTI3V0%2BFZTsVnECN8NyWgiU%2FtlmNgPgChJUy8dpRZgyUWlQxg%2FLccT4G%2BAMO8klHibHcrmA4FK47FQGPaR9NvX2PBPtShHJlCAzfHHp8er9EWjgu0QpbtI8XnCWQOO3q0CI%2F3FJc%2BjfUDTno3qbDiY6%2F7mLXqh5BU3NNCfhFw6TAjzfVE1wQ8JPoWrE15kp%2FTwFKpfyFDobPqdGUDY1S2z07WlWxsOrhXVp%2BFstQLi2Iuxy9VOUNSBdEY6VysVEztcUwAaKK9nCk27HzfHNinTuhRjbMvhtyYELAh06TyZbpBWt%2B3ncMlGdmxAlE1iXfXfbXoiKYVqnIcpybF3CoN5vz%2Bo9RAkS8XPtHQ7kMItlnVszJBl7xrHDMRE8GB4tPemGtK0peU3%2FkQeqTTFsegshPMKXvl70GOqUBQ%2F8MH9nCuPDfB5bMwxd4lcbK%2BTJQEfrR8ML3n0NUqZWRV7WMFEqaGfBf3ObSobzV6c08NPsxMpldKRblDlTEr%2FJh2y%2FVOEh6%2Fq%2F%2BsxzsjTB0XOH1nAdOKEwvhdNsSRS112wYXIYm5JDp%2FYAFt0zzsRT9%2BxT%2B5z4xbwcX35Hu773LhByEBpRfdjFsiCricHPbQZVtTIMW%2B%2Fop5EdgUoZ13Uf370Nc&X-Amz-Signature=14f21316e07cdb0a33941eecd5fb334b6ed9227e4128742c3a5a1731a33ad6b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMXKFAYR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQCmWAcpmSw7%2FlG89HTCNVNlDpCj6pBA6pw%2FE2H0nH0WwAIgf0vVL3vecPxYikGelnfw6czUSsigxvmcetcokpxsM0cq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDGYerQ7iu4AOcuzpSSrcA5SVXRr2X7RGlGILC6mzR2vZeuq0bIxpgZGE8ygvcBx1pvcQVN5Xq%2FV%2BnYBI2mdOVGd17BJlqUU82vLby%2BZvyqy5TppE9QkQi9gdacHpxb3oXXH%2FnTMP221hpkUTZCF5fPBdk59fs3gKUkE%2B05gij8q%2BJnUNZ2cgAmbg6SPEjw0wY%2FNgY1LuvlfvgKWsPUFkyTR5J0H7doD3AMNrYmzq7iR44PrATLJ7X61%2FLbjttF3wDyEyYSpJA%2BjncI%2FV5DT%2BU7xtD1397nWBckc%2BUDjxr9wHbPKjXgNn5mbJcuX9WcIfarkWCaO1TADDipx3Z7PPEAmNAgHe4APvEOJmXTWeJv2LHGqnpSL3GtQdPm6BLN%2B3NDPsQ%2BO8H4mQoIP2gKiLe0f2cFsHn6CiUDUAYaS%2F%2F1gyl2SENBp9R91gjQJrxGuNWcsH8aVVTAnwWYIUYrUiOdr2rY2RCOTmdE3JBsYxq1U9HE%2FAdLd%2BW2dF%2B2HEJhzbwRhwpKB2HXzcj7zCtwdqy%2F6G%2BEh9k3cyDyGjDcCOsrGXUhXU0dNrfHwMHE8AEXXlsnVPy6XRNQgKuPqs3POwvbS9nj5Pm0V9ipzIZaBuEiF39rUGuXIDKE%2BSZLoCf3Qdn9vdehEBfQngF5wOMKfvl70GOqUBVQYQjylidCTDfCqzBMGL2Y%2FCAO2YChDrIYRTOCm9X92w8FVEzM4R4CrzS1fFktofLf1iU04P1gHEb7WEBLcWDc92iqjvuvIDktjEqISn76pJjKDOTBTnGHMUfIuAckRLFws6RnmvKDp2uCgltk%2BBvX%2F53BRCo%2Fitzz8AJ7AfWCU0M4xAzyMuzcb7sNe%2FK7m%2FHngXEqzYkahQsoQdWpulfuHaO3%2Ft&X-Amz-Signature=ff73d95ccab5804e282dd3bd44596499bf555a8dfc7484ea6ea7b974d57a028d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNIL5IOY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIAGmmtPpbaNGUSAe1bo2RnMgcGMNS%2Bq1H2svodyVfmtpAiEAwFm5gB0A4YFYTLnGTmRWrsA8hL5ZHQEiWxVUUlxmcp0q%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDFhTi22JAxsjfMKduyrcA9JKnlGUFUMpM4GFgGaK1rXrAsQ67VJGQf9RxVQhQXpMbbKXOfuj7DowJl1mahHlA5fnZPRn0vwKi0ugQa6D0ipsXyrmjCYE9XGI4bbffr58Knx4%2FOzIVL3fm2zzRaZyHIOicR8PGP4FkOMrHry91L1lEDjkmbjb5LGJdxoXzYG2MKW9zA%2B%2Fyw4kj7PwRk9C6zzlq82EJsTX4iVpJMMH1Q3bk0nHwU6A5glWunoH0aEVitNPvZWYboxqF0MY8aTNoD1Lqgqb2OV%2BV2pimdIGKGGe6EBwiBhqxvrDc3GGIT1j16sROcFhUDmhIZchL4S829pq5%2Fbz0e93sfUUEMWwTG33zBMRi5NE3ypKHLWuzMH%2FnXpN10v2yPjo7f4ykDXoahSTfP%2FmZ%2B%2BN5VB3rNBvPwh0Z52HDsm5%2BBNxPzWepfFE5kHrghRIaAACkaS4kILPmXO4m7pfsKgNqi3kBkjuEutxUQhc%2F4jAA41oyedFuKKDFxZRDcu4kPb%2F47nVqUhYiMauIER3zNsw7fluGuZmtKFr50iZOxCc2Ok%2BtphSFec0HKQO3IlZW196IhwzrRhWodU1aWm9cbkUQOwYjKJ3Nf9O6POY%2BoW6oMvXYE%2FjMZ8MtZ%2Bnn6XHfwivcGn3MI7vl70GOqUBBt%2BlK%2FyT0KFtjjH2Yl7Zqcx9mq6v3VAXnqvR9gFQaDvo%2FWpmJgOesvqooW1Z4efawWS0wki0t9RhOkx8uERPIkGsqWmeQLWSj2exj4xWau5LIH1cQvLR6h6btQ1YB2iNaYYyTCVjc9WS1HipmfjE2HNxtFzjjJckOhrXESsUEmL6ohDqX5R7rDXNb%2BuDWlYQKtt1VJHIj7twMTQLOciw62L3%2Fu39&X-Amz-Signature=fec4d56f0c2d873959024f32d7e4420ec8f247eb9d905180a7f72ba8e377277d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UGDKLEG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIH3RnZvl9QczQ%2BKllvdnAlOlhFeJdtwaHXa8xE5B9PB5AiEAgmSMEzuza3bWtsja1exGSeNieQ67zPN6BpPy3Iao5uwq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDFuiTTNsaIZjXKHS0SrcAx10LjlxzSH%2BE3qL07g7r1wrUk0MuphYu4277yPrrMtrM9qAC1PxeQ8A9VFv8huiCB3DDTc1NHf0iFzXr6Nfn9OOf0fLcNQLk4eI7CPM4S6ue%2ByEXF2k378AnZaHU9LYpj31TQgT1VpSRErkPPDzjHgaRiNy6NH4540XiuvvSEQhmgjy1DuoPFtLK0jPxuc90SQEyuNv8Q4vDiJLVDm3BRJvZKTikda42uB8OFDCuF9ik%2BBNl979yLIHYffg8w3rQopPYnvFG8gUu0818wJEEHtvLMHMA9IoCd3vUJvd2WWuBwTHI9OXAL3omvLWXWS%2FbRFoTNf5ivMxTNdTPVfzVefnvbar0mnog2Y%2F35FUDxCdaF5FJCsXCbrrd69i77qAgOOuLKPyNWcmxDnNfWejP5S3BPuHfxT9RGpi%2BzgbDEQ3QwWhAJei4dDheCPRbk2ZAW4SHoETK7PBUebqMQoB7FI%2BPPIxXpt0OxoKMgk%2F1WmchC2odL2Pdmvm%2FROqCveKYCyDuW0hzPKUu4uT4lVoFTqprazUPi0eg0kSVI7oMqiUGTs9qBVuLIWqOpUd2FoOfGV0ev1IfDwz50jSbBIGm8DSIz03%2FTIKb%2BMusTIUL4fYly8iv3mkmy%2FQHJ%2B6MILvl70GOqUBWFGROGXua38SeH7FpOnjAsytZJasyYDe2CIJDiO2KPEjA2dDZwx%2BsKZgO%2Bd39q5wvXk1BC2ThkydU8T6dJ6FCI33144t8TZrHiHILKzlou%2B%2BPKA0fcTMygKQ7SBCRM6j%2BwE2H8hcKCZa7NpWMXpKIHYSIyXVAR%2FLUjl0Fdw1MJn0kKnKfBUqbkjFTt8LzF%2BlefbSiW%2FKYO7GqWJru29dXuSH1T81&X-Amz-Signature=8d0f269285bce4337f726f73954f44c1f2efd0db7c9cde5afa609da20b9caecf&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKTTP2Y6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCICJTqmVpblSEGWrYV89BqgtJNItoUfddWu4I2vKZRELUAiEAqk7XkM4bLruHfiMEFyxHcPGQfakqNUhGO%2BHIKkcVmEUq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDMuCgZPCqhAxaiXX0CrcAzkuFuUsymsIPFMUvHD55nLq2M4Jqx6W1MgkKg2fRXaAX9iqB6K11sPmHIxJZbQMyXA2Qnja5vBHqnrKo8DSK0di4OGVNYOR4bg8eLD3IGEsOxSNE4sF9zKKvF47SoO62dcWLcWqRicDIPB51wTmTyGJVVKwMnyuahSAfaZ5YmtSNpG8cqzvDp6pDddsQpXvJ%2BfaP1Rt3rWsMygEWVs9VCIhUcxrob%2BQLubp3rgQ%2FvaH1kjdJxFamoX3%2BkOlImlEWzrfyn9DvPK3FSm%2B%2FqeRMwtPFjZlxIumqUEffDokUk%2BNIEi0V8l5Uv41EntQ6ggPSXiPwf%2BUcIlZcZFNg%2FnJRhWWpgohg1JBSd4VGul9EdSBgZUKZuperg7cfrMv%2B6Xx1eYlXUBu14OhB8%2BV1AkLj3wBygKA%2F6wMkyTOUG1blf%2Bs2osbN801YHelLPk49USgZRX4UkdhLUiKICOvFNAbiECzv4Idn%2FeJZSva%2BUDzoLzXBsxVB3vpwZh3k65j2ChrrkUIXpSzVMEeNsPMI%2FlsUwr6%2BK6VJjasQSi1pDfixK2OyBXTHJ9Dn%2B4mLQuXvbOzFoJvib%2F1d3bnqMoJwh2YACRy4CL%2B2ckLgmV0K%2BZbRuYGBQL1VHf2ln8oFJOLMKHwl70GOqUB%2F9erDXwkfraTRghRvNdQrEGSZQEMFObz5R%2B69h%2F31rspikKLF8HoPLmJipPMm%2F97wlYV64Jn6vez2ChkceUekuyOYfIN7c0aGjuGLMAnrVKUOuY%2BNY5mkhSsXhptdWjGE7ME%2FHCEa8vhJj2y64JnntJf7Sk8is%2BMSCDuoO%2FSTMG%2BgA0yao3NDSqWZPD3lClgQW0iJk8s%2FerSbhKLZGKlWOFMvr3z&X-Amz-Signature=97065aac493c009dbf92bbf0b8e97b3145ffdfcb8a9d9bd52b3af7d12d40b1b2&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BLHSWB4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQD5mCW4kQJvHnvnVFx8L1Wf2KsY1y8KwCdRNIYcRfAX%2FAIhAP%2B724%2BWBpuDE9b0Dnz5kbxdFGxZ5%2FAaHgKf5un3PYMeKv8DCHUQABoMNjM3NDIzMTgzODA1Igx3aAPlPCQGEdWInm8q3APG%2FuOTQibSyk4oAwNDJZmH7PSSq15FRhM34cHx4Cn9%2FeDiQ%2F43i8Avr2i01MZc1mK%2BIpfG%2F7G%2F0iwx8GYNT%2BaTMunugBpKhh61IFKGkGCJ7L5x8SLq694Vq%2FYQ92WP%2FnbnmImsZtN%2B5IH0pRLJlUsXi8%2Fv3ttqZFhUgoLjKA%2FpQKZ3QAYiLZbTRVrz%2Fz73il%2FWowWhgFJ5Q6yrig5Wc0ArAs46m1zrLofgSMNdUxkQa6fgVZidgzMfyiKEsip%2B3J1TP%2FnXLfyMGopE1grogoHQ%2BN5FW8UFh5ViztO%2B6WJlmkfg0MUiTm6%2BO%2BvtJ8YM%2B58kJ3D3FRrbtNOUOV0Qc5eI4S50j%2BxSRQRsg5ahF%2BvCPGG1kuEgn0t1TkoghBwViPaUr%2FJ8wJR3aB5bdJjg3q44sOyP3wlEBuWI%2FONx3P2nIiC%2F2Qm9XZd7mjKRycIcXj2g%2Bh9AjSz7RrGig2FWmVvKlsZXRRWvljTeNOW2wIx%2BFuJOJGx6HPPzIoVfuxwH08zZ3KafiSwHIH2pZb9Q4yL7R7x7IwLisiIzEmsCTZKua709VjKj1xE01gY0%2FUQkI%2BMWt06psVBJ8fvLUPbfukGhlAQCKnElmusvhrKlfi8W%2F77QOop26nYH288bGzCb75e9BjqkAbZ8dCmHJowJz4nDrzEY%2Bc71DuMtRqgpPCuDwPEhlN3WBPPCSDlcLMTREdzUL2eEVxh73udo46wJ%2BNe3UrBk9zd0qBqRozXwsDkvGcJcpUPO5Xdz6J07o4PX3Y6TZoTRZ30J5wYBqB96K%2BitM8UUMl4cNr2yTcc9tw3AjA49T%2F9HGA%2FX3UYzg3oXgC00dLJx%2BTpBsyE%2B9iTp6Fr95DZuG84hZg2f&X-Amz-Signature=7bd896a652bee0236fca98024c0480314a4ed2624abacecc4a46f49102245836&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNIL5IOY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIAGmmtPpbaNGUSAe1bo2RnMgcGMNS%2Bq1H2svodyVfmtpAiEAwFm5gB0A4YFYTLnGTmRWrsA8hL5ZHQEiWxVUUlxmcp0q%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDFhTi22JAxsjfMKduyrcA9JKnlGUFUMpM4GFgGaK1rXrAsQ67VJGQf9RxVQhQXpMbbKXOfuj7DowJl1mahHlA5fnZPRn0vwKi0ugQa6D0ipsXyrmjCYE9XGI4bbffr58Knx4%2FOzIVL3fm2zzRaZyHIOicR8PGP4FkOMrHry91L1lEDjkmbjb5LGJdxoXzYG2MKW9zA%2B%2Fyw4kj7PwRk9C6zzlq82EJsTX4iVpJMMH1Q3bk0nHwU6A5glWunoH0aEVitNPvZWYboxqF0MY8aTNoD1Lqgqb2OV%2BV2pimdIGKGGe6EBwiBhqxvrDc3GGIT1j16sROcFhUDmhIZchL4S829pq5%2Fbz0e93sfUUEMWwTG33zBMRi5NE3ypKHLWuzMH%2FnXpN10v2yPjo7f4ykDXoahSTfP%2FmZ%2B%2BN5VB3rNBvPwh0Z52HDsm5%2BBNxPzWepfFE5kHrghRIaAACkaS4kILPmXO4m7pfsKgNqi3kBkjuEutxUQhc%2F4jAA41oyedFuKKDFxZRDcu4kPb%2F47nVqUhYiMauIER3zNsw7fluGuZmtKFr50iZOxCc2Ok%2BtphSFec0HKQO3IlZW196IhwzrRhWodU1aWm9cbkUQOwYjKJ3Nf9O6POY%2BoW6oMvXYE%2FjMZ8MtZ%2Bnn6XHfwivcGn3MI7vl70GOqUBBt%2BlK%2FyT0KFtjjH2Yl7Zqcx9mq6v3VAXnqvR9gFQaDvo%2FWpmJgOesvqooW1Z4efawWS0wki0t9RhOkx8uERPIkGsqWmeQLWSj2exj4xWau5LIH1cQvLR6h6btQ1YB2iNaYYyTCVjc9WS1HipmfjE2HNxtFzjjJckOhrXESsUEmL6ohDqX5R7rDXNb%2BuDWlYQKtt1VJHIj7twMTQLOciw62L3%2Fu39&X-Amz-Signature=fec62e9f52c33ba617ccc56650ba1cef0c481f1e1b812de2bf24d0109f2c9b3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSPWSR4S%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCEEXrHVy1BhrsYh7e2%2Brut%2Bttd8tYYvlYiZVl4b0Vc5wIhALXkG6B8VkwQYcHY%2FFEkIXV8A%2FWCVi6JLh1BqStpxCoEKv8DCHUQABoMNjM3NDIzMTgzODA1IgzX4Kt%2BwK%2BRF5oJvucq3AMknfPgaxtQ5p80OchofS%2B7mG9Gj2vdAqHBoHdnLQg5ACyCYLVi3UoNPytoqvMQ%2FdMdP9C6vRCWznIxxhu3%2BkQMCpZVeL9SJjayfF6gmbo7ppVOflTFbjdlTJ9X3CBsVjdBz14silPqIXN%2FCsZMysaPdKzTh%2FY3e90CKkV6Bca%2Fe2cOpwXdbnd4bT9jEsx4uFBOq6fFT%2FiUhOwsLoA1TSfNmc3SRypZiWyOK5ac7VL2b9oWB9rGFmymhPByhQrB49eC4jRUEBp9s1WaShmCd%2Fp9a%2FgKkSVfyoUi4rNAMy8umwACrCXtntXR4tEMt9e4M562HhHjMtGLB4YXoQOjFnRo1ro1ez%2B8BcEL6G%2BQgCaHDFyOwFL5elevKwEL4V3z3nATMSbsWWG5vFVnw7Wpuxkd87KBRmKtkqYhmX6jtkbw1HhwpgZ%2BRhtMpZ9RfvXOJh4lYrmOE1X5l%2B7q%2F8%2F8m%2FMX%2FQMh53SZMODueZNOzB%2BZpzI6YbASv84vLiA3tOmSlNEKBRuU2vrbo730lDL22qMyON%2FEuXY0nOTKPkvKCgCmetRlwKwpHx%2FfaO58sBKzte3O1FibBk5XMVQWtIUX7jsFBgG9P24tx1MayENlYU1TXACy5hCf12J6AoX0RjDi75e9BjqkAcyA6KF3RJiEqUu9R86xdCmUhB%2F8gdOnhwX50kuFhcVia3qCcdDrLy3rbBzsXW4NQKN4IgCbRbWf0Mx9cewSBOjdebqIok5ih8xR6HjBTCf6mGjk%2Fl%2F25xdj%2B1O5xj0FGiGQABoapCKt8chySqbj0XP5ayLGLo5nl74CbGwlmSO6Yw6Dc9CtbWA51%2Fib%2B75N39Xu1WnuJ3wVpoLtRrrkBZjdYW%2Bm&X-Amz-Signature=ac69dbb7dbe208380689883608ce5a99f05a3a824a53cdf1d3cb3f036d72f45f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSPWSR4S%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCEEXrHVy1BhrsYh7e2%2Brut%2Bttd8tYYvlYiZVl4b0Vc5wIhALXkG6B8VkwQYcHY%2FFEkIXV8A%2FWCVi6JLh1BqStpxCoEKv8DCHUQABoMNjM3NDIzMTgzODA1IgzX4Kt%2BwK%2BRF5oJvucq3AMknfPgaxtQ5p80OchofS%2B7mG9Gj2vdAqHBoHdnLQg5ACyCYLVi3UoNPytoqvMQ%2FdMdP9C6vRCWznIxxhu3%2BkQMCpZVeL9SJjayfF6gmbo7ppVOflTFbjdlTJ9X3CBsVjdBz14silPqIXN%2FCsZMysaPdKzTh%2FY3e90CKkV6Bca%2Fe2cOpwXdbnd4bT9jEsx4uFBOq6fFT%2FiUhOwsLoA1TSfNmc3SRypZiWyOK5ac7VL2b9oWB9rGFmymhPByhQrB49eC4jRUEBp9s1WaShmCd%2Fp9a%2FgKkSVfyoUi4rNAMy8umwACrCXtntXR4tEMt9e4M562HhHjMtGLB4YXoQOjFnRo1ro1ez%2B8BcEL6G%2BQgCaHDFyOwFL5elevKwEL4V3z3nATMSbsWWG5vFVnw7Wpuxkd87KBRmKtkqYhmX6jtkbw1HhwpgZ%2BRhtMpZ9RfvXOJh4lYrmOE1X5l%2B7q%2F8%2F8m%2FMX%2FQMh53SZMODueZNOzB%2BZpzI6YbASv84vLiA3tOmSlNEKBRuU2vrbo730lDL22qMyON%2FEuXY0nOTKPkvKCgCmetRlwKwpHx%2FfaO58sBKzte3O1FibBk5XMVQWtIUX7jsFBgG9P24tx1MayENlYU1TXACy5hCf12J6AoX0RjDi75e9BjqkAcyA6KF3RJiEqUu9R86xdCmUhB%2F8gdOnhwX50kuFhcVia3qCcdDrLy3rbBzsXW4NQKN4IgCbRbWf0Mx9cewSBOjdebqIok5ih8xR6HjBTCf6mGjk%2Fl%2F25xdj%2B1O5xj0FGiGQABoapCKt8chySqbj0XP5ayLGLo5nl74CbGwlmSO6Yw6Dc9CtbWA51%2Fib%2B75N39Xu1WnuJ3wVpoLtRrrkBZjdYW%2Bm&X-Amz-Signature=7de6fe3008a75b84a95f4341249c184185aa9f8cb323f55964e3fd10175e0b42&X-Amz-SignedHeaders=host&x-id=GetObject)
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