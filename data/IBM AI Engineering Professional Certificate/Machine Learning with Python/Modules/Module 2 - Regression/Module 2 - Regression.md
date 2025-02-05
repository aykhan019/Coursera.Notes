

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UGYH2DB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIHoUIMZ%2F2XK9pxtAVYCFP2yGUWBJNS9RnYo1V3nsyMQYAiEAziCJ6cVqdVHQssv4jUDMbVXtp86Y6IVg3T0VuFPNg4Qq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFdZAOodaLjfmNiPxCrcAwTaTLrJWY5qyxg6yR4Keop6uULYrtaEkwwyQxSFwIl30gc%2FP0Yw50E118DO%2BAq5higQ9SRRz6z66VDhX6urOFo5gPOrq38XyM5Lhg%2BgRPuL%2Fl8ShST8Y3F3uB%2Bfli4aMkvX9m7kz0JqZWh2eKLRBwLuOaCwPBrMhwbnvH2zRnITxMBlR9mx8guEKMKkCMDbN5%2BESqUE6EU25zw3UaedtsaKaTPN9zjVHqc2s%2BT3FsyT3tnN2soiyhW9yO2uvxNxQSULAFyKnfTpEpTUUTPRQXfWH0YJXto%2FRErFnN%2F3yMOgffiqvG5VMuWS5OmgekEn%2B2ACfWBctbMJj0PPhTEk%2FBenzPNmaUz8WoBdcU8o%2BcJFzcuAv42t%2B1rnQswiN672Up95FHM3OW46vnQz%2BHLo%2F5uNWpVybOAvTdiw3B5%2B8bxZ8bsy9O1DbFbkvZBpNlB%2Bmwdgq16nERP67Ful40BAe3hmILmuNktrF4hGSF21Q1Dn3yyYUHBofeZpOqRcAYGIA5zBoBxOu0onhRPfkWHIxH%2BJgF0drOGhrKylKR1b3iTyrpke8B7gmXNu%2Bv5kneAuZ8hWoisDL%2B3xb0jFU5B3ZIGuZOIhQs6b87gmYBu53oij8dJXpG1CO4hxa7%2B2MJe1jL0GOqUBndmPn5rJclwIoEn%2FSz8QRvepXjq82THre3yWK98N5LrFFpIGVVn1GVFBkYafsk2PqsUWxJ6d27yJbzqblf8IgPV75frdGnPbOEIiEplcI1G14CNstWeaeUtIWtPfZ2ZG5GvynrRCwXh2I8s3cZBK4yvMFdPLk6g1AkRsDEGW7GDxPvwNJF%2BONtLTbdDAF%2FSLJGEXKH8JUvRkJ%2FzyxlRDCHZ%2FD8Rx&X-Amz-Signature=ae2e80f61fee7cd8d9596e078afa0df0212bcb3f27eff213ee2ecc69d8f75de9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UGYH2DB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIHoUIMZ%2F2XK9pxtAVYCFP2yGUWBJNS9RnYo1V3nsyMQYAiEAziCJ6cVqdVHQssv4jUDMbVXtp86Y6IVg3T0VuFPNg4Qq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFdZAOodaLjfmNiPxCrcAwTaTLrJWY5qyxg6yR4Keop6uULYrtaEkwwyQxSFwIl30gc%2FP0Yw50E118DO%2BAq5higQ9SRRz6z66VDhX6urOFo5gPOrq38XyM5Lhg%2BgRPuL%2Fl8ShST8Y3F3uB%2Bfli4aMkvX9m7kz0JqZWh2eKLRBwLuOaCwPBrMhwbnvH2zRnITxMBlR9mx8guEKMKkCMDbN5%2BESqUE6EU25zw3UaedtsaKaTPN9zjVHqc2s%2BT3FsyT3tnN2soiyhW9yO2uvxNxQSULAFyKnfTpEpTUUTPRQXfWH0YJXto%2FRErFnN%2F3yMOgffiqvG5VMuWS5OmgekEn%2B2ACfWBctbMJj0PPhTEk%2FBenzPNmaUz8WoBdcU8o%2BcJFzcuAv42t%2B1rnQswiN672Up95FHM3OW46vnQz%2BHLo%2F5uNWpVybOAvTdiw3B5%2B8bxZ8bsy9O1DbFbkvZBpNlB%2Bmwdgq16nERP67Ful40BAe3hmILmuNktrF4hGSF21Q1Dn3yyYUHBofeZpOqRcAYGIA5zBoBxOu0onhRPfkWHIxH%2BJgF0drOGhrKylKR1b3iTyrpke8B7gmXNu%2Bv5kneAuZ8hWoisDL%2B3xb0jFU5B3ZIGuZOIhQs6b87gmYBu53oij8dJXpG1CO4hxa7%2B2MJe1jL0GOqUBndmPn5rJclwIoEn%2FSz8QRvepXjq82THre3yWK98N5LrFFpIGVVn1GVFBkYafsk2PqsUWxJ6d27yJbzqblf8IgPV75frdGnPbOEIiEplcI1G14CNstWeaeUtIWtPfZ2ZG5GvynrRCwXh2I8s3cZBK4yvMFdPLk6g1AkRsDEGW7GDxPvwNJF%2BONtLTbdDAF%2FSLJGEXKH8JUvRkJ%2FzyxlRDCHZ%2FD8Rx&X-Amz-Signature=46a3b2d4d671e5db5f1c5e2b2197d3f717591765d94ea9a0a65c0d97c1c66419&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UGYH2DB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIHoUIMZ%2F2XK9pxtAVYCFP2yGUWBJNS9RnYo1V3nsyMQYAiEAziCJ6cVqdVHQssv4jUDMbVXtp86Y6IVg3T0VuFPNg4Qq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFdZAOodaLjfmNiPxCrcAwTaTLrJWY5qyxg6yR4Keop6uULYrtaEkwwyQxSFwIl30gc%2FP0Yw50E118DO%2BAq5higQ9SRRz6z66VDhX6urOFo5gPOrq38XyM5Lhg%2BgRPuL%2Fl8ShST8Y3F3uB%2Bfli4aMkvX9m7kz0JqZWh2eKLRBwLuOaCwPBrMhwbnvH2zRnITxMBlR9mx8guEKMKkCMDbN5%2BESqUE6EU25zw3UaedtsaKaTPN9zjVHqc2s%2BT3FsyT3tnN2soiyhW9yO2uvxNxQSULAFyKnfTpEpTUUTPRQXfWH0YJXto%2FRErFnN%2F3yMOgffiqvG5VMuWS5OmgekEn%2B2ACfWBctbMJj0PPhTEk%2FBenzPNmaUz8WoBdcU8o%2BcJFzcuAv42t%2B1rnQswiN672Up95FHM3OW46vnQz%2BHLo%2F5uNWpVybOAvTdiw3B5%2B8bxZ8bsy9O1DbFbkvZBpNlB%2Bmwdgq16nERP67Ful40BAe3hmILmuNktrF4hGSF21Q1Dn3yyYUHBofeZpOqRcAYGIA5zBoBxOu0onhRPfkWHIxH%2BJgF0drOGhrKylKR1b3iTyrpke8B7gmXNu%2Bv5kneAuZ8hWoisDL%2B3xb0jFU5B3ZIGuZOIhQs6b87gmYBu53oij8dJXpG1CO4hxa7%2B2MJe1jL0GOqUBndmPn5rJclwIoEn%2FSz8QRvepXjq82THre3yWK98N5LrFFpIGVVn1GVFBkYafsk2PqsUWxJ6d27yJbzqblf8IgPV75frdGnPbOEIiEplcI1G14CNstWeaeUtIWtPfZ2ZG5GvynrRCwXh2I8s3cZBK4yvMFdPLk6g1AkRsDEGW7GDxPvwNJF%2BONtLTbdDAF%2FSLJGEXKH8JUvRkJ%2FzyxlRDCHZ%2FD8Rx&X-Amz-Signature=c655afada99c28b5e25018c80b7e3f21b87591b43036fc11523e9096d2a5845c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UGYH2DB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIHoUIMZ%2F2XK9pxtAVYCFP2yGUWBJNS9RnYo1V3nsyMQYAiEAziCJ6cVqdVHQssv4jUDMbVXtp86Y6IVg3T0VuFPNg4Qq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFdZAOodaLjfmNiPxCrcAwTaTLrJWY5qyxg6yR4Keop6uULYrtaEkwwyQxSFwIl30gc%2FP0Yw50E118DO%2BAq5higQ9SRRz6z66VDhX6urOFo5gPOrq38XyM5Lhg%2BgRPuL%2Fl8ShST8Y3F3uB%2Bfli4aMkvX9m7kz0JqZWh2eKLRBwLuOaCwPBrMhwbnvH2zRnITxMBlR9mx8guEKMKkCMDbN5%2BESqUE6EU25zw3UaedtsaKaTPN9zjVHqc2s%2BT3FsyT3tnN2soiyhW9yO2uvxNxQSULAFyKnfTpEpTUUTPRQXfWH0YJXto%2FRErFnN%2F3yMOgffiqvG5VMuWS5OmgekEn%2B2ACfWBctbMJj0PPhTEk%2FBenzPNmaUz8WoBdcU8o%2BcJFzcuAv42t%2B1rnQswiN672Up95FHM3OW46vnQz%2BHLo%2F5uNWpVybOAvTdiw3B5%2B8bxZ8bsy9O1DbFbkvZBpNlB%2Bmwdgq16nERP67Ful40BAe3hmILmuNktrF4hGSF21Q1Dn3yyYUHBofeZpOqRcAYGIA5zBoBxOu0onhRPfkWHIxH%2BJgF0drOGhrKylKR1b3iTyrpke8B7gmXNu%2Bv5kneAuZ8hWoisDL%2B3xb0jFU5B3ZIGuZOIhQs6b87gmYBu53oij8dJXpG1CO4hxa7%2B2MJe1jL0GOqUBndmPn5rJclwIoEn%2FSz8QRvepXjq82THre3yWK98N5LrFFpIGVVn1GVFBkYafsk2PqsUWxJ6d27yJbzqblf8IgPV75frdGnPbOEIiEplcI1G14CNstWeaeUtIWtPfZ2ZG5GvynrRCwXh2I8s3cZBK4yvMFdPLk6g1AkRsDEGW7GDxPvwNJF%2BONtLTbdDAF%2FSLJGEXKH8JUvRkJ%2FzyxlRDCHZ%2FD8Rx&X-Amz-Signature=c32e1986a452b63a7a03cbc250721a6d0b5e8b1584c27249cb5fb5e098830fd2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UGYH2DB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIHoUIMZ%2F2XK9pxtAVYCFP2yGUWBJNS9RnYo1V3nsyMQYAiEAziCJ6cVqdVHQssv4jUDMbVXtp86Y6IVg3T0VuFPNg4Qq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFdZAOodaLjfmNiPxCrcAwTaTLrJWY5qyxg6yR4Keop6uULYrtaEkwwyQxSFwIl30gc%2FP0Yw50E118DO%2BAq5higQ9SRRz6z66VDhX6urOFo5gPOrq38XyM5Lhg%2BgRPuL%2Fl8ShST8Y3F3uB%2Bfli4aMkvX9m7kz0JqZWh2eKLRBwLuOaCwPBrMhwbnvH2zRnITxMBlR9mx8guEKMKkCMDbN5%2BESqUE6EU25zw3UaedtsaKaTPN9zjVHqc2s%2BT3FsyT3tnN2soiyhW9yO2uvxNxQSULAFyKnfTpEpTUUTPRQXfWH0YJXto%2FRErFnN%2F3yMOgffiqvG5VMuWS5OmgekEn%2B2ACfWBctbMJj0PPhTEk%2FBenzPNmaUz8WoBdcU8o%2BcJFzcuAv42t%2B1rnQswiN672Up95FHM3OW46vnQz%2BHLo%2F5uNWpVybOAvTdiw3B5%2B8bxZ8bsy9O1DbFbkvZBpNlB%2Bmwdgq16nERP67Ful40BAe3hmILmuNktrF4hGSF21Q1Dn3yyYUHBofeZpOqRcAYGIA5zBoBxOu0onhRPfkWHIxH%2BJgF0drOGhrKylKR1b3iTyrpke8B7gmXNu%2Bv5kneAuZ8hWoisDL%2B3xb0jFU5B3ZIGuZOIhQs6b87gmYBu53oij8dJXpG1CO4hxa7%2B2MJe1jL0GOqUBndmPn5rJclwIoEn%2FSz8QRvepXjq82THre3yWK98N5LrFFpIGVVn1GVFBkYafsk2PqsUWxJ6d27yJbzqblf8IgPV75frdGnPbOEIiEplcI1G14CNstWeaeUtIWtPfZ2ZG5GvynrRCwXh2I8s3cZBK4yvMFdPLk6g1AkRsDEGW7GDxPvwNJF%2BONtLTbdDAF%2FSLJGEXKH8JUvRkJ%2FzyxlRDCHZ%2FD8Rx&X-Amz-Signature=b7932e438c3080f137cfef161cb022ca0e282f6417b9d812ae8846857cd89f7e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UGYH2DB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIHoUIMZ%2F2XK9pxtAVYCFP2yGUWBJNS9RnYo1V3nsyMQYAiEAziCJ6cVqdVHQssv4jUDMbVXtp86Y6IVg3T0VuFPNg4Qq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFdZAOodaLjfmNiPxCrcAwTaTLrJWY5qyxg6yR4Keop6uULYrtaEkwwyQxSFwIl30gc%2FP0Yw50E118DO%2BAq5higQ9SRRz6z66VDhX6urOFo5gPOrq38XyM5Lhg%2BgRPuL%2Fl8ShST8Y3F3uB%2Bfli4aMkvX9m7kz0JqZWh2eKLRBwLuOaCwPBrMhwbnvH2zRnITxMBlR9mx8guEKMKkCMDbN5%2BESqUE6EU25zw3UaedtsaKaTPN9zjVHqc2s%2BT3FsyT3tnN2soiyhW9yO2uvxNxQSULAFyKnfTpEpTUUTPRQXfWH0YJXto%2FRErFnN%2F3yMOgffiqvG5VMuWS5OmgekEn%2B2ACfWBctbMJj0PPhTEk%2FBenzPNmaUz8WoBdcU8o%2BcJFzcuAv42t%2B1rnQswiN672Up95FHM3OW46vnQz%2BHLo%2F5uNWpVybOAvTdiw3B5%2B8bxZ8bsy9O1DbFbkvZBpNlB%2Bmwdgq16nERP67Ful40BAe3hmILmuNktrF4hGSF21Q1Dn3yyYUHBofeZpOqRcAYGIA5zBoBxOu0onhRPfkWHIxH%2BJgF0drOGhrKylKR1b3iTyrpke8B7gmXNu%2Bv5kneAuZ8hWoisDL%2B3xb0jFU5B3ZIGuZOIhQs6b87gmYBu53oij8dJXpG1CO4hxa7%2B2MJe1jL0GOqUBndmPn5rJclwIoEn%2FSz8QRvepXjq82THre3yWK98N5LrFFpIGVVn1GVFBkYafsk2PqsUWxJ6d27yJbzqblf8IgPV75frdGnPbOEIiEplcI1G14CNstWeaeUtIWtPfZ2ZG5GvynrRCwXh2I8s3cZBK4yvMFdPLk6g1AkRsDEGW7GDxPvwNJF%2BONtLTbdDAF%2FSLJGEXKH8JUvRkJ%2FzyxlRDCHZ%2FD8Rx&X-Amz-Signature=b96d10e5ce1e19411b3a2d7d07d39d0fe29d26e079c089ad94e8af52614146be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UGYH2DB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIHoUIMZ%2F2XK9pxtAVYCFP2yGUWBJNS9RnYo1V3nsyMQYAiEAziCJ6cVqdVHQssv4jUDMbVXtp86Y6IVg3T0VuFPNg4Qq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFdZAOodaLjfmNiPxCrcAwTaTLrJWY5qyxg6yR4Keop6uULYrtaEkwwyQxSFwIl30gc%2FP0Yw50E118DO%2BAq5higQ9SRRz6z66VDhX6urOFo5gPOrq38XyM5Lhg%2BgRPuL%2Fl8ShST8Y3F3uB%2Bfli4aMkvX9m7kz0JqZWh2eKLRBwLuOaCwPBrMhwbnvH2zRnITxMBlR9mx8guEKMKkCMDbN5%2BESqUE6EU25zw3UaedtsaKaTPN9zjVHqc2s%2BT3FsyT3tnN2soiyhW9yO2uvxNxQSULAFyKnfTpEpTUUTPRQXfWH0YJXto%2FRErFnN%2F3yMOgffiqvG5VMuWS5OmgekEn%2B2ACfWBctbMJj0PPhTEk%2FBenzPNmaUz8WoBdcU8o%2BcJFzcuAv42t%2B1rnQswiN672Up95FHM3OW46vnQz%2BHLo%2F5uNWpVybOAvTdiw3B5%2B8bxZ8bsy9O1DbFbkvZBpNlB%2Bmwdgq16nERP67Ful40BAe3hmILmuNktrF4hGSF21Q1Dn3yyYUHBofeZpOqRcAYGIA5zBoBxOu0onhRPfkWHIxH%2BJgF0drOGhrKylKR1b3iTyrpke8B7gmXNu%2Bv5kneAuZ8hWoisDL%2B3xb0jFU5B3ZIGuZOIhQs6b87gmYBu53oij8dJXpG1CO4hxa7%2B2MJe1jL0GOqUBndmPn5rJclwIoEn%2FSz8QRvepXjq82THre3yWK98N5LrFFpIGVVn1GVFBkYafsk2PqsUWxJ6d27yJbzqblf8IgPV75frdGnPbOEIiEplcI1G14CNstWeaeUtIWtPfZ2ZG5GvynrRCwXh2I8s3cZBK4yvMFdPLk6g1AkRsDEGW7GDxPvwNJF%2BONtLTbdDAF%2FSLJGEXKH8JUvRkJ%2FzyxlRDCHZ%2FD8Rx&X-Amz-Signature=c7f888029672f73cd2bcd698da9450cbb3e85b086963ec8e4942fa07527c802a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UGYH2DB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIHoUIMZ%2F2XK9pxtAVYCFP2yGUWBJNS9RnYo1V3nsyMQYAiEAziCJ6cVqdVHQssv4jUDMbVXtp86Y6IVg3T0VuFPNg4Qq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFdZAOodaLjfmNiPxCrcAwTaTLrJWY5qyxg6yR4Keop6uULYrtaEkwwyQxSFwIl30gc%2FP0Yw50E118DO%2BAq5higQ9SRRz6z66VDhX6urOFo5gPOrq38XyM5Lhg%2BgRPuL%2Fl8ShST8Y3F3uB%2Bfli4aMkvX9m7kz0JqZWh2eKLRBwLuOaCwPBrMhwbnvH2zRnITxMBlR9mx8guEKMKkCMDbN5%2BESqUE6EU25zw3UaedtsaKaTPN9zjVHqc2s%2BT3FsyT3tnN2soiyhW9yO2uvxNxQSULAFyKnfTpEpTUUTPRQXfWH0YJXto%2FRErFnN%2F3yMOgffiqvG5VMuWS5OmgekEn%2B2ACfWBctbMJj0PPhTEk%2FBenzPNmaUz8WoBdcU8o%2BcJFzcuAv42t%2B1rnQswiN672Up95FHM3OW46vnQz%2BHLo%2F5uNWpVybOAvTdiw3B5%2B8bxZ8bsy9O1DbFbkvZBpNlB%2Bmwdgq16nERP67Ful40BAe3hmILmuNktrF4hGSF21Q1Dn3yyYUHBofeZpOqRcAYGIA5zBoBxOu0onhRPfkWHIxH%2BJgF0drOGhrKylKR1b3iTyrpke8B7gmXNu%2Bv5kneAuZ8hWoisDL%2B3xb0jFU5B3ZIGuZOIhQs6b87gmYBu53oij8dJXpG1CO4hxa7%2B2MJe1jL0GOqUBndmPn5rJclwIoEn%2FSz8QRvepXjq82THre3yWK98N5LrFFpIGVVn1GVFBkYafsk2PqsUWxJ6d27yJbzqblf8IgPV75frdGnPbOEIiEplcI1G14CNstWeaeUtIWtPfZ2ZG5GvynrRCwXh2I8s3cZBK4yvMFdPLk6g1AkRsDEGW7GDxPvwNJF%2BONtLTbdDAF%2FSLJGEXKH8JUvRkJ%2FzyxlRDCHZ%2FD8Rx&X-Amz-Signature=fddb0f92731c0697fdf2f33b45d79ad569aaa4c63241efb607967da267d0f940&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTGVQN4P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFVv0s0WYe4yp4%2FuhXXQMFj%2FONM824yIFF179VxI2XebAiEA9MLef71vH%2BFH6dATtbFVYo7averLxfhKuD4338J8rX0q%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLb1DNdXSKwIZwVuXyrcA6ynFXc296ioTLMKNcU4WQuF58JHoryUhMvHNiGA%2FDWj9MPDfLRop%2Ba%2Bi1R4cyRm9kbZyVAO56dFJJVrkt%2FQifVjgppzhhI9tAcU1IUzjyNP5GaJduq1AqHFmg%2F8BvtoOY6%2FfgsbSxjSgjJBJuOsJlUrlksb4K4wk5WpCZTXjn2C0h%2B8ldGo76Vzj70Y9zP9I%2Ba9M1zlE2Fizw5%2BSeTcG2wv6BaZ7HZWgdOPgRiV%2BbPNAmfihJeGgNqEf8%2B4i9iIspD07JcDBZz8Z7AdjTrASRft1ywTK25HCqdRkj2m9Q%2BXSj5Vxz141stlz0HIAaa2qudMV4MxwROChsoTIPBRsn3Hgp8eTFUg5frf1uQvI8lUMC%2BE%2Bb5TuNppHgDE8IQz7ls403hgJksYXa%2FQMjA01SF%2BjIUoqkLdkIlCl8Pd1VYw8EPWztzYaeatOOP2rfOolabpKAFeiyovYgTeOOy29ylB8ABrsRYbnM5HXQZ6v9tRBFch0meeZGuearIW6XoO3%2Bkv9u8n4VWUJGB2Mj%2FB56ayd%2B1jYhUGFAu8V8A85N%2BLBIHHsvD8wWVyisUKrjG3Wy4TrKxm6pW67FDSfGLIBgjZfirypOs7t8rVamdMlVxlBeCfawID9WW2EwnwMJmzjL0GOqUBm%2FqVH3TPAVta333CrGtfHh8mpsaH3pTG7v5yE1nESgNoJkH48FD3nGnq%2Bg0sCzXdd%2Fi9P92EhGfane7%2Fc1hLv%2B9%2BoZ5%2BHhJ6%2FbWyKpwGLh7wAcynZ4LAFwi%2Bof6yAp%2BeAiTebBUfBZ7iaehfUowRKPuN2VqToc8UpiFH7%2FMMYcf5IzrqmVfgObi78X8m00ULvZrMmu4fy%2Bmq%2FChL9Rl89jJ9b8c9&X-Amz-Signature=51f517298573655ee939aeff8665f5c1d5f0ba8cf0482408bb7cbe2fd3d990cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR5D6YTZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIBZpQHIN027Ddx2VnncQbwXj%2Bjfkh79eCHlo1Q6iew9TAiEA3Hhrn3%2Byf9Bvei%2F1exaOasNPUv%2BRfebpuZMQWa16%2BjMq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDMoOQtAzVbnABA%2BrhSrcAwyVqKaWVURuJh%2Fbqk79M6Ur0ayrloUWMFZrr8TMEqWdcWzmnHlnKAJdGRbk%2FeCX0zOMUyBnqBcalqX6AclNG4JQiCYBsijhTq0qEprTtAwm3GVB5qRa%2BGqOxn4%2B6HlWwoiOdVwjQCBBv9O8KjaNRt9HaIo0cMJ6WcpSy%2BdJP77k928tdnOKCwIH8%2FIhqBgogufJvFW2NytVEokyqbsXa%2FVcnV0TS8pmT0wi8wOk0eKs6NECybcLDaP8IpIliDUhL%2FWCX19Cx7%2FjehLyQ1n2ajugPREEep7BdQ3e3Nrq%2FosRq59tu%2BxMMunNq%2B27kNERnGLDJX7T0lgZ6v7ueJ5bPDW%2BIfbGavKHtJESmguyC3hf3gVeARrrD6Op1JUUfMuIR9MkjkIaCeNeTJ%2BqjSdQJg8tbX6Ws2ExPJcJEVjvgj9iRlSjAx3C2oIMB0wlUoAKC5Om0oVvAizLkDtgF68jwnzpnKtKwLa%2F0Zpz4Ep%2FLEa8GD8985w0r35T%2BLfRp1dUzpNtSY%2BlR0%2BVUK%2F0aJ0bYM1zJ8fdieVd5X8LR%2FONfmGIdIv5rAQ4AU8KqcxkH3DYU767MOvoGKVFYn4m%2Fw8RFIS%2B485MeqPR9UrHrGR4HtHT6U%2BQcHhzlcXpMMqcMNGzjL0GOqUBZPZwDqFrA06fsBLMl9jEfWLbOXX4vKXYJpl5U20OiaPa47U8YckwLcDV33yI2ZEqym5PkZSxP8rK2u%2B7A%2B5ee8v6DXR%2BG3LN8dx5pdBvZ9cwLUpuKah7tyNBuj%2BLfotnQ7HATtaGY2aZKjjmmMdtyULYxjglQqvTxD1gYOw08MrqL2S3p6kb%2Fz9TrNYcbVbf6aqFyRA4om%2FaA5H86SnZ82Hc6wkn&X-Amz-Signature=9d161773892e339514e541308595c6d9f253283aa882512e6f8e249e9f982dd4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HBQ2WJ7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIDkvXzyjT%2FSLnOkBBcG5BC3gIJAQCyWTkMUsjL%2FXWup5AiEA1UfX2ASA14kfkmfk3WCNsCczuj3NnVHwSgl6buJsvVYq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDDSyqQSX0s7SP516CCrcA2h0gA2lMUuMei0da5KvGQi8iiFtxALVquTRxAstSSY%2FEI00I%2BG8TRyb02q7fCjaLos02NE2Z%2B5eAkFlRy%2BYk4E1akuoAMgKZGLzM6R%2FnRUuAMcZaPqfGMHXzorpYhAu7%2BDxK1oFG%2F352h8z8OAURvluqyNNaA%2BruyWnqyRnnc8WlpULwvlKadYnlGEd7uXh8iof%2Fiw1QSBYk4cymieUy%2BGOC8tiRkvzjTLXKFWpN8kcouD5iUKCyVQomhr5thpOHkNqChonefXX%2F2nx1gvkKFVL03WljcgAI4UqCiVzlZ2Vj1a2Yva%2FfURZJ3QjrochcVEn01mKyYDibJWRNQy64duaHl51z53G5oS0pZ%2FCS9hKvgLT%2FQKaI7tHFSV13P4YQN0HD29gojl9TIFlxHfmb5fh9Fyqt3bGThiAnbWjeCTBTPhcJtwvFuiRc%2Flb6En5TowFZxJ69GUn8YsFe40pVNet5x0xXzQPByJT2clJGrwTLv9aU7mMh9IOKk23WIpnINo7d0cTQcKRf%2FtOLSDzocrnDHe1U7rVawQDOfIxCXQsFb4FVz2ctRolD3W97xl7YV1AjLpULoSgNOoTU236AgVrYVzM%2Byg7%2Bs1yx6tHKluToWoKAluivac4dORbMNmzjL0GOqUBxO3t%2BYX3vvngvhk2GQ3P28rGNKyrbK0fgx90e2Z7bEb0PHMYIMTDiDq8eBbaMQuesNMYpCAdYDAnhaX%2BTt6Re5N0bPIkQfLiKJlMb1%2BL%2B1L5Ih0ROhx8QfpOJ%2Bq2IuaYfMGOwDIdL5aCu5Ua5eBVaZ8%2BBsN%2Fl6TivINNS8T2WMGK9uc0TAnhpRjbcVTj5eOejACJcCWZ16DakaCi3ICFXCVElz0i&X-Amz-Signature=81831225f92c06f2d06cf649ad472d8b2397a0dd97c1fd754bd5998966df204f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HBQ2WJ7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIDkvXzyjT%2FSLnOkBBcG5BC3gIJAQCyWTkMUsjL%2FXWup5AiEA1UfX2ASA14kfkmfk3WCNsCczuj3NnVHwSgl6buJsvVYq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDDSyqQSX0s7SP516CCrcA2h0gA2lMUuMei0da5KvGQi8iiFtxALVquTRxAstSSY%2FEI00I%2BG8TRyb02q7fCjaLos02NE2Z%2B5eAkFlRy%2BYk4E1akuoAMgKZGLzM6R%2FnRUuAMcZaPqfGMHXzorpYhAu7%2BDxK1oFG%2F352h8z8OAURvluqyNNaA%2BruyWnqyRnnc8WlpULwvlKadYnlGEd7uXh8iof%2Fiw1QSBYk4cymieUy%2BGOC8tiRkvzjTLXKFWpN8kcouD5iUKCyVQomhr5thpOHkNqChonefXX%2F2nx1gvkKFVL03WljcgAI4UqCiVzlZ2Vj1a2Yva%2FfURZJ3QjrochcVEn01mKyYDibJWRNQy64duaHl51z53G5oS0pZ%2FCS9hKvgLT%2FQKaI7tHFSV13P4YQN0HD29gojl9TIFlxHfmb5fh9Fyqt3bGThiAnbWjeCTBTPhcJtwvFuiRc%2Flb6En5TowFZxJ69GUn8YsFe40pVNet5x0xXzQPByJT2clJGrwTLv9aU7mMh9IOKk23WIpnINo7d0cTQcKRf%2FtOLSDzocrnDHe1U7rVawQDOfIxCXQsFb4FVz2ctRolD3W97xl7YV1AjLpULoSgNOoTU236AgVrYVzM%2Byg7%2Bs1yx6tHKluToWoKAluivac4dORbMNmzjL0GOqUBxO3t%2BYX3vvngvhk2GQ3P28rGNKyrbK0fgx90e2Z7bEb0PHMYIMTDiDq8eBbaMQuesNMYpCAdYDAnhaX%2BTt6Re5N0bPIkQfLiKJlMb1%2BL%2B1L5Ih0ROhx8QfpOJ%2Bq2IuaYfMGOwDIdL5aCu5Ua5eBVaZ8%2BBsN%2Fl6TivINNS8T2WMGK9uc0TAnhpRjbcVTj5eOejACJcCWZ16DakaCi3ICFXCVElz0i&X-Amz-Signature=62624d795aa994a7b3961e35b1c2c1c9ccc92738043575ef6922d779441fb1ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
