

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6RDLHDI%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDHn1NumIviSWBHRn8%2F%2FTHmYJKSS3e%2BauvmPBWwimD8vQIgNV1UwvR98ZxVbwgg16ymVciDA%2FzEgSHGz%2FWJEB4KrvEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPis0p529%2BJxO6N%2BzyrcA2VNmDfen1N5FGQl%2BEfGdXvYURxlmQmazS0Yg0MwugvJ4tSM2zfTOu47h4SeONch8XQFUpFH5yIb276YbUVbq0ejxAKiD678elIFC8CnDdZkzR7T5yASagandn6CeiWF88ndeZ8HRt3UCOx2PUJS4Pc9KsAU%2Bk4bZQW2IMj004QN0dEYl54dsZuYiVx0DstZ1n56d3TqCFUbwABsJZN1EmMpUtvkcbiUVDPdiKPpVwyeuCK%2FW%2FtXj%2Fc9R3YsYnMBbLsswwna4AxTX0GuMW4%2Fagvb7reXlUNwMsxjB%2FaUZVqXurzL%2FuL2j%2FH1Bgi2GTFDjSc6p9A6yDM5BfctQol233lq63rzllTwrTEp4ja9hnT2KGgFcaTIHWWmrLtJi5eB%2FDnjv8AHsPgnz7zs%2FfZisNfa%2BXUVCgx%2B0PabHPeY%2FHHbH9hTBtB8TKJxxFlOoZcHcRsVZkLtVhr1gwZB4NUNwQs0rgEAwVFFNRsRaDy1Z3xtmfRcSnTse%2FoZH5pSl0eDtnXE3nVQvMcRQjOpr60JwwrfmPwEpuWKU0xxJCzVmTk22KQcyCfSAR%2F22XHLQ72SYLsDqFyPZtfRGePWVObmB9%2FDAfuKzKpYNHfQiMuEDbZ%2FyE6JAyppPXaahy9oMLKps74GOqUBTJ%2FGIa2CRilZNOdEHmYE5r%2FjZEkjxdvN7O8OUIEJxKJC3YFbJI0pS8Yj9JzaJNRbMw61tJv6f4mw6MGfFM%2FiOlQK%2Fk23dC73JNwwopSXhLwfVgXz1oChqUXPOvZIgiMO8vmiRy9DTKhJrVG77787SJJJwABbEqqYravfXs0ouVUpd%2Fud%2FtCyZ6gp0xXVkChEph45yHa2VwpE6cyw9IIkjjCMEzzA&X-Amz-Signature=a3f7be8c0de6da4d2c2d242057fb8e0da3a7f76b5fc713a871ca9cc3584c8b1c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6RDLHDI%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDHn1NumIviSWBHRn8%2F%2FTHmYJKSS3e%2BauvmPBWwimD8vQIgNV1UwvR98ZxVbwgg16ymVciDA%2FzEgSHGz%2FWJEB4KrvEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPis0p529%2BJxO6N%2BzyrcA2VNmDfen1N5FGQl%2BEfGdXvYURxlmQmazS0Yg0MwugvJ4tSM2zfTOu47h4SeONch8XQFUpFH5yIb276YbUVbq0ejxAKiD678elIFC8CnDdZkzR7T5yASagandn6CeiWF88ndeZ8HRt3UCOx2PUJS4Pc9KsAU%2Bk4bZQW2IMj004QN0dEYl54dsZuYiVx0DstZ1n56d3TqCFUbwABsJZN1EmMpUtvkcbiUVDPdiKPpVwyeuCK%2FW%2FtXj%2Fc9R3YsYnMBbLsswwna4AxTX0GuMW4%2Fagvb7reXlUNwMsxjB%2FaUZVqXurzL%2FuL2j%2FH1Bgi2GTFDjSc6p9A6yDM5BfctQol233lq63rzllTwrTEp4ja9hnT2KGgFcaTIHWWmrLtJi5eB%2FDnjv8AHsPgnz7zs%2FfZisNfa%2BXUVCgx%2B0PabHPeY%2FHHbH9hTBtB8TKJxxFlOoZcHcRsVZkLtVhr1gwZB4NUNwQs0rgEAwVFFNRsRaDy1Z3xtmfRcSnTse%2FoZH5pSl0eDtnXE3nVQvMcRQjOpr60JwwrfmPwEpuWKU0xxJCzVmTk22KQcyCfSAR%2F22XHLQ72SYLsDqFyPZtfRGePWVObmB9%2FDAfuKzKpYNHfQiMuEDbZ%2FyE6JAyppPXaahy9oMLKps74GOqUBTJ%2FGIa2CRilZNOdEHmYE5r%2FjZEkjxdvN7O8OUIEJxKJC3YFbJI0pS8Yj9JzaJNRbMw61tJv6f4mw6MGfFM%2FiOlQK%2Fk23dC73JNwwopSXhLwfVgXz1oChqUXPOvZIgiMO8vmiRy9DTKhJrVG77787SJJJwABbEqqYravfXs0ouVUpd%2Fud%2FtCyZ6gp0xXVkChEph45yHa2VwpE6cyw9IIkjjCMEzzA&X-Amz-Signature=88a2e5f9d26c567cf12962de18dc21575867a82fed3461c24965e5da8634c818&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6RDLHDI%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDHn1NumIviSWBHRn8%2F%2FTHmYJKSS3e%2BauvmPBWwimD8vQIgNV1UwvR98ZxVbwgg16ymVciDA%2FzEgSHGz%2FWJEB4KrvEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPis0p529%2BJxO6N%2BzyrcA2VNmDfen1N5FGQl%2BEfGdXvYURxlmQmazS0Yg0MwugvJ4tSM2zfTOu47h4SeONch8XQFUpFH5yIb276YbUVbq0ejxAKiD678elIFC8CnDdZkzR7T5yASagandn6CeiWF88ndeZ8HRt3UCOx2PUJS4Pc9KsAU%2Bk4bZQW2IMj004QN0dEYl54dsZuYiVx0DstZ1n56d3TqCFUbwABsJZN1EmMpUtvkcbiUVDPdiKPpVwyeuCK%2FW%2FtXj%2Fc9R3YsYnMBbLsswwna4AxTX0GuMW4%2Fagvb7reXlUNwMsxjB%2FaUZVqXurzL%2FuL2j%2FH1Bgi2GTFDjSc6p9A6yDM5BfctQol233lq63rzllTwrTEp4ja9hnT2KGgFcaTIHWWmrLtJi5eB%2FDnjv8AHsPgnz7zs%2FfZisNfa%2BXUVCgx%2B0PabHPeY%2FHHbH9hTBtB8TKJxxFlOoZcHcRsVZkLtVhr1gwZB4NUNwQs0rgEAwVFFNRsRaDy1Z3xtmfRcSnTse%2FoZH5pSl0eDtnXE3nVQvMcRQjOpr60JwwrfmPwEpuWKU0xxJCzVmTk22KQcyCfSAR%2F22XHLQ72SYLsDqFyPZtfRGePWVObmB9%2FDAfuKzKpYNHfQiMuEDbZ%2FyE6JAyppPXaahy9oMLKps74GOqUBTJ%2FGIa2CRilZNOdEHmYE5r%2FjZEkjxdvN7O8OUIEJxKJC3YFbJI0pS8Yj9JzaJNRbMw61tJv6f4mw6MGfFM%2FiOlQK%2Fk23dC73JNwwopSXhLwfVgXz1oChqUXPOvZIgiMO8vmiRy9DTKhJrVG77787SJJJwABbEqqYravfXs0ouVUpd%2Fud%2FtCyZ6gp0xXVkChEph45yHa2VwpE6cyw9IIkjjCMEzzA&X-Amz-Signature=910ce9d8c605bcf046210662f2a0223681375194dbfb0726c0bb244ebe173127&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6RDLHDI%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDHn1NumIviSWBHRn8%2F%2FTHmYJKSS3e%2BauvmPBWwimD8vQIgNV1UwvR98ZxVbwgg16ymVciDA%2FzEgSHGz%2FWJEB4KrvEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPis0p529%2BJxO6N%2BzyrcA2VNmDfen1N5FGQl%2BEfGdXvYURxlmQmazS0Yg0MwugvJ4tSM2zfTOu47h4SeONch8XQFUpFH5yIb276YbUVbq0ejxAKiD678elIFC8CnDdZkzR7T5yASagandn6CeiWF88ndeZ8HRt3UCOx2PUJS4Pc9KsAU%2Bk4bZQW2IMj004QN0dEYl54dsZuYiVx0DstZ1n56d3TqCFUbwABsJZN1EmMpUtvkcbiUVDPdiKPpVwyeuCK%2FW%2FtXj%2Fc9R3YsYnMBbLsswwna4AxTX0GuMW4%2Fagvb7reXlUNwMsxjB%2FaUZVqXurzL%2FuL2j%2FH1Bgi2GTFDjSc6p9A6yDM5BfctQol233lq63rzllTwrTEp4ja9hnT2KGgFcaTIHWWmrLtJi5eB%2FDnjv8AHsPgnz7zs%2FfZisNfa%2BXUVCgx%2B0PabHPeY%2FHHbH9hTBtB8TKJxxFlOoZcHcRsVZkLtVhr1gwZB4NUNwQs0rgEAwVFFNRsRaDy1Z3xtmfRcSnTse%2FoZH5pSl0eDtnXE3nVQvMcRQjOpr60JwwrfmPwEpuWKU0xxJCzVmTk22KQcyCfSAR%2F22XHLQ72SYLsDqFyPZtfRGePWVObmB9%2FDAfuKzKpYNHfQiMuEDbZ%2FyE6JAyppPXaahy9oMLKps74GOqUBTJ%2FGIa2CRilZNOdEHmYE5r%2FjZEkjxdvN7O8OUIEJxKJC3YFbJI0pS8Yj9JzaJNRbMw61tJv6f4mw6MGfFM%2FiOlQK%2Fk23dC73JNwwopSXhLwfVgXz1oChqUXPOvZIgiMO8vmiRy9DTKhJrVG77787SJJJwABbEqqYravfXs0ouVUpd%2Fud%2FtCyZ6gp0xXVkChEph45yHa2VwpE6cyw9IIkjjCMEzzA&X-Amz-Signature=61489b0c339d47fc163fdcc64481aec226c82e3cddfdf45cc2a19daad92358ce&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6RDLHDI%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDHn1NumIviSWBHRn8%2F%2FTHmYJKSS3e%2BauvmPBWwimD8vQIgNV1UwvR98ZxVbwgg16ymVciDA%2FzEgSHGz%2FWJEB4KrvEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPis0p529%2BJxO6N%2BzyrcA2VNmDfen1N5FGQl%2BEfGdXvYURxlmQmazS0Yg0MwugvJ4tSM2zfTOu47h4SeONch8XQFUpFH5yIb276YbUVbq0ejxAKiD678elIFC8CnDdZkzR7T5yASagandn6CeiWF88ndeZ8HRt3UCOx2PUJS4Pc9KsAU%2Bk4bZQW2IMj004QN0dEYl54dsZuYiVx0DstZ1n56d3TqCFUbwABsJZN1EmMpUtvkcbiUVDPdiKPpVwyeuCK%2FW%2FtXj%2Fc9R3YsYnMBbLsswwna4AxTX0GuMW4%2Fagvb7reXlUNwMsxjB%2FaUZVqXurzL%2FuL2j%2FH1Bgi2GTFDjSc6p9A6yDM5BfctQol233lq63rzllTwrTEp4ja9hnT2KGgFcaTIHWWmrLtJi5eB%2FDnjv8AHsPgnz7zs%2FfZisNfa%2BXUVCgx%2B0PabHPeY%2FHHbH9hTBtB8TKJxxFlOoZcHcRsVZkLtVhr1gwZB4NUNwQs0rgEAwVFFNRsRaDy1Z3xtmfRcSnTse%2FoZH5pSl0eDtnXE3nVQvMcRQjOpr60JwwrfmPwEpuWKU0xxJCzVmTk22KQcyCfSAR%2F22XHLQ72SYLsDqFyPZtfRGePWVObmB9%2FDAfuKzKpYNHfQiMuEDbZ%2FyE6JAyppPXaahy9oMLKps74GOqUBTJ%2FGIa2CRilZNOdEHmYE5r%2FjZEkjxdvN7O8OUIEJxKJC3YFbJI0pS8Yj9JzaJNRbMw61tJv6f4mw6MGfFM%2FiOlQK%2Fk23dC73JNwwopSXhLwfVgXz1oChqUXPOvZIgiMO8vmiRy9DTKhJrVG77787SJJJwABbEqqYravfXs0ouVUpd%2Fud%2FtCyZ6gp0xXVkChEph45yHa2VwpE6cyw9IIkjjCMEzzA&X-Amz-Signature=d228f4894f60cf9d8392d8739084c538d08ae64f20ff500c88853552e77ca9e6&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6RDLHDI%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDHn1NumIviSWBHRn8%2F%2FTHmYJKSS3e%2BauvmPBWwimD8vQIgNV1UwvR98ZxVbwgg16ymVciDA%2FzEgSHGz%2FWJEB4KrvEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPis0p529%2BJxO6N%2BzyrcA2VNmDfen1N5FGQl%2BEfGdXvYURxlmQmazS0Yg0MwugvJ4tSM2zfTOu47h4SeONch8XQFUpFH5yIb276YbUVbq0ejxAKiD678elIFC8CnDdZkzR7T5yASagandn6CeiWF88ndeZ8HRt3UCOx2PUJS4Pc9KsAU%2Bk4bZQW2IMj004QN0dEYl54dsZuYiVx0DstZ1n56d3TqCFUbwABsJZN1EmMpUtvkcbiUVDPdiKPpVwyeuCK%2FW%2FtXj%2Fc9R3YsYnMBbLsswwna4AxTX0GuMW4%2Fagvb7reXlUNwMsxjB%2FaUZVqXurzL%2FuL2j%2FH1Bgi2GTFDjSc6p9A6yDM5BfctQol233lq63rzllTwrTEp4ja9hnT2KGgFcaTIHWWmrLtJi5eB%2FDnjv8AHsPgnz7zs%2FfZisNfa%2BXUVCgx%2B0PabHPeY%2FHHbH9hTBtB8TKJxxFlOoZcHcRsVZkLtVhr1gwZB4NUNwQs0rgEAwVFFNRsRaDy1Z3xtmfRcSnTse%2FoZH5pSl0eDtnXE3nVQvMcRQjOpr60JwwrfmPwEpuWKU0xxJCzVmTk22KQcyCfSAR%2F22XHLQ72SYLsDqFyPZtfRGePWVObmB9%2FDAfuKzKpYNHfQiMuEDbZ%2FyE6JAyppPXaahy9oMLKps74GOqUBTJ%2FGIa2CRilZNOdEHmYE5r%2FjZEkjxdvN7O8OUIEJxKJC3YFbJI0pS8Yj9JzaJNRbMw61tJv6f4mw6MGfFM%2FiOlQK%2Fk23dC73JNwwopSXhLwfVgXz1oChqUXPOvZIgiMO8vmiRy9DTKhJrVG77787SJJJwABbEqqYravfXs0ouVUpd%2Fud%2FtCyZ6gp0xXVkChEph45yHa2VwpE6cyw9IIkjjCMEzzA&X-Amz-Signature=5e23c6bb1543a03b391eeb52374ce44781ac3eaaa3cd511635a172736478f7de&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6RDLHDI%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDHn1NumIviSWBHRn8%2F%2FTHmYJKSS3e%2BauvmPBWwimD8vQIgNV1UwvR98ZxVbwgg16ymVciDA%2FzEgSHGz%2FWJEB4KrvEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPis0p529%2BJxO6N%2BzyrcA2VNmDfen1N5FGQl%2BEfGdXvYURxlmQmazS0Yg0MwugvJ4tSM2zfTOu47h4SeONch8XQFUpFH5yIb276YbUVbq0ejxAKiD678elIFC8CnDdZkzR7T5yASagandn6CeiWF88ndeZ8HRt3UCOx2PUJS4Pc9KsAU%2Bk4bZQW2IMj004QN0dEYl54dsZuYiVx0DstZ1n56d3TqCFUbwABsJZN1EmMpUtvkcbiUVDPdiKPpVwyeuCK%2FW%2FtXj%2Fc9R3YsYnMBbLsswwna4AxTX0GuMW4%2Fagvb7reXlUNwMsxjB%2FaUZVqXurzL%2FuL2j%2FH1Bgi2GTFDjSc6p9A6yDM5BfctQol233lq63rzllTwrTEp4ja9hnT2KGgFcaTIHWWmrLtJi5eB%2FDnjv8AHsPgnz7zs%2FfZisNfa%2BXUVCgx%2B0PabHPeY%2FHHbH9hTBtB8TKJxxFlOoZcHcRsVZkLtVhr1gwZB4NUNwQs0rgEAwVFFNRsRaDy1Z3xtmfRcSnTse%2FoZH5pSl0eDtnXE3nVQvMcRQjOpr60JwwrfmPwEpuWKU0xxJCzVmTk22KQcyCfSAR%2F22XHLQ72SYLsDqFyPZtfRGePWVObmB9%2FDAfuKzKpYNHfQiMuEDbZ%2FyE6JAyppPXaahy9oMLKps74GOqUBTJ%2FGIa2CRilZNOdEHmYE5r%2FjZEkjxdvN7O8OUIEJxKJC3YFbJI0pS8Yj9JzaJNRbMw61tJv6f4mw6MGfFM%2FiOlQK%2Fk23dC73JNwwopSXhLwfVgXz1oChqUXPOvZIgiMO8vmiRy9DTKhJrVG77787SJJJwABbEqqYravfXs0ouVUpd%2Fud%2FtCyZ6gp0xXVkChEph45yHa2VwpE6cyw9IIkjjCMEzzA&X-Amz-Signature=c9d754f88e414c41a272e35868172b56d174d9f27b43babc412c682796bc3da3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6RDLHDI%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDHn1NumIviSWBHRn8%2F%2FTHmYJKSS3e%2BauvmPBWwimD8vQIgNV1UwvR98ZxVbwgg16ymVciDA%2FzEgSHGz%2FWJEB4KrvEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPis0p529%2BJxO6N%2BzyrcA2VNmDfen1N5FGQl%2BEfGdXvYURxlmQmazS0Yg0MwugvJ4tSM2zfTOu47h4SeONch8XQFUpFH5yIb276YbUVbq0ejxAKiD678elIFC8CnDdZkzR7T5yASagandn6CeiWF88ndeZ8HRt3UCOx2PUJS4Pc9KsAU%2Bk4bZQW2IMj004QN0dEYl54dsZuYiVx0DstZ1n56d3TqCFUbwABsJZN1EmMpUtvkcbiUVDPdiKPpVwyeuCK%2FW%2FtXj%2Fc9R3YsYnMBbLsswwna4AxTX0GuMW4%2Fagvb7reXlUNwMsxjB%2FaUZVqXurzL%2FuL2j%2FH1Bgi2GTFDjSc6p9A6yDM5BfctQol233lq63rzllTwrTEp4ja9hnT2KGgFcaTIHWWmrLtJi5eB%2FDnjv8AHsPgnz7zs%2FfZisNfa%2BXUVCgx%2B0PabHPeY%2FHHbH9hTBtB8TKJxxFlOoZcHcRsVZkLtVhr1gwZB4NUNwQs0rgEAwVFFNRsRaDy1Z3xtmfRcSnTse%2FoZH5pSl0eDtnXE3nVQvMcRQjOpr60JwwrfmPwEpuWKU0xxJCzVmTk22KQcyCfSAR%2F22XHLQ72SYLsDqFyPZtfRGePWVObmB9%2FDAfuKzKpYNHfQiMuEDbZ%2FyE6JAyppPXaahy9oMLKps74GOqUBTJ%2FGIa2CRilZNOdEHmYE5r%2FjZEkjxdvN7O8OUIEJxKJC3YFbJI0pS8Yj9JzaJNRbMw61tJv6f4mw6MGfFM%2FiOlQK%2Fk23dC73JNwwopSXhLwfVgXz1oChqUXPOvZIgiMO8vmiRy9DTKhJrVG77787SJJJwABbEqqYravfXs0ouVUpd%2Fud%2FtCyZ6gp0xXVkChEph45yHa2VwpE6cyw9IIkjjCMEzzA&X-Amz-Signature=75d7ea276801ba45523d4830d7853bf9043099d3ecf199cf4273371bada63d6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6RDLHDI%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDHn1NumIviSWBHRn8%2F%2FTHmYJKSS3e%2BauvmPBWwimD8vQIgNV1UwvR98ZxVbwgg16ymVciDA%2FzEgSHGz%2FWJEB4KrvEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPis0p529%2BJxO6N%2BzyrcA2VNmDfen1N5FGQl%2BEfGdXvYURxlmQmazS0Yg0MwugvJ4tSM2zfTOu47h4SeONch8XQFUpFH5yIb276YbUVbq0ejxAKiD678elIFC8CnDdZkzR7T5yASagandn6CeiWF88ndeZ8HRt3UCOx2PUJS4Pc9KsAU%2Bk4bZQW2IMj004QN0dEYl54dsZuYiVx0DstZ1n56d3TqCFUbwABsJZN1EmMpUtvkcbiUVDPdiKPpVwyeuCK%2FW%2FtXj%2Fc9R3YsYnMBbLsswwna4AxTX0GuMW4%2Fagvb7reXlUNwMsxjB%2FaUZVqXurzL%2FuL2j%2FH1Bgi2GTFDjSc6p9A6yDM5BfctQol233lq63rzllTwrTEp4ja9hnT2KGgFcaTIHWWmrLtJi5eB%2FDnjv8AHsPgnz7zs%2FfZisNfa%2BXUVCgx%2B0PabHPeY%2FHHbH9hTBtB8TKJxxFlOoZcHcRsVZkLtVhr1gwZB4NUNwQs0rgEAwVFFNRsRaDy1Z3xtmfRcSnTse%2FoZH5pSl0eDtnXE3nVQvMcRQjOpr60JwwrfmPwEpuWKU0xxJCzVmTk22KQcyCfSAR%2F22XHLQ72SYLsDqFyPZtfRGePWVObmB9%2FDAfuKzKpYNHfQiMuEDbZ%2FyE6JAyppPXaahy9oMLKps74GOqUBTJ%2FGIa2CRilZNOdEHmYE5r%2FjZEkjxdvN7O8OUIEJxKJC3YFbJI0pS8Yj9JzaJNRbMw61tJv6f4mw6MGfFM%2FiOlQK%2Fk23dC73JNwwopSXhLwfVgXz1oChqUXPOvZIgiMO8vmiRy9DTKhJrVG77787SJJJwABbEqqYravfXs0ouVUpd%2Fud%2FtCyZ6gp0xXVkChEph45yHa2VwpE6cyw9IIkjjCMEzzA&X-Amz-Signature=892b0c3869edd68cce8feeda28ad1f22a3d92f3a43b0bd846b889bf84078bb1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VK3LCTD6%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDYY1zmulMG6TvMERb0DhB%2FvrqHTcu4DZHB1oilrVuG6gIhAP2g9fFhW9cvlRG8z6Ku8XcnzwColXPFFrdsnGaRScsPKv8DCGkQABoMNjM3NDIzMTgzODA1Igw%2FUtwIE85zb%2BcQqvsq3AOa93xaIAgXxklkD6FUIVlBh0eZqDhdkak0gN61KtIbAU5O%2BbkBPANcYpNxpJ3FA%2F32FCd3mp3sxgqHjJea%2Bh7OE9WTkHEWRAVAnVCdZU2%2FIU7jwd6QqnEEgN0yKq29ad136FB3TbGq6cfnCHnByWDj8Qobpty87bn1B8pDF6UlgGIIFXGldHOqN0K37h8HmW3tjJZ2SSFFlCSn0xs082hHbrHjozYYNC4b%2BpLHE8KutJ2ZMAAphVD0WnwAJX%2Bg6TxqI%2BEg2TtwfV7XRLbmd2qfXcASWd2LJCUYPq7kAjASXlrI57RUwgEMq7MYXNaGR3qZjMnVvTUtVNHnhAbHgTg5eFfPnNxy4Fw%2B2t2tFS8I9c0KBJNbsWY5BUHLWI4lo26hf0u5Spy6UDgDza3lgqoqbW0Vhn9qYePfhvas%2F9FbGtI25LGpVRDUk9LM2S4guygvlpcDMJYpsivHRdC3uvC6zFgr8WjV8SoUvMn%2BGV1mvkacoKG5wsVV%2BCqHEHQH7LyXyFI5ZfRKm22GuZSU4Z9CfxA4R7VUcgPCRSrrIYpkLe1AAp3ZWyfVsmE2wJW1ogj4nI47xUxt856X5kINDJZnA66qCzVzZ8pT8Lf%2Bld4LWgKCoj0sHgq4cMin7jDPqbO%2BBjqkAfXw%2FotZILzKpIqsl7vb68lDLTwExNu%2FWr6VmV3%2FMVvxh81H7tQrIpNPfvlu7BgH1b3ttlV27YHCgrUcEegZh7wtci%2FJBCDjcQY%2FJO7V0hrYCg3c6BKmhmWdM9gM%2BIOS0UE6QSilEakl7YPAkClb0N6ZMcKVzT3nN7JlMgWA%2BjM37vaQxDB0UgPxHGQmUV9fZ5gvXNKYVUaDpjyQnVNFNoPIA%2BGb&X-Amz-Signature=5062f05a6b4ea6986e0c0344fd6ce29da80679dfc41eaf11c3eccc9f2290f58a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VK3LCTD6%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDYY1zmulMG6TvMERb0DhB%2FvrqHTcu4DZHB1oilrVuG6gIhAP2g9fFhW9cvlRG8z6Ku8XcnzwColXPFFrdsnGaRScsPKv8DCGkQABoMNjM3NDIzMTgzODA1Igw%2FUtwIE85zb%2BcQqvsq3AOa93xaIAgXxklkD6FUIVlBh0eZqDhdkak0gN61KtIbAU5O%2BbkBPANcYpNxpJ3FA%2F32FCd3mp3sxgqHjJea%2Bh7OE9WTkHEWRAVAnVCdZU2%2FIU7jwd6QqnEEgN0yKq29ad136FB3TbGq6cfnCHnByWDj8Qobpty87bn1B8pDF6UlgGIIFXGldHOqN0K37h8HmW3tjJZ2SSFFlCSn0xs082hHbrHjozYYNC4b%2BpLHE8KutJ2ZMAAphVD0WnwAJX%2Bg6TxqI%2BEg2TtwfV7XRLbmd2qfXcASWd2LJCUYPq7kAjASXlrI57RUwgEMq7MYXNaGR3qZjMnVvTUtVNHnhAbHgTg5eFfPnNxy4Fw%2B2t2tFS8I9c0KBJNbsWY5BUHLWI4lo26hf0u5Spy6UDgDza3lgqoqbW0Vhn9qYePfhvas%2F9FbGtI25LGpVRDUk9LM2S4guygvlpcDMJYpsivHRdC3uvC6zFgr8WjV8SoUvMn%2BGV1mvkacoKG5wsVV%2BCqHEHQH7LyXyFI5ZfRKm22GuZSU4Z9CfxA4R7VUcgPCRSrrIYpkLe1AAp3ZWyfVsmE2wJW1ogj4nI47xUxt856X5kINDJZnA66qCzVzZ8pT8Lf%2Bld4LWgKCoj0sHgq4cMin7jDPqbO%2BBjqkAfXw%2FotZILzKpIqsl7vb68lDLTwExNu%2FWr6VmV3%2FMVvxh81H7tQrIpNPfvlu7BgH1b3ttlV27YHCgrUcEegZh7wtci%2FJBCDjcQY%2FJO7V0hrYCg3c6BKmhmWdM9gM%2BIOS0UE6QSilEakl7YPAkClb0N6ZMcKVzT3nN7JlMgWA%2BjM37vaQxDB0UgPxHGQmUV9fZ5gvXNKYVUaDpjyQnVNFNoPIA%2BGb&X-Amz-Signature=4a51425ce5ea2a81d26538d2498fcc369881d02ccf10db0e7c94516c8c6c842b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
