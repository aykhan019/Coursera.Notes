

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSCMRXIG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTuaewteeO84G62Oh8GVqIjtx1zOoGLiTDxnajSEpgagIhAPNhjiV5pvYUYPyLT8zL%2FaDuY0RXlKanHnOhBsM%2BxXL2KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzoxCl5UAVXQPT6IUkq3ANI14x7lyXOHCKSBYyTJ7CHCExMMyKCAhZm5lM63Q8Xbn2SgB7q5u7X1%2BG%2FZ7EIzEECpPkrpyXs5ReFwMOjEN5mO0cwxl9K0EQrZmSWJtjLtVedTwBe1E7%2Bxx4jN9aWNdUwO49bIJ1%2FBX7djmcnIpEDDQezf74iSpWLKftUYk8b55NNhhkFYNb0H3hg0TjREpfDQOBg1fLUHGhugQCHc%2B9nbOpf9gFaEtuy4Zh0QwIjBZbx%2BDOFHLd25jWY6s6Bx70R2QfuAjzH2XCTlhoJbr1nSuKt0w3hC6P9q79t2BigdreqorKIPneMtJgCQUSajae7xX1xrqHFOBKGvBHXArbTfEpR5%2B7G%2FNOjvYFjMzWtnpcHEVyQm9cWCdxAona43QJgIYqugDUquZVplJsvJBsTuQcETUI%2BcnLXPm06p3RKKKiM0AQCJZKBxqN4gXl5f4IzjDVgEc%2FFk9A84ks9h2ANPgN8wiz2lsl%2BechntJvLlSqLl9G7QB98tKXmtMiwGYC8YcIKn0pItg2VkSqVdLrDB0%2BJ1Js7%2F%2B5i9nH0aDYdqRq6%2BOmVxP%2FV6g2UD9qpPMF%2FxcwVG2%2FTycFGTYwoIvLi56kvIpr9UJlnOtn7Qp2m9qM%2BJWMPp0JzS8%2BN5DCF8vq8BjqkAaUCkwbVo3zKvWKllVcFVQYHVnEuUay1xxBUGd6skq0WqgwAaORUftq2YLMjPsZn4dO0%2BopZqPev%2BJZc9Y2xGRhG8pYceGQq1Cy250wq0N2qaqe0nq4haTIS9YxJmYYn%2Fw6zJ%2FlDsPvmH3nAjHOVmvfP0%2BuLBGQL8h1F9GGfMQd59YT8tzAH8%2FgjU3QZIq1CXr%2FshR2SFIziMaew9j8w9ddcrwVY&X-Amz-Signature=faab2ef25784e7d9dbb69c8ea29ffa8d396f72c0b611012987f7e3f2d65587f7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYFPPNWP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFIdtF5IP98mSAVIWUocckCHN%2Bjev%2FJ%2FssVfxHu8com9AiBKh6p%2FuUIRvpwR3WrBipQBGPmIQb61NYav3YZTrrvWJSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOT0JsJRqdR9vC83yKtwDhPVKRNPhbxGQXdlM34R7GNJS4pNAyor02p15xpr6DJNOzILKuMSsE4NfeOB%2F4KtkFOb5TH6SbfKzUPpZLivm2ng0AA4q%2BlCSnn4A5rygto%2FJxDNbic2r10IArYhSzVvgPQx8jHVb8vgU%2FfLw7OhIyIan4uqzAicNvFCOkqxOSZHSxAQtmaJ9gN5MLiHtYy5ZPYyrIP6vckPBwMrnrHR8huyyKfevvFBX7It2NSByTsFDFSCxiKjmdc%2BRqIG%2BAtWW%2BaKLn9DL6rugB7mHep9VgCNGte3eMwr8xRgglUUvwb9OmqXg%2FhrW49pPkCifOlKMWchOvGIyb03E1m9MdDoLOhdIsELglQHncHvMG%2BN1nxsnAFiRePFGe%2BH%2FfpYiHuGt%2FE7wZXg8DHwP37xFrOBJLLH58C0mupFAOBZwtjDz66ZodpCp9umgvknIyr4OAo6u8WoJh1KFYirKxrZq1llbonxHOztAMgFi2BRxUHJR94lfuQ9OKsOdOl%2FV9UYhzKjV27xVM6uVDAyv5qpTbaBqvdMswe06kmrMgEWytUj0rCf%2Fkv1NJgdzccaccl%2BKr8arAgYrAm%2Bf%2F4rVCCtfRrvELXlnBxfePB80Bp%2F5yVC6mVZs1CIw7tQZxJDH4aIwh%2FL6vAY6pgEQ4ZJxXVQMJmYP9RjqImWmorx3aK3%2BJlvgoJ1RH00qeK11exldGJHDr7%2FfoS%2FlvHAhZQDzT02LCY6oji9RoB60XIwSNWbUH4TWqsfL2CzCf2VGBpI%2Bf2MJsRDi5Oml5q7PQrr8RFoeaEAoagHYyN%2BnK0cs5Z%2BuZ%2B9rShZUR3J4yVb97Sz5zPRNMevIPFNV3cR1Cijhf%2F0iX5Orjq9Yxp9wbFFCkbwD&X-Amz-Signature=dac7cbf13a62b33d874f73d02ab31058b566ab96de84ebe537b584755e74f48b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3YBV2C5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDtvgDgYcGut%2F5Qt18ytl4SC2TjpfSu1brrKj%2FKzIPppAiAOh8oPQX4WF%2FoGO2MK6CiltrEoLIvRiY5UWVdWHNOC1yqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXEAp3Y%2BCfu89w26%2BKtwDuKA1I2Fv9k%2FVPCV7%2FVX3iblcu55Gcy2C9Gqzo9jr2BxPfNSFQPl5TEjLib%2FMeuLlPdcskWRvC6bv4DF9ThFnZdt9l0eQOjtPOCBS50buvOtJSOh3j2MYAOrBBHa3KZ1Sv%2FYIknqvZuyFbN%2BHVgL9roAgOWVpv%2FLLQAv7K0KqG5gWixtmxebl%2Bq7XwW6VgYFW7i24cmxnofeG132HQHmQwUYxzHfHnX0%2BgaQ2knecue5uuAAgiAErwiHFHVTOw5rkW%2FqHqARwyekQj%2BO%2BuZtoQLyHmeWBk7OyMCTFBQkYdC7Z6VGAd6fMTncNaiJVvtyGetlVgYTRC1RiT2JkHljVzPxELYSrYWVLtKfzh2XtIZ45ktohrXzmPcOqQtFQunxcenpT5MmdrwBXN%2BJBEVu%2FuRVxuweeDK2xplB5p1cuMrcglD5qZKK48MtEY7icOwF7Py2EmRv8JuQBBwAZM4yykW8nyYsYu3LrxFw8vF4wo89Ys71tEOL6y8qBknLWsw5evFNzDf4CESnYc7rtQjJHpMS%2Frc2%2FRtr%2BdKx5c3hz5jqIdufgrRXs78jzUEcg8yEEcIPgXudGwEBZMNM8jtR10Eo7gh5s3q4QWWlKe2xexKRuipNMUBpG7TUIMp4wvPH6vAY6pgGR6IZaWLoBMeN5xuosWx%2FSuwgT3Xm%2BA7R4uCCg7aVNODR%2FnH2%2B%2FVkRtwByAs1vEvkf5SKsBILRUDJM%2F5%2BUuVqrlj1fT92YJ7XcgmvXLw0VTb7pusUfdwiAPEm2NyfLjgxIyYiBeRpNZHIp99EjrAyN0yqm6rMljdqLUSJ6SE4SW3RPl9sulUrQmq2KwBahf11vXShvVzOcExBfUUogbkrBoDmWIghx&X-Amz-Signature=939ac5edd7bc8e12b4d4649c43e269ab45db3fcbcae78bfd17edab1c26871849&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4B3MWYS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIExot3UEr0gvYRB3S6gB5V%2F6yig%2FrvqMcnf%2BhwzS9H5SAiEAiNNfvpffrxfet6LsCJAimOvC1ezljTKQnJsrz8BnnYgqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHozswzY9%2BkGLfCqNSrcA7FNmsqehfV6MyPVkI8SamHTLP2CwthakisQnyJSJTW0fFJe64HnXc%2Fs5FYPIM0W4J69jfnW1TfXFz4Rq3lVKyg7M8IGIzAswrWIOAwbPFkB2ialdpLqP%2FUV5iLY27qh01zQSIIc%2BrSJhEz1Yp1Jl5zktiBGp%2F%2BGFysNIVrm6j4%2FsOKWrtC1sOs9jb7lpPIhShHpAwINyKNux5pKJBHQKs%2Fm%2FYxzjimMy7am0rCyTohRqiEm94sR9NWvqdHX23oK%2BQMUQRV8MhcVflVKqmVzgkoSARarYd2hqp7jPzLMajb%2F%2BtQ2%2FhTwOHzU%2BZE4w%2F1%2FxPbf0OgMcreZTqOCc852QK9NxzgcW5vBL2d627K68AC4%2BnZLfmWjLKJ0shtRMGQwvCjEEGDKWkIG51zZJLITfjUXsdGyhLWKq4klscDYsnULwHpCvHrmw3P0F2AVQ4XHz6x56mrnDjse%2BYxE1jZSAxWjqF5si%2FvR77f2%2BAPn9J9XpgTC5rpgYwJ8DtA0C9Nea4wiHeZzsk6fj3bQjaFYbKdkstcZITgfnhQdfxaqblRhJGBpIFPSpcvcfcz3aNkurxvyR4nY0gZvCRucb8kBAQ75%2BxwEHrZ%2B%2BN3m6zkju3ttUSkwYdd9I0%2BSlbjbMJPy%2BrwGOqUBbhIUf0dS9ICEADo61PD9v1UWu0s18tDMwEsLVlfaaLKFcnC5M%2Bo2xFgkE6om6hGaPtvLSyI6KG5vUvC83OdHAI5mO5NSGKv0ztOLus69FIFvazVhq5D5XDd9beW3vpEResnAlFqF3YE0ZgIow3GhnBGIY%2FwZSyXz1tSfGSu%2BI6At8%2BbNjEZjs%2Fr%2BAaCrJkYwcpv21Gv9HGmAoIo1PqIT6Oij9mRo&X-Amz-Signature=efea1ffcdd6727cc70284c4db6d97d23ec8d48f062be572ee0ba218c224dcd05&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IA7ZAMX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXpO%2BnUQdwHZmHhafHWgq8MrHDpqLQoBZEteEosc17gQIgbRYwFGXvs%2FIV6ATJjNktrWjxL0ZK9YkFNnAjAjjPwNUqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEPF2uJlnDxXdqUqHSrcA8wssiEe2mn7fVtRWtHYkKT9ohTMnCc6E%2BzA5eAkRK%2F9dGbBpc0kx1PijnFje3yvtMPPkb7rm6fAl7P9z%2BG8Kgv7YIfPfZsgnHqVYhZi39ehNCqnpKuhNKmoV%2FkDFMHagVHo6L%2BtmVnHatyZ4jDz%2Fs91pL0789Un6X9FMviACHx%2FqHmW3HAlFGGMzR9RJQjyvymRp%2FXwSlHKvvgLxPzvN9YNFFi7ROn56eHpk2C0IiLxINq0KQ4Q8d8kZS%2FuewpOX7YJG%2FQ2TkNVx2e0P6cEUqahOYi%2BcVdGHG%2B8hYYt2H2LpbF%2BsVko%2FYIjVPuK812Rv1WYDKhGX3vELaLRu11FxNr7NwVNWQoJMvFL3XQk171yV0IqS7OIwXKN7XLmmQ58YuA5TJzBk9I8Von2ZacOQbMuuaRfaXk33W4geOy8cAPkJXSBdDgi8ANPX76EJE9LaQxwLOL46%2BKhIAHEvS6JQH1UoDGMEzGP28DvhDRDJ1K7%2BkVNIYcrntgNV4E%2FSeKlKNonwWO3pNHuwB2SuyYhVFLDL42PqOLZY34QvvbaENerUL%2Fby%2B8Nh%2BqhPbj%2F0xeG1KdOe29f2oJ1qb5DuylW1HGXRJtHd79oy60jFVSJzHs2aZq2XzSmDsKfR5d4MOzx%2BrwGOqUB7AGmkRplQLwbuGFwJI1N9Ki4C8vM%2BdhA6vzbCQw91MFaox2bxtiivi7QJxL0xMjyzp50ViRtnT4o5b7ZCediZ0Bra4XvRUT4Ddl70oePr0mZYrSj7BXduuNKdgkjV51jgCXnLIrrif3NXDsjM0YpHhvTDWij9pBxw73y327GqGLDyA3f5u7F2It5dZefW5YsTnOb8i%2BHJLV4TVhCDjMzF4YxG6cJ&X-Amz-Signature=3918483ab5cdab7fdca32c6aa8926f2a4bd120775283ee62ea832d7668e5fb2a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TVUZU4G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERT54XaNqoNdNUu1lw%2FqhBWpssixW0mCrE1TOxNiecAAiB7m71ayKIffyTLSJmigvtTR%2Bui8od10RSeClYU0NRSFyqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvG%2F%2BozS1%2FRBnVcdyKtwDBkswxYR8M8tue3390qBWzOU4loqGPAabkVPnYIV9PwkYTn2g6tqL6idjrv3DZ0HzG86ws2jowYvn0hckzJxtZsW42GU8Ls3qSyc0s2uwaYh0T70ZggEbK55aYaRvj%2BVCu6cJ6c%2F46myFiSlK1IrxGQgYU8oWzSpF1ee463d64SvfXRpYyvYFa3F5ciG0vh%2BCPWfL46WggOyv%2FY4SbIahqsd17tDXyXLUPrmvbnWsHWzSRgH%2B3uY2PQ9rosK2HvQRrTzgfVm8NQbgnprzeKDjyM1Mm9gb8ZsRW6DHEuKxXhR6j8mxCZouUBGnhjlogvizinBd%2FPTjtTC4dW9NCtmbwevQvtIaHFZ4WJ3IQ7CkqxUoy23xyQNM%2BBgXB51Ep63qBF3uAtKNvZwnihlUOTYxhXAqFPEZzJRc0IAiKG2SxYSDQ2GXVqm941r3ex%2BmG7EzseOxINuw6c99%2B5S78ZRp3SkUOr3tvZnHoLhfyHYYRQNn7S3uloM5Mdc9nGTHtauMa2RQuZvMqOh7HFmaZbbjc0dWUrMAtrsdiiEFGWfSxqQegSPX1C0GN21PHix5b6fWhYP5K6W03l%2B8kAavR8UuW1YxD84qRiNkfYftCxJo%2BqPQzDAn8ETpqO7pOB8w5fH6vAY6pgHJEtMIIEexxlNOSCAEYZKTkAX0xGT4lfuCnLah1PxlJItvBJRM%2Bq%2Fn81nA1aaMJtR%2F2yeQTNEaFqslmWM3nYQmQwC8fHhCA31k1vtyhbjNZma%2BSy%2BF2cLZE7ke9fJKRK6iKjioz9DGn6EE7VM8tIcmojG6HhnXo2Mgxb7XmAeSZVz8QtqXpz3Gm%2F7%2BQr%2BRPtz1pBB8uzfuKyQaYLfWexcrPe5SxffV&X-Amz-Signature=a4b1e444681d30e7ad400f2a4ed56467fde3b680606c77cc5d3532dbd41beb3d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WZCKKI5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiWlfZOqN6xQlaW3orVFJ7gy9JMN8Sh45qir%2Bj9JX8WwIhAKa7uW7fzVUlJeeayPwGsPRYTRw1zQe4QF%2Bf1flH5AJ9KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxICOMO7BSdEXPZJ3Qq3ANR%2BHaZ8sy7BcHJ%2Fenwsg4xMn4U8Qq5pK%2FQatO8MJytSYfGIoaNLarunGqKE03ry6dd7U2BAx2dCML%2BJOe4ghnDYp3HYgcTO0AI3iP1c2wJFo9CN01GXrfuYZrCJPeg0GtB%2FNxg4nVB0%2FuLq0YZ06ipBbEM43z1xmFbuB4ks9YSV%2F9S%2FBhz6nuURlJCOj20ZmenrVGKvcA6A4C7aeRNuKy0OK3pNt%2BHMrb7Y314pEWP1MbLYZsdDwwJEHTynmVLYKFlr%2BqLuZXUIx9xHLUVzhVX3hC1FheyrBjIvlprad8ryYn1djr%2FmjA2RwCm11njmB3GATBk%2BuE6AffI5uvrC2X85zKcUP6QYh%2BmJCgKA1foyrt7rIeHdWLyaspU6XilLx6YRujLt962rbDE4z%2B5iCP1T1eBLxtJPl1kK42vB7HR0nPNH2dI8%2FZmMExVGT6pRDGnqFCuLDdGITudNaBWUma7qaM%2FHIo1NHwyyvyBc0PWKWePw%2B74qzKKXf1jGrpXuc4jjMvE%2BO1XE47eGPefWiNeeqW2FIsKUNhyWD844Zuf2PPRz%2BcNqFrjkGejgZonfKFIkZ%2FvKMNbXYxcpv1r49tUXdAPrQBy6wMNSkmw0YkwuHBqNrd%2FPF0RGvLuADDF8fq8BjqkAUfi5IPHRYivCprDjfDsU%2FvcyMH7WxzdfCPs%2BwslzkTVL50P2eLZkWQsxHS%2F3LM2dfxzshHzMeR50nJf6ICjvUivIqylmY4D9dq829OtzQlxr2aeIcCEjsiOAiuHBw3%2FvKzWPKAEMwEQp3s9wV%2FykvehHs6GrBygzAUugGc29A%2BYSmFguavQ%2BFQbEuVOL14Z0V2koIeZ%2Bk3HcBsRZ18bX9zGIUD3&X-Amz-Signature=c154631a03dbda09e0a37c98908d87f235e136c58da4e72422685c9ab9c7ea52&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HC5VS3C%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOiLMqj3P%2BCiMmqMXWv1erwJXhq2b%2Baix%2BEVO%2FswqH3wIgS4MZ3wKa%2FldvkqDz9BVhgH4d0JzRvys17BnM5i9tDfYqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPeRTCUuo3RYlfMMoCrcAwW8uI3cvggWzxJw1GuRj5cl9Rdm2JAzFPxPs6y8522VZllCF8Q3NZdZhw4smdGaJa6DZyig0fU8fvQjzZ%2FXzZHKRsmZyCgi7qSCA8doU8WWOW%2FKKYLH5NAFxHEndxmOXR4hlPPPQ7RV7vu8v%2FH5aCcubOtIgqVv7Q34ihChDg8dHvtJQftdswLlxUQRsw5jSQd%2BNyOnPQAnS5E6Vyf6lS7%2FTM1dLaR2KflvfWsEcrhWHeCEB0YwYpHtilrUTqMBkLVY56wP0j3o57%2FM%2FASlIqDhpp1PfJ%2BfnEIa4p%2BIDTNr40hsSBdIv6Vlm5PZhjPRLg5Nuwj5PBhw%2FgRmpOC%2FqLtrjwsRbJy7PxP1t%2F3P4tS8vD4UIJDsXxYFUtuhm5szeNEcrjKyLLCFl0NfBkQ06wLR%2ByCGRxGjV0j3bs9MM1H%2F42N%2BokHk1R%2FXn8mPYlnbvfXeeMtDM%2B2PSv8YvMnpCA9FLvwX0GOOfhmHwQ3foK76sJYOkVPPP%2BxzaGV0TA0MzB%2BRF1yyM06%2FiMaVg1ZMwOmyEzisxMHTqNeMHr3Qq8gxaU7B7XwR93lYEZLHOdxTZ1SORlV3sofqW8DUPhI%2Bp9cJneq97Anilu1xpIG%2FVaSyTFAPhxRUbg4HV90wMLrx%2BrwGOqUBBLn1dfbVkYAlCIFvlWe8M6cE2iUZpOSsTtKdOBSxGkD4QBLDYM077QRXBQjpbnoLBBpEjisSOjAJwUidNrZsPjAKoc4swx5Qc8I2%2Bm3O2CPuCfQgFv6aHsRV5xuLXw1MlixkPwBCSXwYDsjlfpRjhFeL7oD%2B9vRdn7Prb9cRgcXEF2ZV%2Fz6nSUiZ3F2EqPOzY6OHX5fsRPjZRsiXhSWxSZ7UJsYG&X-Amz-Signature=6d1fb6d7a423c0f5bd50294c35ad14ad5ccaa4bbb4a8fe24338a8381ab510f52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IA7ZAMX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXpO%2BnUQdwHZmHhafHWgq8MrHDpqLQoBZEteEosc17gQIgbRYwFGXvs%2FIV6ATJjNktrWjxL0ZK9YkFNnAjAjjPwNUqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEPF2uJlnDxXdqUqHSrcA8wssiEe2mn7fVtRWtHYkKT9ohTMnCc6E%2BzA5eAkRK%2F9dGbBpc0kx1PijnFje3yvtMPPkb7rm6fAl7P9z%2BG8Kgv7YIfPfZsgnHqVYhZi39ehNCqnpKuhNKmoV%2FkDFMHagVHo6L%2BtmVnHatyZ4jDz%2Fs91pL0789Un6X9FMviACHx%2FqHmW3HAlFGGMzR9RJQjyvymRp%2FXwSlHKvvgLxPzvN9YNFFi7ROn56eHpk2C0IiLxINq0KQ4Q8d8kZS%2FuewpOX7YJG%2FQ2TkNVx2e0P6cEUqahOYi%2BcVdGHG%2B8hYYt2H2LpbF%2BsVko%2FYIjVPuK812Rv1WYDKhGX3vELaLRu11FxNr7NwVNWQoJMvFL3XQk171yV0IqS7OIwXKN7XLmmQ58YuA5TJzBk9I8Von2ZacOQbMuuaRfaXk33W4geOy8cAPkJXSBdDgi8ANPX76EJE9LaQxwLOL46%2BKhIAHEvS6JQH1UoDGMEzGP28DvhDRDJ1K7%2BkVNIYcrntgNV4E%2FSeKlKNonwWO3pNHuwB2SuyYhVFLDL42PqOLZY34QvvbaENerUL%2Fby%2B8Nh%2BqhPbj%2F0xeG1KdOe29f2oJ1qb5DuylW1HGXRJtHd79oy60jFVSJzHs2aZq2XzSmDsKfR5d4MOzx%2BrwGOqUB7AGmkRplQLwbuGFwJI1N9Ki4C8vM%2BdhA6vzbCQw91MFaox2bxtiivi7QJxL0xMjyzp50ViRtnT4o5b7ZCediZ0Bra4XvRUT4Ddl70oePr0mZYrSj7BXduuNKdgkjV51jgCXnLIrrif3NXDsjM0YpHhvTDWij9pBxw73y327GqGLDyA3f5u7F2It5dZefW5YsTnOb8i%2BHJLV4TVhCDjMzF4YxG6cJ&X-Amz-Signature=0c85177a3df0cbf68c7ad9b6f5574abb96c66923361cfb97871b9f4cf9b7ec4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPRCULQB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPg1IzFojCFZ%2BZxRYLQrbUjwpHaYPcz%2BT91L8JNh78bAiAqpkwiy8015AQpdx2O%2F1sPnJZZq%2BDY4Idqp63p5aCy4iqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuG6T663u9B%2BfupHUKtwD0n2jE4W%2FfjTARThw95b8oGjuOkqcah1pfX3pT5r%2BZf2LPfaVHZK%2BgGrfMqlfL2OQ0BO1jVVpZVF5EZoTNEdD8ngXaN2GpWpm6fa8UsBUKdT1NClplSMS42gxuQFAogpXjWKRPiR1dAeZYiBWBnJRho6%2F6qZRp26TlfxMn55iqJa%2FA8N%2BAVqcgGE1EbsWVX3ZVnb2ASgPIUw97dl3P%2BtsyktH0%2FYr8mWvWcp0qmVd3ZbSCBIGbToJr43pZHS0Dsb2f0M4TatNi%2BZWEnYAS1I9PcwZ1f5%2FK3qVEMiQul77IZx7iOSFXen%2FEpufe5E%2BmXxN95sctHlXhAZnHOTnjJDKO0RlWlvUVvelLNvUvLAJXLD86igk%2BtnZ86TubWQsfbjUoQx1x%2FEhvYYVFFRHJuS5QoDv15XM5pu9j17v%2FMVDxphgi0DPe5IWzbqglNQubl2TTEy%2BlesJQk59Mh4w5f47KwOzLW63KZWVkHuYIpUa4bGYPIUdB79v6m1tDP7TJV1hUvSONAYSeMksErt%2BPuDoeoqo1UIvHGW%2Bf5V0ssGrMgTnhj6PlNBXn2bICnRkFPkQc7P0CF7GAh7paDEU78ZJSwL03vJYwvHFZrF0LNWjJEfmVv4SQ3ijNp%2BQMzkwpfL6vAY6pgEDW6M7MvDNMVGFnrxKmdlFxPV9Ce3MUKUCseba%2BjdwwHo6UullOgY5wjROZHtjNCgwxJRqqyRnTMWWhDYz7eJK6VRZG8Ep%2FIifqB%2Fpd1TPRJJFNblNyIihUjsJAPBb7gXzPixN9jEcjHPPb7rAa7dIyzkypL%2BdDMvmPNGza%2FynlOv65Xf3fLYFKxbxjrKVzdXuMfCP0Gft%2FX42grKKMXCnpwPv8Rvz&X-Amz-Signature=bfd6270d3dcde56e49f219788e8bd7b1a0db4bdbe355e8ea796a1414e0e8ad23&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPRCULQB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPg1IzFojCFZ%2BZxRYLQrbUjwpHaYPcz%2BT91L8JNh78bAiAqpkwiy8015AQpdx2O%2F1sPnJZZq%2BDY4Idqp63p5aCy4iqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuG6T663u9B%2BfupHUKtwD0n2jE4W%2FfjTARThw95b8oGjuOkqcah1pfX3pT5r%2BZf2LPfaVHZK%2BgGrfMqlfL2OQ0BO1jVVpZVF5EZoTNEdD8ngXaN2GpWpm6fa8UsBUKdT1NClplSMS42gxuQFAogpXjWKRPiR1dAeZYiBWBnJRho6%2F6qZRp26TlfxMn55iqJa%2FA8N%2BAVqcgGE1EbsWVX3ZVnb2ASgPIUw97dl3P%2BtsyktH0%2FYr8mWvWcp0qmVd3ZbSCBIGbToJr43pZHS0Dsb2f0M4TatNi%2BZWEnYAS1I9PcwZ1f5%2FK3qVEMiQul77IZx7iOSFXen%2FEpufe5E%2BmXxN95sctHlXhAZnHOTnjJDKO0RlWlvUVvelLNvUvLAJXLD86igk%2BtnZ86TubWQsfbjUoQx1x%2FEhvYYVFFRHJuS5QoDv15XM5pu9j17v%2FMVDxphgi0DPe5IWzbqglNQubl2TTEy%2BlesJQk59Mh4w5f47KwOzLW63KZWVkHuYIpUa4bGYPIUdB79v6m1tDP7TJV1hUvSONAYSeMksErt%2BPuDoeoqo1UIvHGW%2Bf5V0ssGrMgTnhj6PlNBXn2bICnRkFPkQc7P0CF7GAh7paDEU78ZJSwL03vJYwvHFZrF0LNWjJEfmVv4SQ3ijNp%2BQMzkwpfL6vAY6pgEDW6M7MvDNMVGFnrxKmdlFxPV9Ce3MUKUCseba%2BjdwwHo6UullOgY5wjROZHtjNCgwxJRqqyRnTMWWhDYz7eJK6VRZG8Ep%2FIifqB%2Fpd1TPRJJFNblNyIihUjsJAPBb7gXzPixN9jEcjHPPb7rAa7dIyzkypL%2BdDMvmPNGza%2FynlOv65Xf3fLYFKxbxjrKVzdXuMfCP0Gft%2FX42grKKMXCnpwPv8Rvz&X-Amz-Signature=77c5fc4141223d3fdeaa99e438ab51dbd8d8f058fe0165dba9c79c43ccda6f3f&X-Amz-SignedHeaders=host&x-id=GetObject)
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