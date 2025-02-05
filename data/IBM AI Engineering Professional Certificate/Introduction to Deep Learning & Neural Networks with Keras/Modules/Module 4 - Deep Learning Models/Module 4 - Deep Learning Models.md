

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHU35N63%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIAyDHh5yNwD66LqEf3Y4ExlWDd7VujQf8sgIHLBpZvCeAiB6wSpdHpeW9stV%2BwNYa2IxRSeNBeX9hKo2j5o6SvgX5yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMBABeKO%2BzAhaWPVA8KtwD0RxjVzPl9o0dx3ZIqOhOEV4yLKbjLsvfFoNCfLBvymksZ2%2F2dfxR6yf%2FDhM6JGFES9V5cxK9DLqXyCSu413xgQig3yYVpDUrPrSdlSGcJWJZrXNqU0siLpOAIO7FhWc5lW7ooUO4FqQdf1jtx8SWv0oKjr%2FoVtHu8BTApFmayYeUdZuCIYnWKYMtZHvE3jnyfcu0UJ%2FWWvATHjRk18%2BbFWrw4jn1mwrgQuUUiAD3Sv0D1GT6wOrQhv92mUEAhJ7PBWKGUZnyKr1LZPkUZ4wY8ZJxm1rjeg5N0ADGDhJAVMQdC1FeMloaL4yV%2BR3KElif75tliDtAWBzTqZxVY0JuyOLVHqgSO9xjh3DmsFNyrAjK%2FQxWzaow1bL6qRpsUbd8EoeRlYOh%2BLyjODrAeDnu4SDt8lH4KQCrm%2ButRUSKnVXXisxcxVZemukZ%2BNl9VRup1UiqLaO5wLJmWxjSifabeQss7L3GsqUXN4jO1%2Fiws7jpzvA41c2BqiRKrNBlBQc%2BjcZADUgqo77TfNOl9CugM9d%2BTHj7e6fyjQPQpvmz2i71%2Bhq6Q95M1Jr3V7coqw0QU1jvGNk6qwGRpTEvqTL3RsNb0FVbVM%2FUwJQ0fCvuQiuIzzHv0xadmutLgTEwou%2BMvQY6pgECeg0gfltIzmvUBoFGNilfjc3pq8Z3NSxWJVuVUwRbyndyl873TcTrBMxNmRzWI3dz3kepCFGicwUwKH%2BAp1HT13yRPkbGiV732kx8V71QQ5YqU4OscxzLbfP5Q07wq0bDanCwWMq35%2FFDjx9QgurbQFkrFB5%2B1FHhMjDsEhhdQ%2FlAU1mEeSGRu0d2enQzwion3wGTmEWYobzl1axPM4GMa6qInRlA&X-Amz-Signature=bfc14473d99eb570c16b678022ae7afe1c588a38a7f9137bdc8847e4c6d499d0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHU35N63%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIAyDHh5yNwD66LqEf3Y4ExlWDd7VujQf8sgIHLBpZvCeAiB6wSpdHpeW9stV%2BwNYa2IxRSeNBeX9hKo2j5o6SvgX5yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMBABeKO%2BzAhaWPVA8KtwD0RxjVzPl9o0dx3ZIqOhOEV4yLKbjLsvfFoNCfLBvymksZ2%2F2dfxR6yf%2FDhM6JGFES9V5cxK9DLqXyCSu413xgQig3yYVpDUrPrSdlSGcJWJZrXNqU0siLpOAIO7FhWc5lW7ooUO4FqQdf1jtx8SWv0oKjr%2FoVtHu8BTApFmayYeUdZuCIYnWKYMtZHvE3jnyfcu0UJ%2FWWvATHjRk18%2BbFWrw4jn1mwrgQuUUiAD3Sv0D1GT6wOrQhv92mUEAhJ7PBWKGUZnyKr1LZPkUZ4wY8ZJxm1rjeg5N0ADGDhJAVMQdC1FeMloaL4yV%2BR3KElif75tliDtAWBzTqZxVY0JuyOLVHqgSO9xjh3DmsFNyrAjK%2FQxWzaow1bL6qRpsUbd8EoeRlYOh%2BLyjODrAeDnu4SDt8lH4KQCrm%2ButRUSKnVXXisxcxVZemukZ%2BNl9VRup1UiqLaO5wLJmWxjSifabeQss7L3GsqUXN4jO1%2Fiws7jpzvA41c2BqiRKrNBlBQc%2BjcZADUgqo77TfNOl9CugM9d%2BTHj7e6fyjQPQpvmz2i71%2Bhq6Q95M1Jr3V7coqw0QU1jvGNk6qwGRpTEvqTL3RsNb0FVbVM%2FUwJQ0fCvuQiuIzzHv0xadmutLgTEwou%2BMvQY6pgECeg0gfltIzmvUBoFGNilfjc3pq8Z3NSxWJVuVUwRbyndyl873TcTrBMxNmRzWI3dz3kepCFGicwUwKH%2BAp1HT13yRPkbGiV732kx8V71QQ5YqU4OscxzLbfP5Q07wq0bDanCwWMq35%2FFDjx9QgurbQFkrFB5%2B1FHhMjDsEhhdQ%2FlAU1mEeSGRu0d2enQzwion3wGTmEWYobzl1axPM4GMa6qInRlA&X-Amz-Signature=856085c409eab50bec037d225023204b00166aaab1eb8f8751c1616c6c7e046d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHU35N63%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIAyDHh5yNwD66LqEf3Y4ExlWDd7VujQf8sgIHLBpZvCeAiB6wSpdHpeW9stV%2BwNYa2IxRSeNBeX9hKo2j5o6SvgX5yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMBABeKO%2BzAhaWPVA8KtwD0RxjVzPl9o0dx3ZIqOhOEV4yLKbjLsvfFoNCfLBvymksZ2%2F2dfxR6yf%2FDhM6JGFES9V5cxK9DLqXyCSu413xgQig3yYVpDUrPrSdlSGcJWJZrXNqU0siLpOAIO7FhWc5lW7ooUO4FqQdf1jtx8SWv0oKjr%2FoVtHu8BTApFmayYeUdZuCIYnWKYMtZHvE3jnyfcu0UJ%2FWWvATHjRk18%2BbFWrw4jn1mwrgQuUUiAD3Sv0D1GT6wOrQhv92mUEAhJ7PBWKGUZnyKr1LZPkUZ4wY8ZJxm1rjeg5N0ADGDhJAVMQdC1FeMloaL4yV%2BR3KElif75tliDtAWBzTqZxVY0JuyOLVHqgSO9xjh3DmsFNyrAjK%2FQxWzaow1bL6qRpsUbd8EoeRlYOh%2BLyjODrAeDnu4SDt8lH4KQCrm%2ButRUSKnVXXisxcxVZemukZ%2BNl9VRup1UiqLaO5wLJmWxjSifabeQss7L3GsqUXN4jO1%2Fiws7jpzvA41c2BqiRKrNBlBQc%2BjcZADUgqo77TfNOl9CugM9d%2BTHj7e6fyjQPQpvmz2i71%2Bhq6Q95M1Jr3V7coqw0QU1jvGNk6qwGRpTEvqTL3RsNb0FVbVM%2FUwJQ0fCvuQiuIzzHv0xadmutLgTEwou%2BMvQY6pgECeg0gfltIzmvUBoFGNilfjc3pq8Z3NSxWJVuVUwRbyndyl873TcTrBMxNmRzWI3dz3kepCFGicwUwKH%2BAp1HT13yRPkbGiV732kx8V71QQ5YqU4OscxzLbfP5Q07wq0bDanCwWMq35%2FFDjx9QgurbQFkrFB5%2B1FHhMjDsEhhdQ%2FlAU1mEeSGRu0d2enQzwion3wGTmEWYobzl1axPM4GMa6qInRlA&X-Amz-Signature=22f26693d466c47e2ccbd825ccbb79b4624a76983673af333fd5a8f1b2cb1dd8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHU35N63%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIAyDHh5yNwD66LqEf3Y4ExlWDd7VujQf8sgIHLBpZvCeAiB6wSpdHpeW9stV%2BwNYa2IxRSeNBeX9hKo2j5o6SvgX5yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMBABeKO%2BzAhaWPVA8KtwD0RxjVzPl9o0dx3ZIqOhOEV4yLKbjLsvfFoNCfLBvymksZ2%2F2dfxR6yf%2FDhM6JGFES9V5cxK9DLqXyCSu413xgQig3yYVpDUrPrSdlSGcJWJZrXNqU0siLpOAIO7FhWc5lW7ooUO4FqQdf1jtx8SWv0oKjr%2FoVtHu8BTApFmayYeUdZuCIYnWKYMtZHvE3jnyfcu0UJ%2FWWvATHjRk18%2BbFWrw4jn1mwrgQuUUiAD3Sv0D1GT6wOrQhv92mUEAhJ7PBWKGUZnyKr1LZPkUZ4wY8ZJxm1rjeg5N0ADGDhJAVMQdC1FeMloaL4yV%2BR3KElif75tliDtAWBzTqZxVY0JuyOLVHqgSO9xjh3DmsFNyrAjK%2FQxWzaow1bL6qRpsUbd8EoeRlYOh%2BLyjODrAeDnu4SDt8lH4KQCrm%2ButRUSKnVXXisxcxVZemukZ%2BNl9VRup1UiqLaO5wLJmWxjSifabeQss7L3GsqUXN4jO1%2Fiws7jpzvA41c2BqiRKrNBlBQc%2BjcZADUgqo77TfNOl9CugM9d%2BTHj7e6fyjQPQpvmz2i71%2Bhq6Q95M1Jr3V7coqw0QU1jvGNk6qwGRpTEvqTL3RsNb0FVbVM%2FUwJQ0fCvuQiuIzzHv0xadmutLgTEwou%2BMvQY6pgECeg0gfltIzmvUBoFGNilfjc3pq8Z3NSxWJVuVUwRbyndyl873TcTrBMxNmRzWI3dz3kepCFGicwUwKH%2BAp1HT13yRPkbGiV732kx8V71QQ5YqU4OscxzLbfP5Q07wq0bDanCwWMq35%2FFDjx9QgurbQFkrFB5%2B1FHhMjDsEhhdQ%2FlAU1mEeSGRu0d2enQzwion3wGTmEWYobzl1axPM4GMa6qInRlA&X-Amz-Signature=cf6a3d3e19e85fa147471469a4a869e3e157036259c5dff0e0e90489ff39975b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHU35N63%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIAyDHh5yNwD66LqEf3Y4ExlWDd7VujQf8sgIHLBpZvCeAiB6wSpdHpeW9stV%2BwNYa2IxRSeNBeX9hKo2j5o6SvgX5yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMBABeKO%2BzAhaWPVA8KtwD0RxjVzPl9o0dx3ZIqOhOEV4yLKbjLsvfFoNCfLBvymksZ2%2F2dfxR6yf%2FDhM6JGFES9V5cxK9DLqXyCSu413xgQig3yYVpDUrPrSdlSGcJWJZrXNqU0siLpOAIO7FhWc5lW7ooUO4FqQdf1jtx8SWv0oKjr%2FoVtHu8BTApFmayYeUdZuCIYnWKYMtZHvE3jnyfcu0UJ%2FWWvATHjRk18%2BbFWrw4jn1mwrgQuUUiAD3Sv0D1GT6wOrQhv92mUEAhJ7PBWKGUZnyKr1LZPkUZ4wY8ZJxm1rjeg5N0ADGDhJAVMQdC1FeMloaL4yV%2BR3KElif75tliDtAWBzTqZxVY0JuyOLVHqgSO9xjh3DmsFNyrAjK%2FQxWzaow1bL6qRpsUbd8EoeRlYOh%2BLyjODrAeDnu4SDt8lH4KQCrm%2ButRUSKnVXXisxcxVZemukZ%2BNl9VRup1UiqLaO5wLJmWxjSifabeQss7L3GsqUXN4jO1%2Fiws7jpzvA41c2BqiRKrNBlBQc%2BjcZADUgqo77TfNOl9CugM9d%2BTHj7e6fyjQPQpvmz2i71%2Bhq6Q95M1Jr3V7coqw0QU1jvGNk6qwGRpTEvqTL3RsNb0FVbVM%2FUwJQ0fCvuQiuIzzHv0xadmutLgTEwou%2BMvQY6pgECeg0gfltIzmvUBoFGNilfjc3pq8Z3NSxWJVuVUwRbyndyl873TcTrBMxNmRzWI3dz3kepCFGicwUwKH%2BAp1HT13yRPkbGiV732kx8V71QQ5YqU4OscxzLbfP5Q07wq0bDanCwWMq35%2FFDjx9QgurbQFkrFB5%2B1FHhMjDsEhhdQ%2FlAU1mEeSGRu0d2enQzwion3wGTmEWYobzl1axPM4GMa6qInRlA&X-Amz-Signature=45499feb80682e018218caa479b0e835e4a5cd1fdfc5f7171b486fe85ba39fc7&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHU35N63%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIAyDHh5yNwD66LqEf3Y4ExlWDd7VujQf8sgIHLBpZvCeAiB6wSpdHpeW9stV%2BwNYa2IxRSeNBeX9hKo2j5o6SvgX5yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMBABeKO%2BzAhaWPVA8KtwD0RxjVzPl9o0dx3ZIqOhOEV4yLKbjLsvfFoNCfLBvymksZ2%2F2dfxR6yf%2FDhM6JGFES9V5cxK9DLqXyCSu413xgQig3yYVpDUrPrSdlSGcJWJZrXNqU0siLpOAIO7FhWc5lW7ooUO4FqQdf1jtx8SWv0oKjr%2FoVtHu8BTApFmayYeUdZuCIYnWKYMtZHvE3jnyfcu0UJ%2FWWvATHjRk18%2BbFWrw4jn1mwrgQuUUiAD3Sv0D1GT6wOrQhv92mUEAhJ7PBWKGUZnyKr1LZPkUZ4wY8ZJxm1rjeg5N0ADGDhJAVMQdC1FeMloaL4yV%2BR3KElif75tliDtAWBzTqZxVY0JuyOLVHqgSO9xjh3DmsFNyrAjK%2FQxWzaow1bL6qRpsUbd8EoeRlYOh%2BLyjODrAeDnu4SDt8lH4KQCrm%2ButRUSKnVXXisxcxVZemukZ%2BNl9VRup1UiqLaO5wLJmWxjSifabeQss7L3GsqUXN4jO1%2Fiws7jpzvA41c2BqiRKrNBlBQc%2BjcZADUgqo77TfNOl9CugM9d%2BTHj7e6fyjQPQpvmz2i71%2Bhq6Q95M1Jr3V7coqw0QU1jvGNk6qwGRpTEvqTL3RsNb0FVbVM%2FUwJQ0fCvuQiuIzzHv0xadmutLgTEwou%2BMvQY6pgECeg0gfltIzmvUBoFGNilfjc3pq8Z3NSxWJVuVUwRbyndyl873TcTrBMxNmRzWI3dz3kepCFGicwUwKH%2BAp1HT13yRPkbGiV732kx8V71QQ5YqU4OscxzLbfP5Q07wq0bDanCwWMq35%2FFDjx9QgurbQFkrFB5%2B1FHhMjDsEhhdQ%2FlAU1mEeSGRu0d2enQzwion3wGTmEWYobzl1axPM4GMa6qInRlA&X-Amz-Signature=8951dfe7fe48692c53d6fe1d68aa61773ad2bf4ffd74d0eb9b1c0e7bff17b01b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHU35N63%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIAyDHh5yNwD66LqEf3Y4ExlWDd7VujQf8sgIHLBpZvCeAiB6wSpdHpeW9stV%2BwNYa2IxRSeNBeX9hKo2j5o6SvgX5yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMBABeKO%2BzAhaWPVA8KtwD0RxjVzPl9o0dx3ZIqOhOEV4yLKbjLsvfFoNCfLBvymksZ2%2F2dfxR6yf%2FDhM6JGFES9V5cxK9DLqXyCSu413xgQig3yYVpDUrPrSdlSGcJWJZrXNqU0siLpOAIO7FhWc5lW7ooUO4FqQdf1jtx8SWv0oKjr%2FoVtHu8BTApFmayYeUdZuCIYnWKYMtZHvE3jnyfcu0UJ%2FWWvATHjRk18%2BbFWrw4jn1mwrgQuUUiAD3Sv0D1GT6wOrQhv92mUEAhJ7PBWKGUZnyKr1LZPkUZ4wY8ZJxm1rjeg5N0ADGDhJAVMQdC1FeMloaL4yV%2BR3KElif75tliDtAWBzTqZxVY0JuyOLVHqgSO9xjh3DmsFNyrAjK%2FQxWzaow1bL6qRpsUbd8EoeRlYOh%2BLyjODrAeDnu4SDt8lH4KQCrm%2ButRUSKnVXXisxcxVZemukZ%2BNl9VRup1UiqLaO5wLJmWxjSifabeQss7L3GsqUXN4jO1%2Fiws7jpzvA41c2BqiRKrNBlBQc%2BjcZADUgqo77TfNOl9CugM9d%2BTHj7e6fyjQPQpvmz2i71%2Bhq6Q95M1Jr3V7coqw0QU1jvGNk6qwGRpTEvqTL3RsNb0FVbVM%2FUwJQ0fCvuQiuIzzHv0xadmutLgTEwou%2BMvQY6pgECeg0gfltIzmvUBoFGNilfjc3pq8Z3NSxWJVuVUwRbyndyl873TcTrBMxNmRzWI3dz3kepCFGicwUwKH%2BAp1HT13yRPkbGiV732kx8V71QQ5YqU4OscxzLbfP5Q07wq0bDanCwWMq35%2FFDjx9QgurbQFkrFB5%2B1FHhMjDsEhhdQ%2FlAU1mEeSGRu0d2enQzwion3wGTmEWYobzl1axPM4GMa6qInRlA&X-Amz-Signature=0680db10574970031ced5b8d4987481bfd604375f6794079087d43d4efb76143&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHU35N63%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIAyDHh5yNwD66LqEf3Y4ExlWDd7VujQf8sgIHLBpZvCeAiB6wSpdHpeW9stV%2BwNYa2IxRSeNBeX9hKo2j5o6SvgX5yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMBABeKO%2BzAhaWPVA8KtwD0RxjVzPl9o0dx3ZIqOhOEV4yLKbjLsvfFoNCfLBvymksZ2%2F2dfxR6yf%2FDhM6JGFES9V5cxK9DLqXyCSu413xgQig3yYVpDUrPrSdlSGcJWJZrXNqU0siLpOAIO7FhWc5lW7ooUO4FqQdf1jtx8SWv0oKjr%2FoVtHu8BTApFmayYeUdZuCIYnWKYMtZHvE3jnyfcu0UJ%2FWWvATHjRk18%2BbFWrw4jn1mwrgQuUUiAD3Sv0D1GT6wOrQhv92mUEAhJ7PBWKGUZnyKr1LZPkUZ4wY8ZJxm1rjeg5N0ADGDhJAVMQdC1FeMloaL4yV%2BR3KElif75tliDtAWBzTqZxVY0JuyOLVHqgSO9xjh3DmsFNyrAjK%2FQxWzaow1bL6qRpsUbd8EoeRlYOh%2BLyjODrAeDnu4SDt8lH4KQCrm%2ButRUSKnVXXisxcxVZemukZ%2BNl9VRup1UiqLaO5wLJmWxjSifabeQss7L3GsqUXN4jO1%2Fiws7jpzvA41c2BqiRKrNBlBQc%2BjcZADUgqo77TfNOl9CugM9d%2BTHj7e6fyjQPQpvmz2i71%2Bhq6Q95M1Jr3V7coqw0QU1jvGNk6qwGRpTEvqTL3RsNb0FVbVM%2FUwJQ0fCvuQiuIzzHv0xadmutLgTEwou%2BMvQY6pgECeg0gfltIzmvUBoFGNilfjc3pq8Z3NSxWJVuVUwRbyndyl873TcTrBMxNmRzWI3dz3kepCFGicwUwKH%2BAp1HT13yRPkbGiV732kx8V71QQ5YqU4OscxzLbfP5Q07wq0bDanCwWMq35%2FFDjx9QgurbQFkrFB5%2B1FHhMjDsEhhdQ%2FlAU1mEeSGRu0d2enQzwion3wGTmEWYobzl1axPM4GMa6qInRlA&X-Amz-Signature=9bd4ee9ead234d1232d98e44f27894be353f7036629476df19adaa71280c3a9a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHU35N63%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIAyDHh5yNwD66LqEf3Y4ExlWDd7VujQf8sgIHLBpZvCeAiB6wSpdHpeW9stV%2BwNYa2IxRSeNBeX9hKo2j5o6SvgX5yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMBABeKO%2BzAhaWPVA8KtwD0RxjVzPl9o0dx3ZIqOhOEV4yLKbjLsvfFoNCfLBvymksZ2%2F2dfxR6yf%2FDhM6JGFES9V5cxK9DLqXyCSu413xgQig3yYVpDUrPrSdlSGcJWJZrXNqU0siLpOAIO7FhWc5lW7ooUO4FqQdf1jtx8SWv0oKjr%2FoVtHu8BTApFmayYeUdZuCIYnWKYMtZHvE3jnyfcu0UJ%2FWWvATHjRk18%2BbFWrw4jn1mwrgQuUUiAD3Sv0D1GT6wOrQhv92mUEAhJ7PBWKGUZnyKr1LZPkUZ4wY8ZJxm1rjeg5N0ADGDhJAVMQdC1FeMloaL4yV%2BR3KElif75tliDtAWBzTqZxVY0JuyOLVHqgSO9xjh3DmsFNyrAjK%2FQxWzaow1bL6qRpsUbd8EoeRlYOh%2BLyjODrAeDnu4SDt8lH4KQCrm%2ButRUSKnVXXisxcxVZemukZ%2BNl9VRup1UiqLaO5wLJmWxjSifabeQss7L3GsqUXN4jO1%2Fiws7jpzvA41c2BqiRKrNBlBQc%2BjcZADUgqo77TfNOl9CugM9d%2BTHj7e6fyjQPQpvmz2i71%2Bhq6Q95M1Jr3V7coqw0QU1jvGNk6qwGRpTEvqTL3RsNb0FVbVM%2FUwJQ0fCvuQiuIzzHv0xadmutLgTEwou%2BMvQY6pgECeg0gfltIzmvUBoFGNilfjc3pq8Z3NSxWJVuVUwRbyndyl873TcTrBMxNmRzWI3dz3kepCFGicwUwKH%2BAp1HT13yRPkbGiV732kx8V71QQ5YqU4OscxzLbfP5Q07wq0bDanCwWMq35%2FFDjx9QgurbQFkrFB5%2B1FHhMjDsEhhdQ%2FlAU1mEeSGRu0d2enQzwion3wGTmEWYobzl1axPM4GMa6qInRlA&X-Amz-Signature=4f3a998ef97039c4dadf189bf7bc730bcaba7718d0850d640f2df5a0cce715c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RCSGDBV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQC1CNbXOOj5bJodzaOfFDKobOs1OEuSvfp3G6rojUSPIwIhAJizV1zYCBOY6ZcSCJSmfqNxHkwALY4zBV4dP13Z3eKjKv8DCEMQABoMNjM3NDIzMTgzODA1Igx%2BS7EcetQs9eaIDMAq3ANQhOSbreG38A4FpJtV0768vk5mRR4M4%2FVdcUSIu5zhYyek%2BrR7DIIXGH9yLur77neN%2Fo%2BHZfnmjmfkq9KgXJ6RHSoiSRMEzVZh7ZGr9QexcHrqji8YC4%2BD0G%2FgdnMBVDkQQKnWO7f6MmRqlyYI96r4B%2BBVOR5qKLVc2CgdGCZxc26vcd6JmB16eOloDfFTiiMkv4iM1kd%2F8iUfOGbDAQrbOM7ZIA6PTTqM%2FMmBohxPpoQFLWvsnd15xfDApOEIkt1%2B8EJTcOwrSLqHA%2Ff9hs9xfqU7RzCRbQLg9T%2Ft1jq3qz5iN56MKE1YxOX6rRsb%2FrC6SQErI5Tmo1Y7Ulx0RJ9BpYMarxOM8UqmhyWTMmmwxcr1ah%2BK%2FHDIhnJx726Dh9s3N6Lf8Vl5gTTyQz38ZDjWFEt9a8AtHsnmFaJXynCA6meJFDnnf8ghK45IqFMMg%2BeXl%2FtTjeotHyIhuW34mKnWKxET%2Ba7pphCogv4ZbH%2BbFcw6kOxslB%2FKP8f%2FfgEAEg7%2FvQEPRGZbVdCiHUcoqCz2LVyufGRzfOhAS5E%2F7xePzp4hm6woSpzNnsTB7ezIztt9ZHGnA%2FSExumxjhLBEHqQ3ol2e8JUJOKe%2BMDS%2BYNZQLJxZRBTX1ZiRrDKfTCX74y9BjqkAWu4bNaaOZiKAJTDkF1E%2FRfrZFWnNsnhVtpIBs%2FmPUs8BWKysnJHAqic499Sg55IVYdEssn%2Fovb2gmNA%2FId37Sv9cXLJB%2BITJ7TYDHC69WO%2FsHZDjVR3%2F1npk%2B9zd1reuFT8HWovDP55ez25FyyNH7WIeD2G%2BRmR0AmYA8f1egFEx7zntn9PxEc4Gu7O7G1IYjGo15%2FT6pTkViFTyMGJuoXx1TFA&X-Amz-Signature=86ef41e0d4c8f99f179e7632dc71e7a713e59878ccacc44862c41b01718af072&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RCSGDBV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQC1CNbXOOj5bJodzaOfFDKobOs1OEuSvfp3G6rojUSPIwIhAJizV1zYCBOY6ZcSCJSmfqNxHkwALY4zBV4dP13Z3eKjKv8DCEMQABoMNjM3NDIzMTgzODA1Igx%2BS7EcetQs9eaIDMAq3ANQhOSbreG38A4FpJtV0768vk5mRR4M4%2FVdcUSIu5zhYyek%2BrR7DIIXGH9yLur77neN%2Fo%2BHZfnmjmfkq9KgXJ6RHSoiSRMEzVZh7ZGr9QexcHrqji8YC4%2BD0G%2FgdnMBVDkQQKnWO7f6MmRqlyYI96r4B%2BBVOR5qKLVc2CgdGCZxc26vcd6JmB16eOloDfFTiiMkv4iM1kd%2F8iUfOGbDAQrbOM7ZIA6PTTqM%2FMmBohxPpoQFLWvsnd15xfDApOEIkt1%2B8EJTcOwrSLqHA%2Ff9hs9xfqU7RzCRbQLg9T%2Ft1jq3qz5iN56MKE1YxOX6rRsb%2FrC6SQErI5Tmo1Y7Ulx0RJ9BpYMarxOM8UqmhyWTMmmwxcr1ah%2BK%2FHDIhnJx726Dh9s3N6Lf8Vl5gTTyQz38ZDjWFEt9a8AtHsnmFaJXynCA6meJFDnnf8ghK45IqFMMg%2BeXl%2FtTjeotHyIhuW34mKnWKxET%2Ba7pphCogv4ZbH%2BbFcw6kOxslB%2FKP8f%2FfgEAEg7%2FvQEPRGZbVdCiHUcoqCz2LVyufGRzfOhAS5E%2F7xePzp4hm6woSpzNnsTB7ezIztt9ZHGnA%2FSExumxjhLBEHqQ3ol2e8JUJOKe%2BMDS%2BYNZQLJxZRBTX1ZiRrDKfTCX74y9BjqkAWu4bNaaOZiKAJTDkF1E%2FRfrZFWnNsnhVtpIBs%2FmPUs8BWKysnJHAqic499Sg55IVYdEssn%2Fovb2gmNA%2FId37Sv9cXLJB%2BITJ7TYDHC69WO%2FsHZDjVR3%2F1npk%2B9zd1reuFT8HWovDP55ez25FyyNH7WIeD2G%2BRmR0AmYA8f1egFEx7zntn9PxEc4Gu7O7G1IYjGo15%2FT6pTkViFTyMGJuoXx1TFA&X-Amz-Signature=0c13cbea9e5c72de9f2902212fa4d0f90c9448c47296aed81ff006540d448c8d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
