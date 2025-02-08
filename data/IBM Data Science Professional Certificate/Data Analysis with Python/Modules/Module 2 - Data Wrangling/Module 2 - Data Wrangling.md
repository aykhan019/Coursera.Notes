

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUZ6BB6S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCICzkQz78Hasp5O9FeAM1%2BJNoj%2BmmWT3CHwqCMpYPxLaQAiEAvCfjox5n5at5HgmQSWccXK%2FY256N7v8UAIGP8cAt8UkqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGBzYiIGGrRvEjYgvyrcA6AaVfTjLpDMJSN4F8bj0zveKgHQOouOJR8SHV4kw6M9%2FFmkAXYmvvfV9pglE%2F2KNSqYDwTd5lWV6651%2FJ9CP4EyJBCkEQ%2FqOqHiY%2Ff%2Fkc%2Fov0U%2Fub6TLP4Gdgwb48Fd7x466wYyvKXyzBm39AhhRUX%2B2CKo9IfmxI3c8UC%2FIXvFfqwwpgqhCDQXAW1II0Z5Eu8qC%2B5PpLG3DgNxaxfLrNNOK5QYRikiONwb5tTOUm5SBLni5zWssqi5Nmh6rNPSpf97qxG5Qb1UtOpXqEVrk%2BUZPxdcvHPQDclQIGR0PfoO98dxFS1YYGxhFhKJYzfr7k2sAOHhxTPnbS2jbW1Fxp2J%2Fi4nm9TdYQHFoKT9zWl%2B3iHZc0U%2B76TsskL%2FXusvf82YfcvmS9h3kjVl4zNyiViDHxlpOLwgbYmUQy6APAz3gX5xYpCB%2BrB%2FwF73Cq1iUrQ3nQjSFOkiZvGFwSReQVPHlfiXyDlRm5fLsguPAoDqaT9xvc1WTmcJ8xy5%2BnvFKxXvleOmR%2FrfceX7CjWU2hFs17iscRGTQAbYEYKxAS8FqLrh4HfGKXfrvzmExEDk1I44f1OjBZhE1k8EyDzlRwElEdBIECcs2V4ULeGvj6%2FrTDivcEePIT8VJ0FNMIqOnL0GOqUBa%2F7RoY6KA6XNCg07pOkc%2FP86hFRAscB0K5FT7LCTplpujZCesCT0WjGjn6EjQHs6QGIesaY%2FoEN9TEWwUz9ZN0GQJQeLWDbtozVr8Tqe8TkcbRlvy0gujSE8Dp%2B1JHCp704D%2FmVS1cuPKbhNe3u6cqg9gbMINO8qlxnX0%2F%2B6I1Pi02IX2VDbkhFjgazcqbRW7eEcsbYxQbIFOL2wt2%2FC2NpGhkJ6&X-Amz-Signature=f6b0b3ab08ec88fb6f9a34eaec6d5c5c27e954e067fe9cd636a70788a09ce332&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TFPD5UF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD%2Fh8CysHlIcOe%2Fk%2FLJZ5DVKUyQeKHQgSeQV3AHLJ32aQIgX2AFxT0SHbv9Hc%2BdEJEY7%2FEHCmDyOW472%2F7HBMxnQqwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2Be7AcOXv%2FTDCu%2B%2ByrcAyOxM2St14Adau8JwFw99vColTWoLQwlT47QIGDP7EmtFL%2BHBqm3pbTCi7DrtwIoF9owqVoXGuNe3wajb4PEWqO4f504TLFO8byJYMUgu5JMt%2FJbeBCzJLQB5VH1fQM9DKv2hl086H9lvYEnfMNm%2FKg5Uw3lEFGt3m2RmDgtMjZ3c%2Bk14qdRHSo4J22ujLg9CzgGqdaXoT0D01FUKmd9qvNQYTQHlwwS6SBjv6VJHo2p%2FDl%2Bp%2BCidknad3%2B5%2FoMZMYVpoFmMlFgaTZvA0IHnkyPMNsqplPA4eYUyu46CMCwk6KfcV77JXvGAPmxKpRWcuMV%2B4ysd6RBrNmHDvJbqrqxF8CTAdBfR4wDA6XTrbPlVP6J2d51viKQFnXBnu8RFIqidbEFJAo1Ora2FH%2Bya8m0k3AMSwkpqRF9puk6w%2FNOo4GVdIzBI7q9rWuYtemg9Qn5mxoWrRMHQu9i4lnSvXIEslPspwjOjYD7vTQhgqv%2Bs0wRVXGjyUlPiURbpU7YwK7dLfW77KmldfBRP1K%2FbW%2Fo6Vf1zYuO38blagvpu6lN8qDM%2FD4T5vtiHKb%2FMm3IOAOFt8MVnKlNBY%2BM2lXdgVK7ZkuTtzDdplEwJce0bbDHjH5EsftS666QxJ%2BYlMIuOnL0GOqUBSlfB64XkJtsZDF7tb%2BSYrwUGDgfPQQhRpBtOGaKcXyThDWMqYQf%2FbNKG%2F9KS5bC1MtDyTtXa%2BxEyPhwKb0wSKHyev%2Ft42UkSZ4dk8WJYTbbgxAtxwP2T7oMMsopXArR9RQvQLj2Xmm0pVOA2UehtdBIU3XwWJrTUEFzI997sy%2BPpAklOVJcPA0C8yGVyvMuV8FeElKz3X5eaFDCsHdadvairgcI%2B&X-Amz-Signature=12111ed6f58152d86253dce63143cb4aee1eada41ddb116ebd0935134802b215&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXVO22U%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTN%2F6PSXjgPCmXuI11nVUfkhh4two0KLICHPegr7D01AIgcjkHz4dNpVjsr7kzDeyqcMiPQ0s8EGbgnHE28x8Kp1MqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB0YRyFioltIxV44wCrcA37DTQcXn%2B6KNVJtv3rBUq%2FeGCRjPFPlkXX73YJmH%2FTHqkdOdvwPGx%2FDSDxQ9OjRO82RmdaBErMpTGkbBxL1ISsenApxHU3RaBxUZUtfh7bByLeW548v%2Bmzc9qNtTEcnYtf2zIeIQL5ViDq9ylXzP9r0nZAOHxkaUgDQC8NMMT5EWrIA3b6f1vL3Gur57VUNNxv0NjfKx8%2Bs%2Fm2UlumZdlvgE8ZL06pKyrYEBQQb3KmKb%2B%2BrkDY7V7%2BBgLvVLcgQyCdIyX%2F53J6X4NQa86w4RNDiujftGoSLnxy2DepNQW2mARH8Zl8C2IU1qFgnsCg5s6EIYjkyVg4LQASKyfvPLF2RgSavnw1iBhl80MW5gTmWY0c%2Bj%2BU7Fr4%2Bk3QeYPUW9bsQKWen8FEg%2F9w9xZpAgDP1O6X%2B6Viy%2B3%2BkpCOX7SKFsGXsDGz8lDHJxrsLNmpD0uQA5WNFwj1Cfzn46nsNjCGgVZaVK4JCGCoG0kiAolDUt2Cyy919owZB6ITAbN2%2Fak4Y3KfoFkWxwyrhExOhfz%2FFDkI42c3Ima1aryaiuS8nYYRncm4UrDOL0YT%2BDBfbUP3txVqbaptDrMaShfoLiz3AkHptcHkEblyAhg%2Bka24kRgKrrf5%2F0AruO6MMMMWOnL0GOqUBh6ncqd7rhNt0mgG2xKNaJeblDm%2FJhmtNp16KBA1hi%2FUl2box3tH75hLCrOvsaO5aVQUxoJPEO1TmXzLlX4K95F2YBmGU%2B2hi6jsUfocD1GYzZmjkJbgYBpuM5SidJUamBv8CXFdnkKKxw%2BfLENAJVhiW8O6zR%2Fx7SgYuCvlVqVAJ3Kp46cOMwQ9vpats80DlbqoRaUhxrEt3StrAf06FY69DsgI8&X-Amz-Signature=da59e075bb66f24e07f00e759299749aa733908bceb6b127361bc5171f2c20eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636T25LY6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDgYvjEZdwW9sej7F67FhIKZSv%2BdWef%2FIc7KsT%2FkMWBwQIhAK5zY3aij7oF7JlE71qK4jHS%2B7vjTrYAck4xyGtDKIkSKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2gKYRYOSBeMnGjnMq3AN%2BZckv1UiUuzdvyram4Q8LVSzNhTYON7Oe7D1s7pGjPH6fpOyXpJg0PIFyBULJF9UDudr6wuLwWuk3FQ7sHHWuLrz4ExgOqR%2Fx6HrGhbS1K6Ix%2FDDetNLsxpLzHpN8QqfhgkPmLo0H2aTSY2Ng%2FjB4DR7zwop3LV13jCqZILvz44iaoped3HCbMnB9NFSAjps3FEPH605%2B6WIrK9eEDdjz1dMy4tCH2%2BVJJdDd4dDeaNXlEg0zJFy5U7jVY7R1bS0vahhFQLYUyOKgUzT09l%2FMACZMZybW33OWEG0d%2F4cJHjn1cKMrEhyfEAZNteKWT%2Bp482WfnfxhyPmFyYYN8lWuTY9a43jfRutulbPdL2sAV99pUFo1aQvlCWMFypAyBmjubAm%2FUodw%2FReC9fGMCg2dULAQarpmXVaLCJtkrQfxg277Mx2UXFTWjGKYB7G51lXzMO6ZyJ%2FZz8%2BlStBYZbX89kPLxdgwPvEBH8IjIj7as93wr5s5G0f78zpjoJv3owsTQNgjVvjAH74LnWTRV8F667yLAv%2BiZuhu2wT3II9gCEHgY4MV%2B9Y%2FRqPXNualFfXsD9sdrmU8jFuJxsC%2Bc2lTGUKHzffjA%2B90QklN9d%2F6X66RcNRklnBP%2Br%2F1bzCtjpy9BjqkAXKiTg1eFLZBhKwFbt%2B8uOnJzlAuq3fm5Qnf30jqf2PU8I6zdOLJNBqXMKa9QO1mCrBGwXU1gbhtZAr%2FIscs4OYp2YpiAmDx%2BvcTk7yMZ0HEVRwspvaIAtwTxi5lvuj%2F77VG3lEkU9e%2BdJu97Wher6qhK190A3RZMY%2FQJQYbxtnXe9N4qar8A0t8bP0qn4bycbZ%2B5j5CXXol0bSS90VNm9ZylVSF&X-Amz-Signature=8c0c4562927f5bc5621ff9c19b98916c317ec6d95f3f1133313c66d6cca14994&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZMMMQ7P%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICSAnVrfjrUwEk5nlb5yK4Bz9hxGenrmHVJ5JjW9vpFWAiB%2BeNrymBHqBGZivCSUAW66EAyUxCAriZdqTTazYxICaCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5T3puQTmo2CmyiUvKtwDfgPTJAVIHYBmXM0hbsd2i9AdDUGqXFYovPpodycrI1oOH1RHNZ1e7wXkV4ZUqDFRRFgAjoV%2FUu6BWONaV2ipPyElo5K41MmyHTHhaERRlfyIoSGS3gOIuZ6D2YO2BPzyhSVUBHEPrJOAVdzMyz9c1uLmO37ImMouyIKwh5YYXZ22WgesHSyJSLmTuUHOPpyd7ZNENFnJ5NHQPVjGA7iFrfjUzgEEwJpgfJjE18AlfTr3XelvzrRKPmPzNAKYuYzKksNK%2FOFepfSA%2BTUex6Axt4S0LU6EtkDIjPtP6divmx65f1KffCGt0oIAPMJpXCtKo%2Fy%2BWEDqbjij01wf8ZmUpR5ODRfdjB1W5O3S4h5azamTB7gl2vLrtYVgYnH9usRiW8Gyj%2BVjmN%2FwY0xozYeWKTvw6Bl7Z20q7TjtAItIe7DmPsXwvLMKzEd%2BAX1ZjozHO4cFKSLU2Rv%2BKX6ALbV%2FqOmNjUwd80SiMJP8iGECwt5U%2B6fQRGromWREGRbKVNSwp456DLZLrx8ZaP2wnl1b4JnTJTJcczoT2OHzjBFXsOaNzMESH439hgar8%2Bg%2FOfk%2BjMAH1lmz0yzmsIjXumXuHgWIjbW3NZD%2BEyOLBYhtJGvVRxb0uucJ8eiLHNQw046cvQY6pgFstCC1HJHnhXcHh89ucujz%2FBSG5cU4H6tvfs44%2BqEp%2FITmI7D2gzNLc6XFNIM9F7HedKCKQSMAsFmD5o5RiMgJeM3daGNDhZaSM4l4RKb8v4d%2BDoxOpEO%2FSkvECSrpNzhKuRHbOEujjTSNyLHQdTXtRf6U91mP6ws2W9yr86Re98p406igVPTiSVyAvXQtiXBmwu4EP1xXmf8ScCJuXoxvjwzARMTO&X-Amz-Signature=6c76f1449f8da5a98a2217a19a081649b89f2202aff3269bac1f75429b8d0eb2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664V6BCUVE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIEEYiJTbxZGNe%2F88umdqpNM96UcKJMduIDTr%2F49xqt2QAiEAjILOvq4bYDkrQlPyUeu9J4ak%2B9druhFHLUIbvOgLiLAqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNqSVMwtisw%2BF5OISCrcA2rnugxAQ55JvXVanZYBpEepqshRBzpkjY8cIzRBF0zZGm97bLzPCLr3of%2FqrqYMCtXbi6wCD2hDi8MfLCsylnKkfO6npb3xJVSjlkFHtgn7olBKbR4ln1sYNK0dqvIN%2BLI9EosgBLCM634N1Aisj5B2HAwZFooBnUEmC55f7xHLrlWLskWKjNlhdjmAkvHDZY9fJrg%2BqavOSxp1wkZaQym8d0moJObXc44nzW7XbGUob%2Fyn1AtjfmmR9pwKQWF0Gg%2B2SycRtdQ299crCgKlS7COlL3GWEbhm702%2FLNtuDDaALESWUwWMbuGnDRCs1ZKsH%2Fhy1De9ZKOnjNmIHG10gp6FsYOZ5u9VzHfcAOu3L2JqZohOr3M9EIY6syoTAbqAqJDNZCrWyVNVVypMYovWpEk1Wnj8c9HOPblxjcb2pqAlAV%2FMAutrAENAmHbtFItBfWdZXyILzUOIpBMDRkVYXUxPtcvekwRpZj8gjJhklJZAfkWwNmG63Uw%2BtW5lme0aIuaLNDS7l8u50A4uHp8ZX7yn4nF9XFfcmSiIp%2BYEbiq2AzXFClEgSkzk4lDIBD7BOt3GbZQwmt2p3BpaRgp4YmMRzopu6vmbHufKB7Ej6xb%2BTekc2Zq5VDV7G%2F%2FMNOOnL0GOqUBxlg4XNg%2BkK6gD0vWUX77LEM%2BxlGJaq3xy9yrSYz0DxgtzEE2l9XTl6usykQn%2F6zf2OJpOB9ozs1sav98WPiLkuljT6u2eMejxqO4CqDhGMRlQE63mC3Z0C3CiVbW8wsgNTIp6Xz8q7vZaHH1zHen1e5L4MVnc0ogbmKDLtflbUjhe9bUjbyxoz9jyKJlCxVk0FlVhG7mK2pK9GgfzKwujCwI%2BXoL&X-Amz-Signature=fc7583e390f1367a5dba7633d1781aa164df2d3a8df4f5bffb9ee0087448ca75&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GKQQEUX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIBGsEpg1JtZ%2Bt%2B%2FxfcuJLTeiFuDKrzl6ZjjdyQsEtpIIAiB454IIqf1k2eJWWgbPXLBBgMFQnIOMDNXM7zlSSBvZPiqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM72LonWmDjG8ajGhYKtwDc%2B3mdi1qnbK8rOqnw2SWZVQ2trXPp8KXShAh4m9tDosIQnVJjWvlPGmYrV0UIU%2BqJSXULfOGxQFy6IOUl86VeFDg6TKyWzfYp3rny%2FbYCmM5LSSt7jWc%2Bvoxme2UlDMmkLGNTEgdSuGWkDZsPs3%2F42%2B6C1UxtpvKI5ArbgPyFjGkBXj2V19%2BJq4SB60Gk%2BX%2BQaAwDaIhZgcWqw1xLW%2B%2BvmNbdJ36yAMY%2FvnZp3IN%2BN4ADqu87Z330wIQDlTCEfzO3j0dLMoCWxGqeZFrWbrmrNTjXsoQenClfaj%2BnnaNiQMfArmEvbWjMXyh3qciuT%2FqXozG%2F0SquqVPCaQ%2FwFhVORMbRPsRCerQhGFLP6LqhS65k5uLtdUCdrhIue2Z79Fz5rznEIYw1VW%2FVUGP2I6ofD%2Fuz5FAPGo4xkNqICPl6kDaYZBuZgfcxZVTw%2BM1YA3T1LxKKi93ig3%2B4VndkDi9aGyV4CWzFKYBXOo6E%2FwaJi3GJckveNFqkIQ%2BTy7T5z%2B106cR11w4iDNEQaa2E5lHGBmQAZ16xV0%2FKbg0v70kecLvawKoxWxG8SI9d0zkmmRBigsNMlItWLCWN8REtO7MArrPojDdDHOEhaRLaj%2B25xN53vECPLYpaWOvK%2BEw7Y2cvQY6pgHU2CvDorIEbyIsPAse8MmhdRPh4qV6bwXUcPlhHcg70AHwy%2B0TuTxq3FK80OCTx6v%2FB0z%2BtY9kno%2BziVEWPS5myU3lvPSeHfO1xMvJPltUqW20cxPCK9TKsmufRagjd3cITIXPID8FUWvLUdy4VrBCow1Slv2z5XAT9X0cZMXewmg9LCgYJmdkIGUhllmK22ybpspo%2FP%2FwAoRGRYgAUNXDgciCxmac&X-Amz-Signature=cade3936b1e8088d7653ec619af940a8ebfb51284b863454e2becd164880cce6&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466646B77RM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHJCjwI4K16gIM0ZTds%2FF%2FSJdAdfMk7cLBDXkqgYlEF%2BAiEAjAPx%2FwDuqfHSkIGXa8fQYr67vzqJm4FA5GSfM%2BM2wtwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDCU16Z%2F6Z%2FG%2F6WigCrcA%2FLG8%2B5E%2FT%2Fg7%2Fj5mjRajJWwnd%2BHuw3J%2BmYaSBVzXYI0HplIULA8FlpxcgFw2meytE4JDgwYuAKMH7lFs3wV5Z1uhi%2BsWpbU6vgOdvALhg8Fzi%2BbIu4f96d0XM7ljbEdqGY%2FWqtKYGVCstXHOoTEo5zN0ve9gFBTkCY4LgLIZy2I3bUJYXW0Je8Pmb63j8xgy7wOoTMz6YOTBUXzsk9VE95EhELaVkQ7k6vFX%2Fa9ZifTcJmy%2FqRKP%2FO6US4XbmddE5SS8ECNnZik%2BtqbGgH1Q5ihbxPW1SvQa%2F%2BJIpqiO618eivwuVCLTr3WQvbW%2FzBgOdOHAn1%2FsQ0s5T482uo4epmZiIaBDEgciClHFIYK2FGbWrvk6rIclIfHshpMjjrxmXCf4Y5Y7fJjkk3%2BfGLAIYW3PipBtxnKa%2F8Biosx4G7eun6KjeUnVF%2BYwpNSXfaFRVDeoNeZkLQGEUClnae0whYjpiYWxeS8RDofp7lJn1CZu5kaYOxOxfeyO0IDIfghMEd4rTlvEBc77hqDoSUb%2FvuHGZzFhuml8Cn0iQhHzykcZdFivaMjqRGhwJw7DWndyrvvXj2XSrayrE7%2FSodsWC3KtO6d0p2IgnvJgJwcf5W7MLA3UX%2FpmTcCBnIAMNuOnL0GOqUBbNAfy3C9kElWWRYl3q5B9Y48ZdYtQoVtmIW7YWiylnLXnfZoknJPBpkRSbQa6VaMnOn3rlF0Fc9Dk%2Bt9nsg90eOdJoxYmjajUqetYIVjbXn4F%2BraPQnktKmlWiE7UiSGe5628VmGpudS%2BdbgEQjzWV5DGiQefnmeG%2BRSIP4TKhKdZ3LvNVbMbl8KLhEPi5iuUF1h9KeMyWqnKfNE8JVkX8lKu3XS&X-Amz-Signature=bbdd9dd0c6ed3679a12d8bcc1332dce3b22e42a408a981f6822789b08b11e0fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZMMMQ7P%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICSAnVrfjrUwEk5nlb5yK4Bz9hxGenrmHVJ5JjW9vpFWAiB%2BeNrymBHqBGZivCSUAW66EAyUxCAriZdqTTazYxICaCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5T3puQTmo2CmyiUvKtwDfgPTJAVIHYBmXM0hbsd2i9AdDUGqXFYovPpodycrI1oOH1RHNZ1e7wXkV4ZUqDFRRFgAjoV%2FUu6BWONaV2ipPyElo5K41MmyHTHhaERRlfyIoSGS3gOIuZ6D2YO2BPzyhSVUBHEPrJOAVdzMyz9c1uLmO37ImMouyIKwh5YYXZ22WgesHSyJSLmTuUHOPpyd7ZNENFnJ5NHQPVjGA7iFrfjUzgEEwJpgfJjE18AlfTr3XelvzrRKPmPzNAKYuYzKksNK%2FOFepfSA%2BTUex6Axt4S0LU6EtkDIjPtP6divmx65f1KffCGt0oIAPMJpXCtKo%2Fy%2BWEDqbjij01wf8ZmUpR5ODRfdjB1W5O3S4h5azamTB7gl2vLrtYVgYnH9usRiW8Gyj%2BVjmN%2FwY0xozYeWKTvw6Bl7Z20q7TjtAItIe7DmPsXwvLMKzEd%2BAX1ZjozHO4cFKSLU2Rv%2BKX6ALbV%2FqOmNjUwd80SiMJP8iGECwt5U%2B6fQRGromWREGRbKVNSwp456DLZLrx8ZaP2wnl1b4JnTJTJcczoT2OHzjBFXsOaNzMESH439hgar8%2Bg%2FOfk%2BjMAH1lmz0yzmsIjXumXuHgWIjbW3NZD%2BEyOLBYhtJGvVRxb0uucJ8eiLHNQw046cvQY6pgFstCC1HJHnhXcHh89ucujz%2FBSG5cU4H6tvfs44%2BqEp%2FITmI7D2gzNLc6XFNIM9F7HedKCKQSMAsFmD5o5RiMgJeM3daGNDhZaSM4l4RKb8v4d%2BDoxOpEO%2FSkvECSrpNzhKuRHbOEujjTSNyLHQdTXtRf6U91mP6ws2W9yr86Re98p406igVPTiSVyAvXQtiXBmwu4EP1xXmf8ScCJuXoxvjwzARMTO&X-Amz-Signature=5a6d2a8491b60d3119a0410be7a8b6dbd273d20dfdffa9f40c75d50da596a166&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4IYKHFS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCMVSG3itfNo2GRyI9amgItP1Gh0DI%2Foo%2BGU0qXqc%2B9hQIgBG0tUnkO6%2FHX8hZgsewf7XYRtZMpz4dpzFUNcFggE2cqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCp5hdNUQx%2Fuz10odyrcA%2FWERJjq0OQyd4UmRv480OHKMZbIuM1BYOWjCjGuLP7lsnGetRDAbDrleBVFEF%2BMEPcBylpT%2Bx4GOpels9flzfGdEoBxIMsAs3JpjPzIEZu4SzG2TAdhzYixKXldL7cUDlyBPAS0BeKCg4OIbptRhRpcBMmtfKkffK2JJ608lysSMziORcsgNIKTZm3T4oIyZYPLgeaDmVmgStwld7RQn0GBNHcXoSvrSRwNBe8KLEhW3gCgvB2auIxKM0psnVDd7PwEtjQtAouc4xi%2FStN70zxfjQ5%2B93frYMK1Uf6pq1pV297BNj7FS1SsktlD74OgBwq%2BgrN1DINY84PpS1wppAFaABQKQGSrwkBXVO1y2tZnLk7ICNTaM7D1ls2xOw5iEjeidVeOmleicq7Mwys7k1jvToDD7E0Gm1GmaMGlEohLJihWrQ2HfTW%2B2QbPMv105Rg2C5GuUtkx8cJPQY4LqFbHil8MJ83cQ536Cmm7SN3oq4aewCoojshLa0RLiVsuRSaOW2Hy1kQUF9%2Fu7DbTUE6cBXC4GZ8qFtnohaZ6iZ7kKYTkTEpAMrlKvGhAi5UH8a1WyCno3DUg4fP8qrG40onCMyKbs%2FLuRSfDQ3bE5OnusJAU3phUy%2BF7nMJ5MNCOnL0GOqUBeq472%2F1g1bK9x%2FJanxpF9stwPe4ypCHZkYYtac6EyU6pBCd6uHra%2BH9NzmlQnPkeK12i%2FK422%2FcNGfO0sZ08cL09xOKH9ynY8EYVCjr4c3eQePmriEl%2F9%2FivDAuj331mr4fDuVK6EYjVKcUMUWISqsb6l4jxdHBIhp6XiOJJR%2BxDQergUNAjsGPN5CC3tFsTrPOsNgQSFhVwn%2BvlDCoZtS0A5G9r&X-Amz-Signature=86b17e4cfe2cb89d4e3096dd13808125b96b0643aca2548b25d332c2bfa1cc46&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4IYKHFS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCMVSG3itfNo2GRyI9amgItP1Gh0DI%2Foo%2BGU0qXqc%2B9hQIgBG0tUnkO6%2FHX8hZgsewf7XYRtZMpz4dpzFUNcFggE2cqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCp5hdNUQx%2Fuz10odyrcA%2FWERJjq0OQyd4UmRv480OHKMZbIuM1BYOWjCjGuLP7lsnGetRDAbDrleBVFEF%2BMEPcBylpT%2Bx4GOpels9flzfGdEoBxIMsAs3JpjPzIEZu4SzG2TAdhzYixKXldL7cUDlyBPAS0BeKCg4OIbptRhRpcBMmtfKkffK2JJ608lysSMziORcsgNIKTZm3T4oIyZYPLgeaDmVmgStwld7RQn0GBNHcXoSvrSRwNBe8KLEhW3gCgvB2auIxKM0psnVDd7PwEtjQtAouc4xi%2FStN70zxfjQ5%2B93frYMK1Uf6pq1pV297BNj7FS1SsktlD74OgBwq%2BgrN1DINY84PpS1wppAFaABQKQGSrwkBXVO1y2tZnLk7ICNTaM7D1ls2xOw5iEjeidVeOmleicq7Mwys7k1jvToDD7E0Gm1GmaMGlEohLJihWrQ2HfTW%2B2QbPMv105Rg2C5GuUtkx8cJPQY4LqFbHil8MJ83cQ536Cmm7SN3oq4aewCoojshLa0RLiVsuRSaOW2Hy1kQUF9%2Fu7DbTUE6cBXC4GZ8qFtnohaZ6iZ7kKYTkTEpAMrlKvGhAi5UH8a1WyCno3DUg4fP8qrG40onCMyKbs%2FLuRSfDQ3bE5OnusJAU3phUy%2BF7nMJ5MNCOnL0GOqUBeq472%2F1g1bK9x%2FJanxpF9stwPe4ypCHZkYYtac6EyU6pBCd6uHra%2BH9NzmlQnPkeK12i%2FK422%2FcNGfO0sZ08cL09xOKH9ynY8EYVCjr4c3eQePmriEl%2F9%2FivDAuj331mr4fDuVK6EYjVKcUMUWISqsb6l4jxdHBIhp6XiOJJR%2BxDQergUNAjsGPN5CC3tFsTrPOsNgQSFhVwn%2BvlDCoZtS0A5G9r&X-Amz-Signature=d82e5ce294aa5686d32ba87063c1c493b959d86a2cfc9aaa79a21a98095a91a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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