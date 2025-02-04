

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP7AJG7W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIH6IlpD3wQiobDBTfS3iRGvXIl2Van4fy8E%2F%2BXeHX7sEAiBGwQRGlklXx56YkCL8SBvCZIWOMEkKpLlJaqVKEgxlayr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMBZcW84VM6lwtUYe7KtwDDGZCe55irdpqzH%2BYKLjc8Np6qMw6bNuHiBWtEjjmA91ecToPKmJHGmop3h8Vp%2FdHdlVkXeXhNjV%2BHG4lM2vYHKSxGy7qncB00%2Bku%2Fpo1XXh6CVMtxQZ50fOOR2kIOOFRghaBWnpl%2F%2BHNMEIBGbbkSwgc%2BiGAarP%2F13Diphv51d6Z4IeN1bndF897q10nWMhwWnOPfeDvYgrMyiM1%2Finlqyk3Z2Oll3oTWUraWZZcljxKLGPmHkPYMgSPEscAi9JsE4pPMgZe1XeRmwxQk7zHcfgb0hRXgi9k5qNlDKilzs%2B%2B9DMM6uUp4Qxp1r%2F7HOnQ3FqkU6WSX2y0lV2hPNTafsjmFRMkFe5G1Ent9q11ZsDrnhOj%2Fm6DMrAtiaHy7dZ1L5KxhDwSBaC9OcSyr2Imma5E14FkTNG9YW%2FGempYMX1syXqg8q%2Bkw4apeWphgPptQpdDBWcMeKqa3caFjHSiwGiCsnuErkFgRxtYvReMUt2%2Bw6I7y52SneCYjhMEFBBVCWKCYJ5eAKSrtZqhBrwRYiQURkBatEUM8L9kReD4fBtiJEeCrfkAJXrfycedxoW95mUw2ri3VVxRmjOhMRp5DEjVrMhK0PXkoFX8eLm03jwTjoY5p5vJqs3hVr4wtL2JvQY6pgFyPZlfvtZUqg%2B5%2BLwqmHv8mxLMPmC4IBo48N05NXF4YegzSX97rnt17kSvTPXQpqGD40jCY0Tp4Qe69lC3OGUYlVz6HbK%2FALq%2F6pn94M670Nipjn9nBeuj%2B%2FIjq23uJN9Zezl8reFl%2BXVhQ52cq63n0Lk96AaTE12IdFiiVPh92k4T4NyMHn8ZsSJ69SVQGeRnvlMBu93aXfzV%2BUSkywCPqP%2FwfUOz&X-Amz-Signature=0b01014f5da3989e5c3ca623c1d12b891a1ef5a65da77398aa093a9ca5ba2a12&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WASV5XMD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCWQDKVjzyN%2BgKKGTKz%2FRMd4P2rOqnsS%2BF%2BP0bXqmiABwIhAPL%2F3cdYe5yOjbUWz1GPAj%2B0ICbxH3HhnuxTv%2BssJiW7Kv8DCDQQABoMNjM3NDIzMTgzODA1Igze%2FDEBa5%2FUZFkepPAq3AOwa16tu8AKmGJpKhA4H%2BJ%2BNEfA3%2Fir%2BWcQga5hp2aqGHiLCn6RtKYa3V4Px1rlkpVN9qVLcEDZrTMtflOY%2Fx1zBsEAXEO4y%2FORkTBa3SFclrv9Hd07k93blEd0D0ongxIYOiJaFWfnZwrlUUz0jYU1L%2FZQx9J2uvm7QxYwStNlFCemNPGhoum5qRUoIRPzqwYPGModaVIg%2BOEeiX1bTFNd8TXagSC6ETMy1iUeL7SxE9cXUsFOWhY84EDgme9aGe0cB5B0IUinbAZUC2QPc%2FlaCjDy7QM3vUlgzYaR4MIuqCGnNqbd7H%2Bv74d4k0eMDggWEXWSVmMSYWRJytguE5Otwu07sTJF9qTwDI5peq4PUGVuJbdb4dGKlyXTEc5loIba3ri5G%2Fn%2BcTcwiywCD%2BhPfKzJIetJ8jSyoKUqEAwOVAG7%2BkDwD1RX%2Bt26eCrL%2FUuecGWy5SG79ECWulVV0vGiGUfY077macWdMX81cgwDRzRFhkogonPyWnZU8XJ1gLGSSLs9fliCrhYEgkQzVyMpa%2BrfEcZqmbQ1SvpiigQClPtbW5eL9ZBExu4PkH7%2FQ2H84s6p14UlddPhxvCSCPLqTGODbKlefRFL7cQxtTdO22b4hShKxSudKVdEmjD6vIm9BjqkAXjTy2%2B6w0t3%2FHtfUCinL7U%2FKPeMjLDLdYRH8ziJ%2F9KW%2Boms72R76xxcfbJAAtxaLeq7z8V9NvJwTXKXaKLCwFzwW0BrYIYGEbmAgJkAkq2yezHxi6XhdlsfZN2znzF6rRc1E0hFXU8W2m0gl1BKPC0IN%2BXtX5bUfV%2FEbg1E7RFKmLyOtWcTrOsXJv0Y2DHnVxWDCaIbNUkb%2FnmBTRXSqVi3knov&X-Amz-Signature=32a13d9e0d8b9f6a1f2b39e88e552d619237369cd2684083238a337d718a7f96&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3UHQGL6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCT0JmjQaEdkAsQtls%2BUbs6KM8VIkTtLKAnLPX3XNxqrwIhAKf2T27MyTBOmwPN%2BBYL%2B13cZrkp6w4y4uzVAhyZJeXRKv8DCDQQABoMNjM3NDIzMTgzODA1Igw44RLp0411e9TsMuMq3AOwySc3oynIK5CdpDOFXY33PMlcpWOteon5%2F9XrLa5NYzfyaJmZZI21vVeWG5zrMLpGH9g1ElKuP8Q85m1Mz8y%2BiB8SBFRg07HZ35%2BzmzWCFielad6VyCd8TWuHgpmQXZOJlhCQGUMryDz3%2Fr%2BI0G95ckgiZO51BM0vhnYLJJLPdT5mNVgqtwOH9%2BeVf5Ops9Wk3NUD5envYd5EemorC4tKp0dcLbuALMuR7p1dd0p9mS5hW8krmOEanLIwYTOiKi3aru3NhnoDv5Hl3SqByBI%2FzqxKyBADBfSypGIVZOWg8M1gGMoe1Rwqc2oSLwH2VZCxp4repxBMVoRtcmNfmnLO7n4NPyv8TvGWt0tTpwEr5WX8GpcMuxQRVqvLqh5IatH5fDuMKS9lmV6tbuf2CnOhAOveQJl%2BJt%2B8g6xn49OmuXqYmfNAJl3IIt0v67Gqpb6EMPmIRc%2BjnlU8GG6L0gXAeR0yE3CNHmf%2F8lG8sDakIbcVlh56M3F9CKlqsk6AheO9k47M0EF1c3Ce%2BAlj5PiAc3%2FeqQl6rNgubOsdGlcBNjSvnFIsxW%2BFplvDMuEMpS%2FUe3vHnAM1N%2FVXF1dUNCfjD2svvJywXmJZ1ZuB81MvK8LjEgwP3nhsyUyn0zC9vYm9BjqkAeWxPnC1PIOGktN3LCIAt5R6SIux%2B7JXcvg7E9vZL%2B%2Fi%2BCONTuaShbfhAXZPBjHHcLGz1bKR%2BzhnLPYFjv0jNrvyzGHUDusRqVFQ7WHPwGThs8xPKeX1JGxiuNNGkCcVf%2F%2B%2B%2FUjHZc%2B0vFnY2rLmhI9FD2cNtDVey39tcciDbilrHnwTxspamuhEnSzlU09PPfAcIDEKrO%2Fc%2FCsafcCy%2FvTwU7%2Br&X-Amz-Signature=929fa6c314507b94c57d793ad7c7607a6d63889b83ad982a5f897c93bb3b07cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666M6Z5KI3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQDfKpUuLlX5Y8YQEte2fv4G1sdOpCQoX4Z5J8jrs%2B6UiAIhALVzw0yyIrVktvJ3phTLWJjk%2B4t0KVkzGKbJY52OqHA2Kv8DCDQQABoMNjM3NDIzMTgzODA1IgxsyOdF6d6PQNDYeV8q3APlgxPk7kVbn0a9mQidL0b0Js9KCZYnTCq656BmeWYRauA9oRWLZ%2FeAdJykJemNtrPjQURLOC3ktkXqWs5%2BD7SYTDmIlQSMQaM%2B0qHw6XwDOq0YSXjZJtxRy%2FBBd%2FhxelRZn58HzNGjXFLv8rTzPF9TDNSCbg1cCO50OGWOcZ0YaVh3jRiyM8Tk1TmVpbshtZAYGRNepU0CwPGw0QzufaY0UZjFVhFdmN6%2B6n1WuS9Fr2fOOUmKZ6LG%2Fi5d95VS6zI5XP5RpJcEgN0P111XIs%2FjzQ9dlol%2BnKLIrP9QZT%2BMPxp6mO51V3ahfX3IjQFLLSer%2FiyCtKUYQHEWGldkdqPjZHKUN8ZdAM1qx9rFfbcuXUP5QCZNPKS%2Flkik3ppYzqOb%2F3MUb7o%2FHFmvFdH20IIDKnX%2FqPUnPurMeNl3%2Bqbg0NVAf9l27CFFs9N45g%2FcuD2QuX4VqRkHdkzMH86lgiVcDQGwZQtqB806GWxpNFSuas1vx7cmC5nkUOqN6x1aKh4D9sphJhh4GB9KHIEWwkGLVGbcFjCbYy2BSKhDDJX%2BNujrwveNtVdaIYFtuXqnhQJAR3aAjhI0Aivhx46ZwT0Od0zO1WTg%2FZInTfQddGe0F834wZmaFwgVUkDSjTD8vIm9BjqkAVuwcNfdkFp%2BjDdO7AwqJXV5r2ianJsvr6sXhev2%2Bbpt%2BWvHeNA1S4%2BrvmipRa6jie9x%2BxxmcPebrbn%2FZq6Ybu8uReI5ft9ZuIyZKs0L3SKk2lRZ%2BLAxF68j%2BJhgtnHCjQJsH8lp69BOpMFfzyPFSfYOVPvIZIOCB649fwDPMLsJFcfh4x1x0E0UpSDlzBxoSw2oxacnr6ba2bezBEVpZALRITrK&X-Amz-Signature=1a1d2f248f2edde5c0015f9be97162474cd2faf63848a90db07c7c7a8d0328e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRP3EJTJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQD7oM63ldACMuUNl4ONa6yQdZJyJEguaqZJbe7RiJlF4QIhAL2Eqmsl75Ze26TPLbcckQ%2BGGiRFWDL%2FYUzDza0BF68CKv8DCDQQABoMNjM3NDIzMTgzODA1IgwaRHAUPotZwzfZ2Ckq3APj%2B%2BuTWuSVbI%2F7v8aE52%2BscWW3F%2F6PIGy45QwlwMcTC5vb7p1SxlLC3ZDxk1nrTim%2FxDY3%2FJmdtvjUfywGpnm4hyXbgoG81J0Efy8A2QzPWpNddsYdlqltTYkVF1NGO8WdKMZSaEU5r3vlHK6j9U4HbVHNVqx4%2F5%2F0Kk7a8sjPKiH%2Ft1NH6n0yXGcXYHqNae8sZDweags0QBtWigEyssN8HqVpfdVZtgtZGOSTTMwExUt6NWpkPj6utpAdsT9CRIQAZlQBGhQDQ8%2BwLPjvxl3OmdWJPt9VtL5L32tNOpzSMrqFJc2Tn8i6NWhT0Q2TELf2szqgRyLWn2VBGMtWhnpTIng8xTuoLAbhz9o3QIyNiwxavoq7j%2F5ld4RNq69rere6YWtCNS%2F4A83UrTcyHpwnH%2Bed02Rt4eyitPw8fMZ2obMh9GrRayqbqpj4fS3YG53vU3%2BgldAWKdMjYtsxfatCKBjU%2FkyeBBG9M1dkZ4vx0G5kv0Z6d26a3R8cTDhl80sSGnFPq%2BPc%2BOiCK4HhG5pCXaG6anGbhxXufhzY4o%2F7MoT7kIoslDYvldcPJFO06Fhke%2BA%2BtpVXeiDObbATHA8lVxvF%2B%2BmnJZq3Wq1HZTkroSZS%2BWf%2B%2F25pNJUo2DD8vIm9BjqkAQEg53tTbkJXSh%2B9yuYMTAXdC6NU8s3eAZvak9odClWLyLJOArsJxdivljLghEtKR8Nw7Q01V0JJt8d2epRHRJE9choZLqde8ewNzHaiWrizvbbkpxWIRgP94ltbQzi9j2aa1xUguSe5eW969kNQkCAofitBPRV0Ehiy7%2BCt9Vmg%2Fr0%2B3iAbCNY84ae5J2RBAoec46N8p0GN9x3YwBHLHBdbjn9O&X-Amz-Signature=44fe4653e9cd9a39c3cb038621d82b3e978ad92288dc74ebedd12698c20d8646&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDAEVJLW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQD29k8J4cDGs96Y2VX5s9GamfpMTFFZbW8hB8PJQizn0QIgQmjwEDOpVY0wby7rJ1Yd5Xming2f0VIeaKnN2bfd%2Bgwq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDCqEZENBeSisYqip9CrcA%2F%2B7d9%2FFgmTxhU59AkDqJA8Jeh6e355roDoSbQfBvLwzqEhJ6W7Ix1JHn%2BR6tvhKKCHobrtAWoO4eUEP5%2BPoc92ji8bHH7VXoOX1uv0C5Ycwc%2BeXBIZfC51N7Bk519vsBPbn2gbYh1AWC1mVt4sG92MXPmER3rH%2B8xZM7SgCgXmeOSvdPtNLfEzvW%2B2E4qjrzdImsql6yBn23XbJ%2F4OKp3uFJe379824yEMWZUeYUSz2tIFgZhKLjw4LIX6yGNdRQFrHOo9dTo7qA8iVtwRXsc2VsROxBy2dcrivCKTPzSVSs9VfMkrGDm40UpDlD85Gq3rNi7RHE4A0FcIBtrTTTrHmv7b1ARNrRg4Atx10svmSaBSgFKGs8CJNz9qE2e9%2FHy8lMXXOEUeBJ4gRhDQZ37JyrNHLEoSnHRTWWvHnLpeHWdgsWNJh8fSmLfQCu6fNJLMAmlDjP4QpuVibGGLXXN%2Fut0LE1r9K9BoOZNYu181f9UrNJHyPvyXDDSeCRdsnQ%2FFE1NfEVVSA5Ttyv4VartWyk1lsl30tPeb3FnpD9ZI2wHS5%2BUKR3mBDx%2BVJFf7kzASmKmAyAfcBer%2FhUlAERaycVvfap%2BHOgUoecFsM%2FXDlV7VVaAVs7GxM9it8MLi9ib0GOqUBU1t007lVxk5yCMrZuqZavuLv0zb3Ad%2BSvUIIysotYJ55n9Osus5qECwr7UZ8qIUSFIHhw1%2Fvm%2FQvGG960HfwW9GhDL8pLaS%2F6%2BXbaI56KNAzV0uUkypNV30i5qudZJYrOlNnjECKmTHeBR4HMjHuAbf408C9sVxYzbXHOU5wb1U2g%2FhlDw36nF0NB1lBoTq%2BSJt75mm2Tj2SeFA7wSUew2gckIkF&X-Amz-Signature=4ffbd02cb47a7619633390d98b98450302639322d659ca7953c5715d29bf4b6a&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ4X5BCW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIHeXo2l6afSeVSCFGGMQVXo4SDCyWBpeI8oYMemBTWYNAiB7vnTK4JEjUJeyVPTrk6o56k0RgyqEEwKRaekTVJmQuCr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMNAF0OdLtN9pOWsz2KtwDhKm9RV9nprGtlb%2BNBEQrLKZep3Oz8s9h4AFgB%2BBjOtpkgzqcXC31os57J8BjV82qtWRG1joWb%2Bh0OENuM60%2BDvS1lMwqUunT8H4Zy6MltnjMm2uieGkZdTru8U8s2K2TXu%2FSo0foJsq9Rcl0wOVZA8MZf4gumH7bAnHkpMNhM7PrzuMGWc9gVlXHyRkzPkSCGeERb%2BI2vvpLzoLrzTW90ywtaY2UF8HiMSS0o3zru77sUlHb%2FIzpD%2BUXvSL1R%2FIYHUu2FhOdZleh0FyQtsQPJOPV8Gv3ABLBRy3IA%2BP7dR1goO4m70fZb8ZNwTP0Tsu4zvhIShO%2FwiF4hDbQqGc27ayd3OCfDRh%2BQyYVJvZ7onrUeQdrDw49RJAV0MYRLq0npoa6mcSpuNeLDyJX%2BuJfeLlqHf9ubhDK%2F6j%2FKrNUby6034Z5jU2TQMI0GvLv3nt3BwvSZExg5RE0iJH1%2F2b4QWuop4C38ijiC3BCmNlTCC3twvQr06HPVDLNDamBQ6AXrRxyLR5JXRSIHIqeaMSig3T0%2ByAnN7wmJ37YuhkoP9E98%2BY24TlRxlsRnbH%2F3suYX09O%2FRu9AaJtx6pqmdQnjYVtamhcLE%2FY2ABQyDst3Izfse5qWuyUjmr48UYw4r2JvQY6pgG2dKvNCvGNdqQ0MMhHyhijbD%2FInv%2FhwXin0qeu%2FFboPTc8wxoHQ9hb9i03yyBe6%2BFNG%2F2DxwEnrTvoeM9Y83ts9ZgJJ3rv7QIyjwoDgNliliKy8%2BO2e6pEOUfMnVKyyIQKETpRQt9bO0asnA9VtJ7fXRtb9F0kVT6VKU2PoygETwgNpUUUQwfOrQ7ovef1I7XSbhpMnWS0YbBUyHWGk5KKnDGbOz6e&X-Amz-Signature=2cbd72b50b8cdd11fb94b6224e932a6d1ddffe6e33e307d38e22d591545148c4&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSOH7PSI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIB77FoTkjggCdQEUePzXD66Oz6uH2FNQAaR0GGUe4FYmAiBEaoenIa3Ygjg3KtlsTtOO5H%2BvPPwXOXLAgPyXjmJLKSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMxVCPwQv7FVz%2F4ZQIKtwD6LWE5Y52rxdboVb65w%2FnwypYnMscSS%2F8loMYEQmoYfLK35ov1F1G%2BQGl%2BxG%2FvwrlTJkXRX8B01HP5Okrj9KjXMHbViXHrpIrfl2WatJiF3BS2lj8gza19pa3rY5euPkbTm5xQ12kdxkLWf3v6KfFCSAPz8J0xMzVySHRwVoiw%2FaYPaXgxCaZdiQpmT1XBVVA3ZcErFJ6Fh%2Be7q6T4Nh7M9z3i4Pi0Z%2FC9VtdeNmFJrYzdSfEsrozEo88uzFrG6eE4ErUfZoEIkUhPdtFAgnYCJ%2FbJya%2FNXHIsqmHHN1ldYtHhOUsfPX8oE3UQyQY1nbmFmpW6uBn0D5XdizJM4DTuGrqyA1VmOiIFoZMudXCRMHVCW9NiDud0Me3cQBAy%2BWKwQ0sQBnehE7LglzId1n672k9lyccy8zDM%2B6DbnyDB8nPpx9rg6IB%2FDh6JY7ZpFKeVFcfSJQ%2FgIEakS%2BjspB26necYuiATyIvuIsYso7zvFWvFxXuOFbym9Q0tlT8b2UJEXYYnPUSttq4er2hKE3eXx56uNNZfHhvjmof6nPVGbfg5tqszzg0ULWwev51iFNITtVcrej0SruoZVMTpbCMT0eduKaZgX2LTMf0yL%2B657VBXF39fq0WH4aFgjMwlL2JvQY6pgEbs2%2BNpPAChcJXApvDBSl4Bqluf0X7z6%2F%2FnvJL1PHwnsCkGZh5V2%2Bn%2B85LEMvJqu3FljZ6TyHNT0qouUnOqz3PnzVwxGwP7diNoi0kcc19YYSYeaGQ2Y7fCByJU7YbhT3NvR8XYIKjyITcbva1J7x83nfl1IOdnjafMjJ88POMMY90OAK1VCxg0kpCcijglatIB9tzFp7Qgv7q1B10Ms3k%2FgJIZOHX&X-Amz-Signature=a6fbaf2804edac8e1804eb1cc7b1b192823e0abc420af66d5cf1d09c250d1e81&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRP3EJTJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQD7oM63ldACMuUNl4ONa6yQdZJyJEguaqZJbe7RiJlF4QIhAL2Eqmsl75Ze26TPLbcckQ%2BGGiRFWDL%2FYUzDza0BF68CKv8DCDQQABoMNjM3NDIzMTgzODA1IgwaRHAUPotZwzfZ2Ckq3APj%2B%2BuTWuSVbI%2F7v8aE52%2BscWW3F%2F6PIGy45QwlwMcTC5vb7p1SxlLC3ZDxk1nrTim%2FxDY3%2FJmdtvjUfywGpnm4hyXbgoG81J0Efy8A2QzPWpNddsYdlqltTYkVF1NGO8WdKMZSaEU5r3vlHK6j9U4HbVHNVqx4%2F5%2F0Kk7a8sjPKiH%2Ft1NH6n0yXGcXYHqNae8sZDweags0QBtWigEyssN8HqVpfdVZtgtZGOSTTMwExUt6NWpkPj6utpAdsT9CRIQAZlQBGhQDQ8%2BwLPjvxl3OmdWJPt9VtL5L32tNOpzSMrqFJc2Tn8i6NWhT0Q2TELf2szqgRyLWn2VBGMtWhnpTIng8xTuoLAbhz9o3QIyNiwxavoq7j%2F5ld4RNq69rere6YWtCNS%2F4A83UrTcyHpwnH%2Bed02Rt4eyitPw8fMZ2obMh9GrRayqbqpj4fS3YG53vU3%2BgldAWKdMjYtsxfatCKBjU%2FkyeBBG9M1dkZ4vx0G5kv0Z6d26a3R8cTDhl80sSGnFPq%2BPc%2BOiCK4HhG5pCXaG6anGbhxXufhzY4o%2F7MoT7kIoslDYvldcPJFO06Fhke%2BA%2BtpVXeiDObbATHA8lVxvF%2B%2BmnJZq3Wq1HZTkroSZS%2BWf%2B%2F25pNJUo2DD8vIm9BjqkAQEg53tTbkJXSh%2B9yuYMTAXdC6NU8s3eAZvak9odClWLyLJOArsJxdivljLghEtKR8Nw7Q01V0JJt8d2epRHRJE9choZLqde8ewNzHaiWrizvbbkpxWIRgP94ltbQzi9j2aa1xUguSe5eW969kNQkCAofitBPRV0Ehiy7%2BCt9Vmg%2Fr0%2B3iAbCNY84ae5J2RBAoec46N8p0GN9x3YwBHLHBdbjn9O&X-Amz-Signature=d9095f4109f53ac8a769cdc45b9b796b94acbe38c06502173e22dafe4512c852&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5Z3N65P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQCs%2FJI4nqj%2Fpnh1PmNZTB47gZzM9xuoX5C7bP5q7Dd7LQIgbODNljqU7cF9ELhCrAC7FdG1Qa%2BiwLvSeW74HVsquVIq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDCTPONhXncxJyav7XircAxTXC%2FH1tg5V2AdLv2Jb9e5QMcgP1gqrsqw7iwW30GlqRbNQhWgyoUilYzV4Ix3bqmCbAmRGcM6gporuUFe33%2BOqwu2VpZvAkd%2BdeFuNYYPURzKSkH0ANbpm7x1wxEHpN9Ueb91Gz33U0iiS%2BihpmAlmxV3nRSpoOUCCrAB29pFHaRivEiUIx37KaCpJU0hxVRB99ZdLDdxQ2uqpqb0B8fguBuJgUpLb72ZZ5ELRMeZ6vdPWn0flPP1N3GbggYbLidtFWmFZbAkFfy7yCrgYHfjgo%2F9a%2F5D7LlP4ed%2Fxpry37CaxpdsMMfzud3kZScHzlxGRlXzOUA9fPXUNRhoda2xr3dcwbVkkBfzKUj1yeBmW2E1Do0IVd2MQDKN1njrozcswP0byVRYTgHPoWOMin4SSiQU3CPM4Qp%2FfzfZVM34P3xXmz8mZMOD0T09HRuNUqdA%2BoCjAR8DKCOjzFWNolRb6Kqf11oDUQhY8TR7SknZoZ1a5DwYHPz957JoS10c95be2qG9AfAHV4TVXuc9vCbOEDbT5kfnOZ4OhgABba1MB7i6zrr7f3%2Flm23sQ87dF3g%2BHZrHX%2BsNZAIPdEZxMlXTdQT00s2JwNIgsHTawAFkeayll34BokQHHOw5mML29ib0GOqUBxmwuJFesMGEQp6Rir%2FyxIZebGMM9CQfaKyLx4JhGUZ4nFI6YWT8quTFObzZl3bqDBZNB5NGkiza24dFZ7xSiK%2B%2FD2i%2B1d7MfERZ3O4k7oBgnpo5Qbz2cJNvTSNWZ8GrvMFdCQwcJd%2F3oWAl%2B%2Fg69l94hti%2FjdGCfd4QjZzm5POL9ABYhqrqjaExl6HmKjTE2ZFVAb%2B5BQWgxx6%2BfO%2FMG6j1msO4T&X-Amz-Signature=3edb81b3919213d0434ebcecd21dd8568d6a57e2c92825288bec1a73e0b79145&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5Z3N65P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQCs%2FJI4nqj%2Fpnh1PmNZTB47gZzM9xuoX5C7bP5q7Dd7LQIgbODNljqU7cF9ELhCrAC7FdG1Qa%2BiwLvSeW74HVsquVIq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDCTPONhXncxJyav7XircAxTXC%2FH1tg5V2AdLv2Jb9e5QMcgP1gqrsqw7iwW30GlqRbNQhWgyoUilYzV4Ix3bqmCbAmRGcM6gporuUFe33%2BOqwu2VpZvAkd%2BdeFuNYYPURzKSkH0ANbpm7x1wxEHpN9Ueb91Gz33U0iiS%2BihpmAlmxV3nRSpoOUCCrAB29pFHaRivEiUIx37KaCpJU0hxVRB99ZdLDdxQ2uqpqb0B8fguBuJgUpLb72ZZ5ELRMeZ6vdPWn0flPP1N3GbggYbLidtFWmFZbAkFfy7yCrgYHfjgo%2F9a%2F5D7LlP4ed%2Fxpry37CaxpdsMMfzud3kZScHzlxGRlXzOUA9fPXUNRhoda2xr3dcwbVkkBfzKUj1yeBmW2E1Do0IVd2MQDKN1njrozcswP0byVRYTgHPoWOMin4SSiQU3CPM4Qp%2FfzfZVM34P3xXmz8mZMOD0T09HRuNUqdA%2BoCjAR8DKCOjzFWNolRb6Kqf11oDUQhY8TR7SknZoZ1a5DwYHPz957JoS10c95be2qG9AfAHV4TVXuc9vCbOEDbT5kfnOZ4OhgABba1MB7i6zrr7f3%2Flm23sQ87dF3g%2BHZrHX%2BsNZAIPdEZxMlXTdQT00s2JwNIgsHTawAFkeayll34BokQHHOw5mML29ib0GOqUBxmwuJFesMGEQp6Rir%2FyxIZebGMM9CQfaKyLx4JhGUZ4nFI6YWT8quTFObzZl3bqDBZNB5NGkiza24dFZ7xSiK%2B%2FD2i%2B1d7MfERZ3O4k7oBgnpo5Qbz2cJNvTSNWZ8GrvMFdCQwcJd%2F3oWAl%2B%2Fg69l94hti%2FjdGCfd4QjZzm5POL9ABYhqrqjaExl6HmKjTE2ZFVAb%2B5BQWgxx6%2BfO%2FMG6j1msO4T&X-Amz-Signature=b40d00c8d0d528b543f4caca6d5a2632325f2836df5d463a18ff6216d2d01f3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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