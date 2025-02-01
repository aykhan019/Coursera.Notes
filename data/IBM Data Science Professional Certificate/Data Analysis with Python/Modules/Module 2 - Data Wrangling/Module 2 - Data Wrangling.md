

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2ZDYEBN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBVTGhxziccQn9BIS26sQq2jBPd3rL4and%2BDI1sQVMf6AiBSqjsxaBvT34ACHOcT0ioTmLuox%2FmDASnB6ok83erVxCqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7AT8eBFJNTPWjXbwKtwDBsc%2B2i1P8V4D2iVRttEVhNFQFo5tuqoclOrgBDyxRGWwonWoH8az%2B49pZIY8taArDbJpwaC7EpJKyA4pZ5r1c4j7ZMtCp1DcvqnAU2TeNhr63ayR3F1oN2Y87hZDo48sP7LncOVXdP%2BvTYN4m1aXB7v8bkW5fv0bDRz5x5n3xSpP9woVG1xIljc1QAYBslKTxb1quSTpSN%2FLT2OINGDD8ZmheCsC4pa4RTdGOLSolRmfydRJILf523cW2OV0d4%2Blg4g6r6%2F7eUBU0BSK67AO%2B5bvkvjfyLnVupgpGLngCbVgpGa85eL1mEqMEI4tP2xygBVCtNwHjs%2BKxmo2DEFuTFkCdC3CjepNqybYRgtsxxrG%2BJp6pmXxLs%2BWiPSoNSBZkIgHtQ9H4%2FwKzs5d1iHZ9nZXT7HvW3bLzq8pXKq%2BvKdUfV%2F%2BSq5OIhGW0XDBJ7L%2FMHe1XfPdmJWoc7bTVxI5SZrcqfUV%2BJB%2FZRLwEJNjHpNT3m2MzwK%2BVU1ZI0Bi%2Bujm6X69hMq%2B9AkVWzthT%2F%2FtZBsaHO6U7uo4WCFgX3GPlYTcBUuXNxukg7oCQSILz3nEBogUjaaxUe5XtWunzG7YC8AnpCOPYrpel20xblxYd6Qc%2FqeOHuJ5arGP9sMw0MH2vAY6pgGx3fCih5q8fwfC8SoaTbeC7rCupk7A4Yjf7JSPCfQa02uZkJQKYruRGCOG3xZTu1GpXqwboAGB2Fho%2BFI9rPzsyWDJLgGaZwOxy5eLLqeYKizSgqf0EF2HnV8cTj8Yd%2FiFGwH%2FeGnFC284psyLROx2gbp6C%2BOpjHo3Fow1cYeLAHAKpGKH4Hfb9HDhUFo2zDOrWiOM2ZY0Y3thj%2BJdI1hs3FFQd7Jq&X-Amz-Signature=9562e6b4948c1942bd760c015d4ee4159c188eb3e633427d27f063bfacd55e37&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKRVTSEJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6WGN0On%2FaMI8PHKcgQkc1XcVh7N9mLeDnBGa3WRFI8wIhAPI12Gq%2F0MySkyUjz12DBdI1GE6%2FQz9%2FhtXIrVOrWVZdKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgylpbIEtq8khnaxTYgq3AMh0qazgr4reDECqS9P90%2BX4MCAlvx6hVhGoXfJyC4kfacCMovHI3aDBkfn9sS1yYTmymgU6wlyji94H8ronay%2B4kA77sJjGvn%2FhAVUQgDMVQYe%2FZI6e3%2BMxFj4ingElquQ%2F1ftf7GUqp4hyUlGJRBCjrj2qPqpGq%2BAhhJ8A7RlXu8aQv7JYzRbRBITYjgXScTA333df5NYwaDor1VQinN1TX5Cy3nVSn%2F38vOPxEAutCAcbzADrNj4v63qJ7uAC2watcMxW6Gf%2BwYtWva%2Fy4L5kAEqkGe1IZ9QC7%2BtqWglB%2BZ1X8i%2BUCprzF%2FUJx2Mg%2FEtKck%2BWfknBbeRMfh9SyOMY2wjqWImN1q2IGYzasK2be9ZCfufqgdzqot3PaC%2BXWGuElMZV631x6cCNeEta4%2FD%2BZdK7PNFybf4QHiiMtCmkGiELYBAfe4UdMudyJzn6JZK5Bltvf7CrqbHfuJEzzZBaJoY5jlM93XR4l2Li6xU6tV9P1uzVoSX1%2FmLMi%2Ft%2BX5frr9FtTwhM8mM8C5Z9nEG2GVgpDIDlufKF97Orh2KIpjvqSEiScwGcNmuBdkE7a%2BiVMSrR9MeFzBWi8Ig%2FKfQaSCkvogtgeQgJzKtoo4jwBCSe8xyjoUKcxqhvTDHwfa8BjqkAWmFSO%2B2pAS8Hd%2F3MaibCMRmsEQ0zSfXeqE%2BTMJcpoHxm89BvLT6%2Fi7y%2FIjUoCjZbe14knvXGFE9N3bZlI77fTVzZiHuBHHEL2l%2FcGqA8J1ngz57jeZYH0ISGBSoAZUOnwSXzHzqsNzetkQwcZbsgtn%2Bo%2Ff9Gl8j1tP6Twtk6ok1WVv4HN%2BgStsd7OMoaN8c%2BGaRypviPQtMFiVmgsW1I1n1ZaLc&X-Amz-Signature=acf3c4aee606c24c0568285686fb8dc21bd217ff2faca16e6542d53f299e05f4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRNKBRJE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPENYNep1KbbVwKe2QJn3vM%2FQJpnSnL3ZtCSHocvLgJAiEAuS6jrqUBQGK0ByhW28Xb%2BWnv7jTvImnW%2BwnFbOkxVwoqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG8POWao7lDNR5qrVSrcA0blB3QYo5KWxwmKjJOue3%2F24l%2BOb5dQ1hAIcW3BVg%2Fwop3OqECpRnXwN%2BqiCQtJ23pSIGmzr%2FozeiW8tg0bj%2FVobq9NBEF5nm00bgoVo%2FLQSMEAVQI3IKArE2Fsi7qMu%2F0SlhSeYXq6yB5WRJHfYxTIkuos1ezWkNVIWLasUBSYd7UlcKLW6KDAVMgDM9x5PMn%2FshLfrtWBvP9jpjxZxTAAdHB6P1y%2FeTTTxu6YZIAU2PRWCsDCPJl7fh07mx%2BDwx7r26%2BTAkW%2B%2BiA5dvAb6RtqgBup6K6%2F2US5GA9Ghl9ckLjcYfhF8XjbzSMYhGrawGHBtCE7r%2FtnOr5GMBvS6PNksDwOCENa%2Fv1aJZZDvDCxx3iOiNa%2BG1ns1yTGRSHv6vyQ%2F3MzpKp3aB1j0DNkUlYQc6XXOm8vzyWQH6O4XqoO0h2yL1IweyDb2k%2F6My2KKbmr%2Btcqasjf8TEXBgrlianXZP7ZUxsHnaPO1ODCSFyAAFqXHBiprAnYJQFR38C0HelwVlSwzOBL%2F77gsaRxzHA9r8LJg%2FosNdSS6Q9XbR519FHvCxgwg9iQ9jknxw%2Bx9RcPABb6i7VpEHujt9aBp8NkLf1x8WCIbCtbUaD%2BissRO9s%2BcoCKiLzYitkwMMfB9rwGOqUBGPKEnHqkLMeLUaWFdT4qIOiSOfFLR7eClFawvLe0UIjlXPlis2Vn5VwANaoGfsIiPOXT0eEWkQb%2Bd4e7a8B5NTg6q4eSw2VQyVsVo874uBA08kZkJah7%2FeVs6CCeJz0uKUAw6V9iz9JknO4Z5kzZz9JO4PKxdvk3T3hmkprFbLzjnMEIuehXMnxhd0I0hxDVzI7rnlQNTeWSuziAPgHTNSyeZqyG&X-Amz-Signature=39a0fed6bc862d93bf33433c3ed28a59fc3b3c4e63e18f5cc2452d46226d1fff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJYKUXKH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIADAg4QTpsFksJ6WKrY2vwhxxkdlo6j0k9aqEMdNDtt4AiEAkktbznzPgLUxNajsQwns2Bq15Gcod15%2BDTLOihk9UQUqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMCVAbcb0s43UveC0yrcAzyQejm5PVzeLpOQWRYQc8W%2FBb9YHK3SDJJuA6jU%2FDCFCxGapnmGhmgVxD7D7AofNaR9m9zcyS7ogIlBadnsFdwKn3FjtUootp%2FFhJ6Av401kyLC1v4U54mgUjegnNXlXWK1Y7oCUVm0d%2FdWCDPXBb2Chcxji5ZhyK4zRAtydzSzejMTYILYDFvArjuaHk%2Fdg7EH5uG2WvL%2Bz2BuQqg2ZE1OvWnmsplwXUE%2F8w15%2FuAIoQqF9vS0DIhq88Ec5F8j%2BgAZv8VBPjH37dJsODv1vkjGtqB7UasKRpaBDQ8YT8vLoM5QnKjgFw2y1EWhFZfiqOmSGjGMDZYuCOJdxuAe6BxeD35pcEqosMSSpfLjRhndXQEUVOYQoQYmSa2cp2a1QDXy9mHOC%2F50YuiJAEHImC07%2Fd8hFxzcklW%2BO%2BUQ2NwA68mzI%2BCfMew%2Bk0RS%2BP7hvHnYcpulwslEKvgfnBvVmrPsYNcqGW3c6pwfviDIM7kAlshgzeOPcgHn013wkWUtzqMpSXOFfOV3qEjM6wdMlzJxJc3aq80dgqdPYK%2F841CtTbjC1VO1suIFVyKn0%2FdMVlB19YaiRSymwxIZ30H%2BfP1ByvmCM31ScqCnNPOtxofuY0YaNgxAtrNKlYK%2BMKLB9rwGOqUBTjqKvnHX53BHb21bGQHwbz2SbH5yl7JkKt%2FcbiXuIscN8iLNgrwQGMkMSJFCpOz0aNBhP6nJisZy5NlpW%2FWbO2VkeUuASu2ehzCfi2qXF0dMKyBnbf9D%2FppHAQoXBqqS5dpuqW5FrgkAvOAmmNHlsK7ZjALfKZVCrblE0HfwKRvq20W60rk21i%2Bba3RC46vfcQGFlL7OKFvdiedhvrx9PX2M4PgB&X-Amz-Signature=d2a676f461e790c587d769be0653b15dc64c1e9236f037e165edbbcad42b1f55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBF6QWCB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCX%2BS%2BWVz%2B9yY9u%2BOxVeZuceGKxug8wc40rDgHfzrgXnwIgFXZXy4pnf4XopBxYzIkJgVyfi0n%2FIWlze1hqosvFhXUqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHr6XyFAjxo6E2ZrXSrcA4YnnA5keSX91aTqtEE3K3O1Wyq3dtyDmwzV64CoFJhS%2BzccAHzc%2F7HQDmLDel3jYfO%2Flx8cvwvrXqHfs%2FTdtLtzWieQhsw79aAbLkmj5f9OKBnes1c%2BK6UCvWc1uZOUvrgBrp7L9WcffZvhh6tiIIwWIyI08zT0FMTahDtl%2BOokAC5YgFiHsohQx4UgiLH5XzJzlKkNeVwis%2BwFlk1AJx288eHQ8ZVsuxp4BAdifUpw3g7AeH3HbvwES1Vz5BnxYW%2FgdaQcCSCmtiN8ieJ4BgfUirTQpGDve6%2F4c%2Fd8vNqmv9nU3H7ki4i1Ne57UsQ0nBz5FPNZObBja76hzZ4sO%2FJY0gRQ0npHBxxgMEK9KuuW7AvM8IygJoYmFWEN37B%2BhjiKhHbYK0BcsO2HwT9H2bV6iSaFyHX4ohJGc1orcjHiye1bp10aYpCazfhuOjiOMB4%2By0dTH9cNdUz3yArEdKq95TE52JASgVnuZhHtJwX5FJDAD0iA4Av9jf02agNOHzWYxpHTl2y%2BmH9SIyVXOr6hD3IMeTtYBVFGqOt2PEwGswmxctXKdGJ1wHzMR%2FgVLi4XnFuNQHmsMoTbqTiBms%2BzePbq5z%2BVvrD3qBaQCSVEZ6lP048Cgcfa30X0MJnB9rwGOqUBLiWXzdwXFAA38%2BoiYD4iGfiUAK7BL0hFXBzUzLIzqmjFyOvUQ4CUwySCHG5EQNtX%2B4Ep1o0XZ7oXYK1TYkjw9N3okv06p0qYpI9zvKZSxpRV4j1Z8n19NoHlZq7aebodnhoW9xnuBayUd%2B0%2F8z1TSLEpau7inQRU7jtvWL%2FsC86DzV0clzkYNFBEauuCi2F6BIr6NKb4EN467uqQgFf9wF0BgSpD&X-Amz-Signature=2f3a03509bae9f8af43c69da9829f94af2b67d6d7a2cc30f7c1228ea95ebd1f8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6RQVSYU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQjOnqcfJtqvdhjdfcAEhMC3ZvLJJgigFTkguFBjb%2F1AiBErqsJPiNmx3zOfhfyCRv4hsG8Iov3T%2FZxiY7%2Be5DmhiqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBUH5dav1%2FIx2rOq8KtwDIQuudEX4QqUUjhLCjv8iTupGXysLDR%2FzXJyq1EAe8R4NO1v3hQtk7ohhhDNTWyT%2BXdNVB7pqh6E00ljEdITYGDWsVgKp5%2FHeaucXHSg%2BHY74tYn4rWXs1iC8SryGzUynYCoYweVxBw8rG2PBNF8hl5tvQZPsyn0cJfA%2F8jNx5o9c2MNzTgLO6LMXPt2%2F%2B7LU3LucBzJOzXn9VHC3nQPRgiSUhCvy8WjkaFVlbfu293JoDXtmSPcHmt3eOIu1yHZRO9AfY3%2Bnritn%2ByL6yrQSN01it0NF6%2F2%2FpmHFATBLtA22BhucwyRBOLMbrpkr8coJZh0YLustym%2F2vxzl7umQj619Js9zB1GHaf2Xrdmg%2BfCSqnQ8TtH8fTD6ZBbfuBMAHyqrbNmhLzT74mCz5SWiG3kUIJsZec9R%2Ba9n3KCyBW6KbNMsBPqQlJFAye0o4AgU3hxENfDEFDsLar8z7YKMfNGZ5cDhpqzyiLOxF2ViE75G4W6IzMKzvBGmacMEs%2BELtmas3JZyKPUcpdyvJuQrmMb%2FxVIBx4u54ENP2Rv7PHwDTTt2SsUxQHNopbk5O%2BPBbtPS9FuqT4H4ZVRLRKgP7Q4Q66QYii8n3kanRnzan4Lh1lRp%2BYcRrheozC0w3sH2vAY6pgGqM4vQ1UtccyMTJBp9xT2Vom49SXOcoZuPSVjxenINWAdQVJF5yTH9ZLvjQukKLqnK%2B5xmI%2Fu7xto8HVpr8pi5YDrb2vxIIxrPlXzTjkYov%2BAFtXSa50czDn7O0TQbgWpxWC5Q7OhSr8OnH%2BD%2Fw7HekjXw1WvHQXKbgtHHgx%2FLezMPVdprs7w%2BijLvgzD7G56ylAnv%2BbOr6ri86s03pFwWfsqzPjVq&X-Amz-Signature=5eb0f2321931d26d8e3039de7450a8af7475d21f8e4f7f21e98b743ff8fe794b&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646CWTTQS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHubaHk3sSu3D1BEmGRcVwPKDC3KBX2J8C%2FiIWIVkQv0AiAv96cTG%2F341wUm4AXAVSn%2FjT%2BdZIdxIyHJsiiSKGwcRyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHxBINtzL0YsyhZUKtwDW5U9QA6CNJJmhgf2LYRptXUx0EZHWRADpKYUC5kDIk5f9AyESkR%2FZGuOxGMVAgzH2hSTyyDcHu%2FForjqlQKR5LfG4Asu%2BNKvz9Op2YS39abSb4NVuv74m6TTZIyEihkguw08NjM1nYBfUNQGa%2Btm%2BgtRb7PUOn50lg%2FodQRb1qCq9C18w1rfZMVB6XXiOwCPFR18teqkDCz4m62c7S4cM19vIEgm27JDGqVdLKBQejqodFhs3gBa1vcGcxklVxDzktQ7GtGiHH5AZ1oBIlZNzZtiau%2BBmcaVOsbhyzrfVYiDFxt%2BPvFWHo%2BpzfG7EvOOt7gEVmC%2FnM3Wv2vPJ9m1tQ5xz%2FkJRLiHk%2FXYSg7UgDVhIiogGnaCMoj3GGEffxj97%2BkWXApcRsU0vUUMKfHLQ7A7GU5j%2Bfv6T%2B6ntVpoI9%2B%2BB6VEO1JWiQHwYLcy43Oyv%2BJxPwT8i%2F2C1R1vIeJXaY2R22id5egWY8TJQ4oUc01RBiwG3ZZzWpmME0z%2FUeZ9Vl7hwi79%2FuN7uV%2FhRJOda5VKgPs6V4fWlKuk2KhObSZRJA7JHnlUpp8mPfJWItOXxNiz%2BUIbijEtRY5Ywtz7IfXL2k%2B%2F6QKjtSJUYxtbESJXW%2FyS4DUJdM%2BIpT0wvcH2vAY6pgHbc1hVrFQqO%2B6ibM913AliTLORdsrwk%2B5HrzYjCoiMmPA%2BuZcMNGSJEVe6P9CkPD7PWGVRghsGfkpzQxbr5kqPLpmumfe8l18dMBKcaT%2FNooGtuI9A1D0b4gyMpOFxQXiUOTSJ%2BQVrRqNCAoGthQETWrIrbHN65glcyDVZZQiUlQ6OISmsj4Yp0p6XpP%2FnccD8IzUrj1LR7njx%2BrWxnIBtztDcxPeN&X-Amz-Signature=4e65812187133999c743c4028f1094e326dc1b1616745c380dd8dde17090da33&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAESTFAK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbVjQ5HON626B%2FFLi3n7ugiYN0HkWyWGZ6bZpedGSKHwIgMxnD7vhajPKF7Cq72%2Bx37hBZWSroIrPsWzaKMMbPA%2F8qiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDa6SeePI6Ar1J8MDSrcA%2Ffx2%2FSW4mbYB6VIUmlPe4PklBfc1U0YeHwR87smEzRPDsigc5fhJUFrTa8kjZTj%2BEMyF1n0q177Mm%2B7MQ6VgNv5KsNZbQozNHXG1ImYwYOWFjXg9hSP00qk2H1GweiLphj7LBp9FSxWL0RJjtMgcLvS9Evd%2FqPOEtis4lpYoYQEUJNeR8n5%2Bs9S7NtKcPs0oikIQxUg6XyYffeFQPSQuAjGbMbQz2EU8flC2RCcOLTne94YyWq9aas%2BUDfH92%2BRP3EC2Y%2FgA1ijccRNEQsxB1CJlvuNHt2eMSWtDKJoZCXO6CgJwEa%2BO%2BvR6SU6Fs6fLMEv3itnCwYO%2BDmsKl79mGIELnF3VSE3TUT8VB%2B0b3MKbrmYvW6ew4LfBPe%2BiKlV7KAgHMFb77eNOrKnkgBYBUngLzNMVXKt0i5FiYWqAguFZnijiet%2B1etG6d230TJyBtQc%2FYMpCEdFNkDsqwycOfCcxcW7X88Fmieay1XHqKGdMV2ecYFYgm6A2wOA3OF1vzPrjC8Cmsr7QIcEj9WGO5oxDOVIg%2B0KhfCqcmblVIIOqF3jqeZZ16D7wfqaNtFj93MEad9o6NVV4kqu082QYqEjHJv8MhSwQ6VLI5Ne6ELTx8YaZPK9MeVl34YeMMfB9rwGOqUBsXSrumuxrQoAx%2F5xA%2FQddV2SXbj1HVe0MVzZbFATTkud0PlSkLxEVRAVbC1kauL%2Bo1Jm7YaA9xyvsSFXdPovQAvZBSvoSMJMXXh6kZFuMh9zqaSNxnN5cgMO5iHB1DR63%2By8IzRDMSQisxGhv%2BUHIva%2FX6rm1rdn6rWoooRzyx3AnxR82GM0EgbFtWKyq7SRWe1c7nBn7P5NlDoV2qGWhDqk5qbh&X-Amz-Signature=6c41ea4871d9216b848c6005ebbe8347037ad4391afc70b5fbfd32e61d33bcb1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBF6QWCB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCX%2BS%2BWVz%2B9yY9u%2BOxVeZuceGKxug8wc40rDgHfzrgXnwIgFXZXy4pnf4XopBxYzIkJgVyfi0n%2FIWlze1hqosvFhXUqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHr6XyFAjxo6E2ZrXSrcA4YnnA5keSX91aTqtEE3K3O1Wyq3dtyDmwzV64CoFJhS%2BzccAHzc%2F7HQDmLDel3jYfO%2Flx8cvwvrXqHfs%2FTdtLtzWieQhsw79aAbLkmj5f9OKBnes1c%2BK6UCvWc1uZOUvrgBrp7L9WcffZvhh6tiIIwWIyI08zT0FMTahDtl%2BOokAC5YgFiHsohQx4UgiLH5XzJzlKkNeVwis%2BwFlk1AJx288eHQ8ZVsuxp4BAdifUpw3g7AeH3HbvwES1Vz5BnxYW%2FgdaQcCSCmtiN8ieJ4BgfUirTQpGDve6%2F4c%2Fd8vNqmv9nU3H7ki4i1Ne57UsQ0nBz5FPNZObBja76hzZ4sO%2FJY0gRQ0npHBxxgMEK9KuuW7AvM8IygJoYmFWEN37B%2BhjiKhHbYK0BcsO2HwT9H2bV6iSaFyHX4ohJGc1orcjHiye1bp10aYpCazfhuOjiOMB4%2By0dTH9cNdUz3yArEdKq95TE52JASgVnuZhHtJwX5FJDAD0iA4Av9jf02agNOHzWYxpHTl2y%2BmH9SIyVXOr6hD3IMeTtYBVFGqOt2PEwGswmxctXKdGJ1wHzMR%2FgVLi4XnFuNQHmsMoTbqTiBms%2BzePbq5z%2BVvrD3qBaQCSVEZ6lP048Cgcfa30X0MJnB9rwGOqUBLiWXzdwXFAA38%2BoiYD4iGfiUAK7BL0hFXBzUzLIzqmjFyOvUQ4CUwySCHG5EQNtX%2B4Ep1o0XZ7oXYK1TYkjw9N3okv06p0qYpI9zvKZSxpRV4j1Z8n19NoHlZq7aebodnhoW9xnuBayUd%2B0%2F8z1TSLEpau7inQRU7jtvWL%2FsC86DzV0clzkYNFBEauuCi2F6BIr6NKb4EN467uqQgFf9wF0BgSpD&X-Amz-Signature=dce8074ccf5705c817df52c7cacb48d01cb72e3b5befce6eb72b68a7dc4455f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMPJ3EMC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD60Vm1%2FDaOI2q0cgD7wG662nZ5Scji5g%2BQ%2FK8x2JhThwIhAJf6i9WBGswGuU2qaAScYqsHmKc3irb0PiFcpS%2B%2BOHE7KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwB9F6LjTVPuIJo%2Fdoq3AMtjEUwf0wTRets4c5enIquNJORVkXhyomgz6dfV1m%2FlnVfEYEYeFNc7TLX4y7sUFvy4segtwQ%2Bnqi9dIZjUAZC83DhfVAiZfaoF5fMm19F1gJvkKjB4If3qcOm5D1%2FMP8INc1AqKeVMRe4x0IYLNGeNvvsFAGAE1mN5FFfbi4jzpx5bJje8todvWz1iYIbXupcsQZ2ae79V2meA6F830QSfdglVoeuQazknmTb0FDI4X%2B59Moj3qvymQmGtmZH%2FDb8HzkwIIqBBUKRVVTGDFlsIrJDgPUyeqxGhOJKbxCOD11KKSShmaCUDoBvcF6OifeOjmttNA6LREYNPaQM0q0jXWpdYimEo5O26a51L%2FB7%2FUJ3w%2FPL48IYttOEm3am%2FJKvzmjmHvINlUHRpiOzFQPIdw18An6B%2BV6XxjeXo4OVPso%2FI%2FZnm20%2F1vTec6h8Q952%2FecYUjN0V4gXi%2FPmEtssUWCLM2mTz4ipYv8R5qM%2FEv2Jr1tEH7UJvOTuYat3nVuj3jo6n8dAO2H7BcGdZCMWRwaHj7rgttjDSQFXf23TgUJlLYR3yeeHTdgKKggui7A6zpMthAPlwYMpsQp4DIGCPt9%2FSn%2FkIrFl4JNsMTlsvhRjVSfmbe46Qio3ajCgwfa8BjqkAT6Kmow5gjJmS7LmCPR5g2HBzUUpphuwT8geDfgxVtsTnOnVtEY1hgYnx04p6mPGn%2BEixK4%2FEHPnq91VIk1NYJ%2BEgJ%2B52nrF7Wv8obrliYVhV7FnhyxZPDct%2FUPFa8Oi9l9czwr1RUVvlgIRVGEie4psSOBeDJ%2FYs4wSnNj1Nqds1CDBFcgpv%2FnmxJE2a1UsDFBQ4mfPwyEQ2Rjj30rwT5MtdUGe&X-Amz-Signature=854609fe77210c531dc9a00df5b3798327b2ed299af681a9ae426551216be8be&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMPJ3EMC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD60Vm1%2FDaOI2q0cgD7wG662nZ5Scji5g%2BQ%2FK8x2JhThwIhAJf6i9WBGswGuU2qaAScYqsHmKc3irb0PiFcpS%2B%2BOHE7KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwB9F6LjTVPuIJo%2Fdoq3AMtjEUwf0wTRets4c5enIquNJORVkXhyomgz6dfV1m%2FlnVfEYEYeFNc7TLX4y7sUFvy4segtwQ%2Bnqi9dIZjUAZC83DhfVAiZfaoF5fMm19F1gJvkKjB4If3qcOm5D1%2FMP8INc1AqKeVMRe4x0IYLNGeNvvsFAGAE1mN5FFfbi4jzpx5bJje8todvWz1iYIbXupcsQZ2ae79V2meA6F830QSfdglVoeuQazknmTb0FDI4X%2B59Moj3qvymQmGtmZH%2FDb8HzkwIIqBBUKRVVTGDFlsIrJDgPUyeqxGhOJKbxCOD11KKSShmaCUDoBvcF6OifeOjmttNA6LREYNPaQM0q0jXWpdYimEo5O26a51L%2FB7%2FUJ3w%2FPL48IYttOEm3am%2FJKvzmjmHvINlUHRpiOzFQPIdw18An6B%2BV6XxjeXo4OVPso%2FI%2FZnm20%2F1vTec6h8Q952%2FecYUjN0V4gXi%2FPmEtssUWCLM2mTz4ipYv8R5qM%2FEv2Jr1tEH7UJvOTuYat3nVuj3jo6n8dAO2H7BcGdZCMWRwaHj7rgttjDSQFXf23TgUJlLYR3yeeHTdgKKggui7A6zpMthAPlwYMpsQp4DIGCPt9%2FSn%2FkIrFl4JNsMTlsvhRjVSfmbe46Qio3ajCgwfa8BjqkAT6Kmow5gjJmS7LmCPR5g2HBzUUpphuwT8geDfgxVtsTnOnVtEY1hgYnx04p6mPGn%2BEixK4%2FEHPnq91VIk1NYJ%2BEgJ%2B52nrF7Wv8obrliYVhV7FnhyxZPDct%2FUPFa8Oi9l9czwr1RUVvlgIRVGEie4psSOBeDJ%2FYs4wSnNj1Nqds1CDBFcgpv%2FnmxJE2a1UsDFBQ4mfPwyEQ2Rjj30rwT5MtdUGe&X-Amz-Signature=b6de3bf462218135ba7161033287dae05fdc5a613239e6c27b2a7c5026a42063&X-Amz-SignedHeaders=host&x-id=GetObject)
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