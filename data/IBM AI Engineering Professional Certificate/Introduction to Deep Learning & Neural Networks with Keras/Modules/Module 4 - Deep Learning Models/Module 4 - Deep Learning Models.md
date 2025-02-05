

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z7YJOHR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCmphJA0T8qRxe88%2B%2FK0DRJ5tuv9wVbL%2F0MR3KBNhD46wIgPd8ddFPf%2BXY0u5%2FNkjKiKcrVxYkr0QqR9jLETcbGQsUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPVlqOskkG8DPkV5yircAyxqnxx%2F%2B9Z3lmLjMHDndu4cRFg7avXw%2BtUMZ7aGBHjjC%2Bu421uNR5Y8%2FIHFakSfgNWlJUkD%2FFBhFwdJi4AZ0Dk%2FkS8ayFnCO3xBSNaL4dgoAe6OB32OuOasieQTGUjZ3U3yuwBvLkw6oZLWLqW5G8vAN41yMfEoOheW9cFZqQdueP%2BMwIu9J%2F5XBCjuivrqy2uuktPgSzsY3RMILUpPikeMhTmNcCHtosgN0qvQAWfYDfd2ImbRwdStvzAkIKm3IvWotwhayKW3NpPOgnzBP1C9ASu0bn4ovF7zbVRwpRDwtQVacQet3gkyDv%2BfgVwdsR8d9AVH7DppwQZcx28sMMEQE0wVJf26g%2BPNrLxtEnSsozGP0SP9WlOXimH0NIXrFmAp23C4Zvv9DV05m2iFFDsaqk8s5tHyKUCyF%2F4w3S3aBjsJyQY4cQadqmii8R6N8JPftGATt2yPLzg4L3%2BoJhFqtULM%2FmJvOQLc%2FiyAMUtLzKt2OvJgGebNxWx%2BgZCK0M7tIeWV%2FxSdV2jrsSN1pNIN0LyY6rkpH4GLz5uJBGYKvq8RYvYoByoGdsBuCzLPoj4IUXmJ7VEwNTTJ0dr6M%2FmtiVz8teIUmyQTBdmkbHGoa4mYuNCKsNsRULlkMJu6jr0GOqUBq%2FbEFqFKnJj5%2F%2F6bvCrUdI4N%2FICRaPf5V10PKULN2lVcaO0t91joZTMEHnvcnknNUkm9xLBWQU6c%2BwUnnhkqqZnPKLqh3fsIqYW7pI%2BL18BL%2F9KqGVGS%2FFtxaJ%2FM%2BsOtNSJGw8X%2FizK52L2dm6rgKJv3%2BOTpIe3pYqPgp3YdfhvB0ouuzsfspOq9opNWThKh2XiGK0ReAv4APl4EhOgmXyhG%2FoAD&X-Amz-Signature=ad4da8747d6f7dc322c1dd9fee6ac1b4aa54d4ee238a5a34898d5f3dd1c19ceb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z7YJOHR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCmphJA0T8qRxe88%2B%2FK0DRJ5tuv9wVbL%2F0MR3KBNhD46wIgPd8ddFPf%2BXY0u5%2FNkjKiKcrVxYkr0QqR9jLETcbGQsUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPVlqOskkG8DPkV5yircAyxqnxx%2F%2B9Z3lmLjMHDndu4cRFg7avXw%2BtUMZ7aGBHjjC%2Bu421uNR5Y8%2FIHFakSfgNWlJUkD%2FFBhFwdJi4AZ0Dk%2FkS8ayFnCO3xBSNaL4dgoAe6OB32OuOasieQTGUjZ3U3yuwBvLkw6oZLWLqW5G8vAN41yMfEoOheW9cFZqQdueP%2BMwIu9J%2F5XBCjuivrqy2uuktPgSzsY3RMILUpPikeMhTmNcCHtosgN0qvQAWfYDfd2ImbRwdStvzAkIKm3IvWotwhayKW3NpPOgnzBP1C9ASu0bn4ovF7zbVRwpRDwtQVacQet3gkyDv%2BfgVwdsR8d9AVH7DppwQZcx28sMMEQE0wVJf26g%2BPNrLxtEnSsozGP0SP9WlOXimH0NIXrFmAp23C4Zvv9DV05m2iFFDsaqk8s5tHyKUCyF%2F4w3S3aBjsJyQY4cQadqmii8R6N8JPftGATt2yPLzg4L3%2BoJhFqtULM%2FmJvOQLc%2FiyAMUtLzKt2OvJgGebNxWx%2BgZCK0M7tIeWV%2FxSdV2jrsSN1pNIN0LyY6rkpH4GLz5uJBGYKvq8RYvYoByoGdsBuCzLPoj4IUXmJ7VEwNTTJ0dr6M%2FmtiVz8teIUmyQTBdmkbHGoa4mYuNCKsNsRULlkMJu6jr0GOqUBq%2FbEFqFKnJj5%2F%2F6bvCrUdI4N%2FICRaPf5V10PKULN2lVcaO0t91joZTMEHnvcnknNUkm9xLBWQU6c%2BwUnnhkqqZnPKLqh3fsIqYW7pI%2BL18BL%2F9KqGVGS%2FFtxaJ%2FM%2BsOtNSJGw8X%2FizK52L2dm6rgKJv3%2BOTpIe3pYqPgp3YdfhvB0ouuzsfspOq9opNWThKh2XiGK0ReAv4APl4EhOgmXyhG%2FoAD&X-Amz-Signature=11e5ac9e8dc39055924ab38dcfa8a28eb2d10d73121dd69cbba1645c9e995608&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z7YJOHR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCmphJA0T8qRxe88%2B%2FK0DRJ5tuv9wVbL%2F0MR3KBNhD46wIgPd8ddFPf%2BXY0u5%2FNkjKiKcrVxYkr0QqR9jLETcbGQsUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPVlqOskkG8DPkV5yircAyxqnxx%2F%2B9Z3lmLjMHDndu4cRFg7avXw%2BtUMZ7aGBHjjC%2Bu421uNR5Y8%2FIHFakSfgNWlJUkD%2FFBhFwdJi4AZ0Dk%2FkS8ayFnCO3xBSNaL4dgoAe6OB32OuOasieQTGUjZ3U3yuwBvLkw6oZLWLqW5G8vAN41yMfEoOheW9cFZqQdueP%2BMwIu9J%2F5XBCjuivrqy2uuktPgSzsY3RMILUpPikeMhTmNcCHtosgN0qvQAWfYDfd2ImbRwdStvzAkIKm3IvWotwhayKW3NpPOgnzBP1C9ASu0bn4ovF7zbVRwpRDwtQVacQet3gkyDv%2BfgVwdsR8d9AVH7DppwQZcx28sMMEQE0wVJf26g%2BPNrLxtEnSsozGP0SP9WlOXimH0NIXrFmAp23C4Zvv9DV05m2iFFDsaqk8s5tHyKUCyF%2F4w3S3aBjsJyQY4cQadqmii8R6N8JPftGATt2yPLzg4L3%2BoJhFqtULM%2FmJvOQLc%2FiyAMUtLzKt2OvJgGebNxWx%2BgZCK0M7tIeWV%2FxSdV2jrsSN1pNIN0LyY6rkpH4GLz5uJBGYKvq8RYvYoByoGdsBuCzLPoj4IUXmJ7VEwNTTJ0dr6M%2FmtiVz8teIUmyQTBdmkbHGoa4mYuNCKsNsRULlkMJu6jr0GOqUBq%2FbEFqFKnJj5%2F%2F6bvCrUdI4N%2FICRaPf5V10PKULN2lVcaO0t91joZTMEHnvcnknNUkm9xLBWQU6c%2BwUnnhkqqZnPKLqh3fsIqYW7pI%2BL18BL%2F9KqGVGS%2FFtxaJ%2FM%2BsOtNSJGw8X%2FizK52L2dm6rgKJv3%2BOTpIe3pYqPgp3YdfhvB0ouuzsfspOq9opNWThKh2XiGK0ReAv4APl4EhOgmXyhG%2FoAD&X-Amz-Signature=227a2d1a8e69f3c6edf4eed42c554b0ac7137a2b492f42e1355f8b61b3eaf9e6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z7YJOHR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCmphJA0T8qRxe88%2B%2FK0DRJ5tuv9wVbL%2F0MR3KBNhD46wIgPd8ddFPf%2BXY0u5%2FNkjKiKcrVxYkr0QqR9jLETcbGQsUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPVlqOskkG8DPkV5yircAyxqnxx%2F%2B9Z3lmLjMHDndu4cRFg7avXw%2BtUMZ7aGBHjjC%2Bu421uNR5Y8%2FIHFakSfgNWlJUkD%2FFBhFwdJi4AZ0Dk%2FkS8ayFnCO3xBSNaL4dgoAe6OB32OuOasieQTGUjZ3U3yuwBvLkw6oZLWLqW5G8vAN41yMfEoOheW9cFZqQdueP%2BMwIu9J%2F5XBCjuivrqy2uuktPgSzsY3RMILUpPikeMhTmNcCHtosgN0qvQAWfYDfd2ImbRwdStvzAkIKm3IvWotwhayKW3NpPOgnzBP1C9ASu0bn4ovF7zbVRwpRDwtQVacQet3gkyDv%2BfgVwdsR8d9AVH7DppwQZcx28sMMEQE0wVJf26g%2BPNrLxtEnSsozGP0SP9WlOXimH0NIXrFmAp23C4Zvv9DV05m2iFFDsaqk8s5tHyKUCyF%2F4w3S3aBjsJyQY4cQadqmii8R6N8JPftGATt2yPLzg4L3%2BoJhFqtULM%2FmJvOQLc%2FiyAMUtLzKt2OvJgGebNxWx%2BgZCK0M7tIeWV%2FxSdV2jrsSN1pNIN0LyY6rkpH4GLz5uJBGYKvq8RYvYoByoGdsBuCzLPoj4IUXmJ7VEwNTTJ0dr6M%2FmtiVz8teIUmyQTBdmkbHGoa4mYuNCKsNsRULlkMJu6jr0GOqUBq%2FbEFqFKnJj5%2F%2F6bvCrUdI4N%2FICRaPf5V10PKULN2lVcaO0t91joZTMEHnvcnknNUkm9xLBWQU6c%2BwUnnhkqqZnPKLqh3fsIqYW7pI%2BL18BL%2F9KqGVGS%2FFtxaJ%2FM%2BsOtNSJGw8X%2FizK52L2dm6rgKJv3%2BOTpIe3pYqPgp3YdfhvB0ouuzsfspOq9opNWThKh2XiGK0ReAv4APl4EhOgmXyhG%2FoAD&X-Amz-Signature=08ba031d3cdd882a4543ff74f0863bd1350f65cca822ce998f96b4ac8b900c27&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z7YJOHR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCmphJA0T8qRxe88%2B%2FK0DRJ5tuv9wVbL%2F0MR3KBNhD46wIgPd8ddFPf%2BXY0u5%2FNkjKiKcrVxYkr0QqR9jLETcbGQsUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPVlqOskkG8DPkV5yircAyxqnxx%2F%2B9Z3lmLjMHDndu4cRFg7avXw%2BtUMZ7aGBHjjC%2Bu421uNR5Y8%2FIHFakSfgNWlJUkD%2FFBhFwdJi4AZ0Dk%2FkS8ayFnCO3xBSNaL4dgoAe6OB32OuOasieQTGUjZ3U3yuwBvLkw6oZLWLqW5G8vAN41yMfEoOheW9cFZqQdueP%2BMwIu9J%2F5XBCjuivrqy2uuktPgSzsY3RMILUpPikeMhTmNcCHtosgN0qvQAWfYDfd2ImbRwdStvzAkIKm3IvWotwhayKW3NpPOgnzBP1C9ASu0bn4ovF7zbVRwpRDwtQVacQet3gkyDv%2BfgVwdsR8d9AVH7DppwQZcx28sMMEQE0wVJf26g%2BPNrLxtEnSsozGP0SP9WlOXimH0NIXrFmAp23C4Zvv9DV05m2iFFDsaqk8s5tHyKUCyF%2F4w3S3aBjsJyQY4cQadqmii8R6N8JPftGATt2yPLzg4L3%2BoJhFqtULM%2FmJvOQLc%2FiyAMUtLzKt2OvJgGebNxWx%2BgZCK0M7tIeWV%2FxSdV2jrsSN1pNIN0LyY6rkpH4GLz5uJBGYKvq8RYvYoByoGdsBuCzLPoj4IUXmJ7VEwNTTJ0dr6M%2FmtiVz8teIUmyQTBdmkbHGoa4mYuNCKsNsRULlkMJu6jr0GOqUBq%2FbEFqFKnJj5%2F%2F6bvCrUdI4N%2FICRaPf5V10PKULN2lVcaO0t91joZTMEHnvcnknNUkm9xLBWQU6c%2BwUnnhkqqZnPKLqh3fsIqYW7pI%2BL18BL%2F9KqGVGS%2FFtxaJ%2FM%2BsOtNSJGw8X%2FizK52L2dm6rgKJv3%2BOTpIe3pYqPgp3YdfhvB0ouuzsfspOq9opNWThKh2XiGK0ReAv4APl4EhOgmXyhG%2FoAD&X-Amz-Signature=f39a29cf78dda952b384df18c442df6c253ce403e30b294cdda1ecd649a2792f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z7YJOHR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCmphJA0T8qRxe88%2B%2FK0DRJ5tuv9wVbL%2F0MR3KBNhD46wIgPd8ddFPf%2BXY0u5%2FNkjKiKcrVxYkr0QqR9jLETcbGQsUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPVlqOskkG8DPkV5yircAyxqnxx%2F%2B9Z3lmLjMHDndu4cRFg7avXw%2BtUMZ7aGBHjjC%2Bu421uNR5Y8%2FIHFakSfgNWlJUkD%2FFBhFwdJi4AZ0Dk%2FkS8ayFnCO3xBSNaL4dgoAe6OB32OuOasieQTGUjZ3U3yuwBvLkw6oZLWLqW5G8vAN41yMfEoOheW9cFZqQdueP%2BMwIu9J%2F5XBCjuivrqy2uuktPgSzsY3RMILUpPikeMhTmNcCHtosgN0qvQAWfYDfd2ImbRwdStvzAkIKm3IvWotwhayKW3NpPOgnzBP1C9ASu0bn4ovF7zbVRwpRDwtQVacQet3gkyDv%2BfgVwdsR8d9AVH7DppwQZcx28sMMEQE0wVJf26g%2BPNrLxtEnSsozGP0SP9WlOXimH0NIXrFmAp23C4Zvv9DV05m2iFFDsaqk8s5tHyKUCyF%2F4w3S3aBjsJyQY4cQadqmii8R6N8JPftGATt2yPLzg4L3%2BoJhFqtULM%2FmJvOQLc%2FiyAMUtLzKt2OvJgGebNxWx%2BgZCK0M7tIeWV%2FxSdV2jrsSN1pNIN0LyY6rkpH4GLz5uJBGYKvq8RYvYoByoGdsBuCzLPoj4IUXmJ7VEwNTTJ0dr6M%2FmtiVz8teIUmyQTBdmkbHGoa4mYuNCKsNsRULlkMJu6jr0GOqUBq%2FbEFqFKnJj5%2F%2F6bvCrUdI4N%2FICRaPf5V10PKULN2lVcaO0t91joZTMEHnvcnknNUkm9xLBWQU6c%2BwUnnhkqqZnPKLqh3fsIqYW7pI%2BL18BL%2F9KqGVGS%2FFtxaJ%2FM%2BsOtNSJGw8X%2FizK52L2dm6rgKJv3%2BOTpIe3pYqPgp3YdfhvB0ouuzsfspOq9opNWThKh2XiGK0ReAv4APl4EhOgmXyhG%2FoAD&X-Amz-Signature=b25f8c5af9b9772ac5ae49d0b1b8c556521df94b17feedc81cf53fdff5c36e1a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z7YJOHR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCmphJA0T8qRxe88%2B%2FK0DRJ5tuv9wVbL%2F0MR3KBNhD46wIgPd8ddFPf%2BXY0u5%2FNkjKiKcrVxYkr0QqR9jLETcbGQsUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPVlqOskkG8DPkV5yircAyxqnxx%2F%2B9Z3lmLjMHDndu4cRFg7avXw%2BtUMZ7aGBHjjC%2Bu421uNR5Y8%2FIHFakSfgNWlJUkD%2FFBhFwdJi4AZ0Dk%2FkS8ayFnCO3xBSNaL4dgoAe6OB32OuOasieQTGUjZ3U3yuwBvLkw6oZLWLqW5G8vAN41yMfEoOheW9cFZqQdueP%2BMwIu9J%2F5XBCjuivrqy2uuktPgSzsY3RMILUpPikeMhTmNcCHtosgN0qvQAWfYDfd2ImbRwdStvzAkIKm3IvWotwhayKW3NpPOgnzBP1C9ASu0bn4ovF7zbVRwpRDwtQVacQet3gkyDv%2BfgVwdsR8d9AVH7DppwQZcx28sMMEQE0wVJf26g%2BPNrLxtEnSsozGP0SP9WlOXimH0NIXrFmAp23C4Zvv9DV05m2iFFDsaqk8s5tHyKUCyF%2F4w3S3aBjsJyQY4cQadqmii8R6N8JPftGATt2yPLzg4L3%2BoJhFqtULM%2FmJvOQLc%2FiyAMUtLzKt2OvJgGebNxWx%2BgZCK0M7tIeWV%2FxSdV2jrsSN1pNIN0LyY6rkpH4GLz5uJBGYKvq8RYvYoByoGdsBuCzLPoj4IUXmJ7VEwNTTJ0dr6M%2FmtiVz8teIUmyQTBdmkbHGoa4mYuNCKsNsRULlkMJu6jr0GOqUBq%2FbEFqFKnJj5%2F%2F6bvCrUdI4N%2FICRaPf5V10PKULN2lVcaO0t91joZTMEHnvcnknNUkm9xLBWQU6c%2BwUnnhkqqZnPKLqh3fsIqYW7pI%2BL18BL%2F9KqGVGS%2FFtxaJ%2FM%2BsOtNSJGw8X%2FizK52L2dm6rgKJv3%2BOTpIe3pYqPgp3YdfhvB0ouuzsfspOq9opNWThKh2XiGK0ReAv4APl4EhOgmXyhG%2FoAD&X-Amz-Signature=f88aff546ab46ff47cc3c39d4d2dc847287020e137aff3825f32b70df61eb8a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z7YJOHR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCmphJA0T8qRxe88%2B%2FK0DRJ5tuv9wVbL%2F0MR3KBNhD46wIgPd8ddFPf%2BXY0u5%2FNkjKiKcrVxYkr0QqR9jLETcbGQsUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPVlqOskkG8DPkV5yircAyxqnxx%2F%2B9Z3lmLjMHDndu4cRFg7avXw%2BtUMZ7aGBHjjC%2Bu421uNR5Y8%2FIHFakSfgNWlJUkD%2FFBhFwdJi4AZ0Dk%2FkS8ayFnCO3xBSNaL4dgoAe6OB32OuOasieQTGUjZ3U3yuwBvLkw6oZLWLqW5G8vAN41yMfEoOheW9cFZqQdueP%2BMwIu9J%2F5XBCjuivrqy2uuktPgSzsY3RMILUpPikeMhTmNcCHtosgN0qvQAWfYDfd2ImbRwdStvzAkIKm3IvWotwhayKW3NpPOgnzBP1C9ASu0bn4ovF7zbVRwpRDwtQVacQet3gkyDv%2BfgVwdsR8d9AVH7DppwQZcx28sMMEQE0wVJf26g%2BPNrLxtEnSsozGP0SP9WlOXimH0NIXrFmAp23C4Zvv9DV05m2iFFDsaqk8s5tHyKUCyF%2F4w3S3aBjsJyQY4cQadqmii8R6N8JPftGATt2yPLzg4L3%2BoJhFqtULM%2FmJvOQLc%2FiyAMUtLzKt2OvJgGebNxWx%2BgZCK0M7tIeWV%2FxSdV2jrsSN1pNIN0LyY6rkpH4GLz5uJBGYKvq8RYvYoByoGdsBuCzLPoj4IUXmJ7VEwNTTJ0dr6M%2FmtiVz8teIUmyQTBdmkbHGoa4mYuNCKsNsRULlkMJu6jr0GOqUBq%2FbEFqFKnJj5%2F%2F6bvCrUdI4N%2FICRaPf5V10PKULN2lVcaO0t91joZTMEHnvcnknNUkm9xLBWQU6c%2BwUnnhkqqZnPKLqh3fsIqYW7pI%2BL18BL%2F9KqGVGS%2FFtxaJ%2FM%2BsOtNSJGw8X%2FizK52L2dm6rgKJv3%2BOTpIe3pYqPgp3YdfhvB0ouuzsfspOq9opNWThKh2XiGK0ReAv4APl4EhOgmXyhG%2FoAD&X-Amz-Signature=d077ef68bd60044f4113736d5d28a934c0b78c7ec7fd7f9fb0f3d1b766dcddbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z7YJOHR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCmphJA0T8qRxe88%2B%2FK0DRJ5tuv9wVbL%2F0MR3KBNhD46wIgPd8ddFPf%2BXY0u5%2FNkjKiKcrVxYkr0QqR9jLETcbGQsUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPVlqOskkG8DPkV5yircAyxqnxx%2F%2B9Z3lmLjMHDndu4cRFg7avXw%2BtUMZ7aGBHjjC%2Bu421uNR5Y8%2FIHFakSfgNWlJUkD%2FFBhFwdJi4AZ0Dk%2FkS8ayFnCO3xBSNaL4dgoAe6OB32OuOasieQTGUjZ3U3yuwBvLkw6oZLWLqW5G8vAN41yMfEoOheW9cFZqQdueP%2BMwIu9J%2F5XBCjuivrqy2uuktPgSzsY3RMILUpPikeMhTmNcCHtosgN0qvQAWfYDfd2ImbRwdStvzAkIKm3IvWotwhayKW3NpPOgnzBP1C9ASu0bn4ovF7zbVRwpRDwtQVacQet3gkyDv%2BfgVwdsR8d9AVH7DppwQZcx28sMMEQE0wVJf26g%2BPNrLxtEnSsozGP0SP9WlOXimH0NIXrFmAp23C4Zvv9DV05m2iFFDsaqk8s5tHyKUCyF%2F4w3S3aBjsJyQY4cQadqmii8R6N8JPftGATt2yPLzg4L3%2BoJhFqtULM%2FmJvOQLc%2FiyAMUtLzKt2OvJgGebNxWx%2BgZCK0M7tIeWV%2FxSdV2jrsSN1pNIN0LyY6rkpH4GLz5uJBGYKvq8RYvYoByoGdsBuCzLPoj4IUXmJ7VEwNTTJ0dr6M%2FmtiVz8teIUmyQTBdmkbHGoa4mYuNCKsNsRULlkMJu6jr0GOqUBq%2FbEFqFKnJj5%2F%2F6bvCrUdI4N%2FICRaPf5V10PKULN2lVcaO0t91joZTMEHnvcnknNUkm9xLBWQU6c%2BwUnnhkqqZnPKLqh3fsIqYW7pI%2BL18BL%2F9KqGVGS%2FFtxaJ%2FM%2BsOtNSJGw8X%2FizK52L2dm6rgKJv3%2BOTpIe3pYqPgp3YdfhvB0ouuzsfspOq9opNWThKh2XiGK0ReAv4APl4EhOgmXyhG%2FoAD&X-Amz-Signature=22104f1bbdcc6c409d35bd968c7937837479d49bbcda39b789ec1224135af951&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IJ7EZKU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIE%2BDCF%2BoSjWd0zLz2OzzskoUgjLISMgEgTQbanWhc8sQAiEAyrHxE92zckcDcqwHD9LUhXFxRz%2BTEHwep8%2FQ64K4X0oq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDJH5yGGR3rqohfTtuyrcAwxNQe65IbEkWfHqLNH88WYl45RFJjW06aZVr2E7%2Fmyy3h7wv%2FcZdbRWBZKJthHvLcbjbEPlwkbXcyogvBoPuLgN2D9cNt4PBbWwZJseKbIVOMOLYV7nRWlSEoRg7yhXgMIrAwznFxutRZTGdj%2Bdr02FLrZHCAgfOS3xgrvRoOEx06Zh80XcZzzPzXlbaunNAYV9eiIxsshQaKYtvH0qEeIlfpZPdT%2Bm%2B1J8wRvPxlM26bsBVRpFQBfKHilZUPCIE5leYxwEiNO5d%2FRnuqH16HfLFjqSurZDu8g9ASY7Ha5qs3Q0VZ979Joe90uHANH203mjHHDSg%2FnGwjL1bX2JIoC34%2B3KUzZVrnHMY5uzFtx7mMSkcjl2SmP5Or%2FR8qREEy%2Fqs2F2Wh3uoJQB5JFUfr6%2Bg78Db1neWF2LfCl36tsztbbbv7BycvzUraT4Vv3GkCMDLIgSWFc0fw0Le3r%2BxYwYQTa%2FOMFObqisHs42iIIEy93u57O26FIlGNhUuuhB0WxC5B0tE%2BxXkLUvvddQjLGSh7KisLrEUnx7WISqJ%2Frfn1cwAQOPtHl%2F6C6lD8Y9fMUbCnK0QyVS7VNyZrAq656mElK13E3%2Fh2ZeA8pPL8y6klgzSNHpHINuX21DMKO6jr0GOqUBW2w%2F%2Bb%2BTBp5qVtXkJsrulm9UoYtP%2B4mtw9EXKNVl4GtFWAf9i4J8ebo6z5NTnrhzANdf9iuoIS%2B5eLXO0pjs8uponryr%2Fz2u6AwuKDw%2BhH26NeZis7mQKWwzwbvBksdcMb2gj%2BULjeCGivS4ic25FjWuiESMJpHf3iarUtZfQOkjo99UoeOJlre7Mv94id0lfetLdOcMips1MHf1A1onsCFMikU0&X-Amz-Signature=69f1331e711b86c0d47c3d8f93921c91bf759f9a40ac8733f76a53d0ab3a0591&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IJ7EZKU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIE%2BDCF%2BoSjWd0zLz2OzzskoUgjLISMgEgTQbanWhc8sQAiEAyrHxE92zckcDcqwHD9LUhXFxRz%2BTEHwep8%2FQ64K4X0oq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDJH5yGGR3rqohfTtuyrcAwxNQe65IbEkWfHqLNH88WYl45RFJjW06aZVr2E7%2Fmyy3h7wv%2FcZdbRWBZKJthHvLcbjbEPlwkbXcyogvBoPuLgN2D9cNt4PBbWwZJseKbIVOMOLYV7nRWlSEoRg7yhXgMIrAwznFxutRZTGdj%2Bdr02FLrZHCAgfOS3xgrvRoOEx06Zh80XcZzzPzXlbaunNAYV9eiIxsshQaKYtvH0qEeIlfpZPdT%2Bm%2B1J8wRvPxlM26bsBVRpFQBfKHilZUPCIE5leYxwEiNO5d%2FRnuqH16HfLFjqSurZDu8g9ASY7Ha5qs3Q0VZ979Joe90uHANH203mjHHDSg%2FnGwjL1bX2JIoC34%2B3KUzZVrnHMY5uzFtx7mMSkcjl2SmP5Or%2FR8qREEy%2Fqs2F2Wh3uoJQB5JFUfr6%2Bg78Db1neWF2LfCl36tsztbbbv7BycvzUraT4Vv3GkCMDLIgSWFc0fw0Le3r%2BxYwYQTa%2FOMFObqisHs42iIIEy93u57O26FIlGNhUuuhB0WxC5B0tE%2BxXkLUvvddQjLGSh7KisLrEUnx7WISqJ%2Frfn1cwAQOPtHl%2F6C6lD8Y9fMUbCnK0QyVS7VNyZrAq656mElK13E3%2Fh2ZeA8pPL8y6klgzSNHpHINuX21DMKO6jr0GOqUBW2w%2F%2Bb%2BTBp5qVtXkJsrulm9UoYtP%2B4mtw9EXKNVl4GtFWAf9i4J8ebo6z5NTnrhzANdf9iuoIS%2B5eLXO0pjs8uponryr%2Fz2u6AwuKDw%2BhH26NeZis7mQKWwzwbvBksdcMb2gj%2BULjeCGivS4ic25FjWuiESMJpHf3iarUtZfQOkjo99UoeOJlre7Mv94id0lfetLdOcMips1MHf1A1onsCFMikU0&X-Amz-Signature=374950cf3e04044d3e31a00865854386dfd57fe67c37ce1722ab88a4c0253459&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
