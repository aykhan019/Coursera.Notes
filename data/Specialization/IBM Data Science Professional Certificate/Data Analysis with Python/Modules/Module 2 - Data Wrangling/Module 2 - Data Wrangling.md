

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NBHLR4D%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQsNsvDFTTxOt7D4jUVVhtntmIrPVHiAyNxq%2FCUf9JgwIhALUxC6VXvHFirEmGkOzX5%2BYPNShyPZYYG5y%2BkJrZL0zoKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMHirrLjS1Qh9UVIIq3AOEtNIiyyjrlii5%2F%2FTnHxUQMFfbm7LKUXc9VL6FefZvncf9y6grMk3lVJBIF3KpdJVQ0nYkx1ON3mW1flYRcCw2VPT0KPw0612gZvoDnm9zJQq1t3GyfjQ9Yg2Dy5kaHhPEXkN51BTVRNMDDqogHk6xoszzQgf6ciC0QtDisfLGKaKrRkuQC4a0jeM%2F9x31Cpw9YFDLg%2B%2FSFhiGlYs5fRtSdfD7ubgW69jNIXPg1xV%2F2UuGRQmOiTm8LYqyg9Zpgv29Jqw0yO3Btlm1y6JcuvjL64a0IaWiJ%2B29diNkcAmpGEzOEwpOAjSg9HzOQeKHCn80aP0iITJqfSYPlmD3VE9eoy2kimmdNYJ865e3l1RSqX%2FgiEoNPrdeDK7%2BQFpB3UFIyG%2BEc8O%2FzJTzUNZVKDtoVcYptsKEB0ZISWn2jtDhJ4CyV6Ff8u6PRc5G3DkbTTUQh9zpcbouKWueHZLlsRH18evlj0Jo9wQ64mskvMCcA%2FeK7Gj5JHJ%2FylDZLgkmpaVf%2BI3UdkjfrpIqenQpYuR51J8MzSqLe5Oq6sLJfNkwnmp4%2BurXiUU92%2FNPLdId8VS1ls0xlxPcOOdjDUTugfGr7dIfsBacWFuKvJNJVeMxdLMkpE0LPd%2FJwN7nGjCRxuq8BjqkAUsMIjAKLZ718aQBDRYtKfzu8a03kHji8UgfXykiB%2FkD2gdkJvAgm5QoV%2FGfKF7UW3rXzLoeglheihl%2Fq3CkKap%2FJXaUvYFAiWggsPd1s4XctVamDGOuSaOdfc3w9q1EUEZm5A8OLV2Qd66QaYeB1KesdAjHXcTLed1WINK867bQXfDMaa%2Bbq5GW4H5QFYEcdXwBzuKYIEVWmMqMZZTwzME6y2kt&X-Amz-Signature=f72affeb693cff3b37787530c7baf2de700d5bf740698c088024b0b1965b79ef&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TRGXFO5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF6g3NuLOkz6oW6%2BeDWZwQfV%2Fx4svsqOBMv4Mtgv%2BldKAiEAsM8AxxtFwFkS%2FU%2FpT6ioz0blHw3dCb0rHdXTSEvEQqUqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQlcnCssp8zI9I%2FoircAyiV2tFUTzXHjnfFHQzc3Zmh8el5ftCpTLy8ohhHsBhOWZ5ED6k%2FKhGw%2BQMlwrsy%2FPdITey56LQKGeqdiZyZPb%2Fm5Gj2QaGFOoXc1xh4%2BiIaP1GT3nnr1bc0vqAN2X4GIx7EWRtDdtH7t5tjxX2YmcAMc3KKZZNEdnAvPMBnGCxcq5Gyn5%2BRrq6UP%2Bd1kAnvaXKSDXi96sZSeQCnMhYq4%2FDdbTDiWb46iRgFgRFkCbc3uu6mNSbXxlgVBCqZIie6T4RgNP29HxgxYzuH%2BS%2B4au6glCmXg4WAWjse5dtiAvyaZLZ2k764pQxXDJDYqri6NYH4VvYVlmBQjGlmq03pZUlNNiaoMCLI6UiSLKT0dAdxo5Q7PPiDHnIUUgjchm%2FobvLydvcWnLDhCMegNDJqcJo33AqoB0Kt3BdgFVNlGUYNzSSg%2FhnNNfqD8liyJ5c%2FWyTzjaFJ3MAuOpVIlNI9l2wxEDSAU5sb0G9GuZFlfOrDeC2d1v7BHQ%2FITiiouaMC8cnQGl%2FlTBvbnDwQvncbxGFqrx88P8ZlcySLQqjSN8CO3k%2BNO6iTTFuWTH1QP8mbzgYn7nEf4q9zDWl5p9P0FGdaSXb9HGqO5IIKyKXpwoRG%2B3B3cdkG%2Ft6pBZBZMN7F6rwGOqUB4KTpFtTXCof%2BVLCqBSZYfVAId665U%2BYmnqU7af%2BxptUSGJjOA5yktSq70APRuYxU%2FpsBrNKVcobtlSjUYJXcqRdL8d7kWbqHBC02Q9c1cUPQlaM4kfF97SM7ccRPLfp%2FXEIfZQuUKVN%2FixOfr5tdFWyiTEKE7KPYra%2BZihumpIapx%2FAsS%2B1Lm7I3YaQuvtoXtcHfN%2BpRd0t%2BIUUIhf7hxbcOyBfi&X-Amz-Signature=e549d9cd9e41c8cc50071ae918d485633dd00e1b10eba762ab115a8da477c446&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K6IRDVA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSFm0KuJvq8ZlTZEqL0roNGxmPquVUhc4%2B3UtY7wUgLwIgYOf9I1618vJVYEb25Fx%2BX7guUZu7AVaupLrbGUlXzW8qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOR7YJx%2F2I7qxpaU4yrcA5NxhLiXdJVeJJFLTmd9K9aW716xSu7gKCE2bgD%2FSduf2QDS%2Bjv7OU3R1%2F2WiDJ2wGrsoS1LiNqTaGY0DBS8JziAWMC4eUOAw5U1WQRS0KPyOTjCv8Ske6nkXEN2zcei5sjo1Hu%2BD30quUSGjpO0Bk6HQjtKNdwIi%2FdiEe%2B602r9%2BxQ38nsDwmIq4icUfRILvxnKhyKv6%2B8k510G1Qqran%2BHu3hIIZa%2FKZKDPYfCLlumfS2ng2j4cGvv%2B3mYO6jsGEXzUYH6edGOgPHHCzbe%2BIvaNkDwscHu6I5fmLkUhvO8IsV5x3dozDqRngmSx%2FbfzsXxbM7YrdIunWR0tDBnCouTRVUl6kCJhDPuRYX9%2FnpDt%2BpEzGxSxjmbaNftWETcB9u4J0Efagf5OO4P5TRAd9X5N3s1elLppSmfPsInH0cXXbGfL24z61W%2FBlL1tn5KUXjjMw2FZfoqenV76c93OSKIC7Iy7pAwnozl%2FhTu9Xi2bh%2Fzc%2B0nfSlrot%2BDlOotKNyK0Y4gGSrHLJzi0HsCTGyhnNedVzWLvMc%2BM4NqK99xollKkgkMyslU40C29EJ%2FI%2BuHK%2FxXLX1KfLHW%2FdueXi6VoMrf58Er8nf8%2Bl3zHcfVuTSYqaUV2MRseBEQMOHF6rwGOqUBqDa8s5tg%2FZVWrgiqm3YFeMLKhtijGCNmqD6KZuk25KohQpFU2jd9s9A6oK8vuwGRfJIsbHVcPLPUfk0%2BowqHVmoLcltuswvWrZ%2B1HaatBDVHZ3uMX7GJiyrkjZM25gg3MfB5ufRRodH0feBpE3eXCzrnzuvHQGbrClwCw%2BprPb7f9JkwJN%2FvXleI7YY68AUAflsv5BmON%2Bz7Zi%2BUkuQI5A3BGnfI&X-Amz-Signature=407b5355e73fe073b9369a3cdfebda630df0c2c338b56e0bb36b0c7b3e1d944a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667J72ADT2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJozBUsIAHdPCa%2FvEhgdyO8pempA6BL29UAswlb6dV%2BQIgEDzKokV%2BqL6%2FGEpUPzi%2FGTLs3vI4gbXEDuTUZPlc1osqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9BJ6Bx7PcyvtYaEyrcA0W9fY2UWlxc1rBsx6TkZ9utBpho3ZeYJ%2FxpaC6s01d3CtCXUuVKTK1IrWzuUqrdMCHAbKtgvLptWfnyH1454OMB9CmkLbbSY2xgfldNwl%2FgLLc9R6bqYkRTcWNh8A%2BBPaGC7LW7HMSaY6fEhl2WbcVLemixzBhJXVrUFAzSUpfjPW4DQ23zTTxTwqetZIRLbSmYaC%2BGTOpB%2B9d1nKQoqxDWL3h%2F7r3hjEVp5AibP%2FB7jrFALrWOwUswri8IQ%2BeSMHt%2B3rTFseZ8fGitR5hfK4TQgHI38DzCdLCwjeYG7baj3ChtaTlpBE5Dy%2F0bQgQ4HhMVwzUT1Yq90l37g8p09rpcG%2BfNS7GzXQfGpjwL7yQOZG7s3li2%2FG73vcYoMW%2BnXC%2BNd4qK%2BO5qBA6zfuFJ7pJGd%2FamyiIrKYr1RMyFa6u9e1O6wA0TEEKzgG8aN7HwigEycighsItqvj%2FoUsBpmwPKuyGllpdtmqSXbXaHy5d%2F7vy7iJa%2F0U48Qihyo92nODDOFfao7Rxq8K7wRXoe11qj8OY1fsrPb1koLzEBy1x73W6ryJIGgMqMs6YFOLQlMI7VIbEYaT0rTPBOTSeYh1IftQGspZPEiX%2BeGDpmnRR8dzcoDLT7P%2BdDi6MPMPLG6rwGOqUBAflIG3d%2BZTeUDwMerBcFlVIKVmb1cW2ZwqN%2BVe1aXAwJ%2FaJSMsiXWuHIjdNv3PkFjFi0DKg%2FSRYLvyp2L3WabxBTJtO5ffGv7DiYzmu3r6bUpTitrWs5c0zvHvQsSTp8kxuW7uoVJK0zJU%2BrJUHk%2FaZlFADXEjhpDyvZpnoNe9BxwxYFBPPXL95wR94RZlzzA9qoYU8t09rYSqVFTs0g6dHTFjpf&X-Amz-Signature=be7049ac3b4e43dcd8219a115edd60f5c593449c361cd65bfc3f698bfebb227d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWF5P4F5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDH1q07lFEO90sHIGPXDnolWgn2hFIbiCnsJC59w8UnJgIgJ1mSGIOhegXxtfQk0o2IFxevQavGNpar7%2B%2B90Zwf0Z4qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGxWdlmV1CT4hlKfkCrcA1McHtkULpA4mI%2B7FhI3byaz%2B7gnD6qHyZrtX1iSNoYovr2UnDG8RxD9HIFTCh4UOfOBGdtWQxCtQPdsN67Rl0UuNvBkVoBz%2BYpU6yuXpRgW3xHmIypIIem%2BrfKybdvcIafag9hf2pzD%2FzcubEfbhfwAHzemmYdzIx%2FsaIvIEI9zHgbx%2F5cKWuF38H3TLTU99pKY3RRQXs8j9S2G9pGSM7CTImxzjPyZG3xZLeW%2FlfdwO1ozVhfA09oRDGtQ6e%2FhfnEC0U7Od3gSKSvEUCqQICLhBeF77FVC0Ho3M8v5cSNU0jE8dzletczaEz9sYsYe9R7EquN65d%2Fupo9cYowTq7nIvw2fUKwDz2LP%2BDSWppem%2F1W%2F9a3ttv37UOFDXAoPsIMdVub2E62HDD73x1G4ScagA5PRDJ6RoG0x9dS42ITuVgN3G1SH7n%2FRplUUedSiXOpd%2FREvs6haVozK3cxLBNqIkS9ijDHl7ccB1o9e4RbON4Oey8c0ZYKUOwbV7gqZwCj6jZ5ZibMrDMRagRgSPPTmMz%2BlR9zK5AjdDNBbE4w1GDF4JjwxT9fzXI17wL%2BzBu%2B7o77KSIIArgeIqV2oZIiweOCoD%2BN10dw0J2NEQoJIkmtTzQTrxWMT8do9MN%2FF6rwGOqUBYwfOacNZ%2BQpmNMFj%2FNo5NTY2JwtNv6Sn%2FsaVubOXvEdaBlInB0RVNB%2FdEI2qXpz3v%2FnqU%2BAdVG7mqtbMFFcufIIPlkxIYoceU50N8TKZ2KEXgHye15ZgXZz36SDl42Re%2Bh4CsqjC3EVDFyVYJx7ImXSuqpLILwTs%2FYKvnm45sOb30D3Tj8dU8ATQSzDsPvjcdMZUOShOsrGoqetMAf8gKfQ8MsFi&X-Amz-Signature=896b5b75e8d47f731bbf2848fee181178543f1d8ee10826604b5ab278f271674&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYTQ62R3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjSOVNvts9tj1wnVv2He0vxXrCUuLcPaA8dtWkZg9ACgIhANq5YPw5%2F9Z7qes9IZocHeOKNzqDI%2Fo8oI%2BD%2FpqeJynsKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxzwynbiGlL7mEsSUwq3APCwtXzMpJtsGMd2xLT7VB0YeG%2B%2FGAnwug848KWrQVzZXotrvacMdK3Sqxz4bCvijlwDjGIEbgeQpMOIp12EwyvspeuuomwGn3r%2BRismjLWuEBTkuq5eRHQiaon7Ftpgc%2B1h16teyquifTQkFVbKrSWV49DWsPQiSn0U9fMnxA6xf0sOxeJqH1xfjC5mX55p2z7AsevJhXGbcVdyanPjBS4DOzljrPXjRYhuDu%2BKImGLFcYlfKVBZ%2FHU2zMBDoR%2FFYvuFbPPHsRscKvBmx7x64Y0UAs3%2BXfKEDkslj3xtKegu9QV6cPZEpxMSzjMNxTqoW7QCLGmJCcx2GuEJh45MZb9lIJQ0Dmah%2BnFcIKm1LE2SXqm692ck0NdQZUtNUhHfi7pXvFiixcPw63jV8X8QnSqYCgqyNtWpmB4qVqlIqRGs8SnUsW8Ytm9k6miltoHhAMJ4wJis8ShkX9HFtZc6oetZMXJmtDN1oBQy1PI7K7I9sTCkRRJGvJ1sDlTES%2BsgOzOj4lwNlu2YTQLcxvGx0w7UKILC%2BRHgrdUHssX56KpwuSVX4Z%2FFG0IiUA1hIu3qxBWT2YheeMBzdcvWuFRK42ir01PnZDoqukdIUZLtQYC8dLZCakEzuF7lbRWDDtxeq8BjqkASk%2BcAIRp4hjxlnkFqejlIQGvpa1ukOYEXQ0Z0SEjPtBgbulOQh%2BW%2FFd8DOjlxbnVo%2FTSIre7yQvPokfqabUVzrVuI2R9frk%2F4sZ7WNsTftMywVANwbIWORiJFiHhPmRImtU%2BeWD%2BuzwrGe1JTLBAg1GI%2FWtHJjLICJmfsRKqXrUX4wzWTIlYEmVwj7BIDtYA6hvlE7T4LxxWRI%2B7A3yoAfziyrp&X-Amz-Signature=5fd1a2bb6fa9fa3394106e7a45849f1bbee271ff8ab9e0a36256cfa7bbd17eb7&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P433GDE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5KepvVvUJFuTZTSJGVAMrzNVmM7GlDI9vJhnckS5W%2BAiEA9xOMe9vrMVPc4A0HfGw5XidMHCuo3fkbwokBoJePLU4qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFkZfoEDcmv5Sv7vJSrcA5veb2RsxX6cWxTtmvwTkVG2FSwcYcpah78N4UArPwbcD8QMG2deKv5UXqSS0nX6NZ20LFi5CRwHNwqPvwXHCwy7eZL7mmsZovDNQ0SbWkhcWgSL%2FmVSxwclQi8BkAogGka%2FfYhwEVmegc89bTZNUhNOTUoOA1l3DXVlEju5Dzs2HAbJMJaIY4sYW2YiEVDI6dISxhCZLU8sJvqUbECeu47g77w9zAYw2QvS%2FF6dlXgIQ70amqjxTawD7RR068cIdBcYEkjPeWT82yRbXZmAv8dJaWsFnkEnGrqJiPfC7j0osXBteRsJKtzXYdbPhUPGsxDOFT1jXJ6up2sbVnuy2rY1%2BfKP%2B%2BWuNBfrROpX1%2BGdh%2BYEEmaE%2FESynEU8EOPnno3muWuFrHQ%2B1fz6HvTeP32jvYbwcqZMOwqKnDcK%2FmMPH4bjd73FCONlCxjLeilsewBEZepX6BE5Qh7jbClRGm2qFNG0gK6BJQEnlyx70X9I%2BM3ejhoQxf3jBcakA7Ab3J2R%2F%2BPqVB8%2BmwpjVpVt4nY1Ym9E%2FNo%2FrsJaY4LjytdK7R%2FIZ%2B6RWN1kUBjjeMsb81T9vmtXUOPopzVPVMCFNbjK8Y3nU4qvmPPvZ%2BnlSddqtGdj571RwfB4xth9MNXF6rwGOqUBota947YCtzeiBgoi4Nhmx%2BQjLU0iuMBIIWuGtNpqiGBBegALpOE2FtJUBaLO16xDtP1uzUhkZqOF2V%2FeTL70zVvc%2BM1PaWGWoYD4QP%2Fq251sxUFfCKz5OJJjiM2g%2BTDlIVLmFfWOK5I9bQZA5iyBuq37JPTEdErXMW3mT44rSfDtiVIsJgnn9Wei7FCakuB2zfw%2FPPBzlOYz2FV5BGA4OE1D5ycs&X-Amz-Signature=68c0aa9502e91daab692bc6c8352b3c2a960ed88adf2fd77a6fa192868c484ed&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGUF5B4M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNr1refzdRUq%2FVvfFgDclefCLA8ChfiOP%2B7HXnUJCpYwIgJiZpsS%2Fpn%2Bz9vDG8iX6MOj1pqpwUYOeWGVFVS4p82KYqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHNNpeC%2Fo6OTpzJgQyrcA2KaAk0fKvE9wZiNRexNDLqYaGtofIyprDtXiheiRsc77cUv8Sd%2B1m%2FRcJuGx%2FNILn3Mz9N4DvHxOWLitjx92ihxQo6MGvtWgIEgW13MYz16VsGWuMenHGq5cKw7yLgi8S1b5fv7M1EuRHe4Ob0Imn2lMcquweoJYETtDCQLas0wGNGaVr6DoJThuCMz%2BtcuY%2FoVCmZOXVsHsrhOehnEnvRAWnFOKcoOeQumTcY5wmPsTY7jns0CJTLNYwFWDMZ2TtZPubK8TeA5d0iHn%2FqIWy2GuXcc1RCPWENfHOjxpUjg7jRFS89R4XvzMhn2Q4Z5iKIQ8lANgtNLZ4%2FKNFD%2B2Hwa8OIo9b5eq8Ui7KuQVwnHe733cobjTtY6nAKkTBdD4xeFYj906lRkxYBQrDNGUCR%2Fry65Mkaxlcgj2%2BcJAhjfyeCMDNTrrJKZdQj5Iu6wbUMmg3EmhVbm7omqHSV3Hd2giS3LP1Tb%2FUyZG9qdtSIElmOmEyAw6442dHJditjX0G62PNS%2BDrmAb38%2BTX0733QImAkf5NjENFD6fP9g6AFBXSDIiFxkJQ%2BysvfyzO3AKlWaROxcZwAlgw1QMLmVwCCEvSrlq4n0sQFpIGTyvziD9nJdrFMTmM6t5HeYMJHG6rwGOqUBTvKzWZHNcUDG3lu4ilt%2BslyhBd4gEn2lYlVOYf%2F65GGcGUrFOZsmPa6cn562mYMe%2BiGYCGIKnxGlkkQSfsGUcmA5D0UFI3BbsBLnWsgXmC4iHgjItcPkZiL4cmdQZB1wMvP3jx%2FAB4z4ZaQNxg%2F0uOHoH%2FKVaaGXIGIe%2FYHVHRA4UX54drGaLAvoCX9Vw%2FclCmyACRncYvm%2BQ%2FKIAV7i3KOFtlbc&X-Amz-Signature=0d5dec02a29049db66624f86a8c57f27bcb0a8ce3e76e26a2dc67e12f2f0c9ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWF5P4F5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDH1q07lFEO90sHIGPXDnolWgn2hFIbiCnsJC59w8UnJgIgJ1mSGIOhegXxtfQk0o2IFxevQavGNpar7%2B%2B90Zwf0Z4qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGxWdlmV1CT4hlKfkCrcA1McHtkULpA4mI%2B7FhI3byaz%2B7gnD6qHyZrtX1iSNoYovr2UnDG8RxD9HIFTCh4UOfOBGdtWQxCtQPdsN67Rl0UuNvBkVoBz%2BYpU6yuXpRgW3xHmIypIIem%2BrfKybdvcIafag9hf2pzD%2FzcubEfbhfwAHzemmYdzIx%2FsaIvIEI9zHgbx%2F5cKWuF38H3TLTU99pKY3RRQXs8j9S2G9pGSM7CTImxzjPyZG3xZLeW%2FlfdwO1ozVhfA09oRDGtQ6e%2FhfnEC0U7Od3gSKSvEUCqQICLhBeF77FVC0Ho3M8v5cSNU0jE8dzletczaEz9sYsYe9R7EquN65d%2Fupo9cYowTq7nIvw2fUKwDz2LP%2BDSWppem%2F1W%2F9a3ttv37UOFDXAoPsIMdVub2E62HDD73x1G4ScagA5PRDJ6RoG0x9dS42ITuVgN3G1SH7n%2FRplUUedSiXOpd%2FREvs6haVozK3cxLBNqIkS9ijDHl7ccB1o9e4RbON4Oey8c0ZYKUOwbV7gqZwCj6jZ5ZibMrDMRagRgSPPTmMz%2BlR9zK5AjdDNBbE4w1GDF4JjwxT9fzXI17wL%2BzBu%2B7o77KSIIArgeIqV2oZIiweOCoD%2BN10dw0J2NEQoJIkmtTzQTrxWMT8do9MN%2FF6rwGOqUBYwfOacNZ%2BQpmNMFj%2FNo5NTY2JwtNv6Sn%2FsaVubOXvEdaBlInB0RVNB%2FdEI2qXpz3v%2FnqU%2BAdVG7mqtbMFFcufIIPlkxIYoceU50N8TKZ2KEXgHye15ZgXZz36SDl42Re%2Bh4CsqjC3EVDFyVYJx7ImXSuqpLILwTs%2FYKvnm45sOb30D3Tj8dU8ATQSzDsPvjcdMZUOShOsrGoqetMAf8gKfQ8MsFi&X-Amz-Signature=44b9faa180001d9f3eaed2bfd5d947c62e7b9af1926d1849963465db275eeda8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LFRUA3O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDY58gUPTQ1992pVmSvI79lHFsZiGVMUpXFDqmYKLsX%2FgIhANK0Gd0zpGkRKwYv6snkm1yNnTGKZdpAec5y5p%2BQrzMyKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2FO8RmpYfZUImYwq3AONqQ8qKvsv%2BCRf8QXWgpPg25Ece2BOe%2FHmYLfQFwj25JY5NzNRc5gwIHgmByf7AcnNHosLGV%2BSEA6aT1ot0ZGbH8hCVfK4MaQciUspvtAD2jywXuWkw48uCUdPLWbOmUbb61ahtc3UhlwkU6rh6wvIlYAfWaEkCMbG6EZPc96ItPQdoUhrL69PZyOsiQ8COkOdXMtB9pqJcLZ2MOWXX5NKZHlnxdNZZJThOsuUc4f8Ne2rMm2aGB0%2BRfZzlg7QxOPJUSS4QzEZtJn2xX3jjoqPp9t9neH3Bhysw%2FuSa3CLN8RHHq8hkS%2BTlhQxmwhqcVMKnmcNpwMyUqTDniPCsq%2BDC3VXgIQdVqKQZdu%2FI%2Fa1KzIOJQ9rgBZkFRE0MBw5gLtll1PFBpe1MZjIAF9FQrDUE8i8sn%2Fw%2BuihHklKoR1jlLXYbd%2FC6jg1rCv54PiXdURz4aRHFhmY5r91bKiP1LvgyEQ%2F%2BX6XkWSBON2U4tULlxIDqS5oIUN1JDHAuKBdUlsUH0O%2FJPT0LMlrQHV1O8cggeLf%2F1jhkHG7WGIdn1DX2JcAj7aZz4u09MN%2Fx%2FQUEpmIHbF75768F6IH2fgszoSf%2FqAwLm2d0at8N0rrARbkZWY6zUNaZ0XxSedZijCRxuq8BjqkAWqmsEDKudBMw0vqm8mNkVBRRzyoW2%2F1Wdd8FuBgHtjjbs933BVzZpVOTGYXi9BWMFsATcxDggkTXcF2fz%2BrFGpYtagBCnohP6aNpU6FobqEwYU%2BnNit71Dg44XS69KUobF%2FcA9mL1Ni5JjteJI0uEYiyUJxFWwG%2Bs51SfMEuxDtpGmOSBtKnpEWDxR9Q5aH4PbRu8BImLlViaeZPrcszZmvwdz0&X-Amz-Signature=6d0bf341ae849fa7850497849a1a1ac81cd962bea7b87649a4759f33c8ed0c92&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LFRUA3O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDY58gUPTQ1992pVmSvI79lHFsZiGVMUpXFDqmYKLsX%2FgIhANK0Gd0zpGkRKwYv6snkm1yNnTGKZdpAec5y5p%2BQrzMyKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2FO8RmpYfZUImYwq3AONqQ8qKvsv%2BCRf8QXWgpPg25Ece2BOe%2FHmYLfQFwj25JY5NzNRc5gwIHgmByf7AcnNHosLGV%2BSEA6aT1ot0ZGbH8hCVfK4MaQciUspvtAD2jywXuWkw48uCUdPLWbOmUbb61ahtc3UhlwkU6rh6wvIlYAfWaEkCMbG6EZPc96ItPQdoUhrL69PZyOsiQ8COkOdXMtB9pqJcLZ2MOWXX5NKZHlnxdNZZJThOsuUc4f8Ne2rMm2aGB0%2BRfZzlg7QxOPJUSS4QzEZtJn2xX3jjoqPp9t9neH3Bhysw%2FuSa3CLN8RHHq8hkS%2BTlhQxmwhqcVMKnmcNpwMyUqTDniPCsq%2BDC3VXgIQdVqKQZdu%2FI%2Fa1KzIOJQ9rgBZkFRE0MBw5gLtll1PFBpe1MZjIAF9FQrDUE8i8sn%2Fw%2BuihHklKoR1jlLXYbd%2FC6jg1rCv54PiXdURz4aRHFhmY5r91bKiP1LvgyEQ%2F%2BX6XkWSBON2U4tULlxIDqS5oIUN1JDHAuKBdUlsUH0O%2FJPT0LMlrQHV1O8cggeLf%2F1jhkHG7WGIdn1DX2JcAj7aZz4u09MN%2Fx%2FQUEpmIHbF75768F6IH2fgszoSf%2FqAwLm2d0at8N0rrARbkZWY6zUNaZ0XxSedZijCRxuq8BjqkAWqmsEDKudBMw0vqm8mNkVBRRzyoW2%2F1Wdd8FuBgHtjjbs933BVzZpVOTGYXi9BWMFsATcxDggkTXcF2fz%2BrFGpYtagBCnohP6aNpU6FobqEwYU%2BnNit71Dg44XS69KUobF%2FcA9mL1Ni5JjteJI0uEYiyUJxFWwG%2Bs51SfMEuxDtpGmOSBtKnpEWDxR9Q5aH4PbRu8BImLlViaeZPrcszZmvwdz0&X-Amz-Signature=9ba699d1310a80b960cc03115578d9bebaab05c635fe6f5e7e30166c17a44d43&X-Amz-SignedHeaders=host&x-id=GetObject)
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