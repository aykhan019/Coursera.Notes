

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WC3DCUEH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIBCBlj3VXji6wDrm%2BVqmZQ5BBt1Toy1hwNkqUcAITQ6KAiEA1Ji8wGWZF%2FbB4Z7yBhT2XjSZpZTujUiPVEMVgo7skc0qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPoRu%2FWySJiat6PNOSrcAys%2Fp4iyyBznuyLX7FZP7qcr3GWIt46bWHfbA80Tznel6Y%2BlgzDrWULTyxPOLualXs%2FGqwXPgbhMxnRRZJSviRNYApLYyo1%2FpAssvCvE6zRMojIlbP0ENGMuwznKVqG7yxNJtq6CNXtJ8QKCMIvEg0gKV%2FfWZsemuNMrug%2B6kIb9KfQKuZ7frlnLvdR75ubLFZiFHqB1%2F70fsXv%2BscQgmpf%2B2ErZBPuJem78OPvDYSCyF0vLqSALGAfnxOjHC1P%2BXuOFHGSC%2BxPxGHgKrlUwjd63e3EYcyVcgNIQCyf7nlEtQdtDmZfzTqS2jRoSRsjOEhDHxNaLTHOCRMJWPY5r1PGbK0B1TMFdzO1IvauIesmInpVDavCx8MlM0QqqgZwcDbSfqW59qmakgVjct%2BYxLwo2ad87swwq%2FznLkiqymSpWAP2zSonC8rhtJWOPtCnGW9wN7VA%2BJoiz84%2Fv4YfKj90rETzDv5ZDRI0PzmKn5HyAdVxobaq9o12qhwhKCGqTZe1QpInNtjyKwi80%2FBa3kJcKj26XrFQJXx06kvPReH3c5XqjHzcdk2fUkqaVWTlCMHXdJaD7HBG4emkHeqrwQgBCvul3SK8JNM%2FzWmb%2F16qb4sAb9R8%2BHXZy2JC0MMu65rwGOqUBz32b8x48%2BvGyi8wyfHoViIZXF2gyjRwfReqvX%2BzaTYCGalyI5uKHqiXLgKF7e3bFM0SSTw1XZp0AKMgc3nBErsJC5EOvi8B%2BnjBnrDE8%2BhodqQFMMRnh9uksUWqWh9gE2hkEkGGL9T2mTHMQroae%2BuHxJmN1B1JQPj2Nh81Rrghg94cfW3cMvZdTGfwvp%2Fmsia00QgUZC7oWvakKGaBBONTWaSYO&X-Amz-Signature=3a1c291b196558c75adc8352c89b4db69fa2ab0c26e7e7c29eb48a7119eb1b5d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WC3DCUEH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIBCBlj3VXji6wDrm%2BVqmZQ5BBt1Toy1hwNkqUcAITQ6KAiEA1Ji8wGWZF%2FbB4Z7yBhT2XjSZpZTujUiPVEMVgo7skc0qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPoRu%2FWySJiat6PNOSrcAys%2Fp4iyyBznuyLX7FZP7qcr3GWIt46bWHfbA80Tznel6Y%2BlgzDrWULTyxPOLualXs%2FGqwXPgbhMxnRRZJSviRNYApLYyo1%2FpAssvCvE6zRMojIlbP0ENGMuwznKVqG7yxNJtq6CNXtJ8QKCMIvEg0gKV%2FfWZsemuNMrug%2B6kIb9KfQKuZ7frlnLvdR75ubLFZiFHqB1%2F70fsXv%2BscQgmpf%2B2ErZBPuJem78OPvDYSCyF0vLqSALGAfnxOjHC1P%2BXuOFHGSC%2BxPxGHgKrlUwjd63e3EYcyVcgNIQCyf7nlEtQdtDmZfzTqS2jRoSRsjOEhDHxNaLTHOCRMJWPY5r1PGbK0B1TMFdzO1IvauIesmInpVDavCx8MlM0QqqgZwcDbSfqW59qmakgVjct%2BYxLwo2ad87swwq%2FznLkiqymSpWAP2zSonC8rhtJWOPtCnGW9wN7VA%2BJoiz84%2Fv4YfKj90rETzDv5ZDRI0PzmKn5HyAdVxobaq9o12qhwhKCGqTZe1QpInNtjyKwi80%2FBa3kJcKj26XrFQJXx06kvPReH3c5XqjHzcdk2fUkqaVWTlCMHXdJaD7HBG4emkHeqrwQgBCvul3SK8JNM%2FzWmb%2F16qb4sAb9R8%2BHXZy2JC0MMu65rwGOqUBz32b8x48%2BvGyi8wyfHoViIZXF2gyjRwfReqvX%2BzaTYCGalyI5uKHqiXLgKF7e3bFM0SSTw1XZp0AKMgc3nBErsJC5EOvi8B%2BnjBnrDE8%2BhodqQFMMRnh9uksUWqWh9gE2hkEkGGL9T2mTHMQroae%2BuHxJmN1B1JQPj2Nh81Rrghg94cfW3cMvZdTGfwvp%2Fmsia00QgUZC7oWvakKGaBBONTWaSYO&X-Amz-Signature=78d1d666cdc50f056e55071918e48d6e827baa1b548a1db5b366dcd841006403&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WC3DCUEH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIBCBlj3VXji6wDrm%2BVqmZQ5BBt1Toy1hwNkqUcAITQ6KAiEA1Ji8wGWZF%2FbB4Z7yBhT2XjSZpZTujUiPVEMVgo7skc0qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPoRu%2FWySJiat6PNOSrcAys%2Fp4iyyBznuyLX7FZP7qcr3GWIt46bWHfbA80Tznel6Y%2BlgzDrWULTyxPOLualXs%2FGqwXPgbhMxnRRZJSviRNYApLYyo1%2FpAssvCvE6zRMojIlbP0ENGMuwznKVqG7yxNJtq6CNXtJ8QKCMIvEg0gKV%2FfWZsemuNMrug%2B6kIb9KfQKuZ7frlnLvdR75ubLFZiFHqB1%2F70fsXv%2BscQgmpf%2B2ErZBPuJem78OPvDYSCyF0vLqSALGAfnxOjHC1P%2BXuOFHGSC%2BxPxGHgKrlUwjd63e3EYcyVcgNIQCyf7nlEtQdtDmZfzTqS2jRoSRsjOEhDHxNaLTHOCRMJWPY5r1PGbK0B1TMFdzO1IvauIesmInpVDavCx8MlM0QqqgZwcDbSfqW59qmakgVjct%2BYxLwo2ad87swwq%2FznLkiqymSpWAP2zSonC8rhtJWOPtCnGW9wN7VA%2BJoiz84%2Fv4YfKj90rETzDv5ZDRI0PzmKn5HyAdVxobaq9o12qhwhKCGqTZe1QpInNtjyKwi80%2FBa3kJcKj26XrFQJXx06kvPReH3c5XqjHzcdk2fUkqaVWTlCMHXdJaD7HBG4emkHeqrwQgBCvul3SK8JNM%2FzWmb%2F16qb4sAb9R8%2BHXZy2JC0MMu65rwGOqUBz32b8x48%2BvGyi8wyfHoViIZXF2gyjRwfReqvX%2BzaTYCGalyI5uKHqiXLgKF7e3bFM0SSTw1XZp0AKMgc3nBErsJC5EOvi8B%2BnjBnrDE8%2BhodqQFMMRnh9uksUWqWh9gE2hkEkGGL9T2mTHMQroae%2BuHxJmN1B1JQPj2Nh81Rrghg94cfW3cMvZdTGfwvp%2Fmsia00QgUZC7oWvakKGaBBONTWaSYO&X-Amz-Signature=a15b9cee6e8c3e2991420d4151120bf44b1f0479d0499079037bf0f8a80c7914&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WC3DCUEH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIBCBlj3VXji6wDrm%2BVqmZQ5BBt1Toy1hwNkqUcAITQ6KAiEA1Ji8wGWZF%2FbB4Z7yBhT2XjSZpZTujUiPVEMVgo7skc0qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPoRu%2FWySJiat6PNOSrcAys%2Fp4iyyBznuyLX7FZP7qcr3GWIt46bWHfbA80Tznel6Y%2BlgzDrWULTyxPOLualXs%2FGqwXPgbhMxnRRZJSviRNYApLYyo1%2FpAssvCvE6zRMojIlbP0ENGMuwznKVqG7yxNJtq6CNXtJ8QKCMIvEg0gKV%2FfWZsemuNMrug%2B6kIb9KfQKuZ7frlnLvdR75ubLFZiFHqB1%2F70fsXv%2BscQgmpf%2B2ErZBPuJem78OPvDYSCyF0vLqSALGAfnxOjHC1P%2BXuOFHGSC%2BxPxGHgKrlUwjd63e3EYcyVcgNIQCyf7nlEtQdtDmZfzTqS2jRoSRsjOEhDHxNaLTHOCRMJWPY5r1PGbK0B1TMFdzO1IvauIesmInpVDavCx8MlM0QqqgZwcDbSfqW59qmakgVjct%2BYxLwo2ad87swwq%2FznLkiqymSpWAP2zSonC8rhtJWOPtCnGW9wN7VA%2BJoiz84%2Fv4YfKj90rETzDv5ZDRI0PzmKn5HyAdVxobaq9o12qhwhKCGqTZe1QpInNtjyKwi80%2FBa3kJcKj26XrFQJXx06kvPReH3c5XqjHzcdk2fUkqaVWTlCMHXdJaD7HBG4emkHeqrwQgBCvul3SK8JNM%2FzWmb%2F16qb4sAb9R8%2BHXZy2JC0MMu65rwGOqUBz32b8x48%2BvGyi8wyfHoViIZXF2gyjRwfReqvX%2BzaTYCGalyI5uKHqiXLgKF7e3bFM0SSTw1XZp0AKMgc3nBErsJC5EOvi8B%2BnjBnrDE8%2BhodqQFMMRnh9uksUWqWh9gE2hkEkGGL9T2mTHMQroae%2BuHxJmN1B1JQPj2Nh81Rrghg94cfW3cMvZdTGfwvp%2Fmsia00QgUZC7oWvakKGaBBONTWaSYO&X-Amz-Signature=de7a79d561c8b927611d7f43fc360ac5e8f420a6f3b9332ee397053b9153a587&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WC3DCUEH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIBCBlj3VXji6wDrm%2BVqmZQ5BBt1Toy1hwNkqUcAITQ6KAiEA1Ji8wGWZF%2FbB4Z7yBhT2XjSZpZTujUiPVEMVgo7skc0qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPoRu%2FWySJiat6PNOSrcAys%2Fp4iyyBznuyLX7FZP7qcr3GWIt46bWHfbA80Tznel6Y%2BlgzDrWULTyxPOLualXs%2FGqwXPgbhMxnRRZJSviRNYApLYyo1%2FpAssvCvE6zRMojIlbP0ENGMuwznKVqG7yxNJtq6CNXtJ8QKCMIvEg0gKV%2FfWZsemuNMrug%2B6kIb9KfQKuZ7frlnLvdR75ubLFZiFHqB1%2F70fsXv%2BscQgmpf%2B2ErZBPuJem78OPvDYSCyF0vLqSALGAfnxOjHC1P%2BXuOFHGSC%2BxPxGHgKrlUwjd63e3EYcyVcgNIQCyf7nlEtQdtDmZfzTqS2jRoSRsjOEhDHxNaLTHOCRMJWPY5r1PGbK0B1TMFdzO1IvauIesmInpVDavCx8MlM0QqqgZwcDbSfqW59qmakgVjct%2BYxLwo2ad87swwq%2FznLkiqymSpWAP2zSonC8rhtJWOPtCnGW9wN7VA%2BJoiz84%2Fv4YfKj90rETzDv5ZDRI0PzmKn5HyAdVxobaq9o12qhwhKCGqTZe1QpInNtjyKwi80%2FBa3kJcKj26XrFQJXx06kvPReH3c5XqjHzcdk2fUkqaVWTlCMHXdJaD7HBG4emkHeqrwQgBCvul3SK8JNM%2FzWmb%2F16qb4sAb9R8%2BHXZy2JC0MMu65rwGOqUBz32b8x48%2BvGyi8wyfHoViIZXF2gyjRwfReqvX%2BzaTYCGalyI5uKHqiXLgKF7e3bFM0SSTw1XZp0AKMgc3nBErsJC5EOvi8B%2BnjBnrDE8%2BhodqQFMMRnh9uksUWqWh9gE2hkEkGGL9T2mTHMQroae%2BuHxJmN1B1JQPj2Nh81Rrghg94cfW3cMvZdTGfwvp%2Fmsia00QgUZC7oWvakKGaBBONTWaSYO&X-Amz-Signature=5ae30d338b3d44edff3535246a60563ffdc67fb02e7326f0894a5a5f650d8ec4&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WC3DCUEH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIBCBlj3VXji6wDrm%2BVqmZQ5BBt1Toy1hwNkqUcAITQ6KAiEA1Ji8wGWZF%2FbB4Z7yBhT2XjSZpZTujUiPVEMVgo7skc0qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPoRu%2FWySJiat6PNOSrcAys%2Fp4iyyBznuyLX7FZP7qcr3GWIt46bWHfbA80Tznel6Y%2BlgzDrWULTyxPOLualXs%2FGqwXPgbhMxnRRZJSviRNYApLYyo1%2FpAssvCvE6zRMojIlbP0ENGMuwznKVqG7yxNJtq6CNXtJ8QKCMIvEg0gKV%2FfWZsemuNMrug%2B6kIb9KfQKuZ7frlnLvdR75ubLFZiFHqB1%2F70fsXv%2BscQgmpf%2B2ErZBPuJem78OPvDYSCyF0vLqSALGAfnxOjHC1P%2BXuOFHGSC%2BxPxGHgKrlUwjd63e3EYcyVcgNIQCyf7nlEtQdtDmZfzTqS2jRoSRsjOEhDHxNaLTHOCRMJWPY5r1PGbK0B1TMFdzO1IvauIesmInpVDavCx8MlM0QqqgZwcDbSfqW59qmakgVjct%2BYxLwo2ad87swwq%2FznLkiqymSpWAP2zSonC8rhtJWOPtCnGW9wN7VA%2BJoiz84%2Fv4YfKj90rETzDv5ZDRI0PzmKn5HyAdVxobaq9o12qhwhKCGqTZe1QpInNtjyKwi80%2FBa3kJcKj26XrFQJXx06kvPReH3c5XqjHzcdk2fUkqaVWTlCMHXdJaD7HBG4emkHeqrwQgBCvul3SK8JNM%2FzWmb%2F16qb4sAb9R8%2BHXZy2JC0MMu65rwGOqUBz32b8x48%2BvGyi8wyfHoViIZXF2gyjRwfReqvX%2BzaTYCGalyI5uKHqiXLgKF7e3bFM0SSTw1XZp0AKMgc3nBErsJC5EOvi8B%2BnjBnrDE8%2BhodqQFMMRnh9uksUWqWh9gE2hkEkGGL9T2mTHMQroae%2BuHxJmN1B1JQPj2Nh81Rrghg94cfW3cMvZdTGfwvp%2Fmsia00QgUZC7oWvakKGaBBONTWaSYO&X-Amz-Signature=2b9f98761030ea2912029bec18e6396e0e7eb43eaa29fe3384e01e83979c8575&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WC3DCUEH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIBCBlj3VXji6wDrm%2BVqmZQ5BBt1Toy1hwNkqUcAITQ6KAiEA1Ji8wGWZF%2FbB4Z7yBhT2XjSZpZTujUiPVEMVgo7skc0qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPoRu%2FWySJiat6PNOSrcAys%2Fp4iyyBznuyLX7FZP7qcr3GWIt46bWHfbA80Tznel6Y%2BlgzDrWULTyxPOLualXs%2FGqwXPgbhMxnRRZJSviRNYApLYyo1%2FpAssvCvE6zRMojIlbP0ENGMuwznKVqG7yxNJtq6CNXtJ8QKCMIvEg0gKV%2FfWZsemuNMrug%2B6kIb9KfQKuZ7frlnLvdR75ubLFZiFHqB1%2F70fsXv%2BscQgmpf%2B2ErZBPuJem78OPvDYSCyF0vLqSALGAfnxOjHC1P%2BXuOFHGSC%2BxPxGHgKrlUwjd63e3EYcyVcgNIQCyf7nlEtQdtDmZfzTqS2jRoSRsjOEhDHxNaLTHOCRMJWPY5r1PGbK0B1TMFdzO1IvauIesmInpVDavCx8MlM0QqqgZwcDbSfqW59qmakgVjct%2BYxLwo2ad87swwq%2FznLkiqymSpWAP2zSonC8rhtJWOPtCnGW9wN7VA%2BJoiz84%2Fv4YfKj90rETzDv5ZDRI0PzmKn5HyAdVxobaq9o12qhwhKCGqTZe1QpInNtjyKwi80%2FBa3kJcKj26XrFQJXx06kvPReH3c5XqjHzcdk2fUkqaVWTlCMHXdJaD7HBG4emkHeqrwQgBCvul3SK8JNM%2FzWmb%2F16qb4sAb9R8%2BHXZy2JC0MMu65rwGOqUBz32b8x48%2BvGyi8wyfHoViIZXF2gyjRwfReqvX%2BzaTYCGalyI5uKHqiXLgKF7e3bFM0SSTw1XZp0AKMgc3nBErsJC5EOvi8B%2BnjBnrDE8%2BhodqQFMMRnh9uksUWqWh9gE2hkEkGGL9T2mTHMQroae%2BuHxJmN1B1JQPj2Nh81Rrghg94cfW3cMvZdTGfwvp%2Fmsia00QgUZC7oWvakKGaBBONTWaSYO&X-Amz-Signature=a1f4a4e3a5e141e29da0be582dc85facf5fa6e36ba0677a96ed2a49ccfdef442&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WC3DCUEH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIBCBlj3VXji6wDrm%2BVqmZQ5BBt1Toy1hwNkqUcAITQ6KAiEA1Ji8wGWZF%2FbB4Z7yBhT2XjSZpZTujUiPVEMVgo7skc0qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPoRu%2FWySJiat6PNOSrcAys%2Fp4iyyBznuyLX7FZP7qcr3GWIt46bWHfbA80Tznel6Y%2BlgzDrWULTyxPOLualXs%2FGqwXPgbhMxnRRZJSviRNYApLYyo1%2FpAssvCvE6zRMojIlbP0ENGMuwznKVqG7yxNJtq6CNXtJ8QKCMIvEg0gKV%2FfWZsemuNMrug%2B6kIb9KfQKuZ7frlnLvdR75ubLFZiFHqB1%2F70fsXv%2BscQgmpf%2B2ErZBPuJem78OPvDYSCyF0vLqSALGAfnxOjHC1P%2BXuOFHGSC%2BxPxGHgKrlUwjd63e3EYcyVcgNIQCyf7nlEtQdtDmZfzTqS2jRoSRsjOEhDHxNaLTHOCRMJWPY5r1PGbK0B1TMFdzO1IvauIesmInpVDavCx8MlM0QqqgZwcDbSfqW59qmakgVjct%2BYxLwo2ad87swwq%2FznLkiqymSpWAP2zSonC8rhtJWOPtCnGW9wN7VA%2BJoiz84%2Fv4YfKj90rETzDv5ZDRI0PzmKn5HyAdVxobaq9o12qhwhKCGqTZe1QpInNtjyKwi80%2FBa3kJcKj26XrFQJXx06kvPReH3c5XqjHzcdk2fUkqaVWTlCMHXdJaD7HBG4emkHeqrwQgBCvul3SK8JNM%2FzWmb%2F16qb4sAb9R8%2BHXZy2JC0MMu65rwGOqUBz32b8x48%2BvGyi8wyfHoViIZXF2gyjRwfReqvX%2BzaTYCGalyI5uKHqiXLgKF7e3bFM0SSTw1XZp0AKMgc3nBErsJC5EOvi8B%2BnjBnrDE8%2BhodqQFMMRnh9uksUWqWh9gE2hkEkGGL9T2mTHMQroae%2BuHxJmN1B1JQPj2Nh81Rrghg94cfW3cMvZdTGfwvp%2Fmsia00QgUZC7oWvakKGaBBONTWaSYO&X-Amz-Signature=7dc2651a9a52f9f7423f40653c6cfc1d4c2e819647e489af24635e566fc09e63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WC3DCUEH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIBCBlj3VXji6wDrm%2BVqmZQ5BBt1Toy1hwNkqUcAITQ6KAiEA1Ji8wGWZF%2FbB4Z7yBhT2XjSZpZTujUiPVEMVgo7skc0qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPoRu%2FWySJiat6PNOSrcAys%2Fp4iyyBznuyLX7FZP7qcr3GWIt46bWHfbA80Tznel6Y%2BlgzDrWULTyxPOLualXs%2FGqwXPgbhMxnRRZJSviRNYApLYyo1%2FpAssvCvE6zRMojIlbP0ENGMuwznKVqG7yxNJtq6CNXtJ8QKCMIvEg0gKV%2FfWZsemuNMrug%2B6kIb9KfQKuZ7frlnLvdR75ubLFZiFHqB1%2F70fsXv%2BscQgmpf%2B2ErZBPuJem78OPvDYSCyF0vLqSALGAfnxOjHC1P%2BXuOFHGSC%2BxPxGHgKrlUwjd63e3EYcyVcgNIQCyf7nlEtQdtDmZfzTqS2jRoSRsjOEhDHxNaLTHOCRMJWPY5r1PGbK0B1TMFdzO1IvauIesmInpVDavCx8MlM0QqqgZwcDbSfqW59qmakgVjct%2BYxLwo2ad87swwq%2FznLkiqymSpWAP2zSonC8rhtJWOPtCnGW9wN7VA%2BJoiz84%2Fv4YfKj90rETzDv5ZDRI0PzmKn5HyAdVxobaq9o12qhwhKCGqTZe1QpInNtjyKwi80%2FBa3kJcKj26XrFQJXx06kvPReH3c5XqjHzcdk2fUkqaVWTlCMHXdJaD7HBG4emkHeqrwQgBCvul3SK8JNM%2FzWmb%2F16qb4sAb9R8%2BHXZy2JC0MMu65rwGOqUBz32b8x48%2BvGyi8wyfHoViIZXF2gyjRwfReqvX%2BzaTYCGalyI5uKHqiXLgKF7e3bFM0SSTw1XZp0AKMgc3nBErsJC5EOvi8B%2BnjBnrDE8%2BhodqQFMMRnh9uksUWqWh9gE2hkEkGGL9T2mTHMQroae%2BuHxJmN1B1JQPj2Nh81Rrghg94cfW3cMvZdTGfwvp%2Fmsia00QgUZC7oWvakKGaBBONTWaSYO&X-Amz-Signature=a7e6badad402eddb7dae01d6080546e04cbac671199cccf9a9ee39371bfa2021&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXGPTGZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHLfhMnYu0VlVFN%2FOnsUGArUjkKuXypUD%2FRo9u%2F2Mv%2FKAiEAqmIvhelbjsEQU4mUHMnNTxMkEKJQuS%2FprJUHdDnDwy8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDYnHB38OB2ZAsKimSrcA1OeqShDitO2N%2BAk2yxpzU5Zi5BjyhWwgX9Lp3%2FmjCjEUXdLxcsLkNUgdNjDE%2BjGIL%2F3jOlfN9NqxVtdWAyTHEKzilwiVhU2XiU3p6H2K54%2Fp7c3rK%2BC5JIHh%2B8nOntg3ojTD6vRBcD6UvR8GsrsV4YoVfWRdY40AavEFxVluCUMG21Y%2Bi1jQBex510jPZHwvjlbkt7E3xRHXVITbiVLBoCPWHBDqr4%2Fyd1BXsRBykMBgHdtieVjd7Hddvt6dJnHXNRyLNRUx9i9aGuDEy8hO1C8PuAPKPGEqHdQwbGaPxMTUBX9n0on4ekcLjAp%2B2yEBF27lm9Oz3Yy8nwNsFLgM8GDfp6Po5pPNqGEpFTWjnaO5sCbQwie%2Fxlyq%2Fz8S38ph2i2U%2FEQ9%2BUEeaGXXEeHTbP6uGObr8l61FtTHnGBBjq0A0E665kqmtA44erxCEnaF4zVJ%2FXb52KiS%2FlZB4LGH1LP73JTUkwUquB4wAD3jRRTAL3LoDVTVD3xaZe6sXeUavDLuyGkVvxO63T8gtO2WA8OVT66ch7NIucNm1trmcaf79RZr88pGfZDMFH%2BwHtgEFWfxo04Uh0qpQNfGSjuwOpXnDVEsWmmKsK%2FHskWNBzZKZKRlw8%2B92sUxlxeMP265rwGOqUBY6i%2BujfVUjFNr4PQKtRq0nX56ru4Hwr9mkGJZ7dySSjLIkxnuipUdqUCD%2FoXWZIjLKHln6UK18nQ55IUnM6o5Ixio3D3vWdCQo1t2tsZDD9Pb7M3AObpBUqoSHIzIwaQhZm0rwpSXQgyfs6jTxgea1dgBhEYti%2Buu8Zuq35X2d%2BGrlU3Y5sQyaHK8Uywr6lmf8vqzh8IkTjYdDX1K2xi3WUzg70f&X-Amz-Signature=e44baf8ae67936bdb552977094ba9b0548321333ecc0162d8c6717db8da188ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXGPTGZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHLfhMnYu0VlVFN%2FOnsUGArUjkKuXypUD%2FRo9u%2F2Mv%2FKAiEAqmIvhelbjsEQU4mUHMnNTxMkEKJQuS%2FprJUHdDnDwy8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDYnHB38OB2ZAsKimSrcA1OeqShDitO2N%2BAk2yxpzU5Zi5BjyhWwgX9Lp3%2FmjCjEUXdLxcsLkNUgdNjDE%2BjGIL%2F3jOlfN9NqxVtdWAyTHEKzilwiVhU2XiU3p6H2K54%2Fp7c3rK%2BC5JIHh%2B8nOntg3ojTD6vRBcD6UvR8GsrsV4YoVfWRdY40AavEFxVluCUMG21Y%2Bi1jQBex510jPZHwvjlbkt7E3xRHXVITbiVLBoCPWHBDqr4%2Fyd1BXsRBykMBgHdtieVjd7Hddvt6dJnHXNRyLNRUx9i9aGuDEy8hO1C8PuAPKPGEqHdQwbGaPxMTUBX9n0on4ekcLjAp%2B2yEBF27lm9Oz3Yy8nwNsFLgM8GDfp6Po5pPNqGEpFTWjnaO5sCbQwie%2Fxlyq%2Fz8S38ph2i2U%2FEQ9%2BUEeaGXXEeHTbP6uGObr8l61FtTHnGBBjq0A0E665kqmtA44erxCEnaF4zVJ%2FXb52KiS%2FlZB4LGH1LP73JTUkwUquB4wAD3jRRTAL3LoDVTVD3xaZe6sXeUavDLuyGkVvxO63T8gtO2WA8OVT66ch7NIucNm1trmcaf79RZr88pGfZDMFH%2BwHtgEFWfxo04Uh0qpQNfGSjuwOpXnDVEsWmmKsK%2FHskWNBzZKZKRlw8%2B92sUxlxeMP265rwGOqUBY6i%2BujfVUjFNr4PQKtRq0nX56ru4Hwr9mkGJZ7dySSjLIkxnuipUdqUCD%2FoXWZIjLKHln6UK18nQ55IUnM6o5Ixio3D3vWdCQo1t2tsZDD9Pb7M3AObpBUqoSHIzIwaQhZm0rwpSXQgyfs6jTxgea1dgBhEYti%2Buu8Zuq35X2d%2BGrlU3Y5sQyaHK8Uywr6lmf8vqzh8IkTjYdDX1K2xi3WUzg70f&X-Amz-Signature=c7e6c0ca4647d7e764bf06134311a52a2c981a1a94636654d85b231f5636d024&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
