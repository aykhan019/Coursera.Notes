

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HFBHBB2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhagMgKib3OGpN5jFZgA%2FD6oXyiCQRQSTBhHNby3xpMAIhAJzbpgKg008bj0bUwBdhw2G%2FKc92Ix59rdpdjhvDyBj4KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsAqGfrRHBXsSYr7Yq3ANgeYnpukA3Hcop71k1LgrZkF7wse7oQ8F9PzTaWGphNo9cicariQJY9Fq%2FaffZQ4GPsdS7DGrzFWqTfc8hkJ07hjOtaJCF08Y2JEU%2FVV%2Fui86G3fA7tmwJ9Kgb3qL8ro1MkfbVUGGo0qi5mgN9UyPnQVj7JvxRV0TCr9iKRRA%2B3AWMMIZ%2FzJAKlbSHK42vwUnOhzq4umMXNuQJKRCvRRu4V9gzuNGv0DYfzzy%2BNNRTeCuTTlezmr6FwMCgW6qvV4gLAmDAfYEFmOHNpi4syp1Hae86XimIlYGlTf9v7%2FtpJL1l52LkfVM2UVDuSFnW%2BQHdjM%2B89YfoYt9NIKxX4TjvCOx7cChYpO2dM1jgQYAnR3AZ5kQ78ChqXKMfetBYML10bD65Jpv5EeU1kDISNLQ%2BjYTJTCjbR9opm4CgKQJ7zpo%2BO61I0dSQxPdJgE6gcQN6tqrDMIB%2FsylmGcEjvHdxIncoXlLDjZBuUt7npvWd07INJnBda8YIYD3XCEktRbQa4wUbyUyR1Ucj3UHrnSv1sc%2FgfbJ97aRlX2gWUsZGu7lzvtefZHYRO%2BGQKaUJ4EvZMi9Jqrokw9F3beVFzv55mAPFpmRIrKqLMyzqLaY%2BCUkkZnMSwjZxGJFCtzCJwv28BjqkARkQxDK9V%2BLmVSFyeD5zdwOjNb2Gur4r4EmpzJj8oZweMuO5p5dHu6vn5CD6eUrhyDjWWGcXPuIaVp8L94XqvapJY1sr35HPItXOJmTy1qTOhn4WsbV0UA3d21PbhU4qZK0s9w4ON%2FWYki1gQGhPxxF3UdBdk4UJhzZpSWWlOoteb93rZbZstxlZFQTLdzuhL0NCOJdbg5FW7CAFY%2BFEid324QjN&X-Amz-Signature=967e955989c58fc54cf74e0a5415cf6ca5beaef092ff3b2cdfd0b773d98c60e2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HFBHBB2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhagMgKib3OGpN5jFZgA%2FD6oXyiCQRQSTBhHNby3xpMAIhAJzbpgKg008bj0bUwBdhw2G%2FKc92Ix59rdpdjhvDyBj4KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsAqGfrRHBXsSYr7Yq3ANgeYnpukA3Hcop71k1LgrZkF7wse7oQ8F9PzTaWGphNo9cicariQJY9Fq%2FaffZQ4GPsdS7DGrzFWqTfc8hkJ07hjOtaJCF08Y2JEU%2FVV%2Fui86G3fA7tmwJ9Kgb3qL8ro1MkfbVUGGo0qi5mgN9UyPnQVj7JvxRV0TCr9iKRRA%2B3AWMMIZ%2FzJAKlbSHK42vwUnOhzq4umMXNuQJKRCvRRu4V9gzuNGv0DYfzzy%2BNNRTeCuTTlezmr6FwMCgW6qvV4gLAmDAfYEFmOHNpi4syp1Hae86XimIlYGlTf9v7%2FtpJL1l52LkfVM2UVDuSFnW%2BQHdjM%2B89YfoYt9NIKxX4TjvCOx7cChYpO2dM1jgQYAnR3AZ5kQ78ChqXKMfetBYML10bD65Jpv5EeU1kDISNLQ%2BjYTJTCjbR9opm4CgKQJ7zpo%2BO61I0dSQxPdJgE6gcQN6tqrDMIB%2FsylmGcEjvHdxIncoXlLDjZBuUt7npvWd07INJnBda8YIYD3XCEktRbQa4wUbyUyR1Ucj3UHrnSv1sc%2FgfbJ97aRlX2gWUsZGu7lzvtefZHYRO%2BGQKaUJ4EvZMi9Jqrokw9F3beVFzv55mAPFpmRIrKqLMyzqLaY%2BCUkkZnMSwjZxGJFCtzCJwv28BjqkARkQxDK9V%2BLmVSFyeD5zdwOjNb2Gur4r4EmpzJj8oZweMuO5p5dHu6vn5CD6eUrhyDjWWGcXPuIaVp8L94XqvapJY1sr35HPItXOJmTy1qTOhn4WsbV0UA3d21PbhU4qZK0s9w4ON%2FWYki1gQGhPxxF3UdBdk4UJhzZpSWWlOoteb93rZbZstxlZFQTLdzuhL0NCOJdbg5FW7CAFY%2BFEid324QjN&X-Amz-Signature=2a51fe16baf06a5e2c59b0416bc3930226c59d97d89932bd1105a4c5348875b0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HFBHBB2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhagMgKib3OGpN5jFZgA%2FD6oXyiCQRQSTBhHNby3xpMAIhAJzbpgKg008bj0bUwBdhw2G%2FKc92Ix59rdpdjhvDyBj4KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsAqGfrRHBXsSYr7Yq3ANgeYnpukA3Hcop71k1LgrZkF7wse7oQ8F9PzTaWGphNo9cicariQJY9Fq%2FaffZQ4GPsdS7DGrzFWqTfc8hkJ07hjOtaJCF08Y2JEU%2FVV%2Fui86G3fA7tmwJ9Kgb3qL8ro1MkfbVUGGo0qi5mgN9UyPnQVj7JvxRV0TCr9iKRRA%2B3AWMMIZ%2FzJAKlbSHK42vwUnOhzq4umMXNuQJKRCvRRu4V9gzuNGv0DYfzzy%2BNNRTeCuTTlezmr6FwMCgW6qvV4gLAmDAfYEFmOHNpi4syp1Hae86XimIlYGlTf9v7%2FtpJL1l52LkfVM2UVDuSFnW%2BQHdjM%2B89YfoYt9NIKxX4TjvCOx7cChYpO2dM1jgQYAnR3AZ5kQ78ChqXKMfetBYML10bD65Jpv5EeU1kDISNLQ%2BjYTJTCjbR9opm4CgKQJ7zpo%2BO61I0dSQxPdJgE6gcQN6tqrDMIB%2FsylmGcEjvHdxIncoXlLDjZBuUt7npvWd07INJnBda8YIYD3XCEktRbQa4wUbyUyR1Ucj3UHrnSv1sc%2FgfbJ97aRlX2gWUsZGu7lzvtefZHYRO%2BGQKaUJ4EvZMi9Jqrokw9F3beVFzv55mAPFpmRIrKqLMyzqLaY%2BCUkkZnMSwjZxGJFCtzCJwv28BjqkARkQxDK9V%2BLmVSFyeD5zdwOjNb2Gur4r4EmpzJj8oZweMuO5p5dHu6vn5CD6eUrhyDjWWGcXPuIaVp8L94XqvapJY1sr35HPItXOJmTy1qTOhn4WsbV0UA3d21PbhU4qZK0s9w4ON%2FWYki1gQGhPxxF3UdBdk4UJhzZpSWWlOoteb93rZbZstxlZFQTLdzuhL0NCOJdbg5FW7CAFY%2BFEid324QjN&X-Amz-Signature=2a5e4900150109d9466cd967171f374e6bf66db39f733d22976a5145e985349f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HFBHBB2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhagMgKib3OGpN5jFZgA%2FD6oXyiCQRQSTBhHNby3xpMAIhAJzbpgKg008bj0bUwBdhw2G%2FKc92Ix59rdpdjhvDyBj4KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsAqGfrRHBXsSYr7Yq3ANgeYnpukA3Hcop71k1LgrZkF7wse7oQ8F9PzTaWGphNo9cicariQJY9Fq%2FaffZQ4GPsdS7DGrzFWqTfc8hkJ07hjOtaJCF08Y2JEU%2FVV%2Fui86G3fA7tmwJ9Kgb3qL8ro1MkfbVUGGo0qi5mgN9UyPnQVj7JvxRV0TCr9iKRRA%2B3AWMMIZ%2FzJAKlbSHK42vwUnOhzq4umMXNuQJKRCvRRu4V9gzuNGv0DYfzzy%2BNNRTeCuTTlezmr6FwMCgW6qvV4gLAmDAfYEFmOHNpi4syp1Hae86XimIlYGlTf9v7%2FtpJL1l52LkfVM2UVDuSFnW%2BQHdjM%2B89YfoYt9NIKxX4TjvCOx7cChYpO2dM1jgQYAnR3AZ5kQ78ChqXKMfetBYML10bD65Jpv5EeU1kDISNLQ%2BjYTJTCjbR9opm4CgKQJ7zpo%2BO61I0dSQxPdJgE6gcQN6tqrDMIB%2FsylmGcEjvHdxIncoXlLDjZBuUt7npvWd07INJnBda8YIYD3XCEktRbQa4wUbyUyR1Ucj3UHrnSv1sc%2FgfbJ97aRlX2gWUsZGu7lzvtefZHYRO%2BGQKaUJ4EvZMi9Jqrokw9F3beVFzv55mAPFpmRIrKqLMyzqLaY%2BCUkkZnMSwjZxGJFCtzCJwv28BjqkARkQxDK9V%2BLmVSFyeD5zdwOjNb2Gur4r4EmpzJj8oZweMuO5p5dHu6vn5CD6eUrhyDjWWGcXPuIaVp8L94XqvapJY1sr35HPItXOJmTy1qTOhn4WsbV0UA3d21PbhU4qZK0s9w4ON%2FWYki1gQGhPxxF3UdBdk4UJhzZpSWWlOoteb93rZbZstxlZFQTLdzuhL0NCOJdbg5FW7CAFY%2BFEid324QjN&X-Amz-Signature=2fcb25ee2f1736238ed3cf7d5fb7682d21c878be9824ba558a652358ff72304c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HFBHBB2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhagMgKib3OGpN5jFZgA%2FD6oXyiCQRQSTBhHNby3xpMAIhAJzbpgKg008bj0bUwBdhw2G%2FKc92Ix59rdpdjhvDyBj4KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsAqGfrRHBXsSYr7Yq3ANgeYnpukA3Hcop71k1LgrZkF7wse7oQ8F9PzTaWGphNo9cicariQJY9Fq%2FaffZQ4GPsdS7DGrzFWqTfc8hkJ07hjOtaJCF08Y2JEU%2FVV%2Fui86G3fA7tmwJ9Kgb3qL8ro1MkfbVUGGo0qi5mgN9UyPnQVj7JvxRV0TCr9iKRRA%2B3AWMMIZ%2FzJAKlbSHK42vwUnOhzq4umMXNuQJKRCvRRu4V9gzuNGv0DYfzzy%2BNNRTeCuTTlezmr6FwMCgW6qvV4gLAmDAfYEFmOHNpi4syp1Hae86XimIlYGlTf9v7%2FtpJL1l52LkfVM2UVDuSFnW%2BQHdjM%2B89YfoYt9NIKxX4TjvCOx7cChYpO2dM1jgQYAnR3AZ5kQ78ChqXKMfetBYML10bD65Jpv5EeU1kDISNLQ%2BjYTJTCjbR9opm4CgKQJ7zpo%2BO61I0dSQxPdJgE6gcQN6tqrDMIB%2FsylmGcEjvHdxIncoXlLDjZBuUt7npvWd07INJnBda8YIYD3XCEktRbQa4wUbyUyR1Ucj3UHrnSv1sc%2FgfbJ97aRlX2gWUsZGu7lzvtefZHYRO%2BGQKaUJ4EvZMi9Jqrokw9F3beVFzv55mAPFpmRIrKqLMyzqLaY%2BCUkkZnMSwjZxGJFCtzCJwv28BjqkARkQxDK9V%2BLmVSFyeD5zdwOjNb2Gur4r4EmpzJj8oZweMuO5p5dHu6vn5CD6eUrhyDjWWGcXPuIaVp8L94XqvapJY1sr35HPItXOJmTy1qTOhn4WsbV0UA3d21PbhU4qZK0s9w4ON%2FWYki1gQGhPxxF3UdBdk4UJhzZpSWWlOoteb93rZbZstxlZFQTLdzuhL0NCOJdbg5FW7CAFY%2BFEid324QjN&X-Amz-Signature=98ae9a5260426cb98f6f9df0aa41921c64df4db68f2b390c3265c8f4366a08de&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HFBHBB2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhagMgKib3OGpN5jFZgA%2FD6oXyiCQRQSTBhHNby3xpMAIhAJzbpgKg008bj0bUwBdhw2G%2FKc92Ix59rdpdjhvDyBj4KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsAqGfrRHBXsSYr7Yq3ANgeYnpukA3Hcop71k1LgrZkF7wse7oQ8F9PzTaWGphNo9cicariQJY9Fq%2FaffZQ4GPsdS7DGrzFWqTfc8hkJ07hjOtaJCF08Y2JEU%2FVV%2Fui86G3fA7tmwJ9Kgb3qL8ro1MkfbVUGGo0qi5mgN9UyPnQVj7JvxRV0TCr9iKRRA%2B3AWMMIZ%2FzJAKlbSHK42vwUnOhzq4umMXNuQJKRCvRRu4V9gzuNGv0DYfzzy%2BNNRTeCuTTlezmr6FwMCgW6qvV4gLAmDAfYEFmOHNpi4syp1Hae86XimIlYGlTf9v7%2FtpJL1l52LkfVM2UVDuSFnW%2BQHdjM%2B89YfoYt9NIKxX4TjvCOx7cChYpO2dM1jgQYAnR3AZ5kQ78ChqXKMfetBYML10bD65Jpv5EeU1kDISNLQ%2BjYTJTCjbR9opm4CgKQJ7zpo%2BO61I0dSQxPdJgE6gcQN6tqrDMIB%2FsylmGcEjvHdxIncoXlLDjZBuUt7npvWd07INJnBda8YIYD3XCEktRbQa4wUbyUyR1Ucj3UHrnSv1sc%2FgfbJ97aRlX2gWUsZGu7lzvtefZHYRO%2BGQKaUJ4EvZMi9Jqrokw9F3beVFzv55mAPFpmRIrKqLMyzqLaY%2BCUkkZnMSwjZxGJFCtzCJwv28BjqkARkQxDK9V%2BLmVSFyeD5zdwOjNb2Gur4r4EmpzJj8oZweMuO5p5dHu6vn5CD6eUrhyDjWWGcXPuIaVp8L94XqvapJY1sr35HPItXOJmTy1qTOhn4WsbV0UA3d21PbhU4qZK0s9w4ON%2FWYki1gQGhPxxF3UdBdk4UJhzZpSWWlOoteb93rZbZstxlZFQTLdzuhL0NCOJdbg5FW7CAFY%2BFEid324QjN&X-Amz-Signature=7fddedeffae8e44b10eabe36cc99de116885990fac23e602099266b6e74f4ea1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HFBHBB2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhagMgKib3OGpN5jFZgA%2FD6oXyiCQRQSTBhHNby3xpMAIhAJzbpgKg008bj0bUwBdhw2G%2FKc92Ix59rdpdjhvDyBj4KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsAqGfrRHBXsSYr7Yq3ANgeYnpukA3Hcop71k1LgrZkF7wse7oQ8F9PzTaWGphNo9cicariQJY9Fq%2FaffZQ4GPsdS7DGrzFWqTfc8hkJ07hjOtaJCF08Y2JEU%2FVV%2Fui86G3fA7tmwJ9Kgb3qL8ro1MkfbVUGGo0qi5mgN9UyPnQVj7JvxRV0TCr9iKRRA%2B3AWMMIZ%2FzJAKlbSHK42vwUnOhzq4umMXNuQJKRCvRRu4V9gzuNGv0DYfzzy%2BNNRTeCuTTlezmr6FwMCgW6qvV4gLAmDAfYEFmOHNpi4syp1Hae86XimIlYGlTf9v7%2FtpJL1l52LkfVM2UVDuSFnW%2BQHdjM%2B89YfoYt9NIKxX4TjvCOx7cChYpO2dM1jgQYAnR3AZ5kQ78ChqXKMfetBYML10bD65Jpv5EeU1kDISNLQ%2BjYTJTCjbR9opm4CgKQJ7zpo%2BO61I0dSQxPdJgE6gcQN6tqrDMIB%2FsylmGcEjvHdxIncoXlLDjZBuUt7npvWd07INJnBda8YIYD3XCEktRbQa4wUbyUyR1Ucj3UHrnSv1sc%2FgfbJ97aRlX2gWUsZGu7lzvtefZHYRO%2BGQKaUJ4EvZMi9Jqrokw9F3beVFzv55mAPFpmRIrKqLMyzqLaY%2BCUkkZnMSwjZxGJFCtzCJwv28BjqkARkQxDK9V%2BLmVSFyeD5zdwOjNb2Gur4r4EmpzJj8oZweMuO5p5dHu6vn5CD6eUrhyDjWWGcXPuIaVp8L94XqvapJY1sr35HPItXOJmTy1qTOhn4WsbV0UA3d21PbhU4qZK0s9w4ON%2FWYki1gQGhPxxF3UdBdk4UJhzZpSWWlOoteb93rZbZstxlZFQTLdzuhL0NCOJdbg5FW7CAFY%2BFEid324QjN&X-Amz-Signature=7ad5a2485efc602d52d55941e87014fff265295a1f5be476050c1bc5d7d29e5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HFBHBB2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhagMgKib3OGpN5jFZgA%2FD6oXyiCQRQSTBhHNby3xpMAIhAJzbpgKg008bj0bUwBdhw2G%2FKc92Ix59rdpdjhvDyBj4KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsAqGfrRHBXsSYr7Yq3ANgeYnpukA3Hcop71k1LgrZkF7wse7oQ8F9PzTaWGphNo9cicariQJY9Fq%2FaffZQ4GPsdS7DGrzFWqTfc8hkJ07hjOtaJCF08Y2JEU%2FVV%2Fui86G3fA7tmwJ9Kgb3qL8ro1MkfbVUGGo0qi5mgN9UyPnQVj7JvxRV0TCr9iKRRA%2B3AWMMIZ%2FzJAKlbSHK42vwUnOhzq4umMXNuQJKRCvRRu4V9gzuNGv0DYfzzy%2BNNRTeCuTTlezmr6FwMCgW6qvV4gLAmDAfYEFmOHNpi4syp1Hae86XimIlYGlTf9v7%2FtpJL1l52LkfVM2UVDuSFnW%2BQHdjM%2B89YfoYt9NIKxX4TjvCOx7cChYpO2dM1jgQYAnR3AZ5kQ78ChqXKMfetBYML10bD65Jpv5EeU1kDISNLQ%2BjYTJTCjbR9opm4CgKQJ7zpo%2BO61I0dSQxPdJgE6gcQN6tqrDMIB%2FsylmGcEjvHdxIncoXlLDjZBuUt7npvWd07INJnBda8YIYD3XCEktRbQa4wUbyUyR1Ucj3UHrnSv1sc%2FgfbJ97aRlX2gWUsZGu7lzvtefZHYRO%2BGQKaUJ4EvZMi9Jqrokw9F3beVFzv55mAPFpmRIrKqLMyzqLaY%2BCUkkZnMSwjZxGJFCtzCJwv28BjqkARkQxDK9V%2BLmVSFyeD5zdwOjNb2Gur4r4EmpzJj8oZweMuO5p5dHu6vn5CD6eUrhyDjWWGcXPuIaVp8L94XqvapJY1sr35HPItXOJmTy1qTOhn4WsbV0UA3d21PbhU4qZK0s9w4ON%2FWYki1gQGhPxxF3UdBdk4UJhzZpSWWlOoteb93rZbZstxlZFQTLdzuhL0NCOJdbg5FW7CAFY%2BFEid324QjN&X-Amz-Signature=c6bbb9e91743c88bc1ee001eee17a85acf3dc9671d80bb31da5d88306f9a9837&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HFBHBB2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhagMgKib3OGpN5jFZgA%2FD6oXyiCQRQSTBhHNby3xpMAIhAJzbpgKg008bj0bUwBdhw2G%2FKc92Ix59rdpdjhvDyBj4KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsAqGfrRHBXsSYr7Yq3ANgeYnpukA3Hcop71k1LgrZkF7wse7oQ8F9PzTaWGphNo9cicariQJY9Fq%2FaffZQ4GPsdS7DGrzFWqTfc8hkJ07hjOtaJCF08Y2JEU%2FVV%2Fui86G3fA7tmwJ9Kgb3qL8ro1MkfbVUGGo0qi5mgN9UyPnQVj7JvxRV0TCr9iKRRA%2B3AWMMIZ%2FzJAKlbSHK42vwUnOhzq4umMXNuQJKRCvRRu4V9gzuNGv0DYfzzy%2BNNRTeCuTTlezmr6FwMCgW6qvV4gLAmDAfYEFmOHNpi4syp1Hae86XimIlYGlTf9v7%2FtpJL1l52LkfVM2UVDuSFnW%2BQHdjM%2B89YfoYt9NIKxX4TjvCOx7cChYpO2dM1jgQYAnR3AZ5kQ78ChqXKMfetBYML10bD65Jpv5EeU1kDISNLQ%2BjYTJTCjbR9opm4CgKQJ7zpo%2BO61I0dSQxPdJgE6gcQN6tqrDMIB%2FsylmGcEjvHdxIncoXlLDjZBuUt7npvWd07INJnBda8YIYD3XCEktRbQa4wUbyUyR1Ucj3UHrnSv1sc%2FgfbJ97aRlX2gWUsZGu7lzvtefZHYRO%2BGQKaUJ4EvZMi9Jqrokw9F3beVFzv55mAPFpmRIrKqLMyzqLaY%2BCUkkZnMSwjZxGJFCtzCJwv28BjqkARkQxDK9V%2BLmVSFyeD5zdwOjNb2Gur4r4EmpzJj8oZweMuO5p5dHu6vn5CD6eUrhyDjWWGcXPuIaVp8L94XqvapJY1sr35HPItXOJmTy1qTOhn4WsbV0UA3d21PbhU4qZK0s9w4ON%2FWYki1gQGhPxxF3UdBdk4UJhzZpSWWlOoteb93rZbZstxlZFQTLdzuhL0NCOJdbg5FW7CAFY%2BFEid324QjN&X-Amz-Signature=fcd097f44c5e53e055b8eaab156263984c35df053aed762b3880029f381aee95&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663O2O7YA3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDW2j2GGnuts9YcaitJ3ZsL3IyVh7cuQ4CxZMGHQoyFwAIgM4gG9u4634hXnin9sGcDPfKW2dqAaOx64CirEcT7f8IqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKFVQNPNfTA3%2FUA9HyrcA3T9i5QLTEwxTR%2BHINtQaLwYwofDQnCyofRaA6%2FkR2n2ZfSzQ%2BzWtUT4AduU55OmrCqHTjiCg7Gfd5ksSEuv7fe%2BySxlX8DPcMnZq9Aost4pKetDixgYWL1ZQnwC68u1JOi20mY3YVIRHmZkMAvdaZSggHQyw4LkOZ4uQZ8zVvNUlSCRcavid7Fd1UH0iXrV62gy%2FNALOPIBkKubwAoA7kK4M5An1Hmdcxxy71ctTre%2BWNK17eG9dlLarYR2e8fpKb1H9gmMlZ1NhOWA51i74WwqT5nOS1keDNnAjGqEwg%2BIPaMRH%2FtjQnUtokhvxSTHuouqdgYlZ1M%2BU%2FTd9%2BdcMv0P8N2pdf32CqAaJxyUY5TAVpk3P2PVg6hxLSxuiRRVvjovRk%2BczyY4nE0u25gZhkzIhDl6RmG0AwnwoAaJLNBBu3W1FWJ9423rSPQTJFIhcEEbwb2zFkmVCDoP7gUszTqcqzk7BpDJ%2BlFlZxkbddfo6TY5L1Tm%2FSzuRdEwVUlfTtl0fTboPUV3KdaGVge0LlBeUHi%2BDekhsKcQI9rXAecQtjxDRmg471BA9Lq2sdtuWFPmsWY2CfMIgZ%2Fgt8Zfg1Rbmtyb0ydE7Vj24y%2FC7UOwNDrEVtTVTRHCUFb2MNzC%2FbwGOqUBDTvmOLPQ7X7xBSr%2FERlP2y4IS3YL1W%2FM2YLUzAH3cLDzp8J98HD%2BA%2B2HczbRFSXJUMEE58psXVMHrf2b4yI2lXufhKjFIW2A8gAhBEVBnGLMYtbLmHYDoYSC0la%2BjHWCNZ5z9PfFbdKeqF8gsJ83cWuez9qQLL9O0AXTfPAYuDOa0htRI8DkZGyuAq2RXGY2YDeCpsYw8iZ5Sh2c3U3nLzqDOsl5&X-Amz-Signature=c36eed8761d6f595812dd534e4ddcd6c66bd165470a81fa1fadd07e0c2eeb920&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663O2O7YA3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDW2j2GGnuts9YcaitJ3ZsL3IyVh7cuQ4CxZMGHQoyFwAIgM4gG9u4634hXnin9sGcDPfKW2dqAaOx64CirEcT7f8IqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKFVQNPNfTA3%2FUA9HyrcA3T9i5QLTEwxTR%2BHINtQaLwYwofDQnCyofRaA6%2FkR2n2ZfSzQ%2BzWtUT4AduU55OmrCqHTjiCg7Gfd5ksSEuv7fe%2BySxlX8DPcMnZq9Aost4pKetDixgYWL1ZQnwC68u1JOi20mY3YVIRHmZkMAvdaZSggHQyw4LkOZ4uQZ8zVvNUlSCRcavid7Fd1UH0iXrV62gy%2FNALOPIBkKubwAoA7kK4M5An1Hmdcxxy71ctTre%2BWNK17eG9dlLarYR2e8fpKb1H9gmMlZ1NhOWA51i74WwqT5nOS1keDNnAjGqEwg%2BIPaMRH%2FtjQnUtokhvxSTHuouqdgYlZ1M%2BU%2FTd9%2BdcMv0P8N2pdf32CqAaJxyUY5TAVpk3P2PVg6hxLSxuiRRVvjovRk%2BczyY4nE0u25gZhkzIhDl6RmG0AwnwoAaJLNBBu3W1FWJ9423rSPQTJFIhcEEbwb2zFkmVCDoP7gUszTqcqzk7BpDJ%2BlFlZxkbddfo6TY5L1Tm%2FSzuRdEwVUlfTtl0fTboPUV3KdaGVge0LlBeUHi%2BDekhsKcQI9rXAecQtjxDRmg471BA9Lq2sdtuWFPmsWY2CfMIgZ%2Fgt8Zfg1Rbmtyb0ydE7Vj24y%2FC7UOwNDrEVtTVTRHCUFb2MNzC%2FbwGOqUBDTvmOLPQ7X7xBSr%2FERlP2y4IS3YL1W%2FM2YLUzAH3cLDzp8J98HD%2BA%2B2HczbRFSXJUMEE58psXVMHrf2b4yI2lXufhKjFIW2A8gAhBEVBnGLMYtbLmHYDoYSC0la%2BjHWCNZ5z9PfFbdKeqF8gsJ83cWuez9qQLL9O0AXTfPAYuDOa0htRI8DkZGyuAq2RXGY2YDeCpsYw8iZ5Sh2c3U3nLzqDOsl5&X-Amz-Signature=1dd748da5beeba958846943b04ba7a4b2b34efce0947ea56f65f97648532e3a5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
