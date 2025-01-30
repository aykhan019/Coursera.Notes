

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XT3FBEL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGd0dLJQ2q0Z9Jag9N3oPBTTjdOQXYuCjtRcdw9YwuElAiEAs4xaab9shzYjOm5McWFitEA5yN3d18fnXygl9cmKV%2F0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPJJns%2F9wOI71iM8yrcAwudQFtNG0jW%2FStJCR9E6g3eoGAP7KJMYfJMmUBcBXjnsOLoieOa8ESS9vL%2BAPhgjFtkC74U53irOzHOn2z8C3y9qWILEOmdrOFNsiQbWQC9RueN1M9Oxvx%2F%2FKkEl1%2BwWRUrk%2B7WzAk6iJwlAmDeOHmMvbzdr5HCzqJC%2BFSjLGrECY7vAYARnZKxuo%2FSi%2BGdso5xfoQByBRvN0il8%2ByiTcwgeeLIePHQgWKJRycUYCdF%2B9QgvUcy0f4jhDuk7tHhWmATq5ijQ4nHuLQKciWjZQ2yesaNdCqFqVK2oypUo91nJ7ZvL0aUkepXz1cCT47KMJrUMsr7visFY6kk4Ox%2Bs4vB0j7wtXOVKbTZLo9ystQ6EhEsE%2F5ce8cbjXbxWRLEGmXZi3p34yvePYg2J3QZ6i%2Buq4ywCL7c2ex3Qz3ADqyotsQlfZK1W%2FULzdhweniMi73NW5YefEpTR0NJqkmPi2r6dlJEpg0iBijf78moU5cFzy7Xj7%2FYpb%2FjrdaBAR3xnyohONAnB9zpPwPXIz4U9GB%2F09ao61FK3BPH0KrbtFHEXOYxt4xLzW2054CEgnFJtnQVat5TSAPsglT98G4rI3ZKzDI3GrisEyWrqzgGBjZKQVT86ZpS8xqXtEIBMLze7bwGOqUBRmpm5j2KKZoyy5ldzHuTQa6yp45T8tNF8HRGBI33taysfGpeQwoiUqbcgDFRemfazQ2r2HJwM9S52BQ8WHq5gSjcnU%2BEo%2BgvAMKHCrjImfn8IuYXGnjibOQpUshp%2BWjThOebnyNw%2BNqBVpKSoFhofUVWkVpzz61Dpt1xYdXHwlaNRrEaTAHBsZxxkvgg5nrukUq0AP1ZyyUDfVh%2FuwvIjw8STzV0&X-Amz-Signature=38a1122ccbf018c13a4df763d57c9f6cb1a8cb669e7c8667f7d606c399d89867&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LDUFXSS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkGPKmVBlccP19yOlJKWqCjEUVVbAeLikrHFWdU%2FmDaAiAl9X5CC%2BL%2FIBPaVee341MGpyr7nFzDq%2FphIO37e0A0dCqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3hPbHloWJCiV%2BDdAKtwD%2F5cjLgaTY3KeyDaEDLqfC53SaG7zu%2B0IkXOKHyEMWS0rPjbp3bCDVzp8GUKEvPPzclfb37o06azLfx4dMPfm5p5JRwLVBSUNYdj7pNKrb8Z%2BIWSGp27few%2FafGivaUhqKmvwP13QBsWz4kA%2BUbxb6GNOZy9J4oNl8pzQu%2B9sbad2FVLDpKFT4LdS5lRfZezXMkvn764CHaBpk%2B9DtUrWEII7L9%2F9PpRoyE4SrfAQ2MJ9uMYzwZ%2BrbNHmbwWwRmGEkVL3Yj7OTkqCArwJtkWdGZEPZ3%2FNiiZICvV0ORJUR%2B2XbKxuSInxjA1EaKTn3qT7%2F2SXSOvJpHPz%2BWSVL6j6K3ksHUJwkEbhOE92rrNtNt%2Bg6H5zB46cznKJ9Qxt9D6MHTBAMZ7pUuiBRsOhQ8w4IsXmJyIl9gxSReMfVYGHaFNDpOS9OhtPCXMFY%2Fy4%2B1yHSVh8StKleEUnAUb0QfiZoGS6l1ZwGZJuWzKb059pOjW4G49k%2BnRCTE6Iae%2BnmA91KQjKNcory1K8ZJyFdScvr%2BDJsk05Czab9%2Fy24QsclwEUqEHCWBDeFffIOt5A0d41lTPjuoBZxB0wMfhdKqZmLH5AruHlj8I146ZvX%2FAVuucrMs68tpoZqL38CMww%2F97tvAY6pgFRCSUw0dsP5Qp8G5ll%2B5p7wkd6rrIOTsJeQbAoB8qmz0W1F4gtVR%2BQvxtcWcEJa%2BiQTf2fmqy4Xfc4Hpcbktp45p0pD4lTnRQIklvPLxJ8ds5AuRfBnvg6wNEmx1A2XLWsz1thjgMetDhg5soEl6n7mkLOPEAF04BJwxabNpEFZdOpRp6O9uZntHTQHjp8yQEsBfYQlcErsRLzAPLdCAu7L41g568g&X-Amz-Signature=bbb8f3afc7c2b2e1390e3a4434d72b31b2bdc70f055169ca0d53ec2c57f1d654&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO4A2OI6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE8JNnmflzGE4eInaCTemBztxGpV%2BOUp%2Bu0fONyOyVwOAiAonEJf2wS4n4ZqXIrP2NbTPzQQdH0ImOey5vBNAJfEgyqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0KKzAFJVp52Mv%2B4aKtwDjZKtpm303Qbk7qkACE%2F4lxiO1VEWMxlqUcoadruGF4f641n4HWpS2UkL4daud2xfnww4jzIk1HD9OIfrr%2FMjYiGxbbD76PeULTwmjFt9hByOy8pfUevbbfO2SYVoiLVb1HrdQbiaghK5bOPuePfWmSmlrplDFThJ6v4kEqD0MDdC5gSDLDupeefspaIHNHY9VqMg0EeihGp9pquEYUFfqmX4QHmmhPwXnfMy2jdXWqqMr9JIUzZLwuM6GeJ3pT0UY82k%2FLJQRFS8SSteKUTStG0sYmnDpkrLZejMTOUCfkXzym9z4PSvfqjpK261CAA8HJgrv2qzZrF974bzbgRVyKtTPzoGcwb5%2FKcgb%2BjbyvYbV6j0GStz%2FUfU0z5V2Jf1qLOQM8SzakjX1n2Bsl%2BfukcENo7Qohnj9TGMV2jEygmJ30GCugaoFtiwTaU1VI8y5RZty%2FGt37Z7Twmofs%2BX%2FC859Gq2qzIy7sO0D9iQ5%2FAthlNtbRZiom9HbeOM8RmD%2BNM7UEZveBD9aGh6lRwJLNwzHu0Te2FmPHVLD7J4TcaieSaDGwg8hV8BtutKJy5saT%2Bp%2FoEE7C6ZEgfNSojMTTPjOBDMCkoR0z5f8uVI7b1sTK4N6%2BdLxD4eg4wws97tvAY6pgEKRB263oouu084S5F7SXkJqHgSLEC6gaFLFgxQFzx0QCQlzT%2Bdrc1EzLduRt2izohjrzPM9Pq6l2w0Lzv%2BWJ3o4EUE7%2BaF0dE2IYzCZZkYq%2BNjH6OqRX3KjElhNCqJ4etfBwEiL%2FIkmqeQWXvysyZnjIV2VYoJ4Q%2BLaeym%2BQ34%2BoQ0heERP%2BBIwjLJakalr40ZfMuBli%2BjRJVDCbjy6ERrYUS6X4AW&X-Amz-Signature=5c92c0b5b1cb16b52d024be4b2590c54a028db797190f79d16469e379ff6454a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHBNGM6R%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFDhEQIs9vCXEL3DYgKTLrLgmeIvsUd4LJIj2d6YZdakAiEAiRtltsNkKHhncsxo8uQMcOiIgIwpD1QJyFN9r%2BL4R3oqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDAJgUWw31ZApraB%2FyrcA2R0AETdiIN0M726cTGlCsY%2FxWFbQcMOD2oH3NNHMcMvTI%2BzjbQHHWGqNN%2Fjf2VKISe0ulb3wVmFF14GUwi0MKWeHWD3g0y4okC%2FLx6VYJwS%2BAUfOieif0a30oNnV06z%2BGQnqVTviNGREveSKYoguQpmd38TcZklHssBE8SNfG%2BsZvHcSxE%2Fgy1YWuE0m1XOVtZtOE8IOlJqp7h9NBZzZU65jd93oCpvUZgElYWUR78gVELy%2FnXQswg2BfQu0xaZxwWH%2Fdlyc0J%2FxquPesKHwKctj3VoA24%2FInk77PXn0m5FZEeZ87Oi8yn6jsVeU4kqdBhe4oDEBMUjW45rzO%2BYE9rcx1UhK1XAwPADWQqulR5oHzlnM5Uv%2Bo64zZKmDZXYvVsbjlORfs4ZHZ7isAxC%2F2uqD9BjhU0eYqrp%2BJKO7mts12hsy0yw4d1SXLyGJ%2Bjvn8JR65NrQAdkJ%2Bf9UJaYtxDEMd%2BVWCtR5cmFPE69VeBASkxagsD7CkeirFtIPZ9qw09Vrv%2B%2BPrIPeBtEBCGkvsWfDYqvbF%2F1tsHXrrhZMDAB%2BZRrgsCcV2PqygBwFdZtEBIPwzHnk7wGweSH5xXpn3ZNFjrQP7cfIwk4RsQjDPOoNRFCbfIZ%2FOb%2F1A3zMMDe7bwGOqUB%2Fy%2F4NSaQitsCOfyGs9LUxnxIvEQsXQTqkgiYFBOqe88b84pgpsY2JZ3S6UCP%2FTs248qB01oZk2TTukXjUU9C4TVDHcErzg3klBX6vP%2Ba88YtiIO6piRaqbcmnErJBKO%2Fu7zQmUWFmscMyIWd50dM0e5czn6DrGRUVeN4ZpaS8ZFrRL61msFmxNOKalml7WQqprL6jlgXO9aPY7vgUNUMCtGm9YTO&X-Amz-Signature=71c43ca6de7810bf98d0ad9423fba66202b1e72d8cfc1294465fbcac02868b72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBE3MZRU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiW7nUGdmORiM1f%2B2qYPMLZcIt8INC7jYEIVhHFx4ggwIhANQ5mYSbJrRyOvEfLanThISzOOp1C1fvpDjZ8%2BssimbNKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwsky8nfcksHOq8q0oq3ANg9m2afjHwv26tbdkUrmMuwa7pfNGvyC935a1ZTu9DzsQHYckr7sOl4cprnesoaGcVLy7E93CDdFxeqm7v%2FfXZGU57CFZzuDaEDDSlBCL0pz3vc4lXS7CHXHbOamAH08g0a9jkTbzhsJoGLJOpLeL34UjgVsl8ecrjl8ofnyC7pyOK6CrRgvG0i4Bl2SIQUhIHBd6m0fDplUR8c3kVy7SukTJN8W1t8lcEWLSmBwgJXPMJIDO0bT5POVTEAumz3S7nzG5lQHX1eWWwwO9qAvT2NTNpO0ssWj%2F%2BlOrKVwbdIT%2FL7RCsWHquvYQQ%2B6dOLdvWXFyfnlGXDDWtnJEIWN9mWpPK29t47%2BHa0GRhIBJ1vakpgLr8nOCMRHpW9TO04Ga1eUBRv95omWfTYl9FCdTsd%2FZX%2BULvIUt4N9CDCDEGscCXrb9NGbdF1NMk%2Bz5AGk%2F%2F1ocalJEKXW%2BHxn%2BJvuUkx%2FxS5MAvuosSzbu%2FzQf9YRevdATynp40puXbb8GwiJbuytYCf4NoYRxRdX0UcjSnqxGya6e9WaoWK42T9aRh1qBTa6UpVW7g0sHC%2BkK6Ewb3DgU4J34K4DsCOAIR8ID0e4Wka0eUWwV%2B88a8wAM8Zka3jAT2f23dHCY7mTDS3u28BjqkAbXUyb5i7Ay8c0ga0GHeB5sAAxZjzavdJudqBcesUwywo4PLBjHHhHzVVIhovoPFWH6vs9fn%2BFORNEyWjDqJn0voP4n3IjgO%2F7Fx%2BZdCfeisc%2BRu4blVJmlhTfbzMqqtCqqOd25xnLZ%2Boiq%2F92utZgRTxCI70HPLHBBUdYMPUEUm%2FKFrGRFjTNhH6wrPRG0FFTmt6L379Mf%2FCg4l2EwFe4sguAfE&X-Amz-Signature=db63f4b25bb35db4be00089734d1e0f5d5f80c76486ab7d6b58f80395968741b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6GD2VNY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTz72dDx8Gf%2FSB%2Fw1WXjI8PO0Mhwn7p0CM4gE%2BHbtXLwIhAKDzQ1xFd6Z49Oyznu9wbCPAvAJys1zQYYLtpEZvtaFbKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxeVuiT1U9rzIjY1oUq3AOF2cBRawExKl%2F%2FUwbjai1aSf5HMaSsOxS9TE577rVJx6CM2Evm5ezuJJW2NBPHwfoD2vYqt%2BGHi1fFJjfa8lQBZDX1cM6uQOn1bPGMIGgm8kpkV%2BFF6PcnKvXVTtRoaT%2FzLi4Jmi5tycKj6OYGX3rbQMKl66U2pD2OzBs%2BtECqMb%2F9V8KT1ABpder0kfR5jovJgYw9ub4s3T6qNdykpZQ87NHF%2Bp6984LOEpIF2nR34WtmWNJrPANYbeaaa2DUel%2BSAJ%2FfqyJnid5WfY0UitST7Nj0FVvRty4tMtrrpa2bLNzb8k5gHwoVI%2BFIcRVW4xVSm0dDUzt1Gbqx7rCCxhGEwCS88btizIBbGP8huT4A9HWJYmxarQQZ6%2B2gaewDkdgNz%2Fc%2BBNZ%2F%2BLCCpmBIToBBG6hjRNvBcXgETRyIToGhCXvN1S7AddyjfzQAdlcZCQfzoEr8BRMrV9kEdJ3USz9%2BU46UsOb6Haf74gQTww8bOYljOWlVOfJyMDUohJgBkRTMTyJWhNzEck9OkJhWzOF2WOGN0sCLKmvPuQvWPB64SkQmEy%2FbVwoqmIS1bBehBkeh67fqpI6TsxaKGSUzUCOuyLKuLxFUXoOcD70W6FSNmQ8Hd6V5eAp%2B%2F%2FGBzzC43u28BjqkAQf45X%2FMh4bksHb0Dx0%2FpIgx02P81jz9OsbIFUd6rwkqDWEUWVmvJhUPD1HdOrVn6pMJOmwIj9hICHrD%2Bv3lpElqcQ9iju4nQrO9ubHAf%2FXjPfmGLc20Z%2B%2Fw6ZUVNLgcrRFndqi%2BxMMQt43%2FBzPNRAVUsntBlPeIAH36JnJpJWaCK1bMjT8ZId%2F9SfJeWEXaBm5dYC3pZEMkSjQudY5MwrZ6Ht7o&X-Amz-Signature=1ee6db61baaa5228fa36cea9e80c151129b521221fa2443a1277dacf74378034&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466626OWTFT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXSQdY7f1mroKBw6qWTKjcPrV7cQZyvPa0Gz7wzN7IeAiAgMUgc4l0V9206r4J1k%2B9Hv0e0kLBxmnEWydcr9PHkZSqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM70pfIJVBImxTSvJTKtwDigCh%2FFDPgrucg3bzsgYntuyuG%2BKF%2FKgwK3AaEHSu5%2BCZGN9OozQsDEfAt2%2BHYn0WpUPeTLYWvejXtgwoSg09eyv%2ByKNl%2FH0iJK56msS9pRq%2FgUjRfQ%2BmQLLTyGYunTzlmYxRmWOv4%2BVaYMUowRNdm69PKOmjp6hywQ273DTU8LhB8eX7utnjvfQrHGTdN9hXB6Gy67JxYWJn1%2FpJUTF5qYTpmr5KIs%2F0rZJs70djjAoHmqjT%2FGHTEfaWzGaQaPrB0Cpaqc3kjKh0ey8mlzK%2FiAavnVCqQj%2F%2B6Z%2Bj%2BQA%2B7CV6FBaW%2FOlRwNT3QrGnHObAgXSsDTISVQRBDA3zQnL8u3UN3nWVvbRjcUGFXoIuYxunYbTfKXq018IJqKnRKblT4iQLRSi9I%2BLvoqlv2f1S9u1w0ZDazC2vnfGA3Wxm%2F57Ji0OBnBRKqQdZt4u9QlVjGmXS1VKPlllifG5f5JlmqpBYDZhJKC%2BwJQi0%2FTI1Mxv7qiftNArn8EuKf13ZKNkmhaHrPZ1yX%2FrDZ0EyrqhpSuNaZBxXn%2BUYtc7nRmmMNW5wbg9Avh5Tyiw01fQoUMUcS3sS8vBJvzLITguONoFa0gWeVcz%2BAcsN57W4rorwsVHG1qDG%2FiZM9NGBQu8wgd%2FtvAY6pgGZQjVzwSJIGiDgeYLoNTosf7iI4b9R7QHpjR4hbju87UFF4rA55xTi6evICvNhypMFtqkDpM6t%2FjFfcuDliEgQuXz4GaTEKIwBrpeNkdNlD%2FmF8MacpbNyyE%2Fwzpqpj8RyhV5CGH%2BeLm0FT96%2FO7I45uJtzM1igmgNgnVWa%2Fgc36BFAazAAO5lTYzYouNlbPncNEk5T1pYk6d1D5jsTqGjfRvZYr4c&X-Amz-Signature=1c413ee948566fe66f5893af409362b61490bb95da9210e896c47f7efa9ad4f3&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NIBCWNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEAwSKRfOhQXsBIh5KvhHh195tQqzWvyTbNtGKYOPTi3AiEA2m3I%2Fm86Oa4oHGxxRubsDDEmkwG0Cs1m3%2BydAhCszrsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNBh5dFjT4Ggz%2Fl2dyrcAy%2FOKANrGpYheLfZfbgDq73Oda3GpNlGar%2BGRQEmVnuQb6wABPsRRnJiTo7IEDJ1bG4aLKa%2FC7yMNojr8CWRCy%2B7PbI8VihQERy4L0lEfRqV3uM%2ByClXHj2ollKkviFzPsc%2FWwum4zanVLuG7%2FwMgxzciG11s4IM57dqROfhXYiK83%2Biz6eGb%2BELZQla0JkaZwDe0UyKjy7OaZlh9neZhipM7JIi7%2F0TTwjWaJKiyPQgEMDDH2FcJBYYCd6ZokKnpBTtMkJ7idlLqPa6hSVltzeNT8JlA1VvRW5JEE1KzUpuqvOjmaki1eDto%2Bo6KILepbakg%2Fy5T8vY%2F5KvQUp%2FTgDoMyEHy2Bm9x4SHUu8TcYui%2FA6jRIThoo3aLFFNY76klNsL%2FzeSIyj6tr9XflWrjZ8GSeEIhG%2F2597p16hg%2FW7RkMZfeiGgTI%2BF5Vv7lnF7CmJ%2BqglzVa6qDBa60NA0y7vWDmg5YKpXNTIQdcA6W7aGdnYKOVIKdZYz6Ftg4MMJBMxY1SJJUtQtnKEHCFUxToGx5%2BOHhGcslbGzoP2Qu60%2F1S6HUQufCDWi0kaLWWisbfnE5V9WELpT0RNcQkbhJwNAR0jHJwjaHrH%2FZPhzBXNT%2BueKDha6Yb5ZfCvMLLe7bwGOqUBSa8zLgrMb23xYep%2Fp9jB0%2B%2B0J3GzQJFb8ciZh8aAjfvBHFvxx6iJhEYZsFRHySr9T7OWMJKlvWeseRmBlDM8DYTP442wlZ9mJ7Cc41yNUmF2MKuR99a7qv9v4nSXiY12WyE4anjSULvCebJ8uiQXzZXk5dcxqqqSK%2BnGIS9ovYqqyQkfVjoBQkUvWpv5wfSFeCy0dXyr6eyFyvVhvrNNrH386Hla&X-Amz-Signature=89313a97f9dec0ad6e63f149d1eafb41136fe744921883b836c3e6a988ece895&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBE3MZRU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiW7nUGdmORiM1f%2B2qYPMLZcIt8INC7jYEIVhHFx4ggwIhANQ5mYSbJrRyOvEfLanThISzOOp1C1fvpDjZ8%2BssimbNKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwsky8nfcksHOq8q0oq3ANg9m2afjHwv26tbdkUrmMuwa7pfNGvyC935a1ZTu9DzsQHYckr7sOl4cprnesoaGcVLy7E93CDdFxeqm7v%2FfXZGU57CFZzuDaEDDSlBCL0pz3vc4lXS7CHXHbOamAH08g0a9jkTbzhsJoGLJOpLeL34UjgVsl8ecrjl8ofnyC7pyOK6CrRgvG0i4Bl2SIQUhIHBd6m0fDplUR8c3kVy7SukTJN8W1t8lcEWLSmBwgJXPMJIDO0bT5POVTEAumz3S7nzG5lQHX1eWWwwO9qAvT2NTNpO0ssWj%2F%2BlOrKVwbdIT%2FL7RCsWHquvYQQ%2B6dOLdvWXFyfnlGXDDWtnJEIWN9mWpPK29t47%2BHa0GRhIBJ1vakpgLr8nOCMRHpW9TO04Ga1eUBRv95omWfTYl9FCdTsd%2FZX%2BULvIUt4N9CDCDEGscCXrb9NGbdF1NMk%2Bz5AGk%2F%2F1ocalJEKXW%2BHxn%2BJvuUkx%2FxS5MAvuosSzbu%2FzQf9YRevdATynp40puXbb8GwiJbuytYCf4NoYRxRdX0UcjSnqxGya6e9WaoWK42T9aRh1qBTa6UpVW7g0sHC%2BkK6Ewb3DgU4J34K4DsCOAIR8ID0e4Wka0eUWwV%2B88a8wAM8Zka3jAT2f23dHCY7mTDS3u28BjqkAbXUyb5i7Ay8c0ga0GHeB5sAAxZjzavdJudqBcesUwywo4PLBjHHhHzVVIhovoPFWH6vs9fn%2BFORNEyWjDqJn0voP4n3IjgO%2F7Fx%2BZdCfeisc%2BRu4blVJmlhTfbzMqqtCqqOd25xnLZ%2Boiq%2F92utZgRTxCI70HPLHBBUdYMPUEUm%2FKFrGRFjTNhH6wrPRG0FFTmt6L379Mf%2FCg4l2EwFe4sguAfE&X-Amz-Signature=68130f95ec4b8ebdfd9ffac5665cdab07aa2196cca2fd9acbe85e8c48af29ef0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SSYHY6Q%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcLFOLN%2F%2BG0yIRIbUegHzX41TYZ7pGiQkeTHk8fwT7XAiA%2F16NcXAdYY%2FE%2FaSKXGEC3t3e8WwIX9RiMSB3R9QAdGiqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGfsXEesY4Lm5MC5mKtwDC4sEawaIVLklMsuo5EPaEwZUYy84%2F8U3zeQnpwugLfLaYGIu14MBqT25bSAxgdotAoNJeC42Vjhphf8Pc9MsA03hyfNqR%2BlRmpfGy1FyDwRttHOAaeO7bGA6h8Vzs5Q8zGD6N2ahgAHGcIj6t0ERAueDgKG%2FDtHR%2F7XSemCV%2FsvUsK5lEfMnXfA234gyo5mm2Ty7lGNfzezv4WsXeJCVGgeZyMNFs9PEsrd5rSae00X1Omd%2FnFgF5sqboXfRx%2BKVXLunbRs2%2FSnBwO3d59oe%2BfXWSXNdw%2FDYkQOVXd46z5b6zLf5habYKB8vZd1RnWpjs6VW%2F7auM8eWZaXHK1%2FVhY978wcsX7aa5zBxjIrLj0zzcZnZuPQUO6p1DzremL%2BAricK1CoQ2IdlLpIDhAouB0Tl6C1TFAqqWmM%2F%2F2ZY3xX6oMbxCiUAZs2G9CfyBVrfKNxb21BZPgrob8gpjJitGaK7RdKhC6Gmn47AUjodE2BRZAQ33tlhY0SsC11RDeBxVSKa8Wn4vSIVsX3d5G0fr1O%2FwEkIi6kvii9FFSSnsZPDo1x2qUUhgT%2BasDKYy8HiAXTK4hANTMPcrxR%2BjDgGRb1YW2fV9wLn%2BOat%2F%2FwfrjCN4S13H%2FMSehlQtUAwnN%2FtvAY6pgFkZet4mDHZ1MGx%2Brl21CnRQ76z2IsIeeYthhPuYt9PxRm%2BCHGuILEn0s54VNVXKAZqyAOXr%2Bb4xYq%2FRqyyM7f6bHeA9RMcRP9Y%2BBehKckQVcnNiJMcl0H1iv%2FJAuBk%2Ff0KKZSwV8qsNC6iZzX%2Bx%2FvQwQdjDxbZBtdcRhjQvSoF9sndbV6NIsZpx%2BvqIjrSufDF%2FLC0vE0r0HxeDFSS9IOfJC74Seq%2B&X-Amz-Signature=edc9c32c607f2395ca032c0e5c683dcd91bf305f71298f91329eb5f14e1f47eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SSYHY6Q%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcLFOLN%2F%2BG0yIRIbUegHzX41TYZ7pGiQkeTHk8fwT7XAiA%2F16NcXAdYY%2FE%2FaSKXGEC3t3e8WwIX9RiMSB3R9QAdGiqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGfsXEesY4Lm5MC5mKtwDC4sEawaIVLklMsuo5EPaEwZUYy84%2F8U3zeQnpwugLfLaYGIu14MBqT25bSAxgdotAoNJeC42Vjhphf8Pc9MsA03hyfNqR%2BlRmpfGy1FyDwRttHOAaeO7bGA6h8Vzs5Q8zGD6N2ahgAHGcIj6t0ERAueDgKG%2FDtHR%2F7XSemCV%2FsvUsK5lEfMnXfA234gyo5mm2Ty7lGNfzezv4WsXeJCVGgeZyMNFs9PEsrd5rSae00X1Omd%2FnFgF5sqboXfRx%2BKVXLunbRs2%2FSnBwO3d59oe%2BfXWSXNdw%2FDYkQOVXd46z5b6zLf5habYKB8vZd1RnWpjs6VW%2F7auM8eWZaXHK1%2FVhY978wcsX7aa5zBxjIrLj0zzcZnZuPQUO6p1DzremL%2BAricK1CoQ2IdlLpIDhAouB0Tl6C1TFAqqWmM%2F%2F2ZY3xX6oMbxCiUAZs2G9CfyBVrfKNxb21BZPgrob8gpjJitGaK7RdKhC6Gmn47AUjodE2BRZAQ33tlhY0SsC11RDeBxVSKa8Wn4vSIVsX3d5G0fr1O%2FwEkIi6kvii9FFSSnsZPDo1x2qUUhgT%2BasDKYy8HiAXTK4hANTMPcrxR%2BjDgGRb1YW2fV9wLn%2BOat%2F%2FwfrjCN4S13H%2FMSehlQtUAwnN%2FtvAY6pgFkZet4mDHZ1MGx%2Brl21CnRQ76z2IsIeeYthhPuYt9PxRm%2BCHGuILEn0s54VNVXKAZqyAOXr%2Bb4xYq%2FRqyyM7f6bHeA9RMcRP9Y%2BBehKckQVcnNiJMcl0H1iv%2FJAuBk%2Ff0KKZSwV8qsNC6iZzX%2Bx%2FvQwQdjDxbZBtdcRhjQvSoF9sndbV6NIsZpx%2BvqIjrSufDF%2FLC0vE0r0HxeDFSS9IOfJC74Seq%2B&X-Amz-Signature=060f7b6a5c260a42803c91a9e087fd2ea23b23e4f7e363eea9bf9713e0831966&X-Amz-SignedHeaders=host&x-id=GetObject)
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