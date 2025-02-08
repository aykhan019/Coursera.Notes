

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIIIOY6M%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDll9tEnhUZvQj%2B2GyrgQHFcCGVmvI5dTPWcapb8eiJYAIgZs7cgo8vrOGBB2UkmZC3qBN0eGZ2pWUsWaBr6IqdcnAqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKF%2F%2FzJKRlNiUPkzTCrcA7IssE027rINxMczdKyeMekH01RVY1%2FB%2FHCBoVqS%2BomWrZhFdHsmZFQyksJIpwWUOHtkTsvrDCp9399N9JhHfo3kKkiJzZM52aI%2FbdwPOoAOtI2dDjZwQly3Sle3816yyPyrQ6WeBunhWXF%2BYzCPRQEhZ%2FP6fWjo4fjpAuX76F6jhODlHx%2FEJdFEa%2FFpK9v%2BaHkCr4eoVkd1%2BmS1YdSqHJ5cFU%2FkemzpJBBUcP8ATKR6RwpWjrZ%2BsL3dxzZQ7KDN8c5Z0APdAdnFWGXOrubK1gRUoV76aXV7%2BKbRFZ47IDW%2BFIR5lYCulQWooH18giGmL89ObCl4F%2BASlMiWRkvr3wHuX8knCb18AsrxBxBqNJ2HY2%2FijRuSN5GN5RW3bgTpwp566%2Fohf2i2QDHHCodCk8rtmFHPTZhT0TrMa0NhWdAkNU6bauEzagzmhXcUxWe2%2F8rMZj7jOV5uMbyGxuKYFp8ouqkuMQVZMRpRnWe1hgyPoNinSQtvcaFij%2B1Ztn%2BMicCdBOSg%2BRYChm%2F1YZji32KS2mCWW7MC1fwyle96UwsTb85HkNHhN%2BbUQa9u6wtlvKdtqsEsO2io2xxUx6DBp1IFcBOzuqK%2B%2BfyTuFKtyYU0AWuoWP6MeusOFrtXMICFnb0GOqUBMu9o9XmRIsHsXhfoaQ8LqbtsnJ0jpO5Vfayo79BaSjTYGSaVwzyI9HD889rmyEZd18NaZKxPx2pUXrrDhWeiQQGmCkKYXYrJErc3bGup1Q0AsYqcfmsVhGEHGklBWomenRnnAbprjc%2Bf4zGIyTouQCTH%2BgY0Q683rbj2U0N0lPHr8ZUZpvZ7%2Fw3lrKtuonWKQv4pwMtCGeICTN2jz6pfXk0hzQQg&X-Amz-Signature=e0ea9fda3da94f5ad13aefb58ffc17f2ba209ae660b89b46b8b834f0e9ee97e8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U66BUENN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDlMJBzgvTSWJy%2FLFbhtfHNQ21lkk3LMhBVwcFkwj%2FYGQIhAJ0SyqJFuh56tMsD69wbTLdbNQw7VDe5AFjInC%2BVXT8NKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAet8uNOcbZtBsowsq3AMA%2BTIvlr2FOsmiN9IGixM0MJopN%2FMAyjUZNScE6gUoS3npZNOYgEgoxgA1sV%2FU%2F4pxqzGDbjESu9vShsWM2dnG2TjfmtU0n%2FJ3cuWwG2JWB2Aw9wLGkI3IvamopmMg9FyFfkAbLo6RLVo7V7pp1WJ%2Bia7bQtZ8XM3zYQpbPh1K4Av2sEv1RDm0uAF05K4vGFQPaBM8PMuy%2BjZefiQKOLu%2BJ47YDN0X%2FBDqF7yRgiVLJeIQNtc5JF89eUIxBqdlmoWGzEpHn6Z1Ph5DSwoSRAvAyBoi0D2WyvFUfiLA9QliTL9aVJOwIX5hUTUscWKSaXGZ7vP%2BnZoOicPbngqtLtDGFzcU4HEIWbdxIJLfobEldClUvWfNh5nGisiKR3HYGb0W6Yprrg%2FeauDHAoqHV0IwtvL842G7BKlaU2ikrMjSAWEq7AI9Sj5eC4%2FWwyeTteOEKE3SZeAKNPMMQ7gUe3W7g3iZUxwRuvJtQS%2Brd7ZQKiWfyzJk9C3qk17QYwbQMPhOzUhmYp%2F4xIxnJrYTUoAz3Kl%2F9r%2BJ%2Fk7mApngVxptjps5Kjv398eMU764Wz9RpfV5coIHkPJfkGXTSdjCGATG2w6I9jofM1m%2FgEM%2F5VT3AKnejhGR8Kx41H5NtzDPhZ29BjqkAQcHVF9gqCPQmZbuqHgDxNQ5id2RdO7lcjlUtZTgxoAhNpjyt8Pc82yF7nXg5VLWsxS1oi8T4Zacq%2F9DDyhz9cqJGYyBN5q7PJHoH8OFAjs0tMBG4chy3nOsYd9c4Mn5oOz9xIid5cChvnHHYUXP3PXMHpf1X5lSNA7xsYDvaIrX%2BryMBgOQdKsijQW5jZJ0grVz1GKirBAfOfazx5U8c7XKL%2FNl&X-Amz-Signature=205d7085bb1c07cd1c4dc1ccee692db7caffe01fbf3b647478effec9a7cfaaad&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJ4PPF3Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIAy3S%2BFkNy5XQi3LAIRfGLYjgu5fHpahTt5dtQaRTBAjAiAx9ikxPsB%2B1tgW1v0lP8eJkwhzcir1vAdTWFR8mWr3%2ByqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7vTLzGR%2Fis5IkJUjKtwDP3T4Z7wi86BVnFsgr7FqezmD%2BYqRIb4Tl0mW3CEVjbsCeyjYQ%2BaFRpK63GI%2FECvXfwt8h66agafCzgh3Z3HlX3nIgzO2dqXk8SxbcNnrArraikhzNrOFdYDRfh3UlGeBz6z9pYEUD3FiTlM7xaqU6uMRkQ91uFAmEJ3CwmYp3lDk%2BiNLEP2xtLrngrrMmYC1%2BeEZF7SoFZVD%2B1OKFgniCaI%2Fq8nZxXt%2Fof1UxWYPKmhwl48V2DCyXfgqMBMsmynoIBnw%2FipxOoS2TTtLXQEZVUsk5HmnHYgRVeiyLY%2Bwk0tCdy61Rhse%2FpjEylcwqo1%2BQ9GExQH%2FrJG4rrqQJAswxBaIAVofLl3CDDG3Nup%2B0%2BFqhkzZehDAvfnSx1B%2ByiHyysBbW4YrwuC4aNjDp9ntpmCXPzhHb4PsMMr8HIIEZzQG03%2BTqH9ab59mBcxdvWNwZAvE4p4TsGDjx%2FjeNYhusYU%2F2n3P0Y%2Buj%2BW4zBmfsEp%2FwYjn8B%2BsJcvOtUtZS6n3OScKS5uoG9MhKqhIHTuvKTby2tohvUJH8bsaLANcwZZeoZat9PdvzlYRL0xVNnot99NipzlnmZkb50FUMgUYN3InHxj689MRhri2SKWVew9HiLTIEEcVTs2WJlww%2FISdvQY6pgGKqUTZXOidYQk7mKZ4Y7WMIpKjye5rQzpULBqz0m%2FISkWEVGkoMXZDvSuymYv2CN1ucxs28A42KuiN1tehHqHXNimfUbj4JVIq09BEZkRSj5AxjDQ9IOsdcJkWJ2YmGdvKc7p%2B6cyQhm88h%2F53dCQcz1D05IXrj59L0YE06vDR0GOrkBfmPMV6HlirbeIYRVJdIorDZUVJ%2Fx4Hx4ZUkl7wQCNfk5cj&X-Amz-Signature=2140c1d62fed005d74f0b79680100ebad1ab9853024ecb6605dbe88b2f03cb71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEMOVYUH%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIDVmP63ruoMRm0ehZYcgHgsdRHaiXmukiY1iuyMtOyxCAiAqXz5wOFlBQVMSWp9AS8EP2ignvK4x7fo3taupuyg8%2FCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTQw6OVqKuOC%2F6wDGKtwDyK4kL93a%2BuizrRR6bvyehOHjhkJmS0BtYMSWUJGRJec4xlcQQuWDwGvzzAhXuU0efJY74Td2vkfg7eXWftzePlDVshz3FaLfdGHGJKof%2BF1GFaGW3Ft60BbOkL3EvFJ7TJXWeIF2KJ0rVpx5kurZvhyhRo8uFTMT7DrLggSySi0uJo3%2BDDZQJSCULhrT3PUqVadnE5Vs4kLa%2BlY05qnWyEHZNgSHTzjasObwDvlRlQnW%2BIR28RD6hau8TTQemaV7qNBNWLSHPJGrFU8OH123XntzgNZa9nCQshqFWEQpNMmTExw3yRthuYKjtGRjgWs0neeiJkF48kErGNrBXrXSV6zh4H7qxCdAMXDCY8%2B6CX8D%2BQMLMBsFw6uzUm%2BfvBaoMzIXZ7h2Or2Ew9oX7mcdpenuoOMhqlpWaFPe3XlmcaQg8rSqGnophs9eJsuSPyoggyk40QrwvhqWkOYUWNx1PrsIkWmrR4KUn4W4H1S7S19FDROAy3DNYdtGgj14GFA1q75qjB0XAYAIqzmptUSLq01sm1KC3ucehBgb3Hj4CzAiHNe%2FYsNFHN4BEH3u2i%2B9hd8JA2bWJUaR0xa%2FWIHG3vW1RX52rF35wIdr5M2%2BYy7PGQdy10x9OBWKdzUwy4WdvQY6pgHXNsv34O8WGxBGWHMGKcrjWX3zoNGJeRxYqQ0CABNd1cT0J7gOOh7J7WGve8oLyv2CZPqhTjKO5IH5NMrAswPTLXcejgmN1DrdyWZYiWXlwPPGS5AwIBnI4%2F2eG0RpxPRUT6kNk4sIf8LT7VbvcZJQDiNza5s5FWfyroYRYV%2BzH0nSdbpFwuYITm3%2FlCULAI6UgEfFR%2BPwWRyQyohTXGcrGOFh7%2FFA&X-Amz-Signature=7c5181f4f801533db6cfc094c60b8e1e8d1e0e36bee3a29ad800633a30e891a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW2D5JGR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIEMgyqGCKqIyDd63N1MbfnLTP2ZLe8wcpwQ2sfBhG1yGAiBmtyy83wwACURW7IK5VrcvJIYqZnPJAiErPYB0SaBgmSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9fZ7s2WrlPJScSsvKtwDP6n98HEpAjuVrIFIcirp7kvaMfsbensb5WxoIiUxFH%2BlSlbQt%2B5Flv5rAsDsYDC0h1QsuyNfJKPmR8KSDtpvGR8Ii%2Bt2UwCNk%2BpX6bidqn69bheREALhsP2vOjLrtS072rq6mxa1am3sWMT2He8YmOfUuF4730ueMCDddoOxcHF17OZBOoaiRbkwE8iLutw%2BWpb3F2xGsEZ2Yq%2BegNHOzWrEY3UwQntEC0%2FnExjZvuVfLLdA%2FZXNAoyCqn4epXhXznCjA83uGNgsZbhkZGYf%2Bvd1APUen9UlhWW%2B52BzeGEscsd2dXx7Rr0THcaWKzpx5BcRRDU%2FprncoMpkTOsWyp%2FRYFco4intVM525FPYsR%2FWcyK0zseHFjg9YPc55Lj5dDSl7xkB6lmIIwEidcGSzM%2FVv9nnlbjPGLPyjsJgD%2FsfvWqfaHtglR%2Fi%2B%2FYG0rLtW3slqO5Px3EvsjgUvGj5h4D2xKjEtfYHhuUXcFBBdpaloG%2B9N6UN0VYXHuNOwAdh37PXeTEVM1TkVQzfd3Kv0PYx8doilu0zOOybugyBFqrY3VZKiXzeEv%2FFb3H7GoWi4931F0XiHT%2FKbYJ7F6Q1F6mp3000uh0TGL2BdL8dPp%2By7OjldjsGpv5dnvkwioWdvQY6pgFGSjjdUpEvis7wfPViqljII8o530r%2BHeeAlIfngUx9it42MKV3itjqdRYtgI9NReB6C4xVXCxMomMFjtsH0Lq%2F7WHkpC719s4MFTc3xMgR5QKZf4aXV6L4Kb%2BoLtU6krfX%2FKP0YtAwFWWUtZvJmXp69aiIIWrKnKioYQ0Jb4nTQlzW4aLsFv1QtAsvRXDQNVJnnMrJYYR%2BEYKcOBVP2zpnta4FPkFU&X-Amz-Signature=ac4cf3c383780ef2a9189583e1e19917f8a572721738676a5c3deb115638fea8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466577SIZXO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCpSmkVYl6Tbd7q2Mlr4OxHIeELR%2FqPkkU%2FNABTEwUSYgIhAP%2BqV2DWY7s8wdFxw5J0YZw61nCpllykgmiiV5XbjIJwKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwd1vi4Wtm5K3GVnlMq3AOMRBiFY%2FjmE%2Bz8cxI8rS11aHuiuV%2FS%2Fhb4PjL4Vp14CYQeOoWIavNeijOSvG8v6I4a27feBOHB8k31uLXDReSSvN7QdPlJkvTnYKJN2BoWChihGldnQ53TNZkuC2vXGhXbI68z7WRNPr2AWNglf%2BmxT%2FlDQxW%2FZXuDSoHkP7%2BqsS9n52S%2FRVok6xhwCSUeVGkQzPzWHhsLzhlPcC2Q0ayA42aITXwoNQ9yoHU7kMdB1XeECcR9ZJxW9RFTFkwmHTLuLgHjavdSQlhlq2sN4xG084E7LibqdUD8SOatI23bdcMd5TcnHz4wKpBBnmcoBiUYz8cOVtZLCxZH%2FY85bIkFTmFaEDD2zZTW%2F%2BGmqt2NDgs3w6Mf9PcPc9Tr0QSNgOc9p5JgcU0%2FhT9%2Fs0yDXxFdSS6AS3e6ZvecY80OpSUIL6ZD29Y3pvQWyIED7zKvN1gGc%2FepLR9TkQSgfnb4UchTp3Ao7In9FZSp4nXfOKW0SLYD1YCC3eel2j7dQrVU6bNKeNDA594OEChh9KqnCsD76qk1PTaRja9QMGY2TmCMK%2BOztXT45jH8bC3NNj138Gc2H397eFj%2FFlQ8QWS9bkBiwNmpvtOroEWQ1F9wCdkzBU9aWrdwdhX4M7TvKzCyhZ29BjqkAWZxZ40PoJeCyGVlSiE9xjc7lJNiD5Lo3S5S9NhmjmXg3T6AkoD2cl6zFgIfbSlnx3K5VP2DBYmGB6R9RjHpNQFikApUoyMUHYMY3RdKg%2FG2wp4ZDTkPCRUNI7XWHx5w0ZkxGUJyrgohsiNTYcNVByZswGzf7CXCjuH4rJd%2B4Efo%2FmnSZpsW17jBO5HpJa32wSKaEc%2B1TEGOJu8pkuQNld6gzRzw&X-Amz-Signature=5111543dd31e57968bf8543c54f88d82edcdf4e5986c5c6bdc86a3f06b41c3e1&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y62SKI3F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIDbJXhjDzZH0HWBPLzeYhc8qHkbyOVkEBHyXEMoZtbzrAiB8l27CMi%2BcXQd9FKVaRzyhL9hmb2eWG2D7z8Wos%2FBphCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIlyJfEhix6haCGz7KtwDrD3PxHYjJK7AeqV5pZzL6NohP%2FIpDm%2BBS98u6jey6lLUFn%2Bl9Xmt9yE8Q25AsIKrblZKCVuwcdSoEgMCAGaXbNhrM5JfyNw0xfYIutKLfgGaqWKBt4EC%2F12Q0P8r29zahXGVbmCjRCvktul8a82lj%2B%2BmhxRFd4ZYt%2F1Q3iYTb0jd65Sfnj5jWBddyc%2BV11kWeQ0GyUNKRE2zqHJQyjLEVuP5kKMNoo2X35naBT%2FhNXJlnJWQrimbfw45oI90Et9dBSoGCRyvZdxZgNaTwUyOko1ECsMRrQWT3iN%2BYQeO%2F5fBwyX%2FEPqHUXHjmGArn2F5Zf5jUI9e2auS0%2FWwkVrSbnmcOjzZq4Qx8KlRS0vbREVxI7bkfM7V9ZIQULRxw4woJ8X%2B1U9yWk7qY2ffAgIHziKJYblvIzFOLiH8HjOO7ylthUbV0cD0loEzRJWS6XC4X0lzVSEr%2Ft1Cl8GJkPeblyIskOPzAII26obgL3qIEi8fF5Br0sjuKJVp%2B%2BTIdxCFBS2nv%2Fh5Ab3C%2FpWS7Cc1ZTBjWceW7gXPvJnLFgYGVZ1T6aQKjH7mnlZE15ToBBU%2FOuBJUQcNvlJ8BTtGBHU5f7ZWT6bDL44Rpyb1Z4%2Fd2cSVMFh%2FSL91A4QzCpQwqYWdvQY6pgFad4lCwSRaaq%2BDrQzFVwr9djjoQkT5Ejg%2B1QSa%2BixhykIMqG4s7NEBK3XkpkU05YsFFOkP8wx6quHw5yL6d9opngkCGcuOPVbN9b2XKaJRYU42Qlh2YwsLIrfpjVntgk1w0U4vFrbyCU%2BOu5xS4a2zQcZB71P04s5fidgrxfH1Gy1DKaenCH78Uls%2F7ewbSfiLL0QTg7ngOAAbwcgTh6Z9HDAixDGO&X-Amz-Signature=3028396df317fc76b6038cc53078df83f094ae8ea85479d7a37f3ed489d4d5f0&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HXEQWAE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDQyfajwPaKSui24JFaUiDUQ%2B76Hpg14drtGyyJnat1HwIgeHgzK0kz%2FLZ5%2FsgYl6JRxYTyJutziCzkiJRV4q5CD7kqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBTEzXrC8YWKSalVjircA8VA98E0oP5zyDPnAXZWlC3krmKG4V8g%2FcHQU52m8Y5Y5weTzJJk97Izt8DxUeJjvUKmhEK%2FF6SHDSQG3h9768PZ7TNp3p0B7A61zqEoGbpK4hfIgXw8uuIQlVeWc6NFyhmpc8xfAPDh7O%2B%2BI%2FCU2FiXhwfKRrGRqggka%2FSoikYZ%2FlvnK3NYZuZSb2ZqwY2%2FwBosZcXly9K1vUMDebLGteAHXmQhpJdlT3qrjRTRjbk%2BS3pG6tN5k7DcmzIC14baPPkVJcp4AhpkeeApq1mtG1VTVGN03SBnG08EkJpnutPqB2I4%2F0UgBH6vXCo8mCctchg7nfVJoDxI5gA6uGlMjqMSjwSkYq7hnPv2z5qGLNuJBbTWflKgH2UHorxmDSDTjrFMepmbAPX1gCi%2BzVjo0toj0o%2FAKYbNlxOdzk%2FC%2BStEzMhpn9HG4BW2ke5ozITaoS9u3oTp0RkLptdWNORGa%2B1u7X1g6Bn9clUeNctyhvlvh6f%2BYLWc8EOtG2bQJQlrdHJrtJDAlOvwcBmHULIv%2FGOPHsNQVgCtIt1VM1xFtavx2gSCd1SS5iAZ2aew8RF5KlILsuhcVQn3Dk%2FjEOH9qLGknr%2BhkvpG8bwCoxGM0F6Zp7FOWCeCkIuXFKfzMNmFnb0GOqUBmTiHtVw8Uvgv6gknXKF%2Bo%2BbD0cIASJWC%2Bn7%2FVnhIWgfJJytDxlNXW9o%2BimfEG61yIPtOz%2FfR5KTPbZiCVaC9RuFQO6JzqEopXBlV3lyXUs%2BLesPkrpWMynAHJ5w%2FZBtKZDy3xuWNqbGlw%2F0amHCEN8rOzqlgjczjOYif9X6I0Uk5ttf19rfHnaWBwhhvRC8TuWzTgogi689KVl9zVemT5w7bKxql&X-Amz-Signature=3b57f7f604d57301f5fe75c5ee61d534bc54f8a249136e947943d4a2e2665b38&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW2D5JGR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIEMgyqGCKqIyDd63N1MbfnLTP2ZLe8wcpwQ2sfBhG1yGAiBmtyy83wwACURW7IK5VrcvJIYqZnPJAiErPYB0SaBgmSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9fZ7s2WrlPJScSsvKtwDP6n98HEpAjuVrIFIcirp7kvaMfsbensb5WxoIiUxFH%2BlSlbQt%2B5Flv5rAsDsYDC0h1QsuyNfJKPmR8KSDtpvGR8Ii%2Bt2UwCNk%2BpX6bidqn69bheREALhsP2vOjLrtS072rq6mxa1am3sWMT2He8YmOfUuF4730ueMCDddoOxcHF17OZBOoaiRbkwE8iLutw%2BWpb3F2xGsEZ2Yq%2BegNHOzWrEY3UwQntEC0%2FnExjZvuVfLLdA%2FZXNAoyCqn4epXhXznCjA83uGNgsZbhkZGYf%2Bvd1APUen9UlhWW%2B52BzeGEscsd2dXx7Rr0THcaWKzpx5BcRRDU%2FprncoMpkTOsWyp%2FRYFco4intVM525FPYsR%2FWcyK0zseHFjg9YPc55Lj5dDSl7xkB6lmIIwEidcGSzM%2FVv9nnlbjPGLPyjsJgD%2FsfvWqfaHtglR%2Fi%2B%2FYG0rLtW3slqO5Px3EvsjgUvGj5h4D2xKjEtfYHhuUXcFBBdpaloG%2B9N6UN0VYXHuNOwAdh37PXeTEVM1TkVQzfd3Kv0PYx8doilu0zOOybugyBFqrY3VZKiXzeEv%2FFb3H7GoWi4931F0XiHT%2FKbYJ7F6Q1F6mp3000uh0TGL2BdL8dPp%2By7OjldjsGpv5dnvkwioWdvQY6pgFGSjjdUpEvis7wfPViqljII8o530r%2BHeeAlIfngUx9it42MKV3itjqdRYtgI9NReB6C4xVXCxMomMFjtsH0Lq%2F7WHkpC719s4MFTc3xMgR5QKZf4aXV6L4Kb%2BoLtU6krfX%2FKP0YtAwFWWUtZvJmXp69aiIIWrKnKioYQ0Jb4nTQlzW4aLsFv1QtAsvRXDQNVJnnMrJYYR%2BEYKcOBVP2zpnta4FPkFU&X-Amz-Signature=14f50e9be652c5a4eed76869863ce22a5177bd3e933bd64bff680cd218961ffb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STKKAFL5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBAYPSOluPdOYmfr%2FO1ZAzP9Fw1RiWiQCvwO%2BergQ4iZAiAdgY%2FU%2FiYWQmSa2CXBWtYZJ0lwmV9qr2glbkgTD4%2FQ%2FyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBJ21sa6YFBeUrvVcKtwDdNsBo%2ByIyGTGgnkZd5yA6BU7QH0l48PJ1O4uGxmVcS2tcdG8L4Pry6hfgTGgiVv16vs6nFbFIhEoGBhCqQ9B2CR%2BqJZwGyGSziiFoKHGy0SdkfVQa%2Fa9W8f3EfwXiItijIDB4jRpOfcmyX%2BfyvR5j2775MCIVJEaX8CgxltK9PemDo62%2Fue9dvi8Bjscr8qw8Ax8KO%2BKc6ZbnBhvtXWx2R0qxvtC0nCcj%2FVrxMqbnORp4VwVsBVBdkMmJf%2BFACiPeG1Lfy6lGzwptG4swWlWrgaVDlnSe8OpEBNpMvZcfSRW%2B%2FU%2FuaIMtbMG5QpB6bZUkrSzhpp3hLwErBL6MZ2HTTu5tuNL7qxYNqRLFm2WX%2Flyu%2FuJGEUv%2Bp6asFHbwMgNJM%2BDUkbDUdgNiX8cmzJ5wfGgXDqPsNqiM%2FLMGDm1Jzur2Biuv4Sz0MJ1AS%2BKwF6R9CO7%2F61w3OTGbCILdNndKl9LvQXrjB7yAkNSmsyNkLQ8ZOFKqw55GVM73dhgPCwnN1f1Uclog45yd2I8CH3uutzxLIaJm%2F24%2B2ZDowzJfSKHS0qBkaFsGx65vfoduirdZCkDgykjjiRAiNLGm8iqZhsT1cC2CcLy7FPwBq5n2WnF75GoO%2F2CdsDiKd4wtYWdvQY6pgEF5eTOsxXBdmuRteYHEC%2BGVyH2br46FN1ZpU3qCH23pxkWtYrh%2FdB3rMIwvEk6RB0YN0%2Bv4g77E%2B4cfoXK0uKn62b7L1LEVqi7fbK8LqNiwR0FVExPfzDdM4QYQaYDFfHFRPDdSPr0h3LkEsgrIsRZ%2ByV8TUdc3fFAHZBZYj%2FQIbna0X5I2j0LuS2GJjJnEY%2B6UBSJTmnXeyIsr62OuprryyGis6GO&X-Amz-Signature=79d6a54983b0c949c3931b700d44f4f9608c8b1252f7a48e816ef660324db963&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STKKAFL5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBAYPSOluPdOYmfr%2FO1ZAzP9Fw1RiWiQCvwO%2BergQ4iZAiAdgY%2FU%2FiYWQmSa2CXBWtYZJ0lwmV9qr2glbkgTD4%2FQ%2FyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBJ21sa6YFBeUrvVcKtwDdNsBo%2ByIyGTGgnkZd5yA6BU7QH0l48PJ1O4uGxmVcS2tcdG8L4Pry6hfgTGgiVv16vs6nFbFIhEoGBhCqQ9B2CR%2BqJZwGyGSziiFoKHGy0SdkfVQa%2Fa9W8f3EfwXiItijIDB4jRpOfcmyX%2BfyvR5j2775MCIVJEaX8CgxltK9PemDo62%2Fue9dvi8Bjscr8qw8Ax8KO%2BKc6ZbnBhvtXWx2R0qxvtC0nCcj%2FVrxMqbnORp4VwVsBVBdkMmJf%2BFACiPeG1Lfy6lGzwptG4swWlWrgaVDlnSe8OpEBNpMvZcfSRW%2B%2FU%2FuaIMtbMG5QpB6bZUkrSzhpp3hLwErBL6MZ2HTTu5tuNL7qxYNqRLFm2WX%2Flyu%2FuJGEUv%2Bp6asFHbwMgNJM%2BDUkbDUdgNiX8cmzJ5wfGgXDqPsNqiM%2FLMGDm1Jzur2Biuv4Sz0MJ1AS%2BKwF6R9CO7%2F61w3OTGbCILdNndKl9LvQXrjB7yAkNSmsyNkLQ8ZOFKqw55GVM73dhgPCwnN1f1Uclog45yd2I8CH3uutzxLIaJm%2F24%2B2ZDowzJfSKHS0qBkaFsGx65vfoduirdZCkDgykjjiRAiNLGm8iqZhsT1cC2CcLy7FPwBq5n2WnF75GoO%2F2CdsDiKd4wtYWdvQY6pgEF5eTOsxXBdmuRteYHEC%2BGVyH2br46FN1ZpU3qCH23pxkWtYrh%2FdB3rMIwvEk6RB0YN0%2Bv4g77E%2B4cfoXK0uKn62b7L1LEVqi7fbK8LqNiwR0FVExPfzDdM4QYQaYDFfHFRPDdSPr0h3LkEsgrIsRZ%2ByV8TUdc3fFAHZBZYj%2FQIbna0X5I2j0LuS2GJjJnEY%2B6UBSJTmnXeyIsr62OuprryyGis6GO&X-Amz-Signature=aa9485d3766428eec0355b7fdb84da7efe447e34eb289944e745fc0572e664b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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