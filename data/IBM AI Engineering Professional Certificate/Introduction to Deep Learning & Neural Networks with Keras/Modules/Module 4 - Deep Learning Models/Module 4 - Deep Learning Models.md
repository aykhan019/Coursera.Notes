

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PIZ3LU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGw8Koqnrjtk7yaJdI2xuA6QVmboyVBLs4yuLN6%2BT5kCAiEAlzNI1zMrGwKSaNKydu6TG%2B5egPzP%2B6lBG%2B8LDD2PZ0UqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVSG8bQ%2BA0l4vWgIircA9PdEqfXxU5%2FTsRLmNZ5lvFz3DRQIQYGnC0HI4dDAH3wl0tfPEnAXa6LgumvzLL7Db%2B0wydXAVhyLSAlsAVqv4%2B%2BjaL4DToO1iZGenDmJHZqtlDS4C%2FUI3sa0R7gStwttPLQnqTLW%2B90id60ca%2FWKvNMIOoYV%2Bs5OcjiydNzC3IX0DkOf0%2BKwuZWk1PlHbYxjrPl3qfU%2BC%2BH4M58hJBaqLIb8kk5tC%2F158rqTEmE4zxf6duZJtr2iU9xFCyKNKOH%2BRhYLC%2Fw2WfZBwT5Y7RDE%2FWZpaT0jBjf6vFxccKz1KINjcifColK69WTgp6N7C1AJbEiyOcLECPr18zUc50MMRbfrEIOgmt0WqCROXFY%2B46mVCZyL%2FBcJyA2NP57SlUJTp48Kor3g6hC5ulD7UIZ439WBfcqKgwUXOesR2NqZz%2FP7TXkYc9Hoci6VQ%2BeZi5yJl595fKmo6AtTrplPEq48wCwn1CsB4zZPSTvcbcDm2mL4ueBiCyW8p0lIImQd8RXLImX98XvwKX1RBW7gVu0zL%2FyG6SNtlk0Fl9vAl3Z05xlXm8sigmVwstDJWpFPn1bBaLvPIUfNZOoz2ORlH8P9tblOBC0X7rmbwQU1cgEchEwT6IzEoDPq80wD64rMP%2BEnb0GOqUBI9u8%2FKMRxpFwSvbjIkc%2BJppG0s%2FCjFtx9yZ0abhPaI3FP%2BcAe8BTDNTPpb%2FLnyN3Idn%2FSmEEuu%2FAybPm%2BkdAPprg5gJJOK7zFcAP9HVxnwaAh5EQO%2FF7iJQUt5cr2bYQkLQAyC4E%2BJiE44KfzYtuH%2B65urJpHltXQMjOxgdwFSr35KJJqDm2ZITO4UnpnFVhhBCNxSlUd3X%2FRV6laZglPBx3amHM&X-Amz-Signature=d0cc9b60cb5cf6a4f33822330ff03a262e500cc66e86f8f3982f5ab44af71f30&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PIZ3LU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGw8Koqnrjtk7yaJdI2xuA6QVmboyVBLs4yuLN6%2BT5kCAiEAlzNI1zMrGwKSaNKydu6TG%2B5egPzP%2B6lBG%2B8LDD2PZ0UqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVSG8bQ%2BA0l4vWgIircA9PdEqfXxU5%2FTsRLmNZ5lvFz3DRQIQYGnC0HI4dDAH3wl0tfPEnAXa6LgumvzLL7Db%2B0wydXAVhyLSAlsAVqv4%2B%2BjaL4DToO1iZGenDmJHZqtlDS4C%2FUI3sa0R7gStwttPLQnqTLW%2B90id60ca%2FWKvNMIOoYV%2Bs5OcjiydNzC3IX0DkOf0%2BKwuZWk1PlHbYxjrPl3qfU%2BC%2BH4M58hJBaqLIb8kk5tC%2F158rqTEmE4zxf6duZJtr2iU9xFCyKNKOH%2BRhYLC%2Fw2WfZBwT5Y7RDE%2FWZpaT0jBjf6vFxccKz1KINjcifColK69WTgp6N7C1AJbEiyOcLECPr18zUc50MMRbfrEIOgmt0WqCROXFY%2B46mVCZyL%2FBcJyA2NP57SlUJTp48Kor3g6hC5ulD7UIZ439WBfcqKgwUXOesR2NqZz%2FP7TXkYc9Hoci6VQ%2BeZi5yJl595fKmo6AtTrplPEq48wCwn1CsB4zZPSTvcbcDm2mL4ueBiCyW8p0lIImQd8RXLImX98XvwKX1RBW7gVu0zL%2FyG6SNtlk0Fl9vAl3Z05xlXm8sigmVwstDJWpFPn1bBaLvPIUfNZOoz2ORlH8P9tblOBC0X7rmbwQU1cgEchEwT6IzEoDPq80wD64rMP%2BEnb0GOqUBI9u8%2FKMRxpFwSvbjIkc%2BJppG0s%2FCjFtx9yZ0abhPaI3FP%2BcAe8BTDNTPpb%2FLnyN3Idn%2FSmEEuu%2FAybPm%2BkdAPprg5gJJOK7zFcAP9HVxnwaAh5EQO%2FF7iJQUt5cr2bYQkLQAyC4E%2BJiE44KfzYtuH%2B65urJpHltXQMjOxgdwFSr35KJJqDm2ZITO4UnpnFVhhBCNxSlUd3X%2FRV6laZglPBx3amHM&X-Amz-Signature=c9e7dabebd14b2d6af01dba67761601ebd33287b85e6d911a947641fc29beca5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PIZ3LU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGw8Koqnrjtk7yaJdI2xuA6QVmboyVBLs4yuLN6%2BT5kCAiEAlzNI1zMrGwKSaNKydu6TG%2B5egPzP%2B6lBG%2B8LDD2PZ0UqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVSG8bQ%2BA0l4vWgIircA9PdEqfXxU5%2FTsRLmNZ5lvFz3DRQIQYGnC0HI4dDAH3wl0tfPEnAXa6LgumvzLL7Db%2B0wydXAVhyLSAlsAVqv4%2B%2BjaL4DToO1iZGenDmJHZqtlDS4C%2FUI3sa0R7gStwttPLQnqTLW%2B90id60ca%2FWKvNMIOoYV%2Bs5OcjiydNzC3IX0DkOf0%2BKwuZWk1PlHbYxjrPl3qfU%2BC%2BH4M58hJBaqLIb8kk5tC%2F158rqTEmE4zxf6duZJtr2iU9xFCyKNKOH%2BRhYLC%2Fw2WfZBwT5Y7RDE%2FWZpaT0jBjf6vFxccKz1KINjcifColK69WTgp6N7C1AJbEiyOcLECPr18zUc50MMRbfrEIOgmt0WqCROXFY%2B46mVCZyL%2FBcJyA2NP57SlUJTp48Kor3g6hC5ulD7UIZ439WBfcqKgwUXOesR2NqZz%2FP7TXkYc9Hoci6VQ%2BeZi5yJl595fKmo6AtTrplPEq48wCwn1CsB4zZPSTvcbcDm2mL4ueBiCyW8p0lIImQd8RXLImX98XvwKX1RBW7gVu0zL%2FyG6SNtlk0Fl9vAl3Z05xlXm8sigmVwstDJWpFPn1bBaLvPIUfNZOoz2ORlH8P9tblOBC0X7rmbwQU1cgEchEwT6IzEoDPq80wD64rMP%2BEnb0GOqUBI9u8%2FKMRxpFwSvbjIkc%2BJppG0s%2FCjFtx9yZ0abhPaI3FP%2BcAe8BTDNTPpb%2FLnyN3Idn%2FSmEEuu%2FAybPm%2BkdAPprg5gJJOK7zFcAP9HVxnwaAh5EQO%2FF7iJQUt5cr2bYQkLQAyC4E%2BJiE44KfzYtuH%2B65urJpHltXQMjOxgdwFSr35KJJqDm2ZITO4UnpnFVhhBCNxSlUd3X%2FRV6laZglPBx3amHM&X-Amz-Signature=a0072af4d2bef83599d01bb2bca9249e796ec3e3f7129f9f1ccde555f2b17e42&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PIZ3LU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGw8Koqnrjtk7yaJdI2xuA6QVmboyVBLs4yuLN6%2BT5kCAiEAlzNI1zMrGwKSaNKydu6TG%2B5egPzP%2B6lBG%2B8LDD2PZ0UqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVSG8bQ%2BA0l4vWgIircA9PdEqfXxU5%2FTsRLmNZ5lvFz3DRQIQYGnC0HI4dDAH3wl0tfPEnAXa6LgumvzLL7Db%2B0wydXAVhyLSAlsAVqv4%2B%2BjaL4DToO1iZGenDmJHZqtlDS4C%2FUI3sa0R7gStwttPLQnqTLW%2B90id60ca%2FWKvNMIOoYV%2Bs5OcjiydNzC3IX0DkOf0%2BKwuZWk1PlHbYxjrPl3qfU%2BC%2BH4M58hJBaqLIb8kk5tC%2F158rqTEmE4zxf6duZJtr2iU9xFCyKNKOH%2BRhYLC%2Fw2WfZBwT5Y7RDE%2FWZpaT0jBjf6vFxccKz1KINjcifColK69WTgp6N7C1AJbEiyOcLECPr18zUc50MMRbfrEIOgmt0WqCROXFY%2B46mVCZyL%2FBcJyA2NP57SlUJTp48Kor3g6hC5ulD7UIZ439WBfcqKgwUXOesR2NqZz%2FP7TXkYc9Hoci6VQ%2BeZi5yJl595fKmo6AtTrplPEq48wCwn1CsB4zZPSTvcbcDm2mL4ueBiCyW8p0lIImQd8RXLImX98XvwKX1RBW7gVu0zL%2FyG6SNtlk0Fl9vAl3Z05xlXm8sigmVwstDJWpFPn1bBaLvPIUfNZOoz2ORlH8P9tblOBC0X7rmbwQU1cgEchEwT6IzEoDPq80wD64rMP%2BEnb0GOqUBI9u8%2FKMRxpFwSvbjIkc%2BJppG0s%2FCjFtx9yZ0abhPaI3FP%2BcAe8BTDNTPpb%2FLnyN3Idn%2FSmEEuu%2FAybPm%2BkdAPprg5gJJOK7zFcAP9HVxnwaAh5EQO%2FF7iJQUt5cr2bYQkLQAyC4E%2BJiE44KfzYtuH%2B65urJpHltXQMjOxgdwFSr35KJJqDm2ZITO4UnpnFVhhBCNxSlUd3X%2FRV6laZglPBx3amHM&X-Amz-Signature=62fc21c638019b7be9be94a1fec64fd10c86c72c84aafc6458cf43190a93822a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PIZ3LU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGw8Koqnrjtk7yaJdI2xuA6QVmboyVBLs4yuLN6%2BT5kCAiEAlzNI1zMrGwKSaNKydu6TG%2B5egPzP%2B6lBG%2B8LDD2PZ0UqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVSG8bQ%2BA0l4vWgIircA9PdEqfXxU5%2FTsRLmNZ5lvFz3DRQIQYGnC0HI4dDAH3wl0tfPEnAXa6LgumvzLL7Db%2B0wydXAVhyLSAlsAVqv4%2B%2BjaL4DToO1iZGenDmJHZqtlDS4C%2FUI3sa0R7gStwttPLQnqTLW%2B90id60ca%2FWKvNMIOoYV%2Bs5OcjiydNzC3IX0DkOf0%2BKwuZWk1PlHbYxjrPl3qfU%2BC%2BH4M58hJBaqLIb8kk5tC%2F158rqTEmE4zxf6duZJtr2iU9xFCyKNKOH%2BRhYLC%2Fw2WfZBwT5Y7RDE%2FWZpaT0jBjf6vFxccKz1KINjcifColK69WTgp6N7C1AJbEiyOcLECPr18zUc50MMRbfrEIOgmt0WqCROXFY%2B46mVCZyL%2FBcJyA2NP57SlUJTp48Kor3g6hC5ulD7UIZ439WBfcqKgwUXOesR2NqZz%2FP7TXkYc9Hoci6VQ%2BeZi5yJl595fKmo6AtTrplPEq48wCwn1CsB4zZPSTvcbcDm2mL4ueBiCyW8p0lIImQd8RXLImX98XvwKX1RBW7gVu0zL%2FyG6SNtlk0Fl9vAl3Z05xlXm8sigmVwstDJWpFPn1bBaLvPIUfNZOoz2ORlH8P9tblOBC0X7rmbwQU1cgEchEwT6IzEoDPq80wD64rMP%2BEnb0GOqUBI9u8%2FKMRxpFwSvbjIkc%2BJppG0s%2FCjFtx9yZ0abhPaI3FP%2BcAe8BTDNTPpb%2FLnyN3Idn%2FSmEEuu%2FAybPm%2BkdAPprg5gJJOK7zFcAP9HVxnwaAh5EQO%2FF7iJQUt5cr2bYQkLQAyC4E%2BJiE44KfzYtuH%2B65urJpHltXQMjOxgdwFSr35KJJqDm2ZITO4UnpnFVhhBCNxSlUd3X%2FRV6laZglPBx3amHM&X-Amz-Signature=eb01d7bccb304d100cfa527fc3427d93dd85dd73025b9bffd55505a36b5b8312&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PIZ3LU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGw8Koqnrjtk7yaJdI2xuA6QVmboyVBLs4yuLN6%2BT5kCAiEAlzNI1zMrGwKSaNKydu6TG%2B5egPzP%2B6lBG%2B8LDD2PZ0UqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVSG8bQ%2BA0l4vWgIircA9PdEqfXxU5%2FTsRLmNZ5lvFz3DRQIQYGnC0HI4dDAH3wl0tfPEnAXa6LgumvzLL7Db%2B0wydXAVhyLSAlsAVqv4%2B%2BjaL4DToO1iZGenDmJHZqtlDS4C%2FUI3sa0R7gStwttPLQnqTLW%2B90id60ca%2FWKvNMIOoYV%2Bs5OcjiydNzC3IX0DkOf0%2BKwuZWk1PlHbYxjrPl3qfU%2BC%2BH4M58hJBaqLIb8kk5tC%2F158rqTEmE4zxf6duZJtr2iU9xFCyKNKOH%2BRhYLC%2Fw2WfZBwT5Y7RDE%2FWZpaT0jBjf6vFxccKz1KINjcifColK69WTgp6N7C1AJbEiyOcLECPr18zUc50MMRbfrEIOgmt0WqCROXFY%2B46mVCZyL%2FBcJyA2NP57SlUJTp48Kor3g6hC5ulD7UIZ439WBfcqKgwUXOesR2NqZz%2FP7TXkYc9Hoci6VQ%2BeZi5yJl595fKmo6AtTrplPEq48wCwn1CsB4zZPSTvcbcDm2mL4ueBiCyW8p0lIImQd8RXLImX98XvwKX1RBW7gVu0zL%2FyG6SNtlk0Fl9vAl3Z05xlXm8sigmVwstDJWpFPn1bBaLvPIUfNZOoz2ORlH8P9tblOBC0X7rmbwQU1cgEchEwT6IzEoDPq80wD64rMP%2BEnb0GOqUBI9u8%2FKMRxpFwSvbjIkc%2BJppG0s%2FCjFtx9yZ0abhPaI3FP%2BcAe8BTDNTPpb%2FLnyN3Idn%2FSmEEuu%2FAybPm%2BkdAPprg5gJJOK7zFcAP9HVxnwaAh5EQO%2FF7iJQUt5cr2bYQkLQAyC4E%2BJiE44KfzYtuH%2B65urJpHltXQMjOxgdwFSr35KJJqDm2ZITO4UnpnFVhhBCNxSlUd3X%2FRV6laZglPBx3amHM&X-Amz-Signature=9c839586b093b772a7817c7aaada33c53d62ecd75cc6d0dafd86ad4d485afe1c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PIZ3LU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGw8Koqnrjtk7yaJdI2xuA6QVmboyVBLs4yuLN6%2BT5kCAiEAlzNI1zMrGwKSaNKydu6TG%2B5egPzP%2B6lBG%2B8LDD2PZ0UqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVSG8bQ%2BA0l4vWgIircA9PdEqfXxU5%2FTsRLmNZ5lvFz3DRQIQYGnC0HI4dDAH3wl0tfPEnAXa6LgumvzLL7Db%2B0wydXAVhyLSAlsAVqv4%2B%2BjaL4DToO1iZGenDmJHZqtlDS4C%2FUI3sa0R7gStwttPLQnqTLW%2B90id60ca%2FWKvNMIOoYV%2Bs5OcjiydNzC3IX0DkOf0%2BKwuZWk1PlHbYxjrPl3qfU%2BC%2BH4M58hJBaqLIb8kk5tC%2F158rqTEmE4zxf6duZJtr2iU9xFCyKNKOH%2BRhYLC%2Fw2WfZBwT5Y7RDE%2FWZpaT0jBjf6vFxccKz1KINjcifColK69WTgp6N7C1AJbEiyOcLECPr18zUc50MMRbfrEIOgmt0WqCROXFY%2B46mVCZyL%2FBcJyA2NP57SlUJTp48Kor3g6hC5ulD7UIZ439WBfcqKgwUXOesR2NqZz%2FP7TXkYc9Hoci6VQ%2BeZi5yJl595fKmo6AtTrplPEq48wCwn1CsB4zZPSTvcbcDm2mL4ueBiCyW8p0lIImQd8RXLImX98XvwKX1RBW7gVu0zL%2FyG6SNtlk0Fl9vAl3Z05xlXm8sigmVwstDJWpFPn1bBaLvPIUfNZOoz2ORlH8P9tblOBC0X7rmbwQU1cgEchEwT6IzEoDPq80wD64rMP%2BEnb0GOqUBI9u8%2FKMRxpFwSvbjIkc%2BJppG0s%2FCjFtx9yZ0abhPaI3FP%2BcAe8BTDNTPpb%2FLnyN3Idn%2FSmEEuu%2FAybPm%2BkdAPprg5gJJOK7zFcAP9HVxnwaAh5EQO%2FF7iJQUt5cr2bYQkLQAyC4E%2BJiE44KfzYtuH%2B65urJpHltXQMjOxgdwFSr35KJJqDm2ZITO4UnpnFVhhBCNxSlUd3X%2FRV6laZglPBx3amHM&X-Amz-Signature=dbe31ade37b4498cf45c622009f689f6644a44ef74106cea3ad445338c6ef11d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PIZ3LU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGw8Koqnrjtk7yaJdI2xuA6QVmboyVBLs4yuLN6%2BT5kCAiEAlzNI1zMrGwKSaNKydu6TG%2B5egPzP%2B6lBG%2B8LDD2PZ0UqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVSG8bQ%2BA0l4vWgIircA9PdEqfXxU5%2FTsRLmNZ5lvFz3DRQIQYGnC0HI4dDAH3wl0tfPEnAXa6LgumvzLL7Db%2B0wydXAVhyLSAlsAVqv4%2B%2BjaL4DToO1iZGenDmJHZqtlDS4C%2FUI3sa0R7gStwttPLQnqTLW%2B90id60ca%2FWKvNMIOoYV%2Bs5OcjiydNzC3IX0DkOf0%2BKwuZWk1PlHbYxjrPl3qfU%2BC%2BH4M58hJBaqLIb8kk5tC%2F158rqTEmE4zxf6duZJtr2iU9xFCyKNKOH%2BRhYLC%2Fw2WfZBwT5Y7RDE%2FWZpaT0jBjf6vFxccKz1KINjcifColK69WTgp6N7C1AJbEiyOcLECPr18zUc50MMRbfrEIOgmt0WqCROXFY%2B46mVCZyL%2FBcJyA2NP57SlUJTp48Kor3g6hC5ulD7UIZ439WBfcqKgwUXOesR2NqZz%2FP7TXkYc9Hoci6VQ%2BeZi5yJl595fKmo6AtTrplPEq48wCwn1CsB4zZPSTvcbcDm2mL4ueBiCyW8p0lIImQd8RXLImX98XvwKX1RBW7gVu0zL%2FyG6SNtlk0Fl9vAl3Z05xlXm8sigmVwstDJWpFPn1bBaLvPIUfNZOoz2ORlH8P9tblOBC0X7rmbwQU1cgEchEwT6IzEoDPq80wD64rMP%2BEnb0GOqUBI9u8%2FKMRxpFwSvbjIkc%2BJppG0s%2FCjFtx9yZ0abhPaI3FP%2BcAe8BTDNTPpb%2FLnyN3Idn%2FSmEEuu%2FAybPm%2BkdAPprg5gJJOK7zFcAP9HVxnwaAh5EQO%2FF7iJQUt5cr2bYQkLQAyC4E%2BJiE44KfzYtuH%2B65urJpHltXQMjOxgdwFSr35KJJqDm2ZITO4UnpnFVhhBCNxSlUd3X%2FRV6laZglPBx3amHM&X-Amz-Signature=4defc79cc6899bb72e96f64ae11cb3544f4e13f402270c050d5c74bb6bbe7d56&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PIZ3LU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGw8Koqnrjtk7yaJdI2xuA6QVmboyVBLs4yuLN6%2BT5kCAiEAlzNI1zMrGwKSaNKydu6TG%2B5egPzP%2B6lBG%2B8LDD2PZ0UqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVSG8bQ%2BA0l4vWgIircA9PdEqfXxU5%2FTsRLmNZ5lvFz3DRQIQYGnC0HI4dDAH3wl0tfPEnAXa6LgumvzLL7Db%2B0wydXAVhyLSAlsAVqv4%2B%2BjaL4DToO1iZGenDmJHZqtlDS4C%2FUI3sa0R7gStwttPLQnqTLW%2B90id60ca%2FWKvNMIOoYV%2Bs5OcjiydNzC3IX0DkOf0%2BKwuZWk1PlHbYxjrPl3qfU%2BC%2BH4M58hJBaqLIb8kk5tC%2F158rqTEmE4zxf6duZJtr2iU9xFCyKNKOH%2BRhYLC%2Fw2WfZBwT5Y7RDE%2FWZpaT0jBjf6vFxccKz1KINjcifColK69WTgp6N7C1AJbEiyOcLECPr18zUc50MMRbfrEIOgmt0WqCROXFY%2B46mVCZyL%2FBcJyA2NP57SlUJTp48Kor3g6hC5ulD7UIZ439WBfcqKgwUXOesR2NqZz%2FP7TXkYc9Hoci6VQ%2BeZi5yJl595fKmo6AtTrplPEq48wCwn1CsB4zZPSTvcbcDm2mL4ueBiCyW8p0lIImQd8RXLImX98XvwKX1RBW7gVu0zL%2FyG6SNtlk0Fl9vAl3Z05xlXm8sigmVwstDJWpFPn1bBaLvPIUfNZOoz2ORlH8P9tblOBC0X7rmbwQU1cgEchEwT6IzEoDPq80wD64rMP%2BEnb0GOqUBI9u8%2FKMRxpFwSvbjIkc%2BJppG0s%2FCjFtx9yZ0abhPaI3FP%2BcAe8BTDNTPpb%2FLnyN3Idn%2FSmEEuu%2FAybPm%2BkdAPprg5gJJOK7zFcAP9HVxnwaAh5EQO%2FF7iJQUt5cr2bYQkLQAyC4E%2BJiE44KfzYtuH%2B65urJpHltXQMjOxgdwFSr35KJJqDm2ZITO4UnpnFVhhBCNxSlUd3X%2FRV6laZglPBx3amHM&X-Amz-Signature=eb38caf43904398e6562758e118e14e26c2791a2c962a1ca3de9266447c3caaa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TACVVCDW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDY%2FKn1aGARHYg%2F4BRT0haQugML4R55aVaCZMPGm6W2RgIgX0AHJ7t3zQJQF%2Br7q5xO%2BEPitJkzFf9dqjOUyPIx1RIqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJksy2%2FWbH6AogXZtyrcAxw6ebalHolu75obtt0xUi9yjyxkV0b%2FnGgreeb26oAiIC2s0Y1tCgAw8qUeiH3InSqIAVV07wL48Ity8Ld5aSd81eqoFLZBTZ3iqpPFEr2Mq6Hn3oBD5N4De3oWG%2Fcuf87Qi%2BE5I8Bt1njEoYcFb99i%2B5N2tCtOAyi4eP25wQQxSPmyvNeWOt2%2FGFskZMy7FvyISQYTnYQmuB%2FgNnf%2BsW%2Fs6E9N4MjF9%2FsKly0dILiD6hKKpZn%2F1HI0zWalgufyAH%2BT2C3%2BCGd0mvmRebycQbu6hlEDU32ZjqyMNsEZEebL5N%2BXktcYt4nkjiYwpxMQCBXjWVCXMZg9XcPLWDrMZgoB4dIKuUWnMbw0BWmUQqoyO7frTMjClarpX2PK2app%2Bs7K6wAnXjhhTI7nU3p2y2d3X7VV1BHPq%2BHRATgegSbCw3mZhCHAxvn8lqfGKIcBcH09Nmln9EwZkxPQpnxNULi2GTuj3z3otCQljcpcHtKpjuwaCrKwLPnr8DdDxpOjweNCX7TuA7LlawF%2Fbhn3PfxchPgcAd7dPjP0EmA4hzKKKJ1ufCTXa1feWlrYBQVl1GPRWChM%2B3EmkXkR2XvaT5dL2QZmXaNZBUi3LZJyUomSgh2SKiqF3QfiZLTLMMGFnb0GOqUBjV8YEbq1QgVqlVnZrBiQ4E76L2CvbTDzpVen0%2F2WwB1XY9cTyvbaOLIVvsBEj%2B4KDOdooxTvQyCUz2II975IweGRqCvahteWpI%2FaYgxUPWqzj%2FESFyJKhdxluQaZI4WE4jWF1eNyZyZgr91a0AanqEbw8QiNfZCZXqoK8Ct6BHg9ulMfc%2BvyHo%2FEfwY6EWeFaiw7Cic%2Frl9LsmRAHvOHprZBYnMk&X-Amz-Signature=589d08f26d1b7f30d2e6558b9f09c9c45106baa29bc0c23263ca5c0b12d15106&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TACVVCDW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDY%2FKn1aGARHYg%2F4BRT0haQugML4R55aVaCZMPGm6W2RgIgX0AHJ7t3zQJQF%2Br7q5xO%2BEPitJkzFf9dqjOUyPIx1RIqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJksy2%2FWbH6AogXZtyrcAxw6ebalHolu75obtt0xUi9yjyxkV0b%2FnGgreeb26oAiIC2s0Y1tCgAw8qUeiH3InSqIAVV07wL48Ity8Ld5aSd81eqoFLZBTZ3iqpPFEr2Mq6Hn3oBD5N4De3oWG%2Fcuf87Qi%2BE5I8Bt1njEoYcFb99i%2B5N2tCtOAyi4eP25wQQxSPmyvNeWOt2%2FGFskZMy7FvyISQYTnYQmuB%2FgNnf%2BsW%2Fs6E9N4MjF9%2FsKly0dILiD6hKKpZn%2F1HI0zWalgufyAH%2BT2C3%2BCGd0mvmRebycQbu6hlEDU32ZjqyMNsEZEebL5N%2BXktcYt4nkjiYwpxMQCBXjWVCXMZg9XcPLWDrMZgoB4dIKuUWnMbw0BWmUQqoyO7frTMjClarpX2PK2app%2Bs7K6wAnXjhhTI7nU3p2y2d3X7VV1BHPq%2BHRATgegSbCw3mZhCHAxvn8lqfGKIcBcH09Nmln9EwZkxPQpnxNULi2GTuj3z3otCQljcpcHtKpjuwaCrKwLPnr8DdDxpOjweNCX7TuA7LlawF%2Fbhn3PfxchPgcAd7dPjP0EmA4hzKKKJ1ufCTXa1feWlrYBQVl1GPRWChM%2B3EmkXkR2XvaT5dL2QZmXaNZBUi3LZJyUomSgh2SKiqF3QfiZLTLMMGFnb0GOqUBjV8YEbq1QgVqlVnZrBiQ4E76L2CvbTDzpVen0%2F2WwB1XY9cTyvbaOLIVvsBEj%2B4KDOdooxTvQyCUz2II975IweGRqCvahteWpI%2FaYgxUPWqzj%2FESFyJKhdxluQaZI4WE4jWF1eNyZyZgr91a0AanqEbw8QiNfZCZXqoK8Ct6BHg9ulMfc%2BvyHo%2FEfwY6EWeFaiw7Cic%2Frl9LsmRAHvOHprZBYnMk&X-Amz-Signature=c3f20df4c96e9553022b4695dfd3cfed332983399d0221f3742315b4da3169b7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
