

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJIPYNEX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDas4sXnvU3X0rEPAT%2FIlbBE9GA2ICKnfEjvMbhCfMzoAiAwvYkpvLOjFFDxUr1mQUvxA8%2FzQSs87DCzhDeze9bbIyqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhmHn%2FCEBq7tSdxGdKtwDTkDQ7ctqTu1iyTzoga%2FddUpDi6f9cDXC53E2dBr0RQ0nYfz5%2F4gUYVSY8TGXAVN8XO2SfQt4BcqyrjgAXcfe7RpKa%2BSjabPvUeuspE2yoJXr9P1lFek1z0uzdgOEhVWYDVoXUaj6vF%2FIDEp2oKxc9V0xdcDvHj5b7d4EL0VTx80fAxIq9I7%2FGufLbYaT3%2BkPMnT0C9tyCjHCFOB09cTNcgvc0r73wCu%2F%2BfdOmmZoj4HT4TY2Vm5QJTD1SnnUbzBqXNEgxh49WXW5ep9vtqgP3yo8pGIlGt39yUkyYGhEzZQk85%2BSOqtujwqrSHn4lfXKkMEt%2FtjweALMNxWc3qbcFcnYhw3%2BPoZOWmAPIwWEhN96Wg6tgaxb3fCVr%2FFCF4oDnxcliiQp%2F5TmU9xW9DCk077nEKajT8hkx%2BA%2BjnaZX798ol8c6LJ7woHyvFILE2TFHIY3Yu9ytxZDssKE2Fn3OXnkLHT4yUQTHBuf5gNlCRF1l907pcchvWvqSkYHImr2wPMjQwzzGs97XPteO5uCLlXpk9GCimx1y3FAX1BBtO0MFVq0zpVE2IQmfLmddAH8dBKpC%2BSgfpbtBybrJXfGHV8zJlUQ%2BTx4CopcUJcig3LrcCV7a79N%2F6tgE0Mw1rqBvQY6pgHsSlkmXS2AHjrnNlLvpCGurdtqOX6Kl3%2Fk6AT7irdEgr6JCkHy1WXPm%2BiRZqwMQw1YzhBGzSKk7sU%2BJDZrFM4iWWto4RfLHbzNWS0A3Krb%2Fe8nZHUAd7Co237Gi4Yh1Zwjusm6l4cIlHreSyGq6t896jSGRxidVTds6OG2T0jFaCbfULbgE%2FQW4J9XgElh8MAB5zTXqqtC1M70K1krWAv%2FG0W5IEVk&X-Amz-Signature=f761542383f8aa251fbeeb0135893c81cfd3d4690abf279b44cc73eff9b14f91&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJLRDLCJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgqGf9sJLuqp5VHBJYHTv4frwukZOSYo3SREaFy9ES3QIhAJNAKUfUlg09VPPkq11kL6rVH7QegbYo%2BcMH8F2iMHYOKogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwO%2FVdccHZS%2Fp1AX5gq3APVY0hZcDUJOC22YJgwkMk%2FdQ9ygcK9f15lGlSF3fivBfSuF44OCtmeHeDYLdnVY%2BRCWLY5zgXdyCV83xNd2JgWkmCCpIL4e%2FYGHNL3IBR8Z6LMZ0uMp1DN9ywkjQP0gUDO8e49yddHKmGalGgReUCAitpNUuTkYNgpMiaWfHh1SpHGrmJFDVfGBUGjPZRRWvKcB%2BxdBaXhag04Jesmw06rdJDZCh3F8Q3QX5y%2BNJSWzIW6d15%2BbDvaTK%2F9L3SJUliv2nYYe8rg1TL%2Frzgui0i9vqfIqwLLF5Zemw0MSypTCjnon04OB6h0HSwZXw5%2B%2BLHPxmpL9iDCzSzX%2BQBlbGzM01ZltBDBAdAoxeu8ULrq9ivKu0Q2p3TQswefuh9G%2FS24%2B6sGeG3Fv%2FPBPGrepu6374ytQjp7v0nP%2B2fnvfBAP8AgZAvbd4OMXoxbBk0DDWVwbohJXkNOPuHbcjFlJ8n5OqJ6sx6gut3QUm4qWmPup5qsicpBHrQF6LXzpzlmBIdEc6yrVb4X8%2FF8urhbDy6RXZL6C3R1l7AXofIFXZuJLXr%2F%2BLM4pXUO2OXuhAUVobN25UBSLrBlH4cwi7I2xxyXEDDlQhHNlJkv1o54ut6CSnsTbE0BM3RdJp0wlTDduYG9BjqkAQbvUoIr0wrm%2FNA4QCz5fj%2FiSRkGiXWzqSgJaCdBsCdkxuHQwL1yDZvXKd%2Br%2BG0wuMAGfFnf24zwt07HZV2DuYOsM0usNB%2F%2BhHHGQuPu23ZyD%2Foc0YIKXRU5sdLZiKDSn0CTqj8hGy5UPrWEHRMnNiV0U8xAS2e0uZQj6lZFNUVmw7fk3iOnr%2FvNpEX65Choi2lZBd9e8UUWiTqgjxo16u1kZgnO&X-Amz-Signature=7f00eb2f4d440968513372fcb822a1995c2719e73a1eaff144b0572a8ef42f76&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKPUL5EV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqLHL9kH7b4rC53O2Sxev3ymzQlnuhlJI89%2FZG2LDZjgIhAK0SwRTN3ePInKRfHXkIDHKDx9RCQguI7fAchpuM6I0IKogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxBITn2Zi4mJKtsugq3ANcbIYTR6WojI2z0KqJZhrhQwOg6Ud80BH1SVFWGURDnF4jrZr2cjWCoNjRWrEYVGhrLmNn%2Bwft%2Feyiu1YRYuEJuTSqmILiqQBHXJ5B%2FfydVtgHLlzx8y8Bjtr4ERBDZROs%2FqJfOMTZKU24w09ntjYeZAfZehwHLHRRws42ys0ead%2BJihVV8HCiCqIx1HjdNIjEmTMrphhJZKjOU8Mobc1sIav7z4uhxjJ7mJInCJwPy7LxpGeBKUh%2BfY%2BO15lGRJT7wxN59p4gM6xI8nbcAocjsHeQuPXAGlKG1jLuRmJDPn1pLmGkGlG7NWbwri000GJatHxE8mkMzoXZGNgIGCuC%2Fui0myRj%2BJsxTyjGnNiVvDhAngTU8injtJvJKXshwSWCoaMmjx72QymzamBHl4RfVGZOHw0pxIpZGYqg000y5p7H0r%2FoUzjbfC05JHxvOlExplIR5DHWkij7Z9fKwaLinLYifjsgqBJEWQV0klBh4CD9pYRfwkeD9qx9h7DKk4lZSYtIGWGYwa7C7pQnF8aAb5cNNNxDB3SOloUAwlDhIqAXHwIO%2FXuc4W%2B%2BcY234rvHhVkQykl3fijqQqK7JIs%2FAnwmV6iVIYzYRm5qQpSnYeyypVrnIX76KjDaxjCSuoG9BjqkAfshgH2j02blBZsefdzBvr9Ho0nY0J93SuI1hta8cpXfDWNbDQ2EDG2xv7bJn7m0Sl6WpYPxNfXUuUvfOyZKGakPbgMYFuYNNB3v%2BwDb4u%2FbjeaReOrL2g5JAIt4oux6aC%2FPjg6z2tCkm%2BHKD9yjS1m8leTJX%2BoPi%2FXUUBmFDqyf%2FDeHxhUhOFduT2GHCfTbB0FKH6XcO5GseJPr0fjddlXDuBx0&X-Amz-Signature=89161c631444cc1b862c559ffda4f11e627b373a7e38519ee28201bfb5afb92b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BRK4JHK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICE1AGAgQ478WZ7X7ljIhLFCIHT%2FyrEzIbZTqkWavuC9AiEApfkjZZiDVF%2BJ%2FT86cWaj8Ne4s21%2FdkFfzKSHxrV5RlMqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIIJvbEZz6xn2V7yqCrcA6uaVVvTVQbdNCimz4E4Yl%2FnjbQe1fCa%2FDzvp5dj2G0ie6D%2BKlFJymOunBjfNcK9WeC1Vlt205fo55wzvIO9uZ%2FQCppJ6RDZINzMGHb9eDG%2Fan6vtUkPBrG6JVj8SlQcrPDZL9SOXW9vMy5Z2daiQy47XUZT3T2JT60OR1EmffF0uYOitoV5zHP78nHRRTaKa%2F0%2F6cQq%2FlSBnNRe4JYWPWe%2FOJuNuyvAnoOdPraRQLZWpNaNpbpFtYNKq%2B5AgzEHuNdho%2F8HA7bqyG7wR3k5g10aIBM4Eo83jCjdg1dAYrusbcNhxYj6KR8MZXtHejOUD71f9sIUkH52tW%2BxWTY3Z1byA2cvOWvtkMnZVjjjIZJ9mzf6JpxEj1DSKrOOFRGt5Lpudcvaoa6dUXt%2FdnhVtocJyRdHW7zhdQnp0PHIzOVfs4eJlAhJpByFMG10gVaODX5oFYryM6oIp%2FSzKAbIWLE4Q8MTgmvA7q2yWxcHcZdHX3LcUtFC4dPtIyZiKPUnHiupcx3qSTQg71%2FOxr2iQfDmjaLHn8g1asUCFyh2ajmJyx3Tt4O%2BwA5FxlyenyhN5GE1mW%2FnMVWS%2FuitFEn2rXFVHKo1Pag9BMn8p%2FLEiQecHuGsD1Jp0p2GXWCbMJW6gb0GOqUBx1hw%2BLKbcWrPZxUBtt2OZDEVuFyibNbigo6LFCP8td%2B5koB17DLkpyKGGRPLorI7Vew5Oa9NnYJS9oV0ivVmbcdXn5kNx49OJ%2BNR9QksRi7QLhEi%2Fok7utjhSfYAl5g30KN5y%2F%2FiAw6AEyKIRQy21EEh59gkfPKSvxoXRKC5N7qafcNoXelKfVOfq%2FPy9KcFCg3jQtF2hr1HuMPYbD%2BlmQxjIfRv&X-Amz-Signature=d54172309616166c37102bab54ffc33d86af944ccddf2a5fff787a006feb673b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCV3XPEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDlzhcI0dT2GSYUB%2FsfrwFjPOp7d0NgQ9e62AA57wqAwAiEAh%2Bp%2B0gvHd8zxyK8mPXnVMEYua%2FjRB%2BNwG9RRaZ5GZmQqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDl3VIcRf2svqn6bBCrcA0PFmYmMidl%2F%2FPgxOUyPpUZAqh7V%2F2bpb8wZ%2F7%2F1CjBSNOedRi3Nc4H%2BEq2TxxQNnv1WYYZKLaBOUbIHt9uG74FFx5MKh1zDnnI2TKas1VbDXSReyasQzvvxAU1VazhnH3ppbS4n8b093mrzQHUVfrXY1Lda3GAmaLjj%2Bw2EqhW80bIy%2BNi%2FrGaQbRnbYXCjUBrd6vUyjzHBpb5Fl8mgPEE7nWVm29JdALDjBuc0A4ZmEEaf5i%2FOOEsKCqbjwv5JG8pE2RrmF7Hd7iv0y%2FyB%2F51QiAZiY9%2FxgMWrWzWwQVW3OFY2xGMolhIUtq35Dp%2FytJpnRrG9qIXs4wYxNC8C7IG%2FgFRFDEQ7lxXgoqdoVvJIf0eVthLP3cXhQobA0aK4CTOvGV%2FMudfT30fy9PNQymUwcZ6tDy9RutCkNdOV5bc%2B%2BBFMYeo8YLLOuPNEOdr39SsqdMDO33VW1usc3xcQfNe5Zh7Ct8zom8DibiH23BXozU2vE6qEQOP3VbTcJXv3P%2BmTuXO006B01skB4%2BAxGnFC5sdtXZlM5%2Bd%2F4AZzpLJjwvO0FmKCGnD7hkibnpPvL7fsE944LxHfhCh4GSLBp%2ByNqH%2Bejmp3Ep2rqFuSapBKXHPC8YebmmnSszzWMLe6gb0GOqUBjyfJ0dfzyIjSO5L%2BmauvG4Rvx7IDGonyv208X2dqhRJcEksK06g0YmvSkSdP6tY2sUxa0bK6Dpl%2BFH%2FjrfsRpQjcl0SfgTonLdAvMhM0jpuNn2MQSgAuCbCKGSCLSaQxGKnx3XeWME%2BFuBLn5yPiA23osSxjmKbC4bAM%2FC2iydBpxhns%2FYXHTjbA25cfOsBq3CxuycytAS6KM7Hmd3j31pRYu6d0&X-Amz-Signature=154d9935e990dac0c4ed21fbeeaaaeaf71f37a5457e3f30eb7c6d68ac9f289b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4H2KRUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BI6qTmnlBs%2BxTv83LWOipfpwrH%2BuGbToBzpX27AdJAAiBU89NOLN%2F9AkyYv6vm1QuheAmbzXZY28c6I1OSdV1%2BwCqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAik29pzutaZkHAhAKtwD5encI2GJ6y%2BcMcJXPSx%2F69lbycL7wsXZLjZ%2FjYhIUSO%2BRkee8%2FzvapxojAOtEa15yrgfTmkkNVbSb1grtDmEAWv07Bkp%2BMOO66DQ3bBDqaHpO9GMEJOFwb6hL4RlPx00Cfy70qnjpTbcGcqeeEBTNIxraAiKJZsUFFgwfLxdXed%2FAQqAnqclSwZ8mCVCb4RxWQwq4bijsIxzpzmGOam8GhkEt0b9%2B8sZwGI5I2ujtQHrEAghci2fcBM5%2BKM6N%2Fvfa5HICrd8CLDysiXqtD8yipgV8TzTop4BOJA0kEkugEGCNpeg5nQA4eiqm%2FaLD%2BFE3NTKtsF5hMYvIOju8WU1kTGA0cw3JuAWX5c4sdNPhX1wck%2FYm5O9n2xcS5u7IZN0W%2FD5cGB6iwoJmJ4Q3HKcQslXZNBkdZ2RHApLqLkODWCas3%2Fp6K9posCrE9Sw8NcZLURV4%2BdVMyCK1L2HOIjroMC51ZpBkHCprygspc9DXmgrObNdfzimXq4pdETXsEBmRggA6OoaN0awFnZLScQu%2B%2F6x0LBoWVwHi4t9eu8htDu%2BDIe1oTv8UprFWSiMHFdrqk4KpbqDPpQnMXdHc7G3doAMYTG%2Bb6B8fmBICE8U7t0%2FR5yFzmIW%2Ftvtujow6LmBvQY6pgF2fL9SFQzxOP2ULnmW15iZ2IPJWTHBDcQTgRnfr7oeaY2Nf9Y3ECJ%2FQUHyg0OA0ScVjIuETfFWZVg5F8pPlLtcg3J4iF91ECHLCkfclNHcb5IFgQgjmE%2BC02N6ofsADqam3IlTniOWllSRfkU0RS3d68k64CQ%2FtAKkeeyJRscV33GVmt96Gb4sPsaV%2FRweG71t46IKWLH5GlDFiQiHRWX4JerMvfC7&X-Amz-Signature=915ac453095b0d1914cf97713a235e1f7dc2ea22e0f43544429bf2c72769e58c&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REIUKAOB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFyirbG1dizSdZAPePIyP0C%2FT%2FceSBifRt%2FF1%2Bu5MRgwAiASAZ2JZSSQrejz3K2bjGIHWfO5wzRexJn%2B%2BvqYwcjlGSqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIcdA0de55flmRd58KtwDIBnLIkbTidAhuTZB2IQdNhkHr5wMifvXZA14y0s0LuOZJk0KDP0wl4mVQZRJ%2BFGyaSsU2v%2BdVDr7JRxH0P%2BPX3b4Rj3vkQRi3Z82I3zVo5e640SgdJL%2F5fp3LEEi5%2ByYqHKC2VhmMypW7ce3zgPa9k7gEemkeElIba5A64SBRBdQnwf%2FQ60%2Femm7SlZNFTrH8gFoXeeLSyGytKDNt9CnFSlNwSO5ytU7X1Q9MI8RVSkGbgMW2NBYnItneOpzuAV89uVKtkRE86TJouy%2BrdewLYnt901NE2991irapgrpJZnvpzQc1%2Bn%2F1nqB0pqJvIfTCubXFK70ySgih2xouY6Frai0H6%2BFCrChoz%2Bd6T3InoshwmOwjwawT9kZCTLOzFl25ZN96NFP6gC5XpiTMluUdwrTC8xdwCaZeBY8C1qz9LWxLNZfKpqGaJLGSSh47%2FVYMTMifdMHC6FPE95QxMNq8iH%2Br5GdTvyZMGmYHKoASRoNTAUapRpFZZBqI%2B0DxzWDDK3KLym9vh0jwEoxMvqot6AX8U1CgGXKigIOlmZ5uNqvTl9Wo9kjKgoUftuv5zKifuwEvK1xbAT3He3q5JBoplpRuXENfTuKWO%2F2e%2Fiq3YHgingXmkTZuKhWYTIwibqBvQY6pgHTJ7fqKx9BaOX1A5yXKe0VDh8E3Xa6ZPVRNqM2yjuhIwMLCZpIlsWcasxLk%2F%2Br0wM3p6Krt5mRfwloTxW1pGSJEKab8ZTPNMj7%2BDdFBEHbyRdxoic4sRYrkzc4USebTw0qfnqjAjfaWuysoLRx8GzWeGAqca0iDUEjkILQIUV%2FHyxys3kuDKUZHNOGtQT9MK3UtYsDvHKNFZE91QV3TYAYTeTOd0pm&X-Amz-Signature=32d39b6db011d8919f49f4b6d00d307ef86f794a9bc229022cbf8c34b41da62b&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NVFY2C4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBzZtMWlt0%2BULFmQz8Hfdv9jvMGNcUjCLKfvpxkKcwNZAiAu6unriALdskqDs3nrdT9bbZN6iB2GKWrAJ5bLFA2kCyqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMR6lJIiDhdfPVsLwaKtwDBuq9TyFhpt4XF5mFjspgT4CdHxfJcFzMJriiSEfdryvWcudiBjbBiROPepBfywRra4NCMxKfduuhqqj4HEHSUCiwkIPcnyTSDu6zY8bMB8LauyZ%2BdEz9XOYL43w3KWsojx1WFZnRGkxszY8Cb%2Fk1vuILDJanCAB9fDGnZVUNlY5D3EfKgE%2Fbf4o0HGyF8QTJIXtIl13nDMoOOTaqANI6J0EajeoHtxgCa9%2BzZ8i%2FB%2Fr2xeWJDBbtfTJE73hUK7n9vyq0%2BmnIWV9ERuERg05ZMMqtPqhC3SvudccCaZKcz%2B54CWM0CdwLfYJ0d%2FHqhq5hvEua2kjh4sGEkcTzWKzRBtsjcBUgP6ACJIVq1U7IhQooY8%2B3E4Msix6LQFLV5J%2FK%2B0%2BS4oMKWZkgHNhXwz0mL%2BtZ6Sgq8FuJpQ1DwYS4sXKfVW9HBMxZ2grZz9UA7h4oEI5aMtcDjpQD0reNrJdPnzSAro%2FkzO4YF3vDaa6xt8kQnTpiHoG2jDnQ0JM46LxdKSy95ZJFj9DIamTDfhwOGkxbciXaiwLoJBnvBr%2FxcXojzVfKzImKYaq7VpF9fmocm4AXCbzh0yDk0QXRpGzlld0yJuXQsuIlcw1ZibQkrXRU2Zu7ONpUJbgFPAcwsLqBvQY6pgGGTgSrn4Z4zinGPKV2rUEFVF4AMv9PLovvarXxTmx63MG11Q4jVcnDicMdkaWMOdMAwLu2n16VZIZC8ksjdJnut7oRDBkDRWcx854eY67f3JLWxyDAroVhfHAl5HXQTAUtESCbBC1eGt5m334dGg5tzNTmQD8KCSE9jkNqjOx2pbOnGYFpkpGj3z5NaPRko4bTQoe3xPPyftEGeuPOo0Ncx45b8xmp&X-Amz-Signature=6f3af204f3e8c0a2f32d046bdb0c2b45b44da44787414636d9401aece523d08c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCV3XPEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDlzhcI0dT2GSYUB%2FsfrwFjPOp7d0NgQ9e62AA57wqAwAiEAh%2Bp%2B0gvHd8zxyK8mPXnVMEYua%2FjRB%2BNwG9RRaZ5GZmQqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDl3VIcRf2svqn6bBCrcA0PFmYmMidl%2F%2FPgxOUyPpUZAqh7V%2F2bpb8wZ%2F7%2F1CjBSNOedRi3Nc4H%2BEq2TxxQNnv1WYYZKLaBOUbIHt9uG74FFx5MKh1zDnnI2TKas1VbDXSReyasQzvvxAU1VazhnH3ppbS4n8b093mrzQHUVfrXY1Lda3GAmaLjj%2Bw2EqhW80bIy%2BNi%2FrGaQbRnbYXCjUBrd6vUyjzHBpb5Fl8mgPEE7nWVm29JdALDjBuc0A4ZmEEaf5i%2FOOEsKCqbjwv5JG8pE2RrmF7Hd7iv0y%2FyB%2F51QiAZiY9%2FxgMWrWzWwQVW3OFY2xGMolhIUtq35Dp%2FytJpnRrG9qIXs4wYxNC8C7IG%2FgFRFDEQ7lxXgoqdoVvJIf0eVthLP3cXhQobA0aK4CTOvGV%2FMudfT30fy9PNQymUwcZ6tDy9RutCkNdOV5bc%2B%2BBFMYeo8YLLOuPNEOdr39SsqdMDO33VW1usc3xcQfNe5Zh7Ct8zom8DibiH23BXozU2vE6qEQOP3VbTcJXv3P%2BmTuXO006B01skB4%2BAxGnFC5sdtXZlM5%2Bd%2F4AZzpLJjwvO0FmKCGnD7hkibnpPvL7fsE944LxHfhCh4GSLBp%2ByNqH%2Bejmp3Ep2rqFuSapBKXHPC8YebmmnSszzWMLe6gb0GOqUBjyfJ0dfzyIjSO5L%2BmauvG4Rvx7IDGonyv208X2dqhRJcEksK06g0YmvSkSdP6tY2sUxa0bK6Dpl%2BFH%2FjrfsRpQjcl0SfgTonLdAvMhM0jpuNn2MQSgAuCbCKGSCLSaQxGKnx3XeWME%2BFuBLn5yPiA23osSxjmKbC4bAM%2FC2iydBpxhns%2FYXHTjbA25cfOsBq3CxuycytAS6KM7Hmd3j31pRYu6d0&X-Amz-Signature=9b5f347857a15debc66e68f466152a5db1e3c7c378fe997a9f3d9e49f74487b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMEIKTKE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDiZOUdBMe6Tq4K1irxkdKknyjPAdJxbulg6Aqn6GuBKAiBMzRtBZCaHB7lIfAwRlZvOu74uFHfWEyS3fuNmVtgI6iqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLeS5do%2Bxo5D45FJAKtwDrJzIJsUCaZcTnflcj8%2BHX%2BycieS3OJ08Ur3%2FNl2gFeAvuKrcFtfGxRs2XZg04xlGiP2VxcyA%2FLTnQuXQL7f5uev39ftZwKDn0ZeMbxBkydVqqBce8WRL%2BR626JGS4XQUKoCRjhB52geXdQZKXNQAilGQyoDbgLLe6nXdmgs2f2GAILKwPvKQuKrDuXUs13hQzzXKUFQBTN3YSOAmXkn3oADHhknhYPDNkTgr8RpkrrWU6rXRRqQ9Yxz28xogwh5bzDfGtYEJgF9A%2FRiTPonyXl%2FzbQAgl3m7yDt3LyD1nzQYbwVDHZZrTvRJla09bDAMNUQbtJ%2B1mMZGwB5ucW%2FTkNXfA%2FqAfseC1cvic9mI9SK4aExZXg2GfKYD%2BzJtZRBPtDBpzHuvc%2FqsJ5xhMzts4ded%2F5NtAH%2Foahuwmu7sAHMKcEnn5tZXMnnIDx3%2BoGsaRwWuulSKvmIE6VPKreBt3qN3BBMSsBVmCzaIXDw6tEhpKi39iNWrdPczb7P6wOMpNWF8cEyhXMqQGq%2BRe%2BIsmQ0w3PskAxRFWBr15xn%2FPFsQ%2BwvwcOFNIT4XHgiyqTeONrFaKnMM2R7MQ9bw9G%2FjREtijZTzwn82t9EiF4hOnseJnp7vpIuNAmzIyIQwhLqBvQY6pgGCDp8KDRgp4Jzhy9j7jPDwkTP8Kc1XW2O9d5gdZ5a%2BP9CjOXhL9huO92Ftqbrpp5hBWoJTcmqI5Y4jw1m1Sec%2Bf%2FVQrgtxyvKgnASXFaKAhNvw7jyfKqJM5pXYg6X3lw4rNvfZkaaMmGbBlTqwcmp7XM9GUROl%2FA%2FfEHFQ5xybm9MYHcuKaafMpW1T3zSkf8QLcTzRZt1je%2F8EGTJpZnT9kfaudULT&X-Amz-Signature=3b697c0e7a5391160fbbdc66532cf056e9456382762ec555a7db1ad7076c8cd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMEIKTKE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDiZOUdBMe6Tq4K1irxkdKknyjPAdJxbulg6Aqn6GuBKAiBMzRtBZCaHB7lIfAwRlZvOu74uFHfWEyS3fuNmVtgI6iqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLeS5do%2Bxo5D45FJAKtwDrJzIJsUCaZcTnflcj8%2BHX%2BycieS3OJ08Ur3%2FNl2gFeAvuKrcFtfGxRs2XZg04xlGiP2VxcyA%2FLTnQuXQL7f5uev39ftZwKDn0ZeMbxBkydVqqBce8WRL%2BR626JGS4XQUKoCRjhB52geXdQZKXNQAilGQyoDbgLLe6nXdmgs2f2GAILKwPvKQuKrDuXUs13hQzzXKUFQBTN3YSOAmXkn3oADHhknhYPDNkTgr8RpkrrWU6rXRRqQ9Yxz28xogwh5bzDfGtYEJgF9A%2FRiTPonyXl%2FzbQAgl3m7yDt3LyD1nzQYbwVDHZZrTvRJla09bDAMNUQbtJ%2B1mMZGwB5ucW%2FTkNXfA%2FqAfseC1cvic9mI9SK4aExZXg2GfKYD%2BzJtZRBPtDBpzHuvc%2FqsJ5xhMzts4ded%2F5NtAH%2Foahuwmu7sAHMKcEnn5tZXMnnIDx3%2BoGsaRwWuulSKvmIE6VPKreBt3qN3BBMSsBVmCzaIXDw6tEhpKi39iNWrdPczb7P6wOMpNWF8cEyhXMqQGq%2BRe%2BIsmQ0w3PskAxRFWBr15xn%2FPFsQ%2BwvwcOFNIT4XHgiyqTeONrFaKnMM2R7MQ9bw9G%2FjREtijZTzwn82t9EiF4hOnseJnp7vpIuNAmzIyIQwhLqBvQY6pgGCDp8KDRgp4Jzhy9j7jPDwkTP8Kc1XW2O9d5gdZ5a%2BP9CjOXhL9huO92Ftqbrpp5hBWoJTcmqI5Y4jw1m1Sec%2Bf%2FVQrgtxyvKgnASXFaKAhNvw7jyfKqJM5pXYg6X3lw4rNvfZkaaMmGbBlTqwcmp7XM9GUROl%2FA%2FfEHFQ5xybm9MYHcuKaafMpW1T3zSkf8QLcTzRZt1je%2F8EGTJpZnT9kfaudULT&X-Amz-Signature=ac4366b75372eab224d0636542691ff9190205f71de9ec9f25a9a94fe6cf0aac&X-Amz-SignedHeaders=host&x-id=GetObject)
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