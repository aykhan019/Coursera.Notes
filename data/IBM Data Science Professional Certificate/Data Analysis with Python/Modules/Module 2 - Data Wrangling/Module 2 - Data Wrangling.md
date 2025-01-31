

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXTDUKSA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvbVLgH0yFfty6g2wog%2FpDRC1JjnwNVUYKfdYlDsK3KwIgeMECJVnVA2S5Po9irXG7tJ7whIgiTswcZVd9jngmKT8qiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGy2hH94CSYZLOvESyrcA4lpVR%2BlAExpmKmYhQyWP86Zjiy7tlfx993OAdwzM9vjozluwcxRHRM88EXZSurMOLGfXLLDz2qXpsBhVQUbBzyIyNOE58vB2BQIsvDrBg%2FJmGzIxdNm%2BrsTAfQmGKntXvPlXWzOwVqRK3HhXn9DJ6Z%2FmSqI1lFs3YMWdt3hqJ8qgbNeZjeLiNNYoPO9Q4R%2Bw%2BZb80sgjrP3Oeaw71GayGIWXcyFAa%2ByI8OXTPt6vb%2FUMc0rjWdPRL1xSPlWkjEHC28Lavuslbf3N6n4kxenlDD9%2Bp9iSpe3JLLLAZDMOX%2Bm%2Fr7GY6c7kTkuCpeqg7seUtEeIbM%2FY2iZJEZMzkDJTc%2Bh7f4qRQ5Yif3MrzXsWgGped76RvDUuG2dAzfPYKmHlcdn2xdEhniw0I9S5ax9Ijuqzj1VFimwbPrVAg86wsaeEutitsRI0q%2B3U2AftetxvcVFvqETSWn2jN8usK0TCpFfwFQ7qr2ADdpAVZdSHZIecT8BTqz%2FMn4S%2BuqSZ3m2lTKhMQm2Gl1eHcC24J7uQPPFvwe1adX1kItHoIDp%2FiCNWfNmDA33JB20AxtuNiifgJ5SJW0VRj43RCkrQXtEVjVv2drjO57sD56VmVPXetyT8MoFURr2yl0U33inMMeP87wGOqUB6qzalDVjPbrq8UWJ3VFmrf0FZFcqUvonj0gDM8CxhWwJMfIWKOLA%2Bgb6FcVNJv%2Fb4zvFurqiehHnjcePBDGyE4cnp3qUymkm2q5OfrVpCFNDHIxkJe8REBuk8hx%2Fdh8lLLvxykkkUnskHQD4NoSSMevIY6byTM1mvMtf1iy32eQp6KygtEL3s1nyr1ghrC7S%2B4XpvYaOTlYT3znxqR0xUXu7aGwP&X-Amz-Signature=7379dea1ec45506e37498da62629501784192f673b97a6bb941d0e572be844ce&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUPLE5YO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHgJjU7Obg6o2UxsOba1KLcWyfC847kwtxy3Ys0k8LeAIhAImR2%2BqkJ9Ht478smfBZOM8xPK%2BTaN9F%2FOoKXj0VgEMbKogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxvuolMd%2FyZuoG2yl8q3AMjvI1%2FPoqjzIoa50l8rmljjoVtmzvBqrnBCv4POjFYdHX%2Fas2VVvyy5j6zZcVzGPxCfqSkR8MpnyJ1JHxoK%2BWCeKEf83tP7S3mOe58b1yOwojNXDPSGnnyqDCYzJNA8GI3Dznm78y6aWRn9StBsSnb5%2FfC1kYMMgDbKHCYjUH8peaE%2BrGrgGUv0pyKwvxB4pRDG9J0W6fsMdjm6vPCda70ENdfo%2BOWy%2F8npbXlQwRZH2vuCIY40bwqhySSh953109WnHSkmgUXy6Z9HQp8j9xBPkg9Erq%2FLPDgyud3Pnz2BogkwkRged%2F9JGoMRlTtv8DZW%2F1XzXySyhEfBTj%2BTiYrSQZqumabNLcC5KceKupBf8%2F82mCwq43rwpsv3SRjGbIyV4VXViuMolc7jhm82P6vYFLjZVsH9GkysQ2kapgfoA20kNgGf6bUs6nKAn6SaOXKSIlbeEVgGFfJ%2F1wouuo4Nqo2Ey8Lst%2BSgqSVSUmHpeemN1lO6xC4Re9CJ1K95DMuCqU79jM6Wtq9EmrUxxf1bVGWBO1uZZs29F1kWCeYertcSEz%2FAGkkcIzGccWm0bWmb3brVxnajTuMhjPZrSEko0sHI%2BcA00IjU8H5YNrSvfOw7GY5GPiH6Ki51TCpj%2FO8BjqkAWNGntUPlU93qzGlWVFD8qz5fVDVBFiVhS8Prjw6isEwsf63s43mvA%2FXvbmZ8OKs26b2y784B33xzWJrY96xPM%2Bsgj1hy5%2FnQXCRWYL12MAqFZALm5VJ5QsB6PnPqd3kM9T3v%2BOCPdLtAUftGOMM1jn4OkashXAZ75DrDSWy3DFp%2FmmbapYu%2BjPpCTzltBGyYZhLr8EITHuYEUBF0JdFeQs2toxF&X-Amz-Signature=bbfc969de2780acf74c02a1e207152215c5fece232b40ba879436f47279167cd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFKTEJIG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuTFEkAdNb9Z5K7npIOEj2ywmLQSjTq%2FhpnZSVR6eBjQIgWIbJW9qzsqHWdFZ3MSXmRmk9l0qSgq6QVEglvDE7F1sqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkDNtczk9EE0IXIECrcA34vYdhlWa31Lj7%2F%2BCgxAnBa7l0DQiymGqM8dji4MhZbnkIgVrXEbNZjllpY9XNYBLmtynp2IKoa0XrDg%2FmwMMussrm0xwCYvce0ftIPsqNmMEbxiWZ4Ho%2BWU3zt%2FO1RbjO4RpNpKnzHHLkBD6CcUNd3ia%2BMUAN3uR2%2B4KDcTzSE0eRfYqTCVbq%2FhbyvEgG9kGSsf8f5hpe1loZZGX%2FK6biLTYJpnDmKsOB5hhq3JF5bElQHFzzhAXLxlGH3bh4d1Ig2jsIHJEK9lVl3an5cYzkP%2BxOUt5KGc5cZsPHRlvxuzPGMoknd11ZfxOhfgfGjG1RCF2WJPLPr1heu8n%2BPm7dEvZXUZnFFc%2FHsapOys%2FfcZeJhL2LH5HY060xiO%2Bj1gyyPKQj9yW0fyGroRUxHt%2Fz06WAkLcKWOmPxOFvilPo5fIIwb07NhiqSF1lLnct7ePVLVSW762TzUKQ8WFVilPGqwDylUSv4NfrhibNVNScdVbkbVcz%2BrUtYCW6oxvg7%2BBjXqFyunbO4t%2FlR%2BK7CK8gjLg2EXruND8M6AX1N7IRNJe6h2LTd7plxVdb4VxlGboJ5Q9uRheEeFVzLXYYuA7YX14MmT2IgsU%2BSIn4iqkBm3aCxvP6v51efVFotMImR87wGOqUB1TNd5nf65m%2BD0zyM08qrUn1ewAJ9L4pkcjR7TydR%2B9Y%2BTD9HH0w6beJu1s0hXsgkOcx5QYxHeoJv47WiVz3gImZCUOlDTQj9%2FnTeTOoLTpqgENXInKuwfw2solD1frFKY3%2F%2F0LPNVik9nRVGhnNgdUVumqQmXbMnedUwzdojr88LNxXB6nxqc%2FV%2FVrTKXA9VyWJjnTBOBpuxTtzONgNuLDWULVFz&X-Amz-Signature=061bcd00d02df9d853fd9e338d97bdbcc15f82997a1f6f57b2dadf3151d2a426&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNOXKOV7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRnnzOI%2BFmzL3c%2FBVF8%2BYTcefhIgmGfo8bHBGkasRa7wIhAKmJDMbv%2Fg9%2B58DVgrirlB7kkFcPznyrKI2xxZ2DUk25KogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyHKn0iYv7lJfXkfMq3ANYT3IKN9Fs4SBh8oN862QfH1QjSDNP4SWVVga6GSKf2o1j7M%2B8VzXXdAxi6GonS904bXuDuOkQfVUjbyYyNLkdmtKUZC6jV8NRUw73tk6lRDBg1MHqd%2FpAo%2FSjnXHqATH%2B6d2thuqxINh11l4eesUHazgVz9tu5bFiywfY9MVdS6bjaZZBMBkFY3Y92ldQ1PVSJoFG7TIzZF2xejjiapaR39e6lNjtBAim%2FB8JYhIGrIyOXPdM7LrBRhqgnUFvdCR9WMxoQf%2B%2BXnRCoJ17SBKA1VzYM0jomh9F%2BUtXtV3HV1BUzPoaVr%2BZvmopDYWsx1osRdSkWQzmQoHcddfeowhMBUKcqJD3R8Xxj%2BxhtfhAJAA%2B97GJSQgY2ykx7HnRmTpFvlf60RP%2B0MPn2GlZ0lOmzqWVwkS%2Fvpb%2BGahGfMCsC9rhm1viet2uuLXxDhGtzSEEPNMZuWQ4Mi08MwP7DiSgs8Pf9ee2cukxJ71zE1U%2B7Hu85yuQYUBNmc2eBmKiBWYo4lykhDtVLA30J1H9CGWCqyD4KXxGdrbtLUkE07d1RsTcz2XISX7hmamQKOk6ip53IFjg6UxvZ84%2BIbDw6ulUHlWuZQjksI6NOM3IOjzXgykJRjOWMpF%2F6qdO4jDQj%2FO8BjqkAT9tFo5IDer8O6VEx1FrN247UTnUkZLZWXCIk8jiZujXOu4elruu8BuR4glDp7YgM%2FE3hlulpbbawjrz1KVXR5zihgbgrCt%2BGzC5WmPho5NH%2FUYyvhoVNAPUCCOC8CijVUOY7etHRJ7%2FdqB%2FVXNaUUPZX40jokQhaH7HlT7Mnn%2BJAj60xlhkZhasI7SohjYGJes6HkevNGd4VXG8k9P9k2LGQLoS&X-Amz-Signature=3d2111ec798ce482219029c1f2c816fa994eb124e6dde23b14b4033cdd51dd36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OJULDJG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVKeQtLsVxZaksZ9b1Kff9yTybsncYISaoQydnIt5Z6wIhALOWIt69ZbdiRpOIqdgwxpmYR%2F9iDcmw%2BJg%2FBTFvIsXTKogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwa7qbOkSi5vBbPDC0q3AMl5XxvK16heBKp2pKObulyMq9N4hI9NS1W5TbWe0GOGapH%2FNMHyfDDVwwgRmeAfqlvOCrRRajiY7sGvp0U3QKHEmq11gwYZMbRf1kjGymNlmmNKP8hpZo%2BU%2FUbvyXUa66lyXy%2FVVJOlJMDDBAB8BP7btfnrtsY%2Fo6WHDtu%2Ftmxsu93rMsOcBYeA%2BPmlxDcuGr9AZ6%2FIz%2BFw%2FUEJcBRrovVyO3DBkpMa%2Fs3MKrJu9ncDzEDxdtWsBh0zdRs5Y8iiWAMpDkhssQ%2FKjagxZBtg%2ByUWyxjzzRPyzRVBS%2FkDi6cmjt6UtbtfSx5ZOqPEyGpNim5A3eikFENcfWmupf4%2B3Rc2PVTSv6LMsnnCyclGc6vXuC4tH%2BG%2BgYO9OUuivqhxftIVFKe2mslm%2B1H4fGgLyfUZ%2BXxIh8onXHJUJU%2BFyN7kwakRtWo6pJDtt339MIO1ZtG3Ex0DVwA3zo16jQiuxnZmLc%2FsGHD2CTBtQigh87mZvfj7O32eEwA4DpLPImkSLkfOLGBL3UBgca63oy0HAQCvoOdRMET2rc%2FZ6HBEZ2cI20lXIVRh07wHz7uOOzZ0rdUI5ngZ4%2FE5tUpYyyjMVGBCT4TpQ3KTiZIpAbOe7h2sWLWB7NTGSs0ayd5GTDQj%2FO8BjqkAY9zzW1v0ybXcLl2E1b36mi7ClyHTmWi9dPIg2qu7qKvFGgXlTF4D2ZJvsozERGepOOWqpUESXNgCtDv2eVZsjQ9MSfKKnZhvphsTIf1KuV%2FRJbm5QxQnqG3xhyM3C0GmF8vawMBHJPTL8Xrp9OT8LPSOgO0sRwoVF5ssOhFlhL6lC2z9A%2BFyfXSec7NoMN9i3VP0jo4P0Frivbv7f5B6ZVRNhiO&X-Amz-Signature=fd9a112329d6d660f5e4422be3642d8910ea46934084ac1fff86900d11d89c37&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIYOGNJ4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPamhJYXqozncNFHk%2FAo9VY%2FCcXw36XtA9D4hVoOzTYQIhAJ%2FXfmkXnwwVVuRK52N0LZaUKVMSWmTVlLW7q4jkTR5LKogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw3qup8tsbqPUyuxIMq3ANgNs5W66ksSlEB6RK7i8yOxzCMcXFnhwIA0yVnh5vXRDKAyCMWMKLlhYdWKMlosKDILVk4RsTDqNIKkskcWUScqYtbSiaTABakq8cgvNiva9JVULvnCOfFjPHFgXxGqxy4BFY%2F5HC83lBV93sdXXyesiljmaueqadlpMzTHQcPWKLl1WLwpzzv8ENt7uFxWWrwOOVgqlWyWxy5TpCmpNEoqrT2BYXVpm6ZgdhEdHu2GjQcZVnor%2FlNz82xT6vrKhermwjH5NeHzVjK8be8VpcYtm26Ydhmfd7I1L20qwVrlZr7ouaepyj2n9GrXY5M7Hf%2Fn8TNGNU1RA3nUUElDheMlmsJS%2FnrBdXWtl87EpYWbDFGuCyKM0lfKAe2QzKM4K999UoX%2FApau%2BlEB9wA8mh311R4jC%2BqaFcL5sG1YLZ0xc6CsHDaAkekGS%2FpFQGjeVhyICJmZFCZmCKyiGTk0%2B0IPrQnzhwKQf9nMeg85mDqu%2B41zBZySzXoKKWkYaJ0T4epSycVcBMsiJaj8pTTqG4VR4wbtB0Pc3ePFyTj7FrHslIrcpMvm%2FCFw0S54B8kRQ0KJQPk1fhRlrRT21%2F%2FTGGkjy6fcFo369zPAf1nN0J7DmsVbp9L%2Fb9lSmQdhzDQj%2FO8BjqkAft8oK1b8PLlve%2Fel0YXYT%2FjUyX5r11hNetoOGwuIk8lx9EDnU9sk8703Q6oAoDKPLLm5K0L8dH8c2nBhO9Da%2FcMIvRyXpduMLKFEjj%2B3T4C4lJdI4xybfuKA8rSoFd9fe%2BlXwfYzKOzwgf2%2FQazRsZaGkxEa4G70UZelx5gJaNx8dSRAhxMwsIGbwRnmBXj10omP5Shv1JesFMKRM4mCnh5UNPw&X-Amz-Signature=1d05351a5f32f6fca44a86fd16e08ba6a01bdc8ab6d547bd9828d90661682426&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFL2KLT7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA4%2FCzfJT0v4Tr2Ucv3O1VXcE8gLNiUT1V%2FRlBfsX0SUAiEAjfBOnAcldpszHpj2MDzD1gj%2BZ6YgOi6Qxn8KgWowkaMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKvMZEyFC3IKt3N52yrcA108ZURaf6lM4h%2Brvgvm3ASfWGrX53PqeuKzVCJCDLRRUp5sZe9KLmUfksXNnQjoa493lyn%2B7vfdyeT4hrtE6K4VYiLcpe7eizTL92xmQBTfvfajG6BUrViPHCrcTqkLQ%2FTmrTwKDO7hI4WWXVU4EivFbFmxHRwPZ69%2FGgCacUv8SshbTEn1ktfZ%2BchS8JF%2Bp7HsvMNEl%2Fy2Szn0TP8TPSsk1ZR%2B%2FIjyhgkNgTa7EhipPYu2Vu5quG4LEARYyL6Cv%2FLEbvQUDQh%2FTNqFli1VNHe0LrKR8uT48H0dhtRg34d0GtX7Pn82JL4NLIXAz7Mn4l2vKekgpEEzWqFpX%2Bez3xFhgYKMVqav%2Fc8U7%2BrLJIi1xTgGFRnrXZapHCp8TZjAv2KZt%2BST4Pv6BLfb5SxNKeudqP4CHA%2BA%2B9XecpHZG3zIv0TsmHC7IKAoSpx2RszdVAdaBMBfSXjEaqPz8OOZ3ggEqldB2IHn4sq%2BBBsbbTGvdpcIpBbRz7riwG%2FnO5Jf8clmDOfXx1GAAh%2BZcCLYthvoBLqvAB%2FkKrv6s0Lbvy%2F4QO9uLQ9T%2FiHAuicsnC1bHZkLboYz0uLnelDjYXK9tUvsA0V68oGjm5FJjmB3TuskVlzmaqijzYDxcZbaMLyP87wGOqUBOV7fVJMhL0rr2oI04pWFS6C2vUQV%2FaH7E4nZ883RSCB8Mdct1zzEAqlVdfdGwPdSeVaBFpcG8NsE%2Fc0BRTMw%2Bbnk59aa35UQPdua4%2BT93U0kA6cwg0epxhpvNav7%2BZgggLN%2ByPzVsnE1n5iz85yjHUeaoGGF8WPo2FtwP3kJtSc2iehAWf3pjiaTSPsuMbsTqDT4dvkzRAatFJTGDEWbpOc6%2F4Zu&X-Amz-Signature=be16bbbb0b3e661aabb127c09f98773e5821a52af99d880bb1a6bc3594b123db&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGYAYL73%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCegm2VQOMFmFTSiLixjHEV2ZgBkHH7LnDc5u7KSvZWjAIgEuu34EjXf1r4fbITKT%2FyOWaquW241Ea8CaFKWVYWSakqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJf34EUdY8Cbqq3vGCrcAyCQmT4mZN%2BTGHCiz4K%2BGYJ1tvXly2rmodu4wetYu%2BNUZGqDTNg4ko7wKU4fygRDkQn09IbQ1%2BcWqlxhO61Jvkky28QuONOg%2FMLdq%2BFUxOfIMSaVkRPF8nUbGSagfBXfBqkmPEmySLJ55LSbUNTpvhEZEoPb%2FV5ga47kct9YVTBb5B4NjfrtPst6jMQlHW%2BiPKfjfPhYz8OvY1WeepPgSUaVA81w3aZrnT1R7D0WuC523x%2BgMNIlzOwFDXFYEBsY%2Fedq5XJOHRSMiGkAJ6%2B8bZ%2Fqv50VLp9uDiRnlxjcOeL0Gs0Ej6IcAGWRe2egYCjDdL23rb3yjVGfGv2tP2yi83z6zPNhUBjLHB4dc7TjJsVsL8nJu9DVZlD12QYb1O59r9ZFw19K%2Bb99bCkcQDAy%2BiotRAW6MQAHOzCbKJ3ElNGmqsILyNakdv2lZ1j5vpihpnmjjFErx7WmhHeQZFVSh0t%2BV8xOaVOL%2BK3xWM9R4Tv%2B4pw3h6FcmLb5EccT8mb0OorAK29IPh%2BvyGlV3UuWpJMvLySZYqvgxB9F2dXXH08XXk4h8u%2Bg1NVsd4at93zxLWSEjAxOIksqn7ohUi31Y7MwIJeWSNM0RFVel%2FirprjxEjuMcr3GcXyYtyZvMM6P87wGOqUBK9SKzGytT%2Fdc%2FORC94X25FH6QRiAf4HP3cQSxz3mHX7XC6tTkw8V%2F7QojklEEyCyjUZndmuEwTFiVeo%2BO3FKuoqHMYAUPx%2F5xUkeGMQ2k4J65qDxKvsAnEl7teGvlXzJ4DO%2BzFt5%2BRocRPbEnN8%2B6V1SjQlXwDdID1u3H1g%2Bw2IVTTtqtpfSQhsQN3YC28lBUG9vK1XVKuZyv1GCLwvQNh3RYCVE&X-Amz-Signature=015ef4964cb765282aa1917e7a75a8665fae986bb13d5edfbcc52e2c4cd4d9d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OJULDJG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVKeQtLsVxZaksZ9b1Kff9yTybsncYISaoQydnIt5Z6wIhALOWIt69ZbdiRpOIqdgwxpmYR%2F9iDcmw%2BJg%2FBTFvIsXTKogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwa7qbOkSi5vBbPDC0q3AMl5XxvK16heBKp2pKObulyMq9N4hI9NS1W5TbWe0GOGapH%2FNMHyfDDVwwgRmeAfqlvOCrRRajiY7sGvp0U3QKHEmq11gwYZMbRf1kjGymNlmmNKP8hpZo%2BU%2FUbvyXUa66lyXy%2FVVJOlJMDDBAB8BP7btfnrtsY%2Fo6WHDtu%2Ftmxsu93rMsOcBYeA%2BPmlxDcuGr9AZ6%2FIz%2BFw%2FUEJcBRrovVyO3DBkpMa%2Fs3MKrJu9ncDzEDxdtWsBh0zdRs5Y8iiWAMpDkhssQ%2FKjagxZBtg%2ByUWyxjzzRPyzRVBS%2FkDi6cmjt6UtbtfSx5ZOqPEyGpNim5A3eikFENcfWmupf4%2B3Rc2PVTSv6LMsnnCyclGc6vXuC4tH%2BG%2BgYO9OUuivqhxftIVFKe2mslm%2B1H4fGgLyfUZ%2BXxIh8onXHJUJU%2BFyN7kwakRtWo6pJDtt339MIO1ZtG3Ex0DVwA3zo16jQiuxnZmLc%2FsGHD2CTBtQigh87mZvfj7O32eEwA4DpLPImkSLkfOLGBL3UBgca63oy0HAQCvoOdRMET2rc%2FZ6HBEZ2cI20lXIVRh07wHz7uOOzZ0rdUI5ngZ4%2FE5tUpYyyjMVGBCT4TpQ3KTiZIpAbOe7h2sWLWB7NTGSs0ayd5GTDQj%2FO8BjqkAY9zzW1v0ybXcLl2E1b36mi7ClyHTmWi9dPIg2qu7qKvFGgXlTF4D2ZJvsozERGepOOWqpUESXNgCtDv2eVZsjQ9MSfKKnZhvphsTIf1KuV%2FRJbm5QxQnqG3xhyM3C0GmF8vawMBHJPTL8Xrp9OT8LPSOgO0sRwoVF5ssOhFlhL6lC2z9A%2BFyfXSec7NoMN9i3VP0jo4P0Frivbv7f5B6ZVRNhiO&X-Amz-Signature=59bcf1c3758fd5f65fc6f8eefe57675a72a25b1dac9639bcaae9b754e27cff70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQYMYGNI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEyz%2FX8hRYfKnCWhmJMWDrwfGDCRB2gC1hbWbUXxjVdAAiEAvjtEaFvOPPuzsHVOyXZZCkmuCYc%2BTC4qgwLO%2BZuHaXQqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFxRRVi3LpwTHZiEASrcA4SocEZ%2FO7hojqJYPB8PKy2Ezqg1p%2B2GgDQqEsOG%2BtE24VRL7POoaOMe7rI7sHXJ4sRqMMdL5uHySLwOP%2Bk2MEsxWlCUVC8nVMz0iESZc%2Fh9JfGmgTD4jvSnfNV%2FXWi2JiDO2J%2FudpYSjbxSQFLrumyY%2BJWAzlxd5eA2Elq6e22yyRh6EW5ZjNkzctWd9w00mZPChE7S6UnRedl2St0XKmYR9pJW%2F87DUrQeCmprGZclEjBRM83N3Zxjjza%2F4aikfP7bGoQUo9vYEJHuHlNESNLPxOvYWJlkMJwuPP47Un1SvhkGobR6fyMnreME0HlscVn%2F%2FNjWbC8eonzMjWtzCYhbwpp9WkjUVf2Y5z4Apb7xLl3bd6yVfqwEIT0xy2aSSdfjTztPrF%2FT4hemtfnvF0BMZdJmUGd54FXv1KYQWxzHonEiLIwoH7B6AHbU%2FL0Eqeqh57%2BGi4XiHYXXxeOkj9GOTZHmIzEEI7%2FRDNEzycqTRW4zr2t51URaT55D%2FZ6QF7hkMaofPpfDmsaznEYWib5hNAUvhzGWX0TW0YYdEOicXl%2FVXnYfdaSXrOtiebbq3FCwLVPFVMERzQFU414Wkg0KQTmX%2FUczlVsXkU0%2Fw7r7X%2FTcR5VCYwp7j8sVMP2P87wGOqUBGfOc7GjHUD6BMT5FbzDQP1vLUqYASOhiyqWdgDJnYsA1G4oCViXoftAKcfRM26yzGjhw7PoLDvXoBCy6VJfZwN7OlszET7YHWKW6P7QcqlDgBOpG5xS8NlYmCkKkLcD0AwBOfwiAIyi10yZSBBbYW4Op9GddmPZwQeMvgBPYaeE8%2FzP%2FLsLan8LezOMHApab8nV1CPDDulLtKTUsxcvB9CBx0hBA&X-Amz-Signature=b752d31804dfad30fcaf1c71e409fb37a3fee756fe664408f23f7f2c21f629bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQYMYGNI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEyz%2FX8hRYfKnCWhmJMWDrwfGDCRB2gC1hbWbUXxjVdAAiEAvjtEaFvOPPuzsHVOyXZZCkmuCYc%2BTC4qgwLO%2BZuHaXQqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFxRRVi3LpwTHZiEASrcA4SocEZ%2FO7hojqJYPB8PKy2Ezqg1p%2B2GgDQqEsOG%2BtE24VRL7POoaOMe7rI7sHXJ4sRqMMdL5uHySLwOP%2Bk2MEsxWlCUVC8nVMz0iESZc%2Fh9JfGmgTD4jvSnfNV%2FXWi2JiDO2J%2FudpYSjbxSQFLrumyY%2BJWAzlxd5eA2Elq6e22yyRh6EW5ZjNkzctWd9w00mZPChE7S6UnRedl2St0XKmYR9pJW%2F87DUrQeCmprGZclEjBRM83N3Zxjjza%2F4aikfP7bGoQUo9vYEJHuHlNESNLPxOvYWJlkMJwuPP47Un1SvhkGobR6fyMnreME0HlscVn%2F%2FNjWbC8eonzMjWtzCYhbwpp9WkjUVf2Y5z4Apb7xLl3bd6yVfqwEIT0xy2aSSdfjTztPrF%2FT4hemtfnvF0BMZdJmUGd54FXv1KYQWxzHonEiLIwoH7B6AHbU%2FL0Eqeqh57%2BGi4XiHYXXxeOkj9GOTZHmIzEEI7%2FRDNEzycqTRW4zr2t51URaT55D%2FZ6QF7hkMaofPpfDmsaznEYWib5hNAUvhzGWX0TW0YYdEOicXl%2FVXnYfdaSXrOtiebbq3FCwLVPFVMERzQFU414Wkg0KQTmX%2FUczlVsXkU0%2Fw7r7X%2FTcR5VCYwp7j8sVMP2P87wGOqUBGfOc7GjHUD6BMT5FbzDQP1vLUqYASOhiyqWdgDJnYsA1G4oCViXoftAKcfRM26yzGjhw7PoLDvXoBCy6VJfZwN7OlszET7YHWKW6P7QcqlDgBOpG5xS8NlYmCkKkLcD0AwBOfwiAIyi10yZSBBbYW4Op9GddmPZwQeMvgBPYaeE8%2FzP%2FLsLan8LezOMHApab8nV1CPDDulLtKTUsxcvB9CBx0hBA&X-Amz-Signature=e0fec233c6dbab8304c0324362749a237918b11e7cec7b02e64719e18f574ce1&X-Amz-SignedHeaders=host&x-id=GetObject)
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