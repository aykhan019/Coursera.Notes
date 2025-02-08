

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQKOWKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQCIP3TJeoEloZnjsLnRQXLWr2D%2Fd247Xu7qxXZLQI6b6QIgeY%2BK7PEZKLm%2BmQ%2BqxITzXxJSa9rS%2FA8bn3vtejdwIroqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOsEg7UclWwmAF0THCrcA%2Bu4sJOzt5G0SCH6pjinfGSCQ201yGaR0C0mh8TBrlXU7%2Bwy5jcXgbB4AkBmDQvBN%2FNpVEXoNdhK2qgOxEcqwjh2wY95P4%2Ba%2BM1L4nH7qZCPEcTTyvRD9j4Jo0KMrW1TjX3Hc3zt5InHCDY3fQsRFSzrm%2Flie6fXyOrK06Vs4XgO2inbZIvryhr9tYw8zW4hx4ANWSavkcuWPtFqiyeFw2zzOJ6jWIo9WzFwcNS%2BlkhMNSUN8um0laAogJtMeY88BQRJX7rTd1pIugCXX6oMFL6eCbj5nuHJzjSI0%2BfIedigNRCBwJ7GMl9Df9kzomv9mJTEaqKwueLJsKzzCA%2BmRRyR3PslCEFf4U%2BY7%2BMD8JMUFJ6b2cNdDhifYPosuzu2QmLkmwlzcfQGzpPEp%2BLm3I%2BautixFIlI7nImV%2FTl9HP8mkMtYSwcJ7K%2BQ98D3futbLXYwx0Z9ze17znSeL2PLHoN3S3YmgcpRAIJvxBInBXhT%2F6uzlysQlqo9CeEU2YEFbfTqPmVWQzpq88zCmxeJiZeA23OmTefd1ZtnVjoNtqzCXbPCWI6qYZZibJ9LeYnXaXEH%2Brh4k2vftaSlzz%2FAKbbB6wxaMe6rJKicjnk2Ueh6579uLTqlYUrSqXoMN2%2Bmr0GOqUBGTdiyJ9pafBCx%2Fco%2BrH3RyZJXgwdIiTvs1bUn3i2RNuCZk4uahMVJqgGWzuQqZvgcPsY9sLrnsTk6Dmt71FRfo63etj%2F3USO9hCh0PZykJvB5PxONs8WNRn27fQFoASjlLgtuqEUtWqJWFakGi3KOfllBIGMtiBAv9qQ%2B1krbM5fKnTOqHkJkS3ss%2Fu6HurxdTw7ubJOnF0fFNIpuxmus3JEgz9T&X-Amz-Signature=177b1af497ebe4cd70cdae79cfc2537731814f3b43ec7b93cdac0693f6524be2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQKOWKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQCIP3TJeoEloZnjsLnRQXLWr2D%2Fd247Xu7qxXZLQI6b6QIgeY%2BK7PEZKLm%2BmQ%2BqxITzXxJSa9rS%2FA8bn3vtejdwIroqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOsEg7UclWwmAF0THCrcA%2Bu4sJOzt5G0SCH6pjinfGSCQ201yGaR0C0mh8TBrlXU7%2Bwy5jcXgbB4AkBmDQvBN%2FNpVEXoNdhK2qgOxEcqwjh2wY95P4%2Ba%2BM1L4nH7qZCPEcTTyvRD9j4Jo0KMrW1TjX3Hc3zt5InHCDY3fQsRFSzrm%2Flie6fXyOrK06Vs4XgO2inbZIvryhr9tYw8zW4hx4ANWSavkcuWPtFqiyeFw2zzOJ6jWIo9WzFwcNS%2BlkhMNSUN8um0laAogJtMeY88BQRJX7rTd1pIugCXX6oMFL6eCbj5nuHJzjSI0%2BfIedigNRCBwJ7GMl9Df9kzomv9mJTEaqKwueLJsKzzCA%2BmRRyR3PslCEFf4U%2BY7%2BMD8JMUFJ6b2cNdDhifYPosuzu2QmLkmwlzcfQGzpPEp%2BLm3I%2BautixFIlI7nImV%2FTl9HP8mkMtYSwcJ7K%2BQ98D3futbLXYwx0Z9ze17znSeL2PLHoN3S3YmgcpRAIJvxBInBXhT%2F6uzlysQlqo9CeEU2YEFbfTqPmVWQzpq88zCmxeJiZeA23OmTefd1ZtnVjoNtqzCXbPCWI6qYZZibJ9LeYnXaXEH%2Brh4k2vftaSlzz%2FAKbbB6wxaMe6rJKicjnk2Ueh6579uLTqlYUrSqXoMN2%2Bmr0GOqUBGTdiyJ9pafBCx%2Fco%2BrH3RyZJXgwdIiTvs1bUn3i2RNuCZk4uahMVJqgGWzuQqZvgcPsY9sLrnsTk6Dmt71FRfo63etj%2F3USO9hCh0PZykJvB5PxONs8WNRn27fQFoASjlLgtuqEUtWqJWFakGi3KOfllBIGMtiBAv9qQ%2B1krbM5fKnTOqHkJkS3ss%2Fu6HurxdTw7ubJOnF0fFNIpuxmus3JEgz9T&X-Amz-Signature=153b9c1082dffab92205d6aa63d7dcb144783841b1a0eb9eb653bc9cfd2ea876&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQKOWKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQCIP3TJeoEloZnjsLnRQXLWr2D%2Fd247Xu7qxXZLQI6b6QIgeY%2BK7PEZKLm%2BmQ%2BqxITzXxJSa9rS%2FA8bn3vtejdwIroqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOsEg7UclWwmAF0THCrcA%2Bu4sJOzt5G0SCH6pjinfGSCQ201yGaR0C0mh8TBrlXU7%2Bwy5jcXgbB4AkBmDQvBN%2FNpVEXoNdhK2qgOxEcqwjh2wY95P4%2Ba%2BM1L4nH7qZCPEcTTyvRD9j4Jo0KMrW1TjX3Hc3zt5InHCDY3fQsRFSzrm%2Flie6fXyOrK06Vs4XgO2inbZIvryhr9tYw8zW4hx4ANWSavkcuWPtFqiyeFw2zzOJ6jWIo9WzFwcNS%2BlkhMNSUN8um0laAogJtMeY88BQRJX7rTd1pIugCXX6oMFL6eCbj5nuHJzjSI0%2BfIedigNRCBwJ7GMl9Df9kzomv9mJTEaqKwueLJsKzzCA%2BmRRyR3PslCEFf4U%2BY7%2BMD8JMUFJ6b2cNdDhifYPosuzu2QmLkmwlzcfQGzpPEp%2BLm3I%2BautixFIlI7nImV%2FTl9HP8mkMtYSwcJ7K%2BQ98D3futbLXYwx0Z9ze17znSeL2PLHoN3S3YmgcpRAIJvxBInBXhT%2F6uzlysQlqo9CeEU2YEFbfTqPmVWQzpq88zCmxeJiZeA23OmTefd1ZtnVjoNtqzCXbPCWI6qYZZibJ9LeYnXaXEH%2Brh4k2vftaSlzz%2FAKbbB6wxaMe6rJKicjnk2Ueh6579uLTqlYUrSqXoMN2%2Bmr0GOqUBGTdiyJ9pafBCx%2Fco%2BrH3RyZJXgwdIiTvs1bUn3i2RNuCZk4uahMVJqgGWzuQqZvgcPsY9sLrnsTk6Dmt71FRfo63etj%2F3USO9hCh0PZykJvB5PxONs8WNRn27fQFoASjlLgtuqEUtWqJWFakGi3KOfllBIGMtiBAv9qQ%2B1krbM5fKnTOqHkJkS3ss%2Fu6HurxdTw7ubJOnF0fFNIpuxmus3JEgz9T&X-Amz-Signature=158f8d9213dfd4c001094c4e4f5073ff9a7723e6f3d51e85ff6090bc7c4dd956&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQKOWKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQCIP3TJeoEloZnjsLnRQXLWr2D%2Fd247Xu7qxXZLQI6b6QIgeY%2BK7PEZKLm%2BmQ%2BqxITzXxJSa9rS%2FA8bn3vtejdwIroqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOsEg7UclWwmAF0THCrcA%2Bu4sJOzt5G0SCH6pjinfGSCQ201yGaR0C0mh8TBrlXU7%2Bwy5jcXgbB4AkBmDQvBN%2FNpVEXoNdhK2qgOxEcqwjh2wY95P4%2Ba%2BM1L4nH7qZCPEcTTyvRD9j4Jo0KMrW1TjX3Hc3zt5InHCDY3fQsRFSzrm%2Flie6fXyOrK06Vs4XgO2inbZIvryhr9tYw8zW4hx4ANWSavkcuWPtFqiyeFw2zzOJ6jWIo9WzFwcNS%2BlkhMNSUN8um0laAogJtMeY88BQRJX7rTd1pIugCXX6oMFL6eCbj5nuHJzjSI0%2BfIedigNRCBwJ7GMl9Df9kzomv9mJTEaqKwueLJsKzzCA%2BmRRyR3PslCEFf4U%2BY7%2BMD8JMUFJ6b2cNdDhifYPosuzu2QmLkmwlzcfQGzpPEp%2BLm3I%2BautixFIlI7nImV%2FTl9HP8mkMtYSwcJ7K%2BQ98D3futbLXYwx0Z9ze17znSeL2PLHoN3S3YmgcpRAIJvxBInBXhT%2F6uzlysQlqo9CeEU2YEFbfTqPmVWQzpq88zCmxeJiZeA23OmTefd1ZtnVjoNtqzCXbPCWI6qYZZibJ9LeYnXaXEH%2Brh4k2vftaSlzz%2FAKbbB6wxaMe6rJKicjnk2Ueh6579uLTqlYUrSqXoMN2%2Bmr0GOqUBGTdiyJ9pafBCx%2Fco%2BrH3RyZJXgwdIiTvs1bUn3i2RNuCZk4uahMVJqgGWzuQqZvgcPsY9sLrnsTk6Dmt71FRfo63etj%2F3USO9hCh0PZykJvB5PxONs8WNRn27fQFoASjlLgtuqEUtWqJWFakGi3KOfllBIGMtiBAv9qQ%2B1krbM5fKnTOqHkJkS3ss%2Fu6HurxdTw7ubJOnF0fFNIpuxmus3JEgz9T&X-Amz-Signature=e6905df2dba6b5658fd1db87ff4fb4825332f9e9e61181d0bd9921fd71145662&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQKOWKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQCIP3TJeoEloZnjsLnRQXLWr2D%2Fd247Xu7qxXZLQI6b6QIgeY%2BK7PEZKLm%2BmQ%2BqxITzXxJSa9rS%2FA8bn3vtejdwIroqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOsEg7UclWwmAF0THCrcA%2Bu4sJOzt5G0SCH6pjinfGSCQ201yGaR0C0mh8TBrlXU7%2Bwy5jcXgbB4AkBmDQvBN%2FNpVEXoNdhK2qgOxEcqwjh2wY95P4%2Ba%2BM1L4nH7qZCPEcTTyvRD9j4Jo0KMrW1TjX3Hc3zt5InHCDY3fQsRFSzrm%2Flie6fXyOrK06Vs4XgO2inbZIvryhr9tYw8zW4hx4ANWSavkcuWPtFqiyeFw2zzOJ6jWIo9WzFwcNS%2BlkhMNSUN8um0laAogJtMeY88BQRJX7rTd1pIugCXX6oMFL6eCbj5nuHJzjSI0%2BfIedigNRCBwJ7GMl9Df9kzomv9mJTEaqKwueLJsKzzCA%2BmRRyR3PslCEFf4U%2BY7%2BMD8JMUFJ6b2cNdDhifYPosuzu2QmLkmwlzcfQGzpPEp%2BLm3I%2BautixFIlI7nImV%2FTl9HP8mkMtYSwcJ7K%2BQ98D3futbLXYwx0Z9ze17znSeL2PLHoN3S3YmgcpRAIJvxBInBXhT%2F6uzlysQlqo9CeEU2YEFbfTqPmVWQzpq88zCmxeJiZeA23OmTefd1ZtnVjoNtqzCXbPCWI6qYZZibJ9LeYnXaXEH%2Brh4k2vftaSlzz%2FAKbbB6wxaMe6rJKicjnk2Ueh6579uLTqlYUrSqXoMN2%2Bmr0GOqUBGTdiyJ9pafBCx%2Fco%2BrH3RyZJXgwdIiTvs1bUn3i2RNuCZk4uahMVJqgGWzuQqZvgcPsY9sLrnsTk6Dmt71FRfo63etj%2F3USO9hCh0PZykJvB5PxONs8WNRn27fQFoASjlLgtuqEUtWqJWFakGi3KOfllBIGMtiBAv9qQ%2B1krbM5fKnTOqHkJkS3ss%2Fu6HurxdTw7ubJOnF0fFNIpuxmus3JEgz9T&X-Amz-Signature=d4de3b4732b193fa7f254d740da71a83cb7b80e80a4a1a3bf5842335d2a7cd47&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQKOWKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQCIP3TJeoEloZnjsLnRQXLWr2D%2Fd247Xu7qxXZLQI6b6QIgeY%2BK7PEZKLm%2BmQ%2BqxITzXxJSa9rS%2FA8bn3vtejdwIroqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOsEg7UclWwmAF0THCrcA%2Bu4sJOzt5G0SCH6pjinfGSCQ201yGaR0C0mh8TBrlXU7%2Bwy5jcXgbB4AkBmDQvBN%2FNpVEXoNdhK2qgOxEcqwjh2wY95P4%2Ba%2BM1L4nH7qZCPEcTTyvRD9j4Jo0KMrW1TjX3Hc3zt5InHCDY3fQsRFSzrm%2Flie6fXyOrK06Vs4XgO2inbZIvryhr9tYw8zW4hx4ANWSavkcuWPtFqiyeFw2zzOJ6jWIo9WzFwcNS%2BlkhMNSUN8um0laAogJtMeY88BQRJX7rTd1pIugCXX6oMFL6eCbj5nuHJzjSI0%2BfIedigNRCBwJ7GMl9Df9kzomv9mJTEaqKwueLJsKzzCA%2BmRRyR3PslCEFf4U%2BY7%2BMD8JMUFJ6b2cNdDhifYPosuzu2QmLkmwlzcfQGzpPEp%2BLm3I%2BautixFIlI7nImV%2FTl9HP8mkMtYSwcJ7K%2BQ98D3futbLXYwx0Z9ze17znSeL2PLHoN3S3YmgcpRAIJvxBInBXhT%2F6uzlysQlqo9CeEU2YEFbfTqPmVWQzpq88zCmxeJiZeA23OmTefd1ZtnVjoNtqzCXbPCWI6qYZZibJ9LeYnXaXEH%2Brh4k2vftaSlzz%2FAKbbB6wxaMe6rJKicjnk2Ueh6579uLTqlYUrSqXoMN2%2Bmr0GOqUBGTdiyJ9pafBCx%2Fco%2BrH3RyZJXgwdIiTvs1bUn3i2RNuCZk4uahMVJqgGWzuQqZvgcPsY9sLrnsTk6Dmt71FRfo63etj%2F3USO9hCh0PZykJvB5PxONs8WNRn27fQFoASjlLgtuqEUtWqJWFakGi3KOfllBIGMtiBAv9qQ%2B1krbM5fKnTOqHkJkS3ss%2Fu6HurxdTw7ubJOnF0fFNIpuxmus3JEgz9T&X-Amz-Signature=127f8a9cc6902636a3da0cad682518777645f37f9b121185a487200605334d72&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQKOWKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQCIP3TJeoEloZnjsLnRQXLWr2D%2Fd247Xu7qxXZLQI6b6QIgeY%2BK7PEZKLm%2BmQ%2BqxITzXxJSa9rS%2FA8bn3vtejdwIroqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOsEg7UclWwmAF0THCrcA%2Bu4sJOzt5G0SCH6pjinfGSCQ201yGaR0C0mh8TBrlXU7%2Bwy5jcXgbB4AkBmDQvBN%2FNpVEXoNdhK2qgOxEcqwjh2wY95P4%2Ba%2BM1L4nH7qZCPEcTTyvRD9j4Jo0KMrW1TjX3Hc3zt5InHCDY3fQsRFSzrm%2Flie6fXyOrK06Vs4XgO2inbZIvryhr9tYw8zW4hx4ANWSavkcuWPtFqiyeFw2zzOJ6jWIo9WzFwcNS%2BlkhMNSUN8um0laAogJtMeY88BQRJX7rTd1pIugCXX6oMFL6eCbj5nuHJzjSI0%2BfIedigNRCBwJ7GMl9Df9kzomv9mJTEaqKwueLJsKzzCA%2BmRRyR3PslCEFf4U%2BY7%2BMD8JMUFJ6b2cNdDhifYPosuzu2QmLkmwlzcfQGzpPEp%2BLm3I%2BautixFIlI7nImV%2FTl9HP8mkMtYSwcJ7K%2BQ98D3futbLXYwx0Z9ze17znSeL2PLHoN3S3YmgcpRAIJvxBInBXhT%2F6uzlysQlqo9CeEU2YEFbfTqPmVWQzpq88zCmxeJiZeA23OmTefd1ZtnVjoNtqzCXbPCWI6qYZZibJ9LeYnXaXEH%2Brh4k2vftaSlzz%2FAKbbB6wxaMe6rJKicjnk2Ueh6579uLTqlYUrSqXoMN2%2Bmr0GOqUBGTdiyJ9pafBCx%2Fco%2BrH3RyZJXgwdIiTvs1bUn3i2RNuCZk4uahMVJqgGWzuQqZvgcPsY9sLrnsTk6Dmt71FRfo63etj%2F3USO9hCh0PZykJvB5PxONs8WNRn27fQFoASjlLgtuqEUtWqJWFakGi3KOfllBIGMtiBAv9qQ%2B1krbM5fKnTOqHkJkS3ss%2Fu6HurxdTw7ubJOnF0fFNIpuxmus3JEgz9T&X-Amz-Signature=9885bc77b6afaca8382668cf624af8c9c8c1adf7ad8d2b04fbbba7ee1512d6bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQKOWKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQCIP3TJeoEloZnjsLnRQXLWr2D%2Fd247Xu7qxXZLQI6b6QIgeY%2BK7PEZKLm%2BmQ%2BqxITzXxJSa9rS%2FA8bn3vtejdwIroqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOsEg7UclWwmAF0THCrcA%2Bu4sJOzt5G0SCH6pjinfGSCQ201yGaR0C0mh8TBrlXU7%2Bwy5jcXgbB4AkBmDQvBN%2FNpVEXoNdhK2qgOxEcqwjh2wY95P4%2Ba%2BM1L4nH7qZCPEcTTyvRD9j4Jo0KMrW1TjX3Hc3zt5InHCDY3fQsRFSzrm%2Flie6fXyOrK06Vs4XgO2inbZIvryhr9tYw8zW4hx4ANWSavkcuWPtFqiyeFw2zzOJ6jWIo9WzFwcNS%2BlkhMNSUN8um0laAogJtMeY88BQRJX7rTd1pIugCXX6oMFL6eCbj5nuHJzjSI0%2BfIedigNRCBwJ7GMl9Df9kzomv9mJTEaqKwueLJsKzzCA%2BmRRyR3PslCEFf4U%2BY7%2BMD8JMUFJ6b2cNdDhifYPosuzu2QmLkmwlzcfQGzpPEp%2BLm3I%2BautixFIlI7nImV%2FTl9HP8mkMtYSwcJ7K%2BQ98D3futbLXYwx0Z9ze17znSeL2PLHoN3S3YmgcpRAIJvxBInBXhT%2F6uzlysQlqo9CeEU2YEFbfTqPmVWQzpq88zCmxeJiZeA23OmTefd1ZtnVjoNtqzCXbPCWI6qYZZibJ9LeYnXaXEH%2Brh4k2vftaSlzz%2FAKbbB6wxaMe6rJKicjnk2Ueh6579uLTqlYUrSqXoMN2%2Bmr0GOqUBGTdiyJ9pafBCx%2Fco%2BrH3RyZJXgwdIiTvs1bUn3i2RNuCZk4uahMVJqgGWzuQqZvgcPsY9sLrnsTk6Dmt71FRfo63etj%2F3USO9hCh0PZykJvB5PxONs8WNRn27fQFoASjlLgtuqEUtWqJWFakGi3KOfllBIGMtiBAv9qQ%2B1krbM5fKnTOqHkJkS3ss%2Fu6HurxdTw7ubJOnF0fFNIpuxmus3JEgz9T&X-Amz-Signature=c9548e797852b3fd33d3c3271d0246e5057f4a38f735352ce32bab1c0959ea44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQKOWKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQCIP3TJeoEloZnjsLnRQXLWr2D%2Fd247Xu7qxXZLQI6b6QIgeY%2BK7PEZKLm%2BmQ%2BqxITzXxJSa9rS%2FA8bn3vtejdwIroqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOsEg7UclWwmAF0THCrcA%2Bu4sJOzt5G0SCH6pjinfGSCQ201yGaR0C0mh8TBrlXU7%2Bwy5jcXgbB4AkBmDQvBN%2FNpVEXoNdhK2qgOxEcqwjh2wY95P4%2Ba%2BM1L4nH7qZCPEcTTyvRD9j4Jo0KMrW1TjX3Hc3zt5InHCDY3fQsRFSzrm%2Flie6fXyOrK06Vs4XgO2inbZIvryhr9tYw8zW4hx4ANWSavkcuWPtFqiyeFw2zzOJ6jWIo9WzFwcNS%2BlkhMNSUN8um0laAogJtMeY88BQRJX7rTd1pIugCXX6oMFL6eCbj5nuHJzjSI0%2BfIedigNRCBwJ7GMl9Df9kzomv9mJTEaqKwueLJsKzzCA%2BmRRyR3PslCEFf4U%2BY7%2BMD8JMUFJ6b2cNdDhifYPosuzu2QmLkmwlzcfQGzpPEp%2BLm3I%2BautixFIlI7nImV%2FTl9HP8mkMtYSwcJ7K%2BQ98D3futbLXYwx0Z9ze17znSeL2PLHoN3S3YmgcpRAIJvxBInBXhT%2F6uzlysQlqo9CeEU2YEFbfTqPmVWQzpq88zCmxeJiZeA23OmTefd1ZtnVjoNtqzCXbPCWI6qYZZibJ9LeYnXaXEH%2Brh4k2vftaSlzz%2FAKbbB6wxaMe6rJKicjnk2Ueh6579uLTqlYUrSqXoMN2%2Bmr0GOqUBGTdiyJ9pafBCx%2Fco%2BrH3RyZJXgwdIiTvs1bUn3i2RNuCZk4uahMVJqgGWzuQqZvgcPsY9sLrnsTk6Dmt71FRfo63etj%2F3USO9hCh0PZykJvB5PxONs8WNRn27fQFoASjlLgtuqEUtWqJWFakGi3KOfllBIGMtiBAv9qQ%2B1krbM5fKnTOqHkJkS3ss%2Fu6HurxdTw7ubJOnF0fFNIpuxmus3JEgz9T&X-Amz-Signature=8eeedfb3466f2b31c0345a276e9d952baa2008fb17ac67162de9b993ba0613f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVGUNNUK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIFEB5BmdjhMBCCRuzKIfRQeBzOAaHMkcrugcUsJryMAlAiEAgQaLmeuvWD32mVMGgSaO%2BBBj8vO5HX4d5S2CunXJfUAqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJJZc5Lo6suwhMMOyrcA3%2FLXLl%2FfSIvOc4SzJ5yMOlUW2Ar9rnLfW%2FdI4CC%2B2o5S%2FD5ICN%2BPjnuVhy1%2BPHhVF6ABL4doltxzw54aSAI93SdUhpDot9QDwu5cMPXbOoZhgKR6WmbDFjOR2xK754iiXUh53kWED1xSJlXU3Rz4hSaSZ8yOzaT9h%2F0wYUyJdaBxGN3UCibWHhmPZb9x%2Bn3yOoRkeZPm4Y9aw%2BsgnHHYPy9T9h25GPpw4S3fmjqkrfT1B2pkkH6HtR5Ewc4vqpHJIeeg8Nfc2F8PzxHBAHS1TvJrFVMH7D%2BZ%2Fnnzk%2BtAnceE1iTs2qGhshHIl%2FjRecrHFM%2F2%2BjjrIvhc3fEEmsvIl4C%2Balvdqrq7SVfMDP%2Fn%2BCKg13udAc7yzOZ4FjSTwigLu77mE8QKScqRuED%2FNWP%2FYMrtgoNZoNrBzw585oeX7cuq%2B4VC5vjzUMqR%2FCJTVIK5XZwqcPGnP6EgolRA8Mt583sSPrfnLJRo2FtbOuW4tewcqeeoedUkRLWkWq5Afx0frBXC5bDTm9gzZ0%2FoLP9CCfWHuRWZJnX%2BWdaDaOtGrpcae0IrHuCzsJjEZhGrQS7PZdUAy4MZd4qguWebxUTVkHpoZlQ7ZV8FkMam%2FhcO9srOcmD07CGHnwKaWzFMMO%2Bmr0GOqUBJugfgdKIwLCHKHkLhgUPx1ChMw0yCaNSzXlbpcEKT9wBGgO7CYfoWtnPhiZFHXa6vAF6GUoB%2BXZ3K3o9OgneV9RLyRGRbGsasBrg9Lv8gWjfx4RMFHSCMR96KqZgvbag7QQZ79blk0DEVqZi5EldT0DPGzdd1nMnagN3i3p0v6KfTHn1DjSTzcy6IRt%2B6ZNlWeSyiWE5oibAnaPIKmgGS5%2By4bIJ&X-Amz-Signature=22b8fed5033f8106d0f40082beeb44ebd8052401bf83b0e82625be357b152778&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVGUNNUK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIFEB5BmdjhMBCCRuzKIfRQeBzOAaHMkcrugcUsJryMAlAiEAgQaLmeuvWD32mVMGgSaO%2BBBj8vO5HX4d5S2CunXJfUAqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJJZc5Lo6suwhMMOyrcA3%2FLXLl%2FfSIvOc4SzJ5yMOlUW2Ar9rnLfW%2FdI4CC%2B2o5S%2FD5ICN%2BPjnuVhy1%2BPHhVF6ABL4doltxzw54aSAI93SdUhpDot9QDwu5cMPXbOoZhgKR6WmbDFjOR2xK754iiXUh53kWED1xSJlXU3Rz4hSaSZ8yOzaT9h%2F0wYUyJdaBxGN3UCibWHhmPZb9x%2Bn3yOoRkeZPm4Y9aw%2BsgnHHYPy9T9h25GPpw4S3fmjqkrfT1B2pkkH6HtR5Ewc4vqpHJIeeg8Nfc2F8PzxHBAHS1TvJrFVMH7D%2BZ%2Fnnzk%2BtAnceE1iTs2qGhshHIl%2FjRecrHFM%2F2%2BjjrIvhc3fEEmsvIl4C%2Balvdqrq7SVfMDP%2Fn%2BCKg13udAc7yzOZ4FjSTwigLu77mE8QKScqRuED%2FNWP%2FYMrtgoNZoNrBzw585oeX7cuq%2B4VC5vjzUMqR%2FCJTVIK5XZwqcPGnP6EgolRA8Mt583sSPrfnLJRo2FtbOuW4tewcqeeoedUkRLWkWq5Afx0frBXC5bDTm9gzZ0%2FoLP9CCfWHuRWZJnX%2BWdaDaOtGrpcae0IrHuCzsJjEZhGrQS7PZdUAy4MZd4qguWebxUTVkHpoZlQ7ZV8FkMam%2FhcO9srOcmD07CGHnwKaWzFMMO%2Bmr0GOqUBJugfgdKIwLCHKHkLhgUPx1ChMw0yCaNSzXlbpcEKT9wBGgO7CYfoWtnPhiZFHXa6vAF6GUoB%2BXZ3K3o9OgneV9RLyRGRbGsasBrg9Lv8gWjfx4RMFHSCMR96KqZgvbag7QQZ79blk0DEVqZi5EldT0DPGzdd1nMnagN3i3p0v6KfTHn1DjSTzcy6IRt%2B6ZNlWeSyiWE5oibAnaPIKmgGS5%2By4bIJ&X-Amz-Signature=4607c34a8158b795d9bf2e0c9af61e5618d65f460d1481fbca67d8b288c38812&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
