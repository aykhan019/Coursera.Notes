

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZOHMVUO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIFp90ynV%2FZXcdwLniqgCuEw%2Fz8w8INk1%2FlhJ7eIlKFrgAiEAonGDlgysWtYNmGS7T%2FKDmLSPVWhQ9wU89CPlfbTtnFwq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNNPpoIZn8BZximMUircA3OGwTJjQ6c%2BB4O8Yc9keZ%2FcXqrLGtFIh8rpiyMWuflfAqYeU1rSeV%2FPmtbVkn7qMhq93XRDTiIoysVhedhxVXOvq63s4u3FtRLC%2BFjQE4WpAwSo6if2Q3AIdY0FrCs0VLO1O%2BbTyAixI2keRLMsEMwrtL83F1v3GM0rKbe0U8fdYPeze0dMyD9JSUkidxoXVDP3rq2D%2Fw9xEXn5bsPvEjRwFWMSlN8MafNlfnJlQ62dG8kPgzCkjpqjmUMCOQGnV5JQYJfZo9eLS%2BkQF1bGHU30UjHsdwIqDQBl3yZhradfLJb%2FkYO6fiNL2LksIA1kL6Z5czdXroytfdInSaOUsQakpUuwjw0uZUSyFJz6D%2FA20rAY6yQIaAqlZ8lAW86mFlQfLtBRrlP7MmVHPOUm%2B22FC8iBlfwmYsM1Ita35Zx8MO7QSF64mf7%2FPVKRWZmcSEArNkjADeyR4Zuyq6%2B3WMyThVgVD5oPK9r49XqLOIwsRQwuQU51LyriwMobBGJO1%2B%2BvcRfCSV%2FygNqAyn2HJUGPvP4GQTuWBHRV6F%2Bg5D58%2FmCPh5zyTKwmAgzzrL306bAaPEp%2BYBPm2JErmCi3ptGFP8SZ1fVqXGyJUxs%2F24TpwxAGZqGusLAJzGHNMJaFhr0GOqUBKEpewg7KCRXM8QgkKY3UIqkY%2FgpmGWVSJr2vVLNmy0%2FLug1%2B5Wq%2FsuTwnLrmME9JgSQHHClPue0esTm%2BuKHNERwzfY%2B3rjBH9hSFLc02TCI1yw%2BA2ju0HA9Kn%2Bbd93jdbDDGSiIvdUM8H%2BoUdDGmibHLHosGcwPzGcCbHVlbFnTwy%2Ff5B%2FIwujQbFD%2BpXkCc0ZBYXdK4y6wRpwGY4kekdU1tqWI3&X-Amz-Signature=a54e0de1456a205f888e24f71f0141716f46c4000441287b9168ace2f55f0208&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WVBTWML%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQCjjk4ddRZ%2BQdF6E%2BsJ3yCBVaYTDhjRAHxq2JGnT9IpSgIhALaoC%2BCc80oLUkbaKn4gmJDwLNwBc3r6JBbZXJPtzZ70Kv8DCCQQABoMNjM3NDIzMTgzODA1IgwuNVBXwJ01z%2BAp%2Fpsq3APAe58vNy7FV4yW%2BGCwjFWe1UZlpa9Ndx4CEicUJe552%2FMNuW3OeeY6nFmF7ioMQLYb9oQADCnni%2Bhp7R9N35koUJJ6g6Fw2bTQsOQTOVLdft52cudalc%2FsWnfIhng9epy36IEXl2%2FBs64ZpnlS%2BBc%2FxaEwUyMDqml4LNu%2FRWMRJyaykV3NxJVIAFPtodsexEQaMPc7CelZSeSMRXBGXh%2BvSumXBS1pM2%2Bw%2BdARAtXInI24%2FKgiMeGyEBfi1b4%2FML8KGPVwnaVxZvqfb0U4RdJTgjyZrBOLvym2hiN5r7WJVAUcicKfM1wZ%2F9BhHkqqoqrlJY7MLrGykx5kaepNFt6Rta89NAFexV90ViynBVGAIGrpbgDFZhZH%2F6zYXon%2FkdnzMWo4kW60M19z%2F5j8uMyXBjbQNDyJTFYp%2BkE0EKMLyc1AIdN7aKjk4niFLZy5fx4%2FsCXB3BczLsS0fvPdfrV3uTsQbiNhb4Jt%2BL2PmpV%2F%2BLqLNhaHv2LsJudAmDfQGWpO5bRjOLmZDwNPDpMrQZTvPN7oXwOj5ctoZvPlCsTuaL%2FtSYSrzdS9haC5OfhlOJZ4SGHkyNYmCWnv6xCrNvKP1C2EhPaorG5c3sWroopXtySYUfgZFOj8w6L75zC8hYa9BjqkARNN3wqD4klX0MTTFKAvSDk62mbLPrQm8H060VZ8nuvRKs5UI0gA7tbo2sBL2EqOG86VSirxyFxWy101oRw90ceVoxBXtgL7Cdmk%2B9HXDvjj9Eqwl4HECBKwZJCd8wNGjfOw4tKLZp7WT0%2BH4hTX6Yt0DfS9VoeBASUb8%2BbT6M3TE6si3Nsq3h9ZAADAetSTrho4V4GtZMvaEpJBh10dwhv2kCMM&X-Amz-Signature=c137fd3242d50ea404e0c3d4443a013d7c67fcc7604b3c044635c1242bb6a63d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USXG65TZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIBAoNNSPUfkIDt08G8woFiRKCrs6k%2B1TTeNin6IoX1JRAiEA9%2FAUagfpegZ6jRar4yXXTUr%2FZgbNZXXJyTfeJr%2BokLMq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDGKf%2FkmGtM2vnHJxTSrcA9aBVsNRxIOU0f7TJdWkfEtp%2FFul2W1V%2BfJcz3Qo2HlEBgSjMUeGoE8v7CxCTtLSHVotMVHuarrLEe7kXjbmo12BizlVD23DxIMjRb%2Ftt1VVI4NVcKAPCT9hYB7x%2F6c%2FW8%2BGUtb14BNm5LcQP9%2B6O%2BSHWdmyemF%2BPBbUcMELMFJu4fd%2BPKqZtCkcGHF23M%2FEb%2F3Wp2%2FDvRZjdhlDKamgWBLRLfR2fGEgTUnsU06VGRddoQL58JKDrydBng29kXSaOJwRx3M6jBVA0npr5nyr6YUx5H3%2BrZiXREa8TgOF6nemOidPnIJbrN%2BWrqlBD%2FtZysY0Sv7wgtu0TQzZXdOC4%2FrKodzkbGlwtuszdgPaZG009LESxqpxSx6IPb%2BM8nBwj71WZLlkhckIUrOhKfJ0Xek7BO793AQBGCTviFuuEoTTsALTdKQ3Ebvd08hUBCVNzbATr39rzYisKDGXYRlRKh0g7Gn5h%2Bf%2BDasiPH9tgwxyuh6f%2FTtNcvSagaLkCK%2FHYSRYZ8SEQckIE0d8g0cu2sHDw9F1HX1qUOMHh8D5Cp%2FbAX3Eb57bTAWlDOgFt3D1bsWkbqUBtZY8fPklX15rxhkHAWqAaZi4FYk%2BNY2g16nJOu9KgpvudfKePUTYMLCFhr0GOqUB9Kh%2FaISbr4mrFoslwlI9xAWIUvUTzh%2B1g36L6%2FtHkudEAUh7a%2BJc1zk9mky6cl%2FjEkmD9vuhmIBVqBdG3k0%2F4N5xYfUds8Zo6ntCIdAgqyUzJcDTxsXF1ihoiae52RiUgm40%2FtmtB0pwZ9vvq%2BJLgnOMX2%2BK4LG7iqIoYj5Kt38%2FyMLZqsz1v0tTZNtoeZIF4%2BaXvupMpsGfR9NIbhHtM3Pm7l1S&X-Amz-Signature=59a3b4a11ff8b3237f1003be0533690757af6b7284a99e42eb7a7fcf726853d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVLMBJQ3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQCmLljuoo8mRaBs6sOtSP41VYvw4TezmUQlBGmt8KlxwwIgC550%2FEkqs7v%2BHGKgyjzUXOeBGM8YizNJVDKhEXhjwl0q%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDEst8qn2NEXOt5etOCrcA5ctDzEE9S%2F7dDUqMVkQdYmJ9rtBvTo%2FMT1wWuu3NqeJ1PMWGuh4sBl6m3U21CYHyeOSdyfBkkBEULiJDman5CErmZ5ozg%2Fy%2FxQHIvALo%2F5APp5Zsmp%2FaewGsZFn274NG1j5iQFFeu4na4fBiK1AVEUn1LFsQ%2BHiKkGkQsEm3Df%2BzqoV5fwrdJGJ1A6%2FEYxpol%2BbNH8oDf5fh0NZL22ovXEgZ09K5A3mvbKD%2BFdB8tufpZLMVN9HveGtcY%2FBs7kqlx0yQnzsI%2FotJm%2BihEMGnV%2B7PvIlU9kIzFLaPjy8jQxnbM6ppFEswAEiG80fm7rmhG%2FfVHYD8rPkoyv4zF%2Bg18RR6ob6VWVG8tZryjRdZkVeJXTg8CIK1ur4CwD2RNW1Cy1oEwh%2FRTqgc%2Bmll0lXu9pWg2UU1aQkScqfNbF9ClYN0eRhf%2BJl%2BM2xSB2wwbJQlLKPQ69Jt9N%2FiFbUptecorDcQdGaGDcXz0nt23hK0cl9YPKI%2F%2F%2BdS60KEKu6DITFzEpVNKXn3%2F45H0v5laIXWYIaJ8gKYs6qVCpxUj%2BpqRHzjM6BU9tMOYoJ3c77M8vkO1KUldL5OdwlscbKYKyQhHsPM0OgCf4HJTOxKvgUDaKnKDyorHykVuaMn3fHMOSEhr0GOqUB6e73nGa9EtUHQIQLOIhhIToz3kT7dhj9%2BrjN%2Fi77izl9QR3IO3QWktCQGcIxVs7lpOo9wlITiy9vRVEBztANbeAlsC%2B%2B2mUrJyM7%2BPI58xqrWu6OldCTHwjivh4v%2FqAp3CVzM1HKVVXItmbaN8azvxLmz3u3wBwwnYz9%2F5ymNpc6jLqXIq%2BFoWOHfFBlsY5oritiVvQbhX%2Bqtp4S8BHAv969LIET&X-Amz-Signature=cd75241b56d12540d035bc643816ba26542e6a41e08c60ef59a7df90e82623ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662HD326P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIG9xD8uEbdpaktd387sBQM8TODZTmsLUbacxURXRJXYqAiEAlSpePyoCaOvnAye1n8eHpIJbOX7KwLwpd6cBxiKBeYMq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDFDRBDB1v6j5ycn0GCrcAyjc3UGEVJ1CNVWc5Hyr3BV3XdKdXYdRMwdg65ToNFzLiDzUKrXd0lk3P6JQ9rB68E61D575KOeNGLDO4p%2BJPYNwIXkZLvI96AqKmpZ2pOP8jn8VKfk2OYpVnVl72Tt784bK%2BGRVHMjE%2FSOXseyqBJhYm1euAMdXUSaHUQPV8YQ3udW6iHRUPccEJG%2BokJg%2BLktZzGUWDlFhis8RKpWgTxdew3i6DmI2Ck3tX0kubAtuoFShY0WTkDfecEVlqlbFtbPtoEFfoMY4vacFR3zt6KQgzBrPc3xyKUA5kXGdQNi8Q11aspnqOYLE0xrb6t41sbc373v1vZuQBxpFONzlZVRLCFxMk%2Bk6JzuBoMARmkDW2yYfGT3TXnSAeFgfoXh7xcBKiizT5FJPkt2smCf5FCkKGbXUxg2SVmkBenuUwbRN%2BeLFCnVMhE4DVrOzV8JtQ7uowxwEs0DDMkcpH6pPXkex0PCQb4Bdc4rpMDFUVkSJRmfmJoA1paeMqziklWBlf%2BsbBZOMqWIwu1L9AIzCi%2ByP77xgwpY8ebpUGWrbtwAKjHXLuKMnqFp0tzs9A2q6XqmsxEyQk2VnvRfpWQqZZDeOAY2eww3dxuLbNvcXJEQdCSSfQeRr4QElwP9zMNmFhr0GOqUBLr1ubMyPkl7x4HnTnv7A2jewmuKnV7qO6l8u9gXPcefBHEF3TpV3d%2Bc4K8Wa8pQGoGcjbUQEIZi1pdxxEaVuVeCwIOUQdmYC%2FcDtNBATOC7avBoji5czqDVeS4xqtHck%2FM5%2Fu60HjOrzBiMQAzoCp2cIN0aEfcDWqo%2B2vlylCQkta1lFc8%2FdFbfe%2BOCu5Hw3nCfuOzOGyCOdLqOezeUJ2n6KYFgL&X-Amz-Signature=b78c2d40efef5423263e991465c5ae58d3e1a2f14e96a8b1b0ec826dccfe4856&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRNGWB75%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQDqV52l5MZp9hX81Ql7Y%2BnJpRwtkcooz0bsA%2B%2FlUv9WMwIgR2znVIGrliWHswXlUFAtqQChcALqyCzRpu%2BtM4IfQJQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDPdqWBzXs7nTAkyTwCrcA5UwdwJSjoDl9f3gMJBDfNZZUrlqx%2BCIJubWwRUIodnpEr518G4a7XVHJmZso4Z8dgoL0pFdWnLmpOxbC6WJQk0wf3j3E0zNOanqDw3T7oWM1RPnneM8D0IthK03o7NhcYEx%2Ft6A7NuIONhAxiNt5OI40GJlduvRMghv%2FQ9uZVdJ93cxT0C3zARNjkcldTXcGoIeWfCkwEFa8XS4FXsZBcn7dRMN7rK1eNZruwWSTkI3X5%2BDIbCjT6rO8qzt3FRKPPoFlwO43Q%2BPEIE%2FrMq6Uel3EEp%2BPxaTfpUcsP2Ag7XlWle9nJ9Qrj7IblAvRVb4INMltUx3L8Jpt%2BsllLXe8Xl7OR28sJmcIfPJI1%2BwewnKRKPr%2FkehEXqUypru%2BQC%2FhhebrJDGW8WGvMazYn5fD0hwiC55zbUu8rMEKqivCK6k5IaN%2BclIsYEH0f8ccVsZhkHoPwt0jxgrxnjZBJG1Ra%2F4L12%2FRbVvaMF5bTbmOgKgfOSOwn8Knf13CbHQCusKy%2BOgNj%2FSP2P1l4dPtixW5SX7TJ7Z0wvjucla7WXn3kfwSDD3unyHbgDtW7B2uwYU6%2F2m5r4oPn3ibsk0N2Dj5CbHzo5H39QjCNFwFy3GItqI09qScRHjjCWQ5O24MKaFhr0GOqUBffGy8tPODjd1MfOPYfO%2BawGevrtSvvORIiLE%2BnVkZNZQ9eNcVQUkOru%2FyM5KfowkARtCroJdXpKRUZjNX1DeB4OzINbdga8gykGyW4W0lLJKrLP2Fb71xcc20h3OW%2Fwbthd4egtIBrQc6y0dkDyJMF9knzMTGKo7mRHXoDvRVXru7mmUlvUTEBh%2B2GpwjbzkxA0N2NC%2F%2BPXf581vyJ1pQkWPxevL&X-Amz-Signature=1e6d4d61f66a0fe3a879d5086934322de15c45b5a78412f253cfbf5c83e56b39&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUJJA6KL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCICyCiebSNlqP%2Fnu%2Fn3nbrgG3byyCCVIE5j7dq7VuafkyAiACbMGIBBmxjZJk9gLWV5ht3v6jAeVt%2BPV9N67%2FyRQlxCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMZn2VblJu4MGvXFSGKtwD%2FuJgcMFY5khdo9hx0h8kE8qq7zwxTxnYGMXnjoPnD%2FKp1URe%2FMgFACLMfQuYyO0BwLfAPS3psyYklpH4oJ3vbEz4dwCk6n4iHhNTP%2FuyOaVBf4qqBcK1hS7kT8e4IzTrSqdcPyf2RqZXWAB2EyO4lqOB5aRTZ%2Bh4vMT7nDDCdDkEa9zB1vGc%2FtukIXZNdbaI5539ngj0xySZDzuTooJk5xAFp1tW65PJdSlnalPlIK0kja%2F2CFgU2vTqzOZddtrX%2F4czj4cbCYzNBqvlziGIquVyU6vSaHLVs1vkB5TxaaZWElfYIbWGP4i8bZfrE%2FM9Ceazxv8yXCj9IWP1b%2FzgiqWMaNMaa0vV1yARVc7eR0yHG4Oe%2F6p6XAc0fGcZ2%2F9pOcROmyectCsHCxl4gdZbPG4TpJ4S481JpoykY9%2F10gmC89lcNtB9sl%2F%2FHB0DWbBHUJUjv9bhNQGNh0dHmu%2BqrStveNRQKwFPripxzO9M7wqXtEaiUJPrYfX8o1d6971TSGO%2Bm%2FQHpVQR5Y8gLAhOtAe4YbVzv%2FF7Bxc4Fz%2BRq%2BlEP2FQmQB2bhIMEAkKLHuqNpgJmhJcebMGPGwVmKrA35CmPu%2FDC2Ss%2FYWrqrwQZz%2BbV53Aty5nw9qh4PMwyoWGvQY6pgF%2F0rkEbE%2FS%2BzyIHQwlL%2BDD7WVEAIgjG4A6vCYXnLynfMctpx6nllQHXAG5ce5b01bGc79420QJzMe%2BOpY1hjgEoBuQF0D3a7d4z2DryX25%2BLdTpO8foh4zbIIRGZXVV6eVB2F%2FwPJDsS0%2F5cGbiyxbaXbcioViqyedaH89tyfCg9FQzhp05EyF4qU4fKnNzjIFYtOeRimUm8XnQ2aKzmd1fGg7%2FqeQ&X-Amz-Signature=e826658024ca17bb70518433bbedc6ee33d876d842938e10a3b138d0de594bd7&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XKORF7I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIGwW5EKBn3pRFKijWfFobYwRNl4nfK2G5Z5cLwcg70d%2BAiEAsvXB79WlknJztRVNvSkMrqDbu1NqMZX%2B%2FOAH3znqLzkq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDESabGohq0dMlGOmqircA%2BXo6h9HrjOyxMq3sysSPa8SB%2BF7YQi1cmjUVAwnE2FlyYJQKa990juXw24%2Bz8YH4MxxN%2FB0J9ay886fPbQ1x4v%2BfY59Qpf9oJRv%2BfLKQuBw2P8Krcr5%2Fl1yZ%2BZbZaQzADvdtOHMaSMhdecoOgENEX4bCCPH4%2B65%2Bu1q4ySVa7Ij4h2ueLAn5b2GvP47UtFjMPD%2FkVLIm7VWFYWnNqhfRXsHa1Rv4e8g%2BzgmM%2F0cxooUbiP7rzGDPWc8BDkDgS%2BOg03YvYQR1jEVRjHDCETV3EHVQ3DGzOBSP69LjMQ9tyOurAArv%2B6JunoW%2Fcq9E%2FW4uvdz0ROX8EN25srubzSFHg%2Fq24PJIewuDl0Vzuk44Jfa2s5aFuFO33dc84ab7EqF9gyYwussDhQbkcIQ6Dcj%2B0S7Yv%2B%2Bq5%2FcuLprPf0u8TEDMxlvca%2FE9BezxM3Pn8fXm189fiZiSAaAxZlL0sfHLmmOtDdP9548e477l0Am2KtP5XSO0JdwUHTthOHGST0u0KGt6Gt8KPNttZdRPV3OwJshbx9AdtTBLoWTF6xm8YPe%2B%2BORx2Ry62n6VEp7vFQfg5KV6M2ZZ02IvM8n3ITPqsIiv6LmjJE1m5SaQIXhUv72fAgLW7zip6IlFyYcMOSEhr0GOqUBku4udqnngr8Le5NmGRXb0aT8hnquYr95S3kQWy%2Bo8eGwpGy9%2F%2FLWAHjJSWd0MwLU%2FiAOKmpOggOZnQIMuq4Smnop4X8gxjWni%2BraUiIC23eVjA1TAz81EI5eVDSk3oimLrm2HRQFJ%2FlifgM4hpmyo24QTQYVgWCxYoo8lPfvHHzafEPcWsRL2oNxHSxPgfGb5B76plkYWCIVxr4dpKZzY6dyiuHh&X-Amz-Signature=97df166f1d9acd8f6a81136de31a0a966c2c0cd20bac4d6ebf1dc406655cbc55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662HD326P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIG9xD8uEbdpaktd387sBQM8TODZTmsLUbacxURXRJXYqAiEAlSpePyoCaOvnAye1n8eHpIJbOX7KwLwpd6cBxiKBeYMq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDFDRBDB1v6j5ycn0GCrcAyjc3UGEVJ1CNVWc5Hyr3BV3XdKdXYdRMwdg65ToNFzLiDzUKrXd0lk3P6JQ9rB68E61D575KOeNGLDO4p%2BJPYNwIXkZLvI96AqKmpZ2pOP8jn8VKfk2OYpVnVl72Tt784bK%2BGRVHMjE%2FSOXseyqBJhYm1euAMdXUSaHUQPV8YQ3udW6iHRUPccEJG%2BokJg%2BLktZzGUWDlFhis8RKpWgTxdew3i6DmI2Ck3tX0kubAtuoFShY0WTkDfecEVlqlbFtbPtoEFfoMY4vacFR3zt6KQgzBrPc3xyKUA5kXGdQNi8Q11aspnqOYLE0xrb6t41sbc373v1vZuQBxpFONzlZVRLCFxMk%2Bk6JzuBoMARmkDW2yYfGT3TXnSAeFgfoXh7xcBKiizT5FJPkt2smCf5FCkKGbXUxg2SVmkBenuUwbRN%2BeLFCnVMhE4DVrOzV8JtQ7uowxwEs0DDMkcpH6pPXkex0PCQb4Bdc4rpMDFUVkSJRmfmJoA1paeMqziklWBlf%2BsbBZOMqWIwu1L9AIzCi%2ByP77xgwpY8ebpUGWrbtwAKjHXLuKMnqFp0tzs9A2q6XqmsxEyQk2VnvRfpWQqZZDeOAY2eww3dxuLbNvcXJEQdCSSfQeRr4QElwP9zMNmFhr0GOqUBLr1ubMyPkl7x4HnTnv7A2jewmuKnV7qO6l8u9gXPcefBHEF3TpV3d%2Bc4K8Wa8pQGoGcjbUQEIZi1pdxxEaVuVeCwIOUQdmYC%2FcDtNBATOC7avBoji5czqDVeS4xqtHck%2FM5%2Fu60HjOrzBiMQAzoCp2cIN0aEfcDWqo%2B2vlylCQkta1lFc8%2FdFbfe%2BOCu5Hw3nCfuOzOGyCOdLqOezeUJ2n6KYFgL&X-Amz-Signature=dcefc145b01d82f3cab90169987a6b70dd9ab4346db8dab767d6a2a92cc5c3ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665J633MLZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQC75IzdTIBef5prRllcDl0xh%2BUQr4hdEBPUrLeSCVMS6wIhAL6l6nr2D2mfbOZvdmsFVUw6GrKfNSs%2FxuwsP3J29nCsKv8DCCQQABoMNjM3NDIzMTgzODA1Igyk6GGOfnCYWtJBVNsq3ANUv2O3caUHmrH%2FnwRWlCqXYEF2Ch%2F838fot1qbJvDEbm%2FoE7KNBemTLA44T2BthzRFjRfSKJPaRxI6wFO9uULCAZWFSvNiRsXgz%2BnIqO4ORyoCMZEJ%2BV9FCOb44HxLFVl8J30%2BqrcY62hSVadv508zGGyRYE%2F%2Fzf2rHr2hdAxWTf3tdqWGU6qoqWYR0CM8z00uXQ99MJKAtMHQqGY36Nx2Cht1PIkedXRTcl86KA6yJA8VPE0DMWvbzI8QUxBq8gcvqmx1%2BWnLlo9Ufi2QUiezh6fu64i%2FuaLRqRThAKVF9jA16X%2FICHgv49zhxrjWaUbm8BKq9sWxo1cYy8Cm87qHYqQG20Kml%2Bv3DmrMeVHz6ts5wSSmdw3pWqmTpJdERD8cN%2BPWW%2FOwg7We%2FJzgJUmEoXaW6O0JsLf3oZb3Ceow1bFIM4mjhJNDA750Cwlw9uR0SWazsmxQ3yGri0G2IBhXToskShk1%2F4VB9MD6pZn%2BehPLQq68vXsSD3c7cOJL6PgkA3jC8J1Y%2BvCfY23F8Uivz0WAeSFMuJRmFZRUBDGHk79SWZ65nsIzxynwOBkjz0brmIB%2FBKoAR%2F%2B0N%2BLMzM9%2FCQhiDNEaF5vEJfNKeohSh%2FY3OuzaSvWmLjAb8zCxhYa9BjqkAdKX%2FqdheQfRWvF1WrCUDTsL%2Fzm6DfjpGk6sZITBo%2FQywYsDn7kfX1DbcU7slGdfw04%2FFLf7KUhJdrVpuej5i%2BTFh1KgajawSdNOf3Hlcr0n4HZvOGZQqRMbSn%2FDrRPWGqaGEQs0CHGLdcqCBKOTqWznBh05V3ElCA%2BmD3M%2BD3l4VIGoaGm4kMkVqw3WuOwcxXnYI6VT6YrVfmMJx6zDH2zXJ%2FmA&X-Amz-Signature=8ab388d24a515bf52107cc68a712581600c5aa97046e8b1cd2de26e915bcce7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665J633MLZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQC75IzdTIBef5prRllcDl0xh%2BUQr4hdEBPUrLeSCVMS6wIhAL6l6nr2D2mfbOZvdmsFVUw6GrKfNSs%2FxuwsP3J29nCsKv8DCCQQABoMNjM3NDIzMTgzODA1Igyk6GGOfnCYWtJBVNsq3ANUv2O3caUHmrH%2FnwRWlCqXYEF2Ch%2F838fot1qbJvDEbm%2FoE7KNBemTLA44T2BthzRFjRfSKJPaRxI6wFO9uULCAZWFSvNiRsXgz%2BnIqO4ORyoCMZEJ%2BV9FCOb44HxLFVl8J30%2BqrcY62hSVadv508zGGyRYE%2F%2Fzf2rHr2hdAxWTf3tdqWGU6qoqWYR0CM8z00uXQ99MJKAtMHQqGY36Nx2Cht1PIkedXRTcl86KA6yJA8VPE0DMWvbzI8QUxBq8gcvqmx1%2BWnLlo9Ufi2QUiezh6fu64i%2FuaLRqRThAKVF9jA16X%2FICHgv49zhxrjWaUbm8BKq9sWxo1cYy8Cm87qHYqQG20Kml%2Bv3DmrMeVHz6ts5wSSmdw3pWqmTpJdERD8cN%2BPWW%2FOwg7We%2FJzgJUmEoXaW6O0JsLf3oZb3Ceow1bFIM4mjhJNDA750Cwlw9uR0SWazsmxQ3yGri0G2IBhXToskShk1%2F4VB9MD6pZn%2BehPLQq68vXsSD3c7cOJL6PgkA3jC8J1Y%2BvCfY23F8Uivz0WAeSFMuJRmFZRUBDGHk79SWZ65nsIzxynwOBkjz0brmIB%2FBKoAR%2F%2B0N%2BLMzM9%2FCQhiDNEaF5vEJfNKeohSh%2FY3OuzaSvWmLjAb8zCxhYa9BjqkAdKX%2FqdheQfRWvF1WrCUDTsL%2Fzm6DfjpGk6sZITBo%2FQywYsDn7kfX1DbcU7slGdfw04%2FFLf7KUhJdrVpuej5i%2BTFh1KgajawSdNOf3Hlcr0n4HZvOGZQqRMbSn%2FDrRPWGqaGEQs0CHGLdcqCBKOTqWznBh05V3ElCA%2BmD3M%2BD3l4VIGoaGm4kMkVqw3WuOwcxXnYI6VT6YrVfmMJx6zDH2zXJ%2FmA&X-Amz-Signature=3e7ce2085a8e30c665b37c704ca0a6caded0e3e096504d7b74912848707ab44b&X-Amz-SignedHeaders=host&x-id=GetObject)
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