

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXAO6SFE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgD3P9bp54aTup6JWiLQxaB3TSiToA0gBsz2BjkFh9YgIhAMVANGZngaIoIibtS1zg7w1ozuj1jcgqKTujcZ5%2B7k9xKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxkLwV4Akf489d9rIEq3AOrv6kJp0bzNfFxFc1yl%2FgLiNtk%2Byvv29ce96YDLEJCY8sia%2BxSzOg410FlPJMG%2FZ5gZvusrPwEYJK9j%2FIy7G%2BnZtmeEu54IntMsFnaTXsj6bggMC4CDNa5Cf69FlYa7GEEgXubKiFgRr8zHzfV4Eydf5BLhXFyGyqWut8CDoyybTX5LPUSWxbpiYODv7WssxHfbhQ2VwufF0LXYDmX1J4h6YpTIKWzsp7xkuzKg3VQZnnymoCz5ih7eSBxSEhzpVbim2Fae9runofpWpCWCVLwwFqXweodcgTyR2LpqDSH3%2F03%2FZzOxqnYqjVk1w3tKS5zpjFm4Tby0X9M5yuyYnKn%2B33KKuFzFwdHziLLuMJrHpzhUAim5seTUhwPWf45AMtnhj4zEaYQdGTwrO392b6aR7tYnvyLwdjpTMhtJyNVydJAEw%2BhuBxHM92QPB%2BkhUCOnZqrNTwMd8I4WQ3W%2FYbuwtEcX7RPxM739NDneiv12DcBayjqgBuflj7LhGz%2FofGfGHcO%2BxePqyG6WRcZyQBGgjjQBYfPZi7Ty5S3d8pIFBhB9VmvorR%2BaTk2ZoJA4vLzcI1SwEK4tDOz8NjFyexACpxe24iFXlE3rv%2FstivGvb5cxTkHE3nNo%2FT4PzCP4e%2B8BjqkAR8KZozXi1qCDpz%2FvMYE9NDejvh7TuuTaqlEHGbg5RzLF7F9wo0%2FEFyRfwaHQG4Su5wxqp178gCgoToH4BVZAUBXw5BqYOZPyIRdFLii30YtqmFo5GZBZHGDXuYgIzhhMCJ%2FVd31vTIsgrSh0hgZ%2B%2FtAu9sVDjt5helEUzrsLYuPCJJsK2oSTiTG9mUcGb%2BJdbQbhpRikR4rXfjdyDXQriwvgP37&X-Amz-Signature=882e65bc95cb29cc349bbe4fad8375a7dc03e7e300742a1851befa04b16ac04e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WFWYX7N%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCPQ%2Bzl6sfYFQoF5uNII4FOLE00GNjh5A9SkR54rwlBgIhAMj%2BVPZo3LXb%2FnQfQf7WYa5AO7OAk01TZDHUzgvEMn%2BcKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx5MDx2Uyqp0hTressq3AMJbR4Ck%2FyvbYwvf6Z4gH5RchLw2kM0L%2B3vB7g4DwCMu8vXtmDZIF%2F58Yr%2BZ4pBd5r0JqpHW6YKuesz5MkhyR1bHLuLLICDQzszrONBPru3CDOH3jpNw8WqeYqds%2FxcjTLncCvW7WoNMa6cuwSL7ids38IA7Us95R7aA7nzAwh2T2xSXXqRRpypt6HmCIR7ycCIP3DBGt4%2FAibvXNL%2B%2FAx2czHO%2B5i8epj%2FEbiyoBGz5UcHsKftgJXKp2UiUImPDD8fu%2BdelrMMVheyJWkk9nXp6lAuZVsmd8%2F1XgDfMrvRGrCDYBQy0DggoI%2BZWIJafQuJp%2BVA7HRqQPEROdASY6UH86vrxniFttSJB0u1va65DE%2FwdtRnB9grRdBtuZcsLxfjtjgEeVSIQ66BROihLrIY5AKiVvhh%2Fxuj7xcGuPYcJQj5xCkjegRHQXP3R2XAH9Qn8taeQWtn3PhLLP4ixsfeGjSx%2FWPLZCB90G2XOUxjGSB6lVlCQVbJFVk08P4xji5PMv6qNjt9MSsy0ltaOwatJEkVNPpXtR04Vz%2BrHoe01YqaD41dtwpZT2E7DscZGaMWKk%2F4Lz%2BQ%2F5QONDWtM2YSkGIkIjpe64F2ciBrGKAjoiUpDe%2BlL59AvoqmSTCw4e%2B8BjqkAXT3YnZs0rKH7UHiV5JiXeu1CcLyzlaKbVroSlHy4hFcjWsOtujhOISVqmTOYdbgPF4g0fkj97QisfmMGkM1fsMNyjzMf9807nuBVZpxc9WXmDkMr575fPa3qYtWkMtWkNPQa%2FdQUyk1lfK7KkVxgZNiljRCkccJIOJDJv%2FRfuuIPCKI%2BMYCDxBDXQAheqsU0pAARTIEzMS7AHrdTAip3YWJc%2F0l&X-Amz-Signature=a3335b21ae0c444d2b58bc6bd3fbdb6ab6b70b008f743ba9a33290f3f1544321&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZSEGW2N%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDQ6x7DPv9aZ6XaHaYGtnfJBBCDR2KCHB5HELPEDl%2BDQIgfVAkk5CSsl1Y6gyDTnb3o0YBwPU7UElQDYtLzuEY5egqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKi%2FG7NK6sBKnz1HWCrcA0%2Bt22pEQhjMW9esmGxxDyADosV9myCVQzg13mbnBcl8h0ZvTG%2F%2Fum6ZjeLL6INzMkc2RGVcRsFN1WIG8qrw5xb2QjAFI9Vw58Fqxw2JLkuu%2BQkNLRe596eWnHUmVxdvOoXQCCUUOBChPVfSbZZSwVAvpK9BXMCGtl5kfKdy1NkEnpiqYD317tBXVLt4Qga0DciCGOu2va1PQfa9C2tU%2FvXlVGsaEciuskgo1nF%2F8vPyeyEgHbOtnUJUI4QNVDIaXrcOcBv%2FPSgDPLTUlxEAdkRxfhfJM98VLvmbgIALZtrA2ivwHeF0pldF7joA3hx0kd1sggylUpBEZn8TF%2Bm2EyDZXt83Qmlwy4EXVrCq5FMbfKtFkT7eWQZKbvAh4MC0OrxqEmEl%2BkaPLOH4ruPnBtedB6kH4c8l%2B8VHmjgUsT5DuscdaeAS3V3aij4NGcYRIiWfFEwmTDAQ36jX6RifCPgRjLpD04MiXUDmlXtK3BUL3qhjaZdB1MTOZeeKNxsf9hrWLOM5hhX2aZhDdFGhtKEhrkukM70acenaskchI014Lm7DJ96GM8SCuhSjIrU1TnA1iIG3AIIlY3g3G2Zfps%2Bc4vM8bbU5mE7A6%2BeLxs69FxSpprWXAbI5GP4uMLDh77wGOqUBStS50wzAu5XLx3CJ9ABOu%2FKXVYCZYb92eg2XKu1l%2BrFStAxJIatrADvkReFQGHeqyucUNqhCE4azcra1WV0txazNw3p6ZA26uN8OAxxKlURW3iqQULojxjJpmxsGm7RcdnQl%2BEVo6qiFAFBu16KZigM5NusiwBpsmwOC98G%2F6jy6LEy%2Bm9KpiR%2BsEn4ia5LyjL1ZtxtX%2F0fpD7MDlCf68t%2BPd74Y&X-Amz-Signature=ec4a65b9a1fa382743a3e37f8a29a83524c688c130243438299779707b137ab9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWGRHZ3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuqQ%2F9J085g4lL%2BEBrY%2BqtMwzwpt9EtTLwfLgS1ARpggIhAME7MWn0kS3gCEuqhiX9fLmME3mSmH%2FjcpYPDMSS4xCvKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwC5rtyZlSPTbWwRP0q3AODqXVCKauGQVNFen0dC2F95J9uomUiMxObiUi5iH%2F7eK0445JnBYnxK67nDC8S4XFfctLWX8bqp0W61W4OT99go8krDYNMy%2FbANSRY5NXMrjxOzYAUwdMFoJSCnuhyEMNHis%2Bv%2FniFyUnCssp5gkKDGTglqwzbjBQCUUJ7E%2FBfzFjRh7bgwZtfIGOsZjA6CqrlJrJ%2BAHg%2BgBWhnH%2FBc2cQwaUcvoQ1pAybTPBE2hcH6dsI%2FQBvKK2ZhM4cgPW5udsoTJAVKyqo0mY5H4WRnJe0y7RUgkXLLYDAmDbAhL5%2BeuS6KPoqAllpwqC3H2LQSF1TqVW%2FgZ0s3ANDa0IHr9fm3jiez7p2RU%2BlUlzDVLkqFndSkYQd6vQZ1%2F%2BlzMyUbShoQlZsWmOUdQCcdsmhNAc7AlztT7lX3L%2FAsLcN03%2F%2FBVT1TBeHtt1k5sAyKo5rNw%2BnNeQhw6f3FCzYr0cJjxU9qRurOl7v8%2FVqHqtrBZyRLV%2B2Z6KclU%2FbNmgPbL92KjKIz3TuJDA3b11y%2FCrXLzIct6QCWvaMq50Foo%2BOyOSvXjudxG45ephKDf3EH27YeHi8QVuziPRG3923TzTlWREqV8%2Bl99S5apGBKfWD2FngFVqmXkOOrb2yRiAKuDDi4O%2B8BjqkAXdyzY2nnIquY7%2B%2F3PCKtHTZm0RTW%2Fh65jBy0LTmi76N2hA5sqmogkheEn3ZW3m%2FeBLyOxCRfXe4eOiVztEn9ecFHFuQQ870K0ChfHE2vRGnDLarPBMXEYckIiurrTpfTpJRyh%2F7efeLrsfezQcFPt68A4XxY8x2CC3LFY6Dm51A4wCPmNY8fLKnP5r0n35BY8QUDoRBQLOYTf4YrIAWkDvHNKS%2F&X-Amz-Signature=f7712f4ff439863396c8c512212af4604c400b7c292e0cca626edd1622d8c156&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SUY7GMQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BQ2cNCwz90zXPXuVXCdMgIAtvoOjgwHmmX7NShfFvhQIhAMoV7a%2B93LYve8%2FdYVKqrP0HRB9dvmfdkAusfjiiVwrgKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyeYdTWIUmwt6yoqHUq3APKeIiSSJP1XbDz1ZTDQf%2B0reD0hL3SkG2LC8zcLHAiF0UI%2F9fRC8TulDkLXrg3EOglHtbHM1bGJdLXLI2WZja1xJFfxiTctU%2Fa6keQIy6GitlU%2BH5JQBRtRQAE1GAtCXpZcUqgyEF3waNY2VOkqEkxpQjVREudJrX%2FBPaI9a9Gm2BRnVUQ1wl87rgxvYJswN%2FjpRmfekCu4KJq03wQnYyPBwencLWVOP4QsJl9WUqO%2FPwg%2BBpy4C9Fx9EH19HaY60txqRM5l4iKy0evR4NAa7ujvpJiYeA3hqRFHdKkBdkMTl8vfdmdEUm%2BZSV1PJt21YmYlFeZewHTiTFAVlJE7Fw%2Be7chH163dgbVdZcJq373rn4xuRGV1TVDHAY%2FlTBvIJHZ58QAKolYntds9AWQfNIhCmkrscVhJcIA1N8m6SuC%2BhbcUeHKUih10YoZc1sSKQEJCCg7GFtzDDNsGeFQQWdTOkfCVOAU6FjtzIaq1h9RMzc2wK8DP821mN5NvV3OCzzgUQ8Ko0gCrgibvTEFt7xXHrunEalo9hQWEn3yv1W8lKQ27nOeNonfMwxQoaNQf3kJMD16Qid%2BiDtOJqEzHK1Lhd99o2ytgFVQHXtWQDLWrIliZd6XDmZniHnsjDn4O%2B8BjqkAdZhjpo7HuyIa0Hw6jlipMdGUWS6Q6QHaVDa7rQpzT9R0u43stl7lK7APulxgNYB83GHZjE4uE7hif8tsRQNiD9QG6zEoNjOeM%2BvX47Zs%2FvU50sOZhRn9Z1%2F%2FQ3z8h7M9QQq2HHpOwPfQYIw0j18OAxaHICIcsBOCmBWeyTNjUd6t53opW%2BzUBAIOBACUMeZ5QEJQPbsfQpiBgopyVF2wMAh%2FDPE&X-Amz-Signature=0f7c7269159d9149f52bb30fc83149124a63a4a28c92d7a90262b7835dfe1260&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGDWJVVD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDggDs%2FO5ByLxXqwyZo5ZsBkXQKJJOhaevnGRLuUbLMUAiEApgN2Irl8d3X4Kxg7%2FEp%2BmUVOS3JtQJsRxZM5A9r6WvcqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCGngiTa3xY2yyakGCrcA9CvzO6PAWoIPfHttuxNW2GTuim%2F3fPrsav36YukRP512VmvgoWcuEaPd%2BVjV7X%2B6UWxHkcSAmAHzGVo%2BLJTq2Am94rhT4oYmb1r8SVocUmdaXT%2FzH1eeyKngpGZF9hS9gxAhdHK7F4KWYDMkV0YQEI%2Bup%2FIuQU4yytpJkcS%2FppXpp9MbVtqlS6QC0x5e1rZHWMp2hYmm63MzGOCMfPhRAT8pZOun9uQVshuWwv9S5bM23iRfL1y1tczxTmyOOYYWW2%2BNXsxGRJWzOUP9DS%2Fa5qyJtujaqaDP%2BJ05%2Faw7vh9BlK818Q4oKYRi06X9BXeDxdG94nrjXIEJsGhQ1ZxUtNYjWyh%2BaZ2jIQa%2B%2BuvVvOE0rveobInkC%2B9N0bTIj5SivFzWZrJmxTG5HhLReFtaB3pPphvBY%2FsgUhP1kzGJL9Rvgf7jPqeX0x6fyIz8oDH%2FsityiUkWmqhKGMGADTTESEXwKsMQt3f2kYO0Bx80ddGyIdqvy%2FNJRLBjJaTaxpNAyNEwFOTPn4CTFs53lwrszNoM1K9l8pzrqIArkCkL3LSsm%2BqmOJca72y7kvPYecv6pPl4cqKIllTxyMeH0R8lOg7ws2dd9c1NZCKppYiZlP1Iymp1zs595Pqs22VML7h77wGOqUBY8nPFcl6M6IO4L45Cxx80s%2BlT2yf28uWZ5Nh8hrXUyC4iWwjtFGVePqNh4l3TlwsfDQ0icmVf84dPLchK7VyELkQfkBtRpJfvxfz4Mcjy0IAQ4%2FVyqOk%2B98s76nSPI6wqKgvjHV4xD1UnMRE0HscNa9QAS4wqE6KI7zn%2FpxF%2FFRorKLd9p6qOeNd4ujb9sJQFs79bgTUm8gCx1RKFnxHluoOGYM%2F&X-Amz-Signature=bea75554a83e8e68f6914504dbd25b07ed9d111faef6ba7d0b24a55618182795&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUUE4C2Y%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICXZTz2vJSlPu7mfq6ETIEkuMkbSQFz0Pnj6nQ06rmPUAiBb1qqFhnmChDNurQ8FREZSYWsclHvqZMMYhIljjVCy2iqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyQC4dG36K0ExEIapKtwDyX632RAmqp3f5Q2CjQvo9g5kEZQBpDZ9rFL%2F92tMLAC%2FOkF3gdGZm3qDsf6emTKqJIU5GvIm4g5ehh7bxbWzb7CFlnsSGYyLCSgFxID2G9Ahplx5Iu%2FT9QExEjag4X%2FVuDyfmNp4bWzlwbBA09gFs4jWqWvTdOUIvbN%2FmVBzd7aX5JjnVYpmb%2B7Z2unOS7EiFZb4HaxHN4jCnY5%2FRXQWqfqZeYzHHHoQlyT80wxNKUfkrJihhRcp2CsqAWcvtcp9UCH5AFMPHrOUxoelpit98EHy5revY9QiQzrsVlcI56%2By1cIUg7gQsAPGsbyIJY8ZuW%2Fov8h%2FnAmHuAVqVYl5HnuCcdBMvgdY3EEdEw74Y3u%2B8V6NK%2BYyAHITWpjPSLoHH4DTTUOv0XxfTNgNmIl3WVXI5kobaOtgRKQ%2BD86uv7luLlxXQuYTGVCeYbyA6FriURtOEaZCQEqXVru2n0ybD5Rqbz68wPxqJYJQP6cCjME65y6%2F%2FWD0KLWWoqnr8NrsGos6106IzKL8%2Fy73BqliLfsRcQEF%2FeZonNZAvB%2BTshF9aXDB%2BR6LRUGa6v2P6TZQqlW3xd1O304J9MYsjWUIciepvmoYtNFmmgvfJHzd3H1Mb3zSWcvzIn4FaS0wmeHvvAY6pgEthrzznW8p60hsxbZ9MfYBYHua6rVTksTFVtWkvJhh3mY9CZ46Fh4tGZ9pS2m%2FKlqeaEnZW3ZKZZmNpV9aFcv79iJsCwitVjvq2ab8llo760DRu5xvSa316XYUPHaemcSBuul%2Bs8I7m0oh5dcFfZ%2FmunM7lh6dZDtlS7cXPI9Bm9fz%2B7lnJ3NH7ogUccKHTUO66KbIicXJF4JRPDBzIeXLBJHhlXVo&X-Amz-Signature=affaf201c2876f7c826a12b51d73c507b5853b0c9ce5d940190ff94f26768f5e&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULD3G5F7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC9arLAQH5%2B1JyR2yMqpdxsfYccTOjxsrxhnOgxsPtVYAiAY06vUbKQRWtnMkiGtxO%2BMuHD7msqe6DMeVMeLJSsctyqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTpoonAYtCgcRJySSKtwDIlJxE7Zq5uoy%2B84TxPHLseL8ACA0yQnJWkBWMOVhqQhJMMddgmeskEk2ZeB4jd%2Bemm6CRumIZ%2F0ce9GN4%2BHD%2BONKNMBk%2BnQdBW32wuGZ0Owzmh%2FyAHUpL4h5E%2FuYQuW7wyGcbAiMkls2w5pUdDjOroxM6Bda2ECPWMvv0HTQjHcrdnxzX8VAqCbslFbjiKdVq1IOkXMIJAOV43xGqjy8jXwl75s%2FNTXTtc%2Bwq%2FX478BxWpBC%2FNwAbt033koWtwahUDiqVHQxCk9DQmruolxcCjlpU36nVqqRTzB%2BmeOa%2Fegyc9Vpftie%2F9lVTf9CsrLHhZ7tpTT1jhQkweLLzKG6eOvgc%2F61DCIuut63Eu1j9ApHS7YSP5Gem%2BiCXing%2BVPD9FxfXY8C4gob%2BAxvDE99t78e8pb9L3Bb75nokWXcYX1X9oYsmXPBSZaBTFLzdxcJp2Cak7EOBq5Qv9ktjL7ardbv9QtOSttJj8qT4%2B9nE%2FZoUokofqmIhFkp%2FYxwjsY0OFm%2BgQ0Oz0PRC1nntSJiif3kMtUbAiHp%2Bf8UkgMgvGFvVmwT%2FWZWGnlllIYchx%2FrMC7GDp%2BiZqMiII0iqD02YZKATBXVJFtH5dWCfXcbnnv%2BVpl0F9Dkm7dbLxQw3%2BDvvAY6pgFciCwSXEvd%2BTkHRhSOHYohXTAzGzC%2FT%2FEVkNvT7khz25jnCFiOBIqfkg4l5Qkb3OdnhPr747%2F8%2BrlcGqDWzJd458p4Cshndot610LN7%2B1G0hcRtUH0fH0rrtCJ%2B1v2Ufx823oNxT2r6KUP%2FLyJGppVLDmqMKo1vQ5%2B29XhCwNN1EGNL%2BAC1ixho%2FRZb1js6QzD2iJRixrHabIgnehbY4Fn5N42NrIC&X-Amz-Signature=d4d186c59bf66a83ea1019612600757805f2481e91a7dc1f1dee9ff61568b83f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SUY7GMQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BQ2cNCwz90zXPXuVXCdMgIAtvoOjgwHmmX7NShfFvhQIhAMoV7a%2B93LYve8%2FdYVKqrP0HRB9dvmfdkAusfjiiVwrgKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyeYdTWIUmwt6yoqHUq3APKeIiSSJP1XbDz1ZTDQf%2B0reD0hL3SkG2LC8zcLHAiF0UI%2F9fRC8TulDkLXrg3EOglHtbHM1bGJdLXLI2WZja1xJFfxiTctU%2Fa6keQIy6GitlU%2BH5JQBRtRQAE1GAtCXpZcUqgyEF3waNY2VOkqEkxpQjVREudJrX%2FBPaI9a9Gm2BRnVUQ1wl87rgxvYJswN%2FjpRmfekCu4KJq03wQnYyPBwencLWVOP4QsJl9WUqO%2FPwg%2BBpy4C9Fx9EH19HaY60txqRM5l4iKy0evR4NAa7ujvpJiYeA3hqRFHdKkBdkMTl8vfdmdEUm%2BZSV1PJt21YmYlFeZewHTiTFAVlJE7Fw%2Be7chH163dgbVdZcJq373rn4xuRGV1TVDHAY%2FlTBvIJHZ58QAKolYntds9AWQfNIhCmkrscVhJcIA1N8m6SuC%2BhbcUeHKUih10YoZc1sSKQEJCCg7GFtzDDNsGeFQQWdTOkfCVOAU6FjtzIaq1h9RMzc2wK8DP821mN5NvV3OCzzgUQ8Ko0gCrgibvTEFt7xXHrunEalo9hQWEn3yv1W8lKQ27nOeNonfMwxQoaNQf3kJMD16Qid%2BiDtOJqEzHK1Lhd99o2ytgFVQHXtWQDLWrIliZd6XDmZniHnsjDn4O%2B8BjqkAdZhjpo7HuyIa0Hw6jlipMdGUWS6Q6QHaVDa7rQpzT9R0u43stl7lK7APulxgNYB83GHZjE4uE7hif8tsRQNiD9QG6zEoNjOeM%2BvX47Zs%2FvU50sOZhRn9Z1%2F%2FQ3z8h7M9QQq2HHpOwPfQYIw0j18OAxaHICIcsBOCmBWeyTNjUd6t53opW%2BzUBAIOBACUMeZ5QEJQPbsfQpiBgopyVF2wMAh%2FDPE&X-Amz-Signature=4ffc0919904a340a79fd2fe3d869a303407f408ec76493e6a4acd431a84c22ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QHMQAZM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfMnGOMMz35pN6AT4uiIWQ8G5EsfnS25QFEnpDXAAF5AIhAJ7sIMTjU%2FHAwCQUwuHFSZyk9aHTAWDWuVuGl6e2YMQZKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqpjlEUCz9YQjxqnYq3AP1Yx8g0yX9OqpprsTM1nZo2V%2BJwlqjyEPfegQItNyUcUUJMy9CsK3KmlVGfP6jf6qTdlBElg5adAljOg6WDrLgw4N6KgP7F55APMAJ6NWzMkOJ6LHLzb2xcpGh81utEho%2BABUTS5dtnUeIUtaFjCmwgt1a%2B8k3UJxLIKKhTfuTqFujTmS5WBdftSHXr0oVJNA6SHHqTZtzuSs3mzTgGB2yg81hgvHimWrZ0%2Bj6MrU24Ks2CBanD7W9yrSsIDv7nf3bxkoRBGWZ9SsoMuP3P6L38ID1vV7aEPhWO7jceD4vDPqkTUYGIC1blxfeY3itOpGcvwhp0KdQm%2BJqLocOXJbLm4F2lUxfKDr1n%2FL7smVb8RHNfW6wFAMmsrrBaD7N9sj8bhOAhz4GJtcnggzfGeXeuChn2YNiwVKyP%2B%2F59FasVyzX6BQl4bpMAhAnsQr774hbKlf%2FDXa7Ei7zy9E5AdepsvgIfg%2BSrn78aEF49S0TWXcXN3LcSzGk5EsuAk8GJMLZLUR6HvX7DJLCmDfzam95PkdwTqbqS0IbKvSMCDgoodLMfHvmCUC95%2FTlhb4r1zg01RAxyc5DIbADHc0laIA7R%2BfTIQmdShwimu5is%2Flf1wdNKIqTMdFCwuefTDC14e%2B8BjqkATFQDUDwmhYvDwqUihAkSarUoGZgNLqupqAXbVVWiw2RNaTnT0Xu6aAT8AkSzIp9MP5RkyPj5ZnuYkl2PxFgvPQUob9Kt2ahpO02k2M5P12CAfoX5D7hLfALtX4ffVm3Av%2Bd8jHZ5bcsUBR7QChX9wKYOAld3cojw%2BecZ1yDrqfhNP8D%2FOk0IVzfEmZ%2BEGmatyvn0cCQnFFwWIE5yrVn0KPAvyw8&X-Amz-Signature=aee2168017d29949f2ea4665c4c82143f6dd7a2a6bdb48c075e12a604f31ec9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QHMQAZM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfMnGOMMz35pN6AT4uiIWQ8G5EsfnS25QFEnpDXAAF5AIhAJ7sIMTjU%2FHAwCQUwuHFSZyk9aHTAWDWuVuGl6e2YMQZKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqpjlEUCz9YQjxqnYq3AP1Yx8g0yX9OqpprsTM1nZo2V%2BJwlqjyEPfegQItNyUcUUJMy9CsK3KmlVGfP6jf6qTdlBElg5adAljOg6WDrLgw4N6KgP7F55APMAJ6NWzMkOJ6LHLzb2xcpGh81utEho%2BABUTS5dtnUeIUtaFjCmwgt1a%2B8k3UJxLIKKhTfuTqFujTmS5WBdftSHXr0oVJNA6SHHqTZtzuSs3mzTgGB2yg81hgvHimWrZ0%2Bj6MrU24Ks2CBanD7W9yrSsIDv7nf3bxkoRBGWZ9SsoMuP3P6L38ID1vV7aEPhWO7jceD4vDPqkTUYGIC1blxfeY3itOpGcvwhp0KdQm%2BJqLocOXJbLm4F2lUxfKDr1n%2FL7smVb8RHNfW6wFAMmsrrBaD7N9sj8bhOAhz4GJtcnggzfGeXeuChn2YNiwVKyP%2B%2F59FasVyzX6BQl4bpMAhAnsQr774hbKlf%2FDXa7Ei7zy9E5AdepsvgIfg%2BSrn78aEF49S0TWXcXN3LcSzGk5EsuAk8GJMLZLUR6HvX7DJLCmDfzam95PkdwTqbqS0IbKvSMCDgoodLMfHvmCUC95%2FTlhb4r1zg01RAxyc5DIbADHc0laIA7R%2BfTIQmdShwimu5is%2Flf1wdNKIqTMdFCwuefTDC14e%2B8BjqkATFQDUDwmhYvDwqUihAkSarUoGZgNLqupqAXbVVWiw2RNaTnT0Xu6aAT8AkSzIp9MP5RkyPj5ZnuYkl2PxFgvPQUob9Kt2ahpO02k2M5P12CAfoX5D7hLfALtX4ffVm3Av%2Bd8jHZ5bcsUBR7QChX9wKYOAld3cojw%2BecZ1yDrqfhNP8D%2FOk0IVzfEmZ%2BEGmatyvn0cCQnFFwWIE5yrVn0KPAvyw8&X-Amz-Signature=6bd2785968e977610208e87b92ddb752317fe0b03fc9c2e94d3b938a3f778605&X-Amz-SignedHeaders=host&x-id=GetObject)
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