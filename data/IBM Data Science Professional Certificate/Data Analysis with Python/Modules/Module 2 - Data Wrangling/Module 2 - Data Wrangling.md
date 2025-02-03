

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQPEBFV2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIH%2BTB1Jo3zBJh8Yc%2BKplqQvniNqpD8xkwCzndnxTSFhcAiEA0jJcbi0e77%2FBTsmg6OW4Oycd9JqXA%2BIbXQkMhXu%2BqVgq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDDCwr4%2FXEXOGo6BmgircA8zdXyTaPl6tJodPiMtaxUIO2u8OMZKlwty31d9rDOOBKqpqvTb6cwT5LqWF1TRoEl5jXG3xkru7C0OrXH2sMNrpOtitiNZuYoK7s4KlhxFA%2B79Vv5hqfkcJ2OpTLndBhvQfJI5NxyfzSEPGaRJh2iU9cXPuxFfXB1qFrf%2BgizFLVYEUx2ClAS3dSmmp%2FupgJCdSSe0WDhLev7IWFHymtORVrSxxUsiDu9ivVj%2BdJw1UTm4tPxVSPpCGjz5tGySUDHv5Y1aJ4HiiNU4iSn67Lu8DPZ81GHvoF9t4OSsLzyvBXeIjsqlUuMN2itlA9Fx1GEOBiOlCQcHmu7drFCeB6ofGnGvY%2FaGs6bKVANZ4MmnZowDptOik4RDFm59wcy79YkxDKMQu69HOBPfFi%2BgYeeHZx4IpUbpG4INtiWGRKhWwiO6XwwEvrKRNae5IlKBf0iakrZ63zIjDsAOwAp1N%2FZQCH%2F%2BEM6ciLdNcUJuBkJAvbQA4RBIncoZhlgrm%2BNmLX%2FY98oql3kFrb0tgKzq3YCDYOqkeEBLCwCoSQL0x8zm%2FyQzQGeVpmESNZ1%2BYIXkwUXvyyklX99KpzEEO8qelmvoLCC6mLtun1I2b%2BJuKRPZGYGBOPy%2FaFIyAAPuBMP68hL0GOqUBUx%2Fx9RUEIIgXvK%2F%2BCe4nqbNEwPKV6nm7SBzbiTIhGkWsv0meBLBHpysZ8cCUJjyEhzXTOU8DSxykCUoApSrMbGjKRlCV%2BNRXtOAYcL450SrcxoakudMEqXP%2FcATtAX755UB313u8ofiP9TNW9fVEK4YgwCzGiTxq1sbAZW3mublpYeHY3YUZs3I54EPfiY5Hq90XijVQqEjD9ZS9YL0u5z8mfsTN&X-Amz-Signature=9ec7e4e0edcdd5c9cb6e7cf628ed5b21bd4040060d0e3fd91e3c5078f41cec1c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKZVZZPD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIFaIcw0aipqSkZGsxEV%2FgB0K5mLeYsGSUnQWaB94Wh8cAiAwqmepxb%2BNhJ2NxXxoOid4krd2oeLfkizQ7sgEkQPUair%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIM%2B1FmAzS%2BAEoGIAu2KtwDieurmyikj3A8B8QSt4ukl%2FjnzhBEDZFBnagzwdn11m2wEaX6lwBKUoNiuNuGF1YvoBNrrrDOnkbvXtzl%2FBTU6l%2Bw27atS5M%2FOKQ8Vh02raQLkI9NavBJerXZMBwAdhZ7ftGQnSV4b75d0e%2F%2BZZPbezdoeLQES5dRbgg9TYe8jUWAZUqNmmnegphJebOqb9%2BsHINDswfXtRnVDK6eU20XCruCX%2BUR4Nza1E2pBWPZfdFcj36h6SR0TimDkDTA78vkswjCsEK5FG%2Flc5k%2B9lc27i9lEQPehpS%2FOYpN6I5FgKj8hkLU%2FPisLF8zcBcFxweyF56fTPVtLuIqX0LKFHHyuKQtnhjtySS8f0N7nawsH1%2FTVwN27izDgZw6NbJHybIWcNI4LOP4VopIYzxro7E3vhpOM9EVt%2FmD4JBxwOD9AVybYK2AZC5ZAqUlEF6dwlJOiuEmbN3SxPNHwqijVWwqe9%2BOmVfq%2FbngkrVs07lEOxKxfpd7dXaGc90xMEq4jyGUtEoNnWkdssa0zABbbOwFfreQq542%2FL8uLlqx7Uacz%2F0uKJznKHi9%2BRk0DkQJkWsV7DzbI9bbOlBAblwQQoAryo7pkDwT6tSCAtPLPVP84UNyydzye9Ka7DzkHt4w3ryEvQY6pgHjkxel7bvi%2BKmLVNn0pieHMt%2BpxfDY0Ngguq54tgPsJMOct6RU5NwmPiCalGxGnc7Qt1kAWxc8CRC8YXFOVgIzUY9EQyNsONqvbzuNFHHIEs650LLUgHBhSdQ0yHha0y7tDO5OnGUrTfTRAiTibhVqV0IZNPzeV547VGSNCK%2BODfIZ4UNdgnPc568VKCCaK1pXD59nv4Hlr%2FZOTOWMvSk%2FnxRkd3R9&X-Amz-Signature=f2bde3ea9b0058b5a0a6cd457675973996c445df781d9c2f4c1b1461020ab964&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVL7UU3N%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIDay1O5GYEZNPibzJTgMN%2FHtjWSmRsEOmRyVnV8eWhnQAiBLdf0qT3oxE4bCd2zw6OurDVzFezF0gGVn93U%2B2fdZoCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMDnNsG2RzypE6G24mKtwDo%2B82LDQoKGthVFVE9nKqTvHV6XUeUEVD1xxog46%2BnwkYgDde0ZEZAYhA0GQTgDgfkB1q2iu7XKcuT%2BI47eJDstvs757Cr3gtmsJiNPfTRo3VVEUN4crDwsT4ezhurnGYevjgTfejtzlGe0XI6AFEqHL3hGmiSzupe11%2BAp2p1OHyH44FCVCs9EBZS08YO%2Ftm6Rs%2B%2FwNahou%2BeAIMF0nZfQaJN1qJ35SrZO%2Be2W2AUN4QMUmIryPLOvkOICJt4WIffCRUmVh8%2BWpq9PW2gTscFOWffm92BywN8vYRTQbi%2B6q5M4SnX%2FfqJicVffZRPBYz7kFF%2F40m8uxrUpZ8HB1l5MSzzgr6p6OiDcCvChDB7hRCHjGJwx4tDXFZHSRILWmitUrCD3rT4HgDxSVFN8IvGp4TGXhO1tyScfj9WFc3xC14dK7j0hXeWDchCqtBjt88xgPY2Ym7gqd9Q9rFkpuc0ZqRuiSZRIsRU63fDH7BqsqGtUaO0jK18xMK7V5XD2ue90aYpXOPmo7ib7Cowi%2BpwJj2uhIY%2BW285j3Jf17TwHTeo4g0P5UukIMfYfrvYcV%2BWipLdVpVicDGiPx9%2FsIdeHdCmLlarZP%2BOldhbaPWZcrDJYRYoK9DAKNNJx8wmr2EvQY6pgFQ2dBERUubqGNcKuyAcEaWMUpKY9Wd2I5Dj%2BIBgPKR%2BBX7xbRsH3aJb5O%2BJYjylHbDXJtxZNBsChwvi3ndbjOTe7nJh%2BbQsk50Rjc2sl9JGW2n7tAGuyfjhIwBifRME0qNfHGbUjFbzgoG3Yz3kTb169Z6GnQpUDFiXL%2BZIYNwkl1atY9FjRd8MAEMph6FIH%2B5gjXt%2FaPK7rky5Keg3UyXQIvxfdFX&X-Amz-Signature=63472e7ca6be777b34031779dd971fd4ac6741d6e46448aa7275724d055b0843&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DOY3LRO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIGqhD%2Fzfqw4qz2V%2B1M8J%2BT%2Fx5Pr6jcq8CzVUSbLEx3OLAiEA6fIrJ5UfQkbo7nBTBeB7I%2FRHK6LXnBSLHWUa8TQ3Id0q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDHSs4cDlpbNbRCFv7ircA2WuwWPxyPrgI7xooFibWJOkr6o%2FKjqaJkgmkrZg2HMDne%2F%2BOLYbhRc2a5aPP9ZbCiMX8wUZXcIM%2Br12gt8Dj4Z0qpw6jtjoBJZV9nKqPz2Gqz8X1ghBtwuh1Qz3nFgTWaTy0L%2FkiTP9mAipksJjnzxL%2F8CAuF44yd8QyQjchR5V34h6mkMHc9tHg40WzasdN8qmZSWKz9vQt3KxZf%2FwUuLe7lTLwkCu3cFEmibzWZts9UnDBo%2BOAaHGuaKO1z%2BdjbakOqFDoAL7zj6%2FGd6dq3XTdcgkuS4GR8vYEH7vOpDpAqIDvhc%2BzKnoQK59X%2F8%2BTAwPEp0JEHLtVLrvSCDzHp1l6xPBT9%2F3VjhgJEDIFr5aZ906tMbeSlYxo2tuEggvdBxwe9QH15dMeXm1Gmd6J%2FACibYA0EPXitGcvqNI91wpYpa2vp2rYsrLzzWm71F31U13wlR9Rsfg1EAdNct6xddKXwtNuw9dOVRLEAwXnoHZWSG36gYC44FL4jB%2B49oEep7q%2BbgKLv6NIVc94q4EIhv7oWffsrq2r%2FlbxwcqAB5dmlGw6lgAM5A8HSmOq0C%2BCcxBCBsiztbnCyem8wjpQEHp3SpNkKkXjQlhavRRPWzXGR3csd%2Bw1WROfpo3MNy8hL0GOqUBB99MFKCB2%2B3kZ878MqBQ2Wdq2qHjligom3FzFiWj%2BcfiJqh1hjvupRVBErYeMvvWPs0HiaAyfahDhINNgFxZnf90Lu%2FMXs6ORbIZxUIXpRIRIq3ZWMgJkUbdWSSg4mtI%2BNDB%2FWuzW%2BCAg43%2Bbmy%2Bo8EVUPO%2FTWokC44a5GMbReJ%2BxfvUJHGU4kJ7ScOpoPF2vKgUb8lpXdrCnUuSf9AtOAO7jEq0&X-Amz-Signature=a974516a69fd67d0c4024097606037441bcd00d4da468754a4b968a5ee694d9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTJCAIGS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCID1ASenOcGmep9dyUsmXF6wRPkGqamV46jugdWvAjhX6AiAKoJgs4wNr2FPqNyb9fqetjT3pXGHp5o%2BMkK5WJYUSRCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIM4x9kGF4XyuqtLpliKtwD0cnAjMr6tRPWgAbyucz%2FMjqAqPaLb%2BRpTKO7%2FRqShkHLpwdYIBniFu5uRR3aOcY%2BE5npG66xbq2RBRDLcuyfjOAjfpJ7GzFTT80inB6WFU3xyNWHAziSdEMFKX1QuVFgRaTB545xWqEbYqwOhFlufmj%2BsZXpaY7GIESJHAdNGdq3rsAHvfPcw3GoM0449P9z3yrdAJW%2BlhRK4yEUTSqO797Xbc90pnMxC0MGU0228jqPk1C5SG2jmR9%2F%2BcdWc8zSjS5GNnAgch5EzwlklxILkCfcrblH9MBIRGIz8N4EuRRppsLpvN76iBgNem4bEHV7wrtbCUsQM0JYWM0n3aAuYqLQl8nZgv7F2qTfYHYbJnxx3D4nJKqYv7g9mrGAToAtU9qUncaa0sXBKj499mgMP%2F8nRQlYjrVNrLfyq1yssdw1rmSfBE0MzorANig7gtKlxIk2uYF08GdTEBYMLqIqvgful1WysmnvVchrjXfPCBSI8re%2BfGBPwX8z3h%2B6Ih3dQ9%2FCtTbNtHzWuoN5LQ5K%2FI2%2FmGcpDCjVr4q6UZnrTdloLeYnQJ1QUAfStSnon4QUezFhepWNoe9bhrGHisYpRzX2v6dl%2F8%2BdkzapLXJTdDWT8xtYcOxHRjnuNzkw9ryEvQY6pgGvuoRpMBC%2BzuXkuF3VhFsD6IvSZZ%2Fg7CuzBOFUxj5H9FJCfWPWCJLLs9QynWtCcXpuSCoiXSZgyBu5QQOQUBq8YlCRdns3i7FSgFOHPH2ytVF6BJW%2BKUPcsszh7qugHCrdyrArRcerY%2FNL%2FFORKV295vW%2B%2Ba3W8ASgxJDRgpGG3hKQbSsA1AuNGmOSqXn%2FKl%2Fyxl3eU3KPXD0l0dUVsXXUdfpoRDF8&X-Amz-Signature=720dad4f574e90a61c4ee531f286747ae3030834dde25f77b1d95063a58399f9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGVGZ4ME%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDoLWCy3Hs3hEbuJcNeB7c%2Fws%2B9NIk8pZpr1cm8rJmADwIhAN7IlVjlsOuwOkCPHLd2jJqNzHBjK49moZi6ya1AledkKv8DCB0QABoMNjM3NDIzMTgzODA1IgwgRDZhsA%2BZHbNkQOEq3ANb%2BniU6upn9SRnMec8ZWuX6yufUfLsWxlteH%2F0TxFy4LCLLiHmp55jKnBeNuk1W1MMKu4D4eyu4sOlWr40pSJ8uJQtgko7S1Y6jhYKKe%2BAG1NZkz70i3yxk7uXNWuae1fpZJQIW85ugCHaZIIxRpgZQ5kQwId6YQUATm9Z0CtPp4XB%2B1uKLFEy2tJjy8kWomIAk%2BPwsDpRTXzN%2FDWvw4Kvhq8qkiBCvRZh7UKtWxnVqownOf88MyW%2B2pGtlZrNlGpIuADI7rPH2wXA3BGnngei5q87dtg09%2F7BsAtuU%2BxPavx%2FOAgozmlFbEWutkF%2BkjQ9B99HJCfEZXaeVe2MUxmU5QqY9SEYW4XEvPlUWWXKsnKSXQfCdhRgG4JXiqXUf5mKOe79gGvzp53Klh2sMAFERdrMSL4zxilvSc8DKk2idmxJ0F2BFmyaVYDHl%2BeRpnwnv%2BfSUO%2B3q38usHfzsc1utc0F%2Bocx0FVzqqNBjD1Azhu%2Fwvf5i0z4wbZUsy1O8uOglJNvm2UUEFL6kG%2F6yqvXdjkLhcV5S1XbxqpiGkp1TT6yQxoHuYQlokVEbem3pdP6PGYx3A7KAowfVfznTNtYd5IG%2FFUSBlMqJQAcz4n7T5Qj8YGasvTCU1FcNzDevIS9BjqkASC5c9hCAoEf7wpPQkHdwlXdOovEQT8BRkRuoaZ%2BV5%2FpwN4urqOMWSdM2Cn6fDB25icAEK5Sl%2FB0%2FEbOaStSBAKysiZ5QsjXORS1F2nHWYlLJ4rMvssjb4WKx4xtIyd71SoONz7JSZgS6uthtDvkSmIbMA7APrtpRWG5FOZySXRteFpQRqI7XiZGPEby6eJmF%2B7KcWK0Paov7JnLVjUf9fGKZhX2&X-Amz-Signature=921971ee66cd6c9148a667a08ff3687695c58bc950c582258de5025820c328a1&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMSQNMG2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIAMRLrIjxqIMxGMFzl9irNWOYbqETXvPU6zDys%2B9DUk0AiBLEfGM7O57gkEsqdquFHf5uwYIdReJx9bTrpCL6Oum%2FSr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIM%2BmnpWzf1ueQ1A5rgKtwD414HwglNs5h972BXoNHK5mnV4NRfVwClAjsC%2FOByemh905YJhaikm1cSw4soSw2SQDVRQmGUXhdeJ2320JLHa0vOoCMJ8TOvFy%2ButoA55wqhir%2FEY9XwzQWAG88bZrRQSSx75mCM2S0kAv%2BhtUAAg8XTosoDBTzCdHOE1%2FTTYuKIoNaPAai9zndvNIaBRP%2B0%2FT72SbaFVC704CcrV1ONYn5IiVe%2FP8iLLoTD%2BSp1BRfjY%2FQV%2BO64M0%2BnespUcL8KNcYm5vROx3NUtJVID0HDlXU7qb1CH6bGCmUjaZGQvmO3f58Bo735HOjF4SAGZb7T4DTseJ%2FXfUf1i3uzoiCxErgVifNTya4f8GFIf6xwdG%2B%2FwpOB9VhPNRShKhFzb3eUpqa2SpsnOkTAEYt4Os9KGys4PF%2FGvPGfZ2ewfaaQmtF4iwGKXLqANXS4XwR44LffhGFOOjGS168ejSp%2FakvxLEqV3%2BupxI6h67Botzzh0MDUHZu0WTSIQbnUSH5rpqCegHyfB5F0yWyZFU%2FiR%2FRq6yrfHOjd%2F5A%2FWPPpWiddXrHzItM3%2BoLJpMfBY1Ji1OB389LP6E9e3zlSTwrecAb%2BE0LJhpjqrsOGwNKrUEu3IvtpdnNRMSnTyWByOpQw6b2EvQY6pgGaGts7ulDiEV4mrTXoy4IAp9DfED5wJJB%2F2qsfibX6xAJmgkZbg9TN%2B2%2BXqxcAt42JOsTCotRn9ah7f4cSmTQ1zJupK3iD37VzVWiMGQ181ed4FmDgBwZ61l5aWYuN1C81lzP%2B44sNlzXedF5keWoMmeg%2FNt20PrnslA4C69%2BvrI5iMZj%2BWpuKL2LNp0EiHDSjhDLzKO3bP1desmju9p9xPo53Ma2%2B&X-Amz-Signature=8cc1e1c91b5bf88a4684320540d15180d9c89390ff6b2bb7c149171af2b10c04&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466467I5YO5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIBxAZ5KsFXOcKRrCd1RqeSZ5eMlis6ZEBPoX%2Bxl6VIK1AiEAjkQR3fBJmkMPbFZ31%2F6K1l8o4bNV70gk79I5UIwsvDkq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDHtNXjNRhoPLrFRXyyrcA3r7q9JpGq%2BlErER5INmLjA9eeLbx0z9hNVP3hNPfFFGB3i3r4exKyt0qM6tGnHZa%2FGo3wxhHxA1x5mqswfuThr520%2BcoF25OECIJVywBF8p%2BADJdwF%2F%2FZhgVtAFAU%2BUsvfnmYUVK3wZBezlT5JqrV9uB8%2FuBmQoR3aFiX1G1y4IAfopRDw8ETtnjp0MAs3fP%2B3xkvTNhS39X9pWnO9rmtdoWdurNgCx9lTE4qz0UYUBZQVABqDASMI1sZIK77Bdpu28Ub33FhLRSveeY75sk7vJb2Nvpd5Wmq2TvS0dVPPUJtQ84HcGFHRhtASDYjJ6dGxeKOR5PVwZcDXeCvmm5alXKhdb9t0FlZNGjGkEGUlBeW6BtdBUryNEacqeBvhTK0GxgAxklcIOg3R62QzRfByDOdMNe2YL2WIhKCkPucvT%2FybVY3TRsMIC6fh2QeoyHNsjXrm4iRy3I1n0%2FTuIXsYELa4SPeZr45DXepFCkkXhAQWQJlQCjLq6mj4%2BswyEv%2FpsZghuJHF%2B2BVWbSe9CmdqUuSBvXPwDteZmSzMeKsSp0TaK4OAbf2%2FUHSFk1oWSKuSpsDlZyK%2BQvrPysoVrFM1%2Bi%2FMxWUAaVY74CHMVfnpOnP37119BB%2F8IBOlMN68hL0GOqUBy0yr9WWZg%2FNKhUKl1LH4%2F35yiMTyVY%2Fn%2BDwVqeoulKAf37VSk3lrpMb38Eb29gvzRyHnpfXRfG%2B52eoyk79n%2BFm2NvsuOu09FYD1s3XFBEQdQ%2BaaTO7STZ0ebwSqwQZUeXmk%2BYBcSeuMCHv3WtPfwN5eMqZjKyy3%2F6SEpgbIvClliIWSNLPdvOS8S6%2B6%2BPWmhKOqfaQ2pVpEqVifLNF7XcCbGkL9&X-Amz-Signature=7337cf0747067e3a29e5f1f755f0a5c313893dc2ff33571c25fa9d8c1f3f92de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTJCAIGS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCID1ASenOcGmep9dyUsmXF6wRPkGqamV46jugdWvAjhX6AiAKoJgs4wNr2FPqNyb9fqetjT3pXGHp5o%2BMkK5WJYUSRCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIM4x9kGF4XyuqtLpliKtwD0cnAjMr6tRPWgAbyucz%2FMjqAqPaLb%2BRpTKO7%2FRqShkHLpwdYIBniFu5uRR3aOcY%2BE5npG66xbq2RBRDLcuyfjOAjfpJ7GzFTT80inB6WFU3xyNWHAziSdEMFKX1QuVFgRaTB545xWqEbYqwOhFlufmj%2BsZXpaY7GIESJHAdNGdq3rsAHvfPcw3GoM0449P9z3yrdAJW%2BlhRK4yEUTSqO797Xbc90pnMxC0MGU0228jqPk1C5SG2jmR9%2F%2BcdWc8zSjS5GNnAgch5EzwlklxILkCfcrblH9MBIRGIz8N4EuRRppsLpvN76iBgNem4bEHV7wrtbCUsQM0JYWM0n3aAuYqLQl8nZgv7F2qTfYHYbJnxx3D4nJKqYv7g9mrGAToAtU9qUncaa0sXBKj499mgMP%2F8nRQlYjrVNrLfyq1yssdw1rmSfBE0MzorANig7gtKlxIk2uYF08GdTEBYMLqIqvgful1WysmnvVchrjXfPCBSI8re%2BfGBPwX8z3h%2B6Ih3dQ9%2FCtTbNtHzWuoN5LQ5K%2FI2%2FmGcpDCjVr4q6UZnrTdloLeYnQJ1QUAfStSnon4QUezFhepWNoe9bhrGHisYpRzX2v6dl%2F8%2BdkzapLXJTdDWT8xtYcOxHRjnuNzkw9ryEvQY6pgGvuoRpMBC%2BzuXkuF3VhFsD6IvSZZ%2Fg7CuzBOFUxj5H9FJCfWPWCJLLs9QynWtCcXpuSCoiXSZgyBu5QQOQUBq8YlCRdns3i7FSgFOHPH2ytVF6BJW%2BKUPcsszh7qugHCrdyrArRcerY%2FNL%2FFORKV295vW%2B%2Ba3W8ASgxJDRgpGG3hKQbSsA1AuNGmOSqXn%2FKl%2Fyxl3eU3KPXD0l0dUVsXXUdfpoRDF8&X-Amz-Signature=7cfe50e4f00ed7be7ac072384d35ef3f8a5a5cbd9356078b2b726bd59cebae28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWUYUUT7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQCsf3JCSkVoXFDmXnW5utSRoYkHYqJB5SW1HFbVwhk%2FjAIgOBud8PNwZXvJ0Z7kMenRHZnRkViDz3GGMusKqVOwAAIq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDBuGpso7u%2ByTfJZ%2FRCrcA%2BIqjUEAms39iOazbJGoF7%2B4TXW7kuCiLFAfkALtfQ1KqjQl1%2BShJ7VSa5vqHCiiS7nHxWfGshUfx0mU9SeNTU0enE%2BdOT1gWoGTHahimSIMEMB0NoZfU0QdtqhpnyGuKoaUHA5pnByPW8KrR5K9D%2B9c6ARyiRbIRcr4emprW2fuVkjlcbQ4TIKe9N7usORVVWON%2BLWy4ZGoy0lpwEzVfuXef3urHFxQLCrqwn7hG4xQROHK2SQmwP4%2Fug8CFqr7nJirR9abMwYgJJI42J4dIqDyQNGVdyg5R0eFFzywXTzQ9tOihxKv7fT37mdKSsLD35rxIRCRt1g5FdVkLdYYqkHiYOET6X%2BIeyYXdiZ2ytexXg9t0%2FM8XWk2dv7dkFGQV8klJK6Co8gomqkjGjpN3knvFcPpBV9%2BIEkMpNIqi7qdEvtYglaTjiVcedy4pKAqF6t9UluBWzB2eiYbnchmDvCJtQdJW4t%2FAt32McEAEe4oNWQ9de4D%2F3Ai%2BY8NCocbFKHIH3d1rdSkVeDCTl66zD7ypZcuP%2BWYI1L%2FH%2BSk1WZ3LZGA15cdhglr9%2FBmr4%2B%2FHjxLbBzdrf8B%2BSKf791a6fULQtqN94Tg7nku1EZ6EVK0a%2BjdO2HVPEi9C7r%2FMLa9hL0GOqUBeh8FkcKi1U0zn%2FOKYwzFysqbKiU9LkZl0mmkSCZvHJkmGZbYWAmQu8aP%2BJWG4crcwUV0dNnE8uO7aHepKuRCyDa%2B1JKaKYEhZz0pl50XsFC3V3ityxynw7Zsg%2BdF1F8a0%2B8QJ8r87psNujyI9sq2c9rg1sOZR%2BuNNDbU5pp6pd3Fl4QBGJYaJvHKcTZQF%2FLk8V96aW5J7iYdJL52Xaz%2FktCPixbf&X-Amz-Signature=2b63422fd6ef376882725a825de91ee70c357c24020f9dcbebd434f56304271d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWUYUUT7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQCsf3JCSkVoXFDmXnW5utSRoYkHYqJB5SW1HFbVwhk%2FjAIgOBud8PNwZXvJ0Z7kMenRHZnRkViDz3GGMusKqVOwAAIq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDBuGpso7u%2ByTfJZ%2FRCrcA%2BIqjUEAms39iOazbJGoF7%2B4TXW7kuCiLFAfkALtfQ1KqjQl1%2BShJ7VSa5vqHCiiS7nHxWfGshUfx0mU9SeNTU0enE%2BdOT1gWoGTHahimSIMEMB0NoZfU0QdtqhpnyGuKoaUHA5pnByPW8KrR5K9D%2B9c6ARyiRbIRcr4emprW2fuVkjlcbQ4TIKe9N7usORVVWON%2BLWy4ZGoy0lpwEzVfuXef3urHFxQLCrqwn7hG4xQROHK2SQmwP4%2Fug8CFqr7nJirR9abMwYgJJI42J4dIqDyQNGVdyg5R0eFFzywXTzQ9tOihxKv7fT37mdKSsLD35rxIRCRt1g5FdVkLdYYqkHiYOET6X%2BIeyYXdiZ2ytexXg9t0%2FM8XWk2dv7dkFGQV8klJK6Co8gomqkjGjpN3knvFcPpBV9%2BIEkMpNIqi7qdEvtYglaTjiVcedy4pKAqF6t9UluBWzB2eiYbnchmDvCJtQdJW4t%2FAt32McEAEe4oNWQ9de4D%2F3Ai%2BY8NCocbFKHIH3d1rdSkVeDCTl66zD7ypZcuP%2BWYI1L%2FH%2BSk1WZ3LZGA15cdhglr9%2FBmr4%2B%2FHjxLbBzdrf8B%2BSKf791a6fULQtqN94Tg7nku1EZ6EVK0a%2BjdO2HVPEi9C7r%2FMLa9hL0GOqUBeh8FkcKi1U0zn%2FOKYwzFysqbKiU9LkZl0mmkSCZvHJkmGZbYWAmQu8aP%2BJWG4crcwUV0dNnE8uO7aHepKuRCyDa%2B1JKaKYEhZz0pl50XsFC3V3ityxynw7Zsg%2BdF1F8a0%2B8QJ8r87psNujyI9sq2c9rg1sOZR%2BuNNDbU5pp6pd3Fl4QBGJYaJvHKcTZQF%2FLk8V96aW5J7iYdJL52Xaz%2FktCPixbf&X-Amz-Signature=4f72ff4301f6fbb891d6a11d513b9ce81907eaab567c408fe513d3a1f27e7438&X-Amz-SignedHeaders=host&x-id=GetObject)
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