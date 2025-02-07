

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=697b3b6f341b6d614d152f2ad4a694659abfd71da9880ca5cf781050c09fd85f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=6c37423231f0cc9aa859c4831302747e3a662d010c97999873014ef393e81d65&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=5520d31c3846e429e5abcd5457a78a76d5da615d9579d3d76464dee7d8d58196&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=6f8f92a003f1e66f9f003fc938aa87aca2af40382f90a6ba307b36b3bdf3feab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=a276f941c3adda8183129937f644ad963ad3fb3ed60ff33f2f6f7f089a6982d7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=cfd1fc9e271c1321fea1165055f2cb2f3238c46f2f53c1e74b26b80bf793a2c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=2023178221ab943869008c2b562e731a1f9752ea4dc69adec7a091ae67d2b8eb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=88137befabec1e063e4e0cd4a04bf30cf264187280af4badeeb957f33580f713&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJO3KUNJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIGlwno%2FHdY9%2BIjGrdS%2FoK%2BeIglG0Oi5AfMkL%2FeJ0g9nIAiBu5RLGpMJHNJzYL4lRz8ilrLIFXEOlSofg7JTX9ZYGlir%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMOC3KxVNJyo2SY%2BW8KtwDGM3VrOqcOpZAmflzFVSQgYbnZcFH5zJbmy%2Ftg1FncOmbDE1BD%2BSYvpeMVNfOZjl1d05h6Km%2BBNejZTjkvgT7ZKVWNpi5RzOweqyGIe1P%2B6xbJjpCvwa9xMTXvnfBfAtyWZJE%2FJuvOKD%2B3IxFjThJAdkrtL5CSOCWw9HmiwraLMM3As7tCQQzedATpoK7wZ7JWjSKM%2B37KktnzLJ2X8JZUyIjrOJdXxyTeWB89AL2T7TiJsrI0DtIPLrlwXCSwn5uV5PZB28PbWrZWp3naiYeKkmpMV86mPwVW0OfF1HK3ptUbVYgMLf8d%2FjlZQshr71dg0l0cypn8OvY%2Bh2QekCJuQjYZcUIBFr5QWdTq5vDS6hFoZoDV0fdyY4cOsnLtj3NCjIwIJA4Ngb6qwn07ztOjd3jmZzn2PfbKhSXR1YB4nmSrm3ucSNIjUVwWhHIHYQeMIpYZmgc%2BhF3aZjXQjl0mhMAseyNg8f6ILN19%2FYSoGoz9lCb2UKUaMPzEvo3GQj8P72pEzrpWUtAHtiZw%2FC%2BzsyTNr2R%2BJvZF7JeRGEBLeJtj2gil1xrCUSbmQ2cExBYE3UvU8n%2FyxIBsXcaVP%2FL4rty2nccsLqb6t%2BflXFoSH6wtCLrr9UfAQA99yUw7JmVvQY6pgGEyc2WZj1xiXbcxh8zn6CP%2BUF8qnepEjMZ05RY4pX7DwquG5q6jKLdmSxxwBmvJyw19TlbS04n8m%2Bfm3n4wXZCxOIkSi%2FZXr%2B4jpsDO%2B%2BPRJl0OtmMSUyZ8jBbcYMr%2FrYxyY3QMMwTCiAZotYjkolqWaF3OZPBhY%2FubWxqLqrdZV3cdNCl2i8714jlUT%2Fckt9WgeBreOF3c6DA8ugD9StuqIHXngrM&X-Amz-Signature=4c62c210653d124287291c01f2d8a39bf350f8d50e7e3d340a247602d499d64c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QJZ4W44%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIFbt62DytBEyBzY2JZEfxF2Ebp9Ne%2FpSCMjmlXq6%2BAdHAiB9pwT86cvE5KYJcj0VrtD%2FUwMyEtxrIUGjfdCwDZY%2Fcir%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMoSIJQPduZ5MED6rzKtwDle%2F78GpwIfagf%2BhYs7stCU66qFHGZrVtkCifcdgo2dBvuUNsIiRPZ7RUvzpK2cfRsu2WpP2i75OPb1dzHLt3e5aBUDpkt%2BZi7B42jmBYB0xA0hiC0xy9Zkjuwbfd1MCYeTq4nqTVjM7L5kuTb2SnHY85VR2fcOvruxEk5mozJbIVm5sxzauTX63WMUApiVAHHmLMaaMb796CJH6uPYnXUER43o%2FxUEQsyn6IkWhcqYkz75NjAeGeofKmAZ3DScsW06lHwQFSJTzdZoApXr8YTp7bP4KJrzCikFLC9juOUbVFu4MsLMe8kNqWDPGaddM6J4oSpzSdch2sfWz7rej626KyNRHBH6jYXN1N6cmq9sdzS6%2BdmJ%2BDJmx3FYybuW1ssGLhX1cHUGVwrmoWZfItx8BdG5dW6%2FfBN%2F6ugmsjtSOGU7EkbSm2COc4ZPLXQOmbqSaCqSLfX1CfrOx3uYKTKjViwdpISihRVRKNiOLbeHM9IEAVdi3epUFpFOOiK%2FXKHzFvGEfIDOvh2XC5p2D3gBeeyIWJU%2FOUkciY%2FqweXVpnOFBF49ksdie1a3h6QHLPJ1fC426NUeGHCQnafN%2FHL%2BLlGY6VXZK2tcyq39ltxt3UPjOpeliMoLsj60Yw8pmVvQY6pgHl8Pjsao0I2n04MdnVpfYlKiR8Yquf%2BP%2FCVo3tI8yfFPc8FVFpKteQumm41WPcxKQOuEHZhfDYdnmU5Prs2au5%2B9AATW4M5aLhk4imyNnBZOuyDzH8DBFED14RNdDB2nbRS7Y35CpyQ5ny4VD1m5M3BFv3bSWOhUdSuS4aBkDoG8zrHh4uDUa0n4dQ08VXJUFUVjkn4fcc0MpIoLBcxtkNlTr7ZWI5&X-Amz-Signature=8f31de0de50de6c493139322b37de073ea653aae495879b338373beef89cbdb8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V46OIYFC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIFIOLgQvhxwy26I0mwkkEZkodSlQR8yNYP8GzgDa84WfAiBXfVhyA28bmnYzFj6PN2g2%2FzzNsmlU25hDN%2FfrC7L1RSr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMGT05lhKm4zrdUxr5KtwDrdRyBnjF%2F0fCD4wRZpHInofMT%2BpQqth20kKMxePwN1LUxUmeOxUxzzZ%2BSFuadkKp4enmkN51dsi5azncTAT0t12otlCmel2spSlw4vp2XLZlDLYT84crQbcn1%2Fq3Bv1klAxqutM270NaKPCoPEGTCJ%2BdGJABUxTIBtNwrzflzrg9zcrxvILZ3seODtijcZ8nXubunNMqZqYwxND5zqqB0WJy9XYszeFDQpkDMZohFDveLGeE1Df%2B3kI1YQFQWY1baNexZivj1Qr0Z0h2H9JwYj0kPBHXN7wy3Nai7qOUGH1R8cOda%2By%2Ffzn57KMt%2FWGJkEAbH2Xenca%2BMh4W32VWm8MlEIooVPTOc8ewnDfu1i1jHEc9qo0l8oKfHj8i6L5O29vMAOR4XR5w%2FrJxA4BqSSKor%2Ffh2n46ZKNNDecAwlKo4rA9Irwm1gYPhWly4ZuNvRbITywMoS5BO43zhkSZhbbdk45Nsum%2FB%2B3H5VzuMtpOO5zJ%2F0Xs5DZpYMZ494vu68CXaz0Mn3DuaHPAev%2FSvK7oOQ%2BEh1BXzD5ECqajUwx%2BAftZUYyHz8ahBAVLnDvLJAzfYWPDp6ypY5NowvkTd0pBht%2BsEYav5YaY8GPlIrjZpxLNrR4X%2Byufmewwx5qVvQY6pgFpPfi5gCk4HO%2FSJ45eq2taC63DSfuzTJufsZeNGoSjvX3huu7w8d9zbfvPWDUgQrRwPv59S56pcjuBXAcjuuRl4gR9H%2FLVmQAQF5r42QzwluuIln3YFdI32SS%2FfGlardv5yPVhsM3iMca8X8%2F%2BsgJWIyjH3ZW7yclfdk%2FzUSbX7lPwBq4RrG6wo%2FWpD1E3VoaVV28LA6AwG46YvEWsuc5YKBBq%2FgJ9&X-Amz-Signature=00d4e30108c7d4b984499b4e28170c1ae38936b63c8d26c425af3f1c20d0d665&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V46OIYFC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIFIOLgQvhxwy26I0mwkkEZkodSlQR8yNYP8GzgDa84WfAiBXfVhyA28bmnYzFj6PN2g2%2FzzNsmlU25hDN%2FfrC7L1RSr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMGT05lhKm4zrdUxr5KtwDrdRyBnjF%2F0fCD4wRZpHInofMT%2BpQqth20kKMxePwN1LUxUmeOxUxzzZ%2BSFuadkKp4enmkN51dsi5azncTAT0t12otlCmel2spSlw4vp2XLZlDLYT84crQbcn1%2Fq3Bv1klAxqutM270NaKPCoPEGTCJ%2BdGJABUxTIBtNwrzflzrg9zcrxvILZ3seODtijcZ8nXubunNMqZqYwxND5zqqB0WJy9XYszeFDQpkDMZohFDveLGeE1Df%2B3kI1YQFQWY1baNexZivj1Qr0Z0h2H9JwYj0kPBHXN7wy3Nai7qOUGH1R8cOda%2By%2Ffzn57KMt%2FWGJkEAbH2Xenca%2BMh4W32VWm8MlEIooVPTOc8ewnDfu1i1jHEc9qo0l8oKfHj8i6L5O29vMAOR4XR5w%2FrJxA4BqSSKor%2Ffh2n46ZKNNDecAwlKo4rA9Irwm1gYPhWly4ZuNvRbITywMoS5BO43zhkSZhbbdk45Nsum%2FB%2B3H5VzuMtpOO5zJ%2F0Xs5DZpYMZ494vu68CXaz0Mn3DuaHPAev%2FSvK7oOQ%2BEh1BXzD5ECqajUwx%2BAftZUYyHz8ahBAVLnDvLJAzfYWPDp6ypY5NowvkTd0pBht%2BsEYav5YaY8GPlIrjZpxLNrR4X%2Byufmewwx5qVvQY6pgFpPfi5gCk4HO%2FSJ45eq2taC63DSfuzTJufsZeNGoSjvX3huu7w8d9zbfvPWDUgQrRwPv59S56pcjuBXAcjuuRl4gR9H%2FLVmQAQF5r42QzwluuIln3YFdI32SS%2FfGlardv5yPVhsM3iMca8X8%2F%2BsgJWIyjH3ZW7yclfdk%2FzUSbX7lPwBq4RrG6wo%2FWpD1E3VoaVV28LA6AwG46YvEWsuc5YKBBq%2FgJ9&X-Amz-Signature=81d56be40f0fc48d415aa29727be5200d2966186be4957ab1132bb27adbf4816&X-Amz-SignedHeaders=host&x-id=GetObject)
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
