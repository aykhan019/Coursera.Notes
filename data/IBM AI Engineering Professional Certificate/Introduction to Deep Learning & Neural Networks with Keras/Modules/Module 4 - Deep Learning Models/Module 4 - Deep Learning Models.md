

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQNZFND%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIxTvnLVpYq2qR2Lmzrf8lHQuiT2J4%2B8F3eH4JM%2BwuLAiAI1LSfdXmkM0wF6qReW2eNbxjRrYNk1kncjuC%2FKaxp0SqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnZDbA6I4UCy%2BjafqKtwDvjThQrRrdwwp%2FRYI2POlkGAvwpgAWtz2XNGWM1HlFys9LsH6GgFto6qpGh9zfHKkBQ%2BAqgMjOXhRNonyHLTQXTDd53HHZS7eiAdUpjzGd8A52OMuBpl7rspJwCa3TfEfBpbByl6xYju7X4XnjbtTd2kcnXQZ7kphp5hQbbToV%2BCLEmVz97rW8lDtFsXMATflbc4Dm6VLdwRed5%2FZv64FR6YHmDouSwNxdnguFv8QdCxKAZvw8pygyRuaqIDxNsNOpaBw2GAbncxkFQdjTDE1qNIlRsGcMU2AQ4gJjr9dPDhjQzKxRYI8qab7zbReFUCLiVyv7FaUcGg0w%2FSfvj7NBp4z2xFHLXgNOEHYCYBOFVNYmeIQxcZsmWZufEPV1Hz3vdlbAEXp2WHL1cfpjbEz8Z3uVChUxPpCe%2Bc4BuxO7WBJiD7PRuEO9fK3sYw9VepNPDwIApnPl9GzJI4sAp6y22V1LzJscv9A5GMkM0rwAX5M5S6SQv9xW9eLA3ynouGd3n8uV8f01i1COOz4N57qxQpVMkp5780rJqe53HHAu9ZU%2BGldAXtpIEB2JcX8nxIg%2Fc2rWSYJ3OKuCMOJGQuWIPHKC3bOsBbSEpGSHOoVOSKXQ39leg5lzLruAEcwjsD4vAY6pgG3R%2B6MwbQvt6VU2iq6ramX2QmCXGfqer6JUcOzzA4CBILGSRt0V0NR21dt0CKhqxZ56ZdZUTQ%2Bz45%2BkwR%2F7kuxb6tvulAIrqESLVtGuaV7iqgY%2Fuz6wxImUhsYiPnFOXphmIRAmPOleeNBORAXYfjxvWGicknSvYcdojN34T76gHD2PK4Nh1MBi660CRo2ktMHLk3FCkDdKl0opr8wUDC8umpu1CYo&X-Amz-Signature=821763b6b16abcf72919ad2e36268255d3d60cf4080f6b8c744dd1f6e7e66ce6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQNZFND%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIxTvnLVpYq2qR2Lmzrf8lHQuiT2J4%2B8F3eH4JM%2BwuLAiAI1LSfdXmkM0wF6qReW2eNbxjRrYNk1kncjuC%2FKaxp0SqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnZDbA6I4UCy%2BjafqKtwDvjThQrRrdwwp%2FRYI2POlkGAvwpgAWtz2XNGWM1HlFys9LsH6GgFto6qpGh9zfHKkBQ%2BAqgMjOXhRNonyHLTQXTDd53HHZS7eiAdUpjzGd8A52OMuBpl7rspJwCa3TfEfBpbByl6xYju7X4XnjbtTd2kcnXQZ7kphp5hQbbToV%2BCLEmVz97rW8lDtFsXMATflbc4Dm6VLdwRed5%2FZv64FR6YHmDouSwNxdnguFv8QdCxKAZvw8pygyRuaqIDxNsNOpaBw2GAbncxkFQdjTDE1qNIlRsGcMU2AQ4gJjr9dPDhjQzKxRYI8qab7zbReFUCLiVyv7FaUcGg0w%2FSfvj7NBp4z2xFHLXgNOEHYCYBOFVNYmeIQxcZsmWZufEPV1Hz3vdlbAEXp2WHL1cfpjbEz8Z3uVChUxPpCe%2Bc4BuxO7WBJiD7PRuEO9fK3sYw9VepNPDwIApnPl9GzJI4sAp6y22V1LzJscv9A5GMkM0rwAX5M5S6SQv9xW9eLA3ynouGd3n8uV8f01i1COOz4N57qxQpVMkp5780rJqe53HHAu9ZU%2BGldAXtpIEB2JcX8nxIg%2Fc2rWSYJ3OKuCMOJGQuWIPHKC3bOsBbSEpGSHOoVOSKXQ39leg5lzLruAEcwjsD4vAY6pgG3R%2B6MwbQvt6VU2iq6ramX2QmCXGfqer6JUcOzzA4CBILGSRt0V0NR21dt0CKhqxZ56ZdZUTQ%2Bz45%2BkwR%2F7kuxb6tvulAIrqESLVtGuaV7iqgY%2Fuz6wxImUhsYiPnFOXphmIRAmPOleeNBORAXYfjxvWGicknSvYcdojN34T76gHD2PK4Nh1MBi660CRo2ktMHLk3FCkDdKl0opr8wUDC8umpu1CYo&X-Amz-Signature=8a2e434fe06f8e3c9667c4ddb7bae279582f69597d5973036386885e5e2808f9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQNZFND%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIxTvnLVpYq2qR2Lmzrf8lHQuiT2J4%2B8F3eH4JM%2BwuLAiAI1LSfdXmkM0wF6qReW2eNbxjRrYNk1kncjuC%2FKaxp0SqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnZDbA6I4UCy%2BjafqKtwDvjThQrRrdwwp%2FRYI2POlkGAvwpgAWtz2XNGWM1HlFys9LsH6GgFto6qpGh9zfHKkBQ%2BAqgMjOXhRNonyHLTQXTDd53HHZS7eiAdUpjzGd8A52OMuBpl7rspJwCa3TfEfBpbByl6xYju7X4XnjbtTd2kcnXQZ7kphp5hQbbToV%2BCLEmVz97rW8lDtFsXMATflbc4Dm6VLdwRed5%2FZv64FR6YHmDouSwNxdnguFv8QdCxKAZvw8pygyRuaqIDxNsNOpaBw2GAbncxkFQdjTDE1qNIlRsGcMU2AQ4gJjr9dPDhjQzKxRYI8qab7zbReFUCLiVyv7FaUcGg0w%2FSfvj7NBp4z2xFHLXgNOEHYCYBOFVNYmeIQxcZsmWZufEPV1Hz3vdlbAEXp2WHL1cfpjbEz8Z3uVChUxPpCe%2Bc4BuxO7WBJiD7PRuEO9fK3sYw9VepNPDwIApnPl9GzJI4sAp6y22V1LzJscv9A5GMkM0rwAX5M5S6SQv9xW9eLA3ynouGd3n8uV8f01i1COOz4N57qxQpVMkp5780rJqe53HHAu9ZU%2BGldAXtpIEB2JcX8nxIg%2Fc2rWSYJ3OKuCMOJGQuWIPHKC3bOsBbSEpGSHOoVOSKXQ39leg5lzLruAEcwjsD4vAY6pgG3R%2B6MwbQvt6VU2iq6ramX2QmCXGfqer6JUcOzzA4CBILGSRt0V0NR21dt0CKhqxZ56ZdZUTQ%2Bz45%2BkwR%2F7kuxb6tvulAIrqESLVtGuaV7iqgY%2Fuz6wxImUhsYiPnFOXphmIRAmPOleeNBORAXYfjxvWGicknSvYcdojN34T76gHD2PK4Nh1MBi660CRo2ktMHLk3FCkDdKl0opr8wUDC8umpu1CYo&X-Amz-Signature=091db5977dd3371f1609761399660b1e2d7671bd0cd86a4f1abeb967cbe86bbc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQNZFND%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIxTvnLVpYq2qR2Lmzrf8lHQuiT2J4%2B8F3eH4JM%2BwuLAiAI1LSfdXmkM0wF6qReW2eNbxjRrYNk1kncjuC%2FKaxp0SqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnZDbA6I4UCy%2BjafqKtwDvjThQrRrdwwp%2FRYI2POlkGAvwpgAWtz2XNGWM1HlFys9LsH6GgFto6qpGh9zfHKkBQ%2BAqgMjOXhRNonyHLTQXTDd53HHZS7eiAdUpjzGd8A52OMuBpl7rspJwCa3TfEfBpbByl6xYju7X4XnjbtTd2kcnXQZ7kphp5hQbbToV%2BCLEmVz97rW8lDtFsXMATflbc4Dm6VLdwRed5%2FZv64FR6YHmDouSwNxdnguFv8QdCxKAZvw8pygyRuaqIDxNsNOpaBw2GAbncxkFQdjTDE1qNIlRsGcMU2AQ4gJjr9dPDhjQzKxRYI8qab7zbReFUCLiVyv7FaUcGg0w%2FSfvj7NBp4z2xFHLXgNOEHYCYBOFVNYmeIQxcZsmWZufEPV1Hz3vdlbAEXp2WHL1cfpjbEz8Z3uVChUxPpCe%2Bc4BuxO7WBJiD7PRuEO9fK3sYw9VepNPDwIApnPl9GzJI4sAp6y22V1LzJscv9A5GMkM0rwAX5M5S6SQv9xW9eLA3ynouGd3n8uV8f01i1COOz4N57qxQpVMkp5780rJqe53HHAu9ZU%2BGldAXtpIEB2JcX8nxIg%2Fc2rWSYJ3OKuCMOJGQuWIPHKC3bOsBbSEpGSHOoVOSKXQ39leg5lzLruAEcwjsD4vAY6pgG3R%2B6MwbQvt6VU2iq6ramX2QmCXGfqer6JUcOzzA4CBILGSRt0V0NR21dt0CKhqxZ56ZdZUTQ%2Bz45%2BkwR%2F7kuxb6tvulAIrqESLVtGuaV7iqgY%2Fuz6wxImUhsYiPnFOXphmIRAmPOleeNBORAXYfjxvWGicknSvYcdojN34T76gHD2PK4Nh1MBi660CRo2ktMHLk3FCkDdKl0opr8wUDC8umpu1CYo&X-Amz-Signature=50d36e66d3476cbd235cd2a450f17b5ed488b20491e45cbc1e71992d3e5521a1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQNZFND%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIxTvnLVpYq2qR2Lmzrf8lHQuiT2J4%2B8F3eH4JM%2BwuLAiAI1LSfdXmkM0wF6qReW2eNbxjRrYNk1kncjuC%2FKaxp0SqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnZDbA6I4UCy%2BjafqKtwDvjThQrRrdwwp%2FRYI2POlkGAvwpgAWtz2XNGWM1HlFys9LsH6GgFto6qpGh9zfHKkBQ%2BAqgMjOXhRNonyHLTQXTDd53HHZS7eiAdUpjzGd8A52OMuBpl7rspJwCa3TfEfBpbByl6xYju7X4XnjbtTd2kcnXQZ7kphp5hQbbToV%2BCLEmVz97rW8lDtFsXMATflbc4Dm6VLdwRed5%2FZv64FR6YHmDouSwNxdnguFv8QdCxKAZvw8pygyRuaqIDxNsNOpaBw2GAbncxkFQdjTDE1qNIlRsGcMU2AQ4gJjr9dPDhjQzKxRYI8qab7zbReFUCLiVyv7FaUcGg0w%2FSfvj7NBp4z2xFHLXgNOEHYCYBOFVNYmeIQxcZsmWZufEPV1Hz3vdlbAEXp2WHL1cfpjbEz8Z3uVChUxPpCe%2Bc4BuxO7WBJiD7PRuEO9fK3sYw9VepNPDwIApnPl9GzJI4sAp6y22V1LzJscv9A5GMkM0rwAX5M5S6SQv9xW9eLA3ynouGd3n8uV8f01i1COOz4N57qxQpVMkp5780rJqe53HHAu9ZU%2BGldAXtpIEB2JcX8nxIg%2Fc2rWSYJ3OKuCMOJGQuWIPHKC3bOsBbSEpGSHOoVOSKXQ39leg5lzLruAEcwjsD4vAY6pgG3R%2B6MwbQvt6VU2iq6ramX2QmCXGfqer6JUcOzzA4CBILGSRt0V0NR21dt0CKhqxZ56ZdZUTQ%2Bz45%2BkwR%2F7kuxb6tvulAIrqESLVtGuaV7iqgY%2Fuz6wxImUhsYiPnFOXphmIRAmPOleeNBORAXYfjxvWGicknSvYcdojN34T76gHD2PK4Nh1MBi660CRo2ktMHLk3FCkDdKl0opr8wUDC8umpu1CYo&X-Amz-Signature=d413fdce0d3a56682c35168fa526b48c6c481762696f83ffe42260c08bf75606&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQNZFND%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIxTvnLVpYq2qR2Lmzrf8lHQuiT2J4%2B8F3eH4JM%2BwuLAiAI1LSfdXmkM0wF6qReW2eNbxjRrYNk1kncjuC%2FKaxp0SqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnZDbA6I4UCy%2BjafqKtwDvjThQrRrdwwp%2FRYI2POlkGAvwpgAWtz2XNGWM1HlFys9LsH6GgFto6qpGh9zfHKkBQ%2BAqgMjOXhRNonyHLTQXTDd53HHZS7eiAdUpjzGd8A52OMuBpl7rspJwCa3TfEfBpbByl6xYju7X4XnjbtTd2kcnXQZ7kphp5hQbbToV%2BCLEmVz97rW8lDtFsXMATflbc4Dm6VLdwRed5%2FZv64FR6YHmDouSwNxdnguFv8QdCxKAZvw8pygyRuaqIDxNsNOpaBw2GAbncxkFQdjTDE1qNIlRsGcMU2AQ4gJjr9dPDhjQzKxRYI8qab7zbReFUCLiVyv7FaUcGg0w%2FSfvj7NBp4z2xFHLXgNOEHYCYBOFVNYmeIQxcZsmWZufEPV1Hz3vdlbAEXp2WHL1cfpjbEz8Z3uVChUxPpCe%2Bc4BuxO7WBJiD7PRuEO9fK3sYw9VepNPDwIApnPl9GzJI4sAp6y22V1LzJscv9A5GMkM0rwAX5M5S6SQv9xW9eLA3ynouGd3n8uV8f01i1COOz4N57qxQpVMkp5780rJqe53HHAu9ZU%2BGldAXtpIEB2JcX8nxIg%2Fc2rWSYJ3OKuCMOJGQuWIPHKC3bOsBbSEpGSHOoVOSKXQ39leg5lzLruAEcwjsD4vAY6pgG3R%2B6MwbQvt6VU2iq6ramX2QmCXGfqer6JUcOzzA4CBILGSRt0V0NR21dt0CKhqxZ56ZdZUTQ%2Bz45%2BkwR%2F7kuxb6tvulAIrqESLVtGuaV7iqgY%2Fuz6wxImUhsYiPnFOXphmIRAmPOleeNBORAXYfjxvWGicknSvYcdojN34T76gHD2PK4Nh1MBi660CRo2ktMHLk3FCkDdKl0opr8wUDC8umpu1CYo&X-Amz-Signature=3308789a5321e19c363a3ad3fe404c8fae42df2361437e07c55310ba6fa1d554&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQNZFND%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIxTvnLVpYq2qR2Lmzrf8lHQuiT2J4%2B8F3eH4JM%2BwuLAiAI1LSfdXmkM0wF6qReW2eNbxjRrYNk1kncjuC%2FKaxp0SqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnZDbA6I4UCy%2BjafqKtwDvjThQrRrdwwp%2FRYI2POlkGAvwpgAWtz2XNGWM1HlFys9LsH6GgFto6qpGh9zfHKkBQ%2BAqgMjOXhRNonyHLTQXTDd53HHZS7eiAdUpjzGd8A52OMuBpl7rspJwCa3TfEfBpbByl6xYju7X4XnjbtTd2kcnXQZ7kphp5hQbbToV%2BCLEmVz97rW8lDtFsXMATflbc4Dm6VLdwRed5%2FZv64FR6YHmDouSwNxdnguFv8QdCxKAZvw8pygyRuaqIDxNsNOpaBw2GAbncxkFQdjTDE1qNIlRsGcMU2AQ4gJjr9dPDhjQzKxRYI8qab7zbReFUCLiVyv7FaUcGg0w%2FSfvj7NBp4z2xFHLXgNOEHYCYBOFVNYmeIQxcZsmWZufEPV1Hz3vdlbAEXp2WHL1cfpjbEz8Z3uVChUxPpCe%2Bc4BuxO7WBJiD7PRuEO9fK3sYw9VepNPDwIApnPl9GzJI4sAp6y22V1LzJscv9A5GMkM0rwAX5M5S6SQv9xW9eLA3ynouGd3n8uV8f01i1COOz4N57qxQpVMkp5780rJqe53HHAu9ZU%2BGldAXtpIEB2JcX8nxIg%2Fc2rWSYJ3OKuCMOJGQuWIPHKC3bOsBbSEpGSHOoVOSKXQ39leg5lzLruAEcwjsD4vAY6pgG3R%2B6MwbQvt6VU2iq6ramX2QmCXGfqer6JUcOzzA4CBILGSRt0V0NR21dt0CKhqxZ56ZdZUTQ%2Bz45%2BkwR%2F7kuxb6tvulAIrqESLVtGuaV7iqgY%2Fuz6wxImUhsYiPnFOXphmIRAmPOleeNBORAXYfjxvWGicknSvYcdojN34T76gHD2PK4Nh1MBi660CRo2ktMHLk3FCkDdKl0opr8wUDC8umpu1CYo&X-Amz-Signature=c93a29d3e2504e368088c44130ed2113713d458c20da3041af19238944f1e120&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQNZFND%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIxTvnLVpYq2qR2Lmzrf8lHQuiT2J4%2B8F3eH4JM%2BwuLAiAI1LSfdXmkM0wF6qReW2eNbxjRrYNk1kncjuC%2FKaxp0SqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnZDbA6I4UCy%2BjafqKtwDvjThQrRrdwwp%2FRYI2POlkGAvwpgAWtz2XNGWM1HlFys9LsH6GgFto6qpGh9zfHKkBQ%2BAqgMjOXhRNonyHLTQXTDd53HHZS7eiAdUpjzGd8A52OMuBpl7rspJwCa3TfEfBpbByl6xYju7X4XnjbtTd2kcnXQZ7kphp5hQbbToV%2BCLEmVz97rW8lDtFsXMATflbc4Dm6VLdwRed5%2FZv64FR6YHmDouSwNxdnguFv8QdCxKAZvw8pygyRuaqIDxNsNOpaBw2GAbncxkFQdjTDE1qNIlRsGcMU2AQ4gJjr9dPDhjQzKxRYI8qab7zbReFUCLiVyv7FaUcGg0w%2FSfvj7NBp4z2xFHLXgNOEHYCYBOFVNYmeIQxcZsmWZufEPV1Hz3vdlbAEXp2WHL1cfpjbEz8Z3uVChUxPpCe%2Bc4BuxO7WBJiD7PRuEO9fK3sYw9VepNPDwIApnPl9GzJI4sAp6y22V1LzJscv9A5GMkM0rwAX5M5S6SQv9xW9eLA3ynouGd3n8uV8f01i1COOz4N57qxQpVMkp5780rJqe53HHAu9ZU%2BGldAXtpIEB2JcX8nxIg%2Fc2rWSYJ3OKuCMOJGQuWIPHKC3bOsBbSEpGSHOoVOSKXQ39leg5lzLruAEcwjsD4vAY6pgG3R%2B6MwbQvt6VU2iq6ramX2QmCXGfqer6JUcOzzA4CBILGSRt0V0NR21dt0CKhqxZ56ZdZUTQ%2Bz45%2BkwR%2F7kuxb6tvulAIrqESLVtGuaV7iqgY%2Fuz6wxImUhsYiPnFOXphmIRAmPOleeNBORAXYfjxvWGicknSvYcdojN34T76gHD2PK4Nh1MBi660CRo2ktMHLk3FCkDdKl0opr8wUDC8umpu1CYo&X-Amz-Signature=26c8c455f93aaf174f84eafd3f6afa355d8b6746c6be5b9a0aec83152d391057&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQNZFND%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIxTvnLVpYq2qR2Lmzrf8lHQuiT2J4%2B8F3eH4JM%2BwuLAiAI1LSfdXmkM0wF6qReW2eNbxjRrYNk1kncjuC%2FKaxp0SqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnZDbA6I4UCy%2BjafqKtwDvjThQrRrdwwp%2FRYI2POlkGAvwpgAWtz2XNGWM1HlFys9LsH6GgFto6qpGh9zfHKkBQ%2BAqgMjOXhRNonyHLTQXTDd53HHZS7eiAdUpjzGd8A52OMuBpl7rspJwCa3TfEfBpbByl6xYju7X4XnjbtTd2kcnXQZ7kphp5hQbbToV%2BCLEmVz97rW8lDtFsXMATflbc4Dm6VLdwRed5%2FZv64FR6YHmDouSwNxdnguFv8QdCxKAZvw8pygyRuaqIDxNsNOpaBw2GAbncxkFQdjTDE1qNIlRsGcMU2AQ4gJjr9dPDhjQzKxRYI8qab7zbReFUCLiVyv7FaUcGg0w%2FSfvj7NBp4z2xFHLXgNOEHYCYBOFVNYmeIQxcZsmWZufEPV1Hz3vdlbAEXp2WHL1cfpjbEz8Z3uVChUxPpCe%2Bc4BuxO7WBJiD7PRuEO9fK3sYw9VepNPDwIApnPl9GzJI4sAp6y22V1LzJscv9A5GMkM0rwAX5M5S6SQv9xW9eLA3ynouGd3n8uV8f01i1COOz4N57qxQpVMkp5780rJqe53HHAu9ZU%2BGldAXtpIEB2JcX8nxIg%2Fc2rWSYJ3OKuCMOJGQuWIPHKC3bOsBbSEpGSHOoVOSKXQ39leg5lzLruAEcwjsD4vAY6pgG3R%2B6MwbQvt6VU2iq6ramX2QmCXGfqer6JUcOzzA4CBILGSRt0V0NR21dt0CKhqxZ56ZdZUTQ%2Bz45%2BkwR%2F7kuxb6tvulAIrqESLVtGuaV7iqgY%2Fuz6wxImUhsYiPnFOXphmIRAmPOleeNBORAXYfjxvWGicknSvYcdojN34T76gHD2PK4Nh1MBi660CRo2ktMHLk3FCkDdKl0opr8wUDC8umpu1CYo&X-Amz-Signature=a35d32b06cb51421686fc67e287ca7392a011a6782e176b55ace09ee28d624eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIDE2DJU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCr%2FiGAQfguDPmLNl6aS1Vc3svQLgOkEzWufXk9p2BkmwIgMeSzryHIYUGA0GMQ1tvMkALqmZ2Pl6FnVcmfCP0uhCAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPmq5w0ln4Fz4FlJ5ircA9ltkRiVT%2FTC5m2A29ffKBMJx2OhVHZxNFxlW313dRLoG91HLxYTvjkJ9QwwQ%2F1fEBf1m2fOG1%2B%2FVIg4QbwaQ8PH2%2Fki4B4UgVx0ngK9K%2FWkWV8IWWlL7Bg7x%2BZW3fqDW1DrDsgXi4zG%2BDp40opCeAe6PB6Z8uppzC9KhFpiqNGa%2Fg%2F0WQqZGqJRdYuSEL%2FIiVh1z1E8%2BAIMpAyjz%2B2hIT7cD7221TAWjtBTwo1aVmKXZ1czHDlrWigmwchC1sG5KDqGnqBVdWasN32v6ie%2FxNiUKas58FneVaY7%2FbHrjRoxeqBz%2BapX1lO%2FONxUC5llVhFUCih1oij%2FNgHpmCGhJsZLOsDaibhUIUnIqTJ02W5lstmcNJQTNJZO2Z0V8549LC09J9q%2B0vSYyNwMT13hTGmwLG8nU5aZZux4UsbTZzeKGRQmMIUiEKc28GLn8CZotPpRGkjs09jKFmwb9bEnuyqvbaaVuKTSxo28NFcbbEsuTNaFgrrO5S1iLWSaEkDTA3b%2Bmj3oxxpR25pUs%2FVdc99Ic50TFz0VD74CN2zes6Ybij%2F0OS0QIyFc9l3YM4KlyXA5yMZN6sDFa4h7bCZ2R5BG0q0O8vtkDiN7md8LWfx01Rg%2Bsud6ByBpZHR2MO69%2BLwGOqUBfC7H82ukYEMK2JRhDv2RcaPGpFopU9uZ%2F60Rrdg8MBpKAeGLW14sSyZqR%2BM5hRP8FgZe5b4gzAhdqp7yO7ZLm0sjYnkIWGQnNr3AhbbXut5cljfi0PdJlyADv6%2BDU3sjb5X1%2Bh%2FJ6TU0pe8ylRuObWO1B8dSmkW%2FbXhLMTksaLz7DvXMoFDCtWDtRypS%2BnoSxOZKwZwrxHIxG2%2BlqYtT%2BVJiUp7%2B&X-Amz-Signature=d8925f8710f2431ec87bc27e2c6595450f7f7d68c95f829dff95b395ff804e6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIDE2DJU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCr%2FiGAQfguDPmLNl6aS1Vc3svQLgOkEzWufXk9p2BkmwIgMeSzryHIYUGA0GMQ1tvMkALqmZ2Pl6FnVcmfCP0uhCAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPmq5w0ln4Fz4FlJ5ircA9ltkRiVT%2FTC5m2A29ffKBMJx2OhVHZxNFxlW313dRLoG91HLxYTvjkJ9QwwQ%2F1fEBf1m2fOG1%2B%2FVIg4QbwaQ8PH2%2Fki4B4UgVx0ngK9K%2FWkWV8IWWlL7Bg7x%2BZW3fqDW1DrDsgXi4zG%2BDp40opCeAe6PB6Z8uppzC9KhFpiqNGa%2Fg%2F0WQqZGqJRdYuSEL%2FIiVh1z1E8%2BAIMpAyjz%2B2hIT7cD7221TAWjtBTwo1aVmKXZ1czHDlrWigmwchC1sG5KDqGnqBVdWasN32v6ie%2FxNiUKas58FneVaY7%2FbHrjRoxeqBz%2BapX1lO%2FONxUC5llVhFUCih1oij%2FNgHpmCGhJsZLOsDaibhUIUnIqTJ02W5lstmcNJQTNJZO2Z0V8549LC09J9q%2B0vSYyNwMT13hTGmwLG8nU5aZZux4UsbTZzeKGRQmMIUiEKc28GLn8CZotPpRGkjs09jKFmwb9bEnuyqvbaaVuKTSxo28NFcbbEsuTNaFgrrO5S1iLWSaEkDTA3b%2Bmj3oxxpR25pUs%2FVdc99Ic50TFz0VD74CN2zes6Ybij%2F0OS0QIyFc9l3YM4KlyXA5yMZN6sDFa4h7bCZ2R5BG0q0O8vtkDiN7md8LWfx01Rg%2Bsud6ByBpZHR2MO69%2BLwGOqUBfC7H82ukYEMK2JRhDv2RcaPGpFopU9uZ%2F60Rrdg8MBpKAeGLW14sSyZqR%2BM5hRP8FgZe5b4gzAhdqp7yO7ZLm0sjYnkIWGQnNr3AhbbXut5cljfi0PdJlyADv6%2BDU3sjb5X1%2Bh%2FJ6TU0pe8ylRuObWO1B8dSmkW%2FbXhLMTksaLz7DvXMoFDCtWDtRypS%2BnoSxOZKwZwrxHIxG2%2BlqYtT%2BVJiUp7%2B&X-Amz-Signature=a347e31f2ce2bb77e7e46eeec79d79942ecc7cb4a0951faae56746fa345bb137&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
