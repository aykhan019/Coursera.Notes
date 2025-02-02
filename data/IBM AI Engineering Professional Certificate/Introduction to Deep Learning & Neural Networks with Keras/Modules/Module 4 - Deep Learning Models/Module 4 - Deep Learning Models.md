

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD3KQV46%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBR26IycBOWZRHWz3onMrjZIwdwNHgZh2YqyVcQvR5zsAiBalzVCtufXYvNx1DkrMn60SxIhrreRpXMw8V057hSI4yqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM810tp65975n3rJg9KtwDPr59t3%2B3A%2FDBIqIwLVvJPIg%2Fg9CNvPIBl%2FXhGeOmVAReJYDL3taeul4MjiHK4eKzZpmfmX8Jq52lOpByo%2Fqv0VroXEJs52FUTiZBtwbL5UpegMrY8AzAmgXWRAb5BSxWo4cwHDl53XmrlkmZJYAdxlrJMuyIGrlY54T%2BAtN7IE3MG9s7mvRW5GU8CoegzCkYWD6pERbS9TejLAW8p5c7HHxwYVZGkzRnC5jNsjNOHwNsi3Q8O%2Fs65q%2FuPdGae77mje7qggBubbHcpEWf9A%2F%2F%2Bzk976utsdkTzRPcH3nOi2chwGWotpYrY28XQp9I%2BykES%2BXWVUfseg56l8Bl9foby1qduU6DervAU64OGYf%2FvyNPz%2B%2B0663HIoq9VeCPrAEWV5B3YWT7uR4fccrio1JnFAjbfAFeeHn1b8OPGNvuk%2BhyCdt%2FaC7kvgGZfPZ0qSP2h8stxzyYGWdyvPWuuCylHbGpp4BW34JH6U%2Bu8Dt81HnX6ExSOqTqp%2By%2Fwy%2BddftoWaankvzmBTY6eIEXxboUbdDhWcjPHOK25d8SuGJ7FsOvfPe5IgSs9NMm1xsZ21G3ZKmGnvqqTUWH%2F3H19x81FXNvo5ZBpRLhpjTQNC18DevahQJAxuuI2%2BmjBnswicL9vAY6pgHOnF%2FlC%2B7aXmwJtiqcbfKF3xyPzXWw8UmwHigzIT2KYN%2Fb%2Fb7RtwpPxwBOwqbiGRt7BU9h5JZG3nTYhcZvxgMvZCfh2iPiKOvdRgJvP9mseEmJzIf8UtBjkm3z%2FJpKz8aKkHJ4PEVrck4R9JLDB6ifwbnXltY0U43bKL4f9tW5pbmXnhWqmzTx1Zi65m85X8ICnYm1tiSGd%2FOcnx6fbNGXVgRsjUsQ&X-Amz-Signature=cdede0cb4fbcb537136b535a37e919147a8475a55877e488ffaa882487031af6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD3KQV46%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBR26IycBOWZRHWz3onMrjZIwdwNHgZh2YqyVcQvR5zsAiBalzVCtufXYvNx1DkrMn60SxIhrreRpXMw8V057hSI4yqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM810tp65975n3rJg9KtwDPr59t3%2B3A%2FDBIqIwLVvJPIg%2Fg9CNvPIBl%2FXhGeOmVAReJYDL3taeul4MjiHK4eKzZpmfmX8Jq52lOpByo%2Fqv0VroXEJs52FUTiZBtwbL5UpegMrY8AzAmgXWRAb5BSxWo4cwHDl53XmrlkmZJYAdxlrJMuyIGrlY54T%2BAtN7IE3MG9s7mvRW5GU8CoegzCkYWD6pERbS9TejLAW8p5c7HHxwYVZGkzRnC5jNsjNOHwNsi3Q8O%2Fs65q%2FuPdGae77mje7qggBubbHcpEWf9A%2F%2F%2Bzk976utsdkTzRPcH3nOi2chwGWotpYrY28XQp9I%2BykES%2BXWVUfseg56l8Bl9foby1qduU6DervAU64OGYf%2FvyNPz%2B%2B0663HIoq9VeCPrAEWV5B3YWT7uR4fccrio1JnFAjbfAFeeHn1b8OPGNvuk%2BhyCdt%2FaC7kvgGZfPZ0qSP2h8stxzyYGWdyvPWuuCylHbGpp4BW34JH6U%2Bu8Dt81HnX6ExSOqTqp%2By%2Fwy%2BddftoWaankvzmBTY6eIEXxboUbdDhWcjPHOK25d8SuGJ7FsOvfPe5IgSs9NMm1xsZ21G3ZKmGnvqqTUWH%2F3H19x81FXNvo5ZBpRLhpjTQNC18DevahQJAxuuI2%2BmjBnswicL9vAY6pgHOnF%2FlC%2B7aXmwJtiqcbfKF3xyPzXWw8UmwHigzIT2KYN%2Fb%2Fb7RtwpPxwBOwqbiGRt7BU9h5JZG3nTYhcZvxgMvZCfh2iPiKOvdRgJvP9mseEmJzIf8UtBjkm3z%2FJpKz8aKkHJ4PEVrck4R9JLDB6ifwbnXltY0U43bKL4f9tW5pbmXnhWqmzTx1Zi65m85X8ICnYm1tiSGd%2FOcnx6fbNGXVgRsjUsQ&X-Amz-Signature=bb484bfa511649c7871a7ae9a6deb58cfa6039bad5557a243b12062bb7b32b40&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD3KQV46%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBR26IycBOWZRHWz3onMrjZIwdwNHgZh2YqyVcQvR5zsAiBalzVCtufXYvNx1DkrMn60SxIhrreRpXMw8V057hSI4yqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM810tp65975n3rJg9KtwDPr59t3%2B3A%2FDBIqIwLVvJPIg%2Fg9CNvPIBl%2FXhGeOmVAReJYDL3taeul4MjiHK4eKzZpmfmX8Jq52lOpByo%2Fqv0VroXEJs52FUTiZBtwbL5UpegMrY8AzAmgXWRAb5BSxWo4cwHDl53XmrlkmZJYAdxlrJMuyIGrlY54T%2BAtN7IE3MG9s7mvRW5GU8CoegzCkYWD6pERbS9TejLAW8p5c7HHxwYVZGkzRnC5jNsjNOHwNsi3Q8O%2Fs65q%2FuPdGae77mje7qggBubbHcpEWf9A%2F%2F%2Bzk976utsdkTzRPcH3nOi2chwGWotpYrY28XQp9I%2BykES%2BXWVUfseg56l8Bl9foby1qduU6DervAU64OGYf%2FvyNPz%2B%2B0663HIoq9VeCPrAEWV5B3YWT7uR4fccrio1JnFAjbfAFeeHn1b8OPGNvuk%2BhyCdt%2FaC7kvgGZfPZ0qSP2h8stxzyYGWdyvPWuuCylHbGpp4BW34JH6U%2Bu8Dt81HnX6ExSOqTqp%2By%2Fwy%2BddftoWaankvzmBTY6eIEXxboUbdDhWcjPHOK25d8SuGJ7FsOvfPe5IgSs9NMm1xsZ21G3ZKmGnvqqTUWH%2F3H19x81FXNvo5ZBpRLhpjTQNC18DevahQJAxuuI2%2BmjBnswicL9vAY6pgHOnF%2FlC%2B7aXmwJtiqcbfKF3xyPzXWw8UmwHigzIT2KYN%2Fb%2Fb7RtwpPxwBOwqbiGRt7BU9h5JZG3nTYhcZvxgMvZCfh2iPiKOvdRgJvP9mseEmJzIf8UtBjkm3z%2FJpKz8aKkHJ4PEVrck4R9JLDB6ifwbnXltY0U43bKL4f9tW5pbmXnhWqmzTx1Zi65m85X8ICnYm1tiSGd%2FOcnx6fbNGXVgRsjUsQ&X-Amz-Signature=56a9d9ceb8f1b20b0d8d96af920403c86efd64112699e5a5cdc39bd48d77a5d3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD3KQV46%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBR26IycBOWZRHWz3onMrjZIwdwNHgZh2YqyVcQvR5zsAiBalzVCtufXYvNx1DkrMn60SxIhrreRpXMw8V057hSI4yqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM810tp65975n3rJg9KtwDPr59t3%2B3A%2FDBIqIwLVvJPIg%2Fg9CNvPIBl%2FXhGeOmVAReJYDL3taeul4MjiHK4eKzZpmfmX8Jq52lOpByo%2Fqv0VroXEJs52FUTiZBtwbL5UpegMrY8AzAmgXWRAb5BSxWo4cwHDl53XmrlkmZJYAdxlrJMuyIGrlY54T%2BAtN7IE3MG9s7mvRW5GU8CoegzCkYWD6pERbS9TejLAW8p5c7HHxwYVZGkzRnC5jNsjNOHwNsi3Q8O%2Fs65q%2FuPdGae77mje7qggBubbHcpEWf9A%2F%2F%2Bzk976utsdkTzRPcH3nOi2chwGWotpYrY28XQp9I%2BykES%2BXWVUfseg56l8Bl9foby1qduU6DervAU64OGYf%2FvyNPz%2B%2B0663HIoq9VeCPrAEWV5B3YWT7uR4fccrio1JnFAjbfAFeeHn1b8OPGNvuk%2BhyCdt%2FaC7kvgGZfPZ0qSP2h8stxzyYGWdyvPWuuCylHbGpp4BW34JH6U%2Bu8Dt81HnX6ExSOqTqp%2By%2Fwy%2BddftoWaankvzmBTY6eIEXxboUbdDhWcjPHOK25d8SuGJ7FsOvfPe5IgSs9NMm1xsZ21G3ZKmGnvqqTUWH%2F3H19x81FXNvo5ZBpRLhpjTQNC18DevahQJAxuuI2%2BmjBnswicL9vAY6pgHOnF%2FlC%2B7aXmwJtiqcbfKF3xyPzXWw8UmwHigzIT2KYN%2Fb%2Fb7RtwpPxwBOwqbiGRt7BU9h5JZG3nTYhcZvxgMvZCfh2iPiKOvdRgJvP9mseEmJzIf8UtBjkm3z%2FJpKz8aKkHJ4PEVrck4R9JLDB6ifwbnXltY0U43bKL4f9tW5pbmXnhWqmzTx1Zi65m85X8ICnYm1tiSGd%2FOcnx6fbNGXVgRsjUsQ&X-Amz-Signature=03d1911a987a226359621e7a6b1f5c4d8e258e22f2327b2d0932fc2785d7f0f2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD3KQV46%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBR26IycBOWZRHWz3onMrjZIwdwNHgZh2YqyVcQvR5zsAiBalzVCtufXYvNx1DkrMn60SxIhrreRpXMw8V057hSI4yqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM810tp65975n3rJg9KtwDPr59t3%2B3A%2FDBIqIwLVvJPIg%2Fg9CNvPIBl%2FXhGeOmVAReJYDL3taeul4MjiHK4eKzZpmfmX8Jq52lOpByo%2Fqv0VroXEJs52FUTiZBtwbL5UpegMrY8AzAmgXWRAb5BSxWo4cwHDl53XmrlkmZJYAdxlrJMuyIGrlY54T%2BAtN7IE3MG9s7mvRW5GU8CoegzCkYWD6pERbS9TejLAW8p5c7HHxwYVZGkzRnC5jNsjNOHwNsi3Q8O%2Fs65q%2FuPdGae77mje7qggBubbHcpEWf9A%2F%2F%2Bzk976utsdkTzRPcH3nOi2chwGWotpYrY28XQp9I%2BykES%2BXWVUfseg56l8Bl9foby1qduU6DervAU64OGYf%2FvyNPz%2B%2B0663HIoq9VeCPrAEWV5B3YWT7uR4fccrio1JnFAjbfAFeeHn1b8OPGNvuk%2BhyCdt%2FaC7kvgGZfPZ0qSP2h8stxzyYGWdyvPWuuCylHbGpp4BW34JH6U%2Bu8Dt81HnX6ExSOqTqp%2By%2Fwy%2BddftoWaankvzmBTY6eIEXxboUbdDhWcjPHOK25d8SuGJ7FsOvfPe5IgSs9NMm1xsZ21G3ZKmGnvqqTUWH%2F3H19x81FXNvo5ZBpRLhpjTQNC18DevahQJAxuuI2%2BmjBnswicL9vAY6pgHOnF%2FlC%2B7aXmwJtiqcbfKF3xyPzXWw8UmwHigzIT2KYN%2Fb%2Fb7RtwpPxwBOwqbiGRt7BU9h5JZG3nTYhcZvxgMvZCfh2iPiKOvdRgJvP9mseEmJzIf8UtBjkm3z%2FJpKz8aKkHJ4PEVrck4R9JLDB6ifwbnXltY0U43bKL4f9tW5pbmXnhWqmzTx1Zi65m85X8ICnYm1tiSGd%2FOcnx6fbNGXVgRsjUsQ&X-Amz-Signature=9b816f3389d030d1cc29d0b81c1cd37da6981a69e3000ef0e3b0e19c1934ed41&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD3KQV46%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBR26IycBOWZRHWz3onMrjZIwdwNHgZh2YqyVcQvR5zsAiBalzVCtufXYvNx1DkrMn60SxIhrreRpXMw8V057hSI4yqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM810tp65975n3rJg9KtwDPr59t3%2B3A%2FDBIqIwLVvJPIg%2Fg9CNvPIBl%2FXhGeOmVAReJYDL3taeul4MjiHK4eKzZpmfmX8Jq52lOpByo%2Fqv0VroXEJs52FUTiZBtwbL5UpegMrY8AzAmgXWRAb5BSxWo4cwHDl53XmrlkmZJYAdxlrJMuyIGrlY54T%2BAtN7IE3MG9s7mvRW5GU8CoegzCkYWD6pERbS9TejLAW8p5c7HHxwYVZGkzRnC5jNsjNOHwNsi3Q8O%2Fs65q%2FuPdGae77mje7qggBubbHcpEWf9A%2F%2F%2Bzk976utsdkTzRPcH3nOi2chwGWotpYrY28XQp9I%2BykES%2BXWVUfseg56l8Bl9foby1qduU6DervAU64OGYf%2FvyNPz%2B%2B0663HIoq9VeCPrAEWV5B3YWT7uR4fccrio1JnFAjbfAFeeHn1b8OPGNvuk%2BhyCdt%2FaC7kvgGZfPZ0qSP2h8stxzyYGWdyvPWuuCylHbGpp4BW34JH6U%2Bu8Dt81HnX6ExSOqTqp%2By%2Fwy%2BddftoWaankvzmBTY6eIEXxboUbdDhWcjPHOK25d8SuGJ7FsOvfPe5IgSs9NMm1xsZ21G3ZKmGnvqqTUWH%2F3H19x81FXNvo5ZBpRLhpjTQNC18DevahQJAxuuI2%2BmjBnswicL9vAY6pgHOnF%2FlC%2B7aXmwJtiqcbfKF3xyPzXWw8UmwHigzIT2KYN%2Fb%2Fb7RtwpPxwBOwqbiGRt7BU9h5JZG3nTYhcZvxgMvZCfh2iPiKOvdRgJvP9mseEmJzIf8UtBjkm3z%2FJpKz8aKkHJ4PEVrck4R9JLDB6ifwbnXltY0U43bKL4f9tW5pbmXnhWqmzTx1Zi65m85X8ICnYm1tiSGd%2FOcnx6fbNGXVgRsjUsQ&X-Amz-Signature=4a9dae1b990f808d2c4b6ce2b57a6099da1beef8acef376c52b66d94cdc084d4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD3KQV46%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBR26IycBOWZRHWz3onMrjZIwdwNHgZh2YqyVcQvR5zsAiBalzVCtufXYvNx1DkrMn60SxIhrreRpXMw8V057hSI4yqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM810tp65975n3rJg9KtwDPr59t3%2B3A%2FDBIqIwLVvJPIg%2Fg9CNvPIBl%2FXhGeOmVAReJYDL3taeul4MjiHK4eKzZpmfmX8Jq52lOpByo%2Fqv0VroXEJs52FUTiZBtwbL5UpegMrY8AzAmgXWRAb5BSxWo4cwHDl53XmrlkmZJYAdxlrJMuyIGrlY54T%2BAtN7IE3MG9s7mvRW5GU8CoegzCkYWD6pERbS9TejLAW8p5c7HHxwYVZGkzRnC5jNsjNOHwNsi3Q8O%2Fs65q%2FuPdGae77mje7qggBubbHcpEWf9A%2F%2F%2Bzk976utsdkTzRPcH3nOi2chwGWotpYrY28XQp9I%2BykES%2BXWVUfseg56l8Bl9foby1qduU6DervAU64OGYf%2FvyNPz%2B%2B0663HIoq9VeCPrAEWV5B3YWT7uR4fccrio1JnFAjbfAFeeHn1b8OPGNvuk%2BhyCdt%2FaC7kvgGZfPZ0qSP2h8stxzyYGWdyvPWuuCylHbGpp4BW34JH6U%2Bu8Dt81HnX6ExSOqTqp%2By%2Fwy%2BddftoWaankvzmBTY6eIEXxboUbdDhWcjPHOK25d8SuGJ7FsOvfPe5IgSs9NMm1xsZ21G3ZKmGnvqqTUWH%2F3H19x81FXNvo5ZBpRLhpjTQNC18DevahQJAxuuI2%2BmjBnswicL9vAY6pgHOnF%2FlC%2B7aXmwJtiqcbfKF3xyPzXWw8UmwHigzIT2KYN%2Fb%2Fb7RtwpPxwBOwqbiGRt7BU9h5JZG3nTYhcZvxgMvZCfh2iPiKOvdRgJvP9mseEmJzIf8UtBjkm3z%2FJpKz8aKkHJ4PEVrck4R9JLDB6ifwbnXltY0U43bKL4f9tW5pbmXnhWqmzTx1Zi65m85X8ICnYm1tiSGd%2FOcnx6fbNGXVgRsjUsQ&X-Amz-Signature=caa652bc5f8b41496223dbb426370012945160ad2a2fa264815360f513cab7da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD3KQV46%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBR26IycBOWZRHWz3onMrjZIwdwNHgZh2YqyVcQvR5zsAiBalzVCtufXYvNx1DkrMn60SxIhrreRpXMw8V057hSI4yqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM810tp65975n3rJg9KtwDPr59t3%2B3A%2FDBIqIwLVvJPIg%2Fg9CNvPIBl%2FXhGeOmVAReJYDL3taeul4MjiHK4eKzZpmfmX8Jq52lOpByo%2Fqv0VroXEJs52FUTiZBtwbL5UpegMrY8AzAmgXWRAb5BSxWo4cwHDl53XmrlkmZJYAdxlrJMuyIGrlY54T%2BAtN7IE3MG9s7mvRW5GU8CoegzCkYWD6pERbS9TejLAW8p5c7HHxwYVZGkzRnC5jNsjNOHwNsi3Q8O%2Fs65q%2FuPdGae77mje7qggBubbHcpEWf9A%2F%2F%2Bzk976utsdkTzRPcH3nOi2chwGWotpYrY28XQp9I%2BykES%2BXWVUfseg56l8Bl9foby1qduU6DervAU64OGYf%2FvyNPz%2B%2B0663HIoq9VeCPrAEWV5B3YWT7uR4fccrio1JnFAjbfAFeeHn1b8OPGNvuk%2BhyCdt%2FaC7kvgGZfPZ0qSP2h8stxzyYGWdyvPWuuCylHbGpp4BW34JH6U%2Bu8Dt81HnX6ExSOqTqp%2By%2Fwy%2BddftoWaankvzmBTY6eIEXxboUbdDhWcjPHOK25d8SuGJ7FsOvfPe5IgSs9NMm1xsZ21G3ZKmGnvqqTUWH%2F3H19x81FXNvo5ZBpRLhpjTQNC18DevahQJAxuuI2%2BmjBnswicL9vAY6pgHOnF%2FlC%2B7aXmwJtiqcbfKF3xyPzXWw8UmwHigzIT2KYN%2Fb%2Fb7RtwpPxwBOwqbiGRt7BU9h5JZG3nTYhcZvxgMvZCfh2iPiKOvdRgJvP9mseEmJzIf8UtBjkm3z%2FJpKz8aKkHJ4PEVrck4R9JLDB6ifwbnXltY0U43bKL4f9tW5pbmXnhWqmzTx1Zi65m85X8ICnYm1tiSGd%2FOcnx6fbNGXVgRsjUsQ&X-Amz-Signature=a5320d2f2990b26a7a43ec50a37a45a3fec2a51e8a12f47bf6bd2b14cd628a9a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD3KQV46%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBR26IycBOWZRHWz3onMrjZIwdwNHgZh2YqyVcQvR5zsAiBalzVCtufXYvNx1DkrMn60SxIhrreRpXMw8V057hSI4yqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM810tp65975n3rJg9KtwDPr59t3%2B3A%2FDBIqIwLVvJPIg%2Fg9CNvPIBl%2FXhGeOmVAReJYDL3taeul4MjiHK4eKzZpmfmX8Jq52lOpByo%2Fqv0VroXEJs52FUTiZBtwbL5UpegMrY8AzAmgXWRAb5BSxWo4cwHDl53XmrlkmZJYAdxlrJMuyIGrlY54T%2BAtN7IE3MG9s7mvRW5GU8CoegzCkYWD6pERbS9TejLAW8p5c7HHxwYVZGkzRnC5jNsjNOHwNsi3Q8O%2Fs65q%2FuPdGae77mje7qggBubbHcpEWf9A%2F%2F%2Bzk976utsdkTzRPcH3nOi2chwGWotpYrY28XQp9I%2BykES%2BXWVUfseg56l8Bl9foby1qduU6DervAU64OGYf%2FvyNPz%2B%2B0663HIoq9VeCPrAEWV5B3YWT7uR4fccrio1JnFAjbfAFeeHn1b8OPGNvuk%2BhyCdt%2FaC7kvgGZfPZ0qSP2h8stxzyYGWdyvPWuuCylHbGpp4BW34JH6U%2Bu8Dt81HnX6ExSOqTqp%2By%2Fwy%2BddftoWaankvzmBTY6eIEXxboUbdDhWcjPHOK25d8SuGJ7FsOvfPe5IgSs9NMm1xsZ21G3ZKmGnvqqTUWH%2F3H19x81FXNvo5ZBpRLhpjTQNC18DevahQJAxuuI2%2BmjBnswicL9vAY6pgHOnF%2FlC%2B7aXmwJtiqcbfKF3xyPzXWw8UmwHigzIT2KYN%2Fb%2Fb7RtwpPxwBOwqbiGRt7BU9h5JZG3nTYhcZvxgMvZCfh2iPiKOvdRgJvP9mseEmJzIf8UtBjkm3z%2FJpKz8aKkHJ4PEVrck4R9JLDB6ifwbnXltY0U43bKL4f9tW5pbmXnhWqmzTx1Zi65m85X8ICnYm1tiSGd%2FOcnx6fbNGXVgRsjUsQ&X-Amz-Signature=f75e953e57685055de3345af516ae2ca9a73fb25eb5cf93a552e895916210ac9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTAFKWVE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUlktaMF8jR9d6YTMxabQNZpxmAZNsg8FYi1W%2BnG%2FFLAiAn5uGc17JNhRBAC42WQXQgytgIDQb%2Bz0ty47KlvgieuiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4%2FXiR28MzCv%2FPXDcKtwDveUdgpGb6GFUpnai3efK4eLL8jXg%2FVIPFxD9TQPEOgLzNBfsaHIH73Jp5dePqJmJWpZFzJf%2B0FqdUoF%2BtzRHpJsYUEu9HaELirnzEtn6mhKWWEChDM6BLGmDBJNqzHpujpJvJQBDxQheWmoXGecRwsk13v44mA6bFme9HNnlz4F2gRZCP6s7fkZkmKhqrr9Z6PElDn4AShDSp8RPjD9gDXdulWbq%2FZJo%2B0fxbXsEPQzBzR%2FgYz%2F1yrOwnEFSSMuSbXdnYrMhdxzBPlgDEz04Sl%2F%2FeBRPm3K91jaQMQy24vvaC11FqWkolWsj3cEDr%2F0Se7bg%2FeDpsIhVUZh7Ijd2DpRQu%2BwWSM1IXjtROkHiRI4nKuQY57w2LCFO1FkZh3qM4eNzFXutfaQ1ZdORgKWt2jntyx%2FTCPKCx18WApc%2F7iZ6N51Z3Acjz5P2qmLMMm3x49kwDRD2jGapl7sAc3r%2B7dSXxfZcooBQ0PLwW3HEB4Fgv8vb4YGkXXB55A1%2BtpBFhxH9gq3BdJNvnUY8RY5ZcyLyqhkHK07LUS5atYu3KhhsWPg6rnp1ZFOSNe9bjZU%2B0UCTnm7OrHmF6KUzEZ5UoewBcrlNkELCm9vDzVXqDRoUbnj9KxcAc8I%2BPrkwhcH9vAY6pgGIghp9gKNAOq51eYLoGgqa7lBNs734ML6g%2FOR0fg3E%2FHQl8CilPBHg7tt%2FVR0Hva1xEfRtzNHlH%2FqZHXDfm81pQcKu5EKvntrFN%2BkGHO%2FbjMaZFP2xcS1EkEmzTri75KTEqUSHo3a0lzOKWIM1LpjvkytifQse4TsLWaFoVLHIarQ1p9d6rt0TGvAl738qpGWE7yG3eQq3F8OlBFEk50zV4xSldz8U&X-Amz-Signature=847a2433e4ceda51099d04b51a5bdc042a61244216d24b81b59d84d3611bbb73&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTAFKWVE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUlktaMF8jR9d6YTMxabQNZpxmAZNsg8FYi1W%2BnG%2FFLAiAn5uGc17JNhRBAC42WQXQgytgIDQb%2Bz0ty47KlvgieuiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4%2FXiR28MzCv%2FPXDcKtwDveUdgpGb6GFUpnai3efK4eLL8jXg%2FVIPFxD9TQPEOgLzNBfsaHIH73Jp5dePqJmJWpZFzJf%2B0FqdUoF%2BtzRHpJsYUEu9HaELirnzEtn6mhKWWEChDM6BLGmDBJNqzHpujpJvJQBDxQheWmoXGecRwsk13v44mA6bFme9HNnlz4F2gRZCP6s7fkZkmKhqrr9Z6PElDn4AShDSp8RPjD9gDXdulWbq%2FZJo%2B0fxbXsEPQzBzR%2FgYz%2F1yrOwnEFSSMuSbXdnYrMhdxzBPlgDEz04Sl%2F%2FeBRPm3K91jaQMQy24vvaC11FqWkolWsj3cEDr%2F0Se7bg%2FeDpsIhVUZh7Ijd2DpRQu%2BwWSM1IXjtROkHiRI4nKuQY57w2LCFO1FkZh3qM4eNzFXutfaQ1ZdORgKWt2jntyx%2FTCPKCx18WApc%2F7iZ6N51Z3Acjz5P2qmLMMm3x49kwDRD2jGapl7sAc3r%2B7dSXxfZcooBQ0PLwW3HEB4Fgv8vb4YGkXXB55A1%2BtpBFhxH9gq3BdJNvnUY8RY5ZcyLyqhkHK07LUS5atYu3KhhsWPg6rnp1ZFOSNe9bjZU%2B0UCTnm7OrHmF6KUzEZ5UoewBcrlNkELCm9vDzVXqDRoUbnj9KxcAc8I%2BPrkwhcH9vAY6pgGIghp9gKNAOq51eYLoGgqa7lBNs734ML6g%2FOR0fg3E%2FHQl8CilPBHg7tt%2FVR0Hva1xEfRtzNHlH%2FqZHXDfm81pQcKu5EKvntrFN%2BkGHO%2FbjMaZFP2xcS1EkEmzTri75KTEqUSHo3a0lzOKWIM1LpjvkytifQse4TsLWaFoVLHIarQ1p9d6rt0TGvAl738qpGWE7yG3eQq3F8OlBFEk50zV4xSldz8U&X-Amz-Signature=6777513a263f8da334adff1d030d2299561a875f55545b13144ebc2165f2d77e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
