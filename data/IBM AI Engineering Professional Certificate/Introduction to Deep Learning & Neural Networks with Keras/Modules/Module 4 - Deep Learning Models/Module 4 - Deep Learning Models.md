

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJA3FZK5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCyUT9w%2F9FGilgrsjNFYOavastvvTsM1ZnVWlrqKemX2QIhALX0destCnzZoqXW1K%2Fap%2B2wAG1woR%2BNsAOPWoMdUUM3Kv8DCBsQABoMNjM3NDIzMTgzODA1IgxZ6C%2Fvjq0VyOqVYDIq3APmLb1b%2Bmeek78bnhqZZjGHCIHzHCw9e4yPt3rrVPQRgC%2B5uavsNd3U4ITxcTtJb5kuNyCQUpMiZ9%2FV3v1XnugMW9hZef2U3fc7HDigYuTJvsZ%2BWiVG0a%2FXnxFvHwSVz2kYADi8AdcQAeRnwSvfgHmfRx%2F1tTV8F45YrdioUbCMa3h3%2BZHLY8OH3dDD9SYGBzt%2FKuaea34pDoPW8vKn7jmEcix7dk3PJ4xW6f9IaA8JlxSj4djBt80XToeYpZVhSQ6H8FdfF9B5BOrRohZOlf%2FVq7NoFiLXu5Akl5bFlMmMBQd%2BTUdnxhJkg4NJHw8kEbEAVuT0zerEuws7X0xWfh1N2tLu6WTxyIfvU97ebro7mZKFgvG%2BoHTdCwo1gl6g7v4DHSfT4dUxJ0Jfj0zRkDN%2BOx%2BSeaYE2j3sscFBbyDDkcYTvJ%2BLbO5QhR9FsLVxWIP4XJ%2FXAxJ6ATlHbGJBqBNAncNy0X54fa4h8D6tTF4LxXfLsxt%2B9ZrTjRKTwYFvQK2tZwxvfy%2Bxt7%2BDPH69t61V32toSw%2FaOtRYYpCiP6cCdXTy%2BmVRNx9h2%2BsZVWMuuZa1kXNyCdXNz%2B%2Bj9pjqdh%2BdLPvYssOPmosJoeP9fPNYHQVxvCMaBAMjeu1Q0DDeg4S9BjqkAYs3vTcILLxJEb2EkVV%2F4uP0rLZDoeiGJ5NT9hbRM0Uc2zbMsp2ONjh2ZfEjMhaoxFZcXf9Vxs6mqPtAb2Sj9JxQQ9dY5vtzc1JQR6Jyy%2BBdHNjAvN%2BzgNPNVbuhob69edoKYCpSMe6WOJfQ7PFQLnZmZXNpwhAKA97BadP2V5xc%2FSoWmJVYDaD56%2BxnDCDrvs6CZSXmGS0AioaHQ94DNRN8QO%2BC&X-Amz-Signature=78bd4b6573ac10b5ce2b32de5f23c894a07e590ee6dcaef9f7b0aebbf29e828e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJA3FZK5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCyUT9w%2F9FGilgrsjNFYOavastvvTsM1ZnVWlrqKemX2QIhALX0destCnzZoqXW1K%2Fap%2B2wAG1woR%2BNsAOPWoMdUUM3Kv8DCBsQABoMNjM3NDIzMTgzODA1IgxZ6C%2Fvjq0VyOqVYDIq3APmLb1b%2Bmeek78bnhqZZjGHCIHzHCw9e4yPt3rrVPQRgC%2B5uavsNd3U4ITxcTtJb5kuNyCQUpMiZ9%2FV3v1XnugMW9hZef2U3fc7HDigYuTJvsZ%2BWiVG0a%2FXnxFvHwSVz2kYADi8AdcQAeRnwSvfgHmfRx%2F1tTV8F45YrdioUbCMa3h3%2BZHLY8OH3dDD9SYGBzt%2FKuaea34pDoPW8vKn7jmEcix7dk3PJ4xW6f9IaA8JlxSj4djBt80XToeYpZVhSQ6H8FdfF9B5BOrRohZOlf%2FVq7NoFiLXu5Akl5bFlMmMBQd%2BTUdnxhJkg4NJHw8kEbEAVuT0zerEuws7X0xWfh1N2tLu6WTxyIfvU97ebro7mZKFgvG%2BoHTdCwo1gl6g7v4DHSfT4dUxJ0Jfj0zRkDN%2BOx%2BSeaYE2j3sscFBbyDDkcYTvJ%2BLbO5QhR9FsLVxWIP4XJ%2FXAxJ6ATlHbGJBqBNAncNy0X54fa4h8D6tTF4LxXfLsxt%2B9ZrTjRKTwYFvQK2tZwxvfy%2Bxt7%2BDPH69t61V32toSw%2FaOtRYYpCiP6cCdXTy%2BmVRNx9h2%2BsZVWMuuZa1kXNyCdXNz%2B%2Bj9pjqdh%2BdLPvYssOPmosJoeP9fPNYHQVxvCMaBAMjeu1Q0DDeg4S9BjqkAYs3vTcILLxJEb2EkVV%2F4uP0rLZDoeiGJ5NT9hbRM0Uc2zbMsp2ONjh2ZfEjMhaoxFZcXf9Vxs6mqPtAb2Sj9JxQQ9dY5vtzc1JQR6Jyy%2BBdHNjAvN%2BzgNPNVbuhob69edoKYCpSMe6WOJfQ7PFQLnZmZXNpwhAKA97BadP2V5xc%2FSoWmJVYDaD56%2BxnDCDrvs6CZSXmGS0AioaHQ94DNRN8QO%2BC&X-Amz-Signature=447a5da2357fe1f64c7b0b0a0073a8c86574bbc899e6f7773a101a0cd587afe2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJA3FZK5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCyUT9w%2F9FGilgrsjNFYOavastvvTsM1ZnVWlrqKemX2QIhALX0destCnzZoqXW1K%2Fap%2B2wAG1woR%2BNsAOPWoMdUUM3Kv8DCBsQABoMNjM3NDIzMTgzODA1IgxZ6C%2Fvjq0VyOqVYDIq3APmLb1b%2Bmeek78bnhqZZjGHCIHzHCw9e4yPt3rrVPQRgC%2B5uavsNd3U4ITxcTtJb5kuNyCQUpMiZ9%2FV3v1XnugMW9hZef2U3fc7HDigYuTJvsZ%2BWiVG0a%2FXnxFvHwSVz2kYADi8AdcQAeRnwSvfgHmfRx%2F1tTV8F45YrdioUbCMa3h3%2BZHLY8OH3dDD9SYGBzt%2FKuaea34pDoPW8vKn7jmEcix7dk3PJ4xW6f9IaA8JlxSj4djBt80XToeYpZVhSQ6H8FdfF9B5BOrRohZOlf%2FVq7NoFiLXu5Akl5bFlMmMBQd%2BTUdnxhJkg4NJHw8kEbEAVuT0zerEuws7X0xWfh1N2tLu6WTxyIfvU97ebro7mZKFgvG%2BoHTdCwo1gl6g7v4DHSfT4dUxJ0Jfj0zRkDN%2BOx%2BSeaYE2j3sscFBbyDDkcYTvJ%2BLbO5QhR9FsLVxWIP4XJ%2FXAxJ6ATlHbGJBqBNAncNy0X54fa4h8D6tTF4LxXfLsxt%2B9ZrTjRKTwYFvQK2tZwxvfy%2Bxt7%2BDPH69t61V32toSw%2FaOtRYYpCiP6cCdXTy%2BmVRNx9h2%2BsZVWMuuZa1kXNyCdXNz%2B%2Bj9pjqdh%2BdLPvYssOPmosJoeP9fPNYHQVxvCMaBAMjeu1Q0DDeg4S9BjqkAYs3vTcILLxJEb2EkVV%2F4uP0rLZDoeiGJ5NT9hbRM0Uc2zbMsp2ONjh2ZfEjMhaoxFZcXf9Vxs6mqPtAb2Sj9JxQQ9dY5vtzc1JQR6Jyy%2BBdHNjAvN%2BzgNPNVbuhob69edoKYCpSMe6WOJfQ7PFQLnZmZXNpwhAKA97BadP2V5xc%2FSoWmJVYDaD56%2BxnDCDrvs6CZSXmGS0AioaHQ94DNRN8QO%2BC&X-Amz-Signature=6f3bc93c68b9eda270a96f6cf3b1565a112c3d438f4ff3960b75016624ca6126&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJA3FZK5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCyUT9w%2F9FGilgrsjNFYOavastvvTsM1ZnVWlrqKemX2QIhALX0destCnzZoqXW1K%2Fap%2B2wAG1woR%2BNsAOPWoMdUUM3Kv8DCBsQABoMNjM3NDIzMTgzODA1IgxZ6C%2Fvjq0VyOqVYDIq3APmLb1b%2Bmeek78bnhqZZjGHCIHzHCw9e4yPt3rrVPQRgC%2B5uavsNd3U4ITxcTtJb5kuNyCQUpMiZ9%2FV3v1XnugMW9hZef2U3fc7HDigYuTJvsZ%2BWiVG0a%2FXnxFvHwSVz2kYADi8AdcQAeRnwSvfgHmfRx%2F1tTV8F45YrdioUbCMa3h3%2BZHLY8OH3dDD9SYGBzt%2FKuaea34pDoPW8vKn7jmEcix7dk3PJ4xW6f9IaA8JlxSj4djBt80XToeYpZVhSQ6H8FdfF9B5BOrRohZOlf%2FVq7NoFiLXu5Akl5bFlMmMBQd%2BTUdnxhJkg4NJHw8kEbEAVuT0zerEuws7X0xWfh1N2tLu6WTxyIfvU97ebro7mZKFgvG%2BoHTdCwo1gl6g7v4DHSfT4dUxJ0Jfj0zRkDN%2BOx%2BSeaYE2j3sscFBbyDDkcYTvJ%2BLbO5QhR9FsLVxWIP4XJ%2FXAxJ6ATlHbGJBqBNAncNy0X54fa4h8D6tTF4LxXfLsxt%2B9ZrTjRKTwYFvQK2tZwxvfy%2Bxt7%2BDPH69t61V32toSw%2FaOtRYYpCiP6cCdXTy%2BmVRNx9h2%2BsZVWMuuZa1kXNyCdXNz%2B%2Bj9pjqdh%2BdLPvYssOPmosJoeP9fPNYHQVxvCMaBAMjeu1Q0DDeg4S9BjqkAYs3vTcILLxJEb2EkVV%2F4uP0rLZDoeiGJ5NT9hbRM0Uc2zbMsp2ONjh2ZfEjMhaoxFZcXf9Vxs6mqPtAb2Sj9JxQQ9dY5vtzc1JQR6Jyy%2BBdHNjAvN%2BzgNPNVbuhob69edoKYCpSMe6WOJfQ7PFQLnZmZXNpwhAKA97BadP2V5xc%2FSoWmJVYDaD56%2BxnDCDrvs6CZSXmGS0AioaHQ94DNRN8QO%2BC&X-Amz-Signature=d3526dedf576de2ca0d2c91440cb8f47521dd2ccc9be2a551fe30a9b4336fa37&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJA3FZK5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCyUT9w%2F9FGilgrsjNFYOavastvvTsM1ZnVWlrqKemX2QIhALX0destCnzZoqXW1K%2Fap%2B2wAG1woR%2BNsAOPWoMdUUM3Kv8DCBsQABoMNjM3NDIzMTgzODA1IgxZ6C%2Fvjq0VyOqVYDIq3APmLb1b%2Bmeek78bnhqZZjGHCIHzHCw9e4yPt3rrVPQRgC%2B5uavsNd3U4ITxcTtJb5kuNyCQUpMiZ9%2FV3v1XnugMW9hZef2U3fc7HDigYuTJvsZ%2BWiVG0a%2FXnxFvHwSVz2kYADi8AdcQAeRnwSvfgHmfRx%2F1tTV8F45YrdioUbCMa3h3%2BZHLY8OH3dDD9SYGBzt%2FKuaea34pDoPW8vKn7jmEcix7dk3PJ4xW6f9IaA8JlxSj4djBt80XToeYpZVhSQ6H8FdfF9B5BOrRohZOlf%2FVq7NoFiLXu5Akl5bFlMmMBQd%2BTUdnxhJkg4NJHw8kEbEAVuT0zerEuws7X0xWfh1N2tLu6WTxyIfvU97ebro7mZKFgvG%2BoHTdCwo1gl6g7v4DHSfT4dUxJ0Jfj0zRkDN%2BOx%2BSeaYE2j3sscFBbyDDkcYTvJ%2BLbO5QhR9FsLVxWIP4XJ%2FXAxJ6ATlHbGJBqBNAncNy0X54fa4h8D6tTF4LxXfLsxt%2B9ZrTjRKTwYFvQK2tZwxvfy%2Bxt7%2BDPH69t61V32toSw%2FaOtRYYpCiP6cCdXTy%2BmVRNx9h2%2BsZVWMuuZa1kXNyCdXNz%2B%2Bj9pjqdh%2BdLPvYssOPmosJoeP9fPNYHQVxvCMaBAMjeu1Q0DDeg4S9BjqkAYs3vTcILLxJEb2EkVV%2F4uP0rLZDoeiGJ5NT9hbRM0Uc2zbMsp2ONjh2ZfEjMhaoxFZcXf9Vxs6mqPtAb2Sj9JxQQ9dY5vtzc1JQR6Jyy%2BBdHNjAvN%2BzgNPNVbuhob69edoKYCpSMe6WOJfQ7PFQLnZmZXNpwhAKA97BadP2V5xc%2FSoWmJVYDaD56%2BxnDCDrvs6CZSXmGS0AioaHQ94DNRN8QO%2BC&X-Amz-Signature=0ce07bfbee4dbffccd08c7926c0ec9066129378098398f3e01516345e827a923&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJA3FZK5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCyUT9w%2F9FGilgrsjNFYOavastvvTsM1ZnVWlrqKemX2QIhALX0destCnzZoqXW1K%2Fap%2B2wAG1woR%2BNsAOPWoMdUUM3Kv8DCBsQABoMNjM3NDIzMTgzODA1IgxZ6C%2Fvjq0VyOqVYDIq3APmLb1b%2Bmeek78bnhqZZjGHCIHzHCw9e4yPt3rrVPQRgC%2B5uavsNd3U4ITxcTtJb5kuNyCQUpMiZ9%2FV3v1XnugMW9hZef2U3fc7HDigYuTJvsZ%2BWiVG0a%2FXnxFvHwSVz2kYADi8AdcQAeRnwSvfgHmfRx%2F1tTV8F45YrdioUbCMa3h3%2BZHLY8OH3dDD9SYGBzt%2FKuaea34pDoPW8vKn7jmEcix7dk3PJ4xW6f9IaA8JlxSj4djBt80XToeYpZVhSQ6H8FdfF9B5BOrRohZOlf%2FVq7NoFiLXu5Akl5bFlMmMBQd%2BTUdnxhJkg4NJHw8kEbEAVuT0zerEuws7X0xWfh1N2tLu6WTxyIfvU97ebro7mZKFgvG%2BoHTdCwo1gl6g7v4DHSfT4dUxJ0Jfj0zRkDN%2BOx%2BSeaYE2j3sscFBbyDDkcYTvJ%2BLbO5QhR9FsLVxWIP4XJ%2FXAxJ6ATlHbGJBqBNAncNy0X54fa4h8D6tTF4LxXfLsxt%2B9ZrTjRKTwYFvQK2tZwxvfy%2Bxt7%2BDPH69t61V32toSw%2FaOtRYYpCiP6cCdXTy%2BmVRNx9h2%2BsZVWMuuZa1kXNyCdXNz%2B%2Bj9pjqdh%2BdLPvYssOPmosJoeP9fPNYHQVxvCMaBAMjeu1Q0DDeg4S9BjqkAYs3vTcILLxJEb2EkVV%2F4uP0rLZDoeiGJ5NT9hbRM0Uc2zbMsp2ONjh2ZfEjMhaoxFZcXf9Vxs6mqPtAb2Sj9JxQQ9dY5vtzc1JQR6Jyy%2BBdHNjAvN%2BzgNPNVbuhob69edoKYCpSMe6WOJfQ7PFQLnZmZXNpwhAKA97BadP2V5xc%2FSoWmJVYDaD56%2BxnDCDrvs6CZSXmGS0AioaHQ94DNRN8QO%2BC&X-Amz-Signature=d8be9211063b429dad70f21ea9c5a0b7a072e12f9ea6a1c60c0e71b271a838ae&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJA3FZK5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCyUT9w%2F9FGilgrsjNFYOavastvvTsM1ZnVWlrqKemX2QIhALX0destCnzZoqXW1K%2Fap%2B2wAG1woR%2BNsAOPWoMdUUM3Kv8DCBsQABoMNjM3NDIzMTgzODA1IgxZ6C%2Fvjq0VyOqVYDIq3APmLb1b%2Bmeek78bnhqZZjGHCIHzHCw9e4yPt3rrVPQRgC%2B5uavsNd3U4ITxcTtJb5kuNyCQUpMiZ9%2FV3v1XnugMW9hZef2U3fc7HDigYuTJvsZ%2BWiVG0a%2FXnxFvHwSVz2kYADi8AdcQAeRnwSvfgHmfRx%2F1tTV8F45YrdioUbCMa3h3%2BZHLY8OH3dDD9SYGBzt%2FKuaea34pDoPW8vKn7jmEcix7dk3PJ4xW6f9IaA8JlxSj4djBt80XToeYpZVhSQ6H8FdfF9B5BOrRohZOlf%2FVq7NoFiLXu5Akl5bFlMmMBQd%2BTUdnxhJkg4NJHw8kEbEAVuT0zerEuws7X0xWfh1N2tLu6WTxyIfvU97ebro7mZKFgvG%2BoHTdCwo1gl6g7v4DHSfT4dUxJ0Jfj0zRkDN%2BOx%2BSeaYE2j3sscFBbyDDkcYTvJ%2BLbO5QhR9FsLVxWIP4XJ%2FXAxJ6ATlHbGJBqBNAncNy0X54fa4h8D6tTF4LxXfLsxt%2B9ZrTjRKTwYFvQK2tZwxvfy%2Bxt7%2BDPH69t61V32toSw%2FaOtRYYpCiP6cCdXTy%2BmVRNx9h2%2BsZVWMuuZa1kXNyCdXNz%2B%2Bj9pjqdh%2BdLPvYssOPmosJoeP9fPNYHQVxvCMaBAMjeu1Q0DDeg4S9BjqkAYs3vTcILLxJEb2EkVV%2F4uP0rLZDoeiGJ5NT9hbRM0Uc2zbMsp2ONjh2ZfEjMhaoxFZcXf9Vxs6mqPtAb2Sj9JxQQ9dY5vtzc1JQR6Jyy%2BBdHNjAvN%2BzgNPNVbuhob69edoKYCpSMe6WOJfQ7PFQLnZmZXNpwhAKA97BadP2V5xc%2FSoWmJVYDaD56%2BxnDCDrvs6CZSXmGS0AioaHQ94DNRN8QO%2BC&X-Amz-Signature=8a6514e197c56a83050eda06d73c397cd5874ae111f23dce601689bc37d4156a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJA3FZK5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCyUT9w%2F9FGilgrsjNFYOavastvvTsM1ZnVWlrqKemX2QIhALX0destCnzZoqXW1K%2Fap%2B2wAG1woR%2BNsAOPWoMdUUM3Kv8DCBsQABoMNjM3NDIzMTgzODA1IgxZ6C%2Fvjq0VyOqVYDIq3APmLb1b%2Bmeek78bnhqZZjGHCIHzHCw9e4yPt3rrVPQRgC%2B5uavsNd3U4ITxcTtJb5kuNyCQUpMiZ9%2FV3v1XnugMW9hZef2U3fc7HDigYuTJvsZ%2BWiVG0a%2FXnxFvHwSVz2kYADi8AdcQAeRnwSvfgHmfRx%2F1tTV8F45YrdioUbCMa3h3%2BZHLY8OH3dDD9SYGBzt%2FKuaea34pDoPW8vKn7jmEcix7dk3PJ4xW6f9IaA8JlxSj4djBt80XToeYpZVhSQ6H8FdfF9B5BOrRohZOlf%2FVq7NoFiLXu5Akl5bFlMmMBQd%2BTUdnxhJkg4NJHw8kEbEAVuT0zerEuws7X0xWfh1N2tLu6WTxyIfvU97ebro7mZKFgvG%2BoHTdCwo1gl6g7v4DHSfT4dUxJ0Jfj0zRkDN%2BOx%2BSeaYE2j3sscFBbyDDkcYTvJ%2BLbO5QhR9FsLVxWIP4XJ%2FXAxJ6ATlHbGJBqBNAncNy0X54fa4h8D6tTF4LxXfLsxt%2B9ZrTjRKTwYFvQK2tZwxvfy%2Bxt7%2BDPH69t61V32toSw%2FaOtRYYpCiP6cCdXTy%2BmVRNx9h2%2BsZVWMuuZa1kXNyCdXNz%2B%2Bj9pjqdh%2BdLPvYssOPmosJoeP9fPNYHQVxvCMaBAMjeu1Q0DDeg4S9BjqkAYs3vTcILLxJEb2EkVV%2F4uP0rLZDoeiGJ5NT9hbRM0Uc2zbMsp2ONjh2ZfEjMhaoxFZcXf9Vxs6mqPtAb2Sj9JxQQ9dY5vtzc1JQR6Jyy%2BBdHNjAvN%2BzgNPNVbuhob69edoKYCpSMe6WOJfQ7PFQLnZmZXNpwhAKA97BadP2V5xc%2FSoWmJVYDaD56%2BxnDCDrvs6CZSXmGS0AioaHQ94DNRN8QO%2BC&X-Amz-Signature=f0009771c4e2b2fb0e166b2bda015edde4cf7b1639c69a69574c9cecb7e82e5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJA3FZK5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCyUT9w%2F9FGilgrsjNFYOavastvvTsM1ZnVWlrqKemX2QIhALX0destCnzZoqXW1K%2Fap%2B2wAG1woR%2BNsAOPWoMdUUM3Kv8DCBsQABoMNjM3NDIzMTgzODA1IgxZ6C%2Fvjq0VyOqVYDIq3APmLb1b%2Bmeek78bnhqZZjGHCIHzHCw9e4yPt3rrVPQRgC%2B5uavsNd3U4ITxcTtJb5kuNyCQUpMiZ9%2FV3v1XnugMW9hZef2U3fc7HDigYuTJvsZ%2BWiVG0a%2FXnxFvHwSVz2kYADi8AdcQAeRnwSvfgHmfRx%2F1tTV8F45YrdioUbCMa3h3%2BZHLY8OH3dDD9SYGBzt%2FKuaea34pDoPW8vKn7jmEcix7dk3PJ4xW6f9IaA8JlxSj4djBt80XToeYpZVhSQ6H8FdfF9B5BOrRohZOlf%2FVq7NoFiLXu5Akl5bFlMmMBQd%2BTUdnxhJkg4NJHw8kEbEAVuT0zerEuws7X0xWfh1N2tLu6WTxyIfvU97ebro7mZKFgvG%2BoHTdCwo1gl6g7v4DHSfT4dUxJ0Jfj0zRkDN%2BOx%2BSeaYE2j3sscFBbyDDkcYTvJ%2BLbO5QhR9FsLVxWIP4XJ%2FXAxJ6ATlHbGJBqBNAncNy0X54fa4h8D6tTF4LxXfLsxt%2B9ZrTjRKTwYFvQK2tZwxvfy%2Bxt7%2BDPH69t61V32toSw%2FaOtRYYpCiP6cCdXTy%2BmVRNx9h2%2BsZVWMuuZa1kXNyCdXNz%2B%2Bj9pjqdh%2BdLPvYssOPmosJoeP9fPNYHQVxvCMaBAMjeu1Q0DDeg4S9BjqkAYs3vTcILLxJEb2EkVV%2F4uP0rLZDoeiGJ5NT9hbRM0Uc2zbMsp2ONjh2ZfEjMhaoxFZcXf9Vxs6mqPtAb2Sj9JxQQ9dY5vtzc1JQR6Jyy%2BBdHNjAvN%2BzgNPNVbuhob69edoKYCpSMe6WOJfQ7PFQLnZmZXNpwhAKA97BadP2V5xc%2FSoWmJVYDaD56%2BxnDCDrvs6CZSXmGS0AioaHQ94DNRN8QO%2BC&X-Amz-Signature=d283a99d3c1251d68fe221229ecbaff9ba421181be3f9f74462fe308b929d224&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XD4O3JH3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCYJVcngi7F00QbVWYMIsUe9CkIOZyi%2FmieHZNt6r5o4AIgEreeodJZ0aRFJrnnmLcGe%2Fm%2BJHgZlYblUmvclPdcNGYq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDJ82fHtI%2B5dmsTBAcyrcA4XKGDEbXg0XCZGsr%2Bdc1Ggc7BZ7FZX7GXwhYnNYrz8t%2FuRqycb%2FREvNJfEarnavo%2B7Jru7LVHoVYnlsEBG7r7acmXlh09AcU1TWxrpy3jDzuWnq905MdU7zPxEhS2VvVJ2Z%2BZ4nreu4ChxrV9YaevKjl%2BJnGvjPz1M2PB85RCg%2FUzlPecevV8QvYkisvn6XtKYMtOX0bXJ6EaCJMoBPRh3262FkK8ec2G9wypiGFlvWOtc%2Frd8Ror%2BeuaR%2Ba2rTCVEhh7mFajnRUO7hW%2FBmmUSL9WmxQMQDXRBfxGo1UVpySa8XWBRtJAe%2Fhpeee%2BdhwJhxIE%2FVAxCuxdA61wyMjxgKpWMEtLGpYD5gUnLqjjWIZNZXTF%2BaKjgMoU%2BTeHYSo1xUlV%2FVpwiDJ1cHTYN8jFncksrj1teFO1b%2Bznrknwfuxcs6ssSQVbx6QXmP%2FT8mpC9j3ztejYEeoKcttAtSmkQ2CApYXZzMoKCj5QeybDPJKNGAbLLrr1L1zi11UKZe4wn2K1lIeyhVqtzA6pKJQZPJxaO6fnQkXUyQHKLE8K5EjSmumLai%2FIlRG%2F%2BFKsvOH9Xzltp6uk9RsiKumw15WYQnQpfosFUGo5IUQmyLKOV%2BnU1BzR9XiCbM5Gj1MJaDhL0GOqUB7dBqShZhttoSpxTwj%2B1RL1cOJFn4HBLD0GhnvupVBbePMprnCFzjqPOpmETLk%2FD%2Fs1i9S8pdhN3S%2BcxmWjiW2P6QRM%2Fh7wTzTdX19ZHQxT74CzPg0Ne9QjlzDL31GIGMSWFwfyJTQvKkjd7frz01AVYz5JBMFkvpR56Kg4iP3FHMjxmv2l8xJ852J04wTH2VK61ab4RXb1xTlVIzwTJLLrOcLhs5&X-Amz-Signature=f2b070ec35310f0d686efd5b3e3f47373eda660e5ad070a2c99961679276ff85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XD4O3JH3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCYJVcngi7F00QbVWYMIsUe9CkIOZyi%2FmieHZNt6r5o4AIgEreeodJZ0aRFJrnnmLcGe%2Fm%2BJHgZlYblUmvclPdcNGYq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDJ82fHtI%2B5dmsTBAcyrcA4XKGDEbXg0XCZGsr%2Bdc1Ggc7BZ7FZX7GXwhYnNYrz8t%2FuRqycb%2FREvNJfEarnavo%2B7Jru7LVHoVYnlsEBG7r7acmXlh09AcU1TWxrpy3jDzuWnq905MdU7zPxEhS2VvVJ2Z%2BZ4nreu4ChxrV9YaevKjl%2BJnGvjPz1M2PB85RCg%2FUzlPecevV8QvYkisvn6XtKYMtOX0bXJ6EaCJMoBPRh3262FkK8ec2G9wypiGFlvWOtc%2Frd8Ror%2BeuaR%2Ba2rTCVEhh7mFajnRUO7hW%2FBmmUSL9WmxQMQDXRBfxGo1UVpySa8XWBRtJAe%2Fhpeee%2BdhwJhxIE%2FVAxCuxdA61wyMjxgKpWMEtLGpYD5gUnLqjjWIZNZXTF%2BaKjgMoU%2BTeHYSo1xUlV%2FVpwiDJ1cHTYN8jFncksrj1teFO1b%2Bznrknwfuxcs6ssSQVbx6QXmP%2FT8mpC9j3ztejYEeoKcttAtSmkQ2CApYXZzMoKCj5QeybDPJKNGAbLLrr1L1zi11UKZe4wn2K1lIeyhVqtzA6pKJQZPJxaO6fnQkXUyQHKLE8K5EjSmumLai%2FIlRG%2F%2BFKsvOH9Xzltp6uk9RsiKumw15WYQnQpfosFUGo5IUQmyLKOV%2BnU1BzR9XiCbM5Gj1MJaDhL0GOqUB7dBqShZhttoSpxTwj%2B1RL1cOJFn4HBLD0GhnvupVBbePMprnCFzjqPOpmETLk%2FD%2Fs1i9S8pdhN3S%2BcxmWjiW2P6QRM%2Fh7wTzTdX19ZHQxT74CzPg0Ne9QjlzDL31GIGMSWFwfyJTQvKkjd7frz01AVYz5JBMFkvpR56Kg4iP3FHMjxmv2l8xJ852J04wTH2VK61ab4RXb1xTlVIzwTJLLrOcLhs5&X-Amz-Signature=038df894f6437fe6a1076b73a0aa50eee30e0d00cb4ba3deed425fe9906c62db&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
