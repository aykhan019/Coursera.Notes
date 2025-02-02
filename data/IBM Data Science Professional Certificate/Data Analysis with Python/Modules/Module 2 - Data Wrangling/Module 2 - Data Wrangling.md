

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3EWZXSF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBQ9TN3le5YR2BmXGXe2GratemIx4aip0%2FCJm1ciQmDXAiAuD1OxgLxei%2B1l%2B8gG4Flk1fIbu2Wl4Aipt2XJ34H2jyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdyvaMBQrwL4AiDm3KtwDWaV86RgrCRZBNi1Ux%2BT36ZUpHGlY57yFi9UQzwYazQs%2BVq4zAakYopOns8B%2BKLvlIoB21mrs9pV5nsuIjiQDqtuOJJLp7%2BvhwwHj3NTb3qEuH0LEpG%2F1JzbPf06CtppmVlMygiaGZAYUmsaf6mZEDEIrWdU4PTT6lsRc1c2UejvkGUA3u2YGNLqg1msXVLUXtrQNSuWrjPreDUIoFAyM99FKHRgLjnfTflIhB3JeekK0bTo14aJ8b2VZsLkuCxXCykqiy60TuJBd776sowoo%2FSColWbLfL09BLOAJerc3njbqh1ULESdR9tZtsRLsHkRT4qfS8OALHnAytLMFyo%2B8UFKidniRFYKiItLWrknVorxi%2BdRwRjBTmt7a78eC%2FB7B%2Fq7i2SMSZufiQvBTYL1LOWEOACkuY7hA%2BkQUOp0fu6x9Zdf6eJ9HAO89VodF9NgqlvKaM7usR1408O3mjQ8Udgpcwwam%2BbP2UzGi4Xan1GwcUbsUUY3ccAIdNU5IF8wfBqSWC8tvFXWum8PvmzFIoxWNpY7rhEDdy%2BQbNQ4DL%2FaQBb%2BbmahLLxmI7nsHKfuz1tFJkPSn%2FcHjRvemBa9L19EvuIIV5UY59NsQUnOmGtbuiQ%2BKEhQiDuW6ucwjLX9vAY6pgHVw1lGj5ItttSLRdB3If5%2BtcZ2U3oWVADAh0BPtaFAN7oIQC6CYDwLF1his%2Fo54K5ojNygtZvCQM%2B%2Bft1QB4gHh7IxJPLOS4hlHCKwbumm4N4jkL7YKtQs1uwwYoc7pF%2B%2FR9bIzEhKRIwKYbG8NFjD9uD6RL86vyRLRNJGL%2F0pcDxehuv6Qc4R1FhHiZ7tNHZU52UgFHKNPEHxVj7w%2BiHwRWAsEthT&X-Amz-Signature=71049a807381db6c3e959e8b73b728fb8781af10e00c2981ac7ea437b6c39a5b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N2RCIWX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICTAhE%2FS1Bh6SWEpVp0ZBlcerl85xRWxchMqDBdj5OEhAiEA3%2FB9KitY7X5Uwl%2BTOtI9u%2F%2BWRIOZ6NgVI7H0hjS6j%2FAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDueATV69YtXrGVfSCrcA%2F7cMQOMLXHA7w1Q%2BNeP%2BlOBUNLcOSOx%2Btjt9lHs%2FCfaOIKj8K%2FwKC8pDc6MExTlqtqHeZakImxyRL7lJ%2FlqVuv58pim98ZFcu4NNQuFwgxzRVU2w8feutigSWOyPOHykJX6MsCII8eJctZ87BkND418VXVcI0ON1fKtpHuXMfZzSdqYYVT3VBJFejs3kw55y8qxpp4PshaE%2FC3EyFteFuovTNzlHK2pvHQYh%2FQeVdItF5dtqZSEB%2Bqr6bV2CAI0vYSkGb8wdYaqWb2TOkuHiazh3ayazVUKU2j6iRy0i8XN3Y%2BQDtC29jVFJpGuO5%2FkR4LjerYQqRH%2FylwrGM3OOmMdfAKku9onXH7YjXQsURMyhukfMULGS318DanB9DQA1KbizhTh%2BIxfd9Bskm4FRnmmc%2FYI6heHT761omS0ikqabsE9jZO2KNQ8SsCT2uKK0qqUgab64m0UgFtIjkDyjX3mqsUA6Fy3vKVQSPpyaV%2FXxmAiInm9aGNOGQzFXHstyhwZRgjGZkbqu%2FcpzOr5t0ccick0VLOeAGF4R5eGrw7JBtvlnn3%2FLC8Uo7U9fVeGlvHaeHaPbFobKJD3mHs24J7OWZYNHURbR4%2FA0A1zFpZ2VHRGeBgoKf7xInxfMM%2B%2B%2FbwGOqUBu%2F81S2ZSlu3mYj6t359rPbdZvUdyeTyTUfdetpQyHk4lEO8QV998I%2F4wuChL9eOn0DH1IAi87xlP2LZvarO6kDIbPVn3xuXSnSoww74oH2ntVGDSV3bq49N463HvosuUXEewJ8Q4kP0LGl8FPGMt84CMnsis7c%2FrkgBADpHeaWyNt78szqHxKCPD6SAlbGt3qAKGpLTAb89CbeRvqz9Iel%2FrE88u&X-Amz-Signature=adad2e4c84f2db28439f57aaebeffefc8de9bc3367e4a6d397ee8e1a2c3fb40e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVIIM44K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDVPmEfh954WA%2Bg5s8K4NJzFfPgKhIpGvFBQ%2BBtMV6KQIgHcFiLRup1CwwrwBMGas4%2BposjFpypvyzWUgC5g3PCmcqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIq3y3IaBacKI7HhSCrcA%2BW9DHoxoyrpX7%2BOpMaMy2EsdEV9wgR99lxhtcZfjUMOfZZoUlw7HB%2F1I93%2FmduZ9K5GFPECgbRRJeVGFuqXUKHgPACJRk5rlqzXXpl6QC1eIsJOdR87i8WauMqxJroqvSsZDJDcx6SdRCQzu5UgQy%2B6cd1xF0hsLECiyRZYP4xcY1SCMQWILj5QQTSr09JWpVn7KLGId0toqGITIMDOXjfMOwiB%2Fh818z%2Bz9lksEdtl2abfUDIPnK8IpjD1eywAI5kAZqvl5%2BZdb3oROjvBaSgO47eWsjUNLPziI2t8gQyFrY0vcuMeHkAsQXvC5x0BZ25EmWq0VUIi8iFMq3EHF2W5AAEQNmDN3%2Fo2jFSmVOIUnXgtVnK00G7S%2BgzB93k6OjWfsmV7ilZFRQh7ZnBsknsCKBOlOvIvZkVOL26PbRdIi8Lhezxr%2FHPmSpWIM1ewO9ZZfBevRE82ALJTXE4MvR%2Fhf9ZaLKO6RTwTqlgIpF9EAOfbK3At1Esm2OuHjDP8%2BJMib%2BiP2lEUmNero8LlIKz2hBLsmvRPm1JcCB%2FxS6zWIyvs%2FFUE0VWj%2BQh%2BKpASHL5mKetadXEMZNFJ6wFLLhHGtcE0RpyZG1JHtqV8DMrp8gj6YiHieniKnVayMNy7%2FbwGOqUBOXcPpFnrl6yCOfbD5mQlRTz5KC4prWXWo9wh7FAXvfrdZYO7gWLvLUl%2BcG7Oiqw7hF2ZH0%2BzqMOqRYhVsbqnvtFcuSS%2FKsqAeFFAQSeP1xdCg2yoKHDPYW%2Btf2nYN7jd8MquNG4tOoowTefC47uheW%2BGoiR6SPzuoqQwLeqNi3AEGd3iqzQjKKGAfLnWOxUmsIGAcN3i7AKnxm672%2BcQDac2Vcua&X-Amz-Signature=aeb855f493a1867daed51c117bc803c0f2718160405cd91f5a40f021efef7e63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FSI22US%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCi1lYGNJ2G2mdfhtoVYY6uPDh1rwx5hI1gx%2FWhMAxEQwIgFKmDVkQezMh8%2F9kl8hWDQE1TIXpHVww8NGr2Ltj4RpUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEkSkvTw1Rx9pag9AyrcA%2BW8qDo9g5P6kHpbupI9D7SIK4coHPlbaRYNw6S67Z%2FkXq4hYeVUI9v7I34J%2Fr772yGQpD1fpX0uGU58kouz6NY9WfBQSilG9ovslyYF7ZvV0z2SY%2FiStzvkKpsSI3%2FtiKw56WueL%2B31d%2BG51Kq%2ByU9Iyy8UTCkzcA7R6f0%2F6xkgHkcXQQ7WQ5grXc3i%2Bhf%2FcTziHxDtD7XK7%2F08IPbuvaGN%2BiBgdKPGM3ymzY%2F1deezp8IVyq3d%2FGS887CevmK27nhl11cDsFxujNXwAW0FAK6dVFYTHr3rsLnI6B5Az7YdB0AViI%2FG%2BBJKhhjp9jq9nsF6AljAzWH3xOgD%2FBD3d0uLnUGo30V%2Fd%2Bunw5zALPA4Gzfi3ykWFqBljHQdmWLCvpC%2FyUIMs2HINQSt9bV%2BZRB6CBgUhUEbmOKHMa14zHv4oyWkABuqQCn3mrGa680m%2FLuJc6LvyFkI%2FhsRfM2WvSceSTba9u71lsmKAQ3GXhILkmXDkZroxJtS8z%2FE%2Fd2dfp%2BHvxt2CgHidMdNewegX58grCib3tRKnv19NFxvk5o0XGQ5LaNZGEbr4DdsWm6n4WeCKseKSMSGc6D3BM68kpsX71nJLS5oUOTp%2FaISkN1cBRbI9w%2BpRt8bb5tNMJq5%2FbwGOqUBCX7vRCcdDmHZx9aet8K6ozyYDYwfh23d7Un9xtW9StS1y%2FtAro1ZEOjigm0M7peQrU6Ac88EhYz3UiKFX%2B02%2FuWxOZPf%2B5QcswkqLwM1t2AZz0Iwwu95IphPvdxi%2BcJ%2Fy3yt9wds114IMydkdhcb32%2BjtQ9fLbowMEGpArYEUYPAlqHduzMiloKw7Ps6MW7wH8fOculFcJ%2BAoKhmNJOR37UZK9EK&X-Amz-Signature=31c6759815c7fd271cf780b5c3cf5420d191313bc1cab602d9c39cb12145cb57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YVWYIS6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2FDCzIsPJPe49MehQW9nJQXgEijxlY4EUF0fCDCgVG3AiBpQufpLL1gd7Q165Al6iaSRqkxepauYj%2FddkrSq8ffBSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQn5nACgPl1FjV5aGKtwDDuxmVx8dLwPHm5vWR%2BkvGqE7eBVf8Sj9yp4mw50zKz8DH%2FC7nbyefpJDpcdENE7T9O5M6eFSVfHRt3FPD49WAsX7rQJffpfUfD1nzYCcKwhjJpoi%2FNeTkKkb7BrRy2ad67HvWR55R3WeCcI0lrg7qWdnInjJYxJDJcATgHD5A0MTythgRzQDhCxz0EuGSEelWNFMgyXOqnshkjuvmHzFxAd5RD1Lt9b6FaPDh9Pyc6THYRKYTubRzt2r1H%2BZCChPJLVr%2Bf7TvV4BqGHZPA7Od2%2Ba4m0qS1UcWuTPlBR1j7T0UDPODE6Y37P5Vgg7PT%2FwnpDyfbQEhmyCkyvKj6%2FNrfX94GCOnfkbU3coVuijtorMPdOLQp%2Bde%2FwtMjbZ4QmU870O6ImUZA0W0EkuJKTiJfBMn0aLPKD5AqQivMo9GH%2BdfslVl7U261fWRqpDQZ4Zd9H4IhRGjq4B8r1wSbjiAjwKdzGMdScE%2FoJ2qOmSpR2o0t8J5k0l64LfHKKX7YxQ9dR2mu2keiS5tqjfWeoiWVJPF%2F3qhV%2BduV1rb9954%2F7pxwwzDdk7BW2wgjq3m54p9oOcIIuuzv%2BRME6vb6XuThxhQ1ADlLHpy9v6%2FG7TGxfFi2VfOwFVUowG02cw3Lv9vAY6pgGivBl39P8%2BwfhLmbR5lS2v5hbEBU3rYdg9aOUFxfyoyS96plfhIFBtOqaqfN6CIT21TOjI6ZTNnY8Er3lJht9T969FpqMgmJu1w0U5JCOeqd0%2BIUFHwW6nuxrpPuyeMF9EaQkXQdcRJjQi6aEBz1CX3VlvkpjHlxYQPEt1fS%2BINWRCbxslTHZTHHdh2gBztjwr%2FXDvCD8dvts0CW8FOVywkCyfwo3h&X-Amz-Signature=3f11c222b522a5e337d9b0e92dd192e036bbbe544cd9563e94d604fa38d459b9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ7MXQVC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQ%2F1PAxYek7uV7o%2F%2BTa%2FdwVB0ngxwhpB7zT4p8dlbIxwIhAOnO%2BMXQxPKF5Xqe3l4Fuydlbjjf5zeMtX3z6PMBzLB3KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxFdUhQgaHl1haZQ54q3APSqVv7iRsxoQe7f8ICMxKGE810h4jIXOwrYs5cnBIlZEWA9G0p4blfcACNhtHVMJ8f258QZozh4CWqTHdvYBHmcAMRXRref%2FMk6rRsv%2Fnuy4e3T7MlLzx4oYv4pOUkAWOcVf1BCayMO%2Btq11T%2BvCX%2FukNXIt%2BawxL3M0WYATs2T0iq8k8LQQSJNKS5I93w%2FFTZkrhxm9xAGk63jzm9MV8iJxh3RvFqN5PQTEo3A%2FrP5IE%2B54Q6xRtNksamblm1nvICJ99L%2FK3JeByj5tirkPBfXKtTT5FBY1tlJu48HYzZozU5HZpTMTJVDKWkVpe6uEEN%2Bh%2FjU9aQM6jIL2eN7BtRhT2alEtXjI0wKBEYx6msxDFS1NDAE%2FpeXwHuaO7XN9TqZnwLAZpy%2FYcwC8mFZXkzGeYXhzN4PGRMUYy8tx9n%2FlCTdIv6yHVsHm4nKKQGIDx0XfDqn1lM%2FNhqdGsvQXLTa5xx37NkmWIQ5jbHvTZwIe7tAz3LHWAcZaFdd2tlpZY7uZCcnHJjQnP%2BQOLdcZ7%2F8%2BRSYAuwjYGkNMinqWBCxJOZQdNi8sqbXlQvmVF%2BzVN4SDODgenMNqhWswCgUSBJgJ9gEx5Js%2FRWBJg403PfArE00rqbWfU%2BsO0wrTCRwv28BjqkAUmKkkaq5f949IauguTdYee5vi8XbRmTHaJBPSNlbZhReUjoca3KPrcAgk3lXMjpNrj9JJjRASc5oU2VDGTP6kA%2FvwBHTKbVKUXGBeKQrFYNMFYo0XSPPjNp5%2BEHiJp7GRMFpJtOerKO68VpqYimcJxYKy1cNqFmEk49yDS0x%2Bz7ewbgjo%2FWZsex0Dm%2B8Mv13QnHPlkCPakDMU5dW6UJEhpcSJzM&X-Amz-Signature=40310c1dd19026842c6c92ebc9491ac270d96d05cea19ae452731a281506e1af&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UZ44MVF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9VMMBAN1t4vIkGnQ1c2GAIn87g4BnR1SzrhwPG7zgfgIhAKyTrXKqn8IIfIBtW2o9IPHnDDUmIbBung%2F0bYuoW3VYKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2B%2FJD8DSMZiXvjrdIq3APRcY3djYQ8ADrxhcd3gMhEtSXJGD6LAnaEtCE93XqFefudDPX85M1Ckc2zhwdoSXQoIWRfwhUK19Hx9z%2Fj56QvQ0VUjkjILgJMattK%2FJcxZvR4%2FVl1wSPnOHpEqO9ScW5XrCeMTkSvz8NKJODeiAXjwLzYPfygKumZC4t59qi%2BfCDw0QGuxW9vE2QhhgEfvpjdx7Oh3G%2BSuPa7lNKuhtC2vr1b%2B15po0L%2F9v7KYvcSFKKLCM5gEURZvT0%2BvHsfMfl%2F4jbjCRx5sbcblBdDqZGyb4%2B%2BVDCdG0dm6%2FJq87Ftsgp5D3Vphvxwyh2gRj5ikOFjCLklw%2B%2B%2FWjf%2BI6Rdhf%2Fv4L9yiJO3ieXFaxuY39gNDh5P5LOz4nz8AWa1r7AZumAV3Re%2B2o4zUt5HmXN5Yo2GfO7cubZ%2B9lLvWWzdwwyPzrf5SpAk%2B8CIvT04X90lFuOMkGMvNl3Y54lf3i4tj%2FSettlQGMKJBe%2B7AzMMZFRViz5iP0WhRUZdeAWmwzL5mkuTzAJ0rMKSXP2c2uxhUx59AyB6iUxvOWkBg%2BF3JfqdlkpA4HyNWRRnvtxzKmecf4jTt%2Bh%2FKudHF0KhZsXWOeoSqPgKAzqvEPCQcjd7ClAzS%2BSu%2BYUAal1mSlE5ADDkuP28BjqkARaJZ1RUudJecWufmc4bZIkPVjoHi%2Bh8E5rrakUbPdV1Yy%2FlMHe4eV1dkgTA6Cy2fYFUaAUjhsW7WfOSvVVQlbpvpGMnJhrmS2uZEvgbcRFC%2BklWgmcfnRMpuZPa0qT1eO1oRXM6xxTdr8T3PlqpMJdvBdBMJa4QnhPIUY93S8XnK%2BGKCFNopgzxvXj%2B1ARS21LWlUW1%2FU3RBBwXXregptlA7p%2F2&X-Amz-Signature=d26cbc5ddc30ea6b4146363e586c0e2409652db67aed661162e0948c00c53258&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RYEXOEJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDb5A8kutrLcACIVw8aLehKQJbdk37Q6qYmflyRdLEqIQIgJaqJ7yDDMVPeRxu%2FDR7D0P6W5tbmYBBhWSKoyFKmUSQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNmeki9TsZ8g7bHB%2BircA3Gn6%2F336N6sB28lOAsBtlYaJTx2gpylKH9AJRx3%2FbpqEkyu3g1itbGEYq77bcuCgdVH%2FND4XCRu9%2FmtF7Y6P1Td0RZLRcDRAnu1PPXBuGf6lugxDKiYSm1Oj99Uhd6D0wZIxYX25txBd19AU%2FvYtuvxE%2BivJJ0YZWHvQcqZV5ER%2FhwnVoycYT4EtYnBV3IPBzJ9eOWVChnA5FdrXVmpiXuHSfYlkzkWGywWqVTFC7nt2mnIW%2FJ28K6ilEHaL3iivi4%2FhbVgn9EBfaSJbYlAQacgC1nEHZ5loWnRKs5HKJHCJnW3B2wrGRPlOQB3g6pX%2FTgoqCldoaA64dYH1bAjVn0pLeylxAE9zFan3Sug4U9DBeJg57H2iAUQXWQ8%2Fy%2BaBe%2Frx5FJKpc%2BqPva2xLcDVerXhSw4I%2BuBf%2Bctp0g4oYiIMDvBi5jCmt7eRcC4nBcWjAHBpCwgnL%2FXuvBSLFyQDSCa3OH80kmYmiLMFWMtxJB4s8IQS2Zr188QW%2Fpj48YozYPvebfxcqJM1d71ThzqlvDaGDtJ30aoZqHwpLgJ9BGlkski%2FMz5wk3naowXp%2B6ezI8r0jrHQpC2S9%2B4rNa2fnLXJUo1%2BM4sgyVzhpMcnBPU%2BLIud%2BuEjMfE8a4MOm4%2FbwGOqUBT8jLhqiQn3zCUcXMeJk6JQM9JTs%2FpyP754RJBcrv4ik5S%2FZJMGcUR%2FWs12cNLlsd7MPpyzcvNPYeW4gpocRz9dRf25tdmK%2Fkrlawz24fnE8KuZOx6A54e1PDd1%2FS8wlrmBTyveF1YGWlu17d0iH5MnOa5EgZaxAQ39yQZMtwd7CRLKPE%2BLqZkwCUbKGS6Y3S%2BeD%2FXy8Q2dOw9PamEeMN9WFDvOne&X-Amz-Signature=73fe7f0500a334690a367a72702a5b060f5f3a2c78448cccb91bd9e80a62cf99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YVWYIS6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2FDCzIsPJPe49MehQW9nJQXgEijxlY4EUF0fCDCgVG3AiBpQufpLL1gd7Q165Al6iaSRqkxepauYj%2FddkrSq8ffBSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQn5nACgPl1FjV5aGKtwDDuxmVx8dLwPHm5vWR%2BkvGqE7eBVf8Sj9yp4mw50zKz8DH%2FC7nbyefpJDpcdENE7T9O5M6eFSVfHRt3FPD49WAsX7rQJffpfUfD1nzYCcKwhjJpoi%2FNeTkKkb7BrRy2ad67HvWR55R3WeCcI0lrg7qWdnInjJYxJDJcATgHD5A0MTythgRzQDhCxz0EuGSEelWNFMgyXOqnshkjuvmHzFxAd5RD1Lt9b6FaPDh9Pyc6THYRKYTubRzt2r1H%2BZCChPJLVr%2Bf7TvV4BqGHZPA7Od2%2Ba4m0qS1UcWuTPlBR1j7T0UDPODE6Y37P5Vgg7PT%2FwnpDyfbQEhmyCkyvKj6%2FNrfX94GCOnfkbU3coVuijtorMPdOLQp%2Bde%2FwtMjbZ4QmU870O6ImUZA0W0EkuJKTiJfBMn0aLPKD5AqQivMo9GH%2BdfslVl7U261fWRqpDQZ4Zd9H4IhRGjq4B8r1wSbjiAjwKdzGMdScE%2FoJ2qOmSpR2o0t8J5k0l64LfHKKX7YxQ9dR2mu2keiS5tqjfWeoiWVJPF%2F3qhV%2BduV1rb9954%2F7pxwwzDdk7BW2wgjq3m54p9oOcIIuuzv%2BRME6vb6XuThxhQ1ADlLHpy9v6%2FG7TGxfFi2VfOwFVUowG02cw3Lv9vAY6pgGivBl39P8%2BwfhLmbR5lS2v5hbEBU3rYdg9aOUFxfyoyS96plfhIFBtOqaqfN6CIT21TOjI6ZTNnY8Er3lJht9T969FpqMgmJu1w0U5JCOeqd0%2BIUFHwW6nuxrpPuyeMF9EaQkXQdcRJjQi6aEBz1CX3VlvkpjHlxYQPEt1fS%2BINWRCbxslTHZTHHdh2gBztjwr%2FXDvCD8dvts0CW8FOVywkCyfwo3h&X-Amz-Signature=9f43d0a6ffe4c94a4d6d5970d7cccb68fdd9d22ce0ba7eb0df85d76873a2a37b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW3OHA26%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFxOZo%2FdLgYlA64E4CQWv0pcMvJZuca5VTlHSqDMSDUkAiEA8USRK%2BI1qFPFtXZMX8txmo95wALJb4pfIk%2BymSXS0PwqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDud837Ha54FS4lKCrcA1hpifhnIIc68KQemZHfGa92vJKMyXDbTmSLsvPzQmJAbi%2FIT7DveDa8xb8H5TXFgmQCBPe1gEoPT62RjNsAsM9ejMS8TBrRzryE1iezNxoSED77zP7z1IdRCGSO0rKlfG%2FX4eQkZ2GSTZ7jUGGOT%2BKv13C2tTc188S5ePxU9%2FkPTkjKKCPIqsAbPEjDPiweUlc%2BtoQLQroD%2FsVY1PZ%2FF19Mra%2FwSBE9mjJzeFDplh%2B7UMYDJLGAppXYToYSw0nOzGje8Rx7RkRDFrUqa6FeTWr0Catt94JnLc54v47C1tclYraUd6n5uhpICbdQa%2BMgzosZ2AyR3wW9hahmrG%2BtGSC00Q%2B2iaR3JJxYFs0xkvRy8dDuYK6HeFivQfqXGBbPegrxQpCDixn%2FRL%2BDbkdxZ7haXZyh522P8mHmWtq1Y0HRxnhAs%2FPeESNGlZI4yHtE3Li%2FKochPN39Ue2Kys%2B4jlaVBBApZFlsehwLo0kLSwhLBhWH1K5oy%2BzJrxsVLbM2oYRMYril9gTxsdr3vXTXUEAzo06nVsnMWl1%2FxAaFv%2BcFGgP3d56a63xGSF9PuJjQ0ijXa1f%2BOrcqoLNlYWSHaxLKKC5gpKqNvbannT%2FqIOcyn7HFYnmB3HpSZstOMJq5%2FbwGOqUBkaUX5sdDujJ2WMDIo5hD8iiTAOswvmHcdI%2Fq3upe9hB9YrLdTzL2Qjlm%2Bn7wUO14B4APypZvdc%2FdLji1LcX6bEY8Pwv1hHa8ruERJhtl60VnWn7%2F0otBzoPFahwU01VzA57D3eQ0bhmHOTguiZF5e7PMTSsEmNo4X2VLUAvh%2B5RkZYLVa8LFpCWDOZ%2FTNmH%2BkchK5EJ2pvTKhwpXVbH%2FMiC%2FXsCf&X-Amz-Signature=1ab01dbf2832af8f6f5aa0c00b1cf54c28b15b91bc4bea6e524fdbc6b3615b57&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW3OHA26%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFxOZo%2FdLgYlA64E4CQWv0pcMvJZuca5VTlHSqDMSDUkAiEA8USRK%2BI1qFPFtXZMX8txmo95wALJb4pfIk%2BymSXS0PwqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDud837Ha54FS4lKCrcA1hpifhnIIc68KQemZHfGa92vJKMyXDbTmSLsvPzQmJAbi%2FIT7DveDa8xb8H5TXFgmQCBPe1gEoPT62RjNsAsM9ejMS8TBrRzryE1iezNxoSED77zP7z1IdRCGSO0rKlfG%2FX4eQkZ2GSTZ7jUGGOT%2BKv13C2tTc188S5ePxU9%2FkPTkjKKCPIqsAbPEjDPiweUlc%2BtoQLQroD%2FsVY1PZ%2FF19Mra%2FwSBE9mjJzeFDplh%2B7UMYDJLGAppXYToYSw0nOzGje8Rx7RkRDFrUqa6FeTWr0Catt94JnLc54v47C1tclYraUd6n5uhpICbdQa%2BMgzosZ2AyR3wW9hahmrG%2BtGSC00Q%2B2iaR3JJxYFs0xkvRy8dDuYK6HeFivQfqXGBbPegrxQpCDixn%2FRL%2BDbkdxZ7haXZyh522P8mHmWtq1Y0HRxnhAs%2FPeESNGlZI4yHtE3Li%2FKochPN39Ue2Kys%2B4jlaVBBApZFlsehwLo0kLSwhLBhWH1K5oy%2BzJrxsVLbM2oYRMYril9gTxsdr3vXTXUEAzo06nVsnMWl1%2FxAaFv%2BcFGgP3d56a63xGSF9PuJjQ0ijXa1f%2BOrcqoLNlYWSHaxLKKC5gpKqNvbannT%2FqIOcyn7HFYnmB3HpSZstOMJq5%2FbwGOqUBkaUX5sdDujJ2WMDIo5hD8iiTAOswvmHcdI%2Fq3upe9hB9YrLdTzL2Qjlm%2Bn7wUO14B4APypZvdc%2FdLji1LcX6bEY8Pwv1hHa8ruERJhtl60VnWn7%2F0otBzoPFahwU01VzA57D3eQ0bhmHOTguiZF5e7PMTSsEmNo4X2VLUAvh%2B5RkZYLVa8LFpCWDOZ%2FTNmH%2BkchK5EJ2pvTKhwpXVbH%2FMiC%2FXsCf&X-Amz-Signature=043892f3e2802e528305acf3273cb0ee98ef7edebd6190d567766c6d274ec9aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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