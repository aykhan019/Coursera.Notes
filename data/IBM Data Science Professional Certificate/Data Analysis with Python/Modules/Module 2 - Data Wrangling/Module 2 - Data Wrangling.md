

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6XY5KNK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCICxs0KnrB2E6Wq4Ju71yvpT4Cy1YMlLcIViTO0VJb8nWAiEA9jQywAU3okWML%2FmkLuLGqUGxmPGqkJMccQDyBbfqEqwq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBFn9CdbWWJZWfxc1yrcA7w38iQ7Ztf0LkOeG1VUFFEdYWJQ3ACVjcZzN8d67squkIRwoKnvhPtoqxPGKDfp5EX%2FQ9nGoz3Fj3ohEv7QecQ5Wq1BZV1sPsF2EySJ2GVu4obdYXSJrnX5JdDuo17rMF%2FoH2u0opfNLoICGivOz%2FbGEwA%2FLfypxn6lvDmG5GmXmJdq8FAcmQpxXna%2Fo0eLvczgcMrl%2B9vOUSSYCpbvsEqK1EorYIB1WbyosZCowl5iJ2ulMgVRCHJll1JXZlUWvKph0xWbgo0odFCJJ3%2FRIVOsl4AEYv5TdU6mVR8LSW1iD0l%2BsQfuWrFxv7zPD2U1%2Fpm2IILhKYteXtX6fLhV4DkkfFk5q5Y%2B%2FSN8Uh%2BFNcc21enbLzjv%2FzQZ0JzN4X6j0%2B4EJqVpqLgCQ0JFHyEU1L85SumtrXIT22ohfX3vEqtA3oAqI2TNnmsPRspg71CzorPgiF3LBjUsjfimplIgFK44wkhuaVVJJUW1XN8swijoJxTz%2FOuhEH2hmUPN2yqSDi2JVHs1X36JObcpu7IpPLbaCSwkKgooYRpugPk6j%2Fd%2BVCB9297d0YYvOiN6V%2Bc6apUIPWTq3Qprps3%2FW3IsFCZX5A1Le2x7sebfNczliwgbgBIFtXfT7k85lHeVMI2ihr0GOqUB4hIEKhFlOUTLqymX2Zkxpc7kZh2o972zZ8DWu%2FnMpG6oIZsGiK%2B3fD0u6pF8IgEqEt23ESsmoj2%2Fvc8kTubCrTG1GYO0fNSTD260k6vjxtcr5hsVJ2Ndg5t4sj%2BuBrRU0psZxiI5gt9fpD0xdw3GfTysPM9%2FFDiGpeclDQc4w%2FJ%2FTVtQZYTQMVQignYJzyBLM1Eoxvjii7rv0XDEWv8BgHtj57%2BS&X-Amz-Signature=36e10f18cedc78831894c9384d195cc3c8ef50bb204b7518bc05b03da9cf6d2c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKVIS7U4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIDvGM%2FmsJTXEnA5uQ8ZuMW1e8pyIIScC%2BDA8kbU2NBW1AiEAqPYCrYqdyH3p%2B1Xj5JQREdouIvOcZNOuvQw%2FTu2xF6sq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDKdWVKyozwLoQT0qYyrcA26blzptbLSm6an8RjFW9wPL4bpn1y6%2Btrtghnmupx8zLKxEF4YlTULKf8N5pgzYvVvV9HkP1jlYFbCrQFQ8lwp5otooVT7lS7ngyE15wJoz3Sb%2FYYpBxp8PSC0U2yiQLqAlPede1QgSxoKZNX7qrYxrPQLRZ1uFhxLEFrnmHTaI%2Fr554glrBsRxOm5jPrX%2FETGZOw%2B0btHTmniHjOkrpA2yWtLqGme2lUvh0fqZATzwk4HEKv5f6Gv%2FsBoKCMYF%2FpXuRHUxrqwb0kpQu0RJ2KlrtISrzTfFsL8hpluZ3FnqrIveNc5nQGhHIWNXjcuwbhng6Vspw1ghEsma7TlgJM3di53lgNQgIILfBXkNYQu6kiQfPl747N6xev4EvPJo6CmiBGNoIg%2FNF4uU7mLTvfVAQJMtdpaK%2FuHnEqsLL9UvGnJ6FRIx1tPto2vEIa39qDb%2Fl3D0RQhG1dI7ddZjSiw5Tc99eqO0G0Qjz8gGIFao3G05Z1XpkkFggsv42ob95J2jskZJ37xj%2B%2BpK87QbZ88oliz6yfQdV4bOP1h6U1BaGHtxEY9ixu7pFd0Gu5cbwmhtSRMVXtBb7cWksKJgd7tIh%2BBgSO%2B%2FKNknu1XAnLgZzX%2BBArnpiZ48h%2BJHMNqhhr0GOqUB9TbE6%2FgQF1RjS6r2hqfTfiVYhFgkXDpJempefgFqdVTD0TAsJ%2FlqS6MYt%2B2mDWfLe6zqpY7%2FPhCCZwYfozEEJCVyTFvOZPywCfMwHTC0BLg1apAVEEIMizIlV61T5kMixYd9EZ94m6rd6oiZa4JU9ymL7oK91RjWbnvfx7QZWUUeX6fIT85tQVjj3%2BqxFX6u1h27UcP9mnDQlpOAv6xh3XO0EP2p&X-Amz-Signature=61dda9f86c3705892a335de563e5b9c6082d23e8a4d619696730e29ba091ec19&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644WIH4MW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQDG8aR6%2FgxJrcQgue0PgADX23m4vfap1gO192TnZ6UfPgIhAJVp6Jlrc05L%2FcjuGBxiTz0P6tsR32ocUgxJnbDJeO2zKv8DCCUQABoMNjM3NDIzMTgzODA1Igx8s0iFc4psWt%2F3%2FTUq3AOdyLc7F5v3Xp3VWtY7rmznq3VE5hwesHomHFXidd1rlAR3FTmJCSv2su%2BMxmFvASB5uCV6bNn4lhE3Ls1rrLhUAKfwZKF1CNb8jAKYTbjeIJ9xLg%2BUeDOLQRsBNfqNShkXsI6YEKJj62FSTNfEBH44mpLb2oO03%2B0jWRpdKw5R%2Bm6EURMsBreX0dkc%2F5GTKjbhbBcLgnw8NNrhtbP%2FrhaXrK70g%2FlxiGWpamvSb1g8F4Uda1jGwKhTj5%2Bv%2Bhb75vk6yhZ5lJxmtkpK7Q23BTLNUvMa9wKHO1taBTzqKc9bmsmXI482XSBtuXoKcpNz7mdna5pO2flDDoCv5UlbmIKGIKS%2BYbQZIZj3yg%2Fqk50GODE7FvY9QA3Uif94YAzMlJWzeHgjHIMjAk4K3thFj31ZswskOS2qlZjTFOPMx1%2BpDwpXmQkNTWx5MzA0EH%2FTXkVsSgX%2F56KPJaABOO0m6S9sAxanHdk6BlAgJkCP9J1vIV6GnbVXXbyevU3BvmO0C3I24xOnQIh16Ye1C4wOlVLoW%2BaPCG50XkMJ81DiygmHzfW34RKSjFPipjskZ9EWL%2FYuwYLySfcSJP79mkublvFsM7p5ys3sFn%2F2wOPOA3vWhzIcmKdV4p%2Fsj%2Bb7xDD2oYa9BjqkAX59PdRWY9tknQOpqTSpYtoEsr67SUQg9oXDd9KRL9D9M6YeESRFitQwuqsowkmirislF37bEz5PTMiqAtinWe6Cy%2F27QB5wWQN%2FxqYQfKpyqmUq3tDC2ppw10MbmAc8Hd0vqA9XvLcGc2XDOQJ8eE3XUE%2BRb7ADckk5xQ%2BiGuz4ClXBJpkG%2B8%2BZ1IogH5ODdIXBf3KnivgzvSUBjggfXIFOSbP7&X-Amz-Signature=6f2f17c6840272e1b5092808224dad021e3112c72f86b77f4972e4222c2975bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X64IQDLK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDlOWVRO%2Bnra9Y5xhCNMeFMBKgbJowrl784mQqOr2HrkAIgXOwZ62EgTz%2FKex5OOFEZDMFZPg3X7ARhGIQQ6BLgWtUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDCBIi7PbotoOpTmJsSrcAzn4xQGzVaUkk7Wb3hNOYFO355eUR%2FjnIM49J0aCzpEcxzDB5JTb5RsG56ecL20I6R1%2FZ71fi%2FYEwAgT47yIX9N0%2BkOahSM0jmBa19upwWBGSSU%2ByXbrC4a2bBesBvc4JaQzLEVQqZn8ceOuYsTY%2B7%2FtqkYEOlp7QZb47b4tRLB%2BEQStClbT4Gx2hQhoG1Z3ZZKPNZkrGqY8BMmXrJt%2FjEbYv1z0jdyjftR%2B7qM9Zl2q67Pc0Ok2yeiLfrFqPMcvthWPaSI0dZQMRzmvvwKB4iLd7Ngc7POTZAOCjexYQXiKv58Tt18mHo1E8s5F5ela7zmk3pgI75zKaZUB3t6VPCdypId90S1AdTZuNsXOjINgb27ssmerqBVAxwtKIVbyVwe0OjnXFBx%2FyQvqb3HGi551GZ0maAcsyDp%2Br90S0pnvIySCAk%2Bh4h6q5PufqaEn%2B0dWX1xpnuEVlWGhmz7hPzwyn8HnFa0Eddje0xg1CAMNNoei8OB%2B%2BN7Wa4yV1diaazp3TUN3nIx1J2qTWva9Dsovem6qj8%2BkhUay3DGh2ugvfRqIq%2BhT17xixaJYnhqQTRu9lkQd6p31Gow2%2B9MxT5ieIfyM8ERD2Sy%2FLeMcw0noZOBYYJsGk0QZdQvNMMmhhr0GOqUB8KDLSCFtCpMJaBYidV1oOPlAyEnLYujGh0eC0WBpYq3nddf%2BkQH2MFsVX3mkkF%2FDGtrz2x%2F57%2FsIohce3FWLti0loBFYlN1KEM7fZozk778FIjvs%2BCPyFrAjZAQsvbqKbysmK4fiP%2F766khYcSd9ElHxET%2F7eMGLTNiMpyvMlnCvrTlZMeu3ffdyzdh4pI%2FMkAShCBNz8gQmfheUIN6h2ulq2NX2&X-Amz-Signature=dac2ae0d10b7eaf7d8b89e980c81d45a94a210a4d9059a5499994ff5d882050e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2K7EOJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIHr3gbPedssstGQcvR5iUyo0uvTTp7puBNnCZuIoDAy0AiBaoxMaz6lXdmKsyFDe7uWo5rSxKdHSHLp4p84MgJc%2BjSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMoDNijLN%2FToS7HAefKtwDJxTHy2TkUV1xbfte5Jbq5RTZCEhkN72lkWnnFlSXtLOAO%2BEXTMeJqfFF0o3me9%2BttgdQJV0LoMLkmNeNdpZFbukgyo8itBpzSibX53qkbzfYH2eR9DtaP2MNFzEXTdZiSyX7RT6y%2FvKOcDMDDOLc%2FfNR4157pg8hHDzG3BOBgoMcmr7Oi4GR8xYTIUtAtCQv7uC4%2F8sd2hT%2FzDrYO70t2JSVYgBLLk8kDWjChKUdS82hgGgQiF9e3eQ4lHK549wenONO59fcHJazj9WRkSMbvcNk%2FiDAh4py1a2qlc906wTE7%2FCMkVEmfLKS27YD5BWihWezt59e%2F9VQUW%2FQDP7B4HFTbk4QlaAPbfYg8KrrU55m7juusRP7OwEyyKsSSzVMxRenKMK5bjakGlmBup8YXK6dweWDQD6NMj33m7LOmX7j%2BK%2BwEQPUHU7GDGjpH7nIEVlSdT9jlvtTQdOKOkxf7sokFwkC69mL%2BMZFeAXUBc3VN%2F9Om6XoQgGhCDsAX0BazZICfPKVR02qdfTV%2BVKsQRHPJxX3eM%2B%2Fkodj9XOWTmFAVDtz2MWleb48QWndhVJtn2JNjPTgWW4bstPUePJKW62WD2ZeXsz%2B%2FNKBXiMjGiT%2FcpeYluhA0gSmavMwnKKGvQY6pgGKOm02cRnmj0Pt8dTCMc%2F%2FIOtu3fNECkQ3w6XhJbOPDpH8KKk%2FJdObvLjXq4Df%2FoSeQEiUGBcwn%2BhLaVT3xrIWnQRDl9EdvzBD3stIhLHqSexjULTb%2F0165XPHe2STKtfo1ZqkJ8Otkqi8w%2FnsWHESEjJ9pLzm%2FvMRrm5H2OqWtNMwZzVTJmWm6m%2Bwy0ib72RQrkNIqLy5s53OcGz7oBxWKP7TbkTA&X-Amz-Signature=8ffc6944c19ce6fc643be6d52d8c6eefd1b5a292fab872b5f29d9937823bdc09&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED5G5G%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCvaL0FdKS2UhsDpwCpX3LQkNpFqInWO0BK6BnTdPWJ3wIgfAGw11OOMfdtSMPB9GdkP4%2BbiVBhIz%2BJ4diRmhYEWDgq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ0MCoYt6yUQf6vLgCrcA%2FYW1nVbodmM2qyRX46uwhKHhFOJ2e0CeKf0Yqoh5SdcOVELWXI2J0FfmNHX4kxAKFCQYtRObf88VNpkHopdnenNwJpX6rTk9Ka9Djiyqx%2FiEajejQCye4Xn0nOCn9CKnPOsxXapS5EZKN6zh8RjIE%2FbRi2PXiWJhKuEgwumkUJ4zpYfIibnvKpaMB6OU0Q6qjdRI3X88JYgOELENXb36stQ5L3T9H6Nyva5DbdCJrUB4hnT4WTt0KK3ZA2bvdkPzqrWig5SSmkOa4lLP%2FRiBm0nFqRr21L7q1Fk2F%2BZX4q7C9qMt3PEHFInuNT9qt7rnXDqxj2m8L4mauUnR51LL%2BRUxzL3H3TX64An80kjJ%2F4PzY72PfszDCEHAfnDAdB8O%2B30OouuCZoyX4F%2BcwsKFH1k4cYkNo8908odc2NcLO8UWNYORQNq6o65sGDXjK%2Frk9PRb3KjcXwRYRvKOIPyS0MmMOE1RT%2Bm9QRRhw1EzKxuPB4Svw922BpCeORiUKpK1q0VYK43SBznPf4Pg5S7riO5cyzGUdy8gvC%2BEBDv655ZVEoMuCIBL4jRimnUg9RN6QeU0MrtJUEqtNaFRhgMDpFdhsCowLiPsc6LkvB9R7ukxHUQqSi8Iy66%2BqLEML%2Bhhr0GOqUBczF6OCO3AegJcP2rKHXORa%2FxVNtPL0qJ%2Fpovf%2FUz7EhpRmuW5dyraewl%2FUa5%2BKXrpE8vR%2Fw0XxMAYPpGXk8dkORzHPb6vexOyR7vwhEOsvWkOOwDH5oSwwz9i2WK3VSQ9I6n2QiK8A2Cl6yx0ZJRqx8eEandVYWukMtHIgBzhzKeOG7h0OhlrXMmyCrkyXap05io7gjiDFwuIgWUzqF4S%2Bz90Oso&X-Amz-Signature=c211c5331626ea61727331656882ef8dd9e6ee2e0f63752a1856c6b3d6d53013&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4NQOBGU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIAZTicJ82hJfO0ByOyAN2aO3uIxZ3ucmjVU66P%2FsuhLRAiEAmBuHrcjz8Z72aPAi8ntns82lAZA6ZzvRzN3CZ66tFFcq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDGvLxiL%2BBaftko%2FmhSrcA8G7a0ltgWkrAuVWp55LWjA7Nm3N5TrvNwrA5Tgvz4cLYd%2FlRn%2B9JfDoj74XS7IH9McH3c3NTIyHijmxgRBHtUW71M5vdK4EiduAot4cDBybXyO7%2FE88MDhJONoVkD8Pym1vj%2FgQfWiZ6mjfGmd1OYXXB0aPDreDhbIkwiB7Z%2ByUSkxenuvNE41qbMMlKQtW10Kpm12%2Bt%2BTGvjqypR8FOWWgJqWxQa7e39wH%2FDcx%2FqB%2FE2aDut0%2BmrErMT4S4rUpQ5VZDRn6lRLcETiJfm8cQ6IIfsYSQlAbA%2B4V1nwRqv7nnYvA%2BMbAnd%2FXEcdyGV5n%2BiEQ20%2FuEPry9nrB3dFTaIwEzGiBuh0ThnSRjBT9YNNhrP0KlpCoWQUB7PiPXxN3l498u1EwoTwqSSnWhLmm%2BtS3pFPEXynP3wGjH6J%2B3igNOpTUuH9zMuiO5rT%2Fs4Cy82suO%2BLnlKH9pdOktEA2S31IDYrzfqF4Ur%2BlfOuz2b59Ts9wpK1UiVySVO27777JwYE%2FVF%2FGsP3D7KD1gUPBOakvukiODj631h%2BBpr7O3hhZV%2BhTxQnrXnlOqQiOAOlVRCeGlrMLT8YwTyykrxHpOiVtNMhbjjpuHQTI%2Bf9FdNC%2FePbCUf%2F%2BlPR%2BDKSjML2hhr0GOqUBkLbVS8I0MOtpY3U%2Fyy39RX6gd8b%2FKZn3dZVgI2pqeNg9CCLkPWG68s8%2F%2BKl%2BcD%2B25GeEYCtlO4FrJWQgzvkHhhqjHSrE1LU8AkuZULRGYS3OdfFNF956dgQbswfravynX%2B4XOJSrPdPt4QkK8c6DmIrbXhvQq8o4nZ91q%2F9TfyGHlXcK8j%2FJr9JEwmLsrZqKGsdr1DERBUGlgObi6VrUiQQ7%2FeIU&X-Amz-Signature=188bb2818016341b37d7439383e88ea797a393ed699909804c7df80912d9a57e&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG3NJOAV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIGhhVRwHI47ZWseOcLWwjY2Upau6TrDJviE6fm%2BbCZgmAiEAmhveb6MH%2FXIZQHr%2Bi4Z%2FTbClltyeF%2BzGBceE1PlCNc0q%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDFeuKROuHRgeVfyLPyrcA27wALJLU5HAICAF5fhxLohQmU6bOFo%2BuodbnMtj2KtTY299UDteLw22sROk5x6FolJW5Yz4FxI7YIy9C54dGfkD1IH2ERar70Yi%2Fi6X%2Fjb6rstFUa1mZtGABWJE2QEdGzpxLXcvwdXnFNLYfmg6lgQEq%2Bxoh5kNSoB0rBEinhaQkPzCg50o86YkRLTm%2F8MxLcxoA9HzZHS9YWSY%2Bo12wAscBohogECunFoMb3jsSiuzk6tZaQ7Yo7yVIWM4lEIyXtnhMjz40MB1%2FpDdV%2FB2r7%2BuwW8btNBU24vht2mQ0fByujaxz6mkfanCBoTqW%2BlaKJ%2FcbdqVs2KKAttvJBfhMLxYWqp5OM3sEjMeYCsT%2BqSc1QvN3%2FDL%2FzWCotOqCc1FfpokpnHtEfmSpQkzLdfY67IECBJmHfC%2Bg0wf0ybJvHMe9KBDSKN3ZS1ntlULEUM%2FwpUK9OkKAtrMJfm5zSMVQbmyBU8z5KyTH6z9i%2Bv9i14y9NScSosCu8qHy1OMbuqMzWn2kZRMW3bxXYnH1MSDKEOONds4k8y79rSCm%2BufbRbijtZLazqmDTdMggCa2QvOaobeICQweqowuulxCgidkMhqff%2FFJ5AkGvX2Nd6JKRKkLpRB4iExA3UKbBxbMOyhhr0GOqUBry3LV2%2B6Z21RVJec5aTBwtiRwtsK%2FDinow9D3SUCSmlBWJWLtpDlp3JR51hDtKyRejlMXE7RAkeUghSR%2Bs4a28QVrJvdcGZn%2BniGDYv0XSzzja2AsSnmE%2BeVVc4FFrT5uTZFGqkRvNqTLI5PYfDT0F0o68nQ8EfuBscOJ8GBKW%2F6SeTA3e15vE4o9rNUv9sB8KHUt5iv5kZJB80MT2nxtr6LLiRI&X-Amz-Signature=77149715d265605a4ad58d438c075c91446393e933df76334d83629a90a5d939&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2K7EOJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIHr3gbPedssstGQcvR5iUyo0uvTTp7puBNnCZuIoDAy0AiBaoxMaz6lXdmKsyFDe7uWo5rSxKdHSHLp4p84MgJc%2BjSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMoDNijLN%2FToS7HAefKtwDJxTHy2TkUV1xbfte5Jbq5RTZCEhkN72lkWnnFlSXtLOAO%2BEXTMeJqfFF0o3me9%2BttgdQJV0LoMLkmNeNdpZFbukgyo8itBpzSibX53qkbzfYH2eR9DtaP2MNFzEXTdZiSyX7RT6y%2FvKOcDMDDOLc%2FfNR4157pg8hHDzG3BOBgoMcmr7Oi4GR8xYTIUtAtCQv7uC4%2F8sd2hT%2FzDrYO70t2JSVYgBLLk8kDWjChKUdS82hgGgQiF9e3eQ4lHK549wenONO59fcHJazj9WRkSMbvcNk%2FiDAh4py1a2qlc906wTE7%2FCMkVEmfLKS27YD5BWihWezt59e%2F9VQUW%2FQDP7B4HFTbk4QlaAPbfYg8KrrU55m7juusRP7OwEyyKsSSzVMxRenKMK5bjakGlmBup8YXK6dweWDQD6NMj33m7LOmX7j%2BK%2BwEQPUHU7GDGjpH7nIEVlSdT9jlvtTQdOKOkxf7sokFwkC69mL%2BMZFeAXUBc3VN%2F9Om6XoQgGhCDsAX0BazZICfPKVR02qdfTV%2BVKsQRHPJxX3eM%2B%2Fkodj9XOWTmFAVDtz2MWleb48QWndhVJtn2JNjPTgWW4bstPUePJKW62WD2ZeXsz%2B%2FNKBXiMjGiT%2FcpeYluhA0gSmavMwnKKGvQY6pgGKOm02cRnmj0Pt8dTCMc%2F%2FIOtu3fNECkQ3w6XhJbOPDpH8KKk%2FJdObvLjXq4Df%2FoSeQEiUGBcwn%2BhLaVT3xrIWnQRDl9EdvzBD3stIhLHqSexjULTb%2F0165XPHe2STKtfo1ZqkJ8Otkqi8w%2FnsWHESEjJ9pLzm%2FvMRrm5H2OqWtNMwZzVTJmWm6m%2Bwy0ib72RQrkNIqLy5s53OcGz7oBxWKP7TbkTA&X-Amz-Signature=62ee9989ea10edfae8ec6f0c942d15e83a3919259d04d14e1c712cf1406d06ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DMTNUI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDvialusPqv1nP55t7Ixz0rRCg7%2BHXP0wO%2Bf0esu3VMhgIgVaUAYWu9iYXj2uab80ZL%2F3qydU%2BC%2B%2BnJZbL9tZTWGegq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDG%2BRQWqMYRbx7GISjyrcAwqz%2BX%2B7qOLnIg%2Fn%2BvViNx47Nd5pNXLDEcSTh1aCit33ah4GEy0SuAwYRpWZA41MHti7fy%2BlQgwKyGV%2FT8vC%2FGY3KBiTR5W0UFavCt6kkXw1H3p2bt4FU%2FyUtzAmSOT8Yz3MPxo%2BKai%2BYfmH0e22CWNgPvfBB44N%2Fu4dHsnKjiHT3Yhld%2FcL19oUdN3AHoTOc8nJML2Quy37Sn0B196X%2FTC%2BIDQsyH%2Bm3E5oIjjc73CietqkBQf4D8MvFMngL5UQ%2FYgnNKtZK5J%2BEnxMiRPaxHYYCAo2QdDyuaRvEfz%2FxjMmJGjase84LJDvEqhyYyUlnW8yOuaefrPdIHTJy7gvqGh8%2FcSffw2FTapfhsrlCGmvQyiIKz%2BnJfeTuDi6ZpZo%2FFdZxSzrWffWvP8SNzW1E69Gv9L7CZv22SnnQCVKVeCNZ45Q9RmG1ApHatAeblQi%2Fzx48UVpoFAlPUEqDwH8maDyoVefZEipdntmgRZ1SL3GIWMSRttUkv5Dm%2BAsaxt%2FIzlOyLB4RjXHUNWBPkPEIIIqiiCoa7mg6uqz6gNdJAg%2F3QjI%2Bg9r%2B%2BYb3FLoIiow2NBG%2FSu85i9ugsgqWOULOoQpA6374O%2BxORVMg0RfxeE1PMqIvphxbtJ5VFkGMMmhhr0GOqUBJD9i5N6QY5SGRzPweGvGhHZ5dii1jWBDx0Z3fNUoPPhuJNrtCXuAlDiK4HVE7ineNCpabDFfMkjG5izb1fkR3%2BtcJ24gh3AA%2BUVbR2RuBoZjX%2FZK6PZbLWL0yhpGMfuW0f1z7PNZTN7Yfc8dxIS54jbJxt4KuaLx1%2FjEjp7vqDzDUWzVVi33DriFqUN2HJKO2anNpfZRKOD1C6R2wpKeP6Bj6AHo&X-Amz-Signature=03e919691fcb79cd6ff2e48360fffc0be9664690a7201b185abb7c84e5c39fd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DMTNUI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDvialusPqv1nP55t7Ixz0rRCg7%2BHXP0wO%2Bf0esu3VMhgIgVaUAYWu9iYXj2uab80ZL%2F3qydU%2BC%2B%2BnJZbL9tZTWGegq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDG%2BRQWqMYRbx7GISjyrcAwqz%2BX%2B7qOLnIg%2Fn%2BvViNx47Nd5pNXLDEcSTh1aCit33ah4GEy0SuAwYRpWZA41MHti7fy%2BlQgwKyGV%2FT8vC%2FGY3KBiTR5W0UFavCt6kkXw1H3p2bt4FU%2FyUtzAmSOT8Yz3MPxo%2BKai%2BYfmH0e22CWNgPvfBB44N%2Fu4dHsnKjiHT3Yhld%2FcL19oUdN3AHoTOc8nJML2Quy37Sn0B196X%2FTC%2BIDQsyH%2Bm3E5oIjjc73CietqkBQf4D8MvFMngL5UQ%2FYgnNKtZK5J%2BEnxMiRPaxHYYCAo2QdDyuaRvEfz%2FxjMmJGjase84LJDvEqhyYyUlnW8yOuaefrPdIHTJy7gvqGh8%2FcSffw2FTapfhsrlCGmvQyiIKz%2BnJfeTuDi6ZpZo%2FFdZxSzrWffWvP8SNzW1E69Gv9L7CZv22SnnQCVKVeCNZ45Q9RmG1ApHatAeblQi%2Fzx48UVpoFAlPUEqDwH8maDyoVefZEipdntmgRZ1SL3GIWMSRttUkv5Dm%2BAsaxt%2FIzlOyLB4RjXHUNWBPkPEIIIqiiCoa7mg6uqz6gNdJAg%2F3QjI%2Bg9r%2B%2BYb3FLoIiow2NBG%2FSu85i9ugsgqWOULOoQpA6374O%2BxORVMg0RfxeE1PMqIvphxbtJ5VFkGMMmhhr0GOqUBJD9i5N6QY5SGRzPweGvGhHZ5dii1jWBDx0Z3fNUoPPhuJNrtCXuAlDiK4HVE7ineNCpabDFfMkjG5izb1fkR3%2BtcJ24gh3AA%2BUVbR2RuBoZjX%2FZK6PZbLWL0yhpGMfuW0f1z7PNZTN7Yfc8dxIS54jbJxt4KuaLx1%2FjEjp7vqDzDUWzVVi33DriFqUN2HJKO2anNpfZRKOD1C6R2wpKeP6Bj6AHo&X-Amz-Signature=343055ed668b60814acc328d52f058464ba37f7392ae17ce241f8601289fc521&X-Amz-SignedHeaders=host&x-id=GetObject)
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