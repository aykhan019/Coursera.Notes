

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OTKDJ6G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9I5x%2BjBTPRmonsj8g6OMp9tx6C7AP22Xxsjnk%2BYxTWwIgDJHaKvGHBFg3s4pEdl4hHw4PbE2SBb5Dgedd%2BDYhzEIqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPj%2FyKhd1hFPFl40kircA5Aiha7PGLOt9KiuogKFaWxRBt6cpGz0yLgGRd4jIkFvRrsx2TVHJG%2FwItIPFMvxCcVro5JkPYMibrk%2BbsYw6HR4DROA7mJOJqh%2BkfOFu50SSg9H%2B4YwL50Pn01UxWEew1bOVBSC8B0NJJ2agLwbETBT3CGxbOwZpvtIk42oR48VjOKSFCv65fBBX1OCcFwdBCY97noFf639RahABciJPNf0IiCXvAP%2FdOz0rfUsDN7%2BXYnE%2Fze7puAMDaMzTPzcnZmWnmAlVq9i%2F7fGeRUGtB2sE2j6VlrM9KXxEwF5H%2BaAWxEM6yCqu4JVbWhQwOY2CxRrkUxtf%2F3JCLTXeK9m%2FghYaOIY1u1847ckY8fy27%2BBNkr5gm8g%2BYHGb6zcYqMEJPW6QCDOShriCtmM59OBMM3Jt6PfImOdbTi2pMKKKQpJ0KHUcrJ5j3lQUg5UCqVOuV5ep0vKNIEDWHvCRu0c8GYzA6szicv21uhiBCcJN7Awj0q4I55rG28GkvGaAAgryyEc6BJjRCM6YwtBJztp91iCd81Cpq3Yrp5WP88dYIR6Ata6VyKoUbDjnQwGuB1kHE7O3HHJ5BaaZo4%2B1Rbs23jLlhtL%2BUeNCVqzU7a0hCt6Ti2EP3gOgvbA5uycMPjW8rwGOqUBpVk7WQ0p3OL5BjACDZFhDAk%2BWuuExynJG2w%2BiDoHhaXUT8TvCjV8RK%2FbVqNyAvWZ2JjdZRFycjCrYYadirREwFw1H%2FuDgXrVd%2BoeDB%2FI5w2nHRbxRRKn3GwKR3fij6ONclibw7jVuqgvWlDSK2g1MTftKBEAWNkXancFsTzcax9yei2LSNHWyHL%2FdP3C9FuD%2BdrT1nljnEl%2Bn8ygaA82jrnkI9vF&X-Amz-Signature=a649c0a8e24a161b7beeca66a3bb5d9983a5b4a8f508bb7506c285ab4c822de9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KWVHWUL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKr4pQuIPs8T9aNysMI0q4UA%2F2NUrXLoS%2BLcpUfnzVzQIhAIaQvQOlipaNKERLheNZTE8vQehwj04yNtAE8H0hKhi5KogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgytViuYi7ZEFso0Luwq3ANCFvRR%2F3yrxOiIbeVrlefu4go%2BcnJUcZTu6K6wJaRGXd08xECoSr90CIt6xtmflr020jjrwZnzLbRIpBG42guOXLcXv6FXgbp%2BOEqocor1whUUrPHSLNHSqnVSOZqotpQVGKvqRxZ%2FB7M2FVD2ltAyzYfD%2FIBfRkAsFyz6wN1HsXe2GhkzBVSiN0P3SvoNxxv58bza4Ew1EzycdZAFBAJltaaFDvUTlPfDAA8LX6vaXekMHlGQ1FMA6BzFzGz8ce%2BLF8dRpcF225P4KOi%2FYLraxvYXvUB8OwIKfIdgBeAfxuBIAqkO1PQTwzrapBsq9DULewT1frRDQOcOD2BEO6vRUjAaa7xWfDE8t6gZlriYpMKNU4V4od%2Ft0eJ%2BfppwHPg06Te15WdYrZtO4TBoavdFtBkHBegbvEd9ZzvDjzp67mFJbH4vZ4zjHzchWsrE1KbdsahoViteeNO85gE55FzV251pnk2YNx4%2BzoLUo7iCjOY7dl1TJCZsK81u6xBWpubJ6zTovBwq52sTcz4UIbXj5iD%2FQXXIu9TSJDcQHIgPyUZ%2F1lTy39AXGo32UNJNptwTfcEWpj4Hrtz%2FwhG21ySNEEpURuMhGwA6qVELLYoSVW4mRt7L5%2BAzTWy6VTDo1vK8BjqkARnY6I6qNDb7M22uEs4bE0%2FlATQm77l0K7XCKcqD9xjuowY4TmgDrY63HheyCJXDC0B7Zg%2FLG8oVR0wscbWYzCH2m1gqc%2FJJQIdWEQRWpGi6X9qbq7w%2FgpHlZ8J4EyBxAaKaTP5xMuzZwFOa6HR%2FTjxlPdnVEdbM%2Fzuojn%2BTQn%2FfbqVwBrq%2B03Sd7C0GzUdqIZWKQ1E5BD8XQcc13yTgugftMoa4&X-Amz-Signature=375d3b485ee1c16248b60ffd65fa7f6f987faafa8f1291f671222f9232875a64&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EG4VGRG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBxE26ir%2BTn1YoiYkHHdu5hlGHykgAzKF23hErUygSrJAiB6mkOpP70FdXudkir7r4tZtMMp8Ezuk5%2BhdfJmI4KD6yqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXzLvA6hwQmTSgGPFKtwDaAW7IB7cGPYjWn8JBjXrB4L8unMtlWjCrI0QEOVPRSveO%2F8cKmiaMtXz0vHVaG%2BSnpRMBliy4kZY0iScX87AqPXa3n2JoLtXg%2Bbg%2BKpc58ho9yBLmNcHZ5oMim7aP8f677t6w%2F7SxSpaMQqAU0LPXjw%2FCV0Hj3uGrlRMZZSy6ZLZcrxHuQcQujdwdOj4HpUUYIxsz6XVmXu2wFdsEgJTVNcZN4g%2BDwBt9YZJRFwENJzbuj0O1oWH%2FGTtD6srWY73W4a8L0ERKvs%2FU3cf2GSe%2Bxr6BgPolWKmr1yHbhphdu5k918KCYRT5bvILLLb1ezKzbxINDm%2Fd4T3tB0h8OX2VxYjZ1oRLFdrEVyqp%2Bmr7psl%2FZaDWGlaxiYK1obGSTsXNSBEzaZev5U09xQR2%2FMR0DEeshX7wJK7GbMASPNTJ%2B2d7EV4IdehAFsd1dxV1ZNXBLCDxlyhe2ilvsD36smzKjSO5Qj5EeI9rKIMr2CwVGTNMa8YOFFcLdnXVexfFlQW%2BEHGjSLmzKom4MWWGAhUbAJDXfTj3xvdj9KKxsApEDqj5SR%2F2EbRqCE8eegbI75cUlFCDSlYPxKj%2BE8Lh1X4MC8Q7igqgD9hRhiORvZoJZzme0mYPeqMOnDypbgw1tbyvAY6pgHlVcJmpa4lvujtnS%2FwgzB85YVKG0VOrlTin568%2F2ebDnHqYHz0Dwbzqa0xfj1GTEngXFdLqszX9TZDqC3GK4cTVJoSGg4tVTKyNNXkOlt%2B6SJDSHN%2FnTYjj0KORxNIECiGMDGpg70r2JUqy3zXqEgCfs7ec1R0FD2gdD4ZbEDabs6RL%2Fp9p%2FSlFPHEerl94I3OjoGRU8TWjbk2uLB0Tk189U73%2BcAP&X-Amz-Signature=733a085b204e1bdf56f94adeeead21fda94b2f5360ad77cb9e57253c0277ee79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOZBQ3QJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFAOLYpGfiDrdbuMrzjlh3j%2B0BsAW7cLNhvkl5iCFuMGAiEA%2BSEAsUmC%2BEyQ%2B5w6ZL9io9HRH%2FUMssMiHi4j1%2F6Z2DkqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLJkMGiQxLQQxw0RiCrcA3QbsjOc9Uq2k3%2BWPmIat8fk9lah8cL6cevQ%2BTFioS1mcoBChsoP%2FkQVKNO90lK%2F5KAFKKnrvTJIypCbiUXBDuiOyteIGfAewnJtSvGtmaLm1BvBHp%2Flz8egV1XmI0QPYVMr%2ByWdzUneUsruaYMJVAQoYw8IuCKGkcnuPofNQ9a%2BwKAuy%2BGrzJ8%2BkoQaYxuWpJcZwMc2isbtgxSVNIvUaDPBgcsvrXXkSWOE%2ByMEUfrSnhRccIUje%2BMWS%2BpkMObhq6fs%2FzuH9GG3GNV8MfZkk7nFgrowsSxIW%2FVFmnZcQBUNjpgBi1QVXfWHMpqwKEt%2FRIcnGZJN6hNv7Xpbq9qn4gmQm5k5s6c%2FNF%2FDoeWlffaov1B8VCY0NuPqRCSyc9hkEfq%2BTqEF2%2BuLg4%2B4R38Uw%2FVq%2BNsCd%2BC30dOaEOfZF7EJdQX0lNK%2B9frCfa8Hh%2BTD1Yy7CNlwqC0KtbLlFar0Vp2dDw5eHfV5jQvCS7EoIoiAwNxBtMGwk2CTbHXg0Av0IHP7infu4IrsBseg3OfsBpV11voyWtSfvDTsxEZ5wXVAkwDopXNjOslctGnYbwhWgdh6J1zyeD5Y4QuBiNmlRCP7vdQ%2FP03sZlTzBR3dbuJwaYtmYzIOJzAdobhWMPrW8rwGOqUBgh5OXM3dmmLy6uiV64HXSfIKLNww3XDVGmwChZTPH5%2FkzFm27gvGvXezlnDjiRECEzWYaBxWX1Qn%2FC%2FzxhVCJVt6KfSFUS4OipLA8y72Z%2BeUntjgMjqqVCfmaulGoGHM31t6CJam7zkTCMP%2FTZOTHA1fsBe%2BIMGCr%2FeSodsv9t11uBO2LRpPmLhAVFszoxvhegWtoxXZIUnlaJlYuLTHyjHqTuvM&X-Amz-Signature=dde12a08b0be655c1ecc5b6e9f7789145b15e257f6b0441e16e489a9a9e0098d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5UAOH5J%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAZnDBh61SYjmDij0cSPmNuClVicbec87zqgdLJp0aq4AiEAsEIFxzsPCd5senv0pvL2VpwGCUyvTUnP199d%2F%2FXfangqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNXCpzb5NYZxqcLJ3ircA8pn%2FPMWpt7zkvZEzGCeDbXRv6y9PxpRFmCmgwYXeR0qknci5Ird1pARJDzbdBzmX9n%2BtwBiQmxUwoNZgm%2Fl8wDZMXsbHaITb6XjP5Uy%2B%2FisMr7aG%2FH%2B1OlVW5GY6VRsHsCwUV75hqZPQjf5GFWb1CMO0ytDVWFzBnzMyCn3LW%2Fc3U0%2B9S7xBy4g6sQwcoxV81MLpanWCzllEY00vC%2B5%2F%2BULlR%2FeMt5k4MeMaHU35eUnQEsOXGmjm2uir9wfR7IGagFEeZUaezvt3Bdpdoe4U6lSarPvXKSKK8EHUDf14p8z5oPwVxUfYCO9ht5SbqGg8%2FUbELTEOvHkzFs0l6LpeHB2pqBpsi1IZ4r5KFXj6WO2juxrSWPw4DyRfnT4hRLBc1Jp1iGoZag8jpk8GjJhCcUrLHRF4P6PhQGQ2zrpdDD5COmOhKy%2FgFLuda%2BRH3MSzeDpLUeg%2FrStS%2BqtcC58Z03Q28ktqhy135O6hm688HZcD38%2BaiS4RCfa3KWpBLR0%2FcUBYHn0%2FGoQ4BRh0QYNo3CEQpJtOtSIWKWFn%2Bw3uyx6l6tSQN84Q4dk17K81kbeINygdvy19EmLOb66fB%2FaK%2B57ZjGNR1ZhwbjOItxMRpPlab2DOrqGyzdiu%2FQPMJPX8rwGOqUB4in62DR8%2F%2BGTYpzUzjF5fkEPHzfxhS9Ki9f4h3KYjw%2BZr%2BujmW%2BdByU%2FkZkVP2h69%2BOiGmtXw2EVLU4HfFgObhhQ%2BkR0Utxqjm6uBKRr4D%2FuBGolpFjkKTCGbmEGmbALsu641d66r%2FFVgNUY3V5bGv19UuQteMz5DJ%2BVt23YtRzxsz7d%2FEbYMftNQnnDJ%2BVoMqSIMDdfwz%2FtNNXTbLkK%2FEOH49Hd&X-Amz-Signature=debf9760a1083a46b04d24243aa3229e0557223ed5bd8d4f1fe5913a732cd8b9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y67EEI5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFJzOije4HWWUGDK%2Fj5ASkAk%2BQgkiQE5mh9OQf2vQJcAIgNOiNWJUh4rEkmu88EunTy%2BXC0XfgnQbi3%2FNzrPKu%2FH0qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFkKrSzluwBef7OrYyrcA85J7100phmTiypboFRT4e4vbGe9CXx08yXHXYlOqTeWfFXp3Hcru0X%2BZkPrv9RZPx7OgQtDdFriGASzEGbpMp4S4HrcJZXIuJqXLcPrlGzSnN5pfUDjJMuSGFNTV7WH2V9rDJzRO%2BrrcAa0ygHQX2ySh%2FnMkx%2FOOdTw0Hg1XeCaCXyJC%2BQrJhM5ETcR8a2cs%2BCJeKFA5XaBWjcvsksmHF96lWvZMQ8zwpX2JMR%2F%2FK%2BI3z5qhEW3JK%2FHcPinGvZFbVvs7vdEHwapC40TWWcVn8dda2I3Fo%2FDCgTRmZeXWsDsLt357T4JHsnLl5MT7i6N7CCruFoYKJXmk%2B4kiw5ND1jjErmIE4TmXz5f7ewfpKCilhDwrG%2BQ7%2BxpZeglgayvqP47XKuQMecR0Xg2VRZDpQSB3fDFzu9fHFv9p6ii4owH%2BSjCPCG6llFOtLsWBIznnjTtQNpHREEEBTVphsRvxWGKRWHLlpVsL9M%2BAxAw7jVe6j7%2FzfeNA3pHMABdVLywB3mtk9LxvmYfl08f7PG6D0PT6Z9rEvg4uBZWu%2BywjsM8SPR7V4rcr0E8uXrFltFL%2BFzJGGZDGn%2BtxdoGasfItWKyxg2ukOk9EqOslu5ImNH%2BHx4I%2FhwFHYP61LNnMMTW8rwGOqUBSDJe06d8cu79cr8TGZcv7dAxgRpHhk1Z6%2FfECXclTjS7uZo03uOrtvXnn%2BTkPgc0ZTBV%2B2szPS87KyZbqfD27kF0Bcf7crppMmy3PdWWynFr3cCsJrqKop68KBNsANin8BJfcEQ58CSQ3dhB1KQLpgQDFUaA3KuWyM2nksawE3%2BTAQXJfNCckHZGQMLcaVftE2FNsihYVn4pUQepJwXnWjsI%2FdI%2F&X-Amz-Signature=5ac29ee091dfed6292eaaab6e8d301adb1afd2fb6a945383478b5d8a7be20af3&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCLDWIAA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FBsVOUhH7yQlFaKU0tyWncXfYv0cMqbIddzTBzm0SbQIhAJLr2rQFiCuqrFysC8fYOhvo18s88YQeLk8FuUiyjIMkKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5M%2FPkh5WXuFBmhYMq3AOlvAdYO63i7f1Mu9kSt93H6kKFJf8tuehu3F6nzQ%2BnKgBmX6eraUv6uDaT%2FCIav63CpTdWTLpcy1UYNbtazygdrGA7OY9%2BwRcujREX0LsI35zn4tceE5UjQAzzpwp%2BmvFCqIWgdHQDjYI4OdK36g0d%2BE93MAKsgO1%2FydgHs4f%2FYRjkxk0aCfzwX%2BkFXjz4n1psUkFoLyEr5htLq8eBnTtlqGt7MwA2IYtoDPLCc1ld7cCpjbG91jdob77NyxEYUnvaPX1Gr3aM0EbPDan6bC780%2B9zK1ZHdQkN8oBOyXq%2FY%2BI3luK2BHrlL0erlrvRJOs9PxLlimnsuEtN8XGZyUg5%2Bd7Az40kVK%2Fc1rWA0iRNf2E7HJN67KhS%2B5vuCYrkihPzuZ7PdD%2FoUltZv9DwdSD350wFmqZbgiq5YFzY5Eu9XIfNp4hT%2FmQSg05wGiAlbnE%2Bg4UN3q6DcH6w6bYKl1Tp6q94nT3polvxKEeaVKeOZ3E3tDEpAs%2Fs1hLrKtDdHK%2F5rNLofidLcPP4kBWExF1ZbrjTvcy2FiglwfZ2ta%2BxSD1LnDRz7PsmO0ORLc72P2uy4h86nySOHN0B%2BabhbiL8N%2F%2BldQ9qQdBm1f73VURADqrdcsd1mQHbB%2F%2B5VzCT1%2FK8BjqkAdJrFHxnHUq9XQYnKroUWoogBLhN1ZNVm6boRkDq5NZzy7MR7tGYfu3XRB%2Bsq8eOxYwPOyjSR8EK4hibMJK9RzqO%2B4kagJMsTHI%2BKpslaPjN0ZDliaxCZwuEj3lG%2FT2mhf6%2BBGKpN3iTMYcKxZiWL8xjYYbuqfn6NBOUfMKg8ko0rxo45dopQEC0%2FUZpdDpvZLwH%2FYyw83PuHdPSJYj%2FbfBoIXLs&X-Amz-Signature=a190926c6f33a237c8fb95fcfaa096fdcc53b345cdeb83fe2c21694bd6ba46d9&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6RMVUTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAwTiw4GhZBccaNLwwuKHfbTZ4ACiQbyIuHNMnyYjHInAiEA9A%2BHDiOyKTshkPBZ6qXPPXzf2Qte9UnBPSugnMtigdwqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHotxv5xgkUkqJkyZSrcA9ejqEMhEH71RkQZyjJuC4YvPehxkulLVcUAB4u4zo%2B2ROo4vE%2F21meQ5ru0mbJO76AH5fSSYvnJYziHc182SI3S0tD1ol5gpQb%2Fj8rt5Mf8CX1x7Dy%2BFOTsH9%2BQIyXymFPlfx%2Ferd6Hl7AxFzGD1LTx9cwtHjdQoZxf4iy9ryI1TQ%2FShh1ord%2BCxeGgVViPYtObatTK22lBE6E25Z7B3t7lxT8dH3hRFMc1k5azanK6FmnQok0ilmN0hZ8QfJiDpxCffDSyYlg%2FWZFq%2BwIJ%2FhtniiS2kREHmCHA9J8Fai2YsjEhlKbBPzwpcd%2Bxuy44m10KJqFqq3VfU0Loj8AQMLpbRTlJexX%2FTD5aoGJHjk3qEMAMnH9wakekArPba5bBSnTTCE6jG5Bt%2Bfa2UnHHSIdgAK8%2FG7ugk2X%2FZxqekledh94GPJVeeOQx4Rs%2BK5TiSPC%2FW6KJz28LKvo1N3hlisfmtfcfcPLfWWGKq%2FzAvF2rJZNBDG8X9hWdaKB%2FclDCG81iTYjJw3C80sr81N8dgPzM6HUtPeqCmzfl6ySI%2BATrowSTcyXhmoUqMp8WV6SOfr4VJQW5EOnHCQpqixdFoivlI%2B42v3mFRSrM8RWbhl1teAmx7RQJKu0oO6LBMPnW8rwGOqUBe9J6FUugjPOJZ3BxJPunjICZh%2Fvs67bZBNUC5W8mRPCZHp1MZJQbsPQfBYRwwgxBZAy5WxI5vow8l93HPZIWJmngWbhww2GMHJGLud26ReIBdcbMDML3%2BeREPnRDlhYKwdNYJYuWE%2Fye4HjSWJ7TNudt0IQr2lTHYK3F2%2Fz%2FZop6hXcNgQwB%2F2MDtYFCEs1GIoKxoLuU5Pwi%2B1wYJVo0luwOsiN%2B&X-Amz-Signature=87d32d2f709481a2fc0e27d92ccfa12966248c64d6d06953024bdfd7b1b3e9a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5UAOH5J%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAZnDBh61SYjmDij0cSPmNuClVicbec87zqgdLJp0aq4AiEAsEIFxzsPCd5senv0pvL2VpwGCUyvTUnP199d%2F%2FXfangqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNXCpzb5NYZxqcLJ3ircA8pn%2FPMWpt7zkvZEzGCeDbXRv6y9PxpRFmCmgwYXeR0qknci5Ird1pARJDzbdBzmX9n%2BtwBiQmxUwoNZgm%2Fl8wDZMXsbHaITb6XjP5Uy%2B%2FisMr7aG%2FH%2B1OlVW5GY6VRsHsCwUV75hqZPQjf5GFWb1CMO0ytDVWFzBnzMyCn3LW%2Fc3U0%2B9S7xBy4g6sQwcoxV81MLpanWCzllEY00vC%2B5%2F%2BULlR%2FeMt5k4MeMaHU35eUnQEsOXGmjm2uir9wfR7IGagFEeZUaezvt3Bdpdoe4U6lSarPvXKSKK8EHUDf14p8z5oPwVxUfYCO9ht5SbqGg8%2FUbELTEOvHkzFs0l6LpeHB2pqBpsi1IZ4r5KFXj6WO2juxrSWPw4DyRfnT4hRLBc1Jp1iGoZag8jpk8GjJhCcUrLHRF4P6PhQGQ2zrpdDD5COmOhKy%2FgFLuda%2BRH3MSzeDpLUeg%2FrStS%2BqtcC58Z03Q28ktqhy135O6hm688HZcD38%2BaiS4RCfa3KWpBLR0%2FcUBYHn0%2FGoQ4BRh0QYNo3CEQpJtOtSIWKWFn%2Bw3uyx6l6tSQN84Q4dk17K81kbeINygdvy19EmLOb66fB%2FaK%2B57ZjGNR1ZhwbjOItxMRpPlab2DOrqGyzdiu%2FQPMJPX8rwGOqUB4in62DR8%2F%2BGTYpzUzjF5fkEPHzfxhS9Ki9f4h3KYjw%2BZr%2BujmW%2BdByU%2FkZkVP2h69%2BOiGmtXw2EVLU4HfFgObhhQ%2BkR0Utxqjm6uBKRr4D%2FuBGolpFjkKTCGbmEGmbALsu641d66r%2FFVgNUY3V5bGv19UuQteMz5DJ%2BVt23YtRzxsz7d%2FEbYMftNQnnDJ%2BVoMqSIMDdfwz%2FtNNXTbLkK%2FEOH49Hd&X-Amz-Signature=0175d60514e4cac12c172e72da69fc2fd13bf06cd57a9031320e7ac80204e27b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF4TI6IE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICy3tqDNP0r2rKbGl0GAuxFpFuHN%2FDrew8OKAfy2AdjUAiB54YRy4iw%2FK21zEu21L31%2B53QWG0fy0gJv7HzNiqdnVCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMk%2Fuszdk3gEFP1JRBKtwDS0kQOnq%2FCeHc3YQZs1lS2D6FXh3PU84pLNe3o1AXaR0ETSLaE%2FrpQwMgyqP017Zr3%2FpRbdQ5Ns30835qJrUdDfLLPiXESVKpvrUsYZxlbkgKnfEe4YvebnDN2WIxR%2BiJ5a4%2FuRE%2Biq68O3So7wKchch%2BZbFxVOlhk1vwtZLrnMiO1AaxQ6xvep98oNxlPLF3l%2FCq88W3fsk%2BaD3rMGKwcPiUc8uZBXiDA%2BxCpZedaLFy6iUDS7OJm4Qp%2B6bY9McFmFquqrK%2FAnPdYxOrpMoe%2F325WeC4rLfLTIuTZFpfFJwkEqXhEe1FZqYlvGiHp51ucJtxVGLWx1yijF5trJmxN4KBwAJg3mc9pGhmtIejb1S0E1gzDpyfuU3u%2BrmPMJFDT1CCfPLrQok3T%2Bj720R1%2FZyGFd4YjGlG1vSC8J0Ujupv8Z29vkoPyGZp9WUCC9H2IvQ3SGxQV%2FLlMy4TxwY0BBREWI7Ds2SYK4OBkjw9lLx8XhFNWlun%2FC24rMcbKFUoRzogW1XjkCrn5MbjBvqWOLd1zumLJ3DweunNNkgXLH5IPPFZVIkO2nk%2FDJj%2BlEDsdYLWT7GpHL37Ega5qIzsOv0fVLBSDshk4jwyiW%2BehspWAznQAYKy7A0lXqgw59byvAY6pgGU%2FXbX%2B9BO7fsZo5%2BifGqSKHmMk7uIvVmI8N%2Bf3Y%2FWh%2Fanj9lppYvkBqnamYysw5mgFjmPI7Tfz3sVbtZ1wzPgXd7bFB8C7lHHuaR3JafGI%2BZNoXBxUYyoLow%2FTFAGKJ8EvBgef4bc01cV6MO4iBHwazKcQLd7KcTjF9uyPFGMtoUcxSjHfisjdVWuLpp4cKSgOgm8qaWV4vRdCInZ5ogk3r1MbFYO&X-Amz-Signature=66048881fafff3e23dc0382bef82a047aacc9b2499742dc04a072c3561d589e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF4TI6IE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICy3tqDNP0r2rKbGl0GAuxFpFuHN%2FDrew8OKAfy2AdjUAiB54YRy4iw%2FK21zEu21L31%2B53QWG0fy0gJv7HzNiqdnVCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMk%2Fuszdk3gEFP1JRBKtwDS0kQOnq%2FCeHc3YQZs1lS2D6FXh3PU84pLNe3o1AXaR0ETSLaE%2FrpQwMgyqP017Zr3%2FpRbdQ5Ns30835qJrUdDfLLPiXESVKpvrUsYZxlbkgKnfEe4YvebnDN2WIxR%2BiJ5a4%2FuRE%2Biq68O3So7wKchch%2BZbFxVOlhk1vwtZLrnMiO1AaxQ6xvep98oNxlPLF3l%2FCq88W3fsk%2BaD3rMGKwcPiUc8uZBXiDA%2BxCpZedaLFy6iUDS7OJm4Qp%2B6bY9McFmFquqrK%2FAnPdYxOrpMoe%2F325WeC4rLfLTIuTZFpfFJwkEqXhEe1FZqYlvGiHp51ucJtxVGLWx1yijF5trJmxN4KBwAJg3mc9pGhmtIejb1S0E1gzDpyfuU3u%2BrmPMJFDT1CCfPLrQok3T%2Bj720R1%2FZyGFd4YjGlG1vSC8J0Ujupv8Z29vkoPyGZp9WUCC9H2IvQ3SGxQV%2FLlMy4TxwY0BBREWI7Ds2SYK4OBkjw9lLx8XhFNWlun%2FC24rMcbKFUoRzogW1XjkCrn5MbjBvqWOLd1zumLJ3DweunNNkgXLH5IPPFZVIkO2nk%2FDJj%2BlEDsdYLWT7GpHL37Ega5qIzsOv0fVLBSDshk4jwyiW%2BehspWAznQAYKy7A0lXqgw59byvAY6pgGU%2FXbX%2B9BO7fsZo5%2BifGqSKHmMk7uIvVmI8N%2Bf3Y%2FWh%2Fanj9lppYvkBqnamYysw5mgFjmPI7Tfz3sVbtZ1wzPgXd7bFB8C7lHHuaR3JafGI%2BZNoXBxUYyoLow%2FTFAGKJ8EvBgef4bc01cV6MO4iBHwazKcQLd7KcTjF9uyPFGMtoUcxSjHfisjdVWuLpp4cKSgOgm8qaWV4vRdCInZ5ogk3r1MbFYO&X-Amz-Signature=c23303394f34d2f514e40f6ee26feef5184335764e8d52c58d7092e3e5bd91c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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