

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROS34CAM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQD%2B1cgg5rwbGQXBYDR9GKNICTTnMaySgbxvzIh%2F3KkuBwIhAJTlYx8EWJEEiTeQ7bFLfevMCmC6nwAuJWEHs1BKPG%2BoKv8DCDkQABoMNjM3NDIzMTgzODA1IgyNJOKKoU5GO07FINQq3AO6XMhYr9hzBgX1zluBl3WXB77htN22aIXnLdf%2FklK7VjY%2FQCdYj9OzU9A42O0%2FIVmOW%2BS8CQ%2FpkfNQQah1wCr1mLvyCDgZVQVFT0lunLEfU1c6as2bv6IHZexHPgk6gvQEquYFRox%2FZsIsHDZF3waFxkxSRyt%2FMgCxIjv2WvnbTJT0FX9tzwzHCjN8B79Y%2FNt%2Bwiwp1DqJRA2WnDlfzOX8QDWSfyHE%2ByEgv%2BOlS1JhnraeOa2oywaM0G9OaBEo%2BaL%2BgJRjXp1UvA7FvWJt6L0r8uTIt%2F6idL9WM4DBOS8OSV8uw%2FkvLUGG1OPwqnYwokQ%2BAH01mQaP8x2qSIF%2F3QbsP1qNGX7MZAVuWK7T%2Bv7AL4pg%2BaVS4BfUUjBIAQtzEwPFjMXu1908L0c1s4RcJNy6iUs4wUqBx6Mdh%2BqbxkO9VrCQmardc6q%2FKOHkskSoQs46V3qJ24OndLjy3LQU%2FSbvvll4zv2BwRrdN865o%2FJWlT7sW1PAAkWME8%2F44tUOluOtuzZfZUrBcXK2knu82zb2MFhl6TPlH8C7UkjOMENH9ajE804bSM2bce2MkIe%2FcZiOSI6Eof1jJIcEdJiFrMKgE4Zeymj2aIkRzlWNZ9GvWcvohu%2F655%2BOQNS0JTD7zIq9BjqkAdlEjplt22kcnpVzNRJFoKr4ohD7DpjvA7BZ6NuUASPzlcdYRnQOtRK%2FSIbx7hYzExxbohi39a0h2fIEW%2BJ9U3rzxUm0akU6FtV41w72YR1ZuwzUQpcuWN%2FcqSvwSaJC96rnTVAL7iyn9C9sQqSCV194OWlH4TFhCckAyyB9qIzP7avZKCSFfZEKbsNtl3rD%2BzH6%2BkmWGiHoNpMv1MM%2Fxom2kDQH&X-Amz-Signature=ec6ba287b134c4cf737591c255143c1a60048c6701cbc51ee340229743f5efaf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSYKCEKM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCTwqh28%2FV79nfjmo6NYh%2FS%2BlqU4EWzQgViMrEowvPWYAIgauuywcfeIFUjbn0aBRV3fPPTPuun8aET4U3HsuUmwRkq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDHsS%2Fm8gSCbCKieAjSrcA8DAEA5NHE0debcGy1xs%2FXudCVXr484%2BfiO5gEvuwum62xFB3uZj6O4FsuCDv9Hv8T5rAVaCRVHj44hTf%2F8p%2Fwmyh6Qiv6OltTg60eKn4Hw0W0eU74k1Y9LPYiIe7CTwHVem%2Bdwat6ao2N2ILYM%2F2EOmDozbIBXv5mwAwZiUIvvV%2FWSyaJp598oR%2Fm%2BFdQz90u%2Bwh2qnrHI4zNzedXZBeFdXLaBBt1g6ZKu73vuOrtRgN3sY6JAjB4aRVaaMRZ4oPZIv8g7N7lVHQETMaX628ow6qK46xaqoSegChkiyfe%2BGRviRMSzGCRZSnfPGK%2BNI4hKprIQQRJq5W5Qe9f71JXFx5OE9dQGKIlFnYq7VizxtFK7d6zkU5nyoQc23AIMVvfdIneiyL4gyIBl%2FeflelD2%2FuXTTQLPJk9KQ7bOTtB%2BdOESza7hR04auxM0r3%2BYJsuYuTNF90fhwDZB9ZiXFXiPihK6pbkvNp21zrjTI%2FvrsE3XJ11DiK8vNEkOatCre5zq6v0P7eJ6DG1iw8GgS1nmjv8aSEyIpUvwnLNhWNL71nSMAqwaXtjPXOkDQS4JXcbB1z8luRFgXw8U83CypGQ6lerwTlgb7j7hmdCdtRZTqa%2BM5CXGPvsPkpsX0MP%2FMir0GOqUBz%2FlT11xQrXDSVso2YrzqWv5Un9PNXw1VUMKeSNavjroEFMXYJ8GNQCvNRSfyIlrhzTXdLUCqJU%2BfImhdD7C0zigt8s7FjfB0cl%2Fk1C54azlv4mo2pNW68mcAaJc8%2F8oJXEtlVynLCJPhQWeYe9n9Ud%2B6MR3hh3SZ4tpX5yl7124NA%2F0UZG2sTtuh62HEmviwTtBbAJZDkpE%2BBdo9qKwzNot48ZJZ&X-Amz-Signature=ad4e4cceade97fcf098261a45508de8e0c963328f212e39d19b7c41bc2972806&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHX3HPAR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICV3fax6ks5khMP76CSbGHfRshJYmJjBl1VoWcEARNgvAiEA8jYVY%2FACtXzcW6c0fgMfCNzVxTrHLtcvBfhrTo%2BQ6KQq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDN3zqbC%2FhZdqhhSe9SrcA7NGolpp7ZLe%2BSAvQLk0uN6uxJPR1XCTd0LC9j8Opm4mLV7iktZQbb7tJjVhfyY6vQhE%2FmgVU%2FY7kH80dKYaTkiL8Ua088A32Pb%2Bz8klJo5KMrB3P1oVgeeiDGnNalSO8Cj4ROOVfLeWtce7Bq%2BK0Idv9PMV%2BRK9gLDM3NmsheHDaz8lteBqT5TdiYghRHJugfcJcR7KMvSCZ29EkKIf591vVWK860ZlvQs3WQJeVCvKoJPORfNR0BdepX87nOCgBiwo1Xea8Dq%2F0Pm6efSYoFH4Q79z%2B%2F7Xv0Qh%2FJHqsXeBCb7pyIkmwAR8u1eVyjGOAQ1Un9eolhwuaYiJzJqeJtbBDjCG0P4qOoCozm6vv7KyVHIQ%2BOO56KxkyfskDhGpMFKkvEkZCaQAGyu%2FfFDuUTKFtyqd7VuicizfzXokB%2BGAar6aOrqlm1XHX%2BhWAPGRhvSAm3l2gAR5ugIkZS3uhMbYTq6OkeG8a46e7y8pf7ovqrptVUfH2%2BcOH1pNtckr6QechJmsAHWcuDywF4m1F6l5YdG8qmPNP9Z%2Bzj18kgpn4L2hoZF2OYb5JCNispQpbhMQ%2BI5EjaCVqQRVwSfx0UytEACMzA3ALXm8zduBH3PAXqUwRDxL7CW5Zw8FMJrNir0GOqUB8yg1Y6iXiLavcvProIrWJewXqPLQHwbv4GsAGyhzxG456c8%2FHQFNNrjQ5VdMhg0cOPPnYLPhovANNcJGzqt599VTFecIZ7bTS73jYi9izG9q7eBlRcIsR5wG14SsT4OoqwjQXCaL62yDfaLeAu9mCNAHyR1Skvw%2BKCBeHj8hSp4oZsQDLwxQXTWindWvSzTcz9QG850IfL%2F8V3J91hAJbaOhSfJ6&X-Amz-Signature=787a0555d8953939ffb4878f3656c20bd680f21acd9aaec499005f7cec57d248&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4M5AUAF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDBDifrEfOL%2FDRw6EYaW%2FnMeEjhXGHMsFHlnNrXf8pyLgIhANY%2FNY4T9uMluI0mnnHJR3bmeSIaSUUvZttRIoNyGIKXKv8DCDkQABoMNjM3NDIzMTgzODA1IgzY1bhyqc6fmn35aVsq3AO0DDZwwIoF0F04qI6JSIRdDeDq9bC2QA7GifvhVDJ5viL1rECfP1a%2FtHp8BIWLV8YD73zDY1yF3%2BBRLkzKxCcXq4Em9R88nLqSubsJKgENMOWYhyfrkja5wd5mmd0B67ven3LdSypIKDreo1d0Q6GophxHHx5v8dNueGHmtGn0I0r56MJm0Aw2dARbzWRNLmqThWHr2CfMOk%2B7Ku7x2YYSFbIL5Y1NAv6CBLKfKYRFDYzRO22nA4wBym%2BF4hE9i%2BWb1XX5JfJc4XT7%2FniadKiUIuBRIaDA3Dh920Jc2SlhD%2Fxz0onLVRJ9OKiFaWAw6%2B52unJZ9lqw20EzjO7jy1rqRwBpLHKhWJPL%2BRJap%2BF%2BG5%2BC4uYp6WdUEDPHUQFGt5ADfqg8PthuuEMeILPtcIf9HoWrA4G9x93SFrxsrM4HQnCL%2Bj8Byaiqi%2F%2BPsCn%2BkL4zpkljCunnyfiTNzoIr95F2hh01Tm6Ir23mkn9xqIoQjUk42dc30zU0c%2FTm97OxJa6NvvJieLFzZqfbdgAoNsU%2BX3oFk2wEO3rSiVeLMTZ5aEoQvIGcO2noqPQU3uoPEySXNRJeq2thnc2hLobsQCRB%2FUG1bFWNUy%2F4u6sFxCslmv444YzFh8ZBQdMijC7zYq9BjqkATJEhvvPEH%2Bex841pqJQcGBUQPx0HABYda7wTXVP0pJoPnUz23V6B%2FCF%2FovSVgJdPLw4UribvcovVxXEa2jjsYSr0z7NrAfncAEVttwI1A9RoqwcZnOoRX0e32KwpiD1EUSjElvw1DijxJbDPVCo9cRuQHMHoa9rnfvbQN%2Bi7MzXnJQkCzn%2FkiI%2Btg9pveAgmvpZlqPa5%2BtQqf42Zt2y7y36HOD%2F&X-Amz-Signature=c6d6d1e5b0c7e5db8b147fe72be148e33a83e81e3dab6b95fb2534849ae78530&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BUA5OVP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDrLjb3q8E5aPLaLhGosFbPSkAE%2BRxJWtexD7ab2abu%2FwIhAPGHb2OnC5G6BmmWevSIojTE7Z34QjWyZOs8qICSLFmlKv8DCDkQABoMNjM3NDIzMTgzODA1IgwY60%2ByLzRrtMSf4c8q3AMRTSVI5I1QKTrE324H7Gz0xVBzFyzHVlN3p3OjHjeRQOXGlLpJY7%2B2ACSFv4wVTvnOLV1s9%2FWk6YUReAeRK0qyK6P0%2F4S8cBh8kaqgiT47cFzl7swnwJUT1I3xML%2BWEDr6VJRctQf1ExD%2Fk0QRvfl14PSL0X7bq8SmaRFksDSsF3xce2bXtabTbQMCYnrRkGJhQBBA4AsWzxhLRLm%2FRTwRcs%2F5cTqdj8plIUkeD1X59KqiFixRihgpJNtdgezuJ3%2Fcg8ITCOS9S9BupW4KaVVxymIpLrYBuWXKTL%2BuFwxkdgF5DO00%2FCJVIay1EiGUgcq0xDbI6BiUUC%2B1EAVBDL2p6kW2gm2nz6qPGD4Uu0YKnhP8PWRRUopJGZLlmYbfUwKMvqgK3VOzD7%2B7k%2BXfTghsWqFZZHunZQPXPYAUdj6POs5e9xuIX3sZ3Gjkv%2FEmUP%2FuaTJVlVHkzwTv1GBkyeECuA1v%2FsPwzXm3BNNy2aq9muHNVrEqscSNs5i6sGAqMb0pHcZ75LfeWqY0rWLcbZ9ILU7DNM0JWwWsKUuMePWJS8fuPJwKcrwCzHFq0wH3ATaa7IBSelnfu9Z7PEVY14fT9KX9QBHw6j7yXJ0cMo1TuyuFF3xqVDJGKLpmCTDwzIq9BjqkAY%2FbqPITdxMtUVamnjkfWMroIp%2FWan0CD%2FfpazGLYNmtxvHY7ypkykCCgVYDdrynjqKL9PDCNXF6eF%2FnxRYOzDZQyy3YxXUI4wPSciX9Ybp9LeOzLdEgieyV0FbTlIAM7ojgaEocp6e8YZ0DEEI7VwHiB2GMXEiMQbdzvG%2BIUQ47Fl6K3WJguXDD9RfKatUVHoEnD%2FK5l8sP8u%2BNxg%2F%2Fb0romcUa&X-Amz-Signature=719f1b373ad98d9e44615d52480ccf46ca1a03e49dc1976dd1cb2ed25476a5d4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KMZTTMN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQC%2BMQ%2Fj%2B5I8iCKkMPYPDFIpLGBTWUiWXKr%2FesEpXyuDhwIgSiFxaU4nEmX%2BeYFBWTifWXCwwPVWGs5J%2FuZ8vrt%2Fr5oq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLBnN2FjCmg2kIUNhSrcA0gIp1r4Fg7vb1QzOd2zmjOg4tGlAnMRwxgEkEipqTg6FIiJ2282qcY8FI9JmR4EuTblXHwgljMqx44Tkt3MK0rjGYTwCJKmif2LqQ0e4qoKOKeYxA2IuZn38Y%2FTfnVDOfUoouK6xtDefkT%2Fr5B%2F0F5%2BpaiiFs44mLdJP54OTyfEI2RTFOBAdDuf79KMkR6BWTGljjo1%2B9ry%2BJJm2tIakZWtX8%2B0HRcdwnh8Fgz%2B7NuZXRuU%2FU3QAKKmBe95LvB33fMnWhJNm4GetkPcEH3ZDv%2Bf7I116igS%2F5fMwOGjBLBQkkmvg1KHch90GvtNtCGif7hozcg%2Fs2bVw0ZK9kf0u3uMrrmQLkLwoktLCRzmxWdmjvspq5Am%2BcimhUQxQmOgV0iN1wKH3HfopouT371jUqWZ61sdEfUhdJhj8y1t37dC8GQhSZp%2F7RsyC48HHG0QiVFf3X9lXO%2B4YQjYQI3eFVM8aLZr4vRAaf4Ok8PEenkrfM6MF%2BcdfaMZBLGb5NlcFOP%2F59o6RFh5SY8V%2BcW4n8wpApxZSvxBhE9E2vhYOKbhajKjPpbRvEJcmkWJhgJlsFw537MOzIgcmPJAuRTX7xQjQ68%2B8zrfG30Evf5kyltf4MCQoF6LvlBF5ITTMNrNir0GOqUBsmkuUlpmBxpV3nCqmebhsmekEsn%2B0qF9KI3NDbfGxueq%2BW%2Bypc0yX9s1j8CXSL7437%2FHPNqgB7QyCeEcRd%2FoBrj1osxyTxknyzjEDcan42lYHNVVlInrRzWP7uZYmDGHyBYqUBh3El945pioAoplLPwIWUcqkyYE2wqj88c%2Fcr9vaCW3YwmiqgP6rBbCpGX9fb6auA1ZRzKGIClqS9xH7%2B3nZvm5&X-Amz-Signature=5150881907adf4932e46e281e74eb88f70dd5349661e5c4e311aa5eb4efd17f8&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FLOVRYF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbf%2BuisxZZFjXMY%2FtD15ungkW3j7Adtw1jSFbbqeJX5QIhALCIvnyXFhDp66qw0hocDxTp8JXO10FvbzCHz15iLgO4Kv8DCDkQABoMNjM3NDIzMTgzODA1IgzSa1y2X3Jt7xY6%2BA4q3ANa97aQO8J%2BRETAF2RZrcVWGodMYepcT3jNp2Nxj2U8TOWoHgFTjunFLqUXowxnMbGsBS66mEV6RO6VgvNpaI7sSLujAAkW7iqOmva8Plp9FVWIfE31tPdpiLu7E11aohDsFbNY040V3PBa%2FJBdmIzv%2FAOyUVlxSgFscw3S1MtFF%2FODFDSKYQcebXzwM7x9dREzKVjCwIy9ZkTZW6ydewjZyPgNfzeLC5gYo%2BN6XCBO6uidg0c4o8KTNjXt7waHdB5hSJqDbnJ8xxmLox2V%2B1pXj1aJTeZXoK9n%2B9GyDttyKbB9kimrqmaI1d0T0HnR9a%2Frlq1agT3Ke7xaRksTnU%2BimQ0k8e17yXUCH9kuLNrOhMLqDZg55sslq9B3yKyafQyXFwXVgAzEAYWVw%2B22vzjCpJQ76hs5ZgY30JL0lsAdyZ4Gn77Cn6DyYaN%2BUdUDdqB1FikOKf1WOM7a3TbJnIdxG9LkN0V1ijWOE%2FIVzTO6f6jf9vmH3RwxG6ct1VIfghP1%2FcohIvwJAwsNH5MtW2LN%2Fv3Bw2CtlZQ4X50xvSZv9%2BeI21uL2coH5DORJRmnbkBgbneVmr5QUzJOassyBfcFkqbOsX795cVB66k0b2iiKDkUfGS6vrA%2FLM1WgjDnzIq9BjqkAWaZ4LUAQSUQwhVopONgyTbWk6Zd5I6jORBtW%2FMwd4TMHkx9%2FYp1qZKcJkUUOHK2dGqwqxMdn2NudN%2FsQIG5HtJ%2FX2sjY68YP6kch%2BzRQKoN70JlzN4LQ2U2z2z9uElnNqZiAeJbdsRqW%2FsCVRvxwIibd6k0zddstzgaKZ%2FVu7F35it8j7iMRqfNvDfNYtfK6vmmqjsPgwxptmNcFb7TOdY0wSEp&X-Amz-Signature=1b564b6869b94cadfe557d4916b94fcb2de08807e7b67f8264d5208b17b829d1&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQBWZCPB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIB7nTOTyovcEQveTldkMkvj2dEddTV8U2rJjeJ4%2FpG3LAiAvXD2tFs44yWH493PsaZBm9M9%2B3L1fLjNIuJlEKLdgkSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMpsjo%2BujqrEoSmahEKtwDmwypOCsIg0CA2QXRl%2FBCfXNMiRakPGV6Sm2uOk%2B4ZoTrYKE4S2HdzkhQML6SewiIqlsZLoYQdOVS8KNfk0DSKpox%2Fvcu2ArHCMUt9duZrgi1t%2FEMqufL2qvd66rQRBdCsAmNIBUZSZX4Btv9m2Lbm0WsMk7D%2BA9gqq4%2BQqyF3wdYq%2B0%2Bvjf5SB3UVTlJEatgsiM5hcCif1XM4xqCMTXENNPqR83PqFnWcWxV8L5ukRrQaqVO8VVcvStCCM5g%2BT6SU2tr3bwzbOgVJ1jp9lo8%2BxiKM1dvW6trgUt6soYraJGdGlZtxDXQyvmk7XW%2B%2B1EDhFpii%2FIYhZU%2B6PJSKQw7aFNVMl09iZnzBN4ZNSL3P5pCpMP1Q%2F6qulBg1xV6e6idRRuVhwRmqj0SXaKD%2BJnm%2FBCyT8vwVTcpoYGQkAWpyQuQ4%2FDZz3hGt2BYTycGWuDQ3iJ3JFdhQge3IT0R4fcOdV2mfQXWX%2FjnpGJLYM2KhMQDRar5o3v5GfqAYKVghpUOTf8QlNP1bghm4ZmW5hNjwHznOfke%2F9AL2t9OtzBxfppxCZjpQymDfpOQL%2FZ5%2BBP3BBNcjVuy7IpgjAbXzJ6rgL%2Fg0UqaIIA4N%2BQOyuNL4goJIePr3dJD9qa78y4wts2KvQY6pgHTHISM%2F8a3mhX4apqyDu8xP3j19eW2PqcX8gYsO72QaI39hHefTEB8pS2Pv%2F6VOZgCxNz84CAX0P89ebrV%2Bv3%2B7oJ5yGRxWewvaZttFRKyEmfHTy%2B48yUyC1r0XVwa5YrZpstiQoidYLP1rtCxMJyJgngOVq1ntKb2JQ3mMczXn4yRjxiR%2BgESE9W%2FEOAoefaJByvlo8pmdBI3%2BdQSTklJzFpY2iQj&X-Amz-Signature=63f20fc091de024bf9d081d98cbe3e17c88d427c8dc7fbc7ba92f8ae58ef854e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BUA5OVP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDrLjb3q8E5aPLaLhGosFbPSkAE%2BRxJWtexD7ab2abu%2FwIhAPGHb2OnC5G6BmmWevSIojTE7Z34QjWyZOs8qICSLFmlKv8DCDkQABoMNjM3NDIzMTgzODA1IgwY60%2ByLzRrtMSf4c8q3AMRTSVI5I1QKTrE324H7Gz0xVBzFyzHVlN3p3OjHjeRQOXGlLpJY7%2B2ACSFv4wVTvnOLV1s9%2FWk6YUReAeRK0qyK6P0%2F4S8cBh8kaqgiT47cFzl7swnwJUT1I3xML%2BWEDr6VJRctQf1ExD%2Fk0QRvfl14PSL0X7bq8SmaRFksDSsF3xce2bXtabTbQMCYnrRkGJhQBBA4AsWzxhLRLm%2FRTwRcs%2F5cTqdj8plIUkeD1X59KqiFixRihgpJNtdgezuJ3%2Fcg8ITCOS9S9BupW4KaVVxymIpLrYBuWXKTL%2BuFwxkdgF5DO00%2FCJVIay1EiGUgcq0xDbI6BiUUC%2B1EAVBDL2p6kW2gm2nz6qPGD4Uu0YKnhP8PWRRUopJGZLlmYbfUwKMvqgK3VOzD7%2B7k%2BXfTghsWqFZZHunZQPXPYAUdj6POs5e9xuIX3sZ3Gjkv%2FEmUP%2FuaTJVlVHkzwTv1GBkyeECuA1v%2FsPwzXm3BNNy2aq9muHNVrEqscSNs5i6sGAqMb0pHcZ75LfeWqY0rWLcbZ9ILU7DNM0JWwWsKUuMePWJS8fuPJwKcrwCzHFq0wH3ATaa7IBSelnfu9Z7PEVY14fT9KX9QBHw6j7yXJ0cMo1TuyuFF3xqVDJGKLpmCTDwzIq9BjqkAY%2FbqPITdxMtUVamnjkfWMroIp%2FWan0CD%2FfpazGLYNmtxvHY7ypkykCCgVYDdrynjqKL9PDCNXF6eF%2FnxRYOzDZQyy3YxXUI4wPSciX9Ybp9LeOzLdEgieyV0FbTlIAM7ojgaEocp6e8YZ0DEEI7VwHiB2GMXEiMQbdzvG%2BIUQ47Fl6K3WJguXDD9RfKatUVHoEnD%2FK5l8sP8u%2BNxg%2F%2Fb0romcUa&X-Amz-Signature=d321fd878752ec231d935ab7937ee86360d98100683438e1fd757737220d25f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB36IYQG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIAHg0PtKJVDAutwLX6zsZ%2BAklbTdvfUBWvkDF0UzWvCUAiEAvSod22%2Bgu1nve4v6yq2aREqlSVjldCdLq6NF2i9ijAUq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDOxVdUsIoUp4eEfZ7CrcA%2B4QIf1sYEcv%2BPCHDJ4g7U4vA%2BuYOB3U5SRZKP4stUbzlGxu0UlGerLu1f3d9%2Bv%2FyaJThRMkgMysluNmm4MzHP%2B185xkXLHjXl4NPZ7JGAZO2nxfM8DgMiviQyRdDLJYyhdW8T5bJowsJFdjAHJEOJVZ1omg0vhd7riF1v5yHowfRsyfnaRKaIFXbdfIDa9SgoJV%2F8s%2BPR4ovLeuxqVZ1vqWiPJOPMoDxYi2S4wctVkPft92dID42wIqgb%2BGoMNdWKsgYSlh9ft1QO7ugOODmM9zEo2Q3A4P%2BhJ5XinLqL4N4wzXIjfDLKr67TLI8jtjQQ4mGfLiyc8fjSqH50dQd3Lxr8ApHK5pqHbPQ0dgxIFEfXcEPiI%2BjjvSQtEzaxnecYfbfG9zKoCp1stxEDI%2B3%2FYbZjWLD0%2B379j4v6Umwz6PveRa382ZH35QeOe8kWsapSSmQt%2F6KtnUat1nyGFQoALYXb%2F7Blb8XHqf5brSMDDJIrmeWiK3qboQYQUEMgZADbmluHGcuM%2BRlbJ1ePZzaC2OjFuUuQIhmicHh%2Bt2O9HTgpgvGMu5k8kLccR9%2BwouQhcV1LFnhUUCDruR8%2BZ4g76LlUiwmz%2FO9%2BUdWoly0%2BVoCxfZOnF8UUyusAf0MOnMir0GOqUBYEkMZKU7vfUw2Lp546vl6sKDmGiPtxkV0eIpMd0cq7w8nYdSnYKSeLzV%2BaT0wUxrtYunHaZRbHGAAsJw7fObszE867VZaCrOTzMpJBWNrPu6tr7il%2F2kX7CCYWpU98PZo6ZMEnmGFKrzLSChV9eHWIQH4FEpctU76PTYqTWuCWg9MBvOZW9x1%2Boa1vvAdCJHJ7qwDLmPLEFKV37CAqtl1MtkYSlH&X-Amz-Signature=918c5db9f47ba6abfe715469132e4f0604c7f14b6a94edc4e34c5c3eeb6df237&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB36IYQG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIAHg0PtKJVDAutwLX6zsZ%2BAklbTdvfUBWvkDF0UzWvCUAiEAvSod22%2Bgu1nve4v6yq2aREqlSVjldCdLq6NF2i9ijAUq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDOxVdUsIoUp4eEfZ7CrcA%2B4QIf1sYEcv%2BPCHDJ4g7U4vA%2BuYOB3U5SRZKP4stUbzlGxu0UlGerLu1f3d9%2Bv%2FyaJThRMkgMysluNmm4MzHP%2B185xkXLHjXl4NPZ7JGAZO2nxfM8DgMiviQyRdDLJYyhdW8T5bJowsJFdjAHJEOJVZ1omg0vhd7riF1v5yHowfRsyfnaRKaIFXbdfIDa9SgoJV%2F8s%2BPR4ovLeuxqVZ1vqWiPJOPMoDxYi2S4wctVkPft92dID42wIqgb%2BGoMNdWKsgYSlh9ft1QO7ugOODmM9zEo2Q3A4P%2BhJ5XinLqL4N4wzXIjfDLKr67TLI8jtjQQ4mGfLiyc8fjSqH50dQd3Lxr8ApHK5pqHbPQ0dgxIFEfXcEPiI%2BjjvSQtEzaxnecYfbfG9zKoCp1stxEDI%2B3%2FYbZjWLD0%2B379j4v6Umwz6PveRa382ZH35QeOe8kWsapSSmQt%2F6KtnUat1nyGFQoALYXb%2F7Blb8XHqf5brSMDDJIrmeWiK3qboQYQUEMgZADbmluHGcuM%2BRlbJ1ePZzaC2OjFuUuQIhmicHh%2Bt2O9HTgpgvGMu5k8kLccR9%2BwouQhcV1LFnhUUCDruR8%2BZ4g76LlUiwmz%2FO9%2BUdWoly0%2BVoCxfZOnF8UUyusAf0MOnMir0GOqUBYEkMZKU7vfUw2Lp546vl6sKDmGiPtxkV0eIpMd0cq7w8nYdSnYKSeLzV%2BaT0wUxrtYunHaZRbHGAAsJw7fObszE867VZaCrOTzMpJBWNrPu6tr7il%2F2kX7CCYWpU98PZo6ZMEnmGFKrzLSChV9eHWIQH4FEpctU76PTYqTWuCWg9MBvOZW9x1%2Boa1vvAdCJHJ7qwDLmPLEFKV37CAqtl1MtkYSlH&X-Amz-Signature=9c0e5fc7e0597738027d87353c588ee779fc87e11c2a168faee87107e6f3e346&X-Amz-SignedHeaders=host&x-id=GetObject)
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