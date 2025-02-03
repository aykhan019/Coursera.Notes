

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VS7KUXJS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIAsog6Eqd0co7Uki1mp0odz2V7dfYJaYnS1PQktbj2HjAiA5I2HTeRTpviAKe3WM7sdqRfRTZls5LXbD95EKPG7wIir%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMqu42bdE8D%2FxrVUVnKtwDyNOoLYy%2BXwoA6OuA6et7LtY%2BM%2BxPRJs4Cwumbl5h0cah2mS%2FH3v8UlLU8mcdW4oEn%2FUnz89%2F4UfZEll2%2F%2FB9%2BEBIHA%2FP844mfDR7jLIbi2ttuBbjk0lKlCwm4W7okGE%2BzvEajGEIOV6NvwynqfCkrdDtpf8IvaEJWD%2FHmJGKziNTC6w8IcGNUQGNViGQAEeaxrsi4T6GlAgplqTa3ub30VPCuQ%2Fq8D4yB3HJMIfV6BwO0%2Fal%2B8ueSglDg6lX6kHuCnBnxC5N5uLYZPxSb%2FPOOXZilX0aG0gNIceVyavJ%2B%2BCqToWn9yI600hk15NUg27VaCFwkFZKAa5xLqnkpkWm37%2FAoKbKRdOEtQz4UlBT50Tl9X0p3nSAUJO%2FYOnpH4nv7uWEgFHvbE31bO0QLZ7JC15UXKYAcyZgFeXK4ou8pGc6H53d%2B3ROOV2FenaPlIYXxzhQR%2FCv2WkQoMh9sjvz9RIb3W%2FXCXcUav9%2B3AS6AwwKfMiEbAp2gPXGGlht1UeOJqxDpFuE9org2sydjHBe9DvcMG5kMeY9cJwv7yFANHkBHOvjiDmxVyewyz4BENVwbXVLllKLYdHh1b%2FSF7%2F%2Fh%2FfbbE8jw6i8fASiyiyMmJKkPCrDCS67E0%2B%2B6%2Fkwi8qDvQY6pgHIQsaJXO97ZWgs9HY0rj4CJdKQLvkoE%2Ftb75a5Wxo9nsbH%2FvkhVWigdtM5vAcoks9ubenXHXEWjhhj%2Ba9nlJwB3fYxH7WSqn5ndWgo14mqjAZ6FFnYtIKdVIObv%2BIQ5Zv8pzH6kl%2FVuxo9x0c0Q3va3RBPcUl%2FgFUTvKaF%2FotXQowDWNq64ti2Tj1gplR%2BDONJXlM87T0uVA11EQZG83%2FISWqd%2FD2T&X-Amz-Signature=b1cc75a4091caa94e2ecd6f9d8a239707dc78a839021f8f98db05d3b446cd9c0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4FFFAE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQCb5LLYbFcxLb7mIPjqBv2q9ByjlzqxCTQmTgxCoeHrfQIhAIjzcS9Mz7JG1VVku1bxf51jAbovfOFh8FLLzYGerN5AKv8DCBkQABoMNjM3NDIzMTgzODA1Igz4obiuRN8WezJzASsq3AMXY7%2B9LILskCMIUIJn50ddymhWL1IpdFuvZtTgQN1RjE9siXwSifAZ8V0P0ck16zupfa6ZNt1rRcD0%2F2XbielkZA4gmMxNHDNWIjuN2XZ7ZYbZsIps151W1E6eFH%2FKMCrRKwHShHWwjmM8ak0ddtLjVYfk7bNXCZxaSxHOv%2Baa0mBuw0B2RpMsDUBlDryU2ipUGzOFH1qaIYx%2B%2FuG%2FrDhQXpBxbl2lXDKdGDpm%2FHL%2FAxsCNX1EsikNnjSe093XlZZM2yw%2FcBUyi12GDzeoNt%2FxrqxMYhPlvStnoQNoo4asZCSwdlqJl1S7FdxjAgtA8cfEsvK9mfEHClu86%2BeOZ5RG1dWzz6XrwUv23Vy%2B1yTr5CxrsjUt6gVmyytXUVWESzffhC3TeTIsGXqYfmDlWOySb5%2BmMuNaSXQzj7u%2FZRdIln8h3%2BWI%2B8PgFYVu4Af6GP99upTDZZw1zL96msoRSX8%2Fat3vmw8F9M4b49yLchQ2tWPng3l8iutUmqCuHxeDYc7uK9K64rhzV9cDyIrkuVxlzi2npKZ%2BJS%2BL9rG3byHldy18St4NuSCYF3J9YbU7y5nfugC9qsdPBC0SNRRG%2B%2FcsVItowXKSTLr7nXDVGn%2FegAroh7t2tiZHt0GmgTClyoO9BjqkAcbh064Tb89UYn7nnegI1dheG3t%2BLGM4HW38zl4YsJ5JVep1dJy2QfBpOGQm8u3%2FjlS2NssuH2EIFjrBq6tAbOU9Au%2BlMyKFBrxzAvqJ9AU6QT0YyqNCu0fYY7BUKa9Tm6nQARU3Fw6XGH7V6rUanN1HTG2ZE5WQs1iJL%2BUhPorgizemj8%2BPvkR%2F2bFK5MaTl5Kf73wsDacBJSS6ik92K0WoycsU&X-Amz-Signature=264dfd3bc86b74547cc1d9aaa0dc33285587c4f201160edec1b74ad15e9fa0fe&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XGEH4S6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIAxNm682aVh94XtB5Uz7kQYBenu60yqbZhArSYShmO3jAiEAkNLhOWzp7aExiVDwnFRjKAfpBDxnQM0G1AO8FEdkY3Mq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDH3wYv%2FNZdxGO0VUVircA8NUDJlPGkZMr5XaS2On4%2FUbYRDIgfnmvjIcq7%2BVvgAqS9HmBpsQQFLPtchz3g3cEAr0e%2FiuT%2F0m0k9JMeUpRnleQbVXcoZTb%2BlUfUTsqMRKteAdpjd2YWTCAN8SsQcEARue3qT%2FVpCNqkqahcDQT6I6W%2Fgp%2FFJWuQxSQE5%2Fk0MCVK6IM%2F9QVZWqwwF8jUAe3NtSNyCEEGWXsrcsKTW31pDDgbOiOHJTfUR2upAazJz6t7ypW4luEeCKOuguV5CBBQh%2BAq3gC2fOPg2b6qH4QzLQUmVZKT%2F%2F0TpLIopH5erBtBtwd%2BBKNUMN3dO4m9rjWHpEPKr2YuNZt%2FeRrOmOu1qWf7xT5A4QMFwt85qDAhhK3NcJ2eJpeGdL3oEFH08O5KNXJZ3vk4eZ2u3ihl%2B6IHOKtqZfYk%2BdI%2FZKO5p%2ByzO2pFKctSLYJtnALDTBVUtQk1FZT0zX3b%2BVSuxPBmxKLZnNEcCShL4Cs9IfAywLXyvB3bAmdwOpoYlmQNNhjURLH2iESKod3oPWHvwFtaFwGpnUfTpFcTlXhF60pKbNM%2BYmBn7vj385ELu4fji7PyjH2broIr7quEJCNq0X6my5Q8lbAxBEENoolqsz7ECMQkLQivKekbwp4kC%2ByaA3MOzKg70GOqUBTZ7G%2BMJXt9XzXzC1BwgWnsRNdndjo2j2AmsuGifHiARBI%2FqepuGYFgU2PbPrbzFahIhStVAKka9tZPUsaT52hFXtAZqGUA3TD6FZto1zCZ6l7bM%2F30JQYrjWNN7Co7Qpl%2FQ30vVK9n6BqVp4%2Bw6ohdDdIicygwUtmRI%2B2ELyrI%2Fyh9WCmXZwLSwlKgJVJEnXruljDQVRkX19XJAXW%2BrNg5UdgZXI&X-Amz-Signature=240251b0e14b1a52136d1e0e1f10671ab9edeeb274a7a55b11cffe2af40a2599&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY7ZXYH5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQDRur1%2FuSW747b9WegKtMJVmqEhAkYQveSZf9c586AztQIhAOyhHyOhUrPyfCkT8Nzspg1Rh%2B2twFqRClK1ZzdbZ4g2Kv8DCBkQABoMNjM3NDIzMTgzODA1IgyoYkWCvMjaDDzCki0q3AMxKLoMWUDo2HFS43JHlTdC3P%2FEOXJWBns4pGHOrrfWEMUFykd%2F4rhGgs91ylchOlRSdaSpdLbsFnibF0na6rAAVd%2FkJ%2B%2Fsr28kSQRFc%2FODrVn1JD%2BEOeEWWaT2f16%2BaqL7LBZSdL6h3fFL%2FkfcmPDNM4budU0DfptptuRqALP1RwSQA07cnAyuF2ZIq%2BoBDcb5z3%2B4If9bur18B23qKrY0M4tcA1qJYt50hfEjfoA%2BTuU8ygwCuBOAofulIb7t5gnAAvSCiRp1TxHntqI1%2BDGus%2BFO6M6ASt8AEDsst9rkKDfn7v1qVW09yOJTIKG%2FrRr3ydIVRIMOgJgYnVaA%2FGhLey0e0lD93udjNsdbbRVdxfbrwadVYa5xsfHqxUoNsWcTowJtmMvE%2BDnE%2FM5eFJEvlZypos0m%2Fc6nhJ6aYEP7DjUwdZukQ1AvTurtKxwRPYc%2Fy4jjny9w4dOuPuHGEr0kMRzoKoMqPH4FdJhgq0%2FUSeVYVvxQvxD%2BBi4Qn%2BQcSNIZK5KdzsLnAIQabT9FrBJ4GYwFnWUTFkcfZw6URWwXrf4CwD%2F%2FMnrHdoht4HqDikXInuzzUpCKOVzMeBcGOic8pkViFjMOY6N6esa70F%2FZc3R%2FAdOYpvmAg6OP%2BDD1yoO9BjqkAVEqU%2FDblFO8Ice4nGWkypyjgOzE2zVRABkgKBoUecYZLaW%2FMrj0UX7itKfLRZ5eqo%2BiO8VGjYLLZe6%2Fs8LWcX3%2ByHv44zoSCqU1HZeqPJa32xI%2B%2Fo%2FN3Qd04MW56tcZF%2B35N8CNdyp85woPKrAFVtcQs61y9VMwUmY5OpVEG1bcS6NByTzkSMGzlreAC1YR7ALP0oEub2tZAC5h4F1aCxY4tID%2F&X-Amz-Signature=71f49f64a4d922408489dfb41042e8e904ec46f27788d79286391561be2a1f6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4XW7OIL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCuY7qp%2B7rxttTTHortD4W7Fb1bF8gblIu2qne99cZIKwIgN125j63BqfsyhNAHy2O%2B3iXwKjoLYrrEoIhqf7FDdLIq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDP2Dm5WQOpExvStmGSrcAxVPwQ9%2Bm5L58XIbepnKlF7c%2F7y4Lf5EBgTDPpv2ojDyhwRozA5igv24EiZ7NAQCvoXsISH%2Bi5axRFZC4hJvt5cNTqWUKzyNoQnxd6v%2FfGkCp5DN9cvkpmnK8rIHL0pUWLqq7vnWLVt4jLYwMGS4u%2Bb9weo78%2FpbSoDx7kjO1AG6fhLVsEpckgz7LzcWdbzNPT6zk7WDv4CWaFZvhmOYmmnVgUJFTza4VyQoIG6l5ecd4F2D1X%2BVU83tVuHtHCbRVUIYZmI%2BopYbAoJwE9yrsBVkZqIrvgMZLTr5N2vt4%2By0zOS1nlbGF6lO4QRJPdbFQt%2FJgjCSKwwwchPxcE0tQNGsmDO7kjlW8y%2FlEDT%2F48eXqNbZ6jlxNPpfj9Vmrpu5MiGI3T%2FeFsO9CqMfIJ6b1%2BO%2FrrdBsOb5DfVEJnr%2Bq5Jmb1%2BjEkQzBT%2BIxqYCDshjkHchPEo6G7G2h06kgmVZ52QsClVjr%2B%2BrPBE8hI6T3MPcKxB8mX4pEQCvXVworQUQ8U5x4yHvNZXNsG3u1CJbtpLXQ%2BkSdB95YAr8FOrodYkzG%2FQWJ2GKsDlhXE%2FfelVJSliCY6Ws1JS0o7kOQvywrvvXvFrhCYsHaP0QfOgQtwgkkWiTTZmF9iQWVw0RML7Kg70GOqUBeG4f3EhdcP8tmYPneNayitxnhi3NoGbo53lkPD%2BbPDvm5fdvA0e0IuApMSjUO%2BueA%2BZ13S7BDOb0CHtSdUfnW8KgBvNaeqGs%2BLBxDhd2HYF7J6my9WhseGwJKXQzntT31zMMt9ZN72RjQKraEj5EDo4697gOeg0wwTsSX0GHNRACIZGevas7h8ZGdlQvfv46qDTE8YDcb%2Bzx8z0aRXrDAbWbbZ9%2F&X-Amz-Signature=28db15965d4410b908840bdd4a631bf6a8784dbc2aee48e646c4b32fcf443d4e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z34CY7E%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIEbXyMeLeTbzdA6ChSfB%2FGwR3Uz1lIC36GkQWER8Ry%2FmAiAtco7Ar7ntBdpKjWx2v0tkqYjq1qQeH9gAJUfEHFY5eCr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIM45isNPwCT0tJpTitKtwDIqgTvIEiyW%2FcTuo6ipudgI9wye1RDxGGqdH%2F2Jd0DCTkwSFEHAtthGh47wokIPsZW1nwyQ9vMj51RS9plp%2FNBjLI6gH80ADsuPoPodPEVjgQgB3UDb5f6vNF4%2B4GqRzqXd7UIRtWdsa50PjFy5nQk%2BugtIL97I4fDR9dKauTtX8znMfKgLQK4Kd5qstkndN5Vv7KILe%2BIhJooz6HniTUCp500rRGjdKXeUtOjR7SlZ0D3OUDXqkoSMv0APs6fvuXVCk6jGZTJVHnrevkgWxO8ZHfMQstd33bAUHqGayD84B2nsX2Qd4O26UIa7Yt%2F%2BBeQmMr77KFgbAIF1bEYvTYqmDcAdpGnjMH2YNHfFqxXtXGthLh9tvTG0HD6UAx8l8liZJaosIhOS0T%2BaVnkElk6lAimHYkoJNOsfqAUNHo%2BfTQYbHl7NnB1mrxqMFcCCDVhQPwSgN83A170%2Bt%2B0f8DJN3mwYWI8xlef9OTBIpVjj7t8ZJmOPm%2FieqdomPKr5ni5QFtjNvmZaLPXxGw1fn6IPQleIGtckcGO%2BDb5YXjCY%2B4ISgirFl0%2FscaZPiasy%2Bk9Mjy1b4e8CTLbugwih5cMwmXs8TEWIm4uiGj6cfeDXY0LfNGLUXeA2EUMwYwzcqDvQY6pgHEou6v8yf8gzINX3qSN1XrTCwkwXq%2FQitC656WNhjMW1Lc7ZL8BSg26aI%2BnB6YiUEhCh9XQsZxqjooRZ34UGvXz09JcEpA1SEnHo5TKJWomPQnfgtTYD%2F%2B15ZnNKTwmHxsDycx5VswkgtTfBR0rRRXw2yV7XmNwr7k%2FkYNWrOuJ4qCHps%2F2BEgXGs2M3xrldeYk9TvD8SuNowJoctuW36bEA0cCtyS&X-Amz-Signature=8a6613adc5104f59cecd03043fc51623545a5e02f5fca809c914734da07ab5a2&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GNNGYFM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIBCbCthNXBJVSL2mjKk3nNfqdo%2F7ebFFe2nBcqO%2FIS1PAiEA2h7DKkru1JVlMY6Pi6e30vHSnxiOmZRSj0iAlDXXeesq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDIZLlhaiSzwSohhIQircA%2FuvtDGwjd%2FsljniNHS%2BAeNQBMdwCov31W1FF9OT2c80o9AyxN1Idi%2FNjzphXeuARK5Tw0OLp8beE%2BflZj16NdrA2GevO9H%2F%2BNSerCiCI0kOdEVW8uEawfO5LxITB6GFIhP9s%2F2KPS73rSg3Iygbzfu%2BlCjX49JM2etnQmOHoRnV7GfYJTKQkjQhPg8MTl4zexBgBDqJf8vktyC9lp7Is9X8BAVU1MBbr01VCsPwN%2FGwuGqQi1inHAQs2ZnEPwE6kKO0J6Tkk%2F5BD95GHtIOW3DwiRwtEWpRmc8ihNMnh5DY7g3Mw7XYUhQP5zlF14DxOPR0wwt7C%2FdfUcAbnBuREuaHTmE7cKhgV4fMvVKTTvzeGXRv4gGnT8kGfXcd2SthXfmZA7aSITJ7q%2FK%2F5jz6SK5c7vm1N1a%2Fjw8MIkN8INZN%2Fd6l4r6X1mX2frykJ0FynCeqnruvje5jvtU04kpawt%2FKCXn58eOCv5tpqQsA4RvbhV0FJ37E4HvA9%2BlVAc5cg%2Byq1QykamRv%2BpReJ1KZKl7FooGiaDCV5JqftWyNyuCQFnabYzO0CuF9%2F9mdu6DdX4dc4ECGGpdYTljoKaZzTMyIp3KaW9cI7PAgyWF8KvkWAAnJ%2FZcYCQbPPyOYMK3Kg70GOqUBmWytIeJSzZUS5XXE9R8NWZXUtACzQPB0Wfeu6FSB%2Bwlt4%2BGTwCccd%2FXCVL94GcO6M8LeNwx6BhioJhZLU9UPCkvcr%2F6vy8JtS%2FimMXpYdyaqLGa5cxpE3Y4QyE2%2BJu29Lkha4WYbLQs7nIN9dyQUo4hsh9jdkzCawfu0g8CBGuc4R7zU7O%2FONKJUuiXyJ3IVhrLmuZo2KKKP%2F0UoeuyOZGCwZ9NR&X-Amz-Signature=01806a598a7bda6ba982c7816066ecbf981cdaecd3c1d1c233deb4b741bbe8d8&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RZUF33Y%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIEuPrU9fk8%2Bw%2BzAYkZwSMZQn92mn4wtsECLlCTOM00a7AiEAtWYLY9hSeqdFdAgywzKBRldTT5P19K0PQ4V0P7Mm9Osq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDMrFimsoDMg9nQoUvCrcAzlLbptJdmeFI6E13DBEuLpKevTtnLT0jsb%2FNxEjzuhwkG4AIFezTjQUwEd1gKhiISeNu1XywgI1zvfVAJdZ7rrFlnXHZDx8SN1EEg5mwsb2UdrytOrjqQ4rCuF2IdGmL2KzuvIwV9GR9m84TWb6K8LoF6tYmQ7wbzVbwurDj0fxZdsWCxay0qOhqenJ3XRqrjRmC%2FXzSPqnSISI0s%2BAkJzjS2gQhLKvXhHtgI8R42zC42NsVNXSw9UOivnTHmoyZusPjVfQbQGSWsChcWmJwb6gqITlLhhBuxiDAZwnM9K7fcs%2F9AdLhhHhY5V6U4w5tU9f5SEWu3c4ANGzXdxQOeIP190c8SaXvVd6%2B%2FclYNAQX5GgPHTgo%2FoXbQEvEQfvnlp9wCZsIGbfs1yfKqE9kZajEfZ9SNUwUQNzynJyFeA64%2B%2FMEQmNAN7NJInGu092RiHp5vVIl48w%2FxbT%2FuhZOX1ujeojXz%2FcjdLn5IosnCJBpsSHFiFIbWts21XB2UlO2nezxgV%2FIRz%2FwweFOXgtTpiIMuIRAuDLHFe63NMFTs7VaDlVAw1SgrOHK1GDS8IP8cs13hmLtUPo5nBWZ%2FKE64YXL5f9sCnyqvrP0Gh8jbRjB4kp98jMjn2sdeUrMIfKg70GOqUBrDfnn6xhQp1NnA%2BdtpO6bt4fm6NuwDdzjyowCY%2BEZQzkR5aPyVwGZYIOZ%2FqYYuuRCJu5vevJGGeEfSM6R%2FlOEtozmTiZeTRO8R4GcQdMjIn77MMpEujzUJZnKNE4aDDH28Snjs4CBYcl8Av4sehledJdLyb%2FaXFiPK%2Be0TD1wVRUKH7a%2FPFTxcBoannLWHGXXWEkG9eW7Y4XjI0Vm0LtRSemBFyA&X-Amz-Signature=f7c601354557f0a807afbf0cb0c3371acbb6d81fa78b07cb8b5c6b8acdc1bca3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4XW7OIL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCuY7qp%2B7rxttTTHortD4W7Fb1bF8gblIu2qne99cZIKwIgN125j63BqfsyhNAHy2O%2B3iXwKjoLYrrEoIhqf7FDdLIq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDP2Dm5WQOpExvStmGSrcAxVPwQ9%2Bm5L58XIbepnKlF7c%2F7y4Lf5EBgTDPpv2ojDyhwRozA5igv24EiZ7NAQCvoXsISH%2Bi5axRFZC4hJvt5cNTqWUKzyNoQnxd6v%2FfGkCp5DN9cvkpmnK8rIHL0pUWLqq7vnWLVt4jLYwMGS4u%2Bb9weo78%2FpbSoDx7kjO1AG6fhLVsEpckgz7LzcWdbzNPT6zk7WDv4CWaFZvhmOYmmnVgUJFTza4VyQoIG6l5ecd4F2D1X%2BVU83tVuHtHCbRVUIYZmI%2BopYbAoJwE9yrsBVkZqIrvgMZLTr5N2vt4%2By0zOS1nlbGF6lO4QRJPdbFQt%2FJgjCSKwwwchPxcE0tQNGsmDO7kjlW8y%2FlEDT%2F48eXqNbZ6jlxNPpfj9Vmrpu5MiGI3T%2FeFsO9CqMfIJ6b1%2BO%2FrrdBsOb5DfVEJnr%2Bq5Jmb1%2BjEkQzBT%2BIxqYCDshjkHchPEo6G7G2h06kgmVZ52QsClVjr%2B%2BrPBE8hI6T3MPcKxB8mX4pEQCvXVworQUQ8U5x4yHvNZXNsG3u1CJbtpLXQ%2BkSdB95YAr8FOrodYkzG%2FQWJ2GKsDlhXE%2FfelVJSliCY6Ws1JS0o7kOQvywrvvXvFrhCYsHaP0QfOgQtwgkkWiTTZmF9iQWVw0RML7Kg70GOqUBeG4f3EhdcP8tmYPneNayitxnhi3NoGbo53lkPD%2BbPDvm5fdvA0e0IuApMSjUO%2BueA%2BZ13S7BDOb0CHtSdUfnW8KgBvNaeqGs%2BLBxDhd2HYF7J6my9WhseGwJKXQzntT31zMMt9ZN72RjQKraEj5EDo4697gOeg0wwTsSX0GHNRACIZGevas7h8ZGdlQvfv46qDTE8YDcb%2Bzx8z0aRXrDAbWbbZ9%2F&X-Amz-Signature=7cda8ba298b3e3c6e8ee7f93122dc385d54fd7a30e11c91d2815614c523670ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZO4H3WNE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQCOQ%2BPxQnSM%2Fzf0AZgh559vv8bp0j6UeWbIgwyOyKV7%2BAIhAKbVq8u6qu3XB8E3sLzUNcxiRC1TuTW8%2FcubVD7%2FfgQ0Kv8DCBkQABoMNjM3NDIzMTgzODA1Igz7nPmhOrmoMNCIFxAq3AO5ey0muFjlAqBp1wyU5oegjRnmVg4Rlirc2H5SUFp%2FSQ9fXwlW%2BpsRUjwyZlW%2FN3f6Tk5KbElfsM4YXLuJuxoADrOu53AsODupYbsUVeyFk5et4YCTfA0OoXQuY7P0pPzGWpzc0kPyUn5pJTdfjng30YDMsZ2KsvPCD7GBdjPxw6fA%2FSnmCxochELZW%2FI0YxtLWsLM4bloixleSBcVE3BFKYtPXvBBcQxOs5txHcWUJF5puMR0As%2FXL%2Bdqo1hRlYFm0%2B%2FoRgt1N9Tds5x1b3LUX5XZKOp5CVw%2FR5SH77joYsqgE9sN1lQmVabcfxMHfMSVe0yxE6W98%2FNbzzkAZHroo28uIMAOK2JkKyLVj%2BwxA8JtyQL8dV9T734DOIOfc1XvnDAxFDinGlA2yh4dYFLGxZUe9Q0136eWNRwcMLy3qlZgBJMFEUJT4GcjGQhQpIRMqMob0UzkosfBuFGEE6HGZTqknHd%2F4WQJnwPebbfn59JSzsy4Dt%2BjqHHEKN9tDxtWVuvSno5zIQjpOBndwhcMZQdz2nezR7HJCyWmb4gDwFl3II%2BLL6sifKNTToqa%2Ft3UDU%2BDD2eiKRiFvm63QnBIiXq0%2BJv%2Fwy1opkoCLSQfy7PK5x0AxzbThtqAzTCSyoO9BjqkAQUjSeYnyLpJhVG6HNorJgrcFzCDuBTSYcdnHnm%2B01P952osvwS5FTa6GtOHRQwkuOy34j%2B6t7uhsI97gAn2GWdXmOqna6gcKlNptKSojmniWpy7jy3r1iBRMdpyBVLnN2WEns0Hic7lFfOyXpx%2F91TftBErBBqJoBV7fcgUBMz4iP6ikmwsNHSV9ULxs1SZuivKWv%2BjjQlGqS8q%2B1%2FqmZ2p%2BIrM&X-Amz-Signature=8dd0d5612cbdf912c898f6ebea32027421f2770d7c8b8ca5b82319585b899709&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZO4H3WNE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQCOQ%2BPxQnSM%2Fzf0AZgh559vv8bp0j6UeWbIgwyOyKV7%2BAIhAKbVq8u6qu3XB8E3sLzUNcxiRC1TuTW8%2FcubVD7%2FfgQ0Kv8DCBkQABoMNjM3NDIzMTgzODA1Igz7nPmhOrmoMNCIFxAq3AO5ey0muFjlAqBp1wyU5oegjRnmVg4Rlirc2H5SUFp%2FSQ9fXwlW%2BpsRUjwyZlW%2FN3f6Tk5KbElfsM4YXLuJuxoADrOu53AsODupYbsUVeyFk5et4YCTfA0OoXQuY7P0pPzGWpzc0kPyUn5pJTdfjng30YDMsZ2KsvPCD7GBdjPxw6fA%2FSnmCxochELZW%2FI0YxtLWsLM4bloixleSBcVE3BFKYtPXvBBcQxOs5txHcWUJF5puMR0As%2FXL%2Bdqo1hRlYFm0%2B%2FoRgt1N9Tds5x1b3LUX5XZKOp5CVw%2FR5SH77joYsqgE9sN1lQmVabcfxMHfMSVe0yxE6W98%2FNbzzkAZHroo28uIMAOK2JkKyLVj%2BwxA8JtyQL8dV9T734DOIOfc1XvnDAxFDinGlA2yh4dYFLGxZUe9Q0136eWNRwcMLy3qlZgBJMFEUJT4GcjGQhQpIRMqMob0UzkosfBuFGEE6HGZTqknHd%2F4WQJnwPebbfn59JSzsy4Dt%2BjqHHEKN9tDxtWVuvSno5zIQjpOBndwhcMZQdz2nezR7HJCyWmb4gDwFl3II%2BLL6sifKNTToqa%2Ft3UDU%2BDD2eiKRiFvm63QnBIiXq0%2BJv%2Fwy1opkoCLSQfy7PK5x0AxzbThtqAzTCSyoO9BjqkAQUjSeYnyLpJhVG6HNorJgrcFzCDuBTSYcdnHnm%2B01P952osvwS5FTa6GtOHRQwkuOy34j%2B6t7uhsI97gAn2GWdXmOqna6gcKlNptKSojmniWpy7jy3r1iBRMdpyBVLnN2WEns0Hic7lFfOyXpx%2F91TftBErBBqJoBV7fcgUBMz4iP6ikmwsNHSV9ULxs1SZuivKWv%2BjjQlGqS8q%2B1%2FqmZ2p%2BIrM&X-Amz-Signature=e7e8e5457e36445ccdae38ffd0cb25dda7fb68d3c1ee9cee3555655ecc675050&X-Amz-SignedHeaders=host&x-id=GetObject)
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