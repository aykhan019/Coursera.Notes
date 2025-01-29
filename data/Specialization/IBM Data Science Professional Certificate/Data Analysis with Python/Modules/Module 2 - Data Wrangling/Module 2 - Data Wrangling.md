

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU24JYVF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDa3tw5zPvc8YHisme1Zf6rixHnoRQGn26wA2EF3HvlgwIgSe69rvPTAvz0JXGmwYtUCLoVF22EGlYvUbozccdt8b4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMHkcDzxgEOzePQoJCrcA3fao8dFC2LV348updE%2BlfsdMhLRnIy6UgFtZvjZnVPZ7lmRAX1v60%2F%2F82cbWVvW0f%2BJAyujIYRKAlSfuoJdxO%2F57JwL6NnpNfLFYNBKaRU89i5L%2ByiLIqizm1Xci544TtY1htDte17EdzefmGnO7bFU8TpbxNp5MzsX%2FYvsiWygeafLvgF8Td4mguDrWdoTgH4Zp7fdfHcIFU7YdQfEM6d8BSgAk28xQnH%2Bp4snsfVlDH8rsHlgfwKrBCYoal3eUMzVKZs%2Bxm9q3bLe1u9YvNQjk5Nwzx2hqKPgOmwLcG%2Fe2fdJg4QQw2qFtI9UGY%2BxlK9zQyGaUS66deZn0urdIE8fLLeDJJGi4oBP8K5OtiggikEpB4ZtrobVh7J4v%2FQl2nDqfW32AUt42p4OaVxy%2FK2qnalYjaONoEF6be%2Bm9GA5VKjIXPgjldDVirgqMgdRLr0qy8Bl2Dz7uq3cORtI1sj2pGmjGBHnYgqhwqaTcQv8uwcxekbg%2FCvzGrrC5FfoQAAEUIqTuz4e7Bu4oY6zhvLOGUhxku8V6oFpdc%2BMIXSu6h0R2iKfMTBC6%2FIW%2F2YTD%2FcHPpIJHL7za72DyBNoyrcP9i6gKNUT1b31H%2BpRfwB%2FnkCTL%2F%2FXHELN%2F%2BBzMJa75rwGOqUBgV0G7Zitne%2FaRoeU7lDxFpJGDVBpgtmkh%2FzlwWmIfYtvU3S9yOaCGg498P%2F2PmtZNBqIWDR14HkecRR5uWsnZTWU2EmS6l2C0jmvZAzlzOxykbfPVN5UflC6v920p6yLhZ%2BzB1Xqm9UWcsU4OpehIXDggS7URruHU8iB1%2BRON3bd6lmJJ%2FYc06gx5%2FHtRBAgduoKZlrSvT93gTnX%2B6D4eUyc8soy&X-Amz-Signature=078afc687d18f13960e27b44cf54d755ed2226d69e01ea7b1c0bc00166b1bd87&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BR3NJPB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIHMtj%2FH%2BpV1KRCMELqD%2FdTSykvjUkOx4wPxEEvnCr6glAiBjFy47Bo8Xf2XZYYfVl26hL6%2BSna7RCX7zXeRVsYBTxCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Fptz2EssIfki1BALKtwD54IwiH0CXKWqYH0c2cTElmE3MAI33T%2BFQ7tvRFWppVtesmVohWjNrKDPqmZ9mu0sddl1AMrnPX%2BMzq1RVVvPRrhHgnUMN1iFL4uFlNnGHo1MkjCuMflkunYkLDX3UeQM6gGRdpCSleGZ8By1xknbIAAkiTM6h%2B5g3GY0sqw6E%2FPjacA6mL3O9JzsVtRKBuF4l2vDIjUEVa8SaKX9QGspr3vtvyBo4PGJei3cbkZA3pFyqNHeNaLOu5Jg%2BPnpRkYQe9mwuv65uJst%2FFvK4RNvWtVw4TNw40D6RKPYFQapNuxiwGDNPndr6pVam83FJ%2BnloAdho3pOM7hEdIq8RnMRR%2B8Ayx9Ju4R19CA6%2BHjhlxPJSOD8YKTIFDXZ46CVHUVtYQjouiPkpwBxVp%2BH%2FvQA%2FAGCEqMAPVnpMGQj3Zqu%2Fucb%2FqIVZQdRUiwOYgZ85AMSbLqESwAfKXn5KPTKotJ6%2FgZ2vUBAfnC6pur2q6%2FIJncVFVdH6P24HWkpDAoUYEGlsHl16ELZf7y0L%2FErm1WKwNl%2FribmPNex8w%2BPk1LRFxoxZDEWG8QkO52vp3LBiUzxpuHntwirmP5P0H8zV56SretSkDLE39IdF2AUZMaodNUCO8Tn6X9iv6TqsNAwzLvmvAY6pgGYAqmkM2NeuGI%2FcmdVviEb3Fp9puG84i6gRmuyYW9LNlKeqOoTSZwqBdacBu%2BxK5lyd9jZN7lZLT8sf5bueaGZ8EDGco65nt0qZ44XoeX%2FWhYx92JQS%2BvoEAkAlDioR4C5hoRcj12%2FkY%2FfQRYq4m%2Fiux1uiwtecjUOQvca6u8u1cicll1XyiJR6eO1BPos6nQbQFrvXgCnilSIrXYCNKuTNhx2HxPd&X-Amz-Signature=6013b4164b5120ce3e681c47216b0572318fcec7722c794c085907a60e41d91c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666T3AV77L%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIEeVC%2B9sbJz6G6sGrfjflVqonB%2F%2FyjfIV5TvbiCQO8OzAiAiqLge70DBjsAzydaWb6yYEWs5wPF8%2Bqu7NQPjSvjaDiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBoRvz26ICzPmPG4dKtwD85evJQ4laeSM6hHAY9Aj4e7hhGiFsCPjZkIi01cV9aDw0tXuS2xr%2FB3b3UgKPzMt4j8idj1UeJfjIvhAZY5PfD8qHiBEZi9op8zPd68kwkmMaRK740wKvfWcLmm7rzmJrUydr%2BcbQH1%2FTuL3asqE%2FmRsh95D3kqhoxogROQ1leY45igpjroDqaKwj8KuHMoGfO2x%2BWyXs8pYqKJDauJ%2FhEJP4FxJo1lGIHTZMvmKbAWXJ4oQeGH8eSeFbbLZZZ%2FnhXUJrZJCcDoQlTEVrz8BGu%2FnRETEojSPQunUViR6PFGMz60KMZRNj2xsCBO8vMbIZ0640%2Bp6NJnEJEAhBP4UjCmwwksSJ3Sbhn5NzSKmKZR%2BXOUnz14LqkAemC5ss8U22j%2BG22tBud8f%2Baz98H%2FuvgsjNA36DhjiYiYYuJIptKLhw9%2FmS5nxLF%2BZvITbpmdkfg21%2FanH3JMy%2BsVSHvtS5%2FJDRe%2FkiiUTJVteedo8jM7EUipkzLcCHpAUxEsV4H8d7EoRpE39WjN9I5OWo%2BfbvXgWAYo9IuEhG%2BaFIXcBxHPFuys0wr12pfAs9LXSE3mRRXUDnCMmyfj8ugmNEgBBxC4U1hDFCBkyLaHnT9byBC%2Fxsn6fxUpgyd51TL4w3brmvAY6pgHOHWzAeRWa5jj1VU5uslfXO8tx8TYuUBOoJBlFrsTsyjx%2FbSbTFCDXhBjI2NrTKc0NSxLNYMKtUExfzXEOuVZ5dj5ejO%2BuSoBSh6%2FRoTsVTCExuGk011mCGa7ri1wkxfhHmiwaZSRvjs1tf0YNuVPL3t5KGPQBD0wuBCEAJmBRReqlueBenJkaJ%2FTMWzVn0bXXC0T%2BudfbcJwyJBp8r4GA78T%2Fvqm%2F&X-Amz-Signature=f343e7f8202c4b7ebb485b44b50054abfc2d34f1743d04c842a03031f660e4ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664B645KGK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQC9QpwyLVnI%2BGto2OhbNvGJYd7rmW0i9mnYGdAlzHycfgIhAOlfYWFoK5prLzQPyIr6IvHdlJpyOWk6tLqOltQZRsVtKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPwDVPXJkEBHdxijMq3ANj%2BjEToi3oIxVzCuuCIwlaxeDRFMXDeXyrBQWAFWQL14d2Dn5bHSL1S2ltLmGW0Fobtnk9Tqgrr2PrR5d7xq9kkMlVR3RKlmsc5QE7rUHHBb9Kw12c6T3KWmnFLHMRf4eglOB1bt1pI0lo9BrwOb4d66k6sSHzoYcNLqMO2B%2FjvbmqN3YlJoH%2F23dOaqtD3Le1VlYOnWeZzg6jsRpUYHjaFfPJsGa074WuGxqFlYN4kN6Bw1QgABi%2BfHh6ZzbLSw0fpoSY%2Bf4gkD3IqUGp7Z2Tb%2FP5ZsLLYHg6LcILZLd4XLzRojbfykPqXO4UOR1b9PnHUMS2%2FAvNc0lOBjzqIBJprPA%2FqW7tvZO4y1vlsit8kPZ0jB74V4MYkHO7Jh323PQG5dZ11%2FLY4Xy3AZ8WWzWGe2KcDzOaKp3KPtHoV4f65vS4yqNCGTUVLM%2Fz0vo5DwzcfXqjocXtOSxsxRpmMEfkx7esfqPnFCzUUdoOiRTKctxOzy9W%2FB7h7EEZlwwhiP7CgMK%2FroRFFZyzQcZ%2FQ%2B16kkkBWPlaQqdfmLr2xT%2Be3aliCxmrN6DYhDxM6wavqyEyeBucejhm7uivDxckyWx0c31fZsBZMsWzHsbfq38fphjtpD785l22x6vcCzCqu%2Ba8BjqkATCd3FFDJLtap3pzVcp3Mcu8ID5CJ5JZd%2FET11QqutnP91bqaxN7plYm80e39%2FjMVvg6ISWUJwnmSaAMNa8kW0CkarCiZHpCj7%2FF%2Bk%2B49vgdMkkHYOl3PGnM%2B0zBdhqoQ3Yy94HxgEbJBIB%2BwXkXeZxFG1MCG%2FGJw2HkOfcEGA952QezVnu0GZ2d3tMJ8qFsVjkJPFrwziwfge1Xam02%2BmmPRTZY&X-Amz-Signature=c80527e42dae7500b60b3c5d36688326f7f79d0cc3def74fdbcf62441ec5c54d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPZIQYT4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQD907E%2FhOTk1NcWkPNZJvT6k0u9jjl1qb8Cr1%2FXrSa5cAIhAOVXeCcoM%2FiLvdCJ1TSXc6msXTs6eY37eGPsHRMSaDG4KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzC%2FM6%2FNEiCFKb8Fk8q3APShOMRN1gxzDob1bykNpgCAdkwk063N5SdKsy%2BZJpWj34lyomXmVRbTYpRWtz4jIg1ClbFdUTdbq1Akvw%2B%2FWwBJCLQJbJUI4IPcjt4fRoKH4c3hfumxQgvl287GLwiGGcIlJBmk8zL2r5TztogtJSnlI6QbTnjmhlNOKAVE2I8J4tiZVpgmISKqRu3pv8lyMl5SFwsgJs%2FzTin0PU%2F2%2FO6AyUMrQhZOoKeWKi7miURHEx6NzME58bPinTN4y4UlNQ8SyQW8LKwaLfWA5yE0JhFWMiv1rFoiqgmlXkuXrHrgZ1dk8k6J7TQ0RSZIO1TBB3oMCmoyuWOy4ZYB5neE4o9JBDC6RRlbVG%2Bg5HBWq0cXZYfKvfXeOfsCQOOEUHaCnvhnHuAHBkJo8IK8RDDXPw71Z4IQHd8KQ0vqW%2FOre8vONJLKWigv86QV85YJLtgtJvkmpRIe09o5LhbPJO7Yi%2Bz3hbWnodzNfVprDFQhShnUrnTl5WQG91SY%2Bc4TfXBVRsi%2FK50v4c0YpOuO5i%2F81Lj02tgZ%2FdK8ApXcoVZBhTzoyEre%2FqG9YIO2Td%2B%2BXO8pdZ47NvUItU52nFfsDWK3zZ9nOM38XfAxmPoje6U%2Ffq6wUQuMRuE9y0Vott4RDCHu%2Ba8BjqkAdqgMqM%2FGoIkAWz3OR3sqr2MaNkzAsBi%2BAer23nGm22v70Nn3ExHX0DBa6Woxxaxx0xiCQRRge%2BWNiqSidAfKBOAJobDH9ZVfAfGpk2hlIJJF1E%2FDqs2C07FnaFzEuTBuo3goFl%2FHzDuFWabdKGw14v8DesUtJXzs%2B9uMFwxtQwgkqISZC%2F8eeLX1nYR0nGtVTqlkbfUGHeMu65yERsQ2lXGFERc&X-Amz-Signature=5fcbb128b0cabb94d9bb75d3323143396063b081b8f2803dca7bd4cf4a014d36&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFOPP4I6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICKdledswEaPFY8DbhoD4JaAgJavdsadw%2By8HG%2BiFGcWAiBbbJxhBl5iTL%2FyquzK0S7QSlqi3n6SyCwK0MR1avcd9CqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdPznhsaP7c5DJdzLKtwDsZFoUcf8BM8Q7S8bdLsIQOG7zsRMd%2FbvDPM65Xf1NxczkP25EyC%2B0lT1jc9wNvxBufyoqQTqspn1%2B6G7j39vmMiXKkDAij0WemnWSh2VGBDg1knHRoi2m8l%2F8JpSfwPZfZgBEgMEYEFYuo%2B09wxQ4Rbw49yE1AktZapEm9gZ2vWrDFiZHFU3lPC2OnIVJoxIwA9qwvSX24Sg9onJUyoiu2p%2FJL4LlKZfki0pb602QqGu5hcYseomgUbppckwKf2Ab1kfI5WxfTER5SqOSYxTucujPmw1NspSMtS4LovxK9KFEXVnrfbzEHcZQqHUIuv4igKaxvMPI%2FDnTPV%2BJgy5%2FOsKOYM8sMAKD8OS%2BDalHiUi57ujPZcsRBTp8EPxTpPsFEv2R39GFvURFbLkwaX%2BNNuKtjUBS%2Fm0%2B426gJjRVa9Felhb7rT7%2BUYS2K1bpi7kqfzTpGCwQK4IfOqYGyyfdQY7WH44D6kNy5ZcWbKpQ7twzi0JfodxtRq2IKDosX2Yslx1ttn0AmQZo0cJ8FFr2oV%2Flz5ee0G%2FeKokw54Z7mvRjHp21iUVuxPcAEgP2k7MD04iWWxNXJR9bqgLZUa4QQCIZ0%2Fm8mzGhw2VNoJYosjWUxSGPifzKslx7Jgw%2FrrmvAY6pgFC5I8IvFCPuWs46fVCmrXihNVny%2F0GdUVltHGVpSAyP04sX0bdzi9TtX40rjhtFX8mrQSSHijDCJi6ubC5Za5qf3G50ad5KCCsYRRX1Hfzoe5uaSHbV3kmjIfbJHvAAxj4iPvx0miwqeVvt19oX2tfZC85QbBUZP3O2KbNtVmsLzmAvbF5LlGdVCK7Qbtx17FeCc2kHW0gtQGXKjHa%2FgWCjGVcEUQ9&X-Amz-Signature=6a7d070dcc3b0debe9af8aeb2dc58a6e5bf8f5d41801cbe45d91dd93d5df4b19&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIGBIP7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIF77FBBWSURYAUZi63LUx7swFWmSm9i1wraIIlIPku%2BnAiB6qt1ZNpXbZLOoThEfESau9ztiNIwTdiA%2FQ%2FJyD48Z%2BCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Bhe2KO5AjHxKZPZlKtwDr1yVTT5Fp%2BLsBniqesWg7%2FqBYz9LLUinuaCLLGEdSGLkN14JVjnVBEuQkhudi6KxdGQ%2BQI%2FtFki%2FL8sBQwVnL59nMKLIHb1QZpK6m5rjEl7QpYdKya9Wea0UdNMMT9IKnqS1olShVgzC5n%2BD86les8I0Pn%2FFSdWIlGuZVGEtaQG0zdxARkpZL3G67xzJbMi1CyVnuJfvKoVwq6nDakmGAI9T%2BXExGc58RDPBf1m9g%2FqDhWQ%2BuB4wNsX8iYtI9%2BjwKYjjrquCYquUh3pt6XVwmyocI6igeI1YvkDWaVWq37tBBfjFoFI9N9gtGnZapJE35ZqM%2F9eYQgZQhgaAihzuBefzdhDZ2O0QH3JyZALNHZfHFvuUt2h1xYHFYRaoKBHEBeExssF65FqX9y8ea73XkRF%2FCZMSAIVP510fqkFT652ACzjq8gYKm7SIkYKF0TI350qQ7Owh%2BtL8jCpi9zRhu%2Fi%2FAW6jqt62JEOaHEcP29Doi9W%2B7liVFdJ4jzbM5yO%2F5Sb0Wnwv9Q6sMI9sNXLBpwIyvzg5lKfDY0A9yVM0xSrspc7k3DB4PzRCf11Ji8lPea8ptEe8PhkHJ4KJbgoR41ajMjpLFeDru4sgMFWHQmKUg88%2FUGWkCn9WyLgw5brmvAY6pgHJqOzDV3pxPCS0ro%2BqByuveOorwjvt8nAeXQZ3jF7sUezhKYewpJ2kMDYiJ1dvHX3VMwRaYaLDeDyh87890xFIk38WSo4oJrHrB0oK5wlYKER74q%2FO5%2FiXLhodPqfTdkx5BejOenzAnenxQ00tKGTUGuTIAhB00rjfz2J5H8kxQuk6BE3FukX9xyR%2F49GC8WuYPM2VX8%2FErqMOW9ZWp3BQisbW48rg&X-Amz-Signature=dd09799aa69d562d0393bfb42016ee28faaf1fdf470ef5f4d133e5f0f207b491&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDOKCNOB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDp%2FYPxTYAZqGOY3W%2BaTNdcdva4um0mLXbHWNpQhKJcCgIgXTY4HsSv6Q1y17G9ZbDWahXM%2FoBg7cKnirkv9QcaAPAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEjHRUyLJg8xUpSVdyrcA6p%2Bf4gA7Uwl%2B3Bf9BVyW0nG3MZHuPQ4ozxKiCehFegto9bACDsYVlgxF3knYxkSIP%2Fi5ec%2BXi0jD8kz5xxYcrOO1zoViuRzdEaakLcnS48AvvQEx5igip2IivIJgVjgscnDOAjogY5wHHnyIAba1Rueaa0N31QVsr4LsNLNFD3oOwOoigpB0vuzhnAFOFJ5E%2F1RLajY63LbkI1%2Buv1yUKae0waKeIU7hHsrK%2FjxmlCKnUXVHw%2FFMxGiyJbk8b5Slm8EiYWUo5ZkNAMg%2FeRgad79AosK%2Bou3Km1edOB8nFAqirD8jz9Z1Sjl2snujaK7NrOKB%2FvRQSy5wiVry2qqvm2yjsQba9gyBBXJUySum5WgbBe6rUDiHV5qikOAfndV2D3JEZV5yPLxV2XUa%2BLnNTlNi1%2FYPDtdPtVJcNFYqY2V8Vm%2B4MUOjN0cb53JNYEPjO%2F9nevOg7jg3lTLpFclru4Eb4D4%2F%2BPKcjsctYzcGHceaWDmXRwbuYMcQ5cQFTXwUoyzHvr5LGI3Sy8IR%2BdMt6E0txh9bRiGcpGo5kXbZVFHQwaQc1YlMYZQFZZNi7Nm87rA7GJd4ES9LxTXs5ZhUGC0xIcakcXUrmW%2BozyY6CvaL7wzKf9hAIQtV3SPMJG75rwGOqUBCuIIRMDWkaUZpzqSS8NPbj0JeHZ0Wa%2BfuDZEPuHnmBtC8RYBnddZnNs0mvC%2FonpsBj77NYpOmZ4zS4%2BwEo5MofS3MaBmabNAGZ6Lhe7IIr6WOtEMDg43Kk2bgHVFyC53F%2FNR5sDtUfZfPylq9Q0wqb2TcaiV%2FSHJpEQgUEqQBebqom9oCUSGh8e5lj6opPJCNnrN9zrs3%2F6mKAGNJnlKGleWJUU9&X-Amz-Signature=13cd781a55816ccb105bdb5eaecd6f68da8a4bdf7eca2f233d2b14a2a09062b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPZIQYT4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQD907E%2FhOTk1NcWkPNZJvT6k0u9jjl1qb8Cr1%2FXrSa5cAIhAOVXeCcoM%2FiLvdCJ1TSXc6msXTs6eY37eGPsHRMSaDG4KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzC%2FM6%2FNEiCFKb8Fk8q3APShOMRN1gxzDob1bykNpgCAdkwk063N5SdKsy%2BZJpWj34lyomXmVRbTYpRWtz4jIg1ClbFdUTdbq1Akvw%2B%2FWwBJCLQJbJUI4IPcjt4fRoKH4c3hfumxQgvl287GLwiGGcIlJBmk8zL2r5TztogtJSnlI6QbTnjmhlNOKAVE2I8J4tiZVpgmISKqRu3pv8lyMl5SFwsgJs%2FzTin0PU%2F2%2FO6AyUMrQhZOoKeWKi7miURHEx6NzME58bPinTN4y4UlNQ8SyQW8LKwaLfWA5yE0JhFWMiv1rFoiqgmlXkuXrHrgZ1dk8k6J7TQ0RSZIO1TBB3oMCmoyuWOy4ZYB5neE4o9JBDC6RRlbVG%2Bg5HBWq0cXZYfKvfXeOfsCQOOEUHaCnvhnHuAHBkJo8IK8RDDXPw71Z4IQHd8KQ0vqW%2FOre8vONJLKWigv86QV85YJLtgtJvkmpRIe09o5LhbPJO7Yi%2Bz3hbWnodzNfVprDFQhShnUrnTl5WQG91SY%2Bc4TfXBVRsi%2FK50v4c0YpOuO5i%2F81Lj02tgZ%2FdK8ApXcoVZBhTzoyEre%2FqG9YIO2Td%2B%2BXO8pdZ47NvUItU52nFfsDWK3zZ9nOM38XfAxmPoje6U%2Ffq6wUQuMRuE9y0Vott4RDCHu%2Ba8BjqkAdqgMqM%2FGoIkAWz3OR3sqr2MaNkzAsBi%2BAer23nGm22v70Nn3ExHX0DBa6Woxxaxx0xiCQRRge%2BWNiqSidAfKBOAJobDH9ZVfAfGpk2hlIJJF1E%2FDqs2C07FnaFzEuTBuo3goFl%2FHzDuFWabdKGw14v8DesUtJXzs%2B9uMFwxtQwgkqISZC%2F8eeLX1nYR0nGtVTqlkbfUGHeMu65yERsQ2lXGFERc&X-Amz-Signature=698838b4a93395e368a21d465fbb13dcd1d0f558e27dc62a61259417c32e723f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVZ3QJGM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQC1pq1jpA6yPAlryptf3TUZqlM0eJZAoM4IzWmcBAlWLgIhAJQoNI4Z1N4J7eufyCWmexmn2DMjCy%2BFwA1PS4fgBYiAKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNgAOLwWeo53uloGkq3APY24AU6qKoeXHpxz6crJ6bp0MKOThYUz%2BwdnQAw%2Fhif9RxLChBrC6GmQQV4m7zzOz128%2BmM6DljwchCpwe57zVG6MhbhrXm%2BF2fPqQmIKt3J0kx2MM%2FUTDVTXoFPzWjnjiAVRCpGSbGcUoVyL%2Fp5gpNDSrqzK%2F8ZUFfVD0I0wNvsRuuwY9OmJ%2FaGwiazRuNWerKGvq4zHl7b43f2ojh7APhobhLfYviDIV%2FxxUViDJIayX7aIQLiqFpUy24C513EnBHNZrDpYbuLCHBIMPo1tKTHPQ%2Bu9GF4r5zCZAA%2FEbjJsgGmm4T6W2%2FlFEixm%2BuAVbkXLY0DX4iu%2FcgThCsas5yKLoGJmy0MW9JtDMDCApS7T3MkGPnbCM3sdd7KhFI3BwpCuDRwTY5EoVYW5U%2FvoBNtF5JAfuJH7rYsG9HMPegNnUYR5x4x%2FiDUlADW9p5tgBsWtse9n267FSyymAuFqljiIQaHZCAXHmlA3jHqlGqh6HHMBrKNQEDtHKd2rqWm2yKnk1199A0AtkRKix1D1ue26jNwkqMaZSVo8lnbK9LMsKegdVOnI4zh7WH8jNkIN0DH0YmvB187IwLvyG1TjShZebrVs0G0IsN22ibdw40WhAvF0kbxT8NYVs7DCkvOa8BjqkAS%2FRhjJ30mvuTdnkMEGFkCGVNK7tOUHy9YwtiWzn%2FzVRkfStYOX8t2%2F7m4JLJO7%2F2XW15hN09c9sip58Z5CPP%2BCSNo9PcTq8UFKVtdEEHuSjuI1T0DSCxFFOaHQLV3xXDQHpjWpsfGQfAqjMkiHyVRFZd3vXRm5QIbqaVYAcBdoU2SZN1K2wHqskHQJwVplLXANpcsA24uou1zKKu%2Bf6QzfDjuAl&X-Amz-Signature=9905cde742d87657c61b832555a58466c256c3a808bedecf71488bff795ae966&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVZ3QJGM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQC1pq1jpA6yPAlryptf3TUZqlM0eJZAoM4IzWmcBAlWLgIhAJQoNI4Z1N4J7eufyCWmexmn2DMjCy%2BFwA1PS4fgBYiAKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNgAOLwWeo53uloGkq3APY24AU6qKoeXHpxz6crJ6bp0MKOThYUz%2BwdnQAw%2Fhif9RxLChBrC6GmQQV4m7zzOz128%2BmM6DljwchCpwe57zVG6MhbhrXm%2BF2fPqQmIKt3J0kx2MM%2FUTDVTXoFPzWjnjiAVRCpGSbGcUoVyL%2Fp5gpNDSrqzK%2F8ZUFfVD0I0wNvsRuuwY9OmJ%2FaGwiazRuNWerKGvq4zHl7b43f2ojh7APhobhLfYviDIV%2FxxUViDJIayX7aIQLiqFpUy24C513EnBHNZrDpYbuLCHBIMPo1tKTHPQ%2Bu9GF4r5zCZAA%2FEbjJsgGmm4T6W2%2FlFEixm%2BuAVbkXLY0DX4iu%2FcgThCsas5yKLoGJmy0MW9JtDMDCApS7T3MkGPnbCM3sdd7KhFI3BwpCuDRwTY5EoVYW5U%2FvoBNtF5JAfuJH7rYsG9HMPegNnUYR5x4x%2FiDUlADW9p5tgBsWtse9n267FSyymAuFqljiIQaHZCAXHmlA3jHqlGqh6HHMBrKNQEDtHKd2rqWm2yKnk1199A0AtkRKix1D1ue26jNwkqMaZSVo8lnbK9LMsKegdVOnI4zh7WH8jNkIN0DH0YmvB187IwLvyG1TjShZebrVs0G0IsN22ibdw40WhAvF0kbxT8NYVs7DCkvOa8BjqkAS%2FRhjJ30mvuTdnkMEGFkCGVNK7tOUHy9YwtiWzn%2FzVRkfStYOX8t2%2F7m4JLJO7%2F2XW15hN09c9sip58Z5CPP%2BCSNo9PcTq8UFKVtdEEHuSjuI1T0DSCxFFOaHQLV3xXDQHpjWpsfGQfAqjMkiHyVRFZd3vXRm5QIbqaVYAcBdoU2SZN1K2wHqskHQJwVplLXANpcsA24uou1zKKu%2Bf6QzfDjuAl&X-Amz-Signature=9d33f291acb570f0f35e7c1f6931e945f24f33f3d09dea47d32913f7859ddb0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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