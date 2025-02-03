

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G4RSBNP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1it0lebNbfwOZI4pPRgIh8RJEz%2BEb%2BmVGFAJ1w4ShGQIgT1x0RcQsSyAwC0H2H8uPe2f3z0RhWHMyp8g3xnoUu4Qq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDD038ZAwH4lFQZPAtSrcAwYPVPUrNoVR5O%2FwTgvSv7IxxWa%2FKj5VTofnTLz%2Fb2Hjk%2BdzGkngLwvaGI83K8bTqrjWE7kpJPU84TPLBXSv3%2BRV92btYVNHv%2BIO%2Bi3ddX8DdoZTTwVXiUfTgB8CQMUw9Xi30AZ3fBJ3tFuxKjCJCrBaW63SEEXF7m1fTztQJjNCZRgw9kpYPExJMm5gG7xumrSAvx%2BOlsVLV54j%2Fhilt%2FtU%2FhCVz6aO5Xa1X3H37S7flUdBsCA7cyjsM2ob%2B9pS9p05uUvEzimkxqWwC3tllvPmkXu7hevGAsV2ofVj3JGu05oaJeFIfSHbdu9puPcg4u22HRMybhxRzIKCD1%2FFrg3hkoqw4DV%2BfWuw64cfZX%2BoT3PTJS%2FD15mNYZAmA%2BEwpXB4yVZRRHAP08jlN95sCD50ZPmgdD6acKSQVrrdFIlvNSIDOnYXEltdTltE%2BfuFnC7d2Y23Sm1K61xFqzBZOYKt6m9ZUO%2FI%2FPE0WgO2Ivg4pIf0ofGTCn48xkBnVueXObcb%2F4XTh70xNSGvDRSJYyxgaBS6cOsVPnuNcV11ooCpHpVAANIA8iHxL2HPKv8F5lObW6LY%2F7eQgrmm0qTm%2FTsklFLIOiWvkxhXt%2F05cF%2FpMFMvKf6OhMCZbLW3MPbwgr0GOqUBr0aEqf2uu53xw07gs%2BhrS9iF7QkWH82Cl%2FaoS2M97ftrevs65PamnpsHcOXCcr0s9G3pUrp2s9dXyeFJxminjkYndiZ2ZCHfDxZDISh0T7KAWrnUdjNB%2BbSax55ks4J8H6nKKBxLFkHEejj6RfpOO6sB%2Fty2ry134lJv5CWFiWwrS2PYe71zP3JOSzy43iugIu7SB7WbsqhJ1qH%2BbAYTngmV2GqY&X-Amz-Signature=8c9be71b76958922b1339a91d415293ebeb79292164a4486ce5657f6e9e7d27e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G4RSBNP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1it0lebNbfwOZI4pPRgIh8RJEz%2BEb%2BmVGFAJ1w4ShGQIgT1x0RcQsSyAwC0H2H8uPe2f3z0RhWHMyp8g3xnoUu4Qq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDD038ZAwH4lFQZPAtSrcAwYPVPUrNoVR5O%2FwTgvSv7IxxWa%2FKj5VTofnTLz%2Fb2Hjk%2BdzGkngLwvaGI83K8bTqrjWE7kpJPU84TPLBXSv3%2BRV92btYVNHv%2BIO%2Bi3ddX8DdoZTTwVXiUfTgB8CQMUw9Xi30AZ3fBJ3tFuxKjCJCrBaW63SEEXF7m1fTztQJjNCZRgw9kpYPExJMm5gG7xumrSAvx%2BOlsVLV54j%2Fhilt%2FtU%2FhCVz6aO5Xa1X3H37S7flUdBsCA7cyjsM2ob%2B9pS9p05uUvEzimkxqWwC3tllvPmkXu7hevGAsV2ofVj3JGu05oaJeFIfSHbdu9puPcg4u22HRMybhxRzIKCD1%2FFrg3hkoqw4DV%2BfWuw64cfZX%2BoT3PTJS%2FD15mNYZAmA%2BEwpXB4yVZRRHAP08jlN95sCD50ZPmgdD6acKSQVrrdFIlvNSIDOnYXEltdTltE%2BfuFnC7d2Y23Sm1K61xFqzBZOYKt6m9ZUO%2FI%2FPE0WgO2Ivg4pIf0ofGTCn48xkBnVueXObcb%2F4XTh70xNSGvDRSJYyxgaBS6cOsVPnuNcV11ooCpHpVAANIA8iHxL2HPKv8F5lObW6LY%2F7eQgrmm0qTm%2FTsklFLIOiWvkxhXt%2F05cF%2FpMFMvKf6OhMCZbLW3MPbwgr0GOqUBr0aEqf2uu53xw07gs%2BhrS9iF7QkWH82Cl%2FaoS2M97ftrevs65PamnpsHcOXCcr0s9G3pUrp2s9dXyeFJxminjkYndiZ2ZCHfDxZDISh0T7KAWrnUdjNB%2BbSax55ks4J8H6nKKBxLFkHEejj6RfpOO6sB%2Fty2ry134lJv5CWFiWwrS2PYe71zP3JOSzy43iugIu7SB7WbsqhJ1qH%2BbAYTngmV2GqY&X-Amz-Signature=b7ca9c75abc3bc3135e292321270d0e93162536018982c935d2fa5c8190e0822&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G4RSBNP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1it0lebNbfwOZI4pPRgIh8RJEz%2BEb%2BmVGFAJ1w4ShGQIgT1x0RcQsSyAwC0H2H8uPe2f3z0RhWHMyp8g3xnoUu4Qq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDD038ZAwH4lFQZPAtSrcAwYPVPUrNoVR5O%2FwTgvSv7IxxWa%2FKj5VTofnTLz%2Fb2Hjk%2BdzGkngLwvaGI83K8bTqrjWE7kpJPU84TPLBXSv3%2BRV92btYVNHv%2BIO%2Bi3ddX8DdoZTTwVXiUfTgB8CQMUw9Xi30AZ3fBJ3tFuxKjCJCrBaW63SEEXF7m1fTztQJjNCZRgw9kpYPExJMm5gG7xumrSAvx%2BOlsVLV54j%2Fhilt%2FtU%2FhCVz6aO5Xa1X3H37S7flUdBsCA7cyjsM2ob%2B9pS9p05uUvEzimkxqWwC3tllvPmkXu7hevGAsV2ofVj3JGu05oaJeFIfSHbdu9puPcg4u22HRMybhxRzIKCD1%2FFrg3hkoqw4DV%2BfWuw64cfZX%2BoT3PTJS%2FD15mNYZAmA%2BEwpXB4yVZRRHAP08jlN95sCD50ZPmgdD6acKSQVrrdFIlvNSIDOnYXEltdTltE%2BfuFnC7d2Y23Sm1K61xFqzBZOYKt6m9ZUO%2FI%2FPE0WgO2Ivg4pIf0ofGTCn48xkBnVueXObcb%2F4XTh70xNSGvDRSJYyxgaBS6cOsVPnuNcV11ooCpHpVAANIA8iHxL2HPKv8F5lObW6LY%2F7eQgrmm0qTm%2FTsklFLIOiWvkxhXt%2F05cF%2FpMFMvKf6OhMCZbLW3MPbwgr0GOqUBr0aEqf2uu53xw07gs%2BhrS9iF7QkWH82Cl%2FaoS2M97ftrevs65PamnpsHcOXCcr0s9G3pUrp2s9dXyeFJxminjkYndiZ2ZCHfDxZDISh0T7KAWrnUdjNB%2BbSax55ks4J8H6nKKBxLFkHEejj6RfpOO6sB%2Fty2ry134lJv5CWFiWwrS2PYe71zP3JOSzy43iugIu7SB7WbsqhJ1qH%2BbAYTngmV2GqY&X-Amz-Signature=8c502d55c01b97a652beeef4118a845d09c6282423a20bf46c41f0ccf2bf1dba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G4RSBNP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1it0lebNbfwOZI4pPRgIh8RJEz%2BEb%2BmVGFAJ1w4ShGQIgT1x0RcQsSyAwC0H2H8uPe2f3z0RhWHMyp8g3xnoUu4Qq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDD038ZAwH4lFQZPAtSrcAwYPVPUrNoVR5O%2FwTgvSv7IxxWa%2FKj5VTofnTLz%2Fb2Hjk%2BdzGkngLwvaGI83K8bTqrjWE7kpJPU84TPLBXSv3%2BRV92btYVNHv%2BIO%2Bi3ddX8DdoZTTwVXiUfTgB8CQMUw9Xi30AZ3fBJ3tFuxKjCJCrBaW63SEEXF7m1fTztQJjNCZRgw9kpYPExJMm5gG7xumrSAvx%2BOlsVLV54j%2Fhilt%2FtU%2FhCVz6aO5Xa1X3H37S7flUdBsCA7cyjsM2ob%2B9pS9p05uUvEzimkxqWwC3tllvPmkXu7hevGAsV2ofVj3JGu05oaJeFIfSHbdu9puPcg4u22HRMybhxRzIKCD1%2FFrg3hkoqw4DV%2BfWuw64cfZX%2BoT3PTJS%2FD15mNYZAmA%2BEwpXB4yVZRRHAP08jlN95sCD50ZPmgdD6acKSQVrrdFIlvNSIDOnYXEltdTltE%2BfuFnC7d2Y23Sm1K61xFqzBZOYKt6m9ZUO%2FI%2FPE0WgO2Ivg4pIf0ofGTCn48xkBnVueXObcb%2F4XTh70xNSGvDRSJYyxgaBS6cOsVPnuNcV11ooCpHpVAANIA8iHxL2HPKv8F5lObW6LY%2F7eQgrmm0qTm%2FTsklFLIOiWvkxhXt%2F05cF%2FpMFMvKf6OhMCZbLW3MPbwgr0GOqUBr0aEqf2uu53xw07gs%2BhrS9iF7QkWH82Cl%2FaoS2M97ftrevs65PamnpsHcOXCcr0s9G3pUrp2s9dXyeFJxminjkYndiZ2ZCHfDxZDISh0T7KAWrnUdjNB%2BbSax55ks4J8H6nKKBxLFkHEejj6RfpOO6sB%2Fty2ry134lJv5CWFiWwrS2PYe71zP3JOSzy43iugIu7SB7WbsqhJ1qH%2BbAYTngmV2GqY&X-Amz-Signature=d9eaa9338dd60fdedcde00b6767a41d2d5449c28404e1160865dc4cbc695a952&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G4RSBNP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1it0lebNbfwOZI4pPRgIh8RJEz%2BEb%2BmVGFAJ1w4ShGQIgT1x0RcQsSyAwC0H2H8uPe2f3z0RhWHMyp8g3xnoUu4Qq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDD038ZAwH4lFQZPAtSrcAwYPVPUrNoVR5O%2FwTgvSv7IxxWa%2FKj5VTofnTLz%2Fb2Hjk%2BdzGkngLwvaGI83K8bTqrjWE7kpJPU84TPLBXSv3%2BRV92btYVNHv%2BIO%2Bi3ddX8DdoZTTwVXiUfTgB8CQMUw9Xi30AZ3fBJ3tFuxKjCJCrBaW63SEEXF7m1fTztQJjNCZRgw9kpYPExJMm5gG7xumrSAvx%2BOlsVLV54j%2Fhilt%2FtU%2FhCVz6aO5Xa1X3H37S7flUdBsCA7cyjsM2ob%2B9pS9p05uUvEzimkxqWwC3tllvPmkXu7hevGAsV2ofVj3JGu05oaJeFIfSHbdu9puPcg4u22HRMybhxRzIKCD1%2FFrg3hkoqw4DV%2BfWuw64cfZX%2BoT3PTJS%2FD15mNYZAmA%2BEwpXB4yVZRRHAP08jlN95sCD50ZPmgdD6acKSQVrrdFIlvNSIDOnYXEltdTltE%2BfuFnC7d2Y23Sm1K61xFqzBZOYKt6m9ZUO%2FI%2FPE0WgO2Ivg4pIf0ofGTCn48xkBnVueXObcb%2F4XTh70xNSGvDRSJYyxgaBS6cOsVPnuNcV11ooCpHpVAANIA8iHxL2HPKv8F5lObW6LY%2F7eQgrmm0qTm%2FTsklFLIOiWvkxhXt%2F05cF%2FpMFMvKf6OhMCZbLW3MPbwgr0GOqUBr0aEqf2uu53xw07gs%2BhrS9iF7QkWH82Cl%2FaoS2M97ftrevs65PamnpsHcOXCcr0s9G3pUrp2s9dXyeFJxminjkYndiZ2ZCHfDxZDISh0T7KAWrnUdjNB%2BbSax55ks4J8H6nKKBxLFkHEejj6RfpOO6sB%2Fty2ry134lJv5CWFiWwrS2PYe71zP3JOSzy43iugIu7SB7WbsqhJ1qH%2BbAYTngmV2GqY&X-Amz-Signature=6ea737430f7609d04b598596d9712308e465c4cc16c19967cdd90faaff5f66a3&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G4RSBNP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1it0lebNbfwOZI4pPRgIh8RJEz%2BEb%2BmVGFAJ1w4ShGQIgT1x0RcQsSyAwC0H2H8uPe2f3z0RhWHMyp8g3xnoUu4Qq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDD038ZAwH4lFQZPAtSrcAwYPVPUrNoVR5O%2FwTgvSv7IxxWa%2FKj5VTofnTLz%2Fb2Hjk%2BdzGkngLwvaGI83K8bTqrjWE7kpJPU84TPLBXSv3%2BRV92btYVNHv%2BIO%2Bi3ddX8DdoZTTwVXiUfTgB8CQMUw9Xi30AZ3fBJ3tFuxKjCJCrBaW63SEEXF7m1fTztQJjNCZRgw9kpYPExJMm5gG7xumrSAvx%2BOlsVLV54j%2Fhilt%2FtU%2FhCVz6aO5Xa1X3H37S7flUdBsCA7cyjsM2ob%2B9pS9p05uUvEzimkxqWwC3tllvPmkXu7hevGAsV2ofVj3JGu05oaJeFIfSHbdu9puPcg4u22HRMybhxRzIKCD1%2FFrg3hkoqw4DV%2BfWuw64cfZX%2BoT3PTJS%2FD15mNYZAmA%2BEwpXB4yVZRRHAP08jlN95sCD50ZPmgdD6acKSQVrrdFIlvNSIDOnYXEltdTltE%2BfuFnC7d2Y23Sm1K61xFqzBZOYKt6m9ZUO%2FI%2FPE0WgO2Ivg4pIf0ofGTCn48xkBnVueXObcb%2F4XTh70xNSGvDRSJYyxgaBS6cOsVPnuNcV11ooCpHpVAANIA8iHxL2HPKv8F5lObW6LY%2F7eQgrmm0qTm%2FTsklFLIOiWvkxhXt%2F05cF%2FpMFMvKf6OhMCZbLW3MPbwgr0GOqUBr0aEqf2uu53xw07gs%2BhrS9iF7QkWH82Cl%2FaoS2M97ftrevs65PamnpsHcOXCcr0s9G3pUrp2s9dXyeFJxminjkYndiZ2ZCHfDxZDISh0T7KAWrnUdjNB%2BbSax55ks4J8H6nKKBxLFkHEejj6RfpOO6sB%2Fty2ry134lJv5CWFiWwrS2PYe71zP3JOSzy43iugIu7SB7WbsqhJ1qH%2BbAYTngmV2GqY&X-Amz-Signature=ae80b54d88d5e861f0e48e667502256946e8390c0869032ceda97989d646cc5b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G4RSBNP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1it0lebNbfwOZI4pPRgIh8RJEz%2BEb%2BmVGFAJ1w4ShGQIgT1x0RcQsSyAwC0H2H8uPe2f3z0RhWHMyp8g3xnoUu4Qq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDD038ZAwH4lFQZPAtSrcAwYPVPUrNoVR5O%2FwTgvSv7IxxWa%2FKj5VTofnTLz%2Fb2Hjk%2BdzGkngLwvaGI83K8bTqrjWE7kpJPU84TPLBXSv3%2BRV92btYVNHv%2BIO%2Bi3ddX8DdoZTTwVXiUfTgB8CQMUw9Xi30AZ3fBJ3tFuxKjCJCrBaW63SEEXF7m1fTztQJjNCZRgw9kpYPExJMm5gG7xumrSAvx%2BOlsVLV54j%2Fhilt%2FtU%2FhCVz6aO5Xa1X3H37S7flUdBsCA7cyjsM2ob%2B9pS9p05uUvEzimkxqWwC3tllvPmkXu7hevGAsV2ofVj3JGu05oaJeFIfSHbdu9puPcg4u22HRMybhxRzIKCD1%2FFrg3hkoqw4DV%2BfWuw64cfZX%2BoT3PTJS%2FD15mNYZAmA%2BEwpXB4yVZRRHAP08jlN95sCD50ZPmgdD6acKSQVrrdFIlvNSIDOnYXEltdTltE%2BfuFnC7d2Y23Sm1K61xFqzBZOYKt6m9ZUO%2FI%2FPE0WgO2Ivg4pIf0ofGTCn48xkBnVueXObcb%2F4XTh70xNSGvDRSJYyxgaBS6cOsVPnuNcV11ooCpHpVAANIA8iHxL2HPKv8F5lObW6LY%2F7eQgrmm0qTm%2FTsklFLIOiWvkxhXt%2F05cF%2FpMFMvKf6OhMCZbLW3MPbwgr0GOqUBr0aEqf2uu53xw07gs%2BhrS9iF7QkWH82Cl%2FaoS2M97ftrevs65PamnpsHcOXCcr0s9G3pUrp2s9dXyeFJxminjkYndiZ2ZCHfDxZDISh0T7KAWrnUdjNB%2BbSax55ks4J8H6nKKBxLFkHEejj6RfpOO6sB%2Fty2ry134lJv5CWFiWwrS2PYe71zP3JOSzy43iugIu7SB7WbsqhJ1qH%2BbAYTngmV2GqY&X-Amz-Signature=912b5d58fc5e90049af6fb2f872b98f3723944fcf2aad55c5bc94b4d15526b58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G4RSBNP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1it0lebNbfwOZI4pPRgIh8RJEz%2BEb%2BmVGFAJ1w4ShGQIgT1x0RcQsSyAwC0H2H8uPe2f3z0RhWHMyp8g3xnoUu4Qq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDD038ZAwH4lFQZPAtSrcAwYPVPUrNoVR5O%2FwTgvSv7IxxWa%2FKj5VTofnTLz%2Fb2Hjk%2BdzGkngLwvaGI83K8bTqrjWE7kpJPU84TPLBXSv3%2BRV92btYVNHv%2BIO%2Bi3ddX8DdoZTTwVXiUfTgB8CQMUw9Xi30AZ3fBJ3tFuxKjCJCrBaW63SEEXF7m1fTztQJjNCZRgw9kpYPExJMm5gG7xumrSAvx%2BOlsVLV54j%2Fhilt%2FtU%2FhCVz6aO5Xa1X3H37S7flUdBsCA7cyjsM2ob%2B9pS9p05uUvEzimkxqWwC3tllvPmkXu7hevGAsV2ofVj3JGu05oaJeFIfSHbdu9puPcg4u22HRMybhxRzIKCD1%2FFrg3hkoqw4DV%2BfWuw64cfZX%2BoT3PTJS%2FD15mNYZAmA%2BEwpXB4yVZRRHAP08jlN95sCD50ZPmgdD6acKSQVrrdFIlvNSIDOnYXEltdTltE%2BfuFnC7d2Y23Sm1K61xFqzBZOYKt6m9ZUO%2FI%2FPE0WgO2Ivg4pIf0ofGTCn48xkBnVueXObcb%2F4XTh70xNSGvDRSJYyxgaBS6cOsVPnuNcV11ooCpHpVAANIA8iHxL2HPKv8F5lObW6LY%2F7eQgrmm0qTm%2FTsklFLIOiWvkxhXt%2F05cF%2FpMFMvKf6OhMCZbLW3MPbwgr0GOqUBr0aEqf2uu53xw07gs%2BhrS9iF7QkWH82Cl%2FaoS2M97ftrevs65PamnpsHcOXCcr0s9G3pUrp2s9dXyeFJxminjkYndiZ2ZCHfDxZDISh0T7KAWrnUdjNB%2BbSax55ks4J8H6nKKBxLFkHEejj6RfpOO6sB%2Fty2ry134lJv5CWFiWwrS2PYe71zP3JOSzy43iugIu7SB7WbsqhJ1qH%2BbAYTngmV2GqY&X-Amz-Signature=2d950d4aa3be4c5709cb400d7b407bba0514cddd873896ca01715db70385e7f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G4RSBNP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1it0lebNbfwOZI4pPRgIh8RJEz%2BEb%2BmVGFAJ1w4ShGQIgT1x0RcQsSyAwC0H2H8uPe2f3z0RhWHMyp8g3xnoUu4Qq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDD038ZAwH4lFQZPAtSrcAwYPVPUrNoVR5O%2FwTgvSv7IxxWa%2FKj5VTofnTLz%2Fb2Hjk%2BdzGkngLwvaGI83K8bTqrjWE7kpJPU84TPLBXSv3%2BRV92btYVNHv%2BIO%2Bi3ddX8DdoZTTwVXiUfTgB8CQMUw9Xi30AZ3fBJ3tFuxKjCJCrBaW63SEEXF7m1fTztQJjNCZRgw9kpYPExJMm5gG7xumrSAvx%2BOlsVLV54j%2Fhilt%2FtU%2FhCVz6aO5Xa1X3H37S7flUdBsCA7cyjsM2ob%2B9pS9p05uUvEzimkxqWwC3tllvPmkXu7hevGAsV2ofVj3JGu05oaJeFIfSHbdu9puPcg4u22HRMybhxRzIKCD1%2FFrg3hkoqw4DV%2BfWuw64cfZX%2BoT3PTJS%2FD15mNYZAmA%2BEwpXB4yVZRRHAP08jlN95sCD50ZPmgdD6acKSQVrrdFIlvNSIDOnYXEltdTltE%2BfuFnC7d2Y23Sm1K61xFqzBZOYKt6m9ZUO%2FI%2FPE0WgO2Ivg4pIf0ofGTCn48xkBnVueXObcb%2F4XTh70xNSGvDRSJYyxgaBS6cOsVPnuNcV11ooCpHpVAANIA8iHxL2HPKv8F5lObW6LY%2F7eQgrmm0qTm%2FTsklFLIOiWvkxhXt%2F05cF%2FpMFMvKf6OhMCZbLW3MPbwgr0GOqUBr0aEqf2uu53xw07gs%2BhrS9iF7QkWH82Cl%2FaoS2M97ftrevs65PamnpsHcOXCcr0s9G3pUrp2s9dXyeFJxminjkYndiZ2ZCHfDxZDISh0T7KAWrnUdjNB%2BbSax55ks4J8H6nKKBxLFkHEejj6RfpOO6sB%2Fty2ry134lJv5CWFiWwrS2PYe71zP3JOSzy43iugIu7SB7WbsqhJ1qH%2BbAYTngmV2GqY&X-Amz-Signature=c22e998a08955de308b7d37c92f497b1c6e86f4dde247ebd49dea1900d7d4406&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IRU26M6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHwYqLbXduEGdSWL%2BzYcQ34ckDsBCn3NbWv8p0DxSDNOAiEAvm53t40mTR1gV7HaNLHl2CyHg6OWTnJImxJVfqSGCX0q%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDIAnFDzM2V5NUTygYCrcAzYNvFwtqzm%2FLGPsJe6eC7ScjmrZS6E94WZqW2yGONCDTUyC4Yqc8eVZNHUFAkoVDTxz2w%2FiTnnZDRL4A00PvOyC%2FzzIh8%2BjRtQ1JWfAdrVF%2FSAIWUGaED3ryXoNpsgXakvMFIah85%2FRZKHp%2Fvpn7yZYvzuroH6eS5ANioGVbbgiAAGtYMHmxGmHWO%2BoXx1u64Ifmj%2FOQyZ3js19gr72e71iP%2BVIsVko3R6c%2BA4I%2F0Rosw39BBR1L%2FtRD2Ig81CpV5YRRj7tOXemXYmL7HWc%2B%2FDQ4qIocryUPraV3qDeTwKi5mtsN%2FI3c%2Fy16PUVN1Tch7EHgIVv%2Bl5DgfV50JciIhU67QXvz97h4E0Znx0W0Pv8Ga%2FmKHJH6Yd78x%2BFqVtINxovvjICn%2B1%2Fv%2BTFOXyg0TU8RWZpKwj6GNVV5GAEcxYXpeNQxKB7wNPNuwtwSDUKw4FGQeXxKm5Rn5CT1NFPE7iR7WbXP1iNcmiTcSBqND59HemDrYULnGI7dgL2Ku5xjap0D1V1AZrpj3Xccy7a3Jv%2FeP97y6FoKb3alLhck36Ncr0aDyfK5WrnTRUnMKksjQfg8X00oMx98SpsogpYDpcWRWWIr7ydQHeOZe%2BCXQG2UZXRUUN9BUCUT2eGMJfxgr0GOqUBVLI4%2Fo3jYPwfRbnhKu0tY7Q8EKL96Hii78%2Baq4GNNYeP0abKKWEd%2FngPmUnZRsrGI1CU%2Fn9S2WSlufdYGyck%2FPkllmCgY3ECfHU7FkI6gfdTtR4ZF4x%2FvG6XlVT6xgB0cMCP1epRNcBqdIee2So2%2F9dqCwQug7EEglj6Sp1i1f02tVfTDuZXMm%2FHyNhBstFbJybo99itNTdWXVb2UrGSUzvRy6Kd&X-Amz-Signature=4ca7c3c8f83b5a6f65992f3e7c74375931d81ab85f006ce34d5962b8d00ff0ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IRU26M6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHwYqLbXduEGdSWL%2BzYcQ34ckDsBCn3NbWv8p0DxSDNOAiEAvm53t40mTR1gV7HaNLHl2CyHg6OWTnJImxJVfqSGCX0q%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDIAnFDzM2V5NUTygYCrcAzYNvFwtqzm%2FLGPsJe6eC7ScjmrZS6E94WZqW2yGONCDTUyC4Yqc8eVZNHUFAkoVDTxz2w%2FiTnnZDRL4A00PvOyC%2FzzIh8%2BjRtQ1JWfAdrVF%2FSAIWUGaED3ryXoNpsgXakvMFIah85%2FRZKHp%2Fvpn7yZYvzuroH6eS5ANioGVbbgiAAGtYMHmxGmHWO%2BoXx1u64Ifmj%2FOQyZ3js19gr72e71iP%2BVIsVko3R6c%2BA4I%2F0Rosw39BBR1L%2FtRD2Ig81CpV5YRRj7tOXemXYmL7HWc%2B%2FDQ4qIocryUPraV3qDeTwKi5mtsN%2FI3c%2Fy16PUVN1Tch7EHgIVv%2Bl5DgfV50JciIhU67QXvz97h4E0Znx0W0Pv8Ga%2FmKHJH6Yd78x%2BFqVtINxovvjICn%2B1%2Fv%2BTFOXyg0TU8RWZpKwj6GNVV5GAEcxYXpeNQxKB7wNPNuwtwSDUKw4FGQeXxKm5Rn5CT1NFPE7iR7WbXP1iNcmiTcSBqND59HemDrYULnGI7dgL2Ku5xjap0D1V1AZrpj3Xccy7a3Jv%2FeP97y6FoKb3alLhck36Ncr0aDyfK5WrnTRUnMKksjQfg8X00oMx98SpsogpYDpcWRWWIr7ydQHeOZe%2BCXQG2UZXRUUN9BUCUT2eGMJfxgr0GOqUBVLI4%2Fo3jYPwfRbnhKu0tY7Q8EKL96Hii78%2Baq4GNNYeP0abKKWEd%2FngPmUnZRsrGI1CU%2Fn9S2WSlufdYGyck%2FPkllmCgY3ECfHU7FkI6gfdTtR4ZF4x%2FvG6XlVT6xgB0cMCP1epRNcBqdIee2So2%2F9dqCwQug7EEglj6Sp1i1f02tVfTDuZXMm%2FHyNhBstFbJybo99itNTdWXVb2UrGSUzvRy6Kd&X-Amz-Signature=c58ab3802cbf47c0f3cc6f2c721c8f71c455d3b7c389c3d390ef586a394afffc&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
