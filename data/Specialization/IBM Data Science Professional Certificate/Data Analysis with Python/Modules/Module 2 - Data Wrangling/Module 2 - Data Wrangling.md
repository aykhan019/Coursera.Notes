

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XMPB4B3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7fxFkgnjLGH72L1KEj%2FYAE2I9xeRcbMFoqihP6gtFDgIgBX2%2F1bVpaAYrRqtfTyLZ4tPaJNC3q2%2BrOJnv6PyXpJcqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK6RgC118mxaIf%2FwPCrcA%2FuOWL1eHRL2qztHBCvvdDNos5nHm4giiND0MGCtBV6nbIHeeoZR6KHWciUGqKkn01071ilYvRNtNzQlL53bR6SwYdLre68OeKW%2BlSHEJOzpqP1LCudYorg7fxZ639USaFn%2BC3pMKGuV02jmD9zwcw8V2KSdWaQzBsH6yg8AIwD%2FCWRj%2FvHDQBpy%2F%2FzEC4WepjfYF0AM9Lx%2FCUhTTiIOFeQIn89A3zLYtkQZcW7pEOclpituQyDrEKsoTJKDseQ6Ai%2BzOejTnjVxccuGPkxuT7xSMxZqc1vgdWTmi%2FUFzq0BePu2ycpvPbxFuOleDe8F8tll3gvjPDtlm1Q4%2FdNmOnME7ZS8fyTlksXQoW%2FQ91fMzCmcZtX9OyPJjDCD2IKENAvkBiRUc06MopBsEDKZWaxKBXMMZnzFvEYVSZjMcG1D4SqNJtp1eixTwQkPIDdHUGQoY1ozB3sR4PS8S%2BSoKI4YzHZuiSG9Z47x8VUYvJh1aZGAxxo14xWNt42Tw%2FyXSWJ8GdDgjmhmxE%2ByUlNisUtx1WuaXFMxH%2FKGBbn34FyxL3NpoZ4FUEog8enIT88vTRiGz3zvHa0Mi58FQw07mRcXrN5tKB0C9j7toDHTj%2Fr2oDaPDeJcFadJfw4LMJ%2Fn6LwGOqUBweN5pu59TlAdg6yqTSGAxPP9GJaSTI1EpsTLFxfSN46jiHc9WczWl%2BlHwBpIxlmeZtcHPFv8tqG%2FXY7VdIYLMQsAABTgetmzwPqhlhGWWYj60LyaRkbOAsbecm5LLrTVBRJ9euCeZkERLRqo6n23bdo%2FmBtr%2ByK8Hj2%2B9jH%2BzbthuSJW%2FRnlmJKM2YeWWRB%2FIswLOnAqIbQ6C8t%2FgjU0oMiMSRi6&X-Amz-Signature=3f616acbb0ec66c1472f3b4221a09f6fbfb947f53d7d77cd7264af17251dc3c0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636YPLUOV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2Bsuwr%2FrD3dhteEhpDLG89ksiP3T4%2Bxf19nLJdeT98DAiBcLfvD7BdYUjEfb6iJuLnS2OZBxDcELOR%2FlBxpsCvc%2FSqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOhV1Low0%2BGoioQeSKtwD1nBe5eTUTlxpluzg2XsUsdnM6ZIc%2Bmmh26HD6Waf1IAaAtvJbD7qYYKIsP6xNc6We3NS1yh4uFdo0kwBsL1SzoS17Tx7FAvt4VrvyZri9V6gvPjW4wQXwSKSbV4CKSmojxvRxoDTN2lf20z6cv54Ru5Bct1Bu%2F6AAu%2FBhj2lyyg4%2FesdP%2FqykzrxqAeCQzevgm9jjUyAgwTzg7eD2zPzX90ysFvji5d%2Bjm7yWUN%2F%2FzvLUlGHzu5x4SE2y%2B4lOw8u0fyuRHN7q787Rf1sbK8bvRLgN1i4EsJJ5QWrliDv5hwmHkujegfso7C5FI7uH7ZYbvWQyImI7Rwf7ZzNXgVrC%2FQdQ4Z15vYaWatC4thAijBfoYGN4gTBTuTgB6oIzRzpy4uCdotvCVFOfyR24bA%2Bu1bYK7AAzwb77QSpyL0AaszxMkl6YdWPwtihPoUuQlyMUxK1RaheNwiPOua35dv6BzwVqT0xgCV1jYaQ2ZUUbGhdG%2F%2FWJFoDeUvKUuyKUJHAtWgoeFD5YNi6tZVr0p%2Ft7tUCUvtIfrmO5HM31BWKxEg7TDoU%2FDQWxTiqj5sX5L7n%2FiIxZXFxZobNvDeThgNqVlJN5xax2me0wJsqQBmzJ9D1fzAlXQGL%2BMhNHdUw7ObovAY6pgF9oIOyVcuqctIT%2BViG5VXwIMEJrkuX1pJG2yn0jd380FexMESI%2FkSsYkLWR4JTct1DFryKeKuKA1dTcg7AFHjLxO03krO3QCasqcfQhtS%2BgY%2ByRzA2sJZf6ZXqJm7th0zTehSwT8CyiqT1%2ByDZE1qbvD%2FYQtlV11ANlip%2Bbl5TqYhW9beWXCOFn7vrTHktlSBAt0farWXpP3TxbmaHdb%2BA%2FeQ16N4g&X-Amz-Signature=6be5a123bff703c4e6ced1f295dd1905481e8a450dccdc4e81650f23871b5d25&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7FKHFAT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQNck0t%2FkOnVWxRsOMj0LVcdEXBLPn%2By5%2BWa07BxXloAiAzxxHIZH98CfIJW1GM%2Bf7%2B%2B5p1jUbKVHNMXkR1pAlGJCqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzZASi2D%2BGCcayaY%2FKtwDFlFkUknihzks74vAwluk6oXUZ7yY8fkJ3q4hwMEmc54GB2vJYXeo7uf5lxvDiKgxkJCK4D8nd9A0PDtfQQJrPTexAtvMa7n9H9030n4qlAOnFw4BFcjhuNu9L0ybDUmC16IcHNvyECunI5tUCezsdZRsvO7e2utv%2BDrfLt97udjQa6grzSc38GFqFsMf3EU5Ef%2F5BwnwbGzJ49xRYSVcp7iIwBjrPN3t06RgELOJJUtIL46KZybulj2XFZA%2FBNPbVr2mqNrfcZwe4w0RPVsUW25juioj%2FO9hRaOcXarOPtEZ6K4Ro6A7bXyDkmpjD%2BUGmM7%2Bkw3zovXNVS3bmQBoDvFx%2B45vooSI8dd2vwlFLaV5l9H0N5MHB7JePLLYHiTRSfMYMlY2TfEm84jkUIQFftfIKmW6vW9Lu36VRs4c4Hh8ugNd4%2BHXRN55ijpeKUAAEqXCVvIo1KyEu1vs0o97LK6zcW1HAbfmwNHoAWNyYJc905BjOColBgUF5eEDrbRGdaY8XIyZ6AZgU1%2FSYTpjiSq%2F1Wg%2FRF5xaJ8IrAgESJ5%2Fvl%2Ff2VdT5s9kC5w%2Frj1HsQfNMna2ZrY%2ByKdOQAQqulbh94ndH3kT0T0YBfQP2gV8YYmd5zikh6%2BubkMw4%2BbovAY6pgF%2BN9994tUOIcySf%2FgfOhLcqqCEfdCfjmBmB0ri6XApmbWD1O7gykX9GJzWrvhjD0vCZoBTOKRCGutFE0AMSxXExBkckdDisRsO%2Bit%2Fp5n4Jg0I7kpJ5VtFEEyPye5nF27wkejfyAqXps3FJ1yWvu%2FEyQfiFzcydq22FfkZalxgBTWHMaVq1gRVofgQtzDpD5RIh%2Beyr6rcwq5iO3OMK%2Blr2IuLOMou&X-Amz-Signature=c6c521bc5048e14c3d18ab58966a0ed5f58fca29c6e609d5391d769ef7b3c9a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RRVB5RO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfPsGUBRy8g7N8xgNPrPYhdaKW3TlHlothqXPgduslJAiBs%2FPMoj4jhBInBSUemFXdOv8cNiS9HihsSYnN2831MqyqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMndH2VWUJhvy%2FRmcuKtwD72k54%2FVMoNrdRFKkhpP4K7ZFaIb2QSbgA3WaVrcRcbuSpZ6KRMDFjnfkSL8xjjJQiGDa5gzBHpio0HQTXwABAmujozWd43dYfeB5bWuc5aV2YxrcJ2tIAAxhM%2FKdZjgJIcamY3Lap%2FbYC26xJ%2B5mp45hxFnPWtd1rl10DeItOUnDNE43jjj4v40p89rpEbmMlDoypCtkkjuSPilgq3h55tEVRr5Nczrf662%2F698eVtaWx5wG14Fy8vRjK80QhsU0DaF3f4ycZz%2BekrICdGaAZpnqoJoWow73EormpBAU%2BJLwCE2cgR7kDM0HmiF%2FYs4hXQrUCsUUOXZpC%2FkHhAiQqADAW0PWEjPTgN7vEwZM%2F5Zc8i7WcIiEAGIDZeEBAZeXbh1bogv8Gp3gyy3%2BwEgcZFyr4kyBzYXsHP3ZxxGUfs4OfeLZy%2FWXt2v5THbV3Tf%2F1pL7oGWh9wQfpaCMZdfiQEfxCH1l3Kqq1Olm1tMweSW70czkQdOWV0Wkd%2BCjfLeIDeJw5dPV5Qy69z9GpfVJd9Os1OtYspvs01Pm8gj2yWTF5mrdaBBTYPGcAs56B95jkv8Oq6cxFlZcP%2FJwCs4ZL%2BAj4AarQu2KEgNxqHeMj29ccgh8BfPbGlhH380w%2F%2BbovAY6pgHiJ3iC2dTPLvouzBZfdBXHMZFH2jkwT%2FXiIZbqUq5ZrPVdXL6EmsYHPBgW%2BpGIHfy%2FQni4lGy8SagMLV7lcSMB7%2BEAGbgyISZupaYbIZN%2FKNNkrVyB23Q6TFoZAPbTY49VDiEMXnaeY7E4wFdADEKXUhIN3uWNzuJAH83cijtfBJcVhYBI0LvW0aqa2Yty46Hr4j8eOWZ7fuUPuG%2F%2BTmsGOqakIh7U&X-Amz-Signature=c9395a19b4716a04dc8d7cf357f1c12658614b42ad3e7355a34a3508e081940f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWXT3VV3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGsJs8r0qMehbim7%2B5fKaYiwbi%2Feem99Hz%2BUeSEwt1BbAiAFXSbAH6ffNzVNdI%2B5Zq4H%2Fxylln9uzAr3m%2FAx8JvtviqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLnUWxiubCjHOhDYHKtwDgwOIBvliu3K%2BYBqxJ68ODr%2B8wXkJ4aEQpOVfIGtjtTXZGitryegDEx9%2B7cYe3Oa7aefdaYdgTg9TddV%2BrOTb5IcGbHzP1C9V2P0K30myYJRaUfREr2dSvc0g%2FRYKybgaQIZw5O%2BiZfszz7%2FvfQLgkfdeRq6GxoAKk3kd%2FX8BVi8OBqjDxFFbws1yyC%2F0FRKM%2BPC66ZOckEwcAyy1sSoGTiV%2B8v0X41vGlYBb88n%2F5ab7fVIz9AbY0ZL0Dnmuqza4oAZHry4HhkrvcuBD51vfxwpn4I9L2x32L%2FZ1xawNjI9qsbQMIpkcl7QYFL8sK2gP2dD3MiM4d9gl%2F%2B9VXgPHteGJYqp2A2ulFNRifDw9kpTN5pTE4hYwi6YJBynn6ofgCRMq9mldmuqW%2BupS8BtnxiVLeSJqnWmmCKpK3PptQytbrUgwLSuzBHkCW2JPdjoj3BOkyqMHaYqgYAiVyYoZ8TbRNa8WuKiBKaNn9CKzHA%2BqKxPn25LJbP8OSZAnDnzndOEYn280wIJ8Mdb7a%2F0bJVExea2VhiyUgAhX08I7VL51Fd%2FgcINidvUtyruZQwW7DKNWFvuSGEp3Cu9vmIMhhJ%2BUp3ti%2FDgG%2BCqod2B9XiKUrgPLpC5QvrQkvE8wq%2BfovAY6pgEPun3k%2FXcQnbbTx5QZv8qKc8P4mLC81nkFbUVsS500C0bB16POYQd2up%2Bb8LdM4Quuta0NNVtz6qA3PtadvHfa%2B8XA9LLtHn00ZAXmBMrmlg6qhDDGQRJ3Et%2BcilutcQaKovsRa4yzjfCVnYsSenoweYMNDfN2eEHqqrKu47dseH0QZT4UP8jO%2FNgJLs6QwsdJDCL6ILYKGhJAYnoMy5DPvn3uSL75&X-Amz-Signature=f403e58effd13251b197b5f7835182b70054f7a22551ab7ed3d23475b306b510&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYX65DTP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICdVAcI2Qs6K6T2VBdmRl9CF00DjSbgAWuJ7y9WruojTAiEAgr50QJoAI8wk1LZ8l9t7nnSZZw%2BzAtsEqCHK4ZgR%2FZwqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOBnJuEcvlsn52%2BDTyrcA8Gcjvs%2BY8YfMyylY51zOmACBRi9WZl95AdSlVCHvHJukw4xIMZ9RWPJx4jgfXqNZfGbN1QR0ogOvEJPYx6B9ZVkkejN%2FhWcUZzCfWlFKB2W6MAB%2FDjqt4IIlcShGnRdCI3Lioxil4ogo2JbLiyDH88mXpaM9xrFFa1cAWthV3lQKMSZAZWXTR5PMqdw3bpC8b2ENk2McBEOyZ07CeL2luMX7%2FMZFp7yRvvlMw%2FsGG%2FbybfQKkzTvtKGxpPbSsK800XK50B1TAWd1OKMsuOgn0p%2BB8Ilx3ImtuGqqANmZGPQ%2BpmR4vB82HaaBsU0VSrM6kpjlpYA8ngroVnVKFvVDWuc8UWlS9CU4a6X%2BZLjal%2BkUGk3Y%2Bg0NhtIJQzfFgynmabMCIsxRdkx%2FlZxHXoYJ9P9fi8%2FO9wqJX4O1GvnFxMsXGPqDBnwPFcsnzBEDsOtYBNk7eJLglIEqwY7OH%2BzgJHNhKk5zPIMo%2BuDcYnpDR41PVUQtJSSney5zCs1aFTB%2FmB%2FYFCsCl0M6B%2FA2sFephLReWzlFneoQhQnS948vqYxJr%2Bx%2BZ3C9Emxa8feXDWr6DdupKf%2F7mhEF7Qle09HFqxEmIY%2BrVrMhFf%2FxFGP2gQOowhcf1GtpI5jHytFMI3n6LwGOqUBTyqWE5zyFz%2BhfDIVRvArZcm62mWcNEvY%2FQXh2wuMeRD4HsYI5IA5zwNaRyYJtNKZEY3rIWblwMac2TbkjEJOK4OrHJpXqiTfJLH4re%2BSPXUhF%2FeMaUUz79cLCt6xhv5SDlTKWa24V4RUQAWsoFawiANl%2BD392hgy0VHapH0ti7mqXDPHyQMoz9TkkQuiOF54T0w5%2Fhip7p9b%2FNWxZsBUmQzF6ZLe&X-Amz-Signature=c4211b94d358fd37d6c3ab8839f453713e55f57855464d885c838ec07c1878ff&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OZ7WI72%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC36KqjFAARxPv5ery7idEJW436%2BNBnMkv%2BEG1vBZLz3AIhAJZf1F7DQL2Ymk7TqXyn3YXGHywh9sV3n27gwEhMgHTYKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVqlSjkwDPka6xRS0q3ANeb1wajfYD8vZY3BBBX55JRQSGmCcnV%2FMb32dqkkMuaQRLUZjhcmvVwhHC3xVKWmCS5HxwQUWlO9hTreJqLxWQrorhc%2BVLP%2B1Ft4RyD1r0gDtFcaVr%2FTQiGNbtF5Y8Utid3o0yuuIdW8Fc2GKLT49v9WZiA6W3OkD61vf0Vw0fs8IapzBldhGzf%2Fc4VKjqlmvC8bG%2Fh00RHPkZQbELpP3o2Iqd8AEIUW9I9c6icsfpex0CFE5smrujOT6en28UDvl%2B7gatNigLzIbWHASU5hDXCKt%2B67qKct3ArZjrxvMdhGSSn0WNwmM69DoXFZOXM9jeFO54gql2Fu6ds1dVVLFJEMXe%2BJwZ4JAgBVL3NUaLuCdtXoQDpRpdXC7eOwM5Iu5Qbi1hSeXkev2I7G7Qk8O2qyFzYkEs3eS7jGRkF1U6zbgqGE6kPSg24H4CT1C6x5Qt6uaog81oD0FRdTvjlevMFHK%2F48HZ4RdKir9LumL4ohSzoYK6Nk%2F0IsHdkbPXK1vlydnnKFHLd4a%2FsX397gxqEu8oAGzLbw124odyLk147kIGlbPMwOcxHSFgGa%2BvgBO7Sof5VDs3wjsNljYmAwuctHJX%2BuA0jHys01VYi0KWNqpWLQ9llvn%2FQwhoozCr5%2Bi8BjqkAWupbEIBMVND1HdYfSSCjWiO5mB9synJoAtpdLt2DeJnGyzXn6rafcgDnPOIAUE0bqHZJV1EFMqAwP7%2BDMqg0vOTYhTs6DgidhHJRIm3Ub0lcomt7N%2F9MP7GimqL%2BPje7KzEFhe03TeiO8h%2BbmxH8h%2BhUqYAI4t9FCZk4WP93lu6gy4fIyLBxW99jX7kEDeMq%2FtH45HUL1eCtkjc9jEw8JLeGs1B&X-Amz-Signature=45836006d67e4a1e163dde80ff499a3916f0c034effbca578453ad6aad575c79&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXSFPFER%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHZO7pBsJ715BJfVTdrDV88NYSKGzm8p3FisfigO2Xa%2FAiBIkMpn49C2ofCc0%2FDlgaLegV7uOynv9DKV0ud9%2Bt34kCqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaCQBMaw08fkHKXZQKtwDDEguQCmDQgUasG6SD%2FyeHYAlLvETJER4sf9CkH%2BzOUnRBFzGENSZ8R6va%2F0HsDE3Rp7OajFBS%2FIYvSfKFCQQPsjQWY04jPXY4dTRAf22gaBPsf2J37w8aCA3bvYuHPkcsfJRrl3c3gm4d8DVRqdRc7lvMgtWGSTeNzaXfVvZowReCQe2pF8r41owFqETgYS1OLdFWiAULSxy7C9iCWrxyd2IDebNaIMkZoQ7kSmmh9Vl6nbKVH872Iv6rLXOD58W9MKSdHHuDsP%2BgvY0qy41Qs71cC0pua0lfNO2Nu5qxilj%2BdKQQGrtWa7KBDeBL%2B7OpBMBTnuMDmA5bIyr3MSNRQfWnTiZgAjy2zxLcW%2FJABxtQGKVm5hgYZhznOYkzJzaQfXbL2WOoLiUVZqYoakzNgJraN5sA7KhlKXq1vhoRlWcjYF5z1EQoDadmSD%2BgbzlICe0UFq28sZSrZjTBtPxel1zYZXrdMwddBMqKMhjJwOhPwhS1%2BST%2FlO67k5sWmPleLZv8VpslhM4r2bR6lz2ZWsqqdATVvl1CwdaGYNUR8%2BnHs41Zhh8MXmopvz4s%2FJowq9orQ9Puq8rzFxHnRpS7X%2FNxx3Fbt6ceXXf5JbcIDAQuwb%2Bi8Sd3a8lGG8w9ubovAY6pgHEeqCUV50Jowc%2B44fzUy2DY4gxpjxScoSHV1hRRrA0L2gF%2FRuoi7cK%2FDeRBBDEt2LRFnyoCfozgFQpFt180tZvSJtiulpeMjGlrgBwJan%2FiZtw5O7jGXiDuGjuvRs5R6np8%2BmtdTpQPorRVeVxo2NWo%2F9LlMyZpql%2BXEoi29qzlH9sgAFiZ6o9CMrUyQaza99jYlBNXM1rrrHg5OIZPY5cNub2xwjt&X-Amz-Signature=eb3c34f26ef6905d61ba5678be4998f0c9681b3b182dbaf092f807cdc1cb0692&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWXT3VV3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGsJs8r0qMehbim7%2B5fKaYiwbi%2Feem99Hz%2BUeSEwt1BbAiAFXSbAH6ffNzVNdI%2B5Zq4H%2Fxylln9uzAr3m%2FAx8JvtviqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLnUWxiubCjHOhDYHKtwDgwOIBvliu3K%2BYBqxJ68ODr%2B8wXkJ4aEQpOVfIGtjtTXZGitryegDEx9%2B7cYe3Oa7aefdaYdgTg9TddV%2BrOTb5IcGbHzP1C9V2P0K30myYJRaUfREr2dSvc0g%2FRYKybgaQIZw5O%2BiZfszz7%2FvfQLgkfdeRq6GxoAKk3kd%2FX8BVi8OBqjDxFFbws1yyC%2F0FRKM%2BPC66ZOckEwcAyy1sSoGTiV%2B8v0X41vGlYBb88n%2F5ab7fVIz9AbY0ZL0Dnmuqza4oAZHry4HhkrvcuBD51vfxwpn4I9L2x32L%2FZ1xawNjI9qsbQMIpkcl7QYFL8sK2gP2dD3MiM4d9gl%2F%2B9VXgPHteGJYqp2A2ulFNRifDw9kpTN5pTE4hYwi6YJBynn6ofgCRMq9mldmuqW%2BupS8BtnxiVLeSJqnWmmCKpK3PptQytbrUgwLSuzBHkCW2JPdjoj3BOkyqMHaYqgYAiVyYoZ8TbRNa8WuKiBKaNn9CKzHA%2BqKxPn25LJbP8OSZAnDnzndOEYn280wIJ8Mdb7a%2F0bJVExea2VhiyUgAhX08I7VL51Fd%2FgcINidvUtyruZQwW7DKNWFvuSGEp3Cu9vmIMhhJ%2BUp3ti%2FDgG%2BCqod2B9XiKUrgPLpC5QvrQkvE8wq%2BfovAY6pgEPun3k%2FXcQnbbTx5QZv8qKc8P4mLC81nkFbUVsS500C0bB16POYQd2up%2Bb8LdM4Quuta0NNVtz6qA3PtadvHfa%2B8XA9LLtHn00ZAXmBMrmlg6qhDDGQRJ3Et%2BcilutcQaKovsRa4yzjfCVnYsSenoweYMNDfN2eEHqqrKu47dseH0QZT4UP8jO%2FNgJLs6QwsdJDCL6ILYKGhJAYnoMy5DPvn3uSL75&X-Amz-Signature=2208d685c42801b09f351217e11549d8e7356d9c8ed1e1a16c26cca382427da9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2VIBCV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCD5hMsY2XRPhy6YyrsXbotlQk%2B3zzksWXADjbvYZBM6gIgJH1Fzw6SvkpPKdVbN7Z49W4cYhj7elurUrDY3ls%2FrIcqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkY%2BI7m%2FDYsldJCkyrcA7Zyyx9gVaeBiVKordoE5fLGBgb1CZEet%2FoMVbZAqJdOdI68y8TQMW5l2Nzn4nEZvVhtXYH9%2Fna8HWG768T5UgEWxercDC%2Fb5S%2ByVXCfY8pQeMfKjPsFjDXMrdeDOMjqmDDQqevy8jywBxhNU%2B3sGnIsAK1iZEugyevSIw9tIOUkAdqmyXBfW8KOLS5tDJRapg%2F3q8nrt9EGh3DqEgwIflQzE8hLVZXRvfuZd9vtYfqcOuzPq3og06gcYrzuVZUUwd1pWD6NvwzBQrdPdaW1Bft9mtSXFxdItRwQwhoh%2BtTKTgdhRbIAewFgLTbe%2FkUnlqawIzkzmedyXZxG2i4g%2BtFk1ZmZwBNiVMA1HGt1k%2Fy9gFOwh1r%2BhvdjZJkALBuVuWqS0SxdzKidaUPjkw6kRWgtB4%2BT6CW8Yde0HddC9lnJnw46mByJ96jS1GZ5xrAAiBYUEoq1wF0Ua4qKiSTBqrjrEHLjfJyAIM9qi6qpys%2FSiOmsnZhE87PBQp5PYiuS7sMg28CeM5%2F3i4laoYNmXrCIyg%2FkokybzqQXts9AeUaaSpipgL8TZJvmZsDuHy8q1uZ4T7xGtQrjUr%2BR5cbrPvgXXdBF9WjhEl9rBuaFZAWLd5uiR5IUK19nZEvvMOzm6LwGOqUBVd0PH%2FbbgpHPluVOOZEJ%2BI6%2FXNN36rtraKzNyEBu2THy%2BrzkkdWiZQEbY52DA7V8FAy7525s9ekojWIEndmeCEt6V8y7M8ksqAs6XKZuMnG%2FFN4RWCaR7prEBemxzPWoQc1rK8HXYdNCQXnqR9YUEFOfI3qkAO4wMqgnDAMPZw%2BuQfm7DgTdyiY9oI57dKRdREf86fM84XZTlsmM80UY3MdMuMin&X-Amz-Signature=34fc554bd6172c3d86600eb148e8d50fa5e3f252ccc737d4383dbca0508c5997&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2VIBCV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCD5hMsY2XRPhy6YyrsXbotlQk%2B3zzksWXADjbvYZBM6gIgJH1Fzw6SvkpPKdVbN7Z49W4cYhj7elurUrDY3ls%2FrIcqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkY%2BI7m%2FDYsldJCkyrcA7Zyyx9gVaeBiVKordoE5fLGBgb1CZEet%2FoMVbZAqJdOdI68y8TQMW5l2Nzn4nEZvVhtXYH9%2Fna8HWG768T5UgEWxercDC%2Fb5S%2ByVXCfY8pQeMfKjPsFjDXMrdeDOMjqmDDQqevy8jywBxhNU%2B3sGnIsAK1iZEugyevSIw9tIOUkAdqmyXBfW8KOLS5tDJRapg%2F3q8nrt9EGh3DqEgwIflQzE8hLVZXRvfuZd9vtYfqcOuzPq3og06gcYrzuVZUUwd1pWD6NvwzBQrdPdaW1Bft9mtSXFxdItRwQwhoh%2BtTKTgdhRbIAewFgLTbe%2FkUnlqawIzkzmedyXZxG2i4g%2BtFk1ZmZwBNiVMA1HGt1k%2Fy9gFOwh1r%2BhvdjZJkALBuVuWqS0SxdzKidaUPjkw6kRWgtB4%2BT6CW8Yde0HddC9lnJnw46mByJ96jS1GZ5xrAAiBYUEoq1wF0Ua4qKiSTBqrjrEHLjfJyAIM9qi6qpys%2FSiOmsnZhE87PBQp5PYiuS7sMg28CeM5%2F3i4laoYNmXrCIyg%2FkokybzqQXts9AeUaaSpipgL8TZJvmZsDuHy8q1uZ4T7xGtQrjUr%2BR5cbrPvgXXdBF9WjhEl9rBuaFZAWLd5uiR5IUK19nZEvvMOzm6LwGOqUBVd0PH%2FbbgpHPluVOOZEJ%2BI6%2FXNN36rtraKzNyEBu2THy%2BrzkkdWiZQEbY52DA7V8FAy7525s9ekojWIEndmeCEt6V8y7M8ksqAs6XKZuMnG%2FFN4RWCaR7prEBemxzPWoQc1rK8HXYdNCQXnqR9YUEFOfI3qkAO4wMqgnDAMPZw%2BuQfm7DgTdyiY9oI57dKRdREf86fM84XZTlsmM80UY3MdMuMin&X-Amz-Signature=5569f93181efadd0600c557581cfa57b88f5c6c0d740ea9c20b224ad9c9d7a03&X-Amz-SignedHeaders=host&x-id=GetObject)
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