

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIO54Z6L%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCID3rRrG%2F%2BbFR2sdG%2BR11C4%2Fsji%2BUdd9HNd8LJzmntLptAiB4Pc01a3mIhU5FeeD5X769XKYHymXNXKKSYiW7jVuPJir%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIM6CTm9xPqMtpGqWvFKtwDLAy9Zxs3ElTzBkq47tMRjTuVh82AbgHUkpWuW7ubex2KswrV21nLmp%2BOxgPQqLDr3vTVxcyr0yevnJQJWhBGxMCWWQeSvLJAy1Igj1sglKm7TFX124J2SDTdFfulA3gGA9HJIupoZ37iPLZ97Ezsoq7OL16f3gevh%2BPQ4EIsShhRls2ySLZGFsxGJ%2Bwsr6F71qaqd%2Fto8VtrowZ%2Bn7PHtDbTV0n53lHtknZFr8JeVrH0DtddNearo1eN5b%2BC0%2FLT%2BclCEXxaDs2tYnYGfdfbJ5n4bPQPwwDLmv2zkv%2FsgCBjzq450713qaF4si0t88OmdDTMRtClqCKL%2FugdVQvEnu8kW7SG%2FMV3CTty3PZhXPPRNZNW%2BmkHpo%2FFv3yeZGnc721FLdxcuN717ZMd0U4H1PjcRWY2hm02v8n1vIiKjNIzb1LutvvI43C%2Fz2b8Jix7%2FelqZTaxManNZbJtyzKim2CnhPBYDmOEz%2BJlEaF12JruqZo2%2BdCgIGK75Tw0HXBOCAmld0nOUQGmZIWeDzN%2FwoxLtlH1y3G3hGtMSc5Ol8oVPQpdFMxDT2omgql3X7aao4ZkRj75mMe6DXRJWAImu9v7w6FHFeVAZKwJ2b8W7Rrn%2BdzA6ZHKXvlInO0wsamzvgY6pgGKCwPHradijnVvvgsqKfDwLoy6WPRhfSoioVGaF1WFj0Ljc%2FgyuPbp1WdwyjY4EfhEXg5EkNNKmdhjIJxyr76NT1kcdevfC34fQfGhCJPBmz%2FRkkdDwHhi75gqvcau%2F4EpWMXwgRZpXex6%2B3h08fFxr1pO75e5HwO5AI13SAz6Fwv%2BogcSEjm0y4foP6VAmRCCGn16vskE7ehUcaIDy38LNZLmTJwf&X-Amz-Signature=ca0a170ffe60500980c268609ddb29d3a7c2e3eba489771df395aba0737c4e9d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZY64F33%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIHHXMNzHX84oZCZsvT0XLNiJdEn09FTrBqNhcCnsQsANAiEAmrFG7kDk7ahJ8eF9uMHnywHd7B9AvCSukAFGan63jUUq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDCQQDmG63zfK3gMc1yrcA9FvYwMTDSILaTQpc3fOzT0hAigyVfx63bS6LZbxJmVGQw3H2hYhJvszSyCTyjClGoJ%2FLgXeIq8DDjmO0Tab7D4O%2Bfx7lYSO1hjwHLrGjHxwIAJmYyJZ1AHfNbYPY%2FTGaoRq6FHMop7TOEMWAS1up9XI3s%2BB03gptau386i4HtjozYiXwKNjUFkmHYMHojZAlylwTBfOsApk3JdoVh9bLZcHustGL%2FU0Jq4KwiSHz0jp2SLGvNZwaGCM4BSYuwRcpAb5i%2Fp%2B0d%2Fxerm5fstRS6rxrl1mwqo5k8i7FDc9MUoUOlnyy%2BF1ZS5a1ghylIn5Y9194%2F5HE%2BxTRnzulI7ajM8zxgz8NwL23D13R6r%2BzlReE%2FqyRYy0Fy2MCIyGeBa%2FEj1QtQyaduNTuuIjEt8XQVmpXI14SV7Uvs0I7xJoZaVduthOatQpo5ednyIXD8AFt842UbLXzmWhwsY%2BHdQRD5a6Sc9MuAyzZRIcMfH1NEmjwczWVEsrGNHYyPrTS4e9k56yltaN86kxRmr2Fwh0eZz5ExZpKeOGNu6i9nxudAuqXxqgV3P8F%2FxijtnC%2FtgXPv%2FceTK5g%2F5Ic93d%2B8hL446SsiS7MusZgh8io56KscWILmbhsblI7uWMtSVsMM2ps74GOqUBfIzt5w%2FKO8AhNFKZDGcQACoOJ3RUpc7XyuISM88faPYEXLzA10uEKS5qDStn%2BZC%2FSH1GHUCaYLzrE7pBXl8Yr%2FnlULmvFF7MfldZtWsNtzYAQbQEBpe%2FWVEGVLjESagVmT%2BvA2RNNY6cmW1%2FcwcA8lhPPa5jUwHxMF33Y3YL%2FvYGiN514Q3Vu4907Js1ffNBoyNsElzd7Y6inQlVBnydFVT%2BsvYF&X-Amz-Signature=14233e26fc7cc9c03bba5044955db6523aca4390d16aa64522d77be4601f77a4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWVVY5ZZ%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCb5iS0HXebEAQGtG0%2BNuR3X3gGavXQ9mhuAOBrQvytcgIgUt0Fm1opfZTxcYCsECxc7uoFTMeeOgFV06756jEz8rYq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDUaUcZ1QyL4ECmJQircA9djTpUpYhziHE%2Bc7WnTtQi1RpyspYmCWVL%2BXRm7VjXT6dDrb3nxirhSOUYhT6Ef3kvuE0QCvSYJwyDXEHpsjvtDn6SfhHi3kS%2BZWUZ41pfW0EPtiyJDZS7dUa0DJw%2FDtiT3cwjr2GQhTtLWBVZ8cFc1NLzzGtZ4hG8CG8Cp5J8plZcugkgDWWngPbinxJkgaF2uZGp1cwMWeX5JXP7G3SkMRR72oyC4l5cuEJienob066iZ9OApUIY5wnsYO7UE103Ep%2Fl91Axi26yk6QR%2F2qoH%2BGeWaHpNa4ek2QPJcZc%2F0FVFsaAivfMyxH4ZSMc9G7FoApPZdCnep2569WjkjwPGwQDu7p1vexgE52yoBbwJ35nQBiLz9r4toBTqH83xH0U7Hwtv9DxFy0SuD5k8iyAY7312hC13GZWhAOJQsZS0rr28mlun1Rs2VupP0JGHfprfY8F79Bgcn%2FYeR%2BQalHRjV7n0pvzN4Adw1o5spWMARPt0qIS%2F%2FMuvljv%2BFzoNxDOqWON1RMZTlUJaT42Pq40wP1GAWGbarFEVEu0pST%2B1B1kpwXSCXERzdCa2T3R5DByAw4%2FVsmDby3%2B8dmEk7HaaKI9fZScEUarMtViZ%2B0c9H9%2FwtgQvQ7u%2FPaZHMLGps74GOqUB5S1Dt%2FvRSiLDK42I5dy6lElUilV0dGHGogwbaY8TsddXxDbb8%2FeDCOTwJ3CGjxFPc6x303k8balp3Rj3B%2Bs01NS59MiR2VyxfTOdnhuxcNwJGrpqNv1zE3AbbgfhQgQm4vWUp87b82ZTITc92%2FMt0KaMnv4FP1NOO3G4kyD%2FEiF54IzO4tYsg5lu2K2pCP%2BO0WYLcw6Zihy6Mb16Zpbq62hXYSjI&X-Amz-Signature=cb4578f00f7a78f2d5a1e6c95db3b5567c6f228de5aaf6c4d7348399c2329ddd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2IPGEQM%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIQCILwGFV5w87Ykll%2Bn8XCSY4xyyuHHUyri3vUVtoITEnwIfaS%2FLm3pogwvNWDwn7JuZTIrY%2Fxk4T386gfbgGnAFsCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMI%2FUe0xjiriBGIEF6KtwDObyzpD5kHb2oNeUv90Z2B8p6fHF7hUlqrYZf%2BIdmUdZjw6PQGlqJmwwF%2FKuXPq4B7bsT6ExqAkVgZ9kPgdtB6dC8b4%2FOzgiwG2zc1e33HbTzDG5vpaW79XG3rojElQo1Ywy8Itq9SwsT3Rd%2BRMCacLRJTa%2BJwrSCY3yrE0IHI1F3ZLquDzQ6A1waB%2BhgIns6DV77Pg7dY5MUyC84CoMLLTTphF0IRw8Nf9yWeYmadhpJ6iucaHWOo40AWKXZcZcP%2Ft6JgMq2d%2BUASH1mqlgLBDPgQxnVJJqvUsx5g%2FSd7dig9KUYw2P4lI9pF7TqwPvrrIKkMf8J1ssDR3hD7N76CkmvMLoiEdjyza2aHsNVwVr3YNwID5jCkB%2Bp%2Fk8vIq8YyyX3d60wL4cS%2FsOkPNzh%2FZTNc1Dq6F3%2FDyDfAIVyCeKbWmcnAKZ0R%2Bz%2BOMjngPOFFgAhkICC0qI8VKL2lvMHA%2BLquVJbjVHgq%2BXp1rRLWBYcyFj%2FklF6XBLH9TyfePNuGYmi1nq3vkgm3LN9keMLIQErJcsMcQ9KE4%2Fwu39eJCnc6EUlC7j6gMLxPOJ%2FpFt0IcafCwu7eMndN9C1MFmpYLX9Ft8LgA8UxAonBfWdqXgNE1c5knBVbcaHxR4w76mzvgY6pgHlEAYIbwF4RuUvwtTWhQgaUbzjjYHi3s1RM%2BFrf%2BTqT%2BVM%2BhCR%2BpqlQo0REEOB594fjJgGnzoqkykCD2frtb%2BqDZZm6evx8tPgtHW92g%2BQTMka9Wpj2gRELULCmASbn4At4pHT49%2BK9hevj6IruCfu4iWMfpJ%2F3Kwf8HjR26n5I7mcVr6Wv0y%2F%2BTVfzsDf9otusKG4BvgTw2df0KkYlypgMp5bqYFU&X-Amz-Signature=205b2751b356987e8d0f42d44a86386b72813c33efdb3cd2cb9e1e7e1dcb1a7c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REMKXHYP%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCxZVSXJyDoRvoia0t42IXNvf7xZiqEMBoIihFLj%2FcvNQIhAPZJn3Z0aG46g9IuR6tI0v9EkEr0C6LGoVXLp%2B4azdKPKv8DCGkQABoMNjM3NDIzMTgzODA1IgyxRhAFf63%2BWjS%2Bix8q3APeZxwnlUrsllYolw4N%2BO8R7oKxb1Fu%2B60aXaG2sKzVN5OAaGcHgYXKgS0v7TvjQbSjwGM6BUHdVq6t9Hxq2iBuF0PaVKGapBzU1L5HYXA3KMRvsPEM7M8dsGpmpG7lYhxrJl7Nn0hEx6xmxVaxvMwz33TBYdBtLsBGwyWnZ2cRI9KQRLIu28QOBpot3bj4pPofWz1RJ9%2B2LZt1DWFc0%2F26GnRo49g3LqpACN%2Fy%2BoIlw5A1ZncgqSjzvShmtTQWV5WC0K9MowgVfxofdkAancT9FRb6cmVuBBbqDS6nWh5b6vCk%2B8SSG48NqXPYXfc%2FCEXNdpW3m%2BNP%2Ba6ABaWs2tDXhXv9BnkF1I4Inv3agn7nKNBoTL2kUDzPkko3OJpx9xvTKRFFLnY%2FEDeHyOZ5y93E89GD2HzLtBIM81utl2kqlZhhLE7kKfjAI%2BkY9pZpwW9%2FfmCjoHuepthxWSuFA7cWWEAK4sSkGYAWZEiGm3BpSSoGIVasiBoBIuMSHym0bNpo1IKHVKhbTT8aNelv3X1oYE6R%2B3qsfC0NO7tehocyuUgTgoTGQPxVdSe42fICv6PiBj0LPtJqXH7L4Rt%2Flo%2BRDF4kH5p3Vj7RHXw3LcrU%2FtHcgYiFoKIHghv2wDDGqbO%2BBjqkAarZyZxNnLUSt3SgnJ%2BIZ6JUa4A9BMhJabpfcSNL%2F1aRe5hPd4lKKo6U%2FIhrsxoHu4QOKMxYFalGERI9oGLuTn8noRbvYWdsoG%2B5WL1E31LYr5JgKQNEfXvJkHwJTh1egFsOiOWOb7cZPi54cAOvcu9pkJBHwhtgVpKhmHvxEx6Tq28FKAvMaMLU6eZbK%2B0Whr%2F4Bs9iubsAj5mLzQa8Vg4QTI8D&X-Amz-Signature=3b57ff7855d2b2c9a612c29cd5a18165b4fc877a080fbbeda138f515f916084a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YG7LACAW%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQD9JgtWRKQy6jG%2FrTQoxZPKGUqaSVFVdlUVSwcLny5iJwIgT3p4P0nWYjJFF9gAUBSwNA0WqTyK%2BE699MgeshkR3zEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDP%2FDOuqj2TN5no4PmircA7jAG4VVVb%2BfspTXAikWofqvUfpVKFUUgI%2Fq4KX3d%2BKjMkUKRHOD0M8cy4RN4km4q4YGYbKhfl9i0AzQqKiE8oiI5clE59YUw7%2B0deq7UUiT15NVjtI628F0rhJAp%2FFNpUm7HblzujUhDbjVt74GXcNc3%2BnaFu2Uu%2FqWhI1tSrv7RMRegm1Q5QpQl3BvQdDC7SFGvPNzNHSatrEzaavPc1WDc1rp%2B95NmHLwe0Utu5uZTh3PHoS4Vmq%2BE2j0A2pl%2Bif9bLPUrC6e%2B5YisMvjBD7l4ymfZHheLcDoTbt8KA8o8G6GH2dYiTASRYkkneElM3KEj9FbTKTVTjNMp2kDOgeqwzdo9kwjlljwUFCU%2Fgv%2B9Vl%2FIfNpJ3ULItEiptqQAniWGLjEtk89khAWGfkKva%2Ff0nYwwK86ONR6hMFnvfaR7zo6e2FvN7KRD3TGsLMnM2KCBOjYOr0lxEK3SQxLwRJce503axtLV0Lgu8BEVn9lZDDLfnaRQCFpgw6amIy%2FZ8hB9WZn6F%2BhvSD%2Bd16pR%2Fc9hTUhx1GipDj0g88iRV6Fjusy87GxnQns%2BL3aR9EmWETxPo12HKMHcyvM9hQMBtMvWAliDrbSOW4QpsCxSe6lE7%2BFCLbaQGaaTeTlMNCps74GOqUBC9AkChhrzxnTKgwltO0wlnbeVq%2BNLgamKoLCXYFuT6Pg%2BT5x16pUhnWD5jeczup7fjrYkbphjEEmib0JR2v2JE%2F1PGd3WHnTp%2FXONVK%2B%2FrFSeBS8pXxgt7wg%2FO8KN6p%2BMHVwvNRTNEQ2aKSJ9qgvby7NQMGqCXvqZTYiXzY24BRQM%2B7kdQs%2BTSsfUu0mFUsXiRwPwBv5%2B34X9a99ZHmv5%2BrFfl8G&X-Amz-Signature=574d39a483118eb4dee049010e82837be604fe7b9f98cfdc14791df77e9edf1a&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FKXSVTS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFBc%2FS4xrly4%2FqR3LTJ8L9VlNQo0UOOsdlRnE40L6oGRAiBMsIh5p72jCMd%2BvFJtXHHo0iB3pC4nOejW4UC%2F6OpHLyr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMOOIhz6yjksD8ZcA1KtwDPV4Zm05QO8%2FuLSWt4YWJ8ZbxVBQ0CZZTr5WFEa5htUKiJniUmmEhlZ5UvX%2FoCG37ACgGJWMcJpxNEBIoKCJHNCw%2BiC3yB1n8rRDtUI6mQnaC99VNptOa08NZCZ%2F5vcDOLU7j3TZCdOx%2Bu0kLoG6bzat92GbdizFomtF5R7cgxgMGLyGpGYVRl03Y6lYH46dV%2BzkUIMsTCVc1x1wCYn0vc%2F6fifagSru8EM3NNyKHLKts1mVQvZDL5hPSr0RM%2FA3W59mazn3ZpsxH3jXXKL3wHKQVvxIJzTTCRQh3FvNf8fvBtU5NTbrV0IHrmJremweyCLBNUxt0mHT83pQ9ftiR0Kvr8QvXG9%2Fb8yIMCtWbV%2B3r7LQPKRwx%2FSdjcKU9yLqYS%2FcZxKngjv6cOfcmfBeemKLa32rdqk6NFkvYATDWVLr8EBM%2FF6pXFnyK3ZWZe%2FOMYBvW%2BHWxjBssiBOhs6PPQV3af7RSIIgfk6P%2B4bay4CGjgh14lZYWhxbC8E5JMF5843K%2B0qw1ouI7qWimGhsk20qishx21Ble5XGkCas2z3A3djNnjB0p0bbtBAoZo4ZR%2BIpauP6cZ9fj5q1Rf2hr3MO%2BbgoN49va1nNDANy%2BPyUQTDasAjtwnZNSHH8w4amzvgY6pgHrESUgdiy6ZvkIbNpglR%2FYLGypLDAqQj4pmXS553kGpvoWgmD3UvQrm1Yx8ZhPIwivKYCZBEs1ulwJd11c4EKToI%2BjUTxiDi2Jd0%2Bpan6qaPsHCdhkbWaCwLErFiNw6XV6Pf0VGUjqPe6u8hR2UeejtzDtiHU%2FKOBjds6cM6TpWcV8TvJEa01f%2FTe9264IlF%2BYEbHmdvneygxdTuI1O2G%2Fn1cBl6aV&X-Amz-Signature=72b7e0f6f781803f8e30d7910c97fb27adfe3d9fb21fdb2ab44f5a244bc62582&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ3TC4MG%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCKsMlcSeR7S3KQ7RkYIWYv1lZa2BvLuSHkJh%2FCnnQEAwIhAMk45loeFCS7B3%2Fv8cH9A5TC4WZaVx6Co%2Fy9j8InGsJfKv8DCGkQABoMNjM3NDIzMTgzODA1IgwQIJfNzm8aNvdaQIQq3APtg6oNxxnX1Cpus4OZqEQ1t00OHvJRo91JP5Jt%2FaAoDP743FdROMngT%2Fu06u015I2yiMKlFIylD7hreNY4bPH%2BGWotYtQXUJS1cF%2B852mMaL60dSrT%2FeUKW17%2FRjlx4WOVoigH4Q%2Fod05mDijxDDizPy6tJ7qAAXudkefVwdk1mwVaAfL%2Bfr3PiogVkFfAxWGypq%2BOvhKBXOusfjh0ANXCMRpxE0qNm5zbx1f7m6mzyJzdRoZ8rYAO7GCXHWrhzPIatVtdqGpwRL9wXelcyHpHFGAuaUXaW0Ye6V8UN9%2BG%2BIM8cbPED58ZdVQyQHVrT0NOinAjr0z%2FNyw18KvO40ajIOkAJ0a7s8j7%2BvHDKkw0qrzOPd4bkn%2F9cLkJ8EWNmVtrDPe2EAOvY4PJWh0rUIP3VYUtjdOEazmyi2J9aM%2Btj9dscmh%2F%2Bgj9SKGB0YulcoUqUcB7CdpgjQu2vDCHIgFN%2FkZowZ6KrF278nwt83rCgS4spcWt%2Bz5Uu6R5S%2BGReExFOKNuXPat%2F2rBGdPqojoSaI%2FSukLZ2LgrgQFIC2A56d2SVNlNNm1umKtxNXVIMWCJ6J7pManCkrdA5Q%2BgypEeFDRl%2FQsYTnDlTeQ1T4Ijds3fMd8BouC%2FAH887DDrqbO%2BBjqkAcNt8mQmxgIsFSVNOZAAsZ%2BAScTM0sLYV4PrQAY023hvFPrni9yEIKZCaBnE4wn8zoqqjnPz0ewVtpbKaL5mfpheuxBm0Fe8dQ%2BzIJHc60O5lQAN%2Fssv2zKFdvgP1qqMJippX%2BFvq%2BBaiNQIcO7XKQ5UA8WVgtPnaE%2FISCAOPcPulOC47nHg1lQRwAMS3h97r8YMk4jpNvjfdkDAfivZ%2FUpVEk4k&X-Amz-Signature=ab05d018f50041aa3c0eeb07f24c80d605b6aaa10b81742d476f302b9b057aae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REMKXHYP%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCxZVSXJyDoRvoia0t42IXNvf7xZiqEMBoIihFLj%2FcvNQIhAPZJn3Z0aG46g9IuR6tI0v9EkEr0C6LGoVXLp%2B4azdKPKv8DCGkQABoMNjM3NDIzMTgzODA1IgyxRhAFf63%2BWjS%2Bix8q3APeZxwnlUrsllYolw4N%2BO8R7oKxb1Fu%2B60aXaG2sKzVN5OAaGcHgYXKgS0v7TvjQbSjwGM6BUHdVq6t9Hxq2iBuF0PaVKGapBzU1L5HYXA3KMRvsPEM7M8dsGpmpG7lYhxrJl7Nn0hEx6xmxVaxvMwz33TBYdBtLsBGwyWnZ2cRI9KQRLIu28QOBpot3bj4pPofWz1RJ9%2B2LZt1DWFc0%2F26GnRo49g3LqpACN%2Fy%2BoIlw5A1ZncgqSjzvShmtTQWV5WC0K9MowgVfxofdkAancT9FRb6cmVuBBbqDS6nWh5b6vCk%2B8SSG48NqXPYXfc%2FCEXNdpW3m%2BNP%2Ba6ABaWs2tDXhXv9BnkF1I4Inv3agn7nKNBoTL2kUDzPkko3OJpx9xvTKRFFLnY%2FEDeHyOZ5y93E89GD2HzLtBIM81utl2kqlZhhLE7kKfjAI%2BkY9pZpwW9%2FfmCjoHuepthxWSuFA7cWWEAK4sSkGYAWZEiGm3BpSSoGIVasiBoBIuMSHym0bNpo1IKHVKhbTT8aNelv3X1oYE6R%2B3qsfC0NO7tehocyuUgTgoTGQPxVdSe42fICv6PiBj0LPtJqXH7L4Rt%2Flo%2BRDF4kH5p3Vj7RHXw3LcrU%2FtHcgYiFoKIHghv2wDDGqbO%2BBjqkAarZyZxNnLUSt3SgnJ%2BIZ6JUa4A9BMhJabpfcSNL%2F1aRe5hPd4lKKo6U%2FIhrsxoHu4QOKMxYFalGERI9oGLuTn8noRbvYWdsoG%2B5WL1E31LYr5JgKQNEfXvJkHwJTh1egFsOiOWOb7cZPi54cAOvcu9pkJBHwhtgVpKhmHvxEx6Tq28FKAvMaMLU6eZbK%2B0Whr%2F4Bs9iubsAj5mLzQa8Vg4QTI8D&X-Amz-Signature=94315c6ba443db4f331afccf9aa521bfa527975dce83534fed82bc191759a60c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2DPM5TJ%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIG7G48QUmYyFRSu70503Tfw1lRZNizjkacgWRxfOc6%2F5AiBVLgCNeoYeuDm5nLy%2Fjd%2B0G9t4dfOzcTbXiuKB5MPzeSr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIM2KVXTy%2BtF9A3PxAxKtwDDU4aI41E6v%2BagXXL6Gi%2BZwiyInlYoq0GZ0Flufd8ctg%2FlkT4ICx9A0Hf0enbuKiRLiaejGKm0rwT%2FksqHKyFJdm8KXXZiyCh9U6WLOJMxWZYulJvmTzbZk0p0Z5ej9MgSkyc8pxE4PN4Wp4KswfKWe2%2BTAQwGgfSgXK3nGDi8BboJuxsNG4MC6AhHhMtfJBZX7ueIx7vqbKyKCjK63gjjOknoHFj2o6MNLj77tqZOPbwjwO%2FkhKCoA3tiNTEHEvKDzE0Hi2kjHhBNuIxBdO5DR3KyTvHwFe%2FTfI9Oh%2F0Nbg9i8BdT6S0j0pZ4YCUFF9yonb0siz5tcsUPAN9Hpb7obuN0G1pwXeyTCGYjR8GKgrtI%2B8k9WyWZGM%2FXwhnaD7nOX3UgMPMOSP%2F2eDsUqU5Yf5WuEOWbcgVRJ206vIz6lPHczFYNnah7sm5NXW7pdVi250JuYgXNfdmqlt2tIcOUJl9iuzg4%2FvbQX3P3ZTVudSq%2BAWq64OWw8BRpECThoECJvumExfcW7as%2FRT10N9iGHA3Pu1XRtqZ0md5qvSEMp5BsCTt%2BVo6s%2BZfwnwWqC4RmZnLrjrzUX4sra06QNiRK4uNwMmIEvgN8dtn6S65LK4hJ0HAlwhOE%2Fd693Iw76mzvgY6pgFwYhNe%2FaHUz7XVAiZiFG9ZyinOyI7LPIIoCsLyy4m0edBFu0Tq3rg0LVyAzNNBdyZ7SwZfGT8LKXjMh9ZojsEnlTndgwcXmXW0qiAZ1V5zsnTYG9JMVdmxNwu3lMcoBOFAZmKvlHqprkNiadNBonO7UjD%2F%2BxFriYG%2FD57fGQJ2LeSFJuXV4iyUfOs5vn%2Fwi58ZE3KzlvINmdp3hXG1Nxyap%2BLSDPa4&X-Amz-Signature=6891a35b0b4723fb7cfb8c527487a19c8701143ab34107d038b05eac64d0e9e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2DPM5TJ%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIG7G48QUmYyFRSu70503Tfw1lRZNizjkacgWRxfOc6%2F5AiBVLgCNeoYeuDm5nLy%2Fjd%2B0G9t4dfOzcTbXiuKB5MPzeSr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIM2KVXTy%2BtF9A3PxAxKtwDDU4aI41E6v%2BagXXL6Gi%2BZwiyInlYoq0GZ0Flufd8ctg%2FlkT4ICx9A0Hf0enbuKiRLiaejGKm0rwT%2FksqHKyFJdm8KXXZiyCh9U6WLOJMxWZYulJvmTzbZk0p0Z5ej9MgSkyc8pxE4PN4Wp4KswfKWe2%2BTAQwGgfSgXK3nGDi8BboJuxsNG4MC6AhHhMtfJBZX7ueIx7vqbKyKCjK63gjjOknoHFj2o6MNLj77tqZOPbwjwO%2FkhKCoA3tiNTEHEvKDzE0Hi2kjHhBNuIxBdO5DR3KyTvHwFe%2FTfI9Oh%2F0Nbg9i8BdT6S0j0pZ4YCUFF9yonb0siz5tcsUPAN9Hpb7obuN0G1pwXeyTCGYjR8GKgrtI%2B8k9WyWZGM%2FXwhnaD7nOX3UgMPMOSP%2F2eDsUqU5Yf5WuEOWbcgVRJ206vIz6lPHczFYNnah7sm5NXW7pdVi250JuYgXNfdmqlt2tIcOUJl9iuzg4%2FvbQX3P3ZTVudSq%2BAWq64OWw8BRpECThoECJvumExfcW7as%2FRT10N9iGHA3Pu1XRtqZ0md5qvSEMp5BsCTt%2BVo6s%2BZfwnwWqC4RmZnLrjrzUX4sra06QNiRK4uNwMmIEvgN8dtn6S65LK4hJ0HAlwhOE%2Fd693Iw76mzvgY6pgFwYhNe%2FaHUz7XVAiZiFG9ZyinOyI7LPIIoCsLyy4m0edBFu0Tq3rg0LVyAzNNBdyZ7SwZfGT8LKXjMh9ZojsEnlTndgwcXmXW0qiAZ1V5zsnTYG9JMVdmxNwu3lMcoBOFAZmKvlHqprkNiadNBonO7UjD%2F%2BxFriYG%2FD57fGQJ2LeSFJuXV4iyUfOs5vn%2Fwi58ZE3KzlvINmdp3hXG1Nxyap%2BLSDPa4&X-Amz-Signature=bbbe8808891ffff0f821c17bb99862d0323a2ec2fd6f8b4bcf2b108f29c0ab55&X-Amz-SignedHeaders=host&x-id=GetObject)
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