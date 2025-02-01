

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6YG2VBF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD77IBntuHYG8yUd5%2F2m5H8eQkywJ1UKyTvS2F2eAk1NQIhAJYDfEerkvL8bIWM5bCPWPNYogWV2E6RCQesLFisnRUkKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyZl9GQupd7ptrnAgq3AM8kxoblfHVovOQaTmvcgTrm5yipplolIDNASIgoOvDYBrVIpdnzS5t3sKozFNH6rA2yJt%2FB4L6hK59XQMgMIN3ggviA5rA4ptkN7tqjf369WFf9zGQuvhdqdrJ3vHudh6MUyHmcP8GffLLjd8vvSnh2MufKFIUeGGvVPAlUxAFqR4kaIKL8f6Q8Nb0PqvF5%2F6%2FJwgpVj7metztPoiN0OEMAHMWjb0D%2BHuVe80IscfYJGJQR8w%2BiFASo6bVpd%2FJrcEKF9I69ij%2FGJWg80krk0rcZLP7HZjdYGKUrGAr8mBA9UsDrwhYjOOAkV8XPWxcxg0qmkdpg8TNHjQU%2Bbg1COQVwwstEc274n8iaA02Q6zrzP7piDuzC9Ybh19nCp%2F2CxQ0226CeuZ%2FZLwbdklSyjvQr%2BjuQmG5YKguh8CbX6Y5E7wtTRg3jDsKmguWBi0u5aZrSs1PPeHXa69MeRgceJ4R783K%2BBfkCVmiW5t%2BjjSm7noYJYs3YQeTiJiaSm2PVG0QnTktiZXD39f4mcBH4xZX5keuu7tFBrw6JHcbIynXo%2F0dLFTYGU4JCifNbGb%2BUupmWqqEF532%2FaaldM6CbShsLo2VFZagHpTlL1QznB3q6jMiokRkYJnzq%2BI9fjD%2FpPe8BjqkAea1duDQuMu1ZkANWx4jdMmjXq1GMv896n0DGaQ9S57i6wfcEFpaz0uro1qUltdukKchgwn3frVvcfed5U0omcK78RZhkZIJJc7bZkAoNTu6Q%2BqNg2O891D5VCh5vZcjMdST1jq4KBdKiO6UusDUT%2FVJNS6L227uUnb6BnX6bFJIJLMw7cdyi0fExhSoVkL89TdIocydmylUKDa3yVqkM82VUAxT&X-Amz-Signature=aaf554e1b52bbdef2f056762914f1e55b696809267288f53c57989899cfb653a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6YG2VBF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD77IBntuHYG8yUd5%2F2m5H8eQkywJ1UKyTvS2F2eAk1NQIhAJYDfEerkvL8bIWM5bCPWPNYogWV2E6RCQesLFisnRUkKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyZl9GQupd7ptrnAgq3AM8kxoblfHVovOQaTmvcgTrm5yipplolIDNASIgoOvDYBrVIpdnzS5t3sKozFNH6rA2yJt%2FB4L6hK59XQMgMIN3ggviA5rA4ptkN7tqjf369WFf9zGQuvhdqdrJ3vHudh6MUyHmcP8GffLLjd8vvSnh2MufKFIUeGGvVPAlUxAFqR4kaIKL8f6Q8Nb0PqvF5%2F6%2FJwgpVj7metztPoiN0OEMAHMWjb0D%2BHuVe80IscfYJGJQR8w%2BiFASo6bVpd%2FJrcEKF9I69ij%2FGJWg80krk0rcZLP7HZjdYGKUrGAr8mBA9UsDrwhYjOOAkV8XPWxcxg0qmkdpg8TNHjQU%2Bbg1COQVwwstEc274n8iaA02Q6zrzP7piDuzC9Ybh19nCp%2F2CxQ0226CeuZ%2FZLwbdklSyjvQr%2BjuQmG5YKguh8CbX6Y5E7wtTRg3jDsKmguWBi0u5aZrSs1PPeHXa69MeRgceJ4R783K%2BBfkCVmiW5t%2BjjSm7noYJYs3YQeTiJiaSm2PVG0QnTktiZXD39f4mcBH4xZX5keuu7tFBrw6JHcbIynXo%2F0dLFTYGU4JCifNbGb%2BUupmWqqEF532%2FaaldM6CbShsLo2VFZagHpTlL1QznB3q6jMiokRkYJnzq%2BI9fjD%2FpPe8BjqkAea1duDQuMu1ZkANWx4jdMmjXq1GMv896n0DGaQ9S57i6wfcEFpaz0uro1qUltdukKchgwn3frVvcfed5U0omcK78RZhkZIJJc7bZkAoNTu6Q%2BqNg2O891D5VCh5vZcjMdST1jq4KBdKiO6UusDUT%2FVJNS6L227uUnb6BnX6bFJIJLMw7cdyi0fExhSoVkL89TdIocydmylUKDa3yVqkM82VUAxT&X-Amz-Signature=f2db3cf4926fd5cfa21d2d45abc60454412ca5bcfcae4e7efa2756958262f678&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6YG2VBF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD77IBntuHYG8yUd5%2F2m5H8eQkywJ1UKyTvS2F2eAk1NQIhAJYDfEerkvL8bIWM5bCPWPNYogWV2E6RCQesLFisnRUkKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyZl9GQupd7ptrnAgq3AM8kxoblfHVovOQaTmvcgTrm5yipplolIDNASIgoOvDYBrVIpdnzS5t3sKozFNH6rA2yJt%2FB4L6hK59XQMgMIN3ggviA5rA4ptkN7tqjf369WFf9zGQuvhdqdrJ3vHudh6MUyHmcP8GffLLjd8vvSnh2MufKFIUeGGvVPAlUxAFqR4kaIKL8f6Q8Nb0PqvF5%2F6%2FJwgpVj7metztPoiN0OEMAHMWjb0D%2BHuVe80IscfYJGJQR8w%2BiFASo6bVpd%2FJrcEKF9I69ij%2FGJWg80krk0rcZLP7HZjdYGKUrGAr8mBA9UsDrwhYjOOAkV8XPWxcxg0qmkdpg8TNHjQU%2Bbg1COQVwwstEc274n8iaA02Q6zrzP7piDuzC9Ybh19nCp%2F2CxQ0226CeuZ%2FZLwbdklSyjvQr%2BjuQmG5YKguh8CbX6Y5E7wtTRg3jDsKmguWBi0u5aZrSs1PPeHXa69MeRgceJ4R783K%2BBfkCVmiW5t%2BjjSm7noYJYs3YQeTiJiaSm2PVG0QnTktiZXD39f4mcBH4xZX5keuu7tFBrw6JHcbIynXo%2F0dLFTYGU4JCifNbGb%2BUupmWqqEF532%2FaaldM6CbShsLo2VFZagHpTlL1QznB3q6jMiokRkYJnzq%2BI9fjD%2FpPe8BjqkAea1duDQuMu1ZkANWx4jdMmjXq1GMv896n0DGaQ9S57i6wfcEFpaz0uro1qUltdukKchgwn3frVvcfed5U0omcK78RZhkZIJJc7bZkAoNTu6Q%2BqNg2O891D5VCh5vZcjMdST1jq4KBdKiO6UusDUT%2FVJNS6L227uUnb6BnX6bFJIJLMw7cdyi0fExhSoVkL89TdIocydmylUKDa3yVqkM82VUAxT&X-Amz-Signature=fb1e5f61122f947bd4407eb727a01912f0447544bdbe41a14ee1c8fd02b1bb48&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6YG2VBF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD77IBntuHYG8yUd5%2F2m5H8eQkywJ1UKyTvS2F2eAk1NQIhAJYDfEerkvL8bIWM5bCPWPNYogWV2E6RCQesLFisnRUkKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyZl9GQupd7ptrnAgq3AM8kxoblfHVovOQaTmvcgTrm5yipplolIDNASIgoOvDYBrVIpdnzS5t3sKozFNH6rA2yJt%2FB4L6hK59XQMgMIN3ggviA5rA4ptkN7tqjf369WFf9zGQuvhdqdrJ3vHudh6MUyHmcP8GffLLjd8vvSnh2MufKFIUeGGvVPAlUxAFqR4kaIKL8f6Q8Nb0PqvF5%2F6%2FJwgpVj7metztPoiN0OEMAHMWjb0D%2BHuVe80IscfYJGJQR8w%2BiFASo6bVpd%2FJrcEKF9I69ij%2FGJWg80krk0rcZLP7HZjdYGKUrGAr8mBA9UsDrwhYjOOAkV8XPWxcxg0qmkdpg8TNHjQU%2Bbg1COQVwwstEc274n8iaA02Q6zrzP7piDuzC9Ybh19nCp%2F2CxQ0226CeuZ%2FZLwbdklSyjvQr%2BjuQmG5YKguh8CbX6Y5E7wtTRg3jDsKmguWBi0u5aZrSs1PPeHXa69MeRgceJ4R783K%2BBfkCVmiW5t%2BjjSm7noYJYs3YQeTiJiaSm2PVG0QnTktiZXD39f4mcBH4xZX5keuu7tFBrw6JHcbIynXo%2F0dLFTYGU4JCifNbGb%2BUupmWqqEF532%2FaaldM6CbShsLo2VFZagHpTlL1QznB3q6jMiokRkYJnzq%2BI9fjD%2FpPe8BjqkAea1duDQuMu1ZkANWx4jdMmjXq1GMv896n0DGaQ9S57i6wfcEFpaz0uro1qUltdukKchgwn3frVvcfed5U0omcK78RZhkZIJJc7bZkAoNTu6Q%2BqNg2O891D5VCh5vZcjMdST1jq4KBdKiO6UusDUT%2FVJNS6L227uUnb6BnX6bFJIJLMw7cdyi0fExhSoVkL89TdIocydmylUKDa3yVqkM82VUAxT&X-Amz-Signature=520d0e8facf6f7cd7e4fe9f1a6647258042b91d07ae8dd436c051d2b03cb7e77&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6YG2VBF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD77IBntuHYG8yUd5%2F2m5H8eQkywJ1UKyTvS2F2eAk1NQIhAJYDfEerkvL8bIWM5bCPWPNYogWV2E6RCQesLFisnRUkKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyZl9GQupd7ptrnAgq3AM8kxoblfHVovOQaTmvcgTrm5yipplolIDNASIgoOvDYBrVIpdnzS5t3sKozFNH6rA2yJt%2FB4L6hK59XQMgMIN3ggviA5rA4ptkN7tqjf369WFf9zGQuvhdqdrJ3vHudh6MUyHmcP8GffLLjd8vvSnh2MufKFIUeGGvVPAlUxAFqR4kaIKL8f6Q8Nb0PqvF5%2F6%2FJwgpVj7metztPoiN0OEMAHMWjb0D%2BHuVe80IscfYJGJQR8w%2BiFASo6bVpd%2FJrcEKF9I69ij%2FGJWg80krk0rcZLP7HZjdYGKUrGAr8mBA9UsDrwhYjOOAkV8XPWxcxg0qmkdpg8TNHjQU%2Bbg1COQVwwstEc274n8iaA02Q6zrzP7piDuzC9Ybh19nCp%2F2CxQ0226CeuZ%2FZLwbdklSyjvQr%2BjuQmG5YKguh8CbX6Y5E7wtTRg3jDsKmguWBi0u5aZrSs1PPeHXa69MeRgceJ4R783K%2BBfkCVmiW5t%2BjjSm7noYJYs3YQeTiJiaSm2PVG0QnTktiZXD39f4mcBH4xZX5keuu7tFBrw6JHcbIynXo%2F0dLFTYGU4JCifNbGb%2BUupmWqqEF532%2FaaldM6CbShsLo2VFZagHpTlL1QznB3q6jMiokRkYJnzq%2BI9fjD%2FpPe8BjqkAea1duDQuMu1ZkANWx4jdMmjXq1GMv896n0DGaQ9S57i6wfcEFpaz0uro1qUltdukKchgwn3frVvcfed5U0omcK78RZhkZIJJc7bZkAoNTu6Q%2BqNg2O891D5VCh5vZcjMdST1jq4KBdKiO6UusDUT%2FVJNS6L227uUnb6BnX6bFJIJLMw7cdyi0fExhSoVkL89TdIocydmylUKDa3yVqkM82VUAxT&X-Amz-Signature=1a34c63eac4bde767774415558cdfaa9f2ede89ce381f66ba6c977a2472158a6&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6YG2VBF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD77IBntuHYG8yUd5%2F2m5H8eQkywJ1UKyTvS2F2eAk1NQIhAJYDfEerkvL8bIWM5bCPWPNYogWV2E6RCQesLFisnRUkKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyZl9GQupd7ptrnAgq3AM8kxoblfHVovOQaTmvcgTrm5yipplolIDNASIgoOvDYBrVIpdnzS5t3sKozFNH6rA2yJt%2FB4L6hK59XQMgMIN3ggviA5rA4ptkN7tqjf369WFf9zGQuvhdqdrJ3vHudh6MUyHmcP8GffLLjd8vvSnh2MufKFIUeGGvVPAlUxAFqR4kaIKL8f6Q8Nb0PqvF5%2F6%2FJwgpVj7metztPoiN0OEMAHMWjb0D%2BHuVe80IscfYJGJQR8w%2BiFASo6bVpd%2FJrcEKF9I69ij%2FGJWg80krk0rcZLP7HZjdYGKUrGAr8mBA9UsDrwhYjOOAkV8XPWxcxg0qmkdpg8TNHjQU%2Bbg1COQVwwstEc274n8iaA02Q6zrzP7piDuzC9Ybh19nCp%2F2CxQ0226CeuZ%2FZLwbdklSyjvQr%2BjuQmG5YKguh8CbX6Y5E7wtTRg3jDsKmguWBi0u5aZrSs1PPeHXa69MeRgceJ4R783K%2BBfkCVmiW5t%2BjjSm7noYJYs3YQeTiJiaSm2PVG0QnTktiZXD39f4mcBH4xZX5keuu7tFBrw6JHcbIynXo%2F0dLFTYGU4JCifNbGb%2BUupmWqqEF532%2FaaldM6CbShsLo2VFZagHpTlL1QznB3q6jMiokRkYJnzq%2BI9fjD%2FpPe8BjqkAea1duDQuMu1ZkANWx4jdMmjXq1GMv896n0DGaQ9S57i6wfcEFpaz0uro1qUltdukKchgwn3frVvcfed5U0omcK78RZhkZIJJc7bZkAoNTu6Q%2BqNg2O891D5VCh5vZcjMdST1jq4KBdKiO6UusDUT%2FVJNS6L227uUnb6BnX6bFJIJLMw7cdyi0fExhSoVkL89TdIocydmylUKDa3yVqkM82VUAxT&X-Amz-Signature=af619e86fb66f530e28e655a0b252edf4bcd78776ce3e09c6ba67217f5d5c48f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6YG2VBF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD77IBntuHYG8yUd5%2F2m5H8eQkywJ1UKyTvS2F2eAk1NQIhAJYDfEerkvL8bIWM5bCPWPNYogWV2E6RCQesLFisnRUkKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyZl9GQupd7ptrnAgq3AM8kxoblfHVovOQaTmvcgTrm5yipplolIDNASIgoOvDYBrVIpdnzS5t3sKozFNH6rA2yJt%2FB4L6hK59XQMgMIN3ggviA5rA4ptkN7tqjf369WFf9zGQuvhdqdrJ3vHudh6MUyHmcP8GffLLjd8vvSnh2MufKFIUeGGvVPAlUxAFqR4kaIKL8f6Q8Nb0PqvF5%2F6%2FJwgpVj7metztPoiN0OEMAHMWjb0D%2BHuVe80IscfYJGJQR8w%2BiFASo6bVpd%2FJrcEKF9I69ij%2FGJWg80krk0rcZLP7HZjdYGKUrGAr8mBA9UsDrwhYjOOAkV8XPWxcxg0qmkdpg8TNHjQU%2Bbg1COQVwwstEc274n8iaA02Q6zrzP7piDuzC9Ybh19nCp%2F2CxQ0226CeuZ%2FZLwbdklSyjvQr%2BjuQmG5YKguh8CbX6Y5E7wtTRg3jDsKmguWBi0u5aZrSs1PPeHXa69MeRgceJ4R783K%2BBfkCVmiW5t%2BjjSm7noYJYs3YQeTiJiaSm2PVG0QnTktiZXD39f4mcBH4xZX5keuu7tFBrw6JHcbIynXo%2F0dLFTYGU4JCifNbGb%2BUupmWqqEF532%2FaaldM6CbShsLo2VFZagHpTlL1QznB3q6jMiokRkYJnzq%2BI9fjD%2FpPe8BjqkAea1duDQuMu1ZkANWx4jdMmjXq1GMv896n0DGaQ9S57i6wfcEFpaz0uro1qUltdukKchgwn3frVvcfed5U0omcK78RZhkZIJJc7bZkAoNTu6Q%2BqNg2O891D5VCh5vZcjMdST1jq4KBdKiO6UusDUT%2FVJNS6L227uUnb6BnX6bFJIJLMw7cdyi0fExhSoVkL89TdIocydmylUKDa3yVqkM82VUAxT&X-Amz-Signature=eddd949d1f07eb61f13a7cd56613348c493411019c9014a65169a6c9b3051790&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6YG2VBF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD77IBntuHYG8yUd5%2F2m5H8eQkywJ1UKyTvS2F2eAk1NQIhAJYDfEerkvL8bIWM5bCPWPNYogWV2E6RCQesLFisnRUkKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyZl9GQupd7ptrnAgq3AM8kxoblfHVovOQaTmvcgTrm5yipplolIDNASIgoOvDYBrVIpdnzS5t3sKozFNH6rA2yJt%2FB4L6hK59XQMgMIN3ggviA5rA4ptkN7tqjf369WFf9zGQuvhdqdrJ3vHudh6MUyHmcP8GffLLjd8vvSnh2MufKFIUeGGvVPAlUxAFqR4kaIKL8f6Q8Nb0PqvF5%2F6%2FJwgpVj7metztPoiN0OEMAHMWjb0D%2BHuVe80IscfYJGJQR8w%2BiFASo6bVpd%2FJrcEKF9I69ij%2FGJWg80krk0rcZLP7HZjdYGKUrGAr8mBA9UsDrwhYjOOAkV8XPWxcxg0qmkdpg8TNHjQU%2Bbg1COQVwwstEc274n8iaA02Q6zrzP7piDuzC9Ybh19nCp%2F2CxQ0226CeuZ%2FZLwbdklSyjvQr%2BjuQmG5YKguh8CbX6Y5E7wtTRg3jDsKmguWBi0u5aZrSs1PPeHXa69MeRgceJ4R783K%2BBfkCVmiW5t%2BjjSm7noYJYs3YQeTiJiaSm2PVG0QnTktiZXD39f4mcBH4xZX5keuu7tFBrw6JHcbIynXo%2F0dLFTYGU4JCifNbGb%2BUupmWqqEF532%2FaaldM6CbShsLo2VFZagHpTlL1QznB3q6jMiokRkYJnzq%2BI9fjD%2FpPe8BjqkAea1duDQuMu1ZkANWx4jdMmjXq1GMv896n0DGaQ9S57i6wfcEFpaz0uro1qUltdukKchgwn3frVvcfed5U0omcK78RZhkZIJJc7bZkAoNTu6Q%2BqNg2O891D5VCh5vZcjMdST1jq4KBdKiO6UusDUT%2FVJNS6L227uUnb6BnX6bFJIJLMw7cdyi0fExhSoVkL89TdIocydmylUKDa3yVqkM82VUAxT&X-Amz-Signature=abe2d29673d9a8e9ab7fa80896661628907ebcafced4b4cf72cfe7d82f08cc5b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6YG2VBF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD77IBntuHYG8yUd5%2F2m5H8eQkywJ1UKyTvS2F2eAk1NQIhAJYDfEerkvL8bIWM5bCPWPNYogWV2E6RCQesLFisnRUkKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyZl9GQupd7ptrnAgq3AM8kxoblfHVovOQaTmvcgTrm5yipplolIDNASIgoOvDYBrVIpdnzS5t3sKozFNH6rA2yJt%2FB4L6hK59XQMgMIN3ggviA5rA4ptkN7tqjf369WFf9zGQuvhdqdrJ3vHudh6MUyHmcP8GffLLjd8vvSnh2MufKFIUeGGvVPAlUxAFqR4kaIKL8f6Q8Nb0PqvF5%2F6%2FJwgpVj7metztPoiN0OEMAHMWjb0D%2BHuVe80IscfYJGJQR8w%2BiFASo6bVpd%2FJrcEKF9I69ij%2FGJWg80krk0rcZLP7HZjdYGKUrGAr8mBA9UsDrwhYjOOAkV8XPWxcxg0qmkdpg8TNHjQU%2Bbg1COQVwwstEc274n8iaA02Q6zrzP7piDuzC9Ybh19nCp%2F2CxQ0226CeuZ%2FZLwbdklSyjvQr%2BjuQmG5YKguh8CbX6Y5E7wtTRg3jDsKmguWBi0u5aZrSs1PPeHXa69MeRgceJ4R783K%2BBfkCVmiW5t%2BjjSm7noYJYs3YQeTiJiaSm2PVG0QnTktiZXD39f4mcBH4xZX5keuu7tFBrw6JHcbIynXo%2F0dLFTYGU4JCifNbGb%2BUupmWqqEF532%2FaaldM6CbShsLo2VFZagHpTlL1QznB3q6jMiokRkYJnzq%2BI9fjD%2FpPe8BjqkAea1duDQuMu1ZkANWx4jdMmjXq1GMv896n0DGaQ9S57i6wfcEFpaz0uro1qUltdukKchgwn3frVvcfed5U0omcK78RZhkZIJJc7bZkAoNTu6Q%2BqNg2O891D5VCh5vZcjMdST1jq4KBdKiO6UusDUT%2FVJNS6L227uUnb6BnX6bFJIJLMw7cdyi0fExhSoVkL89TdIocydmylUKDa3yVqkM82VUAxT&X-Amz-Signature=b146655e3b95deb66af314ae1fc6b6224601339bc5bca8dcdd160285f72a216f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YCH6UR6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHnWJVRlQcEnPMJGLAxeLbqAFMg3PluKR79BaQu6ovETAiEAyToo6ST%2BpsUqUBl9F1Ufhe6vEeTJB5EoL8NW6yVHNDAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnsCx9g2Si3ytCdyircAxtA2SZVUW3oAcsXELvM1jdQRjeEvM0ekkp65VnnkCMI6gNIO724LmVcn%2FWvDSxHNjo5BxaAvP0BERXQU5aH6%2FjcPlCx7HuYdmvsaRrO33lEA1cp2Fobyk%2BiJU0yT665Rr97ERfZQ4%2FzwQ41lZdfIPaqSAjKgkzlFGHmkGZPlRQp7sXpJLN4m%2F3S%2BURMhtFU4OcLSCJraCEXy1grlrwtG6MewqjiQVqmHVcpZaWERqqLilaHWtGS0H3Cp980TuLPka7TTmTkKINgbZxbGCzANCja2u7FGf%2FSw95z7HXt5qHj0CpX1hdrYRgzvQEISfneBpb%2FW0DXoEMFEgsBffY94whcye3uf1BxmlEubvwPFNgVBYu3wh1%2B7YimQX7xXsmXgeNfRkMV9xDoD5QTLq1rOnt11Jx8EBoZFEEcTlt5spORJddmWuID7ZSjtUG59wqrwxCrcX4G7rReaLkBrOGVRA8b8mvjUIQby7PoCaUtz2HlCs7WJ5uNu82QK1IB4Nc%2BkBaA%2FsfwPTxNP%2BZH8qT3fOx%2BfDfSJHnpALAxsPQPXvIciCPpPT82EFZcy%2Bu90UCU1tVnL%2BbtDCHbAmtVzeUbyYG84bvcb%2FS0iq5iJbaE8j%2FjsG%2FfHC1JrTDnUgJpMKWk97wGOqUBZuelr1C3W1mAVXLEWyJkmyerEAms20i6%2BGScbI7Xdg03Fz5ZrfQdZCs0aNJt4wZMWDSkWqjjEgBQ6R0s3gGEUxjnGRHeELt1PnlVMNIti0Dcfnp6ocXniyAolMzhx3%2BxQS%2B8RTlZnH%2F5rqmBfaLixU4lsyEGTf3PcAnZuYyjLIcgzXV9%2FsvRSDdDRk4%2BKgaUN96gkq%2FLm360UNMbC8Z6KHaZXvpI&X-Amz-Signature=fa3b247c7b6f3e6debf37fae0a6e131b96bd6b9f01837e794d3dfc765db3b312&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YCH6UR6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHnWJVRlQcEnPMJGLAxeLbqAFMg3PluKR79BaQu6ovETAiEAyToo6ST%2BpsUqUBl9F1Ufhe6vEeTJB5EoL8NW6yVHNDAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnsCx9g2Si3ytCdyircAxtA2SZVUW3oAcsXELvM1jdQRjeEvM0ekkp65VnnkCMI6gNIO724LmVcn%2FWvDSxHNjo5BxaAvP0BERXQU5aH6%2FjcPlCx7HuYdmvsaRrO33lEA1cp2Fobyk%2BiJU0yT665Rr97ERfZQ4%2FzwQ41lZdfIPaqSAjKgkzlFGHmkGZPlRQp7sXpJLN4m%2F3S%2BURMhtFU4OcLSCJraCEXy1grlrwtG6MewqjiQVqmHVcpZaWERqqLilaHWtGS0H3Cp980TuLPka7TTmTkKINgbZxbGCzANCja2u7FGf%2FSw95z7HXt5qHj0CpX1hdrYRgzvQEISfneBpb%2FW0DXoEMFEgsBffY94whcye3uf1BxmlEubvwPFNgVBYu3wh1%2B7YimQX7xXsmXgeNfRkMV9xDoD5QTLq1rOnt11Jx8EBoZFEEcTlt5spORJddmWuID7ZSjtUG59wqrwxCrcX4G7rReaLkBrOGVRA8b8mvjUIQby7PoCaUtz2HlCs7WJ5uNu82QK1IB4Nc%2BkBaA%2FsfwPTxNP%2BZH8qT3fOx%2BfDfSJHnpALAxsPQPXvIciCPpPT82EFZcy%2Bu90UCU1tVnL%2BbtDCHbAmtVzeUbyYG84bvcb%2FS0iq5iJbaE8j%2FjsG%2FfHC1JrTDnUgJpMKWk97wGOqUBZuelr1C3W1mAVXLEWyJkmyerEAms20i6%2BGScbI7Xdg03Fz5ZrfQdZCs0aNJt4wZMWDSkWqjjEgBQ6R0s3gGEUxjnGRHeELt1PnlVMNIti0Dcfnp6ocXniyAolMzhx3%2BxQS%2B8RTlZnH%2F5rqmBfaLixU4lsyEGTf3PcAnZuYyjLIcgzXV9%2FsvRSDdDRk4%2BKgaUN96gkq%2FLm360UNMbC8Z6KHaZXvpI&X-Amz-Signature=44bdf78c1e02dddf78d590f7bb49ff1bd0d9cb9f9e197634ff08be0fcc9f1f60&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
