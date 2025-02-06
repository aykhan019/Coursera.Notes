

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEBP6DJY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBE%2BSTZchi8h0phjLdkRg1D2akG2VdgTA%2BcCsLJqrQXcAiEA4u1B9uqS2CUZ0WF28K%2FQTBe0j%2BoRueZpA54fJFfYQ2Aq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIztBRuROeCFQProJSrcA3ejoguJQRw0BQns%2FDRo3uGcP4On2fV%2FqWsPlm919yMtXsRK3FnpnWTiLdjDkhuywL%2BTT0ITZJDfi%2FG3wrUk%2F2aVQEfvxNlrxHe5BYsjKhTwGxEfnOmxAJdFkdEfECz4sOhmM3ZAOKvZy0S0g1JCuOSmU7eK3b3Xq2YSG2kbacT5bRUMH2eNFqVyR7vBmroVVx91PSU3Hz8H2TgusXOrrQiAhk8pyq364mWl3%2BZm3fYkR2Cm%2Ba4TfI1Vkuia8MrkAE6%2F1ScDrYdGkW%2FBM2f4%2F1ZJLk5BdONEdBoeTKoTjZg0Q%2F%2Fytnn9ahr%2F%2B8mrImy8UPbiBie6xnucW7hkypKtTc0C%2BusQR%2Bni1kp0ONcVY4HVpy4sDd3c%2B2mB86p6lGluLS1tIUg6MHwdqlErKaS%2FmhYZjeiFxTBiHCuDKwMU2q4pfSrRrzl3%2Fsv%2FJkFFact0ZoYLVEHwdLDCRJePn0w2PXGO364VIPraHlCcT3rdQHWfnEKz45tA5Spwujf%2Fc1Grh30qJ1taZsVAFNpMik0Q%2FMY4Tl2v%2FEKDqnBRWhUf1bea2l1L0L2%2FDTsRzLOBBTQCT6tpTSZllA%2FRuf5inX3blQ%2Fo%2BtliWDtnD0TzSJhmuEZ1%2FeNNtp%2Bymm16N2DpMMrqj70GOqUBOtYt8kp1bw0F5ajTrR%2FG9q3%2BXAFVG5OJuJhxGpcnnNFO8vIGlnqgLYs8vqJN1kMKX2QQKKswKVjrHJIBHrHp1TndhNPlWw1l2gngSBffnoZZagaevzlPLyapyRUpk6Xuw29l%2BCtzpGKlPzHl7ZMisEBipLxQoqSb6JfQIc2vO84cLkW9bYb4ZVQMhYN0ecDlYW5V7qDf8PivKTutBU4o1ofDTIMB&X-Amz-Signature=d218834d1ac49f13e1b82d1bdcc816b32b808a056782c5dbf4850742f279aa73&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEBP6DJY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBE%2BSTZchi8h0phjLdkRg1D2akG2VdgTA%2BcCsLJqrQXcAiEA4u1B9uqS2CUZ0WF28K%2FQTBe0j%2BoRueZpA54fJFfYQ2Aq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIztBRuROeCFQProJSrcA3ejoguJQRw0BQns%2FDRo3uGcP4On2fV%2FqWsPlm919yMtXsRK3FnpnWTiLdjDkhuywL%2BTT0ITZJDfi%2FG3wrUk%2F2aVQEfvxNlrxHe5BYsjKhTwGxEfnOmxAJdFkdEfECz4sOhmM3ZAOKvZy0S0g1JCuOSmU7eK3b3Xq2YSG2kbacT5bRUMH2eNFqVyR7vBmroVVx91PSU3Hz8H2TgusXOrrQiAhk8pyq364mWl3%2BZm3fYkR2Cm%2Ba4TfI1Vkuia8MrkAE6%2F1ScDrYdGkW%2FBM2f4%2F1ZJLk5BdONEdBoeTKoTjZg0Q%2F%2Fytnn9ahr%2F%2B8mrImy8UPbiBie6xnucW7hkypKtTc0C%2BusQR%2Bni1kp0ONcVY4HVpy4sDd3c%2B2mB86p6lGluLS1tIUg6MHwdqlErKaS%2FmhYZjeiFxTBiHCuDKwMU2q4pfSrRrzl3%2Fsv%2FJkFFact0ZoYLVEHwdLDCRJePn0w2PXGO364VIPraHlCcT3rdQHWfnEKz45tA5Spwujf%2Fc1Grh30qJ1taZsVAFNpMik0Q%2FMY4Tl2v%2FEKDqnBRWhUf1bea2l1L0L2%2FDTsRzLOBBTQCT6tpTSZllA%2FRuf5inX3blQ%2Fo%2BtliWDtnD0TzSJhmuEZ1%2FeNNtp%2Bymm16N2DpMMrqj70GOqUBOtYt8kp1bw0F5ajTrR%2FG9q3%2BXAFVG5OJuJhxGpcnnNFO8vIGlnqgLYs8vqJN1kMKX2QQKKswKVjrHJIBHrHp1TndhNPlWw1l2gngSBffnoZZagaevzlPLyapyRUpk6Xuw29l%2BCtzpGKlPzHl7ZMisEBipLxQoqSb6JfQIc2vO84cLkW9bYb4ZVQMhYN0ecDlYW5V7qDf8PivKTutBU4o1ofDTIMB&X-Amz-Signature=259655caec5789458749f320cc2b6a46d9edeaa6e85d9809e25b9f4803d63c66&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEBP6DJY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBE%2BSTZchi8h0phjLdkRg1D2akG2VdgTA%2BcCsLJqrQXcAiEA4u1B9uqS2CUZ0WF28K%2FQTBe0j%2BoRueZpA54fJFfYQ2Aq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIztBRuROeCFQProJSrcA3ejoguJQRw0BQns%2FDRo3uGcP4On2fV%2FqWsPlm919yMtXsRK3FnpnWTiLdjDkhuywL%2BTT0ITZJDfi%2FG3wrUk%2F2aVQEfvxNlrxHe5BYsjKhTwGxEfnOmxAJdFkdEfECz4sOhmM3ZAOKvZy0S0g1JCuOSmU7eK3b3Xq2YSG2kbacT5bRUMH2eNFqVyR7vBmroVVx91PSU3Hz8H2TgusXOrrQiAhk8pyq364mWl3%2BZm3fYkR2Cm%2Ba4TfI1Vkuia8MrkAE6%2F1ScDrYdGkW%2FBM2f4%2F1ZJLk5BdONEdBoeTKoTjZg0Q%2F%2Fytnn9ahr%2F%2B8mrImy8UPbiBie6xnucW7hkypKtTc0C%2BusQR%2Bni1kp0ONcVY4HVpy4sDd3c%2B2mB86p6lGluLS1tIUg6MHwdqlErKaS%2FmhYZjeiFxTBiHCuDKwMU2q4pfSrRrzl3%2Fsv%2FJkFFact0ZoYLVEHwdLDCRJePn0w2PXGO364VIPraHlCcT3rdQHWfnEKz45tA5Spwujf%2Fc1Grh30qJ1taZsVAFNpMik0Q%2FMY4Tl2v%2FEKDqnBRWhUf1bea2l1L0L2%2FDTsRzLOBBTQCT6tpTSZllA%2FRuf5inX3blQ%2Fo%2BtliWDtnD0TzSJhmuEZ1%2FeNNtp%2Bymm16N2DpMMrqj70GOqUBOtYt8kp1bw0F5ajTrR%2FG9q3%2BXAFVG5OJuJhxGpcnnNFO8vIGlnqgLYs8vqJN1kMKX2QQKKswKVjrHJIBHrHp1TndhNPlWw1l2gngSBffnoZZagaevzlPLyapyRUpk6Xuw29l%2BCtzpGKlPzHl7ZMisEBipLxQoqSb6JfQIc2vO84cLkW9bYb4ZVQMhYN0ecDlYW5V7qDf8PivKTutBU4o1ofDTIMB&X-Amz-Signature=79aa9aa0c7ead49e33206ae7087053326bceed6814168e1c8b555d6e5d835d63&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEBP6DJY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBE%2BSTZchi8h0phjLdkRg1D2akG2VdgTA%2BcCsLJqrQXcAiEA4u1B9uqS2CUZ0WF28K%2FQTBe0j%2BoRueZpA54fJFfYQ2Aq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIztBRuROeCFQProJSrcA3ejoguJQRw0BQns%2FDRo3uGcP4On2fV%2FqWsPlm919yMtXsRK3FnpnWTiLdjDkhuywL%2BTT0ITZJDfi%2FG3wrUk%2F2aVQEfvxNlrxHe5BYsjKhTwGxEfnOmxAJdFkdEfECz4sOhmM3ZAOKvZy0S0g1JCuOSmU7eK3b3Xq2YSG2kbacT5bRUMH2eNFqVyR7vBmroVVx91PSU3Hz8H2TgusXOrrQiAhk8pyq364mWl3%2BZm3fYkR2Cm%2Ba4TfI1Vkuia8MrkAE6%2F1ScDrYdGkW%2FBM2f4%2F1ZJLk5BdONEdBoeTKoTjZg0Q%2F%2Fytnn9ahr%2F%2B8mrImy8UPbiBie6xnucW7hkypKtTc0C%2BusQR%2Bni1kp0ONcVY4HVpy4sDd3c%2B2mB86p6lGluLS1tIUg6MHwdqlErKaS%2FmhYZjeiFxTBiHCuDKwMU2q4pfSrRrzl3%2Fsv%2FJkFFact0ZoYLVEHwdLDCRJePn0w2PXGO364VIPraHlCcT3rdQHWfnEKz45tA5Spwujf%2Fc1Grh30qJ1taZsVAFNpMik0Q%2FMY4Tl2v%2FEKDqnBRWhUf1bea2l1L0L2%2FDTsRzLOBBTQCT6tpTSZllA%2FRuf5inX3blQ%2Fo%2BtliWDtnD0TzSJhmuEZ1%2FeNNtp%2Bymm16N2DpMMrqj70GOqUBOtYt8kp1bw0F5ajTrR%2FG9q3%2BXAFVG5OJuJhxGpcnnNFO8vIGlnqgLYs8vqJN1kMKX2QQKKswKVjrHJIBHrHp1TndhNPlWw1l2gngSBffnoZZagaevzlPLyapyRUpk6Xuw29l%2BCtzpGKlPzHl7ZMisEBipLxQoqSb6JfQIc2vO84cLkW9bYb4ZVQMhYN0ecDlYW5V7qDf8PivKTutBU4o1ofDTIMB&X-Amz-Signature=8de3f3b85b67e5cb0d682e6097017857bb6b95be96cb98d6db0c7c673ad84c47&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEBP6DJY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBE%2BSTZchi8h0phjLdkRg1D2akG2VdgTA%2BcCsLJqrQXcAiEA4u1B9uqS2CUZ0WF28K%2FQTBe0j%2BoRueZpA54fJFfYQ2Aq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIztBRuROeCFQProJSrcA3ejoguJQRw0BQns%2FDRo3uGcP4On2fV%2FqWsPlm919yMtXsRK3FnpnWTiLdjDkhuywL%2BTT0ITZJDfi%2FG3wrUk%2F2aVQEfvxNlrxHe5BYsjKhTwGxEfnOmxAJdFkdEfECz4sOhmM3ZAOKvZy0S0g1JCuOSmU7eK3b3Xq2YSG2kbacT5bRUMH2eNFqVyR7vBmroVVx91PSU3Hz8H2TgusXOrrQiAhk8pyq364mWl3%2BZm3fYkR2Cm%2Ba4TfI1Vkuia8MrkAE6%2F1ScDrYdGkW%2FBM2f4%2F1ZJLk5BdONEdBoeTKoTjZg0Q%2F%2Fytnn9ahr%2F%2B8mrImy8UPbiBie6xnucW7hkypKtTc0C%2BusQR%2Bni1kp0ONcVY4HVpy4sDd3c%2B2mB86p6lGluLS1tIUg6MHwdqlErKaS%2FmhYZjeiFxTBiHCuDKwMU2q4pfSrRrzl3%2Fsv%2FJkFFact0ZoYLVEHwdLDCRJePn0w2PXGO364VIPraHlCcT3rdQHWfnEKz45tA5Spwujf%2Fc1Grh30qJ1taZsVAFNpMik0Q%2FMY4Tl2v%2FEKDqnBRWhUf1bea2l1L0L2%2FDTsRzLOBBTQCT6tpTSZllA%2FRuf5inX3blQ%2Fo%2BtliWDtnD0TzSJhmuEZ1%2FeNNtp%2Bymm16N2DpMMrqj70GOqUBOtYt8kp1bw0F5ajTrR%2FG9q3%2BXAFVG5OJuJhxGpcnnNFO8vIGlnqgLYs8vqJN1kMKX2QQKKswKVjrHJIBHrHp1TndhNPlWw1l2gngSBffnoZZagaevzlPLyapyRUpk6Xuw29l%2BCtzpGKlPzHl7ZMisEBipLxQoqSb6JfQIc2vO84cLkW9bYb4ZVQMhYN0ecDlYW5V7qDf8PivKTutBU4o1ofDTIMB&X-Amz-Signature=18fb047d925e22baf532429b13e3612de231b2f952680d4a0e0ca0e094a1fb0b&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEBP6DJY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBE%2BSTZchi8h0phjLdkRg1D2akG2VdgTA%2BcCsLJqrQXcAiEA4u1B9uqS2CUZ0WF28K%2FQTBe0j%2BoRueZpA54fJFfYQ2Aq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIztBRuROeCFQProJSrcA3ejoguJQRw0BQns%2FDRo3uGcP4On2fV%2FqWsPlm919yMtXsRK3FnpnWTiLdjDkhuywL%2BTT0ITZJDfi%2FG3wrUk%2F2aVQEfvxNlrxHe5BYsjKhTwGxEfnOmxAJdFkdEfECz4sOhmM3ZAOKvZy0S0g1JCuOSmU7eK3b3Xq2YSG2kbacT5bRUMH2eNFqVyR7vBmroVVx91PSU3Hz8H2TgusXOrrQiAhk8pyq364mWl3%2BZm3fYkR2Cm%2Ba4TfI1Vkuia8MrkAE6%2F1ScDrYdGkW%2FBM2f4%2F1ZJLk5BdONEdBoeTKoTjZg0Q%2F%2Fytnn9ahr%2F%2B8mrImy8UPbiBie6xnucW7hkypKtTc0C%2BusQR%2Bni1kp0ONcVY4HVpy4sDd3c%2B2mB86p6lGluLS1tIUg6MHwdqlErKaS%2FmhYZjeiFxTBiHCuDKwMU2q4pfSrRrzl3%2Fsv%2FJkFFact0ZoYLVEHwdLDCRJePn0w2PXGO364VIPraHlCcT3rdQHWfnEKz45tA5Spwujf%2Fc1Grh30qJ1taZsVAFNpMik0Q%2FMY4Tl2v%2FEKDqnBRWhUf1bea2l1L0L2%2FDTsRzLOBBTQCT6tpTSZllA%2FRuf5inX3blQ%2Fo%2BtliWDtnD0TzSJhmuEZ1%2FeNNtp%2Bymm16N2DpMMrqj70GOqUBOtYt8kp1bw0F5ajTrR%2FG9q3%2BXAFVG5OJuJhxGpcnnNFO8vIGlnqgLYs8vqJN1kMKX2QQKKswKVjrHJIBHrHp1TndhNPlWw1l2gngSBffnoZZagaevzlPLyapyRUpk6Xuw29l%2BCtzpGKlPzHl7ZMisEBipLxQoqSb6JfQIc2vO84cLkW9bYb4ZVQMhYN0ecDlYW5V7qDf8PivKTutBU4o1ofDTIMB&X-Amz-Signature=a19fb24b787acfc89a39c3e2b818e82aafc928dc2eb89d758a6970cd40fa44be&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEBP6DJY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBE%2BSTZchi8h0phjLdkRg1D2akG2VdgTA%2BcCsLJqrQXcAiEA4u1B9uqS2CUZ0WF28K%2FQTBe0j%2BoRueZpA54fJFfYQ2Aq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIztBRuROeCFQProJSrcA3ejoguJQRw0BQns%2FDRo3uGcP4On2fV%2FqWsPlm919yMtXsRK3FnpnWTiLdjDkhuywL%2BTT0ITZJDfi%2FG3wrUk%2F2aVQEfvxNlrxHe5BYsjKhTwGxEfnOmxAJdFkdEfECz4sOhmM3ZAOKvZy0S0g1JCuOSmU7eK3b3Xq2YSG2kbacT5bRUMH2eNFqVyR7vBmroVVx91PSU3Hz8H2TgusXOrrQiAhk8pyq364mWl3%2BZm3fYkR2Cm%2Ba4TfI1Vkuia8MrkAE6%2F1ScDrYdGkW%2FBM2f4%2F1ZJLk5BdONEdBoeTKoTjZg0Q%2F%2Fytnn9ahr%2F%2B8mrImy8UPbiBie6xnucW7hkypKtTc0C%2BusQR%2Bni1kp0ONcVY4HVpy4sDd3c%2B2mB86p6lGluLS1tIUg6MHwdqlErKaS%2FmhYZjeiFxTBiHCuDKwMU2q4pfSrRrzl3%2Fsv%2FJkFFact0ZoYLVEHwdLDCRJePn0w2PXGO364VIPraHlCcT3rdQHWfnEKz45tA5Spwujf%2Fc1Grh30qJ1taZsVAFNpMik0Q%2FMY4Tl2v%2FEKDqnBRWhUf1bea2l1L0L2%2FDTsRzLOBBTQCT6tpTSZllA%2FRuf5inX3blQ%2Fo%2BtliWDtnD0TzSJhmuEZ1%2FeNNtp%2Bymm16N2DpMMrqj70GOqUBOtYt8kp1bw0F5ajTrR%2FG9q3%2BXAFVG5OJuJhxGpcnnNFO8vIGlnqgLYs8vqJN1kMKX2QQKKswKVjrHJIBHrHp1TndhNPlWw1l2gngSBffnoZZagaevzlPLyapyRUpk6Xuw29l%2BCtzpGKlPzHl7ZMisEBipLxQoqSb6JfQIc2vO84cLkW9bYb4ZVQMhYN0ecDlYW5V7qDf8PivKTutBU4o1ofDTIMB&X-Amz-Signature=22066d5330af87b36974c4591acb66e1f314325bad53218ef0b2708ac84d652e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEBP6DJY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBE%2BSTZchi8h0phjLdkRg1D2akG2VdgTA%2BcCsLJqrQXcAiEA4u1B9uqS2CUZ0WF28K%2FQTBe0j%2BoRueZpA54fJFfYQ2Aq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIztBRuROeCFQProJSrcA3ejoguJQRw0BQns%2FDRo3uGcP4On2fV%2FqWsPlm919yMtXsRK3FnpnWTiLdjDkhuywL%2BTT0ITZJDfi%2FG3wrUk%2F2aVQEfvxNlrxHe5BYsjKhTwGxEfnOmxAJdFkdEfECz4sOhmM3ZAOKvZy0S0g1JCuOSmU7eK3b3Xq2YSG2kbacT5bRUMH2eNFqVyR7vBmroVVx91PSU3Hz8H2TgusXOrrQiAhk8pyq364mWl3%2BZm3fYkR2Cm%2Ba4TfI1Vkuia8MrkAE6%2F1ScDrYdGkW%2FBM2f4%2F1ZJLk5BdONEdBoeTKoTjZg0Q%2F%2Fytnn9ahr%2F%2B8mrImy8UPbiBie6xnucW7hkypKtTc0C%2BusQR%2Bni1kp0ONcVY4HVpy4sDd3c%2B2mB86p6lGluLS1tIUg6MHwdqlErKaS%2FmhYZjeiFxTBiHCuDKwMU2q4pfSrRrzl3%2Fsv%2FJkFFact0ZoYLVEHwdLDCRJePn0w2PXGO364VIPraHlCcT3rdQHWfnEKz45tA5Spwujf%2Fc1Grh30qJ1taZsVAFNpMik0Q%2FMY4Tl2v%2FEKDqnBRWhUf1bea2l1L0L2%2FDTsRzLOBBTQCT6tpTSZllA%2FRuf5inX3blQ%2Fo%2BtliWDtnD0TzSJhmuEZ1%2FeNNtp%2Bymm16N2DpMMrqj70GOqUBOtYt8kp1bw0F5ajTrR%2FG9q3%2BXAFVG5OJuJhxGpcnnNFO8vIGlnqgLYs8vqJN1kMKX2QQKKswKVjrHJIBHrHp1TndhNPlWw1l2gngSBffnoZZagaevzlPLyapyRUpk6Xuw29l%2BCtzpGKlPzHl7ZMisEBipLxQoqSb6JfQIc2vO84cLkW9bYb4ZVQMhYN0ecDlYW5V7qDf8PivKTutBU4o1ofDTIMB&X-Amz-Signature=891ffa86be871d49b7b39f06f454a8e79e321b9ca1fd189a050e679c99f400bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEBP6DJY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBE%2BSTZchi8h0phjLdkRg1D2akG2VdgTA%2BcCsLJqrQXcAiEA4u1B9uqS2CUZ0WF28K%2FQTBe0j%2BoRueZpA54fJFfYQ2Aq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIztBRuROeCFQProJSrcA3ejoguJQRw0BQns%2FDRo3uGcP4On2fV%2FqWsPlm919yMtXsRK3FnpnWTiLdjDkhuywL%2BTT0ITZJDfi%2FG3wrUk%2F2aVQEfvxNlrxHe5BYsjKhTwGxEfnOmxAJdFkdEfECz4sOhmM3ZAOKvZy0S0g1JCuOSmU7eK3b3Xq2YSG2kbacT5bRUMH2eNFqVyR7vBmroVVx91PSU3Hz8H2TgusXOrrQiAhk8pyq364mWl3%2BZm3fYkR2Cm%2Ba4TfI1Vkuia8MrkAE6%2F1ScDrYdGkW%2FBM2f4%2F1ZJLk5BdONEdBoeTKoTjZg0Q%2F%2Fytnn9ahr%2F%2B8mrImy8UPbiBie6xnucW7hkypKtTc0C%2BusQR%2Bni1kp0ONcVY4HVpy4sDd3c%2B2mB86p6lGluLS1tIUg6MHwdqlErKaS%2FmhYZjeiFxTBiHCuDKwMU2q4pfSrRrzl3%2Fsv%2FJkFFact0ZoYLVEHwdLDCRJePn0w2PXGO364VIPraHlCcT3rdQHWfnEKz45tA5Spwujf%2Fc1Grh30qJ1taZsVAFNpMik0Q%2FMY4Tl2v%2FEKDqnBRWhUf1bea2l1L0L2%2FDTsRzLOBBTQCT6tpTSZllA%2FRuf5inX3blQ%2Fo%2BtliWDtnD0TzSJhmuEZ1%2FeNNtp%2Bymm16N2DpMMrqj70GOqUBOtYt8kp1bw0F5ajTrR%2FG9q3%2BXAFVG5OJuJhxGpcnnNFO8vIGlnqgLYs8vqJN1kMKX2QQKKswKVjrHJIBHrHp1TndhNPlWw1l2gngSBffnoZZagaevzlPLyapyRUpk6Xuw29l%2BCtzpGKlPzHl7ZMisEBipLxQoqSb6JfQIc2vO84cLkW9bYb4ZVQMhYN0ecDlYW5V7qDf8PivKTutBU4o1ofDTIMB&X-Amz-Signature=b9333c61590b330e9fd54f0f9a0c0f46aa7d335a350fdc3c2be51e9afd63aa20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWNE7NBX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCnQbnFfAXZFTgTHnjSU6POI35X%2FokRrcJDO1S6Ag3NZwIhAKHJrbRMikCc0h7krTGEQGhfok2mNL1xgIaYUuqSvPr%2FKv8DCFEQABoMNjM3NDIzMTgzODA1IgztMxGuuYYRVTJj9Esq3APQ%2FZdsNn%2FxMeRrWgR3iRpCiYRleuTQDrpAIWT2rKy0CzpifdVEcSL0%2FPh1VFZ7ITsZ52G9cTMbhemHPjHupsKR7X4h0lrYHeoyP0LyMp%2Bqg9TS6tbCQ6gBzXr5Q%2FfIzpo9oT9Ld8EfmcEsbNaDgDZ%2F%2FrYw%2F2MX540kEpAvMgRWIVI73EyvpqR7QdwsqleukEy8LPKxJPfuHbwPc65Edcxtu4MeXf67Y89fsSSsCXRDi7J4OHezss0YcWc6by29sC9%2BAyNOQFwI1AUWl0LTI%2Bj5dgG%2Bmm4Hm%2Fqp4Fnr2MxfuivLGhuLS9FJNG3E%2FbWiwifHIKLhvsPlwg%2FnjnRcEUwcet4%2BC4IvruKClKF4ikM3SU3aGHEZBrEBDEUyNqPjC%2FEOQPQR65iOrV4GQp0HOF%2BGeadJ5Z%2Fl3QIF%2FrOlxYQUBnB9G2c5cPX1baX3w%2BQX8QWSf83N%2Bdi8ewIPpzIyU3Jkv1ipjhdCSetn9bC9B2koB0SiT37p17WHlCLk%2BmqJh%2BpReepswn1AcZ%2FAz0j1uAg6jK3DkaJJjd5MY5iz9%2BnkuY8eTotkAnK8IuL2oaU23Z7wgl8RFiznphxjs8Ujx2kYJZUMVGH0WUxpjpUAnQKDv%2FJlG4OpA6f60nP4zzCU64%2B9BjqkAfFaT3tWnq9%2BYzM5K3zP0akmsoUSS%2Fe5u82dx%2FVs6gWm3o%2FVPsNAs162itSl6x4PZy35EptUHFJp%2FLqf8sIbGm5a524h5GKCdrwz7GHBEFjdmzLX8izG06lnPrOshc1Kj%2FOgpq9DrHcU1%2FZbDpePXefrO8HNQQ50FmoSP8Mxvi2jGYUVW5zrAtt%2BZqgVkzqcxWTZiIICf9Yfoc60DXBYGrLcZoOt&X-Amz-Signature=645360e3e5f2604bdb5244a7195424af992b12f449841ac59432edb5acb0ee73&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWNE7NBX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCnQbnFfAXZFTgTHnjSU6POI35X%2FokRrcJDO1S6Ag3NZwIhAKHJrbRMikCc0h7krTGEQGhfok2mNL1xgIaYUuqSvPr%2FKv8DCFEQABoMNjM3NDIzMTgzODA1IgztMxGuuYYRVTJj9Esq3APQ%2FZdsNn%2FxMeRrWgR3iRpCiYRleuTQDrpAIWT2rKy0CzpifdVEcSL0%2FPh1VFZ7ITsZ52G9cTMbhemHPjHupsKR7X4h0lrYHeoyP0LyMp%2Bqg9TS6tbCQ6gBzXr5Q%2FfIzpo9oT9Ld8EfmcEsbNaDgDZ%2F%2FrYw%2F2MX540kEpAvMgRWIVI73EyvpqR7QdwsqleukEy8LPKxJPfuHbwPc65Edcxtu4MeXf67Y89fsSSsCXRDi7J4OHezss0YcWc6by29sC9%2BAyNOQFwI1AUWl0LTI%2Bj5dgG%2Bmm4Hm%2Fqp4Fnr2MxfuivLGhuLS9FJNG3E%2FbWiwifHIKLhvsPlwg%2FnjnRcEUwcet4%2BC4IvruKClKF4ikM3SU3aGHEZBrEBDEUyNqPjC%2FEOQPQR65iOrV4GQp0HOF%2BGeadJ5Z%2Fl3QIF%2FrOlxYQUBnB9G2c5cPX1baX3w%2BQX8QWSf83N%2Bdi8ewIPpzIyU3Jkv1ipjhdCSetn9bC9B2koB0SiT37p17WHlCLk%2BmqJh%2BpReepswn1AcZ%2FAz0j1uAg6jK3DkaJJjd5MY5iz9%2BnkuY8eTotkAnK8IuL2oaU23Z7wgl8RFiznphxjs8Ujx2kYJZUMVGH0WUxpjpUAnQKDv%2FJlG4OpA6f60nP4zzCU64%2B9BjqkAfFaT3tWnq9%2BYzM5K3zP0akmsoUSS%2Fe5u82dx%2FVs6gWm3o%2FVPsNAs162itSl6x4PZy35EptUHFJp%2FLqf8sIbGm5a524h5GKCdrwz7GHBEFjdmzLX8izG06lnPrOshc1Kj%2FOgpq9DrHcU1%2FZbDpePXefrO8HNQQ50FmoSP8Mxvi2jGYUVW5zrAtt%2BZqgVkzqcxWTZiIICf9Yfoc60DXBYGrLcZoOt&X-Amz-Signature=24d8650dea4f3808aded1f256f0a671b24abd2f6f6f21f946ad60093e734cd99&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
