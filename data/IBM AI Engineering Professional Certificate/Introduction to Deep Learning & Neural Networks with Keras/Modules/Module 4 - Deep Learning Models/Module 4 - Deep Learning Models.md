

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FLOVRYF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbf%2BuisxZZFjXMY%2FtD15ungkW3j7Adtw1jSFbbqeJX5QIhALCIvnyXFhDp66qw0hocDxTp8JXO10FvbzCHz15iLgO4Kv8DCDkQABoMNjM3NDIzMTgzODA1IgzSa1y2X3Jt7xY6%2BA4q3ANa97aQO8J%2BRETAF2RZrcVWGodMYepcT3jNp2Nxj2U8TOWoHgFTjunFLqUXowxnMbGsBS66mEV6RO6VgvNpaI7sSLujAAkW7iqOmva8Plp9FVWIfE31tPdpiLu7E11aohDsFbNY040V3PBa%2FJBdmIzv%2FAOyUVlxSgFscw3S1MtFF%2FODFDSKYQcebXzwM7x9dREzKVjCwIy9ZkTZW6ydewjZyPgNfzeLC5gYo%2BN6XCBO6uidg0c4o8KTNjXt7waHdB5hSJqDbnJ8xxmLox2V%2B1pXj1aJTeZXoK9n%2B9GyDttyKbB9kimrqmaI1d0T0HnR9a%2Frlq1agT3Ke7xaRksTnU%2BimQ0k8e17yXUCH9kuLNrOhMLqDZg55sslq9B3yKyafQyXFwXVgAzEAYWVw%2B22vzjCpJQ76hs5ZgY30JL0lsAdyZ4Gn77Cn6DyYaN%2BUdUDdqB1FikOKf1WOM7a3TbJnIdxG9LkN0V1ijWOE%2FIVzTO6f6jf9vmH3RwxG6ct1VIfghP1%2FcohIvwJAwsNH5MtW2LN%2Fv3Bw2CtlZQ4X50xvSZv9%2BeI21uL2coH5DORJRmnbkBgbneVmr5QUzJOassyBfcFkqbOsX795cVB66k0b2iiKDkUfGS6vrA%2FLM1WgjDnzIq9BjqkAWaZ4LUAQSUQwhVopONgyTbWk6Zd5I6jORBtW%2FMwd4TMHkx9%2FYp1qZKcJkUUOHK2dGqwqxMdn2NudN%2FsQIG5HtJ%2FX2sjY68YP6kch%2BzRQKoN70JlzN4LQ2U2z2z9uElnNqZiAeJbdsRqW%2FsCVRvxwIibd6k0zddstzgaKZ%2FVu7F35it8j7iMRqfNvDfNYtfK6vmmqjsPgwxptmNcFb7TOdY0wSEp&X-Amz-Signature=d381e3bb4b33c3f2fb376246933cd4b4321c5cf702332ff03de33c80fe91887f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FLOVRYF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbf%2BuisxZZFjXMY%2FtD15ungkW3j7Adtw1jSFbbqeJX5QIhALCIvnyXFhDp66qw0hocDxTp8JXO10FvbzCHz15iLgO4Kv8DCDkQABoMNjM3NDIzMTgzODA1IgzSa1y2X3Jt7xY6%2BA4q3ANa97aQO8J%2BRETAF2RZrcVWGodMYepcT3jNp2Nxj2U8TOWoHgFTjunFLqUXowxnMbGsBS66mEV6RO6VgvNpaI7sSLujAAkW7iqOmva8Plp9FVWIfE31tPdpiLu7E11aohDsFbNY040V3PBa%2FJBdmIzv%2FAOyUVlxSgFscw3S1MtFF%2FODFDSKYQcebXzwM7x9dREzKVjCwIy9ZkTZW6ydewjZyPgNfzeLC5gYo%2BN6XCBO6uidg0c4o8KTNjXt7waHdB5hSJqDbnJ8xxmLox2V%2B1pXj1aJTeZXoK9n%2B9GyDttyKbB9kimrqmaI1d0T0HnR9a%2Frlq1agT3Ke7xaRksTnU%2BimQ0k8e17yXUCH9kuLNrOhMLqDZg55sslq9B3yKyafQyXFwXVgAzEAYWVw%2B22vzjCpJQ76hs5ZgY30JL0lsAdyZ4Gn77Cn6DyYaN%2BUdUDdqB1FikOKf1WOM7a3TbJnIdxG9LkN0V1ijWOE%2FIVzTO6f6jf9vmH3RwxG6ct1VIfghP1%2FcohIvwJAwsNH5MtW2LN%2Fv3Bw2CtlZQ4X50xvSZv9%2BeI21uL2coH5DORJRmnbkBgbneVmr5QUzJOassyBfcFkqbOsX795cVB66k0b2iiKDkUfGS6vrA%2FLM1WgjDnzIq9BjqkAWaZ4LUAQSUQwhVopONgyTbWk6Zd5I6jORBtW%2FMwd4TMHkx9%2FYp1qZKcJkUUOHK2dGqwqxMdn2NudN%2FsQIG5HtJ%2FX2sjY68YP6kch%2BzRQKoN70JlzN4LQ2U2z2z9uElnNqZiAeJbdsRqW%2FsCVRvxwIibd6k0zddstzgaKZ%2FVu7F35it8j7iMRqfNvDfNYtfK6vmmqjsPgwxptmNcFb7TOdY0wSEp&X-Amz-Signature=ff711dda9d80da04d86806fc69c14723e770f62ba68cc79064f1c37ddf4c0000&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FLOVRYF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbf%2BuisxZZFjXMY%2FtD15ungkW3j7Adtw1jSFbbqeJX5QIhALCIvnyXFhDp66qw0hocDxTp8JXO10FvbzCHz15iLgO4Kv8DCDkQABoMNjM3NDIzMTgzODA1IgzSa1y2X3Jt7xY6%2BA4q3ANa97aQO8J%2BRETAF2RZrcVWGodMYepcT3jNp2Nxj2U8TOWoHgFTjunFLqUXowxnMbGsBS66mEV6RO6VgvNpaI7sSLujAAkW7iqOmva8Plp9FVWIfE31tPdpiLu7E11aohDsFbNY040V3PBa%2FJBdmIzv%2FAOyUVlxSgFscw3S1MtFF%2FODFDSKYQcebXzwM7x9dREzKVjCwIy9ZkTZW6ydewjZyPgNfzeLC5gYo%2BN6XCBO6uidg0c4o8KTNjXt7waHdB5hSJqDbnJ8xxmLox2V%2B1pXj1aJTeZXoK9n%2B9GyDttyKbB9kimrqmaI1d0T0HnR9a%2Frlq1agT3Ke7xaRksTnU%2BimQ0k8e17yXUCH9kuLNrOhMLqDZg55sslq9B3yKyafQyXFwXVgAzEAYWVw%2B22vzjCpJQ76hs5ZgY30JL0lsAdyZ4Gn77Cn6DyYaN%2BUdUDdqB1FikOKf1WOM7a3TbJnIdxG9LkN0V1ijWOE%2FIVzTO6f6jf9vmH3RwxG6ct1VIfghP1%2FcohIvwJAwsNH5MtW2LN%2Fv3Bw2CtlZQ4X50xvSZv9%2BeI21uL2coH5DORJRmnbkBgbneVmr5QUzJOassyBfcFkqbOsX795cVB66k0b2iiKDkUfGS6vrA%2FLM1WgjDnzIq9BjqkAWaZ4LUAQSUQwhVopONgyTbWk6Zd5I6jORBtW%2FMwd4TMHkx9%2FYp1qZKcJkUUOHK2dGqwqxMdn2NudN%2FsQIG5HtJ%2FX2sjY68YP6kch%2BzRQKoN70JlzN4LQ2U2z2z9uElnNqZiAeJbdsRqW%2FsCVRvxwIibd6k0zddstzgaKZ%2FVu7F35it8j7iMRqfNvDfNYtfK6vmmqjsPgwxptmNcFb7TOdY0wSEp&X-Amz-Signature=a525357cc340b6d9b1fecb0574dada9ac1d0034df50665ed361d7f4b24494341&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FLOVRYF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbf%2BuisxZZFjXMY%2FtD15ungkW3j7Adtw1jSFbbqeJX5QIhALCIvnyXFhDp66qw0hocDxTp8JXO10FvbzCHz15iLgO4Kv8DCDkQABoMNjM3NDIzMTgzODA1IgzSa1y2X3Jt7xY6%2BA4q3ANa97aQO8J%2BRETAF2RZrcVWGodMYepcT3jNp2Nxj2U8TOWoHgFTjunFLqUXowxnMbGsBS66mEV6RO6VgvNpaI7sSLujAAkW7iqOmva8Plp9FVWIfE31tPdpiLu7E11aohDsFbNY040V3PBa%2FJBdmIzv%2FAOyUVlxSgFscw3S1MtFF%2FODFDSKYQcebXzwM7x9dREzKVjCwIy9ZkTZW6ydewjZyPgNfzeLC5gYo%2BN6XCBO6uidg0c4o8KTNjXt7waHdB5hSJqDbnJ8xxmLox2V%2B1pXj1aJTeZXoK9n%2B9GyDttyKbB9kimrqmaI1d0T0HnR9a%2Frlq1agT3Ke7xaRksTnU%2BimQ0k8e17yXUCH9kuLNrOhMLqDZg55sslq9B3yKyafQyXFwXVgAzEAYWVw%2B22vzjCpJQ76hs5ZgY30JL0lsAdyZ4Gn77Cn6DyYaN%2BUdUDdqB1FikOKf1WOM7a3TbJnIdxG9LkN0V1ijWOE%2FIVzTO6f6jf9vmH3RwxG6ct1VIfghP1%2FcohIvwJAwsNH5MtW2LN%2Fv3Bw2CtlZQ4X50xvSZv9%2BeI21uL2coH5DORJRmnbkBgbneVmr5QUzJOassyBfcFkqbOsX795cVB66k0b2iiKDkUfGS6vrA%2FLM1WgjDnzIq9BjqkAWaZ4LUAQSUQwhVopONgyTbWk6Zd5I6jORBtW%2FMwd4TMHkx9%2FYp1qZKcJkUUOHK2dGqwqxMdn2NudN%2FsQIG5HtJ%2FX2sjY68YP6kch%2BzRQKoN70JlzN4LQ2U2z2z9uElnNqZiAeJbdsRqW%2FsCVRvxwIibd6k0zddstzgaKZ%2FVu7F35it8j7iMRqfNvDfNYtfK6vmmqjsPgwxptmNcFb7TOdY0wSEp&X-Amz-Signature=90176fe88358b4adfd7a7a516b96a0ea9f99e2cb338dc07154861889af2e7bfb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FLOVRYF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbf%2BuisxZZFjXMY%2FtD15ungkW3j7Adtw1jSFbbqeJX5QIhALCIvnyXFhDp66qw0hocDxTp8JXO10FvbzCHz15iLgO4Kv8DCDkQABoMNjM3NDIzMTgzODA1IgzSa1y2X3Jt7xY6%2BA4q3ANa97aQO8J%2BRETAF2RZrcVWGodMYepcT3jNp2Nxj2U8TOWoHgFTjunFLqUXowxnMbGsBS66mEV6RO6VgvNpaI7sSLujAAkW7iqOmva8Plp9FVWIfE31tPdpiLu7E11aohDsFbNY040V3PBa%2FJBdmIzv%2FAOyUVlxSgFscw3S1MtFF%2FODFDSKYQcebXzwM7x9dREzKVjCwIy9ZkTZW6ydewjZyPgNfzeLC5gYo%2BN6XCBO6uidg0c4o8KTNjXt7waHdB5hSJqDbnJ8xxmLox2V%2B1pXj1aJTeZXoK9n%2B9GyDttyKbB9kimrqmaI1d0T0HnR9a%2Frlq1agT3Ke7xaRksTnU%2BimQ0k8e17yXUCH9kuLNrOhMLqDZg55sslq9B3yKyafQyXFwXVgAzEAYWVw%2B22vzjCpJQ76hs5ZgY30JL0lsAdyZ4Gn77Cn6DyYaN%2BUdUDdqB1FikOKf1WOM7a3TbJnIdxG9LkN0V1ijWOE%2FIVzTO6f6jf9vmH3RwxG6ct1VIfghP1%2FcohIvwJAwsNH5MtW2LN%2Fv3Bw2CtlZQ4X50xvSZv9%2BeI21uL2coH5DORJRmnbkBgbneVmr5QUzJOassyBfcFkqbOsX795cVB66k0b2iiKDkUfGS6vrA%2FLM1WgjDnzIq9BjqkAWaZ4LUAQSUQwhVopONgyTbWk6Zd5I6jORBtW%2FMwd4TMHkx9%2FYp1qZKcJkUUOHK2dGqwqxMdn2NudN%2FsQIG5HtJ%2FX2sjY68YP6kch%2BzRQKoN70JlzN4LQ2U2z2z9uElnNqZiAeJbdsRqW%2FsCVRvxwIibd6k0zddstzgaKZ%2FVu7F35it8j7iMRqfNvDfNYtfK6vmmqjsPgwxptmNcFb7TOdY0wSEp&X-Amz-Signature=1b81c1fd8fabade193fc46328792e9092e347d40e6be6ecdc860d7268e9b0723&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FLOVRYF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbf%2BuisxZZFjXMY%2FtD15ungkW3j7Adtw1jSFbbqeJX5QIhALCIvnyXFhDp66qw0hocDxTp8JXO10FvbzCHz15iLgO4Kv8DCDkQABoMNjM3NDIzMTgzODA1IgzSa1y2X3Jt7xY6%2BA4q3ANa97aQO8J%2BRETAF2RZrcVWGodMYepcT3jNp2Nxj2U8TOWoHgFTjunFLqUXowxnMbGsBS66mEV6RO6VgvNpaI7sSLujAAkW7iqOmva8Plp9FVWIfE31tPdpiLu7E11aohDsFbNY040V3PBa%2FJBdmIzv%2FAOyUVlxSgFscw3S1MtFF%2FODFDSKYQcebXzwM7x9dREzKVjCwIy9ZkTZW6ydewjZyPgNfzeLC5gYo%2BN6XCBO6uidg0c4o8KTNjXt7waHdB5hSJqDbnJ8xxmLox2V%2B1pXj1aJTeZXoK9n%2B9GyDttyKbB9kimrqmaI1d0T0HnR9a%2Frlq1agT3Ke7xaRksTnU%2BimQ0k8e17yXUCH9kuLNrOhMLqDZg55sslq9B3yKyafQyXFwXVgAzEAYWVw%2B22vzjCpJQ76hs5ZgY30JL0lsAdyZ4Gn77Cn6DyYaN%2BUdUDdqB1FikOKf1WOM7a3TbJnIdxG9LkN0V1ijWOE%2FIVzTO6f6jf9vmH3RwxG6ct1VIfghP1%2FcohIvwJAwsNH5MtW2LN%2Fv3Bw2CtlZQ4X50xvSZv9%2BeI21uL2coH5DORJRmnbkBgbneVmr5QUzJOassyBfcFkqbOsX795cVB66k0b2iiKDkUfGS6vrA%2FLM1WgjDnzIq9BjqkAWaZ4LUAQSUQwhVopONgyTbWk6Zd5I6jORBtW%2FMwd4TMHkx9%2FYp1qZKcJkUUOHK2dGqwqxMdn2NudN%2FsQIG5HtJ%2FX2sjY68YP6kch%2BzRQKoN70JlzN4LQ2U2z2z9uElnNqZiAeJbdsRqW%2FsCVRvxwIibd6k0zddstzgaKZ%2FVu7F35it8j7iMRqfNvDfNYtfK6vmmqjsPgwxptmNcFb7TOdY0wSEp&X-Amz-Signature=e8ec6ca21e04ff67676c4accc83a9d1dc296462a3ff61815af4c97c227a1f84d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FLOVRYF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbf%2BuisxZZFjXMY%2FtD15ungkW3j7Adtw1jSFbbqeJX5QIhALCIvnyXFhDp66qw0hocDxTp8JXO10FvbzCHz15iLgO4Kv8DCDkQABoMNjM3NDIzMTgzODA1IgzSa1y2X3Jt7xY6%2BA4q3ANa97aQO8J%2BRETAF2RZrcVWGodMYepcT3jNp2Nxj2U8TOWoHgFTjunFLqUXowxnMbGsBS66mEV6RO6VgvNpaI7sSLujAAkW7iqOmva8Plp9FVWIfE31tPdpiLu7E11aohDsFbNY040V3PBa%2FJBdmIzv%2FAOyUVlxSgFscw3S1MtFF%2FODFDSKYQcebXzwM7x9dREzKVjCwIy9ZkTZW6ydewjZyPgNfzeLC5gYo%2BN6XCBO6uidg0c4o8KTNjXt7waHdB5hSJqDbnJ8xxmLox2V%2B1pXj1aJTeZXoK9n%2B9GyDttyKbB9kimrqmaI1d0T0HnR9a%2Frlq1agT3Ke7xaRksTnU%2BimQ0k8e17yXUCH9kuLNrOhMLqDZg55sslq9B3yKyafQyXFwXVgAzEAYWVw%2B22vzjCpJQ76hs5ZgY30JL0lsAdyZ4Gn77Cn6DyYaN%2BUdUDdqB1FikOKf1WOM7a3TbJnIdxG9LkN0V1ijWOE%2FIVzTO6f6jf9vmH3RwxG6ct1VIfghP1%2FcohIvwJAwsNH5MtW2LN%2Fv3Bw2CtlZQ4X50xvSZv9%2BeI21uL2coH5DORJRmnbkBgbneVmr5QUzJOassyBfcFkqbOsX795cVB66k0b2iiKDkUfGS6vrA%2FLM1WgjDnzIq9BjqkAWaZ4LUAQSUQwhVopONgyTbWk6Zd5I6jORBtW%2FMwd4TMHkx9%2FYp1qZKcJkUUOHK2dGqwqxMdn2NudN%2FsQIG5HtJ%2FX2sjY68YP6kch%2BzRQKoN70JlzN4LQ2U2z2z9uElnNqZiAeJbdsRqW%2FsCVRvxwIibd6k0zddstzgaKZ%2FVu7F35it8j7iMRqfNvDfNYtfK6vmmqjsPgwxptmNcFb7TOdY0wSEp&X-Amz-Signature=83eed36ab37b012f291b01e39dd14e4f89d8705775cee82869d188acfee0891e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FLOVRYF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbf%2BuisxZZFjXMY%2FtD15ungkW3j7Adtw1jSFbbqeJX5QIhALCIvnyXFhDp66qw0hocDxTp8JXO10FvbzCHz15iLgO4Kv8DCDkQABoMNjM3NDIzMTgzODA1IgzSa1y2X3Jt7xY6%2BA4q3ANa97aQO8J%2BRETAF2RZrcVWGodMYepcT3jNp2Nxj2U8TOWoHgFTjunFLqUXowxnMbGsBS66mEV6RO6VgvNpaI7sSLujAAkW7iqOmva8Plp9FVWIfE31tPdpiLu7E11aohDsFbNY040V3PBa%2FJBdmIzv%2FAOyUVlxSgFscw3S1MtFF%2FODFDSKYQcebXzwM7x9dREzKVjCwIy9ZkTZW6ydewjZyPgNfzeLC5gYo%2BN6XCBO6uidg0c4o8KTNjXt7waHdB5hSJqDbnJ8xxmLox2V%2B1pXj1aJTeZXoK9n%2B9GyDttyKbB9kimrqmaI1d0T0HnR9a%2Frlq1agT3Ke7xaRksTnU%2BimQ0k8e17yXUCH9kuLNrOhMLqDZg55sslq9B3yKyafQyXFwXVgAzEAYWVw%2B22vzjCpJQ76hs5ZgY30JL0lsAdyZ4Gn77Cn6DyYaN%2BUdUDdqB1FikOKf1WOM7a3TbJnIdxG9LkN0V1ijWOE%2FIVzTO6f6jf9vmH3RwxG6ct1VIfghP1%2FcohIvwJAwsNH5MtW2LN%2Fv3Bw2CtlZQ4X50xvSZv9%2BeI21uL2coH5DORJRmnbkBgbneVmr5QUzJOassyBfcFkqbOsX795cVB66k0b2iiKDkUfGS6vrA%2FLM1WgjDnzIq9BjqkAWaZ4LUAQSUQwhVopONgyTbWk6Zd5I6jORBtW%2FMwd4TMHkx9%2FYp1qZKcJkUUOHK2dGqwqxMdn2NudN%2FsQIG5HtJ%2FX2sjY68YP6kch%2BzRQKoN70JlzN4LQ2U2z2z9uElnNqZiAeJbdsRqW%2FsCVRvxwIibd6k0zddstzgaKZ%2FVu7F35it8j7iMRqfNvDfNYtfK6vmmqjsPgwxptmNcFb7TOdY0wSEp&X-Amz-Signature=3b21cc6b2cae3b8c7e1d361b56bc6408a547b831fa8360a84aafd95e9ee9b480&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FLOVRYF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbf%2BuisxZZFjXMY%2FtD15ungkW3j7Adtw1jSFbbqeJX5QIhALCIvnyXFhDp66qw0hocDxTp8JXO10FvbzCHz15iLgO4Kv8DCDkQABoMNjM3NDIzMTgzODA1IgzSa1y2X3Jt7xY6%2BA4q3ANa97aQO8J%2BRETAF2RZrcVWGodMYepcT3jNp2Nxj2U8TOWoHgFTjunFLqUXowxnMbGsBS66mEV6RO6VgvNpaI7sSLujAAkW7iqOmva8Plp9FVWIfE31tPdpiLu7E11aohDsFbNY040V3PBa%2FJBdmIzv%2FAOyUVlxSgFscw3S1MtFF%2FODFDSKYQcebXzwM7x9dREzKVjCwIy9ZkTZW6ydewjZyPgNfzeLC5gYo%2BN6XCBO6uidg0c4o8KTNjXt7waHdB5hSJqDbnJ8xxmLox2V%2B1pXj1aJTeZXoK9n%2B9GyDttyKbB9kimrqmaI1d0T0HnR9a%2Frlq1agT3Ke7xaRksTnU%2BimQ0k8e17yXUCH9kuLNrOhMLqDZg55sslq9B3yKyafQyXFwXVgAzEAYWVw%2B22vzjCpJQ76hs5ZgY30JL0lsAdyZ4Gn77Cn6DyYaN%2BUdUDdqB1FikOKf1WOM7a3TbJnIdxG9LkN0V1ijWOE%2FIVzTO6f6jf9vmH3RwxG6ct1VIfghP1%2FcohIvwJAwsNH5MtW2LN%2Fv3Bw2CtlZQ4X50xvSZv9%2BeI21uL2coH5DORJRmnbkBgbneVmr5QUzJOassyBfcFkqbOsX795cVB66k0b2iiKDkUfGS6vrA%2FLM1WgjDnzIq9BjqkAWaZ4LUAQSUQwhVopONgyTbWk6Zd5I6jORBtW%2FMwd4TMHkx9%2FYp1qZKcJkUUOHK2dGqwqxMdn2NudN%2FsQIG5HtJ%2FX2sjY68YP6kch%2BzRQKoN70JlzN4LQ2U2z2z9uElnNqZiAeJbdsRqW%2FsCVRvxwIibd6k0zddstzgaKZ%2FVu7F35it8j7iMRqfNvDfNYtfK6vmmqjsPgwxptmNcFb7TOdY0wSEp&X-Amz-Signature=fbcc608d49d9a7a3c7a0fd1009165033aae116249d9ea4ee53fd0bfcdf0728d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QBXBWQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIE4W7uI3s1VV40LrWQDWK2gCUAoRwA5Mh56K%2Fnk2RvopAiEA%2FM8RO6wb7zFI67s6XKQ8Qizgv3UJgNBU6a%2FTY3B8VBUq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDE3zlR6L7pii5jLUEircA7IMsL%2F%2FvAkJ8t0iN7IHJ%2BUzH5MtoiRkOP3PQSI0tFg4N%2F1MCC4yHSSQEXJLgkb8njUN%2FEhEdwyjd0M3%2Fd1Vcq2wf9TyqwBJLbfgyjsLkDS6Un1zw9OaV4E1XLQDv%2BsTUkmb3nxG7vSbDBryKzk9i4%2FabxLk1YdjKJHY7ZpnJ5SrzcH2mIELh3HGB9yxU4znoz%2F6uAu%2F9T0DBzUey6AW6sMFMp6FhDWYLZB8iIFi9ZfQcHv894azlHYaZpDjsOAVGOgFpSIJPmiTl6zW2WHTiA1TOzIG1DjHw6edOtrNHm7KYJ4ZB5y3qd5aUlcg0jGwDoDxzjrXZqaKR2NGofKs0%2FKRQUd49HDdlO61tq7sVTUxhgwe%2FHBdnvLu4JHl51iQSmnVjWnUOikicJ0ujCqccwvRJT6p4pRuaL1YY0sEUczDBa04OOQDrRptXadYcMVDGUlc9llZW3YD52PAjqkDB9PgLHrB9jRx8m%2BDJKVG0rGZFu4N9rsUUPagxYkm6XneSEfmHT4MNeGiKsQ1u3Zfdtxq8PcrWz4ZVz4tLJEHUlIoEaZ6foA4JOfaF6esPnykUBX%2BqeKB6nLQUPH3mamgs6z4%2FaW40GlbDVr5II28xLCjyB5ey%2Bu%2FJ%2Fr4CeWwMPrMir0GOqUBqBrKHKhJv459wm0G9ABsdQhwZrgb3maabKIpiBRIjqJe%2BG3Z2y%2FNNsHysCp9Qym4N6rwXzjTIbozJqkB0zYQCCaikpPjWO7%2B9aKEmotHobnLqoXxiLkvi1xM%2Fy9w32I8MHROnFIq8Xh%2FkVDhJ0D3zTBO6CfRGBS6R3wLgMGLbCz%2B0fx0fKYrklVldH7zimWVLL%2BTKmu5vzboCUQOn9mulpT%2FeJmb&X-Amz-Signature=d9aee9a6eeefee70b179c92a04d157487821b58f9eb29cb92a63d287c8bb4775&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QBXBWQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIE4W7uI3s1VV40LrWQDWK2gCUAoRwA5Mh56K%2Fnk2RvopAiEA%2FM8RO6wb7zFI67s6XKQ8Qizgv3UJgNBU6a%2FTY3B8VBUq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDE3zlR6L7pii5jLUEircA7IMsL%2F%2FvAkJ8t0iN7IHJ%2BUzH5MtoiRkOP3PQSI0tFg4N%2F1MCC4yHSSQEXJLgkb8njUN%2FEhEdwyjd0M3%2Fd1Vcq2wf9TyqwBJLbfgyjsLkDS6Un1zw9OaV4E1XLQDv%2BsTUkmb3nxG7vSbDBryKzk9i4%2FabxLk1YdjKJHY7ZpnJ5SrzcH2mIELh3HGB9yxU4znoz%2F6uAu%2F9T0DBzUey6AW6sMFMp6FhDWYLZB8iIFi9ZfQcHv894azlHYaZpDjsOAVGOgFpSIJPmiTl6zW2WHTiA1TOzIG1DjHw6edOtrNHm7KYJ4ZB5y3qd5aUlcg0jGwDoDxzjrXZqaKR2NGofKs0%2FKRQUd49HDdlO61tq7sVTUxhgwe%2FHBdnvLu4JHl51iQSmnVjWnUOikicJ0ujCqccwvRJT6p4pRuaL1YY0sEUczDBa04OOQDrRptXadYcMVDGUlc9llZW3YD52PAjqkDB9PgLHrB9jRx8m%2BDJKVG0rGZFu4N9rsUUPagxYkm6XneSEfmHT4MNeGiKsQ1u3Zfdtxq8PcrWz4ZVz4tLJEHUlIoEaZ6foA4JOfaF6esPnykUBX%2BqeKB6nLQUPH3mamgs6z4%2FaW40GlbDVr5II28xLCjyB5ey%2Bu%2FJ%2Fr4CeWwMPrMir0GOqUBqBrKHKhJv459wm0G9ABsdQhwZrgb3maabKIpiBRIjqJe%2BG3Z2y%2FNNsHysCp9Qym4N6rwXzjTIbozJqkB0zYQCCaikpPjWO7%2B9aKEmotHobnLqoXxiLkvi1xM%2Fy9w32I8MHROnFIq8Xh%2FkVDhJ0D3zTBO6CfRGBS6R3wLgMGLbCz%2B0fx0fKYrklVldH7zimWVLL%2BTKmu5vzboCUQOn9mulpT%2FeJmb&X-Amz-Signature=fc35511abeffa0f6f71322a670c2b439ee2efcac0ce77d50e6c6d4a017a02d81&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
