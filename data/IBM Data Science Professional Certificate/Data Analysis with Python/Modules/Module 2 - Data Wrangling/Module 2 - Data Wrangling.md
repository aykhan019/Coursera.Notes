

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFYTLPVS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCiqdqlt49bA9rDrOVNkocDFqif7JsqFKYUuoXg16gTjgIgdHWblXJ%2BIpUSY5APiBPi%2FDpvaQh51K2vzZqf51TwsDYq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDNNaqVPWowh8z8ALRCrcAzokLMOGtOE4zE4jCEODgUpw1CLJz%2BPCHUz4adKyPNdMQkmbiOEKQIVqt85rhevl%2FsmCUvZ6uMe2cpnNrANDm45ALWSjGyTLXAxubjgNkSjO8TRibV%2F6fhxN1IUBGrQ%2BO0r93LTJhsx0eTpHzBr%2Fy3n33yhxwl%2FlK33YZCEnD568OL2f9jjzhj4RJXN7Mg7Bl7%2B1u%2FMwkgLmmj%2BVxvgX%2Fmr5gntNUhHk6YyYdfNKxUkjsTSjuOjAuvdG4MK4OuB4oB9PN4dHmHD9ISIexS83YAddO%2BrokKdwltjk7m51f6mkcGMLwR85yT2NrFlUg4ZuiKe81v56Qw0Hgftv%2BYi5I4lyGC0qfcjkRa1W%2FZbLU0PwWVOiXjsoXkpbjCKrABoNWurICSQMg2N7iLKKOI%2BOLD22t33yr3ZGD1M4q9j1J28tBNRdmRlH03Orz2%2BHRIeHap6kczZZx%2FBGKAQjx3xwWnukqApZJvHJ8ouGcfHsV0OhRmvRS07wkr1UfAF7NOCi6S3kaiIS1jHVOVJKQwF2Aom1di8j4BVW34w%2FL9TRLYgIs2Lo3O%2FF4rWc1U8GOybzQMct62H44LKdHa1wYym65Dl3hjxOfV6GUdGHKDjGNKdGjwRHc8avKT4uv%2F2vMMiUhb0GOqUBXY4FybjZPZUzqGYC0NQ%2B8p%2Bs2wCsf3dO8CW3mPQDgBaQiR4EcVqnOzf%2B861piV6CrFvboekf%2BCP8%2FtHt3XodfEDivjEyC5Hrsdm8Q2yBtLcv2QAeJbTcxz9QUAm%2BKz%2F2r%2FDLC1EnN5Fj2Y2EhCkry82x%2F8gcQ4FiT2Fty%2B5ggLDKp9g3aPIRYQYgRjGW79YxzZE6tS%2FS8BhmhJ5BZ70jKEwT%2FT4a&X-Amz-Signature=8d0838d15fd6ca00ea0a582740c0cf6ff242ced31d2a4d2006182ae1d7b456da&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZDYZYZ7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCDuekEhQelckO%2B9K%2Bz%2FjhKbiZceDm42LGNnLOsorEi%2FwIgWG6JijaCF9UjaYdd9UA9yJ1EpErOyQ4mS3QZ8MkA6r0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDLq2bgxUuPmVx3MqryrcAzkbCUCfHWRkfw5oDqaiedt45Wc4g9EwYajoWhAdBPcC3SkfaaK%2BRZ7HQCbtcWGWivOrn10m0xlwX70sjTskPmBO%2BNRlqjHYwTDD%2F%2BOCHxC571Gg2G9umXDnXOh7PmLf2d5rFPM2K4GHiUlranRCrv35Ygfy41DClbsAXCDrPyb5uPGr%2Flc0Xq36ZVGQuXrPrN4%2F9UW%2Fj4I39llh43J7TqImgp1I4rE98sYMK890aD%2F2pO7fdsPi6JOYfnQ9z2Fa9VYCPj%2BZdF2GWo7BMdBcssx%2Bn2SSYrM2yIaC7aWayWhSAQ1nd4j6YfgaPqUnHKn3yP9UfxhxySsPiyQPZGkN10UmFlYWnczj587fQZWeZ6Dckfveiz2juDkWE0fDx8H5Yy3RTOHVH%2FQzCh6ea%2F4sD5oGmtXgn7Lm05qM%2FRt3LCVqpnbLm9%2FjVoVOek9bpB1nPDtFFaOpIdASflYMC5T8ZmkZHx1pEdQqlhPdQ%2FlgZJ8ZM0%2BxZzbe7SArJ0erP9Xhq9vQIoi2SE0DReTr2UT3SmWszbSLd93Rj04IV8dwp%2FruTShc49xXSrWr3AXGPsN3ewURS7zWz7S9xfFmoNT%2FAb%2FzvvelaTSlM4UH%2BLLLL9B3tCXhaHQZqtO7ZdrsMOGThb0GOqUBC38OjV7Bs3XpizfUk9MF58pf%2BHEADLarM13FkfS73f8flBfZTdD3w2puR%2BNc4zY0bpiDxnHYHlRRgjDg8AWHEPrwUfFgcS5FLJVkRlKefVzQ2tPkZDWp74p6h7S8l2b%2FnNYmyvxlSfmXPpkboZ%2BAk13Zu5rNY3gVBqW0YpKhEaQJ0bAtRNQ%2FxjOMjHKBBvmSW5g9n6Fpj869ZqQ6Iq5iAhpDAURN&X-Amz-Signature=4b62ced6d62e1ba8c93c767b4102a7c88660ea4e49c7efd99d33dedcad41fe8f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NY5Q3ZI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCPfWUE7BbHlYJFq5Myh%2BC5e1104C1EDoHdlQ58BmceKAIhALdvSu55gyzUmzuLWKCkZCME6qBp1UBytQj0oQ77RpnHKv8DCCAQABoMNjM3NDIzMTgzODA1IgzjUnTwvrRIWRav3IIq3AMShBAvR3xzUZ1WQ5glWIuRDsPiPPs6Gf1Cc%2BvYR1dU1fgJFxc6JP3KDgYPXXbEEuTUIw1R77N2eM7s%2Br76K%2FYYxHj0WGE00d8cueidqWJqcNwFlIFEtRLibrYntBHqn1Dx8owpxgjKzpeWDoC5fu%2FhKQSsOXBY%2FAsGE4B7%2FtD4s49HnrOtLrgtKOP2bXjv8XsJYAg81zGMzbLUQR5%2B6Dp9DM%2FRdQsW787bQuYX56OeoajkftqmGwdI3YxvaHYfHHlXNEA79%2FL6YoyT%2Bqo690LrVCDgo0vC2%2FXuSoqnjV5K597OyvlLLD8cs%2BxnwTpndxjm4vem%2BRqvLz%2BdUbtyO1Mcb3qmy8jYM5%2FLlo35gYtXQ%2BYT9%2FuO%2Bf%2BEMleStIlDZf0zkEFpxAJZySq7vqKGnsOdQEMPDhFNENmiEVsh0IQrdi%2FlQ2DK6TbRWPXBvApsDHhHMVAJc76HnUVxYKJpBty7tA8pGCpaX2lOJBU3f8kOBqW1Qh%2FASlnOHcba7h0NBiIvmJfzBGUNNidQlear%2FHRJrKfSP5ejDuwSHWPxJo7XYco0pwaI3wQlAwV3E1HctD%2F7m4NuYCeOTR0IcDwydS9ANSG%2FHt8ZEs2Zi0DwGsAAmwvrbJZj4QbanruMKTCBlIW9BjqkActND%2Fg2D2YM7X6Tn95bEgiptRd4FlpeHkrjEN5bUQbWic7yQNTsFcEYtBTYOUVT%2F1w1BvzoTRh%2BflfsJ41Tzhx%2FwsqpTHSVxCTA3KeWE7wlC51gukHGDycPV9h6lBaqJ%2BYWWORP0yDKQoVcLIblVcWv6044cJAfqpP9aLZfxQ6oCvgyMSf3utD1mZuUi5urd38uukOghULwh%2BkxPuyEdhbNY4tf&X-Amz-Signature=25bd6caf51caf73bbfe57a56f0011907a90f5123b701c94f203f2bedce2929d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNHKLZKH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCID%2FUTYGlJuuX0yf99Qa4Wym%2BtobqcbMm6qOTwz112dCwAiBgeoz1QsUnaBKbOK4GE%2FcJuGEjjIj7W4OoIl4dpuFg1ir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMBGuvzwRsNCKnDoK6KtwDND8Ylm53vlc1BDSVzvTV4C8%2BCC%2FGf%2B3bwEw0LFRJ3H3MOV6wZqUJWRQwBasn5ht7wmSvUaynL1yesKBeXbJhEQqu8xXA8m24SUoYzuY2DFEgBgt%2FpNiBgoPlipIR0PRbmv3AkMgdgTwbR4WhyeeV5kKyvm64TosLKa4j%2Bq0I2%2F0MwsNHrFdJthx%2BD2hHRFMr0ooHjUK33V4CWDYGagmv26N0%2FCMW7MbQcdVgJltycSlsyK7isQ4A0%2FhcPMMin6bBSkKgI7bi96g3JDV9t%2FOCrekKrlrjm4r6sulzkv%2BjG%2BySZlZKoMovJ8DypDUu8Q%2BNY%2FujeYmM9GCXAEK53FIOPLo2KvL6rPwvI6jdj9P4sIkjgZcH9GC21YUIaBp6B2CspnjDu%2FlCqE%2BfHiTrbx41ry3qyPsu%2FgI0aGaGJPRhNSE3gCFjZuEYvDCa5pfMEHdVrUuWU407DvhDc7vOyN7Owg%2F0Z73ANwbXAGyD864%2BO5o%2BBcDTs3esISMm4%2BuOxbeNrypgEjHULagAqD40kJKJuTYTu1y%2Bf7WQMpib7wS9k2EzJWX4eh%2BBsrtjkRDC5rgEuogb1UT9%2B6R5bylRebM%2B0s8caLcbx5RGldWzIBzcKp2K7qXApqgGBEfkPZMw95OFvQY6pgG9io9AJzLI4Ob89Ob0TkIsP2aLEWayi0u8N6L0AEhlYVlotUmGO2cYAt0GidBjdqY%2BDISlH1X%2Fqhh8Jn9CF4KWGSkdBgvFhVQ7iKDoh%2BkNl3d4viotX3XICS6D1iC8WdKuSyKYB7RNnUUSHjVT8bCIRZsHSyYTBp9rsxARtLhybi2d2ydbQYuQABcKhx8x%2B28ma1hMz2KyUkMm3WESG5hkD1zTLfI1&X-Amz-Signature=2cbf8b53ea5591ec445e42168be387eff3fdc8319a80861af6e46b91bffb3239&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WM5Z5SSZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCxdIvCwIDcsNb5pRdVPdPCHtUygWFVjbvsGNS6diDoFgIhAOHC1m3RLU4JMhTVWyCWq%2FVGstEt2CkQBawWIEgTWIxfKv8DCCAQABoMNjM3NDIzMTgzODA1IgzlhF3dcfojSxurvuQq3AMroDAzJoGi2oiPff%2Fe%2BMJH6lEdfBKVURzDItvkxQnn1NeDTcm8iNSpzW6DHmhBuyFyuMH1g7JuEylAiGt9PoJxUCkHfWf6vuevcrmABSeeslwuFXCwMa%2BrN0ldXa%2BN%2FO8iTygGuTta9lwnF1SX5IjLLLlPsc1zBG1PMpz9IrClR37k9lrCKplkJadKjSFdXEygNrWlZP5byze9iFmp2lGDvUOADfSOZPri6pP0sx1JNYKhBZKmXH1OaagNpQDQHlmJdv75Il%2F2dlHwDefnLtS1gGrQs0EdXcjIF%2FrBf%2B57UVPKIRVtmiotV08j%2B0HvtL7tIIgqYprBxt6o27iPS%2Be5PmT%2BO8OArd5BM3u%2BC0rS5a44zlYMcM6gsVVIaPXlxf7vhjftrXvb2rhplEeIFOlodeSa9HHUPAoQ33HCpyI9CXOTMm8kWXR5FdtA5c91aVmvt9AvaMDviu%2BJPCd8Nkoq8yz8CjJubM7mN7TWMbzBiEXWcPJu0ko0poSm9w6TinUkQWBBtriUaD%2FYuMjid6%2BEE5I6z3R7ciOV9VZS0dc1TfcULM2LFmfHpKJ4EQULlldF9OqGqVXL1%2BP34g8Es3yvaHvnPiUeo3us8dXPRYaY3CW73f0mW1yshZ%2F5ezCGlIW9BjqkAWldF1N18o54bRuwvmAddx7erBgobpRrJgHIcOjSdQglqR0q845C0gxXmd2yaf0G2afVp70CB3IUHCA0WRJ1n%2F3dcDPcVj%2BR9jFDbvkHTu7frJeOBsAGpCL%2F%2B%2B1LWs%2FZlE%2Fx8CkeeQN3XfROGZcpjM0XWrMD72lOQvVzTCh4omuw4EBQSsSJJ7Fnaa9IoYH9%2FSiYkUihWQuT29P%2FO8G20P5AVIgG&X-Amz-Signature=7b2727b8ef8b1b452746cfa40cc2dfe717856cdad45fafe83687e383192b6811&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLA35BJL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDKjtvaDazaDnX4PGFRUYzZ9HvsqltRvmcjUqRbkoO1SwIgE4KIgKJE5X2y1gq8%2F8RnvkXGSCGxAlrhF66WTaNEG%2F0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDFJEE%2BEJvhy26%2F1zeCrcAxKyqeiinhAse6wa7tVmrpFw9zI736uJeXQHFE4%2BYwRa8Q%2FeHre0e5BhRJocvrKkMzUcZE18fG%2BO%2FA3uM9ZX6UuGLCKS8MdB1BcnVCHwFvwgdZIP0k%2BSGB44ucC0To9Qx%2Br85QVVbPH7B1zBKmbM2aCmbsNNmAXS7dRh2AlRZMLEh%2Bx2v%2Fm%2FoD5zooMCFrJxcap4JOmKirkw5eINJ%2BGEoYbNXYIC%2FzoYZVVp0TTvRnMmMPIpe305DbFYeGhcuYKM05Swh4%2B2rqNmlw%2BEi7tz6X1ccWupuv4ql23dLl0vHRR%2F13ICxENspiTqH5opRn4Xg8daKPkkYVr%2BK9aNMXKTEdE5jcd4ehB6lpZpsu1ohqLkKKAxNs55zWtRWiPr1EWsv8symBkwoJRlmEbBvY0r8Acri9HztgNE%2BFbnGu1VIfcz209L83KXnew25dZj8shqAjJaZ7SP6nwGay3QK1Rl5lS9ME617gxrN6J%2Fu6d5KttqUls4wo18p8EIWJSaWqUODzU0lkjFXy5DGYU9R0kgc40jy9B8NLwHJeHqmgjbfBCyLqLsJ%2BIaecaH4xJZrp6KvtIEgvhxYXUAPbWgSsU6l5cInuc7%2BhIXQcjBLqhrAZkto92V2oXdohf1tko7MIqUhb0GOqUBp3e6KhLgdmk7foCxKsoUkpiXtbmw8xRZZ7zhO5mY5LEsaZsqvt7o7mBcVPH85o%2FB5nOth%2FUCMi8ANsIjSOA%2FHfJUV5I6gjbpC%2B3CyzK39Ao8ZsXPkqc7jINW1nEKu67fxxLRF%2BvGCO2%2BD%2FDX3WboWz1qSoaFl6uqBZqrsm%2FGTW7TTxKWUA6Savx1%2F2muvT7sZ54JrN6JzKIgeURhOueqyNwJwcaM&X-Amz-Signature=4613c1f45df936adeef551b077c57d8c1d46aca4dfa4089a186f31c2d32d2595&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4XVST7S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDWReR%2F7dPAJWlLiZeOvM3d8c99iveiRQUEy4fJw30ftQIgQ9NfCUwG8mSuLdwZC8oWZ0zVt2umhGN7pluT4Qe5DI8q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJSF1efiJKyTRseWFircAywvrDpl25yybfxjc%2BGeiuyvVXIunLfRKcb4%2Fca6WuhxCBnZOIawx61Sscz1Vsok3RLubs4AunTwQy6REuQubOylNwCV8q3z%2BMlqo3K3u2LhEdbg7FXXZ1CW1D6ijnbYy99hm%2FfvzqjcFupYoKlkVEmULKKiCancEr1QGOXU8125iW9JlILPp50YM1ClUgiZp1lU%2FPZ2ULeRUC%2BfrWaxwAbZ0YqOLUOrz2M6frxW%2FgtU5Kfsm2cbO9hdcLGk3nPmzmNq7G46EI4HU8M62Z7%2BmXiFlj%2BlPColv2MPReeFvnw5zqFW8cIegh%2FIG4hKfRNQtaJC0rZALhAYhgeqgZvneELy853%2BjaJ6YVn%2FELsumK1WkC96bVy2sMxixN4pIB%2BcdwBHu0usZiGqzfoTlW6u09efTmYmD%2FiMiWW24MKHa9XzbQaG5U9mGXXFTe%2F9SVEiMZ16BaKXlYE1VMFxTXKecoQ6dIoZp2IOOoEDpM4xKaoGYsGyqe4%2FAjpEDuwI99Shzdk7wXhFWyinIuRLRqDzU0J8FB7Vooj%2BkJf%2BaKP8WoEwBosSmgSJpdhan8ouRBEtLh3jL3ZV%2FgQfOfrqGcUg3UldbiwTr9kP%2BhQO7lV9x4jpq%2FJoZF9gzGH278tvMPeThb0GOqUBXXdtg11sQfXLaTyRzsTAl0o10DmINLxCLI6n%2BdDte2JT5NAsig1RxQc50Z2Ev7EywA3cZTap4VepuP4%2BsdY5mB1EcFQM1xUgXOIQGwE0CXCdaSFlZfKOEYKeHwFHINAcanx49IZKdJrPZBTjZLpAGTAgnyxQYAoaXYG2nPItUeuxy0XprbXNm7JL6n5wUFUK0NWwCepY8OMXuAHfHmAyrZOxm2Hu&X-Amz-Signature=c77f43e8f474797671ee5c2fdf3ac6277887f5a91a9b071d9db90b9fbe5bcd69&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3HBL42N%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIBxVGKYvWaPVW78Jkp7GcbF3dV2ABDyFFCNOLBMg4wjOAiA%2FDugI%2BT4VsAPJ%2F1kgffaoqekkffxMHx2HGS5TqQH5DCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMQHij7x6EeGh%2FKRH8KtwD9DNFJ1fSgbFEmkfXnlBaIprsTIYOHy%2BHH42HECRmeTaZ%2FFuG0u1ix5hwsWYK9F802cQjqTWP%2BERWhHUJhjrsifxR5MfrSWyJN4YO5QVdEp%2FEB75dofYfk0Bl8EoTbz33%2BCo0XroteONJkFGMLHLeLjfV%2B9TxN9DIHrFqJ5i%2B1jiWOR%2BikRzgEf03ecPzArkz1M0PJov%2BO6mIMvuOcqatJ48PKGJJW6obw9mal6jSs9KPZOQ%2FnGzaZGOKRlGfTjWtYb8RdC0Jy9sjR%2BVftTqlOVNQtA3FGEVPH35IYLj2jNdHMpU7eY%2Bw5WMPkWTq7SqF8zcS8L2RH4hCSGs%2BuwalqKBWV9p6KTSHWIm52a5jvn0I8w5VFOU28QNJgHMVXfGymo8R1wxg91w%2FLnr28j8L6OY5TZvpzUp2QbH2MbmUk3%2Bq4F8QaHiNDMatGJdJydDeIOFQB2%2Fn%2FMlo0e5DLlaODXbAWgnlIJOTgq64bqDb9KVXtUlFfd%2FkWFmLy9CdTKaDySvM8uREUGGDUDgApLi3hAuBxpqK6%2BkVXY1bDK%2FKQ%2BeZC%2BdRjBINI6Xi8WWcqfsxUvNfOgF8GXM%2FJQhlFnTtZdbDgTkyHvAi%2FgQL3dAw%2FxOY2i%2FAagzcgmnnvTww4ZOFvQY6pgGXOYcdI%2FzmEEyFpEwxgypHMsnBHxQxKEj%2FA0PbP87l80g5rx3HNa%2BsdPatuiCy%2FUtdk%2FZlPx3O8JCwjyqt186PGLGop4DZjJegLCYFq3acIaA2hXbvbvanYk9FrLDN%2Fjg4aTczc8l3HsR5k1sc0Zald5aDnCtEM%2F3ZKGoAPIGG8rFjbYjlHVF6EzY66wfI1PdwcRNeAXE0h8MXBRET9rVqe27aEjCS&X-Amz-Signature=1b9a10607c141f6ba03ba354902b8a532e04b055748cf76718f6a87258800a1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WM5Z5SSZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCxdIvCwIDcsNb5pRdVPdPCHtUygWFVjbvsGNS6diDoFgIhAOHC1m3RLU4JMhTVWyCWq%2FVGstEt2CkQBawWIEgTWIxfKv8DCCAQABoMNjM3NDIzMTgzODA1IgzlhF3dcfojSxurvuQq3AMroDAzJoGi2oiPff%2Fe%2BMJH6lEdfBKVURzDItvkxQnn1NeDTcm8iNSpzW6DHmhBuyFyuMH1g7JuEylAiGt9PoJxUCkHfWf6vuevcrmABSeeslwuFXCwMa%2BrN0ldXa%2BN%2FO8iTygGuTta9lwnF1SX5IjLLLlPsc1zBG1PMpz9IrClR37k9lrCKplkJadKjSFdXEygNrWlZP5byze9iFmp2lGDvUOADfSOZPri6pP0sx1JNYKhBZKmXH1OaagNpQDQHlmJdv75Il%2F2dlHwDefnLtS1gGrQs0EdXcjIF%2FrBf%2B57UVPKIRVtmiotV08j%2B0HvtL7tIIgqYprBxt6o27iPS%2Be5PmT%2BO8OArd5BM3u%2BC0rS5a44zlYMcM6gsVVIaPXlxf7vhjftrXvb2rhplEeIFOlodeSa9HHUPAoQ33HCpyI9CXOTMm8kWXR5FdtA5c91aVmvt9AvaMDviu%2BJPCd8Nkoq8yz8CjJubM7mN7TWMbzBiEXWcPJu0ko0poSm9w6TinUkQWBBtriUaD%2FYuMjid6%2BEE5I6z3R7ciOV9VZS0dc1TfcULM2LFmfHpKJ4EQULlldF9OqGqVXL1%2BP34g8Es3yvaHvnPiUeo3us8dXPRYaY3CW73f0mW1yshZ%2F5ezCGlIW9BjqkAWldF1N18o54bRuwvmAddx7erBgobpRrJgHIcOjSdQglqR0q845C0gxXmd2yaf0G2afVp70CB3IUHCA0WRJ1n%2F3dcDPcVj%2BR9jFDbvkHTu7frJeOBsAGpCL%2F%2B%2B1LWs%2FZlE%2Fx8CkeeQN3XfROGZcpjM0XWrMD72lOQvVzTCh4omuw4EBQSsSJJ7Fnaa9IoYH9%2FSiYkUihWQuT29P%2FO8G20P5AVIgG&X-Amz-Signature=635020fbc7ebee6307648cab613be7a0f40bbdce9e2d02836fa8579f68c00582&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGEGB3CD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQC3ew6SiAJLil67RbMBPrcRADCbMSfhEHC2B%2BxS0l1MaAIhANrnq8XOITmuXR%2FHLFG6scFExPgnzox1VKCkX7SrllOfKv8DCCAQABoMNjM3NDIzMTgzODA1Igww8ReFDO2BAqaCAOsq3ANkagOFgyHNZa70ipifpO7wjLgK6PnUqpSPtHtxVtVGNSPzsOGs4VVTystJj%2Fcwrswt4%2F9PUVUBigWdhdGnjmKNfEiDGpd7JirHj%2Bur6%2FL9U%2BexGvEjTvDwIOgHZnNc3oYSNE1YG8hJdM%2Bk8GL01bhgUwlIBVVhux34CbORFbujrCnChTx1eAE2jKKVPwqBRZQo%2BU2B4eHOpZQYNCfkO%2BZthe6iz9Rar8aaz4x67QP0DIUi6NF%2F4ktlfeGP58koD0B%2BNRA8xpMkh7jnolWsRd3r66KMQGIWHwpy1142UGD6aSaHC8sYvPdYvSCDn5AIogOsqGdBXf73uyG8%2FmEKwLQ8fHnBu47tgJrg4zmWCeSrpUIhce1jKe2Zo4fyaJje6HSbU0O63zdGJfF12%2BRS%2F%2FTl%2FT0G0Y8pFYgdDwv0O26CfDYI9ss87ofIUHFaGbqGeiRTH%2BG6I8CiFfnp99AmXaZUnJ5Kx61%2Bsue%2F1KcvuyRuKXGSWxXubh1tzZETT%2FOB9c5mbaUFGtVUn6P8vu33vRYUz%2BxKyoXAHaCzQ4FrhOzLLcprYTqc8NYwHZmCk8jUKlJ12sQzIj642TkgrPU8pRecuNvETL8aoKnQS4to9z0woLl7ND2lflSL9w3JFjDRk4W9BjqkAb6KkAvilPQX2q7Qipyu8Tct7Uv5a9xY0BLlJM9yAfnGdot43QKBZpSAH1gEUgs7%2Bk1cQkaxyF%2BwpUvi9dUCbxf6ZCamDteMG0i%2FNj9U80NMMmggzdYu%2Fxm7nle36KsH4qGJsaSpXfPSWbK%2FM%2FL3HteB9kRq74C2ciDQNlqQO7VgmoYHpNdSDnAyBdfBmCkjpCO6i4vBSAbItxQ8ZduUW48geatz&X-Amz-Signature=da446fa0fbf5353cd438cf9b573bfbb45adef399fc7a6996b5c98f83dd98cd85&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGEGB3CD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQC3ew6SiAJLil67RbMBPrcRADCbMSfhEHC2B%2BxS0l1MaAIhANrnq8XOITmuXR%2FHLFG6scFExPgnzox1VKCkX7SrllOfKv8DCCAQABoMNjM3NDIzMTgzODA1Igww8ReFDO2BAqaCAOsq3ANkagOFgyHNZa70ipifpO7wjLgK6PnUqpSPtHtxVtVGNSPzsOGs4VVTystJj%2Fcwrswt4%2F9PUVUBigWdhdGnjmKNfEiDGpd7JirHj%2Bur6%2FL9U%2BexGvEjTvDwIOgHZnNc3oYSNE1YG8hJdM%2Bk8GL01bhgUwlIBVVhux34CbORFbujrCnChTx1eAE2jKKVPwqBRZQo%2BU2B4eHOpZQYNCfkO%2BZthe6iz9Rar8aaz4x67QP0DIUi6NF%2F4ktlfeGP58koD0B%2BNRA8xpMkh7jnolWsRd3r66KMQGIWHwpy1142UGD6aSaHC8sYvPdYvSCDn5AIogOsqGdBXf73uyG8%2FmEKwLQ8fHnBu47tgJrg4zmWCeSrpUIhce1jKe2Zo4fyaJje6HSbU0O63zdGJfF12%2BRS%2F%2FTl%2FT0G0Y8pFYgdDwv0O26CfDYI9ss87ofIUHFaGbqGeiRTH%2BG6I8CiFfnp99AmXaZUnJ5Kx61%2Bsue%2F1KcvuyRuKXGSWxXubh1tzZETT%2FOB9c5mbaUFGtVUn6P8vu33vRYUz%2BxKyoXAHaCzQ4FrhOzLLcprYTqc8NYwHZmCk8jUKlJ12sQzIj642TkgrPU8pRecuNvETL8aoKnQS4to9z0woLl7ND2lflSL9w3JFjDRk4W9BjqkAb6KkAvilPQX2q7Qipyu8Tct7Uv5a9xY0BLlJM9yAfnGdot43QKBZpSAH1gEUgs7%2Bk1cQkaxyF%2BwpUvi9dUCbxf6ZCamDteMG0i%2FNj9U80NMMmggzdYu%2Fxm7nle36KsH4qGJsaSpXfPSWbK%2FM%2FL3HteB9kRq74C2ciDQNlqQO7VgmoYHpNdSDnAyBdfBmCkjpCO6i4vBSAbItxQ8ZduUW48geatz&X-Amz-Signature=59c7b7206990cd9b761e53bd17558427d8c4b9554427d0b77f3b575b460bdb8e&X-Amz-SignedHeaders=host&x-id=GetObject)
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