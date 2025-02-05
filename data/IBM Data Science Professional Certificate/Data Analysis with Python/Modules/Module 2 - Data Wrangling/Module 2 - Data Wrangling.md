

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWTHQU65%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIDqwfQ5pqSen%2BETMYxoaUs%2FCo20VyPdoxRy2SeYQd0ChAiALBdS01aMhtapj5%2B9Q7zgZaXEg%2FBzcGDi9krGal5F6Gir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMdWrJRJsAs1igv4OIKtwD2xbNrSuHcut5Ma6Tl%2BtjPCSeZPqkELGIYT9TXbfinjdh5WOqRLKoBikY1wy304G%2FRqn9473QvZrPEZ9zehLEj1AvL8yHG%2BwdO2naCzSwqE3Jonj%2Fcakq72um61pZkmLB1x2fbmFyvoc5m3fYtlnJ%2Bh1uqerAPvYdjoqlrWvbJlQSfqUXUEmTYnrMtB%2BaoHlpAZiHNmSY0VT7RTEkIRH6LsB%2FaK2kAci%2BX8GuFew28IPdkcz8z9HtQ2U%2BJTtBQMye5XqbZJMAuDL79vD%2FDHakEKYB15DiG8zyX1z3jOYaqG29eLJYGgm79fCfTAKaViGEtkyOOquECt80Gi6gm9IHCEd3qAPBrAZYYnwrvIohku3WnMYRGddUCSwzrrfDD9g72qci2JPj9EHWd20N%2B9dyWuazgmWzsIOSyuc7UROGCmkfSJbyYHLfYDeiyZ0zC4DO1wAj%2BjY2BEnPSSdbbITTiyq7rOejglCl%2FRlvO639kL%2BrL%2FSz%2BpkCoXKt5GJ3LAEMRFQ0Z%2FopBt11OqWjaHeH54xEErBl%2BDd%2B3DzgVMQHqhCc79os0Bo4Y3E8PhyJ35ZXfViRFTnEllquuqbT4UuC%2Flv4xu64jfmA0knYrcREnAoYmF0cz%2FnlQDGtITgwrs2KvQY6pgH%2Fwm1Q5J7tSKxXPvjiDFL1WA3xIf%2FIsIGbsDTVrPD0mUaWZ2jZ3bk6COZ4R6jiT8fZt1ke%2FxTzUcfYfSIpfuDh%2BfG5nCJlS8byQxrUPbdjxPNjV1B7CpPuO4fbrfk6aHn84WIBmfJ2BS9ipuophmW89YvtXuVofvAX1GFf9lGh0vDjdIWyDwyywGSWyqeUrhvvRm33rqHAXKK0rNZezGxavQ8kjiaY&X-Amz-Signature=3f4daeb2caf91af723b5559e2937445e1fbbecad1b6eb0c69546352eb50c893d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZOPW3I5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIGs6KfsMNLJxDIK4GVTcy%2BsH2KOVFEqyYbaJ90u5GjaFAiAPDR3r9a5qCel9DQlhkMwDKQUxxVsFzd%2FCS3GYtNraESr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMDLN1xzTOkXoSHi5zKtwD%2BzJmjn5tNoKnI0z89uBRXgLGInPZPbLohq1WljaRaDQEsaxiemrQPtHJWNnGwjVGK9%2Fy3Jg%2BDvgaHL3HRArrNrHYUXs8MSE5JkWxSsEh382yrCMMWC3Iwel%2FYyK1PGWI8U5%2FSBdkM5Uq69%2BTnEvuWZgeaqnemRZ3AlygMJl5JbbW19C4DoP5wloboHkm6iHbS21FwJ1Gxwio4EW2fiGwsQN33LB9vDnxF0PFdYQ0m96SKpt9ylr%2BcgSYDdHvPciHNsxKV2EHwFZRcNLzVA66%2B1LAUuXvSBF5rXSz9CwrTPDCHV39zWXtZuYXW6syRfzXnMxvHuL3vHUpNti1qyf0WwinvZBWXU2V7WRvWajnnhiyjke14ZSv6sR0VlFcX7RxOVbRHrzFiZgNGy%2B5kLz3zycd7cNx39bzCi0HtlnJBUQsLl6GtbIDq8GX%2BivDsNW5KFWmOY5EFrHuNf8vsauY0zy1WXtRJP831sSuqDB1BraZyxh8liIeJNKyTncSiu0MWJBQyQDkCrmxtELC%2F%2BK%2BOU0bzJsUO9cGxR0WGQKek86pBHZaDxmcsFekm6ziQjJeEhyysoegP92ReX1jwR1d5Ng1RYl%2BnN6oO491ciXKP1kpoxcMhaFweVvXpIkw5M2KvQY6pgEnEKtXU3GwP3VtVwIryg3lFtngY26tAhx14ifkikmDa8iDJoEokHGARvdA9Aj8h%2FhWJT78pkKwg%2FBMh2RbmPdj28UExwxR6tdciUpHVNYO0x6nsptpk4nuZHudnwQqVjR0jBlvFAZoLATDYOvf1wDes9p2hKH87paBicMQipmNayKvNDm%2BYUbqw95BjUpknthMgP6vrREGREs%2BOJWwFVk9R9nJETq0&X-Amz-Signature=1bf24ed1740de6dfb45f934993f8e382216845cca41ea3a61f55b3f6e65c3034&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TTNRLSW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFAizPm38cg24OpNP38N9VWqPw2BD9rGkefu97cFol5GAiA7k9HrcXk%2Bfdi4zl2QDw4W2iWjW2iRuqXx2vj8hYJ5fyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMgIwJEQe9sBfnHJi4KtwD%2FB9AKNMgd%2F0mzbD5Xs%2BfjAc7JPm56I4dCc9RhSRrR79VBRrYryYVE4tB5SHoEJl%2FNqO7EfNKYzLlwS3H%2B6LIv4B2NocfST%2BnMtYZEW8QCvE7x7VColXOchacWjYrihi38HOsi5eRYrqFnjK%2BIdoeYvlKwJrAJr2Tby3KzVXTtyre2mY6J2o8edZHgVLu9AvgSrWj0YOY9r14fYpY7K1vU2EUws1mQUjwDPeZICqVPDrMOnis6LYnNFYctAacA0o9%2FsfiounCMzzSVsEd1O6tGOZ15or2fGFvtsdPU%2F94ZRnGY%2BeOOnEtmPQNQR65w8Vi48HcAKL%2FfnKypU5oMR1uKOICf1pFGjeRy%2B%2BxJgJdD%2BI3G84aivUbBjPa8VSrghDluIJRKy8SsvTxqGB8MYXCSdMT2pozfGX%2FBzF26soHKI5ppn23xu3I3eV2bFmkm8dDmg9BuHOkLo80sTBucQy5nGbmhvL%2FjkwHwpXf9I3t8ktT%2BxYmRy59sT83l56Zmowx39woNo7d39zpHg37QIzNQm4fQZsDLvKbqXLvcqB%2F6oixAwxoNJKy4zqLT9LlyK9nYFtQmORv5L0NPKg3uxgs8GK6TPwJiVi1Syf5vOqHa%2B54Vb2nTy0phQTCyWEwrc2KvQY6pgH3Y%2BQniPIlFq3TuFIg7Gx4%2BlE3dw01vni6nco0eMj%2FTR%2Bup0ag%2BurvaRCKqh55UWvLpKzgeLEefz%2FY5cMnp3vRxBNld%2BglLa7dNMBAiUuLwPWMr9yVfP411gosJKbM3Z94O4bYfQnm6Q5xuPAoekglj0swwQ3vCF9jWYvvW7%2FMUPZbO4qJuj3E00u%2BVPT8U6O66JXMizq%2FbUsjqxYUk0boZXqwXbPs&X-Amz-Signature=d5c81d20f7708824f190ca0c34fc012f9994cc92267b4e550e19ab75fa427255&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRL2TVOS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIF3%2FfPilA1HURPc9rV2piBhuCGr73EDxMe1tqdJ0JUBNAiEAiVTSoiwt6ircWJ1Mtz%2BE3LaAb7qlU350xeVv0pYtzpYq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDEda75I92F%2B3UxmVJyrcA5G9ND%2BnyIRM%2BM3OoH%2FizdZh9eFsoEW%2BMhG%2BaGdFgZ%2BcsKT%2Bm66oDbjjJKo3pJ5DxLsha6NadRZozlL26iolwhx9o7jNXDBTN9otJjYds6LSmTE8YlquxuIOmc676tORp7FA6bay6Z5Api1cGN0qAbvuGhZWU7d5fiVitX9zdKas5q4UsrAzOLBeTOOF0YhNbnL0bxdTVnyM2kIDJ%2Fnclfnfbb2GWrtHSxyhYTyMSmOI4PsiAWbvcCS%2FiG57q9faZAOEq%2FpsG%2Fg93HOZnGDWql6n2%2FI27PMwSFxoX9W4Pqc7iXjABNfl2vngwzVTP8U1ASq5GVH%2BDgaN1%2FjzVoJ8QwTkau%2FpWASoLz8DaBwwoOnFGISlSGx%2FzNwMlPHs17F34uQMjCH6qDAYHIymU4VLloJs2F%2FLpmFaPFXkA105wbdYvKrqrzID3AgtvPDEfmnyt4hewIZdfxbC2fpjzoblULm8hxE94v9tVqzV9RJWhGDYTdRXGmy9Ld0taHyTL28TKnv4R4YAEhzR5%2F%2FEU3el%2F8DYMr%2FxS4GH8wym5A0APUGh%2FwxMcT%2F%2B3IqchkaM2xCiukZm8Q6LJRLCAOstTu7C8Th%2FIa779bcl7VR8CcVNpFpZtI%2BUpZjImhZBWzVmMKXNir0GOqUBJ4aujwGepVnE5J3XaH4b3AIbE2xE9K4x9Q101INQ9GqUNgzuEkKzBZbXgO%2F1bCwoIpbj9R2H640%2BLlwuRv%2BJymRMZf2QXHxs8J3wJE%2Fb0Zk3tk4ZO5Nxh2ev05zGX2xYmCqLM1H0b7kXSZHDbh%2FNuFojeR1YbsdgteK5lQapzX0fS0basfwWk%2BnZuYcqH15iG8nARQqEXtbsjnjOjqO8cJxsiqYq&X-Amz-Signature=f7b3dde82427cfd04f502e5133456384e883a04c713a5eddfbf215da432e1f51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSXKI3Y7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIErQ%2FC4Zl9qc2oLJi15ck8uLY9qHrR6xDgA53W%2BTs952AiACzz0vJf9cafxUG2TC5C9OAZwkpbCvIhKPS7cpecOQmir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMLuKkRZaneZzr4dJZKtwDX5QfIDFxs5FlBG%2FOqQWf%2FFbhkFtHVjp2NQ1IiTrEpxIBNxzAHDz3lrUZAOGYdjQtKKSGXI5hM7wHudwXNes30T5j7jwqSGc608shKB3c7mJgm%2FBF7gmTF2z0NS3ZWLJrmhLkXcA0KFty0jnF24ELLwITAdn9uWoEV3TrbDBKjMZF3ibfDirzG%2FGiOvMVx5mJXmZ5Cbj5gZ932moXGi6UeaBFCuHN56DjUO76KlhImbFAeEDnuSFzE%2BbJBQhMvbvUjgtVpdrlt3gGHHbKV6sOc2hnZOwEDfsPQNChyvA8RL2XHIH%2ByPz6j8Ewe8AY3zIdL9hM2LGgRhgDeKZgjZRwqFwNJvfpZ4IWLMfUT1VSzrYnDdKGjDwV5iSMg0YKmI9RZCh3RU6pXClqeyBPwe%2B7M%2BbmDcmzZf7c9mDzzKNVxFio6TVFlpMI3N9L0fSz8Lp%2FK%2FUdp4rI8zqXrhLGXmLZzearXqsk03vSU4HA%2Bb6d5HhawPy%2F6aGrCdw%2BnQqwXxoBDOuxf6J2HXQ1pfs0d2rPzLpV0LQpKSUesa9iOC4EYcN9f37k%2Fh%2FVlwSu88CiGRhUF6yqF8%2FYplac8Q7D6e2zlLoerQQOyCHXIgPa3i1t2hVsquew2MDSeoznjvgw2c2KvQY6pgGo3bAlJLPY4GzW9VBSztwmb2sbIidqOoKAFahsM9aSD%2FFwzLWGSgDo%2B8vKkn4w9XWP3KSn7d7f7Io8eOFq51QKDD6WR2ubtzrjHoCFSDKIh4sFgyEY0afsvwjS7ytXQQJnxJM4w0pW6PNvvznfkBY6KogawtS1ed3epTvhHVFkPFJGy6aJQLEUhTgkgxKrNqcTtemSXU8%2FZ7XCqSmxRDPMvoNuXLAf&X-Amz-Signature=30b4c28ea3b4792872d8a0102db667e1d15d3660f27dc8876d52796019c81127&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNZAGUGE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBX%2FWSxSUqUW57SEsAwGWjDIdQeuAIly6%2BRjg2iSK38bAiEAz9BmFz1FShfeM%2F9V7gTBx34JoibE%2Fp0c36fkniG0kJYq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNuhdiaHJiv1csW6JCrcA2OpDxZX2RJKdqOaDUbxfsvuapeze5rNn%2BQrguLlwA1RGqgBFr%2F25f%2Ba7tA8R0gC3r5hZxnJShQHcy%2BZWBx2Thp2k1c8JIufw6L3%2Bil4bJbTqtAyTwtkdt%2F%2BCwaR8y6hWXs7N5WpIXWMnh3rQfqEQUKeUtjLK2tqelSZdfprtKUq7MXqz6zw%2BSB%2Bp1LxRm56nzyjMvUVSomIGb%2FYSB%2BtPCPnQymbnhQqN5rCTHG2%2BKV%2FoYZcmHN5oZTES69GrmTyp7%2F1BkJrqTNjAPKZvKGmmk%2Be0zGHk1JVraUXvPjwoJoIJ6hxumDMXRFNxf2hL5ZAgylFPrV0Pd1dSxlWyYSx4tndI4UTR6qK4G2UBlpjt%2BgyIVvDEpqFibrxkpD%2BaK3wFBZUhjTSE24Je1lFoV3dw%2Fuaen%2FvRXgXVI658%2FoglnQsRFmniO7qw6wSvo6FUiJhVXm1a4P22sTkC67uEvtbb3e54%2BglGiwX28aaHTy63rGTShjeMRJv0jkEwnRMxU0TmJC5RW1sRJD2d8gTPxAjt8rs4Ol7PJZsJia37%2Flol0U5nEwl4BJJ%2FG%2BLnVU%2FDSvSAlYBcgWyEj9eOAPAABxmdxaHWkZIqS38pmra3zbiXH8PELNTZrnyh3kmVMzjMOzMir0GOqUBjSaa3NNrTH3TM7rR1firtZ%2FxM94%2F%2BA7ACV3fG5nU4TultSkc4MErYpGOQUSUqzL25pQHLsN6R5URdAZYwjdjanANgHekLWE9zHhKe8VEOrc%2B%2BV7sEZMmb6Wy3lxEfuvUvnC1CYxStm2WJvvJUXNwMcI026hfW6meQ9IMVhYJ%2FIxyJPGwL%2F5ObSrPPW8s6tbIuB238rAtdiogQCYP4FHmnNT18bvg&X-Amz-Signature=d28d7129a11b758f0a834439b8d318950ec62fd7e3eae4a7103498c450c11d76&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPOI32H3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCSdrEq1NIkCWyOag%2BqOBaxFCnxbCc5uNbA5GPL6Xdl5AIgGrUHvPBsbhu6b8wVR%2FdxEXPEy2PiV75VlEluWuhai3cq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDJJ3LQqkw2vrbFwZqircA0rIDozFp4raOUN6IyhL%2FdPyu5Dj%2FvHk5Z0Cft6HK7cJrtqNPgtdeDUUdm2YWOcouxfvoqK6rqKMrka7JMOoeAZIAmkvMUs983F5IrUHNxIk8L99ggnBpp9ZvpfxGXxhIQRZfdygawff90HwLUMrP83pCE%2BZvrPtXo7Qhi0ircdXER3OvPZbvuS9cNALm457O2hqTHBIFCDsCVYURxBtZ2rpbznQaLXZySdWVTLL5wxZC7ZaQmRe4HHfVW6mhzX%2BRzDtA%2B7xyVNvJT9rn%2FTsWKGc1vdwaNA7C%2BA5euj62EcK2Ag%2FCvb5GLDzhTaxAF6yFNophpu03uK9F4sle9e%2FbXrz133%2F5driVB7YFHI7%2B6Ra55qKkkv9XiVd4cmPrAqu7YTpE4G5SZjK%2Fx%2BJQd9TmeHjk1naV9geqrlKDKNMH0Tu8nOtyVydJLxio4LRZEELeGmWYcinqNVzcDmfh%2Fgk3A%2FrU9I3XJKGbfipDOVc06vR8pUWrYZnL5%2B%2BEnY4Kjbf0cPqiXOFSPevAuKg3eE9Fl5Gzg%2Fq1%2FzjBsCf4IkfFXzVAcI2HUMmjTPsyqnXdA%2BcvXpHh0UeMlaatzTvPw%2BliNGMSpM%2BxWeCIagJUvSaWLz9BcFv56IwBgdj%2FXNqMJXNir0GOqUBcn2yfu%2BswpcJ4FZ0avyqtuwZWP930Kfxftb7I%2F7%2FEr3utYUuCu4jdgrC0L9%2FkFDx1w0XoNUzB7wMHD%2B0OBHm3p26UmFiaLavOrzdqbVYhCIXkIlf38gOhP1dhKSE0kiqZ1T3oBciv49RzxFlNPkcqab01SipN92ut42SdJntg3eWpnHeVeVp4wyypVwCD%2B5rY2LYBo9SHmmINpTcNFd8zDcUNgEO&X-Amz-Signature=9bfb247c77c22c0d7fc074a6f8ad758058f61bb3e51639ca3e6f249004467826&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RCYMZZS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCICT7l1fv5ubfLg57SkN1FDQI9Pdiz8PLH5oEaR%2FfkOYjAiAuSZiAuZS7Zl6x6jmmK02ljxY0oilF%2FzZbVqQEfyuCXyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM%2B5ENDwbAQeVzij%2F%2FKtwD%2FZDrFPl7WalieL4bFKhLj1eXtG4FC6OZTJmfd%2FtcI1QWqpVKP8mujsxgCKwMB26Ru4WQpOCgaC4XXvuYjdBjq%2FNmKWaVeiXyOQCusbnYnFUsKGquBGjRIwn1QOsSpKQkAGm00eDpq3odSCXJ4gq%2B9dl8fY86NqgzpizdBGSLqNO1nH9pc03h8sMv%2FsRX2KfmUyS%2BKQNrZUZnGsQPrCfFVQZok%2Brpi9L5fKhcf%2BsvgwItYb0uJSKXahQYJBQMhzrXXA35fI3tgjAWX79tzeLJw6R6PLFRGtjyigbfMjf5WTf8aG%2BsvvvlDZ8N67DsNq0PkdxRWyHbC8MFzBsHHXYTrrpkh7Sk3CoUlrSy%2BL%2FTbe%2B2nkSK3yXzAJOL3dvxUldZg6DTvLFMIgBvXNzKopEizlId7ev4PTjp2RzatS2rH049PRTJ6LOboGXDbb%2BgjoplmGiw%2Bo79Xm%2B4u%2FR5ncIfqsFD%2BvfnP6h5qHe8P5rCgKQIct214SVgXawN%2FrJXIyOrGB%2F72oompC6FN38dklPX5UyeNZgQZ8XMRQL0UHhzD8TRam2BdtrvZxmPpva6ugwj%2BWVmhdgl%2FS6J8Av4pSt2v5%2Bnzs2irjL10eyw4KOXzYDzOTMpu51%2BrEnyE3gw%2BsyKvQY6pgHTrJSYiyS%2BtPLveJyn62MQ9NOS27vV%2Bkuj%2B8WiGqzOtIRB6lgIiAwbwDn7l8aNUmEFa4pVMu0HMTzGxvYzA%2Ffj%2BbIjgRArEPYRmOvhOtMCmdHtUL0AIsU%2FKsS8htME1k9cUPO9x5v3991ze3%2BrpwD0br6EjbNgqUOQKfoauJOo7vHfkBDRJ0jkc0HH2NXSmlMhtF6UHCs6sF9w93R8MI3YjOKO683Y&X-Amz-Signature=1f506c02cdde50f67c8aa32eb6e284debe9ac13df44da1af5f4dfbeaef8fbda1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSXKI3Y7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIErQ%2FC4Zl9qc2oLJi15ck8uLY9qHrR6xDgA53W%2BTs952AiACzz0vJf9cafxUG2TC5C9OAZwkpbCvIhKPS7cpecOQmir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMLuKkRZaneZzr4dJZKtwDX5QfIDFxs5FlBG%2FOqQWf%2FFbhkFtHVjp2NQ1IiTrEpxIBNxzAHDz3lrUZAOGYdjQtKKSGXI5hM7wHudwXNes30T5j7jwqSGc608shKB3c7mJgm%2FBF7gmTF2z0NS3ZWLJrmhLkXcA0KFty0jnF24ELLwITAdn9uWoEV3TrbDBKjMZF3ibfDirzG%2FGiOvMVx5mJXmZ5Cbj5gZ932moXGi6UeaBFCuHN56DjUO76KlhImbFAeEDnuSFzE%2BbJBQhMvbvUjgtVpdrlt3gGHHbKV6sOc2hnZOwEDfsPQNChyvA8RL2XHIH%2ByPz6j8Ewe8AY3zIdL9hM2LGgRhgDeKZgjZRwqFwNJvfpZ4IWLMfUT1VSzrYnDdKGjDwV5iSMg0YKmI9RZCh3RU6pXClqeyBPwe%2B7M%2BbmDcmzZf7c9mDzzKNVxFio6TVFlpMI3N9L0fSz8Lp%2FK%2FUdp4rI8zqXrhLGXmLZzearXqsk03vSU4HA%2Bb6d5HhawPy%2F6aGrCdw%2BnQqwXxoBDOuxf6J2HXQ1pfs0d2rPzLpV0LQpKSUesa9iOC4EYcN9f37k%2Fh%2FVlwSu88CiGRhUF6yqF8%2FYplac8Q7D6e2zlLoerQQOyCHXIgPa3i1t2hVsquew2MDSeoznjvgw2c2KvQY6pgGo3bAlJLPY4GzW9VBSztwmb2sbIidqOoKAFahsM9aSD%2FFwzLWGSgDo%2B8vKkn4w9XWP3KSn7d7f7Io8eOFq51QKDD6WR2ubtzrjHoCFSDKIh4sFgyEY0afsvwjS7ytXQQJnxJM4w0pW6PNvvznfkBY6KogawtS1ed3epTvhHVFkPFJGy6aJQLEUhTgkgxKrNqcTtemSXU8%2FZ7XCqSmxRDPMvoNuXLAf&X-Amz-Signature=9e0c3657898eabdcffc7d85b9b57b0c8027a8132a904a296fca6683c6bc21636&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QH6EK7G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQD5vILsKg7%2F51REH68P4F0OU%2FcOFMCniyjU8jkpAXOoogIgUYkux1r12AaxXo2IG89xZpSe5bFRLUfbgIHUPSE%2Bq04q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDKYVSgCB5OONDQhgUircA7gTIg44DavONqeZ6%2F16R0o4RsfC1aBu872W1PoQxRjEcWMgSTxc55hBsuSBcJCe3ese7iGa6bU5sMArMJpJFswLIDrygQr1FoWtUhCgpKWfifNmjedb2lyHM89qhmSpjdV87OPfsjugzM9URQ0HQ%2BcRWxwBPjWKVcy1Q8S0chscNBlxXRuPhhd5A5IUGEB1aIblwdTRAwZkkHY5bk1pSpC5E1PKNbYprnmQ%2FmfMXXnz7BZsmbDFW42OHLcXBV3mraZag1wcEh92w1654TpbJB%2Fj0WXrUqjYbqro6%2FwEepL9cqszC1GJKonRdn2yFs0SUKAQc7pyPoMDSs97XdzVSrxVmgfY1vVg2Bgy1GuvOgN98aga8v672myLCEAmnQHK4BeeWp%2BI5Qp9OfmbcDhjZ5CdjKwoVBFRnR223uaXFBBhs28vMCLKyLtx3pH92VyRWnk4mrBS5EB72nME0ujZlc71rMmGIkOQXpp7WjB0Kb9LIzxofuN9K%2Fg4gzZPZQmhQ4Q1IfTMqL4bcbe3BC23So%2BcRCsK6dm24q88oRxrcN7rdu2DznCqHFXS42S67PoeLlwXO8eGs8iSx5QkAH0Wt7PE5r%2B36W1fjJeOEJpGulH%2BG0YRM8G0UujD8bOBMKLNir0GOqUBQTcKK1a1zGWbAWYKu9tNJMraXlfKB9tFMlbpy7kosvUQuPlqqXpp2HRL7X%2BMC7%2B6cojOOEDHYVy1sLdZG5xeJGl6QimDpChnZEabnDU5rcDwAcjLYm6hDh53suaeE0RLFfzEDmfxeYyreN2X8KSW67GVyXWl2sJUPheK%2B7Acrplta2Ehm4s75F1RjD8HFqBpv8ylLydDui2zTr1FX2cUouRePkRC&X-Amz-Signature=0c70195764ef1a1019405ff3e0f596bbf5969f4b6c097f710d22abf02897b152&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QH6EK7G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQD5vILsKg7%2F51REH68P4F0OU%2FcOFMCniyjU8jkpAXOoogIgUYkux1r12AaxXo2IG89xZpSe5bFRLUfbgIHUPSE%2Bq04q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDKYVSgCB5OONDQhgUircA7gTIg44DavONqeZ6%2F16R0o4RsfC1aBu872W1PoQxRjEcWMgSTxc55hBsuSBcJCe3ese7iGa6bU5sMArMJpJFswLIDrygQr1FoWtUhCgpKWfifNmjedb2lyHM89qhmSpjdV87OPfsjugzM9URQ0HQ%2BcRWxwBPjWKVcy1Q8S0chscNBlxXRuPhhd5A5IUGEB1aIblwdTRAwZkkHY5bk1pSpC5E1PKNbYprnmQ%2FmfMXXnz7BZsmbDFW42OHLcXBV3mraZag1wcEh92w1654TpbJB%2Fj0WXrUqjYbqro6%2FwEepL9cqszC1GJKonRdn2yFs0SUKAQc7pyPoMDSs97XdzVSrxVmgfY1vVg2Bgy1GuvOgN98aga8v672myLCEAmnQHK4BeeWp%2BI5Qp9OfmbcDhjZ5CdjKwoVBFRnR223uaXFBBhs28vMCLKyLtx3pH92VyRWnk4mrBS5EB72nME0ujZlc71rMmGIkOQXpp7WjB0Kb9LIzxofuN9K%2Fg4gzZPZQmhQ4Q1IfTMqL4bcbe3BC23So%2BcRCsK6dm24q88oRxrcN7rdu2DznCqHFXS42S67PoeLlwXO8eGs8iSx5QkAH0Wt7PE5r%2B36W1fjJeOEJpGulH%2BG0YRM8G0UujD8bOBMKLNir0GOqUBQTcKK1a1zGWbAWYKu9tNJMraXlfKB9tFMlbpy7kosvUQuPlqqXpp2HRL7X%2BMC7%2B6cojOOEDHYVy1sLdZG5xeJGl6QimDpChnZEabnDU5rcDwAcjLYm6hDh53suaeE0RLFfzEDmfxeYyreN2X8KSW67GVyXWl2sJUPheK%2B7Acrplta2Ehm4s75F1RjD8HFqBpv8ylLydDui2zTr1FX2cUouRePkRC&X-Amz-Signature=b9ab8df6b3906f9abdd29d15d47c18f1eddc485651ea524a05246205fef4c0e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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