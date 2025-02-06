

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2ZCUHS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAG6nwHB9eIrAWJY2UhSdxSGpZSbEbVQ9MWvds99ZxoYAiABmE%2FexOtxJlglaqpxA79VCvXqV1ZxUWtjC5U2oZn1Sir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMPSJeuR3QJ7GL2UbbKtwDztgYA0%2BxhJLh7B3%2BH%2B2uTL3nXVWWe88m2vHVKJteIi%2BObZ1gNffbGqq6DuhJ98rMBdC92LQyk0niqNLbQroJZdlfKMrfXwFfV0Yk13048ckjBYwuNIwPeiXMKVVsAFNKrBg96B7movybiGSlB4kYD5rEaNBajbb62dF08YcHM%2FDEcYYt4ai3zz8WipG5xKDxw7%2Bax%2BuaaKNvgsJgi1aPuwsVeJCqK18da32%2FIC%2FsdbDSuXuhHvxiZud7RFW%2FHS%2BBTDwaF6wPyUAwASH79CVo%2FQdX%2F9PN7IkECvv26nd1%2BaN9r44GIkvXmsq3UQSn45lNxrw4EBuK0FvN26DJMZpoQoWpTgkclqyByjd0gqGXdivQEIoh0IkwD9O5j%2BqBiFqo6NovU4f3RXB%2F3b%2BHLUl%2BRahKVn0nZo0Ah2buEqAi7dGlos3sJho6KYusBV%2FR74EY0hb%2F82tdl6k4BIeqELxT%2FgRhrPm8Xs2pwXbX85qD%2FLuqAZhy0dbRnLYd4mPOzD%2F8jt%2Bv1XX%2F%2F7zrMG7k0mo%2Bx%2BJFLwrMDHpLUQL8BAATKQSofqV7wKEsmupa1Ve0g4KNMyxTjLgbUk6SdGCSsrjIJsOzDA7Z8hQggYdw3v1K2iDTBmss4wEUDYWUYOownuyRvQY6pgHvgHQwXhJeQGVfev%2Fp%2BnfpNakLA49otyzE56HYuQzCErmus9mDaEbboalqA%2FpLY%2BJC0ECeZFNiAWOkSNLSHtiGVfkNGIp9y17a6XABcthvg4k9N9gqwZAz5RTuyqO3rMnOWNcSnnSsMnKUQG7%2B08s6RlJmOwMqIOopMvoETWf5GdTXzXncVhXEa0ld7P%2B6aIW6%2BtLyoDazfNhkX16hr5SmsY4gaU3Q&X-Amz-Signature=46fffc35b7919778dec3018ce7848f43195e6c6f21ef123643bc2db2f36ebc0a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2ZCUHS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAG6nwHB9eIrAWJY2UhSdxSGpZSbEbVQ9MWvds99ZxoYAiABmE%2FexOtxJlglaqpxA79VCvXqV1ZxUWtjC5U2oZn1Sir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMPSJeuR3QJ7GL2UbbKtwDztgYA0%2BxhJLh7B3%2BH%2B2uTL3nXVWWe88m2vHVKJteIi%2BObZ1gNffbGqq6DuhJ98rMBdC92LQyk0niqNLbQroJZdlfKMrfXwFfV0Yk13048ckjBYwuNIwPeiXMKVVsAFNKrBg96B7movybiGSlB4kYD5rEaNBajbb62dF08YcHM%2FDEcYYt4ai3zz8WipG5xKDxw7%2Bax%2BuaaKNvgsJgi1aPuwsVeJCqK18da32%2FIC%2FsdbDSuXuhHvxiZud7RFW%2FHS%2BBTDwaF6wPyUAwASH79CVo%2FQdX%2F9PN7IkECvv26nd1%2BaN9r44GIkvXmsq3UQSn45lNxrw4EBuK0FvN26DJMZpoQoWpTgkclqyByjd0gqGXdivQEIoh0IkwD9O5j%2BqBiFqo6NovU4f3RXB%2F3b%2BHLUl%2BRahKVn0nZo0Ah2buEqAi7dGlos3sJho6KYusBV%2FR74EY0hb%2F82tdl6k4BIeqELxT%2FgRhrPm8Xs2pwXbX85qD%2FLuqAZhy0dbRnLYd4mPOzD%2F8jt%2Bv1XX%2F%2F7zrMG7k0mo%2Bx%2BJFLwrMDHpLUQL8BAATKQSofqV7wKEsmupa1Ve0g4KNMyxTjLgbUk6SdGCSsrjIJsOzDA7Z8hQggYdw3v1K2iDTBmss4wEUDYWUYOownuyRvQY6pgHvgHQwXhJeQGVfev%2Fp%2BnfpNakLA49otyzE56HYuQzCErmus9mDaEbboalqA%2FpLY%2BJC0ECeZFNiAWOkSNLSHtiGVfkNGIp9y17a6XABcthvg4k9N9gqwZAz5RTuyqO3rMnOWNcSnnSsMnKUQG7%2B08s6RlJmOwMqIOopMvoETWf5GdTXzXncVhXEa0ld7P%2B6aIW6%2BtLyoDazfNhkX16hr5SmsY4gaU3Q&X-Amz-Signature=25e5e535180c0ac983e2d58b7cecbc8f454067e18a235628b96cf67da9e60527&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2ZCUHS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAG6nwHB9eIrAWJY2UhSdxSGpZSbEbVQ9MWvds99ZxoYAiABmE%2FexOtxJlglaqpxA79VCvXqV1ZxUWtjC5U2oZn1Sir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMPSJeuR3QJ7GL2UbbKtwDztgYA0%2BxhJLh7B3%2BH%2B2uTL3nXVWWe88m2vHVKJteIi%2BObZ1gNffbGqq6DuhJ98rMBdC92LQyk0niqNLbQroJZdlfKMrfXwFfV0Yk13048ckjBYwuNIwPeiXMKVVsAFNKrBg96B7movybiGSlB4kYD5rEaNBajbb62dF08YcHM%2FDEcYYt4ai3zz8WipG5xKDxw7%2Bax%2BuaaKNvgsJgi1aPuwsVeJCqK18da32%2FIC%2FsdbDSuXuhHvxiZud7RFW%2FHS%2BBTDwaF6wPyUAwASH79CVo%2FQdX%2F9PN7IkECvv26nd1%2BaN9r44GIkvXmsq3UQSn45lNxrw4EBuK0FvN26DJMZpoQoWpTgkclqyByjd0gqGXdivQEIoh0IkwD9O5j%2BqBiFqo6NovU4f3RXB%2F3b%2BHLUl%2BRahKVn0nZo0Ah2buEqAi7dGlos3sJho6KYusBV%2FR74EY0hb%2F82tdl6k4BIeqELxT%2FgRhrPm8Xs2pwXbX85qD%2FLuqAZhy0dbRnLYd4mPOzD%2F8jt%2Bv1XX%2F%2F7zrMG7k0mo%2Bx%2BJFLwrMDHpLUQL8BAATKQSofqV7wKEsmupa1Ve0g4KNMyxTjLgbUk6SdGCSsrjIJsOzDA7Z8hQggYdw3v1K2iDTBmss4wEUDYWUYOownuyRvQY6pgHvgHQwXhJeQGVfev%2Fp%2BnfpNakLA49otyzE56HYuQzCErmus9mDaEbboalqA%2FpLY%2BJC0ECeZFNiAWOkSNLSHtiGVfkNGIp9y17a6XABcthvg4k9N9gqwZAz5RTuyqO3rMnOWNcSnnSsMnKUQG7%2B08s6RlJmOwMqIOopMvoETWf5GdTXzXncVhXEa0ld7P%2B6aIW6%2BtLyoDazfNhkX16hr5SmsY4gaU3Q&X-Amz-Signature=cecaf44625f261df9baeb01b195aceac2861eb133f04fac08c8a06f14d7482c6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2ZCUHS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAG6nwHB9eIrAWJY2UhSdxSGpZSbEbVQ9MWvds99ZxoYAiABmE%2FexOtxJlglaqpxA79VCvXqV1ZxUWtjC5U2oZn1Sir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMPSJeuR3QJ7GL2UbbKtwDztgYA0%2BxhJLh7B3%2BH%2B2uTL3nXVWWe88m2vHVKJteIi%2BObZ1gNffbGqq6DuhJ98rMBdC92LQyk0niqNLbQroJZdlfKMrfXwFfV0Yk13048ckjBYwuNIwPeiXMKVVsAFNKrBg96B7movybiGSlB4kYD5rEaNBajbb62dF08YcHM%2FDEcYYt4ai3zz8WipG5xKDxw7%2Bax%2BuaaKNvgsJgi1aPuwsVeJCqK18da32%2FIC%2FsdbDSuXuhHvxiZud7RFW%2FHS%2BBTDwaF6wPyUAwASH79CVo%2FQdX%2F9PN7IkECvv26nd1%2BaN9r44GIkvXmsq3UQSn45lNxrw4EBuK0FvN26DJMZpoQoWpTgkclqyByjd0gqGXdivQEIoh0IkwD9O5j%2BqBiFqo6NovU4f3RXB%2F3b%2BHLUl%2BRahKVn0nZo0Ah2buEqAi7dGlos3sJho6KYusBV%2FR74EY0hb%2F82tdl6k4BIeqELxT%2FgRhrPm8Xs2pwXbX85qD%2FLuqAZhy0dbRnLYd4mPOzD%2F8jt%2Bv1XX%2F%2F7zrMG7k0mo%2Bx%2BJFLwrMDHpLUQL8BAATKQSofqV7wKEsmupa1Ve0g4KNMyxTjLgbUk6SdGCSsrjIJsOzDA7Z8hQggYdw3v1K2iDTBmss4wEUDYWUYOownuyRvQY6pgHvgHQwXhJeQGVfev%2Fp%2BnfpNakLA49otyzE56HYuQzCErmus9mDaEbboalqA%2FpLY%2BJC0ECeZFNiAWOkSNLSHtiGVfkNGIp9y17a6XABcthvg4k9N9gqwZAz5RTuyqO3rMnOWNcSnnSsMnKUQG7%2B08s6RlJmOwMqIOopMvoETWf5GdTXzXncVhXEa0ld7P%2B6aIW6%2BtLyoDazfNhkX16hr5SmsY4gaU3Q&X-Amz-Signature=babb2c97e2d9e3cae9f614df6c5f9a6d4155d4f849b6d160ce2bd8bc8dac142f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2ZCUHS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAG6nwHB9eIrAWJY2UhSdxSGpZSbEbVQ9MWvds99ZxoYAiABmE%2FexOtxJlglaqpxA79VCvXqV1ZxUWtjC5U2oZn1Sir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMPSJeuR3QJ7GL2UbbKtwDztgYA0%2BxhJLh7B3%2BH%2B2uTL3nXVWWe88m2vHVKJteIi%2BObZ1gNffbGqq6DuhJ98rMBdC92LQyk0niqNLbQroJZdlfKMrfXwFfV0Yk13048ckjBYwuNIwPeiXMKVVsAFNKrBg96B7movybiGSlB4kYD5rEaNBajbb62dF08YcHM%2FDEcYYt4ai3zz8WipG5xKDxw7%2Bax%2BuaaKNvgsJgi1aPuwsVeJCqK18da32%2FIC%2FsdbDSuXuhHvxiZud7RFW%2FHS%2BBTDwaF6wPyUAwASH79CVo%2FQdX%2F9PN7IkECvv26nd1%2BaN9r44GIkvXmsq3UQSn45lNxrw4EBuK0FvN26DJMZpoQoWpTgkclqyByjd0gqGXdivQEIoh0IkwD9O5j%2BqBiFqo6NovU4f3RXB%2F3b%2BHLUl%2BRahKVn0nZo0Ah2buEqAi7dGlos3sJho6KYusBV%2FR74EY0hb%2F82tdl6k4BIeqELxT%2FgRhrPm8Xs2pwXbX85qD%2FLuqAZhy0dbRnLYd4mPOzD%2F8jt%2Bv1XX%2F%2F7zrMG7k0mo%2Bx%2BJFLwrMDHpLUQL8BAATKQSofqV7wKEsmupa1Ve0g4KNMyxTjLgbUk6SdGCSsrjIJsOzDA7Z8hQggYdw3v1K2iDTBmss4wEUDYWUYOownuyRvQY6pgHvgHQwXhJeQGVfev%2Fp%2BnfpNakLA49otyzE56HYuQzCErmus9mDaEbboalqA%2FpLY%2BJC0ECeZFNiAWOkSNLSHtiGVfkNGIp9y17a6XABcthvg4k9N9gqwZAz5RTuyqO3rMnOWNcSnnSsMnKUQG7%2B08s6RlJmOwMqIOopMvoETWf5GdTXzXncVhXEa0ld7P%2B6aIW6%2BtLyoDazfNhkX16hr5SmsY4gaU3Q&X-Amz-Signature=3fe47caf40106bc104fcbef5d1b016f2dd60cb7da7abde0fba4168dfc3414542&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2ZCUHS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAG6nwHB9eIrAWJY2UhSdxSGpZSbEbVQ9MWvds99ZxoYAiABmE%2FexOtxJlglaqpxA79VCvXqV1ZxUWtjC5U2oZn1Sir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMPSJeuR3QJ7GL2UbbKtwDztgYA0%2BxhJLh7B3%2BH%2B2uTL3nXVWWe88m2vHVKJteIi%2BObZ1gNffbGqq6DuhJ98rMBdC92LQyk0niqNLbQroJZdlfKMrfXwFfV0Yk13048ckjBYwuNIwPeiXMKVVsAFNKrBg96B7movybiGSlB4kYD5rEaNBajbb62dF08YcHM%2FDEcYYt4ai3zz8WipG5xKDxw7%2Bax%2BuaaKNvgsJgi1aPuwsVeJCqK18da32%2FIC%2FsdbDSuXuhHvxiZud7RFW%2FHS%2BBTDwaF6wPyUAwASH79CVo%2FQdX%2F9PN7IkECvv26nd1%2BaN9r44GIkvXmsq3UQSn45lNxrw4EBuK0FvN26DJMZpoQoWpTgkclqyByjd0gqGXdivQEIoh0IkwD9O5j%2BqBiFqo6NovU4f3RXB%2F3b%2BHLUl%2BRahKVn0nZo0Ah2buEqAi7dGlos3sJho6KYusBV%2FR74EY0hb%2F82tdl6k4BIeqELxT%2FgRhrPm8Xs2pwXbX85qD%2FLuqAZhy0dbRnLYd4mPOzD%2F8jt%2Bv1XX%2F%2F7zrMG7k0mo%2Bx%2BJFLwrMDHpLUQL8BAATKQSofqV7wKEsmupa1Ve0g4KNMyxTjLgbUk6SdGCSsrjIJsOzDA7Z8hQggYdw3v1K2iDTBmss4wEUDYWUYOownuyRvQY6pgHvgHQwXhJeQGVfev%2Fp%2BnfpNakLA49otyzE56HYuQzCErmus9mDaEbboalqA%2FpLY%2BJC0ECeZFNiAWOkSNLSHtiGVfkNGIp9y17a6XABcthvg4k9N9gqwZAz5RTuyqO3rMnOWNcSnnSsMnKUQG7%2B08s6RlJmOwMqIOopMvoETWf5GdTXzXncVhXEa0ld7P%2B6aIW6%2BtLyoDazfNhkX16hr5SmsY4gaU3Q&X-Amz-Signature=1ff1f0e850e54e8c0ea7510a26762a5082badab3ec2a7ec624a1853c06776330&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2ZCUHS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAG6nwHB9eIrAWJY2UhSdxSGpZSbEbVQ9MWvds99ZxoYAiABmE%2FexOtxJlglaqpxA79VCvXqV1ZxUWtjC5U2oZn1Sir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMPSJeuR3QJ7GL2UbbKtwDztgYA0%2BxhJLh7B3%2BH%2B2uTL3nXVWWe88m2vHVKJteIi%2BObZ1gNffbGqq6DuhJ98rMBdC92LQyk0niqNLbQroJZdlfKMrfXwFfV0Yk13048ckjBYwuNIwPeiXMKVVsAFNKrBg96B7movybiGSlB4kYD5rEaNBajbb62dF08YcHM%2FDEcYYt4ai3zz8WipG5xKDxw7%2Bax%2BuaaKNvgsJgi1aPuwsVeJCqK18da32%2FIC%2FsdbDSuXuhHvxiZud7RFW%2FHS%2BBTDwaF6wPyUAwASH79CVo%2FQdX%2F9PN7IkECvv26nd1%2BaN9r44GIkvXmsq3UQSn45lNxrw4EBuK0FvN26DJMZpoQoWpTgkclqyByjd0gqGXdivQEIoh0IkwD9O5j%2BqBiFqo6NovU4f3RXB%2F3b%2BHLUl%2BRahKVn0nZo0Ah2buEqAi7dGlos3sJho6KYusBV%2FR74EY0hb%2F82tdl6k4BIeqELxT%2FgRhrPm8Xs2pwXbX85qD%2FLuqAZhy0dbRnLYd4mPOzD%2F8jt%2Bv1XX%2F%2F7zrMG7k0mo%2Bx%2BJFLwrMDHpLUQL8BAATKQSofqV7wKEsmupa1Ve0g4KNMyxTjLgbUk6SdGCSsrjIJsOzDA7Z8hQggYdw3v1K2iDTBmss4wEUDYWUYOownuyRvQY6pgHvgHQwXhJeQGVfev%2Fp%2BnfpNakLA49otyzE56HYuQzCErmus9mDaEbboalqA%2FpLY%2BJC0ECeZFNiAWOkSNLSHtiGVfkNGIp9y17a6XABcthvg4k9N9gqwZAz5RTuyqO3rMnOWNcSnnSsMnKUQG7%2B08s6RlJmOwMqIOopMvoETWf5GdTXzXncVhXEa0ld7P%2B6aIW6%2BtLyoDazfNhkX16hr5SmsY4gaU3Q&X-Amz-Signature=b943b8318eff92dc1cbf264c9e2f77302390c2dfa9a5f7cd6fa3e80dc05d3a9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2ZCUHS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAG6nwHB9eIrAWJY2UhSdxSGpZSbEbVQ9MWvds99ZxoYAiABmE%2FexOtxJlglaqpxA79VCvXqV1ZxUWtjC5U2oZn1Sir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMPSJeuR3QJ7GL2UbbKtwDztgYA0%2BxhJLh7B3%2BH%2B2uTL3nXVWWe88m2vHVKJteIi%2BObZ1gNffbGqq6DuhJ98rMBdC92LQyk0niqNLbQroJZdlfKMrfXwFfV0Yk13048ckjBYwuNIwPeiXMKVVsAFNKrBg96B7movybiGSlB4kYD5rEaNBajbb62dF08YcHM%2FDEcYYt4ai3zz8WipG5xKDxw7%2Bax%2BuaaKNvgsJgi1aPuwsVeJCqK18da32%2FIC%2FsdbDSuXuhHvxiZud7RFW%2FHS%2BBTDwaF6wPyUAwASH79CVo%2FQdX%2F9PN7IkECvv26nd1%2BaN9r44GIkvXmsq3UQSn45lNxrw4EBuK0FvN26DJMZpoQoWpTgkclqyByjd0gqGXdivQEIoh0IkwD9O5j%2BqBiFqo6NovU4f3RXB%2F3b%2BHLUl%2BRahKVn0nZo0Ah2buEqAi7dGlos3sJho6KYusBV%2FR74EY0hb%2F82tdl6k4BIeqELxT%2FgRhrPm8Xs2pwXbX85qD%2FLuqAZhy0dbRnLYd4mPOzD%2F8jt%2Bv1XX%2F%2F7zrMG7k0mo%2Bx%2BJFLwrMDHpLUQL8BAATKQSofqV7wKEsmupa1Ve0g4KNMyxTjLgbUk6SdGCSsrjIJsOzDA7Z8hQggYdw3v1K2iDTBmss4wEUDYWUYOownuyRvQY6pgHvgHQwXhJeQGVfev%2Fp%2BnfpNakLA49otyzE56HYuQzCErmus9mDaEbboalqA%2FpLY%2BJC0ECeZFNiAWOkSNLSHtiGVfkNGIp9y17a6XABcthvg4k9N9gqwZAz5RTuyqO3rMnOWNcSnnSsMnKUQG7%2B08s6RlJmOwMqIOopMvoETWf5GdTXzXncVhXEa0ld7P%2B6aIW6%2BtLyoDazfNhkX16hr5SmsY4gaU3Q&X-Amz-Signature=8b96151f576246d9b5edcddf1d526c7a66e0f842057ae49c8d6b8af74a72ffe2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM2ZCUHS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAG6nwHB9eIrAWJY2UhSdxSGpZSbEbVQ9MWvds99ZxoYAiABmE%2FexOtxJlglaqpxA79VCvXqV1ZxUWtjC5U2oZn1Sir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMPSJeuR3QJ7GL2UbbKtwDztgYA0%2BxhJLh7B3%2BH%2B2uTL3nXVWWe88m2vHVKJteIi%2BObZ1gNffbGqq6DuhJ98rMBdC92LQyk0niqNLbQroJZdlfKMrfXwFfV0Yk13048ckjBYwuNIwPeiXMKVVsAFNKrBg96B7movybiGSlB4kYD5rEaNBajbb62dF08YcHM%2FDEcYYt4ai3zz8WipG5xKDxw7%2Bax%2BuaaKNvgsJgi1aPuwsVeJCqK18da32%2FIC%2FsdbDSuXuhHvxiZud7RFW%2FHS%2BBTDwaF6wPyUAwASH79CVo%2FQdX%2F9PN7IkECvv26nd1%2BaN9r44GIkvXmsq3UQSn45lNxrw4EBuK0FvN26DJMZpoQoWpTgkclqyByjd0gqGXdivQEIoh0IkwD9O5j%2BqBiFqo6NovU4f3RXB%2F3b%2BHLUl%2BRahKVn0nZo0Ah2buEqAi7dGlos3sJho6KYusBV%2FR74EY0hb%2F82tdl6k4BIeqELxT%2FgRhrPm8Xs2pwXbX85qD%2FLuqAZhy0dbRnLYd4mPOzD%2F8jt%2Bv1XX%2F%2F7zrMG7k0mo%2Bx%2BJFLwrMDHpLUQL8BAATKQSofqV7wKEsmupa1Ve0g4KNMyxTjLgbUk6SdGCSsrjIJsOzDA7Z8hQggYdw3v1K2iDTBmss4wEUDYWUYOownuyRvQY6pgHvgHQwXhJeQGVfev%2Fp%2BnfpNakLA49otyzE56HYuQzCErmus9mDaEbboalqA%2FpLY%2BJC0ECeZFNiAWOkSNLSHtiGVfkNGIp9y17a6XABcthvg4k9N9gqwZAz5RTuyqO3rMnOWNcSnnSsMnKUQG7%2B08s6RlJmOwMqIOopMvoETWf5GdTXzXncVhXEa0ld7P%2B6aIW6%2BtLyoDazfNhkX16hr5SmsY4gaU3Q&X-Amz-Signature=718a798b4ab7c0a5dcc05e95de79a4d54bf6c39b5ade49dd93da12195859b271&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZDABRTG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDp3rGVM5iLbvp4VuCeaqD9Mb7z7kfaxxQ02ogErtVKwwIgdiOtryYrzawlu9rRa%2F1tFopk94NeNWlLYOFPvh%2FJ0SUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFzyW2WR5FAoj2dylircA9bRvVAEoPKP3L7uzJSUubzWKtw%2BlGltMDA1xzLLOylVOM9nXT9ElWjwsE7gtBsEMNsa08xczZYFoo%2Fo9738fzSeOQL5Qnt6mL1CjEcWeqCfJDAQnHlqlFPUcohqxToNQZVcL8kSKLvnsgU779e9rXpa5ItAnMV1tnc4BFLqSnbNFkleMdrlxusoT1TLmMk27l7sQg5A%2BnmRgAmRnL5HgwFAdDIiidTbjlTRl%2Bj%2BKLPrtKGymVKzRgUhRjn0zYeQz8lAU3R%2BcZbKy1oRFb9Pq0siqHIQ3%2Bkg9SC3WXmVuDAgfMQdEK7UpOJ%2BtLNLb1Il7tMsWvWmW5Rk3LQeYgG2JdqY50U2pnLcq6yCTzK1M8mcnD3bGx%2FVe9jS5chKVEQByDxLNQjhldeQ2kpDlC2OiOy5yY0GqAPQa3rGE8mcGa8pSQb%2BGLNtb9Ph2fw8PxUUfh8oyTWyvW21nNQrExnzEBatCb%2BnG5cFG5JGC%2FjAG%2Fr5zZUUVrqUuB9sCl7VhVmQLbg3nuAqy%2BSJ6hVkvS0fLx%2BEn02OmDHc5d93ZNr2lj1hrZaU%2FdgnEGx77F2ZtfVxyvSyUwUi%2FSNKfgBO2lZlBmWUNJHV%2FYA64WJRwz6ryugcDa9iqtiuRFgLDswBMN%2Frkb0GOqUBW2HhRhLikNuuPRwyENwMhhgnHxlUDLISurFYrDfkvZev8EjSCiFsH8L%2F0wLxYWQj3%2BSqArc%2F8vPayB7frviJWQK%2B5DC4r2gfIjrbreaeq5agC9SUgEYCMX67hliEs7%2FNv6RAYtxKs0S30kEJ3SC5EgCtT4pT51nTefGLDNMup1YzQIZhxUwjzuq6rPBI4Ossft4DfCTAoYW8%2FXqiI2sVA67oTKGb&X-Amz-Signature=56ed9de43f7770a8831471f8898c7517c188afea5741beae22e4658ef8e5efd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZDABRTG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDp3rGVM5iLbvp4VuCeaqD9Mb7z7kfaxxQ02ogErtVKwwIgdiOtryYrzawlu9rRa%2F1tFopk94NeNWlLYOFPvh%2FJ0SUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFzyW2WR5FAoj2dylircA9bRvVAEoPKP3L7uzJSUubzWKtw%2BlGltMDA1xzLLOylVOM9nXT9ElWjwsE7gtBsEMNsa08xczZYFoo%2Fo9738fzSeOQL5Qnt6mL1CjEcWeqCfJDAQnHlqlFPUcohqxToNQZVcL8kSKLvnsgU779e9rXpa5ItAnMV1tnc4BFLqSnbNFkleMdrlxusoT1TLmMk27l7sQg5A%2BnmRgAmRnL5HgwFAdDIiidTbjlTRl%2Bj%2BKLPrtKGymVKzRgUhRjn0zYeQz8lAU3R%2BcZbKy1oRFb9Pq0siqHIQ3%2Bkg9SC3WXmVuDAgfMQdEK7UpOJ%2BtLNLb1Il7tMsWvWmW5Rk3LQeYgG2JdqY50U2pnLcq6yCTzK1M8mcnD3bGx%2FVe9jS5chKVEQByDxLNQjhldeQ2kpDlC2OiOy5yY0GqAPQa3rGE8mcGa8pSQb%2BGLNtb9Ph2fw8PxUUfh8oyTWyvW21nNQrExnzEBatCb%2BnG5cFG5JGC%2FjAG%2Fr5zZUUVrqUuB9sCl7VhVmQLbg3nuAqy%2BSJ6hVkvS0fLx%2BEn02OmDHc5d93ZNr2lj1hrZaU%2FdgnEGx77F2ZtfVxyvSyUwUi%2FSNKfgBO2lZlBmWUNJHV%2FYA64WJRwz6ryugcDa9iqtiuRFgLDswBMN%2Frkb0GOqUBW2HhRhLikNuuPRwyENwMhhgnHxlUDLISurFYrDfkvZev8EjSCiFsH8L%2F0wLxYWQj3%2BSqArc%2F8vPayB7frviJWQK%2B5DC4r2gfIjrbreaeq5agC9SUgEYCMX67hliEs7%2FNv6RAYtxKs0S30kEJ3SC5EgCtT4pT51nTefGLDNMup1YzQIZhxUwjzuq6rPBI4Ossft4DfCTAoYW8%2FXqiI2sVA67oTKGb&X-Amz-Signature=e72c488d4cf67fb542f4ffd268f515d0ee3db23e63ddb5d232cb33034d2319de&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
