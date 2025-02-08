

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOLRODKT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQC20w2A8orDtxlgxE%2FNrDK3Ak7N6bs0hMAUwdi88ReCWwIhAM4KtafHnnLUeNBKHL5aE2M3VcNbS1lvAUHj50Y5zV7VKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx33YR3yji9JzPaDnQq3AOUv3ZC%2F39U3lZNyZ8XbxkNjJjeWtuKVF4estAwaQhOqLdyE5ntsbtxKbSpMuwtru2fiaSGxEjjmwO%2BKeYfTz8WDXkDIzYVcjNp%2BjAV4SnwUxF%2B9nIHKpu3s5YaILbsK1oKSzOVbWBVIuEaYTG310rvXRAlrw%2Bmoo3Zcl05V6%2FU9orwY3yoFG2tEGTpADyCWnlgSgwNGDzBh3CGK98Kz%2B5JlVihEsXRBpUkOVc4ezfQF1Xsr06owyKZUg7wUBfA9ud4Mi3G62o44dh89bEKd%2BOm8grN%2BqA%2F6gTkvBsgELwQU%2FlRVFM0emuMEcgVDpmVJy5kSJxQaHjgZtRqutvVLr4hJ9sxJ3RNm4%2Bu5J4u%2BrOSwVb38w%2B35sxVpwR58slNAr4bJuzWFcRZKmV2ZS0kIXegfJcCa82WWF%2BXQc8BcOc956mdFEatpZBFkNusGFu3Ml5knj0q7jyqFbAAz6sSdH28xVc%2By3IVJCjnws4igfVGpNLhBRtyYM8sD6989LI8re3R04W3RzvvIMbatC%2B41PPK%2FtOvl96cpWB%2B7i8CEMbOzGJKa8Mu150qEwscN2ECvAALrm0l%2FWA%2BVBYlq0Mz5c1aQ0vqh4w%2FrRkARzU334PeMP40JDHNqLI3D9K6UTDgspu9BjqkATGaeB82f6BUfiWLlBgv11xIq1EyptfNOa3okNjx8F%2FU6jTwZaFJjmiK1StIOQtxsnMxp9FTkl%2F%2FwXdhe7Bhy6llKrdx61gv0aiRUK%2FbDKK%2FpqNxWiCc2V6MqSry3QLlnJVcMAYFYL3Cqb%2F0GWEefvHNbDJm5AUnFaS%2BBT8OYNi4Nk1OqcFFZA00mzr5Tcp%2BJRKXhfqdCVWeFiE5B%2BU70mCXFgUF&X-Amz-Signature=f978b4e8e8f8460c03a59191825bca86276f90d30c68acd79093d499a7abce49&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4Y5QREE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIG%2BxWbtXGGepZFoWVwI02mSKp254AcneaVfLm%2BZF0wKYAiEAySY0BXIwRt7JPq7MVuhnOl0bFEKolmaGW9ffHJR%2FLdMqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFO3O6keK50OrTmT%2BircA%2BESYGWkDc7CjzNXge7pJaAKLfFaG36s%2FAaG1EpLlpCAtnpcSTbVwDkm3QyYe3OSgD6n8RJWsJBh4qfAvJUECQHIQY4wp6gQiTvoixuuDLDgjvd%2BNg2emXfAqqRN%2BmdcCjIdnCjtuFEcT%2FxcM7LV3XhmEKmmPDJaum9fGJndgKRlUxui7XWvtk8RAeF5SvHqfyiV9y5zss4Iip7AeaYGukaFWcIjxZlvzpNT0MnuRRU11DuNwHx56Ic6TlcHA48UMhFSUz7p5fXTHgPf%2FqSurdaHCGIGGe8iLeQk%2BsAIEEysms9q1v9vcNLvjAIPkvGu8Ce26W9ALUwutchTxDT%2FhNju0aMkU4jj4l%2BtwRlWl0kujnZv8gtmuvdprcEmC2k%2Bd1iCyW4q8conrt8h1SAOrrZJiK0xCBeET9XGeqV01JNGvgNiqCuTC%2BNJtjuRsKCNNOlS46fsBMvo6WaRn8Ng1t7XrqDRnnca16Osr%2BAQdIMWsIV2gfjfh4v1Eb4MTXNoBzbEzLrA22z%2BSRp05zs6%2FOmAW%2F91NApNllvpBmZHUbMXJVhlkCEiYruF7bsOIT6a%2FjsYCrcYmfFp%2BwNw9jxp7FPpzJ4Cz0yLGCo1EgATO49%2Bsiy9VIR9A5YXABAPMI%2Bzm70GOqUBpsx%2B85EkD%2FAnVYJDh3Kuv%2FRW4VefSOZbJsXDspStVQ0jtgnGLJpmHbPX46M37zCYg%2BzFTUqpA5IcEnwfxhH5adpfL%2FtbEiCfZsvPrQAnMhF0%2BlwjU1QCbzSD8nu2v4j0pCGsvFP%2BnRbBJWTRk76E7dRGDQht5a%2BQL0k9lMw2%2B6eShgAEK0j3%2BfaATX7%2F%2BedpJe20zofXiMzfRK2Jcj0iV8zqnslg&X-Amz-Signature=c397a1f5054a31d24f66fe26f4a262a1a7687c1e33b2affab4ee38881465052c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXGISKTQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIGx9NB5jbMgPPXS8dTbY%2F78wrMemW1JLJxPaNs02KAP4AiAIs7f1yvhZEBqy%2BKhvL34m3FXtSCu3agMX5iI1hv9PaCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiamV06MBstsoTKUyKtwDcec4FGpyjZZQch4pYmBnhTDAxJa8ovQNpjNFfbpNCUT2ka7dkxfy5ckZ44p6NIZ8KpSAaYyhT4q1BG8efCCUM7ztnJYZuip1dTZqpsXeDzJcrhraQEnFM8Hf4NYPcjiJCF5bpaDUEDMCPmlCq5X7nUO87%2FY8q6dD%2FKkQ1ypI7XCvUO8YY7qHavtr3ConoqX2aqL3QK8EA7q3WfT6eqmiqf6BtjVGyU46App4hi8FdOc4IqtO9y%2FqfTdExFbF6VRZ%2Fqsdk0IMDTMbJXpAYHgbi2Mi7AYIeLu2qQRIA%2Fi6PifV5zI3NAWowQwCE4Hka0jL5uhBUde207Buxl0qzcU9425nxcUjKRYMTsjoXVU18jYUSSHgjtorWzSjTKUhDLOjCMO%2FX8WVL7z9G7nEdss%2F1VY1C9AYEfKfy7rQK7gjOufeO7fVX8PJeZWD4gtiTEIoNbDwPf%2FR8RZgEMIQj7ciigDYPMELTaOVu33IWKTKYoveuc3sbDpLfTBxWS8G3I9OpDPjnA%2BBlqD2VDxMtNTxjUh4YOLCt6U4Mlv32hUKuhtetIgy%2BzwdqPvCcEEKmVTZU1aFhzikrraJJjMBK0H7dqy4xGeR4FFFBlOArZvhmWHo%2F%2FcGslZuyS7PM1ww4rKbvQY6pgFbspgopcvGbEpIs3uzsiufg9ROcot6DSnju7waVaqGoMJM7WwGBIuof10vQh2CjslZFWE%2BCxYGM8laJvJui9K%2BrLS3hLpdDyiUInOSfEydq6VH92GglumHszsHjBB1Iu0aInmHwpRRthOK95GVSA9hn32qtl0JGHTbfrtKIQ99YU0ZRMNCWwh3SHsf4NqMQaFkqGB5MV8EUFfGXygx7xBVR5PSbiu%2F&X-Amz-Signature=c21655496ee12c5487847206f0cd958f1b42752b5b02766380377defa50b9e7c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VR7X4CZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIH5qFebrtjjkgAt0wGtRLsCOySkhyo9WaE6NWxNCe5coAiEAzTs3cmE1aOiovfJt%2Fe%2BulghT0zpf1m3sDRDMJ4zzUQ8qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJCVCSFmZBy%2BMt53KCrcA9M16Ts3iWsld06wneG6UU0P9tJCQjt5xvYoe8Kg4tHsXz0qlNSN4MvBK8wUK4hEvKp1T%2FicABAaUevkIXyCWlV1BpD5eBlISSMg4YN5gXnLce6c9x0YEoXTKncFMxsZYPhkDsvUm1Yz%2FPnWUyziCKZRBDalVqn5KNr%2F6Irkr2oS6kIpf5dGPmMDQRKlGfxLwP7DCH0OD5yUJ0D8E8O7fT8TV5xroasrsPe8QDEYAA9geugeoesY4MxLLVnQZJ9lR8xQsHfWrd9eSONJWBfipW0OvRhtvfECANEk0qSIFZOJ4J2AS2gO8%2BonNbireMjzuVvxcoWiqQEFrZhyJZHF25%2BYtR6EDZQacipnMSFSnvuTI4NWYRAjygNrkQCEIcX5C1hhACXx8UMQrB%2Bbgea4BdP9rMLl9H5tfmtwK%2FLbbrV2arwQ7J6DbYfRzHfwNjk8fWKqUuOXOQQrt%2F35XPHLWHpPuegnKQNxMRQ8OZmPo02v1Hx7LWLnicJWqMGA5bd0mxyaAUMqz9cPW%2FeDmqwvMAeydYVRHpLWIQRjJCwhbr5SXT2G90FSNXbTHL1UuP5XIW%2BRyShrnYfx0jMhDppoBKQj8HQxngWpbWPMiRlWPWHkuZ%2BJybG%2BJFJTNw7gMJ2ym70GOqUBrKLeSwbGjMVcU2Yr3Ymga23wauf4TBS1U3q6PJkOsPw%2BKl1TthmhUBaQTksLvy4mJdXlhWnWd94mgtmucQczn0kcqXMQc44LjyICtrNthXn5cbdxIbEmUGTHoIFSu%2B%2BXwl%2Ffc3kmtIZdFw671s4QmlalD7YhRmG9aW%2FbIEDUDbMsej20FANPIgFoWirEd1%2FJxN86%2BEuk%2FYLEhIvjw3ZfoJkLf1Yl&X-Amz-Signature=35c47995b9a74986fd0656f089713dd928f0dfb8d97910f7df4db5e751ebe26b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663IXEUCT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIDF%2F6%2BF%2BuNx1kxgcFQhHMVUSsMROmx1Q1JM6oMJhr%2FXpAiARypS1WEEEJnrv9yg%2F%2BXfPoiEJylCRku%2F591MYNMPt6yqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMU%2B%2B42BWSpuLDdpgQKtwDjBN0%2FvQWQBLRCUfYTmcs0xfiCNZg9gQZfhvOQ2jVNYa%2BDE6dNqg1j2oS2KpXDr3jxapNISBRq3VdbcRzO2des9wgc9QxYEziou20PlNDXxNFle0MpAgHvF%2BJyoQvOGW99YDmidHwcDJhDs7duEbnRLVUFxevLxX9R8BBosPwne0H54b%2BIPq5kB%2B9v0C82uu9%2BMcaFPUskFDRPSbWquaXh2KTBgFUERml2sYS1vXWRSWQ4u7NA2NFAAGRw3BRakXGcq0W3dG%2FtgHD9PkXcbK5hfk%2Fqt%2BXoIoGkim8F5%2BTbtP2hqTihuEBAl5KXm%2F3kudBlJd1hQtvSwyP0oz5V9lNc3WjIAYtKAcsDb5MFCn2n%2BNJ%2Bov3R7YeZI4Zv3jsepBINJvtkHtQuqIGrE5xPBVp8H8qFoG2PmVqyD6EdScUTcyYT%2F1tMMTXjrEEQPUKMdyfP%2FMtuMjpyqI2FmAGNffGLeDI0ZgfIO1cyUXv6a4Q9aBAsB6v0Ty3cLqf3nj3M7SKHyoSndAv3u1IawBxoQWU5uIdG8kN%2FD4v8t8mfIZELSGYgqdQcpIv4eb%2F87SXOjWy%2BnCGSAIDaM9PV6pW%2FQpXN7JuFVJ4u7aVrGkXt%2FNLlzW5WKetxP3trLIEVCYwoLKbvQY6pgFJtR4QijNl5NedrIYXMzE1UlZ3Q2R%2FHHclbyAeFQUdAqIiayv7knWwvJVAVaO681paTfiDq8Y5%2B9Nx0Xk1DrDYhUziK4o4PrPFKllWz2Di9AV3IiiO29mQE32fOotTvpHg3n4kpp0xZYby0t6NTJV%2BI5eZ23o7ig%2F8SugmlUFiXGv%2FG67xD7loqBWCUn6n51DqXw%2BsyXscGhvwgyOtf%2BHEX1Z%2F63NM&X-Amz-Signature=bc2bb14c82157f986c392c79961a12cc25ac3ab69d39d18b0c5bdfa660d2bcda&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2Y5KG7J%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCFaztZyLbIivR8iEJ9uQ%2FfmSEhf%2Fp0bCaRsuRXLRwexAIhAPOKyOBcuBd1qNryf%2BOv8%2F0SH%2BA8RLHPXZ8j68i0T4JHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7CDd02WZIjZDB36gq3APADRlOKj%2BJGZw%2FwMINuRQ7uUBtbkDTadW97rSpUNNailvP4WMyCenoZZvJXuwFwUwSkjhPYAYH%2Ba5SfOxZ1%2FzoPd2eG4yLHeOAjhd%2FxjBoRllGdTRkITAHo%2BMePzRr3UAGE18BQ%2BojABpDO6BU0z9zjxEv3vlsnkyQGtwHcIRezpmU7CD9SqOGLsAmU2AqwGbIapyn64adwJ3xZPfyN63W3hiDafjIrUxBZbryTvVP5Cetz65X0j29Jf7u%2FdT2PSz5K2SRAWXNrrwDGxAKuBAPP2PaakI7TBMCU5IJCcJiv9DpX06aSWocwhGDWhlpKXaOHO%2FaY52GvryA3ssar0Vk5wpt8ic79puKbMLliyDefZQOQStf2K6TQkbxDdqZc5QSmbR%2FQtSdiVbztKTydEqSLuJ0hmUhDQhr%2FWwS24tDQnDJ0BtjDW9acMIfMGbSvnBJkCqUrIZEG4kIz5mD8dSBKIf91QcZcA45Lg1i94GiFp%2BDenDyTeYXCyLekGQmICmCrqyzj%2FhcbH4NiJ88T3ZmqUemlhh0XMwM7erfhEA5x1WlPmX%2FSZnAlfv4dXdiBCmr9TFW9m%2FKtpz8lAONn6%2BWk2KVSQABQ6B%2Fl8o1s4y2YBvHKiLeKkZaWlACaTCSs5u9BjqkAT%2FRZbcD6IM%2BtYe6Ouy9OBPnXb3N0qwh6kkFwUkrarKz7K9EdfMb9vP40prV11wl5ndPBKOZr6%2F0OC%2Fe95LFOH51h2980NPrhJvdXBzU8pSv9j2Vr%2BjqDO2BxVa0Z3p1PcJPkYk1DqZ9V%2FEo6MUoGZer6htTmYExWVddErg5eHZNpRfLUIsje%2BndZFFoQfEr%2BE%2Fwp%2FvuoSr4lSxlRT0Xcst7%2Be0E&X-Amz-Signature=3113655a75535e40fe76230b147e670c854d807b30d44a2e22f8c7f7e89cc00c&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IPRBHZ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCWCuvTbwvYnoAUV%2BrDKilu%2FWVT3AgE6IqAMNfqFIga9gIgCa6RcHyCOZqdaRg5cUJAQJpk1L5J1gz8z%2B7DM2wKm6gqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLAUQvKt1R%2FPWaG%2BCircA1HTBq1CvxQ0ydn3v94c7x95Evl%2F5pn%2Byzv7UQzZ3QRjP78pr4HXOdqr0ddWhOvVDlpcZ8VgCHy2JVG0kKzSm6QH0%2FkkQu8PfRqvop%2FDSsJpnJCSePtERm8f%2FIwOaMuUYNZksum5ttEq8M3R05QGlH8SE%2BnsAe%2FKPKgp8UYSuqDgBTc788shisa29C6n4fd22SEINEGo3HwfUHak9DIe4HiS85E547MFpHL3SYJnaeoPLLZiac4N1z4l%2BxvbC9uxGHoiczktHOZToQ9dMooOEQ5Umfn4VZong4qJgmTRPTeQXUgUIO%2F3rEdEZLLy1JOGKH2KK6IIak9%2BI5xID7mlUuQuvBrzKNKHoP%2FGJcdjNKbRJJQIqQOyUasYPkOCfoFEfMvj2pkx0f5vv2YsLARpdFrlp0D9oUP85fQ3j26wTgxu6qnig%2F9tkkbv62%2Boa1YU2lvkmQMl3BKi04UXGjghiuSGj55eKIHNNRZ1fI3S%2FGYKNBtGZZ0Xw5dANcPZQnQGr8DB0DomJ5pMmzmVy2OK46VsoXFQ1u4Qr7taJcORxdQfjbCP34mGS1aZM3PnyzzFA6vbi%2FDU%2B77tvTEEB1A%2BOEZkppnFuXn3gHbA%2BBltY%2F3j3n4hOwxIWSbQAdx2MI2zm70GOqUBQfFsNFJL9BD1bYn1Nah7GkY7OxlRRBAoDnI5OX7h98J674fLpV%2Bmcp%2F11AZGQn4LTLDGebC0LcH577ZOgcM5EjcPDAl2x%2BZ0ChsT%2FvkHllxrfaVO4pR7QytAC0cHnOycCMU4qFepDyEMMCtV0%2BN6%2BZRHc1crDtIyDu7%2FkxJ45VNuAU7%2FSsyPuGVdq%2B1%2BEO%2BPh7Tkbd3MwAoaK6HUgLGH73jLw2vJ&X-Amz-Signature=96b509058fd1e79420ebe8a7763f4514b4df7baff9705eb39c8b7c2cfc8c852e&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKZGRN7K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCQupsWxUiYbTIV5vFeMe0Q5uDsQsbsEmf83h2t7XcKDAIhAP5tmR%2Fi7dyrWBT0GtWiqQ5xEg8F8VZMsfXWdkRoh7YPKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyi9%2FfgWBlVYgxPmMAq3AOOF4dMzhosFD7JaZ2SjnvBpjm%2BrSuqDOFUHZsb2NOEkep4Rr2YTnOkf1TU93sSmaQ5iVTkQjK6zjWNSmwJflfx0%2F71HnIJJC0sdYS%2FVw%2BSomjuDi1H2AC8XifPkt2mRFLfm7lt7YMfgwbL6EVkUVi1nkB2o%2F2XfuJXx3Xki%2FTwd%2FNvCIA0ubAZOWAlfq%2FABBHvkroX7jdmD%2BDgDfeCBGIt4q3xyHle5VK46LSz5Izhnmh2tSK4uexQxa7y1i5nbpklPfaOMeKWu3bHpYih7z4WQ00lwyFL09ueLV18uQ%2BP5u3bDc48c5QkOegncob6L8pdcd3dBXG%2FsndfY5RuOuftAg9Soj9%2B6%2FfWV1QhSuI5cMZEJqe%2FO4%2B1WqkBEXV7nj312EaXpDKAju5BUD2hBIM1abCH%2FDhPo7xcSXgUHa8oHXAbYWTA10F28zaGEaxUzo2gl%2BVQOGkEgaxqiwVHjAapNtS%2Bcna2tnx4%2BwUpA3VLZeeOJclmoljePRSDmlFlyi%2BGk%2BUrYQLATeXaGt3lPI3L%2Fz5%2BKuGZnaI6CKIaQyM4Y%2BhW1TvqYQ2a7bESyUITQgbve8XD8iTqiBT1VXMDht7gbYVo7T5Qhdi20wb1L699PZfW2Ltxk71qr0GVPzCrspu9BjqkAS%2B6%2FFjPyqxDyvYyaeIvnWTGy0JR5NDp4vCZ0ckxad7dBmkG9o%2Bix2nLhtOkesL3pEtsODxkJ71oEqzCLSLzkUyZBXuNQpo4SC67xMfz1HfGOkZQDpCZk4Nps2HrHKcYVm06G5Y1wMqaOLhJrZSvVJwCmtT7ZvHGXvVl178DHpxl0y8bZ2u0aNU%2FVxQnv%2BQrdKiZA2xFQ3CWhrVfKtskXt8OUsPd&X-Amz-Signature=0d8d2c2bf160a0686f1f319594ec9c2613731f126aa83d8b45b57738063b9bf5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663IXEUCT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIDF%2F6%2BF%2BuNx1kxgcFQhHMVUSsMROmx1Q1JM6oMJhr%2FXpAiARypS1WEEEJnrv9yg%2F%2BXfPoiEJylCRku%2F591MYNMPt6yqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMU%2B%2B42BWSpuLDdpgQKtwDjBN0%2FvQWQBLRCUfYTmcs0xfiCNZg9gQZfhvOQ2jVNYa%2BDE6dNqg1j2oS2KpXDr3jxapNISBRq3VdbcRzO2des9wgc9QxYEziou20PlNDXxNFle0MpAgHvF%2BJyoQvOGW99YDmidHwcDJhDs7duEbnRLVUFxevLxX9R8BBosPwne0H54b%2BIPq5kB%2B9v0C82uu9%2BMcaFPUskFDRPSbWquaXh2KTBgFUERml2sYS1vXWRSWQ4u7NA2NFAAGRw3BRakXGcq0W3dG%2FtgHD9PkXcbK5hfk%2Fqt%2BXoIoGkim8F5%2BTbtP2hqTihuEBAl5KXm%2F3kudBlJd1hQtvSwyP0oz5V9lNc3WjIAYtKAcsDb5MFCn2n%2BNJ%2Bov3R7YeZI4Zv3jsepBINJvtkHtQuqIGrE5xPBVp8H8qFoG2PmVqyD6EdScUTcyYT%2F1tMMTXjrEEQPUKMdyfP%2FMtuMjpyqI2FmAGNffGLeDI0ZgfIO1cyUXv6a4Q9aBAsB6v0Ty3cLqf3nj3M7SKHyoSndAv3u1IawBxoQWU5uIdG8kN%2FD4v8t8mfIZELSGYgqdQcpIv4eb%2F87SXOjWy%2BnCGSAIDaM9PV6pW%2FQpXN7JuFVJ4u7aVrGkXt%2FNLlzW5WKetxP3trLIEVCYwoLKbvQY6pgFJtR4QijNl5NedrIYXMzE1UlZ3Q2R%2FHHclbyAeFQUdAqIiayv7knWwvJVAVaO681paTfiDq8Y5%2B9Nx0Xk1DrDYhUziK4o4PrPFKllWz2Di9AV3IiiO29mQE32fOotTvpHg3n4kpp0xZYby0t6NTJV%2BI5eZ23o7ig%2F8SugmlUFiXGv%2FG67xD7loqBWCUn6n51DqXw%2BsyXscGhvwgyOtf%2BHEX1Z%2F63NM&X-Amz-Signature=272b7f0a57b79c1bbb4a1a3835374c4cad5907b6d1368c4da665a28c87d0ff91&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4J4SAHL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQChWVCHHjzXr4vPy3KLONh6rPob6IDceOb0FUM6WRuHZAIgJbc8jjM4YYmjqu90fdGQcPAGXjy3frMTdtBAxsQnhNMqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmBGbWDFPCLIB6zFCrcA4JwCjOMGFsVYqnoZlGn0k8hvAAAcLa0iCvUGT%2BEr7f%2FeJxCqL%2BjADS%2FPVMiaC%2FrML6f%2FR%2FnkYIb3vHG5FY37ci%2FQlSISeRcdLXO05HPha018TtOlAdNmbMTvwwz4xXHQD0n7r3KdxL8GpTGf9qh8FwxcUgZoXc3M27Kwn2Lx2Ff1ZznAzEOTvkGZ3jhXK5jqVvcaeyFp95a3xAxbIds6tyFd8ihzGYRklcT9Ky6OfFukiNR9O4Dd3Za8%2FE9KC%2BVCAmcb1n5bQ1c15W3NgsCe7kGVMG1hhsTVt2CbuXuuXjgrqyKr77tlcNslHZmiDTtbEcWw4FqqwjeoG8HH4OcSuMmIOqAL6lEUhOsYi7%2BZAk9buA3mLoYAEpNEa9J42F13hxaawVnMLQw4qRSUG5L909%2BAy1GTwnL9HxMN9imVPGKCrkdquNS4r8qgmFOfSon0c%2Bkhjq8Xmx2LmX3QLOIa%2B3rF%2B7erGW0XM%2F5fnPHoFZyxgZ8jFHtDJkJLdUhDIFQPKJ%2FzqpUzCAsE%2BrQnxkUemRxC9E%2F8jz7wX0CBlh5R2wuD%2BienVwEhnpJbCe12KMWrMqpOmm8yTexAyjQIe4JNQZfyaYD7myCC3SQEfVPLmpZGKmrmxJg6XUcCUyaMOCym70GOqUBmDEd5UELF2X6upKgdImGqxiAKAjHneCiuYPB7p1aw0msnUKnHl%2F%2FnPBNVWz2a7BIKB%2BxYkDYn89IX%2FzcoF4%2BKT46bR3sPNFjYA26rp%2F7TwGJYHvuFEaBL45meziOfGKeAm%2BO%2FLLunT27laTpTaCyl%2FVRg%2FSvdDAC6qjiKjBoKulBNBMIxTl%2FbcNgX8y6OtPNDyYInz%2F%2B%2FH5dotTeUCN%2BqOuwlw9M&X-Amz-Signature=0d4f063998f2c2a01b3675ce90322ee319f28ef5efb0ad55fdf7d382cb8f07e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4J4SAHL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQChWVCHHjzXr4vPy3KLONh6rPob6IDceOb0FUM6WRuHZAIgJbc8jjM4YYmjqu90fdGQcPAGXjy3frMTdtBAxsQnhNMqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmBGbWDFPCLIB6zFCrcA4JwCjOMGFsVYqnoZlGn0k8hvAAAcLa0iCvUGT%2BEr7f%2FeJxCqL%2BjADS%2FPVMiaC%2FrML6f%2FR%2FnkYIb3vHG5FY37ci%2FQlSISeRcdLXO05HPha018TtOlAdNmbMTvwwz4xXHQD0n7r3KdxL8GpTGf9qh8FwxcUgZoXc3M27Kwn2Lx2Ff1ZznAzEOTvkGZ3jhXK5jqVvcaeyFp95a3xAxbIds6tyFd8ihzGYRklcT9Ky6OfFukiNR9O4Dd3Za8%2FE9KC%2BVCAmcb1n5bQ1c15W3NgsCe7kGVMG1hhsTVt2CbuXuuXjgrqyKr77tlcNslHZmiDTtbEcWw4FqqwjeoG8HH4OcSuMmIOqAL6lEUhOsYi7%2BZAk9buA3mLoYAEpNEa9J42F13hxaawVnMLQw4qRSUG5L909%2BAy1GTwnL9HxMN9imVPGKCrkdquNS4r8qgmFOfSon0c%2Bkhjq8Xmx2LmX3QLOIa%2B3rF%2B7erGW0XM%2F5fnPHoFZyxgZ8jFHtDJkJLdUhDIFQPKJ%2FzqpUzCAsE%2BrQnxkUemRxC9E%2F8jz7wX0CBlh5R2wuD%2BienVwEhnpJbCe12KMWrMqpOmm8yTexAyjQIe4JNQZfyaYD7myCC3SQEfVPLmpZGKmrmxJg6XUcCUyaMOCym70GOqUBmDEd5UELF2X6upKgdImGqxiAKAjHneCiuYPB7p1aw0msnUKnHl%2F%2FnPBNVWz2a7BIKB%2BxYkDYn89IX%2FzcoF4%2BKT46bR3sPNFjYA26rp%2F7TwGJYHvuFEaBL45meziOfGKeAm%2BO%2FLLunT27laTpTaCyl%2FVRg%2FSvdDAC6qjiKjBoKulBNBMIxTl%2FbcNgX8y6OtPNDyYInz%2F%2B%2FH5dotTeUCN%2BqOuwlw9M&X-Amz-Signature=3aa8f0767aff50a5aac944ca7a2231692f3b16f2712eb98fb291209de841d47e&X-Amz-SignedHeaders=host&x-id=GetObject)
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