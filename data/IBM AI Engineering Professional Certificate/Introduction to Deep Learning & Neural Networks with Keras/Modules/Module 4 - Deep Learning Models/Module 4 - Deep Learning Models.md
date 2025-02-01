

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGLNREC4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTZtGjOzU%2BGX0jv1qXd0J45XRSNiPY7fxYQXcb1AP7uAIgPg3RprP7XJHw9QJ2RKylw37xBa7mzr%2BEfqNkL5BJmGYqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNxTmienIWE5NZRKBCrcA5sOdFAmHZakHWnTbLTixsQ0fTS3NoueZQThfYxUd32bR%2FLiXusG2nidLf%2Fai2gPbsH6%2FmpdXtubkOfYLqZFOyFsrchjiAEUAwwHLzYKF7091eyXFVZ878iGTLdSHgeDBL5WoYZkzoxsxOfNKH1oVVD4NWD6WMSoHtRzHR7jKBrF%2Bn8bGVNcKY6ar6KHV8bXAZQFh0RhO%2F32xTSRW%2FWKSahJDx5cua5TBfjyI95Z8JN9HqR3CWrZ%2Bt9UOsMjP291PaEn5zuFrFudqlZL2GPG6HGQydz2QPii1XOlP5l5ZpcC7H25pEMIISxqg2V6chQ33X%2BlFzTIlzKFJvEWTn2KAQZppKsYdo8jI6VNTR0PzXC53Bd1stZSu3oy9XEkcZJewu2INcPZKmstxmHUsy9P4oa7xtJOAuBJQAV3Sf23uAnVWetqVd2%2BCJQpn5nn%2FFQ8ErFPYDR5211Pu%2BoBZBfaS%2FHyxAktw1bkGxLUdiWfVJRwqEMCswHYJN5COhZH8FW1JCoWbY8GWroeWk1VpmI2ge7KV%2Bnwoor4SnZ0r3OzERhlTFpNnuIp2OlSt02laZveyonrlFPTP%2F%2Fmum83Kiev%2FY%2FjTXHFNSO1Ci5gOJuXJNKszzWenb2JBcthd9UNMJvN9bwGOqUBsjYo3RTQg5KxYT39vy5DHpkAY5WSqf3pNWeZX3vpihh%2B0TFm6p6%2FsOAj8swRse%2B2X2fShvjG%2BbSjLHlJxCBuScsJeMzYVvPBKvsa2lTBtxr3CrdcRNtSaIqRWY1KtQSrAv1WMpXo%2FamoiOb5xfF8VSEFLWg20RDHS0bwcKKP8RuC7RYW6X6A25eQ2wVD75tZmziZJ2uoyU8oA4DeMaWcp25odjEq&X-Amz-Signature=1d69d452dcf5465299a830bb905c93dbc60a5723d134696165f7c0dfa7ab2b51&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGLNREC4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTZtGjOzU%2BGX0jv1qXd0J45XRSNiPY7fxYQXcb1AP7uAIgPg3RprP7XJHw9QJ2RKylw37xBa7mzr%2BEfqNkL5BJmGYqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNxTmienIWE5NZRKBCrcA5sOdFAmHZakHWnTbLTixsQ0fTS3NoueZQThfYxUd32bR%2FLiXusG2nidLf%2Fai2gPbsH6%2FmpdXtubkOfYLqZFOyFsrchjiAEUAwwHLzYKF7091eyXFVZ878iGTLdSHgeDBL5WoYZkzoxsxOfNKH1oVVD4NWD6WMSoHtRzHR7jKBrF%2Bn8bGVNcKY6ar6KHV8bXAZQFh0RhO%2F32xTSRW%2FWKSahJDx5cua5TBfjyI95Z8JN9HqR3CWrZ%2Bt9UOsMjP291PaEn5zuFrFudqlZL2GPG6HGQydz2QPii1XOlP5l5ZpcC7H25pEMIISxqg2V6chQ33X%2BlFzTIlzKFJvEWTn2KAQZppKsYdo8jI6VNTR0PzXC53Bd1stZSu3oy9XEkcZJewu2INcPZKmstxmHUsy9P4oa7xtJOAuBJQAV3Sf23uAnVWetqVd2%2BCJQpn5nn%2FFQ8ErFPYDR5211Pu%2BoBZBfaS%2FHyxAktw1bkGxLUdiWfVJRwqEMCswHYJN5COhZH8FW1JCoWbY8GWroeWk1VpmI2ge7KV%2Bnwoor4SnZ0r3OzERhlTFpNnuIp2OlSt02laZveyonrlFPTP%2F%2Fmum83Kiev%2FY%2FjTXHFNSO1Ci5gOJuXJNKszzWenb2JBcthd9UNMJvN9bwGOqUBsjYo3RTQg5KxYT39vy5DHpkAY5WSqf3pNWeZX3vpihh%2B0TFm6p6%2FsOAj8swRse%2B2X2fShvjG%2BbSjLHlJxCBuScsJeMzYVvPBKvsa2lTBtxr3CrdcRNtSaIqRWY1KtQSrAv1WMpXo%2FamoiOb5xfF8VSEFLWg20RDHS0bwcKKP8RuC7RYW6X6A25eQ2wVD75tZmziZJ2uoyU8oA4DeMaWcp25odjEq&X-Amz-Signature=63a98ff2e502d8b78819816258cb3a9a93221c7c2ff6c0018c92236527670497&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGLNREC4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTZtGjOzU%2BGX0jv1qXd0J45XRSNiPY7fxYQXcb1AP7uAIgPg3RprP7XJHw9QJ2RKylw37xBa7mzr%2BEfqNkL5BJmGYqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNxTmienIWE5NZRKBCrcA5sOdFAmHZakHWnTbLTixsQ0fTS3NoueZQThfYxUd32bR%2FLiXusG2nidLf%2Fai2gPbsH6%2FmpdXtubkOfYLqZFOyFsrchjiAEUAwwHLzYKF7091eyXFVZ878iGTLdSHgeDBL5WoYZkzoxsxOfNKH1oVVD4NWD6WMSoHtRzHR7jKBrF%2Bn8bGVNcKY6ar6KHV8bXAZQFh0RhO%2F32xTSRW%2FWKSahJDx5cua5TBfjyI95Z8JN9HqR3CWrZ%2Bt9UOsMjP291PaEn5zuFrFudqlZL2GPG6HGQydz2QPii1XOlP5l5ZpcC7H25pEMIISxqg2V6chQ33X%2BlFzTIlzKFJvEWTn2KAQZppKsYdo8jI6VNTR0PzXC53Bd1stZSu3oy9XEkcZJewu2INcPZKmstxmHUsy9P4oa7xtJOAuBJQAV3Sf23uAnVWetqVd2%2BCJQpn5nn%2FFQ8ErFPYDR5211Pu%2BoBZBfaS%2FHyxAktw1bkGxLUdiWfVJRwqEMCswHYJN5COhZH8FW1JCoWbY8GWroeWk1VpmI2ge7KV%2Bnwoor4SnZ0r3OzERhlTFpNnuIp2OlSt02laZveyonrlFPTP%2F%2Fmum83Kiev%2FY%2FjTXHFNSO1Ci5gOJuXJNKszzWenb2JBcthd9UNMJvN9bwGOqUBsjYo3RTQg5KxYT39vy5DHpkAY5WSqf3pNWeZX3vpihh%2B0TFm6p6%2FsOAj8swRse%2B2X2fShvjG%2BbSjLHlJxCBuScsJeMzYVvPBKvsa2lTBtxr3CrdcRNtSaIqRWY1KtQSrAv1WMpXo%2FamoiOb5xfF8VSEFLWg20RDHS0bwcKKP8RuC7RYW6X6A25eQ2wVD75tZmziZJ2uoyU8oA4DeMaWcp25odjEq&X-Amz-Signature=aac8e20929ecf602c21405fc4da51622192fc57de87e2ae41252dcc82e98a947&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGLNREC4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTZtGjOzU%2BGX0jv1qXd0J45XRSNiPY7fxYQXcb1AP7uAIgPg3RprP7XJHw9QJ2RKylw37xBa7mzr%2BEfqNkL5BJmGYqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNxTmienIWE5NZRKBCrcA5sOdFAmHZakHWnTbLTixsQ0fTS3NoueZQThfYxUd32bR%2FLiXusG2nidLf%2Fai2gPbsH6%2FmpdXtubkOfYLqZFOyFsrchjiAEUAwwHLzYKF7091eyXFVZ878iGTLdSHgeDBL5WoYZkzoxsxOfNKH1oVVD4NWD6WMSoHtRzHR7jKBrF%2Bn8bGVNcKY6ar6KHV8bXAZQFh0RhO%2F32xTSRW%2FWKSahJDx5cua5TBfjyI95Z8JN9HqR3CWrZ%2Bt9UOsMjP291PaEn5zuFrFudqlZL2GPG6HGQydz2QPii1XOlP5l5ZpcC7H25pEMIISxqg2V6chQ33X%2BlFzTIlzKFJvEWTn2KAQZppKsYdo8jI6VNTR0PzXC53Bd1stZSu3oy9XEkcZJewu2INcPZKmstxmHUsy9P4oa7xtJOAuBJQAV3Sf23uAnVWetqVd2%2BCJQpn5nn%2FFQ8ErFPYDR5211Pu%2BoBZBfaS%2FHyxAktw1bkGxLUdiWfVJRwqEMCswHYJN5COhZH8FW1JCoWbY8GWroeWk1VpmI2ge7KV%2Bnwoor4SnZ0r3OzERhlTFpNnuIp2OlSt02laZveyonrlFPTP%2F%2Fmum83Kiev%2FY%2FjTXHFNSO1Ci5gOJuXJNKszzWenb2JBcthd9UNMJvN9bwGOqUBsjYo3RTQg5KxYT39vy5DHpkAY5WSqf3pNWeZX3vpihh%2B0TFm6p6%2FsOAj8swRse%2B2X2fShvjG%2BbSjLHlJxCBuScsJeMzYVvPBKvsa2lTBtxr3CrdcRNtSaIqRWY1KtQSrAv1WMpXo%2FamoiOb5xfF8VSEFLWg20RDHS0bwcKKP8RuC7RYW6X6A25eQ2wVD75tZmziZJ2uoyU8oA4DeMaWcp25odjEq&X-Amz-Signature=80ea1fb8c95bc9dd01ec5b6899e146f36037c4b84d2e8611fb4a8eb30abc1fdc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGLNREC4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTZtGjOzU%2BGX0jv1qXd0J45XRSNiPY7fxYQXcb1AP7uAIgPg3RprP7XJHw9QJ2RKylw37xBa7mzr%2BEfqNkL5BJmGYqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNxTmienIWE5NZRKBCrcA5sOdFAmHZakHWnTbLTixsQ0fTS3NoueZQThfYxUd32bR%2FLiXusG2nidLf%2Fai2gPbsH6%2FmpdXtubkOfYLqZFOyFsrchjiAEUAwwHLzYKF7091eyXFVZ878iGTLdSHgeDBL5WoYZkzoxsxOfNKH1oVVD4NWD6WMSoHtRzHR7jKBrF%2Bn8bGVNcKY6ar6KHV8bXAZQFh0RhO%2F32xTSRW%2FWKSahJDx5cua5TBfjyI95Z8JN9HqR3CWrZ%2Bt9UOsMjP291PaEn5zuFrFudqlZL2GPG6HGQydz2QPii1XOlP5l5ZpcC7H25pEMIISxqg2V6chQ33X%2BlFzTIlzKFJvEWTn2KAQZppKsYdo8jI6VNTR0PzXC53Bd1stZSu3oy9XEkcZJewu2INcPZKmstxmHUsy9P4oa7xtJOAuBJQAV3Sf23uAnVWetqVd2%2BCJQpn5nn%2FFQ8ErFPYDR5211Pu%2BoBZBfaS%2FHyxAktw1bkGxLUdiWfVJRwqEMCswHYJN5COhZH8FW1JCoWbY8GWroeWk1VpmI2ge7KV%2Bnwoor4SnZ0r3OzERhlTFpNnuIp2OlSt02laZveyonrlFPTP%2F%2Fmum83Kiev%2FY%2FjTXHFNSO1Ci5gOJuXJNKszzWenb2JBcthd9UNMJvN9bwGOqUBsjYo3RTQg5KxYT39vy5DHpkAY5WSqf3pNWeZX3vpihh%2B0TFm6p6%2FsOAj8swRse%2B2X2fShvjG%2BbSjLHlJxCBuScsJeMzYVvPBKvsa2lTBtxr3CrdcRNtSaIqRWY1KtQSrAv1WMpXo%2FamoiOb5xfF8VSEFLWg20RDHS0bwcKKP8RuC7RYW6X6A25eQ2wVD75tZmziZJ2uoyU8oA4DeMaWcp25odjEq&X-Amz-Signature=8cf25ac88f4ad816c2c180d05f8eaf06e58d347b16b3781c56454c8d4c7f7344&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGLNREC4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTZtGjOzU%2BGX0jv1qXd0J45XRSNiPY7fxYQXcb1AP7uAIgPg3RprP7XJHw9QJ2RKylw37xBa7mzr%2BEfqNkL5BJmGYqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNxTmienIWE5NZRKBCrcA5sOdFAmHZakHWnTbLTixsQ0fTS3NoueZQThfYxUd32bR%2FLiXusG2nidLf%2Fai2gPbsH6%2FmpdXtubkOfYLqZFOyFsrchjiAEUAwwHLzYKF7091eyXFVZ878iGTLdSHgeDBL5WoYZkzoxsxOfNKH1oVVD4NWD6WMSoHtRzHR7jKBrF%2Bn8bGVNcKY6ar6KHV8bXAZQFh0RhO%2F32xTSRW%2FWKSahJDx5cua5TBfjyI95Z8JN9HqR3CWrZ%2Bt9UOsMjP291PaEn5zuFrFudqlZL2GPG6HGQydz2QPii1XOlP5l5ZpcC7H25pEMIISxqg2V6chQ33X%2BlFzTIlzKFJvEWTn2KAQZppKsYdo8jI6VNTR0PzXC53Bd1stZSu3oy9XEkcZJewu2INcPZKmstxmHUsy9P4oa7xtJOAuBJQAV3Sf23uAnVWetqVd2%2BCJQpn5nn%2FFQ8ErFPYDR5211Pu%2BoBZBfaS%2FHyxAktw1bkGxLUdiWfVJRwqEMCswHYJN5COhZH8FW1JCoWbY8GWroeWk1VpmI2ge7KV%2Bnwoor4SnZ0r3OzERhlTFpNnuIp2OlSt02laZveyonrlFPTP%2F%2Fmum83Kiev%2FY%2FjTXHFNSO1Ci5gOJuXJNKszzWenb2JBcthd9UNMJvN9bwGOqUBsjYo3RTQg5KxYT39vy5DHpkAY5WSqf3pNWeZX3vpihh%2B0TFm6p6%2FsOAj8swRse%2B2X2fShvjG%2BbSjLHlJxCBuScsJeMzYVvPBKvsa2lTBtxr3CrdcRNtSaIqRWY1KtQSrAv1WMpXo%2FamoiOb5xfF8VSEFLWg20RDHS0bwcKKP8RuC7RYW6X6A25eQ2wVD75tZmziZJ2uoyU8oA4DeMaWcp25odjEq&X-Amz-Signature=5293fb60d956a589559d9fed5055d9e42bcea298911ef762f139c86af3eb1003&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGLNREC4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTZtGjOzU%2BGX0jv1qXd0J45XRSNiPY7fxYQXcb1AP7uAIgPg3RprP7XJHw9QJ2RKylw37xBa7mzr%2BEfqNkL5BJmGYqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNxTmienIWE5NZRKBCrcA5sOdFAmHZakHWnTbLTixsQ0fTS3NoueZQThfYxUd32bR%2FLiXusG2nidLf%2Fai2gPbsH6%2FmpdXtubkOfYLqZFOyFsrchjiAEUAwwHLzYKF7091eyXFVZ878iGTLdSHgeDBL5WoYZkzoxsxOfNKH1oVVD4NWD6WMSoHtRzHR7jKBrF%2Bn8bGVNcKY6ar6KHV8bXAZQFh0RhO%2F32xTSRW%2FWKSahJDx5cua5TBfjyI95Z8JN9HqR3CWrZ%2Bt9UOsMjP291PaEn5zuFrFudqlZL2GPG6HGQydz2QPii1XOlP5l5ZpcC7H25pEMIISxqg2V6chQ33X%2BlFzTIlzKFJvEWTn2KAQZppKsYdo8jI6VNTR0PzXC53Bd1stZSu3oy9XEkcZJewu2INcPZKmstxmHUsy9P4oa7xtJOAuBJQAV3Sf23uAnVWetqVd2%2BCJQpn5nn%2FFQ8ErFPYDR5211Pu%2BoBZBfaS%2FHyxAktw1bkGxLUdiWfVJRwqEMCswHYJN5COhZH8FW1JCoWbY8GWroeWk1VpmI2ge7KV%2Bnwoor4SnZ0r3OzERhlTFpNnuIp2OlSt02laZveyonrlFPTP%2F%2Fmum83Kiev%2FY%2FjTXHFNSO1Ci5gOJuXJNKszzWenb2JBcthd9UNMJvN9bwGOqUBsjYo3RTQg5KxYT39vy5DHpkAY5WSqf3pNWeZX3vpihh%2B0TFm6p6%2FsOAj8swRse%2B2X2fShvjG%2BbSjLHlJxCBuScsJeMzYVvPBKvsa2lTBtxr3CrdcRNtSaIqRWY1KtQSrAv1WMpXo%2FamoiOb5xfF8VSEFLWg20RDHS0bwcKKP8RuC7RYW6X6A25eQ2wVD75tZmziZJ2uoyU8oA4DeMaWcp25odjEq&X-Amz-Signature=22174e3e68f631924703a4068252d2435f924584f49e5d4d1eed7c89ac5972c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGLNREC4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTZtGjOzU%2BGX0jv1qXd0J45XRSNiPY7fxYQXcb1AP7uAIgPg3RprP7XJHw9QJ2RKylw37xBa7mzr%2BEfqNkL5BJmGYqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNxTmienIWE5NZRKBCrcA5sOdFAmHZakHWnTbLTixsQ0fTS3NoueZQThfYxUd32bR%2FLiXusG2nidLf%2Fai2gPbsH6%2FmpdXtubkOfYLqZFOyFsrchjiAEUAwwHLzYKF7091eyXFVZ878iGTLdSHgeDBL5WoYZkzoxsxOfNKH1oVVD4NWD6WMSoHtRzHR7jKBrF%2Bn8bGVNcKY6ar6KHV8bXAZQFh0RhO%2F32xTSRW%2FWKSahJDx5cua5TBfjyI95Z8JN9HqR3CWrZ%2Bt9UOsMjP291PaEn5zuFrFudqlZL2GPG6HGQydz2QPii1XOlP5l5ZpcC7H25pEMIISxqg2V6chQ33X%2BlFzTIlzKFJvEWTn2KAQZppKsYdo8jI6VNTR0PzXC53Bd1stZSu3oy9XEkcZJewu2INcPZKmstxmHUsy9P4oa7xtJOAuBJQAV3Sf23uAnVWetqVd2%2BCJQpn5nn%2FFQ8ErFPYDR5211Pu%2BoBZBfaS%2FHyxAktw1bkGxLUdiWfVJRwqEMCswHYJN5COhZH8FW1JCoWbY8GWroeWk1VpmI2ge7KV%2Bnwoor4SnZ0r3OzERhlTFpNnuIp2OlSt02laZveyonrlFPTP%2F%2Fmum83Kiev%2FY%2FjTXHFNSO1Ci5gOJuXJNKszzWenb2JBcthd9UNMJvN9bwGOqUBsjYo3RTQg5KxYT39vy5DHpkAY5WSqf3pNWeZX3vpihh%2B0TFm6p6%2FsOAj8swRse%2B2X2fShvjG%2BbSjLHlJxCBuScsJeMzYVvPBKvsa2lTBtxr3CrdcRNtSaIqRWY1KtQSrAv1WMpXo%2FamoiOb5xfF8VSEFLWg20RDHS0bwcKKP8RuC7RYW6X6A25eQ2wVD75tZmziZJ2uoyU8oA4DeMaWcp25odjEq&X-Amz-Signature=06275d76a71e2d888778815a9bd4b82e55e369ea5147ebe6d0c75287c82d031c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGLNREC4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTZtGjOzU%2BGX0jv1qXd0J45XRSNiPY7fxYQXcb1AP7uAIgPg3RprP7XJHw9QJ2RKylw37xBa7mzr%2BEfqNkL5BJmGYqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNxTmienIWE5NZRKBCrcA5sOdFAmHZakHWnTbLTixsQ0fTS3NoueZQThfYxUd32bR%2FLiXusG2nidLf%2Fai2gPbsH6%2FmpdXtubkOfYLqZFOyFsrchjiAEUAwwHLzYKF7091eyXFVZ878iGTLdSHgeDBL5WoYZkzoxsxOfNKH1oVVD4NWD6WMSoHtRzHR7jKBrF%2Bn8bGVNcKY6ar6KHV8bXAZQFh0RhO%2F32xTSRW%2FWKSahJDx5cua5TBfjyI95Z8JN9HqR3CWrZ%2Bt9UOsMjP291PaEn5zuFrFudqlZL2GPG6HGQydz2QPii1XOlP5l5ZpcC7H25pEMIISxqg2V6chQ33X%2BlFzTIlzKFJvEWTn2KAQZppKsYdo8jI6VNTR0PzXC53Bd1stZSu3oy9XEkcZJewu2INcPZKmstxmHUsy9P4oa7xtJOAuBJQAV3Sf23uAnVWetqVd2%2BCJQpn5nn%2FFQ8ErFPYDR5211Pu%2BoBZBfaS%2FHyxAktw1bkGxLUdiWfVJRwqEMCswHYJN5COhZH8FW1JCoWbY8GWroeWk1VpmI2ge7KV%2Bnwoor4SnZ0r3OzERhlTFpNnuIp2OlSt02laZveyonrlFPTP%2F%2Fmum83Kiev%2FY%2FjTXHFNSO1Ci5gOJuXJNKszzWenb2JBcthd9UNMJvN9bwGOqUBsjYo3RTQg5KxYT39vy5DHpkAY5WSqf3pNWeZX3vpihh%2B0TFm6p6%2FsOAj8swRse%2B2X2fShvjG%2BbSjLHlJxCBuScsJeMzYVvPBKvsa2lTBtxr3CrdcRNtSaIqRWY1KtQSrAv1WMpXo%2FamoiOb5xfF8VSEFLWg20RDHS0bwcKKP8RuC7RYW6X6A25eQ2wVD75tZmziZJ2uoyU8oA4DeMaWcp25odjEq&X-Amz-Signature=76f8969be851214ece28df36e24348f80a33fd62843a2add98e0d5aba161339e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSVBHHQB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICf2F48bBvfyZPE2lXB7WZaDfVw0XcwKu87ZEq%2BOrU0SAiEAoam0gudHUlIFgRf44elUwUEfvapV1LNBKyZjFXIV7oAqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgGp%2BZWqPiZT3obKCrcA4F5Uqm246lyVsNb4gAU49kAdq58hfOBIlnOPWQ6gjmkMGXZzGnNZOgZgoIuYwgDhtl8W%2BIN4DpCibLbXL82jsL9NP8%2B5n6aGrCph5SGqvzhZzO38%2BtGlt7hmwKfncW7BU2bv2hWaqdzd9LzCVD4cS9nrMNWudNm0A4qdenSlsbWz0PPwzMZfoszkORk2hlwYdoDZXX0Y0KTuIr9m9mL%2BP8qFrxEqCRQp3afGDO1gBMlUgVU7DhkFIj2%2FWVM61in33QJjhSjSOO3HLzNyEjZ1PuLjNZVSrzDpVNbcd9a%2FEyGue%2BqD%2FHC5%2BgNq70gO%2Fi4mvSHvmrfAQnFFu%2FBfSc4aX%2BONSWSymnbQbM7E8QuaWqnMgNg3BJM6LkhWo7Kcv2TxrvZ%2BzZQONdjJ4n7P2Q85aqfDYB9D6i0Ibdj5MfRVtTY61ElQceOmYzGakH2UjqfWYakkqFUTTAVTQcbl2iH5vMklURfEfs1XJIElJ7X0j%2BgdUgIBEexeeOpyf%2F1pxNj2nL4Zin%2Fe4vYDG%2BRACQaLEslVtkyMINGB2vULst2AEiHgoVbm2U7J5jZMc%2FzGiynfxY5ykZE7NWDQ9cT4WZurb%2BBPuJqxxGZj%2B%2Fl4rpFTH%2FtL%2FijSIQxko52hYiSMPrM9bwGOqUBW5Q%2FYAhj6TLUaYn19bY0ErQH0g1xTS7KHqUkIqKHDNq9gXJ7A%2B%2FLmdKx04gi6zMARCZU7bCP3PpRHDGQqzcZrrt09U4AL2TevKKobUrIeCe%2BLy39H8QABfu0RPAWsmStS0vkQFUrb4ifCgcnFvFtrNyy%2FJHxmyPXdBdD7qhStcJ1sO4asTszH3Z30ehOTNgIP3DnBzFjZP%2FqGcwjrU3y6yqzzCdY&X-Amz-Signature=88e049a4e921cce56bace0e7cb219c2519f7d71297cf7630a81dcf11a4f645f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSVBHHQB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICf2F48bBvfyZPE2lXB7WZaDfVw0XcwKu87ZEq%2BOrU0SAiEAoam0gudHUlIFgRf44elUwUEfvapV1LNBKyZjFXIV7oAqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgGp%2BZWqPiZT3obKCrcA4F5Uqm246lyVsNb4gAU49kAdq58hfOBIlnOPWQ6gjmkMGXZzGnNZOgZgoIuYwgDhtl8W%2BIN4DpCibLbXL82jsL9NP8%2B5n6aGrCph5SGqvzhZzO38%2BtGlt7hmwKfncW7BU2bv2hWaqdzd9LzCVD4cS9nrMNWudNm0A4qdenSlsbWz0PPwzMZfoszkORk2hlwYdoDZXX0Y0KTuIr9m9mL%2BP8qFrxEqCRQp3afGDO1gBMlUgVU7DhkFIj2%2FWVM61in33QJjhSjSOO3HLzNyEjZ1PuLjNZVSrzDpVNbcd9a%2FEyGue%2BqD%2FHC5%2BgNq70gO%2Fi4mvSHvmrfAQnFFu%2FBfSc4aX%2BONSWSymnbQbM7E8QuaWqnMgNg3BJM6LkhWo7Kcv2TxrvZ%2BzZQONdjJ4n7P2Q85aqfDYB9D6i0Ibdj5MfRVtTY61ElQceOmYzGakH2UjqfWYakkqFUTTAVTQcbl2iH5vMklURfEfs1XJIElJ7X0j%2BgdUgIBEexeeOpyf%2F1pxNj2nL4Zin%2Fe4vYDG%2BRACQaLEslVtkyMINGB2vULst2AEiHgoVbm2U7J5jZMc%2FzGiynfxY5ykZE7NWDQ9cT4WZurb%2BBPuJqxxGZj%2B%2Fl4rpFTH%2FtL%2FijSIQxko52hYiSMPrM9bwGOqUBW5Q%2FYAhj6TLUaYn19bY0ErQH0g1xTS7KHqUkIqKHDNq9gXJ7A%2B%2FLmdKx04gi6zMARCZU7bCP3PpRHDGQqzcZrrt09U4AL2TevKKobUrIeCe%2BLy39H8QABfu0RPAWsmStS0vkQFUrb4ifCgcnFvFtrNyy%2FJHxmyPXdBdD7qhStcJ1sO4asTszH3Z30ehOTNgIP3DnBzFjZP%2FqGcwjrU3y6yqzzCdY&X-Amz-Signature=96f068523cae6e65476d453194e9dd348681081be844668adbd5ec280895e7f4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
