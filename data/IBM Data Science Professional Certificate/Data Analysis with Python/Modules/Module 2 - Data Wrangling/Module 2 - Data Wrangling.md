

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGC2GI2W%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDpvr4a4FxBdua9NcMUfzaAK1DsV0g4dUeFLOPsNuoa6QIgGo7GMsVJtaACltJ03sppsPnP8kg7XgCKkOMBIi55wu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIrBAQCFcVmMFGWJTircAxMX0GMJwvDmBRUw7gjN9iUqmKYRzObcmQfqMehjKhYwmWgGLm0YVllI9ZFsQg3uBNVoPma6spuuEFsg0Rn5T9F%2Fo5BwGYOCPQgPivC6m5vBR77WtsfTjViw%2FYcmn%2BtUtQkpNNb8AEfzYBv3Dn98Sgfmm8rdkDe3qZird%2BF9Z6FnuWEdLLjL%2BAYIMJdMcNNooV1UaZeWzQXj5qOrF1hegj%2Fzfg9UcrLSx8peXkV%2FCc35jbWtARWVFaCYuRUJg0%2BoDwEC1ymuoIb9Wm%2Fyfc51WQ0ECzYJ2vNx0xF5GzNpkLlbfqLbGciuVsQbCUxNKff%2FLX9Y6i%2FbrOSHT%2BJ1C%2BlbpL6%2BvHJK7DAxjTFCKUuKkvujnEagCfLT8mwa8bMU6w0FsCk5ANA4%2BiDh4MgG1F23nlDtG3wi331Y5x%2BrcX8JSvnNKle%2Bu5KBqUNIrnOvVhtr1korlIA81CfOJDY8Zyi0E6hrJzA42f5utt7L%2BlKYXSrNxQ1WnIw5CA%2BDbBTRojI7pYfl9lomhhgK1TnU%2BbXy%2FLv6nUK9P7%2FC7esx%2Ff2N9qVKoopSD0stlIRxFDQMaRM5eZO6kvQZZn0aPQWch7bxOxeOHsU7Q%2FrvM%2FZI2QPdbPTzkcs9wkC0Jry%2FaR5DMJCFnb0GOqUBc%2BA0AfRwBF10poe%2BWnn3VQV7lb15aX7FDpVELgDiwogSOOD%2BXaPIB6v1mB4nHx1nsb%2BRJNak2j95c4rRcGLsn873tgVyE12IX1uotL%2BmdEQfNL2qjcP%2BgSOBZ%2F1mOlY7Hdkj0TpEisQ3X43BYhTLwNt0j27uhMAhO8We6ByatskGYQZQ4aFHxweRX1BlM2q1pla82Lz%2F2bU3mszmSm4ahBeG1eH9&X-Amz-Signature=d5bbd678409d358cb0d020c3049695aead06f18662d09ac963c2bd26e6f73c6b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UPS5QNR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDGYDCtOVLLsIc7kvv9BMDCiwYdgQsoPbIONd%2Bmg%2BWLCAIhANcb6H1%2BPizhFxcL%2BlQhmD9Qyt9wY46Mp7JkLIHTblcqKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmEI4RHFkfp5F2%2B%2B0q3AP4jWmGr03E3feHlysKVcA7Locs4uEbbGN0sxU5Q9NhGc8pDu9DB4CIXIYUt4cmNujuyUSYyHhnU4Y0FQKTx6nASYazRE3Yec%2Ft%2FVNTjHlURFwoAmvnHo8hyxIwuWa7L1HeTFbccasrqO8TzykeKfD1SpUjD0aRZkRm2EnYrIB49Kd6SwGTlC1aa3ZLsfkAdgItlvlWy8IYKdLTSXmljqeLYu49Ya3aB%2BkSqNgbdxMdMjtMYWBsFM5kEVzy%2Ftcpo7lp42m8EBRm0qtgB894uZkBh9c5f%2FZWwpODCyuRkHDo3kp328p7Bx%2FOVnYq%2FHDltqYXFF1MOE0NKNumuefcsOiDgDTh9qWyb3Uu%2BqnxwMZLFQoZhM5duhn%2Fqrtb6baZiTUWb2LDtr5NTWuTXpOgI%2FsA9Nli3nFSA1a2fAni7HQEtRTjY0ybvA3r%2BjInYJhNKO8mKKBQ8m74SFbNh0YZRUxTVwBEGMXdAcIBfZsO6HnaszJR5exENpD17CLFLYgjy3uFhFpeQZBqowdcbCL0eXoRmg2LyWFBl%2B5R44hDVR8f%2B4bEwKX2sRVermo95l%2BffwVBoCsiToy%2B2e2oKyzZ0jLVUS5JUnuxneRVwlHVboQ6Qc68%2FmSMCX89QWM%2B6TCHhZ29BjqkAYQUqy%2FattUcvc9TAXUCilI6N7%2FfLYXvefpbW%2FWErS2WvG3tuW1ndWVjAQk1H3SU9xU%2FEvkBlWacIb6DvLJceQbzsmKZs6mMkelmSu3Uxt0ZnSXLD49z5%2FXDrcrLF36jW82utILFwKJD7SvQM5gV%2FGINKEzovF23av138RgccKPT6%2FCmXgsJbU5lv%2Ffa9Gy1SZ0jKjp4JEcos5c3fywWG0fHT6De&X-Amz-Signature=5b7656d96b074c9007ba3a8f0913f58f7adf459787d38c7fcc16e3cb858d766d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U66BUENN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDlMJBzgvTSWJy%2FLFbhtfHNQ21lkk3LMhBVwcFkwj%2FYGQIhAJ0SyqJFuh56tMsD69wbTLdbNQw7VDe5AFjInC%2BVXT8NKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAet8uNOcbZtBsowsq3AMA%2BTIvlr2FOsmiN9IGixM0MJopN%2FMAyjUZNScE6gUoS3npZNOYgEgoxgA1sV%2FU%2F4pxqzGDbjESu9vShsWM2dnG2TjfmtU0n%2FJ3cuWwG2JWB2Aw9wLGkI3IvamopmMg9FyFfkAbLo6RLVo7V7pp1WJ%2Bia7bQtZ8XM3zYQpbPh1K4Av2sEv1RDm0uAF05K4vGFQPaBM8PMuy%2BjZefiQKOLu%2BJ47YDN0X%2FBDqF7yRgiVLJeIQNtc5JF89eUIxBqdlmoWGzEpHn6Z1Ph5DSwoSRAvAyBoi0D2WyvFUfiLA9QliTL9aVJOwIX5hUTUscWKSaXGZ7vP%2BnZoOicPbngqtLtDGFzcU4HEIWbdxIJLfobEldClUvWfNh5nGisiKR3HYGb0W6Yprrg%2FeauDHAoqHV0IwtvL842G7BKlaU2ikrMjSAWEq7AI9Sj5eC4%2FWwyeTteOEKE3SZeAKNPMMQ7gUe3W7g3iZUxwRuvJtQS%2Brd7ZQKiWfyzJk9C3qk17QYwbQMPhOzUhmYp%2F4xIxnJrYTUoAz3Kl%2F9r%2BJ%2Fk7mApngVxptjps5Kjv398eMU764Wz9RpfV5coIHkPJfkGXTSdjCGATG2w6I9jofM1m%2FgEM%2F5VT3AKnejhGR8Kx41H5NtzDPhZ29BjqkAQcHVF9gqCPQmZbuqHgDxNQ5id2RdO7lcjlUtZTgxoAhNpjyt8Pc82yF7nXg5VLWsxS1oi8T4Zacq%2F9DDyhz9cqJGYyBN5q7PJHoH8OFAjs0tMBG4chy3nOsYd9c4Mn5oOz9xIid5cChvnHHYUXP3PXMHpf1X5lSNA7xsYDvaIrX%2BryMBgOQdKsijQW5jZJ0grVz1GKirBAfOfazx5U8c7XKL%2FNl&X-Amz-Signature=1037589f9af3cdaa293052e41100681bffe90e6efaf55b0bf8283d1779a8ccee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLHMXXPR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIBWMshkucl%2BRuFjV0WUFvVI74t5MrfRz3LlT7c8DugM6AiEAmh1vxilAOAiIpCQAAcsyaLJTvsEQCRnWuLTEqI6M2uwqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOed7OiSj97wGbUdjircA51cTWLgNV6QM%2BH%2BlJx1RxbZclpdLui%2FNema3o%2FHPyyWkUbfoP%2B3%2FZDo%2FgPIODJtDvq0TZIqfTBAXZR%2BMuYQ7v6ScujBhg4vPumh28rTdJHoiGaDzGG6SG1X8TxLVq6CgXjU1gBBXu7nPomvgMCkE5UUzTf9gg78yoMnt1kDFhWyyNj8rkHDyyj91vuyIki%2BqnRkmooF1d3wZQfFg74ZFmcQhKWXmx3X%2FMY6nl5YQnnE5g8qCjO5Ok3q5Fz0ERgaquztRcBCKSPIb6quA%2B0H1Z2CamYHBByJ0v2CsFYBCpNCB0ZkKyPgu1c3CKkN31DwnEDglr36f4erbuUAi6aJH6kedU7qmFWjwYsXopUs%2BnIGkeJHZ8gOJ4Hp8nkM%2BZ9VaeRXbBSd43jJnoruf6VXSsAwgsjZIyMFLVs4VFxlGPKo5YueHkOsroHuymDon7u2KJFUZtq5LkRVTFH%2F4tf%2B1507RvjpklE6LsD7hNJhNnhayrXYk36P2Z%2FFzIZ5%2BuLlvq%2Be0DmqQ%2B0bgfb2VIT0CL8OuhBBs%2FXqCfmvhz4HiZO1%2Fx1cCnQhYtM5PnY4F3%2BL97wRwHRGDYtKC6i2f7ybTGDf6tTrdQiQroRwQtJH6ixRQWVf%2FzEH0OVSpkcMMIqGnb0GOqUBQp0nQR2CN7MK52%2BfOK42eS90fjBrDsPhDD0nWBcAxAOzeyTHIqqOf8k8nD7uX7f0NYWnysPCvkj1QjgG%2F49QfM2pEJ4ffBH9vKYsocqYelESZ1P5GzJCoNNyOVfRQqFBpYMXrEq%2Bo1xSxZCXRBCnAgtx0tYGb25%2BnvPn0b%2B0Nz4W%2B4bRlXcSF2Pg%2FeBRKLtS02MFcr73zH0kLsxr4PT8Flfd8eId&X-Amz-Signature=e234674cb8ce0740b28223b2e8e9779b359ae78b6a89341d1033d80ed5a6c3c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRRIWMIJ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCICr2vQzcj5OdW%2B6jkHlGFvdmMiN9ontfVQiEEtYaH14%2BAiAX2QNKqFt8mzcuo6ltvzuUD5HSD%2Fw8xjwhuldKkM3GuSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTQxP58nxdT%2FoGz02KtwD0TsWx9sa8vImWYSrXvbLCaXP2in1vj0gt9nNSfebqfcMPMDaATS1nSYMtq%2BRefsLZ9%2FxEqlric1SA16k3%2BdEa9DE%2BPd4eIWKCkNUImu8YF40H%2FRqfo2asE%2BLHKDPhcBAaypQJawgOLw%2Bl0VbN7UhVN4ZuuoZoMxfui6mlDz%2F%2B8Ozcg6VkQx0j5QtlE81BQ39KcpjtlQP23y7kv7Ykcco8y8G88n8I431a%2Bl6pNFrhAl2whi10HxLQdS5THhYBD0YWdVgstbSdjV5IlIuLMr%2FUkxACDdX3A%2Fj0n7jAESQJzFClS1O84anHyiFBcEbsnpaxh8Nue7fe0GQyfcnxRrF1%2BYyyM%2FTR0mx7RmYpIaSs3yxf6feX%2FC8ZJXq4233LZSP6dI9Tt1kYW2Ua48l0dtmOIxts1Yfv%2BrLIH8vUnVxGcYVg%2FUT7Qhrxveg44Wbaenk1GS072F6Mb6DPfeFdkUfIXmweiJ9p4FWydkPI0axUpfTcxeSt8zegu0s%2BstvNIBISmmsHTx5EoJjDgfFjbglWTJA%2BToyia4Bsj2eFVR4nzqIIwQ5K1hodre2s6Zsn%2Bn88LruvejfsECiCkfvqE87kaRDIKksWhR2ea1biZHBuy16ZO6133MWSgG028cwoYWdvQY6pgF%2BmrCdLymyTYpE%2FxvQ1sQnvDBWxm2wq7CLcgkCoecevvn8TCMSOjxj%2BstuBfN7%2BbDXPwwPrf4Q6YNgKotxjGZfUiWJ%2Fnz8Mbfleh7RUm1Qkg0ICVcgzgy0nUMzvnKIaR9i0p%2FrJ5gxlqTftbrfrMD40%2Fz87pfxgWM79wgeUqO6a7nkwJo4womRHcPADot5cOEY2GRb%2Fuhff9duOwYcNixr22DpTcQh&X-Amz-Signature=bf94c18805ed815a3dbfb01dbb868111f65a56116508f6ca29e8a30440de7e7e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW7UW3U6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQC2xfj%2B%2Fam1bj73p5uknGA6%2Bhc44q8UnuqkERTsIHk8yAIgNlvuUfSRQsxyhDHd53BTXXv8MFy4cbos%2B0RnNZHgjzMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB7f%2BNzmfowLIA8o9CrcA48jurp3g2Wj6wb%2F%2BwIUjgJH6vrTKthKvegs%2Bs8jWLf4bFaNATM91FzNTAZTJ90Qj7DYHaW36O2e8oOpC1xGSudGuU6TH9g34ad49GifoGqPISlABTlhYLqbFaXKYqXRbH%2FDmlnwirPmNLI6ANokRBbQTBLK3fBvXxwb6hozVID7XjOvITNY%2Fe6q5WRx%2F1Kw99fIg4noec5M%2BhahrJ%2BR%2BYPlDirQslyyqwH9htGQK%2BhdMrgrofhN4X%2FwXe%2FmF0egTnYoN%2FvZzyKNsrYTYE1Mb3ZWgvyLX8Mopm8FGLAvYoTAy%2FGK%2FykQd9CeClxl8tZ74mrIhMUyxmzszxSpnqOyrXURVGZFgcBZ8681MVGGk841WJkoL2ueoqosq7pwBo58ljQMjvxdMJNzLdrSpySe0zJ37VWIy%2FpatYz8vXmjoib43goi8I8IqUoJymFOI%2B2X7oAagpBTXo0LRETQezaBBOMsFVihzaB9BR44cTfLJ3nHiORlAQdKzG4xt6NcQC9%2FlqHwCFTpGaEzXuXRmdCAqbbIx7VS%2FH70OI%2FoVNUvK1HwP%2B9E0sqdFYoPw8IRefS44Gt0iCEDJuHHFvZ8n2cywgzaVtUL5MPL%2BLyzzywkXV0xNvitsWA7dOnEYd8jMP2Enb0GOqUBomF99G5l0bpUGLpYcze1%2BQuO5XCV2OMno3bs9qLb0inFSSf4AXW5T43iGA%2Fab3Taye9w7j7lVao4M7nfLM9M0SXnweGSDjn6teXonAu2y1Bug5nTjMJz52rjNB9YO3qIFvyTNlyth5ZsVbKAbXZU2zp%2BQ3RpSMwsLrBp6%2BSBoPIUTuBxVMMH9lRCJJB4KrODjq%2FyqQjO599bmv2FOj7Tjho5jEAX&X-Amz-Signature=7183c6e70832cc86963b9c8441350ee54594ed354566a132dffdc552ad1d2abb&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LMVMPTZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDATWPoh87IUaoMpi5IrD%2F9cUi7%2Bzy9eLoMFhiCvR7V3QIhAKzQfvTT6MjxC828zzxBWByL2gRQtg4%2FuRDtIDggAfyvKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9zFx8ihA8UPqDhjEq3AMvtYbg8bPOqr8UTcGhLb5whUcIVl5Aiw%2FhqFD4gzwRg1MvmVyRb6ESzNzFDB6Fcqe72MmB43g6jCWEu0qHHPu6R%2FXpS0hBT7xp2b7fnyFBcnXe45a1IVnm7Dalv34CSPH56xtb0FjGzO9Z8oC6Wp5vsKTQaLLhaJLKUajxIJFp6GiraraOIU%2FPdktmR6EhQ3%2BQskmLjOMY4pZuq9CmqbSCWTON1L%2BgVr6%2F9yiEfwe1fO2ddyPAH%2FUh4xV%2F%2F7Z5gSQv5AS5zNT%2BF24PY21KGGWRHr%2FSC3hMWhAGT%2B8Ehv9%2FqTHaO7MjcUPKZr8Ei8TcteVYta2yeOf0jSfgwXkfreDUv%2B7yo61TfTdeTq5Tdexm51EQDKEIVWXgVv5fqrzXVJGVtLzmzAXOujOgGoHAgJOs1mApVtSnEXyt9ya3NB3lYKZ91J5wQe7KwWdBexyrQcwlMMox084Pc74JsaJ2nokVrH4txGRD8jPGJv1UicdRzc%2FG6eMUgclJUzrphQo5Wxx7YdonHjmZmOemL6%2FVw%2FyZD59DcJjywKIgYR80%2FPH3nuXCRFJyVIxRlL4Uknhr0b78nptP0Pypub4MmyvS%2B3yml4uylUux2ca%2FgrcGNgcc7ZTJh4GlJfS%2Ful1sojCghZ29BjqkAd5f1ArhWAeEEwV19rCuTU%2B5iCFIrSqfAuC3JwJM2vEu%2BCJmGOc9hnIJqZq39%2BzFUSN%2FGl0U%2FKdr9ApgaDkk2%2BkGo7Qy3zpEx34pjgt6Cj1FGp1zk7RnEcV1cbbOP1cbeLQi49xoB7AYfQzn2Pi1SkWcFmUtF3%2Bn0k%2FQVj38USM1%2BWFGzrmXgq1hlNJoawpWiVdOC92hPEMEr%2Fzu2remsmJvluOy&X-Amz-Signature=a84d8058f9301a38793a9e53a97ad52900ec29729e8bd98d07fd9fd844ce7feb&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIFILIBJ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCNgM8GQ%2FBingqEyt2UFiOaRf9J8V8HMqSXdiyGdds7%2BAIgSaSL5dX0iX2oylHN1%2FPlzaPVDp9vNtopzTaIB55OifkqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KNtSmyJ79Un2xzyrcA3VhM6zGtIKVrI%2F0%2BL1XReI9Tii%2BsuyvmtNUmdzc%2FB0q%2BsZlW%2FxCbCFaeQrYeWDihvnQv%2BHUptCtlueq90OSeQw%2BrYxh0Sq9D5byJ6HGnInyLPzOZmNGjjOabQEwxIADwNpdPZgKnInXjN5y9hR%2BnN0DNWxM264VfVZ5vfyKBZg4NXhWgUKfybd%2BNMn0OLMGDxPNxInfI1flLUs50lPId5Il%2FDRB%2B7IPuHzL0nIxjDWboy7mIj5ZbdFiFBMrJiX1awx96W65NzywFTdPfg84Fq10IM%2F%2B9zNr4TQ%2FmOTS%2B%2FUvHMVTENfJ%2BPQXV2XUdtDTCjDvlIGx9KDBLQD6HKrdjTO4Dx8biQ0OklRsqbOcf03XjQVA8Q%2FN1rWJxKKgWTDYlaJLhQ%2BbnA0q8gNmuylrFlFZYRGnrkK7Ww7v6Le88AJl%2FLr4HcSzCc%2F1XfHEfjqBu%2FkSG3CpN2PMwotzoHUdLzg1tQ%2BEDYjHw%2BgX9Yxt9zSdxmMwiYNx5of6HMey76l7Vk9UMtaGJcwfdacBuvWKMiQoHf%2FObyOKInCWGduCeJS%2B1Poa6AVdYCoPLJH9JfwHOCSBgFgKiFoHrUkrftTPLZ%2BDIZ8x4%2FzQyaU0irSsO0FdGjoS%2BOjVEezL888RML2Fnb0GOqUBzxWdSdztwEte7tteAz%2FsiHsor6GSXJjXzFPTE41ftEGPt1V596BADw5L4ADAYgZysRPVpDmAZ8ksGY2lnjYQwfWiO61aM8d108SyngqMeGj5b7Nzc23Rf2aUB3Uzi%2BidpCe9fCPIK9bgFaItqsgCliSu%2B116MXgF8CssTjAD8jzboJOaZTNHTV2fzOTN8U%2BIEaW1czJheEPshH3RWKQbfRsTOISv&X-Amz-Signature=0591dd0c5afc8d9a7908ec92f611d3378436b6da9f5b497d37d99ac054efba04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRRIWMIJ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCICr2vQzcj5OdW%2B6jkHlGFvdmMiN9ontfVQiEEtYaH14%2BAiAX2QNKqFt8mzcuo6ltvzuUD5HSD%2Fw8xjwhuldKkM3GuSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTQxP58nxdT%2FoGz02KtwD0TsWx9sa8vImWYSrXvbLCaXP2in1vj0gt9nNSfebqfcMPMDaATS1nSYMtq%2BRefsLZ9%2FxEqlric1SA16k3%2BdEa9DE%2BPd4eIWKCkNUImu8YF40H%2FRqfo2asE%2BLHKDPhcBAaypQJawgOLw%2Bl0VbN7UhVN4ZuuoZoMxfui6mlDz%2F%2B8Ozcg6VkQx0j5QtlE81BQ39KcpjtlQP23y7kv7Ykcco8y8G88n8I431a%2Bl6pNFrhAl2whi10HxLQdS5THhYBD0YWdVgstbSdjV5IlIuLMr%2FUkxACDdX3A%2Fj0n7jAESQJzFClS1O84anHyiFBcEbsnpaxh8Nue7fe0GQyfcnxRrF1%2BYyyM%2FTR0mx7RmYpIaSs3yxf6feX%2FC8ZJXq4233LZSP6dI9Tt1kYW2Ua48l0dtmOIxts1Yfv%2BrLIH8vUnVxGcYVg%2FUT7Qhrxveg44Wbaenk1GS072F6Mb6DPfeFdkUfIXmweiJ9p4FWydkPI0axUpfTcxeSt8zegu0s%2BstvNIBISmmsHTx5EoJjDgfFjbglWTJA%2BToyia4Bsj2eFVR4nzqIIwQ5K1hodre2s6Zsn%2Bn88LruvejfsECiCkfvqE87kaRDIKksWhR2ea1biZHBuy16ZO6133MWSgG028cwoYWdvQY6pgF%2BmrCdLymyTYpE%2FxvQ1sQnvDBWxm2wq7CLcgkCoecevvn8TCMSOjxj%2BstuBfN7%2BbDXPwwPrf4Q6YNgKotxjGZfUiWJ%2Fnz8Mbfleh7RUm1Qkg0ICVcgzgy0nUMzvnKIaR9i0p%2FrJ5gxlqTftbrfrMD40%2Fz87pfxgWM79wgeUqO6a7nkwJo4womRHcPADot5cOEY2GRb%2Fuhff9duOwYcNixr22DpTcQh&X-Amz-Signature=b5cca24454120c6007185c4cf4034effd43d5b760eff56b2ec09530c7037d2dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2KFGT47%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIE8lfDqnRx6uq3gCB4i9XnGaszfPKVja9iACcNrHb2Z1AiAYLsXupLtDJOpghXLF%2F8aS7MNF8tP%2FTMAmsGfLpTiRESqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMa3PcC5jWIJHI9YDbKtwDhA3rZ9mShG6DnJrNrgg%2F6LWHpKrxPcDzupbNFctsmp3yO1yyp39kVDGTMnghGzf3PLNHXSO9PnRLJcRGSzb%2BvGXHJgcMSj3y9tC2DsHuAmYX%2FC7RWxIDhIq6A2dtzk2%2FRvhijJUCToMjX8%2BR6VcRA9SbK5hN8aFio%2B0PqGQZZ%2FubIui1i9ZNlq7UbhMH9tYVbvumniBHnFWjtP4dYzGcY1W5P%2BW%2FqC3ySZxMy7FMn8ZNlG67vmNM%2FWzeVUbU1TtxdemV8XWenqaMZw6AGtLhwHVo884cGB1nKncWhWXXOgen7VLWtl9UTZ2iru6mEkUxbqkAAOwy4J8LBTfuDa00zWO5gFzTLdRszDq1TJGQ3uoOM12U9OxHiWRyn01IQ6FRJuZ7CtzyzEhnCM%2FJoNC4JKB74RxX6w5XDHvWswicmRwHxgG21S7sWr2aMoYirsgYi6Xu%2Bi%2Fb1VyZAxXx5Ov5fo6z2n0%2FCK%2Fb8CPY9LDcqOIEwSAoYdai2M1Adi0z3b%2BAb7IBu9unkQeL%2FqPgCbFw5thDCK2hRfrioO6u2klS%2BKJPUBgNy3uy3DLZBSE3QTCg2U4PJ9jricTYzdK8U4ovX73BrEnB9v4ZnGnN4e2Mx3OuJOWYs3Zas0pBM%2F8w2oWdvQY6pgFLXv5tfzzbWx8JULXNY08%2BRP0citaf1Llzp23ixPjzE1V6IW%2FWjFHuQPRkPrmMaII54P5X3XPWumzu0ivjqsn3%2BBMPQyiY7zOFUL4aGfvvnkAWsWxm0ZMumNntx%2FIF8pLv7jJGUDYTqTuqIdOkv46XDhJHb6tFkNJn%2FV4F54c%2Bi7g3ZWpTICKhas%2FBKOETAjXqJLEoJ7J2TZNCcek94GowZgaSOGPs&X-Amz-Signature=de98167167a02fb39f1d21c6a2880b9d5144edf9d170ca4aaebfeea0fc117dc7&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2KFGT47%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIE8lfDqnRx6uq3gCB4i9XnGaszfPKVja9iACcNrHb2Z1AiAYLsXupLtDJOpghXLF%2F8aS7MNF8tP%2FTMAmsGfLpTiRESqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMa3PcC5jWIJHI9YDbKtwDhA3rZ9mShG6DnJrNrgg%2F6LWHpKrxPcDzupbNFctsmp3yO1yyp39kVDGTMnghGzf3PLNHXSO9PnRLJcRGSzb%2BvGXHJgcMSj3y9tC2DsHuAmYX%2FC7RWxIDhIq6A2dtzk2%2FRvhijJUCToMjX8%2BR6VcRA9SbK5hN8aFio%2B0PqGQZZ%2FubIui1i9ZNlq7UbhMH9tYVbvumniBHnFWjtP4dYzGcY1W5P%2BW%2FqC3ySZxMy7FMn8ZNlG67vmNM%2FWzeVUbU1TtxdemV8XWenqaMZw6AGtLhwHVo884cGB1nKncWhWXXOgen7VLWtl9UTZ2iru6mEkUxbqkAAOwy4J8LBTfuDa00zWO5gFzTLdRszDq1TJGQ3uoOM12U9OxHiWRyn01IQ6FRJuZ7CtzyzEhnCM%2FJoNC4JKB74RxX6w5XDHvWswicmRwHxgG21S7sWr2aMoYirsgYi6Xu%2Bi%2Fb1VyZAxXx5Ov5fo6z2n0%2FCK%2Fb8CPY9LDcqOIEwSAoYdai2M1Adi0z3b%2BAb7IBu9unkQeL%2FqPgCbFw5thDCK2hRfrioO6u2klS%2BKJPUBgNy3uy3DLZBSE3QTCg2U4PJ9jricTYzdK8U4ovX73BrEnB9v4ZnGnN4e2Mx3OuJOWYs3Zas0pBM%2F8w2oWdvQY6pgFLXv5tfzzbWx8JULXNY08%2BRP0citaf1Llzp23ixPjzE1V6IW%2FWjFHuQPRkPrmMaII54P5X3XPWumzu0ivjqsn3%2BBMPQyiY7zOFUL4aGfvvnkAWsWxm0ZMumNntx%2FIF8pLv7jJGUDYTqTuqIdOkv46XDhJHb6tFkNJn%2FV4F54c%2Bi7g3ZWpTICKhas%2FBKOETAjXqJLEoJ7J2TZNCcek94GowZgaSOGPs&X-Amz-Signature=52314205b8f0bb180cc76f82d4c78814f0d8af1099cceb7e3d7df3afa9459a16&X-Amz-SignedHeaders=host&x-id=GetObject)
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