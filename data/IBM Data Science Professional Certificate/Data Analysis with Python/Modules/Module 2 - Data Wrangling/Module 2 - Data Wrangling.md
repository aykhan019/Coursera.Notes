

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647EG5DJ6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDiUJcG4woTXa7JIfqwka91S97lO1s0FcATHphuTqaW9AiA8jtNrnxVZDvHLZhZ%2FThUeonF8xcAgKPFe3JuDhIyo6Sr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMHCRlX6lu%2FrStUJKiKtwDY15zhcM4mk8gYBNSXbtsTRE7N9mSioroIwojfTZzIt5yBnub6sRkS3hBybCcs2wl3GHeK1BSBn2C0A8HyHYqutP8caVlQQ1SS3V7VPkMw23Ux6Jv1%2BX4%2BzOgoiTcCR3crPelktjuCzaxq2wAIQxHQ%2BGceE%2FKPksjt8xO6SISvoKMYhPS4b7zNTrEfVPzht0SZRoz39g09ZuiY4vmxrnW8wdjGTEQcCtHFbYv9VukpWXTiY0SPPd6WnxJg3%2BaCJNGZJ8v0fjx%2F8KPSd9q%2F21L5OWLb1ZosP5wS0jD4ekWZg%2BN4EZLxKf4cqqGYsUwO3W%2BTt8HGZ5A9jUJK64eJjjdhTm8e9chXRIaRZX%2BVk%2FpPaL1%2Bdrxl0WLkCNg9jMP3RPJGnA1e1hoTyFj93KpVERZSXKHWVDKs7%2FKWENAiFpBTLsZcGJdZhVIC5FVEdCbP6Y58oA9xFCnYqEQC7vthdgYezz6VKzhvXW5pzLPObxYvkvFqwL2APq3DXrvgfpYAktm3PHDsp6bOx85Y6Adn0EMPIsKNMSW6LVZiSnisdajw0Nb1KI%2FY7ftcJI4KaKSiyF0lZn8XJJkCKqkUE9Zy%2F1aPtO0LIMC8F6YPgHZM4wzI93eRWSwpyHDBd8OfEwwtJSKvQY6pgHGIVWcHuOv65u8JaWHfcLi1dUlkyv%2Fu2piZKMFd0yNrQClWkZG0EJZDP2PO87BTgQvw5BWzZZ9O0MukOhUl6Yt3emcsA4nIJPLFwu5Zfb0KOeP9MHFldHYw%2BXt3UJIg%2FpH2q5Mo1FveEa6sUUO5Xf3ZhT2XsrrKNYSyztzDxCWeiHcGEEIorrfbnoQE1nX55ZRBtIl5LRyq9%2BMdNfyJq9VN8o95NV5&X-Amz-Signature=64401ed77ec835c089117889a33ddb97918ce4f99f8a9e4fa4e8453ca8e7c586&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HEOA2TL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDfD8S2uIsKYLhTUOnqd0QkdhgkfJwF2%2FbJ1mLd9h1olQIhAOhLnkvaqhLGDUK%2FHUUS%2BlvBvBLLtfyDBb6TSRKXZpPDKv8DCDcQABoMNjM3NDIzMTgzODA1IgwfgXrdv7EKQiHCGCMq3AMkMr4ghNfn6NAEI%2FyYXg6KwKiS52YKWJWu6OfeuyTz%2FP%2Fk867g1M6bDXJrJrZOzpp5PsTSBVXdyTFjsdekKYpFvEdJ8sIt7ymtPIUvT7euhAmvJS2EUPXeTUz9dN%2B2yvTsL2kruu4eBhk3pFzcMSfqr0g9lYvJdm1oQUeRTjkLBH2L4014QbxZmetGUGzJQ%2BH79BtJEJ%2BMLUpUnAOCoqmHlMIiuhokpFILWrY2quebTdgCO5NlbPQ0ZTe1zj%2BNPKjLX5vPGlBFUYxMVi07lzaVXKxf63P8GN1Ej0uQyX4bjuvKYCVHOdCZetOJT4M0nevmTfzE5IXieh2xxX6RWLHuxRUZ0bSXRi2tVTX6eJAJjLT%2Fjh6Tywk7hXfAncewPldryOv2yvTGt%2BOwVWUpI%2BZUX%2FrEO5HKvB%2FBOcwq3Gb4PVhhscMFrjg1D9XAM26y7CxcTL5TH%2Fd0edYkFjgYR3NDBaSx4Js7tgqt9N1dRrPMcsWuucEZmC6pDkQ0YHJxErf6FjMWsI8ocW26Npl2kczeVHpE6AQe78OIYnWEwpWB5Ly7WOoiYjv7XTyhv6Sb%2BNH3Wl93Bl8hOiu0cInh6Q15Q%2Ff%2BPiziuqzUlUF7pBsplFTkBneleC9g00qt9TD8k4q9BjqkAXO%2Fk2j66dBkSLS%2FT6oZCcZN8HaZdKvlFspjtjRSZOS1x5WrBfykBkN%2B%2F8I%2BTrGL1YQUAqJlBPwHumdTLMsIwF5WZTa191aMaftzrb9OvSfzhlKP6dFil6U%2FyVIn6BDhb68BYZKQdRyKCpPHm8dvAsb0U4TK8zu5GsJuhR7Y%2Fd93RO1Ps2HU5fus%2BPfC1Guk8ekX6IX7d%2FdX%2FWIZwmeFByPE5U73&X-Amz-Signature=7d7f6ebebadbf96639509d877b1f159304efe35c127c7a309b404b16909d3143&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AUNT2EJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIB0Qv4br3HCaJKtSG2bxSmy%2F0Rm8iGju7v1n4utWzRjKAiEA%2BDQKo%2FFvazkU73OXF9U%2BsQGF%2FTw1nalJbM8IMal4RDYq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDD8rb0Xag%2BROEsMVDCrcA%2F78c5dF4cx4B0nSphXCWnutBye7cEyYjP5AA%2FHy5q0r5PdnBVp5XH7eMewLFJIAmHjnLPgVko8chTz4hiTPTBEkjTT7kHpBlHv6hMMURYRWr2qpcZWD0m8EyfyoJggWmUicyXc3FBCWorv1OQykzakl2MOXSlO7f6eCQmlsK%2BPNkTpy9RHEgFMY5zduLR58g0jlKx8JqJvJ%2BF9C6d6EPqRUVCH%2FvJm8xGHQL%2Bi1B1zgboZ%2Bnd6hVTS23yjB5QBEHYdqzoDeJkno5ZP1qymIsj4fA0SGyCfkwpD%2Fdbg%2Be2CAzvjTLW%2BQfMrM5f6rrzuDReSS17L69OLo5f%2BMVKROBf2ftD8FGMC%2FthId0NGUTZUO%2BPXmYHwk%2FNIZt%2B%2Bq6GJ17t%2F6bzsUYcehzmCiqKF%2FisUAcuNSfbUo0xn9LRxgXTGgGqUEpvqF0eiTYTMwuiX5n1O59Pzl%2FWoK8jTC%2FLDB2%2BBlZD6C%2BDzEas8OBNUcq%2BKa78EHKhzK4CwmW%2BJtOlvk8V9hTSiKwrX38ertRpZY5Z6DTwEsqL%2FIaw9N9V3nfq6HTUAocGu%2FJfVtvc1lRU7LGWwGGHLw0CnWmUlQHJAXvuw5E%2FX7Pw4ueFtYWYcjH%2BmcjekOxVPsBVoWJ8ZUMOyTir0GOqUBZo6KUIl7FCHKT46QREcwDkucD0gII%2FEMhn%2B0JqHr1mUVvLham3kUB5%2BV5%2B3rJkHt2KUdsEbEWguQaQVhCcDebYW3Gna71SFIpEWh4EjPQW9baxPN4J%2B99%2Bpu%2Bj%2B5CBf9Vks0MVuKg1NwJk6mVva3%2Fw9EpP4u7zXMN2ESLbiAuUUHQ95gIJqGehJl%2F%2FncTS6AeAGrc0VyAXdsCGRLHf5kQHcbQZn1&X-Amz-Signature=5047dab310af210f4e0642964872f94673fc1a5dcdb8f851e7bb0665c4d93828&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBPLS2FG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIHqDtsQD7NV4Z4Vwb%2FskJVdRzDW7252LaFpDV14leFhMAiEAhga3TnAvrpzQhmO3UVN58L9zXk2KxKZGDxJq2m%2FFzcMq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDCoKjjp7z4MtffQudircA6IODDy62%2FgiP9BfV%2Fv%2BQPFCgX1nLn5R6XPum%2FAEz%2FwVTWteKKN3oX5fVCdC3AfrsMOWUeCRDZ4NirURdyCf%2Fzzd21crcyOaQLQWro0RD7ZYgUhS9j8RoDRZjGVzcly2bVoOaw3lwDvQ3wlKSFXP%2FO7WO34XzxzYgoN9TFEfCfWZ8r4cNQiRBahqs9VPGG9VpTSXkqTyaUmqQaOpylbceBJfzeccF4Z8RzilvvloMlSSXO9hjRZh%2FhmKBWQgNcNCxD1zjs3Bpk3o%2FlIivGATfhAuky3cNACfZNFMNPeadxIWa%2F3ocCGU92KXK77GyUCQknpNEiJygHrO67n3huPAql%2BpfdnSMMkTlwxmP54gh5%2FYcSKs7eUqg8Vu0M1dbBLjXnQjzB8mWlqKHCdBunX%2BFCgmMhSXZd2zmdoK5IJVxmC36yc%2FhlTPrAw7h2%2FJnfniStOTh3%2FeK5fjQoOMONoApOHJV2wOJbliEThI7Y%2Fiqxl1hqwIh7FO90QoqJ1xNvY8NBkxpv5k7bevbGxoAo6oU49ZyF4s8R6haVUDa4P0wIVNsTTG%2FS7%2BOLrYnUHU1Tuk0XOBr0i8n7ae%2Bg6GcDseD%2BTBrKWK10FrPELQCXedT5hPbARBLBGZwUEhfLygMJ2Uir0GOqUBwHmDfgBSABipYXLHxS5eE%2BTKuvowlCIFUMuSw%2FIp3dHXptkqG4n2Quvu45vKl48e4DxGAZ2WruWt9v%2FbVkn3yHz6pwuuYR8NlJm9wE19R%2Bijuk2ehDMqCJAXYpcl2YtNKQDhq55DMXSJtQARxYfOAU2HOVxVo0muKL8K0ALFgD21fOpRJuFNMPm41eG%2FKncxtG%2BQQ2duwWAukTbIZ4IQ62srKq22&X-Amz-Signature=2e4eb4078879243c0be70f035b5ac700c953bce9fcb2937a077a20b0b7d0142b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMY4RHK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQCUW9D5Evx%2FRBFPWUTvR5Igo8XgNKAAnVkkCGgqsb0qKwIgECFJF61tnkjVg%2FqXJui8hGugmyLqeoH5LXilKl%2F7Cwgq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDKMqqxaY%2BSydA3jbhCrcA5iMH27C9tOhciM52J5RzllXycrsMV0rBboIxTzLKKTAK%2FfabhzBEVm3Rl%2BI5GmaXGTtXJkm4pXSzl%2Fghm6VWTj6enbxlBZfqASG%2Fs2tYjTcABtcFuO%2FXtcZ7kpnmDXHEvM%2B93HmpI9WB2MtlzcQcPnom7xb1EE%2B7t9lFUzhED6Li%2BCi4kDRlV33bQSVrILt6txwmxM24jQG5dQm3WQ03qNRDfDEAvd3yKzCaLhFlKh1j%2FsLkbzIJwMHQuhQELTS5Gjvt4JUCBrDi3ntatsuQvrKirUQHmo5aCFqNTPXbY9GycrUM4MBQ66qL1%2FIAcIY4IUeXe%2F6IqwkOGP%2F5j%2Bp83aeUQdr4oSbbj%2BFKqBX%2BiY%2FxTKor706CpUtgJKz3NxGz0PvlDdFI0ELN8PgUFFVaAPyKcmC7%2F76pVuShBEtXL2jNjlb5FVMXD95RfEuU%2FIplU2iKAhp2suYmbRJC%2FT4K7d1iP%2F7It76UFAAStLOUsE8sdD%2F8INHdBFAIjw4VO%2B28X%2BizYna%2BmOhtcOzf8jLD35oB5uFjFcSo8aIuUxAd3LRyNOmOAWhI9XnL65bRYRssxxZ0mIb7o0iwX4P%2BQWtgM4FJbgT715eEmEUD%2BgmZb5hhqxOz2UUS5nFZm%2FeMLCVir0GOqUBAm%2BaiU%2FWpxXat10l7hP6BUr21AfnZ0q5kTCNyu%2FvQl6%2BHy%2Fcd6GsesH0zV4CUpTcUNhOKwDr8c4X74gEroAwtUhv0dAtn8NTQ2iywof3m4XMfIbsZvw6wAqcuJPlUBZJHQkbs9Coe%2FTesvvaSglRR%2Btpj9DWM0mPra3wFfWq309LrxwSGzUrOf8Fmg6Vbkw%2B%2B0iFOaWK5KM7KWwlNkc9PD4LBsKv&X-Amz-Signature=e93fa68d85936b2506e7097434494f1b2f2a0af519ddefa286f158ac08fb2afa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6PSH6SE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIDeyoQFYe%2FUMxA15MTskj40Npnd2YQzHaqL0Wo8CTIn0AiEA8dZPMhxZT5MOsp2jatncmX7VggGRs5y5oP30fJ34IhQq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPdYu5IEPGIIsEjakircAzMj9ik1hN5B%2BXy6%2BAUwjok4HDlrIenHhPyEDH%2F018p1Va%2B3m7qx2XkXAmujoolizfJpBNT1RmLuNlgtgyKM1dOnfkuX4kgNJwJtc3bTb1cpKK83w8bP%2BOht4G5oXrUGmA7PRxNcd%2FgW7SpIUaUaFaCFNWPmuCICV8I%2FptUfi%2BumCUaIbljFT7SQf0njzow3XOIK1d8oM8KQgNtHa589hGm%2FoFtrdQxxZBtlEbZzhJMK%2FLin3YgSRAPjIqNMCc6y1O5Med8EULytGv6h0WEOdVkZWtKE8kvogXD7KYL4LFYPqr5APpBjJHSbJQFznNXvUsbR%2Bh3nT%2Bd0GnMEbE4PyocHt3ynT2Sd3IkYZQHLLKLxFgr%2F9lYQy4ZUU3E9buU9sdlhgvnxawZcaeX9B79q7vJapcTSelciKZ%2B8CUeDf4V9xuCa7vswY%2Fmjre9KWgZFqfiHz9Gyb5fgbpaZLKd5eohlmqcv6%2F0ZzrIZteZto7kYacLDIm92L1HEomFbw5i7kwPRORbiAfjhjLx%2FZRCUvryYDowFDwa3DUg1yO%2FoGE97WPQq1YnKJH4iXFNbUpCfBbuiY2UamMOrKqgQFRG3Cs4Gl%2FkEtWQ9mNv1ZJBenXF%2FJUNH1R4G3wyMw6QTMLWUir0GOqUBbgyQkJy6mYzNT9Sjm52r2y%2FuzWIpwSPG4lPlh7BeoZrLqBiBYoH2ZXlyC2iA4SViZ4dlwSeeNixUcoizJ599AZdqbV1qVAHYoXMbhB95EJ6LMLVzQ%2BuqslbJJdmvKg8S3Fjxuiwm%2B9hvK3GolPVzsyV6zNlnI%2FtP8S7aJkrTaO06zCoo%2B%2BNVSzawcfRL2Mg6VAqPQ9UtrjJq%2BxWwajxnR5Ue3N9s&X-Amz-Signature=dacdcea26c5c8ff84722e4f4b106da0775f569af454b8652ad86c896efc1fe35&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633JX7PYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCsCr%2BgC96p6SUIe7FC2Yq4JqVEjZEHW1mxLadNVf%2FI5QIhANs%2FvCJet5XXW4y8LdERyFjGxGJUpONtbPQFC1U7H1pZKv8DCDcQABoMNjM3NDIzMTgzODA1IgxbX2mZJprCAm%2FY%2BKQq3AN9a3I%2BOFqighKM4NkjxOnCii%2Bs7AJto2MymQkOlxoMDcSwAs6judEpiw%2Bkya8Tq%2FZ%2F4OJQr73TdfQKL5vzJkEySjCp8lp7egXWEs8KTziGD4tDtUbSPNgVN9UKaN0ns83hhRc0s38GPj26lngW4aRrk9nJCEb7IlsXrW75X2seDp%2Bl8EMN6b%2BnqTcCoLh8hk3lx3kZDvrmN3Zdut8BCNFFmzkJ1cQ0cabnE29%2FkSKwVb%2Fd1ik4vjC8TUK%2BrQ2%2Fv5OEPq8SooLocYbYJdNgx3%2BSUwM2Ul3yO8fgevp%2BehAOCjVitvVRu6fZFyk2jBcrFvJVEQwVCh7kkN7l8UXvW8yooGaijiBH6IUDKh0kMe9SlMVRjRcYODud4KjiUzFZENggKrx5QKzXLdHrlH3ksbcdXyi%2BG39RYxv%2FSYJFH6BKhCj87lMrmB8uaQ6sVDM5ou6c8HucKqWd4fJCfj4x7ZWcMEYWzBCLOh0bYATTbTV%2BX78nwBxs2HaZsCVD5gXdI6HkD60Qf0JpkTUZaHX39eS9U50C1L6Keccete%2BjpXx6sm6iJxXyW0%2F8pC0NZJonUVU978vjAGlo%2FLNmcCV3LtqYhH1TJrxqmywyJqTTOY4bzyCq9XkyZq7ks09U%2FTColIq9BjqkAbeHpj8vdbD8PpHbc5qUbRFVIj4gYvoB41M4u1kTd05N7z9j0NUxQBF78nl9yNqkyHTD%2BhrhrsrkRTWRhFUOzhodoVs2ohEYZ9e2x%2FtIEjflSCu3TSePk4cmTBi046NTjFuGYq0tdefo%2Fx%2FmdkEt3wTlIwBEGVi41Z0kmLa3y3uI5uPFeEDd7i4Z08xpT1crpo59A0mTVwzVoDDcNbA1mjob6dKX&X-Amz-Signature=73e55769130a624578ef2ffc3a3b4ccb039fab14be6c7eab96adb63f30d0602e&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7V5VAM6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQD5W1jpvnQeoa3n9zMng2ChiKRmFEec1SadtOWEawfNZAIhAOTcoAo3CodTyNFupYngmI7lc2cpluXGEhEl1v3Hg8llKv8DCDcQABoMNjM3NDIzMTgzODA1Igwqrbsypyt3%2BeFyIf8q3AO163UG9nB8kYrrNc7UNgMico2ayfiYORwpZOtJXodd0mSWicSOsWMllH5UvBoS9Wp5lFtv9UcNUEWGeerk%2Ba7kxiVWIjXtdaLBaPdYYyinVAiTZ%2FJ%2F6XPs1t87sgJiG%2FZPm96KutvoEH6yVt2kWGf%2FsRaqHacvuaiupZ30ht%2FkHLGF2kp1BLSygvZHC7zJGLPGKzLt5snAPR3CIEmDQrjaFnmO8jo3UAAqerYF%2BYAU13s%2Bexto%2FdKRsDpiSycA0WYc10Mn%2FIhjGn4LxT3O2bM3JPj6T7tgkfSZowZfQbVLwh3qZRGZ2A1WS93LZbt9LHvoLQOLC17Z03a2QJ7XZ%2FNPa%2FVRowszUF6J66TJfl9S%2FBA6WtyVtHpFVM4sWPUpX7p2qO5U1NACwA1hV5tE5ipFRT8t%2F46eHlwyeRmvQJRbpAQxOqTJnRQNTNqN6dmOAouH7Oa7FOd5vkCMf6BgP2FZbgIFdzRxzedxxQgp6B2ABlTpdn7a9hChBOaXJRm8WXuzruAPTSrZ8e8LUv4%2FiGCi8bkR1%2BM1mjuLmw312Va7cyPUMlK06trsamEZ9pQVjss5Mx4YbbnjYKNl8ri%2FdRhDycBAfV8J9msJtA0j6t8ZASLCIflzNX3Mur2NzTDllIq9BjqkAVQ%2BDEk6QNhOMWyiy3egEZdjJ0sYLyQHh9C8AxmhaKmmkB5tFh03NA6HpX5u5eCL23CTuyciiD698StsTTIH8Hv6mCEJaioqwXQy7mFMy1%2FD0yv35FZ6AMz9uvlCReU6LrAc7LXytIJ2owvjRQiehTr3eYdZ3aWqxwYe6UQupjSRr58pBYJPvcoHtk%2B3ARSHJcwHjIRZeNTzdrPt2MEvJxsi3HEH&X-Amz-Signature=8ba51caf1625642a3905ef40146f92f9946fc27fb9b8edaad9103b755d3c6072&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMY4RHK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQCUW9D5Evx%2FRBFPWUTvR5Igo8XgNKAAnVkkCGgqsb0qKwIgECFJF61tnkjVg%2FqXJui8hGugmyLqeoH5LXilKl%2F7Cwgq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDKMqqxaY%2BSydA3jbhCrcA5iMH27C9tOhciM52J5RzllXycrsMV0rBboIxTzLKKTAK%2FfabhzBEVm3Rl%2BI5GmaXGTtXJkm4pXSzl%2Fghm6VWTj6enbxlBZfqASG%2Fs2tYjTcABtcFuO%2FXtcZ7kpnmDXHEvM%2B93HmpI9WB2MtlzcQcPnom7xb1EE%2B7t9lFUzhED6Li%2BCi4kDRlV33bQSVrILt6txwmxM24jQG5dQm3WQ03qNRDfDEAvd3yKzCaLhFlKh1j%2FsLkbzIJwMHQuhQELTS5Gjvt4JUCBrDi3ntatsuQvrKirUQHmo5aCFqNTPXbY9GycrUM4MBQ66qL1%2FIAcIY4IUeXe%2F6IqwkOGP%2F5j%2Bp83aeUQdr4oSbbj%2BFKqBX%2BiY%2FxTKor706CpUtgJKz3NxGz0PvlDdFI0ELN8PgUFFVaAPyKcmC7%2F76pVuShBEtXL2jNjlb5FVMXD95RfEuU%2FIplU2iKAhp2suYmbRJC%2FT4K7d1iP%2F7It76UFAAStLOUsE8sdD%2F8INHdBFAIjw4VO%2B28X%2BizYna%2BmOhtcOzf8jLD35oB5uFjFcSo8aIuUxAd3LRyNOmOAWhI9XnL65bRYRssxxZ0mIb7o0iwX4P%2BQWtgM4FJbgT715eEmEUD%2BgmZb5hhqxOz2UUS5nFZm%2FeMLCVir0GOqUBAm%2BaiU%2FWpxXat10l7hP6BUr21AfnZ0q5kTCNyu%2FvQl6%2BHy%2Fcd6GsesH0zV4CUpTcUNhOKwDr8c4X74gEroAwtUhv0dAtn8NTQ2iywof3m4XMfIbsZvw6wAqcuJPlUBZJHQkbs9Coe%2FTesvvaSglRR%2Btpj9DWM0mPra3wFfWq309LrxwSGzUrOf8Fmg6Vbkw%2B%2B0iFOaWK5KM7KWwlNkc9PD4LBsKv&X-Amz-Signature=54986a49507ac0935267cecfb3e41c6033cdabbbb1f4fe9a504400c6e7013450&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCYRCFE3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDxGtVSCVehao5iUNASQJObAYIXbfTk2u43r2Clh%2BzFdwIhALh6ZqFlT15%2ByfEtXdyLqq2NmACob6IVNd9cCpBRnY8xKv8DCDcQABoMNjM3NDIzMTgzODA1Igx5nX058hPOTvCq2xMq3APc7B3kNhFngfqLTLsk34Tptsxu3X35Fi8Wka30PY%2FOcZvvN1LzvnbXv2Uh2ogMS%2FOkORTk8J4qEf0QHv9x0e7TxWi6t3IwlNWEZMevtlBtlVGLgSu1Sc0Zw5nU2KWcKt549noGq9VpAjPK%2FcpFTUhBu%2FEb3ooMaiRWvYRyN%2BpoLw9eWQkmk6Z%2BAGkr78pvQe2A7pMawdEU%2FfNWh7V4F1MugUDa8yPvJFthDWHK4leqeSBi2To7LzeUHaRNeSG9uwfnboXVyejwi1ECtJ43QZFuHUaoMclnMCq0xpjgNVQttCVw1OWnOFmKZpj8zqatxWJLzaFQvlJk%2BH2dhOMHjTvuZi%2F0SzwsJLtXzJRU93Gtp4wz6nFkJlfnpViCqZixanAqG33eABz34atUvkv55rzyUr1Je8VCqYiavSkVtMx57HPXuRfZqNxeaO0YwKsQy9S7MGly1zMBkBzopnbvH29rB%2FdGvuCgl3DPaG0pUBrjsGF9rCgvSmRfjXL%2BQ39c1e3HCwwgIx2mXBg8wGJQ3niAZEUcQTO06%2BekQRGEcNcDtyONL1qYGqJ4YN1WXF96oWNY1zwj%2BVWmFqfgigdzZP7F1GeyHeaxiSN15xL%2FY97p5GMF8P8hUHJIwNucCjCWlIq9BjqkATfPE%2FHa8Xu0PhpC8Zp9fvCyGhfst83pHxQw711IEJRii89mw3cMK2CiHZkOYjz%2BUoYpgI2NNkLga4mLq7QBvS%2BluOq4cqpHYMeM9G5CnbV8qn3r6PRr1DkvPcPqjZAGxcKwdA8f3KjCeu4pk0pVKDSJH9wOERpwdKJT3xnd0nMyPDD2FQaES0g9mkT18grays4uVMEWAgXWRTAFzFCXYOCVuxwJ&X-Amz-Signature=61f167585f492af3949d5268905b61eadb215890ed77c130b9a31c5cd2a7d649&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCYRCFE3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDxGtVSCVehao5iUNASQJObAYIXbfTk2u43r2Clh%2BzFdwIhALh6ZqFlT15%2ByfEtXdyLqq2NmACob6IVNd9cCpBRnY8xKv8DCDcQABoMNjM3NDIzMTgzODA1Igx5nX058hPOTvCq2xMq3APc7B3kNhFngfqLTLsk34Tptsxu3X35Fi8Wka30PY%2FOcZvvN1LzvnbXv2Uh2ogMS%2FOkORTk8J4qEf0QHv9x0e7TxWi6t3IwlNWEZMevtlBtlVGLgSu1Sc0Zw5nU2KWcKt549noGq9VpAjPK%2FcpFTUhBu%2FEb3ooMaiRWvYRyN%2BpoLw9eWQkmk6Z%2BAGkr78pvQe2A7pMawdEU%2FfNWh7V4F1MugUDa8yPvJFthDWHK4leqeSBi2To7LzeUHaRNeSG9uwfnboXVyejwi1ECtJ43QZFuHUaoMclnMCq0xpjgNVQttCVw1OWnOFmKZpj8zqatxWJLzaFQvlJk%2BH2dhOMHjTvuZi%2F0SzwsJLtXzJRU93Gtp4wz6nFkJlfnpViCqZixanAqG33eABz34atUvkv55rzyUr1Je8VCqYiavSkVtMx57HPXuRfZqNxeaO0YwKsQy9S7MGly1zMBkBzopnbvH29rB%2FdGvuCgl3DPaG0pUBrjsGF9rCgvSmRfjXL%2BQ39c1e3HCwwgIx2mXBg8wGJQ3niAZEUcQTO06%2BekQRGEcNcDtyONL1qYGqJ4YN1WXF96oWNY1zwj%2BVWmFqfgigdzZP7F1GeyHeaxiSN15xL%2FY97p5GMF8P8hUHJIwNucCjCWlIq9BjqkATfPE%2FHa8Xu0PhpC8Zp9fvCyGhfst83pHxQw711IEJRii89mw3cMK2CiHZkOYjz%2BUoYpgI2NNkLga4mLq7QBvS%2BluOq4cqpHYMeM9G5CnbV8qn3r6PRr1DkvPcPqjZAGxcKwdA8f3KjCeu4pk0pVKDSJH9wOERpwdKJT3xnd0nMyPDD2FQaES0g9mkT18grays4uVMEWAgXWRTAFzFCXYOCVuxwJ&X-Amz-Signature=2dabb9657f9ebf60126597c4b5cf002389e31f3e6eaae81be5a057dfbd611540&X-Amz-SignedHeaders=host&x-id=GetObject)
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