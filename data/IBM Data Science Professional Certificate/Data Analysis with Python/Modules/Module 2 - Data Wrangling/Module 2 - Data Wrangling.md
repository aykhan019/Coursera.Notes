

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DUJYSGG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC4EPGy7Xl17IlOByGJ1CHSJtUfUqDAVPTgqh8DC6mBhAIhAIaWwq1TwzpyFOWrjKpeMkAaHNWX%2F04rqqqv4hUTGMeeKv8DCHgQABoMNjM3NDIzMTgzODA1IgyPmeBJLwEyLC5Y3%2Bgq3AN39tOoWf%2B27HbTNPNx7rKItBR%2FUgimgg93HZL6%2FXRnnIXh8kbN14OW63CQJWyw5TqCKCC1yE3P1jvTft9HzEhRV4yIhwbRXz9IhbuSqIQfMQjXRwuALV29FilyWI4bL5zXQQLbd%2BcNHygZ3vVHSlk6FzqCNddCKSpbJD%2FIdMqrGvTjbYSxB1RwwsXT7UJf7HUtT1eJrC5yg9BiIhu3LMykyV63zMHSYeMgNfes07xC2FEr0nIoRZwN9juXdf3%2BKGjc6j5yXKQUfqqZa7mvFpU7HukbrTwp8cRO7Kr45SX69L7drDr%2Fsux7KZxNbDBYLw9PZz%2B%2FqkZ%2F2ZF9UbErxnKcZeWykwLDE3XgDDXGnC2MVy9igmk9PwyS8HpNVeoC7lyiymw4bfbVqueLCcbJSdcI%2B0KL3O92V%2BLO5GqeSBBAqcUuT5%2Fcr0lwv48sh58H4B9oiLP2jZVzZbtbij6x4VLpF9gsEdLYLsl8s4S8m6qQMvpPjjmzXlreRUNWFMD7%2Fdnn1wg1Fj8scq6yHUJTCHn4aS715S8fR2c6o2DZCEA%2FfNEJ5P14e0EEmCWmsoI9KqIVEaioStNdCOar9RVigoGhDUOiaX%2FxJCoTA0%2BY1GY9HvtUXbP7276OXXfjzjCTxJi9BjqkAcGxneUf4FvNJQHjKXEerSlx%2BKh17tBZ8kbnJREnBu7JjlepBeewjcJj9fL%2F8pjW5wfqh8sq77SiMtVKiY1H72B4mrOm%2FMxISrik5aIFi7gt7VJHdmLciQwVUP7jrCqJ2FY7r3aD%2BaZCaSsZmCdYMGdLjj1BlcH8R%2B5WauE9baHhbC8J00UwzRsqLyEYgi5angfH35ULzMFEXdR8MMT8UsjNZXvP&X-Amz-Signature=f82c160089e298af7b5137462f7ea5811981e47f92d80bd32312d9af0f0a4f5e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2IUTAWS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDA2kkUlsNQdjdhbzgn0YA7vTYAPic%2FC6iOWXPapx5OrgIhAI3K08OogYWNv74lA336el4UHKQJX1EdzRidsdn4hiNsKv8DCHgQABoMNjM3NDIzMTgzODA1IgyaTZmA6TohA4W%2Bbr8q3AMeGI52ogZvAOI1o8uZwWNRvNOHoWWxEfsfRW8wp3u8cgDVrhHDr6rhuGSOx6wl3JKkYt21rxe96W0GdRzRf1RDJNpTtOZ51aXxhI3lQx0z3Wjh9tQ5qY0FxCJdp1RS%2B3Vfhp%2B%2B031Nhu%2BmYhxPeVUQWpZbB0%2Fmgnvx7gzIQ%2BjwvSGGUdexXyhUJkADGIvLCroOMu2A%2FGuexeNMQFGu%2BaqpE4uKZ8rpmymMj%2BoDYkew4Y2MqczAOL3xQ95IuD%2BxfdPPym1rMxp7lfDtJPhhhYtgqZmDkcRcw2qMpZqlTbdNTr2GAkye9aVFzKGUj7r7FXBubSynPfAIbe%2BcLhV7LoVZv%2FeazvN9v4OPe7dTyR4wloqfbDLkCy4ft9GDGLWYjVGJ8xNTiq9t8hU9lATq2TSOSKQnU3wCa8T0HODHu2kCobwEWnwf2CaNXQk%2Bf1N28PubAYcYys%2BuEssOv839xN9YnxLWYqYCxmg6wjquOEwZeEknzcSSBYFBX4can4YrBcNIx7KGSA6IFIG8hDgznb%2BeZ1rWuTm0PigREFb0e%2FfjVTK7q99zHQv36%2BtdakVvqOZjzOPkUX5LJNEOtb0%2FFJItie9Cxj51Axw5WfG7z9tuDpcPjU788a3JY0bADTDbw5i9BjqkAZzDi0TXWn2M0Cjh9cIJATCUYL%2BFrsBBTGotjPPN%2BKW1vC15BzhFtnnZN2TvV%2FjaGKqmBwEdFanyAp5GNPMnOACcqQhb2yPo%2BEtaJIEcw%2Fkq37Lyad0M9Z7VNla%2BXEAp66CaPuCzyyctWv0hQ4XUn5qWnHMr9g6FCBbkqoselwxfhsmWTpBdpyhX2yHmKlR2ziZifoQXC7j%2FMOybiZI5uF9CndeK&X-Amz-Signature=67e6e0e089e5b93d9093c336dd94dccbf47fcd98903320164ce10265769ece5f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662COGKV7M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIAtqF12YtpUi%2BNrj0njA2uUIsZ0g2Qa8iBWKxhGtNnQ7AiAo9GZfA1MmhEdWeUqkDPsgeDFbpL45D5JjFNJ%2Fv74AIir%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIM3uAo6%2Fj2KNqxRL2GKtwD1V1apuBZ8qdGYwJHspuApVH03%2FJT6OyXV5B5LhXKOyyXyWkgMdaESVsPSAJSj9cB%2FZpYoutwqjhGlMt4GW3x2jlFvDt7LtUioJdZJBVGW%2B4wwebo842IhmJGMmiLR5%2Fbs7eYiL9PIwRCjT7igWh5jKQnh8lUQdlFeG5ULaxvVKkYcT7DwIpSa1ceS1h7%2BWd2SGWkczNWbMBj0qz9YB0EhnamnCYcZxsZKx5JzHs2yGX6MTxu6AomzomenAfffbOLRjoSjpykjKMswfWiP7czdj%2B%2Bofe2nT2V1ehdKrNQMMarDc9P2Ab0hV7m83%2BwOQQhE%2BXwZbwIbQos3GLEcewlK3h9qvtxR6LZTHhGRw770fr6uswUL7qxeXhUs9zrSs0CgwwEUYw47uKumiskIDIoCgI%2FQDZ%2BUtQv5%2F7xGFVguUYQzJyQRNTH%2FikCnNOWg18yIlyrAfPfb8hdRM7evbv%2BdXdmlqyqwgbU%2FfLTyXVDpbN3WLTeg9wrhE0MZyaIpacazN0RZFRHyCX3bOD9%2FPImLOsfNm89Sxc2ljIrxWROjXPTpwveFmVT3lzO%2Bl3YJ9%2Bv5ofx%2BOuPtV8IanECIW5NhDDma8J%2B7wDBkSKGnDpjLcGIPJQiPs1P90MOplsw78OYvQY6pgFuHKtY2C7%2F%2BUN%2F5gM%2Fa21wtdaaeVIv89V7DAvKz5N0im5saOmM5WK6izVI%2BxSpm2Nqpg5uKde3%2BM%2BiPDppqC8j24b%2FNuYONbAlamDuX9%2FiR4WeLAYZ50f0JbJZBp01OdYBX2G75Va%2BzMSvDngKNKDuyexcCtjIAsIpd%2BBbYTOPV4mB%2FqE5cQUTm3Ylqut%2FWWzJEabOE4e4S7sCXtti%2BxPwvsAC1B6T&X-Amz-Signature=d28c92b5458d67c8b85631c923ef88e9c78c14e411bda0500e87ae35b3d9ea52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTYPGIDT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCOiqkVqGLRw0rAYpEaGklZz81tPfJRtzyTW7I%2FzDTUKAIgUFTWgoHFDELLfU60nlw2HFF7Es99d5re0bXZ%2FLRhASMq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDITdTrFedswwzz3rhSrcA0ockmr5vZOuT3Ir2xr072nn3aQ%2FL83w3mEeNM2XDaGzXbrXnzvR8l5Z84RcNbQBBJoXXSa0spDOP8h99v6b4CmT2YVMIgBCfn9RRfKF6YpQLF7h%2BmwURtQTknFQokVAEBPDHB4Sr5m762b8lBGd9DAH0kgN0bIHqS5ywl%2FhDvPGQDkYi1E3WR6osvG4iUwUsw%2FDGXcZIKsFRTchFBeB%2FanmQWpFrxNlyjlum8wzX4cxlnwExJp1xie3LG8jsYNYVEa%2FnYRB2BMOYJe5IlGlJ1lJjAB1qPMEjap%2FnsK44IGFJ1%2BhLaOw0z83BwjfCjt4moI6UpQc4kDlC5TGgJLA52ijfzNGch2WoQK4xcW9EOeBwDd3oNYj7DDsTLdvSUIzDKcIU1KG4H4Hc0K121eoXiOWcqtE9aEqb24HM09I2bCawj3sa5rEBQU0GN5dzYAMwTuz7eVIl51I%2BV5i%2BQ%2B%2B0G%2BY7UvGkCXlbY3bC%2BGyaibcUgbu2KlsfLFlW3AGlM1Vm3loSuIL72WLb1v1p45lytWviq5LEzGm%2BWCl%2BcSG2QlnPyX320n9B4JOXNpJLk96KKnOWOSZflVI1K%2FnRt9zgyio1ZJW2Ctnx7xEhbJfrRv24EGpmvXFJROZ9jBgMKfEmL0GOqUBtN7UaJ5kbnuBIBTZWtBPOG2WVgCRaps6n%2BtU6HReP7cZDiVBCUj0w%2F1BPnM9lckt0U5k5BCsIm3MAGzkeO67nUa%2F23ufl1Xzt1GLiqX%2BS4BkcXexxHae5sohlsXEy0o1B0BkR7XXoHXkqFyKzWhZ4eNfOONwPJgpAcYwVzzWNk%2F1pCtySiq22y4mMJKeQP4j36V3lIdIkpyIwg7M5WyPEbtp5IZ8&X-Amz-Signature=85fc22d4b04c3002019e7d4b6878ce2d0e596de9ffd214f126c664673942f5e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZAHHZFC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIC%2FeKneJjH%2F3KcvFRK%2BfRs%2BfeMR%2BJ8g0lLoPhmnPK5LwAiEA7Fb5jN1cpCm3c6DG9vIznZK6vw43spq22OapeYy820wq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDNHSYS5MvOqmLW05RCrcAzIJBqFlFJh4jnsybhLDC5HQvoHO1aRwKd3cc2r3Ar75L2nsga4E%2BYJNnXJhRYgo88RCnUr0rHdXfeOjA%2F8H3Uvctpbet4No23U7QeKKEwxM4Ql%2FTd5ITk2WcXNz0IB6NTA%2BbDoN5uG%2B3%2BARHH%2Fl558UWtPJOcHOlpTJqodt33iicQmTe%2F4XRWxcRu0IeM3m9MklexWQ84UO3R8iTvqEQQsSKHcnpEu0ycN4JB4RWSCw35%2BOojD7pMQ8CYZecn6DwokK8cwXSIrNYorTRWlpKzWANSeq9aPjt4fFcAmOaoyDtnEdkCs0GXPewzVN6pls6yQyhmjlSsBbXnl%2FF6jc99e%2FyWteUjmTG93xeo2CgP0cnsvrDv7hew3mMA1J%2F9xjI5P8EKlY%2FZt6vzoci503fIumaBJQGzte3k0hUgNC57c5BbKk1sRs9mq4a0VmaEVL7eNZ1bxtI9RBFobINomzZ2h8A4WMAOxV9q6ONdDEidjxskkJ6vHR%2FcfGjIDMkMKEA%2B0MLf8xBtVmuWP2bcyZ8KryD1z9K1jNqqWSqgC6syAFwRL9xiSgdVf4jfdW9n511NSQWX4EuUqwh%2BWdyYG4ad1RfZDYNGxw%2ByPR7mkxXMdQS0T4P4%2B5YGQqPKQyMKbEmL0GOqUB%2BH3ZWyyPoiliJdgKALCZUmCKtTaMjfHSksRyNMFs2Iel%2Fc4O%2BTsFW%2FnlfrPdz8R45FvHva3BiRiBXdiGKIx63y62iEDpAX1UDKgaVn9%2BV7QdWiznj1Ji6uvTJoFHJ1vDs2FF6wc9MiUhzxVA5EagLkXry6nQsVBSU9duq03lZlwkwxSl%2FqkPTHKSt00%2FZV3l%2B3Rumse29W%2FEnDZ9wDW7%2BvrO58n6&X-Amz-Signature=a4891aa470f4ebe75eb8e0f69f4eee01182f288e8a1e4a2364e3dd2a625f411e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOUUF4LE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICCQI5JHGn3s%2BkisujUNHe4B7NVoZkaXCZgGATUU9kEhAiEA77ZZle3HxicZIrXcaoSJyomsQR0CoDOglugS5NzQkgEq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDNijKgYG1bdDQy8wKCrcAxu9yfaeRhQiilvQCu%2FiNmxOkhzARrX51A248REsfttPEuy2AN3I6mxvA8WofnGBTwdGm0DnClrlfpsGpxF8NiemPFlvZSuFzofyTBvsp9SL8XhZAkJL8Kz74YQ9Wg%2BGH26NI1L3OR0p16DTLY%2FxkfUVq9fGJXxjCE0v4uW47pXG3lLVbEWE7lAfIxxm6b%2BAUMwPuADyyN5KV1Ps5w6mmqsRq%2F%2FwkNaIrVnjsU3vBowkdBOymVSur8OmxVELBjRzHZJh5oAEJ2aEsLfhFz%2B%2BPxZIBrLpHcOnY18ROfqOf2FbZQ7Y9junpQzwXAdrLh45Jwtb8x1U5%2BUcULjRoXBv%2BeayV8hnwSweoQFcvUEJLrdb%2BB%2F0KsURtXev%2BBFkyYFzJdKY4mgc103t%2B0TaZvYV919enfokxmi0cWa%2FC0ohTtqiq9TkAsG%2F8qClk44LfIdBGri1RQDVnd3tSfHRplOZr%2FDkzWY1ImtXddpzlUWPidIT1VUsgbeJO3r%2BBjZDcatwj3onCQeTCxEi2bzSMOOH04nc%2F7CxY2eCYfTDN3BsN1OInCWzEqCuJFL%2B%2Bi%2BI5W3kcspIU1ThMH4s4BPu5Stn%2BgX3Z80fb30nZAsZnAx94bb2%2Fk%2F40Ydsy9qAsn4oMO%2FDmL0GOqUBmwQvqxUbf0ZARLpZQ1iTLeAi69CduALsg4lgEp%2Bb29Y6RN5cQd%2Bqc0hgudfyPmC71AsYmn8ZBMKjuKKVfrppKYFTdpvZCWAmIr5YjS7%2FsTgefoUz7y4s4iwFTZTeEXsZzwi9VS6H0700QB85QTxTgM4eJ2CoabBfDmrfgaeuAuf9xqBUvCAIa7CoM%2F2J%2ByVfB4bDD54mWMcVqUQpUFg6zukp4%2Ffr&X-Amz-Signature=06f79d3304882c9167631acc7a014a1a3328222855ad008a0093d9319fa45f40&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSODZAWC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDF%2BgCZvHX0UPML3ps%2FB97z0KsIroYedbnfQTpO3C8xHQIgRWbRvLw8Jk90Q6mq%2FHLARWCz8LfHcWS5AVSDT3FRykAq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDIICOO3n0zq%2FfnuU%2BSrcA4R%2FdPOic5nxowUerkSuhwt1%2FPf%2Fy7UHM%2BTg0gBgU%2BtI6N4d616NxAu2EGx1njfoWK%2B0OOmJ%2Fb7x%2BuPPUvXeb6EEgrsrWM6MSy5wrAWOpVNAXcGk%2Bo%2BcVMj%2F5l25tbIG7d7BMj%2F%2Bk4hKemkrauDGW1pBfwPwOkMX7bGkkv44gO1cmwvLPbyPmtX66XcVC0yvBdTCXBBRcXpnhMMlEeMbA52rx%2F6t%2Bb%2BXUZpdzsItRSmki%2BcKOLOfjextyATstPAKCQoznT0VnSv1Xv3Pe1l4L9pdrqGH8tPQMUKE2fnC%2BFzky6vncByP6pDkI6FCNc6zRn3%2BcM33ejXrg5yNfRDSvjc7JevRsMuGz5FkhxZlji6G4%2FU58HrRC3n1QSPZ%2FrQ4jmy7iHaJd3nkozzo5%2B133BJ6AGASweb0SgvvtMdfklA%2F3RSWP7v2B%2FN1BGy6oH2fZ%2FSeMQs2pHovwWXEYv8Vji%2BDGXSs7U0syLYrKnjgngJU%2BcMTgkd3e5V3a61Z2sXU87IUlSD2FGsIZJbKEp4YJJnoYu%2BTO5MUA0ajgAQfSqGRAhDyw2atXoHGWYppNlIfwp6XxmFJ0jCyUcGCsbUGoWUBzBKFCj12yJFI5A3xhnSsWTeqJT0sl92xuwh2MJDEmL0GOqUBmyJRNfPfF%2B4ZcFte3gdSTSlT1YP%2FRFgYeelvXPCkRmSJptXHT37aL1i29qGQS5u8jQI%2FyqLHjUafB01R23GkNz5w1PhHzYXQAG70fv%2BpDFZ4CujCarULPHo8mQtiFR76Isy9h%2B3Svp2aLV%2FvAcPisXOoTotWANx6KGRvOCvVmFQnAbeDQl9vYzsRPEkULK4vdUCukRInwZ3gcgNf8eGQ9n%2FVlkBL&X-Amz-Signature=7bc6b9c30e06a11af374d242097f466c9595cb64ef89fae1573a73f8d5e3c4b7&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RD3VMC7V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2Bpx74eAgOok1FRmZHEDQDtycFD%2FLCLNvLVWYZEC78vwIhANXiZCjN7sLKIWLEMDoP084Cn6bCUnbmEcbw9p69ciD%2FKv8DCHgQABoMNjM3NDIzMTgzODA1IgxNV%2B8hyhEDKpE0VpAq3AMYAalUV7HHmqD6gPd4zRt2fao%2BaCzwYMnLYr8HyqsIPZ%2F6sX7WfoHggY2a5C%2FSt07SEfctNSKKEuFuCSf4OK7vgjXepXUL%2F5aFXjV0vLLuNJZH26ihwkGl41ixxlXJbUBm2sx5KHxz6M6i8HGEY7dAd7Jdx2M2FePzZ0lgiGIFekoJj1kdE5o41dxEkqRJEagTLzhdSDZwZManABqXPUXbVUAJOOZBPMyBYwtQEi%2FKF3bzgoN2RT8NSL8l9j1eo4yT%2B1NWRzl0Wt%2FNNlpkHWTXjqaU6XMrR%2FsXxqtIS0pjfWfuelgtioInqgFMGo%2BT33N%2BrC01vv%2FAKtX19P1xF8OoLDTrMsu89rlw1mNLb8rmksw0BGtqfwb3NkOzGpTN%2FitW9vNo9zqLcYuwEcZ69L1CBcmGF8xlhO0xY7QiKTTu8TQ0DTBJG6qwaE9H535JcvO3t8ywPVg6g5LlcchFAK3pAFNGAool0zCA1SvtsAQFej2kDKHCCleVXmL5H0CGwWIESbVSUMC7l66oRi9aO8JSqc0FM5MgCyTcO%2FGFT3p9vCKIF%2BCFd1OcVkfi3B1D6nN9%2B54MmLuAdu4c6o513dMdvn8QnomzNWb0fF%2FVBuHB%2B7yCReCUhXEWXx%2FkvjDww5i9BjqkARzm%2B5NUh803vWON67T90%2BinHImC%2FJWpTY%2Fgg%2F7G620987G0gTxFf30j3zsVyuPiQzJBnthRD9PMSQrbNfKE0wJj9ZdsoSndZn9jpBEOX4aG8U6qbh1BJytonmaOIkIf8ZpEj0VuhhyBRaZfvts0EvoAmD1C2UAySX4pzeqHAkUXGX34xrcpT2Iime2n5xFdY8qlP5qRU91gZOpciHKUvwNszl9Q&X-Amz-Signature=4457c0a20d1cc2b7271f48c60584ffdcbd8adc336631492e203454dad36edc26&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZAHHZFC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIC%2FeKneJjH%2F3KcvFRK%2BfRs%2BfeMR%2BJ8g0lLoPhmnPK5LwAiEA7Fb5jN1cpCm3c6DG9vIznZK6vw43spq22OapeYy820wq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDNHSYS5MvOqmLW05RCrcAzIJBqFlFJh4jnsybhLDC5HQvoHO1aRwKd3cc2r3Ar75L2nsga4E%2BYJNnXJhRYgo88RCnUr0rHdXfeOjA%2F8H3Uvctpbet4No23U7QeKKEwxM4Ql%2FTd5ITk2WcXNz0IB6NTA%2BbDoN5uG%2B3%2BARHH%2Fl558UWtPJOcHOlpTJqodt33iicQmTe%2F4XRWxcRu0IeM3m9MklexWQ84UO3R8iTvqEQQsSKHcnpEu0ycN4JB4RWSCw35%2BOojD7pMQ8CYZecn6DwokK8cwXSIrNYorTRWlpKzWANSeq9aPjt4fFcAmOaoyDtnEdkCs0GXPewzVN6pls6yQyhmjlSsBbXnl%2FF6jc99e%2FyWteUjmTG93xeo2CgP0cnsvrDv7hew3mMA1J%2F9xjI5P8EKlY%2FZt6vzoci503fIumaBJQGzte3k0hUgNC57c5BbKk1sRs9mq4a0VmaEVL7eNZ1bxtI9RBFobINomzZ2h8A4WMAOxV9q6ONdDEidjxskkJ6vHR%2FcfGjIDMkMKEA%2B0MLf8xBtVmuWP2bcyZ8KryD1z9K1jNqqWSqgC6syAFwRL9xiSgdVf4jfdW9n511NSQWX4EuUqwh%2BWdyYG4ad1RfZDYNGxw%2ByPR7mkxXMdQS0T4P4%2B5YGQqPKQyMKbEmL0GOqUB%2BH3ZWyyPoiliJdgKALCZUmCKtTaMjfHSksRyNMFs2Iel%2Fc4O%2BTsFW%2FnlfrPdz8R45FvHva3BiRiBXdiGKIx63y62iEDpAX1UDKgaVn9%2BV7QdWiznj1Ji6uvTJoFHJ1vDs2FF6wc9MiUhzxVA5EagLkXry6nQsVBSU9duq03lZlwkwxSl%2FqkPTHKSt00%2FZV3l%2B3Rumse29W%2FEnDZ9wDW7%2BvrO58n6&X-Amz-Signature=009c9e3a7b94860d2154520dd8e78068f1c863311963e322df12178c22f6db99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644E2BO3T%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCWGOrlan9sQkE4mIEevwAFuKhe0P31M2YulbiIl7slhwIhAIHfMefBx4uieD5G1OT1aXQNsGT9nPK2qHkEQYDpvRC1Kv8DCHgQABoMNjM3NDIzMTgzODA1Igyk52Vou8Sl%2B1hcgWAq3AMV92sfn3wTsun0k3nmuJzMQOOeVDbWST2WD6hO6UQZ2jdKDFvhNfj%2Fq7vgOUhzLuAl7iI%2BvR4qWLZadGBvkVteMDNIoe9yJ3u3wFdeKGW%2FcqyyYkS%2F%2BnUo8m9GOueMuQnG5ltonxj6OVhsXsM%2BOpDl%2F7LlgKAO8adclOA7ntTfrFWkZcWarJMlQQSRxvKFHv92d9bx3Ojhky6LPXmwK5l801vMNNsjWXBHVGaNOrYlBqij3XH%2F%2BzIMNf%2FDesgPmgDMqkVrW5EzLNFLQfsuFirNdvW4jvmjlsKfI1Clb37hxX0LOva7dCnJE8dIuHHNbfINLKFhtX1zE%2Fje4vB8LHfDMpLVPSP31cBxvGzOuw44ap0IGhlOKNFYxXGuL75K%2FelnvS1ieIIj%2BN7X%2BU4ROwvtw5OpaNh0dQfpajVR9QN5WYRsClGeHjicPzIn4cZoIh2Oq%2F080b8G1JJYOJgdLnaQifTGPDVrRiTsLCnZJjZXcfYztSS6DY4t0cpobyhExk4Wzvz6aVNVyYNzabGL36ZASz28rlyCVYLGPLG9bJOYyqJl0t1y7XsEvFoTCD5y6JzVLIyq25gt%2FbSysVqDij%2F9s7MtaF%2FFpJxUk2GPPTYB8O7Hs8Jhwztv5Ld7fTDuw5i9BjqkAQusqSCJ%2BDfAs%2FOf5zSQ%2FPAF1ZJyT391M71XVCb3fVUBSzoI%2Frv9sDwLlGCClm6LOVh8FTfwbIRfeEFgWAOa3a9SRUgGm%2BAdI4bYz9%2FTnsPEZMeIv1Jx6g8kqLIbF3wsSU1Fn%2Fb6crus5yaOHncbIM4fA70PuFwggwwrgr4VZ0CpfX9XkzRN99Xo96rKQxR8m9gpoy8YEB7nE6cv%2FIWIgeOdzsXi&X-Amz-Signature=cb12525d2171c502303d6738461674bc98790f1d05c33bf9f782a4c91992e64c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644E2BO3T%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCWGOrlan9sQkE4mIEevwAFuKhe0P31M2YulbiIl7slhwIhAIHfMefBx4uieD5G1OT1aXQNsGT9nPK2qHkEQYDpvRC1Kv8DCHgQABoMNjM3NDIzMTgzODA1Igyk52Vou8Sl%2B1hcgWAq3AMV92sfn3wTsun0k3nmuJzMQOOeVDbWST2WD6hO6UQZ2jdKDFvhNfj%2Fq7vgOUhzLuAl7iI%2BvR4qWLZadGBvkVteMDNIoe9yJ3u3wFdeKGW%2FcqyyYkS%2F%2BnUo8m9GOueMuQnG5ltonxj6OVhsXsM%2BOpDl%2F7LlgKAO8adclOA7ntTfrFWkZcWarJMlQQSRxvKFHv92d9bx3Ojhky6LPXmwK5l801vMNNsjWXBHVGaNOrYlBqij3XH%2F%2BzIMNf%2FDesgPmgDMqkVrW5EzLNFLQfsuFirNdvW4jvmjlsKfI1Clb37hxX0LOva7dCnJE8dIuHHNbfINLKFhtX1zE%2Fje4vB8LHfDMpLVPSP31cBxvGzOuw44ap0IGhlOKNFYxXGuL75K%2FelnvS1ieIIj%2BN7X%2BU4ROwvtw5OpaNh0dQfpajVR9QN5WYRsClGeHjicPzIn4cZoIh2Oq%2F080b8G1JJYOJgdLnaQifTGPDVrRiTsLCnZJjZXcfYztSS6DY4t0cpobyhExk4Wzvz6aVNVyYNzabGL36ZASz28rlyCVYLGPLG9bJOYyqJl0t1y7XsEvFoTCD5y6JzVLIyq25gt%2FbSysVqDij%2F9s7MtaF%2FFpJxUk2GPPTYB8O7Hs8Jhwztv5Ld7fTDuw5i9BjqkAQusqSCJ%2BDfAs%2FOf5zSQ%2FPAF1ZJyT391M71XVCb3fVUBSzoI%2Frv9sDwLlGCClm6LOVh8FTfwbIRfeEFgWAOa3a9SRUgGm%2BAdI4bYz9%2FTnsPEZMeIv1Jx6g8kqLIbF3wsSU1Fn%2Fb6crus5yaOHncbIM4fA70PuFwggwwrgr4VZ0CpfX9XkzRN99Xo96rKQxR8m9gpoy8YEB7nE6cv%2FIWIgeOdzsXi&X-Amz-Signature=98eb64f411bd1cc79e2f258c86109b47fcecb025c7dfe922f4e84807cc5da886&X-Amz-SignedHeaders=host&x-id=GetObject)
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