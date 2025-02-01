

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FJF5UMG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCduhdC9dAJrHGtNUSKucKw%2FrU1tEtOm81qZ8chflvhnwIgICG%2BwIVAe50Nr6mfgDkQN74wcgJfH5vYvLkNtPe5HUwqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLaVgsdE4pN9VwOGVircA2PAqlhqWI903iFcPfs0QWpuQWnesV7ooHio4rBBfimaVcis6MSlejldW0uHC7frzbnNmwuPYwwENsnX4t%2F6X320addEeLIrr0RykIio0sbeybJAWCt3cegB40xrey78vJsXen9C4xWb6QQ%2FM7JaDmQV5%2FBL1cVUt345OJbvn76RxHtC%2BDOOLAE6UeE56DrahKE1JTfGnsqSccbDoj6EJsT3K%2FnxptNfrUVPpgdTLPo0SOohcH4EWWLUhZhG5d98QUJoCYz2SDK%2FFADq0wpizRniyHG7XA4d9rKtv1s%2BD1%2BmL9qkaAKik8TQJeiOsALSINoAg6szey8DWxNelIDdz9k1g6UiXbWOPjxJfuec3P%2BfWBcpWRuBgVEgRKQn8bA85P1SQIqdOX2%2FmNcPfh10k9NopLQi7t1Tnpw9wYXVHK7RIxkygRBS1WR5%2F3gKtkmI1P%2FtJlQ979ahPLYRlNzClu54i88xDtIhmwj8sSrx4Rkw17x5xjjgGDuwItJwQRbjUusDYkbxJlV1i2E6gjvtx%2Ba%2B2bgT6JKcSdb0X0uPjVHImeyqr5xkQhjtFhURCzNSKz9KggpfZdJo33Xp1L1ry2f6gVBk6qAQXQNxTyH8UjAIpD%2FavrfVhvVchNdyMLP59rwGOqUBCTymtUSNnAoJ6geQioQAM%2FjPX2%2BOOHJhL1qft2DIDzFlVegLseDL5hCpiG5JlN0RoAQLnoKBQdqQ5qsvhc5%2BW%2B85CtMhVr3fbj4S43v%2FV8rZONl7uQDdw%2FccXCA1ylApWr%2F%2FjGYPRe0E%2FHwyHdTZaDrcObphiYTJ9qGLYnJ36QbgqnuU3uvK1LbtvAwAqOsfu1SrAqHv5%2B09ruEG%2BrwfV43IiFjW&X-Amz-Signature=edd581f279a28b468a107174bc22d69d525ea466bec35e2eb1bbdf1df980ce06&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ISFTFHL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9M8zYAaeTXtrWUIG7QZ2ETL%2FqnFmhyHThcu0lN7vOHAIhAMlyRoXVZyY0HZG8i%2F%2BnREf1bkF%2F%2FnfRwCszxI0b9aSOKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwNnT5cZ%2B3VYXogRukq3AOR%2BhYA6vW46YJJY0TjHoK5ywcfxG6Z%2Fb1MXJvlTBgRDab6df60%2FE9pvfGVDyPvs1uI4DUG4NgpBdHn%2FDxW%2FQSDPiLD9%2FnCU5%2BZe1XVedeIaOMTI4myDF1d%2FeNmIZkHGxhgq61U3SxVq0h2UW8Nx%2BBqCUKA%2FgTcZ7No4KSaYU7R7TgHMaIfLoAikDc9Ou2k%2FMWfyRiFuBml27ViFiftj99q83P55b9qqU7n01HA06ZHtuIMFPqxlbQo6F%2BIgsDtUC0dYMDfO6WTA2TzESAAC%2FPBECJljNqCdHgKg3cffeTo5Lpi6odTi6HbKH4GoZ3QYzP%2Fi4%2F2fMOthEB9UEH07iWcs7JgziLHx8KBYbX%2FfvfDbtL8q%2BTFT2fuvurWNqxP9zQv4Q58tpHvR9HePT6DE6ItmU%2FElaG0haXsZGl2ojzPJBEQe9SM%2FcvWw4njBM%2FD57XLXgsokYjBhsyFToSJOod60mDPyR4oHo%2Fghg64vfDEU1W7%2FFDXfx%2FLOUqi9Q8bduRdbWR3KUF26vVUQyYA2P2EPbTdXefjeeh28825zte7VEsmPGitBoY3nfEtgOeQbQBy7iSuTNUE4GiiZq855uO0CW74eJgVImH2%2BSH4V98lYWJc%2BF0VGxyN8SjaijDO%2Bfa8BjqkAZGcAQBe98fxqfvClxJJWy3sOS25OEW6FzPDC%2FgdSZm%2B%2FzYGv%2B%2BQQLFJ7QxL0Nan7IKSQ95gnZAaVv7dt9pUuPmLO%2BMh%2FzInz%2BXYJD6vAlxAxoAOn5wLHyoPQ2CCI2s8EnyHrmJ7BeDv0AlMlsZq9j7%2F8%2B8k73hd0egOQ9306FG8BLBGFi1Y57hlyOJQXxjJnehqzCdGU%2B9dQOrmhXezxzidKP0u&X-Amz-Signature=8063171c8aa91fd0462574f86b14eddbd3d0b37f624031fe532a878dd34ccdf9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666X2JLF5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAnvexUUjCOukbjs9kOou5fTkZCSas6fY7MNi7KYVA8RAiEAu0wxBZRjJxjkOEWlrgnECZcDxzR0EIO6nu7RIkrZP7EqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB0dg9%2BxX6RVzXm7%2BCrcA%2BPf5sqwzYK51hqopVUMWvIM4UhczNqUro%2Fs%2B8OEXwJMwxN9%2F88BcOOTRMNEUmBhzrpb%2BLaAby7oMv%2FAtW4XMOyR7joaXiZcjdKgHsEEicQ2Jq4Vd3X8llKeDf%2F7z3r%2FR3wtHFpBFDppDSLy4CdCGdUcTh8PoqIOeXfXNjQvqHszpNUSRmxQWMkUbO0pW6R44JwvgV5rPZabUNOP4QRxsrTuLsyDnfkWUySvPMIxDWL1PWI8rFkXHY3QsLlRQgChmg0K7JToZ0fLCXCYzlcECgz5LhGmaZDuxLELavUmoGs0zd%2Fsz%2BnGqptrR0ti6NN4jbuNwHO625n1X2O74yTss5YutQBTkc1bL6Lpa1ynUU1vnbNicI1WGWj%2Fj6GI6tUZQDeHIkW08yxH3pdhb%2F5HR3aPwBlRhz%2FjYBWppFO%2FHr1v6hrk8Y9BpGXLoMc3H3B0LpIPyVYtK89SiVLedM5u%2F5XSEJiieSpU921OSM7fFeeX9Z%2BcyEW10OSNh%2BSfGxasmwZfTdxnAL%2FKBqmqKshPSPH%2FOtTWywy1lk4qn2l4oxs%2Fde%2FuxiIvrPLbPD16l3B9%2FLktywRUjrlLp5ikjczXkV6wbvBGL89AOAKlff%2FVywLpnwonufb1SrTI9%2FYHMNT59rwGOqUBIPzmqIFevgxqVb7rocljG9JcK5T3jcdXhwxZNNCPoQsf%2Fun2TLcy8gaIiUN%2F1i92BiyPGnraR3GdxTHnPU8pQr%2BtrGpfK8qnj%2F%2FoclIbE3yIG%2BtCAfqYZKOF7onFQXbwnwviwQHef4ebUWFcLDrewNAqPq%2BpAyqkGOefFyUOWxHZxqoFJK25IH3zu2a2uGKZ5eMSa2biQ78JqSplpvknSiaU6tLW&X-Amz-Signature=55870e1a333f36a623fb154b1df69982db3dde790fee52b060fe2c3c34cd5909&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHX57P7U%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGa6eGG1dbDSyqSc33RROJlzaWgCp1ydtwDLS60K39oTAiEA9AhugeHReYjjrQIyOSrnyqCZHIh8NX9xEIa39ehxlEIqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMuNQQRO%2Bmnc56G53ircAyV%2BD9%2BN1ONQ4jpL%2B4IiUsESChzxYRNpmkSHa90J2HN3ESR5yCUR4CUv6o4CITCMNpl8YK1EevEnVt9KWxKNfHpyfkHUsnNLDPte7771XXaF3EluKGt8gWphjvNqH3to4iJknhcpRKJGz4D%2Fn%2BS%2BLcI8Zh86R2GM7csi6%2FtJ0M06JNtDeyuHFd%2F20sbqTA96Ky0YNnTchK9qGCxL7%2BtaZSZVrmde3%2FKdr%2FZVn5iWqvQwEATkZqf65Yw25ty7CENa838WiMReYDusFiYbcxUi2D6F97kOBWvek1ZLIRmI4oGSoQDUSUJSvUnLra2%2F8zqu%2BmWIMzdTS2CVzJ8tmA9PlSWJQ1IaKKO3%2BDGq1auCmV78yPRjQWQTMlNMOSFHtO4U4T1ZyTCmWCuyFAgQZKCVJK4duBfb9XxOkXiogNLpxWRPGSYuwDYOUbD%2BA6MC1R6TvGUNSwLl3lw43VrlOEB3Wmaxe2czVPeLnJXYduBY2eJWl2LkFghR5dCCirTBCoo3%2BP4q2dy80OIYkqylsm1Vf7T6BpL%2Bfn4cHzaKUszy%2Bdvf2MO%2F8%2B6klQL7DnUbATdoo7oQsYo96AUEpbvkmgTegIkJdQ5fQDtuFlIYkq1teCXEj1J4M5%2Bel4cwf%2BOYMJ769rwGOqUBsLZC%2BqK43FbTWemNSmKoRK2Tb0ffKTl0z9OH1%2FskzWQDXssAFQ%2BzHszgN5txoqRQHZQ%2B5yuwOWAUOOE6KLHJt3JaMLscnHIE16%2BXgyCdh3GRKX1xP9j1VGCU5%2FPf1JHdVhFiamXUoBDBlj39dQsxbHOzjeGXkohyiHPbv18nkG3XNbojE59PPVhCsZAaCLm2f18KrlfR6X4wEJox8qS4XWXF8yqg&X-Amz-Signature=388706d01a7a83cd70dba4dcad84e6595aaa2a88e6efaa89df3c4b3a7e3429f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHLEZYUK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID35FBLv6jnVio%2BAqQX98oudzmv0yYf%2FZYTKIrv%2BNMyvAiA840lVfCEmiS0zpEXuEcpCJGbayY7SuH8BOG%2Buhm5fHCqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMroH6XQoMvhywMB25KtwDSVMD%2FsGeEwRqFRxYCXDKatKmEZoC4ak8zyk%2B3ZpDFu5XpVl4pMIpRMDxNybt5bdeA93IrwXH4DYnqs%2BfbBsdwIjAqFtqPpSbz8goZqmlLiliSqle8a%2FyEjg24VSAdv0G%2BLOojOzeaiLsJ5gjHX95taYVBwoX90xr1zOs3btqtdzE5tzfIsyaAGysY%2BOT0wHzG8Fj%2FBTeS4%2BA2%2FhCLbLfu1ubkBlPhUFaWte%2FtdPCvPS4zrIzYc%2Fj1xHYxHA8phj4FLY5u3KG1Iqfs9TEhZuBBncAVrYO7Gj1Ls5T2a7j0%2Fd1zULdix0JlgHRMli0dvtwBgrH%2FJitD%2BGSm4S8SvffKmti9sZ4LFv9JSvRbntBha3I7GaTzBTFQVvGE3hHzDr8q77YLVOtmYf67Tb7pTzOd8VHQYYbAVaC4kaUtlXARu4HT9uyI2uMCtrXLI%2F6vKdHD9M%2BXlSApATGreeMzVHkg0Z6NWW1LMKPvnUf9F39ho5mCahYuWm72LOoQTGAAdpPwz2cEGr0k79SaU%2BVo4acRpLBJyxdZHYnGgIeAt0sVDCJlWG4vsaBSHQu8vXLFqDZAvzxJlnEVbiXhluYA9TirnquQguqbvbNLBGnEtY0FJgPN45q8AWERbOFaBkwvfn2vAY6pgGE8iV%2Bm5ZqgNx45UY6QxLb%2B5%2BtO01woGtN6cVpqtj1gUSo1ypXYKGluc%2BYJ4pBnUuX7NK4jnudQvB%2Fev28Cw3Ene%2F%2FIaD5DoS1QDhvuac4qqshGLSVZZxOsADB66jD8FWBSzV2kV%2FqGdHPL3RMf%2F2smIWL8GR%2BK5s8XxlgeQBmbQBuo8zjXfL0gwV4LBzCrWx1Qkm3G6EoU%2BYciIBLEW2NTJ7PuCPR&X-Amz-Signature=324d57ae26ee2d1bed9a1d53c5fbab2b7d2e2cf1e257dd1ed244522b906e549c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TMRWBOY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNGkf10d2tttdtinhOSs%2B08hosylykIEYghnl5AcZqxAiEAw5g97iTfYhOipwMy95NtCbn7rQfdaiuq74im15GIYuUqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRSgIuqGc5hF5KFNSrcA8PXaj8RB252oK1H0%2FdoRt%2FGcTiNhyOSXo4bw2rmOVP6Snbh4%2BFjUBgIEi9DEVlybIqOQQm8ZDeQu92nxCRa4BwGivtpzk3WLY5fcNhyh80J7N72Rr14Caipl%2Fz2B%2Brj4255QwJvSsEBbAwE6mATj6iEKS%2F0z46vXmE807TJCFpuEMB9t1yCO581d7Y7OqSyVNX50laQJLlNiAZFCpA%2FS2cdcpvYcR58LlHaXCyo6gT3TrhYlmTXJzYLEt0s3aicjazrA%2BnZqdfw3Rti%2FyrakTGrj8iVQJA70NVHqxTSq1vpH7Q9CkYhQVSAbBG8io%2Fc5ZXc2XkhA%2BpmpbuAaLWBbP%2Foi6SD23SilIhZ%2FUjZ1d%2FWC44G%2BYIfGlw8TORCOW2qJ587qAclNPHIzPZWnh70NqFSSR%2BjNrb9W0dH56hyaYQ8FLVcpGKem0fEntEF1NuhwkNuJl%2FvawcHStw1ybAbsTu3f8CUThCzJIe2BA3WHKdUMeQ37AQWfyhFG47iwu7O1x25AIZrdc0op2DikjQyVQH8V3Jui%2BGK4SdrUq4HDa6oHfb8hp49KYK8tRoprvHodko0uH4lPh60OmaMtRK5yEXy18Ax2uhAvbczN5S%2BlrxP%2BEAThELzP3tohhlVMPL59rwGOqUBQ%2Fzn27Cy%2F5fb%2BHW4kNEGY1vDEBGxfXr1uTU3%2FcxSGq0sOb2aUB3%2FiCIPQ3EDXQ88qekeip3wY%2FkoTdb6CxKbI6R8THwU2t%2F0PCYGeU6Z7Nxn7Z%2B8iTTgbIxbNlIUx3bEMMbVx60mgRQN%2Bef%2FtLtRG458jX9I6UobF10nyKeFMokjtphfvtEEo8h5taPLEJ9Zry6j3JpcotoCx1m0X8bIAkPvMrSL&X-Amz-Signature=0005bdacb1214a2a06b8c8ad27f46c91fe77f1abd636793b402a89a32610d623&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OFFWWB6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9HRtFIXFKnJQxnd676pu8SJrrT10dnqnD5AvRlFrOHQIgO5VHyKc2L%2BbsAsrOL96g1z6Ft8JRKW1pxcBew85cKwgqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCLYKRgMB2oMBZypRSrcA5WOKSRjjmvzmFlRLCl14mZ3bFXbCe5BUYncEs4ccg2lMQWkqnp5G5dbAfYmCyf6Mn4AIS3MVF8bgn9lp7nROTyjDg%2FFFgARRPenw1qQK%2Bh9VJwskxDE2%2F1wb7tWlvSKNPEm3X%2Fz3LgV4As4vWGFt5UOGzlUnDD%2B%2FTiumgp6wwPo6u5FrJs%2FbDJwC0puJmb1VgFEuKSAIRG3b3dCcH53BAaK626vacOgve1Nb0QUhI3%2BVI%2BF2yrRifgQElPgFgW%2BeVt1tevZoo%2BKSOjahiFprCjPBFzCXOmZs3vZjqUNiPjUeArHKPukm1MG5bJI5MFlMpaKRfuyZAeNub35sf0oIBc1dOl4DsL%2BOOrv4MsMIKw45JA%2BpqV%2F8UK7wmJ%2F2JY9yBl6IdlOhXWhYsVvf5%2BmItv1yaIWIU6rBqIg5P2JOpzo4uFM7yneQb63rro%2B0EyT4T1BJWriZZ6V18Jxrb%2BsHgxlxYDH9GLQQdPhqyzSwue6QaYtkg9NPAMOpSukpkj4%2Fm4ZamJvbYq%2Br7edW1Iv1YuYClE1B7Nou3FDDc%2B8%2F5QQqVRabHDKkS1ecGxrQHsLKwcdUpwRfPPYKqSHIOe6XDzSGgzmmBLkPP0IOmXmtjys1bynp57jwKrD1PzyMJ%2F69rwGOqUBJ1b0%2BJ5TD3CChdnhh%2Fp1nE95JsQcm%2BXwSBPG7CRvirn2Y%2BbsQMOKX5vMxA3%2F2kgho%2Bj085Cv2upQLY3tvMWkCp%2FxbuEAEMZJ3ftyM8%2Fa2zmSqJ6IzsJdJGoPSeZzaaPr3r3f%2BY4X1VBKTVJcKBeFkqb52x5W%2Fm3z4AYft%2F2Sg8dOSKAsssLMagZKoWKIZ9kFuSKk4EsXQXc%2B4GORgKunWmIBbNfP&X-Amz-Signature=584543f3be6fdbc5c93cadee7364fe185ddcc09b7e30896274c343387570bef0&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THQPDFEM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAdB2LBkU5Zld1s6wh2sS1r5oZGGL2amFKyYxC9tLLjQIhAJM9n6NUc4A1U5xeQRcP1Nty1ksngpY%2FwmqDsIHLsGjdKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmIMybKciXBOF%2BowMq3AOhqJ%2FY8o5lim7Io%2FuuUnM6TKIe1%2FBgcDjJREBRvIs5bdgoC%2Fae6nwn6qEJ8oMb%2F%2F7rUtOnnKoDLDt8o1KELAw16SDdZDTwIVGlCP5QYs7EXpaiEt58t99NmizWAq27qVE0sIfCk%2FW9RAXBINbynS2IiNuIuLKmKxmOaAu1UdJOuUc3OfeNJVY60CSqtLYPEFSlI4aospR5m%2Bj6O%2Bet%2BrEeK5w5XWy9NvC7OFTer4kJVZauUjJzsk0hqKTelWOie8ILoJOT2GctTTktaOWzb2Ro3MlZNU9fQKNg48SfqHW1DIIzt8Kz1z73NeN924bMrJA7DX5kR%2FFxzNRTcsXVvMR8DnPO8UfMYhYDuhWwLPDX%2FeNk8kxzvkpNvpCRRO80LLRjgVrqvyU9bwHQpvriT4fDSj77zQxhex8YxbpNrBg2SFrjjXvQ%2FWsTlB%2BCsJ%2F4Ph%2BBo%2FzNhPeYLKbGHxJGdNq%2BigzQqHEiHlJB04h1hKQgTOMAJFU1en8SXmrDcj384XAGe3ZAfXShcJ9aGee4U7xMQy0dIVbxGfXeHaOM4aJ4oo8B4D3SVvads%2B77ViWRw0ZbQKdJgI8zaImIh8CDwNBrMIP%2FvZCXItDdZLexbgjz99%2FibvD920lX3xZOtTC%2B%2Bfa8BjqkAQoJofnnFXvEzUP8sDquKP7v9G7TUWu6t1cnLqxjwoJr99Y2tPqOH5HnHCG6RH7aWw4MHGcSAix2Cq%2BPy79olygzZBeypWb%2FyvUnfPrTGaztKtHImnnZ7Rm3jGNEvT8fPo%2FX0XYn0GcQQJJmQsGnOVfuXxkaE3xngZDaEflCu4X1t%2BtegaO47dURA5djgfyuzJOEnxc0WkfnBAGUpmHW9FtkVwWt&X-Amz-Signature=5b22ff12274eb9238f8f17ff4b3499ad836dd1b8a9e1efa95c340e1a8b59fbc5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHLEZYUK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID35FBLv6jnVio%2BAqQX98oudzmv0yYf%2FZYTKIrv%2BNMyvAiA840lVfCEmiS0zpEXuEcpCJGbayY7SuH8BOG%2Buhm5fHCqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMroH6XQoMvhywMB25KtwDSVMD%2FsGeEwRqFRxYCXDKatKmEZoC4ak8zyk%2B3ZpDFu5XpVl4pMIpRMDxNybt5bdeA93IrwXH4DYnqs%2BfbBsdwIjAqFtqPpSbz8goZqmlLiliSqle8a%2FyEjg24VSAdv0G%2BLOojOzeaiLsJ5gjHX95taYVBwoX90xr1zOs3btqtdzE5tzfIsyaAGysY%2BOT0wHzG8Fj%2FBTeS4%2BA2%2FhCLbLfu1ubkBlPhUFaWte%2FtdPCvPS4zrIzYc%2Fj1xHYxHA8phj4FLY5u3KG1Iqfs9TEhZuBBncAVrYO7Gj1Ls5T2a7j0%2Fd1zULdix0JlgHRMli0dvtwBgrH%2FJitD%2BGSm4S8SvffKmti9sZ4LFv9JSvRbntBha3I7GaTzBTFQVvGE3hHzDr8q77YLVOtmYf67Tb7pTzOd8VHQYYbAVaC4kaUtlXARu4HT9uyI2uMCtrXLI%2F6vKdHD9M%2BXlSApATGreeMzVHkg0Z6NWW1LMKPvnUf9F39ho5mCahYuWm72LOoQTGAAdpPwz2cEGr0k79SaU%2BVo4acRpLBJyxdZHYnGgIeAt0sVDCJlWG4vsaBSHQu8vXLFqDZAvzxJlnEVbiXhluYA9TirnquQguqbvbNLBGnEtY0FJgPN45q8AWERbOFaBkwvfn2vAY6pgGE8iV%2Bm5ZqgNx45UY6QxLb%2B5%2BtO01woGtN6cVpqtj1gUSo1ypXYKGluc%2BYJ4pBnUuX7NK4jnudQvB%2Fev28Cw3Ene%2F%2FIaD5DoS1QDhvuac4qqshGLSVZZxOsADB66jD8FWBSzV2kV%2FqGdHPL3RMf%2F2smIWL8GR%2BK5s8XxlgeQBmbQBuo8zjXfL0gwV4LBzCrWx1Qkm3G6EoU%2BYciIBLEW2NTJ7PuCPR&X-Amz-Signature=05233f593d1e8b6e59d75199a1c206c7bc7f571d32bea94b7ac546226a6ad3cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NQ7MI4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCusXiYVZ2sgfkVO%2FgxC1DAedTibeUJWLfT2JsobYSiWQIgcP%2F9SvIVNR00GTW%2BYNQRm8YwGDQbrz6WE0guk5TDNSYqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP%2BT74fYvqJiMkc1jSrcA%2Fsszta0prJcnjvgeIiMbTgbIzROOdByqva05tUpOzohmZSBB8zPUtk7NWHPkHXXkSETDNPXGJQ9SccKx8eKu781kbBVVkvwhaH7vgfpz%2BGx576lyvGV0oJ2JE2%2FDlWFaNzCCBPaDtM2QjJBuwL04ipVUkCZZ1MWd%2FHDYlyUuJQzJwHc1JqzY%2FZltkt%2BouCmL5bSz4cTTA%2BXkrSjV92vdnxV6%2B9XRR%2F2Vm%2Fzdp0l2pou3wFXwDbokxcybf9idvp74Hop6MVfHK%2B1S30M50eM9vwIZv1050gPebiAk7H5PE9bTYOG5cwvn1kDnp%2Bmbwt6q8twryECTOk%2BNX4H%2FGJ79Wq7MnuCeqVmNSAVEzpjZI%2FfSn7quGGG1zSejRdL5ncZJUO57ujK51T%2BgVwyEOhOrx3knbQp%2By9cs8KkN2jEzfjRnpj%2FccKIRhgrFnCeZqAOersXrvXro4VWMu70NF%2B4JH94r9hV40AXlme7%2Fy6otszix1PBR9XG%2BAf1sHil6BuGPxzC8jgMiVcgdUmi5rtE7y0a4RRWPsEG2nDMACOMI4Dzb41BywjaiKlLAF%2Fn0eFZu58bjmBowqvNXi%2BSAum%2BnvxvrHkrfFfiWncv1p2rAe50ojBfJLULUwIq%2FpIWMOL59rwGOqUBfAKylzdT8w9SX1w%2BXiN9uomjsPdC7JA%2B9KcTDE%2FRc4N7cOxYSu%2FTm1ojNw0EvAGLQ9%2BMTyJFRdIc3EVCNkauc0JjM3FDUmRH00WEZ0jxWguAzE0%2BcK%2Ff4pv0B3lq6u0LwRnoUFym1vsCuwrtuaZEiwJgEdEC84P1eKi1A4Dzc7DU4XV7Zip%2BlkiZ%2FKYAOORb738HG7RSjsbY%2BA8rQASdzPi5%2BdCP&X-Amz-Signature=2e86b6ce5d74851d81d52eac08f1ca31134fe2c0d56d558342d4e767695160f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NQ7MI4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCusXiYVZ2sgfkVO%2FgxC1DAedTibeUJWLfT2JsobYSiWQIgcP%2F9SvIVNR00GTW%2BYNQRm8YwGDQbrz6WE0guk5TDNSYqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP%2BT74fYvqJiMkc1jSrcA%2Fsszta0prJcnjvgeIiMbTgbIzROOdByqva05tUpOzohmZSBB8zPUtk7NWHPkHXXkSETDNPXGJQ9SccKx8eKu781kbBVVkvwhaH7vgfpz%2BGx576lyvGV0oJ2JE2%2FDlWFaNzCCBPaDtM2QjJBuwL04ipVUkCZZ1MWd%2FHDYlyUuJQzJwHc1JqzY%2FZltkt%2BouCmL5bSz4cTTA%2BXkrSjV92vdnxV6%2B9XRR%2F2Vm%2Fzdp0l2pou3wFXwDbokxcybf9idvp74Hop6MVfHK%2B1S30M50eM9vwIZv1050gPebiAk7H5PE9bTYOG5cwvn1kDnp%2Bmbwt6q8twryECTOk%2BNX4H%2FGJ79Wq7MnuCeqVmNSAVEzpjZI%2FfSn7quGGG1zSejRdL5ncZJUO57ujK51T%2BgVwyEOhOrx3knbQp%2By9cs8KkN2jEzfjRnpj%2FccKIRhgrFnCeZqAOersXrvXro4VWMu70NF%2B4JH94r9hV40AXlme7%2Fy6otszix1PBR9XG%2BAf1sHil6BuGPxzC8jgMiVcgdUmi5rtE7y0a4RRWPsEG2nDMACOMI4Dzb41BywjaiKlLAF%2Fn0eFZu58bjmBowqvNXi%2BSAum%2BnvxvrHkrfFfiWncv1p2rAe50ojBfJLULUwIq%2FpIWMOL59rwGOqUBfAKylzdT8w9SX1w%2BXiN9uomjsPdC7JA%2B9KcTDE%2FRc4N7cOxYSu%2FTm1ojNw0EvAGLQ9%2BMTyJFRdIc3EVCNkauc0JjM3FDUmRH00WEZ0jxWguAzE0%2BcK%2Ff4pv0B3lq6u0LwRnoUFym1vsCuwrtuaZEiwJgEdEC84P1eKi1A4Dzc7DU4XV7Zip%2BlkiZ%2FKYAOORb738HG7RSjsbY%2BA8rQASdzPi5%2BdCP&X-Amz-Signature=55ee734de7f79a77e5e0ce145207f2ca6578169d3f3786c4878a583b024eb877&X-Amz-SignedHeaders=host&x-id=GetObject)
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