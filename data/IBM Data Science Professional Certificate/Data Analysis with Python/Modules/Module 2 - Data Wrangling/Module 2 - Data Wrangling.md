

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NQG26J4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCkxthbA0uNxInPqbSlnQGWFdD3T1LcB4%2Fg3xMbFAnS9AIgdrT8lRWBvzjC9PHNzB0qLSOvIuONIZQcBfnMkZTLjn8q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDKOd2J%2BQ5nTWTz4pKyrcA0%2FkHNGFTJ5xMzTo7zsDp6BBpFmpuAWxWo0zkbRaB%2B5YtztjQzG2H8qktg2XYE3DT4DQJFiXMP8IIAQa5%2FxVWdGrmpjQRZSKSHIAx9fW1jPi6dPEDzePDQ1ax54weKON5aSssWSpumI4T8JtN24IJ9JhTcqOf%2Ff3svqs35MRmi2IpRGokM%2F1p5lfIy%2BGq%2FZ57JRnDilRm00QcwoA8THN9TxgLNkW4y6naXkUeid2ThXStH5S3Exwn0uHuYDVbweiROguZJ%2BpkCmh2nu4GOMb92vP%2BJHGpSo%2BthusXpf5vxr2m3tx3YWU4rkPVoJWXhOLE9RwdqkmbeLKGyjQudPx1aDke%2BFtNGsrdyDesl8%2FSFilLwNjb451jk7HaVds2NpZnoGMxFCKjXtuqpudLTSIDh8iqs6BQdy6m1JBlQXacVn2PfGBXIMfV9bonF59PoutwKuOQJNDLFKaiSydC7MFRU0VJ0cgKfP1LvYKvngyGhzzFaSN021fa0obVxU9kR54BL8qlQ7oG6ZJ%2FI0u1AGj2qPghVOMiR0Y9fyPL66t5s5wAKDcaFINu26ttTju4n%2B8q3pE2ogrrJtD0hQWy9AypAhhWwDWi0tPzZj3QNNYvwoeKMgGbZG4P%2BCz8E%2FiMOeKjb0GOqUB%2FdkqafXLLJ5jqc5xdkQ0ci73R9lNqkzLTiHrPFPyq72bNMCioQ5wuldwA2rsw%2Bq3G88nPt7pG3PA3ZDg1m2J0qxlJNjDcv%2B3iANtCPrM51cdr47y1pTYQ2Ihvt5onEd5M0HfxBkxmL%2BCmbV5D1WS7I50Jhm4jiySVZeCch0pKJYVudH5HTHjZWaJW0DrZNveq3sqED%2FSU6QRN3s9n0AFJqE5NAM2&X-Amz-Signature=8b27e52eb726316159aa83df5b14e50e8f8f68b2fc0bfd7999a89d83a0ca25d5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VMM6TQX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD9IQOMg2V4CS3FQEXMX63msELM9r701DYqbGBTRyqWMgIhAO9UmHfxV6BLRzLvotH9v3%2BG4dU7FFOmn8D2j%2Fg%2Fa11hKv8DCEQQABoMNjM3NDIzMTgzODA1IgyAH%2FQeoYWhHgfor%2BQq3AMD%2BRzXg7Y5taBqtZ235r9iGwF57vtNK6iZ0penM4HHUzsFjbkfvgPLQT%2BcpMdMhbU6Kzj8h93vCH2eXq%2Fq%2FQ%2BTBlHys1U3oeYgczrlcqVxEOKw6IwJMWAgx88GZcIGP00n8fk3Sa7jfHS%2BTgQKQOiP3P2rWEG7bh7GLSgCHohCEqoH59U1AAdKhk5wv1WCU4qtFTE0ecnbozcY%2FWRArKRTtrt19JtmwE8JeR6m6AcSEmfz3dG5Awhf6eWgEVYGA4tENh60ThJHoW8vm7MKg8xCC5NzqORnJT0TFyAYWQEcN%2B%2F7TuZo2jUlDjvZX7xwLOjKmGKE2y7FBQ2K8YeDG1uC6qk0COpwP8ULZno08BKZcF9fLbG6wDqsoQLQ3o0tph5%2FC643z3vrxVrGemvd%2BodN%2BuFtAanhVG090h2lyDvSLNuqxA9L48VxZ99QKc0QmkEZvpYSh0NxzXlumfO8Bo4fpxTYeGqMSVTcFsc3KDEsW8b24r99f2K48HKu79a%2FHu3lbo439tfAdyNGRFmVu8Wv%2FZjQRo5l0jTVoNcu5Cza2chhk76wHbitIpeFSCtT3XrTJlylHyTjyMjsf8WdqT731SqWkWTo39jVqkdZqpVq9LCkiCKKBUvyy%2BXubTDvio29BjqkAaWtq10vXb7KoO%2B7K05h3WfTKjCBKWWFuPTlhAhlRL4r6puesIyp2JAIq%2F8nTLOmIzMMYP52RA6WkeixgwUhoKDFSJj4KgW4dv0TSiepf5XCA87qXxgN9duCJtI0DHCusQ7rxiq7RRCwA9cJCLIhcU%2BpZ4bsBPpv7LQs2V0%2FOBH29xRhh%2Bsy20SwZkEe%2BRvdjxLZTE%2FPqCzqhp0%2FcYlWW7RueTuy&X-Amz-Signature=08b0b879ad90024664136e21e968db44878abbe3eabd854d457dc6664b67d754&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD6HIACI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCDNfYy1leNB2EZ9mDWAOWG%2F4PlbFAv1%2Fj2nxOgBhBXdgIhAIwNejBJmOdQ06%2FDOHZZJZLvN3RC%2Brr%2BrZF%2BKOfCK5eEKv8DCEQQABoMNjM3NDIzMTgzODA1IgzsUS%2FlFyC3KJS5EMYq3AN2ehv7Xo16SETji77p9QtbAcqKbtgtdzEBiM1rhMoAK%2F515mUF%2BzsFzO0gmDLC3125cjeXVmm5MY9Vk2v6y2cbkVyV6vGV6u0lGi7bT73Fcqs6XR%2FfuYgXAsHXqirHkMvTy55DUyAUW7muGrdF6Q7Og4zORzkUlR6iZArNrFo4rNtZ1y3NcrKhO8IibDWuyOmt5zmex%2Bciq9MwwxXwRAYjGTHUT6lYUfhnwFu5ZBhnIHPOOiQuh0J2aMtMNwwKj3sinobjDDf41gu690PB2ORxzXiv6XKHKnt6vaas%2BZ2Ph%2F8F5NrDuR7fYhsgd%2BNg0hujO4m%2B2KlrTUQi1WMHBhy93bnwgfXAT4kKRVf3Iu%2BzVDa7pXaCug0CJ5sv1uIb9KS3Bp6aGGc8G668r5FMz3J1x%2B7kMkSL7ydtmrb3DoqKmdsLN5QMrby3a7UA80DBa7ckAJGckBZjf7tv190yDJvoWFiZs9Tkzno2NfwYx2ov%2F5IapVFSE8HWzfPXBuoAzToGh6r820g%2Fjp3Z%2BpMsqeyL6%2FiKiqIKPNM6yf8uiHug7y0tiOdJKlWzX%2BDQQCOHq3oArde4rQSuxm%2B1Bd5gDA3zj6GgNjalf0VJE6%2Bif0%2B96f2HIEOCeHGfiHXNWjCsi429BjqkARNp80rmO%2FhP%2F27i9yaA6a6lGSITzraIGZqjK5l07UgvyfCmDJ2dJli1VPLnS9bA8cYmJUrAh%2BpleKXx0W4TaTxeaBoV1Kixb8Ue4ryphCAZ%2BB9hn%2Bsak125ChJwy1pgZABkBDB6a%2B0rhOHXz0O0I%2BwLZ93vSdmaUJxLU111YY9hkin2LaIkxWWkuCojOkKfc8p9KH6oXDAx4W9zqyevnS26L17F&X-Amz-Signature=fc2602d4d23c4250186ac8e8a1649dafdcc338d62d575c8e4df3527092b68f1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=f04bcd601899a2e0935c038bbb372d765194aef4a7f476285e195c79cffd801f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCFSBHXU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCOXQO8%2Bc0GTDgk6Iu7nkf49afVy2HX3x72DtVJgZHVIQIgIYJQRGC4s94Ghzo7yH8D03h67Avd3Fe3L1VNC7Cz7fIq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDEsguRXEhccPtMyWKSrcAzQ%2F8rbAJdKILore%2BPoyjwHBehMsatZc7JcHIRWH%2Bl%2FdEEfBJ%2FjMt9lpViL9LRk7KI%2F3QBMAPm6vOrLVFD0tOTDX8ESK90VybSOagKT3bSOqTr3xERiGq6hehAVY%2BwH%2BlAoFNH4%2FYr84jOwjo%2Fpw1q3Dn7VvPUwWGDjql7jhVLf9V3OkB0rhH3NajcMyiWu8N2FOGRJiC9JhI7bD7IUJh3QY6RTMBCS8Xq8Z6qxUEJbRnDw%2FCu7jedVg00Pkjgg3%2BKNZ5BFJK0b3VJiOJ1JPMV86ziy7l1%2Bin%2BEP7e%2FsaKcK3vkPhtG64xftQ4kF8n62tCwWRQbJUIMo1%2FJhJvd3dO8l2Mlyk0Ybce50xqx%2FS7%2B57D%2BoMA%2BOb3SxgAMKdR6zc0aHuNNCTrC0q04KJoyZnj9axS%2F9bMxnSnmI6%2BXg2uOTQzgH5T7X6tKsL4Wbguu4sux852Wy7bWxIgSpzhj9WJMbSkgMef9eP3WJImGqnhd8x1ADiywkO7A58G%2Bf52Nr7q0t9f6kZfvImcw%2F3Lr53TbJVPLHX58SI6UJK2qITjpeTQSsyTU323jD9njwfU0xGZ6AjChOBhqwK2FrEStC4EH6FX2fwZQTyr7mOwXbF3TcN6vJ85YN4KLrfRKKMPSLjb0GOqUBcC28kUpSUdXOxVCauj1bapVfYSGfYCvQ3SrkYNtXG2MLOse%2FsvRhNWyyAhmaDZaMYoMRSbtDW6tMfYUK1psZbeh%2FW7h144FvMxdqeKAueTrHci%2B4kBO89BLQ5bpt22Qgm%2BqTGKIh9quBn6PnfLP8hEgxeMft3GaUoeJ6AcdN6Wb2lZJRNAIUYz%2FOEMVTb3dvE10JvKwIt4Y6qxAwpMFdZtNRZ1kp&X-Amz-Signature=ea76d579131c18bb882a5d72b3beb79a51218f31381afd3f6507abd260ff58db&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDAERVVD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDWqR%2Fi6DhZYaCMWUzYp%2BohUMkYcimSouFk30cnUCrWYwIgK%2B8DSlAT8mt9T1VUKAaydCHWpk4mxw%2FPetTOlax%2Bp90q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDIAR9UOfmkS7ZjxowSrcA2NV6ncD25T3pe2som9O4rSMIlKdmMEwSDQtzDY839bbC1yOSDTteNBM1ENmuNIub1Q7EYeY3Mtk5pjjDyM%2FVK72bLY8N6cwskxxTm%2B%2BigT9gzFm3RZsLsfd4vSn9bYbDpEhww2efQSzUhx1cEBZmqBuVhMM6k%2FEnB0UHcnOqM1q%2F7m1IHekdtKplJjb364MVV2NZmVZ0%2B6F8Uycz8DACY132hZCncgcRcR9cq6Ju%2FgZ03d198SF01KI3Re49UIBDfMbN000jYJJMJJISjUIcilCEq%2FAkGw5M0O08Urpp7e35c2%2F3FZEZE29Kwcb6WhRg%2Fj7w9ZcPw86Ltk8toyMvuflXKJzko240mNFk3GtBSXF9jg3KQ1nVcxJ41%2F1m6KE5zrUJexuKaDfuBM8EGxivlhTHHA%2BwPt88j7nKBZn2jxo8mu85UMPZaK6OSWBj8R%2FimGO3TpdTN4xrfXs4%2BNC0VAwMkyXmvKBhpcIblXuFkFNGKR%2F8leNRFHeQ3Znezv0mnD3MXB936r6TAt1xzHzW%2Fa8fKZK2LLtqifCjHCT%2BG5bmnjkYcbGYPhHVIXqBqvzkhjYrFzNYmGhWEH1o1kexAwP9MyV%2B4Ej5LuyKgMEn2XX7pIhNzKCm39MSqa%2FMJSLjb0GOqUBSTixlYpVHhLfppGnFPM%2B52A%2FE4tPXkjGdXabL8LbixhyqghWZNyfP2pUOUEjrxsJcGjq6ZPOEul5Z0ywj3k7UZLYaT6w3iJtjgb%2FV5AV1KABssxEJkzUfs8zrNV3le%2B4nhltzFNw37MD8ljt%2Bghe%2FrkC0d1ErWPaOV63gE5GOSqQP9log8AVRz4muRl1F0xd2AnjjhkqknvZhR85nQIqnDb4by55&X-Amz-Signature=f1cf0d54eabc7d8666f70a9d9a93f31c07fd85ca453a4891ad781bdc9bdfa8da&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M7NHOFW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDzIccq3YiKiBs7SpKPzsCGO4hKQ%2ByLElVCSITunGM64gIgQ2IoHmqg1dW6Metp9nciV6SuWVIzUXbiv7Dlm2QG3g8q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE%2F6CbRuaZdaoaUCaircAwRl0u8f9WtPlgaAtemTOaseKJrRlEdF%2BuKNaX%2BxaEg3lm%2Bx8TVOKP%2FzQrcVjd4GG06zVCyPhBYvw5hE%2B49HoiJXq3Ycb5ro9f2rFDUC%2BkFoYixE2dMEpiOPYO9V6xn5RfKfNoNDu4FKmy%2By1SCAaYQIhrDekwPomKRTwI3EZt4jtzzeJc8kaxFjyCHpWuUEGHXIGuU4%2B86yRuPb2JpuTalJttd0mkiUnoAOaWK5u7mwMrb3dAGhjWbu3HsQbx4LhS1OuDB1gTrEx7UDEFOaYanF%2BRXTC1i%2FGFCGq1xkFKRDRPg%2B27H0t4u%2FSINbGlAqenviBKYDre1joL5amHI5z9NsRLIl8Zx8FVP3wsUSkPotRJspA9VMTEijqQt9iOn56TZZOqzDyOY7VwWwTwE7KiVdi9jHZtFcHl8jbzs45yIiL1zG397lpy0%2FEpvqKpVGR%2F607Ji4a4u86TxlHb8qdPuq%2BpsZp04IbdQVDMzq4PmmKZSjeWTPpmKvf9pguDRTGeB4mICC0YZqqWhphL%2B1wJYDq1hFdximed4eIsbECcSsQFUjdbUo%2FPAQ%2FZgVyYLqgHOlVd8kGHa%2BUbcVzXhXpE%2Fmy85botS8PSyF0yBA%2FIHD0zWCN4q8fHfgrnzQMI6Ljb0GOqUBuwFqhm8cP2i%2Ba%2B9EqTr6fdzHtA5CH4whaOdbe7%2BlWyx5zQirD1J%2F9Gy9QrgFgdrPHzKzMVjrtJXkG5l5Y5Msm5%2BdG4z2NNosIEW9ahIn354Lz0NMW2X1Qx21cth3RZTZ4aTbRpfPytSnBX%2BAye3%2F6r4LB0a17camfD7eIp%2F3qLesCS9E%2B32mr7hiyXS4luvRcfZ4KOFTOR0aM4JKPj0teclz%2BZGt&X-Amz-Signature=a4ef88e269a8bec3fddb2c2bb44e2fa188b9131313960819e1da336289882729&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LY7MPWI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIGWwy4HmzWHtY2FooScV3o8xMHbBFA20xkIz4zdsfCD4AiBKin7S2zSK0oDAJv5ni300CxfDgEBkupzAAdrmNaQjkCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMzwYprTqTEbyObYEzKtwDLoCQdsDUoD1Xbwl7YKXl%2B%2BQLdcktLqeVwhYb%2FZFFo02089HfVHpgxrX9eF27m29QhXHogMsxUm6evT0vHfUGO1CoPJLEUoRACgfDLzXOc6B1omxpDKSH5WlumMBe9koZbznKT3gNEzd8Bi9F6d%2Fz7lXtQRiLHc5egqbiRECxx7KK%2FYticpGkwo3R17z75KDXBPjJa4DRF9NpTkIcVPXQM3%2BcNWrnq2ECfTKrrqwtVho8Fyenq4tFWD4JtM9fo%2FBljB8IHu2CL9sj2RrpEJv8czqfmZfrtvZghyZUK2P2b%2FjA55elqaMQsspjXTIetRFxaTU%2FKjpv%2BPkXuPY9ZhjF1n5OfGPQkRLcHuRcqQRlgmk2x%2BOG6%2FDctYDmXw6Slc5%2FQKY5%2Fxs360fapTfWbVuCueIfqJdXvYVuCLfFUV8r%2Bf7Hvfqu%2Fc5mPCn6gD83vyHTKMvKYtvRyUB3aGyMwYT7OTMmWgYvzNF1xB5%2FfPyFSRylEfnfeVzIi7dwzTr6ql%2BmHB65kkgLQgPVwG1hbjF%2Fhj5RkXeLV880dC%2FoIbqBBU%2FqVtoiXbNFgQ7%2BX%2Fd0jujX26p1NbtWz6mgGhWnuQ7Atad5SYmOffJEU9PsuNP2VpV%2BLfPP8PvfT1xZn8gw84qNvQY6pgGcyEXvqklsEDHwX6Ahw5OVHNOzRQlKLHHM3PXR%2FCSbLnM3kFeqn0Xu29eY43hsaCJmDZf2bkVDgPacvkAnRK1RUamPgUsWDAPiTkCtmEgPZPRmOc6TFkrrevmxucUeIm%2BqXdWXuOg6eBjjtf5YvAi2LSQdgEdL4EM17enSjkwn3Y8GVLhzN9yI13EAP47OD0CUQ0tKT8%2Bdcv1vBKPpf52LQ8hqx4L7&X-Amz-Signature=4f76ce944e7c1592c251c209f576029f89a52ca4f1abfe0002e7f3c36c0b30a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCFSBHXU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCOXQO8%2Bc0GTDgk6Iu7nkf49afVy2HX3x72DtVJgZHVIQIgIYJQRGC4s94Ghzo7yH8D03h67Avd3Fe3L1VNC7Cz7fIq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDEsguRXEhccPtMyWKSrcAzQ%2F8rbAJdKILore%2BPoyjwHBehMsatZc7JcHIRWH%2Bl%2FdEEfBJ%2FjMt9lpViL9LRk7KI%2F3QBMAPm6vOrLVFD0tOTDX8ESK90VybSOagKT3bSOqTr3xERiGq6hehAVY%2BwH%2BlAoFNH4%2FYr84jOwjo%2Fpw1q3Dn7VvPUwWGDjql7jhVLf9V3OkB0rhH3NajcMyiWu8N2FOGRJiC9JhI7bD7IUJh3QY6RTMBCS8Xq8Z6qxUEJbRnDw%2FCu7jedVg00Pkjgg3%2BKNZ5BFJK0b3VJiOJ1JPMV86ziy7l1%2Bin%2BEP7e%2FsaKcK3vkPhtG64xftQ4kF8n62tCwWRQbJUIMo1%2FJhJvd3dO8l2Mlyk0Ybce50xqx%2FS7%2B57D%2BoMA%2BOb3SxgAMKdR6zc0aHuNNCTrC0q04KJoyZnj9axS%2F9bMxnSnmI6%2BXg2uOTQzgH5T7X6tKsL4Wbguu4sux852Wy7bWxIgSpzhj9WJMbSkgMef9eP3WJImGqnhd8x1ADiywkO7A58G%2Bf52Nr7q0t9f6kZfvImcw%2F3Lr53TbJVPLHX58SI6UJK2qITjpeTQSsyTU323jD9njwfU0xGZ6AjChOBhqwK2FrEStC4EH6FX2fwZQTyr7mOwXbF3TcN6vJ85YN4KLrfRKKMPSLjb0GOqUBcC28kUpSUdXOxVCauj1bapVfYSGfYCvQ3SrkYNtXG2MLOse%2FsvRhNWyyAhmaDZaMYoMRSbtDW6tMfYUK1psZbeh%2FW7h144FvMxdqeKAueTrHci%2B4kBO89BLQ5bpt22Qgm%2BqTGKIh9quBn6PnfLP8hEgxeMft3GaUoeJ6AcdN6Wb2lZJRNAIUYz%2FOEMVTb3dvE10JvKwIt4Y6qxAwpMFdZtNRZ1kp&X-Amz-Signature=6205f4c15a3ca8b5e84c2f3db7a9ba960749fc2321ff48100f120b751849b736&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJ23WNYX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCdKKap5z8joKJITb8o1xQ7O6QtXdFlcTw8lUapfcCo3wIhAMy7N9t3OHZ3AQ4%2BLMPISFGPXI%2BzPbH8YDzOYgWiqh0tKv8DCEQQABoMNjM3NDIzMTgzODA1IgwX1diaLay2xEsPmEcq3APvlQqfadJ7fevI204RsAkDWk83hdkQeOk807WTybT9ohlXnpqD9pGw58x78%2Bx3dKU%2Fb0edygu2VFyhXrbNX6KsibWfzRZcPzP6g1xqlKMVjyouOx5T6NlH2ZDsfLpE7NhRjgJcV9qxLDRi1uNmtXNjO9QfRV3wEmbRq4Yku6tYaa3HaCi%2BTRdobyh6pyKbs0ok87uy1bTS0yeag6q54Es%2FXmVdM0hx%2FD1Z99h3W2hoAKCbPd8Ul1rkOJ8qrYT3Dy%2BOr%2F6cVQXadRjab2hz3BjsDbqI5zeHWek%2BQ70eU0WuMgcKXxjnfW5AHgKcS2NPiyf%2BZPPmV7p3IZU4xuNoWB7QoD4AdcrCaOIaEoXhZ0RV6fWMIjDdGQ2pPyYdognBBUjKroDs1Tf%2BzM75E6aYwIhMxEY0CWqB7tkAIJ63BFDswJK770OOLYYCfOjAccodKCrSoirhAt5fqgAdQ1WBALc0s4H%2BX6EA4G6CpaeMulpQzgZpAubTbbMfnftmqWEcIxy1C9Tr%2BKxu%2BUnfUFjOfbugRY7SxCYWTh5UBHL%2FfN%2F5nMjS3Dbf3hRw88hodQuVEQrvDTg58MXstNOrfOoYg6xNCPkhMI0XjfWV%2BaCiIQFAPiZhC9BNrlGqVSCyJjDQi429BjqkAa8bdP%2Fqfogh8VtdOtJhBpOGHmozamY2GUSKuaCQnUG1J2fp0oczSg%2BulffCrB%2FA3c1A0QshA560EphUFnYrred4jH0qb4p61WtOq%2FWaD1kXk3AcxUYxY3NTtyt9hSqD0k1mi67M8n6Don9lI0eyI4XQVt4tGhYyCxuLDBe%2B5APhPbX8wr%2FDKYD0n97RzSElzBq9ZNa2%2FMdJUoy6h8vbubHE0cBH&X-Amz-Signature=6e61138e71f06ff1da238ad847c3889fbf93c449430d5385ea71ca827fcb4978&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJ23WNYX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCdKKap5z8joKJITb8o1xQ7O6QtXdFlcTw8lUapfcCo3wIhAMy7N9t3OHZ3AQ4%2BLMPISFGPXI%2BzPbH8YDzOYgWiqh0tKv8DCEQQABoMNjM3NDIzMTgzODA1IgwX1diaLay2xEsPmEcq3APvlQqfadJ7fevI204RsAkDWk83hdkQeOk807WTybT9ohlXnpqD9pGw58x78%2Bx3dKU%2Fb0edygu2VFyhXrbNX6KsibWfzRZcPzP6g1xqlKMVjyouOx5T6NlH2ZDsfLpE7NhRjgJcV9qxLDRi1uNmtXNjO9QfRV3wEmbRq4Yku6tYaa3HaCi%2BTRdobyh6pyKbs0ok87uy1bTS0yeag6q54Es%2FXmVdM0hx%2FD1Z99h3W2hoAKCbPd8Ul1rkOJ8qrYT3Dy%2BOr%2F6cVQXadRjab2hz3BjsDbqI5zeHWek%2BQ70eU0WuMgcKXxjnfW5AHgKcS2NPiyf%2BZPPmV7p3IZU4xuNoWB7QoD4AdcrCaOIaEoXhZ0RV6fWMIjDdGQ2pPyYdognBBUjKroDs1Tf%2BzM75E6aYwIhMxEY0CWqB7tkAIJ63BFDswJK770OOLYYCfOjAccodKCrSoirhAt5fqgAdQ1WBALc0s4H%2BX6EA4G6CpaeMulpQzgZpAubTbbMfnftmqWEcIxy1C9Tr%2BKxu%2BUnfUFjOfbugRY7SxCYWTh5UBHL%2FfN%2F5nMjS3Dbf3hRw88hodQuVEQrvDTg58MXstNOrfOoYg6xNCPkhMI0XjfWV%2BaCiIQFAPiZhC9BNrlGqVSCyJjDQi429BjqkAa8bdP%2Fqfogh8VtdOtJhBpOGHmozamY2GUSKuaCQnUG1J2fp0oczSg%2BulffCrB%2FA3c1A0QshA560EphUFnYrred4jH0qb4p61WtOq%2FWaD1kXk3AcxUYxY3NTtyt9hSqD0k1mi67M8n6Don9lI0eyI4XQVt4tGhYyCxuLDBe%2B5APhPbX8wr%2FDKYD0n97RzSElzBq9ZNa2%2FMdJUoy6h8vbubHE0cBH&X-Amz-Signature=dd895f432dc5c99b6841471e178576c7367494e1067beb791dbeae372bc1f603&X-Amz-SignedHeaders=host&x-id=GetObject)
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