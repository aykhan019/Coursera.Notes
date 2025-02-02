

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3IAR4B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID12pFeAIHHDu2HNFQePB5bF8mKmybEC%2F8UMgxt3%2Bjy6AiBd7loGif7cVhtPugtVon51%2BxlLhqPRNKX0h%2BEWerEnkCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9cWiLemTRsPTefRKKtwDpt2ccLm1QtfZ3Cm%2BRA8d8HRYTehAa4fMubg3rG8E6ULjiqJvj2qtoI10xV1lAFuH94RyWi32nCtA4C9FGBAEkCA98OIjW4RoHCG1eJ24rcVITBavm%2Bkt0w9CEy7D8nF9ps6ckV%2BvSJr%2BFW5azZaW%2BMBUGcqe8eJ6UC33bjDDOiv8lB%2BHiUSvZadovFHhd2dqsTkLNeHxm4DuoLNnxi4L0rEdaQSc2JAoFKYYkiMMcvgPuy%2BrNHQ4vQoBXuGaKGSDLKSLTelTcuf5zzzQkaBgTpMgJQn9%2B%2FMPil%2FpiR%2BSJymnRNw%2FJWk%2F3cGTb7ZqRbP4xFaG4hyBqbGl1oh41uHHPse8b1FBYZ2cSAkYgJCERX3emW7j0gDISwhabmiQXkADVRXPnZt%2FUZ%2FhOQvJ%2FXKDry7mlZBjl1%2Fii8KvCHhj%2B9CAXso%2FRCb25Uz62zYou8bxFx%2BE3%2BWb9Jcs1xD9tRn7DfD2bwcKxrDjvkY8%2B7BU4s%2BocihS%2BSJIp%2BylkHWKMP%2FVJH1TaTMxWKVUsIoacZKtFCqOe6XNP%2Fe71nliHn8YNO4ZcjpiwPhjPg1oLrHvRfDN1VJHoz4MCO0sv8Xm2DwiNeMiXpQ4A60EcwA99iVJg3Lgt5oh7g%2FhHHouvC8wleH7vAY6pgHMRjlqEx6uHCWJIEn0aaGGgoK1xs%2FrcG5nkbNhnCO0W9ygki5JZFBJlM996F5ytJSokfpVH%2F3Job9UFuOqKbMs4ZXRHdT%2Bh%2Bk%2BUhDHqiFvMYDb4MUHFl1GLpx0Xz2%2B2iq7cwNaGRn%2FcVUX7XX3vQGqZ4wIqTON1vvby%2BHUP72Ybv8QwNHZwXc4aRyhzAiUv2lbHwgVERqsA0hUKho2209H7o1EWGi9&X-Amz-Signature=d5a2a9d162bd86ab3812aeade042bc2aa4e93c25c2981392cbe44957786e357f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Example Dataset
Consider a dataset related to CO2 emissions from different cars. The dataset includes:
- Engine size
- Number of cylinders
- Fuel consumption
- CO2 emission
#### Predictive Question
Given this dataset, is it possible to predict the CO2 emission of a car using other fields such as engine size or cylinders? → Yes
### Historical Data and Prediction
Assume there is historical data from different cars. The goal is to estimate the CO2 emission of a new or unknown car, such as the one in row 9, which hasn't been manufactured yet. Regression methods can be used to make this prediction.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3IAR4B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID12pFeAIHHDu2HNFQePB5bF8mKmybEC%2F8UMgxt3%2Bjy6AiBd7loGif7cVhtPugtVon51%2BxlLhqPRNKX0h%2BEWerEnkCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9cWiLemTRsPTefRKKtwDpt2ccLm1QtfZ3Cm%2BRA8d8HRYTehAa4fMubg3rG8E6ULjiqJvj2qtoI10xV1lAFuH94RyWi32nCtA4C9FGBAEkCA98OIjW4RoHCG1eJ24rcVITBavm%2Bkt0w9CEy7D8nF9ps6ckV%2BvSJr%2BFW5azZaW%2BMBUGcqe8eJ6UC33bjDDOiv8lB%2BHiUSvZadovFHhd2dqsTkLNeHxm4DuoLNnxi4L0rEdaQSc2JAoFKYYkiMMcvgPuy%2BrNHQ4vQoBXuGaKGSDLKSLTelTcuf5zzzQkaBgTpMgJQn9%2B%2FMPil%2FpiR%2BSJymnRNw%2FJWk%2F3cGTb7ZqRbP4xFaG4hyBqbGl1oh41uHHPse8b1FBYZ2cSAkYgJCERX3emW7j0gDISwhabmiQXkADVRXPnZt%2FUZ%2FhOQvJ%2FXKDry7mlZBjl1%2Fii8KvCHhj%2B9CAXso%2FRCb25Uz62zYou8bxFx%2BE3%2BWb9Jcs1xD9tRn7DfD2bwcKxrDjvkY8%2B7BU4s%2BocihS%2BSJIp%2BylkHWKMP%2FVJH1TaTMxWKVUsIoacZKtFCqOe6XNP%2Fe71nliHn8YNO4ZcjpiwPhjPg1oLrHvRfDN1VJHoz4MCO0sv8Xm2DwiNeMiXpQ4A60EcwA99iVJg3Lgt5oh7g%2FhHHouvC8wleH7vAY6pgHMRjlqEx6uHCWJIEn0aaGGgoK1xs%2FrcG5nkbNhnCO0W9ygki5JZFBJlM996F5ytJSokfpVH%2F3Job9UFuOqKbMs4ZXRHdT%2Bh%2Bk%2BUhDHqiFvMYDb4MUHFl1GLpx0Xz2%2B2iq7cwNaGRn%2FcVUX7XX3vQGqZ4wIqTON1vvby%2BHUP72Ybv8QwNHZwXc4aRyhzAiUv2lbHwgVERqsA0hUKho2209H7o1EWGi9&X-Amz-Signature=2f5e68999822dcdad36e4d9b2e3dde4c1d6420b8218d8533c46a263a505fdaa4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Types of Variables in Regression
- **Dependent Variable (Y):** The state, target, or final goal to be predicted.
- **Independent Variables (X):** The causes or explanatory variables.
### Types of Regression Models
#### Simple Regression
- **Definition:** Uses one independent variable to estimate a dependent variable.
- **Example:** Predicting CO2 emission using the variable of engine size.
- **Nature:** Can be linear or non-linear based on the relationship between the independent and dependent variables.
#### Multiple Regression
- **Definition:** Uses more than one independent variable to estimate a dependent variable.
- **Example:** Predicting CO2 emission using engine size and the number of cylinders.
- **Nature:** Can be linear or non-linear depending on the relationship between the dependent and independent variables.
### Applications of Regression
#### Sales Forecasting
Predicting a salesperson's total yearly sales using independent variables such as age, education, and years of experience.
#### Psychology
Determining individual satisfaction based on demographic and psychological factors.
#### Real Estate
Predicting the price of a house based on its size, number of bedrooms, and other features.
#### Employment Income
Predicting employment income using variables such as hours of work, education, occupation, age, and years of experience.
#### Other Fields
Regression analysis is also useful in finance, healthcare, retail, and more.
### Conclusion
Regression analysis has numerous applications across various fields. It helps in estimating continuous values using historical data and independent variables. Various regression algorithms exist, each suited to specific conditions, providing a foundation for exploring different regression techniques.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3IAR4B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID12pFeAIHHDu2HNFQePB5bF8mKmybEC%2F8UMgxt3%2Bjy6AiBd7loGif7cVhtPugtVon51%2BxlLhqPRNKX0h%2BEWerEnkCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9cWiLemTRsPTefRKKtwDpt2ccLm1QtfZ3Cm%2BRA8d8HRYTehAa4fMubg3rG8E6ULjiqJvj2qtoI10xV1lAFuH94RyWi32nCtA4C9FGBAEkCA98OIjW4RoHCG1eJ24rcVITBavm%2Bkt0w9CEy7D8nF9ps6ckV%2BvSJr%2BFW5azZaW%2BMBUGcqe8eJ6UC33bjDDOiv8lB%2BHiUSvZadovFHhd2dqsTkLNeHxm4DuoLNnxi4L0rEdaQSc2JAoFKYYkiMMcvgPuy%2BrNHQ4vQoBXuGaKGSDLKSLTelTcuf5zzzQkaBgTpMgJQn9%2B%2FMPil%2FpiR%2BSJymnRNw%2FJWk%2F3cGTb7ZqRbP4xFaG4hyBqbGl1oh41uHHPse8b1FBYZ2cSAkYgJCERX3emW7j0gDISwhabmiQXkADVRXPnZt%2FUZ%2FhOQvJ%2FXKDry7mlZBjl1%2Fii8KvCHhj%2B9CAXso%2FRCb25Uz62zYou8bxFx%2BE3%2BWb9Jcs1xD9tRn7DfD2bwcKxrDjvkY8%2B7BU4s%2BocihS%2BSJIp%2BylkHWKMP%2FVJH1TaTMxWKVUsIoacZKtFCqOe6XNP%2Fe71nliHn8YNO4ZcjpiwPhjPg1oLrHvRfDN1VJHoz4MCO0sv8Xm2DwiNeMiXpQ4A60EcwA99iVJg3Lgt5oh7g%2FhHHouvC8wleH7vAY6pgHMRjlqEx6uHCWJIEn0aaGGgoK1xs%2FrcG5nkbNhnCO0W9ygki5JZFBJlM996F5ytJSokfpVH%2F3Job9UFuOqKbMs4ZXRHdT%2Bh%2Bk%2BUhDHqiFvMYDb4MUHFl1GLpx0Xz2%2B2iq7cwNaGRn%2FcVUX7XX3vQGqZ4wIqTON1vvby%2BHUP72Ybv8QwNHZwXc4aRyhzAiUv2lbHwgVERqsA0hUKho2209H7o1EWGi9&X-Amz-Signature=60dcfa7107179af96c3cc75a7ed47309201b6d78560dc4edf0eebd13aefe83ea&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## Introduction to Linear Regression
Linear regression is an effective method for predicting a continuous value using other variables. This introduction provides the necessary background to use linear regression effectively.
### Dataset Overview
Consider a dataset related to CO2 emissions of different cars. The dataset includes:
- Engine size
- Number of cylinders
- Fuel consumption
- CO2 emissions
The goal is to predict the CO2 emission of a car using another field, such as engine size. Linear regression can be used for this purpose.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3IAR4B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID12pFeAIHHDu2HNFQePB5bF8mKmybEC%2F8UMgxt3%2Bjy6AiBd7loGif7cVhtPugtVon51%2BxlLhqPRNKX0h%2BEWerEnkCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9cWiLemTRsPTefRKKtwDpt2ccLm1QtfZ3Cm%2BRA8d8HRYTehAa4fMubg3rG8E6ULjiqJvj2qtoI10xV1lAFuH94RyWi32nCtA4C9FGBAEkCA98OIjW4RoHCG1eJ24rcVITBavm%2Bkt0w9CEy7D8nF9ps6ckV%2BvSJr%2BFW5azZaW%2BMBUGcqe8eJ6UC33bjDDOiv8lB%2BHiUSvZadovFHhd2dqsTkLNeHxm4DuoLNnxi4L0rEdaQSc2JAoFKYYkiMMcvgPuy%2BrNHQ4vQoBXuGaKGSDLKSLTelTcuf5zzzQkaBgTpMgJQn9%2B%2FMPil%2FpiR%2BSJymnRNw%2FJWk%2F3cGTb7ZqRbP4xFaG4hyBqbGl1oh41uHHPse8b1FBYZ2cSAkYgJCERX3emW7j0gDISwhabmiQXkADVRXPnZt%2FUZ%2FhOQvJ%2FXKDry7mlZBjl1%2Fii8KvCHhj%2B9CAXso%2FRCb25Uz62zYou8bxFx%2BE3%2BWb9Jcs1xD9tRn7DfD2bwcKxrDjvkY8%2B7BU4s%2BocihS%2BSJIp%2BylkHWKMP%2FVJH1TaTMxWKVUsIoacZKtFCqOe6XNP%2Fe71nliHn8YNO4ZcjpiwPhjPg1oLrHvRfDN1VJHoz4MCO0sv8Xm2DwiNeMiXpQ4A60EcwA99iVJg3Lgt5oh7g%2FhHHouvC8wleH7vAY6pgHMRjlqEx6uHCWJIEn0aaGGgoK1xs%2FrcG5nkbNhnCO0W9ygki5JZFBJlM996F5ytJSokfpVH%2F3Job9UFuOqKbMs4ZXRHdT%2Bh%2Bk%2BUhDHqiFvMYDb4MUHFl1GLpx0Xz2%2B2iq7cwNaGRn%2FcVUX7XX3vQGqZ4wIqTON1vvby%2BHUP72Ybv8QwNHZwXc4aRyhzAiUv2lbHwgVERqsA0hUKho2209H7o1EWGi9&X-Amz-Signature=8947344a085a72f77b9a66bcbbcad70eb96b1d1d65d7a820064061821e114a4e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Linear Regression Basics
Linear regression is the approximation of a linear model to describe the relationship between two or more variables.
#### Variables in Linear Regression
- **Dependent Variable (Y):** The continuous value being predicted.
- **Independent Variable (X):** The explanatory variable(s), which can be categorical or continuous.
#### Types of Linear Regression
1. **Simple Linear Regression:**
	- Uses one independent variable to estimate a dependent variable.
	- Example: Predicting CO2 emission using engine size.
2. **Multiple Linear Regression:**
	- Uses more than one independent variable to estimate a dependent variable.
	- Example: Predicting CO2 emission using engine size and number of cylinders.
### How Linear Regression Works
#### Scatter Plot
A scatter plot can be used to visualize the relationship between variables, such as engine size (independent variable) and CO2 emission (dependent variable). The plot helps to identify if the variables are linearly related.
#### Fitting a Line
Linear regression fits a line through the data points. For example, as the engine size increases, the CO2 emissions also increase. The objective is to find a line that best fits the data, which can be used to predict CO2 emissions.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3IAR4B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID12pFeAIHHDu2HNFQePB5bF8mKmybEC%2F8UMgxt3%2Bjy6AiBd7loGif7cVhtPugtVon51%2BxlLhqPRNKX0h%2BEWerEnkCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9cWiLemTRsPTefRKKtwDpt2ccLm1QtfZ3Cm%2BRA8d8HRYTehAa4fMubg3rG8E6ULjiqJvj2qtoI10xV1lAFuH94RyWi32nCtA4C9FGBAEkCA98OIjW4RoHCG1eJ24rcVITBavm%2Bkt0w9CEy7D8nF9ps6ckV%2BvSJr%2BFW5azZaW%2BMBUGcqe8eJ6UC33bjDDOiv8lB%2BHiUSvZadovFHhd2dqsTkLNeHxm4DuoLNnxi4L0rEdaQSc2JAoFKYYkiMMcvgPuy%2BrNHQ4vQoBXuGaKGSDLKSLTelTcuf5zzzQkaBgTpMgJQn9%2B%2FMPil%2FpiR%2BSJymnRNw%2FJWk%2F3cGTb7ZqRbP4xFaG4hyBqbGl1oh41uHHPse8b1FBYZ2cSAkYgJCERX3emW7j0gDISwhabmiQXkADVRXPnZt%2FUZ%2FhOQvJ%2FXKDry7mlZBjl1%2Fii8KvCHhj%2B9CAXso%2FRCb25Uz62zYou8bxFx%2BE3%2BWb9Jcs1xD9tRn7DfD2bwcKxrDjvkY8%2B7BU4s%2BocihS%2BSJIp%2BylkHWKMP%2FVJH1TaTMxWKVUsIoacZKtFCqOe6XNP%2Fe71nliHn8YNO4ZcjpiwPhjPg1oLrHvRfDN1VJHoz4MCO0sv8Xm2DwiNeMiXpQ4A60EcwA99iVJg3Lgt5oh7g%2FhHHouvC8wleH7vAY6pgHMRjlqEx6uHCWJIEn0aaGGgoK1xs%2FrcG5nkbNhnCO0W9ygki5JZFBJlM996F5ytJSokfpVH%2F3Job9UFuOqKbMs4ZXRHdT%2Bh%2Bk%2BUhDHqiFvMYDb4MUHFl1GLpx0Xz2%2B2iq7cwNaGRn%2FcVUX7XX3vQGqZ4wIqTON1vvby%2BHUP72Ybv8QwNHZwXc4aRyhzAiUv2lbHwgVERqsA0hUKho2209H7o1EWGi9&X-Amz-Signature=1b92b71fe6e9fc0c453fd2bdfaf475f1a3ca7252f07701db8c8a4b5f5c11b4e7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3IAR4B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID12pFeAIHHDu2HNFQePB5bF8mKmybEC%2F8UMgxt3%2Bjy6AiBd7loGif7cVhtPugtVon51%2BxlLhqPRNKX0h%2BEWerEnkCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9cWiLemTRsPTefRKKtwDpt2ccLm1QtfZ3Cm%2BRA8d8HRYTehAa4fMubg3rG8E6ULjiqJvj2qtoI10xV1lAFuH94RyWi32nCtA4C9FGBAEkCA98OIjW4RoHCG1eJ24rcVITBavm%2Bkt0w9CEy7D8nF9ps6ckV%2BvSJr%2BFW5azZaW%2BMBUGcqe8eJ6UC33bjDDOiv8lB%2BHiUSvZadovFHhd2dqsTkLNeHxm4DuoLNnxi4L0rEdaQSc2JAoFKYYkiMMcvgPuy%2BrNHQ4vQoBXuGaKGSDLKSLTelTcuf5zzzQkaBgTpMgJQn9%2B%2FMPil%2FpiR%2BSJymnRNw%2FJWk%2F3cGTb7ZqRbP4xFaG4hyBqbGl1oh41uHHPse8b1FBYZ2cSAkYgJCERX3emW7j0gDISwhabmiQXkADVRXPnZt%2FUZ%2FhOQvJ%2FXKDry7mlZBjl1%2Fii8KvCHhj%2B9CAXso%2FRCb25Uz62zYou8bxFx%2BE3%2BWb9Jcs1xD9tRn7DfD2bwcKxrDjvkY8%2B7BU4s%2BocihS%2BSJIp%2BylkHWKMP%2FVJH1TaTMxWKVUsIoacZKtFCqOe6XNP%2Fe71nliHn8YNO4ZcjpiwPhjPg1oLrHvRfDN1VJHoz4MCO0sv8Xm2DwiNeMiXpQ4A60EcwA99iVJg3Lgt5oh7g%2FhHHouvC8wleH7vAY6pgHMRjlqEx6uHCWJIEn0aaGGgoK1xs%2FrcG5nkbNhnCO0W9ygki5JZFBJlM996F5ytJSokfpVH%2F3Job9UFuOqKbMs4ZXRHdT%2Bh%2Bk%2BUhDHqiFvMYDb4MUHFl1GLpx0Xz2%2B2iq7cwNaGRn%2FcVUX7XX3vQGqZ4wIqTON1vvby%2BHUP72Ybv8QwNHZwXc4aRyhzAiUv2lbHwgVERqsA0hUKho2209H7o1EWGi9&X-Amz-Signature=fa63e1d2a060b704a656b5b469c796e1863417e4074f7ad6d385e07a3b94fa8b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Mathematical Representation
The fitted line in linear regression is represented as a polynomial. For a simple linear regression with one independent variable , the model is:
$ \hat{y} = \theta_0 + \theta_1 x_1 $
- $ \hat{y} $: Predicted value (dependent variable)
- $ x_1 $: Independent variable
- $ \theta_0 $: Intercept
- $ \theta_1 $: Slope or gradient of the line
#### Estimating Coefficients
- $ \theta_0 $ (intercept) and $ θ_1 $ (slope) are the parameters of the line that need to be adjusted to minimize the error.
- The goal is to minimize the mean squared error (MSE), which is the mean of all residual errors (the distance from data points to the fitted line).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3IAR4B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID12pFeAIHHDu2HNFQePB5bF8mKmybEC%2F8UMgxt3%2Bjy6AiBd7loGif7cVhtPugtVon51%2BxlLhqPRNKX0h%2BEWerEnkCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9cWiLemTRsPTefRKKtwDpt2ccLm1QtfZ3Cm%2BRA8d8HRYTehAa4fMubg3rG8E6ULjiqJvj2qtoI10xV1lAFuH94RyWi32nCtA4C9FGBAEkCA98OIjW4RoHCG1eJ24rcVITBavm%2Bkt0w9CEy7D8nF9ps6ckV%2BvSJr%2BFW5azZaW%2BMBUGcqe8eJ6UC33bjDDOiv8lB%2BHiUSvZadovFHhd2dqsTkLNeHxm4DuoLNnxi4L0rEdaQSc2JAoFKYYkiMMcvgPuy%2BrNHQ4vQoBXuGaKGSDLKSLTelTcuf5zzzQkaBgTpMgJQn9%2B%2FMPil%2FpiR%2BSJymnRNw%2FJWk%2F3cGTb7ZqRbP4xFaG4hyBqbGl1oh41uHHPse8b1FBYZ2cSAkYgJCERX3emW7j0gDISwhabmiQXkADVRXPnZt%2FUZ%2FhOQvJ%2FXKDry7mlZBjl1%2Fii8KvCHhj%2B9CAXso%2FRCb25Uz62zYou8bxFx%2BE3%2BWb9Jcs1xD9tRn7DfD2bwcKxrDjvkY8%2B7BU4s%2BocihS%2BSJIp%2BylkHWKMP%2FVJH1TaTMxWKVUsIoacZKtFCqOe6XNP%2Fe71nliHn8YNO4ZcjpiwPhjPg1oLrHvRfDN1VJHoz4MCO0sv8Xm2DwiNeMiXpQ4A60EcwA99iVJg3Lgt5oh7g%2FhHHouvC8wleH7vAY6pgHMRjlqEx6uHCWJIEn0aaGGgoK1xs%2FrcG5nkbNhnCO0W9ygki5JZFBJlM996F5ytJSokfpVH%2F3Job9UFuOqKbMs4ZXRHdT%2Bh%2Bk%2BUhDHqiFvMYDb4MUHFl1GLpx0Xz2%2B2iq7cwNaGRn%2FcVUX7XX3vQGqZ4wIqTON1vvby%2BHUP72Ybv8QwNHZwXc4aRyhzAiUv2lbHwgVERqsA0hUKho2209H7o1EWGi9&X-Amz-Signature=3539d8028ffd322cd72681583de01c2230270716f5277bef2fba358c2f1b9d05&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3IAR4B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID12pFeAIHHDu2HNFQePB5bF8mKmybEC%2F8UMgxt3%2Bjy6AiBd7loGif7cVhtPugtVon51%2BxlLhqPRNKX0h%2BEWerEnkCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9cWiLemTRsPTefRKKtwDpt2ccLm1QtfZ3Cm%2BRA8d8HRYTehAa4fMubg3rG8E6ULjiqJvj2qtoI10xV1lAFuH94RyWi32nCtA4C9FGBAEkCA98OIjW4RoHCG1eJ24rcVITBavm%2Bkt0w9CEy7D8nF9ps6ckV%2BvSJr%2BFW5azZaW%2BMBUGcqe8eJ6UC33bjDDOiv8lB%2BHiUSvZadovFHhd2dqsTkLNeHxm4DuoLNnxi4L0rEdaQSc2JAoFKYYkiMMcvgPuy%2BrNHQ4vQoBXuGaKGSDLKSLTelTcuf5zzzQkaBgTpMgJQn9%2B%2FMPil%2FpiR%2BSJymnRNw%2FJWk%2F3cGTb7ZqRbP4xFaG4hyBqbGl1oh41uHHPse8b1FBYZ2cSAkYgJCERX3emW7j0gDISwhabmiQXkADVRXPnZt%2FUZ%2FhOQvJ%2FXKDry7mlZBjl1%2Fii8KvCHhj%2B9CAXso%2FRCb25Uz62zYou8bxFx%2BE3%2BWb9Jcs1xD9tRn7DfD2bwcKxrDjvkY8%2B7BU4s%2BocihS%2BSJIp%2BylkHWKMP%2FVJH1TaTMxWKVUsIoacZKtFCqOe6XNP%2Fe71nliHn8YNO4ZcjpiwPhjPg1oLrHvRfDN1VJHoz4MCO0sv8Xm2DwiNeMiXpQ4A60EcwA99iVJg3Lgt5oh7g%2FhHHouvC8wleH7vAY6pgHMRjlqEx6uHCWJIEn0aaGGgoK1xs%2FrcG5nkbNhnCO0W9ygki5JZFBJlM996F5ytJSokfpVH%2F3Job9UFuOqKbMs4ZXRHdT%2Bh%2Bk%2BUhDHqiFvMYDb4MUHFl1GLpx0Xz2%2B2iq7cwNaGRn%2FcVUX7XX3vQGqZ4wIqTON1vvby%2BHUP72Ybv8QwNHZwXc4aRyhzAiUv2lbHwgVERqsA0hUKho2209H7o1EWGi9&X-Amz-Signature=f6d8cab5ad331bb3777934edf0a90d2369755bdfa2e31735bf77e424f52962c4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example Calculation
For a dataset with known values:
- If $ θ_1 $= 43.98 and $  θ_0 $ = 92.94, the linear model is:
$$ CO2Emission=92.94+43.98×EngineSize $$
#### Prediction Example
For a car with an engine size of 2.4:
$$ CO2Emission=92.94+43.98×2.4=198.492 $$
### Why Linear Regression is Useful
- **Simplicity:** Easy to use and understand.
- **Speed:** Fast and efficient.
- **No Parameter Tuning:** Does not require parameter tuning like other algorithms (e.g., k-nearest neighbors, neural networks).
- **Interpretability:** Highly interpretable and provides clear insights into relationships between variables.
___

## Model Evaluation in Regression
Model evaluation in regression aims to assess how well a model can predict unknown data. Two main evaluation approaches are commonly used: train and test on the same dataset, and train/test split. Additionally, K-fold cross-validation is introduced as a more advanced method to address some limitations of the other two approaches.
### Evaluation Approaches
6. **Train and Test on the Same Dataset:**
	- **Process:**
		- Use the entire dataset to train the model.
		- Select a portion of the dataset as the test set (without labels during prediction).
		- Predict target values using the model.
		- Compare predicted values with actual values to calculate accuracy.
	- **Metrics:**
		- Compare actual values y with predicted values $ \hat{y} $.
		- Calculate the error as the average difference between predicted and actual values.
	- **Advantages:**
		- Simple and straightforward.
	- **Disadvantages:**
		- High training accuracy but low out-of-sample accuracy due to overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666APIYIOZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWrlSuAbs1AHB5Zh7tnqklPWOdb41iOatCekJqgTw9DwIgQcEB3l%2BWOdsz3JbBNfod38%2F3RYVHsayGH6CHQOm20gIqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBYqOepYgwXt1de%2FkCrcA1p2dFGTt2m5qzY%2BnvM7A9x2urfBmAJTeL6vfxG6w2%2FoPecnrv2nX9Cnnpn2hDrGJ81nbMUoKHEUeRguqXojnPAh80hEJBya9cB0QZfyi0oS4wP%2FpUubwt6zhpDS6k4WzeSRVo4FdSXA2jZsBYEqHRusAND7Eoeqvafr5%2F8vvbzj9RfBD5wobiEuu9KDzD6pxxSaKGbAUefdgQZp%2F41fHArDbD4vWhSffU9%2BySJxIJwUwaIU7yCCUqi8QgdjAuQwsKLkDpts0wB3JmI9sXY1LkZ%2FwTAWpHQQonS7bVHYVirh3lBJqnspQA9M%2FLrmh9E2EsROXrSBZ4htibsaWJEefSTNDRaJGSg8AbUWz%2Fl77rRSDbSzS4wMAyMXve%2BCV1mX4BJZxgBKd4sJnZNayBHX8C7Oi%2B88K24A6YioVfgkhjJMTp2fei3hVJEs9tTtybljPktnhxkn7OYdjAXd92TP%2BSMZKnbzdDOktSzJuFXlvJDx0JkIQ87MsIhoEv9aUqKgIoKq0K6jIlUgE2x2%2BwAAYfxf%2BmlN1ohJQ4u7dfkkQ5Jr59GH4Lxw7z2mjddSOkVLsjH%2FkR7Jt7y9wWQ85Nof5HhYujUTt7%2Fz565MRRLCDrj1a1Og7uApWmSS9Ni%2FMIHi%2B7wGOqUBmdKNCt0x3nACQorrmhgZynjY0Y15FULzVICqTQ333oj1%2Bx6w8Uv6xByKC4GwB6XllYZf5TQ6fwh%2B9Pa1KH5VEbMv3hrk4LXN%2BQUg1bTRj31jI%2BCARL3mgWark1FiOuE%2F15OFm8RkQkHP1bzk7HhSm9fsJo0IJxm6dOTVez1yiza2lDd9ZTwM%2BWiKSXQvFrsHVrtA6wWR%2FWdNHNL%2FB3KQ29dFAMx2&X-Amz-Signature=2666a4f67d33fe4c980a80497db02a236daecb9a95ab9553d3cb3d9888db4aeb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# Predict on the same dataset
predictions = model.predict(X)

# Calculate training accuracy (MSE)
mse = mean_squared_error(y, predictions)
print(f'Mean Squared Error: {mse}')
```
7. **Train/Test Split:**
	- **Process:**
		- Split the dataset into training and testing sets (mutually exclusive).
		- Train the model on the training set.
		- Test the model on the test set by predicting target values.
		- Compare predicted values with actual values to calculate accuracy.
	- **Advantages:**
		- Provides a better evaluation of out-of-sample accuracy.
		- More realistic for real-world problems.
	- **Disadvantages:**
		- Dependent on the specific split of the dataset, which can introduce variation.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QNI4R45%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRdZOdyIKimM%2BKcXCQbQHNjOusgT0se0oxm25ChM4XagIhAK5%2FWA82A%2FSiYen4kBRAZL%2FqCLLjnmpEoMDYDo9HxZlUKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwI%2BnXdmDURlNm1Iwwq3ANwT59SY%2Bs6q7nUpAK5OKuDpjChADuwMgXq0ml1QafH33Ucw7waZCsT0F6TMHcy7U%2BQ6Ph5uR%2BFidWfodgCc98vk%2F3%2BNbORB4ey3UpSzqbPoMO713boH7Wf0tf7VbtgXDoNWcSgOwdTn9q%2Bo9R%2BE4zORlHq2inp124zhwIjQjHmLKozp7XxO5IDVE8fvlI0YVyd5CXohpPiB6bTqEz7%2FYzjePsTvp1rUEAeRRgkANjZ52Ok0b7EufPXsabssxTu%2B5VxuJcyhSQUOwaKBU%2FXm%2FNNudJoUnOaSGhZ7YiRN1khoQ%2FRJzNFN6jpyhXtFjBvxttOWqTl2BHMrEC2EyjnqaMXpmpEMcL3Rpe60qFH0t2WcfV9YbffJOORxw03v8prZVkFbT6ZzRI2XZxKguabHOCQclMICUq65YI1%2FHSzCYPr3BIGZi6VPUS6Qwz4oxkWa1FI4VfT%2Fkhz%2Bb5DNADqJkXCxOq7Jsty%2B5rGs8luNV1o69n6WGazEqGuSGKl8b%2FUWvYqX4rSXzoFIWvz2epo1K8rbp5Gkx%2BEEHxgooSwLZlT9KR8X90fr%2Fa9iu2fTglF2qTEzbjnNhd70wxTr8hfTXeVchp9uoXaKGc4XPAvWEuc68iWIue2AfBMHgNjZDCC4fu8BjqkAaFPnFu7Jj9WSyk4aQYxeHWfe1ZGTDy7mKjdXcYMRY0yzFxbyR8CKoQYS11tFaxDfMHIGeRsgrRouk6%2FIERtmJv56KdBPv1Us1HHJFXC4Payy1wH%2Bg94hggszvtihrkxcaQiGg34so%2FxGmu7OSjDy9Yg%2FY%2BkUK2YQqmrLnYzNzBkH3r0F7fI2k7PWuyM2vkAq94wz%2FDvP6FbtCevzIzBrSNf%2Fx3F&X-Amz-Signature=fee7d7f8862f58085c3edc53d49814dac42e30268a7d8f313142477ffb95188b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.model_selection import train_test_split

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Test the model on the test set
predictions = model.predict(X_test)

# Calculate out-of-sample accuracy (MSE)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error on Test Set: {mse}')
```
### Key Concepts
- **Training Accuracy:** The percentage of correct predictions the model makes on the training dataset. High training accuracy may indicate overfitting.
- **Out-of-Sample Accuracy:** The percentage of correct predictions the model makes on data it has not been trained on. High out-of-sample accuracy indicates better generalization to new data.
### K-Fold Cross-Validation
K-fold cross-validation is a method to address the dependency and variation issues in the train/test split approach. It provides a more consistent measure of out-of-sample accuracy by performing multiple train/test splits.
- **Process:**
	- Divide the dataset into  equal folds.
	- For each fold:
		- Use one fold as the test set and the remaining $ K−1 $ folds as the training set.
		- Train the model on the training set and evaluate it on the test set.
	- Repeat the process for each fold.
	- Average the accuracy results from all folds to obtain a final evaluation metric.
**Example with **$ K=4 $
- Split the dataset into 4 equal parts.
- In each iteration, use a different part as the test set and the rest as the training set.
- Compute accuracy for each fold and average the results.
**Advantages of K-Fold Cross-Validation:**
- Reduces the dependency on a specific train/test split.
- Provides a more reliable estimate of out-of-sample accuracy.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633OBDVBW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpRNGN636j8XoPKwH8TGoBHOznbcZ8b0dZvDXxgI1%2B%2BAIgMCacotSWnzz7eX4ycylyTx38%2BST3j4EuFu4Wcuu25MAqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPbc%2FSvHMszPPE574ircAz1M7gATFI8Zvs3zHu%2B4WLyLUr6tQ%2FSRguUAWvALKoifV0GRebIPfN%2FxXSi%2FmQk4kSnnmF1UoPudAERLsYuaZ7vJvbUtwV%2BHEkfzo4mHEVO1P6pFpJXrMrKl7N7VltFu4LEN9iI2N8jB7oGMj%2BYF%2BUt57CsUC5f4a1m8OEvVZ%2FczYOxWz6wwjb3nbP2H0QPrK1ppoGBT21%2Fi5hXVfbqXKU9Eku%2FZWG2IYWzIm9jyYacoM1WRfx1JkOVXXIevZEwUqFfZ2lzYnuvZhImb%2Barc%2BGxPXHL3j1owMq3A91a1QNvIBuAgTBTmN%2Bxjoj%2FupCJw3p22QSMzkqnXMNjZCgq4QUjRvvWkS3vjfatkXcGnxaLeZtexCCHvA91xlSKCagDU%2BZ%2FutrULzHE9NEtEs1wgzbCAO4rzWW7WsssEevlX%2FaV0dWh66yaXpko%2FD6t8ZkOM1AzkxOM7Ibsa3l6IDkzTxSrvqgWh%2FQkSK8qh5nXOJc9Iju9%2BkfGWr%2B0vKJJeo%2BXiuTdIdOivNId0D%2BfSdnlZAzwTTb9eIVZS3tfqUV9She69fHu8QQX07W%2BHHkNMupCKO9cz6cqEoUCVR39G0r%2B9K%2FKouhbu8v64371dnvWmgLfYNCgbV3RW%2FlXXD8zWMOjh%2B7wGOqUBD97mcC3xIC2dYearCxvacA5LRqZPnUcKr1sdzqxSvZHUOO3IuYAYysYA2GMc%2F%2BfaxNRCqX4Gkh1f59Qub48nKZHQUvukoLiRa%2BXjSH5oRQsNt68lRBUobikntunbqUr6SiRx3vd7qQnsR44ny2FlZ7ZUiy06q8kiJ09KPP%2F4SgKsxI%2B8RND9YL4CyyFcES9685smKlruD%2BKS66YTdvqKgx5gbR2D&X-Amz-Signature=ed7b3bf26456cf945f6bcf5487867e2b07294c5ee28e6649b0a3389f96673598&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.model_selection import cross_val_score

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Perform K-Fold Cross-Validation
scores = cross_val_score(model, X, y, cv=4, scoring='neg_mean_squared_error')
mse_scores = -scores
print(f'Mean Squared Error for each fold: {mse_scores}')
print(f'Average Mean Squared Error: {mse_scores.mean()}')
```
### **Formula for Mean Squared Error (MSE):**
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
 $$
Where $ y_i  $ are the actual values, $ \hat{y}_i  $ are the predicted values, and $ n  $ is the number of observations.
### Summary
- **Train and Test on the Same Dataset:** Simple but prone to overfitting with high training accuracy and low out-of-sample accuracy.
- **Train/Test Split:** Provides better out-of-sample accuracy but can still be affected by dataset dependency.
- **K-Fold Cross-Validation:** Mitigates issues of train/test split by averaging results over multiple splits, offering a more consistent evaluation metric.
___
## Model Evaluation Metrics for Regression
### Introduction
Evaluation metrics are essential for assessing the performance of a regression model. These metrics compare actual values to predicted values, providing insights into areas needing improvement. Several key metrics are used to evaluate regression models, including Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Relative Absolute Error (RAE), Relative Squared Error (RSE), and R-squared ($ R^2 $).
### Error Definition
In regression, the error is the difference between the actual data points and the predicted values from the model. This difference can be measured in various ways.
### Mean Absolute Error (MAE)
Mean Absolute Error is the average of the absolute differences between actual and predicted values. It is easy to understand and represents the average error in the same units as the data.
$$ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
 $$
#### Code Example
```python
from sklearn.metrics import mean_absolute_error

# Example data
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Calculate MAE
mae = mean_absolute_error(y_true, y_pred)
print(f"Mean Absolute Error: {mae}")
```
### Mean Squared Error (MSE)
Mean Squared Error is the average of the squared differences between actual and predicted values. It emphasizes larger errors more than smaller ones due to the squaring term, making it more sensitive to outliers.
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \frac{RSS}{n} $$
#### Code Example
```python
from sklearn.metrics import mean_squared_error

# Calculate MSE
mse = mean_squared_error(y_true, y_pred)
print(f"Mean Squared Error: {mse}")
```
### Root Mean Squared Error (RMSE)
Root Mean Squared Error is the square root of the mean squared error. It is popular because it is in the same units as the response variable, making it easier to interpret.
$$ \text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
 $$
#### Code Example
```python
import numpy as np

# Calculate RMSE
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")
```
### Relative Absolute Error (RAE)
Relative Absolute Error (RAE) is a metric expressed as a ratio normalizing the absolute error. It measures the average absolute difference between the actual and predicted values relative to the average absolute difference between the actual values and their mean.
$$ \text{RAE} = \frac{\sum_{i=1}^{n} |y_i - \hat{y}_i|}{\sum_{i=1}^{n} |y_i - \bar{y}|}
 $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
# Calculate RAE
rae = np.sum(np.abs(y_true - y_pred)) / np.sum(np.abs(y_true - np.mean(y_true)))
print(f"Relative Absolute Error: {rae}")
```
### Relative Squared Error (RSE)
Relative Squared Error is similar to RAE but uses squared differences. It is widely adopted for calculating $ R^2 $.
$$ \text{RSE} = \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
# Calculate RSE
rse = np.sum((y_true - y_pred) ** 2) / np.sum((y_true - np.mean(y_true)) ** 2)
print(f"Relative Squared Error: {rse}")
```
### R-squared ($ R^2 $)
R-squared is not an error metric per se (by itself), but it is a popular measure of model accuracy. It indicates how close the data points are to the fitted regression line. A higher $ R^2 $ value indicates a better fit.
$$ R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} = 1 - RSE $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
from sklearn.metrics import r2_score

# Calculate R-squared
r2 = r2_score(y_true, y_pred)
print(f"R-squared: {r2}")
```
### Residual Sum of Squares (RSS)
The Residual Sum of Squares (RSS) is a measure of the discrepancy between the data and an estimation model. It is calculated as the sum of the squared differences between the observed actual outcomes and the outcomes predicted by the model.
$$ \text{RSS} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = MSE * n $$
#### Code Example
```python
# Calculate RSS
rss = np.sum((y_true - y_pred) ** 2)
print(f"Residual Sum of Squares: {rss}")
```
### Summary
Each of these metrics quantifies different aspects of model performance. The choice of metric depends on the specific model, data type, and domain knowledge. Understanding and selecting the appropriate metric is crucial for evaluating and improving regression models.
___
## Multiple Linear Regression
### **Linear Regression Models**
- **Simple Linear Regression**: Utilizes one independent variable to estimate a dependent variable (e.g., predicting CO₂ emissions based on engine size).
- **Multiple Linear Regression**: Involves multiple independent variables to predict a dependent variable (e.g., predicting CO₂ emissions using engine size and the number of cylinders).
### **Applications of Multiple Linear Regression**
8. **Identifying Effect Strength**: Determines how independent variables affect the dependent variable. For instance, assessing how revision time, test anxiety, lecture attendance, and gender influence student exam performance.
9. **Predicting Impact of Changes**: Evaluates how changes in independent variables affect the dependent variable. For example, predicting how a patient's blood pressure changes with variations in body mass index, keeping other factors constant.
### **Model Representation**
- **Equation**: The model can be expressed as $ \hat{y}=θ_0+θ_1x_1+θ_2x_2+…+θ_nx_n $.
- **Vector Form**: In multidimensional space, the model is represented as $ \theta^T x $, where $ θ $ is the vector of parameters and $ x $ is the feature set. The first element of $ x $ is set to one to account for the intercept ($ \theta_0 $).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633OBDVBW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpRNGN636j8XoPKwH8TGoBHOznbcZ8b0dZvDXxgI1%2B%2BAIgMCacotSWnzz7eX4ycylyTx38%2BST3j4EuFu4Wcuu25MAqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPbc%2FSvHMszPPE574ircAz1M7gATFI8Zvs3zHu%2B4WLyLUr6tQ%2FSRguUAWvALKoifV0GRebIPfN%2FxXSi%2FmQk4kSnnmF1UoPudAERLsYuaZ7vJvbUtwV%2BHEkfzo4mHEVO1P6pFpJXrMrKl7N7VltFu4LEN9iI2N8jB7oGMj%2BYF%2BUt57CsUC5f4a1m8OEvVZ%2FczYOxWz6wwjb3nbP2H0QPrK1ppoGBT21%2Fi5hXVfbqXKU9Eku%2FZWG2IYWzIm9jyYacoM1WRfx1JkOVXXIevZEwUqFfZ2lzYnuvZhImb%2Barc%2BGxPXHL3j1owMq3A91a1QNvIBuAgTBTmN%2Bxjoj%2FupCJw3p22QSMzkqnXMNjZCgq4QUjRvvWkS3vjfatkXcGnxaLeZtexCCHvA91xlSKCagDU%2BZ%2FutrULzHE9NEtEs1wgzbCAO4rzWW7WsssEevlX%2FaV0dWh66yaXpko%2FD6t8ZkOM1AzkxOM7Ibsa3l6IDkzTxSrvqgWh%2FQkSK8qh5nXOJc9Iju9%2BkfGWr%2B0vKJJeo%2BXiuTdIdOivNId0D%2BfSdnlZAzwTTb9eIVZS3tfqUV9She69fHu8QQX07W%2BHHkNMupCKO9cz6cqEoUCVR39G0r%2B9K%2FKouhbu8v64371dnvWmgLfYNCgbV3RW%2FlXXD8zWMOjh%2B7wGOqUBD97mcC3xIC2dYearCxvacA5LRqZPnUcKr1sdzqxSvZHUOO3IuYAYysYA2GMc%2F%2BfaxNRCqX4Gkh1f59Qub48nKZHQUvukoLiRa%2BXjSH5oRQsNt68lRBUobikntunbqUr6SiRx3vd7qQnsR44ny2FlZ7ZUiy06q8kiJ09KPP%2F4SgKsxI%2B8RND9YL4CyyFcES9685smKlruD%2BKS66YTdvqKgx5gbR2D&X-Amz-Signature=08b1b9139dca6d38e02fbee324c044c074e702e26a990c12523cf390f8bb5a07&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
Here’s an example of implementing Multiple Linear Regression in Python using `scikit-learn`:
```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Example data
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])  # Independent variables
y = np.array([2, 3, 5, 7])                      # Dependent variable

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Coefficients and intercept
print(f'Intercept: {model.intercept_}')
print(f'Coefficients: {model.coef_}')

# Making predictions
predictions = model.predict(X)
print(f'Predictions: {predictions}')
```
### **Error and Optimization**
- **Error Calculation**: The error for a prediction is the difference between the actual and predicted values. For example, if the actual value $  y $ is 196 and the predicted value $ \hat{y} $ is 140, the error is $ 196−140=56 $.
- **Mean Squared Error (MSE)**: The average of the squared errors across all predictions. The objective is to minimize MSE to find the best parameters.
### **Parameter Estimation Methods**
10. **Ordinary Least Squares (OLS)**: Estimates coefficients by minimizing MSE using matrix operations. Suitable for smaller datasets but can be slow for larger ones.
11. **Optimization Algorithms**: Methods like `Gradient Descent` iteratively adjust coefficients to minimize error. Suitable for large datasets. Some Optimization Algorithms:` Gradient Descent, Stochastic Gradient Descent, Newton’s Metho`
#### **Code Example:**
Here's a simple implementation of Gradient Descent for linear regression:
```python
import numpy as np

def gradient_descent(X, y, learning_rate=0.01, iterations=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for _ in range(iterations):
        gradient = X.T @ (X @ theta - y) / m
        theta -= learning_rate * gradient
    return theta

# Example data
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])  # Independent variables
y = np.array([2, 3, 5, 7])                      # Dependent variable

# Adding intercept term (column of ones)
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# Apply gradient descent
theta = gradient_descent(X_b, y)
print(f'Optimized coefficients: {theta}')
```
### **Prediction Phase**
- **Using Parameters**: Once parameters are found, predictions are made by plugging input values into the model equation. For instance, with $ \theta_0 = 125 $, $ \theta_1 = 6.2 $, $ \theta_2 = 14 $, and input values, CO₂ emissions for a car can be predicted.
### **Concerns in Multiple Linear Regression**
- **Number of Variables**: Adding too many variables without justification can lead to overfitting, where the model becomes too complex and less generalizable.
- **Variable Types**: Categorical variables can be included by converting them to numerical values (e.g., coding car type as 0 or 1).
- **Linearity**: Ensure a linear relationship between the dependent variable and independent variables (maybe scatterplot). Non-linear relationships may require non-linear regression.
___
