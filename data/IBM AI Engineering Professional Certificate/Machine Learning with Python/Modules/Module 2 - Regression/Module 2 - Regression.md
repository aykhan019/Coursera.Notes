

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ANYGBQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDVNg1QAI%2BjXN0wQupRnQ%2FmYYScPBIbTy68cEkNwi%2BJVQIhAPSyJ8ywJZSb%2FRsBBehnwbTpF37n1cplK0cSMEPQkTAnKv8DCEoQABoMNjM3NDIzMTgzODA1Igw7YSe8icVf9Ra%2BCbYq3API%2FsHWbrWRDWBxQKqQ1hOGZEQMu5CnhzxVdWIAOpSTvob9zPpgaBUd66z%2BKqmMmyPZzjTkp2BjxTQeR9ZVkqLdHkmIJl4AssS%2Fif20%2FV52Ft8QBeLiIM0Gyvp19fuoV0tRv8c6%2FgyKVDgijSu0tOgqWLXZitXDAHEixD1uSiR4wYRYC%2FOBbDl2dK04FAU0mKKn%2Fd5Swp5obSkuLKnu7zkXK86nUmY2UeU9WvVRW00hioypkTWCx9O99YfBS2bKrTx6TQNEEQiUZGNx%2FkjiAPAy8TK2eeJ6ghobbugKTjnonVStu0cV39f7gCnrTZ%2Bsf%2Bn36vd%2BWw%2BJnpRq%2F%2BEvaQipLcrLhIT7yqBgd93HZm0WwT%2FBFr0tibBe%2F1Pvvkag9YmQMyMmpCHf1ikJLh6tyY3u5T1Et1wHqbP9qChJ9587O%2FkqjyltdNMhNZrg4hHa2Y7xuRtp1mbwJIR26Aa2QaQeEbbYQdBLt6Ic6SPywWFctUCpBWcOe2SqgqGSSbexBQF1JbPh8GY%2FRQ6Be7NX2xe7bOb66lSODj92FZLjIexVLo%2BCkSEO3OC8jlvcs0U2eai%2BkYT0TRU3DkZbwP2Rw129o1y4B4WhgMewp5hMWj5I1N0OOqEneT0JK%2BFkNjDcuo69BjqkAabN8x7TZ8Ta062dYWPj%2BKLzxjperb95G%2FHFuvEkYMe84lv23pRdOGlj%2Fq3647SS6ibEWrTpmzoRCCXgt6FCWPgoktAz%2B0Z4WZaVx7Ikor3Jz0iH6bEPcsHKsFeqXEokZsx7K7AHmvRo2GwurR0gwcG%2FO1b6yzJ8wfQ9AjXVr9IgAqwB1Vo%2BrujFfCf6vSX4g4fP7pU0ptOhMDkmfwFJu%2Fkec9Fu&X-Amz-Signature=d5b5efda7257eebfb45043d547d898c0a38caaa1b90ba0cbec499bab27a4b55b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ANYGBQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDVNg1QAI%2BjXN0wQupRnQ%2FmYYScPBIbTy68cEkNwi%2BJVQIhAPSyJ8ywJZSb%2FRsBBehnwbTpF37n1cplK0cSMEPQkTAnKv8DCEoQABoMNjM3NDIzMTgzODA1Igw7YSe8icVf9Ra%2BCbYq3API%2FsHWbrWRDWBxQKqQ1hOGZEQMu5CnhzxVdWIAOpSTvob9zPpgaBUd66z%2BKqmMmyPZzjTkp2BjxTQeR9ZVkqLdHkmIJl4AssS%2Fif20%2FV52Ft8QBeLiIM0Gyvp19fuoV0tRv8c6%2FgyKVDgijSu0tOgqWLXZitXDAHEixD1uSiR4wYRYC%2FOBbDl2dK04FAU0mKKn%2Fd5Swp5obSkuLKnu7zkXK86nUmY2UeU9WvVRW00hioypkTWCx9O99YfBS2bKrTx6TQNEEQiUZGNx%2FkjiAPAy8TK2eeJ6ghobbugKTjnonVStu0cV39f7gCnrTZ%2Bsf%2Bn36vd%2BWw%2BJnpRq%2F%2BEvaQipLcrLhIT7yqBgd93HZm0WwT%2FBFr0tibBe%2F1Pvvkag9YmQMyMmpCHf1ikJLh6tyY3u5T1Et1wHqbP9qChJ9587O%2FkqjyltdNMhNZrg4hHa2Y7xuRtp1mbwJIR26Aa2QaQeEbbYQdBLt6Ic6SPywWFctUCpBWcOe2SqgqGSSbexBQF1JbPh8GY%2FRQ6Be7NX2xe7bOb66lSODj92FZLjIexVLo%2BCkSEO3OC8jlvcs0U2eai%2BkYT0TRU3DkZbwP2Rw129o1y4B4WhgMewp5hMWj5I1N0OOqEneT0JK%2BFkNjDcuo69BjqkAabN8x7TZ8Ta062dYWPj%2BKLzxjperb95G%2FHFuvEkYMe84lv23pRdOGlj%2Fq3647SS6ibEWrTpmzoRCCXgt6FCWPgoktAz%2B0Z4WZaVx7Ikor3Jz0iH6bEPcsHKsFeqXEokZsx7K7AHmvRo2GwurR0gwcG%2FO1b6yzJ8wfQ9AjXVr9IgAqwB1Vo%2BrujFfCf6vSX4g4fP7pU0ptOhMDkmfwFJu%2Fkec9Fu&X-Amz-Signature=10fa0fb14eb06069540854368c41bd16786c7551994f7e25187c919e12fab277&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ANYGBQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDVNg1QAI%2BjXN0wQupRnQ%2FmYYScPBIbTy68cEkNwi%2BJVQIhAPSyJ8ywJZSb%2FRsBBehnwbTpF37n1cplK0cSMEPQkTAnKv8DCEoQABoMNjM3NDIzMTgzODA1Igw7YSe8icVf9Ra%2BCbYq3API%2FsHWbrWRDWBxQKqQ1hOGZEQMu5CnhzxVdWIAOpSTvob9zPpgaBUd66z%2BKqmMmyPZzjTkp2BjxTQeR9ZVkqLdHkmIJl4AssS%2Fif20%2FV52Ft8QBeLiIM0Gyvp19fuoV0tRv8c6%2FgyKVDgijSu0tOgqWLXZitXDAHEixD1uSiR4wYRYC%2FOBbDl2dK04FAU0mKKn%2Fd5Swp5obSkuLKnu7zkXK86nUmY2UeU9WvVRW00hioypkTWCx9O99YfBS2bKrTx6TQNEEQiUZGNx%2FkjiAPAy8TK2eeJ6ghobbugKTjnonVStu0cV39f7gCnrTZ%2Bsf%2Bn36vd%2BWw%2BJnpRq%2F%2BEvaQipLcrLhIT7yqBgd93HZm0WwT%2FBFr0tibBe%2F1Pvvkag9YmQMyMmpCHf1ikJLh6tyY3u5T1Et1wHqbP9qChJ9587O%2FkqjyltdNMhNZrg4hHa2Y7xuRtp1mbwJIR26Aa2QaQeEbbYQdBLt6Ic6SPywWFctUCpBWcOe2SqgqGSSbexBQF1JbPh8GY%2FRQ6Be7NX2xe7bOb66lSODj92FZLjIexVLo%2BCkSEO3OC8jlvcs0U2eai%2BkYT0TRU3DkZbwP2Rw129o1y4B4WhgMewp5hMWj5I1N0OOqEneT0JK%2BFkNjDcuo69BjqkAabN8x7TZ8Ta062dYWPj%2BKLzxjperb95G%2FHFuvEkYMe84lv23pRdOGlj%2Fq3647SS6ibEWrTpmzoRCCXgt6FCWPgoktAz%2B0Z4WZaVx7Ikor3Jz0iH6bEPcsHKsFeqXEokZsx7K7AHmvRo2GwurR0gwcG%2FO1b6yzJ8wfQ9AjXVr9IgAqwB1Vo%2BrujFfCf6vSX4g4fP7pU0ptOhMDkmfwFJu%2Fkec9Fu&X-Amz-Signature=d22aaabf766c3b855687ce346b2a19247924dd7c2eccdf78f3e9a2fbcdb711bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ANYGBQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDVNg1QAI%2BjXN0wQupRnQ%2FmYYScPBIbTy68cEkNwi%2BJVQIhAPSyJ8ywJZSb%2FRsBBehnwbTpF37n1cplK0cSMEPQkTAnKv8DCEoQABoMNjM3NDIzMTgzODA1Igw7YSe8icVf9Ra%2BCbYq3API%2FsHWbrWRDWBxQKqQ1hOGZEQMu5CnhzxVdWIAOpSTvob9zPpgaBUd66z%2BKqmMmyPZzjTkp2BjxTQeR9ZVkqLdHkmIJl4AssS%2Fif20%2FV52Ft8QBeLiIM0Gyvp19fuoV0tRv8c6%2FgyKVDgijSu0tOgqWLXZitXDAHEixD1uSiR4wYRYC%2FOBbDl2dK04FAU0mKKn%2Fd5Swp5obSkuLKnu7zkXK86nUmY2UeU9WvVRW00hioypkTWCx9O99YfBS2bKrTx6TQNEEQiUZGNx%2FkjiAPAy8TK2eeJ6ghobbugKTjnonVStu0cV39f7gCnrTZ%2Bsf%2Bn36vd%2BWw%2BJnpRq%2F%2BEvaQipLcrLhIT7yqBgd93HZm0WwT%2FBFr0tibBe%2F1Pvvkag9YmQMyMmpCHf1ikJLh6tyY3u5T1Et1wHqbP9qChJ9587O%2FkqjyltdNMhNZrg4hHa2Y7xuRtp1mbwJIR26Aa2QaQeEbbYQdBLt6Ic6SPywWFctUCpBWcOe2SqgqGSSbexBQF1JbPh8GY%2FRQ6Be7NX2xe7bOb66lSODj92FZLjIexVLo%2BCkSEO3OC8jlvcs0U2eai%2BkYT0TRU3DkZbwP2Rw129o1y4B4WhgMewp5hMWj5I1N0OOqEneT0JK%2BFkNjDcuo69BjqkAabN8x7TZ8Ta062dYWPj%2BKLzxjperb95G%2FHFuvEkYMe84lv23pRdOGlj%2Fq3647SS6ibEWrTpmzoRCCXgt6FCWPgoktAz%2B0Z4WZaVx7Ikor3Jz0iH6bEPcsHKsFeqXEokZsx7K7AHmvRo2GwurR0gwcG%2FO1b6yzJ8wfQ9AjXVr9IgAqwB1Vo%2BrujFfCf6vSX4g4fP7pU0ptOhMDkmfwFJu%2Fkec9Fu&X-Amz-Signature=379386c6d558a86fe26367f7de59409a99ee88ce75f3818813e944d9d3ccda3d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ANYGBQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDVNg1QAI%2BjXN0wQupRnQ%2FmYYScPBIbTy68cEkNwi%2BJVQIhAPSyJ8ywJZSb%2FRsBBehnwbTpF37n1cplK0cSMEPQkTAnKv8DCEoQABoMNjM3NDIzMTgzODA1Igw7YSe8icVf9Ra%2BCbYq3API%2FsHWbrWRDWBxQKqQ1hOGZEQMu5CnhzxVdWIAOpSTvob9zPpgaBUd66z%2BKqmMmyPZzjTkp2BjxTQeR9ZVkqLdHkmIJl4AssS%2Fif20%2FV52Ft8QBeLiIM0Gyvp19fuoV0tRv8c6%2FgyKVDgijSu0tOgqWLXZitXDAHEixD1uSiR4wYRYC%2FOBbDl2dK04FAU0mKKn%2Fd5Swp5obSkuLKnu7zkXK86nUmY2UeU9WvVRW00hioypkTWCx9O99YfBS2bKrTx6TQNEEQiUZGNx%2FkjiAPAy8TK2eeJ6ghobbugKTjnonVStu0cV39f7gCnrTZ%2Bsf%2Bn36vd%2BWw%2BJnpRq%2F%2BEvaQipLcrLhIT7yqBgd93HZm0WwT%2FBFr0tibBe%2F1Pvvkag9YmQMyMmpCHf1ikJLh6tyY3u5T1Et1wHqbP9qChJ9587O%2FkqjyltdNMhNZrg4hHa2Y7xuRtp1mbwJIR26Aa2QaQeEbbYQdBLt6Ic6SPywWFctUCpBWcOe2SqgqGSSbexBQF1JbPh8GY%2FRQ6Be7NX2xe7bOb66lSODj92FZLjIexVLo%2BCkSEO3OC8jlvcs0U2eai%2BkYT0TRU3DkZbwP2Rw129o1y4B4WhgMewp5hMWj5I1N0OOqEneT0JK%2BFkNjDcuo69BjqkAabN8x7TZ8Ta062dYWPj%2BKLzxjperb95G%2FHFuvEkYMe84lv23pRdOGlj%2Fq3647SS6ibEWrTpmzoRCCXgt6FCWPgoktAz%2B0Z4WZaVx7Ikor3Jz0iH6bEPcsHKsFeqXEokZsx7K7AHmvRo2GwurR0gwcG%2FO1b6yzJ8wfQ9AjXVr9IgAqwB1Vo%2BrujFfCf6vSX4g4fP7pU0ptOhMDkmfwFJu%2Fkec9Fu&X-Amz-Signature=70f93d407aad6f4497ad632b91694b6907680db0f90b08018415fe8d2f34589f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ANYGBQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDVNg1QAI%2BjXN0wQupRnQ%2FmYYScPBIbTy68cEkNwi%2BJVQIhAPSyJ8ywJZSb%2FRsBBehnwbTpF37n1cplK0cSMEPQkTAnKv8DCEoQABoMNjM3NDIzMTgzODA1Igw7YSe8icVf9Ra%2BCbYq3API%2FsHWbrWRDWBxQKqQ1hOGZEQMu5CnhzxVdWIAOpSTvob9zPpgaBUd66z%2BKqmMmyPZzjTkp2BjxTQeR9ZVkqLdHkmIJl4AssS%2Fif20%2FV52Ft8QBeLiIM0Gyvp19fuoV0tRv8c6%2FgyKVDgijSu0tOgqWLXZitXDAHEixD1uSiR4wYRYC%2FOBbDl2dK04FAU0mKKn%2Fd5Swp5obSkuLKnu7zkXK86nUmY2UeU9WvVRW00hioypkTWCx9O99YfBS2bKrTx6TQNEEQiUZGNx%2FkjiAPAy8TK2eeJ6ghobbugKTjnonVStu0cV39f7gCnrTZ%2Bsf%2Bn36vd%2BWw%2BJnpRq%2F%2BEvaQipLcrLhIT7yqBgd93HZm0WwT%2FBFr0tibBe%2F1Pvvkag9YmQMyMmpCHf1ikJLh6tyY3u5T1Et1wHqbP9qChJ9587O%2FkqjyltdNMhNZrg4hHa2Y7xuRtp1mbwJIR26Aa2QaQeEbbYQdBLt6Ic6SPywWFctUCpBWcOe2SqgqGSSbexBQF1JbPh8GY%2FRQ6Be7NX2xe7bOb66lSODj92FZLjIexVLo%2BCkSEO3OC8jlvcs0U2eai%2BkYT0TRU3DkZbwP2Rw129o1y4B4WhgMewp5hMWj5I1N0OOqEneT0JK%2BFkNjDcuo69BjqkAabN8x7TZ8Ta062dYWPj%2BKLzxjperb95G%2FHFuvEkYMe84lv23pRdOGlj%2Fq3647SS6ibEWrTpmzoRCCXgt6FCWPgoktAz%2B0Z4WZaVx7Ikor3Jz0iH6bEPcsHKsFeqXEokZsx7K7AHmvRo2GwurR0gwcG%2FO1b6yzJ8wfQ9AjXVr9IgAqwB1Vo%2BrujFfCf6vSX4g4fP7pU0ptOhMDkmfwFJu%2Fkec9Fu&X-Amz-Signature=ad26b35f380451f54850b22deeecc148bb6cbbc54752d1e09156911632aed672&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ANYGBQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDVNg1QAI%2BjXN0wQupRnQ%2FmYYScPBIbTy68cEkNwi%2BJVQIhAPSyJ8ywJZSb%2FRsBBehnwbTpF37n1cplK0cSMEPQkTAnKv8DCEoQABoMNjM3NDIzMTgzODA1Igw7YSe8icVf9Ra%2BCbYq3API%2FsHWbrWRDWBxQKqQ1hOGZEQMu5CnhzxVdWIAOpSTvob9zPpgaBUd66z%2BKqmMmyPZzjTkp2BjxTQeR9ZVkqLdHkmIJl4AssS%2Fif20%2FV52Ft8QBeLiIM0Gyvp19fuoV0tRv8c6%2FgyKVDgijSu0tOgqWLXZitXDAHEixD1uSiR4wYRYC%2FOBbDl2dK04FAU0mKKn%2Fd5Swp5obSkuLKnu7zkXK86nUmY2UeU9WvVRW00hioypkTWCx9O99YfBS2bKrTx6TQNEEQiUZGNx%2FkjiAPAy8TK2eeJ6ghobbugKTjnonVStu0cV39f7gCnrTZ%2Bsf%2Bn36vd%2BWw%2BJnpRq%2F%2BEvaQipLcrLhIT7yqBgd93HZm0WwT%2FBFr0tibBe%2F1Pvvkag9YmQMyMmpCHf1ikJLh6tyY3u5T1Et1wHqbP9qChJ9587O%2FkqjyltdNMhNZrg4hHa2Y7xuRtp1mbwJIR26Aa2QaQeEbbYQdBLt6Ic6SPywWFctUCpBWcOe2SqgqGSSbexBQF1JbPh8GY%2FRQ6Be7NX2xe7bOb66lSODj92FZLjIexVLo%2BCkSEO3OC8jlvcs0U2eai%2BkYT0TRU3DkZbwP2Rw129o1y4B4WhgMewp5hMWj5I1N0OOqEneT0JK%2BFkNjDcuo69BjqkAabN8x7TZ8Ta062dYWPj%2BKLzxjperb95G%2FHFuvEkYMe84lv23pRdOGlj%2Fq3647SS6ibEWrTpmzoRCCXgt6FCWPgoktAz%2B0Z4WZaVx7Ikor3Jz0iH6bEPcsHKsFeqXEokZsx7K7AHmvRo2GwurR0gwcG%2FO1b6yzJ8wfQ9AjXVr9IgAqwB1Vo%2BrujFfCf6vSX4g4fP7pU0ptOhMDkmfwFJu%2Fkec9Fu&X-Amz-Signature=68f9ae4506526e82fad4e84268270307f2faf0167b15b3d4bebf770d9a843af2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ANYGBQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDVNg1QAI%2BjXN0wQupRnQ%2FmYYScPBIbTy68cEkNwi%2BJVQIhAPSyJ8ywJZSb%2FRsBBehnwbTpF37n1cplK0cSMEPQkTAnKv8DCEoQABoMNjM3NDIzMTgzODA1Igw7YSe8icVf9Ra%2BCbYq3API%2FsHWbrWRDWBxQKqQ1hOGZEQMu5CnhzxVdWIAOpSTvob9zPpgaBUd66z%2BKqmMmyPZzjTkp2BjxTQeR9ZVkqLdHkmIJl4AssS%2Fif20%2FV52Ft8QBeLiIM0Gyvp19fuoV0tRv8c6%2FgyKVDgijSu0tOgqWLXZitXDAHEixD1uSiR4wYRYC%2FOBbDl2dK04FAU0mKKn%2Fd5Swp5obSkuLKnu7zkXK86nUmY2UeU9WvVRW00hioypkTWCx9O99YfBS2bKrTx6TQNEEQiUZGNx%2FkjiAPAy8TK2eeJ6ghobbugKTjnonVStu0cV39f7gCnrTZ%2Bsf%2Bn36vd%2BWw%2BJnpRq%2F%2BEvaQipLcrLhIT7yqBgd93HZm0WwT%2FBFr0tibBe%2F1Pvvkag9YmQMyMmpCHf1ikJLh6tyY3u5T1Et1wHqbP9qChJ9587O%2FkqjyltdNMhNZrg4hHa2Y7xuRtp1mbwJIR26Aa2QaQeEbbYQdBLt6Ic6SPywWFctUCpBWcOe2SqgqGSSbexBQF1JbPh8GY%2FRQ6Be7NX2xe7bOb66lSODj92FZLjIexVLo%2BCkSEO3OC8jlvcs0U2eai%2BkYT0TRU3DkZbwP2Rw129o1y4B4WhgMewp5hMWj5I1N0OOqEneT0JK%2BFkNjDcuo69BjqkAabN8x7TZ8Ta062dYWPj%2BKLzxjperb95G%2FHFuvEkYMe84lv23pRdOGlj%2Fq3647SS6ibEWrTpmzoRCCXgt6FCWPgoktAz%2B0Z4WZaVx7Ikor3Jz0iH6bEPcsHKsFeqXEokZsx7K7AHmvRo2GwurR0gwcG%2FO1b6yzJ8wfQ9AjXVr9IgAqwB1Vo%2BrujFfCf6vSX4g4fP7pU0ptOhMDkmfwFJu%2Fkec9Fu&X-Amz-Signature=53336b23fee20b60d264dbdc581507771da702d5097990fb7fd5f97dc30559fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWQ7LXAJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIGKshwQ%2F3djNlfQvElqESivta8pUCB9wRe8AFER9uxInAiEAhZNyrlhmMhed5p4QdfwvtL5o87wa9GwS1XIMd13%2BZZ4q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNeQ2r9gpYWeLHljtCrcA17xi2b8aXQ9VBYPoOeonyyqssMqvDe7vfWVuTxYi5lBPXgUtqwfxKghtEvA%2FWlB2TNAky05cg0iFZRGT%2BLLXfYzOpLPhxRnu9MppETMo46eH1zXm60K%2F%2FPC4ABWGUmCGWGmqBeP6Z9yaF2fao1BVqm%2F22i1BtxXDo0P9a4KwPeKoEpJKnxX0yQO3%2Fx0DqbBPhj8uFdYTrWsvrwU1hwo0gICGFamXvIEvgv1oJhd0bfax6w%2BIhSNprO85kHLEExxbJghtJV3ifkAxKEl98yVAxGQbBnITyp9L7aUvEdu5AFtmmd7z7541rvLrqxARlcE4ugJvejzf2VR48iHDpWwfa1DTxconMy3Yaqw52C%2Fva4TcsEgw6%2FiMbKia11fvraOKN5czWRLRD8e1SWDBuf%2BJ6ldUYVa3L8y4fjN0y5SeE3QtomjpsKMfqHasvS%2FeiJzNzeW1sV1XX%2FwvlGlO800OnwbbmL0NS6OkwwCAp7%2BdAAqetSp9eQFcUMVEgUPzm4rZ73nyE9YSWjPUryxntdTkUDqRemFfbIG1Zwf5X7mpRGxqnBZdkWmpwuu2%2BrobdzpWE97DK6sPloOuXDssb7s3klS1WmyS3ruj%2Fcsf6AIPXpQPEYzdY9QL%2Fz%2BT6ZKMJm6jr0GOqUB8t0NLLJ87c%2FFVGDgZuAjtBCy7hGBKXrIOndAdAVyONhYapMlO7C9OyDTBFyNM7m26w7r58HZ1P2cQkSvHi1Lk45wIvhjEZh59QsYlLBGtn5Qom1jrjYcEa3iiFvY3wmctcy%2BTrF6lPp%2Fe57mKdB%2FxRwTNpmcEJixNmO5Ru7IzUcVpHmt9rZiahJEiW%2BDqepuDQKPdECDZeN6cSIxuPROsNwJZzsC&X-Amz-Signature=71738238235564c2929205aa0f90a5902d6cfe5a13f203453a7d56d84ef801bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFS7IZ3M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQDUpPpjzhyzFK5oRLtTE458CJcU%2FCosJBEIs7yabivqLAIhAOHnLMWRokEWRsxIet7NDw7WA24tEhRuJ4dyDH0xfRKnKv8DCEoQABoMNjM3NDIzMTgzODA1Igz%2BvzgFK%2FZ1u6cfUKUq3AN%2BeOfOFGwNKzYRYX6sHf5fcBNgEvhh463FKYfJHbhhRSMez14Vv%2BamMFOiL6YHWx%2BNmZZE3rVOJV9vITRgkxTxda5tBLERMzBkAZLOOTO24KeJqgdjOjxDaX%2F3hVbEmgEeMStD%2F3J6HA2UdQQMtQLtKSmCW2xHi1jwcdGwXYIhP0FeocfB%2BLmIgtnZFuJOrQu4UpR2oscmh5pkdWOizeCs0bww5UiKgEsJTf6d3TpEY4cqD00ptg8Yu%2FF%2BoLU10bjFDvb%2BtNrkClfFMKx4wumfaMMptUcJrvA2cN7SA52Y3cpjTEZkGUd0hYovY%2B4ky4hgHxR9sEpVUn57JxemiGfb0w0x37pMNb9D3DWHAykoSoharMYpTbRpN9tz16HUTjkRbOdvb%2Br%2F3NRfKcDDeebwE8oioE3W9fd7t3hxbok09o1ktmiyMb44sskHXh4BRsskKAj%2FTdYNl5svas8c47OvPkbbGu8bYfo8WuqKUFvAbSdUBBWKhVEMdI0itU70j%2B76QpM70Du34SsXVUBs40%2B7p4gh3r4GKJtWuWkEGjWqODq%2BLKgfDc5FKF1ZmjSzsfnxAWtRXlXz5P0hOvoNPgktPs9fvQuiBuKwDRuo0TCCuvHn4EGdR8qyg73ONzCuuo69BjqkAa2qvQ36H5XIK2zzu9XwIT6YFZbmu9DqMqBfEgzhHHdoiMt0El1FXZD%2FpZe2Dwh7mcx0xAEWm72tjQRUGCF6AIR13Hi7Nicu05d%2Fo0WLQePTw32Ey%2FJwuhs7eZwPGlw%2FM%2Fyd5W2RkchntTyAWDVB%2BhLTOP1z%2Bw0LAWmAc3WRublCc9GMNSaNUfijR8BTW9GqGqwuZU4Qs4FECEeioSTErBpJStGP&X-Amz-Signature=3190b1613d58fcb064560906938dffafaa80f4100ebfbe885ee073864ca934ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q5XBJXQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIDeyZZ%2BQsFyPTk%2FdBx5F6MDnLMmls0NHQoUgdlXwFpMuAiEA6xanezNUGESnsomFTgJHVa4lpBiM8ZA0cplUDPKgE%2Foq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDMa%2BMQx3WY3ahJpVMircA5tJDL%2BhhLyc7%2FaSgmeHzHCkR8FvhA3OFhhy7xtQZpckQfcurLRL%2F660k4eZ6sQrLB%2Fj%2B%2FFk8%2BvidUlWyI8m4V2nNi3QRGXgU4GSY0KgveIHMZzgcerSl%2FcaJO4FV9qpQ%2FA5MfAazJIfV3ScvQyzV8vBbSKQRrzUicxUaBXukIP1Wq6YGLr%2BVtaHFwNDZyPNiqfRyM0edhO1gUUyBi3O41Yjl7Rs%2BP%2FINGR9pYulBR7d839%2BIV52ekEcPXb4BUbBx8uyIosjDmhgAPF%2F%2FTjFdMhWta58SpCC%2BRh01MmwxeOl8Xf%2BXnSAUSX78HHFODTl4ShXWZBAuwil9x8z285v1xbxEGB74z7AB3tAf4cYMr9atgGKkajsMh792xVxjLDMchK6%2Bk8dlTe%2BDMdEZKabGMqVHXu7bR16Fy8rb8YLn6IFU6SrOF1fWAiLAlm7GgMGYvDnYaIeQuWS7Z1ANXkVZUoqqdvH2PYpyCGliG3fUdYAeOQcbwQQ1ePp6rySgKqsNuMCpsxkxDZ1iXBkPZiJQa%2By3tD9wBiM4T44DXZqEV%2FmyaZLyUttUf5VIM3RAAoYhQ4RqjLLj6QI7xcoeE50kDodRPeJUG3Pt1L6%2B4f5AnwSabLWe3uCn60HDPRcMJK7jr0GOqUB%2B3bKeQGp%2BvK9nIwHo%2FbX8Pmu7FT5sINEfw6NC4SdYJ38f4wpbB3Vzult7UjjdvtgxRN6jO2ZRCjg%2BnCyyoLnJUpE0TNyk8qpv1NMMlEq1xlu7dIB2pQsldcGX4n%2FFY4%2FYIA3d5eiZ87wVOnbKNutR0J5V2gxNRK%2FTTV4lhx7RLImjWimqKMFind%2B%2BTpRsJPC5ynL5C6G8CcSsxAyPcWonqE%2FJ44N&X-Amz-Signature=8aac8bdc84e0363e8a88fb18d613c42196c4b899ff3c664d86b3f30a16124f2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q5XBJXQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIDeyZZ%2BQsFyPTk%2FdBx5F6MDnLMmls0NHQoUgdlXwFpMuAiEA6xanezNUGESnsomFTgJHVa4lpBiM8ZA0cplUDPKgE%2Foq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDMa%2BMQx3WY3ahJpVMircA5tJDL%2BhhLyc7%2FaSgmeHzHCkR8FvhA3OFhhy7xtQZpckQfcurLRL%2F660k4eZ6sQrLB%2Fj%2B%2FFk8%2BvidUlWyI8m4V2nNi3QRGXgU4GSY0KgveIHMZzgcerSl%2FcaJO4FV9qpQ%2FA5MfAazJIfV3ScvQyzV8vBbSKQRrzUicxUaBXukIP1Wq6YGLr%2BVtaHFwNDZyPNiqfRyM0edhO1gUUyBi3O41Yjl7Rs%2BP%2FINGR9pYulBR7d839%2BIV52ekEcPXb4BUbBx8uyIosjDmhgAPF%2F%2FTjFdMhWta58SpCC%2BRh01MmwxeOl8Xf%2BXnSAUSX78HHFODTl4ShXWZBAuwil9x8z285v1xbxEGB74z7AB3tAf4cYMr9atgGKkajsMh792xVxjLDMchK6%2Bk8dlTe%2BDMdEZKabGMqVHXu7bR16Fy8rb8YLn6IFU6SrOF1fWAiLAlm7GgMGYvDnYaIeQuWS7Z1ANXkVZUoqqdvH2PYpyCGliG3fUdYAeOQcbwQQ1ePp6rySgKqsNuMCpsxkxDZ1iXBkPZiJQa%2By3tD9wBiM4T44DXZqEV%2FmyaZLyUttUf5VIM3RAAoYhQ4RqjLLj6QI7xcoeE50kDodRPeJUG3Pt1L6%2B4f5AnwSabLWe3uCn60HDPRcMJK7jr0GOqUB%2B3bKeQGp%2BvK9nIwHo%2FbX8Pmu7FT5sINEfw6NC4SdYJ38f4wpbB3Vzult7UjjdvtgxRN6jO2ZRCjg%2BnCyyoLnJUpE0TNyk8qpv1NMMlEq1xlu7dIB2pQsldcGX4n%2FFY4%2FYIA3d5eiZ87wVOnbKNutR0J5V2gxNRK%2FTTV4lhx7RLImjWimqKMFind%2B%2BTpRsJPC5ynL5C6G8CcSsxAyPcWonqE%2FJ44N&X-Amz-Signature=3d60b8d6bb6307401621ab0c5f598e30a9fb32ffcd47bd35e1dae9b41e84bdd4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
