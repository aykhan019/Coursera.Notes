

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z7G3BNE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIBp0TLXLPnd2JGHoHV7zRXw%2Fjg6e20unfyC9d32kMebVAiA7R1quO85%2Fxa5Pv9zbVdNr%2FoDrAHcBv7Lv3IKoRf8EMyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMG75We6C5Xq8GFSGAKtwD2nT8JaPmt3g7tU04QipgB5YoIL3h4WELZwDXHVcB8r36yxdgVGwlM9qBr5l0NYca4eq6mwfoQ8XsweU%2BZeRQTchVAI4zuHdSfY5a9oJw%2BcWNs4dJAdAJ%2BVqjbYd%2FV2jttIDCi2oAPIqpyP725TQAmuS4nLDav00IYBo5bii0LaReklI1S%2BKzR1NUjWKIuPHTM%2Fd%2BXm1NXo2TtLZO%2BdobVj5J6DvS3quTrXkdbQORh%2FH%2FD7b01SzdiQhdZbOaDDBESnjMnknsugOlKxCQ4sKdItIPaI8vIlcstADIh7NO87Jd%2F%2Fn9DuTejkOHHxndBDHZ2Jx90HHUUZccSNIxXvhZW3eqjUiIder%2BJKM3F4eSPscdgR8e1Ng6bVkNLE7GEtTFuHNUYPvKY7ne1j3BYon7EjGmJLe37yKq8egkQn35HQkHeEgOh%2BZEYgKmlBS%2B6jJgBHmbgt7EGZ6qRgAyUPt6u%2BNyYQmmkp7cXlAr6eW0dTSOK%2FLgQTCn55IdgexB%2F9q2VR58bNX3NyHzUvyJOAe%2FyLta1K78e1M1CWc6MPNkxX7oziq4vee7%2BONduO5TmNB3MhGi5QEjvArzqakvu85O%2FmfwpBGekX5%2FoQscUerj5yRL7mfU9wtVQmL1CCMwk%2FqWvQY6pgHNDfci7UwmSgW2NzSY%2FLaof9Fu5%2F6SmnfEviCmw4tA%2Bmg4QSL1L3lvJHyddIjJU52sNFeHV1hvL8gtiy8QVw3XmWGgZID5A4te12tyNk14dQfB7c6Q%2B8ftYdMMUDVdj7diTrgw3ps1H2LhF7FhJqwZTSy95sxCC9HN3LKBXjBgVI%2FSjziyYhazMTRrPcGY1klxnqpwJrDcUNcqbuKKCsRqA%2BO6m9rp&X-Amz-Signature=c21f7e30ae6ca835cdeb71cc182974b75b3b383d9b3c2be1bafa722c672c971e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSCHO2II%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCF6tA%2Fj0mnjfWWF9UsFVuFKe5SRCWFlkF4PQepRXakMgIgWDquxiMbUuk%2FY6i5edYPrLC5PYAo3MP%2FSLez2Q9Vhgoq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDHHIXsjaZ0tkW16EJircA3gV7fcY%2Bya%2BlBWAcBO9eqntsM3AduHtrfvVvL4MynlAXzYAIUA%2FITix4iO2FME5vvRmi30Tk7J9HbMQfl9WfgsKedge63RrGoBlCiCaFmLciKrtYAjq8lPXeMVqxj7aWy37FeigJaNVsbm6dRWL3GYYL2%2FcoeT05HGQOOGbWTfiQoSetXXyWYam6ts6IJrRzW5k2gY7hDsp%2FYqlVJkbS3jbQayriRdV9AJFhUF%2Fd6ZHi8L6pqoGE3WPflpgV58fKu263g7CspwcXqlv4bmCVsadtR5Auvj0btteIXQX%2BlSk8zS%2FGEXTpSGplyKYuRfCt5NAYqt6AFMkgsH4MRyujR3lj9Cs0SB92y8toFM21P0gCvwJ82mYFg3ryBemtLZrjiiUCNtV3EPS3G0SQaBBG7jhfe5yUvn%2FxCjoGo6PBV7tyn8%2B0C8s9EtaGraa4bh23RowUVLYu3TvLCKS1fCZ1GMVSj9dSuQWCcHe%2Bi81ZOrGuBMVleA3JxUVruJx6NUYE%2Bw4fBGqCoq5PJWnsIoavHA%2FZsWJ7vAcl4R06V2sUej9%2BF%2BLWobIcKdK2mswTOoJpqJtjIUvnZAs6I3%2Bt5doKWIjhgvYuEmjJe3pQ5dvE9wFz3c4pJTbvD8LRs74MMH5lr0GOqUBxN4GCGDLEOjnivREe2RbMF4uEFpooN%2FXous7zvYxiIV2nEqwJuYM4uqIB8HmPSvSaL25Kr79RrxO%2Bs5A5%2BCtgDGvORV3FPRXJTJy2ACbCMEfX7ct%2BS6Z8ia2%2FYNWogEZ1g6y33j7j%2BoVFz8aGFWB3WumLE1tVLru%2BmSsGS9ossgS6pxEqlpqOOuv%2FTzJuLLZnIiDFW1zrlP2BN4vsJqoS2PF8G0J&X-Amz-Signature=48ca4bb3e591251f50c25bd531be89f3524ecdc1c6d8bb40934787937c2af4fa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKTDARZ5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDdI5qBWYpjmSTEEjJ1iCEvfdGlZosuBZ4y7s%2Bznx9wWwIgTiHFGGAdPv%2FnDynfCYrPuNTRBTDcZZe0ECFBPsmv09Mq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDP7pv0w3zflHg29rgircA1EkBa0DLLoOywocL%2FNTeuns%2FO3hTTbel19vcW0o3PaFpPUQ6HYPXLQO0wf8I7ZDMr5liFDQa2Juez2jkGHUmvLMrfVGjSXzyJG%2FQUuPbmZmDIberMm9kXKU2GXU%2FpVb2PW4g4O7EfwHBmUfsHeDMT7XH7LLzH3g%2FjsK9rImantbHBmJKmLML6L6YVSkdrCw%2Fe0D6UAQtxNFVRNUUw%2FRx9YEF9BRpu1k%2BEeWlW%2FkfO7R0dWN9gDaD1uqaBHHoOyw6UvZAQbvErky%2BMWDExUU9q1sH%2BuOCj4IyTYd78U5lxa9rWApSmVdUKzqIXwkX9y2proXkWqNhLilGnD3EnkvfFGRZZeKjEVy9JeLIS5EYJcR7%2FyhU2yUFIsDRJEql%2FQuTrsETHWp3ss5%2FPWfLydHqII4y6CVnW7AbUd7la319R5Yrtvc%2Fb4taXjWyEQclTA9gfKI%2BASLtGRw%2BKwKFUvdEQEnpmVDp%2FQbfc1wRlBT1KUT05sY16dKDvfk1u0S8QlpV1jluHEI1bvYO0RZY8KHlqcxJ21H8e%2FzCmUTlUDZkze7mGc8harOTxP2ngeVzupZJClpiW%2FjFVQWR5dHHf9U6sA7xjtzWqH4pwU%2FNmJXcP8EnzaADTx%2FW%2F9kVJdmMNf5lr0GOqUBML42EL8hPM1Ef0oate%2F5GRh94HhQR4gTXRXDHGLbv6gwQQudDq6xfni4XZeUxXni1qLZsjiN96C%2BhRCoMcooRZeJ4ZU%2FcLGjlQOLNYSEuxp9xuOtgTxa3rqKW36oIynCCexEk1tNyZ8Ttt9nkPuPag11hBGDQrrJWZ8vuXr25TQ%2BlZEvlEr109%2BO1vu6qg%2BWhCHZkNqDa%2FoDvYt18I9vUkYJdxXe&X-Amz-Signature=16e31554e728e361aac4852e9d08dcb50d8790c509f11124dabbea7bf877b370&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643DFQ6ZN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIENKlg0I8whyM6ORUMGwHVBCizSvh%2FdfUazjYGLpz6kmAiEAu7kCbXM5bv8EmWjjRXJFBPbBzAl2sd9wW2E3Jl3fe20q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDJLCevAsLMT45oyH8SrcA%2B9U94jDNtq3vJWKYOtqcoHuxleGu2fHy81Ckpf4yxsZpu5IbI%2FCem7IEAkyTlNumf94kVEn2tSFPGZ5P0U8rAFtXOo4M7uk76Msp8zpjBpnrS7B04JOUyeXDsF%2FN77M1n5UiolpaintGNtkl87G2fk%2FiRulZPhIz2M84QwIJaidQPkbBmFwTOjvITMc53vlpCjI%2BADIg%2Fs901ySYrghwv4%2BydUl9fMi2TOafZAWIOjXaqzWRSzEkM4PyVFsv9%2FnczGMsKouxcvDbfGC8Hwr6O4CnVoaAhve4FScN77jGU4EaBG1XCGOorEY3HuJlrrSZ0B0qSqpU4Omon8RVJeD74s6jfElr4SIXC3qxIJf2KZWQr4OceyHVuzBEI0oKXgDbZTsbkzB8gFhRxdHOf%2Fc7nb2jA5Vat9a50V%2Bf%2B%2FYksaWf43flz5a52eFgfucjJ6TGVfal2eVhfTxbdR%2F0Egc4B8ZvhTmTVJlW5vZZhTG%2F9aemtZuvKMNluyrAu007qux848tfrpx0qcw5Q4F7V1pBkNi9%2F9rnOvggruDkL7d04YuMQ6T6LDC5mx2cMsWXNwejxVgbc5qhXfo7o8zX%2Fz8ZRm6APhSV7V10LE4ATV9WndQGIFGw5Dv6o1iwqJ0MIL6lr0GOqUBcOugsAI2K1k%2BsWjKiTL69ie86bZch05RplEyDGOV3e9FopKh5eagmS2fQrHGice1nPi5PyyED0c63KlNH%2FePdEfFpXhvxMTWfwoNGZOOLxgtnWCuUgen604vqixnlGpCQR0KdUXIhie292dfJhw5vSQqRkiiF6S4WOj8cRrClba5KK%2BBsD5hN730OO6Ba5Rl7amLA07%2FcVT98mDLTiWj4xUvdKl1&X-Amz-Signature=05d343f434e9bbc6cac922c6af4e6f83126eee5bfacd659371d1ab75d94497e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EAX2MH2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIC5HteN1Wzsx%2FlKWxVauIlJGcK%2BI2iyKkLOKpUgPpqx4AiEA1cNtsVCtswOZe%2BFM%2BzIcTcBdGyXe7BzZH%2FmYPtChSbIq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDHfjfX6iSO9ga4cHQSrcAxCjG2VTmTM%2Fx68HKJWef76n4PN7M9PKiDxENhp3SOHmQ7G0RNLi1%2BFoVVqzgSvRERdXPO9h24He3%2FqPkNJ54MYkx2wgDGVL2xqnnPFOE6TSjZ89JgRE0EzaK%2Fic%2FNt0aWLIfHMsRNyd4AD6JN2reeC0LDRCRVN9qtLlfD0S9A9jgUcwO%2F25BJCpk4QrxxsLdDE2Y6fZlHoNfQrKPUB%2BjIwokR1d8Athzu9JsLIexpl5BhkoViakMwUnI4ecNVtaPw4WTb0dKj%2BXiFayOooZ66tMCo2MvyYrbqpaFcTriI2mGOLbBlL2K%2B5Is6f5FpB%2BOiwI62Q57mE8sp2wa0Ya8nAvSh0HNmNcnA5JWWVhs0BzSZDXwpzPFsii24dILMK7mhF6KqrQ3ThWmMVJ0BXQ%2FC2%2FD0bW6i4NSRnLJIB%2FvKMF6dRNPxm158LodxXXCnnsyv%2BrvNGG4g3VrxyHaAH%2BrAUDreoiJfW91hjmkAMgoQdnIJx0RxSLGgVYoCeTtnl2%2FQyLXP76qB%2BulW8V6Pp2hh%2BLMGnzi1PrzaQqPXATYv9I%2FSel%2BnBJPzW1bWO2jDvV0RFOmg8EZ2Fby6WMc%2BqxFmNHPkiOPjxOC%2BK0m6mdah88IN%2FJ%2FDgmMXziRFY6MJv6lr0GOqUBL%2BlGEIwhj0h9tV0HU%2FU3YFXhjNEme9fyZD5rSvdtyP3hdIdW3oneMAJQKaYL4MHTohAjcsyf8JZ%2BusItycrHpVMAygnmxw7jcYfcItwyZUqmffzIcQ%2FeCLPHjVFBRZhpgsR%2BdgbgJt%2BUFfqWqtxq8vn4e26zqJ5cBsw7m9YSQTS8R8nMVF3U561rnT4r61h2TkocxB8I%2FjVIbMQbIs%2FboAf%2F3DhB&X-Amz-Signature=96144841f15191b0a8db753548113ac691e445c9cbdfb7d59f3d607ab15a1e82&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EZ7MBIR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDcrdFjJ1GsJ%2FnX8PVqVv%2B0%2BRFaCJsi6cc9vO%2B6vAJcjQIhALbM7%2FLKP3tYfQxPn3W8tpC28S%2BegSKcIaAt4dRRv1VMKv8DCHEQABoMNjM3NDIzMTgzODA1IgwtRsoNj0xDFDsGdL0q3ANYRMVbyyNmzYbPeg7Z%2B36OPyyfzmubZE0R2zo6rivCtLHcsPWYAv%2Bs%2BWG0J%2BokkLCfCg0l5ie0AOI2%2Fm2aTtqH4TapEMnvQtRXmi6YhCGoGPM9fJDFZrtuyEBBX5fcHIcLoTU20Y4KjzVRzEGPYd%2BEiWo0McBDORSm%2BFKNOm024gzFG93U9ojkvJIeOfQkYI1LOmK2Rv03UUtQLwrjXfMn7ZljzeiwJPZh7jy9jHwUbLDdm5fatI0qmXOxDsrzQ4AyWvQ01%2Fa1l3oPIDFRLqI2R8m%2BIVkixR%2BppHnW19tlseAKUKmjOZwatj0Xhx%2BNNrlu5OMZ%2B2isShJuIG5Lr7GD98qR7VPscwzwlPDjtV7OSZu0Y61f6IqsH86lr8knz0S4YNdQHShrMSaOmbgJNKKqmnpkxgLDT1XJeLu%2Bqf8NBg18wNILvIgSG8u%2B9rhXs%2FIng7BSFIx5ra5kYiUJVGr7g2xs%2FFsSJkXxru2SxNT8FOXP4tRAnUg%2BL7fyAAhOummMr9Dvb%2Fj13zlrPEns7xob%2B8V9CybyzXP8yYqpSCXaAdORc7f6FZ7nc4yOc3hkar1MhNVYVFKYBDmXThKf%2BDQvXG9IqIwIf4b9jwNb%2FHWkGOZB9L35V6n5Zo8dcjCb%2Bpa9BjqkAev%2FS3jAg1AU2%2FRuYZ7lz6tmHhNMjSEtjl0o%2Fh0XqoyooudrHSTHfW%2BTEvi%2FJ3ADTLbO0G8u7V1mnrkz5rnjRHETxPhLno2ZoQyar5cNMQRiGUZ4UZ17f9h7NWDJ7IRApv1sXzx4dPa3j0qXcoAZaf1bOVVqnYzV6J5mj%2FxJy8vg4nozPbNLyZVRsOTCLTDIhPqDfdhWtc2mnuyLGDR6AzBuoQO5&X-Amz-Signature=465461314a1dd5cda6e8b5a4b6eb05347b38d1680641eb6326e1afd2131b3b11&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GXWW7K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDbnFwTVrvIW%2FvlBMmv1%2B21QuFmolfJXmX0UoN4C%2BDHLQIhAITExLqZlDidacrZ562YYo%2FGaOKzbxSZqr5TUNHAfOzgKv8DCHEQABoMNjM3NDIzMTgzODA1Igwolv3FtzdEKh6cVVYq3APwUOXYF%2FMkJj%2Fc8SFMjXax1VT6%2BSsn3KlqsvHna%2F8U9o0ira%2F7SfA2CegKJw9gnLpdZ9rpA1rt0vIGLxkkWfouTpfRcg1JjVLFxxUhfntJ8dZKz135wk9pDkI0hFdl5RF0ZHnhV9dRnzoaLkCV6zVnt8VOeeB3293cHtsO0KpHrVuRKnLaICHJqAhTp3i8Y1qR0mlqgc4JInCGJxKj1WmC2Rp12KMjxENvfZqUON72jqOZJmmmU2e0HhDzzdeCCB00ECiq%2FJyGl636AR6cCP9P%2FSsVJQg19dImLwpXw2fk%2B40DaO6GH4QM10e0F5WnrSDDXAxHGuqbsJOOVebSiyb1CIJtf0v1REy%2BCx7D2ITDWwv0a%2FGiJeOa7pX4ek%2Fa6Csks%2BixQK3UU58Bz7%2FflIkWsP%2BV8GF%2BY%2F8NOnJab%2BdfawAQVrxQGIRtczhMqk%2FcHeXpFXRpk6GWK3weau1xvkEgEb4hAs3hV2Vy0b1PF%2BBwhBYHLFe2ne5KKEmobGUef3y%2B3gxpRFoDO4xNLJgEkUvakIPsHa2yuNqQErQlSsBl7MpT9gQnHkGX516B80PR4X%2BDn75mRZE3WvrAvvlk3vISTMxvaFFYSxuiiBQtvvDVO0R0yJLcJ%2B20I10MQDD4%2BZa9BjqkASRizhQsLr%2Fqr3D74QkOXfkWT8lAQUCoW%2Bq5jtY%2FwEm097b8WhjkVqDhI9lrX9Gk0R2Y9VU7E7q%2Fn0AnYTQxV17Cp%2FX%2Fox6%2BB30i5Bin96VKP6sR7nTB%2FtxT5VT9nvPihxzmyiAvNObHk004lY1xptZFvaNbgsn4HHFm%2FaXHa%2Fv1wIYgLPXgz0gdJdNTyA9qkNRblxlme7hwjMJMRRAyKcR%2BGsK4&X-Amz-Signature=faee152360cd38d8e9f6884042674a6369ed68c980536620d4ea8217db9a429e&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7OBHZWM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDfXuD2lONN%2B3LKCi0nB8bCLEB9ZQch%2Fkcl8cZtwDZP2gIhALo1%2F4bv9t1EsolVoLV7mvipAE9aXwr0N%2BjdBdkfqeXqKv8DCHEQABoMNjM3NDIzMTgzODA1Igy%2FJKAUUf2R7avDzOYq3AOqF%2Bol%2FeZtWXmtOxIWJvJ3piZw0uCHuSDGtvI7JvOnr4CkaXS7yVSlwLqTd6mZFGN5DSBkOsy7aED6%2FC%2BnJtEyak2dP6BAVftESHLyJ8eCKg8ElzybKZ8P6HIrho%2BgpW%2FPnCThaY7zzV69sIoXbYL6FA6sQXZP%2FImUrg6xXP%2BMsp6bpstcISJnOPc9IQ6rsEfeU5x%2BCXDu7Ky0weijhx0p3M3Ond6JBqLXLF0Npwf8LyNOc4Upt1WtBv1EXri0ipaCmxaURPjrPpFPnNRNWTKTES0QPw6m1R88DDnOzt2EnN5e1lLX2TGYXxu2zOihaGjdztefYOu9AbCECvoQ2pS7Nz66jcrF7lpSNos8pnxlspQ1oOqw67KbnAlswHUV5h9xe2wlmm9UHWKum6OjSVFcMA7uRQW8XEkPntrKcH5AQp4OdVR%2FZJtjjQV1YYgpb0q0TK2qknd%2FFKO8A7%2FCiIcWAgGycVqX7VaSyJxVyqSP3tLOdXtP4RNL4jcX9Y95Ie2VUqZy05wlz57Qw2TOYaqxHLamiM4whcIyq7B4fm7ois5b69In4N2VnziA9vZzqQXMEJr2B7SM4cLKUGysbhIt%2BdaMF30Fl6Z4yUd7GD8EPXcJzR8q1X83Kg6hjTD4%2BZa9BjqkAaEzN72FGIxJCY9u7j9twFfABKint4CQJ1koP3tJtQAPZZqV37H2B8O1iaH6gWR9C0ZNSviMA2sEX8cga8PEw%2FL%2BeferdE7XJz3zreP4nqRAFV7%2FWnnpCiHDA3qaEa6Xt0mPs53STfRtI1OPBrmdx6rq2s3eYVSaQ0PoPwku9FHyf58Z6aKA%2B8888iOHu7EB6yQjXAJLCKH6mf2WWb3xhS%2Frp4pR&X-Amz-Signature=cb40f309085541c38658ca87f0eb5718b5e16c40d802920701b1944a1aa19186&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EAX2MH2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIC5HteN1Wzsx%2FlKWxVauIlJGcK%2BI2iyKkLOKpUgPpqx4AiEA1cNtsVCtswOZe%2BFM%2BzIcTcBdGyXe7BzZH%2FmYPtChSbIq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDHfjfX6iSO9ga4cHQSrcAxCjG2VTmTM%2Fx68HKJWef76n4PN7M9PKiDxENhp3SOHmQ7G0RNLi1%2BFoVVqzgSvRERdXPO9h24He3%2FqPkNJ54MYkx2wgDGVL2xqnnPFOE6TSjZ89JgRE0EzaK%2Fic%2FNt0aWLIfHMsRNyd4AD6JN2reeC0LDRCRVN9qtLlfD0S9A9jgUcwO%2F25BJCpk4QrxxsLdDE2Y6fZlHoNfQrKPUB%2BjIwokR1d8Athzu9JsLIexpl5BhkoViakMwUnI4ecNVtaPw4WTb0dKj%2BXiFayOooZ66tMCo2MvyYrbqpaFcTriI2mGOLbBlL2K%2B5Is6f5FpB%2BOiwI62Q57mE8sp2wa0Ya8nAvSh0HNmNcnA5JWWVhs0BzSZDXwpzPFsii24dILMK7mhF6KqrQ3ThWmMVJ0BXQ%2FC2%2FD0bW6i4NSRnLJIB%2FvKMF6dRNPxm158LodxXXCnnsyv%2BrvNGG4g3VrxyHaAH%2BrAUDreoiJfW91hjmkAMgoQdnIJx0RxSLGgVYoCeTtnl2%2FQyLXP76qB%2BulW8V6Pp2hh%2BLMGnzi1PrzaQqPXATYv9I%2FSel%2BnBJPzW1bWO2jDvV0RFOmg8EZ2Fby6WMc%2BqxFmNHPkiOPjxOC%2BK0m6mdah88IN%2FJ%2FDgmMXziRFY6MJv6lr0GOqUBL%2BlGEIwhj0h9tV0HU%2FU3YFXhjNEme9fyZD5rSvdtyP3hdIdW3oneMAJQKaYL4MHTohAjcsyf8JZ%2BusItycrHpVMAygnmxw7jcYfcItwyZUqmffzIcQ%2FeCLPHjVFBRZhpgsR%2BdgbgJt%2BUFfqWqtxq8vn4e26zqJ5cBsw7m9YSQTS8R8nMVF3U561rnT4r61h2TkocxB8I%2FjVIbMQbIs%2FboAf%2F3DhB&X-Amz-Signature=6e2fe736e1303721bd5afd609f7a3c6c1f6ba8235abb7cd0fba2c3bed988e629&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHP5PRLW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCSsmiBP1SfZ72V4%2FwVA1LlpiCx%2BVnjJiDN4W801J%2B2bgIhANsRmq1GeZhStXTSsUkqNIqJanuIU7rVgke6hGnKCrxQKv8DCHEQABoMNjM3NDIzMTgzODA1IgxOdLEGxDpKoc%2FWaDIq3ANkfLDtH91rUAgLFVZbGH0Zs2aGxeMaom7P%2BPcS9gzRQGIMm7dcJ8qTQa3mPm5UjA4WEoYqrR8hqK9rpJATwW7PB3PehUOnNCyJx2512g%2F6l%2Fm%2FvwcybiibkuW6LNSZ%2B1se56w%2FiIDWOmGL979ComW4w0c9bZCd%2FMFnwtZtjSPIxBkF%2FBWBi96di%2BP%2BnUPDxqaJDJwMeSlzuSWGZ%2FLUJXbIDrC%2FdRrKD%2B6J8IOc%2FIsDZu%2F9dCtDhbekY%2Fi2ELh%2F8Tty5UcHwoSn4vBVFgRfDjyikDhGY0ctZNW774Z4x%2BjwtlQGKmoXJ1T9whXOfILTKJtZJORay3HB6kZU022PNlFMIay6%2BpUr0eHOggXzfFlp%2FmkwLJrHcivFHx7%2FFv0gqqxM3a1tLC1SL9GD6EDg85UHY3SsBwO6U7Pi9JVWyqFezqNZl%2FVMMDqV2kdGJ48CuS6Tn%2FEeAWQmhMqsFSxysXH518WANxBG1WZ74kWGEy4m5tR9nSJrWQeV9hZYGv95IdlXUqWH4bWvgg%2BSYCThV%2BODp6OhptL5Eh7%2Fv8lLORtrLE44ZQhDGiLK1BLu2%2FDh%2BBt2y4LUbAtncrg2ujXglyIn2XHLYse2gzuQ1yZwJUZtKZHc5Nq8XSsdC1rCDTC8%2BZa9BjqkAb105znY0tdEon8HygV9b6XZhpzn3fcoGAIHF%2FmIwQMGS0yQfeBNbuWWDcjdhfl5G27Ter0jWmx%2FeMCS1o5e8oPkMxk%2FJ1Q5heKUJuW49W95hWV1c1djpOg22mfNTqITzWWqbSmvpykD05XeShq1k60yVPeDKN1AqspaYyB3H%2FIQsQFDggzexhfENiv0VEJ9KMZ9KXeheWhvmjW5V5edQvZJtJZT&X-Amz-Signature=f8a1868d7e51ca03cce06eba7b4e093fc8668603f3031873b9f246e56e640c4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHP5PRLW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCSsmiBP1SfZ72V4%2FwVA1LlpiCx%2BVnjJiDN4W801J%2B2bgIhANsRmq1GeZhStXTSsUkqNIqJanuIU7rVgke6hGnKCrxQKv8DCHEQABoMNjM3NDIzMTgzODA1IgxOdLEGxDpKoc%2FWaDIq3ANkfLDtH91rUAgLFVZbGH0Zs2aGxeMaom7P%2BPcS9gzRQGIMm7dcJ8qTQa3mPm5UjA4WEoYqrR8hqK9rpJATwW7PB3PehUOnNCyJx2512g%2F6l%2Fm%2FvwcybiibkuW6LNSZ%2B1se56w%2FiIDWOmGL979ComW4w0c9bZCd%2FMFnwtZtjSPIxBkF%2FBWBi96di%2BP%2BnUPDxqaJDJwMeSlzuSWGZ%2FLUJXbIDrC%2FdRrKD%2B6J8IOc%2FIsDZu%2F9dCtDhbekY%2Fi2ELh%2F8Tty5UcHwoSn4vBVFgRfDjyikDhGY0ctZNW774Z4x%2BjwtlQGKmoXJ1T9whXOfILTKJtZJORay3HB6kZU022PNlFMIay6%2BpUr0eHOggXzfFlp%2FmkwLJrHcivFHx7%2FFv0gqqxM3a1tLC1SL9GD6EDg85UHY3SsBwO6U7Pi9JVWyqFezqNZl%2FVMMDqV2kdGJ48CuS6Tn%2FEeAWQmhMqsFSxysXH518WANxBG1WZ74kWGEy4m5tR9nSJrWQeV9hZYGv95IdlXUqWH4bWvgg%2BSYCThV%2BODp6OhptL5Eh7%2Fv8lLORtrLE44ZQhDGiLK1BLu2%2FDh%2BBt2y4LUbAtncrg2ujXglyIn2XHLYse2gzuQ1yZwJUZtKZHc5Nq8XSsdC1rCDTC8%2BZa9BjqkAb105znY0tdEon8HygV9b6XZhpzn3fcoGAIHF%2FmIwQMGS0yQfeBNbuWWDcjdhfl5G27Ter0jWmx%2FeMCS1o5e8oPkMxk%2FJ1Q5heKUJuW49W95hWV1c1djpOg22mfNTqITzWWqbSmvpykD05XeShq1k60yVPeDKN1AqspaYyB3H%2FIQsQFDggzexhfENiv0VEJ9KMZ9KXeheWhvmjW5V5edQvZJtJZT&X-Amz-Signature=fc7ab9dc99edeca7e5ffef7bc1173cada30ba995cc6a555588e8dbaa79208390&X-Amz-SignedHeaders=host&x-id=GetObject)
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