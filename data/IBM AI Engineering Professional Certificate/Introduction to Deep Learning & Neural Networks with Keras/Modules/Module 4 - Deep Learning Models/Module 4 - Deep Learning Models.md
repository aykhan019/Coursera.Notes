

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFT5Z5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKcTjevFJt6AoKFrmo3WsceJEsfANvaYb%2FVtawsMw2oAiAFVNjmdnpR8ou7BoYFcz%2FYWVNHLo%2FHif6mWikBiJHlBSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2BBhCj5VaVP7XsnsDKtwDzlDd%2FkQrSOFFC0pmPaRHdhxvg%2FZbCe2Vw4YN7G9j44yaVf%2FLsTV%2FmCkSW6JAQZ3Cr8d0LEcJiB42jc6BjWHu1%2FXcHUn3V8xYYlKeGcS6fJcQhsPXIntogWDaFezhXWVWAixXtg0xFZIJfVd7QfPoHCyadz5o%2FoY6OblwHtkZDw3naBiTfiDf5vHQXKWOgoHmzgRy1BbwrOBLBS%2FakAnQk03%2Fk85AdLgdy9W3XTMZY7oKu5nl8P%2F7S%2FAVEEh9cI4TdkEGC7QS%2FryF0bzti%2BINqsP6%2BUtdZJuHJM9dA%2FHxjw8UZIc0iO05r6jM1yZuVwSvnhye4ciB9hL7v2v28OQdBQq%2FzUOfCf0PbCK8AnJBRb1Ai70rKpNBxwNHW540CXwmTzY0JSCbr5DsNl3gOvfipFQ85CgiVHArM9VsODxNIsIT0qLezjQMWuWFKDXK0Rj6w6VyUjHO9b0RvDHR4Cxbn1je4stBKksLhf2n3rpHrT4YOESH%2BnVs47Qnl1UPMGzg%2FD3n%2FBfStqkyPKNnxzVKXFycgAmwxbAg6uVqeHZCTiYiDErk5fZBN4O5eNvIGFT8ZgZ%2B4K4rhJoHmL%2BpUNHU4kd7bD851HyCOa0cW2uO5UdX8Hc9aB3GQdfwT5owtfOBvQY6pgGqU9kLQPw4YSgYbF%2FQiHONwCUKhc%2F9jdc5fvWEilA76ERtj%2BnFboLWxGwIZE%2BejEXRX5eYA9aviaqN8ENwSuxK6Gy7MMit9XyhY%2BgZuE8IliHnpxyGu6I%2BIKgbty5UvK6e7aSrVHrHQAM0irpfbWI4wzlD9h9ngvUdgVluf3i9sXwb%2FcTvSm0ylfYtRV%2Fidl4OK5%2BwUppxEuBjlNZkOkyjHmYj%2FQMQ&X-Amz-Signature=30274b01673fdec0eb2904bd6948f0254ebc0a2cb504e5ac33e02159fc87e42b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFT5Z5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKcTjevFJt6AoKFrmo3WsceJEsfANvaYb%2FVtawsMw2oAiAFVNjmdnpR8ou7BoYFcz%2FYWVNHLo%2FHif6mWikBiJHlBSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2BBhCj5VaVP7XsnsDKtwDzlDd%2FkQrSOFFC0pmPaRHdhxvg%2FZbCe2Vw4YN7G9j44yaVf%2FLsTV%2FmCkSW6JAQZ3Cr8d0LEcJiB42jc6BjWHu1%2FXcHUn3V8xYYlKeGcS6fJcQhsPXIntogWDaFezhXWVWAixXtg0xFZIJfVd7QfPoHCyadz5o%2FoY6OblwHtkZDw3naBiTfiDf5vHQXKWOgoHmzgRy1BbwrOBLBS%2FakAnQk03%2Fk85AdLgdy9W3XTMZY7oKu5nl8P%2F7S%2FAVEEh9cI4TdkEGC7QS%2FryF0bzti%2BINqsP6%2BUtdZJuHJM9dA%2FHxjw8UZIc0iO05r6jM1yZuVwSvnhye4ciB9hL7v2v28OQdBQq%2FzUOfCf0PbCK8AnJBRb1Ai70rKpNBxwNHW540CXwmTzY0JSCbr5DsNl3gOvfipFQ85CgiVHArM9VsODxNIsIT0qLezjQMWuWFKDXK0Rj6w6VyUjHO9b0RvDHR4Cxbn1je4stBKksLhf2n3rpHrT4YOESH%2BnVs47Qnl1UPMGzg%2FD3n%2FBfStqkyPKNnxzVKXFycgAmwxbAg6uVqeHZCTiYiDErk5fZBN4O5eNvIGFT8ZgZ%2B4K4rhJoHmL%2BpUNHU4kd7bD851HyCOa0cW2uO5UdX8Hc9aB3GQdfwT5owtfOBvQY6pgGqU9kLQPw4YSgYbF%2FQiHONwCUKhc%2F9jdc5fvWEilA76ERtj%2BnFboLWxGwIZE%2BejEXRX5eYA9aviaqN8ENwSuxK6Gy7MMit9XyhY%2BgZuE8IliHnpxyGu6I%2BIKgbty5UvK6e7aSrVHrHQAM0irpfbWI4wzlD9h9ngvUdgVluf3i9sXwb%2FcTvSm0ylfYtRV%2Fidl4OK5%2BwUppxEuBjlNZkOkyjHmYj%2FQMQ&X-Amz-Signature=0bff51ce5148e611384e4bf39c869ceb7f1caec68751d692ea1365f00e8f056e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFT5Z5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKcTjevFJt6AoKFrmo3WsceJEsfANvaYb%2FVtawsMw2oAiAFVNjmdnpR8ou7BoYFcz%2FYWVNHLo%2FHif6mWikBiJHlBSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2BBhCj5VaVP7XsnsDKtwDzlDd%2FkQrSOFFC0pmPaRHdhxvg%2FZbCe2Vw4YN7G9j44yaVf%2FLsTV%2FmCkSW6JAQZ3Cr8d0LEcJiB42jc6BjWHu1%2FXcHUn3V8xYYlKeGcS6fJcQhsPXIntogWDaFezhXWVWAixXtg0xFZIJfVd7QfPoHCyadz5o%2FoY6OblwHtkZDw3naBiTfiDf5vHQXKWOgoHmzgRy1BbwrOBLBS%2FakAnQk03%2Fk85AdLgdy9W3XTMZY7oKu5nl8P%2F7S%2FAVEEh9cI4TdkEGC7QS%2FryF0bzti%2BINqsP6%2BUtdZJuHJM9dA%2FHxjw8UZIc0iO05r6jM1yZuVwSvnhye4ciB9hL7v2v28OQdBQq%2FzUOfCf0PbCK8AnJBRb1Ai70rKpNBxwNHW540CXwmTzY0JSCbr5DsNl3gOvfipFQ85CgiVHArM9VsODxNIsIT0qLezjQMWuWFKDXK0Rj6w6VyUjHO9b0RvDHR4Cxbn1je4stBKksLhf2n3rpHrT4YOESH%2BnVs47Qnl1UPMGzg%2FD3n%2FBfStqkyPKNnxzVKXFycgAmwxbAg6uVqeHZCTiYiDErk5fZBN4O5eNvIGFT8ZgZ%2B4K4rhJoHmL%2BpUNHU4kd7bD851HyCOa0cW2uO5UdX8Hc9aB3GQdfwT5owtfOBvQY6pgGqU9kLQPw4YSgYbF%2FQiHONwCUKhc%2F9jdc5fvWEilA76ERtj%2BnFboLWxGwIZE%2BejEXRX5eYA9aviaqN8ENwSuxK6Gy7MMit9XyhY%2BgZuE8IliHnpxyGu6I%2BIKgbty5UvK6e7aSrVHrHQAM0irpfbWI4wzlD9h9ngvUdgVluf3i9sXwb%2FcTvSm0ylfYtRV%2Fidl4OK5%2BwUppxEuBjlNZkOkyjHmYj%2FQMQ&X-Amz-Signature=36595ad65c8a48384c7bacd16c74814a90723b103835ae74cf33c87e8914ec39&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFT5Z5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKcTjevFJt6AoKFrmo3WsceJEsfANvaYb%2FVtawsMw2oAiAFVNjmdnpR8ou7BoYFcz%2FYWVNHLo%2FHif6mWikBiJHlBSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2BBhCj5VaVP7XsnsDKtwDzlDd%2FkQrSOFFC0pmPaRHdhxvg%2FZbCe2Vw4YN7G9j44yaVf%2FLsTV%2FmCkSW6JAQZ3Cr8d0LEcJiB42jc6BjWHu1%2FXcHUn3V8xYYlKeGcS6fJcQhsPXIntogWDaFezhXWVWAixXtg0xFZIJfVd7QfPoHCyadz5o%2FoY6OblwHtkZDw3naBiTfiDf5vHQXKWOgoHmzgRy1BbwrOBLBS%2FakAnQk03%2Fk85AdLgdy9W3XTMZY7oKu5nl8P%2F7S%2FAVEEh9cI4TdkEGC7QS%2FryF0bzti%2BINqsP6%2BUtdZJuHJM9dA%2FHxjw8UZIc0iO05r6jM1yZuVwSvnhye4ciB9hL7v2v28OQdBQq%2FzUOfCf0PbCK8AnJBRb1Ai70rKpNBxwNHW540CXwmTzY0JSCbr5DsNl3gOvfipFQ85CgiVHArM9VsODxNIsIT0qLezjQMWuWFKDXK0Rj6w6VyUjHO9b0RvDHR4Cxbn1je4stBKksLhf2n3rpHrT4YOESH%2BnVs47Qnl1UPMGzg%2FD3n%2FBfStqkyPKNnxzVKXFycgAmwxbAg6uVqeHZCTiYiDErk5fZBN4O5eNvIGFT8ZgZ%2B4K4rhJoHmL%2BpUNHU4kd7bD851HyCOa0cW2uO5UdX8Hc9aB3GQdfwT5owtfOBvQY6pgGqU9kLQPw4YSgYbF%2FQiHONwCUKhc%2F9jdc5fvWEilA76ERtj%2BnFboLWxGwIZE%2BejEXRX5eYA9aviaqN8ENwSuxK6Gy7MMit9XyhY%2BgZuE8IliHnpxyGu6I%2BIKgbty5UvK6e7aSrVHrHQAM0irpfbWI4wzlD9h9ngvUdgVluf3i9sXwb%2FcTvSm0ylfYtRV%2Fidl4OK5%2BwUppxEuBjlNZkOkyjHmYj%2FQMQ&X-Amz-Signature=0e2c8729642ba8428cae1c2233fa5c94f55cb9b652bc6fca4bdc9077edfb7f67&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFT5Z5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKcTjevFJt6AoKFrmo3WsceJEsfANvaYb%2FVtawsMw2oAiAFVNjmdnpR8ou7BoYFcz%2FYWVNHLo%2FHif6mWikBiJHlBSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2BBhCj5VaVP7XsnsDKtwDzlDd%2FkQrSOFFC0pmPaRHdhxvg%2FZbCe2Vw4YN7G9j44yaVf%2FLsTV%2FmCkSW6JAQZ3Cr8d0LEcJiB42jc6BjWHu1%2FXcHUn3V8xYYlKeGcS6fJcQhsPXIntogWDaFezhXWVWAixXtg0xFZIJfVd7QfPoHCyadz5o%2FoY6OblwHtkZDw3naBiTfiDf5vHQXKWOgoHmzgRy1BbwrOBLBS%2FakAnQk03%2Fk85AdLgdy9W3XTMZY7oKu5nl8P%2F7S%2FAVEEh9cI4TdkEGC7QS%2FryF0bzti%2BINqsP6%2BUtdZJuHJM9dA%2FHxjw8UZIc0iO05r6jM1yZuVwSvnhye4ciB9hL7v2v28OQdBQq%2FzUOfCf0PbCK8AnJBRb1Ai70rKpNBxwNHW540CXwmTzY0JSCbr5DsNl3gOvfipFQ85CgiVHArM9VsODxNIsIT0qLezjQMWuWFKDXK0Rj6w6VyUjHO9b0RvDHR4Cxbn1je4stBKksLhf2n3rpHrT4YOESH%2BnVs47Qnl1UPMGzg%2FD3n%2FBfStqkyPKNnxzVKXFycgAmwxbAg6uVqeHZCTiYiDErk5fZBN4O5eNvIGFT8ZgZ%2B4K4rhJoHmL%2BpUNHU4kd7bD851HyCOa0cW2uO5UdX8Hc9aB3GQdfwT5owtfOBvQY6pgGqU9kLQPw4YSgYbF%2FQiHONwCUKhc%2F9jdc5fvWEilA76ERtj%2BnFboLWxGwIZE%2BejEXRX5eYA9aviaqN8ENwSuxK6Gy7MMit9XyhY%2BgZuE8IliHnpxyGu6I%2BIKgbty5UvK6e7aSrVHrHQAM0irpfbWI4wzlD9h9ngvUdgVluf3i9sXwb%2FcTvSm0ylfYtRV%2Fidl4OK5%2BwUppxEuBjlNZkOkyjHmYj%2FQMQ&X-Amz-Signature=adf51fe10ecf7c5fd302613db40365d5723dc4d4b637695c280e711ec946fd38&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFT5Z5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKcTjevFJt6AoKFrmo3WsceJEsfANvaYb%2FVtawsMw2oAiAFVNjmdnpR8ou7BoYFcz%2FYWVNHLo%2FHif6mWikBiJHlBSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2BBhCj5VaVP7XsnsDKtwDzlDd%2FkQrSOFFC0pmPaRHdhxvg%2FZbCe2Vw4YN7G9j44yaVf%2FLsTV%2FmCkSW6JAQZ3Cr8d0LEcJiB42jc6BjWHu1%2FXcHUn3V8xYYlKeGcS6fJcQhsPXIntogWDaFezhXWVWAixXtg0xFZIJfVd7QfPoHCyadz5o%2FoY6OblwHtkZDw3naBiTfiDf5vHQXKWOgoHmzgRy1BbwrOBLBS%2FakAnQk03%2Fk85AdLgdy9W3XTMZY7oKu5nl8P%2F7S%2FAVEEh9cI4TdkEGC7QS%2FryF0bzti%2BINqsP6%2BUtdZJuHJM9dA%2FHxjw8UZIc0iO05r6jM1yZuVwSvnhye4ciB9hL7v2v28OQdBQq%2FzUOfCf0PbCK8AnJBRb1Ai70rKpNBxwNHW540CXwmTzY0JSCbr5DsNl3gOvfipFQ85CgiVHArM9VsODxNIsIT0qLezjQMWuWFKDXK0Rj6w6VyUjHO9b0RvDHR4Cxbn1je4stBKksLhf2n3rpHrT4YOESH%2BnVs47Qnl1UPMGzg%2FD3n%2FBfStqkyPKNnxzVKXFycgAmwxbAg6uVqeHZCTiYiDErk5fZBN4O5eNvIGFT8ZgZ%2B4K4rhJoHmL%2BpUNHU4kd7bD851HyCOa0cW2uO5UdX8Hc9aB3GQdfwT5owtfOBvQY6pgGqU9kLQPw4YSgYbF%2FQiHONwCUKhc%2F9jdc5fvWEilA76ERtj%2BnFboLWxGwIZE%2BejEXRX5eYA9aviaqN8ENwSuxK6Gy7MMit9XyhY%2BgZuE8IliHnpxyGu6I%2BIKgbty5UvK6e7aSrVHrHQAM0irpfbWI4wzlD9h9ngvUdgVluf3i9sXwb%2FcTvSm0ylfYtRV%2Fidl4OK5%2BwUppxEuBjlNZkOkyjHmYj%2FQMQ&X-Amz-Signature=454f51718af3219a0308e0150148cfa126840f9e7450dec162d1904e610ba42e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFT5Z5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKcTjevFJt6AoKFrmo3WsceJEsfANvaYb%2FVtawsMw2oAiAFVNjmdnpR8ou7BoYFcz%2FYWVNHLo%2FHif6mWikBiJHlBSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2BBhCj5VaVP7XsnsDKtwDzlDd%2FkQrSOFFC0pmPaRHdhxvg%2FZbCe2Vw4YN7G9j44yaVf%2FLsTV%2FmCkSW6JAQZ3Cr8d0LEcJiB42jc6BjWHu1%2FXcHUn3V8xYYlKeGcS6fJcQhsPXIntogWDaFezhXWVWAixXtg0xFZIJfVd7QfPoHCyadz5o%2FoY6OblwHtkZDw3naBiTfiDf5vHQXKWOgoHmzgRy1BbwrOBLBS%2FakAnQk03%2Fk85AdLgdy9W3XTMZY7oKu5nl8P%2F7S%2FAVEEh9cI4TdkEGC7QS%2FryF0bzti%2BINqsP6%2BUtdZJuHJM9dA%2FHxjw8UZIc0iO05r6jM1yZuVwSvnhye4ciB9hL7v2v28OQdBQq%2FzUOfCf0PbCK8AnJBRb1Ai70rKpNBxwNHW540CXwmTzY0JSCbr5DsNl3gOvfipFQ85CgiVHArM9VsODxNIsIT0qLezjQMWuWFKDXK0Rj6w6VyUjHO9b0RvDHR4Cxbn1je4stBKksLhf2n3rpHrT4YOESH%2BnVs47Qnl1UPMGzg%2FD3n%2FBfStqkyPKNnxzVKXFycgAmwxbAg6uVqeHZCTiYiDErk5fZBN4O5eNvIGFT8ZgZ%2B4K4rhJoHmL%2BpUNHU4kd7bD851HyCOa0cW2uO5UdX8Hc9aB3GQdfwT5owtfOBvQY6pgGqU9kLQPw4YSgYbF%2FQiHONwCUKhc%2F9jdc5fvWEilA76ERtj%2BnFboLWxGwIZE%2BejEXRX5eYA9aviaqN8ENwSuxK6Gy7MMit9XyhY%2BgZuE8IliHnpxyGu6I%2BIKgbty5UvK6e7aSrVHrHQAM0irpfbWI4wzlD9h9ngvUdgVluf3i9sXwb%2FcTvSm0ylfYtRV%2Fidl4OK5%2BwUppxEuBjlNZkOkyjHmYj%2FQMQ&X-Amz-Signature=17b5761bb3e31e1417470abe3f23f898c205c0acb3db6c8c5f9aebb483013dac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFT5Z5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKcTjevFJt6AoKFrmo3WsceJEsfANvaYb%2FVtawsMw2oAiAFVNjmdnpR8ou7BoYFcz%2FYWVNHLo%2FHif6mWikBiJHlBSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2BBhCj5VaVP7XsnsDKtwDzlDd%2FkQrSOFFC0pmPaRHdhxvg%2FZbCe2Vw4YN7G9j44yaVf%2FLsTV%2FmCkSW6JAQZ3Cr8d0LEcJiB42jc6BjWHu1%2FXcHUn3V8xYYlKeGcS6fJcQhsPXIntogWDaFezhXWVWAixXtg0xFZIJfVd7QfPoHCyadz5o%2FoY6OblwHtkZDw3naBiTfiDf5vHQXKWOgoHmzgRy1BbwrOBLBS%2FakAnQk03%2Fk85AdLgdy9W3XTMZY7oKu5nl8P%2F7S%2FAVEEh9cI4TdkEGC7QS%2FryF0bzti%2BINqsP6%2BUtdZJuHJM9dA%2FHxjw8UZIc0iO05r6jM1yZuVwSvnhye4ciB9hL7v2v28OQdBQq%2FzUOfCf0PbCK8AnJBRb1Ai70rKpNBxwNHW540CXwmTzY0JSCbr5DsNl3gOvfipFQ85CgiVHArM9VsODxNIsIT0qLezjQMWuWFKDXK0Rj6w6VyUjHO9b0RvDHR4Cxbn1je4stBKksLhf2n3rpHrT4YOESH%2BnVs47Qnl1UPMGzg%2FD3n%2FBfStqkyPKNnxzVKXFycgAmwxbAg6uVqeHZCTiYiDErk5fZBN4O5eNvIGFT8ZgZ%2B4K4rhJoHmL%2BpUNHU4kd7bD851HyCOa0cW2uO5UdX8Hc9aB3GQdfwT5owtfOBvQY6pgGqU9kLQPw4YSgYbF%2FQiHONwCUKhc%2F9jdc5fvWEilA76ERtj%2BnFboLWxGwIZE%2BejEXRX5eYA9aviaqN8ENwSuxK6Gy7MMit9XyhY%2BgZuE8IliHnpxyGu6I%2BIKgbty5UvK6e7aSrVHrHQAM0irpfbWI4wzlD9h9ngvUdgVluf3i9sXwb%2FcTvSm0ylfYtRV%2Fidl4OK5%2BwUppxEuBjlNZkOkyjHmYj%2FQMQ&X-Amz-Signature=39558c03ad8fa70895642d7f1bb7a6e39cbde04643964b2b5454021fdb600a05&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFT5Z5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKcTjevFJt6AoKFrmo3WsceJEsfANvaYb%2FVtawsMw2oAiAFVNjmdnpR8ou7BoYFcz%2FYWVNHLo%2FHif6mWikBiJHlBSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2BBhCj5VaVP7XsnsDKtwDzlDd%2FkQrSOFFC0pmPaRHdhxvg%2FZbCe2Vw4YN7G9j44yaVf%2FLsTV%2FmCkSW6JAQZ3Cr8d0LEcJiB42jc6BjWHu1%2FXcHUn3V8xYYlKeGcS6fJcQhsPXIntogWDaFezhXWVWAixXtg0xFZIJfVd7QfPoHCyadz5o%2FoY6OblwHtkZDw3naBiTfiDf5vHQXKWOgoHmzgRy1BbwrOBLBS%2FakAnQk03%2Fk85AdLgdy9W3XTMZY7oKu5nl8P%2F7S%2FAVEEh9cI4TdkEGC7QS%2FryF0bzti%2BINqsP6%2BUtdZJuHJM9dA%2FHxjw8UZIc0iO05r6jM1yZuVwSvnhye4ciB9hL7v2v28OQdBQq%2FzUOfCf0PbCK8AnJBRb1Ai70rKpNBxwNHW540CXwmTzY0JSCbr5DsNl3gOvfipFQ85CgiVHArM9VsODxNIsIT0qLezjQMWuWFKDXK0Rj6w6VyUjHO9b0RvDHR4Cxbn1je4stBKksLhf2n3rpHrT4YOESH%2BnVs47Qnl1UPMGzg%2FD3n%2FBfStqkyPKNnxzVKXFycgAmwxbAg6uVqeHZCTiYiDErk5fZBN4O5eNvIGFT8ZgZ%2B4K4rhJoHmL%2BpUNHU4kd7bD851HyCOa0cW2uO5UdX8Hc9aB3GQdfwT5owtfOBvQY6pgGqU9kLQPw4YSgYbF%2FQiHONwCUKhc%2F9jdc5fvWEilA76ERtj%2BnFboLWxGwIZE%2BejEXRX5eYA9aviaqN8ENwSuxK6Gy7MMit9XyhY%2BgZuE8IliHnpxyGu6I%2BIKgbty5UvK6e7aSrVHrHQAM0irpfbWI4wzlD9h9ngvUdgVluf3i9sXwb%2FcTvSm0ylfYtRV%2Fidl4OK5%2BwUppxEuBjlNZkOkyjHmYj%2FQMQ&X-Amz-Signature=98b5333ff30c47a53715dc91ff4c940194a7c63f2d8b2d4090d1b59f4b44cb05&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQZOAZM3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDk068etIEAIbw8M49nB%2Bq2eiCwhTeZXq2hxdEYfauXQgIhAP8zxlb2YJkjTPUcAKD66P7tCj4k8vIZ4%2BI4R2cz6FtdKv8DCBEQABoMNjM3NDIzMTgzODA1Igz2b8eco4bMHd%2BZzc4q3AP31Oo%2BYu30ctZ2HoW6dHMG2evYDVmYVkKx1TsM5fwNuaXZ3yHoxGzP7P9FrgkgI6q3%2FBhvxZyEZ%2BwMltDrT9KzYvy6zxFBGxDvmLuTIusdLn%2FoG1QIb7BmlrT7QAcwnn7TFWDufQa8uGgJ2F%2F3n0iNZP6hsNXY7%2FwmCmXReSCR5DZzDIZ3VpT3CUz5zZX1FnTlkBYhEoqGaf5heeOqSe4dt0pFX3QodkMyJANMBGDaRR%2FoJnDnR6aa3W0FGmzfT%2FuIAONt7ciacXnCclzMbCFlyY1U87gotT1a9o8y5TlK1yWnEVA4meFwAybEAdCwX6WbKe0jcs00Z9iFiguHNrxA2SBikH8AL%2BWwUqsjPonQXW%2FSrTm1fqN%2B%2FpZUO9NPl66EZeSAkh4iOk8phIck4XEx%2FE7Lym6miwjxJfNGOAobuYXrVC5W55%2F0wPukSP9RcRk50Q34tT9TrVZ0aewNxId5LvNPWX%2B8H3%2FLauVtqEAanvyIcYavw8L053A6D9cysbDrLqn5zTGv6dW62o%2FJl7aLD6yVOUSonbFzitN5mYMK7uCPvh4TSQegK%2BulFjVlxNIHVNhvFvXlCFv6O8gL7Qpe%2BJXCyo3FpikO4eqATm2uO3dR2HYS%2FZmiVj9vazDo8oG9BjqkAVJuPdhxtx0NU2LGpTVsNLqLRwjSrp0E55wqrXsQFIYNowiQKe7RebcnO71gHjb6PrgpA0zjJa1LnXyIwwwtS%2FKlbKzzL96KXlfBAk5Y1AJXRa%2FivIFB98KmzoYOoqPqZHWWoTYgc3AVDmbT0iNU8OZNAT9Hyz4Hm2MANPTbz2eIilhPN0HnkumdRe%2BpWI3CsKtziv7qP%2By6PXgnO8GueZqvW4U2&X-Amz-Signature=a2360a3ff1d262fde7786e8b15d521825cb3f1d0495342e479e6deae4bdf45e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQZOAZM3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDk068etIEAIbw8M49nB%2Bq2eiCwhTeZXq2hxdEYfauXQgIhAP8zxlb2YJkjTPUcAKD66P7tCj4k8vIZ4%2BI4R2cz6FtdKv8DCBEQABoMNjM3NDIzMTgzODA1Igz2b8eco4bMHd%2BZzc4q3AP31Oo%2BYu30ctZ2HoW6dHMG2evYDVmYVkKx1TsM5fwNuaXZ3yHoxGzP7P9FrgkgI6q3%2FBhvxZyEZ%2BwMltDrT9KzYvy6zxFBGxDvmLuTIusdLn%2FoG1QIb7BmlrT7QAcwnn7TFWDufQa8uGgJ2F%2F3n0iNZP6hsNXY7%2FwmCmXReSCR5DZzDIZ3VpT3CUz5zZX1FnTlkBYhEoqGaf5heeOqSe4dt0pFX3QodkMyJANMBGDaRR%2FoJnDnR6aa3W0FGmzfT%2FuIAONt7ciacXnCclzMbCFlyY1U87gotT1a9o8y5TlK1yWnEVA4meFwAybEAdCwX6WbKe0jcs00Z9iFiguHNrxA2SBikH8AL%2BWwUqsjPonQXW%2FSrTm1fqN%2B%2FpZUO9NPl66EZeSAkh4iOk8phIck4XEx%2FE7Lym6miwjxJfNGOAobuYXrVC5W55%2F0wPukSP9RcRk50Q34tT9TrVZ0aewNxId5LvNPWX%2B8H3%2FLauVtqEAanvyIcYavw8L053A6D9cysbDrLqn5zTGv6dW62o%2FJl7aLD6yVOUSonbFzitN5mYMK7uCPvh4TSQegK%2BulFjVlxNIHVNhvFvXlCFv6O8gL7Qpe%2BJXCyo3FpikO4eqATm2uO3dR2HYS%2FZmiVj9vazDo8oG9BjqkAVJuPdhxtx0NU2LGpTVsNLqLRwjSrp0E55wqrXsQFIYNowiQKe7RebcnO71gHjb6PrgpA0zjJa1LnXyIwwwtS%2FKlbKzzL96KXlfBAk5Y1AJXRa%2FivIFB98KmzoYOoqPqZHWWoTYgc3AVDmbT0iNU8OZNAT9Hyz4Hm2MANPTbz2eIilhPN0HnkumdRe%2BpWI3CsKtziv7qP%2By6PXgnO8GueZqvW4U2&X-Amz-Signature=c83b277950df32ef30ea8d65ca91913e576d81ad88582271834896bde4937d85&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
