

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YE4OP5L%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvhRwtIVzACNcnKuUqeOf4uPfxFZLmp981HbjYP9DIaAiEApiWbxQ66sHGSxoGsQ28UjlCVRAzGHkIdnfStpl85iwcqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2BFqZYbtWpxn4lIUSrcAwbT5xpucSS6HFuurNjkWy6Q87xzASxplFSGVKgknQd%2BU47Ivt6nV%2FYjBolAyJPcw%2BEuvCPVVo7DR6%2B86jiEit3kQaAAgmuuLuge3S%2F6cuALT8neJd786Rnn%2Bc3ct7L4zO%2FRlhPOeOYNrSBYe0tGuwiWtoM9V%2F6lEfSRAjZPU%2FSdLrlUvmI8p5yD%2F8z0iA2NtZAKUK8HSxZeox0W8tmw2Ivj86yn6dARKlt%2BdI2owX%2FOABxqJrKPuvaqbJn%2F6%2BNi6ddGyh4jT3yC4X1kRAImGJ3VbkB5DgLwxIxIP94iVlLEA9qor2vX1%2BrGLHBjANFBrNLVFcii4OIr1N9U%2BoGve%2FUixyI4fPfs3sDlG65xOBb7jrd415m2qaZi2xHF34uPx2Z20xoTAYElCHlYqUCBTtO%2FJe0CLLpvsrKLVsgzwmFCI6F%2FmIoaoWIQfXV59BrCwKh6%2ForgoaVZwoDwvCdrYkPA6sJtgwaWXtYH%2FIe53OLIZfxzRO7E7y4oxFOZtaTqeX%2ByNQdTkzwyvtfUeqgmkM%2FNJJPeylX%2BAB1DC0G3rcXBJpPb9lotK6YddRb2Z2fKcxBVcWxoKkG%2BLDR4Ppeu4wjC%2BtnKlLpOVaByPCduWbEsAIj4RysHVZ12ZPMpMNae%2B7wGOqUBlnk%2FowoPj5%2BnHWAH2CMPFYchfQ9bF%2FLqTYf1porSjRhnvAY6B5zkQzYnr%2BZIlscBXRVGo6ZPVvornS6pwcsmwYNDlrYtkyCjIRUX31QMOPPIUmgRZTWehsNMjLN%2BcNl8Mzn7NjJWfNXm70MUOa85FVVyGga3QPk6QrdjR8PIvt4H1jGgAsPPWGGYngwK66TE4aGHoKzvitbchk4rOvNvA9GPwS0c&X-Amz-Signature=5a31e5216b0b873567e8f839cbf8328d0c710fb886662043a3165b30bb139da0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJZUCFRA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVTjvfM9PWJZMk14qWgmUWTGTxXtklgDGFtFBfZpkLBAiEAx4KJVah9VVdU%2FfNP4ttduQa954Mss15%2FMGGDGIa17Z4qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLeRiPdUHeT%2FQOUJgCrcAyjdp9bsO7AARwKA0gLiNoCM3rUYoZTsJm2fkOmN8n7iCAb9MNGQZV6GSc5WiaOxOsX9r%2FAcmDzYxBjuLrXUCxECEQ6FA59fQT1Pd0u06UIc7213nQJ5ss5FFIsZ3Xxtm8754tsbLhEd1E30hry9%2FwArnJR1IHH1LanQR2cqqoVYGTCLw0fr2gVmPhYTtC0z2XH70nHU0cD1QBKZcUksubxmSL%2FMK5Shb7IB1QeMAcglaqJl3pD1RReZi7APrLbh1DXdsErkaoVUWFqdRwrAjfRSz3wb3UYvdViMw2afr7804VqUkb%2FZkk684q49BmRi2Oa6gT2tg8c13%2Bd8%2BnViWzavGp%2FkH7C0MFrwIsAzf3xiBPoTsuGdvWTm06JFD0LIEdjYBk2Dt%2Fj9mC0i39xq%2F%2BV%2FMJUAs5iQa5mW3632w7qSLgDbIIMTlW%2FF1L9WdxxpFjvUlyyJkXQVaSK%2BrlO7VMKIBL%2BKvH%2FRhjRlo7MDkiENVUvZ7KqURjeLCiP2kEPLEkBqbGT1ma%2FUBR%2BxeGdTMkzEYD08EM23NTe3%2FWQnOQKTH4LKdI6CnamboubAS1cpua%2FHn2bR5cHJjqIe9wlDki2peVa4k96E3AQbmoY9tMp%2FOArnLgsJY89iRag5MKmf%2B7wGOqUBfE0rSKMuXbdu4Fiqy3RhIJYvA%2BG4X3JkKNnXBbHqGYWWGyl%2BUUP24zBqK5jQj0wwdiv4rlfGzQvJaHb%2B2Oo6m5o1aSf%2FCiMHyjXYCjPUGXDapeSr6LiZx0n94FyoC5i74%2FkffpkMC8CEhj1tzSp45cvVXx5kkmuFBvHXMXQZ2SvThlNMBlfAElw0z67zC3cBuRUESLgLv%2BiVzsNwQWjuSBlMApFb&X-Amz-Signature=107dd305dc3f74b533f68b62a6d6c1d75c4be4f93a2fdfd956230f5916bc2cf9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHOX2MED%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICP%2FItOEUo%2Buxc1KaUnLKqTnDHa2xu%2FvcftHymFT1lJFAiB9bGibsZSK9HyLkJA008%2FBRmqxQmIramud9gmyF16vsiqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2BQo5cYW0Vv8nlT2KtwDQjdwXw%2Fy0tNdDzbmbB9GLAG6ke4%2FcPvKvDhqUhtmNdoOMBvur8Jzg%2Bq3c7IQkiZU5wFJzGqliGgq6J5uTd6q58fW3RZmgOopWW19SxZTiBY%2FxzNsTcRK8Rx%2Bf9XzIFJL%2FD0dVWCARrpTnDa3Orl9uTkTG7EpDnyz8M7jNF7x6m07afElURliRR6b%2B47IXtF78ndh3Rl7Mti%2BBg%2F7GFdKJsubf%2F%2Bechir%2FR%2FVZcWeE8tfyKf7ppYGvqT%2Fl2qxLRgyL%2BMRWVNoY%2FEZ4nHXjkD0A1t51yzeRkBd9HvEj2RBkjr51eV4JfZH7kkhxKYhb4xm2TivB7EuvJ%2FH5PeitTvXeoy%2BAw%2FbBe%2FsOV%2FmIXrBYYEfsOs4I%2BHxU7IhuALjqTwo4addVykJQWTByzwTSBF3aTV8jRj2Kt8KlT1j%2FiNjLAup8f9EI2MgE0O07PiUvnMiOBDx9uWyfYt3%2Fnv2nfYlGgJOIjyjInxoH5X%2BxRVGvkZmJKWBOboPk1LC0ZllqBcMOXVsBhZgI4vpDs2xpQu1Gy3DwHWkjzAUBVeaLIDsLRz5GDCT%2FuxHP85mr%2F2fd4BY%2FQkOGuwMhyN1Cfrrn6a9zRF%2FX7VmDyGcjQwoDH14tU0ELTa0kALmMCU4fWUwyp%2F7vAY6pgHJ%2FBGb%2FEJsptHBA8sNcHNV54fQ4rLQa24tteswlZfZjwZMd9q2ItKDNMAUYcPjiD0aDl06DfDiZkx%2FYdCxs8IZTbSbk8tlk0hJCXAnyzwZAMS2DIVnz0tn4dkKKPd2ErXzJVZjhsa5enRLagFd%2BebAqoIW66BzbbC5Il8m0DCH64WS2cc7Hf3y9QYXDCi7nIjhIHAbx65vwRXYJw9HWPMzwmJu9iCW&X-Amz-Signature=f47a95adb7d1ffefb86d96ae370d11cecb318689947337bf7eb97a6bf277b312&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYOVPWRL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHt%2FyNPKMBp278Q0SDdJqokP3WDj4Bvo20gSJajZLxTAiAdYCWviRnfWSjhU7eys1UXbht%2BRZ8yE32Va2fIlgSY6yqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgfzsE40Od7tv4n%2F7KtwD%2FTT67qSVYyc94Sv4ljuQXvc%2FC4beIa2QAm4UBlFafqh6u7h1dmaIQQ5PiIU9Jn2mGAlJXK8PlOZIrBaBhyYpmMyJsnXsLERBwmdBFlgPb9%2FzwytAljgBHYFKJfQZSv%2FOfWPQEkuFdt1lmLpv6YOuNky9vJ1NbwRhSzJDIA%2FLhlrXJyZYNIKr4Sp5LfbJlYZ1y9JvcKeZ8smQghZRMdQ4jK4E2OqX4jsQvOpl1ioncNfif1HGwNxKgokqtBSDukbH7p7quIEgRol0UpqkUnSkGtGUCDtlgtaJ8gY6tr6XKv0U46pFuYB3%2BsTXhHWVHN5EVbSesMJ%2BUBRq8%2Fa4xAPctydzBlFk6zYZHAC2w66OEId0x4riPf6i5sBPoc8Qms%2F6CEGP%2FD2uuiGBcm3W3HEtcunjqzht7VqmGiV1gk5QXhXTB%2FxBp2AGF9JpO277cVy2I7k%2FY4t6QDdnQit%2F4ZhytKINJEC3VaOu36MiLN7NlhrdkTCzgVnThRSCzuNV9XSknRqaVjwLglnTkN0UisKWLJW%2B5Pl6pnnLpZcn%2BeXSLJMI2pD49jE9QbYlMvu92LCUVrySWKfCsqb%2FELD8ROI835lkUejAq71aI6hwFk7Oxmg8Slk7QnnntYcOuFMw0577vAY6pgG2Dxcb%2FwGfMQTMCEmDhYKWxB5oinu3lXFNH3mu4eeyerUvc7xK2WPmQK6OpEG4PlBfEwzIwsbzW1kDuMiRDYij0I%2BHhYAHUlYbob4X4L5D05JoSWhm46Db2Goybcxxo642WxyzCUd1BVd%2BY17n6uFlLgzijx18K5oyX5xz5cPBqYyE3jnNbG8OonNJsT%2FzOkoutLyWm25VObCfLYFn88fEN1iQPGpo&X-Amz-Signature=0b846a820cd92df3ff924e480eefd98ba8bd1d39d74fa6087e2e18708b2ffb40&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VPNIRIS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDf5MT0iRBM%2BSbUbwaBwmiK9EB5zgbd%2FnQyn7m8XeEPqQIgOJtf6LRJw6oQm9KMlBOLzyn%2Buo%2FCUXGWlqSIVcNA8AQqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3z%2FlpoptEuXVNNMSrcA7xS5G0I8qQzuscsVdx93QbK6%2BOMfbJMwUguljOQarhl2%2BuASq%2F9Md%2FAHp8q3xRp3RtMI1F%2BAXlU8QQSQ%2B5g5XMeeTnKzBdJz%2FEd7zLQTQ4VLdxaNvo2I5b%2FRQlCsxu%2FAXswacejo93I31WqOykqAgdKON%2FJK4UqIndBFv4JCZo6YwR4JMuOH9XQ%2BicjHJR%2BsNuOQ5GTAJSa%2Fa3W78NE6sEuq7PCjlvPhikiVDZBTrWAqA2BlIB5Z7BmkvZg25YPk%2BPun0DOZS6XRHIMVIHkpy04%2F4S4%2FGTz5F%2FyrpzIwMuFtHeuChX1yEAeOxvGvfKmhxAfptLJijSDz5WX3PsDiAwAxs3QdEsXQVlje%2BTqEjjAv6v3XT8jSvTahABd4YuAPhCS8YkoWUmKH8vcbF94Vf6MCWo1as9lhYC17%2F05twky%2BaOZn%2B9ZUb41co%2FdPBU0DV904xfDFtuJxMXyJFapWMoB3OLpmT74Pj%2B68eBG85m9DmVNOlXWCoLaDXGMbYEqOkPxDTdXDa8jbfxqlccfAO8WPkLyuAENWIFSDDtK33MZ6son8ZCgu%2BU6QWeo8ECIlEB%2BJJyQLRzAmqUcPhpP%2FiZOQaov7f6C6SQZvHAbGTnPwQTAnnmc2OmaHQ4qMP2e%2B7wGOqUBXLi8t3oBnpNXP0nLWzNvh3agKVrmXKplKKxxJ%2F8BsDJOfJpwt9g9H6%2F9RI3Ud092hAnelMFdZQGUkNY1162%2FwBMuN%2FN7GgV5mW%2FRqkSzL%2BjbNb86tKNzu1WcRRxBUxWiSk%2BRG97ZmLRlBma%2BCBqDgSfJczR3z00GYw4tU5ATazjCvwQqR%2BxksYjLi2NCK1UdivcYFiY%2FddEUYjDoij1KcXJGGE66&X-Amz-Signature=98d1f2bd5f2140be9cfe09472cce7948b56f4905121710971a72d7edff3961ba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NBH2UPM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzaBbA3xklKxuGi74YAVOrJdub53%2B6p1mCRpFhWcELOQIhAO5bBCax9v9GbTx%2B0NbqPV9rZoVvdMJl9xCXS2fPzKOhKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxrCrTYmkdGb8mWtEcq3ANepRqMx%2BftPFY%2BiFzRzMHw8katLWr09C79ckAiMc2DeasCwvP4MBJu6pr7WUj08BM3JYKsvLrKmxa6x4KJCQWytigcxbvwD9f4oTSEHKQK4NcClAdJ7DKyJJFGJvTA6CUM0FO5kCgdP7I1Uc%2BuHZA%2F7slxVsVz9wQnHzpR9v%2FhSY0ToQy79kNYjDimQOQFUKOpXDbwOyn60v1i5oeNSeUzxk%2B%2BQZ64L8kjXMzxlMGdPOfSdDzrcOvFMLwfQdCdUth8P%2FrcFX3kOAkIWSDTo5iPJ45Q9rPwPsd7Eibpee5%2FBF0qOhZ6nXdDmR1e3S7saLUCSTK2tmldc%2FsFfE30hk2nwITjPXKnUYhhymqIkLsCz40%2F9l2FJd3rC5OF7te9%2F90qJTFJrLgeqi47F%2FXb7c77hgWKJ3pz%2FUJFHNP1cSRnRhg16NJcHsfZ76pyzShFOGueojq86Ki3kriAT3NKWpDoajYUoSqnjcT1%2BBT9uQse5dbY%2FqkFXj0Wc4PBy1wq%2FgYZpCE7xQk5vHDBt7Dn9zHY0lNISks2ZPnIVBq04oHNl6Q1Ym7%2BVM66MQFc6WKS%2B1q612rsyGqowZpg3QhL8QsvZh0O4xnvrvVWeGHm7xVEWt7V3lOcP06tked%2BSTDdnvu8BjqkAftfWL4hU2TR%2FhOWoMnVcN7qr%2BLpGIt70NhgpSwpzTOAuyFybrlHshkHGkkyTFsofAgp7Zjuu2fKhj7m6Zx%2FrrOBURBVPDe5MxJROpvLnrpSyFLA6hIBVMFAYsLFvIbHDXD37e0lSG%2BUc1q5L9dR5vWEY%2F317Ed4TMVoqcbGfpqxIkX30bb8Y4YOyu0q%2Fa9Tlckgcu0RLbEbkTD5DHuZQFpbrOwQ&X-Amz-Signature=e41806c7e5f0162b8ad68e43b5930204404193adb99f9e200a8c54db99b14e08&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VL52PJYW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPOPeLbb%2FkivlyBsNtcLgaTsGTYDHGunsKwt0g374hqAIhAKbtud2rrkkEPH%2BkDTpRk%2FfVS13M2rJ7jf34aLO15zfPKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxy85gOATA2WhVFrQ8q3ANEFmfu7DI6s67qMBR%2BngfSekmujZn9yoUT0YW%2FVBFaYu5tm%2F%2B3d%2F0Kck7Sge3KTHdnJNWEXx9UuJ3p7WASQM6kp8aGpBXZyZeaTX1eqaN2HI8Jx95HBTYqnN%2Fp1bgsCJhI024Xuotd9v2KFY9WSD%2Fqt4MQwDF%2BQMnf08XuOJ9NMaV1ibK7cJV%2B64X%2BaWv9ZIfJtDWNV2jJPyapREDduKXD6%2Bk5S4ozUGQbNcPofhlLElf0vvDqxRIjDNSJQyiO%2BxEwRtvaTVcuwFM2tiBeIZzH%2BBTQQQE278frWIWNXJnIz4esUQ84sfugvJEiBkD4X%2FsO9ENKDmharho4klfdjw73jlq9FuLn2IIXhauEmp83tuCuBuPfQJqvrAMeAtBunpeoK3nbOkfzMxeMZbJU8tBIXWCi5Vex%2Bxt8EIs9itCVt8H0wnxzgNgWCQgDSHpzha83ZlYIHBo7fEnffR%2BbStdWG5N9oyckxkcTlloM7jXr7BOUsLIVrbLg9gwWlapSLuG0c6f6ZeuG1aDiXPaMFK4MNNNgzCousdm%2BeyxLfuSIP5Rzm4wVZ%2FlvZHcbxMw68ySuiCmsqTjsp%2BjwEL8CZi5okSGZhJXnMm9OJosHM68gZyLVy%2BvnhcXXumqgUTDznvu8BjqkATwY9jO1LYORxmkaox6eyL9kfrkqSN7%2FoNEHMf1VNxJNgQOD%2B95xDIEGVvtY5eX0DQA9B3713wZ%2FMavdXDG9WrSF%2F5HypdmJJHuWlCAr424nZa5tg5vTUQ5edTv29LD%2FHfTvxrMeosDZMRSe9O%2F5sOBOAVxGANV5xG0hiIl9mREx%2F1UKbupdkgfdNKlu4wcSXNg%2BKKPbJGAABQ%2FtYK2CltFVArcm&X-Amz-Signature=18f3b6adee414c9f894f62f6c8fcecda03e57571a2abaaf3deaf4f4c89e79095&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDFRUVWE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUPuFlkWpcS%2FMo%2BnUtzh6gCgoP1aSGMSMlsH1hCDthowIgFAKY3DLf%2FGYrAQNDyAlkYchrUwmOFqi6yD2VtrA6%2B%2FkqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHfCeJdJBlKtKDhEZCrcA%2FljXbdDc3sF3BlvXGGErf6mqkMUxEC%2BlLrOvrjUeeW9dzPqBuNw%2Bi9UQErne9P1GblXWf4%2FChHqlbAzrfr3IPYczmDmRYPTSfYwWw8hY3ToyHx%2Bb%2FNjtrImBDJ%2FHlf92n9eFatjkR7hLePRb%2Bwef5k1IytHpRFr9kT4DiUB4eenZwtD3DLl4rcKMw9X5lUjoAnx1riFN1FoWDWnuFDzutuWhyMhqnR7pe%2FIMdQts60Po6xdEUy8w%2FL6eZEaljL6RQnPO4ExQ9AQH1ZIvoNsMiyEGfcFVfc6d93lQVROOQrKN2SJ69j8H61uRqUAyZb%2Fn3Wq0sD%2Fg4XcJ7SAWRZBd7kYIDpIealbKdzQzYphKM5ReBiD3ZNdp5BS%2Bf%2FKQVIcF3wSIJFnOxuJXf6iz9vi9Iv1qAM7VdZF0xQrETcBDKSJwWKaEnbnaoq%2F8Hvt6ye7hvOPT98s%2FIBZgU5KNtMP8QlrfG56OfQj%2FrgjEjRF8wuRagNonHyiaPban9IpFiIbpnxKDH5LOaOLJCDXjcFlD4bhyCfl4QPPX1ho4R3pQv3WYtCjeabCtrgnOL875U3TrBJsyZzA8DbX%2FgC1ZKO1eyTOVO8ZF%2BJANjSCIuR5nYDzBZ4R6pmsbR2YvSLFMNae%2B7wGOqUBVrOopIilnTWb5cETNuG9R6BUqN6Zllujsb41SFjWHa5anrPADWlFDZgFkqESVzCCubC74eBp5783E4wDV5Rb2UpRSiBZA%2BB4dPFUX%2FDHKiLSoOYHqNuEWR0hHTpB3iZ9fpC6hmXo6X3d%2FNF%2B8CmqCRVsMYxdsj6XAQH7vukt%2BV%2BgSHxzXanSpGc%2BrWNM7x8etu5blx84QgptYUY8nLt%2BgqM65NfW&X-Amz-Signature=09ee082a67c9d6b8fda70de4cc197fa590fe0e99a626ac3df06472475adf0137&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VPNIRIS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDf5MT0iRBM%2BSbUbwaBwmiK9EB5zgbd%2FnQyn7m8XeEPqQIgOJtf6LRJw6oQm9KMlBOLzyn%2Buo%2FCUXGWlqSIVcNA8AQqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3z%2FlpoptEuXVNNMSrcA7xS5G0I8qQzuscsVdx93QbK6%2BOMfbJMwUguljOQarhl2%2BuASq%2F9Md%2FAHp8q3xRp3RtMI1F%2BAXlU8QQSQ%2B5g5XMeeTnKzBdJz%2FEd7zLQTQ4VLdxaNvo2I5b%2FRQlCsxu%2FAXswacejo93I31WqOykqAgdKON%2FJK4UqIndBFv4JCZo6YwR4JMuOH9XQ%2BicjHJR%2BsNuOQ5GTAJSa%2Fa3W78NE6sEuq7PCjlvPhikiVDZBTrWAqA2BlIB5Z7BmkvZg25YPk%2BPun0DOZS6XRHIMVIHkpy04%2F4S4%2FGTz5F%2FyrpzIwMuFtHeuChX1yEAeOxvGvfKmhxAfptLJijSDz5WX3PsDiAwAxs3QdEsXQVlje%2BTqEjjAv6v3XT8jSvTahABd4YuAPhCS8YkoWUmKH8vcbF94Vf6MCWo1as9lhYC17%2F05twky%2BaOZn%2B9ZUb41co%2FdPBU0DV904xfDFtuJxMXyJFapWMoB3OLpmT74Pj%2B68eBG85m9DmVNOlXWCoLaDXGMbYEqOkPxDTdXDa8jbfxqlccfAO8WPkLyuAENWIFSDDtK33MZ6son8ZCgu%2BU6QWeo8ECIlEB%2BJJyQLRzAmqUcPhpP%2FiZOQaov7f6C6SQZvHAbGTnPwQTAnnmc2OmaHQ4qMP2e%2B7wGOqUBXLi8t3oBnpNXP0nLWzNvh3agKVrmXKplKKxxJ%2F8BsDJOfJpwt9g9H6%2F9RI3Ud092hAnelMFdZQGUkNY1162%2FwBMuN%2FN7GgV5mW%2FRqkSzL%2BjbNb86tKNzu1WcRRxBUxWiSk%2BRG97ZmLRlBma%2BCBqDgSfJczR3z00GYw4tU5ATazjCvwQqR%2BxksYjLi2NCK1UdivcYFiY%2FddEUYjDoij1KcXJGGE66&X-Amz-Signature=8178b88ed872350175c62968b9154486900bf89b2ac23dce32c7aa01781827e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMOS5CEO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFijzW4Rzk2GEUqZ%2Fn6yeZ7FS5C%2Bc%2BLtY%2FpNfYasDPj%2FAiEAn2mzHidinmwpeFDHZ8AUbynwfgslaxA%2BltTUdI45TREqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBzQOh4V6sBAcoDu5CrcAwDoKC0qJBUSR6Re%2BJWeoPsxbA2SxuQ6pt3GYpZNJeJZaJhpq7Nl16deln92rO%2BcpYTbn52irGwvizBSd2Bf%2FkFsfJ06vdiDbGSXm5CKh3sMo85Ab%2BB8PuQ2ZXlYARzRhQAqAJSBnYIHYsa%2F137a8RN9tQD5SW5hhU4WyE2aHmF9CqybSITZuETJ3ZohGU6nyOAn3a5LS4AaUSZCYRkx0Cje7zKcYwtZO97YKFKePVSMX4hdtekIpUzxqtq3%2Fqa538%2BKzuATQMIYUxN9AyhqiQK%2BnXpd8wApaqKpqyOBzgAK5ttXEJu9emfoVISVz%2BWM1%2B%2BVC3C7vIFaN%2B1sC4PFcXl1OGQwRWaRdzFG4LZbuhGPkdc8JEIJmMoyAGgp0CorqaG4EKbjzZwGQhqzOXjYoe4uJFG0Fg%2FDBlsesGDS5oMFfAsveqCrojgD09xRHOBosRKGFCSaBI%2Ftm%2BeLcas%2Fje4pJGcYfH6VXspgfSw0lQ2i7oq2d1%2F2N%2BYe8QbOf2z2MJz95cV9Ya0zMf5giOdYddLqhH1PyQboL0UO54s4mfM%2FDyRRsY4MpKSKZNRBlBqbXc0jImtW2DEjreo87UMlZSNpAeb61RLy9QfOLB3roW4z9kT5KM5Vb9FLhz8CMIef%2B7wGOqUBY3aHt9rGQayeYg0n9q1Qt%2FbeX1BT2yhuITW%2Ba32bCF3PYnFUXwiGvntglIuV9YUlcJ%2BuntcmQm76LHnscV4e8%2BcwRHurcztFoPNwETLJM7Y%2BIpE8d1MpijNXgqnX3%2B9p33F7FmieEWqsr8wh1Cid%2FZCJIKDaZjwAIruFue2AUET2kIFcQZo9T0ahBdiIEMN2Y4mOFWGpzCs2dd%2Fq%2FCFW9mQRX%2BNY&X-Amz-Signature=6979183ab444b63cfed611c46fa354cdde567c76063e1a25abffcbd8995959b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMOS5CEO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFijzW4Rzk2GEUqZ%2Fn6yeZ7FS5C%2Bc%2BLtY%2FpNfYasDPj%2FAiEAn2mzHidinmwpeFDHZ8AUbynwfgslaxA%2BltTUdI45TREqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBzQOh4V6sBAcoDu5CrcAwDoKC0qJBUSR6Re%2BJWeoPsxbA2SxuQ6pt3GYpZNJeJZaJhpq7Nl16deln92rO%2BcpYTbn52irGwvizBSd2Bf%2FkFsfJ06vdiDbGSXm5CKh3sMo85Ab%2BB8PuQ2ZXlYARzRhQAqAJSBnYIHYsa%2F137a8RN9tQD5SW5hhU4WyE2aHmF9CqybSITZuETJ3ZohGU6nyOAn3a5LS4AaUSZCYRkx0Cje7zKcYwtZO97YKFKePVSMX4hdtekIpUzxqtq3%2Fqa538%2BKzuATQMIYUxN9AyhqiQK%2BnXpd8wApaqKpqyOBzgAK5ttXEJu9emfoVISVz%2BWM1%2B%2BVC3C7vIFaN%2B1sC4PFcXl1OGQwRWaRdzFG4LZbuhGPkdc8JEIJmMoyAGgp0CorqaG4EKbjzZwGQhqzOXjYoe4uJFG0Fg%2FDBlsesGDS5oMFfAsveqCrojgD09xRHOBosRKGFCSaBI%2Ftm%2BeLcas%2Fje4pJGcYfH6VXspgfSw0lQ2i7oq2d1%2F2N%2BYe8QbOf2z2MJz95cV9Ya0zMf5giOdYddLqhH1PyQboL0UO54s4mfM%2FDyRRsY4MpKSKZNRBlBqbXc0jImtW2DEjreo87UMlZSNpAeb61RLy9QfOLB3roW4z9kT5KM5Vb9FLhz8CMIef%2B7wGOqUBY3aHt9rGQayeYg0n9q1Qt%2FbeX1BT2yhuITW%2Ba32bCF3PYnFUXwiGvntglIuV9YUlcJ%2BuntcmQm76LHnscV4e8%2BcwRHurcztFoPNwETLJM7Y%2BIpE8d1MpijNXgqnX3%2B9p33F7FmieEWqsr8wh1Cid%2FZCJIKDaZjwAIruFue2AUET2kIFcQZo9T0ahBdiIEMN2Y4mOFWGpzCs2dd%2Fq%2FCFW9mQRX%2BNY&X-Amz-Signature=afc496a484092ccbdd03b401ae957680230cef2aac4e5d8201d2712ff6f7558a&X-Amz-SignedHeaders=host&x-id=GetObject)
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