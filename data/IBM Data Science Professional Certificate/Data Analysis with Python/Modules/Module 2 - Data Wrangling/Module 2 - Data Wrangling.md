

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WE564LWG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDthhwrZEgWIakML%2BTD6TqlB9UT6JVJ%2BTh%2FOj8YEpwptQIhANy4upOA1szzUXJA%2FKJv0K%2Fo%2B%2FxFj23pyKW%2F6ooeY277KogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTEVUBJU04QQ6UOmMq3APKshLkmiP4ownx50tV9ZGTcbkSRRD7kK%2FH0EjKs8fcAOqLLylIDberk%2F0wvK97D3KUXZ9buHG4bYmKyLDAxZgI%2FxyTXazSpvu0S9O3apCtjzQTXk1vIoEq1KqvayUvar8JIod63dXMJjF6uZMDnsIfIgwPkIsjYmKMat9NJYDx9V4F9U79vUP9tLeLThnMk2HA9%2FItMRiQfHrjWQN%2Bgud6Xm7mfAixMqQACc0997cUcY%2FLEbd84w0lbX3NNWG5%2FaC6B0KE9PfzqP1T1vf7csVlBwKsSwQ2e3uN6yJuHCFhzhhtJYmjIzNVOka7UCzPPMe7Oh706br8CagwcIEVEwZuNURhJ53Pa7zW1VBqF84tAuKe4hDstxYJMBGnay%2FHGuDJhUBPU%2FX8JkQbj614bURup8m37GVeyKa4cgH36BSp6o%2BWtYtDOF1cucfdquY0YZ5AUSS%2BJvsRhKgb%2F5wjqKoMghpuMU%2Fug%2F1zVAGmhWENdr9ya79zyMPoQfCQ1qm7hioblvpj2WZxzSGbWCuP8aK4svmyM%2BEu6DzBDwZVtoj8YTyOyX98npr6NsVnM5dVhcw8MGhiBoxfoXkN4%2BcJOlvNgui%2B%2BI4KmhkbaOHV4ziRUkt9QpjXicS9Fv245zCt75u9BjqkAQCpynT3xEQZ8H1iNoGDoVoMgZVu%2B%2FC9FS0Mh6V0kVmy6pPA01gTV48mczrLikwfUn6gudQShLkMmo1uwSrLZEaKiPj0KlncQw7uzySk2dqUIUm%2BofBx7TgoU4QksTSAaHTNbl1vTT%2FSHM5VJqe6HV2G6hfzH17MEFCU1XMw8T8eEhm1AP6mceRnjkUtyXwgrSuC27md7cbWi6e4j8ixCnlFn7Tq&X-Amz-Signature=71b697e40a0907fca3100adccda3545ebde8202428e51c767330cef01d247e14&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBIHDAV2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCICytGKEZnz5Y%2FnJM4OuCkD5dzl2j5SVqnbNiIS25fy2SAiA7G5jKCmwKCTsqbmEle%2FpPJB680DDMh%2BN8ETRDXBkyRSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGrD0142evvThuMpDKtwDuAJeAS9jFPm7yGHxzCXQuvH%2FMcNyQtKyeZzZPO0IVsv3cnCFnzwcjcGY%2FACw0iSN%2FyY%2FNZgCxHMmHF1zzY%2B2zpy4Vb6Wuv4FWJWaLZ9dDomoi8sbvLhqAwWYp4PF77bEsZVjADqLOfQnUxsAk2dsZZQ3m7PLpyBplpk5LRcgntXRT30QkWd8HjywaO7lwZ5MDL8Pr06C3IuDZIazaKzMKL3mXecGBD%2F8XC9HOnaPRSErqa8vSY9uLCDMdhk67Bvkr6bDk6WJ4mwQWmxI0knd3u1SU6eQd6WpeAbOUyZFcaQlinrEuJtfJzLLaCtDUy2bAOoKgvxdm2SscrHxp6OHYi2RDTi1xp7anaKGnfV3uIhsGw%2BFI%2FXHAlktmVrhxTfzSJQo2Ub1y2uZLAYujaJKuPBuKt8yGIroo2AwIFbW7JK2lLPtSQUy38UeGs0ig0%2FWTsciBnXVWVxGhQEY3F8ipDDiTMVIVEE3HupRIuUsDBFh76cOZ9yBNPfE1B%2B0wiAEG5qBEwNKLojsnjnmZy%2FWdrKur0DgvheZLDwLOnrtJG4iE%2BNo19g0X3XdChKuSoDvp1hNtKsAvd4otbSrkDdrn%2F7cHBJ%2Bal8Pu%2FNASmmpxBArIaZJvEOZXVrr%2Fh0wuu%2BbvQY6pgEdONm9BGppgLoFdLMq8XMlmzWH0nWGJY3yQ%2BljDtUNYqJe5bCgqoULkM0v77a60DILQ7akEqAK2DJUOBpHXr3WpzAVWJq8nPZP5Dy4cOo6zHBOzxu7XOrKJALQHU6NuIVn%2BXzTqh9Vpai3eb%2B%2FlnCvAtF61S5rcru40iWPWN8HTDyuLpFL%2FiJS03fdI%2Bl2iCH%2F%2BnU%2B%2FugG8qAA93CC7CzIA5Gt3YM3&X-Amz-Signature=d657fac25405179b551bbf5e369d5d62110c538ffd853bbe09f1b789753aec0b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUAVE36G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCghfo6rvdl5FFeS3GAuLoCJvScUJbxf0SQN9i9gzRCJwIhAKoY%2BJD9mGQECYFZdBIqXs2abg8Wa5bpULDIKz88wiowKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXmLNPeILBGsXSKWMq3ANpfrtQKU%2F1QTovG77d64XulGLRt%2F%2FDxDLlYb%2F7j%2BbFXhn32DAi81xQPSfPnV8U%2BmWH9LMi%2FdtBHYjMMzBrIM3h1Au7gICCFIDof%2FrRPpCY6qyKIRWxuj%2FykhSW0C%2FrPAvZlq9fhf%2Fit3xuVtfSVti04dWHSzRqM3I4TdZ4%2FqN3CkQ1Yc%2Fc3W0b1p9ZSLuNl%2FM4C8eRPSLGzMmtL5rDuPh6%2Fa%2FKmlcL19T6XubxzBr3dX2r9cCdY9ZTirXgk9YGahN07JbAhacPkiWd0%2BdWxKcGguiLuLTL57%2BO0eBCLb9h6seTcYxULNf8wqPSpvi3SoBR1fHHSMV64aEfo0WfslYVGDGyQ2NC4O3zMM2QHnOhzM75g539%2BhYnRk8pzcvm71AISimLNVoFAwaHBzmVswgjidXqSpGJY31kJnqM7P0Q2DdH%2FHINXidVANcnpLW03LS78L46Yfkyf2QIRyUW1tgOdOpQDpM%2FpYrtesjDoHhr9XjIxPLlHHH1941pa9s6Dh0%2F0WbZD0OGvfpHxC01l5UoEKWKJr5MdsJHFYJ97qqP0lW0pAqxWsSrv3jrMCMJp0rJDYFjF9vVhPj7U2smV04Y3%2BSDDgqTS9MZw6DhV6OkSsbmP6%2BmhTAoBE07xDC475u9BjqkATfuctTPZgPNS%2BLC3aouLxH98ffdFtvaUerpqG1zxsr%2BQyRgn3siU3XaolCoC3JD7Yi7esJdlXmaq%2Biork1Gj4YnS2wZRwT8LqWRA9GYLspEK60x%2BsKrqUdpOUbvVcgrb%2FwsjNuOb0kQVXhJacOxREW8qcx%2FhYjVYvK0llmpyn4aSrwtZ6UmAjMggbChjPJ4Aqm9w5tgvbFm4m4yJJ03ecrUQvac&X-Amz-Signature=3ea9e519f7e2f3c7e5364216bc3bc8b45b15c8272df3554c11ac893463f9310d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKH47PBW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQCQI65RVHZHyRZqMpwiA2wfsTx42QM%2Fs7dbVs1EavAdgAIgVL1cHHdR3AYklNc1sgd4YsJ9U%2F87kOZbzWEiDYHn%2FzYqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOGJyyAIdQA3ZLOblyrcA8MGo9UmLhC1AD%2Fon%2FRfwS7zcsWp%2BZUu9b4w9efzo1eb%2FsN9csDR0qX8X%2Fk5nzhlQom3ix2udL1WL00UpwoBeavWZcrzqE7mt7WrU%2FVLvHTz38mdnAfmlOa7yP4VYrPnwJpNz8XJtYdkvyuOVT9GYYuw1zH44%2FDpayTUh973ZrA2URXUqu3LZgvGqRD8QTFAAnR7ETiw48hwuUrO2pZEiZ9eaCTFGhRJnfwxYdaO4ybvAiGrZssJiM4lqXTXP4Z8lqUIVou5uLC8MuUMSt57mvyDMqRM7w9btysA18aMvpURyGEugLK2UiHvl5yoXggIJGnaVEYudm38nkg6J26B86%2FVCCsFZGSDG9Qb%2BJEE%2BM4IgukVCOwvYroZffsGjLF8NMVIr6xRs%2BYKhPPq75Hebq5Dexy%2B5DbzoQA1SbkjYkv29YGeBBxxkWA5VAPHyV1yisW0nQ3PN%2Fi2nhTRb2ukUBo6bj1kNPXKkLu1uwsPJN7S%2Fij0Wv1Lk9LYo0mVkLmEkjFYx%2FeF9gL%2Bg%2BTGBIB0J4bxKIj%2Br7v1XLx6sVNrnYpk1YduUK4Wwa7K0C1hDz0MM%2BkLZllmaY1dxShGukjadqQ5dkwqKo8JhNmiSeculoXKvq7vIMbjkVwBGq%2FkMLvvm70GOqUBxh6xtiUymivbTj70zccNnWlHJPTaZNQfOpnZyLEtyapEwKzeClSsP8KJiK%2B96ydXmPIf0mjl49yNbbrfQjuIe0L3%2FkDVmRpyTdsQz4UjGqxna38yfyirDl48gawf2FxfcmFWrFr1nkgfHUquDKQQiQHWYi03qZVnfMdIdluDmhMH205yDfJH84tvjASq%2FkEWwRHVyQ1P7BE8pxHlzICny0SUnKBa&X-Amz-Signature=efcf6a4b0283eb516b708b3dd2936bed0ef9db21244d79c101d04624543a8d20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CEX4WLT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQDIAHvCuhXQ4D2QVp0R2e4pQ%2FwMji7gOh2vND1%2BSB6WEQIgR9ghh2fE3MurimcjDybn%2BCuq0fIO9WiY1HclJscV2osqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaTcbdaKqN%2FjgVh4ircAwoflc5fA%2F1etYzeYjDGTkaLzXZVd%2FnZ7EIepE%2FW9As0VFkM30Itquq2hLhkoDd3XiQhnqW4zR%2F9wqYLqjdqw5PyvDSEmEX%2Fp%2FNBmsb%2FzA2sPRPKCrpCCiTdkrdGe9wTNDi%2FxKhmhGwjlX0QL1mPw6wtdI3xxVkhu1K1bxi%2FsdXqn%2FBPY1SPnpO0vQ%2Bmdo91aa9c9EyhW3fGWhMyXpzOE2P8OKlAf%2BxyIHzkNOzJQEF5%2Bih%2FZM%2BzMazmxN2VAexHfoUapZBTQr2RtVVsrxsZU2vqybsVkPUMJxg3r11d5X6Menw2YuVeueoDP0zmI5nqOGFXxOa3SJmQDknHSkop2WKG0oUyFeZ5%2FnNEDPh4T9lIuEqUqcjaIRtTV6t2zenQKYSV%2FH4%2FgXEmjZ1BsKAHUnCooQyx4CovYGVTZ9NwqFL3qrRrc%2FBJcmqj5UwM6sfBw83ZqIaluWpM6eWytxyjeLnmv%2B5SyzDuqboCzPgCRT0GZjd4vOmb3pAF4TBYwGx%2F8ygXP3evupbtRryCv16BkDzOo5HH8%2BdpaemzXj1HnlYz%2Bit6OHhyPheJqCQf90bicthq0yh1%2Fh1SeHTuJHvivRH9hmjZtYS8SkcrICCklhTcecnKzLxy1lgbHFtVMPfum70GOqUB8NAEJ0oVNd163IJA0eqWTZWMj4VMbKGQp5IW03MZDwn3twkE9krQ1TaQUPZqg8TKLwng7N5O%2F%2FMGdai6L1a9J%2BWRBOT%2FduNaJW%2B%2FLDXXtg2FCSV5jdvHTmxIed%2Fc09tmJuAtOBzI0%2F3%2FVg%2BLrPj72q3KWnKeqiohV6M1IrB0r%2BqFjcpIk7tbmYgOzRkzny1w4smw3V5IDR91wNFPIxiZmn1w2kT7&X-Amz-Signature=c2d883d376e5b9313c8ae71bd49e53e82d45edff0b9988c9e5bcfe34255f18cb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZLMGZIP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDkX0Bv%2F8xnYLIEa25PQGUbuCSztv2A%2FqOPXpDb%2BDOSmwIhAKqCAzkPblNUZa%2BB%2BQLpf5qardr7dpyc8K5icMLn5ko%2BKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwmGKR%2BBAg%2F1WCadmoq3APkd66303dD95rFbUc%2FPWKjAnE2Bwdsjtpy41yZgBsupuwmlvX0oKNo1N2L4MQ%2BMkffqR6HP6QXdxpKeTvUl%2FPJqtccBb1TBIcPGIDNcf0uv4mptqGasz9iERQdgl2TZ5lFllCP5rYHt50KSkOtA%2B%2FCvaC6yBp4ubPWFcPLIok4XFhlKO%2FeWbj2dPbD%2FEEOP3ixDMiEiPyxRPlICzW9moYUhZn7%2FaR%2FgSa9tGqtyptABUZhHxm2q0E3CF7zrPJGjEMViTQrmg9VbQRfvWspgJ0XFDi4eKn7ltwLJQKlVsnIt6hxA0DdAswZ%2BrcFLGAkW8XUIQcd01l%2Flq432T3YzBTWnqHdwQE8AS%2FSJADYvWbnRF3D8cYKYlx9mFLhVWKjpSh4Si%2FygzhDeZYcehetGIGtxT7ATab4XaTBAaA%2BN7mLEik%2Bka7jw7YyicyOc3tu2vHiWfSawjkHkjekg%2BbwK8QSBZPSAFBZXgoRPMqMjpUsHdytj9ylzLN7YPRVB6kyhAY3j39oB1xvmwi9N6BSWqvq%2FgEdep9jf6p22TAbQ7jIbQSxIb2syUHodd0Lke5w5Zw%2BZCbpTJMUpBV1d4Ky7zdFOHJwjB1DOBnBKynw3KSyQI3MwZ5Q8WK2OaERazDC75u9BjqkAcbGh5%2BQGOwxDJy79T2f6uJvdf18w78Ph1mvRV%2BwCmh%2BMQlkti%2FpmhZ6JNgIzxiP%2FwElWd3Ckxau7JxzPrixL7qwBN3TmCLAHzZfyMyvh0NKN6VssPm9nwOfAE4wEMmENDv8AtMmGyRvpUK5jhOuJzu4%2B8FGO4CbJDbVeuzGWGE31dlL0P0IeIVDdQw2I52Bm0ksyN6iz8LZ1V%2B4RJUcDwiyzjWs&X-Amz-Signature=2b712fb41d653d915826fb890ebc032c0696eb21aa3eab03a9fa0479b4f11019&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWPTDGW3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQC%2FORoBqJIQ0EwzQuPJAmR8%2BgJil%2B6OlVHToiNwD28dQgIgLEnvSLO1NnmrSQ9k8iJFvz9xiP%2F0apa%2BgzS2D%2B5pInAqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCF%2BERlR0v%2F77rd%2B3CrcA%2F32Q0Xpm1YvalcROmWx12%2B0ach%2BeDDQ8wj79qa99JASOW61gGL3nNxd4JUNfRAitPCJq8l5irSOA6HCyaR%2BF5dwMKB%2B%2FqUvB3CQmG2vkYAYDU52PmF%2BLp6zZtuFjq2I2INcv6f%2BrRUV5JvMm3VwfUiuMUFOOQsHAEqlISkGdbz0FngWlz0sEukRY90eRAPb3k%2FT1W9QksrmFpK%2BmRowiGw6Bc0k2RTEfOqPxT4SbBOLzHG2Gdhj9slp8tmK3i02WWSAT8wthYaO%2FL8Fihn93ycCjBt8bWNpvXIR3mOP8qMeP5Nk61zT1btWCZVh7rz1C7gJXQIANyTUHQjXrGn8tQRE4p6T90U3apSqs%2BHiFXLoGQeoX3aCIJV7R7Tnw%2FZkspX8mAbcHMu7LkPFTxTtB7s4MD9Nc9VTXOYosu48jstpEGWP%2FrHQGbyQJ6QBmVFIajlovV5kmGffS5r8Wp6KFmGe0z4hTabTLoF0AWY%2FBIp95MTOppcCnclBBi1q9I1frHGYXiQbfsDwbKls8r2wU5IimUe4l4IQ%2FNjOpLX7CFUxbeDB3fkG42FniHPzAGTlCrFpVRQ27rQIy1EQJ2%2FkGdqJTylIT5JOQbqgTr1PuyMOceXk6zcvadd769xfMJ%2Fvm70GOqUBenAI45BzF3scjHPqQtUGNNnhcTstRkZy%2FwlIcASgRCExFnpOEhbHeQ2c5r8Rv7BJ%2B4pntLg47nnZQbwONal7opT9jW07zpYEjxr1ECFYup%2F4Jy%2BQmGvA0ngHXyxrto74GgiIY2woJVPTtOinclWUNSj2EY3ifnd4hwii17HQDnmUcldek4CDrgkYSLcXVmih2TOgfHnSOnv5STkKGQPM4Ctd9lfn&X-Amz-Signature=9e5e9d9075e1f2a44f0f89eb97aa2676af79de5356d8747b64dd8133ad05530f&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSG2HNHS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIHxFlYQRMc97f29KO2lhpD48ZlUnaJfs0UcxAEUp9DECAiB1p2qJi2RYCkbjbkTo8YE4%2Bj9x2N%2FzvcjKAplI4n3sMyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY%2Ba6LYvNdXQI%2FsN8KtwDn6DC3WD17EWEfFJznL%2FOCYD%2BHqMzZWDcPbaY0D3jXHeCK2ZXlKuhTeMpwwRLe1A%2BM2H3AE97B7%2FLgpjm7IR8UAJ321ixcDUUJVRCjvMpL7FF6riBzYnSvbbPvw8TSWuWp40ICYxrj8a%2FgihqY%2ByD7ciV1n3zzn61RaAgt3IDUl01Erg54Y%2FSUqVFIILrZy4g6zJUiOw57agNvWVK0Z6EbeUswDErJ%2BKBtiQFQCskAtKArADQoskJMJLoj%2Bo5zMAhu6NAfC70FxCxJ%2FmJHpTT6Ck3ej3KrnpdHtah0GdfbW3oVutbswpMYA53Q6sJpuM5NLKD48NITyVzie8iJquZhuG%2Fz8%2FiZOxbqx2T%2B6gWZb6yhtA92sfR0hn%2BxytQQUfN0TVFNPopqr0Hi6vjEzC09vKV8Pr6b4%2BS1Ju5H43PJEx8JMRcQ9EpMe2857hGs9tHPnc2%2BYou7%2F%2BY23LilWshMJABvE1OPKIZC8gOItj2Jmm8s2HgpIixtv8SQwZsBPb%2Fb88fs%2Fcx2E2KP071X3ubDCs8%2F%2FAQX04fF5rwr7KG5VxFpndf3TeoK9xTJLcGO9UGDN6pC%2FP%2BRRy51jJqsSZTqgq3qYq6E3k1B6gaxdcFCvBUGnO3aGGH2d54tggw2O%2BbvQY6pgGF0ginumjcAf4e6o4LPNpylOHQBB8oRsooJyCDY4Daidjdo321xVTD8fRCAY%2FcsGCG13q%2F6t8PxJSr190eEZlmKT%2BaYwSL1FSy9Zv1X%2B1JrLImFmPHhc1sEQVew3nBlgyE%2Bl5%2FZMYXvGR7cOZoqOWMG%2FsbP020JKle8TLYFzwuiguumOJpYRbviRgBtK25AlKAXrrXkj1I5aca3kIynQ2mnbw7UB39&X-Amz-Signature=4756b26d51b5854dbccb6679981943fa262a73edd47e9469f20ee2015a58793a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CEX4WLT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQDIAHvCuhXQ4D2QVp0R2e4pQ%2FwMji7gOh2vND1%2BSB6WEQIgR9ghh2fE3MurimcjDybn%2BCuq0fIO9WiY1HclJscV2osqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaTcbdaKqN%2FjgVh4ircAwoflc5fA%2F1etYzeYjDGTkaLzXZVd%2FnZ7EIepE%2FW9As0VFkM30Itquq2hLhkoDd3XiQhnqW4zR%2F9wqYLqjdqw5PyvDSEmEX%2Fp%2FNBmsb%2FzA2sPRPKCrpCCiTdkrdGe9wTNDi%2FxKhmhGwjlX0QL1mPw6wtdI3xxVkhu1K1bxi%2FsdXqn%2FBPY1SPnpO0vQ%2Bmdo91aa9c9EyhW3fGWhMyXpzOE2P8OKlAf%2BxyIHzkNOzJQEF5%2Bih%2FZM%2BzMazmxN2VAexHfoUapZBTQr2RtVVsrxsZU2vqybsVkPUMJxg3r11d5X6Menw2YuVeueoDP0zmI5nqOGFXxOa3SJmQDknHSkop2WKG0oUyFeZ5%2FnNEDPh4T9lIuEqUqcjaIRtTV6t2zenQKYSV%2FH4%2FgXEmjZ1BsKAHUnCooQyx4CovYGVTZ9NwqFL3qrRrc%2FBJcmqj5UwM6sfBw83ZqIaluWpM6eWytxyjeLnmv%2B5SyzDuqboCzPgCRT0GZjd4vOmb3pAF4TBYwGx%2F8ygXP3evupbtRryCv16BkDzOo5HH8%2BdpaemzXj1HnlYz%2Bit6OHhyPheJqCQf90bicthq0yh1%2Fh1SeHTuJHvivRH9hmjZtYS8SkcrICCklhTcecnKzLxy1lgbHFtVMPfum70GOqUB8NAEJ0oVNd163IJA0eqWTZWMj4VMbKGQp5IW03MZDwn3twkE9krQ1TaQUPZqg8TKLwng7N5O%2F%2FMGdai6L1a9J%2BWRBOT%2FduNaJW%2B%2FLDXXtg2FCSV5jdvHTmxIed%2Fc09tmJuAtOBzI0%2F3%2FVg%2BLrPj72q3KWnKeqiohV6M1IrB0r%2BqFjcpIk7tbmYgOzRkzny1w4smw3V5IDR91wNFPIxiZmn1w2kT7&X-Amz-Signature=5f40e3380f7e03bcc3f91e77e7562400a1fd829bc56d527d19a5026f321b7701&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XIOR6YU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQDi%2FqdXssuRZBvi%2F%2FRNx8lcJf51ZOhgjPgPwBcHK4HBUQIgZPjq01aOTE1431w3L8RaOl%2FLSE78I3Zcnwth9rjLuIYqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIMTN2KUdwPdtMOiqSrcAya35wJ3cu8NClL71B1%2FNfbs1VDQ3eQ9lU0O6oorxobjiw9c66G082mlBwtwr767uV8gFtCQb0OSymV1AYlpmrWeQsgNqS7z0sofSrz7v9cZmXlAynZ973OWmI9ahdp4%2FsX2EuK2qbiC70u84OX7zix5LrVASEbTL0u3JUi8bo9%2B9j24k6oBI0lhhL26O1eFh8e5eWvQHhhjqsAIYU%2BSDtUdpBXOsI2sIAWJxAKsRXA0SrBc%2F9c4Gdz7vvawVd7AiMwKCh5rfN0yzIrYXyaeMzJliHBBehmyHeHDoifRUt3sbjJ8Z7XsLxXE0fr%2BxX%2F2qK9AEnZln1VXjyI9qFpI%2FvNHuLNGtnFmIljA08g7bbGXpvj0cU1T8nAcHbnd3gH%2Fx8GNVzaUNHWTaNGEr7gK63%2BSKeyoERTrV3mahJzWUShHjGuxcoJvbwbD0aAeYgDGoV8uLxLCfY6G5xUU%2F6Iqg41ke8951YFgQAO2lSGVrsxyhv1WDWUtHs0KAk3F9GnH%2FTMfMLAtYbMMieJh9r2QEcQquyoYG%2F%2BYqF4SK8RgAQwZzEAQpCqDMr4kGEbboejGtC29kGz0jil71XDgaZbKa4H%2BjLTYrYVjwwN6fhE4sD5Hy3ZJfG3J8NKYNHmuMMnvm70GOqUBYpZ4hmlSogw5E8VvwhPaQlgiqjW2m%2F58CpW8Dgujs%2BRPvetHmaw9l67217AC2n3sY2%2FeBX2V5fOB%2BbyX2aj9MpvvDqjz5BzrU6%2FLB4CHijWpwY3NYTPVPDTdWoaITTqVd%2F2p%2B0kXG4K9WGIHUiITD8sA3lS%2BosOLr2asbOiiwEssyAHMdJ7h4JzAgViLHxFSR46%2Bz795rU8VmNzyvPBPFb460a33&X-Amz-Signature=d326f0ecfbbf18315f56d10cf465170f3b93030f8b5b26dc781725daa24650c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XIOR6YU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQDi%2FqdXssuRZBvi%2F%2FRNx8lcJf51ZOhgjPgPwBcHK4HBUQIgZPjq01aOTE1431w3L8RaOl%2FLSE78I3Zcnwth9rjLuIYqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIMTN2KUdwPdtMOiqSrcAya35wJ3cu8NClL71B1%2FNfbs1VDQ3eQ9lU0O6oorxobjiw9c66G082mlBwtwr767uV8gFtCQb0OSymV1AYlpmrWeQsgNqS7z0sofSrz7v9cZmXlAynZ973OWmI9ahdp4%2FsX2EuK2qbiC70u84OX7zix5LrVASEbTL0u3JUi8bo9%2B9j24k6oBI0lhhL26O1eFh8e5eWvQHhhjqsAIYU%2BSDtUdpBXOsI2sIAWJxAKsRXA0SrBc%2F9c4Gdz7vvawVd7AiMwKCh5rfN0yzIrYXyaeMzJliHBBehmyHeHDoifRUt3sbjJ8Z7XsLxXE0fr%2BxX%2F2qK9AEnZln1VXjyI9qFpI%2FvNHuLNGtnFmIljA08g7bbGXpvj0cU1T8nAcHbnd3gH%2Fx8GNVzaUNHWTaNGEr7gK63%2BSKeyoERTrV3mahJzWUShHjGuxcoJvbwbD0aAeYgDGoV8uLxLCfY6G5xUU%2F6Iqg41ke8951YFgQAO2lSGVrsxyhv1WDWUtHs0KAk3F9GnH%2FTMfMLAtYbMMieJh9r2QEcQquyoYG%2F%2BYqF4SK8RgAQwZzEAQpCqDMr4kGEbboejGtC29kGz0jil71XDgaZbKa4H%2BjLTYrYVjwwN6fhE4sD5Hy3ZJfG3J8NKYNHmuMMnvm70GOqUBYpZ4hmlSogw5E8VvwhPaQlgiqjW2m%2F58CpW8Dgujs%2BRPvetHmaw9l67217AC2n3sY2%2FeBX2V5fOB%2BbyX2aj9MpvvDqjz5BzrU6%2FLB4CHijWpwY3NYTPVPDTdWoaITTqVd%2F2p%2B0kXG4K9WGIHUiITD8sA3lS%2BosOLr2asbOiiwEssyAHMdJ7h4JzAgViLHxFSR46%2Bz795rU8VmNzyvPBPFb460a33&X-Amz-Signature=c8c94fdbf68423958a93782e5f2e9d583197e6fd574d8e5bbecdacd1d13a421a&X-Amz-SignedHeaders=host&x-id=GetObject)
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