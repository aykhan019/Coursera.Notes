

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XC4KIZNI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC60SiACe4VdCxHlRHu0vXU1VRuLcH9jrGVr6xUTT5dlgIhAOqbG0LZeTdgRtMb2un42C0kxJWQiO9zr2aUI1RAb5lOKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXwD9uKIObQkVeWPgq3APhXAVbuThBHfJpIpCteCGGuk4hvKrQDqjAO94kfCSJktTJzlaj2OtJzrDMYpW0N3BEvwSWBItmpC%2Bl0GdfZ%2BTLXPxqcEWNdjHCyJ4CXroomrxAu%2FFSP%2BA9K4b1cBsOgpdMpN%2B1onVAsJGJarhI3%2FuTeYNh2MgzECI5LiUdvTcledADIjTLT9kC3MFlBeejzBUtS2KHYQpOS2xeSh7E1uzxNBnLfvtkrcnNNZSAfeq8YSfQhsO5sxW8JZysxXOf7Em3fnVCNUs6ZKU2Z2xjTPqvuI3XK%2FN6NOV7rStEaNRwx4penLXyanlfRWNw0nuWjiVLwt7d9PLgLdyBvVl3O9mQklSSfOf3dGENOtG1l%2FG738nAN6qDiFVJKm3tVvqAprvoPxiTZdwPiPLP%2FWPf8zJACqQc%2BHJTiDoGMY5SP4NjkOeld4vMuBQ4H8x2efEh4lRXw%2B62HdJN6%2FFVCyRcfEzvYhV%2BFZ6N2uDU3J92PK%2FxylFeX3HKhtqdT%2FWDviQfYu6DVAmYJ2W2rax5H67etTJTl%2Bx1RrRxEB5Y%2FelaGRY0DAhCq%2BxFPWQ4Hyu3C44u1%2FRSiEpF%2FOvl53cH5JA4kaIZp8FonY4EcfgILG80eXe%2BIJfaJi%2Bd6WCVzLnvkzCOlPW8BjqkAXbPELUr%2Fki46HP6TolslPkzucpfd11pvVG7DLvgywl0gUfgZXNS44iMUf0Zigbzfot%2BcMPN1XSqXvYVC7ZkghLk07qwOrAl1Wdn6gkxaRsvLbGtqgCg2bl2kWtVO%2Fotyo0chKsKC2yp1zWmEoUwbWF558xIalOOMkGxxbTbbwkuT9DujcbO2xDxJIwAPx20MP89j4tn8fR2AOscl9I%2B2EM3QT3K&X-Amz-Signature=a643de8f8c656e213a402bb6d590813660a83bf84ef8740f411b6f57db3f3b40&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNHU3A6O%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG01CcBv67eL6lrvBBVQE7q47ZICm0erDoOl8E9RJ5oGAiEAoLaNGC6w6V2OTBG0VrYH2gF9Snl0rvmDocbAXeBmWzgqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ5yeQb6lYyXT95zuircA5OTuQAxcgkNSA7luOlRgEW48RbY4WeGnxnxZyemQsypx4sZmJFHscXOtX2mQFzHXdP8d2uYBeW8emhqjSNqejyeEB2rzPBUzHOuZC80U7QEEEpkN4dO2qtI43HPOwWjTmTw9MbZmjFYVqFR3qbOsSHfEAG6CN1%2F7fnmoPoI%2B3GLj6ay0g%2B3Numk59Q2Um0j%2BdgGMYW5Y5ruSrmeGmCtTslhudl%2BNg0MNbwNuy42Yzxe9f1hAn69jjU1ugA9CqJkSywFW3Wem0qyGPLw9dQFYYPFbBBemy8OvpZ5eBuWRlVFAmoAvDg0Ivb15vPvhkDtkv70bC%2F5r3zRlvT%2FJIykcXhC2T25FPRzLMgBwKtv0iZ6AmAUCSfEAvtUTB9CtsF3%2BJqYtPRfKTfaXjlfpl6GKMU2OKKkrD3Z3TRYhNq5uwR0PTqPd5%2F5vw3x2pXLoJFXqruUQjLzcewYCr7L1FzPiQDoi2Ddm0r%2BC5UoSP6LQRe1EsFtFUlYbha1ejXLwPq25A%2FjpxAEsF5Zv2uEOg5MvisI%2BmwBl%2Fl1IyZ%2BXwAYPSZ%2BtdiKYHDUD61uzbXL7omMDmA%2F7UYrI7ChktJN5vDyuJHseccKC3R9uEsn9yIlaMyq4YHAQTVuKCVQleVHMO%2BT9bwGOqUBnmKXYh4jTe9hl7fMoRN6sbcB0DRDH%2BdhA%2BbwMelCg7rb4n8NM%2BxLlEC2sVlorfFfGt6rHjCgGCO5QWxIrsYBN6sAWZhMN3slNEsLpONPTJxwHutdx0d4SP0pyDKMS3AIaMUu0kdVS5e3SxU9fZ1EvAT0%2B4OkQ4%2FvpebAXvSI8BLXFrDWlS8EL9ctNQMT1OyDwbbMU%2Bo4IfqA472VCgec6p2bOgNX&X-Amz-Signature=993bf581adb4e3da99a88f0aad49ed6491dccdb5c1a8e76eff8d1c07026927a1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWOAYDTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFFbOk3phYqtjbvrAfGBhY%2F4Rj2eyml8WLHcU7DmC3QrAiEA4c1kdPbEf0l1iJQKHQZ6dkt%2FKmbQYMAviEv79sEOzAkqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ35qJK1v8dFJLQkgSrcA5ZB8hLnEpna3Pa8ErWiEvvwHTn1G471wOnTZlQkzYPWDL2uHqtO9nBRA0kdS6h%2F3bXo5HwitxKfkDFPWk%2FjLyY6qETRc1H5hN65t6geSnQtbI2Zt26vcyDcVzV%2Bu2ewY7qRLlidyVMe0EkMurtFSOls6L5IJP9xgvsFAWyajSIC9bAPqJ5Evvr89e9xOQSrQ60zXJCtbvBL6n2Gm9%2B%2BFu4u0MEeAXEQcjzx8AAgAhaxm84%2BKxsifRChHAyFWBNGQGwQlQEJD57y%2BpI8Dbq5ICElH6UGFQD9vgpvnroZapwkYaA1X3NCGMiyFh2I9msSAJgNf0hQVFu1zgkBcvsSwMSaJW6lT%2BlYM4k9mQJlkbMIPIUIO8LmEtK4GAHJYrBqBH3q8MOcfGRgXbfkMgZmIq1ueNpNGSqx05dRQXrFy9l%2FMNYrm9M%2BhCh7DWb1t9xEDatFolnk81QnnBiYwH7wsAZxAJ1vQGcsz0LTlPrmwhxgzwxr5QRnDSIuOvLb827Aed1pAzWfzCwmJd54IlPqYS3QbRqxw54Em9JOjiaBSFhY6B8ez3QRlTR%2FMBTOZHbv9d26TDKazXmYrjlGsc%2Fkn%2FceIR1z9DwnQsBU%2FQWLy1uUvBMcbsmQyvuexaooMO6T9bwGOqUBuGi3F4DypzJqpiCibsCV6DoKczYC2NR5WLmoFJ3SRHoMmkmS1%2BEaJqnpraIs5NK5TyM4NQmpe2mHWQMqDzQ%2F1EUO3kbfqDmu9UeETzmj0OCQRPr01l0BPjy%2BMaDvwvCu6sscZEd%2FbLeO2wgw2Omv6ODUpPdVftVZ2se9fwUtZegA8oGF9aCiQHeXgzMLrABUBwms8ghIj2S1MSNbX9TmFHRHgrdG&X-Amz-Signature=fd8b80461dbeab79505f22c9b6d0bb5adcf39dbfe3ee6fad57a4c56e30ecfdfe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E25EI4L%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICt74mDXzfjRXkhtT9WoLUcHhrzkaSGLiDRB%2B4zS73JgAiEAsApsqX%2FmNFUzIcYoOdbRRoc4U5EdZk0HKyKt8ngoETQqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG8Q70OyaHELq9CXmyrcA%2B0Tc6mhbf9QpTBJv6nrTmJ39gt7r8%2B9X7IqPBFWpQeO7icyPTT2X1ThjXuVQDJNswNvS1z4Yiw6NoF6uOfc%2BAoumK%2BUzi9tBghgidMBYz0zkLmbMYczLMhwlnSLYGukWA2uVGdb5yDIfBm85KXFo2WviharGMyq%2Fe1%2BzADMhsvYggUzNV5oEOvmi%2Fc8OjE%2FqAOeN2hzprHjyplIiZyhy%2FJfpu4HU3Ap6qO%2BWKAgu3tAyrx63Az4UTMF5kq4XiOhEKMDJYqyHGHhYcWk9iA4EUu4Uj2HtinpUPhAaNFDJs3IEI1GdXMoEBkQxrIQXLAu1YeN6%2FSkcJNGNzCHS9NjCUQeb8B9rNqZvhZC1sK3IvgJznT0qDubGS8x4qeasDw9TctXd9ClYDjhn3mgo%2FbZoDiEBRjL6x%2BxX5tNC0EfPb0hYBuh49CS8ZA4mU%2F48l7DsVgVpo3ELJ9sbyO9oWPJCdnAAJpPZl3jPsMdC0Dz2xQxi5hGvngwRF1Yu45lhCikmgH0DDZ%2BFoiGPRqpFFy6n7T0fu6ptsig8MIqDlU3n23ikhNWdNJcRlYJpx3jZr4PEGDwI0hfDLXfOX13tC2uhLKzOjkg1s3tpeaNwBku%2FffZAhd0Ae1PwhJFID6DMKuU9bwGOqUBCW0XmBLloHZzFfLb4U1RFBC8NwPFLiyzWbvnBSeFqhsfww6wml9jQ8MVouJb8aS899Vzp%2BB%2B8%2FdIvW15Wc%2B5wNiTNltTiseX7ACb2yZ2dSVSUABRj006kXHWfSiRnbLQIXbwEld8Ow7cfpcpI9huepqSkZmSX7u%2FGAwFuchwkMds8ddNVcilK5V227%2FaJvfMmwJLYVpU6k6XjCHL4Mj0UZgf9bjT&X-Amz-Signature=1f0b257f7b424ad4c37af7b56097909f0895054ae0c7fe514265c9b2bc312229&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRCFTC3D%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG5hm3ACKOj26a%2F0srx4miq12tcMtfa%2BBrwVFgExu2jzAiEAxvqrdfODP54%2BFdng2U6jQkflpI87407zXa%2FyjFk83NEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGPoc9OsOkTN5H13aircA6%2FciokP9F%2FRnf1evmbGZtbJih6uxZT4vBz3TPfiqZTCbqu8a4LLLEOoKCWyBF1U4eMgd3%2BKnMVicjS2Jx%2BH6SkkVSTUftOPjIxlGH5e5wStlfPvCIWSmwteO5VtHr6amTGbWdgUeCgABP3zKCcXdcsptsQs4DVt7FVdRp4UKJOFTpVF4j2lA8lo3RgtcLciXCtR2LDz0KPzOeFyXTaT%2BA5Lc6oSoR78deJfXufmAN2a2iHC54vo38sX2xVAx1gjJCrXGuR2JNBmIpmHWp%2Bkgnu83oZwWVjVOn9Jdce7h12I6BtyDbE3Hg1Irn8iHl2puGOauW6dbIOI9DdZn5SEFJdXM%2FHglVnHCflG9xk7G%2FycCy08uOtyCuH0WSQ6bJfeE2eq2HQLenSneJ5ga3hKqxh874yQKzD8jzJST%2Faf7ACwmHOxXM%2FcUg2QDiAfppBwIvvWLOzmkGEUeeKNgMpnhjCCxNVAFGJBjQXJr7J20Is4a6soAUXo%2Fv4LGfWzUAusbQ4DqgX4vOP8bxqQ7OphB3k%2BjIdgKfTqlEafA6a7bus9LL1pIGdpopd2NYODqmZN0u2SmJEBgjuYGgryQ9HVGLOIrZrNe5dYfuqWyiKlEUGZmjIJV%2BXKg%2FWwHY6MMIP49LwGOqUByn57S28tAe4%2BNUnSZ%2FRloqmyMDtDT201JF8%2FDep0HFEBh20eWZ3aua4Luc%2BYTZmYltgZnK9VVjN4Aizhq9%2BjeaD0w590%2Bkb%2FiFO8mNOt4VdQDJCKbSQrSbNft1yNU1tf340fD6Ip0l%2BuK3ISUUwUf3MwnsncxKqaK2%2FTpaDpDmHjNl7XcEMFRW8JqZVliB%2FQyJtaOEYHcvZey2fbFZpPLGB%2BBCHI&X-Amz-Signature=72f5922d82c33739663edc8ef4e289b34d3f7ddf341b823ff31262509d29e03b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L4FZ4MX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBtXkqUJw%2B7JS111j1ISDvh6gPBZXquQ6LYUNVpR69NCAiA%2Fp7Hwch3y9SzRLeDqSlkiS8IqloFm80ZOluEAaEjitSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMifmdYIKjOxEfPs6BKtwDPPzCu9KrZxK9G4SMMYppNQvlHcCafkDgQbZ5iwAmGDUIEnwRLfwRWgMKpd0j1C82RxASJ%2FuEG4YEI0T4Zp9tbl8gK%2BwAATvcPNaQ2%2FvePZLjgz0%2FN%2BXgRRP60UzdiFt0ytjnGz9f%2BLspjYWgVY3SE%2FXzkgjZt9PbSXwKKCRALtM%2F5YktSLIVYEBEqmR57rvj6vIJUjL8DudJ6Savni5qL7wJiSd9y9GVb9e50KBi06PYGADMHvovv3Vl1d46r7oS8SIbv8ai0P6HqYqX5vjdVpy1phrEDFNtIF24jxQLnnx%2B4ItvqIity5YVxzRuNWJdVkMtW4RtjYcEtLMzeA3uDBx4%2B6qewPA4TYuaOpadTbqDkDGBs2DcZeSlAn2spw7XfeJ4sMfgrtmzpv9RIeuDzZBNbfXP451j0NfTNL6IojMJ7ZbEbKdMze7xUaGrACbdnS8VUbIkRAtCM3MV%2F97R143tb64Po%2F%2FezjrCPjTiVNm7DKPBRWQDiFuEMe4Zug7xZTi7kGD%2FkKkAxiLumzDNWsIBjKYcTiVT%2FTPpk6qCfnx%2FK8NUcVHlL%2BsBDnGrePvDQMCw1NXI3UmvHODgCkyox5JTS5KfC%2FOV56TTj8t5Y4j6P9ubRD2x%2FG9zpsMw0pP1vAY6pgF6xEpxH9hqnA2Hlfn5E2qVSeFQ8iCU3DfyigmVCETrGO1%2B6YJdbyUOKT7wtVPprGhv2QUbp7ZC5rZTvJ3tdPGCWRz2D%2FKaF%2FzfqXE7fNa9eF%2BL4Ao5UIUrvsnasp%2BWfrF5S7X8ErWFN4DnjPXBIwJucbQx7fTtuFljdOH%2FmouAV122grEVaCSrH4sCRU3r%2BXp%2B1aYuMSaJdjwXUXr1r%2BbD4z7Vj0Sd&X-Amz-Signature=65c415f3535f2962ac5cb28e80a9f5007cc01c7d48d40af06937ed2442f812ce&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJ3YUX6W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKMlNIm3tn1ArfZs5zG%2Fx2wGBaSDyZph1pYPECGEvSwwIgO90TeVEBJhAFdnusxGTW%2BevOpjS%2Fqpw4ZB6hEuyUEWMqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7MM3PU8RF80yb7iSrcA%2Faeukq7SKdMp9QvqX79AkugU5lnwAEvnKnDu9vZmxJTDAkd71FmHN%2FPqst1Q%2BmTu1LAqiYQLEdg0chzLOUNKCkvh9gHdOQhdOzC0mX0S1RxnnWpheRIdp3RQn65SXUGhRpGekaKPQkcadhKYMiPM4zm4u42vDmfrieaVpVv96tuPQtvPyHfVEgGERA5tiW8wX9bK6Kqr4072iTsOUElOfcAM52IEHZDFJpH1L8rJRC6VcjbbrjD84Z6LWAm%2B8y9%2BcHUcN5PB5pF3EqL5doKFp1f6C6FsvDDwkoGite%2BIxAsylHrKjU0muMUvWbm7Nj0zTYqYF%2BtvZEwas9BrowKi3f0nlSnrRTTtkrSa6mNjrims5i5tCULgaZoysxcD5sINWsZg40%2BjtdokFNTkEqGiJt16M2QnkuRZWmeHrTIhcnwNZ8MAXiSu8CjjdmlXEyxCEg5YZdWdeOVqlFAOEoHi7hYVm0Rcgomy0eWjMIttvxsWpC5rvyXZX1HTPOcOSuEMFL%2FOEdqjE9%2FSEtnwIDtlLnFdDpXJTiAcuEs8jcDuhA2y3cCjEcmLGmTBtWrmO5e99Mw%2Bgn4spp5RlRxua%2BDt4H5tOOEE9QoPgMnv2gvu5w7BkFDkp4EkZBKb6sJMMGU9bwGOqUBwOfTgctGhH%2FO%2BxiJIyBEzJebOTIHW7qOniBqTfulIRmcBz7NQOMQooH8tkJ8HAAR9DrIavppmBE9Xn1BnxjZ8Fw48149u9sJ5m0%2FjPKLrbiRC8aJ%2FqBRfquCUhH%2FNGJRVzPZUr0aR52iDY0z6%2BD9s4z1KbCgDu7XmBBH7DP3uX9X1eqipevUylkGbksO4OYAjVhkdX%2BKGZenIHlVGhkxyR5p3gsO&X-Amz-Signature=efea4f435dfe7e8cb9fa70e407512c919c50e2cb6c3e11974677fdc204401b8b&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S76KB52S%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE2UhLF8HtrnZwoWMIp1bPAInI5mYdM7gYzcZPEY3BknAiEA5p828hGrkbAROwuGWVvJ%2FpoiA%2F%2BBatKQMtqDpjL0qL0qiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHHmcWz5ercdTkmzGyrcAxccKfz3E%2BjBqSLIcoMsubhzq2ReMAEjYw6m3W3Q4T2qHNxbky31ICFQAfpKgzbjtfG7rmZMlJ1Zq3X9804Ype8Ce8Ia4xLLoKbjrVv4rR%2BxSn9xdX%2FeMvWdEjQo%2FbNlq7rGDeL8ofgFZBGIAqYsE9UxJrF8vaaFYrnWyLPJnP5QRKp48ss3ayarERkNeQ0QWFWOpRb4OTjwD155PAKOaFfqehmPl0gVddmhTten9W%2F7s9kLuFn6zN1emMTVao%2BgfZ1mf2mbhp%2FtoPx7WvKLVpAI7VFW3RBCJaRdxiN2HbPSMg1epkJjI6UNyWvNbE3QFzYrPnBd8MQyYqQPvHXc05Vghy8CRom0w%2BLUR%2FuGRM0OB7lYirDQfsDtihZV2fNwgg9JrPWBY3bFHJmYtf7qr6kgrbBTXvwcJIo8UmuqyZAEQxkYSBX07KeO82g9zVoZLc5hmTOnUST4yjDkzVt%2B9iysqv%2Bg6NC8g%2FzA0vVNcz7J4%2FfQHSm2yEXp5WPUVhyAezcFZEnfu%2Fcnr83C66rPjuU4JoAe6DnMYJ64gsRZcjJdFh4XFpy9TbX6vLiJaQioPF6Zgt8ZddyLJGQxcEfwPvtlmJCqzksVP8ANJK%2Fq3YzFJJ3UO1FIKsjUx%2BbSMJWU9bwGOqUBqP4abG7dGRwOsemh2ndBV2F%2BWpkDFXI0eVss9pk40K1saISwiVhTOHSghfg3njFDErnOO7ZXKlrCN1a08Shv6iwU89caGji7ocIIonH4k6df7dqy4mdBZbbVIS1fw0xxITvnoBLiFD7Aq7c81xCfrQMzlnYKd3ykQSt8IXt1FdvccY55WyaRKID4vCut7pE7b3IQw%2BSk2ZLZIWlqsBn22pZSb%2B0W&X-Amz-Signature=14c4c5d680d794e63d63fcee5a1cc6b3d60cd84cfebfe046a6e97f1489ca5239&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRCFTC3D%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG5hm3ACKOj26a%2F0srx4miq12tcMtfa%2BBrwVFgExu2jzAiEAxvqrdfODP54%2BFdng2U6jQkflpI87407zXa%2FyjFk83NEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGPoc9OsOkTN5H13aircA6%2FciokP9F%2FRnf1evmbGZtbJih6uxZT4vBz3TPfiqZTCbqu8a4LLLEOoKCWyBF1U4eMgd3%2BKnMVicjS2Jx%2BH6SkkVSTUftOPjIxlGH5e5wStlfPvCIWSmwteO5VtHr6amTGbWdgUeCgABP3zKCcXdcsptsQs4DVt7FVdRp4UKJOFTpVF4j2lA8lo3RgtcLciXCtR2LDz0KPzOeFyXTaT%2BA5Lc6oSoR78deJfXufmAN2a2iHC54vo38sX2xVAx1gjJCrXGuR2JNBmIpmHWp%2Bkgnu83oZwWVjVOn9Jdce7h12I6BtyDbE3Hg1Irn8iHl2puGOauW6dbIOI9DdZn5SEFJdXM%2FHglVnHCflG9xk7G%2FycCy08uOtyCuH0WSQ6bJfeE2eq2HQLenSneJ5ga3hKqxh874yQKzD8jzJST%2Faf7ACwmHOxXM%2FcUg2QDiAfppBwIvvWLOzmkGEUeeKNgMpnhjCCxNVAFGJBjQXJr7J20Is4a6soAUXo%2Fv4LGfWzUAusbQ4DqgX4vOP8bxqQ7OphB3k%2BjIdgKfTqlEafA6a7bus9LL1pIGdpopd2NYODqmZN0u2SmJEBgjuYGgryQ9HVGLOIrZrNe5dYfuqWyiKlEUGZmjIJV%2BXKg%2FWwHY6MMIP49LwGOqUByn57S28tAe4%2BNUnSZ%2FRloqmyMDtDT201JF8%2FDep0HFEBh20eWZ3aua4Luc%2BYTZmYltgZnK9VVjN4Aizhq9%2BjeaD0w590%2Bkb%2FiFO8mNOt4VdQDJCKbSQrSbNft1yNU1tf340fD6Ip0l%2BuK3ISUUwUf3MwnsncxKqaK2%2FTpaDpDmHjNl7XcEMFRW8JqZVliB%2FQyJtaOEYHcvZey2fbFZpPLGB%2BBCHI&X-Amz-Signature=49b2a2fc5c11054c123104e20e58b03e2565992161d96aafe37df79b2d250a1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6XYLJAS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGzL1sCQz4%2F50RaDxg0pbIzzuXzBksVFTSwqxAFZNsWRAiEA7SQcaW1STnTFdGpHhEIh8P72RkalHBMcGdo8QUKVbkkqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBigSMOjq7zL628mQyrcA4DIrg%2Fmnamk2LvFuEaQcdb8cl83Mydwek4RnTWJvnWRcoY7qYQdyPm9EKbAi5yRdOllYa0Vw25ahjShKAJB9Qr2EKa6KAL6KNw0QR9%2FY3pjK18cwLSBTU6eQaMg9nhN1rcq0S49GswMD1OMUZvfeXYUF8Y%2FCCH03%2Btx5WbKTdkyNeuAAw55lsOzW5SOqOH5ascArlxRaUUVP9lnQLqhp6QfqMBfC6vYsfPlTSGnv%2BCyOtuj%2Fq3KwW8lmRzu2iw1aiY65OoTy2vdHIkbJ5lLywqAijUHvBtH52DCy2sWbsXwX9L1JWHFaOtmCeunBqRH59AS3r%2BBivzUC0f3Uo7XN6tFeRm%2Bbpa2%2BqwT9W%2FW6crvWoV1OKXyfWCGzS1yd3AxkLd3f3imQ5nVsC3HlwLdwVCzTqaD3xV4V1WDSkfBiV4I6E%2Bde7pPyMOfHwGimhixg1GsRtcSr1f9S9mzN3h%2FIuyCd1ZpmZgxDKd8DJ0VPs%2BdZvLTbBzRPOFyMTVKhJszRz44G1qsvVtW7pIJUs7LBnRLSyA%2B0lBImUqU6fJOJkFZH327TXRa37w1EMlylpcYmphX4fsk9ZcGRJcJZB2rMyOfltgIF6RMjt7kCEIXoyj%2B4MM29Ys0uUjlsRWmML%2BU9bwGOqUBPDjeTO9yqVQjNqHZdI2ENXPTH616dF%2Fsbrzk31XqfqVHx%2BJ67VL7OdUeyTEbrnEn5S%2F0gRv44B%2Fu8hYVokCamqxcDmSC3PIHKDzaOJj%2Bjk3WYQSBJ3v7JlZrFBTUnmm6Y12Nw5Bva%2BI6KkU%2BLomElyJNAq8hi0PO%2Be0JUDO3TOXtM8gQzuhtPhDu%2BfX97xQiWOT%2BKomZmKIpL261SBOeGMQXdJmV&X-Amz-Signature=acd0c91460d3c2a4cae29ff09e856206676c1be359d4e65ac179a29d4aced3b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6XYLJAS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGzL1sCQz4%2F50RaDxg0pbIzzuXzBksVFTSwqxAFZNsWRAiEA7SQcaW1STnTFdGpHhEIh8P72RkalHBMcGdo8QUKVbkkqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBigSMOjq7zL628mQyrcA4DIrg%2Fmnamk2LvFuEaQcdb8cl83Mydwek4RnTWJvnWRcoY7qYQdyPm9EKbAi5yRdOllYa0Vw25ahjShKAJB9Qr2EKa6KAL6KNw0QR9%2FY3pjK18cwLSBTU6eQaMg9nhN1rcq0S49GswMD1OMUZvfeXYUF8Y%2FCCH03%2Btx5WbKTdkyNeuAAw55lsOzW5SOqOH5ascArlxRaUUVP9lnQLqhp6QfqMBfC6vYsfPlTSGnv%2BCyOtuj%2Fq3KwW8lmRzu2iw1aiY65OoTy2vdHIkbJ5lLywqAijUHvBtH52DCy2sWbsXwX9L1JWHFaOtmCeunBqRH59AS3r%2BBivzUC0f3Uo7XN6tFeRm%2Bbpa2%2BqwT9W%2FW6crvWoV1OKXyfWCGzS1yd3AxkLd3f3imQ5nVsC3HlwLdwVCzTqaD3xV4V1WDSkfBiV4I6E%2Bde7pPyMOfHwGimhixg1GsRtcSr1f9S9mzN3h%2FIuyCd1ZpmZgxDKd8DJ0VPs%2BdZvLTbBzRPOFyMTVKhJszRz44G1qsvVtW7pIJUs7LBnRLSyA%2B0lBImUqU6fJOJkFZH327TXRa37w1EMlylpcYmphX4fsk9ZcGRJcJZB2rMyOfltgIF6RMjt7kCEIXoyj%2B4MM29Ys0uUjlsRWmML%2BU9bwGOqUBPDjeTO9yqVQjNqHZdI2ENXPTH616dF%2Fsbrzk31XqfqVHx%2BJ67VL7OdUeyTEbrnEn5S%2F0gRv44B%2Fu8hYVokCamqxcDmSC3PIHKDzaOJj%2Bjk3WYQSBJ3v7JlZrFBTUnmm6Y12Nw5Bva%2BI6KkU%2BLomElyJNAq8hi0PO%2Be0JUDO3TOXtM8gQzuhtPhDu%2BfX97xQiWOT%2BKomZmKIpL261SBOeGMQXdJmV&X-Amz-Signature=b634ef52b2240ac431710c5c5e66305022a8578d81362d80de36f259707c677d&X-Amz-SignedHeaders=host&x-id=GetObject)
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