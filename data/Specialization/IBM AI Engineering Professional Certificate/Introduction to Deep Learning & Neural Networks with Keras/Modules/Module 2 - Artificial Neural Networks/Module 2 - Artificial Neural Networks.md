

# Module 2: Artificial Neural Networks
## Gradient Descent and Optimization in Neural Networks
### Introduction
In this section, we will discuss the concept of gradient descent, a fundamental algorithm used for optimizing weights and biases in neural networks. Understanding gradient descent is crucial before diving into the mechanics of how neural networks learn through backpropagation. 
### Understanding the Problem
Suppose we have a dataset where $ z  $ is twice the value of $ x $. Our goal is to find the optimal weight $ w $ that generates a line best fitting this data. To achieve this, we define a cost or loss function, denoted as $ J $.
#### Cost Function
The cost function measures the difference between the actual values of $ z  $ and the values predicted by the model, i.e., $ wx $. It is given by:
$$ J(w) = \sum_{i=1}^{n} \left( z_i - w \cdot x_i \right)^2 $$
The objective is to find the value of $ w $ that minimizes this cost function, leading to the best fit line for the data.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bd20068e-2350-4c53-ba35-db137540515b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011038Z&X-Amz-Expires=3600&X-Amz-Signature=b64610716cde4eefef275ecd871961cee26684b01b1f45246390b0d9b21dde1e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example: Simple Linear Data
For simplicity, consider the case where $ z=2x $. The optimal value of $ w  $ that minimizes the cost function is $ w=2 $, as it perfectly fits the line $ z=2x $.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ce186573-efd7-45c0-81e8-d88b278d76c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011038Z&X-Amz-Expires=3600&X-Amz-Signature=ca5ffec1b4f38c3be61ffa82a384a80abd40b4c297ee40c42cc1dd8eeabc2593&X-Amz-SignedHeaders=host&x-id=GetObject)
### Introduction to Gradient Descent
Gradient descent is an iterative optimization algorithm used to find the minimum value of a function. It is particularly useful for minimizing the cost function in neural networks.
#### How Gradient Descent Works
1. **Initialization**: Start with a random initial value of $ w $, denoted as $ w_0 $.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3a4b2b9f-74fe-40ea-bd5f-b6da8e8a1b53/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011038Z&X-Amz-Expires=3600&X-Amz-Signature=e4a69d844279174e3dbfc30177ef82886b2a09a94995a6ca0e02bd929727bd2d&X-Amz-SignedHeaders=host&x-id=GetObject)
2. **Compute the Gradient**: Calculate the gradient (slope OR derivative) of the cost function at the current value of $ w $. The gradient indicates the direction in which the cost function is increasing.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8bba6cc9-bbcb-4ba7-a8b7-d5c36ae63437/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011038Z&X-Amz-Expires=3600&X-Amz-Signature=e5586e30f728834d69fc5674d64fdac056facef4c93f4e6c35a0755b70b94cbf&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Update Rule**: Adjust the value of $ w  $ by moving in the direction opposite to the gradient. This is done using the formula:
$$ w_{i+1} = w_i - \alpha \cdot \text{gradient}(J(w_i)) $$
Here, $ \alpha $ is the learning rate, controlling the step size.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/42a2d642-6adb-46de-883a-9c979db13be1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011038Z&X-Amz-Expires=3600&X-Amz-Signature=602eb78b9f28ce714a2b6309e2a50c1fe781602acb9f9b4344c48353ee3016b3&X-Amz-SignedHeaders=host&x-id=GetObject)
4. **Iteration**: Repeat the process until the algorithm converges to the minimum value of the cost function or a value close to it.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/045d3977-5b07-4e2d-a476-fe683b0708a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011038Z&X-Amz-Expires=3600&X-Amz-Signature=ea25a2f2aa45c196e2996e6958dc19f0ebf4aee9c87addc16d420f8f3dd44060&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Choosing the Learning Rate
- **Large Learning Rate**: Can cause the algorithm to overshoot the minimum, leading to divergence.
- **Small Learning Rate**: Can result in slow convergence, making the algorithm take a long time to reach the minimum.
#### Example with Iterations
Assume we start with $ w_0=0.2  $ and use a learning rate $ \alpha = 0.4 $:
- **1st Iteration**: $ w_1  $ moves closer to the optimal value $ w=2 $, causing a significant drop in the cost function.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2ec0fa27-9d1b-46d9-9353-5593db897df3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011038Z&X-Amz-Expires=3600&X-Amz-Signature=cdb751bcc3d120dd676d4dd25311d74d40ca07d78868c88b897ff18da33be617&X-Amz-SignedHeaders=host&x-id=GetObject)
- **2nd Iteration**: $ w_2  $ continues to move towards $ w=2 $, with a smaller step as the slope decreases.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3162cdb0-ddff-47b5-ada6-d09807f482dd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011038Z&X-Amz-Expires=3600&X-Amz-Signature=02cf6d4d1a46dde04a3b8042f48e57dd1ba4a20bfc9d9e873b94d3129c17e469&X-Amz-SignedHeaders=host&x-id=GetObject)
- **Subsequent Iterations**: The steps become smaller as the algorithm approaches the minimum, with the cost function value decreasing steadily.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff65aa88-841b-4a86-8b66-352055ba85a8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011038Z&X-Amz-Expires=3600&X-Amz-Signature=4692ea73d4567fb29802722cd9e772cb5d4d017878bd1330f20a4bd3dac2087f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Application in Neural Networks
In neural networks, gradient descent is used to optimize multiple weights and biases simultaneously. The algorithm updates each parameter in a way that minimizes the overall cost function, which measures how well the network's predictions match the actual data.
#### Forward Propagation and Gradient Descent
During training, neural networks use forward propagation to calculate the output and then apply gradient descent to adjust the weights and biases, improving the network's performance over time.
### Summary
Gradient descent is a powerful optimization algorithm that iteratively adjusts parameters to minimize a cost function. By understanding how to apply gradient descent to a simple linear problem, we are now equipped to explore more complex scenarios, such as optimizing weights in neural networks using backpropagation.
___
## Gradient Descent and Backpropagation in Neural Networks
#### Training Overview
Neural networks are trained using a supervised learning approach, where each data point has a corresponding label or ground truth. The goal of training is to minimize the difference (error) between the predicted value by the network and the ground truth. This error is calculated and then propagated back into the network to adjust the weights and biases.
#### Error Calculation and Cost Function
- **Error (E):** The error represents the cost or loss function. It measures how far the network's prediction is from the actual value.
- **Squared Error:** For a single neuron, the error is computed as the squared difference between the predicted value $ a_2  $ and the ground truth $ T $:
$$ E = \frac{1}{2} \sum (T - a_2)^2 $$
- In real-world scenarios, the network is trained using large datasets, and the error is calculated as the **Mean Squared Error (MSE)**.
#### Gradient Descent for Optimization
To minimize the error, gradient descent is used. It iteratively updates the weights and biases in the network:
5. **Starting Point:** Begin with random initial weights and biases.
6. **Gradient Calculation:** Compute the gradient (slope) of the cost function with respect to each weight and bias using calculus. This shows how much the error will change if we slightly change the weights or biases.
7. **Update Rule:** The weights and biases are updated using the formula:
$$ w_{\text{new}} = w_{\text{old}} - \text{learning rate} \times \text{gradient} $$
        The learning rate controls how big a step we take towards the minimum of the cost function.
#### Backpropagation
Backpropagation is the method used to calculate the gradients of the error with respect to the weights and biases. It applies the chain rule of calculus to compute how the error propagates back through the network:
- **Derivative Calculation:** Derivatives are taken at each layer to determine how the error affects the weights in that layer.
- **Weight Update:** Weights are adjusted by computing the gradient for each weight and applying the gradient descent rule.
#### Example with One Input and Two Neurons
Consider a network with two neurons:
- **Forward Propagation:** Compute the weighted sums $ z_1, z_2, $ and the outputs $ a_1, a_2 $.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a695635c-0446-4714-a226-718ac9577549/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011039Z&X-Amz-Expires=3600&X-Amz-Signature=4fe125e8d2e4fe51e95dbc26f81d90144f78cae768f7accef8bd7e4b22bcc063&X-Amz-SignedHeaders=host&x-id=GetObject)
- **Backpropagation:** If the ground truth is known (e.g., 0.25), the error between the prediction and ground truth is calculated. The weights and biases are then updated using the gradients and a learning rate of 0.4.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd5117c8-af5b-46ec-857b-f6ad4622631f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011039Z&X-Amz-Expires=3600&X-Amz-Signature=dc10038cbaa6b4d8de9d283e40201f72484946efe6894e7c97d8af6bca481c02&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Weight Update Equations
For the second neuron:
- **Derivative of Error (E) with Respect to Weight **$ w_2 $**:**
$$ \frac{\partial E}{\partial w_2} = -(T - a_2) \times a_2 \times (1 - a_2) \times a_1 $$
- **Update Rule for Weight **$ w_2 $**:**
$$ w_2 = w_2 - \text{learning rate} \times \frac{\partial E}{\partial w_2} $$
Similarly, the biases are updated using the derivatives with respect to the biases.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3ed6542e-ad49-481c-bce8-115e2cb8faf9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011039Z&X-Amz-Expires=3600&X-Amz-Signature=cbabea13a0c8b66766aaccac73cbae6e447ed82eee4be515f05090d2294ec6ae&X-Amz-SignedHeaders=host&x-id=GetObject)
[NaQwXc72EemgrQ4z3gANog_5cdaec1e385342c1a8095e8b6c3eb7ad_Partial_Derivatives_Backpropagation.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/038b0865-3aac-462b-bab6-083877527b3b/NaQwXc72EemgrQ4z3gANog_5cdaec1e385342c1a8095e8b6c3eb7ad_Partial_Derivatives_Backpropagation.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011039Z&X-Amz-Expires=3600&X-Amz-Signature=569ccb84ef0368fcae08d96304757f7a2239614df6829dc15a99c0723664892e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Iterative Training Process
Training involves repeatedly performing the following steps until the error is minimized:
8. **Forward Propagation:** Calculate the network output.
9. **Error Calculation:** Compute the error between the prediction and ground truth.
10. **Backpropagation:** Calculate gradients for each weight and bias using the chain rule.
11. **Update Weights and Biases:** Adjust parameters to reduce the error.
This process continues over multiple iterations or epochs until the error is sufficiently small or the maximum number of iterations is reached.
___
## Vanishing Gradient Problem in Neural Networks
### Overview
The **vanishing gradient problem** is a significant issue associated with using the sigmoid activation function in neural networks. It affects the training efficiency and prediction accuracy of the network.
### Problem Description
- **Sigmoid Activation Function**: The sigmoid function maps input values to a range between 0 and 1. While this can be useful, it leads to problems during backpropagation.
- **Gradients in Backpropagation**: During backpropagation, the gradients of the error with respect to the weights are computed. For the sigmoid function, the gradient (derivative) of the activation function is always between 0 and 1. This causes the gradients to become very small as they are propagated backward through the network.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1300f8d7-31e2-4054-a375-dd0677d27731/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011039Z&X-Amz-Expires=3600&X-Amz-Signature=961deea8b22bc011de3ffe5e7d58874fbd33ab0fc2a7820492367aa92417aece&X-Amz-SignedHeaders=host&x-id=GetObject)
- **Effect on Learning**: In a neural network with multiple layers, gradients of weights in earlier layers become very small. This results in:
	- **Slow Learning**: Neurons in earlier layers learn very slowly compared to neurons in later layers.
	- **Long Training Time**: Training takes significantly longer.
	- **Compromised Accuracy**: The prediction accuracy of the network may be affected due to inefficient learning in earlier layers.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/5eeb41c8-279a-4556-a186-f41c06da54f6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011038Z&X-Amz-Expires=3600&X-Amz-Signature=6b9cd3ddb52d63e039bb4396f471ed3d61991d628185d1c57c6ca1b7906aa035&X-Amz-SignedHeaders=host&x-id=GetObject)
### Mathematical Insight
When using the sigmoid function, the derivatives of the activation function can be very small. During backpropagation, the gradient of the error with respect to the weights is calculated as a product of these derivatives. Thus, gradients tend to diminish as they propagate backward through the network:
$$ \text{Gradient} = \frac{\partial E}{\partial w_i} = \frac{\partial E}{\partial a_n} \cdot \frac{\partial a_n}{\partial z_n} \cdot \frac{\partial z_n}{\partial w_i} $$
where:
- $ \frac{\partial E}{\partial a_n} $ is the gradient of the error with respect to the output $ a_n $.
- $ \frac{\partial a_n}{\partial z_n} $ is the gradient of the sigmoid function, which is small.
- $ \frac{\partial z_n}{\partial w_i} $ depends on the inputs.
### Conclusion
Due to the vanishing gradient problem, sigmoid functions and similar activation functions are not ideal for deep networks. This problem has led to the development and use of alternative activation functions that mitigate this issue.
### Next Steps
In the following notes, alternative activation functions that address the vanishing gradient problem will be introduced. These functions are commonly used in hidden layers of modern neural networks to improve training efficiency and accuracy.
___
## Activation Functions in Neural Networks
### Types of Activation Functions
There are 7 types of most common activation functions:
12. **Sigmoid Function**
13. **Hyperbolic Tangent (tanh) Function**
14. **Rectified Linear Unit (ReLU) Function**
15. **Softmax Function**
16. **Binary Step Function**
17. **Linear Function**
18. **Leaky ReLU**
*Additional Note:* 5-6-7 are not popular functions.
### Introduction
Activation functions are crucial for the learning process of neural networks. They introduce non-linearity into the model, allowing it to learn complex patterns. While the sigmoid function was commonly used in the past, it has notable shortcomings, such as the vanishing gradient problem. This note explores several activation functions and their applications.
### 1. Sigmoid Function
#### Formula
$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$
#### Range
$$ (0, 1) $$
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/20bb4bb6-02a5-4a68-8fe0-6a70da31ed6a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011039Z&X-Amz-Expires=3600&X-Amz-Signature=22b855cd45474a494c3d6a876799eea12609a5a8a80d10b23bdda350c3b3cd0a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Characteristics
- Outputs values between 0 and 1.
- Gradients become very small in the regions where $ z $ is very large or very small, leading to the vanishing gradient problem.
- Not symmetric around the origin; all outputs are positive.
#### Applications
Previously popular, but avoided in deep networks due to vanishing gradients.
### 2. Hyperbolic Tangent (tanh) Function
#### Formula
$$ \tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}} $$
#### Range
$$ (-1, 1) $$
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/db2f9c8f-51aa-4db6-aa8c-3855d0b93b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011039Z&X-Amz-Expires=3600&X-Amz-Signature=e2ce794e28fba64fcbf02e7435f2d7b2192ceca066fbcd713716765e5c5f43c9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Characteristics
- Similar to the sigmoid function but symmetric around the origin.
- Gradients can still become very small in deep networks, leading to the vanishing gradient problem.
#### Applications
Used in some applications but also limited by vanishing gradients in very deep networks.
### 3. Rectified Linear Unit (ReLU) Function
#### Formula
$$ \text{ReLU}(z) = \max(0, z) $$
#### Range
$$ [ 0, \infty) $$
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/5d06c921-b0fd-40ec-b681-15be7e883d76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011039Z&X-Amz-Expires=3600&X-Amz-Signature=c9160343456a14578209c0248a2d129ba99eb8895f361a5eb10392b7fb7c612d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Characteristics
- Non-linear activation function that only activates neurons with positive input values.
- Helps overcome the vanishing gradient problem by ensuring that gradients are not zero for positive inputs.
- Results in sparse activation where only a few neurons are activated at a time.
#### Applications
Widely used in hidden layers of deep networks due to its efficiency and effectiveness.
### 4. Softmax Function
#### Formula
$$ \text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j} e^{z_j}} $$
#### Range
$$ (0, 1) \text{ (sums to 1 across the output layer)} $$
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7df121d3-29b2-4c62-801d-b1a78e0a433c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241030T011039Z&X-Amz-Expires=3600&X-Amz-Signature=17a64943f16a8e9b5ff6bda0fddfc4e08c955d83efeaf7e99e30614bb59caa14&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Characteristics
- Converts raw output scores into probabilities that sum to 1.
- Useful for classification tasks where we need to determine the probability of each class.
#### Applications
Commonly used in the output layer of classification networks to handle multi-class problems..
### Conclusion
- **Sigmoid and tanh Functions**: Avoided in many modern applications due to the vanishing gradient problem.
- **ReLU Function**: Preferred activation function in hidden layers of deep networks due to its effectiveness and ability to mitigate vanishing gradients.
- **Softmax Function**: Useful for classification tasks to provide class probabilities.
This concludes the overview of activation functions. For deep learning applications, start with ReLU and consider other functions if necessary based on performance.
___
