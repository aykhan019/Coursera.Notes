

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GZUGIN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEDQKnxS%2BxvZIz6xl4kexPXak21VcbViR%2BJWySnSfbSqAiBlyzb6SQ905zuFPTj0mSe7JtLLv2%2BS3EOJPhc7p2sMqyqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKfHgxAd%2FTWrHQ9b%2FKtwD4K1mmcIWattVA2wLdGkuLLwintpsWjm4tEdlMLUt5CTo6ixT4G81KK9xUwEn1U2b9pUSCwhBsCvngEB3Zw1DU4J3oohttqZIleMfY9dx7d%2BI2ANzNWayBWTAMzoJ9obTh0%2FcZ77qqdvMvwjTI%2FUJtJpw0PPygP6jGvqxzM2Q%2BR0VbJiUPQ%2BZfD8HfWzY8fP%2BFKFVNi796Lko2lKwcj%2FltYhBX6NgJ4LjJbp5f7ED0XuTy6bZGlzfypxdnx6aTAdGedvUxVRfW2xfyrTAAidGXYfDobqKMWiDHhLcnCZjgjjvwqJIK4XVhkPXHP%2FTX1P%2BxBNj9hyewUlZExw2jSKB1a6Rbe2h4EVuHz6aiVqQHJZ4QZJK7xlhXvq%2BzTMxSnibZAsTV0p5fnV1umBUwLypaz6Kh0U3fFkRkSLKpszJgF5CgF%2BcZuagKSSXFssFImh9FDBEc%2FZIy82zNjaT1N6Y4q3c0fgVvAiQCf1N%2B6MzZzzSsCleElFQgfvFqZ4ZdpApNZlxsHgZDXmtacnnCE6D1EWCb3qkT%2BE3wE08wRc4MvIbbUBYVvA9tW99a5u8YpdziQGgwzZhtjZe4%2BERaud3a6aprJCcrMTd7JGYEAAZ435JLdEaFXr4k%2B%2BBhHow1uHxvAY6pgHHDm09295x0TWoX9KV2IbaSqgjZnFHZg7K5Z1Tbokqbs0tmQ%2ByBWmHJGCM12GXxl5AidEXd52JzrC72PbV2OcOSeaJ84XWxuhS%2BFAk3XRBnnBNuEKdo0b93CkUHL1ZQtm0FC1nC9DAuiLkTVoLzD1JGxfbcIVtKA4OXnQRjIInb6qYFnS%2Fp8E%2FTn2t6DVHGfyfVZIDwlapiyOvKgVt3f4YXFjf%2BNBY&X-Amz-Signature=016fa8b735928d2083e5a96a833bfa066e3a3c0b14d60be347e45cfcbaa8243a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WUA743X%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDbRlhVG%2BLO2B%2Fav%2FxhLd3f4hfBK2u6eCHOEytobBEzJgIgA6Ps4jY2V1A3u0jKKoYPF%2F7zth9T%2FM%2BhckGOAqfoQVoqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLOuMoSFbbqE5kpBgCrcA7JVs%2Bx4QWSC24hSeavHFMdM%2FmJ4yxAikukXcLDTJb%2BnmSkbmtszTsbhJWxPAsNy0BWRNHImvi3luAFDu6OBLpO0m7Szg6nRrVrrSlN9oRwvRpHq%2B0MbtntL7kD6D74Pyj632TbdRjN5KwSN4ceJoYUsNgZpqbCa3e6D3ZAcpSVj4JchXmZCbMXnj70B0O%2BOspwH8bdHgR3BoGMK22O8INJTiJESIL0DYGJRgGsdB0ksxNHlAzrPHDCUA2xy805wYfnAAj39FFmYwMmUddm95JvfUcfhO6lKITQikuhDvFS8G1Mi93z8pm7REMeVWFTW20cN%2Bnpm0moiMBzOOMIst17Pfuz2d3cotfGa0THkhzHk5NqCYsU6X%2BLi3ajIt%2FYz2OhTHAe3dyZOM9je4HzHFNh7favHAVOjL1X33hy41e0CI5pTjmBxIVWYckHEFVATOZhWIl%2FBLwDMHmmyY%2F8dndYxqt%2BNr9Y%2BYIq5Jsw%2FqlUjMS18mIyIa2Lqkx8GjyRmB6c82DRipVx9GNuHsnafWWj24Y2EqnJKEvPr6F7aTqGNV%2FBGNslE0%2B7exdC5n1ABNR%2FUWigJ2LV9kVGHW94XXAf13hCpsR%2Fyl8dlhuSWITfQXz5Tnz6NC%2F8v9tMLMMzh8bwGOqUBZHwtfRgC%2FMwBABTyxbWwFwnQfCunZvnkU0hEUAQoEPM6e4LHzSg0MPjegbQ%2FR%2FvF%2BYm07RDmmt1vdmRo4nClg1Xc0OY6xYCf6g1grB62cOBlbh2oDmVnbclfSFhavVF7EX3WctxN0Vy0LjTDL%2FoCSECRf8oDeLanECAeLOm%2FJIC2kK0YO6%2BovBkCfFpH%2BVfLa%2BPsQ9m2UlKvlclQWc78JIue8%2BaD&X-Amz-Signature=68cdee5ceeb571179d4b638bbc0383707ea6dc11707182a02cd4a6dfb8653fce&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TDB3PER%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICVA0e4IAT%2FvXmOm1InuI95eNhwJAVELiSTBdTiLUvnmAiBTPXm1gnc7HkzQpzUDa2SbJMeyorsxsnoddws9NM0w8CqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlQ1xWcH9XM0PKmYiKtwDFYejDMJpnt4tw8nZsEhsyuURg3nN8Gsyhft7WoY4blf%2B1ehyZeSUxGAa8P6cOUF6e9Hk%2FdWlGja3sWXqqy9sFrzaLVVgBoumfCQU100y5T7U%2BXzEpFMklASMze3f7d88p7FNA94Db%2FiBGWu8nCzp74M1ni6%2FAotuFuOSJkmV%2B3LmH8YXE4yUqPVB6LMDv3I3ZhX1KZ%2BGFXRpK2yz4wAAdss3QRFGSm6YWJwKTS0hrMRAaR7PLeW%2BTNx8URvdptWa0YidmvczrTIAIrrv9nKc3VZiRNeLKGVWqlx2wq4N8%2FzJypOy9O37K37JZ0YQrIfpwzPrnnbfT9Twhysd3PaVX%2FGre3U1LsoFqD6zqEebjTtFyQUCLC8rnudv88Q0MRFE%2BQj3NnIfS13CmAZ8sisyM0YrLJEL8maOo7OpIFhNbxtFSyQXrphJl07wiFZJjsYhbhC3orkpunLealLKE24ijjBAl8eGWjfXKqqvYulY57Uvfg7WB7YlnYI%2FkuVuhZrODQMWmve4BaPdflJHQZMJNZSOpuIBMLOvdfPnk5VuY%2FOH9q2xARxIdXjJVtk3oaYsW%2BjkoaORaJnU6cPDHoYDBwBEAFEbYfUeG7kwpVRTsj1AavoyxwB3HnKQaysw4eHxvAY6pgEoKyVosY00PVV9cs5Y2bIJ2hG0hQrcO5tlB0eB5kTo0pt5LCrjBNRBV42WzbY6IlMEdHSc6CDTklWIXTgx9wm0%2FY67vmAgn%2Fd56yrZoqgeqZrsPWufc6MJsTIR06nANIxBLJKht21CxE8j8K6NK73%2BjNyI3AypiALeZE%2BXB6vw5eHi0qfmKQVCnb%2Ba87t6H%2BwFEyWkIcERTBmGEdIgYQMUVpCDZlkm&X-Amz-Signature=657995cce1f1cdb41b958e3f141b47da3a6fdf847b8660ca244d0c853975aa32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EBFNYXI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFi1a591tp2PJF8zCIwBwNL7IgYMq1iWHI8xHUaFhDMoAiEAmfVawwajU9Nf%2BfbHtvn9DNbMYwLGSIyNy84AvJ1mNmUqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGk2joSHScoVf4wqHircA8uo9LllIIcYLpN9xna8JqWVWPXYNVDVgLK7yOaj9f9CaOqObqSds6N9XYIzcOBauIQXbHSm6hmnKfUtS1JXqDi1UCQfB7t%2FsKUIIX8hp%2Bfc9dwHwTnRQvdLNUkTpt25oQBLDy9eslyt8qxPLTQKds%2FGQgWmxiA9y3oiyjXUpG%2BSX%2Fg1zsSxJRtZ5bdUzAGBbO3BYDbZSbOGqwQVxKhAgnroPlLU%2BmfRM%2BVXbqFTMgCrWiumx1so0PonNHAnySKn7Cj3aaXNmcjHW%2BSKBop9DsGafOTZ2OQjpTusurQN%2BDOMOG4paDO9CDrs0MloyBnVifw8vhf1iShwU7fPXrRK%2FYNt3hMHQD5VkWBt8YkRbbsYir%2Fw40NDEDj6qjweLb5Bwd51%2BG7UK52Q%2B2LJ4wN%2FBPWPNmMr3rlDRLJHdOoF1LwLh%2ByzHk3xMsPq1E6bnXbjtRgvxnM5R3xuviMj1Q6HCNwXiRW0Gmz1J9%2Fa93f1wdoZcKQNtT05pWqimX5JKmrEoZqruSRVBMGJBO1H2E8SUAbV7OSQS26MjuYX%2FfPdzWh%2FepHIpT1Y%2BAiQu6QzCI9zyXLGrPNLQT%2FMovjtZKXFEvT7BHeDetA8Unfl6YTY4YQ1fEdJtcfvP9Tb6d1iMJvi8bwGOqUBa8dGHjwBrRiFg%2FdPMQZJajjhU3g9jKOLSei6Q0oR0Xh5tO3jZESe%2Bc%2BUdZ%2FJt599wvln04hy%2FbMxUwV%2Fn5zC7Z43sXo67wO8MGtXRtg%2FAlfQSlhMRL1IkrVXemXSNedJy2xqCx4i0WlBQvY%2F9Byd5CuonKcibTUkEu0PYEsBZUN7%2BKU2%2BcLGQwbmCgOhYerc1FniGbOlXJIPy9TZe6dddjdW%2FoGY&X-Amz-Signature=3eaa0cfe574622e68d75b60e0e3a51a3910b0b85f3a77f7f925649aad44239cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HN2VL37%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAN58AHjaFL0xXExdfM9lhlIqvUzRrmHgONrG85kGCwmAiEAqiN9xCUY8oLx%2ByLm8DybW2DOegGDw7t%2FYkkWevOZ7WMqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKNnld0L33MLizd0ByrcA2kRxrjGI%2FG0xdzxYXK6bZU7q95NPyt27CLV9jS2i2k5NEDUC%2Bw%2BBUqIoFqtVF65Fsq9VHPgWXLfYjzVekWDWBsVSQy6eaFenGgXGz2ToVIj%2Bba2KNjXMYmFtQEBiRsqDlKWuWuLtZUkyjabwc5Ajy4PMMrK3SAd%2BSom0d177Q%2BaoE4z4OZzO1NzNZMvR%2FDUqLz07hTE01iOc5sGUx8r3dZbSeL8yMmnPn3at2Wn%2FiDrHZ5fGqpW%2F3C%2BQTOhD6ixpz2LuPGLcso1u0MpqRSHtvKBjF7CJm5%2BRcAtwFBWNsLGa%2FvN4RHvKTFYz8KcDBFauJMbgUutUvr%2BrTF%2B%2BM7z7XrkBzhawvAWqk4vyFm4D8nP5%2BsF8HX2wG1%2BW7y9ZWbj8j00LEerSpHN7z6deYBvba%2F6gvjUYIOkeBhnjwdzh5%2FbtyJuVywd99XgPjnNjk%2F7NOE5XmI4pYvtoAo8kA0AUFpdmuIM3piE41x%2F7%2FpFjcDxxRf%2BpmLRnIzwKlLEO9wiLdLNTDmtGa4fgG7BE9klyZVg4KVkh3tJonyW32z8A9iqSjrU6tkXDtf8Ar6Cft8ad%2FcFcGKLYi%2BeuT%2Fesxun5s7AAViGUGs%2B6a8U4gd6OLZUqJvKXG07eE4e7jA7MPbt8bwGOqUBfztO6LUy10%2Bf61KVAUjpF1aNwMO5WG1n1D5ksZOnRPMdL5kUAZGPZPh%2Fuj2AEkISykd2%2BtB2NoX2wuhZmXDRskbYds3LU%2BszJ2wJ4mvMAnjPVhW68CppM4LjjL6sLPxUkSVOKDLCXL1qgGIvsJmc%2BonHS%2BLZpPSe18MIS6uofCT8q%2FoWVehH04PgdUXoztsy4%2B5Sx%2BCm1D22OcD6D37cf1GS2di6&X-Amz-Signature=59f46748ee1c44d789808916734fed83f719f3af341b83fa8b8b5656012d6b6d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLZXCJOI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCULqoIcN33alGKwZVIwUksvi7nLCntP78Z4mAHBloLvAIgTvMTiPi1zgX0JlHl2Piuw2fTF2dFTqCYeyiOV3T83icqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3eT6Er6xeb08OZvCrcAz0utoBjA8AFJPfSkkFDvkxKKVQxtYdARXMbeA8sLyN%2FL9u8%2FuYlKn8mo0Gasf3c1dFhcsdT3op5HmKqNdnv5%2FjHfX3V4M9cbfNoVCFbBvOuNAjF7O6N5b28Zw9aY%2BzhLuR7BxYQxoMWpMd88o1xuJuEZeZlTMs3EpMCgp%2BISKyX%2BmzlrNmyKdBNQv45vClaaW7ckyZNjhfM6JiOYJDuyuK4r6Kmj3Doz8%2Bd3KcjhaCuKdh8z6CLV6rjPeLXwhUxhgwV1P5GoMT%2FkPvtQgiONDlnldgIwTH%2F%2B554w6saPwY%2BO%2BvQUdcA3K9wr4quLrPqSqAvaa2fO0VsSLzrS1vQgqlZYGXPQ%2BdQMNItIGrgjyDAAVp%2F0PrJG2zH2Sb%2FnaPuQXYxfpJ9HaBL3QtppMU62JJMCGo8KGgoSW2ovxWO6Vyzo9yjcnQl4F0g8j41d77TD%2BwIdH52dyCN2GOd22Qz8NHIKbms1GV9t%2FrxoWtT5KgB4INRDUcwsDMWXThgYhOUkj7nCVjw0osenWtoWQs3MB02SAKBlE%2F%2Bsa3Jt3exw4kgV7AhzcrPaaGpDCFBPQvY4Ae1mrvVydyAq0nrI7ReNXeYTplcemGqAGVACPTBw49bZLV990kYHzjg9itlMPPh8bwGOqUB4sDa6PJNrOr0YliERVNyFJ7pTi15GNnrOFKlHALyuISDvAV6U%2FLo9%2FKh3l42kJ9jADNHeCJQ8zLYNfU61hhZUxoR%2FrPbb7jYWk29cPWYdl3dOBURKng1xeHg%2BrR1HDsm6ZsHHYhFfwE90KNYJm9KT%2FJT%2FRvAgbp3WeDv%2FN3j0hdRZPtRCJRvhPFH4uleNeqdw9YTTebhzoLVp9ok%2B6LPVFH7m0Oc&X-Amz-Signature=8d2701f4577c9795d173319bb453db734aea356fc9d1916891a441b899d5d072&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UZKJRQP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZRFKVl3%2BU%2F4Jndk8Wpr3Qq8W7vuC0aUV%2BPqQZYRyHCAIgcXhbgQOpwtkDRlg2S%2BdggBs1fj18A2%2Bi4%2Fj364Pk97MqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOJJYN7cmSN%2FaxrwHircA6WMLh8n4L%2Ffr2PhyuHxMsNy5nijGGNQSkbqfbgWw%2Fk4Oj%2F2%2BLtOeINqLupqhvcxCwcB20X1KIbX7xgjA6pA8ZB0fA0883P8%2FV9wVUxSkPpWOaBFDnc%2BlsV53ypOvklRagmnoo4EUIqEsr37wjv79mz2ZJrrhEFN4VFqFl3ALFGr9DMuX%2BgYKANHImFfHTQR%2FB5UXBNXoqbNaomwIGR2D06WvLkAgGYgRTWOZgaeaRv1oxda3ICmofDZHxY1s42wozxeOZmMjzSAa6EcrT7Ux0n2jkxjO1MskxOBwyOLeVTxyDJs8SBnyaZ3U49jpzQs25ikF0425BPbp0atsSQz72as7d1BJf%2FDLQ3E45siIqgx09VPkGVL80qadAt7NNHMD0kmKXPaXmtT55GCYBz5e8YmgC4hJPqYgxe5g6fPJkHnUDEnetg9Y0IOZ%2Befc3kJ2Wy%2F9dFGvCGCN78uOKV3CsRDiB8yss3jTKFNI9gaMcoK1ZUFZljFiA5V7wYcqEjxx%2BbYFINrU8ok%2FFNqxcJwG6T7BLagrFglB92sF2W1rXEfWP%2B3AYiOWiPcaH1dQS3Q0asP9n1i77a2pVS4TLNviFLD9IKqUCSNWPMmU0FZJwF%2BZJX0c%2FM8IEMrJNzDMMHh8bwGOqUB1U2HQx2vPHFSoO31qnVy5YxObRPvEXoTKP8s6p17%2BcabBah%2F2Fs3Gp3MBBK4qyomNgySxL0QrzelzkzVGBB0SNrKA0cuDF6Maz%2BY2uTVDMtM%2F85tY78j0XxLOzBpIb3YLOv%2FixOB2fZhKHD%2BGdxvBbrdlZiSlSHo%2FMh69cpEag6VyjS%2FYDFP%2FzFy%2F8r7dI%2FaBiY47DnQ2VTT4lZNlpkLBg6zd%2B9w&X-Amz-Signature=6480f28c1148d0a401392e16b38f083d108af682052da39881506de34b229b1b&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNMIQBUH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrS%2Fk2c3ApqjccCfXY9O%2Brtonbv7HADRfiI9M0J2Q9dQIgFh6UuUulhbMRJPgaMIGyIi8LoHYgmCjeNBpEF4VOEd4qiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLR1i0y0lBuqo1MpkircA1dFZACijLlfYSjkk4cUw1agB%2BxAGnWDVbTMMTIuF2mSVPCnpyxrqG6YJ1ngzv%2BImrFY5AkuM0uFeOrq4S6P8dZFFgRP5mBoIonrC0gGQk2HRiADrta2tHk5TbqpgvxNJa566%2FUowkK6lI%2FGRTgvGJK2H6CdHcyRBeXPtkOHxR1%2BXlP6mtP9xgz7jsjB0y5bqFLm2SG97QJUKfpKdV2uqwTAyTlRqPwgC2UqHucTZUB3ELcEADq%2FRSZ1EL0BnFF3LPKzyhfBaEEDU38KsHUWm%2FXJuuuQhHa3Nok%2BJMiLXqHWc0oQ8%2F2qrIHm0Kxr5zUdXJ%2BUoAEIpEqNV6P5ABZa1jtP18NAkpqZRVMKWg8uV9QCM6ZTYYPonyRcjQiyLggeXxWbIocQns41lJdbpOlsW9c0K6A0wGmL4np7KOw%2BgxPBn1mZce%2FS5OukiZvPI%2BmCFc8b7JiGxYQ6NkJuAUYGV2XOUEftUp4NAMQs74XprIOdizuZFWdOFItZ1HKXVJHWDuYvFeAhmmQoXFQajICypmgqlAMkYWegjYaqTO5I2gDcVVXSrrL8kGKjMSMT8wefOUhqHXsKHm5afscv3suz9UvWZNTV9X9OoO8G%2BL%2BbJjX2%2Fw68l5rtb3INdeOOMJbi8bwGOqUBi1j8wl59OOm9hK2VTgiYiGqrw%2F4JSnL2Z4hal9P7GGPn2CV6yq74%2BSuunalccbpUqoGheIOE4M7PoOsgi7B1bqWzm2PEp5mzNPHirDiGTkzs9iiI5OBqqiKkg05AsPvd2v%2F2r0%2F0wf5Ep8q%2BHa57MwY3lYX4xa15VaPj92L6zZ2xWbU3DLkIcwntdQD71Ue2DxwuQYAEvwi34tXnGnviGkOTdzea&X-Amz-Signature=d35ca790c357131b7a7be65f479a5564d1b1e9f44d7b188418cf13338f50f292&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HN2VL37%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAN58AHjaFL0xXExdfM9lhlIqvUzRrmHgONrG85kGCwmAiEAqiN9xCUY8oLx%2ByLm8DybW2DOegGDw7t%2FYkkWevOZ7WMqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKNnld0L33MLizd0ByrcA2kRxrjGI%2FG0xdzxYXK6bZU7q95NPyt27CLV9jS2i2k5NEDUC%2Bw%2BBUqIoFqtVF65Fsq9VHPgWXLfYjzVekWDWBsVSQy6eaFenGgXGz2ToVIj%2Bba2KNjXMYmFtQEBiRsqDlKWuWuLtZUkyjabwc5Ajy4PMMrK3SAd%2BSom0d177Q%2BaoE4z4OZzO1NzNZMvR%2FDUqLz07hTE01iOc5sGUx8r3dZbSeL8yMmnPn3at2Wn%2FiDrHZ5fGqpW%2F3C%2BQTOhD6ixpz2LuPGLcso1u0MpqRSHtvKBjF7CJm5%2BRcAtwFBWNsLGa%2FvN4RHvKTFYz8KcDBFauJMbgUutUvr%2BrTF%2B%2BM7z7XrkBzhawvAWqk4vyFm4D8nP5%2BsF8HX2wG1%2BW7y9ZWbj8j00LEerSpHN7z6deYBvba%2F6gvjUYIOkeBhnjwdzh5%2FbtyJuVywd99XgPjnNjk%2F7NOE5XmI4pYvtoAo8kA0AUFpdmuIM3piE41x%2F7%2FpFjcDxxRf%2BpmLRnIzwKlLEO9wiLdLNTDmtGa4fgG7BE9klyZVg4KVkh3tJonyW32z8A9iqSjrU6tkXDtf8Ar6Cft8ad%2FcFcGKLYi%2BeuT%2Fesxun5s7AAViGUGs%2B6a8U4gd6OLZUqJvKXG07eE4e7jA7MPbt8bwGOqUBfztO6LUy10%2Bf61KVAUjpF1aNwMO5WG1n1D5ksZOnRPMdL5kUAZGPZPh%2Fuj2AEkISykd2%2BtB2NoX2wuhZmXDRskbYds3LU%2BszJ2wJ4mvMAnjPVhW68CppM4LjjL6sLPxUkSVOKDLCXL1qgGIvsJmc%2BonHS%2BLZpPSe18MIS6uofCT8q%2FoWVehH04PgdUXoztsy4%2B5Sx%2BCm1D22OcD6D37cf1GS2di6&X-Amz-Signature=e8293a99614cd324935a18fca6d983a418f423e35003a1d566fc0203b0da8cf9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7P6RQF5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID4oKYtNdcwXGV%2Fql9TmkgemVEYbK%2B%2F4cJqu4uBUkbbNAiBs9skyaBdgwvWNaIyk0ExZSYE33Jdu3jAGBu0UfBdkIyqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSEII2hiBvsUc%2FRzvKtwDFKz6DY0IqgZgU5aDFwt3VghNeqeX4E3qbSzb4HjvWMyTaBinuJwFLYWo0eG2HRyjbzWsQNymR6ZMIwS4nEnuSRYGyCvxPaU9WDqwouBpJE0Sd4hbEvtWwALDGlKkiEclSUmIXeiNosmJJPlxDC5cU1la9zkSMXedDTpSBtxMV%2BdABqcVr0dXd5sZwhTNhksUXcJTK6huO81wCrCdlgbVo2%2F30O%2FwrPvvHbdHa0A6p%2FnLpH0K9gWiS726%2FZvUQwdK1eRFBG91xgQPK2Dq1JBbYgBTjivWQxYNGtBDCeo6EcyKWblmcRqZt8Zpg9qj9ObWpI1rJ0Y6Fo396EpIiI02EbYQTc5MTLt91%2FOhrP9M0Rn0lEOnpbz6T18Ah55TZw1TeS7HUX0lRj%2BYTtburB2Xj87J5NGAgPogs442Bs9g14Cafbn1E%2FrT0%2BLz%2BOMx37grCtut7mgxpWuWljYSYxEU%2BCqzM%2BySNlq2bFIZCBm7Qe%2B4QpCGcDp0GePjLhtq%2F%2FEgduxnXHPtOJIe%2BUDRD13mWvjxijACMSlQc4lJn5%2FdE3zmWJxITJsd%2BA8w2hKbj4hNJkISvDI4Yhl2%2FXVD2Zg%2FPBoMUThHlYhJ1Bcl2cU8QVLKVjNc6LVr3gTR4yUwlePxvAY6pgFZ2yiK9MBUt15fkxdmXagZR2nfvSl96ARhGeNz4ZHUNUZJzRqKY0Jb%2BX4B5U1y6IEpSaryrIq84JLG3DvyJE0OXws%2BwKClhlheqpVmwfenkftNWrkuwBISJPP4WJyMq3gAbKNvfVBwmmB1EjvraCIoHppyPjE2DgfSQ3zZEUDPXMHkQVrshJdhSKA6xHMRVjOuTjbxmWwCZYUc3XoBKq1bCYINxgPz&X-Amz-Signature=2c6d450c345b207360077d8d09a6134ed02cad264e7675ec7f3528d668991865&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7P6RQF5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID4oKYtNdcwXGV%2Fql9TmkgemVEYbK%2B%2F4cJqu4uBUkbbNAiBs9skyaBdgwvWNaIyk0ExZSYE33Jdu3jAGBu0UfBdkIyqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSEII2hiBvsUc%2FRzvKtwDFKz6DY0IqgZgU5aDFwt3VghNeqeX4E3qbSzb4HjvWMyTaBinuJwFLYWo0eG2HRyjbzWsQNymR6ZMIwS4nEnuSRYGyCvxPaU9WDqwouBpJE0Sd4hbEvtWwALDGlKkiEclSUmIXeiNosmJJPlxDC5cU1la9zkSMXedDTpSBtxMV%2BdABqcVr0dXd5sZwhTNhksUXcJTK6huO81wCrCdlgbVo2%2F30O%2FwrPvvHbdHa0A6p%2FnLpH0K9gWiS726%2FZvUQwdK1eRFBG91xgQPK2Dq1JBbYgBTjivWQxYNGtBDCeo6EcyKWblmcRqZt8Zpg9qj9ObWpI1rJ0Y6Fo396EpIiI02EbYQTc5MTLt91%2FOhrP9M0Rn0lEOnpbz6T18Ah55TZw1TeS7HUX0lRj%2BYTtburB2Xj87J5NGAgPogs442Bs9g14Cafbn1E%2FrT0%2BLz%2BOMx37grCtut7mgxpWuWljYSYxEU%2BCqzM%2BySNlq2bFIZCBm7Qe%2B4QpCGcDp0GePjLhtq%2F%2FEgduxnXHPtOJIe%2BUDRD13mWvjxijACMSlQc4lJn5%2FdE3zmWJxITJsd%2BA8w2hKbj4hNJkISvDI4Yhl2%2FXVD2Zg%2FPBoMUThHlYhJ1Bcl2cU8QVLKVjNc6LVr3gTR4yUwlePxvAY6pgFZ2yiK9MBUt15fkxdmXagZR2nfvSl96ARhGeNz4ZHUNUZJzRqKY0Jb%2BX4B5U1y6IEpSaryrIq84JLG3DvyJE0OXws%2BwKClhlheqpVmwfenkftNWrkuwBISJPP4WJyMq3gAbKNvfVBwmmB1EjvraCIoHppyPjE2DgfSQ3zZEUDPXMHkQVrshJdhSKA6xHMRVjOuTjbxmWwCZYUc3XoBKq1bCYINxgPz&X-Amz-Signature=3f8177917637327647289863280a0f7e3a22ad24dac3c3443dd04b4deb893fd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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