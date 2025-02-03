

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHJKGYWO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDb9oxZ3qgM0qKuTpOqi7Bqy4Rtibb7x99YQN6baYuTMAiBgw041lP3eJUoiN3PIqgRv5HFTDazOUOL1P0HRebepPir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMPlOU1aeuIFzrULFvKtwDGQPBm7ptDyF75DdwjODeUfceVHXhbkbzF7IWD%2BdhMwcRbq48L2Fmgg6rG8siHKEv6vObTClvMBYZq%2BS4JFicpOEhpXLQsqSc%2FoxCVjsn0aKEKMniFPt6Q1EGgDvmAd5BZBFXEy3D9silpwfnaaHPUDjoHvoIdLQKC6J0iJYWoRX3ZMDMdT4VznJoD4grrtf7lA4jSwsH97nhPUDg9yb3cKS8z118ACeb6J2t4c8d5260L%2F1VII0MPdY02DBQKKVY5ixGyKmjh5SQSMhhLmj%2BpdLtuN4cVyR5Pu0vXYUen35X3dYfsVDSpp2xotv556rR6uYhktNKVQ%2Fcvi5c2ZzkB36f9obaMyBh2wvduZ8PhnqhT8qDScFlRTdTABE5uO2OV81BDz5yzwx%2Fi9YzVtvVhpuvRbuCaiNMNiVd6dqJ1sTaFftGfdELLEpYmNtRrWIuwhwA7d8AU5fjoz9gG00ylXv4pL57%2BmhKmbbEfr5qr97%2F4F7WVlrFGJ1Qxcj6I0261PL2Sr49ViWQ61NQTO0gSX9kpa7lUREFOz%2F%2BO%2B%2FGJ7cUFvcGx%2Ft8ztWLnjOduXWbC9k%2FVoBQsi5eNvRiesHYGDWAEktvo9k89rw7OMjK%2FZw5Rkf5UdGipi%2Be0CMw5rSCvQY6pgH60JHekHF5SbjLCx5wrY2hBgMhFGke2kR22nFjYvZaMMmhRrcKa0rdrV5uUSFljXC%2BqGBt5dw7JXgMQ20L2XOPhc93h0WEkAfDSfJOHn3vbHaSukk8pnOb%2B3UqqowRXKgx963UgixIs7PnDaAYJu0sw%2FaPaOsfvwTgr7EmA1Lm656aQiQnAJjjVmZhqn8km8jl8EiFSkPM1%2FAkIhCNcFtIAs3Ddbta&X-Amz-Signature=a7b1e25b4efdaf48bc8a46bcd07ec6cd9e1151311bc80619e0d38b5dd32f6769&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPF3KX7G%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBniasrBYbVfsu84xBEkBSvEODFWEyPfU5Gl%2BW6vqWpFAiEAqjWNhG4EqTd2veuI1llWQ5KgbhyiHo9x1T5p95EUCzgq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDEFOmFY1OldtQkLA2CrcA%2FfePepymp9%2BBi2kh0YYOAX7Ah637ObQd2aKgU3SBfdokknH6UNbK48qDkR6VRjVlBTS2XpE4suJ2xO2WlG6nSC85GxBTKNjoccryhkeVY9Twap0tOtTzyLhwp5ebpM6UDLgFPRVZC5yt7T7cZwm9Mk%2FJer8DeM2tjLF98zh4ad3N38yijneh7e7hduY%2Fv%2BXpYuxd12EvHnSFk8OBJuOi8EMsHR2pOsDPmLBYaks4tNhdYgdjoVQffK36v5eoz5TvqpHZXkSkWiF6eORcvwoHMwaMDw4iBhJ1FfLGEQU83jg6byWeTqxoDUdG87UnocgP0XRuriAtegtIAg4lY8Ynhy12kxehO3uwAiLpGVl0Hl7I4jT9AIzbqwmUzRog3xAR78g%2BGzP%2B3S%2FDIzd9qNf1R64qu2VtK9ceLnb%2FpXb8%2FCVR%2F%2FNmaOYg2A4H4UjO1yXUC9dVx%2BUYjQlR1ZPxfUqX7g%2BuWhkPagjlzJytw0js5wCB0SumKVrESU0MRgtsrGnm881rMwRtPNIFW0H%2Bp2iSRusa1n9AOnVjiIzveq%2B1v5QoaE7Q%2BqUZ2PLf4f5ixB7eTYzfY26%2BatD2Jq3TS5PrQEtVGOjsTge6VoQoFqLdbD3pGu34DickPbCK1M3MLO0gr0GOqUBFBgQsEiiHZZx7QmgxZ%2Fyp05h9pVrSFSKvowBHhkBFOxXMJwGCA7YiF%2FEYf2hgHf3j6C1q1aTrHO2y%2BrPMITs4VuACUErToj7qJ9xTbQT3M5BKEbcKHSTsQm3bATqu%2Bs%2Bb1Rg2OejWfjekMC15AtIDoNozalfUOLWGWEdKTwi86SvsYFx6cWYxJvObLg84JUYPo2y3an5FNfIdBgoRGRx0R6mdTzC&X-Amz-Signature=dd10cc5b532ae1bda73c1db8dd376b22e3bf5003b04aa3b651f2ceda6e07ec6b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SO4UN4YW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzO8RVGLTNykaLf8nMxnTsdJntysmM3K5O9l6i97UydgIhAOWstdQ895VrAuRCa9N8yEa5%2F%2BtIsZi%2FPtYsI3UrGosvKv8DCBQQABoMNjM3NDIzMTgzODA1IgzcJosszmAI8jPirhEq3ANHlPO8b6yZtHqEeB%2B%2F8HkP1tWQBD9FpPynkgo6Fcfj6pLLPU4ZkHBkiG7O6bWJgoI1Y3wxU5iZhOv%2Fw7EiPvuqpnz2PfSyvooMhGsEBsvP7vsDzrrn2FEboOILoVh1sWKvW8HqMZ%2BWvyJzuZVRNKT%2Fww%2BOKvUFIPHOZl6niUkJt3S1KWFG3gUTUNfp5k4S4DdTR%2Fp6DrlkfqsxooKfu6sZgKyQnuSwjgQHFnfvEJS2tbiCLNh5U9viEkk%2FLokUBBL2F33FRs9lGy2tB36wPyqsHHYu%2F3pbqqrDJNudyTZmLCSsztMXUC2OIsaZiyjKhjetVK1uVeDXxIwqQX%2BRzydIKU7BMvxM0n3P9j84FzP5zzhgQA3ma%2BqWPVqgoqL8yW0mrEdpWQdn02RqtZCGsnT%2BOYGF36IeigkNHGeksqoHk73fdv3Dyci4ZIgqpurZs0yIYTvIKLpVkTvx2QQGwMRvM2slFPu4ny8TWJ8JMjlZa4lPEG5kvGdTPs5HOeY9YBr8FgbMoM8ZYMUGJI08%2B%2FT9vj%2Bejs1ErjPHnE0%2F%2F%2BdKfjCB7uorb%2BBoSWpiTlmMaOHOXD0slFZlu%2F65S3ue9iFsJ1r94d%2B7rXt7%2FGm9KyLWN0aI5llnMwCo0iN2gzCgtIK9BjqkATwHq61HcxtEki2EWHEvv3tMk1QdtkgAVzpyK%2FgQJzygWODfiBb5eAzWOcdCBBT%2FO6g2mSm%2FXvacuIW4ffqB2NPb2yjLxoNHprBr0FGJ23XsX3oWaekyCplrNmelbzR81wIW2rjWt%2FIkDnekI30tuX03kyqWfHePk4gd24zIdSYiOJ3LEuwx55akZMQNQO2A5bp84QFSNZuZ9Z%2BDnPOjxBz8G3or&X-Amz-Signature=a5368c165c38cb10ea87d3c3f683dacb8bb1ab97cb31f5f24abc9e043966db77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPTEARP7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqRudvuTylBF1bgd%2FibosHjA0APk%2Ff5zyyD%2FZ7%2BFFwfAIgPDdzdNPBETEo84RNVBEirxjIblHCJZyzFv6cdFJCj%2Foq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDFAGxVsi25bxKKyRbircAzup1z8qbUCQk387vxG16uWrnZ8JwOq%2F3gPue03Ig5TW7hJ%2F4yvmiYvqxePAXIvCY7vauxIMEF33QJqt6LSNvfj7snMUiZFDmEFAuBfURTSG3N91PMfM0qkeWqjdpupSC5cCsJHDLQUD%2FKqk0bI2iZCdC9juxBusXsCvWldC6csVPr6A7fTO8rCrBCHGu40%2BhnTYxff6kW7xyoELs5I4WXrlfWm8taRo%2FlucJv685p2WPs9b8WU5nOQh2AIWeT9KHew3Ruv%2Fz8ZcHYhsnmSQOXhrA%2BWoipxgvy%2FAVeZSsQSnNozc0rLUC9RygVIRCZz432oD9uLHTeM2liHk0ShO86hsojCwA04PDhA6DkYk2ijWHboaCXmsPKXD4kxG9j53RB%2FnxLP60THGsnWtmz80h337v93ydjF%2BPQRSRbNFa1%2FWDFCCFotT8K0xWkmblwIdUESGBGEMiTy%2Fw5o0VCuktmNFZrUT2r39jBGxv08Xq9zfpq0SIYyV33wiGbvcSVfUaSCyBi9VSAcnTiFPXFtymm%2FZUTye7gR8hfOKZaw94ei3BoQZjboyhGp0rZMHg%2BXA8e4hcA7B7lOUZoarniYkIZYnFClkcC0HlC1PzktuuAPR8lG5XGuuhed9LvAPMJW1gr0GOqUBOxgNWgVTOGJUXitEbCC10odW97DGMos3Fz7NI42zcV0v8rEawKxEzndFuxTfNB1dqIxtJsKz6g0jeUgTqKN2bKkl9NRfOweeYH3LO1x%2F%2B8aQjaY%2FDsETxmhK1aK7guowGI12Fn6DMNMWaSiuCyDdsVo33SXlM6Xi9L%2BIfjxtoXtXsNFlsTC%2BUR%2B37gQF1T0Y%2BG%2FZKVfXopkqUSSemHRzGWjgzBvL&X-Amz-Signature=e95d5ddb3e26b5c3cd90070ec6d9b6dc6d35fc2d52d2b032361649f576276792&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BIR27H6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQ9VMq6Zel2csbLUs4FriayQPTF1%2FiOsYdPKdTthF6WAiBV9T2Sk9aq48JLygcyLtlPtFO1iMkedNBOay91AxL3aSr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMef2tltyMxzJ9gAK%2FKtwDfewMgJbN1sAjU5NOIeFu9Ly41v55Za%2Fc%2F95K7PIqtzsCyZPwVYlW6y9aswOnzmJ4BvMH2shj%2FxG0uKJJkD8AlEOhrTQZz8gYcf8oS0K%2BvJIqjsHFseohMjS9u9%2B1aS3YqqqK9VIOYGT9XG2a%2BGuwR%2BkkQr73iN%2BEaYWwHOIY3fQl0lr8EiLPQFJdv3lGRvZlWMT%2BIWdWXslINZMAbAZVoeaPSnxa2D18OQHqltFz%2FZ%2BgSjq9j8pSre9P0d1f7k30nVa7cnNai18Oo6Nkzbgq1rFz9GCRN5hOzTEa1Y1CRjTQWOxosgVStaB%2BlXS4HVa7KhPVRqeEF%2BYWSkBDyc4IvCqlp%2FZBu%2FDRFqw7DxKH0iEO%2BZFVuf%2F6gg%2BIbyNvsHVhde2tf2eNUU5vUtrbw4n4Ip%2BVCskU2zh2lF84u6a4XD0LRU4rCnPjKsFsFnEN1ej7iX5lFSHn0Obw0sg3rOf%2BtUtmPyovdr0p%2B4sYUuhUGP20c%2Be1Dw0i%2BZ6mNFgWCWlc7Co%2FN5z46A%2FmcyYGIvWE2tauz75qwz7itj8laA4sZirqcvB2PHj1GTO5vjVp0GG3MrLjPK2CDq2%2FrDBVMb74rMBx6pSAiJbm5yGQgaaanNG32X8j7AobtXvsPF4wk7WCvQY6pgGwTnbvPhyKmjhMpraCzYcZxAzJQls49%2BLEqlaZoWoWCih3QuB2V9VSdzK2ZUR3u4JGlnlZIyaJrh6%2B5Nda%2FVO%2BlEzajkb7pnQDgoX1dTFOvq3SHehHWNdxHgGxoEwFE4Df29yGEYlpsn4xI3pMD9ydP5IvcrY%2FHWDX2ye4beCMYxxpBt7GZayppnsSflMtC7LYSZZ7SIwHPbbdY5RvyzT9rT8SyOwp&X-Amz-Signature=4b975e7dda009ae1053dec63b0f31ea1676ff1869130cebcee122434de6053bb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3LSG6FC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBRtjMTpvmiJYeyLm6CFaUryMDbvcnLtIrT4iW7E%2Ba7nAiB6oPT9gZjeB87TaCIsTROD1KsBlf%2BxfT9PkjIUg1u%2FBCr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIM%2FIdsAsZgSoAOZtUXKtwDprpOSi6D4CW4UslTZlYTX77bHadnMn3z2AQ06txOL%2BhsQoL6Nyy%2BEBQrh%2FIX0WnFblw5njrf3IRlGIhQE%2FF4nfzOL6vdenJn%2FEQJcPBWieoStpP8WKM4Il%2Fgn%2BVTFa6qWm6nCxQBR1gJ7pu2wpu%2BfGkiooR6FTmWTkyaLCih1w7uryz%2BmvYg3FAOvWT0gDoEavRTnIB%2BLWQ3ssfjqumQODg27Vo7LwC3szE08bgBMm0zrWPG5RYO9WGgN%2FTQaBF8hJg%2FdTj%2FIbxw9y29O26V1fnNjtRWOpU9Sy7TiLFKGqbmclTBJU0V7tJ828D8fU%2Bvap7Tqm8v30DookrDoQwu6V3vrq61JW%2BPfj05WW24jT7ixHNk3yB%2B5rKO6cuAHETtftegz3OLnVHWgEU5Sc3lySCGne9kCGIdz36dGZJNm2h3zr3GKl6o1CUoMkOT5zKv0cxhdlcsrRwgY%2B%2BVgcPgvu0%2F2AKT9LRTWEPmQzG7nRNXlD2X%2BmAdS%2F%2FjCks6ngbw4cBLEGU9r8bJib5E%2Fs5sCexwlZtKeQXhUNwL8SIeuTlErhekw6F%2FrqblRaqAZKzzuuYx88FJo8%2BOi8xp6RW74foZAjiuThqSrpo8C5xolB3M60FOnpjJnrep73gwiLWCvQY6pgE7GhOIC1fagqeEeRDJIGCxQMGhLhXPpuY2ogWsGmMlCAMiUS2cUMJYF7biHRY3izeu1kzMRP%2FflPeIHzbo%2FQomb9cNa9Vk2SXmsuamz%2FDuIHiDv6XWJ9zHP4P4hTfdT5BqDyU6Mvox9O5QAewvW1QB%2B2qPZSIEyixBbKhRomVYuXSVA08PZwjzLisOD9ORMWSUQ99SA5Z6BrVYL%2Fg9anKTFIRVUcNN&X-Amz-Signature=9fe22d3dee317f063b82911b34377097fa6635152be3eae81f76e4faa318a680&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSKCTI4V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMciHzAbP3239xPfFGTi3n3TKSYfgGhhXDmBAKwZNpMAiBcAAPldWyuWdGZaSrQf5yI1BSi8pSNKPEu0mUw0fJowir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIM0UGFEYMF1Qq%2BekInKtwDVvclvf8Icuy34xVbSxT8gBvQBkOI8HeGygFstY7%2FYjVEGmXPFfLy%2Bbfm17mXgOv%2Bq9JPEmOyrIS4xx9g0psthrLxApxDE2aQ7liDTZBsFj59Sj55KwSolFUUjmOsOu7lURWTmK1OaZ3G2GroxmpWsZ1xcD3Pfa1sGDasiXsFiVyD8ZJEbOcmfWyUeYqHs%2FOUMJ2KcRKUp0AjQS2D9oyhu0%2BVhwK1y2j9gSPFa%2F1xviiLW3%2F%2FVBL1H1JcuvDL09cgAfn3HZyYpnf0LjImS%2FH4uczC4gNDCswTmnO5TVw21fmZud7AhHsuC8qb4O9ChKky%2Fg6d4JdizX8cNVvxVDw%2FOcTWG1EqxqoX2AMzlvE9UNk0wpD0tHayutp%2BmNlLNCOXV4sJ4CgHWpMWP5BYmEe6CNkm3fPM1sOlWKsRqAcx5ZpooQM%2BcTIlFwucc3VxkeTEFEs%2F%2BR57W8m7bZvj2VXM0da1sOrUguTMuuxsVJzcHQh12DKIRv84TgsX6BcoDqTOQX0oInVxX%2BfAjDU14PVITv8OZQMNW4S0s1WERg0i%2F0b2nl31SALOVKXyK3y7xSPLUm4owbpTMU5C8Iz0A1gZy5ZPuE13Ce%2BRxNi6Xj6MBAJm5UnsRAfHYaFtGPEw%2BLSCvQY6pgER4x0%2FYy%2Bs6e%2F%2FoPv4MeSJY0qo%2F17JPJb0B3gyV82nzlJiujDt9A4UpMa%2F%2FS11uRLiGkUBzu1uKXT2HvwomcSCtEAw4ocMQY9JvTXp2NhHV6IzK8sIsdFbOM4c9G6vc%2BZxXMHsaO8cN2KtEMowLlP0Pt5JI4yij3r8DeN0TOEeUmqMTp%2F2a4teYPnS7hbLATAWWEYJlXKtL1ZpbhP0X0Kkwe383TZ6&X-Amz-Signature=820e33bbe5977942d0a89e5077352f973d9fc349a92845843996ac29bfcbabd2&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VVVOZXP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaumKBYOrhDrCEmLvlKet7GTfo8JMBoO%2F5FbHQvwzdawIgUzfS6udx7%2FO%2FRFUPyTcZ655Zwmguue%2FLchxEyauvLnYq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDA%2FFthj3wg4lLAM81CrcA%2FMNHOeZWbDzgCrGEujXjZIM%2B8Q1snk%2Bxgfn7t3QXdZCesI52ot8geSSqgMa0%2F%2BEcIYnyJ5nEvqVWZ2CLqpE6H0o230udsG%2BERlH6Pw5nqnHNVp1tARR2%2FCDXOcua4PAjFy5pyGJySzepKgCEfz9WxxVsi0%2FYY%2FFT0AMQimDa80mHd8FruZUn6xr1A3Yt%2F5Wl39W5EvzoDxa6dj7kUrYjLmEbPp7%2Bsc6xqCKLmAVE3dufmojv4QZS8xt0Vd%2B2VGUVhuz5tiooUdOXJb3aND8iSC%2B%2FVNsZbZ61wqleG%2BdhDwg9JiNGIXETVhArOuI%2FIFQPqddzHiNKKwjST3Rye%2B1zsYY89j0xctcBFtBPAgWzrTVUeuRbSUIMN6smYDzLnMYjLkmuXxiTPZKoIZSaueiO3OE50wYv6w0CIXbJjE5NtA3KnZMBVXVAi90vTxuYnGW2ivQPwpK5mzsSss%2FXMaKxdPiuLIsXXdfoGpClohWNrkiFq6N82ObZR8Y52%2FCAC9yhZp3NabPEupb9ts654mjWCJMtnSPKjzl7UMGnC6KarKLeUnd%2FYN6XeXo%2FJwpvp9fcYAJ53g2vvANWBxSyTjw9h7tvBDClEXEoKZ9D3JED%2FKohPndjEbDi69mRAHtMOK0gr0GOqUB41wS7SLcI7x%2FCZ%2BfFjqACDBCeZfCXw%2BblTgugZ2Btd00fMzKvdIhjkZE7oNgu1eB440TY481PIaAPXIghXSZR3X6%2FJ%2BQMfr48lbBcvYHNB91Q7eoGIzowP7Iej2p779A66cs8vEbbyLwgrHv8KkS9Wb1m0DZnRIOk2FSd0FITH%2FocIoTNgtvTdRj1on%2BoEZZ3CWyFOZiKlFoZtxa4q4lxP0UZ6ri&X-Amz-Signature=88d1f57f88a9f1107fdf2b20e44806ab4ae823c85eceae7bc27ad6a20dbf996b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BIR27H6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQ9VMq6Zel2csbLUs4FriayQPTF1%2FiOsYdPKdTthF6WAiBV9T2Sk9aq48JLygcyLtlPtFO1iMkedNBOay91AxL3aSr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMef2tltyMxzJ9gAK%2FKtwDfewMgJbN1sAjU5NOIeFu9Ly41v55Za%2Fc%2F95K7PIqtzsCyZPwVYlW6y9aswOnzmJ4BvMH2shj%2FxG0uKJJkD8AlEOhrTQZz8gYcf8oS0K%2BvJIqjsHFseohMjS9u9%2B1aS3YqqqK9VIOYGT9XG2a%2BGuwR%2BkkQr73iN%2BEaYWwHOIY3fQl0lr8EiLPQFJdv3lGRvZlWMT%2BIWdWXslINZMAbAZVoeaPSnxa2D18OQHqltFz%2FZ%2BgSjq9j8pSre9P0d1f7k30nVa7cnNai18Oo6Nkzbgq1rFz9GCRN5hOzTEa1Y1CRjTQWOxosgVStaB%2BlXS4HVa7KhPVRqeEF%2BYWSkBDyc4IvCqlp%2FZBu%2FDRFqw7DxKH0iEO%2BZFVuf%2F6gg%2BIbyNvsHVhde2tf2eNUU5vUtrbw4n4Ip%2BVCskU2zh2lF84u6a4XD0LRU4rCnPjKsFsFnEN1ej7iX5lFSHn0Obw0sg3rOf%2BtUtmPyovdr0p%2B4sYUuhUGP20c%2Be1Dw0i%2BZ6mNFgWCWlc7Co%2FN5z46A%2FmcyYGIvWE2tauz75qwz7itj8laA4sZirqcvB2PHj1GTO5vjVp0GG3MrLjPK2CDq2%2FrDBVMb74rMBx6pSAiJbm5yGQgaaanNG32X8j7AobtXvsPF4wk7WCvQY6pgGwTnbvPhyKmjhMpraCzYcZxAzJQls49%2BLEqlaZoWoWCih3QuB2V9VSdzK2ZUR3u4JGlnlZIyaJrh6%2B5Nda%2FVO%2BlEzajkb7pnQDgoX1dTFOvq3SHehHWNdxHgGxoEwFE4Df29yGEYlpsn4xI3pMD9ydP5IvcrY%2FHWDX2ye4beCMYxxpBt7GZayppnsSflMtC7LYSZZ7SIwHPbbdY5RvyzT9rT8SyOwp&X-Amz-Signature=6106dced96be3fe808d88093fa09fe3fc20ae195cec09630af387fb4c48fb1f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JP5Y3SE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTGNqEkgmOoRg06toIQ0uuy5X6ntKQYp%2BCa0MAtJxohAIgeyFsFX%2BFhpeGyZW4LFqFVYeH%2FbrM2Wr22IidRGYISbYq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDOXOOEg4oH2tSsUQZyrcA3wQCjyr9cB69lN5Wqmfo02pIOt%2BIsWHcGgEkURiqugiLltOxJn08H%2Ff2s9hZ6Be2J5Kn2ESAVwXg26dy6Vxblo57g2ScS%2BWfxfrs4QKfvB0VlNthihO%2FvMN1dRad1W6wouCv3M8RRcDi2GpuNbzIiZfCR%2FpvN0PuP4QpDBUUsLXkWes6Hm%2BlSUK04kpUZ4ahWPcSnfwqlfJweXT7PQdiQSKQ44CrXoHOUdE03iICeu4RrUDo5dBwzxrew333a9NoZPNGAsSnLT62MMEF8USiyIOOK93%2BoLt%2FoQ66ZEfbmGtBaOjgykJIj5BNsbvIdDotTDHCrnDWHI4OLS96A1NEQIuKAdPZOPIbMC%2B3shTvjcofFVsriyLvA%2FOR%2BJ2p%2B8C%2BEBskAlSJg%2BGrU4%2BsdCclf9wbtbaR2%2F7x6aHPn%2FJ247Mv%2FLdjfWtiH5YiZr5VuDL3wzu4oKXTUMK3wUH01AjK3XmNQUdHH9qnK7NnXedEFNri4tyuL62GPELRAQMIs%2B%2B9kO9cT5%2FWkqp2UhAqg%2B6UPduMUuTWii0t3rle8ac3PSwBkOjA9QxHtuzfVxXrM7ffolsBrd2GiO2UEqZGUINrQgZ%2FEXDGfv3VRic7y6pH8vX9s%2FlY43Sr8sAYmkLMPy0gr0GOqUBuoxvgAwhv0Hh7xZC8hXFfcdeZH8wmnZWFuXUICeH28JUrtEkmWIGybm1ufvY0aRCDe5zws%2FjRPidSBTD5AJDilZJRFT2x%2B3HOvVnCIySk4V9LGDtB9gC%2F7gr5XBdutvj%2F3TBx%2BvEIpxVPEvwZkDBAudElAPXsuZAfzjnYlf02rrmwd4ZFsLLibnILqq3cZqg9TGs3MXKgYeZ3lAfdo0xEEjV01%2B%2F&X-Amz-Signature=8bac6cf66742b6e79d1af62ef7ad176b9630024ea45ccda154a7c7b3ede745a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JP5Y3SE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTGNqEkgmOoRg06toIQ0uuy5X6ntKQYp%2BCa0MAtJxohAIgeyFsFX%2BFhpeGyZW4LFqFVYeH%2FbrM2Wr22IidRGYISbYq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDOXOOEg4oH2tSsUQZyrcA3wQCjyr9cB69lN5Wqmfo02pIOt%2BIsWHcGgEkURiqugiLltOxJn08H%2Ff2s9hZ6Be2J5Kn2ESAVwXg26dy6Vxblo57g2ScS%2BWfxfrs4QKfvB0VlNthihO%2FvMN1dRad1W6wouCv3M8RRcDi2GpuNbzIiZfCR%2FpvN0PuP4QpDBUUsLXkWes6Hm%2BlSUK04kpUZ4ahWPcSnfwqlfJweXT7PQdiQSKQ44CrXoHOUdE03iICeu4RrUDo5dBwzxrew333a9NoZPNGAsSnLT62MMEF8USiyIOOK93%2BoLt%2FoQ66ZEfbmGtBaOjgykJIj5BNsbvIdDotTDHCrnDWHI4OLS96A1NEQIuKAdPZOPIbMC%2B3shTvjcofFVsriyLvA%2FOR%2BJ2p%2B8C%2BEBskAlSJg%2BGrU4%2BsdCclf9wbtbaR2%2F7x6aHPn%2FJ247Mv%2FLdjfWtiH5YiZr5VuDL3wzu4oKXTUMK3wUH01AjK3XmNQUdHH9qnK7NnXedEFNri4tyuL62GPELRAQMIs%2B%2B9kO9cT5%2FWkqp2UhAqg%2B6UPduMUuTWii0t3rle8ac3PSwBkOjA9QxHtuzfVxXrM7ffolsBrd2GiO2UEqZGUINrQgZ%2FEXDGfv3VRic7y6pH8vX9s%2FlY43Sr8sAYmkLMPy0gr0GOqUBuoxvgAwhv0Hh7xZC8hXFfcdeZH8wmnZWFuXUICeH28JUrtEkmWIGybm1ufvY0aRCDe5zws%2FjRPidSBTD5AJDilZJRFT2x%2B3HOvVnCIySk4V9LGDtB9gC%2F7gr5XBdutvj%2F3TBx%2BvEIpxVPEvwZkDBAudElAPXsuZAfzjnYlf02rrmwd4ZFsLLibnILqq3cZqg9TGs3MXKgYeZ3lAfdo0xEEjV01%2B%2F&X-Amz-Signature=abd791b2c07c3ee35df3c7cbec7b578d2d718ced140499260d0cfa011d4e3703&X-Amz-SignedHeaders=host&x-id=GetObject)
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