

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIGL36ZY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDven4BNlzrlUxBmS8pJy5D4ZCM3vNPqknUhbb5%2B5%2FxKAiEA8t1bkxXGRsotCwDAI%2FxsSuVK8qB0tX8F1GLYQW6CB3IqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAj6aBFPQ0gAAKNWLyrcA8rN%2FFnE7LPIlKRpyN68MKqzgyT4HXSbZTeYjYWwgdD5tIC44Pj1sgjD3%2FGNobalN2Jw2W5VATEldCjIkeqF8MSWX%2FkhGKhQLPDIqbAk8UT6wi7Cwsmi4sKIPUq2A%2F0WpmS7xHjjnHOKlRWp5SSZ2plhVn5VVzVlmkURvtegMrAu%2FrbYnulLzpx5TL9ZTNxbmL6txC%2BM5B7UX9HSWCSxWl1wipGi99HCqpccOndT03ITXee1YkPqTP5BweK5UNQQHeiUkTlbf9Q74BPlAmE4rZ3iG6WinOdbqApek%2BUwNbs06N1xm8iUo4bubzmaw2%2BEZSXtqc6eMiN%2B0EHLKhDn7O%2FqZeX%2F7a0Tc9BgK35QDrXOexqQF3b59gOlSy9ThiNReHPVfkDXf%2FuN4SVRaS0tI3rq8sFaV8nP5Pp6UHnuU5sa8QVNS0czxg48395G5Imxy1jVBOa6IR%2Bp%2FoR8OTGSQUEBpazoCV2NgQDEO%2FA5hMdS7SeGX7Ll6ARnFinlHkdlUq74rAa6AqRxD0Le9UkIYIBATaNuaB%2BwXhOnY9Oaj4sL%2BNkaDk4Lt%2BNOSk8%2FL%2FKq2c2bzS3u1L4llZ%2BM1FM9phme4FoXof7SXPVRQnNdgCfMdoG0xWy%2BDep5bPbiMNWL7bwGOqUBGE3ynjF87muND%2FDpRs2bvyaYj49dv4%2FddVYdWvQg8R9c1inOGRLPg42hlDl2CGyiYIwJLOIt2QXr4AAFRpSbg4rPasf37zJeeGSGI6GtERK3OrGqGJtGqe16iqLgbil7ziXTuJFzURqAvP8Re7luJgswd1IjtKJo2eglOqZOlm%2BT6wNGgZMzwTNQg%2FywHhJNzYBOnJMRR9nbKQQuqcLtGmgHqC1e&X-Amz-Signature=123efa1b8afffc59af941b62fccccdc5fedcb205a6058b8ed7f7448bdbdfa9b3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MMA3XMJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUoNyPDG03AdNZFifOlq%2Fy%2FO%2BiyR21utcdwRGxS6umPwIgFL9plBk2m%2FDKkwZosWS4aBldpRATBDQp1h0%2FaTiwA5cqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLROShpQuDmSpJBJtyrcA4gt70QDxVvyXn60zbsmtcGvRl583C1cCX90cgtARSBI3FEVY4j%2F1Uwf40YB0fZ9MgOMsSJuoq6ASRGYSHEIYtgNCLIFSFmk78tyDHzPJsUoYn%2Fjz%2FSTiEa3rRm8XDrkvD%2BnkHcLveUuLB7C%2Fwc63UTDontx%2BwzTLOu5qigUTla%2BtbN4zR4AGWdM3byCypBH91N6Pis7gjIvG4r8rLpAHibNyPz3ARY%2F7p7YMcGvYbeY7xptbsgKlJApdoigUhWGxA00c0vhiggRiSAhOduKpcxs5ZedffJkKIyrep33nGBHyhTmhaue1DY3IEyd4AurT8E1m3tXka7trYoRUIs7bbCiAYLFLNbX3dX8VScQeh3qA0NWFcDlWKrycdLFNQOJo2B4yQ13X%2BSO8CdZZNWZcOeq7QfyNcC4AwK3afEdLt1bVfV2BzDvZJLsg8HQNwL5nF7MTfbolNFpzRtYzR42CUrJ4VvAQVi3EgV0%2BKn5rv%2BJ5E8Bo2dQtrL5jlAGiXPvnjNqUkHzfDuHvxTUxk5DY%2FDocRsoHtEyAyfL1bgF9H%2B4O0Cw6hFg9MMTBJ8lRuuhgu4Jc%2B4X467bYKTmcQ9hi%2F%2BiZFWVTEz3wWIeRknrZIRlpoxcg%2FHkSPhxHV6JMLWK7bwGOqUBOR1vueMOWnx6GysPUoezSoigeqGe%2B96W7IYsxeJ2KDf26JvX%2FfTOQjVXp0D8jvw0QAic0oirjcQURb1rcrVWMcICfDHVQAc6o5YjWNMHA%2BEQTLznuyWELX8uaxNkkz2hmvMkSpLJXqmoUdUwR6uZJcL74ov%2F3yP0HC13YL3gt18Bk8f%2FvV%2BKIUVkkq57bVr1JP2QBJXXvM0%2BE1Rd%2BaRbfgyj7%2B96&X-Amz-Signature=c25d7666d3776f65e7367749d86df52ef7ca36183920ac0b9974366b98286400&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCADIESU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdRPxV9bkens337J%2F3scp0icchrysZ8b8rhppons1W1gIhAKjwERNq7M5wtmWhHO0nyCdCpm45%2F0flo27Sq85NbPyYKogECKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7PbtBzzu4%2Bv0%2FL2Uq3ANUXiBXIyLdFdL3yScg0P5H03IQw5LQRB5W49U%2B7aqtYBYCdv9i9kEXizoLiiUOTI6QD5UWc0CEsWOHt%2BXpeTcOjnOsSf97%2Bdprsluug%2BJsjrrEvVCF%2Ftgepbf17gQ0iI37gTlcq7SHorhbjO9bLb47DV3eOoy8zopr4olA71iZjweFHSup0vOfbNOQJslG0JOQue43KDeYsfQuJFKqMAVZrmy8I8mIn970fCW037PkpVk%2FlPNFALxEIX0WcM8reLEVlym9nLODHTSt8GmX0lgTrxs%2FP%2FBAubgAbJ%2FSb0%2FdkUv%2Bu3ggMTInSH7z%2FhjPGBsoGVvxm8Usz%2FxaG35QojAyYrfFfbVDJCcFpy4DQ%2FLZu4jXBqpA8R4ftCzCr0fBnrxBcCkWSDXtLlBwRI4NGChFlQWa0N14BdOZTBy2qTbrAUR4jg1uUcnd8SXXyrKBoNOWwA7Na%2FxRTO3u6ZhnvPQL5RM16%2BEYDHjmgdBSPlmNyHWP9UcLkf5JInXJLViY7%2Bad9p7HS8jlFNoO%2FI6mI44V%2BpecjxmJRWIaONuDMpom15HdaxiAvTnX3RPhluPLkMGtuuAxXTnkFUN6z6DYjd3zcPUqDwIncvD00Y%2FO3BRkPuerIQB1mwS%2FGa7vXTCHi%2B28BjqkAdhRRWyMxKMBNLydEG2Imbzb4%2FSIv2vTWeYzkrvp0diAKH%2F2RBFM3pjzK2OpS748521gt5stDpT5O%2BmKlK7GguSEnKy%2Bfh2LlsiFVgIeAYwAQmUOVSx9PmNOjI0lUGPwtd1XgFV6lOO8UfFXAWcZz2IOpGhbWT80iZwSzUC5IdNaEBwERD4xD4P91d6FxLzkSNHHMrAiRKSLC0wu%2B4Ul5l4xsBJl&X-Amz-Signature=39e225c4f6960d128058f23b8fff823e6e729b9560d1907bdb21426e186c9526&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WG4CUY2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGA3IEq5VTf%2ByVQ84X9IwuWwQBvnZLKjhyC1kcItr5XJAiAKqKdKL6oZ2ziqJFhJ1joG77kkqs7FXgYtIPvQNtn5KCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBd0cwTaX4aw75%2BYRKtwDnvmEwZbiYWgjBuGwjYfK2MP7JNJK4HN6aRGdtQ78e6koZBaPNG0%2Bd8Ymbr5QFevZ9vGQwbsp72rbIoDO2PMfHtmCOaPR9yA6QK7XSS2HF71n1sz5K3HG%2FMVINy6eUq2Z8vUF18EnmozPC92KmmXVvmaEmtQfTnvaiFN7joI7K6zfNqzWIe62yWSbpGX8S9TRO%2FNcOMr5K77fV%2FSx9729WHYxgYwMDB%2F9C5Okk5eNU8DPxPBbUOuFrmG1qlSgs3nhEZgXne%2B8SDTtD7lB19k3hFwsXxxY2IMV9SkdBINTKppuGpFjga3oY6CI5LdPxu8vlfPCmSbh%2BWQjggKK9MOm%2B4Qc5Jnb%2Bsamp5hOHrv2JYxSbQHcvBtc3Arnua8mZJAhyWQxyUlGZn%2Fq8yUDwi2bw2f9B8Y1IBVa2CNww2zbulTIKRCg9CypS12nORfo9V35Hnu98sF0xQpLpYMHTb6V%2FRQZVvVxVGnpT%2BB7PIa2D6ddfAWSeBrvUaFBjH2pWgIwdkru57PyEuOzrQa2tsvY49mdzZidhL8PO1mkmoSKoDGqKFtHdUwHmgoc57dkc0Of%2BZ4%2B8H6AEoGOnZMU%2BYy9WMzRHMjoA7n%2FEDd8EWKBb7AkN7uY0uBQm3r%2BVz4wgYvtvAY6pgGjCAnk4hB58Tajvhvrso37HsPBiGq6rB2Miaafm87lkGw%2B5jbCtTYKq99Zd4cRylliy7mJiI%2FBlt%2BiUu%2F0U4sMGMIAheYI8Mq3aYWM2aVNvRfc%2B0Qh%2F91DvCM6hqOZUofBHyNAeIUppgE0jVyOttak5yL7rRjkoLc7VmE8VW6LJbOK2p7eqR3IblefQDCylbDZPMGpb79ZwWSsIoJ%2BTBLSlGD3sLJ9&X-Amz-Signature=ff215b3c7b407f1c2724326aa0e54ffe35955f01c6ac96827e1db81f6e035212&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SLT5HBB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGOrLZ3USCKU%2Fb0PHLDTNvWYEvnJfbrjb0ZYmZECGqPOAiAq%2B%2BYpehMk0YWR7jN9WZQt2ndDHMMRQMGkqm7EqkkIQCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlbRmkwqhW9EzW57sKtwD%2B5FK%2FBE2hXDwXO9XG7HTlSs%2B6MWRm5tkFDls9DHSgM6F9ECubTwZQUrqs80MYqRvqmSBpb0O0ZakbxOR%2BnSk0ceox34ONB0lLQOV9tW81nH%2Fnvgzk0Fe2GxO0UX0IYhaa0hJeVH%2B3zvNwJypsSoGCY2qATBWshu2bb9E%2FRde7%2BPO326gAsvfiklArMrLLCtz9OlxHNMpc47lisbnXgHDsM5EF48qzZaSBnrSMv2l0H7nj2F6JbDGL8JqLI2L9r%2F00rviozc3jA%2FHlat0h38N%2BJHMhGteA3xpaz3VI6NiDACMwjK%2BtrehRHqqfvzeiHbr9fX5O%2Br4nIWR60Cj2q8FlNxIvMqv%2B3OMgp6El1oaPQAvNAz90rX1sP3vY%2BIiOuYaFjcw1CkVEextqYX9EEwNdW7eommwQu4vTUqJSFhZhzKkhTPwlbwtRXh5A%2B68UCYGDhs1AYTl%2BPB94DK2eVRFI5fo3THpUDysx8h5jbQdfbnkgOWiAGg5bAlNj1ZYv8bn5vOnxPmT0Di05UxcI7pkRzADLECrhRZenjH9Xog8Nof1SDxzKjbuJk4OU%2FWVTGlLGbFKAHQ%2B7wh263u8mAyBwTO6VgB%2FpIxI%2Fs42zemLO0DDQNlDatft9A0ih2Mw4IrtvAY6pgGAdAbTmE9xXzej8YFFIsawWAGeK%2BYiDRW1Hw%2Fch40XOQb3mJd%2BsYUb%2FHPW%2FKaUBMAsuOBWLc4HJZfLHWKIzNGG9ZsucRfkRP8yMzTb1eqj2S9hrPJgCtYL6X4zsP%2BgMtThgqkgfHg3doldzB%2Fvp7VP6if05MI97xinBIv7RgtkIDKrjpphhlMQ5Xd3%2BieMO3%2BecurpagczC5KiU2bb1W1ti7uBKC76&X-Amz-Signature=2c3cd9c67ff350da315aac854a06efba2a8dcd59a5247975169060fe9e43bc3a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK4XKO3W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCX%2B3903fJKM9K6V0hC8EyGECzIZ%2BZGfJJUqVjDHSVZewIgTB1QsQKxKICVFJe%2BtYTc%2BGlOAr978dbm0qhAUdzXFfkqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN0IIDYFXgCuACg6iircA6bQgupA7coBbUAWFri2cIkHaVNHxHQ8Tj4ZNxBkqv5t4XKozfscnm70zI24e8sLlzKDDUuH9i33JDiUFz3MCcKtEExaXCnSgeJw%2FAf3t2AzP4np%2FbARfFlyyyNlkWQOD%2FjOjL6%2Bk%2Bjk4d1etn4bgd6L6qdBBUWRoqvHagLojdzTC8iG96SFlPL%2Bexwz50EDuAV6DLYxa3v476bdtFROe0TXY9ouXlbikZkbCX4Mv9qfta%2B0dXgvVOyJuR9QOx3XIMPR6pWWzqoxGjwUbHscAjP%2FUOsABTGbhIFzOHL2PbR5Cr13o%2Fic3EFoAIaXqJd4sxYJxbOFy3ZsKLytuLifuAujVzriRPFvjZntQVSjkf2inSRNZfKPcvPuaZ3g50ysYGGyuBKojIrjwcNEq85jcCaKGCXezRaHfhK%2BBVa4pMaGL7q0Ft6fcNyc2PYdWeaPWAgr5THT0R1Kibd1aF1ALuI8LN9nODMBmWHfzpmiXl1KaYIr8LGscvnRSGLshiEdLYeq0IyZ7%2BbREspdJdvKYq%2FuEVtlfIE5OD%2FcEAj61hXg%2FB70%2Bfxe4I4YCtBmZHKB4m2HawlZCK5DFn5kMUl1gsIIJT3lFyml9hGHQG3lK2r1zGIp4o60lrSQh5ojMK2K7bwGOqUB7xwRzYPQg2wuF2uRETbd3UD2AeaSAxezGVavtMk2rS%2BmENG5JxyuAA4YzFjmbdlvU0ekvtrgNRcLtZPRyD17O16SXcHHJliKEP7BhNxGRbNfycd0zVW7j8kjkErwoQ8%2ByB%2FU9wMvFEfqpVCVQdl36J81mNbG4Ofw%2F9ocG3LHT1o2EvZCE6tdt0OiiB5uTa46qP1ZcXZrwEP%2Fg3jzdqM9GGSPxwnw&X-Amz-Signature=52f985d05b32b89f1ee83810a1670a7b3699c43cdbd2f2a0b849fd2db1670841&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLOS6EMQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHYPcFdqjjOVmHNsnHo7aIPItkExHGUdg8WiH8norH4gAiAezbaJVLWbUGermQmXcd3YXDKEIlEBhQ3yyODiEkZ9kyqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo8oY%2B33lIls%2B509WKtwD5%2Bl8XfiA102xodaon1yNI3asiujg0AQrzJCSXAD%2FUCDTYUuG%2FcIwdpmujC%2FktkD2DT5TZ3AFa3wuI01gFq2vCf79Jg8nEQ8acl%2FP8TlFgiUjp%2BPGIN4qhIlbP%2Fa8o86GKpC29n5dkGkvClNkBxOTupMHnHR4gVQnZwNTI9za%2FXl8TsH84dWVOGH9NE5s7ikpX2ONPPYcPIOGwMJtYLptBsaltCfXOZ1oSGSDHTnDePqIMW1N8IS5xFAJib0qAtPzb3%2BR38EEMnFWUim8%2FzjiOFQvXIZRe4JRRUPiAmb%2BeqKM1r9s%2BOcdXUqYcS4rK0zW27uKOQwNVfzYKS4DqND8HT%2BXfHgv6%2B9TzNdaBZLbbMXekl6ETjzQ9zLFIigN4GAgfAx3naNPVqJisd8QDJQHezUFLBSnhQxYvFuPIzcWk7IlBng2UKLdsOx04bvgYomZQrg%2B0yLOKJOuRZInMRy0yPcXmt%2FCJ8n89MNtfjteHIf3lIk4%2FJg%2BDj0AcTPjSTXh%2BPTcFxxSXaMrm46gYoc8AeRthG8%2F065R809v6Z70tRowYg3xLddwFyh1jBewSdh0J51wAS2KSRZN8jBjjmCs%2Fu6Q6mENJGImPZtuEcfIq76DoptwLt0cntcpeD0wwYrtvAY6pgEnV%2FP0S%2BDaz7gZXAmJwPdKPYZb6nC8d%2F7q6HUEVftAk%2FQVZSM0cSDvUap5HJ5UMhgCl4a1peRQUn5AjPLo340N1H8KHppBszVuKmIeDz2kqNPzC6Lk1MuhHihY7PTBG8Px6Dmf%2FgurXLhhv6pob5JtccNJ4edbehur%2FeBkKTicxHAfdBlOO2NtWSkhU3U2z%2FakZeFmSNCgYpRz8cLxfWAxwSPMJ%2FQL&X-Amz-Signature=d89c19e0f7702f241de662e9fe1961f482a0e481f5e4d3bf0964a046093db363&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6TKMPMG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIApIpBjXkX36jvuWBa5GCHGpR0VixZJfOATrVEKjZCYPAiEAn6jgOJRS8yz26T6E5LrtmIfKODBc7GtbrfJlJiZ%2Fqt8qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOhnG%2BQV6VaRBz1RwyrcA%2FBtDK%2FA7v8aDWc0OapfwmcWQHd1hTatOZMvozUbRTF1AhvpdtEhly6qkMrEnCt9SneYUOHqfPfB%2BuyJOuUdTH6tQvKZ2Dtn6XOzK6zs90Kean3Dk3wi737TaTMJBKRtF1Fhib8g2feEdtHUYMDpoM5EWyHoSeg3Rm833pkRmejR%2F9FzqS5Qu8GFnw2c8JGmSnDmW6AWfSTtZaa9EAEyxAE638GrOK56Vp%2Blj9EVmW%2BS9PfgBbo2v7SmWIE8w9GSMd9uaGQo7VsHo81S07MnXI6cBwlN5a%2B5lu3WInIkaEhDDUV%2FzTsmXoKPxwUPGKo00XylgZmz%2BpK0f%2Fh03872yDInsERFgeMDshiR36eJYwy52Bqp1w0CDRGq0RDRJDkRJYTOk6Ez2OK5aBYn%2B89naObUB8oXRTiEbfTlqUgMOxXkucmnmGdo%2FKlN8GxI%2BdL9ADwBiIvpa79aPRzNKkijh%2FCWYkDoMMC%2FZY60K1WHZhr8n935an6MklcfLx9JZsdWqRkyQIZRlxv87Ak%2Fyx%2BRil0gj1ThOHXRWWA3hdqqskOrT%2BdxtZMQEAXRkuwDQrod6zciTpkhdqxCmR%2FE6FFsGHhtAbkXwddW6%2FY%2B8Fe5PFZwnGizuX8nnm3kE%2BoGMOSK7bwGOqUBS2A%2Fe4cyI2ZtEkLbIsTZBorWDiV0JtRUoSEmbKLh9MH6aCxKexM8qN9G7CwROaYF4YC%2BjI6SfCXZV3VfRtXfzVB5Ehq5ZD5W9cMOEGeQtOwGecHSDo2GnBzpDnnCmujQMJ3WisiJT3Lu8%2BeNxKSXygX3lVtyNa4ztWLWk4kXIZQgpiXKbH12lAkQhVGHwUQLaRHs3KPvkwWfaIWizSDNxV6yvsBA&X-Amz-Signature=827f0b539266709dde850bcbe04126cfd8036264934eebbd11fac15263b10345&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SLT5HBB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGOrLZ3USCKU%2Fb0PHLDTNvWYEvnJfbrjb0ZYmZECGqPOAiAq%2B%2BYpehMk0YWR7jN9WZQt2ndDHMMRQMGkqm7EqkkIQCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlbRmkwqhW9EzW57sKtwD%2B5FK%2FBE2hXDwXO9XG7HTlSs%2B6MWRm5tkFDls9DHSgM6F9ECubTwZQUrqs80MYqRvqmSBpb0O0ZakbxOR%2BnSk0ceox34ONB0lLQOV9tW81nH%2Fnvgzk0Fe2GxO0UX0IYhaa0hJeVH%2B3zvNwJypsSoGCY2qATBWshu2bb9E%2FRde7%2BPO326gAsvfiklArMrLLCtz9OlxHNMpc47lisbnXgHDsM5EF48qzZaSBnrSMv2l0H7nj2F6JbDGL8JqLI2L9r%2F00rviozc3jA%2FHlat0h38N%2BJHMhGteA3xpaz3VI6NiDACMwjK%2BtrehRHqqfvzeiHbr9fX5O%2Br4nIWR60Cj2q8FlNxIvMqv%2B3OMgp6El1oaPQAvNAz90rX1sP3vY%2BIiOuYaFjcw1CkVEextqYX9EEwNdW7eommwQu4vTUqJSFhZhzKkhTPwlbwtRXh5A%2B68UCYGDhs1AYTl%2BPB94DK2eVRFI5fo3THpUDysx8h5jbQdfbnkgOWiAGg5bAlNj1ZYv8bn5vOnxPmT0Di05UxcI7pkRzADLECrhRZenjH9Xog8Nof1SDxzKjbuJk4OU%2FWVTGlLGbFKAHQ%2B7wh263u8mAyBwTO6VgB%2FpIxI%2Fs42zemLO0DDQNlDatft9A0ih2Mw4IrtvAY6pgGAdAbTmE9xXzej8YFFIsawWAGeK%2BYiDRW1Hw%2Fch40XOQb3mJd%2BsYUb%2FHPW%2FKaUBMAsuOBWLc4HJZfLHWKIzNGG9ZsucRfkRP8yMzTb1eqj2S9hrPJgCtYL6X4zsP%2BgMtThgqkgfHg3doldzB%2Fvp7VP6if05MI97xinBIv7RgtkIDKrjpphhlMQ5Xd3%2BieMO3%2BecurpagczC5KiU2bb1W1ti7uBKC76&X-Amz-Signature=28b1083940fac885714947e9979ebfca521e7d164848d83bf55b85e7decb2947&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LFVT4DW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC4BylMcPoyhpp0VjeBMKCpu1SUIy8N7HUHiUIBA0uraAiEA2Z3E%2BToKXFhwkJDiS4692JMY2gZKcWR4GxUPuNwRyz4qiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2B3wVuYGDIaenvQFSrcA5VytJP4T5d4Ru%2Fo4WYnmWMfS5FqB3GMnmJHnJwCVjhnE3KdDZnCgLK%2Fq7MO29LMvpJJcYTS1p5K3a%2BUmP8ShYtq95iCNdL2LkfvaYTEyiKe75sqmnrYoK8BC6LpyLXhm0mqhgJfZilOVA2GJ%2BdVjpVgJKZYFpgR%2BMALKKZ74r0WyUOVsRglRAC1yTp2RfDe7svAFv%2BZYiakOZkfjIpgo2SDlRaLFPDlZ%2Bl%2BbxrpFdfn0%2BWEOEQyYlCU%2BLTJt0uYUSmKdvUwuj%2BZhjUqPTXDKJAYPzsYLAe3rJIly7%2BnZkmuAkeJCDifsgkvisyg9oZNRfWbpM4xSoZjREKS7a06sPjwSjLPteCkMCqtlLALkyLzGnvJCiB9EXGCcSBTUM1ZoPdZ6lzwb4jqlD6E9xBZfuvU2dWIx8i%2B6geYb%2FBLT2TX%2F24%2BUNxuUKTzG9zuwhWL7Luo%2FKGKGE%2BkAL9eLlP9bW%2BBEZ3%2FOEFW%2FwqnquiAdvyxk5%2FFHUVeYQaxKBTF9WXPhE17tWR6WobbTC7%2F%2BJdziD%2Fag6hb2xga%2Fi8XPQpCFj0v9kLQhYpoQAQvWg8YEJJYOgcSSdN8bIFk00oH%2F5fEysq02MDBKxTMop%2BTfUeqbCC4DUBYwtGB4PQ2JgMUMK%2BK7bwGOqUBUpatXYkNft18xtS0%2FvQbDNnmSMYBnqTDp98wzLmVwu04A1iRTZFm4rYBa%2BOE4Z9CjQecw6bPsK9SeQz%2FaOCCD6MySNdmRBdSt4EhzXpuWuL%2BYdGHq3hG%2BAlyhaBvNvvXAd%2FBNY6qjl%2Bxd2w%2Bhd9kc0PEddBLx8XM%2BoRaeqcg3G7BwMaWD5HLv1eTBb5px35yVPMFNZUTRhpfqWL305w1esaaSLLL&X-Amz-Signature=49213211de2f131e5705016019e18f5f47b107f9ca624f54254df82f25245a9b&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LFVT4DW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC4BylMcPoyhpp0VjeBMKCpu1SUIy8N7HUHiUIBA0uraAiEA2Z3E%2BToKXFhwkJDiS4692JMY2gZKcWR4GxUPuNwRyz4qiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2B3wVuYGDIaenvQFSrcA5VytJP4T5d4Ru%2Fo4WYnmWMfS5FqB3GMnmJHnJwCVjhnE3KdDZnCgLK%2Fq7MO29LMvpJJcYTS1p5K3a%2BUmP8ShYtq95iCNdL2LkfvaYTEyiKe75sqmnrYoK8BC6LpyLXhm0mqhgJfZilOVA2GJ%2BdVjpVgJKZYFpgR%2BMALKKZ74r0WyUOVsRglRAC1yTp2RfDe7svAFv%2BZYiakOZkfjIpgo2SDlRaLFPDlZ%2Bl%2BbxrpFdfn0%2BWEOEQyYlCU%2BLTJt0uYUSmKdvUwuj%2BZhjUqPTXDKJAYPzsYLAe3rJIly7%2BnZkmuAkeJCDifsgkvisyg9oZNRfWbpM4xSoZjREKS7a06sPjwSjLPteCkMCqtlLALkyLzGnvJCiB9EXGCcSBTUM1ZoPdZ6lzwb4jqlD6E9xBZfuvU2dWIx8i%2B6geYb%2FBLT2TX%2F24%2BUNxuUKTzG9zuwhWL7Luo%2FKGKGE%2BkAL9eLlP9bW%2BBEZ3%2FOEFW%2FwqnquiAdvyxk5%2FFHUVeYQaxKBTF9WXPhE17tWR6WobbTC7%2F%2BJdziD%2Fag6hb2xga%2Fi8XPQpCFj0v9kLQhYpoQAQvWg8YEJJYOgcSSdN8bIFk00oH%2F5fEysq02MDBKxTMop%2BTfUeqbCC4DUBYwtGB4PQ2JgMUMK%2BK7bwGOqUBUpatXYkNft18xtS0%2FvQbDNnmSMYBnqTDp98wzLmVwu04A1iRTZFm4rYBa%2BOE4Z9CjQecw6bPsK9SeQz%2FaOCCD6MySNdmRBdSt4EhzXpuWuL%2BYdGHq3hG%2BAlyhaBvNvvXAd%2FBNY6qjl%2Bxd2w%2Bhd9kc0PEddBLx8XM%2BoRaeqcg3G7BwMaWD5HLv1eTBb5px35yVPMFNZUTRhpfqWL305w1esaaSLLL&X-Amz-Signature=a76a202d198b2eb3fce2289c694515502986e4cfb4fc6b98b75592b0e4125411&X-Amz-SignedHeaders=host&x-id=GetObject)
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