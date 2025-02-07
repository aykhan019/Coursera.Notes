

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H3MM55A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCp%2B04m6YOD4af9BusX3IRfpT%2BZfLYaf05G4IEJqZHXSQIgGtId39h%2F7Z2wgYPLD7GVXhOea8xlKas1Z5nvGp9rNl8q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDK6UeQgiHzm3p4OlsircAxfWLWdsIrRtyqUAbWhEwWx9f2H%2F3GRpuPbIF3buVw0CBXaF75BMyDRUjv%2FZxgWc4jOjXl6LWosR%2F8nk4lhYAJYXkcTa15hxxPdZ%2FXHzS72%2BvlirrUx3ZKkmvwAUwvIIQntVg%2FblQqH%2BWwRfqXwlji5NAZyJ9W3XlCsvdUdOukLBu6ocN%2B0JnhRQUtwOIsWrYZd0lXNvFuj6Hd0KElXAAN4OveyrFRhi%2BMxvsBPfVNpbbtUvCgs7yhz5IJY8HGgWpv1F89l%2BdAjTSnMt7S7Sd69BrVj%2Bt6ty9yi7A9WBlGgvYW3Ox1Hl5HIfYMDQf4D%2BEepuCTPobugVPuWaO%2F9CelpgSaYGgk9d8DP2mpFWdMPqvTX2vP%2BIuRGjVHkSwY1i8%2Bl%2BQvfe0PHEOT8jTYdiaklX1WcQHgza6exgIB5FCLMOs0GHNbnH1iokiVbGw3vUP5ZeFBY1MdEGj%2BYjNbtoWI3zHQ%2FWo4xlIYawdmupGsF7pED1ENfRIOycHvDTimXfhgE9tMkEK1U1P9k4a1W7SlM0vDEhRP9toY1Uh%2B7gEKVBnjAHwlhwCKlStlewP%2F7YNBZ3qSeAjDI1o%2B%2FAUAC6RkKy5Uv5LolkpN1I02FoJ87m21jzbbBg14rEzQ3tMMX5lr0GOqUB9m6jK0%2FXZUP%2Fokx8Km8rIdAPXt1WkxzqbkY%2BSvh3pnf%2BPthmzm7LTcXR6DO0hkM136EmcenpPVvgpwkwzLAc%2F4e0njHjzro9uO3w1n3rdPzJ3CaEsb%2BaQiuDiVIIpZmNsIT9NrL4DFqaXPK47cLr9J3M138c7xzexvgDu6%2F%2BplVTS4IAN01OYmkTKKy92MwuECzfGlDnlnu4eyH3e3elebGDx8DT&X-Amz-Signature=6b4f711b2baea704bb5711332988a4a1b2ec8caaf92ab02737d95c8170ddc16e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRC7X24S%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIHwmhu7drC%2FvWowSH%2FwgfFACNq651H%2Fj%2F9s4Ft%2B8tswOAiEA41BZUG6xSxZzBmIYu3chfHKz4xz7Ro2u3v1a3hUADDUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDEAiXWCnSS1Lm77LrSrcA3HUBo%2FagjbmJpRbOAQa8FyZpbeyMSzLLycHleKYVZfL7BuUpiqVMPugnAXWn2lgOMZn2kx7FL1TY2MhEX%2BkFvYi0SmdnXhTa4HaKadhES14VGFHvY52bzF53dcIJPRETVElWIxTGT%2B6btVZNfNI85f5OeAVPo2vv%2BGyCZXIqgr1EHA%2FoysjKYYn%2BfmA0AO41JzxtpiUvHdfRPoXs3VzJlHPlQM0U9Gt0iCwK8eSZU1gZSn9Nr6I4Vb7nLklT84axnymAWg8alPcaTcDVIrg9lsjgVKar1CDqT%2FVFjGqsemOeTc%2BMKm%2FeqC06k%2FdOK26vPL6N9oCK58Lhk6tEoEaI6pD1ovPjsuBw4wZpzazI%2BSvNyGfYmzelAnT%2F1wr4RcQS0d58rAMMF5rjw7ILLrXtjNkhHM7v0NNk9MGS0kOK3PkEn1GINVRQ58VTVtzKANmG7mKfUCWodt%2BdUzPb6fqbrIb9Hs4%2BpyVv2gsHyVJ0pT6xUCUQaAW3MEyAf%2FU9eMxJJJFhHRMmt1ihaVKwYjMNVPIxmeGB%2BDYwNB03RLIB9z4acFmqBIxwLUv6yBBy7XTtJR8nPiyGd7wf6kvLty561WmHWbgsFdjk1KU6XxMpgP03ePdJ1Sfi76RLcOWMNf5lr0GOqUBAWk4HtsU%2B50r6%2BjTYNEzOFxwg1nTn%2ByuUt8iIO4VfGmFeM%2BgPIy7tRCG1yUK3d9XZvS7AUI%2FTyjT%2FrhiGvb3%2FOGC7EhIm6YvlfA0sujfwCgNrgwJeSDn%2BxGB0T09NRnIN0ZyjrN7%2BNvl%2BVvAsBRwEijziTwNBNw8ZTZlKSm%2FZ1WQFeeUWLJ0f5bm9J8PI%2BcuGAxFyt9fzUl5Ydys0736UMIsL67U&X-Amz-Signature=32dfecb6e7a07c3e29ea4c6f7d6e47096b8999ecbab32ac6ac9abbbc54908fb1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFIOPJJK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDWx95D3PcVbgJ2UogGzEUVCxyDfSoRD0tlaDSW1Ol%2FlAIhAL%2Bfsn831b3hoTCKRrEp%2FqcE0GrqbHyuzs%2FYI%2FApr44IKv8DCHEQABoMNjM3NDIzMTgzODA1Igxfhy8YF1ZK%2BUHnk%2FIq3APAekSRwauYtkoIYpXo9GlOseRPRB67NB7qugWNX19YgjUalD9zrSs1st%2B95rzUf0%2FD56XOfup2SGHC3%2B8YvFUjFZdM2tB7QytV9k2qQRytqgn1ngcYcmq%2F12ZiK4wJ%2BGRXR8LBo6Tjaxfz1uW9%2BM3w9Vu3193tb%2FHVgf3uzgm%2BwtWB2gS%2FGUyI2ql1cph3F8WRTskOO%2FvJh7SuEm9s5SOm4O3QmRVqoiuSJ7RpMI4qAvpjbpKAJ9mcF3PZO4meQ63urOtjwbrbIaW2Mv19Iy9FuVmoDbao5qRYe1EWHgLoMhxCoy%2BtP72Z8zLFLkU5EC2efH7nZ6GWVpHYce0pyNK9x0vU1j5N0vkmRWhqFrmtyTVqPTjfoBrZVYOQwjF8PtMfJMkW9jnnWYjBUtPJEgq098sVn%2B%2FdUNu5aTRcLfDGoHdlHIhwR4FRGrG8k%2FQKM5%2BHVDxSDVdPGwgp7BSF0ANEVKpC%2BlNtylTxysJnIWNnBUt80i%2FhsReyOuJ27T8uz50AfgTKqGRmBTm0c0Ks39CExhYg0zKdiymp6NGEGRcaJcDHq0oHPcJ6Llb6dAv3patm0Kz4Rh%2B3KS7EXlQB0HhpizPjurMTAEEodXcKi0USDYqR9O%2FhY9EWQblDdzCU%2Bpa9BjqkAbXdFpbcNmBBhw4iBlXvnAhFlGCnarkgpShsaOMJD9p7BkesrB%2Fbwil4Te3u4VcBtHCJveCbfyzqWx0afyIWgvUJIKBstlt3hDu4%2BxmwBShibSBhErX8Gy7zjG2RN522FPJ7xky6id79nSMAWXaZe9SWYqJCr15sHpL78LhoPfahTcNT4QjfzmNYF%2BA0IENJbgrwJJiIfqbKrzYqB2zWf9%2BlCKvg&X-Amz-Signature=91683e9b167fef8b6502b92de32e22777f8ef66cec156c0da2f06344e0c9c59e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI5XKXXP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQD5cMtmooZKWpuTWRKjTaTie6M19TdqHAzm2irOPaxINwIgXzecEolap9Bwq0Ar%2FlB0ZRI73KMp7TK%2F7vlskTKdOakq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDDuSnQFUbivw0qzmpircA4wN7%2BtDMIbJnz3ZbpYVkEHqq9eB3ZyoOgtNNLlY0PjPf3yAegjnj6PaUD2hLRMqT0cG3gXkSMTtUMFDHcPe2pB0u8UF3NYujAOTlhNJTRt2BiA2VOt5vxYmrr8SpSvvBB24ig5amzqBOiK5oBEgRHgDZ%2BKTYFFgd5uG13DJSMXRWhIs0XMrLfCdY9HrAnOWsluTDI%2BDodC56ybiB1BGqoqvzGu1kRTp4ucoa9Gae%2Fi5n383G%2BfCKkKRScGXcoZaEJ4jyhRqSCNrgLK5zfoD%2Bqi0Q4Gqni%2BgnzDUF7nKx7Vof7AsV1W0JYAc%2BItz1q5N%2BQ%2BLyEXHo%2FR0vFl4ZdIWmrSGrhPygAKF8JMV9r6POP0WZlWO2Z6t4rUXDq8iRVVlJQeZPPdjGx28QVdYkEtr8Xg%2FBRON6JjMQq9K9uQRcSk%2Bt0LQVusFCSrcbs9rfaO88bW%2FxZl5fVa%2FDAF7P%2F9AQ9Ums7c4%2BFQ7P%2Bxl3taQ5f4emG8GJh96v9J3PFeX4aLu4k9gaUWXaBwVjxdUyzbpQ2Smfa2k1u7R40W9efn2ldi8Xj8QKPVQmpD9MLjF7UrSXyFmD1fAXqJNeLPgXOWSgZu9ukDM%2B6O0vjSbvTrpIryz6lVaB1mSxhznEgwTMLn5lr0GOqUBeB08X2KTkMrW0j%2FuVBNdS8KpNBZQCx0VDEyRhSWzATx8WZiGL06Hqx9FKbzVsMS3bp5L%2BJxukRFvU70n40qnmdKsE7fDuRSZ7oCucIX3rzfaLfPkNuhzxU80fxOjlSNHfPxOj31CeIcdVpNNSOKm8cQX6vBFIk1%2F%2Fgr9hocwtA%2BX%2Bwu%2F52pVbyGu45xW09sE4HyZrFQlkMPvFX5U4rBK4tY2m5Pf&X-Amz-Signature=9296b2a2a7c590f5f02a66ce7a899773b528d97c7c5522c5c58cf995a056dfce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRZU4AZJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCdkcGy2E7QBILkSr9mvhvAOBanztlCWlB73ykuF%2BNawwIgJsj%2ByPlzuhUts%2B2KaumM7h4wmjEbA3kFQ0fhEzBLH%2Fsq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDPcRMTF%2Brbx5OuVx6ircA9SQETrD4nykF8qLjtxZlET%2FaaPI9z0pkQwrRwqmRdbzqVZmcreDy5OJb%2FFY4nMLgeTFT51mRtbqFPmkG6sWorBgLdqsfkqarKr7Hp%2BpE3LwajiTd7E3matDwks3BwDwSGkZI8mgp8pjFYkCgdNHS1MY6NRqdWItPCUOFc0EuU7kAVGcYjcm%2FZFcpdkqshqhQv%2FjTZlTTvic5YtA7FgS4qk12ufmZZJ8E03HTsKu1yI%2Bz2LR2oKoMSRzNdoYAC49ZjMZF4w7NexEPPJbNJrqzNmvMJKYcAkxKZ%2FWiO586jZiBgOD8ASxOv7z4zC7S%2Bp7o8baHRcU37vIuOLoq11W%2Byj6j0L9PA75b64y3CB4bncEQQeX8bgslMEadpOiwUw3suMQPHs%2Fzp3xe52GfNgY%2FovhQNXOSoTFHm7HeQ1MhB4Vb605xvayTg7VopvMXAwfHfYJd3LdSLxw41rKg6sbMGozBmhZJFClm8zDTMKLecBWuw%2BD2Cu%2B5u5fZNPZ8VgxREVRPnNABzhWBeqAD6krFzhG7iFcDM8XAt01bMqFnZPeL1D5GPCrCTrpPw5%2B%2BXrU6XVPD16mwwzS5bfLKhWk811gTkyDhYfB5bwke0ILkV2%2By0yQF7W%2BgtUbBQ7%2BMLf5lr0GOqUBLdOjLxRMwIlAovWviKJIGNmJYuJ0R9e4OlRM%2FKxLzthD%2FFKsQT9AzRDNs9d9X6UD575nouEU6humEH8himSNH0cYIhlvO1JhEH%2BpUautrMQGDDsSlKJqOwQhgOksGlMCQyP87JIqWZolQsKPaWqYBX3bbDEFgWPhUbZ2gQQCRI1DOppsxf0vckf24lpeL3ZboXCbJjmI%2FyX7QRJGFcLN4kG8eakj&X-Amz-Signature=c946ff2f7d19c3c4282ff722b91d1202f9a08c02e8190e4997c025357625bb35&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWEC5JZD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIActvOGLEF2mFjIRw8V5SmIhjPvaCLQvtuZzDxYVci2aAiBZEE3Fx%2B0aar6A45%2BU1KpXJoAoko0fLs0TIHOwGlAa5ir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMU2RFUi3tFfyjCVxUKtwD%2BPqa8I6Ki6BYUG%2FgVrMZn5FQ8GA6nj58va9pkIY7wHH3yLdHfUk2B77DJ7LZISm01bsdlUOkJN6z4jKNW3H%2F4UAPdep38%2FoRznrq9Yo3kNkeoK%2FY3vwjsvfzl2FUB14IwmJI5xPW4bp40mtuQF9JbPJwLEBEHMf9cuD1l4%2BLlSdbldf9tpiT4EcONZ5HtgycD4T3oqSo4w01qWQ9mIe7MbjsFayE8W5deqE33ymZ%2FFMLqf0AZ97duhE62sZw2xlljtsp3hrgaAGrh8U2k1hjJi4VJcay20fjJG8lU0UL%2B2OY8SwEvXqp7HrJSessUO0F3sdcPCk6dZjCnt8OidcbW9YWf%2B4MkhVX%2Bdo2rYnf968VkEwv9wAHRBlAJCbNhdkZ%2FDO7O727tUABgU7oVlKSZ4PJfZH7M1iHVHhKVogjHjPUsL3qQlPW7oSuxh9b%2BrGe3BO6benxSGX6M95%2BDd3AmNxglGB2FDsI4nDfDLUREXMe2O0SJMEf%2BiyRMps%2FntqW76zBxewF5%2F%2FHTrJEFEnoLIzKDkjrFAixoFDZsslL9ex5gAscPjVpQnAYX2EivP7pOud66Cr%2BU1oLfWWPVR68dP9917iDzGl4uceZTnfyVbBinDRvlTemV1MafPgw1%2FmWvQY6pgHk%2BCMgZpSHRUX8PGYUBm2XeeWMRaQbyC0jBIQW1u1o2F9ThGf8QGL5K6WwU4htEhnhE8XBQcO%2Brn0SMLc5sSspQFkWQG5udc0AIsAjQCAqIA1uzHMn6J2fXXN%2Fnow4jlvu3xYRuECvd1pctosH4wpPqZ8Ya3pbpdVy%2BSCjGmmzsMic6QvxDAiM25rf1M4XPGOCu05L57iWrK7LV%2F2h9uHceLSjbESR&X-Amz-Signature=fb258b20187417916457ca7789dc018772369b31dc752ec3cc03217dca4decdb&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GMETZFH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDots72vx18sSSb%2B1dXyHnbHSL5e1YFT4pw81fqqMqhUQIgNlXqCrmJlVA5ZLqIa0mPx4pBKGJowPEkfGlzV2W6X3Mq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDO3xmzRSTUtogONE6CrcA1IUmXlVrEv%2FVXp2ySu7KznOF4fTTVhVXrVg96559IX%2BsCey%2FHaD%2BXkHlvZGr5VTNhv2XPmsu8pV28brM4EktszCr5yewdeQX9LLYHUrGfx3Q9M%2BP6wW6vQC3nH1YrLPXRE2iwSXSGYgfRNCxkydKujbUKx11yORTYM7WjKhYSqjffYsaUGtQL0NK5sHGjcfu35aVNvhQxPfReskHAV%2B087RpgIOxLPFupFokU7NOTIJ26XRanjgVKjbeZyn7oNQcGfe5h83xnuRk8fRsIW3UWt6oOHNuYRgoPgPVbv7PC4SB1xLTfahy3TPe0kaGRDa1KpP5swlv9Y9x1AAR7wsmlfvzeoCrY6Rq4d%2FD6YSOzNBGuT9Ebxzqs8%2Fo461HdhP%2BhYww5%2Fc3IQDyw7oTKbr7oMLRyP90oO4lAlhkrZE%2B%2BHYzn%2FnfYroAqlkmMEw0kXe2I5gYTV3M7Al2TC91QfZNBpnUVRmFzFGOLOERXXi2fPVnYlvOqwGVXEad%2FtB6N8jEvQu0l1GGmE3c6WOmNtvm2Ugb8iDDzYbX49pnXnUb4ioJW9KOHrXKZIkddXbyXs9XF1koDEAa%2BLZstOwIxuZ9ru91A%2F%2FYTXggfME3OEtpyK2eKFbJ6vDOvnzjS%2FnMPv5lr0GOqUB4pa%2FZE4qnGUifOPmWF0Xjf2npPI6zODR0zPS9lgi4ZiFSiRpGVXO2GasO%2BANQfGdfdbsr7PkPSuVuTxl9sVmGDd1TsGUkpQUFfkYVu3l%2BeGxjMX6Es6EULMmITpFU0HQ9vrHEtF1fTFaoqQq%2FytG1Aw19glpEF6sCdYWYmaT0a4A6zechkGJdxzhYuZ1D6T%2Fg7PUMZI9NW4tw0kAXfYCXdyHImeh&X-Amz-Signature=52ca43d53cff1f9e9e48ed4d20c3fd2b859b78beec70a802f9371acd50768a39&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NIPCIUY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCICnlYpJxkvojlRaJlc0yOgsaS2c7oIHHI3ac%2FEVcfgAuAiEA%2FO%2B7A8zB7GAewXcPZpaVSWAEr09%2FaLxf0MA9Hbch7iIq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDIQQ2mA5I3LWjeQqTyrcA2Dx5dJ7vA6P4UhAFYwtp8%2F1ymctyvSkxEV9EPr%2BYq8j04LzPCNJ3rtVc1dQZ6Dijx%2FvvOx357sQcywOkGLsDgXBomigKjNCHLmlIX0AKAcF%2BHFN%2F%2FWo3k0Syy3WyQS9W4SR5x9M7XPruA8qi4uwgC9IhpvOa71vjQA0trRYuktgBGgIIFJvPsKBeRk%2BTjAxU%2Fms%2BO10zQqhJ1RAqgqBDP3aTl9v4nPkCtTSNqc3cJxywzUFIR%2F%2BmLZJGkpV82VM7e5O%2B8rL1rDBXaZeHQlGYTLqMjcopEUwDcmOkJhMOyeJIe08yll1ry6Uj4nDPw3fTviLD4sregjK4Na1skQqyxoeiIyA1459ND%2FlTebFiwdsym04XLWbRqQ8MJrrCtrcZ5P0xSSiPumkZOcNBiE5AgepRMxpiFpOuTKWZT%2Fjk%2BE5Lri30U1fBcf5fPD8f%2BMcRRmX0DZW1osZwZqf%2BpqhusXpGhdVZXJjQuKM1FzB%2FcKmMzQmcAahwh5%2FCRz8KruNFHD65j%2Bqbln1MG4hdhpZ4cNZw5yXoOp7UObd122zUZ0%2BHkybEfy%2BG9CvTQY8Dly5MdMxyjhaNSfshQTDvQsx3FLBtyvddZKURvr%2FM8t%2FQwZs7LfWKKxL2ddc6TmGMLr5lr0GOqUB15xOdNg%2B4v63VobdiWUh0Apo34H6Jh5fi%2Bn00O4Z2meO6oVHITSpSvVJxS7oSrPp2m8T9caastDiZwUmpI3zqbmvj0KPCYCF0zg3aea%2BJlVN9DFTC2lVX%2BuTc0%2BbHrjky%2BUgaZfoa0VSbh7pWLPjmG0igjdJHLDru1DUstNMuxH2Zu0EdKzBQmvgwDt6ipR6qj5rc6QkKUznPX%2BkqtzkLOBCeGRs&X-Amz-Signature=724900588b9d7a6eecb71a26c15cb51dcd5d3bc9550859cdea581bfcf3d9e68d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRZU4AZJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCdkcGy2E7QBILkSr9mvhvAOBanztlCWlB73ykuF%2BNawwIgJsj%2ByPlzuhUts%2B2KaumM7h4wmjEbA3kFQ0fhEzBLH%2Fsq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDPcRMTF%2Brbx5OuVx6ircA9SQETrD4nykF8qLjtxZlET%2FaaPI9z0pkQwrRwqmRdbzqVZmcreDy5OJb%2FFY4nMLgeTFT51mRtbqFPmkG6sWorBgLdqsfkqarKr7Hp%2BpE3LwajiTd7E3matDwks3BwDwSGkZI8mgp8pjFYkCgdNHS1MY6NRqdWItPCUOFc0EuU7kAVGcYjcm%2FZFcpdkqshqhQv%2FjTZlTTvic5YtA7FgS4qk12ufmZZJ8E03HTsKu1yI%2Bz2LR2oKoMSRzNdoYAC49ZjMZF4w7NexEPPJbNJrqzNmvMJKYcAkxKZ%2FWiO586jZiBgOD8ASxOv7z4zC7S%2Bp7o8baHRcU37vIuOLoq11W%2Byj6j0L9PA75b64y3CB4bncEQQeX8bgslMEadpOiwUw3suMQPHs%2Fzp3xe52GfNgY%2FovhQNXOSoTFHm7HeQ1MhB4Vb605xvayTg7VopvMXAwfHfYJd3LdSLxw41rKg6sbMGozBmhZJFClm8zDTMKLecBWuw%2BD2Cu%2B5u5fZNPZ8VgxREVRPnNABzhWBeqAD6krFzhG7iFcDM8XAt01bMqFnZPeL1D5GPCrCTrpPw5%2B%2BXrU6XVPD16mwwzS5bfLKhWk811gTkyDhYfB5bwke0ILkV2%2By0yQF7W%2BgtUbBQ7%2BMLf5lr0GOqUBLdOjLxRMwIlAovWviKJIGNmJYuJ0R9e4OlRM%2FKxLzthD%2FFKsQT9AzRDNs9d9X6UD575nouEU6humEH8himSNH0cYIhlvO1JhEH%2BpUautrMQGDDsSlKJqOwQhgOksGlMCQyP87JIqWZolQsKPaWqYBX3bbDEFgWPhUbZ2gQQCRI1DOppsxf0vckf24lpeL3ZboXCbJjmI%2FyX7QRJGFcLN4kG8eakj&X-Amz-Signature=66e2af6730d67c7894d4c639b11034f9abd122616f8f3407d641ddc7f5e79e7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ECTEPPU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDucM6dp6mm9i4WHUvA%2B9XULIVnipZlnbcROFK%2Bb9hKlAiA%2B28UHqKK5DzC4Xwotjeb291ZxPxXFF1aCVyjVdiHoFir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMogDNBYH0H%2BqyKDKAKtwDLnFQlWlJ%2F8CKt%2BalpPGTSceYi31J1hVrrpE%2F%2BgBiNY9UDAATclpzPPT8eQ9T%2BLogSbHDM72rC8xdBJQfUrHtMDguCg95QUkqfQBrmPCxIsFiLLqLM0jiCw5w8o8cDMteMzzMaFYr4XU3uzxYosX%2B56OruGkDB7FCe1V5w3uuW%2BSNDVwBWdJDuIWUACneYbh%2BGnD5wLardSJ23FOBJltaRo1HjnpMbDaFqUOuLjBOR3E7qHOKLjDh8AlJ%2B%2BFip%2B11iw9RYCWXGUFZ9cEVMBGc93Kq1xDujic6piiubflswQOFiVJarHwI7rSdhIQ2N2x9XvHvdu56ZrOWXmtnvAiKRjxq7jrmA0lJZAPGp9IVP%2B0rX5cjG7teOUVV%2BV3KEHUHxYLgbL00xxCkcrqn5kafB87kv2zSGL6u9XXyWe0JlPOIg1dFA8QO92nqP5CYoDpP8lSWGfw11J%2F7gC110wrH8dwuu0bzOP5M90sq%2BcU%2BUt9b6xKii0SWBycRch9s5v97IqnfOxCyr4QsL0ghUtJiBFJYl%2Fv98aO1vydqg6PQ74EJHXPALe7WSidyBU%2BlIMja1Ya73CAmXoKn8Tk6tv53BmUCvPnedS37yZWW%2B5rWbyep%2FKW%2BWXCJbSXo%2FGowg%2FuWvQY6pgG86uDn82hi%2B3RR9xvxFMCC0uJhn7h7KzD4qD0fc0kgbci8mmnVy4kHdrVGBuikgSqvPPtRfdH%2F8gLo%2B83UXUZ6dATO3BHQKT1QUDCU%2BgdRszIFEsppYmrI%2F9iCpATn7cFjeAgOGzt8ux0N4%2FknWiNaOEhm9tguAgf0TucAHTELH72Z3pwQFfttnFYIe3%2Bzf8i6brfWRSWncMyQgGwerARIyiDENsbO&X-Amz-Signature=9a7e9d96fafcb2fbd921834dd7dfaea37e6c4be4f961cd13266d0ec6e324296c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ECTEPPU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDucM6dp6mm9i4WHUvA%2B9XULIVnipZlnbcROFK%2Bb9hKlAiA%2B28UHqKK5DzC4Xwotjeb291ZxPxXFF1aCVyjVdiHoFir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMogDNBYH0H%2BqyKDKAKtwDLnFQlWlJ%2F8CKt%2BalpPGTSceYi31J1hVrrpE%2F%2BgBiNY9UDAATclpzPPT8eQ9T%2BLogSbHDM72rC8xdBJQfUrHtMDguCg95QUkqfQBrmPCxIsFiLLqLM0jiCw5w8o8cDMteMzzMaFYr4XU3uzxYosX%2B56OruGkDB7FCe1V5w3uuW%2BSNDVwBWdJDuIWUACneYbh%2BGnD5wLardSJ23FOBJltaRo1HjnpMbDaFqUOuLjBOR3E7qHOKLjDh8AlJ%2B%2BFip%2B11iw9RYCWXGUFZ9cEVMBGc93Kq1xDujic6piiubflswQOFiVJarHwI7rSdhIQ2N2x9XvHvdu56ZrOWXmtnvAiKRjxq7jrmA0lJZAPGp9IVP%2B0rX5cjG7teOUVV%2BV3KEHUHxYLgbL00xxCkcrqn5kafB87kv2zSGL6u9XXyWe0JlPOIg1dFA8QO92nqP5CYoDpP8lSWGfw11J%2F7gC110wrH8dwuu0bzOP5M90sq%2BcU%2BUt9b6xKii0SWBycRch9s5v97IqnfOxCyr4QsL0ghUtJiBFJYl%2Fv98aO1vydqg6PQ74EJHXPALe7WSidyBU%2BlIMja1Ya73CAmXoKn8Tk6tv53BmUCvPnedS37yZWW%2B5rWbyep%2FKW%2BWXCJbSXo%2FGowg%2FuWvQY6pgG86uDn82hi%2B3RR9xvxFMCC0uJhn7h7KzD4qD0fc0kgbci8mmnVy4kHdrVGBuikgSqvPPtRfdH%2F8gLo%2B83UXUZ6dATO3BHQKT1QUDCU%2BgdRszIFEsppYmrI%2F9iCpATn7cFjeAgOGzt8ux0N4%2FknWiNaOEhm9tguAgf0TucAHTELH72Z3pwQFfttnFYIe3%2Bzf8i6brfWRSWncMyQgGwerARIyiDENsbO&X-Amz-Signature=89234605b862135a871d06190119a390d6727d72a0b60adcc2c7fd6604443c03&X-Amz-SignedHeaders=host&x-id=GetObject)
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