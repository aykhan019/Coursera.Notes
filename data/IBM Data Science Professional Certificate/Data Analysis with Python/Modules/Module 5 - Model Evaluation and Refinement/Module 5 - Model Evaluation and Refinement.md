

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=3494295b5166108e3b535bf3b0ad641a1de5f4335adce646d753ab3ccbfb41ad&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=17cc9bc6826438929227577a13de320bc18c8c8a9ec1ccb0b7a3f3ea3d9f0571&X-Amz-SignedHeaders=host&x-id=GetObject)
**Example Code**:
```python
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# X_train: Training data for the predictors
# X_test: Testing data for the predictors
# y_train: Training data for the target variable
# y_test: Testing data for the target variable
# test_size=0.3: 30% of the data will be used for testing, and 70% will be used for training
# random_state=42:Ensures reproducibility of the split. Using the same random state will produce the same split every time
```
### Generalization Error
- **Generalization Error**: Measures how well the model predicts new data. The error obtained using testing data approximates this error.
### Cross-Validation
**Cross-Validation**: A technique to assess the model's performance and estimate generalization error by splitting the data into multiple folds.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=a1842b87a0460f2eed7a0a14fd13d89bebc16f214be083b9c967adfb68d64ade&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=85c05ead1427a9b2c472c97556881b34777c16c192866662f510c3ab0a874f1c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=c7f8b8e4c189d1fcca6259932ddd85f3cba3179ac5cd7e257554efd7f320f3d4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Cross-Val Predict
**cross_val_predict** is used when you want to obtain the predicted values for each test fold during the cross-validation process. It returns the prediction for each data point when it was in the test set. This is useful for:
5. **Visualizing Predictions**: You can plot the predicted values against the actual values to see how well the model performs across the entire dataset.
6. **Diagnostics**: It helps in analyzing the residuals (differences between actual and predicted values) to diagnose model performance.
#### Example in Python
Here's an example using `cross_val_predict`:
```python
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Example dataset
X = np.random.rand(100, 5)
y = np.random.rand(100)

# Initialize the model
model = LinearRegression()

# Get cross-validated predictions
y_pred = cross_val_predict(model, X, y, cv=5)

# Plot actual vs. predicted values
plt.scatter(y, y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Cross-Validated Predictions')
plt.show()
```
In this example:
- `cross_val_predict` returns the predicted values for each test fold during the 5-fold cross-validation.
- A scatter plot is created to visualize the actual vs. predicted values.
#### Summary
- **Training Set**: Used to build the model.
- **Testing Set**: Used to evaluate model performance.
- **Cross-Validation**: Provides a robust estimate of model performance by averaging results across multiple folds.
___
## Model Selection and Polynomial Regression
When selecting the best polynomial order, our goal is to provide the best estimate of the
function $ y(x) $.
### Noise in Data
**Noise** in data refers to random variations or errors that obscure the true underlying patterns or relationships. It can come from various sources and affects the accuracy of models.
### **Underfitting** 
**Underfitting** occurs when the model is too simple to fit the data:
- Example: Fitting a linear function to data generated from a higher-order polynomial plus noise results in many errors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=48618db7152b2a5ba90c9a1e09049ee4fc45837cc974a5500a61cccb15aa8afc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=68a2e4251b84210bdbc5570c3185d80592c88bd5b0d22ee53a7949f3ce4a2ca8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=d14f10137728afee0fffbe6ab625bceda898249dcf6863f53e6afdc348c64ce7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=1ff9f12287a5597c3df23d113821fc9fb336ed8149105d07607c7d10333a4189&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECHF4ID%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFUuJtDTYHS7LZzaXLlPWPro98w5Go04XfnkqzfWzQ%2BcAiEAx75rhRhc%2BP%2FSc3fGyJUothcF8oad84tEMw0WxOlqTswq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDJiEipcMQyRlGFVCBCrcAyDGApqlqT4eJg%2Bni7oSjXJh3pxaYVqUp7SQYEXf95DObjfs1KsqCJHCPLTJYylJpkIiUWBuryQnRSFgMqXtagN9wzNOm8oqutjLy2MlNDet9W5KKJmtXcxayTJG7wI3YxOSzV8Q1J2Fvca73kGvEb9QHkUUXrucAtBZpEiFIFt7m0AHrtBNsrqRqmMVVqsfkpzF%2B6Tz5UpxfFePbdRzo7qUCXGcgQFTw5SOd6rgZhvkFVek8b4aI6n27vBE7LkulCm2%2FtSUhouo4uWxKj%2Bes8lWjMELFhV53ntmgyAN%2FQQFOzKBNpr20pUUppp32CrHVYH6mlXwR37vHMsmSP%2ByAlZeFrNxZwFM6MIZJBzTqybNlVg17FiFbmljCS0q%2BBZV8PXKe7UilKJFbm8xt8uLC%2FU56nMu55GI88BquYzofaCbGemcNfsErQ1w1Vs6F%2FxhTVbryn83vnGdpAL9hylgl1KoEYG%2BqD%2BRtEm9eBYwG7%2BeZ6%2FPLN08Hw7Ff9jSxDTDvBavsVf8LDqNJ6Jh2sITtO1wyTzBANYcl3VVb%2B84GkYnrNHbWi7fUI%2BvW%2BuGl245bupVSQ4b7mg%2FBzrYO2rTztMdMAD9UazU8%2F0YC0Dtl6jYAmuRH23Pt9yOEhyeMLSNg70GOqUBmGFlyfUaU1AtfgaO6Nkmv%2BvEAW8ch139KkWEezYLeGWQ%2FtVeki9D47n%2FHeMK%2FJlvXHNrdlLe7EHx6qyUpjmbVOOJx5Oyegts3ixWklOMRf80OMkDoEZ%2BNBfwPTSFb%2Bu5kiW5xjdNm3sSd9tEA%2BTexJSEaFhxEAtx8eCz59x3721t1huVoCH3J%2Fr8TQ0ztWBy0H5fl5LOcmhpLoGZ%2FDBe6ApjRDnI&X-Amz-Signature=6326eefd21f1da3f2da4ca62f42da64c1891b4fc5500944bf170d14655912c28&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECHF4ID%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFUuJtDTYHS7LZzaXLlPWPro98w5Go04XfnkqzfWzQ%2BcAiEAx75rhRhc%2BP%2FSc3fGyJUothcF8oad84tEMw0WxOlqTswq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDJiEipcMQyRlGFVCBCrcAyDGApqlqT4eJg%2Bni7oSjXJh3pxaYVqUp7SQYEXf95DObjfs1KsqCJHCPLTJYylJpkIiUWBuryQnRSFgMqXtagN9wzNOm8oqutjLy2MlNDet9W5KKJmtXcxayTJG7wI3YxOSzV8Q1J2Fvca73kGvEb9QHkUUXrucAtBZpEiFIFt7m0AHrtBNsrqRqmMVVqsfkpzF%2B6Tz5UpxfFePbdRzo7qUCXGcgQFTw5SOd6rgZhvkFVek8b4aI6n27vBE7LkulCm2%2FtSUhouo4uWxKj%2Bes8lWjMELFhV53ntmgyAN%2FQQFOzKBNpr20pUUppp32CrHVYH6mlXwR37vHMsmSP%2ByAlZeFrNxZwFM6MIZJBzTqybNlVg17FiFbmljCS0q%2BBZV8PXKe7UilKJFbm8xt8uLC%2FU56nMu55GI88BquYzofaCbGemcNfsErQ1w1Vs6F%2FxhTVbryn83vnGdpAL9hylgl1KoEYG%2BqD%2BRtEm9eBYwG7%2BeZ6%2FPLN08Hw7Ff9jSxDTDvBavsVf8LDqNJ6Jh2sITtO1wyTzBANYcl3VVb%2B84GkYnrNHbWi7fUI%2BvW%2BuGl245bupVSQ4b7mg%2FBzrYO2rTztMdMAD9UazU8%2F0YC0Dtl6jYAmuRH23Pt9yOEhyeMLSNg70GOqUBmGFlyfUaU1AtfgaO6Nkmv%2BvEAW8ch139KkWEezYLeGWQ%2FtVeki9D47n%2FHeMK%2FJlvXHNrdlLe7EHx6qyUpjmbVOOJx5Oyegts3ixWklOMRf80OMkDoEZ%2BNBfwPTSFb%2Bu5kiW5xjdNm3sSd9tEA%2BTexJSEaFhxEAtx8eCz59x3721t1huVoCH3J%2Fr8TQ0ztWBy0H5fl5LOcmhpLoGZ%2FDBe6ApjRDnI&X-Amz-Signature=263b7dc4704c1599253b9053f7d5c619ae6def368badc331402584038a9660c4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECHF4ID%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFUuJtDTYHS7LZzaXLlPWPro98w5Go04XfnkqzfWzQ%2BcAiEAx75rhRhc%2BP%2FSc3fGyJUothcF8oad84tEMw0WxOlqTswq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDJiEipcMQyRlGFVCBCrcAyDGApqlqT4eJg%2Bni7oSjXJh3pxaYVqUp7SQYEXf95DObjfs1KsqCJHCPLTJYylJpkIiUWBuryQnRSFgMqXtagN9wzNOm8oqutjLy2MlNDet9W5KKJmtXcxayTJG7wI3YxOSzV8Q1J2Fvca73kGvEb9QHkUUXrucAtBZpEiFIFt7m0AHrtBNsrqRqmMVVqsfkpzF%2B6Tz5UpxfFePbdRzo7qUCXGcgQFTw5SOd6rgZhvkFVek8b4aI6n27vBE7LkulCm2%2FtSUhouo4uWxKj%2Bes8lWjMELFhV53ntmgyAN%2FQQFOzKBNpr20pUUppp32CrHVYH6mlXwR37vHMsmSP%2ByAlZeFrNxZwFM6MIZJBzTqybNlVg17FiFbmljCS0q%2BBZV8PXKe7UilKJFbm8xt8uLC%2FU56nMu55GI88BquYzofaCbGemcNfsErQ1w1Vs6F%2FxhTVbryn83vnGdpAL9hylgl1KoEYG%2BqD%2BRtEm9eBYwG7%2BeZ6%2FPLN08Hw7Ff9jSxDTDvBavsVf8LDqNJ6Jh2sITtO1wyTzBANYcl3VVb%2B84GkYnrNHbWi7fUI%2BvW%2BuGl245bupVSQ4b7mg%2FBzrYO2rTztMdMAD9UazU8%2F0YC0Dtl6jYAmuRH23Pt9yOEhyeMLSNg70GOqUBmGFlyfUaU1AtfgaO6Nkmv%2BvEAW8ch139KkWEezYLeGWQ%2FtVeki9D47n%2FHeMK%2FJlvXHNrdlLe7EHx6qyUpjmbVOOJx5Oyegts3ixWklOMRf80OMkDoEZ%2BNBfwPTSFb%2Bu5kiW5xjdNm3sSd9tEA%2BTexJSEaFhxEAtx8eCz59x3721t1huVoCH3J%2Fr8TQ0ztWBy0H5fl5LOcmhpLoGZ%2FDBe6ApjRDnI&X-Amz-Signature=444654d47c15ab6776599c2bf513b59d1d9f632fdb5e9cb894af6aba1342305f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=410c3ffcdf11a30aca9a8b93f0d4ed2a748625edbb93641e92b05eddc99ab011&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Calculating R-squared Values**
7. Create an empty list to store R^2 values.
8. Create a list of different polynomial orders.
9. Iterate through the list using a loop:
	- Create a polynomial feature object with the order as a parameter.
	- Transform the training and test data into polynomial features using the `fit_transform` method.
	- Fit the regression model using the transformed data.
	- Calculate the R^2 value using the test data and store it in the list.
Here's an example of how you can implement this in Python:
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# Store R^2 values
r2_values = []

# List of polynomial orders
orders = [1, 2, 3, 4]

# Iterate through polynomial orders
for order in orders:
    # Create polynomial features
    poly = PolynomialFeatures(degree=order)
    x_poly = poly.fit_transform(x.reshape(-1, 1))

    # Fit the model
    model = LinearRegression()
    model.fit(x_poly, y)

    # Predict and calculate R^2
    y_pred = model.predict(x_poly)
    r2 = r2_score(y, y_pred)
    r2_values.append(r2)

# Plot R^2 values
plt.plot(orders, r2_values, marker='o')
plt.xlabel('Order of Polynomial')
plt.ylabel('R^2 Value')
plt.title('R^2 Value vs. Polynomial Order')
plt.show()
```
Output:
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=f228796e60a69819885e200035f5010e90946df96096a85d6773286da2ef2dce&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=45f277d79ae3b01fcb3b6226c57cee41e1d39596bddb8aa48612693c0cc55eaf&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=311147dcb5b568f17fb474adebc5322928025be0f77c0607f150e9a73c463032&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=da5e66ac547e8a285a233c5495ba0d80280b10e785fbe50e0afd2586d3d1593f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2VFASFN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET9I4q%2BQoyBFN%2Fchshd1tC1JwUrNbSgA2TrYKfrUvWrAiAHRJ%2BobqJddCBvLNrp8ye%2FMrq7KoHnYvPIxWY%2FmUWd6Sr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMAItu4EEdNOvwIYieKtwD5fSQ6DnBXv4ivXUJsruAi7aNMIc493BZvgChE7RAzGBgJZTSm6s080q022Xw%2F7PIFmIKy7TjXdaYor%2ByPD3aA3%2B8T0lqhOw4mpvSLdqKjN1H9kr8BsyGyfcEsBrlta%2BkgL6DjWS2XvCLW1LMLkBXyYdbc5pGFG%2FFCBqia005IE7eWqjaLlBDpVVoj8h6HN7svUtKxpIV1%2BmTpbkgRV1VE4kriG4ldqUB%2FAn%2FEuAaFH0RsLOPoKD5fLWS0RFHpZeYhz6SHgKqvRW9t4GGOdGAEZgAbnhi4T1NB2ln3mSa0xAYw8xvKUvLKtXVG4ZVHrgZrVJAC4TKR49QiRoR7RCU05W2cwLcaLOOKppeH%2BE2aE6Qzu7YZVuAUcRNQzkX1WA1RRJjP0B1Owkxn5x5Rmfgm6HwYfcMw2%2BSETbGFSXA7g4Xr%2F8cM%2F4BFFd13B6STJk8bxMHyLAY2BoNNhORwhfQfyTbP1cKpLoWOsK2KrSHmTkYbX7eUPH%2BKmX8AjBx1FxBeQcIuC9m2g2rSA6I1WqkjPBbam2eUuMCBXR8vgrkhX1EsD4owAbUp%2Fodqvfdp1tleCZ6ZOZYpMVQhE3K7GVY3waOGlOMN2SsVeYKO8ZFPGK27X%2BN%2FdtfF5UF1scw9o2DvQY6pgFzjLwACSCWAlM2BgsGWpIVwqD0L5CZK5w%2Bq4UD0Jb%2FYge%2B%2BH2nJBN3DxHZfULU4A0kILH4rxA1EjGo2rnd01qOW8QIqsntjeXsYX2KmNK9v1ZMSlHnEC1m%2BWOVBLjmX5b32xqxpr%2BiH6ds8CJQ7sv0dEAzmQV1%2FoVxS9dPLI%2BGuSdIfz9hZGxk9KsS64%2BrlOhE%2FN304yMZT8djXDkkhiGlgKgePOWo&X-Amz-Signature=c83afd5cf1cbe0b43a99d7411c64b4fed7ab9b143d4076f8412177142e2f4289&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662EEMYG5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwvtd4V8lN0QLQRaF5y1VdKcj6Zgav0M6FP6wO2lcy4gIhAKi%2FWdURhD6NRcri7tmPY5ynXOTUuyEUqhaoRLjrZTKbKv8DCBcQABoMNjM3NDIzMTgzODA1Igxse%2Fs%2Fob8CPlvYdusq3AMP97pNplt%2BtuF%2Fg1q0NYmdt4b3LBCVSz2pUobQWhdVXP4J%2Fu0QgBdxHsCrdNDBst52HgojePul4jSgpqZqoOFFGgYxlCWmXXXWZNnx93gZ76ojSzA7gdJ3Vx8k5eYjAMNjCUqXJOhtCSNWpAQbP98wrVgFuET26aj6wSzNSduLoaqED8V43MNtt0Me5AFZ4mAh8D0I7602WstLfmHD21XG5LF01xruGmqWfiUGKrFhTjGxYUAheXR7kL7oUsCn5F8H7l2kU3u%2B57Yyp%2Bhw9Noxa6gMPkxp1D5gS%2FtBIGS2Xdjx2SzORA98R1E9OgQargnRdteZ78DGoVEj4E5CRY%2BkqrlwK12jHVvzbBSbJTr1MGwsDEcUHOgik9s1%2BrYx%2FWo1FSJgBagnD5vTZoOz4PVGKWI4tS8oT7pLfpZ%2B8vgp2kB0F1Ni1d%2FSfccpuW30s%2FjRyj%2Bt9IcwnQPg4k5O9FWDUXbZWeD%2FmOE2UBfVzHICdvfbAl3sSuiPgIsY%2FVyG4anyluGBPSL3ZjhXQE4fsIeNcbsqiqbjTKa8ZzkYsuL2QrVvOEd2L%2FZ6RxDfQ0PGHZvxTZ8p5IeB%2FTIa%2B89RcQslCG%2FM%2FFk6vLXU55hGD2l3X0fqGyyb%2BY%2BbFZzIzDCUjoO9BjqkAXOfUav%2BMzwKGEq21vaVMFGWsh782n%2BPH8ijsAhqOH3zND%2BLebSFl0rAjYk%2F4gnNqi81cf3fbacuX69DM62hUSUwnol2BetxhFNBNj4yJl6jTm375p2F%2FNrYzpIUZakYUZfQq56zWdtBUZY5RNjfm8ck%2B4ssVImXNDj2oiXIMFp1GVmvVfwFV7Ei8OaMJ0dXRG38A%2BtJKD3LZPOow0anysjts%2BNI&X-Amz-Signature=a35bcaf1a5130359252211dec87c89a27b611fa4d56cc2de8454907c2ba54bf7&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662EEMYG5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwvtd4V8lN0QLQRaF5y1VdKcj6Zgav0M6FP6wO2lcy4gIhAKi%2FWdURhD6NRcri7tmPY5ynXOTUuyEUqhaoRLjrZTKbKv8DCBcQABoMNjM3NDIzMTgzODA1Igxse%2Fs%2Fob8CPlvYdusq3AMP97pNplt%2BtuF%2Fg1q0NYmdt4b3LBCVSz2pUobQWhdVXP4J%2Fu0QgBdxHsCrdNDBst52HgojePul4jSgpqZqoOFFGgYxlCWmXXXWZNnx93gZ76ojSzA7gdJ3Vx8k5eYjAMNjCUqXJOhtCSNWpAQbP98wrVgFuET26aj6wSzNSduLoaqED8V43MNtt0Me5AFZ4mAh8D0I7602WstLfmHD21XG5LF01xruGmqWfiUGKrFhTjGxYUAheXR7kL7oUsCn5F8H7l2kU3u%2B57Yyp%2Bhw9Noxa6gMPkxp1D5gS%2FtBIGS2Xdjx2SzORA98R1E9OgQargnRdteZ78DGoVEj4E5CRY%2BkqrlwK12jHVvzbBSbJTr1MGwsDEcUHOgik9s1%2BrYx%2FWo1FSJgBagnD5vTZoOz4PVGKWI4tS8oT7pLfpZ%2B8vgp2kB0F1Ni1d%2FSfccpuW30s%2FjRyj%2Bt9IcwnQPg4k5O9FWDUXbZWeD%2FmOE2UBfVzHICdvfbAl3sSuiPgIsY%2FVyG4anyluGBPSL3ZjhXQE4fsIeNcbsqiqbjTKa8ZzkYsuL2QrVvOEd2L%2FZ6RxDfQ0PGHZvxTZ8p5IeB%2FTIa%2B89RcQslCG%2FM%2FFk6vLXU55hGD2l3X0fqGyyb%2BY%2BbFZzIzDCUjoO9BjqkAXOfUav%2BMzwKGEq21vaVMFGWsh782n%2BPH8ijsAhqOH3zND%2BLebSFl0rAjYk%2F4gnNqi81cf3fbacuX69DM62hUSUwnol2BetxhFNBNj4yJl6jTm375p2F%2FNrYzpIUZakYUZfQq56zWdtBUZY5RNjfm8ck%2B4ssVImXNDj2oiXIMFp1GVmvVfwFV7Ei8OaMJ0dXRG38A%2BtJKD3LZPOow0anysjts%2BNI&X-Amz-Signature=9d906642af284b328de1c9c8db03dfd375180578e64e7a5e277f7871d64bab54&X-Amz-SignedHeaders=host&x-id=GetObject)
12. **Model Training**:
	- **Procedure**: Use cross-validation to select the optimal Alpha. Split the data into training and validation sets.
	- **Steps**:
		1. **Train Model**: Fit the model using different values of Alpha.
		2. **Predict & Evaluate**: Use validation data to make predictions and calculate the R^2 or other metrics.
		3. **Select Alpha**: Choose the Alpha that maximizes the R^2 on validation data.
13. **Implementation in Python**:
	- **Import**:
```python
from sklearn.linear_model import Ridge
```
	- **Create & Fit Model**:
```python
ridge = Ridge(alpha=1.0)  # Set the desired alpha value
ridge.fit(X_train, y_train)
```
	- **Predict**:
```python
y_pred = ridge.predict(X_test)
```
14. **Cross-Validation**:
	- **Purpose**: Used to determine the best Alpha by comparing performance metrics (e.g., R^2) across different Alpha values.
	- **Process**: Train with various Alpha values, evaluate with validation data, and select the best-performing Alpha.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCTTENFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA9dw0QKbdOtW34h7OQP%2BEKwDMFu%2Fs3Zl9C0qkggWoInAiEA9nTI4J9tZFi9NnZIz%2Bass7jZfb5qhHFcrKQOn14UW1gq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDNHyrBEDYNXH%2F7rFQircA2oVwOuAmZ87OwHzCx%2FYrJju8gyENGxt3UMfd%2ByhSZ0EtA1A7BQyZ%2FPO3Xh7dHM5Py58lqvbg5VD23E0mtIJgO0ndCHuWU7Dvgscj5MUVn%2B%2FFs50P5fIio10vh86lFbY71TQZcnQIPjLfSmjbDjmPoQOdwypS3CQSqdXaL70bbAjmcNLGaedRnQFDr9vVssJFooPy1XE6S5aC7Zs9fP6tSfFnjNGTHHGM8FzRmZYkgx3EqoT%2B3UiiW6OxczHamQ5bQVNbxv586LlqLL6JzXy7S3gwsZ6LM%2Btx3lLt0y51B8uSZ3TdAFj5oegaJaYARUalCAYL7UTDDXt4jpXfa%2F07tRwiVy4989UNcmhWqw9peJhtQvEKZ1eoKI1PXFV%2B%2BvV0IDzMWOyvPBKCVDQR68GSDZRI3Gko7r7woY7e4p57tSycODF1eK4stw5TlWZLU2mP0CJef6n%2BalLMJqTb0Mmteh69sreEYI6WJ94%2F9z9twRhSvKdzrbLlktXazDoLMD4HfqfrvIvx1ACMkMfQTFs9sYgrwUBQN3jEMCfPpOu8MafdNMh6qXdb9X2CpG3wMw80S3rxfx%2BMweomMNprGQ%2BCj9gc9VvS3eKQ1ebwr80sIWN4HJRpt6HeC4hPLFyMJSOg70GOqUBO5oHSua6Lacq304LIG4DtSY%2BkEsGauI5g0JHR4Bi1FcyS9mxIETHWBs1eEsEuJN%2BKVoxpXAN%2Fj1ttfAvrwI2hxS8IiYEKZ2PXLp6V7UunGXsf%2FrfAEFkHRnDlkdp5XnmcvXBoxk5KsvhiggwLmPy1EjD5iScoL0e%2B6IHHXTf997N3PSfX3ey8YiqCGWmYIXMA9F7Pqgip9t5nAv027HySBXwcFPx&X-Amz-Signature=028e89e87d09f7ff71fdfe54c1cb5bcf9890fe7088f9a2d540bd0ebd739eefa1&X-Amz-SignedHeaders=host&x-id=GetObject)
15. **Example Visualization**:
	- **Plot**: Shows R^2 values vs. different Alpha values for training and validation data.
	- **Interpretation**:
		- **Training Data**: R^2 might increase with Alpha but eventually converge.
		- **Validation Data**: R^2 may decrease with high Alpha due to reduced model flexibility.
___
## Grid Search for Hyperparameter Tuning
### **Grid Search**
A method for finding the best hyperparameters for a model by systematically evaluating different combinations.
- **Hyperparameters**: Values like Alpha in Ridge Regression that are not learned from the data but set before the training process.
- **Process**:
	1. **Define Hyperparameters**: Set up a grid of hyperparameter values to test. For Ridge Regression, this might include values for Alpha and normalization options.
	2. **Train and Evaluate**: Train the model using each combination of hyperparameters. Evaluate each model using cross-validation, typically using metrics like R² or Mean Squared Error (MSE).
	3. **Select Best Parameters**: Choose the hyperparameters that give the best performance based on the evaluation metric.
### **Implementation in Scikit-learn**
```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25])

# Define parameter grid
param_grid = {
    'alpha': [0.1, 1, 10],
    'normalize': [True, False]
}

# Initialize Ridge model
ridge = Ridge()

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=ridge, param_grid=param_grid, scoring='r2', cv=5)

# Fit GridSearchCV
grid_search.fit(X, y)

# Get best parameters
best_params = grid_search.best_params_
best_score = grid_search.best_score_
best_estimator = grid_search.best_estimator_
cv_results = grid_search.cv_results_

# Results
print("Best Parameters:", best_params)
print("Best Score:", best_score)
print("Best Estimator:", best_estimator)
print("CV Results:", cv_results)
```
**Example Result:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODW4AK3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1EGrsPJQXL%2BIzZIHJrp%2BMQiXzerZVUKaloD%2BSUKry8AiEA10kKSCkcFyG5VcFzGH588tCx7n99DkYifZSSjkvFSn4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDjo01CEd4KZ33hvOSrcA01v3Odfom7m7qRFjnr5LECTnO21cEpW%2FYbslsG%2FWYghstmGoXJs48eh8AeFJnLzVlfqE7hW5zwpoHGMxu6o5mf2bQsNwrlmi2asDAcCc%2Fmr%2F7pRvFM4%2BDfljCzEpHj%2BIraYijzYjkDYi%2Bhgptz%2Bg3Vk5KVfEDptwv75XMLuryqSZh10q6r7LTcyrPa%2FuGVwJFrjiSrLHVaZFomPtMSOQfcINJvDQBgJ1Lck8DzelDQRCYeDvASp%2BfwB0BJIdQlmIJCksGAeCIcz%2BgyhKI2Ymf1GnrbTg%2FGj6NCOkqhVxCQHEqWKFfkPqN%2B4xHhuqgT4rS8Wyi83YihbEgXQLBPyZe6LpfkQr3TeI7e%2FM2ZXfIPg2VF2CRIcn14bEApGazmNhDQbv%2FIC1pfsy8dNTNIExCv5RjdfaBdMurSoDyRQObShiJEOLmTcun01eXztYPNo5tEH6EdSJPlc1iHtYHr43GlwwIYJ1O1%2BMdKhlzMnc340JgR%2BjXdTiyUtY14RCSlz6Y%2FgPu9LgkiVjW0Q0v5zOAeUAmt1Qz1wNDvyhjndjATr15yzN4so04o0T6LGV39oBrhVCFHSpPGF73DfrnQmSePv4CG35WpowM%2B8D3CGQjUTDoVELpza5A7LUcbFMKiNg70GOqUBv4fEe1%2FUQ6EOUy5b30BSB82IVyyMQvduToaevkg0o6iusfViJuUzwr3bPCGMGfk8M%2Flfmob2jvzCBBXgRU81%2BdqMaVM8LjJL12JrHfdtUardXk%2BwSUxK7PnhPoObQ%2FbojuARoPlYdc0ekTU8KmE7uzGBLgNf6waECUJ3KRM9GO2sS04uHRWpX9Vq0K2QCVLKK6DOMp8w1VgpEX2ewyV6TXnimocs&X-Amz-Signature=6166a7802fc47e492690ccc05e1c67add3dde71242b03c3a7d1235b306c5f5f1&X-Amz-SignedHeaders=host&x-id=GetObject)
- **Key Attributes**:
	- `**best_estimator_**`: Best model found.
	- `**cv_results_**`: Detailed results for each hyperparameter combination, including scores and parameters.
- **Advantages**: Efficiently explores multiple hyperparameter values to find the best combination, reducing the manual effort required for model tuning.
___
## Cheat Sheet: Model Evaluation and Refinement
### Splitting Data for Training and Testing
The process involves separating the target attribute from the rest of the data, treating it as the output, and the rest as input. Then, split these into training and testing subsets.
```python
from sklearn.model_selection import train_test_split

# Define target and features
y_data = df['target_attribute']
x_data = df.drop('target_attribute', axis=1)

# Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)
```
### Cross Validation Score
Cross-validation involves creating multiple subsets of training and testing data to evaluate the model’s performance using the R² value.
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Initialize the model
lre = LinearRegression()

# Perform cross-validation
Rcross = cross_val_score(lre, x_data[['attribute_1']], y_data, cv=n)

# Calculate mean and standard deviation of scores
Mean = Rcross.mean()
Std_dev = Rcross.std()
```
### Cross Validation Prediction
Generate predictions using a cross-validated model.
```python
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression

# Initialize the model
lre = LinearRegression()

# Perform cross-validation prediction
yhat = cross_val_predict(lre, x_data[['attribute_1']], y_data, cv=4)
```
### Ridge Regression and Prediction
Use Ridge regression to create a model that avoids overfitting by adjusting the alpha parameter and making predictions.
```python
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures

# Initialize polynomial features
pr = PolynomialFeatures(degree=2)

# Transform features
x_train_pr = pr.fit_transform(x_train[['attribute_1', 'attribute_2']])
x_test_pr = pr.transform(x_test[['attribute_1', 'attribute_2']])

# Initialize Ridge model
RigeModel = Ridge(alpha=1)

# Fit the model
RigeModel.fit(x_train_pr, y_train)

# Make predictions
yhat = RigeModel.predict(x_test_pr)
```
### Grid Search
Use Grid Search to find the optimal alpha value for Ridge regression by performing cross-validation.
```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

# Define parameter grid
parameters = [{'alpha': [0.001, 0.1, 1, 10, 100, 1000, 10000]}]

# Initialize Ridge model
RR = Ridge()

# Initialize GridSearchCV
Grid1 = GridSearchCV(RR, parameters, cv=4)

# Fit GridSearchCV
Grid1.fit(x_data[['attribute_1', 'attribute_2']], y_data)

# Get the best model
BestRR = Grid1.best_estimator_

# Evaluate the model
score = BestRR.score(x_test[['attribute_1', 'attribute_2']], y_test)
```
___