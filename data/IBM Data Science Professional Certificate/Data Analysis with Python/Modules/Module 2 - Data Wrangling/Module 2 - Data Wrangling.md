

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA334V3O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCID9CHgXqV2AcXWDcfzHExCB7dR5hRURRHUF%2Fj5q8lMhcAiARl%2BM5V8lShRuYLo4L2M5kTIoAdyQ2zjsBeQlh2bYJvCr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIM6QAO%2B2SX%2FfIL7HdaKtwDeKS5FfMw1fU3tilb%2FMVeM1DQgYvT%2F%2B7BIRME9zCVZcoFsdl7MLnrwN%2Bi1ynLtw%2FwPvokoH9yUFkfIQReeMr4%2BepO1N2c4fKHLBZ%2BnLCa2oEUxRK7e8RI2qGzx20A1qVq0Xdwh4qaJ%2Fs9V4beRvMkxBp3l%2Fmf13grWEwT86Ebf5s%2Fo6HfDyv5aHNXCK8lMFw803rb4WlGthDRgqRD%2FnPSPL07GcOrNnSLhvcd9qeuce1TSt9lI4%2FD1U7kOwtiTxQV6OmoP5grHQrHsjh187%2Bx8o47Z%2FYXzVUoLKb%2BYCnjCNCFbtWROsOMoJT6VtplVNpkKdfAYDL3Z6YcegSDgJAKpH%2BfP0v6kouJAiPtA0kPkvoOkGCA7k72QmUEN4WNzV0YH5zwoWW3wxvR%2FCalt4AkL7qBogZ1bVKG4IaEUqqMtEn8J6FOw4nBF69Cfhm6dBKkef2ZG27KF2%2FERvfURsNEcWN0%2BR12wpRqgP11x7CB8SiLlkHPIL1tsET3D%2BUnY1DaqH8dSq6J7c%2FHSPebLJ7aN%2FkfhKvfZqiGB5o39ysDFnudGF1WFNj%2Bbq4rInHxEA8FMd5Xp7gHnpxut4e5nmwlGg%2Fjk7OM9tDJnFqQ6pCal8xl0ZPdziRhO2IDI%2Bow1PmLvQY6pgGk4b9nDUWfFAR9WUt3TS%2F9LR94eaZcHvF6zP%2BqX%2FxADK2TAsqsl5FNwznGzUOk2PUkUa7DsdZynVvGSSzYoP64xhZBYit1JG%2FgT%2FObnNkPkVKtSeNWeROBnPpfpKGtTLHVZunWE0dBiOCBxIxuUKbkoQzSTsniHzKrg%2FQ7M7ldZbwHqu%2BOt%2FElHIKiMX5oY0G9eQEI4sgQ3qVdRoRvH%2BoywDggrN46&X-Amz-Signature=d8a621cd892efd6f7311ed9cd017ec1ce54c7ea6970d3e101b510cc1e5d49a9b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJW3EJAA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIEwM6iqEkkdDKh8N64M4DJgNqsdUkm%2F4xrcA%2BFyoHwKLAiEAtYuvnVRUC2AsbTZxzexbXsp4eYmsrZQ9Wu%2BZjZSPo3Aq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDK%2Br1RQLSqZnIHM0QircA5s8GhMExNyTNcYbTxFPYO0L2%2F1TLz6MEJ7pbGwAtM4lvGdohQMh2IFcVFCV4cwe3%2F8noe28quqiF0FgX%2FxujNKU9JIE1J89tQib1gz1kcE3YWGBlWtmMLSrKUiQ5rrCk4vLtJby%2BD6Yx1qrcFzzMiIcGyKb7SJ1CmLw%2BRTXn1fbSm0B4NpQjbuYX2qYqH9diuzD3eJBw3dE2wqDtKlbHaBGzgB7YroWNTsnAFjLbPn6%2BqT87ve7Rs%2BslEJXeHV17s4JrWULYCSqRCqvm6eTenDTVszG9cwqgxuv0%2Fq4XSTkc70fAAJHzZasmJ2sf5WyEik1YGRX3xDKqlqpHs%2FBqCazO6saipZ2rzNPclm0nf2YRb91c9bCmIYNff%2BVyK8jvqHkA4oONnaYyn9fMQp9Sc5fXr7DGGMJIn8bGX%2B4z7MsdAhgtNd3E34gMWa%2BlhMH4NLJBelBuYApByoZZxIGRMU2HqeYne%2BYlR7bYKXzE78KD%2Bkoer%2B%2FNPdhsl8VeMtywww%2BGCDZpb58iPaZ%2BgRllt67sR8Y%2FSzBASR%2B464ipBDb98bqoGSXzkNSrUyUlKvL3%2B3vn4U5yvNO80uzN3xaRZYGRZ16DEpZ35Ra6SXaZhpB%2FbBNA7jb5Ol8%2F0S4MMP5i70GOqUB9WhO5b1zS%2BFxlhYhmpk9mqO3jx5FC%2FqV9wsTyhj%2BBT%2FYyGvMiMFdcIazguJh0OYUff90Z9b3UDM6n33VEywbXygShggywRuVARAF4%2BqkVftYUM%2B4iq8d%2F3lviymatZzOQVtprxeHH7LOSCiD00RuzZe%2FH4HyD3xhtzlwQ0DYEnADrr4RRmC8vQtJ92Lptj%2BAwwZEoYSp63sXyiT56T7Iu5zIL%2FTN&X-Amz-Signature=ecbfda029b985417a1d7f13a3b0bb77fb736ad1d0dd028ae08cdec52367a6a4f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIG7GKTI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDikiP40tUWFoarNRCGjFoT%2BjjQSrbSbJSYTKu6Ipf%2BcgIgHVNIuzuEjYdJmUwihiI8UhtlUCKfYheRIsBDScACguIq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDL64dY%2BC0ue1IKndeCrcAyunfR78n3ynQEEmsedyyIezup5oFiwgadp6dMzmCzHSstVmNIcfQp0Yg8v70zMci%2BsOeo1%2FJMzqVqAsaobPgdGpnwrISTfwBzVQMOBM5I4S0LjYfn%2BFNGs17AUqyqeS2o7G6UxD9ZcY4Li548gv2WGm8Mn%2Fli7VXxlbMNaAtHgJE0Tc25d9%2F7RMsiWD7oEWh1%2FR45Ta7%2B4s6kUWIdbkWWNn2VHZMObKmRcQyQc3WFzZTPzQziOZi5f9ZOBf7WYDIHWXwxDCtGIY06pPb9DMMnqgoV5f2ndxGAN2gEGvSATetemFVS31QSHio%2BTm1mwMByEnsMi4AgAcJOdYLba3Ifl1a%2Fx%2Fcdd%2BR07kDs0WkmCP2yh82VzZPkL34Qgak5pUbJmOFK0dGuYTAa28AXtzV0vy8gYjvtJt7gz81UJYSeeV906nuFuqmV3lJFOqoR%2FyiYuRIk2Y2vb60QifPp851mgSDAiEQfP6Ifr1yAEG3Yolco9fTe8RTYkdkBhv97VV1x48i2QBCHW0dW6qWdg6rtaQLXsqhrTXPz4WCQxmfPkBlT4TAs8pL3uuy12GLqKfSZxXvsTK9BkQg5bwl29lrmcJ8e54PvMItWQYNM247PHkUWjJ%2B%2FKqAYHGHHWmMLz7i70GOqUBpn1Wfqthsc3CZ8jX4Fv%2BaRVKkvTQ6ulsqi4%2FstZWn%2B4P0udpdi3Y3T0pBFS%2Fv5LXhf55SSvJtYudjN%2BWG98vO4t%2FNJAbwsl%2BV%2FQ4lhYElCWAtk%2B%2FjWGnypkXIUYFUjKLPqc%2FKWDr0k%2FYmkLqb%2BlPJ7EPQkkGR%2B5sse1uuUp%2F97VyYyDE7LO58GOZSKSpQCIePWZ%2BhWIJQekawdnViiQfRnglpoNA&X-Amz-Signature=ac95bd8f2d62104fdcf16f8d77ed92ca0ebe382234616a581d95269b5312800a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIM6IBWN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIFS7%2BQN6bNnXf7YmPzXBxudrI%2BRvHp2v018hELjB2HnxAiBLQeksLXS2odOqBk6g2zXkjXRgHR%2BpWA3DbOSSyZlS0ir%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIM58A78EW93UfONXDPKtwD4tLcrHVfme4kPmPwIlFNZe6aUoyNmcbYZ9OjTSMmnOt%2BPDosezqeH2Hb2iqVr8Jx%2FYPaDMQrSOZLLBo1%2Bqqfk0Azg%2FTpJ%2B%2B2S%2FZ4PWhCDgifDDpMtRwcS1a2LnnyEkW7Fq4mSiygI36oGC67e7mEICDqytQ0ql6y8hnoEEp3ID8hZ%2BKD7yWfHWI%2FfYOHpA%2BAE8veMI4hlNTrqITHsYFUkJzxsHagKI66USuIGRmPRvPyF5TLXUoffs6k34CTFrI3ZCiaUXN3OWIeHL%2FlXd26Qvu%2FcHv2f58zSqUdEeeNNQM2llYaCQQCWUETu4vPYZEo8FjJ0KxSwt27%2BRp56y6m6gA6SNPHYlz1n0f0GicVrpBulOUUuuHupzoTEoCKIzT5FrsVdjDXC97DvMHGFN6AEHMIVYIibSeUtB5Q9WCmbYZm7kSj6jUcjjo0n4muDL8R86UdVAGZGZnwpd1Cbiu%2Bw2sGaaowkPDyg0eb8k7uWXgBpQcH1k3mp9aj%2FjqwzBSWU4ginOSs2Mm4wcNU5QujErQF2UQrCh62XsMM2pwZIv2HP%2B93jNDSHphrcV1dyg4gBomureOg%2FjfTMZ1kpzRQLonokmxSFa4UXCaY3Hcmt403tFkFok8qb4EknM0wqvmLvQY6pgELIOmmvJwaf6C%2BgKPI%2BI8JeT6ecbS3abOK880SrNTdGTihk9apdd9Mpj4vIKpqm8kf9vDHnWsP6FPhmEyi4RNbiwQ1GAO4Ds1QP1qNsaR3tLFtQtbk8AtoIEpxjB3eyl7Dx5QN5rYHuQ33KuVXDJbsOY9%2FylgXRhalP9w%2BrXlcG3V3G0gxL0PVEFWaY%2B4039NceZ0YklBYmbrq1Os1%2Bo0%2FmKDeMp7i&X-Amz-Signature=ae0795856f9feb8a47416a46d0e99671b4565688bc58bea4cc79ddf22cbd3e5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN65W2TK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCeRSChTAR2IsFv3y%2Fj4z%2FG9QEZYUd2qNbXC022IUIZtQIgKmsH4bcjrfh%2FcKUgZsZ3W8zxfrPCuk5WhT1OUDbNRecq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDL2zVAt8FbX%2F7pOcPCrcAzmU38p8yHj4FFjbdakd%2Bkb%2FV4e4ZYPKIiocaTw4511kSGgIlMEA%2FWdS8JJfeRnDcHEPjm%2FZkFPtXQdHesknk6fKW3h%2BM7WewELCpB1zwsmn3x6t%2FHdaf07uWDPMt8%2BFSDeDCSJh5ArHLGXrRj%2BBQx6w7HfpFbMgjbZW6gnoGa2YQb8EhYhQXSfE5vt6w%2FaKvgQ5%2Fg5njpVi4t4yTKMd2Pe1mLA6txeKvDFkdKDGomLVutNCGRjQ5RL2GyZ4iGfA0KXJTEprQIYk8o3mXLvfvIMatoeRoWP102%2FG63Yk0sdX7y%2BnY2IhO3COBig3sSfvwY6onk3dtMfXT%2FF6TyrSs6Hb2MnD6dhkWtOab%2FUhkbSKYv4C7DK5aEfRB2hYtVmQ9Vy1ZWzVF59Gr6nAFD1qSvbM%2BXh7NZuoHsZBbPtdJTWv5yDuPgDJ5tUvEkP%2FzSP3yfeW7ZbjbZJHx1%2BKzBdEc%2BFZFWnoehdPGXn79RLkoFj%2FFeHXqmFp4Qunhgd6L1y%2FgWuqfLQA2fV97E2zWx%2FWoIHi3Riyhz%2ByAABEP9fFo8yyhKLi8mv0wEg9tA%2BKoefnQ2doz6b%2Fk45Z5sbrVOSLn2mzjjoErH5Qth0Zw1RFtxhqDSNdy0nMM7pJJFdFMMv5i70GOqUBlVn4Ptz7Hz96bsWLI4lqual7B1xDI5imAUOQG712EdN7mrL98f6qsfHFDChTxj5t57%2FHAv4tkmzEn3OI8gfwqUxH2BTqMJyeoEOzW6fhC2xwET3S8ADFXwujDIA3xvn1Y4yCJlNg%2FJoBHhj8Bu7bSUi33H9BtPGXd8IvZMJ1NYRKQRwITEGh%2B0AlDiddNpojjWK3FBU06E%2BJkWzxiP2qaEAmWALE&X-Amz-Signature=e07bd86e6e603da9359ce95b7624a68fed8b94df652a6608627ae2e7d23bfcdd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662J2UOQRP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQDeDYANWOQ%2Fl5TLruNcdJJeJHb0iQsEfuBLE6BdHrkn8AIhALHUmDZmJNASthkZsSfvfiWx2g2%2BdZLjqPvhJ0F%2BTUpuKv8DCD8QABoMNjM3NDIzMTgzODA1IgzrpdMYZJ%2FA4dz1XKMq3AMxMfEe3rGBVkqXpZ1iAeoVIAojKoEhuuNJqV8UIeO4bV6C1lOBMNriDHegXzgvzR%2BO3agHN8zn9qSbXeIN%2Bot%2FVDWI4uoS1Aqpj%2FHIWYGF3rrIU0bz2Aug%2BjKBZW1YtcxalXBehK1yycthqcqklG%2BGMlnp8zYjQd8p9fV7qiEgRtlYn8gXt%2FmnrCji5sjkjrN2MVc4l6pyZUe2g9PwuI6%2BC5vZTK5wwwgNz2h9k8FoEFNBy6GaKTSyCWVwFGWom5wIrLclt4SHwkAt5WbN%2Fsg1RmPjkVoGaqTxroE%2By53S%2F7suOshVZCx2sdrtxpb%2BI57BZ1BXn%2FKZmRka3RzzY0yXCnkYey%2FI2uYC7MvuHAsCySwMO7J%2Br4V56vQC1F5v8dbqV15qkbbZp45x7BCrnyxu49CPW%2BIOFoEO97bqbxaqxdflLVN4K0SflwD5QFzFDUl2%2F%2FG4Ev%2BQ%2BaZI27BekljDKqVcnLybpp9mRoIy%2B3uTj76T5%2FlVsWbpDEh8u%2F5QuHn7x2D6Siau0QrB0i5M01ibKRPZPnUSGUJ86FKQ9hsII5T%2Fn29p3g5Nwc%2FimZFVoVL5%2BWgAWcErtYKVVrjKxUGs31%2BUf9bKrD0borZacvfuggqCFohxPJncWx95DTCG%2Bou9BjqkAe%2FsCFgPD3%2F5GzxST6jU6dZ586XwD6xQN3nuJFTPwv%2FYiEh61NlDRTx8YgdsefcSZT8q%2BGnv8JLb69RKB3L4oEJjlQuYaHXUe3WHD43HLkHQDNbSrfsfHBOqvMUGfZ1HzoHJwuR%2BKeodCkhWAkIlbOd4IPDOsVzbZp3orwHXOKx5O3TymdRkSGsoZ2fYOkBztu6KKMLxfwWyWOFSWYIBfW2E%2Bhli&X-Amz-Signature=2134e90db8d29291364fcfa6d35b9dec0e89161c5d45f45bd2c6143f5f03b5d7&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWDNWD2C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDMXujwzG02ErWmoj8wdrx0fjeQfMiW3pqHHeLvI4uEKgIgAwQ3jB5pLY9UAPY%2Bn0JJToFb1q%2F%2FpaE8VyTQcDsAhdUq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFzkz%2BlnoBNaIFMz3SrcA5bnrQtgcSSbQGTDzTZ1y1BXO%2BOjZdkCH%2FRapOpsN6%2BDYzxO2uer%2FTC%2BKjOf6kOYN74MCViOHuQ43DvAU2KRtbXeZw%2BuznrRmjsUvY53ZWrOb0yhqEHuhz7ALmSf67KIcWZpFZZ0mMeeswBhW6lZD7m7ThMUcsyLyK1dTq%2FI3K773oMy%2BUVHitelyh0FoHy9zmuyxUCkuzzoOBzaQEGR01xQ6cODjtO49lA%2Fdnsr43OgQmWuYuEdF46aZwvWCGUD3nAim4rELnFcmDoGR12GW0Ywa2VOCeXkCnCf0CuNGrx5N%2FVlobG8jZUeEZI5b54frz8Gx6L9TKQRzrF7MMQOK%2FjXGoMhqHpIC2IWI1RRX5Vmkh4yKYtOjy%2BmwzFlgYJ6%2BRyTPdjqrE9XEgb8hK%2BFgAeEcA5GSNTgkA5m8eVrGrCZNjRIJmKKz9xaTvZwuBUvUZ%2FEanXy8zHwvt5Jcq3NCULLtU8IJYgntEeiLJTlv6d%2FIBoUwDA0G8fbdyMa6jxjauu6m%2BvqJznMEiVCpn7ZEEss7239UHlQ08ETgx6omHg6rrA4A%2B%2FVrh6EHFfA3H3FhNXttEyiBv8ZE7Ssr8j1OGcVSfi7gtKzO7yd7pExKczuiBThmXWRU7Pe8VXuMNT5i70GOqUB7SfyYJceDr2Mur7xSLP1vqldDCI8MStY%2BQwpZHnQnzNxi3xVgLIKkJi8n0dTOvpMabAlryLKQoGY5tYaWTn3fukePJQArkPLY2xnVWWf9e4o3eTEPnhOTSP0z0oBuuLN3w1vDn7sN1uv%2F%2BSWs7JSwK0mqXdp7bh1Caa4CfPFmCGfFQFTwjKpaYT60W8dFCHUggYUx07Fa9imkeuexAjsztoNfM3d&X-Amz-Signature=b6d1bfd0ccf7b574670c4fee0a6f3725b789291de54aab14f7045453e9a92899&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRCX42NA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDDezjurZlPDVVltGDGTYlFBXfZkkipsURqy39V%2FepHmQIgBKYSlWy%2BEbPA0gYyVsSjbAWtSgVhCeZBVPdfpEf%2Bp%2Bwq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDC7PFOi9ysLC6zyTVircA9I%2FRPH7pAD7iuPbTv9Qg9s2id0IVQcoQf%2Bz%2FwdyHbss79ILVkYMKgvMghSDyTGluk1%2Fx71fAVpDjBWJgHz%2FCAOx2MyQQ36QC9paPeSIRadiLWoWQHuYjJFJBVFUrWwD6Y2uIskgTTkYm897MTiVmoITQ5khFjr%2Bdk9f0XoDGW43qEEHqLIW%2BM8KwEuzESrXB%2BDCQb401GdrA8Bie%2FDsix9d09l9JwB%2B7sIic73PO2EXJZMH1Lw9WveM3iIGmB3rpuE32hIrd3CzYh3kDIXyj13r%2FGzobxoPet%2F38BVL%2BQwuv%2FrT%2F1i%2BK1m25e7A7JB2sun7EF9DfR8iL12OICfHjJcONrKL2TxcCshxDzM%2BAtkvuTDlzgGKxB4FTvGcnV1uMqI6CWVUQpn1L5NpSYmaoQj%2BbkdtcI2hsKN7a4wRr%2Be4G%2BRSSQzTmT6bVQf34aP8ELr85DyYfqLMzNTdukMv9JK3345yW4UTQF755yNUQES3wGHIM402g6a%2BzBJN8ba3O6O%2FgEcwEXPLRLuOLnb7pzBiV0aqnn%2Bj9EdnAfXXjCbPDix1aNPmFWdFSi0s9scva5U2RzmI0Tyb9lY3ecAD75rsQ7EmiYj69Z4qiDWerAvZ3CgQjGNpNVxfYtO1MIb6i70GOqUBFubFyiYmd7t4s%2B3rqolnvUpGpIvKs7M%2F0YtaA2D3zqhKM0KKzZVgouNWe2Mi6tA%2FNDb2clR5pscOclSirBqlQfXrK7Ju%2FFqJOlftW%2FbKT%2Bo9jn4uoBgd2ZtJ1wa1W9D8m8X0N1UDy1Wa6Zo%2Fx9FDIVmbR3iL5optiX61tU1ongLKoXQvV07WZgR%2Bj%2BYyCIMlsG94FrwBq5IwDR0I05MS60rwPrgj&X-Amz-Signature=25b269efbe095384a60adb41b6a3afa6b727c8e66a9e7272d8eeb4252c9474b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN65W2TK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCeRSChTAR2IsFv3y%2Fj4z%2FG9QEZYUd2qNbXC022IUIZtQIgKmsH4bcjrfh%2FcKUgZsZ3W8zxfrPCuk5WhT1OUDbNRecq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDL2zVAt8FbX%2F7pOcPCrcAzmU38p8yHj4FFjbdakd%2Bkb%2FV4e4ZYPKIiocaTw4511kSGgIlMEA%2FWdS8JJfeRnDcHEPjm%2FZkFPtXQdHesknk6fKW3h%2BM7WewELCpB1zwsmn3x6t%2FHdaf07uWDPMt8%2BFSDeDCSJh5ArHLGXrRj%2BBQx6w7HfpFbMgjbZW6gnoGa2YQb8EhYhQXSfE5vt6w%2FaKvgQ5%2Fg5njpVi4t4yTKMd2Pe1mLA6txeKvDFkdKDGomLVutNCGRjQ5RL2GyZ4iGfA0KXJTEprQIYk8o3mXLvfvIMatoeRoWP102%2FG63Yk0sdX7y%2BnY2IhO3COBig3sSfvwY6onk3dtMfXT%2FF6TyrSs6Hb2MnD6dhkWtOab%2FUhkbSKYv4C7DK5aEfRB2hYtVmQ9Vy1ZWzVF59Gr6nAFD1qSvbM%2BXh7NZuoHsZBbPtdJTWv5yDuPgDJ5tUvEkP%2FzSP3yfeW7ZbjbZJHx1%2BKzBdEc%2BFZFWnoehdPGXn79RLkoFj%2FFeHXqmFp4Qunhgd6L1y%2FgWuqfLQA2fV97E2zWx%2FWoIHi3Riyhz%2ByAABEP9fFo8yyhKLi8mv0wEg9tA%2BKoefnQ2doz6b%2Fk45Z5sbrVOSLn2mzjjoErH5Qth0Zw1RFtxhqDSNdy0nMM7pJJFdFMMv5i70GOqUBlVn4Ptz7Hz96bsWLI4lqual7B1xDI5imAUOQG712EdN7mrL98f6qsfHFDChTxj5t57%2FHAv4tkmzEn3OI8gfwqUxH2BTqMJyeoEOzW6fhC2xwET3S8ADFXwujDIA3xvn1Y4yCJlNg%2FJoBHhj8Bu7bSUi33H9BtPGXd8IvZMJ1NYRKQRwITEGh%2B0AlDiddNpojjWK3FBU06E%2BJkWzxiP2qaEAmWALE&X-Amz-Signature=9af5d698b5d537b217f27b1c89c236f03a3b4e024c13bfb50bc4c0cd7c8deb2e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZVLJMEO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIEXjy%2FxW3LgtT8CUsWUy%2F94mWmI%2BrAKTR%2FoY57qSPif9AiBQnwaL3iC3%2BG5v%2BkQBYwOntRkMOxkRS1EcfYbRjYWRlir%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMYVLiS983vVxjweo0KtwDlwtW1RHuQELd%2BcZR8GE7cuJPsvFkTw7fPn7i68tT8wBRmvYmX6ONieMUe0CfQbJgo9k%2FWLVBGjKaQ6IC6PYByKLaYOuIfF6Mc5pwCIFW%2B6XeolDyG7WN3mRliUciF48MeaXXUgG8JWmr9q9UdZOAmUV0g5dqftxQi6I9yFePYIC7eGOkRHceV3gk%2FIKemXX6zftsxQAq7AlF56wWhQKUFv%2F%2FLF%2BCuYGHRZLH%2BPx0OcLNIGlwaYCiK0wsIiK0CzUzFv0t1qdqCk4AKiRPQz59QecQTJpZYr6BsvlZOZj6hf%2BiNPEqFQDITsVQUJ5BTG0xte2O3ejGVVYdfMX%2BUnfjCvDytljkYLuSz%2B58CeJ7fnPqzm67%2BcFZcgdtYwVMC25sPJUs5viAQQU%2BiyG4i6ZIoOEEauA%2BVrngnTWs%2FTB3aWE%2F0yJdnwG2TV0RH3xTH8V3v5rl7OV9joihzCPvKug5zd8b%2Fjk9mDFgqXHLZZMP%2F2T1Rogl8TytBVhQzr9atxdp2jCHzTtWVRDmgFRAsgYUbF5KNF%2Fa%2BjmdOphNdfUMbA77y6pkusMsNL7O1OR2KNgybReZDFHGN0cBD2ZIepVMDdbo9Lw2uMLq9SYSaN8sy%2B72v0nAEV21wgLRjscws%2FmLvQY6pgFUuq%2BGhT4VUqaIFcfCzsSwNkp1muTpuUARkW1xmusRYaboU3TATUDJ4XoauvNKkbIpqURIWWo6Bpcf%2ByYjmBY94vHHODWZdB3KORoVALEIaISioN3SSSnwdZ%2B8sDRq%2FQa8bheT7A70FYR17hTrV%2FPg%2BT2ISmLjpaGC9Mqbsoz89KrvGaDjV3rgsVq9zfkvUZBz2xwCWbuOz73Zqx3ZJRJylQ0QBnIG&X-Amz-Signature=e3291b740f8516c21f50624954bc49788f1f73a74f254a53250bc000084b0ba8&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZVLJMEO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIEXjy%2FxW3LgtT8CUsWUy%2F94mWmI%2BrAKTR%2FoY57qSPif9AiBQnwaL3iC3%2BG5v%2BkQBYwOntRkMOxkRS1EcfYbRjYWRlir%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMYVLiS983vVxjweo0KtwDlwtW1RHuQELd%2BcZR8GE7cuJPsvFkTw7fPn7i68tT8wBRmvYmX6ONieMUe0CfQbJgo9k%2FWLVBGjKaQ6IC6PYByKLaYOuIfF6Mc5pwCIFW%2B6XeolDyG7WN3mRliUciF48MeaXXUgG8JWmr9q9UdZOAmUV0g5dqftxQi6I9yFePYIC7eGOkRHceV3gk%2FIKemXX6zftsxQAq7AlF56wWhQKUFv%2F%2FLF%2BCuYGHRZLH%2BPx0OcLNIGlwaYCiK0wsIiK0CzUzFv0t1qdqCk4AKiRPQz59QecQTJpZYr6BsvlZOZj6hf%2BiNPEqFQDITsVQUJ5BTG0xte2O3ejGVVYdfMX%2BUnfjCvDytljkYLuSz%2B58CeJ7fnPqzm67%2BcFZcgdtYwVMC25sPJUs5viAQQU%2BiyG4i6ZIoOEEauA%2BVrngnTWs%2FTB3aWE%2F0yJdnwG2TV0RH3xTH8V3v5rl7OV9joihzCPvKug5zd8b%2Fjk9mDFgqXHLZZMP%2F2T1Rogl8TytBVhQzr9atxdp2jCHzTtWVRDmgFRAsgYUbF5KNF%2Fa%2BjmdOphNdfUMbA77y6pkusMsNL7O1OR2KNgybReZDFHGN0cBD2ZIepVMDdbo9Lw2uMLq9SYSaN8sy%2B72v0nAEV21wgLRjscws%2FmLvQY6pgFUuq%2BGhT4VUqaIFcfCzsSwNkp1muTpuUARkW1xmusRYaboU3TATUDJ4XoauvNKkbIpqURIWWo6Bpcf%2ByYjmBY94vHHODWZdB3KORoVALEIaISioN3SSSnwdZ%2B8sDRq%2FQa8bheT7A70FYR17hTrV%2FPg%2BT2ISmLjpaGC9Mqbsoz89KrvGaDjV3rgsVq9zfkvUZBz2xwCWbuOz73Zqx3ZJRJylQ0QBnIG&X-Amz-Signature=b25b1eab8c74cf8ee5f7a8eda856e9376cf029bf9f4e2751e6a98ede724ce6f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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