

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DNFU2ET%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAaSgf%2FazPLbAQll5KxA%2F%2BNVYofbuxVZNSXbUebF73mWAiBA6XmIqsAul%2BplrroAd7ZILIXFgXOD3w4Qrzrhtk3OxSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2p8Xlm1F7Fl1%2B5C%2BKtwDCJpoRAG2gfIFsqabgCufVRKvaYtApi3A19v2g2LuA0nL02nvigD4VOhTP%2BwooUkk5z92cIJyuWDTk%2B3KLWhgEKq1A9QKZrzCI%2FQhvQlDxW3jzStUkIuX4CswQPVUlIHvshcNycoZ8ARGH5vVcomKE2cE9NCCStEiJGH777HEXOpYbikUrCxvpyQ5y0FE7RYr3Y%2F8Bbqh11aGuAlMONZ09XaMny8IA3gtxwAXFNh1gXKTPZqn4HZbZ8SksZH%2BLmG1%2BOiq0ftm%2FLzxnQvVNHnBMdzpJ8Jzrrg15nHg8Cq%2BANLeRX%2BuMLFGTEYpiEQNZhtKqaLq3CxMmk%2F9nAUOCoSPDkLXJ0AtBMEpPupknhmm7E1n%2BBcwifG8iwF%2BdXWjorfCM3lak%2Fy3t64yf4fyffSqurNIZwdT0qnVSQEWJY3udksVRW8RwivCHxxnBa0xl9om2CJ7pKmxhQ1pL7BSXTVVLVi6TUnIpTQ7rUlIUwHys93pDeYtPkWAlY8IY7%2Fy5vKdHWmROz%2FxjnD%2F7ONJtec2n91KlfyV7O8m3gmNf7tAXJFF1Goxv0P52CJR%2FGvGMCAhQ%2FKUTsX%2BbccXWdpeqkL2fgkR%2BN4nzor%2BP8o%2FekrP4rxvyUoHElStfD8LaxMw097%2BvAY6pgFDnKhiWq3muYwqDdxdJdbO%2BrIVob8D1jN%2BSTCSCyVGxPJ1p%2FABk1LFKkS294gzQhXtPEBtv34nAiPDgyu0eiprNc%2Bjzgrgavp5xxiMdVtQmKkEj%2BRjK3sQWbLzKNX7ThXXn1LIPIuiNyLoufLdiUQdfw0RpJWP6%2B5VliIRPOFrXAlU9XcJRT0mHGhGBl%2BFBFGAANbkfbpS512hfm0DsUZgMm%2FqLTjS&X-Amz-Signature=47bf1f81b01ff55b00226a30edd38e478fb02b8ea83fba3b79d16416a40cda8c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPHVSL2M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGzhu6guMiur%2FM4vTMkh5RiY5JGkK1oYVxw0nYhhkMZOAiEA9fut4fEx32wxVAbO5W9RuR6mJYu4baKYG6fJ%2BMJd%2FewqiAQI9v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLotWuK%2FwkUrOHtvGircAxxc4kFZeGtZrDTlccE5ZH6RwXNXcfU%2BSlvc3MPHdO%2F4j1Sdxg7tRvm40xypmeNoHDZ39cCjjiExLe4nD6TYOh7axF2vXTTPnXk0QhR16gt2%2F1HPYTkJpdBVJJUTCnj33ubzKdBz6xo3n%2F2z6z6FBU6sAdII3I3%2FSnz%2B4EOutCLo7qVhezDCfGncLKtXKwIlADLS404eWR8NwtOa%2BB0ATj0FNGgNOdPED4bVidrrQLQdmkx4UWzbJAzW6vcB3WkH%2BRS914s9cgDlSvBUReuV3LVa4KQuoT50u6fJG8NZ8B0%2FPM1ASbYCNVZwW083%2FFhxdpOvQ3pbZ3bBvFImADlK3StPHgFjqoS2RNd5dGQqQJC1kZiwMRd5KIKekLxfw%2F1QauUBL%2FSWFSkkCfd%2FY3l9DaPLcd3HIeERm%2F49BDEZuHMvuysnsBYBUBtPCWk%2FqTBK0UHNT0YFgFABGxfQTS6NRjUctHpN6DUnwc0tfzKengfFEVK7r%2BOtLX7iG%2F1MEj1cst1OnTE8PwJRJ5CoxpgWd7pJkwJFbVw9ptywIfSc7N7BSbpR7w%2Bb2HqEB0%2Fc5xQp9yuVTA9%2BJYvpujsM%2B0xhnHfnaDIsy29SoppX3DGHwBeIdxa8dRXbMfMLuHIfMOux%2F7wGOqUBzIoS5NBmcUz7fM1egW3G8vAbqwQjZEqCMPyA9AXfta82Y%2FSZAqy%2BXft1yK1NgNxOYmTYr6EfHd0DEiH5muLaahEMyYIVJILe9Dm7YhEJ4hRy91wYqstJCurC5WuKrDn6U3oBB%2FUQA1U6khNRx2NsDn37zp4%2BJOEB4ODNCsJ2ZXXQ3raaot1VFcu5zcGyAjU6wbho%2BJKXzRY7dBxkBZJDJL7ptnAv&X-Amz-Signature=4207495eca6c0efd16a788d3663b6c1bbb59195b84f1f24dc13ba05608430ab5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIVDMBRA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcSbACiA5J8jBX9EXiNX9LudX26t8RlqWkwfOStpXGsAiBs7FghQsJFQBdyOfkKoYjay63SvqtfHxt4jbhlKdKZkSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjHx%2FJgMIuBwaGr5AKtwDPB%2Bls1E%2BEer9IcjrNkenfIX8UypCetDt8Kk16d02sQN%2Bnu30gK8NW75GC4bl%2B6L2Yk5xAW6a4M4Z0IgtPidRkZiHhCmyyVtihizbYSLuOWHtkRNjnyzqdj0mOlpRaSWUtqF4WhQJ0chx180tKP0mNhLHECmJ9sJG62ZystO3yrWIOsbVPppD7JYswelcTJD74Hw0L5aG3enI7BGY2ymlvcMjGpyCXpuhBOy%2FDfQbaCQZyeJfWHuVuulXFG0dkeAIKvEeA5b7JLUtMRYkRVs20DyfDZSdSG%2BrW9ucB896pHRFArZMD1YHk2u3U8ZqNCev4NctCGgCN1uObGlfnSnbglz4zzrmQIc6va%2Bs0VPnDuyD2%2Fxpk5YH7%2BGUifIK0PPLEOIGeif%2Brhp5ay3EpXudnA9nwbmDI6Y%2Fj2bcsLC2yolEQhLknDUW8%2BK0o9%2FU%2FO2AmLuyIESBDNgTeRjwheL8iTP1ZHEV%2FE2UmTrcv3f3shp0VWAhtG%2FzJd67nCwMuCd7a8VVWjLcXH4%2Fe3Ir5%2F%2F65KBIw8ALSVY60EQiBxCJF4yCMYvgjbyJT5yv%2FF0bgWicOrgh8pX%2Fh9bMsDyqh5eRZXkc3Dch8CKqm%2BbRfA8SYQBp72jHikqY85J53Qow9uH%2BvAY6pgHLhXBksUpgKU8wuReL4hGXWMtqNoBBWb%2BD0AJufJoI2P2f1IVFyY5MTRG8HlJguF03UwaKzDhaudbz3cZ5awc3%2FrJXsYyiOyU2XxrGvkghBjMvJP7KlczZWjAZ6%2F3n1dkNixBb%2BK1dJkyNYAY0NXb0errg5mvSjP1%2FcMacc2FEA4h0YCle6qdsf3zcOt1TmLgDtA2TuYEAaf6RjhWsmQz7QW3VkiDX&X-Amz-Signature=c237fa7c95a6dd6c4fcdc807d29eb1b047b405e25a69ad4d86741121afb63d2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMTJIGE3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDqeNqRB2wY0GQfGNeZkbZBSuU8egU1Jnm9NhaTZUvVNAiBiHZ5eZxSAtSZtL1C8XcV1lmTOu7tbXmkt3uMs%2FQ3QhSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Bt1cV%2BQvhjgoTFQ0KtwDZnLNbjv0rt2ooKK4QasBwG6enp2LiLK0wP1%2BX6w4N%2BjYEQA9nakphYOF%2FJ8IrWPXyuu4d3QJj6%2Fvko31%2FQI5jUXKmVfsAROjmXObqxM94Vk0gWkEVJVyGdsGG4wzdl29gSP6rhYcdcs6cgHVCkjFNwaobdVSlPuusUnf94ZkaoON84VO8lkq5MGsyFffqNy%2Byf1%2BOEI7U7mVxOnppnUPqDgWm7p%2BD54iv%2BEFFCJZ6MBJND1VeHylwjI2poPThoTj%2FnuTNFfCAHIqxNOyk5vIANmFI94%2FnUwo3DIPaj5k2%2BGLZHZEJljg5ZqaNOldXRdkqnCQ7WNEGXBSW%2BMl%2B9GiQiClqB0AAwSWwhdjjcfsV9pMOl2L%2Fu22llheSf%2BbSLCgKsTbAx0%2BuH9trBoW4TnbO9ZCfCehx2FL0tbPAKw6EQ9oUL6zYgI3xjyAGKfJwvjV6VJalIcwySzpWFIDU89q5i6a7q1e0Uy8nfSwERvTz1I2qGse85Xsbfy08rx731xsY8Lv7Hrda%2F0tOFcOlxsqK6gRN0Ps4Z2FDoERMK5bs34pEHO5uU8msyLoEasE5Wn0hLXgq5GQwy6W3tnLED8EpqJMhKQI0ge8HwiFnQ8rurnPtQDWPcQokOMkB8owq9z%2BvAY6pgGWhMUPXLtBY3vt%2FfzffhGqZhh0xB9QWeytgu5NwW4%2FxAXvAkCO5VxNFLqbWA3wMoidj2KMTGauMZaxZSdTmTkZmHeNvrPwqBVIEDqm56jvZM6%2FGXPhFdxhRY6Bdh72tTjTFCqAHIvuNzN%2BNRqEK%2BOifj8hhLn9vGl%2F9vPBsfS0C3UhLYhd9Tz%2B0DzjaqkaRbqewOiQRqwAebYI5y2otWMzsR919rBe&X-Amz-Signature=cab666623e5d440e06c650e49f5e0e4269b611d0f335216c0bfbb7aa682f08db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4WO7O7G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE1dDtOy%2B%2BKeiVz7hJwCjvaHW%2Fw6ACpvtHKkz9RfJvpgIhAO0VaWGHVNb8ekhY53v0DKuxPA6RIZu1ptFVz%2Fs1q7EIKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwX%2Bv39camNEmqRy4Qq3AO2EO%2B%2BN45Iqen%2B2S113urKbdEvynIkWU5yZs2rGvoz8eVEu5znIy8pAnhsiVXWwjmcOXna7qUaKcihLh7NsV%2BIM757%2BVLqg0vn4E8INY0wv5264GKh%2Fon09NQw63eO9VzoKahXTtHEuTlwvicbqbM7jWZqTODakPL%2Bj7lCAUu5xf0sS7TpIJ2kxnCtF3Kr17HAW%2F9O2altIgXdXWJVJvcooPgTgcT9tXWJGvDIjUgewjanjcFhtwEJGVJzyE1uTCpIXf96hlgaZk583uzVLfGCup3NcZhB2jxH%2FdXGucKKNuyKNag13dXcaXxOc7YI%2BukGJpgcVPwNuhrBQBUn1IK27s%2FGj%2B%2BhP3Fjd3PYTbusVmuHK%2BhSniI6lfMTGoo0eVVwQYQ6FZm7QH14gBcXR9VqsOMAwB9TnfW%2BsnRIItXtgxWXHPLcW7ooKoqYSMxTTby%2FarDOzx6ZOl%2B5vgV8jY67bi1wuVNwUs45kXUqhsl9OH5YwwZ4%2BF6t44xtZh%2BL4DPC2swk6SmHmSvuoEe33osWbmLcl0ErzLhzhe%2Btx%2BkRiJBNMXOs7UEeO9rf8NBdqwm48pa%2BsqMOnEhJGLU5ETdcczykilfYNEu1W9bMOR0paKiOSaW6x%2FkLxA1zfDDQ3f68BjqkAYQgRsX5hGEOJe2orSoKyh3PTzsdKnmuclJzFCO7x7fpY1%2Bg4yvn1MJ3%2B6%2Fa%2Bgu%2BqRsJ%2BL46K2QbhyZqCOTXYrnAPCF9Vsy2FrXT9dbRznF0vvb7oEiNlOWF%2BXzyc%2Fa%2BM8dHFZyIs0g08PqI69LzwrSDwWSPnyjSGfrVVd8fuiLCE0sb0d2z7LdClD6OJ4LWSSPHlET8F4cvGEJP6E2LPyeQ0Lk6&X-Amz-Signature=55af811154c6db63008cf5d7c9a824104b8a3695af0177ba688ad93ff5b6dbb1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RE6TBRCX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGMA5wly2FwzM1o7pr8kDRCbuyeqXN1VymRHAgrhjSCCAiEAqIZjT%2F6vWZ1j3%2Flb2D0WfPeFx1GveJv%2Fr6YseTi9FToqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHiwdqIvQXeiox6mBircA3fQG0EVwwysIn6tezYyOHqDIbAkiJ9pskBzFDwiqj5eKimPVIF4vLxaieGza3K1s0etBo1WPakwq3Cwy%2B8%2BSqxd2h9NpclvZpCCxUhBR615sjkKl0mMlCjbfehOaQNffJ02jm5EKhtKPldO8pBzK0Zbd3JZjQT6w5eDLbpbYPcETWOEyLFOMTUKFWBC6d9IwCczSJb%2BMl8hybCuFcSDq3q2210qTMCcD9vjwrvlmb1EDfvPBetKk7X%2FQsXnYSQAndhD5ZZHMOcZ%2B%2B2C57YWATugcN%2Ba5t%2F3riAvfTyL0hme7tT6jiHvHlsw813pqXdmubGXXxuA6aFVCjhTcw2s%2FtMufV%2B6YTXlEzOKEzFDcxVi4jMGDMXSdTklQsGYA1W2kWwIWX8FM4yQIjXLUg4TwGalr0z4oCl%2BaVrnIm1bfNtIYCtnULnDWMbUAhw3OQNe9oc4sE7oQItawM1kwLczZHb%2B9v8VtH5stJAPRaiVZ1I480g%2BGKgxNBvtyxaQ9PelxYwt4sKFEq0VvTMJCDKDLye%2BN6%2B72oZhRhYOdaUSeRfz6XruME9DYJDBwjRYtPpXDXA%2BCLKcMZVK%2Bl0xjkj%2FjBcCEwgAYPKA4NVLeyMOyKgooRmcZvDWLUOZ2j4gMLbk%2FrwGOqUBK6N6EYk%2BKyZD14tVbr%2Fw2EO79jvl0hLpLLPG%2B1lIe3g7pYd0Poid36igLTm0WAVBOgijp%2FNE5scHdiJXJus4ZpMp6dYczDvSOOiYN8crsWwTjx8iq5eckhfaE7ekj2%2FDQlB5%2FitKN4qRQnRa%2FnuzXIAz2S6PJiFuJFIjMyJGQmhlWaEulTUiggEFjPOq3LTbIx03w3sS2Aq%2FJQHiQBO7KDynh0nc&X-Amz-Signature=7f46e37806d2e497bbe4682352b6be4d9089d007eca63d85e67ef4978a0d81b3&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAYUBNCI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFiM2tcHAUKNH42zbUaWR4BugJAlbYNNnuouM%2FPiVOi0AiAp7wg0LBxWwDYR9h1gZ4Fse%2B%2BrT%2FsxlQGG55oGrIt6YiqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F6zxiAOYXkcvgUTYKtwDb7bx3mJLQijlv%2BJ2qAzmltOrE0RPkeAmhnv9YEb4%2FuqSSPjP3AX5wnHylaMULubLBEFPWwmLG%2FwDHpTm1qyvaKEACfJPu5WRGYc%2BWSmGVbjyuy4jDE7j4J06Sc6RDvmtnumaL%2FZ3SqPJFT9J6Ta%2B2WlaN6bl8s5wWHquhzYCJcByiEBpWqZvE62aFQkx2aG3byAlWWzlxOsD6KEYed0%2BEhL4b008opAScj3Qj3EBZOfqv%2B7lwyKNO00c%2FR237OD5lm0745yj2J3zlcBPqfVyUTxgmDcoRkLoXFUtUO7WeSy81%2F%2FK5EBh%2B4%2BP9BgjzXvT2N9Lpt1xMScd02XvH3qQj6saFNsoOygpi43zr3eD%2FdP7iSI8IqsspIMMiGLcnKXO0kXhW18Iu6ovMeg7H9H1W5WTO3%2F7bXaQRPqSwXlLJcZRhxQ5oFfzb7KoX%2FZsKFyxUpyZraJYjNrBt%2Ba64YczCxhh1AZQVFz4hER5YeaXALeQxYb9c57WnI1izZYpakZjRmm607QXKq6ZMKNoJg7p94rBCsVkS47SUBvIAASfw5nZ6AC4W8Y9hc5ybbXLlzrSeQgcB0KTF9VcAC41CAdQLf9w1kZRvshf8VnbgeJq8zqJl%2Fn3PXwSuf48iO0wq9z%2BvAY6pgFWzqkJ4z%2F6E1haYZ8rOmnhNLP72tr6WhwYD%2FVBfcSBk4unyn5Hs2kEl4ejNzPOftdLlKu%2F81%2FhuJD9m98cEZy0sUyomvS4oOPZx8wNTIt3j%2BnPCNlU9m2g9YyoL1prP2BiWDqlyNZvJOz1SncTB5qJpZBu8zE%2F5%2BgKg0mdXy3igSgwxLRDPJ8hcsI86n574MWyipSTFt7vLlZK0gwGufSS1BbFYnZV&X-Amz-Signature=238ebdef09c400384bae85b3c0e48813e2b04f9f47562dc6eee943f8763cc78d&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z47NDHGC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHewgCOHpG3RrrpKbgZRRC36ZRcO84N%2FW95bEGbPXpRpAiEAx%2F4ZPRJ3ZpsSsDafGCMKdhXrWt9EK0S3cYI4WjUJAtQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAAXuEskWSTsB5JkuCrcA7a7jeO2wU%2F5EaUYKZPvwxJeLcLI2pBYUbFUUStZ9ZKY5ugiZyH%2BXfAiYiwqwYbIN0vCz%2FsLOL3%2FSiE52CPpUzm1xIQABdbVLQVtS1xcML950x%2FoGZxNKQ%2B%2BbOBb%2FzhVtRuKdbRhevsYKvc%2Bwll2Yw81UPaFLpwmnIsZBYBWt8UwmiUzcz9EteWbIqvlDcUk6oKIZ%2FWqvOwGTzN6nsYZX17%2BBvkNZjkSmPXhdK6LEfluVj8m0a6T6KZ4M%2F2D%2F7lI5Mpu%2BEjHTnUzoWSdQrSwOOKZ6mJiC01chdF3c0WhLjdwIhR2O9tjRGrH65EdsLwNAiixOC61jjcCFCG2PeRMYMmfjB4D6naEYIb%2B4m%2FlPgyvFxFma89n1Ka82VkF1jFsiuBElvFCmRx%2FEDjwf86HddF7uJ%2BR8va%2BY%2BJCZegu%2BPXZwPoiOMlyKff8ojmqXdn3js%2FBnaNHc1G6GEMnxKoF%2BfeLRSozo%2FHPHJH%2F%2BlB%2F3%2FP9%2F4AGsAsJJZKO7MmQmeZls4pH1wi%2FxAvCT7Sq1Tq%2BKpul6i1Y2l9MAElJWEvNIBTQYT0ww2MwDbqEbBnqjpuMMCFag5i0vOOaogesaVDenBoG0Ak2QlLhJnmeamKJwUu7NM1eFwfAzp%2B6r9fiMKLj%2FrwGOqUBm1JmUgwxHEv%2Bilnoj6M1BFgO8xvGDn6p5XlhRIMZmWdzZTeViMb%2BTRGEQvPLF9xNlqGkBCLv5Ngvq2S%2B9QVSrFoCgUhLXwyTQPsg0bRpPUCQxTCQ0rdHpF2eFB6nyKXYSq2UZ7ogwp6aXnAVV0pZbaeUsZIeVsun4JHtuHuHbVgWa2bayXtFjN1W99Y9y4utqydAlYYKqxWcQ%2FMrz5oafqfvyIeq&X-Amz-Signature=8feeba55f3a69bfcc63b945c4a7e8c35e06f6e5d52f987b532ca5069abb18b7c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4WO7O7G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE1dDtOy%2B%2BKeiVz7hJwCjvaHW%2Fw6ACpvtHKkz9RfJvpgIhAO0VaWGHVNb8ekhY53v0DKuxPA6RIZu1ptFVz%2Fs1q7EIKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwX%2Bv39camNEmqRy4Qq3AO2EO%2B%2BN45Iqen%2B2S113urKbdEvynIkWU5yZs2rGvoz8eVEu5znIy8pAnhsiVXWwjmcOXna7qUaKcihLh7NsV%2BIM757%2BVLqg0vn4E8INY0wv5264GKh%2Fon09NQw63eO9VzoKahXTtHEuTlwvicbqbM7jWZqTODakPL%2Bj7lCAUu5xf0sS7TpIJ2kxnCtF3Kr17HAW%2F9O2altIgXdXWJVJvcooPgTgcT9tXWJGvDIjUgewjanjcFhtwEJGVJzyE1uTCpIXf96hlgaZk583uzVLfGCup3NcZhB2jxH%2FdXGucKKNuyKNag13dXcaXxOc7YI%2BukGJpgcVPwNuhrBQBUn1IK27s%2FGj%2B%2BhP3Fjd3PYTbusVmuHK%2BhSniI6lfMTGoo0eVVwQYQ6FZm7QH14gBcXR9VqsOMAwB9TnfW%2BsnRIItXtgxWXHPLcW7ooKoqYSMxTTby%2FarDOzx6ZOl%2B5vgV8jY67bi1wuVNwUs45kXUqhsl9OH5YwwZ4%2BF6t44xtZh%2BL4DPC2swk6SmHmSvuoEe33osWbmLcl0ErzLhzhe%2Btx%2BkRiJBNMXOs7UEeO9rf8NBdqwm48pa%2BsqMOnEhJGLU5ETdcczykilfYNEu1W9bMOR0paKiOSaW6x%2FkLxA1zfDDQ3f68BjqkAYQgRsX5hGEOJe2orSoKyh3PTzsdKnmuclJzFCO7x7fpY1%2Bg4yvn1MJ3%2B6%2Fa%2Bgu%2BqRsJ%2BL46K2QbhyZqCOTXYrnAPCF9Vsy2FrXT9dbRznF0vvb7oEiNlOWF%2BXzyc%2Fa%2BM8dHFZyIs0g08PqI69LzwrSDwWSPnyjSGfrVVd8fuiLCE0sb0d2z7LdClD6OJ4LWSSPHlET8F4cvGEJP6E2LPyeQ0Lk6&X-Amz-Signature=234613586c763bb64522e8614183e043b07f62e27b9811b124d8b65b351db832&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCIMAVLE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBB3Fk8ItUgR0zAJFCJ6LqwCPfgLCWiuxDXzRidX2BKQAiEA95uqC9ObGDTyozF18Tc8xmSwACEI1bD0F7svKRo4p4sqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdandjbub3SY1MA1yrcA2SpI4Uc3NESjWoXAuPmjG1sH1aoyUdfWKUO1yxyAXhIoL2cLC5m47y%2BSGohUonXKRkEz00R%2BIN1L5AwL9g4Ci%2Fbx4a7Kvlpo2otSgVibL3CEIjNaqA3HLGqhRMlZo7VS7sL%2FhxMF%2BypxQvi0cvpt%2BjnrSZXKgG0raTSvY0FdL9qre5%2FZpf0%2FBG62O00bgKGhyeVQNA%2BeBrruwhUnB%2B1pyDELsqgyH17bthrhcMNlJRF6bc4rHaU53sObVE1qrw3qJ1R6XWOksU2Tp3kqwwNtEMmc9zMgIJd0RLKwqHNSSm%2BWAWD1hGfPBsi1BbpHGrlXOoc4jsK2JXGVlYsMXYXz4w1qaAyoLOM8kpULW53LJ70anyJvMaAKqEr5tzeTlA%2BZuwErIVsYn395S%2BR4cbLnCM1YAmsc44%2BGNRjtF%2FGjsM3u%2FWWGt5D1Jmj7iR6ikDhNZ5dpLwaj0ljxjgE6qDzUQogfj6L4ZL98%2Bj%2FhbtaAH6kNuwT96p%2FgKDaf92mJMbqiJLHibQnjNSAUX7q%2FU8k5K4Zamcp3eIS%2Fd5zZn5MpCckbX%2Fqc%2F9EmaCj66%2FSIh0VPT54GqLzBGugQWaITEg6WeCbAlHLTQRogExk2OQH%2FKZjIrEd7YkqzWXgu7hFMKLb%2FrwGOqUBOGQjZJiebkmmUzNM59cMmNZ5oSV%2FuXEVHeaY%2Fv3UNKbJTHB9EpTGbjhZxP%2Fu50LrTOL56jKS8SXoWqFK3gJqUYH4iHf6JfK8qpsSiLwOTc887eSRuI1%2FXhz%2BHPmSAeMSGS2AuJA8Q6j10kK24jIfkkUPca5t4UKUMyJLbf0z43RbhI3wduKfaMpvqbPIse%2B9AWFLZqmZb5g9KhjkDdpt%2F3Ss1%2BjY&X-Amz-Signature=27a9d12cf3d87cca1983cf9a8e7f81b976abf122a315a787f037595d33ef953d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCIMAVLE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBB3Fk8ItUgR0zAJFCJ6LqwCPfgLCWiuxDXzRidX2BKQAiEA95uqC9ObGDTyozF18Tc8xmSwACEI1bD0F7svKRo4p4sqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdandjbub3SY1MA1yrcA2SpI4Uc3NESjWoXAuPmjG1sH1aoyUdfWKUO1yxyAXhIoL2cLC5m47y%2BSGohUonXKRkEz00R%2BIN1L5AwL9g4Ci%2Fbx4a7Kvlpo2otSgVibL3CEIjNaqA3HLGqhRMlZo7VS7sL%2FhxMF%2BypxQvi0cvpt%2BjnrSZXKgG0raTSvY0FdL9qre5%2FZpf0%2FBG62O00bgKGhyeVQNA%2BeBrruwhUnB%2B1pyDELsqgyH17bthrhcMNlJRF6bc4rHaU53sObVE1qrw3qJ1R6XWOksU2Tp3kqwwNtEMmc9zMgIJd0RLKwqHNSSm%2BWAWD1hGfPBsi1BbpHGrlXOoc4jsK2JXGVlYsMXYXz4w1qaAyoLOM8kpULW53LJ70anyJvMaAKqEr5tzeTlA%2BZuwErIVsYn395S%2BR4cbLnCM1YAmsc44%2BGNRjtF%2FGjsM3u%2FWWGt5D1Jmj7iR6ikDhNZ5dpLwaj0ljxjgE6qDzUQogfj6L4ZL98%2Bj%2FhbtaAH6kNuwT96p%2FgKDaf92mJMbqiJLHibQnjNSAUX7q%2FU8k5K4Zamcp3eIS%2Fd5zZn5MpCckbX%2Fqc%2F9EmaCj66%2FSIh0VPT54GqLzBGugQWaITEg6WeCbAlHLTQRogExk2OQH%2FKZjIrEd7YkqzWXgu7hFMKLb%2FrwGOqUBOGQjZJiebkmmUzNM59cMmNZ5oSV%2FuXEVHeaY%2Fv3UNKbJTHB9EpTGbjhZxP%2Fu50LrTOL56jKS8SXoWqFK3gJqUYH4iHf6JfK8qpsSiLwOTc887eSRuI1%2FXhz%2BHPmSAeMSGS2AuJA8Q6j10kK24jIfkkUPca5t4UKUMyJLbf0z43RbhI3wduKfaMpvqbPIse%2B9AWFLZqmZb5g9KhjkDdpt%2F3Ss1%2BjY&X-Amz-Signature=70e69d9bd38059df32c200ac9d46a044db4ed226fca1efc44a8ba1b79657b546&X-Amz-SignedHeaders=host&x-id=GetObject)
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