

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDVS4UD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDwMxGEz6QJ5%2FudlpRw1VNWSaMXphX14a%2FU4f%2BGfBKhJwIhAOqUKsM5EGVBPMm2YzQsFbnCxaV42OgTKpC4BWgV7BhRKv8DCCsQABoMNjM3NDIzMTgzODA1IgyGIIZ7ZbgvD0pf8MYq3AMu9d6Rbm%2BOdyJnfQmAyQ6c3jFhm1BxSedNIuKXexPh%2F%2FmP7dI4JV9pf7eud8SQNyYeYZjC7IkAxzuRLttbQTU5bQ5g43fEjfNJxmAlqB7vXXbMe2NJALb%2FzhZloXMpgU0DJg6yu1LujZYn9LXi5%2B0q52k1wKNQtxunNIF1Xj11l3vUfP4LX8w1IyFSHceqr5BaJsybx3Oed5PchnAhL0N8ztlW04X03yR2FQAwd1jQB2YbjsdxxDqlOkDuVaTz9frRyEuxjhyeS2Hmgw9rScb1QTUmDBWtuKiNMHWaPsv5m6D2COsR%2ByUtyRSa4biEJZ%2FgAQ%2BaguLYKeN4rmb6Fvu5xSx%2Fz8r3bd6ZZsaSnIJTPK18L0wCGXcQfwIhbtAssMGstcnRStKj3ns6WvRu6y5A1MbSVWH16p6x40kopaBkMW1t%2BPlXDLv778GqAwwMbhcZQuu8q6rqPqkk62AP08Qc4U7FVaTtqoTy3PvPqDIrL6%2BpW4cTH9ilba3cj7h%2FAZbMXzneXoeUyExS6xFs3NlWdPi3KlyOmjvQ7n52E%2B6F3w%2FUJZCjmi%2BDhhRWtiHeLSH0FSvfn1d%2BfmGJwu4U6rwWJjjtnDdgRLxbZrs5yFFUlVzyWpaq78yffilORzDbyoe9BjqkAZvXsCcIz1QwJoj5b4XhlbBZRkOZUFW0%2BqXfFNw65Bd57OKLfPxYEnUcCKMM%2B4lZ29KmcTqR6IBIwp8yb6QFIsRoO5RFH5JmpLdkKIhtqw95X0aHI0Hi9gAu1v69uf3hntRoRpwsK7PHKwTxMXi0Dow5NpJh4jsXAVcNjEjUU15juKsrfcPen8lmAfGs62FlsXQHezXjQzJ2zIKlURD8RUF1a7xR&X-Amz-Signature=ea7699dc984e5484fed0e2d14b769bd0f9f45ead82c24f0c79ad859fc0019daf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDVS4UD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDwMxGEz6QJ5%2FudlpRw1VNWSaMXphX14a%2FU4f%2BGfBKhJwIhAOqUKsM5EGVBPMm2YzQsFbnCxaV42OgTKpC4BWgV7BhRKv8DCCsQABoMNjM3NDIzMTgzODA1IgyGIIZ7ZbgvD0pf8MYq3AMu9d6Rbm%2BOdyJnfQmAyQ6c3jFhm1BxSedNIuKXexPh%2F%2FmP7dI4JV9pf7eud8SQNyYeYZjC7IkAxzuRLttbQTU5bQ5g43fEjfNJxmAlqB7vXXbMe2NJALb%2FzhZloXMpgU0DJg6yu1LujZYn9LXi5%2B0q52k1wKNQtxunNIF1Xj11l3vUfP4LX8w1IyFSHceqr5BaJsybx3Oed5PchnAhL0N8ztlW04X03yR2FQAwd1jQB2YbjsdxxDqlOkDuVaTz9frRyEuxjhyeS2Hmgw9rScb1QTUmDBWtuKiNMHWaPsv5m6D2COsR%2ByUtyRSa4biEJZ%2FgAQ%2BaguLYKeN4rmb6Fvu5xSx%2Fz8r3bd6ZZsaSnIJTPK18L0wCGXcQfwIhbtAssMGstcnRStKj3ns6WvRu6y5A1MbSVWH16p6x40kopaBkMW1t%2BPlXDLv778GqAwwMbhcZQuu8q6rqPqkk62AP08Qc4U7FVaTtqoTy3PvPqDIrL6%2BpW4cTH9ilba3cj7h%2FAZbMXzneXoeUyExS6xFs3NlWdPi3KlyOmjvQ7n52E%2B6F3w%2FUJZCjmi%2BDhhRWtiHeLSH0FSvfn1d%2BfmGJwu4U6rwWJjjtnDdgRLxbZrs5yFFUlVzyWpaq78yffilORzDbyoe9BjqkAZvXsCcIz1QwJoj5b4XhlbBZRkOZUFW0%2BqXfFNw65Bd57OKLfPxYEnUcCKMM%2B4lZ29KmcTqR6IBIwp8yb6QFIsRoO5RFH5JmpLdkKIhtqw95X0aHI0Hi9gAu1v69uf3hntRoRpwsK7PHKwTxMXi0Dow5NpJh4jsXAVcNjEjUU15juKsrfcPen8lmAfGs62FlsXQHezXjQzJ2zIKlURD8RUF1a7xR&X-Amz-Signature=884391cec061379918232d193316a01e1bba5db75681d377f908d545c60e2c73&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDVS4UD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDwMxGEz6QJ5%2FudlpRw1VNWSaMXphX14a%2FU4f%2BGfBKhJwIhAOqUKsM5EGVBPMm2YzQsFbnCxaV42OgTKpC4BWgV7BhRKv8DCCsQABoMNjM3NDIzMTgzODA1IgyGIIZ7ZbgvD0pf8MYq3AMu9d6Rbm%2BOdyJnfQmAyQ6c3jFhm1BxSedNIuKXexPh%2F%2FmP7dI4JV9pf7eud8SQNyYeYZjC7IkAxzuRLttbQTU5bQ5g43fEjfNJxmAlqB7vXXbMe2NJALb%2FzhZloXMpgU0DJg6yu1LujZYn9LXi5%2B0q52k1wKNQtxunNIF1Xj11l3vUfP4LX8w1IyFSHceqr5BaJsybx3Oed5PchnAhL0N8ztlW04X03yR2FQAwd1jQB2YbjsdxxDqlOkDuVaTz9frRyEuxjhyeS2Hmgw9rScb1QTUmDBWtuKiNMHWaPsv5m6D2COsR%2ByUtyRSa4biEJZ%2FgAQ%2BaguLYKeN4rmb6Fvu5xSx%2Fz8r3bd6ZZsaSnIJTPK18L0wCGXcQfwIhbtAssMGstcnRStKj3ns6WvRu6y5A1MbSVWH16p6x40kopaBkMW1t%2BPlXDLv778GqAwwMbhcZQuu8q6rqPqkk62AP08Qc4U7FVaTtqoTy3PvPqDIrL6%2BpW4cTH9ilba3cj7h%2FAZbMXzneXoeUyExS6xFs3NlWdPi3KlyOmjvQ7n52E%2B6F3w%2FUJZCjmi%2BDhhRWtiHeLSH0FSvfn1d%2BfmGJwu4U6rwWJjjtnDdgRLxbZrs5yFFUlVzyWpaq78yffilORzDbyoe9BjqkAZvXsCcIz1QwJoj5b4XhlbBZRkOZUFW0%2BqXfFNw65Bd57OKLfPxYEnUcCKMM%2B4lZ29KmcTqR6IBIwp8yb6QFIsRoO5RFH5JmpLdkKIhtqw95X0aHI0Hi9gAu1v69uf3hntRoRpwsK7PHKwTxMXi0Dow5NpJh4jsXAVcNjEjUU15juKsrfcPen8lmAfGs62FlsXQHezXjQzJ2zIKlURD8RUF1a7xR&X-Amz-Signature=dd557cf31362e85704bf6fbe75da948fff263cf25314c24db2c9bb1ff8c4e725&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDVS4UD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDwMxGEz6QJ5%2FudlpRw1VNWSaMXphX14a%2FU4f%2BGfBKhJwIhAOqUKsM5EGVBPMm2YzQsFbnCxaV42OgTKpC4BWgV7BhRKv8DCCsQABoMNjM3NDIzMTgzODA1IgyGIIZ7ZbgvD0pf8MYq3AMu9d6Rbm%2BOdyJnfQmAyQ6c3jFhm1BxSedNIuKXexPh%2F%2FmP7dI4JV9pf7eud8SQNyYeYZjC7IkAxzuRLttbQTU5bQ5g43fEjfNJxmAlqB7vXXbMe2NJALb%2FzhZloXMpgU0DJg6yu1LujZYn9LXi5%2B0q52k1wKNQtxunNIF1Xj11l3vUfP4LX8w1IyFSHceqr5BaJsybx3Oed5PchnAhL0N8ztlW04X03yR2FQAwd1jQB2YbjsdxxDqlOkDuVaTz9frRyEuxjhyeS2Hmgw9rScb1QTUmDBWtuKiNMHWaPsv5m6D2COsR%2ByUtyRSa4biEJZ%2FgAQ%2BaguLYKeN4rmb6Fvu5xSx%2Fz8r3bd6ZZsaSnIJTPK18L0wCGXcQfwIhbtAssMGstcnRStKj3ns6WvRu6y5A1MbSVWH16p6x40kopaBkMW1t%2BPlXDLv778GqAwwMbhcZQuu8q6rqPqkk62AP08Qc4U7FVaTtqoTy3PvPqDIrL6%2BpW4cTH9ilba3cj7h%2FAZbMXzneXoeUyExS6xFs3NlWdPi3KlyOmjvQ7n52E%2B6F3w%2FUJZCjmi%2BDhhRWtiHeLSH0FSvfn1d%2BfmGJwu4U6rwWJjjtnDdgRLxbZrs5yFFUlVzyWpaq78yffilORzDbyoe9BjqkAZvXsCcIz1QwJoj5b4XhlbBZRkOZUFW0%2BqXfFNw65Bd57OKLfPxYEnUcCKMM%2B4lZ29KmcTqR6IBIwp8yb6QFIsRoO5RFH5JmpLdkKIhtqw95X0aHI0Hi9gAu1v69uf3hntRoRpwsK7PHKwTxMXi0Dow5NpJh4jsXAVcNjEjUU15juKsrfcPen8lmAfGs62FlsXQHezXjQzJ2zIKlURD8RUF1a7xR&X-Amz-Signature=eb6784d4ec924d7707ed52c73e74600acaae8d4224019391d4025a8bccbf97f2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDVS4UD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDwMxGEz6QJ5%2FudlpRw1VNWSaMXphX14a%2FU4f%2BGfBKhJwIhAOqUKsM5EGVBPMm2YzQsFbnCxaV42OgTKpC4BWgV7BhRKv8DCCsQABoMNjM3NDIzMTgzODA1IgyGIIZ7ZbgvD0pf8MYq3AMu9d6Rbm%2BOdyJnfQmAyQ6c3jFhm1BxSedNIuKXexPh%2F%2FmP7dI4JV9pf7eud8SQNyYeYZjC7IkAxzuRLttbQTU5bQ5g43fEjfNJxmAlqB7vXXbMe2NJALb%2FzhZloXMpgU0DJg6yu1LujZYn9LXi5%2B0q52k1wKNQtxunNIF1Xj11l3vUfP4LX8w1IyFSHceqr5BaJsybx3Oed5PchnAhL0N8ztlW04X03yR2FQAwd1jQB2YbjsdxxDqlOkDuVaTz9frRyEuxjhyeS2Hmgw9rScb1QTUmDBWtuKiNMHWaPsv5m6D2COsR%2ByUtyRSa4biEJZ%2FgAQ%2BaguLYKeN4rmb6Fvu5xSx%2Fz8r3bd6ZZsaSnIJTPK18L0wCGXcQfwIhbtAssMGstcnRStKj3ns6WvRu6y5A1MbSVWH16p6x40kopaBkMW1t%2BPlXDLv778GqAwwMbhcZQuu8q6rqPqkk62AP08Qc4U7FVaTtqoTy3PvPqDIrL6%2BpW4cTH9ilba3cj7h%2FAZbMXzneXoeUyExS6xFs3NlWdPi3KlyOmjvQ7n52E%2B6F3w%2FUJZCjmi%2BDhhRWtiHeLSH0FSvfn1d%2BfmGJwu4U6rwWJjjtnDdgRLxbZrs5yFFUlVzyWpaq78yffilORzDbyoe9BjqkAZvXsCcIz1QwJoj5b4XhlbBZRkOZUFW0%2BqXfFNw65Bd57OKLfPxYEnUcCKMM%2B4lZ29KmcTqR6IBIwp8yb6QFIsRoO5RFH5JmpLdkKIhtqw95X0aHI0Hi9gAu1v69uf3hntRoRpwsK7PHKwTxMXi0Dow5NpJh4jsXAVcNjEjUU15juKsrfcPen8lmAfGs62FlsXQHezXjQzJ2zIKlURD8RUF1a7xR&X-Amz-Signature=7597ef78a5b8abf9d4ea48af33f73a74e3716f3f9e41849ab1a90abf4450382f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDVS4UD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDwMxGEz6QJ5%2FudlpRw1VNWSaMXphX14a%2FU4f%2BGfBKhJwIhAOqUKsM5EGVBPMm2YzQsFbnCxaV42OgTKpC4BWgV7BhRKv8DCCsQABoMNjM3NDIzMTgzODA1IgyGIIZ7ZbgvD0pf8MYq3AMu9d6Rbm%2BOdyJnfQmAyQ6c3jFhm1BxSedNIuKXexPh%2F%2FmP7dI4JV9pf7eud8SQNyYeYZjC7IkAxzuRLttbQTU5bQ5g43fEjfNJxmAlqB7vXXbMe2NJALb%2FzhZloXMpgU0DJg6yu1LujZYn9LXi5%2B0q52k1wKNQtxunNIF1Xj11l3vUfP4LX8w1IyFSHceqr5BaJsybx3Oed5PchnAhL0N8ztlW04X03yR2FQAwd1jQB2YbjsdxxDqlOkDuVaTz9frRyEuxjhyeS2Hmgw9rScb1QTUmDBWtuKiNMHWaPsv5m6D2COsR%2ByUtyRSa4biEJZ%2FgAQ%2BaguLYKeN4rmb6Fvu5xSx%2Fz8r3bd6ZZsaSnIJTPK18L0wCGXcQfwIhbtAssMGstcnRStKj3ns6WvRu6y5A1MbSVWH16p6x40kopaBkMW1t%2BPlXDLv778GqAwwMbhcZQuu8q6rqPqkk62AP08Qc4U7FVaTtqoTy3PvPqDIrL6%2BpW4cTH9ilba3cj7h%2FAZbMXzneXoeUyExS6xFs3NlWdPi3KlyOmjvQ7n52E%2B6F3w%2FUJZCjmi%2BDhhRWtiHeLSH0FSvfn1d%2BfmGJwu4U6rwWJjjtnDdgRLxbZrs5yFFUlVzyWpaq78yffilORzDbyoe9BjqkAZvXsCcIz1QwJoj5b4XhlbBZRkOZUFW0%2BqXfFNw65Bd57OKLfPxYEnUcCKMM%2B4lZ29KmcTqR6IBIwp8yb6QFIsRoO5RFH5JmpLdkKIhtqw95X0aHI0Hi9gAu1v69uf3hntRoRpwsK7PHKwTxMXi0Dow5NpJh4jsXAVcNjEjUU15juKsrfcPen8lmAfGs62FlsXQHezXjQzJ2zIKlURD8RUF1a7xR&X-Amz-Signature=1f5456c1a9f95e224b97bc03a951edb07445f4df0fb16fe4c0a704901993dc25&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDVS4UD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDwMxGEz6QJ5%2FudlpRw1VNWSaMXphX14a%2FU4f%2BGfBKhJwIhAOqUKsM5EGVBPMm2YzQsFbnCxaV42OgTKpC4BWgV7BhRKv8DCCsQABoMNjM3NDIzMTgzODA1IgyGIIZ7ZbgvD0pf8MYq3AMu9d6Rbm%2BOdyJnfQmAyQ6c3jFhm1BxSedNIuKXexPh%2F%2FmP7dI4JV9pf7eud8SQNyYeYZjC7IkAxzuRLttbQTU5bQ5g43fEjfNJxmAlqB7vXXbMe2NJALb%2FzhZloXMpgU0DJg6yu1LujZYn9LXi5%2B0q52k1wKNQtxunNIF1Xj11l3vUfP4LX8w1IyFSHceqr5BaJsybx3Oed5PchnAhL0N8ztlW04X03yR2FQAwd1jQB2YbjsdxxDqlOkDuVaTz9frRyEuxjhyeS2Hmgw9rScb1QTUmDBWtuKiNMHWaPsv5m6D2COsR%2ByUtyRSa4biEJZ%2FgAQ%2BaguLYKeN4rmb6Fvu5xSx%2Fz8r3bd6ZZsaSnIJTPK18L0wCGXcQfwIhbtAssMGstcnRStKj3ns6WvRu6y5A1MbSVWH16p6x40kopaBkMW1t%2BPlXDLv778GqAwwMbhcZQuu8q6rqPqkk62AP08Qc4U7FVaTtqoTy3PvPqDIrL6%2BpW4cTH9ilba3cj7h%2FAZbMXzneXoeUyExS6xFs3NlWdPi3KlyOmjvQ7n52E%2B6F3w%2FUJZCjmi%2BDhhRWtiHeLSH0FSvfn1d%2BfmGJwu4U6rwWJjjtnDdgRLxbZrs5yFFUlVzyWpaq78yffilORzDbyoe9BjqkAZvXsCcIz1QwJoj5b4XhlbBZRkOZUFW0%2BqXfFNw65Bd57OKLfPxYEnUcCKMM%2B4lZ29KmcTqR6IBIwp8yb6QFIsRoO5RFH5JmpLdkKIhtqw95X0aHI0Hi9gAu1v69uf3hntRoRpwsK7PHKwTxMXi0Dow5NpJh4jsXAVcNjEjUU15juKsrfcPen8lmAfGs62FlsXQHezXjQzJ2zIKlURD8RUF1a7xR&X-Amz-Signature=23ad11c0c7edcff6ea8e9263ad381af7f9503048dd3d7dbf255047c683d7ea7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDVS4UD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDwMxGEz6QJ5%2FudlpRw1VNWSaMXphX14a%2FU4f%2BGfBKhJwIhAOqUKsM5EGVBPMm2YzQsFbnCxaV42OgTKpC4BWgV7BhRKv8DCCsQABoMNjM3NDIzMTgzODA1IgyGIIZ7ZbgvD0pf8MYq3AMu9d6Rbm%2BOdyJnfQmAyQ6c3jFhm1BxSedNIuKXexPh%2F%2FmP7dI4JV9pf7eud8SQNyYeYZjC7IkAxzuRLttbQTU5bQ5g43fEjfNJxmAlqB7vXXbMe2NJALb%2FzhZloXMpgU0DJg6yu1LujZYn9LXi5%2B0q52k1wKNQtxunNIF1Xj11l3vUfP4LX8w1IyFSHceqr5BaJsybx3Oed5PchnAhL0N8ztlW04X03yR2FQAwd1jQB2YbjsdxxDqlOkDuVaTz9frRyEuxjhyeS2Hmgw9rScb1QTUmDBWtuKiNMHWaPsv5m6D2COsR%2ByUtyRSa4biEJZ%2FgAQ%2BaguLYKeN4rmb6Fvu5xSx%2Fz8r3bd6ZZsaSnIJTPK18L0wCGXcQfwIhbtAssMGstcnRStKj3ns6WvRu6y5A1MbSVWH16p6x40kopaBkMW1t%2BPlXDLv778GqAwwMbhcZQuu8q6rqPqkk62AP08Qc4U7FVaTtqoTy3PvPqDIrL6%2BpW4cTH9ilba3cj7h%2FAZbMXzneXoeUyExS6xFs3NlWdPi3KlyOmjvQ7n52E%2B6F3w%2FUJZCjmi%2BDhhRWtiHeLSH0FSvfn1d%2BfmGJwu4U6rwWJjjtnDdgRLxbZrs5yFFUlVzyWpaq78yffilORzDbyoe9BjqkAZvXsCcIz1QwJoj5b4XhlbBZRkOZUFW0%2BqXfFNw65Bd57OKLfPxYEnUcCKMM%2B4lZ29KmcTqR6IBIwp8yb6QFIsRoO5RFH5JmpLdkKIhtqw95X0aHI0Hi9gAu1v69uf3hntRoRpwsK7PHKwTxMXi0Dow5NpJh4jsXAVcNjEjUU15juKsrfcPen8lmAfGs62FlsXQHezXjQzJ2zIKlURD8RUF1a7xR&X-Amz-Signature=61d9023238b803cbe23be727ea9040c59314d0263f01c0519bf2da0c97b2a1dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDVS4UD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDwMxGEz6QJ5%2FudlpRw1VNWSaMXphX14a%2FU4f%2BGfBKhJwIhAOqUKsM5EGVBPMm2YzQsFbnCxaV42OgTKpC4BWgV7BhRKv8DCCsQABoMNjM3NDIzMTgzODA1IgyGIIZ7ZbgvD0pf8MYq3AMu9d6Rbm%2BOdyJnfQmAyQ6c3jFhm1BxSedNIuKXexPh%2F%2FmP7dI4JV9pf7eud8SQNyYeYZjC7IkAxzuRLttbQTU5bQ5g43fEjfNJxmAlqB7vXXbMe2NJALb%2FzhZloXMpgU0DJg6yu1LujZYn9LXi5%2B0q52k1wKNQtxunNIF1Xj11l3vUfP4LX8w1IyFSHceqr5BaJsybx3Oed5PchnAhL0N8ztlW04X03yR2FQAwd1jQB2YbjsdxxDqlOkDuVaTz9frRyEuxjhyeS2Hmgw9rScb1QTUmDBWtuKiNMHWaPsv5m6D2COsR%2ByUtyRSa4biEJZ%2FgAQ%2BaguLYKeN4rmb6Fvu5xSx%2Fz8r3bd6ZZsaSnIJTPK18L0wCGXcQfwIhbtAssMGstcnRStKj3ns6WvRu6y5A1MbSVWH16p6x40kopaBkMW1t%2BPlXDLv778GqAwwMbhcZQuu8q6rqPqkk62AP08Qc4U7FVaTtqoTy3PvPqDIrL6%2BpW4cTH9ilba3cj7h%2FAZbMXzneXoeUyExS6xFs3NlWdPi3KlyOmjvQ7n52E%2B6F3w%2FUJZCjmi%2BDhhRWtiHeLSH0FSvfn1d%2BfmGJwu4U6rwWJjjtnDdgRLxbZrs5yFFUlVzyWpaq78yffilORzDbyoe9BjqkAZvXsCcIz1QwJoj5b4XhlbBZRkOZUFW0%2BqXfFNw65Bd57OKLfPxYEnUcCKMM%2B4lZ29KmcTqR6IBIwp8yb6QFIsRoO5RFH5JmpLdkKIhtqw95X0aHI0Hi9gAu1v69uf3hntRoRpwsK7PHKwTxMXi0Dow5NpJh4jsXAVcNjEjUU15juKsrfcPen8lmAfGs62FlsXQHezXjQzJ2zIKlURD8RUF1a7xR&X-Amz-Signature=1d4323581bd82bb1dec8625264b3ae17f02b4d1057b81b40b61ea848645c82b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DRO6TAT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIFjKE2I4ntSssjY3T5oWaerktknJsBE%2Fl8LqjbIvfsrWAiAxbrl%2BgDAQO337071IAT8vEc5sqeIUIh83oW28fTsBUyr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMv6xlkPwXOteLpuEiKtwDzCcF%2B3ABgxV0h4DjVn7HlRsnOYyPLBXnRokFdBL68GubXMwx0L23G3R4mMGc0lFmNFjNEz2DzV8saiIJXsQNj5owkTuR64zPAfOCCT4auwo2kz%2Fme0yVUxCclaW0U%2BMfMekSIJe0x%2Bwpk95wN%2Bja9VsfjKM5rvdWZHkIsAxMmHTF4B0ilik6eTrEiJsS8UKjZrhZaH%2FF5qQ2HKcmlTKF%2BD7YgDLRay1mUmoBtdRFwsyRu5uIttH4ChBGNtY%2F7Vyhjc%2BkmwNlgLUNZH4UVjQHVTeus6xJ8M0QBi9CWmQCDEKjlTxau3iz%2Fdzrtuji0bwPlxpNQOpSiE3kRMkrYjfc812Ums89YXoMfsGHfkCNedTB9t%2BCO11NKHS55kdYn6D%2Bb9Qa0zc7%2FYIMhJe1Yu1EqrTfbzEl6hFarIK9iZ2DPb37WdOzED%2FkvRrnvR88542HXu518DYCPa%2B%2FWf3B3BgBry6IUGhL3mByOQ6zmrPLrumFJEUcSnQQp5aII4YBioaf8o4oYdFtzG6k%2Bx9t3DRdiJ0raw9ub0o96wF6dTIo6Y4l1Pn65dtqctBB4TBzbOdRlOjqRQHJJwXirunAv2da5is1bX9GPuF9zn7g9JnImU87QbLlt%2F4vH1oT7H4whsqHvQY6pgE8fU%2BbX0Kq0u%2BBhW59%2F%2Fr2FrId3PfV1Lz48%2BYwwnCjjDy%2FUpJ1vpdEbfLYgXIkNgIWg%2BVEeaSnHCsRnx1GWIXd5KZ3468YsnU%2FeWJYOcP5oDyBEqOuygTkPp176%2BmJt%2BZGgbtJ0ytRT%2BGOulmyjT5cP9E2VvuPS%2FPWaGtj4b8WPimhWTGrqO69FmUwrNHsJMxRFVzK5COoBmNnPmkFWuYY7Hv2x2xc&X-Amz-Signature=aec0ecaf8d41c3debb7c1abf5526e791f89899d9fb48f730e3059bbaa58dcaee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DRO6TAT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIFjKE2I4ntSssjY3T5oWaerktknJsBE%2Fl8LqjbIvfsrWAiAxbrl%2BgDAQO337071IAT8vEc5sqeIUIh83oW28fTsBUyr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMv6xlkPwXOteLpuEiKtwDzCcF%2B3ABgxV0h4DjVn7HlRsnOYyPLBXnRokFdBL68GubXMwx0L23G3R4mMGc0lFmNFjNEz2DzV8saiIJXsQNj5owkTuR64zPAfOCCT4auwo2kz%2Fme0yVUxCclaW0U%2BMfMekSIJe0x%2Bwpk95wN%2Bja9VsfjKM5rvdWZHkIsAxMmHTF4B0ilik6eTrEiJsS8UKjZrhZaH%2FF5qQ2HKcmlTKF%2BD7YgDLRay1mUmoBtdRFwsyRu5uIttH4ChBGNtY%2F7Vyhjc%2BkmwNlgLUNZH4UVjQHVTeus6xJ8M0QBi9CWmQCDEKjlTxau3iz%2Fdzrtuji0bwPlxpNQOpSiE3kRMkrYjfc812Ums89YXoMfsGHfkCNedTB9t%2BCO11NKHS55kdYn6D%2Bb9Qa0zc7%2FYIMhJe1Yu1EqrTfbzEl6hFarIK9iZ2DPb37WdOzED%2FkvRrnvR88542HXu518DYCPa%2B%2FWf3B3BgBry6IUGhL3mByOQ6zmrPLrumFJEUcSnQQp5aII4YBioaf8o4oYdFtzG6k%2Bx9t3DRdiJ0raw9ub0o96wF6dTIo6Y4l1Pn65dtqctBB4TBzbOdRlOjqRQHJJwXirunAv2da5is1bX9GPuF9zn7g9JnImU87QbLlt%2F4vH1oT7H4whsqHvQY6pgE8fU%2BbX0Kq0u%2BBhW59%2F%2Fr2FrId3PfV1Lz48%2BYwwnCjjDy%2FUpJ1vpdEbfLYgXIkNgIWg%2BVEeaSnHCsRnx1GWIXd5KZ3468YsnU%2FeWJYOcP5oDyBEqOuygTkPp176%2BmJt%2BZGgbtJ0ytRT%2BGOulmyjT5cP9E2VvuPS%2FPWaGtj4b8WPimhWTGrqO69FmUwrNHsJMxRFVzK5COoBmNnPmkFWuYY7Hv2x2xc&X-Amz-Signature=deb6aecc1c8cc3cab00b837a476fb98901d0e3676c72b7ba1db34deac1da78b1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
