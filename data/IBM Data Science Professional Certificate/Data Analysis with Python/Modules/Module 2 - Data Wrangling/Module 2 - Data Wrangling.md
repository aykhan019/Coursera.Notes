

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FIN4KVB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIAiuc0W%2BiSHeXTlkfrEeLvJgr7sww0%2BFxnSKUsR7D1%2BFAiEAqYei%2B9JckkNYpcA4iLAuNI3%2FcJwRojykU8SZGtkXFFEq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDMU2AJUB9VcVPlfC2ircA7Yx4NpDtKAb2vcMUzlRnfYoN%2FMD08lFsFWrK4zUoJ6cJcVQjpEv9gkAyFD6u499xs2JqF80tTpdp3QUbiYbK5iZUZ9jgXDIU1R0lMtIMSEjsZvGYgbw8DUXMxYHMsu%2BSWa7lU7JvZ1Ut0VaPdic2QBFZFh2YTv7553urJkgOPC0eJHK3MV1tmivzLClwJ2XAq7x3fp8CctrUweeFAP7xGwfeZ04OwVhssia1o%2BcLg0BnAvERUyxC4OXw9ADULGuo1dc0xOyp%2F9yZ7aePX%2FsZJLERzETDUZcbum4jYC5RjIArcPBKlsgAengpF5ZP5HmFO5GY5OcKP8kYfMqI9On49eztbbB%2FQMqOei%2B7wP57B4tb%2FJi0YvJlIp%2FDobCdrfoMyNbrdDnqxCqWIL73PCLUUb8ovwIbjHbh5O9XEe6rrWL6yyOY%2FeD%2BJl0s1iSf4fh33o7zP%2BKl8BXzUAJT48zAqkf983ZflAyNsceZG9JL6MgXftuYWAWhYt%2FgyeuVIfh5quaPR870DC2eWx8%2F5qVSP7lyRa4vrKTuLcL7ILJjivpHgSL6QthOIz2Np31oLj9EoA6E5NGntZrskoCzuzAAzK6HYDiyUW4AWQfReP7DY%2FVkM3TrcGpFndWujtWMNSuh70GOqUBNeBAHCHHA50dKcdXTYw5Uo6yrW00JuyMzNv01%2FplelzlP57g1cLYS3967MvHeRJwIoZ399H2el6BLs8aPQD965%2F01H5tyZx2Kp%2BA5xl3CBZS3EcBv6pyBjWutqII3Ss2JAaHcG6rde3pKCoQ7ytJzdAFBeAFnHEjOPr0W6VS9tt4jtn1d%2F4Y45baJNMRUYHqNQ3hd1HaAmQ%2BtCCRWpCyTiBuO3ug&X-Amz-Signature=72ed6de1541e308bbf4135aea0c2ddb75d9d40dcafdff944e6559e36444c5837&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJH2A3RC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCVqUWk8FO3n9nHVObKQ7x%2FvRELoO1bR9xUNLMEHCax4gIhAJMLze67Hx%2FgZIcwQa%2BfMuiOlW%2BvCfYCOXmMsbBEvi%2FbKv8DCCoQABoMNjM3NDIzMTgzODA1Igzm0AnTJRHoL3pfBkkq3AMG6pCY8AF0ADTJiUHeqSkqL5BC4a6adCZTtf2Dau538GOd0zBUXxRlZjI0XQiT7eg2a%2FpPkuSUuX8x5Tgm7AtrpdbY0Bi7x%2F7Iomd19RxM5xNab7eVjP%2Bi%2BDOnNVQVjaA97YHnWIoJRRBwNtg%2BaJ%2BOGCIAW52r%2FTcEaIa7YiqzsjcFQ6F%2BxSIKFePSnKjkXEejmAJLpSTsG4R2jPzji4iHNcaV9e5ARjLUry6%2BBnX%2BK5vZihOp9HRsUPGCfr%2FNwsVBmFXEuH7aBwtWJlyxSXuIfvc5l5gSQ2%2FrkN28gmeAy0UY1h0DNRCgUSrWtLNL8Rv2rGWUA3PUIgV5fZKZOP66Gn7GxzPM3ZAekUOl%2B%2BNZx2tbyHl%2B0tJtaZpAf0dwSih3rL3vCwHsY1r3KrD0rtx89YOPaV08SrUru%2BTV484PtDEeY1KEOZvbwpX09Lk3Dj3uU%2BMHbiokW2QQ7ywZikVFV5GLLGHbQriiVGCav8Wg246w0aA1vYtfsgVOvZVbCHWTSWLayhhO7mkdzd3D%2BlDBEgTiPFwf6umt02zrP8F8aJq8czTZZeEQxbzXN3bt5sj6Xu2SFlH%2FQXH2S1Zc4agSbKtJKMfavRe%2BT6PUCVcJ06UBU332lDMRYnQr%2FzDIroe9BjqkAXAxXHujT5dd5TEoRgun%2FxylahEh58ZPPcknV%2FUKvgURS89abltksg0s%2FwUigIgwaoLLO49%2FfrOU36pR29pauHT4t2o08NIo7FLf6e4P%2B6TN95L1RzyR40WfB%2BZqwNI7gbDEUfDm4QGsRyNHkF%2Fkv7CgWJkFd%2Be9o2gm4pPisyvqqfX6IcHKDHYZ6d9kCs27uFYh67HlV9p3Ow9Z8kZZPtHuABUE&X-Amz-Signature=fb8c1ad36104e3853c3122e08677c4d9a57a36261e99bf67572000f0e1f373a6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667COGPXLC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCznpcM9YoXTQoxoaudVX%2FBlHpHl5jVs62YiJCbAR8LdgIhAKR%2Bbcz2ZkM90El5QjVhBg8S97HJGYDeXf7BFKgo1fQIKv8DCCoQABoMNjM3NDIzMTgzODA1Igzc%2FzQApetOkAxVGNoq3ANM%2FDDavycCPMUMpzQ8h%2BWp3sZ4eGqHs%2B2tBq48WtiQtFszDN%2F6suOdn6ox6Fz3wAEhSkTBYRoYBhnIyz1YVCIVKaIUNawL19W8UTI1BgW9nvDNwJXgvTb%2BbOdYmUXhSCse01TtEjpD7PbPmIqamNpWGxO78YWHkCoFhsbc3pGMbfUh47PmD8vEBOqCu1%2FnAXYjsBGQARKy6lVlHAj4ZiVtYBzl2R%2BSzL3enRd%2FHd1pVxHH8hRXYijUmU%2BYBEsgfCp9Bdg5GEGhcQu04WZjF7Cu%2FAgHxkgxo4Qa4THOCS4NiLVHqtOIlBOAB8YCosAApJIkphq%2BkhyLmXIfM8SxD7DaD4YmQVTqs4Ect2IzC2KjTOveUroiN3mtyqkZh4VkB82A4qC1dgQ6JVahIAXcS2XJBx3fQvj8T7vS9k3ctJ3JfFQBApFR3cxDjJPknXl8cklfPFHqEHIbyasAlxoRKD3gOdsYhW77ugZab4VMqfV4sOYC6gEzO6yzWmzTWBrJHXRUYjkV8Jfq6HvhjHV45DvdzcqKggt5ppQlHMwoJtF5X1Ty9F8FMfig9ZdQ2Vq%2Bomi7dlfK07cOTT%2B7ru9viibX8gnCt1L%2FhS7lOeuHF7vW6hBF8M7eI4%2BjsP02WTDiroe9BjqkAVj%2FFvKncGNSoZYijtRJO3LDiEtp4rjsjusGGWrIZxALE%2B7r2%2BNAF2NyS2beB0YWHdFVU6o5TtNLxY5R6SvgLwXlk4NXuG4hB%2FtRBz5IsCjFD7nNUGNS3AKqT1XuLV189Y0c%2FBWiZVqVJ%2Bmv25mDsARPJveZYyBZvjjK3BQ8%2BwPuF7Uic%2Bf0uQkMauEXwZjNujmuYvXxLqON%2FbbwmbD%2F3KSmKvl7&X-Amz-Signature=93981d9870d7f23f64c6b8b62c78a6a7e09ef911d32e7702a861a79f6b1707eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDOD27HS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQDs2u1XuELucLE5qqJDYymFak3I2wYLgQ%2BbehYVQPKLKAIhALvoDgvnrA2pw31SvytG8qbsKhmphC0tjGszqxUMHkR9Kv8DCCoQABoMNjM3NDIzMTgzODA1IgybqpbXRPL0xBfR7Gwq3APbtLI9JvS%2BOG7x0osQNmL3i41iiz8jOgF1tfoB8vJmsfcwxCtYyvk5Rz2ubG1P%2FzSFfO3G0YHd0xoPum799dX5AUcY%2FtD%2BEJPg6QmjiP8lVt9wm7kS9%2FLy0DpkgUWci0N%2FSC6EW0bep37NMaN2Ym8e%2FL5lzO7WRdihiTagLbRbTxNQ%2Fe5bVyNqMJJX%2BXMxKPt51j%2B5WzqIqhUa4nGSPMwIBJNyqumPXFqLCeI2Mk2xk1nqrcvItPQwTRmHUW9cl68BHb%2F%2BRchzyh9KmhPfOL7xEftpimSi1nyXzom3XTecgrqdljGG6AxKxtk94DiZ3iqO967Cn5qzyT14Md%2FBbQyQcg9ze9WalWNPMuEO4%2F1WTll%2FUn7WiZSgVcROtoXPXR%2Fg6WElBgO09gGYc2y%2B2nICWwQF%2BcZrzWAIbe1SielKM4JG3btaFcDuK57RNjz%2F3%2FASP0k77ep%2Fs6ep1UvH9OibTCrGSFUPFPZUSMZYECwRj9r3O1g0zXDuAE3X0tlcCg6990xvKwDMsvF8mqAySCsPMMCLpiMiXEtQPFNvXukcRBuIderGaBhsVwBHb373MbHVj37TOhp53BYdqCP7AmlBOnKKHPGjyYzmb9QGptD%2B1aIimB5USLWMuA%2FLIDDUroe9BjqkAZbgPoQOhCbd1H04XgJjv9auFgAHZOl%2FeMVX3qkuot7tDqgDP4KGMI4qZaViohsU1k5d6NB8HZ3I%2FKnqiljo7CluM%2Bo%2BCHm7EeLkLZxwlv3uacjAMKxULGc5FjozA9AJpMcyM%2BieGQyg%2BDhn93%2B2DaK%2F34av6pxgTHdlacNqmTMUd1ilz92FsDXzAcgOY3dZNdnbq%2B7ume%2F29rsxqR838rWCXRmp&X-Amz-Signature=e54dc179971ed70fe320d6a334133415c6dee7a47baf6df3e980283c636a4500&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJGWBMWM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQD2uDWBUzy%2F%2Bc6ydyAn48fbDiUMnSxqBzZu6pfQo2ZsZwIhAPD4ugqlZKawftAxkwjxxH%2Fvpv2nlya36dnxa3hzPxPEKv8DCCoQABoMNjM3NDIzMTgzODA1Igy9%2FxLaWXbIv6HDBk4q3ANaR2iGFPEZRUjCkJtPEpej3IHVWRHkMtx3gFg5EZ3HE8YI6AtGbJNe7SAI8ioChfunORH62RWvpUn%2BNQZgGnSb2ylVMcmYygHU3hNUrPhvc%2Fr7jASfukcpVcLb2uULcuR0zvqyr0kX1F0gsE8eP6VmPhhj1iwrnBm7%2B58QfAfpgtLKve3BoxFxae8IvDNxddfaucVI9f8hdsGtNM1Dr2CoavXJonipyNY7fOmKunyex2tY0%2F36C%2BLDzjtFIpdB5ADKUQ7%2B6p%2BWsV1THEfmuMJcgqL8t8Z5YmLVK2PYbmAWqUEv6BOgjKoZpCF%2BUxJx3EfOuUbyymwLF7Qa55lc3bLKz2VOd4LhtQANQsq6%2BEAgDJ3OLo4M5PUFO3rZ1sUH2zu02BfORrf0ClZSlo5KdAa6dPoJhDgoPLVq%2FIWEZsYacd7T3%2FZdFBTOEIGzgYCzG%2Ft4%2F945C7%2B7ST%2BhvsnMwnURmq417F%2B9d6ruBGyEaZD5kS7SUiITT2JWBTLBXP6tpVe1Mt09EPfmiGW2laQs86e%2B0phPg4Xnx9aC4%2Fi37ioYTm0p8RVYLunCaqPl6d9v9EG6Cm4I3ApQHonOkkRMQV%2FA%2FK%2BR7KrhpQLjCaAKoK99uVa6tXn8iDpyWorTqDCqroe9BjqkAQtxmNyMPmmkwyT4TTgo4UpyRuhwiWoNvHmKiWoZwjmX8t0HOWowfA9Gobb2KaeBHL%2FP6e1TghYw7PlfAjaA%2BAkdv3cVgtJMDRxgIR4MCpBFSekz3O%2Fm6yuLZ6yug4WH0BP2ggNTZBskln2fmYyNWUoteceVexOIbH4Qjd4lH5deXq5mKzxNvUaRpld4W6McS3ooi9nWf3Nt24kpn4OCcgrzZw0v&X-Amz-Signature=be5c897d6213083ad8a370fc4476ddaa47520d3d87dba1f2ede5d2ec1e75bb62&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIXUAQOT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIADVltbTjd%2Bi6cWYIYeYRS1IU2u5ww1tHmcsp9R%2BZSktAiEAqVINUCEHUM4QEK%2FsFK6z0YgygRAnmWGcqqSwbyQW1qoq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDG51lKYtu%2B3e90E5NSrcAx7ZjfYBwLAzXWzE4VhKgFDdJLdxaRyHW4eYZ%2BQxCtE497V2Xe0t0qdvGMGCZldMAlNOBjhbMor%2Fu%2FXjSEY9ga7vgfvo81pbyhDjH20nyk0BUPhCcllRHlO1VTFrsVzHx%2BowqNqKLecMKfebloZ014i%2F90egF5wc0jCp6OKEd5DdO9sOmUgIUr7stF1WL6S93uVIyEaI7f7nAnVg6SyS1jZLUVVUFttIBPv0jqX%2BVVP2DCJsUDj9Cj4AS04QH%2Bza4O59OtrGnzpBkdU3JnNb5QkqwXzDqmFvobcHiYMIgInKuVX87cazYVi%2BM7DxfInd40XcQR0EIKEb3KCIp8EN0%2BBbE8pzjGorau6ABZ%2Fog6RpMHHkYoK2KZRWtWgbvkLJmnFD0xccgBf%2BOEO8nJ20sBipnx4m7vFsyhxuIf%2FRdW6dTmV8RdasoeAWfmIg3WrHmuf2WOIjuVQZdlQTmQvaFj9p58bF9oF%2FPomLyXi6884FukkR9pH57QkHypAhBX8ZYVqJTj0FsMDr0KpLU73ecAYHSgG7qk5Tn2ddZHl4voDv7C%2FpkI1goLN5dKC%2FqI3foOpsKn7zlJO%2FTGjpIU%2BBQcdL6tnURNZsevQuFGJV8BNgOdbjKzfwlyMj%2BOAnMMmuh70GOqUB7EvuQzSJm9YNMV8b%2BmF6vnRf%2BlqRN2d5MQ9IT6hKp61DUBVzkH3u8ZJETHM4bwiivLbS2P2BKK5lwKlWMOhSsPy73AgGRTi2ykD90MVq08POzh3l6Bk%2FnB12WAnMDlJ1yO5l9M%2FQVmqa9wf7nrDbwyS1e1hBgWH0l%2FHRgUIBR4iOjE5Xxm%2BYTkYYDXiTRXoi8TvLQJc8zn9AmadAuRapOcEC8waW&X-Amz-Signature=68d9be77172c914f80014b197bdc92193e5ed25d563c7414bd600668be1edf0d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEFYERFT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQC%2FLbdBHkBgOu1odhtOk9SZ%2BKSxgQL0aF%2FzIhccbwoaFAIhANLXmrVvoD4tXh5u61qdgo%2FE0la5kmWS%2BL%2BV8ia4wdgzKv8DCCoQABoMNjM3NDIzMTgzODA1IgwRfhXYGemJaAg7VdIq3ANaqIbN9lkeuQh2FD6eBoQ83Jr6oqDbgIQ2DAY%2BK%2B10kBoorC9T8IZTJ%2BKq0hms6kozU2PTXDYDnEb%2BEkPTcP7h3tZIQzfIPtMhmTy20Qtk1jtTjWojsHDJSHPaNOw8hJHakJ8pJFvFXIg2aMpg6Z6n5PRq13paxSeeGi2s8DWvcj2f2Zz8Jx%2FL7c1mc82GTIXnk89KyzDldUBoSiY6KBG14QqWWB7dOOK%2ForFoP0YFIwePQmguszuAmHlLWF5wAIjM4p4C0ATGMwApa4Z9aB2rioeTtA87Z3UI1dZwgwBJIYoW%2F3VVUOkJXTkTlFkuzvgB5drvEoqtBY%2Fn%2FfTksbjFcbScPetMtfILNm%2FjbD07o4NMuMEsLoMD3UN1LHzt2huP%2F%2Fjj2LR9Ub%2BcCG7m%2BpptsjDe%2FO5QLQ1hyErIJFIFnvg54vF2rYNASWjeWprBO6YLhcPaIJiO2OMqsfXVI%2F5MSf2YRgb0vI40tEexQWg%2FQcty%2FddL1izaDEzU4vEGMI9YAFnk27O5WiysQD1AQvrTJy0lYni%2FhPEhf%2BPXAGy6HIaiFmyiMVAXj1UPcTAVxvuJGJPUXiwqejXtF7GLd6RgL2SmHYmuqTCuHjJQCaoW1efs6kE5wz%2F%2BsFp1nzDmroe9BjqkAS6Sm%2BVylif%2FtjmCGxbpXHUSVJHMY9Vf7hON7SGgiECxHs4TYo4UjFx3XxEa9fom7b%2FXyb2fuwj2uFXa91RSN7DnA2kjXmcL%2BIDjIR5Jf5roRIrnOkICTPNNazX5g7l4la2nvwcZJELIAm9%2FMfjCBWd1YK340ZH4hUNyl83nrbcgLCyFu1%2BQq9W%2FOYHs1f%2B%2F%2BjvFxrpE4c%2BqH6QjV09QTpEnAK89&X-Amz-Signature=4456f7b1ba992035410e0d1f23a2371f4421d1ad853cc7fd0efa2fc7d11fa22f&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5FWW3ZG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIBe9VjhVFftWHj6VSrzi0CmmOENTlf8ZZhG9pbUNSJFJAiEAu7Tt8A5CAaWiTZYEa03WtNkuwMLMlZiuTJDLAodP%2FsIq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDGTV%2BbsJWnsHtmV3cCrcA4Wq8LCqOTfoDosDGAECCBSZ2Bxm18hLx2iKUIdIrYCFImFovbxjCJiKxozLgFovzJYmCDp%2FGcS7CoBeNifva5rniBgKKQFkXY55yYQVIt7slTlHP919m5md71J9OHAEyJHuqZ86QeRQcLNn5mouepuT0OuPjwo103w1ms7VV4b8ibJFNodlpFR6M6vW0T7YR6FJ%2FHTm1E8FsndDdNKtTslk72vAkPkqFe01IlIrJq1lp3LQ6irfnHfDbq%2FsCAJZmlxI1nlk7m1nBVZQqKRTRz0T3ctmhgpbyZBgX9ES4F6FIy4AHZBljPs5xzGwmOSMiNWBiXb4fFTuuU%2BsA%2Fget8U5C3Y5eKoH%2FGcXX%2BjdZav6lDxjQKecI2SRjcdm4Wr4qrpSbTHjP5sd%2BBgpQUkJILXgYtxmoyhI6ZpsnlG0LV3%2BkpCFUjRLU9BuoN54UADOdQiwWXyPf%2FPiF6lSVtUgLQXP5YnE7%2FqiYosdz5WuG2MbtiXEQQKTJh2phJcu4G9V9DphRaaG6yYVzSPKPGejDPCm%2B15lrpq79JrBns8fi%2B9fefjsWwIFlXiN6vmsSBRM22eg20UWnffE0gjU6N2W28yisuiraOxF6IijmQlm3Qs5qiIx%2BWwYbdUT55oAMNauh70GOqUBBC8Qi9z8nNowVyOaLQA96kxbHRYL1rfX2a2SYEsFUzhAVIFzGkKnoawB6byx0CM9NfukYZF5h6CpiVjd%2B85hrhTeiFfGoyZ1dHtob9FlQ2zuZbz66Avo98IuEwwkxnYTs%2B2gnbcP%2BXm6WCamKhmxrEoRXbiAkQ2w%2F8Av8jMlWlYkWJcUg6B62E4L8qzo%2FIHZohAsZmrOPngr29HN0JNTcSS4dZH7&X-Amz-Signature=8b53152d10d11c95e74f3a645a806eb8013d98fd400b353673f7283b2c2e4294&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJGWBMWM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQD2uDWBUzy%2F%2Bc6ydyAn48fbDiUMnSxqBzZu6pfQo2ZsZwIhAPD4ugqlZKawftAxkwjxxH%2Fvpv2nlya36dnxa3hzPxPEKv8DCCoQABoMNjM3NDIzMTgzODA1Igy9%2FxLaWXbIv6HDBk4q3ANaR2iGFPEZRUjCkJtPEpej3IHVWRHkMtx3gFg5EZ3HE8YI6AtGbJNe7SAI8ioChfunORH62RWvpUn%2BNQZgGnSb2ylVMcmYygHU3hNUrPhvc%2Fr7jASfukcpVcLb2uULcuR0zvqyr0kX1F0gsE8eP6VmPhhj1iwrnBm7%2B58QfAfpgtLKve3BoxFxae8IvDNxddfaucVI9f8hdsGtNM1Dr2CoavXJonipyNY7fOmKunyex2tY0%2F36C%2BLDzjtFIpdB5ADKUQ7%2B6p%2BWsV1THEfmuMJcgqL8t8Z5YmLVK2PYbmAWqUEv6BOgjKoZpCF%2BUxJx3EfOuUbyymwLF7Qa55lc3bLKz2VOd4LhtQANQsq6%2BEAgDJ3OLo4M5PUFO3rZ1sUH2zu02BfORrf0ClZSlo5KdAa6dPoJhDgoPLVq%2FIWEZsYacd7T3%2FZdFBTOEIGzgYCzG%2Ft4%2F945C7%2B7ST%2BhvsnMwnURmq417F%2B9d6ruBGyEaZD5kS7SUiITT2JWBTLBXP6tpVe1Mt09EPfmiGW2laQs86e%2B0phPg4Xnx9aC4%2Fi37ioYTm0p8RVYLunCaqPl6d9v9EG6Cm4I3ApQHonOkkRMQV%2FA%2FK%2BR7KrhpQLjCaAKoK99uVa6tXn8iDpyWorTqDCqroe9BjqkAQtxmNyMPmmkwyT4TTgo4UpyRuhwiWoNvHmKiWoZwjmX8t0HOWowfA9Gobb2KaeBHL%2FP6e1TghYw7PlfAjaA%2BAkdv3cVgtJMDRxgIR4MCpBFSekz3O%2Fm6yuLZ6yug4WH0BP2ggNTZBskln2fmYyNWUoteceVexOIbH4Qjd4lH5deXq5mKzxNvUaRpld4W6McS3ooi9nWf3Nt24kpn4OCcgrzZw0v&X-Amz-Signature=dcb438cdc4351e545230af96cb5154e5f037f555bf49c32fc4d0caf2c246ce04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3LTPPW4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIADHNfS%2B4rEqZMkFrEaxOfpLHGqCaoWCbUxkFDHP3Vo%2FAiEAgv4bScS%2F%2Bq%2BPGuRXf%2F7P9u8Ia6PzJTyyqX%2FgLqFt32oq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDIW%2FQ0KnhysAolX0FSrcA%2B6o0oBjS%2Bzb0LQTw6A39Bk63h0RI32XwnWIg58c3Ci03v%2Bp0rZ%2BJ9n4NFe55X3AWBQJKFYctjQSiuN%2BA0MuHVwj7Er58hvqZ0OV4mJCEzUFiAmvxgjytKndtr8EAKT3HC6hqgtUbRja18JM9QVppJD6LzFffgUStjr0UlIbcUGuqjOBFJpFvvcNz%2BEFoJAHqoE%2BqyHtITyLHtZ%2FfQPor%2F2yaj%2FlKpMn%2FUf%2BKbwM6u6vGux5ZHl6UDGWgoSibAoQPAyZYXWfgE4WLE4pfU%2F4hJR8RtFot2AwkPFLqUI7sH5JGvbjp9vOofJ4tcdOSeF7Am79mq3mL7lmi71JQUAfHY3vMEVYQxZHpTmbrLVVCKuL%2BxCx1U2rir78m6rdAZexHBzuRXIjcIoQ%2BirOg5qYPvoP3Kv3f34pKmK5b9rPlCaT4BHGlMSaSmlKWYo2l73shYTkz6V3jjnZAjRSaBO5V3Do3LKZRfVaNyZYBpVfeQg1YNdSOK2hMlgbs4vnlL%2BaIlYVCcnR0JlOcOFsJUZsLbD2jXaI%2FPlpk8wYiJOWJN%2FbS8jDdbIA41bFYAbcTFuyVxIPlaC%2FRQGwilLcvbl3LrmRBrk8i6yu8pIy4sueVEiJLD2C9K5HGgVCp1wdMMuuh70GOqUB98LV6FgUjUfUO%2FjVSt8CwPXLSx%2BKFERpawbYq%2FV1QBC206az7%2FUFBPc5033oVgPwVM7Oz4jBTKy5bA7OEqesDp9jttGUhUivX7K%2FN450RbaKZeC0jyTfVxxdH6w75J0UxlOJPnVQ1uvVp6Hde2TP0jHzAfbUACL32F64LVRiQq7w0v28I9G%2FiHD8HZYeOy0Y5jO8dI3KTW0tpb1oMW7tG%2BQe3bFs&X-Amz-Signature=c24de8294d2a525d90ae10392d2906fd8b343d3fade9b0144baeb09707c9d407&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3LTPPW4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIADHNfS%2B4rEqZMkFrEaxOfpLHGqCaoWCbUxkFDHP3Vo%2FAiEAgv4bScS%2F%2Bq%2BPGuRXf%2F7P9u8Ia6PzJTyyqX%2FgLqFt32oq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDIW%2FQ0KnhysAolX0FSrcA%2B6o0oBjS%2Bzb0LQTw6A39Bk63h0RI32XwnWIg58c3Ci03v%2Bp0rZ%2BJ9n4NFe55X3AWBQJKFYctjQSiuN%2BA0MuHVwj7Er58hvqZ0OV4mJCEzUFiAmvxgjytKndtr8EAKT3HC6hqgtUbRja18JM9QVppJD6LzFffgUStjr0UlIbcUGuqjOBFJpFvvcNz%2BEFoJAHqoE%2BqyHtITyLHtZ%2FfQPor%2F2yaj%2FlKpMn%2FUf%2BKbwM6u6vGux5ZHl6UDGWgoSibAoQPAyZYXWfgE4WLE4pfU%2F4hJR8RtFot2AwkPFLqUI7sH5JGvbjp9vOofJ4tcdOSeF7Am79mq3mL7lmi71JQUAfHY3vMEVYQxZHpTmbrLVVCKuL%2BxCx1U2rir78m6rdAZexHBzuRXIjcIoQ%2BirOg5qYPvoP3Kv3f34pKmK5b9rPlCaT4BHGlMSaSmlKWYo2l73shYTkz6V3jjnZAjRSaBO5V3Do3LKZRfVaNyZYBpVfeQg1YNdSOK2hMlgbs4vnlL%2BaIlYVCcnR0JlOcOFsJUZsLbD2jXaI%2FPlpk8wYiJOWJN%2FbS8jDdbIA41bFYAbcTFuyVxIPlaC%2FRQGwilLcvbl3LrmRBrk8i6yu8pIy4sueVEiJLD2C9K5HGgVCp1wdMMuuh70GOqUB98LV6FgUjUfUO%2FjVSt8CwPXLSx%2BKFERpawbYq%2FV1QBC206az7%2FUFBPc5033oVgPwVM7Oz4jBTKy5bA7OEqesDp9jttGUhUivX7K%2FN450RbaKZeC0jyTfVxxdH6w75J0UxlOJPnVQ1uvVp6Hde2TP0jHzAfbUACL32F64LVRiQq7w0v28I9G%2FiHD8HZYeOy0Y5jO8dI3KTW0tpb1oMW7tG%2BQe3bFs&X-Amz-Signature=3408ee2d0679a88d1741c6f0e96af52508a808a80599659329aa09eef06a78e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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