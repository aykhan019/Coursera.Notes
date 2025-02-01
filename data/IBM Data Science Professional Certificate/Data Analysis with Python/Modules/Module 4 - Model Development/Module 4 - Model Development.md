

# Module 4: Model Development
## Introduction to Model Development
This module delves into the process of model development, focusing on predictive modeling using datasets. It covers various regression techniques, model evaluation methods, and the importance of accurate data in making predictions.
### Key Concepts
#### **1. Simple and Multiple Linear Regression**:
- Use linear regression to predict outcomes based on one or more independent variables.
#### **2. Model Evaluation Using Visualization**:
- Visually assess the performance of models.
#### **3. Polynomial Regression and Pipelines**:
- Employ polynomial regression to capture non-linear relationships and implement pipelines for streamlined model building.
#### **4. R-squared and Mean Squared Error (MSE)**:
- Evaluate model performance using metrics such as R-squared and MSE to determine prediction accuracy.
#### **5. Prediction and Decision Making**:
- Utilize models to make informed predictions and decisions based on the data.
### Importance of Data
A model, or estimator, is essentially a mathematical equation that predicts a value based on one or more other values. It relates one or more independent variables (features) to dependent variables (outcomes). The accuracy of the model often improves with the relevance and quantity of data. Including multiple independent variables can lead to more precise predictions.
For instance, consider a scenario where predicting an outcome is based on several features. If the model's independent variables do not include a crucial feature, predictions may be inaccurate. Therefore, gathering more relevant data and exploring different types of models is cru1cial for robust model development.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD7VPCCO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7vefhfj94ly%2Fhx%2B%2BAA58oM9A0VxjATsVJzo5J6SUeTQIgWdf80c6ZBzAYGI7rZeRT493W6bAireFJfHII2HOf2K8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQ9TOrQ1CCRs%2By97ircA5oIGOqJcpKE3WfP3I%2Begdxz4glYezVbVcWqIVmPMS5hdS%2B485cLWCUFiNSW92w6yFmrjqwoL3aG2pznxEVMIFqQbc3KSjpPfVBzeHF6awG0i8f3LelucwKWKm%2FuuDQJccDovo5ORqy27k5uB2V23F0X8wjW2T3QO%2FmHXAIO%2Bm5cYFFleB1m7drZxh%2BCuHFe8ymqkJChnGpUPDw3NqtLonj%2FBF%2F%2Fy9FVgxMJZbGYNdC7ofyPL5SjTeFfwVokiEckr88sSM5f2VgOgwZF4ob7PDSZB8QgW16Oi3skBa89IWmOPtezl2UBwdFmsDHBQU%2FDAmu86V42lrbLrJBs2NIiCt3ftVTBdQtpMWu%2F0iJb49jf4sbWXzuVZcQspiflYfqfIwUXhuPRGJAKFXDRxN7R2YocCzjuG5HGa0CdXMG4QNe9bIqQ3QP6Kq89sezZymK0dMDuHdoIpCHGrpoP7AX663T5wJ6g%2BnOvQJPWWdi1OtokW8toqLSYAfMDeEOXDyS388aHkXKuy85mCDndNz11GduQQ9Mo8mdARCE7LscfPAMbXHKNHgqmvpECXmgiD22qe6%2B0Ss%2BnH0L2hZkgj21ZBq7QsLgGIMBhndMQD5Sq5kVUplINmxXwTppbeKqGMMCk97wGOqUBiGV8yEn%2BkJFuUIjzzn8WvU92s3ZDtP2PMB3VdmY8w41PM4NSB2DS2%2BsvEGRdPG1DzzT30uR17n5bCffu9vG7TpFjb%2FO9zalUFPzDLiKle3PRnQ1qjfc4OvyqvpngOCP%2F2VavAXtDYQJY5m1OV%2Fj%2FxbMn3EQ5hZvAvTI4OUuXwLEUKJk49RIp7p9zfWrb806MnKYmUUkUDzSnPjALY7e4apRHOHCl&X-Amz-Signature=bd520bcb56229c63ff2a3eb0507ed762c2c33386ec53526dd34411464a316ca2&X-Amz-SignedHeaders=host&x-id=GetObject)
___

## **1. Simple and Multiple Linear Regression**
### Linear Regression
Linear regression predicts a target value using one or more independent variables.
### 1.1 Simple Linear Regression (SLR)
SLR examines the relationship between two variables:
- Predictor (independent variable $ x $)
- Target (dependent variable $ y $)
The relationship is defined as:
$ y = b_0 + b_1 x $
- $ b_0 $: Intercept
- $ b_1  $: Slope
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD7VPCCO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7vefhfj94ly%2Fhx%2B%2BAA58oM9A0VxjATsVJzo5J6SUeTQIgWdf80c6ZBzAYGI7rZeRT493W6bAireFJfHII2HOf2K8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQ9TOrQ1CCRs%2By97ircA5oIGOqJcpKE3WfP3I%2Begdxz4glYezVbVcWqIVmPMS5hdS%2B485cLWCUFiNSW92w6yFmrjqwoL3aG2pznxEVMIFqQbc3KSjpPfVBzeHF6awG0i8f3LelucwKWKm%2FuuDQJccDovo5ORqy27k5uB2V23F0X8wjW2T3QO%2FmHXAIO%2Bm5cYFFleB1m7drZxh%2BCuHFe8ymqkJChnGpUPDw3NqtLonj%2FBF%2F%2Fy9FVgxMJZbGYNdC7ofyPL5SjTeFfwVokiEckr88sSM5f2VgOgwZF4ob7PDSZB8QgW16Oi3skBa89IWmOPtezl2UBwdFmsDHBQU%2FDAmu86V42lrbLrJBs2NIiCt3ftVTBdQtpMWu%2F0iJb49jf4sbWXzuVZcQspiflYfqfIwUXhuPRGJAKFXDRxN7R2YocCzjuG5HGa0CdXMG4QNe9bIqQ3QP6Kq89sezZymK0dMDuHdoIpCHGrpoP7AX663T5wJ6g%2BnOvQJPWWdi1OtokW8toqLSYAfMDeEOXDyS388aHkXKuy85mCDndNz11GduQQ9Mo8mdARCE7LscfPAMbXHKNHgqmvpECXmgiD22qe6%2B0Ss%2BnH0L2hZkgj21ZBq7QsLgGIMBhndMQD5Sq5kVUplINmxXwTppbeKqGMMCk97wGOqUBiGV8yEn%2BkJFuUIjzzn8WvU92s3ZDtP2PMB3VdmY8w41PM4NSB2DS2%2BsvEGRdPG1DzzT30uR17n5bCffu9vG7TpFjb%2FO9zalUFPzDLiKle3PRnQ1qjfc4OvyqvpngOCP%2F2VavAXtDYQJY5m1OV%2Fj%2FxbMn3EQ5hZvAvTI4OUuXwLEUKJk49RIp7p9zfWrb806MnKYmUUkUDzSnPjALY7e4apRHOHCl&X-Amz-Signature=0ae4fb9ea9cfd89ae1fef2619ea873766707cf9abcdf82927ce48f289e8abb94&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Step
If highway miles per gallon is 20, a linear model might predict the car price as $22,000, assuming a linear relationship.
#### Training the Model
Data points are stored in data frames or NumPy arrays. The predictor values ($ x $) and target values    ($ y $) are stored separately. The model is trained using these data points to determine the parameters $ b_0 $ and .
#### Handling Uncertainty
Factors like car make and age influence car prices. Uncertainty in the model is addressed by adding a small random value (noise) to the line. The noise is usually a small positive or negative value.
#### Python Implementation
```python
from sklearn.linear_model import LinearRegression

# Create a linear regression object
lm = LinearRegression()

# Define predictor (x) and target (y) variables
x = ...
y = ...

# Fit the model
lm.fit(x, y)

# Make predictions
predicted_values = lm.predict(x)

# Model parameters
intercept = lm.intercept_
slope = lm.coef_
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD7VPCCO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7vefhfj94ly%2Fhx%2B%2BAA58oM9A0VxjATsVJzo5J6SUeTQIgWdf80c6ZBzAYGI7rZeRT493W6bAireFJfHII2HOf2K8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQ9TOrQ1CCRs%2By97ircA5oIGOqJcpKE3WfP3I%2Begdxz4glYezVbVcWqIVmPMS5hdS%2B485cLWCUFiNSW92w6yFmrjqwoL3aG2pznxEVMIFqQbc3KSjpPfVBzeHF6awG0i8f3LelucwKWKm%2FuuDQJccDovo5ORqy27k5uB2V23F0X8wjW2T3QO%2FmHXAIO%2Bm5cYFFleB1m7drZxh%2BCuHFe8ymqkJChnGpUPDw3NqtLonj%2FBF%2F%2Fy9FVgxMJZbGYNdC7ofyPL5SjTeFfwVokiEckr88sSM5f2VgOgwZF4ob7PDSZB8QgW16Oi3skBa89IWmOPtezl2UBwdFmsDHBQU%2FDAmu86V42lrbLrJBs2NIiCt3ftVTBdQtpMWu%2F0iJb49jf4sbWXzuVZcQspiflYfqfIwUXhuPRGJAKFXDRxN7R2YocCzjuG5HGa0CdXMG4QNe9bIqQ3QP6Kq89sezZymK0dMDuHdoIpCHGrpoP7AX663T5wJ6g%2BnOvQJPWWdi1OtokW8toqLSYAfMDeEOXDyS388aHkXKuy85mCDndNz11GduQQ9Mo8mdARCE7LscfPAMbXHKNHgqmvpECXmgiD22qe6%2B0Ss%2BnH0L2hZkgj21ZBq7QsLgGIMBhndMQD5Sq5kVUplINmxXwTppbeKqGMMCk97wGOqUBiGV8yEn%2BkJFuUIjzzn8WvU92s3ZDtP2PMB3VdmY8w41PM4NSB2DS2%2BsvEGRdPG1DzzT30uR17n5bCffu9vG7TpFjb%2FO9zalUFPzDLiKle3PRnQ1qjfc4OvyqvpngOCP%2F2VavAXtDYQJY5m1OV%2Fj%2FxbMn3EQ5hZvAvTI4OUuXwLEUKJk49RIp7p9zfWrb806MnKYmUUkUDzSnPjALY7e4apRHOHCl&X-Amz-Signature=09d503e5d2b2246a67b010d1c23efd58f17c1e257188f6e3c383fa40b8bb9821&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD7VPCCO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7vefhfj94ly%2Fhx%2B%2BAA58oM9A0VxjATsVJzo5J6SUeTQIgWdf80c6ZBzAYGI7rZeRT493W6bAireFJfHII2HOf2K8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQ9TOrQ1CCRs%2By97ircA5oIGOqJcpKE3WfP3I%2Begdxz4glYezVbVcWqIVmPMS5hdS%2B485cLWCUFiNSW92w6yFmrjqwoL3aG2pznxEVMIFqQbc3KSjpPfVBzeHF6awG0i8f3LelucwKWKm%2FuuDQJccDovo5ORqy27k5uB2V23F0X8wjW2T3QO%2FmHXAIO%2Bm5cYFFleB1m7drZxh%2BCuHFe8ymqkJChnGpUPDw3NqtLonj%2FBF%2F%2Fy9FVgxMJZbGYNdC7ofyPL5SjTeFfwVokiEckr88sSM5f2VgOgwZF4ob7PDSZB8QgW16Oi3skBa89IWmOPtezl2UBwdFmsDHBQU%2FDAmu86V42lrbLrJBs2NIiCt3ftVTBdQtpMWu%2F0iJb49jf4sbWXzuVZcQspiflYfqfIwUXhuPRGJAKFXDRxN7R2YocCzjuG5HGa0CdXMG4QNe9bIqQ3QP6Kq89sezZymK0dMDuHdoIpCHGrpoP7AX663T5wJ6g%2BnOvQJPWWdi1OtokW8toqLSYAfMDeEOXDyS388aHkXKuy85mCDndNz11GduQQ9Mo8mdARCE7LscfPAMbXHKNHgqmvpECXmgiD22qe6%2B0Ss%2BnH0L2hZkgj21ZBq7QsLgGIMBhndMQD5Sq5kVUplINmxXwTppbeKqGMMCk97wGOqUBiGV8yEn%2BkJFuUIjzzn8WvU92s3ZDtP2PMB3VdmY8w41PM4NSB2DS2%2BsvEGRdPG1DzzT30uR17n5bCffu9vG7TpFjb%2FO9zalUFPzDLiKle3PRnQ1qjfc4OvyqvpngOCP%2F2VavAXtDYQJY5m1OV%2Fj%2FxbMn3EQ5hZvAvTI4OUuXwLEUKJk49RIp7p9zfWrb806MnKYmUUkUDzSnPjALY7e4apRHOHCl&X-Amz-Signature=c9f93abc6db405a778b4a0bba7411a544320ea63afcffa603286f43c143667b6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Visualization and Training
With two predictor variables ($ x_1 $ and ), data points are mapped on a 2D plane, and () values are mapped vertically.
#### Python Implementation
```python
from sklearn.linear_model import LinearRegression

# Create a linear regression object
lm = LinearRegression()

# Define predictor variables (z) and target (y)
z = ...
y = ...

# Fit the model
lm.fit(z, y)

# Make predictions
predicted_values = lm.predict(z)

# Model parameters
intercept = lm.intercept_
coefficients = lm.coef_
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD7VPCCO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7vefhfj94ly%2Fhx%2B%2BAA58oM9A0VxjATsVJzo5J6SUeTQIgWdf80c6ZBzAYGI7rZeRT493W6bAireFJfHII2HOf2K8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQ9TOrQ1CCRs%2By97ircA5oIGOqJcpKE3WfP3I%2Begdxz4glYezVbVcWqIVmPMS5hdS%2B485cLWCUFiNSW92w6yFmrjqwoL3aG2pznxEVMIFqQbc3KSjpPfVBzeHF6awG0i8f3LelucwKWKm%2FuuDQJccDovo5ORqy27k5uB2V23F0X8wjW2T3QO%2FmHXAIO%2Bm5cYFFleB1m7drZxh%2BCuHFe8ymqkJChnGpUPDw3NqtLonj%2FBF%2F%2Fy9FVgxMJZbGYNdC7ofyPL5SjTeFfwVokiEckr88sSM5f2VgOgwZF4ob7PDSZB8QgW16Oi3skBa89IWmOPtezl2UBwdFmsDHBQU%2FDAmu86V42lrbLrJBs2NIiCt3ftVTBdQtpMWu%2F0iJb49jf4sbWXzuVZcQspiflYfqfIwUXhuPRGJAKFXDRxN7R2YocCzjuG5HGa0CdXMG4QNe9bIqQ3QP6Kq89sezZymK0dMDuHdoIpCHGrpoP7AX663T5wJ6g%2BnOvQJPWWdi1OtokW8toqLSYAfMDeEOXDyS388aHkXKuy85mCDndNz11GduQQ9Mo8mdARCE7LscfPAMbXHKNHgqmvpECXmgiD22qe6%2B0Ss%2BnH0L2hZkgj21ZBq7QsLgGIMBhndMQD5Sq5kVUplINmxXwTppbeKqGMMCk97wGOqUBiGV8yEn%2BkJFuUIjzzn8WvU92s3ZDtP2PMB3VdmY8w41PM4NSB2DS2%2BsvEGRdPG1DzzT30uR17n5bCffu9vG7TpFjb%2FO9zalUFPzDLiKle3PRnQ1qjfc4OvyqvpngOCP%2F2VavAXtDYQJY5m1OV%2Fj%2FxbMn3EQ5hZvAvTI4OUuXwLEUKJk49RIp7p9zfWrb806MnKYmUUkUDzSnPjALY7e4apRHOHCl&X-Amz-Signature=47dba02d7b9779b13538af8784de8f8898f4cf2651ec7b34f92db2b8a7813661&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD7VPCCO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7vefhfj94ly%2Fhx%2B%2BAA58oM9A0VxjATsVJzo5J6SUeTQIgWdf80c6ZBzAYGI7rZeRT493W6bAireFJfHII2HOf2K8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQ9TOrQ1CCRs%2By97ircA5oIGOqJcpKE3WfP3I%2Begdxz4glYezVbVcWqIVmPMS5hdS%2B485cLWCUFiNSW92w6yFmrjqwoL3aG2pznxEVMIFqQbc3KSjpPfVBzeHF6awG0i8f3LelucwKWKm%2FuuDQJccDovo5ORqy27k5uB2V23F0X8wjW2T3QO%2FmHXAIO%2Bm5cYFFleB1m7drZxh%2BCuHFe8ymqkJChnGpUPDw3NqtLonj%2FBF%2F%2Fy9FVgxMJZbGYNdC7ofyPL5SjTeFfwVokiEckr88sSM5f2VgOgwZF4ob7PDSZB8QgW16Oi3skBa89IWmOPtezl2UBwdFmsDHBQU%2FDAmu86V42lrbLrJBs2NIiCt3ftVTBdQtpMWu%2F0iJb49jf4sbWXzuVZcQspiflYfqfIwUXhuPRGJAKFXDRxN7R2YocCzjuG5HGa0CdXMG4QNe9bIqQ3QP6Kq89sezZymK0dMDuHdoIpCHGrpoP7AX663T5wJ6g%2BnOvQJPWWdi1OtokW8toqLSYAfMDeEOXDyS388aHkXKuy85mCDndNz11GduQQ9Mo8mdARCE7LscfPAMbXHKNHgqmvpECXmgiD22qe6%2B0Ss%2BnH0L2hZkgj21ZBq7QsLgGIMBhndMQD5Sq5kVUplINmxXwTppbeKqGMMCk97wGOqUBiGV8yEn%2BkJFuUIjzzn8WvU92s3ZDtP2PMB3VdmY8w41PM4NSB2DS2%2BsvEGRdPG1DzzT30uR17n5bCffu9vG7TpFjb%2FO9zalUFPzDLiKle3PRnQ1qjfc4OvyqvpngOCP%2F2VavAXtDYQJY5m1OV%2Fj%2FxbMn3EQ5hZvAvTI4OUuXwLEUKJk49RIp7p9zfWrb806MnKYmUUkUDzSnPjALY7e4apRHOHCl&X-Amz-Signature=edceb63fc73023e77266f5b66c30f767b6c37e03823e84f1cd06edb0965f56d3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 2. Model Evaluation Using Visualization
### 1. Regression Plots
Regression plots estimate the relationship between two variables, showing the strength and direction of the correlation.
- **Horizontal Axis**: Independent variable.
- **Vertical Axis**: Dependent variable.
- **Points**: Represent different target points.
- **Fitted Line**: Represents predicted values.
#### Creating a Regression Plot
1. **Import Seaborn**:
```python
import seaborn as sns
```
2. **Use **`**regplot**`** Function**:
	- **Parameters**:
		- `x`: Independent variable column.
		- `y`: Dependent variable column.
		- `data`: Name of the DataFrame.
```python
sns.regplot(x='feature', y='target', data=df)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD7VPCCO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7vefhfj94ly%2Fhx%2B%2BAA58oM9A0VxjATsVJzo5J6SUeTQIgWdf80c6ZBzAYGI7rZeRT493W6bAireFJfHII2HOf2K8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQ9TOrQ1CCRs%2By97ircA5oIGOqJcpKE3WfP3I%2Begdxz4glYezVbVcWqIVmPMS5hdS%2B485cLWCUFiNSW92w6yFmrjqwoL3aG2pznxEVMIFqQbc3KSjpPfVBzeHF6awG0i8f3LelucwKWKm%2FuuDQJccDovo5ORqy27k5uB2V23F0X8wjW2T3QO%2FmHXAIO%2Bm5cYFFleB1m7drZxh%2BCuHFe8ymqkJChnGpUPDw3NqtLonj%2FBF%2F%2Fy9FVgxMJZbGYNdC7ofyPL5SjTeFfwVokiEckr88sSM5f2VgOgwZF4ob7PDSZB8QgW16Oi3skBa89IWmOPtezl2UBwdFmsDHBQU%2FDAmu86V42lrbLrJBs2NIiCt3ftVTBdQtpMWu%2F0iJb49jf4sbWXzuVZcQspiflYfqfIwUXhuPRGJAKFXDRxN7R2YocCzjuG5HGa0CdXMG4QNe9bIqQ3QP6Kq89sezZymK0dMDuHdoIpCHGrpoP7AX663T5wJ6g%2BnOvQJPWWdi1OtokW8toqLSYAfMDeEOXDyS388aHkXKuy85mCDndNz11GduQQ9Mo8mdARCE7LscfPAMbXHKNHgqmvpECXmgiD22qe6%2B0Ss%2BnH0L2hZkgj21ZBq7QsLgGIMBhndMQD5Sq5kVUplINmxXwTppbeKqGMMCk97wGOqUBiGV8yEn%2BkJFuUIjzzn8WvU92s3ZDtP2PMB3VdmY8w41PM4NSB2DS2%2BsvEGRdPG1DzzT30uR17n5bCffu9vG7TpFjb%2FO9zalUFPzDLiKle3PRnQ1qjfc4OvyqvpngOCP%2F2VavAXtDYQJY5m1OV%2Fj%2FxbMn3EQ5hZvAvTI4OUuXwLEUKJk49RIp7p9zfWrb806MnKYmUUkUDzSnPjALY7e4apRHOHCl&X-Amz-Signature=d908ed93e8e8303b8b03bf858d4451e1f4a09145c681e33c509edae56279ee7c&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. Residual Plots
Residual plots represent the error between actual and predicted values.
- **Process**:
	- Subtract predicted value from actual target value.
	- Plot the error on the vertical axis, dependent variable on the horizontal axis.
- **Insights**:
	- Zero mean distributed evenly around the x-axis indicates a linear model.
	- Curvature in residuals suggests a nonlinear model.
#### Creating a Residual Plot
3. **Import Seaborn**:
```python
import seaborn as sns
```
4. **Use **`**residplot**`** Function**:
	- **Parameters**:
		- Series of dependent variable (feature).
		- Series of target variable.
```python
sns.residplot(x='feature', y='target', data=df)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD7VPCCO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7vefhfj94ly%2Fhx%2B%2BAA58oM9A0VxjATsVJzo5J6SUeTQIgWdf80c6ZBzAYGI7rZeRT493W6bAireFJfHII2HOf2K8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQ9TOrQ1CCRs%2By97ircA5oIGOqJcpKE3WfP3I%2Begdxz4glYezVbVcWqIVmPMS5hdS%2B485cLWCUFiNSW92w6yFmrjqwoL3aG2pznxEVMIFqQbc3KSjpPfVBzeHF6awG0i8f3LelucwKWKm%2FuuDQJccDovo5ORqy27k5uB2V23F0X8wjW2T3QO%2FmHXAIO%2Bm5cYFFleB1m7drZxh%2BCuHFe8ymqkJChnGpUPDw3NqtLonj%2FBF%2F%2Fy9FVgxMJZbGYNdC7ofyPL5SjTeFfwVokiEckr88sSM5f2VgOgwZF4ob7PDSZB8QgW16Oi3skBa89IWmOPtezl2UBwdFmsDHBQU%2FDAmu86V42lrbLrJBs2NIiCt3ftVTBdQtpMWu%2F0iJb49jf4sbWXzuVZcQspiflYfqfIwUXhuPRGJAKFXDRxN7R2YocCzjuG5HGa0CdXMG4QNe9bIqQ3QP6Kq89sezZymK0dMDuHdoIpCHGrpoP7AX663T5wJ6g%2BnOvQJPWWdi1OtokW8toqLSYAfMDeEOXDyS388aHkXKuy85mCDndNz11GduQQ9Mo8mdARCE7LscfPAMbXHKNHgqmvpECXmgiD22qe6%2B0Ss%2BnH0L2hZkgj21ZBq7QsLgGIMBhndMQD5Sq5kVUplINmxXwTppbeKqGMMCk97wGOqUBiGV8yEn%2BkJFuUIjzzn8WvU92s3ZDtP2PMB3VdmY8w41PM4NSB2DS2%2BsvEGRdPG1DzzT30uR17n5bCffu9vG7TpFjb%2FO9zalUFPzDLiKle3PRnQ1qjfc4OvyqvpngOCP%2F2VavAXtDYQJY5m1OV%2Fj%2FxbMn3EQ5hZvAvTI4OUuXwLEUKJk49RIp7p9zfWrb806MnKYmUUkUDzSnPjALY7e4apRHOHCl&X-Amz-Signature=63f79ca8b58cf54917a639b811fb660579bb1b1d957447c7f0097a4171ec23bb&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD7VPCCO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7vefhfj94ly%2Fhx%2B%2BAA58oM9A0VxjATsVJzo5J6SUeTQIgWdf80c6ZBzAYGI7rZeRT493W6bAireFJfHII2HOf2K8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQ9TOrQ1CCRs%2By97ircA5oIGOqJcpKE3WfP3I%2Begdxz4glYezVbVcWqIVmPMS5hdS%2B485cLWCUFiNSW92w6yFmrjqwoL3aG2pznxEVMIFqQbc3KSjpPfVBzeHF6awG0i8f3LelucwKWKm%2FuuDQJccDovo5ORqy27k5uB2V23F0X8wjW2T3QO%2FmHXAIO%2Bm5cYFFleB1m7drZxh%2BCuHFe8ymqkJChnGpUPDw3NqtLonj%2FBF%2F%2Fy9FVgxMJZbGYNdC7ofyPL5SjTeFfwVokiEckr88sSM5f2VgOgwZF4ob7PDSZB8QgW16Oi3skBa89IWmOPtezl2UBwdFmsDHBQU%2FDAmu86V42lrbLrJBs2NIiCt3ftVTBdQtpMWu%2F0iJb49jf4sbWXzuVZcQspiflYfqfIwUXhuPRGJAKFXDRxN7R2YocCzjuG5HGa0CdXMG4QNe9bIqQ3QP6Kq89sezZymK0dMDuHdoIpCHGrpoP7AX663T5wJ6g%2BnOvQJPWWdi1OtokW8toqLSYAfMDeEOXDyS388aHkXKuy85mCDndNz11GduQQ9Mo8mdARCE7LscfPAMbXHKNHgqmvpECXmgiD22qe6%2B0Ss%2BnH0L2hZkgj21ZBq7QsLgGIMBhndMQD5Sq5kVUplINmxXwTppbeKqGMMCk97wGOqUBiGV8yEn%2BkJFuUIjzzn8WvU92s3ZDtP2PMB3VdmY8w41PM4NSB2DS2%2BsvEGRdPG1DzzT30uR17n5bCffu9vG7TpFjb%2FO9zalUFPzDLiKle3PRnQ1qjfc4OvyqvpngOCP%2F2VavAXtDYQJY5m1OV%2Fj%2FxbMn3EQ5hZvAvTI4OUuXwLEUKJk49RIp7p9zfWrb806MnKYmUUkUDzSnPjALY7e4apRHOHCl&X-Amz-Signature=6032b554250b458534446edde394fe4ea8e076a741de9f1872470e18937096ce&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Distribution Plots
Distribution plots visualize predicted versus actual values.
- **Use**: Helpful for models with multiple independent variables.
#### Process
- Count and plot the predicted points approximately equal to a target value.
- Repeat for various target values.
#### Creating a Distribution Plot
5. **Import Pandas** and **Seaborn**:
```python
import pandas as pd
import seaborn as sns
```
6. **Use Seaborn's Distribution Plot**:
	- **Parameters**:
		- `hist`: Set to `False` for a distribution.
		- `color`: Set to desired color.
		- `label`: Include label for legend.
```python
sns.kdeplot(predicted_values, color='blue', label='Predicted')
sns.kdeplot(actual_values, color='red', label='Actual')
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD7VPCCO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7vefhfj94ly%2Fhx%2B%2BAA58oM9A0VxjATsVJzo5J6SUeTQIgWdf80c6ZBzAYGI7rZeRT493W6bAireFJfHII2HOf2K8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQ9TOrQ1CCRs%2By97ircA5oIGOqJcpKE3WfP3I%2Begdxz4glYezVbVcWqIVmPMS5hdS%2B485cLWCUFiNSW92w6yFmrjqwoL3aG2pznxEVMIFqQbc3KSjpPfVBzeHF6awG0i8f3LelucwKWKm%2FuuDQJccDovo5ORqy27k5uB2V23F0X8wjW2T3QO%2FmHXAIO%2Bm5cYFFleB1m7drZxh%2BCuHFe8ymqkJChnGpUPDw3NqtLonj%2FBF%2F%2Fy9FVgxMJZbGYNdC7ofyPL5SjTeFfwVokiEckr88sSM5f2VgOgwZF4ob7PDSZB8QgW16Oi3skBa89IWmOPtezl2UBwdFmsDHBQU%2FDAmu86V42lrbLrJBs2NIiCt3ftVTBdQtpMWu%2F0iJb49jf4sbWXzuVZcQspiflYfqfIwUXhuPRGJAKFXDRxN7R2YocCzjuG5HGa0CdXMG4QNe9bIqQ3QP6Kq89sezZymK0dMDuHdoIpCHGrpoP7AX663T5wJ6g%2BnOvQJPWWdi1OtokW8toqLSYAfMDeEOXDyS388aHkXKuy85mCDndNz11GduQQ9Mo8mdARCE7LscfPAMbXHKNHgqmvpECXmgiD22qe6%2B0Ss%2BnH0L2hZkgj21ZBq7QsLgGIMBhndMQD5Sq5kVUplINmxXwTppbeKqGMMCk97wGOqUBiGV8yEn%2BkJFuUIjzzn8WvU92s3ZDtP2PMB3VdmY8w41PM4NSB2DS2%2BsvEGRdPG1DzzT30uR17n5bCffu9vG7TpFjb%2FO9zalUFPzDLiKle3PRnQ1qjfc4OvyqvpngOCP%2F2VavAXtDYQJY5m1OV%2Fj%2FxbMn3EQ5hZvAvTI4OUuXwLEUKJk49RIp7p9zfWrb806MnKYmUUkUDzSnPjALY7e4apRHOHCl&X-Amz-Signature=3eca79fd4f4b43864516ed2365abeaf301ed65d1eef3066822be444a231669b5&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD7VPCCO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7vefhfj94ly%2Fhx%2B%2BAA58oM9A0VxjATsVJzo5J6SUeTQIgWdf80c6ZBzAYGI7rZeRT493W6bAireFJfHII2HOf2K8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQ9TOrQ1CCRs%2By97ircA5oIGOqJcpKE3WfP3I%2Begdxz4glYezVbVcWqIVmPMS5hdS%2B485cLWCUFiNSW92w6yFmrjqwoL3aG2pznxEVMIFqQbc3KSjpPfVBzeHF6awG0i8f3LelucwKWKm%2FuuDQJccDovo5ORqy27k5uB2V23F0X8wjW2T3QO%2FmHXAIO%2Bm5cYFFleB1m7drZxh%2BCuHFe8ymqkJChnGpUPDw3NqtLonj%2FBF%2F%2Fy9FVgxMJZbGYNdC7ofyPL5SjTeFfwVokiEckr88sSM5f2VgOgwZF4ob7PDSZB8QgW16Oi3skBa89IWmOPtezl2UBwdFmsDHBQU%2FDAmu86V42lrbLrJBs2NIiCt3ftVTBdQtpMWu%2F0iJb49jf4sbWXzuVZcQspiflYfqfIwUXhuPRGJAKFXDRxN7R2YocCzjuG5HGa0CdXMG4QNe9bIqQ3QP6Kq89sezZymK0dMDuHdoIpCHGrpoP7AX663T5wJ6g%2BnOvQJPWWdi1OtokW8toqLSYAfMDeEOXDyS388aHkXKuy85mCDndNz11GduQQ9Mo8mdARCE7LscfPAMbXHKNHgqmvpECXmgiD22qe6%2B0Ss%2BnH0L2hZkgj21ZBq7QsLgGIMBhndMQD5Sq5kVUplINmxXwTppbeKqGMMCk97wGOqUBiGV8yEn%2BkJFuUIjzzn8WvU92s3ZDtP2PMB3VdmY8w41PM4NSB2DS2%2BsvEGRdPG1DzzT30uR17n5bCffu9vG7TpFjb%2FO9zalUFPzDLiKle3PRnQ1qjfc4OvyqvpngOCP%2F2VavAXtDYQJY5m1OV%2Fj%2FxbMn3EQ5hZvAvTI4OUuXwLEUKJk49RIp7p9zfWrb806MnKYmUUkUDzSnPjALY7e4apRHOHCl&X-Amz-Signature=5febb6ab9aad390f5f6a9c94743c4644f9f548f09826edda7210ee2904974d82&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Types of Polynomial Models
- **Quadratic (2nd Order)**: Includes squared terms.
- **Cubic (3rd Order)**: Includes cubed terms.
- **Higher-Order**: Used for complex relationships.
#### Example Model
- **3rd Order Polynomial**:
$$ −1.557x^3+204.8x^2+8965x+1.37×105 $$
#### Implementation in Python
- **Using NumPy**:
```python
import numpy as np
coefficients = np.polyfit(x, y, 3)
```
- **For Multidimensional**:
Use `scikit-learn` for more complex models.
#### Polynomial Features with Scikit-learn
7. **Import the Library**:
```python
from sklearn.preprocessing import PolynomialFeatures
```
8. **Create Polynomial Features**:
```python
from sklearn.linear_model import LinearRegression

# Create a PolynomialFeatures object with the desired degree
poly = PolynomialFeatures(degree=3)

# Fit and transform your data
X_poly = poly.fit_transform(X)

# Create LinearRegression model
model = LinearRegression()

# Fit the model with the polynomial features
model.fit(X_poly, y)
```
In this code:
- `degree=3` specifies the degree of the polynomial features.
- `fit_transform(X)` generates the polynomial features for your dataset `X`.
### Normalization
#### Why Normalize?
- **Purpose**: Standardize data for better model performance.
#### How to Normalize
- **Using StandardScaler**:
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
```
### Pipelines
#### What are Pipelines?
- **Purpose**: Efficiently automate data preprocessing and model training.
- **Benefit**: Simplifies complex workflows by chaining multiple steps into a single process.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664V3CSHN5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRUhvKDkUNGfF6M2TuG4CK5w1fcR2bnSUkON3h2I42BQIhAMX9ZTR1G38YHPihKFae7fVA21iT5aoHKRs5XvdlbgbGKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZgrP98g3xAk1HIxsq3AOAdTQprrvrEW8iVDuVptZLuT0AuMBB1l%2FTOlCJY4Ad%2BlmGuNZTAQFQ6jCh7yMm94HuPr14vPPeFTOUWpkc%2FXwmIOJNQaKeqK5WMMMpf1WyIv7G2q60OTVU7eri%2FjzwPuuSbimSh%2F%2BJDgCjkTsfvZk2YldNzNGLF%2FTdR3dg3ieiiIUyaoCJQBtRDZ%2B8Ez87moqjaXl%2BO8W1uFF3KamZ1orkjLytTIsfTNjrD6puJOazda8Jc0zlWp6wPlPx5LZ9%2BMv%2BzM70zuFgWmwO8yLwP9WH%2FdQxQjXeOJ6bO206tiEwSwdZ1qiIqy%2Fjsoc8n%2F4xGvwKdNTbf%2B%2F2mgzXDPu7ZiG88C5GadkUXFrqqMFLo123XMe3Dif7U60%2FHA%2BJiqW6y4z%2B%2B4J%2Bk6JFr0JQGVqKXp72LvSzArgTW316%2FayC%2FB4saja2IIrJiNpx01lbrPLzIfrHmX7cwG2ni6zSBBciz4uEez1RS1vQ7f%2FKcewenta%2BCvWL%2FQ83DiJOw3iBXeRbxsv%2Fg6CmWW7EHBSU15CFARiNIyq8efc1W0BBXURFM%2FWZyDFoKqTB3Ae%2Bn1vHFXSK42iKWxlW4uldzk5yj4v2YWPUj9C8Fsut2R1TU1dehGW4MQ%2Fq57rDCwshpAt7jzDDpPe8BjqkAS9kwxvsGuybmt26r5urUUtBc3GkEiMvYyiqfLELlQCZJwSZnWtXcjgazgfknxTCOvkcQwHWQAvjQ7ccM6UCCdcfwuHgOGtlzUfVO2iaVQBhLQ2tPUzxcZktwPXWpCs9AZnCa7iBaXng778InJ2qR7NjA9xVMEi6ECLzwPBrhM1xA%2FOc9evJHN2Mgj3rJHOnSeaNSD9wI9copyKSS2KkeeIFAEl%2B&X-Amz-Signature=b3d062dd6699c37552875899c3e8b3ef885d7b8483485603db01cd3c59e65b2c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Benefits
- **Efficiency**: Simplifies code by chaining steps.
- **Maintainability**: Makes workflow clearer.
#### Creating a Pipeline
9. **Import Pipeline**:
```python
from sklearn.pipeline import Pipeline
```
10. **Define Steps**:
```python
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures(degree=3)),
    ('model', LinearRegression())
])
```
11. **Train and Predict**:
```python
pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_test)
```
#### Key Points
- **Sequential Processing**: Automates the flow from preprocessing to prediction.
- **Versatile**: Easily adjust steps and parameters.
Use polynomial regression and pipelines to enhance model accuracy and streamline your machine learning workflow.

### Note:
#### Simple Linear Regression (SLR)
- **Definition**: Models the relationship between two variables by fitting a linear equation.
- **Equation**: $ y = b_0 + b_1x $
- **Use Case**: One independent variable predicts a dependent variable.
#### Multiple Linear Regression (MLR)
- **Definition**: Extends SLR to include multiple independent variables.
- **Equation**: $ y=b_0+b_1x_1+b_2x_2+…+b_nx_n $
- **Use Case**: Accounts for multiple factors affecting the outcome.
#### Polynomial Regression
- **Definition**: A form of regression where the relationship is modeled as an nth degree polynomial.
- **Equation**: $ y = b_0 + b_1x + b_2x^2 + \ldots + b_nx^n $
- **Use Case**: Captures non-linear relationships by transforming features.
#### Key Differences
- **SLR**: Linear relationship with one predictor.
- **MLR**: Linear relationships with multiple predictors.
- **Polynomial Regression**: Non-linear relationships using polynomial terms.
#### Example Code
```python
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Simple Linear Regression
X_slr = np.array([[20], [30], [40]])
y_slr = np.array([15000, 13000, 12000])

model_slr = LinearRegression()
model_slr.fit(X_slr, y_slr)
predicted_slr = model_slr.predict([[30]])
print("SLR Predicted Price:", predicted_slr[0])

# Multiple Linear Regression
X_mlr = np.array([[20, 5], [30, 4], [40, 6]])
y_mlr = np.array([15000, 13000, 12000])

model_mlr = LinearRegression()
model_mlr.fit(X_mlr, y_mlr)
predicted_mlr = model_mlr.predict([[30, 5]])
print("MLR Predicted Price:", predicted_mlr[0])

# Polynomial Regression
X_poly = np.array([[20], [30], [40]])
y_poly = np.array([15000, 13000, 12000])

poly = PolynomialFeatures(degree=2)
X_poly_transformed = poly.fit_transform(X_poly)

model_poly = LinearRegression()
model_poly.fit(X_poly_transformed, y_poly)
predicted_poly = model_poly.predict(poly.transform([[30]]))
print("Polynomial Predicted Price:", predicted_poly[0])
```
___
## 4. Model Evaluation Metrics
### Mean Squared Error (MSE)
- **Definition**: Measures the average squared difference between actual and predicted values. It indicates how close predictions are to the actual values.
- **Formula**: $  \text{MSE} = \frac{1}{n} \sum (y - \hat{y})^2 $
- **Python**: Use `mean_squared_error` from `sklearn.metrics`.
#### Example
**Scenario**: Predicting house prices based on size.
- **Actual Prices**: [200, 250, 300]
- **Predicted Prices**: [210, 240, 310]
**Calculation**:
$ \text{MSE} = \frac{1}{3} ((200-210)^2 + (250-240)^2 + (300-310)^2) = \frac{1}{3} (100 + 100 + 100) = 100
 $
**Python Code**:
```python
from sklearn.metrics import mean_squared_error

actual = [200, 250, 300]
predicted = [210, 240, 310]
mse = mean_squared_error(actual, predicted)
print("MSE:", mse)  # Output: MSE: 100.0
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664V3CSHN5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRUhvKDkUNGfF6M2TuG4CK5w1fcR2bnSUkON3h2I42BQIhAMX9ZTR1G38YHPihKFae7fVA21iT5aoHKRs5XvdlbgbGKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZgrP98g3xAk1HIxsq3AOAdTQprrvrEW8iVDuVptZLuT0AuMBB1l%2FTOlCJY4Ad%2BlmGuNZTAQFQ6jCh7yMm94HuPr14vPPeFTOUWpkc%2FXwmIOJNQaKeqK5WMMMpf1WyIv7G2q60OTVU7eri%2FjzwPuuSbimSh%2F%2BJDgCjkTsfvZk2YldNzNGLF%2FTdR3dg3ieiiIUyaoCJQBtRDZ%2B8Ez87moqjaXl%2BO8W1uFF3KamZ1orkjLytTIsfTNjrD6puJOazda8Jc0zlWp6wPlPx5LZ9%2BMv%2BzM70zuFgWmwO8yLwP9WH%2FdQxQjXeOJ6bO206tiEwSwdZ1qiIqy%2Fjsoc8n%2F4xGvwKdNTbf%2B%2F2mgzXDPu7ZiG88C5GadkUXFrqqMFLo123XMe3Dif7U60%2FHA%2BJiqW6y4z%2B%2B4J%2Bk6JFr0JQGVqKXp72LvSzArgTW316%2FayC%2FB4saja2IIrJiNpx01lbrPLzIfrHmX7cwG2ni6zSBBciz4uEez1RS1vQ7f%2FKcewenta%2BCvWL%2FQ83DiJOw3iBXeRbxsv%2Fg6CmWW7EHBSU15CFARiNIyq8efc1W0BBXURFM%2FWZyDFoKqTB3Ae%2Bn1vHFXSK42iKWxlW4uldzk5yj4v2YWPUj9C8Fsut2R1TU1dehGW4MQ%2Fq57rDCwshpAt7jzDDpPe8BjqkAS9kwxvsGuybmt26r5urUUtBc3GkEiMvYyiqfLELlQCZJwSZnWtXcjgazgfknxTCOvkcQwHWQAvjQ7ccM6UCCdcfwuHgOGtlzUfVO2iaVQBhLQ2tPUzxcZktwPXWpCs9AZnCa7iBaXng778InJ2qR7NjA9xVMEi6ECLzwPBrhM1xA%2FOc9evJHN2Mgj3rJHOnSeaNSD9wI9copyKSS2KkeeIFAEl%2B&X-Amz-Signature=717f41b509f5e3565deef870394cbc2e99a4c1d1ef5cb970c3b0039e6438d726&X-Amz-SignedHeaders=host&x-id=GetObject)
### R-squared (Coefficient of Determination)
- **Definition**: Indicates how well the data fits the regression line. Values range from 0 to 1, with values closer to 1 indicating a better fit.
- **Formula**: $ R^2 = 1 - \frac{\text{MSE of regression}}{\text{MSE of mean}} $
- **Python**: Use `score` method in the linear regression object.
#### Example
**Scenario**: Predicting test scores based on study hours.
**Interpretation**:
- **Good Fit**: R² = 0.9 (90% of variance explained)
- **Poor Fit**: R² = 0.2 (20% of variance explained)
**Python Code**:
```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([2, 3, 5])
model = LinearRegression()
model.fit(X, y)

r_squared = model.score(X, y)
print("R-squared:", r_squared)  # Output: R-squared: 0.9642857142857143
```
#### Example Interpretation
- **Good Fit**: Small MSE for regression, larger for mean → $ R^2 $ near 1.
- **Poor Fit**: Similar MSE for regression and mean → $ R^2 $ near 0.
- **Negative **$ R^2 $: Possible overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664V3CSHN5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRUhvKDkUNGfF6M2TuG4CK5w1fcR2bnSUkON3h2I42BQIhAMX9ZTR1G38YHPihKFae7fVA21iT5aoHKRs5XvdlbgbGKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZgrP98g3xAk1HIxsq3AOAdTQprrvrEW8iVDuVptZLuT0AuMBB1l%2FTOlCJY4Ad%2BlmGuNZTAQFQ6jCh7yMm94HuPr14vPPeFTOUWpkc%2FXwmIOJNQaKeqK5WMMMpf1WyIv7G2q60OTVU7eri%2FjzwPuuSbimSh%2F%2BJDgCjkTsfvZk2YldNzNGLF%2FTdR3dg3ieiiIUyaoCJQBtRDZ%2B8Ez87moqjaXl%2BO8W1uFF3KamZ1orkjLytTIsfTNjrD6puJOazda8Jc0zlWp6wPlPx5LZ9%2BMv%2BzM70zuFgWmwO8yLwP9WH%2FdQxQjXeOJ6bO206tiEwSwdZ1qiIqy%2Fjsoc8n%2F4xGvwKdNTbf%2B%2F2mgzXDPu7ZiG88C5GadkUXFrqqMFLo123XMe3Dif7U60%2FHA%2BJiqW6y4z%2B%2B4J%2Bk6JFr0JQGVqKXp72LvSzArgTW316%2FayC%2FB4saja2IIrJiNpx01lbrPLzIfrHmX7cwG2ni6zSBBciz4uEez1RS1vQ7f%2FKcewenta%2BCvWL%2FQ83DiJOw3iBXeRbxsv%2Fg6CmWW7EHBSU15CFARiNIyq8efc1W0BBXURFM%2FWZyDFoKqTB3Ae%2Bn1vHFXSK42iKWxlW4uldzk5yj4v2YWPUj9C8Fsut2R1TU1dehGW4MQ%2Fq57rDCwshpAt7jzDDpPe8BjqkAS9kwxvsGuybmt26r5urUUtBc3GkEiMvYyiqfLELlQCZJwSZnWtXcjgazgfknxTCOvkcQwHWQAvjQ7ccM6UCCdcfwuHgOGtlzUfVO2iaVQBhLQ2tPUzxcZktwPXWpCs9AZnCa7iBaXng778InJ2qR7NjA9xVMEi6ECLzwPBrhM1xA%2FOc9evJHN2Mgj3rJHOnSeaNSD9wI9copyKSS2KkeeIFAEl%2B&X-Amz-Signature=dc879d67702823ffffc90b413879b6d6ba42da933e6a5158682c13842c9e4bb0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664V3CSHN5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRUhvKDkUNGfF6M2TuG4CK5w1fcR2bnSUkON3h2I42BQIhAMX9ZTR1G38YHPihKFae7fVA21iT5aoHKRs5XvdlbgbGKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZgrP98g3xAk1HIxsq3AOAdTQprrvrEW8iVDuVptZLuT0AuMBB1l%2FTOlCJY4Ad%2BlmGuNZTAQFQ6jCh7yMm94HuPr14vPPeFTOUWpkc%2FXwmIOJNQaKeqK5WMMMpf1WyIv7G2q60OTVU7eri%2FjzwPuuSbimSh%2F%2BJDgCjkTsfvZk2YldNzNGLF%2FTdR3dg3ieiiIUyaoCJQBtRDZ%2B8Ez87moqjaXl%2BO8W1uFF3KamZ1orkjLytTIsfTNjrD6puJOazda8Jc0zlWp6wPlPx5LZ9%2BMv%2BzM70zuFgWmwO8yLwP9WH%2FdQxQjXeOJ6bO206tiEwSwdZ1qiIqy%2Fjsoc8n%2F4xGvwKdNTbf%2B%2F2mgzXDPu7ZiG88C5GadkUXFrqqMFLo123XMe3Dif7U60%2FHA%2BJiqW6y4z%2B%2B4J%2Bk6JFr0JQGVqKXp72LvSzArgTW316%2FayC%2FB4saja2IIrJiNpx01lbrPLzIfrHmX7cwG2ni6zSBBciz4uEez1RS1vQ7f%2FKcewenta%2BCvWL%2FQ83DiJOw3iBXeRbxsv%2Fg6CmWW7EHBSU15CFARiNIyq8efc1W0BBXURFM%2FWZyDFoKqTB3Ae%2Bn1vHFXSK42iKWxlW4uldzk5yj4v2YWPUj9C8Fsut2R1TU1dehGW4MQ%2Fq57rDCwshpAt7jzDDpPe8BjqkAS9kwxvsGuybmt26r5urUUtBc3GkEiMvYyiqfLELlQCZJwSZnWtXcjgazgfknxTCOvkcQwHWQAvjQ7ccM6UCCdcfwuHgOGtlzUfVO2iaVQBhLQ2tPUzxcZktwPXWpCs9AZnCa7iBaXng778InJ2qR7NjA9xVMEi6ECLzwPBrhM1xA%2FOc9evJHN2Mgj3rJHOnSeaNSD9wI9copyKSS2KkeeIFAEl%2B&X-Amz-Signature=e33be4075d72ae1cc3938fc5ee2bb45a1e41fa220ea0b8b2ace8efe44f995825&X-Amz-SignedHeaders=host&x-id=GetObject)
### Example: Predicting Car Price
- **Scenario**: Predict price for a car with 30 highway mpg.
- **Result**: Price = $13,771.30 (reasonable value).
#### Coefficient Interpretation
An increase of 1 mpg decreases price by $821.
#### Potential Issues
Unrealistic predictions may indicate:
- Incorrect assumptions
- Lack of data in certain ranges
### Generating Predictions
- Use NumPy's `arange` to create sequences for prediction.
```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([[20], [30], [40]])
y = np.array([15000, 13000, 12000])

# Model training
model = LinearRegression()
model.fit(X, y)

# Generating a sequence for prediction
mpg_values = np.arange(1, 101, 1)  # From 1 to 100 with step 1
predicted_prices = model.predict(mpg_values.reshape(-1, 1))

# Example prediction for 30 mpg
predicted_price = model.predict([[30]])
print("Predicted Price:", predicted_price[0])
```
#### Explanation
- `**np.arange(1, 101, 1)**`: Creates an array from 1 to 100 with a step of 1.
- `**reshape(-1, 1)**`: Reshapes the array for prediction.
### Visualization Techniques
- **Regression Plot**: Shows data trend and potential non-linear behavior.
- **Residual Plot**: Curvature indicates non-linear relationships.
- **Distribution Plot**: Highlights prediction accuracy in certain ranges.
### Evaluating Models
#### Mean Squared Error (MSE)
- **Interpretation**: Average squared difference between actual and predicted values.
**Example MSEs:**
- 495 (good fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627PRAB7P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsNQxxEu6DaNo2VqhHc61y9GJ%2FiPBDY9WihJT9gE4f1wIgLPMv5S%2BlOrO3rCnHVPdFM8GhG3iNsTwVbG2CCB5A%2F5UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPnuF5DcvxkyMNKThyrcA8kGz1yHpFbfOmfpdFkYHMgTnf64IOErV9SDatxyuIqvxs4uBnr%2F%2B06nxufFbD2I3%2BO0l12t0lW0j0vbA%2FBzCRdnLAR4W3A9REyL8TbtnTp74CB2lLECqS3LnG3C0%2Bsql%2B0E2XEJNaXWT95tf%2B0ZcK2LsWykSYCYHw%2B8JlBFK7jIa%2FasZ5G2zUCvC5jvGPmWIXMQEgGKcu1udbsSr2WoVc1ZBpYZIs2R%2FklsdT6OdAmuK4mk942uNSJj3MjAQ9%2F0EgvyG2DA4ZJy43w2y2XEssBCxb%2FQEA53zmN3kB0k%2B%2B%2F%2FMf1E3ux55Nk8Ggz8cVJOYINy8NfTCsWmhgcL9%2BE%2BosbfrrdU3HUip1BaC7VVYkibMnX7DfLAxbxPmtNet9K%2B7hb%2B%2BjkuEB4xnHa9OHDaZB4ahS6D3hWjjKTII2dYZFtNTjJzqsJ2U2BokaM9avHk6c7wMAwtc6YRyLtIwPkjBEIR9NervGhC1xbjlNvtzg2nOQcF7Q6Qq2t4fVcPZ7vldSuiffXS7wdxU42x8wUVLoAzJOCcZhIUnk0LRno2ZcIL%2BT2rl1mhDKO5bDSWfeeftB926aknkvKMFx6xIUgN984avA8mUrQ5dr693zSR4Iz3UoA2c6W4FDj4OVYCMJml97wGOqUBnocBizRL1I8kDU8CIstu1DW0IhrZl7bq1vRmKUexQt8JPhRbXWfPAzUXovMeX0SYxghSFjUCOJ%2Fh8eHGAOP9zKfVh9jiTX5853X%2BdwlnkVzG%2BwsyOy4Oun0NJvbjW19fRK66e4OqPg4V7BPN6WJBvmvmYWxsxdmLrkLx8baNf9sRZbyV5FRGC%2BLgZkRv4xcnCrK670jlFp3PctNCuXGNvp9UGVzV&X-Amz-Signature=38d2bdc93b5e05bcb4e4a18e7558d6f7709a03d1257a0134fbe485fc1a5f19de&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627PRAB7P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsNQxxEu6DaNo2VqhHc61y9GJ%2FiPBDY9WihJT9gE4f1wIgLPMv5S%2BlOrO3rCnHVPdFM8GhG3iNsTwVbG2CCB5A%2F5UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPnuF5DcvxkyMNKThyrcA8kGz1yHpFbfOmfpdFkYHMgTnf64IOErV9SDatxyuIqvxs4uBnr%2F%2B06nxufFbD2I3%2BO0l12t0lW0j0vbA%2FBzCRdnLAR4W3A9REyL8TbtnTp74CB2lLECqS3LnG3C0%2Bsql%2B0E2XEJNaXWT95tf%2B0ZcK2LsWykSYCYHw%2B8JlBFK7jIa%2FasZ5G2zUCvC5jvGPmWIXMQEgGKcu1udbsSr2WoVc1ZBpYZIs2R%2FklsdT6OdAmuK4mk942uNSJj3MjAQ9%2F0EgvyG2DA4ZJy43w2y2XEssBCxb%2FQEA53zmN3kB0k%2B%2B%2F%2FMf1E3ux55Nk8Ggz8cVJOYINy8NfTCsWmhgcL9%2BE%2BosbfrrdU3HUip1BaC7VVYkibMnX7DfLAxbxPmtNet9K%2B7hb%2B%2BjkuEB4xnHa9OHDaZB4ahS6D3hWjjKTII2dYZFtNTjJzqsJ2U2BokaM9avHk6c7wMAwtc6YRyLtIwPkjBEIR9NervGhC1xbjlNvtzg2nOQcF7Q6Qq2t4fVcPZ7vldSuiffXS7wdxU42x8wUVLoAzJOCcZhIUnk0LRno2ZcIL%2BT2rl1mhDKO5bDSWfeeftB926aknkvKMFx6xIUgN984avA8mUrQ5dr693zSR4Iz3UoA2c6W4FDj4OVYCMJml97wGOqUBnocBizRL1I8kDU8CIstu1DW0IhrZl7bq1vRmKUexQt8JPhRbXWfPAzUXovMeX0SYxghSFjUCOJ%2Fh8eHGAOP9zKfVh9jiTX5853X%2BdwlnkVzG%2BwsyOy4Oun0NJvbjW19fRK66e4OqPg4V7BPN6WJBvmvmYWxsxdmLrkLx8baNf9sRZbyV5FRGC%2BLgZkRv4xcnCrK670jlFp3PctNCuXGNvp9UGVzV&X-Amz-Signature=41fc4b94ad943d4410cce1f2fcbd6cb403212f551d2fff4654941376dec15247&X-Amz-SignedHeaders=host&x-id=GetObject)

**Code Example:**
```python
from sklearn.metrics import mean_squared_error

# Actual and predicted values
actual = [15000, 13000, 12000]
predicted = model.predict(X)

# Calculate MSE
mse = mean_squared_error(actual, predicted)
print("MSE:", mse)
```

#### R-squared (R²)
- **Definition**: Indicates how well data fits the regression line.
Example R² Values:
- 0.9986 (excellent fit)
- 0.61 (weak linear relation)
```python
# Calculate R-squared
r_squared = model.score(X, y)
print("R-squared:", r_squared) 
```
### Model Comparison
- **MLR vs. SLR**: More variables can lower MSE, but not always a better fit.
- **Polynomial Regression**: Generally has lower MSE compared to linear regression.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627PRAB7P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsNQxxEu6DaNo2VqhHc61y9GJ%2FiPBDY9WihJT9gE4f1wIgLPMv5S%2BlOrO3rCnHVPdFM8GhG3iNsTwVbG2CCB5A%2F5UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPnuF5DcvxkyMNKThyrcA8kGz1yHpFbfOmfpdFkYHMgTnf64IOErV9SDatxyuIqvxs4uBnr%2F%2B06nxufFbD2I3%2BO0l12t0lW0j0vbA%2FBzCRdnLAR4W3A9REyL8TbtnTp74CB2lLECqS3LnG3C0%2Bsql%2B0E2XEJNaXWT95tf%2B0ZcK2LsWykSYCYHw%2B8JlBFK7jIa%2FasZ5G2zUCvC5jvGPmWIXMQEgGKcu1udbsSr2WoVc1ZBpYZIs2R%2FklsdT6OdAmuK4mk942uNSJj3MjAQ9%2F0EgvyG2DA4ZJy43w2y2XEssBCxb%2FQEA53zmN3kB0k%2B%2B%2F%2FMf1E3ux55Nk8Ggz8cVJOYINy8NfTCsWmhgcL9%2BE%2BosbfrrdU3HUip1BaC7VVYkibMnX7DfLAxbxPmtNet9K%2B7hb%2B%2BjkuEB4xnHa9OHDaZB4ahS6D3hWjjKTII2dYZFtNTjJzqsJ2U2BokaM9avHk6c7wMAwtc6YRyLtIwPkjBEIR9NervGhC1xbjlNvtzg2nOQcF7Q6Qq2t4fVcPZ7vldSuiffXS7wdxU42x8wUVLoAzJOCcZhIUnk0LRno2ZcIL%2BT2rl1mhDKO5bDSWfeeftB926aknkvKMFx6xIUgN984avA8mUrQ5dr693zSR4Iz3UoA2c6W4FDj4OVYCMJml97wGOqUBnocBizRL1I8kDU8CIstu1DW0IhrZl7bq1vRmKUexQt8JPhRbXWfPAzUXovMeX0SYxghSFjUCOJ%2Fh8eHGAOP9zKfVh9jiTX5853X%2BdwlnkVzG%2BwsyOy4Oun0NJvbjW19fRK66e4OqPg4V7BPN6WJBvmvmYWxsxdmLrkLx8baNf9sRZbyV5FRGC%2BLgZkRv4xcnCrK670jlFp3PctNCuXGNvp9UGVzV&X-Amz-Signature=ba2eaccf9da3dc4086676901869a02934a8a4624f97b9cd36f295377bf23847c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Conclusion
- Evaluate models using both visualization and numerical metrics.
- Consider context and domain for interpreting R² and MSE values.
___

## Notes
### Regression Plot
When it comes to simple linear regression, an excellent way to visualize the fit of our model is by using **regression plots**.
This plot will show a combination of scattered data points (a **scatterplot**), as well as the fitted **linear regression** line going through the data. This will give us a reasonable estimate of the relationship between the two variables, the strength of the correlation, as well as the direction (positive or negative correlation).
### Residual Plot
A good way to visualize the variance of the data is to use a residual plot.
What is a **residual**?
The difference between the observed value (y) and the predicted value (ŷ) is called the residual (e). When we look at a regression plot, the residual is the distance from the data point to the fitted regression line.
So what is a **residual plot**?
A residual plot is a graph that shows the residuals on the vertical y-axis and the independent variable on the horizontal x-axis.
What do we pay attention to when looking at a residual plot?
We look at the spread of the residuals:
- If the points in a residual plot are **randomly spread out around the x-axis**, then a **linear model is appropriate** for the data.
Why is that? Randomly spread out residuals mean that the variance is constant, and thus the linear model is a good fit for this data.
### **Simple Linear Regression**
One example of a Data Model that we will be using is **Simple Linear Regression**.
Simple Linear Regression is a method to help us understand the relationship between two variables:
- The predictor/independent variable (X)
- The response/dependent variable (that we want to predict) (Y)
The result of Linear Regression is a **linear function** that predicts the response (dependent) variable as a function of the predictor (independent) variable.
### **Multiple Linear Regression**
What if we want to predict car price using more than one variable?
If we want to use more variables in our model to predict car price, we can use **Multiple Linear Regression**. Multiple Linear Regression is very similar to Simple Linear Regression, but this method is used to explain the relationship between one continuous response (dependent) variable and **two or more** predictor (independent) variables. Most of the real-world regression models involve multiple predictors. We will illustrate the structure by using four predictor variables, but these results can generalize to any number.
### **Polynomial Regression**
**Polynomial regression** is a particular case of the general linear regression model or multiple linear regression models.
We get non-linear relationships by squaring or setting higher-order terms of the predictor variables.
### Measures for In-Sample Evaluation
When evaluating our models, not only do we want to visualize the results, but we also need a quantitative measure to determine how accurate the model is.
Two very important measures that are often used in statistics to assess the accuracy of a model are:
- **R² / R-squared (The Coefficient of Determination)**
- **Mean Squared Error (MSE)**
#### R-squared
R-squared, also known as the coefficient of determination, measures how closely the data aligns with the fitted regression line.
The R-squared value represents the percentage of variation in the response variable (y) that is explained by the linear model.
#### Mean Squared Error (MSE)
The Mean Squared Error (MSE) measures the average of the squares of the errors. In other words, it calculates the difference between the actual values (y) and the estimated values (ŷ).
___
## **Cheat Sheet: Model Development**
### Linear Regression
- **Process**: Create a Linear Regression model object
- **Description**: Create an instance of the `LinearRegression` model.
- **Code Example**:
```python
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
```
### Train Linear Regression Model
- **Process**: Train the Linear Regression model
- **Description**: Fit the model on the input and output data. If there’s only one input attribute, it’s simple linear regression. If there are multiple attributes, it’s multiple linear regression.
- **Code Example**:
```python
X = df[['attribute_1', 'attribute_2', ...]]
Y = df['target_attribute']

lr.fit(X, Y)
```
### Generate Output Predictions
- **Process**: Predict the output for given input attributes
- **Description**: Use the trained model to predict the output values based on the input attributes.
- **Code Example**:
```python
Y_hat = lr.predict(X)
```
### Identify the Coefficient and Intercept
- **Process**: Retrieve the model’s coefficient and intercept
- **Description**: Access the slope coefficient and intercept values of the linear regression model.
- **Code Example**:
```python
coeff = lr.coef_
intercept = lr.intercept_
```
### Residual Plot
- **Process**: Create a Residual Plot
- **Description**: Plot the residuals (the differences between observed and predicted values) to assess the goodness of fit.
- **Code Example**:
```python
import seaborn as sns

sns.residplot(x=df['attribute_1'], y=df['attribute_2'])
```
### Distribution Plot
- **Process**: Create a Distribution Plot
- **Description**: Plot the distribution of a given attribute’s data.
- **Code Example**:
```python
import seaborn as sns

sns.distplot(df['attribute_name'], hist=False)
```
### Polynomial Regression
- **Process**: Perform Polynomial Regression
- **Description**: Fit a polynomial model to the data using NumPy.
- **Code Example**:
```python
import numpy as np

f = np.polyfit(x, y, n)
p = np.poly1d(f)
Y_hat = p(x)
```
### Multi-variate Polynomial Regression
- **Process**: Create Polynomial Features
- **Description**: Generate polynomial combinations of features up to a specified degree.
- **Code Example**:
```python
from sklearn.preprocessing import PolynomialFeatures

Z = df[['attribute_1', 'attribute_2', ...]]
pr = PolynomialFeatures(degree=n)
Z_pr = pr.fit_transform(Z)
```
### Pipeline
- **Process**: Create a Data Pipeline
- **Description**: Simplify the steps of processing data by creating a pipeline with a sequence of steps.
- **Code Example**:
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

Input = [
    ('scale', StandardScaler()),
    ('polynomial', PolynomialFeatures(include_bias=False)),
    ('model', LinearRegression())
]
pipe = Pipeline(Input)
Z = Z.astype(float)
pipe.fit(Z, y)
ypipe = pipe.predict(Z)
```
### R² Value
- **Process**: Calculate R² Value
- **Description**: Measure how well the model’s predictions fit the data. This is the proportion of variance explained by the model.
- **Code Example**:
	- For Linear Regression:
```python
from sklearn.metrics import r2_score

R2_score = lr.score(X, Y)
```
	- For Polynomial Regression:
```python
from sklearn.metrics import r2_score
import numpy as np

f = np.polyfit(x, y, n)
p = np.poly1d(f)
R2_score = r2_score(y, p(x))
```
### Mean Squared Error (MSE) Value
- **Process**: Calculate Mean Squared Error (MSE)
- **Description**: Measure the average of the squares of the errors, which are the differences between actual values and the estimated values.
- **Code Example**:
```python
from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(Y, Y_hat)
```
___

