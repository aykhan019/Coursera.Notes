

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJIDBYFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFN5uxME2sqAuiOGxIbIgvgcOpKSv14lSrNrF%2BL62pZeAiEAkyxa7Nn%2BeJJ2bCsgthuZhNI3B%2F9cZ1pIAwdnL6MeTHAqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC3iVXJ0fsKjfIyKPSrcAx5XaqSfNyANZ02dGgZJcwsnHNnErRMZ4bfL8tFWPXXgZg9lcWA7u3yzcYFaTPV6HpNMJSx601o2avAUibBy5WtxgoB3McLnseQ%2F8cKkYN6UXnu7jjXSXFsqNgNbz01mMZZ3x4pG2LSNbvoEE0MRhDU9A1ZStlwCe4%2F9yDBtic5CyjPOMCsJX6qjdYykAd89OUbwBXlSVPnfsXs%2FZZRwXTNGj6K5Xc3J3OKWe0auHhfeKmKw7gy8hXbKQGID19v15dv9eyh7K8U4hZxG0s8hQUbuy4KlHljhCQD6rtRMB%2BK%2B4K7Ag6teiGrpK98Q2GCORHDPhxGL6GL%2BWAAODqNj%2Fa3SjtCFTuNb6xBCCJMQpekenQLFZ2SDOK9nzV2Bt3WVSOwrJwYN%2FcPIW8Yjo9ZTv0SXq0S%2FKz8qjWz16gV1JkbQvWQBNKEYGxgBv5%2FomY7hVI1yQ1SxN7vDHdBD3tCZl6puUBev%2FJNqtV3pBgUCMhxAx9IJN4rRhm%2B1R5txulFBZ7%2FYXSf2JD04SMJqPTmwEmYOwQzmHq16%2BWwF%2B1s5EtxBJTh4keGNYbXyo2q7G7h%2BCCIGUy4sWN%2Byta34sZv7lz1ewHJOJCa2toqKiPuwDqMtesq0XugdYdTTc%2B5MMMbd9rwGOqUBF1yMPwYQd2zY47hXfMT5fnwH5LxyXPzCy3PmF17G1bOlgohWMgVETCukj2GNi34d6hjKY7uCXaSARwgXFr1NhmL0t47ni9gr3UWEq6gwnfuOY22FLYS0eriJH%2B7hF4bWFTC%2BiUv4aJzYN3EkegPFoDNnfh3rsL299ZvlmDRykXX0OdE8wpa7cmqJwBsIho2s90hrfoHcbD%2BkMomsYrYZQ2YTF3Di&X-Amz-Signature=e638ee09709e38fcc3d79289dbfe1bfefd43a340a0c4c20b92ffce44b1ab03a2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QDG6SA2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDw6zB9H%2F4MgEwQFEMbAC4Ddpxu%2FrpuXXP7T%2BIC8kdYNAiEA0c%2Bs2vEFZGSycTsCTNgi0LKZ44S5qrqyUcYKNooVVFEqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHPpmCU70lTQuVcnSSrcA4qDOM05reWjfxVAt%2FlX%2FtdL2uI%2BnAyrcJdp00JSh5IphVWVOilykIFS7pyZRZMQSC2qeCgO6vHv%2FNWxhzM82FIxbc8bTCeGuek86XNHtgTb5keyWs1I6tV8AkAo07Kja1eiAkzcQhpYWONWBZHOUedd%2Btn0q6nXDJOgeSB3bBEhXelo4XUmwJTWdyjTc95nTxFa52KcunZnVHxSqRTEvuaAd6s3taJ7y%2BemPMyQtERGiWiTSd5fYfexjQyMZvnsov4FSZJPzvE%2BaZ1U06DSh%2FVTybqUU0EceC%2Fdoy6xcHu%2Fy4DLJMB4%2FYQpTNRLfyVqsChcNkun0JNy2GkrV9ukkZOj3Agv6ip%2B5diK7p%2FEfr6boFUj9RbH72wGE5pp0k2VVPLsmJoSQLvZ2exZVaYNNOfjc7HUVXdC%2BgX9Io2w3Wea4JUDm1%2BF74B4aVdFN8XQLZDyK82ecKsuFBhCQ%2B4B9EQXbhP21U5bVJMwxLCIjU0ZczTazU5wYxBAlmygW%2Bn93QfAWlyZvjcfobFzFu36vv0agQulK%2BzcYzPNQqz9%2FPyWsMIouz36ij%2FnFmT9KjxqE9l09YsPETM0HqItklFE4zsso35JaImnUT3KqGFp%2FXSC3dI3DzlUUhNGQqLYMOvd9rwGOqUBOf7Fik%2F2gAZQqpvCwfsTnV6lhBqwsRlvKBwrGCY4dg9YJZ9BR8afQQnoYKIJvTqX1UUXWbbwCeX%2F7kvAjnVG8yNknRc1ayw026n0Ib7lT42Wr1XYaeJWdacQ8TeLRT3AjRmhIXOyOjNGKzV8mnPe0PM3SG6QX8hPPGOZ6JGanmqVUjEkHowonDkiIHz13K3%2BV27DEV2rcavFteNMALT4hVrRMT84&X-Amz-Signature=95fb0820e6b9f43e1447699d12d8472e7dccf0b357707a6dd646651c3a1f2ff1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBDCTXI7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXft8I%2BWAH85tNZYPIB430T0lriDK80tiw1wVI1f1thAIgFZGSITebsfrwa8ksWey7UA2lZSSNt0MhVDgDPgbYyPsqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPpWDy%2BKNH%2Bal5pHhyrcAy5S3XZ5ILlY2Zw8pAvLtbgL5b3%2BX8f1V0SZhsSn1GjPy%2BVTgh1qAYW4hh2kmaEfs4jfPh7r%2FGBm3rzynAsMEL5Inxvz9leD02%2B3AlmLXyws54QsIzSrSksRAJSQhp0vGZMd5%2Bjp%2BB2GyaMHtJC6ws1ib%2FoNeLH3e7uN4nTiR65wVrfZROm5scIfn%2BvkdKoa86DCbjgk3Tot44WAAKJy%2F2HOeySnNUKSsZ%2BltE3hhHE3Y2S5urFC7kUjmMzXevePBh9PPcQadx1wdSU1PDDYiodHqPOXktBWsIHbrp%2B2w7MzmM0t5Llb9uszM8DiybnBdrD%2BaVQWOhuqFdYn7M%2FbUhteGypdV%2FaUTszWfz7MfHaidO2IGkXjim5iRyNED5ymzKTR4JAWBMUB3EmDl2I9TuLyW08W5viIAVtM2Det6Y7zLqRqoMEtWxm%2F10ytXw2209Jg4Zg7utfWFmUi7GJ4TUJYlioORO5MxUuDcnHxRLK1LmerJP0XPFVOm7iOFS4k9SZTZqVeTSD2Ftpr%2BzjbAbKgvKnQBLr4k3qbi9uofBvrtQuPXyotGY5xpS2XIGVpKDKrOhrdWPupUCoSZelOENABZxCmFCwUQuECy1VvLHSb9mWxHKbjnq5bUnVZMNrd9rwGOqUB541gkkVzeRUD5jKDPrYP7OxR3Xk8RORngXIUkWEcpKZcT4hhDn06Aotix7FiNjI8LbslA4aSfHGT1FdUzPg6WxYzO2Mrl7KSa60WjJJOLWDUhSjBt%2FqoF0a5qv5pKt5hUxo21tgrovH6xdIiyRlbSefevPQsoDbRHqiGUZtcoWdr2H6oAzZooTcxagx4gwzlz9ITpDEy3vBaVrrcxAadnhtsJBvk&X-Amz-Signature=64442a95cf19e5de4c527d8eac6460f89f16a8fd1b549b811b756cde8ad8102d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSC5S6D4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAc6Olfab650InwRE0fX0gIpEzWwIQ3Gw0BvqoMAtXQtAiEAy3%2B1QTsDYLcpcnJ8OQ98hQl3IZizzQ8M4wh73ihwrZUqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9yJlF7tuYLv59aTCrcA37BFtirxfCRsFdBAey%2FqMUjsFpLkHPTKuRRRCgEIdVXyadxQ1yi3jpKvM%2FQpBBNbr9UuqICX497GRYBMBIT9qi0XLSI%2FoazpS6oxnzf4davaLsakP0d76nKWdicwVPYxwufcrnVgYdbZyaVppAVdDByvLscBwdWrqiFvcHORPvJ05q7T8NoI1AOeAZCk9k9Xg8p5Wn7AHwlOIg7iW68DpieuFz1HYi%2BDitPBjM2y%2Fi1rSRO%2Bfq2FaqqiFNPpTjmLTdjM8WYC6zrb3lwMmqTTAs23Ssh0M6haYTMLm6wkRHsUffI1YwIlMxIhwnUCcOJaY3iTnB6TInMRU46qpcT41c7unDK7LlgSDJ513%2BAPjd%2B2olLCwta8bTXPBC5nsEhaG7kHYwxdr8anJ65Jd2eaw0Hvtk7GMQMn%2B0bYkRnB2Wq0QaNwhF2nnvjxPC7ehq7ckf0M9f9of5X7J4HhSv%2BUZ6Gg3DRFps7GTNtXJkdKDzacHudTWKyssqCdJYQcVNpUQ%2BkjoKWfWOdI%2FWUQxF57e9w9wmxLX7J5QE%2FOZz4WPaOEF3J%2BuFAM592kM7QrGlUsatFDKkpQkuS%2FtZeWAU4yKnzQCIbs2K6Ra9G%2FzQ5HId5toB7XVY1Q0c5Pvt8MNXd9rwGOqUBJjQf3IN1s6CQBtuAOBq0QZP%2BGS4DhY8yn93%2BASb68ai8SuWpOGgQKghijw%2BHLGYcc2MBTUBvnWBmwdr6unZnAAgim25fPVqnspqhhbB%2BM46pa04tvYvJPve48tBGhbtQK59GowZYH9eItjfP4rzT4ccBcdcRwQwvlLCQ9K9ScdZiQ8ZpM160YLq%2F%2FN6RojJdLl8hbFCZ%2FdyCR8BADZCOvwEcdyk3&X-Amz-Signature=6b470d65d8152da7b2cf6f841c0f78a4643605907a064c510ecfc1114bb52c16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNWEXBRA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAkmp%2Fm%2BHZ56VtzYRGfSAOsKrxYkKsYBybCEVx41bGV3AiBZpb0cHBRvKwpA9Ie4wwIx6jqvnKoNsxX5TSVTi3%2BsSiqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZtAdpmv375WwZm3AKtwDUfmQH7MBb4KShPnq63uNHOTa6zmomp7EQUAGmbr24DIcOq6TdZHUIn5vJntkQySrQod7B43K%2FprtoKFRGlvxE1uLiVGovviOuKI%2FyG5Wz%2BW8toob5X7tUo%2BCwtA3qyWVEnfeIEacoSyI8Af3CFfj7YlkDrpSfneI7Uow3D2MIdpe86EC9kgfNADYSugTyb5izo3VhEKZYpKlIkPJq5PCdIOXJL7hjUHLSTJZJ0hQHtEMzw0QTL03eHFomQSPQdMCgdIFdMogWoxlluYVIqCd%2Fb65Zl4DHU3UykZPrH1kMui20RkNaSkfsACarp7bOB29jq9DpekW9V204fDA3bdAPJ6I8%2Fi4%2BNIV07UQH0El6gnS%2BhE%2F%2FwNRvFNL3hk4RhTs9hG2Yu7Fw9I0GsKwwYpV4gDfB9uJxzye94%2FB5qK3GmwRv%2BNMZmk%2B5khDlkYV5yCv8%2FofN9fERBivhlXwVu2z6Ok8hnXnPXci47m1iNkcaMyDRH3gydts88DalflV6DMLQ%2BRiLYcJD85l%2F9Z5aVTHFvCX7AFp9p0XPUGNWxZv4t22wJKpsAFEJ5Tgfdwot8DXzY5XJroQtmE77XSMaWJmvb0Yb9vrBgLK%2FR81ukFr%2B1ysLvTY9iWyV5nOFKQw1vj2vAY6pgFpP%2FXVcEr9dld%2Bx9AwnUBOulXYAuMcJNsHdCn1GKnv8jN63ypr1mxHxjyx%2BbpILy75XccPJIB2sM74O3oex3wzIZZT8sWaqW2AwKgPF7T5kqwG%2BCmZINHxN%2Bj%2F7QMnNSJ02dvM%2FtSz6YIp7qLV3J5YcPRfu%2BxDfKUUworSI9%2F17GSFGniGF1JkxHVXyHc0TTh%2BPFvkIhGwKyemJ1FxEeCkvPoirVK4&X-Amz-Signature=c1844c364483f581dc3350a6888691751e7d3e7476420d422cc95bf93b673cf9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JULNI53%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmBYiHUh5CiLI67PtOabgLr6ZSdbK8ruqL7rL5CSHtYwIhAPK10lcUkJ56uO%2FVEp5gq8RiDO6nok6wQHynujH57UZuKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzr5iJVRwzBjIEcAkEq3AMXzasdt%2B9vbjukT5en3XgnkDKDiywqSsnSMgFMUzKxMySgLzEilmibUZwTrn%2F1caKNpB3cElVwsRynZvrtoDmU6CFXNOGcIzg2CqCtz0dNDBlXz1ItT2kf9PQeFlqDrpd7qg6pRfms2HChe%2B%2F2rdar0fYKI9YHaLUwTTY9kc%2BxQMYwK7ihCWfeRRMqRqrTr3jI3hUVUG594kuFw5vwEfJF0H3T9OuXtiqMvnAXIytHWO6UqrNuZvXUVJnslAY2o3wI%2BNSWeV4Jl5yq%2FARDi8Ms4r%2F4wMxODmkop1CjrzfvxNgZR6wm71ICzgrEDwTHSMpoC%2F%2FHozim%2FxqtvRdXLDqVxuZSxTUoDVbhJt%2BGysl3c%2BvXfe%2FEQXtW4E1tOWmE%2F26qof6kGzu5tfbYV2hn%2FZ6fYt%2B8aCkKUP%2FjmnxZMg%2BueThbZCbVSHrcXqpbu8acqAp6s0kmJ2oSxAJuZu4%2BU2jic8UJjKT39zID56poYkYFeVczy7ziQzLgBa0zKUcgEQNxBAmJR3oViYtKKCqrkJU1odorbm9J7MIeCHJ2n8Cq2lONbj1GjzZo7JLEZU2tNt%2BRBACrxT3VMCL1vQWX%2BYSIZJa8cCGPmS41eJZHbuBhulCgO%2BmUWB6u8caqxjDc3fa8BjqkAXQpYPAI4PnMCtW9qM52ZzCKBczBGISWKNARIabCDSroYfGeD0lI%2BPPRLIm1U6HepXEVirm6DfCgR4WvA4Yica9HsZnjswgQoO1SJGEodHE1Uh5nRI6tewOR%2BM7UNieagEtKLZw%2FhZykSpr9rIqxmBnCoprPKUYDNFzKiN3LhcZs9lv2dfT7NfynqNYnGUNdTOmEEchtcA8rOCs0QL2hYR7Kcvs5&X-Amz-Signature=b158ce78d693bf641a3e3de75492388edadda5ff87da7edacd69129396acb47f&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUGPR4XA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEIJKWKnA5OfhqAYBIaArUI3iIh9zBGB3OcyD1dZdw%2F3AiEAwa9k0%2B2E6k%2FrRFr6Tl2sl4OvAg3YUagMRsn7z%2FGICeoqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI1HpwkviUO%2FE9GxvyrcA9zT92B0UTz2mHh9Tx34cDyPevE2bBBOqcdipcxSdQDyJRoz4K6A15pgzd4xbw%2FHyMkaYMusIrM9CQJiAeDD5McZbj86fXvtuICNLvTCgpWmd6OHxU5dvLgq%2BG0ELnQlj5gRR%2FvsGEiYeo4B%2Fr%2F%2FVM3wgmF97sRNJwxS%2Bl8MTnoWuRq3N%2BoNAPf6XNtbQdK3TqDj2kwkbQyrcNRnNcSpGYXUsABt9On9XLW6kmDM3X9nCs0GHGJj7Nigen19MaxC6fj62gBlNdU%2BjYdHvLx3CxufcB8dnVIOVtQDGI8L4RxIEbgcYyVGhGcVX0QRgKcogijKFkj70pJUsBA%2FLL1%2FBI146Q8DyckiA39xa%2FJ9RN5Ck2BfBYOyfRMtbNxGk2yT5w2fUkwtwNLLi68U6p2Npdti7Qe4Rhj6T1hrN170zD1u8UcExA7dzNoNRkxbdcqHlRM4hhIlUxPPIQOSyNeJj0UgbpfXCcO%2BdUK6E2ZPXqxPXIJYKwPLay7CnLrQOaPMvJChAb8MqbmNDo8MayYkXoT0Jx9rpQGbxl3zVSSHRbsxXs7i8fTfBw66i1c%2Bgywpi4FbUAtP%2FWjEeInQtJl%2BN9%2Ba7JHEXlSuuQV0zRDYkNfwutOkks%2FkKgEtKMUkMMrd9rwGOqUBrYdxick1OHkBGEJDivKppo0goe4KEKmhwE4gautf15oCkuvVDmMiExr%2BaORHkCTx3Nq2TmFcKi1AKQJlRE5BNgJWa3AxeNrb2bc%2BUkZkQircD9YTkjYvviMCmEDqa6gBb5YFsJQlTuDBjtGmymhhC%2B17lXGCRZxDrq0FmG1SZd%2FUmWPQeJtRNfuYjgCq8sRVDQVcx%2FczER8ipS4TcsTP4QIGyDkM&X-Amz-Signature=408a770be4735831c7a057e857153a12c71666e2aa59d4059664261fc1345369&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RRUIGPO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtIdJI5zYmu6yjmqqZ2GF3L3I7P6M5rXm7STWlsyN8EAIgGAxNa1qCSDLHzQuK3vXe%2BgYtozpBUspo6xFyzIu%2BbhQqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOTiSKo8OXYG%2FNhEGCrcA9OdLOq3OeLdpO%2BC6j1rp8fpOQMWu67DDwlryvxQ3RSfQ9YWqBg012QaJhR79kP3czRBuyFG85alTAsdeIKIRgejKqyFRjP6zO4r3opX0icILGLdlLg8Ewy9xJFqoV3s1PIcwOB4H%2Bi9k%2Fh8QBQPOvcg2IvjQClJuVgBNy4fQXQm6436VwYDwcvlSkLoXTlKYNClb3cv%2BGV2glcI3hMVtGYWnzzzRVYAwGEw%2BQ7OgIxm%2Fc9Ccet0soMjJL4VkC14giSHg9dY6zyZN6J1PZPcWMuGM5Xw7IU73L1d1QvKRkNHKFPtF39cRZ8kBay%2FGFqE2rbf0hkYGWdZlz02Gb9YV7LTmSfx7B1bTbSsz2kNFGnCDyiUja86VwDBmnf615FF1q%2BcGj0PsQj7lBBtIY0pOY%2BBrJy7bG%2BMvkaTQr%2FSAjJ3OFcCePSXQnHSz%2FMic%2Bx12Y8q90QjybBKFgtQtrxXZu5x11E%2FtkvPGBNzUiK5eAO2ept5RKf8GEp5%2BDCTAWZ20pIcjTmDdZSKLNjKp8pk459brQ6i7RKx%2FBBUfe%2F8uBhregBpH7mh%2BOTJNo%2F6PF7KusZ6UbAiT5ukPP8K%2Fr0odisnXiq3lOub8gdVHOTfI93S%2BeUlcDylv22nJEn%2BMMfd9rwGOqUBE10%2Ff0fFc3FQ1teu1ajHul9W3nSPJb2K%2F3epvqveo%2BE78PDVXq%2Fw7qqce%2FERP6QxHnYdCwwt0Hr08l1iZBIyAGNow4d9fPmW0aAC2ABu8KkZKRA1OsnNF61WUeDuuVrCWSHpMS9YT1n0KjZcD0Dwf%2BUTfybCyvz9JgZs7ejZU5btA3qK4IhIS1Cmx7TLvfeyOXYQXwq6LRC5RkkfKQ9RDYcWfRmi&X-Amz-Signature=9b8f42c6a973157570775ccb9e2775f196bcb63f962751cdfc2cefb69d827b35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNWEXBRA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAkmp%2Fm%2BHZ56VtzYRGfSAOsKrxYkKsYBybCEVx41bGV3AiBZpb0cHBRvKwpA9Ie4wwIx6jqvnKoNsxX5TSVTi3%2BsSiqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZtAdpmv375WwZm3AKtwDUfmQH7MBb4KShPnq63uNHOTa6zmomp7EQUAGmbr24DIcOq6TdZHUIn5vJntkQySrQod7B43K%2FprtoKFRGlvxE1uLiVGovviOuKI%2FyG5Wz%2BW8toob5X7tUo%2BCwtA3qyWVEnfeIEacoSyI8Af3CFfj7YlkDrpSfneI7Uow3D2MIdpe86EC9kgfNADYSugTyb5izo3VhEKZYpKlIkPJq5PCdIOXJL7hjUHLSTJZJ0hQHtEMzw0QTL03eHFomQSPQdMCgdIFdMogWoxlluYVIqCd%2Fb65Zl4DHU3UykZPrH1kMui20RkNaSkfsACarp7bOB29jq9DpekW9V204fDA3bdAPJ6I8%2Fi4%2BNIV07UQH0El6gnS%2BhE%2F%2FwNRvFNL3hk4RhTs9hG2Yu7Fw9I0GsKwwYpV4gDfB9uJxzye94%2FB5qK3GmwRv%2BNMZmk%2B5khDlkYV5yCv8%2FofN9fERBivhlXwVu2z6Ok8hnXnPXci47m1iNkcaMyDRH3gydts88DalflV6DMLQ%2BRiLYcJD85l%2F9Z5aVTHFvCX7AFp9p0XPUGNWxZv4t22wJKpsAFEJ5Tgfdwot8DXzY5XJroQtmE77XSMaWJmvb0Yb9vrBgLK%2FR81ukFr%2B1ysLvTY9iWyV5nOFKQw1vj2vAY6pgFpP%2FXVcEr9dld%2Bx9AwnUBOulXYAuMcJNsHdCn1GKnv8jN63ypr1mxHxjyx%2BbpILy75XccPJIB2sM74O3oex3wzIZZT8sWaqW2AwKgPF7T5kqwG%2BCmZINHxN%2Bj%2F7QMnNSJ02dvM%2FtSz6YIp7qLV3J5YcPRfu%2BxDfKUUworSI9%2F17GSFGniGF1JkxHVXyHc0TTh%2BPFvkIhGwKyemJ1FxEeCkvPoirVK4&X-Amz-Signature=6a804924cdbc111a2f6de9084ed6487c9c734e5183704ff7fadc4994d1219f2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKFI5M2B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB32L3e6aoU%2Fzfrj0NriGqX%2BC5xmKSTibvb4o6HciW7tAiEA0sVcBKAXQB6HieNbtzHwmWMmb2OabRFAPpIBcBx6k%2FMqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHLdw4q4F0mZqHI14ircA6aXjlLKlUjHqALsxvrEHW8%2Fsnx%2FQyt%2BaaRBpv3i5k767M8scRkwpAVuaC499BCX7hOyCNCq5R2Ff4rrcXucQJjy2lSfHJ%2F0LmxfXPijvo9QBcc%2F0Lz1xAo3Zpiuj0LuitiCfLcpUizxylz2a1CO6FN3GG1xept3Qb3RG9IvHs2caTfEwlpWOAEAxJY0UqSFGA1ngt4FiS6li8VdPwRNBCgJh%2BwhmpJnKzJuaeEBG10Wu8dQBTTPjRZcgVJExVmRVbnJuxyvDtoHbrRNWFPjGSusIyMXS6QRglLwINW9rEB%2BeYN0I4WZ3w%2FnuIuRrb87YFl%2B8FkE40eJmqK2ngeHLFKdC4CNhvRYfXGqGhk1a2QeJSI5HQgRdgIYqswftyTG4FL6YRfHrcci2smqIMuhOCbOcmLzn%2FIYGxtx208PjDo1G1DMkVTTHSmfiw5mbi6RX%2Bax7Oa2TjhSpb4Tn1CNa7TGFBxRaForLmLNnuK012LvveiCSZPj%2FOBclv4cTj2UDFQkioH4OVYKdT%2B0n4%2BuzzsJInXkBE13OLHDaHRVbDqqdtC4yaJusC0bpOHfUQ7jHBVGdBVqulKPc1lzGPVyPKZZVlJmNfbq7zuu7MJbVNPI8Qk78sLDipZGl8SmMNb49rwGOqUBhwZ%2Bbzgpwx3TqlTQilX3vhGxV8Jx%2B53HDE8ub9%2Bnt%2FmiK%2FOvgfDr9RuDE%2BBhyYRJHfkHnn7xn%2FPxj9RFLCboO6JlsJQMY9leeLI546GF0fz794y92AHdFgLCaBepnlj7q2izQp1C%2BJ2y0yt6BlW28l%2BsDxCkozH4GRN9X95kS8j3INE7xMSpiM7ePIzT1YdtnxkAWqX%2F5g3y0yi2vy4oa%2F84WacZ&X-Amz-Signature=8cb699a6726a5b0e9ef17d8de7055844effb85c11742bd585de090b31fa0dba2&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKFI5M2B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB32L3e6aoU%2Fzfrj0NriGqX%2BC5xmKSTibvb4o6HciW7tAiEA0sVcBKAXQB6HieNbtzHwmWMmb2OabRFAPpIBcBx6k%2FMqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHLdw4q4F0mZqHI14ircA6aXjlLKlUjHqALsxvrEHW8%2Fsnx%2FQyt%2BaaRBpv3i5k767M8scRkwpAVuaC499BCX7hOyCNCq5R2Ff4rrcXucQJjy2lSfHJ%2F0LmxfXPijvo9QBcc%2F0Lz1xAo3Zpiuj0LuitiCfLcpUizxylz2a1CO6FN3GG1xept3Qb3RG9IvHs2caTfEwlpWOAEAxJY0UqSFGA1ngt4FiS6li8VdPwRNBCgJh%2BwhmpJnKzJuaeEBG10Wu8dQBTTPjRZcgVJExVmRVbnJuxyvDtoHbrRNWFPjGSusIyMXS6QRglLwINW9rEB%2BeYN0I4WZ3w%2FnuIuRrb87YFl%2B8FkE40eJmqK2ngeHLFKdC4CNhvRYfXGqGhk1a2QeJSI5HQgRdgIYqswftyTG4FL6YRfHrcci2smqIMuhOCbOcmLzn%2FIYGxtx208PjDo1G1DMkVTTHSmfiw5mbi6RX%2Bax7Oa2TjhSpb4Tn1CNa7TGFBxRaForLmLNnuK012LvveiCSZPj%2FOBclv4cTj2UDFQkioH4OVYKdT%2B0n4%2BuzzsJInXkBE13OLHDaHRVbDqqdtC4yaJusC0bpOHfUQ7jHBVGdBVqulKPc1lzGPVyPKZZVlJmNfbq7zuu7MJbVNPI8Qk78sLDipZGl8SmMNb49rwGOqUBhwZ%2Bbzgpwx3TqlTQilX3vhGxV8Jx%2B53HDE8ub9%2Bnt%2FmiK%2FOvgfDr9RuDE%2BBhyYRJHfkHnn7xn%2FPxj9RFLCboO6JlsJQMY9leeLI546GF0fz794y92AHdFgLCaBepnlj7q2izQp1C%2BJ2y0yt6BlW28l%2BsDxCkozH4GRN9X95kS8j3INE7xMSpiM7ePIzT1YdtnxkAWqX%2F5g3y0yi2vy4oa%2F84WacZ&X-Amz-Signature=382945aab6f747bc0db2bbf7090cfe44e8c895fc05156acb86d793cc3c97a3ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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