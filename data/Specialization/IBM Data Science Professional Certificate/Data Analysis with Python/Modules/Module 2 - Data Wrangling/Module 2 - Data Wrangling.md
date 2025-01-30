

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LYTKQSM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFjKD95PsWAMNFFdcxUbxA9pbqr88BV%2FUXbDjShgwqy5AiB8jNwvQiRffVJO326SWARVOQHRQmMdVvuPoWRVol8BCCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkRIgSAk%2BbK%2FnLAIzKtwDoyyrY1j18ka3jbXrrSTWWbPE89w1rbEQ9hfXa1HOlY2%2F9KSroWWplK4HR5OC3ghT7HpwKi8H58ooN2WVYZT1VPBA5ZLAXhzQkpgYXA%2B7bxiVjbSHNu0fwPJo%2Brm1pUzcdPhqwy7Q2qmLAgBbqVd5Zr0O9581WvdxS84IoKV6Y6rJlc7s4wsA1TohsdSpnQfLPta9iECmvQ9L9lSzxHqZl3cTExAJdU3M8J5Qmj1k2GLyverH4e8dO8i6wklawNxCexO3Mb1n5unBTAy2KlFW9aHTcROZwulW%2B3jKYe71pIIymiz%2F96gYpiA0WqUAR6MJxhEzTgeuovG%2FN11NK4AItC42GAH%2BKyJCLJLcoX4pUm%2FAc15VH75cijN94JXmCm9wloMeR5jEBv%2B%2B2gVXNrt1%2F%2FSUTwj97Tx7PjWDlaJ9ZWe66%2BZk%2F5nr4Fn7oz5THMnMmsl1OZu0MqYowTmYxT2OqfEh4rdLs%2FvY4DHVi4S97qP2kPgFlZuHh12gBbmd8%2FChFmy1kg2plC%2F8tVg0fB33M8f92VCQZGhJP5c7JtmYrUpr%2BByuMlA8dz%2Fwh2jKo0fs4L1nmHDr8CzwjRQ97mh%2BEUlItUGvUtzJACT%2Fe83fuFUR%2BR2GKEzIISGKvw4w8JbrvAY6pgFlgPCq6vPDpm6m%2FmwO7lsJeZgqhIHGkBqROSNnZC8YkftwWVWbiv3LcfXFUXJ283vIae1nb6Y5KTMw3hhogrg2XgMbVcNv3OZiCyGyEsxC581Wbt9KFRWP6q%2B1eDCwiOSUZQp0bY5qYYysfjFBeWhZbGCxNNFcMtMY45v415ve3XdqFXrxUjuCygnrLwEvE2pJ0YiwlT7NJDH1Y%2FIrzzjemDtzjvh0&X-Amz-Signature=f1851c5ae2f71c3cfa2de1e66df55871b9941fe8056b340d9e685a751b13d7f5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RJUUVSQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJhCaqTb5gdYhNvU0v9cDhjdbWzSEeC51cAmr9XgvyTgIhAOHo7vm9DYSTFMIWOu5vyD54GAut3kONgVFH4CQ%2F2BUXKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwneAU9%2BljexgtFlXgq3AONiKfA2X6AZ6HNmwGAmjU5SjtpG%2FDgG0MUHq%2BS175o2g3cK%2F7hwmyD1haFmaLhETase7WXoafb3ssdr2oBHcIObbT2m%2BQIvEK7NOW409%2FqErVIEUN74PLZFJQ%2F1Cdt7Lab1an8VE5NrTQ6xsZQbtYA7FxlGyYJG9VgfmpX%2BsegJNgJb7yoj6%2FnNBZos19rZjdv5HPFB%2B4tEdHiKNlQSd2ClPBjmUgNNWrspgaEJHAW%2FNgcDB6i7Wbaj1zOHAq7B5VdOGut6hH%2FtmwjCBujwinqWC6UrW447zEASP7GjiS1KEyTJ1daXJO7p9pIlrkRlru3CaBZ1%2FUYIlKJsEaP22TUvHy7ykeokhyI%2FfqJTo44vZCojCfbabq1CQGSQuPIaucKKLvx7pBHvPsvNWpVO8AXrSX1byVTc5wL6JdDOoko%2FG8jlzOGWukcD9hkrfP%2F9FlahLMxRvjZIQX6xkMhUeI0zpt3Uxi08LFs%2BggML1ZhWEa%2BPtP6sC3rsOBkVGxgCrd%2B3BjbF3wZnIViEok3JUQZOczhGjy0tI3jxLRL2NavdplzN15txP16vpHgE%2B215dhwLIHd%2FMvFfWdDuN1TKCunUtRblYn6aE%2Fz0gxXAiEl4XqY0Kb9WmTBOe0cYTCyluu8BjqkAf%2F99qLqhFWNZrrWLlU3jMlYSCq8rULUykZfWJ1b%2FoC5Rh6u5SmdvkWj7KjOsP9JLpmouk5aMRerZPtiGw4RicbZ%2B3GP9WIdRQfu4ekJseGSivjsoVTbUFV7SKaejjprDEpjDnNfBFHL5KX8Xo17H98v6PuHtobIuo8pLellIYXaLLM0DXUdQgypw9UQTyeqzDZeW0LDS2Fq%2FG7YNGtX%2F6HMSOv2&X-Amz-Signature=30de55260b9bcf8f1858474afc4a730690d47eb906fed3c0c3d8c1f3af9e4ead&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUHDUSDV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmjL9BIO2Bg4KBR8zYaMDa6fpYisqwHreT2%2BozGVPj8wIgSkp1hgkVrPqRZdDI2zKFDIWjOh9g3511y2QAu5ga6mYqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhzCspaMkJAhnzXPyrcA4Bb6AnGg5VfAhIsJWzYR2y1zs2rFZYSnWniXsazyurshqLgTBpbpdwrWbnaywBJQVTs7ddG916UiuGg%2FHjr8gsiXTiKjK4PInrOtEnuIWYgDnU0iOaI%2F16XzRC7AGIs8zt1KiqwX5zMCHSjXZT2kdtQAdBi69Z2Adoj63u4x1HYqD%2BrEyeS%2BmbTOg23wESlNdRfWvkpl5gD9x6M%2FwomCgOGhruNkSL5ShmOpfjDt%2F3yYwTqXZE1Dl%2BJe3xBQPG8YTb5%2FJUoAjtlriqOtvESlQN4uQs3lsWaDDp9FNmiYR9mTwNR9Y8sQTVjTpAoGIzk17kkZs3jxM03XXfV%2B%2F1T%2B%2BHTh%2F6eM%2BAxudkfpiR4B2WjiU0FgWU4nnjc7H3QS0aqjtSrdiEr4vvIrKeeITMTCh0nebuA1MuD7bfikLmhBfLmH0KI7LJIgOYZOIwhNDg%2BqaaP5lbk0HpOUN1PBEJlfo4rWEdLIz%2BHr%2FuwhLEN8zS7McnGUY5PSwpyIFEQY0xOsbJqKSHZpiAxbt0Dp7Zlqv6oHMUHpkJvg0OZGIj%2FVWlfvRDt6QGEbYeG%2F2ZmP6OYl5N8RCCpOURqB8o572rr5UJN9mY9lrkD5%2B7ay6LHwkMRR%2BCaoo%2FBbEfMwsL4MPGW67wGOqUBl9XY9fdgbnDL2z9ZoUep3%2BSSku1kmFf6Ga3bS4FPlVQUcuyERS9H6yVcJDlOIM102i2CIrOHJwWjDGdn74YvPWgtM4JxXIWQnB8JcjV0M2gxtMcFBrFS70dmey05NugJpEt4uY%2BrKTgbinO0fq8eCVg2cISRQLhSpfSZlLv6Nzocs%2BbVZSVV2fPCtdbSPVqwcjX3Nxd2DW1ABDgD4BWUwSn%2FyG04&X-Amz-Signature=2a9091edbb8237e341738cc27344bdde39672e7ff2e317d9ff8424bc7e01325b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SFR4GON%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID1DUcaQaDmGBDI0oX64QBZ0y4t1%2BsFq7hMXNZK3lt8OAiB0PJEpvfDZvm%2FURo3Lvw0zgo3poIgDEXkQkgGOPbd7ySqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXSQF1IvqtVRjQy%2FMKtwDzaq0dREtytrhU%2BZuLSlEs1B85PXhzmB7hTZb8OfdzVddlzMb2j3KvFYvGxQnjy90Nyb5Tp4ilEZ1tuT%2FPlGvIVTai%2FwbKSTOKDU8YutZhzKWX3Ul1uIqUe9NxMhHG7XSFN6eLUWolt0FIXb2ZqVQUIu0HXwmMM%2BhdLZ8dwu%2BVPrkKvz7i3PkEzEfuFRKVNA9GCJi202zddRMnARHD7BHmcmFaSzYveHoEac0dYLI5bhNLO%2BNskYfeBoLCHc%2BmQ65ea9p6R3LwumX8mlTXZCAwhyMi7kTushfGrnazDCJZv6r9tbuiNZKiQWDVJMNm1slw9Vi69q%2Fj3rbRjcj2UorX%2BItIsK0u7ZJR9ewc7XWEbVsoIXyEx1LRfNXK1v9C6tW%2Fr7VzZOwyR4H90kMwc3Jn55%2FIt5oSx7dXdMvnV0%2F%2FLOyVmBKFtot7DwxUttWpvIK%2FeYwGCgt3WUpmvten3wGV8bsaizMB6szpeM58UddmLKuYC0qg%2B67k0rqT53GnJO%2BamNSTiYl2nCZQbL%2Brj41C8PHW%2B3pkJrqCwwAJz0aL1yRvFOu7QFJwpA3BtNdmlXcGxbDFly%2FLXsWymVi5NWkagtDptg1vCjNggo%2F6bu%2B0rwECgk21D3HmwaSD0Mw45brvAY6pgGTExO1gJ3vKvj8kVRO8XMoYjZKukWqdL2E9xoRiyb5n35Uc8LNLY9okUoR8pz9vQH9ykU4EvseTJnnkLcd6HRQ93rzjdXe9fBI%2FGblsTUv1NWMlf3WhNmFKH4CCtdToR5atpWpiz9BJ5jdTQUQbtjLdSS7Yjk3xPNK15srtAQQ90m%2FQLg67P2yQHPrbOUrPRFl0mGh01DwYTUxZotoAUu9zPYhE6a7&X-Amz-Signature=c46e8e128b906a26abe856ec1d1f431a67709c754f196211f8345d884aa221a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466663MLTOR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBSPNUim0u6Hkktj9OQXQUNSb6J0kscGZ9G2Rp%2B%2FK7%2FgIgFB66by8eYz7v9GT%2BWbWifXFD%2F5TVc8HlMyruRujlt3YqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIIP10n0UXjzWbhb%2FircA6X0AzNFTK7V%2BkBqGBUYuRuxL4Z57kPK%2FVXRvZCheFYeMCRkciKntuTYvQnwlGMmeaXfMzb%2FACJtd6h0C0VGh94vHQblRzhlz0bIXzsqS10kAaY2df5%2Bm6QJU%2BP3Fnim2FReIqW4LXiZEiOtm89b1wk7oUpV6FFWJb7Efj517M3%2F2LKrebAyrOI4s1vf6HQ3Yo199JL4WSWZjuFesh0tI1tWyBuBxC2X6XFfDVajdZ1d7b%2F5t9mLmok8LeialrMRvsZcIEvkC3KuvcwSzwUdJRR5WhGTvmgLUvPq8Z4gzr8%2Fsx6i9X%2F6HMyDlXqUKWbNfsD5tcs0mro2gIFf9lOBGSWD81wOyqnHKeTtLFXBSdxM7km7oqJfdAIqwii1jFHzgihaaAUtzpu6KjsbfSHLKhuW5Pc1eil6Jje4l8Kk%2Fe1qUtL%2FZ2tC3aVKgLedwFo%2FsZ2C2QHmzhi%2B9zHI72YxXN0gm6fEU0lQVAlI%2F3Ucua%2BWtuH%2FzQpt%2Fih0qrWLp9oiTcijRQ9vzvwL2qmBgnJ7i7A682GtP%2B8DY3vkxWF1d9sCnq6j1LU2nr8Pzlo9GWeQufq%2B1SbEm%2BRofN0gI87Ly%2FKdsgQb%2F%2FDPaYuxJdb8HlyISPbqL3cTfRL4vvLQMO6W67wGOqUB1en%2Fe7lXwKpl0UktUn52640XKrCnqib8aFQLYsWUBx%2BduNjMujmIXctEku4MMMmmiATR7x4IH1lasi%2BmmLg9HS5cGk%2Fr9a7XNfH1ckLMT94SE7GO4BZ5elhCww2O0PffflwqcjKh8wxJOqGtdjJz%2BMTkYzHHYYYKnByvnAdCr1gmz0huzSAMn%2FvXzhGVTpkGWMwL7ksVsMZmOY%2FgWlWXPB%2F4IkOW&X-Amz-Signature=26fe6fbef88deab258f2a365fc3074d976fc5e92951fc6d893a37f1de82e1e27&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6CI55NK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpgVRtwCVS8eLDCVAyDyr9FFutL1SLHui9kKTqW59w8AIhALIaIwOIzzmyxaN21X3FS613gJIIVuoBOxqcWUTKvp0FKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOEt0aJAISC6ZjL2wq3AOkTdp%2F%2Bshv8dkIT2dyHR3%2BcmGTR%2Bp6MyG%2F4vnbnfCivLPx5ZyZxST0Ndf38YFZhE3U16qq%2Fed1KlL9l2irFU02DXoe2t7LiM6sr%2B8utu%2FUYH8LhQTMbrV%2BPoP5ngAQilOuPfeRTlq54Yf5o79maWDuiOYeQ22%2B9NPapGbsMkHfnd%2F0kE%2Bq%2BZVvdOMD5%2FrAOtTN8OFDo92F6oGr%2FDc%2FVq%2BLrDOky6gRCsaBTy29kadpplgcxgctGHgJsVkkbP4E3rGL9bs3RVc5PP%2FCUrSY3XcHBqVCEMlCnLdDu1DjkwYxyN7sqpntcTRPm5t0oGGHL%2BbLuS2s0w74efVxB9%2By2FAnzO%2BJae%2Fqd1RFKbSXwI5s5jfxmW8tIE0q6N%2FKo%2F7LvMhFyFI7GMwsrUkJXiYb1gaxU%2B4ILCgu3xMekFYeFZ4Jb6y2Nn9WiyiLAe09o4tnWjikA7Z9m%2BemND9w50XwtwsQuRXzX%2BfSiETJjB6Z5lydYPg%2Bbe5PhGxANJvy2SQpHoBk462YIWp3QNFXYjuqf7kVhOJN859THGRMfJzlEO5mdjh4X%2F1PR4NSJ%2FYTL2vqEH3AijpH6q4fO%2BN%2BqNXjItBXT7X4VoKCuuukkmxXKSKvOkfrTpkFKMy5pIEsZzDSluu8BjqkAQtsb6wjSxr91xaMXe7ikQuZG2OxN%2FYiC9SuUIS0OgbnUmcBkKCxLddvgmCPqDsc0hER2qfmwcMEuGZ7swaJSl%2F7YxTs8Ut80ySH5crVxZBR2aRNCiBa4I4EcQ7yw%2F4ICbC%2BWpTSxnQfFPLSCduMjSQfovUkfe7LAg%2FRAkAw2TumlLSyoxfoRY7u2FZ9CS0KRQxpv6tUU519WP5V%2BuXB8V52IsVe&X-Amz-Signature=88bd0fc9bb84c6dc0e59f3d2738bb0d68dfe8fcd8f893e0113310e11edfa84ec&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYK5EXO2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDv2217Up%2BnL4c29T1s0ZupQtbcb%2By0n1m1PD6bVTW5WAIhAKOR8Ccw2IsiCqeJZw2Nu8vbED5ptN%2FyQFIY4t51ITW4KogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxg8dWEgzErDUOnw2kq3AP4fSYo0TQ2sYLqQJ5xpvjdFMlcldpv3vPzUvHDtE2zn9UWxLE3rVyTJp9UpbuEQ7nBZCD7xUOuZT6qv1dxvzL5ADcD1LsbZnQ2OpsyD1errK5nMSJkORuBMgVsYn%2FuHUBZsv%2FHgK2SpXaPGiCSK8fKjSEV8P4Isxm0oVhyyyE%2FeZ7GUV2YA%2B1LSTeNmpUWg4SbBRUuYiazMiZF7CgihXPMCK2lratXkb9Y0%2FtRngi9PBXkdJEeaxCkcyOzcF7cV3VWjkNyjhKZgq6znaLQdN9JwHHkyTrDuPscUF5oE%2BzGWJw2NvA1nUw0CP6X3MvlVtGZKliVfSMg2ooauCdQpH1w1gib37vK3io1QMnnF%2FsM8NvswwHynQd%2FSxGXVWCFfA2c9Y6mS0p8HeT%2FSfAEM5Pm1kEPv%2FE49BFVkKbZZ44wGIYbbaes9jvb%2FjO10Qdv6xb8cxU7%2BflgR6isrgDLDWc4HliOpcusT5aAwIOnz8hRuDQNZkB5V5j17SXUxuZzbJIAcZASyhPwS71B%2Btsb1Upbk9r%2FpyTDH16gWzCz7zQ2t7fFDBV6Tx9HWmAw%2Fkfgonb6MEEZViuPD4WMqNZLVk9DK%2Fbn%2BZ1ZtdGuOjjLFUmF8WSD73I6qdKRYZZSKjDvluu8BjqkAaxwysl%2BmPUqdAgYdg5nKse%2FTQEGKa8U3xz9Hh8kgK9GbAQ%2FnJCafC3ugJH%2BePV8o3WOFx4ri51peKZtoRW0fUocATdlq4W7AnXTKWD05FznKi6cw6HNQ2B1oO68l%2FEaWjIGoi7HzQz667X3EI9aBTjVYmNfFj4FFjSnGBkYzbsnV%2F1VgtqtTEzWP%2FGwU48qHacAvK2xtx%2Bf6L46bRMaBA3XPWHH&X-Amz-Signature=eaf139b2602c8333cb31343db34cc777d38fff2cfb23e6f327f14a3274bd0994&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEGMBGRE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBs2bw2Bk56BHW89bml0UPvq7D2cyjiYV5pq3Hldb4grAiEA%2FHllEx0UsZAZlXxvTWzvEl62ZnRDpS86KhRIuya4RFIqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM7kDjKZNjfjOB2WuCrcAweyV1WWt9QwcdpndclOsBaBjW%2FF03rKDuA1yXM86QnwMfCx%2Bas3vTU4MIFwQjcdyO%2F3dhZxr7yGhizRNowktWuCy8MxzwTFuPC3BHam3ZdBFOhADdbGOWx%2Fp9t4CJ0u9snJisMbajprj0Zu4Pbo0wkQBeTJhn9flUZJNRr6ZhL6UURqC37kDwyJfqFCoGdTis0mOeNDt8JH%2Bgxjn6AKSqizKLQoohFZLZEbUmeelB%2Fqcp3Ro2FDFmkDQz9cgB9L8rmrc4bDPqmWxouG4v9sLNUbysXTF3YnadWWlQG4I4z%2BQh4JsKz3%2BAk4Rswa2Q0PfHXqPq707ECZlc0azUVA8oEUJ%2BNhz%2FiaOjLNsztLKSSzXxTfHRNdoJMpje%2FR69ECTXjiQ07JOhqi%2F%2FI%2BqA%2Bsj%2B8zf6hXSwaBbmhNEMX8O1bGqT7M0qRqGZil%2BEOFtP6FdwrpZKk5KHzQKMPPenAIyI02Z%2FnFsLzJlWnfAXZbWeqHbF7W%2Fwg5Y7smuBQLkOa%2FdkgCfvvNK9QrF57lWfy68zJPuSi7aKhmSgQdMlffwlUwKsyhVk5maemvjheTUKjT16Ilwsx4R82M1mdbxEgaJ7O1aKNLaaBL1hEPiw%2FgkzmJSOMRqp1VaFZtlZOZMOWW67wGOqUBakJAT8cL4KIqh9cy%2FY2mrcbRh%2FH8Io3iuyrLqqv2d7qGeuWUDwwxGMS0rrje0Ij1GvKeVDP4bFiCdlFaYNGy2J63AKfUvfzp6V1MkSHKiAI%2BSylT8cyz0zrM%2FqVbe%2FzdljCytU8pOxPuYTZObsG4yJwGyTpAgZC7rmDRYk8NzaFqnpgAX5m9Ltdb4UX8Nsq%2F%2FuCddAZYOQqL5JUVmJrIewTrwDeK&X-Amz-Signature=febd4d9a36596978ba98cb6df6ddd157b7651d53abf565ad287d832db9cbbb6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466663MLTOR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBSPNUim0u6Hkktj9OQXQUNSb6J0kscGZ9G2Rp%2B%2FK7%2FgIgFB66by8eYz7v9GT%2BWbWifXFD%2F5TVc8HlMyruRujlt3YqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIIP10n0UXjzWbhb%2FircA6X0AzNFTK7V%2BkBqGBUYuRuxL4Z57kPK%2FVXRvZCheFYeMCRkciKntuTYvQnwlGMmeaXfMzb%2FACJtd6h0C0VGh94vHQblRzhlz0bIXzsqS10kAaY2df5%2Bm6QJU%2BP3Fnim2FReIqW4LXiZEiOtm89b1wk7oUpV6FFWJb7Efj517M3%2F2LKrebAyrOI4s1vf6HQ3Yo199JL4WSWZjuFesh0tI1tWyBuBxC2X6XFfDVajdZ1d7b%2F5t9mLmok8LeialrMRvsZcIEvkC3KuvcwSzwUdJRR5WhGTvmgLUvPq8Z4gzr8%2Fsx6i9X%2F6HMyDlXqUKWbNfsD5tcs0mro2gIFf9lOBGSWD81wOyqnHKeTtLFXBSdxM7km7oqJfdAIqwii1jFHzgihaaAUtzpu6KjsbfSHLKhuW5Pc1eil6Jje4l8Kk%2Fe1qUtL%2FZ2tC3aVKgLedwFo%2FsZ2C2QHmzhi%2B9zHI72YxXN0gm6fEU0lQVAlI%2F3Ucua%2BWtuH%2FzQpt%2Fih0qrWLp9oiTcijRQ9vzvwL2qmBgnJ7i7A682GtP%2B8DY3vkxWF1d9sCnq6j1LU2nr8Pzlo9GWeQufq%2B1SbEm%2BRofN0gI87Ly%2FKdsgQb%2F%2FDPaYuxJdb8HlyISPbqL3cTfRL4vvLQMO6W67wGOqUB1en%2Fe7lXwKpl0UktUn52640XKrCnqib8aFQLYsWUBx%2BduNjMujmIXctEku4MMMmmiATR7x4IH1lasi%2BmmLg9HS5cGk%2Fr9a7XNfH1ckLMT94SE7GO4BZ5elhCww2O0PffflwqcjKh8wxJOqGtdjJz%2BMTkYzHHYYYKnByvnAdCr1gmz0huzSAMn%2FvXzhGVTpkGWMwL7ksVsMZmOY%2FgWlWXPB%2F4IkOW&X-Amz-Signature=84cb3f4e0d422fcf3fe4865f9ea7fbf2b1e370d471ecdda29dff81999e2a8b5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZQQPQA3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEBnLRnVGY4sQr1oZPJwySc7IwQcsT7xA0TNRdv%2FtWWCAiAok5vrVGz%2FTNr7RpmPEzKeKIOGW37YQ8y9ccjk%2B7or%2ByqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHmY5hGGhzwLtG6xGKtwDTsDCW1RwGIN%2Fc2xVqoOJRNAn14vibB2oHdjyOypWRwCgXMApe4crJNq1kPJyGi2hPIWuO%2B%2FUnWMdlMVGqp1ItvgcJCW4Fwd4yycaRuFVkmGCSSBKvDAdI3V1ku4ujR89ljdTutMTuivRaY1LDefiahAEzxlYVT7kwAgy166ICj3RvRYpbjvfy4oV7U8DQ0sW%2Bx45Xh6shPjVWC79xNAy%2FCjqFurFbKgpXK02H5HoJThW2ymWVj%2BjLQWx33Xz%2Ft5zjhyZpzlcd2u3N48TFRPLePckCmLG3g39rXRw3xwRC5ccj1LWcd9qpsOmjLeLIcagvA8NzcABpAbVsiOo%2F5wioi0QomdkVzm7qjcNdDnLXZMF8Qxy0KkH4uu5Fir0MHTsaI0OzCNb0IEdwco47qqxcbzw%2BT7H450uR3UDIRSupHEMiSAtu6bH3ck4xIMGyJszeRdacMBOf3%2FmeFiNb3SyBdEdvhu0kTgRVEKc%2FInsM9iDEJHTBFABDyYKhccCAcw0%2BjaaghJTwaYjdu%2FYkxGRXrpvZUjkSsfXkpsyJDiRGlUlCH0Cjg18Q%2BBeggOfuNSsptx1CNFfcJyX6gf%2B6lbyquq4DCPHfju2cP1ZcfRVbSklyoXAgkDwepZ3SD4wzpbrvAY6pgG9Bzlg3tT58ebgMCYIScob55bhxS0oFMfiHNuo2TNtZxBHG6YxO6bH67%2Bebkz%2BuknoLRCTA7UQmjlyRTeI8W%2B16w8bziwxHqcaTArA25U%2BNaCTETPU9sbE6V5OMOMckrjuGsARDUYr%2BO3ms0OgolWyfO2uzwyhQdkCvu7rZA7RTWVjscxjC6RH54beU07mNSktTdsQbBWpnlCvlPiTbeM2PD%2Fi9BM8&X-Amz-Signature=1ee6b07a996665bb52cd7dc104c8ca371f41791c33d1b9f78e3ec66cf18e736b&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZQQPQA3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEBnLRnVGY4sQr1oZPJwySc7IwQcsT7xA0TNRdv%2FtWWCAiAok5vrVGz%2FTNr7RpmPEzKeKIOGW37YQ8y9ccjk%2B7or%2ByqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHmY5hGGhzwLtG6xGKtwDTsDCW1RwGIN%2Fc2xVqoOJRNAn14vibB2oHdjyOypWRwCgXMApe4crJNq1kPJyGi2hPIWuO%2B%2FUnWMdlMVGqp1ItvgcJCW4Fwd4yycaRuFVkmGCSSBKvDAdI3V1ku4ujR89ljdTutMTuivRaY1LDefiahAEzxlYVT7kwAgy166ICj3RvRYpbjvfy4oV7U8DQ0sW%2Bx45Xh6shPjVWC79xNAy%2FCjqFurFbKgpXK02H5HoJThW2ymWVj%2BjLQWx33Xz%2Ft5zjhyZpzlcd2u3N48TFRPLePckCmLG3g39rXRw3xwRC5ccj1LWcd9qpsOmjLeLIcagvA8NzcABpAbVsiOo%2F5wioi0QomdkVzm7qjcNdDnLXZMF8Qxy0KkH4uu5Fir0MHTsaI0OzCNb0IEdwco47qqxcbzw%2BT7H450uR3UDIRSupHEMiSAtu6bH3ck4xIMGyJszeRdacMBOf3%2FmeFiNb3SyBdEdvhu0kTgRVEKc%2FInsM9iDEJHTBFABDyYKhccCAcw0%2BjaaghJTwaYjdu%2FYkxGRXrpvZUjkSsfXkpsyJDiRGlUlCH0Cjg18Q%2BBeggOfuNSsptx1CNFfcJyX6gf%2B6lbyquq4DCPHfju2cP1ZcfRVbSklyoXAgkDwepZ3SD4wzpbrvAY6pgG9Bzlg3tT58ebgMCYIScob55bhxS0oFMfiHNuo2TNtZxBHG6YxO6bH67%2Bebkz%2BuknoLRCTA7UQmjlyRTeI8W%2B16w8bziwxHqcaTArA25U%2BNaCTETPU9sbE6V5OMOMckrjuGsARDUYr%2BO3ms0OgolWyfO2uzwyhQdkCvu7rZA7RTWVjscxjC6RH54beU07mNSktTdsQbBWpnlCvlPiTbeM2PD%2Fi9BM8&X-Amz-Signature=ad08b8b0913ffa154d35822c08556758e6f8294b3fb554a6630ca4534d4f6bc3&X-Amz-SignedHeaders=host&x-id=GetObject)
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