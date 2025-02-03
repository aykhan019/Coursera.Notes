

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664X5S5UE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDxaW%2FNYXd7FD8iS9AiViz3ewBluiRBKBtW%2BQEiB2hqwAiEAmp9f0sO7Uq5JMD2Optz3TEnJLYcw51QBEgywrNGbyoEqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2F0vRb2dufKYCCJrCrcA1m9aJqb%2FoCNhqKqnvEdMTP%2FnqG%2BRC6apOfKVc8%2BhtrdUmPlT%2BWzXXOCaRZjYrqTCYIdyWEEa9XXKWfwhh%2FPy46blLETQyzj3lW8%2FMJZ72kVpxBmlf3AFa1CJZc11POETyTHISq7%2B31hBSSyY3sIR0Onw3OfStx4N6v76m9gX0HgarOrg8tuVdv6zSu0kyl9xdevX%2BmViCWOLJSHNk%2FSsJ75vqu7tDRxhF21kXxo1T%2FdgpyFbdo9qbdQ2FdI9gqxqm2EFBTHEjwDSLfkGFzlOZ%2BH7gOL6rH9RtOVCYXGn54MYZj0JvE82MJ0C9cb5aZHJkWKJdrS1k7Yw3qePU7pDvAvwvTHlMJtvVPtMlsgbpYktOPfgws3gO2IfXYzrGIJiGQpPsjtlSRz2pOsBeJO9HDfFV3ABB2nOg0DRzOTXmmne7ozQX78rANpJF5xBy8%2FA0cjI87XJHQ7XfSClnNj0sCjXK2LmqEufxwjEPxVPhAULLKSd2JmXrg66084aE%2Fj7qJLxCZ6NdUMpoesdRnaqj4Kv%2F2prlVQl9ZRcMGgBelH%2FCDXONWP3NZt7TEiKWQ%2FIqHuPGYQi4nqA%2FsAQQWc1P7HZBAvaEFMHMv8AHX88nkUtKQ2YY8TSMb2Nxw7MMTk%2F7wGOqUBK9gXYZ1H0mny%2FUGXUeMaWO9hb7wbVOho%2BdnLDjgT%2FvPQkgtQjNfTTnQKrl4j2nIKgDIqtBwsGcPA95oUj7YxkDix1y8e9xLAsDucyM%2Fj04cz4fJ10LM24OF7vU9uk7aLV3qBqL%2B81q%2FoagMXO70aN%2FbQ90B2tqIyYe%2Ba4pMZXD7amv3zcW9aQhBC%2B78MuBDUvewx3KLkgESN7%2FWh85DFBimTJ%2B2l&X-Amz-Signature=5537ef822d198597e5b17699a87dc51b3e04d77976d7657ed595bff88f1e0b9f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667L7B43W2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtd9NAr78D%2FyeU2CybdVD0R7sy2gDznWnaV7rlVUgmyQIge8IRJZk5%2FPYULvHYeJSkHvI25rJjE0i1VJ9hlRL4AQgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNUw%2Bhmdp3nytu3OBircA8%2FplRxbcmuVsDwBq%2Fczfz4czwifMH9Y%2F9yLezadn0%2BYn5EZbQhTyD3FxkpQY0N9meZCc6BlZTSy512IGUe0DPg9jidc%2F%2Bmg8e47W1UTRqLsNsQO9C7WVhrupzSB%2BfUQcdSdX4qaaKljUlVnSfdTTlvRuxSRiMhyFIM8m%2Bzb8JaRBM%2BPRsqPWQHOdyyoyQTW1j9ZK6auaxijqMTzs7heaIVIKDVoTo6hAlt76UhhFs%2BJ9BLYqKUxxlTHF2Zjx%2FaNPZCDDPe8eIh4w6ABeYuzKe0Vy6xVralwdJe5cMzyLeVSP3cB%2FqFSWXe7euLS4SO%2BoG7CrMOJFpHR29HshX%2Fz4UB%2FtmSUn5559p3L5lQtrH15dhSbwpSNbwOqZ8u9IAIZjy4%2BWPkBVzEsEZ8%2Fgft2QJlTpIWZmVrtvl6edG0OSSH%2FWN2Fso2L2pszo6MbtoKf28fgYPFhY0XSKGnysxv3aot5nTroIYVhGNrtpuicXh8jr%2FB%2Bw6kN6jkodxvvFtCh3QAFfetZGMwMdsILDNFB1sg2fBjUqWy%2FEw5oyMqbMruG%2B5tjSf%2FHVCVVWDi2MBWKjFrlUTgFk04xEXtlORU228auYY3hb8Um6SB7XPvot%2BH18MLQ2%2FkMFCrlP7KAMMDl%2F7wGOqUBYahhLxOjQAjF1jskUiao%2BDVQBq8fagKIqQPozGLik54Ai4fuBSXrf3twjbfz1xcTNHQlFv6lv%2FgsGwUoRH4tqGtFGhHRLw6%2BvLXnkeILfCXr0Qj7hlw%2BQL0j47OeoBi95cAcx5xQfadoanQBuLmtnua%2FU9%2BA2jY%2BOWV7t0mZB2AdqYajNjVFowyrpfLlkks6KlphBKTRptOwXIzMCQQUnbXrmxCE&X-Amz-Signature=46702901e7144d3227a217e6c0d2ac952196975c6ff11ec84943a2980bdc0946&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHYV3VLQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDdmbpXJ58sfhObzag1K9XBy3P7WUeMWnzMsx56zCQDfAiEAzwx7OnQ7q3%2FR59gRkEs9oU2qT1A1GS7irHPTKM4x%2B4kqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCinBDOWn%2F3XMp5b4SrcA6PZJOnntKwKOKaB7PA4tc2hbA2NxHgvfw%2BDEu4o%2FJajZex9PKFYwNCJDu99oBLuiTlf%2BmKVnmQcgZr2rlurldt13uIfoj53jx5ETjmiRBLEZ8DJ9586YRaEgQx2P4uy6FgZjbJ1ef05QCJsMLr%2FodPAUWTD9J4WKnj53%2F77goge4Xvv6IbmQlpts5yR55aBjUxsB8dPjX34gjMmAS%2FFHel7qNT5ejFYTX9ik0PAHdRHDot7vJysM4i%2BSlE5xNX%2B5WZ3f52XFlMIshFfxuuzrtfduCsyx0du08Mxi1id6cqmktcZDKBJK%2BEgv9KPBTZqByYcJCkD%2FEuFhsqjx4cn0HC%2F1M%2F%2B0mZUe%2Fhoifn2jd0SysYuVjpVHaDuIIs2qCjQnXBvGYz8%2BQ9xyXGaF25rTw%2BPAZay1ZDYncww6nQ7B7OAwM3J%2FQN7wzVVEF1TIye3OjjduU4ZXcKnfIT%2B8SW2Nz%2BYk5WEXUOhRUMGDRSQooQYlar0BsTtkO5GMXDx0bOM2gKU7Wt2uIb9Oia4oms12q4m6NIcsZmyp5xvVFzWgXA%2BUW0QeCanbhYvF2av%2B%2F7aUFTIjGl1sxlapGRYs8U2GkxnSMtUjUVcl%2FVCnSs%2BqwQ0fWp1ixAwuCDm5dhRMLnk%2F7wGOqUBRs9VaKmaHtFT%2BWaK0iy7aCnJwCc4J%2FPwS0p6s5o8cM0yveCcsYFlWJWb%2B9jtQQAyudN5o9dbyMSThfwrS%2B3WajiZ4danJ%2Bg%2FLPN%2FGhIXF1AuUFA5gHQaoOzpji%2F2n2CnXkegyMxz0qyuAw8C3oiwgOuDqcYurRs%2Fqyw1ElHrKFniR%2BqO7SDh49Yufpm7wSsnMqcZy5J2G%2BfrVKjrDPrh6z%2BucaXz&X-Amz-Signature=bdb6f9c456d6dbf6422d6a796390b090b1aafdeb981af301c144057ac5a8c8ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKIKTOI3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICzt8LKqU4aRqib2J1wzhufLm68C5nbJY8%2FnfQMLfXkBAiBGvggVtQsKZTM0wF5H6ZuIHH%2FCJdZh6btEmOFLMxR%2BoCqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNS7yhfnhU5TEvrfyKtwDe3hQLTR3qEk1M4lJHNJiI9z3eJlddh%2Ft2Gba%2BDG90MAnE7XwLKZfsL2%2BjEbyVGX2SYmePyjAQP4XfEzQ3pvpmADPAAfWzT0G2jR3zpUXuxxFS8jwmugrApV25ZuTKxzaIHu1rZ1X1MWbwJao6FhULvfKen%2BgLjfKveuw98Q2a4ABiq%2BHun3RUQ99kNo6x1znF%2FYioxi1XwR75k7vbMAoYefi6DiBAskVFm2WLXZVZud%2Ft4k57hh46Ze1G%2FmnmEDftQqqoAZ38RmPD3vy18TPq%2B0cazsm7QHO7PZVU7gOhMZvHEDYvnZYbJyFPZPzHUID0J1yeqtY5ZxLPZ754Kep6tBFZEEdCiquhq2RFVvMqRFaHLg3QEtKQB5mmBz0qAkPRMs1%2FEYJpU3JsAy9%2BW%2Fw9Kzd0RlfET8M4DYCvy0RM6IoOm8D5utOqfscBdUx4xqaCFn4um7HyN8vAYr%2Fpi7xOPGBloH3Uemv98Rp0k8V0CeiMqgpuIyZsaHh6hP74o5ynB30RrgkZZVVmeufHhpTK5hZi6KNpXnq8Mvcfbaihq48G1zpOfNrjDT1wC0eVVXba7sJ8UqmNtbn%2BWx0EiHq%2Fe7Do1RxOLfhgu8eRRcSZQeP%2FqHUxzPNkbGQgj4wh%2BX%2FvAY6pgEgbvHo6sUkFUOkBapE1s9bVGpuoITmLRMhXrBBDtqd2H%2BPahrSGRMiJgJpelAeMvwlkYF6q0U%2B7BX%2BTEa8T6pBvh01YlEREDuj7e0N1GNI9b5n66GQ9zGgZMS%2BUSEaQTqz8u8sv8wWdtonGEZY0M2XIcnUfyQZVkJXGgmOPQpc1A2ByWgxnKAe76MigXJ6igCf8UCxMcgLrrtWRVc2Wm8aIsbotVKk&X-Amz-Signature=27df9a3e5036ee990d9cc55c1b4e2411c3c5124f83ea568d3cf17ed35249aa31&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666M5Z5KZ5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx96dIdhIlhhq2VhbclOnas2jJzAUhT0EfDie5FX8%2FNgIhAJo3eqrElCXZAZPCAOXuS6GsWy5p%2ByAA9CYJWOxWffD4KogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZAKacbQnQ3x6KlG4q3AMKhmwl%2FgCk4N5%2Bne%2B53ng%2FygBFgXcJtj7XcnNz6zOoAeRuLNOiXieZHT8Z%2F3rRhMYb1ZCuCg7lEAnY8R6HcSzx5St27vegUGT7sHuWhzHlZuHyALPYsL%2BspY80JBPo2TyyJPOvPH%2BM5XbRU5c1onJzg1yaqFmibXKD0ZTzYOJn%2FB0zikz%2F3SwkikBMA9RpgvSNyqZN%2Fx%2FG1yzZjToICVWT89GOD8E3j%2FT7ZIkyic7jH5FcBpEclf7qBof0midxGKP81Yt03S2z2v27n7RJiiZBGSznsk4iLlj4qUWwxRtgvx%2BI4%2FZqWOA1qBiTfoEIe%2BFRbirI91qv39NbmGVHdzPZlHaLosSpSbEzffazN3Wr7mBWeW6RvGaMMh9F1FWRuSdVndUeDmn3CMkSBOlj53oOrgD4GroIDFtmIdGPbfF83iTwrPocyFV%2BrEpLrnLTJKZPs9UG4IwEhkxgG36xpYDa%2F1QsBsprFZw%2Fr4qN%2FD1ikWkiq%2FrRdSizw%2FdiSHmJAUORG5h1I5yXNq7YzesGWxPCIbwJ55MwtR%2FAip7MZUKneBPrffGFcvZgj8HyRMqrjgJgTTKL4SV3iWwFSLEP9mQv%2Bb1BB1gN18rlKsTrUA0uJjtUkTzZiDFY9I4%2BVDCt5P%2B8BjqkAcYuEHg2XXoJG4L2CEO1aHPmdkcaM%2F1ifhDfkqHlWww%2F7uuSjY7qONn3jmqZZudGpxGqJbhGaAhpuAeayZtEC38dc2ayPMNqBMWx8MaIze4Ef1wjC9ktR29UDL59wpH2%2F8z5VGQ3jlDIkfon1CR7Wh%2FuHfzj5r4lc2zO07bzG3bgf0I1XZBMvqjlLPIfV6qP15%2F5M6qjztEo2JLz61MxHfJRkK78&X-Amz-Signature=a78e99706980d9f372db36c8ac2ea7ca9ea5b74802a73a36d92967025a01debe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROIWJKG7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNyY5vmAnIgF4%2F0WLBcyxhjUedt%2FmJIIejIWmHW8PB9AIgcNe0tGCNTzgwolRCkiu9zhUrilggPzXx4YPyMAPN%2Bz0qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrP4rxIdSh%2F3vlyYSrcA%2B9zChHwpRR3PMsP3YKpRmG8PvFdgUFI7StO1HaDlUoCzm2duo%2BLRjEbR3klxTP%2FvJolYB9wM4lNUkmXY0Ejbytg%2BIZCj5glVzqmYPzBqrKmUVZPX5Ip%2FC02hxKiCbYJMYV3dSXuTlaUsA5EY88NxgKrtj2RbrB5ks4SQ4Uf56524763dM%2F0WHPaInR4F5%2BDBozMDsjUq4KhSSpmqFFBEO1Yyxq2pur5N5XohcOsSuq8AoZvRsVhtlX8btDUlWk7tqsSej%2Bf7N82euURvZfw7%2FN5R2X0TrnF4a37GPG28pNwF8X8kku8FIp1RQR%2BYkrObD0ldaRIBccTclaDBlf%2BqAWtNI5E2pCXlld17iozRPK0WK%2BwdeUOVZcHYdy7MvbFDr2heuG1sU8QVGZBWrDaLYlu%2FmIiE193%2F352id%2ByVyb%2FZ%2Blg5gojExQFRfySh8cLJ8YyETL75Dnw0Ro4d1jXzw0441Fm0sOkhGYFA1etbWi7IoBmj3Q5uOXsYCznF6gWrkW%2BCsl5gYCDINmeL6B7kJHL3sWyupLBx9HBLcNXMhB9J94oKW0RqEaLP3WgfaQjo0tTaSxWoiXoLJgfi3yAEHDKUmLdBHF4R7wKtu%2BTsd5YyqI7xdMuMzySrKjEMNfl%2F7wGOqUBxvsgVGhd%2Bt%2FDHK7QNTwxxr6G%2BAeDgjBb9Xu4y6mS4vdl44RETCxLF8FW3LlWgTygwUHk%2BBr3pbWJQk0TNF0jRxr%2FdBpAQS8jhIqfAMKP8J4vMqd4ittv%2Bo%2FkhffOC89EEyKcrD43Zlok4zsqtuU%2FXYZGcHIgshJ7t6pXjD2QtU8Ao5X0lcX0HFLNQIRhOk2D4XtVuijeZdIkeynxUFkx9awERyDJ&X-Amz-Signature=20a5575226da643fb8e3226c45120777b41b005fd55483557289e83eab697669&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5DNTZIK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU4o09Gt3kY8pzUx6Wzdg0pZo477ABiOwNqRUgSPZ6EAiEA0E2mvb3NkFJDHkB%2FxJplodz2F5AQ%2B1mydRa3QucyrHMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNs%2BQki114E86TUSbSrcA9nevlIEVMNbpsEsln%2BCmPYLeLjoxV3KIg%2BEoqr1addz5oc%2BKuXEETomN6Bb98OhmJ%2BHsoybjaXghISPFmdc8UabFaJpJ%2FxtVX57IISLpuM5mEaEYFL5Rcu3kjsW%2FykU%2FxAMYwmETlPeBmjEFUnFbBJfG01zXWvNsQ5VoIoXotZJoP71XsEK5EK4FPsaSRtS3JGElXgNr6LO1Rw7%2Buk1x3gvvcqVE%2F%2BI92efUqJyum0Sftf4%2B5XsfrnntMwPXq3gFmdixmbHGssFGkratJ2rqxoawYs3mND8WnnN7EQSjHsdCEfoyMVdy24qYSCNHwAe4JDCJuHOPHNG8Gb%2BOy6f1WPzzCVceEJoPpu4ToVoicM9GGv4WhC3kpT5p6HcNj197i2hpAUi1DHlBPYcfmgQTMWDXTGzHXRWvNkbWd81VS1XfsV3rLBiQU9p%2Bahmi4gFLzPL1kqXJJXNY%2BMcG7QUp9VxmdB%2F40n6wPV0lUQxqvSzaY3063c2ik6ud39ZyEnOxfLZmcWvX0Hhx9rtKsIT2MXFdgJIU5xUqsgOF1xdXXr6%2F%2B1Z8IHlfD0sets7nfWYE0WSVDxY0u%2BhdLnp9y6UQWgTvtKR8Wc6tMml32GpYDBMok6qkXrXEU2Yf20KMI%2Fl%2F7wGOqUBGdcVkVm%2B90J1QnknoWhrnrsazVoA6DNV3kmiE%2F%2FGh5m62103G4oUYzfgUdGUWqo2pi1cmCQ7LNitTwsPCLwgjWN%2FGinlUKDLWaVIvRQuYtavA980V0wpuWK6xv6Vw1AXlhPvvODD5tAU3qEO67FUleY0tFsnXP9JM%2B%2BzvF%2BFRWyHiiJlQopE0SPl8kiAl2CcA7lspuUEni2hyob6GC1ptWe26ayN&X-Amz-Signature=a93eec2507d16b628c0b12d4ed2b7675d5d82e2752550b41b1b58580cee711fc&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OHVJKBW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGz9oONBE2B10A1UPZuVq1axppowhY%2B7qGF9QnB92USdAiEA7h35%2BBShVXgPi8RQKOpjTplE0TGaUVo%2Bc5Z4bdmj2aEqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC5J5N6AQCvgix8NESrcA9hXKXJDNltiC10E2GWyNRwtMxoC%2BkWXSSBU0%2BNPwfoItSYUtExj7WIuWWwTksagyUN5Z09AWMvP71cNT47HElJZlFVSkHt17z%2F4Di6a2gfkJDxNEXOn12BsROiE0httavv7onjbn3xqNMYjoNaPFTVrIabFXOHrScfJDA%2F%2BwCUnsKvXVJdE5b6tN9nGGYnCtWDeFHWHwyPX4Fkhxs%2B18K6tjhyhIX3Pw6JGNgBG%2FQfz7LEwRU7nyIxT4Ue3VI%2Bg7eYw5wAUEiWI8Aihdh%2BTo%2B%2BKl3LAkzLpD2tRzFm%2FBCHMGlmnMzhIMA0p6%2FYbXyjblZ9R1dTuTccmKfEi9cEzLdwfDkUwuuLCOgvDNpRAEDpLuD%2BriDEIObcyCs4yYT4QJcfuY6ZAJq63kFObWGAbQT4tzJdCN1E9%2FojP1V2hf2o0h7SVc2hfrB0tt3%2BgiEGrvL1I%2BLl8LSzGd2R7cV9vGYUKCxdGBH4XW2wqNbk0qDlmqxBnjqTPBPYHojs4o2EG9HC8%2B%2B%2FS70H8bbvAeA7lAe3meRJRJqpmwUvEiAFUIOt9dFA7p5EG3kag8zoZOI27G0ngABG3mEt4e87kVEnDrLkO1ZNt1rw5R7FJ%2FJ8BlQaeSFd5goz70mHFqSheMMXl%2F7wGOqUBp2o2HP8rJ1Ui%2FqAWQh6p5wlaS88tB5yunsIr6gswft%2FwGUaVHrV9Txz8x%2FRUoAc6heAQVAyEeVsFlmp3DLHs%2F0WKx7WMuSMkaQfH6v27%2F1H6H7id2U%2BzFye9J5q9Vd%2BQozzkSOtITgBfwCHImLkaF%2BfZthTAffQnv%2B706pJU6YHa%2BvMj9nY3UgW9XCpI4dp9P6VrFh3xo%2FSzEaVeh67ll1K9%2BNMD&X-Amz-Signature=9aec8b793b9962b3705eae1afe33d6daae9849f1b92118bed7357327f61316f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666M5Z5KZ5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx96dIdhIlhhq2VhbclOnas2jJzAUhT0EfDie5FX8%2FNgIhAJo3eqrElCXZAZPCAOXuS6GsWy5p%2ByAA9CYJWOxWffD4KogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZAKacbQnQ3x6KlG4q3AMKhmwl%2FgCk4N5%2Bne%2B53ng%2FygBFgXcJtj7XcnNz6zOoAeRuLNOiXieZHT8Z%2F3rRhMYb1ZCuCg7lEAnY8R6HcSzx5St27vegUGT7sHuWhzHlZuHyALPYsL%2BspY80JBPo2TyyJPOvPH%2BM5XbRU5c1onJzg1yaqFmibXKD0ZTzYOJn%2FB0zikz%2F3SwkikBMA9RpgvSNyqZN%2Fx%2FG1yzZjToICVWT89GOD8E3j%2FT7ZIkyic7jH5FcBpEclf7qBof0midxGKP81Yt03S2z2v27n7RJiiZBGSznsk4iLlj4qUWwxRtgvx%2BI4%2FZqWOA1qBiTfoEIe%2BFRbirI91qv39NbmGVHdzPZlHaLosSpSbEzffazN3Wr7mBWeW6RvGaMMh9F1FWRuSdVndUeDmn3CMkSBOlj53oOrgD4GroIDFtmIdGPbfF83iTwrPocyFV%2BrEpLrnLTJKZPs9UG4IwEhkxgG36xpYDa%2F1QsBsprFZw%2Fr4qN%2FD1ikWkiq%2FrRdSizw%2FdiSHmJAUORG5h1I5yXNq7YzesGWxPCIbwJ55MwtR%2FAip7MZUKneBPrffGFcvZgj8HyRMqrjgJgTTKL4SV3iWwFSLEP9mQv%2Bb1BB1gN18rlKsTrUA0uJjtUkTzZiDFY9I4%2BVDCt5P%2B8BjqkAcYuEHg2XXoJG4L2CEO1aHPmdkcaM%2F1ifhDfkqHlWww%2F7uuSjY7qONn3jmqZZudGpxGqJbhGaAhpuAeayZtEC38dc2ayPMNqBMWx8MaIze4Ef1wjC9ktR29UDL59wpH2%2F8z5VGQ3jlDIkfon1CR7Wh%2FuHfzj5r4lc2zO07bzG3bgf0I1XZBMvqjlLPIfV6qP15%2F5M6qjztEo2JLz61MxHfJRkK78&X-Amz-Signature=94c9ac32ee6ccba9b84044008022b8909aaa6abbf7f3a2caa39a8586e3efa95b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DDUJ63Y%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmcXGsPzj1TZ2EiSY4r4IPa%2BDw4AlVgUb9D5yUFMlAwQIhAKD%2FSCvK86ejZC9fOBF%2FGJus9fwxIqziBDl7OFvU5VNkKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzoRegi3mRErnLuM8Uq3AOn5MmF8DLr5AGt8aVXImg13kwcsUTa7srjBx%2F4TaxRGwS45vWhcG5VzQBOTBMsSpttvMsfo%2FJGOHcAcircwy%2FSv54urjiJiWAK7l9SFBTVtF3l6zfKuOgnC2ttpGtRsLhbnazuqfVLnCVqI5SInRmtZR72cU6wXoQ1b8HMULsNQC6dFXyoVzLXCiGdl15H8ptPqln%2F5%2FOGEQz19Vq3kKENWRLnyJQvxdi9CtWfPaJtQ2LOpSb9IXflBq%2FiMfmV20u5M8Bk6qfpHMvthdlaBvrZYsGQ1tUJA37E679eTE8GdK8NYHJ9KpIzzdTGsfA%2Fuc05kbA1KxUS3NvQfKK5mpL7CJl1kKzJQevopn%2FChI46mPgxN53V9wfa2h4nsVqdcAXu6L1f8rUgbLrMN2qp0yg1yjs3OViowQP1yOWo07cXtlPwebNgu06cebBBuCzRv%2F1cTzSCa2YgLY98nI6aD9m7DDk4sXQ%2FMwgKooeRbTP7YI3%2BXDqxlcPNHsx40anmtYYrTL9P9nXcLiJQ5YUOmlcja7xG5KazncpVF9nw29vWXzsZVf7qnIt1jWC%2BNrV5OQ270Swiis%2FYR5jezOygqhLlKkpg6Vlbi33x7dmgASzOUESBWSNqG0ZkSgi85TDM5P%2B8BjqkASKLDtKmGWa2Krvoz6xhpus0EJoDoXT5%2B2ympUXKyu%2BPxD3aEIVEUQU%2Fo8KmJ4swT1kbMGRiJX7ve7mr3cI1n5IiHJ%2FpuLOuJk54owR1EHhZKTlMJQWhK2WFkJCL6yfdkZpPCpOu8TL2bA0FJT29r2Ndq1ylTSzEjYhyyLihEXfOjHdTnWLwNKDdTKd1Ft%2BLElD6e8RpP%2BQrPbTrKuUe%2BpIuhqMr&X-Amz-Signature=53ec6f1b41abf22329b0e3b838478804f76177226409c853d9d871b890f44194&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DDUJ63Y%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmcXGsPzj1TZ2EiSY4r4IPa%2BDw4AlVgUb9D5yUFMlAwQIhAKD%2FSCvK86ejZC9fOBF%2FGJus9fwxIqziBDl7OFvU5VNkKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzoRegi3mRErnLuM8Uq3AOn5MmF8DLr5AGt8aVXImg13kwcsUTa7srjBx%2F4TaxRGwS45vWhcG5VzQBOTBMsSpttvMsfo%2FJGOHcAcircwy%2FSv54urjiJiWAK7l9SFBTVtF3l6zfKuOgnC2ttpGtRsLhbnazuqfVLnCVqI5SInRmtZR72cU6wXoQ1b8HMULsNQC6dFXyoVzLXCiGdl15H8ptPqln%2F5%2FOGEQz19Vq3kKENWRLnyJQvxdi9CtWfPaJtQ2LOpSb9IXflBq%2FiMfmV20u5M8Bk6qfpHMvthdlaBvrZYsGQ1tUJA37E679eTE8GdK8NYHJ9KpIzzdTGsfA%2Fuc05kbA1KxUS3NvQfKK5mpL7CJl1kKzJQevopn%2FChI46mPgxN53V9wfa2h4nsVqdcAXu6L1f8rUgbLrMN2qp0yg1yjs3OViowQP1yOWo07cXtlPwebNgu06cebBBuCzRv%2F1cTzSCa2YgLY98nI6aD9m7DDk4sXQ%2FMwgKooeRbTP7YI3%2BXDqxlcPNHsx40anmtYYrTL9P9nXcLiJQ5YUOmlcja7xG5KazncpVF9nw29vWXzsZVf7qnIt1jWC%2BNrV5OQ270Swiis%2FYR5jezOygqhLlKkpg6Vlbi33x7dmgASzOUESBWSNqG0ZkSgi85TDM5P%2B8BjqkASKLDtKmGWa2Krvoz6xhpus0EJoDoXT5%2B2ympUXKyu%2BPxD3aEIVEUQU%2Fo8KmJ4swT1kbMGRiJX7ve7mr3cI1n5IiHJ%2FpuLOuJk54owR1EHhZKTlMJQWhK2WFkJCL6yfdkZpPCpOu8TL2bA0FJT29r2Ndq1ylTSzEjYhyyLihEXfOjHdTnWLwNKDdTKd1Ft%2BLElD6e8RpP%2BQrPbTrKuUe%2BpIuhqMr&X-Amz-Signature=630ce3250c056932941b1ee455bf0486296609b72846c3e306ca396dc8708d18&X-Amz-SignedHeaders=host&x-id=GetObject)
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