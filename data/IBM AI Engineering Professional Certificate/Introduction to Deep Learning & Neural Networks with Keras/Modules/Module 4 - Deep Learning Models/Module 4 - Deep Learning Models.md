

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ3YRTWP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD7SeTY%2BmBaIIz04vRsSrhMts9vXgJYsiVXqgY4ZGRUuQIhAMFQpSyxqnmVY4GS%2Bky%2FeAAj%2F8RPvnC634S05UP2scP9Kv8DCCAQABoMNjM3NDIzMTgzODA1IgxGj2vZbTLlyXp2XVQq3AN5JepHFRV3%2FoGEnguuKgVGl6Dsw96pjimLfSyMOy4fBTmQP7rrlPsE%2FrqQ6tlCnSd%2Fady%2BDOoy3ftbR8Xzpa6w6jRbXEkHOep0kl7BcaBRGkUtRGvuCjaqQbtDeFSJlvfCgn%2BOgi2YLWukOq0Rx6hXooVLIvqsYVy0gZvN%2FdcC4HE1iaXHzwsihhyQcW%2BecGEMo%2Fp%2Bd4PU10JzjlO3p7q4O71TzKReVy06lpQzNjjVKj2mN3FuHVw7OPIOa%2Fn2RxmQeVU%2Bno%2Bb42ufYMVZQeVOCqouY9gAKH1qJ%2B17GfSRWALX3%2BDPVy0yFDxsYfdSszvZBpqaWzZG1x2%2FJlv9lGxYN8Hocup0aYOeKdrwYd5DhlShR%2FJH5xA6KwOvDOFC2XwAqGc9X%2BdzJVCp3Am1Q4HLxayD8Jzh%2Fn%2BgPjp%2B0DDlRiQbAZz6y3WwQgckOTpx%2BCZI0F8D4U3UG6Q9XypZqJwZ6CR9zCLZK5aW2ROw6wZ6E0INEPcaXUcbzG8S4mfgd14cRkmbTv1fcpytojRZLwbs6a6Cfv8YHIglZypfO%2FFQTwV5LKQSwY9ZJ57%2B3hA6aBiEWSEk1aR2lrvEdGGiv0Zkl4qaHTeimPhuiy78t02qUu19kscIzeGsUWqZZzDkk4W9BjqkAUYxN2KTZqQ2WKIMxPBcsjz0ZdenwEaZjWuY%2B9ozZlXtYijNF2pIGtATZC64qBov81ka7iEVXmhpTDs1f9AyNId6Y8%2FKxsMRP9kyvnV0sSDkNPcyUuXM%2F%2BlvAw%2F4YZGfivLTW8yfQ0R2SstEu%2FTYlVhBXGA7OL6JKSPVRyNpjYWQBVmCmpAZBLBz5fYZ6oRuuMlERnY0N513N0eZjczj1%2BQnHwQ2&X-Amz-Signature=cc858354aa58563370a586c28be18d52678ab830595e1f12344d45d0513a26fc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ3YRTWP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD7SeTY%2BmBaIIz04vRsSrhMts9vXgJYsiVXqgY4ZGRUuQIhAMFQpSyxqnmVY4GS%2Bky%2FeAAj%2F8RPvnC634S05UP2scP9Kv8DCCAQABoMNjM3NDIzMTgzODA1IgxGj2vZbTLlyXp2XVQq3AN5JepHFRV3%2FoGEnguuKgVGl6Dsw96pjimLfSyMOy4fBTmQP7rrlPsE%2FrqQ6tlCnSd%2Fady%2BDOoy3ftbR8Xzpa6w6jRbXEkHOep0kl7BcaBRGkUtRGvuCjaqQbtDeFSJlvfCgn%2BOgi2YLWukOq0Rx6hXooVLIvqsYVy0gZvN%2FdcC4HE1iaXHzwsihhyQcW%2BecGEMo%2Fp%2Bd4PU10JzjlO3p7q4O71TzKReVy06lpQzNjjVKj2mN3FuHVw7OPIOa%2Fn2RxmQeVU%2Bno%2Bb42ufYMVZQeVOCqouY9gAKH1qJ%2B17GfSRWALX3%2BDPVy0yFDxsYfdSszvZBpqaWzZG1x2%2FJlv9lGxYN8Hocup0aYOeKdrwYd5DhlShR%2FJH5xA6KwOvDOFC2XwAqGc9X%2BdzJVCp3Am1Q4HLxayD8Jzh%2Fn%2BgPjp%2B0DDlRiQbAZz6y3WwQgckOTpx%2BCZI0F8D4U3UG6Q9XypZqJwZ6CR9zCLZK5aW2ROw6wZ6E0INEPcaXUcbzG8S4mfgd14cRkmbTv1fcpytojRZLwbs6a6Cfv8YHIglZypfO%2FFQTwV5LKQSwY9ZJ57%2B3hA6aBiEWSEk1aR2lrvEdGGiv0Zkl4qaHTeimPhuiy78t02qUu19kscIzeGsUWqZZzDkk4W9BjqkAUYxN2KTZqQ2WKIMxPBcsjz0ZdenwEaZjWuY%2B9ozZlXtYijNF2pIGtATZC64qBov81ka7iEVXmhpTDs1f9AyNId6Y8%2FKxsMRP9kyvnV0sSDkNPcyUuXM%2F%2BlvAw%2F4YZGfivLTW8yfQ0R2SstEu%2FTYlVhBXGA7OL6JKSPVRyNpjYWQBVmCmpAZBLBz5fYZ6oRuuMlERnY0N513N0eZjczj1%2BQnHwQ2&X-Amz-Signature=39da02b7ffcceb342c8597b6391b462757b5f76eccd908879ecbc5b3400a3e6e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ3YRTWP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD7SeTY%2BmBaIIz04vRsSrhMts9vXgJYsiVXqgY4ZGRUuQIhAMFQpSyxqnmVY4GS%2Bky%2FeAAj%2F8RPvnC634S05UP2scP9Kv8DCCAQABoMNjM3NDIzMTgzODA1IgxGj2vZbTLlyXp2XVQq3AN5JepHFRV3%2FoGEnguuKgVGl6Dsw96pjimLfSyMOy4fBTmQP7rrlPsE%2FrqQ6tlCnSd%2Fady%2BDOoy3ftbR8Xzpa6w6jRbXEkHOep0kl7BcaBRGkUtRGvuCjaqQbtDeFSJlvfCgn%2BOgi2YLWukOq0Rx6hXooVLIvqsYVy0gZvN%2FdcC4HE1iaXHzwsihhyQcW%2BecGEMo%2Fp%2Bd4PU10JzjlO3p7q4O71TzKReVy06lpQzNjjVKj2mN3FuHVw7OPIOa%2Fn2RxmQeVU%2Bno%2Bb42ufYMVZQeVOCqouY9gAKH1qJ%2B17GfSRWALX3%2BDPVy0yFDxsYfdSszvZBpqaWzZG1x2%2FJlv9lGxYN8Hocup0aYOeKdrwYd5DhlShR%2FJH5xA6KwOvDOFC2XwAqGc9X%2BdzJVCp3Am1Q4HLxayD8Jzh%2Fn%2BgPjp%2B0DDlRiQbAZz6y3WwQgckOTpx%2BCZI0F8D4U3UG6Q9XypZqJwZ6CR9zCLZK5aW2ROw6wZ6E0INEPcaXUcbzG8S4mfgd14cRkmbTv1fcpytojRZLwbs6a6Cfv8YHIglZypfO%2FFQTwV5LKQSwY9ZJ57%2B3hA6aBiEWSEk1aR2lrvEdGGiv0Zkl4qaHTeimPhuiy78t02qUu19kscIzeGsUWqZZzDkk4W9BjqkAUYxN2KTZqQ2WKIMxPBcsjz0ZdenwEaZjWuY%2B9ozZlXtYijNF2pIGtATZC64qBov81ka7iEVXmhpTDs1f9AyNId6Y8%2FKxsMRP9kyvnV0sSDkNPcyUuXM%2F%2BlvAw%2F4YZGfivLTW8yfQ0R2SstEu%2FTYlVhBXGA7OL6JKSPVRyNpjYWQBVmCmpAZBLBz5fYZ6oRuuMlERnY0N513N0eZjczj1%2BQnHwQ2&X-Amz-Signature=3ebd4fc5a2918290d8c50931f73bb0dd5a150a17c20a8de1f8980929a216441d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ3YRTWP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD7SeTY%2BmBaIIz04vRsSrhMts9vXgJYsiVXqgY4ZGRUuQIhAMFQpSyxqnmVY4GS%2Bky%2FeAAj%2F8RPvnC634S05UP2scP9Kv8DCCAQABoMNjM3NDIzMTgzODA1IgxGj2vZbTLlyXp2XVQq3AN5JepHFRV3%2FoGEnguuKgVGl6Dsw96pjimLfSyMOy4fBTmQP7rrlPsE%2FrqQ6tlCnSd%2Fady%2BDOoy3ftbR8Xzpa6w6jRbXEkHOep0kl7BcaBRGkUtRGvuCjaqQbtDeFSJlvfCgn%2BOgi2YLWukOq0Rx6hXooVLIvqsYVy0gZvN%2FdcC4HE1iaXHzwsihhyQcW%2BecGEMo%2Fp%2Bd4PU10JzjlO3p7q4O71TzKReVy06lpQzNjjVKj2mN3FuHVw7OPIOa%2Fn2RxmQeVU%2Bno%2Bb42ufYMVZQeVOCqouY9gAKH1qJ%2B17GfSRWALX3%2BDPVy0yFDxsYfdSszvZBpqaWzZG1x2%2FJlv9lGxYN8Hocup0aYOeKdrwYd5DhlShR%2FJH5xA6KwOvDOFC2XwAqGc9X%2BdzJVCp3Am1Q4HLxayD8Jzh%2Fn%2BgPjp%2B0DDlRiQbAZz6y3WwQgckOTpx%2BCZI0F8D4U3UG6Q9XypZqJwZ6CR9zCLZK5aW2ROw6wZ6E0INEPcaXUcbzG8S4mfgd14cRkmbTv1fcpytojRZLwbs6a6Cfv8YHIglZypfO%2FFQTwV5LKQSwY9ZJ57%2B3hA6aBiEWSEk1aR2lrvEdGGiv0Zkl4qaHTeimPhuiy78t02qUu19kscIzeGsUWqZZzDkk4W9BjqkAUYxN2KTZqQ2WKIMxPBcsjz0ZdenwEaZjWuY%2B9ozZlXtYijNF2pIGtATZC64qBov81ka7iEVXmhpTDs1f9AyNId6Y8%2FKxsMRP9kyvnV0sSDkNPcyUuXM%2F%2BlvAw%2F4YZGfivLTW8yfQ0R2SstEu%2FTYlVhBXGA7OL6JKSPVRyNpjYWQBVmCmpAZBLBz5fYZ6oRuuMlERnY0N513N0eZjczj1%2BQnHwQ2&X-Amz-Signature=f97311c8194208ac472d7bc5b0b80eb287643266e62e76dd96cac38d8caaf409&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ3YRTWP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD7SeTY%2BmBaIIz04vRsSrhMts9vXgJYsiVXqgY4ZGRUuQIhAMFQpSyxqnmVY4GS%2Bky%2FeAAj%2F8RPvnC634S05UP2scP9Kv8DCCAQABoMNjM3NDIzMTgzODA1IgxGj2vZbTLlyXp2XVQq3AN5JepHFRV3%2FoGEnguuKgVGl6Dsw96pjimLfSyMOy4fBTmQP7rrlPsE%2FrqQ6tlCnSd%2Fady%2BDOoy3ftbR8Xzpa6w6jRbXEkHOep0kl7BcaBRGkUtRGvuCjaqQbtDeFSJlvfCgn%2BOgi2YLWukOq0Rx6hXooVLIvqsYVy0gZvN%2FdcC4HE1iaXHzwsihhyQcW%2BecGEMo%2Fp%2Bd4PU10JzjlO3p7q4O71TzKReVy06lpQzNjjVKj2mN3FuHVw7OPIOa%2Fn2RxmQeVU%2Bno%2Bb42ufYMVZQeVOCqouY9gAKH1qJ%2B17GfSRWALX3%2BDPVy0yFDxsYfdSszvZBpqaWzZG1x2%2FJlv9lGxYN8Hocup0aYOeKdrwYd5DhlShR%2FJH5xA6KwOvDOFC2XwAqGc9X%2BdzJVCp3Am1Q4HLxayD8Jzh%2Fn%2BgPjp%2B0DDlRiQbAZz6y3WwQgckOTpx%2BCZI0F8D4U3UG6Q9XypZqJwZ6CR9zCLZK5aW2ROw6wZ6E0INEPcaXUcbzG8S4mfgd14cRkmbTv1fcpytojRZLwbs6a6Cfv8YHIglZypfO%2FFQTwV5LKQSwY9ZJ57%2B3hA6aBiEWSEk1aR2lrvEdGGiv0Zkl4qaHTeimPhuiy78t02qUu19kscIzeGsUWqZZzDkk4W9BjqkAUYxN2KTZqQ2WKIMxPBcsjz0ZdenwEaZjWuY%2B9ozZlXtYijNF2pIGtATZC64qBov81ka7iEVXmhpTDs1f9AyNId6Y8%2FKxsMRP9kyvnV0sSDkNPcyUuXM%2F%2BlvAw%2F4YZGfivLTW8yfQ0R2SstEu%2FTYlVhBXGA7OL6JKSPVRyNpjYWQBVmCmpAZBLBz5fYZ6oRuuMlERnY0N513N0eZjczj1%2BQnHwQ2&X-Amz-Signature=86f36356ca58ff07a528839ea62fae8d66db602b22559d7a258f7af8de45e245&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ3YRTWP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD7SeTY%2BmBaIIz04vRsSrhMts9vXgJYsiVXqgY4ZGRUuQIhAMFQpSyxqnmVY4GS%2Bky%2FeAAj%2F8RPvnC634S05UP2scP9Kv8DCCAQABoMNjM3NDIzMTgzODA1IgxGj2vZbTLlyXp2XVQq3AN5JepHFRV3%2FoGEnguuKgVGl6Dsw96pjimLfSyMOy4fBTmQP7rrlPsE%2FrqQ6tlCnSd%2Fady%2BDOoy3ftbR8Xzpa6w6jRbXEkHOep0kl7BcaBRGkUtRGvuCjaqQbtDeFSJlvfCgn%2BOgi2YLWukOq0Rx6hXooVLIvqsYVy0gZvN%2FdcC4HE1iaXHzwsihhyQcW%2BecGEMo%2Fp%2Bd4PU10JzjlO3p7q4O71TzKReVy06lpQzNjjVKj2mN3FuHVw7OPIOa%2Fn2RxmQeVU%2Bno%2Bb42ufYMVZQeVOCqouY9gAKH1qJ%2B17GfSRWALX3%2BDPVy0yFDxsYfdSszvZBpqaWzZG1x2%2FJlv9lGxYN8Hocup0aYOeKdrwYd5DhlShR%2FJH5xA6KwOvDOFC2XwAqGc9X%2BdzJVCp3Am1Q4HLxayD8Jzh%2Fn%2BgPjp%2B0DDlRiQbAZz6y3WwQgckOTpx%2BCZI0F8D4U3UG6Q9XypZqJwZ6CR9zCLZK5aW2ROw6wZ6E0INEPcaXUcbzG8S4mfgd14cRkmbTv1fcpytojRZLwbs6a6Cfv8YHIglZypfO%2FFQTwV5LKQSwY9ZJ57%2B3hA6aBiEWSEk1aR2lrvEdGGiv0Zkl4qaHTeimPhuiy78t02qUu19kscIzeGsUWqZZzDkk4W9BjqkAUYxN2KTZqQ2WKIMxPBcsjz0ZdenwEaZjWuY%2B9ozZlXtYijNF2pIGtATZC64qBov81ka7iEVXmhpTDs1f9AyNId6Y8%2FKxsMRP9kyvnV0sSDkNPcyUuXM%2F%2BlvAw%2F4YZGfivLTW8yfQ0R2SstEu%2FTYlVhBXGA7OL6JKSPVRyNpjYWQBVmCmpAZBLBz5fYZ6oRuuMlERnY0N513N0eZjczj1%2BQnHwQ2&X-Amz-Signature=81c92a306b2a761b55f477ffe910bbebfca8d75499f5cba4d80d992aa817be92&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ3YRTWP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD7SeTY%2BmBaIIz04vRsSrhMts9vXgJYsiVXqgY4ZGRUuQIhAMFQpSyxqnmVY4GS%2Bky%2FeAAj%2F8RPvnC634S05UP2scP9Kv8DCCAQABoMNjM3NDIzMTgzODA1IgxGj2vZbTLlyXp2XVQq3AN5JepHFRV3%2FoGEnguuKgVGl6Dsw96pjimLfSyMOy4fBTmQP7rrlPsE%2FrqQ6tlCnSd%2Fady%2BDOoy3ftbR8Xzpa6w6jRbXEkHOep0kl7BcaBRGkUtRGvuCjaqQbtDeFSJlvfCgn%2BOgi2YLWukOq0Rx6hXooVLIvqsYVy0gZvN%2FdcC4HE1iaXHzwsihhyQcW%2BecGEMo%2Fp%2Bd4PU10JzjlO3p7q4O71TzKReVy06lpQzNjjVKj2mN3FuHVw7OPIOa%2Fn2RxmQeVU%2Bno%2Bb42ufYMVZQeVOCqouY9gAKH1qJ%2B17GfSRWALX3%2BDPVy0yFDxsYfdSszvZBpqaWzZG1x2%2FJlv9lGxYN8Hocup0aYOeKdrwYd5DhlShR%2FJH5xA6KwOvDOFC2XwAqGc9X%2BdzJVCp3Am1Q4HLxayD8Jzh%2Fn%2BgPjp%2B0DDlRiQbAZz6y3WwQgckOTpx%2BCZI0F8D4U3UG6Q9XypZqJwZ6CR9zCLZK5aW2ROw6wZ6E0INEPcaXUcbzG8S4mfgd14cRkmbTv1fcpytojRZLwbs6a6Cfv8YHIglZypfO%2FFQTwV5LKQSwY9ZJ57%2B3hA6aBiEWSEk1aR2lrvEdGGiv0Zkl4qaHTeimPhuiy78t02qUu19kscIzeGsUWqZZzDkk4W9BjqkAUYxN2KTZqQ2WKIMxPBcsjz0ZdenwEaZjWuY%2B9ozZlXtYijNF2pIGtATZC64qBov81ka7iEVXmhpTDs1f9AyNId6Y8%2FKxsMRP9kyvnV0sSDkNPcyUuXM%2F%2BlvAw%2F4YZGfivLTW8yfQ0R2SstEu%2FTYlVhBXGA7OL6JKSPVRyNpjYWQBVmCmpAZBLBz5fYZ6oRuuMlERnY0N513N0eZjczj1%2BQnHwQ2&X-Amz-Signature=a00ed9ed976097016a33c1266b147dcec5d5e9e26b708f2e95a86d374ec2df46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ3YRTWP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD7SeTY%2BmBaIIz04vRsSrhMts9vXgJYsiVXqgY4ZGRUuQIhAMFQpSyxqnmVY4GS%2Bky%2FeAAj%2F8RPvnC634S05UP2scP9Kv8DCCAQABoMNjM3NDIzMTgzODA1IgxGj2vZbTLlyXp2XVQq3AN5JepHFRV3%2FoGEnguuKgVGl6Dsw96pjimLfSyMOy4fBTmQP7rrlPsE%2FrqQ6tlCnSd%2Fady%2BDOoy3ftbR8Xzpa6w6jRbXEkHOep0kl7BcaBRGkUtRGvuCjaqQbtDeFSJlvfCgn%2BOgi2YLWukOq0Rx6hXooVLIvqsYVy0gZvN%2FdcC4HE1iaXHzwsihhyQcW%2BecGEMo%2Fp%2Bd4PU10JzjlO3p7q4O71TzKReVy06lpQzNjjVKj2mN3FuHVw7OPIOa%2Fn2RxmQeVU%2Bno%2Bb42ufYMVZQeVOCqouY9gAKH1qJ%2B17GfSRWALX3%2BDPVy0yFDxsYfdSszvZBpqaWzZG1x2%2FJlv9lGxYN8Hocup0aYOeKdrwYd5DhlShR%2FJH5xA6KwOvDOFC2XwAqGc9X%2BdzJVCp3Am1Q4HLxayD8Jzh%2Fn%2BgPjp%2B0DDlRiQbAZz6y3WwQgckOTpx%2BCZI0F8D4U3UG6Q9XypZqJwZ6CR9zCLZK5aW2ROw6wZ6E0INEPcaXUcbzG8S4mfgd14cRkmbTv1fcpytojRZLwbs6a6Cfv8YHIglZypfO%2FFQTwV5LKQSwY9ZJ57%2B3hA6aBiEWSEk1aR2lrvEdGGiv0Zkl4qaHTeimPhuiy78t02qUu19kscIzeGsUWqZZzDkk4W9BjqkAUYxN2KTZqQ2WKIMxPBcsjz0ZdenwEaZjWuY%2B9ozZlXtYijNF2pIGtATZC64qBov81ka7iEVXmhpTDs1f9AyNId6Y8%2FKxsMRP9kyvnV0sSDkNPcyUuXM%2F%2BlvAw%2F4YZGfivLTW8yfQ0R2SstEu%2FTYlVhBXGA7OL6JKSPVRyNpjYWQBVmCmpAZBLBz5fYZ6oRuuMlERnY0N513N0eZjczj1%2BQnHwQ2&X-Amz-Signature=a12dd33238400cec39696b04e40bb5f7abe606e0a0d4e586c0f93e8aa660bf53&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ3YRTWP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD7SeTY%2BmBaIIz04vRsSrhMts9vXgJYsiVXqgY4ZGRUuQIhAMFQpSyxqnmVY4GS%2Bky%2FeAAj%2F8RPvnC634S05UP2scP9Kv8DCCAQABoMNjM3NDIzMTgzODA1IgxGj2vZbTLlyXp2XVQq3AN5JepHFRV3%2FoGEnguuKgVGl6Dsw96pjimLfSyMOy4fBTmQP7rrlPsE%2FrqQ6tlCnSd%2Fady%2BDOoy3ftbR8Xzpa6w6jRbXEkHOep0kl7BcaBRGkUtRGvuCjaqQbtDeFSJlvfCgn%2BOgi2YLWukOq0Rx6hXooVLIvqsYVy0gZvN%2FdcC4HE1iaXHzwsihhyQcW%2BecGEMo%2Fp%2Bd4PU10JzjlO3p7q4O71TzKReVy06lpQzNjjVKj2mN3FuHVw7OPIOa%2Fn2RxmQeVU%2Bno%2Bb42ufYMVZQeVOCqouY9gAKH1qJ%2B17GfSRWALX3%2BDPVy0yFDxsYfdSszvZBpqaWzZG1x2%2FJlv9lGxYN8Hocup0aYOeKdrwYd5DhlShR%2FJH5xA6KwOvDOFC2XwAqGc9X%2BdzJVCp3Am1Q4HLxayD8Jzh%2Fn%2BgPjp%2B0DDlRiQbAZz6y3WwQgckOTpx%2BCZI0F8D4U3UG6Q9XypZqJwZ6CR9zCLZK5aW2ROw6wZ6E0INEPcaXUcbzG8S4mfgd14cRkmbTv1fcpytojRZLwbs6a6Cfv8YHIglZypfO%2FFQTwV5LKQSwY9ZJ57%2B3hA6aBiEWSEk1aR2lrvEdGGiv0Zkl4qaHTeimPhuiy78t02qUu19kscIzeGsUWqZZzDkk4W9BjqkAUYxN2KTZqQ2WKIMxPBcsjz0ZdenwEaZjWuY%2B9ozZlXtYijNF2pIGtATZC64qBov81ka7iEVXmhpTDs1f9AyNId6Y8%2FKxsMRP9kyvnV0sSDkNPcyUuXM%2F%2BlvAw%2F4YZGfivLTW8yfQ0R2SstEu%2FTYlVhBXGA7OL6JKSPVRyNpjYWQBVmCmpAZBLBz5fYZ6oRuuMlERnY0N513N0eZjczj1%2BQnHwQ2&X-Amz-Signature=89e0d4d522cdcdae2c4e22b2b45147e8aa8c5e29dd0fc01add3b6f1ff05ee6a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQKCU65M%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIE39kZglE1zdKWIYIvHGfV8YNmLGi5xLtiV4l3hcose0AiEAtbFmZLiTE2b7PgNMgS30aTkwQlAlVfl2njUQ5FU8eI8q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJW3yF8u581aEH5n2ircAz0S2vtT0LU15nSq6z2nG%2BZPALIgiHGGuPw93HrHuF9sfr0t4s4LMm%2FcJ219t7fMdBRPQ5r0l3jBTlfGLNaXCowiwSMuxGEZLjh3Io8%2Bt7rYLVhD5lNzgS54pTSVA8RQTDmvtIDOXGUwQ8FlrtODaawzfUkjNsplXLDDBCK0lKZAXBdavePSuJOmkvBu5K1bFO4jcsJ23m%2BreXfOlJsWO0nXMp0DKG%2BOok9BdNVyBUCrtbNtrPJulmye6pBExppZLWWh2BQKZviVB6DqCCaWxaNinuIQK6QDNv10xJ%2FPu4zvj%2BYUIg5ZJscfwMd5reNT0Ekd6RYjbYtUQPwKwM1Fn5VOywjZ2B2txY7hUgPdV21Ug5Edk2jPLWQ2WvFocm3Y%2F%2Fl3Rv8AAnmPUA%2Bceyr0o4d0NBPWwQzjPPgZ6sq%2FsddixXh2KDdL4aF7qI%2Bfp0CnNI2hWHjwh4KM%2BGYc7AFcegzeMVQ0BB45gvebqUiilImiClyxAwUxsJgNa3QDEnjVIDbH%2BZJENKXtiSGSrS1V2deVD3cXKfTH3%2FcwxPdqm%2FiqqlqmjUFvFodYOY2%2F%2B1hOFlpt3Nsb0Nw69QNerqhOCCKry8MRxgKEbEzb7gmSMD12oj2bmP2iQRbizpykMLyUhb0GOqUBdD0h2Six6AmO2rwV70Oa4bhm2FO%2FXOwu4oZvnQ6spQa7uABB2pPdhRaRAy6Kft%2BEdptuakygb9NgPKaOxIKcbXo4swfUc1IZCKD0BL4w73THaFDz%2Bz9Iiw%2F8M5%2Br2Hk7j8fTjz%2BGuDE8tJXagsMVsyya8d1K3EIyCki7UIEUwFiaiMAypOmIe%2FODdxlB4XSV44vLaOWy7qgZ6Ckj2g8SFO%2FjA1Y3&X-Amz-Signature=ff26d9be48237384a7cad178dfb11cec7b8df49ba3cfbe9d5c7496f2dd08ee4c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQKCU65M%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIE39kZglE1zdKWIYIvHGfV8YNmLGi5xLtiV4l3hcose0AiEAtbFmZLiTE2b7PgNMgS30aTkwQlAlVfl2njUQ5FU8eI8q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJW3yF8u581aEH5n2ircAz0S2vtT0LU15nSq6z2nG%2BZPALIgiHGGuPw93HrHuF9sfr0t4s4LMm%2FcJ219t7fMdBRPQ5r0l3jBTlfGLNaXCowiwSMuxGEZLjh3Io8%2Bt7rYLVhD5lNzgS54pTSVA8RQTDmvtIDOXGUwQ8FlrtODaawzfUkjNsplXLDDBCK0lKZAXBdavePSuJOmkvBu5K1bFO4jcsJ23m%2BreXfOlJsWO0nXMp0DKG%2BOok9BdNVyBUCrtbNtrPJulmye6pBExppZLWWh2BQKZviVB6DqCCaWxaNinuIQK6QDNv10xJ%2FPu4zvj%2BYUIg5ZJscfwMd5reNT0Ekd6RYjbYtUQPwKwM1Fn5VOywjZ2B2txY7hUgPdV21Ug5Edk2jPLWQ2WvFocm3Y%2F%2Fl3Rv8AAnmPUA%2Bceyr0o4d0NBPWwQzjPPgZ6sq%2FsddixXh2KDdL4aF7qI%2Bfp0CnNI2hWHjwh4KM%2BGYc7AFcegzeMVQ0BB45gvebqUiilImiClyxAwUxsJgNa3QDEnjVIDbH%2BZJENKXtiSGSrS1V2deVD3cXKfTH3%2FcwxPdqm%2FiqqlqmjUFvFodYOY2%2F%2B1hOFlpt3Nsb0Nw69QNerqhOCCKry8MRxgKEbEzb7gmSMD12oj2bmP2iQRbizpykMLyUhb0GOqUBdD0h2Six6AmO2rwV70Oa4bhm2FO%2FXOwu4oZvnQ6spQa7uABB2pPdhRaRAy6Kft%2BEdptuakygb9NgPKaOxIKcbXo4swfUc1IZCKD0BL4w73THaFDz%2Bz9Iiw%2F8M5%2Br2Hk7j8fTjz%2BGuDE8tJXagsMVsyya8d1K3EIyCki7UIEUwFiaiMAypOmIe%2FODdxlB4XSV44vLaOWy7qgZ6Ckj2g8SFO%2FjA1Y3&X-Amz-Signature=17ed05da6d0de130556c5c1bc5b8e29cf649e9ef8f6403c7eb510c8f26b52595&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
