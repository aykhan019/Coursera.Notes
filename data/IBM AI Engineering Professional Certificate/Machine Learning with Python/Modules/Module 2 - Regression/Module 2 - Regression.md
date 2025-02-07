

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZNJPI7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCICpIAd0xHFalRVE%2FxyjCW56jp%2BY5Maj92bnm4Lq3txQ%2BAiEA8kSHoyClheTwHULOR%2BOIKhh9up4%2FQWSxZDvRR9KMjCwq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLRCmjx7UJpzBJtWDCrcAwXLgGrMrQpvLy4zADFl%2BbkS7Dip222kis7LwYcvTwHaZOYYNANnFHnpQGDT50SRBTp%2FUfOkgkdDpy%2BLA7vsB2cDUic0lcifeWYuX0MFJr9mGmNx2YqN%2Fo9UyDoxU4iz1k9R9s0gCX3AhGn2iprnrUWsLdPC5IuKSjkAKsuqWVsuWKQNsCFCxzFjKXaEBZ13yFyo7%2BBaTV94obrJXxP4F%2BYTX%2Fj1rrm19XebBIsWldGGIpdABmJghxDL%2BWhFQ3lPAYF2LhyykLPAqlFWyynjuq6Q4N%2Fq5VdzKg4Vb5zkAZysVOJvBnEokY0Tbrd2U1ZVMfsDO5PQ%2BYxXmJrQ0EBuaw41EsQMXTwBFSWdoXRFPQ3F86YlabapxPsSYWQYaRmQiY15FpTPdOs2HpsqF1e5INOk2%2BezPRda0dqDC48G5xXa2XR5ClwbWjGA5c7iuV6yjXP2R1v4WGm0t5xQ9LGysKibrnzsad6YurcCwYGuFLgmaoEwG8XVBRnAsLjwLz960n48IsrShOdeqQ8pqPFtVPdPGlTwPeC%2FIcFFPP19mJe7WfriVObMR0mRsmkyAHT%2BasO3d9MpbYvHUWI4568zV2aZBE%2FFnUjxqsZMNxT5zx59qlXPRyqDUA5pwaSwMMf%2Bmb0GOqUBIig1OSVvXHHgJ%2BPseVSq3guQvWIis%2Bd3YShjceTj5kuNaG4q94krOPc0i9v0lZIqyyxsJnKAYeQQNsax6ouBoQSKsKIKG9Ze3srLpBcZ6tgAR2nNfJFJw5aHA2f%2BTyLl8U1Uh0pPxjUh8NYAEHYHavtFmwCU2CQD6xFuFBuls2gTFQ187Ner1hRu7ZqKu6TmtCHkAcB%2FfQIktksHPO%2F78GkBwpqa&X-Amz-Signature=9ca759cd3308f07fbb69305c65d6eec5a69a2a81f79e718aa12a8a31100c17b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZNJPI7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCICpIAd0xHFalRVE%2FxyjCW56jp%2BY5Maj92bnm4Lq3txQ%2BAiEA8kSHoyClheTwHULOR%2BOIKhh9up4%2FQWSxZDvRR9KMjCwq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLRCmjx7UJpzBJtWDCrcAwXLgGrMrQpvLy4zADFl%2BbkS7Dip222kis7LwYcvTwHaZOYYNANnFHnpQGDT50SRBTp%2FUfOkgkdDpy%2BLA7vsB2cDUic0lcifeWYuX0MFJr9mGmNx2YqN%2Fo9UyDoxU4iz1k9R9s0gCX3AhGn2iprnrUWsLdPC5IuKSjkAKsuqWVsuWKQNsCFCxzFjKXaEBZ13yFyo7%2BBaTV94obrJXxP4F%2BYTX%2Fj1rrm19XebBIsWldGGIpdABmJghxDL%2BWhFQ3lPAYF2LhyykLPAqlFWyynjuq6Q4N%2Fq5VdzKg4Vb5zkAZysVOJvBnEokY0Tbrd2U1ZVMfsDO5PQ%2BYxXmJrQ0EBuaw41EsQMXTwBFSWdoXRFPQ3F86YlabapxPsSYWQYaRmQiY15FpTPdOs2HpsqF1e5INOk2%2BezPRda0dqDC48G5xXa2XR5ClwbWjGA5c7iuV6yjXP2R1v4WGm0t5xQ9LGysKibrnzsad6YurcCwYGuFLgmaoEwG8XVBRnAsLjwLz960n48IsrShOdeqQ8pqPFtVPdPGlTwPeC%2FIcFFPP19mJe7WfriVObMR0mRsmkyAHT%2BasO3d9MpbYvHUWI4568zV2aZBE%2FFnUjxqsZMNxT5zx59qlXPRyqDUA5pwaSwMMf%2Bmb0GOqUBIig1OSVvXHHgJ%2BPseVSq3guQvWIis%2Bd3YShjceTj5kuNaG4q94krOPc0i9v0lZIqyyxsJnKAYeQQNsax6ouBoQSKsKIKG9Ze3srLpBcZ6tgAR2nNfJFJw5aHA2f%2BTyLl8U1Uh0pPxjUh8NYAEHYHavtFmwCU2CQD6xFuFBuls2gTFQ187Ner1hRu7ZqKu6TmtCHkAcB%2FfQIktksHPO%2F78GkBwpqa&X-Amz-Signature=509f4ff17a1df4d293f67042c92b624cb0a7fe19ab7951e6e296e6c1e112d370&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZNJPI7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCICpIAd0xHFalRVE%2FxyjCW56jp%2BY5Maj92bnm4Lq3txQ%2BAiEA8kSHoyClheTwHULOR%2BOIKhh9up4%2FQWSxZDvRR9KMjCwq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLRCmjx7UJpzBJtWDCrcAwXLgGrMrQpvLy4zADFl%2BbkS7Dip222kis7LwYcvTwHaZOYYNANnFHnpQGDT50SRBTp%2FUfOkgkdDpy%2BLA7vsB2cDUic0lcifeWYuX0MFJr9mGmNx2YqN%2Fo9UyDoxU4iz1k9R9s0gCX3AhGn2iprnrUWsLdPC5IuKSjkAKsuqWVsuWKQNsCFCxzFjKXaEBZ13yFyo7%2BBaTV94obrJXxP4F%2BYTX%2Fj1rrm19XebBIsWldGGIpdABmJghxDL%2BWhFQ3lPAYF2LhyykLPAqlFWyynjuq6Q4N%2Fq5VdzKg4Vb5zkAZysVOJvBnEokY0Tbrd2U1ZVMfsDO5PQ%2BYxXmJrQ0EBuaw41EsQMXTwBFSWdoXRFPQ3F86YlabapxPsSYWQYaRmQiY15FpTPdOs2HpsqF1e5INOk2%2BezPRda0dqDC48G5xXa2XR5ClwbWjGA5c7iuV6yjXP2R1v4WGm0t5xQ9LGysKibrnzsad6YurcCwYGuFLgmaoEwG8XVBRnAsLjwLz960n48IsrShOdeqQ8pqPFtVPdPGlTwPeC%2FIcFFPP19mJe7WfriVObMR0mRsmkyAHT%2BasO3d9MpbYvHUWI4568zV2aZBE%2FFnUjxqsZMNxT5zx59qlXPRyqDUA5pwaSwMMf%2Bmb0GOqUBIig1OSVvXHHgJ%2BPseVSq3guQvWIis%2Bd3YShjceTj5kuNaG4q94krOPc0i9v0lZIqyyxsJnKAYeQQNsax6ouBoQSKsKIKG9Ze3srLpBcZ6tgAR2nNfJFJw5aHA2f%2BTyLl8U1Uh0pPxjUh8NYAEHYHavtFmwCU2CQD6xFuFBuls2gTFQ187Ner1hRu7ZqKu6TmtCHkAcB%2FfQIktksHPO%2F78GkBwpqa&X-Amz-Signature=fd82c4bb3b3b7de9f714f296abf1602b416ee3d9ad0f63faa73a0c9dc4b836ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZNJPI7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCICpIAd0xHFalRVE%2FxyjCW56jp%2BY5Maj92bnm4Lq3txQ%2BAiEA8kSHoyClheTwHULOR%2BOIKhh9up4%2FQWSxZDvRR9KMjCwq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLRCmjx7UJpzBJtWDCrcAwXLgGrMrQpvLy4zADFl%2BbkS7Dip222kis7LwYcvTwHaZOYYNANnFHnpQGDT50SRBTp%2FUfOkgkdDpy%2BLA7vsB2cDUic0lcifeWYuX0MFJr9mGmNx2YqN%2Fo9UyDoxU4iz1k9R9s0gCX3AhGn2iprnrUWsLdPC5IuKSjkAKsuqWVsuWKQNsCFCxzFjKXaEBZ13yFyo7%2BBaTV94obrJXxP4F%2BYTX%2Fj1rrm19XebBIsWldGGIpdABmJghxDL%2BWhFQ3lPAYF2LhyykLPAqlFWyynjuq6Q4N%2Fq5VdzKg4Vb5zkAZysVOJvBnEokY0Tbrd2U1ZVMfsDO5PQ%2BYxXmJrQ0EBuaw41EsQMXTwBFSWdoXRFPQ3F86YlabapxPsSYWQYaRmQiY15FpTPdOs2HpsqF1e5INOk2%2BezPRda0dqDC48G5xXa2XR5ClwbWjGA5c7iuV6yjXP2R1v4WGm0t5xQ9LGysKibrnzsad6YurcCwYGuFLgmaoEwG8XVBRnAsLjwLz960n48IsrShOdeqQ8pqPFtVPdPGlTwPeC%2FIcFFPP19mJe7WfriVObMR0mRsmkyAHT%2BasO3d9MpbYvHUWI4568zV2aZBE%2FFnUjxqsZMNxT5zx59qlXPRyqDUA5pwaSwMMf%2Bmb0GOqUBIig1OSVvXHHgJ%2BPseVSq3guQvWIis%2Bd3YShjceTj5kuNaG4q94krOPc0i9v0lZIqyyxsJnKAYeQQNsax6ouBoQSKsKIKG9Ze3srLpBcZ6tgAR2nNfJFJw5aHA2f%2BTyLl8U1Uh0pPxjUh8NYAEHYHavtFmwCU2CQD6xFuFBuls2gTFQ187Ner1hRu7ZqKu6TmtCHkAcB%2FfQIktksHPO%2F78GkBwpqa&X-Amz-Signature=57321b88aeb20e314fad151c20e7ad29fba07bd640bdafd66d49f3c378c9fe4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZNJPI7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCICpIAd0xHFalRVE%2FxyjCW56jp%2BY5Maj92bnm4Lq3txQ%2BAiEA8kSHoyClheTwHULOR%2BOIKhh9up4%2FQWSxZDvRR9KMjCwq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLRCmjx7UJpzBJtWDCrcAwXLgGrMrQpvLy4zADFl%2BbkS7Dip222kis7LwYcvTwHaZOYYNANnFHnpQGDT50SRBTp%2FUfOkgkdDpy%2BLA7vsB2cDUic0lcifeWYuX0MFJr9mGmNx2YqN%2Fo9UyDoxU4iz1k9R9s0gCX3AhGn2iprnrUWsLdPC5IuKSjkAKsuqWVsuWKQNsCFCxzFjKXaEBZ13yFyo7%2BBaTV94obrJXxP4F%2BYTX%2Fj1rrm19XebBIsWldGGIpdABmJghxDL%2BWhFQ3lPAYF2LhyykLPAqlFWyynjuq6Q4N%2Fq5VdzKg4Vb5zkAZysVOJvBnEokY0Tbrd2U1ZVMfsDO5PQ%2BYxXmJrQ0EBuaw41EsQMXTwBFSWdoXRFPQ3F86YlabapxPsSYWQYaRmQiY15FpTPdOs2HpsqF1e5INOk2%2BezPRda0dqDC48G5xXa2XR5ClwbWjGA5c7iuV6yjXP2R1v4WGm0t5xQ9LGysKibrnzsad6YurcCwYGuFLgmaoEwG8XVBRnAsLjwLz960n48IsrShOdeqQ8pqPFtVPdPGlTwPeC%2FIcFFPP19mJe7WfriVObMR0mRsmkyAHT%2BasO3d9MpbYvHUWI4568zV2aZBE%2FFnUjxqsZMNxT5zx59qlXPRyqDUA5pwaSwMMf%2Bmb0GOqUBIig1OSVvXHHgJ%2BPseVSq3guQvWIis%2Bd3YShjceTj5kuNaG4q94krOPc0i9v0lZIqyyxsJnKAYeQQNsax6ouBoQSKsKIKG9Ze3srLpBcZ6tgAR2nNfJFJw5aHA2f%2BTyLl8U1Uh0pPxjUh8NYAEHYHavtFmwCU2CQD6xFuFBuls2gTFQ187Ner1hRu7ZqKu6TmtCHkAcB%2FfQIktksHPO%2F78GkBwpqa&X-Amz-Signature=f9577c16193bb4bf960ef0f06d11d0817dcb2567b1281e84a0ab98c36431011a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZNJPI7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCICpIAd0xHFalRVE%2FxyjCW56jp%2BY5Maj92bnm4Lq3txQ%2BAiEA8kSHoyClheTwHULOR%2BOIKhh9up4%2FQWSxZDvRR9KMjCwq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLRCmjx7UJpzBJtWDCrcAwXLgGrMrQpvLy4zADFl%2BbkS7Dip222kis7LwYcvTwHaZOYYNANnFHnpQGDT50SRBTp%2FUfOkgkdDpy%2BLA7vsB2cDUic0lcifeWYuX0MFJr9mGmNx2YqN%2Fo9UyDoxU4iz1k9R9s0gCX3AhGn2iprnrUWsLdPC5IuKSjkAKsuqWVsuWKQNsCFCxzFjKXaEBZ13yFyo7%2BBaTV94obrJXxP4F%2BYTX%2Fj1rrm19XebBIsWldGGIpdABmJghxDL%2BWhFQ3lPAYF2LhyykLPAqlFWyynjuq6Q4N%2Fq5VdzKg4Vb5zkAZysVOJvBnEokY0Tbrd2U1ZVMfsDO5PQ%2BYxXmJrQ0EBuaw41EsQMXTwBFSWdoXRFPQ3F86YlabapxPsSYWQYaRmQiY15FpTPdOs2HpsqF1e5INOk2%2BezPRda0dqDC48G5xXa2XR5ClwbWjGA5c7iuV6yjXP2R1v4WGm0t5xQ9LGysKibrnzsad6YurcCwYGuFLgmaoEwG8XVBRnAsLjwLz960n48IsrShOdeqQ8pqPFtVPdPGlTwPeC%2FIcFFPP19mJe7WfriVObMR0mRsmkyAHT%2BasO3d9MpbYvHUWI4568zV2aZBE%2FFnUjxqsZMNxT5zx59qlXPRyqDUA5pwaSwMMf%2Bmb0GOqUBIig1OSVvXHHgJ%2BPseVSq3guQvWIis%2Bd3YShjceTj5kuNaG4q94krOPc0i9v0lZIqyyxsJnKAYeQQNsax6ouBoQSKsKIKG9Ze3srLpBcZ6tgAR2nNfJFJw5aHA2f%2BTyLl8U1Uh0pPxjUh8NYAEHYHavtFmwCU2CQD6xFuFBuls2gTFQ187Ner1hRu7ZqKu6TmtCHkAcB%2FfQIktksHPO%2F78GkBwpqa&X-Amz-Signature=42e1fa0235d61188a0d726d94013cf9418d370b495432861e32e2ccd25eef033&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZNJPI7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCICpIAd0xHFalRVE%2FxyjCW56jp%2BY5Maj92bnm4Lq3txQ%2BAiEA8kSHoyClheTwHULOR%2BOIKhh9up4%2FQWSxZDvRR9KMjCwq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLRCmjx7UJpzBJtWDCrcAwXLgGrMrQpvLy4zADFl%2BbkS7Dip222kis7LwYcvTwHaZOYYNANnFHnpQGDT50SRBTp%2FUfOkgkdDpy%2BLA7vsB2cDUic0lcifeWYuX0MFJr9mGmNx2YqN%2Fo9UyDoxU4iz1k9R9s0gCX3AhGn2iprnrUWsLdPC5IuKSjkAKsuqWVsuWKQNsCFCxzFjKXaEBZ13yFyo7%2BBaTV94obrJXxP4F%2BYTX%2Fj1rrm19XebBIsWldGGIpdABmJghxDL%2BWhFQ3lPAYF2LhyykLPAqlFWyynjuq6Q4N%2Fq5VdzKg4Vb5zkAZysVOJvBnEokY0Tbrd2U1ZVMfsDO5PQ%2BYxXmJrQ0EBuaw41EsQMXTwBFSWdoXRFPQ3F86YlabapxPsSYWQYaRmQiY15FpTPdOs2HpsqF1e5INOk2%2BezPRda0dqDC48G5xXa2XR5ClwbWjGA5c7iuV6yjXP2R1v4WGm0t5xQ9LGysKibrnzsad6YurcCwYGuFLgmaoEwG8XVBRnAsLjwLz960n48IsrShOdeqQ8pqPFtVPdPGlTwPeC%2FIcFFPP19mJe7WfriVObMR0mRsmkyAHT%2BasO3d9MpbYvHUWI4568zV2aZBE%2FFnUjxqsZMNxT5zx59qlXPRyqDUA5pwaSwMMf%2Bmb0GOqUBIig1OSVvXHHgJ%2BPseVSq3guQvWIis%2Bd3YShjceTj5kuNaG4q94krOPc0i9v0lZIqyyxsJnKAYeQQNsax6ouBoQSKsKIKG9Ze3srLpBcZ6tgAR2nNfJFJw5aHA2f%2BTyLl8U1Uh0pPxjUh8NYAEHYHavtFmwCU2CQD6xFuFBuls2gTFQ187Ner1hRu7ZqKu6TmtCHkAcB%2FfQIktksHPO%2F78GkBwpqa&X-Amz-Signature=e68fc8da3c6ec28933b35eec7956a8fc110954161e121ef05620bfaa4e0961e6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZNJPI7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCICpIAd0xHFalRVE%2FxyjCW56jp%2BY5Maj92bnm4Lq3txQ%2BAiEA8kSHoyClheTwHULOR%2BOIKhh9up4%2FQWSxZDvRR9KMjCwq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLRCmjx7UJpzBJtWDCrcAwXLgGrMrQpvLy4zADFl%2BbkS7Dip222kis7LwYcvTwHaZOYYNANnFHnpQGDT50SRBTp%2FUfOkgkdDpy%2BLA7vsB2cDUic0lcifeWYuX0MFJr9mGmNx2YqN%2Fo9UyDoxU4iz1k9R9s0gCX3AhGn2iprnrUWsLdPC5IuKSjkAKsuqWVsuWKQNsCFCxzFjKXaEBZ13yFyo7%2BBaTV94obrJXxP4F%2BYTX%2Fj1rrm19XebBIsWldGGIpdABmJghxDL%2BWhFQ3lPAYF2LhyykLPAqlFWyynjuq6Q4N%2Fq5VdzKg4Vb5zkAZysVOJvBnEokY0Tbrd2U1ZVMfsDO5PQ%2BYxXmJrQ0EBuaw41EsQMXTwBFSWdoXRFPQ3F86YlabapxPsSYWQYaRmQiY15FpTPdOs2HpsqF1e5INOk2%2BezPRda0dqDC48G5xXa2XR5ClwbWjGA5c7iuV6yjXP2R1v4WGm0t5xQ9LGysKibrnzsad6YurcCwYGuFLgmaoEwG8XVBRnAsLjwLz960n48IsrShOdeqQ8pqPFtVPdPGlTwPeC%2FIcFFPP19mJe7WfriVObMR0mRsmkyAHT%2BasO3d9MpbYvHUWI4568zV2aZBE%2FFnUjxqsZMNxT5zx59qlXPRyqDUA5pwaSwMMf%2Bmb0GOqUBIig1OSVvXHHgJ%2BPseVSq3guQvWIis%2Bd3YShjceTj5kuNaG4q94krOPc0i9v0lZIqyyxsJnKAYeQQNsax6ouBoQSKsKIKG9Ze3srLpBcZ6tgAR2nNfJFJw5aHA2f%2BTyLl8U1Uh0pPxjUh8NYAEHYHavtFmwCU2CQD6xFuFBuls2gTFQ187Ner1hRu7ZqKu6TmtCHkAcB%2FfQIktksHPO%2F78GkBwpqa&X-Amz-Signature=37ba52dec701cb15861c2df7a7e9e1148d1f75b280a992f81d378b018d19f48f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL5PZ776%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIGPZzDq13UbBRAXvnxk1mNurheVDaWCp4rz5MdnoY12AAiBwPWtsv2SuQ6VWdElVGVaZW2K%2FB1c%2Fpmg1y5M2w6GdLCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMTIfF8UFffgaaQhGjKtwDnrlAKJbvBXLQTjuiitYwiQ5wJZwMIsiA8%2FVh0SyVC31u6Ya5ezAQIb2lQYwztU91eZKYJGpjVhH0Rh9B1OVODEi3PC8eB1bVhYc93JJQQtHjSuhXLqA0tZ02bDr0yivFrxqlKCXdejJiW8vgh61SamQbz7sIFeI%2BJFHDxluG%2FoatR8oxHm%2FbuRvK6iSArWPZt3gw9P9rpMM8rjODXawgY7i%2FY4Q3VJNjM8nfgS87eXCynsKfXlgExbfbnWrKWgDt7auU152Tgb6NMF8tXXTuBgrfOUZPPXE698Hq6%2Bx7nsR8%2FKlVMxnGg76Lzvzl83vYU1Fr5Y7bVx%2FM7W25gifJy8R8cyN%2BwTDQZ%2BYU3eFLwqlrlqtMuQ8WmwTZQeGmzX%2FELGK6W4%2Fovxe%2BYJo2TUXNgxihJ%2BhCUQPNkxqQKbux3fpINT9Y6%2F8BIJYpvBL7LzAx2CeP1U4t21Jfd2wwVDSou6iVUkdXUcF3Yoi8egR5%2B6OLmIbBEbLjzanYeXG0XLXAmwf81urxrgw3OjCDdWFxHd6%2BiOfKTnRQKCvC1GtwBShbs%2BWrL0GmAC6TUMO39pFH2RCuhCJjiFz5XDvhUs8mPw6Mqf5dnDkVSs0jp%2F59U%2Fd9fTQMpMhdSUxJsIIwlP6ZvQY6pgGt8UL%2BsMSdGF2FQmMiyjfuo%2FbE7gTCQ4j30pN0O4LgR%2BhXVZr61Rr4R%2F%2FvIQi9nnM9ciKyZeRIh0HzZeQZQJFbOHLL%2Fmgt1jP3qYPu%2BCXT4qb7ybwzpZKl3Wn3352AYAzypcnhhlJux%2Bdm%2BqNyaslihbA4cUJvOSQuJGTU5%2B6EcLUsrp9WSPC2skfiUTVaeA%2BJcgl9wdVrrtfVJYsmJweCwzThirvp&X-Amz-Signature=2497d93e95d962b9d4154bae55cea263ae5af5eebc8eecf7561bdeaaf4285265&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UAT7XP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDnjRnKcl0cYX7GYdi7QPUcusaaxqGew0LWTkOqwTuDOQIgXO04zExQ8CFK3b0pE%2F8F50n7uQo4walVYFntvR6i0G8q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDE%2Bc6LJgw7XPEQFYSircAxTdnwNlTs%2BfCkCQQ2T8Jb5kncSBww%2BNgXTo0NKr5QUlvnVNN%2Bsx2yG36nBxrmxP44HE1KWKYxCjoukxKhS6JL1CI27S6T7F56AJErwDgi3Ytr%2FXMMLNKbp9mWpvU2CUusPACcGrWw3Qz0vm7faHMnVzT5ASm%2F%2B77d8oVPF8zag9TnXPnLRM6MaTiXVpA6VoU2cIHhgp7sUPJDEy%2F7pBBF6I6eL2dnZbgWfQ6lFMMUjxJkWo2kDuKN0m0R5l87I6v9pX31NPyrDGjhyN6FcUSaHX%2BoNgQKmLtGaA3ssuSOsTGkoJ%2BrCfvr1eaN57HUWeQaXJ4KEKSow33SAFZ8VMKhzC4AnexDHmlB5EFJxvhJ3E0VvOO9xMkn4CSXaN91AS%2F7Ku0BcLGN40DCS9ILL61Z0NDO0Z362pfwOZXVbAOv%2Blj%2BEV%2FTJHjM%2BL9jOGpgjIYxnAcm6B8ud17GJmXvXb%2BTaLz0tb%2FnePMzDCdyWsCdDxvMO7XiUNOX8eys%2B7w%2BH32SDBfmyDT%2BZxA7hqI3GxH8C87DNnvltTXcmlzCiV%2FNMMhizjmBciQsJv%2B5uElQ3JVTNEd44C4m77LsYFTqtgQsvarU2x8S6O9mOWWoP5cMktmgGquQ3VEJaF8WHjMLP%2Bmb0GOqUBqmLpPtu1L6Vuvx%2BxvycfiYoi4OGibOR4KiJIYSkN%2FaSA8feLBDurvak%2BIu3VS8ucgkKBMz8R8y9atnOacZZpZLV9X6PjIFmTE9V6iv8mcfY4TMZtPhNpTiD6CTFUOKo%2FoeMTYdKn4AAeYfVUjviqBPA%2B4fbUkQ1ZVmTnpJRXsg0hmN5gvL5o4Gm2EuqI0%2BcQ1HJMxFMOiXy61sxgaorzJVpZwoGj&X-Amz-Signature=d9442f50ff74d54efdfc4fbebc21c31ca4a168b7c4d30f50190f86c61c3a76b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EE6OWVJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFKgG1MdLmy4%2FdJhIkciluwxg%2FiZFgyLo5WYhwOBWEiWAiEAmizn%2B2IfGX%2FH006rhihaTVqR1%2BBFDrP9IKufd7f5bPoq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOXvRdJpPqtDuQq6MircA%2FXxhS5Wk6a6TheqanYaJZs0EhNwu5QTtfDmul%2ByADyEvyUkGvkvd5lu5g%2BskiFnxDBsBta6hhOv0cFfzH2RumJPhjTlI1jb1YDgjeYWf9643Fy8ysQfMyNPBa%2B5lacefp614lhoytFFTlMWH0Egf%2B%2FrlStQZxhB4iigQUvYDGzKQ6Y6dfzDZnhZeOdd4rogbcN%2BDyl3STh2v4qSvgrkYQOGcMy6LNDIlaDgbZEWhs%2BpIv9QEQLS5eAqHh32V%2FHJPFeVLsPhU5PHxuKX%2BQBtGjfqsRn43Lw9RMHJc2Kfw5yQO3S%2BjqeXc2lWAzn%2FPv%2FjulOFo0t1ZfeQT%2B8qWvRU3kz6ShvcepI8YbaDpoYPfCjn6HrdbIQcwTYUwhfS1T%2FOSYGmIdhZGpRmjE%2BkuYQTNIfi4i8o1Z6J7%2FqyP%2BU%2BUZa1uFInwgCvmXzp5MhR%2BMBB%2B%2Bep%2FbxDWtA%2BXGmxcjmjoEsIj1JIfPsb7Ygmv5EWosEoWlGNHpjFk%2Bge6C98bth9BU4Vu7dt1WQZ6CNs%2FxfiJNC%2BDrTnd9Ay3fsSsi6uAQvl331Em%2FmwfhOlB1L0Hf0%2BDxI0m2OFLaqzBSyokDWAXzMIZqw0HxZ9qeu8EZ2riQsqeoI1NSORxcPkszxDMNX%2Bmb0GOqUB2sFePfCQbDq%2FfANMyVb%2F9uXN5nJBVbsmmMb7VcWfcHKWau5S9AX8JhEM7%2F%2BX5MPstdhKi3V2u8XcyAGyIQvPhmLCmSnsmoFXGpFSi74Q7t7zlM7BWmKbB3g9%2BTno6e%2BgLIHa%2FDLVItCY0UA9o6%2BEfNM%2FpjbnC0EsUdz6CLarhvkF5hPOSz6gHu2mj%2Bk%2F5Rw0f%2BAXPCG0AtH6SgeazboqnQORBfHl&X-Amz-Signature=3cc196e7fc0e5ac1943894298ab37356a76d08d14d85ec9cf85352bf608eb51f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EE6OWVJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFKgG1MdLmy4%2FdJhIkciluwxg%2FiZFgyLo5WYhwOBWEiWAiEAmizn%2B2IfGX%2FH006rhihaTVqR1%2BBFDrP9IKufd7f5bPoq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOXvRdJpPqtDuQq6MircA%2FXxhS5Wk6a6TheqanYaJZs0EhNwu5QTtfDmul%2ByADyEvyUkGvkvd5lu5g%2BskiFnxDBsBta6hhOv0cFfzH2RumJPhjTlI1jb1YDgjeYWf9643Fy8ysQfMyNPBa%2B5lacefp614lhoytFFTlMWH0Egf%2B%2FrlStQZxhB4iigQUvYDGzKQ6Y6dfzDZnhZeOdd4rogbcN%2BDyl3STh2v4qSvgrkYQOGcMy6LNDIlaDgbZEWhs%2BpIv9QEQLS5eAqHh32V%2FHJPFeVLsPhU5PHxuKX%2BQBtGjfqsRn43Lw9RMHJc2Kfw5yQO3S%2BjqeXc2lWAzn%2FPv%2FjulOFo0t1ZfeQT%2B8qWvRU3kz6ShvcepI8YbaDpoYPfCjn6HrdbIQcwTYUwhfS1T%2FOSYGmIdhZGpRmjE%2BkuYQTNIfi4i8o1Z6J7%2FqyP%2BU%2BUZa1uFInwgCvmXzp5MhR%2BMBB%2B%2Bep%2FbxDWtA%2BXGmxcjmjoEsIj1JIfPsb7Ygmv5EWosEoWlGNHpjFk%2Bge6C98bth9BU4Vu7dt1WQZ6CNs%2FxfiJNC%2BDrTnd9Ay3fsSsi6uAQvl331Em%2FmwfhOlB1L0Hf0%2BDxI0m2OFLaqzBSyokDWAXzMIZqw0HxZ9qeu8EZ2riQsqeoI1NSORxcPkszxDMNX%2Bmb0GOqUB2sFePfCQbDq%2FfANMyVb%2F9uXN5nJBVbsmmMb7VcWfcHKWau5S9AX8JhEM7%2F%2BX5MPstdhKi3V2u8XcyAGyIQvPhmLCmSnsmoFXGpFSi74Q7t7zlM7BWmKbB3g9%2BTno6e%2BgLIHa%2FDLVItCY0UA9o6%2BEfNM%2FpjbnC0EsUdz6CLarhvkF5hPOSz6gHu2mj%2Bk%2F5Rw0f%2BAXPCG0AtH6SgeazboqnQORBfHl&X-Amz-Signature=0a43c274680290dd29fd00ae5b74a22f8921fc2f495022304651ee583fe3c851&X-Amz-SignedHeaders=host&x-id=GetObject)
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
