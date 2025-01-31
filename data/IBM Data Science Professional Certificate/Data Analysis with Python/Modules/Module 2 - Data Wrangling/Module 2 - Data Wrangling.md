

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRYUUBLF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDPc5a6aRsGpyWlAwlTddwvxAxQACqSZyadUOvqmhBlAiBD4OFpXK17oPJPEAkZleD7%2FHtkalq5ciQEQp61SIzSPSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjKpbmy7UF2qIW%2BktKtwDTnn6Y3ZdUSvgd6WYLlsT77i7wIX%2FGk%2Fp3TxA9ti7fXmIqAO0%2BnQJ1k5%2FrcaaM1E2EzHViLuBBzd1zTaG%2BFhFId82Ajm9Odv9g4kEZl2vCWutGNQ%2FaNidpxkBlbnfF8%2BC6q%2B2lCJXX3CpsniWcea7IVtY5FSxN7vOdaESd0WF3IiZRfHFMIcbVWZ%2F8YElm65XRR7w%2BtLzWEicqNb%2BhkvPtvtWeDdk7QxUdDrcqipc6GFh0F8kIyHi0khpq%2B2UuhYokpgYwSccl3vh2gMQplU1Sj5qpZ4hbjY7lHQremIvpgYc8oMicjbg0A6kmWyx4r%2FMqisz4y%2FTaUL3NIPydKjyTt0MEzWxBQ5E8ykGI8zUhiGNNHx4vLLAEukEScFuh6l0wNE4nGve6%2BGrj%2FOArMVQH9jp4ToU0PYii0MCSLN5%2F%2FENayk6S2W83j%2Bq6up4N5S%2FAp64PAeGgtvjkfPCIqCePWqxVB1%2Bg9LXPQCx8w25%2ByV%2B6X9%2F7j1vMqVLpZPohQnWgRB%2BArnWsGnDW2kxkemKcucsUDTaU4UbuE67uJHJQgtTdrOS1L%2FRImN4vnoFnYomf3ZxtmNaVen3ip8cC3ztbb1n3G8OlVnqnFzkgbPNoyR3mqqo9jsp4kEwl2IwxaT0vAY6pgG6uu32DWvAWstxg8Y36ZDLilCPzlbVHkdh8gfjjhNL1P%2FTsuS2c97zlLz5zYBmO3uLnF7MYolGtXz%2F%2FOHdFuZExyRDnSdTnB%2FEzBT9d1I%2BLwOz4xw39Az2Uaqp9LNBXNB3HHOSNQNB7TXcxd1irn%2F9hlWzpQaGjmMLVVBDuOwg%2BRc6G1xUs9xTbtvc%2BlpJwK8fdF7LstSDyVr42r652aDPbZ5RZFTA&X-Amz-Signature=cd806e1b604cb0e7dec4a20c10b6a5076d7d21817ae85f0ebd40252114793713&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCLRPXYX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLKnnGYAebYzMTqDEIzHV9hdDAHkjBvQzCnvv3vuSbhwIhAMNB8TJPFmGI4qUY%2BTMVKKQ8ZdRNmQgoO8Zrc0fDbY8OKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy19mgpeQ4PQJec7QQq3AN1awmSWra69fkrhbaaJonlyfZfvsKAnbPuTBX4VT27TKPWa2IcV4FP2NwEVtj5EtpH07gUQDRA0p3hAv5RaLnNCYvALId5i%2FNIu%2BQVrwkL%2F3GbnJfVyHwUigQ8I1S1azPfbGV3KOES2G6UaT5uJSnZB4p3CXfcgfdsmdFH9iKIiqGdWNDQWR74T1Qo6AWPV%2FQvdGHBycttftuaA8CuIwmzJBXk9PjH3u6ovaUXZSVkpILuJSOcee%2BTBUqS8qpjiyIQWqoOxVNr76R%2FLCVHdZj8gWwqc7uwmhyMU7xNPEoe%2FH4%2F1nnNIGStk6%2BfIjWHybqjR2CilmOlw1htpbH%2FDcd%2BtYrd4Y0krlJjT4Y0XTmZA7%2F3uV2nOSfKlikJkesDdIetgeQiVHG%2FNXjSM6xdMnx1IH41Tq9o4kNYo0YTRuNQxk6aEp8Ezcod%2B%2B9QB9JNyQpSfj05Ksn0%2F8%2FBgbgiIRx85di%2F%2BpkWu8qSQ3XmNGP6AcItvpPUY4SqQqHHRmxzXouiV0Fj1BRp2gJfhDST3c50RLCL0sPLKF5pWPUlh%2Ft8MIeGSHj6y9ueGWT0XtrbAV72iVJbIKxax192AZOyG8bISx1sEEzwcAY35AmB9WmImTUx6AY3yFEZ0Efu%2BjCRpPS8BjqkAZK5TZdBrbw5FVAzWVG7Yry%2BLmsoxm3OqzzbDTd07RX2JJTB%2FK4fPGwPJqc4NPWQKKPQQDJuCfqW6NzAadoFvlwJhIwcN1JMbk%2FIPVtjpt3wqJSN9dlXqMogQKmpUjCRXmEBz1u6waZ5MTdAsHA6veYMqr7peDjJcV1uWIBq93z52rbPaHSkZ3oPa6Ovwyq2rDqFDLyX5BQTPkcndSfMGXTslQcB&X-Amz-Signature=b715d64299385fcd34f97a07ed943bc64bcd4e83e0a8cce50fbed2b7cae053a2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQVDTL3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICbVWq%2F0Q10jXAfmu8c83%2FiFdNzs1H8BArf29G2dSmjWAiEA%2FROZPwMWcy335CCQKQJCZQ12Cpor1Jsrmeibzp2m12gqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiFzEq4eoz3xR%2FEWyrcA1VquYmFwao%2FZTJbqXmHY9t8FciSRJIyJffRI98nou7jFwdOHDk20wJzh19nK9ioJfMRfW0QaSD7VW4h4QH401vWYeBIpcJab5pR4dJLZW%2BDH90eZYInAkZSKkyZycbzcLjQXVQawNj9y2%2BWoRSJqi9K9Rlola0U6ZN3CMcFPqHyTFXdzEri1GOAPLvOq0IdEBiJ5O7QPHFYNLsBZn9fl9tKzTwu9pLrz6NoPg97nZSZZX7q2iAM9vsGshOzY4Akpinuwt4NxabLRuzhyWMthrZQZU8i3JMT51QT%2BFfhmnx%2B4Vmn7F%2B9DHY563bPw51T80oTOyH7%2FtjiFnjb4p2JFnSKswqzXzaOrxbIrY966N%2FH30sEEI1CnONJTRrwERH7oO9o2TFpAao6YExUn1GJwHdf%2FnadcQpsWNxPBRY9OCNYuQSFxMSAtmvsNY1haimREMYz9tCYQou1HM52F1DxWHqr4%2BR73EpDwxEmu3acExud%2BOuv3bCV%2Fqtiac5iMBY6HQ8hNjCM7cs2%2BZ4Fqj%2BVgmGn0klIf59cDCVeYXI%2BpWe1Du0mMXBq%2BRXdF%2BTYn1VAtfu8l%2FObyJaAPYqyvHZPC4yl9xrBdOSEenmmvyYlb0dy4i1a78yR0IkspphGMMej9LwGOqUB%2B%2BQHK%2BU8a8TfVt8P4b0bR8SShU7UQmbca7qqjaGoGkW4R6aDEaH%2BiJq67eRHx5RloKPMVZNx9QLDCxmSjSjpLQnuDGRigisYLTSwFQTP6wFWJvgWPMTXTodZNoOcz48olQJqh28sNs3HinR5DDUm16OWGVXY8WqMWlrb1eUzVfl%2Bg5xT60q%2BrsPOZ2xl3omcKggCtWZfKg06RQe2vjkBgxM8eyHF&X-Amz-Signature=50c359aae3aaf10bb01112e3eb06280bdb154c9246578e81498aabd91c0a1e8e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627Q72RPT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBf4doei%2FNbZEr4obgtvcoxldXimaH3GZoaEC0SNqgrcAiEA1v32jdkCqs3uQwwfT3BrYx5bvb2H5ovFwmLCrC1XMtsqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFv1ALP5l1LIyVDJLCrcA5skVH6Cs8KckNUwAko4j93icj0cSoG8CiRXEp87KXfQp5fwpCUJweyTdmcGFXT3YK74G8HmSlKQrL1GRAsrUwjPZWdpwGwWMcX%2FN9oBwoxbPn373JDUXqrVhDZVR28Xps3Xyj%2BgOAgHn9Oy33O5PP6olXCjVCCMRJ%2Bwd6VphoMtER%2FphrDy8LvO4N71G3XO%2By5Dl3tJxkO%2FO06Ja11gMrtuPudRaTCLlQlluvzn0o3Wy4lwuLfd68gB042FWmVU%2Fr6YsZx16fDpxzesUqT6%2F4h2E8UCvtBlQUMJqCJxa7pAI1gycDvdckklixT%2BT2hyyKgQoYbqdYvNyHLkN6Ln9GBUZi9Xqkor%2BoUDVrBbWCvcnEPvO7hBwqgbn%2Bx45ste2qjbyPxtXecN7etc0lQ1UeDuoUS1VJ%2FLSR5O8XkwmlhRpCjy55gWd4EYzloimIuyWwOhZNjbj3TYElBSVK0i2Y7F5yjc0OwEdzxR8AVfNDBYxcBZIuzUSj6X6txH1wuPL3zGGwvhtthshpODTd2tKc2wVIWI3qbrCUv5w%2FKKEYeJ4%2F7YSSEV4yt7YW5CT77huxkNT%2BF%2BZYqN1aDx5%2FaKi3vDqcp64Tew6airU7gea6H5eSaJjBIcndHe2wL3MOOj9LwGOqUBUqoXV9l5McIrLvAJRqiIU3UlWIerKhKdaSpYCz4%2BhEcTMkB3b%2BnZCoSuKqQjgdtQHBbXwb4oKN%2BFldnXKuS9FElFeYAfISJ%2FbsQYo%2FfZccSCBukaKWU14nqJImlhzl0onSQmmszO%2FwqAP0F8Vx63ch14I4txEjShiqa9YF%2B2kosIL1RrhpruSBFLPCf5SHYpx4jnX2BkjpKIQxuERRhKw1pCqMEh&X-Amz-Signature=b314b4df6f0d6bf52832e1758a9c11b9089201746228a3e39ecff5ea6bf61acd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HZQDKBQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9NbuL3i4e1eQaphtIfvUoXalhkOqVjmq8W3mi8zruUQIhAPsYV9xAwlRnIJ0sE7e8NaZRTDe4WYf4rtOphB1kmZjNKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxnR3HgP2%2F95oUkZx0q3AMExQHRiSL9PJrzyidSVMjK1m3jcLXdMXteGgk%2BAaYaj7%2F7zFrWU3o%2FaEaeEaG23dmtcXkIO%2FRCehOl%2BLimrm9jZTnV1%2BOdhZr22Y7Uku1xEB8RSL7FybxybGHorHYi%2BGFwAX%2FbsN2n9HcZERGnhQcLF8ncGB52fe7mIEqoX%2FjJ2VMHs6f7ok%2FbXP04TgLVvyYzEy%2B1YaydBk%2BoQ4ZmuqONokaZPwp47R5LigNV9m9jFRq6%2Fl8qLnpABtOZWN%2BBA%2FQcU1B%2B7QYg49nsZkibkaP0Brm30QZ2JamlKxUkKX0L4O7ewYHCbnETKimWWWxgnjcHpXbgfuF68XX7tHXRyEuC%2BFBwUCzEz8xBBBIFXeYyFy5NuvSit0dpM9r%2BsOyOuEFtAoteVPvyE8QLFgZk7WwoXVZt8EBBXRkXakdiBJOuR38BdXNOlZ1kCZkXsaqPILrazrtf2zMctc1hA0cTtibF6zZVPMBnKWVwkcPKcsag8g8Oea%2B5IMRKBB4Hr9%2B%2FqGU0pFxAPmMTAMIKQ9g45JRo8sNzvY%2FnkmimM2D8n2fR%2B%2FYbCpd1gAKz6R6Xo81iHhEO20XrPbeBr3kIA%2BfIa2ETZToZ4I52zwBl1T2SqfTiAz%2FiyeTodSYLTwm5mTD4o%2FS8BjqkASWfPtHyV07FAWWHjqZEI8pU2YhEqPBwKAoO3AN2cnw%2BAPCxZvtQePdGfQi7Ilx3npG2UReQ0YRzTTEOfJL%2BQFZt6qcyZk%2FefQNI5QrSiNahtJ5F8PWtP6CxlCWXcYA8j7OAPbi6uVBiVfrCDjL8h2DyKU2YPxBqh6SZitOZV3vQQrKmjARdBpSoJRyec13vMvayyfFHR1BhCoSXPj5xlIIVoL73&X-Amz-Signature=59512a5c0e841c5555395eec2f043391065a0d575cccdfe5cf4180628d426343&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLYYFWC4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBIuzy0smAN1ZTu1a8f4sw3rbjtH24tgYQaMXUWz3uwQIhAKzweND9ALenKI6fXDHO5hL92FsbDhLV%2B3nURS2LDlsUKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxp%2BnkHHOsGYH7LS2Iq3APxI7Qd00Vqk8lLppNKQgixL4wGyykqyT5mNQPYzUyhWP5FBifAfTwWPee6nxOh3E%2BVgRtHA9BZbS0mJeehQYkYrUUUDsLr1%2F%2BoBAlkErLLv4VjxNZPkxYmHaY2e%2FhYD4RF5UHZ4CMmbFiphFBi3vk5I85ATHbLj8daTDNYlzxvZGQqqIRk1d0Do%2F8QIsh%2BnSLFqPmw%2BCv%2FvFksb7t6ZWaqqwcUa8gWqR%2FNKZqVZtvF2hOqrvFMRCzxPx83f0JQApmrc0yWaswiGgWoafJTmpgcRV8XeFimg%2BCVbAbHLY1nq1dRnSVU7iIvyMQF%2FdM42kOCxdnGRqsrHEy%2FTtVsrJIqOR%2FuQovr0v4M%2BOONiwd4nTKm6eJqWSTlOGe4Ek3gGmlhUGoFXQbwOvr%2Bz96e%2FNZJPBhGci47G8utzv1VJiiK5%2FpdrKhG%2BgfhcxiU3QyY7X6tpiyelPMbWgE2sTcvkmQcg7goVsJHmpgSFsjeC35Cd7KwtdBoUCvv9LpoXAE3GSbkuReqsxN%2FnPVOhIX%2Bl0GMiEUal8srU27Fa5Q06V%2FxdIxbWnuPMjC1jl37c9eqyjfzln1LfuO6O7afw%2FtuXKJ3Z5hhjeGkyMKu2kNhXeDcjbmqAlTovPLej2cRxDDbo%2FS8BjqkAWgeVGtWDy445Y%2BaNcAH3jHyszvNQAqOT2WoQhcgvOuKziX4GkJnMhq8ruAKygGj%2FoPpWxPyVjkB3%2F9QgDBIgQ114rRZxkx1sp%2BzDVvCC6VfOXY36HGV1xPHhDnQBVBWYKQNLsfnxIFoZ1zKQlUV742ljsGPg%2BUIr4Mma5SxsoZoWbJn%2FYAq0kh55DTXSL%2FFokcoITQpAY%2FujDeaq7t9nm5XwZQU&X-Amz-Signature=b6519a77df6b9823473b959128a0c0175a05304ffd1ad10636ca082dc126f747&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD44FVZ6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF6C6agbotWHBaQMCFibN5nIoLUXxzB%2BOZzmmz1%2FeezrAiEAr1ovq7yExcrWaehxGZbOH7a3YbNNzUsL1AWThfsI1H4qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNkep64DKTjfvk0znircA%2FvGCH3TZMu0mqqFotnKQsozE9VSZzztbtHKCPxW41jS051DAZke5YTexFTYZFQNDPx%2BiHIV7DuMsqHGgfGcPdO1YObq1jK0EvaTcXW7U7Z0a8zSOFEory7wR4wOH%2BxgUHXWg8hzIFFIS99kUAxbVDcjd%2FtKx1QvbdE2LaWRfwimu%2BKn%2FJAbsDSgCOQBWRK0gt8qJJaq2ngzNuncCIpGimlf1PJ5jk2zwAKYscSzzxRNXC5BYihNV0YTAHJ0o1B6r1d6EjnZNyS2hZnyKt0nw3bz2757pMrC79sxy9xl3f99d895l4yJdu9EQ2k8f6soogDLr3EHy2BPXoMMTfbt5hLoyg5OD%2F9%2FU2ZjOqCi7uHFjT1J2Irsqc0toiUJVoqzjdJJFMm3d%2FSfWhXok7O3itUtTHO427v1ovi%2BmSpn8axbAbfrlojQZuxMQxwa7Iy5TUVokuqIXcpXuA5kROo%2BE%2F0EMwJFLHGKu4506J%2FSZJBJtJF5mKwd5vhiLtC%2Fmjy8YnQn04YcpIKxBTl199l9DW0qYW77YTMlIPY2LwaJ0T7PP1DLGG6lR46M1hRONp9IfwmjBauwnCaIVJwqvSLmzHfftECnRssOmjY1v%2FDylqoEjGXiweLM9iOnU602MJGk9LwGOqUB1JtiF9KxQRCUrho3N0ZVEJTwlJ%2Fc8MQ5T2s6zq2JbTPd6GhA23CmDrxV3zhwaY89p0dq%2BDnmrNKcfXL%2FYFEe0EG0WrOj%2FfYfouGvTVxZ9kboGI21QhQ7LKb7kysMF4Tt1D%2B2XtFHww2wHM%2F0LmtMj7EwhdGjyvnZhhGsDKkWmjHZVWenCEQHpGfmibTqR4abKuaVguZE0vvSizwfMxZS4sT1NCLN&X-Amz-Signature=61a895a51a4a930eae4580e998e58ef0b8afec049adff24ed74bb1a9b50d5276&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BSEICBP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA4cnz9XJMxNyF8hNdxNeFnod1sfoMvOOiFte8qxGia2AiAT34v%2BaUZyIe21W3%2B983eNL21F1edsd5AUPN4vnxI8CSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaGqfw00aTcEnC4wkKtwDXfGQN%2BKpsmYa3y9kKEr6aUxmj45wlopLG6IFg2anXy9B7jtg7aJaor0VZ%2FLDCWiJkFkrtOuzzruX7mBdUXCvLkEolp8pkQIQtxH1mexBkCi2OofCQ%2BL4%2By3kTzHRxqDqqKtrlxxxa4QNtmq04tvtTUu5hgT7e5xMHQCiVH0Uo6%2F5RjeTN4bGfQUZ5yHXwiwz6mua7WiGI4WpH6RvUXChVcKZagyFrsaZ24Z77IC2mFeAIHiHx9tYpA5N1eRTiQklJ3sioli2TCI4Tiibe93U5qU5xXnZK8sBEm%2BZUUbcEI8JkmQW2pM6FY1yk1oRFwHPQEXLk6A0XOEAQ7iy9r5wZ93BBQpBXwmEBsc5WdLlCPd6CNl4Sm5bn3aByqDQdJdgobNEI%2Bp6HloYY5b6iqV5uRPGfQrIXbds0iaZKxVmWRJcxEIUl3zyng3oJIpUBUerldSjUxmyG1cjV7KHpDEogOZdcBlPYiVvz%2FtQcsBE8BOjfrTAFX63dAaggGGMEz3wr8K3qcrgwW8VOqMqo2nwo5pAasXwAhHAEmsnjwMmxlxTw45xaMf2POQhUmiztEo7TeSe6ObjxVvcweBLslu5s9lAZxathF8pLjG0XJ9VVvBntoOdUOSeSqTP3q4w%2B6P0vAY6pgFM8i5qWwRj0UM6ZcYKRw0o25FpDfO79V0DvBztnxoSWVMU55bh1uVfZrtRgTCCYBrROQtC0vII6La54UhBMo4fWyundsP4bW7z1z%2FphVVbU1PdSYy0Y9wJI2oyBaUKlwBod%2F6NqLOjt9opiOgPkhkQFmBT494xxnq1LiJlJNNUM6UOZD9%2BtYwKhJPE%2FBvAlFz2anDDTp%2FgDdKOje0llaz83xuc9sW6&X-Amz-Signature=8d1c73bf29be620ada8a838114f1d2db65001e1f457ed2dc94fb511733a7c2e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HZQDKBQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9NbuL3i4e1eQaphtIfvUoXalhkOqVjmq8W3mi8zruUQIhAPsYV9xAwlRnIJ0sE7e8NaZRTDe4WYf4rtOphB1kmZjNKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxnR3HgP2%2F95oUkZx0q3AMExQHRiSL9PJrzyidSVMjK1m3jcLXdMXteGgk%2BAaYaj7%2F7zFrWU3o%2FaEaeEaG23dmtcXkIO%2FRCehOl%2BLimrm9jZTnV1%2BOdhZr22Y7Uku1xEB8RSL7FybxybGHorHYi%2BGFwAX%2FbsN2n9HcZERGnhQcLF8ncGB52fe7mIEqoX%2FjJ2VMHs6f7ok%2FbXP04TgLVvyYzEy%2B1YaydBk%2BoQ4ZmuqONokaZPwp47R5LigNV9m9jFRq6%2Fl8qLnpABtOZWN%2BBA%2FQcU1B%2B7QYg49nsZkibkaP0Brm30QZ2JamlKxUkKX0L4O7ewYHCbnETKimWWWxgnjcHpXbgfuF68XX7tHXRyEuC%2BFBwUCzEz8xBBBIFXeYyFy5NuvSit0dpM9r%2BsOyOuEFtAoteVPvyE8QLFgZk7WwoXVZt8EBBXRkXakdiBJOuR38BdXNOlZ1kCZkXsaqPILrazrtf2zMctc1hA0cTtibF6zZVPMBnKWVwkcPKcsag8g8Oea%2B5IMRKBB4Hr9%2B%2FqGU0pFxAPmMTAMIKQ9g45JRo8sNzvY%2FnkmimM2D8n2fR%2B%2FYbCpd1gAKz6R6Xo81iHhEO20XrPbeBr3kIA%2BfIa2ETZToZ4I52zwBl1T2SqfTiAz%2FiyeTodSYLTwm5mTD4o%2FS8BjqkASWfPtHyV07FAWWHjqZEI8pU2YhEqPBwKAoO3AN2cnw%2BAPCxZvtQePdGfQi7Ilx3npG2UReQ0YRzTTEOfJL%2BQFZt6qcyZk%2FefQNI5QrSiNahtJ5F8PWtP6CxlCWXcYA8j7OAPbi6uVBiVfrCDjL8h2DyKU2YPxBqh6SZitOZV3vQQrKmjARdBpSoJRyec13vMvayyfFHR1BhCoSXPj5xlIIVoL73&X-Amz-Signature=d4a668497a5a2898f1b091aa8ef746528c8846c9727d567410dd69b7be2265be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZO2AUUSW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4w%2BUpWFQmvX%2BEFItqbDINYNXmZF2%2FVCHHUGqu2WwZcgIgUJEqN68SuVPTZAuSUx0rRve7DAM6uKMEZqb%2FSb69m6oqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHwocfKgwgYZl%2BwpZircAy%2FHyR6XRP5xg2GeWYxwOxoJWkiXZ4ty6frGG3dRYkemGLgjogniIfzZ2fw4ctfGuM7RucewTQz8pJCI%2Ff%2B1Nwso9xkTY5P8O%2BJBBuV77lDnvZyl5kFE2SwyxBS8ktdfAgVNEW2uaGbaohsKHwgT5jQ28WNlzYkR9CIotWIWtqrkKeVobcmBCkv0YbvCWpWx9zIX6L5%2F7fH8RZ0PHtWZsPkwEf48%2FhD9%2FftgUtfXuxY6YvTQHmGaFLa5PRZGA35JDbRw5iGAmWskxu2weFpr32JTT%2Ba6lRxjt40AgN5l%2BOZ5bpkDW8V4Rz1PFyOz8K5U%2B5krtXV5d2b7WMqyg5JdASKzK2UmRkb8M818p5kqxsAAzD0iTvat1dAD%2Fx1m4LNO6X0qwngp%2Fhi98g1G9rjTuCjNfmLXEFRqUkcuPKMwsVdWJb7A46aGxb6gPpVwBItQ%2FsZaY5RXA4a7KVWQcaZosh5wEboztiCRmxnp32fZ6IukeNnTVCh1lJbheKwalD16eEtWeZb8rC6jG%2FFtFH4TGw6uJaGEgiHXYdWzwKkyULWwJhypSVG8KTpQi9w0dDauyNROccB%2BWa1tVVUWwGQPc1NB4Qhulngk9B2fCTuoN9NY%2FrV6RkJN9%2BycHPiKMKyk9LwGOqUBFDcgynhkHNyAQRc1pJimFbdWNCnEqfsg1ZwC1mOXYgZdwLMgUmipOgtF%2FQe7%2FwhDTtOZKewj4NVimDenEs660Cg8U%2B0IWAN3Ubz1nzTk2iNJmEYjUmy0YlJD5Z5XSzEF5ep%2FC55IHBxRuqJn5stq7ExZtg9NprD8GZxZXrRYkiZst9xW7mmmSEQgS2Z5Wv3x51CjH927JucrICDzTx9fZjMCRHJK&X-Amz-Signature=4f65abbf25f15178a3981667e9783b42ef4bf45f01ae210c7840bf15a10a2220&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZO2AUUSW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4w%2BUpWFQmvX%2BEFItqbDINYNXmZF2%2FVCHHUGqu2WwZcgIgUJEqN68SuVPTZAuSUx0rRve7DAM6uKMEZqb%2FSb69m6oqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHwocfKgwgYZl%2BwpZircAy%2FHyR6XRP5xg2GeWYxwOxoJWkiXZ4ty6frGG3dRYkemGLgjogniIfzZ2fw4ctfGuM7RucewTQz8pJCI%2Ff%2B1Nwso9xkTY5P8O%2BJBBuV77lDnvZyl5kFE2SwyxBS8ktdfAgVNEW2uaGbaohsKHwgT5jQ28WNlzYkR9CIotWIWtqrkKeVobcmBCkv0YbvCWpWx9zIX6L5%2F7fH8RZ0PHtWZsPkwEf48%2FhD9%2FftgUtfXuxY6YvTQHmGaFLa5PRZGA35JDbRw5iGAmWskxu2weFpr32JTT%2Ba6lRxjt40AgN5l%2BOZ5bpkDW8V4Rz1PFyOz8K5U%2B5krtXV5d2b7WMqyg5JdASKzK2UmRkb8M818p5kqxsAAzD0iTvat1dAD%2Fx1m4LNO6X0qwngp%2Fhi98g1G9rjTuCjNfmLXEFRqUkcuPKMwsVdWJb7A46aGxb6gPpVwBItQ%2FsZaY5RXA4a7KVWQcaZosh5wEboztiCRmxnp32fZ6IukeNnTVCh1lJbheKwalD16eEtWeZb8rC6jG%2FFtFH4TGw6uJaGEgiHXYdWzwKkyULWwJhypSVG8KTpQi9w0dDauyNROccB%2BWa1tVVUWwGQPc1NB4Qhulngk9B2fCTuoN9NY%2FrV6RkJN9%2BycHPiKMKyk9LwGOqUBFDcgynhkHNyAQRc1pJimFbdWNCnEqfsg1ZwC1mOXYgZdwLMgUmipOgtF%2FQe7%2FwhDTtOZKewj4NVimDenEs660Cg8U%2B0IWAN3Ubz1nzTk2iNJmEYjUmy0YlJD5Z5XSzEF5ep%2FC55IHBxRuqJn5stq7ExZtg9NprD8GZxZXrRYkiZst9xW7mmmSEQgS2Z5Wv3x51CjH927JucrICDzTx9fZjMCRHJK&X-Amz-Signature=ab15f2e1634b875f2cad529d3d876dcecf2468a3f7708d72dbeb36b39e5b2db8&X-Amz-SignedHeaders=host&x-id=GetObject)
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