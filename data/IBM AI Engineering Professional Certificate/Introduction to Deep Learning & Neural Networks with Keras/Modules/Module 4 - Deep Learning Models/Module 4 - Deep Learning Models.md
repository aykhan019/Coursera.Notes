

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD52VABG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClm7LaAjk5gXVYjGlFWC6yIUmGWhurbQ7qDYzxv18%2BOAiEA9VfZ9HcwlgZVnBGh%2FPBrr1Qw9MNZLl3oUrh2hsNRP0UqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuhXfyi3uSKX%2Fo%2FoSrcA%2FZntrqTglKU3jabgkR9ULmhPBAmIXurqJ254Za1YTQko4d5%2BWIPdMgaCRk3rvdhJ8%2BbeScfiqFeWi32R6Nc%2F%2FdOMlLWruEUGA%2FqQTFjQ9UZupgts9XLa5lBx32wR6AAHE0Ail8k9jvEusm%2FYGtHxP21WPiPQiomUdssPiMEV1fsyDP9VMILwa%2BtD1SPXcraELfxQcbuaKXCGjVYFJLHHjtw4DJLUd%2Fhk5O6KWhYtWHevcOYRWO%2BtCV7lwmVz8af8wOAprLGGNq4YvFcGAjYCYhBvJkzCc20zKKjaC20VLdjRsCGisoYB74UF2zgzKcdI8fx6sMGdMzUp9%2FlUbT0tPSC9VEL%2F2mwVV6uPstOyuQkGoCC7Fo4iipqDsNRvDybMaZ6u8iNmzieW9NMu5Jynsha37mO01ZIGWtH2e8B4y9%2B4L694EzfizuqCgGpE6gT1sgfIwrY6i%2BUf9C6EflHU5Auxrj4ZXorfjMdEsfekkOnI5SEJK2hTRLQP%2FmcptWa0P6KazEm3kdJd%2F23CQXOH7tT7foO7da9vZQ8f%2B%2FNN3cHEZwzBRM0g0HOhu5N4J74dwp7cV%2B%2Bk%2FKSc6RomJGEagGFLUb76MRciaOpoH6%2ByMGdRQayR1ty29LeTTgOMJj49LwGOqUBXiAAKJr9BXjDHffxx28FLhtcmb9G8nNPxlHN4IYOxja3OyZX5573%2FHDHbtX2DAJ8nthRWqJtCLcXfnGIh1CXjQZ1E9WjWCwH3ZgceC0opS4JvTvpbha3Ha6RCI4rn%2BZokBy7Wt2nz3ohX3y9kk0W5jzPH5frmKnkxw8le6AMQhOOtpd47wV38cR8KaSeyhcqSVwAUsn6unjvf4%2FlOjfmjjNTo%2BNR&X-Amz-Signature=242fe0f902c567367f4c09ca0ab82bab1b71a7524e879826ce9d168c7655aa3f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD52VABG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClm7LaAjk5gXVYjGlFWC6yIUmGWhurbQ7qDYzxv18%2BOAiEA9VfZ9HcwlgZVnBGh%2FPBrr1Qw9MNZLl3oUrh2hsNRP0UqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuhXfyi3uSKX%2Fo%2FoSrcA%2FZntrqTglKU3jabgkR9ULmhPBAmIXurqJ254Za1YTQko4d5%2BWIPdMgaCRk3rvdhJ8%2BbeScfiqFeWi32R6Nc%2F%2FdOMlLWruEUGA%2FqQTFjQ9UZupgts9XLa5lBx32wR6AAHE0Ail8k9jvEusm%2FYGtHxP21WPiPQiomUdssPiMEV1fsyDP9VMILwa%2BtD1SPXcraELfxQcbuaKXCGjVYFJLHHjtw4DJLUd%2Fhk5O6KWhYtWHevcOYRWO%2BtCV7lwmVz8af8wOAprLGGNq4YvFcGAjYCYhBvJkzCc20zKKjaC20VLdjRsCGisoYB74UF2zgzKcdI8fx6sMGdMzUp9%2FlUbT0tPSC9VEL%2F2mwVV6uPstOyuQkGoCC7Fo4iipqDsNRvDybMaZ6u8iNmzieW9NMu5Jynsha37mO01ZIGWtH2e8B4y9%2B4L694EzfizuqCgGpE6gT1sgfIwrY6i%2BUf9C6EflHU5Auxrj4ZXorfjMdEsfekkOnI5SEJK2hTRLQP%2FmcptWa0P6KazEm3kdJd%2F23CQXOH7tT7foO7da9vZQ8f%2B%2FNN3cHEZwzBRM0g0HOhu5N4J74dwp7cV%2B%2Bk%2FKSc6RomJGEagGFLUb76MRciaOpoH6%2ByMGdRQayR1ty29LeTTgOMJj49LwGOqUBXiAAKJr9BXjDHffxx28FLhtcmb9G8nNPxlHN4IYOxja3OyZX5573%2FHDHbtX2DAJ8nthRWqJtCLcXfnGIh1CXjQZ1E9WjWCwH3ZgceC0opS4JvTvpbha3Ha6RCI4rn%2BZokBy7Wt2nz3ohX3y9kk0W5jzPH5frmKnkxw8le6AMQhOOtpd47wV38cR8KaSeyhcqSVwAUsn6unjvf4%2FlOjfmjjNTo%2BNR&X-Amz-Signature=1095428fd721161dc6327bc03ed623c6aec750751d902f6e25c357fb974842ce&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD52VABG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClm7LaAjk5gXVYjGlFWC6yIUmGWhurbQ7qDYzxv18%2BOAiEA9VfZ9HcwlgZVnBGh%2FPBrr1Qw9MNZLl3oUrh2hsNRP0UqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuhXfyi3uSKX%2Fo%2FoSrcA%2FZntrqTglKU3jabgkR9ULmhPBAmIXurqJ254Za1YTQko4d5%2BWIPdMgaCRk3rvdhJ8%2BbeScfiqFeWi32R6Nc%2F%2FdOMlLWruEUGA%2FqQTFjQ9UZupgts9XLa5lBx32wR6AAHE0Ail8k9jvEusm%2FYGtHxP21WPiPQiomUdssPiMEV1fsyDP9VMILwa%2BtD1SPXcraELfxQcbuaKXCGjVYFJLHHjtw4DJLUd%2Fhk5O6KWhYtWHevcOYRWO%2BtCV7lwmVz8af8wOAprLGGNq4YvFcGAjYCYhBvJkzCc20zKKjaC20VLdjRsCGisoYB74UF2zgzKcdI8fx6sMGdMzUp9%2FlUbT0tPSC9VEL%2F2mwVV6uPstOyuQkGoCC7Fo4iipqDsNRvDybMaZ6u8iNmzieW9NMu5Jynsha37mO01ZIGWtH2e8B4y9%2B4L694EzfizuqCgGpE6gT1sgfIwrY6i%2BUf9C6EflHU5Auxrj4ZXorfjMdEsfekkOnI5SEJK2hTRLQP%2FmcptWa0P6KazEm3kdJd%2F23CQXOH7tT7foO7da9vZQ8f%2B%2FNN3cHEZwzBRM0g0HOhu5N4J74dwp7cV%2B%2Bk%2FKSc6RomJGEagGFLUb76MRciaOpoH6%2ByMGdRQayR1ty29LeTTgOMJj49LwGOqUBXiAAKJr9BXjDHffxx28FLhtcmb9G8nNPxlHN4IYOxja3OyZX5573%2FHDHbtX2DAJ8nthRWqJtCLcXfnGIh1CXjQZ1E9WjWCwH3ZgceC0opS4JvTvpbha3Ha6RCI4rn%2BZokBy7Wt2nz3ohX3y9kk0W5jzPH5frmKnkxw8le6AMQhOOtpd47wV38cR8KaSeyhcqSVwAUsn6unjvf4%2FlOjfmjjNTo%2BNR&X-Amz-Signature=e61c396b88aaf18fa96a28a37d5a4188526b57691027dcd4334a0cc39bcc9f37&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD52VABG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClm7LaAjk5gXVYjGlFWC6yIUmGWhurbQ7qDYzxv18%2BOAiEA9VfZ9HcwlgZVnBGh%2FPBrr1Qw9MNZLl3oUrh2hsNRP0UqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuhXfyi3uSKX%2Fo%2FoSrcA%2FZntrqTglKU3jabgkR9ULmhPBAmIXurqJ254Za1YTQko4d5%2BWIPdMgaCRk3rvdhJ8%2BbeScfiqFeWi32R6Nc%2F%2FdOMlLWruEUGA%2FqQTFjQ9UZupgts9XLa5lBx32wR6AAHE0Ail8k9jvEusm%2FYGtHxP21WPiPQiomUdssPiMEV1fsyDP9VMILwa%2BtD1SPXcraELfxQcbuaKXCGjVYFJLHHjtw4DJLUd%2Fhk5O6KWhYtWHevcOYRWO%2BtCV7lwmVz8af8wOAprLGGNq4YvFcGAjYCYhBvJkzCc20zKKjaC20VLdjRsCGisoYB74UF2zgzKcdI8fx6sMGdMzUp9%2FlUbT0tPSC9VEL%2F2mwVV6uPstOyuQkGoCC7Fo4iipqDsNRvDybMaZ6u8iNmzieW9NMu5Jynsha37mO01ZIGWtH2e8B4y9%2B4L694EzfizuqCgGpE6gT1sgfIwrY6i%2BUf9C6EflHU5Auxrj4ZXorfjMdEsfekkOnI5SEJK2hTRLQP%2FmcptWa0P6KazEm3kdJd%2F23CQXOH7tT7foO7da9vZQ8f%2B%2FNN3cHEZwzBRM0g0HOhu5N4J74dwp7cV%2B%2Bk%2FKSc6RomJGEagGFLUb76MRciaOpoH6%2ByMGdRQayR1ty29LeTTgOMJj49LwGOqUBXiAAKJr9BXjDHffxx28FLhtcmb9G8nNPxlHN4IYOxja3OyZX5573%2FHDHbtX2DAJ8nthRWqJtCLcXfnGIh1CXjQZ1E9WjWCwH3ZgceC0opS4JvTvpbha3Ha6RCI4rn%2BZokBy7Wt2nz3ohX3y9kk0W5jzPH5frmKnkxw8le6AMQhOOtpd47wV38cR8KaSeyhcqSVwAUsn6unjvf4%2FlOjfmjjNTo%2BNR&X-Amz-Signature=bf16709d19173ca61f8216af862f7ae5e9db16d5803a016ef7f370ec6d37125c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD52VABG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClm7LaAjk5gXVYjGlFWC6yIUmGWhurbQ7qDYzxv18%2BOAiEA9VfZ9HcwlgZVnBGh%2FPBrr1Qw9MNZLl3oUrh2hsNRP0UqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuhXfyi3uSKX%2Fo%2FoSrcA%2FZntrqTglKU3jabgkR9ULmhPBAmIXurqJ254Za1YTQko4d5%2BWIPdMgaCRk3rvdhJ8%2BbeScfiqFeWi32R6Nc%2F%2FdOMlLWruEUGA%2FqQTFjQ9UZupgts9XLa5lBx32wR6AAHE0Ail8k9jvEusm%2FYGtHxP21WPiPQiomUdssPiMEV1fsyDP9VMILwa%2BtD1SPXcraELfxQcbuaKXCGjVYFJLHHjtw4DJLUd%2Fhk5O6KWhYtWHevcOYRWO%2BtCV7lwmVz8af8wOAprLGGNq4YvFcGAjYCYhBvJkzCc20zKKjaC20VLdjRsCGisoYB74UF2zgzKcdI8fx6sMGdMzUp9%2FlUbT0tPSC9VEL%2F2mwVV6uPstOyuQkGoCC7Fo4iipqDsNRvDybMaZ6u8iNmzieW9NMu5Jynsha37mO01ZIGWtH2e8B4y9%2B4L694EzfizuqCgGpE6gT1sgfIwrY6i%2BUf9C6EflHU5Auxrj4ZXorfjMdEsfekkOnI5SEJK2hTRLQP%2FmcptWa0P6KazEm3kdJd%2F23CQXOH7tT7foO7da9vZQ8f%2B%2FNN3cHEZwzBRM0g0HOhu5N4J74dwp7cV%2B%2Bk%2FKSc6RomJGEagGFLUb76MRciaOpoH6%2ByMGdRQayR1ty29LeTTgOMJj49LwGOqUBXiAAKJr9BXjDHffxx28FLhtcmb9G8nNPxlHN4IYOxja3OyZX5573%2FHDHbtX2DAJ8nthRWqJtCLcXfnGIh1CXjQZ1E9WjWCwH3ZgceC0opS4JvTvpbha3Ha6RCI4rn%2BZokBy7Wt2nz3ohX3y9kk0W5jzPH5frmKnkxw8le6AMQhOOtpd47wV38cR8KaSeyhcqSVwAUsn6unjvf4%2FlOjfmjjNTo%2BNR&X-Amz-Signature=d385449dea9653246728868cc5ef464879e67251a3939da2e3e3206c0ab70805&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD52VABG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClm7LaAjk5gXVYjGlFWC6yIUmGWhurbQ7qDYzxv18%2BOAiEA9VfZ9HcwlgZVnBGh%2FPBrr1Qw9MNZLl3oUrh2hsNRP0UqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuhXfyi3uSKX%2Fo%2FoSrcA%2FZntrqTglKU3jabgkR9ULmhPBAmIXurqJ254Za1YTQko4d5%2BWIPdMgaCRk3rvdhJ8%2BbeScfiqFeWi32R6Nc%2F%2FdOMlLWruEUGA%2FqQTFjQ9UZupgts9XLa5lBx32wR6AAHE0Ail8k9jvEusm%2FYGtHxP21WPiPQiomUdssPiMEV1fsyDP9VMILwa%2BtD1SPXcraELfxQcbuaKXCGjVYFJLHHjtw4DJLUd%2Fhk5O6KWhYtWHevcOYRWO%2BtCV7lwmVz8af8wOAprLGGNq4YvFcGAjYCYhBvJkzCc20zKKjaC20VLdjRsCGisoYB74UF2zgzKcdI8fx6sMGdMzUp9%2FlUbT0tPSC9VEL%2F2mwVV6uPstOyuQkGoCC7Fo4iipqDsNRvDybMaZ6u8iNmzieW9NMu5Jynsha37mO01ZIGWtH2e8B4y9%2B4L694EzfizuqCgGpE6gT1sgfIwrY6i%2BUf9C6EflHU5Auxrj4ZXorfjMdEsfekkOnI5SEJK2hTRLQP%2FmcptWa0P6KazEm3kdJd%2F23CQXOH7tT7foO7da9vZQ8f%2B%2FNN3cHEZwzBRM0g0HOhu5N4J74dwp7cV%2B%2Bk%2FKSc6RomJGEagGFLUb76MRciaOpoH6%2ByMGdRQayR1ty29LeTTgOMJj49LwGOqUBXiAAKJr9BXjDHffxx28FLhtcmb9G8nNPxlHN4IYOxja3OyZX5573%2FHDHbtX2DAJ8nthRWqJtCLcXfnGIh1CXjQZ1E9WjWCwH3ZgceC0opS4JvTvpbha3Ha6RCI4rn%2BZokBy7Wt2nz3ohX3y9kk0W5jzPH5frmKnkxw8le6AMQhOOtpd47wV38cR8KaSeyhcqSVwAUsn6unjvf4%2FlOjfmjjNTo%2BNR&X-Amz-Signature=9e2c0e4c182b7c077ac9a77e1eb7fed90678549fec4b580849f5d2fb19906a50&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD52VABG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClm7LaAjk5gXVYjGlFWC6yIUmGWhurbQ7qDYzxv18%2BOAiEA9VfZ9HcwlgZVnBGh%2FPBrr1Qw9MNZLl3oUrh2hsNRP0UqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuhXfyi3uSKX%2Fo%2FoSrcA%2FZntrqTglKU3jabgkR9ULmhPBAmIXurqJ254Za1YTQko4d5%2BWIPdMgaCRk3rvdhJ8%2BbeScfiqFeWi32R6Nc%2F%2FdOMlLWruEUGA%2FqQTFjQ9UZupgts9XLa5lBx32wR6AAHE0Ail8k9jvEusm%2FYGtHxP21WPiPQiomUdssPiMEV1fsyDP9VMILwa%2BtD1SPXcraELfxQcbuaKXCGjVYFJLHHjtw4DJLUd%2Fhk5O6KWhYtWHevcOYRWO%2BtCV7lwmVz8af8wOAprLGGNq4YvFcGAjYCYhBvJkzCc20zKKjaC20VLdjRsCGisoYB74UF2zgzKcdI8fx6sMGdMzUp9%2FlUbT0tPSC9VEL%2F2mwVV6uPstOyuQkGoCC7Fo4iipqDsNRvDybMaZ6u8iNmzieW9NMu5Jynsha37mO01ZIGWtH2e8B4y9%2B4L694EzfizuqCgGpE6gT1sgfIwrY6i%2BUf9C6EflHU5Auxrj4ZXorfjMdEsfekkOnI5SEJK2hTRLQP%2FmcptWa0P6KazEm3kdJd%2F23CQXOH7tT7foO7da9vZQ8f%2B%2FNN3cHEZwzBRM0g0HOhu5N4J74dwp7cV%2B%2Bk%2FKSc6RomJGEagGFLUb76MRciaOpoH6%2ByMGdRQayR1ty29LeTTgOMJj49LwGOqUBXiAAKJr9BXjDHffxx28FLhtcmb9G8nNPxlHN4IYOxja3OyZX5573%2FHDHbtX2DAJ8nthRWqJtCLcXfnGIh1CXjQZ1E9WjWCwH3ZgceC0opS4JvTvpbha3Ha6RCI4rn%2BZokBy7Wt2nz3ohX3y9kk0W5jzPH5frmKnkxw8le6AMQhOOtpd47wV38cR8KaSeyhcqSVwAUsn6unjvf4%2FlOjfmjjNTo%2BNR&X-Amz-Signature=3e294062119c7965c5e1bf5c7a6a9339b5918f12f0e60f72f4eed6b59118c5c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD52VABG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClm7LaAjk5gXVYjGlFWC6yIUmGWhurbQ7qDYzxv18%2BOAiEA9VfZ9HcwlgZVnBGh%2FPBrr1Qw9MNZLl3oUrh2hsNRP0UqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuhXfyi3uSKX%2Fo%2FoSrcA%2FZntrqTglKU3jabgkR9ULmhPBAmIXurqJ254Za1YTQko4d5%2BWIPdMgaCRk3rvdhJ8%2BbeScfiqFeWi32R6Nc%2F%2FdOMlLWruEUGA%2FqQTFjQ9UZupgts9XLa5lBx32wR6AAHE0Ail8k9jvEusm%2FYGtHxP21WPiPQiomUdssPiMEV1fsyDP9VMILwa%2BtD1SPXcraELfxQcbuaKXCGjVYFJLHHjtw4DJLUd%2Fhk5O6KWhYtWHevcOYRWO%2BtCV7lwmVz8af8wOAprLGGNq4YvFcGAjYCYhBvJkzCc20zKKjaC20VLdjRsCGisoYB74UF2zgzKcdI8fx6sMGdMzUp9%2FlUbT0tPSC9VEL%2F2mwVV6uPstOyuQkGoCC7Fo4iipqDsNRvDybMaZ6u8iNmzieW9NMu5Jynsha37mO01ZIGWtH2e8B4y9%2B4L694EzfizuqCgGpE6gT1sgfIwrY6i%2BUf9C6EflHU5Auxrj4ZXorfjMdEsfekkOnI5SEJK2hTRLQP%2FmcptWa0P6KazEm3kdJd%2F23CQXOH7tT7foO7da9vZQ8f%2B%2FNN3cHEZwzBRM0g0HOhu5N4J74dwp7cV%2B%2Bk%2FKSc6RomJGEagGFLUb76MRciaOpoH6%2ByMGdRQayR1ty29LeTTgOMJj49LwGOqUBXiAAKJr9BXjDHffxx28FLhtcmb9G8nNPxlHN4IYOxja3OyZX5573%2FHDHbtX2DAJ8nthRWqJtCLcXfnGIh1CXjQZ1E9WjWCwH3ZgceC0opS4JvTvpbha3Ha6RCI4rn%2BZokBy7Wt2nz3ohX3y9kk0W5jzPH5frmKnkxw8le6AMQhOOtpd47wV38cR8KaSeyhcqSVwAUsn6unjvf4%2FlOjfmjjNTo%2BNR&X-Amz-Signature=9c3554683751951336359c8f4068a97b440a4b79d0061d60877af5619531289a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD52VABG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClm7LaAjk5gXVYjGlFWC6yIUmGWhurbQ7qDYzxv18%2BOAiEA9VfZ9HcwlgZVnBGh%2FPBrr1Qw9MNZLl3oUrh2hsNRP0UqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuhXfyi3uSKX%2Fo%2FoSrcA%2FZntrqTglKU3jabgkR9ULmhPBAmIXurqJ254Za1YTQko4d5%2BWIPdMgaCRk3rvdhJ8%2BbeScfiqFeWi32R6Nc%2F%2FdOMlLWruEUGA%2FqQTFjQ9UZupgts9XLa5lBx32wR6AAHE0Ail8k9jvEusm%2FYGtHxP21WPiPQiomUdssPiMEV1fsyDP9VMILwa%2BtD1SPXcraELfxQcbuaKXCGjVYFJLHHjtw4DJLUd%2Fhk5O6KWhYtWHevcOYRWO%2BtCV7lwmVz8af8wOAprLGGNq4YvFcGAjYCYhBvJkzCc20zKKjaC20VLdjRsCGisoYB74UF2zgzKcdI8fx6sMGdMzUp9%2FlUbT0tPSC9VEL%2F2mwVV6uPstOyuQkGoCC7Fo4iipqDsNRvDybMaZ6u8iNmzieW9NMu5Jynsha37mO01ZIGWtH2e8B4y9%2B4L694EzfizuqCgGpE6gT1sgfIwrY6i%2BUf9C6EflHU5Auxrj4ZXorfjMdEsfekkOnI5SEJK2hTRLQP%2FmcptWa0P6KazEm3kdJd%2F23CQXOH7tT7foO7da9vZQ8f%2B%2FNN3cHEZwzBRM0g0HOhu5N4J74dwp7cV%2B%2Bk%2FKSc6RomJGEagGFLUb76MRciaOpoH6%2ByMGdRQayR1ty29LeTTgOMJj49LwGOqUBXiAAKJr9BXjDHffxx28FLhtcmb9G8nNPxlHN4IYOxja3OyZX5573%2FHDHbtX2DAJ8nthRWqJtCLcXfnGIh1CXjQZ1E9WjWCwH3ZgceC0opS4JvTvpbha3Ha6RCI4rn%2BZokBy7Wt2nz3ohX3y9kk0W5jzPH5frmKnkxw8le6AMQhOOtpd47wV38cR8KaSeyhcqSVwAUsn6unjvf4%2FlOjfmjjNTo%2BNR&X-Amz-Signature=899473a908b5aad82b513771c09516199627453d0b50a1fd4653cb58acf35a72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SDCLZ3G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2FRghPRh0AoFgNtLMnyMZbAoNCdNPsdk0wuCbPvaHOQAiAn0NU9%2FlNyNqDC8QX8vb7JbnPBnpjjSA8o8LKwo5om1yqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1GjsIlI2ZS3aivc6KtwDzBqRtKX5bxQXVl9lG7KkFZFLvpgDvVwA4xiVhS7n6rfn%2FFq%2BbdkqnIva22JwXthxtCg6zCjNMmM0ksG8%2F5xj9V3VYesn4KO4FSmU69eRgMPRfSmcQJ1POc0Xg4AZiL6MOYkwQyWyzg6MPW8fkfxoN5IZktF0I%2BYcNVrdm7nh1JDFrBFFaQx8lzMtcbv664je7gNgzhIcSH%2FWWi3bSyuxpMb%2Bp3dLIZ5CR%2Blx5KxVlUmjqObmgVl8LT0c9OTl8poKsAvlGvn4F41SdJLv%2B76GZ8ox7Gih5rTYpnpJjWsRhOUtsUY7%2B9ps7Il2Xy4Yq3%2FzQ3xTJCZYLXVFsEiqF15jvexTt0%2BG%2BRIkaLxMR%2FykiCKK1hstv0hBsVhKnH%2FEW%2FRI0xrs7rW0984G7rmenvfmPEAylPIqI39u1PG5OSkc7lfClQTiy9hjtpFxWKGhgjPFshpOjJ3K%2FRnT%2FADImv5t05JfPMCxMES5Gut1ONJHBu0j%2FQSEly5ajWZQvXMgKO%2BemqY7OV0hTYF8BWCWwDV%2F%2FJ3Kxi8I%2Bx2yv1xGXjFpXVUkiGoAUAmkggRrmcYHi4omatR4TNpFThpbA7OSj53ZPEl5Rl3ibFiXkaHdwgXb%2FR6HY0BhEg8p5mAFo24wktv0vAY6pgFYn1q2ImYdz9JezsF2d28ndS8xL0am%2Bt97ffER0kCItWjCZca7dRycxhRd4LsB8HGbS%2BVY29u1J%2B7lJ%2FRemAZKyA1urkcvW5jex5jqr7S1vSRqggYydF%2BgSZu9TLYBsVrHtCfkCAQ0on8z%2BVUeCTmeIlQ0mJqGuUZUrXOigc038jzsdWvNfuWdlK4fUlJ66qjWsos9zeyESWkyjV0Jo30K6MroI6Uk&X-Amz-Signature=e309de903039e60abfdeea2c9a9a821951089b0013d73c66b7c8e867ebba2799&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SDCLZ3G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2FRghPRh0AoFgNtLMnyMZbAoNCdNPsdk0wuCbPvaHOQAiAn0NU9%2FlNyNqDC8QX8vb7JbnPBnpjjSA8o8LKwo5om1yqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1GjsIlI2ZS3aivc6KtwDzBqRtKX5bxQXVl9lG7KkFZFLvpgDvVwA4xiVhS7n6rfn%2FFq%2BbdkqnIva22JwXthxtCg6zCjNMmM0ksG8%2F5xj9V3VYesn4KO4FSmU69eRgMPRfSmcQJ1POc0Xg4AZiL6MOYkwQyWyzg6MPW8fkfxoN5IZktF0I%2BYcNVrdm7nh1JDFrBFFaQx8lzMtcbv664je7gNgzhIcSH%2FWWi3bSyuxpMb%2Bp3dLIZ5CR%2Blx5KxVlUmjqObmgVl8LT0c9OTl8poKsAvlGvn4F41SdJLv%2B76GZ8ox7Gih5rTYpnpJjWsRhOUtsUY7%2B9ps7Il2Xy4Yq3%2FzQ3xTJCZYLXVFsEiqF15jvexTt0%2BG%2BRIkaLxMR%2FykiCKK1hstv0hBsVhKnH%2FEW%2FRI0xrs7rW0984G7rmenvfmPEAylPIqI39u1PG5OSkc7lfClQTiy9hjtpFxWKGhgjPFshpOjJ3K%2FRnT%2FADImv5t05JfPMCxMES5Gut1ONJHBu0j%2FQSEly5ajWZQvXMgKO%2BemqY7OV0hTYF8BWCWwDV%2F%2FJ3Kxi8I%2Bx2yv1xGXjFpXVUkiGoAUAmkggRrmcYHi4omatR4TNpFThpbA7OSj53ZPEl5Rl3ibFiXkaHdwgXb%2FR6HY0BhEg8p5mAFo24wktv0vAY6pgFYn1q2ImYdz9JezsF2d28ndS8xL0am%2Bt97ffER0kCItWjCZca7dRycxhRd4LsB8HGbS%2BVY29u1J%2B7lJ%2FRemAZKyA1urkcvW5jex5jqr7S1vSRqggYydF%2BgSZu9TLYBsVrHtCfkCAQ0on8z%2BVUeCTmeIlQ0mJqGuUZUrXOigc038jzsdWvNfuWdlK4fUlJ66qjWsos9zeyESWkyjV0Jo30K6MroI6Uk&X-Amz-Signature=ab211b6f5c3f87fbff9b445ea2a3bd3655e3738aa61dc03044d94f3a20384281&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
