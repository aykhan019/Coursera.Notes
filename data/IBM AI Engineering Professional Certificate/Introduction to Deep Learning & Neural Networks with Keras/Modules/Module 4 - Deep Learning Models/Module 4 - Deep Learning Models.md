

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ6OL7RP%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIG3fSgqXtSD9HDvl1vvwfEqxANgIvZThLABz1HWtLztwAiEA1Zq40QJgR7J0yc5sxWYOiFxYXwpN03Q53TOKPbfER5cq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNDeti1AbusiJc4n2CrcA7YSVpAheI4KOtiD0fL81TQwtUT9awMuvF%2Ft%2B6LzyNpSqCagSYYBGz0nad3pnszG9zf6f7EkHD9tuSQXxG089HylQyqmOc5O65XRswVeT6H7Z6f8L53cbtGb%2FhQE0B78QkDu%2B%2BIH%2FlJm6Hd8pIjIeNfRaws6ekxFqmSmJAG75z%2Fd1Tn0FYVICktJkLfZljK5V%2F9MtZmGkdz7slkuIKZtMSC8RjYEW9uYIY3RfVrNNkaGec%2FWKotqFsghXbrQpwpbMvIVwvqWjKHnRp9PZeynf1q2twqxg6yCK3rkxs%2FVqanY16ZzYeeMorFtFRHJ18aXai868si%2FB9qA50J7DsBpChB4qVjICRX0xStzYsiCT96LjGOXlbccrROwJHBjVhQizBFT9gBI7mDuWo6u3kU%2B5hepK4lJH5MQu2q7XER99oXoYAsafJUng2mt5h3ce179k%2BPu4qusIQLmS81d3RS8NWJVHY7pEuzKDBPJK7Jv3I6lwtjWnaSbDj%2Bt26MTkE7XlfXkVeZtfkuhluy304dRXQyOdztunnKRrv3bepflOnJFnsWtXL8xkYllPFAWWcW5FolZE14cqzWG98qmP6Kl3OXQv%2B4KgBcgK8P3wnsJHIkFHpe0kCpf5yEirnQOMMLkxL0GOqUBWkdbRGpq8dJLqWVbqhyyyTVlh47M7jkGSPkfoF%2B9zHWSoMOvvsERz7sKNinU6Dt9ZEVGlidxNfnc7ohTrDOaLeCu0Mf9ugz3Vg4kbxLHM9zX%2Bud9pNl3NO1ELuIYMcRGcwiMVdPOn%2BNwae1DHdH6syFwfUhFSL2as4X%2BNnMnVpH4pdF9j2T0X7WYOwEPppWZYRYli8hWPgeaQUMduzSYgNgKFwsg&X-Amz-Signature=097ad97f2e29849b0e43dbaaec258e09a23653e843ac8de8eb6a61c893d707c9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ6OL7RP%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIG3fSgqXtSD9HDvl1vvwfEqxANgIvZThLABz1HWtLztwAiEA1Zq40QJgR7J0yc5sxWYOiFxYXwpN03Q53TOKPbfER5cq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNDeti1AbusiJc4n2CrcA7YSVpAheI4KOtiD0fL81TQwtUT9awMuvF%2Ft%2B6LzyNpSqCagSYYBGz0nad3pnszG9zf6f7EkHD9tuSQXxG089HylQyqmOc5O65XRswVeT6H7Z6f8L53cbtGb%2FhQE0B78QkDu%2B%2BIH%2FlJm6Hd8pIjIeNfRaws6ekxFqmSmJAG75z%2Fd1Tn0FYVICktJkLfZljK5V%2F9MtZmGkdz7slkuIKZtMSC8RjYEW9uYIY3RfVrNNkaGec%2FWKotqFsghXbrQpwpbMvIVwvqWjKHnRp9PZeynf1q2twqxg6yCK3rkxs%2FVqanY16ZzYeeMorFtFRHJ18aXai868si%2FB9qA50J7DsBpChB4qVjICRX0xStzYsiCT96LjGOXlbccrROwJHBjVhQizBFT9gBI7mDuWo6u3kU%2B5hepK4lJH5MQu2q7XER99oXoYAsafJUng2mt5h3ce179k%2BPu4qusIQLmS81d3RS8NWJVHY7pEuzKDBPJK7Jv3I6lwtjWnaSbDj%2Bt26MTkE7XlfXkVeZtfkuhluy304dRXQyOdztunnKRrv3bepflOnJFnsWtXL8xkYllPFAWWcW5FolZE14cqzWG98qmP6Kl3OXQv%2B4KgBcgK8P3wnsJHIkFHpe0kCpf5yEirnQOMMLkxL0GOqUBWkdbRGpq8dJLqWVbqhyyyTVlh47M7jkGSPkfoF%2B9zHWSoMOvvsERz7sKNinU6Dt9ZEVGlidxNfnc7ohTrDOaLeCu0Mf9ugz3Vg4kbxLHM9zX%2Bud9pNl3NO1ELuIYMcRGcwiMVdPOn%2BNwae1DHdH6syFwfUhFSL2as4X%2BNnMnVpH4pdF9j2T0X7WYOwEPppWZYRYli8hWPgeaQUMduzSYgNgKFwsg&X-Amz-Signature=4ba0ea0326c525a7b06835ad0cd327808da6a1f0e9dec99abffaacd093ee9efd&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ6OL7RP%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIG3fSgqXtSD9HDvl1vvwfEqxANgIvZThLABz1HWtLztwAiEA1Zq40QJgR7J0yc5sxWYOiFxYXwpN03Q53TOKPbfER5cq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNDeti1AbusiJc4n2CrcA7YSVpAheI4KOtiD0fL81TQwtUT9awMuvF%2Ft%2B6LzyNpSqCagSYYBGz0nad3pnszG9zf6f7EkHD9tuSQXxG089HylQyqmOc5O65XRswVeT6H7Z6f8L53cbtGb%2FhQE0B78QkDu%2B%2BIH%2FlJm6Hd8pIjIeNfRaws6ekxFqmSmJAG75z%2Fd1Tn0FYVICktJkLfZljK5V%2F9MtZmGkdz7slkuIKZtMSC8RjYEW9uYIY3RfVrNNkaGec%2FWKotqFsghXbrQpwpbMvIVwvqWjKHnRp9PZeynf1q2twqxg6yCK3rkxs%2FVqanY16ZzYeeMorFtFRHJ18aXai868si%2FB9qA50J7DsBpChB4qVjICRX0xStzYsiCT96LjGOXlbccrROwJHBjVhQizBFT9gBI7mDuWo6u3kU%2B5hepK4lJH5MQu2q7XER99oXoYAsafJUng2mt5h3ce179k%2BPu4qusIQLmS81d3RS8NWJVHY7pEuzKDBPJK7Jv3I6lwtjWnaSbDj%2Bt26MTkE7XlfXkVeZtfkuhluy304dRXQyOdztunnKRrv3bepflOnJFnsWtXL8xkYllPFAWWcW5FolZE14cqzWG98qmP6Kl3OXQv%2B4KgBcgK8P3wnsJHIkFHpe0kCpf5yEirnQOMMLkxL0GOqUBWkdbRGpq8dJLqWVbqhyyyTVlh47M7jkGSPkfoF%2B9zHWSoMOvvsERz7sKNinU6Dt9ZEVGlidxNfnc7ohTrDOaLeCu0Mf9ugz3Vg4kbxLHM9zX%2Bud9pNl3NO1ELuIYMcRGcwiMVdPOn%2BNwae1DHdH6syFwfUhFSL2as4X%2BNnMnVpH4pdF9j2T0X7WYOwEPppWZYRYli8hWPgeaQUMduzSYgNgKFwsg&X-Amz-Signature=47683321d4d21848569ef06ed0e718590244958215606e270b383935cc44f330&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ6OL7RP%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIG3fSgqXtSD9HDvl1vvwfEqxANgIvZThLABz1HWtLztwAiEA1Zq40QJgR7J0yc5sxWYOiFxYXwpN03Q53TOKPbfER5cq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNDeti1AbusiJc4n2CrcA7YSVpAheI4KOtiD0fL81TQwtUT9awMuvF%2Ft%2B6LzyNpSqCagSYYBGz0nad3pnszG9zf6f7EkHD9tuSQXxG089HylQyqmOc5O65XRswVeT6H7Z6f8L53cbtGb%2FhQE0B78QkDu%2B%2BIH%2FlJm6Hd8pIjIeNfRaws6ekxFqmSmJAG75z%2Fd1Tn0FYVICktJkLfZljK5V%2F9MtZmGkdz7slkuIKZtMSC8RjYEW9uYIY3RfVrNNkaGec%2FWKotqFsghXbrQpwpbMvIVwvqWjKHnRp9PZeynf1q2twqxg6yCK3rkxs%2FVqanY16ZzYeeMorFtFRHJ18aXai868si%2FB9qA50J7DsBpChB4qVjICRX0xStzYsiCT96LjGOXlbccrROwJHBjVhQizBFT9gBI7mDuWo6u3kU%2B5hepK4lJH5MQu2q7XER99oXoYAsafJUng2mt5h3ce179k%2BPu4qusIQLmS81d3RS8NWJVHY7pEuzKDBPJK7Jv3I6lwtjWnaSbDj%2Bt26MTkE7XlfXkVeZtfkuhluy304dRXQyOdztunnKRrv3bepflOnJFnsWtXL8xkYllPFAWWcW5FolZE14cqzWG98qmP6Kl3OXQv%2B4KgBcgK8P3wnsJHIkFHpe0kCpf5yEirnQOMMLkxL0GOqUBWkdbRGpq8dJLqWVbqhyyyTVlh47M7jkGSPkfoF%2B9zHWSoMOvvsERz7sKNinU6Dt9ZEVGlidxNfnc7ohTrDOaLeCu0Mf9ugz3Vg4kbxLHM9zX%2Bud9pNl3NO1ELuIYMcRGcwiMVdPOn%2BNwae1DHdH6syFwfUhFSL2as4X%2BNnMnVpH4pdF9j2T0X7WYOwEPppWZYRYli8hWPgeaQUMduzSYgNgKFwsg&X-Amz-Signature=1e799a17efc080b9fae9e6cb6bb11c5d2461bd027a50384ca5532e6fe56637b4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ6OL7RP%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIG3fSgqXtSD9HDvl1vvwfEqxANgIvZThLABz1HWtLztwAiEA1Zq40QJgR7J0yc5sxWYOiFxYXwpN03Q53TOKPbfER5cq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNDeti1AbusiJc4n2CrcA7YSVpAheI4KOtiD0fL81TQwtUT9awMuvF%2Ft%2B6LzyNpSqCagSYYBGz0nad3pnszG9zf6f7EkHD9tuSQXxG089HylQyqmOc5O65XRswVeT6H7Z6f8L53cbtGb%2FhQE0B78QkDu%2B%2BIH%2FlJm6Hd8pIjIeNfRaws6ekxFqmSmJAG75z%2Fd1Tn0FYVICktJkLfZljK5V%2F9MtZmGkdz7slkuIKZtMSC8RjYEW9uYIY3RfVrNNkaGec%2FWKotqFsghXbrQpwpbMvIVwvqWjKHnRp9PZeynf1q2twqxg6yCK3rkxs%2FVqanY16ZzYeeMorFtFRHJ18aXai868si%2FB9qA50J7DsBpChB4qVjICRX0xStzYsiCT96LjGOXlbccrROwJHBjVhQizBFT9gBI7mDuWo6u3kU%2B5hepK4lJH5MQu2q7XER99oXoYAsafJUng2mt5h3ce179k%2BPu4qusIQLmS81d3RS8NWJVHY7pEuzKDBPJK7Jv3I6lwtjWnaSbDj%2Bt26MTkE7XlfXkVeZtfkuhluy304dRXQyOdztunnKRrv3bepflOnJFnsWtXL8xkYllPFAWWcW5FolZE14cqzWG98qmP6Kl3OXQv%2B4KgBcgK8P3wnsJHIkFHpe0kCpf5yEirnQOMMLkxL0GOqUBWkdbRGpq8dJLqWVbqhyyyTVlh47M7jkGSPkfoF%2B9zHWSoMOvvsERz7sKNinU6Dt9ZEVGlidxNfnc7ohTrDOaLeCu0Mf9ugz3Vg4kbxLHM9zX%2Bud9pNl3NO1ELuIYMcRGcwiMVdPOn%2BNwae1DHdH6syFwfUhFSL2as4X%2BNnMnVpH4pdF9j2T0X7WYOwEPppWZYRYli8hWPgeaQUMduzSYgNgKFwsg&X-Amz-Signature=18b1bd533fa24796639bd3e32d501ef744f7bed1b7ed2300529acefc49477356&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ6OL7RP%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIG3fSgqXtSD9HDvl1vvwfEqxANgIvZThLABz1HWtLztwAiEA1Zq40QJgR7J0yc5sxWYOiFxYXwpN03Q53TOKPbfER5cq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNDeti1AbusiJc4n2CrcA7YSVpAheI4KOtiD0fL81TQwtUT9awMuvF%2Ft%2B6LzyNpSqCagSYYBGz0nad3pnszG9zf6f7EkHD9tuSQXxG089HylQyqmOc5O65XRswVeT6H7Z6f8L53cbtGb%2FhQE0B78QkDu%2B%2BIH%2FlJm6Hd8pIjIeNfRaws6ekxFqmSmJAG75z%2Fd1Tn0FYVICktJkLfZljK5V%2F9MtZmGkdz7slkuIKZtMSC8RjYEW9uYIY3RfVrNNkaGec%2FWKotqFsghXbrQpwpbMvIVwvqWjKHnRp9PZeynf1q2twqxg6yCK3rkxs%2FVqanY16ZzYeeMorFtFRHJ18aXai868si%2FB9qA50J7DsBpChB4qVjICRX0xStzYsiCT96LjGOXlbccrROwJHBjVhQizBFT9gBI7mDuWo6u3kU%2B5hepK4lJH5MQu2q7XER99oXoYAsafJUng2mt5h3ce179k%2BPu4qusIQLmS81d3RS8NWJVHY7pEuzKDBPJK7Jv3I6lwtjWnaSbDj%2Bt26MTkE7XlfXkVeZtfkuhluy304dRXQyOdztunnKRrv3bepflOnJFnsWtXL8xkYllPFAWWcW5FolZE14cqzWG98qmP6Kl3OXQv%2B4KgBcgK8P3wnsJHIkFHpe0kCpf5yEirnQOMMLkxL0GOqUBWkdbRGpq8dJLqWVbqhyyyTVlh47M7jkGSPkfoF%2B9zHWSoMOvvsERz7sKNinU6Dt9ZEVGlidxNfnc7ohTrDOaLeCu0Mf9ugz3Vg4kbxLHM9zX%2Bud9pNl3NO1ELuIYMcRGcwiMVdPOn%2BNwae1DHdH6syFwfUhFSL2as4X%2BNnMnVpH4pdF9j2T0X7WYOwEPppWZYRYli8hWPgeaQUMduzSYgNgKFwsg&X-Amz-Signature=b571d5e280c15bb5e0186d44b3ca77a526093d03ffb84d5ad3ace2c6859acb65&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ6OL7RP%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIG3fSgqXtSD9HDvl1vvwfEqxANgIvZThLABz1HWtLztwAiEA1Zq40QJgR7J0yc5sxWYOiFxYXwpN03Q53TOKPbfER5cq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNDeti1AbusiJc4n2CrcA7YSVpAheI4KOtiD0fL81TQwtUT9awMuvF%2Ft%2B6LzyNpSqCagSYYBGz0nad3pnszG9zf6f7EkHD9tuSQXxG089HylQyqmOc5O65XRswVeT6H7Z6f8L53cbtGb%2FhQE0B78QkDu%2B%2BIH%2FlJm6Hd8pIjIeNfRaws6ekxFqmSmJAG75z%2Fd1Tn0FYVICktJkLfZljK5V%2F9MtZmGkdz7slkuIKZtMSC8RjYEW9uYIY3RfVrNNkaGec%2FWKotqFsghXbrQpwpbMvIVwvqWjKHnRp9PZeynf1q2twqxg6yCK3rkxs%2FVqanY16ZzYeeMorFtFRHJ18aXai868si%2FB9qA50J7DsBpChB4qVjICRX0xStzYsiCT96LjGOXlbccrROwJHBjVhQizBFT9gBI7mDuWo6u3kU%2B5hepK4lJH5MQu2q7XER99oXoYAsafJUng2mt5h3ce179k%2BPu4qusIQLmS81d3RS8NWJVHY7pEuzKDBPJK7Jv3I6lwtjWnaSbDj%2Bt26MTkE7XlfXkVeZtfkuhluy304dRXQyOdztunnKRrv3bepflOnJFnsWtXL8xkYllPFAWWcW5FolZE14cqzWG98qmP6Kl3OXQv%2B4KgBcgK8P3wnsJHIkFHpe0kCpf5yEirnQOMMLkxL0GOqUBWkdbRGpq8dJLqWVbqhyyyTVlh47M7jkGSPkfoF%2B9zHWSoMOvvsERz7sKNinU6Dt9ZEVGlidxNfnc7ohTrDOaLeCu0Mf9ugz3Vg4kbxLHM9zX%2Bud9pNl3NO1ELuIYMcRGcwiMVdPOn%2BNwae1DHdH6syFwfUhFSL2as4X%2BNnMnVpH4pdF9j2T0X7WYOwEPppWZYRYli8hWPgeaQUMduzSYgNgKFwsg&X-Amz-Signature=28af20f50aded9e14a500946609efd6699fad290695fbbaa0a13156a5c7cc8d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ6OL7RP%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIG3fSgqXtSD9HDvl1vvwfEqxANgIvZThLABz1HWtLztwAiEA1Zq40QJgR7J0yc5sxWYOiFxYXwpN03Q53TOKPbfER5cq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNDeti1AbusiJc4n2CrcA7YSVpAheI4KOtiD0fL81TQwtUT9awMuvF%2Ft%2B6LzyNpSqCagSYYBGz0nad3pnszG9zf6f7EkHD9tuSQXxG089HylQyqmOc5O65XRswVeT6H7Z6f8L53cbtGb%2FhQE0B78QkDu%2B%2BIH%2FlJm6Hd8pIjIeNfRaws6ekxFqmSmJAG75z%2Fd1Tn0FYVICktJkLfZljK5V%2F9MtZmGkdz7slkuIKZtMSC8RjYEW9uYIY3RfVrNNkaGec%2FWKotqFsghXbrQpwpbMvIVwvqWjKHnRp9PZeynf1q2twqxg6yCK3rkxs%2FVqanY16ZzYeeMorFtFRHJ18aXai868si%2FB9qA50J7DsBpChB4qVjICRX0xStzYsiCT96LjGOXlbccrROwJHBjVhQizBFT9gBI7mDuWo6u3kU%2B5hepK4lJH5MQu2q7XER99oXoYAsafJUng2mt5h3ce179k%2BPu4qusIQLmS81d3RS8NWJVHY7pEuzKDBPJK7Jv3I6lwtjWnaSbDj%2Bt26MTkE7XlfXkVeZtfkuhluy304dRXQyOdztunnKRrv3bepflOnJFnsWtXL8xkYllPFAWWcW5FolZE14cqzWG98qmP6Kl3OXQv%2B4KgBcgK8P3wnsJHIkFHpe0kCpf5yEirnQOMMLkxL0GOqUBWkdbRGpq8dJLqWVbqhyyyTVlh47M7jkGSPkfoF%2B9zHWSoMOvvsERz7sKNinU6Dt9ZEVGlidxNfnc7ohTrDOaLeCu0Mf9ugz3Vg4kbxLHM9zX%2Bud9pNl3NO1ELuIYMcRGcwiMVdPOn%2BNwae1DHdH6syFwfUhFSL2as4X%2BNnMnVpH4pdF9j2T0X7WYOwEPppWZYRYli8hWPgeaQUMduzSYgNgKFwsg&X-Amz-Signature=e9b68685ec0acb2a01d1588412650bec28692094be560fff2506d1567cbd686e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ6OL7RP%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIG3fSgqXtSD9HDvl1vvwfEqxANgIvZThLABz1HWtLztwAiEA1Zq40QJgR7J0yc5sxWYOiFxYXwpN03Q53TOKPbfER5cq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNDeti1AbusiJc4n2CrcA7YSVpAheI4KOtiD0fL81TQwtUT9awMuvF%2Ft%2B6LzyNpSqCagSYYBGz0nad3pnszG9zf6f7EkHD9tuSQXxG089HylQyqmOc5O65XRswVeT6H7Z6f8L53cbtGb%2FhQE0B78QkDu%2B%2BIH%2FlJm6Hd8pIjIeNfRaws6ekxFqmSmJAG75z%2Fd1Tn0FYVICktJkLfZljK5V%2F9MtZmGkdz7slkuIKZtMSC8RjYEW9uYIY3RfVrNNkaGec%2FWKotqFsghXbrQpwpbMvIVwvqWjKHnRp9PZeynf1q2twqxg6yCK3rkxs%2FVqanY16ZzYeeMorFtFRHJ18aXai868si%2FB9qA50J7DsBpChB4qVjICRX0xStzYsiCT96LjGOXlbccrROwJHBjVhQizBFT9gBI7mDuWo6u3kU%2B5hepK4lJH5MQu2q7XER99oXoYAsafJUng2mt5h3ce179k%2BPu4qusIQLmS81d3RS8NWJVHY7pEuzKDBPJK7Jv3I6lwtjWnaSbDj%2Bt26MTkE7XlfXkVeZtfkuhluy304dRXQyOdztunnKRrv3bepflOnJFnsWtXL8xkYllPFAWWcW5FolZE14cqzWG98qmP6Kl3OXQv%2B4KgBcgK8P3wnsJHIkFHpe0kCpf5yEirnQOMMLkxL0GOqUBWkdbRGpq8dJLqWVbqhyyyTVlh47M7jkGSPkfoF%2B9zHWSoMOvvsERz7sKNinU6Dt9ZEVGlidxNfnc7ohTrDOaLeCu0Mf9ugz3Vg4kbxLHM9zX%2Bud9pNl3NO1ELuIYMcRGcwiMVdPOn%2BNwae1DHdH6syFwfUhFSL2as4X%2BNnMnVpH4pdF9j2T0X7WYOwEPppWZYRYli8hWPgeaQUMduzSYgNgKFwsg&X-Amz-Signature=e7953eac7358e3cfd412df5050f320c1dfdc2a98a4db9d7d812adc66acf7ac40&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLOSWDYI%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCt%2BVec4NoYEJ5gEGmJhA7oyH97scGO1MC2bymQ8tmh%2FgIgFnOVMfWklYShFcdt6rJ0dlFnXn1tBlfwFttGPR%2FMWmYq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNEQUj%2BzAQZbUAma3ircAzwjfnapDJF49phjpz8f%2Blzp%2Bct7WswV6YTQfxX36%2Fqa1aqa3lKdCud0GvwL2%2BEjB1O0n6ezASbAMMbMBiwPoeETLoMR3IQh0Jh1vyKlYq515InsUqQFbHFxC0tLiY2gDYlbX48LVYBTqA1B26OEberZ7v9Zcot17L%2FBY9riDHYb0177BRp1dIBuFC3TEQ15zsX2MekqkuDahRv6LSTnEp19wHft3uRCA9UK%2FklktOcmIg2UdfaE6%2BtKdmHR1w6iZQvC9cQjDCmRLZsBvnVniMEARzFY89c4cS6jcRTm0QCYCtpX7S%2BzxP%2BuguOCR7FeUZhJImP1VJS78ALiRsEoWG1HpcZwPIz%2BTCaYzyD5U5ZfI6pB93BvN0eOSLpeLr4TaQDdY96KE9KTGhNYR07%2BVK3jIFAIC83sOPheFbl7kFEpNB1GzW%2B9yGd8yqoCwY2d5ok3I80acPIgKY0K%2BgDBQ03NZ1e442yFEyIXCNjjh%2Fi3pr%2FGgAbZIx9%2Bsftj9D9Oq533Jsiq1TYzOyomaQkWc%2FxFgtxX2JINSrzP2n6neYg33%2BdjqIPxMAmGcYjMRlbADfpBIt9RItRUoqH91uM3kodvvOXWIzkTe05Ygd1WPA7OzmJRjyuaKguAUzsmMOXkxL0GOqUBH2EIfG3rXltRlBMk6BRPOwKiLgWYZCPqDVfkaFrsIQpZbitDC%2BJBBFYDooDhsFgGHEcmHCjPNWmvtmKREHKPeB1ZjM3mgwjnj6sguBydqftiCMgcOWu8Zrwey%2Bf7HGoH8Go3A96q6qJqcYQ4vuGip0wgyycvFY4dRJOc5SD7wk7bJNiaV0nNfklqhdz09n5lJHcTqz%2FTV6frCOa7HgozX%2FcrJ51n&X-Amz-Signature=bc651f1e0502f63835bbe71691fb652dbc2fee0a4df5b3d21f97a54cbe6ca96f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLOSWDYI%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCt%2BVec4NoYEJ5gEGmJhA7oyH97scGO1MC2bymQ8tmh%2FgIgFnOVMfWklYShFcdt6rJ0dlFnXn1tBlfwFttGPR%2FMWmYq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNEQUj%2BzAQZbUAma3ircAzwjfnapDJF49phjpz8f%2Blzp%2Bct7WswV6YTQfxX36%2Fqa1aqa3lKdCud0GvwL2%2BEjB1O0n6ezASbAMMbMBiwPoeETLoMR3IQh0Jh1vyKlYq515InsUqQFbHFxC0tLiY2gDYlbX48LVYBTqA1B26OEberZ7v9Zcot17L%2FBY9riDHYb0177BRp1dIBuFC3TEQ15zsX2MekqkuDahRv6LSTnEp19wHft3uRCA9UK%2FklktOcmIg2UdfaE6%2BtKdmHR1w6iZQvC9cQjDCmRLZsBvnVniMEARzFY89c4cS6jcRTm0QCYCtpX7S%2BzxP%2BuguOCR7FeUZhJImP1VJS78ALiRsEoWG1HpcZwPIz%2BTCaYzyD5U5ZfI6pB93BvN0eOSLpeLr4TaQDdY96KE9KTGhNYR07%2BVK3jIFAIC83sOPheFbl7kFEpNB1GzW%2B9yGd8yqoCwY2d5ok3I80acPIgKY0K%2BgDBQ03NZ1e442yFEyIXCNjjh%2Fi3pr%2FGgAbZIx9%2Bsftj9D9Oq533Jsiq1TYzOyomaQkWc%2FxFgtxX2JINSrzP2n6neYg33%2BdjqIPxMAmGcYjMRlbADfpBIt9RItRUoqH91uM3kodvvOXWIzkTe05Ygd1WPA7OzmJRjyuaKguAUzsmMOXkxL0GOqUBH2EIfG3rXltRlBMk6BRPOwKiLgWYZCPqDVfkaFrsIQpZbitDC%2BJBBFYDooDhsFgGHEcmHCjPNWmvtmKREHKPeB1ZjM3mgwjnj6sguBydqftiCMgcOWu8Zrwey%2Bf7HGoH8Go3A96q6qJqcYQ4vuGip0wgyycvFY4dRJOc5SD7wk7bJNiaV0nNfklqhdz09n5lJHcTqz%2FTV6frCOa7HgozX%2FcrJ51n&X-Amz-Signature=cb4cbabec6feb2464c12c7baf3642f8ff71e73a17bbdadb2934afaab7160da32&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
