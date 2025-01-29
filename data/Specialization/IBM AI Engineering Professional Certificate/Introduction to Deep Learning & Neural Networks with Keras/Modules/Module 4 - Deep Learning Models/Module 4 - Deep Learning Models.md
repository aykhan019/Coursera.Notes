

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466627RGIBS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkIQSna4vX%2BXCwwCiPobT3exkVCgFiUNcg4CBGLYf2NQIhAPvaD5yXMrs6ninNrxk5N5cU2C0sYOv6UwcLnb3ly7R6KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ%2BY1T%2FuEolizuQpsq3AN33STrd4I7kUCia3g%2BQwxBr86ksMRL97uRnk%2By1zvt9z0dg%2F2e%2FTSzClhqnS7v400fX%2BqBeY36paS7Rq5KCXghjMYQ%2B%2FT7PL9e0lpd8z19QsMgP22sdNI3DBybhRlINO9pBtlzxCn9xNjh63BgBUGjXlbAUhcuC0fKWfpv0mw3SmzkWVoSJphd95E%2FoSJ6OXRvfYHxz7ODH5p6X8AdthMD%2BitjE7Gn%2FkVdmT5I3%2B9IesnsGdKB%2B3ATxF0KWjtHI2A49%2BOdPz6yWqplw13ruAau0SOZp07DcE0xf5547BiuHI7eW4GGy9VqmA1bTF84yJs8qmy0i9KWpFjH3cfiyU01kTOcs0YQ1SQFifRCNUu%2B91c7J9ptmoispHB2Ig6%2FHIDl7YuPmArD6JE7%2Fb4HOWJ85amjc1gTJiDrRP7VscVTBAOwyHXyhV4U68Zg8vmANWhAmvsLZGUfY6IPmW69AOEbLC2FQWjMsk%2B7DBbBi9pVCYJZ4z0fK5obC6xUUTvxpqTYrAOtxUs9dmMx4vO0YzPckU1LGM8W4wJCPFmeeauUGl8Bxhyi79g%2BsBmXlJKlOLGgB%2FAGXpKJKVDjyQejn0TY9CbfhBwdqANm26RIRxrv9%2BWoyhlUd6HS29TWQzDE%2F%2Be8BjqkAU871JvysENOTrRiBg%2B4jRwbmUiCYoikAPQ9v9aQhe44djm6IPbdDnvYjknid4%2FkCPBncZ069tC2YiahizPHZb98XCww3gFA4U2JFghoIWfmH8UT7X5MycNAtdA9r0y9HtZQkQWYBoT7q0SSIflNNA2OZjoxEaeogZwkd5zu%2FS3Re2nTGcYA5GJTx3D9D49PnmoZXWVKLPVZg%2BJstLRuLauYrpdJ&X-Amz-Signature=db3aff1023e4ecef8a3247970965fb9ea4d01e6017707a6eca2a0a9feb9423c6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466627RGIBS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkIQSna4vX%2BXCwwCiPobT3exkVCgFiUNcg4CBGLYf2NQIhAPvaD5yXMrs6ninNrxk5N5cU2C0sYOv6UwcLnb3ly7R6KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ%2BY1T%2FuEolizuQpsq3AN33STrd4I7kUCia3g%2BQwxBr86ksMRL97uRnk%2By1zvt9z0dg%2F2e%2FTSzClhqnS7v400fX%2BqBeY36paS7Rq5KCXghjMYQ%2B%2FT7PL9e0lpd8z19QsMgP22sdNI3DBybhRlINO9pBtlzxCn9xNjh63BgBUGjXlbAUhcuC0fKWfpv0mw3SmzkWVoSJphd95E%2FoSJ6OXRvfYHxz7ODH5p6X8AdthMD%2BitjE7Gn%2FkVdmT5I3%2B9IesnsGdKB%2B3ATxF0KWjtHI2A49%2BOdPz6yWqplw13ruAau0SOZp07DcE0xf5547BiuHI7eW4GGy9VqmA1bTF84yJs8qmy0i9KWpFjH3cfiyU01kTOcs0YQ1SQFifRCNUu%2B91c7J9ptmoispHB2Ig6%2FHIDl7YuPmArD6JE7%2Fb4HOWJ85amjc1gTJiDrRP7VscVTBAOwyHXyhV4U68Zg8vmANWhAmvsLZGUfY6IPmW69AOEbLC2FQWjMsk%2B7DBbBi9pVCYJZ4z0fK5obC6xUUTvxpqTYrAOtxUs9dmMx4vO0YzPckU1LGM8W4wJCPFmeeauUGl8Bxhyi79g%2BsBmXlJKlOLGgB%2FAGXpKJKVDjyQejn0TY9CbfhBwdqANm26RIRxrv9%2BWoyhlUd6HS29TWQzDE%2F%2Be8BjqkAU871JvysENOTrRiBg%2B4jRwbmUiCYoikAPQ9v9aQhe44djm6IPbdDnvYjknid4%2FkCPBncZ069tC2YiahizPHZb98XCww3gFA4U2JFghoIWfmH8UT7X5MycNAtdA9r0y9HtZQkQWYBoT7q0SSIflNNA2OZjoxEaeogZwkd5zu%2FS3Re2nTGcYA5GJTx3D9D49PnmoZXWVKLPVZg%2BJstLRuLauYrpdJ&X-Amz-Signature=1648b8d84036358caf6a5e2b40d91a579c07cb2971601c3a9134cfdddd3a1594&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466627RGIBS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkIQSna4vX%2BXCwwCiPobT3exkVCgFiUNcg4CBGLYf2NQIhAPvaD5yXMrs6ninNrxk5N5cU2C0sYOv6UwcLnb3ly7R6KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ%2BY1T%2FuEolizuQpsq3AN33STrd4I7kUCia3g%2BQwxBr86ksMRL97uRnk%2By1zvt9z0dg%2F2e%2FTSzClhqnS7v400fX%2BqBeY36paS7Rq5KCXghjMYQ%2B%2FT7PL9e0lpd8z19QsMgP22sdNI3DBybhRlINO9pBtlzxCn9xNjh63BgBUGjXlbAUhcuC0fKWfpv0mw3SmzkWVoSJphd95E%2FoSJ6OXRvfYHxz7ODH5p6X8AdthMD%2BitjE7Gn%2FkVdmT5I3%2B9IesnsGdKB%2B3ATxF0KWjtHI2A49%2BOdPz6yWqplw13ruAau0SOZp07DcE0xf5547BiuHI7eW4GGy9VqmA1bTF84yJs8qmy0i9KWpFjH3cfiyU01kTOcs0YQ1SQFifRCNUu%2B91c7J9ptmoispHB2Ig6%2FHIDl7YuPmArD6JE7%2Fb4HOWJ85amjc1gTJiDrRP7VscVTBAOwyHXyhV4U68Zg8vmANWhAmvsLZGUfY6IPmW69AOEbLC2FQWjMsk%2B7DBbBi9pVCYJZ4z0fK5obC6xUUTvxpqTYrAOtxUs9dmMx4vO0YzPckU1LGM8W4wJCPFmeeauUGl8Bxhyi79g%2BsBmXlJKlOLGgB%2FAGXpKJKVDjyQejn0TY9CbfhBwdqANm26RIRxrv9%2BWoyhlUd6HS29TWQzDE%2F%2Be8BjqkAU871JvysENOTrRiBg%2B4jRwbmUiCYoikAPQ9v9aQhe44djm6IPbdDnvYjknid4%2FkCPBncZ069tC2YiahizPHZb98XCww3gFA4U2JFghoIWfmH8UT7X5MycNAtdA9r0y9HtZQkQWYBoT7q0SSIflNNA2OZjoxEaeogZwkd5zu%2FS3Re2nTGcYA5GJTx3D9D49PnmoZXWVKLPVZg%2BJstLRuLauYrpdJ&X-Amz-Signature=6d3180e5b25106a4002e07791ea5ddf87acb6e9de4314ca18db09fc96b623548&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466627RGIBS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkIQSna4vX%2BXCwwCiPobT3exkVCgFiUNcg4CBGLYf2NQIhAPvaD5yXMrs6ninNrxk5N5cU2C0sYOv6UwcLnb3ly7R6KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ%2BY1T%2FuEolizuQpsq3AN33STrd4I7kUCia3g%2BQwxBr86ksMRL97uRnk%2By1zvt9z0dg%2F2e%2FTSzClhqnS7v400fX%2BqBeY36paS7Rq5KCXghjMYQ%2B%2FT7PL9e0lpd8z19QsMgP22sdNI3DBybhRlINO9pBtlzxCn9xNjh63BgBUGjXlbAUhcuC0fKWfpv0mw3SmzkWVoSJphd95E%2FoSJ6OXRvfYHxz7ODH5p6X8AdthMD%2BitjE7Gn%2FkVdmT5I3%2B9IesnsGdKB%2B3ATxF0KWjtHI2A49%2BOdPz6yWqplw13ruAau0SOZp07DcE0xf5547BiuHI7eW4GGy9VqmA1bTF84yJs8qmy0i9KWpFjH3cfiyU01kTOcs0YQ1SQFifRCNUu%2B91c7J9ptmoispHB2Ig6%2FHIDl7YuPmArD6JE7%2Fb4HOWJ85amjc1gTJiDrRP7VscVTBAOwyHXyhV4U68Zg8vmANWhAmvsLZGUfY6IPmW69AOEbLC2FQWjMsk%2B7DBbBi9pVCYJZ4z0fK5obC6xUUTvxpqTYrAOtxUs9dmMx4vO0YzPckU1LGM8W4wJCPFmeeauUGl8Bxhyi79g%2BsBmXlJKlOLGgB%2FAGXpKJKVDjyQejn0TY9CbfhBwdqANm26RIRxrv9%2BWoyhlUd6HS29TWQzDE%2F%2Be8BjqkAU871JvysENOTrRiBg%2B4jRwbmUiCYoikAPQ9v9aQhe44djm6IPbdDnvYjknid4%2FkCPBncZ069tC2YiahizPHZb98XCww3gFA4U2JFghoIWfmH8UT7X5MycNAtdA9r0y9HtZQkQWYBoT7q0SSIflNNA2OZjoxEaeogZwkd5zu%2FS3Re2nTGcYA5GJTx3D9D49PnmoZXWVKLPVZg%2BJstLRuLauYrpdJ&X-Amz-Signature=9b9fd1dad1312c3454df85533f54e5f7ee7df084447227ba9003b34b97a0356c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466627RGIBS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkIQSna4vX%2BXCwwCiPobT3exkVCgFiUNcg4CBGLYf2NQIhAPvaD5yXMrs6ninNrxk5N5cU2C0sYOv6UwcLnb3ly7R6KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ%2BY1T%2FuEolizuQpsq3AN33STrd4I7kUCia3g%2BQwxBr86ksMRL97uRnk%2By1zvt9z0dg%2F2e%2FTSzClhqnS7v400fX%2BqBeY36paS7Rq5KCXghjMYQ%2B%2FT7PL9e0lpd8z19QsMgP22sdNI3DBybhRlINO9pBtlzxCn9xNjh63BgBUGjXlbAUhcuC0fKWfpv0mw3SmzkWVoSJphd95E%2FoSJ6OXRvfYHxz7ODH5p6X8AdthMD%2BitjE7Gn%2FkVdmT5I3%2B9IesnsGdKB%2B3ATxF0KWjtHI2A49%2BOdPz6yWqplw13ruAau0SOZp07DcE0xf5547BiuHI7eW4GGy9VqmA1bTF84yJs8qmy0i9KWpFjH3cfiyU01kTOcs0YQ1SQFifRCNUu%2B91c7J9ptmoispHB2Ig6%2FHIDl7YuPmArD6JE7%2Fb4HOWJ85amjc1gTJiDrRP7VscVTBAOwyHXyhV4U68Zg8vmANWhAmvsLZGUfY6IPmW69AOEbLC2FQWjMsk%2B7DBbBi9pVCYJZ4z0fK5obC6xUUTvxpqTYrAOtxUs9dmMx4vO0YzPckU1LGM8W4wJCPFmeeauUGl8Bxhyi79g%2BsBmXlJKlOLGgB%2FAGXpKJKVDjyQejn0TY9CbfhBwdqANm26RIRxrv9%2BWoyhlUd6HS29TWQzDE%2F%2Be8BjqkAU871JvysENOTrRiBg%2B4jRwbmUiCYoikAPQ9v9aQhe44djm6IPbdDnvYjknid4%2FkCPBncZ069tC2YiahizPHZb98XCww3gFA4U2JFghoIWfmH8UT7X5MycNAtdA9r0y9HtZQkQWYBoT7q0SSIflNNA2OZjoxEaeogZwkd5zu%2FS3Re2nTGcYA5GJTx3D9D49PnmoZXWVKLPVZg%2BJstLRuLauYrpdJ&X-Amz-Signature=db34a1c95b0bdb9832e8b402cb9f46082434abf362c5f58ca94d6b22a1e087ed&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466627RGIBS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkIQSna4vX%2BXCwwCiPobT3exkVCgFiUNcg4CBGLYf2NQIhAPvaD5yXMrs6ninNrxk5N5cU2C0sYOv6UwcLnb3ly7R6KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ%2BY1T%2FuEolizuQpsq3AN33STrd4I7kUCia3g%2BQwxBr86ksMRL97uRnk%2By1zvt9z0dg%2F2e%2FTSzClhqnS7v400fX%2BqBeY36paS7Rq5KCXghjMYQ%2B%2FT7PL9e0lpd8z19QsMgP22sdNI3DBybhRlINO9pBtlzxCn9xNjh63BgBUGjXlbAUhcuC0fKWfpv0mw3SmzkWVoSJphd95E%2FoSJ6OXRvfYHxz7ODH5p6X8AdthMD%2BitjE7Gn%2FkVdmT5I3%2B9IesnsGdKB%2B3ATxF0KWjtHI2A49%2BOdPz6yWqplw13ruAau0SOZp07DcE0xf5547BiuHI7eW4GGy9VqmA1bTF84yJs8qmy0i9KWpFjH3cfiyU01kTOcs0YQ1SQFifRCNUu%2B91c7J9ptmoispHB2Ig6%2FHIDl7YuPmArD6JE7%2Fb4HOWJ85amjc1gTJiDrRP7VscVTBAOwyHXyhV4U68Zg8vmANWhAmvsLZGUfY6IPmW69AOEbLC2FQWjMsk%2B7DBbBi9pVCYJZ4z0fK5obC6xUUTvxpqTYrAOtxUs9dmMx4vO0YzPckU1LGM8W4wJCPFmeeauUGl8Bxhyi79g%2BsBmXlJKlOLGgB%2FAGXpKJKVDjyQejn0TY9CbfhBwdqANm26RIRxrv9%2BWoyhlUd6HS29TWQzDE%2F%2Be8BjqkAU871JvysENOTrRiBg%2B4jRwbmUiCYoikAPQ9v9aQhe44djm6IPbdDnvYjknid4%2FkCPBncZ069tC2YiahizPHZb98XCww3gFA4U2JFghoIWfmH8UT7X5MycNAtdA9r0y9HtZQkQWYBoT7q0SSIflNNA2OZjoxEaeogZwkd5zu%2FS3Re2nTGcYA5GJTx3D9D49PnmoZXWVKLPVZg%2BJstLRuLauYrpdJ&X-Amz-Signature=fce11b70f698f5ae6e2534c0ed02082d1f9e149273687b7582b2238526b52f21&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466627RGIBS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkIQSna4vX%2BXCwwCiPobT3exkVCgFiUNcg4CBGLYf2NQIhAPvaD5yXMrs6ninNrxk5N5cU2C0sYOv6UwcLnb3ly7R6KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ%2BY1T%2FuEolizuQpsq3AN33STrd4I7kUCia3g%2BQwxBr86ksMRL97uRnk%2By1zvt9z0dg%2F2e%2FTSzClhqnS7v400fX%2BqBeY36paS7Rq5KCXghjMYQ%2B%2FT7PL9e0lpd8z19QsMgP22sdNI3DBybhRlINO9pBtlzxCn9xNjh63BgBUGjXlbAUhcuC0fKWfpv0mw3SmzkWVoSJphd95E%2FoSJ6OXRvfYHxz7ODH5p6X8AdthMD%2BitjE7Gn%2FkVdmT5I3%2B9IesnsGdKB%2B3ATxF0KWjtHI2A49%2BOdPz6yWqplw13ruAau0SOZp07DcE0xf5547BiuHI7eW4GGy9VqmA1bTF84yJs8qmy0i9KWpFjH3cfiyU01kTOcs0YQ1SQFifRCNUu%2B91c7J9ptmoispHB2Ig6%2FHIDl7YuPmArD6JE7%2Fb4HOWJ85amjc1gTJiDrRP7VscVTBAOwyHXyhV4U68Zg8vmANWhAmvsLZGUfY6IPmW69AOEbLC2FQWjMsk%2B7DBbBi9pVCYJZ4z0fK5obC6xUUTvxpqTYrAOtxUs9dmMx4vO0YzPckU1LGM8W4wJCPFmeeauUGl8Bxhyi79g%2BsBmXlJKlOLGgB%2FAGXpKJKVDjyQejn0TY9CbfhBwdqANm26RIRxrv9%2BWoyhlUd6HS29TWQzDE%2F%2Be8BjqkAU871JvysENOTrRiBg%2B4jRwbmUiCYoikAPQ9v9aQhe44djm6IPbdDnvYjknid4%2FkCPBncZ069tC2YiahizPHZb98XCww3gFA4U2JFghoIWfmH8UT7X5MycNAtdA9r0y9HtZQkQWYBoT7q0SSIflNNA2OZjoxEaeogZwkd5zu%2FS3Re2nTGcYA5GJTx3D9D49PnmoZXWVKLPVZg%2BJstLRuLauYrpdJ&X-Amz-Signature=66dd4a54ffa224cb5137bf82652d1258eb5087e939557ab93cdd0ea91029ef63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466627RGIBS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkIQSna4vX%2BXCwwCiPobT3exkVCgFiUNcg4CBGLYf2NQIhAPvaD5yXMrs6ninNrxk5N5cU2C0sYOv6UwcLnb3ly7R6KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ%2BY1T%2FuEolizuQpsq3AN33STrd4I7kUCia3g%2BQwxBr86ksMRL97uRnk%2By1zvt9z0dg%2F2e%2FTSzClhqnS7v400fX%2BqBeY36paS7Rq5KCXghjMYQ%2B%2FT7PL9e0lpd8z19QsMgP22sdNI3DBybhRlINO9pBtlzxCn9xNjh63BgBUGjXlbAUhcuC0fKWfpv0mw3SmzkWVoSJphd95E%2FoSJ6OXRvfYHxz7ODH5p6X8AdthMD%2BitjE7Gn%2FkVdmT5I3%2B9IesnsGdKB%2B3ATxF0KWjtHI2A49%2BOdPz6yWqplw13ruAau0SOZp07DcE0xf5547BiuHI7eW4GGy9VqmA1bTF84yJs8qmy0i9KWpFjH3cfiyU01kTOcs0YQ1SQFifRCNUu%2B91c7J9ptmoispHB2Ig6%2FHIDl7YuPmArD6JE7%2Fb4HOWJ85amjc1gTJiDrRP7VscVTBAOwyHXyhV4U68Zg8vmANWhAmvsLZGUfY6IPmW69AOEbLC2FQWjMsk%2B7DBbBi9pVCYJZ4z0fK5obC6xUUTvxpqTYrAOtxUs9dmMx4vO0YzPckU1LGM8W4wJCPFmeeauUGl8Bxhyi79g%2BsBmXlJKlOLGgB%2FAGXpKJKVDjyQejn0TY9CbfhBwdqANm26RIRxrv9%2BWoyhlUd6HS29TWQzDE%2F%2Be8BjqkAU871JvysENOTrRiBg%2B4jRwbmUiCYoikAPQ9v9aQhe44djm6IPbdDnvYjknid4%2FkCPBncZ069tC2YiahizPHZb98XCww3gFA4U2JFghoIWfmH8UT7X5MycNAtdA9r0y9HtZQkQWYBoT7q0SSIflNNA2OZjoxEaeogZwkd5zu%2FS3Re2nTGcYA5GJTx3D9D49PnmoZXWVKLPVZg%2BJstLRuLauYrpdJ&X-Amz-Signature=5849c944b0a4d98d50e8baaecae93073a9ae66911cd182643ad8feddaa58acfe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466627RGIBS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkIQSna4vX%2BXCwwCiPobT3exkVCgFiUNcg4CBGLYf2NQIhAPvaD5yXMrs6ninNrxk5N5cU2C0sYOv6UwcLnb3ly7R6KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ%2BY1T%2FuEolizuQpsq3AN33STrd4I7kUCia3g%2BQwxBr86ksMRL97uRnk%2By1zvt9z0dg%2F2e%2FTSzClhqnS7v400fX%2BqBeY36paS7Rq5KCXghjMYQ%2B%2FT7PL9e0lpd8z19QsMgP22sdNI3DBybhRlINO9pBtlzxCn9xNjh63BgBUGjXlbAUhcuC0fKWfpv0mw3SmzkWVoSJphd95E%2FoSJ6OXRvfYHxz7ODH5p6X8AdthMD%2BitjE7Gn%2FkVdmT5I3%2B9IesnsGdKB%2B3ATxF0KWjtHI2A49%2BOdPz6yWqplw13ruAau0SOZp07DcE0xf5547BiuHI7eW4GGy9VqmA1bTF84yJs8qmy0i9KWpFjH3cfiyU01kTOcs0YQ1SQFifRCNUu%2B91c7J9ptmoispHB2Ig6%2FHIDl7YuPmArD6JE7%2Fb4HOWJ85amjc1gTJiDrRP7VscVTBAOwyHXyhV4U68Zg8vmANWhAmvsLZGUfY6IPmW69AOEbLC2FQWjMsk%2B7DBbBi9pVCYJZ4z0fK5obC6xUUTvxpqTYrAOtxUs9dmMx4vO0YzPckU1LGM8W4wJCPFmeeauUGl8Bxhyi79g%2BsBmXlJKlOLGgB%2FAGXpKJKVDjyQejn0TY9CbfhBwdqANm26RIRxrv9%2BWoyhlUd6HS29TWQzDE%2F%2Be8BjqkAU871JvysENOTrRiBg%2B4jRwbmUiCYoikAPQ9v9aQhe44djm6IPbdDnvYjknid4%2FkCPBncZ069tC2YiahizPHZb98XCww3gFA4U2JFghoIWfmH8UT7X5MycNAtdA9r0y9HtZQkQWYBoT7q0SSIflNNA2OZjoxEaeogZwkd5zu%2FS3Re2nTGcYA5GJTx3D9D49PnmoZXWVKLPVZg%2BJstLRuLauYrpdJ&X-Amz-Signature=868951171484d7492859ea46012bfc8e1bf5b1d92455c690cb56d5a421ad109c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KN4AX6A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkJw42UgCKK2yFN7y36pFsjyXjL9XLZrRg9u3%2F0f7SaAIhAJIs64VpspISgV%2BWp2AEHl4IiCle%2FKHcmtCidDrNi%2B04KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2AitNhttt9ISoxagq3AOIvdOrvOpWfz6FDwbbIt%2FMq6HBEpyKUZtCIYkP5HnVAay%2FmDHQK7hNuUAPGZNG97nHvker3WP7vJQnRVFjUtyBvKWNtVbJdfF%2BnBN%2FT1GxbFdhAUdd59fAIrb64a76%2Fams8LTvREd9gE8WNtNBKCvco92qavB8zBlP8Q99LBGVOm%2BmYRIRdgr6tuTnWKZSdzWMZI2Ahkz4bbwo0yNQIO8noe3ARHtcgG3hJosS3IokbEHjkOPpoCLRxr5pSi3j0KAB5gW18%2Bt5OLeN6WhUaij1Afai69YRY2E8qTCLfiGQP0Nxii7kCynjvCV1YJlg0skMfGQTeaKvSqQVF%2B5dA81p3lio3O5m07VfVEerPDAj1EvYIFxLMybiV9qoa3sAzZCZx6M%2FsZte4ACqPSPVEA01FVwG2SbPYviP3BOE91H7QiSbwZuOynpjCZ36He3el2sdsskE6iPrjfwwKdZmEKgOvk%2F%2FYSrYR88T5iBA6y83eC8QuGq31mXTTvR%2BhWVtHJyUyaiiCV8eg0IbM16ARrMjKAPLwHy8ih7kVFM5FiSpZyFVYkRDRkkmPZ5Ey%2Bs3WuYe95nvuI782UZWejqPn%2F%2FNSBGC%2F8JZCqdpSku%2F8rMFZbZxJIjYcO4u6J0xeDDN%2Fue8BjqkAYjnpKdwFrNzaJ7pzToFMcaXYozpZdMM0jPN8chZ%2Fr8ZDqUNUxc%2FXsUr801s%2FVxg8o7v3bnmgyRD8dIzO%2B5%2B72c7RtjLmPDfgfErDUNwdeyrvo8pLiQMAsOxGJ%2BTM9Cb25FA9iaVlZUzcor7Smg%2FVVP%2BEtlXDSPrHgdOGPFoAxqpcUs2fSwTZj692qcrgDNFyqvwQdZaY795loS%2F40b%2FNPJpuMkb&X-Amz-Signature=de52f9017a499cbbbd0b116835ba52495ead3ccee4837c5703b6ce423eaa116b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KN4AX6A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkJw42UgCKK2yFN7y36pFsjyXjL9XLZrRg9u3%2F0f7SaAIhAJIs64VpspISgV%2BWp2AEHl4IiCle%2FKHcmtCidDrNi%2B04KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2AitNhttt9ISoxagq3AOIvdOrvOpWfz6FDwbbIt%2FMq6HBEpyKUZtCIYkP5HnVAay%2FmDHQK7hNuUAPGZNG97nHvker3WP7vJQnRVFjUtyBvKWNtVbJdfF%2BnBN%2FT1GxbFdhAUdd59fAIrb64a76%2Fams8LTvREd9gE8WNtNBKCvco92qavB8zBlP8Q99LBGVOm%2BmYRIRdgr6tuTnWKZSdzWMZI2Ahkz4bbwo0yNQIO8noe3ARHtcgG3hJosS3IokbEHjkOPpoCLRxr5pSi3j0KAB5gW18%2Bt5OLeN6WhUaij1Afai69YRY2E8qTCLfiGQP0Nxii7kCynjvCV1YJlg0skMfGQTeaKvSqQVF%2B5dA81p3lio3O5m07VfVEerPDAj1EvYIFxLMybiV9qoa3sAzZCZx6M%2FsZte4ACqPSPVEA01FVwG2SbPYviP3BOE91H7QiSbwZuOynpjCZ36He3el2sdsskE6iPrjfwwKdZmEKgOvk%2F%2FYSrYR88T5iBA6y83eC8QuGq31mXTTvR%2BhWVtHJyUyaiiCV8eg0IbM16ARrMjKAPLwHy8ih7kVFM5FiSpZyFVYkRDRkkmPZ5Ey%2Bs3WuYe95nvuI782UZWejqPn%2F%2FNSBGC%2F8JZCqdpSku%2F8rMFZbZxJIjYcO4u6J0xeDDN%2Fue8BjqkAYjnpKdwFrNzaJ7pzToFMcaXYozpZdMM0jPN8chZ%2Fr8ZDqUNUxc%2FXsUr801s%2FVxg8o7v3bnmgyRD8dIzO%2B5%2B72c7RtjLmPDfgfErDUNwdeyrvo8pLiQMAsOxGJ%2BTM9Cb25FA9iaVlZUzcor7Smg%2FVVP%2BEtlXDSPrHgdOGPFoAxqpcUs2fSwTZj692qcrgDNFyqvwQdZaY795loS%2F40b%2FNPJpuMkb&X-Amz-Signature=886a7dcdeb694f210030681df64ae801fb90f1c60e2c76f10d658a692e228a47&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
