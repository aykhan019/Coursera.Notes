

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC3EZC3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWv3XgRzCIZjcFiVOAFKDuLMDEFr0%2BiME0FOoCAbhIvwIhALXjC%2FNzLpzp0Ys247jrwGLTyJGFjw8MXQGxCuNeehC1KogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZ8xLRoL3kO9JmmVEq3APLiCzeI6HoBP1EwcmTyAlwGa2MojQist4WKUQr3xoT8qdSb%2FjVoLdekwqd70An6xyUjDuEi%2Fv8Nn2BaDnFuzAeT%2FpW30OMj1gZ%2BDCl8QrarkIPzZFtktHg%2B2rUjLS5ecFmnof7znNVvDQ%2FA4yPEXMbghRdovSyQByDYeNEjizxmHi%2FKR%2Bxlv3YG1xtzHVV54lVExnIO7oGvaZdaT3BTC%2FP6VkCmqmsZWcdW%2FlACV9PToy6XnM358TlnloUEYld9RcW1C51TrvWuj%2BL7An7Zi%2BlniHEDoEQUp%2FDVzM5w5wgX2ImgyJqLI0%2BHMjUTd162mx6MQs4%2BpZ6Ew00nl4V54bwtnRliGEhtnUOf8LTwQve7SBhMwWFCLrH2ElP9a5%2BkWx%2FZPe020lUgwMUkkrKzmdAE0vwM9pmx0FASCj8HwzwzdblJncBrjGRxB0nwWOrmC7cJ8BWsU%2FS5KZuofcm5n9%2FwDm%2Fxco7Xil40T5FKoRQUWSiC9nIih0cPrLSltK7I47p%2FVo39Cukj6IA8nTRdU8hLF4iXdNPzobXvPhnn%2FWkRQ2Bsp7p3dqX%2F9RZHluhc3soyAo8rP3zDf0a8iqw7LUVgTs50aCm%2F7PdWMDNUxsMk87I5JXKUmd78xpCkjDM4fu8BjqkAchFfBgShvjcX%2FG6uiQ9BzShjFkEy10Ozae5KYpvUFtbaDfbPZNFoBOAmw%2BEDPUE%2BorxVAOrlZ5hG%2BJQaijkHNrPyjE2xY6HPq6ZHLmL9FWe5GRIwpamnPKPfZroexhso7kzgrwTHXTPnx1Pn8nAlbmVfB%2BSAftExCAoRkU1viCKfHQC4KvPNFwKaVpIBUkn3%2BlB03OxRFNQCVUQtghNAq6qXPp0&X-Amz-Signature=b8729b2bb9c4db19aa21e7df6e8019a050a8bbdf497cb2f869a7668fad760775&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KAWBVPA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAMdneCgJYO9Zcipi3MVTE4JRG2zcTBHqgvYDKOMgxyEAiEA1hFrbXO90BFwq0F48qXGT8YlgicbFo%2BtTFWjuVjK1lcqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFURXbmDhb0EDPvJwyrcA0caTyOp0kJQFeHRilouBgW6%2Boucb1B4vR8lBHpKzrF7ixrf64qn98cbVwP9EipXNL4KtVqQvBYlbN1ZcJMh%2FTdE%2Bs4JQVzGV3%2B4o1qFvROQz8rgJuekPjyOK1LXMSu4%2BPgnQ1ZVuOVB3grzeJFfXvziwLNOS6cW%2BqmlmBtpm5TG%2BVHgWRFRrHXd1twEDIcWzBARwvDNQUjwGaqCC01PYNBtq%2BF%2FYCuRAl1Apg1Z3Jvt5qB0AQZ4ii1Wb9627eeHTOr2O0xAr9x1CPDCJGPerkV6ANwmoNYh2AauzCOiHK2QbkOE2qnOpl7MZRJ0zov63fZPNT340Qf%2Fm34iCnqaUend9BMuDU1x5yA7K7hySXf4SUfzj6Td4om5FDPCVX2bcqNN0XLhpZk8I9IFlQemATSR3enobK2jCxhLIiguOwukfgtuUhv2K4eGMrG%2FVUGmVqnBx0wSe5x1VUj3B7mNiKVFulCBJLm4vsmWuSn6zgfXdJzrjPOzZ5fxdp6ljeoGaH3CgW1CV9M5%2BPAiGPDhoDsKNkOgBkXLvNjRLEcW8erXSTl1GTvlS3wL0fMjkR2ae%2FssMmc%2BfMQZzpjXkWvZPklD9kd31QDJF%2FPzsqome9wod%2FCTGGzQ7GJvsRTPMJfh%2B7wGOqUBzHelyiUQUbcKcpwG0KCRsBRXQL34XIn%2BUk1hIZ6AVGYznswXVbxQzC88qf%2BRqRRjO5gl5gMrOrF%2FPkFkKe7%2BYPSM9d6kvj8z8wTcMVY1%2FVn8BEcSTmENA58uJn8YACVY%2Bn1%2BNm8VuGW8DFx%2FIpqJS0CKd6F7df%2BNbe1i8LOkvtpLAkvbKeVcshGGPwWT7A3a5%2FUqt03afdjZ9feYCjB08%2BAtxFpO&X-Amz-Signature=b05f3d18ace2003b0fff06172a847737c49a8738faf0f1f10685d931de27ac50&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6JYHGMP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEJpLn%2FTsg06TMTO8AVpIszv%2BkL7yODiJyoH5n0Ux0sOAiEA09IoIFWrUaDgCnB5nwV3wg96HnbbUh2i6jsyMHsTIUEqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJfWP0sXfEpUrR4B8SrcA0akrff6QrDRtkMdl302%2F5cDUezTATQLBcdBxOCmLrdC9YT63wyxGtoSgXij%2BfB%2FWs7sbOJ6dPWrePLJB7mtNE2aAcaIA9zhzGDnSLzm0S6CK%2FGuA2CGU%2Fz8vacdIBJbV3fJu3keW%2Bws2tia27YFMzN8BlHYhFD8ZaCpkbkFnQphkce0XcPplLmnmm4l9GxJ8wVdiMfKe86Ep515q8mhvF3iAZnaX2V06Lbf5soX8SlN2B%2FsI4EJAtDHWBS2Y8fDIrwfKhzcnJ0UxBYUT%2FLA9S9WFCiDihFAadCgo4QHh4Dz8Z62p0qBEZtJMuZdpkAE0Q%2FdFGhZ4lT0BmZVZDI2i3PNtnSqRr%2FFctUAZbn3GTDMTLpl0%2F3f%2B8ggEB7ajlaFzrEyCcDC%2BKcKq%2BFV%2B%2BYAQVqMqv%2BbQsco%2F19rAFRIu6gKljO9E6FqnIHftgQYY%2BTkyhWAQFI06V7VqH%2Fm02NlJ%2BimYVyxfSu%2BVWBaM0308kdQUlbekfSr6gx33CdybajKbFA%2FwrG75Fv4YgDgLFXs6x1pVL%2BPt3Yk6FXQXN3HEKxWepmFyIBYPttofde5vVvgZXbITPkfvmbR0mJhEpoqoyRs9opgq6iSn217jVGsCBt9QPrGboUemt7CfkXfMNCb%2FLwGOqUB178fx0vvovaCACKFCSaB2Bbch4CRiZsM9UzycoBilmJqlyTPWQlLxjiq08WQQeiQJ%2BKUIefh39b%2BTP6q58nw3ZUZkskQTaWR9%2BBa5Yjx0PgiVOqYQrWxcZsRtZMSS9l8Djp%2Fc7CFl4YX6pSxtWLHXRr8o6ZFGu%2FW596HL0uhGjzdgGHaCpqK4mjJxO8n5REXY62dPBqHvU8HiQJ4PdoIlpYqcJQ%2F&X-Amz-Signature=adace69740ce01c72ae6fb1165d780a595f6f9841f83d6cf213ed56788622625&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AZ564VF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCR40FMblIn3poOQkrTgPXGZuRbupmMjQHwUCnR%2BXyVUAIhAL97OTQBcSN8SS0p60HK0QmGvnnrrLJ9yMy6b%2BZHG2qSKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVr8hSk0Z1IMoUY3Aq3AMhpauGHUxR%2BfDt1%2FuREBwFImAL9vFOlcqZ85WsHLsPOX%2FXlvHl%2FZrJpQZhCj6Im1XiWhoJdD4NSfS1V9gk%2F5Wk22sZqK3Uk5KZ%2BGXv%2F1vK%2F06HW9GsEGpByuPDt0eUTReDvixfIEID6aHnkyrwmPrVvBHxXdkJyZT6AmPhurMQYfDhRyeowjDkDTT2gOEMtMgOLz%2F28U2puOfrDE7tVjCBvk3%2F0TxoWrf%2Bmy%2F%2F5MZoZAUS1qL8aktOthb7vIx9CSYgK6ueuuzfEx%2F7biQvEEXFRmNttiFsCVkmYqFptzU6w5s4Tb4B3GJl7ByMWr1aySu%2FwYj62BKdLDNb8VQ%2FjjX%2Fwgkmwd27hPZQkmrsP8HyWs4whyhn464%2FHwN34giytZZg7zswuu1FiHu3M%2BaoUoRt6YoKB92Hkf1%2ByooYGgJaylU0h8NGUbHei0RuE1rMFGeTFqrB5Tgvnl18HBF4IImOnYf8lw7pvGurxdi9Q8mcnhHA%2Bi0wS22izffxFF5GXrI89%2FgwiLbB5t%2BcYR9drYpGZuw0Yro2WeITEnt9h9FDDCEJPr8wlHnJSKAM%2FWm9v%2B1DLJm9k05heN0c12cGCMpbfyU3gUtFWf%2Fp6gwl6q3%2B0AtmfSiSv6atHAm%2FWDCY4fu8BjqkAY3jJZRwjqsiO0EVVpadwK7OpiJGT%2Fk9j%2BwGZRRBIBblRmtLkdGhlJdvX7sQnR2%2BvXfFp5YSVWGMHKpj1CbqtErP45cp11wza99rzG3J7q7WPUqxtEuGKKBRXauo4XJ895vRxuBwaC1jAV2lgbQFgZVBsg4%2F3RYRaSrRLzAk6koruTznNIAtSniM4dYTwqRpQsZ81x8wixBgH5TLCVFF9TfR7YJk&X-Amz-Signature=d135847374c302b09d6064dc7cb2ee2ad21d75dc68867e42fa43ff8f8042be6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2AH7EK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDZnRTmSSSp%2FCIHogSlFIMJ%2BFDi6OUW4mGxvnNis%2F6ypAiEA3n%2B9sFvdY3wXq5jRhvHsGnW1ik%2FauMpYJh0ZAETO7xwqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN9bXJ36pLWNWEy8circAxcbfh2q43v3sLmmoHidC4ZoSQ7Jr%2FeRJCMVzUMYt%2BLjCStRTURGlF%2FyxmD9FfmCZZbHTs%2B%2BDUXc%2BTWzZUp4e%2F47lyz0XNVtAOFHkx%2FhQNZ5vPhkacVmi%2FfxZvz9cmiSB%2FCdcEkdl61tkIo4IF%2FzvqudptvcVdvI5N4LjvDZRpMbYrt%2FFDgaEWTgDXNoTn6KEKKNffAd%2F0kFIHULHDMc6ZjuoqIdWaEisCsb5YHvuxINCPeEwmTTxwzMGJ27Gt7S14yWBbyF6mzotYuf1ts3%2BLsjpoBHgIcOso1xu0viMXoC6%2F2SvrI0n9ZaDMy8kI55T6XZ8a8Ykla8ZL0beb6zxdqAmh%2BwE8nNOPH4yKOZGOtNCi%2FIXSEJ9L9zY7Nd6Ivrk2LJYZIBwbXYjgDqITpvkYlffXOVSrJU35wQcRT62xumIhZOtegExG4k0q0iR0nAbs5cPw6bR4vT6j%2F1aKpvGYsCmWuP90Ana1ePLzjadFf1ez3bwjQX8o%2F7EPXcY0dSmL2EPCtTZJ4dp1ILu5O1eNy8qKm0G3NqKNxqGkXDGh2fVp0Z7wwy2YVJkG9itVUs%2F8XnnzcA1KnNyEDiLS4SjZYf6VXa3z7fGJNI19l%2FAJ5TvzEj1fseAc9h0HHfMOXh%2B7wGOqUBSQxFs2pFm2Mi%2BOxMXbI9x6Py1qYh8tMzf4kkIxweGdtHnvIg6RPJS%2BD%2F6T1hmUCJO1GigSnSCQMQKUmQmj0WQW7E30phHVRwFyOP2QkHfSl7gvJWrFRLlNAlq51pSAyeVPH9zHk6kJJZLTXmfERpv37rIPOmU5HXY84h%2FyvB8eFUUIASpsEN9P30CycguT4kcJKVVLuZVLsb8NF9%2FpV6n6fzjslX&X-Amz-Signature=3d295850a65e5e5775745fff0ec7c9a84dbe20d88f89c857778086db2ffb44eb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGCHIGWZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGkWrn1RBgGvNsVhUpu5TBAo0Q1%2BwNDkv8qft5ixmE5AIgOWvzLKxdM6Gu8tjAWV2C5wlecTBFTphQs9EYlJgfnxMqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAeCuXClU3x3LieSqSrcA%2FTg804XdCaXZyhhmt80MtRJ1gIMd3%2FNBIu7HP5mElBO5GfdVBicglDI8eJ6NkafhX2SfEw5CJtUWpPLOzdCEj3ov%2F98LT%2B0FInHIqojXLWovUe1en3Mm43LCSec%2FGO0TomQTppPN70I1D4NEKi%2BOioKKTST9zIlNBs9lzELceeilSq1VNJoa%2BuUTT87Er5YXlS%2FHy%2B9kIWr56xF9rNCi97Mu7PPadr%2BjPniBJW8KxqkLRIkGarZYdcT7NmZDwTe75kW8uzAlC0430cHMKa%2FZKa6F8R%2FNL1Q8aUsNSIszqPE7uY04iEimpNKOjUOxxPUgUufHaywpGY84ZNcOx6knDgf8ipZqhMXhP8NI79rsfiMDOjv%2BH6VWEz%2By7MGtm3DYH%2ByCjRVTAdDVCz9pAp%2FimhwNlJP0biD1rP5qDDlAu5PUSl%2FGBN56MRAfYDDzbmFsq1g%2FM9SJVL%2BtS9b1bsHxTnx0o3iq0UGcgX0Kdf42L9jfVvnockAmOxlhNJJvaK5ElWddHNYqtiIbySCv0RBptLmrKXqzJit2R6mhDQTmhBTuo5F5er1SnlCFjSk3fAfAEq2z9C41otPHQXfPhnkHQtJcvfuCh%2F2RDAP8CQmnF0ihdpeQJlQYeq2qGJTMJrh%2B7wGOqUB6BWtq5V4yjKJ6yhYS%2BtvGEnPfjoLvnAZaZhIbwq%2BCFvHf%2BhIeSlF7s0hNuPtnbvf7GAPDwT5hK4NhsCU2UIP9HN%2BWF1Vl0Wfzy0fIwqfPV8vVCD6kY1LEdvDC2zqIZtJPwlfGDFuDFw0BQqMlVKibOyNzhjYUrEKNE84vfCSWPTPswry3iCJHMexdEC5Mbkj%2B0UaxMGpxb3UKeiZHK2Re6Mh37cf&X-Amz-Signature=e2e59f4baae8b346b0d5c6e39f841e8b53b32851eca11514ed041812246fce05&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQBSUTU3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAu1k9sXxMorXyuavBRgyyL%2B31QpElkXLlitdMPI%2FE3PAiBQxlYKqMSzyUZEEEb23thp79SmQFrxRXZRUpjwIXXmlSqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjXijOU1VXXDJhWqZKtwDZ3Bc18ItWQ7klkE6DsIRm%2Bi4ZAwVAYznwcdsN9d423SJibaCPaBLc53Lvjbt569qocJ8jjbmuvxCSGTpgE1UGlds4StH5r7SDv98XqaV1ZkiHBNcSZ1wcSg0ONgXW5tA4Se0xqCsqHT7j7iqWWMYd3zIaaMelkzwem5GNzmwEyhcj3pSxYybJRO0yM5MreY8dd1xNRuAAX1bPhjSKWLNwztNbD1eFJQlWv7xZZW5AXucJYqF5uHQL2kenQJvNdjm2yP5eCtRwUjr2Jg6KM9m8pGO7Szti4B4IF2jwgTHc74FiJ9bkw7CbWAuibZKfHZGB64PsvpGpd%2Bw6VImjs435uTc4BAZe8HW7d6QZeR2Q3F0FpjVGCBVTRsrc00%2FHnj2ehnd8%2FIrHA8qZYKmaaZf42GSUlBf%2BeMbNnq39xfOEcc%2FS6ltB6VpWPX8lOQ%2FoJbo5T41jM6PhOZ1BV50sMWlTKN%2BnQzhscCu8ASfGmpwbrShtx8SPmxraCqDN38DEctwVexgJcMskdbTJe3JYP%2BVnx09YFvwSENrHpgkb83Vmp5wV4Wt2Gl6kuN0ieYGIpHSMksSOtIs%2Bq%2BgiIHNef3%2BxrhTyFxbpvi8vEL79zCSwcSD8kWHLBz7cUNSF6wwqeH7vAY6pgFNKVujI1B8P%2Bp5FuMdYSTghFEJesCcpUrO7iZDxkRzaWcNv%2Bi4yM7Ab%2FgQ0TI%2FQFdnJe%2FBdBeh03lu%2BqulSDCckYypLBDibJP4nxIYQ3q%2FJgfmEe%2BktQNy6XZG1TVPQe6rkz7ffgTg06mfExBUOewnJlmNTb43Mja14O%2F5lni%2B4oU72bdajWLjmr2LOwE%2Bpw5CJ9Cr55sMqOEJneW0kDPPdVP4yvvK&X-Amz-Signature=06cc7e82e4074a887d21f7dc3951d5186adf55cbdec3ddc69c2b249ce33e5969&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW2ILV5V%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2u7xcn%2FGYAKpq1Xp6es8gwrJM5xSDSACP23bpC67K7QIhAKlccDiaOFT3e20vMvruy1kjbgc4uVKQoyG9JJIn1cWFKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwzfVw6OQYISrntSZAq3AO1rBu%2FaC71hKJGXS1R8IvssUKZiP7%2BgbSXInFd1DKlUL32sPjGTINuiT5jAfhGwsyFbueYzeyNtH62NSt4DI6YMqrzWoqbWaQzcYnfYi7lhTnuSAXF5%2BKyUGEYQwXIRXvJBeiVHuRilttjaIhhgqxRLQsqlXztU0yf24pkaqvx8qYzUrvGUngyK59zDZW%2BXC60jc2OT0IeMjFCOSLLY2a0wquttZPVkySrBo6CW%2F0zwXkZ%2B9%2FeYz%2B6QuiYwZnsUZJKD131qyLI45gTIp7bBiIy4c6bhmZQE%2B7E30chG7BqopmqBnc%2F2m6I0jWbLlOyyC6UH5WpdDoiq%2Blc4u%2BPcrQ1t7M7pvpLDl5sH%2BLHrVtbl%2BJnadSsDfhXp6GvHQNbhIgruywsezhyqX3Nz3diVLv0j0HkxCFYuk%2FmaF3my%2FaleXJN0x4b7hRoOcccvxzpDIN0ujG3pKJmav4HNDXXejQKlYpX%2BChvbRvmo%2FXSD%2B8g2zbSoSId9ClD9DOm5LM1IIPDDXd7D7h%2FCNyFGMISXoOx4t0verKOWjOrVKM9OatwX1KevE55al3xKos6O2jgI%2FW%2BD%2FIRPSuha4P%2FnHhXoF2U5q2wkBHhO01fFZix9Jxnd2MNKq78jf67H9r%2BhjDB4fu8BjqkAQPbPdKbW8IlD9B7dh%2BT2HxOUrqnvTBrqKRIxLOhN6doOxL79NDkbNwbg4RTSNuBWVNTRqSJbma%2B3RNC2IyRQYfZwG5NzX6whQnRdWW3FPCxLAEP46XBQp4kwFpYt6U%2BE3XIhDVXCQX5DTn%2BIKylIZl0v1zTBsmsVhcg9ELwyLMtq45cgN1NjwS3JXZJ4XE7GNOWwPey9v%2B0DbxIbVQvOtEBbwQv&X-Amz-Signature=ba95c604a36a2ee6bba3c0636bd0445d1480325da632cb7efe1457fba4fe2ec4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2AH7EK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDZnRTmSSSp%2FCIHogSlFIMJ%2BFDi6OUW4mGxvnNis%2F6ypAiEA3n%2B9sFvdY3wXq5jRhvHsGnW1ik%2FauMpYJh0ZAETO7xwqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN9bXJ36pLWNWEy8circAxcbfh2q43v3sLmmoHidC4ZoSQ7Jr%2FeRJCMVzUMYt%2BLjCStRTURGlF%2FyxmD9FfmCZZbHTs%2B%2BDUXc%2BTWzZUp4e%2F47lyz0XNVtAOFHkx%2FhQNZ5vPhkacVmi%2FfxZvz9cmiSB%2FCdcEkdl61tkIo4IF%2FzvqudptvcVdvI5N4LjvDZRpMbYrt%2FFDgaEWTgDXNoTn6KEKKNffAd%2F0kFIHULHDMc6ZjuoqIdWaEisCsb5YHvuxINCPeEwmTTxwzMGJ27Gt7S14yWBbyF6mzotYuf1ts3%2BLsjpoBHgIcOso1xu0viMXoC6%2F2SvrI0n9ZaDMy8kI55T6XZ8a8Ykla8ZL0beb6zxdqAmh%2BwE8nNOPH4yKOZGOtNCi%2FIXSEJ9L9zY7Nd6Ivrk2LJYZIBwbXYjgDqITpvkYlffXOVSrJU35wQcRT62xumIhZOtegExG4k0q0iR0nAbs5cPw6bR4vT6j%2F1aKpvGYsCmWuP90Ana1ePLzjadFf1ez3bwjQX8o%2F7EPXcY0dSmL2EPCtTZJ4dp1ILu5O1eNy8qKm0G3NqKNxqGkXDGh2fVp0Z7wwy2YVJkG9itVUs%2F8XnnzcA1KnNyEDiLS4SjZYf6VXa3z7fGJNI19l%2FAJ5TvzEj1fseAc9h0HHfMOXh%2B7wGOqUBSQxFs2pFm2Mi%2BOxMXbI9x6Py1qYh8tMzf4kkIxweGdtHnvIg6RPJS%2BD%2F6T1hmUCJO1GigSnSCQMQKUmQmj0WQW7E30phHVRwFyOP2QkHfSl7gvJWrFRLlNAlq51pSAyeVPH9zHk6kJJZLTXmfERpv37rIPOmU5HXY84h%2FyvB8eFUUIASpsEN9P30CycguT4kcJKVVLuZVLsb8NF9%2FpV6n6fzjslX&X-Amz-Signature=0ef72e642ab85dfd1ec7c6c51d527abe4a2d00ec4e24f1d15c9c68b1ea6da3da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQV72NHQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIETJco2iKEmtiUY5qzRaNASr2KtTHGFauXu5Xj0yBAaLAiB2ovslxNeII%2FOC4Ns93s9od0ORC3s8jPMkDpmm86PRBiqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRbTkmoS55eW4VLlnKtwDqg0vxmTtxooJVJpuAqSWXtGgItss18XunRtff2W8KoxJNNuNJNehy20JtjfLgVw1qzuZm0ar6iDJArsd2G%2F3vPLhdehHdb2J%2F3RyE%2B%2FvXzlGdjCB2qXNb9o14q620kXNJsJepe6xGpZ3jouaUJLiZ%2B7s1AuyvTZpIqVGYr8x%2BM0Jmp4iceFxv7%2BEAye4s8dMVBJiahzQ%2FjSAvxSbtOJaBtU6aigsiOTw%2BJUSHbhK6DxZdPDovujIUmPxksjWmofTiPRrwrEQBYsB4ekCbxm0OglRli31oN3tABJT%2Box9%2F6DXRW6uYIied20ImYABB%2F5V0wKlu%2BziRFS6yq7KXIF7GT6qByE1nWmd%2BXOz2sv9jjhd6Hz7PA4bhY7DUbv%2B2LoQ%2FFJgeJvEkAzp7lGfNTlQ0GtR%2B9M37T7st4Cbj7Jb%2BTvDg%2Bp8LQLl%2Bawuh%2Bf1Wn8CWhCBiUIp%2BHuO%2FeZqqXIRG5xLKjbero%2BIfpW8AnPWVWE8fmOThJ3hag%2BWCry5IIjJYU9ZCVMhWWmqrEG78%2F5jFWSyreCsdaAUsF5dtlQPRlSGlbXSET0YyCgCfV1QUlP4Ab4wqahpjgS6tQosymwxwhxO65BuEV8Q%2FgQASNPMV62DTtuUtbnPMIBVbhEwzZv8vAY6pgHMKeWhlMDK8HSTgGcv2otwvQZGeerA1WcoRjP0lWg2fECqiW7RU8LXbdJfv%2FHu%2BksJcjf5gZVbdknrAFguIpGmCG1M3%2FSVynXntBhPxaFnQy3xGbuBgitj2TEhXngDGR3FbIKML11iA69CGuqiKPWL%2BJOSWcMYGY3D%2BurDIRP2Wz%2Fp7fqtwQ4b4cUlxrnNDUcjNRct1wmEjhHkv9Mulb6thVMkFiCW&X-Amz-Signature=89aa86a82db2b019eea7511b4fd48efe991b2064798aec49822687186b471b0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQV72NHQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIETJco2iKEmtiUY5qzRaNASr2KtTHGFauXu5Xj0yBAaLAiB2ovslxNeII%2FOC4Ns93s9od0ORC3s8jPMkDpmm86PRBiqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRbTkmoS55eW4VLlnKtwDqg0vxmTtxooJVJpuAqSWXtGgItss18XunRtff2W8KoxJNNuNJNehy20JtjfLgVw1qzuZm0ar6iDJArsd2G%2F3vPLhdehHdb2J%2F3RyE%2B%2FvXzlGdjCB2qXNb9o14q620kXNJsJepe6xGpZ3jouaUJLiZ%2B7s1AuyvTZpIqVGYr8x%2BM0Jmp4iceFxv7%2BEAye4s8dMVBJiahzQ%2FjSAvxSbtOJaBtU6aigsiOTw%2BJUSHbhK6DxZdPDovujIUmPxksjWmofTiPRrwrEQBYsB4ekCbxm0OglRli31oN3tABJT%2Box9%2F6DXRW6uYIied20ImYABB%2F5V0wKlu%2BziRFS6yq7KXIF7GT6qByE1nWmd%2BXOz2sv9jjhd6Hz7PA4bhY7DUbv%2B2LoQ%2FFJgeJvEkAzp7lGfNTlQ0GtR%2B9M37T7st4Cbj7Jb%2BTvDg%2Bp8LQLl%2Bawuh%2Bf1Wn8CWhCBiUIp%2BHuO%2FeZqqXIRG5xLKjbero%2BIfpW8AnPWVWE8fmOThJ3hag%2BWCry5IIjJYU9ZCVMhWWmqrEG78%2F5jFWSyreCsdaAUsF5dtlQPRlSGlbXSET0YyCgCfV1QUlP4Ab4wqahpjgS6tQosymwxwhxO65BuEV8Q%2FgQASNPMV62DTtuUtbnPMIBVbhEwzZv8vAY6pgHMKeWhlMDK8HSTgGcv2otwvQZGeerA1WcoRjP0lWg2fECqiW7RU8LXbdJfv%2FHu%2BksJcjf5gZVbdknrAFguIpGmCG1M3%2FSVynXntBhPxaFnQy3xGbuBgitj2TEhXngDGR3FbIKML11iA69CGuqiKPWL%2BJOSWcMYGY3D%2BurDIRP2Wz%2Fp7fqtwQ4b4cUlxrnNDUcjNRct1wmEjhHkv9Mulb6thVMkFiCW&X-Amz-Signature=8a77e8c865ca43ec9a0a50ae786a04b13ca169d8b5daa0cd235f17eed0805e4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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