

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664INEDOHV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIFEP5EXJGNyEH4Wq7AF0Mz8x%2F0PSPaFmJE75C7hWqhROAiEAu3Uun%2BuLmrBg7BTuJONor%2FClOLqVsNu4z6IoqRCby8Aq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDGbYZLuSMtDCjUd5lCrcA%2BWxERNZ%2B87cD5DXu7Dl41BvtYVCsY%2ByLPtyRakKE48a1hnCmm3ptzFx0icxFRaMXZs%2B3d6jI1J%2BdoaBsKiJ8KhDiwUeQnbACoM2fF9s7bKJ%2FD9NnKrFtr95Tko7ZooWYskjf9X0jlBDV8m17k3wvaECsBph05afBuIpGkfe6dtZvPklr5PAUjIfbOBe3kG5fbNxL4QE9sAfBHFyog1X9Nn9eu%2BMVjLMKRFRnQDUgJO6QEylK%2F5baSg3QccChsIUhOb4gr73AlIMBhF6vTzEmxcLWzp1gae6dAoj9Y%2FXYWSpmYbloMasy2Tf1zptB4D2EBxSrcVJ0tufbdccQnIADRLaYoLPX5wOxDzTHDHn%2BIM9eiAN3ebZEsWmQws7c%2BXrZTS0PyjLmcbPT5zSMq4CTluErSAqnrqga0g3ya2O01zD8S44mDi5h2CS%2FAfdt%2F8ihFMfUkjaz9v9fBueLB73wwgbLXqMpYWtGg6fqnP3NGQbefE5b4m2tDKp4qw8yl%2FqLyx4fHCb7TVB92UNsxsf2TTozXxydURW3frw0BYj5iHiD5PtUAiUB7IFcAl40%2FJaBe40gwRlqdOksdNb%2B%2B8SvhhDUA2EraWDF8a%2FBqOcnUzllYT4ihVXsIZiBPdiMNuUir0GOqUBkUwU8il2%2BTcBz3g7y9cEuSNAhHNbUKUPwDxhcs2TFeP%2BFUoJ9jW6mxK1al%2BnDjI8%2FAvlpnpZ6U%2Fw5i78Sd5d7GZdR2eDjzlxI85NhCVlQVElxFnlUs70U7mLIvPgb2%2BID9v8PTuTZfUW%2Fm7YiitnwZMenr2NGOLGOl4p4cD4esdfzalrGxFEmkdiQlEEgB1MZGLi3LgOhN4N%2FdUmkhvoSPZovT6d&X-Amz-Signature=aefe1a6be1e99458f725ee3ab3600daaba75f025d79a42c78adf11ffe1bdcb76&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664INEDOHV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIFEP5EXJGNyEH4Wq7AF0Mz8x%2F0PSPaFmJE75C7hWqhROAiEAu3Uun%2BuLmrBg7BTuJONor%2FClOLqVsNu4z6IoqRCby8Aq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDGbYZLuSMtDCjUd5lCrcA%2BWxERNZ%2B87cD5DXu7Dl41BvtYVCsY%2ByLPtyRakKE48a1hnCmm3ptzFx0icxFRaMXZs%2B3d6jI1J%2BdoaBsKiJ8KhDiwUeQnbACoM2fF9s7bKJ%2FD9NnKrFtr95Tko7ZooWYskjf9X0jlBDV8m17k3wvaECsBph05afBuIpGkfe6dtZvPklr5PAUjIfbOBe3kG5fbNxL4QE9sAfBHFyog1X9Nn9eu%2BMVjLMKRFRnQDUgJO6QEylK%2F5baSg3QccChsIUhOb4gr73AlIMBhF6vTzEmxcLWzp1gae6dAoj9Y%2FXYWSpmYbloMasy2Tf1zptB4D2EBxSrcVJ0tufbdccQnIADRLaYoLPX5wOxDzTHDHn%2BIM9eiAN3ebZEsWmQws7c%2BXrZTS0PyjLmcbPT5zSMq4CTluErSAqnrqga0g3ya2O01zD8S44mDi5h2CS%2FAfdt%2F8ihFMfUkjaz9v9fBueLB73wwgbLXqMpYWtGg6fqnP3NGQbefE5b4m2tDKp4qw8yl%2FqLyx4fHCb7TVB92UNsxsf2TTozXxydURW3frw0BYj5iHiD5PtUAiUB7IFcAl40%2FJaBe40gwRlqdOksdNb%2B%2B8SvhhDUA2EraWDF8a%2FBqOcnUzllYT4ihVXsIZiBPdiMNuUir0GOqUBkUwU8il2%2BTcBz3g7y9cEuSNAhHNbUKUPwDxhcs2TFeP%2BFUoJ9jW6mxK1al%2BnDjI8%2FAvlpnpZ6U%2Fw5i78Sd5d7GZdR2eDjzlxI85NhCVlQVElxFnlUs70U7mLIvPgb2%2BID9v8PTuTZfUW%2Fm7YiitnwZMenr2NGOLGOl4p4cD4esdfzalrGxFEmkdiQlEEgB1MZGLi3LgOhN4N%2FdUmkhvoSPZovT6d&X-Amz-Signature=d22092f4dfe8c6f6c4a73a405ea96aa729d6a9ead541944f2a543f00d0896d68&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664INEDOHV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIFEP5EXJGNyEH4Wq7AF0Mz8x%2F0PSPaFmJE75C7hWqhROAiEAu3Uun%2BuLmrBg7BTuJONor%2FClOLqVsNu4z6IoqRCby8Aq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDGbYZLuSMtDCjUd5lCrcA%2BWxERNZ%2B87cD5DXu7Dl41BvtYVCsY%2ByLPtyRakKE48a1hnCmm3ptzFx0icxFRaMXZs%2B3d6jI1J%2BdoaBsKiJ8KhDiwUeQnbACoM2fF9s7bKJ%2FD9NnKrFtr95Tko7ZooWYskjf9X0jlBDV8m17k3wvaECsBph05afBuIpGkfe6dtZvPklr5PAUjIfbOBe3kG5fbNxL4QE9sAfBHFyog1X9Nn9eu%2BMVjLMKRFRnQDUgJO6QEylK%2F5baSg3QccChsIUhOb4gr73AlIMBhF6vTzEmxcLWzp1gae6dAoj9Y%2FXYWSpmYbloMasy2Tf1zptB4D2EBxSrcVJ0tufbdccQnIADRLaYoLPX5wOxDzTHDHn%2BIM9eiAN3ebZEsWmQws7c%2BXrZTS0PyjLmcbPT5zSMq4CTluErSAqnrqga0g3ya2O01zD8S44mDi5h2CS%2FAfdt%2F8ihFMfUkjaz9v9fBueLB73wwgbLXqMpYWtGg6fqnP3NGQbefE5b4m2tDKp4qw8yl%2FqLyx4fHCb7TVB92UNsxsf2TTozXxydURW3frw0BYj5iHiD5PtUAiUB7IFcAl40%2FJaBe40gwRlqdOksdNb%2B%2B8SvhhDUA2EraWDF8a%2FBqOcnUzllYT4ihVXsIZiBPdiMNuUir0GOqUBkUwU8il2%2BTcBz3g7y9cEuSNAhHNbUKUPwDxhcs2TFeP%2BFUoJ9jW6mxK1al%2BnDjI8%2FAvlpnpZ6U%2Fw5i78Sd5d7GZdR2eDjzlxI85NhCVlQVElxFnlUs70U7mLIvPgb2%2BID9v8PTuTZfUW%2Fm7YiitnwZMenr2NGOLGOl4p4cD4esdfzalrGxFEmkdiQlEEgB1MZGLi3LgOhN4N%2FdUmkhvoSPZovT6d&X-Amz-Signature=5f62d0f4769a5b962eb3e0cbafefc439e22718def186e470d0660999a6749dcf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664INEDOHV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIFEP5EXJGNyEH4Wq7AF0Mz8x%2F0PSPaFmJE75C7hWqhROAiEAu3Uun%2BuLmrBg7BTuJONor%2FClOLqVsNu4z6IoqRCby8Aq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDGbYZLuSMtDCjUd5lCrcA%2BWxERNZ%2B87cD5DXu7Dl41BvtYVCsY%2ByLPtyRakKE48a1hnCmm3ptzFx0icxFRaMXZs%2B3d6jI1J%2BdoaBsKiJ8KhDiwUeQnbACoM2fF9s7bKJ%2FD9NnKrFtr95Tko7ZooWYskjf9X0jlBDV8m17k3wvaECsBph05afBuIpGkfe6dtZvPklr5PAUjIfbOBe3kG5fbNxL4QE9sAfBHFyog1X9Nn9eu%2BMVjLMKRFRnQDUgJO6QEylK%2F5baSg3QccChsIUhOb4gr73AlIMBhF6vTzEmxcLWzp1gae6dAoj9Y%2FXYWSpmYbloMasy2Tf1zptB4D2EBxSrcVJ0tufbdccQnIADRLaYoLPX5wOxDzTHDHn%2BIM9eiAN3ebZEsWmQws7c%2BXrZTS0PyjLmcbPT5zSMq4CTluErSAqnrqga0g3ya2O01zD8S44mDi5h2CS%2FAfdt%2F8ihFMfUkjaz9v9fBueLB73wwgbLXqMpYWtGg6fqnP3NGQbefE5b4m2tDKp4qw8yl%2FqLyx4fHCb7TVB92UNsxsf2TTozXxydURW3frw0BYj5iHiD5PtUAiUB7IFcAl40%2FJaBe40gwRlqdOksdNb%2B%2B8SvhhDUA2EraWDF8a%2FBqOcnUzllYT4ihVXsIZiBPdiMNuUir0GOqUBkUwU8il2%2BTcBz3g7y9cEuSNAhHNbUKUPwDxhcs2TFeP%2BFUoJ9jW6mxK1al%2BnDjI8%2FAvlpnpZ6U%2Fw5i78Sd5d7GZdR2eDjzlxI85NhCVlQVElxFnlUs70U7mLIvPgb2%2BID9v8PTuTZfUW%2Fm7YiitnwZMenr2NGOLGOl4p4cD4esdfzalrGxFEmkdiQlEEgB1MZGLi3LgOhN4N%2FdUmkhvoSPZovT6d&X-Amz-Signature=315ca72e6a58344cfb411cfac19a9eb38ba44a86df3743ee962c951fdfb705f4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664INEDOHV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIFEP5EXJGNyEH4Wq7AF0Mz8x%2F0PSPaFmJE75C7hWqhROAiEAu3Uun%2BuLmrBg7BTuJONor%2FClOLqVsNu4z6IoqRCby8Aq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDGbYZLuSMtDCjUd5lCrcA%2BWxERNZ%2B87cD5DXu7Dl41BvtYVCsY%2ByLPtyRakKE48a1hnCmm3ptzFx0icxFRaMXZs%2B3d6jI1J%2BdoaBsKiJ8KhDiwUeQnbACoM2fF9s7bKJ%2FD9NnKrFtr95Tko7ZooWYskjf9X0jlBDV8m17k3wvaECsBph05afBuIpGkfe6dtZvPklr5PAUjIfbOBe3kG5fbNxL4QE9sAfBHFyog1X9Nn9eu%2BMVjLMKRFRnQDUgJO6QEylK%2F5baSg3QccChsIUhOb4gr73AlIMBhF6vTzEmxcLWzp1gae6dAoj9Y%2FXYWSpmYbloMasy2Tf1zptB4D2EBxSrcVJ0tufbdccQnIADRLaYoLPX5wOxDzTHDHn%2BIM9eiAN3ebZEsWmQws7c%2BXrZTS0PyjLmcbPT5zSMq4CTluErSAqnrqga0g3ya2O01zD8S44mDi5h2CS%2FAfdt%2F8ihFMfUkjaz9v9fBueLB73wwgbLXqMpYWtGg6fqnP3NGQbefE5b4m2tDKp4qw8yl%2FqLyx4fHCb7TVB92UNsxsf2TTozXxydURW3frw0BYj5iHiD5PtUAiUB7IFcAl40%2FJaBe40gwRlqdOksdNb%2B%2B8SvhhDUA2EraWDF8a%2FBqOcnUzllYT4ihVXsIZiBPdiMNuUir0GOqUBkUwU8il2%2BTcBz3g7y9cEuSNAhHNbUKUPwDxhcs2TFeP%2BFUoJ9jW6mxK1al%2BnDjI8%2FAvlpnpZ6U%2Fw5i78Sd5d7GZdR2eDjzlxI85NhCVlQVElxFnlUs70U7mLIvPgb2%2BID9v8PTuTZfUW%2Fm7YiitnwZMenr2NGOLGOl4p4cD4esdfzalrGxFEmkdiQlEEgB1MZGLi3LgOhN4N%2FdUmkhvoSPZovT6d&X-Amz-Signature=a977686287309301894ff4b65a325a3f5216376d0bc1aa729bf956670c0208fb&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664INEDOHV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIFEP5EXJGNyEH4Wq7AF0Mz8x%2F0PSPaFmJE75C7hWqhROAiEAu3Uun%2BuLmrBg7BTuJONor%2FClOLqVsNu4z6IoqRCby8Aq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDGbYZLuSMtDCjUd5lCrcA%2BWxERNZ%2B87cD5DXu7Dl41BvtYVCsY%2ByLPtyRakKE48a1hnCmm3ptzFx0icxFRaMXZs%2B3d6jI1J%2BdoaBsKiJ8KhDiwUeQnbACoM2fF9s7bKJ%2FD9NnKrFtr95Tko7ZooWYskjf9X0jlBDV8m17k3wvaECsBph05afBuIpGkfe6dtZvPklr5PAUjIfbOBe3kG5fbNxL4QE9sAfBHFyog1X9Nn9eu%2BMVjLMKRFRnQDUgJO6QEylK%2F5baSg3QccChsIUhOb4gr73AlIMBhF6vTzEmxcLWzp1gae6dAoj9Y%2FXYWSpmYbloMasy2Tf1zptB4D2EBxSrcVJ0tufbdccQnIADRLaYoLPX5wOxDzTHDHn%2BIM9eiAN3ebZEsWmQws7c%2BXrZTS0PyjLmcbPT5zSMq4CTluErSAqnrqga0g3ya2O01zD8S44mDi5h2CS%2FAfdt%2F8ihFMfUkjaz9v9fBueLB73wwgbLXqMpYWtGg6fqnP3NGQbefE5b4m2tDKp4qw8yl%2FqLyx4fHCb7TVB92UNsxsf2TTozXxydURW3frw0BYj5iHiD5PtUAiUB7IFcAl40%2FJaBe40gwRlqdOksdNb%2B%2B8SvhhDUA2EraWDF8a%2FBqOcnUzllYT4ihVXsIZiBPdiMNuUir0GOqUBkUwU8il2%2BTcBz3g7y9cEuSNAhHNbUKUPwDxhcs2TFeP%2BFUoJ9jW6mxK1al%2BnDjI8%2FAvlpnpZ6U%2Fw5i78Sd5d7GZdR2eDjzlxI85NhCVlQVElxFnlUs70U7mLIvPgb2%2BID9v8PTuTZfUW%2Fm7YiitnwZMenr2NGOLGOl4p4cD4esdfzalrGxFEmkdiQlEEgB1MZGLi3LgOhN4N%2FdUmkhvoSPZovT6d&X-Amz-Signature=cad040b8e286b018ec8da68724312631d1f1b141fa4f4e6ff0c85d60d3f6effe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664INEDOHV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIFEP5EXJGNyEH4Wq7AF0Mz8x%2F0PSPaFmJE75C7hWqhROAiEAu3Uun%2BuLmrBg7BTuJONor%2FClOLqVsNu4z6IoqRCby8Aq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDGbYZLuSMtDCjUd5lCrcA%2BWxERNZ%2B87cD5DXu7Dl41BvtYVCsY%2ByLPtyRakKE48a1hnCmm3ptzFx0icxFRaMXZs%2B3d6jI1J%2BdoaBsKiJ8KhDiwUeQnbACoM2fF9s7bKJ%2FD9NnKrFtr95Tko7ZooWYskjf9X0jlBDV8m17k3wvaECsBph05afBuIpGkfe6dtZvPklr5PAUjIfbOBe3kG5fbNxL4QE9sAfBHFyog1X9Nn9eu%2BMVjLMKRFRnQDUgJO6QEylK%2F5baSg3QccChsIUhOb4gr73AlIMBhF6vTzEmxcLWzp1gae6dAoj9Y%2FXYWSpmYbloMasy2Tf1zptB4D2EBxSrcVJ0tufbdccQnIADRLaYoLPX5wOxDzTHDHn%2BIM9eiAN3ebZEsWmQws7c%2BXrZTS0PyjLmcbPT5zSMq4CTluErSAqnrqga0g3ya2O01zD8S44mDi5h2CS%2FAfdt%2F8ihFMfUkjaz9v9fBueLB73wwgbLXqMpYWtGg6fqnP3NGQbefE5b4m2tDKp4qw8yl%2FqLyx4fHCb7TVB92UNsxsf2TTozXxydURW3frw0BYj5iHiD5PtUAiUB7IFcAl40%2FJaBe40gwRlqdOksdNb%2B%2B8SvhhDUA2EraWDF8a%2FBqOcnUzllYT4ihVXsIZiBPdiMNuUir0GOqUBkUwU8il2%2BTcBz3g7y9cEuSNAhHNbUKUPwDxhcs2TFeP%2BFUoJ9jW6mxK1al%2BnDjI8%2FAvlpnpZ6U%2Fw5i78Sd5d7GZdR2eDjzlxI85NhCVlQVElxFnlUs70U7mLIvPgb2%2BID9v8PTuTZfUW%2Fm7YiitnwZMenr2NGOLGOl4p4cD4esdfzalrGxFEmkdiQlEEgB1MZGLi3LgOhN4N%2FdUmkhvoSPZovT6d&X-Amz-Signature=9eb7b33e545ae0b77d3b1f489db769da12d5713f927d53adc3006bdf2346bccd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664INEDOHV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIFEP5EXJGNyEH4Wq7AF0Mz8x%2F0PSPaFmJE75C7hWqhROAiEAu3Uun%2BuLmrBg7BTuJONor%2FClOLqVsNu4z6IoqRCby8Aq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDGbYZLuSMtDCjUd5lCrcA%2BWxERNZ%2B87cD5DXu7Dl41BvtYVCsY%2ByLPtyRakKE48a1hnCmm3ptzFx0icxFRaMXZs%2B3d6jI1J%2BdoaBsKiJ8KhDiwUeQnbACoM2fF9s7bKJ%2FD9NnKrFtr95Tko7ZooWYskjf9X0jlBDV8m17k3wvaECsBph05afBuIpGkfe6dtZvPklr5PAUjIfbOBe3kG5fbNxL4QE9sAfBHFyog1X9Nn9eu%2BMVjLMKRFRnQDUgJO6QEylK%2F5baSg3QccChsIUhOb4gr73AlIMBhF6vTzEmxcLWzp1gae6dAoj9Y%2FXYWSpmYbloMasy2Tf1zptB4D2EBxSrcVJ0tufbdccQnIADRLaYoLPX5wOxDzTHDHn%2BIM9eiAN3ebZEsWmQws7c%2BXrZTS0PyjLmcbPT5zSMq4CTluErSAqnrqga0g3ya2O01zD8S44mDi5h2CS%2FAfdt%2F8ihFMfUkjaz9v9fBueLB73wwgbLXqMpYWtGg6fqnP3NGQbefE5b4m2tDKp4qw8yl%2FqLyx4fHCb7TVB92UNsxsf2TTozXxydURW3frw0BYj5iHiD5PtUAiUB7IFcAl40%2FJaBe40gwRlqdOksdNb%2B%2B8SvhhDUA2EraWDF8a%2FBqOcnUzllYT4ihVXsIZiBPdiMNuUir0GOqUBkUwU8il2%2BTcBz3g7y9cEuSNAhHNbUKUPwDxhcs2TFeP%2BFUoJ9jW6mxK1al%2BnDjI8%2FAvlpnpZ6U%2Fw5i78Sd5d7GZdR2eDjzlxI85NhCVlQVElxFnlUs70U7mLIvPgb2%2BID9v8PTuTZfUW%2Fm7YiitnwZMenr2NGOLGOl4p4cD4esdfzalrGxFEmkdiQlEEgB1MZGLi3LgOhN4N%2FdUmkhvoSPZovT6d&X-Amz-Signature=87c6ff1ba38b0d5d3e20153a44041bd6f52a4a0485c3e87e18c2e4b131533719&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664INEDOHV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIFEP5EXJGNyEH4Wq7AF0Mz8x%2F0PSPaFmJE75C7hWqhROAiEAu3Uun%2BuLmrBg7BTuJONor%2FClOLqVsNu4z6IoqRCby8Aq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDGbYZLuSMtDCjUd5lCrcA%2BWxERNZ%2B87cD5DXu7Dl41BvtYVCsY%2ByLPtyRakKE48a1hnCmm3ptzFx0icxFRaMXZs%2B3d6jI1J%2BdoaBsKiJ8KhDiwUeQnbACoM2fF9s7bKJ%2FD9NnKrFtr95Tko7ZooWYskjf9X0jlBDV8m17k3wvaECsBph05afBuIpGkfe6dtZvPklr5PAUjIfbOBe3kG5fbNxL4QE9sAfBHFyog1X9Nn9eu%2BMVjLMKRFRnQDUgJO6QEylK%2F5baSg3QccChsIUhOb4gr73AlIMBhF6vTzEmxcLWzp1gae6dAoj9Y%2FXYWSpmYbloMasy2Tf1zptB4D2EBxSrcVJ0tufbdccQnIADRLaYoLPX5wOxDzTHDHn%2BIM9eiAN3ebZEsWmQws7c%2BXrZTS0PyjLmcbPT5zSMq4CTluErSAqnrqga0g3ya2O01zD8S44mDi5h2CS%2FAfdt%2F8ihFMfUkjaz9v9fBueLB73wwgbLXqMpYWtGg6fqnP3NGQbefE5b4m2tDKp4qw8yl%2FqLyx4fHCb7TVB92UNsxsf2TTozXxydURW3frw0BYj5iHiD5PtUAiUB7IFcAl40%2FJaBe40gwRlqdOksdNb%2B%2B8SvhhDUA2EraWDF8a%2FBqOcnUzllYT4ihVXsIZiBPdiMNuUir0GOqUBkUwU8il2%2BTcBz3g7y9cEuSNAhHNbUKUPwDxhcs2TFeP%2BFUoJ9jW6mxK1al%2BnDjI8%2FAvlpnpZ6U%2Fw5i78Sd5d7GZdR2eDjzlxI85NhCVlQVElxFnlUs70U7mLIvPgb2%2BID9v8PTuTZfUW%2Fm7YiitnwZMenr2NGOLGOl4p4cD4esdfzalrGxFEmkdiQlEEgB1MZGLi3LgOhN4N%2FdUmkhvoSPZovT6d&X-Amz-Signature=712b8c6363eaceb9048af960a3da2f09bc77ad4a901bfa7f18e1e3a7ced21e05&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJ3O27UA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDV0G3eCttVQXKBjK0wQOXjgdkkC1ZTUGP58ieB79pfOAiBJ%2Bk0tyOD2WwXqP%2BP6y%2FxExsDemsTzY7vBMnLX3sKQdCr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMQTlVRwBVHMkc9zXbKtwDXo5CqpSaPL%2BYc0nIKdu5arw4zlX0d0XPJIXKQR9YH3Dm4z4OGKe%2FKRWavTBFMoXaBUG3K2BWcw3ApFUjVA%2B0dmXoQwFFF8un6OBD%2FrPB7iJfl8TSASaetrEfV%2FmKg6mncnJfIBOqgItWNfXM4mjMCOmfXP4iQP9FNy8EJMXrF%2B0xAkSk1PDXOZZSV9Fh3NdHchrVUyr7QSEPmi5SBgR5q2xfW1sECcyYEBX6hX%2BrChLdnIo45anvDvcUBnvPiz0Glx%2F1ueyzGhUGyIRXkiK580cszWQc%2BU%2FtPecZEYfLU7B8Y%2FOvluKlkpG0B%2Bwf8kjMrPAuKyHMPcgGj5G0XftOP4b3opXi7B%2BhRdYXP2HlIIZrBHrjDjNoOnZNL%2B49z5lM0od9BZHGodNSmUP2PNOaOwPGek4JJenBRr%2FcWK7Yx05K%2FpM3HmfBrOyBlVYViy05apHDzq4FlzH78gA%2Bea9az4T4SjiMWXGFVvpLE4HcHYfLAL648Yj1B9x26iVlLgdfMiF%2BM1JPcK%2F9jFyS%2FvIHYLvWNwVYyy47G%2FqQJgyWV%2B9RcQgldPBZfRCxw33rlVyQimBPAAyOhoW3oCEz3g7Oj1qHUFLydwCVEaX6kYZBkx674YPVAVTFjuYIKFAwlZSKvQY6pgEwnRzEwoZ8qYUaA2EtOfuu7tBbs%2FuCipiewC1iQ1pxBZJTtdAlrDyeRlDmqBXC8lHqNa7TvQ7sazgO9jp2wz7%2F0q5y92Uv5MMztohv7zMnRTleoScFPNra6frFG%2BcTyr9WJYIkMxsbsmuHTKA1Zm9STzzkp02i2yNrfAgnP4abx4xwTjCqhp2UdOdgNF%2BweTO9tP6rFZ7cvsOkCji1EAOT9GwLDw8I&X-Amz-Signature=390c4b7a14e1157cdfb102805e4f4b4b103bb8558164c15b3325e0cf11c0cf44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJ3O27UA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDV0G3eCttVQXKBjK0wQOXjgdkkC1ZTUGP58ieB79pfOAiBJ%2Bk0tyOD2WwXqP%2BP6y%2FxExsDemsTzY7vBMnLX3sKQdCr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMQTlVRwBVHMkc9zXbKtwDXo5CqpSaPL%2BYc0nIKdu5arw4zlX0d0XPJIXKQR9YH3Dm4z4OGKe%2FKRWavTBFMoXaBUG3K2BWcw3ApFUjVA%2B0dmXoQwFFF8un6OBD%2FrPB7iJfl8TSASaetrEfV%2FmKg6mncnJfIBOqgItWNfXM4mjMCOmfXP4iQP9FNy8EJMXrF%2B0xAkSk1PDXOZZSV9Fh3NdHchrVUyr7QSEPmi5SBgR5q2xfW1sECcyYEBX6hX%2BrChLdnIo45anvDvcUBnvPiz0Glx%2F1ueyzGhUGyIRXkiK580cszWQc%2BU%2FtPecZEYfLU7B8Y%2FOvluKlkpG0B%2Bwf8kjMrPAuKyHMPcgGj5G0XftOP4b3opXi7B%2BhRdYXP2HlIIZrBHrjDjNoOnZNL%2B49z5lM0od9BZHGodNSmUP2PNOaOwPGek4JJenBRr%2FcWK7Yx05K%2FpM3HmfBrOyBlVYViy05apHDzq4FlzH78gA%2Bea9az4T4SjiMWXGFVvpLE4HcHYfLAL648Yj1B9x26iVlLgdfMiF%2BM1JPcK%2F9jFyS%2FvIHYLvWNwVYyy47G%2FqQJgyWV%2B9RcQgldPBZfRCxw33rlVyQimBPAAyOhoW3oCEz3g7Oj1qHUFLydwCVEaX6kYZBkx674YPVAVTFjuYIKFAwlZSKvQY6pgEwnRzEwoZ8qYUaA2EtOfuu7tBbs%2FuCipiewC1iQ1pxBZJTtdAlrDyeRlDmqBXC8lHqNa7TvQ7sazgO9jp2wz7%2F0q5y92Uv5MMztohv7zMnRTleoScFPNra6frFG%2BcTyr9WJYIkMxsbsmuHTKA1Zm9STzzkp02i2yNrfAgnP4abx4xwTjCqhp2UdOdgNF%2BweTO9tP6rFZ7cvsOkCji1EAOT9GwLDw8I&X-Amz-Signature=7924b14ba53de26a56ffd082bf389e5a5ba0fd0e1af901ba7a90c5d4a412ae0e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
