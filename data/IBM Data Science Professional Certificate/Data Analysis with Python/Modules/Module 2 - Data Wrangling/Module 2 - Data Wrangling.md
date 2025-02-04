

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MLFWQBW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCICKVSpdLAnmzic3mxRhu9DjpSRZBXJhRT7HpFuBbMA%2FMAiEAyR3bKw1X%2BbHiDLhPre6vHUzTsJ1T1XyTCEqc8c9jUQ0q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDPyJ162Q3nyhxUp0SSrcA1ujMebmoYjKX8KA%2BCEn%2FuN9MQq5Hv%2BR8sw1A2FlAEFonFBgY8T1LceVIy9q67dqcwv19QXWt559MeppKilJG1FFBKRwBzF49nhPcMgwSfGTPk36liQPL1mOPWH7TH7VAq2pSQF3pRjCMP58ethuMw0tGn5t6%2FSK6KYehstnaPkcTrw4D0vjdnFq2xK26CC7Ig2vU5SbGCkJ6ADTPw53fUO6RZXVhF5NSY%2BHMMjb2LoM2uMiPu7ZW%2FCWvHFu%2BYC6WDJ5FGBZQCZsh7h9Dxh%2FSprSh8joiwTcpCRyD2n6xl2v4zHBWi7N872fmu9HW09vdFgGF7wc6i4WvLSqh6S4P%2F83P6C4UbX2lpQdi3oWcJW%2FIn4Ga8w2s%2FQEtrhLQ001gppJzKu65eAmGzhCvh64rOAX%2BwEYaE%2BzjDTHtRLA281xE%2BnlRUK4mkf8s1vXnHz7QZnoXwg%2B86P%2FXVyNXUeUrPszHqIWfaSUHIkrMRUsZY4kG4wUj%2FHlKyqygLIQU%2F3c%2FPSDOgnllRVK1iFKOWAXvfI9JgG8xpUVOBJADqu6qoFoG9sYLuIXaqGSTnn3v%2BIAqgxFa1bapEehhOvrw9yCPaRjPE7%2FVlIYUOYPjBQVQnQiL%2FLabXAltawolI31MJ7mh70GOqUBVy6p20%2F0Dl3pZPsxYO0I%2FFXdqXdnLo3NQigzfLFgZsz59Emb3xR4SfzBe8zMt%2F6jF0KUdu72bB6xpTK%2FEb0GJA94%2BPkE4bEG%2BJ9FtluFIiLG4J2hvoac3XeyUB5E66tK6fG0tw%2BfNEyciWhUyw2rnwESHOR%2BXf5gfqAWHxA7nfOskKjIZMW8CzNZHQNGBn9qMertPVmP7EQJKewnIj86yOVbnFwc&X-Amz-Signature=2c9c518d1676717ae9d6104d5a9c69c12ddbda2da67dabd687de35a5fd3b3302&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JN4HBLB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQCRJ7YNS2WeP4gCHgBFXUkR9mDKeRmLfxFf8p6gkwshEAIhAMZBHrrXICvgjKhm6IUWrJyEkq7QDAlCv7LVHub6CGvNKv8DCCwQABoMNjM3NDIzMTgzODA1Igyjr5EpIKmTeW0By14q3AMA%2F2kBt%2Fc5%2B1W30hc3t3QxS4kh8dCUTa81r%2FjP6htudbDKqw2IAOYBsY0xRabk0Es9ZmJCHiXIYdoeCDu5E89U08814iI12o8T%2BxLwE9X3VIrWdY4YdScnvxA7eVWDYcWkmwkhA9h3X%2FJJpIGpSpD907wmKTjMhPu%2BUPb0xVaT4g6Fm7TQmuxMFGvAbzKi3F%2Fw00lKBZy2i6TbCXIBfeT957HXKyJYMgLt442KmgQEBn73B3Z9P1Nt%2FtC3V3UISMSH6QHBhSkw4C81pCZGL0MdSL4THKRlKvFvqQfwGxFrqhi3B7Bgkqe5hkwirkThvKO2yodmXRQ6zQ0fxvySGYVvlNXnheSd3xjZOhVhaLpMIW2Ug2GJVCjRGl%2Bz%2FwfUv9VrzrnFW7hUWLzOESQYzAOg1C1JoAINMKV8Vdq%2BKy%2BqTSXIMMo6B846XvYeGynCP%2FPmmWzkkiSB5NMyss0qHPFON3PhZiMKdwSFZY3jVwaZ%2BjuSNlCLky2%2Fh%2F8UlfErP10l7%2Bwk%2Fy0xGe6bLUXtgRDITgzM%2BC0MBiHLRLEEi41pjTzmreO1TO6pxnWW8cv8xXpO2%2F1ydap%2BEz2zlEZT78EKWBYcewp2A3ZaEFamIh%2Bwt7Mqb4%2BSGsiY6KCmpTDU5Ye9BjqkAV7WeT23fXkWkr1cPv%2FJvxv8%2BXZc%2BiL7J9rGd3%2BEyooCRPchK%2BZG1vdLWHTdP2EMQ6V1WvHtaWsRtR4AJrOygHAp3na%2FEHOgxAKcBskHw%2FPBxl5b9X7WBEisRIaNVlUQCLFxpcnUvWSnllfU27RYPsQ%2BEu2AxSZkeeVWjshvSaYOF5GMXyVUVB%2BWybf7phR98CiqGHK4LSfcQq0tmWu2Qjs5rsWv&X-Amz-Signature=57a2a612b73d2673c1803eb539b423ec734cf6b3aeb08d9f1040fed54e6e2859&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYRQLK2G%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQCyiMyP%2FZk7ak8M3nlMx%2Fs9qimdrnxBtP28gjGsUILFQwIhAOpv67vwCwFB96Y3gc%2Bsx2WszhF9tf%2FkvszkrJ9nQfTtKv8DCCwQABoMNjM3NDIzMTgzODA1IgzW9ONgGR00cXDe%2BTcq3APTuEWjyi2WUwzKxcZDMeIhcjn1SNpO2%2FemHW5fcyJheQe7v8W1weov%2Bp%2BR6uSw06nJqaOw4Cqc4K9HAsGQS3kFW8cJrsznxBxQmfc0sRL15fMEd0OIlIplqPA%2B6e1iEOBFqT0bfgVgfuhseN%2BqPeX%2BlKxu4GdGnpiaXuGSKWWgClEuDsx1l5IYMvfuKIYcTMEnXGT3orrJl4CR4SvJUgpHZSmCOklAGcQI6TRZ%2BqRXhVnHAvGt8%2FH7vKSPDOY5yCWpikIVQHxAWss3pJbwrlU%2B5%2Fw4r0sIv2D%2BuD8ofwU95aN19TP9Kd7mB7NJEMKCXYluv7doMECvA2Rg2GMhKmHMd05rQbEj1wm1aJDelz8JFi6GWLsqg%2BTu%2FVQWYHOQgEZOlTk1NgJXRzYXtQP%2BjDO6MYroAXPruoSYPdQz2B%2F817uMGuddzOk9Png6ojxmZC4Bxp2FHkTdTv1BZvNVN2saiz2J2xYzNJe%2FEUzFZOeKAFUY5XJVIDhXBxOVntqxYp%2BqCSJdhkIY2BywY7JCyP9Zx9%2B8QXbr%2FOUNeUGzWd6Ds5veoRI9gs2ql8r3wGROjLfCZbZ5Cgxw2WDr0v%2Fchqf8e3kt83rILNxM5Kl7U9UIu3u4mpaCQwzhIBk0LTDp5Ye9BjqkAXOEWlI5obKHx4JzwuhsOoDKUAD%2BcyuzGOAG3u2OV46Z9%2B6tLZBp70D8KcunZA8nHlhyNQB3zIrHbQHPdHL4aAgXuTTeRtdV7aqYF%2F9zmPcGU6pKb3%2F13SGS%2F8LqcT1bYDT2RIcLTQepZ9XxnMjDUrncSWnYNOnbjkCaXqltvAYpALwpHN9mLuI0m7K0917kZGbMKjAZzLQnOULv9ppELrFRPIeh&X-Amz-Signature=9da199e577ef306f968f212fd332e7ee7041802804ed054594b9bff64cd48a75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3RNM22W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCICq66fNHHXXE%2FBHMgQWBWDmVpJ7aOhncyu2SD70646h8AiEAyJhOolIUg4ycqXAfKUHqy6l4rbXliafsg76IAHZQ9OQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDEfJkrgljP5NGToCBSrcA2UaEs63zlhrmZS8O7pvS6KschY3d93CUG4aYmKvdjy0Xho6q5ktWr8vBFR%2BolN%2FEbmNcU9yj%2FxrcANVDsC1iOPYdPuOHvQYLpjaC8v8ncQ%2FkT5oDpqDaRxJTkhEfjPTBnMjF1pT73W3h8JPPU7z%2F100Go1DVYd1ishMFh7Sls0NdIKs1uoZoyFuODXiqhzeaTXvcCdWWsqYPkwgVo9AgTwa2VG55AgcNpcTIkcdy2wwYSrCP%2BlPeykbT%2B6N9XGu1hWJUUJH%2FhNLaLZ2a6Q5nGlJl3EBx2FKJ53GsoZbUmwvZjupNEHrbrBQLlMFsA0KH6a1n03UEawBG25oMw8%2F5Sb7UiWuSytmEM4l7A6IrbMjBi2QcebYoLjDklH2pPs2tanFnT47%2Flz9Vgcsc59O8FeLV9uZAC4q6er55reWIwcO%2FfW7WnwuQ2oEQi2PVmbMz%2FG7KqYXAY6BDvf9u5SzKhQaMN6tjp%2Btt4dpbd09TKUI%2B8pLf5WHj%2B%2F9TH2rI1riMSzpi4LlP5Vi2CXQ2UWQli9do9HoUJPB6imMHkiDWEBfCRp5RRqJCM5N6QLYROdZ0wwJiJ72r6mbpzJQqlJ03miwSIE1h4Q7VOWiWEJ5ZMswf0hXwhinhMQjgQf8MJ%2Fmh70GOqUBasAwkpXpY8dhY6hc05shdcdW9gU6j8vsqG5qXohBTEG0gs80SjgsFZcFpNmbWvmoN01bND%2BTltiYFPxH1cxpgG%2BZuFkvUnIOlWlf%2BxQa3q4cwbBwWx2%2FqAzW%2Ffb%2BfmOc9%2BJ6RaOabteEDKqQEtz58I07evIHqoLgG%2BNitOO9VFo0wxMbrxpDOaxq0E98dm5wHowpWwe%2Bvmw5UMlZOkgqp1hmYg5F&X-Amz-Signature=e8d529cf91fa193d322d18aefa35041051493b3f10e773205468d5fba3282420&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X67KU2ZN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCsqbdo2MYH4TUUvANjvErCJ4hXyyPVff54EJo4zrWWlQIgexzhBDFYafii7wk%2FN5SrIed7lfyfKyaaHTkOREDzDVQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDABph%2Bf3bROZx0HK%2FCrcAw73sn85niD7r8TMVvlO46hxQVqkRI3ZpPNk1V%2B6r0YSrdOv97h1TEyr%2FoXNoHvDphscs5DAI9LWurBE4TLdwOz1SCV5IK%2B33FTMvMnwWhGpb%2FSErafuuJnSDwvYuniduH3HV3mnpaRTjBTrhQUtfNafO3E7CFepk6YFhzES8sEVDQZNeoYf3PLMj0R74XZ7iQ%2FVtVupG5pTkIjoCmysuZHY4wzA%2BN2j2vmWfFKaF7jzc2JbSpNTkCXD4swTam4wCFmamRlufsuEOt1jDbgJHYm8MniZ6B4F%2BbGG3cTJpJJ4caRWpFd1nOekOkJt28EPvXCSsG5hcXGIslrlVqndSBLZCedbzpAPbBqhuBvrzIvzjT42TOmyFVIT4f407IbbpXKFFGqG0j8geizuatlv5EQFqx6IBoNeICTvp7eTP1img5xKxGmTow6PDwwwgKetvDqVxVIcQcaWo0%2BGcUKZVEYBG%2FMgv9okNQW%2Fk%2BzkXbcQzjhYLOZd2n74VGArT%2F%2FzC3So3Xm0Wghm%2BXEsIMRN5Ds9waTVjaTizbdGjwcEjW2HNVVZt9GmmbwqfsTTKsmVHApKKJ1t%2FFQduebapzrAAxLrWM6P9aDq5GZ3NR09VyUmZFaRvBCJ2pxBKAbVMOHlh70GOqUBZA5i7gO%2FOkWO0KVUccnRjloDeHda4O6JfpwNlTKPbNtAT2JM0m56oaNQ%2B0fq3UD4lp4FJVlMN276t9TpgOI6pmrnFRlbcsVpyhi23%2FrkONMfF%2BVJuQhlOkGJHgXu8aH8bU7PeOhmD6lq%2Bw2ieRdcZmzXT%2BmFuSWwZJKgGWCbYF%2B9%2BwlWORlo2Ze8p2LJTfUaTeyktZ0piKTVeHZgsQwP1fIm0USn&X-Amz-Signature=7f72b42731fecb8d5d9d7564eba0de37254e6f8a07492ea564277f55c176881a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCAGI3PQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIHQsyMEfG%2FH4pwVBMqzFVLKuwUvxFItf1FQTrAIjDXdCAiBy0kI0VSZb%2BeU2ooTqWJLtqjo3Fa2Dno69ZLXM3AA%2FvSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMwG%2FKqMbbOI8%2BWP1kKtwDqakiLJDnSTHc9gbRkBTtHToOnNPKkLQ2mtAZhOC%2BvFjXQgQ5d9pEoWjYzQGDUTGnA47iW6tVs52VvvJWz6A9b6SyqR7XIXari8rqSclb%2FSJGEFRCuz4S3d135NIxnB6c7z%2FvY7hPsU6Uq8naFiDiIqK8GgSELIaGOflLZuePDI8xILr5%2BA6fH07v09UlFMDcf1PlqEwS3DgItZ%2FNHcG2c0QkQYgIjkms9vjYBB2%2F69d8PMkIOeHhY%2BiqcbRU6BjhDjTJIBWgpYrzip5tSopKEzRQdxTcELZmQh%2BUVDdsfar88H2rd26xk0UnV3W2hS82ulri4sMcEQB7MgI8d6w43cA%2FURG1lBp9bGKcaZqc%2B5f8RWlUAVrrCPgE%2Fb44mmgj4EiC0uO8W91a8LbL3SYnlOBnOt1JnGVuoIvA3cu%2B3v8uhloQ33rK9OEUQ84ud4jiLiFQFoGR%2FR5NdkUnIF0oytzhGSlwvFDy5yosB6yRDMzqJpW%2FAoHlJ0jd8BGRiID0k1xqXLMuLPvDPA12RDRsL4nBHVggTUPrYrDH7AoOOXv3lzt%2FpCmM2XCQSwmZe9Ok7wBmP%2Fu0ZBi6Gz7EV%2FEHaxyX7BsaC5S6Yx0C1RXHW8iZ%2B619TqTeNloy0yQwjOaHvQY6pgGoPXPWtXduxa56E3iFxCXK%2F6LO3yFu%2FSK1Ac4mOSf5W9WTrUQOJnUffOveZUlJVvijQCBEgRL28sFqziUX6GYrUUG%2F8oOGFs9e2T3WyQksnGueVIn4gd%2FcmYGHDGyXDGx3wcopnekAmBhw5uYelzbnZ9KaUUrgTXWVBkyM9HCg911%2FyE4tiuPGFRmeWjCppe1toEOz1Q%2FpnqFwmjUWKzqO7ALg7ioc&X-Amz-Signature=0528ed2d8fa1797e8cce5df4b8f9360c344ccc9f9909ed39fe65e3eb03a2199e&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GEWQFJB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCAXBQLNXjmin1KJKL4QXzWdjxWZNqN34iWX6IOxOaQVAIgE5QrzMfG7RnK40EEATq%2BrJkv34Y1DOeW8H0kxxDJlyQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDFSdUP%2F9I4fJI1op%2FircA2Ku797Jk4uxNKlSm1qnSvzWgzN7mWoc%2BL%2FZfiyawSgWzyhfA5TLUF9208CCA876AS1sYmFOBCeSKh27AgNA%2FNpQVHJP83dBxoE6pzyNRvLy856cWtg%2Bvl5RAmEgksm8XtexGA7YrXhVmQE0IlIYNyc5P%2BOgGHVU%2BupY6FQ7q0RVyK46FviZ0EF4abWDwoEPU6Ve0LfyUnirBtuJYH%2BLWPRQGzT8R11J6UKyJnf8RkxqKwJRh31cjHgw%2BVSMEudI2JmH%2B5zIcig14jSv1wDlc7mAIkdP7hzguXIErbAa5CPx3AkSCiMHqN6oqR0ca5%2BO7OmRsu%2F0QQHm8SIMOb%2B%2F0N9KJ%2F24Vxo4XK%2F%2BXTbfrA0diic%2FeZqjx1Dd%2BM4PfABbvDgamfb2JKCnQXKs%2B41XJFAAzwGWTEJwxR9ksEQbgS5qD%2FryJvLr9%2FfH4MP3RHv9ovu3OfJcU%2FedKlRbf%2BGoXiRPOSY07xAVpx1tOc3%2B3mw6FQhaS1W7nFbNy5FonoYQtc0noXImxMlAS0KAobyhONyqsf03hzdV0DGrLj0u46itIwrR5esNWmNrPVJKh7aqfSEsWD8%2BuuUEGr6Ksm%2B0L7uE1QlJF0swOZWs7FuFPrE%2BqEYP7eEfIwbqgeLZMInmh70GOqUBgXwsKruLDAlrT3TbgCN7YY6Yu5aI5ZH2dIbR%2FJr9DThfNVaWrlqO8Vi8qVS1EAyV%2B0flQfrNDVwZ7EtMmm%2BjR0AqHL5wvaCmimTD7v1fZRTQLf5vUjqc1QfGZgeuR8OrYRdDfizJSZeYbACl3Fn3Wy98M0Lzws1cGRlMmq7OTxXO3pMO2TuHTXqspy%2BovYT3osXjM5KA528%2BbzL5BPtPwWiCz4w8&X-Amz-Signature=a543a40707f058f9cfefb44d7168de59e7788913769d483589f3feabecec7c99&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YGHQ4DC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQCfWAFIODoNjmpCMbrEQ4CcHo6I9bpWcvre5U2O6WcxngIhAMwzw7eN%2ByNLYbtn%2B8brxCT1Mg8xcwmKWtjy97OHF2eRKv8DCCwQABoMNjM3NDIzMTgzODA1IgyrhYp%2FrrM1OmBeKIoq3APyYKR11DAcURpGS7nuPcs9cLpr3hctYN4ZHT8DgHGYX718Dfx3p%2BPOoSR9k6hwNe%2F7Fkzq23T0A6caGdED49Lds7O6EulXFcj6IqpM5jR5de9oJLWLwNZoSE0JWarmMGZiX91E8x2DNVQhVsDQ04uo3FN8NEE4NQ2bYc0X94sWHJLE8N5DRPbnlOBdNT%2BkRSk%2B9cUn2ppYXxmnTtMwcEibz9WxVj%2B1gzzoISC42DU5B0nQPqGHaaYmfhGmxyWXzyvYVvklHkGMoypoG9f2LafVWSMbZMPrDlxG%2BqpBX4R2OiXuwpRdOFUeXXL%2FUJGCXOBi6dkZewkMV6JqsO2xvLHo18PDFLYLvu1hRny51q%2BiFYAFt%2Fn%2Fa5mRMWi8B8%2BoKOOFAt3D%2FRB%2Bq2xMpPFsLHDR3qwFVp4b19FZpvzL7s87c2EUvMinuyn4uO4DqZiESW4AhIChFbWoXxldyrgLOeBSwd5BPvyAxYLSXyn2hbsxsfHjH%2F1JJOpvLOb9OSJnoKD4UthXq9zOYJi7RI40tzLM6cleh6c0va3h%2BPwe189H6eMKUKGD9v%2FJ%2Fbc4wTInzfYg60Ek%2B4Vy2tQNHp5YB8amzHTFpEaxeXogU85lCcRGiKiRSDsaUxBkxFvx7jDH5Ye9BjqkAcUQn4EKHAIg7EPY9pjKFvNWGQcTuQgvt2XbUA2rm5WDj%2FbyFcWKaCrZ1B5wlIDQ1inY%2F7mwx3xZpM6sHjauGvVDWe99h%2BeJVREa%2BqgN8tYTL5iW%2BIKF2Fa64mSQtdcJQBzm%2F7iVmZQXQB%2FF%2BGj7ks7plq4eLqz%2B9Rf3Za4PihPcxP%2BRR6oo2mTsqqfxrCrdUOIjRDTsTDMtFGaB2ZcZuoBC0K7n&X-Amz-Signature=02c2a7b602ccd422145772b7c7d567b6e52be6b119596f6789d0428e0cf52013&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X67KU2ZN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCsqbdo2MYH4TUUvANjvErCJ4hXyyPVff54EJo4zrWWlQIgexzhBDFYafii7wk%2FN5SrIed7lfyfKyaaHTkOREDzDVQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDABph%2Bf3bROZx0HK%2FCrcAw73sn85niD7r8TMVvlO46hxQVqkRI3ZpPNk1V%2B6r0YSrdOv97h1TEyr%2FoXNoHvDphscs5DAI9LWurBE4TLdwOz1SCV5IK%2B33FTMvMnwWhGpb%2FSErafuuJnSDwvYuniduH3HV3mnpaRTjBTrhQUtfNafO3E7CFepk6YFhzES8sEVDQZNeoYf3PLMj0R74XZ7iQ%2FVtVupG5pTkIjoCmysuZHY4wzA%2BN2j2vmWfFKaF7jzc2JbSpNTkCXD4swTam4wCFmamRlufsuEOt1jDbgJHYm8MniZ6B4F%2BbGG3cTJpJJ4caRWpFd1nOekOkJt28EPvXCSsG5hcXGIslrlVqndSBLZCedbzpAPbBqhuBvrzIvzjT42TOmyFVIT4f407IbbpXKFFGqG0j8geizuatlv5EQFqx6IBoNeICTvp7eTP1img5xKxGmTow6PDwwwgKetvDqVxVIcQcaWo0%2BGcUKZVEYBG%2FMgv9okNQW%2Fk%2BzkXbcQzjhYLOZd2n74VGArT%2F%2FzC3So3Xm0Wghm%2BXEsIMRN5Ds9waTVjaTizbdGjwcEjW2HNVVZt9GmmbwqfsTTKsmVHApKKJ1t%2FFQduebapzrAAxLrWM6P9aDq5GZ3NR09VyUmZFaRvBCJ2pxBKAbVMOHlh70GOqUBZA5i7gO%2FOkWO0KVUccnRjloDeHda4O6JfpwNlTKPbNtAT2JM0m56oaNQ%2B0fq3UD4lp4FJVlMN276t9TpgOI6pmrnFRlbcsVpyhi23%2FrkONMfF%2BVJuQhlOkGJHgXu8aH8bU7PeOhmD6lq%2Bw2ieRdcZmzXT%2BmFuSWwZJKgGWCbYF%2B9%2BwlWORlo2Ze8p2LJTfUaTeyktZ0piKTVeHZgsQwP1fIm0USn&X-Amz-Signature=e0be076301092237ed4ff2d3a150291c4a17a9418a2b898ddedaede830976ed6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YL2QXQMM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCICc2EfQfULQ9zGW1EA7zENtZm9dB86ZvgIfS%2Flq9jb85AiEA5%2FJtE7RiAWiYJ%2FEDQrxfRaLW%2Fj3Y8Ij4Ia7HPWxZt5Iq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDMTnzWZzS7StvqrgQircA9U%2BPa2Ofw4g7eOm69M4TGor9bEYL%2F3d808I0HfmZlx6IahJzfkN8BCLMKyjkh%2FExdtWVNFcMkNWN%2BupZQ4Vx7VNHhxIzfxoY30c5AMm8LLBvnLLpG5Q4QVTMHK%2B%2BmS%2FOvCEO71odNAsxyKe9tmrcfbmglUeHY%2FZsx8zoLc9SEfh8L4YKLhYSV7liKv7ue3hTa5RoiInujf6CKNm8cZxhNxkgl6dLhIAhc%2BdErPNgpR9jiR9U9XDAVnIax6mqJDko23e4SLy%2F8Va%2F3vPtj0t3aDWqbcY0Z7%2FXqPmlGevHD5%2FMfNugLKYSZJ5cN8AVmJWPhx3odFHOwd5D5EkyLgIoYVH7CmSkA8Sv1RJ%2Fr8wBRVbDFqugvzkiZDEMOAQn1ES%2B6H7fSQIBzgLjuluCNd6dzs%2B7CtT7fLdQLOLrqMdICkLLlpowaMP6Gf07kSJBhrJM6niYMMOdEPohFs3fBGZL12%2BqhN7%2BXpml71UK1Wnt6cZnQru3CJcyotkmZ4FB%2BBia%2FrEgT7JbP9i%2F5g8rabZ%2BSKp4d7YjH%2BgixTTo1hncBrIYXt0h0EF2Z744%2FDd1IfQyMI58cP3Y9wUYpNK5LXP8j10YLcW0mJXqcgOrdg7wFutgsnsnbA1Z6vv%2BcEWMMrlh70GOqUBuFUq%2FQHWGmAKEjSztfhZ04SSBdPS98GIPrelUOdX0F8GDCzPCpQVgnRqvpVNR4oJTQGJsgf%2BJo8s0ToAvlXFFHBRb9IGm46s6blgFcoW7VHFuJgxBSg004j8NQ5g%2B4pGH9vhB3YggaZ3BOFlwcfxc7qACReCgfvz9GH6cRO7LKOnDgp1SB8gr44EwxZcmd5PBGQPIi1LifOQNfl7%2BeCl1gG37xRZ&X-Amz-Signature=d357852f0b7f2d0657b7bc093a4ad2d4f073abf1dad6481ee12bb4036c57502b&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YL2QXQMM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCICc2EfQfULQ9zGW1EA7zENtZm9dB86ZvgIfS%2Flq9jb85AiEA5%2FJtE7RiAWiYJ%2FEDQrxfRaLW%2Fj3Y8Ij4Ia7HPWxZt5Iq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDMTnzWZzS7StvqrgQircA9U%2BPa2Ofw4g7eOm69M4TGor9bEYL%2F3d808I0HfmZlx6IahJzfkN8BCLMKyjkh%2FExdtWVNFcMkNWN%2BupZQ4Vx7VNHhxIzfxoY30c5AMm8LLBvnLLpG5Q4QVTMHK%2B%2BmS%2FOvCEO71odNAsxyKe9tmrcfbmglUeHY%2FZsx8zoLc9SEfh8L4YKLhYSV7liKv7ue3hTa5RoiInujf6CKNm8cZxhNxkgl6dLhIAhc%2BdErPNgpR9jiR9U9XDAVnIax6mqJDko23e4SLy%2F8Va%2F3vPtj0t3aDWqbcY0Z7%2FXqPmlGevHD5%2FMfNugLKYSZJ5cN8AVmJWPhx3odFHOwd5D5EkyLgIoYVH7CmSkA8Sv1RJ%2Fr8wBRVbDFqugvzkiZDEMOAQn1ES%2B6H7fSQIBzgLjuluCNd6dzs%2B7CtT7fLdQLOLrqMdICkLLlpowaMP6Gf07kSJBhrJM6niYMMOdEPohFs3fBGZL12%2BqhN7%2BXpml71UK1Wnt6cZnQru3CJcyotkmZ4FB%2BBia%2FrEgT7JbP9i%2F5g8rabZ%2BSKp4d7YjH%2BgixTTo1hncBrIYXt0h0EF2Z744%2FDd1IfQyMI58cP3Y9wUYpNK5LXP8j10YLcW0mJXqcgOrdg7wFutgsnsnbA1Z6vv%2BcEWMMrlh70GOqUBuFUq%2FQHWGmAKEjSztfhZ04SSBdPS98GIPrelUOdX0F8GDCzPCpQVgnRqvpVNR4oJTQGJsgf%2BJo8s0ToAvlXFFHBRb9IGm46s6blgFcoW7VHFuJgxBSg004j8NQ5g%2B4pGH9vhB3YggaZ3BOFlwcfxc7qACReCgfvz9GH6cRO7LKOnDgp1SB8gr44EwxZcmd5PBGQPIi1LifOQNfl7%2BeCl1gG37xRZ&X-Amz-Signature=fb5018c56b6822c3aede2a5b127dbca6eb8219f60bb0f25f42111c9455a5b134&X-Amz-SignedHeaders=host&x-id=GetObject)
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