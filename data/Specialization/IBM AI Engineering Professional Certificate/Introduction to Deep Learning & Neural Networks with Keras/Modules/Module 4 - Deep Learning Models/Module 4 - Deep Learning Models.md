

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CSS4IO7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDtjlumoW%2Bo0kEfC8yZd%2BC5w6gF37Mjh1ssaKJ0YSUKfAiEA0smAdBInJ%2F0AKhuf3WpMLi4IYzZ%2FwCGHP1GTZSL%2BMwQqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMv9fpc%2FF530hgmxpSrcAyRVYCuIJvon9dC4LLZQRbefIdaWDCG1rnbwLQygBQTbe2cNEEcmGnDyFzf%2F%2FwgBe%2FRdIvphO27viSsZ09LLlox0Vbhpmy4uOLJABOWCVr8jnqWbE1YJfeSVQYdiIlhQRSdMgt7rLvdZYt1b1Itn8BLjNBdR37dZm2jH3O%2Fn11%2BdEX3uFWQDhoU%2FdkQntZWtbO2MI2hA3F5pBhXqrKeMCzvydPeljiH7aGAYawO1fviyT7UorYEE580ANuucGZZYVwwtvSWxUazdZgHgMMwWL5Y1SCUhS5vTrfpZcBQzA0DgELM3o9c29I77GAPRKcKaCoaW5Ot15ZBdB2Zm21%2B7t0lwD8XMOrCutREdSm4I%2FAyubQ%2BSifCUqsEK7qhB%2BRtEC9qa%2B%2FOuNO0lmV58IaNHv11Ec7wbCXqcW14Q2EADPr2lBgK07X9QUHpTaVYzlH2SYQIvpPn4sIOrD28RoasMEyEPHwxUVYSYx5ww91zEhSdNr7yq2ed4NrxkizU9Q7XMk8HO4Z56GP6iQGrhzGFrX3VsMyWWAatjmhfc7cI4Zs%2FRBfLiKWwdKL4Eu0kZ0b4vblSYHfCYVEjho7Q1ZtaRjyFHvRkfSDEwMLwb19%2FmlmFZNnZobjgvuCTvIOCEMJqj7LwGOqUB9JQbjlYlBWgGCQN5Bhjq1TyD%2BAN8W12JYZrlSmLAu3cE06VW0%2BNr76yyEyWf1gDeM2Ge4xA9lDx57Z7QVpd7P4S8mkDGxP%2FWXKUL0HN8enDpyi66bUM4n1akvYUXDUNHDzPgaUwP2m254llQWJN0XxLS88fbM8bpCpmhGrSldfqpzg9b7jiGLB%2B6pjfalxlhDIsbAgXZoTBOjrIrnwDp2ymNl72A&X-Amz-Signature=81b2ab53084832d723f64eb401ff12182b5afca5bc6658803bfacb400d1f6dcb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CSS4IO7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDtjlumoW%2Bo0kEfC8yZd%2BC5w6gF37Mjh1ssaKJ0YSUKfAiEA0smAdBInJ%2F0AKhuf3WpMLi4IYzZ%2FwCGHP1GTZSL%2BMwQqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMv9fpc%2FF530hgmxpSrcAyRVYCuIJvon9dC4LLZQRbefIdaWDCG1rnbwLQygBQTbe2cNEEcmGnDyFzf%2F%2FwgBe%2FRdIvphO27viSsZ09LLlox0Vbhpmy4uOLJABOWCVr8jnqWbE1YJfeSVQYdiIlhQRSdMgt7rLvdZYt1b1Itn8BLjNBdR37dZm2jH3O%2Fn11%2BdEX3uFWQDhoU%2FdkQntZWtbO2MI2hA3F5pBhXqrKeMCzvydPeljiH7aGAYawO1fviyT7UorYEE580ANuucGZZYVwwtvSWxUazdZgHgMMwWL5Y1SCUhS5vTrfpZcBQzA0DgELM3o9c29I77GAPRKcKaCoaW5Ot15ZBdB2Zm21%2B7t0lwD8XMOrCutREdSm4I%2FAyubQ%2BSifCUqsEK7qhB%2BRtEC9qa%2B%2FOuNO0lmV58IaNHv11Ec7wbCXqcW14Q2EADPr2lBgK07X9QUHpTaVYzlH2SYQIvpPn4sIOrD28RoasMEyEPHwxUVYSYx5ww91zEhSdNr7yq2ed4NrxkizU9Q7XMk8HO4Z56GP6iQGrhzGFrX3VsMyWWAatjmhfc7cI4Zs%2FRBfLiKWwdKL4Eu0kZ0b4vblSYHfCYVEjho7Q1ZtaRjyFHvRkfSDEwMLwb19%2FmlmFZNnZobjgvuCTvIOCEMJqj7LwGOqUB9JQbjlYlBWgGCQN5Bhjq1TyD%2BAN8W12JYZrlSmLAu3cE06VW0%2BNr76yyEyWf1gDeM2Ge4xA9lDx57Z7QVpd7P4S8mkDGxP%2FWXKUL0HN8enDpyi66bUM4n1akvYUXDUNHDzPgaUwP2m254llQWJN0XxLS88fbM8bpCpmhGrSldfqpzg9b7jiGLB%2B6pjfalxlhDIsbAgXZoTBOjrIrnwDp2ymNl72A&X-Amz-Signature=4848646fc96b2bb34f1b5e5749629357027bdcc0a5bbb99c9e545756e538c53e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CSS4IO7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDtjlumoW%2Bo0kEfC8yZd%2BC5w6gF37Mjh1ssaKJ0YSUKfAiEA0smAdBInJ%2F0AKhuf3WpMLi4IYzZ%2FwCGHP1GTZSL%2BMwQqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMv9fpc%2FF530hgmxpSrcAyRVYCuIJvon9dC4LLZQRbefIdaWDCG1rnbwLQygBQTbe2cNEEcmGnDyFzf%2F%2FwgBe%2FRdIvphO27viSsZ09LLlox0Vbhpmy4uOLJABOWCVr8jnqWbE1YJfeSVQYdiIlhQRSdMgt7rLvdZYt1b1Itn8BLjNBdR37dZm2jH3O%2Fn11%2BdEX3uFWQDhoU%2FdkQntZWtbO2MI2hA3F5pBhXqrKeMCzvydPeljiH7aGAYawO1fviyT7UorYEE580ANuucGZZYVwwtvSWxUazdZgHgMMwWL5Y1SCUhS5vTrfpZcBQzA0DgELM3o9c29I77GAPRKcKaCoaW5Ot15ZBdB2Zm21%2B7t0lwD8XMOrCutREdSm4I%2FAyubQ%2BSifCUqsEK7qhB%2BRtEC9qa%2B%2FOuNO0lmV58IaNHv11Ec7wbCXqcW14Q2EADPr2lBgK07X9QUHpTaVYzlH2SYQIvpPn4sIOrD28RoasMEyEPHwxUVYSYx5ww91zEhSdNr7yq2ed4NrxkizU9Q7XMk8HO4Z56GP6iQGrhzGFrX3VsMyWWAatjmhfc7cI4Zs%2FRBfLiKWwdKL4Eu0kZ0b4vblSYHfCYVEjho7Q1ZtaRjyFHvRkfSDEwMLwb19%2FmlmFZNnZobjgvuCTvIOCEMJqj7LwGOqUB9JQbjlYlBWgGCQN5Bhjq1TyD%2BAN8W12JYZrlSmLAu3cE06VW0%2BNr76yyEyWf1gDeM2Ge4xA9lDx57Z7QVpd7P4S8mkDGxP%2FWXKUL0HN8enDpyi66bUM4n1akvYUXDUNHDzPgaUwP2m254llQWJN0XxLS88fbM8bpCpmhGrSldfqpzg9b7jiGLB%2B6pjfalxlhDIsbAgXZoTBOjrIrnwDp2ymNl72A&X-Amz-Signature=45396ef7097018cec0449db73795124b9a8a45430b7d58e5a35b7a622ce92fc9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CSS4IO7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDtjlumoW%2Bo0kEfC8yZd%2BC5w6gF37Mjh1ssaKJ0YSUKfAiEA0smAdBInJ%2F0AKhuf3WpMLi4IYzZ%2FwCGHP1GTZSL%2BMwQqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMv9fpc%2FF530hgmxpSrcAyRVYCuIJvon9dC4LLZQRbefIdaWDCG1rnbwLQygBQTbe2cNEEcmGnDyFzf%2F%2FwgBe%2FRdIvphO27viSsZ09LLlox0Vbhpmy4uOLJABOWCVr8jnqWbE1YJfeSVQYdiIlhQRSdMgt7rLvdZYt1b1Itn8BLjNBdR37dZm2jH3O%2Fn11%2BdEX3uFWQDhoU%2FdkQntZWtbO2MI2hA3F5pBhXqrKeMCzvydPeljiH7aGAYawO1fviyT7UorYEE580ANuucGZZYVwwtvSWxUazdZgHgMMwWL5Y1SCUhS5vTrfpZcBQzA0DgELM3o9c29I77GAPRKcKaCoaW5Ot15ZBdB2Zm21%2B7t0lwD8XMOrCutREdSm4I%2FAyubQ%2BSifCUqsEK7qhB%2BRtEC9qa%2B%2FOuNO0lmV58IaNHv11Ec7wbCXqcW14Q2EADPr2lBgK07X9QUHpTaVYzlH2SYQIvpPn4sIOrD28RoasMEyEPHwxUVYSYx5ww91zEhSdNr7yq2ed4NrxkizU9Q7XMk8HO4Z56GP6iQGrhzGFrX3VsMyWWAatjmhfc7cI4Zs%2FRBfLiKWwdKL4Eu0kZ0b4vblSYHfCYVEjho7Q1ZtaRjyFHvRkfSDEwMLwb19%2FmlmFZNnZobjgvuCTvIOCEMJqj7LwGOqUB9JQbjlYlBWgGCQN5Bhjq1TyD%2BAN8W12JYZrlSmLAu3cE06VW0%2BNr76yyEyWf1gDeM2Ge4xA9lDx57Z7QVpd7P4S8mkDGxP%2FWXKUL0HN8enDpyi66bUM4n1akvYUXDUNHDzPgaUwP2m254llQWJN0XxLS88fbM8bpCpmhGrSldfqpzg9b7jiGLB%2B6pjfalxlhDIsbAgXZoTBOjrIrnwDp2ymNl72A&X-Amz-Signature=2bdc1c7c50a241d698a56ae1a54406b4cc70a0071b23b631d99dbc8d41eb520a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CSS4IO7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDtjlumoW%2Bo0kEfC8yZd%2BC5w6gF37Mjh1ssaKJ0YSUKfAiEA0smAdBInJ%2F0AKhuf3WpMLi4IYzZ%2FwCGHP1GTZSL%2BMwQqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMv9fpc%2FF530hgmxpSrcAyRVYCuIJvon9dC4LLZQRbefIdaWDCG1rnbwLQygBQTbe2cNEEcmGnDyFzf%2F%2FwgBe%2FRdIvphO27viSsZ09LLlox0Vbhpmy4uOLJABOWCVr8jnqWbE1YJfeSVQYdiIlhQRSdMgt7rLvdZYt1b1Itn8BLjNBdR37dZm2jH3O%2Fn11%2BdEX3uFWQDhoU%2FdkQntZWtbO2MI2hA3F5pBhXqrKeMCzvydPeljiH7aGAYawO1fviyT7UorYEE580ANuucGZZYVwwtvSWxUazdZgHgMMwWL5Y1SCUhS5vTrfpZcBQzA0DgELM3o9c29I77GAPRKcKaCoaW5Ot15ZBdB2Zm21%2B7t0lwD8XMOrCutREdSm4I%2FAyubQ%2BSifCUqsEK7qhB%2BRtEC9qa%2B%2FOuNO0lmV58IaNHv11Ec7wbCXqcW14Q2EADPr2lBgK07X9QUHpTaVYzlH2SYQIvpPn4sIOrD28RoasMEyEPHwxUVYSYx5ww91zEhSdNr7yq2ed4NrxkizU9Q7XMk8HO4Z56GP6iQGrhzGFrX3VsMyWWAatjmhfc7cI4Zs%2FRBfLiKWwdKL4Eu0kZ0b4vblSYHfCYVEjho7Q1ZtaRjyFHvRkfSDEwMLwb19%2FmlmFZNnZobjgvuCTvIOCEMJqj7LwGOqUB9JQbjlYlBWgGCQN5Bhjq1TyD%2BAN8W12JYZrlSmLAu3cE06VW0%2BNr76yyEyWf1gDeM2Ge4xA9lDx57Z7QVpd7P4S8mkDGxP%2FWXKUL0HN8enDpyi66bUM4n1akvYUXDUNHDzPgaUwP2m254llQWJN0XxLS88fbM8bpCpmhGrSldfqpzg9b7jiGLB%2B6pjfalxlhDIsbAgXZoTBOjrIrnwDp2ymNl72A&X-Amz-Signature=368d41869399e59db515b9ca991d6a6d4971df1b6dd0ea302ace8b241055b591&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CSS4IO7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDtjlumoW%2Bo0kEfC8yZd%2BC5w6gF37Mjh1ssaKJ0YSUKfAiEA0smAdBInJ%2F0AKhuf3WpMLi4IYzZ%2FwCGHP1GTZSL%2BMwQqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMv9fpc%2FF530hgmxpSrcAyRVYCuIJvon9dC4LLZQRbefIdaWDCG1rnbwLQygBQTbe2cNEEcmGnDyFzf%2F%2FwgBe%2FRdIvphO27viSsZ09LLlox0Vbhpmy4uOLJABOWCVr8jnqWbE1YJfeSVQYdiIlhQRSdMgt7rLvdZYt1b1Itn8BLjNBdR37dZm2jH3O%2Fn11%2BdEX3uFWQDhoU%2FdkQntZWtbO2MI2hA3F5pBhXqrKeMCzvydPeljiH7aGAYawO1fviyT7UorYEE580ANuucGZZYVwwtvSWxUazdZgHgMMwWL5Y1SCUhS5vTrfpZcBQzA0DgELM3o9c29I77GAPRKcKaCoaW5Ot15ZBdB2Zm21%2B7t0lwD8XMOrCutREdSm4I%2FAyubQ%2BSifCUqsEK7qhB%2BRtEC9qa%2B%2FOuNO0lmV58IaNHv11Ec7wbCXqcW14Q2EADPr2lBgK07X9QUHpTaVYzlH2SYQIvpPn4sIOrD28RoasMEyEPHwxUVYSYx5ww91zEhSdNr7yq2ed4NrxkizU9Q7XMk8HO4Z56GP6iQGrhzGFrX3VsMyWWAatjmhfc7cI4Zs%2FRBfLiKWwdKL4Eu0kZ0b4vblSYHfCYVEjho7Q1ZtaRjyFHvRkfSDEwMLwb19%2FmlmFZNnZobjgvuCTvIOCEMJqj7LwGOqUB9JQbjlYlBWgGCQN5Bhjq1TyD%2BAN8W12JYZrlSmLAu3cE06VW0%2BNr76yyEyWf1gDeM2Ge4xA9lDx57Z7QVpd7P4S8mkDGxP%2FWXKUL0HN8enDpyi66bUM4n1akvYUXDUNHDzPgaUwP2m254llQWJN0XxLS88fbM8bpCpmhGrSldfqpzg9b7jiGLB%2B6pjfalxlhDIsbAgXZoTBOjrIrnwDp2ymNl72A&X-Amz-Signature=ec27f9c13f1af2b01a3834134175f077fed35bc8f0f45a237f8f4021f309bc3d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CSS4IO7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDtjlumoW%2Bo0kEfC8yZd%2BC5w6gF37Mjh1ssaKJ0YSUKfAiEA0smAdBInJ%2F0AKhuf3WpMLi4IYzZ%2FwCGHP1GTZSL%2BMwQqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMv9fpc%2FF530hgmxpSrcAyRVYCuIJvon9dC4LLZQRbefIdaWDCG1rnbwLQygBQTbe2cNEEcmGnDyFzf%2F%2FwgBe%2FRdIvphO27viSsZ09LLlox0Vbhpmy4uOLJABOWCVr8jnqWbE1YJfeSVQYdiIlhQRSdMgt7rLvdZYt1b1Itn8BLjNBdR37dZm2jH3O%2Fn11%2BdEX3uFWQDhoU%2FdkQntZWtbO2MI2hA3F5pBhXqrKeMCzvydPeljiH7aGAYawO1fviyT7UorYEE580ANuucGZZYVwwtvSWxUazdZgHgMMwWL5Y1SCUhS5vTrfpZcBQzA0DgELM3o9c29I77GAPRKcKaCoaW5Ot15ZBdB2Zm21%2B7t0lwD8XMOrCutREdSm4I%2FAyubQ%2BSifCUqsEK7qhB%2BRtEC9qa%2B%2FOuNO0lmV58IaNHv11Ec7wbCXqcW14Q2EADPr2lBgK07X9QUHpTaVYzlH2SYQIvpPn4sIOrD28RoasMEyEPHwxUVYSYx5ww91zEhSdNr7yq2ed4NrxkizU9Q7XMk8HO4Z56GP6iQGrhzGFrX3VsMyWWAatjmhfc7cI4Zs%2FRBfLiKWwdKL4Eu0kZ0b4vblSYHfCYVEjho7Q1ZtaRjyFHvRkfSDEwMLwb19%2FmlmFZNnZobjgvuCTvIOCEMJqj7LwGOqUB9JQbjlYlBWgGCQN5Bhjq1TyD%2BAN8W12JYZrlSmLAu3cE06VW0%2BNr76yyEyWf1gDeM2Ge4xA9lDx57Z7QVpd7P4S8mkDGxP%2FWXKUL0HN8enDpyi66bUM4n1akvYUXDUNHDzPgaUwP2m254llQWJN0XxLS88fbM8bpCpmhGrSldfqpzg9b7jiGLB%2B6pjfalxlhDIsbAgXZoTBOjrIrnwDp2ymNl72A&X-Amz-Signature=107ecd390ff06391b430821e44352d3d579c5aaa8239aa8e2ab7fa23e5340f59&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CSS4IO7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDtjlumoW%2Bo0kEfC8yZd%2BC5w6gF37Mjh1ssaKJ0YSUKfAiEA0smAdBInJ%2F0AKhuf3WpMLi4IYzZ%2FwCGHP1GTZSL%2BMwQqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMv9fpc%2FF530hgmxpSrcAyRVYCuIJvon9dC4LLZQRbefIdaWDCG1rnbwLQygBQTbe2cNEEcmGnDyFzf%2F%2FwgBe%2FRdIvphO27viSsZ09LLlox0Vbhpmy4uOLJABOWCVr8jnqWbE1YJfeSVQYdiIlhQRSdMgt7rLvdZYt1b1Itn8BLjNBdR37dZm2jH3O%2Fn11%2BdEX3uFWQDhoU%2FdkQntZWtbO2MI2hA3F5pBhXqrKeMCzvydPeljiH7aGAYawO1fviyT7UorYEE580ANuucGZZYVwwtvSWxUazdZgHgMMwWL5Y1SCUhS5vTrfpZcBQzA0DgELM3o9c29I77GAPRKcKaCoaW5Ot15ZBdB2Zm21%2B7t0lwD8XMOrCutREdSm4I%2FAyubQ%2BSifCUqsEK7qhB%2BRtEC9qa%2B%2FOuNO0lmV58IaNHv11Ec7wbCXqcW14Q2EADPr2lBgK07X9QUHpTaVYzlH2SYQIvpPn4sIOrD28RoasMEyEPHwxUVYSYx5ww91zEhSdNr7yq2ed4NrxkizU9Q7XMk8HO4Z56GP6iQGrhzGFrX3VsMyWWAatjmhfc7cI4Zs%2FRBfLiKWwdKL4Eu0kZ0b4vblSYHfCYVEjho7Q1ZtaRjyFHvRkfSDEwMLwb19%2FmlmFZNnZobjgvuCTvIOCEMJqj7LwGOqUB9JQbjlYlBWgGCQN5Bhjq1TyD%2BAN8W12JYZrlSmLAu3cE06VW0%2BNr76yyEyWf1gDeM2Ge4xA9lDx57Z7QVpd7P4S8mkDGxP%2FWXKUL0HN8enDpyi66bUM4n1akvYUXDUNHDzPgaUwP2m254llQWJN0XxLS88fbM8bpCpmhGrSldfqpzg9b7jiGLB%2B6pjfalxlhDIsbAgXZoTBOjrIrnwDp2ymNl72A&X-Amz-Signature=0594c81eca4bf094e10d2ed5b61e640a6667be4949ac297f45314345bdff348f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CSS4IO7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDtjlumoW%2Bo0kEfC8yZd%2BC5w6gF37Mjh1ssaKJ0YSUKfAiEA0smAdBInJ%2F0AKhuf3WpMLi4IYzZ%2FwCGHP1GTZSL%2BMwQqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMv9fpc%2FF530hgmxpSrcAyRVYCuIJvon9dC4LLZQRbefIdaWDCG1rnbwLQygBQTbe2cNEEcmGnDyFzf%2F%2FwgBe%2FRdIvphO27viSsZ09LLlox0Vbhpmy4uOLJABOWCVr8jnqWbE1YJfeSVQYdiIlhQRSdMgt7rLvdZYt1b1Itn8BLjNBdR37dZm2jH3O%2Fn11%2BdEX3uFWQDhoU%2FdkQntZWtbO2MI2hA3F5pBhXqrKeMCzvydPeljiH7aGAYawO1fviyT7UorYEE580ANuucGZZYVwwtvSWxUazdZgHgMMwWL5Y1SCUhS5vTrfpZcBQzA0DgELM3o9c29I77GAPRKcKaCoaW5Ot15ZBdB2Zm21%2B7t0lwD8XMOrCutREdSm4I%2FAyubQ%2BSifCUqsEK7qhB%2BRtEC9qa%2B%2FOuNO0lmV58IaNHv11Ec7wbCXqcW14Q2EADPr2lBgK07X9QUHpTaVYzlH2SYQIvpPn4sIOrD28RoasMEyEPHwxUVYSYx5ww91zEhSdNr7yq2ed4NrxkizU9Q7XMk8HO4Z56GP6iQGrhzGFrX3VsMyWWAatjmhfc7cI4Zs%2FRBfLiKWwdKL4Eu0kZ0b4vblSYHfCYVEjho7Q1ZtaRjyFHvRkfSDEwMLwb19%2FmlmFZNnZobjgvuCTvIOCEMJqj7LwGOqUB9JQbjlYlBWgGCQN5Bhjq1TyD%2BAN8W12JYZrlSmLAu3cE06VW0%2BNr76yyEyWf1gDeM2Ge4xA9lDx57Z7QVpd7P4S8mkDGxP%2FWXKUL0HN8enDpyi66bUM4n1akvYUXDUNHDzPgaUwP2m254llQWJN0XxLS88fbM8bpCpmhGrSldfqpzg9b7jiGLB%2B6pjfalxlhDIsbAgXZoTBOjrIrnwDp2ymNl72A&X-Amz-Signature=6b93f9e4f4f3d3c0e3ec222ebfcbf3964b366f6786172ade8a6180d861299375&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FB6MH6K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUZJI%2Bb0aSJtKJondsYVQJSiJ78fjVNTZT11yUW1Sz8wIhAO61rsS0AXbdWHPUYUxvctmnrFNlIEAWq6O7bHIaPwVkKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb9w0LRPZIwzgP21gq3ANOtjsP6NGf%2FvCUWFBRuBcxmB6Z%2FqfAhijok0HHDDttTLm5d%2FsDuh7xQqPmBL1KA7VEhrqKHeXsMtTuUoIdCKilN93y%2BFDe90128NfHPBj6GXHEqOoTHd1DKH9CWgw2BiY22uwNUSqyihHvPM2x8NdRO5IpHb%2BVgxYAkgJBLNpvPTdNEqp2W8LqFkUFm9CmTrdERIgJ3URSnMcdA3MSSBfNkgcT4r%2B9y5%2BE8wSY2byLHGULv%2B%2Bse2oYyhwye%2FzFriuijrpRG3B7S9sPd9b8xSQcw8CpxpgbYKCogqdm9r8tWw0BPek1X%2FrL8E5yuJA599xKRpwwU1W0iGMWCTx6YjIRglkvv6k2rjVGMQb5r9Xu0d%2Bvs9sEPyPwyx%2B9PRwROlhcjdd8ePJ376Ahyea6SrD4LB5KetnYDNG8JNqQOX6TcCJTABvTU8TllNqba92QePv%2BgOhgZ8NEeHDqCbEbOv09enDf5IE%2FfulTnIv%2BcGZwjbMnowTxi9WX1QZDlzlnXr7LF7mmNn59%2BxOg7F1kdpaYfDQHhtlQzjlVIO%2FUabxxIxfhjzhHYsXOJit9NpmMt6gf8w8mdjAcIztj9ualDJlAzFhyF7eJp%2FTTyYeNxUNooQquN6JTFgZEHAfQJjD7ouy8BjqkAZvQWxJWNeh5MiZceK2q75JpipaGppBbr%2BkgVBnhyTkv7gOjPrN1nHiXG4E%2FPrsvzFFQrZ6dtoXZ4mxbrR7aFGfEYZsv7Isf%2FhWXUH8l6mIvufx7X0YYGrMV%2F3Va%2BOhQbsL7%2FqEig%2FGNZGb79TUzgpeghur1Mo2465mYgjKNHaVvZMTO9EqvMAnsgN%2FwB772yhxm9qstA5mvT0yfkImG2QgWoYQG&X-Amz-Signature=031a71833fa6bf58258c86af3d84eed8ad60847c25354028c36d385c3fbe586f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FB6MH6K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUZJI%2Bb0aSJtKJondsYVQJSiJ78fjVNTZT11yUW1Sz8wIhAO61rsS0AXbdWHPUYUxvctmnrFNlIEAWq6O7bHIaPwVkKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb9w0LRPZIwzgP21gq3ANOtjsP6NGf%2FvCUWFBRuBcxmB6Z%2FqfAhijok0HHDDttTLm5d%2FsDuh7xQqPmBL1KA7VEhrqKHeXsMtTuUoIdCKilN93y%2BFDe90128NfHPBj6GXHEqOoTHd1DKH9CWgw2BiY22uwNUSqyihHvPM2x8NdRO5IpHb%2BVgxYAkgJBLNpvPTdNEqp2W8LqFkUFm9CmTrdERIgJ3URSnMcdA3MSSBfNkgcT4r%2B9y5%2BE8wSY2byLHGULv%2B%2Bse2oYyhwye%2FzFriuijrpRG3B7S9sPd9b8xSQcw8CpxpgbYKCogqdm9r8tWw0BPek1X%2FrL8E5yuJA599xKRpwwU1W0iGMWCTx6YjIRglkvv6k2rjVGMQb5r9Xu0d%2Bvs9sEPyPwyx%2B9PRwROlhcjdd8ePJ376Ahyea6SrD4LB5KetnYDNG8JNqQOX6TcCJTABvTU8TllNqba92QePv%2BgOhgZ8NEeHDqCbEbOv09enDf5IE%2FfulTnIv%2BcGZwjbMnowTxi9WX1QZDlzlnXr7LF7mmNn59%2BxOg7F1kdpaYfDQHhtlQzjlVIO%2FUabxxIxfhjzhHYsXOJit9NpmMt6gf8w8mdjAcIztj9ualDJlAzFhyF7eJp%2FTTyYeNxUNooQquN6JTFgZEHAfQJjD7ouy8BjqkAZvQWxJWNeh5MiZceK2q75JpipaGppBbr%2BkgVBnhyTkv7gOjPrN1nHiXG4E%2FPrsvzFFQrZ6dtoXZ4mxbrR7aFGfEYZsv7Isf%2FhWXUH8l6mIvufx7X0YYGrMV%2F3Va%2BOhQbsL7%2FqEig%2FGNZGb79TUzgpeghur1Mo2465mYgjKNHaVvZMTO9EqvMAnsgN%2FwB772yhxm9qstA5mvT0yfkImG2QgWoYQG&X-Amz-Signature=5a2b819379da527b7d6e279fdcaeaaf75fc69e5914df1bf668df8b746562e708&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
