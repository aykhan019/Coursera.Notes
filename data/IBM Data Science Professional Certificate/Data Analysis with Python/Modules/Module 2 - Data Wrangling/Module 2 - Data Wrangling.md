

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KN36DGR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2czkf1PJnLVFFbzsGl8c0aNq3dHnm6ZENXgSyYLCe1QIhAJy5YQSAe1kc14eQkJwggnMcP%2B3YbQxbVFjex6aWfZmuKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyIyBcXKc7gE3jwkR4q3ANexpMsKiHgVUw9jpPmDsuiMhqAkaUubAHTuYSVYyNY965UdgQVpgD%2BMlaWo4Bpxhn3oxG3bWi00Lyd6t7j%2B2gWsDV7MOON25PR5fmP1JpHJS7nXCE9jOygpkKE2ShXU82xwi35O9eOSJX6HOB63ci87WThaM9L91URtkcjDT43GP1%2BG05KaSw8q9uK%2FGZBleaKRmUyYv1qguMK8yiN%2FETI55HVBQqZebyz0Tzr7uNAWRd3jQ7dAIXfqN2vDo5CqGUSzw1X7JusUOpgpGARk6NdU%2B6A%2BuFHOjAXPqc%2BUtJa7Iw2tuF0b3wOaDk2NmlSJbjt%2BDXf72O9or4xhovh2RbkMg%2Fd19tYVaP814YVa5fFACgmWnLyvTORlxu5wj6CTujEwvFNY8spF3wj9VzKgP8CszzW8pY9GotgbsdrPaZBjkExeLg6hsodxJCZI1cmtqTx5BdYVeE1AHEhQOonDd7Niw%2FFSXtkpzqQ5RvPXR2woNzZeE0fkjcH4WqIprLHIi37fEp6IaiR5BlLGhS9JpPGLtUOA7C2Nsyc6Tle1TP8W%2FTJqwH2aoUW0304zr3DMgm6X9FeaU%2BaNJh8%2FS1kpO%2BX4EnFvt5rQgnR71pjRKcZccKKwewpApl4SFzC5DDYv%2F28BjqkAURqf5Ug7d2TcsNQk5V7uRfy2U8%2FLf48e9mxDpxvliFgTG49GhbKtrea1bgswYz8pBovl8iqg6vQZmtZpEWouj1%2FtAZYIhtQOXspjgms8%2B1FJpeT%2FOwU%2FPhO%2Fpx7Z66YZrDTFKBQDq4lYkDM8Kr53RZA%2B6cKxUk9DFVaYoKwXOTcA00VxPVfZ0a90YG6a%2FP%2FOl33NRStw5y%2FpyjqsEEz76Nyjngf&X-Amz-Signature=3b146e9e0a597baef1029caa4f662ea283551428ad1b6a741ceea1b1801de279&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZI3FI7I%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA0%2BO4vJNcQjmgY1DrrB1ckzfr91awALwS7Kaycx6ozEAiEAqsvrA2jUkiID%2BMUEpsTBZeQMCyneHX3N9f%2FnYQHLO%2BgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJUeFHdST1zpxlKivCrcA8snUPkXtcSlSIDCPvDakeCDg1pVaEeZ3tHRuQldWH6DeBV7wljmLhy%2BoEwAyZtgJPnj2%2F9dc5xVRAYFyQT%2B6rG39xZ9jtrWyfIRxsyUz0hdeRdFL8lO1NmdH4ojFQ01DWZZ7Vh1yXi6w%2BD865w8DM681jAiwqDhcUYD9kzih9X6enhGlDHdv2E3wO04IH7UsKP5dZgSt%2FlkHyA6ZXKfrk702xx5HknNGAJecnRmzISpvpEiPTWB2kFCfMkEKBG3p9sFHsgvt617355osJN3SOHiuz1b8a6AHoTqywada5X4GUPdmsys1zI52ad3NPf1tw3NCibpvMo9%2Bb0%2BSEjPOGpUD7yv4jcba9Q2O3y56xP6JXQvtM9aSQ7eALxEeT2qspnoculSLu9IkuSjnxBJTQ%2F3NOdPqHckhHaU9CvLFgMPtXlJFfhv9P68lPv2t%2FUL2QskI4noeS8DfamaxiZiD7Xxa%2FFOJeDfCRkdRuROy2Yh1KQk8%2B9mWIKAzQwDuOqQnhLr8VUKi2Uioo0ZM2%2F%2FsMfKa3P%2B5q8awC3BKcYdiD4lp%2B1NqljEf0mD38Jy0ugXKxHXoFU0wJ8Xi2BN1TRmF6ryJiG56xxlyqNo87bMfXWQ%2FIJh83INbm8k39mLMIjC%2FbwGOqUBxTyNpikzZQkedfsgy%2FVNVW8PljSW%2FB%2BrUnIe%2B3Zo3eS7c6DQ7qqT7zaXyRuEGNDM4CW9SIFw8LTPvIC90TDQkLa6jl%2FdHw0A5J0zIJ5goawhWPuvXZQ6A8eRnyZ51iA7ADrIcWj1O3sIA%2FsKJOjMhEhaqmOEqMYSh23YTkYNUg9ki2KTYIBe2rokqn7mN%2BhmaUDYjmWkHptWcxM%2F%2FDuHpwiwSkBM&X-Amz-Signature=849bbfae3613625349b42bcc55f1ddb40b904907993f1eeb42d7781992e860ec&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HFBHBB2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhagMgKib3OGpN5jFZgA%2FD6oXyiCQRQSTBhHNby3xpMAIhAJzbpgKg008bj0bUwBdhw2G%2FKc92Ix59rdpdjhvDyBj4KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsAqGfrRHBXsSYr7Yq3ANgeYnpukA3Hcop71k1LgrZkF7wse7oQ8F9PzTaWGphNo9cicariQJY9Fq%2FaffZQ4GPsdS7DGrzFWqTfc8hkJ07hjOtaJCF08Y2JEU%2FVV%2Fui86G3fA7tmwJ9Kgb3qL8ro1MkfbVUGGo0qi5mgN9UyPnQVj7JvxRV0TCr9iKRRA%2B3AWMMIZ%2FzJAKlbSHK42vwUnOhzq4umMXNuQJKRCvRRu4V9gzuNGv0DYfzzy%2BNNRTeCuTTlezmr6FwMCgW6qvV4gLAmDAfYEFmOHNpi4syp1Hae86XimIlYGlTf9v7%2FtpJL1l52LkfVM2UVDuSFnW%2BQHdjM%2B89YfoYt9NIKxX4TjvCOx7cChYpO2dM1jgQYAnR3AZ5kQ78ChqXKMfetBYML10bD65Jpv5EeU1kDISNLQ%2BjYTJTCjbR9opm4CgKQJ7zpo%2BO61I0dSQxPdJgE6gcQN6tqrDMIB%2FsylmGcEjvHdxIncoXlLDjZBuUt7npvWd07INJnBda8YIYD3XCEktRbQa4wUbyUyR1Ucj3UHrnSv1sc%2FgfbJ97aRlX2gWUsZGu7lzvtefZHYRO%2BGQKaUJ4EvZMi9Jqrokw9F3beVFzv55mAPFpmRIrKqLMyzqLaY%2BCUkkZnMSwjZxGJFCtzCJwv28BjqkARkQxDK9V%2BLmVSFyeD5zdwOjNb2Gur4r4EmpzJj8oZweMuO5p5dHu6vn5CD6eUrhyDjWWGcXPuIaVp8L94XqvapJY1sr35HPItXOJmTy1qTOhn4WsbV0UA3d21PbhU4qZK0s9w4ON%2FWYki1gQGhPxxF3UdBdk4UJhzZpSWWlOoteb93rZbZstxlZFQTLdzuhL0NCOJdbg5FW7CAFY%2BFEid324QjN&X-Amz-Signature=e629a554704de1db3052944476abf2bfa8f2cda724c3135ae988f92a200cfb2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466345UHODU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwRYRDQgJSBVFDNkl%2B7g0sgBV1yNOqAlQNHI6Wl2p3iAIhAPO0vtGD9jY3K%2BxD1%2FxMSCwyUStQuHe2B%2F%2FQzP%2FrzO%2F8KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBErDd2GT%2B0RLM9i0q3ANT15MoX%2F4Wp3X1PNZjsNTCRaiV28otHmgE0VtjeQIDxUylfI5YTn3IoLD%2B5LZK%2BkUSzB5t58gdv2pQEQ8t91NUN6px91GlvKOuhS9Nye7k2SdA2KfDqJ5HiWH8XoFGnQsPBiuJJ9T8OWLmOdWJTwxcK6H63qbKq3v2V%2Bk%2FMdR2Al87cCKD5iplV2LC1ncrDl7yBfD7ScPz3m5sPvhybHrIasXwa1ENb3Pr3C3TUdCj70NXT0JB%2FbUANZyECh5Gui02LKr%2FA4Pm7f7YsU3iu287uo48Zzh25u84OSZjnas%2BRTPyU2LozWrKUhzRugE8Zr92rcqX0JF6QrMs7KI2h1WIVd4I1K6nIzXBCLtmHFE2mBS4zPyyC99%2F%2BhebjP3pUhnE0%2B9gze0os5mOJiQ1PYFLwJa%2B5gsxnx%2Bt1owyZqnjvWU9v8YmeGTomsZy9E8fL3FBPtr8%2FruPclA%2F6RUsxhkLVyAQF4sZqc6KIdKte5r9yyQRF9matbYp%2BRwaS53ImGinYJDDGVfMS2nSxoc2oEqndhfNpPljHeifpgce3f%2B22glJc%2BLYI0l0f82MuoEI9u18eVcvGBUiH9UR1Gyiq%2BqqgoN%2B%2B6k%2BSji6NbXonqsX7pwRf6j%2FGHHLJsYwyDCqwf28BjqkARFQZJqAJytG6rJhNWUKCzUWojodVomK905h%2FLb4o220bsDhfrKcuTof%2Ffc2B4ar2x2LWqPnq82ggDtAlNcrh229Syj%2B8fxFOfya2k03tyrljElizYyiaqSM%2BZfsz55jzlBCqD2%2B2kKaNv8ZEbE7XdOfGpQF8gcG2Pc4Xq1J6f0r9oYbtxo5OiBW%2FR76apBcL8MOcwjwzAbHm6FKopSaw53wwlo7&X-Amz-Signature=45372b17358fec0d6d93860043d13a6d80501301e4167a3cf79c6448edc429f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MERSEQZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqYVm7BrmVjtMlw5Ta2LdoAVpRfBwoAId2L1aW4iPskAiBX3yzvaVw%2B9u6Z0GwUBJxr38uShNPPwuFbHkrfjnpOtyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIManWU%2F387oEPKo5IvKtwD03oJum%2FgPCU5Khl5v4hg%2Fu77kGOWJWA8t54YPkb0q1mjKEL57%2BKQEsOmjSpZjXeesh7PBrEVSepprcH7fVZUth34hSUi9aYh3oxISDiqUZSb0Z9XZ9lPl4McM09Y%2F5j6iakUbY%2BzTYFYy%2Bsp1EjB2Y%2B5pliohNWFvNPhP4TAOJpTZfRhviienN05BYQ9SDFMSTwvbaWkyl1N1ukAWHKcdwK%2BXhVl6Kd3HYEis7zC4fczeGNxoDAG%2FapR8%2F4ve7X4SuXnradGJQQtrgXGgh7kEYY1YsnklV0fRiB7oLR%2F4npPWPO4Htnpy1WC2jih9tQNt%2FwvMm4oKJqn%2B25txG%2F6CjSrJTJnd4Cvw2vT9%2FVHtqcK7Ra0I%2BUQuQFA1Phsd3KDryYMNK3u2Vb%2F5Np4%2FlY1Im0c%2BtsSzGseqty9drJrI3E9RpxKBC0T6mP%2BbCjWNwQsPbHZYS1UzZOmw47KvE9cgNWM0SijMNGSyqZa5tndZ2Y6QDiYForYeJdmuEeeDH3xgBdDbKog21%2FUU2ZYYGcqSsyxEpYcnoffeyoYK%2F9wtZXFsSlkMNk3yz07QD1ZlJFPUy4qWqYDjMBAOUoBy9rG1UZsEjxGLQF5Sqpd7zR4n5NVBiMEWd5QbCWCbRkw5b%2F9vAY6pgGSYb6ga44HJkS3NI%2F1M5hHg3tgR%2BoKegaYb%2F8E%2BUEJ2IzJemKQLzekNi%2Bx5D2Bio4AZuRnzcluaeyCGdB9bpVXd5yUar2xpaNEj3is02C%2BioBuFEwCZJgAi0gmBbMFzvw686ZGAnUY9GM6P3DdTWT0dPEAltbl1coz7Va0JH0IKZgME0uQ5rjNazaluLk%2FSWFBLoZnUbtAb0HFy11Jje4RWeXUIZgH&X-Amz-Signature=df19ee615647667f8e1e0f0606dcd6c3ae4579e8b9ac97a993c3e1463bfea233&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YFKYNDH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEtoTn3FpM9GdcrXz7Pxtcr22zKbOHXQi0FQNMcLDVp0AiEAkN1dX7mB0lAFbvKgOG60%2FqAcJidrte2DsN9DqHrd4PUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFzAAE%2FqW%2FyXVjHHHircA7P9LHdkouXwuGHuSw8iN85vP5OvBscweaPJdmSZma2BIraZv9FtlkeKRAxPovZH9hwWY9tZ910YjJF%2FEVZ2zHgzsXxpga0aZso7cG3rEShnUj5NmuOsvmRepcLRr6kNLMnH8xdbF5oZVIWItqeTTh950SFeQUBMJ3lKcSWDvKboIjKqXfcdOuajrWyY1NQ%2FfMzoehavf1t3Rh1TdFliMqgDV9SFzmHDZXDE5h1Vos%2F7BKc0LXAs8pDkpqJxM%2Fk87H5GJyQABOlVrpj7PtQUkwt0sdrXApEI4OVqsQfYN8ac2YY%2FMnPEde0nOA9kcEGL0XCf5Z3v%2BRPTOaxxsYB2niZdNcJ3oevbhEp95TNCaJX5gw4i%2Bl6zDW6%2BqaYj8f%2FTxjgy6Gip23ou%2F0jnHrSt5bCQ0J9GOcTszZnLWY040Vm9FlGMtAM%2BTIth%2BTVRK1M%2FvA4DThRVdVm%2BABM1rDfiuL0ecww%2Bxgt%2F1PYTowlVrj0yAgJ1nWiF6EPtsTrH3k9aDRD8aUApi7cKTRPkXnzGYBBro9Qs%2FU3qcImq4O0UpH1FYfXjVsdtL1zreHRj13AeRHfO276OmSYVtptmcg9h%2FaGv16cOcpNbKKtLJBBQORgyljquv6vAHhroTPtFMKnB%2FbwGOqUBbRqfY265GtfpCdE4A%2BUnSuQ4bq3VmKeeqCXr4w6R3o73jIVW17hCtlOS28xggjZPqlALCSjJGDr1IU2V4%2F7vY9d4qgkAMHjCvDVv2PJzLhiM6FbAp5b1Oai85Dq6%2B4F41TzJSUonyyLnEIVLnWC9eBlda3s0pramttC1oquJ%2F80L%2BlVg0L%2FGu9h2NMK16irG4XerBM31qCHTBgeA5XRfm9X%2FJXAe&X-Amz-Signature=461f4a691a7cc11c1b5c2011008be4d9f7f610c1968d9ee777a26824dd6376f1&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMAHKHSE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHdA0TFQVu2hTVh14JTIOdaKGGRraJq%2FEzDVaR%2F00WpAIhALpDZ3IWWQckEfeeOkvaFYRFEbFxuY%2BMs9WPzhOfRJFRKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySQTdkLREAvMWLeGcq3AOFLlYNM2wlDm0qZ1UkbojMgOqQwdFbcMDC1LEeIhgYxn7ZNwPxRHFubAe4DMy0oeMKSdvu92KyTkKTirKfZOUjpKrDabo%2BhxRF1Lm92QUiPcHgF1XIcAdBMDQX1BMnv3Pl8aw0FBARiQnL1ZKkalTzieLtDGvheqfKgL25kAcBvLL0hjPKP7P5aNtFbbuCN2RQTAh9%2BtpbLXtHYOxgupFT0UflrSjxL59fSi%2F%2BDIgmL%2Fo3ohh8pMhMjzJ%2BCEVFMEXjxy0UFdQyNa0PW7iO%2B8sVQL1v6OAmW%2Fh5ba%2BoDPgJ03OZPexIu%2FojKbr2QvLVq6BkCABLdHdRwgCL0gejDD0IeeTRbZI4z8H%2B7Jlt7ZqTsKkVsk4E7iOoaUULcDSM1azjnpp29%2FFBiGD43sgHmWnyb3zMfW2onVza%2BTOlwbQu4sp0KC0smUlGqsQ0EM7EO3dbbMrZvgIHhg2r7xX5uk0ePx00q9E%2FSiGsuXUIvTBvKr8G44mXTJHQKvdQs34ThRPAoueLgwsIyyvELo0ojhSf78u6BJhYvheTT4tgYAXL8yyRVM8xIsWTh7Re1l0PyKljru8xPwkCRvSnaNsQdcgfNIAQBaEbIe9Qn8MkG7XI6oltUpIa7fpu32RH3zCjwv28BjqkAYIXMkEWgAHTdmMVzZAw7Ls0gINcYPSNUBEqsDj9gCYI6XcnHI4RjQd6KiPU2L5U8AK9kuq26sStK8wVBDi01pCnWuxtcgqOoxu2f4rCc%2FBe6ozmIUwOMnDa%2BxX0lTBawsZ5FNIEUfhJekjZSiU7hmSDQBxL7O0e%2FZ0G5CgkaBBBmtCS2SaLcqqk7i36QUcSpefQS3Whl8vbxufX2xJwZz4lPNaQ&X-Amz-Signature=1c8195c391e67d3451d04f57b9d21911b27461c801831fb48376a35eb8639130&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4MD2OTS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6yD9pU21GFhNhnwjxp2fJfBvrlfGD6%2FxuvUuPmNJNlwIgGmAbpGkrT5u4Xsr47%2FQms8mIo45y1TzCi6g2njaBwbgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBgXH%2FY1zeuqEgibVircAxjGYK0o1wwXaFhopW0%2B0rBe83cDMv9Jytb6Q1Be3acBuTbrRkfLoR0r795IxIlGXZMf8VULeqb6Nn82TANnJV3D3kzQHH4G8HC2q0yt7uLkEP5HT8V%2BGrKKYfwgKQPcQzlJmnMECvlYbxETU%2FkMj%2FsPCDdmYxdMnmoGMu7efPMiZqYppbdnMcNe0RLnD6vR4wMjAOBiU6BTIAZdg0J5pkGmJs%2FLHR%2FfE%2B9MBAO5QdHy0okSkY0f6t%2BP2f4Zo%2BtdGefFDP3q%2BmViieVug7UwMtJgj2VkJ8Xl3znv8qXen%2FWAEkX%2BYivrVVszhz3%2Fyh%2FLHiUJ1n4w6fdPZaiYofI7sCev4TwPKxhQTTQOHal%2Ff96UmuqWOZ81c1TNMvq4HCkYZ0GAGxDfFzfznspbdMRIiI6ulaUQBIP7HwSzyIYT2SY3TuO6hIHMnsDir3dWRBPAtM02y%2BfDU1FhuA%2FCkPGRiIWUBMPqXwsCXR87DoJT37psxkyX1X0JV91dchbjS0syGpcMOPuy5FMob7%2BQYTlHFaHNHQbZRUWikPq3SPF92sIBGtoQMZv2xpf74bI8qRqxXgdUBh3wDMWoc94wEgYpzzC73njOMcJ%2FSM3CtnaVu2Xrb79IHUuYqSPO5TpBMNjB%2FbwGOqUBalmK%2B231AFHkh2HUUNnaH87u5r7K74d7RBJBVrBj1PKIaT7N83dhdzYbYl8Vd%2FUdEsMHlQCBs9M4RZIoW%2BrLhfjBxXsBMTiI6k%2FwQmBAqJnM%2FeeLYwY293Yl76brprEkmcVXucaAP8fZtpdGbMIrJadlxqf0kYZjlV4RcED3wFHfO1f4ry%2FO%2BaNcWAhiygPp1HSKiEeyRj0cq763JM%2Fs8A0Se4cZ&X-Amz-Signature=e78972251489f4caa5add54fa051a7bf5075989eafced51c3d6b6625eb5ccefd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MERSEQZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqYVm7BrmVjtMlw5Ta2LdoAVpRfBwoAId2L1aW4iPskAiBX3yzvaVw%2B9u6Z0GwUBJxr38uShNPPwuFbHkrfjnpOtyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIManWU%2F387oEPKo5IvKtwD03oJum%2FgPCU5Khl5v4hg%2Fu77kGOWJWA8t54YPkb0q1mjKEL57%2BKQEsOmjSpZjXeesh7PBrEVSepprcH7fVZUth34hSUi9aYh3oxISDiqUZSb0Z9XZ9lPl4McM09Y%2F5j6iakUbY%2BzTYFYy%2Bsp1EjB2Y%2B5pliohNWFvNPhP4TAOJpTZfRhviienN05BYQ9SDFMSTwvbaWkyl1N1ukAWHKcdwK%2BXhVl6Kd3HYEis7zC4fczeGNxoDAG%2FapR8%2F4ve7X4SuXnradGJQQtrgXGgh7kEYY1YsnklV0fRiB7oLR%2F4npPWPO4Htnpy1WC2jih9tQNt%2FwvMm4oKJqn%2B25txG%2F6CjSrJTJnd4Cvw2vT9%2FVHtqcK7Ra0I%2BUQuQFA1Phsd3KDryYMNK3u2Vb%2F5Np4%2FlY1Im0c%2BtsSzGseqty9drJrI3E9RpxKBC0T6mP%2BbCjWNwQsPbHZYS1UzZOmw47KvE9cgNWM0SijMNGSyqZa5tndZ2Y6QDiYForYeJdmuEeeDH3xgBdDbKog21%2FUU2ZYYGcqSsyxEpYcnoffeyoYK%2F9wtZXFsSlkMNk3yz07QD1ZlJFPUy4qWqYDjMBAOUoBy9rG1UZsEjxGLQF5Sqpd7zR4n5NVBiMEWd5QbCWCbRkw5b%2F9vAY6pgGSYb6ga44HJkS3NI%2F1M5hHg3tgR%2BoKegaYb%2F8E%2BUEJ2IzJemKQLzekNi%2Bx5D2Bio4AZuRnzcluaeyCGdB9bpVXd5yUar2xpaNEj3is02C%2BioBuFEwCZJgAi0gmBbMFzvw686ZGAnUY9GM6P3DdTWT0dPEAltbl1coz7Va0JH0IKZgME0uQ5rjNazaluLk%2FSWFBLoZnUbtAb0HFy11Jje4RWeXUIZgH&X-Amz-Signature=56374e34845711eaad11efa995ce50cd5f23bb94f38b005dbd030873c8463574&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C2TQ4LI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHe9yoR33nnyG2Ahh%2BvBFoXyihma90EMHSowqcaM8JIBAiEAu8gtfIUWZ4sLSjPpjt%2F8DjHH0kLXtp7p%2BUgJP2G2C9sqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFe4FGw0evWyhsk5DircAyW%2BVYE8hJxphNFqmNmXP3%2Blf2OC%2FA0p%2Fh5VdlFPK%2BTkcQzqXZZxuLFtQl6XwEGE7UuL8Sr7uCiACK5jLkBalHoWBSQCMC%2B6hKi%2F1RZYzZM0Qblcj0pDMX9T7x7z%2BUm7ElR9%2BXl6sCBvkcBeXK%2FdyafyvRYzoiceXKZO%2BjgTinlp3WM5VyEohVkXA%2B7vGM%2BN1bTDb0wCZSjRitphQpY6sgNtBQSbmyTcwVdPBE78Xx2n5MaUV3kj5m1ta4n9p1JHIHhMlDn0c6u9RbF%2BfXugcdg%2FeDY3hCgoI%2Bt8yZxETX900PaCsMIRm13CwNtPP%2BZ2N6UM5i3Gmg6QumXzEPFZhtx2YKRtZjPxaVpTDjQ8V%2FSqPJiaHYyVShmx5yAEqK%2FVXldnHrWXuVBtE0C9EsN7ehcqAAZc234R%2FZLGX4OOtUM6ALh5aBHDz1XSI3vSU%2FxG7uV51mEBwNVbFhKhlxf3QF3DcW82REDhqRY9un6ZPhOnu9kBGZ3OEO845XjOM9hWbePOQq697lcABYH4j5hcqtHGH6TIj1CRsz%2BVK%2BWEJ5MkoVmBrsvfRwIsbKe7JRcNDiO1C9fARsYCaHf6XqIZMlTeqA0b0%2BX%2FfHbnpfuEaAUSola%2Bu6DuLNa1SmzhMOe8%2FbwGOqUBO1bY%2BZrjnEnKPnxTkgQLTTOxT%2F46A19KmXKYS6Udbfa2s7VM%2FpSx%2FfwPLyU1sUuK1RN9Ng%2BKtsY7pEXBJ%2FlejBZ0JK8w4CzTMQVaNQfZYMhN7i5QKYRymC260q4dEnVxQO3bRZ2JclZiufjcTQWyylInsU83p%2FhcZhQxh3p%2BtH0Y4YAG1vJqcUcTgKT1F1O2%2Bcgr9o%2BHQvxO7E1ZYKWN%2Bncvbt9K&X-Amz-Signature=37b1ab193ef3e9aacdb4a8732e7d773e5812f83e70d9964a975937a11ed4d433&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C2TQ4LI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHe9yoR33nnyG2Ahh%2BvBFoXyihma90EMHSowqcaM8JIBAiEAu8gtfIUWZ4sLSjPpjt%2F8DjHH0kLXtp7p%2BUgJP2G2C9sqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFe4FGw0evWyhsk5DircAyW%2BVYE8hJxphNFqmNmXP3%2Blf2OC%2FA0p%2Fh5VdlFPK%2BTkcQzqXZZxuLFtQl6XwEGE7UuL8Sr7uCiACK5jLkBalHoWBSQCMC%2B6hKi%2F1RZYzZM0Qblcj0pDMX9T7x7z%2BUm7ElR9%2BXl6sCBvkcBeXK%2FdyafyvRYzoiceXKZO%2BjgTinlp3WM5VyEohVkXA%2B7vGM%2BN1bTDb0wCZSjRitphQpY6sgNtBQSbmyTcwVdPBE78Xx2n5MaUV3kj5m1ta4n9p1JHIHhMlDn0c6u9RbF%2BfXugcdg%2FeDY3hCgoI%2Bt8yZxETX900PaCsMIRm13CwNtPP%2BZ2N6UM5i3Gmg6QumXzEPFZhtx2YKRtZjPxaVpTDjQ8V%2FSqPJiaHYyVShmx5yAEqK%2FVXldnHrWXuVBtE0C9EsN7ehcqAAZc234R%2FZLGX4OOtUM6ALh5aBHDz1XSI3vSU%2FxG7uV51mEBwNVbFhKhlxf3QF3DcW82REDhqRY9un6ZPhOnu9kBGZ3OEO845XjOM9hWbePOQq697lcABYH4j5hcqtHGH6TIj1CRsz%2BVK%2BWEJ5MkoVmBrsvfRwIsbKe7JRcNDiO1C9fARsYCaHf6XqIZMlTeqA0b0%2BX%2FfHbnpfuEaAUSola%2Bu6DuLNa1SmzhMOe8%2FbwGOqUBO1bY%2BZrjnEnKPnxTkgQLTTOxT%2F46A19KmXKYS6Udbfa2s7VM%2FpSx%2FfwPLyU1sUuK1RN9Ng%2BKtsY7pEXBJ%2FlejBZ0JK8w4CzTMQVaNQfZYMhN7i5QKYRymC260q4dEnVxQO3bRZ2JclZiufjcTQWyylInsU83p%2FhcZhQxh3p%2BtH0Y4YAG1vJqcUcTgKT1F1O2%2Bcgr9o%2BHQvxO7E1ZYKWN%2Bncvbt9K&X-Amz-Signature=488f151c5c863bf3c95113a2351808df69605f773fcccf6a322e5f2747455717&X-Amz-SignedHeaders=host&x-id=GetObject)
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