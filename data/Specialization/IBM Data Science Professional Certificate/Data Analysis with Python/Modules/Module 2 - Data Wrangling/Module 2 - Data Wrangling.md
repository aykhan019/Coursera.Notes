

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTILWBPX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIAdQV7ggtejcCCrGKrlYzNn54ZIWI%2BKjTu7wzpyFe3ZEAiA%2FELyFE%2FpsbT4NIFIdCgjRAis31s6fz1Y9W7x2S8qBoCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMukKEqOXt8SODnNuQKtwDqN9DIi2DkZCmBa5zP7zRzqNJwCZykSjRUSmSDu0bkt9Jir3xQotlVgDQukEHgeS%2BlgbKXbjnEzEUmyLOt7wfaWz8DZFwKH92ovXB%2BiJuGWvTgUYN1N5GZIZ7et2UsxfI0Mj5OhsvashDWdNOMfrpewWziS1LmrOrUizxXKvIXD7cTgVWwGYrWm5CGQ6fFeuxz9D5CJZBzhDAKhQmJ1fQBm%2BvPlVUuITa%2BxPcUKsldqbkwDjYarv8ifVWfYNDAUVTukaLXCbFBu74uxVsq1H8rIYj4AMCiHExDjWJqm4Quaz6JQ5rUtuzH%2BvAFr4pvqzyeh2gHz7%2Fz5b2wWf7ZeCoa05lYqDpuqVYx%2Fdei2Av4ZEJstJQTEDxAgbNYPcQF2bzLaDlxjswozmIaAJGKWRv2As8P1c0%2FGjqwkmcOdoBa%2Fib5IqHt5ADri%2F%2B6JW%2FcejfrS4kFeKn%2BBBK3kJU5ibgs4KkoWOyObRlbqQ6JPANDWtapaArRKSvXHQHqLredczsduAvg0NFUuc%2BbyUzjI1TbPGEFphUlkWFhHP5oByNhwzNcXYLS3f%2FY%2BOcVIdJNwzespdjYxuehMvJrvHwEhoJGKcQ37%2FBnDEL9cF1Nzhs6r7kDCbK5ma1T9Z82OwwgOjlvAY6pgFv4IXt2M9run5kIz0I5jfFKWyAW9yLNY8ShBkb3YtA%2FxdAGF%2FabmGUY1dL4QGFiqnwSuF6RS9vfpa7lMn8tK%2BzBK4tOoJq8ZehBO6lTRlvAbv0l3M22O1tizrTooHeupjeZosFQTQQtMMBURXK2aKodahBqo%2FxYh%2BoN8B1hYsd1rMh4E4M5VofVf8kxs%2FMVBrw88UXJDcNPAmjY1658GUvIlcQQJHZ&X-Amz-Signature=97bb2310fff07a0023e7729892cbb83224947c0691500ce42697a8210198d09a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUJMRSER%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCICORR8rEsKkKIr87OoUYvWwz5qSlDJLWYXR%2BKuwA84GxAiEA8jf1uB44o%2FgNsnDvnnbwdD%2BzPVSsK59P7k2BmbAMjboqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGoMsmvxqnVQ86Vn%2FSrcA0tlE%2FKAxQWBZSS0XwQGvlHXq7zdPFtPcaDouSUeIZvyIG1dls0n%2BhltupTuQlyc8yYjC3K9JWOxtmaZ040tcO8h09AfJnvFulIdQcc7z6JB%2B9X7rdD21USMcGvgJ6YWfEGIA0MGD4pADe0CJ7eyLzOxkRVtCow3sbirt4ibn4BJLyr%2FJWJR6tsVKAKG4R43xFTDo%2FhHDMQa24Ga2WmmioYVbNzy%2FtxyIWYL0E0eLOhUjCAwEk4yaQ6SqF0YeBob0JPSFWZqo6UV6sMpAd%2BoIHjT8BApDXg4T4v275XKvVxaJ7viZMYZiKIrtkNN7kirpGWVVdyu7c9afxA7bULSaJWSTLN0W%2BjnYgB9KCAvvtLdDIyI64Ak0%2B8s%2BvoBDZzp0I2HJg7UsHTqugTJTzaGA%2BxIAGqB8xISvOiFO4wri6jhsOTDM%2FRgwkusRLEhnizesm4q22TvBxSUBZZDJfohx1%2FW1be3vuLoFQ6TjLk0ydWnbabQDEcN5nb8cr%2B9%2F%2B2pjbIPVrpJUZZgr3lIV5c98YvqVj94SfkXcOFdXnj4N87cbly2adzeLsM2CzZb01XW9tKckhBdfWxFPWHic%2Bene3dmS7issLa8OfUOUj8XzzwlQzWMnpyzJnUJdq1JMOPn5bwGOqUBKd7DWqt5W9Oupej7yzVTwqq%2F0kEujolkeNwSE3RgxVEAo3b3iudi7FUCanjue9OfQQBWYT9kmq5BGKWA2DxNf4h2IR%2F%2FQQlpulTO1e1EX0hwhJK%2FNQK%2B%2Fr%2BdiP5oPtYDh9Xbl7mORgtOMgfNaDj4cAYbqsCA0UATJo81C9cDXRcEDOENu6kCyM58H%2B6%2B9ZN6lhbCeAmmwha9%2Bof%2B5eoMZA7mxJF%2B&X-Amz-Signature=19deded3c53d2897264e0510051a8496acc71fbd0853679b0eb5d0052d1a76a7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O7E5BBV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIFNwr%2BlD4vwsSqGkQ25z6ma7P82x%2FyAa5cnitz%2BUZFoCAiB%2BQSznm%2FF2k2LTLKReIuxGG3IKhCG8smB1i2JEZrqQ1CqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM83LUP0nrFszy0jFUKtwDewWDW1C5KDnZII%2BzKccuyzouhzZQL0WqIDPZCQxmLrg7dFJNPTf81w8shHR8ffwrF0VxvgX2Ai%2BDiG74BDwRlsa5BzvaZ68BKQb31dAlAzl%2BVfQQNQRe8Vod0jFujW4qlO2iM06KRIYY8EsUucERI2qGjoluqbgW5ykAVI%2BeOFPxGeEvScezHTrDnmGLZJNeKXkZEW9ns5pfnqV%2B8nDJjMapOdW%2BvYV95SVhrNNkH4EtUz8C4G6%2F4a%2FhFRD7rvYpifbKaQabvq8ybMohTapmA4xaJSSykOnVbVJTjHRjX%2BEYdKJ30haeuT3UgpYywkldnbS6bCcNe46bulWRyrSvU8MxPwPyYIJ6zwHvkMwjUr7pDGf7HrklkSxM%2BcnBVboRtd2wY03JzLgJ5CHnDxhNDT1tt5HR1zCE2Kob0QlfJuWhUriQAC%2FIHl0RCd5tEetm%2BqfBs%2FOC%2F2V3mHz2qj8rUUqVXXztZaXELO313GnhrO%2FrAPxeQYscKm2FNQAC7kZf1%2F5hkt3VnBV7UjSNY2y1h3AjLNcRWC%2FdIJeMgUAO1eFdSc%2BMTooKhuXwhdellwidIaxas9iH7LLkp0vIjq%2FBKReQgg7ybQuCOGcXYt2ZgKvgEU%2FLTUvzYfrVyDkw4OflvAY6pgEpmHpYaS1nqDJdMA%2FDLNy0rHNFOtdsu8bzNOIKaAOSMqv%2BmHZqLGpXneE9pmLyDr5GmacX4obBeqkkHJzttmQHh%2BGTlM0n7D7qGLsQCrXj5MztxENpC%2BgyKAUC73Xo2lH5gauMQSVVCFuKZXCPe6X44n2I5QyXD%2BzhsKX2MrmUE5k7%2Fy5ucywMrXFD9JTKzW4ckWjnCA0nDpIY%2BC8fAigoiP5flpMU&X-Amz-Signature=a68e266509fd794732d47962b157023df0ae6055433edf5382c5a722cf9e551c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HL4N2GU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQDMIPSUz6nEDbRUFbUg9YbOIfGiOUYkSZ%2BlAc68ABOk2gIhANImu9voBzegTtgk0VsB%2Fn7R0IxWGZuBiQVcAPi%2Fq69iKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwv6%2BE0%2Fu46%2FYncTXkq3AOWQyTczE1XOhkj7PMRxYigK7ui0T4kpWILLKpIUAVxGcAfolzS3PF%2FsUuJZyXpJiSk4L8TjZRoW32BTHD9qEV9SS40ItWKfCCUqEAfumaKwhyIfmCmNObpftrt5MQ2an3ZkZCNu5EozT%2BrxPwFX%2Bl4KHAy0QEaUm1phaNTDHArYAk5SKoxbrpFUHYhKPkSm2e8rg%2BqClhDUrAPFqm%2FoMrzMhpcUnXM3OVBvwXtDhv2yGmIgB59ZpgkzYUjycg0AZKtQjR0mpdNVh%2FRnEzwpWoQCvhLCWZw2CxEQJRBL5KdEXB1lohGrkT4z5xn4indTc4tZsm15Kh84oIFmDPpsm72V6WZUd5XMPwSFgzz1ILNj15E3dIbr0ZXAlWgE5bo4vQMk9NZtnpkMy20Jhm60g2Af9iR00OvV%2FrrSPn5UexoBl7tyrYog8FxEYGppsNj5blhmukvK6bryibUrZMUQnab%2FMCWojnTvRwWwiDj2WGjeE4BSNCZtfcOPKVJPgkhEjl1BA7%2FUg9%2F5gX4M6d1xIt3Tb%2Fm9Za%2BtunK8%2BiX7R2u4fTVO0iKKaLXCdDZlGOhKqV2gdaYFa%2F4GYLnKhO7lXv7j3UJdJ1rk%2BnnX0SB%2BIsVa0GV1Eea2fLb4CVw8TDs5%2BW8BjqkAYtS399GbXQJnAmGBtqkV%2FJxSzEew0gyMg%2B70dBlIL%2BA5UPkhbA0maM%2BVOPC3pYO7ELe4Io0tVezvdWUA420vIT%2FDj7QS7CnhK%2BOoMnd3yZ9rLLKExAUI8gpe%2BkeLGsAUSVxfGlOJeM7P1kiOvRUoNLmqde%2F5QJxrz%2FbGz%2FjWs4j6XHodhltQKPkQFezR36Nya1bzIM6X9DK2hQwPGatsshIWofY&X-Amz-Signature=4afd3f2b5b18f49883f46fa00e2d9c3ba02ce84ea3a76d4e7011b07faf069913&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2Z7ZYGV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHbZi49g9bZ2s%2FVW1YH5PfsrN4oZPyGwhIYghqbp5APlAiAs5qPaqXXk2flIH%2BCxdA%2FNmIhpkBWFU4AtoZlco8ONjyqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpSUMvm4acLgKExa%2BKtwD3DGY0delcdzYByyv%2FfQqkPCJJYHAigGUEkxQJhu0KJAOoMo1RWMMASGb2peBYgiPFqCk%2Ff57Ej2HJoR5l9EFSPo%2BvjceiWqoNEl2ieZUg1WrAmM8Jw%2F8wjum9fQsLvanUS7HE%2F4vVqh%2BFlXLHP0%2F1Zetjft5DCyQGqLzCd1f2r64yZ8Bjj4SLl%2BSW7%2BAqSowSAXMgQFRlDV2vhuNAK9dTWz1p3GQzHO3x0qTHQsgLP6R2MrIuqkdyyLYjXOweTAMgR5itGykAOTH4MIXkljcVUbxjJMk9pHBf%2F3k015vcqo%2F7y7kN4EY4fpBpRhzPdXZ3fi6xHRLHKI7%2B1hdUbBYQzLaRbGPTCAReGUGS0YDOr4%2FK%2BmsJTL4Z9BxQuzLU0Ni92gJxHVM54ylwEzf2xsDCjqNahFiyR05QbPdpJTLeNDeSJ85D0oOD9GKGdNjmUiSd0Y%2BgEZADJgDYxoTqMvYJfg0skKobJwKhjpbOdDBNzbjkViQL3sb2qnvwcADTdkPjeYkzIQm61bAZZfpIfd%2BNmyWsoFCbinHkevldmQQt10KJKXDSIgjEEvDXKrN77BjR9uK7cbaFR213OVf%2BkMft8VCcf%2B1LDI5jbZFNoezRX214sosUMISSX3oowYw4OflvAY6pgFwzjHuQmqejoOmo2ocDBVmq3uWxXCqqdAa2%2BtcFPf9jJ%2BtmM7Rf9oM%2BtZjWzdLJuh6Chp6LJL%2FkE8GH9Oby4Ra8xYnmeMCN4BqMfEX2uEIpIbv0UhKVLvzYxvgAhhQICh8AKUfGvvgd6cFXjy6MjMihNRskAFjQ%2FIe85sUBZ2g85EG1XJiYtcBJ2VIy3AhC6TM4PiXlNl%2FBw8iWHsjMPHVWFcaw05e&X-Amz-Signature=6bb6b8a27d9557d44de21122d4e35ef3f902b2d49de7934ce78b5d86b905ec6f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVPTCSZ3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQC26ur1CITiX9ok1LuK2QIYfnFr3gcdjAhB5IEI%2BnGceQIgIpoU5Ljm1CZH04y8fNog3fguO%2FqKaof2nNESvkDpcCcqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhyWI0Lt0vDol6LyCrcA9s27RLy%2Bm84ZBZcjQump0ippvjs4o4TC4x1RSIj08Z4E97Fh5wb%2B6uQ9ouPI4b9KR4LXLm4zxsnBONgI7LEHptz9fXE04F6j%2BJXg9vwh86zXcl7Hg82Gh0gfEiyPT%2FNTKrJH86QtyCONOVpA6mW4y0qPMe6sGzKW2dTUBf9gmHqu7cPNtRVRmZ2QDW%2BDPttSXL2%2FCV7MYaWY4gZgrYO%2B%2BqCzDbSow9ayBW6LCQaIRY0a5WKXI2G609gVdCqtU2TQDVIXfHkl%2BgX6a6SH7z4i6XvhdeGesnoBEqMua2Th2KGoeHY%2BS%2BpoIzhVoblhzrmco1drj4cq5E3OODzvT5tDe4VyKmrf1BA71hmEh%2FqkkTnUH59dOAQysC9eP7AQUUvWFYV%2BgOdbhRIVGGiCDWvhKCPbmMJys%2Fng97qv4NRItg20XRGGT5MyAhbwoFJteYtRW2q93Gi5ff0cCJDCmqzy6%2FHhDW67smR%2B6zXFFV8A%2F%2B%2Fp5cmtkqtlwyVnFwohUsyUqJ8%2BuoPcQ3dnS0nKT0z3EQ0MOR4yVfgIH5tSPoi0DicJJLFBAEoJsxEdm4jQtlz487Yb3EPUkKjrXDpmBhQyES4gcKpp66ID78GSZaxmY3cvYPeXTfUYSVuZWe3MOzn5bwGOqUBojsxrHFVlSfCTBF7IEWLE7rRmNnSdfmV26ypki0EC1lW0Pe4ymb7jVLpjht87sSYmVKJLC5s2E52UnD0rSg90W8Ckv21JtmIh5wy7hbBK3TZ3bwLQKjpkAJ6oEQeKRpeVAVlL%2FN2oGBawHC0SnzKfos0REjoMNCGcHC4B%2BKJmAGUB7zq3bGKFlXUgC9yOBQtZ%2B446ulsrtBUel7Ri81vTyhYCEJY&X-Amz-Signature=543632a10cef4a03ba4b8e1388dda6d4ac5d54ff34ee6bcd2ea06e88956ce42b&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD5DJXWS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDEukyLC8RrH6uvgpIfyP3OyG82GnCrouGL%2FikwaGOINwIgTroczrV1DVA1tb1TuBRofprh9tAQfDXt3Q6W8uC7a0gqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJO%2FZb3%2Fhv4XaZHQOCrcA2%2BK1eMPOLQRkbRzkYOnwKMyGe26EImJjLLeikxwh4ox30R%2Bcc0LDRvpgHe4RwWNjqinRGQwC0MFUMVMoqra%2Buu5oW6u%2BGA%2BbTMCFvP7D7W8I2KtQNsxxj4iH1REXfGakgCfldb6drerZAM1lIW9bTwwCwton4cTrl565M%2BjU7vB1NfqypwAfdil1BctkniHAWaDoizSZc9YqHMy7n%2FrgbLVUQ1RREItk84f4wMRyj6epPTRkqSsbq3iX4QAVZiujA9p%2FDtKBW58%2BT%2FaL4pImdDiNBKJ95lSj3Bsv%2BRTNbru8DxabL3yQP%2BybV3akdwteMxdMtH5dumVt4PtBfTUJiDJ%2FvPsomSsRTcnNh%2F87MbSSO3FCNpP2zfOLxbKNJ%2FakyA6v8YTD3oYmTbgccuonG57%2BBmesbg7gJF3lFz00Xu%2FaAdIjFFcftlGhDgDVLPl28NkUbNZXV4U8clFxb1zUpqV4aXXY95achTwhIziBpoJ2rhsYcEdLDOStV9c5NlU9rzuJ9ZxIEW1H4n6faNLa4G5pXsd%2FlrXQHYXMjAD%2FfvJUCa98v4LmAahpU%2Fu3dmFWs9QHCU%2BXdaWBSQLs%2BRih%2F8iLbNmnmY2blbsgUxNt6tNQ%2FKCq57FoW9QBFo6MMPn5bwGOqUByJukEnRlrxfHdKxcDkMV4iBMmNEKnTd%2Bxgn2xGhAIUcHIJzuijTILyb1vR8vIytoMIzuO4zDtDOlKPmYHAFQKf0NjOC%2Bc5rslJzWGBhD0CFH6E3Um6zsolXdknkYSr%2FV3f6IpcVOe7EXcrDeMIxwHjxNRw1OIYVRy66u84udKrJLIy%2F8lWMBIeGbgpdlnj53hm34Gn4A4DckBYR5YwMdFn7TeBqO&X-Amz-Signature=16c38d1b5059528c55a840beb3f621eff5e310698837e54c5c44eac998e2620f&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPEPIIW4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIEumTiglHuznxtEUXshjPgv0w6XFNRxc2WkZ0PUmmKu9AiEA39O2WpEC22Vo4hPkJH0Al4%2B9AeKCgUVS2OZvlGFgZYkqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9xrxMx5PHe9R5o4SrcA5y7rC9Du6skjfzv2Bt%2Fm58Bu1bZGh2%2FcjJyWLsqBYsqyy0cCS14KZEJA3ije%2B9XJ5dHgCXnfKy9DTNKedI9USrnczSkEXI2tP96uFJtvoLRP%2Bx93EBpOQ4o9%2FguPOZ4X586h6gAIUqPidAVHbW24xYow7TNf%2Bfs9z8sBOdvY0q28On99uIwdbCd1oqRSHVSG%2BBgaCTG9LUBCGpcoC9dPsM0NFFwojEhnX2QpfU75apqQbaiBbbUpQl8sUYuvXl8RXmNMVO2gRU8V6uL%2FGzSdUCu%2FiYAF8SjoN4I%2FwpQ2ID6jvT2xadXCc0Fx4%2BrSAAHX0w0DDzzodidFq3gOK8TMFEZEJ7vvsUq9PPMfcuEYsVQAXnEhdjUtNCu3kUIhEXdUZ3OvCeAWCkq6AnMF%2FKeqNHYofn7m%2BAmSr9462q%2BIrKkNrCgmmthNj%2BixMTiI1XYYax%2F9re%2FIjEMD1FjSDplr%2FozNtImnTeHZ3fJrt0vZKMwWVirG46RzT%2F6MXh%2FRvIzRG2KYtLqe0Ux%2BtOryh9r%2F1JakJs7oHRXlkjt2k3u7%2BBf%2BtUn%2FH1eg3fnZ2xxeQhvKTL6u8OL%2F2gUqqgG8KexM6FJEZJy3hppEFlklcjTkouCp9mpexys0wae4vvzMMPo5bwGOqUBdeT4GFS0jgK7Fzc6Z1NyTVxj1XkGkl5sIlDGv0ITYg5uk5f9%2F6sBposXsdNOVmVYpYBt1JKksZDrs%2FiHyPXJcdU9QXsU6Z5mcv5KXNyJKn0EYx2QDs4Ebqpn8Ac7ApRNuBiaWplisT9pGPAwhozhocX0JVwsbpx4rzJ%2BPf6ev5bOFNIlflOehocMhzrU81%2FDE04PtjVOw1dFOILW1wmTAqHDq5hW&X-Amz-Signature=6005b0557697e234b0f0e4e184f6c94f6168d2db2d679715a5fbd7aadb482dfb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2Z7ZYGV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHbZi49g9bZ2s%2FVW1YH5PfsrN4oZPyGwhIYghqbp5APlAiAs5qPaqXXk2flIH%2BCxdA%2FNmIhpkBWFU4AtoZlco8ONjyqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpSUMvm4acLgKExa%2BKtwD3DGY0delcdzYByyv%2FfQqkPCJJYHAigGUEkxQJhu0KJAOoMo1RWMMASGb2peBYgiPFqCk%2Ff57Ej2HJoR5l9EFSPo%2BvjceiWqoNEl2ieZUg1WrAmM8Jw%2F8wjum9fQsLvanUS7HE%2F4vVqh%2BFlXLHP0%2F1Zetjft5DCyQGqLzCd1f2r64yZ8Bjj4SLl%2BSW7%2BAqSowSAXMgQFRlDV2vhuNAK9dTWz1p3GQzHO3x0qTHQsgLP6R2MrIuqkdyyLYjXOweTAMgR5itGykAOTH4MIXkljcVUbxjJMk9pHBf%2F3k015vcqo%2F7y7kN4EY4fpBpRhzPdXZ3fi6xHRLHKI7%2B1hdUbBYQzLaRbGPTCAReGUGS0YDOr4%2FK%2BmsJTL4Z9BxQuzLU0Ni92gJxHVM54ylwEzf2xsDCjqNahFiyR05QbPdpJTLeNDeSJ85D0oOD9GKGdNjmUiSd0Y%2BgEZADJgDYxoTqMvYJfg0skKobJwKhjpbOdDBNzbjkViQL3sb2qnvwcADTdkPjeYkzIQm61bAZZfpIfd%2BNmyWsoFCbinHkevldmQQt10KJKXDSIgjEEvDXKrN77BjR9uK7cbaFR213OVf%2BkMft8VCcf%2B1LDI5jbZFNoezRX214sosUMISSX3oowYw4OflvAY6pgFwzjHuQmqejoOmo2ocDBVmq3uWxXCqqdAa2%2BtcFPf9jJ%2BtmM7Rf9oM%2BtZjWzdLJuh6Chp6LJL%2FkE8GH9Oby4Ra8xYnmeMCN4BqMfEX2uEIpIbv0UhKVLvzYxvgAhhQICh8AKUfGvvgd6cFXjy6MjMihNRskAFjQ%2FIe85sUBZ2g85EG1XJiYtcBJ2VIy3AhC6TM4PiXlNl%2FBw8iWHsjMPHVWFcaw05e&X-Amz-Signature=2d1e3f84f1c51ce8c337ba70353d3b79cca23d078883739fa5f6d9019d8bf3bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEPGBIB6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIFTInLNpQSTxBwITzg1WIWCqffZa10wQe2amyQ7BgZGlAiEA%2FgL%2BmkT0IeBnfw8TlAOxyG3kKRWRpWZzRW73FhAuKAsqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAyCm%2FT%2FMc%2BBCEy0nircA7BFIlrXfObyagv2CmpBom%2FBPWVqCw%2Fh5pcGa3MNrK9EQQhgbH73kpWXALun5TNi30VoYqUaYiU2ZIz526eW7fXfTfAYNpbTIgRuGTE4pPJMemh%2FCR7UT1tB39nl1Wg72rKmjkpAheA9dSwRtymcNeP%2F33QsjbgHAV9ElyqPy8Pz28ypq9WRdxA8OxN44hdrVSYTb7qjdSv2j9fLQjDMqDCe8GhQM0sbNw7P750pct7mvga8JW8JxVuYzUcvxcznjS2wMZI8LG%2FjO4GzrC2f2Ok6aCfwFs5SXQm01xiMf0QccpxEqqRxZqrwBEkPpFlb6HDv3a%2F5LWybKDT9%2FBoiGd7hB7KpveQsU6Ae879XKL8o9kCG9WOViNhgvZoIdTEhpaWHo2wrrOGMZK7ohKGKQWc28kvq0nUld3V4yjxKcPudbMEAzlzPrZ2vKJpI5WrwlTZq6ipbX1rykm4Bxz1RXwL3w0sSzpzbiPyQXZXwNMz7v9e0fpzCuPLL%2BHUD71MfwZaMi9AI%2BWTClJXWX0r5rudHggeM%2FYfpoCluF3ypjJtZxYEAJj8LyLTJw%2FKcSog1rp7s5cye%2FNJggDsIhWX11cK58mFXMFE7aNHwuzWfPDON%2BEX6GMbPxApmsRWrMMLn5bwGOqUBFZsrQmFnc6VPQ21WEO7QCSz6uJv8EO96czaw4f19d9TtKZAxMtNBEMuQa9hVGNAbPf6uDco5KnAxB1ClVoFgawl0GDPimkYNla0Rh1gp%2BuguzBuuZ4sK3tNrhFxDAWbL45HuV60eTXOsxwWHqQW%2BVyzgcBDGU7y%2Ffuhoijy5wjk%2BZlvbDnmll1Zp1pjjW4mz9IzuisjkiJJQay%2FA7XPYY9WO2zau&X-Amz-Signature=41acafd08271fb644a8f933c912af479362b6a70558ba2576ed6a827b9b984f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEPGBIB6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIFTInLNpQSTxBwITzg1WIWCqffZa10wQe2amyQ7BgZGlAiEA%2FgL%2BmkT0IeBnfw8TlAOxyG3kKRWRpWZzRW73FhAuKAsqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAyCm%2FT%2FMc%2BBCEy0nircA7BFIlrXfObyagv2CmpBom%2FBPWVqCw%2Fh5pcGa3MNrK9EQQhgbH73kpWXALun5TNi30VoYqUaYiU2ZIz526eW7fXfTfAYNpbTIgRuGTE4pPJMemh%2FCR7UT1tB39nl1Wg72rKmjkpAheA9dSwRtymcNeP%2F33QsjbgHAV9ElyqPy8Pz28ypq9WRdxA8OxN44hdrVSYTb7qjdSv2j9fLQjDMqDCe8GhQM0sbNw7P750pct7mvga8JW8JxVuYzUcvxcznjS2wMZI8LG%2FjO4GzrC2f2Ok6aCfwFs5SXQm01xiMf0QccpxEqqRxZqrwBEkPpFlb6HDv3a%2F5LWybKDT9%2FBoiGd7hB7KpveQsU6Ae879XKL8o9kCG9WOViNhgvZoIdTEhpaWHo2wrrOGMZK7ohKGKQWc28kvq0nUld3V4yjxKcPudbMEAzlzPrZ2vKJpI5WrwlTZq6ipbX1rykm4Bxz1RXwL3w0sSzpzbiPyQXZXwNMz7v9e0fpzCuPLL%2BHUD71MfwZaMi9AI%2BWTClJXWX0r5rudHggeM%2FYfpoCluF3ypjJtZxYEAJj8LyLTJw%2FKcSog1rp7s5cye%2FNJggDsIhWX11cK58mFXMFE7aNHwuzWfPDON%2BEX6GMbPxApmsRWrMMLn5bwGOqUBFZsrQmFnc6VPQ21WEO7QCSz6uJv8EO96czaw4f19d9TtKZAxMtNBEMuQa9hVGNAbPf6uDco5KnAxB1ClVoFgawl0GDPimkYNla0Rh1gp%2BuguzBuuZ4sK3tNrhFxDAWbL45HuV60eTXOsxwWHqQW%2BVyzgcBDGU7y%2Ffuhoijy5wjk%2BZlvbDnmll1Zp1pjjW4mz9IzuisjkiJJQay%2FA7XPYY9WO2zau&X-Amz-Signature=5aa0b2ed2e3b0f8c4810f88ef13470d3e6fd867fd0e5fa25582deca1dcc6a077&X-Amz-SignedHeaders=host&x-id=GetObject)
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