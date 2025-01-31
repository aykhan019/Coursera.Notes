

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SZGRRG2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDfy%2Br1ABkF9%2FGGjR%2B8UIK8YnOpS87gYoXg8Tafz16lgIgQIZcq7TmEfQJLbjNMcv%2BCr4FB5xeccrmoNqKK7A3968qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFjEc%2Fl%2BMg%2FJOK9GircAzEEBsNR31a5GN8sh1VK3X5btIDne26UaQe1J2NftzUVrCOM%2BGaxX4L2JdIg4DtCabr%2FQOKZ9P0asQm46Pz52Vu3v6HlwPa%2B08alnPLpsQD2%2FGa8uLuS0mR8A%2Fxp6098x2nBdjgmMgp6ZUgXL3hfMSXPnQzENj3C400VzOMTuiqCX7Y235Epcfnvg3qYA9F4qQlN1CULmxU7W7ipenbGx9A2IRMVF5mJCxaN2skjvMZORqK50vwo2jQEnO%2BemT%2FMjmrHOeHVZpp%2BVDBDR7sXIlBexOHp8q4ZYk0U1ryFcTzwAaRhO24hjQF2opr6mlqFUBsvUPfti%2BvRkUlTDSAYK7k9m6vT029o3hOeRPpEjJUAHrBlgDANqW3sbUpIOtJ5oTq2GkiBR6Oe5VsMMHl7RtW219BkFS%2FVpXGgZ0WiwNs5ykgD5EaVlHV0vIdDrikEFVs70TXdnU2IRuiuH5%2FQUxPe%2B3LWjChv8eechBF%2F6LjS%2Fl4lb2oaKXd2b%2BAIdSuNU46XVU%2FYVR%2Bn2aaatZdubE7E%2Bh5KfafMIxPbpGuTpK%2BH6MDgC3PtSS7qbiy1Z965Rbl4KMv4Hl871h76p5xBapRlvnvNxLMIBB%2BskiZAH%2FnzSnz0j21Pqaf1NPcNMJXI87wGOqUBYFUr1tXzX3OrzOaExZmeqzDjiQjySjugh%2FSzfuw%2Ff0FI0wU0j0HgrSbwQ6UWf%2BMteMqNrFvxaV8T0xSfmKR%2FV6P6QbiSO1SETk3Oeiegbn0MNBr1DXC4Su14c%2B8KeQm%2B4kUqPlqBtqTvA%2F%2BOKm%2FmdUI%2B4EzwID64uTWSgeumH4UUYRfV47Tit4WKnOOdcRODaiWKWS6sqFq0yMYBqp8sheHrYDSN&X-Amz-Signature=cb4aab23c1fa80697efe6ef326c702acb4052a3a43361ff91217a01d90a8115d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYRM5OJA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlPkFSnvOieQ3na7DHA9nBOPps58oOOS1UgTfIKCin0AiEA5duP17mHBxPmDHF0XmfoaBlWXixHCCobieHUOCZcVqcqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKYYlN8QGF%2Fwn2guSCrcA6r%2BXIzH1jcH%2BWym8pxbXhNrVC5iM5xWagmI0TsS1mlsZTwDD5Xg2GnM4tIpQh%2Fli8Qp390ATVyAdZyzeFyJRkTdsK5fNDU0xpEPtbEVkBr%2BEQhba5r%2F1TGmNp5SVg%2BmBSFuMWgB0VUNSDiEkCcS4Tvn9K0gMWH2UAquAt5lybQmxfRIE%2FSk%2BXe5Gllro9SnxXLw7x3J%2FGiJs7EERiB26cYJ8fcZ3F95jLdtASK0JHpPRzqzPC1R1LNi05bpRtBNsWMsMR1au8sdNqmqHokfv3ejUuJ8idcNME9ziDs57xXycQDL21yYkae5bLWgCgLD4LJMRq4rWSOShqBTAr8jpeZqQTEc%2B8HL%2B3H%2B8VLTmclWJvZTk2Dvel8xre2tZpsUuIF6b1bHB69YJHcV1iXgDJpBWqOxzRZ%2BpbEmy9xdWBypwHy373bggeZG1vt1OaQ%2FkTV9er20kv5VUZgBM8baDanoZcYkQW4WrlN9qxTMSO6%2Bgw%2BFAHaKcxB9fQFBHjt5S5VMa8%2FEGoRfQGKCe0HvfAoW8wNE4c6NXWxoXacksKzTf5K0uT0l62nurAdiRhim%2FGpGWZ3q6crRBMrIryd7rO6wIcJuyPjPc%2BKGUU2Ui%2FnuZYtICaA9ZG5iMmqDMKTI87wGOqUBCUJqzXVWyiOy8H7wfiqn7fEob4A2ELUDru%2BJ2vxaaxgx7lJQHPwq3NZLayo94U9FnxlpskIf8UNoPETxZLOqFz3dY3XkHG0b5n515YBre6Ttl9aYB1xS3YfDme%2FbCQiraE2%2BFx62qg9ypARkDf3xoGigIv8yKHN1TIoFB0mADNUxb5Gcdk%2FCpE%2Fzin%2FxyH7mKyk27N9g7Xguno0OCM7yulKNVzVr&X-Amz-Signature=0771ac2863801c19ec09ec870d2dc02a83a28fae88e15c37dabe3cef59706610&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGXSKUH6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT%2B9j1Ot4HWqNZdiX%2FGL8mkLOYQQB%2FQXbY%2B3PUB00tvwIhAMuJcXrorKNJKSLQmIIaUCSP7%2FlWVyJwL95Nf6rcalLyKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJUC%2FNuiN56JyQoDcq3AOCa8dMWbzBNmQbnvkDgfBc6hZdQaMcx0RbfBu1ARnnHYengWIcH0%2BErcMYmMVjgqD0SOQL35sW8hdkyhBhDgkdDT4Yn9YqhS0zoUCquBpjDznMjX%2BYcVMevwLqbyplPxeQwbSYHVbFVTAV%2BLFxaCyjcivB9vtrhGr3jQWLNzZAhaZ5SorEoeCka5Abqgf6DYLraZO%2FZsKy7NY6yY6tUk%2BNCk%2BFyXsK%2FPbSTEZA0R3LPZP%2FKrSmRwFJ7w%2BaRC2CIAWATcX6zAYSy6qdJgf%2FWmVh6NyFiwu6%2FvUdRoJ7bhy69MCpWZ4VXslVEnKq41oWHQ0C1QWMoeYUJ3z6jKXG3lvi1VamfwpUPUao8Bt4HUWoOoTqGNoQtA1b4GvLjvFLzW7A6BOY%2B1jT%2BKpdg8kfjYnNYjCyTvdBlxEYRBcS3BRtRMShbwTkOwxdnQbhlvuYODj7YxojuQxsxVGhtnNww4uhP0%2Fb7jVoUiD%2FddfQlXDMbG%2FyApneGbZ4ilYQ08gMfIvS2y5k3933EHjvFnKLGD%2FtttKN7xA%2Bsa1WZ%2FEC7BL9cadFk1RGtjN7xuqfpO9rnw%2FU42AKYCuKoTvYsnWqtl1GiSGWLC9ySPVMTDucOof50qHSOsFujpDJnck0nTDIyPO8BjqkAZTe0zvBEZE%2BXWF6AcIIz7Cg1UdyLX1OrmjuDxn%2F8HsWUmKk5iz%2Fqh704ozdWac1uoiMEDMXviUtibAYNc8jyZ4E3aIVCGDMvK4wtXn0w%2FLhC04pdQNxfagv8IzRROuxmIc2xwHPNpOYpnLwX4pW1qMuEG4LHfa33GQezm1khge6kMmrHaAr3udnC1BPemR9p1a8aGkzZO1deaW%2Bkn63uMhv%2BmGi&X-Amz-Signature=82c8b830e2c5a92a83bd6ac85d42a578ea57c238800560db6884079c8a207996&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXVBI5B7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFVe%2BXldvcIpFqnOmwGT37gBdh6943ShqBgM4nCmuknzAiEA2C6Wl0myMSNL%2FKyl0HyHbMpkW5sVdTNFi2%2FdynCXKfwqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIN2AQBb27I32p8h%2ByrcA6xvJnQRRsp38dK14sWE1U3rtxGEf%2For9sa72n%2BDxVvrmSd8RgGJ67dWUaUNPjapyr3z5Gk4UDYZAiNYEhyn65kHKc5ZKB%2BkKDVp7te7FnCFsOYYsEGlb0ovF%2BolwC6LPQDqssMJoYmR8BTk0V8BoNMPOL7e1fvSPSfmtln6J5rRCOmOSzH%2By6Gl%2FyscW%2B6oQcZ6Ei5pCtgBInbf9pC1Vw%2BL%2ByqLzV4ZFKdjWIZ5ii%2FiMQhRxqEEeoRbHYy0IVE4SSdb7KvDLNW3XwPN%2FPdBLEyfhmOSdpzT2TaPK%2F7A2rC5sB8xpOToNCItdR5HPLiajnrZxxdM7AFYfutJ7m2kWa3YyG71vSoqQZX1ZeiQf7ORmFDjscm5BAtMDKdqlDXf7%2Fljg%2FqhncyYbsIcBJ5%2BILRGHUxb%2BqLEMAQNkREmTdKSxu%2BaBnglsScNeFT0Wxj42srO3U%2FAXw8%2BGsUpQbU62QYv01lCZfq%2BBm6dZoxZH16t3TNyjuZv3D5owROsVQBDYZnwA76DxY%2F%2BbsJ2iA5xQAgG8vDZvFmFGtOzQdh9DQIjtJWF1yB4JS5KMBrPsOuaUGI9jt0SJvBAYn0b6Hvfo1yrFrxokxZPjITg24AjhHgE2iCsSKLFX5FSf0GnMJzI87wGOqUBfeC1x9hoC3FJ1V0rq6NJH9xHyMDR44zJkq%2BfO7cogoJndxRd12E5CG%2FAEFN%2B0IZNO1%2BYdJ4RDWftLt3W5IcM9PLxqdmPYEhCi2OuEKPyysXH7moE7HTzfxK1D6rVXVXhY2yXcYDTPNDfub%2BGHbjVqij8soIZd3vQuLNYNcZGhYN%2BGw702WF5pWwAKS9TFrgwuNAE3E15WKxmOkt8ZgCB7lug%2BuW3&X-Amz-Signature=ba69e30adaed3ba26836044b9fbb44a5a42d2a1640a69e32290667e9463ac608&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UJKVSK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTjnch3Mh2pEGGXypOaxdrD9KNAnoUyGeSFlJvwKbILgIgKogVNYVz98ObSg9NLYzhrGG8STojuiBsrGavvpYS0EYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJO836D4U9lYdgbuNircA6SIBr53b%2BWCCxY%2FUBCNttds8X3eXApWIzQAZuWp56F%2FMiQPIx6lC2l2PYFYpl09afMb4nsjbs%2FFhPdK26TKKXXwm7WutAZivqXCye9GIjVIpy%2BqPzK6dxr%2BZVFV2vJ0K%2Fs1qek22tK5wkTgg9%2FMsIWZ9XdpInRZdI3dYsqsnfzLGuMcNTdg4bPZsIweUhHqbxU5T10omT%2BAGWq9XmobulXZwsIJIwZJr7fo44uXcrE%2FCIboeCWlrFy%2B2pTTYR2UG8rbhZ0q72qquZ7k37drZIdOq8zHaA%2FiH4fjuF7JQQhof8SsHXbeGgugUzfUEgGZ71qtmZFhlRkHX7XiVEbw2dtlB1P9rhljDqZARvmZe0PqAmmsmz7A%2BhN%2BZt8ya38ORdidhfmDiiMzOIRElzRvBJPbomiOB4oUdRZsAIUszg%2FiWO0hTA8iAlCoTHRdhNMwRpkhxfmdr8zqsvOoOnWJpv2KLTUqSTBqgr1P14xu74scIqFbh9My1qELSxRJa3uhCCTuxUtWOmTTJE8XIVk9BiJwacCK19bAP6xtI3t4mJaTByaWBb15bUr1JpHudIDcKxxqtAU7DFteU%2BD3uygQMMg6ExbjfkffiC6yoFWo1Tz%2FbRymtBORQbZlilw9MLrI87wGOqUBrPwCxAuak55zzA7NgnXGEI1vp5vOF%2FE6C7GGakSkMm3A7Nch5bZloXODMO%2FdHacD14rgLnLyBp0WhIvfhcufxf3jyhIbJNuT2eJ%2FQYR%2BJmrjJTL36fq5jo0pkK%2FhSHcyQsrpetYZ%2BE%2BW8biS3lECGV1vNv92gIkA7Du1L9pjw575I0E0sxlZwGCH%2B0P8gV7wkbRFwz46F8VtKDIKhjarRjke4RkE&X-Amz-Signature=5dc520cba7519e4efd3c64bed266cc7746742a42336f3703dd48b7d75efe2991&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSTKAUZ4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3eJZc%2BzRHokLpvkJSrsHqfsj8lhAh7qojH0OoeVBd2AiEAuTnON%2FCYjtZ3WFzATS7nulPLcvghFrj7WtUBiBR6QesqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHaD84hzVE3vUnW7tircA8BJ1PDYm436EG8%2BfXnUCcgCFrOvY8GE5%2BlpVH53xQT8PviyaEYyVY7yj%2BhrR5Hw8ChnOVWfPr2E3o3jRoPZ6CsY0mcYnKMwuPcyQu2rzDnfys%2B%2FQY1qPm6s5lKVVa89vRkVdaT7XJMTJWa4f%2BSO4E9ibns%2Br1eSEJCeKrNfAmSsaB69dtwEKJ1Mfqmj8OO4kJqE3SmovU2v4It1Pto41qL7elCkaSfg3eD2HZixmkcbUSo6GFW58N5QbexJRhXoCGeCgBQraAr6ZCtcA0WWw15dVkXiq1oTl5py7wyplUrj%2FnuTdT5pWdwSU3zEoK81f4tKKMqDoDGKI%2BqxfgsPA8xe5p%2FxJrMI6qSGy7lRdjcuKylZCi7WtzMMJ0Sc2wDI3Dh9oJhST84ffeTb6IVWetoP4xuOZvr0L%2BG2AoFmiX3oY%2Fy%2BafgA%2FlMV9SK7Jewc4fB%2BdBn1bA1nKiHlOYBPnYrGZTHz2f80Cl3og0dqQYpDmeO%2FlHpLhQqkmXW3CvI3LFLNu63svbZ2TuQwHMnP67kPuo4q9SIS28rS6kyZWxVV1ap6SUkR9QISSw4oqe9N%2Fe8VxzUo0Jp89Fiubd7UNpk6vpiS5p6qjoexuEjzZBfggFovis7MvlLr9iaNMNDI87wGOqUB777t2dy9PXRy9Y12D3vAqS4oiWBXC%2FAV4hkm0nYbnaJK0QaHJlKfwfwD4FbvAomJLdveqjxhcZS4w8QP5n%2Fu8NletJ4mPD7A0KhFiXAGBJt%2BZjFr%2B85xWbRtL7q2Hb%2BJQFe8kfaJnzVKQx76lo3ataSMvD7irDtF5%2FJ0bYxSGlusOqCfCihY5ts1LTiTgoeUy%2FcWSlF9p3Zy87JdZJ5%2FyN%2FsXWhu&X-Amz-Signature=126c6d6adc803adb9269cc40eae3e1ae1f2283b1ff33067a0f143a562192e75b&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QC5IRW63%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGoljFq%2BOoqde95Z1tMIC6cqFdBA8Y8bS0I8WviTkviJAiEAiExWjukrAPQHu0m491DFvLaM8PdAkaQj0feT7mbjxWQqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDByXS9lIRveaQJFwmircA5S%2F9RWWW8KdBs5mpeKZygK1gz0MM%2BDiATFJhui%2F1qnSO6bYgWrgrh1FbTcBbAWjsa2qsk8KdF3zkuW5sH9352c2o02cX8azHi3r3C7MgKJQY%2BsnCOQLqamVaUI63aYQ5NUTxZiT%2BuuaOeVhabFbTkT4zQBsuj61JZQfvv3iEtxOJW6UD2hf3GnzrqHCpnu4PWTRc5oKukKhpLvXP6E98%2ByeF40UNmTB6dZfEk4DZRg%2BzsWlJAow1XYBy3pWrzklW2SFmBeQlU0tfH1YFVeiYHypsa%2FRptVSL5kiHKEN28Mx1SbdlWvogm0NmRL6aVt554shT7fo8HFlI0WdsD3kNbgcRjAL2U14e4%2FJuDhmbn9GXrHJM2idZ13165C5%2BF4rJ74lRnsnTsCOf8OecTx8961JNh%2Fz5zxG6fkG7MjJ2Y%2B9JmJdE%2Bd4NoCk7pAifA9O0doD4eQNpXqx%2BALHPqJlI7rhqlHbyU7ncTZ%2FcSbWhAy1m4bKMhTS8OsQlBLTJAvylsKguP5cVkJ5het5%2BrcLOkWO8Pdd8roM7szqfQ6PeIem6GmKBjim03ik87vVXnpUiRPqhPcv4TpR2%2FiTZurgO%2BAMheeAcMgt%2BwHB%2B3s1kK1sYMV8aXsUuOq9%2Fsl9MJDI87wGOqUB4WNpU8x%2FsZtv048TDS00VnJ4CW6rTLgspiwORsFczP3lMVabO1eZg5ltaT7tBCJ0Lk3zhGmFC5kkAgSq%2Bdp%2BufI%2Fe%2FCPtK6rZlcuqj8M%2BL3xPezqSgjNnYFDwR4%2Ffjd3Tx79g0dybiawTuxDPFzdnJWhfA2OgxnOLyG%2Ffp7EsGFmVxjMsy8YLlTkGm5L9PFlfC7CwzUN14ML9RAIEwBe1LYlWpAg&X-Amz-Signature=a4b585f99c9d79e046e00b0e0eccf906df1ea5f36213551972967ebe9f75abfa&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N7K7OWO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgi%2BQLYXRFDjjc1lnXYcHF%2FPmJ%2B%2FOdOeTw4iSWFs35VAiEAm%2BhMqZ%2BhOHCmJyESJiFcA4MSzOf5ozLsyaI88hclPRoqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMg3OHABxmZ0Kn0%2BlyrcA%2FKONadBHvsi1iPCQOA5aDW48M7qEj9EDqsY4c9ulnQRmEYq33FprxwACJ5dNvsFMjvNnA4MEqfEPPUON1qIENHWKJs7v3NyegEDGn3b9uov2kfWMwCV9O9nNOKMC2%2FSb58yO76N62SR1EJWO6mWSaCeJfwJZYxRiHFLlhaXhtqeJIfSC5VcWZsd1AJ2lEdyDPRIU%2FrohrAlamBLaBVlcFBAjCeUC7UiY2qa0QrieYQjbvnG5WcyENlsqwOnaf7rZWEmTfdXwjMdCQFHO8xX8SO8T%2Fr9HK21gdkoqhO90W0VjRzgafvw2TsfUrgzpBKp%2BvZXCaIENPhXkTxEupQnAzmD%2FmLYF5OGS2VqwNU6nyiN3ckbXOzqzV7HZKhX945C16RSCKBDohcbmvkK3A261%2BnScKLQ%2FGbgTvASWYRv3jI3jJVb8bqwZw1x6Sy39I7ZtO4dwB2d7P7W%2BSlGCGF7bXb%2F38M4jhrJx8%2B4l0rB8l5QgTvaJ5dPgz2KIT81r%2BOuAxzL5QnXQ5NX76ZedtfKAXhyQBQHUx1KxOAlsTNR0qDuiH%2BDj22kTtu%2FyMEibEkWfn1JkUN80lf%2FOCyFzVR2YzevsofjfN0%2B1wcsVWcYa9YTj736YicHALLKBQ9tMLDI87wGOqUBLBGfLTfuRI56FKBn8N7KaXNVgmoFiV9K%2Ft4VAdYnnXftynglndDfcatURBv2zxeojRwwzGd7jEvH3VuQ9wXyep6E41uhU9BP9nstkqpChCitJl93q4nkVg5iMIHphFL1XMfjh%2FsBwQVaOS%2F69%2F%2F3MNUyPJl9%2BQm9%2BVZq6Bs%2FARupJ3CXZVuRFQUKwN%2Bc4RA9bgV82OlkPmPrw4pZdQc6O3vMGz5g&X-Amz-Signature=a5606af773ed416c0768c8c32f667a79773913d73440934369cd4dd44e29e02b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UJKVSK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTjnch3Mh2pEGGXypOaxdrD9KNAnoUyGeSFlJvwKbILgIgKogVNYVz98ObSg9NLYzhrGG8STojuiBsrGavvpYS0EYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJO836D4U9lYdgbuNircA6SIBr53b%2BWCCxY%2FUBCNttds8X3eXApWIzQAZuWp56F%2FMiQPIx6lC2l2PYFYpl09afMb4nsjbs%2FFhPdK26TKKXXwm7WutAZivqXCye9GIjVIpy%2BqPzK6dxr%2BZVFV2vJ0K%2Fs1qek22tK5wkTgg9%2FMsIWZ9XdpInRZdI3dYsqsnfzLGuMcNTdg4bPZsIweUhHqbxU5T10omT%2BAGWq9XmobulXZwsIJIwZJr7fo44uXcrE%2FCIboeCWlrFy%2B2pTTYR2UG8rbhZ0q72qquZ7k37drZIdOq8zHaA%2FiH4fjuF7JQQhof8SsHXbeGgugUzfUEgGZ71qtmZFhlRkHX7XiVEbw2dtlB1P9rhljDqZARvmZe0PqAmmsmz7A%2BhN%2BZt8ya38ORdidhfmDiiMzOIRElzRvBJPbomiOB4oUdRZsAIUszg%2FiWO0hTA8iAlCoTHRdhNMwRpkhxfmdr8zqsvOoOnWJpv2KLTUqSTBqgr1P14xu74scIqFbh9My1qELSxRJa3uhCCTuxUtWOmTTJE8XIVk9BiJwacCK19bAP6xtI3t4mJaTByaWBb15bUr1JpHudIDcKxxqtAU7DFteU%2BD3uygQMMg6ExbjfkffiC6yoFWo1Tz%2FbRymtBORQbZlilw9MLrI87wGOqUBrPwCxAuak55zzA7NgnXGEI1vp5vOF%2FE6C7GGakSkMm3A7Nch5bZloXODMO%2FdHacD14rgLnLyBp0WhIvfhcufxf3jyhIbJNuT2eJ%2FQYR%2BJmrjJTL36fq5jo0pkK%2FhSHcyQsrpetYZ%2BE%2BW8biS3lECGV1vNv92gIkA7Du1L9pjw575I0E0sxlZwGCH%2B0P8gV7wkbRFwz46F8VtKDIKhjarRjke4RkE&X-Amz-Signature=03f4b62072e63dbd7efb9149e0521cb9250493ffb3c41678a5901c4e1f6351b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVBYIE7T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD51QFJfvwts%2B0pRASmvDmRx41V70Jwdb8KMLm1r7Xz5wIgc1edqmVqN2sPeOWnN7g9PgL5ylSrcGd%2FWMMSC3zjrwYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdERnXZEhXMaKhfSircA5YzF%2BpcYsZHfP%2BntceUyqFMhI75hhvgfsQqWbxjvd2ukO6ed7AqnfH5pOwdggsrXVCb%2BNMBlj2DKaKlwefYTeeYIf%2F12L7JGKz%2B7ygG2047%2BcNkBUxs6SHiUzjAUYeYPP3aYiTWRAnvOkrHWL22C4vbmVNiHbn5t8wBXCd7J3dAGg2wiamGeM%2BqhwfvgX9F6I5bq77VVefeCJ2F6EatcB5wU7lGGIcGY%2F22agg4JwYQjuGfMdLwyHUwy5vhUe%2Fiwkg9rpVVQdqZS%2Bzck5NO2pOKIV4xgZ3rbrXTtEsFf29JrbRhJw4yX15N5%2B3mTgkvZGXLHh8axPSS6sMdmeu2dJ0hd9erD1BMeCno4dH0RRGppOeCpljphfF7W%2BXHk4XJPPnFEW7QflyGvTRIr%2BMCptZYZxkIkAFS4eLsPZOLDccgk7lMY19hJteZOccvPI9WqlLuzKJkoxb9fDtirRu%2BwIqWYAss%2BAKIR%2B76yZuZy3h7JJj0Wg4a6p3FivXB1%2BoMJ68C2Mg6tO%2B1Jz1Icr%2FIyY8dmDRa5VOyblqFBuzrrCTG2KiH%2FANClq13kHUFWvszo%2BJTHT8M7ivg8vImI6g2I5omp7JHlTVyV4eM8k1Xq3FIZOMLV7XaQvGWWRoOMJHJ87wGOqUBKrz5LWh4aBf9ALuufCeE%2FUwX9u5yqpt4r3GNoCRrxHRdF1qeSHYIGKNj42rYJxmImf8%2F22Ug6UwTQNKR6Ou0Gk24E2rIXHJbLcXuaDSdHm5E53pG7RotVqtn96ZtxhV6rUt%2BrAmn4hU0ntpM%2BRLKYW11ojq2nf891yhPnQOnMQwHk5uaUOSbY3kT6XPQdl7l6QJRPNK6LIYssTQ%2FxNCT2nEAbtVq&X-Amz-Signature=e7fba8096dcb33334ed8c76b910a41223803d76633837b8bc563ef0a180973da&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVBYIE7T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD51QFJfvwts%2B0pRASmvDmRx41V70Jwdb8KMLm1r7Xz5wIgc1edqmVqN2sPeOWnN7g9PgL5ylSrcGd%2FWMMSC3zjrwYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdERnXZEhXMaKhfSircA5YzF%2BpcYsZHfP%2BntceUyqFMhI75hhvgfsQqWbxjvd2ukO6ed7AqnfH5pOwdggsrXVCb%2BNMBlj2DKaKlwefYTeeYIf%2F12L7JGKz%2B7ygG2047%2BcNkBUxs6SHiUzjAUYeYPP3aYiTWRAnvOkrHWL22C4vbmVNiHbn5t8wBXCd7J3dAGg2wiamGeM%2BqhwfvgX9F6I5bq77VVefeCJ2F6EatcB5wU7lGGIcGY%2F22agg4JwYQjuGfMdLwyHUwy5vhUe%2Fiwkg9rpVVQdqZS%2Bzck5NO2pOKIV4xgZ3rbrXTtEsFf29JrbRhJw4yX15N5%2B3mTgkvZGXLHh8axPSS6sMdmeu2dJ0hd9erD1BMeCno4dH0RRGppOeCpljphfF7W%2BXHk4XJPPnFEW7QflyGvTRIr%2BMCptZYZxkIkAFS4eLsPZOLDccgk7lMY19hJteZOccvPI9WqlLuzKJkoxb9fDtirRu%2BwIqWYAss%2BAKIR%2B76yZuZy3h7JJj0Wg4a6p3FivXB1%2BoMJ68C2Mg6tO%2B1Jz1Icr%2FIyY8dmDRa5VOyblqFBuzrrCTG2KiH%2FANClq13kHUFWvszo%2BJTHT8M7ivg8vImI6g2I5omp7JHlTVyV4eM8k1Xq3FIZOMLV7XaQvGWWRoOMJHJ87wGOqUBKrz5LWh4aBf9ALuufCeE%2FUwX9u5yqpt4r3GNoCRrxHRdF1qeSHYIGKNj42rYJxmImf8%2F22Ug6UwTQNKR6Ou0Gk24E2rIXHJbLcXuaDSdHm5E53pG7RotVqtn96ZtxhV6rUt%2BrAmn4hU0ntpM%2BRLKYW11ojq2nf891yhPnQOnMQwHk5uaUOSbY3kT6XPQdl7l6QJRPNK6LIYssTQ%2FxNCT2nEAbtVq&X-Amz-Signature=8871fc2db62fb3a9c43a0c7ba8c2ac7237deeefb3f97fcc45ca3219b365be360&X-Amz-SignedHeaders=host&x-id=GetObject)
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