

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQI3PC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIECjSv179oUTiOKgI2Gkvdt1T5%2FFnH%2BeR89dgTObY9uEAiAA5gD8WjHJTZ5Yz0McY0qzGIBdS0ckLkpRzKPWpvbMcyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1lQ3Ti8uMuop9PqlKtwDROJzMy5m%2B2jbr6cFC2nGtvdwyN%2BnsZ8Ai3pQaG%2BUmTvqgnbcAp62gcouDGkNLnNBh7bMSvOeHT0nX6%2B2uSWRGBEgeGl5%2BUduJrIqceu%2F%2BYSlLy4fyka2gE3kJMK7%2Fsr%2FIrRwFNjgJFVXkzw2Z4orBjjlVW94x9wPO0X2tSvf%2FQnoeX73pH2svqdQ0PiS2d01n0eYAdZWBjfVUZ%2BLIOW979%2BD5cvitPEED64ZLSob3N3WF0Ah6I2beDF8znLY%2BmTNFR5%2FU%2BaXJLY2Wc1retD13lWEZlNmeW96uhsLr6hQulqi840%2F1Ah%2BoEf2GQswl46qi%2FBKCDGPf8YJ54vdmr78J%2FmgrLuBqEWkIY5eL8LE3w1nGedXMPbMZ7g47zVAnJlbAhP%2BfZM2jT5mAcGIPrm%2B1OzARbs3RAnqavC0PO9TThKKRon9%2FjWBdxJquELl0iNZRpaS%2BxBzRFt1tstmdZD8yXcZdtm3lazoILFIZggRzHdMtoDGyIm%2FbvbCokpcxZiU9sgEEbfrYvHgRrRoxXG4FWe%2FmtSa2g1oPa1teySv1gWdOiZdz1xWHjgixquCtEBAwrDqY5MGJddy%2BxnX90K6Z5HGVz%2BMvFGl00e7RqQEixnrXxRDBiTp6p3rgwUwivTyvAY6pgHXZyXfPZC7p0ZnenbAMWe2nQTVOiFDj6NaNYbPIHT6YuB0cXyfEwgzGm0xvaCSlIZse6HyXpEyD1ZyoaU%2FW%2BJXH3Dzz3XQ1lNhIVqQVQeJIngPEBODxl1VxYQZ%2BkVjIxortZneCFEZHc7NgEtU4uhQnlYGmYDoCzfZupLERwh19qtu6oYOZ1dmjxxzDxfZAKqG5vKhrBNpz%2F7wFhlzPbaUfdOqp5uY&X-Amz-Signature=07d14aaf07660fb4c7f2c7c05db143d76815fd795836d4b8ad474bbdc29cfa89&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQI3PC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIECjSv179oUTiOKgI2Gkvdt1T5%2FFnH%2BeR89dgTObY9uEAiAA5gD8WjHJTZ5Yz0McY0qzGIBdS0ckLkpRzKPWpvbMcyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1lQ3Ti8uMuop9PqlKtwDROJzMy5m%2B2jbr6cFC2nGtvdwyN%2BnsZ8Ai3pQaG%2BUmTvqgnbcAp62gcouDGkNLnNBh7bMSvOeHT0nX6%2B2uSWRGBEgeGl5%2BUduJrIqceu%2F%2BYSlLy4fyka2gE3kJMK7%2Fsr%2FIrRwFNjgJFVXkzw2Z4orBjjlVW94x9wPO0X2tSvf%2FQnoeX73pH2svqdQ0PiS2d01n0eYAdZWBjfVUZ%2BLIOW979%2BD5cvitPEED64ZLSob3N3WF0Ah6I2beDF8znLY%2BmTNFR5%2FU%2BaXJLY2Wc1retD13lWEZlNmeW96uhsLr6hQulqi840%2F1Ah%2BoEf2GQswl46qi%2FBKCDGPf8YJ54vdmr78J%2FmgrLuBqEWkIY5eL8LE3w1nGedXMPbMZ7g47zVAnJlbAhP%2BfZM2jT5mAcGIPrm%2B1OzARbs3RAnqavC0PO9TThKKRon9%2FjWBdxJquELl0iNZRpaS%2BxBzRFt1tstmdZD8yXcZdtm3lazoILFIZggRzHdMtoDGyIm%2FbvbCokpcxZiU9sgEEbfrYvHgRrRoxXG4FWe%2FmtSa2g1oPa1teySv1gWdOiZdz1xWHjgixquCtEBAwrDqY5MGJddy%2BxnX90K6Z5HGVz%2BMvFGl00e7RqQEixnrXxRDBiTp6p3rgwUwivTyvAY6pgHXZyXfPZC7p0ZnenbAMWe2nQTVOiFDj6NaNYbPIHT6YuB0cXyfEwgzGm0xvaCSlIZse6HyXpEyD1ZyoaU%2FW%2BJXH3Dzz3XQ1lNhIVqQVQeJIngPEBODxl1VxYQZ%2BkVjIxortZneCFEZHc7NgEtU4uhQnlYGmYDoCzfZupLERwh19qtu6oYOZ1dmjxxzDxfZAKqG5vKhrBNpz%2F7wFhlzPbaUfdOqp5uY&X-Amz-Signature=615467bab2c2fa1f5776a87feadf12b033238dcc4aa86e5a6a515611b5fd4879&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQI3PC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIECjSv179oUTiOKgI2Gkvdt1T5%2FFnH%2BeR89dgTObY9uEAiAA5gD8WjHJTZ5Yz0McY0qzGIBdS0ckLkpRzKPWpvbMcyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1lQ3Ti8uMuop9PqlKtwDROJzMy5m%2B2jbr6cFC2nGtvdwyN%2BnsZ8Ai3pQaG%2BUmTvqgnbcAp62gcouDGkNLnNBh7bMSvOeHT0nX6%2B2uSWRGBEgeGl5%2BUduJrIqceu%2F%2BYSlLy4fyka2gE3kJMK7%2Fsr%2FIrRwFNjgJFVXkzw2Z4orBjjlVW94x9wPO0X2tSvf%2FQnoeX73pH2svqdQ0PiS2d01n0eYAdZWBjfVUZ%2BLIOW979%2BD5cvitPEED64ZLSob3N3WF0Ah6I2beDF8znLY%2BmTNFR5%2FU%2BaXJLY2Wc1retD13lWEZlNmeW96uhsLr6hQulqi840%2F1Ah%2BoEf2GQswl46qi%2FBKCDGPf8YJ54vdmr78J%2FmgrLuBqEWkIY5eL8LE3w1nGedXMPbMZ7g47zVAnJlbAhP%2BfZM2jT5mAcGIPrm%2B1OzARbs3RAnqavC0PO9TThKKRon9%2FjWBdxJquELl0iNZRpaS%2BxBzRFt1tstmdZD8yXcZdtm3lazoILFIZggRzHdMtoDGyIm%2FbvbCokpcxZiU9sgEEbfrYvHgRrRoxXG4FWe%2FmtSa2g1oPa1teySv1gWdOiZdz1xWHjgixquCtEBAwrDqY5MGJddy%2BxnX90K6Z5HGVz%2BMvFGl00e7RqQEixnrXxRDBiTp6p3rgwUwivTyvAY6pgHXZyXfPZC7p0ZnenbAMWe2nQTVOiFDj6NaNYbPIHT6YuB0cXyfEwgzGm0xvaCSlIZse6HyXpEyD1ZyoaU%2FW%2BJXH3Dzz3XQ1lNhIVqQVQeJIngPEBODxl1VxYQZ%2BkVjIxortZneCFEZHc7NgEtU4uhQnlYGmYDoCzfZupLERwh19qtu6oYOZ1dmjxxzDxfZAKqG5vKhrBNpz%2F7wFhlzPbaUfdOqp5uY&X-Amz-Signature=9c61255058f4eda8f798643428a0bd9ba64d9c804a769b1dac35b11059c27629&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQI3PC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIECjSv179oUTiOKgI2Gkvdt1T5%2FFnH%2BeR89dgTObY9uEAiAA5gD8WjHJTZ5Yz0McY0qzGIBdS0ckLkpRzKPWpvbMcyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1lQ3Ti8uMuop9PqlKtwDROJzMy5m%2B2jbr6cFC2nGtvdwyN%2BnsZ8Ai3pQaG%2BUmTvqgnbcAp62gcouDGkNLnNBh7bMSvOeHT0nX6%2B2uSWRGBEgeGl5%2BUduJrIqceu%2F%2BYSlLy4fyka2gE3kJMK7%2Fsr%2FIrRwFNjgJFVXkzw2Z4orBjjlVW94x9wPO0X2tSvf%2FQnoeX73pH2svqdQ0PiS2d01n0eYAdZWBjfVUZ%2BLIOW979%2BD5cvitPEED64ZLSob3N3WF0Ah6I2beDF8znLY%2BmTNFR5%2FU%2BaXJLY2Wc1retD13lWEZlNmeW96uhsLr6hQulqi840%2F1Ah%2BoEf2GQswl46qi%2FBKCDGPf8YJ54vdmr78J%2FmgrLuBqEWkIY5eL8LE3w1nGedXMPbMZ7g47zVAnJlbAhP%2BfZM2jT5mAcGIPrm%2B1OzARbs3RAnqavC0PO9TThKKRon9%2FjWBdxJquELl0iNZRpaS%2BxBzRFt1tstmdZD8yXcZdtm3lazoILFIZggRzHdMtoDGyIm%2FbvbCokpcxZiU9sgEEbfrYvHgRrRoxXG4FWe%2FmtSa2g1oPa1teySv1gWdOiZdz1xWHjgixquCtEBAwrDqY5MGJddy%2BxnX90K6Z5HGVz%2BMvFGl00e7RqQEixnrXxRDBiTp6p3rgwUwivTyvAY6pgHXZyXfPZC7p0ZnenbAMWe2nQTVOiFDj6NaNYbPIHT6YuB0cXyfEwgzGm0xvaCSlIZse6HyXpEyD1ZyoaU%2FW%2BJXH3Dzz3XQ1lNhIVqQVQeJIngPEBODxl1VxYQZ%2BkVjIxortZneCFEZHc7NgEtU4uhQnlYGmYDoCzfZupLERwh19qtu6oYOZ1dmjxxzDxfZAKqG5vKhrBNpz%2F7wFhlzPbaUfdOqp5uY&X-Amz-Signature=e65e24b23242a4769b4153a228c0ac59d798f85faca19d63836c4fccafcfc12b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQI3PC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIECjSv179oUTiOKgI2Gkvdt1T5%2FFnH%2BeR89dgTObY9uEAiAA5gD8WjHJTZ5Yz0McY0qzGIBdS0ckLkpRzKPWpvbMcyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1lQ3Ti8uMuop9PqlKtwDROJzMy5m%2B2jbr6cFC2nGtvdwyN%2BnsZ8Ai3pQaG%2BUmTvqgnbcAp62gcouDGkNLnNBh7bMSvOeHT0nX6%2B2uSWRGBEgeGl5%2BUduJrIqceu%2F%2BYSlLy4fyka2gE3kJMK7%2Fsr%2FIrRwFNjgJFVXkzw2Z4orBjjlVW94x9wPO0X2tSvf%2FQnoeX73pH2svqdQ0PiS2d01n0eYAdZWBjfVUZ%2BLIOW979%2BD5cvitPEED64ZLSob3N3WF0Ah6I2beDF8znLY%2BmTNFR5%2FU%2BaXJLY2Wc1retD13lWEZlNmeW96uhsLr6hQulqi840%2F1Ah%2BoEf2GQswl46qi%2FBKCDGPf8YJ54vdmr78J%2FmgrLuBqEWkIY5eL8LE3w1nGedXMPbMZ7g47zVAnJlbAhP%2BfZM2jT5mAcGIPrm%2B1OzARbs3RAnqavC0PO9TThKKRon9%2FjWBdxJquELl0iNZRpaS%2BxBzRFt1tstmdZD8yXcZdtm3lazoILFIZggRzHdMtoDGyIm%2FbvbCokpcxZiU9sgEEbfrYvHgRrRoxXG4FWe%2FmtSa2g1oPa1teySv1gWdOiZdz1xWHjgixquCtEBAwrDqY5MGJddy%2BxnX90K6Z5HGVz%2BMvFGl00e7RqQEixnrXxRDBiTp6p3rgwUwivTyvAY6pgHXZyXfPZC7p0ZnenbAMWe2nQTVOiFDj6NaNYbPIHT6YuB0cXyfEwgzGm0xvaCSlIZse6HyXpEyD1ZyoaU%2FW%2BJXH3Dzz3XQ1lNhIVqQVQeJIngPEBODxl1VxYQZ%2BkVjIxortZneCFEZHc7NgEtU4uhQnlYGmYDoCzfZupLERwh19qtu6oYOZ1dmjxxzDxfZAKqG5vKhrBNpz%2F7wFhlzPbaUfdOqp5uY&X-Amz-Signature=7e8c78fd04caf0e2ada2e7cb5b3f47533dce252d5a541f4907302fe3919e4ab1&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQI3PC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIECjSv179oUTiOKgI2Gkvdt1T5%2FFnH%2BeR89dgTObY9uEAiAA5gD8WjHJTZ5Yz0McY0qzGIBdS0ckLkpRzKPWpvbMcyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1lQ3Ti8uMuop9PqlKtwDROJzMy5m%2B2jbr6cFC2nGtvdwyN%2BnsZ8Ai3pQaG%2BUmTvqgnbcAp62gcouDGkNLnNBh7bMSvOeHT0nX6%2B2uSWRGBEgeGl5%2BUduJrIqceu%2F%2BYSlLy4fyka2gE3kJMK7%2Fsr%2FIrRwFNjgJFVXkzw2Z4orBjjlVW94x9wPO0X2tSvf%2FQnoeX73pH2svqdQ0PiS2d01n0eYAdZWBjfVUZ%2BLIOW979%2BD5cvitPEED64ZLSob3N3WF0Ah6I2beDF8znLY%2BmTNFR5%2FU%2BaXJLY2Wc1retD13lWEZlNmeW96uhsLr6hQulqi840%2F1Ah%2BoEf2GQswl46qi%2FBKCDGPf8YJ54vdmr78J%2FmgrLuBqEWkIY5eL8LE3w1nGedXMPbMZ7g47zVAnJlbAhP%2BfZM2jT5mAcGIPrm%2B1OzARbs3RAnqavC0PO9TThKKRon9%2FjWBdxJquELl0iNZRpaS%2BxBzRFt1tstmdZD8yXcZdtm3lazoILFIZggRzHdMtoDGyIm%2FbvbCokpcxZiU9sgEEbfrYvHgRrRoxXG4FWe%2FmtSa2g1oPa1teySv1gWdOiZdz1xWHjgixquCtEBAwrDqY5MGJddy%2BxnX90K6Z5HGVz%2BMvFGl00e7RqQEixnrXxRDBiTp6p3rgwUwivTyvAY6pgHXZyXfPZC7p0ZnenbAMWe2nQTVOiFDj6NaNYbPIHT6YuB0cXyfEwgzGm0xvaCSlIZse6HyXpEyD1ZyoaU%2FW%2BJXH3Dzz3XQ1lNhIVqQVQeJIngPEBODxl1VxYQZ%2BkVjIxortZneCFEZHc7NgEtU4uhQnlYGmYDoCzfZupLERwh19qtu6oYOZ1dmjxxzDxfZAKqG5vKhrBNpz%2F7wFhlzPbaUfdOqp5uY&X-Amz-Signature=67e682a878958efb3c7fd09de166e53cd66d6c9b715ed67af554b60d60166ee9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQI3PC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIECjSv179oUTiOKgI2Gkvdt1T5%2FFnH%2BeR89dgTObY9uEAiAA5gD8WjHJTZ5Yz0McY0qzGIBdS0ckLkpRzKPWpvbMcyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1lQ3Ti8uMuop9PqlKtwDROJzMy5m%2B2jbr6cFC2nGtvdwyN%2BnsZ8Ai3pQaG%2BUmTvqgnbcAp62gcouDGkNLnNBh7bMSvOeHT0nX6%2B2uSWRGBEgeGl5%2BUduJrIqceu%2F%2BYSlLy4fyka2gE3kJMK7%2Fsr%2FIrRwFNjgJFVXkzw2Z4orBjjlVW94x9wPO0X2tSvf%2FQnoeX73pH2svqdQ0PiS2d01n0eYAdZWBjfVUZ%2BLIOW979%2BD5cvitPEED64ZLSob3N3WF0Ah6I2beDF8znLY%2BmTNFR5%2FU%2BaXJLY2Wc1retD13lWEZlNmeW96uhsLr6hQulqi840%2F1Ah%2BoEf2GQswl46qi%2FBKCDGPf8YJ54vdmr78J%2FmgrLuBqEWkIY5eL8LE3w1nGedXMPbMZ7g47zVAnJlbAhP%2BfZM2jT5mAcGIPrm%2B1OzARbs3RAnqavC0PO9TThKKRon9%2FjWBdxJquELl0iNZRpaS%2BxBzRFt1tstmdZD8yXcZdtm3lazoILFIZggRzHdMtoDGyIm%2FbvbCokpcxZiU9sgEEbfrYvHgRrRoxXG4FWe%2FmtSa2g1oPa1teySv1gWdOiZdz1xWHjgixquCtEBAwrDqY5MGJddy%2BxnX90K6Z5HGVz%2BMvFGl00e7RqQEixnrXxRDBiTp6p3rgwUwivTyvAY6pgHXZyXfPZC7p0ZnenbAMWe2nQTVOiFDj6NaNYbPIHT6YuB0cXyfEwgzGm0xvaCSlIZse6HyXpEyD1ZyoaU%2FW%2BJXH3Dzz3XQ1lNhIVqQVQeJIngPEBODxl1VxYQZ%2BkVjIxortZneCFEZHc7NgEtU4uhQnlYGmYDoCzfZupLERwh19qtu6oYOZ1dmjxxzDxfZAKqG5vKhrBNpz%2F7wFhlzPbaUfdOqp5uY&X-Amz-Signature=2b67b0b5841d5983851483d43cc35b643c0d778ba9f550a2299b8b751b4e9877&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQI3PC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIECjSv179oUTiOKgI2Gkvdt1T5%2FFnH%2BeR89dgTObY9uEAiAA5gD8WjHJTZ5Yz0McY0qzGIBdS0ckLkpRzKPWpvbMcyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1lQ3Ti8uMuop9PqlKtwDROJzMy5m%2B2jbr6cFC2nGtvdwyN%2BnsZ8Ai3pQaG%2BUmTvqgnbcAp62gcouDGkNLnNBh7bMSvOeHT0nX6%2B2uSWRGBEgeGl5%2BUduJrIqceu%2F%2BYSlLy4fyka2gE3kJMK7%2Fsr%2FIrRwFNjgJFVXkzw2Z4orBjjlVW94x9wPO0X2tSvf%2FQnoeX73pH2svqdQ0PiS2d01n0eYAdZWBjfVUZ%2BLIOW979%2BD5cvitPEED64ZLSob3N3WF0Ah6I2beDF8znLY%2BmTNFR5%2FU%2BaXJLY2Wc1retD13lWEZlNmeW96uhsLr6hQulqi840%2F1Ah%2BoEf2GQswl46qi%2FBKCDGPf8YJ54vdmr78J%2FmgrLuBqEWkIY5eL8LE3w1nGedXMPbMZ7g47zVAnJlbAhP%2BfZM2jT5mAcGIPrm%2B1OzARbs3RAnqavC0PO9TThKKRon9%2FjWBdxJquELl0iNZRpaS%2BxBzRFt1tstmdZD8yXcZdtm3lazoILFIZggRzHdMtoDGyIm%2FbvbCokpcxZiU9sgEEbfrYvHgRrRoxXG4FWe%2FmtSa2g1oPa1teySv1gWdOiZdz1xWHjgixquCtEBAwrDqY5MGJddy%2BxnX90K6Z5HGVz%2BMvFGl00e7RqQEixnrXxRDBiTp6p3rgwUwivTyvAY6pgHXZyXfPZC7p0ZnenbAMWe2nQTVOiFDj6NaNYbPIHT6YuB0cXyfEwgzGm0xvaCSlIZse6HyXpEyD1ZyoaU%2FW%2BJXH3Dzz3XQ1lNhIVqQVQeJIngPEBODxl1VxYQZ%2BkVjIxortZneCFEZHc7NgEtU4uhQnlYGmYDoCzfZupLERwh19qtu6oYOZ1dmjxxzDxfZAKqG5vKhrBNpz%2F7wFhlzPbaUfdOqp5uY&X-Amz-Signature=3a8073264047cf89dac9b85dd47d41c4035cdb4ba64e9731063161d4d38efa0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQI3PC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIECjSv179oUTiOKgI2Gkvdt1T5%2FFnH%2BeR89dgTObY9uEAiAA5gD8WjHJTZ5Yz0McY0qzGIBdS0ckLkpRzKPWpvbMcyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1lQ3Ti8uMuop9PqlKtwDROJzMy5m%2B2jbr6cFC2nGtvdwyN%2BnsZ8Ai3pQaG%2BUmTvqgnbcAp62gcouDGkNLnNBh7bMSvOeHT0nX6%2B2uSWRGBEgeGl5%2BUduJrIqceu%2F%2BYSlLy4fyka2gE3kJMK7%2Fsr%2FIrRwFNjgJFVXkzw2Z4orBjjlVW94x9wPO0X2tSvf%2FQnoeX73pH2svqdQ0PiS2d01n0eYAdZWBjfVUZ%2BLIOW979%2BD5cvitPEED64ZLSob3N3WF0Ah6I2beDF8znLY%2BmTNFR5%2FU%2BaXJLY2Wc1retD13lWEZlNmeW96uhsLr6hQulqi840%2F1Ah%2BoEf2GQswl46qi%2FBKCDGPf8YJ54vdmr78J%2FmgrLuBqEWkIY5eL8LE3w1nGedXMPbMZ7g47zVAnJlbAhP%2BfZM2jT5mAcGIPrm%2B1OzARbs3RAnqavC0PO9TThKKRon9%2FjWBdxJquELl0iNZRpaS%2BxBzRFt1tstmdZD8yXcZdtm3lazoILFIZggRzHdMtoDGyIm%2FbvbCokpcxZiU9sgEEbfrYvHgRrRoxXG4FWe%2FmtSa2g1oPa1teySv1gWdOiZdz1xWHjgixquCtEBAwrDqY5MGJddy%2BxnX90K6Z5HGVz%2BMvFGl00e7RqQEixnrXxRDBiTp6p3rgwUwivTyvAY6pgHXZyXfPZC7p0ZnenbAMWe2nQTVOiFDj6NaNYbPIHT6YuB0cXyfEwgzGm0xvaCSlIZse6HyXpEyD1ZyoaU%2FW%2BJXH3Dzz3XQ1lNhIVqQVQeJIngPEBODxl1VxYQZ%2BkVjIxortZneCFEZHc7NgEtU4uhQnlYGmYDoCzfZupLERwh19qtu6oYOZ1dmjxxzDxfZAKqG5vKhrBNpz%2F7wFhlzPbaUfdOqp5uY&X-Amz-Signature=639b85f3b9f226a3e2f720ef2c3549d3ccc461557fb37467cf2b989d82773270&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAUT7QT2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRCKlR%2BaA%2BNALD8Jk52CCr%2Fcq2t42ayUO%2BqwIjEE1%2BNQIgJNizTSoM4aqfjQOyda4H9ecDGCL8j4OwhADLsGqUu2UqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2F%2BMqlEI23gKWnDFCrcAwxHUE3f56wHrwhrOdNwlsLDZbG6FPbNUsYiwxyCe8fLIWkVHtdr8B1sEKr36dR5%2Fpmc4iTbG%2Bxe%2B7AdmlLkAgzFiVNYMBF28daSG9IYEiPxWBlHEV81MOQq6DJGYhqZy8EoFPJ3Jeee2Q3RRfNHDV%2F0cT2OdES8tOetnyqEFm4REWDNhFMcuFLiKJ8XAB2%2BscghH0Rl3EFgChkmANxB1CwZ%2BoQal9vp9ItoFCr3fKrflu51XHpNvW63kaIq%2BB210rkNKQPslj7zx7Usl1JnthwuRBQF2kL3BDjJHgqPfKw3B37H3fyzaHw%2BujlA1sv4zuUB7WnnBz%2BrBUDoQMiC0F3DgSeMXkIZGEgtnXthvHP1x0kiZyjOU94V%2FdcyGSI4ItV3xzScSFbgmhvo2Kqd1YEEOI8%2BcHlCNYOkaRlxzj2nIkMrpXcHdXW5cQRa2a5hezqGeDB2RTUSo2It3K09Avo2jNl7nIpXA2jbk%2FifJal1T2godzuI7HWK8KSfjEsY654dcVHlHzId5rvx2DHT7SXbCg%2FGFvbhtXIGfn9JN3%2BHWrOCPHHoXvNVGqJPQBTyb3QjKlRUrxpFDsjTgSq7f1IgPqlAldt7snO1eAtz8zin9eVoNM%2FpzXzOu6CAMKX08rwGOqUBJAELmI5c2vDB6yUL%2BwXW1qvpHzpOmI4lsJrJcPg1mm26mkRi0PkTjotp8oSJrN3TwNYaR1KienxTdliV7SHGKk%2FycLyOYmxYu7H2hhQiYZB1rNreDit6SCmzYOWRdD1qIcntvSxg3FsZ9Hrlw0%2B4sukP7ARLYwhd5%2BlzVO1quTiqzC3XPpwkQYquqEAFKhqckhPHsyYgJZYFzTLDz5N7ovA2a6aR&X-Amz-Signature=c426e072ad76bcac6e3ec39a05cc92c2e9b2d8caf156870d78bd54cfca59505e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAUT7QT2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRCKlR%2BaA%2BNALD8Jk52CCr%2Fcq2t42ayUO%2BqwIjEE1%2BNQIgJNizTSoM4aqfjQOyda4H9ecDGCL8j4OwhADLsGqUu2UqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2F%2BMqlEI23gKWnDFCrcAwxHUE3f56wHrwhrOdNwlsLDZbG6FPbNUsYiwxyCe8fLIWkVHtdr8B1sEKr36dR5%2Fpmc4iTbG%2Bxe%2B7AdmlLkAgzFiVNYMBF28daSG9IYEiPxWBlHEV81MOQq6DJGYhqZy8EoFPJ3Jeee2Q3RRfNHDV%2F0cT2OdES8tOetnyqEFm4REWDNhFMcuFLiKJ8XAB2%2BscghH0Rl3EFgChkmANxB1CwZ%2BoQal9vp9ItoFCr3fKrflu51XHpNvW63kaIq%2BB210rkNKQPslj7zx7Usl1JnthwuRBQF2kL3BDjJHgqPfKw3B37H3fyzaHw%2BujlA1sv4zuUB7WnnBz%2BrBUDoQMiC0F3DgSeMXkIZGEgtnXthvHP1x0kiZyjOU94V%2FdcyGSI4ItV3xzScSFbgmhvo2Kqd1YEEOI8%2BcHlCNYOkaRlxzj2nIkMrpXcHdXW5cQRa2a5hezqGeDB2RTUSo2It3K09Avo2jNl7nIpXA2jbk%2FifJal1T2godzuI7HWK8KSfjEsY654dcVHlHzId5rvx2DHT7SXbCg%2FGFvbhtXIGfn9JN3%2BHWrOCPHHoXvNVGqJPQBTyb3QjKlRUrxpFDsjTgSq7f1IgPqlAldt7snO1eAtz8zin9eVoNM%2FpzXzOu6CAMKX08rwGOqUBJAELmI5c2vDB6yUL%2BwXW1qvpHzpOmI4lsJrJcPg1mm26mkRi0PkTjotp8oSJrN3TwNYaR1KienxTdliV7SHGKk%2FycLyOYmxYu7H2hhQiYZB1rNreDit6SCmzYOWRdD1qIcntvSxg3FsZ9Hrlw0%2B4sukP7ARLYwhd5%2BlzVO1quTiqzC3XPpwkQYquqEAFKhqckhPHsyYgJZYFzTLDz5N7ovA2a6aR&X-Amz-Signature=8e59500e93292bbf09d7560e728ef2a761d7d9f9493bc2c6c460352ec5688f4e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
