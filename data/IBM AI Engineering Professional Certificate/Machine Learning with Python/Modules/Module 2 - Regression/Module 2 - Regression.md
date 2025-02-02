

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KKEZP63%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDikJs%2B2sDriecSv5Av3m1Z21lM4y8VJV5R81orvtjzVQIgarm2vklNTAATU7Jq6v%2BLAVNZvazrR4xijAtxNrfip7gqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCCH54yHWOzs5BvGyircAyHT3LHuyXUyhQA8halQfOVNTBqb8ZIioZ81i%2FTPyFhyKRs206LURwpX2cK5NrR5yc%2FErf2R5I94qC6AWSde4%2FJ5WpHO%2FJpgU9JB1eBoOLF5QRKpXVLIk3wA2e4DZSB9A00HZjAnMugK%2F%2FfPBzHZP4NgfkjL%2Fsq31eOdw9SYoHc97ZmLH9uVvxJ7zpOR262Km%2Ftp%2BVL2DSKGWPkR9Yzm1bwV04UzNXmR2jXK4HAuUA4RRCEu65eEjmtxpAFq6aB3ejSu8Pe1pnhQuHqIIarmryFkR%2Bgt32nsenDH9Yi0OiZqLpiWFv3oQcRzP6E6x1whuTwjncxQxEjShw8c%2FdfCjPnQgnTqUVlBnmrve7bZCQp0Ol82KLUbElIGU90opU0koM8RQx9YAUP6C6h0ksrsbaetDod81PXWP7lpGT3p1%2F0o7jrDefi6P1yaxJ9kvFA9QaM%2FdRKFdKIJlNThL0ab169aFXKJamYHbLYMBMyZgDEWD4rsjU56wEKMcNxgL52nTZdmRoFkl8AbUcx1v75fNv4ABGqXc6AiP5ZLof8tToZjjn%2FD4FITESRE%2B5CtSUwPdOT2ffyMb9Z4Ynzks4i%2FZepgtWV9wBNafm2LF%2BWULJxHuzHzv%2BSbBL72l6DoMLPh%2B7wGOqUBNGcRtFfPbdR0PDHIPr57QlbmqTH0U4YjJXwll4OYnTE3sa3r65IK4z60NXlSkRohCB%2BUsPAiLUQ2YW29rOug0X3tghCKuYYbBQgDa0IHwu0uyp7VvJTrMwCA3tp6A78LbGRO49So%2FaaR4rZXMxIIS7Ti2jZaGAEtyRtGQxD3YfDVNk%2BtH9%2B%2FqkocZeKCCdMjZAn9go3EMxWC3b30Kz8weXyWIQOZ&X-Amz-Signature=416d7138a8320e1d1c1659d188c1bc8f37cf18223a3260fc109b2e10a661034c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KKEZP63%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDikJs%2B2sDriecSv5Av3m1Z21lM4y8VJV5R81orvtjzVQIgarm2vklNTAATU7Jq6v%2BLAVNZvazrR4xijAtxNrfip7gqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCCH54yHWOzs5BvGyircAyHT3LHuyXUyhQA8halQfOVNTBqb8ZIioZ81i%2FTPyFhyKRs206LURwpX2cK5NrR5yc%2FErf2R5I94qC6AWSde4%2FJ5WpHO%2FJpgU9JB1eBoOLF5QRKpXVLIk3wA2e4DZSB9A00HZjAnMugK%2F%2FfPBzHZP4NgfkjL%2Fsq31eOdw9SYoHc97ZmLH9uVvxJ7zpOR262Km%2Ftp%2BVL2DSKGWPkR9Yzm1bwV04UzNXmR2jXK4HAuUA4RRCEu65eEjmtxpAFq6aB3ejSu8Pe1pnhQuHqIIarmryFkR%2Bgt32nsenDH9Yi0OiZqLpiWFv3oQcRzP6E6x1whuTwjncxQxEjShw8c%2FdfCjPnQgnTqUVlBnmrve7bZCQp0Ol82KLUbElIGU90opU0koM8RQx9YAUP6C6h0ksrsbaetDod81PXWP7lpGT3p1%2F0o7jrDefi6P1yaxJ9kvFA9QaM%2FdRKFdKIJlNThL0ab169aFXKJamYHbLYMBMyZgDEWD4rsjU56wEKMcNxgL52nTZdmRoFkl8AbUcx1v75fNv4ABGqXc6AiP5ZLof8tToZjjn%2FD4FITESRE%2B5CtSUwPdOT2ffyMb9Z4Ynzks4i%2FZepgtWV9wBNafm2LF%2BWULJxHuzHzv%2BSbBL72l6DoMLPh%2B7wGOqUBNGcRtFfPbdR0PDHIPr57QlbmqTH0U4YjJXwll4OYnTE3sa3r65IK4z60NXlSkRohCB%2BUsPAiLUQ2YW29rOug0X3tghCKuYYbBQgDa0IHwu0uyp7VvJTrMwCA3tp6A78LbGRO49So%2FaaR4rZXMxIIS7Ti2jZaGAEtyRtGQxD3YfDVNk%2BtH9%2B%2FqkocZeKCCdMjZAn9go3EMxWC3b30Kz8weXyWIQOZ&X-Amz-Signature=9b724ae76cab86bdb39aadaeeee62db176531187eccf2698c22172d4b996a9fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KKEZP63%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDikJs%2B2sDriecSv5Av3m1Z21lM4y8VJV5R81orvtjzVQIgarm2vklNTAATU7Jq6v%2BLAVNZvazrR4xijAtxNrfip7gqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCCH54yHWOzs5BvGyircAyHT3LHuyXUyhQA8halQfOVNTBqb8ZIioZ81i%2FTPyFhyKRs206LURwpX2cK5NrR5yc%2FErf2R5I94qC6AWSde4%2FJ5WpHO%2FJpgU9JB1eBoOLF5QRKpXVLIk3wA2e4DZSB9A00HZjAnMugK%2F%2FfPBzHZP4NgfkjL%2Fsq31eOdw9SYoHc97ZmLH9uVvxJ7zpOR262Km%2Ftp%2BVL2DSKGWPkR9Yzm1bwV04UzNXmR2jXK4HAuUA4RRCEu65eEjmtxpAFq6aB3ejSu8Pe1pnhQuHqIIarmryFkR%2Bgt32nsenDH9Yi0OiZqLpiWFv3oQcRzP6E6x1whuTwjncxQxEjShw8c%2FdfCjPnQgnTqUVlBnmrve7bZCQp0Ol82KLUbElIGU90opU0koM8RQx9YAUP6C6h0ksrsbaetDod81PXWP7lpGT3p1%2F0o7jrDefi6P1yaxJ9kvFA9QaM%2FdRKFdKIJlNThL0ab169aFXKJamYHbLYMBMyZgDEWD4rsjU56wEKMcNxgL52nTZdmRoFkl8AbUcx1v75fNv4ABGqXc6AiP5ZLof8tToZjjn%2FD4FITESRE%2B5CtSUwPdOT2ffyMb9Z4Ynzks4i%2FZepgtWV9wBNafm2LF%2BWULJxHuzHzv%2BSbBL72l6DoMLPh%2B7wGOqUBNGcRtFfPbdR0PDHIPr57QlbmqTH0U4YjJXwll4OYnTE3sa3r65IK4z60NXlSkRohCB%2BUsPAiLUQ2YW29rOug0X3tghCKuYYbBQgDa0IHwu0uyp7VvJTrMwCA3tp6A78LbGRO49So%2FaaR4rZXMxIIS7Ti2jZaGAEtyRtGQxD3YfDVNk%2BtH9%2B%2FqkocZeKCCdMjZAn9go3EMxWC3b30Kz8weXyWIQOZ&X-Amz-Signature=3d6fac798509a0454c393de6346b57551bed98b09bb1a3357315db675489b814&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KKEZP63%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDikJs%2B2sDriecSv5Av3m1Z21lM4y8VJV5R81orvtjzVQIgarm2vklNTAATU7Jq6v%2BLAVNZvazrR4xijAtxNrfip7gqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCCH54yHWOzs5BvGyircAyHT3LHuyXUyhQA8halQfOVNTBqb8ZIioZ81i%2FTPyFhyKRs206LURwpX2cK5NrR5yc%2FErf2R5I94qC6AWSde4%2FJ5WpHO%2FJpgU9JB1eBoOLF5QRKpXVLIk3wA2e4DZSB9A00HZjAnMugK%2F%2FfPBzHZP4NgfkjL%2Fsq31eOdw9SYoHc97ZmLH9uVvxJ7zpOR262Km%2Ftp%2BVL2DSKGWPkR9Yzm1bwV04UzNXmR2jXK4HAuUA4RRCEu65eEjmtxpAFq6aB3ejSu8Pe1pnhQuHqIIarmryFkR%2Bgt32nsenDH9Yi0OiZqLpiWFv3oQcRzP6E6x1whuTwjncxQxEjShw8c%2FdfCjPnQgnTqUVlBnmrve7bZCQp0Ol82KLUbElIGU90opU0koM8RQx9YAUP6C6h0ksrsbaetDod81PXWP7lpGT3p1%2F0o7jrDefi6P1yaxJ9kvFA9QaM%2FdRKFdKIJlNThL0ab169aFXKJamYHbLYMBMyZgDEWD4rsjU56wEKMcNxgL52nTZdmRoFkl8AbUcx1v75fNv4ABGqXc6AiP5ZLof8tToZjjn%2FD4FITESRE%2B5CtSUwPdOT2ffyMb9Z4Ynzks4i%2FZepgtWV9wBNafm2LF%2BWULJxHuzHzv%2BSbBL72l6DoMLPh%2B7wGOqUBNGcRtFfPbdR0PDHIPr57QlbmqTH0U4YjJXwll4OYnTE3sa3r65IK4z60NXlSkRohCB%2BUsPAiLUQ2YW29rOug0X3tghCKuYYbBQgDa0IHwu0uyp7VvJTrMwCA3tp6A78LbGRO49So%2FaaR4rZXMxIIS7Ti2jZaGAEtyRtGQxD3YfDVNk%2BtH9%2B%2FqkocZeKCCdMjZAn9go3EMxWC3b30Kz8weXyWIQOZ&X-Amz-Signature=14e7e66f3f8bfab9be9587867aeb394330657313d07b951c781763136e035213&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KKEZP63%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDikJs%2B2sDriecSv5Av3m1Z21lM4y8VJV5R81orvtjzVQIgarm2vklNTAATU7Jq6v%2BLAVNZvazrR4xijAtxNrfip7gqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCCH54yHWOzs5BvGyircAyHT3LHuyXUyhQA8halQfOVNTBqb8ZIioZ81i%2FTPyFhyKRs206LURwpX2cK5NrR5yc%2FErf2R5I94qC6AWSde4%2FJ5WpHO%2FJpgU9JB1eBoOLF5QRKpXVLIk3wA2e4DZSB9A00HZjAnMugK%2F%2FfPBzHZP4NgfkjL%2Fsq31eOdw9SYoHc97ZmLH9uVvxJ7zpOR262Km%2Ftp%2BVL2DSKGWPkR9Yzm1bwV04UzNXmR2jXK4HAuUA4RRCEu65eEjmtxpAFq6aB3ejSu8Pe1pnhQuHqIIarmryFkR%2Bgt32nsenDH9Yi0OiZqLpiWFv3oQcRzP6E6x1whuTwjncxQxEjShw8c%2FdfCjPnQgnTqUVlBnmrve7bZCQp0Ol82KLUbElIGU90opU0koM8RQx9YAUP6C6h0ksrsbaetDod81PXWP7lpGT3p1%2F0o7jrDefi6P1yaxJ9kvFA9QaM%2FdRKFdKIJlNThL0ab169aFXKJamYHbLYMBMyZgDEWD4rsjU56wEKMcNxgL52nTZdmRoFkl8AbUcx1v75fNv4ABGqXc6AiP5ZLof8tToZjjn%2FD4FITESRE%2B5CtSUwPdOT2ffyMb9Z4Ynzks4i%2FZepgtWV9wBNafm2LF%2BWULJxHuzHzv%2BSbBL72l6DoMLPh%2B7wGOqUBNGcRtFfPbdR0PDHIPr57QlbmqTH0U4YjJXwll4OYnTE3sa3r65IK4z60NXlSkRohCB%2BUsPAiLUQ2YW29rOug0X3tghCKuYYbBQgDa0IHwu0uyp7VvJTrMwCA3tp6A78LbGRO49So%2FaaR4rZXMxIIS7Ti2jZaGAEtyRtGQxD3YfDVNk%2BtH9%2B%2FqkocZeKCCdMjZAn9go3EMxWC3b30Kz8weXyWIQOZ&X-Amz-Signature=7040eca9c3a06762191479d95417ae960b51ccc034a3a90cbb7429cb2d827dbd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KKEZP63%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDikJs%2B2sDriecSv5Av3m1Z21lM4y8VJV5R81orvtjzVQIgarm2vklNTAATU7Jq6v%2BLAVNZvazrR4xijAtxNrfip7gqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCCH54yHWOzs5BvGyircAyHT3LHuyXUyhQA8halQfOVNTBqb8ZIioZ81i%2FTPyFhyKRs206LURwpX2cK5NrR5yc%2FErf2R5I94qC6AWSde4%2FJ5WpHO%2FJpgU9JB1eBoOLF5QRKpXVLIk3wA2e4DZSB9A00HZjAnMugK%2F%2FfPBzHZP4NgfkjL%2Fsq31eOdw9SYoHc97ZmLH9uVvxJ7zpOR262Km%2Ftp%2BVL2DSKGWPkR9Yzm1bwV04UzNXmR2jXK4HAuUA4RRCEu65eEjmtxpAFq6aB3ejSu8Pe1pnhQuHqIIarmryFkR%2Bgt32nsenDH9Yi0OiZqLpiWFv3oQcRzP6E6x1whuTwjncxQxEjShw8c%2FdfCjPnQgnTqUVlBnmrve7bZCQp0Ol82KLUbElIGU90opU0koM8RQx9YAUP6C6h0ksrsbaetDod81PXWP7lpGT3p1%2F0o7jrDefi6P1yaxJ9kvFA9QaM%2FdRKFdKIJlNThL0ab169aFXKJamYHbLYMBMyZgDEWD4rsjU56wEKMcNxgL52nTZdmRoFkl8AbUcx1v75fNv4ABGqXc6AiP5ZLof8tToZjjn%2FD4FITESRE%2B5CtSUwPdOT2ffyMb9Z4Ynzks4i%2FZepgtWV9wBNafm2LF%2BWULJxHuzHzv%2BSbBL72l6DoMLPh%2B7wGOqUBNGcRtFfPbdR0PDHIPr57QlbmqTH0U4YjJXwll4OYnTE3sa3r65IK4z60NXlSkRohCB%2BUsPAiLUQ2YW29rOug0X3tghCKuYYbBQgDa0IHwu0uyp7VvJTrMwCA3tp6A78LbGRO49So%2FaaR4rZXMxIIS7Ti2jZaGAEtyRtGQxD3YfDVNk%2BtH9%2B%2FqkocZeKCCdMjZAn9go3EMxWC3b30Kz8weXyWIQOZ&X-Amz-Signature=8b14a7585fd7aa3efd4a2637cd611c525d2d4c8631a02ae7aa94d5fe1e674415&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KKEZP63%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDikJs%2B2sDriecSv5Av3m1Z21lM4y8VJV5R81orvtjzVQIgarm2vklNTAATU7Jq6v%2BLAVNZvazrR4xijAtxNrfip7gqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCCH54yHWOzs5BvGyircAyHT3LHuyXUyhQA8halQfOVNTBqb8ZIioZ81i%2FTPyFhyKRs206LURwpX2cK5NrR5yc%2FErf2R5I94qC6AWSde4%2FJ5WpHO%2FJpgU9JB1eBoOLF5QRKpXVLIk3wA2e4DZSB9A00HZjAnMugK%2F%2FfPBzHZP4NgfkjL%2Fsq31eOdw9SYoHc97ZmLH9uVvxJ7zpOR262Km%2Ftp%2BVL2DSKGWPkR9Yzm1bwV04UzNXmR2jXK4HAuUA4RRCEu65eEjmtxpAFq6aB3ejSu8Pe1pnhQuHqIIarmryFkR%2Bgt32nsenDH9Yi0OiZqLpiWFv3oQcRzP6E6x1whuTwjncxQxEjShw8c%2FdfCjPnQgnTqUVlBnmrve7bZCQp0Ol82KLUbElIGU90opU0koM8RQx9YAUP6C6h0ksrsbaetDod81PXWP7lpGT3p1%2F0o7jrDefi6P1yaxJ9kvFA9QaM%2FdRKFdKIJlNThL0ab169aFXKJamYHbLYMBMyZgDEWD4rsjU56wEKMcNxgL52nTZdmRoFkl8AbUcx1v75fNv4ABGqXc6AiP5ZLof8tToZjjn%2FD4FITESRE%2B5CtSUwPdOT2ffyMb9Z4Ynzks4i%2FZepgtWV9wBNafm2LF%2BWULJxHuzHzv%2BSbBL72l6DoMLPh%2B7wGOqUBNGcRtFfPbdR0PDHIPr57QlbmqTH0U4YjJXwll4OYnTE3sa3r65IK4z60NXlSkRohCB%2BUsPAiLUQ2YW29rOug0X3tghCKuYYbBQgDa0IHwu0uyp7VvJTrMwCA3tp6A78LbGRO49So%2FaaR4rZXMxIIS7Ti2jZaGAEtyRtGQxD3YfDVNk%2BtH9%2B%2FqkocZeKCCdMjZAn9go3EMxWC3b30Kz8weXyWIQOZ&X-Amz-Signature=cc1f829b5d06259169892aefddaa8ac4141ec1190a4966c47922cbf3939bc934&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KKEZP63%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDikJs%2B2sDriecSv5Av3m1Z21lM4y8VJV5R81orvtjzVQIgarm2vklNTAATU7Jq6v%2BLAVNZvazrR4xijAtxNrfip7gqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCCH54yHWOzs5BvGyircAyHT3LHuyXUyhQA8halQfOVNTBqb8ZIioZ81i%2FTPyFhyKRs206LURwpX2cK5NrR5yc%2FErf2R5I94qC6AWSde4%2FJ5WpHO%2FJpgU9JB1eBoOLF5QRKpXVLIk3wA2e4DZSB9A00HZjAnMugK%2F%2FfPBzHZP4NgfkjL%2Fsq31eOdw9SYoHc97ZmLH9uVvxJ7zpOR262Km%2Ftp%2BVL2DSKGWPkR9Yzm1bwV04UzNXmR2jXK4HAuUA4RRCEu65eEjmtxpAFq6aB3ejSu8Pe1pnhQuHqIIarmryFkR%2Bgt32nsenDH9Yi0OiZqLpiWFv3oQcRzP6E6x1whuTwjncxQxEjShw8c%2FdfCjPnQgnTqUVlBnmrve7bZCQp0Ol82KLUbElIGU90opU0koM8RQx9YAUP6C6h0ksrsbaetDod81PXWP7lpGT3p1%2F0o7jrDefi6P1yaxJ9kvFA9QaM%2FdRKFdKIJlNThL0ab169aFXKJamYHbLYMBMyZgDEWD4rsjU56wEKMcNxgL52nTZdmRoFkl8AbUcx1v75fNv4ABGqXc6AiP5ZLof8tToZjjn%2FD4FITESRE%2B5CtSUwPdOT2ffyMb9Z4Ynzks4i%2FZepgtWV9wBNafm2LF%2BWULJxHuzHzv%2BSbBL72l6DoMLPh%2B7wGOqUBNGcRtFfPbdR0PDHIPr57QlbmqTH0U4YjJXwll4OYnTE3sa3r65IK4z60NXlSkRohCB%2BUsPAiLUQ2YW29rOug0X3tghCKuYYbBQgDa0IHwu0uyp7VvJTrMwCA3tp6A78LbGRO49So%2FaaR4rZXMxIIS7Ti2jZaGAEtyRtGQxD3YfDVNk%2BtH9%2B%2FqkocZeKCCdMjZAn9go3EMxWC3b30Kz8weXyWIQOZ&X-Amz-Signature=8433db13b2178ce1e6eb7884f8b9f4c104d13e81b1a7cd69d8b2e0c0c4b222b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQFTYT5Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmH9f42gwzliwqXObVBDh9eMU0R8JA17RC%2FzHNe6jUOwIgf4VUaRaa6whaxYu7nPGIPcNvlZk8sHMOOGpqpmH%2BwH8qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN25QAbx4Ucs%2B9jEmSrcA1HIdpsXLJ%2FN7LgLC6Uus0ZFETguPDZ8b0ZXGbuAFdoeb7FsdzN0TMt8NiHzXT0iV1s3qFP%2BM30nrkMaP8HHwqY%2BDtZTOkVX3JNeU%2FCHI2xQ6i4SjN6H0pkRFeciVl%2BgRsCG3VKila5XPsXAXfjH0gZzQgbQ4im99yNuR%2Bc0a30Ub0%2FRcXQK6jkg3Fdf%2Bz5Of%2BKg0vTPOHLZHvgcaG5TyjeZsavPhSc9Jkf2TbNhJxiX2mn3FYLWyi6QJLi9XtuVSrzmStPCRtcMQ0VL3ov5EmfzIIZNyqEBnoSheVcFU5naHttDH9ZcyLlPYQjfVewfG0G14JN2LJTOM14BzOHmvlp6y5g7ira89k5XkriApHyfbpo%2Bfi0W%2F5JUmQtMSZ1rND7M8cuaQyVeoqS29HGVa1xyyBnM79A2O5shFJFKxlib3OHV5bSHj6KCtpa%2FA9fC%2FYEXbr%2BRvw2p3pPcutyElORTfNUaqOZPCD%2F95F%2FCvhEkk1uCWdO7coUwRX%2Bm1VAYfBQA6pLFtYJF%2BbjcLVoNuVF2F0MQDfV6GjKp%2FeJNYe74wWsqTIyx%2BQpFghH8wWFn5%2FCblZr2SAyOongY3Xro%2FI7e3Iu0t4jzZ066XWmRhDY9hU6amYChwO158cqiMN3h%2B7wGOqUB%2Fb3w6feVAv2byzAHwbCuL9%2BujWEuz3wJzqWzlLC42qQco0f48kmacnCLB7Gp8zShKq%2BZHJKu9ZUyTAJDo8yY0GRmMOzYGdpiOc2wm0UCN6aTz%2FMJv%2FFwjFgaEsFPHSWoIW7gCMkftmKJaXZCJWDuYEfsWo9GjfY16Wj4RBcEPOmUP83v0XMA82qM2OoN1ugyhw0czz1FXzZvrM0vNLzrK%2FhQePn5&X-Amz-Signature=45ca0fd6556390fe409c4a7f5e4b640699a4d56324c35cb88f1328c6972c9068&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVGVVOEC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENIXu%2FGIGNDFjEpv9GoVMtLmc5bMzRdp2u5ZIf95oWWAiBUN3KpPnVMNMcEzjmK6ADnJ2QrDkVs5splEUIisxvKdiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDcwGUxLhgT4aNG6GKtwDjY%2F3E0g%2Fno3NyoKVY%2BLuJsXZVHYAWXWTlCrL97%2Becm0C8Ic5wby4X8pEituxnKSfDr%2F%2F68Sioq3P8BpLD1f%2B22ns8BRdAkb5gSfsr5%2Fp%2F4y7YQ9kLaVN3yqfvHXH52yzSX8jBYN1Q89z%2BjlYhO%2FK%2FV2MSe3rOmxudRcUDb%2FSpkmc68BiQDvHZlTQFR9%2Fuqaf07Xl3vZBTtFx%2BzfO6t2pC3XtW6iXwKlD3k1HGUCDpIdokZ1k77MdZFmr3HueUHjdS2oV8Z7jaAYhyyrsceaw5LrU0jFIVvgttKYGBgT1K5Jbn9EgnpjipGYgbeqVUI29M1ACWWyx7tjKE11HFXZkmY6zybSn8Mi8OEuEHiNKYYoEJ9s3rvIJf4W%2FyWmXV5iQZsMhCK2hxw4BnoQ%2FmQdzLAOZOOMGMCj26ioRT5oyoNbtbY%2FvmwGkp6wnRl8NvwAVGu0sDkg%2BS2hRGYwK7rTS8fLBAEdto1jMvcYxtmkcT2nzNmEiaMAsO5nhviwRd4KYMrS9bsqu7gKL%2F3Y%2BY457pdipiNENsHf07rA%2BopI%2Be5%2BG7fz5zyCrtiGsdCPhRvq%2Bw93Nu%2BJFVHClFJC%2F1rCMKgDYNQR%2FNkuTEbXf0JByM25zqtkjqM3h8UqPA7Iw5eH7vAY6pgHoVgdtW94CrHX5XGnV5ouyIu1nSD9vgi4IcMLrC6bLjmQrF7WPkd83eNA8sXhZ2z3t9lE6lbnAZ9gA9VDvFAyihRu8qELm4jFe0tpulwklKLAzcal%2BCs5FcL9OvObQRosNpnZpSQZfZ61hqhkRjmWUGXOHauMX0YjWaVNryzoSBQnqNKHa0snVanOiULNPU5u7D0bcrXJ%2FTYuxbCD5GzAwWsDZ1Fyk&X-Amz-Signature=f1cba4b75918d2555d8d01800e4196f5cd8d6f8ed1dad3230f6c46f03625ab0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IVMKHQD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxlqKf%2FXt5O0sYTAD%2Fp7cylhbtVnuOfgRGnfmgzcTE3AIgW1kYJwt3sYdgVc03PeHWVYHQ2Nfg6Kgm%2Bu35LNyaQCsqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2FpEjIqJEHXRoemSSrcA15VB6n8lW9lCLv74ycKRwYFpAhWmmxtdlvlW1CrjljNA8447cdiyVUcGNXAbjwb9tyRYF%2FV2hxRkykJb%2BJJmEfFABwBcf6d1BpeLxQ2qpvF3Igu2LkyaFPo9xFYkPnXvFVWOkPHt2PbcrzedIXeV%2BqUj9TmNGMb920XiFZxJxBPkAdsb2oUN8fP4aS7E%2F1N0bnwRn2bxK4zPpYP9OelccSGB2DL9WM2y%2B8zoGqGCaq%2BVHimK1ZPv9FS30%2FmeurKyPl9D6gLdxiOCvg%2FPcSp57EVA%2B9bUCHntxaA6GEelKsNnRnWjyNUC5N8nuHiPmDf72cx2lVagtgnqRaBQPyP1IBt5vvTlDJrZ%2BPWpsBUIXHgG347g2chI7b188ClsV6UEDm5E%2BjlHjJbvnqwICes%2Bl4ZtzMPEfSghqdv%2F2Y3dSme0conEh%2BMzcwljDVCZAJM%2F%2FeS7EDjJvzHM6qVa2bx9jIwJH8xiU0ZlM4QQhJ8VoiOrFdblfwzlPpR7VLR9t2%2F5ikROE5ED4PzZArbwgImnsc7Ih3Dn2WDAXpQvUhSKDdvWjymxtBZ%2BpWPp%2BfCjteEtoLH88BdK9EIXXmSBVwVCAnQeJzU3HvwVfAsTSL%2B044y1jPASV5WgUXQKW4wMKrh%2B7wGOqUBbXEdffQDmrLZk9fu%2FVhmHREGdJVggW2r4kJxXcspXZ9Jn2MTFZUwAeyQDpHedPsMoYKgH949kQc3PlfsF6XgfQRTllsNJty6KTlBwHjZQInWXMUN9X9DI10fFljZ3lG5N7U7y5KhNAB73uIwnhQJrz5wD1McJVJjTmRp5KWB7ic8LzE6kKzmUZW%2B4MbI8S6T5aaeDK2FACzHxPyA1Irj7SeuHf5C&X-Amz-Signature=c182bb76a661bc486c6e1118f3740cb64028f2586b2372c5c44dd9d38b182f25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IVMKHQD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxlqKf%2FXt5O0sYTAD%2Fp7cylhbtVnuOfgRGnfmgzcTE3AIgW1kYJwt3sYdgVc03PeHWVYHQ2Nfg6Kgm%2Bu35LNyaQCsqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2FpEjIqJEHXRoemSSrcA15VB6n8lW9lCLv74ycKRwYFpAhWmmxtdlvlW1CrjljNA8447cdiyVUcGNXAbjwb9tyRYF%2FV2hxRkykJb%2BJJmEfFABwBcf6d1BpeLxQ2qpvF3Igu2LkyaFPo9xFYkPnXvFVWOkPHt2PbcrzedIXeV%2BqUj9TmNGMb920XiFZxJxBPkAdsb2oUN8fP4aS7E%2F1N0bnwRn2bxK4zPpYP9OelccSGB2DL9WM2y%2B8zoGqGCaq%2BVHimK1ZPv9FS30%2FmeurKyPl9D6gLdxiOCvg%2FPcSp57EVA%2B9bUCHntxaA6GEelKsNnRnWjyNUC5N8nuHiPmDf72cx2lVagtgnqRaBQPyP1IBt5vvTlDJrZ%2BPWpsBUIXHgG347g2chI7b188ClsV6UEDm5E%2BjlHjJbvnqwICes%2Bl4ZtzMPEfSghqdv%2F2Y3dSme0conEh%2BMzcwljDVCZAJM%2F%2FeS7EDjJvzHM6qVa2bx9jIwJH8xiU0ZlM4QQhJ8VoiOrFdblfwzlPpR7VLR9t2%2F5ikROE5ED4PzZArbwgImnsc7Ih3Dn2WDAXpQvUhSKDdvWjymxtBZ%2BpWPp%2BfCjteEtoLH88BdK9EIXXmSBVwVCAnQeJzU3HvwVfAsTSL%2B044y1jPASV5WgUXQKW4wMKrh%2B7wGOqUBbXEdffQDmrLZk9fu%2FVhmHREGdJVggW2r4kJxXcspXZ9Jn2MTFZUwAeyQDpHedPsMoYKgH949kQc3PlfsF6XgfQRTllsNJty6KTlBwHjZQInWXMUN9X9DI10fFljZ3lG5N7U7y5KhNAB73uIwnhQJrz5wD1McJVJjTmRp5KWB7ic8LzE6kKzmUZW%2B4MbI8S6T5aaeDK2FACzHxPyA1Irj7SeuHf5C&X-Amz-Signature=7d54f618f55a2e4329442a85a800d2d514328ed9245036c17ecc5443e95b902e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
