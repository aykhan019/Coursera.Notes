

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRVBKF3G%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCb2iA8fQ7%2BZiaMNXR4AxHV5XDVcO0BKtJgFrG7Y5CUbwIgYpjFzxCgKnmSRU2TQI0HCqQv0mtGIaUxREYPeABRutIqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP%2BzpuUNmqIvQPPHcircAzPbp9P%2FMVcDe%2FFKQTVOKh8C40xb8fRhkY1wHdHB%2FM9f46Fxmv%2BZU5Vs9eZT1HcSOmFUYSNZRZnXoFCaRdrp9%2BFrpothMOQFpQCAtxP7YHnBKBPniiUimPg6W0PtqfuiCa2g4PzsDp8Xakx%2BLbCRwcsjJvkwFUOtKZ1icHx0mVlpcWIaoR6WCbFuPnw5hX7RCt0JKX5DOAIA5g91NocBK%2BBnj5OuqkQhLHYGTKmdZarDYGT43ZTUzy1FjFd%2FwADOMItEuAxIzTLLfALIWgaUKMJ6xlU4LFwV0eoqbpq%2B86aJB8n3irdA%2FXYlTQthDanmmeOphq0bkdYhjSLl%2BInbCrOEsDnsJgPxKuiFujon1cRRCgf9G%2FNFpU%2B3ronBxchzE2tKOCpy8UrSHTbBbVIWHPgQpmAmWhfqTBIFJavn7d8KWdEHnNC%2FLHAbjtrxWPvQS7Dy0RsRLhrYJuGlqcrDf%2Bl1OOrjaZ4aFhCvPczWMaFLNbeVyorat00CCJYkkiLH4jIim4EnDhIPQwHxl1IRpnecawCiBlrCBOQeQwdu1h93zKq7UA6wVs9LsJbAX9MUAZr8sOJPVarC0tQzEXc8%2FsKGkEPuTMASSOtQ6y09rKoIMwRgLK9CwWmI%2FfIaMLD8ob8GOqUBTBakuOY8YYU4z7tIf%2BHxtfNcKQrGNw8YCn4uAIwvQ%2Fkbp7eI7AamrL3jFFpYWD6GTTwHb15P3sNxe2j7R7ILe%2FIu9%2ByUJcrex5E6K%2Fhp2piIgfQ5Xv1rUPZCl%2F95Pn6waVFYJRgS1Ff3s%2Bi9p484U99gaLHC6dr2JhVVOSToHH85Rr6BEZUYFiKH6VNx2mG6c8xEV3HEMo19t6SiT1R9pFttnFkt&X-Amz-Signature=60e9229702f7fa82d9d0363a0f0123620e3671b4959acccf991ca2b7efd8b5e6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOCHQ3DW%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIB3OGRSmfLZwQ7PHm6oZSYfltS%2FckrB6JasLUwYXtRl6AiBPyJLQ6373W8nsV3t0NxnjesYfYE0AX3OoSeuD7fdkvSqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbKWTmbd7axm2ccvpKtwDMhcajAWd%2Feqrl%2FgeryoaW0Ki2l65xrR9InsCr%2BEyT1C4QlbswcPNcmG0sokR%2BSTaI8eudn%2BaeSek78tkqyrUzadJQ0Jx09TB%2BGtSsUg%2BXJcBYc3l1iXpYQ8JudF0Y2GhgCW49p4ywJdWEp6ZtnfYDw59AEbe%2FZaGUB8Opr2OT4QWAhHFIB25DBOdOYGbu02uQ%2BYTK8pYtHG%2FZ19eBGkeKboaobcAU%2Bq3bsXAnTRLqQpcLQ2%2BObItt713ygps57HHDSd2VALZRnoIJuu7P%2Bz1gOb7FyK0c%2BB30bpwJ9%2F%2BT2X5AIWqAT9Lpqhh%2BniWl40D9cM4e%2BDCW8e%2F6ynwjgC5msoedcDHAV34Q98VU2LPk9CsITIUlwjBE8I30mkP4JX2%2Fnv%2B3HSVlTIj9obKGPC5HV2MY3c%2FR%2FVDUaGH%2BlKk7zaAEHXZF3Ao59yAF89pyuu3oqgtaefMrVTQSn4%2F0bmo%2BZqt1VfUsn6RDAZBRjuZK%2Bqi%2B8Bcdf5U3tCahNW4XFPyhz4Ayr%2FOyXDhl%2F%2Fhy6B9cS4rXq4xTLfRSLHckUrQsFAxkVLmF%2FFF%2BB8eMmR3fIT4MK9kEaOqc%2BwO6TqfOBkAdOaNoUIE5V7nj%2Bpkd2n9%2FtPV24GggPeBhnFicnQwrPyhvwY6pgGgksx7C8D1MooBLOmwFLmajn%2BEIUaHC350wLceKhALbT5RTSdS7s6B93XeB%2F8EW2u%2FSPs2akPliqAxUqXhvQWdvV9Zr9RHrp6FXExPsEn2VFCBO%2FUOHk5tYxoXnUCa9l61blSxXuyFi%2BGrbxwqGH9S%2BmEciRM9WGMWhsVXDqaUhP7c5CIQhHo2N%2F%2Fe8EIaBOotS991hBwqwENTiuJZYyvuIFOHKuMJ&X-Amz-Signature=7796a29ce6d5df858b8ca450e9143ac2edeedfa09e9677bf5ce9c9656d3f6bc5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644CMKBLA%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDcoaiHNVsXBcEkwy8n8hhtKSpwEKZbxHUmOgA%2B8x6BpwIhAOMvr%2BYON31PaGC2vldP8QD8lkMcX6XXyHlNZUVSEtdYKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjwMjbLKAw1yT1GHgq3APGqBcrJ2M7v32RpPY0INOCC4OmE4KD%2FR0tQc1d64lEcnicZZdi%2FHMXYo%2FgFbD9aLnrvYkNvt6kiDrwNAoPtbX4CU0i4Kmzrty21x3qBbwTlULpGHfKocowrEhCFKKCLoVSqJLTCVzmQLpKyxeyPbm1hcOMVO0kQqEQTyPZNbRrVYiFa4ppyPo9bXAJRXtIYsDcBzlKHsiP7ema3ZJecbu6ut46L0qFYEGUYCgYMZNsrcf822sLwl32FlQCx4k4GMtZK2%2FtJDc084%2BQ3ZPNiDvUjwsOF%2BcjOObjtS%2BqCo%2BBVlz1g%2BJOOO4zVyjmxEoQrq18BG6dAJVFt76bhlAeWsO4t811kfBaX2bpO7BVzLmkop%2FP3BT9e%2BoeBwrmH5c%2FLJE4pv9im8uQQUPWSqcyGJx1L5DlioXrVKHHqOLlNn2DfULfblyzc99iIo%2Ffn9dHzGAOASNurVpdfBizvKjPOUd9%2FnrwP3G5RYpUYRciNWLhL%2Bjf9BeGD4MSKkdEDAfSWctjjHisA0XRJZbh1gxfyPt%2FwVFm2%2FOGQOA42PGUFeCIq2QKpIrxd4muEprkYAZW7Wxdz5YNJL6IroUH5%2FhFfpT7uosQA9EOpkJNRpdI4d5aV0WJyEWC6zcyLCylKTDR%2FKG%2FBjqkARv%2Bu4y6B3SQXGLc9N38JtBtKCiiW4W8JARS%2FRrtM%2BgdAWTTmCK1fSUlpSZG3tCpO8l4EV0a4L69qbloGsk7Jrp8lNkxXleKotjW%2F4EzcHPSTTnBobZ%2B4YyYM2Nal3OrhJwXxWOr1j6HU2f%2BhnrT5d8XnEZ2h7I3Um7oL4vpQmOD1gqcGaaogkpipRhnkirQ0rmZFxucJBe%2Bs5GsDkvDiMEHmxg2&X-Amz-Signature=8a013655014448261b9e3d43d1afd478b98964f6e8133b8444eb009f6b962578&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZJFLIOU%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIDDBMT3r42tpKWUYGhfK%2Fv7wfusD9r%2B9F9Gdnb0eHyK0AiBlnHcdq9LGXqJ%2BzW49dLJ2XIkqDxCcnCkbF7s70W8SbiqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5bfhJV3OxInK8gGnKtwDb1dPx9FTng6nG0IOunO2H9G%2FIVDxbd%2F91K%2BuG%2FVvV3dk%2B2aj9NWCVpj%2FRlsHXuV9dNB%2Bk0NqBKDwNYY%2BPwyEj2VN3lR5MFu4rwpRWyxqw4Dt9JDG3OED53MBgMPleLF3%2F8Xvpvu4DAOLozNUUyHZaFb0zbESnYQtLxeiRXGp5JVhxeRAjiTT%2BWbWM4bBOUxjGZsVDmNJzAW%2FDGPpXbteW4Fv7IaWzik2UU8KJmLk0OrmUKLbUdNthpKn%2BUIAQOba5f985E90QgjlXBVhT1fzD1iNAhc%2Fx5aX0sWs4%2FxhtFVnJcouqZgsCNt%2B5p%2FwYq4sWeQdxxXuan16FxSf5ZHUkHqbIEWycBdGiqCpICehRikLY2dE1tSenv6HzTpLY8e6R2A%2BqWoNO9TsrdBe%2BixFP7sz7lnxBUGQx8%2FcHANilKeIE3pkrDBs1tgbOOKO69v3F0GgRRExF%2Ffcky5k7XzjQ%2F3zq6wx%2FppfKX%2FjikZBG04TpG4bHYAxdI6M%2F1tm3qE%2B%2FaJ8pwPLdt9B%2B9I0m5r54bV04LZndjuTe0yaJy1dcZuwUl7Oq8H%2F6csonXD22TzeXs0eXpJvhCixr9eIq2qjPOlXYn4J0HvgbdbGq354mL87ox9CqurXjayMtVcw1PyhvwY6pgHuTF%2BBxWdo0lvaOsI1BF1e9BCLyOtd9owR8LUIxARapHBpPiwVJ2BYL%2Bjjf1vDVCUF2vWyqhySS8%2FchGqoG3qkybmy6NWRhw32DTzyzjc8wMfja1FrivT7gPiX%2FjyuHBsaW75m9dVeLZnEtzmhS6Oy2uav3bfz2QIDokNtyao4vd%2Fjaike4fur%2Bi31XtAK1QKxjEoss1JMENKEPnFPS4JCE7H%2B3ze3&X-Amz-Signature=5491cd5a2fb62185f92465fb7f2786c368809943d4081fdf207ff599c85a9009&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBZXOGJF%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIEhV%2FRy6ifYi0lI4zSbHuZmZ%2FMtQzbQS7SFFrM6uE5txAiAEzJVKETJjgqHAv6ahzR9FtjgI236QbK92LxGjgvgGsCqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQoTsSnKHMZPJytMfKtwDWXk6k41DbjF17YBiKywnQq4Go2TjdR4RdczK2U00ktFgRsBuT6%2BdgsvazzdZDe69R%2F9xGiSyr1yHKbZRMLKCPmgHYP67hguakxOCJPqJYpqTifDKpJNWg6ReI51xAv1MXnB0xeZfbBJUUyiNCKtaGjE2w50uYTPRz8M3EyqjUk51KuLopECSRqY2jHEbZeSrbrCLUk3D06bCNqLDKeSsH3DhYDWvTnAnII8130WCL%2BgtxQpiZ8dXNO0Zltp33WcZUvXqy4W%2BjrFN1b73%2FPxGc9UG5mADg0MO9%2FvJdbJFkIjzpZCETbN2k1puCBykz4IJ5NYbnFy6pqug8ofcWSiN4pidFX%2FyKniR3doQ4%2BbmWsGVMH784alDdPPx3%2FfXCdcHj4yQxlGK9q8qKElFX%2FE9L1LetMMpinUhAM6W5pUFG6cI6BCB%2F3%2BiCP4EidWt6gA8toQ%2BTNZyfPpjMAOn4%2FH%2BXIlIqYdkhSFQqAXqJyJC2NCO91HTg30KzLvcWBnLORXrptFkvu97Pa0qHKLB1QxOIUvKMsHsWva38h0c2DdKTqS1wTiPFo4He9BLl50VsDXsOcorqYD9F0qR8wDolUn8iY9dBbGbmSIeFfqVNQlp2izT3lP%2FKbxDrkL4OegwtvyhvwY6pgGvtzNbbnDf6ytKNqfeoFoC9O0s5B7UdcF7RDGmU0p3K8sADGtUPr21KuuQE1CYLktvkdYh9%2Bn2wZQdp5ytjAS%2Fq2Uncbb4x%2FNbvXkSAQq%2Fw%2F2Ud5rkZg02dNCAfKMHcge8od5G%2FLJWcJS7LJTdtd0KB46Se5tSuOOJgV2KxJSCJ9e86px91skmg%2B6x2xl6oY4TqdJU%2FHsNxjZeKTdw%2BRK9G5s1xXcT&X-Amz-Signature=1a7e427f5d872a9dd3108942edc3e0ab770589e3e4679506f0903756ed1c3512&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YV46DFMD%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQDZuG%2BSUATqQhIjXDRhRNfDSn%2B16JjuRK7DEosaHS9TBAIgG6bROLcOA8gO%2BYfoOw7Z4N60I9sHB72jJc3fe9HADm0qiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLiKdxt7judvrhPElyrcA9SgvZrwPK0bzxFjNf%2Fzj2i9ktRD3u4lajKKUAF2aGoZEqgmTEiLPIYZ6jyTpK73oxIOnGEIFRaziSLq%2B9lkanBE0ZzwKOUAsjBBdNy2J3wCe1Ki3BkULWDlQdlQ1z18oCmjAmteFAF%2FLrhdl%2BcZrR7buLqAY9c9l36koIEJCLpz3WZCMeOdzPGL9MGpiB9YIl8nmt0LiIuKuoVrm0sgFbF0sguCnT24jBqkqV0baDT8kaoTQHCidCaFG6sYJQMM4gJw1zDMqBxedQy%2BQWgQdiH5rluzMvU43kKN2cmktRovyJh%2BC5gijQxDjUGZq8KlPvu6OeLY3Zp%2F02id%2FWj42kuXhIwbPFWGOWhSuX8Iwk7KfM6gxejviB8LCFNEvij84fGwONcQ5tcuFOCI03RxFrt5ahqOM%2FHOpK9eTaehmMIhFF9No4lWFRW9oxnAwjeRQ%2F2V6Tk%2B6SHBk3pkgLDZNvxdTI2UtKbQNksXmy7b9%2BCtO22xc3EMhiN6nRhrp9E7fPSVdPbYkPnd5suS53mvK61C%2BTFxbqnbmLWQS28Lm1MMzlKyW5pooqvNjXYtTw0m9ujdSHxaBJPgNFeyN0HkMrkAPXgm%2BFwoqjYbFZrduDpvuyrQbHCrnJbqIca%2BMKD8ob8GOqUBT7tHS9QuZgIsxF%2BfP8%2Fsh6M7Bd%2FAi0qigunIeu6qr9RBoy8QgOMfMk%2BK9j8wLdsqCOXPw3lA2PdkUSZw%2BXtE6MBV3dUZs2klXVgbrR3PtFRYeZZZuWV8qoKUW%2B0aKJ5kpWXnXT3cUNU%2B4Z%2BO0Jq7qu5fmQ2Mqoy5PqsoFAQsbjuH6H82WOqLYrqrA18ScG6krwLRTmW%2BpAV%2FaUQ3ZId7LvLTTwA5&X-Amz-Signature=bdabbc6cdb17f87751d5f85422fa097e1e2b3d6df68a310be4a4dd3709b0608f&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIXDU3VF%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDFDzVTomwdaquxUQt%2BTpkUEuU3%2BeHR5kGDCv7oWkZOvwIhALXxJgelegkFnG7uTOmk%2BHvJS%2F%2B3kVpTuF77cYrhPD8SKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwoiCC6tJxt66MuiFQq3APvhrdxxQm5lnp%2B6D7kyxvjx98Tn6TOk89RVjbetzTdt5CQ%2BElmZOeJKHPUPN4eqw9evGMHparIJ6zC2oNE1VeB3Zn7M7bh0T4ttujWFazkPW9%2BughWPFh%2FUE8Xlz9Tx0oyF8pMsHx9hQTsXJAYh40d5nLYTyvYyuVCw6X%2FVm18NheyTiq1YcFcnsD1cFY%2BqH0BkcEI36YlSIhLVuQMjts9OQaPw17aNZ9kP1kf2ONtLWGLF2444bB5GHEHena19TsBm3X23IPgvBZFCdXMzlJiXpuQvqXU8DqviAMX23zZeg2qvIWu7DuCklLnR9G4eeYLlQV8xaWHSu7Oz7teR6gn4s88b2XqdQ6G8AYLtahvbYrhUWv9hSm9z2xalBORKi50gZsdUmKNuNG6f%2FXo3zml6gqcO%2BS0Xltihxtu1hVYSDPDYg5a6sO3PG%2BmlFO2iVTdF7UWZ1pcW%2BUb9%2BGUqIZwQTZ5is4jCgeA9CNVil1yW5fh%2FELfRjKtimgRSRqExWLr8%2FiiJwrGYoJczyM2bHcehBXdCoY64f%2F7ldqf7CykO1C5rBLjjzJNL6bkhEpGjUlA6CKlrBqblPgl6ePBjxuU%2FdP2QE%2B0HJwi6oms4vR77WZojaP%2Be0TNhWpRcDCp%2FKG%2FBjqkAcLWBSpBTFZF4R5dTurQGUEBLx6cTkO%2BaYwX83l9raBcB0LS9a5LPa3qzYKGYJMkWNWQvm8FdRfp5dH7T4XA4ZsuehKKiCIlkedhG4iYKJYHdL8B2F9V2iFWaPHaTIZQhxlR1vK69vN09pOc7LZDStyLCuBffeRgbVhHYBuPSkDXSrlBMz9hSMUKHTY7vGF6cZE2C76NFXZI%2BaLwa5k%2FwUyvyRrW&X-Amz-Signature=9836d192b644d6479ad7bf97af52a1679898da0c04e3b08496ab29564e2690df&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKZ5JBOD%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCICcOY%2FVndLmAOrWomQYBq4hkxMDSEIlG5aPI5dcULu3bAiBLelk2JKkKUuaKplKAvDDar53xgP5rttKTqIKeIA1F3yqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMh8SAVH7KmfzFPkd5KtwDlsxWjJgI4BzQPlolx9oRjtI5EKL2r8%2BocutLbSCko1vYE0wrGeEoNzMMcD9Flbpc7WADLME%2Bqiwsz7Hm%2FonDRjw4ZzNJ%2Bde1QSLJtGGNNvHev0HREXON8cr4PJj4e2mQCo%2BO9TZG%2FdM%2BLcBDfL5lskPTJ%2BYC%2FtgB8y3yuTqogG2XkALum3QCSl9XxS7QzLnm88r4LJpksz5GubyuSxvW8EB5mun95gKk4TRtBhP69YPunBAvEUAOI95Ly6zsi0FUoG5WQzWcShIvdfZ7tdJmT2gEnD5v2vVhKacvm75PCTrI6Fy1lP%2FN9ynnwEFX%2B73py96aFAThhP2CMu%2Fg%2FCak0t7l6n5OEBdqHaI6BsveybShznhzzcM6k8hP2hr64dTKYSl5a5mX%2BZHGSd85owBwPDcDEsQNKnkAWXao5a951A989B0NRC6X1zIX1nlv%2BBhp6OyQaUllKTBDvAR4jwArk5tqlqjbM%2F2pG8z2Apl7UQIsVNzM5m5BW%2F6dKrlBHaALemK%2BAZykvzMEh0fd0gf3v19s60SSY4JxOYQLYWMA5Pw0YwzDQx78G3uYARK%2FoSzchHk1IctPAu2Q3V%2Fy0P2x4OY8KzIPKFOLDn100A9QLokH%2B1oQQtaFfbWwHOkwz%2FyhvwY6pgEC9NAokV5XBu1FtYqRCbyYQyoGYToM9glPR021DT6wStZknVi05xNVQUvJNo3PNeum6KmWG7biM4WEy4MA%2FDXh7RdJ5rim1pBdyP5z%2FtrvWItlXuLO6RPY6cqEO1%2BbBy7E999QrTJ%2BpO8v3pzycZJ6jftnHH7kXse7X55y8oZKhtx2NIBhSP8XAah%2B0IkS9Ai6Y%2BJ38GDiqDSgiqFd9bcKd7cFqIrI&X-Amz-Signature=677f884e01425b28cdc4c1530e6783ce40605b539ffed6cc6b6455b705c57d16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBZXOGJF%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIEhV%2FRy6ifYi0lI4zSbHuZmZ%2FMtQzbQS7SFFrM6uE5txAiAEzJVKETJjgqHAv6ahzR9FtjgI236QbK92LxGjgvgGsCqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQoTsSnKHMZPJytMfKtwDWXk6k41DbjF17YBiKywnQq4Go2TjdR4RdczK2U00ktFgRsBuT6%2BdgsvazzdZDe69R%2F9xGiSyr1yHKbZRMLKCPmgHYP67hguakxOCJPqJYpqTifDKpJNWg6ReI51xAv1MXnB0xeZfbBJUUyiNCKtaGjE2w50uYTPRz8M3EyqjUk51KuLopECSRqY2jHEbZeSrbrCLUk3D06bCNqLDKeSsH3DhYDWvTnAnII8130WCL%2BgtxQpiZ8dXNO0Zltp33WcZUvXqy4W%2BjrFN1b73%2FPxGc9UG5mADg0MO9%2FvJdbJFkIjzpZCETbN2k1puCBykz4IJ5NYbnFy6pqug8ofcWSiN4pidFX%2FyKniR3doQ4%2BbmWsGVMH784alDdPPx3%2FfXCdcHj4yQxlGK9q8qKElFX%2FE9L1LetMMpinUhAM6W5pUFG6cI6BCB%2F3%2BiCP4EidWt6gA8toQ%2BTNZyfPpjMAOn4%2FH%2BXIlIqYdkhSFQqAXqJyJC2NCO91HTg30KzLvcWBnLORXrptFkvu97Pa0qHKLB1QxOIUvKMsHsWva38h0c2DdKTqS1wTiPFo4He9BLl50VsDXsOcorqYD9F0qR8wDolUn8iY9dBbGbmSIeFfqVNQlp2izT3lP%2FKbxDrkL4OegwtvyhvwY6pgGvtzNbbnDf6ytKNqfeoFoC9O0s5B7UdcF7RDGmU0p3K8sADGtUPr21KuuQE1CYLktvkdYh9%2Bn2wZQdp5ytjAS%2Fq2Uncbb4x%2FNbvXkSAQq%2Fw%2F2Ud5rkZg02dNCAfKMHcge8od5G%2FLJWcJS7LJTdtd0KB46Se5tSuOOJgV2KxJSCJ9e86px91skmg%2B6x2xl6oY4TqdJU%2FHsNxjZeKTdw%2BRK9G5s1xXcT&X-Amz-Signature=82247670372abe6253fce6bcedf24a9c64ad04b3b308683822874bb897ce3fe3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SFWH4Q6%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIHKSVYVDhRWusbSuCo6a96o%2F3GS1NODsAKW%2BiY3G5S8hAiEAvLetS8Lzt0W3ZAjtuHmOXZ0WwJm8t%2FZ393WxW2IVH08qiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIcOohUXx02hQwxNsCrcA%2B1KA46Jt4ey1j77vXv1AyFRFjb8SA9nDUxxN3ngOCV4b32X%2B0iHSShX33p08eb5u7zneKFBJIiw6%2BNhQlMqLkz1lDzp2kbPoaMC34%2Bja05GK28uZivUMBFvGiu89cJAuuKu0XYss0PHUvmzX%2F5u2oCGHmMueSHS89Aqek9dFyRnhZr%2FuSmqCEEhkhVYOlWrYVI9opy6IKLcLGRpOj6OMnitbEOW1F%2F8dNkNvjLA9BwQA%2FSw3lMCmpSrhH39iNxLotcml2lOSKMOQaCBjftcaaG3qooh5s%2FfDaM3n0JF2dgjWV2vLJ%2F21uA9Il6Ol83Zy2deCDEpyYMYbR%2FyU4r%2FSguvuDVyyWLfGgUbACD8ajPYiyo5BXKJzVwI1AaCBaS6bqRxGiUG%2BDiRi7njGTc72GHLHw3KHpqxuq50IHizGBR8UF%2FK6YlboHbpXI35VYT8qjtsRW2frutjz3EszoTuBD3%2BUiF7XT2eWG54y1EbXAZu7djUO08qTTvzbVcE%2BTriaxT6IzvQ7CDdofjL7ch0DDSqYdNbBjZh%2BCZSISmGQC0Vv96paEqUoYlOTp1%2Bku5WOe87f6V37Dcox9TeOv3D5N8iyFKM%2FxPoRUQhSeriouFb2pbat3%2BiGS2%2B%2B8gvMKn8ob8GOqUBCtXlUztZK6SJeyMVFbZ2Z1xGvx6oMgYKO%2FaUyQEs%2BoGyA2G3y0R0NGg3ECq%2F1ZNLHki%2FAY2Zd3XWnFKrlvcpJUfJAF4SmwFH1IGQyMEnskmmGQqxYr3tA6JabFTJipn%2Fv2uItUoVY26dSuydtt4sGwG6TzahL61hrWm4VHY%2B6%2BMTBwFSUYKSgkti1pvrS6nWybMGleQk7JBW07uSeAL8y%2FvNZVyo&X-Amz-Signature=f256d999c846146606a430f3ea7e5b2bbcd8bddec6e6b15fb6db1eb42ea724c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SFWH4Q6%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIHKSVYVDhRWusbSuCo6a96o%2F3GS1NODsAKW%2BiY3G5S8hAiEAvLetS8Lzt0W3ZAjtuHmOXZ0WwJm8t%2FZ393WxW2IVH08qiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIcOohUXx02hQwxNsCrcA%2B1KA46Jt4ey1j77vXv1AyFRFjb8SA9nDUxxN3ngOCV4b32X%2B0iHSShX33p08eb5u7zneKFBJIiw6%2BNhQlMqLkz1lDzp2kbPoaMC34%2Bja05GK28uZivUMBFvGiu89cJAuuKu0XYss0PHUvmzX%2F5u2oCGHmMueSHS89Aqek9dFyRnhZr%2FuSmqCEEhkhVYOlWrYVI9opy6IKLcLGRpOj6OMnitbEOW1F%2F8dNkNvjLA9BwQA%2FSw3lMCmpSrhH39iNxLotcml2lOSKMOQaCBjftcaaG3qooh5s%2FfDaM3n0JF2dgjWV2vLJ%2F21uA9Il6Ol83Zy2deCDEpyYMYbR%2FyU4r%2FSguvuDVyyWLfGgUbACD8ajPYiyo5BXKJzVwI1AaCBaS6bqRxGiUG%2BDiRi7njGTc72GHLHw3KHpqxuq50IHizGBR8UF%2FK6YlboHbpXI35VYT8qjtsRW2frutjz3EszoTuBD3%2BUiF7XT2eWG54y1EbXAZu7djUO08qTTvzbVcE%2BTriaxT6IzvQ7CDdofjL7ch0DDSqYdNbBjZh%2BCZSISmGQC0Vv96paEqUoYlOTp1%2Bku5WOe87f6V37Dcox9TeOv3D5N8iyFKM%2FxPoRUQhSeriouFb2pbat3%2BiGS2%2B%2B8gvMKn8ob8GOqUBCtXlUztZK6SJeyMVFbZ2Z1xGvx6oMgYKO%2FaUyQEs%2BoGyA2G3y0R0NGg3ECq%2F1ZNLHki%2FAY2Zd3XWnFKrlvcpJUfJAF4SmwFH1IGQyMEnskmmGQqxYr3tA6JabFTJipn%2Fv2uItUoVY26dSuydtt4sGwG6TzahL61hrWm4VHY%2B6%2BMTBwFSUYKSgkti1pvrS6nWybMGleQk7JBW07uSeAL8y%2FvNZVyo&X-Amz-Signature=cce924ac596cb91e7d3f4c0cf0b61c1499aa5a5044aca289e48e0e9d2144e6ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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