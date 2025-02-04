

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SYE7TML%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDDy2JYqo1Yv1FT2Qhpd78zcm6Bu26gQrBGCp7loga7awIgd2FbArdaN%2Bv%2BHVgsk02T7%2BcQC5jVrQJ3HuBCTdcL4VQq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDPETwsKAj%2FjXl6AxpyrcA8NrEYVaIjaLetLYiQCGPOipAkeTjTtFYuizAzigvIMzUKQP1apDsVxIi1O7ANB4aKcbZvnKP%2FyfBsRfCfGeHUJBcoM4A3kN6t3SOQG6zN7R%2BgW5rl79c6W2BegOVW1Lvd6Rek36xiNZ73x192B6gyIHIECCswqh08i69NUq9nn902nsWqlvGZXRN4RjlRcmMFY%2BWmoiCVtiVqksnZU2In2IJrShe6u%2BHzp11n%2FV8SUZbecPNrLFfzJEkgJvvNWQ3UbkOgCY%2FJBuwONNFZUNbXIBfXip1VfeD3YA1nqV4n5fLPL65SaZR33JoDPnClMVJvagB5Q%2FIPR%2B1XQiDGh8tcrE89dLC0YXmoG6sMfvp9SO2OjGBjmsr18KtfMVlvXzE6RCq8GT7cWyfFP8UWLhNbLW%2FeQs7lIyheYkHWqu9waCi4V%2B%2FW7WPXy%2ByJDfFWnZhG%2BM33Tag7p7nafpOVy1s8EZ9tTnwo1WFwyC2Du7A5fnP5h%2FoJP38tp9Cj26mjZLUta9e%2BCvqQ0kjG%2FyjoWgq25rswsp%2FXWDLu71XjtghOzFvFe5p53Zv36uH1Yvm6G0Aai5dmi31YfNomUrtdLnyhLLj9jIBOlOstSu4VbNNgPK37GCesjANFi%2FctW6MJaDiL0GOqUBKXmq58fWCV%2BWeLpx3QZ%2BHcKn%2BKIpOfMW%2F24WWZBfu9HuTIsjFUi7lwEokfL5%2BA0AC4FWvbOefZpeuZ%2FZcVLjBEVPW%2FMpcFL%2FD1upDVv96rAUYCBvkf7SE6L9Imvk4V6IKNo3Tbc76x7FYaX7%2BFHNQTIeVz1%2Fy30bHMv%2Bs4wWmBJB2%2FrFyECPcOSXhGDhH3JunivvxeKzYh03Pm2Xje5uclt6nRsQ&X-Amz-Signature=8ef9ae7282a6e4128f11e1126441f9312daee7a277afd96bdee24319b534bb63&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SYE7TML%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDDy2JYqo1Yv1FT2Qhpd78zcm6Bu26gQrBGCp7loga7awIgd2FbArdaN%2Bv%2BHVgsk02T7%2BcQC5jVrQJ3HuBCTdcL4VQq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDPETwsKAj%2FjXl6AxpyrcA8NrEYVaIjaLetLYiQCGPOipAkeTjTtFYuizAzigvIMzUKQP1apDsVxIi1O7ANB4aKcbZvnKP%2FyfBsRfCfGeHUJBcoM4A3kN6t3SOQG6zN7R%2BgW5rl79c6W2BegOVW1Lvd6Rek36xiNZ73x192B6gyIHIECCswqh08i69NUq9nn902nsWqlvGZXRN4RjlRcmMFY%2BWmoiCVtiVqksnZU2In2IJrShe6u%2BHzp11n%2FV8SUZbecPNrLFfzJEkgJvvNWQ3UbkOgCY%2FJBuwONNFZUNbXIBfXip1VfeD3YA1nqV4n5fLPL65SaZR33JoDPnClMVJvagB5Q%2FIPR%2B1XQiDGh8tcrE89dLC0YXmoG6sMfvp9SO2OjGBjmsr18KtfMVlvXzE6RCq8GT7cWyfFP8UWLhNbLW%2FeQs7lIyheYkHWqu9waCi4V%2B%2FW7WPXy%2ByJDfFWnZhG%2BM33Tag7p7nafpOVy1s8EZ9tTnwo1WFwyC2Du7A5fnP5h%2FoJP38tp9Cj26mjZLUta9e%2BCvqQ0kjG%2FyjoWgq25rswsp%2FXWDLu71XjtghOzFvFe5p53Zv36uH1Yvm6G0Aai5dmi31YfNomUrtdLnyhLLj9jIBOlOstSu4VbNNgPK37GCesjANFi%2FctW6MJaDiL0GOqUBKXmq58fWCV%2BWeLpx3QZ%2BHcKn%2BKIpOfMW%2F24WWZBfu9HuTIsjFUi7lwEokfL5%2BA0AC4FWvbOefZpeuZ%2FZcVLjBEVPW%2FMpcFL%2FD1upDVv96rAUYCBvkf7SE6L9Imvk4V6IKNo3Tbc76x7FYaX7%2BFHNQTIeVz1%2Fy30bHMv%2Bs4wWmBJB2%2FrFyECPcOSXhGDhH3JunivvxeKzYh03Pm2Xje5uclt6nRsQ&X-Amz-Signature=83048a78ed795abaa13645c8be7d9fbbbcfddbec826e1e5edc86d3ebd276f337&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SYE7TML%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDDy2JYqo1Yv1FT2Qhpd78zcm6Bu26gQrBGCp7loga7awIgd2FbArdaN%2Bv%2BHVgsk02T7%2BcQC5jVrQJ3HuBCTdcL4VQq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDPETwsKAj%2FjXl6AxpyrcA8NrEYVaIjaLetLYiQCGPOipAkeTjTtFYuizAzigvIMzUKQP1apDsVxIi1O7ANB4aKcbZvnKP%2FyfBsRfCfGeHUJBcoM4A3kN6t3SOQG6zN7R%2BgW5rl79c6W2BegOVW1Lvd6Rek36xiNZ73x192B6gyIHIECCswqh08i69NUq9nn902nsWqlvGZXRN4RjlRcmMFY%2BWmoiCVtiVqksnZU2In2IJrShe6u%2BHzp11n%2FV8SUZbecPNrLFfzJEkgJvvNWQ3UbkOgCY%2FJBuwONNFZUNbXIBfXip1VfeD3YA1nqV4n5fLPL65SaZR33JoDPnClMVJvagB5Q%2FIPR%2B1XQiDGh8tcrE89dLC0YXmoG6sMfvp9SO2OjGBjmsr18KtfMVlvXzE6RCq8GT7cWyfFP8UWLhNbLW%2FeQs7lIyheYkHWqu9waCi4V%2B%2FW7WPXy%2ByJDfFWnZhG%2BM33Tag7p7nafpOVy1s8EZ9tTnwo1WFwyC2Du7A5fnP5h%2FoJP38tp9Cj26mjZLUta9e%2BCvqQ0kjG%2FyjoWgq25rswsp%2FXWDLu71XjtghOzFvFe5p53Zv36uH1Yvm6G0Aai5dmi31YfNomUrtdLnyhLLj9jIBOlOstSu4VbNNgPK37GCesjANFi%2FctW6MJaDiL0GOqUBKXmq58fWCV%2BWeLpx3QZ%2BHcKn%2BKIpOfMW%2F24WWZBfu9HuTIsjFUi7lwEokfL5%2BA0AC4FWvbOefZpeuZ%2FZcVLjBEVPW%2FMpcFL%2FD1upDVv96rAUYCBvkf7SE6L9Imvk4V6IKNo3Tbc76x7FYaX7%2BFHNQTIeVz1%2Fy30bHMv%2Bs4wWmBJB2%2FrFyECPcOSXhGDhH3JunivvxeKzYh03Pm2Xje5uclt6nRsQ&X-Amz-Signature=f18bf1ac2d0b55dbb39a4ad7509cd1ea7cd552557736b657ec13db46fac18993&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SYE7TML%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDDy2JYqo1Yv1FT2Qhpd78zcm6Bu26gQrBGCp7loga7awIgd2FbArdaN%2Bv%2BHVgsk02T7%2BcQC5jVrQJ3HuBCTdcL4VQq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDPETwsKAj%2FjXl6AxpyrcA8NrEYVaIjaLetLYiQCGPOipAkeTjTtFYuizAzigvIMzUKQP1apDsVxIi1O7ANB4aKcbZvnKP%2FyfBsRfCfGeHUJBcoM4A3kN6t3SOQG6zN7R%2BgW5rl79c6W2BegOVW1Lvd6Rek36xiNZ73x192B6gyIHIECCswqh08i69NUq9nn902nsWqlvGZXRN4RjlRcmMFY%2BWmoiCVtiVqksnZU2In2IJrShe6u%2BHzp11n%2FV8SUZbecPNrLFfzJEkgJvvNWQ3UbkOgCY%2FJBuwONNFZUNbXIBfXip1VfeD3YA1nqV4n5fLPL65SaZR33JoDPnClMVJvagB5Q%2FIPR%2B1XQiDGh8tcrE89dLC0YXmoG6sMfvp9SO2OjGBjmsr18KtfMVlvXzE6RCq8GT7cWyfFP8UWLhNbLW%2FeQs7lIyheYkHWqu9waCi4V%2B%2FW7WPXy%2ByJDfFWnZhG%2BM33Tag7p7nafpOVy1s8EZ9tTnwo1WFwyC2Du7A5fnP5h%2FoJP38tp9Cj26mjZLUta9e%2BCvqQ0kjG%2FyjoWgq25rswsp%2FXWDLu71XjtghOzFvFe5p53Zv36uH1Yvm6G0Aai5dmi31YfNomUrtdLnyhLLj9jIBOlOstSu4VbNNgPK37GCesjANFi%2FctW6MJaDiL0GOqUBKXmq58fWCV%2BWeLpx3QZ%2BHcKn%2BKIpOfMW%2F24WWZBfu9HuTIsjFUi7lwEokfL5%2BA0AC4FWvbOefZpeuZ%2FZcVLjBEVPW%2FMpcFL%2FD1upDVv96rAUYCBvkf7SE6L9Imvk4V6IKNo3Tbc76x7FYaX7%2BFHNQTIeVz1%2Fy30bHMv%2Bs4wWmBJB2%2FrFyECPcOSXhGDhH3JunivvxeKzYh03Pm2Xje5uclt6nRsQ&X-Amz-Signature=d60dbae59c62c2e3fd56a94448f6320358632b15369c2f8d41a3d75cab2b026e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SYE7TML%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDDy2JYqo1Yv1FT2Qhpd78zcm6Bu26gQrBGCp7loga7awIgd2FbArdaN%2Bv%2BHVgsk02T7%2BcQC5jVrQJ3HuBCTdcL4VQq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDPETwsKAj%2FjXl6AxpyrcA8NrEYVaIjaLetLYiQCGPOipAkeTjTtFYuizAzigvIMzUKQP1apDsVxIi1O7ANB4aKcbZvnKP%2FyfBsRfCfGeHUJBcoM4A3kN6t3SOQG6zN7R%2BgW5rl79c6W2BegOVW1Lvd6Rek36xiNZ73x192B6gyIHIECCswqh08i69NUq9nn902nsWqlvGZXRN4RjlRcmMFY%2BWmoiCVtiVqksnZU2In2IJrShe6u%2BHzp11n%2FV8SUZbecPNrLFfzJEkgJvvNWQ3UbkOgCY%2FJBuwONNFZUNbXIBfXip1VfeD3YA1nqV4n5fLPL65SaZR33JoDPnClMVJvagB5Q%2FIPR%2B1XQiDGh8tcrE89dLC0YXmoG6sMfvp9SO2OjGBjmsr18KtfMVlvXzE6RCq8GT7cWyfFP8UWLhNbLW%2FeQs7lIyheYkHWqu9waCi4V%2B%2FW7WPXy%2ByJDfFWnZhG%2BM33Tag7p7nafpOVy1s8EZ9tTnwo1WFwyC2Du7A5fnP5h%2FoJP38tp9Cj26mjZLUta9e%2BCvqQ0kjG%2FyjoWgq25rswsp%2FXWDLu71XjtghOzFvFe5p53Zv36uH1Yvm6G0Aai5dmi31YfNomUrtdLnyhLLj9jIBOlOstSu4VbNNgPK37GCesjANFi%2FctW6MJaDiL0GOqUBKXmq58fWCV%2BWeLpx3QZ%2BHcKn%2BKIpOfMW%2F24WWZBfu9HuTIsjFUi7lwEokfL5%2BA0AC4FWvbOefZpeuZ%2FZcVLjBEVPW%2FMpcFL%2FD1upDVv96rAUYCBvkf7SE6L9Imvk4V6IKNo3Tbc76x7FYaX7%2BFHNQTIeVz1%2Fy30bHMv%2Bs4wWmBJB2%2FrFyECPcOSXhGDhH3JunivvxeKzYh03Pm2Xje5uclt6nRsQ&X-Amz-Signature=4bd84698ca8dfbd619e64028ec2ce1d636530044a4a8b488c3a9e95f363189af&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SYE7TML%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDDy2JYqo1Yv1FT2Qhpd78zcm6Bu26gQrBGCp7loga7awIgd2FbArdaN%2Bv%2BHVgsk02T7%2BcQC5jVrQJ3HuBCTdcL4VQq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDPETwsKAj%2FjXl6AxpyrcA8NrEYVaIjaLetLYiQCGPOipAkeTjTtFYuizAzigvIMzUKQP1apDsVxIi1O7ANB4aKcbZvnKP%2FyfBsRfCfGeHUJBcoM4A3kN6t3SOQG6zN7R%2BgW5rl79c6W2BegOVW1Lvd6Rek36xiNZ73x192B6gyIHIECCswqh08i69NUq9nn902nsWqlvGZXRN4RjlRcmMFY%2BWmoiCVtiVqksnZU2In2IJrShe6u%2BHzp11n%2FV8SUZbecPNrLFfzJEkgJvvNWQ3UbkOgCY%2FJBuwONNFZUNbXIBfXip1VfeD3YA1nqV4n5fLPL65SaZR33JoDPnClMVJvagB5Q%2FIPR%2B1XQiDGh8tcrE89dLC0YXmoG6sMfvp9SO2OjGBjmsr18KtfMVlvXzE6RCq8GT7cWyfFP8UWLhNbLW%2FeQs7lIyheYkHWqu9waCi4V%2B%2FW7WPXy%2ByJDfFWnZhG%2BM33Tag7p7nafpOVy1s8EZ9tTnwo1WFwyC2Du7A5fnP5h%2FoJP38tp9Cj26mjZLUta9e%2BCvqQ0kjG%2FyjoWgq25rswsp%2FXWDLu71XjtghOzFvFe5p53Zv36uH1Yvm6G0Aai5dmi31YfNomUrtdLnyhLLj9jIBOlOstSu4VbNNgPK37GCesjANFi%2FctW6MJaDiL0GOqUBKXmq58fWCV%2BWeLpx3QZ%2BHcKn%2BKIpOfMW%2F24WWZBfu9HuTIsjFUi7lwEokfL5%2BA0AC4FWvbOefZpeuZ%2FZcVLjBEVPW%2FMpcFL%2FD1upDVv96rAUYCBvkf7SE6L9Imvk4V6IKNo3Tbc76x7FYaX7%2BFHNQTIeVz1%2Fy30bHMv%2Bs4wWmBJB2%2FrFyECPcOSXhGDhH3JunivvxeKzYh03Pm2Xje5uclt6nRsQ&X-Amz-Signature=a021e55d827d71431aa96a158e954458d3a870bc4ae15e4ba3cbd7802fa72446&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SYE7TML%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDDy2JYqo1Yv1FT2Qhpd78zcm6Bu26gQrBGCp7loga7awIgd2FbArdaN%2Bv%2BHVgsk02T7%2BcQC5jVrQJ3HuBCTdcL4VQq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDPETwsKAj%2FjXl6AxpyrcA8NrEYVaIjaLetLYiQCGPOipAkeTjTtFYuizAzigvIMzUKQP1apDsVxIi1O7ANB4aKcbZvnKP%2FyfBsRfCfGeHUJBcoM4A3kN6t3SOQG6zN7R%2BgW5rl79c6W2BegOVW1Lvd6Rek36xiNZ73x192B6gyIHIECCswqh08i69NUq9nn902nsWqlvGZXRN4RjlRcmMFY%2BWmoiCVtiVqksnZU2In2IJrShe6u%2BHzp11n%2FV8SUZbecPNrLFfzJEkgJvvNWQ3UbkOgCY%2FJBuwONNFZUNbXIBfXip1VfeD3YA1nqV4n5fLPL65SaZR33JoDPnClMVJvagB5Q%2FIPR%2B1XQiDGh8tcrE89dLC0YXmoG6sMfvp9SO2OjGBjmsr18KtfMVlvXzE6RCq8GT7cWyfFP8UWLhNbLW%2FeQs7lIyheYkHWqu9waCi4V%2B%2FW7WPXy%2ByJDfFWnZhG%2BM33Tag7p7nafpOVy1s8EZ9tTnwo1WFwyC2Du7A5fnP5h%2FoJP38tp9Cj26mjZLUta9e%2BCvqQ0kjG%2FyjoWgq25rswsp%2FXWDLu71XjtghOzFvFe5p53Zv36uH1Yvm6G0Aai5dmi31YfNomUrtdLnyhLLj9jIBOlOstSu4VbNNgPK37GCesjANFi%2FctW6MJaDiL0GOqUBKXmq58fWCV%2BWeLpx3QZ%2BHcKn%2BKIpOfMW%2F24WWZBfu9HuTIsjFUi7lwEokfL5%2BA0AC4FWvbOefZpeuZ%2FZcVLjBEVPW%2FMpcFL%2FD1upDVv96rAUYCBvkf7SE6L9Imvk4V6IKNo3Tbc76x7FYaX7%2BFHNQTIeVz1%2Fy30bHMv%2Bs4wWmBJB2%2FrFyECPcOSXhGDhH3JunivvxeKzYh03Pm2Xje5uclt6nRsQ&X-Amz-Signature=84ac5463b668e9109ac8ac2da9ced7733a95d32b62bcfc372d8a57ea1e0a08bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SYE7TML%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDDy2JYqo1Yv1FT2Qhpd78zcm6Bu26gQrBGCp7loga7awIgd2FbArdaN%2Bv%2BHVgsk02T7%2BcQC5jVrQJ3HuBCTdcL4VQq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDPETwsKAj%2FjXl6AxpyrcA8NrEYVaIjaLetLYiQCGPOipAkeTjTtFYuizAzigvIMzUKQP1apDsVxIi1O7ANB4aKcbZvnKP%2FyfBsRfCfGeHUJBcoM4A3kN6t3SOQG6zN7R%2BgW5rl79c6W2BegOVW1Lvd6Rek36xiNZ73x192B6gyIHIECCswqh08i69NUq9nn902nsWqlvGZXRN4RjlRcmMFY%2BWmoiCVtiVqksnZU2In2IJrShe6u%2BHzp11n%2FV8SUZbecPNrLFfzJEkgJvvNWQ3UbkOgCY%2FJBuwONNFZUNbXIBfXip1VfeD3YA1nqV4n5fLPL65SaZR33JoDPnClMVJvagB5Q%2FIPR%2B1XQiDGh8tcrE89dLC0YXmoG6sMfvp9SO2OjGBjmsr18KtfMVlvXzE6RCq8GT7cWyfFP8UWLhNbLW%2FeQs7lIyheYkHWqu9waCi4V%2B%2FW7WPXy%2ByJDfFWnZhG%2BM33Tag7p7nafpOVy1s8EZ9tTnwo1WFwyC2Du7A5fnP5h%2FoJP38tp9Cj26mjZLUta9e%2BCvqQ0kjG%2FyjoWgq25rswsp%2FXWDLu71XjtghOzFvFe5p53Zv36uH1Yvm6G0Aai5dmi31YfNomUrtdLnyhLLj9jIBOlOstSu4VbNNgPK37GCesjANFi%2FctW6MJaDiL0GOqUBKXmq58fWCV%2BWeLpx3QZ%2BHcKn%2BKIpOfMW%2F24WWZBfu9HuTIsjFUi7lwEokfL5%2BA0AC4FWvbOefZpeuZ%2FZcVLjBEVPW%2FMpcFL%2FD1upDVv96rAUYCBvkf7SE6L9Imvk4V6IKNo3Tbc76x7FYaX7%2BFHNQTIeVz1%2Fy30bHMv%2Bs4wWmBJB2%2FrFyECPcOSXhGDhH3JunivvxeKzYh03Pm2Xje5uclt6nRsQ&X-Amz-Signature=d96a883656e850b1a8df4e64ba5a301cade437947b26e31ae7f8edeafc330d45&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SYE7TML%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDDy2JYqo1Yv1FT2Qhpd78zcm6Bu26gQrBGCp7loga7awIgd2FbArdaN%2Bv%2BHVgsk02T7%2BcQC5jVrQJ3HuBCTdcL4VQq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDPETwsKAj%2FjXl6AxpyrcA8NrEYVaIjaLetLYiQCGPOipAkeTjTtFYuizAzigvIMzUKQP1apDsVxIi1O7ANB4aKcbZvnKP%2FyfBsRfCfGeHUJBcoM4A3kN6t3SOQG6zN7R%2BgW5rl79c6W2BegOVW1Lvd6Rek36xiNZ73x192B6gyIHIECCswqh08i69NUq9nn902nsWqlvGZXRN4RjlRcmMFY%2BWmoiCVtiVqksnZU2In2IJrShe6u%2BHzp11n%2FV8SUZbecPNrLFfzJEkgJvvNWQ3UbkOgCY%2FJBuwONNFZUNbXIBfXip1VfeD3YA1nqV4n5fLPL65SaZR33JoDPnClMVJvagB5Q%2FIPR%2B1XQiDGh8tcrE89dLC0YXmoG6sMfvp9SO2OjGBjmsr18KtfMVlvXzE6RCq8GT7cWyfFP8UWLhNbLW%2FeQs7lIyheYkHWqu9waCi4V%2B%2FW7WPXy%2ByJDfFWnZhG%2BM33Tag7p7nafpOVy1s8EZ9tTnwo1WFwyC2Du7A5fnP5h%2FoJP38tp9Cj26mjZLUta9e%2BCvqQ0kjG%2FyjoWgq25rswsp%2FXWDLu71XjtghOzFvFe5p53Zv36uH1Yvm6G0Aai5dmi31YfNomUrtdLnyhLLj9jIBOlOstSu4VbNNgPK37GCesjANFi%2FctW6MJaDiL0GOqUBKXmq58fWCV%2BWeLpx3QZ%2BHcKn%2BKIpOfMW%2F24WWZBfu9HuTIsjFUi7lwEokfL5%2BA0AC4FWvbOefZpeuZ%2FZcVLjBEVPW%2FMpcFL%2FD1upDVv96rAUYCBvkf7SE6L9Imvk4V6IKNo3Tbc76x7FYaX7%2BFHNQTIeVz1%2Fy30bHMv%2Bs4wWmBJB2%2FrFyECPcOSXhGDhH3JunivvxeKzYh03Pm2Xje5uclt6nRsQ&X-Amz-Signature=023cd2d3c9294dbbec4413903276700164d3654f916b862df88a93deb59e254e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SZKEM5H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDW6i6wVPsQug6%2FSvT64LfUeqme3dXHBsUGN%2BJxEa6ZMwIhAJNsqynbjhHo7mUA4Ol0N41R6KNJahFSPd0VRk9KQNNaKv8DCC0QABoMNjM3NDIzMTgzODA1IgzhRS%2BnNcxBXOkrOLEq3ANiFDp6RsM7ZmdqzwrZ3v%2F9D131gTybTLGwDuyJRH6OCPEhxyQE%2BGvrUIQpx%2BgF23wKhREjTTscW5inckClxsLEeWaJcMuImHhLUnTuDGnwH5B7KLDrx56osNlY4pqJ%2Bdcc71Oz%2BwBXz6enoXG6GfcXMxHQysQoocGt0fPpoSFS1iF9lNaf4m8tVeyYg0sPIsI95HW4dACM6F92g%2B0SkzPB5nsSFxSwiBKM%2Ft3gJRoMLQ%2FMydzB%2BubCyyPzE%2FLSFi08Bb9iT6oMTJYQTprDoodRy8ehFd3lFfvlPEG7qvYFj3RKo6A55yB1Lh8LfSuILhdq0Xhw0yMBsE5Ese9%2FbF4jmpxBGHWM1vjMb0Buk9EbJ8yujkNTzZCyKZiFhfGSprGKXOYpgb57uCmyMSf4%2BrY9UCDfIDc2Cy1joDAIvtyy2R7fhYu77YLXDszXv%2BsL2QjMBW%2BrX5qebeWxYNYtE13D638dGaz%2BaNfVhJajv3NWCA%2Fy0SAovniUeLcqlmHhkndmXXJDnvERKYXrFCRjVVINLuwkwvFueFuG%2F5S4Vz9ZlIFWR2lhncnB4qydpaltkPkq3S%2F%2BbyN5U6L%2F7s1roqho8NJ3YXryJMq1ok7rIcFcVX64zh9tbQG9UEWtbDCIgoi9BjqkAbZdaC9%2B0Ot%2FUPW4Nw8vQM4mKp8sSZZfd%2Bn45HMDzqjvYiQWgJRM1YiVsTMzXY6%2BmhoEaFnN5A7NioPZ3wwHKFHRyKsNO7sVz%2BIZpi5FsGaNkGZ8hCe%2BzYl%2BC%2FrJTmfLsdAmClndIX92QcznZ3w7IRbSA0nVrVeg%2FctYZZ2PLQ4RbcXhr32WaqQPv7qR9P64SMwDCP71Gxum1GO11Senke9h4VI9&X-Amz-Signature=bbab7c9eabb9821b42f9f8d5837332cc63afc9fea5744ba030fbffd355b1f393&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SZKEM5H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDW6i6wVPsQug6%2FSvT64LfUeqme3dXHBsUGN%2BJxEa6ZMwIhAJNsqynbjhHo7mUA4Ol0N41R6KNJahFSPd0VRk9KQNNaKv8DCC0QABoMNjM3NDIzMTgzODA1IgzhRS%2BnNcxBXOkrOLEq3ANiFDp6RsM7ZmdqzwrZ3v%2F9D131gTybTLGwDuyJRH6OCPEhxyQE%2BGvrUIQpx%2BgF23wKhREjTTscW5inckClxsLEeWaJcMuImHhLUnTuDGnwH5B7KLDrx56osNlY4pqJ%2Bdcc71Oz%2BwBXz6enoXG6GfcXMxHQysQoocGt0fPpoSFS1iF9lNaf4m8tVeyYg0sPIsI95HW4dACM6F92g%2B0SkzPB5nsSFxSwiBKM%2Ft3gJRoMLQ%2FMydzB%2BubCyyPzE%2FLSFi08Bb9iT6oMTJYQTprDoodRy8ehFd3lFfvlPEG7qvYFj3RKo6A55yB1Lh8LfSuILhdq0Xhw0yMBsE5Ese9%2FbF4jmpxBGHWM1vjMb0Buk9EbJ8yujkNTzZCyKZiFhfGSprGKXOYpgb57uCmyMSf4%2BrY9UCDfIDc2Cy1joDAIvtyy2R7fhYu77YLXDszXv%2BsL2QjMBW%2BrX5qebeWxYNYtE13D638dGaz%2BaNfVhJajv3NWCA%2Fy0SAovniUeLcqlmHhkndmXXJDnvERKYXrFCRjVVINLuwkwvFueFuG%2F5S4Vz9ZlIFWR2lhncnB4qydpaltkPkq3S%2F%2BbyN5U6L%2F7s1roqho8NJ3YXryJMq1ok7rIcFcVX64zh9tbQG9UEWtbDCIgoi9BjqkAbZdaC9%2B0Ot%2FUPW4Nw8vQM4mKp8sSZZfd%2Bn45HMDzqjvYiQWgJRM1YiVsTMzXY6%2BmhoEaFnN5A7NioPZ3wwHKFHRyKsNO7sVz%2BIZpi5FsGaNkGZ8hCe%2BzYl%2BC%2FrJTmfLsdAmClndIX92QcznZ3w7IRbSA0nVrVeg%2FctYZZ2PLQ4RbcXhr32WaqQPv7qR9P64SMwDCP71Gxum1GO11Senke9h4VI9&X-Amz-Signature=f5c8c8ff47ef555f17b527c2b0f4266b962d40a37aab4fe896289969d8506c28&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
