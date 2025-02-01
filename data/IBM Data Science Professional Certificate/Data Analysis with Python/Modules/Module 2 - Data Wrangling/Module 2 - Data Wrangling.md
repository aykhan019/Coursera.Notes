

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2ROT23P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBKTVd%2BPbyjgZ%2Fr9W%2Bi1rr0cJcEH%2FVaTMUW1fnACos5aAiEAw4wn7ljjUjZqaAPzh78I45X44EAvNSNObUojrbUMcxUqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF9fu%2F4cZF3EZcZXrircA9RoI5wEuY%2B91uCD7JbTVuaWtQzizyoTzOwOVpDRZn2R7EyZrCcWwceiXdFBXPtEc3FDb2vItsYta%2FkFcb415Pah%2FKHXWsPt63Kb1nD%2FiV4pGh9MF8rplNufzYU3aCxI8Z4xnnBaOx8nrST358duWqLX5zyKgNiC0hkvjCgweAkZj90RCpzkWRkTfB2wQ4obIMh%2FGq%2Fk2tCoumWneczAEr%2B0QVYf40ditnACOU0nQMPaTpeSUUkchEd11W5Y%2BxKL%2FL3yc9J0N%2FBmcge2zwDtqCxjU70e13fNyP67tGXHgkg3AJVndaA%2B%2BsAaFpopkhGac1zNaf8R9rNsyV2S3M540%2BBnF27%2FInEL8I5a%2BytLOEeO2FSueWSRqK5N%2FDFnvDtdXZXpMy56e%2BMew77l%2FrlKEbL5sC6G3FF5iQQKjltBetreCuoXgWX3T4MnPErY5Kh%2BbVSzAYgA%2BWb6zk3LLl1nwlWIOdESvj7hXvAT27lWMgOH9Lg5L1QLhQIXCPW4rHZRwdEg%2FLejSGLYX%2B4xb1TiNAHJ0iySMudZgcNmUrtMMMNNl4nXy%2BFlYxTFO9XRXBnjYChSqPxbe8P%2FEFwP9O%2BlV18dfvxGEF6JcHSk3W8Y7Z7SaLmUuvICFn5OjgLpMNmr%2BLwGOqUBRA174x8UgnmMwAgGRQR4KxlynNzZrJ2p2x%2F%2BzmrBxy4DEAxHlCavUgA%2FswbffYJRvXLp0Rc36ZEq3qSQgJwvX79xavqEX%2BAEWmlP%2BI61S2ZGVvD5PiAJg5wmWc3aagG4TOHeH6M7Ji5Xb3yMgK%2BPut851U79vXy3Qjvpt4ZglLsdzHAYrex23oZQtHgOD%2F3BG%2BCJ1%2FOibnzE7SZ4xga%2BTQoXJtoq&X-Amz-Signature=8cb82504991b0014d0c65e57dbbe9cf24c16ef33f38c0d72850c06b18648cf6d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAGKSHYJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJ6lL%2FYwJPkgbm12R2GKYyc3DnsLsh0lwXHWjVsq7w7AiEA9B%2FDLzvyqXbqmR2Lqf3ieSHFgFZXa5jLcVMhZeJfYqwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQ%2BhcXcuLetQzh3QCrcA5Ii8Wj2Hdms9NkmlpBtksedwz7iCQGklrZkd0gZbPQlPe7weVzhgboACro%2BpYNuhKADZ%2BPIa%2F%2Fvf53kU%2BneXetjVrV3fGd2rLoqQhP5szXWM0K3B1Bsw36iPc05j7PZTgprVwd11NhB6uRzO6pUa5ubWTAS%2Fg%2BwxLxZj84JMRlgzfibS8ww6lcDph5L4WzTI2CgT4hL6ls1VFGeJnFFi%2BvD1%2BTH4aZqXoGzx4yRFHkBmRBfTBmfTKjKKQ6sBtJvJwmLEiKpoBCz1TBIIjwFqEcaRci8gR9n%2FFVktVmWs3w9j9hr8mUUYxsOFgWyft7tskse9FqVavaDLUv0cC521HhrMRHP0GMrLEcung9tczk%2BLb36MgqW6uvgwKUGi2PWR3%2B9nyCLlzGtLY4P3N%2BYBqeSczL1eLTbZeJAn5quf13jMP%2BpVM%2BJ1Wgqh%2B2%2F1ey0skYG5J%2B6ZtuIRNuh88hlqyhtRp0kUcT42x7PALdUxvC%2Fgi0Czrl28Lu4T1snTXgrlmfsaNhL4UVCO1Kg9KHqEctomaKwQwpdtRhem%2BwDp%2FmrZbVDAc6X%2F787dtPQ5B9KiaWaUR1CTj5RaBE9dR0prPmyhiJDRHmFSPs00%2BaR%2BSCGJOxtRZL7EkbIRCdMMPrK%2BLwGOqUBAdKOwunxVd6uySYWnHKRTWwLUiTVsOXhZ6AeCGl3WEaTNi6FrXjwHsqV43Dh%2BaCR%2FNOqkOBAJvtzzOY50xLM96BHLVvEPcO%2Bx%2Bb4tPPQN%2Fe6GU5yQrQxxHonAGLxUFLezzbEPBr2N5BepHCVL7pNoTV7%2BWt9WPsC3e4AdJfpZ2bEgQMOIvPBC0wWEQFYsi7H%2F3keLUrmMv25EYU%2BGJra6cwdEuFa&X-Amz-Signature=abb26c6ec328fc04ad183d269c241e9ae9a6900b7ab0cec69b50b7149743e85a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MVDUY6Z%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDJbtGN30RP8C5zA6WQxCQw9jy8DwZgNhe0eMLXS%2FMawAiEAmi4Sr3zl%2Fy27pKjvCa%2FOYdfWXcUKcvfEcKx7kYy%2FEE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKZFkKqYKyIClerZnSrcA8BqT7s6KFriSjh%2FTyzbFf8T%2FDoBDH6jY5KZ%2FzKCzktkWbhsXE9wX6QKKcSDXyvEN8eMZl9vEmAyame32nzA4DFYO8W8z21Crtun%2B1NEgxxEw3%2FIMVsBWbKQJsVk97Z%2F9SBHVAr1UwQv1UmGTI8WBAirU%2FSFiLb7FOtdCvf51c%2Fmnn6rSMYrieM6uwJI0gAVSAtThIJanwYhn3LykxoJ7cohDnAL3uiyE2Anw7WC5pEY9qQStt8y8oKJlVovfqf6W1u7Z8bgtpfbrnC8Fyss8b6PeR6Tfz5BAdH8otcC3O1cmQ9M1p4bE43UI%2Fchxk7NfuUMlPEd54Dv3N2bYRSG53yDjFTKVBs1uMrKItI8D6qBNP3w%2BPRDWh5uFmxevs2Th8J2wvkQUVoRzhdlqHwGqIOIsu7Cqlqi59w9LxaBq6ahBdS0GVByQlqK5un9WObxOebr50%2B0KbsFUUzGhb%2FvCg4eGfg8AOH%2B0UFSJWzKMJlqUhnkXFZc7hQ78PaVStC1r%2Fk%2B0O2%2FjrFhstBQJlqMYsIpXmBc732d8lSJ0TGhUhpt47mQyOVuJuAHFP1plxCBj4T9xPxT3eArbKgtytgWjLhwyPe6n6rwpRz71HYQYi0XoEwHsnnHQ%2B%2BZD6%2BDMPjK%2BLwGOqUB1cWN0I2ceR6tORUXZyJdSVZ8nHxLRXjvIJ%2BVRhnSieij5XyoClMCOWZ%2FHfwnE1XCNhrgZ2sPo077fXzr%2BOwOxXZsCgYgKUnqsNaunI8JOKfj4DjYHmqv%2BeAjZs97MTcaZRN6C37M9nMvdLUDL7JQMvHN%2FAn34TsBeYKNYAgm%2B4DhPXBL8w%2BVyaOUJz1%2BrIJItgwk6MffmWqzVxIVQ22JhoXrLuVH&X-Amz-Signature=a1d1ecda7196bd9cc612bd3243b70286bcfbb56a65f6a44f3de68344f1be5fe7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLQ5FPWN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDO6RvxCV2IvLkuzaKnO6V5%2F4A3M7WzC2oEXWcqrxW7ggIgAORAVSeYZkTy9nhnxJ7Abh7Uz4AN00CCiN0lLkXLCKkqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqGg8z5FEYna6rsPCrcA%2FDzYM0Zov9doBrk2vEvA1jg0aNorMTqOFcuxff%2FvNf2UttSRi%2BtkHmCjQi8WV1uO2EI0Kg%2B9okbLPh7x4L9b91mILIp4oFe90%2BTAbjpBDU7aijJGZQmLlQlJMMijvHNYDk25o1hJvCP%2BkVKLxOwv9xjQ16d8Vo6%2FIlzHj2BTLBKmlQpINJ6mkZySEV%2Be2F2A%2FbzPygVWzpdC6gmyUgkH2Whrr9TNXdXNVMHdFpP%2B6nnb258r4czYGX9l9npl6h0DRKp32erSf%2BG2f1%2FxJW0wRC4hvST%2F7%2F3mMJWP4%2BF62fqiaVAcxeUWj3nJR9jF3XCte%2Fi1vcHcTM53XZGlzvHeGlJtPGhg9JYlLKgM%2F6nHQmIKMfAc897z%2Fv61VhS7mJBuRCnwVvsMuw%2BD1vM%2Bk0%2FbQQaeOUQIOlZTEMQmH2yo3YtIJxyn3gyRYSMGvA9cXBZeuPth2HNwSaNqnp9ugnwB7L4ZqNSxJvnr5zxT1wvlfiR7u5HrrKKYoWoDFTN7ksNnNFJkAjGyOwFPm6TolufxXIAeLcsVphgsXo7Ykm1BCjO4X%2FBUbxyQHkKuvduuMJT8Qs5kNcRjfjYozcRwmTaBV0Sai499Cw48jp62nyrfQhaWwZP1U0LosOGqjKxMNqr%2BLwGOqUBs2ZSlTJ1ahxxr2joqBgfGqHP11JNq279v%2B7P96EGTQ%2F08nJzM8GmAYv2UobexcRyG0a%2B%2FiS0dVM6zRZsfd3vhbGupBORuTsPZd5AvWOkIWj9AI0OiMRPSUzs9AoieLz8rqGbuBvkQFOtKyGku3k2ABxPpo7bOQ6jcTyR07L9fd2vkBakLusQMrksEBHfEqpOeWOan4h%2BFkxC7dx8n6sv6K8fSok2&X-Amz-Signature=b0055e40494832fd52b0566e42328bb9079248e16b42b22f22c734fa3e1a8a9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOB4UFIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEcJbi5dIhy38N%2FllmwXMtvjUIjzLhRdVA%2B8ctg27VOOAiEAo%2BLcD41kVyGEobHnAmpm7FqSXAlcghFq%2FTyzALGofrIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD0krESCLqnmZvD%2F1ircA4tPRsa7aB4FS8p%2F48B8G9PXNSJBU4FVhjgei4UfVx49QjwXI6zPbCv4FrF4jYD0ugBoSWmwPwZN9Slatn822Al7fDwcNkLTXz6zE%2BBdlZMjszwbc8zhjteSSPHVuMkY%2ByVjCtzL9%2B7bojVIgJbvJOTE%2Bs8ZJGQxGXse4dCa9SLLD%2FnX8Q88jLH2E3F4ypO9ZVVHtzgLsAt%2Bw974fNS2nGpcZPQLsN0oXngEugoBLgo2hH2JDwgktFFZochTP5UzuOLr%2F4CBWDtF8ubiWI4WhVsjL53HaGEuyk4%2BJHoIdYRxlS5USoNnMEPi9UYxUa0AjMoaqutNH3Sgl6Zm01JIS%2FUvwDn5yMCkeHjppnv2uUD92XHM%2F82bZ7UgTY6cnNIcsd0WzJdqiV2OhHhobdH%2Fx0mAFzMW1I5DB3Qt8%2Fy5RUxZ9RaTGzCT8nD7suuO55d3MPlAW0RtgnCENrnOvb%2B5X6E3%2BE8pDTRLKJjPb%2BHv0cxG01YCZZgUMm%2FLtFnth3CGBYBxKEE%2FtaJNUhrPYDGfZASxtRJXZJSz%2BPWawUhwDUZ8%2By%2BvuCNkpnEEL63krOx40HnLl8L56WMcBlbuxMo4lKP9tNPVe%2BzoV9BEO1Kv1mzjLOI4hPXQlkY6whXkMLrL%2BLwGOqUBOKxNtZPQCZkopZrgEPk2vzbSk3MQ5vZOf1%2F6zu6m2LQVD9IFi4UxlwG6dhfYg8Mh4%2FXYcFRHKFUR7AtPLz6ytV4Gp3YuSu4Bbsrv223kqN1CRov1hq0LdZGPCyxbdQgCDV%2FIHuaw5o0pEfyfoe1xKU34ZO8by6MetOh3YdcVesCL3OZgqnIyuKWm3k%2FjaZ4tDUDJeKf%2FbW1rr1srULiKKYYh1q%2FX&X-Amz-Signature=5fb52b70d1bd77b3695f6a4204c7bd86b64e6aa54f65f5b1878a5e9149763954&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PX237DV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD57ZMKORoWq2oAXrvTQ1Ppuo9Z5lMjh6hn2E%2FXuxFGNAIhAOLqE65RxRDxKxSExwJP0dr1BLZD6vZjeOg3jrQWCi4SKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOVmV5oFFyd3hD1OIq3AMP7HsC4CmX%2FpN%2FU1jpLn4gp6dhCiN9pXQFSnyJdG7FUwZkFBJYaYmN%2BL9Vq8OsWG1yLwzkmW5fBU0yvdNLAkovtsUecMbpl62Yk1GRnZFWUSKneWKFXmIha5E%2Frykdc7Dyjz4ZEjt6%2FQcc70sp%2FN0q8I%2FQqQC2aEN3qokHcfagpA8EkyZY979QbEtt1jj6UQxGglhMheB%2FCIdi0%2FBXn7LkLqADmpqE2mnYmwcvR4nikpvrhuPfUW%2BjHPSeee6HnuFFMvLn0Zr4NPCIvqoXVoMBPD9lEkdN%2B8plLH6w4S%2FAmoWBJMunk%2Fs%2FAf%2FtXfu1zFO8OzREkwV%2FPun8PcbL3v8noD2DDRiQt%2FSigIpGrm5%2BZJ5AGBOQwJGlfgCEPJEgGFIexaGSPy59vRk25HqVBALwT3bHcU2YqF7wOssaQvAhtoTSnMvjfgalhhSArjOI6k83TmdVzTTdheMbkByFD6uQ6iSFuK%2B7z6vwsY32LC8bMMA30WB7BkcThsxBmfjQJb0kz8jrD8Ycsoie7UyFRou%2FBlq0ZwdVdbUcZK8kKCBWpwafpJBOKjvxg%2BeyqQ%2BGhYWujsNAv03Hrgsko5zvSqYSaSY%2Fd8%2FagcDE6pTWq353%2F58EWcWHiGZDUiAQgzCOwPi8BjqkAenK9RP1WTOuANJ4E0RNphbkQqfL%2BH8sdbfNmI9E8dBmLKkJGV%2FVpoy2QExmlsCtdmtgG6ZL5x3Ha57GnPloWnFVw01IyCqWOZarhUx28ISfefoNpunjO7yz%2Bg6JB4ZYjX5jGtNfUETUVu2Eb1%2Fs0aqrWmgsJRELLXGXkyu7HN%2BwDK4eWgIEP1nX%2FQNmtPhcG7F1RYGiqDwC9C0dtu5pUvT1nLp2&X-Amz-Signature=25b65ae5b40f905a24ad2447f1a067034ec224ff89d11e5f8da95983f618a605&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE5PPMSE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FCun6VoF5n9UTQFO%2F4OU%2BgSnMFNu6v7pHAIGfM%2FzHKAiAucPxC5IQhYh2ap%2F%2Fa637ksImaGbofYyxTmDRPMyWdKCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMN3eXy945CTXAoX2RKtwDLKTm5E0jdYcRU%2BpP9raUmfZLMEW1JN9ldg26u92EBO4jdVOOREzGdW2uEQ%2FwZUTxnbaRrpTfYitP%2Fjl3p8lNIrJKRbm9FTNWXb%2BIXpBy1FvgdeP%2F0kVib1cz7BK2pgCq9T320rfhY%2FUyU8IiTDIa9uwyjubymb4tS42BYFr%2FU4TrZJ%2FONbri%2FWe5YmY56p%2BQUFWIBoV0LSX73op7hcBKO0EqTuAac%2BW5q8rj59DEAe18t%2FmSVqh1SY%2FBTImlfx0EoNFApPDPGqx9duWelTd3vIIN4K1ogTINK6dr0LppyrhwyTswwjqqfwxtm1uOwHMBR7fmdXZy89LfZZdJjmeBYHzh82sCyZ8P6tE1fONKBZCFhDYHdDgw00%2B3dWX5JCdWrtIe8pE4wYgBpVBBLjYJ58aF%2Fn1HLgEGGfic%2FXf8dItcV6bt9j7n6hTuXWIsR65p6M%2B2AFFsDBBOVED1LpDKUPaUlESzU5qinREJH7Pqi37%2B4MKbhyfuO6ElShqb5lwy6%2B3o%2Fvl%2BuB4a52YjDqigMa5nglH%2FSt3wV4tqD4a3Egl1FszlISAB4lXiYkf%2FdfNnUJ7aKtvjs3uYCX9h0zB2Qd3WbVBK8JcrH6KZPHl%2B4lmPR3OX40jz4cSoM%2F8wr8b4vAY6pgGb1vjPMPBwjLgpnxKovWH2bd2jcddJPDV1YDTQ8ZXgtr4BD4DG7200chteVaNaIvY6FiWk4a0%2Fim4HyWlYYUMn8GoQjesdkz0GwAJHuqKJuPBqHGzCkD9BQknuyCknsfcUNy9g2tw1OwrkvMTgxcNGJ17LowjWkg8FflKEtDY0j7q4WcRuf4kd8Xgq7kABrcM4ATsI8VObpdpWEyb5o2Q4Ra8V%2Bb0P&X-Amz-Signature=8a7472e99160245f5a97d1840497d54be5c646285f89c2cd2c11aeecc734290d&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZQPNOJK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbT4KJSbaNOcfdwitt0TFhx8UtGiOL14kc8ao3yyQTnAiAaTh2%2FBM8W8xrTooHBd%2F%2Flux5esD%2BxFUzdQ7txEVzHPSqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlRpVpslq9DvgcDb0KtwDPYr%2BTeOJPrbpPc494%2F8PJSt1Kk12L%2BObd8Sxh3dY449jajf9ne4oCPbnTH18e8m0s%2F3iQrWRuyspGSfoVISoGGYDZ5ZFAUZw%2B%2B%2B8zGT5729BbJDS%2BpIE1uRjeKugRLmFHvuVow030cMOEbmrqs0ROt1bx4XVrQRsLOIM7XFYSqfJ3BoUK9t7p14Wulue%2B1%2FLpCmlf%2BYeB77pJlWKZueXsuwXcXLNLsDLT8A9Rn2I4lETIZFpI24NrWsPmj3JtJyhRuGdT8x48Er6t3OtxA6V7CAxBRlQGtiiShakyBE6EtpMev3DmIFErcWIyBWdedh1%2FKpVPOp8GMmAu2yxy35n55%2FYPRluPpAMZWiQbO7DE2QhEoZ3IHHceW7mKq0RDWaVPPdm74YZVtyp0Y7r4ZGEklJgX%2F7YSbVNgyW1wByRXEWpN6Bs1Q%2BlJhlE5xn2Hs1YkVlkLnA%2BBX3u8kD0vQGkJAGFGdgIR04W1VBVw91RwykkWcGP983F9vs2tdXwXWZo2E165IaYVZw6w7hScPyiitSzrT%2BxFADbYxzsadUuvvNBSpBbEsQbWbXUtHZ42n73mrQJq2EngIRgK%2FMGwRWOugqc5R%2FlPTuOuCbB3xmWgZXeWDNGXql0Lu7ZVPwwosH4vAY6pgHaa1HPJRnM3cX%2Bxtkes0sGe1XY3r8CVI1l0nKrqNp6t8QaUxsZVOMyS5pwX5elUXu48893qOiCK343986N9rY3vlTM3BqYI2MZN1poOy7BW1rL%2BE%2BJSHy8teA4ZZLdpNnUScLy8gcRQYuJr0gpfPKZCyxFLUnzIwoN0C%2F4TlKE5XOPReToOwdd5ACL6WV6y0oEMCzybNh%2FMvWU9e5nuUC0DoxdpVmD&X-Amz-Signature=9a399e2484896c9f0d82488b44b0ea0a2e839914d23c30cef7ace51cc5fc89e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOB4UFIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEcJbi5dIhy38N%2FllmwXMtvjUIjzLhRdVA%2B8ctg27VOOAiEAo%2BLcD41kVyGEobHnAmpm7FqSXAlcghFq%2FTyzALGofrIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD0krESCLqnmZvD%2F1ircA4tPRsa7aB4FS8p%2F48B8G9PXNSJBU4FVhjgei4UfVx49QjwXI6zPbCv4FrF4jYD0ugBoSWmwPwZN9Slatn822Al7fDwcNkLTXz6zE%2BBdlZMjszwbc8zhjteSSPHVuMkY%2ByVjCtzL9%2B7bojVIgJbvJOTE%2Bs8ZJGQxGXse4dCa9SLLD%2FnX8Q88jLH2E3F4ypO9ZVVHtzgLsAt%2Bw974fNS2nGpcZPQLsN0oXngEugoBLgo2hH2JDwgktFFZochTP5UzuOLr%2F4CBWDtF8ubiWI4WhVsjL53HaGEuyk4%2BJHoIdYRxlS5USoNnMEPi9UYxUa0AjMoaqutNH3Sgl6Zm01JIS%2FUvwDn5yMCkeHjppnv2uUD92XHM%2F82bZ7UgTY6cnNIcsd0WzJdqiV2OhHhobdH%2Fx0mAFzMW1I5DB3Qt8%2Fy5RUxZ9RaTGzCT8nD7suuO55d3MPlAW0RtgnCENrnOvb%2B5X6E3%2BE8pDTRLKJjPb%2BHv0cxG01YCZZgUMm%2FLtFnth3CGBYBxKEE%2FtaJNUhrPYDGfZASxtRJXZJSz%2BPWawUhwDUZ8%2By%2BvuCNkpnEEL63krOx40HnLl8L56WMcBlbuxMo4lKP9tNPVe%2BzoV9BEO1Kv1mzjLOI4hPXQlkY6whXkMLrL%2BLwGOqUBOKxNtZPQCZkopZrgEPk2vzbSk3MQ5vZOf1%2F6zu6m2LQVD9IFi4UxlwG6dhfYg8Mh4%2FXYcFRHKFUR7AtPLz6ytV4Gp3YuSu4Bbsrv223kqN1CRov1hq0LdZGPCyxbdQgCDV%2FIHuaw5o0pEfyfoe1xKU34ZO8by6MetOh3YdcVesCL3OZgqnIyuKWm3k%2FjaZ4tDUDJeKf%2FbW1rr1srULiKKYYh1q%2FX&X-Amz-Signature=bddc0cce8bbe63d302472f1b1021ea6e773276036798b0c477f594df16f0cdd2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRUUII2Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVRGJNURGOuLqmMMMENJ4LTw4QRgBVHoC5VfUc%2FKP8xQIgPNDgR85PHi3H%2BgWDkWg9a8lvYoIa%2FLfRsGmFu4afYC0qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKB6y6tjyf%2B%2FcCrEFSrcA%2BM3Be3ZCR52a0Th089b02WtfuWJAQ0MZwflwuTR1H4yCRHwiGedsZ2lZhnzyrWqgIYsMrr1OtMXJlRiTACpifePRYMux8Ik6zctkfMTCkumexCn5a3GbWddWJ7Cm91ukckJ1%2B2dcCvJmRjRj3xkWaXlY3wN9%2BVFSa2o2ahw1QNsi59B%2BfGxA6sm4S63vZlnDr%2BYxzUEGiValzIxrwPsItYnlWT4oCySKDR0VO28xI4W88aGbM5ohzJNDVZyiEUZ%2FE2AeB%2FuAxZSg%2BsNlL%2BjF2hDRfRmjJu5IXJRRKyITIWXx5xNj1hh7OZAndNXlCdBkWlh4Y057vIMpOilsn3rS4oIXcsJMOYwdRM2lVxfCy9%2B%2B4nwpZZKAZlKqGO7Bwi%2F%2BsPaVjEDx5jzfU3bjH9wKia2LLoBTkbjsW1SbtbYHQh59CVaBhwZqUddp2Uf1j94iRjh1YkGwPRZuYfeY%2Fho8SZujXxwp152frq5tpBmaJIZrKK6TYhQ6fUfSXmgQNID8reQh6q5B8ODwl75mmnZxUuiQufWRsc%2FPrAeIICHLFbLz%2FOcDtZqCR9p4xrqOhpYlnlzZc08Vc%2FY7L49Si4ZijK%2BYw%2BulpSFTQXbPCSVBMK4WvQgJ02gajiqdK%2BUMOvH%2BLwGOqUBY3P57MoXZEiHnhP5jIlbOD4yfi85GP9HRD9IFw71rkZtr81LHs6vFwSb%2FCvJrwaquBAk2t47NT2P6yXkZSuVGNOyBo4FyJgGSfnu%2BER6%2FNguSfuzGimrx0M%2BSDWDDp%2BVgdBLIca%2BjPKfEqIV2lXNa8x82wbxMjAiOT1IvhMbMcfedowYM5HHmIWWsmuYXwdGXD3CGNjGdEyeoSMkkqMdvknGvkrJ&X-Amz-Signature=5f420ed43385b1051b1610ffc5ebae55f300ef67b312a46cfd90904b72746977&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRUUII2Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVRGJNURGOuLqmMMMENJ4LTw4QRgBVHoC5VfUc%2FKP8xQIgPNDgR85PHi3H%2BgWDkWg9a8lvYoIa%2FLfRsGmFu4afYC0qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKB6y6tjyf%2B%2FcCrEFSrcA%2BM3Be3ZCR52a0Th089b02WtfuWJAQ0MZwflwuTR1H4yCRHwiGedsZ2lZhnzyrWqgIYsMrr1OtMXJlRiTACpifePRYMux8Ik6zctkfMTCkumexCn5a3GbWddWJ7Cm91ukckJ1%2B2dcCvJmRjRj3xkWaXlY3wN9%2BVFSa2o2ahw1QNsi59B%2BfGxA6sm4S63vZlnDr%2BYxzUEGiValzIxrwPsItYnlWT4oCySKDR0VO28xI4W88aGbM5ohzJNDVZyiEUZ%2FE2AeB%2FuAxZSg%2BsNlL%2BjF2hDRfRmjJu5IXJRRKyITIWXx5xNj1hh7OZAndNXlCdBkWlh4Y057vIMpOilsn3rS4oIXcsJMOYwdRM2lVxfCy9%2B%2B4nwpZZKAZlKqGO7Bwi%2F%2BsPaVjEDx5jzfU3bjH9wKia2LLoBTkbjsW1SbtbYHQh59CVaBhwZqUddp2Uf1j94iRjh1YkGwPRZuYfeY%2Fho8SZujXxwp152frq5tpBmaJIZrKK6TYhQ6fUfSXmgQNID8reQh6q5B8ODwl75mmnZxUuiQufWRsc%2FPrAeIICHLFbLz%2FOcDtZqCR9p4xrqOhpYlnlzZc08Vc%2FY7L49Si4ZijK%2BYw%2BulpSFTQXbPCSVBMK4WvQgJ02gajiqdK%2BUMOvH%2BLwGOqUBY3P57MoXZEiHnhP5jIlbOD4yfi85GP9HRD9IFw71rkZtr81LHs6vFwSb%2FCvJrwaquBAk2t47NT2P6yXkZSuVGNOyBo4FyJgGSfnu%2BER6%2FNguSfuzGimrx0M%2BSDWDDp%2BVgdBLIca%2BjPKfEqIV2lXNa8x82wbxMjAiOT1IvhMbMcfedowYM5HHmIWWsmuYXwdGXD3CGNjGdEyeoSMkkqMdvknGvkrJ&X-Amz-Signature=43c060e80c3bf5b0cb41205b504cab63bd7c98f1616bf530ced65181b0129fb4&X-Amz-SignedHeaders=host&x-id=GetObject)
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