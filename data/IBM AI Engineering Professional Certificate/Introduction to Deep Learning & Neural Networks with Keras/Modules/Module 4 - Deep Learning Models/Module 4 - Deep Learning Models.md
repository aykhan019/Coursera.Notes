

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4ENKKOH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRysIzXncgx7Vn7eYulJK9gLk46UswS1tEStgmsmziNwIgI%2FvqlqULUc8NGBVBq44eRPjgDXr2guHKdS0H2yuDcBoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCkNaZ4%2Fbg7%2BwV0rircAwmiOMNO3MyREP4AzZzRigWOCDvyI5xIFnUF7GUJ5e1tQRMIMi8XL42FvtGtE7MjvP9FTEjEIi16cbWbwQydcE0H6ifMsX0QQYcAp35A%2B7MNdQbFEBY4XUntn0ivpD3TTToCb4zZu7Z72eDY44uqYZ1E0Aq6m8jNMHryo0CyyCu%2BGqL6ZzcMn%2BfdwMsyO6xozGB41hby%2F0yrP7gStowfb0aAssu3jDMGL4Pm0ZE3Oj4mU%2FIzb221AS4%2BWwSj6%2F0KUjKhc%2BLFdYxw%2B2M38f9L1OSeQQOF4egKrKPUpN6UZSA%2Bg%2BpyZj%2BSvV4GKtPJ%2F0Q%2Byhd0JT8wvv%2Bn1w8US49w%2BMOEo0Xuw%2B6Tw0LQwlweyDg61z%2BbeBzxh%2BSknjkJGC7wghiunw17HzKRmTfTBcVF4s53YUOfRs3bkGCZ9dgcLi4qmFNB0oTSXCfBawhmnWB5svXe2LUO5ZPC%2BH%2B91XDnM%2BCct%2FZnnxwsT5Pk7SbOtUcyTawJfCSNg3H8xbVU9XbKXVVi5yTx88WfCm67MSZ%2B%2FmJ0ovX9ZZ9N2s6rGuztTCaWI6F7GNOnbOEdB6pyL8rM7RSYCKmKSgcLYybYILXYcllaWGes41hWk1dyzCcs5hLXJgmreY3kA6zK6LgVMIjI%2BLwGOqUB0DyAYAZpudLxv%2B2KvXxFC7HAbFx9UG8t4dy817z01PaqDkrVXdqMOBGfEvJw8rB6Uf6pTsvFD%2BfgB2F693fcdkNtQlcY6taS8tosTjx7HGp%2Fw7pjJrdCAHpSSqJJehgIW4sDAYxk1%2BkHpPhGtK09dR0yodtosJPQaZ3m%2BrglBhg2VZWpBb9yCawRHkIuWcFqSFO6dtU02pNeml1XtK%2BBB%2FUrZi8a&X-Amz-Signature=b8b46eb627f3c0024b08f41bf2abd861a825a82a8aee2152a4798e5c009f03b9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4ENKKOH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRysIzXncgx7Vn7eYulJK9gLk46UswS1tEStgmsmziNwIgI%2FvqlqULUc8NGBVBq44eRPjgDXr2guHKdS0H2yuDcBoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCkNaZ4%2Fbg7%2BwV0rircAwmiOMNO3MyREP4AzZzRigWOCDvyI5xIFnUF7GUJ5e1tQRMIMi8XL42FvtGtE7MjvP9FTEjEIi16cbWbwQydcE0H6ifMsX0QQYcAp35A%2B7MNdQbFEBY4XUntn0ivpD3TTToCb4zZu7Z72eDY44uqYZ1E0Aq6m8jNMHryo0CyyCu%2BGqL6ZzcMn%2BfdwMsyO6xozGB41hby%2F0yrP7gStowfb0aAssu3jDMGL4Pm0ZE3Oj4mU%2FIzb221AS4%2BWwSj6%2F0KUjKhc%2BLFdYxw%2B2M38f9L1OSeQQOF4egKrKPUpN6UZSA%2Bg%2BpyZj%2BSvV4GKtPJ%2F0Q%2Byhd0JT8wvv%2Bn1w8US49w%2BMOEo0Xuw%2B6Tw0LQwlweyDg61z%2BbeBzxh%2BSknjkJGC7wghiunw17HzKRmTfTBcVF4s53YUOfRs3bkGCZ9dgcLi4qmFNB0oTSXCfBawhmnWB5svXe2LUO5ZPC%2BH%2B91XDnM%2BCct%2FZnnxwsT5Pk7SbOtUcyTawJfCSNg3H8xbVU9XbKXVVi5yTx88WfCm67MSZ%2B%2FmJ0ovX9ZZ9N2s6rGuztTCaWI6F7GNOnbOEdB6pyL8rM7RSYCKmKSgcLYybYILXYcllaWGes41hWk1dyzCcs5hLXJgmreY3kA6zK6LgVMIjI%2BLwGOqUB0DyAYAZpudLxv%2B2KvXxFC7HAbFx9UG8t4dy817z01PaqDkrVXdqMOBGfEvJw8rB6Uf6pTsvFD%2BfgB2F693fcdkNtQlcY6taS8tosTjx7HGp%2Fw7pjJrdCAHpSSqJJehgIW4sDAYxk1%2BkHpPhGtK09dR0yodtosJPQaZ3m%2BrglBhg2VZWpBb9yCawRHkIuWcFqSFO6dtU02pNeml1XtK%2BBB%2FUrZi8a&X-Amz-Signature=9a87699955d5ca79e04cb86363b1689a99767084b4a28700a73a74ab4de3a9c2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4ENKKOH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRysIzXncgx7Vn7eYulJK9gLk46UswS1tEStgmsmziNwIgI%2FvqlqULUc8NGBVBq44eRPjgDXr2guHKdS0H2yuDcBoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCkNaZ4%2Fbg7%2BwV0rircAwmiOMNO3MyREP4AzZzRigWOCDvyI5xIFnUF7GUJ5e1tQRMIMi8XL42FvtGtE7MjvP9FTEjEIi16cbWbwQydcE0H6ifMsX0QQYcAp35A%2B7MNdQbFEBY4XUntn0ivpD3TTToCb4zZu7Z72eDY44uqYZ1E0Aq6m8jNMHryo0CyyCu%2BGqL6ZzcMn%2BfdwMsyO6xozGB41hby%2F0yrP7gStowfb0aAssu3jDMGL4Pm0ZE3Oj4mU%2FIzb221AS4%2BWwSj6%2F0KUjKhc%2BLFdYxw%2B2M38f9L1OSeQQOF4egKrKPUpN6UZSA%2Bg%2BpyZj%2BSvV4GKtPJ%2F0Q%2Byhd0JT8wvv%2Bn1w8US49w%2BMOEo0Xuw%2B6Tw0LQwlweyDg61z%2BbeBzxh%2BSknjkJGC7wghiunw17HzKRmTfTBcVF4s53YUOfRs3bkGCZ9dgcLi4qmFNB0oTSXCfBawhmnWB5svXe2LUO5ZPC%2BH%2B91XDnM%2BCct%2FZnnxwsT5Pk7SbOtUcyTawJfCSNg3H8xbVU9XbKXVVi5yTx88WfCm67MSZ%2B%2FmJ0ovX9ZZ9N2s6rGuztTCaWI6F7GNOnbOEdB6pyL8rM7RSYCKmKSgcLYybYILXYcllaWGes41hWk1dyzCcs5hLXJgmreY3kA6zK6LgVMIjI%2BLwGOqUB0DyAYAZpudLxv%2B2KvXxFC7HAbFx9UG8t4dy817z01PaqDkrVXdqMOBGfEvJw8rB6Uf6pTsvFD%2BfgB2F693fcdkNtQlcY6taS8tosTjx7HGp%2Fw7pjJrdCAHpSSqJJehgIW4sDAYxk1%2BkHpPhGtK09dR0yodtosJPQaZ3m%2BrglBhg2VZWpBb9yCawRHkIuWcFqSFO6dtU02pNeml1XtK%2BBB%2FUrZi8a&X-Amz-Signature=30ba9ac525bd9fc8c9a6adc8373c5f8868ecbbb136d12dc80ed07cec8527ea73&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4ENKKOH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRysIzXncgx7Vn7eYulJK9gLk46UswS1tEStgmsmziNwIgI%2FvqlqULUc8NGBVBq44eRPjgDXr2guHKdS0H2yuDcBoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCkNaZ4%2Fbg7%2BwV0rircAwmiOMNO3MyREP4AzZzRigWOCDvyI5xIFnUF7GUJ5e1tQRMIMi8XL42FvtGtE7MjvP9FTEjEIi16cbWbwQydcE0H6ifMsX0QQYcAp35A%2B7MNdQbFEBY4XUntn0ivpD3TTToCb4zZu7Z72eDY44uqYZ1E0Aq6m8jNMHryo0CyyCu%2BGqL6ZzcMn%2BfdwMsyO6xozGB41hby%2F0yrP7gStowfb0aAssu3jDMGL4Pm0ZE3Oj4mU%2FIzb221AS4%2BWwSj6%2F0KUjKhc%2BLFdYxw%2B2M38f9L1OSeQQOF4egKrKPUpN6UZSA%2Bg%2BpyZj%2BSvV4GKtPJ%2F0Q%2Byhd0JT8wvv%2Bn1w8US49w%2BMOEo0Xuw%2B6Tw0LQwlweyDg61z%2BbeBzxh%2BSknjkJGC7wghiunw17HzKRmTfTBcVF4s53YUOfRs3bkGCZ9dgcLi4qmFNB0oTSXCfBawhmnWB5svXe2LUO5ZPC%2BH%2B91XDnM%2BCct%2FZnnxwsT5Pk7SbOtUcyTawJfCSNg3H8xbVU9XbKXVVi5yTx88WfCm67MSZ%2B%2FmJ0ovX9ZZ9N2s6rGuztTCaWI6F7GNOnbOEdB6pyL8rM7RSYCKmKSgcLYybYILXYcllaWGes41hWk1dyzCcs5hLXJgmreY3kA6zK6LgVMIjI%2BLwGOqUB0DyAYAZpudLxv%2B2KvXxFC7HAbFx9UG8t4dy817z01PaqDkrVXdqMOBGfEvJw8rB6Uf6pTsvFD%2BfgB2F693fcdkNtQlcY6taS8tosTjx7HGp%2Fw7pjJrdCAHpSSqJJehgIW4sDAYxk1%2BkHpPhGtK09dR0yodtosJPQaZ3m%2BrglBhg2VZWpBb9yCawRHkIuWcFqSFO6dtU02pNeml1XtK%2BBB%2FUrZi8a&X-Amz-Signature=9d556b3bdbe6d92acf4e7171d8bda877d4038af8997924e4fae7952780ec3888&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4ENKKOH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRysIzXncgx7Vn7eYulJK9gLk46UswS1tEStgmsmziNwIgI%2FvqlqULUc8NGBVBq44eRPjgDXr2guHKdS0H2yuDcBoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCkNaZ4%2Fbg7%2BwV0rircAwmiOMNO3MyREP4AzZzRigWOCDvyI5xIFnUF7GUJ5e1tQRMIMi8XL42FvtGtE7MjvP9FTEjEIi16cbWbwQydcE0H6ifMsX0QQYcAp35A%2B7MNdQbFEBY4XUntn0ivpD3TTToCb4zZu7Z72eDY44uqYZ1E0Aq6m8jNMHryo0CyyCu%2BGqL6ZzcMn%2BfdwMsyO6xozGB41hby%2F0yrP7gStowfb0aAssu3jDMGL4Pm0ZE3Oj4mU%2FIzb221AS4%2BWwSj6%2F0KUjKhc%2BLFdYxw%2B2M38f9L1OSeQQOF4egKrKPUpN6UZSA%2Bg%2BpyZj%2BSvV4GKtPJ%2F0Q%2Byhd0JT8wvv%2Bn1w8US49w%2BMOEo0Xuw%2B6Tw0LQwlweyDg61z%2BbeBzxh%2BSknjkJGC7wghiunw17HzKRmTfTBcVF4s53YUOfRs3bkGCZ9dgcLi4qmFNB0oTSXCfBawhmnWB5svXe2LUO5ZPC%2BH%2B91XDnM%2BCct%2FZnnxwsT5Pk7SbOtUcyTawJfCSNg3H8xbVU9XbKXVVi5yTx88WfCm67MSZ%2B%2FmJ0ovX9ZZ9N2s6rGuztTCaWI6F7GNOnbOEdB6pyL8rM7RSYCKmKSgcLYybYILXYcllaWGes41hWk1dyzCcs5hLXJgmreY3kA6zK6LgVMIjI%2BLwGOqUB0DyAYAZpudLxv%2B2KvXxFC7HAbFx9UG8t4dy817z01PaqDkrVXdqMOBGfEvJw8rB6Uf6pTsvFD%2BfgB2F693fcdkNtQlcY6taS8tosTjx7HGp%2Fw7pjJrdCAHpSSqJJehgIW4sDAYxk1%2BkHpPhGtK09dR0yodtosJPQaZ3m%2BrglBhg2VZWpBb9yCawRHkIuWcFqSFO6dtU02pNeml1XtK%2BBB%2FUrZi8a&X-Amz-Signature=95512cb27835b2cd2380e93e6c68f3e67902174528c42a48399d1d07e97e74da&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4ENKKOH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRysIzXncgx7Vn7eYulJK9gLk46UswS1tEStgmsmziNwIgI%2FvqlqULUc8NGBVBq44eRPjgDXr2guHKdS0H2yuDcBoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCkNaZ4%2Fbg7%2BwV0rircAwmiOMNO3MyREP4AzZzRigWOCDvyI5xIFnUF7GUJ5e1tQRMIMi8XL42FvtGtE7MjvP9FTEjEIi16cbWbwQydcE0H6ifMsX0QQYcAp35A%2B7MNdQbFEBY4XUntn0ivpD3TTToCb4zZu7Z72eDY44uqYZ1E0Aq6m8jNMHryo0CyyCu%2BGqL6ZzcMn%2BfdwMsyO6xozGB41hby%2F0yrP7gStowfb0aAssu3jDMGL4Pm0ZE3Oj4mU%2FIzb221AS4%2BWwSj6%2F0KUjKhc%2BLFdYxw%2B2M38f9L1OSeQQOF4egKrKPUpN6UZSA%2Bg%2BpyZj%2BSvV4GKtPJ%2F0Q%2Byhd0JT8wvv%2Bn1w8US49w%2BMOEo0Xuw%2B6Tw0LQwlweyDg61z%2BbeBzxh%2BSknjkJGC7wghiunw17HzKRmTfTBcVF4s53YUOfRs3bkGCZ9dgcLi4qmFNB0oTSXCfBawhmnWB5svXe2LUO5ZPC%2BH%2B91XDnM%2BCct%2FZnnxwsT5Pk7SbOtUcyTawJfCSNg3H8xbVU9XbKXVVi5yTx88WfCm67MSZ%2B%2FmJ0ovX9ZZ9N2s6rGuztTCaWI6F7GNOnbOEdB6pyL8rM7RSYCKmKSgcLYybYILXYcllaWGes41hWk1dyzCcs5hLXJgmreY3kA6zK6LgVMIjI%2BLwGOqUB0DyAYAZpudLxv%2B2KvXxFC7HAbFx9UG8t4dy817z01PaqDkrVXdqMOBGfEvJw8rB6Uf6pTsvFD%2BfgB2F693fcdkNtQlcY6taS8tosTjx7HGp%2Fw7pjJrdCAHpSSqJJehgIW4sDAYxk1%2BkHpPhGtK09dR0yodtosJPQaZ3m%2BrglBhg2VZWpBb9yCawRHkIuWcFqSFO6dtU02pNeml1XtK%2BBB%2FUrZi8a&X-Amz-Signature=bede8f2a82eed44f52c265303b898dcda7cee3fd13d1df28bab548f9cf56c4a7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4ENKKOH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRysIzXncgx7Vn7eYulJK9gLk46UswS1tEStgmsmziNwIgI%2FvqlqULUc8NGBVBq44eRPjgDXr2guHKdS0H2yuDcBoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCkNaZ4%2Fbg7%2BwV0rircAwmiOMNO3MyREP4AzZzRigWOCDvyI5xIFnUF7GUJ5e1tQRMIMi8XL42FvtGtE7MjvP9FTEjEIi16cbWbwQydcE0H6ifMsX0QQYcAp35A%2B7MNdQbFEBY4XUntn0ivpD3TTToCb4zZu7Z72eDY44uqYZ1E0Aq6m8jNMHryo0CyyCu%2BGqL6ZzcMn%2BfdwMsyO6xozGB41hby%2F0yrP7gStowfb0aAssu3jDMGL4Pm0ZE3Oj4mU%2FIzb221AS4%2BWwSj6%2F0KUjKhc%2BLFdYxw%2B2M38f9L1OSeQQOF4egKrKPUpN6UZSA%2Bg%2BpyZj%2BSvV4GKtPJ%2F0Q%2Byhd0JT8wvv%2Bn1w8US49w%2BMOEo0Xuw%2B6Tw0LQwlweyDg61z%2BbeBzxh%2BSknjkJGC7wghiunw17HzKRmTfTBcVF4s53YUOfRs3bkGCZ9dgcLi4qmFNB0oTSXCfBawhmnWB5svXe2LUO5ZPC%2BH%2B91XDnM%2BCct%2FZnnxwsT5Pk7SbOtUcyTawJfCSNg3H8xbVU9XbKXVVi5yTx88WfCm67MSZ%2B%2FmJ0ovX9ZZ9N2s6rGuztTCaWI6F7GNOnbOEdB6pyL8rM7RSYCKmKSgcLYybYILXYcllaWGes41hWk1dyzCcs5hLXJgmreY3kA6zK6LgVMIjI%2BLwGOqUB0DyAYAZpudLxv%2B2KvXxFC7HAbFx9UG8t4dy817z01PaqDkrVXdqMOBGfEvJw8rB6Uf6pTsvFD%2BfgB2F693fcdkNtQlcY6taS8tosTjx7HGp%2Fw7pjJrdCAHpSSqJJehgIW4sDAYxk1%2BkHpPhGtK09dR0yodtosJPQaZ3m%2BrglBhg2VZWpBb9yCawRHkIuWcFqSFO6dtU02pNeml1XtK%2BBB%2FUrZi8a&X-Amz-Signature=2be187739fafde375b49d33cfc6791e3f86ec2c3355e3c68c28fecabd0c62478&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4ENKKOH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRysIzXncgx7Vn7eYulJK9gLk46UswS1tEStgmsmziNwIgI%2FvqlqULUc8NGBVBq44eRPjgDXr2guHKdS0H2yuDcBoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCkNaZ4%2Fbg7%2BwV0rircAwmiOMNO3MyREP4AzZzRigWOCDvyI5xIFnUF7GUJ5e1tQRMIMi8XL42FvtGtE7MjvP9FTEjEIi16cbWbwQydcE0H6ifMsX0QQYcAp35A%2B7MNdQbFEBY4XUntn0ivpD3TTToCb4zZu7Z72eDY44uqYZ1E0Aq6m8jNMHryo0CyyCu%2BGqL6ZzcMn%2BfdwMsyO6xozGB41hby%2F0yrP7gStowfb0aAssu3jDMGL4Pm0ZE3Oj4mU%2FIzb221AS4%2BWwSj6%2F0KUjKhc%2BLFdYxw%2B2M38f9L1OSeQQOF4egKrKPUpN6UZSA%2Bg%2BpyZj%2BSvV4GKtPJ%2F0Q%2Byhd0JT8wvv%2Bn1w8US49w%2BMOEo0Xuw%2B6Tw0LQwlweyDg61z%2BbeBzxh%2BSknjkJGC7wghiunw17HzKRmTfTBcVF4s53YUOfRs3bkGCZ9dgcLi4qmFNB0oTSXCfBawhmnWB5svXe2LUO5ZPC%2BH%2B91XDnM%2BCct%2FZnnxwsT5Pk7SbOtUcyTawJfCSNg3H8xbVU9XbKXVVi5yTx88WfCm67MSZ%2B%2FmJ0ovX9ZZ9N2s6rGuztTCaWI6F7GNOnbOEdB6pyL8rM7RSYCKmKSgcLYybYILXYcllaWGes41hWk1dyzCcs5hLXJgmreY3kA6zK6LgVMIjI%2BLwGOqUB0DyAYAZpudLxv%2B2KvXxFC7HAbFx9UG8t4dy817z01PaqDkrVXdqMOBGfEvJw8rB6Uf6pTsvFD%2BfgB2F693fcdkNtQlcY6taS8tosTjx7HGp%2Fw7pjJrdCAHpSSqJJehgIW4sDAYxk1%2BkHpPhGtK09dR0yodtosJPQaZ3m%2BrglBhg2VZWpBb9yCawRHkIuWcFqSFO6dtU02pNeml1XtK%2BBB%2FUrZi8a&X-Amz-Signature=a6fcb165048e4b73d574740080f0851a3586ec875ca8f9408900629b3b91528a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4ENKKOH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRysIzXncgx7Vn7eYulJK9gLk46UswS1tEStgmsmziNwIgI%2FvqlqULUc8NGBVBq44eRPjgDXr2guHKdS0H2yuDcBoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCkNaZ4%2Fbg7%2BwV0rircAwmiOMNO3MyREP4AzZzRigWOCDvyI5xIFnUF7GUJ5e1tQRMIMi8XL42FvtGtE7MjvP9FTEjEIi16cbWbwQydcE0H6ifMsX0QQYcAp35A%2B7MNdQbFEBY4XUntn0ivpD3TTToCb4zZu7Z72eDY44uqYZ1E0Aq6m8jNMHryo0CyyCu%2BGqL6ZzcMn%2BfdwMsyO6xozGB41hby%2F0yrP7gStowfb0aAssu3jDMGL4Pm0ZE3Oj4mU%2FIzb221AS4%2BWwSj6%2F0KUjKhc%2BLFdYxw%2B2M38f9L1OSeQQOF4egKrKPUpN6UZSA%2Bg%2BpyZj%2BSvV4GKtPJ%2F0Q%2Byhd0JT8wvv%2Bn1w8US49w%2BMOEo0Xuw%2B6Tw0LQwlweyDg61z%2BbeBzxh%2BSknjkJGC7wghiunw17HzKRmTfTBcVF4s53YUOfRs3bkGCZ9dgcLi4qmFNB0oTSXCfBawhmnWB5svXe2LUO5ZPC%2BH%2B91XDnM%2BCct%2FZnnxwsT5Pk7SbOtUcyTawJfCSNg3H8xbVU9XbKXVVi5yTx88WfCm67MSZ%2B%2FmJ0ovX9ZZ9N2s6rGuztTCaWI6F7GNOnbOEdB6pyL8rM7RSYCKmKSgcLYybYILXYcllaWGes41hWk1dyzCcs5hLXJgmreY3kA6zK6LgVMIjI%2BLwGOqUB0DyAYAZpudLxv%2B2KvXxFC7HAbFx9UG8t4dy817z01PaqDkrVXdqMOBGfEvJw8rB6Uf6pTsvFD%2BfgB2F693fcdkNtQlcY6taS8tosTjx7HGp%2Fw7pjJrdCAHpSSqJJehgIW4sDAYxk1%2BkHpPhGtK09dR0yodtosJPQaZ3m%2BrglBhg2VZWpBb9yCawRHkIuWcFqSFO6dtU02pNeml1XtK%2BBB%2FUrZi8a&X-Amz-Signature=a6247250f1e1dafae6e42261427f9290637b6032a6c7a86bf52bc34d40a27015&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6B6QVZU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICEOc7O7fR4z%2F4ITSJDDvX4GX7eGmZQ2YgQNyKSDqu46AiBgaINEGKn%2BBiirLiJn4xFzmB3tOR3xiOAZnxPHoUvs%2BCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOd9bNIweVibzSaZyKtwD0krbHVvWiz0EM4JecBfb3SE23jXMBeWTl%2FQqqaHX6OFBMksv5ijbtHrRFJfHX8hUGLwHEVjibiJ12FL5fLTlautQaldZZMraGVxBLqOtb1GYPEZWvuXrwJzScN%2BPcdpAHuSqVJIXqLAb7yjJbeunWaYwf7BAKksVyJtW8%2FZjRAH9pnqC6MNGuhKv20fUaoJe4M5m8HV5QhF%2FTC7g8N0Y9iqdvG4TIvulQeqWJCYYGQ66Xh64qe0%2BbjXX3psgknE4DlFv%2B%2FXIJsEaPpPyy8ysR3Rb%2B%2Ba8WSeCFEXrEBEnAQjQv4yCFssxyAteyQnukUWMo3uXpzDznZyoUIiZSISqJC2kCZUfFgNDjRaT8Ta78SQSpKFyI2dCyjyek1Byr8fjXfzJFY4eQbE8gQZbUFzmUIRLqhM%2BNW51HI6h5yIODlijmfv4WrNWHT5kSayb7bph4FJEgqTU1v21ytaKoUWjeB8ncqP9d2DSZ8gMOoGxyELwjm4001JVn0QBr15Ui3hOH7XMEq25aJJYoStZHG4yPX5DeKYueaZ536X9R5RpZz%2BNSXCMh6eoSyJbCIVMij6nkHLxjjh6A%2BIQ2C6eSlOUc%2Bf3P4JCGDsRVpqG80rKc%2BkuwIrtoNrun2r7wOow%2BcX4vAY6pgG%2B9FxL5NtyrewwrNCvVkH7jNUkAZ9ap%2FVGJ72FJLg1nGfAFXrywCeqF9A7o7xY9XQyiqSdkY6MX8Pw4JIhtn4TJax4CuH76TD00SgAYvxCO0yJOq5DpvmO3d4nbAMfZO76DZftNleI%2BhxelSFUdiwvDi4kqTNOvDkk5%2BLITFrFKPGvopE3wmXOjTq6sS3LUM8kmSuVp%2FuUodD%2FtjSw7sl%2FaB3gdaMg&X-Amz-Signature=40d8e3618b6cf9f36665d57e44bae043b9eb6025aff101f85fef9287cfd24ce4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6B6QVZU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICEOc7O7fR4z%2F4ITSJDDvX4GX7eGmZQ2YgQNyKSDqu46AiBgaINEGKn%2BBiirLiJn4xFzmB3tOR3xiOAZnxPHoUvs%2BCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOd9bNIweVibzSaZyKtwD0krbHVvWiz0EM4JecBfb3SE23jXMBeWTl%2FQqqaHX6OFBMksv5ijbtHrRFJfHX8hUGLwHEVjibiJ12FL5fLTlautQaldZZMraGVxBLqOtb1GYPEZWvuXrwJzScN%2BPcdpAHuSqVJIXqLAb7yjJbeunWaYwf7BAKksVyJtW8%2FZjRAH9pnqC6MNGuhKv20fUaoJe4M5m8HV5QhF%2FTC7g8N0Y9iqdvG4TIvulQeqWJCYYGQ66Xh64qe0%2BbjXX3psgknE4DlFv%2B%2FXIJsEaPpPyy8ysR3Rb%2B%2Ba8WSeCFEXrEBEnAQjQv4yCFssxyAteyQnukUWMo3uXpzDznZyoUIiZSISqJC2kCZUfFgNDjRaT8Ta78SQSpKFyI2dCyjyek1Byr8fjXfzJFY4eQbE8gQZbUFzmUIRLqhM%2BNW51HI6h5yIODlijmfv4WrNWHT5kSayb7bph4FJEgqTU1v21ytaKoUWjeB8ncqP9d2DSZ8gMOoGxyELwjm4001JVn0QBr15Ui3hOH7XMEq25aJJYoStZHG4yPX5DeKYueaZ536X9R5RpZz%2BNSXCMh6eoSyJbCIVMij6nkHLxjjh6A%2BIQ2C6eSlOUc%2Bf3P4JCGDsRVpqG80rKc%2BkuwIrtoNrun2r7wOow%2BcX4vAY6pgG%2B9FxL5NtyrewwrNCvVkH7jNUkAZ9ap%2FVGJ72FJLg1nGfAFXrywCeqF9A7o7xY9XQyiqSdkY6MX8Pw4JIhtn4TJax4CuH76TD00SgAYvxCO0yJOq5DpvmO3d4nbAMfZO76DZftNleI%2BhxelSFUdiwvDi4kqTNOvDkk5%2BLITFrFKPGvopE3wmXOjTq6sS3LUM8kmSuVp%2FuUodD%2FtjSw7sl%2FaB3gdaMg&X-Amz-Signature=d21eddb561acb9d5cc41443492a9605dad5bd56fda0feef6a3497ac1ffe9d571&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
