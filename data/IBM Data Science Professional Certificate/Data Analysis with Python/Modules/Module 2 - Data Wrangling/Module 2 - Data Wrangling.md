

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRSM6BGG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIDXM4jkeBBl%2BoISedDh9umjhkUQaLj%2BzcQiIn6n%2BKgRoAiEA6gyTFfs6xIv4%2F%2FCzEw3sA%2Bk3PW2xbYfCEh1kf63uwIwq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDPEYNmmqwLdFsDa%2F1yrcA5wBVfshBF364FEZgeg1mHzaPyOEQz4NYRhpBPEOmzUP%2BfjnGb8qTN67A5%2FP6TK1m18CdR3Jk3x9C%2BowMLXSHNTX5OXxouaX%2Fj0MgdajuaSYpyOMrQfSweaR2RwAe95RKxQR7WSfr3QpELvELP1Oc7Fxdo1SEE04wrNsJRQhb5jlmGx%2BoWZSCUyN89zSt2zkXW4tPrHhpf%2FEXDNsc%2Fbe9ylAc9ytiUmJUO1M7RThc5Jupf90bFsACuqQm96vV13HatOgxn6p4KP5qPMVtd0hYv2FQwu%2BJJnSSbTHxI4dhA125LbDYcopLlG5pdaMqjHypOMqA9DeX7JYkUEYFljSyTaB8g0zOr5yXLH7IqkXRF9svgJlJgL%2Bg3iRpHY9Usp%2BUFJU8C4VMJVHdYpWiLz3Nw5KAfyI2hUvDcNZxCGw3YMrJ73S9ojQ6VvRPg8ZkLZklzEeSRha6cERfrKAltrv%2F9qGf43ogQGOHfMAHqi0bXExr4jByhEMAladmvhJacYE3dqC%2BhsFXYMLi6eM%2BBAmhnTcCgyejcfkaLDY7ZzvEdd6D28VYCNKCM7fi1uK0028UAgHsDh%2B%2Fp0UiihEegOCIKMXLrI3%2BKIrxx3TGaHRkGY0Z0c2aOeYgizhcp2ZMK%2BCiL0GOqUBE0f7uW3o7ZQ%2Fej513s%2BbOAARLLBb%2B6jpFACZNyXtePxy40JyrXVptSOubq6JRQMNa17V1Mj6CFWgotCw%2FzBejCpuuKDVMf0nIkAYTMSwtKrJ4%2FbT%2Fvl5%2FfhcjYK36CwrYuctn36U4t0qkCEwPXfbH5boM05YgTDOlUKkpjNHACoDb4zVE7myjBmfc9BS4XDMT7%2Fu4ijVytE07eNLSxcOjJNdYyzw&X-Amz-Signature=6c1aa764fd7e4e4b9dc9e7e647fd5ab36995dbeb1360476808a7f3f7be2e101b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHVIMFKP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCm97T6lp%2BhR5c65zhTLkxfle9O01Y2%2BJh5E%2FQHsq9AGQIgOrA6bvWDUBk%2BTsVQ5pkhaVo81jZX5lhj3iiAiuWsSicq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDDB0Kkz0We2sbs2TfCrcA4OeKTWivF5cnuKlrNRNSM0wt35SqOe%2BGgG8lZO18HFQWWVC26hVH8nU2Nw8nfFbSFp9mjUsFlQWoLZIY82ZSTj33ov0CUP8De%2BIjPqoGc%2F6qcsvazjEiuyN1iS9bf%2FVXJ%2BV6h%2FcTE8eVT1o59u%2BYqdgDBfH4fdQ21Np3C2evCnrmp3yd6RDLmUb4G9yK%2BbMeJOHpwIfmwzHR%2Fg8SXQoopxgtOcKiOhKc%2FUz64oOi9ZEZLmTjM7Ucyw8UJLKeGj180cWv8rGRr6e3xHU4Fka%2Bn9lvOTqnvdsd%2B2PS6%2BKYfqATTcgq2Jc8TrxnHCbOEpY6uympHS9UIN7cIjvUfMiy4fS1TvR8MhfhqsdHXgjEbr1VtNax1GFpL4phtA0yZgRJWbr%2BpvQ%2BAXKHzYzjjMiYpV%2BAH0K3cVM8jymVZd4PTCw93TG%2FgUs0hKreyiPxElkC3TGdIFFiF66E%2FDrLI%2FFge1U4jl2Xo1hAgeT8KDemoYG5r4Z3PYs%2B546KUbx%2BTJgHHPxo868G8u6%2FGZlWxDSdU%2Ftq8MfqUwFYx%2F4N6Pzl%2FOprspZkHOZJLyJaEakrnMBZZwl2Gw9jerN4LV8ALf92II5YhJaVy6%2F6bexOJFZbyauSfF825GL%2B0cZC9SSMMWCiL0GOqUBKOrL9FmjcEtgRNAaYDr09KbCMPl2Q68HsYq%2Ft%2FxsM0umwsQR8GAePSouqLdXF1sZHs%2BZJKOsWfDKpZb0kfW27Ii7Emcy1PdwhwGWTkV0MIgFO8cDKsRHr1ZDqQ7452ICfoq1%2BQ1ejx%2BcWcbe%2BWEhwfTqnlP%2By7CIZte5b2kF35f00w%2B9shXcVDPbolsxbggCOzmSO1KhD7MxAHZQAyGzOJkw%2FAja&X-Amz-Signature=c7d0aebdea1ee1096c747c4b9d63f2ced74ac283b592b5fa046429426c7b1170&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637HP5LQY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDZg5PDYoJi2kvuzHyUMWAu0iUOTTv%2B6iLjtUgUr%2BX7VQIgXJaroMoNKy6IddZ5r3FtBLkSQJGxdkGD9nJMFUxb5MIq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDMIzEI4KJmTcwflxCircA0xH97BkBRzP6CbgEsFC78H8xQWs5mNCXaZn2xuEV5pI39naqMMT23ergLuxmDD%2FJ0yx1FAWSvLyELNeTme3RHaSWQmyp8h2PTrvSV5iQz1CytVtNVY9RrMupUhogr9tlqntJINwChuDiXriUt0r0Q7%2BOWUaWxcHtvR5eqHH1Q6MoFrHNBCNs1%2B%2FabBoTI%2FjOwlsTWj3XIfTFtnbHHTX4L03tW1SKmv0%2FAH%2Fx%2BkvEbdHXrZ625ejQvOXJxqnx4x5l3mhcaKFtbXHyLFxTlvcDgWFVgnB4rk5%2BRW60bmfsy1i3%2B5BsOxKZcKlfJT6hVi4QWmL4v0j6gYraPq9ZUDINd2FKP9EKV7GJPLurtBKOvw5kbhpmMg%2BB2f6cjtXz4XiqkgrihKDWe6zovbMmsfxKKh704CIWLFDEacezllO5T%2BhzjmcTYXcJzLv0cV2Pvt8FfsTTLEILqmW8M%2B4pbMbGXjhJ9g%2FDmb83940HHEKdtDntRuOhW6HaLWBjmE8c0yd4TDUPvPyAEv7r72J5xgb790TDfT3rbhcNomQzM%2BDg8eK3TIrneAnJGduda0Zd7UHmrbYdNVd%2FBuKcKsTvh5GSpe4UIHRv%2F4yavxzO3tttWvy1jiUK39dt87MEEkwMPWBiL0GOqUB5HsJe%2BZbrOidgCEMqu5uCzZnJaOjCDZmTjDaFPPsJGk1p3wq9YE7eUUQCS%2BTdB1eZwY1IZFcuG%2FTcn%2BoRQT918pZoiTouYF0xFKGKbwTsM5J1NAZw6BiM0sJKZnl4oNqQ5Rinfl%2BIOOy%2B3lIP7jx9TFtiLOsGRqoWxIRKupNGS%2FOkYiLFBSJ2aZ5p6LDgWGA9PPR%2FzusyUaQMHnuth2gAkFPyn%2BM&X-Amz-Signature=0083de4cf0805bb0a06a821c04e97d25f834e709ec32163fefc30e73fea98cf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ42KL3C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAOtpIHAlfioDTnaLS4SazOfnWERrre%2F4R5Z8R9BTGQQAiBHHN9zWmIQmYmexjZet%2BAw7j43jWSf3WkxRY0bl7xfOSr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIM%2BLelfs4ufJNh1v3%2FKtwDIQNTbUCakSZn1EpcJUlkvBhk9oE80jTxlSJAlSjdJsS8Vl6jR30GjQ0gjWt2o9ZpvF0Q7t%2F3M19EIb%2F7y2aCAy54muUt%2FkZYnwoa9Va9A0kGYk9%2FllYP2UlkmK2r5PsYTko%2F%2FD7g%2FDb8GqwMVLIH1oX0LKQc1%2FIIFSv6LA9bRGcO5FH013uu4Hfzc6T7DfuCpNG%2F6zcEwabHUYHw4TSwVBth%2BVeryHkrj%2B7saWD316fZngWE24tBhckXmcxCpADFlq%2FDLwS4u2IxS0aIswqHALXcE9zVtZiq1J5n%2BGv3u%2B%2BV7mCjtIkff14ILY4BGzmCJ%2FrVGnL0bHaX7p9nWJoBMQmNgtGjRpHsXpCGxkL4vp9ovV9gAjZd1FGnOh4qMlVbU4yCTpb%2FzQme9Sev6aUy1abZDmK%2FgVtHsbpNHm6xxkRPnsSJSZY6RzoAvtFqQnjEYVuqGo4CrE3zIAPL%2FwOxObZw0XwfT8cYpgKj%2BedhEvbGL1fCtsndVCJ24ZZHgI25qauz84Ao0M5jxCEql034zP%2Fv%2BHBn6Vx4xJO79qysOOCbTdf80WaoerEOOGPLCCwOd%2Bp8ypSSaMLch1%2FN8qu3OUnhvh8wjeqbzaP5i0LSUdsPBrKuYLs%2BhVDb1%2FYwiYKIvQY6pgGITYKleOecpV6l%2BTcLpnnR%2BphKH20He61%2FU7rUomAtchcjRCJgCKgBhFgbSknkBYrtz17aYRsSjqMg49FPfu%2FpPBYENnYuMytQRm9Ip0vxo5k0TNuvM5gTOCvQITyNAyJv2adF6uljTuButX%2Bimo0YMW7RJpBEZare7uPIPBVg1kGDa5pl7P%2FfXAs4wd0nnG2yAVB6rk4UPh%2BQ2yv8z4OrexBOHNiP&X-Amz-Signature=5147f17bcf72a816c974ea9f2c5f15a4febc8ffb9d73559ceb00fa4c940fb6bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHWGVPAD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQCrMZsuApjv%2FHajaceUbyhpBzqDLNFfkof4ls7ZgReuoAIhAJwn8PLLRjsZ4bQIYth%2BmcKpwwzcap7LIcCfLPrVBHtxKv8DCC0QABoMNjM3NDIzMTgzODA1IgwusOx0uiyBKI9QK%2B4q3AOAUhEBkW1pTcNXddg%2Fc%2BlwKJ1DKzHKvL3o3p6%2BSzOFzdCyPu%2FXuNqbzuUCHsthlPY44ITq9D4YE7E%2FNHrUW30lszRlj5WVbb8Lchrf6BB1iM%2BkSPNqEJ6NIsiGZKDJAP8fjqbCaN1UZ6W0gTeajLB1XmyBlrILZDRQ2FwPNBHjHdc8KbPXci4%2FjTV3knYWwZpMqceRDKM0wM5Qk1VZc3GN%2FSIZyksr1CuvthFKpAWa5W8vRvkgTRrumRiP33lBZ9t%2ForgQHJkvYNlG%2FKMl8rBfpiT5mFqniM3thH69fFcIi24ysyXdJ%2FL7xgQ6mHMa5RjnUicA4HPWhQDQqqlJqp9kRzz3T2CVGX1PJDMh1VHWdg4rS5bZTbpQd3Zmas%2BtIQ4onDOeWvF1jXf8O3aClYFzaI7XGFgUHNSSVMkI457aaYFTmG7Cw3RhoVbbZ6GRVWfIzrNY2NLoa61TzAq45WOOMTw9T%2Fuh1Z04n3tTiMaG0UTIj%2FdbJ5rYLFSsG%2F2qwaiPTYxbq2oArTFlO5MRJsiOoPOwaZdxXu%2B2b0Psu%2FW%2F%2BVXSApX9%2BvVZ7jpDE%2F%2FL5SOLxcTXNdwhP6ZV0v9edTeQXEehrVfEI2SrbzHzc9Hju4rC82bM4VTLgmwhYzDVgoi9BjqkAUi%2FLrhSHwpbYGUemh8GWmAQMZs4PVDg1f%2BogEQebRoNATWW8RTnUyGt%2BB4YFro1VtV9A7J6V42kBAlI2f9a%2B8OVhVn%2Bld4uCHbMMYL4UWZVCEDLaZbT8F6TT%2FajOkYJ77NkW6F0BxJyVYi7%2Ft50LSELP38gi2%2FbKImnfS8QWAzlHSedEuPJC7r8R0k1tiWZp5CdUIAkfAWSxZLaMwYLGI7bJmHt&X-Amz-Signature=77a3393b8876627d618058c51da0aaec53e5190a2f7de672150001708c9f01a8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AS3QFMH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIDi2DPfcfM5azRk%2BMysQTtIwQE%2F%2FQWmLwPjIA6bgoX2HAiEAp%2FlvT3rnB9h%2B7RVJYa1yeQX8kMUbtpfdtPFxiG5gTmYq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDIbyRHG1iMVoqBJZpyrcA%2B2TD2CMe1kXDdAGvNA6BfhU8x1fLFOMPt26q5IYyRMrVoDYWkB%2F0voAsNGSO3uEnrj9KgrtWH7EH8XIIU7qbLAAXGJYV0T2hirV539j%2FsRR37eOP4i%2FBJ3Adg27M84vOX4UPz3swguICA3m5KuUYs3wZoIohL2E%2FIdcOMX5AMb7WzTC%2B915YwMzYmHTD%2BNNmjiHk2DHRC92DhPQ7ll4AdRZdiPiV1gL8rG8TYbicWazU8wE03eB7kModcLa8NLJs6O27X%2FwFiwX%2Fj9qjYNlkMTsBFyNhT0ykSJoPog6vAnQeAGBobkTsg8u5hmUI65WddNL9PAOcAcVOHphObBWMCRpcjEMAP%2B4W4u1h6Q4zZccf9Iz0Mp2VN6rOfB750z86q%2BYEm0ceW3pZzMJR%2BbvR1JcQnD%2FPyOtHkLAEWPBL06cgfsiMx9UJSXc0TSuqZRRZNT9g9rIpGmgGmc1fi%2Fjhymq9VfPf%2BNkNinmAS7bnfTBunD0T8UeM9EfAVp3n0gCoqIwvmaIY%2FnroGTp2h8jDLtGWhH3l1aeTjp5A7OeUbhdpa8M%2FALh4GK9y88wpOyXmpkw%2Bv9m8qXt6EJbDVM6maleDf71S8sZAIOA95fuV0rjbzs4gOUu2stgGfG8MPSBiL0GOqUBaLxnTuhr9eaxOy%2Fa7C4RUeOQgVl0c8N1EMepnpJ4m5gX5wXBcevBv%2FtJw7ZZIW9vPE1NvwFvKZwSTb11FBTL0c4saZrcLhbFd0cqxLIfoUWTD7x42WqvgCSiCPUEU5j1H3j4Dt5IWD2RfdJg%2BS80XGY7viaNi4UyXEWq706ubYxSfswrjqu7%2BXjVbl2K%2FwmBf%2BVG6fc91W%2BXEwpJXXecUtU2Tons&X-Amz-Signature=9832842f48d3639ccc5a17ed3218ad96e617370ddf267256ade83622b1edda01&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22ZK2C2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQD4QboB3J5K%2B8WAfz8U2FKRSWuDdIAaB5%2FroS4wdCot4QIgNpwI6NxTMmsS5N%2B2foE58BJshG7RXMRKdNY%2FFAMIc4Eq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDEJiwsUcI5oxjBhSYyrcAwto2QuUo0Q0Me1rgSyHzmcM1paukZ%2FlceGQClkvRbHTJ3bGMLdgKryBEwJ5uRAW%2B14uH7iG%2B2QwicOt4ivz5JNR0DYkUmqLQ7zROu6p3RDSrE7TH9KVoX%2Fd55n%2FmB7903JHGHVDu4WrsTNeFJS%2FIdN22Vmp%2BbRX0%2FYvt96AhYZqLQHhZ3egAkcUR4PBPY8Op4oJBQXI%2FRvbI8hVtcuy1cX2kyNucE1xJG2tvEd46SVXzQzXClfq9BCPRrzD2j%2Fz9MlDBjMjyh6yCfiZ7FElhP3Kd1PHafn4N3El1%2BBRBMFeorTlJq1Vio2HmPrWxSGMTMJxUvotIwPE5FRfj3TFUUBozeg9JwrvIFtMSRp2NaDpjpp%2BC%2BK%2B%2F2BURsQGKHwZK3H%2B72S0UmqXlAIZg4CkXbRGgHqK%2B3lu%2Fez010eN0NXOIY8sttFD4JClWZNcV2OFLU5agfWGsuAft8LXsOUWExdyN0QI829xtKCCa%2FpG%2FqgPZpD3kr7y8wYs88h7FP5I0Xmnz%2BeNeqNKpin%2BGfRrkrOLlobB3UlEUz97A09JXXQLrNURYLbNoLtC2k7f19yE70dp%2BkK36ZiAQUBGvLu49euR1AZF5qmnkbIluUwoJAooKdqzvYSRcl%2BdMd0eMNWCiL0GOqUBWbAqGfkqjr8bD5flcQExqtLLRSr45dNm6K4WRgFZlJVVu0IMiTkX1tRyAmIf1sPowdG5iCJ0%2FAVae6Nq3VeJHMotUJRRua4egK4axPT1yC2zRMRG6JlFSLX69oxpzcufgSWkpYq%2FDPiMhZ2D2LrF2mJsvpDs%2B9fs%2BiHZchalXxn6dEr5LG%2Fn7CKAydGvfRcUKINTF4maE220txtRezjPtrx7jZTN&X-Amz-Signature=4b2d256b2765c55833380c73247ba8be3d994aac6445392bb575af08ff2c4b77&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HR3JFJX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDtlpmkgoOuY4LN1x1cKFMtOPStRaciKXO8vjyHUbHCrAIgXHnw6IOFLEBwm0SqRIk7%2Fao57zIHfrDOrt%2F%2FJiDtCy4q%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDKhwOFJedZZcppZvCSrcAzuLFskk68JD7DRHJsuv4JAc3CX3s5ydh7nhZmiy2fvQ9CZ1bWaJcepYD%2FyDv8bEi5Zgs4GkQw4u%2Br1GYcNgUJX1TQan3psVj5kWAJm88Ke7ohgGqPgsD2sloUJc0ca%2B3Tizrie5s9eyS0p%2Fw56K2JKhkucWCj5tK43QWDIVEn8aqAd93GD6H5OOywPZBqIi5g2rIKQ5rRx6Sd3PlnNtFt8mdFN3kQ4UYVOV1TjF3wcVohlt9sm3bdM7z7zX9auBwTUMsNrX%2FBd685Dg%2Fyy595l0s20FkhigASi4HZ9tQxwgbd1f8EEC4ji2OuR4p5jNupOWzQ86KzhViMTJ3dC6%2BXYy5I0wyucAcLPjwFt0Ro8LkfffP1jw3KTyU5bBMfM1ryXQ7BUBWyzlUWqzvpTYPaKuD%2FIdF4NVHr73P9P3qLVhpgmduyJVcTU8uszT68eqgnL8px4jJksU1lKT7zk4vLcc6O9TK3irJoqkBazF4sI1aRZPWgnk0ITXFrs6jS2UPAJ5AUBD65YP5cck%2BqC%2F67qdhhyTurtAPbmtzjTEFIu5Raa5%2FSgKS0S3Cnt8DZxq1GGGpELBXiwlUxK7%2FkTDC8ALrD490ElQ%2BmH0DWm8pWnq3P5mMFGMOZXp%2FvUGMJyCiL0GOqUBqOpGeRuWoaiRrkLGrciwDkIlHlhQAf%2FI5hiyp1h4%2BLz%2FoqXoO59%2F4sjxNvgPNo2RFCXMj2BUyoLsW9bbUZHwre8pbUd8pPuy04Oxtarakh8o5Zg2n6sYGvoYrtXbBqEDaQFt6ORrtC1NWDqBm%2B4f196jI3CFkfRkca%2Bnfz6thLtBPzjF9M6V%2FqLcJyXlmzrPAt%2BZU6axUDFTWKs5oH2XeMFKXrHt&X-Amz-Signature=412d457aec0ac3e3b6991d7335befb213c3042dfbb9b2db0507acc69ac8d14b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHWGVPAD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQCrMZsuApjv%2FHajaceUbyhpBzqDLNFfkof4ls7ZgReuoAIhAJwn8PLLRjsZ4bQIYth%2BmcKpwwzcap7LIcCfLPrVBHtxKv8DCC0QABoMNjM3NDIzMTgzODA1IgwusOx0uiyBKI9QK%2B4q3AOAUhEBkW1pTcNXddg%2Fc%2BlwKJ1DKzHKvL3o3p6%2BSzOFzdCyPu%2FXuNqbzuUCHsthlPY44ITq9D4YE7E%2FNHrUW30lszRlj5WVbb8Lchrf6BB1iM%2BkSPNqEJ6NIsiGZKDJAP8fjqbCaN1UZ6W0gTeajLB1XmyBlrILZDRQ2FwPNBHjHdc8KbPXci4%2FjTV3knYWwZpMqceRDKM0wM5Qk1VZc3GN%2FSIZyksr1CuvthFKpAWa5W8vRvkgTRrumRiP33lBZ9t%2ForgQHJkvYNlG%2FKMl8rBfpiT5mFqniM3thH69fFcIi24ysyXdJ%2FL7xgQ6mHMa5RjnUicA4HPWhQDQqqlJqp9kRzz3T2CVGX1PJDMh1VHWdg4rS5bZTbpQd3Zmas%2BtIQ4onDOeWvF1jXf8O3aClYFzaI7XGFgUHNSSVMkI457aaYFTmG7Cw3RhoVbbZ6GRVWfIzrNY2NLoa61TzAq45WOOMTw9T%2Fuh1Z04n3tTiMaG0UTIj%2FdbJ5rYLFSsG%2F2qwaiPTYxbq2oArTFlO5MRJsiOoPOwaZdxXu%2B2b0Psu%2FW%2F%2BVXSApX9%2BvVZ7jpDE%2F%2FL5SOLxcTXNdwhP6ZV0v9edTeQXEehrVfEI2SrbzHzc9Hju4rC82bM4VTLgmwhYzDVgoi9BjqkAUi%2FLrhSHwpbYGUemh8GWmAQMZs4PVDg1f%2BogEQebRoNATWW8RTnUyGt%2BB4YFro1VtV9A7J6V42kBAlI2f9a%2B8OVhVn%2Bld4uCHbMMYL4UWZVCEDLaZbT8F6TT%2FajOkYJ77NkW6F0BxJyVYi7%2Ft50LSELP38gi2%2FbKImnfS8QWAzlHSedEuPJC7r8R0k1tiWZp5CdUIAkfAWSxZLaMwYLGI7bJmHt&X-Amz-Signature=32bd942ab40e06590200662cf795c8db0ea2e3a35f7d70c1d136414b93a180d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOUGYBBR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCoNUoiSTFoCuPKjnfhVC3vKDwoMMzLWSMqUZWfNkeC6AIgBt1OSRGFH%2FKreNVZuooUFkjNTMkK12KlBmUuX6TXqK8q%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDEru645QMEPvw77MBCrcA2lavA3M4UWhXycS1%2FVc4uFhd8VPla1trjOT0%2F2p%2BoPVnL109zVGQALkDfzSuTqd7%2Fk1yt0f4deOflECMRHPuGERBQ8XfYDqYG8BkAL9WYralc67Gn3jgw8hYHEXBAF5KE2Odabk%2F4nGtoCB0t2VY%2BGofSOmW%2FMeoqESB7HzUOwJwoB2xE15TFXUB8M%2FbsPzzwiE4ypVOlVPTBUcclEotpn4fLSY42855vdHtP0HFmiWQlOOamDllshaOP6z75F6X0B3SRRxUm%2Bel6MXxStJJ8zxHuqgEHBul8ONdgSY9tz8En4MQ2KFC25FdiqjLdU9105Bh9ZGAI2uo6L5%2FxN9jJ%2BsT%2BHhASMcz0rB2IC5mzBocZZhiVaYgCo8ZjF%2FDmGRqeK1cbFcmwv6GfBIaAZUtLYZQQi6192vloUWbOCPKoPeIrPaxx%2Fwo7qYaS29j%2BBVLIdVDY9rVtJ1h6TlMvJQOITotXwan48fW3dv89P%2B46d%2FWVIDCKSzyJAV7RhIMbZNF%2F0d5mXOpYeh1uHByhAg0KB6KDeU9Y%2BZiC%2BMNQIIEVIN0x%2B8LH7pdytNiTW7S2cR7DZ29%2FGDBydJI%2BVEj9j7soTr4GlEPQGRqiS7hhs8f1LzOsipstGlWSV4vnisMJGCiL0GOqUBmz4XnsEXg9MSYcMNzrawIP4wTibO6lKXOWJpOaROsRpCKYwXipW0vW098QEk1KRn9IxdkxiA5U7yUKvDPJ3eyuYXQu8HtdWTkgX88DTIUEvplizq8jnLeunwAWxDSupMgiBdB3txeoOL1nOj3EO%2BRHZlMY4JQvKRllooe%2FegCSMSQet%2BDTCLwAe2Co4DnWWUOlQ%2BCDhUzO2Ca80pDhiN2BtrouYG&X-Amz-Signature=28f272b9e15ccf53fdc127070ae8edbd525eb88761b1b0a46073006cfffe649c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOUGYBBR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCoNUoiSTFoCuPKjnfhVC3vKDwoMMzLWSMqUZWfNkeC6AIgBt1OSRGFH%2FKreNVZuooUFkjNTMkK12KlBmUuX6TXqK8q%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDEru645QMEPvw77MBCrcA2lavA3M4UWhXycS1%2FVc4uFhd8VPla1trjOT0%2F2p%2BoPVnL109zVGQALkDfzSuTqd7%2Fk1yt0f4deOflECMRHPuGERBQ8XfYDqYG8BkAL9WYralc67Gn3jgw8hYHEXBAF5KE2Odabk%2F4nGtoCB0t2VY%2BGofSOmW%2FMeoqESB7HzUOwJwoB2xE15TFXUB8M%2FbsPzzwiE4ypVOlVPTBUcclEotpn4fLSY42855vdHtP0HFmiWQlOOamDllshaOP6z75F6X0B3SRRxUm%2Bel6MXxStJJ8zxHuqgEHBul8ONdgSY9tz8En4MQ2KFC25FdiqjLdU9105Bh9ZGAI2uo6L5%2FxN9jJ%2BsT%2BHhASMcz0rB2IC5mzBocZZhiVaYgCo8ZjF%2FDmGRqeK1cbFcmwv6GfBIaAZUtLYZQQi6192vloUWbOCPKoPeIrPaxx%2Fwo7qYaS29j%2BBVLIdVDY9rVtJ1h6TlMvJQOITotXwan48fW3dv89P%2B46d%2FWVIDCKSzyJAV7RhIMbZNF%2F0d5mXOpYeh1uHByhAg0KB6KDeU9Y%2BZiC%2BMNQIIEVIN0x%2B8LH7pdytNiTW7S2cR7DZ29%2FGDBydJI%2BVEj9j7soTr4GlEPQGRqiS7hhs8f1LzOsipstGlWSV4vnisMJGCiL0GOqUBmz4XnsEXg9MSYcMNzrawIP4wTibO6lKXOWJpOaROsRpCKYwXipW0vW098QEk1KRn9IxdkxiA5U7yUKvDPJ3eyuYXQu8HtdWTkgX88DTIUEvplizq8jnLeunwAWxDSupMgiBdB3txeoOL1nOj3EO%2BRHZlMY4JQvKRllooe%2FegCSMSQet%2BDTCLwAe2Co4DnWWUOlQ%2BCDhUzO2Ca80pDhiN2BtrouYG&X-Amz-Signature=a1365dd66132baf4f7ef72cc9485e358b5eeb71f8bf7a9879d98e1403db80d5c&X-Amz-SignedHeaders=host&x-id=GetObject)
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