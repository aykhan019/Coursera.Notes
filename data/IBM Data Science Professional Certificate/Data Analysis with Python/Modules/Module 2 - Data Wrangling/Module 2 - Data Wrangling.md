

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665X5EEXD5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThAVs299gBsNh%2Fq9CaathWCkdqzLRFbDjGwTSygYs3AiACcYImxy7T1KOtghzpSuqUp83Lt1axC%2BSbM%2B2apyjVKir%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMomz4Qy80uTZ8F4O3KtwD0ZVmPYJ%2F87BrR30tU1bCMUWkkteS3KdDnBPdVUmRI0NNQ0RK%2BukBHymIpa31BeTqRjnhxijodhjb2d2YTcurh4Z99wi3PF%2F%2FUKG6BI3o5PPeZxQ00NVyeAQcycUhZ3oLqxW96Id0kKJurOxobW67Fhi93DUyXFpFoBJHe6Z1a4Mw1tQLdb5oxeB4PtkQeAq%2FeXAR3WKjVaE7uEIQkATOkPIFoL3vOZ%2FTAplufjTT62ZrPcg9EbZTASp2IpuyFqq7jHROeGiW3dnBozWuHl3cI%2B71wXYNKLAV%2FLYt%2BVR7EyVhV5iINKKkWgfqj1A223idPV2oFhz1759rH%2BV2p6FRZDWP8TdCr2Fi%2FODqUOQJ29g5dKRTe7XMYx4roEBqIZzs6tlakqCnZsdQGxXfzg8LFAa5w9e3Wvm8bcUBbDu8y6vRZf04AHrbffXUzVggEQ%2BIWvs44d8pZ4tzMl4tzneNHFimVBZoh7p4QmSqLBNyy376XVCuexqsi8%2BzgKQbcPDHQLSxdmWNuShpizRyCyv%2F2WLU6ZCtT%2BYeYWtE9xKZFrY%2Bj5BxjR1sIb5IpDrKTkvIj1%2BW2hmMYWW98g16yPZwUtENnu4Wsbxhv%2BJ0dyNhkdHTZQ4wdiki2aLMZL0w5dKZvQY6pgH6aXAosIxwiL1WTNPhY9%2Fq2Q2jpOSmVqHkWUZyC2eE7rmAbPHcIkSV5TC2wPBJIWiaBEEGHf7H1r50DOSZrVJ2uSlgfPtDhoAQ6AjeOXEI8nWBLvp97DNs%2Ffktw2lp%2BHe2s3F99w%2FwUGQcJ6d8%2FvWdYypFPwoaeTrTqZhzgeSHDO27aL1iD2QRnrXAoCYiZsEljRV%2B0ZjrvJD8tai2Ih3ig2cidTvs&X-Amz-Signature=5eb2241965411b7610a2ab3acb5d0641c441bf32337f54381d2365437a545959&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XY6RJT46%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDArNGVgooidLBB9H2z%2BPj3%2BtO1tzvLTTOXzQyvHCax7wIgMOTKWnf%2Bbe82ykySGTV2uCmfV8eVyiCVhn%2Bzs3slXMQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDC%2FgnFnrDsEIkwI%2B6ircA0hDoiIAJCggwamzYbZ9HVntFUqMhxOq%2BfqXT6wo1NgOEoTleNgoRAzZ9P22z7A6yeeU%2BqgAK3e5qePEQ1bIZQ9q19%2FKYHluVmhhFh8j0u9%2BDeWb4DptvgP8zBodIt%2FDWWNdiRGPMziIF65dzYpNX%2FTELqf8s8Vxt2we9cN6ih9PPBkpiPYLOh%2BjHijPidHMypewzC9hjaKF0rsm3q6x4jTpGFUFFROWlMa3YC8Q3%2FELwOVkonkcOzTQ87dIzAYj%2FZHD6vFcoiJFYvYm8H1E%2Fl0YuarYPJeBFF%2FXgEcgDX%2FrAbh6ouObNBW70zqLHLaoiKmZzjhoLIEmJNNaoOXLJLyjcgA1DNmz5r4otL7B2G1APRkEPOVHuYxfwBRxWgktAezs2g2ZBK6iGsxcaYiXYb6eaxp8sJjc88zlZTehxMdgkXjopqpSkJBWkw0rsWYm6p7o8qX03zV11XG1n14RGeMDWJh%2Fj73gTCm9RsrV1M7wkc21ZvXyIIEg13g8RJY99p%2B9pC5kDTF4zmO01B4H8LOkdVaK3MrhxYf6JywEAx4PzDK8wt%2FIA89ybvc27h9g3RYPmH0Om6pCCU2PF3X%2ByXVQ1kXQuIHeuM%2Bu5EoayI221SPGv5oY0nsS9ywPMPfSmb0GOqUBvnTaopu3ADMPDPx0%2F%2BBAOKrJiLqn43WKvKBKKWUhQCHYX9y5m4q5zr5rLTkK5BsP3XDo5K0n0VPM4h%2Be%2BB3mNRDoErq%2FK9BZaQh1zfY9J7HoLPoUm9OLJd76U%2Beqtr8JN2hpAShyHdFoqYbUwuj%2F8xCnKzhViM6NE8yRWHeoI230j1iDzqhGMCHL3aHna7p%2B3aPiDmBDiYIYkulbqioWyImzkMhq&X-Amz-Signature=613f330cb73183bbc49dfe559d89c85cbee85255505ac895462885b36b9def73&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34WMXYC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIE3GA7lLX6at5ije%2BE1fLh%2FU6sH5DvtJObnkCHL%2FVqMBAiBs%2FRMsCaz118DCkjPT4G6wZF0NnGr4zjBlwsgNtxvxXSr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIM9mp9tnXzSqGIKTUbKtwD0RtS8zqMlQ%2BETdENfPbIMZ3HUPm2SREg1M4DuDvZ0MSgq4d5fKOHMSmmZfdck4h11iMFxSPDdJ271eP62Qg8W1CwDr4zKSDOPsf4fDuGgXsrq3wib9b91MSFGbIQTF6fPn8TSMN6FhbNfHwn9R7w5jtTBmegrN10h%2FK1Ae9ewtu9Vsm21jKl5ZCl%2FBUz%2BeSXmtwEhMc7aDU9FuqvHUU158EpiiUst%2Br6VOSaUEx608iH2CTSbsh8GRzSD%2FQK4sJVjkFnQ1uIyvE%2B33jhSZSmPWJHM1aTimeqHa8ov7w7uSVV5aFAkIa92FQtYgY9PXEAx1bgNMJdpbi8GNdjLF58DFGC2yWn%2F76gNmnGOLK438N5chvv%2F1QkRXsd4CB%2FQxfbXJyVpD0kM%2FySz%2Bm%2BL4T1CAjHNak9e8aYAFpiMndTnx7iwudX2g%2BHfRWD8VoprrM5y9YkK50FAHDXW4qFwtLFTuCChNOQX%2Bs%2BtiYpx6EGnWtbj1YQyWn2OUBxk79Tod0csfhphsPklNNBPOx1QsbkfzZzqkFMz5i5WxwtA4yaqVWE%2FRCeXoLp2mOcbFyBeCF2GV4gnmznEg5b3J6q8N4go4au9Ffd%2FLjXxyiZElL8mEX4d9sBVvjeu3qjuIYw6NKZvQY6pgEKRYWeHb1GKxck6N24XN29ANSce9q21UQ5AW53qbYGJjkN%2BJpkJxIAQLBDL4uAAGj5QfaLrYuJcQ2AE%2FVxdmjgWLe0tncx%2BtFfmSQ0zsgpYmheFAqn6DhvZVdqXx396ICfOOzrJjceEWfXKDOee4PmnMrXnq3njGjYDlAgRiWrIjOmZQgRjTket6n4V2%2FL%2ByFv2u15e%2FzYNyw%2BiyyUVXoyDF7auPn6&X-Amz-Signature=4e12b897b36695edea0b10d0a58f0210a3a236f86891719e76b5dd7be41868da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJOBRZDG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCZW4fn58FsDrPLQ5gCrqK0mMadcCY4rm85QjTYy71hygIhANa4fnY%2BO7c48VWLdAlQeAHsB4kDva%2FE9YVDzIY62TvXKv8DCH0QABoMNjM3NDIzMTgzODA1Igw3%2FM4mTBldaxDiV5oq3AMvK5kSKeUO0IUIVjU2hm4CrQDIN6XWypXLZ1dX2hiIDc48aW%2B8sZO4vVGXY6fkqZ31UKI88VXHmBA5GdP44fcjSWoSahZoegwwnoFaN2fbuuROwKdP4uIac%2FImyCgcJ6a0huIouEZSAdDUVVvwk5j9qaC6cmxbKvATqXcN98MT%2Fggy2bVlvsQYnKYcTNFnoCnPIhRhTWHrV4bfOhO4f6ppXVA2ZfYl8W5XCfy09rCt%2FjIAJTkN6z0xdSbSW1M2%2BbxK5yF93x%2FYzjR%2FuUUNLRAAWD078Hyu1oOgY58b6gvunqWZ18r4oYGpxio6Hqt3lEgm5sPke5Imues2%2BjsXdjtCOp%2FQMNbewmggz1Wiw5H2TZ8JY3bVwIW2Dn6YEwdiyUqoG13dko5pB7xrkIYelWjxA%2BqtkA1END3Np6Jq4Wk%2FNSWpvSWaOiBczxj%2B5wLZV3nfNXHZ4aiG4hAdnNW1HvGpyF1%2BLbtaiNF7emB%2FtiMNLc%2FD0%2FM%2BYmcOBXDL%2Fbb3GRT8BAjyDyI1LZKCdVvak3Dgnfqi0s9%2B246NTBDgMSlC0h2AHqxRTQSEtA368lLOHZxNwAAW0CEdCAapDicoE66sx2EzKafX9sd91izEQY0rtAu5hlXtUWQypdxKYzCD05m9BjqkAYSs5t%2Fr111bgi2MzqbhwIpM6SAovMQqszK%2F7qn13VrkhW03f8CQGhzoVD2Oy6KCnR%2BzqdaVqStog9kvR2yAYg3%2FCRt67SBn6qsR%2FEOjygGz73Dqs4i3pXxlfyzGIVETny%2FvYospkXjlp0ReIkhElAvZbaOkiDTUq2mWBYg%2FM6MbuOvdhKkUSWkpW9O%2B0IZkcFJZTDz8i01IxmW8Jq3tRo9m1ruT&X-Amz-Signature=a245820ca596dbd1e054ca0b88f8ce4e098ff0c322692a6d0f0a5ae8dba282a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZM3DSLI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQD3hSKMS1ENeKNEDCfjCix6VmOJl7kP3GK8Wz6FhPZJgQIhAKOZc4EkKSgbvRi6uxX%2BHQLP99E9Imy9gWjHY7Q0G615Kv8DCH0QABoMNjM3NDIzMTgzODA1IgxZGiLFjjDHWBjFUx0q3AMdyRRyu0XyfJmWy2NMOMiHH5sKZNMZUTpZPpe88a%2FZ5mW4Lzc2USpvmgwVuL8WoxjjdiF%2BBudKAUdY%2B%2BXEFehlpxbOzPW82ViDlWxbWRi%2FIz6%2Bg0Z4E%2FaRObnJ5Xk%2Fufp9WcgdpkwUeznqlEI9oLOCdZgpUUH27vZ%2BL8int%2F%2FLQcFoMnOaYmFYkmhdfIGP8LJU8mH3RglV3QyhlUki4952RRqbP3HdAsSkNu2rntabKdqIQ1ugW4xf6waTQejHQXMMOvxAQHAZs0xbIYS5nlA5bpfZyRKdM8dNEJvuXv1QguhCA8VWOx9PASKz9N7TLzfMoG87SkcoZ23h4c9PBri2KSSoRW3O3jinOV5c%2BwxI%2BeTGR8yrTTWoVYW4eKlLDvcXejsYBftkU31nyC7t7qBgQtZ7FXe4etqVu6BDFODkDxzp%2BV2eCnVR0SXOyb8g4HtaUA%2FRJGHLjTEo3cxm7hErMnCpjqOv6iIJ%2BwOlR5mZZK%2B1qpBe9yY2o%2FSqaDZWfCZs%2FfUToC8CJbBQdjfzptJ3GhwnkvcB%2B0IZyml6BYh2%2FEQxbBKEY4tJKYYhMKIk5%2FqDC1B1ARit8sb2ETfF%2BFtinEQUVMhJLB%2F9%2Frvgz8fbXK4CQvcpuBBbA4M1fzCk0pm9BjqkAek8zmnOa8jC%2BAf2jw%2FCZyySBvftZRhhLyyg2YDDX%2B8dXukiJdVAv2NA7P6zzf5lAjLG5vGt2qHuwVfN%2FdVpAfbvoSZab1HteYHtn47JF12ckA5OI%2FTQEX%2F4A0%2BtFSGQn%2FVmjMZCEJNd9cAjIlx21BzjQL9DBmDuAB25EZIp7pPaD0WPR%2BJa7Ih%2FNVgHqHPMEHNwQsu4OeBYPtYgyuP6KuJTyAUS&X-Amz-Signature=ff6cde5dfe3122072d0270b31533c54de6754f886c319bfc3fe11b74d8955e62&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQ2XUA4Q%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDGq%2Fdsmooj8OeXtgWk%2BDSfg1488PokVLp7sfj%2B3vrF%2FAIhAJ1PMwrRAVShj70JeuM754cY4Jb7pBKLSChNcIrnAXxuKv8DCH0QABoMNjM3NDIzMTgzODA1Igx8y3UyZlIB1bWP%2FeIq3APv6XDV1Tp5xCOxrdJjAWIUfcqu%2B%2BhTZjY98DO%2BBwCZqM4CbGpt2X3SWTh%2BDtnbYFnslbDBCwuG04vhGQit08C0YaIGwkcOU%2BeX7ieskyKacKthQxGyc0QVV2aG5y4VxiPbgSG33%2FOokZeF7cDilpdslFOCE05s8EjTjimhCXHn%2Ffuv7h1lv8PnPV5enAik%2Bg1eQkehWe3NzUTNKKGM0Nuaqj%2Fi1Arcc2ejIlRGWSdvKKrrHq2yCwxFWeCv5NJkWHuD8yt28owscYVGPXu2moiS2VM%2FVFFilot%2B08aSFnx81LCqwKUl269E%2FD37eMZQfGPDOqZcMHCsbtz9P9Ti7vOEJxwh7SBXaOlhT9X6ulbMsD6RaRUAKGCnbNcQ2TXNEE4iUsNe7rPPS%2BCnTKhsoxOf86fSffe%2Bs5pmr%2FbPsodLXe19YJ16t8auyUa849i2L3wcF4Dh7Nc0efc3J8SCzJY%2Buu0gRehAeedTp2oQ%2FIi4TPP5E4P4Z3LS1X8gMA1HV2kvptmXlf7nD%2BlfFVBQX2c9Qm2bFdq2whAvz%2FxIJvXc3qud0LT57AW0pX80Asd1CIy3cppKz17iixUeIrMu1d2QEwipGwl1hZxaLTOKNkhX6AE%2FV6YVUmV4iZI1bzCo0pm9BjqkAfj1q%2BzEDy63CttAE7HxqykZ7p1rRLPN5yEUrdF%2F0iqo3kqbmoW1w2JNg%2FfYTbjsLwRY6tLNCJFJpMDRIbRu3D3L0pqAaMBOk8UgQHqgR9rij%2F4AN72NhJMD3aQxPDDMqn3CBksiOxIshAf4J3MjFTkaJQwqz4SZsuhuTUKZBlXa8zvdwuVHPGmCZ%2BimcEzUfkZlySRumvuKyLE0trUHYAlmbk8S&X-Amz-Signature=1d48e43bedc07f9a8ccc0ed5e893c1ce2180473866e7652771e318aaf67e0a56&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7RYSTAK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDgRp%2FZUwjNwYoA9kbYbVsbojduCr3zmsXpmzs7NZIhKAIgSCFw%2B44iU8SwjlXaSIZ3BXOGh7OaYxgTqvELTo7jF3Eq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFkLKPSC5eu5LK%2BFBCrcA%2BCVxzvIVAdm0r67XrBl7Ifj5gtAeeHuHjG0130qLLzjYLzWbX8raqELeJJVbzPyUwQVpAePpRB9XjA8g%2BH%2FZPtu8zYG5HU4VxFyxtz%2BHtSuuB%2BbNbyMW7ttoRTH5XgZnkwdZJ3Nay%2Bv9UmsYQhWQZLrUsgabTqZjhK6IycTe%2F4UuMgvBRpOh0lj14k9AONgUdJBdQGLTP7Eoig%2FkKNlv727JYqbqnhGn1lhcjFFk8yuq%2F1gotguKcvedplnrDfvC1f1GbW6PLv06XcMCK4IkQc1uij4mtmKYDp7SZUmrVp2XnkH6hfjyx8RPjw4jw5naGZ%2FQ3XnlwaBX%2BMAAgifUh7DeroxDmpdIa1JJGErNyi8O3VkESmiBERYfxv3IIvxhk8Q%2BmOUmUUnrREPuDjOAD%2FpnTRGTY42o1YiK6w7%2FCD1HnfgqZqEpKkoveG7%2B68OOzDMEwPt0IhFBhwRycz%2FBZQoejQgJP%2BXztxsyiaHhOvUZ%2FXjCabT8GOEPWFx4twe9QGhOyZCirmfthBhZmgOUV%2BVgh8mqSiR22KwAqkNb%2Fcze%2Fz1sFvbwoE7oAUY0Ow4IbPtPxZeA4QsMOEqSKIo%2F90T2wVf7qrTfeLqaaAXNQjUhekoUcZnMuL5sxvrMJ3Smb0GOqUBJSOwozK449fXGHBg8y14UwhpVRdzXWftBrOEMIeeCRT1dkhWz89jcLUyktZtzMAMacYGzhRw%2BVe33SXOBWXxpCi1FblP%2Fc7aA2Ep%2BXeDn79CopIYO3ElbGXkvy2jtqxIkbXqwaf%2F2vQIVQr8a2eVWZh8ScGU4dqsm0FCksX6ih2ozMKZmQoTfELmLWsH7EdFFVW8YUCS3bOimRmq%2BoTwNCm4vzCB&X-Amz-Signature=c7ec03b6b8dec378c8c721bf23bec2addbc0221ed7ef4c522c1bcc8d4d0ee110&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TP5MWEX7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJFMEMCH0BKDLZKU%2BpchIp0JVEGFPi4b%2FPEpJKG4GcL%2FidNw70CICDP%2BandM2f6mE%2BmWKzrQ3jRCXd%2FqFLwApo1HrbmHFEoKv8DCH0QABoMNjM3NDIzMTgzODA1IgwXQPBM2LhsAmosptgq3AM6ItRijAosAyXX6bIr2Mojf5TEVkFfgtykDplpx8dNaoSxfmuyWSz76MYs7u9O%2FkZ56md%2B0MGdBRu%2F1sw2l8yQ2s1RDxov5NanznLGkSQ8hRpTuljfSgbycaVY%2B6zAYBUR8DqAJDIK8MdfWAsA04mhtcXnzAa2gRYNkW3h02XK%2F5obzIEqySTg9DQHgi2J1NvGdJLbiB2fEO0VFryUrJTQbr19RtuZhWekC%2BMVkLhBbMNe%2F4sNJO5Flm240ekY2LI8echZvaG8yBtvbSwHd0kQD5y91lTKp9l3lQMZibAuRLx2I710WEzSBrwxXY3%2BAveM4JCqctxyBs4fnX%2FZoAE04ygptkzXmJUx7zFJFOZmlATNYnCkoO2kMyK18Dk1UKh2PWw%2Bq0clFQH8OvcYk23T%2FAYT7gxDamAqiclCWwHhzQFsWA3IqB60FeKxNhT1750dHRK2Ekr8E6qED32IqpJmxHwUcHAmhjQLFgof%2BG0swvMxQPX%2FmTR2eVfZRHVarlpseP6kopnrkZ8xuFO0oCtb37DhoWhHjb%2Bnj41BX5CYRjvDzU5zHLQxOrHwz%2FvNjCTIgvbUvvfDkomV2GivDa3JOtCJ%2BRNZeMYLTayRoTy4Z1sOKl%2B46XzdOtjZUDCy0pm9BjqnAb5wX1UShjHgRn%2FcvOvwBp6Bgh399lIv0DpcArAt6VqcE%2FUnZfxqMhEg9GZhY%2Bk3USMwjhyq3JwBRb9hsF3dsF%2FtXiOJxBsf5m2J3piPxrP%2BXdM4GnXV4XS1Nnk34FLUP%2BHRl063HsDZRL3d1KftqKGYP3OzV8LkZZqUlfqYe8kbLEuR3bDpZbr1VP9gEBX9y4W7px11gZAuUWryWCgdMdujjvWIUmKq&X-Amz-Signature=5b829dbdacbab64e4ea5481efda068dfa02375c8dcb215f1dc4cb6b1bd504b59&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZM3DSLI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQD3hSKMS1ENeKNEDCfjCix6VmOJl7kP3GK8Wz6FhPZJgQIhAKOZc4EkKSgbvRi6uxX%2BHQLP99E9Imy9gWjHY7Q0G615Kv8DCH0QABoMNjM3NDIzMTgzODA1IgxZGiLFjjDHWBjFUx0q3AMdyRRyu0XyfJmWy2NMOMiHH5sKZNMZUTpZPpe88a%2FZ5mW4Lzc2USpvmgwVuL8WoxjjdiF%2BBudKAUdY%2B%2BXEFehlpxbOzPW82ViDlWxbWRi%2FIz6%2Bg0Z4E%2FaRObnJ5Xk%2Fufp9WcgdpkwUeznqlEI9oLOCdZgpUUH27vZ%2BL8int%2F%2FLQcFoMnOaYmFYkmhdfIGP8LJU8mH3RglV3QyhlUki4952RRqbP3HdAsSkNu2rntabKdqIQ1ugW4xf6waTQejHQXMMOvxAQHAZs0xbIYS5nlA5bpfZyRKdM8dNEJvuXv1QguhCA8VWOx9PASKz9N7TLzfMoG87SkcoZ23h4c9PBri2KSSoRW3O3jinOV5c%2BwxI%2BeTGR8yrTTWoVYW4eKlLDvcXejsYBftkU31nyC7t7qBgQtZ7FXe4etqVu6BDFODkDxzp%2BV2eCnVR0SXOyb8g4HtaUA%2FRJGHLjTEo3cxm7hErMnCpjqOv6iIJ%2BwOlR5mZZK%2B1qpBe9yY2o%2FSqaDZWfCZs%2FfUToC8CJbBQdjfzptJ3GhwnkvcB%2B0IZyml6BYh2%2FEQxbBKEY4tJKYYhMKIk5%2FqDC1B1ARit8sb2ETfF%2BFtinEQUVMhJLB%2F9%2Frvgz8fbXK4CQvcpuBBbA4M1fzCk0pm9BjqkAek8zmnOa8jC%2BAf2jw%2FCZyySBvftZRhhLyyg2YDDX%2B8dXukiJdVAv2NA7P6zzf5lAjLG5vGt2qHuwVfN%2FdVpAfbvoSZab1HteYHtn47JF12ckA5OI%2FTQEX%2F4A0%2BtFSGQn%2FVmjMZCEJNd9cAjIlx21BzjQL9DBmDuAB25EZIp7pPaD0WPR%2BJa7Ih%2FNVgHqHPMEHNwQsu4OeBYPtYgyuP6KuJTyAUS&X-Amz-Signature=5e802cd81040654b42233b05fbd50343f8701ed4d5bac1cae2ba62375c8293d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUYUGREE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIDu62j%2BLE9Kn25Y6yAKzdaspZ9K70OmH6HY0SE78gfPCAiA7YS9pcSrDdzx%2Fp4PYODhkN5ClLzWhVRhrVbALPgyelCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMN%2Bu%2Blu%2BBWQPX1DwsKtwDpNXVNfstOxEa5z8jOm37HN0YXQ2PQeTXCA9vmA4o8LzoMg7%2BcDY4VJ7sBnyaVVBppiDrRbPONtEQLTgrbXsXudNEhUAxtKFjUERqbT7R7nUYWy6the53amxLlfVBjafj%2FCIOzKd9niW7IYYyu6e%2BddFm5BIog1pz40rm7RNI7b%2BHRG0LBiTX8qg30bGxtoxQiKYNAyS5eoVq8%2FJZv91K%2FFn3l5Cmaj0Q5d4RDChh4kC%2BZpFwspC1XI9oAlTHyKL6wTeJsIoamP9plE2RWB4EU4xAeGJRAO%2F5VheXqSgO7YQsWmHkp8HIR3%2Fp1bkxJnOGtS8Wsd7uZnDim2yjfnmA411sa0LPazBCqrXJMj37pBhBDSQBfv3wCGhsnDva9qU%2BwBd4yUbvAtDI5JGNf4D40liyyeWgw6CHgD%2BdbauRjXWrKZBmosuv%2B8hBO9dLAfXWGLCsRMYEMpYouKv43RJx9vMs5%2BtyQJfvslFbVQkR5LjVk%2BVB0IxyXOSKoolBNGp1hhlsHPKnYvZWUnmW%2FWvNPa7o4%2FsPHWwvEmMvE4%2Br0yGKofpePCHcitQ6Ce5vu8jOZWqGdM2kderV2EYsifBDta1KudYPAjq3YMQmGbNGU2I8UobCJO%2BDzyvlxLgw7NKZvQY6pgGnFRp9PESiTBuXS1vOaPW2u829%2F7cV2YlulueeyuDcTsSQ3KnRueHm8DbVZIn%2BuzW%2B6r29knh48Xx0trwvIRlKyZ7V7x2d327jAZqFbeXRosNrfPOkRme5fgEyo6F8jNEnQvXD7BW6Mb5Juf9sooOhc7L6RaIJdl2EimnF7dwoSSbbjrDJ%2FiSzv1ybVJaiemiUYNBri5bYeQbP8liODFQAWTcwMpO%2F&X-Amz-Signature=967a8e92921ab0d7f62e8183b0181bb91afee3ec77522b1abb2c72213b61ee0a&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUYUGREE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIDu62j%2BLE9Kn25Y6yAKzdaspZ9K70OmH6HY0SE78gfPCAiA7YS9pcSrDdzx%2Fp4PYODhkN5ClLzWhVRhrVbALPgyelCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMN%2Bu%2Blu%2BBWQPX1DwsKtwDpNXVNfstOxEa5z8jOm37HN0YXQ2PQeTXCA9vmA4o8LzoMg7%2BcDY4VJ7sBnyaVVBppiDrRbPONtEQLTgrbXsXudNEhUAxtKFjUERqbT7R7nUYWy6the53amxLlfVBjafj%2FCIOzKd9niW7IYYyu6e%2BddFm5BIog1pz40rm7RNI7b%2BHRG0LBiTX8qg30bGxtoxQiKYNAyS5eoVq8%2FJZv91K%2FFn3l5Cmaj0Q5d4RDChh4kC%2BZpFwspC1XI9oAlTHyKL6wTeJsIoamP9plE2RWB4EU4xAeGJRAO%2F5VheXqSgO7YQsWmHkp8HIR3%2Fp1bkxJnOGtS8Wsd7uZnDim2yjfnmA411sa0LPazBCqrXJMj37pBhBDSQBfv3wCGhsnDva9qU%2BwBd4yUbvAtDI5JGNf4D40liyyeWgw6CHgD%2BdbauRjXWrKZBmosuv%2B8hBO9dLAfXWGLCsRMYEMpYouKv43RJx9vMs5%2BtyQJfvslFbVQkR5LjVk%2BVB0IxyXOSKoolBNGp1hhlsHPKnYvZWUnmW%2FWvNPa7o4%2FsPHWwvEmMvE4%2Br0yGKofpePCHcitQ6Ce5vu8jOZWqGdM2kderV2EYsifBDta1KudYPAjq3YMQmGbNGU2I8UobCJO%2BDzyvlxLgw7NKZvQY6pgGnFRp9PESiTBuXS1vOaPW2u829%2F7cV2YlulueeyuDcTsSQ3KnRueHm8DbVZIn%2BuzW%2B6r29knh48Xx0trwvIRlKyZ7V7x2d327jAZqFbeXRosNrfPOkRme5fgEyo6F8jNEnQvXD7BW6Mb5Juf9sooOhc7L6RaIJdl2EimnF7dwoSSbbjrDJ%2FiSzv1ybVJaiemiUYNBri5bYeQbP8liODFQAWTcwMpO%2F&X-Amz-Signature=35ae7e5d6cc202b8fc654041707b693f6309f7d2e56b4dea90e74dc3d32fe5fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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