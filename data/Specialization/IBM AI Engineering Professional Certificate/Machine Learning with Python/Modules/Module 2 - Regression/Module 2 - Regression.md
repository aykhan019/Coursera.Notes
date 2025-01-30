

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBLL7NX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBX7mJuZWA4LiWlOcRTu%2FucwqHmBAMZ%2FbyfkZ5wP61y5AiEA37lWHDgOx%2FD2AwrESMoE1U4PzgR3MQa2WMx8hDOz9tAqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCP1z9R7%2Bk8Hnfh0yircA9UFkBzb4tG0rD2Zf3NI46dUk%2BdPYqdoMYrpq3Nd2G7Vmo4ngAotKj5jUVDPQGF7PNDysa%2BvXkqgmVH2NW83cORWbHyRY9282JJxA9CvMi9RSpK6%2Bepl0o4suRPqZuPAOirCc%2F6Ehrzm8HbUPtmyyMb0Q%2BTzXtvljC7hDIwfOwU%2B05B8IrFb8yE%2Fuk5%2FOgKdGBSS33U%2Bc3nJKqTOaT1unMuL9A5%2FuxWw%2B1bt1XDIFt0RFC3WgKAe%2BsUe0MhQ7DMpsUCNd98WEjEstT52j6nGQSUcShxnAlRa3Uf9cP0IthGuYZeXQUrsYs4Is5bZ%2BHBGjvXnlwYQ0edpeCK930D9k3qC33cFLIXxagh%2Fr2sioVDXqwznCRDrVIKShC9%2BBKZlzyVxxyAXnBAQsunKkMFf1XGTakkSnHT5rmnq6tnevsckavXGb%2FyTsF1nAjpN8Jif4K%2F2QPXG%2FUfVoOIy6A5v9brEnT%2F68k9jcsPZsbAWdSWTDc%2BEnuLrHIrHhCZPkWvbNBNG3%2ByxkJ3XnxrZeC%2BvEHj%2BuAxyhFit%2BdRlztSBBn4r8LlCOAFI2u2Kq7YamvaNZuUXzpY0SA3vE9WKJ0CThC0E9mWYZxIOJ9YqS7dgb0Hyeb66W8uf24Ezu1VtMP%2F67bwGOqUBLP4%2B%2B4kl8i%2FYEe1757mXZ4FZTlM7aP0LB3FCWTHx9hMkDhnUM%2FIg3Nt3%2FMg%2BHcBgBu%2F5Ugayq3PIk5rQhehCQQhzw%2BNQqKFyegFumlECYEsSXt79F5FSlJHy2CoiPdiXx5vfpspIgPyvaryfSKENXORf21vwb7Nb6kPizpZbhP0MOeLfpLraXl%2FYh%2FQ6MpbTMvDnaX2dAEazPSCR71H0fym5d%2BGB&X-Amz-Signature=3e14e83fab12c01b4d52bace54d3d44401098ab85550618d590b5f014606e617&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBLL7NX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBX7mJuZWA4LiWlOcRTu%2FucwqHmBAMZ%2FbyfkZ5wP61y5AiEA37lWHDgOx%2FD2AwrESMoE1U4PzgR3MQa2WMx8hDOz9tAqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCP1z9R7%2Bk8Hnfh0yircA9UFkBzb4tG0rD2Zf3NI46dUk%2BdPYqdoMYrpq3Nd2G7Vmo4ngAotKj5jUVDPQGF7PNDysa%2BvXkqgmVH2NW83cORWbHyRY9282JJxA9CvMi9RSpK6%2Bepl0o4suRPqZuPAOirCc%2F6Ehrzm8HbUPtmyyMb0Q%2BTzXtvljC7hDIwfOwU%2B05B8IrFb8yE%2Fuk5%2FOgKdGBSS33U%2Bc3nJKqTOaT1unMuL9A5%2FuxWw%2B1bt1XDIFt0RFC3WgKAe%2BsUe0MhQ7DMpsUCNd98WEjEstT52j6nGQSUcShxnAlRa3Uf9cP0IthGuYZeXQUrsYs4Is5bZ%2BHBGjvXnlwYQ0edpeCK930D9k3qC33cFLIXxagh%2Fr2sioVDXqwznCRDrVIKShC9%2BBKZlzyVxxyAXnBAQsunKkMFf1XGTakkSnHT5rmnq6tnevsckavXGb%2FyTsF1nAjpN8Jif4K%2F2QPXG%2FUfVoOIy6A5v9brEnT%2F68k9jcsPZsbAWdSWTDc%2BEnuLrHIrHhCZPkWvbNBNG3%2ByxkJ3XnxrZeC%2BvEHj%2BuAxyhFit%2BdRlztSBBn4r8LlCOAFI2u2Kq7YamvaNZuUXzpY0SA3vE9WKJ0CThC0E9mWYZxIOJ9YqS7dgb0Hyeb66W8uf24Ezu1VtMP%2F67bwGOqUBLP4%2B%2B4kl8i%2FYEe1757mXZ4FZTlM7aP0LB3FCWTHx9hMkDhnUM%2FIg3Nt3%2FMg%2BHcBgBu%2F5Ugayq3PIk5rQhehCQQhzw%2BNQqKFyegFumlECYEsSXt79F5FSlJHy2CoiPdiXx5vfpspIgPyvaryfSKENXORf21vwb7Nb6kPizpZbhP0MOeLfpLraXl%2FYh%2FQ6MpbTMvDnaX2dAEazPSCR71H0fym5d%2BGB&X-Amz-Signature=6a1b3a658ce55ebffe3c7fc0c855a34561a776d1fe406a00e77d75687026b220&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBLL7NX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBX7mJuZWA4LiWlOcRTu%2FucwqHmBAMZ%2FbyfkZ5wP61y5AiEA37lWHDgOx%2FD2AwrESMoE1U4PzgR3MQa2WMx8hDOz9tAqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCP1z9R7%2Bk8Hnfh0yircA9UFkBzb4tG0rD2Zf3NI46dUk%2BdPYqdoMYrpq3Nd2G7Vmo4ngAotKj5jUVDPQGF7PNDysa%2BvXkqgmVH2NW83cORWbHyRY9282JJxA9CvMi9RSpK6%2Bepl0o4suRPqZuPAOirCc%2F6Ehrzm8HbUPtmyyMb0Q%2BTzXtvljC7hDIwfOwU%2B05B8IrFb8yE%2Fuk5%2FOgKdGBSS33U%2Bc3nJKqTOaT1unMuL9A5%2FuxWw%2B1bt1XDIFt0RFC3WgKAe%2BsUe0MhQ7DMpsUCNd98WEjEstT52j6nGQSUcShxnAlRa3Uf9cP0IthGuYZeXQUrsYs4Is5bZ%2BHBGjvXnlwYQ0edpeCK930D9k3qC33cFLIXxagh%2Fr2sioVDXqwznCRDrVIKShC9%2BBKZlzyVxxyAXnBAQsunKkMFf1XGTakkSnHT5rmnq6tnevsckavXGb%2FyTsF1nAjpN8Jif4K%2F2QPXG%2FUfVoOIy6A5v9brEnT%2F68k9jcsPZsbAWdSWTDc%2BEnuLrHIrHhCZPkWvbNBNG3%2ByxkJ3XnxrZeC%2BvEHj%2BuAxyhFit%2BdRlztSBBn4r8LlCOAFI2u2Kq7YamvaNZuUXzpY0SA3vE9WKJ0CThC0E9mWYZxIOJ9YqS7dgb0Hyeb66W8uf24Ezu1VtMP%2F67bwGOqUBLP4%2B%2B4kl8i%2FYEe1757mXZ4FZTlM7aP0LB3FCWTHx9hMkDhnUM%2FIg3Nt3%2FMg%2BHcBgBu%2F5Ugayq3PIk5rQhehCQQhzw%2BNQqKFyegFumlECYEsSXt79F5FSlJHy2CoiPdiXx5vfpspIgPyvaryfSKENXORf21vwb7Nb6kPizpZbhP0MOeLfpLraXl%2FYh%2FQ6MpbTMvDnaX2dAEazPSCR71H0fym5d%2BGB&X-Amz-Signature=e96983e16633c39a6ca7952fa210b83be014d7c42ab176392907719b83003734&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBLL7NX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBX7mJuZWA4LiWlOcRTu%2FucwqHmBAMZ%2FbyfkZ5wP61y5AiEA37lWHDgOx%2FD2AwrESMoE1U4PzgR3MQa2WMx8hDOz9tAqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCP1z9R7%2Bk8Hnfh0yircA9UFkBzb4tG0rD2Zf3NI46dUk%2BdPYqdoMYrpq3Nd2G7Vmo4ngAotKj5jUVDPQGF7PNDysa%2BvXkqgmVH2NW83cORWbHyRY9282JJxA9CvMi9RSpK6%2Bepl0o4suRPqZuPAOirCc%2F6Ehrzm8HbUPtmyyMb0Q%2BTzXtvljC7hDIwfOwU%2B05B8IrFb8yE%2Fuk5%2FOgKdGBSS33U%2Bc3nJKqTOaT1unMuL9A5%2FuxWw%2B1bt1XDIFt0RFC3WgKAe%2BsUe0MhQ7DMpsUCNd98WEjEstT52j6nGQSUcShxnAlRa3Uf9cP0IthGuYZeXQUrsYs4Is5bZ%2BHBGjvXnlwYQ0edpeCK930D9k3qC33cFLIXxagh%2Fr2sioVDXqwznCRDrVIKShC9%2BBKZlzyVxxyAXnBAQsunKkMFf1XGTakkSnHT5rmnq6tnevsckavXGb%2FyTsF1nAjpN8Jif4K%2F2QPXG%2FUfVoOIy6A5v9brEnT%2F68k9jcsPZsbAWdSWTDc%2BEnuLrHIrHhCZPkWvbNBNG3%2ByxkJ3XnxrZeC%2BvEHj%2BuAxyhFit%2BdRlztSBBn4r8LlCOAFI2u2Kq7YamvaNZuUXzpY0SA3vE9WKJ0CThC0E9mWYZxIOJ9YqS7dgb0Hyeb66W8uf24Ezu1VtMP%2F67bwGOqUBLP4%2B%2B4kl8i%2FYEe1757mXZ4FZTlM7aP0LB3FCWTHx9hMkDhnUM%2FIg3Nt3%2FMg%2BHcBgBu%2F5Ugayq3PIk5rQhehCQQhzw%2BNQqKFyegFumlECYEsSXt79F5FSlJHy2CoiPdiXx5vfpspIgPyvaryfSKENXORf21vwb7Nb6kPizpZbhP0MOeLfpLraXl%2FYh%2FQ6MpbTMvDnaX2dAEazPSCR71H0fym5d%2BGB&X-Amz-Signature=b29b3cb8db2a9bedb8b281b08f2f9032018597c66c9abca337b3b109edee6d66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBLL7NX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBX7mJuZWA4LiWlOcRTu%2FucwqHmBAMZ%2FbyfkZ5wP61y5AiEA37lWHDgOx%2FD2AwrESMoE1U4PzgR3MQa2WMx8hDOz9tAqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCP1z9R7%2Bk8Hnfh0yircA9UFkBzb4tG0rD2Zf3NI46dUk%2BdPYqdoMYrpq3Nd2G7Vmo4ngAotKj5jUVDPQGF7PNDysa%2BvXkqgmVH2NW83cORWbHyRY9282JJxA9CvMi9RSpK6%2Bepl0o4suRPqZuPAOirCc%2F6Ehrzm8HbUPtmyyMb0Q%2BTzXtvljC7hDIwfOwU%2B05B8IrFb8yE%2Fuk5%2FOgKdGBSS33U%2Bc3nJKqTOaT1unMuL9A5%2FuxWw%2B1bt1XDIFt0RFC3WgKAe%2BsUe0MhQ7DMpsUCNd98WEjEstT52j6nGQSUcShxnAlRa3Uf9cP0IthGuYZeXQUrsYs4Is5bZ%2BHBGjvXnlwYQ0edpeCK930D9k3qC33cFLIXxagh%2Fr2sioVDXqwznCRDrVIKShC9%2BBKZlzyVxxyAXnBAQsunKkMFf1XGTakkSnHT5rmnq6tnevsckavXGb%2FyTsF1nAjpN8Jif4K%2F2QPXG%2FUfVoOIy6A5v9brEnT%2F68k9jcsPZsbAWdSWTDc%2BEnuLrHIrHhCZPkWvbNBNG3%2ByxkJ3XnxrZeC%2BvEHj%2BuAxyhFit%2BdRlztSBBn4r8LlCOAFI2u2Kq7YamvaNZuUXzpY0SA3vE9WKJ0CThC0E9mWYZxIOJ9YqS7dgb0Hyeb66W8uf24Ezu1VtMP%2F67bwGOqUBLP4%2B%2B4kl8i%2FYEe1757mXZ4FZTlM7aP0LB3FCWTHx9hMkDhnUM%2FIg3Nt3%2FMg%2BHcBgBu%2F5Ugayq3PIk5rQhehCQQhzw%2BNQqKFyegFumlECYEsSXt79F5FSlJHy2CoiPdiXx5vfpspIgPyvaryfSKENXORf21vwb7Nb6kPizpZbhP0MOeLfpLraXl%2FYh%2FQ6MpbTMvDnaX2dAEazPSCR71H0fym5d%2BGB&X-Amz-Signature=5992d83bdd6f39e05fe52dc343f0d2dbdb7a0f732a4786b2d16e427dd68c9cd5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBLL7NX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBX7mJuZWA4LiWlOcRTu%2FucwqHmBAMZ%2FbyfkZ5wP61y5AiEA37lWHDgOx%2FD2AwrESMoE1U4PzgR3MQa2WMx8hDOz9tAqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCP1z9R7%2Bk8Hnfh0yircA9UFkBzb4tG0rD2Zf3NI46dUk%2BdPYqdoMYrpq3Nd2G7Vmo4ngAotKj5jUVDPQGF7PNDysa%2BvXkqgmVH2NW83cORWbHyRY9282JJxA9CvMi9RSpK6%2Bepl0o4suRPqZuPAOirCc%2F6Ehrzm8HbUPtmyyMb0Q%2BTzXtvljC7hDIwfOwU%2B05B8IrFb8yE%2Fuk5%2FOgKdGBSS33U%2Bc3nJKqTOaT1unMuL9A5%2FuxWw%2B1bt1XDIFt0RFC3WgKAe%2BsUe0MhQ7DMpsUCNd98WEjEstT52j6nGQSUcShxnAlRa3Uf9cP0IthGuYZeXQUrsYs4Is5bZ%2BHBGjvXnlwYQ0edpeCK930D9k3qC33cFLIXxagh%2Fr2sioVDXqwznCRDrVIKShC9%2BBKZlzyVxxyAXnBAQsunKkMFf1XGTakkSnHT5rmnq6tnevsckavXGb%2FyTsF1nAjpN8Jif4K%2F2QPXG%2FUfVoOIy6A5v9brEnT%2F68k9jcsPZsbAWdSWTDc%2BEnuLrHIrHhCZPkWvbNBNG3%2ByxkJ3XnxrZeC%2BvEHj%2BuAxyhFit%2BdRlztSBBn4r8LlCOAFI2u2Kq7YamvaNZuUXzpY0SA3vE9WKJ0CThC0E9mWYZxIOJ9YqS7dgb0Hyeb66W8uf24Ezu1VtMP%2F67bwGOqUBLP4%2B%2B4kl8i%2FYEe1757mXZ4FZTlM7aP0LB3FCWTHx9hMkDhnUM%2FIg3Nt3%2FMg%2BHcBgBu%2F5Ugayq3PIk5rQhehCQQhzw%2BNQqKFyegFumlECYEsSXt79F5FSlJHy2CoiPdiXx5vfpspIgPyvaryfSKENXORf21vwb7Nb6kPizpZbhP0MOeLfpLraXl%2FYh%2FQ6MpbTMvDnaX2dAEazPSCR71H0fym5d%2BGB&X-Amz-Signature=358cf890bcd436df1b57e9ce6bb6cde6868c4e847602127feca20244dbaba63d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBLL7NX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBX7mJuZWA4LiWlOcRTu%2FucwqHmBAMZ%2FbyfkZ5wP61y5AiEA37lWHDgOx%2FD2AwrESMoE1U4PzgR3MQa2WMx8hDOz9tAqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCP1z9R7%2Bk8Hnfh0yircA9UFkBzb4tG0rD2Zf3NI46dUk%2BdPYqdoMYrpq3Nd2G7Vmo4ngAotKj5jUVDPQGF7PNDysa%2BvXkqgmVH2NW83cORWbHyRY9282JJxA9CvMi9RSpK6%2Bepl0o4suRPqZuPAOirCc%2F6Ehrzm8HbUPtmyyMb0Q%2BTzXtvljC7hDIwfOwU%2B05B8IrFb8yE%2Fuk5%2FOgKdGBSS33U%2Bc3nJKqTOaT1unMuL9A5%2FuxWw%2B1bt1XDIFt0RFC3WgKAe%2BsUe0MhQ7DMpsUCNd98WEjEstT52j6nGQSUcShxnAlRa3Uf9cP0IthGuYZeXQUrsYs4Is5bZ%2BHBGjvXnlwYQ0edpeCK930D9k3qC33cFLIXxagh%2Fr2sioVDXqwznCRDrVIKShC9%2BBKZlzyVxxyAXnBAQsunKkMFf1XGTakkSnHT5rmnq6tnevsckavXGb%2FyTsF1nAjpN8Jif4K%2F2QPXG%2FUfVoOIy6A5v9brEnT%2F68k9jcsPZsbAWdSWTDc%2BEnuLrHIrHhCZPkWvbNBNG3%2ByxkJ3XnxrZeC%2BvEHj%2BuAxyhFit%2BdRlztSBBn4r8LlCOAFI2u2Kq7YamvaNZuUXzpY0SA3vE9WKJ0CThC0E9mWYZxIOJ9YqS7dgb0Hyeb66W8uf24Ezu1VtMP%2F67bwGOqUBLP4%2B%2B4kl8i%2FYEe1757mXZ4FZTlM7aP0LB3FCWTHx9hMkDhnUM%2FIg3Nt3%2FMg%2BHcBgBu%2F5Ugayq3PIk5rQhehCQQhzw%2BNQqKFyegFumlECYEsSXt79F5FSlJHy2CoiPdiXx5vfpspIgPyvaryfSKENXORf21vwb7Nb6kPizpZbhP0MOeLfpLraXl%2FYh%2FQ6MpbTMvDnaX2dAEazPSCR71H0fym5d%2BGB&X-Amz-Signature=f7c606b27cd7caff61bd5a82eb5d5efc71d2d99712502e7073167d6dddcc82ce&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBLL7NX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBX7mJuZWA4LiWlOcRTu%2FucwqHmBAMZ%2FbyfkZ5wP61y5AiEA37lWHDgOx%2FD2AwrESMoE1U4PzgR3MQa2WMx8hDOz9tAqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCP1z9R7%2Bk8Hnfh0yircA9UFkBzb4tG0rD2Zf3NI46dUk%2BdPYqdoMYrpq3Nd2G7Vmo4ngAotKj5jUVDPQGF7PNDysa%2BvXkqgmVH2NW83cORWbHyRY9282JJxA9CvMi9RSpK6%2Bepl0o4suRPqZuPAOirCc%2F6Ehrzm8HbUPtmyyMb0Q%2BTzXtvljC7hDIwfOwU%2B05B8IrFb8yE%2Fuk5%2FOgKdGBSS33U%2Bc3nJKqTOaT1unMuL9A5%2FuxWw%2B1bt1XDIFt0RFC3WgKAe%2BsUe0MhQ7DMpsUCNd98WEjEstT52j6nGQSUcShxnAlRa3Uf9cP0IthGuYZeXQUrsYs4Is5bZ%2BHBGjvXnlwYQ0edpeCK930D9k3qC33cFLIXxagh%2Fr2sioVDXqwznCRDrVIKShC9%2BBKZlzyVxxyAXnBAQsunKkMFf1XGTakkSnHT5rmnq6tnevsckavXGb%2FyTsF1nAjpN8Jif4K%2F2QPXG%2FUfVoOIy6A5v9brEnT%2F68k9jcsPZsbAWdSWTDc%2BEnuLrHIrHhCZPkWvbNBNG3%2ByxkJ3XnxrZeC%2BvEHj%2BuAxyhFit%2BdRlztSBBn4r8LlCOAFI2u2Kq7YamvaNZuUXzpY0SA3vE9WKJ0CThC0E9mWYZxIOJ9YqS7dgb0Hyeb66W8uf24Ezu1VtMP%2F67bwGOqUBLP4%2B%2B4kl8i%2FYEe1757mXZ4FZTlM7aP0LB3FCWTHx9hMkDhnUM%2FIg3Nt3%2FMg%2BHcBgBu%2F5Ugayq3PIk5rQhehCQQhzw%2BNQqKFyegFumlECYEsSXt79F5FSlJHy2CoiPdiXx5vfpspIgPyvaryfSKENXORf21vwb7Nb6kPizpZbhP0MOeLfpLraXl%2FYh%2FQ6MpbTMvDnaX2dAEazPSCR71H0fym5d%2BGB&X-Amz-Signature=43ef1da2e4692bb749b77f11edeed88e2a31e45b2d135c441f622133e4a2f7b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUD3GZXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8yyy8rxOQ8NDDIUOOPtWe9pUoPa4zzr3cNbbrtYABNwIhANy2QN37eord0fEh%2Fby9PeGYvGm3OquLRMY6o%2BrhzJ7ZKogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwozi5XMK8cjYsasH0q3AP8BbT%2BIkPOIsCV42R%2FBzB20SzEq2DCXOzQT8ahfqVULdPATmhnnpTGBP7Vo47r6%2FPlcS%2FDVZ1KTzlpDcr1pl%2BuUbC9Xj6SK9Ix7fEDmMDOSVi%2Bgj7FVbhPvKXMSR2ZBIiV97Vxi3axA2FEzlVy3xX4VbSuRpFND3QS3J9Aq9KCGvou7tTv1XtJMUjeYVxDiB7H30ntz%2Fl62bhPQKJVvcHELz%2Fz1iBunjcQhd9IC771goVIMcQdc5AVSqx4LiNHMvEVHZ2gANMWpRjTV%2FgCAMubJljOdwNHF8Y7bTXC8QwHN5RnsUG77EcHVyVnOcqdvWi73eLqq8JIClg6S6pIU7YtrrQZ4cS%2Bt0XU2eyobf%2Bo%2FY%2B88spj7pVCKIGk8m3lJ%2B1LVD4BbMaQXKYmGtGvupzuFIbRBAWlKRdjsh1j10Q5Whhw1%2B6kmUCrXTcA8B4RRrHbSWTilmcqQca22UwY96aTnK5%2F6Ccmij%2BG7vUj7zR2FJ%2FoQqbJy%2B6GawYYd2YN81fCi9hOPdAkDfpcvviiqOsDlRY0t2YxJmf5WrNtuYxKhNB8%2BzjB%2BlPfPZvBtLp33EjhuED370xAmD2EZZeAFHUOkrdS3nsp7wo66USuHN3ENWlfWoBHds80AsnZMDDO%2Bu28BjqkATBZcry6kNwQXit4BsUYTAnbFh2nTHKt%2FcA1R5ZrKcpT1diq6Vus%2BhLkmJYskiZM4372p1zxgwk0h1%2F8ojosrxD4hFIRd22RR4qasRLjA2I3bRMXKXa75cl6XSwpG6JYwvzXKK9cQw8c57b8IVD3o0lmQQQPPZ4ng36Q9eMOS6U1zwgoLJiYHe8djRhQc4oqk%2FCuX64GsMZNbAZLf5qU6LPUm0HE&X-Amz-Signature=f2190555cda4c3e1dcb847d5973e6f68593c8ada57aa4a0016b786e75f36b1ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JLBNV7C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDStCIf070dNswtZ8BJy29GbKjIPcXTEcIE1fikUH1DYgIhAOpZ1UTKtKGOE72uuxHr%2BOyMFvxp%2Bwx4n11AyN6QKvjiKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsRGb%2Fj1PqFWgP5CIq3AOZbns4YbyynozKLAiCOBIbnUlj4qO%2FH%2B6PGOPG1jo%2FJoJY5FUt9oh0t7LKUQg1SF74oP9KXl2tQ1kgVDiYQADALLpbhVJcncO80qZ1AUWxRA1rjD%2FCJJEZoNEOaCooNyRG3jCmQTZOcNBc1pg2qO3w1%2FXePKGVBMw%2Bi%2BYIiF7v%2FBhOyVv97GsJ4jHt%2FGFX6XmxIWzs8vGTkms4WJsuJVACNsfZJg6NNjo0fQXkeOCK85dz3jXyTLsAolf0fade%2BSTpVALdhn3vmAfaWVFqCdZL5Mhw0LJXZYinUQclRIGNgK9%2Faju6o3c5UIucHdCFSsW8FvzakJbW53mD7lZGDQBhyOA1qIjo0A8Hzv4E6r4PC3QSflAbvdNLDE36P7CkauCJ3jGZOfXkLZSeyjMwVzuWvJ7Uy38fg1BYsehURRiVq%2BIY1w0TVySnYdUwQFX8GQNhwiH0SMyXMXUKt2lUZ0P9GmTtNWUvwegNE7g%2FiCVnWazE9KIXI5u0ZfDmprT%2FCvwxLyPHt%2Fr73FT95m8a9np37Xvj45jkSvqgDLIcZTuGI4%2BPeojkQ0ycnsDPbp0FbXjWgT8aGfS7LN26HngFkXjac8Jd79P5PD77DfMWQtdFqbN9fAmdEAqSdir14DDH%2Bu28BjqkAeOxKzbvU%2BzVhaly%2BlDPILSOQ%2B5oYIA8BkNqAqW4qpvSo2hy6hPeD%2FNQh3rTFE37Y0Hyf%2FJ7%2FhPAuDVapOh2BlqbrCt6F6GO7TJSoKf2wdr%2BgEy7%2BaIxcBbAQ7MR9ip4A29djM93g7QNiDh%2Bv6AA1p6VJd09Cse56a2mqdI4PFYy30KfCcH%2Bwg3wzIfbccKKJv7aU4tOb8s8rOpL1VhbMtAM9coR&X-Amz-Signature=50d1d6899af586f9f1dd78a771cde75b82311504134bd55cbe5c50839fc4f484&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UHXHI4O%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD86nIKsNPyOoABFqYR2gKTsPq8j9Hpfci%2FeAj3B4p6%2FQIhAKJnjkk2IWubvpKdEKD7WBnS9569Zspc3g82ErX8gXmkKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2J893X04tz2sw%2Bqkq3AOKlZZKM87%2BE611lGSoNuaXSK2pUFSLDU23sw4vrMqS%2F5mAUCyiolQNNi7OOqU3vfOIeZJJKIDXaKoMlh52jAgqXmgLamht0SFOle2cFpk%2FunlxQdVqAfrUM53vAeuPuwJSrmVUGjyl8o2ctbx3ZnGuy5HeCzZ1k%2BCTbOwMc8TsBG4cUo9OHNKjrxFfER%2FoioVRKc4ug8sf2I%2FS9hGJ%2FvZC3Pud9MnZR9ycxF1%2BfCMl2J5rUkI51ndyUcgZILk%2BqTQ3vTQXJNbNV6GwHU5h2RJDHwJxe0PQPAJZFiBCPLfjpIbMVbHthXzvLC1qA%2BCxuIzbydgVeNbU6zu3IqOllKroxtfMBRIj7CgZkMzHNhcsw04cVWAQvE%2FTrHPPXkDB7SSAAWEY73M4FMW6WC9YCfT6otQ2pVfBQdYT0nPQC5aaRyNEXw9MNSaZgHSIiDQy73AKyYs3EIvumhX6BI%2F7w5DrmwGKwLnKxwI%2BEjxVzq0Ddipv0U7VYs2e4L79xmsL7COMipPnfCbfJmX%2BztBO4nCDSOBS9BtxvNv%2BjtXsyau6TNHgStWwWB2vSZj%2FDB4xLSEJSby23vV62H8wcCwOTYJhATPsVPZwt%2BVvf0JHWYFEnf7JCuCu5R7WyPs1gDD2%2Bu28BjqkATbnedj8O9ZojJ%2BYYUmKomHeVhV9QciIKWAoXtDh08dlSqVIjjTyhTdgulzi5XJcfsE3s7vCuzTBz303fnbnZgv7%2FM28MP%2BVoTOw4seUMsB7ye%2FVqBH5o7rHZ%2BOkjbi%2BMYXK4nnKmD551W7UwsEbzQ2UKxOsJ3fE3LvsxCgCX6%2BdKJvCy5F3iijgnYBB6NoPCpcg1E%2BUHvbcL651SR5Af4jbvT0%2B&X-Amz-Signature=6d5cbfbb4e16f71504ccdf27c2cf0472c732000ae9cf6258ba2ec3fc0e0314bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UHXHI4O%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD86nIKsNPyOoABFqYR2gKTsPq8j9Hpfci%2FeAj3B4p6%2FQIhAKJnjkk2IWubvpKdEKD7WBnS9569Zspc3g82ErX8gXmkKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2J893X04tz2sw%2Bqkq3AOKlZZKM87%2BE611lGSoNuaXSK2pUFSLDU23sw4vrMqS%2F5mAUCyiolQNNi7OOqU3vfOIeZJJKIDXaKoMlh52jAgqXmgLamht0SFOle2cFpk%2FunlxQdVqAfrUM53vAeuPuwJSrmVUGjyl8o2ctbx3ZnGuy5HeCzZ1k%2BCTbOwMc8TsBG4cUo9OHNKjrxFfER%2FoioVRKc4ug8sf2I%2FS9hGJ%2FvZC3Pud9MnZR9ycxF1%2BfCMl2J5rUkI51ndyUcgZILk%2BqTQ3vTQXJNbNV6GwHU5h2RJDHwJxe0PQPAJZFiBCPLfjpIbMVbHthXzvLC1qA%2BCxuIzbydgVeNbU6zu3IqOllKroxtfMBRIj7CgZkMzHNhcsw04cVWAQvE%2FTrHPPXkDB7SSAAWEY73M4FMW6WC9YCfT6otQ2pVfBQdYT0nPQC5aaRyNEXw9MNSaZgHSIiDQy73AKyYs3EIvumhX6BI%2F7w5DrmwGKwLnKxwI%2BEjxVzq0Ddipv0U7VYs2e4L79xmsL7COMipPnfCbfJmX%2BztBO4nCDSOBS9BtxvNv%2BjtXsyau6TNHgStWwWB2vSZj%2FDB4xLSEJSby23vV62H8wcCwOTYJhATPsVPZwt%2BVvf0JHWYFEnf7JCuCu5R7WyPs1gDD2%2Bu28BjqkATbnedj8O9ZojJ%2BYYUmKomHeVhV9QciIKWAoXtDh08dlSqVIjjTyhTdgulzi5XJcfsE3s7vCuzTBz303fnbnZgv7%2FM28MP%2BVoTOw4seUMsB7ye%2FVqBH5o7rHZ%2BOkjbi%2BMYXK4nnKmD551W7UwsEbzQ2UKxOsJ3fE3LvsxCgCX6%2BdKJvCy5F3iijgnYBB6NoPCpcg1E%2BUHvbcL651SR5Af4jbvT0%2B&X-Amz-Signature=812c6888b0b0ea6798481b9cea38edee55daadefaf4d662760ef14e91f8f8dff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
