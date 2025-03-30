

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBAGFNNZ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIBGjJzlF5s5Q39k7YZNowJWj9R1b7N8rRu1DJ%2Bb1QOplAiBwqzEsKeHL06cMJCiP%2BVmhGK95YxLx%2FGoA4uKo71rw7iqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAvPa1zoti3kUM3teKtwDCCOVHyjyzp0T8eOBxoTaX2f4S4quMtkGMA6M5AVeptgznqLma62KG9d3rvthegsCcdPM%2BRrFRHHBWB9KLpj2WuKuKZOafnqRN7b%2BYIqmupWYKUP9RflUqjnLXSONRLMrjebz2clpPsJj3H0T%2FuIRfM5gQf4Jut59Ovzn8w%2F3LC%2BjZ850QNok0Mh3LlvPdjbrCzis3t8zansASLr5CWMlgYe%2F4SXf9EfHJprqnq6L7mqD6g2lJIhE8ArDGNHOSkhc1Mgi4r1tu8dM42N%2BWr4EM2AzUclm%2FaGuNifxtZG1UOOM1c%2BNEiaRJT9Ey7YlFm96DWNzbYXEbDNMMFKagKYMJPMJR0ha4tGu9lgh1fI%2BbV%2FicnvF2s1T3xm%2F0sZaUMeARbZ9A5Tgkhmti%2FLh5Dd5d4cUpua%2F%2FNChSoo1%2FofgVJ6Nhij2nQG3Nrwo7CmaQ9aWcpBZHiwGu6XTXZgAV99NRwWMOfWnM79yODAhErphwGCOvFAaS9C0v8d%2FA89aOiW2x7lZFS1z4Q6FGryD1MWaZiM81elBaH9h4f1sIu4NeeH4BRW9TZmdUHiAqPVwkEVVQfoIVRp97VBzhbf3yWg6yPxlU2wdyHt3Azv367OwRM89dobnXbO%2FFYDvRYwwsPyhvwY6pgHdmhPDrr4%2F9sVdOWK8mdBKJUzEbqCCjx2OwOkp2UaNKnML318POFYOiiohBEWpFhpNyJSmlG5RD%2BSKRtpiF4pfh3eC2AWuHmvDaaIAWWMKeFBOhHkaD0L6WWbS33nCa4uysq4jm8LAxWidMvZUb729EKN5brVSTyfC7sgjt2FmCiPue4WMBkLwfWbQp1WPOwJcVVobiuvedbnFWdVHsbQ35QTqJ5lv&X-Amz-Signature=0e25b7da5db91bdba8aa018c85be5c80607f1970f822221672189fe7b9047fa5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBAGFNNZ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIBGjJzlF5s5Q39k7YZNowJWj9R1b7N8rRu1DJ%2Bb1QOplAiBwqzEsKeHL06cMJCiP%2BVmhGK95YxLx%2FGoA4uKo71rw7iqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAvPa1zoti3kUM3teKtwDCCOVHyjyzp0T8eOBxoTaX2f4S4quMtkGMA6M5AVeptgznqLma62KG9d3rvthegsCcdPM%2BRrFRHHBWB9KLpj2WuKuKZOafnqRN7b%2BYIqmupWYKUP9RflUqjnLXSONRLMrjebz2clpPsJj3H0T%2FuIRfM5gQf4Jut59Ovzn8w%2F3LC%2BjZ850QNok0Mh3LlvPdjbrCzis3t8zansASLr5CWMlgYe%2F4SXf9EfHJprqnq6L7mqD6g2lJIhE8ArDGNHOSkhc1Mgi4r1tu8dM42N%2BWr4EM2AzUclm%2FaGuNifxtZG1UOOM1c%2BNEiaRJT9Ey7YlFm96DWNzbYXEbDNMMFKagKYMJPMJR0ha4tGu9lgh1fI%2BbV%2FicnvF2s1T3xm%2F0sZaUMeARbZ9A5Tgkhmti%2FLh5Dd5d4cUpua%2F%2FNChSoo1%2FofgVJ6Nhij2nQG3Nrwo7CmaQ9aWcpBZHiwGu6XTXZgAV99NRwWMOfWnM79yODAhErphwGCOvFAaS9C0v8d%2FA89aOiW2x7lZFS1z4Q6FGryD1MWaZiM81elBaH9h4f1sIu4NeeH4BRW9TZmdUHiAqPVwkEVVQfoIVRp97VBzhbf3yWg6yPxlU2wdyHt3Azv367OwRM89dobnXbO%2FFYDvRYwwsPyhvwY6pgHdmhPDrr4%2F9sVdOWK8mdBKJUzEbqCCjx2OwOkp2UaNKnML318POFYOiiohBEWpFhpNyJSmlG5RD%2BSKRtpiF4pfh3eC2AWuHmvDaaIAWWMKeFBOhHkaD0L6WWbS33nCa4uysq4jm8LAxWidMvZUb729EKN5brVSTyfC7sgjt2FmCiPue4WMBkLwfWbQp1WPOwJcVVobiuvedbnFWdVHsbQ35QTqJ5lv&X-Amz-Signature=c8b81d2d5b95b3038ab08343ad27bc916e4323063367d888894fa1854564f4df&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBAGFNNZ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIBGjJzlF5s5Q39k7YZNowJWj9R1b7N8rRu1DJ%2Bb1QOplAiBwqzEsKeHL06cMJCiP%2BVmhGK95YxLx%2FGoA4uKo71rw7iqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAvPa1zoti3kUM3teKtwDCCOVHyjyzp0T8eOBxoTaX2f4S4quMtkGMA6M5AVeptgznqLma62KG9d3rvthegsCcdPM%2BRrFRHHBWB9KLpj2WuKuKZOafnqRN7b%2BYIqmupWYKUP9RflUqjnLXSONRLMrjebz2clpPsJj3H0T%2FuIRfM5gQf4Jut59Ovzn8w%2F3LC%2BjZ850QNok0Mh3LlvPdjbrCzis3t8zansASLr5CWMlgYe%2F4SXf9EfHJprqnq6L7mqD6g2lJIhE8ArDGNHOSkhc1Mgi4r1tu8dM42N%2BWr4EM2AzUclm%2FaGuNifxtZG1UOOM1c%2BNEiaRJT9Ey7YlFm96DWNzbYXEbDNMMFKagKYMJPMJR0ha4tGu9lgh1fI%2BbV%2FicnvF2s1T3xm%2F0sZaUMeARbZ9A5Tgkhmti%2FLh5Dd5d4cUpua%2F%2FNChSoo1%2FofgVJ6Nhij2nQG3Nrwo7CmaQ9aWcpBZHiwGu6XTXZgAV99NRwWMOfWnM79yODAhErphwGCOvFAaS9C0v8d%2FA89aOiW2x7lZFS1z4Q6FGryD1MWaZiM81elBaH9h4f1sIu4NeeH4BRW9TZmdUHiAqPVwkEVVQfoIVRp97VBzhbf3yWg6yPxlU2wdyHt3Azv367OwRM89dobnXbO%2FFYDvRYwwsPyhvwY6pgHdmhPDrr4%2F9sVdOWK8mdBKJUzEbqCCjx2OwOkp2UaNKnML318POFYOiiohBEWpFhpNyJSmlG5RD%2BSKRtpiF4pfh3eC2AWuHmvDaaIAWWMKeFBOhHkaD0L6WWbS33nCa4uysq4jm8LAxWidMvZUb729EKN5brVSTyfC7sgjt2FmCiPue4WMBkLwfWbQp1WPOwJcVVobiuvedbnFWdVHsbQ35QTqJ5lv&X-Amz-Signature=16ab431f45439d4a5ddf6a474a82f43d13f73ebc135ca8cee6cf9ff253415f0f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBAGFNNZ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIBGjJzlF5s5Q39k7YZNowJWj9R1b7N8rRu1DJ%2Bb1QOplAiBwqzEsKeHL06cMJCiP%2BVmhGK95YxLx%2FGoA4uKo71rw7iqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAvPa1zoti3kUM3teKtwDCCOVHyjyzp0T8eOBxoTaX2f4S4quMtkGMA6M5AVeptgznqLma62KG9d3rvthegsCcdPM%2BRrFRHHBWB9KLpj2WuKuKZOafnqRN7b%2BYIqmupWYKUP9RflUqjnLXSONRLMrjebz2clpPsJj3H0T%2FuIRfM5gQf4Jut59Ovzn8w%2F3LC%2BjZ850QNok0Mh3LlvPdjbrCzis3t8zansASLr5CWMlgYe%2F4SXf9EfHJprqnq6L7mqD6g2lJIhE8ArDGNHOSkhc1Mgi4r1tu8dM42N%2BWr4EM2AzUclm%2FaGuNifxtZG1UOOM1c%2BNEiaRJT9Ey7YlFm96DWNzbYXEbDNMMFKagKYMJPMJR0ha4tGu9lgh1fI%2BbV%2FicnvF2s1T3xm%2F0sZaUMeARbZ9A5Tgkhmti%2FLh5Dd5d4cUpua%2F%2FNChSoo1%2FofgVJ6Nhij2nQG3Nrwo7CmaQ9aWcpBZHiwGu6XTXZgAV99NRwWMOfWnM79yODAhErphwGCOvFAaS9C0v8d%2FA89aOiW2x7lZFS1z4Q6FGryD1MWaZiM81elBaH9h4f1sIu4NeeH4BRW9TZmdUHiAqPVwkEVVQfoIVRp97VBzhbf3yWg6yPxlU2wdyHt3Azv367OwRM89dobnXbO%2FFYDvRYwwsPyhvwY6pgHdmhPDrr4%2F9sVdOWK8mdBKJUzEbqCCjx2OwOkp2UaNKnML318POFYOiiohBEWpFhpNyJSmlG5RD%2BSKRtpiF4pfh3eC2AWuHmvDaaIAWWMKeFBOhHkaD0L6WWbS33nCa4uysq4jm8LAxWidMvZUb729EKN5brVSTyfC7sgjt2FmCiPue4WMBkLwfWbQp1WPOwJcVVobiuvedbnFWdVHsbQ35QTqJ5lv&X-Amz-Signature=9e75e07d8e794882b3666b7f14ca78f52f123e232ac2f06d246c0077e7ba6fc5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBAGFNNZ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIBGjJzlF5s5Q39k7YZNowJWj9R1b7N8rRu1DJ%2Bb1QOplAiBwqzEsKeHL06cMJCiP%2BVmhGK95YxLx%2FGoA4uKo71rw7iqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAvPa1zoti3kUM3teKtwDCCOVHyjyzp0T8eOBxoTaX2f4S4quMtkGMA6M5AVeptgznqLma62KG9d3rvthegsCcdPM%2BRrFRHHBWB9KLpj2WuKuKZOafnqRN7b%2BYIqmupWYKUP9RflUqjnLXSONRLMrjebz2clpPsJj3H0T%2FuIRfM5gQf4Jut59Ovzn8w%2F3LC%2BjZ850QNok0Mh3LlvPdjbrCzis3t8zansASLr5CWMlgYe%2F4SXf9EfHJprqnq6L7mqD6g2lJIhE8ArDGNHOSkhc1Mgi4r1tu8dM42N%2BWr4EM2AzUclm%2FaGuNifxtZG1UOOM1c%2BNEiaRJT9Ey7YlFm96DWNzbYXEbDNMMFKagKYMJPMJR0ha4tGu9lgh1fI%2BbV%2FicnvF2s1T3xm%2F0sZaUMeARbZ9A5Tgkhmti%2FLh5Dd5d4cUpua%2F%2FNChSoo1%2FofgVJ6Nhij2nQG3Nrwo7CmaQ9aWcpBZHiwGu6XTXZgAV99NRwWMOfWnM79yODAhErphwGCOvFAaS9C0v8d%2FA89aOiW2x7lZFS1z4Q6FGryD1MWaZiM81elBaH9h4f1sIu4NeeH4BRW9TZmdUHiAqPVwkEVVQfoIVRp97VBzhbf3yWg6yPxlU2wdyHt3Azv367OwRM89dobnXbO%2FFYDvRYwwsPyhvwY6pgHdmhPDrr4%2F9sVdOWK8mdBKJUzEbqCCjx2OwOkp2UaNKnML318POFYOiiohBEWpFhpNyJSmlG5RD%2BSKRtpiF4pfh3eC2AWuHmvDaaIAWWMKeFBOhHkaD0L6WWbS33nCa4uysq4jm8LAxWidMvZUb729EKN5brVSTyfC7sgjt2FmCiPue4WMBkLwfWbQp1WPOwJcVVobiuvedbnFWdVHsbQ35QTqJ5lv&X-Amz-Signature=e92f54b399246b70db6f44a7298ae2b2630ad59216710cb3a358489017742957&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBAGFNNZ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIBGjJzlF5s5Q39k7YZNowJWj9R1b7N8rRu1DJ%2Bb1QOplAiBwqzEsKeHL06cMJCiP%2BVmhGK95YxLx%2FGoA4uKo71rw7iqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAvPa1zoti3kUM3teKtwDCCOVHyjyzp0T8eOBxoTaX2f4S4quMtkGMA6M5AVeptgznqLma62KG9d3rvthegsCcdPM%2BRrFRHHBWB9KLpj2WuKuKZOafnqRN7b%2BYIqmupWYKUP9RflUqjnLXSONRLMrjebz2clpPsJj3H0T%2FuIRfM5gQf4Jut59Ovzn8w%2F3LC%2BjZ850QNok0Mh3LlvPdjbrCzis3t8zansASLr5CWMlgYe%2F4SXf9EfHJprqnq6L7mqD6g2lJIhE8ArDGNHOSkhc1Mgi4r1tu8dM42N%2BWr4EM2AzUclm%2FaGuNifxtZG1UOOM1c%2BNEiaRJT9Ey7YlFm96DWNzbYXEbDNMMFKagKYMJPMJR0ha4tGu9lgh1fI%2BbV%2FicnvF2s1T3xm%2F0sZaUMeARbZ9A5Tgkhmti%2FLh5Dd5d4cUpua%2F%2FNChSoo1%2FofgVJ6Nhij2nQG3Nrwo7CmaQ9aWcpBZHiwGu6XTXZgAV99NRwWMOfWnM79yODAhErphwGCOvFAaS9C0v8d%2FA89aOiW2x7lZFS1z4Q6FGryD1MWaZiM81elBaH9h4f1sIu4NeeH4BRW9TZmdUHiAqPVwkEVVQfoIVRp97VBzhbf3yWg6yPxlU2wdyHt3Azv367OwRM89dobnXbO%2FFYDvRYwwsPyhvwY6pgHdmhPDrr4%2F9sVdOWK8mdBKJUzEbqCCjx2OwOkp2UaNKnML318POFYOiiohBEWpFhpNyJSmlG5RD%2BSKRtpiF4pfh3eC2AWuHmvDaaIAWWMKeFBOhHkaD0L6WWbS33nCa4uysq4jm8LAxWidMvZUb729EKN5brVSTyfC7sgjt2FmCiPue4WMBkLwfWbQp1WPOwJcVVobiuvedbnFWdVHsbQ35QTqJ5lv&X-Amz-Signature=b59d4be6608e6c656c8f039a659c72612fbfce4ca999a01038bba3c6625adc9e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBAGFNNZ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIBGjJzlF5s5Q39k7YZNowJWj9R1b7N8rRu1DJ%2Bb1QOplAiBwqzEsKeHL06cMJCiP%2BVmhGK95YxLx%2FGoA4uKo71rw7iqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAvPa1zoti3kUM3teKtwDCCOVHyjyzp0T8eOBxoTaX2f4S4quMtkGMA6M5AVeptgznqLma62KG9d3rvthegsCcdPM%2BRrFRHHBWB9KLpj2WuKuKZOafnqRN7b%2BYIqmupWYKUP9RflUqjnLXSONRLMrjebz2clpPsJj3H0T%2FuIRfM5gQf4Jut59Ovzn8w%2F3LC%2BjZ850QNok0Mh3LlvPdjbrCzis3t8zansASLr5CWMlgYe%2F4SXf9EfHJprqnq6L7mqD6g2lJIhE8ArDGNHOSkhc1Mgi4r1tu8dM42N%2BWr4EM2AzUclm%2FaGuNifxtZG1UOOM1c%2BNEiaRJT9Ey7YlFm96DWNzbYXEbDNMMFKagKYMJPMJR0ha4tGu9lgh1fI%2BbV%2FicnvF2s1T3xm%2F0sZaUMeARbZ9A5Tgkhmti%2FLh5Dd5d4cUpua%2F%2FNChSoo1%2FofgVJ6Nhij2nQG3Nrwo7CmaQ9aWcpBZHiwGu6XTXZgAV99NRwWMOfWnM79yODAhErphwGCOvFAaS9C0v8d%2FA89aOiW2x7lZFS1z4Q6FGryD1MWaZiM81elBaH9h4f1sIu4NeeH4BRW9TZmdUHiAqPVwkEVVQfoIVRp97VBzhbf3yWg6yPxlU2wdyHt3Azv367OwRM89dobnXbO%2FFYDvRYwwsPyhvwY6pgHdmhPDrr4%2F9sVdOWK8mdBKJUzEbqCCjx2OwOkp2UaNKnML318POFYOiiohBEWpFhpNyJSmlG5RD%2BSKRtpiF4pfh3eC2AWuHmvDaaIAWWMKeFBOhHkaD0L6WWbS33nCa4uysq4jm8LAxWidMvZUb729EKN5brVSTyfC7sgjt2FmCiPue4WMBkLwfWbQp1WPOwJcVVobiuvedbnFWdVHsbQ35QTqJ5lv&X-Amz-Signature=9d7f12e8644bec8a6a2cd5d8ee9534a97f232f553bcbb8f2ebc839406571a03a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBAGFNNZ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIBGjJzlF5s5Q39k7YZNowJWj9R1b7N8rRu1DJ%2Bb1QOplAiBwqzEsKeHL06cMJCiP%2BVmhGK95YxLx%2FGoA4uKo71rw7iqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAvPa1zoti3kUM3teKtwDCCOVHyjyzp0T8eOBxoTaX2f4S4quMtkGMA6M5AVeptgznqLma62KG9d3rvthegsCcdPM%2BRrFRHHBWB9KLpj2WuKuKZOafnqRN7b%2BYIqmupWYKUP9RflUqjnLXSONRLMrjebz2clpPsJj3H0T%2FuIRfM5gQf4Jut59Ovzn8w%2F3LC%2BjZ850QNok0Mh3LlvPdjbrCzis3t8zansASLr5CWMlgYe%2F4SXf9EfHJprqnq6L7mqD6g2lJIhE8ArDGNHOSkhc1Mgi4r1tu8dM42N%2BWr4EM2AzUclm%2FaGuNifxtZG1UOOM1c%2BNEiaRJT9Ey7YlFm96DWNzbYXEbDNMMFKagKYMJPMJR0ha4tGu9lgh1fI%2BbV%2FicnvF2s1T3xm%2F0sZaUMeARbZ9A5Tgkhmti%2FLh5Dd5d4cUpua%2F%2FNChSoo1%2FofgVJ6Nhij2nQG3Nrwo7CmaQ9aWcpBZHiwGu6XTXZgAV99NRwWMOfWnM79yODAhErphwGCOvFAaS9C0v8d%2FA89aOiW2x7lZFS1z4Q6FGryD1MWaZiM81elBaH9h4f1sIu4NeeH4BRW9TZmdUHiAqPVwkEVVQfoIVRp97VBzhbf3yWg6yPxlU2wdyHt3Azv367OwRM89dobnXbO%2FFYDvRYwwsPyhvwY6pgHdmhPDrr4%2F9sVdOWK8mdBKJUzEbqCCjx2OwOkp2UaNKnML318POFYOiiohBEWpFhpNyJSmlG5RD%2BSKRtpiF4pfh3eC2AWuHmvDaaIAWWMKeFBOhHkaD0L6WWbS33nCa4uysq4jm8LAxWidMvZUb729EKN5brVSTyfC7sgjt2FmCiPue4WMBkLwfWbQp1WPOwJcVVobiuvedbnFWdVHsbQ35QTqJ5lv&X-Amz-Signature=7d20cc7cec50c8f6694ed691627e8a8874d06f6f679d6094f2f5982b5e762281&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBAGFNNZ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIBGjJzlF5s5Q39k7YZNowJWj9R1b7N8rRu1DJ%2Bb1QOplAiBwqzEsKeHL06cMJCiP%2BVmhGK95YxLx%2FGoA4uKo71rw7iqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAvPa1zoti3kUM3teKtwDCCOVHyjyzp0T8eOBxoTaX2f4S4quMtkGMA6M5AVeptgznqLma62KG9d3rvthegsCcdPM%2BRrFRHHBWB9KLpj2WuKuKZOafnqRN7b%2BYIqmupWYKUP9RflUqjnLXSONRLMrjebz2clpPsJj3H0T%2FuIRfM5gQf4Jut59Ovzn8w%2F3LC%2BjZ850QNok0Mh3LlvPdjbrCzis3t8zansASLr5CWMlgYe%2F4SXf9EfHJprqnq6L7mqD6g2lJIhE8ArDGNHOSkhc1Mgi4r1tu8dM42N%2BWr4EM2AzUclm%2FaGuNifxtZG1UOOM1c%2BNEiaRJT9Ey7YlFm96DWNzbYXEbDNMMFKagKYMJPMJR0ha4tGu9lgh1fI%2BbV%2FicnvF2s1T3xm%2F0sZaUMeARbZ9A5Tgkhmti%2FLh5Dd5d4cUpua%2F%2FNChSoo1%2FofgVJ6Nhij2nQG3Nrwo7CmaQ9aWcpBZHiwGu6XTXZgAV99NRwWMOfWnM79yODAhErphwGCOvFAaS9C0v8d%2FA89aOiW2x7lZFS1z4Q6FGryD1MWaZiM81elBaH9h4f1sIu4NeeH4BRW9TZmdUHiAqPVwkEVVQfoIVRp97VBzhbf3yWg6yPxlU2wdyHt3Azv367OwRM89dobnXbO%2FFYDvRYwwsPyhvwY6pgHdmhPDrr4%2F9sVdOWK8mdBKJUzEbqCCjx2OwOkp2UaNKnML318POFYOiiohBEWpFhpNyJSmlG5RD%2BSKRtpiF4pfh3eC2AWuHmvDaaIAWWMKeFBOhHkaD0L6WWbS33nCa4uysq4jm8LAxWidMvZUb729EKN5brVSTyfC7sgjt2FmCiPue4WMBkLwfWbQp1WPOwJcVVobiuvedbnFWdVHsbQ35QTqJ5lv&X-Amz-Signature=75c13dea3a1677e644a81d1fcd3516e4db80540cca2a5265c6d6d098cdfdcc89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJCPSVOS%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIDEh29AdPGrJGz3ICBj56MZGjcaENh1sfLCJsu0uMy%2BlAiAI18MOlmHB2oDCOX4Kc2Cv0uwFfl6r046qakLHZfCHHSqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYzgs9xRUKte%2BFTW7KtwDgANT%2F0vZXRtK0iJ2T8NCPVYLfHSKcBkaJARdiL95DgkTyh5q7WlCNfT69TS%2BN4gIA5GP9nxrCKQqUjAJI0FpYkQRhKM%2BL%2BHHQgOlchLJ5%2BNIG%2BdpjgIWIiNFLayxLBqdjwRh7cAVIB%2FBiP4gvvmnujDzGoMINfvdtAhWZa%2BwBq93tAFANIeCbhQraDoQAI862hC5wCaxYGYa904fq9XhdaK6OF3M2sww1S%2B9N3K%2Fpzb0LHf2Cttdv7VjwJBkNJbIXSBPWK4GcSBUu2mtqC9lrLBUFbQ7r6vgWD8RN0UWbyfQH2C3YVpAfflf1fFWRSS7Dv4w6iJhWsvv2e8fbvwSBAK6WT6TdbquAllXBgiicvLRleoj%2FikrQ1%2FOH6GjY5FUfOqD8Pzxiis6UKqrfF37MuEOn32vZHqcH2djDLDFssGnsyYQW3afSfL7mJhN7GWgJbbkFdBz1rtrkltVLSy7JcxtRNXIGPhj64BGg0cLsQtkn1YY9fuFUd%2BV5kNtek5l0TAN8udekxg2u72a71QjbvuG8GNdY5KZz8OUJ2pVAhGk%2B6mwlQGJcsHjXcoQs1%2BtjH3o43S%2BDp%2B3FxFntCRLKbAhrBH3I9o3xbaF8A1cr6d3JkLYFs6PmGtnAPgwvfyhvwY6pgE0sw5d6gReCjbtxrnCuWoVwqn2ZjQYCORAyoL1Ts9J7Oopj7KdUggB7Cd%2FzB71R5DdIAoPQz8o3Y9WlGufevAT%2F1N8mxERWfRr6seVGeUAVPxD9V9%2BrubllYOcnj0bpUukQJ3zF3uyNHiDUQ6IWUB5WU%2FllpU6xfB58iBZNUi9%2FLRd9diwTxLB2s60UI30UvLG9%2FATI%2Fnnq3jU%2BZ84E50NqGMpLErN&X-Amz-Signature=4b1f03270936d8d1880939e52a8df0244fce3bd787b17cf7e3d27f566a4f4bd8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJCPSVOS%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIDEh29AdPGrJGz3ICBj56MZGjcaENh1sfLCJsu0uMy%2BlAiAI18MOlmHB2oDCOX4Kc2Cv0uwFfl6r046qakLHZfCHHSqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYzgs9xRUKte%2BFTW7KtwDgANT%2F0vZXRtK0iJ2T8NCPVYLfHSKcBkaJARdiL95DgkTyh5q7WlCNfT69TS%2BN4gIA5GP9nxrCKQqUjAJI0FpYkQRhKM%2BL%2BHHQgOlchLJ5%2BNIG%2BdpjgIWIiNFLayxLBqdjwRh7cAVIB%2FBiP4gvvmnujDzGoMINfvdtAhWZa%2BwBq93tAFANIeCbhQraDoQAI862hC5wCaxYGYa904fq9XhdaK6OF3M2sww1S%2B9N3K%2Fpzb0LHf2Cttdv7VjwJBkNJbIXSBPWK4GcSBUu2mtqC9lrLBUFbQ7r6vgWD8RN0UWbyfQH2C3YVpAfflf1fFWRSS7Dv4w6iJhWsvv2e8fbvwSBAK6WT6TdbquAllXBgiicvLRleoj%2FikrQ1%2FOH6GjY5FUfOqD8Pzxiis6UKqrfF37MuEOn32vZHqcH2djDLDFssGnsyYQW3afSfL7mJhN7GWgJbbkFdBz1rtrkltVLSy7JcxtRNXIGPhj64BGg0cLsQtkn1YY9fuFUd%2BV5kNtek5l0TAN8udekxg2u72a71QjbvuG8GNdY5KZz8OUJ2pVAhGk%2B6mwlQGJcsHjXcoQs1%2BtjH3o43S%2BDp%2B3FxFntCRLKbAhrBH3I9o3xbaF8A1cr6d3JkLYFs6PmGtnAPgwvfyhvwY6pgE0sw5d6gReCjbtxrnCuWoVwqn2ZjQYCORAyoL1Ts9J7Oopj7KdUggB7Cd%2FzB71R5DdIAoPQz8o3Y9WlGufevAT%2F1N8mxERWfRr6seVGeUAVPxD9V9%2BrubllYOcnj0bpUukQJ3zF3uyNHiDUQ6IWUB5WU%2FllpU6xfB58iBZNUi9%2FLRd9diwTxLB2s60UI30UvLG9%2FATI%2Fnnq3jU%2BZ84E50NqGMpLErN&X-Amz-Signature=f4f408ad9609b1e2a280821b2d2f5765b00ad5031229ee01b5f63335e3c3f62c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
