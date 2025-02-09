

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WMM3VAO%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGVJpnzthfxB89fQ47%2BYDyyfuc55EtMBiqhNfdxiuIstAiBz35TDYJnqpsnNn102dg%2BM0HvOI395EcL4AnIIsKJYViqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4Xknu%2FaxYo7nYaavKtwD%2B1cZd8ILGMahLr60ah51VObs6S6Q0WD8lEFseU0DnXfH%2Fblx2VkKz6R8WYfhOlqokJ0HJvurF5caD2x3KHDFYLReSkm3n7oH3FeAnKHWUe2aZ8toWtZrW9oIRshz8yBKcONSDDl0IgjXPh9pPGW0TNE5SRk%2FAAd7iPD0DeqX%2BoWKfjiF2HW%2BdySPyDULspxbBz9Qhuq6olhJZDGezeob5YTbhqgSbHuDvq6t40WmLgBkbSozw7sSc6qoY3zN0sCK4cXvRhnxY%2FJpGavKikKCJqXmsoMzjh%2BzGW3vUinlT%2FuVTgjO69uNXba8j5YONaAV01ZxTFxxk3%2BSj1cZVrIZT0n94nYMVPjVtKPwd8RAwW6VY%2Br8%2FVsLdhN0aV8i9L2ohGtO87IPRIxeJp7GzG77q9JcpWwn3SyVoFnN9ozAej13%2Bjsaj0B0zFLyGSGiuGhsBXuqtbTr4kvAHZvtjRwhnE1OW52Wz%2F1hWldfMKyo3TLFPZMeezcMFroCVS7PiCWwrIq7%2Bc%2FcClwNl2iCIOx7C3emA8OEfJWTbN6Ed0GCG90KDeqRMAspgn8E4cr6naM6AtE1%2BDxK8OnjPmdDR41abBCKWcAkDoGNJrxYbNcKiBDPWTv1dgUNZ%2BN1o4sw4NafvQY6pgE55fa2OYyuhykk2gDm7j%2B0KSWqdMBRF%2FntFnVlWb4VoYNsMrlMM10W6Sy89z9c4ATZA1DePAq9uOAmH60DR6P3UhcqqbTCU3HFk0sEBKP6BgJrf9qF%2Fx3Tzg%2BN5lGF9scqUFjiSwkBKYU1fqwmVV90zvhYNHuA2H4CXJHKRtJ7mK0cToA2eOhmOO13ePjPq1IXXC6UJyZ%2F1y2w6cEMnAf%2B7QTQjeXq&X-Amz-Signature=f8779e809339323ec228396204baa67a20d0c4450a4fb82924e9085795c0290d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRLFYXDB%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQvxnQIRwEKk%2B4AI6tQf3gsSKVT%2B1zkty7MZmkj4vcJAiBvZio5kPYrX6tkqXn7n0%2B%2BB1rwCSUDla2SvFgNH31H3yqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM096IxSPE7uuiCL9nKtwDrQsSzlO6OwTjV%2F4X3uEYkMQEj4%2B1FBQVfmiYJnEw1P4deYqFT8%2Bj14sBgeF1wshgRlHnJtTLa1FCbXgpYOjIFx13Zk6h8Q3jsbgnhV0zDmsEQPSUPQP0HnKyb9Fu7cv%2BozrHD9%2Fu2IyDS3%2FdOtdOtml3ma%2F5T%2B08xm0JPiU9HZoU6n%2Fo40PG2iUHJuttSYrDsVUJuP%2BVtND4FPryK03P%2Bua%2B%2F9g5YaAXjhJYaEyyJAlgOV6h53zNMX44vJdnasJ%2FUNK2prUFFhY%2FjEYzGpZtG6dWlOPo72riKzxfcTt6vGxgJinPNKnhgYYPa9i%2BU5iKQWu6bNlvno4btepIG2VnyfODjvdtbX2pOC1cRB%2FByCAy7Ad7Ce2sMHq3LxlAs9y539Q67qMOceaec6ZKI6YZHU3%2BRBgW7mhlz3KRlmuzbmduZZDPCNWImAJPwH%2FRnjFym%2FeaJ5we9n7xqBz2ZO9GMeW%2FDpoQgvwXVkR0wE9z089mQhxarE2LP9SbfgeF%2BuO3xCS0h7dUz%2Fpuslh0iPMLiRLM37BcUQo8SoGUN05mOClznz7riGhF3ERwW92CuCqT%2Fy0h29EGQyE7s9z51ZYdKsKfnX%2Brrj7ejwgsM24HeiVMa4v9jB8wbMZjgcowhNefvQY6pgF7o9xnMSysoxH3mn8pV3jsxewEpjlI3Neex5e3xWphpCBbDIPtQDCavai8MIqXPSRcV4%2BLHn0lkxpLhOZ77Ho2Ai2rFxv6UQVl0NsMyEmrf7JRUczksWZ%2Fm3ECg8VYR1GL9FO4LB02CMGfZFiepwSRjMkyrDKDWQzzZ6tgq9ZhSpTyN2m%2FIbC9EVoWw6YhNN87UamH%2BvFN0Rmvf6%2F658XA0QFtvB%2FX&X-Amz-Signature=73b97ba87fab90b6cb4dde545ad9099c0275780c214d722d9b550623ffa55287&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X6WWKDB%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBBHV6uNaeiBoV01AuZ8KiARxfQhin26loqIBsJOyjbUAiEAjPo3tM8kVaIu0yvMiwm3C8OYRkxSa6EUIy4blWq%2FsdMqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKDZc9tEIDYXbaDe6CrcA%2FXaQ72zGQq2j%2FZsslhuJOWKb80C4sEK3ck5TYzFnH3JNF5G96R2nZFYhdRf6Qs9Tq%2F9D26GWlcH0ZC%2FR6rqWSN8cc8sBh1hGai4PZCzQGpv7k0HFl2kDJ0nywX76HnCH4ApCZxI8csmQlZvCKYztg%2FtRZALon4587dYZzQw6q5OZ%2BP5SVFIPMilVIuLD%2F2K2sl%2BWRbjWGgPNcXpA5%2BSU1bTzn98Ix5x6Cj6%2FfVEH47Pes4%2BywapGfCHFGQhKo5Vg3GkEHZ%2BAYPxvKm5QN4sDKqE7SJ7eCkYyv01gvEsFx4nrUFxb9TLNUTBbRxsm2UaHuWi%2B6A61PZLyRe8t7DEHMfL8ilOv6B%2FtXXbxxzGXLDJ3ZxsuIXSacIYD8obtoG36hUZscczWSTwRgLTPFbzDsq77eIr0OFjiNsMjx%2BXN8yFxbTwE1RKpUTQJjHkGGtRK0iR8N50ye1UGOlj8wtLwJj%2FoYf6Y%2FFWYNfKOjR6DUchf1gAUgegptpuDmuBsHOteyh%2F6ZfYGkqyIny2TrZ3ffOIUUMW%2BegiN6IzX5IRLXgNX5U2gqOYLKyFXzcCXiHJFPMGJA6REFl0YVZvi8ZwWHodYeJjY2%2BmH4cRcUqTtMcSg378VQT0CcKNq3%2BaMI3Xn70GOqUBpG8YEzYn7jMTt2%2FFrZIb3Il4hsLXrw7NOunHf9B4qb9zrmrufQt%2BKvuaYs54N7OARvH7HhCypWFPCmOAmyQWFFHLlh%2FitmACdHuHTlplTT6jBGJauxNQptC0wBYi1C5VfjBacGd2gzRMbcTV%2B3i3bxe%2BhiuM6VfnGCo0wraDa2KGi0CUwfuLyKT195AOzsiaeq6FJ5s4dDM6m7kXymfG3k20sL%2FU&X-Amz-Signature=40065420e46254f56174f0da3d904b5c984ce395caa84ff4506b8e7a216d5645&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UQTCJGS%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHcaHzSVpcuep0I9PyzV50Zdb7xrynNGpVCWd%2Br%2BMNlwIhAKKXRgc9YpvbwfshhQYawUMhIk63Z0%2FlQlq0ViLuAu3VKogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4GnxJbrRk382MVNMq3AOtCbgaJ5vJ7Np9%2F3tc7wqit2GcaFmvhXeg%2ByFnNlpsdCn8PU8uiYRfps7og9XtkRZb5rlFvdwSE28bIfHU0OCymKktKrJd5PMdVGPFrH1ns7MTwH%2BPewZq7SQJIYzJl45qCL9muR2JIEYYPnozUSpWaFCyj9myOv8vq8AXYiKfgKMzkqZhe4RC1F3oVhmJPCxJOE7b51JfgwhKcl0wMpUFLPRtm197nMtt5NK8W2Om74oezC8XwivpVQGOYijZPy688GEuM4y3imd1KBZ1Fbn08dK7B3h6p5kci3htSuzaa5GEGYpoxkXDJFdBwdVzGZeeGBjuBGTFkUlt4xqtK4kee3CQXmq%2BssZAj8tEQvqmcnzJvN2s%2BGysJ82hygKt9CajM20PDuvrXrBW8hKTgZiIOhEqU2tY2ZbzzAVuZJLpT8b%2BTTzSh7Y8LIFN%2FerQL0yK81XhYNtS677WeiL4y1xWaUyKD5xMOeCJDTEJGIL3FE5FJ7Q7ScbYHEpdYcrImS3xdQIUxawDrG3wbiOoOBVTv3QpEaTilqrCxLX79vpqtFRKifTSmwsFzaJkEGgfO7LBuw4pu1IvdV%2FIcCfvPmMfJ9FNakLYkihKpnjAK0puUr41tYuKOUswbf05hTD11p%2B9BjqkATu78SDhxP5oaa0QnDdqjx449kranikvtvyXH8FDiENesA3j1RhNCKq59lujj7ap5r%2F2Z9Nuq0w89yld8DKfV0yq8L725tPoYceQjry%2FWNl5JDUg6gmZ0rzIdesIaG81%2FjeQFsbkjubBimC0xJhLQL8rrclzO0TzgYryzoudHildqsuVQT4xQNnABh7tZ%2BUerrYcoPSiRLdXeEns650mcQLvL2H0&X-Amz-Signature=790be63be7e37574bd74a6ccb0b3ae23f02a92bc3e16dcab02ea7e5e3b1b285a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPAJZUWC%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC52bo28UJCB%2BLDMrOyxY1CXmksTCAbxdicfCt%2FO9AL%2BwIgYlvgclL0q6%2FX17kARZ1T%2BPXeTpw8d3GbOyDfbH42cwoqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8DLZlodo%2Ff%2BSizlyrcA7g96ZvggeJgUGMCGD1%2B262DLyZe0kdIciheS9d%2F%2FTMh74HZeW6zSatg9JYB9vARWnqDaLNDV%2F6v%2B1Ho2nkZc3uI81ivaBZ8sqVMUzpZuwMGOC8B9n7C0GoopFtFqAbmFAOVEATb4Lqnheq68ftvOzj7JtJNNK4ACMQ8OCTMHxl92qyYqUJxpncJs6iyXe8vSNBRviesanUCbiD7o%2Fib07qRRerWO3pyp%2BWwCqDKzIUHvvaU1%2FzQJZw5zwi7R2x2TjP1BQEhFiB9MoAObExpWI9VZy1BBAg4GkmIPoGpnE4EiVPFdMHrmmnPmmPj%2BXeQNghmvygqHEF3KF6dsA8TRHg1sWLSvaPfBCMji5UhjdE%2FzTwcRUhBFmwjILj%2BwtkaMPdxYVYjfU0c%2FpjV%2FosEB5%2F7a93jdQAvJhjl9e%2BC3zlvsOTbV2z8Ar5lOBSTQ8mdzDPiLtgfnxkCUYfcVLYOHNXxOxDkQJmJyI55MnIPpT5X1ZudaBIz5axx2vrl63e4zkmjYziTyxJ%2FI32xkr1S97Xd05nEgQysNgO%2BK1jWSbSfckeQzOv5dPY5gGB7RVdGLT8lkztg0buZeBh24q70qRoq3BIQ%2FUOGhc9eqPoa6%2FsYFu6BCoRR0SurJ6OpMN%2FWn70GOqUBxNrgjnwbZGislkxFervL22OLpZsYGooCPpGE2pQq0xBJfF%2BgcvPo1P19TkzDbYWmz%2FLHYIS7NQXdA7JqLqwX3QPcF91%2FbhHIxKcR3qWO5zS3XDpmDh21UgBGl0QGm5QmN%2BXhN7MCKcXYt6JZC41asXk4R6qRS8a6oWvxZQRbo0plwf04I5nVQbTqySnYAGGDYXhOnTcWWRxyRBlf3p2tAl5p5tjY&X-Amz-Signature=c7d57a404884bc7034f6d3fe4e6da9099eebfd37fb72c00341f14ff8e2378408&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZPDHZ3D%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhGvW%2BRivR6nHhptasmwdTRFjohNFhCCTPCrIKf6CqRQIgZwErT8vmBj1NUYX35ki05a1boECVRQa7akfSN2eTLxcqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYxpV%2BGwgTq5oosaircA0gNTYrM%2BOw77m50eWXuW3dwNHNQidcoEAjLILqCEL98P%2FdhLVCU2nFYC2myAzQSvtP9obl%2BMDyKz%2B%2BxL5RqSoCbHUpkrmmSht0e1PpDqBtR6FiRgnXb5sCkcSXIYPxdmBWsz5IwMYxZxPVPU1eqrPOKTeFFSzv9QYH3Vd3DzLC29sx36rFatW%2FajpAAdXGnyDZIFYbVtTaMB9LWBLWyvWv2rHszoRNv48bDyqm8yaEESMSBiupXnQq44m2oPv2VAm8QCj4YlLti10UGuCTgIJncDuB7buOW0z2V%2FR85EMMZNj6plVLXFJNE6RoqSmcihfAIgCOG0oHzmbJlk0tZC3Z5YQ8fUxzSIWrAcLtJ3kXmFmKsLD7yNRaenatNR8bxX7onqETbKFmkNhKQzjoxUiDGrVVNp8rjWfW1IILKHVhDdCkwVKEPotgw2ZX9eZB%2BcCB8elVExg8PDlFEpuOINVATNm6q%2B3unJMM0dqRim3XmOuAsWLinPpVNSeTvF3LVTigU8GIJCgnaYJ1DUJp1FZv0lb0BPvSRfpOrHAcDOdjfU%2BBUh5ha6PxOATpVPIV2BhdsDgcZxf2ZMYA4js%2BHncr%2BGAFYuDOkZ%2BLfAZShz3KJmHggrtSIX8DMVXBBMMLWn70GOqUBSzFN%2BhiQGG8pRr5nlCjc5i%2FHc8e3PL0SRvbJ%2B%2BX8o%2Fpb5rkCqkrc2QtFGt7OBqlprY%2Fo0n9UM1PfYkV8BkmS46YIfOvjLFnpQy1xewhzAGclQEANmDqV%2F%2FbznsHEQpqSJLwLUx%2Bbnj0LouIbOF%2BmhQe%2F3cxITS2TjdQwuH7%2Ftl4shbxE1W7lHZe71ot2gbhr9DeY8xbXPxD5oR3ZsEitiRvLI3pI&X-Amz-Signature=af7c6a225d24c5f8ef296ef4c391031c36a1b8943c537beefb49bc62ce97fb66&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZ3U4P2F%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFWjs0PF7G6Jx2zDAAewHTzKQoMhCkpGupX7%2BNM%2BHm8nAiEA1D7MNLIxePdaMoDWKDNI6hTFIiQrlpTFQxc0MMrQGJIqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNIPc%2FEdTvcoMKaOLCrcA30RLjanjnsTXIVnZpULU2CT89eAA6EYDM3eYHzMUk86j44lhhjbFNcgsPfJAiVNK7VuL9xMfpeyOQT7AvkeAMrdWKVAz%2Fdo0JPI580oB%2Bufx50iLk%2BA56vX%2FfHhhOawl54pRrcKZ9Jvq1Lybj0b%2BMCSlJ3Gvk7mnpozWnHspj7f2%2BHO3zt6jl0NaYRZ%2FFCexNKwnzY4Mk9p60oRqHbg5X%2FEo0nhkI0oerLTiOcyFHBS0eL4e4hHL%2FgkZw8XAMM9K0S7LasO5aXLGeXIro2OwGpNWHKVPWymmp%2F5CJC1tb3ftJDPGEeGuaQnRP7CxlCagd2IqYRYZedTEvZk7KmzTuDtpFO7VMX4t82bpUjTzB6PEUnYg0FA4LR2pWlClWM58OfSNWZ%2BbqUhtqdeCm4orfrY%2FfKZRmVuzRGLvbJ0lyEgo9wc%2BeLL3JQI74TbAmcm7o6UnlydkE7274GeXmnaKMR0ZpjiXvimauZb5SEpRgIBuEYNadw7SA30aQzFpFM3QUg1y1dh1n3bSFlt%2FDP54U9mGrocDYgBATK%2FKJ0g8H5jVUr1oAM9o289oB3RPC9cbyQaMerjEO6rpkFDC61XJpzOPue6ZReh4l7PUIx8gJGcoDRInBSqdJdisrooMMDWn70GOqUBdMV1a%2FNgdkY0TbXbL9y0n6DKBL5t1Cx4BMNPG0hAGusgJTi446ZPJ03s99nMMFtaMYuMkZI09IIg6ilL9jzxp70OB6ti4JmQocjcUVuO2UfTOjTY6H7YcYsKwtCoRVshXSXSNuCtWH%2FRlg7Z2K%2BD8M%2FEjPmn%2BdMUGikANn4YSzYjbvECPzMTcnLwlyrxxZ68zPe6nmK7A32RzHV%2FA%2BgJ7sjDMg3F&X-Amz-Signature=b05a99f59680f2632836dd605d400596758221a19dcdb549a61934d7c9594ad5&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJJARSJL%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICTtMhAd8FtxZhFDEI9cjYXdk5oomiHlgQtMaqdEuApXAiBVQpYI9%2FfCnfvnUcxJXaOvvQZkCD2t4g%2B77oQoglHn%2BSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHtz6mhPa5rSA8WyFKtwDb6cWFlc38IXyOQF6jB2dT3OLylUPvC22ey9Kfwi%2FRVO3ElOl7%2F3GlA4VAJewsxgbqfoY7reIJAPZ7qT7fcxdtxRm07%2B8LTM2gPDi2ITeOIuDA4I2DCTq%2FJszhaFv2WijyHKXb4rl3oXnfHOE4p8ZCl9X0qQZ64237T2t985uC9YujaKuhyv2pVAxzdqwdx6%2BaOWt9qhzktFNe1KixGEa3oFDr0qMqy%2Fr790f7dJw0xcUICdwkjwKS9zfYmPrVQaI86D4IVyaITqLeBHLYXaAreogCJ0qgYLUZ9YJhKAfRh7fN8WwOLxaX92Glizt%2BY7JE0%2Fmo6lCPV19voooudanPEYE4ozApAmPxrtOMqFTe6oYC8Nweop%2Fsc8fG9cGG9g6o4yFaJJbOvffl2Hgqx74iw5XmY45lPelqwCWbHp4YEOv2SEbqsOXJ1CpW%2B%2BJCCo1OEc0frhcMBMO%2F8vSaj%2F5kFIt%2B%2FZtX1GV1XT9z3WmBdeBGxAOAL%2BagSq8Ezak6yVTEuMvFw%2FLsKYCgTkI2HVU0hQrAHWWeyK8yBQIPdjq4Uuibme3Xm0Mw4INLU7VapAie15C%2BX2bWrw%2Bd0UvbmXO4f1P%2Fdu16r40OP7Od1XNsw4pzQKS9ptwaHWaxpMwldefvQY6pgF0xxVUfodB%2FtCjoeU46jb56B5a32Yu0SOnIj%2F39vzDLTowykpPIwiEPsbSM7mvtwZjwQFDuCA7i83YE012T4%2BaRnVwZ3VmBNwDMcnWhvpEHuJFYKxlyxOl8Fj%2FlcoTY1702m4GPLcB9pT1nzRYydtX7dJRfMRP0o1Q5MJO%2BbESsjZIu1RIAAHVbjtiEZijrZbhPM9EQgLtWL4atNO%2FJlEu8V8JK63S&X-Amz-Signature=fd2f4244ec66b94844d2e544d94164472499dec34baecb735b994e38c5acbc01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPAJZUWC%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC52bo28UJCB%2BLDMrOyxY1CXmksTCAbxdicfCt%2FO9AL%2BwIgYlvgclL0q6%2FX17kARZ1T%2BPXeTpw8d3GbOyDfbH42cwoqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8DLZlodo%2Ff%2BSizlyrcA7g96ZvggeJgUGMCGD1%2B262DLyZe0kdIciheS9d%2F%2FTMh74HZeW6zSatg9JYB9vARWnqDaLNDV%2F6v%2B1Ho2nkZc3uI81ivaBZ8sqVMUzpZuwMGOC8B9n7C0GoopFtFqAbmFAOVEATb4Lqnheq68ftvOzj7JtJNNK4ACMQ8OCTMHxl92qyYqUJxpncJs6iyXe8vSNBRviesanUCbiD7o%2Fib07qRRerWO3pyp%2BWwCqDKzIUHvvaU1%2FzQJZw5zwi7R2x2TjP1BQEhFiB9MoAObExpWI9VZy1BBAg4GkmIPoGpnE4EiVPFdMHrmmnPmmPj%2BXeQNghmvygqHEF3KF6dsA8TRHg1sWLSvaPfBCMji5UhjdE%2FzTwcRUhBFmwjILj%2BwtkaMPdxYVYjfU0c%2FpjV%2FosEB5%2F7a93jdQAvJhjl9e%2BC3zlvsOTbV2z8Ar5lOBSTQ8mdzDPiLtgfnxkCUYfcVLYOHNXxOxDkQJmJyI55MnIPpT5X1ZudaBIz5axx2vrl63e4zkmjYziTyxJ%2FI32xkr1S97Xd05nEgQysNgO%2BK1jWSbSfckeQzOv5dPY5gGB7RVdGLT8lkztg0buZeBh24q70qRoq3BIQ%2FUOGhc9eqPoa6%2FsYFu6BCoRR0SurJ6OpMN%2FWn70GOqUBxNrgjnwbZGislkxFervL22OLpZsYGooCPpGE2pQq0xBJfF%2BgcvPo1P19TkzDbYWmz%2FLHYIS7NQXdA7JqLqwX3QPcF91%2FbhHIxKcR3qWO5zS3XDpmDh21UgBGl0QGm5QmN%2BXhN7MCKcXYt6JZC41asXk4R6qRS8a6oWvxZQRbo0plwf04I5nVQbTqySnYAGGDYXhOnTcWWRxyRBlf3p2tAl5p5tjY&X-Amz-Signature=e07e3b30252bcdb2c651f5ba77e0d53412437ce996b7a6dae87906d86f7756c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBXYGWAY%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdmcvbR6jr5fmmL1S06gONOmwjilD%2BifFMKR782%2FysHgIgfQNZSANwgt46TDtvxG0HfLu%2FnmzuGkptwduB9vZYl2wqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiPKPovxjUno1xItCrcAyb%2BZs0HXAVC79QaEt0aUSlMg6KG6zHD5Lt8AZfF41DpZVBHzbvG%2BRjaK6soV5I3%2F0n7CpQQyqdU74awbdlGe3WiQ%2BIqjtzlcl4vQqx7ivI%2BlEK1yZ5G81aiFjLwXJRsXJWesEJxBEoLVhJAVZHiok9HaJQCU381ijeLSlAwmc7vi33E%2FJ3xfwUZfrS13NvJUGwOFqGQdZIJPa3x6uhVRaDQf9rZaLVqFhOuvmZvlqAz1UI6aL1P79Oa1%2FLSWaoMtuiq6IaC2JRgpp4mnZHZ9pdVn6IOW0i45SeNMo8AIYg0cPGe3gzAcggLJrokT4zC%2FpB8YDYNM9UFiYQA0vpFErzXP3klW7o%2FYNWbv4%2BYJN50qcNZDkj%2FBeoPYncy9%2BXFJIEwPgRG%2FNL1nsvxAFwMo3HUmLCOL2Ow%2B5tIiaWYtpyqiOVWNWthJacrjlYcK5esNXc1tBcKxinmlA1ZuSalIqBAuN6gx0twQ4Ob%2BROLXBYqZ7z1DTgpfvSuR21RX1VtFxV6%2Bft55NzKaBVypOpjuIkj7gYk%2F7pIrXK%2BQUb%2BfgVKQO%2B%2BNp1WbegQBXcCjWGiLNnQ5fxHUP%2FRHc5stTchGwZ9OIHJinF9lRy12g9bZxuojodbHQyIe5LlDGNIMIPXn70GOqUBQ9rLTPvqG1I%2FAYxHMbWvJuOLsjVvN2KZrUD05fMZuRfWfxVMHU5MAm9WwQxQpY%2BM0nSTFfE53enQkIMI%2FQni3zWgFb%2FRJeqKsNSKn8TjLphZbpdabOlfRu63kam71w1ZYywA5u8fuZXos2F5iLeiosMqWwuHfW1a6k%2F6WCGTWPmTEGXNcKu2sZ2TduznY9OeoIVsoz%2BVd8B2LvxV4NdimJnqseX7&X-Amz-Signature=02a4c3ca3258ebddf457fa4e8ae5fd7eb0026ef149dc86f4240bd51bff61260f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBXYGWAY%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdmcvbR6jr5fmmL1S06gONOmwjilD%2BifFMKR782%2FysHgIgfQNZSANwgt46TDtvxG0HfLu%2FnmzuGkptwduB9vZYl2wqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiPKPovxjUno1xItCrcAyb%2BZs0HXAVC79QaEt0aUSlMg6KG6zHD5Lt8AZfF41DpZVBHzbvG%2BRjaK6soV5I3%2F0n7CpQQyqdU74awbdlGe3WiQ%2BIqjtzlcl4vQqx7ivI%2BlEK1yZ5G81aiFjLwXJRsXJWesEJxBEoLVhJAVZHiok9HaJQCU381ijeLSlAwmc7vi33E%2FJ3xfwUZfrS13NvJUGwOFqGQdZIJPa3x6uhVRaDQf9rZaLVqFhOuvmZvlqAz1UI6aL1P79Oa1%2FLSWaoMtuiq6IaC2JRgpp4mnZHZ9pdVn6IOW0i45SeNMo8AIYg0cPGe3gzAcggLJrokT4zC%2FpB8YDYNM9UFiYQA0vpFErzXP3klW7o%2FYNWbv4%2BYJN50qcNZDkj%2FBeoPYncy9%2BXFJIEwPgRG%2FNL1nsvxAFwMo3HUmLCOL2Ow%2B5tIiaWYtpyqiOVWNWthJacrjlYcK5esNXc1tBcKxinmlA1ZuSalIqBAuN6gx0twQ4Ob%2BROLXBYqZ7z1DTgpfvSuR21RX1VtFxV6%2Bft55NzKaBVypOpjuIkj7gYk%2F7pIrXK%2BQUb%2BfgVKQO%2B%2BNp1WbegQBXcCjWGiLNnQ5fxHUP%2FRHc5stTchGwZ9OIHJinF9lRy12g9bZxuojodbHQyIe5LlDGNIMIPXn70GOqUBQ9rLTPvqG1I%2FAYxHMbWvJuOLsjVvN2KZrUD05fMZuRfWfxVMHU5MAm9WwQxQpY%2BM0nSTFfE53enQkIMI%2FQni3zWgFb%2FRJeqKsNSKn8TjLphZbpdabOlfRu63kam71w1ZYywA5u8fuZXos2F5iLeiosMqWwuHfW1a6k%2F6WCGTWPmTEGXNcKu2sZ2TduznY9OeoIVsoz%2BVd8B2LvxV4NdimJnqseX7&X-Amz-Signature=1ec77dff539c0b864903d503902c35d3dd220291653c0f9c8717e479201a6a11&X-Amz-SignedHeaders=host&x-id=GetObject)
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