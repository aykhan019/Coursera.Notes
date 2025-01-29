

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V6ZQZUV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDbX46j3ByqYmk%2BAY0PrmQCVgJ0VgWjt%2FxvJQMJw5SubgIgBK5jzHs85Q0NH%2BOR2vHqCoQxDOtPwfiTqLrWSzqqJQ0qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHMotIgdQjGVVHoICrcA7iHhmFD4TaNY2Dkq0lEvQTf%2F7N3D8XAPi5ZckpzWndZX9WQdh8Qkxuk%2BskUm%2FWOz2B%2FTmCRE%2FyuMu9Qc3irfXl%2BqIWf6K9oFjOvvBjdzfimWHlecd347bCjkso%2Fsx9p%2BH1stKcKi0dBF3wxsSHrhwm9Pl%2FyQpaWHFhZdKmMWxkuDPxPwDwdnGHusLKF7q917Abd10Rk55IKL%2FuLXi%2BZL0tCUY33%2BjLVi1v%2BgPF2NZr4%2FGOwUMXfbiXg64%2FhtjB%2FduArAtp7eKsLsZotZJAoyEx0elkNcGVVPbYj2qZHh8%2BNHJZHbI8Km4UCdtEg28dCiEzO7AFUNxuc3vLQ7plsCEkqXmUZJu4EoacjRXnNFSV66vu7Hi6H0rnT7JVN9CpRqZUYH36vmatWkswR6UwnaEvEiqaQKV9gP6HSnPtJXLS6WvdZwAzlTWOnw61V988TgVl1j02D6k6%2B0TaCfTpMBL%2BIMR8yFTXccqRIy0KZZng6ZnrKTbq5kZcjuWt4AXSTXafj35rhTU1Qb8%2BzhWQ4vrxj%2BUun8KHhC7aICC4WZ6vY7Rvy7u%2FlfiobxauEZ1UNLZXI5nz6df5yWg1Of0rn6O%2FIMYnc7%2BiQg%2B9DCQOw9Ari081myn5NnzPoS1COMOCf5rwGOqUBx9hsIyBcm6X3UuegHN9IM8sqb8fYxog39ZcHCJYy4Jm3PNpyNfjf8ZUuUlj8mUbisat6hVBDkrtZTdhmrtoCQN95l4iLDuQX8w%2FzpLKzt8P%2B4s92%2BVw2NN0EZ%2Ffmtccbxz5t%2FeHbxmw%2FsdPmTuQBkPe0drtNWLFi%2BCmZqqNbtyDxNC%2FqjOKXycwSaFgoe3vN7ALS%2BE8NaRzA5G4074MwiscZf%2F6%2F&X-Amz-Signature=e26e62f83315ebeedd7bba6f76769435fd660400471aa6e165ef0463f9e59a65&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V6ZQZUV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDbX46j3ByqYmk%2BAY0PrmQCVgJ0VgWjt%2FxvJQMJw5SubgIgBK5jzHs85Q0NH%2BOR2vHqCoQxDOtPwfiTqLrWSzqqJQ0qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHMotIgdQjGVVHoICrcA7iHhmFD4TaNY2Dkq0lEvQTf%2F7N3D8XAPi5ZckpzWndZX9WQdh8Qkxuk%2BskUm%2FWOz2B%2FTmCRE%2FyuMu9Qc3irfXl%2BqIWf6K9oFjOvvBjdzfimWHlecd347bCjkso%2Fsx9p%2BH1stKcKi0dBF3wxsSHrhwm9Pl%2FyQpaWHFhZdKmMWxkuDPxPwDwdnGHusLKF7q917Abd10Rk55IKL%2FuLXi%2BZL0tCUY33%2BjLVi1v%2BgPF2NZr4%2FGOwUMXfbiXg64%2FhtjB%2FduArAtp7eKsLsZotZJAoyEx0elkNcGVVPbYj2qZHh8%2BNHJZHbI8Km4UCdtEg28dCiEzO7AFUNxuc3vLQ7plsCEkqXmUZJu4EoacjRXnNFSV66vu7Hi6H0rnT7JVN9CpRqZUYH36vmatWkswR6UwnaEvEiqaQKV9gP6HSnPtJXLS6WvdZwAzlTWOnw61V988TgVl1j02D6k6%2B0TaCfTpMBL%2BIMR8yFTXccqRIy0KZZng6ZnrKTbq5kZcjuWt4AXSTXafj35rhTU1Qb8%2BzhWQ4vrxj%2BUun8KHhC7aICC4WZ6vY7Rvy7u%2FlfiobxauEZ1UNLZXI5nz6df5yWg1Of0rn6O%2FIMYnc7%2BiQg%2B9DCQOw9Ari081myn5NnzPoS1COMOCf5rwGOqUBx9hsIyBcm6X3UuegHN9IM8sqb8fYxog39ZcHCJYy4Jm3PNpyNfjf8ZUuUlj8mUbisat6hVBDkrtZTdhmrtoCQN95l4iLDuQX8w%2FzpLKzt8P%2B4s92%2BVw2NN0EZ%2Ffmtccbxz5t%2FeHbxmw%2FsdPmTuQBkPe0drtNWLFi%2BCmZqqNbtyDxNC%2FqjOKXycwSaFgoe3vN7ALS%2BE8NaRzA5G4074MwiscZf%2F6%2F&X-Amz-Signature=ae5458b30aa5da9e8fee598f0de1a69863cdd2ac09d62402f5f26040018f012a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V6ZQZUV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDbX46j3ByqYmk%2BAY0PrmQCVgJ0VgWjt%2FxvJQMJw5SubgIgBK5jzHs85Q0NH%2BOR2vHqCoQxDOtPwfiTqLrWSzqqJQ0qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHMotIgdQjGVVHoICrcA7iHhmFD4TaNY2Dkq0lEvQTf%2F7N3D8XAPi5ZckpzWndZX9WQdh8Qkxuk%2BskUm%2FWOz2B%2FTmCRE%2FyuMu9Qc3irfXl%2BqIWf6K9oFjOvvBjdzfimWHlecd347bCjkso%2Fsx9p%2BH1stKcKi0dBF3wxsSHrhwm9Pl%2FyQpaWHFhZdKmMWxkuDPxPwDwdnGHusLKF7q917Abd10Rk55IKL%2FuLXi%2BZL0tCUY33%2BjLVi1v%2BgPF2NZr4%2FGOwUMXfbiXg64%2FhtjB%2FduArAtp7eKsLsZotZJAoyEx0elkNcGVVPbYj2qZHh8%2BNHJZHbI8Km4UCdtEg28dCiEzO7AFUNxuc3vLQ7plsCEkqXmUZJu4EoacjRXnNFSV66vu7Hi6H0rnT7JVN9CpRqZUYH36vmatWkswR6UwnaEvEiqaQKV9gP6HSnPtJXLS6WvdZwAzlTWOnw61V988TgVl1j02D6k6%2B0TaCfTpMBL%2BIMR8yFTXccqRIy0KZZng6ZnrKTbq5kZcjuWt4AXSTXafj35rhTU1Qb8%2BzhWQ4vrxj%2BUun8KHhC7aICC4WZ6vY7Rvy7u%2FlfiobxauEZ1UNLZXI5nz6df5yWg1Of0rn6O%2FIMYnc7%2BiQg%2B9DCQOw9Ari081myn5NnzPoS1COMOCf5rwGOqUBx9hsIyBcm6X3UuegHN9IM8sqb8fYxog39ZcHCJYy4Jm3PNpyNfjf8ZUuUlj8mUbisat6hVBDkrtZTdhmrtoCQN95l4iLDuQX8w%2FzpLKzt8P%2B4s92%2BVw2NN0EZ%2Ffmtccbxz5t%2FeHbxmw%2FsdPmTuQBkPe0drtNWLFi%2BCmZqqNbtyDxNC%2FqjOKXycwSaFgoe3vN7ALS%2BE8NaRzA5G4074MwiscZf%2F6%2F&X-Amz-Signature=807f4d550affe06a84527c632724d8deb2e6590973ff1bab9bea1ec1f181bd08&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V6ZQZUV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDbX46j3ByqYmk%2BAY0PrmQCVgJ0VgWjt%2FxvJQMJw5SubgIgBK5jzHs85Q0NH%2BOR2vHqCoQxDOtPwfiTqLrWSzqqJQ0qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHMotIgdQjGVVHoICrcA7iHhmFD4TaNY2Dkq0lEvQTf%2F7N3D8XAPi5ZckpzWndZX9WQdh8Qkxuk%2BskUm%2FWOz2B%2FTmCRE%2FyuMu9Qc3irfXl%2BqIWf6K9oFjOvvBjdzfimWHlecd347bCjkso%2Fsx9p%2BH1stKcKi0dBF3wxsSHrhwm9Pl%2FyQpaWHFhZdKmMWxkuDPxPwDwdnGHusLKF7q917Abd10Rk55IKL%2FuLXi%2BZL0tCUY33%2BjLVi1v%2BgPF2NZr4%2FGOwUMXfbiXg64%2FhtjB%2FduArAtp7eKsLsZotZJAoyEx0elkNcGVVPbYj2qZHh8%2BNHJZHbI8Km4UCdtEg28dCiEzO7AFUNxuc3vLQ7plsCEkqXmUZJu4EoacjRXnNFSV66vu7Hi6H0rnT7JVN9CpRqZUYH36vmatWkswR6UwnaEvEiqaQKV9gP6HSnPtJXLS6WvdZwAzlTWOnw61V988TgVl1j02D6k6%2B0TaCfTpMBL%2BIMR8yFTXccqRIy0KZZng6ZnrKTbq5kZcjuWt4AXSTXafj35rhTU1Qb8%2BzhWQ4vrxj%2BUun8KHhC7aICC4WZ6vY7Rvy7u%2FlfiobxauEZ1UNLZXI5nz6df5yWg1Of0rn6O%2FIMYnc7%2BiQg%2B9DCQOw9Ari081myn5NnzPoS1COMOCf5rwGOqUBx9hsIyBcm6X3UuegHN9IM8sqb8fYxog39ZcHCJYy4Jm3PNpyNfjf8ZUuUlj8mUbisat6hVBDkrtZTdhmrtoCQN95l4iLDuQX8w%2FzpLKzt8P%2B4s92%2BVw2NN0EZ%2Ffmtccbxz5t%2FeHbxmw%2FsdPmTuQBkPe0drtNWLFi%2BCmZqqNbtyDxNC%2FqjOKXycwSaFgoe3vN7ALS%2BE8NaRzA5G4074MwiscZf%2F6%2F&X-Amz-Signature=2f44ef0fa3f96d0dc29f232275c3b82ad02749e7228dca153d2f41eee842d4ad&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V6ZQZUV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDbX46j3ByqYmk%2BAY0PrmQCVgJ0VgWjt%2FxvJQMJw5SubgIgBK5jzHs85Q0NH%2BOR2vHqCoQxDOtPwfiTqLrWSzqqJQ0qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHMotIgdQjGVVHoICrcA7iHhmFD4TaNY2Dkq0lEvQTf%2F7N3D8XAPi5ZckpzWndZX9WQdh8Qkxuk%2BskUm%2FWOz2B%2FTmCRE%2FyuMu9Qc3irfXl%2BqIWf6K9oFjOvvBjdzfimWHlecd347bCjkso%2Fsx9p%2BH1stKcKi0dBF3wxsSHrhwm9Pl%2FyQpaWHFhZdKmMWxkuDPxPwDwdnGHusLKF7q917Abd10Rk55IKL%2FuLXi%2BZL0tCUY33%2BjLVi1v%2BgPF2NZr4%2FGOwUMXfbiXg64%2FhtjB%2FduArAtp7eKsLsZotZJAoyEx0elkNcGVVPbYj2qZHh8%2BNHJZHbI8Km4UCdtEg28dCiEzO7AFUNxuc3vLQ7plsCEkqXmUZJu4EoacjRXnNFSV66vu7Hi6H0rnT7JVN9CpRqZUYH36vmatWkswR6UwnaEvEiqaQKV9gP6HSnPtJXLS6WvdZwAzlTWOnw61V988TgVl1j02D6k6%2B0TaCfTpMBL%2BIMR8yFTXccqRIy0KZZng6ZnrKTbq5kZcjuWt4AXSTXafj35rhTU1Qb8%2BzhWQ4vrxj%2BUun8KHhC7aICC4WZ6vY7Rvy7u%2FlfiobxauEZ1UNLZXI5nz6df5yWg1Of0rn6O%2FIMYnc7%2BiQg%2B9DCQOw9Ari081myn5NnzPoS1COMOCf5rwGOqUBx9hsIyBcm6X3UuegHN9IM8sqb8fYxog39ZcHCJYy4Jm3PNpyNfjf8ZUuUlj8mUbisat6hVBDkrtZTdhmrtoCQN95l4iLDuQX8w%2FzpLKzt8P%2B4s92%2BVw2NN0EZ%2Ffmtccbxz5t%2FeHbxmw%2FsdPmTuQBkPe0drtNWLFi%2BCmZqqNbtyDxNC%2FqjOKXycwSaFgoe3vN7ALS%2BE8NaRzA5G4074MwiscZf%2F6%2F&X-Amz-Signature=41c465e1326105c07a8f16e83b8d69af7e02feb862ca05dd124d73ae40146a5c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V6ZQZUV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDbX46j3ByqYmk%2BAY0PrmQCVgJ0VgWjt%2FxvJQMJw5SubgIgBK5jzHs85Q0NH%2BOR2vHqCoQxDOtPwfiTqLrWSzqqJQ0qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHMotIgdQjGVVHoICrcA7iHhmFD4TaNY2Dkq0lEvQTf%2F7N3D8XAPi5ZckpzWndZX9WQdh8Qkxuk%2BskUm%2FWOz2B%2FTmCRE%2FyuMu9Qc3irfXl%2BqIWf6K9oFjOvvBjdzfimWHlecd347bCjkso%2Fsx9p%2BH1stKcKi0dBF3wxsSHrhwm9Pl%2FyQpaWHFhZdKmMWxkuDPxPwDwdnGHusLKF7q917Abd10Rk55IKL%2FuLXi%2BZL0tCUY33%2BjLVi1v%2BgPF2NZr4%2FGOwUMXfbiXg64%2FhtjB%2FduArAtp7eKsLsZotZJAoyEx0elkNcGVVPbYj2qZHh8%2BNHJZHbI8Km4UCdtEg28dCiEzO7AFUNxuc3vLQ7plsCEkqXmUZJu4EoacjRXnNFSV66vu7Hi6H0rnT7JVN9CpRqZUYH36vmatWkswR6UwnaEvEiqaQKV9gP6HSnPtJXLS6WvdZwAzlTWOnw61V988TgVl1j02D6k6%2B0TaCfTpMBL%2BIMR8yFTXccqRIy0KZZng6ZnrKTbq5kZcjuWt4AXSTXafj35rhTU1Qb8%2BzhWQ4vrxj%2BUun8KHhC7aICC4WZ6vY7Rvy7u%2FlfiobxauEZ1UNLZXI5nz6df5yWg1Of0rn6O%2FIMYnc7%2BiQg%2B9DCQOw9Ari081myn5NnzPoS1COMOCf5rwGOqUBx9hsIyBcm6X3UuegHN9IM8sqb8fYxog39ZcHCJYy4Jm3PNpyNfjf8ZUuUlj8mUbisat6hVBDkrtZTdhmrtoCQN95l4iLDuQX8w%2FzpLKzt8P%2B4s92%2BVw2NN0EZ%2Ffmtccbxz5t%2FeHbxmw%2FsdPmTuQBkPe0drtNWLFi%2BCmZqqNbtyDxNC%2FqjOKXycwSaFgoe3vN7ALS%2BE8NaRzA5G4074MwiscZf%2F6%2F&X-Amz-Signature=ad9c2ae6ff38ca5efd0ee2c13d060db73bc67d014017f79565f053fa7a48aff6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V6ZQZUV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDbX46j3ByqYmk%2BAY0PrmQCVgJ0VgWjt%2FxvJQMJw5SubgIgBK5jzHs85Q0NH%2BOR2vHqCoQxDOtPwfiTqLrWSzqqJQ0qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHMotIgdQjGVVHoICrcA7iHhmFD4TaNY2Dkq0lEvQTf%2F7N3D8XAPi5ZckpzWndZX9WQdh8Qkxuk%2BskUm%2FWOz2B%2FTmCRE%2FyuMu9Qc3irfXl%2BqIWf6K9oFjOvvBjdzfimWHlecd347bCjkso%2Fsx9p%2BH1stKcKi0dBF3wxsSHrhwm9Pl%2FyQpaWHFhZdKmMWxkuDPxPwDwdnGHusLKF7q917Abd10Rk55IKL%2FuLXi%2BZL0tCUY33%2BjLVi1v%2BgPF2NZr4%2FGOwUMXfbiXg64%2FhtjB%2FduArAtp7eKsLsZotZJAoyEx0elkNcGVVPbYj2qZHh8%2BNHJZHbI8Km4UCdtEg28dCiEzO7AFUNxuc3vLQ7plsCEkqXmUZJu4EoacjRXnNFSV66vu7Hi6H0rnT7JVN9CpRqZUYH36vmatWkswR6UwnaEvEiqaQKV9gP6HSnPtJXLS6WvdZwAzlTWOnw61V988TgVl1j02D6k6%2B0TaCfTpMBL%2BIMR8yFTXccqRIy0KZZng6ZnrKTbq5kZcjuWt4AXSTXafj35rhTU1Qb8%2BzhWQ4vrxj%2BUun8KHhC7aICC4WZ6vY7Rvy7u%2FlfiobxauEZ1UNLZXI5nz6df5yWg1Of0rn6O%2FIMYnc7%2BiQg%2B9DCQOw9Ari081myn5NnzPoS1COMOCf5rwGOqUBx9hsIyBcm6X3UuegHN9IM8sqb8fYxog39ZcHCJYy4Jm3PNpyNfjf8ZUuUlj8mUbisat6hVBDkrtZTdhmrtoCQN95l4iLDuQX8w%2FzpLKzt8P%2B4s92%2BVw2NN0EZ%2Ffmtccbxz5t%2FeHbxmw%2FsdPmTuQBkPe0drtNWLFi%2BCmZqqNbtyDxNC%2FqjOKXycwSaFgoe3vN7ALS%2BE8NaRzA5G4074MwiscZf%2F6%2F&X-Amz-Signature=2702a6676f3cf90654bbf638de01ee4afcf18fb983cd439213a592168f39c84d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V6ZQZUV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDbX46j3ByqYmk%2BAY0PrmQCVgJ0VgWjt%2FxvJQMJw5SubgIgBK5jzHs85Q0NH%2BOR2vHqCoQxDOtPwfiTqLrWSzqqJQ0qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHMotIgdQjGVVHoICrcA7iHhmFD4TaNY2Dkq0lEvQTf%2F7N3D8XAPi5ZckpzWndZX9WQdh8Qkxuk%2BskUm%2FWOz2B%2FTmCRE%2FyuMu9Qc3irfXl%2BqIWf6K9oFjOvvBjdzfimWHlecd347bCjkso%2Fsx9p%2BH1stKcKi0dBF3wxsSHrhwm9Pl%2FyQpaWHFhZdKmMWxkuDPxPwDwdnGHusLKF7q917Abd10Rk55IKL%2FuLXi%2BZL0tCUY33%2BjLVi1v%2BgPF2NZr4%2FGOwUMXfbiXg64%2FhtjB%2FduArAtp7eKsLsZotZJAoyEx0elkNcGVVPbYj2qZHh8%2BNHJZHbI8Km4UCdtEg28dCiEzO7AFUNxuc3vLQ7plsCEkqXmUZJu4EoacjRXnNFSV66vu7Hi6H0rnT7JVN9CpRqZUYH36vmatWkswR6UwnaEvEiqaQKV9gP6HSnPtJXLS6WvdZwAzlTWOnw61V988TgVl1j02D6k6%2B0TaCfTpMBL%2BIMR8yFTXccqRIy0KZZng6ZnrKTbq5kZcjuWt4AXSTXafj35rhTU1Qb8%2BzhWQ4vrxj%2BUun8KHhC7aICC4WZ6vY7Rvy7u%2FlfiobxauEZ1UNLZXI5nz6df5yWg1Of0rn6O%2FIMYnc7%2BiQg%2B9DCQOw9Ari081myn5NnzPoS1COMOCf5rwGOqUBx9hsIyBcm6X3UuegHN9IM8sqb8fYxog39ZcHCJYy4Jm3PNpyNfjf8ZUuUlj8mUbisat6hVBDkrtZTdhmrtoCQN95l4iLDuQX8w%2FzpLKzt8P%2B4s92%2BVw2NN0EZ%2Ffmtccbxz5t%2FeHbxmw%2FsdPmTuQBkPe0drtNWLFi%2BCmZqqNbtyDxNC%2FqjOKXycwSaFgoe3vN7ALS%2BE8NaRzA5G4074MwiscZf%2F6%2F&X-Amz-Signature=d7d1e98c3ac73cbdddeed88cc4e5be0479df42254159d9da121d844ebf0bfc50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V6ZQZUV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDbX46j3ByqYmk%2BAY0PrmQCVgJ0VgWjt%2FxvJQMJw5SubgIgBK5jzHs85Q0NH%2BOR2vHqCoQxDOtPwfiTqLrWSzqqJQ0qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHMotIgdQjGVVHoICrcA7iHhmFD4TaNY2Dkq0lEvQTf%2F7N3D8XAPi5ZckpzWndZX9WQdh8Qkxuk%2BskUm%2FWOz2B%2FTmCRE%2FyuMu9Qc3irfXl%2BqIWf6K9oFjOvvBjdzfimWHlecd347bCjkso%2Fsx9p%2BH1stKcKi0dBF3wxsSHrhwm9Pl%2FyQpaWHFhZdKmMWxkuDPxPwDwdnGHusLKF7q917Abd10Rk55IKL%2FuLXi%2BZL0tCUY33%2BjLVi1v%2BgPF2NZr4%2FGOwUMXfbiXg64%2FhtjB%2FduArAtp7eKsLsZotZJAoyEx0elkNcGVVPbYj2qZHh8%2BNHJZHbI8Km4UCdtEg28dCiEzO7AFUNxuc3vLQ7plsCEkqXmUZJu4EoacjRXnNFSV66vu7Hi6H0rnT7JVN9CpRqZUYH36vmatWkswR6UwnaEvEiqaQKV9gP6HSnPtJXLS6WvdZwAzlTWOnw61V988TgVl1j02D6k6%2B0TaCfTpMBL%2BIMR8yFTXccqRIy0KZZng6ZnrKTbq5kZcjuWt4AXSTXafj35rhTU1Qb8%2BzhWQ4vrxj%2BUun8KHhC7aICC4WZ6vY7Rvy7u%2FlfiobxauEZ1UNLZXI5nz6df5yWg1Of0rn6O%2FIMYnc7%2BiQg%2B9DCQOw9Ari081myn5NnzPoS1COMOCf5rwGOqUBx9hsIyBcm6X3UuegHN9IM8sqb8fYxog39ZcHCJYy4Jm3PNpyNfjf8ZUuUlj8mUbisat6hVBDkrtZTdhmrtoCQN95l4iLDuQX8w%2FzpLKzt8P%2B4s92%2BVw2NN0EZ%2Ffmtccbxz5t%2FeHbxmw%2FsdPmTuQBkPe0drtNWLFi%2BCmZqqNbtyDxNC%2FqjOKXycwSaFgoe3vN7ALS%2BE8NaRzA5G4074MwiscZf%2F6%2F&X-Amz-Signature=53c4d3d79ba3af995aed6fffe8a62f852510c56411cbe07d91d042521b9a6884&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J5OYHAB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIDAMzkpLqllZYNEn%2BimSfiEJtPDOOYa5GJsDH0NADb00AiBArNnzVSvwXWo4WYbFC7kPNnPD2cTjK5tjSwb9lw%2FqGSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1qkCiGHZX6B2CtfuKtwDl0RGU5woQNI8CMBdPhxSTVyyK5avh%2FXeTYIAjpNhyr1g%2FIlJdDBjeHozpzqrnMlYGtqRjQCbWPqhTcmFbe84WEaFpnF41KxIPdNr8YZUTG%2BjCDMfnyqXiYnuhxBOtgTuoIQ1Q%2Fyig5ECH%2BlmPO4rJlFvyc4%2BcXuwE%2FfwRUDbSyAZ%2B3hucjgLhzK12nRgoPdmRCPWuqZVZwn7OHNq5Vy5fTY%2FWSDqewUCAFQcJXMlSsOJqI6CdEX39r6PbVAD7%2BJD0zJKCRrfxyUjTMjL7JLjz99LjYYoHvVYypD%2BwvjrqvLATFOgp6ygu4WAO%2F%2BEyKOfm17ijE1wqZ5ilp%2FlsP%2BhmSwtQFDVFo%2FTefdus87n0DZv1iTnSOh7o3K31lMkJxZmFu0QvnBi6S585QUEluaYwcJtL5u6YO3M8%2F93YBc004B6f5VdyVM6EANiRCsA4LLzae%2BhCVgB3TBwKIesPFxk1Wuo7E%2B813%2B1CgaM0ieRQbi2oHhA9YIsRZalGVkLfgCCd%2FWML7A9dhhp2vKJtfQlT%2BWiTXce0V7Qtp1P33%2F6CRDPlDicNgRy200DkcP0q27H%2BrJN%2BlbeBvpso1FHfSsxFTRbOQjTQ2mGMvaaHOUo8u2aQeaLXVHUoziOfHww07rmvAY6pgFk704XA2o66dElqbU7raN7HI9aNLr6pEtx0%2F1cVWe17qtT5dyE88wfzB5Tlio%2BV6R63Ag2TedxfSjPAN2nOTuHLgFkFD2c%2BpaTZUdV9COHSr3LN9Oxrz1vOvPdYnxkQGuLJpl2aVRGpD1yssNTxZZPDkuy9ZKGBgMW447XGW7pEvD09w4FhoTOH%2Foixnl71iPravKdPm643Kd%2Ftg9ndUjdaRrA9daW&X-Amz-Signature=ac26ca34543f853b84c1b6fe53ed084954e8d0663452409ffc90353e5e99923f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J5OYHAB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIDAMzkpLqllZYNEn%2BimSfiEJtPDOOYa5GJsDH0NADb00AiBArNnzVSvwXWo4WYbFC7kPNnPD2cTjK5tjSwb9lw%2FqGSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1qkCiGHZX6B2CtfuKtwDl0RGU5woQNI8CMBdPhxSTVyyK5avh%2FXeTYIAjpNhyr1g%2FIlJdDBjeHozpzqrnMlYGtqRjQCbWPqhTcmFbe84WEaFpnF41KxIPdNr8YZUTG%2BjCDMfnyqXiYnuhxBOtgTuoIQ1Q%2Fyig5ECH%2BlmPO4rJlFvyc4%2BcXuwE%2FfwRUDbSyAZ%2B3hucjgLhzK12nRgoPdmRCPWuqZVZwn7OHNq5Vy5fTY%2FWSDqewUCAFQcJXMlSsOJqI6CdEX39r6PbVAD7%2BJD0zJKCRrfxyUjTMjL7JLjz99LjYYoHvVYypD%2BwvjrqvLATFOgp6ygu4WAO%2F%2BEyKOfm17ijE1wqZ5ilp%2FlsP%2BhmSwtQFDVFo%2FTefdus87n0DZv1iTnSOh7o3K31lMkJxZmFu0QvnBi6S585QUEluaYwcJtL5u6YO3M8%2F93YBc004B6f5VdyVM6EANiRCsA4LLzae%2BhCVgB3TBwKIesPFxk1Wuo7E%2B813%2B1CgaM0ieRQbi2oHhA9YIsRZalGVkLfgCCd%2FWML7A9dhhp2vKJtfQlT%2BWiTXce0V7Qtp1P33%2F6CRDPlDicNgRy200DkcP0q27H%2BrJN%2BlbeBvpso1FHfSsxFTRbOQjTQ2mGMvaaHOUo8u2aQeaLXVHUoziOfHww07rmvAY6pgFk704XA2o66dElqbU7raN7HI9aNLr6pEtx0%2F1cVWe17qtT5dyE88wfzB5Tlio%2BV6R63Ag2TedxfSjPAN2nOTuHLgFkFD2c%2BpaTZUdV9COHSr3LN9Oxrz1vOvPdYnxkQGuLJpl2aVRGpD1yssNTxZZPDkuy9ZKGBgMW447XGW7pEvD09w4FhoTOH%2Foixnl71iPravKdPm643Kd%2Ftg9ndUjdaRrA9daW&X-Amz-Signature=b4994391458a6f4c7494cf9959c47fe1e26830c826f2f7598f8392176f75fc33&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
