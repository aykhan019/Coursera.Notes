

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SUQHFKO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwcdRPHzVdcdc7KxOphR6%2FFzr0LrLu8hU%2BCuJhJcl5DgIhALvLf06o22nzkzCvKT9ijblVhlZ1LAe31Ns58QBsQ0uwKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyE2HjRd11QHm4Y%2FbAq3AP4OmpuUTrjlWXs4Hp%2BJ1394REocdSUJX7cUEQiTpLgbwSd1NwazfTPpTiFv1L%2FhxFsVbxF%2FKVXtK6mn%2BIg%2F3o3NrF%2B5tEW23Xlhp%2FqTV6BkHSy82NRbIQ4jOLsx5C62iLQH2pEwKbEUduN%2Fg69F4u5nOwejpQBeWp%2F6yaXbBC0oDPoAg2sNo6T5IExc2zZLx7YszLS1jqDdZGgYHcYHBoMYhR3fLBHgnVdouy4V9uo3%2FJSD0Cg7k6E74Fp57dJqBKz8aDXSz3g6QGjQou1bs2qb07XH1G6TSjCCxQtJJPKfCKOoC5p%2BEEb0xfOUp7ItOkhbnutjZ6BMvEfJf1EUtTkOCys5xzsA15tDY5F5xrlvS21S8LPpx0UyR4unZL%2F%2BRN8NbTSugwtqlOzZSnewjoWgUy1c6sUnreTsmA6w9m%2FOvI4gipn9cZAiJ3n4w9SIIu1b65kpNF%2B2jkdZiXiQG8Toath7D7q2TJKvwvJUkNd59rCoewtHobsg6bJYF2YCtnoGcT%2FioTuf8MEVe571c1WzJBrl6xBuAJFtqluD9BZSlqx3xgLYNzjh1z9ELysLxONk6g%2FnXqRPRnFLX41WYxEX%2FOOG9TiXlEHRJd4oKp8azcyfo0SKxCro91WmDDS3v68BjqkASPzn5EtOkOndJdZF91ebsnVRN%2BMkoKlmazz4fEDQuMdXHmOwxPX2pVPKI22sVpph%2BTvjF94n06oDZC9Y%2BgWpbgwp0Lae2USHD5aya3ppnmRQhahsDnR%2BsMvMNcsmm8Uk7sZavusAOjFsRWPdHkz9vwpgmU5W1Xs%2FbT0vWbpleT8gA94cknREesDHaFYzfp12AFfyzqF6OtVDgtwRpa0tC7dyS6D&X-Amz-Signature=fa6409ee3669c5220d22cbe0cbb77daf99e7c981cf8b6c0100f0b97f7bd87e33&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SUQHFKO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwcdRPHzVdcdc7KxOphR6%2FFzr0LrLu8hU%2BCuJhJcl5DgIhALvLf06o22nzkzCvKT9ijblVhlZ1LAe31Ns58QBsQ0uwKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyE2HjRd11QHm4Y%2FbAq3AP4OmpuUTrjlWXs4Hp%2BJ1394REocdSUJX7cUEQiTpLgbwSd1NwazfTPpTiFv1L%2FhxFsVbxF%2FKVXtK6mn%2BIg%2F3o3NrF%2B5tEW23Xlhp%2FqTV6BkHSy82NRbIQ4jOLsx5C62iLQH2pEwKbEUduN%2Fg69F4u5nOwejpQBeWp%2F6yaXbBC0oDPoAg2sNo6T5IExc2zZLx7YszLS1jqDdZGgYHcYHBoMYhR3fLBHgnVdouy4V9uo3%2FJSD0Cg7k6E74Fp57dJqBKz8aDXSz3g6QGjQou1bs2qb07XH1G6TSjCCxQtJJPKfCKOoC5p%2BEEb0xfOUp7ItOkhbnutjZ6BMvEfJf1EUtTkOCys5xzsA15tDY5F5xrlvS21S8LPpx0UyR4unZL%2F%2BRN8NbTSugwtqlOzZSnewjoWgUy1c6sUnreTsmA6w9m%2FOvI4gipn9cZAiJ3n4w9SIIu1b65kpNF%2B2jkdZiXiQG8Toath7D7q2TJKvwvJUkNd59rCoewtHobsg6bJYF2YCtnoGcT%2FioTuf8MEVe571c1WzJBrl6xBuAJFtqluD9BZSlqx3xgLYNzjh1z9ELysLxONk6g%2FnXqRPRnFLX41WYxEX%2FOOG9TiXlEHRJd4oKp8azcyfo0SKxCro91WmDDS3v68BjqkASPzn5EtOkOndJdZF91ebsnVRN%2BMkoKlmazz4fEDQuMdXHmOwxPX2pVPKI22sVpph%2BTvjF94n06oDZC9Y%2BgWpbgwp0Lae2USHD5aya3ppnmRQhahsDnR%2BsMvMNcsmm8Uk7sZavusAOjFsRWPdHkz9vwpgmU5W1Xs%2FbT0vWbpleT8gA94cknREesDHaFYzfp12AFfyzqF6OtVDgtwRpa0tC7dyS6D&X-Amz-Signature=ec7f3ac48ede3c8ef62b193d9dafc8aede5ded38ee744e9442548a43c3003825&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SUQHFKO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwcdRPHzVdcdc7KxOphR6%2FFzr0LrLu8hU%2BCuJhJcl5DgIhALvLf06o22nzkzCvKT9ijblVhlZ1LAe31Ns58QBsQ0uwKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyE2HjRd11QHm4Y%2FbAq3AP4OmpuUTrjlWXs4Hp%2BJ1394REocdSUJX7cUEQiTpLgbwSd1NwazfTPpTiFv1L%2FhxFsVbxF%2FKVXtK6mn%2BIg%2F3o3NrF%2B5tEW23Xlhp%2FqTV6BkHSy82NRbIQ4jOLsx5C62iLQH2pEwKbEUduN%2Fg69F4u5nOwejpQBeWp%2F6yaXbBC0oDPoAg2sNo6T5IExc2zZLx7YszLS1jqDdZGgYHcYHBoMYhR3fLBHgnVdouy4V9uo3%2FJSD0Cg7k6E74Fp57dJqBKz8aDXSz3g6QGjQou1bs2qb07XH1G6TSjCCxQtJJPKfCKOoC5p%2BEEb0xfOUp7ItOkhbnutjZ6BMvEfJf1EUtTkOCys5xzsA15tDY5F5xrlvS21S8LPpx0UyR4unZL%2F%2BRN8NbTSugwtqlOzZSnewjoWgUy1c6sUnreTsmA6w9m%2FOvI4gipn9cZAiJ3n4w9SIIu1b65kpNF%2B2jkdZiXiQG8Toath7D7q2TJKvwvJUkNd59rCoewtHobsg6bJYF2YCtnoGcT%2FioTuf8MEVe571c1WzJBrl6xBuAJFtqluD9BZSlqx3xgLYNzjh1z9ELysLxONk6g%2FnXqRPRnFLX41WYxEX%2FOOG9TiXlEHRJd4oKp8azcyfo0SKxCro91WmDDS3v68BjqkASPzn5EtOkOndJdZF91ebsnVRN%2BMkoKlmazz4fEDQuMdXHmOwxPX2pVPKI22sVpph%2BTvjF94n06oDZC9Y%2BgWpbgwp0Lae2USHD5aya3ppnmRQhahsDnR%2BsMvMNcsmm8Uk7sZavusAOjFsRWPdHkz9vwpgmU5W1Xs%2FbT0vWbpleT8gA94cknREesDHaFYzfp12AFfyzqF6OtVDgtwRpa0tC7dyS6D&X-Amz-Signature=119ee23be98caf85fbc7bb45acd66771dab21c105670b56d011743fd8a874468&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SUQHFKO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwcdRPHzVdcdc7KxOphR6%2FFzr0LrLu8hU%2BCuJhJcl5DgIhALvLf06o22nzkzCvKT9ijblVhlZ1LAe31Ns58QBsQ0uwKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyE2HjRd11QHm4Y%2FbAq3AP4OmpuUTrjlWXs4Hp%2BJ1394REocdSUJX7cUEQiTpLgbwSd1NwazfTPpTiFv1L%2FhxFsVbxF%2FKVXtK6mn%2BIg%2F3o3NrF%2B5tEW23Xlhp%2FqTV6BkHSy82NRbIQ4jOLsx5C62iLQH2pEwKbEUduN%2Fg69F4u5nOwejpQBeWp%2F6yaXbBC0oDPoAg2sNo6T5IExc2zZLx7YszLS1jqDdZGgYHcYHBoMYhR3fLBHgnVdouy4V9uo3%2FJSD0Cg7k6E74Fp57dJqBKz8aDXSz3g6QGjQou1bs2qb07XH1G6TSjCCxQtJJPKfCKOoC5p%2BEEb0xfOUp7ItOkhbnutjZ6BMvEfJf1EUtTkOCys5xzsA15tDY5F5xrlvS21S8LPpx0UyR4unZL%2F%2BRN8NbTSugwtqlOzZSnewjoWgUy1c6sUnreTsmA6w9m%2FOvI4gipn9cZAiJ3n4w9SIIu1b65kpNF%2B2jkdZiXiQG8Toath7D7q2TJKvwvJUkNd59rCoewtHobsg6bJYF2YCtnoGcT%2FioTuf8MEVe571c1WzJBrl6xBuAJFtqluD9BZSlqx3xgLYNzjh1z9ELysLxONk6g%2FnXqRPRnFLX41WYxEX%2FOOG9TiXlEHRJd4oKp8azcyfo0SKxCro91WmDDS3v68BjqkASPzn5EtOkOndJdZF91ebsnVRN%2BMkoKlmazz4fEDQuMdXHmOwxPX2pVPKI22sVpph%2BTvjF94n06oDZC9Y%2BgWpbgwp0Lae2USHD5aya3ppnmRQhahsDnR%2BsMvMNcsmm8Uk7sZavusAOjFsRWPdHkz9vwpgmU5W1Xs%2FbT0vWbpleT8gA94cknREesDHaFYzfp12AFfyzqF6OtVDgtwRpa0tC7dyS6D&X-Amz-Signature=520a4e5376024a73d265b008e5c6754cafb5719c5f3a966b03e2162053d141b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SUQHFKO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwcdRPHzVdcdc7KxOphR6%2FFzr0LrLu8hU%2BCuJhJcl5DgIhALvLf06o22nzkzCvKT9ijblVhlZ1LAe31Ns58QBsQ0uwKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyE2HjRd11QHm4Y%2FbAq3AP4OmpuUTrjlWXs4Hp%2BJ1394REocdSUJX7cUEQiTpLgbwSd1NwazfTPpTiFv1L%2FhxFsVbxF%2FKVXtK6mn%2BIg%2F3o3NrF%2B5tEW23Xlhp%2FqTV6BkHSy82NRbIQ4jOLsx5C62iLQH2pEwKbEUduN%2Fg69F4u5nOwejpQBeWp%2F6yaXbBC0oDPoAg2sNo6T5IExc2zZLx7YszLS1jqDdZGgYHcYHBoMYhR3fLBHgnVdouy4V9uo3%2FJSD0Cg7k6E74Fp57dJqBKz8aDXSz3g6QGjQou1bs2qb07XH1G6TSjCCxQtJJPKfCKOoC5p%2BEEb0xfOUp7ItOkhbnutjZ6BMvEfJf1EUtTkOCys5xzsA15tDY5F5xrlvS21S8LPpx0UyR4unZL%2F%2BRN8NbTSugwtqlOzZSnewjoWgUy1c6sUnreTsmA6w9m%2FOvI4gipn9cZAiJ3n4w9SIIu1b65kpNF%2B2jkdZiXiQG8Toath7D7q2TJKvwvJUkNd59rCoewtHobsg6bJYF2YCtnoGcT%2FioTuf8MEVe571c1WzJBrl6xBuAJFtqluD9BZSlqx3xgLYNzjh1z9ELysLxONk6g%2FnXqRPRnFLX41WYxEX%2FOOG9TiXlEHRJd4oKp8azcyfo0SKxCro91WmDDS3v68BjqkASPzn5EtOkOndJdZF91ebsnVRN%2BMkoKlmazz4fEDQuMdXHmOwxPX2pVPKI22sVpph%2BTvjF94n06oDZC9Y%2BgWpbgwp0Lae2USHD5aya3ppnmRQhahsDnR%2BsMvMNcsmm8Uk7sZavusAOjFsRWPdHkz9vwpgmU5W1Xs%2FbT0vWbpleT8gA94cknREesDHaFYzfp12AFfyzqF6OtVDgtwRpa0tC7dyS6D&X-Amz-Signature=eab092b1b6efcd5cd74a7fc43ae9b9bcdca60b7c7b243aeb90237d03882ff66a&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SUQHFKO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwcdRPHzVdcdc7KxOphR6%2FFzr0LrLu8hU%2BCuJhJcl5DgIhALvLf06o22nzkzCvKT9ijblVhlZ1LAe31Ns58QBsQ0uwKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyE2HjRd11QHm4Y%2FbAq3AP4OmpuUTrjlWXs4Hp%2BJ1394REocdSUJX7cUEQiTpLgbwSd1NwazfTPpTiFv1L%2FhxFsVbxF%2FKVXtK6mn%2BIg%2F3o3NrF%2B5tEW23Xlhp%2FqTV6BkHSy82NRbIQ4jOLsx5C62iLQH2pEwKbEUduN%2Fg69F4u5nOwejpQBeWp%2F6yaXbBC0oDPoAg2sNo6T5IExc2zZLx7YszLS1jqDdZGgYHcYHBoMYhR3fLBHgnVdouy4V9uo3%2FJSD0Cg7k6E74Fp57dJqBKz8aDXSz3g6QGjQou1bs2qb07XH1G6TSjCCxQtJJPKfCKOoC5p%2BEEb0xfOUp7ItOkhbnutjZ6BMvEfJf1EUtTkOCys5xzsA15tDY5F5xrlvS21S8LPpx0UyR4unZL%2F%2BRN8NbTSugwtqlOzZSnewjoWgUy1c6sUnreTsmA6w9m%2FOvI4gipn9cZAiJ3n4w9SIIu1b65kpNF%2B2jkdZiXiQG8Toath7D7q2TJKvwvJUkNd59rCoewtHobsg6bJYF2YCtnoGcT%2FioTuf8MEVe571c1WzJBrl6xBuAJFtqluD9BZSlqx3xgLYNzjh1z9ELysLxONk6g%2FnXqRPRnFLX41WYxEX%2FOOG9TiXlEHRJd4oKp8azcyfo0SKxCro91WmDDS3v68BjqkASPzn5EtOkOndJdZF91ebsnVRN%2BMkoKlmazz4fEDQuMdXHmOwxPX2pVPKI22sVpph%2BTvjF94n06oDZC9Y%2BgWpbgwp0Lae2USHD5aya3ppnmRQhahsDnR%2BsMvMNcsmm8Uk7sZavusAOjFsRWPdHkz9vwpgmU5W1Xs%2FbT0vWbpleT8gA94cknREesDHaFYzfp12AFfyzqF6OtVDgtwRpa0tC7dyS6D&X-Amz-Signature=872034130542e155c94fe976dc7f9e74401035a481d19dcc8485e20fffe690f2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SUQHFKO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwcdRPHzVdcdc7KxOphR6%2FFzr0LrLu8hU%2BCuJhJcl5DgIhALvLf06o22nzkzCvKT9ijblVhlZ1LAe31Ns58QBsQ0uwKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyE2HjRd11QHm4Y%2FbAq3AP4OmpuUTrjlWXs4Hp%2BJ1394REocdSUJX7cUEQiTpLgbwSd1NwazfTPpTiFv1L%2FhxFsVbxF%2FKVXtK6mn%2BIg%2F3o3NrF%2B5tEW23Xlhp%2FqTV6BkHSy82NRbIQ4jOLsx5C62iLQH2pEwKbEUduN%2Fg69F4u5nOwejpQBeWp%2F6yaXbBC0oDPoAg2sNo6T5IExc2zZLx7YszLS1jqDdZGgYHcYHBoMYhR3fLBHgnVdouy4V9uo3%2FJSD0Cg7k6E74Fp57dJqBKz8aDXSz3g6QGjQou1bs2qb07XH1G6TSjCCxQtJJPKfCKOoC5p%2BEEb0xfOUp7ItOkhbnutjZ6BMvEfJf1EUtTkOCys5xzsA15tDY5F5xrlvS21S8LPpx0UyR4unZL%2F%2BRN8NbTSugwtqlOzZSnewjoWgUy1c6sUnreTsmA6w9m%2FOvI4gipn9cZAiJ3n4w9SIIu1b65kpNF%2B2jkdZiXiQG8Toath7D7q2TJKvwvJUkNd59rCoewtHobsg6bJYF2YCtnoGcT%2FioTuf8MEVe571c1WzJBrl6xBuAJFtqluD9BZSlqx3xgLYNzjh1z9ELysLxONk6g%2FnXqRPRnFLX41WYxEX%2FOOG9TiXlEHRJd4oKp8azcyfo0SKxCro91WmDDS3v68BjqkASPzn5EtOkOndJdZF91ebsnVRN%2BMkoKlmazz4fEDQuMdXHmOwxPX2pVPKI22sVpph%2BTvjF94n06oDZC9Y%2BgWpbgwp0Lae2USHD5aya3ppnmRQhahsDnR%2BsMvMNcsmm8Uk7sZavusAOjFsRWPdHkz9vwpgmU5W1Xs%2FbT0vWbpleT8gA94cknREesDHaFYzfp12AFfyzqF6OtVDgtwRpa0tC7dyS6D&X-Amz-Signature=656bf3788401255782d0c9326b8f506acdd3fbd384fb423e63ca0612bb48f109&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SUQHFKO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwcdRPHzVdcdc7KxOphR6%2FFzr0LrLu8hU%2BCuJhJcl5DgIhALvLf06o22nzkzCvKT9ijblVhlZ1LAe31Ns58QBsQ0uwKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyE2HjRd11QHm4Y%2FbAq3AP4OmpuUTrjlWXs4Hp%2BJ1394REocdSUJX7cUEQiTpLgbwSd1NwazfTPpTiFv1L%2FhxFsVbxF%2FKVXtK6mn%2BIg%2F3o3NrF%2B5tEW23Xlhp%2FqTV6BkHSy82NRbIQ4jOLsx5C62iLQH2pEwKbEUduN%2Fg69F4u5nOwejpQBeWp%2F6yaXbBC0oDPoAg2sNo6T5IExc2zZLx7YszLS1jqDdZGgYHcYHBoMYhR3fLBHgnVdouy4V9uo3%2FJSD0Cg7k6E74Fp57dJqBKz8aDXSz3g6QGjQou1bs2qb07XH1G6TSjCCxQtJJPKfCKOoC5p%2BEEb0xfOUp7ItOkhbnutjZ6BMvEfJf1EUtTkOCys5xzsA15tDY5F5xrlvS21S8LPpx0UyR4unZL%2F%2BRN8NbTSugwtqlOzZSnewjoWgUy1c6sUnreTsmA6w9m%2FOvI4gipn9cZAiJ3n4w9SIIu1b65kpNF%2B2jkdZiXiQG8Toath7D7q2TJKvwvJUkNd59rCoewtHobsg6bJYF2YCtnoGcT%2FioTuf8MEVe571c1WzJBrl6xBuAJFtqluD9BZSlqx3xgLYNzjh1z9ELysLxONk6g%2FnXqRPRnFLX41WYxEX%2FOOG9TiXlEHRJd4oKp8azcyfo0SKxCro91WmDDS3v68BjqkASPzn5EtOkOndJdZF91ebsnVRN%2BMkoKlmazz4fEDQuMdXHmOwxPX2pVPKI22sVpph%2BTvjF94n06oDZC9Y%2BgWpbgwp0Lae2USHD5aya3ppnmRQhahsDnR%2BsMvMNcsmm8Uk7sZavusAOjFsRWPdHkz9vwpgmU5W1Xs%2FbT0vWbpleT8gA94cknREesDHaFYzfp12AFfyzqF6OtVDgtwRpa0tC7dyS6D&X-Amz-Signature=d1571ca365dcf70055ad054c4283c0cebb89e055fe89a24738a195a2adfca0fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SUQHFKO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwcdRPHzVdcdc7KxOphR6%2FFzr0LrLu8hU%2BCuJhJcl5DgIhALvLf06o22nzkzCvKT9ijblVhlZ1LAe31Ns58QBsQ0uwKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyE2HjRd11QHm4Y%2FbAq3AP4OmpuUTrjlWXs4Hp%2BJ1394REocdSUJX7cUEQiTpLgbwSd1NwazfTPpTiFv1L%2FhxFsVbxF%2FKVXtK6mn%2BIg%2F3o3NrF%2B5tEW23Xlhp%2FqTV6BkHSy82NRbIQ4jOLsx5C62iLQH2pEwKbEUduN%2Fg69F4u5nOwejpQBeWp%2F6yaXbBC0oDPoAg2sNo6T5IExc2zZLx7YszLS1jqDdZGgYHcYHBoMYhR3fLBHgnVdouy4V9uo3%2FJSD0Cg7k6E74Fp57dJqBKz8aDXSz3g6QGjQou1bs2qb07XH1G6TSjCCxQtJJPKfCKOoC5p%2BEEb0xfOUp7ItOkhbnutjZ6BMvEfJf1EUtTkOCys5xzsA15tDY5F5xrlvS21S8LPpx0UyR4unZL%2F%2BRN8NbTSugwtqlOzZSnewjoWgUy1c6sUnreTsmA6w9m%2FOvI4gipn9cZAiJ3n4w9SIIu1b65kpNF%2B2jkdZiXiQG8Toath7D7q2TJKvwvJUkNd59rCoewtHobsg6bJYF2YCtnoGcT%2FioTuf8MEVe571c1WzJBrl6xBuAJFtqluD9BZSlqx3xgLYNzjh1z9ELysLxONk6g%2FnXqRPRnFLX41WYxEX%2FOOG9TiXlEHRJd4oKp8azcyfo0SKxCro91WmDDS3v68BjqkASPzn5EtOkOndJdZF91ebsnVRN%2BMkoKlmazz4fEDQuMdXHmOwxPX2pVPKI22sVpph%2BTvjF94n06oDZC9Y%2BgWpbgwp0Lae2USHD5aya3ppnmRQhahsDnR%2BsMvMNcsmm8Uk7sZavusAOjFsRWPdHkz9vwpgmU5W1Xs%2FbT0vWbpleT8gA94cknREesDHaFYzfp12AFfyzqF6OtVDgtwRpa0tC7dyS6D&X-Amz-Signature=17389a3022de06b2113afbf803635eaefbc707ae93fd4d853171e47a86599a10&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FWRTD5U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPEsYEtqzwYZCVYtPsRqGSLw8pfnPY8fpRq0lIejzLuwIgMIG%2BHbzpDomTGmiFvhluM8vVps7YGT1yHZdykPkboRcqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIlgFWtNhZOgplo%2BiircA4xp02d7a1aLdo8au7VSm8RJquOCKzuqmCZXrs4kIYJw9Y0aKQrrSFV4uPwU93A2ccpGm%2BFUFRZNkXMJvdYtwfnW5GiEpLXj9HxSeZfYDTFyf5N6zDlAA9JLfB1xEV59xKg51brHHdY1jAgr114%2BFh7Kxtrq2HWqtTBNdFrjxciqOCMPBXs0P5q5IPkMHUsihLs3D1MoJaGMINO%2FFbc43MZbLj4vItYYWT9Cnd%2BmpUhVqFzVuLySjQRfjpesOVl7yjY69Xch9Jxm5FBvQYpgcRam9TvsygvrrL34afmm%2FTbJs2Wn2hpPblPWhdYNzgiUReZiWCQBBQ%2FYMn%2BXAGSsyfD1VD3r7%2FHWiduTGkutBdJMmy45VkeroSaWfnfCeTC%2BUMw1EKVQ8TwY3aotFRWplp00XU0aO0voWFPn8HhmirK%2FXgIKjh3KLIG8nTvx7ZKaJwOeSgpQDcO7ckY0QUyhIo7qwxhHj7QhQYoZCJjszn7aFApaBMKWdyPeUdmiULBwJFm%2BSuCoubo6e%2F47i%2BgOW6gKGxx7GM6u483N4JPO2%2FUDappmV6J9LZumW%2B5kanO%2BWjDgcgrD4SCYSQWRArnLR8gf1bX%2Ff%2FxGDi1Xjw3VwzJSXW8cqCH%2F%2BPvAQ9ZsMJzf%2FrwGOqUBwH3XiDsQDesdZ2bzA7VoquuKhqijGrmoaNaa3hsOCQDk59IA8zfmWBrvPZt9O6w2eY3duwN6HSw7ThJqGb3je3vjGD%2FAHgM2uMjFOqqIDLpYDyQ%2FvBcC4bT9UL0zQPftOOFbeBKC7C%2FGWg13FOjUKmNVxG8uefXtYfbphUtznXWK7M9DDMgXqk74ewSIQH%2BPRfcNgBLgxLuvk703ieVW2x7LWUm%2F&X-Amz-Signature=1ef8bd517f67a312fb3bb4f4fb2a9b66ed47324ab09849c7fbd3977908eecf3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FWRTD5U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPEsYEtqzwYZCVYtPsRqGSLw8pfnPY8fpRq0lIejzLuwIgMIG%2BHbzpDomTGmiFvhluM8vVps7YGT1yHZdykPkboRcqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIlgFWtNhZOgplo%2BiircA4xp02d7a1aLdo8au7VSm8RJquOCKzuqmCZXrs4kIYJw9Y0aKQrrSFV4uPwU93A2ccpGm%2BFUFRZNkXMJvdYtwfnW5GiEpLXj9HxSeZfYDTFyf5N6zDlAA9JLfB1xEV59xKg51brHHdY1jAgr114%2BFh7Kxtrq2HWqtTBNdFrjxciqOCMPBXs0P5q5IPkMHUsihLs3D1MoJaGMINO%2FFbc43MZbLj4vItYYWT9Cnd%2BmpUhVqFzVuLySjQRfjpesOVl7yjY69Xch9Jxm5FBvQYpgcRam9TvsygvrrL34afmm%2FTbJs2Wn2hpPblPWhdYNzgiUReZiWCQBBQ%2FYMn%2BXAGSsyfD1VD3r7%2FHWiduTGkutBdJMmy45VkeroSaWfnfCeTC%2BUMw1EKVQ8TwY3aotFRWplp00XU0aO0voWFPn8HhmirK%2FXgIKjh3KLIG8nTvx7ZKaJwOeSgpQDcO7ckY0QUyhIo7qwxhHj7QhQYoZCJjszn7aFApaBMKWdyPeUdmiULBwJFm%2BSuCoubo6e%2F47i%2BgOW6gKGxx7GM6u483N4JPO2%2FUDappmV6J9LZumW%2B5kanO%2BWjDgcgrD4SCYSQWRArnLR8gf1bX%2Ff%2FxGDi1Xjw3VwzJSXW8cqCH%2F%2BPvAQ9ZsMJzf%2FrwGOqUBwH3XiDsQDesdZ2bzA7VoquuKhqijGrmoaNaa3hsOCQDk59IA8zfmWBrvPZt9O6w2eY3duwN6HSw7ThJqGb3je3vjGD%2FAHgM2uMjFOqqIDLpYDyQ%2FvBcC4bT9UL0zQPftOOFbeBKC7C%2FGWg13FOjUKmNVxG8uefXtYfbphUtznXWK7M9DDMgXqk74ewSIQH%2BPRfcNgBLgxLuvk703ieVW2x7LWUm%2F&X-Amz-Signature=b51d45452a01d91576ff9070b209c759f5b1fd42eb22d97201b9c4e380d776ff&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
