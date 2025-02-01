

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZOTKZK5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEQHXZiL4uyYQPCLVMCREh%2BT%2B30M%2BvCJ7JDD2wYLqtwuAiEAusouaNoD%2BVyKeQLdwHh90YAoniFR52G2inRu7bsFZ%2BEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGtJ6hZIhDXTCiZO%2ByrcA9W%2FALK0WtrI8cb1yxu2%2FVrbice%2F3I6%2BbjYiqR1xRSsDasleLfdXzC6%2B0vB923smMDnAzeoUxRyktKUy2qjdwzA3yHyrNiBbcl9Sx%2BV0YE%2FPy%2FgoLzy1o32oi41MPpHKafzZ81SUjE584zUCDybxNXVit6GqpEfEC6tQlIOpKQg76jQJGOzuYr3a59tN6E6MAqpLdn6QVeY%2FVfFpWQ1kQfUO9%2B2vqCUgrsNQCri9Fq9uVmMDkdzEuoJdBSf3QQWPSnOW1R39afgJYipWkrksfmJQRgOM5A1CQ5ipxm0v%2BUjXHhVA048Wh3FF4KFfgAyQ4nczCwY101ZQQAQMPL8hBGlN9ge9xeIdnmIAfvWqesHX783B6fbsIc5P7JYzPb9%2Bk%2B6HzGPG8uzHv8tx7629q60lHF6KQrIQg2BzkbZbsxKnSyzBgKjoVfkxQ17Qydr2GTHuA0m0%2BHW8qRiY7c35MIBqj8MKJJvtjpYWLJnVCxWI2pG9tJI0l%2BGnkAXbdaTT0ynECRU22%2BAVpm37ffBo2h%2BLWiMtAtP6UP0tPbcdktpONvi0VbOrBKPRNcjx3jClkT%2BbNVyGnD3%2F3SNOls6yUt4RCWM426eGFj%2Bo2PqIbdhFQ5wbk8W0wxdqOzQ0MPrK%2BLwGOqUBzDb%2FWb698k6n9IrIj%2FyBtseCwY%2FpgJDMEOr8iL8wAuWG1fgHss5PqKUhXthHsFMxLkSvz9FK7tJ4aFvVcTRcwSUznDCyykChRt%2FmL80U6MYSHvmjDUmahw5pPXQa%2FxUR0nKwjpYi6yVSK0oGZ6h6YAXbZ1om6imyO090%2BUwjWk2MOJJ7CNxuvdnyMIlHobefSninbwUYR4aLaxUM68mR1QlNU8Fx&X-Amz-Signature=a46c36326431005a9e8b4dd2d78e0c7bcb218d39187150178f59574b6583c182&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PH7GYTS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBZXB6bsfp6QHHaeSr0eNYmywxfF9MSBE9dohytI3BW7AiB1G3PnjcPABUCINF9CIDrwA59QrH5hbgDU2280eh6oiyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLQaMLS2vhoh9BlS2KtwDP4RmI9nS0UhYeKPvKSK1pzsn%2FtxHAEcx1TGMryqPlfl%2BHQJvxxIbsBfFr9cvjyBt8rR3aWa7WQMM4g4exLk13QjPpSBQ0cqSzf5Tu%2FBXl2nU1P62LiCq2Lgq3lPRJ%2F1tXQ7bQveRa4Qq34%2BSXhxTkCNYqDwjcGUmlTheWJm96oHW8OnwqVqX8svj%2FKk9D6sKArPxzm0kzt9k7El5LM8a%2BYfoTMDWaw6%2F6ovfhMYjUW4YwW3hCZxLxB0AP9i8Vk%2BnnEZJy%2Fi%2FWmufRGjH9EQC69wowhmM69cv6dKEHPQk3pBeiOSeoSwYfbjl8fWdxPi0oYmoGtIlim8Sadjr6DSuu1TDtAl%2BwxRwW7AqH6TJbjKm%2BE5KxMOnZGc1Tj6gzMDwVSQUBfq7vdOK7EYzs1%2Fakdve%2BEv45nAobOKuzh5AF0sic%2Bhn%2FUXkWojtkHKoCe%2FViY9OyhMcogVfdB1X40tFmrb%2FfBRZHgJkcisIeizLs4AFFbu%2FW3xztPnIkuvBYTGAQPACvKFCoO9%2FqFvmHAkCDbYc6bYZ2nNuBrCvllFcNr7wArBNmTSd%2BawUUZLf3ry0awLMTwqrh5qR48W1mrJZogCZJa%2Bmm2dvslF1fq1%2Bp9KFcaUoHbcLWoB8SiEww8r4vAY6pgEW2gIExSPf4KG1ckfWBKugdux0XhOwG9a%2BkFz1215ivewBCkkmWLDRkh%2FyhFU4yyOAl4fUtl73%2FaXyePLdz%2FIO2iSrhHIwph5nzcrSLDSfKFXfUmIiGGsSQx%2FNMyfGLXTBx0PzE%2BAn5LDrO4RP%2BkbSP35gimZ6XblK2CIGXjJ6Q7QBnUKFcNDdIgRFoCqhKkhZL5qH6ee4QgcUeyZXexeSaxeKHcdA&X-Amz-Signature=a712463d91e3ff24186959a5c64f5c8bc97f8751f1f7f3630e6e90acc3e99f17&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GMZ37Y4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1Ig0iyFyA7DFAuyOBOmYTW0YDMOugbs2woyKvEVNz%2FwIgNLrXCsbgrlBcrz9U9ma9syq7cvWUL6McL%2Fb537bOgPkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL28o7fwAVlU%2Bc%2Bm5ircA9%2Fb0gfF0myQhI%2BsF4GPlz0hTvqmw1U32tUiJFY7Rzw5yK%2B8A7WHQmV9tSu0RNhML38BjnT1cDVksLBicCcz3GqpSyEgTbBl09kwzXXwkfaNJesTxd80c6QiPon4t1fegoJAzxjg2lvL%2FoDL%2F8cJh2RmEHzIaxZese5%2BCr2zyN2iic5udW%2BM%2BW57WVTmsFXOC24kbjnhjkEk%2FzOjb9i9d14aU3%2Fl%2FZTyUaVHBgc%2FjqtJvbycMCgHTfTQ60mcQxCWJKNO5jbAuqCZvE67MOUwPn3Eh%2FffZohN108vxuMYXVzJ9choLKK5pu6HqmkvSz8gdbDcjnb1u2s5eI78SBon68e7SPLnrZjW%2FN0JCiFW40QipgEkmusWVBnqH52XtX6KgsJqqdcaZXF0IWyryis4scWDIn1F%2BGhv7%2F12nsgOO3n7vCW6pbJ2PaRbRQ3eMjGfUmyGY22UIexC58AaoGMbBPFhLzI0GO7El6BvyJ67cLCZqmjDeYNlYDqMfauq5KndIf7AanmJ5bXDsGB4%2Bhj%2FGnowcFtLSMFeBiIEOjleDGaNbYCWTregzcnPE4a%2FNKqUslMKFHSzE9jQk1UeogeJTU0NYFzTjEwq4YUDxmJDCNUrsSm8YeMysJmSJm7WMIDK%2BLwGOqUBPbpUoc%2F0JuCc0K%2Fnpqa6wv3eEvSsTav6H8dWB8FbIo9bGdHPp%2BtJonU9kN3Sz6zxhnwyxFu9cj88beNMx4m5zdLp4ec%2Bt0TYaRXFvgikWvDTVmkSB5oxNJclpbGjEo331P%2FxIgdYaQG9F4zoOCWH2FaSiEOHbbwe0nKNkO9JF1ixr6TOH%2FCbkNwWh5UjWC4fWFfzCJb4wuubG0jallktQKVUBkA4&X-Amz-Signature=c7c21a60a1689a731584ef32a5869ea8209e8b33db7e707f85f03eda0e608f27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V5MOKRM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFaF5qxXhmCvzFMZoTgwmHQxgw8XMN4P507JO6sQH8RkAiA3s3ONGkq2fYhbd%2FKEAabsIKbKwpcUjxS0KtCHuOg%2FeCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxK8aMpwDX4NIGdFXKtwDvqbJ4WvuOTvfeJGxQUkOmmYZ%2F%2FPMUNjI3QXLJWWjJEUCtnhCjaXqQ2EKR4Pa5GySoJs1CgaJBoIDReVfpjX1LFVXj%2F2POoSYdQ%2BxK1AzO9te2pJrTlUZ4w%2Fz6plzIfEBceHyI8YpebKSqnqvitTbDrhZJizP%2FkASBjE1EHdL5DGs%2B%2FDEw2m22RCGAtZe%2BCQ84qhszjzThF9l9%2BanfzBIDu684Eo05dfKZtTmwVfoI6PgrSXFJiJ5NdBYypUsUgiOExnySMy1LoPEBPIW3cY3F3EMy2t01v78kin6RpNE7THOast6awvMmit1IKE491gfPU8guDzw45ljyorx6cGBlmq2OGdEFaa%2FOikPHZhP8gdjJufo438En%2FbX73GUqkDioiaR1LMmRjlWcsCmQ9S0onRZI7aF5%2B53nd5eU9OlCH0X61migQvvcrc9DaaiCLTm3YZYErWU%2F2NVxrDEQGi9Oa%2BdKm21W7AqMDomxA5Q0puu8mhiG3joLFed2wXFiGGoBetJOREE5Hq%2BkQwPYbjcVO6OLr6clrSmwSxb1zVAgJGYcQy%2FcGv1Rv4rDOQhhmEkXCiXq5BHemwreHBz2ebj00gl4ENW3vqCAbnGmY1rf8%2FTt3Wp6o4h16COpyEw3sn4vAY6pgFZzbo9XmUYlP6a5djDfT%2BpttBnTycsy1Rs8OewUVyKoDah1geRapfVUXsTTw4Eam0Q10RTZFmIZlC3ZKXQT2IKmlKPHh7%2BL3DCxsarysLkRwff8JuwDwDo%2Fe%2FsWbsAqquYITm%2BNfSDeDiGA4Rg5HBOuOtErRn3z8F0OUoFxObeKjok2rnRY2KpCprTSdWz5FGiCSofP0REvK18W44beei%2FlyHELWkR&X-Amz-Signature=b5801e64a87beaba2616e8ebb6d02caf50ecad26f1b6ffee30232e2a02e56e0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJM4J2SZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4t990Oz063AlYefBZoLab6gneNDcMlx4owJMVqBcCXwIgQo8B8WOtDygSXGVLAIu7S7aPZfJP%2F5yJ02NwGuRRqhwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBX6K43RrXAmNI43vircA097OGLltJ3VOZpvGCkL0cbLnh1TA1hQzuVgYZRijuuYiFLPqlj0X6pGdWE5YeWuHf6h0vl%2Bi%2F4kBA4w80oZ0u0eLD1RITHJsS%2BUjbzpLTwT4HL2NuGoTGsmoBHG0SKTDCY3uxs9xnj7ZbKYcJvsANi0oqZgTHc%2F3kfH1NtfWnb90gfrq7FwcHCJXf6TGUArGbe1SKWAMu%2BV5H365VNczJiH3ZTTZSTNIn8ocW6oRUaj0%2BvO3jTElmo5csSllOswnxHNq61O8pXIe1OM%2Fy2Rooie5efU5ybeakyOtHrAN%2BdE5F3jBiZhFCzyYFUJJ7o%2BJI0KmkgSJWYwjk5nwz28dloOPQ4WLBFqOqv2EBfpZNt5%2FNgSjiJcYSkciL9AMv%2FKeayh87VBe5fDMX8Hk%2F%2FsY7BAAZlh34tIfe5MjA2gIXAn%2FpWl2bVFbNyF%2FDxYjr1qe%2B%2FRngx4AWVr2RHAIvgAnVvkSORbErWQI%2BULocCElh6RhD4VXyARPz4yEJBf8HluGbUNkW1zOfYEI3FP3%2B2%2BPvUnHQa2zvBq08CpQ4SxSaU0I4wAupxus2eCPtX0%2FHJimcbfLtaYfuBZX9NV0j1s%2BJU8a8B1AVH20i69w7jUc3UeQwNfkaDdJu4WwrSFMM3F%2BLwGOqUBHNaAaHiN4V%2FQlN5D2WC6NgyKcfhGRjra9F1eclWiG7ZffDs4qUAaMmJ%2BNe9qNap16s%2Bwz7o%2BBgpMayo53uUyCY7%2B44hH03Zh8FA4mrkWhuuEjCaiwV5yE9di1%2FbimOQA%2FqKXBdZj%2BrDTuywp8D7XwOZxH6ywrqq%2BLjjnDzsYX9gTuQKIFR5GNYgaYAMCFJ16g2gvPZu9BEpkm6dwbEJ5QLm%2Fdrtn&X-Amz-Signature=628b63d2dfc6856acb8cad6d1e26b4b6093ade772aa410945409a23f236e5c47&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26PDAH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGGg7T6k7OAoi%2BdnVIwO0ewMxoT6unwF6HR%2BP0kF6FIlAiBb1pXzSLBcluYBvFkfPBmioA2HgPUYaLFF6UF2WOiK1SqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPdzNMm1ExYg9%2BhXBKtwDr3IFwEk2QSccuZZd2ExlC%2Fn7SJs53DrNXAbE9gHngowIJ6%2BmIRdK0dQ1GhY9AsCaIHwO2VCst5NwhKbpW91%2Bh6SDjkG00O%2FO7s74te1xTEg73XhPr3a14O7HU%2FYwSBova1SGjf%2FeRH3l1hB4PeeitdfDTX7WTVxBpHSfNg37XXgp2uailVuGf3jAQ6vL%2F0EhJRt73UXe%2FcZErPcvsMMC86Q00U7eo6w7Zu%2FcOP83%2BEfmndJM0R0JD1YmzYzPXGEGU0Gk7fN%2BKeceMZiK%2BzgfCasSfwLfe94%2BgRGo7Ocs4M4FNj94HBp7d4bisbHaG3nz42Bufo0H6trZodBb9X5MlKJmMv3fG3xGqpJapj6LYorsFUDGglQWm5OktEO8MbdCYOOpWNnQulqJhsd5aUFFyhYTaqpD6YrTMS9g%2FrQmNUOfhN09Zg%2B%2Bcyi9BizsyCPZ3hKwXj9fgPSlaaHiAc8LQsdgZHFoVfHz47mNWMCe%2FH1dNfUtk%2Bys0X7qUJ8KgORn7SP3NQKaJ%2BMzbH9C5GXhJMGgtyHE7OehV1OqImm4BRZZndr8qKN8T2h8xTZZECNPFXlyAkI4bpulmEFTal0tizvz1EsTmEJlpA5yO8Z1ORleE0rbGORQcAChraYwhcP4vAY6pgFOO6K%2FBtjrQEUiAAXGzMbivj1vFrpnsUQz3fLY1HyAUJeyEudpXsJ1o7OnVFpPpC2FsB5iOYfBEMxZFbx0cFpqB%2BzuhvhpjbzQUrBAdYF4%2BVCWJ4iykpbkL80UXhyeDKtXeoqKL%2Fne6TIL17QzwjeejGk6s4NWVKB1cokq0hvirIwXoGSXLwlcFWVK54q7SHVLr6uD0LHnAfnimacPHtjZ%2FfoIzqcc&X-Amz-Signature=1f94a8b5033bce91bcc4596d99687d35923c456524370f703c90b48e6a405fff&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V3GNXVS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGmA%2FDqaZoSK8hVWxUyJVEg3DMhI15eFET0x%2BV%2BLgMpIAiAMCA9OK5cG1vSTuHFhwpfOIm%2BY%2BgnHYl6chT%2BbKmHrxiqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc0XA%2BJalQh%2BneSL7KtwDEkmaOmtVqAFq4WN0oCoIL1apXIeThNVOIgxk9WHCN6fMqL3iCqk%2BHiLymALlTJRLIZeWCv41vRTmvT4uANb5UT8y8BSWa%2FaLJ7KyEskfLDwK%2FfpyYUDiXpsVAydSYIbXNAVYb%2BTDziEj403n8fFKUfPAOZgrlm2FEXjbMggLmWd9GvdOzTudrw1lt77j304VS5WvttABik%2BxhT%2B6Q%2B92o6S1loTCri9xPCR3jVJqJk%2FaeV%2FA%2F%2FBbBPg8ylIr1IhdTrVFf5Zlo3B2tt9obnRo8L%2F%2FQoFt3vP5xhqZTF%2BfNiH6UvAMsWBicfhrbOjkJY7BgxNArN0Fn0D%2FeAtNv3johD1Tz1RMRs%2FW1ePnK%2FmaR7LBDU%2FRzRstFFUnK4bJ0HpWFGdFEmzm8jznlYjdZQMQ2%2Bd7%2FHZH7%2BjSHYftj%2BXYrTrUuOAJFoFVn7qQ3VAtg6iDQcpblHKweV7CSjqa3p7D6aEozpVSU2yP2BjYlRjI5GXXc9JY0XPA7dmuSLMQzH%2FV3ibTKJw5%2BDdNPZOI%2FTgfkyT39PS7jypepepyaqqLBBsOQquCVQwqzaLoH942lgC7BE%2FME9TTAjBRuAy%2FgKLgwy1p8KI9yEqCz1icBCx35OknIqbdptMzxWFMZxEwzr%2F4vAY6pgEnuyCHkLSlOPtkfMIJWvF%2F%2FTF9ASamLaSWFyDHyMCkc2w3RqhUzLXiwrOV9w3dQJ5l0PQ9bdB2SAXwp0AM4e%2BdNErdF%2FJ4NNpU3rZPAAM0XliFyzHCxuGpzDAx%2BpVN%2BwKJIDdyR1uQ6cUF1vKtO1VcwVN1%2BuXLBMg5ImwvBy01qWZJbu23G2Ffw1S4%2FVveCaxAZmfWg%2BtaORE1qdhZiAHKew9QX5Pe&X-Amz-Signature=66a5e877e4c0760f5c6cab00de80a972876bd2a885467a4aae2b4ced6ed51bcd&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663I6C53SZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID60nUAKWJm6aqEQ6X6M6d830sdeYaVytkl1j9DQgpF8AiAqLJox%2F706HqtuQzm%2FH4CY%2By5%2Fsrt6TFZ2gU%2FpE98GmyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlCjgrROQzIKG6aRIKtwDDJx4PGiXqAgeZU3epGmy0GGL594Y%2Bxz3c3uvp857NdxXZ8Hq0n3y82P38NQ2Rmlc2KV1po9bMF%2BVwrgs0brjp1A5Z9uPni207f64hXxlANWP74brwL0QEd7%2FQ0id8ozkE1Sr0kblrZ5WfYAksvMxQBB9GKlfJn84cNRrm%2F21EbiIcbeDxDaat2DmzACit29Q10OIciBFuNaQTqqJ6gsyztjdOcTmyDshlyuqjUHlUnLTTatq8kqHFXw0umkuwwEcukMwbxhRwM5beDK8X8Gcm1ZAGZXwInM3TyMC%2B%2FlTwDTLnDi2PC5HfLHPjcSCyPUtK24cNH3LHcsZot3F4ztoTjJurCitpG1tWxFfpX9NFP20BCi3X2d4HAbYfs4PMe%2F5vmIxZ9%2F3DCkYwq4%2By6MB9lgtJ4%2F1CVVZgI8RiBb%2B%2BUitZTwXyPxuZFNCQryJCdfYBA3JOMQdBqzFBVg3OJQyfS7dOEavZyVCIYdvxu6LisLyejwWTfa1yoCTypJJDQ5b7%2BkieryLtPhdPntIWZIlJfvlgIGlLCVDQ56pkPXsDPD7G1K%2Bn0EPNvVUDB%2BX21J8KYLaCaSMrjFEwwnWX8JkbU8FIep26b9%2FOrqREGblTdjmU%2B%2FOKF5DghgQMX0w%2BMX4vAY6pgHEaz9%2FUx%2Fe34tladvbvYskC%2FXDTdDLnEboE19L13ANzAv8%2FlvG8ApY%2FTYFD%2BzswlgT7t55cI7lDXXSaZC%2BZPcScRCfqR%2BnUTlM4cVN0cuwQmDbs3AmSl8ZuFVx6W9EygfeIgMgGFl94voVhJtjh%2BwY8C6ev4GmigXVl57NstzJVLjm37DDCb3KuwKPsKhjGjUjOmEcsQQUh6QaKSQQ%2Boziu11Jrnxa&X-Amz-Signature=5068848f3387b32a94aec370ef89b1e8987398a720388c169005257a27d2b9ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJM4J2SZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4t990Oz063AlYefBZoLab6gneNDcMlx4owJMVqBcCXwIgQo8B8WOtDygSXGVLAIu7S7aPZfJP%2F5yJ02NwGuRRqhwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBX6K43RrXAmNI43vircA097OGLltJ3VOZpvGCkL0cbLnh1TA1hQzuVgYZRijuuYiFLPqlj0X6pGdWE5YeWuHf6h0vl%2Bi%2F4kBA4w80oZ0u0eLD1RITHJsS%2BUjbzpLTwT4HL2NuGoTGsmoBHG0SKTDCY3uxs9xnj7ZbKYcJvsANi0oqZgTHc%2F3kfH1NtfWnb90gfrq7FwcHCJXf6TGUArGbe1SKWAMu%2BV5H365VNczJiH3ZTTZSTNIn8ocW6oRUaj0%2BvO3jTElmo5csSllOswnxHNq61O8pXIe1OM%2Fy2Rooie5efU5ybeakyOtHrAN%2BdE5F3jBiZhFCzyYFUJJ7o%2BJI0KmkgSJWYwjk5nwz28dloOPQ4WLBFqOqv2EBfpZNt5%2FNgSjiJcYSkciL9AMv%2FKeayh87VBe5fDMX8Hk%2F%2FsY7BAAZlh34tIfe5MjA2gIXAn%2FpWl2bVFbNyF%2FDxYjr1qe%2B%2FRngx4AWVr2RHAIvgAnVvkSORbErWQI%2BULocCElh6RhD4VXyARPz4yEJBf8HluGbUNkW1zOfYEI3FP3%2B2%2BPvUnHQa2zvBq08CpQ4SxSaU0I4wAupxus2eCPtX0%2FHJimcbfLtaYfuBZX9NV0j1s%2BJU8a8B1AVH20i69w7jUc3UeQwNfkaDdJu4WwrSFMM3F%2BLwGOqUBHNaAaHiN4V%2FQlN5D2WC6NgyKcfhGRjra9F1eclWiG7ZffDs4qUAaMmJ%2BNe9qNap16s%2Bwz7o%2BBgpMayo53uUyCY7%2B44hH03Zh8FA4mrkWhuuEjCaiwV5yE9di1%2FbimOQA%2FqKXBdZj%2BrDTuywp8D7XwOZxH6ywrqq%2BLjjnDzsYX9gTuQKIFR5GNYgaYAMCFJ16g2gvPZu9BEpkm6dwbEJ5QLm%2Fdrtn&X-Amz-Signature=3426347917f4beeda9fb3141a083cd2028d18592545a9b0e54deb22ddaff3230&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MBEXLUT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVFnE%2B598nEPx2cxa0bgKAKx%2FuRmJ9IMUKanZCEAPIGgIgfjbYOqSRCT6Omt%2FiL2y9NKGWIDD8KeBH3yUhaGFOdHIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMIqXIZ50eNZYu8hISrcA0qNpCAK2HKM4mQRExax6sF%2B8Bsjyp9Uw6ANpLwabqqrwj4OPmju5vrt%2BADEtigZc%2F%2BY1VET5icUbikriAF6EBmCyrtUxMfuU2EGuBbLCGuPWpq6JUA%2Bvu8czb6feNB6s81cdLuzlEhKMIdUNtpAsBh8CjSuN7cHJF1XMkJKAASSaNeXyslLSgXK8DQ8pAo9RSWF4MRFHtD4rdt%2F4wK2LNPxhbq5eDeW3mKi87scTTj5e0i7nWfU9R4YEcp9%2F%2BKxBDHvzgN%2B5Xv8mRLfSvPxmSghTptfkLnvgWbPtdHVfPMNoA%2Bp3oXo82TTsDYuGZdPdzfpxv3cc41Db6DYYB%2BaZbF%2B5IWtcep1c2TKgcxHOaxQWIh0AYDB5qk8Z9Adn2ohOaCwnQZvynFgudm%2BlAlrHVxmOQHERtMxi8dusubmiu5BMWblOA3%2Fx4V05U%2BX9suVYz1z2zrSrM7aauSysidxBOFMmPyNmDltl9hbTr1nBuw6A89MEpvn87leIV07i49JfZaKTELluxDAY6a7YUX14G38kFQnS276uUQZHww1qcx1vMogG5aN%2B4K%2BL1iPi3yw8IbAyUmqdph3x9ojlIlxNnpabI4RT23yzPOO%2F77cXcrGaE2UtpVEbhUikyGcMKLB%2BLwGOqUBfbz2kaEBV27UQ%2BZ9s7x93pgTWPsQfvHUiwaWyn9wQOA6jbqTTeMH6EIQnNsPQGFl7AhkYzBmG8KdlrNR9jp8xV9EWTsD3sLEeeLdmus7Km%2BOYoM9KnvP%2BnIlXH3OOZpTQ0Rlfus8DnBopEv2YPJxthgceT32wOLhiwaJYxnoUgsvMc7lv1DsTUTbIW7Ad5ZP%2BbcXeKjpklQR9oF%2BYZRnIXztXxu3&X-Amz-Signature=5f4ca9fefb9658b5b963e3c53543a99b287241d7f7969a75f5c8494493cd94b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MBEXLUT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVFnE%2B598nEPx2cxa0bgKAKx%2FuRmJ9IMUKanZCEAPIGgIgfjbYOqSRCT6Omt%2FiL2y9NKGWIDD8KeBH3yUhaGFOdHIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMIqXIZ50eNZYu8hISrcA0qNpCAK2HKM4mQRExax6sF%2B8Bsjyp9Uw6ANpLwabqqrwj4OPmju5vrt%2BADEtigZc%2F%2BY1VET5icUbikriAF6EBmCyrtUxMfuU2EGuBbLCGuPWpq6JUA%2Bvu8czb6feNB6s81cdLuzlEhKMIdUNtpAsBh8CjSuN7cHJF1XMkJKAASSaNeXyslLSgXK8DQ8pAo9RSWF4MRFHtD4rdt%2F4wK2LNPxhbq5eDeW3mKi87scTTj5e0i7nWfU9R4YEcp9%2F%2BKxBDHvzgN%2B5Xv8mRLfSvPxmSghTptfkLnvgWbPtdHVfPMNoA%2Bp3oXo82TTsDYuGZdPdzfpxv3cc41Db6DYYB%2BaZbF%2B5IWtcep1c2TKgcxHOaxQWIh0AYDB5qk8Z9Adn2ohOaCwnQZvynFgudm%2BlAlrHVxmOQHERtMxi8dusubmiu5BMWblOA3%2Fx4V05U%2BX9suVYz1z2zrSrM7aauSysidxBOFMmPyNmDltl9hbTr1nBuw6A89MEpvn87leIV07i49JfZaKTELluxDAY6a7YUX14G38kFQnS276uUQZHww1qcx1vMogG5aN%2B4K%2BL1iPi3yw8IbAyUmqdph3x9ojlIlxNnpabI4RT23yzPOO%2F77cXcrGaE2UtpVEbhUikyGcMKLB%2BLwGOqUBfbz2kaEBV27UQ%2BZ9s7x93pgTWPsQfvHUiwaWyn9wQOA6jbqTTeMH6EIQnNsPQGFl7AhkYzBmG8KdlrNR9jp8xV9EWTsD3sLEeeLdmus7Km%2BOYoM9KnvP%2BnIlXH3OOZpTQ0Rlfus8DnBopEv2YPJxthgceT32wOLhiwaJYxnoUgsvMc7lv1DsTUTbIW7Ad5ZP%2BbcXeKjpklQR9oF%2BYZRnIXztXxu3&X-Amz-Signature=95ef2dc267a8d83f0f17f442b0283db1307fe8fe5f91db3769ecf9c488c03a5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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