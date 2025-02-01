

# Module 4: Deep Learning Models
## Deep Neural Networks: An Introduction
### Overview
Neural networks have evolved significantly over time, transitioning from shallow networks to deep neural networks (DNNs) that handle complex tasks and data types. This note explores the distinctions between shallow and deep neural networks, and the reasons behind the recent advancements in deep learning.
### Shallow vs. Deep Neural Networks
#### Shallow Neural Networks
- **Definition**: A shallow neural network typically has only one hidden layer.
- **Characteristics**:
	- Simpler architectures
	- Limited ability to extract features from raw data
	- Often used for simpler tasks or as building blocks for deeper networks
#### Deep Neural Networks
- **Definition**: A deep neural network has multiple hidden layers and neurons.
- **Characteristics**:
	- Capable of learning hierarchical features from raw data such as images and text
	- Ability to extract features from raw data.
	- Handles more complex tasks and datasets
	- Example: Image recognition, natural language processing
### Factors Contributing to the Rise of Deep Learning
#### 1. Advancements in Neural Network Techniques
- **ReLU Activation Function**:
	- Addressed the vanishing gradient problem
	- Enabled the training of very deep networks
#### 2. Availability of Data
- **Importance**:
	- Deep neural networks excel with large datasets
	- Large data helps prevent overfitting
- **Current Trends**:
	- Access to vast amounts of data has become easier
	- Deep learning algorithms benefit significantly from increased data
#### 3. Computational Power
- **GPU Utilization**:
	- NVIDIA GPUs and other high-performance computing resources
	- Reduced training times from weeks to hours
- **Impact**:
	- Enables experimentation with different network architectures and prototypes in shorter periods
### Conclusion
The combination of advancements in neural network techniques, the availability of large datasets, and increased computational power has driven the recent boom in deep learning. The field continues to evolve, with deep neural networks becoming increasingly prevalent in various applications. Upcoming topics will delve into supervised deep learning algorithms and convolutional neural networks (CNNs).
___
## Introduction to Convolutional Neural Networks (CNNs) (Supervised Deep Learning Model)
### Overview
Convolutional Neural Networks (CNNs) are a specialized type of neural network designed for processing structured grid data such as images. This note covers the fundamental architecture of CNNs, their operational mechanisms, and how to build them using the Keras library.
#### Convolutional Neural Networks (CNNs)
### Architecture
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646CWTTQS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHubaHk3sSu3D1BEmGRcVwPKDC3KBX2J8C%2FiIWIVkQv0AiAv96cTG%2F341wUm4AXAVSn%2FjT%2BdZIdxIyHJsiiSKGwcRyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHxBINtzL0YsyhZUKtwDW5U9QA6CNJJmhgf2LYRptXUx0EZHWRADpKYUC5kDIk5f9AyESkR%2FZGuOxGMVAgzH2hSTyyDcHu%2FForjqlQKR5LfG4Asu%2BNKvz9Op2YS39abSb4NVuv74m6TTZIyEihkguw08NjM1nYBfUNQGa%2Btm%2BgtRb7PUOn50lg%2FodQRb1qCq9C18w1rfZMVB6XXiOwCPFR18teqkDCz4m62c7S4cM19vIEgm27JDGqVdLKBQejqodFhs3gBa1vcGcxklVxDzktQ7GtGiHH5AZ1oBIlZNzZtiau%2BBmcaVOsbhyzrfVYiDFxt%2BPvFWHo%2BpzfG7EvOOt7gEVmC%2FnM3Wv2vPJ9m1tQ5xz%2FkJRLiHk%2FXYSg7UgDVhIiogGnaCMoj3GGEffxj97%2BkWXApcRsU0vUUMKfHLQ7A7GU5j%2Bfv6T%2B6ntVpoI9%2B%2BB6VEO1JWiQHwYLcy43Oyv%2BJxPwT8i%2F2C1R1vIeJXaY2R22id5egWY8TJQ4oUc01RBiwG3ZZzWpmME0z%2FUeZ9Vl7hwi79%2FuN7uV%2FhRJOda5VKgPs6V4fWlKuk2KhObSZRJA7JHnlUpp8mPfJWItOXxNiz%2BUIbijEtRY5Ywtz7IfXL2k%2B%2F6QKjtSJUYxtbESJXW%2FyS4DUJdM%2BIpT0wvcH2vAY6pgHbc1hVrFQqO%2B6ibM913AliTLORdsrwk%2B5HrzYjCoiMmPA%2BuZcMNGSJEVe6P9CkPD7PWGVRghsGfkpzQxbr5kqPLpmumfe8l18dMBKcaT%2FNooGtuI9A1D0b4gyMpOFxQXiUOTSJ%2BQVrRqNCAoGthQETWrIrbHN65glcyDVZZQiUlQ6OISmsj4Yp0p6XpP%2FnccD8IzUrj1LR7njx%2BrWxnIBtztDcxPeN&X-Amz-Signature=a14d198277c07fb06fd1c37983ebbe633049a94bd14fcf7a9b1aebb693769b83&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646CWTTQS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHubaHk3sSu3D1BEmGRcVwPKDC3KBX2J8C%2FiIWIVkQv0AiAv96cTG%2F341wUm4AXAVSn%2FjT%2BdZIdxIyHJsiiSKGwcRyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHxBINtzL0YsyhZUKtwDW5U9QA6CNJJmhgf2LYRptXUx0EZHWRADpKYUC5kDIk5f9AyESkR%2FZGuOxGMVAgzH2hSTyyDcHu%2FForjqlQKR5LfG4Asu%2BNKvz9Op2YS39abSb4NVuv74m6TTZIyEihkguw08NjM1nYBfUNQGa%2Btm%2BgtRb7PUOn50lg%2FodQRb1qCq9C18w1rfZMVB6XXiOwCPFR18teqkDCz4m62c7S4cM19vIEgm27JDGqVdLKBQejqodFhs3gBa1vcGcxklVxDzktQ7GtGiHH5AZ1oBIlZNzZtiau%2BBmcaVOsbhyzrfVYiDFxt%2BPvFWHo%2BpzfG7EvOOt7gEVmC%2FnM3Wv2vPJ9m1tQ5xz%2FkJRLiHk%2FXYSg7UgDVhIiogGnaCMoj3GGEffxj97%2BkWXApcRsU0vUUMKfHLQ7A7GU5j%2Bfv6T%2B6ntVpoI9%2B%2BB6VEO1JWiQHwYLcy43Oyv%2BJxPwT8i%2F2C1R1vIeJXaY2R22id5egWY8TJQ4oUc01RBiwG3ZZzWpmME0z%2FUeZ9Vl7hwi79%2FuN7uV%2FhRJOda5VKgPs6V4fWlKuk2KhObSZRJA7JHnlUpp8mPfJWItOXxNiz%2BUIbijEtRY5Ywtz7IfXL2k%2B%2F6QKjtSJUYxtbESJXW%2FyS4DUJdM%2BIpT0wvcH2vAY6pgHbc1hVrFQqO%2B6ibM913AliTLORdsrwk%2B5HrzYjCoiMmPA%2BuZcMNGSJEVe6P9CkPD7PWGVRghsGfkpzQxbr5kqPLpmumfe8l18dMBKcaT%2FNooGtuI9A1D0b4gyMpOFxQXiUOTSJ%2BQVrRqNCAoGthQETWrIrbHN65glcyDVZZQiUlQ6OISmsj4Yp0p6XpP%2FnccD8IzUrj1LR7njx%2BrWxnIBtztDcxPeN&X-Amz-Signature=ea12058027573225a4e4fdf3f5f726dae637481559ce3f0640f85cba94805786&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646CWTTQS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHubaHk3sSu3D1BEmGRcVwPKDC3KBX2J8C%2FiIWIVkQv0AiAv96cTG%2F341wUm4AXAVSn%2FjT%2BdZIdxIyHJsiiSKGwcRyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHxBINtzL0YsyhZUKtwDW5U9QA6CNJJmhgf2LYRptXUx0EZHWRADpKYUC5kDIk5f9AyESkR%2FZGuOxGMVAgzH2hSTyyDcHu%2FForjqlQKR5LfG4Asu%2BNKvz9Op2YS39abSb4NVuv74m6TTZIyEihkguw08NjM1nYBfUNQGa%2Btm%2BgtRb7PUOn50lg%2FodQRb1qCq9C18w1rfZMVB6XXiOwCPFR18teqkDCz4m62c7S4cM19vIEgm27JDGqVdLKBQejqodFhs3gBa1vcGcxklVxDzktQ7GtGiHH5AZ1oBIlZNzZtiau%2BBmcaVOsbhyzrfVYiDFxt%2BPvFWHo%2BpzfG7EvOOt7gEVmC%2FnM3Wv2vPJ9m1tQ5xz%2FkJRLiHk%2FXYSg7UgDVhIiogGnaCMoj3GGEffxj97%2BkWXApcRsU0vUUMKfHLQ7A7GU5j%2Bfv6T%2B6ntVpoI9%2B%2BB6VEO1JWiQHwYLcy43Oyv%2BJxPwT8i%2F2C1R1vIeJXaY2R22id5egWY8TJQ4oUc01RBiwG3ZZzWpmME0z%2FUeZ9Vl7hwi79%2FuN7uV%2FhRJOda5VKgPs6V4fWlKuk2KhObSZRJA7JHnlUpp8mPfJWItOXxNiz%2BUIbijEtRY5Ywtz7IfXL2k%2B%2F6QKjtSJUYxtbESJXW%2FyS4DUJdM%2BIpT0wvcH2vAY6pgHbc1hVrFQqO%2B6ibM913AliTLORdsrwk%2B5HrzYjCoiMmPA%2BuZcMNGSJEVe6P9CkPD7PWGVRghsGfkpzQxbr5kqPLpmumfe8l18dMBKcaT%2FNooGtuI9A1D0b4gyMpOFxQXiUOTSJ%2BQVrRqNCAoGthQETWrIrbHN65glcyDVZZQiUlQ6OISmsj4Yp0p6XpP%2FnccD8IzUrj1LR7njx%2BrWxnIBtztDcxPeN&X-Amz-Signature=22399e3d86116a3b6d85e5472fe04c2ede75bc24419f70d9d5fd8c210f1ff9a6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646CWTTQS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHubaHk3sSu3D1BEmGRcVwPKDC3KBX2J8C%2FiIWIVkQv0AiAv96cTG%2F341wUm4AXAVSn%2FjT%2BdZIdxIyHJsiiSKGwcRyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHxBINtzL0YsyhZUKtwDW5U9QA6CNJJmhgf2LYRptXUx0EZHWRADpKYUC5kDIk5f9AyESkR%2FZGuOxGMVAgzH2hSTyyDcHu%2FForjqlQKR5LfG4Asu%2BNKvz9Op2YS39abSb4NVuv74m6TTZIyEihkguw08NjM1nYBfUNQGa%2Btm%2BgtRb7PUOn50lg%2FodQRb1qCq9C18w1rfZMVB6XXiOwCPFR18teqkDCz4m62c7S4cM19vIEgm27JDGqVdLKBQejqodFhs3gBa1vcGcxklVxDzktQ7GtGiHH5AZ1oBIlZNzZtiau%2BBmcaVOsbhyzrfVYiDFxt%2BPvFWHo%2BpzfG7EvOOt7gEVmC%2FnM3Wv2vPJ9m1tQ5xz%2FkJRLiHk%2FXYSg7UgDVhIiogGnaCMoj3GGEffxj97%2BkWXApcRsU0vUUMKfHLQ7A7GU5j%2Bfv6T%2B6ntVpoI9%2B%2BB6VEO1JWiQHwYLcy43Oyv%2BJxPwT8i%2F2C1R1vIeJXaY2R22id5egWY8TJQ4oUc01RBiwG3ZZzWpmME0z%2FUeZ9Vl7hwi79%2FuN7uV%2FhRJOda5VKgPs6V4fWlKuk2KhObSZRJA7JHnlUpp8mPfJWItOXxNiz%2BUIbijEtRY5Ywtz7IfXL2k%2B%2F6QKjtSJUYxtbESJXW%2FyS4DUJdM%2BIpT0wvcH2vAY6pgHbc1hVrFQqO%2B6ibM913AliTLORdsrwk%2B5HrzYjCoiMmPA%2BuZcMNGSJEVe6P9CkPD7PWGVRghsGfkpzQxbr5kqPLpmumfe8l18dMBKcaT%2FNooGtuI9A1D0b4gyMpOFxQXiUOTSJ%2BQVrRqNCAoGthQETWrIrbHN65glcyDVZZQiUlQ6OISmsj4Yp0p6XpP%2FnccD8IzUrj1LR7njx%2BrWxnIBtztDcxPeN&X-Amz-Signature=251669b9155c54acec60c640a3e33be979790c0349859500b2596ab94d53e895&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646CWTTQS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHubaHk3sSu3D1BEmGRcVwPKDC3KBX2J8C%2FiIWIVkQv0AiAv96cTG%2F341wUm4AXAVSn%2FjT%2BdZIdxIyHJsiiSKGwcRyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHxBINtzL0YsyhZUKtwDW5U9QA6CNJJmhgf2LYRptXUx0EZHWRADpKYUC5kDIk5f9AyESkR%2FZGuOxGMVAgzH2hSTyyDcHu%2FForjqlQKR5LfG4Asu%2BNKvz9Op2YS39abSb4NVuv74m6TTZIyEihkguw08NjM1nYBfUNQGa%2Btm%2BgtRb7PUOn50lg%2FodQRb1qCq9C18w1rfZMVB6XXiOwCPFR18teqkDCz4m62c7S4cM19vIEgm27JDGqVdLKBQejqodFhs3gBa1vcGcxklVxDzktQ7GtGiHH5AZ1oBIlZNzZtiau%2BBmcaVOsbhyzrfVYiDFxt%2BPvFWHo%2BpzfG7EvOOt7gEVmC%2FnM3Wv2vPJ9m1tQ5xz%2FkJRLiHk%2FXYSg7UgDVhIiogGnaCMoj3GGEffxj97%2BkWXApcRsU0vUUMKfHLQ7A7GU5j%2Bfv6T%2B6ntVpoI9%2B%2BB6VEO1JWiQHwYLcy43Oyv%2BJxPwT8i%2F2C1R1vIeJXaY2R22id5egWY8TJQ4oUc01RBiwG3ZZzWpmME0z%2FUeZ9Vl7hwi79%2FuN7uV%2FhRJOda5VKgPs6V4fWlKuk2KhObSZRJA7JHnlUpp8mPfJWItOXxNiz%2BUIbijEtRY5Ywtz7IfXL2k%2B%2F6QKjtSJUYxtbESJXW%2FyS4DUJdM%2BIpT0wvcH2vAY6pgHbc1hVrFQqO%2B6ibM913AliTLORdsrwk%2B5HrzYjCoiMmPA%2BuZcMNGSJEVe6P9CkPD7PWGVRghsGfkpzQxbr5kqPLpmumfe8l18dMBKcaT%2FNooGtuI9A1D0b4gyMpOFxQXiUOTSJ%2BQVrRqNCAoGthQETWrIrbHN65glcyDVZZQiUlQ6OISmsj4Yp0p6XpP%2FnccD8IzUrj1LR7njx%2BrWxnIBtztDcxPeN&X-Amz-Signature=34bd128fc676127740703c75f5f6ff9a2e5044e25e097dd304d93d04995354d4&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646CWTTQS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHubaHk3sSu3D1BEmGRcVwPKDC3KBX2J8C%2FiIWIVkQv0AiAv96cTG%2F341wUm4AXAVSn%2FjT%2BdZIdxIyHJsiiSKGwcRyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHxBINtzL0YsyhZUKtwDW5U9QA6CNJJmhgf2LYRptXUx0EZHWRADpKYUC5kDIk5f9AyESkR%2FZGuOxGMVAgzH2hSTyyDcHu%2FForjqlQKR5LfG4Asu%2BNKvz9Op2YS39abSb4NVuv74m6TTZIyEihkguw08NjM1nYBfUNQGa%2Btm%2BgtRb7PUOn50lg%2FodQRb1qCq9C18w1rfZMVB6XXiOwCPFR18teqkDCz4m62c7S4cM19vIEgm27JDGqVdLKBQejqodFhs3gBa1vcGcxklVxDzktQ7GtGiHH5AZ1oBIlZNzZtiau%2BBmcaVOsbhyzrfVYiDFxt%2BPvFWHo%2BpzfG7EvOOt7gEVmC%2FnM3Wv2vPJ9m1tQ5xz%2FkJRLiHk%2FXYSg7UgDVhIiogGnaCMoj3GGEffxj97%2BkWXApcRsU0vUUMKfHLQ7A7GU5j%2Bfv6T%2B6ntVpoI9%2B%2BB6VEO1JWiQHwYLcy43Oyv%2BJxPwT8i%2F2C1R1vIeJXaY2R22id5egWY8TJQ4oUc01RBiwG3ZZzWpmME0z%2FUeZ9Vl7hwi79%2FuN7uV%2FhRJOda5VKgPs6V4fWlKuk2KhObSZRJA7JHnlUpp8mPfJWItOXxNiz%2BUIbijEtRY5Ywtz7IfXL2k%2B%2F6QKjtSJUYxtbESJXW%2FyS4DUJdM%2BIpT0wvcH2vAY6pgHbc1hVrFQqO%2B6ibM913AliTLORdsrwk%2B5HrzYjCoiMmPA%2BuZcMNGSJEVe6P9CkPD7PWGVRghsGfkpzQxbr5kqPLpmumfe8l18dMBKcaT%2FNooGtuI9A1D0b4gyMpOFxQXiUOTSJ%2BQVrRqNCAoGthQETWrIrbHN65glcyDVZZQiUlQ6OISmsj4Yp0p6XpP%2FnccD8IzUrj1LR7njx%2BrWxnIBtztDcxPeN&X-Amz-Signature=3dc6052d89f9a4c673d5e6ce0362f9506a05aa9cf3234187339efeeedb890bc5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646CWTTQS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHubaHk3sSu3D1BEmGRcVwPKDC3KBX2J8C%2FiIWIVkQv0AiAv96cTG%2F341wUm4AXAVSn%2FjT%2BdZIdxIyHJsiiSKGwcRyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHxBINtzL0YsyhZUKtwDW5U9QA6CNJJmhgf2LYRptXUx0EZHWRADpKYUC5kDIk5f9AyESkR%2FZGuOxGMVAgzH2hSTyyDcHu%2FForjqlQKR5LfG4Asu%2BNKvz9Op2YS39abSb4NVuv74m6TTZIyEihkguw08NjM1nYBfUNQGa%2Btm%2BgtRb7PUOn50lg%2FodQRb1qCq9C18w1rfZMVB6XXiOwCPFR18teqkDCz4m62c7S4cM19vIEgm27JDGqVdLKBQejqodFhs3gBa1vcGcxklVxDzktQ7GtGiHH5AZ1oBIlZNzZtiau%2BBmcaVOsbhyzrfVYiDFxt%2BPvFWHo%2BpzfG7EvOOt7gEVmC%2FnM3Wv2vPJ9m1tQ5xz%2FkJRLiHk%2FXYSg7UgDVhIiogGnaCMoj3GGEffxj97%2BkWXApcRsU0vUUMKfHLQ7A7GU5j%2Bfv6T%2B6ntVpoI9%2B%2BB6VEO1JWiQHwYLcy43Oyv%2BJxPwT8i%2F2C1R1vIeJXaY2R22id5egWY8TJQ4oUc01RBiwG3ZZzWpmME0z%2FUeZ9Vl7hwi79%2FuN7uV%2FhRJOda5VKgPs6V4fWlKuk2KhObSZRJA7JHnlUpp8mPfJWItOXxNiz%2BUIbijEtRY5Ywtz7IfXL2k%2B%2F6QKjtSJUYxtbESJXW%2FyS4DUJdM%2BIpT0wvcH2vAY6pgHbc1hVrFQqO%2B6ibM913AliTLORdsrwk%2B5HrzYjCoiMmPA%2BuZcMNGSJEVe6P9CkPD7PWGVRghsGfkpzQxbr5kqPLpmumfe8l18dMBKcaT%2FNooGtuI9A1D0b4gyMpOFxQXiUOTSJ%2BQVrRqNCAoGthQETWrIrbHN65glcyDVZZQiUlQ6OISmsj4Yp0p6XpP%2FnccD8IzUrj1LR7njx%2BrWxnIBtztDcxPeN&X-Amz-Signature=f414635eb91a7e288302c81dcfd18bd5678f9c037d036db4dcb3d7726b4d687d&X-Amz-SignedHeaders=host&x-id=GetObject)
### CNN Architecture
- **Input Layer**: Defines the size of the input images (e.g., 128 x 128 x 3 for color images).
- **Convolutional Layers**: Apply multiple filters and include ReLU activation.
- **Pooling Layers**: Apply max-pooling or average-pooling.
- **Fully Connected Layers**: Flatten the data and produce output based on the number of classes.
- **Output Layer**: Produces the final class probabilities using the softmax activation function.
### Summary
- **Efficiency**: CNNs reduce the number of parameters compared to traditional neural networks, making them computationally efficient.
- **Applications**: Ideal for tasks involving image recognition, object detection, and other computer vision problems.
### Building CNNs with Keras
1. **Model Creation**:
	- Use the `Sequential` model to build the CNN.
2. **Defining Input Shape**:
	- For 128x128 color images: `input_shape=(128, 128, 3)`
3. **Adding Layers**:
	- **Convolutional Layer**:
```python
model.add(Conv2D(16, (2, 2), strides=(1, 1), activation='relu', input_shape=(128, 128, 3)))
```
		- **Parameters**:
			- `16`: Number of filters or kernels.
			- `(2, 2)`: Size of each filter.
			- `strides=(1, 1)`: The step size with which the filter moves across the image.
			- `activation='relu'`: Activation function applied after the convolution operation.
			- `input_shape=(128, 128, 3)`: Shape of the input images. For color images, the last dimension is 3 (RGB channels).
	- **Pooling Layer**:
```python
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
```
		- **Parameters**:
			- `pool_size=(2, 2)`: Size of the pooling window.
			- `strides=(2, 2)`: The step size with which the pooling window moves across the image.
	- **Additional Convolutional and Pooling Layers**:
```python
model.add(Conv2D(32, (2, 2), strides=(1, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
```
		- **Parameters**:
			- `32`: Number of filters or kernels in this convolutional layer.
			- `(2, 2)`: Size of each filter.
			- `strides=(1, 1)`: The step size with which the filter moves across the image.
			- `activation='relu'`: Activation function applied after the convolution operation.
			- `pool_size=(2, 2)`: Size of the pooling window.
			- `strides=(2, 2)`: The step size with which the pooling window moves across the image.
4. **Flattening and Fully Connected Layers**:
	- **Flatten**: Converts 3D feature maps into 1D.
```python
model.add(Flatten())
```
	- **Dense Layers**:
```python
model.add(Dense(100, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
```
		- **Parameters**:
			- `100`: Number of neurons in the dense layer.
			- `activation='relu'`: Activation function applied to the neurons in the dense layer.
			- `num_classes`: Number of output neurons, typically equal to the number of classes in the classification problem.
			- `activation='softmax'`: Activation function applied to the output layer to convert raw scores into probabilities.
5. **Compilation**:
	- Define optimizer, loss function, and metrics:
```python
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```
		- **Parameters**:
			- `optimizer='adam'`: Optimization algorithm used for training.
			- `loss='categorical_crossentropy'`: Loss function used for classification tasks with multiple classes.
			- `metrics=['accuracy']`: Evaluation metric used to measure the performance of the model.
6. **Training and Validation**:
	- Train the model using the `fit` method and validate using a test set.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646CWTTQS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHubaHk3sSu3D1BEmGRcVwPKDC3KBX2J8C%2FiIWIVkQv0AiAv96cTG%2F341wUm4AXAVSn%2FjT%2BdZIdxIyHJsiiSKGwcRyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHxBINtzL0YsyhZUKtwDW5U9QA6CNJJmhgf2LYRptXUx0EZHWRADpKYUC5kDIk5f9AyESkR%2FZGuOxGMVAgzH2hSTyyDcHu%2FForjqlQKR5LfG4Asu%2BNKvz9Op2YS39abSb4NVuv74m6TTZIyEihkguw08NjM1nYBfUNQGa%2Btm%2BgtRb7PUOn50lg%2FodQRb1qCq9C18w1rfZMVB6XXiOwCPFR18teqkDCz4m62c7S4cM19vIEgm27JDGqVdLKBQejqodFhs3gBa1vcGcxklVxDzktQ7GtGiHH5AZ1oBIlZNzZtiau%2BBmcaVOsbhyzrfVYiDFxt%2BPvFWHo%2BpzfG7EvOOt7gEVmC%2FnM3Wv2vPJ9m1tQ5xz%2FkJRLiHk%2FXYSg7UgDVhIiogGnaCMoj3GGEffxj97%2BkWXApcRsU0vUUMKfHLQ7A7GU5j%2Bfv6T%2B6ntVpoI9%2B%2BB6VEO1JWiQHwYLcy43Oyv%2BJxPwT8i%2F2C1R1vIeJXaY2R22id5egWY8TJQ4oUc01RBiwG3ZZzWpmME0z%2FUeZ9Vl7hwi79%2FuN7uV%2FhRJOda5VKgPs6V4fWlKuk2KhObSZRJA7JHnlUpp8mPfJWItOXxNiz%2BUIbijEtRY5Ywtz7IfXL2k%2B%2F6QKjtSJUYxtbESJXW%2FyS4DUJdM%2BIpT0wvcH2vAY6pgHbc1hVrFQqO%2B6ibM913AliTLORdsrwk%2B5HrzYjCoiMmPA%2BuZcMNGSJEVe6P9CkPD7PWGVRghsGfkpzQxbr5kqPLpmumfe8l18dMBKcaT%2FNooGtuI9A1D0b4gyMpOFxQXiUOTSJ%2BQVrRqNCAoGthQETWrIrbHN65glcyDVZZQiUlQ6OISmsj4Yp0p6XpP%2FnccD8IzUrj1LR7njx%2BrWxnIBtztDcxPeN&X-Amz-Signature=3e46c442d61bf2332f45145e39c17b1de7c0e1992a17c66bf6a0a8a13492f30f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Conclusion
CNNs are powerful for image processing tasks due to their ability to automatically extract and learn features from images. The architecture involves convolutional, activation, pooling, and fully connected layers, which collectively enable the network to perform tasks such as image recognition and object detection.
___
## Recurrent Neural Networks (RNNs) Overview (Unsupervised Deep Learning Model)
### Introduction to RNNs
- **Purpose**: RNNs are used to analyze sequences where data points are not independent but rather follow a temporal or sequential relationship.
- **Architecture**: RNNs include loops that allow them to take both the current input and the output from the previous data point into account.
### How RNNs Work
- **Input and Output at Each Time Step**:
	- At time `t = 0`, the network takes in input $ x_0 $ and outputs $ a_0 $.
	- At time `t = 1`, the network takes in input $ x_1 $` `and the previous output $ a_0 $, weighted by $ w_{1,2} $.
	- This process continues, incorporating previous outputs into the computation at each step.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646CWTTQS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHubaHk3sSu3D1BEmGRcVwPKDC3KBX2J8C%2FiIWIVkQv0AiAv96cTG%2F341wUm4AXAVSn%2FjT%2BdZIdxIyHJsiiSKGwcRyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHxBINtzL0YsyhZUKtwDW5U9QA6CNJJmhgf2LYRptXUx0EZHWRADpKYUC5kDIk5f9AyESkR%2FZGuOxGMVAgzH2hSTyyDcHu%2FForjqlQKR5LfG4Asu%2BNKvz9Op2YS39abSb4NVuv74m6TTZIyEihkguw08NjM1nYBfUNQGa%2Btm%2BgtRb7PUOn50lg%2FodQRb1qCq9C18w1rfZMVB6XXiOwCPFR18teqkDCz4m62c7S4cM19vIEgm27JDGqVdLKBQejqodFhs3gBa1vcGcxklVxDzktQ7GtGiHH5AZ1oBIlZNzZtiau%2BBmcaVOsbhyzrfVYiDFxt%2BPvFWHo%2BpzfG7EvOOt7gEVmC%2FnM3Wv2vPJ9m1tQ5xz%2FkJRLiHk%2FXYSg7UgDVhIiogGnaCMoj3GGEffxj97%2BkWXApcRsU0vUUMKfHLQ7A7GU5j%2Bfv6T%2B6ntVpoI9%2B%2BB6VEO1JWiQHwYLcy43Oyv%2BJxPwT8i%2F2C1R1vIeJXaY2R22id5egWY8TJQ4oUc01RBiwG3ZZzWpmME0z%2FUeZ9Vl7hwi79%2FuN7uV%2FhRJOda5VKgPs6V4fWlKuk2KhObSZRJA7JHnlUpp8mPfJWItOXxNiz%2BUIbijEtRY5Ywtz7IfXL2k%2B%2F6QKjtSJUYxtbESJXW%2FyS4DUJdM%2BIpT0wvcH2vAY6pgHbc1hVrFQqO%2B6ibM913AliTLORdsrwk%2B5HrzYjCoiMmPA%2BuZcMNGSJEVe6P9CkPD7PWGVRghsGfkpzQxbr5kqPLpmumfe8l18dMBKcaT%2FNooGtuI9A1D0b4gyMpOFxQXiUOTSJ%2BQVrRqNCAoGthQETWrIrbHN65glcyDVZZQiUlQ6OISmsj4Yp0p6XpP%2FnccD8IzUrj1LR7njx%2BrWxnIBtztDcxPeN&X-Amz-Signature=b034532480e398b5c5b8590209acb50993bace17f02399d8650b50536dcb8004&X-Amz-SignedHeaders=host&x-id=GetObject)
### Applications of RNNs
- **Text Analysis**: Suitable for processing and modeling sequential text data.
- **Genomic Data**: Can analyze sequences in genetic information.
- **Handwriting**: Applied in handwriting generation and recognition.
- **Stock Markets**: Used for predicting stock prices based on historical data.
### Long Short-Term Memory (LSTM) Networks
- **Overview**: A specialized type of RNN designed to overcome some limitations of traditional RNNs.
- **Applications**:
	- **Image Generation**: Models trained on images to generate novel images.
	- **Handwriting Generation**: Creating handwritten text based on trained models.
	- **Image Description**: Automatically describing images.
	- **Video Streams**: Analyzing and describing video sequences.
### Summary
- **RNNs**: Effective for tasks involving sequences and temporal data.
- **LSTM Models**: A specific type of RNN that handles long-term dependencies and is used in advanced applications like image and video analysis.
___
### Autoencoders and Restricted Boltzmann Machines (RBMs)
### Introduction to Autoencoders
- **Definition**: Autoencoders are unsupervised deep learning models used for data compression. They learn to compress and decompress data automatically through neural networks.
- **Purpose**: They aim to learn a compressed representation of the input data and then reconstruct the original data from this representation.
- **Training**: Autoencoders use backpropagation with the target variable being the same as the input, effectively learning an approximation of an identity function.
### Architecture of an Autoencoder
- **Encoder**:
	- Compresses the input data into a lower-dimensional representation.
- **Decoder**:
	- Reconstructs the original data from the compressed representation.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTSRDQ3A%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDiL5DbWAXSxHZGUjVWefF6ncSNu6VGKoKmgSmAQJAd3AiEAjHtJajhv43xWvinjKdNZQ6dMR1uNMldOB%2BAGwatzQA0qiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGeaz6auGd80PIcTtyrcAwepZ%2BcFYu87xtT6hFtzyX86KB19oFJ51cyVAczNOVRhTVo2fnCy41sQazlqsfH4HLGG3SWJtC0WML5mjx3WabP3YEmnHDA0t7SEbimgaBaNjcG35Ke88agESSVBoyueY2WU%2BVI7GvVlfwIf2beQwjebqVlK12kLf4HLxKKcZVUftkGvl0ZLwS%2F8e41rIYkvjambm7zJpey0gDfnO3haavPevyvEO2RotKAYjrBXxp%2BT26JSHX%2FDrLd%2FETF%2Bq9pRN3UCG0F4sNIVZpjmihiBQ4O2tNuciHDjTuyj%2FD6I%2BDXtxGHjXLY3eM9FJaKc4sUM07xumAqE4WntvIychKGhkk5vIGuVSD%2BSTXDvqKvWp7pBeXXWOJp9v%2Fn6EZnJIxKUaHjSsuQPPCd3iDBrLLba%2FgosIhUgoyZOUZHV%2F4mZiaVa3KFOWeiCxcAUeJgQ%2F%2FV8ZtyVC8ZtcAdH0ZkSSNej2YV6c8IHLW2DZ3VbgP43y452LmQRLwsNTymnvQyR4%2F%2BIFWFBdE2eGRBo3RtY6%2FsRxOFQVfzjiFsbVBhIZCx32bqgfJ2A43d8bQ5cP3ukZjTkaYxyRIiz1dIhhcHp5pPHArTZn4ORyTXAiIoxgnXXrTdki5cXPeRVDiniB8ASMNzB9rwGOqUBuTnwGSEFaTLzoUZEd8TorZxCe6Uf9u7vlXBA9IM7Bati8%2BMt0NNVdPmA%2BNyD%2FJSyySoWtsP6cnGHZarAt6FQ8TspzpJ02gFpzr%2FCXblej2VEEEl%2BuXXGM%2FfIxL%2FBidXzhZMiJCzBp1mTg5KpficHEO6F%2BxJH8p12E1bzhYM5z2I8dFqHEss10vxo5u116wgHBT%2BxUQw3akF9ncPIw4RvvkxACF8R&X-Amz-Signature=90caba3d3bf1adfb38ec28ce3a0e431e46f779034fe100a54c2bd2f52b044776&X-Amz-SignedHeaders=host&x-id=GetObject)
### Applications of Autoencoders
- **Data Denoising**: Removing noise from data to recover the original signal.
- **Dimensionality Reduction**: Reducing the number of features in the data for visualization purposes.
### Advantages over Traditional Methods
- **Non-Linear Transformations**: Autoencoders, with their non-linear activation functions, can learn more complex projections compared to linear methods like Principal Component Analysis (PCA).
### Restricted Boltzmann Machines (RBMs)
- **Overview**: RBMs are a type of autoencoder that can learn the distribution of the input data to perform tasks such as:
	- **Fixing Imbalanced Datasets**: Generating more data points for minority classes to balance datasets.
	- **Estimating Missing Values**: Predicting missing feature values in datasets.
	- **Automatic Feature Extraction**: Learning features from unstructured data.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTSRDQ3A%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDiL5DbWAXSxHZGUjVWefF6ncSNu6VGKoKmgSmAQJAd3AiEAjHtJajhv43xWvinjKdNZQ6dMR1uNMldOB%2BAGwatzQA0qiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGeaz6auGd80PIcTtyrcAwepZ%2BcFYu87xtT6hFtzyX86KB19oFJ51cyVAczNOVRhTVo2fnCy41sQazlqsfH4HLGG3SWJtC0WML5mjx3WabP3YEmnHDA0t7SEbimgaBaNjcG35Ke88agESSVBoyueY2WU%2BVI7GvVlfwIf2beQwjebqVlK12kLf4HLxKKcZVUftkGvl0ZLwS%2F8e41rIYkvjambm7zJpey0gDfnO3haavPevyvEO2RotKAYjrBXxp%2BT26JSHX%2FDrLd%2FETF%2Bq9pRN3UCG0F4sNIVZpjmihiBQ4O2tNuciHDjTuyj%2FD6I%2BDXtxGHjXLY3eM9FJaKc4sUM07xumAqE4WntvIychKGhkk5vIGuVSD%2BSTXDvqKvWp7pBeXXWOJp9v%2Fn6EZnJIxKUaHjSsuQPPCd3iDBrLLba%2FgosIhUgoyZOUZHV%2F4mZiaVa3KFOWeiCxcAUeJgQ%2F%2FV8ZtyVC8ZtcAdH0ZkSSNej2YV6c8IHLW2DZ3VbgP43y452LmQRLwsNTymnvQyR4%2F%2BIFWFBdE2eGRBo3RtY6%2FsRxOFQVfzjiFsbVBhIZCx32bqgfJ2A43d8bQ5cP3ukZjTkaYxyRIiz1dIhhcHp5pPHArTZn4ORyTXAiIoxgnXXrTdki5cXPeRVDiniB8ASMNzB9rwGOqUBuTnwGSEFaTLzoUZEd8TorZxCe6Uf9u7vlXBA9IM7Bati8%2BMt0NNVdPmA%2BNyD%2FJSyySoWtsP6cnGHZarAt6FQ8TspzpJ02gFpzr%2FCXblej2VEEEl%2BuXXGM%2FfIxL%2FBidXzhZMiJCzBp1mTg5KpficHEO6F%2BxJH8p12E1bzhYM5z2I8dFqHEss10vxo5u116wgHBT%2BxUQw3akF9ncPIw4RvvkxACF8R&X-Amz-Signature=b71f9ffeb91eddbff9ca6b572b043a30db9543a9c508a293be0a09e91b595675&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
