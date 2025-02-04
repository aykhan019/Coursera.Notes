

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BUUXBOE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIFFsCuJaUDxyGR9vWmYvGImnQrR9RRZDhnCXLm9qQZZPAiBEgNRBSYI7bY4062zL8gMDugC6VnymKYSwMt9AYdJE%2Fyr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMvjqVuHjFaXiPjFpwKtwD2Or6H%2FlSffeA2R7dd4IkL2svDTiJDNbfjvqzCMGUJKvnpeTyDPhKl6hKyOZt%2FtD7%2FeJWjfrPzd75qyGiPn5z6BzxJ6eaybhimu9HV15BrjdLK9OzLUOoNmC5no%2Bd2KV8ZbA9DSFKbQfmB1BYrYQErMKGLuBzDESsiJMDK7TakiEQG6w2vPmInzEI92avn2LBcqx027mNUkB1JDKk98SFMbnUHYWpdOzEYDqU3HgCqiubWVqr6648ej5qjTzrdzq9aFVk0bfyjt%2BzbozPFS5GqxjDPhc4rUGTJ5OF58Iv%2BsoF3n32gJEurjmaeuVg%2BpYyGG%2BNLOqc9rGDmI9JuM8tjg6eUIah0KnByMP3E4zsMbIRNCOdEXSTCW72F6JayijEcGZfdnjtD6Ov1ZN7SrsdEae28k8Ycz83xYpKlaBrUdMk64FR4JsCDG%2Fd4y95zUbf1qKSwvrfcEDx%2FYkWK0SnkPJJigauoo3mMeqXGx6AaEcIRlZxN05g8gVYv7%2F9UpmJY55wtVJq3ICUr2xLn4BJO9tmrR%2FV7%2FNtSuaDHVrBFD049eOtJ1Y0mi5bgTl37FxU%2BMxtOR80SYYKMLht%2FHKXHck9LovqWubNXaExZa27o4OqFSS5R4O2mS7Z%2FXEwt7%2BGvQY6pgHdAitBNVKT9ZVRO8mLFSsagG6kuRB8hBURKhbFj0zPEJ%2FWwfQJK5OtmNy8lD3CITA954APedskh7YgquiUcEbu1EaSZgWs4kzZ5HsJHhfJWUNPwWs9iXr9apok%2FEWbnXxHUbYoK7ozi84we7GMhnig%2BxSz6TP5pygpM9fJ4i1J9OFZCJ1mKI%2BVKRonjVHXW%2BVCYQtHolvvUzGvLJRiUr5%2B6Y1Ilon8&X-Amz-Signature=9d767c8b7565ed0bd70742899fc3296e4830627231afb5db7a201f639299d2c5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LM7MPVB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIEG1MZXZ0o0CwDp4Lf%2F0VSXLpqmdhU3nStkjv%2BHbNVOpAiEA%2FmtRNOnXtWP%2BNWy%2FPVyWQNKmbIgVYpkoca52rY36hTgq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDEJimf3gs1fh2W9B1ircA1ii%2BJaG0R8kxqel6dbu8PO2i0fMg8X5w8Ah9rrUtEOryuuIBXHNZDHxScw1YxpmciD9rh8WHzJ3ME4xhjS1%2F9%2BSzqqTJeZTjcjmYcaBRuMR1WqIoylqYrGmWQkRILT9gaMFOBu9hXy6E8f1bQDO6%2B%2BFQB6VWC81YFFrVpiLW5NFRIwjdJeeHDZK7LXjHmnp7bbXc6bf7smxVHN2nnwLJ5SMWZkYUpt5o5bwnp2Ty6ZeyAuITdNNswO%2F3CL68xRVJFk%2Bv%2F%2B%2FFqBrG9ZVF%2BgB2jwD5ZdbCLSrCxreAGrpl1fZLUOwyqxkzLuqpD0t2%2BinGnLoOXgNKaDY%2BDnEyNB33qMryr73yV%2B0PXc9aZxlBwgXh2gc32WWGzlpk8uRzznurgMA9Oz382By2v3igV1G8ys70%2FKITLxm7ZJNtNZCa661xODivnuzk9GsmSRsH7mH1qseXgbnvL1Tv6O8JDsgfs5x9nrmGhshQIdEwf%2BYBEPH3WX3uj2yZNLZ4Tf3XDmdpGlPV6DFBirjFQVm3T0DL5i0ZMZ%2BEqsD5YCyTeqMuNUJFDUhqj3iekhAVot8ID5gyg6wQsDZrtfzJd6IFfZ%2B2mLfWFmDI8LzEtsmLtnotjz0GZR8hAjnZvKyDxfIMLy%2Bhr0GOqUBmRkTJ62%2BS69bXVuoRDCJCTYBHj2cdT%2Fbwdj8Qf2zkQewjZ164lY7su9XJHNCgNUQz7HU8ODM4x1EIl9rsdTTY%2FCZnj0GIZLYzpBokZjZKY8Ds9%2BRrSXQ8LWyC1qalJ4aIoJHgR4qMMz%2BPSH9oYp%2F1VoWnN1PMitS2fNXydJu7Hsr61FyD4fQtQ4AdgTSq3HXC1hmWv86fyXsdKQqphA2TxeRBu59&X-Amz-Signature=f95a2f95dc3a81decdb7e82fb6ecf664907fa492a8f3501c96ce70d648ad29a9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZWGKZ4D%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDWXnVEMbHofDN8DQmh9g3or14r3wTXzC6BDESP4VYS%2BgIhAItWC1vihH5XrUVpiYrBzTrad4xLLXtB%2BvMce08WPU%2F5Kv8DCCYQABoMNjM3NDIzMTgzODA1IgzaoXEykODDci2YGBEq3AObqsDP2AUd4dkhsLO6ymBnn4y1hinszlcldY%2BxlKBZSKrph5b%2FdZ3lslt18TDsmF%2FLPLU5pt7ZuaqM8Evv%2BdFXNQunhskDor4Co7YFd4nOjouFwiZZRQlIQykNEK%2BMeEdtHVUFGU6n1GY6PNvh7PUXfpw94wmWazmx5WgnyMqqYYtqFpulEcgTHoP8evxn5Ra5XHo7mejwDJpGLbGWOFfx3pzfomMjRH%2FENg9Gt7xD%2FnCMqQMNr%2FdH6uDnoi%2Ff4qEFh3PmzVcP2%2FWyiSZKCeC07jFwydNSfn3bv2DF5M%2BtZvXQsRMu2po%2FJMPT5vA%2FkglOuw%2FQ5JcDDE1sie3DW3z91RFp2SSo7WSTtLjG4UfqGi4pfBAtceQUUjtjXXBSNDajC6aZ5iG5xfbd9LpsMRf%2FV%2FZfwwk%2BK4Z2Pn5z3A9paEnYPLdkpAKg1I5HaX1XbUdI2VMcF0VvtZvPvNfANhBiojIFPErf3W7zbt1gn3M%2FrB3%2BHETt7P2JSnADUeLDI8Fqu0qPsJPH2bLYQJ3QURrLwIKfVigC6MC29xVJI3%2FAOWF0HvzztON852%2FD9hQUIVqLkpqeSfYGXxxbWnVnxxnBpttgqo%2B%2BtiPN0%2B9HIYWbutQQFCjapfFMtLZygTDSvoa9BjqkARXkvDQGF5hl2eBWdFVFSdvqNgPDeftQkBehFNYX%2BZOQ9w8QVbl6WrXziVhtsyRMZf2Mrz09gGDSVi%2FwWhFXaji2MckIOal42GRZ563bmZ7TDEkZXEbq34EIbPeueaLhOiIfqZV1spmMlyyF59HOWA0LoR0e96v80rE46iTB1WZN8jcPHUWN7PBc5jWX5txStYZKrsIiGOeVCOX8y1nL089NACTg&X-Amz-Signature=0551e0b4031ffc64f502cd65d8c507c3121c95206cad302a2e778e54c46a5554&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSA32AK7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICEVtl5Z%2Fw5P99Jy95nVBCbTycpmcrNB6B1sOruwjyPlAiBIFSxdUJz4Hn3mR7VxXDFuSIkcV0P%2Bo989NTZsOmA8uyr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMX1L8aWnmgEDxcPKFKtwDCPpoAtba0USOnER9GFuPHDlLdH5ZCFJ6Gu58eZqaYbWhPSIzlDnR0AcIgPZUuiI%2BvoLk41aWlU1pI3lBMTvg8YFkeidqUe0PkxRWzl%2B6uSCzLhZZuQaj4MnF0%2FOY6E8u14vAQhmog9o%2FzPU5iQAwTueV3VNZjz4JKjqpaoj6KSv3hEwSpJ1zhPfGg%2FwPcdxg9ar7%2BshgAGhuLNwjqYJLqSkQAJxsGXLcf2ZaBAJnO8%2FCOiZI8cAqljz6o5AMSkgD8i4ZEsd%2FHSOzVsufkuIuj41p3g4Mv4fVGn59XeKI2Wulugt3WXH86ZDS2LzihAhTbj4Vw5kORaVDRnYFwB0xAfrvXicvbu5avM1NLNSqwgCHfaTJkqNCCQyXjwVy27QkvHYwnSbaEKYfV2BhXfrnTIql%2FVA%2FaCmrJPQCtTeaIOZwykE1n0IjCea3LuxSvpPvDbmkld579ZmNGpmnawoJakz%2BheqqxMdBfRRqyIneVqlFlqawlfbKVm88XCn5AhYnxNQqwpaVPBKUr2Sa7nkx0pwKONVXiSzGpm1YKFhmOsKxPAOH9KbEsdkSxib4dkcdjvt941xJHT7yTa%2Fio0X4lySLGEjOoL4ZLaq3n%2FKqNjia%2Fc2tkGiRhmhrYdAw6L6GvQY6pgFW9M9I4eXugR2w9RjiMIRDd90zOGkGIThflirhFoNbcc2OACZOEZWeRFT2FxY8bpfXZaMunRuAwKlNQ6t4knn2ar%2FkFLiGZdZq3M%2BoloCaNf5ajD%2BWyz2voBEJR8PCkDCNifFDEb5gRv1cteI%2B9O6%2BNEerZnNbEQPYo3PBZc%2FNQ8d5Qig8rUWoiZuqSjBfu09whDjJeKDDvELfbcHwQlNrcfwEVAWg&X-Amz-Signature=d4ad833b00b66ed2972555fc3c85d7084054e4b917acafb61efff31b8532bcfc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDAGTYEN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIAxl6Si%2FoRJacrkzsAU1nPcYrcrG%2FCnR4ytZeZrzXEzfAiEAoiDiD8%2BivSKwTBY0zcg%2ByM64auszEfmgzZ5ICC6pRtIq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOome1oOFJdQYEt4FircAy9tdJcXT%2B2WFEGKXV8exD%2FrcqirPFB4ELBgngS28csNmzNy6pztR54Q8UcpEcHWyfz3ln%2Fwdz95GfQk9zeo0ob6FL5I5Zddn94Jo%2BiQJnstMepR5hGjn9TS9Z9WetnHUhUjlFqM%2BBJYhln0wkyIDgrUiahW895o4AvThabWpHIkE5QUUPysi82jPU8sI5hHe5rn2gSoPGVdefi3TzF5oWEd4l2s8ZvLCKp%2FJ4MxvW5MW%2BXWrQKKqJsfWrcQgganGI5HlOcBwtuVhCzsYavujKBHvl3bgR0V0I7u4OAL%2Fj7x9c60cZ0ei2gP2plzX97njg6e33Gpc5ANAk9ME%2B77aETQEqD2AWJN8fPTgmxTddTKYeq%2BHa7d2tMB%2FFR2mvRyStu1IJZNzvkUTSFwjYzD40aH9IQ2AI64f2l%2B9GpNvkMlrHmxQ20FANbUjTSIK4mjDFKToGYai6fFHSWhfPxCIXSYC24DBshz676L3VkNAZFSJXnjxUc1ITc%2Bs%2BnLTbNJePfoJ7xZ5iqtctH%2FhaXgPK3dSuM9ipT4ogvAxcMuI7Sn%2B%2FnltMXjCb%2BRvGDs0II%2FzkZPboblT%2FvUNLJJGSR8wMI8CTxuGKGY5KxnNC9dC3gOI1q%2FnBCFkHsHNHTRMMe%2Fhr0GOqUBUfV8Pp0cI0BsueuzISWqfBbKq5fJZ%2BMs0Orkul%2Fg%2FSOpIAnFysDstSYiaXRQqbPI3fit4oxzr6RAWf0tpKYifGf4dmgTLQ5Ih%2FhYLAsOLSW1Lay%2BTWrvDvbsH3pxk6kKnwBDvK3hbogiAOLhI8ktvrQE0Wyk3SaQi74aqIpCUwMeif7FSURSCRUKBssg0y25mXnjWNtC40dhT833BtycWZwDn46I&X-Amz-Signature=572805492ca6f9266ae5729a1cf9fe64413fc320b23f24c1024f47bab87a4b21&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KXIYLTA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDj3pvcbOOM%2FjQjjnmt4pJXj2i5m177qZJo1N1QbILu%2FwIgVUlXEvSbGtrx4bBK4v9gI%2BBVDR9K45c92k6Ju%2B7MgrEq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGRyiNkV%2BAnqhX1G3ircAzX31McQ%2FFAu854mEZOkpg0ZOGyGaXPd9%2FE%2BuZAcSlgbraOz1Cni4ffa4vr8P4c72KH8lsXqSxIE4ARFN4jrPHL2ey5XZ28POzs1MLet4JBVsTY7Ao%2FiQcxxgjc8QGYc12lxgBs3deT3Ic7GRdviua4Cza8uLgPtqkiC9NnwQS9Kbb3Dz1l%2F1ArqwfK%2Ff4abLUuksgG6JFOLtoeTsUizctTFH%2FZkAnXEIS67OVrzs7%2F%2BkuESBdGmRsnIdWvi3wDjOTJFcF4N%2F3ZkBagUIfkb%2F9JNmQ2L1Eq3O5PSRztEezNzFDbmugWRjmUp7Dofy3pQsofafW02ljNG2DiDn65pjF0RQyr10n4McCLmB2gwf3UvwHkAHl87lCLhmt96yJOmZTaK7CH9rKZ8eXJ8I1CSYAVaotRgKcCogoR6gFrTwQoFy8NPlsDCSbWnXSatmIDg78quluxa2fQEwKbRh6brZ%2BdXTxYxfcB%2Bq7MiDOyrjLtiDkHfZZQOquutPYimY5YhiPAOzBoUe0HPbUGtw%2FN36H%2FCl6rMC2%2Fz7MnfXdWZqu6%2F918I%2BQwuAX%2FIywDBsWIgaE76sT3RuF5vD6oQE9DPo%2BrKsSBeBC7yIt2yOISKu8UADtfEW6A2Zxhrf4uxMO6%2Bhr0GOqUBIJxztTTbbBbdbekLAchDOk%2FqGlwG1RtG3u0rjRUJtOzvs1M0FHRc5JUttSf3agoC2Ss%2FW2XgNtBtpNeJBQPjkZfohVAyizdjukb%2Bud2fv7mSV8oIABkRx3KAL%2Fyn7kWf64tm28oveRaOyb4H6fTZRxB4EiHO2Tg3SnC%2FHkXxFOH1ePOMve%2FcvKR%2B3YN1hOqPp7fmpYfbKoiZeP26Mny7y9xqgvvD&X-Amz-Signature=acb3773fb2f770d807e0ffbc0b1e732b264af00587b9ed2969561c86cba13667&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCEEBXZG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDnjhZod7McRratPdPjAvoI59g5aCPt3arP2ONlTQ9zEgIgZNKty9pp0aliKaFYfQsqyM45BZj0TOK%2Bb3hAqGm6e4Aq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDFwga2BOgBGDvxG7XSrcA4W0e3GQz0c%2BjAzmIYQwqMtnb4Px918YuaWiYsEKGFNhd%2Bp8Js9baWj47siott%2Fag0jCuFi4gOEhJVdvELRA7ZwWamCn15C7Rfxbmmcv%2Fo2wG%2BHI8qgEKsH0LMe4tssfNTLXG6QnOGsIVBcJTH9XLoZopOzjHgPnFolTgKe64BzkdJuc4nZ3JnKLy6%2FFNK3mClCi6BiVL81rH5j6ETcrwEY1s8YGIdIlIPhx8WXNzo40IKwaDSkgTf5f82X7%2BOmMWap5f%2FSsbDHNGBNXUFeaRX0LGSqfychEpwJ6EDs6WGiYY7LUWqMCuzSAZ3PLJ414mHGFES5wnBLyxrfVaZjZk8g1lr7rUklhbgtDjue%2B33YYkTeR1UcaQx5Sna%2FUy3nwITK2UPZAixPauHvcr168lJ1wcK9vfz8uje1ZqEXsBx57W%2FBUzioi%2Fp6wmd8EPzL6OdZ1BWU22ovs2sFed2wQC18NnjUX3%2FIRAf4wpJwTeFKj8TeLpjWj7fdHqEOQ0GLSjMiAkNCTP8xid8jEb8P4mFr7UtQNm9gGGRNz0owRe33cfpOBnT52maxJNdYxnXs7YI%2Bq%2B%2BLb4EObwwfhvlfmCg%2F7vLSD18TLTVTmTIyARtBTQiwJfpN%2Fxd4%2BYAB0MMW%2Bhr0GOqUBIHTDdlVdZt5%2FB%2Bb3J5R98bDqVo2ubmU4rg90EmKVvtmI%2BymEk%2B5UmH2NaTKjR%2FM9pfhITU9CBbIFKzgQY%2FUJ1YY9bMlXinE2vjtXiRals6v7SKipEfoP%2BC%2FQSaEQowEoDFiO9HgofD3zJkcwya8NzUlY075yK6bt0Q6QtjZS9SLhZqsIAqAl6K0bm%2BL10LL5k9%2B35UmCMi0gEwtXvs9w29fhoQFS&X-Amz-Signature=4adb7129f8252bfab2ec8e56ed7812e568373b35e7b218724229f988e314822e&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNZINLFT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIEuT29HbKr%2Fv%2Fs7F1Jv0vN7j0xeQzYaC%2FzRGGla4zebyAiBn8wXUxGHTNDR%2BrRR8dHmb78BYw9py2Rn0vB21e%2FJ6Byr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMkJaysWc7neSBl9e8KtwD5UEeYX%2FmbZDeA3zmZJMVRFXk7u%2F4nR5BQq1T62HbOG2CR7gyp3kSGNqQC%2BNblOxG4YB9BraCr%2Bixecfm%2FYEO%2FSDcVcx8zF%2F%2FjwlOCRBXx40VHKNt2%2F2yGTQN2OjnT3ySZle6OvuTwH11PysmRBB8L3m33RscjXMFBtFG2qDrf5Cevx1ZtnjMd3CIN6yZBwyRw%2FG1G2P3lIt6eWG%2F8Q7ePZIFfVmXYe2jJveWb0%2Bio6fQkS18dWmK%2B5ntxjawb9mrgdmwkGl6GAxGWHVz3EmvIbErbbOrvYIRJcNNVt5G3j4y%2Bl1yIxPqI3DMykZBE97xdbrtJOaKxdVdGevCdX7hoMfXM%2BQ7DX957kvT3JlOQ21%2Bivn9xFRHUFQ48qsFJiERJcJaTnlREusfsGuGkwb1Kx6w8GByQRHAChzfOF7M%2BOUstnRkeZn4DsEjbrH1V%2B2%2Fhzlk3q2RLvuD8qM9B2PVVjcWa9t4leZVS9jh9f%2BxqrSGKb2twiVG3%2BaxcNKeT8%2BKD7aO6LVW8nEzC7jbdZXB%2BBtcfVAxZz7dbZaWJziCzRoup7vNWDXjGlmIYYnzRBSFO2b5QdD4Tny40y2DcBaslDw%2FZA8t9O6ve3Kh%2Bkcnvo1OJgbJGx8%2FWcdv0yEww7%2BGvQY6pgHp2EFBROOnLJ7RQrE2bYn9G4WrWMbP8wDXKCSMtnitFlq5sMK%2B7zQ8vvLe3YXKxL2KP1TaKFGMfo%2FAigMyl%2BFZeAHJ3pysi7A0Lo%2BReFCTiSl%2BvVb7%2BH6x%2FTEj2rOSH5NSfAxHn17tXKHU9diyQemcPY2qycC9oZRXZpzAJynUWaskwq0d0gNrDocrUEHlDHkJ%2BIy6WIIsvcpZULP7ZchiIBCqY29C&X-Amz-Signature=b15d0064dcc361af7753f89e6d958efb7981c189a1b880b75c04b6ae839bb3bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDAGTYEN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIAxl6Si%2FoRJacrkzsAU1nPcYrcrG%2FCnR4ytZeZrzXEzfAiEAoiDiD8%2BivSKwTBY0zcg%2ByM64auszEfmgzZ5ICC6pRtIq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOome1oOFJdQYEt4FircAy9tdJcXT%2B2WFEGKXV8exD%2FrcqirPFB4ELBgngS28csNmzNy6pztR54Q8UcpEcHWyfz3ln%2Fwdz95GfQk9zeo0ob6FL5I5Zddn94Jo%2BiQJnstMepR5hGjn9TS9Z9WetnHUhUjlFqM%2BBJYhln0wkyIDgrUiahW895o4AvThabWpHIkE5QUUPysi82jPU8sI5hHe5rn2gSoPGVdefi3TzF5oWEd4l2s8ZvLCKp%2FJ4MxvW5MW%2BXWrQKKqJsfWrcQgganGI5HlOcBwtuVhCzsYavujKBHvl3bgR0V0I7u4OAL%2Fj7x9c60cZ0ei2gP2plzX97njg6e33Gpc5ANAk9ME%2B77aETQEqD2AWJN8fPTgmxTddTKYeq%2BHa7d2tMB%2FFR2mvRyStu1IJZNzvkUTSFwjYzD40aH9IQ2AI64f2l%2B9GpNvkMlrHmxQ20FANbUjTSIK4mjDFKToGYai6fFHSWhfPxCIXSYC24DBshz676L3VkNAZFSJXnjxUc1ITc%2Bs%2BnLTbNJePfoJ7xZ5iqtctH%2FhaXgPK3dSuM9ipT4ogvAxcMuI7Sn%2B%2FnltMXjCb%2BRvGDs0II%2FzkZPboblT%2FvUNLJJGSR8wMI8CTxuGKGY5KxnNC9dC3gOI1q%2FnBCFkHsHNHTRMMe%2Fhr0GOqUBUfV8Pp0cI0BsueuzISWqfBbKq5fJZ%2BMs0Orkul%2Fg%2FSOpIAnFysDstSYiaXRQqbPI3fit4oxzr6RAWf0tpKYifGf4dmgTLQ5Ih%2FhYLAsOLSW1Lay%2BTWrvDvbsH3pxk6kKnwBDvK3hbogiAOLhI8ktvrQE0Wyk3SaQi74aqIpCUwMeif7FSURSCRUKBssg0y25mXnjWNtC40dhT833BtycWZwDn46I&X-Amz-Signature=34755a519b758881f0d500c909ca05bbdc7448066fca8d4a6e43cd794a35734f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJG64RUJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICLWiUrGlI7CR%2Bi7EJA6%2ByAvVBdm4KodI%2F1naK4AIbyGAiEAmbkRynNMX1KKSpRjyzwRIdns5I%2BQJFXK3MV0TRE%2FK90q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMJLTtr2ORHMuVVGmCrcA85DiWY0%2F%2B29eVNbRoW0s3GFBHqijydVHCt9rh2qv34mzSCGXhzHWrw4SYxpnDwLiql9quh0c7UGfyRf4laIAZjTjGnt05PHOS99SW0JLtSBVPeq%2BS%2BuKXuIjcbIJDA%2BkDjH6HGyJoGgSUtGONEvxENq6X2w1%2BiFM2mkVIHSX7660RTSMjoighTlncwIhWjqU6mxqdLcGKqbrew4JjmcKO7q97OCYx3XcZ3nDKSpRibeb%2BLzcS6hf6NMU8yzJoSt9uPqIEKXUn4HdbcvRGP564EkHrzpa9nqhQS2K1ipHbQTaSUONF85n2R4D93Ydh5A4jdx75jwDDWhv%2B5pariHIi3hkprlP3cXdQLJVE4uUcxssxzSI%2FT1m2LXhrn2du5eLsBfa8DzvB6wbKt%2BSc8xzP7m9%2BOO%2FB2OurmJmb28u62f6vtq%2B3pmhERoKvpOhC6lkrZrW389%2Frv9ESmIZDOIA7T6S9ZtoysmFtGFXVFC7mFB8RoG6Vf5VV1mymTAbw4f5L23BOhm0mekkzgOOp35iFyGFt7fylEd6mrTEm5y%2BAcK%2FsQmuQcpV6k1TYhaxdA3KpVGfo8XpLeCmt3Zewb7HaoBfCfYHeuwpxI%2B3rarRYbG%2FoG%2BF1nXY%2F0DDEdWMIa%2Fhr0GOqUBj69V0I2II1KtCwiRDpPuLEaUCfXz1dhTmntYYrF%2BiKZYVSDSiFQgdRyFu9R8lC7uOULpPAy8cLaQAURu9kXT%2BaIO7rFAkL3RxTk0CouOP4ItMj30FXjqd%2BL%2BossMZu%2B%2ByNML%2F00TipkxZp5SjT5ZBniSNgh%2Br9jbP78Ep3UNKMWcTYQo3TUg1bNrBmRVTtUPtG19obNv%2BoUhozw4s%2BrXreMb2y5g&X-Amz-Signature=e8cc268d22e1b47a0c6aa96abc882495b86e44426d9961513210442aa9355cb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJG64RUJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICLWiUrGlI7CR%2Bi7EJA6%2ByAvVBdm4KodI%2F1naK4AIbyGAiEAmbkRynNMX1KKSpRjyzwRIdns5I%2BQJFXK3MV0TRE%2FK90q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMJLTtr2ORHMuVVGmCrcA85DiWY0%2F%2B29eVNbRoW0s3GFBHqijydVHCt9rh2qv34mzSCGXhzHWrw4SYxpnDwLiql9quh0c7UGfyRf4laIAZjTjGnt05PHOS99SW0JLtSBVPeq%2BS%2BuKXuIjcbIJDA%2BkDjH6HGyJoGgSUtGONEvxENq6X2w1%2BiFM2mkVIHSX7660RTSMjoighTlncwIhWjqU6mxqdLcGKqbrew4JjmcKO7q97OCYx3XcZ3nDKSpRibeb%2BLzcS6hf6NMU8yzJoSt9uPqIEKXUn4HdbcvRGP564EkHrzpa9nqhQS2K1ipHbQTaSUONF85n2R4D93Ydh5A4jdx75jwDDWhv%2B5pariHIi3hkprlP3cXdQLJVE4uUcxssxzSI%2FT1m2LXhrn2du5eLsBfa8DzvB6wbKt%2BSc8xzP7m9%2BOO%2FB2OurmJmb28u62f6vtq%2B3pmhERoKvpOhC6lkrZrW389%2Frv9ESmIZDOIA7T6S9ZtoysmFtGFXVFC7mFB8RoG6Vf5VV1mymTAbw4f5L23BOhm0mekkzgOOp35iFyGFt7fylEd6mrTEm5y%2BAcK%2FsQmuQcpV6k1TYhaxdA3KpVGfo8XpLeCmt3Zewb7HaoBfCfYHeuwpxI%2B3rarRYbG%2FoG%2BF1nXY%2F0DDEdWMIa%2Fhr0GOqUBj69V0I2II1KtCwiRDpPuLEaUCfXz1dhTmntYYrF%2BiKZYVSDSiFQgdRyFu9R8lC7uOULpPAy8cLaQAURu9kXT%2BaIO7rFAkL3RxTk0CouOP4ItMj30FXjqd%2BL%2BossMZu%2B%2ByNML%2F00TipkxZp5SjT5ZBniSNgh%2Br9jbP78Ep3UNKMWcTYQo3TUg1bNrBmRVTtUPtG19obNv%2BoUhozw4s%2BrXreMb2y5g&X-Amz-Signature=908d6228750e8de27be13c6862ace5c8228f03d01a0b1224430ad1fb420bee85&X-Amz-SignedHeaders=host&x-id=GetObject)
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