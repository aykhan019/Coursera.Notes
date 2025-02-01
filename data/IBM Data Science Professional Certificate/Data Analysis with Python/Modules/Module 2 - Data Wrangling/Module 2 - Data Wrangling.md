

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWSEVJHC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKzf1GYgE6H0Iq%2BB6MRB6kG2q3w%2FHulD6K0tH7C099AQIgZalRoMzt8EfhEgz%2FKhwm0W9QTjAD3fkbLwf8%2BuqhqFcqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK6fDqkwDsgfpibbYSrcA65vVDj5lMLuBa5oXjTUwmSZ%2FLs5wc9U5oJToOQAFTJK3azY29nB75M%2Bw4nV5mQCcA42C3GvKThPOBnLL3CSFhdxNCXkj832%2B4iUK76HKz7Q2HL4Mu4F0m3G1nlSDRAnIKkkaac8PLgBR8%2FvZOToSSl10ih0Sx%2FZwu1takV8jYVXQrEmvHZNJmMjOOxN1cLVPQhN%2FjtQ4AmtvWa2rFusmg%2BF4YciEhiZzwqD69%2F8JseaHuKhR3HUFoLKHJKIleMqhEdXhI56FPUkTNGvwgvDgsOKpwUtIaevHKIw8ljFDCKmJKaksqD7YlOWutycTnlZ9fOoMXLBxwwSNUMYXasm6PrVTHHRitRj6k745LBBj7zXtKLmyTmGB4ArPnbXo721BIyGBS23kU%2Bt9Mbdkjhnj3PHbGf2DzrPwrSySitcNqgGjZny%2FFX3LqK9Lc4f%2B2KRGMJnIVdX8K0Gjxd1bDUPzP98DWxm1Wdl6lU2ppvfk%2FoLjrqnRFWcJNfSs1x2yqtFhb10JS4WaCwVJP98QG8%2BcETiNhudCzuRReAaQ7lM4v%2BVx9o9UBgbHtq3KY%2FG8wUpiWlGgkh6A15f5a7FpUuKDhCmbxb4m5RshfwEOFJGTRTDqVSmKdXMSz7xhaz1MKek97wGOqUB5TgBbuDAwtQ6btUR31dqCWlZHK8%2F0gKofJmp4w5jHYjZwjhbxyGMmlDaqyU%2Fow9%2B4xF25JDiH7zmDtLbc2GudHja3D5eQuzixYSbWr3upQ3ssgJ%2BCxPlBW8wiTFTeLs5Fl5TyXVFsnjmnvQK9EDPhwezLXHIWX1VBDvx%2FG3u%2Fz2lKThE6xgc8cnX3%2Bv2XyuWdETs5cmuR7tGpY%2Bt9KtUPcs1B3bW&X-Amz-Signature=032cdf1a3c63c6a5d7597a48472009550def39234c99c5179b3b48c6fb2eb980&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFOPFFWE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHheANYQPufbAeT9ld6v%2BuHnnBgdCApqrBZ96Tb9an0RAiAOCwEA136OiUV2rsyFmMQZM7SzbVwS38BILr2%2FLUolBSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjpc3S3VbK55mDB58KtwDbtV1FtWkfFqc1cg6pV3xluafLwKVe1sH5Iqk0TVhnWNz6RYAojwDJ1G4JILtllmx%2B8vagj%2F1KFwuanvsczdVmqZK%2B9WybHJNCMVLChU%2B1dzlZvWiiPYy61fY7Shwm2WDWb0BoDMsgOP1ioG16ItFATs9yPyXUDvG1NsnGIotRm1%2F6HjO%2B%2FqcOFwRqhve56i7kXPfg7Z36WcqeawKcP5ulqruADdPqoQaj%2BNZmX7hPSTLxuD19h53PtDfu6nxamGvibV58UXI57dTGn4oLEyaYTGE4tGZk7RMUs3cIr7isVQiwla9giK95rWM6xwR1PR1kzsr8O9VhjmM2bP16CfGD1tOEU5kdd3WSmqTrV9ood9oFiZRhe8xEcOXX3TpBiIJfw1ZAYQ%2FOPpkFIaEjQgKBVxm0zC0qH4ZHzWo7vPph2JUA4QmyElLNru4ZJ2cw5UGC7F%2FgN%2BNRncpW1Vqeo8PlE31d7eM%2B22Uj3THGcFiODnqIxEvV0WwLeZS5NfYn5XUsPgR8jjvcWN6Lvx%2FFpR5WQJ18G%2FiBeZOYMN4IiFcQqfc3Rm7s9%2FrAJ9Y9PWTS6SzgwDQflzD%2BCm7H4w70k8m%2B19iB3s6tynG2sXxlHjR6CtrIGGU9uRocd2xEvcw1aT3vAY6pgFdV%2FX6adPs9qgcrh0t4tFrFk0iIraJB1lLfl%2BGNyut8Ho7iIcEuka5vdXHFoPnu0TknkqEO%2Bl4VTRR%2BgzhntiUUlkreuASGtWpNl6FjFs3VZ3P4pt4VEEGM7xsO43DlRl41TNWgsDZgr7TR0f91lqF%2BGMspPvglSSwHpOJXmxtBrWgCVWyOkSsRz1ugfXvhihVaJmA%2FLJLCsxr0YC1v0AGW5RxIppv&X-Amz-Signature=e4e6dee257fc4f6b1efbde73395cebed775a4a8fc43e297b4ae602b1dfb3826f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNYOKZ3H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEWXfwZi9SEQ5pqx%2Fhmr95XkWcU3B%2BlFaC3s%2BllqU2syAiEA0qMHXyjS%2F%2Bi0bw7V%2FvADjlDUTFigc%2F7GXVPVojbyZ8EqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMtBP7s3KTt6fhSG4yrcAw%2BeLdIPpmCfDE9EWWbrcpTROSZTx1XEdtL8IgnXwKKoTRKzGwiIsv%2FvMTj4oZ%2BOxghMsVHGpSd0KLST%2Bln1t7dRvs5IBZPozz3BFI8nCwj4%2Fm61vhXNRZocP2fo%2FFhXnjfspbcTzoClJGuz7vyLJjJNdjWbXXUsu9WUHTefKRy%2Fr0gByb4TMvsI7YGF4jFPYQ6B3H3eQKw%2FiRB3tGt5NBlUWLY4Z9MWKSeKmv5HjCgjLkcNBEKFOPA%2FII6W%2B2QmFNyJdIlXPzmhpGxVTYxcyXJaFDvgFGu7zUOyqNubP%2F%2FjsGofPWkuOkfR1mwnssXPXtDxynIgXYvTjke77uf50i8I%2BC%2F%2BHnaFGaBQ73xBqo3pKYZPLM8ArVR0KEuRDuwRLgLBHJ9ijc5qwbAl%2FoNHRD3j9KsVVlJdbWrncQxuYt1oDCEr%2FkiBe1bnwoU5LX0BkVBTOLt0hMZvl7zWwZW1itFVCDlv%2B%2FEOk4zgfDawQcT8bpbOsHrbvqKeHPvh%2BC3M%2BeDjLOjdOvM3%2Fb8QC3kZ6nKfF8n3odk3sztS7kWs%2FkYKG%2FYCA5%2FGnutKcbZx3SrCK5aVOSOU5s1FE76dHsN7IYO5oLbK0OFbPUbNdjX7a7v2h7zHTBIGfM7bhQBeMN2k97wGOqUB5Lozv%2BW7Gm6QyKPKv1%2BQT%2FxsOZ5T8vIUooK6v%2BKGawZJGARb52P7VdYeZGkARFDDifGwcPhpNTdymTNEObVDwlX5Q%2BPCylYtA3RFQJaeoVabcDPhyeC%2FicVD6ko30sKi2jJbBTyRRaqAFTnMQkXoYgiln3zVb%2Bj8UohKiyh8NCGW0RDUVljlMWAxFBtykJg2gpnjharxVLq1goQ%2FSVJbvH%2BsUz0T&X-Amz-Signature=70f15b419995d054702920ab62936a84daedf1a97495521e600c4817069531d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PHPX4QT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL67riJYu59aEgpNRQgVcTn%2BqjHV%2BAB7zf4gMxcV%2FbwQIhAOTyEqIoP7dSlqA2IYO41Eiw1ptBLMUcryMLWar8dlYBKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJPUp%2Fs1lqSB9MwLcq3ANsMX6g7Q1Qbql09YkLn%2FtAciKwfNNVJ9z%2Bo8p8KEzGR2WClFgy5f2RBD3IEMhdEBPaY85%2B60JlpMra9LMjSOEPhZYg4MqQZmeqFR7R%2BTCSbiH%2FRjMW12CvtTHsrUkXb22vGBARgkpRRd6WmLT59UCkiQOE4K7gISbovMttNSZQk5FMxENOmhc6ntfbCO8LoXxOz4yQMT6TYUn0DzWuKUimUGoRYnhhdE748o%2Bh6XBlyMWMTKC0Re5WWJM6FGB8QH9yF4ZmwBlk0NIwZym%2BEirtWFJvZO1O8Y1Nt6c6Rme1FPsjh4SagBX36jn8dCjNr1yz34F4ppyt30%2Brvg6OdS74s0bQLIE%2Feuo28aqygVvjwIQGiTlNvueHaZla0nKTmXwEZRhp4Qc8s41NlzBdRKKQTzsOYEK4%2Ff3DQ2sO6J%2BV9cf7QuTPJKHzTIEzdOdY2nNRBFi3beg95go4iiquVts2GHAnLuU0MDaD3gdcpUnP5U6oC1%2B2qIiXzVKlyyicr3%2BJzOJqkrGGsAIakOzISCcG7WWCLrEvjOSvICIy1NaDOMCr%2F7b8fXAgY3V7T5qA88jqsJ3Ea4xpZGUDMiz%2F2RLsfxp3ZLkXmub8QCrkyDznk%2ByRCm0B8wCHt31G%2FTClpPe8BjqkAcwv%2BRJQjhPSfPJ736DkLbyVa7t97Aqg%2F3Zew%2Fs50epwkpK9mgd5%2BYf580iKRLrUweY6n7NCax53ELCFJGgs4%2BQ9OdKlkjFXHoGDsejWelKFi7n5knbsq67rwdIDSrLdNNBEtU57E%2FG2AxIaN9LqVbLiR4P1y6MXGNFGpP0yguJu1A5wb8PccJRWu%2FrbS1SfxO0v9fffNeuYemIgx%2BJmWT2e1ssG&X-Amz-Signature=cf360dd141b5a78ed83340889a96153baff6443bd5f9c81be34cea7767217fee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q36FUARQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEPlLI6j7k8FuwoSIP06wzmH4nmP3QffJ9J4cuLcPXJgIgSysj8I1uonk5Xcc2AyRhrur1Zz%2F5cL1Xu4v8ZzpbvosqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAYxpxid1xRkZQ%2FjOSrcA1HCfJ1W2iqujnUN%2BNAWIvYVGjMidahucW6PX0JM7BcGd1HWk6ukUhHjXivKHWNsLhx1bZ5ITnpB0Pvw5tYBZlX3Pj7U%2FvawBwAhU9LxPCyPteTQQ9kbTLFomewMecCX8dc%2FtT2ogZQRdfJjxCRw6BJ47ol5YhaLk6jTJhfInqncUgVyVW0qKqoNv7odHa3mVHehqKvUG3NOsJSnOFx76UeIRvMDeCXx%2B9GtYWSxc7aGN6ov5EHR5vvdmLzMc3nXMaVUJma0L2GwpoXQ3VCNPNNmGen0kjCimtvyZkkYPlewkakLV%2BGNFJ%2Fpy3QrcgNk8ABh2TxeLeuHqA5Z4W%2FYC%2BKcGusuL3SwPiaBSmP2J8rgZG6cqZi6AWMxon6DHy7TtZxTYHtT70Ou4qz%2FK1%2BVEoKMOm2Q6s6YinIAGAWXsGZdfMzP3YDEIdq4OMrj6YdS8qimWf9wVf8eovUuek8rOc89fSKuBMqvIW28lXWdr9F3fnCSJ4E11eGaB3u%2BKbyIiJ4oykkxngso0LOF2qFxoY%2B%2FG6Mtsh8pSB8Q%2FJIng%2B9FJzAzB65xCu%2BQfdfetVO4O%2FfvYvVS4UNm%2FWcR8qulHEHwZsacaZSQg%2FeLjV7BYp%2BcG0p6jmDahHo4Va8IMNWk97wGOqUBh99y7PHoV2BLTtXOwuG8W%2BPz%2Bzm8Met9Ip1IRap0xzGOuERd2oUywwVJ2zJZdd1Bd%2FMllmLkEI1ib5f1aivq3oniKyOOcUBncnjv0%2FZWnjYPM54uz5duKB2Luv2zr3I6MPccu3rg87VMytuixmIzG0MXj%2BNCQHU5Y%2BfE111uZhdSC9HFwJWbXZ7Y0T6QlnWJo0YjA1yMdHFFMM6%2Fl5L9omBDHzhh&X-Amz-Signature=66849c2333fc9f270e15d3fca9850c28f9eb011adc1fb6e965484b0f863bf038&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D6AYCMT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2BBET9pqqHWUho9jpJNocwZZvqOASsYtaPfbMjuxwzwAiAZv85eYjUSW5BylS5KNWTET4qygyCB5cNP9E4J0HYzQyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDPLrkNfARZCpzWp7KtwDU8WpBtaKPhljNCR%2Fpq3dfIl6rywYWttqddfx8wrmKHUOG4MwK%2BxF0QiXEmpXeK4xe0cgj2pJ%2FUnQBjvUxJFbJrOMnOTbPyDLeaYA4CADyr879DbL0pMzKUfR%2FdTXn98W%2Faeqv3J%2FWYmtjtBrzUTcDZket6aN561vEBxRAJHPl3RjRUhYu7hjUErzEchkTZqCafpcoRuKb0z4MbZK8y3VQGMl6YLnnmu7xR8UFAm8g3nEBt1P0PQ%2FByZjtjUvWfbV%2FrgRPocbrGhAcu9OB6ZGbhVxY3zmpbmFfaSY0h%2FA4yzcN2%2F0xG8FEvRLJF%2Bf7BnafE39%2Bm3LJoBYqR81Z9QB5T8MY8w7SKajX3Z3S7cRv20%2Fy4uO8J8s3D4yd9LVZzVIUozkdu%2FD3h1xcg3vycoiu1XL2Sugd1VvXGXJXq0xB%2FTRK9HLLghQf3wv8CUZSJ79%2FTKAf0i5dZ2oKXVHtsc9kN2AuIgE5OKe%2FkWPzCB6ZLg8fQ7ZkAH6B66yBN8WSIvt9UffYAdOIjvQvfMMBv8GvP3hIoTWn5rLqqCcXnOD4hmYYO2%2FuOxoGBSQYA7We6CTdfSxr%2BaAOUXV3oxdd29I5JhfPdQHkFNuuOOSrxGzUmPbi4IQYewZSbAhJIswyaT3vAY6pgELBKHyq%2FcAWP5pTVsLXW8HWYfa%2FvW00kdrA%2BRw9Rz3Fp2FkD6ZY%2FvCgjWsQNJ%2BPJhZqxrvgYvq9CsphNUbPzq8ZfKzyW0cYu2LupjiIlRkRJJ4%2BG3MPlEccEuh1a4DK9%2FrFlfb%2BfOzGFojizCqMwTblgUApbtrgf62p5%2F3gDqm9%2BaZiSwFPWP7FU36%2BixtMXD8IGbQlJyb%2FER8%2F6dad3gVizos94RE&X-Amz-Signature=edf68d5844e7d72b0a7fb079ac4d96f6549eb25725c7acfddac83386794b092c&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYQC2HBV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFC0dYyl7KhWnAHf1od0zy56kLamuskgPtIRDUioQELAiEA4vmq5ce9JmNyvPdgPJ3IsKD91ZUkXSusHbijKKcoG3gqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIodmvNwyWWsNHX7uyrcA9iG5%2B7iY%2BEDRy5CLpDWhSqKIvu0Rhw5rzcm%2FpR55NW8SgEtC0I7aPGJDlZy%2FEgK9P1VD%2BtFyiAbGBiI3CLhT5kJcDreEMbs0aZ8YdVNor7GTZK4eHzUjP4DCec3fhwo%2FNzb%2FcCwh2X3%2FBp1%2F%2Bv8j1hIdYgFQiHXGVdfvR1g76Cc7ReNRHrKnJZVVVCLe6KalbFhSJbp%2BJ8FFnOvBdPUoNkhZBtg4nIpU6GKjMNYNsezlGgZA2g2r1g%2BQMJF32U00xbjskM4QJW9C0qRM9dlPpdOa1JFmnvZCZFZ52BshqZdx7CveEOfKfChkFTHlnlLy0f8g6XF%2BQMYXxmMzpl8fS45VK6lrQWtrDjzJNB4XPdpg2PRx2Gshr6wqQntMUefwnEU76NtUUT%2F0Ro5M0wrZgPp1guyU%2F0yI4yzi2cC8OZTnY4EPekM5ig8HtMGHV%2FuuSNJwg72ABuNhsYkgpdMxpiUPvU6O3czaKaREyrK94InOWtttMMPlmqXc9x2PDdHSRJay%2B4nApUTevk5%2FNTgKsWLgRdSM0XfYAh3g2yEag6MKvHCgzibGAATKvIVk6AdvQzVm0AnabX6GOHpsUsyMSERT%2F%2BW63bMnzoY5MC7nlFEazV3SJ3rMFANECAnML2k97wGOqUB3ah7Fg%2FnQYt5RBggKw%2B4fV4OnkTi5YeQ%2BwpHwk43MiAjCoiNml7vvYpOhiRIfZPbExzr7B7ADIIObeo0zebeXu5vpHFwEMdpJGdSKpvCzLFTyjBqsfmW2VJEuOJ8wF0V8OmR%2FkkLVWZ6FAWqh3q18iTuiaPBc0T22OluHmHmFDrPFCviPe4QUu4junSPmgSajWm2BPBKsqT0QiAx8Ow8j7ZvKWFP&X-Amz-Signature=4b23d708314209239fbaa4edc031358977e7b3ff24af36a9fddf2a416f9806d0&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646FFY5YW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFOQHxLa6JuGfF1gNUCS9SFkQ%2Bo0Kt39NOEF4W2QL0fSAiABOUu7zwnsE7U5igN09vpJtzN56IrluT%2FJDbup80EjrCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMCgLrr7R0xz27f2WKtwDEfr8lUcX0reHlcOndUMPn2XMiBDCkpICB1vj1h1GGtZ4yPp%2BD88%2FL0b7wFpEItlomUWiMnyUjw9ymYksE0hY4wsJHFJbtl4Jyyn%2FvpSakejhdaimGaDYo4v7hyn%2FphX0Kar%2Bb36xaLc0zygHD%2B7VBMwvFF7ofLV3mn5Nf6SRdyqimNBXpv4Pl8uDiKH3zah574os9F%2BVU925IYmZC45cDRgEF7JWNSfKe6PvcpnDCUfe2y2O0vDZBE2ctBFknuflgPEKQslwM2eZa5iggzsmsN7FOs7StPPSvbONAwi9Dd0%2BUz%2FD0E%2FGV%2FqJhGT1qk4VCCo9tG02n3UX2KCBkps8Ps0qjABIheqTKN9SbhZMv4Bd1PAqH1ychdax%2BrpeHFynTStOCc8cHI31cjJUKe3Zs0vQBc9zPav%2BT%2F3pnGoxm9hlF%2FIlnHMoR%2BZuXg3EhI31vsoAT2VtvzEJLZ8eVETQHXhPM4w0%2ByN95dYP0ZQPBctqg9F60bxREonoSILzfXhZpjtp4MXIKoVufDBGjBmyoa8yrzBnVHSWLMlkHnvjaJaS9SfwiBiZZzdJJ%2BLSCxEipjTOlAz5ZzBtJFT%2FMAozOohk70aFi%2BYkFrHljKkbuaYbSgXay0td3wSGibQw3aT3vAY6pgEjI3k19l9UGR7lkOi8gMFfECpTdMGBNjqZMWatMfdZO2Lus5p38LyzVFbPs8GtxvNMVvIgkoCQskcEx7D4BhQhwXRdxzEQfqIbpjUmKHpjAwWvZcYB84B6wqNzjhB6ae6APx3owUDIm9Y%2FJivvnZTzvP1NZ1GlTYKukpdzU36i6zdXwVW1ROi1bGbv564dTHCPcyMwCOtgAefts2dROxwD175FQsUG&X-Amz-Signature=be0f7f44502e9cf3342e5d9c2bf91b622116ef3b6bc1644c9b0a5941666d4010&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q36FUARQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEPlLI6j7k8FuwoSIP06wzmH4nmP3QffJ9J4cuLcPXJgIgSysj8I1uonk5Xcc2AyRhrur1Zz%2F5cL1Xu4v8ZzpbvosqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAYxpxid1xRkZQ%2FjOSrcA1HCfJ1W2iqujnUN%2BNAWIvYVGjMidahucW6PX0JM7BcGd1HWk6ukUhHjXivKHWNsLhx1bZ5ITnpB0Pvw5tYBZlX3Pj7U%2FvawBwAhU9LxPCyPteTQQ9kbTLFomewMecCX8dc%2FtT2ogZQRdfJjxCRw6BJ47ol5YhaLk6jTJhfInqncUgVyVW0qKqoNv7odHa3mVHehqKvUG3NOsJSnOFx76UeIRvMDeCXx%2B9GtYWSxc7aGN6ov5EHR5vvdmLzMc3nXMaVUJma0L2GwpoXQ3VCNPNNmGen0kjCimtvyZkkYPlewkakLV%2BGNFJ%2Fpy3QrcgNk8ABh2TxeLeuHqA5Z4W%2FYC%2BKcGusuL3SwPiaBSmP2J8rgZG6cqZi6AWMxon6DHy7TtZxTYHtT70Ou4qz%2FK1%2BVEoKMOm2Q6s6YinIAGAWXsGZdfMzP3YDEIdq4OMrj6YdS8qimWf9wVf8eovUuek8rOc89fSKuBMqvIW28lXWdr9F3fnCSJ4E11eGaB3u%2BKbyIiJ4oykkxngso0LOF2qFxoY%2B%2FG6Mtsh8pSB8Q%2FJIng%2B9FJzAzB65xCu%2BQfdfetVO4O%2FfvYvVS4UNm%2FWcR8qulHEHwZsacaZSQg%2FeLjV7BYp%2BcG0p6jmDahHo4Va8IMNWk97wGOqUBh99y7PHoV2BLTtXOwuG8W%2BPz%2Bzm8Met9Ip1IRap0xzGOuERd2oUywwVJ2zJZdd1Bd%2FMllmLkEI1ib5f1aivq3oniKyOOcUBncnjv0%2FZWnjYPM54uz5duKB2Luv2zr3I6MPccu3rg87VMytuixmIzG0MXj%2BNCQHU5Y%2BfE111uZhdSC9HFwJWbXZ7Y0T6QlnWJo0YjA1yMdHFFMM6%2Fl5L9omBDHzhh&X-Amz-Signature=0c596324612846a75be08ec725b00db4be22c7771317c64ad9cc80e50d949b84&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMNDQ4KG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHSZONbPArL3%2Fq%2Byv82jU%2FHqsseANKMly0nJCFdx6Wd6AiBgI7poLQl%2FwN7Aeox1%2B9RqF4Xh1QRxZPAhegq72U5elCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsGhY7wS7qnoEIzJXKtwDCe7Gi2WyUC33U99gHYTCenZiFpWG%2BtbAXc7syhgvb%2FHrR8cI04AclWaHq%2BNkFWBtQg3YzByctTM6QKrILlGCkXabYK%2Bfxj8hyjb3%2FPc806J3gTxbmvczcrHzT0PKsX8v4MOS31BUOyPLvEeW3%2FaEBhawgp6UQ5Mg5EoUgLbSSy89CGSXg4TRc7Okcn2spvSSUx1AyynFr6DImtZ%2B18iRIBbPXdVROcvAjw3BIiv4bE2FjIkQZ1pKZeCKkuPrDdU7okPw2dJrI%2Ft44E5lixyb7aq971s7GNkv6dWAKUrHlOxOtPgSaeI7DDbpFRQDHQ3sgrg%2BPwrgBEjwcKXWF0%2F5QdidfTtxUSopoA%2Bu3UG3AQBySEPSsJvQaO0puGzmaQ3XH87i0Vcil61BOewsyviOugJNnCHVJUuIcW1HBP96WwaFKbNjbCzDFM4Uv1FWJtaWKXZXvt1b2i9SVKSfaFK5niFDYKg8kj8uFl7OWdXIq4YLBllQ8Z1Ok8aUtJrXZ8rh0gbIkcMTkGyJrXuBIOo169cuH7L4O8mTCxmLy4ITGI90HsxZ9tjYpiC0gxXFyJdyF%2Bglfcr2uqozISjM%2FD7b%2BxJxQrss59Eztd8Qq7XawpXVPjpIOP0TmF2gtlMwvqT3vAY6pgF8bFAbwzLJOnipa8RoSQidCT0PxuRDZpnA64MZZapBHjrvHnBUAMIbuPdj06X5Jc5eNu3HXd5E2gdX8imOMUnQhKHJ9qAGp70kBGj3k85WAGsTeFxkTLQ9jQaW9qm4hc2oE5nqgUs8HKObs%2BUY5ffphy5nBOgP8UnICLwYlVFTEEWYoq0FE0fkAe7CJVoCEPsWJF0ONIMiGaVsmautOkSwciHPvYMe&X-Amz-Signature=569e41be07e5ea32cbbfb5b6459a2b696de4cccbcf4b7915b9bf8195974ad01e&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMNDQ4KG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHSZONbPArL3%2Fq%2Byv82jU%2FHqsseANKMly0nJCFdx6Wd6AiBgI7poLQl%2FwN7Aeox1%2B9RqF4Xh1QRxZPAhegq72U5elCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsGhY7wS7qnoEIzJXKtwDCe7Gi2WyUC33U99gHYTCenZiFpWG%2BtbAXc7syhgvb%2FHrR8cI04AclWaHq%2BNkFWBtQg3YzByctTM6QKrILlGCkXabYK%2Bfxj8hyjb3%2FPc806J3gTxbmvczcrHzT0PKsX8v4MOS31BUOyPLvEeW3%2FaEBhawgp6UQ5Mg5EoUgLbSSy89CGSXg4TRc7Okcn2spvSSUx1AyynFr6DImtZ%2B18iRIBbPXdVROcvAjw3BIiv4bE2FjIkQZ1pKZeCKkuPrDdU7okPw2dJrI%2Ft44E5lixyb7aq971s7GNkv6dWAKUrHlOxOtPgSaeI7DDbpFRQDHQ3sgrg%2BPwrgBEjwcKXWF0%2F5QdidfTtxUSopoA%2Bu3UG3AQBySEPSsJvQaO0puGzmaQ3XH87i0Vcil61BOewsyviOugJNnCHVJUuIcW1HBP96WwaFKbNjbCzDFM4Uv1FWJtaWKXZXvt1b2i9SVKSfaFK5niFDYKg8kj8uFl7OWdXIq4YLBllQ8Z1Ok8aUtJrXZ8rh0gbIkcMTkGyJrXuBIOo169cuH7L4O8mTCxmLy4ITGI90HsxZ9tjYpiC0gxXFyJdyF%2Bglfcr2uqozISjM%2FD7b%2BxJxQrss59Eztd8Qq7XawpXVPjpIOP0TmF2gtlMwvqT3vAY6pgF8bFAbwzLJOnipa8RoSQidCT0PxuRDZpnA64MZZapBHjrvHnBUAMIbuPdj06X5Jc5eNu3HXd5E2gdX8imOMUnQhKHJ9qAGp70kBGj3k85WAGsTeFxkTLQ9jQaW9qm4hc2oE5nqgUs8HKObs%2BUY5ffphy5nBOgP8UnICLwYlVFTEEWYoq0FE0fkAe7CJVoCEPsWJF0ONIMiGaVsmautOkSwciHPvYMe&X-Amz-Signature=52b2d06c725bad199e1e8440d2b7e12b9a68e9ff5359a6090428473851a4c07e&X-Amz-SignedHeaders=host&x-id=GetObject)
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