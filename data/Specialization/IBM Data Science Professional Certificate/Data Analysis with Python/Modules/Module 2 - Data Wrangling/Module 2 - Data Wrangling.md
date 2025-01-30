

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LRRA37G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFpEjqcnGo0RavmojuGIHc%2FomH120WECVDq%2Fm%2BprqZpmAiEAp8zbK%2FmDojOfQp7eDD0foF4u6OmcgQycvIecbsrWx3cqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHsx0wJ7FmiYr%2F4pKSrcA%2BrcbX4iZ1FSzjwdw7hx6ROtlqcKSBtS4L14yvl49NrAXqqCEhnV00si8N31oM3cGidkoL6U0nnh3pMfcd5GEmBbToTatMBckLf97zBAHSym4iCXDMXOE6eNOnmzAZzrJJXmt%2BJUUgMFpI9RdaXrsORBoAaMJSzpb6KzwEiXfquTtA%2FXCaozKyqNTLzYt4YXuCtcMqhhiQyN3ZrOnF5BCjJKKpIEe9TZA4wBbepH6zoONjAFi4H8WhZjMq4q7ak7xShJsh4U0g5ZjqFH%2BCos1q5jdt7t0JTDMhTgYnewnYbAhMhvctiHDdOqznwkFPrwUDaQgG%2BAI1u27l2ZThGEB6SF94%2BzyAcKox5eANTSOwSe4KvDSdXUG9F5HIxoaC7w%2BnDqVGgitaJEBnco8JxFLk0323luDGteULXrJml0kPpWsoL0iweacWi0i6c3x1LNC8uFvbga3HzEzKLUDMPkgW6zPUqelnbIQMOUthOndFh7NDipLqc62pDbM7M4lnF15bUl%2BrHtnxqpIVOee7fVumXauSftpk5m1eAVXFUYiz8h9VMd5ScpWKMGZrKCoBC56CGadHk%2FJ9FC2kh3KPiPEm3QP5aqDQnC5u5lLF9oXPjoDE1lXf8CvS0%2BaoHiMI3f7bwGOqUBL%2F6JOtvME658QZ1u7tomX%2Fp1OMigML%2BwBNMOY3jbIp3rUSvh%2FkbaPhLEctNmJ7oJ78r1B%2FQN2%2BzpnVRzUIHeheuHwMY1G%2FfHcnRQZAhd5H3sPxGGRQkuRnt34DIZRboAL1C3140eOXl1N42C%2FnHF1Yw%2Fo%2B%2Bl8ZcrnN3HvrdYnbysDVe5FK%2B9r5SnpKHnk22KwSQAc3EAMFxI2DFP9GI7lbdfsg1Q&X-Amz-Signature=df1019a233ba7a4a6a1c040bab39b2578183ac7af0d7553071f037ee2abef96a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUWCZWX6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCg%2BPPYcjAVDQ8v791%2F2fYNBzuQOiMhnttjfMPodKSj2AIhALSYoaFgATUAdngKXr6tRpz4NuEj06OM8VLXQqpgJJ2jKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxSjWKAPQsyIwWVpcq3ANsUzkNVx8yxoVxU0i0zn%2BTntpecf8%2BN4xptk1LkDckfbD9Nf42Ril%2Fp7K8COdu8OLaU2ec8qLwAHASxvqDxL1WoTyPVdsUlw08CW40WzXKac9FHW9Tk2%2B3NnFADkchbsB%2BhoyCzGX3KX8XsTzuEe1olK0PiwiA7k4dDXGT1jx7qv0Iw2uv3HqGZfM%2FFu%2B9agf8e3FYQI0In%2B1liqhTCTQu9iUsENH%2FZUsnsi8PrXRvIcrRelakz3yDTPyt5xWottuygRsdNN2Ebh3NEmdYjhmO4Q17diCaC8HEyUX47YAHGjiexVUDmBFZ1EWiOQF1teLqYWBRyGEeDkRZyO6j%2BNI52m43ETEHS2CODzgS0Gq10Gm8diRUv7QUsW9F1y%2F0DUIGlkQzL5wzSbrsAH2avfOEk%2B8Rkq4aWqxo98Bfqjj7SLeQo7%2B8%2BGrn9hB2%2FDtofvPkeqQ6u4Y6im55QoE3IjfX5vE9LJS2tOpcUK4O6f1HruFcj3rQN9Dvh0cxjwHkj78QEUpFyFpJ4VgBx%2FhE7lvV64HvttEhMnaqz%2Fq8LhV%2FsPy6pYbq4ak42VvCA5fKyTwmxQNnoqXX7vbXV1mPCoGDo8Qtk16bQPKPEiRFMJ6GmxjsawmoZSwvJzII9jCa3%2B28BjqkAU3nXEWjMy6XwUVRZOow3xF58CgGISnrHrq5Ga1GeKF%2BbYY%2BG2NBBdwocxV5Yot%2BmJCstbqX5hXcAIlzf2zdmZvb7YGeX1%2BBESziUZ1e2qIJbD934diyq9vhAul7T2J1m%2BzgKvQKAfKPWzf9ngSRSWbuiUQz5ijl4nPPTXWrFPZiZae9LlRgZ33Evwwls1eRzI9l1FDipvdyiBrtXc20ZsIZcxnY&X-Amz-Signature=dfe2aa4559026f28ded7f9385f66c895ef6dd7c117b2907e3677c1a1b1bff516&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRSJVVAC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIVKKc9rd0Gs7QDebhC6IOFtW2FXEtkh9Od2SE0exRKwIhAOwvPyAF3n6fegvQxhZJmUzl2jngLS67wY9KL0Mai6d1KogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJQuSLi0r7r8BvhN8q3AM3eyiXlLch3k5lsypdNEof%2Bdi4oBx5h8PTz4mRZ9WJxMpcMXvRFt55P2TxtSwWqtcg019e2wvKYhNZdwtupGd2Gu0qVWnfFBGn%2B6T8JtrLI2oGJiwkkfqwtkLRKLrcbeJc4r0vC4exgTxQezQJ2R6k5rsMnv1S%2Bnvi%2BJrUwovVe2UY%2FCczco203XBPnSNwt9dP8jrSjuXl1bTAG4%2FP1u9mDAg0TZeG1axOOYNVPWcB35FbHX5cebmEIe9NwtqTg5esxRsQUM8YKESZHaavhsGVAT7O9V8QJhDyUoSd8i1mUj6%2F6W1YWFbN8Jrzd6F%2BiPVVcw6YMxdzICPUMtybRPLQDVFe2X%2BQtz%2FXpzY54Ri5qJKI5%2FlOIIusbFx5rL4qg572IESBBQGSP7OA%2FYeXSieeKb4iGfRpJR6Q862Fj3f9RK4loLM6yS0c%2F5CE2Po5LLzqD0SJDuUcLxbM%2FLYr5LNzohxhXU2%2B2C6ILkX0yl79hurEgbmMiW2L%2F9uDnHjOnTizk43AqNxi6LdS9WJDEYisntRKQqrZXQS3UgsGW4c5j1g7zZbquA5rkNnXlTX7KURVrNQI0WO7%2FXMXx8vrFlaSSZupwAak1z%2FcxNzqoMAJdWecs2fB1CCgrR5P6jDA3u28BjqkAUbE8sSI3Pd5o4GWfH6rqfSEd8EjeL0Zhy%2Bg00r41hymOUsGvQRXiYx1cNnkC6HHP5r06OIIezlf1szMO%2FMO420ULNl16cDN2SCZhr7W5OLZa%2FNxAx4OF3QuOiD5eYzK5dLn6EJ3KVPY%2Fvyu9bFXhk1EWrD1jssh36mAeUDUbEAUOLFR0CD3zlwpAlY1ou2%2Ffbno1tlZeelrBcDkTtnIaSEGn26Z&X-Amz-Signature=8feb2891b3cd38954927c657d6215b7aa538bc5b4bd60785acc65f99b6fdd870&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DEBMYI6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqlLNrkQfbEe8Ql%2FjYRTYSKMc%2FnUfDfLtF02IDwvVvCwIgdbqI8lKDNaPAkVFjmXRYtIseMiSvI5MZYdt%2FrFMEQj0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJYPs%2FMwcavAyoUYcSrcA8YNLPHMCbnRN%2B7BuC1ylM7EB7fixJ0oPT3nf6OzJ%2FGBOK%2FZyjQZqhVUN1IdwvNWs1Plxv683I1KDd43V1TU5WTx0Kt4y0APUDBhj1cZTeJTEz%2BN1V4QwfKKphrFyVtVZtcEPkgX4G2OsdzEtKZixH6F42SDx%2BmuPpEral8T%2Fb2p6jmOTwCOgOZn6ZCzWL6OV9Z%2F6EU48Ul62Q55W7WU%2BilNv64VvqCJMIan6fCLibjXqJwxi%2B5KSn0jrRXNY7RRv2czoNa9hqWHWkgGl1a7DHgivj6uKPMCUmOZOuGc563ZuuB%2B51%2FZxslGp5%2BMOYeam6oHZ5EKXZKNBwfrJhExEzSFZe7vpTBuoUJKTixoXxyfZcWjON3DcEsM2Lw4NjGDp08VYQvcPxAAQh6LqqMjhueaVVvaFpYNFXHpT9SrMW2xyVJNiIM1uXs671XMoLa5wYAH5MCWUQWBL6F%2BnEnGY9ni3wAG2IcPSTU7JzCgjd%2FEbg0UIxruVN6WwV9u7pYrxLyO18w4JVz%2BJf8dKf4MYGTxTyKViVwR0kIoJ%2FgNC%2Fm3rZtaJ8m1G68WxRPLkNu08nSiA%2BaZkcY1U7ieB%2FNT4fDTrXjeE8v9sj69C2fj3ss4UOQS7fHmO27kMIVRMMDe7bwGOqUBKMGuSo9DsdnS89ohEJiaYs96sqQmqyLfGd4Z%2F02Nwnt4iNH%2FZAUFu5EWbWKYF546bYgoBQqWReF2xfUu9uWt1Kv0K0c%2B9Nuzg1HnhpEISVtjc3IMEG7PdeVKWUU9jAGtz5XmJqiv%2F5ZpSyWJeUK0Y2hZdLmXT5nXoAbGWrhwQdHEhpAyxQtQnj0KcUnrnPGlErUnj4uAXBAwskBHSv3vgZ5r%2BCYk&X-Amz-Signature=1cdd36015011dd45b6e7027f4f8cce06c7469a761730fa23913097ac5cf82cac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THE4E4DW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5E3u08rTJTbpLTPU21Vj%2BOLGLqZRJ0L7TrWl6n3kBHgIhAK6HN10L6UTOMpeLDuqaC65TUq1wdXPGuG2XCJiS8oObKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgXmuYNrTYDUZ%2Bl6Aq3APL%2B85%2B1IhEEYr2MsuPztOXJQyb%2F%2Fi071vXESrExa2SqNOjtG9EagK71qOkaOeg%2FeYVKUP%2F440eh%2FPTC%2F7PDWDrwv%2BeEDTd0Nk%2B7nLhVQSBEn1abOX2HVy5%2FrIUUK9FvlbgA%2FDMJB0h6Jn9P7DKpTN8Z5IrXhFL94BzzdiaeMGtwkX7EPms%2FZrebuuBKnDlj%2FREEkUwtIWJTJ2g8p5FcRa7%2BuxkH3aUlOzqgAXqE8yqh1Jj4jgGRSAe24602JAGxab%2BgUBI385gBvt16I59bmpY4F6JXmVxKlJXlTj23Y79VLvrZDuoG4LXoepJXwXnkdRAM3nDioO48f4%2FGVk420ms%2FzjLQQ%2FE854GrEBw3CeWaeMeUnJ9mLXRKxRVIOmDZRfhrkWMDDSQG4y9MgjnUGzPVi%2FUK3JKv2g7mVYERJoVLuI9ED%2FV7xvFau7iNZwlR%2F9pdQ%2FcipHrXBaPyje3d2YXk6UlQiUeADH44Fc4ULcO9n8Zng0%2FvV%2FA199hOjYHaVdKNVQ%2FQNkueBP5QhjCKaESBqHNQWs24tdt1Y0P8VqBlGDgAhlbmrNlPFUl8ywpeJTWVfXSGaprJRwSuObQo3faEss3v3b0UlFPgC6TZUwW8gdMvdNRqclcqWwIrzD%2F3u28BjqkAX0c9tvws0LO9ZmRLntnyweZwoG0J9%2ButaF1o4Dk%2FydChZ9xlkuNxrbwXIHPTobAgajx219mFw8wDWQanZzzU4uOKnxZ91hTmhWQfXGc%2Fwh%2FEBOTtcKcvXXBchX%2Be7utlIWKFcXeAHS%2Fx1k5UeJFBxYpbQ%2F0PJQLDHSGjSmzUYde80WrF8lVAUgYRDddTpeG5qvE7FNTrPFdsJ1P2y9EFYVPEBrq&X-Amz-Signature=44cd419d9d43173d0ca92d1fb64b1755fc4c6c08c0d335d4b0417dfa833d0191&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VASZ4SWN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxbmCzL7iktwjn5YoVi03odYfhbtLQuzahe09YUhxCcwIgWuxcL5J7rBIv%2BW0OQ%2FF%2F7ncsAHV44lSMW08Sd1sdE04qiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFiXG9ac1FlMA6qxyrcAwdrAPooKb7qjxKb%2BmBkNwm9vz4HB39QDX389yhTM5urwtJqm8urPIHr%2FtMYWy3hMJ0bpE%2FkJL996Mf0kPD3VAwrYE0qbNltY6Z%2BG4HkaOvdisseeQxAlCB9Cv5w32r0WDD3H2SpTmMsGeBx4IMDcmVw4nEyDArRFEYX%2FgK6swFe5Pcj1m8wxr5jL0ZgM2oRPj3zclEPml8XlD%2FbiN9ZdS6GX0UbiEqtq6Ui8qouR0%2FDLnr4tR17rnh6RvJT2sU2PCTSCQFJN8ni1iGZ2yZlljihBDdaT2uDDzwNW9hDCH71Fuko1M20gc8Hls0KVyAjChkcJ8s4Tvso9OKC5zTukkaiOWMbnIP9QGcOyJtd3rHllXtKdCXt6QJU0KZ1M0ejaK%2F6HNZR%2BqCeDdrLUYa17FwO4FjqjZvh8Cxs5pawaDftMURgWFlmxt%2BlwWrmvsGyBxUjAAB1dGhWPoZYWvx4%2FDyi0U3DKU0R92hVv4JXmCRj8eByx%2BS6W%2B7eFeJCJ6cZThPKUvBgg2SRf%2FG92NehJSDALXtRw%2BwUFHKQF5X3W9y%2FLfTVL8cZ9WWURLXeE%2F9cma1o1St0lCjg0Vqe%2BAEcdS4mWTQTVd8%2ByHthxWwhceoDjIAHIHe%2FkLpsFqFAMLLf7bwGOqUB3fnUnKK67OQDIR8xhWZcHXVpCV%2BgcvniJRUqAF8yOdfflbCj1x2eTIEO5EUcrpDMsmpZwaaVjtyCN%2FZX4al3HwrJ6v0Mm7vepFknPgrNc9aVroNGXH6lz3i9%2FVixUwZUTPZg9bb2E0vfRMEbjx8%2FERAsWwlWIYhoa0M%2B7kehdxDR6G7GMLlKHXTHHGrpLabngxGL%2FSITy%2FMbMogMCcGEnkJ5lI%2BT&X-Amz-Signature=f8dc5beb38454dcda132fec2477cfcb099fd22ac6275b3cb33d22eb2dbb50de1&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OTUUJVI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDY9pGQyAiN5jiFmrDJ4n6i77hlx0iH9%2FVYjA528QFbawIgcYm7gqWqKuqTkfJJvUm0ht0PGhAZmd8owXeAsOnHGK0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMfCy0P9U82%2F0QipEyrcA8GrovudKt4ZFUwT86WlRk6ILXRXFAGFyIhzN56s7pZkJFNScNGf6EFKRqGLjA5dld4h7pv0lVzgV%2FNLNL9%2Bt2L%2FgZoOuhdbbiin54Xz3DPRs%2Bmk5Y0qWd7YSaX8YYowHIfY8dCKwfN3hP4w2rjXEa%2FoELu%2FsdL0dsLbneuAEfTvjswJRiJsalH99%2F7Znb2E9AW6lI9pB1jO2uBj0bDvyRLdUSXkFYm4Xaq9usVK1XuPmOklvSdzb3hLixtGkaf2j4%2B1LUE3ctv5ibRpXbEXQwDxr0uo%2FoWqIhbjZjnoywr4b%2BXIoGqcrYimfUNcJLOplGGqlDttiZDeG9xxUUFfe03d%2FlMgeFo8F8jJSoerC%2BBRypkosBKwFrPKeBa7bSqTb90z5IxvApjLDkYkLIq8RqryLkHXg26d90w79xloIg5%2By5CQhhDiAFVS9zXvSRVCu0Q6EUsEvavkyT597cMDU6i6jNwEqBz1wKs9ljUBW85AdTx7aAZ4G4Ckl81hionh30mgxCWP83F4oBbPvBjOgf%2FsZf%2BVakq%2BH90UADP4jycqWGBOiXEA6K2xtlpaOQN5QCqFkeNsYFxC8TsDUiTxPDqlCfZ4agwrIW6Uo5WLLTFqekzwcBbTswmRp%2BnIMKjf7bwGOqUBNGgc2gGuIMOH1z%2F04XoCoWD526W2YFxMDwnyCtC%2BLG9%2FbeqeWSB6j3CUqlhZvpHYX7AkS0ZTbp1jOzXIYGXmFi8CZKYP3g%2FANZDqqI4gZQhdbgahqwuExht4Nv5GAD7Fy3DHJ%2BjI5wAtCQladg4JU0B%2BnK1ZmDG%2FItvpoCO9fwR8%2BzzuIYqdMm1Cot9231HHbtbBTzLSksMfbxJYDx75X7sGFg2l&X-Amz-Signature=d227cb195619b352439925b313a3421063df8b957a0817b1a8c0c626a3169357&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWSWFZBD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIANS1Rw5Wgh3e1XQAWRLQL2KSwL2Z6n1jJrN70%2FNmMIPAiBY2W5ReqHu%2Bds7XoL0w44i2F%2BFbpePjnGF9nyulcIycyqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSjmG4tfzbCvihRIKtwDGdReQz00LwUlXMOtMAk3xuMDqAMqoOyXDWKZKaOxeP1T65BVERoP59RxREUdYiZ%2BLE71tE1kDyGkvWZUVjo%2Bz8f0bDeCwtut%2BkI8Cak3EiauTHzaSKgTBaMMTs5CMTiloJGSY9kBC7tyLUMQzMOTvWiQaKHvj6o0L8Jk9w4LM8csOrB5%2BzllGjGx5CZTI6wjWmQ7Hf5VwjFW6coR0A8dU1h8QG8HeCrZrwc7wBe6U%2FQnbp8hphcwZQ%2BeD7j9Ysz2nNhHWLoSkZ9%2FgVvS98tb%2FOgeaNoyYg6M84OWDvLrtLVNQd8vNz%2Ff0WWIMYFRYrTWsoYvv0hqC03aNdN5RmVIY2MgL3vr%2F5UyaiLke4NBTIOqjlCkxU3V5fNN%2Fqp%2BNis1oZnxjW8dK14ofMxRn0tsL%2B9Sky8WqTUDE7obhGm%2B2hafg3jIqemqT8FgZi%2BObfS3mWJcFbNR5hK84e91Lqz4W93omixgZcznqAzwQ7wB7E1eetMAbBDlE9%2BX1ybqPn2Lz6T9FZA4dVT8zgCwMABxkswGffI1GrK1iOQdcZB%2BeoyaskrCK8Ist2g4x%2Fk4I%2FU%2BlzRIFMMq8ORbM4KLx%2FYOOZp0I5NPenu6cBN9LpZwSXeY9Zl%2FjPGx2w9bQuswvN7tvAY6pgFeHYJZSkPDRIXiMhzdwAC%2BCMxf03KO0ZVC6X1MOkpAFX82RFh%2F1M45a2oIl6nBeK%2B9XQQ%2BdLlCiyZpAq3rs61cl8AeXWUl02m5%2FB7L7HtyYeHLOS5dtz1ajYhHxXHJ0YY20ae7ZCCrNfwm%2FRxxVEBgeaQC04xHpjYr20%2FVJYkb4meivKY%2F3ggbv1MYV7n9FnuuwBlztuEf5ngDqISEcGAeYmNNlgH%2B&X-Amz-Signature=4110505317aeb8e5b87c5a7e5f4d62328581269600ef962a9a38fe3418bf44b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THE4E4DW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5E3u08rTJTbpLTPU21Vj%2BOLGLqZRJ0L7TrWl6n3kBHgIhAK6HN10L6UTOMpeLDuqaC65TUq1wdXPGuG2XCJiS8oObKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgXmuYNrTYDUZ%2Bl6Aq3APL%2B85%2B1IhEEYr2MsuPztOXJQyb%2F%2Fi071vXESrExa2SqNOjtG9EagK71qOkaOeg%2FeYVKUP%2F440eh%2FPTC%2F7PDWDrwv%2BeEDTd0Nk%2B7nLhVQSBEn1abOX2HVy5%2FrIUUK9FvlbgA%2FDMJB0h6Jn9P7DKpTN8Z5IrXhFL94BzzdiaeMGtwkX7EPms%2FZrebuuBKnDlj%2FREEkUwtIWJTJ2g8p5FcRa7%2BuxkH3aUlOzqgAXqE8yqh1Jj4jgGRSAe24602JAGxab%2BgUBI385gBvt16I59bmpY4F6JXmVxKlJXlTj23Y79VLvrZDuoG4LXoepJXwXnkdRAM3nDioO48f4%2FGVk420ms%2FzjLQQ%2FE854GrEBw3CeWaeMeUnJ9mLXRKxRVIOmDZRfhrkWMDDSQG4y9MgjnUGzPVi%2FUK3JKv2g7mVYERJoVLuI9ED%2FV7xvFau7iNZwlR%2F9pdQ%2FcipHrXBaPyje3d2YXk6UlQiUeADH44Fc4ULcO9n8Zng0%2FvV%2FA199hOjYHaVdKNVQ%2FQNkueBP5QhjCKaESBqHNQWs24tdt1Y0P8VqBlGDgAhlbmrNlPFUl8ywpeJTWVfXSGaprJRwSuObQo3faEss3v3b0UlFPgC6TZUwW8gdMvdNRqclcqWwIrzD%2F3u28BjqkAX0c9tvws0LO9ZmRLntnyweZwoG0J9%2ButaF1o4Dk%2FydChZ9xlkuNxrbwXIHPTobAgajx219mFw8wDWQanZzzU4uOKnxZ91hTmhWQfXGc%2Fwh%2FEBOTtcKcvXXBchX%2Be7utlIWKFcXeAHS%2Fx1k5UeJFBxYpbQ%2F0PJQLDHSGjSmzUYde80WrF8lVAUgYRDddTpeG5qvE7FNTrPFdsJ1P2y9EFYVPEBrq&X-Amz-Signature=9b7ff2fe88f7a442a8788156204f1baaf852ee200ff0f9bbfd9ee5163e9db098&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHNRXJ6Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjYCJ0%2FzPudbyIHBYGiqFZf3rSsMJI3%2BXGc4rs40TjVAIhAPoxa0db3x5uH7lfw%2FpApxKxhmWDBddlSCrBtmYT2SwoKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwBFjSpO7l%2F9EltxaMq3AMJhPR1YM2MP11NXFMr%2BRPXgMoQIQNEnfpeYaArjfj68ZAIwziQvnD8WqEowJu0lnUL9HwnuAxr0Nydf%2B7jgoomdL71bJ2FLozg3uUjly6%2BOr8AT%2BZ%2BnbGni1GsEtXJdWaVWvAnX0%2Bypc40BxEEO8F5dDtwVklsGfwbM0ZRZ075YKZBe5gGsQpKDwFoc7G8rtfIywvPIjdBvQ7qV%2Fv8o7hIH1%2FgwIkhctemAINdCPZDF5a5pn83qOVnbU%2F3oLsCWce49zwSLLHUrmSjxM%2F4suTad5SWPsa2daez86c%2FRkAMq0CcCQF6Kppmx8CgUnay0yQN%2BSqvQU%2BpLGw8TcTDBIoVjjl%2BE7l5llm%2FPBd8Una%2BMJDr1AObq3Km13B48SL%2FSI491xOlIl1X32LuJyTPCro3L6FYQgmWrpvWUjuoKd2Ti%2Fqhe72XZyXSO4pthBgT03OCrVmEqVxnZbA1KhQE%2Fb9%2BWL5SflWCqJi%2FfQrwIrYaX1HyfVz1udY1P4JQiEkXVzUGIkco1EZud0SuNiyt5yhr2sp0KWaiJGw4Sc717J3yb7mvXSm0PZp08cL%2BU18hNI4itgzQxQIRlnUfC6Xwfc0r%2Fm2oRF2uNRGsqjnaAAmv6eVScmATTS0dBlXL8DD%2B3u28BjqkAYVuAucq8rorkje7fCbp3ijv0dxzbmqZ7xcZJagV8crciz9E5WI98PMyK8RNt%2B6yTK4vxp9PR%2FnnFCRP4qCSNvaTE67d2TIeAda6XMIGcTaiTb8Z0yf3SR8yKWLYm%2BLmr9mLGaJcRdIFqJF9lcN%2FEA5p1RPJYchlBIRxVGmMMwbDm7%2F873lgOSPvboq%2FegRvUNQ8BNJ%2FntxFO5CIEroU9JJ1dFRP&X-Amz-Signature=73910c4717de76b5270cb1bdda46c1dcef9a1b8e045c2f6bcb658cbbfb96e158&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHNRXJ6Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjYCJ0%2FzPudbyIHBYGiqFZf3rSsMJI3%2BXGc4rs40TjVAIhAPoxa0db3x5uH7lfw%2FpApxKxhmWDBddlSCrBtmYT2SwoKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwBFjSpO7l%2F9EltxaMq3AMJhPR1YM2MP11NXFMr%2BRPXgMoQIQNEnfpeYaArjfj68ZAIwziQvnD8WqEowJu0lnUL9HwnuAxr0Nydf%2B7jgoomdL71bJ2FLozg3uUjly6%2BOr8AT%2BZ%2BnbGni1GsEtXJdWaVWvAnX0%2Bypc40BxEEO8F5dDtwVklsGfwbM0ZRZ075YKZBe5gGsQpKDwFoc7G8rtfIywvPIjdBvQ7qV%2Fv8o7hIH1%2FgwIkhctemAINdCPZDF5a5pn83qOVnbU%2F3oLsCWce49zwSLLHUrmSjxM%2F4suTad5SWPsa2daez86c%2FRkAMq0CcCQF6Kppmx8CgUnay0yQN%2BSqvQU%2BpLGw8TcTDBIoVjjl%2BE7l5llm%2FPBd8Una%2BMJDr1AObq3Km13B48SL%2FSI491xOlIl1X32LuJyTPCro3L6FYQgmWrpvWUjuoKd2Ti%2Fqhe72XZyXSO4pthBgT03OCrVmEqVxnZbA1KhQE%2Fb9%2BWL5SflWCqJi%2FfQrwIrYaX1HyfVz1udY1P4JQiEkXVzUGIkco1EZud0SuNiyt5yhr2sp0KWaiJGw4Sc717J3yb7mvXSm0PZp08cL%2BU18hNI4itgzQxQIRlnUfC6Xwfc0r%2Fm2oRF2uNRGsqjnaAAmv6eVScmATTS0dBlXL8DD%2B3u28BjqkAYVuAucq8rorkje7fCbp3ijv0dxzbmqZ7xcZJagV8crciz9E5WI98PMyK8RNt%2B6yTK4vxp9PR%2FnnFCRP4qCSNvaTE67d2TIeAda6XMIGcTaiTb8Z0yf3SR8yKWLYm%2BLmr9mLGaJcRdIFqJF9lcN%2FEA5p1RPJYchlBIRxVGmMMwbDm7%2F873lgOSPvboq%2FegRvUNQ8BNJ%2FntxFO5CIEroU9JJ1dFRP&X-Amz-Signature=edd3494564d18ca991e6453b2e8aaf82e95c9d2534bff2e4bbe1f9d629c66b9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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