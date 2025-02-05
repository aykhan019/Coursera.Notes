

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FGHCDPB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQD3%2FTQuQmsNf9oxQCVQ0P2U3pFJc2CXpbsudqPk%2FMfdcwIhAOKCsZ4SLlJ0oStrXGNQgOjIdFKpqlvy39s6RHxA2bHxKv8DCEAQABoMNjM3NDIzMTgzODA1Igwre6JJsQuQC6f3Q4Eq3ANZ79knKXMosLyZdNC0lv0Z3EX1z7yeaoLkbdvtwaaECunbtvKSQqZCglnouNvfj0sq2tiMtLN39lvMSDbPWuzF3G6tfzefgSzb8qfgdhWzoNAJnUGiDLyGN6y3LRuS8O4TWSYfHa4gUQ51ae%2Fxn9Pvz97F12%2BGhtOLHlVcjuogWhczck4bbmY7W1%2F1q3aJTZO8x80L4CXIgqt3ZGYHkilw6E5H3t28nC5itK9Ggt4MgciqdgGp6qD5GJPsZ5%2Frsm%2BBGyrgZ%2F7cct1XVEncyo02K%2BjYRvf1UYOHr97k6bcRCRNjd5g0XxxXqdnNb%2B85ZlNN3bC5ll3tSl335zJIMoDDEAAXzNjt8wLRQS1Zn78zWenK%2B18UvEKuDzhBX1%2B3iELedIN0Q86Qo50%2BxIWvgcr8fWRP1sILKoLS2PMZvlvZ%2BL0aDVIlLIsVBXXtpcwrgvDxGUXxyxvI3oUYm5Gee1c8o3RH5zNSc%2FM531UOghh3%2Fmm89MgJYJRO3bgo7BismnWsRBKCcuMsHPVteiPpeFK4KUp9nFtbTL%2FHHO5uybqm6elha935TUcYIU0stddbIe0Tt5ZT5KbiG1QYy5lBv0Xckz5NtF6%2BLeJ5hNbsQfN0hEMoWovX75%2FOCEUlRTCKloy9BjqkAcaFBvaCL5uDEoGIcMxxgJh3jkVn5CjptkUQ6H1LypjZQkmE%2FOZAtuEIedlqecqzQfZt0iOqiyh4Q00A%2BFpST2gpka9Hq%2BOw9xoLutCVYb9OsJApwQRMtJEprsuYYsp0HfVcSIxpmsowUVi71kW0eicJGDL7hzIkOxH4pyTwqS0e7fdZzf4JNuTjkNz9IbreY1e0Tu3o0c5SGYR9awJzjIqzhweW&X-Amz-Signature=3663cf03155ac3554571c363127405ae4c46e7f7f0f754ce7603abce24ae7029&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZTM3L5T%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDLosHzAqk1CrXFw82bULKRvVodeVEWzRxw3%2FxIFrkSvQIgOLDPlbQpMT59cMNpCX%2FNUo%2BYSLKV0cKezgAodUXQnjUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDE2njFg007wuF3bUVSrcA6IZ7BGgXAGAbHoi%2B8tjcdG1E74dUSnh0R5Yuhx3WwoUh2rGYgfiNJ6TYZf12YTk12%2FBdFgtY%2FBkNj4irZnejB17jAivHR26Be%2FyaOzIFKzJiRx5GNlMb1VlhgZyZszMRv%2FxCXaVt3NPs5vOQaGfkCAKjrP3c8Fisd%2BRIoXH9ptLce%2BNWkOM7EfvPwuMwS3dLXFbHitN%2Fxypapk%2B9VJoXKTMGSoE11gJFR6hyWdzZsUYLZ4LYJ7TyDfe4wJwlOvg3RNQdksoGDipNeNj0IFfDQFlcX3V%2B7ZDjNcMbqzV5R2uO3anAtbxRTzH4tNB54gRsmym9zxFQY586uAKEMi%2BKVcbmv8E%2FFPzamOHotsL5oar7%2F3Vpl1BLyYb5XMq4AEa3lEQpzy7j4Xhzx6xDbtiOmEk8jCuk3CaJDPV41pfEJ9adwbGCCJUt7w6oBnwtlYmJKIjm6EdVYY%2BGhQ%2FcT5wU5O%2BE1ix4SYttgL8gT26TnLf5WdyQ%2BeqhtoFO15jiiqDs%2FUYwv%2Bunc2QTKcOuXSGiRwFf9y5%2Bg%2BPeiY%2Bi266iXIZENkzfHY2o1%2FNTUZAiczS9iU6hnj9H8zS8vCobXWWaO1vzJ%2FbMzjolqx1YIb4dImloOYpoeTRDjKeelLgMPSVjL0GOqUBLMS1pKPpDzrFUxN70zQgfIOYzYukTPR5gCgM8rS9ZXP6GAEXONKtxS8LtWM5IFcTKFnzOpVYQZW%2FW3wSZraQix5NzT0d3n0r4Lwuq0A0cOX1sM23w2N2BzAtT20q%2FQQwXdgyp%2BMdL1V5Ah0nzy9GVs88ltfvJQqsGOpyAMtcUgysibLUYr1gIK8edh3U6AIx7b9o1BEoRUsS5xe0tjiSXt4ow7KO&X-Amz-Signature=912fe17308d61b5e0174c46d560437e22e4a09a9f05cd5dda727e64d87e9d136&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LRSTZV4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQCvwL9yzvx0QGhFgeMeTkI9HYeg3Pbq5cBRVdAVQk0e0wIgNrhVucyCkR1qILU3mPpvylU2XAbS6%2BUWQiBXjzIK92cq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDC0Qs0AsfsqRKHWAJyrcA7fzAox4YxMclE2A0CnlHnEbPnq7%2F8FftBwoXBD2nempjHsciCPmm2ZJCcmW7tJ8jPk6btgz9JgwHR5iLyP1q1zfwAbskcz7b0YcG0sGI%2B8vB0%2F%2BOmY13Ti%2F3F%2FdU%2B%2BM1s%2Bwnxcbg8KWb3xEhh%2FYDbWyERWoeVfLQI8Ie4J776F640vArZaJHF%2Fe9acPMeQZQbAsMP1vRf%2FZS%2FuIkUtHEUk2DDaEfGPC83Tfodbrm8QBXT9grK0DK0Gxeb0Bo8MF6KDXTPvxL%2F2wycCrzkOMnHvqHek%2FXdwT31yke93sxYuBj0Yv%2Fm2l1RZHTdaAYmGkt7Fz5Jm2vP99H1Y8pTR0SKeTVvBbbBnKyn%2FN9BxGwXbA%2BminVbyi8mDbAWGgzELbOrXy1JFgjUVT4uBJ14IQqzWX7yXbC5o9uUssHsP%2BL4jP31So4%2Fs3EMQP9VkXmotOHne2UKxoCokvQFAq8COko0o1uUKdqQ7TPUZNpEGZrrplYSvBqmeTkb560ywekbc9CGwcWu2YjaNukFL4w62fD2Wj04EbSjXtubWjDJrnl8ac%2BzAc4%2BjXFLXvXHF5XkcIldsYyVcPjshIN8Q3tqylh2EBm1CcMfmK1nQk7TXhzUavJ%2BRgDpDxh90%2BqIf6MOmVjL0GOqUBj0%2BieVFqtIF%2FEgSVXIT5LyUwSo0ThWOZi%2Fid%2F1DhO0Ag51MRmK0q5ryYUZ1OzUd8ISGDbaSKyY%2FVZ1voqhwZ%2FKDmA9kDJ7r3XsGOtj2CKcSuG8BFVu7SJsQU4EiUIXnUQibO5MKkf07j7ZlBbwX1UhuLMrP3bOfHX79o4vXjxYRcK%2BXaiBuHOhu5U6NMf7SHMVdnHKPck29ZE22N0rZVwXAopNqM&X-Amz-Signature=00ef0b09b8b944089845580c698705b76047ec72a131fb03d275f6c46f23fc83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624F5LY4W%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCICuwPLfkhPbY8W1dQRGUHR2E1WKBwhH2YxdzIWTOrYt9AiEArj0org%2BwL4jGkGR1LnraBhUXxhgcJmj9rwMAQIap6qEq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDB3x0HvKW%2ByJ5hJVmCrcA4oDtfL413LHlkOFfEWZnHy%2FrLkY%2BbURHOrq9aa6TMzgfkFdQlpUR%2BAfmWX1FUzISH547vG4eYL4WnDYPWpc1ybw71ZtE%2FORgCvAAZFIgUVbuycPHO0GW1zT0G9zkzhsvwyp5eDjyWrFbUov6y0pz0FaKQDHFIrbDc2Jm1NONHVMznkb6glKWWVsY%2FdYiLyEJrSYhVmrfvqPg%2BGJQ%2BvPn7%2BqfSyOcRMYA5aWvIG7ybh4QcZPJzfCs83SIiyb89MFk%2F2SD3WzdwEevWdj99QjhkEAGfBfDqQgV9peO%2F9aZSAtV5pr7N0csDq8sF8cMJZoy3p%2FYo9QMHDoBxb4qT6dqtwkyt%2BWnjPC6uhrUbjLVhp8Qy1TQfwk6eulXdB7WA4hKW6SW9rZgkCevTKGnTrHMp0xNEzRGwgT%2BFtaXMTSmiq0ti%2BVFFIzzWDac47pQGscQ2wGa9PbUaBx%2BJUZHfaVR%2BbtNnjugAD1%2FvX5Neo384zDtuJorLvSmyEmB2ULbtUJ72EuYG5qx0C0qDSp52jePUIhUgQcuf%2FhwuOqfg%2Bg2M2lz5dO94cKncGvDl0FbbLPY2ygq1cmtv%2BsRV1cJNVOCBqhijMh84d9cPZTG4aYULIh%2FrUNEDogSVUreytCMJ6WjL0GOqUBX7CEETRp3faPk1RLCIeIaCLXx6Qkdu%2FCQZJ4hKGmt8mk4jtmG%2FkDHxZmP5pOXyTfqIeRLdORKAQsxyP2rqcSgC7vMHVnJwVpNCojkYiMDU22ZwS5Avr2JeQ4msMn%2BkIPb7kRVLipf6iBayXwKfpjiq2lQ9kWa7t7aQ0XqmC41WeseZ7drcQtn8eFDPxbi1kN1gz2NI2bA5hOK5cdzxKQ3vzyZU9p&X-Amz-Signature=8fd49860c965437b7ddcc4dacfbcedb67004156d46fcef5cd66f80fd44c8816e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AZA6OIQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQC0bp3ghoDmOyP8zm3RDSNZrMPx96SZUk6V40WwnQyz2wIgZrq7SlQzk63ZG0HWOXiM3HxajOPT4ysCaIConTzcVEMq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDAeZipJuKIMW04dPxircA8d2vJws6RZNknwSWTM1XFw3Wvp99dfXP%2F%2BJsFkZBo3pEjGnkhWcCDJJWyVAFvvrTtXYs5iucwFUZUFGvvnQB3MN5GL96PNr3tDeZkFwOr5vj2Fk6xMJE4L5I3ZcTNV3B5usdhGZmZxJOWs8bWI3oRHK%2FsN8RPli0Hx51oAoLp%2Fp0H7XTSrDI6oJk0VeJ7OwtNsvgUOmIXO2oW65QZ4587Q3PqqrD7NdLsAIC4%2F0eCHjf2fQG%2FEedKgebdeqtGZFMqLIlbNKvm1m4SyKk9YGNgVUHN7aRJZ9UnMDzIDyUecRCiWTH7ZL0NPI9yC6OtdvjCsb4ooP7A%2BvQ5C1ETIGN4NKGCMVhGVHbj46PvucTM%2BMoYOs%2F8QTv1Ht9YFMWeCrsKD9HBgm8B7hn2MfHltGDeM%2BNMk8577vlJUTMl2Fegq9JGCTN6maeHPIl9A%2BIFX%2FDrTpUWAv73v53QqniUA100cJg0wfnv7x6vQcZN%2B7tCESvedXmErV1rakBZwQkLIU6B%2FSFoGrrn8AvXbD3LpFAN8cvrJ1xUMH%2BMcq5INbFQonJt3O%2BEhnWYHS4bX73m%2Bqd62o9aMRpUR%2FFy7DJQfmVOJUlrwNo21aPCcJr1AZ%2FimyaR3liOFsY9hR%2Fgj2MJaWjL0GOqUB%2B5iYfAr2gohfalGDwRZd8R%2FdKFYJ7w8VO9sbo%2FZrT33nLvgwE3zcn%2FnRLYoxxYaxyrJ7pG%2FRLhSSrTqa0PEMpNYXII0emFNZnAnjCqqYlUZLTdylzvBO%2FJq6kMBYCMzeTgT%2FfzTkjU7T%2BrlbmWIerDuDSxS%2FwlaEWsjcikFyyF%2Fo66kFa30hxl4m0PQmJOL9nGKgLxsznB2uHE5OrCnQM55dVc%2Fs&X-Amz-Signature=ca6f468da20d4d96bc1295c5672cd30148d9f1a7ae69aaf7d22e2be3e4b40b44&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4HCXZUE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQCWjQai06gmRhARPVxrcobfKYSkWjmaAo1pbeEWbzgAkgIhAN3%2B%2Bsd6ghv1%2BqzYcG7cZfyCWG9xKnm18xjnouBgSWpjKv8DCEAQABoMNjM3NDIzMTgzODA1Igw9eKWWFgnE7Mn0F9Eq3ANA3wz87W%2BOymQlwlqF7hqIf1rJRovCsYhinnK8Bl382NqjnelR2wie%2FEN9Hfq2t4%2FDG5fCcPVrWT%2F1rwOO2Y7J4WCPGPO8id%2Bcu%2B42mS1mli9ekO3zL8G2RXJw2PsCTXzCUMhPpcTcRlHt4ZiwyfHpCkMSlD9Oe2CnW6ePNS1vMlCBMR4eum6j2ZTjYXipBCHPdHRKUzVV5VMfvcKMCX3VSb7dgNnrMMY5C%2BO%2Be7tqroLRjAaM0CjdEsSaphoWWs4Ej8YfX2ePAw9BpC2npuYNw4sokmOtZf1HW9MftUEE9DvGXbDtqpubvr6fEpqkGNJiuWSyseCktDzknomcKu8QWqh3jEEboRquuUrSdXZdTmqRvxVhgQwzNBwbS%2BkDMyqhBIRyRaJbhTy5sXIM7qHHqqRN6yCpNI9pvIWBv4N%2FPDDJdyC47dAoTc9wd8NWyZCW6Nq9pxYLYpt2PnMkS83dM51NirR2ihlFyfbAMJ1%2FnI2ycd9vLUx5yRwqQYkWaM%2FhngZdVNS%2FZmWnSoyTVshuK6UhyvhJklp5a%2BnrnJpznsNe%2BYUP9%2F%2Bs2IBX5RiyTNIWWDMuFuxHp4eLMWTENAYOMmhN1uXtHy%2B%2BL1uqGI3o%2FwS5tUug8%2BLpnnS4OjCUloy9BjqkAVSjdolS2XHmGjhz0A52BJ2RAklN3jBWjt9nRlbc7nrYz6D%2Bwc%2Fkhq%2Bn26%2BeQkHufqwp6MQbxgrl5Dbwlt7mx87Ej8b2AaMLsEzcFjrzswLc0XGk6ogqvjbMHXLZkY%2FoWYl%2FwMrTnospIzaO6%2F9rFmWKv7CYaQSq13qTstXr44VX5e8x2nKznAdO8k3%2BYjUol7xZj1BFbZ6SrzucWCbrbApzSMq0&X-Amz-Signature=38ee30c6012216e566d1733ee7f2c31bbfdd83c5d53dc1e77d48ae3b9ce54556&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPHQHQYI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIEDzK0CldWnS63Uj7ye8xVCfIEDCZ3dN68khAq2vLEzbAiA%2FGP6Qz6ByyclsvsQnSJ5Nn32BrjWDveRfk4N%2FO3Q5yir%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMuB5IkEag1YjLi0JeKtwD5DcRWPORcX0z%2Fx6rlCq1pSgXxeF5pLoJsjM7BvQYpir13XCugiOQWOwcpE4nNA5AzJgNPzPrD9VSJbt0hzGdo9KcKN4EH3kk56Ga0%2FHfbVmnRNKv9R4NG%2BnJLfVb4JRkaw1G0CPC0FdWWD%2F0S6IN%2BcVYN7WwYn8hg9xHqRjXqbt6rA9w3zc2RhUS4S2DgQVmxPusaqNrvpQpC%2FK57bdKxATAIhnLxeUV9K4qHUQyA30SeDszWZhePLzuYsrIOOFVxxFHwzZQp%2Bsjsg6r6RG7EYpI%2BHE2tJtmG3X6XlzhfVu7WCsmVR%2F2EEgLzA4zSnppzlAKmff2hL%2B%2FciXQXJSnYURIwmI%2F4ETY%2FYZIllAj6NCJQaoBrXc6WefjNXY4adBQxFbJg3XlQscz3PWFfSEPq8W9LJDmGKp875bPQLh8KrRJdy8iu2U3QLOsTZq0kwzMQpQpEMWTr1lWPxNyDqi81bXwQslm1JAhQMVhEJDOrM4d1c1CHFqq32OK56xp4O68DNe9qQcJNIkHHl1p38mmPPvKdYW9Y8lgsBiH5orD%2Bzqz5xPq8c%2FR4elCMDnERWJPtVgdYXRR9M%2FH9yyWckTnZxozBZII8KBz3RzxdV9Gt1LSxdxT2EnFEvd16i8w%2FJWMvQY6pgFK4fqIH284PWrz%2B1%2F4kre6Rwwc6x0pMGKH8WgOkPQydzE%2B1pdUeYXPRtqV93MA%2B8cqGSwyM9d0G0WMydVi4j7ZkES5M%2B%2Bk%2FIm1SovMa7TQJFoOM2zvMrhA6BhcnfRMjBlnw8JIEmKFZUx4aD0CrZJ0zqVE9nOLWgh0JJAIE4O1XbF08rzOjJMyIWz1Owwe7IaTK8PaEEiUHiqkrWmlN%2B5JmR039aty&X-Amz-Signature=c027d570752ee6481f51cc302fc812de47cd53144008ba8b0faedf345784d7d8&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KX2BC5Z%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIBI3SMBT9BBuRyYrDMcNgm8qNFp4LXDnChyvt%2F82SUWJAiAs%2FlyxIVFAOqia7N6U4JdBhmrVwhHGEqtsWpQYPhTmVCr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMB%2BTFyUZU00e8CVpvKtwDfw9hzS1PIPrK5wDExkK4AbsTWrb1iKDVOmO0kEXFr6vAdUBqMlhIeGPwq%2BxCHAfDs2DKaXNzvcaSpPFnhIbNSRvIE9yuqZipnYiffFAY0E%2BbhCK5YWwzasWwmIwcn1GcoqcFak3pIqFvrZc93PysSsSFVAwa8C0AOt6whk%2FYHvH7Fu%2F95lRFCT7DH%2FCMEmyhbMuDEUFgEyWwuW1mztP3z3Bg452YUWidRVgfRwlSFHOzWDAvCexQzc%2F%2FZODN0XiWW0Iq8tmlyTZT2r2OsyfHBZFbFOCs%2FsuW1r8ANVQSutN%2FESKn45%2FyN7b01Vckpz9h6LBkUPBRrqLGOw1ano4c%2FTKTb8d%2F55dKCUDSSfEs5%2FCkh0bmHK%2BiT8TatqAAO3fGvZb3YoumtiwHpK24AB3tgnLg4JfgVt9209DEzZl6uARyq4Bx9ih79Ou%2FgosFtwkqnSMb4Ekv3rkuXuEv0xReDSKojVp7h%2FRstoM5SNu345lM0ugS54KNxVTgycTnGmADHOyRbkZsJfuI33BOkgaxwN6ULZkMSOu%2B7ovuFq7al9dULKDRJ%2BWYFrAvM5EmhG0qkmEiDBbRlzIlE6WpH9laVSvn8izJtVFakV54rM%2FQUdW2s2zrS3L3R2CmYRwwlJaMvQY6pgGrrRvF4XGHP1Jioq31LpTdabHitRFV1DLyIXNu422FjUEUi57ufYg%2FwcANFBHm4yukUllYgXB4JpFfHTxSIWAyHrP5udyIDgy7pM%2FOTNps8RtzYt7dppe8YHVvWgPpDKPt0qkI2%2B5YgoRHD4Pun8dgFzsLFDEBAsGot5xCy7kkXz8bPiMTHbyZ9nB5pQsbmFYFbAylfeArV5rMmbFTNy2AHL%2FwPFjZ&X-Amz-Signature=f34d3a9aa311950c6c97bf0aefd7ad57682829a328913a122781334062a3eb6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AZA6OIQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQC0bp3ghoDmOyP8zm3RDSNZrMPx96SZUk6V40WwnQyz2wIgZrq7SlQzk63ZG0HWOXiM3HxajOPT4ysCaIConTzcVEMq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDAeZipJuKIMW04dPxircA8d2vJws6RZNknwSWTM1XFw3Wvp99dfXP%2F%2BJsFkZBo3pEjGnkhWcCDJJWyVAFvvrTtXYs5iucwFUZUFGvvnQB3MN5GL96PNr3tDeZkFwOr5vj2Fk6xMJE4L5I3ZcTNV3B5usdhGZmZxJOWs8bWI3oRHK%2FsN8RPli0Hx51oAoLp%2Fp0H7XTSrDI6oJk0VeJ7OwtNsvgUOmIXO2oW65QZ4587Q3PqqrD7NdLsAIC4%2F0eCHjf2fQG%2FEedKgebdeqtGZFMqLIlbNKvm1m4SyKk9YGNgVUHN7aRJZ9UnMDzIDyUecRCiWTH7ZL0NPI9yC6OtdvjCsb4ooP7A%2BvQ5C1ETIGN4NKGCMVhGVHbj46PvucTM%2BMoYOs%2F8QTv1Ht9YFMWeCrsKD9HBgm8B7hn2MfHltGDeM%2BNMk8577vlJUTMl2Fegq9JGCTN6maeHPIl9A%2BIFX%2FDrTpUWAv73v53QqniUA100cJg0wfnv7x6vQcZN%2B7tCESvedXmErV1rakBZwQkLIU6B%2FSFoGrrn8AvXbD3LpFAN8cvrJ1xUMH%2BMcq5INbFQonJt3O%2BEhnWYHS4bX73m%2Bqd62o9aMRpUR%2FFy7DJQfmVOJUlrwNo21aPCcJr1AZ%2FimyaR3liOFsY9hR%2Fgj2MJaWjL0GOqUB%2B5iYfAr2gohfalGDwRZd8R%2FdKFYJ7w8VO9sbo%2FZrT33nLvgwE3zcn%2FnRLYoxxYaxyrJ7pG%2FRLhSSrTqa0PEMpNYXII0emFNZnAnjCqqYlUZLTdylzvBO%2FJq6kMBYCMzeTgT%2FfzTkjU7T%2BrlbmWIerDuDSxS%2FwlaEWsjcikFyyF%2Fo66kFa30hxl4m0PQmJOL9nGKgLxsznB2uHE5OrCnQM55dVc%2Fs&X-Amz-Signature=38ce2623c0d71e1632cb2d42170fdee4446dfcbffa815aed72c4e8a07fac8679&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HIYMIJC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIDg0aBhneBYeOSUTfu8SgjmlTE0RhUz7S5Yos5%2F8Nl%2FGAiA6RtOHvUWwQbUre1%2Fqwuf2Tq4m8wAgKjy9YqqM29HVWSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMZ95ccOn%2FLYMLY1ZEKtwDYusPqC5MdTqFJlBASL%2B7U7MRBwg%2FBIP7oMEnKDPMD7TxrocGnE0uc7m7XXbfCWTeK7g66HYf8ha2Kt8HNJvzdVBB0cS11fGk4T3AmDApw1tDZ0zD4QmfKyDYsW6VHSRxDcQF5OUqwvaHn1Fft4vO5eh9Jg6RY8pBFbUZzGntHzXonG6Iti8kLL0p%2BQ22ZfC86Z5hcBlaYxcl6IDc%2BiH8sqoqaao3GQOWkacZiFUCoj%2BarYYw9kv4o%2FmRPomL0rV%2F%2FVEtqu4OLkJF7kWHhBZeq9dFQCVesqYm3iY7NNhPuCUh1RiFsrDHWHfsSTyJ0JrBIdNjGUXhBNM8bJce0RI3gwKCdAIAjcUdfYkM7CRini4N5mfFZ%2BgZXIceDYocBSHSs2vo%2BtfZIVSiOCoYjSw944y0NadWVEivisePyzjDWUk5z%2FyWfnp3Z4cQ04HoRq%2BK%2BuH%2BCmnkzPYcRQPGYsfeoEtXz2Mi1jw%2BTUcNe7Ub4xyTnddBTSierXGUTCbc4w%2B5CbTbn%2BMNQ4kY%2FWSWvAQUYlslzWATyI7ka%2FUf%2BOLxB29Jhu56t9Wm7lUcWKypHqQEcv39GdSodyKPi9ew5MvTfstwjplpYLptDW98utIznJqk41qVLbQv03aiSLcwlpaMvQY6pgFnxDKvYrEGTLkfGd6412rXO3V4k6UfyKX%2BnZvxILuKZyHTPX3k%2FYOnV%2BMii8SC978fz05uM3E38BS9IJUQEkC6LsZWppe0uHfz%2F7T0mdtr7K6QlPdMj60iEEgQOlZzYfyi3ee25o6YcU01NKUlGyvoJZfUJvzDlaEK12SsbvUAzjpCKjfuEjFHN%2BnnDNRSGv9wLAKEFOD%2F4Gt8w0tEFQQPn%2F2Ky6Jv&X-Amz-Signature=7e15c6d3e50856a5ca1a0583fb8b2197eec128508a18c8b704e04674edca5de7&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HIYMIJC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIDg0aBhneBYeOSUTfu8SgjmlTE0RhUz7S5Yos5%2F8Nl%2FGAiA6RtOHvUWwQbUre1%2Fqwuf2Tq4m8wAgKjy9YqqM29HVWSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMZ95ccOn%2FLYMLY1ZEKtwDYusPqC5MdTqFJlBASL%2B7U7MRBwg%2FBIP7oMEnKDPMD7TxrocGnE0uc7m7XXbfCWTeK7g66HYf8ha2Kt8HNJvzdVBB0cS11fGk4T3AmDApw1tDZ0zD4QmfKyDYsW6VHSRxDcQF5OUqwvaHn1Fft4vO5eh9Jg6RY8pBFbUZzGntHzXonG6Iti8kLL0p%2BQ22ZfC86Z5hcBlaYxcl6IDc%2BiH8sqoqaao3GQOWkacZiFUCoj%2BarYYw9kv4o%2FmRPomL0rV%2F%2FVEtqu4OLkJF7kWHhBZeq9dFQCVesqYm3iY7NNhPuCUh1RiFsrDHWHfsSTyJ0JrBIdNjGUXhBNM8bJce0RI3gwKCdAIAjcUdfYkM7CRini4N5mfFZ%2BgZXIceDYocBSHSs2vo%2BtfZIVSiOCoYjSw944y0NadWVEivisePyzjDWUk5z%2FyWfnp3Z4cQ04HoRq%2BK%2BuH%2BCmnkzPYcRQPGYsfeoEtXz2Mi1jw%2BTUcNe7Ub4xyTnddBTSierXGUTCbc4w%2B5CbTbn%2BMNQ4kY%2FWSWvAQUYlslzWATyI7ka%2FUf%2BOLxB29Jhu56t9Wm7lUcWKypHqQEcv39GdSodyKPi9ew5MvTfstwjplpYLptDW98utIznJqk41qVLbQv03aiSLcwlpaMvQY6pgFnxDKvYrEGTLkfGd6412rXO3V4k6UfyKX%2BnZvxILuKZyHTPX3k%2FYOnV%2BMii8SC978fz05uM3E38BS9IJUQEkC6LsZWppe0uHfz%2F7T0mdtr7K6QlPdMj60iEEgQOlZzYfyi3ee25o6YcU01NKUlGyvoJZfUJvzDlaEK12SsbvUAzjpCKjfuEjFHN%2BnnDNRSGv9wLAKEFOD%2F4Gt8w0tEFQQPn%2F2Ky6Jv&X-Amz-Signature=ffa0d496155a3a967993c0b0916b487af8022a2887bfe1f232d99d55061d7358&X-Amz-SignedHeaders=host&x-id=GetObject)
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