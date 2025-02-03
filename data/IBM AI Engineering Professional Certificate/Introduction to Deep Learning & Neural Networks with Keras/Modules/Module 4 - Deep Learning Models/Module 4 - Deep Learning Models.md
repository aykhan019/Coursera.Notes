

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXDWDH5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYv09Lmaw4Sak%2F4vGYprIP1pFXfPwCYBW9ejpnTWIuoAiEArJT4hRrdJDeUuINImmCrguF8sE%2FcrUxzPQUdD0HUnHoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGll3cXFaKTsLbM0sCrcAyulRMCLuL6uEHSiIMv2cXZUAnZM2l1aBPXkyoZk28GYBEUFt9icN91ehbMW7c4sCXqIk2fNyTVSCb%2B1N0Zu3TNv1hfME0T8vtaGqJEL6m7rTU0BXFBiZXtIkrTUSVVQzaOUwk4DmmVT6EcOvV%2FcxR5ECzSDfycApDoVl4NSDnVRhbv1iy%2FD4hfIPq%2FXXjpuPgg%2F6Do0ZJqW1ZrDXob5iGgDXHijXSAKOH%2F71KyM%2B58yL%2FsOoUPDucoKyFjTO7%2BrvWNXuI4gK80RXuc%2FixU9MFjYxSDxdVPrjIJZSeh2in55ti7oGpfjK%2F9dTD7H9zt86QNYPwC5lgK18vtZMi8OCTm7Kh2nV7gpEHprYhmLbpAdJr2vzeWqbbtbRx%2FnkxNTfnxZIOzBPjjTrwCEbzcrsiC7kTwznoZdGwcs4h0yFDaRQKfTcR%2BIDO8e1qd0xSlnG7KtF0cROC8qzWbLACygX6FR5KzVhExlRdkAaCI%2B2PGkfGciaTj9LgnCSgDnXR%2BcePlszjNQPbtd7kL%2BEornDYClFBV%2FyJYjUMftxpufF3xlblRrRZxAo5w187pxs1r8HTWcqKI10dVLEasETCOLr2NgT3pYnH0CsD5xFGkt5vcB1ccPD6EUZdAixXQOMK%2Fzgb0GOqUBE8hWLYKg9jW%2FyR4G1hIEzdM0JMNhsS29brfZcQzQ8d8gbabSZKPeUYm%2BJQ4XabFmzZcmJq3RZ8MtgAFogRKvDGWIZN8tQB4dji0lUCmrOjuA5Krt7G6sOz59FTgImY4xgZ3l4wtIKDA8bojzQHxF66ycbbu0SW3XbQYZrmq0ZwRHq0t0HMwZhWe%2F0PtxfyMZrzUGHjtxLpCR4nG%2BxkxwZRx%2B2VcI&X-Amz-Signature=5449a582f2c815db043904e5d126ab8c2f141a3fc96d71aaa451dd47e539cead&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXDWDH5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYv09Lmaw4Sak%2F4vGYprIP1pFXfPwCYBW9ejpnTWIuoAiEArJT4hRrdJDeUuINImmCrguF8sE%2FcrUxzPQUdD0HUnHoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGll3cXFaKTsLbM0sCrcAyulRMCLuL6uEHSiIMv2cXZUAnZM2l1aBPXkyoZk28GYBEUFt9icN91ehbMW7c4sCXqIk2fNyTVSCb%2B1N0Zu3TNv1hfME0T8vtaGqJEL6m7rTU0BXFBiZXtIkrTUSVVQzaOUwk4DmmVT6EcOvV%2FcxR5ECzSDfycApDoVl4NSDnVRhbv1iy%2FD4hfIPq%2FXXjpuPgg%2F6Do0ZJqW1ZrDXob5iGgDXHijXSAKOH%2F71KyM%2B58yL%2FsOoUPDucoKyFjTO7%2BrvWNXuI4gK80RXuc%2FixU9MFjYxSDxdVPrjIJZSeh2in55ti7oGpfjK%2F9dTD7H9zt86QNYPwC5lgK18vtZMi8OCTm7Kh2nV7gpEHprYhmLbpAdJr2vzeWqbbtbRx%2FnkxNTfnxZIOzBPjjTrwCEbzcrsiC7kTwznoZdGwcs4h0yFDaRQKfTcR%2BIDO8e1qd0xSlnG7KtF0cROC8qzWbLACygX6FR5KzVhExlRdkAaCI%2B2PGkfGciaTj9LgnCSgDnXR%2BcePlszjNQPbtd7kL%2BEornDYClFBV%2FyJYjUMftxpufF3xlblRrRZxAo5w187pxs1r8HTWcqKI10dVLEasETCOLr2NgT3pYnH0CsD5xFGkt5vcB1ccPD6EUZdAixXQOMK%2Fzgb0GOqUBE8hWLYKg9jW%2FyR4G1hIEzdM0JMNhsS29brfZcQzQ8d8gbabSZKPeUYm%2BJQ4XabFmzZcmJq3RZ8MtgAFogRKvDGWIZN8tQB4dji0lUCmrOjuA5Krt7G6sOz59FTgImY4xgZ3l4wtIKDA8bojzQHxF66ycbbu0SW3XbQYZrmq0ZwRHq0t0HMwZhWe%2F0PtxfyMZrzUGHjtxLpCR4nG%2BxkxwZRx%2B2VcI&X-Amz-Signature=c0db966bfb0eded12c54feefa76228bfa9f4209e7e43ce0ba86a99e22d054492&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXDWDH5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYv09Lmaw4Sak%2F4vGYprIP1pFXfPwCYBW9ejpnTWIuoAiEArJT4hRrdJDeUuINImmCrguF8sE%2FcrUxzPQUdD0HUnHoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGll3cXFaKTsLbM0sCrcAyulRMCLuL6uEHSiIMv2cXZUAnZM2l1aBPXkyoZk28GYBEUFt9icN91ehbMW7c4sCXqIk2fNyTVSCb%2B1N0Zu3TNv1hfME0T8vtaGqJEL6m7rTU0BXFBiZXtIkrTUSVVQzaOUwk4DmmVT6EcOvV%2FcxR5ECzSDfycApDoVl4NSDnVRhbv1iy%2FD4hfIPq%2FXXjpuPgg%2F6Do0ZJqW1ZrDXob5iGgDXHijXSAKOH%2F71KyM%2B58yL%2FsOoUPDucoKyFjTO7%2BrvWNXuI4gK80RXuc%2FixU9MFjYxSDxdVPrjIJZSeh2in55ti7oGpfjK%2F9dTD7H9zt86QNYPwC5lgK18vtZMi8OCTm7Kh2nV7gpEHprYhmLbpAdJr2vzeWqbbtbRx%2FnkxNTfnxZIOzBPjjTrwCEbzcrsiC7kTwznoZdGwcs4h0yFDaRQKfTcR%2BIDO8e1qd0xSlnG7KtF0cROC8qzWbLACygX6FR5KzVhExlRdkAaCI%2B2PGkfGciaTj9LgnCSgDnXR%2BcePlszjNQPbtd7kL%2BEornDYClFBV%2FyJYjUMftxpufF3xlblRrRZxAo5w187pxs1r8HTWcqKI10dVLEasETCOLr2NgT3pYnH0CsD5xFGkt5vcB1ccPD6EUZdAixXQOMK%2Fzgb0GOqUBE8hWLYKg9jW%2FyR4G1hIEzdM0JMNhsS29brfZcQzQ8d8gbabSZKPeUYm%2BJQ4XabFmzZcmJq3RZ8MtgAFogRKvDGWIZN8tQB4dji0lUCmrOjuA5Krt7G6sOz59FTgImY4xgZ3l4wtIKDA8bojzQHxF66ycbbu0SW3XbQYZrmq0ZwRHq0t0HMwZhWe%2F0PtxfyMZrzUGHjtxLpCR4nG%2BxkxwZRx%2B2VcI&X-Amz-Signature=c9547864818a5ea1a7d4238c467444fe5473794aadfe3aaf1b585ddbfd7215b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXDWDH5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYv09Lmaw4Sak%2F4vGYprIP1pFXfPwCYBW9ejpnTWIuoAiEArJT4hRrdJDeUuINImmCrguF8sE%2FcrUxzPQUdD0HUnHoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGll3cXFaKTsLbM0sCrcAyulRMCLuL6uEHSiIMv2cXZUAnZM2l1aBPXkyoZk28GYBEUFt9icN91ehbMW7c4sCXqIk2fNyTVSCb%2B1N0Zu3TNv1hfME0T8vtaGqJEL6m7rTU0BXFBiZXtIkrTUSVVQzaOUwk4DmmVT6EcOvV%2FcxR5ECzSDfycApDoVl4NSDnVRhbv1iy%2FD4hfIPq%2FXXjpuPgg%2F6Do0ZJqW1ZrDXob5iGgDXHijXSAKOH%2F71KyM%2B58yL%2FsOoUPDucoKyFjTO7%2BrvWNXuI4gK80RXuc%2FixU9MFjYxSDxdVPrjIJZSeh2in55ti7oGpfjK%2F9dTD7H9zt86QNYPwC5lgK18vtZMi8OCTm7Kh2nV7gpEHprYhmLbpAdJr2vzeWqbbtbRx%2FnkxNTfnxZIOzBPjjTrwCEbzcrsiC7kTwznoZdGwcs4h0yFDaRQKfTcR%2BIDO8e1qd0xSlnG7KtF0cROC8qzWbLACygX6FR5KzVhExlRdkAaCI%2B2PGkfGciaTj9LgnCSgDnXR%2BcePlszjNQPbtd7kL%2BEornDYClFBV%2FyJYjUMftxpufF3xlblRrRZxAo5w187pxs1r8HTWcqKI10dVLEasETCOLr2NgT3pYnH0CsD5xFGkt5vcB1ccPD6EUZdAixXQOMK%2Fzgb0GOqUBE8hWLYKg9jW%2FyR4G1hIEzdM0JMNhsS29brfZcQzQ8d8gbabSZKPeUYm%2BJQ4XabFmzZcmJq3RZ8MtgAFogRKvDGWIZN8tQB4dji0lUCmrOjuA5Krt7G6sOz59FTgImY4xgZ3l4wtIKDA8bojzQHxF66ycbbu0SW3XbQYZrmq0ZwRHq0t0HMwZhWe%2F0PtxfyMZrzUGHjtxLpCR4nG%2BxkxwZRx%2B2VcI&X-Amz-Signature=870469f0f5c02f1002a2526a769d4ec9178bbee55f0335c4fb73f284beea9379&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXDWDH5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYv09Lmaw4Sak%2F4vGYprIP1pFXfPwCYBW9ejpnTWIuoAiEArJT4hRrdJDeUuINImmCrguF8sE%2FcrUxzPQUdD0HUnHoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGll3cXFaKTsLbM0sCrcAyulRMCLuL6uEHSiIMv2cXZUAnZM2l1aBPXkyoZk28GYBEUFt9icN91ehbMW7c4sCXqIk2fNyTVSCb%2B1N0Zu3TNv1hfME0T8vtaGqJEL6m7rTU0BXFBiZXtIkrTUSVVQzaOUwk4DmmVT6EcOvV%2FcxR5ECzSDfycApDoVl4NSDnVRhbv1iy%2FD4hfIPq%2FXXjpuPgg%2F6Do0ZJqW1ZrDXob5iGgDXHijXSAKOH%2F71KyM%2B58yL%2FsOoUPDucoKyFjTO7%2BrvWNXuI4gK80RXuc%2FixU9MFjYxSDxdVPrjIJZSeh2in55ti7oGpfjK%2F9dTD7H9zt86QNYPwC5lgK18vtZMi8OCTm7Kh2nV7gpEHprYhmLbpAdJr2vzeWqbbtbRx%2FnkxNTfnxZIOzBPjjTrwCEbzcrsiC7kTwznoZdGwcs4h0yFDaRQKfTcR%2BIDO8e1qd0xSlnG7KtF0cROC8qzWbLACygX6FR5KzVhExlRdkAaCI%2B2PGkfGciaTj9LgnCSgDnXR%2BcePlszjNQPbtd7kL%2BEornDYClFBV%2FyJYjUMftxpufF3xlblRrRZxAo5w187pxs1r8HTWcqKI10dVLEasETCOLr2NgT3pYnH0CsD5xFGkt5vcB1ccPD6EUZdAixXQOMK%2Fzgb0GOqUBE8hWLYKg9jW%2FyR4G1hIEzdM0JMNhsS29brfZcQzQ8d8gbabSZKPeUYm%2BJQ4XabFmzZcmJq3RZ8MtgAFogRKvDGWIZN8tQB4dji0lUCmrOjuA5Krt7G6sOz59FTgImY4xgZ3l4wtIKDA8bojzQHxF66ycbbu0SW3XbQYZrmq0ZwRHq0t0HMwZhWe%2F0PtxfyMZrzUGHjtxLpCR4nG%2BxkxwZRx%2B2VcI&X-Amz-Signature=cfd23d2e38d300bae18ebb8927b1a2172bbc3b381a1bd5999d1137b5103394a2&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXDWDH5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYv09Lmaw4Sak%2F4vGYprIP1pFXfPwCYBW9ejpnTWIuoAiEArJT4hRrdJDeUuINImmCrguF8sE%2FcrUxzPQUdD0HUnHoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGll3cXFaKTsLbM0sCrcAyulRMCLuL6uEHSiIMv2cXZUAnZM2l1aBPXkyoZk28GYBEUFt9icN91ehbMW7c4sCXqIk2fNyTVSCb%2B1N0Zu3TNv1hfME0T8vtaGqJEL6m7rTU0BXFBiZXtIkrTUSVVQzaOUwk4DmmVT6EcOvV%2FcxR5ECzSDfycApDoVl4NSDnVRhbv1iy%2FD4hfIPq%2FXXjpuPgg%2F6Do0ZJqW1ZrDXob5iGgDXHijXSAKOH%2F71KyM%2B58yL%2FsOoUPDucoKyFjTO7%2BrvWNXuI4gK80RXuc%2FixU9MFjYxSDxdVPrjIJZSeh2in55ti7oGpfjK%2F9dTD7H9zt86QNYPwC5lgK18vtZMi8OCTm7Kh2nV7gpEHprYhmLbpAdJr2vzeWqbbtbRx%2FnkxNTfnxZIOzBPjjTrwCEbzcrsiC7kTwznoZdGwcs4h0yFDaRQKfTcR%2BIDO8e1qd0xSlnG7KtF0cROC8qzWbLACygX6FR5KzVhExlRdkAaCI%2B2PGkfGciaTj9LgnCSgDnXR%2BcePlszjNQPbtd7kL%2BEornDYClFBV%2FyJYjUMftxpufF3xlblRrRZxAo5w187pxs1r8HTWcqKI10dVLEasETCOLr2NgT3pYnH0CsD5xFGkt5vcB1ccPD6EUZdAixXQOMK%2Fzgb0GOqUBE8hWLYKg9jW%2FyR4G1hIEzdM0JMNhsS29brfZcQzQ8d8gbabSZKPeUYm%2BJQ4XabFmzZcmJq3RZ8MtgAFogRKvDGWIZN8tQB4dji0lUCmrOjuA5Krt7G6sOz59FTgImY4xgZ3l4wtIKDA8bojzQHxF66ycbbu0SW3XbQYZrmq0ZwRHq0t0HMwZhWe%2F0PtxfyMZrzUGHjtxLpCR4nG%2BxkxwZRx%2B2VcI&X-Amz-Signature=9a86ab9cd334de964168e78e6d0d184ca970f5ba7fcea2e5895d97146069f5ab&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXDWDH5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYv09Lmaw4Sak%2F4vGYprIP1pFXfPwCYBW9ejpnTWIuoAiEArJT4hRrdJDeUuINImmCrguF8sE%2FcrUxzPQUdD0HUnHoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGll3cXFaKTsLbM0sCrcAyulRMCLuL6uEHSiIMv2cXZUAnZM2l1aBPXkyoZk28GYBEUFt9icN91ehbMW7c4sCXqIk2fNyTVSCb%2B1N0Zu3TNv1hfME0T8vtaGqJEL6m7rTU0BXFBiZXtIkrTUSVVQzaOUwk4DmmVT6EcOvV%2FcxR5ECzSDfycApDoVl4NSDnVRhbv1iy%2FD4hfIPq%2FXXjpuPgg%2F6Do0ZJqW1ZrDXob5iGgDXHijXSAKOH%2F71KyM%2B58yL%2FsOoUPDucoKyFjTO7%2BrvWNXuI4gK80RXuc%2FixU9MFjYxSDxdVPrjIJZSeh2in55ti7oGpfjK%2F9dTD7H9zt86QNYPwC5lgK18vtZMi8OCTm7Kh2nV7gpEHprYhmLbpAdJr2vzeWqbbtbRx%2FnkxNTfnxZIOzBPjjTrwCEbzcrsiC7kTwznoZdGwcs4h0yFDaRQKfTcR%2BIDO8e1qd0xSlnG7KtF0cROC8qzWbLACygX6FR5KzVhExlRdkAaCI%2B2PGkfGciaTj9LgnCSgDnXR%2BcePlszjNQPbtd7kL%2BEornDYClFBV%2FyJYjUMftxpufF3xlblRrRZxAo5w187pxs1r8HTWcqKI10dVLEasETCOLr2NgT3pYnH0CsD5xFGkt5vcB1ccPD6EUZdAixXQOMK%2Fzgb0GOqUBE8hWLYKg9jW%2FyR4G1hIEzdM0JMNhsS29brfZcQzQ8d8gbabSZKPeUYm%2BJQ4XabFmzZcmJq3RZ8MtgAFogRKvDGWIZN8tQB4dji0lUCmrOjuA5Krt7G6sOz59FTgImY4xgZ3l4wtIKDA8bojzQHxF66ycbbu0SW3XbQYZrmq0ZwRHq0t0HMwZhWe%2F0PtxfyMZrzUGHjtxLpCR4nG%2BxkxwZRx%2B2VcI&X-Amz-Signature=82ab31b84459bdab8caf3ae3aa10db3c233d3814539ee8a0c827209e2699e253&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXDWDH5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYv09Lmaw4Sak%2F4vGYprIP1pFXfPwCYBW9ejpnTWIuoAiEArJT4hRrdJDeUuINImmCrguF8sE%2FcrUxzPQUdD0HUnHoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGll3cXFaKTsLbM0sCrcAyulRMCLuL6uEHSiIMv2cXZUAnZM2l1aBPXkyoZk28GYBEUFt9icN91ehbMW7c4sCXqIk2fNyTVSCb%2B1N0Zu3TNv1hfME0T8vtaGqJEL6m7rTU0BXFBiZXtIkrTUSVVQzaOUwk4DmmVT6EcOvV%2FcxR5ECzSDfycApDoVl4NSDnVRhbv1iy%2FD4hfIPq%2FXXjpuPgg%2F6Do0ZJqW1ZrDXob5iGgDXHijXSAKOH%2F71KyM%2B58yL%2FsOoUPDucoKyFjTO7%2BrvWNXuI4gK80RXuc%2FixU9MFjYxSDxdVPrjIJZSeh2in55ti7oGpfjK%2F9dTD7H9zt86QNYPwC5lgK18vtZMi8OCTm7Kh2nV7gpEHprYhmLbpAdJr2vzeWqbbtbRx%2FnkxNTfnxZIOzBPjjTrwCEbzcrsiC7kTwznoZdGwcs4h0yFDaRQKfTcR%2BIDO8e1qd0xSlnG7KtF0cROC8qzWbLACygX6FR5KzVhExlRdkAaCI%2B2PGkfGciaTj9LgnCSgDnXR%2BcePlszjNQPbtd7kL%2BEornDYClFBV%2FyJYjUMftxpufF3xlblRrRZxAo5w187pxs1r8HTWcqKI10dVLEasETCOLr2NgT3pYnH0CsD5xFGkt5vcB1ccPD6EUZdAixXQOMK%2Fzgb0GOqUBE8hWLYKg9jW%2FyR4G1hIEzdM0JMNhsS29brfZcQzQ8d8gbabSZKPeUYm%2BJQ4XabFmzZcmJq3RZ8MtgAFogRKvDGWIZN8tQB4dji0lUCmrOjuA5Krt7G6sOz59FTgImY4xgZ3l4wtIKDA8bojzQHxF66ycbbu0SW3XbQYZrmq0ZwRHq0t0HMwZhWe%2F0PtxfyMZrzUGHjtxLpCR4nG%2BxkxwZRx%2B2VcI&X-Amz-Signature=c832fc9400ec421d09d458d204920e8f210b910679439a4946fc79db01b20301&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXDWDH5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYv09Lmaw4Sak%2F4vGYprIP1pFXfPwCYBW9ejpnTWIuoAiEArJT4hRrdJDeUuINImmCrguF8sE%2FcrUxzPQUdD0HUnHoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGll3cXFaKTsLbM0sCrcAyulRMCLuL6uEHSiIMv2cXZUAnZM2l1aBPXkyoZk28GYBEUFt9icN91ehbMW7c4sCXqIk2fNyTVSCb%2B1N0Zu3TNv1hfME0T8vtaGqJEL6m7rTU0BXFBiZXtIkrTUSVVQzaOUwk4DmmVT6EcOvV%2FcxR5ECzSDfycApDoVl4NSDnVRhbv1iy%2FD4hfIPq%2FXXjpuPgg%2F6Do0ZJqW1ZrDXob5iGgDXHijXSAKOH%2F71KyM%2B58yL%2FsOoUPDucoKyFjTO7%2BrvWNXuI4gK80RXuc%2FixU9MFjYxSDxdVPrjIJZSeh2in55ti7oGpfjK%2F9dTD7H9zt86QNYPwC5lgK18vtZMi8OCTm7Kh2nV7gpEHprYhmLbpAdJr2vzeWqbbtbRx%2FnkxNTfnxZIOzBPjjTrwCEbzcrsiC7kTwznoZdGwcs4h0yFDaRQKfTcR%2BIDO8e1qd0xSlnG7KtF0cROC8qzWbLACygX6FR5KzVhExlRdkAaCI%2B2PGkfGciaTj9LgnCSgDnXR%2BcePlszjNQPbtd7kL%2BEornDYClFBV%2FyJYjUMftxpufF3xlblRrRZxAo5w187pxs1r8HTWcqKI10dVLEasETCOLr2NgT3pYnH0CsD5xFGkt5vcB1ccPD6EUZdAixXQOMK%2Fzgb0GOqUBE8hWLYKg9jW%2FyR4G1hIEzdM0JMNhsS29brfZcQzQ8d8gbabSZKPeUYm%2BJQ4XabFmzZcmJq3RZ8MtgAFogRKvDGWIZN8tQB4dji0lUCmrOjuA5Krt7G6sOz59FTgImY4xgZ3l4wtIKDA8bojzQHxF66ycbbu0SW3XbQYZrmq0ZwRHq0t0HMwZhWe%2F0PtxfyMZrzUGHjtxLpCR4nG%2BxkxwZRx%2B2VcI&X-Amz-Signature=ed11bb01ab9443a145548acce10e3a5c9105ebc73abc8520e71aed417f688a42&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JSFVN6Q%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLsq2L4nx7e%2BsFxyq5ijQVOGRPiDkCR2yRjPRMUBSL7AIhALeNLXoXWM0i7X4%2BxWonB5ycbOh%2Bg4lQP1jw1CiFmCSyKv8DCBEQABoMNjM3NDIzMTgzODA1IgwHhd2hWNT9p8h1v%2BIq3APRSZEhAHvZtdAt0jRyumE%2BkiaLqlojUwIhhON34F48IOBS2dAZV5gFgmqzSVwyqf6FW2QZIFKnmskrqFtr78JYOplhgy87ltAAsLm%2B2lOz2GaAMoqlvSmfvMVUIvqz%2BTf%2F3WlzKISw%2F4BWVERuLL9Lsyc%2FKGf8PhP%2BoFhh%2FX%2FUit0ARaP3W%2BZDwJ9cixXDulmSMLKiIhi3M0SsojifEVX6O5e1WwcYEaYaNL%2BCrPBll7Yewj8pNo8NLJOOSzd9KEluqv4Rpe0GvyzH2U0kiV7NL77lEH3e7YIx1fdYF0Hs2NrubtTWN6oDftAcLzQ1baoj9BEZG5mUQsx5nIRBfLcPc4P4X%2BoVx6AkHwaiw5ddE7%2Fe3qoudq%2FPPsjdhe3JWTR6DpreqTjgBiC%2Fv9GkPX6tkjmyKW%2BYoZwIJxbMHFsmnMuUmtPvKNR6pqMMm%2FfZ%2BkQRgom6PI9G6%2B557bbbbeaKaNUqUPMy6JiIzcph7rl9N62bieA%2F%2B%2BGtGVN2hE1j%2FzCJdR4y1VXUR4wgCTuyQJJTf42mO8C1dxYUO7kv3UeNi3W9bZuI7AVhH%2FUkhH0rUjiytdv5imOMX%2BjA9YyaQ%2Byf1vIfP36HH9dQ9zCSquRdHTL6ICImO4EaDZbx2DCw84G9BjqkAbqcmnHtOlrcDRgX30wNSaoe40Fg%2FZCTgJikLr%2FOz%2BJddjqP%2BxN3j7KlVdZOX%2F8GKNIBnSFORPYlNAqg2DFEI0LH6NuUUQjT48bPX2AApG7fx6fChT552zUkPHnnmzRPAqt7kwejIvXnBIQLDssMeISOAvKuDk2ogGvqP2Znonpyfpk3avqK9tHwYSEJ%2BXNba%2FAQXgzCRpiQqZOGj%2BEqRQ6SPz7O&X-Amz-Signature=369bda3165188e7d4641f916232b512e124171d63951a24fa4c8c1438a038e24&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JSFVN6Q%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLsq2L4nx7e%2BsFxyq5ijQVOGRPiDkCR2yRjPRMUBSL7AIhALeNLXoXWM0i7X4%2BxWonB5ycbOh%2Bg4lQP1jw1CiFmCSyKv8DCBEQABoMNjM3NDIzMTgzODA1IgwHhd2hWNT9p8h1v%2BIq3APRSZEhAHvZtdAt0jRyumE%2BkiaLqlojUwIhhON34F48IOBS2dAZV5gFgmqzSVwyqf6FW2QZIFKnmskrqFtr78JYOplhgy87ltAAsLm%2B2lOz2GaAMoqlvSmfvMVUIvqz%2BTf%2F3WlzKISw%2F4BWVERuLL9Lsyc%2FKGf8PhP%2BoFhh%2FX%2FUit0ARaP3W%2BZDwJ9cixXDulmSMLKiIhi3M0SsojifEVX6O5e1WwcYEaYaNL%2BCrPBll7Yewj8pNo8NLJOOSzd9KEluqv4Rpe0GvyzH2U0kiV7NL77lEH3e7YIx1fdYF0Hs2NrubtTWN6oDftAcLzQ1baoj9BEZG5mUQsx5nIRBfLcPc4P4X%2BoVx6AkHwaiw5ddE7%2Fe3qoudq%2FPPsjdhe3JWTR6DpreqTjgBiC%2Fv9GkPX6tkjmyKW%2BYoZwIJxbMHFsmnMuUmtPvKNR6pqMMm%2FfZ%2BkQRgom6PI9G6%2B557bbbbeaKaNUqUPMy6JiIzcph7rl9N62bieA%2F%2B%2BGtGVN2hE1j%2FzCJdR4y1VXUR4wgCTuyQJJTf42mO8C1dxYUO7kv3UeNi3W9bZuI7AVhH%2FUkhH0rUjiytdv5imOMX%2BjA9YyaQ%2Byf1vIfP36HH9dQ9zCSquRdHTL6ICImO4EaDZbx2DCw84G9BjqkAbqcmnHtOlrcDRgX30wNSaoe40Fg%2FZCTgJikLr%2FOz%2BJddjqP%2BxN3j7KlVdZOX%2F8GKNIBnSFORPYlNAqg2DFEI0LH6NuUUQjT48bPX2AApG7fx6fChT552zUkPHnnmzRPAqt7kwejIvXnBIQLDssMeISOAvKuDk2ogGvqP2Znonpyfpk3avqK9tHwYSEJ%2BXNba%2FAQXgzCRpiQqZOGj%2BEqRQ6SPz7O&X-Amz-Signature=df7940006584bdf3e8a385ae3f7240d89aa7f2f8fb590b5b7ee5578190f7a33e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
