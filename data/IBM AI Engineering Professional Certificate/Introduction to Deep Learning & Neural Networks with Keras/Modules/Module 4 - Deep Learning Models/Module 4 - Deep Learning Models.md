

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=38b1e39837478910c38e82c3b8b4ce1e1eedce5e28436b13a2f35d055bc1098d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=6155456cea96fafc2f707770638321255a9f41fef2a197390cbf941df991c0b1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=b760c5f1c09b6991a71b9444c9397f9c455a52bbf7f89d698c1837a2375bdd4c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=146570f5e184c2f1cd2e715254fba37eb4f14595ef3f64079eed0d5178327f16&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=1f654861fca5f54f6921605aad9647d21699397739e74f114c7344b14775647c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=d17df801a301f51f25a73e29143446e7a897457fe0750df0f1688263b8c44378&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=a39f865c47e73c5d42b0eaeb36725c88672a03a65d1ea57592fd3f05b919bec4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=08ee0fd462df3752c557195b28b9587c7ebc615deca2b2bf539fbe26e356ec41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=9fb6f9bbd27a60be8e025a3cb28dc3996848e34609cb2d54c1d47960f3c02998&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FXKNCQB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDflaFvZaHCcDxV%2FFOePNkO%2BOr0KkT0COsLpkEIVOSbYwIgGFzgYfVW4ZOiyYJ2QCDesByHN8Oo95DwdYw%2BDhWvAhEqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDsZGrVIdDa72EYXUCrcA%2Fhd7J8Yp3H7Tgr%2F55dUs0MpuSaZY%2F3WCXJpXTcXTASZCt0hfjtezHvEVrnctLJrVPCxF3cd16L2%2FGdO%2Bt3Rwyusz7%2Fchqoo%2FT3xdcIstfPrXzUguOCUS%2FTm1SHQZ%2FVa1lxfBMg4aFGNLe30BsjJgW3Q3xVNLHGQk7BxwwPPG06E8wpuo1VPzC%2FBVA6A4Lh%2FLfzfpZt5MWAtOKmDp4TR8sK%2FX3wLEA5nBVhlTf8nhWdmBeUd6EoIAIzqtbTHdQ52%2BGJH30Ps%2Bq2FlsgCKbTW0WfxCqN1fIRl%2FcoiY3Q0nsRYwXbQ2ipwqSRzGfd%2BTXWrXw4ja9TBPfmCofWuYKEGAdEo73QvW7xoe5lrG1SlJgd84GKAEqEv8tLb4nxd202NOVA9fiR%2F9O3c6MYxlAXmOIN%2FrpSy3PlYk5%2FpokdhjZHROF8zkQpsThjxgEWcCA7peb2%2Bi4NwcxX%2BxgVq3nU2%2Bekn%2F6cLD68MRyyxejb2XSnDO2WIoJetE0JZ%2FL8uRcpOd28e14jBja9oou1%2Bnmf4gjSFEmZ%2FiVUlaqeum2bIEFMO8eR0C8puyoxg%2FdqB5JIs8HcGKuDMA3XScZC9p9%2BVwZnIY5HDVCS%2FN1fcs2Lj393Oho3jNdwwPsBXeBiDMJOf%2B7wGOqUB49S2%2BdiwMMGcn%2FP%2BpAjWavgO4hR4FceAos5VSrPM4J%2BLlos8GMh%2Fi7%2FbUy5VaYf3hBvpZ%2BSzhp4rzyGCIuaULd17omWfA6rFGefs8HLtHP9lYw8XEu5%2BnWDo3xcd2Qgki7Iz83Q5DvGhxs%2FIKKxjpALyBGM%2FwoI%2FoHA70Tpo73Ug3NXVw0nzGFC8hTAJJ%2F2D3R7hcOsqwrd%2F%2Bb9k8nQtojhttcBT&X-Amz-Signature=9f34341de3ddf83a89216d9a8872416a5db5ce9ddc7f521a6c05e556040f483a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FXKNCQB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDflaFvZaHCcDxV%2FFOePNkO%2BOr0KkT0COsLpkEIVOSbYwIgGFzgYfVW4ZOiyYJ2QCDesByHN8Oo95DwdYw%2BDhWvAhEqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDsZGrVIdDa72EYXUCrcA%2Fhd7J8Yp3H7Tgr%2F55dUs0MpuSaZY%2F3WCXJpXTcXTASZCt0hfjtezHvEVrnctLJrVPCxF3cd16L2%2FGdO%2Bt3Rwyusz7%2Fchqoo%2FT3xdcIstfPrXzUguOCUS%2FTm1SHQZ%2FVa1lxfBMg4aFGNLe30BsjJgW3Q3xVNLHGQk7BxwwPPG06E8wpuo1VPzC%2FBVA6A4Lh%2FLfzfpZt5MWAtOKmDp4TR8sK%2FX3wLEA5nBVhlTf8nhWdmBeUd6EoIAIzqtbTHdQ52%2BGJH30Ps%2Bq2FlsgCKbTW0WfxCqN1fIRl%2FcoiY3Q0nsRYwXbQ2ipwqSRzGfd%2BTXWrXw4ja9TBPfmCofWuYKEGAdEo73QvW7xoe5lrG1SlJgd84GKAEqEv8tLb4nxd202NOVA9fiR%2F9O3c6MYxlAXmOIN%2FrpSy3PlYk5%2FpokdhjZHROF8zkQpsThjxgEWcCA7peb2%2Bi4NwcxX%2BxgVq3nU2%2Bekn%2F6cLD68MRyyxejb2XSnDO2WIoJetE0JZ%2FL8uRcpOd28e14jBja9oou1%2Bnmf4gjSFEmZ%2FiVUlaqeum2bIEFMO8eR0C8puyoxg%2FdqB5JIs8HcGKuDMA3XScZC9p9%2BVwZnIY5HDVCS%2FN1fcs2Lj393Oho3jNdwwPsBXeBiDMJOf%2B7wGOqUB49S2%2BdiwMMGcn%2FP%2BpAjWavgO4hR4FceAos5VSrPM4J%2BLlos8GMh%2Fi7%2FbUy5VaYf3hBvpZ%2BSzhp4rzyGCIuaULd17omWfA6rFGefs8HLtHP9lYw8XEu5%2BnWDo3xcd2Qgki7Iz83Q5DvGhxs%2FIKKxjpALyBGM%2FwoI%2FoHA70Tpo73Ug3NXVw0nzGFC8hTAJJ%2F2D3R7hcOsqwrd%2F%2Bb9k8nQtojhttcBT&X-Amz-Signature=31f73581e062b4648368cf64c2d1756006f7be8efd0426d0eb2ff44e4337efbd&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
