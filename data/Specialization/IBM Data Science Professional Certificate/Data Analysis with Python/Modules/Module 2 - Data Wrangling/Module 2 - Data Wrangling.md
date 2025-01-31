

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXBCZXHX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcHJoOY%2Fx1%2FUCHS4RdyEuxdiESdrK%2FcAIx1%2BMQ%2B9ewpAIhAPAoZaUro85WaQ1PhCKiiDi9tO5PDP8K4tUKI3ZQm40IKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyw8UDA7Hi79ZfWa4sq3AM7Di2z%2FHAe1eufJIcmdZTYCj7bSmJlSnSjkUxPa2mJIZhEZ2eTQz9%2FeGVM7X7AhQw37X5C5W3tsXuRI3QDtq%2BWPkVB%2FEhxvzdn8QogAhxncwFfp0J8b2thZxoHovuO1GXWjEDGFnQLfId4VkHnrupv7qZtu%2BB%2FM5hdhfki%2Bf%2BD38qealTMA%2B3bT91VRUE%2FCm9HZE6uc5tUig9Yek%2FNLhJDkiCqCOhnG%2FkCyqWQvqCeT9zZS%2FTJV5icIZU%2FA9YHZmlDqEgzPGAmzoDSUk7fDLaoDY9ZhPWuZwRiinKsRNCCQh%2FY8TsvvYPlLOOh44DD6WFfLQ6vIPiv4IHxoJv3bIWhLsLolS56H%2FbWlWq2nTp9HyD67K%2F7ZnYpFa5V2yruytuTvaK0y%2FmlLQpkzLIWiUMzM%2FYeNnJFz7IIArG%2FRE0H%2BSqHCtCue8WJbYaHTphTgRE0YZE2%2BcHMq3Om1uiEYHPaAV2zggjUuPG5AD5258OGyaacDFdmB1HeHMEizNXiTZZsPjGaXJvnAywcMGDoIffjOyxNy3b2HE9aUVGjbZg53TOETCFv1hdMIVxb2o6jUr%2FAUVLNHSt6rvDeb67lkbnasT6XTkepAgxlKRKd8UsOcezpP5TjZTvzQnq9OjDqmvK8BjqkAey8RrvAo9Xb314Cdp3drlpvn18M9D32Xcua%2BzQU1B4%2Fjpm5mX35d11ZgZuhnBlHlb1rdITpzkSbdSKfUc45p5HbWM1J24nJPF3gujaKS8HvLH0jL426UPRxeQd9vGbS94liG5W8xbQANmtEAkpfyCmXUBlVNywDY85g1OoNujdovLbo50nwtTgKfmZveh7sc0mDDIgqUiW1EOy8D8He7QobYCID&X-Amz-Signature=6a0aa8be8934d5134603465120a0b4e9cfee020df5eb722012fffe13e84af621&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OY4OSNN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqMq99JBbmdRW6o192K4nFhUZacuiubIH8pzvMBwDr5wIgR7FugL%2F1uwj6HKnJCq5csEB7bUI9f530QrD5sjVJ838qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaUG5m3FsZwTKBxzircA4QCWGPvy8PA9PBPBrH4c28mi9S86bZWYha20b12FP0pnJG6ecSKGW8BCCp2AtbWcfmiqFtM9npPxCiYNSjBUPhYIqkxFT5bXMfbgrQL9nZdhIRSl95BBEOVHWacWkK0eFS5fVCQqEfN718vAukYUg%2BG3F%2FF13ZuS%2Bg13AU3e04yoyGmict78J%2F3%2BsOH%2FIPtOxE%2BPnQrvdDqpK%2BfTxjfQAfXlvbY1nD8Zn3RV410WwZPIuAnvMVzZLmoipWHzYZDy1rh0Z7gdBwrf55ApD6C2dfZBoSA%2BOcYpY%2Box3tOxm1%2FxmSkk0WQUROIbvP21ikM7JEM1QjC0tkywVQObCVraplPkdYv%2FwBnq40S78UCBMwZw5UlC4f6WHf0hqGRTGEEmIxKsrDjsQG15VybKmDVa%2BadQRv9Jkg%2Bk4DWBuxLhqz4kYiq6QLbDTG4y2eKZYbABLXnJKYrn7ulLgyXPMw41AlftemXeAAbtvqXKL4j%2F0yY8KFOITK5gO4kpjaVticG4MXgER659sL5LZwFKJyLfoyMl9ZVg9%2FHeY5aYXnOqU%2FwHCHIt4c95cmD3LlGr9a1KwtwJgIhC4IE4Ugo99t46HjCQHYbIJkB7Qvwu97TPwrycQeeVYlIKVQex1PfMKGa8rwGOqUBI%2FUduI2gYVsbDK6b86fmzkfsalmd8YyphORdAoVa%2BkkR5T7GQvhuf9bmtx6cXDcpt5xxmuo8a3x5uKmQTGDx6Ry5glFT3sfEuwaoG%2F%2B%2Fgjkg0shQiumRfDSYRuRXCqHFU4hHxUlYBrgvg5tqYPl0GDKdRY%2F%2BFSwGS6wtDl9r%2BMqu%2BW3N9Bhg%2Fg8KszdxEwBRk%2BxiFjCUalzUBd6IFLZPBmcOVewf&X-Amz-Signature=3fd9d44805fb19a4e2a6828ae0c05e7814fc7b8b594c305b0d8e82f8c31b73ac&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVCOBT6V%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzjVmaarfLNpMZfWeWSwLebfMje38GSFLIceJIIC%2BVYAiEAk9R7u5fIZNXjJ5YYZdwVxwMNRwiTtRg6%2FHJWR77NqkMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGEGTwly9V0IgE9ttircA0GiDddXsr51dNCTvxcjEjee6ys437v441KziYkrrQTqdgJ6aqx9D%2FMr9orj5YqQA3xJCAPA91F5Z4QVfXeNFTeX8QnCi9RVwqSHBe9dRNO9oOelDg%2BAIbnkm9I86wAxPz7rzRcWndLOsIYIxcym8DuS9zefnikGE6Nyq2bOK%2FkAyOZr76lEf1NjT5Z7yK2DV2ctizAaK12wLLsl9ysEbBjc436Sfs%2BNP%2FjhLuRH6hija%2BhGGmqF%2BQYGxqurGsGZsviwHTWksLCicYfIHlrgMyNhpumt89ezZ6AG8MWG7YU5n3Y%2F3Lr0WVFQTdJsMzsD2tnTuHY%2FtOmNUCAIjkTnB9jmB%2F4b6sf5KAKqaWzbKeDfknKQsx3arYwitA%2FttWL9lKsEzMme0iMB6TDu2VVhqjdGOSjQAIE%2FMjP9OfR3hguilnhYy0zSwyia5pSc0LwkxHvoCL3JJhf9NJAtu6%2FxUQsFTQ6sBXx4KjcQvfy74YB0YWdwXQ5nrbWa1CSiJo3pLWUa0IoOSjlpLnmco9b6Q9OQSjlBT848RhoMIgf2ZMoa%2B2x3pHQg8LRqUl6tKgLM6fUTAiP6qGHmPuJWpIIs%2FcBGdHHiQkUh7lua8XLPoPBDJwDWkcg%2B6lBI6f9VMOSa8rwGOqUB9JM2ShNjOjmHMYs%2BsEHthYwnyZEVDN%2BQfcdNvT6ZKQMimRQSObOgJTtG7gNr5tZsnlg6P5a5szaCJWqrVIJb8nerKK8RVhpgmAfl7UcoGciDubOPouF0IQ%2FnBLtqA109uwGULsjHbpVkjaobVNdFfJESqsmrfSvbjOJkwf9%2Bnq%2F9NbxiCyhO6OhV5aueLilV06NvCSBjgzT77Jq4PAc692ADZe9f&X-Amz-Signature=2672615cdf59de8e76a180159f71e1c6bc3ff9bec73a4c55269abafeb456a84d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AGILTGV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvwWM%2BoYcyPY9O8CEpeIWBswCwO7JHyBL0H8c0cIAF6QIgGGL3kSLri%2F5Im80DzxEyMEF5sRP6ef%2FBQnz%2B9m1p43cqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNx0%2FT%2BBlVNN%2Bf9EyrcA9uHqIgUhTByN2%2BQ8W2tr2KsadvZsk%2FcYagJP9mu1RyNi2mmxOV8DqqICGC0NoPFSMnycZug5u%2FGIC1iPdzR4%2F%2Fvr7J2F3rBYwiPwvwqci8Z7CmR1ReMnyRSo7esCxJfHzaduWwZPbAK0Oke6DmtNtfr1Q148f%2F%2FObaj1nh484iJAg%2FcdeF%2BPCGIahZOTNr4S%2FY0wLqGsdU6GpVjNDQXQZLxUq891KRnXQwLjo8TcRZwdsv7WepD4JmDtZ6ZI5Idy%2FYOi%2FDIqZ8c2iyMo%2BrWWgCTsYuy1v%2Fgy%2FAiw08em5V7pE%2BAKqHHhsQx4V7Uq3MA6lQ2G82i1yNPW7oHUzlFwUSEQmcqiiMWOMullQn8qjED4JuV7yrrxzkJQRnUVDnr%2BiJ3MnYKjsfOzOwhlNAjL9fgaQ8ZH4h%2BXmbs1JWvkG72QReEdCdj80koKf85SUpdFcyC6NpaOEhHh9B5PV6niLgpK2tlZlRFcKF5gsT2JxBLjQfG8cCEeHfmx70iGpFvUH1%2B5j2qxM%2BeCYPMu4JBXZVpvDl3HmtvB4CH2ud0G%2BByl%2Fs6NeAbDt4Swm5%2FEwyL7grVFfBR43TsZRO%2FcH5ASvrjjEKjnQ1eI2w2byB5cTajwrWrmoztliYy8LC0MMOa8rwGOqUBmROAAZ8FNs1Aw6UFRY1A7YZ9x7utX2pbj6pt41o5GtDJ0n%2B2z7npx%2FH8KWIZm6vCLb6R%2BhmsE%2Fls0DfGq8PjzymSajuEiR8%2BqEmfTyXNPxdHObfP18r0%2FYujBeL80oZQl1b%2B6l76qV1ZdmUI1Ajq32pAC4h7a8p4gbYYpbm8rk071zHH%2Fs1X6B%2B1Nd%2Bqu8KSEwzdiu98WXhzRYV9zWwCTCLwQ27H&X-Amz-Signature=b500e7511155f00ced8aff005dea7dee865caff0b022b0eedccca643bbb7b43b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWVUE7HS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFDv7pSamYNUaW9e67VXKRWenkgXpqd3yc67cG79CATiAiA80ussGBlI55PPe0xB53sFgeO%2F1RbVBffGzlTMYwtwEiqIBAi6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtEg3c6vA%2BcBer8YhKtwDQO%2FxTuVtjBzwaTogOm4xKs1PJ93TtyU0spyEBu3aOA3gKL%2BCJppurrxdJ%2FGXubLhJSUylSZvQ7cqAPjZy4XTtrWi5DdMwqlrh190FmjKp7deH2m%2FKQVWlREsYMK1GFwYmoAsbOm1VNoh0C4Ytz08v0iQsmi8DPxoW442L7j1OAmVvGii8iS%2FyCBbwwkqJIk8eQ3BOTqEAmTLHzncPmeFqfxhW1acvnrEfE%2Bs4WotUO3MMwsCCnecAF7lNwDeDHA8CMwpAQ4yNMNHNb%2FdQA1kbXQGPkLVxOAzl8S5vsaoMsm8oKVVDgtXd%2BdHejslY7thjbHEQXXnGNqvV0uzX9RJNxqhweTSovs1ayseMtVhN0x9MpkviAfgHhSNogttgg%2Bq6y1ZvSuanTqIrWdj%2FmzqrxnSlpe%2BtpWdpD5STdQiNiREtjmo8tubaeylQwA%2FvKLpYJSU9Nm1hoxizxPA05NcahECUUiukOcw9U6ds1DJWuVOLInuMUEXVNC6E3VQ49mJS0WRnvUqQdealApgQQweWISF1VR5GTbZkkZzA6Hwc5HsG9nx7kuPSK6Kx7shCchDY4rtSTo6vtRJvI3M0cSv7IUCf0ajHoxmw%2F1l5%2F00VN7AX4cwQ1EyBKIeiyAw55ryvAY6pgG8muysYVJDFhfxvM%2BMp7TM88DSQSWdTWo3%2B9bRSJyHfpJPmYgPtgiQPz1XBdwC4Jacp4cc8YSOCN6u1evJpOOtztNp5LQtu2R53OpOsQYvmiLjLmiYew4p4EPuLfWjKfnCfS7uUo1XCHn9INs7cPvI50IDP7TjAnlMMNYTFussEKERufSIYvyx6O6BeLBEkSWLkj9IGXumaCrvpxl%2BITV3kGyZXlme&X-Amz-Signature=a729ffc04ba688578650bc7e21ce7d81f50e7b2b972435f0c06e4f1df330f83b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKH3FLCN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHlT5TGrvs0hR2c4e6GfR4oWJMAUzBfiL38JMv3sFz7%2BAiArIh%2Byy9Yeb7jIl2jJ%2BzBgWOLpaTPfwywPBFoedj6%2FFyqIBAi6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0F6FzYiNZJ0VjCXTKtwDVGHNk3jK25t95yuXzMQJTDnfOBMV0Qv3K2f1ztQn%2F7eCEjat%2FWswAwf3WXXCs2olS%2BRvRVWu91Wu0U8vpsl5jhzLIY7JwTk3%2BOrfLLsip%2FZriNbgdD3R4fb92Fht6NaDZYcI%2BRjbb%2FS1cjTxR0y7ICjhuXH7Wo%2B2hWAz%2BlVl5DH0vVuLAnMUxk7B7b61t%2BeoJ0AFPoB2p34WaTjCsbnK92fs2G%2FgFOxr%2FgD11ucwC1pl9luStb6KzJsQ0%2Bcq2PVIpvHw2%2Ff0f6j6Rg0cgfw0Av5H8CdijtfD6vaxRpUl2df%2Bdwl9Im3snfYVGb0H62S%2BF1MajHZ1lVmJInascAc2ErffJUvKibQTiI8BEGh71txjfhrIAM3SzwuBEC3IphAt4GhCT1aRH8WZfHPWFJO32FNvsBiRfjXXuy5cmStPiej7bHhK3pp7AiyjpoeufPxpoQKfgj6RWVyB8dcHy%2BAyf6Tyv2M6JqsjAjQDKTLyfi0jQ1CZMnEbGLKQiNyto2q04xn56LBJYcZIw6oz3jAob9oylggwd%2Fm6v0pmz%2F1NLAh%2BiuwbN%2BXBWg94cmgy2rP1l5ishmvchQOA4koIjYnPHoHux6pI4ogU4tEaPlDwNCYbxbU4cvFzO6sjqC4wrpryvAY6pgHYMLzp8yq2347U7e1483iBsl8gDmEsSGrhGbtCQMjfVRmDn4ZvO%2Bo9qZf%2BlTJ0wbIdnm%2BRDplWLI7WKoMdvXh67vw%2BTS0CMTqNT5larzZkN3kvLSbJqmigN2wTq%2Fceo3aLU0pdNf6A3bZPJ0jCM4Yi9w9YKm4kgEjqxZzhOtRQ4XkCGiWj9501NVyGYnmZKS2BNShkJlw%2BdlH%2BMaUdjy%2Fk82sbQ6SZ&X-Amz-Signature=db22e1cdd5d5d0531cf9c0dd17627c2de3336e8ceb79350e944a07920045ffd1&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBCW5CU5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDQKMhYW%2FsUKBkdUyZgT3jG9eUUX%2BioeQvcY7lx3k%2F3pAiEApqDrgQPhBqqMNxnKmkcp%2BhX%2BlC%2FbXFowcy%2FSG8l7OvgqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJWvmCSf0MDVPBrOwyrcA6kvE9cZDChlqfkePfSxr4wIFQC4sYXaXGy1Yznmwax62TLAjfyj1bdK9NgN15aIKmDUdf3ei8MxOT55S693hSSbuVArgUCp%2FiHKJ6qq8p4GEnf3tIADXwOzd2Hz%2FBQiMQbHNb1DdYcfpYTfsBYgeLV02luE8XSnsgf05fEkf4wNTEYh9TtezRCM3FJKoVR8d30sDr87Fx9es4i2fiNX%2BML1g8oCLNigYiXp4osSV6NLZ9X4x7idgWGvh728Omb38ZH5wrakCLcykKCvwA03%2FNkwdVzKgmHzSA%2BaS6%2Ba7ccXmctHyGKmYvOUpqRBfvUyVgCRKvT1u37kDp5tY5B3WaNHcPbFPCFHXojRMkPSnHx8B23T%2B33XzM0%2FvEvnrR1%2F7voBOa4ZlTdyAEvwIcw1EJe%2F%2BPrjocBM%2BYlfq%2Bgm90zTJOVdKxI81VRdBi0Q%2F12r7s%2FO9NWeitNJs%2BSfOB8SXO548H3CfOVypmQmekNlDK%2BDqotx83dW6%2FwQMGi6fZtlnedf%2Fs%2B20OexSxd5A2ofy6JEVWEljGSCBM6ppSiGMd%2FXd4Ycmp8hyLo05MIG4EAFKSbMcySmu42XcKRpwGjDQG5TA4Rsf4cK%2FZv3F%2FQiPtGvE2zrCDVoZJLuQYKXMKKa8rwGOqUBilLlf2%2ByI8q2ER9mUPaLuy5mKB7oOGUwWJQ4AIHTBreg1hbg62oDAjWwBpDp%2BYrNxr2B%2BMpcFDbzumirs59H5DM95QrgZnGSOwkOrgWBgfQ5ImRUwGH6mnaCEwF8Sf9JH%2FztxYTxVt%2FYR8a7g6AQlWiu%2FIprYynRYn3CwvWfPmuHSlWu7tYLvFZ8LXGU8C59HKHv7P5AR28d6CSxNwbZDbr%2BmSpx&X-Amz-Signature=01953fd9dd7415ced1f9803cb978640e09cde0171e0a1503576b2ec448769175&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OJI3KOH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWHyHikYfcZW6x%2BrKll%2FrHbDXH%2Bt3S5XZxhJC6VJ%2BtDAIgYffAM7ArPkgNaE7YLxKB7TqWj4RAZ2JXKGfujm7OWB0qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOaehQMQ8XL%2FUM611yrcA2IuFXrQ7iTSWPOW0lMPlBHFthX4Eo0aMIK72xj4A6Qjsp3LSg0fKdAuhqloAJBKH4yklRQe4VI%2BvEch%2FML%2BnzGPKMVFj4ULvgBaG91Xd1YW4%2BnbYqA4DS3n7PZQHv0tKThVw3Ry2ZJeA3HdKTS88YhwBJ7cmWejSik5VfYEdPBMssLYSVDwiyOSUZt3QvooYDxOGbd0MP3%2Fsf4b4ULZFKEfZdHhQzpI3JpTdzKGrC71%2BKxPCK3aTkk1zzwK1pe1dU85tGTx%2Fxe92t1CHkaBwxOOcDK5wz0CUlBz8QSt4JIv3WFSvf9FAsZhcTf97GhRk9ortCx4U0jdv%2BzusIj5mGmyRvK50wm0bQf4as8gzMIOshWco3Ge3TV0fCYD%2FjufXELAThkq57rJHVt6DMM1Kseo6pd5TyKW5z3JvsMgUbeTzWd%2FRE%2F0QKB5jVyrnNRkGSH4xZMg%2F8XkiBdBRt%2Bv%2Bz2mF%2Fk2Cc29dbnpJFlU1FCpcLu4s93s01B0Qf1TYQW2TuWcdC4s0MiSI8zUr8%2Fkx7XO%2FoVg4fGa%2BclGY5VS6wdKRaxdiGDsuYyQa0vFr%2BfO%2FrIx%2Fex1gI9XQ%2Bgxzns9c5%2BRPIXS%2BSdBrxnWOqALsl4wOQw%2BVtuovnW75mXbMPWa8rwGOqUBM01G7zJ4g6TVeLEpCokslyiLmuKa%2BEKgmMElCZkWJdZfe8HXwxIpLZwzRFfE4Tj2tEjZ7%2FUcf845V%2Bq2CxURWA8PugtmDCxl%2BRJ5bDIlpak9%2FaQDBqCuHusC3%2FAXUdS%2BY5IC1xV%2F2YbMbZ30uFdFHkwNpUNTt95cMxw64%2BdcdKT1ksIgBoNz1KbxQrQCkmU5alX2iyytX2IGdlnHa%2F3oADIFxuAa&X-Amz-Signature=ec7c7ce30532014a4b384f6b1dadde9923939069afcd5544a5fad0da3209cd41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWVUE7HS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFDv7pSamYNUaW9e67VXKRWenkgXpqd3yc67cG79CATiAiA80ussGBlI55PPe0xB53sFgeO%2F1RbVBffGzlTMYwtwEiqIBAi6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtEg3c6vA%2BcBer8YhKtwDQO%2FxTuVtjBzwaTogOm4xKs1PJ93TtyU0spyEBu3aOA3gKL%2BCJppurrxdJ%2FGXubLhJSUylSZvQ7cqAPjZy4XTtrWi5DdMwqlrh190FmjKp7deH2m%2FKQVWlREsYMK1GFwYmoAsbOm1VNoh0C4Ytz08v0iQsmi8DPxoW442L7j1OAmVvGii8iS%2FyCBbwwkqJIk8eQ3BOTqEAmTLHzncPmeFqfxhW1acvnrEfE%2Bs4WotUO3MMwsCCnecAF7lNwDeDHA8CMwpAQ4yNMNHNb%2FdQA1kbXQGPkLVxOAzl8S5vsaoMsm8oKVVDgtXd%2BdHejslY7thjbHEQXXnGNqvV0uzX9RJNxqhweTSovs1ayseMtVhN0x9MpkviAfgHhSNogttgg%2Bq6y1ZvSuanTqIrWdj%2FmzqrxnSlpe%2BtpWdpD5STdQiNiREtjmo8tubaeylQwA%2FvKLpYJSU9Nm1hoxizxPA05NcahECUUiukOcw9U6ds1DJWuVOLInuMUEXVNC6E3VQ49mJS0WRnvUqQdealApgQQweWISF1VR5GTbZkkZzA6Hwc5HsG9nx7kuPSK6Kx7shCchDY4rtSTo6vtRJvI3M0cSv7IUCf0ajHoxmw%2F1l5%2F00VN7AX4cwQ1EyBKIeiyAw55ryvAY6pgG8muysYVJDFhfxvM%2BMp7TM88DSQSWdTWo3%2B9bRSJyHfpJPmYgPtgiQPz1XBdwC4Jacp4cc8YSOCN6u1evJpOOtztNp5LQtu2R53OpOsQYvmiLjLmiYew4p4EPuLfWjKfnCfS7uUo1XCHn9INs7cPvI50IDP7TjAnlMMNYTFussEKERufSIYvyx6O6BeLBEkSWLkj9IGXumaCrvpxl%2BITV3kGyZXlme&X-Amz-Signature=61f8ad3b9c80afc90e0f51a55b7cc39882db259ab9fc80872cf80f73c82a020d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHWKAEY2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFmvHv4m4zpmAe0V43gHVYutaDTHHPCT3oKEf8gmBuXjAiEA3pLscn2GmroVd3WPpvgV6XcWbNeb4NeIrGGWnbg210UqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEwwMZjyFiAs2ORbOSrcAyNzeLXsWf8z0OA%2Fnl5dKobZ%2BlBfgtnkEkMd6KuG3pqVWdUSeNp%2F0gyMACaFSbHD8pYpDBTL9MzhnXbBDlNLnhABxY%2Fd4nEyP%2BjM6gIFxboJIPuq2QDMiHl1kr9O0RGrBPCzUHAquVnaYnORJoYggt0%2BDrR1v7LAgGmJLm9jwE3a51W3U9rKVhzOg230nWom5gIe9LPiYDROTtshtZxt6cuHtM87IxWmjO%2FsSiqTYW0mm4XKk%2FHss%2FR9qxiJHVHV9DbQQB6%2Bo3FfKjjh3h9e5TGvWbY5u9MMlkkHlrryhnoKHcA%2B73%2BJCHidiNnEggpC3rq34dj5WvES9j4S%2Bhw1PRdzOcJHHDMzGPRqGgXZWXV%2FDL4uZ%2FirsqrGub%2BKVhZ2REKPJYSbLx7lznY1K1rsq%2FYIM7o%2BErLsfxRagyQRYDQMb05vCGYoOh%2BzK7UruYMDM1pdknJOTnnYLhIroH8t%2BQltZBh4E8rHCBtny3qqgx9Nc1OITNe6PQI5VAjiytBZZMn9XOOo7BVjkR%2FZqk%2BjtbFFGXY7waEs6Vuxgga21%2BtyMk%2F4ClIGNqaRawDs1wtGGONb7dlG8SfYijPMl9Nwv7NeC%2BWkNHi0MTQNiKkZ9qZlun76Zgamfhji%2FHHWMPOa8rwGOqUB6COjjKWFXv2iaHf6DMkVKOqpjTNsnZypExwlfYUBdRiFKWIRJMNETXezDxhjKtXsRnLJKQe4VA%2Bv%2BFFRb1FU8sOWrnEKrwoGAFHxd0lFRH%2F0tRICAc%2F8ol4aeuR0EF%2Fy3laeko3ZgZ4J%2Ftl82IduNVnFS%2FnG1HVCVEX%2FG0kwMweoXJtnaUPAJhfZTLGOk8nyAMuUQ47WoKkCKQru6jDKUqIWuvNJ&X-Amz-Signature=6aa9e69b1cea63b50600cabba3f9f12dd94007d5259ac8e8adce3e9d6a8d6152&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHWKAEY2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFmvHv4m4zpmAe0V43gHVYutaDTHHPCT3oKEf8gmBuXjAiEA3pLscn2GmroVd3WPpvgV6XcWbNeb4NeIrGGWnbg210UqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEwwMZjyFiAs2ORbOSrcAyNzeLXsWf8z0OA%2Fnl5dKobZ%2BlBfgtnkEkMd6KuG3pqVWdUSeNp%2F0gyMACaFSbHD8pYpDBTL9MzhnXbBDlNLnhABxY%2Fd4nEyP%2BjM6gIFxboJIPuq2QDMiHl1kr9O0RGrBPCzUHAquVnaYnORJoYggt0%2BDrR1v7LAgGmJLm9jwE3a51W3U9rKVhzOg230nWom5gIe9LPiYDROTtshtZxt6cuHtM87IxWmjO%2FsSiqTYW0mm4XKk%2FHss%2FR9qxiJHVHV9DbQQB6%2Bo3FfKjjh3h9e5TGvWbY5u9MMlkkHlrryhnoKHcA%2B73%2BJCHidiNnEggpC3rq34dj5WvES9j4S%2Bhw1PRdzOcJHHDMzGPRqGgXZWXV%2FDL4uZ%2FirsqrGub%2BKVhZ2REKPJYSbLx7lznY1K1rsq%2FYIM7o%2BErLsfxRagyQRYDQMb05vCGYoOh%2BzK7UruYMDM1pdknJOTnnYLhIroH8t%2BQltZBh4E8rHCBtny3qqgx9Nc1OITNe6PQI5VAjiytBZZMn9XOOo7BVjkR%2FZqk%2BjtbFFGXY7waEs6Vuxgga21%2BtyMk%2F4ClIGNqaRawDs1wtGGONb7dlG8SfYijPMl9Nwv7NeC%2BWkNHi0MTQNiKkZ9qZlun76Zgamfhji%2FHHWMPOa8rwGOqUB6COjjKWFXv2iaHf6DMkVKOqpjTNsnZypExwlfYUBdRiFKWIRJMNETXezDxhjKtXsRnLJKQe4VA%2Bv%2BFFRb1FU8sOWrnEKrwoGAFHxd0lFRH%2F0tRICAc%2F8ol4aeuR0EF%2Fy3laeko3ZgZ4J%2Ftl82IduNVnFS%2FnG1HVCVEX%2FG0kwMweoXJtnaUPAJhfZTLGOk8nyAMuUQ47WoKkCKQru6jDKUqIWuvNJ&X-Amz-Signature=578240b08ba22fb91c5faf4bbc4ba58d48fb679f91c028aea76243db57a297b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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