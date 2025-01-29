

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAF5NKLR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKfLaCuRCBqQmyBUpwgPGJV6%2BXoAbt2l9H014c%2FtTqAAiEA4SHDbjlpkd8iUBRH8C%2F5B6zXI52E7EmCrHkVhf65rcsqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB36gYs6H8s1S22g%2BCrcA%2FG5sMa5Grs%2BgC2PBVAXpoA29FBB7Lm%2F%2FHpaaPk8r6b9L0xPejKdrPPTqc6KMJWJLaiaJF4guEn%2B8ORah2EiysmO0S9%2BLKbN4Ei5fQgvNxovQwHmpatIJ0tIIc6CN5rw3A%2By3aDaNpJ0JduQK29rAdFzxO8g2fpDJnIFp5%2Fr%2FJnUABGU8MJo7r%2F7sWv6zReNdZhzc%2BkSq5wD4qWovZWkHn4bSYnUVBclqQoIRLjHM7l40MadIt9drIh17CyV7kuHLameh8JQmt1vUIHSC9QfOJy7kobCHdGRp6ZCdWlwmBjgx4qbfsRoj0v6OVW3Hsbf6jevo5OVemHPDfpkboXZ4%2BL8fGnIvghBqLZ1dmE0zBCsfD4gnBbOwuG7U7BpNUKGIzpn1F6zME2AnxzIrd7atkigKEkstt4pKc9T6lkkq3qBi68lS%2BeFL4sdHR3P1LwYqycqfzen0h4cpaga%2Bnu%2FywsTbOtlV%2FZj5%2BEQXxogHgIa0nVnp65dTY%2F5wdQh2ZU1o9FKdj%2FVsUEE5SElRhNkD5hnmRtQBF2PsIh%2FCE8vL0Dbdmk%2BIL52LwnH4540%2FTu6Vdv%2BQnCNrCVAxYYMd6PJgqMC%2FOcMw2FbjUdzT%2B%2F2mC3mkmvebSnVC2lSd3NjMML%2B57wGOqUBpOyV7EkiBmBgnCNRmgvxUqdOYQjqNyJf5BIo%2BxfvgsQb%2Fx42y6UNu3SNNY8uwuHjllx6Hk7lmfucKAyhA8siZMGZQ3yyV5hZ72et8lxl1baOdIsP0bHOuXqcp5q6UVNojGngSkntXcACS1sLYdq6gbyJpWS7hfWTioDP2s2MqI5YdLSL9rB%2BpS79XKwRBmp%2Flf4AJnadgPPf2mg5PbhR2XvEIkb%2B&X-Amz-Signature=65c07dac70cf4f0835575d9e77c7c4ed70a0af50fffc4dde658e87c6ef96ff0c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAF5NKLR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKfLaCuRCBqQmyBUpwgPGJV6%2BXoAbt2l9H014c%2FtTqAAiEA4SHDbjlpkd8iUBRH8C%2F5B6zXI52E7EmCrHkVhf65rcsqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB36gYs6H8s1S22g%2BCrcA%2FG5sMa5Grs%2BgC2PBVAXpoA29FBB7Lm%2F%2FHpaaPk8r6b9L0xPejKdrPPTqc6KMJWJLaiaJF4guEn%2B8ORah2EiysmO0S9%2BLKbN4Ei5fQgvNxovQwHmpatIJ0tIIc6CN5rw3A%2By3aDaNpJ0JduQK29rAdFzxO8g2fpDJnIFp5%2Fr%2FJnUABGU8MJo7r%2F7sWv6zReNdZhzc%2BkSq5wD4qWovZWkHn4bSYnUVBclqQoIRLjHM7l40MadIt9drIh17CyV7kuHLameh8JQmt1vUIHSC9QfOJy7kobCHdGRp6ZCdWlwmBjgx4qbfsRoj0v6OVW3Hsbf6jevo5OVemHPDfpkboXZ4%2BL8fGnIvghBqLZ1dmE0zBCsfD4gnBbOwuG7U7BpNUKGIzpn1F6zME2AnxzIrd7atkigKEkstt4pKc9T6lkkq3qBi68lS%2BeFL4sdHR3P1LwYqycqfzen0h4cpaga%2Bnu%2FywsTbOtlV%2FZj5%2BEQXxogHgIa0nVnp65dTY%2F5wdQh2ZU1o9FKdj%2FVsUEE5SElRhNkD5hnmRtQBF2PsIh%2FCE8vL0Dbdmk%2BIL52LwnH4540%2FTu6Vdv%2BQnCNrCVAxYYMd6PJgqMC%2FOcMw2FbjUdzT%2B%2F2mC3mkmvebSnVC2lSd3NjMML%2B57wGOqUBpOyV7EkiBmBgnCNRmgvxUqdOYQjqNyJf5BIo%2BxfvgsQb%2Fx42y6UNu3SNNY8uwuHjllx6Hk7lmfucKAyhA8siZMGZQ3yyV5hZ72et8lxl1baOdIsP0bHOuXqcp5q6UVNojGngSkntXcACS1sLYdq6gbyJpWS7hfWTioDP2s2MqI5YdLSL9rB%2BpS79XKwRBmp%2Flf4AJnadgPPf2mg5PbhR2XvEIkb%2B&X-Amz-Signature=78d31bd038fa591a7e42b5428cf27f208d09e115237348fc51af95691eea3043&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAF5NKLR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKfLaCuRCBqQmyBUpwgPGJV6%2BXoAbt2l9H014c%2FtTqAAiEA4SHDbjlpkd8iUBRH8C%2F5B6zXI52E7EmCrHkVhf65rcsqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB36gYs6H8s1S22g%2BCrcA%2FG5sMa5Grs%2BgC2PBVAXpoA29FBB7Lm%2F%2FHpaaPk8r6b9L0xPejKdrPPTqc6KMJWJLaiaJF4guEn%2B8ORah2EiysmO0S9%2BLKbN4Ei5fQgvNxovQwHmpatIJ0tIIc6CN5rw3A%2By3aDaNpJ0JduQK29rAdFzxO8g2fpDJnIFp5%2Fr%2FJnUABGU8MJo7r%2F7sWv6zReNdZhzc%2BkSq5wD4qWovZWkHn4bSYnUVBclqQoIRLjHM7l40MadIt9drIh17CyV7kuHLameh8JQmt1vUIHSC9QfOJy7kobCHdGRp6ZCdWlwmBjgx4qbfsRoj0v6OVW3Hsbf6jevo5OVemHPDfpkboXZ4%2BL8fGnIvghBqLZ1dmE0zBCsfD4gnBbOwuG7U7BpNUKGIzpn1F6zME2AnxzIrd7atkigKEkstt4pKc9T6lkkq3qBi68lS%2BeFL4sdHR3P1LwYqycqfzen0h4cpaga%2Bnu%2FywsTbOtlV%2FZj5%2BEQXxogHgIa0nVnp65dTY%2F5wdQh2ZU1o9FKdj%2FVsUEE5SElRhNkD5hnmRtQBF2PsIh%2FCE8vL0Dbdmk%2BIL52LwnH4540%2FTu6Vdv%2BQnCNrCVAxYYMd6PJgqMC%2FOcMw2FbjUdzT%2B%2F2mC3mkmvebSnVC2lSd3NjMML%2B57wGOqUBpOyV7EkiBmBgnCNRmgvxUqdOYQjqNyJf5BIo%2BxfvgsQb%2Fx42y6UNu3SNNY8uwuHjllx6Hk7lmfucKAyhA8siZMGZQ3yyV5hZ72et8lxl1baOdIsP0bHOuXqcp5q6UVNojGngSkntXcACS1sLYdq6gbyJpWS7hfWTioDP2s2MqI5YdLSL9rB%2BpS79XKwRBmp%2Flf4AJnadgPPf2mg5PbhR2XvEIkb%2B&X-Amz-Signature=d1b207b448e1e4b765b19d513a74de9ba8d816c3ed275aa4be6a8b5438eb048a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAF5NKLR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKfLaCuRCBqQmyBUpwgPGJV6%2BXoAbt2l9H014c%2FtTqAAiEA4SHDbjlpkd8iUBRH8C%2F5B6zXI52E7EmCrHkVhf65rcsqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB36gYs6H8s1S22g%2BCrcA%2FG5sMa5Grs%2BgC2PBVAXpoA29FBB7Lm%2F%2FHpaaPk8r6b9L0xPejKdrPPTqc6KMJWJLaiaJF4guEn%2B8ORah2EiysmO0S9%2BLKbN4Ei5fQgvNxovQwHmpatIJ0tIIc6CN5rw3A%2By3aDaNpJ0JduQK29rAdFzxO8g2fpDJnIFp5%2Fr%2FJnUABGU8MJo7r%2F7sWv6zReNdZhzc%2BkSq5wD4qWovZWkHn4bSYnUVBclqQoIRLjHM7l40MadIt9drIh17CyV7kuHLameh8JQmt1vUIHSC9QfOJy7kobCHdGRp6ZCdWlwmBjgx4qbfsRoj0v6OVW3Hsbf6jevo5OVemHPDfpkboXZ4%2BL8fGnIvghBqLZ1dmE0zBCsfD4gnBbOwuG7U7BpNUKGIzpn1F6zME2AnxzIrd7atkigKEkstt4pKc9T6lkkq3qBi68lS%2BeFL4sdHR3P1LwYqycqfzen0h4cpaga%2Bnu%2FywsTbOtlV%2FZj5%2BEQXxogHgIa0nVnp65dTY%2F5wdQh2ZU1o9FKdj%2FVsUEE5SElRhNkD5hnmRtQBF2PsIh%2FCE8vL0Dbdmk%2BIL52LwnH4540%2FTu6Vdv%2BQnCNrCVAxYYMd6PJgqMC%2FOcMw2FbjUdzT%2B%2F2mC3mkmvebSnVC2lSd3NjMML%2B57wGOqUBpOyV7EkiBmBgnCNRmgvxUqdOYQjqNyJf5BIo%2BxfvgsQb%2Fx42y6UNu3SNNY8uwuHjllx6Hk7lmfucKAyhA8siZMGZQ3yyV5hZ72et8lxl1baOdIsP0bHOuXqcp5q6UVNojGngSkntXcACS1sLYdq6gbyJpWS7hfWTioDP2s2MqI5YdLSL9rB%2BpS79XKwRBmp%2Flf4AJnadgPPf2mg5PbhR2XvEIkb%2B&X-Amz-Signature=50cb177ab41f45dcec9ab92fce45ecaac60f8e1ea9c920dfbedcf3aad9fd54e6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAF5NKLR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKfLaCuRCBqQmyBUpwgPGJV6%2BXoAbt2l9H014c%2FtTqAAiEA4SHDbjlpkd8iUBRH8C%2F5B6zXI52E7EmCrHkVhf65rcsqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB36gYs6H8s1S22g%2BCrcA%2FG5sMa5Grs%2BgC2PBVAXpoA29FBB7Lm%2F%2FHpaaPk8r6b9L0xPejKdrPPTqc6KMJWJLaiaJF4guEn%2B8ORah2EiysmO0S9%2BLKbN4Ei5fQgvNxovQwHmpatIJ0tIIc6CN5rw3A%2By3aDaNpJ0JduQK29rAdFzxO8g2fpDJnIFp5%2Fr%2FJnUABGU8MJo7r%2F7sWv6zReNdZhzc%2BkSq5wD4qWovZWkHn4bSYnUVBclqQoIRLjHM7l40MadIt9drIh17CyV7kuHLameh8JQmt1vUIHSC9QfOJy7kobCHdGRp6ZCdWlwmBjgx4qbfsRoj0v6OVW3Hsbf6jevo5OVemHPDfpkboXZ4%2BL8fGnIvghBqLZ1dmE0zBCsfD4gnBbOwuG7U7BpNUKGIzpn1F6zME2AnxzIrd7atkigKEkstt4pKc9T6lkkq3qBi68lS%2BeFL4sdHR3P1LwYqycqfzen0h4cpaga%2Bnu%2FywsTbOtlV%2FZj5%2BEQXxogHgIa0nVnp65dTY%2F5wdQh2ZU1o9FKdj%2FVsUEE5SElRhNkD5hnmRtQBF2PsIh%2FCE8vL0Dbdmk%2BIL52LwnH4540%2FTu6Vdv%2BQnCNrCVAxYYMd6PJgqMC%2FOcMw2FbjUdzT%2B%2F2mC3mkmvebSnVC2lSd3NjMML%2B57wGOqUBpOyV7EkiBmBgnCNRmgvxUqdOYQjqNyJf5BIo%2BxfvgsQb%2Fx42y6UNu3SNNY8uwuHjllx6Hk7lmfucKAyhA8siZMGZQ3yyV5hZ72et8lxl1baOdIsP0bHOuXqcp5q6UVNojGngSkntXcACS1sLYdq6gbyJpWS7hfWTioDP2s2MqI5YdLSL9rB%2BpS79XKwRBmp%2Flf4AJnadgPPf2mg5PbhR2XvEIkb%2B&X-Amz-Signature=c1779fd7f37189fc3ad16f9af6a485969d80895bd7fe2b42a75af5e51203548b&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAF5NKLR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKfLaCuRCBqQmyBUpwgPGJV6%2BXoAbt2l9H014c%2FtTqAAiEA4SHDbjlpkd8iUBRH8C%2F5B6zXI52E7EmCrHkVhf65rcsqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB36gYs6H8s1S22g%2BCrcA%2FG5sMa5Grs%2BgC2PBVAXpoA29FBB7Lm%2F%2FHpaaPk8r6b9L0xPejKdrPPTqc6KMJWJLaiaJF4guEn%2B8ORah2EiysmO0S9%2BLKbN4Ei5fQgvNxovQwHmpatIJ0tIIc6CN5rw3A%2By3aDaNpJ0JduQK29rAdFzxO8g2fpDJnIFp5%2Fr%2FJnUABGU8MJo7r%2F7sWv6zReNdZhzc%2BkSq5wD4qWovZWkHn4bSYnUVBclqQoIRLjHM7l40MadIt9drIh17CyV7kuHLameh8JQmt1vUIHSC9QfOJy7kobCHdGRp6ZCdWlwmBjgx4qbfsRoj0v6OVW3Hsbf6jevo5OVemHPDfpkboXZ4%2BL8fGnIvghBqLZ1dmE0zBCsfD4gnBbOwuG7U7BpNUKGIzpn1F6zME2AnxzIrd7atkigKEkstt4pKc9T6lkkq3qBi68lS%2BeFL4sdHR3P1LwYqycqfzen0h4cpaga%2Bnu%2FywsTbOtlV%2FZj5%2BEQXxogHgIa0nVnp65dTY%2F5wdQh2ZU1o9FKdj%2FVsUEE5SElRhNkD5hnmRtQBF2PsIh%2FCE8vL0Dbdmk%2BIL52LwnH4540%2FTu6Vdv%2BQnCNrCVAxYYMd6PJgqMC%2FOcMw2FbjUdzT%2B%2F2mC3mkmvebSnVC2lSd3NjMML%2B57wGOqUBpOyV7EkiBmBgnCNRmgvxUqdOYQjqNyJf5BIo%2BxfvgsQb%2Fx42y6UNu3SNNY8uwuHjllx6Hk7lmfucKAyhA8siZMGZQ3yyV5hZ72et8lxl1baOdIsP0bHOuXqcp5q6UVNojGngSkntXcACS1sLYdq6gbyJpWS7hfWTioDP2s2MqI5YdLSL9rB%2BpS79XKwRBmp%2Flf4AJnadgPPf2mg5PbhR2XvEIkb%2B&X-Amz-Signature=de6473bb0bb3ff7f2eb62fd634a96350b77af157eb5fb718daca278b92a04865&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAF5NKLR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKfLaCuRCBqQmyBUpwgPGJV6%2BXoAbt2l9H014c%2FtTqAAiEA4SHDbjlpkd8iUBRH8C%2F5B6zXI52E7EmCrHkVhf65rcsqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB36gYs6H8s1S22g%2BCrcA%2FG5sMa5Grs%2BgC2PBVAXpoA29FBB7Lm%2F%2FHpaaPk8r6b9L0xPejKdrPPTqc6KMJWJLaiaJF4guEn%2B8ORah2EiysmO0S9%2BLKbN4Ei5fQgvNxovQwHmpatIJ0tIIc6CN5rw3A%2By3aDaNpJ0JduQK29rAdFzxO8g2fpDJnIFp5%2Fr%2FJnUABGU8MJo7r%2F7sWv6zReNdZhzc%2BkSq5wD4qWovZWkHn4bSYnUVBclqQoIRLjHM7l40MadIt9drIh17CyV7kuHLameh8JQmt1vUIHSC9QfOJy7kobCHdGRp6ZCdWlwmBjgx4qbfsRoj0v6OVW3Hsbf6jevo5OVemHPDfpkboXZ4%2BL8fGnIvghBqLZ1dmE0zBCsfD4gnBbOwuG7U7BpNUKGIzpn1F6zME2AnxzIrd7atkigKEkstt4pKc9T6lkkq3qBi68lS%2BeFL4sdHR3P1LwYqycqfzen0h4cpaga%2Bnu%2FywsTbOtlV%2FZj5%2BEQXxogHgIa0nVnp65dTY%2F5wdQh2ZU1o9FKdj%2FVsUEE5SElRhNkD5hnmRtQBF2PsIh%2FCE8vL0Dbdmk%2BIL52LwnH4540%2FTu6Vdv%2BQnCNrCVAxYYMd6PJgqMC%2FOcMw2FbjUdzT%2B%2F2mC3mkmvebSnVC2lSd3NjMML%2B57wGOqUBpOyV7EkiBmBgnCNRmgvxUqdOYQjqNyJf5BIo%2BxfvgsQb%2Fx42y6UNu3SNNY8uwuHjllx6Hk7lmfucKAyhA8siZMGZQ3yyV5hZ72et8lxl1baOdIsP0bHOuXqcp5q6UVNojGngSkntXcACS1sLYdq6gbyJpWS7hfWTioDP2s2MqI5YdLSL9rB%2BpS79XKwRBmp%2Flf4AJnadgPPf2mg5PbhR2XvEIkb%2B&X-Amz-Signature=e3b381ada744fae133a803ebf02a73e14afca372c72b7a3263a0b0a8e88ddf62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAF5NKLR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKfLaCuRCBqQmyBUpwgPGJV6%2BXoAbt2l9H014c%2FtTqAAiEA4SHDbjlpkd8iUBRH8C%2F5B6zXI52E7EmCrHkVhf65rcsqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB36gYs6H8s1S22g%2BCrcA%2FG5sMa5Grs%2BgC2PBVAXpoA29FBB7Lm%2F%2FHpaaPk8r6b9L0xPejKdrPPTqc6KMJWJLaiaJF4guEn%2B8ORah2EiysmO0S9%2BLKbN4Ei5fQgvNxovQwHmpatIJ0tIIc6CN5rw3A%2By3aDaNpJ0JduQK29rAdFzxO8g2fpDJnIFp5%2Fr%2FJnUABGU8MJo7r%2F7sWv6zReNdZhzc%2BkSq5wD4qWovZWkHn4bSYnUVBclqQoIRLjHM7l40MadIt9drIh17CyV7kuHLameh8JQmt1vUIHSC9QfOJy7kobCHdGRp6ZCdWlwmBjgx4qbfsRoj0v6OVW3Hsbf6jevo5OVemHPDfpkboXZ4%2BL8fGnIvghBqLZ1dmE0zBCsfD4gnBbOwuG7U7BpNUKGIzpn1F6zME2AnxzIrd7atkigKEkstt4pKc9T6lkkq3qBi68lS%2BeFL4sdHR3P1LwYqycqfzen0h4cpaga%2Bnu%2FywsTbOtlV%2FZj5%2BEQXxogHgIa0nVnp65dTY%2F5wdQh2ZU1o9FKdj%2FVsUEE5SElRhNkD5hnmRtQBF2PsIh%2FCE8vL0Dbdmk%2BIL52LwnH4540%2FTu6Vdv%2BQnCNrCVAxYYMd6PJgqMC%2FOcMw2FbjUdzT%2B%2F2mC3mkmvebSnVC2lSd3NjMML%2B57wGOqUBpOyV7EkiBmBgnCNRmgvxUqdOYQjqNyJf5BIo%2BxfvgsQb%2Fx42y6UNu3SNNY8uwuHjllx6Hk7lmfucKAyhA8siZMGZQ3yyV5hZ72et8lxl1baOdIsP0bHOuXqcp5q6UVNojGngSkntXcACS1sLYdq6gbyJpWS7hfWTioDP2s2MqI5YdLSL9rB%2BpS79XKwRBmp%2Flf4AJnadgPPf2mg5PbhR2XvEIkb%2B&X-Amz-Signature=2490fc0bd3f68a437e16fddeab461e73612b68805c5e5d03a6dcf9c3a633e4c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAF5NKLR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKfLaCuRCBqQmyBUpwgPGJV6%2BXoAbt2l9H014c%2FtTqAAiEA4SHDbjlpkd8iUBRH8C%2F5B6zXI52E7EmCrHkVhf65rcsqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB36gYs6H8s1S22g%2BCrcA%2FG5sMa5Grs%2BgC2PBVAXpoA29FBB7Lm%2F%2FHpaaPk8r6b9L0xPejKdrPPTqc6KMJWJLaiaJF4guEn%2B8ORah2EiysmO0S9%2BLKbN4Ei5fQgvNxovQwHmpatIJ0tIIc6CN5rw3A%2By3aDaNpJ0JduQK29rAdFzxO8g2fpDJnIFp5%2Fr%2FJnUABGU8MJo7r%2F7sWv6zReNdZhzc%2BkSq5wD4qWovZWkHn4bSYnUVBclqQoIRLjHM7l40MadIt9drIh17CyV7kuHLameh8JQmt1vUIHSC9QfOJy7kobCHdGRp6ZCdWlwmBjgx4qbfsRoj0v6OVW3Hsbf6jevo5OVemHPDfpkboXZ4%2BL8fGnIvghBqLZ1dmE0zBCsfD4gnBbOwuG7U7BpNUKGIzpn1F6zME2AnxzIrd7atkigKEkstt4pKc9T6lkkq3qBi68lS%2BeFL4sdHR3P1LwYqycqfzen0h4cpaga%2Bnu%2FywsTbOtlV%2FZj5%2BEQXxogHgIa0nVnp65dTY%2F5wdQh2ZU1o9FKdj%2FVsUEE5SElRhNkD5hnmRtQBF2PsIh%2FCE8vL0Dbdmk%2BIL52LwnH4540%2FTu6Vdv%2BQnCNrCVAxYYMd6PJgqMC%2FOcMw2FbjUdzT%2B%2F2mC3mkmvebSnVC2lSd3NjMML%2B57wGOqUBpOyV7EkiBmBgnCNRmgvxUqdOYQjqNyJf5BIo%2BxfvgsQb%2Fx42y6UNu3SNNY8uwuHjllx6Hk7lmfucKAyhA8siZMGZQ3yyV5hZ72et8lxl1baOdIsP0bHOuXqcp5q6UVNojGngSkntXcACS1sLYdq6gbyJpWS7hfWTioDP2s2MqI5YdLSL9rB%2BpS79XKwRBmp%2Flf4AJnadgPPf2mg5PbhR2XvEIkb%2B&X-Amz-Signature=41bcdccfaf524d979efde0bb71f53e358daa493b31d7e226a00a0bf9ab257876&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UK3XTBLW%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXez1pX4j%2FYHDnIz0jnd7HKhdbxjYgTAsJuRNLBRFWcAiEAk91hDv053wF%2FgyOXy7mLWX2TELM0sgYJ46G%2FQR%2FQsOEqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNAg88J6z9CV3h1eoSrcA10LH737o4HpG5DwKLcV1yWe1QJnR9MTWar5aUl7Dhl1PSifFcBS1hFOVNJPgCqg8OoYjMpMFy7aZr0ZYFQNXCwHW0RyqoIZUIw%2FWGgdPxb4lAJAlfzrsbDEVQkEIK86Iyf3iPeIKh1vcS%2FBvL%2BkjxXwVHjCzx3GckTjQXvQJwqIvvhptWA2xH6t2I9JME4JNOL%2FSgvTkOJyB%2FsEPWnKXcqgldupbkNbYwB51Fs9nBXxhiayCEnz216zTl5O106lpdoj%2BYYgeQ5us%2B1L%2BDCwQucLAIpzjqpb2jrfDjmnJXrLLZJsWSjOosad%2BnrsyULm7MbmXs9R5LUB2ol2N3CpCkVn6S7s8jDgC3gSLDqLm2duv0S8GZ9bizW8Y%2BknNMQoKdpUbkANQTqNSYFWesw%2FBD%2BSTbw7%2F69gGH1wRFpBqe4B7ZdsTRhRUFQW0z4H%2F7exK4peNCE5C%2BMpgs0FE1LJpn19W14cGfDps2HHbUVcC8vZQcXw9TZflVMT4JyvlwOvUbzwMNtnTxxnnqxp2bc15Y%2FzonBfO9fDdda2yqf5uyScd9f0u3fKN345vWmS0aZn9ZqsRqK5y1%2F58uVgCYd%2Bm1JNMzQAkB4OEVtm4mN9cQ%2FNRH7EWxGuU8E7f9MxMKfj57wGOqUBLeZwePMhLjK6%2BqbbiMTaq2VWSBmmJzTEcE8OZhYuTR2uqeC9%2Fri8uR1fKuqhJPTuxLLJBbAW%2BLZDJjfFAoo4C1wKerwnJUczJVROw9DgdGq2F%2F9%2F5o6UOeehJ8601E4u89Uvn3oRxV8egI8m9edJ9PPBthl8M73k0B6rECqxJGNo7FlZ%2FFNjxY371J5IMHR3TYtU7eenjDmjCPR%2B%2BZU1vhoO8EUZ&X-Amz-Signature=b25e16a328291533ecf95e1fb955c19c72ae1568cab181961f8970cb63c04718&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UK3XTBLW%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXez1pX4j%2FYHDnIz0jnd7HKhdbxjYgTAsJuRNLBRFWcAiEAk91hDv053wF%2FgyOXy7mLWX2TELM0sgYJ46G%2FQR%2FQsOEqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNAg88J6z9CV3h1eoSrcA10LH737o4HpG5DwKLcV1yWe1QJnR9MTWar5aUl7Dhl1PSifFcBS1hFOVNJPgCqg8OoYjMpMFy7aZr0ZYFQNXCwHW0RyqoIZUIw%2FWGgdPxb4lAJAlfzrsbDEVQkEIK86Iyf3iPeIKh1vcS%2FBvL%2BkjxXwVHjCzx3GckTjQXvQJwqIvvhptWA2xH6t2I9JME4JNOL%2FSgvTkOJyB%2FsEPWnKXcqgldupbkNbYwB51Fs9nBXxhiayCEnz216zTl5O106lpdoj%2BYYgeQ5us%2B1L%2BDCwQucLAIpzjqpb2jrfDjmnJXrLLZJsWSjOosad%2BnrsyULm7MbmXs9R5LUB2ol2N3CpCkVn6S7s8jDgC3gSLDqLm2duv0S8GZ9bizW8Y%2BknNMQoKdpUbkANQTqNSYFWesw%2FBD%2BSTbw7%2F69gGH1wRFpBqe4B7ZdsTRhRUFQW0z4H%2F7exK4peNCE5C%2BMpgs0FE1LJpn19W14cGfDps2HHbUVcC8vZQcXw9TZflVMT4JyvlwOvUbzwMNtnTxxnnqxp2bc15Y%2FzonBfO9fDdda2yqf5uyScd9f0u3fKN345vWmS0aZn9ZqsRqK5y1%2F58uVgCYd%2Bm1JNMzQAkB4OEVtm4mN9cQ%2FNRH7EWxGuU8E7f9MxMKfj57wGOqUBLeZwePMhLjK6%2BqbbiMTaq2VWSBmmJzTEcE8OZhYuTR2uqeC9%2Fri8uR1fKuqhJPTuxLLJBbAW%2BLZDJjfFAoo4C1wKerwnJUczJVROw9DgdGq2F%2F9%2F5o6UOeehJ8601E4u89Uvn3oRxV8egI8m9edJ9PPBthl8M73k0B6rECqxJGNo7FlZ%2FFNjxY371J5IMHR3TYtU7eenjDmjCPR%2B%2BZU1vhoO8EUZ&X-Amz-Signature=21ab70c8e665820e2ea3c83df6bde743fca75a91a07dfda724458e574a3a223b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
