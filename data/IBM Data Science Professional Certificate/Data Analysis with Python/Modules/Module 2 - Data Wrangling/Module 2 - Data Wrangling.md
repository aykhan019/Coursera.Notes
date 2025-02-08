

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3URKP3Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCICAdrEUAdMGrJ7hPFHjFksKSA8d9z59%2BIhnMLtOdB5rhAiAGkloU1LzmGc92ZN30Tp1KDDJsSZHNTIfpTtIJCxuS6yqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGtY%2FSdqGJ9dN9ps6KtwDGLh4t3AVLp7ml7MYoVbLGOi%2FiqBARQAxy3Y3MgmGGzjQsE46ktF%2FoOqR%2BZ%2BYTsbc19Up531Ji8Y3kiqwKE6P2w3G4TSK0O%2BSR3XLR2qxqJ21jQPq15Rmec%2FrRyRKlEa2tIfCVP3BJ624YBq8n2T3HeklNuBD%2Fv6k36VIraV%2BDLOGz2x57JAwfvmTofEuEOL9RuwpnpLmOaB4nKeXD2S9N3pDimMXByxseUasrQdg%2F7Qb4VsnAOWMHTB9AzVgBtTgfbl3JGzErR5XbQ1%2BQgYApyRxDJIrTXj3y6hHha1wlDR4h6FjyYcs%2BpuIRUVOaywkCTWvbc2TbZVbWjSdKAXHSl6hWs1gPhXIABkomatgIy006%2FmnNrnqKycmu%2BPn0Ns7BSp%2B4GtEXhz8OHWzXMvnM%2Bd2m8O12L24MD1E7YZHEVE6rVIovnN5hyqaxm%2FIaSyxAY%2B9OVEP7vOziUVLinRzYNGkAvf4uNNWlXX7oAxedxNWApPr%2BQT8xamBXqzEmQlx7aWOlGw3EEK7QPZ67O41hgk8udqpQW8%2FXK%2BbZ2DkEQlnwr73KyQCKif831cQ8%2FIoCwNiZwOH33I7R3LTMyW4iHbVE%2BHuWAj6%2FboqYWMQ%2Fqy77Kzgjd0tJdfVAJQw2NSbvQY6pgE0uPHO6skf1YUnzvj88YEpus7EptwyvM5pxmTZ7M9etl%2FLG2vjhLgSKHqzpGDhT6hU15pACIQdpM2QrxvEmMUlcKXeNz4g4%2BTOXcEYQjlpgSo7le%2BTcmL8jxUFRUcTffxzCiDJUB7eN3xNRRrFqqyHTcT82a2hX06q7r%2FKdkTISS45rU2gppzXf4LFzcNGnGE3bfGFR8Scr1xsQLbJoIYveh6a7cgB&X-Amz-Signature=c395aedd4d2a69e1a8945e438604ccf7ca45d08f733c97be0093101fcc035848&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ5PYDDI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIAVGiJxBs33V94mB2yfg6x9%2Fq99YNPKuuWzsg%2B67Lo5cAiAc6x9%2BhdUibQ6MC0Azs936%2F97jbvYLomeuavGWKJs9%2BSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUJsJKQXSHRRKlakVKtwDzcCDXpewxGIM2IV72R%2F9SNuba7YQblsA2GjznB4FsB5eFDYZg1fT1YysL%2Fce9S5%2FIyaw8JfpZqyhEv79EuBgi7hQHxHNLg%2FAxTBwfEDqLUEGurOdiCegDLO67jPmBV%2F0RvRxdjvNhLz0QYTbB5D%2FXbj5Di8E73Ax7jJFWtXVmtgXVaKo%2FnhLP1LX0%2BBkQx3uj5qKI5F2PcjtbHrGCkc6DDz65iZYncXjogUYVFbwam0SBFTJub%2F8qJoYAjJviBjWDUfNzW83Rbg4MJD7DcQa4m%2FD1roZug2hNO3ikQwcMQHcdBRIjlx3OM1hkGMoJvVr1fyuV0WjTzu%2FHBSaSzHOG48zEZJ7NhyvUEPX7Xg1Xy%2BcFjfEacfnAprpHKG4W7Zt8jItfaJjAI8bm%2FpLqF8kNA9wTChOg%2B8usOleeUDqjZQHq4Qi9YRE51ElzocUDowWeIe4gzViY3CnZNcCn8p9BBQh2GxLrz9LdNxLxxef%2BVjggtJI3IUVDYTA0w2Ms%2FXrfmV0s3peheYHkt%2BBmDMpY0Xgui02PDr6U%2FR9Gap4Zk47Q862wYtVbT00XuaN32sIAZjcXyuoNa1XPeUcZlP7706oYnOV7XhDAvn7A7Fidl%2BEvtrdl4LLRl32uB8wkNSbvQY6pgEyNAoW5bawE1oWKu5eYTB53DnCjfaq2BPrYpS20fWvmynb3BTZzvYFDysmTpqvhE8dmIvrKe%2BAXj9WEM9ocLtlXYCyCXoA%2FYFhJbY0xAWzAuPXkjL2K14yc2cy4OL%2BLPHI8NIaJcS0DftbJ6Kzd9vq5yS6lglpzqrJ0ZowTEDdffJm9Ds8Wt3sHbQhEpUhxhkkLg5UK1qL7g03dzIsfyLeWLc5QTCV&X-Amz-Signature=ecca63352038033cf9512b919e186cc3fb7656d171e2a680a429f82e12acf09e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3URKP3Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCICAdrEUAdMGrJ7hPFHjFksKSA8d9z59%2BIhnMLtOdB5rhAiAGkloU1LzmGc92ZN30Tp1KDDJsSZHNTIfpTtIJCxuS6yqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGtY%2FSdqGJ9dN9ps6KtwDGLh4t3AVLp7ml7MYoVbLGOi%2FiqBARQAxy3Y3MgmGGzjQsE46ktF%2FoOqR%2BZ%2BYTsbc19Up531Ji8Y3kiqwKE6P2w3G4TSK0O%2BSR3XLR2qxqJ21jQPq15Rmec%2FrRyRKlEa2tIfCVP3BJ624YBq8n2T3HeklNuBD%2Fv6k36VIraV%2BDLOGz2x57JAwfvmTofEuEOL9RuwpnpLmOaB4nKeXD2S9N3pDimMXByxseUasrQdg%2F7Qb4VsnAOWMHTB9AzVgBtTgfbl3JGzErR5XbQ1%2BQgYApyRxDJIrTXj3y6hHha1wlDR4h6FjyYcs%2BpuIRUVOaywkCTWvbc2TbZVbWjSdKAXHSl6hWs1gPhXIABkomatgIy006%2FmnNrnqKycmu%2BPn0Ns7BSp%2B4GtEXhz8OHWzXMvnM%2Bd2m8O12L24MD1E7YZHEVE6rVIovnN5hyqaxm%2FIaSyxAY%2B9OVEP7vOziUVLinRzYNGkAvf4uNNWlXX7oAxedxNWApPr%2BQT8xamBXqzEmQlx7aWOlGw3EEK7QPZ67O41hgk8udqpQW8%2FXK%2BbZ2DkEQlnwr73KyQCKif831cQ8%2FIoCwNiZwOH33I7R3LTMyW4iHbVE%2BHuWAj6%2FboqYWMQ%2Fqy77Kzgjd0tJdfVAJQw2NSbvQY6pgE0uPHO6skf1YUnzvj88YEpus7EptwyvM5pxmTZ7M9etl%2FLG2vjhLgSKHqzpGDhT6hU15pACIQdpM2QrxvEmMUlcKXeNz4g4%2BTOXcEYQjlpgSo7le%2BTcmL8jxUFRUcTffxzCiDJUB7eN3xNRRrFqqyHTcT82a2hX06q7r%2FKdkTISS45rU2gppzXf4LFzcNGnGE3bfGFR8Scr1xsQLbJoIYveh6a7cgB&X-Amz-Signature=853703d72b77e2c43717070caa58fae60cf3773d58073d94a66ce3301db92fe4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YPD3USA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQCN1sA%2BK3JKPviuHhyYNyHC1VDJLLqBhCbybbL%2BUXG%2BpQIgbhAZU3XXxdYJhrVjd9woVY1sR64DDFasen3MB48CtjwqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP%2Bm4olvZrdmu%2Bm9fircA7fsE7v1HLm9gcndRksuiIU4ltdZfRe%2FMO0U2EFELFRgH1HlkEPkG4k6gs3a%2BntaZDPROfUiHOwhuxoy8thV4gxFaMM%2FrFm3MXs2%2FPRKiZGuum9ITCNaf%2B0tpVGAomyOJYE8TIpb1aHFNFK%2Fw62I2c49%2FKNejAj%2BA1x91lUpszIYfhbyYtGQN1x5EXl2rHiK%2Brn0xgeQ0F4EeBFHCeMI5hrMFjR3jD1XoTkY8lvDW4nIWXbXVG8eMeNnXOWwTvvAmFJplC73JQkFvdYay3alVeI%2Brfc8VIn%2FqthVTtQwatiBXo%2F5qpoxmPlpV%2Fao8mn0BIsXYQU7ZooQcfVZS3Ha4KKc84jFpo7ii7pxCzGfQOzsg28FEonQs6Hr99pectZqo0ah7MtIzP8BZ5qyU2u0bwqlfAPNc1BwSeuzJCRONXWzRRMsFmLKJn2%2FbmTnDFry5e7IEi86p6zo%2BtNDS6gKUzA4zaizYEg9AdTg%2FGR77%2BjNHBT2%2BEWMRZzRGfmMsydXNvI0ieNLc5QvbQ1PT0SWy7Y4s%2FI2Td1EYsTiRP3GjQAFKYfYVi1S4Z83rfk0OYjcgTCpac7CD%2BQVogOrB5Q9OeaOqNMgZzENwpJlCAOsHAlJ6aC2t1NxUh1Pez%2F9ML7Um70GOqUBxfBZ8Pr52LggyAWkiKVDvvL%2BCRPf4om9ZarrjIqLe0sS%2BvbgI3EkHWsyMw6v%2FzE8Fuh5Ed2Ujs7DMJrqcZmed%2B1u5i7qzoqYqA8%2FxI7JweGvshESk4wLvdMA6e327gr8sk%2Bx5iGT8NjS7xIrteFDsWB5aiPSd20mP5meroXFf5oXzOjqDZI9hl7lNSx2iEuCPs5clhsoT10iuR4M32Mps6gtb%2FxH&X-Amz-Signature=d09bdce0ee9b14312890b686efc4814ecbd4cf5477b6b8b4e48731764dc9f893&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624QPPKY4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQCBRZ1oyH2z1socJcK6lfVkyfXHVU%2BSd7Cdky4F9SpQHwIgWPptg%2BeLZREEP2EMYOgGZW6RS%2Bh8jgDBnjaIDsnBessqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK1hcmqmCmJnn4NV3SrcA8D%2BilpubEt11qbK3nFPl20UNyAbWjwZE5PxSs%2FUMjT5Sp3FI%2BAX3fn8YnyTrEXIkFZ8yUH8irsn3mFNHgqHTn%2BPnbYEvRdT9%2BkveQIohG7TSdgR3jhBTYm2%2FzbqU%2BWj4DQ7J0KhoL%2F4N2EKIHW5Wujb%2FhwEk79h6a461HEa7G4lzX2JAvpNTbWzxlMSlkwnziAbYXAQ%2FfJjpx0NQaMo30jB2fIolAyVqVFpTRHn3mU24wWJGJMq2Jt09ol6jZBVHrk8J23UUP78ZrSgtvgUERvzD2SxMisSv3Ztia8PIsl4lQB%2FIyFV%2Bib%2BfTUUCJ4WsXc3Z%2BOUQ3tudqWfGkUQTfvbvXCWTqwsjXzud2O8sCcg1ewqe4Ryg6VTdvkYFyaXh3394eTFIk3NP7wnWYyXhygQoKRgiK2tXpHBkd9HS0YTQznscmA%2FiCceFTYBY5diPQsU0XL%2F%2FJrmfiASzRCdhv0ECitqHzmJ70zLgPVZ1gTS1DWDZtxZtCZt%2FkJtwO58LzJu8tDpQw12zAtxSJDZ3G%2B7dliFP8adSdXe4wpsITFmBt9xYxa0CIB4qpzoO3Um28J6mXkv8pIqE0ShEbuRaT0moeuQS2UNung9eJOAOrBYjd64j11tTNEukcawMJXUm70GOqUBBptYPlimXK168ZzIamnhqskegrqVU1aguXdnU1xCRCct7m%2BUgiVQCGIlAYetvHG2Be1w71J0Ff1fWKx0WtD%2F5zr5Lpk54KnzUYBNlkzLvNDwMG4tZ1lEFknXR4q3O3DXLLjgv6F%2BLHEo4MSNjpXxSKoWy7REWJIlxiwT13PMCKMyozj3%2F3%2F5H%2FXT25shfgANDEB%2BeWqehBzBpktO2LXEOKfQrpLA&X-Amz-Signature=f5cfb1d77cd23f50aa239772115690b123dc5b12328a7945cd561aaab22c595e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGF2IMU2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQCWOGEYoNHhCIEVlSMShv8CshUmmCKmSroUYD67FQTaOQIhAJqQ2dpU30UKJlLXNIY7YqQFIsrahIwjGEwd7uT7vqnLKogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb37TH4Lk95QsDLg4q3AMds52SqQuN7e5slt%2BIiIx86sbj0CWHCg8mlq%2BaVSHzobJsrdThWvlehz9lwxP5k1vzBlXxqXDRuJbDNPGBIl6IynGdeF5l2kSQeUiMaqxs93Xb21rEpFqoIGBFTMuuu9GInqguNWe7Ox410HgkLUYIdJCfARlidqcHXZSa4ndr0P4DzdTKCisNWqt7%2FPUl%2BDxUcIv3EOMgebNiAB7R%2Bxh9e%2Fp6OsXUp2PTdDa2KtMQn4Bc3VzJ2TPgBvU8jubZHBamwAt9ZjTfGKGH6Di6A%2Fleqgl3mWtRRt2m5S3QZCSgd58m4rJzeto1w8iw38j5C1uFlpcvofCFwEdg5R5x5e9X7DFAct47CKJU%2BKyRzmheQmtKgOwPlgw1sg8FHCt3b9emDQ8i2QnzDzxR9q%2BQxq4YNaTTDNLbLT5ZJnFoW1HPGBghv%2FNgxZTUXpmbtrxGE%2BhR9%2B%2B9V0p6%2FXMI6IqQkYPu%2FGU%2FaxNGJKJmp4JNipBIGLI44blraTkWjaua6VqobZHv7Ryb%2Bo1%2FhwKq7ligaqmOyd4A6ZUCSBsFQ55TzHR%2Fwqm6CzNLq979ETZ1dViF0D%2BDxcR28QQMHqzgW7jj7SmXComxDN%2FGV8MW7UHt8tF8IHPuUZ5uCVpeyD4ahDC11Ju9BjqkARRSQIChRi6CPBavAvc9dGOD3EUEe900fARw6ayqAstq02KyKOmFNFXvF%2F%2BTRgj0l6zl%2Bvbw7f9yg7j1xFXhiuj%2B3IDfe0CZk9CqkPlX2quaZkngADrdQBEH%2B%2FgpX8sVIDLFBIrQcTtWMCCxXB9pT6%2B%2FXiFmFNaOqBzrEBxITXM%2BfcLJYGRnJ%2Byq5jqRKAOX%2BcTfFsLggpMmMQzKmBZX%2Bban8EJ2&X-Amz-Signature=26b8dbfa06b146e7960dd11a1051b6b6081bbe7ba2e47fae8af3080bf6cd7557&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OUTA6AV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIAx6xB0qYmNHUt0LymRB6d7acoDo8NlzBLuII9%2BxW5Q1AiEA%2FtB1PE8G3E79tHnB7RtYxIijsgApFUKk7TBpy%2F3ge4EqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbZo8xQAcgHzGkYlircAwaULqnYKMHDxokQza7YV90k63TAd9533ojcNS9NchbyLmvulQ%2BxsvJcr9dGVv1nTM49OyVMIAQhJrhOpbuwjA4fNNeUb2S6U0em8d0l6oDTjJiR5UlUAjfVYmyHkEirwAUdNtSoOnXtBpHosvRJsbMktwSb7uSca6GzeEfuy2DUchrUiGwVRprZudjgPeyfa69v9cntT%2FkUEZTYNO%2BhnfFjPnGyTuXAG%2Bl4Lhew0X%2FntAEH%2BCk%2F8OrVRhexH2vkQMAzBB2MgLrjmb%2Bb5maXjwPhUxfQeWWb64iOQ%2FW9TAuzEs%2B2T2vTA2G4QEotXsGYrf2ZMD9V7CPxrP%2BU1riD4OK5FhUrFH8iCBHmsmMl45bOArRJ%2FKd%2BvPmIekceJtbqyWSe1AAIDC1YOiWiQr0ZO%2BWuxGTPEWl8aH0oa9y4wq%2B7Tqg21M6ul0MouMolL3hPhNcNFHR7mxfjzc9cBDnnHWC7ieE8hm08T7kLcvtiJwj2Mv88ozWq6qhaYug%2BHPL7QS6KxpYUjcaZjCpfjFfGepVS8lFvyoBE9T99TlHo5DbW%2BM9D4fmLz9BQerN%2FTusB9CVJ4rE360dq5XjFKr9UYw1sLvk%2F4%2BRiIIA2HmNhAQECXCI2QxZZYIzQU2sZMOLUm70GOqUByHMSK%2BTp7k5PsC1DUlj%2BldzBMWmMiLzIaDPpbwW8mAdfWRAXhxmhqdU%2BB4asornyEPVfrpq87%2FF5u7Ic%2FTxpQ7mfuBcZUFbE4hIdxGd8B4cjPBTV3y4s%2FbMRQ0u3EYrAnJAozcE3BwoDNY8Y3eiM%2FeY%2Bdt0TOdXmmHIDrz3TC9ZQNPeXprNnUJgiHfPFwgajIrOP%2Ff%2BpWXrnVUEA4cqQ5vWu5V8D&X-Amz-Signature=4d8e34dee11adbabdd9cc123ef333418aa0c1dfd20bfbe04dc862df3ea758661&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW45Q3LQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQDbXtIRUYz5zPFAcau4VVHeP%2FY4fpE5sb6TkzjlI6UgdgIhAIkSb1LqWWQBcDEhEPVVxpHzRriVT18PXBTLPdM15DIDKogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxlyeLeI4WQrMuMPAQq3ANG%2BhYZkVZ54JiNL2N1gZ37IcmOoCq6lFrSTULZ0MIvjb1RkmQ45HzYWj34wIbECDj9z91oXsbY0hFpD2m8Vu0WKGXydphx6C2huSgFf9KF9Ljm0VEhWDBTAkBpdZJyCJS%2BLol%2BIhMY%2B2%2BUrj13WrlXOC2LfBIMIdEte3X%2BwkasPoHXo4zID0WizOnNEmj6oWlni6aPVMrhZaQXXVv3Hl7E56sJH4br0FAi%2FqM1jy8s1TGD%2BsMA4u99UqPlmbs6XkRhn2E1NQ8mNlonRIx%2F0JN5j%2FL1RVN5wVNJnagUIlr0BNeA1d88OB5cuTR%2FoEWdT1xORzIC9REveoRBGORQzivqcZWXqZAHXxn0KL%2BokFot3kieTJhOx3uzmqAfUlK8AAVPJHa3PUinLcIOUOmUac7%2BgnI1Ya0YKHkndXs3Fl%2BHlIK4lfmnHr3JrKnRcjUY6q4trvgwm1%2F9oQs7LrrX0Chg%2FWX0P5d7vi1faMDibiPqPpME6krudVd7%2Bt9HRTgMFICo%2BeRUplwuBmhd7kQrltfrDdPHyWg0vlqODFGBF27nnrvx7Wp40%2FoUEw47QMEq7yU8doC71bmjVASW7SDuYo3cBcko8l7j5hlXZxLM5%2BuhkmnyjJPHT2QKjCpsVTC%2B1Ju9BjqkAVIFb4TgdaH9E%2FlhEI4l5xxFI7VVnrNpRAort1HJMfiVZAmv7b450WJWZFgM5X92%2FoSo8EdBJx9%2BVs6lw6ZBMvT9kULnKLTKB3NgJweeG%2B0lrTrJuy7pl%2FZ6lDgRcV3wO0QoiFTEm3GVUQZ6GjMNwEIc3DSIbsiS0YjFHOU4bEPzJkU2giGMPrx8mun9eTSHGRXivcRM3MUB63K6KEbGMhN60Q5y&X-Amz-Signature=1aa5dff8bcd582d0f914ebc09063869605fcefd83bff31861b89a1cc21db9d29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624QPPKY4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQCBRZ1oyH2z1socJcK6lfVkyfXHVU%2BSd7Cdky4F9SpQHwIgWPptg%2BeLZREEP2EMYOgGZW6RS%2Bh8jgDBnjaIDsnBessqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK1hcmqmCmJnn4NV3SrcA8D%2BilpubEt11qbK3nFPl20UNyAbWjwZE5PxSs%2FUMjT5Sp3FI%2BAX3fn8YnyTrEXIkFZ8yUH8irsn3mFNHgqHTn%2BPnbYEvRdT9%2BkveQIohG7TSdgR3jhBTYm2%2FzbqU%2BWj4DQ7J0KhoL%2F4N2EKIHW5Wujb%2FhwEk79h6a461HEa7G4lzX2JAvpNTbWzxlMSlkwnziAbYXAQ%2FfJjpx0NQaMo30jB2fIolAyVqVFpTRHn3mU24wWJGJMq2Jt09ol6jZBVHrk8J23UUP78ZrSgtvgUERvzD2SxMisSv3Ztia8PIsl4lQB%2FIyFV%2Bib%2BfTUUCJ4WsXc3Z%2BOUQ3tudqWfGkUQTfvbvXCWTqwsjXzud2O8sCcg1ewqe4Ryg6VTdvkYFyaXh3394eTFIk3NP7wnWYyXhygQoKRgiK2tXpHBkd9HS0YTQznscmA%2FiCceFTYBY5diPQsU0XL%2F%2FJrmfiASzRCdhv0ECitqHzmJ70zLgPVZ1gTS1DWDZtxZtCZt%2FkJtwO58LzJu8tDpQw12zAtxSJDZ3G%2B7dliFP8adSdXe4wpsITFmBt9xYxa0CIB4qpzoO3Um28J6mXkv8pIqE0ShEbuRaT0moeuQS2UNung9eJOAOrBYjd64j11tTNEukcawMJXUm70GOqUBBptYPlimXK168ZzIamnhqskegrqVU1aguXdnU1xCRCct7m%2BUgiVQCGIlAYetvHG2Be1w71J0Ff1fWKx0WtD%2F5zr5Lpk54KnzUYBNlkzLvNDwMG4tZ1lEFknXR4q3O3DXLLjgv6F%2BLHEo4MSNjpXxSKoWy7REWJIlxiwT13PMCKMyozj3%2F3%2F5H%2FXT25shfgANDEB%2BeWqehBzBpktO2LXEOKfQrpLA&X-Amz-Signature=7b951200349c49264695329bf93c2d029884970f5ef05d403c8ecd6b62c27eb0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TE6Q6E6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIQCtYC7y2VRnHk0Da9jpEoQDwxvfwuJfMJ1CrqyiuPwcVwIfJmkAdAKAS8iw%2B%2FgkZfxNEcsn48Ymu4UYnaCYPn8WUSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV6vVGYEhdJumAvCgKtwDBP9qh%2FFIzVRijNT4nUvYKUnfqsMeEzy6ipKb3o%2FqZnTAz6ejxMlP0PDoonJNqb2Sv3KpSlVmb222M7CioeffQ%2BTOjNkrKvfbVlWaSkbQaBJY3qzTNvZk7YArMw%2FxBX3odMY02%2B33sLuFeLDAxBirjcHYgurmIjXkWdOzOgdF4YJp0t6v3EFGqdNgSP6XYBcTSHckd1TEfvNFN%2FIl2wRQIk0XqJ037tSSJe96%2Bsxd77qLL7PYNMKq0QDYkT%2FVgrmaOs2Mlrl99uyln%2FKMPzRnX1NI%2BoIlOUwkj1VSq5or4USOqUZC%2F3i94ZN0UXSILDHdA5WbCKxwAnm%2FcYcICEJG93UYz6PaOje7WH2sEAD3Bjio%2BKohejyFrsRtxHUzUTHsqWbv1xVoOuSemTgBST2Yw3myhaZMcV5G89hVR8WDM9Et7Jr9l21X6FLHDXJdOXZAGI9nkPOJNY94Qs5ak2CsFUtFP6R07vdMgAeC7KtBrIpsXOfBntBCJMtfkQU0sMrLCGQW4TAFEIqGc%2FljW5Uetp%2BZ8Rl5l5skIYBVNrX3UYT9a0%2BvJyzfFhyLmGO2mORYBgeOwbvtBbymXk0HiwrhNrf19z7hVQoNAep5GMZayQQ48nXgWzZZbhYJkgMwvtSbvQY6pgEV0VQiXoI1PVtc8ohpYOG2d%2BwwGnsWvJpVDn7QlN%2FigGqCCaMRwUyU1hXPv4jprRy6yBQZ5c14FQnswb8gnEPlvTakQDMw0Lq6pQ76yRZfdjoC6SJx7HeOcF08D6Uutb6p38CxTMA0U2%2BHZ%2Fq5xaRfcOPXE2%2F9x0RRmKngEpJbPcAy37w7Fh7fugbJHn2oWaYmt7voy6lmDvJDTcUARZ3QvIr7UU2A&X-Amz-Signature=a791d14ecac54648842969705769c15eb0eb078aea6187cd0d40eb8138e0651d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TE6Q6E6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIQCtYC7y2VRnHk0Da9jpEoQDwxvfwuJfMJ1CrqyiuPwcVwIfJmkAdAKAS8iw%2B%2FgkZfxNEcsn48Ymu4UYnaCYPn8WUSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV6vVGYEhdJumAvCgKtwDBP9qh%2FFIzVRijNT4nUvYKUnfqsMeEzy6ipKb3o%2FqZnTAz6ejxMlP0PDoonJNqb2Sv3KpSlVmb222M7CioeffQ%2BTOjNkrKvfbVlWaSkbQaBJY3qzTNvZk7YArMw%2FxBX3odMY02%2B33sLuFeLDAxBirjcHYgurmIjXkWdOzOgdF4YJp0t6v3EFGqdNgSP6XYBcTSHckd1TEfvNFN%2FIl2wRQIk0XqJ037tSSJe96%2Bsxd77qLL7PYNMKq0QDYkT%2FVgrmaOs2Mlrl99uyln%2FKMPzRnX1NI%2BoIlOUwkj1VSq5or4USOqUZC%2F3i94ZN0UXSILDHdA5WbCKxwAnm%2FcYcICEJG93UYz6PaOje7WH2sEAD3Bjio%2BKohejyFrsRtxHUzUTHsqWbv1xVoOuSemTgBST2Yw3myhaZMcV5G89hVR8WDM9Et7Jr9l21X6FLHDXJdOXZAGI9nkPOJNY94Qs5ak2CsFUtFP6R07vdMgAeC7KtBrIpsXOfBntBCJMtfkQU0sMrLCGQW4TAFEIqGc%2FljW5Uetp%2BZ8Rl5l5skIYBVNrX3UYT9a0%2BvJyzfFhyLmGO2mORYBgeOwbvtBbymXk0HiwrhNrf19z7hVQoNAep5GMZayQQ48nXgWzZZbhYJkgMwvtSbvQY6pgEV0VQiXoI1PVtc8ohpYOG2d%2BwwGnsWvJpVDn7QlN%2FigGqCCaMRwUyU1hXPv4jprRy6yBQZ5c14FQnswb8gnEPlvTakQDMw0Lq6pQ76yRZfdjoC6SJx7HeOcF08D6Uutb6p38CxTMA0U2%2BHZ%2Fq5xaRfcOPXE2%2F9x0RRmKngEpJbPcAy37w7Fh7fugbJHn2oWaYmt7voy6lmDvJDTcUARZ3QvIr7UU2A&X-Amz-Signature=56611f9dba1128a353d78ead0ce1e2b503228846c0c0c92da3c69521f9277e5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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