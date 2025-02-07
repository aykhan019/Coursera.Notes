

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WPKGARL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQD3%2Fc68bnED8fLXQwyCC18esKFgqwlbOirGFYyauOyuSgIhAOr4IE7LxrZhR%2FP1nrmdgmxvBI4dkjynDVeACvd%2FuHN0Kv8DCHAQABoMNjM3NDIzMTgzODA1IgxGGikqzLlkUbGsoB8q3AP8HcAxmMnu1bddUXIKcDI70VfFeTc8T55pCh%2FF%2B%2Bc6TAryRk8dYEr6w%2BFSnY1TV7cT9dVEylCIsW3uPpYujRqe6ebBdyzvO5X3%2F3TrWVyu%2BwMD685PA%2B0UhdsxU7YUY2sqQ%2FhaedybFZOj27JkQ3rMwfp61I%2BCnCQ799FJ6gAc2tBZHQrZzyNMVBSDEF1sxqxY5PQ95%2BEgFaCPC0PtHoXE4HCwF%2B3cEZIkVyRNMp3nwccXuaR2zloR%2FSct1XedtM6kQhWiQowWF8IZ2l4%2FckYHVFTDZW8qYtl5m%2FEWOoGKhjU4nky16Tj5NsHxrC5bI58rLUlaec%2FjKbN%2BfgdkXD4RxH%2FCgjfyLk5SL%2FS%2FaPEq%2FvPUiuQ0XNVYlHuH80Qnk2MGKZbCZs3Rvsr%2FdqKCJX3Ny79Xk34wAJ5jhvQsgUhWx4ML%2BaM0%2B0qlMR%2BB9HVDZWrW5lOPs5PxZTo16wdHLYPhx7Gmx8mhZNquq2vHy52phY1xO%2FBjpj9%2BxyqqWj7VCY61Zfa7EHD16m%2BcsVJ%2BI2pZWefaizvHSCAWpDa439tg4DsMkOUryP7hYu8FC46Wttql%2FTzXNSYOqSMP%2Bj4NG0gTYqVo9qC0BOD%2BPL287BU72GntR5q3w1Tw3yp5%2BzCW3Za9BjqkAXwX8Dcdpk4iJFHGm9LY8irFUJW0JIxLi9XqympUYSgIkJfymb15ikbynn7z%2BM06rYqLQuJS6v71y9%2FL4yrixSrbFy%2F8VCvCLFIVWap3o1kLwEaOsI5dOlHm8HuI9uLMGeybHGzlvfdHWUmHf%2BlOutYqNousnrElMxz6fYqXQdk6Kac4gnnDKEbKmchtMgN657f%2Bqfc3Zn0RhFvbAyTn80%2FDot6l&X-Amz-Signature=cb4fab8da051564869c3b65915aa8cbd450bb34c1b52780b3b20f8baf7245934&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQWEGRQL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIH7dXtiwXKX7Dhsj6zY5T3oQo5cSgbuXBS%2FAb9AW2AGxAiBKNlLDiPkVL3RawJqNgius%2FumOuazrNbNXVl3f4Ag96ir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMugfVioS9iNNZ6pobKtwDCvWuv2HmVm1ylKgtZP1OfSUJPwL43cwUD4fVeLJVqeBk9voN5rgHS8M9L5AaaYaMLnUEJoaA1JkG7%2FIe9XAMa3fAEW7wV1CquHfOYlY%2FJnP0z5Y%2FNb6l12PsuMNBl70KLoMhtWB9k0g6d1HXmkWT4PJ0dbnTZsmXw4as0QivPrQE3qKPUZTwODpk4GpMFcQ7pBYmD00PVawzjrDLyE%2FrAkm35xx2sLxle6IH9eceXf%2BxMACL76Zo7NxzwMAN6mVXe2r5RUh%2FGceg6KyndClVN%2Fb71TIut8ksjH4Uh63shDm28THyi3J3XzaWm1J60XNXBldDaDA3iaUXeZoO6EMfnk6wO8jCKqP0%2Bv7FEBq%2BcVqXHpxSsMSYk0iFJqXadybdwEuCxNtkeI%2FmA0pXRkT%2FfgjBxD%2BiSIOt2zF3w7NqmSDvkXlwZorofzUyEJVCHqOOu70H82twwhk0x7Fu3s7peH754md0AXnVH2Xv3ACW8XrkZE9MwDgBzd5acBQ1yUpKTA%2FGPMKx97GOY3fnKPIwF1U3JTIhsQ%2FLe8uQkJXK5vkuFrhE08p%2Bo1dX1lVFoD063nKz4PW8hMR51Xh2oD7PBgXHm%2FUbGFKCbEAc4Y2Ug8BHjBgqWosOJHkRZ2ow9dyWvQY6pgH%2BqCo1p%2B8BPlly%2FAn1TqbAg7Z4wyuq0TCiUfxtyYdgFoWwHuCnlqd22WlJUOnPIPz2F8p5EYhSntjkMgnvDQScVCrAmY6XNLqVh9NWvnM2VTTmbrZCJeYNGcpL3mOvPdnld%2BclCGf4j8tYwfSHcLBT5NW981sKrp%2BSBLJ6mMXA1WJvcQbyp%2FTQZh%2FvYhflzlwP35LYEWDGpuIZZMoxJ7HKysKjKv%2Bi&X-Amz-Signature=83e8e646357fcd299ddb981339942514c37082af38ad8a8f2b6fa02993e82b57&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCQVWD3J%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQC%2FEjTAkVW2hGyfO5ghQZIa24V9C3%2Fb6n2%2FMbJ%2Fwz5npgIgYm9F24RjOOMsnAECSdRte%2BQFYEeklhEo0HcHOPV4PMgq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDLGoOWKCNPkmR6%2BkHyrcA9htyTAbQyg4XpEJDIYwrhQoySVrPeNCrag4d6EQC%2BjxFGVpcid8%2BmZG9UeKrzxVx2TjLjjgyERsZhFkiP9qwCqxO6WRENBkfGyjGOEX%2FVSe3GRdpObC6X9tNB9yGz7CMRMyjVdq9aYVOo%2BttsCY2f6G0Mc0CTD3P7Jdbcn7%2BGrkErpWLUvPJxmGha8ljTfl1myUbUjCrvgJVOioYbrMlMeFDdT1rTEnw%2FMR3Q0AfeELQ2QWYy7%2B2NqWFbZ%2BfqnDPUVUQKZoko%2FwIoUHmd3WMgmfsaGR7xOj15cjlcL7MwN9N%2FX73T4N%2BX4FHKOCLjZT%2Bi8GmAF6XxxtR40XxLQcQTrEMLwxrYKGWNcyVSSIN9AxuzyfE4lOwdURlO0%2Fx6x%2F9Y%2Fy%2Bnrc760UlSYTRAV16c7%2BSoOUAO2MLlvNKlUULszyfEgzZf7KUHZELQJX68ZdJB%2FU0LfHbGOJKV3jrtBgVVNm%2Fy8%2FyYI6D%2FyGhOr05FfDosBQW90y1%2FZP7oYrhnkj2wC8V%2Fd%2BPRLEQDhG%2BQlbE%2FPAXkB4lqUabsWQsfiplJ75wxSrDSG4Y%2FWaH7QCsZgpQ7Xa3tLaTZUA%2BXs%2Ffk7cYMd6jBnU9Fvp2%2B9De%2FZ4lFKWLP7gqL0xkG4T6r9RMIXdlr0GOqUB9QWbTAaG2N09dVWf2Rjbx0x18j9hg3UJhGl2S3FM8cla9Ihk4R69blgfKSXOBOPdGLdSmdTrCuSTqn7hAdAe55bh8B1OEE6XpKphskclGyyHNGDMkyzIABZ4bWX6sM%2BIwr4IrUIR7uczD%2BsQkxhu2y7t%2BfFtdxcZJuWrjfqvpF3kfoVts%2B%2BGkMNU8yj1BWbvBBXCk2VXufziFHJ0Eg3fEMqlMHlt&X-Amz-Signature=a1815cc447cafaa264c621f180b5b24789e07b80bc3b232292757d7e13a607c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVCUSJPJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIG4SVDPZz8Ksd%2B6zg9cmcGZDm%2FEpDuaRAKMI7KC7LLLGAiEAt2jpzUvIS%2BbpUC3oKfVYvdvV%2B1Vv%2FgZ527MuykkGRiEq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDM9ypi4ASf0NjeGn2ircAyHc7AHvOdMbrhKiDSH%2BzQSLV53NFQbwa5WKrl03zdLvS8XkQsCsV0yNYYt%2BFXSLaGIKC7%2FqVNEE7Nk6igowtBmUWqgRrLEza0raLKBB6EH4dZXTI0PLp2hIawLj0q82A%2FjsmfFXTdxO6xm4PglFXTnaAgisAgGoarUGYP%2FaWt6IDZ2RRKXeqSUcTHkr%2FiqdzGFB8xm4bOTACf%2BfB1FRsrT8qVLRBetPa9WRXt1xWYICr7r9xGYQAweNAwUprO8xNNjsu%2FuNgD66GuM7qlPccep0XM6kq6NI31FUGvmd6mTp0Rj%2FCMqWmTdJWHoUJC%2B24A92cRtdoOrjJGbbPw7VMw7KKQllt0DSQyY%2FpMbY24G3XqBVCjQf7vSnhHT6VVP5XwDlxbefhKN6s1gh1tiKXTPTEEM0D7ixw5AxziORmtmoskIO2d4mq5wBHoJKmvYrLpv0lT5P8HelujpRd8MbciHK5cDtYVmpiyDlra79PuPDJ7Mt%2BkS%2BoYlRFTxJKLIroYznQ0d0O87C%2BhXn%2F6QfzkTGEOpxHcYThd25MQFTjR8IQ%2BM4%2FoyW7HIT2zEdH2%2FKJmTtic0P9Iep%2F%2F8OfRkO11bSGEJL1w7MKy5kMaqxyJuInWmroGoCli8nX9gZMLfdlr0GOqUBoqZyAGBg6QaT%2BA4e9WT5B4wXtuQ9rG0mSMVfVIp2Xh9bo01GdNehvrXOvq2raRm2HpFjSb68GXhLVWIerjNglgoXPtpQNZ%2BByVXbSajtydFF4VIoMU%2Fy3EkHJJRjzteGTiCe0c5ned1dh6OXPu0aqUZaEXIK2ZYPsdYtAyDoxk3hBrJQzQQVC1srg3O9oODNiiJbsuy9jETWw%2F19aPkiDz377r%2BS&X-Amz-Signature=16d86c0273d75fd43b387c441a1750b1b10e8a14e47be6946012a6d423149b4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3Z7DY3N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIAQA4%2BU%2FJzEwp%2FHGrDlicdyXQfdA00jzXIQOhcB5pVdDAiBh89IOw2Oa0%2FcfVhsvlnlQROnvULU3HZaedLho0QVr3ir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMMa5NuWegAzUKwdA0KtwDT577j7owYnAhJDFH2UjwXTpPhTcCg%2B47EnRR8vW%2BTUzR0pUOBjTO0LN9nM5q%2BmdicRSUCloUXj5S8%2F4PCLn7lRcmkgxlrdvxrVGHUj5GnRiVGtjEqNmkCQCkYDKgdpWQx3Ab9P7T%2FlwSqktzgMEYtch40eYxhXgB63qQ%2Fq2bknUWn54DSkrE%2BedOkmdIG6NaOaCvnKD6zNDH%2BT5k3fvQ9QnTPdIPtJeT8HwGoYHr9rB7bFZPk1HaX7OKpWCEcLvRrkr8BoxoQCCAfPFtXiY9ok%2FYsVJ8M4odxUIRqECmNwu%2F2E6OkmD7CcGqKNymD0WjcuBOegzhx8HJ6jGr%2Fm39yTPL31XG%2FyKfpyjETLqqw4hdzvWP7dAD4qeX%2FUkP0QZbDZXyMRzF4o%2BJ939gpjNtDcAhyDRl%2BTg%2FOSEmOGoBEG%2BYTkJ7hWLPoK7HSbAGAVjjp5eZnQ5fhPa5WUUL1NXWT4BdLbFi6%2B7z56LnyGy0G9L6pEnBVmAIyMTwn3X0gKBCeMzcmsyzjEMoKgoPq6T2o9tMLSZCiNEkJwnU2IsGE%2BY4ihWCVPnxnxoSx7X4EEovMkk2poZ16quZg0k7tJyqSeMu6ua8Ct6gcpAnUS%2FZHpC1jXrKBpxeCwbf7X0wnt6WvQY6pgG6%2BUFUHjX3CZtlQLZc4f23MynkQ%2FPByC0AGbGfuMEqNieDjcv0yAm9t6CK9xmXKetRjEITMQYtijtG6z7%2F2I1SUMKb5sSjG0B%2BZqxlFlXNAsy2dJl6PQJq6S7F4e6pvvRMRFggngLNZb3KYOfYgyXj4Nd9c0oOnI%2FVEG41it5L2tdXareqpQTHewA5avPyo%2F5QFkQMmoaRrkiqq4YThWDu528oisKr&X-Amz-Signature=2849def5853a29cadd0642c1893c259d20160cf6b2ae57781a09d1b1a8e47e61&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRUQDMR2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIFU3CHP1Xf7TPBRQeRQ%2FuEJh4OnUrFLcjlrFnXSE4YJpAiEA8T54hKQKsEcM2JPSwbJ0MVo3lvdC7n9WbhVhkS0YVAMq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDPdc7MxsqQIo6zHiGircA2elD1aLbv93496VOj6X5TxIDofwQ%2B0jTxquRJlPJMPJQ927k1LS8zIwf3%2BdDRLxV6FB9rxUoS1tNqiCcQff%2BCCaTXmiyzquF%2FQnU3Pu0iO%2BdcNGvnEXd%2FQsV2ITUopfq%2BGblh8PLXn9UhH0oU1EeJTNGgW%2F5ItsfKRinZBBk%2F4vxks9LcCrW1xR2%2FNYeajp%2BKiRMeob0kW1XvYy%2FhSIRwUxn4PtJ16VtkYHaZzyQDE02Ck%2FjE7Qn9Q0e%2FPkIxUVsAffbo%2BE88x%2FA9vISKSrCzo40wtnKrCUwhKQrCfbqwD%2BrP%2FHGqebzGMVjmznShYAx0FXAX7MbK2ttQA%2B2czBX%2Bvjb8FhsUzcjUnK3%2FURLYoVo%2FQRKILIK8FiRYSX%2Fzp8%2Fa9Dc3oNpzxAMimB3F4leN%2BODzpfKPwLe9D3KskOgWBzAxd8Ena%2FI9xExYpOZzFBOSxFv5lHEE3zg4X9Cz8W1Sen4TOYQeLLnEKUvXkMdm%2FihNx%2BSFBhBUcYTzP5FKoNeysp82k3MUSUzWa%2FKQXkRaqFi0wtB%2Fuc%2FgiyWUtMvldzYuRAe7T72S%2F%2B02tn1H6ou4HHr%2B6ljc38b6RLZJ4ihwS1iJJ2OcsMf0Zt%2FQpJ%2Bs4SJygd8no6rwIhFhrzMP7clr0GOqUBdoNGxAv6G87sOFEDr8P6y87LFF561OpIPpPNL%2BlPteKCyiSfIfMWY0VdE%2BiMSYDHqk3GiOdvao5%2FoeMEYi3ya6FgXroaghYJzPOJYpXnbqBt2AafhU%2Fo390COw0UrNNTUYytqLV9Yl%2BlqlJgS0VpSvp3YAZOkGIiAyhY3PXphxGzSOpIsL6eTstLCEaHwJk3AMV77s2dJcaA3CLkuAfbAg22ALsW&X-Amz-Signature=025187b76b6df854a46a973bd701b9bf3b7e96382929061d543383fac1c2e12d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6YBX5ZI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIBa%2BXLNRe3YHNtcTe60nOoFBzeZLH0NgKtc21RcmYfbCAiEA6ASFnZO1zKIZ1ZL6aPpmL0kuXWEBU5FEbyLjHjuS7Bwq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ4kEdG1PPl7dFce3SrcA2ewlzHfedB98iIdjtO8NTN4ywmqb92WNVS0brqIDYLtNh8aZEZRieRHNy1wgjLrhcB8As2c0wcXt%2FnqYCtHzpbf7zjhya%2FegdFzZLuyaayYnZES4A671E4tApiIS%2B7iKSMgPwAnLAjvsmI1mxqhK%2FVB7gbHSUddvMPIDFYqn3tC87F6SU9lHay9tXzvOIkJ%2F%2FFbNEAOV96R8oTYas5%2FtD06su2qkrATCCFml34Oq64vEdvw1Zr2NTivgUZ2%2FNtf1Zga5qWUL2Gc0G9UvY9PxN4m5WMerDrrUTMaBslTcbzpj1ptBG2Dk0dDhszSzPfKmuIiSdwwaNYh7KIsI7T0zglqh0xWBLGWQRlXRR543DlAfLG85sC3X1nbKTYQXqKwm1Rq8hvPgF2yubICGmmmIHGpqBbN43%2FMgThuw7P6SR%2Fj4g0Hvz7VOMtnAENYRef66zTG2UNF7l3PZPr0tDcevoVwYm3Yn%2BxHf9q4qcaMjFFODKlraF%2FRpjteZcBlyvncswYs9DxbhtVHeAiGFzT%2BkKlcyFiAKpQ4rRtWw%2BkOVc9lVfO%2FXLzYZHI4bJvDtfsc%2F571ol3ACk%2B%2FFvketzbyaALX54Xpu4XeJaODiD%2FXnC7iHvCwNcbgP9%2Bi6QbJMMTdlr0GOqUBMF5CKzJ3D978XlWs7xcbr8P6fEXozvPH3u0VPh%2BDSNpPxo83ferqkRPQIUB0XR%2F20tg9sMlRMtnZs83CHymFxagCS4LWBF1miBG7CPSpO7ULKbSA5HDjktbJvZuLm3pXxIn0ECgfS614b0IjO7ka4r8zn28PAtoemIKY90svGhK4kZ64nLaEqRwpppneqYxVh2JHX6IzOno%2BfMlaEYy31tP6HOZK&X-Amz-Signature=26967dfccc91613ceab0916ac47a7739bf5ce61b71eb56c2a9c5a2db2a450cac&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOARR5YF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCN7VE9uTvcG%2F05PsE1TSAtXG0%2BjbcD50zvMLgOPobtcQIgP%2FNsZye32YF8aXisU%2BIYCDlAZYVcCZRdrOVDm8E0Rrwq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDEf0x%2FDyTqyYCR2O2ircA6ADbDkBYIdJl9lEWwVGoj6MZxgIOz4KcvS%2F0Zpdk6%2Fm57e8WnBii4kJmi3Dnyss3C1SgZfw9cHuO4Yx%2F1Fj6RMppNsaTkcfw%2FDC8HQUeqKv5RCdg89r%2FDDXSPzczo4dXkzdmABqevdDfKun%2FlTW6GrzcibHsezYAibtcZTDtd4xOf0YvfRCZyXetuT3cFrAka%2F7aCJiuR0AV58W8fmBZm83q9%2BN%2BxTV8LJhpGTrv8ZvW3peCqAIKo7hWDh2zt6tKVtBg0AkYZgsxt72oFVXkLQ%2BENAtZOA16xq1KQcWr0uh%2F4z9WcPCd6VVDAasEdudKqcw%2F%2FH%2Fa3gX7s5FaomhX1dF4JdXo%2FuerXaSUYbNVGCxtYwdq80Xybl7J4RNPQLwVaW4nxDjL2sA93gTMGMGk2OKP%2Fx2o3Ofs7m92FmkAoa5BaltUlnG0igQLqSc2t4EZxLqaM%2BotV4SEpJROWZp6S1RDY8ENNNfo%2BdEEq6lS6DM7fUfFoFb684fXcRz8oVlduaDQGjUN4%2BBgsRU26i1yruQ000uWmyJvDZJv8RTrEHzTtwTlrNFtY4PaSbGE2HNxe%2FfvqyjGLbUZ%2FO58gXjgZ6OUAsOZoE73twESv642gc6WrRw7E7xKnkVGu5YMOXdlr0GOqUBMOaX7jEc0BKHRsM7uYTgKI%2BIEjM6kmYSzfFvtnDaSy5RpJpWzCCf5U%2F9SXjXxA9DBWlzrnkKpJiso8lza3pF6PSWRq7fElSKek4M4PSppdfA9BsO%2FwLimcmR6%2BkBTbzSRKa0AACN5NpmDXdq6JFL9QqPVWaFw6uZMsl0u47mT7a3ghx4Yzq18KjkYq7JjWbrM8WUSmj7SJgsrPm9veewkEtclwJP&X-Amz-Signature=03d6392a9c3500813a35af7437cfc4442141f120ca69e8b320b6325be33ebb89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3Z7DY3N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIAQA4%2BU%2FJzEwp%2FHGrDlicdyXQfdA00jzXIQOhcB5pVdDAiBh89IOw2Oa0%2FcfVhsvlnlQROnvULU3HZaedLho0QVr3ir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMMa5NuWegAzUKwdA0KtwDT577j7owYnAhJDFH2UjwXTpPhTcCg%2B47EnRR8vW%2BTUzR0pUOBjTO0LN9nM5q%2BmdicRSUCloUXj5S8%2F4PCLn7lRcmkgxlrdvxrVGHUj5GnRiVGtjEqNmkCQCkYDKgdpWQx3Ab9P7T%2FlwSqktzgMEYtch40eYxhXgB63qQ%2Fq2bknUWn54DSkrE%2BedOkmdIG6NaOaCvnKD6zNDH%2BT5k3fvQ9QnTPdIPtJeT8HwGoYHr9rB7bFZPk1HaX7OKpWCEcLvRrkr8BoxoQCCAfPFtXiY9ok%2FYsVJ8M4odxUIRqECmNwu%2F2E6OkmD7CcGqKNymD0WjcuBOegzhx8HJ6jGr%2Fm39yTPL31XG%2FyKfpyjETLqqw4hdzvWP7dAD4qeX%2FUkP0QZbDZXyMRzF4o%2BJ939gpjNtDcAhyDRl%2BTg%2FOSEmOGoBEG%2BYTkJ7hWLPoK7HSbAGAVjjp5eZnQ5fhPa5WUUL1NXWT4BdLbFi6%2B7z56LnyGy0G9L6pEnBVmAIyMTwn3X0gKBCeMzcmsyzjEMoKgoPq6T2o9tMLSZCiNEkJwnU2IsGE%2BY4ihWCVPnxnxoSx7X4EEovMkk2poZ16quZg0k7tJyqSeMu6ua8Ct6gcpAnUS%2FZHpC1jXrKBpxeCwbf7X0wnt6WvQY6pgG6%2BUFUHjX3CZtlQLZc4f23MynkQ%2FPByC0AGbGfuMEqNieDjcv0yAm9t6CK9xmXKetRjEITMQYtijtG6z7%2F2I1SUMKb5sSjG0B%2BZqxlFlXNAsy2dJl6PQJq6S7F4e6pvvRMRFggngLNZb3KYOfYgyXj4Nd9c0oOnI%2FVEG41it5L2tdXareqpQTHewA5avPyo%2F5QFkQMmoaRrkiqq4YThWDu528oisKr&X-Amz-Signature=6de40d0cab6bfd7f9e2effafba58a3370113a1ec65f324344b0182e011d52beb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGFW2RSA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDN5cCddmHAoiFTcaSheZopBGuxZlngS6bwZNhCcB8ffgIhAO63Q59RPO%2FPZTz4R%2F6WMyRgWLKaldhGGrogL5xGPp8kKv8DCHAQABoMNjM3NDIzMTgzODA1IgyjK2HHMIo1AUT3dcEq3ANfYrtVXdhIGrFGee7TevHilqGzmOlf4hXy3CDnNF7TB%2BhiYIs3ZZzHkvDi4U69KXrJ6Oiwag1Pay2JmamLneOp2%2FC7koe7h9NJtRS1ExDjnaPUj7fHwRIwwvPwxUBC9OQNXg%2F7W5PfzGIDRZPXOuEW6jPk%2B4wxJTPNmb0PUPxuALQXrU335DeXtxj7jP568%2FWvcw%2Bz6YnQSKPM8%2FBYjPLaGQpv7GK97MNh1H2yTpgnXs%2BJrZ3ePGXU1kO3dzKiwXj0F6tyEuHQmvLMrtvH6rjQuO4rA3kzZ58baOi%2BjvAGYRGySFw3Lt5UnirD8dEm%2FCcv3NOKGQTh6yBwruMrXcCWqj7it9kuTNMKaD8Erlso9BS7SuD%2BG%2BRC13KwBudLxjYLkGi9UCB3UyrJyb2C3lmyU5ws43SlR%2FLCv86S365QIa2EABaH1KTyq41ME1RokJPfMHRr4PkXu5nns3iPkwpNOxrDEZBDRWVooF8%2FqTKLj%2BW3xUjUJaIcO0BA0qBsLnIh1%2Bwiair0IOAmnHlaFYRCMxkSkZRvKOxyqo3JB3N7T7rMCX2qcuZPS6Q4NoHhSHYv8WnZRonEWlBNdo%2BpLvqikb9oNnR475LLbdrTMnvxRQORgr8qvJGrCwhQpjD93Za9BjqkAQrXIqlHmbvSsd%2FqQXh3UY45nTb6uNKwP9%2B1ZpwJBP1FJDKEuH5ynHOA%2BTFx0PVRj3ZS5mbFBbCS5f%2BXkvQRbL0TfiVY%2FgQzwVnzA91sdXChkHNKayvb3tTJBM5a0CA1R4OZ1CQZs0PNbNCGrY5HeVuiR%2Bg1vF9uNv4PuQ%2BcoTim%2BgQyKrz1QUvTfgcvQXMFFECH9BOASGKsUw1rlfM6irHx01G9&X-Amz-Signature=cc4eb85ad233850403f585627690e2b593098b17539678d5611dc76ed2e822cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGFW2RSA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDN5cCddmHAoiFTcaSheZopBGuxZlngS6bwZNhCcB8ffgIhAO63Q59RPO%2FPZTz4R%2F6WMyRgWLKaldhGGrogL5xGPp8kKv8DCHAQABoMNjM3NDIzMTgzODA1IgyjK2HHMIo1AUT3dcEq3ANfYrtVXdhIGrFGee7TevHilqGzmOlf4hXy3CDnNF7TB%2BhiYIs3ZZzHkvDi4U69KXrJ6Oiwag1Pay2JmamLneOp2%2FC7koe7h9NJtRS1ExDjnaPUj7fHwRIwwvPwxUBC9OQNXg%2F7W5PfzGIDRZPXOuEW6jPk%2B4wxJTPNmb0PUPxuALQXrU335DeXtxj7jP568%2FWvcw%2Bz6YnQSKPM8%2FBYjPLaGQpv7GK97MNh1H2yTpgnXs%2BJrZ3ePGXU1kO3dzKiwXj0F6tyEuHQmvLMrtvH6rjQuO4rA3kzZ58baOi%2BjvAGYRGySFw3Lt5UnirD8dEm%2FCcv3NOKGQTh6yBwruMrXcCWqj7it9kuTNMKaD8Erlso9BS7SuD%2BG%2BRC13KwBudLxjYLkGi9UCB3UyrJyb2C3lmyU5ws43SlR%2FLCv86S365QIa2EABaH1KTyq41ME1RokJPfMHRr4PkXu5nns3iPkwpNOxrDEZBDRWVooF8%2FqTKLj%2BW3xUjUJaIcO0BA0qBsLnIh1%2Bwiair0IOAmnHlaFYRCMxkSkZRvKOxyqo3JB3N7T7rMCX2qcuZPS6Q4NoHhSHYv8WnZRonEWlBNdo%2BpLvqikb9oNnR475LLbdrTMnvxRQORgr8qvJGrCwhQpjD93Za9BjqkAQrXIqlHmbvSsd%2FqQXh3UY45nTb6uNKwP9%2B1ZpwJBP1FJDKEuH5ynHOA%2BTFx0PVRj3ZS5mbFBbCS5f%2BXkvQRbL0TfiVY%2FgQzwVnzA91sdXChkHNKayvb3tTJBM5a0CA1R4OZ1CQZs0PNbNCGrY5HeVuiR%2Bg1vF9uNv4PuQ%2BcoTim%2BgQyKrz1QUvTfgcvQXMFFECH9BOASGKsUw1rlfM6irHx01G9&X-Amz-Signature=1e77f9815c4a287d8cead822785048e50fe351356891a475fcacafec43cf25b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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