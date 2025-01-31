

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFCYWXZM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEUWXEZF6o28d%2FOW2b%2F9AdCzh45STiFz3li5C9WL3WJdAiEAo4VCqn1e8gxhyf0%2F9oSF7edL9PcJH23Ewxs8hfFiV7QqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLnyxbqoYczv0e6z7SrcAxGBSax8d3fDDuaSkONcPQ4%2FlWezh8gpigTtk7wIwbj3DJ8JEIiBXiRZlUqAvcpzx4c6BAsZPDp6Vv440K88rN1tYqZ5pEaFMuPazd7wk0o1rMwSZ6kA6PA5q%2B%2Bhfq3m%2BFxqIEvvxSND%2FQejXJKV26%2F%2BtKQUIDGAbIeV5by6M5QwT3y985FbuHNOhaDbEcyGb3BPIl3MWodKdEsof4O0b5rYOVpeSTeI1pnusBTfDv3HP6Z%2FTQPhlReVz8LOGAkEIFgo9NpFc1kQlfPOsYBmazEdE9vX1OiE0izF%2Fld7tSeM83%2BDK18Uq%2BGOyHBIG9K6thgna4kpuypxp6cKCDR%2B%2BmmhAaJeGMCQpR84%2BJ5CFJtuBQMvg1o6UeFzeCx3b6WWcSceP2%2Fsg7i500mW%2Fezq8zFrYfAbU%2Fp%2Bdr9D8tr4fCgfInngJrBTbS33CTGeIzJSth6LQ2iKAiG6bww7lYlcyHMdEKyi%2FehAzd1l6ybdVekOp9qrstry5oOufhZzi0fy%2B0v2KZ8ZEtsojBVIFhCaAIHdEMc4JSx6vTQWYwTuco%2FsewY7qnR2eF5%2B117cl0XUkCPjn6zb2rhYIn3JTBRRCRfMXBBsoiEI32OLZM5uqCJBq6aYUdw44wiQAVQ6MLT%2B8bwGOqUBrCmfmkw4cOdDvUordf9ru1TU%2Fo2k%2F6IxY1WeBstTQ6j9fPnyVaqsnBAUdWB39e3FPVYMdQUDnltEKekNmEgdo1qeIyTCVSfVrvRguf%2FZYXBh1chSxsSbJiZ4M2Xc3KN%2BPpSUEg5XyJw56nfHGb9LBcw%2FxCl3Lavt5HuajiC5IGCoFb4D2%2B708bhmgK5vYOz1khOqOyoGxfiJ3eq%2BdlGCpBlsinT5&X-Amz-Signature=643f28ade9f3ec9d06e49de755e53b33af9a52593fa0c971fea480b394f02a0a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DP3XDHY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKW7nTF9%2Bqka6qnDCiAS4hXdNXsgBU%2FCSVxN93RiXPkAIhAJzEmk9XAdjGCh5Q5j42Y3fF247auXDIc%2FCuCgaXFq%2FJKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXFyy8xYosienXxpkq3AMPUTaDHPDV5zeYk46syFiyFFooMGM3pOiQ0qzlYIWyPxPRb3%2B05yDckVU4jbqomzXF%2FdwKEJzzj33lrZby0Lrwk0qx53UBRD%2BmZav%2F%2BU2BGXHkRuoM3NMHLwaR06fG3RmP%2FfpsNwIcXUEumsHpqshvx9L9afNr8i6VTiQIpzo6fckkMRiAJdBLBDpzA7mmcPB7JIv6%2Fced6bjqd91Rxw12hvAeV5WJrcdzbIsAwO%2FtVNEXpvaYbvRabEQDQiEagWFG4IAO4q6TAssyRuNJ7W4fNKu0X7baPBUD8%2FHc5bAnYavAdklfhgjquDRDpDWj8SGTwEY6LQpcW7pRyIko0sduOcjikIxtdUJJt%2Fqqk0pcNZPWhgSw8rOq1w6HZxdZlMeQskZ9TZp7kuUDrhI8ggwDZDPOcqP%2Bp6m4amLt5G2dU6DxdB5IVj7uM6ItHnDktaoH2xALpJUoHhvY3fKoPzweyYDykezjrILNvnwYiCwrdT1aEg%2BoERaaW7VtiWs2pGGj6avUveaMuTijZ4nGyvdf3tyPkB7%2B5ZsKrBKxVeeXow38dBHEUghCB4rkGn4pAkVTlkCqW2aCZc%2BYYRw8TzcZj2llBIrQndw2SH0tuQJJ9DP8sNVCytmolLaYmjDu%2FfG8BjqkAZnwh1vkrxmhOZZyAzMqQACUDMV8NVYX7qqc5cE%2BkZq1ticmxeKUT6F0zLy4coFFz5JOAH8fXlt%2Ft4nywTF8SERxXscTwNLOyogoIDh2%2FciI8lAJCgupHlJLBxjAlZ5kzu8O1DP3uFdLTJq7nJn2xo0YRQYv1TnSjz8g9fhwIm86gVBaZWHtbhuHIyI%2FcrhYJupGp05%2B3CGGSlyJs7Gcsk6%2FMugB&X-Amz-Signature=3d257513cd2ea10cdbaf2b6539ebd413b9ab555dd5ec4cfe3ac534f8148a0755&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643QAI6CO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfSpBHdaLP8QhO%2BegOSrQyoExRx5mH0e7kjQbPhGXKvAiB2FK2mbsgUGDkNEOfkGmz7Wic2hthCX4du28v7p6%2BdtSqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMltPzh6ziqHhpIx6dKtwDA%2Bdremqf1skO%2FtrC8brC7mUxwjPc%2Begp4M0GB5BOMQ01SLSZJjIzOgq0kYel5N3TWVIDQti8otzMJcOgJaaMz3fSiaibEfGWycu8XIsjh552kelUz65jr2Zgiabx8WWRRAqAeB5BJPxqlN3x5gf2t%2FizfUsOxPcw4YR9sJsav8LQdrULTPx%2FRZO7gHaJlRUMEJJwHRoMgnmO%2BLFfG%2FmkA%2FsVTKwxS%2B0UFU45yVbmPYtU1D4XJkQsxkUPiQcoOLcN%2FQe7h%2FnAJkUS%2Bxb8M6%2FPpcMvvYDcwtdenb0x69FIAjGkfmZOTBBxlRHIKG5N3USmMIQXTcZaeYCgUIE7lIbTEeW5zotMoWhKxR%2FeA4DC1VCUOKHFQZhdo%2B6zvhibiGrLf2CiBcxAoRz6gpApAiYU67FmgL4rbRawZc74c2mX2aawlbNkQ%2Fdq72yEsD0Ay9ZqPVVBqt2yogXEX72U6JQUDoIKQ4idWBMbdf%2FmvRRKads8R9oaZEHmTBzPTcqKNr1bE5ODg%2BjqNGebIkJYdCyGS0E%2BqH7Fzx%2Fo%2FIArjZnR6qklrZkofV9lLZkRCVi%2Fkz6FC3eQpQfFi9ISBHY0YOHbK1RTqM4hWPGh%2FJ0XJuA1I78JTUgqxNByJV9D%2F54wkP7xvAY6pgF2V7iJNFPZVWklSLj1Cj9FjeJX3vT0W5vUTZbe7kRL5G7%2FIb9nRtpKk4rzp8z8FKYy2bOq2x%2FVLbsdZ1d%2BhkLfTpoTUAfqQwIU9UiNvuFV4lJprYnqi13is%2BuOYcTAglRZvJzCZoVXWyibQCEGrmi4KxeGTqg%2FKbs7AUkByJxPxB8h%2BXlXlqeZQti5kcG3TRUEfU85PNJXXAGihrpEUEd79qs1wkBl&X-Amz-Signature=84b360069d0f146aefefe3730248e59b556896b5079a495bb61f1f5f680dd391&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJHPCQVW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDuo3xQxRJxrlubr%2FsbSwO7MMu7Fzh3l06S%2Br0JHO%2FtwgIge%2Bmp3h6pB0PBT%2BkhRCyNk3AIrurjRRgTh9FRUuy%2Fn38qiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2BvlosqxNNidnr2FSrcAznOVmvpmCjcV9wFERsomKKld0AZpAqKK47Xm%2BqYKTuZSpTiUcZPRoEHMCxOhld6Wcp2f5MvIWYFOJd0QjVGnC177sfDK2DbXVyy1da080WdxtH6%2BsN79YtKiaUBt%2FvF5UQtL%2BEUCKhofp%2FujYCKut5aBqB4X6HUPp8VGkh4%2BBK7ZM%2Br0%2F5WLUYBKpjAyb2LRA19kd3Hc71gDzYV0Anu3qWulTfo4UONpQAhLXTRd%2F6QNjokzKPPSTfdDkJfo4kW%2BHOJGIRS9wdBLK3NWEKXPDAZGYD3y9lQ9yqDF0PpRFySAgIj5Yr7YcJdBXndtSKzHQPAloMLAZpiUoYRFPujK6QP%2FYFVAG8vmvUUFX919FEcc538BFLay9bwBLkIJtrmw7ykfptbMsgs7%2B6t5JdbRWpj9LwmPkM9LwYFC96xgGSHyqs9Ns7PhQKhdhLD%2BSki6FQX8PbEkHjfDPpZmWcSAeNLkKEkjF01F46S1CIiPRDTWzzMXVr6a5u5jMvb7Qts7dhn5Unu8rfyilRy9oQA83ia67JxCjRFvjHMpw2kEDVvHPe6ecuLUHrxD65ixFrLhg8%2BYLgaiChpn226dzDZICGE5dXlhc%2BYyXcJMdBBGTx3Ra12q9zAkpuOMYhPMNP%2B8bwGOqUBEbEN%2FuCnD4UCuL8n09dqvHgnmxkiqY6wBc%2B2zURXxdBBuIVCn1yO1RkEpvrmGGjqkLu2ChilE%2Bcwang2jn5ghS%2BBllJlUc8qxb5%2BANG%2FKJsTQv2Q2Rsb1qrpsduolo2F%2BUxQU9%2BHSmcXWbqBe6dVPQlKv%2FRS5CFiIcoL5eJvhURCGzfTUNbUjr3qvWto1IugPcak8qaLmWcbWLGlOjban6cc57kr&X-Amz-Signature=03502373b4b66fec6b131ad4597ea0825196be46483b8b5f474f3b6a2aae25c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USET7YFN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBMrId%2F61fUmFal6c4K4hoALm%2FOEW4ScxBVPVroIruGQIhAJDBU2Jgyt%2BHsw4TdilX6FZvgSXlraGlUi5laNxLYFfyKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxvEH6qOqfQgMpJbhcq3AM%2BW45bBdIIPwJFKfmtpN4Sus%2FAIN3KogpRDsVEX6Z2uuESZbU6Wxk9HkL5yAmb2w%2BDHTgdWKyPNZH1ktoB8Gpsx3yQ%2FY4WTp%2ByH1dgKnfFybxN4RwEgZthWBR%2BhjMvPE2m3%2FYPSa8y6QmMSVjXCWuNRRXQK%2Bd3PYwTgQ3fazqvnqi1krmQbm%2BYuW%2F%2Bl%2For7l40aoG2htL4HPvsQRx0w1%2FFKcBuAxKxEyg0jGO0zpCYtQvoLogBKiF8RpiY8oEgiDEh3rMcLZ0zYG3Rvo21lwG6Fc6WECcPN9XMB%2F4vgMAeoUAbjDczXf%2FtL28y3TNoAqE834wY89DgLpDRiEh2mbxYtsVmqRx8hQWktjgy6cBb3t6HB5jvTVn9XWrsg5ahzWrIbQvhkMy0og3KxL7HaleSRbjENhS4FvO9MV2orwVuF1t%2FzhNOgB0x0ZucdC4q%2BoSG1ftQOQgFfSI2LARLj2P%2BeANI3agb8WcKR3sYF%2B7i1Guc7zgrvX%2BZXv9XT1wocwad3JM6JYyE7v3IW59o0ifaP2%2BJd7jzYeTYhdDkLwadXtGT9c92JuCN8hN%2Bre%2FUE8MS637tdVjqDl0BZgA4sSY7hgwHhxZHDIK49PBnB5mZDbm89lgFax3P8cQeijDP%2FfG8BjqkAV4AVr%2BkmwgG9tdvK%2BZWFjf6dlthLbANjoVGTCaJyozFdr7jIDzBIGa%2FmQ896kosEFqaNwt5PZYyJt79LH72nqc5sKbQNvlapr2UYFHwC9CEh7l5jKcBkYSLBvQeSidxw6xlDBQsMi35pvlpa5hO7AD9iI%2BsB0y7lFWSRKmi%2FduOwKm44xd4rAKDtn8QVxvCxH8tBy%2BbuiC5SLt5GIzPWEheftdO&X-Amz-Signature=5d1de4ee59bbfb97e2ee52019b3b823638101b114bb72ea4848925588fe3d618&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MNDBT7M%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyVzHB11H%2FBhoGGFdl8GHAbn%2BI7djwMw1U5xI9Ks4PPAIhALdqj6%2BCrMpIWWPEdwD5KZ2eXxenfOep3ZRSK%2F0YFFiIKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzByKu2Mh3JMmJ7rLwq3AMWsxWsAvrHuKYX0zO8H2jaN2K%2Bsov4xnSaMW7fkVTvZRt%2FeBe%2B0fSi1xsJ90wI%2BroiDVAvTS9S7GpAhR5K49SbPKQ9n%2Bxe32SYRGB5dr90qUk5x715YQGRWwstjBm4MhPfGBmRGIJPUUil332CzHiLfAvrnq%2BuA44%2FGO8iRWuBUDSPf%2BaduNN8WX006%2BV3B5zaOXMl5MyQiNr3oQaZgUj7QT4v0hP3MurTjneMYBSI4hCGjvOneRrJmQJ2qOr5D%2B9raIBJpscgk90oPqRmImRfv44NUC%2B2RbICLouW4AXqXweudw8TTr3PK%2FpW0wRQnBsPKjetgM8fyWODq8iKR08gOULt9kJiZwjqNo9CDhLO1SafL94M5J1PDI0amwbWJsF5jrihJAeGRKfdyTPjZGj1YfABbcbDxAwWwzNy5cLbOQSqh1i61tsgVVYVrqqqBmlwci1ogSiE3NFZVlxcoPBpYu9g3VZaNQ46B2P1pNwiMX3qtyZGINkSHbiebJUiwub1he1%2FfKpkmd%2B0wAzbAtULmwj%2FQylJsfO7jkD0ljcd8eGNsjEz2qsik8T1yBffmZFKAerEafQI7zN8aLJ7ihx8DlxqiVvTj%2FwOhdKLC%2B2VMMd3RAEJpqo4xARLFTCF%2FvG8BjqkAcuiaLd5J0ETQmMrSzVyjsfemRTeCe07Va1BdgQtWtOpwa6Utb08bDCMLuntRnV6jO5aYcitLNamj9G5x%2Bk0pWpFbONnZhgFRF1NJJ0mimG45Sl3TMCFAOxM1HO0VVxgEaypWW6ADBsrL4Xk1V7jZ1eXn5gbfENkCRqrSIfvuzNsES6bWXYUR9izZb1SqrlSkpY0OzZdvFmc6vsGH58DsoFexZcC&X-Amz-Signature=d98518d45d6735e0e113368bdd8659e2db908871e0d1f439488a0667137b76f8&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675PNHPLQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFnwpcu0RHFBahVW59nodbjgmbmxvJURwjpzV%2FZW1faUAiAim%2B2A8C6%2FpJT9kG7sQ9VRXmnWrxnSVRer8c%2F5cYHoFiqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvXhQ%2BI2h4zrF7i3tKtwD33zLl9lm%2FyIi2hGS05YQrmZuEMKbOkmdtoxf9e31P3zgC3pOBUsJGrBQvkvblmZvKgVk3azmt5%2BmfFuX1hGhZ92Dxsvw6EUeLT8TGNZbrxjPTX7W2cvBp5bnsMPUk0TWn%2BSMZSx8p6IVyqZbOOzTrkWb0d6ujgnyf4EXaZkwisHtpnKoJls0vBCbB8wbZUKNm57OP3mvMHio3Nxg7WExV%2Bgz%2F8pbqargV2uxqFp8NikdFVvlyppfT6Qxngv3QiHyRk%2BdqDey3gWgIPUTDsNLF6GhhjELv054TI4VHaVrLdwXg2dIwyTpLNp%2FOcmZTiE8TkWG7Dl%2BBN34VpcREsq%2Fuve83x2vy1WJN4UAv0HPC02fT6BPj5gUOyH1mqZ9y69mQQsO1ZKS0HR8hQRTFZOvba1zbOyxFLsbwtvUF3NJfincvTVfxuHh9xnDQj6m7VdkGGLLBgw0phVM0NexL9iUlmQmJ%2FNtE90SOwYD9KgljesZ%2FX5U%2F1e1cdsdrwV5cCzTCOJbRSvrHz8Bto7E5HxZcCzQgDwE4%2BMWG3olb5etwerZC1XeXKVxCVszeZ1uKEyejxpkK59b8ID%2F3N%2BvJFFz4Ras0zj8Bm2pautcWqFCwI7TepZ8tQPjp4%2B5XaUw5f3xvAY6pgGleNN7Z6Vo7lgjXC2d8%2FymIb%2F8mGbDQjSpX95cOCl36gNdS%2BfEqYxXxXdsqu9O1kwTy%2BrDff0DH%2BfvOaEuhduUiSwS2V%2BP3s3437wmlfm%2FxKgDI0ZWdlfih%2Foa1O%2ByGI16MDOQ8D7g5qri6GVC3hfc40LhyUrKtUfjjjKUNgG%2BEYipG041Ru%2FOWL%2BWvsznoKKcqEvo5J6bcKjhcjCkjU7aouHNy4Rh&X-Amz-Signature=dae32010c7c984438967ec93f34347a637b04308f637f661bacae4e6e3016a5f&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZEFHOKF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID2lzgOdO6QKVRGfX1n9pAKba5C8tamGu6O7AcS7yTFqAiEA3rHBwZqyEsw3OXhYapKU6Q7KLg%2BdjjjinM82vaira6cqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDESz0KbpK4SpYf%2BtRircA1hiKioyozydRCW9JL%2BUVxgZsYgAz5EEhcEC7VLtJvJXN1yo7GBvtHTe19%2FweYAmZdFM5Z0E6X2K8Z3xAzCl8OYtv0H6sy0gZ00UND1CWNmmfV38LG8oK4dGQEbH1t5KDx3WWhMRU0%2BjfP3GeIU7uVYX%2BoifR9o9RZF%2BeAOcp5ryy3aRO2cl16tMBk76iSqGa2ZIpZAWM7ZiN5n%2B9XwBGA5jWKOCu1p1thJQK2jsrGzigS5nUK%2FsNO%2Frj2%2FRHP1CQy0143yZIqbcvCaYl0rIjxrTEkjH1HXTIxcZ4PHyT13qjTLQ%2F%2Foj8N2p35Yy76nghgqN9TcqBEmWzfMnbnWz9LzJEr4WaPvIG6sFPazT5iTU6TwqM%2BW7xZWPR%2BRjc9Q%2BAHtVI0wpCJYDCKhhH29wSR9PgoQ3zwalSaYVh0kzgekmDLQBunH6U1utxuZpc%2Bm%2FGmhcP4QUohH6JwymJvxet8QpvAdtXAeJTaHUsY3muHPo2jQjtUUDmnbhWM4ihTlTtN9BXtADTkqKD3jvMHc99wzX1V6zOEBp5DVIQgFyTGpHxeeCHOmFVp0huLjmBOc7nGKP3CDyfyyB7oKsYKgj9yq38ikBM26Nn2PiIQy6%2BLvPfTO22pP1lh%2BJw1KkMJD%2B8bwGOqUBnrM3OjhjAH8pa8kx78lghypRYDjkwgXJO9r9FT%2Fdu59mVwnEg0%2Bg9nsSKJrn%2BnjG%2B3kuxc5pvz62zcfBUUrm9x9XbGoCEw9ngIpIQBPMD%2FzrWilnU31JUl%2Bw0lzCHtWAh8L7bOvil9cVjCvB4e2lCpj6TZAZZo39aQseS3XZTByTqVU7YGJkwSs5cjzoMXAUGAeSdfv5xDKGLPzbWZ1eKHMZf4yA&X-Amz-Signature=2b1f5e08fb3164b2ed752b61c325b1d1e249a8999c14e422f471438a38691972&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USET7YFN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBMrId%2F61fUmFal6c4K4hoALm%2FOEW4ScxBVPVroIruGQIhAJDBU2Jgyt%2BHsw4TdilX6FZvgSXlraGlUi5laNxLYFfyKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxvEH6qOqfQgMpJbhcq3AM%2BW45bBdIIPwJFKfmtpN4Sus%2FAIN3KogpRDsVEX6Z2uuESZbU6Wxk9HkL5yAmb2w%2BDHTgdWKyPNZH1ktoB8Gpsx3yQ%2FY4WTp%2ByH1dgKnfFybxN4RwEgZthWBR%2BhjMvPE2m3%2FYPSa8y6QmMSVjXCWuNRRXQK%2Bd3PYwTgQ3fazqvnqi1krmQbm%2BYuW%2F%2Bl%2For7l40aoG2htL4HPvsQRx0w1%2FFKcBuAxKxEyg0jGO0zpCYtQvoLogBKiF8RpiY8oEgiDEh3rMcLZ0zYG3Rvo21lwG6Fc6WECcPN9XMB%2F4vgMAeoUAbjDczXf%2FtL28y3TNoAqE834wY89DgLpDRiEh2mbxYtsVmqRx8hQWktjgy6cBb3t6HB5jvTVn9XWrsg5ahzWrIbQvhkMy0og3KxL7HaleSRbjENhS4FvO9MV2orwVuF1t%2FzhNOgB0x0ZucdC4q%2BoSG1ftQOQgFfSI2LARLj2P%2BeANI3agb8WcKR3sYF%2B7i1Guc7zgrvX%2BZXv9XT1wocwad3JM6JYyE7v3IW59o0ifaP2%2BJd7jzYeTYhdDkLwadXtGT9c92JuCN8hN%2Bre%2FUE8MS637tdVjqDl0BZgA4sSY7hgwHhxZHDIK49PBnB5mZDbm89lgFax3P8cQeijDP%2FfG8BjqkAV4AVr%2BkmwgG9tdvK%2BZWFjf6dlthLbANjoVGTCaJyozFdr7jIDzBIGa%2FmQ896kosEFqaNwt5PZYyJt79LH72nqc5sKbQNvlapr2UYFHwC9CEh7l5jKcBkYSLBvQeSidxw6xlDBQsMi35pvlpa5hO7AD9iI%2BsB0y7lFWSRKmi%2FduOwKm44xd4rAKDtn8QVxvCxH8tBy%2BbuiC5SLt5GIzPWEheftdO&X-Amz-Signature=0efe92a78184299e5a6a5abfe9152323933d1ea17b918be8468d60298f4482fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN3HUDZC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDk9n4GAlhhIsx1nm8AHfTlp0oMW9X9slN8ddqFKWJzIwIhALdhNagpYaQtoOs1ee8gW%2FCznToUZcP7ccypm3cQdZobKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5btKFBh2C2P4PRVgq3APc%2B07vD0%2BLDwNg7nSGs7dz%2FEU%2Ba7Oh8cYrOIHckmudwaZzrV1VgfdlSqgmbFtwS2pJk0OCU7Kf9%2Bxj%2F5GGwS%2FamI%2BQOol2iIIczJmnNwZu41dxN3aCU7ycBiKVa23n7kMVSk04rDs2tNzAqbs%2FgCtt%2FbL9MAQEpq36UFZdaUxlBQwptP%2BAEoI8En5Ys%2F%2Fx%2BdJbs%2BAhRGwRUKzYXaXmYrzUQ3Ure9AOQToXcd4N2w6D72Xndx%2FXiEONhRPPa3CQFaADYeQSOLzXRAykpH1DmR3ksq%2FZkJq3ow9zP%2F116YP9s6OV69i4f60LYh3muS0%2F%2F0wzgEHJD6MbsE9NArC%2BxOEryhhEeHT%2B2sz7vyr2CW8A3x2x5Bd%2FoE3BaN1E1tITQevb2dG%2B6jnt6deTjsWOxra8pJ41WFzEoTNUWaXnaXaG7aaxI41M6quit5qvExLFYt03IZPpBCMCVc0kLFpmUqnStDqhPLKMkCPZIlrr6zRkPwo43NAM0qCa%2FnfAmZgvc%2FHO8SOocHw%2BPS2zaOSYQ%2F2WpiVPtXRZQu1CY8mcnzDriaS2OHJHbt76smr7MTneVrmXQNAqB1BBT2g44TUq2933BhXDaTbfpxbPxQA8CFsKTJZ4N3D8R6EmnoAPQjCK%2FvG8BjqkAZjbWDuX8XdktFVkieTm5zNexyRi%2F9d%2Bd7%2Fvp4RCr4eBlOiysUtZLsqbM0Y747SiIeUY4SMyCDkA144BCdItzF%2BGEplrWMmO477pVfnbv2MQpMjCbkbXxTxO5Egu7rvUFUUUmqaxj4k2ojRWTkgT0YYvbqYSV2NCbhBZwCy79M0uB%2F3vsb9EowlZg2DOj2wO1buVjNKlS7zOKHECovDfpOFBePVG&X-Amz-Signature=7fe788b8d5236ff207a760b2ebdc156e52ecfd31fd4290c330500211011b101e&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN3HUDZC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDk9n4GAlhhIsx1nm8AHfTlp0oMW9X9slN8ddqFKWJzIwIhALdhNagpYaQtoOs1ee8gW%2FCznToUZcP7ccypm3cQdZobKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5btKFBh2C2P4PRVgq3APc%2B07vD0%2BLDwNg7nSGs7dz%2FEU%2Ba7Oh8cYrOIHckmudwaZzrV1VgfdlSqgmbFtwS2pJk0OCU7Kf9%2Bxj%2F5GGwS%2FamI%2BQOol2iIIczJmnNwZu41dxN3aCU7ycBiKVa23n7kMVSk04rDs2tNzAqbs%2FgCtt%2FbL9MAQEpq36UFZdaUxlBQwptP%2BAEoI8En5Ys%2F%2Fx%2BdJbs%2BAhRGwRUKzYXaXmYrzUQ3Ure9AOQToXcd4N2w6D72Xndx%2FXiEONhRPPa3CQFaADYeQSOLzXRAykpH1DmR3ksq%2FZkJq3ow9zP%2F116YP9s6OV69i4f60LYh3muS0%2F%2F0wzgEHJD6MbsE9NArC%2BxOEryhhEeHT%2B2sz7vyr2CW8A3x2x5Bd%2FoE3BaN1E1tITQevb2dG%2B6jnt6deTjsWOxra8pJ41WFzEoTNUWaXnaXaG7aaxI41M6quit5qvExLFYt03IZPpBCMCVc0kLFpmUqnStDqhPLKMkCPZIlrr6zRkPwo43NAM0qCa%2FnfAmZgvc%2FHO8SOocHw%2BPS2zaOSYQ%2F2WpiVPtXRZQu1CY8mcnzDriaS2OHJHbt76smr7MTneVrmXQNAqB1BBT2g44TUq2933BhXDaTbfpxbPxQA8CFsKTJZ4N3D8R6EmnoAPQjCK%2FvG8BjqkAZjbWDuX8XdktFVkieTm5zNexyRi%2F9d%2Bd7%2Fvp4RCr4eBlOiysUtZLsqbM0Y747SiIeUY4SMyCDkA144BCdItzF%2BGEplrWMmO477pVfnbv2MQpMjCbkbXxTxO5Egu7rvUFUUUmqaxj4k2ojRWTkgT0YYvbqYSV2NCbhBZwCy79M0uB%2F3vsb9EowlZg2DOj2wO1buVjNKlS7zOKHECovDfpOFBePVG&X-Amz-Signature=8a10e0ee2bac7d407e19eb0bc3612010501013e9fa149fd1e27287eece974aa0&X-Amz-SignedHeaders=host&x-id=GetObject)
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