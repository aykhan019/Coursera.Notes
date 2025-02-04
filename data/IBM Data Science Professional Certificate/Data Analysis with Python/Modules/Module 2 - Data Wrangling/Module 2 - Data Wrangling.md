

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6E566ZV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCMnPhzwZwEMzv58aie55bCBJFp2tnY6w2oMX%2Bwfj9%2BDgIhAMVu4de5QmqwQ3JrbzBUh520Jpxf%2FmhQSQgy2QaFcR3MKv8DCDEQABoMNjM3NDIzMTgzODA1IgzyvicVFxW91o4TxBwq3ANC%2BJ2I9%2B30lF04h1pru1im2%2FhLnlvYLfUJnD%2BaXea6lqnPhoKh1vEc4xYZBUa5kFSoWqmnFoZ1ECDEQCh6cCGWKiAhnpXdhPA%2FCxlqb84jPTl54zuSSWr2aYKLK1C5oeuGKk9nhy4VO02H2d11U4Tz%2Bn756JW1zbA%2FrmQGvULTUtkdfu3cY53wKzz7km77ktJCv65Vls99i264zsNFLW5FUcTvRsNznRXcpLyqe6D7yZY%2FYZ2rhkMsjPsuqWTxrX6BJjxNEGSHJPN%2ByIVzql3%2FF0sBuyhvaXbRbcuJOlROc915iPGO4Jfc6K%2BsPiRwgw6BkYycU54eZdRF7niZlMW2X5hTvOf0KzpRJ0dDaoCYJAm1ZzXc8QTx5wXKdeQrnQbRoE2ZzySfwPOrHx4ZGhECMS0k18SyDrqCgdyyY%2FK6hoC4w6OsHMit58U1BIyChxv2yMsHbuhNfvQbXAnuRuLhPhe2mafWxcfvn7ZKUOKO4kbhzEECQPrEZhCJx83GGH0I3ZuKeIVvM1SRaWAOZYymrvLgbwYXvONZpim0bDueS3u%2Fjpe8VNfErTBBip4sp7vrtrh8rJUXGDxoT5JmZCB%2BgYpLQ9pOa5SBBCF1z%2F4GYGx%2FZMPrhJ5WH%2FcnvjCO54i9BjqkAYnpJ3bu7fbb8M1VHLWyYpWwTECCEyBsVktaWZ5q%2BbrDpj6jsRoMg3HdQkxzAa4pGRKmhQd1OUiiPMhsr4pLwbLzpfmLVNpbB4WlzA4SXSawgGcEnqK%2B3xLk1qsYtRVAS7Du%2FTsq6KofwV8FiH%2BklZQq8uon7TamIbtDjYyjMiTllU%2FkZBfCU1HgGhFbdsni9bHZ0aQeHvIvtcaNwzHUjs0sUAMF&X-Amz-Signature=3431ea5a36bad26ba6e304832b745e27818db2a133627314aa69623b07eef0f5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOSADDF6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIGxy2mgXcDSJeS3GNB9gAsmsM780j42pKt5ezFXxqE22AiA7JIZLQzlOhwHQnE%2F%2BWaEmmFvxTP2rMAQAQL8%2FKqsApyr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMhwXDV36GKfBiVUZ6KtwDewU6AOlZNZCCujZY%2FM7pUTFv6j6yvydzFXUKQK1qOtdKMi6FR4iRmlaUDFfkxoD2V8tuNdq6%2FNVaLbtT5stXCyDz%2Fo%2FgCtzKjQTkqweJ0udTNWiPJfwGG41Y1f50Zq6Rtu2C1ZfOH237s%2FgKzn0mhyd8DCpe9eSZw4o8K2xTnlor61wvQYrtnO5sSYR%2BksY8GYP7xpW6Bfj9tPxXRbnnz9Tr7W%2BQnHWtWgJmI%2BTIwW32eRuP8oOQtln34uEZf%2BGOXAbTkM2Lqp835qXvsqwi%2FVY711qptNYWRwk%2FHsTwuZDRByoExgpvO5Ciuz8rgUzAgaAHEOgGOXFqfMWU07fN6Bya%2FNPWU%2Bm6VW9BU9uqHPzBxNOcdBHj7MpFy9wNToxJJvgfSkis6%2B4DQ0qvZvvsw3hlT2MRrE5jI%2BvPicmdMX14JRO9ZKcdPFDVBHes2HEqLed8ndpkoONbO0IvCu4%2F%2FpHQfR7pad1bJ2fJeiyoILN1oNRAMqBV7SIdwVlFXUdQ06Hq2fSOsTCPsc%2FhvEnYvhchNJA%2BfJkFTRvUIq%2B5ZNw3wPPe3wwekTIeiS5I4ksQxbN0BtytpMyUZ7jawjsePEnCFAOsyuKXnWuoTCndlS3%2BDXOPx7aKHwnCiVswheeIvQY6pgHP2Kj3AxGvYzLNNeoJMTJ%2FkJOREvTHn50UqFCUPe%2BR%2Fq3a2RlGOWpO8s7b3DGfecBb7S8JPr46LGUc4CEGTnol8Q%2Fpi4%2FOSv%2FMgD5wKqCQbytWfA9fqib6JqGrhGiRj9pd3JX9%2BUuD6T0KL8ZtMeMxk%2BZhM1Y4iyOxc5Z4ImYVTaSU8aJaiJYViJyBu6bPMr8%2BhwpnB25hpFeWniwRcVCoJvNQ%2BwwD&X-Amz-Signature=c5e500ec835e13c16c49109ca4bc6439738063d9506c93736f1019ebf9904ec9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NGO4JSX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDvTuJt0CV18b6WbLiW10SKIaBywUpUOc2SQ5wrXhmjZAIhAOTfMdn06pvIfR1GLDCB1eBHWRAhN3LJ9LpORZkK0q%2FeKv8DCDEQABoMNjM3NDIzMTgzODA1IgwFnnNyr8sfwBT8Czcq3ANbNG0tqpICVWFT02%2Fs9exV2FmJGYuEqa%2FzXnPRS5%2B3%2B7bK6zdW5ikO2I9g9efZIA6W0Q%2FZNYbG7%2FFSqM8cki9JJff4vW3O5HezJBh2P0BURHdG5X5sVvguLsmIzynG7IUXpHovbs6xUTpDCyUzRuG7dVNDvpHzDKGSc4VjCGTZx6nHrwlScqm62zf2YQnFiy%2BMz%2Fcfub%2FEnkJ0mgqA7zT0fALybjtMY09JHbyitNG0BOYCxFwRRGPq3PDvPlhPD04x0ZJydY9xPFUshDCnSTzB2xZgSntlDBF2YHRaokI7bNNGqqbBymhIK%2FTo2IGjibRhTgZj%2F%2FJOiYFSkGyuqpNLjIK6tD3R36rlkYRzPw9VElhSN8pr%2Fgdn1N63SfXKVNG4KEhbZ3ifNLsyh%2FvjkvNsz3OIr33p7fvQlBcqgX5m75AFK1%2B6O3R8jM81Vo75%2FErcAEM1gacpiHhYiVRkl1FXByjU2lrtxraHSGKelTXQ%2BVYqNrI2gzAh0%2F1xcMQYNYU5V9SfjpeB%2BbBc5xWnc8L6kqMiU2ZsZ6l%2F%2FsmbjWhjzUHzkLsC%2BfEhHEITDstlo6EJdfVP5CuzxOD05tY25CCRsY3a0dXG5LQYSanMAReeSN87jRP7EXcCWhDEuTD25oi9BjqkAVksko6qyieVQupPPhp%2FrvKBYUmddSAjHPMAGES%2BnRWAMuaW8SRvrS5yrFr1%2Fa8J1haEzRTwe6u0Jk4OgOIIMvJa71jJs2GBAMYX182TznnAc401Gcif4xO0W9CwOAuHZLjGaGLSnD85sV%2FkbrUivfR5eFPyD707DJl8aYFipOE%2BgE7sqHEv1qMvVsT3GSZjWyw7fow%2FYGfUTYqJgr4D6Nd5k82x&X-Amz-Signature=fb261c081d10c2bb1762f568003a3d43fdac7c053e8b2802c13165f2009ab6ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKCROHNC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDJP3pD%2BMzkJcR9y4KZmeuyGO7uwfOQLldcmZ4gMlvlXAIgCIR2C9kK9WNHuvXyd75Y3LTemk5q3iFKzuYI6zLH1t0q%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDObKuDck99%2BZ9ajJnCrcA%2FIRDF2pft%2F%2BFBsuD%2FYlkWcSNvoOLqiI8lmpdb7%2B1uOjaOBI7VvXpPDwtn3ORw7fG4FlQFlRvB%2FlkJZwPFiMR5wvPDWr%2FHqAQowcxXuKFntD%2B4W2fC3Z%2BlqNLDH7wW8XC5%2F5dUL%2FdNC1kwommYMWCjovy6oJUQvRbcCtYNCtXaBnS1wyjZ3v5r%2FsTVbcUuKK7CXSlSsRnnwOpef%2BjxRp4mt5xOIeqlOwgR39z%2BENk58i1NJSAz%2Fg6u2zalqi3gJIDVry7W1nqJmNzsLIPOwTSDKDboAbzOlhCPOeofrG4DteckDLc%2FcdcW37MZYbcMxgr%2FZV29ccxwFVc4pnb7%2BGlEEBD1w5mdsExa5eOdFWisfmjTWcIH8nYvlbtCX5qgwTUv9vHk4EZv5AlkN3U648GS7SJ21D6rKh0AtLMOj7OVhJqKfnzX2JzdC5kWtcUwxY5JaqP3gu9kpMr6LxnaD7vjkRNbQoEzjvaIRXAvH%2BlXFDeuoriis0EuP%2F9Xs%2Bk6VsDvcaOY%2F9GDs%2FXyOGy4H7pJtz187N5qas3VoTZ1um42e%2BHTDCqW8%2FvTivMk4k9xIuYfWXpJk0PomQdHSXmp9eAvJsRvvZw3vTMs%2BkExqRhGxqNni7JT33jEZAzMRuMKDniL0GOqUBTJlpvUWs8yQMr7PUz%2B1ylZLbnFdkkydyDrDnnbuCr4oB%2BOdQD9j2x%2BqlG5t5bjugsgdum7eJg6GDeZ8%2Fr%2BccN4HRticv0avyZQS%2B4rafnWkOUDIOzm9aHhb4PPhKHxG%2BiRMiiZUH%2BSSquEItFoccMInZw9P9zdMykbcUksRbTtJcZL6k%2FvqmDCyJcDL6p6yz2THt88YquVIJpdDFMczzuF8bZyhl&X-Amz-Signature=6a87fce05ba11d7d0e130d4064a095cf096e2504eccc665f4f97db5b97ee73ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMMLIUTR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIA1kSD2b8pf5e5MbJ0E%2F3nV3uLq8B75ZoYjpnvtH15jbAiBha0BmI9LsNAdbe1K6BxUbziPuli%2BMe1epDo%2ByLHUQjyr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMW0TjQmaO8kzO2ZazKtwD3SWnBEWtZSbGWb0BN794Difyl0bYnApw4qAqS9f2%2BfCzGCD17KpFSho8UkmGS1vVz%2BZabJT6QlgdA1c%2FWajC7SGCDcrkxqzVBI5jNJRTuOyg2FsczgOCdW%2FMEisS3oPqqCVyU4irpfrmQTW4ktNUH6FBoOn%2BtT4%2FmVKutmNG1F0ORBRnnsWLueIBeG5rDYeRT9kNJW%2F0H9GrSEvvJpQ%2BFRULZhcim27fWR7PDy2YPL%2FpV%2B1pBXx6AlCmW%2FEPYod0T5xVt1laZ%2BcR%2BrcahF%2BetyoS3VzYVAbjk4yJGS7kRzkSL9YAwTnb4DK0tOk5zGZnwquFmx21yoJKdspdGN009wxdUmMyfJWFH0JPz8ekHwqSyZ16BKkjh5cXqjFzPe%2Brfg4qLvyRcPaqt8PiVLVFkA9eePdH7C6FR0uqZHzGJG39UtIV15vwMlvhNw3h4leIowo%2BASAUuA2ba8c48cQhA3iBBnoNgQ%2FUWbrb9skRXo%2FUvG9iNFdpQpzCCeIKJ4fvFj8fMt8YLcpPu6%2FhCz5d7K8XK0kqjSA%2BJQ6DDehhwiOFPz2fGe6ubA1VS6BgcsIdqAkCUEWI3nXFeNkPayhCshNJl0zj1kYAIRmvw0EpCq7%2FpHnw2cezXQHQK2cwzuaIvQY6pgEwiHlBlSbU6Yvp28ZECuabBhg57i7PRvM7SVRN%2BxCqzZ3RgZ3gyXq5w4nJOGcpj13BfkMmrHgvAjN3YxZsTHzUcTJBWus4lLxfT12zSiQTdIDoXJ%2BnYD9uZe9rwIssolN3D8nJGlZR9TRIPDo4vaHLPkNmVyUOFOSa4ikZa07mgRvFZlW%2Fis460Z4An2pdEJwe7rPuG6DPYZY7LNQDODEn6PJLTsTU&X-Amz-Signature=9a5e67f8e4fce50fd2ff7cffabd1edf3a37debd06b990c70a106c7c714a4aac4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4LZ2HJ3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIBMaY6KyGiIjeqqeBVwbK0Geuwm3BrsJCyyPfhbpeflIAiBRnWDkDid%2F7Cr93udhLLBixdoUanQIUnz9jjBExls%2BKSr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMCSvqke98mrCCIF5oKtwDbhopHvv%2BQuZ2l9n%2B3Jyg%2FkTlNNmDZZ4qtA2UQ0ClIieg99fmyoTCP6s6mt1RpaOciY7ZEcsnm%2FuEpbvblwlrFdF3Nw314v7V15V%2BAhr2w%2FPjqzJI6sIV8SET2MRzUXfA857l2GWjw%2FdeCYJoyW9kpi7zhyXZgbFTEgk%2BU6j3pm5oytV1djZhNUNzjxsqFA4S%2BC8OCCBekV7%2FmflVThZX0f8X4rvTAu5zxYNKu%2FVkHiwyZAu9R9NsdOcRAWA%2FbpOxiKMJr0adhRZA%2B4EwFJ5Sx7nQ%2BzCG9GvVFyrzFwypvBdyu9aWcmh1ldYbU5w9hoEuq1rWfa7d3iIIOMSPT6EguwRXG60AtIauxjGx7Ea9xTbeP%2FHusUZe79vuVT73W%2Bs67%2F%2Fk7bJapSc51Nxgp2n%2FNKoMD2MjkPd7E%2Ffte%2F0MJedzeHeYj%2B2f8KFTonr42Hzs87C18ZCdfdOoNI7tRXE8hG%2FEHZWWgr2VCvqoAXrew%2F5Y9Lk%2BBWw3B%2BI7%2BbC1Em8pDb8GZHOREAfGN1%2FOAERiSws0ynQCovsdB6oxdct1BTaacXoxTz4ccxKC3%2FmHHT7j0Ua1bUvupQi0w6HCRqE24yGZkv9KkvvOeAdyEOaV4IzM68vKXYh4qhHNKskw%2FOaIvQY6pgFsP%2FVCaNjDLvE5HreaDvHAI4JwJ4tr%2FscY9h2kwBYF2N65IEOdRSS%2Bmsel6N6RD%2B%2Fm0R%2FpDYnivTQu653J3eD8pnPzwyTlhMP0Yri9XmwxeHi434GkLRrdqRqUcg5KBB0nq1r36G4lzhQAln9f%2BfCCaJjEn0shTQync2IWHGRWdY%2F5MuPtje2%2BIuH%2F6ivXNV4N95NbvgGVF32%2BlUm%2FnYwoT5sj2UE8&X-Amz-Signature=4d05e027a0856fde36a07ae9dacc5a1297d7aec7e8a7fa1acd38dcfe0b5339f7&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WMXBGFR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDCahd4u27qTeNHZScIcq7gxsQpUCabdsmL%2BAFYAyexIwIhAK6RSB3nyPix%2FJrc2z62NWcD5jfg%2FvmFlTTJQoSJo0wvKv8DCDEQABoMNjM3NDIzMTgzODA1IgxO%2FfrZuJeL0jJmRRsq3AOhSZ2BgVNJ4NnNWXddpZPLWZ2zHupUTVEpOIFzVpwyI3LhagV88M%2FNRitsQCCEq6I5EvRFL2w2eOKYZ9xy%2BaqRjfFKT%2F6kd2%2BUNq7Ihou7IGeQkhgqQ3CeBNsJJPR1FdianwfPrTYcs7jW3MnkJ2Nr%2F%2F1D2XbsYptc7w3At%2Bs2%2FNx7C9jssSrj%2Fysehs%2BFUZhFco7dpbgPfYLYggdKcJRA1ajfND9PRmPw%2FfGVmJNGK%2F2ZE%2FbjYDP0ZXiyWDGqAqsaMTqOzMg9veVd%2Fw2Wlxy6YwO2DZ9W1a3yJLPNNNXLWFu5tlf0MXCRmTMVK21ch84geTNJG2Q8wlB4LfNx00iCwiY9MqG82NmwMvd4bQ%2BSyV1vUEALEfJfVOjNKKGxZCIIMVWhOM7Lf%2FIRAIKT8D2Bu9shx6pQhr10zwYKJYXBaLqe54iAFmPLeiKIgrzMoBVF69O6HP9mSONzm0a9DLcbZXDmeT1ZtxWcp6aFcKkAgmzXLiaPvJYYH3LeCAayp1q06t1pUaNFbxqAh5quVLLgGgSpKblWGZcRBF2m9ILiFooCk1RANrmw%2BttF1iHDl5yujmWPnLkBWnfVvjyJ8Gj601uztwh2vIOYKb%2B9fMYaLE3Hg%2BXuRuIy7iCQRjDs5oi9BjqkATy0qxw5yvGjYekbfEPYwIEG5WcyHMdsP8R6lOvcrZnb%2Fk%2Fukqs9fYlAeqd38JV37hSenGDS3t%2F5Wqpxw82V9pqZcLYVQE9bN131uw1HQoWjAIjGSgtinv7eHorXcpN9A55PWlPEjhptKMXKPzHDQ3ZiHUXW7vm%2FCRF%2F9BgqZw%2BXO4FD92bg%2FIMTFsPEiq8IVtvpbs8Gtk0PFNdowQ5ebW2I38zI&X-Amz-Signature=1ecbc745fb18518f994945bd4b74e788113e1b2411a816f6441c5e7aa3176865&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RNZ2EGU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDf0K%2B3vtPSwzEHZ6E8LZFFjUhOmB1rZeSppydU4NBf2AIhAIPLy%2BEHyiOm32VTrr4dPzgePAh0Io6XhE0C06mWBNv2Kv8DCDEQABoMNjM3NDIzMTgzODA1IgybluXcBSiGpy%2BfW%2BIq3AN6hzjf%2BbNCyS3dd7gEf6VCTjztiamhvsAYHsgKgugTQBGBxbzij%2BlpP7dQFi7u6lPru1uc2WZfx8rqFLxNxs3USBBjSLWCOUvESiKW%2BSigxMhHDp4gd8YQjtbrwgZ9lRHmpb8QqLc1sV6oWnYUBWU9KvdcSBBqTCjpQ69A54saLXkh2uDn8d5FwPxC2YyFp28Vb6kptf3RG5cde4fc4Q8l5uq%2Fx53jUyI3p%2FH%2FNcc0JswqkrWQj6CViyVFasu%2FzB%2Bm6hfZXDM9d4FGCdTjRo0CDXSlXOZMyWKev8GnOArD%2FHIPRcZ9s4sk%2BWDIiK%2BWO0t8ct3Rq0n6C0F00IGlu63Xjr5vRkus1KagmF9k%2F2s%2BYXeYWbZqI2%2FEmsrmU%2BeGw0WpBMDfmi0wDMl%2BWB3WPjohCgisarKUFRlYYG1nvcNoA4AcuQclKo%2BnpB%2FpqPIMerovXAp%2FDlYDI6Ce5CKZHhzXZiDfYo6%2BMWBb5t%2Fzh%2B%2BnKmj1mW%2F3us5pQ0rhuuzjvw%2B1sDS7M04HjoBWYz%2FmdAC4PCl6atpy2HqqPhd3aOUlIraQG01THMaj5%2FewIwKMsLND7vp%2FgkbnDgQ6QrDS2k3IdTZlUPxijxA1dkMa1ip4B5h9Mg4At8otLgFdwTDP5oi9BjqkAdZPWKBe6BVnROEWqKamTgijSisHfE1tA0c0ZlqiTrW10Bpk2bY8t4Cbvv8GDj%2BJIyaas1%2FlZDAUMDc5%2B3Dc%2B8pwUyPbKwic19Pd4YqV9YmPMH%2BQqZ1if%2B11%2B7QNBtn2QTOdlPJsjqUShHkZeeLKxKgZc6C%2FPTza9W9LMxYvUV7yHBufipd4yBBuwTUEae5v5DGfTra2XcnwrhNdUMJ8lhZuSu%2Fo&X-Amz-Signature=9b50e83e1b81de8197e321cb42330638e8ebcfcfca49b9adffbeaf1af1c8f7d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMMLIUTR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIA1kSD2b8pf5e5MbJ0E%2F3nV3uLq8B75ZoYjpnvtH15jbAiBha0BmI9LsNAdbe1K6BxUbziPuli%2BMe1epDo%2ByLHUQjyr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMW0TjQmaO8kzO2ZazKtwD3SWnBEWtZSbGWb0BN794Difyl0bYnApw4qAqS9f2%2BfCzGCD17KpFSho8UkmGS1vVz%2BZabJT6QlgdA1c%2FWajC7SGCDcrkxqzVBI5jNJRTuOyg2FsczgOCdW%2FMEisS3oPqqCVyU4irpfrmQTW4ktNUH6FBoOn%2BtT4%2FmVKutmNG1F0ORBRnnsWLueIBeG5rDYeRT9kNJW%2F0H9GrSEvvJpQ%2BFRULZhcim27fWR7PDy2YPL%2FpV%2B1pBXx6AlCmW%2FEPYod0T5xVt1laZ%2BcR%2BrcahF%2BetyoS3VzYVAbjk4yJGS7kRzkSL9YAwTnb4DK0tOk5zGZnwquFmx21yoJKdspdGN009wxdUmMyfJWFH0JPz8ekHwqSyZ16BKkjh5cXqjFzPe%2Brfg4qLvyRcPaqt8PiVLVFkA9eePdH7C6FR0uqZHzGJG39UtIV15vwMlvhNw3h4leIowo%2BASAUuA2ba8c48cQhA3iBBnoNgQ%2FUWbrb9skRXo%2FUvG9iNFdpQpzCCeIKJ4fvFj8fMt8YLcpPu6%2FhCz5d7K8XK0kqjSA%2BJQ6DDehhwiOFPz2fGe6ubA1VS6BgcsIdqAkCUEWI3nXFeNkPayhCshNJl0zj1kYAIRmvw0EpCq7%2FpHnw2cezXQHQK2cwzuaIvQY6pgEwiHlBlSbU6Yvp28ZECuabBhg57i7PRvM7SVRN%2BxCqzZ3RgZ3gyXq5w4nJOGcpj13BfkMmrHgvAjN3YxZsTHzUcTJBWus4lLxfT12zSiQTdIDoXJ%2BnYD9uZe9rwIssolN3D8nJGlZR9TRIPDo4vaHLPkNmVyUOFOSa4ikZa07mgRvFZlW%2Fis460Z4An2pdEJwe7rPuG6DPYZY7LNQDODEn6PJLTsTU&X-Amz-Signature=43286e35df1d22204e9518486c4ce330ddc028c401eaf820c539f7ebefa7b0b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TTDH44W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCICe%2BpSrOWnhrhSFNL%2BmzcZ1kU3KnndFRNz6P40UY9zGEAiEAvT822UIIaDDMjjbzGwrvpLA64jkVYNZCpVvNZZ2SEsIq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDBfc%2FYn%2FRxqwmfB2eircA%2FfoadTe1WSZ5ppHYhCxKOztOo5XnA%2BuZDGVFVsVXeuNAlvWR2VWH0d8X52oV5j7tEfbhTgQcq%2FJZ3AWWU68jBMPVjADwCEzL8iwEOyG%2F%2FB5YkfZGJPSLtigHR236d4gCWUE6K0uKefKy3BVWw6G39b8sN2Veq4nTu3xSyNqc0gRBVz7MvB8rI3VLh5r14iODSILfyEMLIpXZkRH0hGrR2P7STC%2Fip1b%2FexiVbjVv6%2FoZ4VHrymJ2smB68Jm1viGX159jn7GXXtDcZsNpcqJX8IRYgAnQYnYCZNrhxuYcw6GMzaS%2BlNq4JuD8Je9nry%2Bjs%2BrHzGpKwiV%2FxlWAirfwkXYbfPTKaSbapWJmEr%2F1SiaY%2FxY6hcOA8EAtEOCINsxlgLuvMdCUWa0nF9WB6v7Nlrt9JU5HeaOt4PyVJM2BwTF6JLt0rMAHp6FbK3nrontVHP%2B1h898v25h%2FJM5yegdzs5ihHKrBY4Ef4e9bApfDEDNa5rOi6Tn7lHnP1A9uaKd37QCtk3tOto0uoVX4qYtB%2BVuFCrpE2vJ3YLKIS%2FD5qDOsdbzC5SVatu3XG8WWheCelz4o3ZYEcoESyEZ%2BGX62loXR3QLBUCvQuiDCiFDhCDqigXgtUk9sMzJUktMMvmiL0GOqUBn3zqQF9bZG3tqLOXCBkvDKIhGTN0Q%2BBuJyZ0VKB0SsTydWZnEyrq5j7ebj2dtN7AdBQAtUZb5zNuz5v5w4SdI%2FnBhW0LYayWWqOTdy%2FMLjZKIeocTHNGZ3tPbS5ZU5u73cnABD2Ecpbsssjow4Jpq4eN0dX1lfW7EUbi%2Fgp0HE84BzOn9pSmRFvmhe3tNxtJD3lPtSQEyi8BrTuznt52o6hBIWl1&X-Amz-Signature=5ed0b84edea30cc8ea432a95f31ec7efe5a2ae7cc4c8b8f9564878439661d9b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TTDH44W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCICe%2BpSrOWnhrhSFNL%2BmzcZ1kU3KnndFRNz6P40UY9zGEAiEAvT822UIIaDDMjjbzGwrvpLA64jkVYNZCpVvNZZ2SEsIq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDBfc%2FYn%2FRxqwmfB2eircA%2FfoadTe1WSZ5ppHYhCxKOztOo5XnA%2BuZDGVFVsVXeuNAlvWR2VWH0d8X52oV5j7tEfbhTgQcq%2FJZ3AWWU68jBMPVjADwCEzL8iwEOyG%2F%2FB5YkfZGJPSLtigHR236d4gCWUE6K0uKefKy3BVWw6G39b8sN2Veq4nTu3xSyNqc0gRBVz7MvB8rI3VLh5r14iODSILfyEMLIpXZkRH0hGrR2P7STC%2Fip1b%2FexiVbjVv6%2FoZ4VHrymJ2smB68Jm1viGX159jn7GXXtDcZsNpcqJX8IRYgAnQYnYCZNrhxuYcw6GMzaS%2BlNq4JuD8Je9nry%2Bjs%2BrHzGpKwiV%2FxlWAirfwkXYbfPTKaSbapWJmEr%2F1SiaY%2FxY6hcOA8EAtEOCINsxlgLuvMdCUWa0nF9WB6v7Nlrt9JU5HeaOt4PyVJM2BwTF6JLt0rMAHp6FbK3nrontVHP%2B1h898v25h%2FJM5yegdzs5ihHKrBY4Ef4e9bApfDEDNa5rOi6Tn7lHnP1A9uaKd37QCtk3tOto0uoVX4qYtB%2BVuFCrpE2vJ3YLKIS%2FD5qDOsdbzC5SVatu3XG8WWheCelz4o3ZYEcoESyEZ%2BGX62loXR3QLBUCvQuiDCiFDhCDqigXgtUk9sMzJUktMMvmiL0GOqUBn3zqQF9bZG3tqLOXCBkvDKIhGTN0Q%2BBuJyZ0VKB0SsTydWZnEyrq5j7ebj2dtN7AdBQAtUZb5zNuz5v5w4SdI%2FnBhW0LYayWWqOTdy%2FMLjZKIeocTHNGZ3tPbS5ZU5u73cnABD2Ecpbsssjow4Jpq4eN0dX1lfW7EUbi%2Fgp0HE84BzOn9pSmRFvmhe3tNxtJD3lPtSQEyi8BrTuznt52o6hBIWl1&X-Amz-Signature=a0075b671a0fad5202874ff2d8cc38c09fc6ebf3991e782d1bddc5b5b9c109a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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