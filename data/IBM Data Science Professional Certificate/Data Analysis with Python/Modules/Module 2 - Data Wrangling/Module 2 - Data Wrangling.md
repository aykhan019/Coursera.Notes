

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWHWMMLY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDdNT2rmuv5TW6JgRTdCaN9JpPB8Q12ZTE7vhqRTzWvMAiADQ966rlxneVhhr8vs97boO4zVOWIqIU8lhR%2BtAn7MLir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM2syggDuI5xKc7SgSKtwDvoPwxMUpW37gI1LsVYfnUNqU47uv5vJXrg%2FqiUheuHG6na3nA1eS83DkFZKix7NdR733Vp18VYNDYbcgLySG1zC%2FyUbT9lsVrb1Myde6fgPlFQ1O6CAJesd9Zg%2BEipDcc%2B9cRi3hRpALIC%2FEv39nrCl90vFhsH6waHyS1ZgBPDU%2FsKSnvVzNAUxHw7hleF47dCUs30WN3mEAq3MBmEKlaLiaNodRvmIzzd1y3m6jWEAdjQksYS6o%2BIwpAhsVdatu7rEIU1hXk2hn3nxntMl4klrSVH%2B%2FkdyWg8ZMAufgdA1K%2FheoAhtITJT1yUP9TlxZ6X48qw0f8iQOZJdidyHyvnOzCyulG7xAYU2t5lEwMpj3fbh6x414CtAXeUatn5kEgUQp1z5sDjKfGeu1xNDmtoBadATXqfmDXsKXr%2B2Pq8cD%2FPZ9lkpMdaOolz6ChURyDmLvg3dFaLclpmMIkkw3a0eODnnZ8hJW0IDV58MTgA2ZOva9IzCP%2BV9qGeLp1NtnWsyPfAq0%2F2B7l4Sri2fkdRlWnV6dzJ2Dr6LFyB1IKD3Xl5MYSAGCNDQIF0TGbGyQVDk%2F9z3YXwVD6YuJ5PsPnaxwI2x%2FcFTxATQDwPECnj%2BdYMVrWOpe8ZtjqAEw8rqOvQY6pgH%2F8DC0yWQMKL%2BQHTswUE%2BszDDcZVR4QMfHDlcP96Mq2vjv5dUWZas%2BPSL3nfiJKPVznBfxZmByHncbbuEnGEHrL4lpZr7ke57anhw05wA03dYuoJWVUm9CQswNqtgyayP8b6bu35HqbWw1MqIFo8pz0TagV3yXo2NKTPSyVlCs9r8h6NCUrf20r6BZ0%2BmqUA3HTXgEmJan8Vjhuv2rTsPW0I6RPEoU&X-Amz-Signature=090ef8013ba2bed314d6f3fa4da2be91e5202f68b9884d7eaf1392396abb29ac&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LSMPAEK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDUXX%2BM4mgzAlRaNyzTLygpR23aMKp1eElF193ScrpBVAiB9e6qNGvyZqu3B9K6l2QGZMcNgPigwCJ0IhipvRq7heCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMepnsXYgkEIAKWvjQKtwDQYKg6RWjKrmgAnBt9WE9Xmx%2Fq23gEwOtU4sbA4N467%2BFa0Q6LqvQWo0B38cuMGAQNanqgCHQkhWiTtbs%2BEjPzd6SCSFjVIyllLRliYyNwYHe9ZCz1MFD6Q6Lod9zlUKaom0wR8flCh36tgXyN%2Fh%2BWIs1KauKX9WDUNi5vuiAiZzX7MpOENT%2FYTlirMlB6vpxl46XqF5PBm4ahH%2F1jB%2F1YBMrB95MYHi2OClviVbl8%2BWPfmVfOcRAkUgEru59G183xcOOx1JSo3y%2BGqr35S5NSbaHeJX%2BNDU03ZyRpms3tMumwxykIkGCEqj6vDoduARyTVpbHzyp9mlX76H6Z61Cs808WvnpFroldq92ylBsrim%2BfTxwPhBzWdxA%2F1Yozcznx%2FQ%2BCxvhCflIUPzmX9yR7RbkLyFrDwkg0aijP3vSX4xnf8vmQT5uNnJBvk%2FYgHLBFAu%2FZxEvQNU%2Bx7CArWTsJGDM1ynKi6ChK522AkIfM3PKXMxh7wxnB2Knwt%2FCpVTFJw4UgRtih0LfWLd2nMikCtotvI2%2BkgD4EcMI09ryc1JCx9rreSfHHiZtIeYu817F94S8b9kotrwraAy1B0O7iN0HqK64tCbzAZtR6Xf97mr84b%2F8Jcj%2F%2BCTAIjkw7LqOvQY6pgEdwB%2F8%2FsBWZt7sVPggFF3nOXzoMh%2BN3M3wBnXUIQMF4zAZZmKgoa2LqC4RPJ3yY%2FTODkCe2B7YtvYFBZtuy7wLO3PuA2sg2oX%2BzWjiSoQBeCho8vNfYfr1I7rRFl%2Bc%2B5U7RstdfytAhwuOdRo84UgwOMauPn1PJT9vhwHRO0qz0y%2FXP2eFcdxMQmjSKavQXJPgONNovcIi%2ByIRreNI%2BKc%2FOoH2T2WG&X-Amz-Signature=7c328d7c8012522b0547d549bcbe0df4ab122c9af16f68d187c87c29169c6bc1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFA4QBRP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCaNZE5sW53s2hensoKj%2BUCHrkkft3Ii5kBSf4JGuQkWgIga1TiM0KZsMkgtcxt6wKfBEGK3d%2FSWucZDnN5Bmgfoisq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFsBBBKa3GNJLCRhwyrcA3dFa7LcRgwkOGSBaJhrGfdmNWxtyM41pkav7Y8D%2Bc4wA6NBMizQicywCGbHp9HkQadnUFOEjANZA%2BLiqa6d%2BVhn9t3AsL%2BwPOtlMIqhM2JxmyskddbP1ZE0HKv5ubvYmSMqI26fM%2FRoZReQf6I9mKH25AT1gwbEq75fTITZlsAbZhyjM4J2B%2BUXRkVVIJ66HZf6NbvV4P%2FJfCwCmWGsVr0MDvh7qaepqbz0eCFoZlQOw7ntKkmc1lB01%2F0NeLCtQFeU9Ek%2F4bypIPmBSFvGyRK92ubtsoBZtc7VeUPRWv2RBppjTcjBGQVNI3DMiOirxPRbm6BlO1dalaUXYOSaBpHH%2B91KIobj8GSFYOzjwpEBcl4NPK92PxECo%2FuxstcTJA3RM1jlJljtHo%2Fy65UopaAcqGicBja%2Blq3eeEBjJPt0XBUvOxZDZARluau2ZllTwGDYBtr2OtuFvT3qqh8tRRzfvubw%2BD6TdVqdMI5QH%2FpH9OKXIsVWHb0qfPolyNJjXGzdUxUiOgd1OW%2BHeho5Q3uNO5QhLx8g1UEtFZEerjYW5HaIaBcWgaJ9tJxOXcGLL4Su18%2F1Hpe9Q8%2B35dxMZ8SAhq9tK%2Bm2Gh1NA7m4KLMYqaiQO9J2WLC5bqO%2FMJm6jr0GOqUBHrTyMrp5wc0V9I9RGtvJqmVMak9jqvC4JEFuEU6mn3FEb7RVF%2Bu0%2FP3WAkZENHX45nfaDovHMG8JQLULvP7jJs2d8PS3qjW5UV8DvVYwQBE3%2BNaJCavTDT5FO5tSBqSkjBic6UPSEi6RGOj30YUw4iIwvhvCyNUkXGyJ2dDERkiUw7TczRj6zOkRiKTOsVlYNf%2FIgvpXaZ3dw0IyyPpF3DPTSk%2Bg&X-Amz-Signature=cfca55fd0b6563bd53c1ea66ff9cb9f570aa2b39e9bf0a9e9d3115386e82697e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLNGXVOT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIFJRiqZxa8ewJeF0GvEMjLLuzgwqqEQT%2FD8VIt7NCqWdAiEAtoEgUdaFyZ74F6oJVqe%2F6HEKvGmAiGDNHXZfbLt4LhUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDA7t1vxoAL0ufLjsJircAwrkeusrP1R5RUwpL37gQn52x1OP5YGZHPxf8nKCKKtD%2F%2FEIDkUfghvRj71rk4zEgbyui6l5iXfZyXAxEBmNyxOeBxq%2B2a9G6ydiELjIlCr%2B08NzgGPjQMJEQi15h8ixLOpmrCR1D9qPMIMS6zW1yzCHQxdpGGpMiYlI5PVnds9fiMMnCc5wnYfeX%2B926DohmHy1DR9Xl%2BxPjSyfkkjflibdChtjGpxeiWgkETh%2FDkeqy4%2B3LN3mBjcdy7EDA%2BWlTo6IRsSeqbGBQHMdVT1VfIsoGmTJRxpGSyJyWwjhSqXHJeN9kSK1wBYubJv1WnZWfHg5iIRIDuULwfQzzzf6ehKEt0lw4i5njyoj0q2JuitwcgcmY%2BmSjU%2Fl2m%2BA7l9ZAPmWd%2BlT2yS1VNEfn%2BwSBiQhruCTTCb7UeDXZHN1d7m5gUgeQXNm96YRGqRChRo6xSTHTTAL5Ta00dKYqqGJ375AMhMci6q6r9duUTlNtX302IkUtwxjDEgKeztf7wohj9fmN72q3Y1rNS4Lx9bkG3d0dQvPD9X007Gd9afMpMR%2Fvrkc3pDLSws5Noj9gp7nUZbI3dZyPPTV8efoFK5oDxRPX3dzGO2xRjqemjzsyqCCskwLyMd7zXVj7WuxMKS6jr0GOqUBNsg3KgwKCw5koQYIMyNo%2F1Dc0VoL5Mx0KgHvMBkSfVe78Gc2W8nkDe15q%2FvneIbqczrhMfu0O2oPLZzWw3Gz4Yk4irxVn8NiAqNzMMK1XFx5Zy3Q5cDp0TBP95%2FbncLqdpB50rComI6tjpadFyKNrMNXk5ef6IBJTEtWwVf%2FWSk8F6AzlsE72id0J8u6H9rdByuMZQgVT4Q0t6X01t5Ye6cVD6UM&X-Amz-Signature=7aa1c0e59496a7a5f98f8951e7484fe131f26ee59f20decdcb766078c02397b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCYDGKRR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCICb2JXYEz2MApV5RJCV05yWOZdOKhFDc%2B4AI9233OLYJAiEAsgYoDEjhJI9SbfDitrnMv1J5D%2BqHJWou6St%2BUxGvTTYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDIoVsfx2EJpWctBo1yrcA%2BbL1rz2Ws3G%2B5EimiaBEcBNdjU%2Bbv0NpgKxAWLmUV4Vgd6qH9x9zAq0DF1nMz5tc14VjRW9dq4tC3kyhEyKsqlO5DVnzDY2Wxxs5fcsN%2BN2KwdJSCI%2FvE2IpoWE6UhqQ7GnvPFMwDSZFzbYCQ1IXx68ZDkTURp9aRGMILLTi07H6pnPlEBax9Ts%2BW6LfrcX5IerSBHoSu%2BZ71Y2rzw3xWcF%2BI5z4g8BND8M15qT3DWmE6j%2F2zQOhDXlMoTxoAoaBU26ci9Kh1MhrLpJ2exhxEdrNOtw30oZUWzA0T5pLd0%2F7%2BWS36jFkqvtJg384lydk%2FO95oYmLDU%2Belqgijy63o6GfVSgvF3MMlIwic6eap4Gtu8Ec8zp%2BVNXWX65szH2qf2R3a7aQ6NlRhLiBa8bzlag7F%2FXUWwDI8H%2Bi7IVLbAKU8mwKkmWH7FPwWq7pQ4OWKetMmo3c20xOBopImg5nJSVbRSVz9%2FjZ2diAionNgC0g86uuAMvSW8PI4lwhGTbWKUK0EfB7qR%2BEenLp6btYx7682DuibicAyDA75FPj%2Btu288nF64hwRxVJLNzw%2BH7VEKHid%2FiuzFOVuhkl6zT2pTbocWdgTA0cSRrQmG0QRrdWNBC0EyLN%2FkheVljMNm6jr0GOqUBzV1sMHS13sADYy8W%2BXyIgsvhidelTh1WcmTmE%2BVe0tD3Bz8UvSmEefvzOHl8hVcpzYGNwa%2FsrAWU5HOQnynHOUgGqcA%2F3%2FUhd3fqFblVzYxlpvCXfg5U%2Bo62p3YhcgtyYOiKUFIh8VnXjOmB3NyxINmjJyzcuL9OGjw6V8pyXgKJqyiFwCYPYLgjzw%2F9JV9TogljTKThwqr4GcTZQvi3mJpRkYo7&X-Amz-Signature=de7a91ed6251fb9cddfcfaad08a7ab9c89932809d5170b8b3012bf38fa0608f2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUFJKTGD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDtPkWAciba2hxqczo2keqxSvHpoESlLSXyDlC%2Bm5RmZAiA0dLfvtP%2BsTtx9E1fV2omAIU2Ub%2B4XTCeTlWBvxHXqEir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMm3AGl3gx1DLrjqY%2BKtwDJ8ZfoLHQE%2FVtVUXr8v1M9%2F4uBANz2RIOwFV0HijuhyufQLgI6GTQZk9MkBWR8PoQXllHsRYYO30iP1jTsUAV1n16nnYiKy2OO80ALXvtmHZlqzm5vtFG1fw3X3jRJs4I6cLsU%2F4kyVQa1K4ZenG8F%2F%2BFioQRGpnu%2FMTk5qNrA4ezbkBkRzq%2FHiYvrib9vzpQr5lbVdk9H14MUPU9gTUzRrGkww%2Fo%2BwW2%2FY08FLXoJcDTWKQdEi4uLTZKiqbrfrKM61Kp39wGnDCDbiHWIwrrz42zkzPvBgNCDpUhlkFeUZ1HxbVRhGTxiw5hDmDX4vsVd4%2FKMSR5Srz8YznW0LVBnrDF8uYAX29IHYiWYPYNNUERbn%2FXej9BnMKn7Ciu1LVf2%2BEdZwiUbdsLDL1aC5fEuAiRuxv6Q7Y8bHaHVekjAU3SzziwwI%2FleogMkqpfntvFN9Vkge7yw%2B%2F6%2Frrrl6%2F3mEL4UKha11lo4AqSk50kVjAc7mE9P5pw3H3XW07hNo4fklKporJQyK%2FnHJzxQLyhPitNya0NDjeO0fJaEguL6%2F9ziJJS9ofbA4j0kyXIU7t0vRCbe0v1wp26XHRUN2iNJbnEtJaq1NTGbCogCLbxY47PtW%2FYnn6jVC55ya8w5bqOvQY6pgHO5qnZIzgGNNg58RJ06724QqmblFeWvtBXDE3vOUI3h5DNv0sZQmpHQEZCkbLJSrTs1LqQyRwewjEYc%2Ft6WMfY8wZa5DLZVt6PupAe6b82muokAD7wfDwYI1uC2SX1huzC5eQDvX4pQKsGUD8US350DMvnYsChbXxa26DmhKF76rHVVx0tVLGNTdxoMS8eeUr0lEpOhnkDSO0xX9pbW%2F2hElbfNo1j&X-Amz-Signature=2d3bf579630815e74e6089b1f3c7d09fb41e2265f7c52d733f347ae1f232808d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWTTCBQQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGev0S4JNHLCVP48thibZCHGC5upujxBL4fZLoA0ClWGAiEAmwmd0zFnjJ27mw2WmSJ0%2FJDZ8%2BICTrjXAT86F5zfAeQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFrzWV4u5iU6OIGXGSrcA20qmp1qbFKuIIBg5rDrDS6vQWCl2Xw6yZpdV7tF6kZPcHRPipYDvBdqzOsZQvJDbT052xJdXXuz0oq8lGjQofZ17RaIl%2BdwrAvhOmrqs%2BJUmNwEu1lUI6aHdKJQsyTPuwdsJwbMG80CsQGrOT0AAzLx9bS1EjvErhBysScyjtleXpFzYoHXT%2BeIB8LrZ9%2FI2lGZ0g1MwSSDWJ1WvxXBljndnQoYwHFez2SB1KgHi42C1P5zV4bnnyiyOy6OjEObg8rzc6RrvY1vFh1vbmvcB2LaQlmpO0pxcxa%2FB9dQ8fViaN3bxXrYLs57R01UJM8Ci9JYVMJzNxBM3WKzw7IKeo%2F6tDYe9vQVUDjj9pOhw3WCP63L6GXk0OiQcMVgrHTS35pasMkOFG44LIcjdlui2P8N2cZ%2FbTUTu9O0KVZjOBjFSYgCC1UsDSDY3wyBoO2ZJhtLNfWVi6%2BUSTzdcsNIg6mNlLHJZMuseP5VmWI8QzXG8ofNhhh1UuHRnIu0RQloDlgejVbJCmtkysKV49bveEJJ1lSCZhOJpEsAZFRY%2Fn79mzaYoG9IqlHFbO2TBu9LPC7X3J4sh6P3oyq1YOgCDryySe3OcwlqZFIJWce4nsbpewX2jwdSD2hPKR4uMMC6jr0GOqUB2mFv5aU2P2hYNC%2FrE1KvbxApAvFYfdkq2GA8VHFnLJpczat2YwG%2ByNNvLvDJwUU28tfz73RpsYaWlnKowvvqHdjWcn7FtSFTrEASRzrwhQ3C7DFfLS9NMAJqzM6uLNf9fMowfcc0zYS1QQSHau%2FXzWydwIcHFNQ%2BTexIYbaWnY2F0JzFS5%2FqJd6XT727g%2FYmoxHwuJo2ephUoctvF8CHMRiZ5UDW&X-Amz-Signature=204c14dd0ceecb60bd8b3f774c1b77831f248648b93cdb35751d58b36442ee36&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2KRNR7M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCTG7llKuMLKRgX8S%2BpSdQKNnxmRF1OhRh9LQTdDgjr1QIgMwLdldbcbizCd85D%2FOfIruo8BrXQYWnLu6PFMNaYHNsq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPB4w5RxHxIZTZ8ZzSrcA3Px8PeW60ufxXA9HGWn5qfqhOirr07M6ytqKzOafAVHYm730j%2BpiRnYf3dx3JyUW2IYrqYijdkEmPsK1Yupt0FmeyNSu2KqrgC7Vxb5sqix4bquEVumnt4QFBeR8nSkTDs0VOYUa7ylnAOOrXq3e97qGPEzl%2BA43cCQd6Egvu6JSsNtOqV9iWcW3SljGgmf%2B6DgMyhW5kMy96l%2Fnt8Xvlau4%2FqWjg4ULOHDb1M1TVCnhL3O4i0enbM1AktuPmvnsSsDS2J3CieWY6vdjZt5QHihAzFWifb80%2BwjfHEuzPt6TEVKyikwfD1OLg%2Btshdvddqenu2gQTBWihtC4e75t%2BGbxlctT%2FPWvhak1s7t5EYhNp551IlU4tKRe%2B9fs2iOOV3U3s5axiP8zUyf%2FvO31gzrC9Vy%2BNdb1u6UjKmCSucETNHPslCYS%2Bh1h7pYZKzNUE8CCG4pt58L%2BK7TxpzMT8S2kRXyl6ZxCor5NvEeSmm9Y2AhsxxbJZE9gkKU2vbtdjBrdjt1ZBODdC7m8hPSRUlUMs2KNWwsaknrb6vynskq7LOxhPbFf1MzGBhNldG461zVg1n%2FEtHxI%2F%2FOYDokCDA4cEbHHwbICeANPz38QuOF8i4UeeGseAgFstwtMLm6jr0GOqUBl3uso4jAU96WWDlBcWlVkR6Fyi6Y6Z99FB09MtSIILuIZxgiprY9pMkyeLr6MT8XMDPkgv7X6DTKmoLcaOus7wgHswohHOfQBDIP40mh9h4Z%2FLUqtVY%2FAftnzGwhn%2Bvm0hXW%2F054geU3yxU0Gm0xXb7LPyVrfSWQQGRZA%2FX8p3DZC%2FTlF1horTv%2FqSyHBxhynxyz23rHQ%2FKQc5J8U2Rni0oSV8KX&X-Amz-Signature=975a0efcdf36c4d9661b50b02f3cab7f2673f74dee4745016149be12e62c81e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCYDGKRR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCICb2JXYEz2MApV5RJCV05yWOZdOKhFDc%2B4AI9233OLYJAiEAsgYoDEjhJI9SbfDitrnMv1J5D%2BqHJWou6St%2BUxGvTTYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDIoVsfx2EJpWctBo1yrcA%2BbL1rz2Ws3G%2B5EimiaBEcBNdjU%2Bbv0NpgKxAWLmUV4Vgd6qH9x9zAq0DF1nMz5tc14VjRW9dq4tC3kyhEyKsqlO5DVnzDY2Wxxs5fcsN%2BN2KwdJSCI%2FvE2IpoWE6UhqQ7GnvPFMwDSZFzbYCQ1IXx68ZDkTURp9aRGMILLTi07H6pnPlEBax9Ts%2BW6LfrcX5IerSBHoSu%2BZ71Y2rzw3xWcF%2BI5z4g8BND8M15qT3DWmE6j%2F2zQOhDXlMoTxoAoaBU26ci9Kh1MhrLpJ2exhxEdrNOtw30oZUWzA0T5pLd0%2F7%2BWS36jFkqvtJg384lydk%2FO95oYmLDU%2Belqgijy63o6GfVSgvF3MMlIwic6eap4Gtu8Ec8zp%2BVNXWX65szH2qf2R3a7aQ6NlRhLiBa8bzlag7F%2FXUWwDI8H%2Bi7IVLbAKU8mwKkmWH7FPwWq7pQ4OWKetMmo3c20xOBopImg5nJSVbRSVz9%2FjZ2diAionNgC0g86uuAMvSW8PI4lwhGTbWKUK0EfB7qR%2BEenLp6btYx7682DuibicAyDA75FPj%2Btu288nF64hwRxVJLNzw%2BH7VEKHid%2FiuzFOVuhkl6zT2pTbocWdgTA0cSRrQmG0QRrdWNBC0EyLN%2FkheVljMNm6jr0GOqUBzV1sMHS13sADYy8W%2BXyIgsvhidelTh1WcmTmE%2BVe0tD3Bz8UvSmEefvzOHl8hVcpzYGNwa%2FsrAWU5HOQnynHOUgGqcA%2F3%2FUhd3fqFblVzYxlpvCXfg5U%2Bo62p3YhcgtyYOiKUFIh8VnXjOmB3NyxINmjJyzcuL9OGjw6V8pyXgKJqyiFwCYPYLgjzw%2F9JV9TogljTKThwqr4GcTZQvi3mJpRkYo7&X-Amz-Signature=c4d6ddc5ca88ecb07ad555dc16f0b141725af7fbc1ac0cab5efd49154c1e0967&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2Z6RMVA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDZ%2B81kjmfHQHDGJkU9McCiKQem2sew2oahMbDdhwCR8AIhAPmPxJ0I9aLM%2FjBc0FpYnY5QNbVVgCiBA35f3diPuk9rKv8DCEoQABoMNjM3NDIzMTgzODA1IgyQxxHwbgkBToFNor0q3APVeZ11l4xEr3uSo9lv8fY3%2FWjo4uN2XpPKLB933lFg4QcqeKnvM8A2s97lH%2B%2BGiokvkTwPa6Pjb9RpVcxmjH9whB7E51RpRaf8bLPm3XYfrQN5htUt7h6OzymPtjDMPGJ8wadkInbDUh2cCMVQvJrvGj0lS1JbRhEcVd5W98oud8GM1lm4Hr34owW9n07ZfmPs7tma4piOL9wOkzV7V%2BKkeRiMOfBbqB2zYsvV%2FNC1rrR0ojPI91c49IAW5R7y0YKO0LfOREzKSkH3%2Fcx88xcf2HvnCuNio%2BPXThT86M8b%2Fzrq0yokIr5D3d%2FHLdZTpydjTpA5nfJiFamlizUTpbd832VycP%2Fj69jMfKm82pj%2BDwcvcI3O10nf0QuT6etRNR%2Bf%2B1A6ELNj0UKNemacqMgyecIvOnnpW546bDvSe4RpblsB5AtBlSsWCwJa8A2A7VK4Vy7Cnby5czRNY%2BoRAWvYa%2Biz3oTosNJFzhG9NIURWkkRlUl5bfmAyJxgrYo0SHr7NYB5WHCKIy4KJ%2BiiY9XRpfN3h%2B8lecsDB67dLbgbYQ8YOfi7O4oNMiEFjb5Wh%2BvHUQ2RwlpwaBHz8c43xfqy3J5UE%2BPJpf25NqKsraBtQWRff21OMekrwQ1p3DDUuo69BjqkAZHGT%2FoBmT9FAUA%2BLPX%2FlKAuMg7R0ahF2n5eCzfF7vGU3inqXAQU25DN66g5Qw9ZYffpYLaKgOU%2FHMhQweIzZaLwpin9Z2Au7xRNbKhDeIApROSLTEopedhfrMhfpdWWTcZlEyO7MtpUgycLFVZxWfkf%2FDZpHHJqpoJO8A4ThI9hU64e0JL%2FZkRuHGb0hEvt3dbKad8Ugah%2FyWXA%2FdUGxqcwloCs&X-Amz-Signature=be2047388e81ec494c6335b98079b5a1c9c577cfcd193fa2b05b49e6f8be4cd7&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2Z6RMVA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDZ%2B81kjmfHQHDGJkU9McCiKQem2sew2oahMbDdhwCR8AIhAPmPxJ0I9aLM%2FjBc0FpYnY5QNbVVgCiBA35f3diPuk9rKv8DCEoQABoMNjM3NDIzMTgzODA1IgyQxxHwbgkBToFNor0q3APVeZ11l4xEr3uSo9lv8fY3%2FWjo4uN2XpPKLB933lFg4QcqeKnvM8A2s97lH%2B%2BGiokvkTwPa6Pjb9RpVcxmjH9whB7E51RpRaf8bLPm3XYfrQN5htUt7h6OzymPtjDMPGJ8wadkInbDUh2cCMVQvJrvGj0lS1JbRhEcVd5W98oud8GM1lm4Hr34owW9n07ZfmPs7tma4piOL9wOkzV7V%2BKkeRiMOfBbqB2zYsvV%2FNC1rrR0ojPI91c49IAW5R7y0YKO0LfOREzKSkH3%2Fcx88xcf2HvnCuNio%2BPXThT86M8b%2Fzrq0yokIr5D3d%2FHLdZTpydjTpA5nfJiFamlizUTpbd832VycP%2Fj69jMfKm82pj%2BDwcvcI3O10nf0QuT6etRNR%2Bf%2B1A6ELNj0UKNemacqMgyecIvOnnpW546bDvSe4RpblsB5AtBlSsWCwJa8A2A7VK4Vy7Cnby5czRNY%2BoRAWvYa%2Biz3oTosNJFzhG9NIURWkkRlUl5bfmAyJxgrYo0SHr7NYB5WHCKIy4KJ%2BiiY9XRpfN3h%2B8lecsDB67dLbgbYQ8YOfi7O4oNMiEFjb5Wh%2BvHUQ2RwlpwaBHz8c43xfqy3J5UE%2BPJpf25NqKsraBtQWRff21OMekrwQ1p3DDUuo69BjqkAZHGT%2FoBmT9FAUA%2BLPX%2FlKAuMg7R0ahF2n5eCzfF7vGU3inqXAQU25DN66g5Qw9ZYffpYLaKgOU%2FHMhQweIzZaLwpin9Z2Au7xRNbKhDeIApROSLTEopedhfrMhfpdWWTcZlEyO7MtpUgycLFVZxWfkf%2FDZpHHJqpoJO8A4ThI9hU64e0JL%2FZkRuHGb0hEvt3dbKad8Ugah%2FyWXA%2FdUGxqcwloCs&X-Amz-Signature=92cc9bf1dc61d280d2fdcaf0caf7a1a71503a87cabbc65f367e69b955a8fe13b&X-Amz-SignedHeaders=host&x-id=GetObject)
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