

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663657VFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQC03X0jiSXMyVFaVv0r69sr6XwERtlGL7CchCkYMt6%2BPwIgXn3SaegFEa48w9O2%2FBI8tPyb8hB04d5nz5wZv7RxEiUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDA%2FXpdcfDmxcNB74PSrcA%2BbMsBm2gSVvUyzz%2Bb%2BoKpwsJ6vSbfC8BYQX1QE32Bc6hF8zThWOyByXrvU3PeeKpEvvwmfaOhOeFIsVEQRzJrcLAwQ87vT0GJSxkF4zV%2B%2FXtBA%2FTCHV%2Brwdtb8lPms9p0pnAOWHxmKnB0kKPCKa7ib%2Bv9kWQxD1XvzTL5KT6LQc2lPjEjXeS7BEqsA2YLs2EQ%2BUeSDQcHLylaHX8Yl4Uqj8Z7RaxE4ac44eQ45ewLrCDeap9hAReL865ubTRM0hto%2BswV73dT1SQZVNwiBcw64cBS%2BtxWpRN2Gl7FWSXvNCENgVMyluDxkMbkh%2BXHlc6y78qvYUzr4981jtk3jK35uzOw9gIRNTMSzQYJyqv5DFw%2BX4EElc48aB6u6M2aP9Z42jOaGIb%2FwPJyoplDAP15%2FZ86PAYAzpynzkAY0wVZtX8UnjsgkOK201U7ghjPMCFFMf0mYVRcl3kOeQASW8wDkrG%2FgH19ZtJlZ5uRN0LhiHAB%2Fdky0iaa5qAZMC%2Fqfi93J0lDO7po4e2q4nAdV%2BmV4bTd4gxMXPHFjMLiUegRe9i0l6npw0B5SZl2HAfrw5CbtjmYkrcazPLGre0I3E5FmEnU1o6WTYVzXNbUvsrtLPyRT9Tu8Ia2GgpIu7MK6WjL0GOqUB7VvBoRy8lbCFycyYXkxPYqGHr5aRqh6TqMa9iOvXN8eBhflLBz98bjuX5EnTPHFXsS2WqXHWkLMfv7glbh4NzH8vn6y%2F8Ymm%2Bk8XVhdeMT1ZkIL0povglxMTlKrIELmUHEGRgW8CobyMJOnGIxAqW02j1a72DchL6nG%2BVT2MlYiZYR0YqF8VOieorjkPDxhs16a0dIvBSzs%2FD86%2FDoUGxAz8OHGM&X-Amz-Signature=e0fd5a29da07ad763b05c9ba64fdd21f3d071adce73e5cd3c2f241292ec8ae4f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663657VFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQC03X0jiSXMyVFaVv0r69sr6XwERtlGL7CchCkYMt6%2BPwIgXn3SaegFEa48w9O2%2FBI8tPyb8hB04d5nz5wZv7RxEiUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDA%2FXpdcfDmxcNB74PSrcA%2BbMsBm2gSVvUyzz%2Bb%2BoKpwsJ6vSbfC8BYQX1QE32Bc6hF8zThWOyByXrvU3PeeKpEvvwmfaOhOeFIsVEQRzJrcLAwQ87vT0GJSxkF4zV%2B%2FXtBA%2FTCHV%2Brwdtb8lPms9p0pnAOWHxmKnB0kKPCKa7ib%2Bv9kWQxD1XvzTL5KT6LQc2lPjEjXeS7BEqsA2YLs2EQ%2BUeSDQcHLylaHX8Yl4Uqj8Z7RaxE4ac44eQ45ewLrCDeap9hAReL865ubTRM0hto%2BswV73dT1SQZVNwiBcw64cBS%2BtxWpRN2Gl7FWSXvNCENgVMyluDxkMbkh%2BXHlc6y78qvYUzr4981jtk3jK35uzOw9gIRNTMSzQYJyqv5DFw%2BX4EElc48aB6u6M2aP9Z42jOaGIb%2FwPJyoplDAP15%2FZ86PAYAzpynzkAY0wVZtX8UnjsgkOK201U7ghjPMCFFMf0mYVRcl3kOeQASW8wDkrG%2FgH19ZtJlZ5uRN0LhiHAB%2Fdky0iaa5qAZMC%2Fqfi93J0lDO7po4e2q4nAdV%2BmV4bTd4gxMXPHFjMLiUegRe9i0l6npw0B5SZl2HAfrw5CbtjmYkrcazPLGre0I3E5FmEnU1o6WTYVzXNbUvsrtLPyRT9Tu8Ia2GgpIu7MK6WjL0GOqUB7VvBoRy8lbCFycyYXkxPYqGHr5aRqh6TqMa9iOvXN8eBhflLBz98bjuX5EnTPHFXsS2WqXHWkLMfv7glbh4NzH8vn6y%2F8Ymm%2Bk8XVhdeMT1ZkIL0povglxMTlKrIELmUHEGRgW8CobyMJOnGIxAqW02j1a72DchL6nG%2BVT2MlYiZYR0YqF8VOieorjkPDxhs16a0dIvBSzs%2FD86%2FDoUGxAz8OHGM&X-Amz-Signature=7d50014dcfd8440da81a9f7f05b43e81454bc11c6bee9db44fdf406e995f1170&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663657VFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQC03X0jiSXMyVFaVv0r69sr6XwERtlGL7CchCkYMt6%2BPwIgXn3SaegFEa48w9O2%2FBI8tPyb8hB04d5nz5wZv7RxEiUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDA%2FXpdcfDmxcNB74PSrcA%2BbMsBm2gSVvUyzz%2Bb%2BoKpwsJ6vSbfC8BYQX1QE32Bc6hF8zThWOyByXrvU3PeeKpEvvwmfaOhOeFIsVEQRzJrcLAwQ87vT0GJSxkF4zV%2B%2FXtBA%2FTCHV%2Brwdtb8lPms9p0pnAOWHxmKnB0kKPCKa7ib%2Bv9kWQxD1XvzTL5KT6LQc2lPjEjXeS7BEqsA2YLs2EQ%2BUeSDQcHLylaHX8Yl4Uqj8Z7RaxE4ac44eQ45ewLrCDeap9hAReL865ubTRM0hto%2BswV73dT1SQZVNwiBcw64cBS%2BtxWpRN2Gl7FWSXvNCENgVMyluDxkMbkh%2BXHlc6y78qvYUzr4981jtk3jK35uzOw9gIRNTMSzQYJyqv5DFw%2BX4EElc48aB6u6M2aP9Z42jOaGIb%2FwPJyoplDAP15%2FZ86PAYAzpynzkAY0wVZtX8UnjsgkOK201U7ghjPMCFFMf0mYVRcl3kOeQASW8wDkrG%2FgH19ZtJlZ5uRN0LhiHAB%2Fdky0iaa5qAZMC%2Fqfi93J0lDO7po4e2q4nAdV%2BmV4bTd4gxMXPHFjMLiUegRe9i0l6npw0B5SZl2HAfrw5CbtjmYkrcazPLGre0I3E5FmEnU1o6WTYVzXNbUvsrtLPyRT9Tu8Ia2GgpIu7MK6WjL0GOqUB7VvBoRy8lbCFycyYXkxPYqGHr5aRqh6TqMa9iOvXN8eBhflLBz98bjuX5EnTPHFXsS2WqXHWkLMfv7glbh4NzH8vn6y%2F8Ymm%2Bk8XVhdeMT1ZkIL0povglxMTlKrIELmUHEGRgW8CobyMJOnGIxAqW02j1a72DchL6nG%2BVT2MlYiZYR0YqF8VOieorjkPDxhs16a0dIvBSzs%2FD86%2FDoUGxAz8OHGM&X-Amz-Signature=1ac9437e6a16b35ed079dbfe3e83423f9fdc68da203a6e59fc7a2c6149567960&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663657VFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQC03X0jiSXMyVFaVv0r69sr6XwERtlGL7CchCkYMt6%2BPwIgXn3SaegFEa48w9O2%2FBI8tPyb8hB04d5nz5wZv7RxEiUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDA%2FXpdcfDmxcNB74PSrcA%2BbMsBm2gSVvUyzz%2Bb%2BoKpwsJ6vSbfC8BYQX1QE32Bc6hF8zThWOyByXrvU3PeeKpEvvwmfaOhOeFIsVEQRzJrcLAwQ87vT0GJSxkF4zV%2B%2FXtBA%2FTCHV%2Brwdtb8lPms9p0pnAOWHxmKnB0kKPCKa7ib%2Bv9kWQxD1XvzTL5KT6LQc2lPjEjXeS7BEqsA2YLs2EQ%2BUeSDQcHLylaHX8Yl4Uqj8Z7RaxE4ac44eQ45ewLrCDeap9hAReL865ubTRM0hto%2BswV73dT1SQZVNwiBcw64cBS%2BtxWpRN2Gl7FWSXvNCENgVMyluDxkMbkh%2BXHlc6y78qvYUzr4981jtk3jK35uzOw9gIRNTMSzQYJyqv5DFw%2BX4EElc48aB6u6M2aP9Z42jOaGIb%2FwPJyoplDAP15%2FZ86PAYAzpynzkAY0wVZtX8UnjsgkOK201U7ghjPMCFFMf0mYVRcl3kOeQASW8wDkrG%2FgH19ZtJlZ5uRN0LhiHAB%2Fdky0iaa5qAZMC%2Fqfi93J0lDO7po4e2q4nAdV%2BmV4bTd4gxMXPHFjMLiUegRe9i0l6npw0B5SZl2HAfrw5CbtjmYkrcazPLGre0I3E5FmEnU1o6WTYVzXNbUvsrtLPyRT9Tu8Ia2GgpIu7MK6WjL0GOqUB7VvBoRy8lbCFycyYXkxPYqGHr5aRqh6TqMa9iOvXN8eBhflLBz98bjuX5EnTPHFXsS2WqXHWkLMfv7glbh4NzH8vn6y%2F8Ymm%2Bk8XVhdeMT1ZkIL0povglxMTlKrIELmUHEGRgW8CobyMJOnGIxAqW02j1a72DchL6nG%2BVT2MlYiZYR0YqF8VOieorjkPDxhs16a0dIvBSzs%2FD86%2FDoUGxAz8OHGM&X-Amz-Signature=671b4df6f39a1cab6dcade728869373d1d7532b2764be68300300d00d367ee0d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663657VFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQC03X0jiSXMyVFaVv0r69sr6XwERtlGL7CchCkYMt6%2BPwIgXn3SaegFEa48w9O2%2FBI8tPyb8hB04d5nz5wZv7RxEiUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDA%2FXpdcfDmxcNB74PSrcA%2BbMsBm2gSVvUyzz%2Bb%2BoKpwsJ6vSbfC8BYQX1QE32Bc6hF8zThWOyByXrvU3PeeKpEvvwmfaOhOeFIsVEQRzJrcLAwQ87vT0GJSxkF4zV%2B%2FXtBA%2FTCHV%2Brwdtb8lPms9p0pnAOWHxmKnB0kKPCKa7ib%2Bv9kWQxD1XvzTL5KT6LQc2lPjEjXeS7BEqsA2YLs2EQ%2BUeSDQcHLylaHX8Yl4Uqj8Z7RaxE4ac44eQ45ewLrCDeap9hAReL865ubTRM0hto%2BswV73dT1SQZVNwiBcw64cBS%2BtxWpRN2Gl7FWSXvNCENgVMyluDxkMbkh%2BXHlc6y78qvYUzr4981jtk3jK35uzOw9gIRNTMSzQYJyqv5DFw%2BX4EElc48aB6u6M2aP9Z42jOaGIb%2FwPJyoplDAP15%2FZ86PAYAzpynzkAY0wVZtX8UnjsgkOK201U7ghjPMCFFMf0mYVRcl3kOeQASW8wDkrG%2FgH19ZtJlZ5uRN0LhiHAB%2Fdky0iaa5qAZMC%2Fqfi93J0lDO7po4e2q4nAdV%2BmV4bTd4gxMXPHFjMLiUegRe9i0l6npw0B5SZl2HAfrw5CbtjmYkrcazPLGre0I3E5FmEnU1o6WTYVzXNbUvsrtLPyRT9Tu8Ia2GgpIu7MK6WjL0GOqUB7VvBoRy8lbCFycyYXkxPYqGHr5aRqh6TqMa9iOvXN8eBhflLBz98bjuX5EnTPHFXsS2WqXHWkLMfv7glbh4NzH8vn6y%2F8Ymm%2Bk8XVhdeMT1ZkIL0povglxMTlKrIELmUHEGRgW8CobyMJOnGIxAqW02j1a72DchL6nG%2BVT2MlYiZYR0YqF8VOieorjkPDxhs16a0dIvBSzs%2FD86%2FDoUGxAz8OHGM&X-Amz-Signature=60fa896a260e4d22f73051384bf6d2f195b1b5a7acf8c7f56d34572df0f00016&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663657VFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQC03X0jiSXMyVFaVv0r69sr6XwERtlGL7CchCkYMt6%2BPwIgXn3SaegFEa48w9O2%2FBI8tPyb8hB04d5nz5wZv7RxEiUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDA%2FXpdcfDmxcNB74PSrcA%2BbMsBm2gSVvUyzz%2Bb%2BoKpwsJ6vSbfC8BYQX1QE32Bc6hF8zThWOyByXrvU3PeeKpEvvwmfaOhOeFIsVEQRzJrcLAwQ87vT0GJSxkF4zV%2B%2FXtBA%2FTCHV%2Brwdtb8lPms9p0pnAOWHxmKnB0kKPCKa7ib%2Bv9kWQxD1XvzTL5KT6LQc2lPjEjXeS7BEqsA2YLs2EQ%2BUeSDQcHLylaHX8Yl4Uqj8Z7RaxE4ac44eQ45ewLrCDeap9hAReL865ubTRM0hto%2BswV73dT1SQZVNwiBcw64cBS%2BtxWpRN2Gl7FWSXvNCENgVMyluDxkMbkh%2BXHlc6y78qvYUzr4981jtk3jK35uzOw9gIRNTMSzQYJyqv5DFw%2BX4EElc48aB6u6M2aP9Z42jOaGIb%2FwPJyoplDAP15%2FZ86PAYAzpynzkAY0wVZtX8UnjsgkOK201U7ghjPMCFFMf0mYVRcl3kOeQASW8wDkrG%2FgH19ZtJlZ5uRN0LhiHAB%2Fdky0iaa5qAZMC%2Fqfi93J0lDO7po4e2q4nAdV%2BmV4bTd4gxMXPHFjMLiUegRe9i0l6npw0B5SZl2HAfrw5CbtjmYkrcazPLGre0I3E5FmEnU1o6WTYVzXNbUvsrtLPyRT9Tu8Ia2GgpIu7MK6WjL0GOqUB7VvBoRy8lbCFycyYXkxPYqGHr5aRqh6TqMa9iOvXN8eBhflLBz98bjuX5EnTPHFXsS2WqXHWkLMfv7glbh4NzH8vn6y%2F8Ymm%2Bk8XVhdeMT1ZkIL0povglxMTlKrIELmUHEGRgW8CobyMJOnGIxAqW02j1a72DchL6nG%2BVT2MlYiZYR0YqF8VOieorjkPDxhs16a0dIvBSzs%2FD86%2FDoUGxAz8OHGM&X-Amz-Signature=8b0993b777a14dea93380a3c5f055de17d19dd9ddf8ac0872a24c0199b3bce5c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663657VFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQC03X0jiSXMyVFaVv0r69sr6XwERtlGL7CchCkYMt6%2BPwIgXn3SaegFEa48w9O2%2FBI8tPyb8hB04d5nz5wZv7RxEiUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDA%2FXpdcfDmxcNB74PSrcA%2BbMsBm2gSVvUyzz%2Bb%2BoKpwsJ6vSbfC8BYQX1QE32Bc6hF8zThWOyByXrvU3PeeKpEvvwmfaOhOeFIsVEQRzJrcLAwQ87vT0GJSxkF4zV%2B%2FXtBA%2FTCHV%2Brwdtb8lPms9p0pnAOWHxmKnB0kKPCKa7ib%2Bv9kWQxD1XvzTL5KT6LQc2lPjEjXeS7BEqsA2YLs2EQ%2BUeSDQcHLylaHX8Yl4Uqj8Z7RaxE4ac44eQ45ewLrCDeap9hAReL865ubTRM0hto%2BswV73dT1SQZVNwiBcw64cBS%2BtxWpRN2Gl7FWSXvNCENgVMyluDxkMbkh%2BXHlc6y78qvYUzr4981jtk3jK35uzOw9gIRNTMSzQYJyqv5DFw%2BX4EElc48aB6u6M2aP9Z42jOaGIb%2FwPJyoplDAP15%2FZ86PAYAzpynzkAY0wVZtX8UnjsgkOK201U7ghjPMCFFMf0mYVRcl3kOeQASW8wDkrG%2FgH19ZtJlZ5uRN0LhiHAB%2Fdky0iaa5qAZMC%2Fqfi93J0lDO7po4e2q4nAdV%2BmV4bTd4gxMXPHFjMLiUegRe9i0l6npw0B5SZl2HAfrw5CbtjmYkrcazPLGre0I3E5FmEnU1o6WTYVzXNbUvsrtLPyRT9Tu8Ia2GgpIu7MK6WjL0GOqUB7VvBoRy8lbCFycyYXkxPYqGHr5aRqh6TqMa9iOvXN8eBhflLBz98bjuX5EnTPHFXsS2WqXHWkLMfv7glbh4NzH8vn6y%2F8Ymm%2Bk8XVhdeMT1ZkIL0povglxMTlKrIELmUHEGRgW8CobyMJOnGIxAqW02j1a72DchL6nG%2BVT2MlYiZYR0YqF8VOieorjkPDxhs16a0dIvBSzs%2FD86%2FDoUGxAz8OHGM&X-Amz-Signature=7e68087771a4842a912a57eb8ae1c0ed950785992e8a6003aecf272aa8eaba48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663657VFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQC03X0jiSXMyVFaVv0r69sr6XwERtlGL7CchCkYMt6%2BPwIgXn3SaegFEa48w9O2%2FBI8tPyb8hB04d5nz5wZv7RxEiUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDA%2FXpdcfDmxcNB74PSrcA%2BbMsBm2gSVvUyzz%2Bb%2BoKpwsJ6vSbfC8BYQX1QE32Bc6hF8zThWOyByXrvU3PeeKpEvvwmfaOhOeFIsVEQRzJrcLAwQ87vT0GJSxkF4zV%2B%2FXtBA%2FTCHV%2Brwdtb8lPms9p0pnAOWHxmKnB0kKPCKa7ib%2Bv9kWQxD1XvzTL5KT6LQc2lPjEjXeS7BEqsA2YLs2EQ%2BUeSDQcHLylaHX8Yl4Uqj8Z7RaxE4ac44eQ45ewLrCDeap9hAReL865ubTRM0hto%2BswV73dT1SQZVNwiBcw64cBS%2BtxWpRN2Gl7FWSXvNCENgVMyluDxkMbkh%2BXHlc6y78qvYUzr4981jtk3jK35uzOw9gIRNTMSzQYJyqv5DFw%2BX4EElc48aB6u6M2aP9Z42jOaGIb%2FwPJyoplDAP15%2FZ86PAYAzpynzkAY0wVZtX8UnjsgkOK201U7ghjPMCFFMf0mYVRcl3kOeQASW8wDkrG%2FgH19ZtJlZ5uRN0LhiHAB%2Fdky0iaa5qAZMC%2Fqfi93J0lDO7po4e2q4nAdV%2BmV4bTd4gxMXPHFjMLiUegRe9i0l6npw0B5SZl2HAfrw5CbtjmYkrcazPLGre0I3E5FmEnU1o6WTYVzXNbUvsrtLPyRT9Tu8Ia2GgpIu7MK6WjL0GOqUB7VvBoRy8lbCFycyYXkxPYqGHr5aRqh6TqMa9iOvXN8eBhflLBz98bjuX5EnTPHFXsS2WqXHWkLMfv7glbh4NzH8vn6y%2F8Ymm%2Bk8XVhdeMT1ZkIL0povglxMTlKrIELmUHEGRgW8CobyMJOnGIxAqW02j1a72DchL6nG%2BVT2MlYiZYR0YqF8VOieorjkPDxhs16a0dIvBSzs%2FD86%2FDoUGxAz8OHGM&X-Amz-Signature=c39d1ce5af55ae9ba1cf51f562f0af35f3943d4029cc4fe6b94bfcd43c3a9ada&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663657VFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQC03X0jiSXMyVFaVv0r69sr6XwERtlGL7CchCkYMt6%2BPwIgXn3SaegFEa48w9O2%2FBI8tPyb8hB04d5nz5wZv7RxEiUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDA%2FXpdcfDmxcNB74PSrcA%2BbMsBm2gSVvUyzz%2Bb%2BoKpwsJ6vSbfC8BYQX1QE32Bc6hF8zThWOyByXrvU3PeeKpEvvwmfaOhOeFIsVEQRzJrcLAwQ87vT0GJSxkF4zV%2B%2FXtBA%2FTCHV%2Brwdtb8lPms9p0pnAOWHxmKnB0kKPCKa7ib%2Bv9kWQxD1XvzTL5KT6LQc2lPjEjXeS7BEqsA2YLs2EQ%2BUeSDQcHLylaHX8Yl4Uqj8Z7RaxE4ac44eQ45ewLrCDeap9hAReL865ubTRM0hto%2BswV73dT1SQZVNwiBcw64cBS%2BtxWpRN2Gl7FWSXvNCENgVMyluDxkMbkh%2BXHlc6y78qvYUzr4981jtk3jK35uzOw9gIRNTMSzQYJyqv5DFw%2BX4EElc48aB6u6M2aP9Z42jOaGIb%2FwPJyoplDAP15%2FZ86PAYAzpynzkAY0wVZtX8UnjsgkOK201U7ghjPMCFFMf0mYVRcl3kOeQASW8wDkrG%2FgH19ZtJlZ5uRN0LhiHAB%2Fdky0iaa5qAZMC%2Fqfi93J0lDO7po4e2q4nAdV%2BmV4bTd4gxMXPHFjMLiUegRe9i0l6npw0B5SZl2HAfrw5CbtjmYkrcazPLGre0I3E5FmEnU1o6WTYVzXNbUvsrtLPyRT9Tu8Ia2GgpIu7MK6WjL0GOqUB7VvBoRy8lbCFycyYXkxPYqGHr5aRqh6TqMa9iOvXN8eBhflLBz98bjuX5EnTPHFXsS2WqXHWkLMfv7glbh4NzH8vn6y%2F8Ymm%2Bk8XVhdeMT1ZkIL0povglxMTlKrIELmUHEGRgW8CobyMJOnGIxAqW02j1a72DchL6nG%2BVT2MlYiZYR0YqF8VOieorjkPDxhs16a0dIvBSzs%2FD86%2FDoUGxAz8OHGM&X-Amz-Signature=778265a2d4ac7882efd3477513c951d113e493ae0ffcd86b31470cf34c567879&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGYU6HB3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIFQR4MhLnUglhBx472cL49vnNDR9sj%2BjE3fClhcXnnC7AiAFbUtc7aybPwjMe523CsE6d0WnOHCbJofDiwOpbwgWZyr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMZA6gNkDTZwexmPRVKtwDWkPS7QSMx68z8qZmQ7yBGnxjtblhyIyY2WCFjZPCF3Xg7PKgeF6vODmFY9xjGgRarzrLvo22yhFFBe%2FGkUJ2eARiAoJaB1pEeWdLWzp%2BZiF%2BjvBX9g4aXZOl3TkP%2Bocdr2pLofXTwn%2Bp91J0OS%2F8XCgLoKze%2FzEczbRwBE2NYHc9HuGdI4n%2FgYo3PaTks4Fe7EHd6MioSxCcLQlfLmyPRQUGGDbSQ3%2FTkF2BmAtX6WuzyoXpTRz46%2F%2BiBdqh7uknZTNYneMJl8AAezy9LO1RiTAms2Txg8xbQO%2By1tN%2BzDv5VphESNDeeyXewWiYLPuMbPXoZJtWXUFJjSu7hjHbRbv5hCE19%2BLi7Epx78AxWye5sJPMM%2FOmfkzJla6E2PHFKmw7AP792B9gtfc%2FX9IQeTvM020zO4j8UE%2B0%2FXLETEGcUFZ1%2BW66443y%2FpyOATP0wztK%2BvygRSJzIo%2FPqjY9%2FL2sUj9dUY%2BQo8CWlpvJlLkQqZ5SP%2F3F%2Fg3BRUZ9xmYZ1ndxhlqJSfglW%2FIDF4mg9a8aAJADR3LMdmKuW3IQrxUSetYP%2FCEhlHdSL%2Fd7ZBR5R2YTABnFwlrj1LKhvX8vXvxq9nVDpppCrv2%2Bp3NVCg2uA%2BnycpmYpZ2%2FFMgwsJaMvQY6pgF2YlMe%2FwESD8S7SVZillhI%2BcanrA8Ay58Xp9KvmOff4BUY2AIeEynDuj96QzmCNuL9btfGxXfdgWfLWTFO9P%2FVsjV%2Bx7ban17p9lIOXaLOzDsV4UNM5SNeIu%2FwhZjIdSKrBB9WzfdoCrkn7zjYzL5%2BoCbZy8Z6U8V9LN7CAvcXJRGcR%2FGxvsJ6EZFVQ%2BgGrKQ4HmwdUoW1Dt9S9i9k8wCE%2F8jBQQIS&X-Amz-Signature=cc15090d47289b6822a38ba9b6ead8d3b17d0d97adccef081095fd9f4a5c2fb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGYU6HB3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIFQR4MhLnUglhBx472cL49vnNDR9sj%2BjE3fClhcXnnC7AiAFbUtc7aybPwjMe523CsE6d0WnOHCbJofDiwOpbwgWZyr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMZA6gNkDTZwexmPRVKtwDWkPS7QSMx68z8qZmQ7yBGnxjtblhyIyY2WCFjZPCF3Xg7PKgeF6vODmFY9xjGgRarzrLvo22yhFFBe%2FGkUJ2eARiAoJaB1pEeWdLWzp%2BZiF%2BjvBX9g4aXZOl3TkP%2Bocdr2pLofXTwn%2Bp91J0OS%2F8XCgLoKze%2FzEczbRwBE2NYHc9HuGdI4n%2FgYo3PaTks4Fe7EHd6MioSxCcLQlfLmyPRQUGGDbSQ3%2FTkF2BmAtX6WuzyoXpTRz46%2F%2BiBdqh7uknZTNYneMJl8AAezy9LO1RiTAms2Txg8xbQO%2By1tN%2BzDv5VphESNDeeyXewWiYLPuMbPXoZJtWXUFJjSu7hjHbRbv5hCE19%2BLi7Epx78AxWye5sJPMM%2FOmfkzJla6E2PHFKmw7AP792B9gtfc%2FX9IQeTvM020zO4j8UE%2B0%2FXLETEGcUFZ1%2BW66443y%2FpyOATP0wztK%2BvygRSJzIo%2FPqjY9%2FL2sUj9dUY%2BQo8CWlpvJlLkQqZ5SP%2F3F%2Fg3BRUZ9xmYZ1ndxhlqJSfglW%2FIDF4mg9a8aAJADR3LMdmKuW3IQrxUSetYP%2FCEhlHdSL%2Fd7ZBR5R2YTABnFwlrj1LKhvX8vXvxq9nVDpppCrv2%2Bp3NVCg2uA%2BnycpmYpZ2%2FFMgwsJaMvQY6pgF2YlMe%2FwESD8S7SVZillhI%2BcanrA8Ay58Xp9KvmOff4BUY2AIeEynDuj96QzmCNuL9btfGxXfdgWfLWTFO9P%2FVsjV%2Bx7ban17p9lIOXaLOzDsV4UNM5SNeIu%2FwhZjIdSKrBB9WzfdoCrkn7zjYzL5%2BoCbZy8Z6U8V9LN7CAvcXJRGcR%2FGxvsJ6EZFVQ%2BgGrKQ4HmwdUoW1Dt9S9i9k8wCE%2F8jBQQIS&X-Amz-Signature=7c32aebfc754741878d94097a4c938f764edbcc88d98c404c3900d50a69da5c9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
