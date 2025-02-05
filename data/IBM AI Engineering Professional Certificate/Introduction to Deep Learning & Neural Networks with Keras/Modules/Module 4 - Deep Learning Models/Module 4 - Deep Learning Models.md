

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZQQPYN2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCQwAX%2FIy831k7HLsbQmtzCE01C0nqPsOjuwHEErKF82QIgJdrrcp9GmfNZ4MVBGy9iTfXZXusLNSlC8AXEZ06uHrkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAvcKLhCbgqtsdg%2BzyrcAzyaK7Qlp7QJMnDCmPztiolHcHHXO59lLqVbG%2BE%2FYfX1ZowXrJPG36pcf4oH5UyLIjV1aIe7IKkH4gJJBcklrXKteEQDroaPAnguj1XY1xSEWw6%2BHf%2FQ75A7cSNyjr7mRxDaKMW8fote3lPuZ5C9oRtJsJqPGbMJJsDFw2OKb8KSEubOtqkeDwaKfGk3GYoNIYRx0PER7Z3xRXcntdKVZDVdeyMpWycdQfHAxW1cyrQwMicD4W9y3ACNfFPtccfrAJM0fmeip%2F7S9JsP0hUhBk5pZ8bU5kP%2F1bVv7uz2vA3DNGpEk9WKayyiXNXKpMZSDe6SKyEN21hIIzcEFwv0wQp5eL%2FP7PUfptypw73pXELaa5rCxciS%2BzX%2F29kN5OV9DdladbqH5CgcNUynxjAbmOOXtlWrKceypCJWngV1QbhAr5zlh6%2Fk3nfzdQz5KB4CB9OCK54LxSZnS%2BdA4vajl%2B2gz9U%2FH5WV4qb3s7a4LQlP%2B3TkALE55VPmIxI73ZtB%2BwVCOpc7w2GFMg4POS4VVGKTy3qZDfncktcAvz2RLpNdnqo0ScFloRgV14zD7CuVjHQMNMUm3sKkpDCGwrxDVsxypAhHR6i4IgGjRX5pt1%2FWMwuPDh7YfUmIkBlZMO66jr0GOqUBc%2BjdxMaKW4apsZuKJLJ41fnIhYj%2BpPP745TSqHbmeVUhcZKdgkPvxXAmjzszo4W61%2BFyQ8G2rPw2uLkcsvaONIvNKYuNHR357KN3C7B7YuYoF%2FM9AlRPdPbnlb2d%2BjTmkx0FwbeeO2zM1POWqkt4uO3d3lq2HJnxX3%2FAK%2FoRlC3B4rVm%2FYqawZ8wpuGSQMXl%2FRTWmX9DqZrigA6PAp3WvPVdmLYS&X-Amz-Signature=ccdcaa21c0ec791d622684533f1b3a30303664a0453df05d3cb6526b5c6c8e4a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZQQPYN2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCQwAX%2FIy831k7HLsbQmtzCE01C0nqPsOjuwHEErKF82QIgJdrrcp9GmfNZ4MVBGy9iTfXZXusLNSlC8AXEZ06uHrkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAvcKLhCbgqtsdg%2BzyrcAzyaK7Qlp7QJMnDCmPztiolHcHHXO59lLqVbG%2BE%2FYfX1ZowXrJPG36pcf4oH5UyLIjV1aIe7IKkH4gJJBcklrXKteEQDroaPAnguj1XY1xSEWw6%2BHf%2FQ75A7cSNyjr7mRxDaKMW8fote3lPuZ5C9oRtJsJqPGbMJJsDFw2OKb8KSEubOtqkeDwaKfGk3GYoNIYRx0PER7Z3xRXcntdKVZDVdeyMpWycdQfHAxW1cyrQwMicD4W9y3ACNfFPtccfrAJM0fmeip%2F7S9JsP0hUhBk5pZ8bU5kP%2F1bVv7uz2vA3DNGpEk9WKayyiXNXKpMZSDe6SKyEN21hIIzcEFwv0wQp5eL%2FP7PUfptypw73pXELaa5rCxciS%2BzX%2F29kN5OV9DdladbqH5CgcNUynxjAbmOOXtlWrKceypCJWngV1QbhAr5zlh6%2Fk3nfzdQz5KB4CB9OCK54LxSZnS%2BdA4vajl%2B2gz9U%2FH5WV4qb3s7a4LQlP%2B3TkALE55VPmIxI73ZtB%2BwVCOpc7w2GFMg4POS4VVGKTy3qZDfncktcAvz2RLpNdnqo0ScFloRgV14zD7CuVjHQMNMUm3sKkpDCGwrxDVsxypAhHR6i4IgGjRX5pt1%2FWMwuPDh7YfUmIkBlZMO66jr0GOqUBc%2BjdxMaKW4apsZuKJLJ41fnIhYj%2BpPP745TSqHbmeVUhcZKdgkPvxXAmjzszo4W61%2BFyQ8G2rPw2uLkcsvaONIvNKYuNHR357KN3C7B7YuYoF%2FM9AlRPdPbnlb2d%2BjTmkx0FwbeeO2zM1POWqkt4uO3d3lq2HJnxX3%2FAK%2FoRlC3B4rVm%2FYqawZ8wpuGSQMXl%2FRTWmX9DqZrigA6PAp3WvPVdmLYS&X-Amz-Signature=20b8867fc2bd4a485361acfd995b01054fd877b23ffb025adc60d1f21e77eeff&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZQQPYN2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCQwAX%2FIy831k7HLsbQmtzCE01C0nqPsOjuwHEErKF82QIgJdrrcp9GmfNZ4MVBGy9iTfXZXusLNSlC8AXEZ06uHrkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAvcKLhCbgqtsdg%2BzyrcAzyaK7Qlp7QJMnDCmPztiolHcHHXO59lLqVbG%2BE%2FYfX1ZowXrJPG36pcf4oH5UyLIjV1aIe7IKkH4gJJBcklrXKteEQDroaPAnguj1XY1xSEWw6%2BHf%2FQ75A7cSNyjr7mRxDaKMW8fote3lPuZ5C9oRtJsJqPGbMJJsDFw2OKb8KSEubOtqkeDwaKfGk3GYoNIYRx0PER7Z3xRXcntdKVZDVdeyMpWycdQfHAxW1cyrQwMicD4W9y3ACNfFPtccfrAJM0fmeip%2F7S9JsP0hUhBk5pZ8bU5kP%2F1bVv7uz2vA3DNGpEk9WKayyiXNXKpMZSDe6SKyEN21hIIzcEFwv0wQp5eL%2FP7PUfptypw73pXELaa5rCxciS%2BzX%2F29kN5OV9DdladbqH5CgcNUynxjAbmOOXtlWrKceypCJWngV1QbhAr5zlh6%2Fk3nfzdQz5KB4CB9OCK54LxSZnS%2BdA4vajl%2B2gz9U%2FH5WV4qb3s7a4LQlP%2B3TkALE55VPmIxI73ZtB%2BwVCOpc7w2GFMg4POS4VVGKTy3qZDfncktcAvz2RLpNdnqo0ScFloRgV14zD7CuVjHQMNMUm3sKkpDCGwrxDVsxypAhHR6i4IgGjRX5pt1%2FWMwuPDh7YfUmIkBlZMO66jr0GOqUBc%2BjdxMaKW4apsZuKJLJ41fnIhYj%2BpPP745TSqHbmeVUhcZKdgkPvxXAmjzszo4W61%2BFyQ8G2rPw2uLkcsvaONIvNKYuNHR357KN3C7B7YuYoF%2FM9AlRPdPbnlb2d%2BjTmkx0FwbeeO2zM1POWqkt4uO3d3lq2HJnxX3%2FAK%2FoRlC3B4rVm%2FYqawZ8wpuGSQMXl%2FRTWmX9DqZrigA6PAp3WvPVdmLYS&X-Amz-Signature=e45077a6d2694b65462045ffb32826b620fc60dafdd9d023087136e3ca054791&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZQQPYN2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCQwAX%2FIy831k7HLsbQmtzCE01C0nqPsOjuwHEErKF82QIgJdrrcp9GmfNZ4MVBGy9iTfXZXusLNSlC8AXEZ06uHrkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAvcKLhCbgqtsdg%2BzyrcAzyaK7Qlp7QJMnDCmPztiolHcHHXO59lLqVbG%2BE%2FYfX1ZowXrJPG36pcf4oH5UyLIjV1aIe7IKkH4gJJBcklrXKteEQDroaPAnguj1XY1xSEWw6%2BHf%2FQ75A7cSNyjr7mRxDaKMW8fote3lPuZ5C9oRtJsJqPGbMJJsDFw2OKb8KSEubOtqkeDwaKfGk3GYoNIYRx0PER7Z3xRXcntdKVZDVdeyMpWycdQfHAxW1cyrQwMicD4W9y3ACNfFPtccfrAJM0fmeip%2F7S9JsP0hUhBk5pZ8bU5kP%2F1bVv7uz2vA3DNGpEk9WKayyiXNXKpMZSDe6SKyEN21hIIzcEFwv0wQp5eL%2FP7PUfptypw73pXELaa5rCxciS%2BzX%2F29kN5OV9DdladbqH5CgcNUynxjAbmOOXtlWrKceypCJWngV1QbhAr5zlh6%2Fk3nfzdQz5KB4CB9OCK54LxSZnS%2BdA4vajl%2B2gz9U%2FH5WV4qb3s7a4LQlP%2B3TkALE55VPmIxI73ZtB%2BwVCOpc7w2GFMg4POS4VVGKTy3qZDfncktcAvz2RLpNdnqo0ScFloRgV14zD7CuVjHQMNMUm3sKkpDCGwrxDVsxypAhHR6i4IgGjRX5pt1%2FWMwuPDh7YfUmIkBlZMO66jr0GOqUBc%2BjdxMaKW4apsZuKJLJ41fnIhYj%2BpPP745TSqHbmeVUhcZKdgkPvxXAmjzszo4W61%2BFyQ8G2rPw2uLkcsvaONIvNKYuNHR357KN3C7B7YuYoF%2FM9AlRPdPbnlb2d%2BjTmkx0FwbeeO2zM1POWqkt4uO3d3lq2HJnxX3%2FAK%2FoRlC3B4rVm%2FYqawZ8wpuGSQMXl%2FRTWmX9DqZrigA6PAp3WvPVdmLYS&X-Amz-Signature=f118fb459b44957a33725d15920c3a3333936d8fe13e0a0edb02376ebcaf7c0f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZQQPYN2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCQwAX%2FIy831k7HLsbQmtzCE01C0nqPsOjuwHEErKF82QIgJdrrcp9GmfNZ4MVBGy9iTfXZXusLNSlC8AXEZ06uHrkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAvcKLhCbgqtsdg%2BzyrcAzyaK7Qlp7QJMnDCmPztiolHcHHXO59lLqVbG%2BE%2FYfX1ZowXrJPG36pcf4oH5UyLIjV1aIe7IKkH4gJJBcklrXKteEQDroaPAnguj1XY1xSEWw6%2BHf%2FQ75A7cSNyjr7mRxDaKMW8fote3lPuZ5C9oRtJsJqPGbMJJsDFw2OKb8KSEubOtqkeDwaKfGk3GYoNIYRx0PER7Z3xRXcntdKVZDVdeyMpWycdQfHAxW1cyrQwMicD4W9y3ACNfFPtccfrAJM0fmeip%2F7S9JsP0hUhBk5pZ8bU5kP%2F1bVv7uz2vA3DNGpEk9WKayyiXNXKpMZSDe6SKyEN21hIIzcEFwv0wQp5eL%2FP7PUfptypw73pXELaa5rCxciS%2BzX%2F29kN5OV9DdladbqH5CgcNUynxjAbmOOXtlWrKceypCJWngV1QbhAr5zlh6%2Fk3nfzdQz5KB4CB9OCK54LxSZnS%2BdA4vajl%2B2gz9U%2FH5WV4qb3s7a4LQlP%2B3TkALE55VPmIxI73ZtB%2BwVCOpc7w2GFMg4POS4VVGKTy3qZDfncktcAvz2RLpNdnqo0ScFloRgV14zD7CuVjHQMNMUm3sKkpDCGwrxDVsxypAhHR6i4IgGjRX5pt1%2FWMwuPDh7YfUmIkBlZMO66jr0GOqUBc%2BjdxMaKW4apsZuKJLJ41fnIhYj%2BpPP745TSqHbmeVUhcZKdgkPvxXAmjzszo4W61%2BFyQ8G2rPw2uLkcsvaONIvNKYuNHR357KN3C7B7YuYoF%2FM9AlRPdPbnlb2d%2BjTmkx0FwbeeO2zM1POWqkt4uO3d3lq2HJnxX3%2FAK%2FoRlC3B4rVm%2FYqawZ8wpuGSQMXl%2FRTWmX9DqZrigA6PAp3WvPVdmLYS&X-Amz-Signature=45af2d2b806bf1fd4ecbe0ccb486fb1faeeff7e1f9e4d978cfd19adfb5bd75ee&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZQQPYN2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCQwAX%2FIy831k7HLsbQmtzCE01C0nqPsOjuwHEErKF82QIgJdrrcp9GmfNZ4MVBGy9iTfXZXusLNSlC8AXEZ06uHrkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAvcKLhCbgqtsdg%2BzyrcAzyaK7Qlp7QJMnDCmPztiolHcHHXO59lLqVbG%2BE%2FYfX1ZowXrJPG36pcf4oH5UyLIjV1aIe7IKkH4gJJBcklrXKteEQDroaPAnguj1XY1xSEWw6%2BHf%2FQ75A7cSNyjr7mRxDaKMW8fote3lPuZ5C9oRtJsJqPGbMJJsDFw2OKb8KSEubOtqkeDwaKfGk3GYoNIYRx0PER7Z3xRXcntdKVZDVdeyMpWycdQfHAxW1cyrQwMicD4W9y3ACNfFPtccfrAJM0fmeip%2F7S9JsP0hUhBk5pZ8bU5kP%2F1bVv7uz2vA3DNGpEk9WKayyiXNXKpMZSDe6SKyEN21hIIzcEFwv0wQp5eL%2FP7PUfptypw73pXELaa5rCxciS%2BzX%2F29kN5OV9DdladbqH5CgcNUynxjAbmOOXtlWrKceypCJWngV1QbhAr5zlh6%2Fk3nfzdQz5KB4CB9OCK54LxSZnS%2BdA4vajl%2B2gz9U%2FH5WV4qb3s7a4LQlP%2B3TkALE55VPmIxI73ZtB%2BwVCOpc7w2GFMg4POS4VVGKTy3qZDfncktcAvz2RLpNdnqo0ScFloRgV14zD7CuVjHQMNMUm3sKkpDCGwrxDVsxypAhHR6i4IgGjRX5pt1%2FWMwuPDh7YfUmIkBlZMO66jr0GOqUBc%2BjdxMaKW4apsZuKJLJ41fnIhYj%2BpPP745TSqHbmeVUhcZKdgkPvxXAmjzszo4W61%2BFyQ8G2rPw2uLkcsvaONIvNKYuNHR357KN3C7B7YuYoF%2FM9AlRPdPbnlb2d%2BjTmkx0FwbeeO2zM1POWqkt4uO3d3lq2HJnxX3%2FAK%2FoRlC3B4rVm%2FYqawZ8wpuGSQMXl%2FRTWmX9DqZrigA6PAp3WvPVdmLYS&X-Amz-Signature=1cb87e8dfb25dfe6e68b92fc33f113234cfeee0036bd8f52c65d490521697c25&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZQQPYN2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCQwAX%2FIy831k7HLsbQmtzCE01C0nqPsOjuwHEErKF82QIgJdrrcp9GmfNZ4MVBGy9iTfXZXusLNSlC8AXEZ06uHrkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAvcKLhCbgqtsdg%2BzyrcAzyaK7Qlp7QJMnDCmPztiolHcHHXO59lLqVbG%2BE%2FYfX1ZowXrJPG36pcf4oH5UyLIjV1aIe7IKkH4gJJBcklrXKteEQDroaPAnguj1XY1xSEWw6%2BHf%2FQ75A7cSNyjr7mRxDaKMW8fote3lPuZ5C9oRtJsJqPGbMJJsDFw2OKb8KSEubOtqkeDwaKfGk3GYoNIYRx0PER7Z3xRXcntdKVZDVdeyMpWycdQfHAxW1cyrQwMicD4W9y3ACNfFPtccfrAJM0fmeip%2F7S9JsP0hUhBk5pZ8bU5kP%2F1bVv7uz2vA3DNGpEk9WKayyiXNXKpMZSDe6SKyEN21hIIzcEFwv0wQp5eL%2FP7PUfptypw73pXELaa5rCxciS%2BzX%2F29kN5OV9DdladbqH5CgcNUynxjAbmOOXtlWrKceypCJWngV1QbhAr5zlh6%2Fk3nfzdQz5KB4CB9OCK54LxSZnS%2BdA4vajl%2B2gz9U%2FH5WV4qb3s7a4LQlP%2B3TkALE55VPmIxI73ZtB%2BwVCOpc7w2GFMg4POS4VVGKTy3qZDfncktcAvz2RLpNdnqo0ScFloRgV14zD7CuVjHQMNMUm3sKkpDCGwrxDVsxypAhHR6i4IgGjRX5pt1%2FWMwuPDh7YfUmIkBlZMO66jr0GOqUBc%2BjdxMaKW4apsZuKJLJ41fnIhYj%2BpPP745TSqHbmeVUhcZKdgkPvxXAmjzszo4W61%2BFyQ8G2rPw2uLkcsvaONIvNKYuNHR357KN3C7B7YuYoF%2FM9AlRPdPbnlb2d%2BjTmkx0FwbeeO2zM1POWqkt4uO3d3lq2HJnxX3%2FAK%2FoRlC3B4rVm%2FYqawZ8wpuGSQMXl%2FRTWmX9DqZrigA6PAp3WvPVdmLYS&X-Amz-Signature=4a157a233e0ef8186eac24988875cdcd60098c382f3ea3518743a9a6880325d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZQQPYN2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCQwAX%2FIy831k7HLsbQmtzCE01C0nqPsOjuwHEErKF82QIgJdrrcp9GmfNZ4MVBGy9iTfXZXusLNSlC8AXEZ06uHrkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAvcKLhCbgqtsdg%2BzyrcAzyaK7Qlp7QJMnDCmPztiolHcHHXO59lLqVbG%2BE%2FYfX1ZowXrJPG36pcf4oH5UyLIjV1aIe7IKkH4gJJBcklrXKteEQDroaPAnguj1XY1xSEWw6%2BHf%2FQ75A7cSNyjr7mRxDaKMW8fote3lPuZ5C9oRtJsJqPGbMJJsDFw2OKb8KSEubOtqkeDwaKfGk3GYoNIYRx0PER7Z3xRXcntdKVZDVdeyMpWycdQfHAxW1cyrQwMicD4W9y3ACNfFPtccfrAJM0fmeip%2F7S9JsP0hUhBk5pZ8bU5kP%2F1bVv7uz2vA3DNGpEk9WKayyiXNXKpMZSDe6SKyEN21hIIzcEFwv0wQp5eL%2FP7PUfptypw73pXELaa5rCxciS%2BzX%2F29kN5OV9DdladbqH5CgcNUynxjAbmOOXtlWrKceypCJWngV1QbhAr5zlh6%2Fk3nfzdQz5KB4CB9OCK54LxSZnS%2BdA4vajl%2B2gz9U%2FH5WV4qb3s7a4LQlP%2B3TkALE55VPmIxI73ZtB%2BwVCOpc7w2GFMg4POS4VVGKTy3qZDfncktcAvz2RLpNdnqo0ScFloRgV14zD7CuVjHQMNMUm3sKkpDCGwrxDVsxypAhHR6i4IgGjRX5pt1%2FWMwuPDh7YfUmIkBlZMO66jr0GOqUBc%2BjdxMaKW4apsZuKJLJ41fnIhYj%2BpPP745TSqHbmeVUhcZKdgkPvxXAmjzszo4W61%2BFyQ8G2rPw2uLkcsvaONIvNKYuNHR357KN3C7B7YuYoF%2FM9AlRPdPbnlb2d%2BjTmkx0FwbeeO2zM1POWqkt4uO3d3lq2HJnxX3%2FAK%2FoRlC3B4rVm%2FYqawZ8wpuGSQMXl%2FRTWmX9DqZrigA6PAp3WvPVdmLYS&X-Amz-Signature=ae4e8b1c3082e2c36b229003038bb19e2c1a57154704eb2832d4c1375c9f0b25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZQQPYN2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCQwAX%2FIy831k7HLsbQmtzCE01C0nqPsOjuwHEErKF82QIgJdrrcp9GmfNZ4MVBGy9iTfXZXusLNSlC8AXEZ06uHrkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAvcKLhCbgqtsdg%2BzyrcAzyaK7Qlp7QJMnDCmPztiolHcHHXO59lLqVbG%2BE%2FYfX1ZowXrJPG36pcf4oH5UyLIjV1aIe7IKkH4gJJBcklrXKteEQDroaPAnguj1XY1xSEWw6%2BHf%2FQ75A7cSNyjr7mRxDaKMW8fote3lPuZ5C9oRtJsJqPGbMJJsDFw2OKb8KSEubOtqkeDwaKfGk3GYoNIYRx0PER7Z3xRXcntdKVZDVdeyMpWycdQfHAxW1cyrQwMicD4W9y3ACNfFPtccfrAJM0fmeip%2F7S9JsP0hUhBk5pZ8bU5kP%2F1bVv7uz2vA3DNGpEk9WKayyiXNXKpMZSDe6SKyEN21hIIzcEFwv0wQp5eL%2FP7PUfptypw73pXELaa5rCxciS%2BzX%2F29kN5OV9DdladbqH5CgcNUynxjAbmOOXtlWrKceypCJWngV1QbhAr5zlh6%2Fk3nfzdQz5KB4CB9OCK54LxSZnS%2BdA4vajl%2B2gz9U%2FH5WV4qb3s7a4LQlP%2B3TkALE55VPmIxI73ZtB%2BwVCOpc7w2GFMg4POS4VVGKTy3qZDfncktcAvz2RLpNdnqo0ScFloRgV14zD7CuVjHQMNMUm3sKkpDCGwrxDVsxypAhHR6i4IgGjRX5pt1%2FWMwuPDh7YfUmIkBlZMO66jr0GOqUBc%2BjdxMaKW4apsZuKJLJ41fnIhYj%2BpPP745TSqHbmeVUhcZKdgkPvxXAmjzszo4W61%2BFyQ8G2rPw2uLkcsvaONIvNKYuNHR357KN3C7B7YuYoF%2FM9AlRPdPbnlb2d%2BjTmkx0FwbeeO2zM1POWqkt4uO3d3lq2HJnxX3%2FAK%2FoRlC3B4rVm%2FYqawZ8wpuGSQMXl%2FRTWmX9DqZrigA6PAp3WvPVdmLYS&X-Amz-Signature=82ee099a71526554347b45e676aabb32d6d8e29e387c29dd61d1054e30cafef1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYXFCCWM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCvqTGtYrsg0PDGby9NOunruS3S7rW7QXQm8tt8hizX1QIhAIl5fIH%2BMZg7fKSsH9rJXzMsaZJFFIE9TNWPFmV6Od8RKv8DCEoQABoMNjM3NDIzMTgzODA1IgyLh1ol4tbb%2BSughvoq3AMVr8tdH2H4DWjGPLwlvygnyKe22mH2KcjH2YWww6QyLAilqd1QVGd%2Fc5kucP%2BtGlkzVkwwWsmNNAvedDXVomHpt5MnmTJ4qC7YaZSPYGu5rTTujG1UaOVrhsnDNuLzmMzoplrjDc04mVTGDOlqW4L1%2FZhmiRHsHI2Zv%2BH%2BKZIzvDYZd9Q%2F2lFAt3DBIuRE9KmtjDzpGnaLe5JNYOPPCRK%2FvXlxcPQBkoCxjlyjX%2BGV5MOu96pCrgZ3nTx7p6%2BIANgfN6b1xCEXTgH82EIPS0cRCHOWIJARQOvtACiMwAs4OC31oraOiIUbqWxcrD6mET9nljNzWW5WWH4L318%2FKWnZ0AeVKDtRrMOtdvVvuuZrAt0DMy3VER6kU4Y6wSo%2BSNKG6aq5jpfm0c2yx1jpKyRhuFM65dQQ%2F6rxwBVdZtgyXLzVLZEcejbU12265kH7TzkFBz4I4sSGxUV3Zxa1dfEjnRLAuTOu7tBPZh5QPawBubT8yeszjQUNgDMYncunBk7uHeKaNkrazY%2FfCa8XZmn001FhaVPi9%2Fhh5H0htw8uHl7KARpttekIPO0byb6h4%2BCaQxhIkdz7C9JFO%2BLUwQBYvKs8ghwsLJj4nruRfPETgqOgpD%2BvSfrdo%2BDScTCXuo69BjqkAamB%2FslaxA%2Fayu827sgZD09F9THBvBNK3IfYzBqih9SpE6OK8UW9f6m6zuAuXXHGo0pvfHzQhznPbPJXprJZG9JZkyJ3bad7ybYCt9JCKoZiwJ3%2BqUnmxwqKpY6G1QGloRQk5TlDKCMtzIHWv0ZVBFuQl%2Flg3hlPsFf8TlCDJ%2Fzt4E7KwKWF93gz8hzODa8MV7C6kx1pLs4aURj0jWBp9IKSQNQ5&X-Amz-Signature=169034c67e330fe26ec1dd9161f0a88c62c9f225ea6d9632281775543d54abba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYXFCCWM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCvqTGtYrsg0PDGby9NOunruS3S7rW7QXQm8tt8hizX1QIhAIl5fIH%2BMZg7fKSsH9rJXzMsaZJFFIE9TNWPFmV6Od8RKv8DCEoQABoMNjM3NDIzMTgzODA1IgyLh1ol4tbb%2BSughvoq3AMVr8tdH2H4DWjGPLwlvygnyKe22mH2KcjH2YWww6QyLAilqd1QVGd%2Fc5kucP%2BtGlkzVkwwWsmNNAvedDXVomHpt5MnmTJ4qC7YaZSPYGu5rTTujG1UaOVrhsnDNuLzmMzoplrjDc04mVTGDOlqW4L1%2FZhmiRHsHI2Zv%2BH%2BKZIzvDYZd9Q%2F2lFAt3DBIuRE9KmtjDzpGnaLe5JNYOPPCRK%2FvXlxcPQBkoCxjlyjX%2BGV5MOu96pCrgZ3nTx7p6%2BIANgfN6b1xCEXTgH82EIPS0cRCHOWIJARQOvtACiMwAs4OC31oraOiIUbqWxcrD6mET9nljNzWW5WWH4L318%2FKWnZ0AeVKDtRrMOtdvVvuuZrAt0DMy3VER6kU4Y6wSo%2BSNKG6aq5jpfm0c2yx1jpKyRhuFM65dQQ%2F6rxwBVdZtgyXLzVLZEcejbU12265kH7TzkFBz4I4sSGxUV3Zxa1dfEjnRLAuTOu7tBPZh5QPawBubT8yeszjQUNgDMYncunBk7uHeKaNkrazY%2FfCa8XZmn001FhaVPi9%2Fhh5H0htw8uHl7KARpttekIPO0byb6h4%2BCaQxhIkdz7C9JFO%2BLUwQBYvKs8ghwsLJj4nruRfPETgqOgpD%2BvSfrdo%2BDScTCXuo69BjqkAamB%2FslaxA%2Fayu827sgZD09F9THBvBNK3IfYzBqih9SpE6OK8UW9f6m6zuAuXXHGo0pvfHzQhznPbPJXprJZG9JZkyJ3bad7ybYCt9JCKoZiwJ3%2BqUnmxwqKpY6G1QGloRQk5TlDKCMtzIHWv0ZVBFuQl%2Flg3hlPsFf8TlCDJ%2Fzt4E7KwKWF93gz8hzODa8MV7C6kx1pLs4aURj0jWBp9IKSQNQ5&X-Amz-Signature=3d6195555285d828f3712126c787ce61c031d8bbb8c3f8d535f4aa49b19bf1b6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
