

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KGR2DUY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC52FKhQaIFAmZcsWZoQfdQM4NRDBaRHgrcLDzypJsjLgIhANAuKip%2BoGDq8VHnJRHxEvjEpnY6%2BZ5TjmNVYr6deSoBKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8wNyPsjZAjUTO6oYq3AOP17UuBIYG1VqKMP%2FcJMJ8MbenKn5BVSwipmXricDNnYWAKR%2BuIqHQ6q1FD76fpJSKIqyoVc9qSzR93YJzCMp%2B1zCSQ2XJzI5GI8uhpBR1n23Tvta2Gfes%2B1vt4wDc2DqG55K03Ce2PM6pZaSEIurRvw8gIzaVtAXFnpKtUwvTaxMHoD6AoIueE7HR6lhrh2AJ8J7YJq51FjJoWXJbWkqZes83dVB6hnO%2FiLtuYKmcF7B1PfFsgjLyTUcPZDGWPj%2FqBjX0v6oEORLiMOw5PMDdjsq8QBIPbWOa1FznehlyFJ%2FktW3DIgmsNEO3QDeIjwPlc40GNEXJGDjffbeeqce7FYmHh3nqukA6uHk5xk8e%2B90ykNDM7FotZ79PmareV2BbiL3W2X67DJoN0KjOgGrJ6c8dF28TPUngNIsii4y96S62jiicWJnHqJ8mgGN63tQamh7yv92w7Ure%2BZYdbxppZiPnS1oVcegUBibbKmQI9xTn700fyOxxpyM%2BeG2nbNePO5QWgSslB%2Byg97jZTD4ITcC4uSvDiJEJtK1iy%2ByFRrMN1SYhje0cUAxxTeR9G7keBl9axNB9DizH7TuuD59gNu9X8ElY3RgYaDumd39I%2FPHobWv15IVQhV%2F6PjCAo%2By8BjqkAb6ECmElaW%2FWkxu8EBU3jehC%2BUVoObymhDomGKy6ijGnQBWCUPPPNW0TNt%2FWKDzib2v9a6NFZLOOhHVZHjZNlJzPLks3VldFADSw7vS7iCZpseSEKfDQMEQZN1Qi65vZEBCtBc%2FQ1fR7WRwUsxBUF83ETCAenvs3vfDAWrkh3Qp%2FkIrhscFfLB9FGEXD%2B9kZ5vFc5BdSDpupAIZ3QYhGvWwqexEF&X-Amz-Signature=5fa8b6179d41d82fb1de1fffb9827a5f4e4439b22fca92d2112b78104de4ba8f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KGR2DUY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC52FKhQaIFAmZcsWZoQfdQM4NRDBaRHgrcLDzypJsjLgIhANAuKip%2BoGDq8VHnJRHxEvjEpnY6%2BZ5TjmNVYr6deSoBKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8wNyPsjZAjUTO6oYq3AOP17UuBIYG1VqKMP%2FcJMJ8MbenKn5BVSwipmXricDNnYWAKR%2BuIqHQ6q1FD76fpJSKIqyoVc9qSzR93YJzCMp%2B1zCSQ2XJzI5GI8uhpBR1n23Tvta2Gfes%2B1vt4wDc2DqG55K03Ce2PM6pZaSEIurRvw8gIzaVtAXFnpKtUwvTaxMHoD6AoIueE7HR6lhrh2AJ8J7YJq51FjJoWXJbWkqZes83dVB6hnO%2FiLtuYKmcF7B1PfFsgjLyTUcPZDGWPj%2FqBjX0v6oEORLiMOw5PMDdjsq8QBIPbWOa1FznehlyFJ%2FktW3DIgmsNEO3QDeIjwPlc40GNEXJGDjffbeeqce7FYmHh3nqukA6uHk5xk8e%2B90ykNDM7FotZ79PmareV2BbiL3W2X67DJoN0KjOgGrJ6c8dF28TPUngNIsii4y96S62jiicWJnHqJ8mgGN63tQamh7yv92w7Ure%2BZYdbxppZiPnS1oVcegUBibbKmQI9xTn700fyOxxpyM%2BeG2nbNePO5QWgSslB%2Byg97jZTD4ITcC4uSvDiJEJtK1iy%2ByFRrMN1SYhje0cUAxxTeR9G7keBl9axNB9DizH7TuuD59gNu9X8ElY3RgYaDumd39I%2FPHobWv15IVQhV%2F6PjCAo%2By8BjqkAb6ECmElaW%2FWkxu8EBU3jehC%2BUVoObymhDomGKy6ijGnQBWCUPPPNW0TNt%2FWKDzib2v9a6NFZLOOhHVZHjZNlJzPLks3VldFADSw7vS7iCZpseSEKfDQMEQZN1Qi65vZEBCtBc%2FQ1fR7WRwUsxBUF83ETCAenvs3vfDAWrkh3Qp%2FkIrhscFfLB9FGEXD%2B9kZ5vFc5BdSDpupAIZ3QYhGvWwqexEF&X-Amz-Signature=05c82d6a025487a26a6b425b19509ab222dd00e2d736cdcb5ac7eaf498cbc62f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KGR2DUY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC52FKhQaIFAmZcsWZoQfdQM4NRDBaRHgrcLDzypJsjLgIhANAuKip%2BoGDq8VHnJRHxEvjEpnY6%2BZ5TjmNVYr6deSoBKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8wNyPsjZAjUTO6oYq3AOP17UuBIYG1VqKMP%2FcJMJ8MbenKn5BVSwipmXricDNnYWAKR%2BuIqHQ6q1FD76fpJSKIqyoVc9qSzR93YJzCMp%2B1zCSQ2XJzI5GI8uhpBR1n23Tvta2Gfes%2B1vt4wDc2DqG55K03Ce2PM6pZaSEIurRvw8gIzaVtAXFnpKtUwvTaxMHoD6AoIueE7HR6lhrh2AJ8J7YJq51FjJoWXJbWkqZes83dVB6hnO%2FiLtuYKmcF7B1PfFsgjLyTUcPZDGWPj%2FqBjX0v6oEORLiMOw5PMDdjsq8QBIPbWOa1FznehlyFJ%2FktW3DIgmsNEO3QDeIjwPlc40GNEXJGDjffbeeqce7FYmHh3nqukA6uHk5xk8e%2B90ykNDM7FotZ79PmareV2BbiL3W2X67DJoN0KjOgGrJ6c8dF28TPUngNIsii4y96S62jiicWJnHqJ8mgGN63tQamh7yv92w7Ure%2BZYdbxppZiPnS1oVcegUBibbKmQI9xTn700fyOxxpyM%2BeG2nbNePO5QWgSslB%2Byg97jZTD4ITcC4uSvDiJEJtK1iy%2ByFRrMN1SYhje0cUAxxTeR9G7keBl9axNB9DizH7TuuD59gNu9X8ElY3RgYaDumd39I%2FPHobWv15IVQhV%2F6PjCAo%2By8BjqkAb6ECmElaW%2FWkxu8EBU3jehC%2BUVoObymhDomGKy6ijGnQBWCUPPPNW0TNt%2FWKDzib2v9a6NFZLOOhHVZHjZNlJzPLks3VldFADSw7vS7iCZpseSEKfDQMEQZN1Qi65vZEBCtBc%2FQ1fR7WRwUsxBUF83ETCAenvs3vfDAWrkh3Qp%2FkIrhscFfLB9FGEXD%2B9kZ5vFc5BdSDpupAIZ3QYhGvWwqexEF&X-Amz-Signature=15076bcc71dcea8b7815708c371d0f162180661b70dda1d9501f005ac9fab914&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KGR2DUY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC52FKhQaIFAmZcsWZoQfdQM4NRDBaRHgrcLDzypJsjLgIhANAuKip%2BoGDq8VHnJRHxEvjEpnY6%2BZ5TjmNVYr6deSoBKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8wNyPsjZAjUTO6oYq3AOP17UuBIYG1VqKMP%2FcJMJ8MbenKn5BVSwipmXricDNnYWAKR%2BuIqHQ6q1FD76fpJSKIqyoVc9qSzR93YJzCMp%2B1zCSQ2XJzI5GI8uhpBR1n23Tvta2Gfes%2B1vt4wDc2DqG55K03Ce2PM6pZaSEIurRvw8gIzaVtAXFnpKtUwvTaxMHoD6AoIueE7HR6lhrh2AJ8J7YJq51FjJoWXJbWkqZes83dVB6hnO%2FiLtuYKmcF7B1PfFsgjLyTUcPZDGWPj%2FqBjX0v6oEORLiMOw5PMDdjsq8QBIPbWOa1FznehlyFJ%2FktW3DIgmsNEO3QDeIjwPlc40GNEXJGDjffbeeqce7FYmHh3nqukA6uHk5xk8e%2B90ykNDM7FotZ79PmareV2BbiL3W2X67DJoN0KjOgGrJ6c8dF28TPUngNIsii4y96S62jiicWJnHqJ8mgGN63tQamh7yv92w7Ure%2BZYdbxppZiPnS1oVcegUBibbKmQI9xTn700fyOxxpyM%2BeG2nbNePO5QWgSslB%2Byg97jZTD4ITcC4uSvDiJEJtK1iy%2ByFRrMN1SYhje0cUAxxTeR9G7keBl9axNB9DizH7TuuD59gNu9X8ElY3RgYaDumd39I%2FPHobWv15IVQhV%2F6PjCAo%2By8BjqkAb6ECmElaW%2FWkxu8EBU3jehC%2BUVoObymhDomGKy6ijGnQBWCUPPPNW0TNt%2FWKDzib2v9a6NFZLOOhHVZHjZNlJzPLks3VldFADSw7vS7iCZpseSEKfDQMEQZN1Qi65vZEBCtBc%2FQ1fR7WRwUsxBUF83ETCAenvs3vfDAWrkh3Qp%2FkIrhscFfLB9FGEXD%2B9kZ5vFc5BdSDpupAIZ3QYhGvWwqexEF&X-Amz-Signature=21c0ac695dd7a084cefd429b90e2087d12e90b94abde2f4531d7639f6293baf4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KGR2DUY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC52FKhQaIFAmZcsWZoQfdQM4NRDBaRHgrcLDzypJsjLgIhANAuKip%2BoGDq8VHnJRHxEvjEpnY6%2BZ5TjmNVYr6deSoBKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8wNyPsjZAjUTO6oYq3AOP17UuBIYG1VqKMP%2FcJMJ8MbenKn5BVSwipmXricDNnYWAKR%2BuIqHQ6q1FD76fpJSKIqyoVc9qSzR93YJzCMp%2B1zCSQ2XJzI5GI8uhpBR1n23Tvta2Gfes%2B1vt4wDc2DqG55K03Ce2PM6pZaSEIurRvw8gIzaVtAXFnpKtUwvTaxMHoD6AoIueE7HR6lhrh2AJ8J7YJq51FjJoWXJbWkqZes83dVB6hnO%2FiLtuYKmcF7B1PfFsgjLyTUcPZDGWPj%2FqBjX0v6oEORLiMOw5PMDdjsq8QBIPbWOa1FznehlyFJ%2FktW3DIgmsNEO3QDeIjwPlc40GNEXJGDjffbeeqce7FYmHh3nqukA6uHk5xk8e%2B90ykNDM7FotZ79PmareV2BbiL3W2X67DJoN0KjOgGrJ6c8dF28TPUngNIsii4y96S62jiicWJnHqJ8mgGN63tQamh7yv92w7Ure%2BZYdbxppZiPnS1oVcegUBibbKmQI9xTn700fyOxxpyM%2BeG2nbNePO5QWgSslB%2Byg97jZTD4ITcC4uSvDiJEJtK1iy%2ByFRrMN1SYhje0cUAxxTeR9G7keBl9axNB9DizH7TuuD59gNu9X8ElY3RgYaDumd39I%2FPHobWv15IVQhV%2F6PjCAo%2By8BjqkAb6ECmElaW%2FWkxu8EBU3jehC%2BUVoObymhDomGKy6ijGnQBWCUPPPNW0TNt%2FWKDzib2v9a6NFZLOOhHVZHjZNlJzPLks3VldFADSw7vS7iCZpseSEKfDQMEQZN1Qi65vZEBCtBc%2FQ1fR7WRwUsxBUF83ETCAenvs3vfDAWrkh3Qp%2FkIrhscFfLB9FGEXD%2B9kZ5vFc5BdSDpupAIZ3QYhGvWwqexEF&X-Amz-Signature=0dbc3a47cf8adba4e3a1bf53b64c9292eb92e4c757e578acd874666d12d6f835&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KGR2DUY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC52FKhQaIFAmZcsWZoQfdQM4NRDBaRHgrcLDzypJsjLgIhANAuKip%2BoGDq8VHnJRHxEvjEpnY6%2BZ5TjmNVYr6deSoBKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8wNyPsjZAjUTO6oYq3AOP17UuBIYG1VqKMP%2FcJMJ8MbenKn5BVSwipmXricDNnYWAKR%2BuIqHQ6q1FD76fpJSKIqyoVc9qSzR93YJzCMp%2B1zCSQ2XJzI5GI8uhpBR1n23Tvta2Gfes%2B1vt4wDc2DqG55K03Ce2PM6pZaSEIurRvw8gIzaVtAXFnpKtUwvTaxMHoD6AoIueE7HR6lhrh2AJ8J7YJq51FjJoWXJbWkqZes83dVB6hnO%2FiLtuYKmcF7B1PfFsgjLyTUcPZDGWPj%2FqBjX0v6oEORLiMOw5PMDdjsq8QBIPbWOa1FznehlyFJ%2FktW3DIgmsNEO3QDeIjwPlc40GNEXJGDjffbeeqce7FYmHh3nqukA6uHk5xk8e%2B90ykNDM7FotZ79PmareV2BbiL3W2X67DJoN0KjOgGrJ6c8dF28TPUngNIsii4y96S62jiicWJnHqJ8mgGN63tQamh7yv92w7Ure%2BZYdbxppZiPnS1oVcegUBibbKmQI9xTn700fyOxxpyM%2BeG2nbNePO5QWgSslB%2Byg97jZTD4ITcC4uSvDiJEJtK1iy%2ByFRrMN1SYhje0cUAxxTeR9G7keBl9axNB9DizH7TuuD59gNu9X8ElY3RgYaDumd39I%2FPHobWv15IVQhV%2F6PjCAo%2By8BjqkAb6ECmElaW%2FWkxu8EBU3jehC%2BUVoObymhDomGKy6ijGnQBWCUPPPNW0TNt%2FWKDzib2v9a6NFZLOOhHVZHjZNlJzPLks3VldFADSw7vS7iCZpseSEKfDQMEQZN1Qi65vZEBCtBc%2FQ1fR7WRwUsxBUF83ETCAenvs3vfDAWrkh3Qp%2FkIrhscFfLB9FGEXD%2B9kZ5vFc5BdSDpupAIZ3QYhGvWwqexEF&X-Amz-Signature=aff09800ca42e63d9e727afd1f810a417ffdb4010d634a54db5f6bf1e635d872&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KGR2DUY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC52FKhQaIFAmZcsWZoQfdQM4NRDBaRHgrcLDzypJsjLgIhANAuKip%2BoGDq8VHnJRHxEvjEpnY6%2BZ5TjmNVYr6deSoBKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8wNyPsjZAjUTO6oYq3AOP17UuBIYG1VqKMP%2FcJMJ8MbenKn5BVSwipmXricDNnYWAKR%2BuIqHQ6q1FD76fpJSKIqyoVc9qSzR93YJzCMp%2B1zCSQ2XJzI5GI8uhpBR1n23Tvta2Gfes%2B1vt4wDc2DqG55K03Ce2PM6pZaSEIurRvw8gIzaVtAXFnpKtUwvTaxMHoD6AoIueE7HR6lhrh2AJ8J7YJq51FjJoWXJbWkqZes83dVB6hnO%2FiLtuYKmcF7B1PfFsgjLyTUcPZDGWPj%2FqBjX0v6oEORLiMOw5PMDdjsq8QBIPbWOa1FznehlyFJ%2FktW3DIgmsNEO3QDeIjwPlc40GNEXJGDjffbeeqce7FYmHh3nqukA6uHk5xk8e%2B90ykNDM7FotZ79PmareV2BbiL3W2X67DJoN0KjOgGrJ6c8dF28TPUngNIsii4y96S62jiicWJnHqJ8mgGN63tQamh7yv92w7Ure%2BZYdbxppZiPnS1oVcegUBibbKmQI9xTn700fyOxxpyM%2BeG2nbNePO5QWgSslB%2Byg97jZTD4ITcC4uSvDiJEJtK1iy%2ByFRrMN1SYhje0cUAxxTeR9G7keBl9axNB9DizH7TuuD59gNu9X8ElY3RgYaDumd39I%2FPHobWv15IVQhV%2F6PjCAo%2By8BjqkAb6ECmElaW%2FWkxu8EBU3jehC%2BUVoObymhDomGKy6ijGnQBWCUPPPNW0TNt%2FWKDzib2v9a6NFZLOOhHVZHjZNlJzPLks3VldFADSw7vS7iCZpseSEKfDQMEQZN1Qi65vZEBCtBc%2FQ1fR7WRwUsxBUF83ETCAenvs3vfDAWrkh3Qp%2FkIrhscFfLB9FGEXD%2B9kZ5vFc5BdSDpupAIZ3QYhGvWwqexEF&X-Amz-Signature=486f3494d25ba4fd69d6a78f09d98c8d3910d4418b272b6acb69320d9e0e8365&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KGR2DUY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC52FKhQaIFAmZcsWZoQfdQM4NRDBaRHgrcLDzypJsjLgIhANAuKip%2BoGDq8VHnJRHxEvjEpnY6%2BZ5TjmNVYr6deSoBKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8wNyPsjZAjUTO6oYq3AOP17UuBIYG1VqKMP%2FcJMJ8MbenKn5BVSwipmXricDNnYWAKR%2BuIqHQ6q1FD76fpJSKIqyoVc9qSzR93YJzCMp%2B1zCSQ2XJzI5GI8uhpBR1n23Tvta2Gfes%2B1vt4wDc2DqG55K03Ce2PM6pZaSEIurRvw8gIzaVtAXFnpKtUwvTaxMHoD6AoIueE7HR6lhrh2AJ8J7YJq51FjJoWXJbWkqZes83dVB6hnO%2FiLtuYKmcF7B1PfFsgjLyTUcPZDGWPj%2FqBjX0v6oEORLiMOw5PMDdjsq8QBIPbWOa1FznehlyFJ%2FktW3DIgmsNEO3QDeIjwPlc40GNEXJGDjffbeeqce7FYmHh3nqukA6uHk5xk8e%2B90ykNDM7FotZ79PmareV2BbiL3W2X67DJoN0KjOgGrJ6c8dF28TPUngNIsii4y96S62jiicWJnHqJ8mgGN63tQamh7yv92w7Ure%2BZYdbxppZiPnS1oVcegUBibbKmQI9xTn700fyOxxpyM%2BeG2nbNePO5QWgSslB%2Byg97jZTD4ITcC4uSvDiJEJtK1iy%2ByFRrMN1SYhje0cUAxxTeR9G7keBl9axNB9DizH7TuuD59gNu9X8ElY3RgYaDumd39I%2FPHobWv15IVQhV%2F6PjCAo%2By8BjqkAb6ECmElaW%2FWkxu8EBU3jehC%2BUVoObymhDomGKy6ijGnQBWCUPPPNW0TNt%2FWKDzib2v9a6NFZLOOhHVZHjZNlJzPLks3VldFADSw7vS7iCZpseSEKfDQMEQZN1Qi65vZEBCtBc%2FQ1fR7WRwUsxBUF83ETCAenvs3vfDAWrkh3Qp%2FkIrhscFfLB9FGEXD%2B9kZ5vFc5BdSDpupAIZ3QYhGvWwqexEF&X-Amz-Signature=2492ffedb9b90783e0c85029b3da84845e918a536dc2736ea456619d7a5c6bd3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KGR2DUY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC52FKhQaIFAmZcsWZoQfdQM4NRDBaRHgrcLDzypJsjLgIhANAuKip%2BoGDq8VHnJRHxEvjEpnY6%2BZ5TjmNVYr6deSoBKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8wNyPsjZAjUTO6oYq3AOP17UuBIYG1VqKMP%2FcJMJ8MbenKn5BVSwipmXricDNnYWAKR%2BuIqHQ6q1FD76fpJSKIqyoVc9qSzR93YJzCMp%2B1zCSQ2XJzI5GI8uhpBR1n23Tvta2Gfes%2B1vt4wDc2DqG55K03Ce2PM6pZaSEIurRvw8gIzaVtAXFnpKtUwvTaxMHoD6AoIueE7HR6lhrh2AJ8J7YJq51FjJoWXJbWkqZes83dVB6hnO%2FiLtuYKmcF7B1PfFsgjLyTUcPZDGWPj%2FqBjX0v6oEORLiMOw5PMDdjsq8QBIPbWOa1FznehlyFJ%2FktW3DIgmsNEO3QDeIjwPlc40GNEXJGDjffbeeqce7FYmHh3nqukA6uHk5xk8e%2B90ykNDM7FotZ79PmareV2BbiL3W2X67DJoN0KjOgGrJ6c8dF28TPUngNIsii4y96S62jiicWJnHqJ8mgGN63tQamh7yv92w7Ure%2BZYdbxppZiPnS1oVcegUBibbKmQI9xTn700fyOxxpyM%2BeG2nbNePO5QWgSslB%2Byg97jZTD4ITcC4uSvDiJEJtK1iy%2ByFRrMN1SYhje0cUAxxTeR9G7keBl9axNB9DizH7TuuD59gNu9X8ElY3RgYaDumd39I%2FPHobWv15IVQhV%2F6PjCAo%2By8BjqkAb6ECmElaW%2FWkxu8EBU3jehC%2BUVoObymhDomGKy6ijGnQBWCUPPPNW0TNt%2FWKDzib2v9a6NFZLOOhHVZHjZNlJzPLks3VldFADSw7vS7iCZpseSEKfDQMEQZN1Qi65vZEBCtBc%2FQ1fR7WRwUsxBUF83ETCAenvs3vfDAWrkh3Qp%2FkIrhscFfLB9FGEXD%2B9kZ5vFc5BdSDpupAIZ3QYhGvWwqexEF&X-Amz-Signature=6fe780d359cedf009a0f7222ec62693572bf12471349386788dc2618ca24a317&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4JFONE3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1Kb29bJbPlkMsj7WfsxlRIdp%2BRzFDV77dqPGSxpIcTwIhAM1ueSUs2dKeDConKzpJX6JXmI%2FPJD%2FC%2BYiaD6tUGpU1KogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFzuCxCG38UGtHph4q3ANdOSQ%2Frpj3e%2F2jdEf72IEGDYFT1wg0GolYAOooCpWHhxsDwENyjK0M9Npl5pK1se9v2L4mVD4WVOLoXMJ8BHch%2B4%2BbYONtcniSGhwqn9LWYF5gVf%2B0hIarkorggoisIaMVVaPbGBr%2Bzus3zI%2FihOVtkjiQrgAfYL%2Fv4CL4epzLfDvHi%2FpBgPyYPRCdt7jTOE%2Biw2Z1lo6mgMQkvHaNI8SlNJUeJkXFJiRGt%2BDRUfndKldhL927pnDzuax%2Bu8JJ%2BFdSH477uuvErdx0DHFg5FvEjrk00Wqh84gawClfFwYCIWQ3aZOQEpXB8JWNcuuNJ%2F19LTnFAugg0g6wkbcnKFoyq4z4BC1ZRtsLh6x%2BpTjKjd0y8zDmJHBd0KDtktPlWXq99H9yY7COScqSShJEhi2gje3Ho9yJbCn8%2BAeYtGYNYxSGiBZ4c3WawJk7tTcoSeALyeZnHx529oKvL0yMh7u9Gum4j%2FP%2BOETf%2BMoNpuU3G6EYtX6PcMdGECdJT9Eipqxs97Ck9B%2Bvbviqy0qnpDkD%2FMEhuRZkssB5DxH84ExY3sZ1%2FxP6PnGE%2FN2lgabmZYTjqY%2F%2BNe6o93XdK1S9N2NtjUFTO3TL%2ByuakozjnurP%2BVOC6KMzi8LQ5dXF0jDPouy8BjqkAbwGlB1O5EWKMm4hQ%2FxIIY2dpjldpZtEA9BegyUEeu1hZ%2FhW9THBDG5Twz2XEqqKis8loNNrv6%2FXwe2Xnx9T7HvS4LBD39iEglN8uAoliMwa4e2OSXxxMgsQX18CdAnw%2FT%2FFlBf3AlbJAIpCj6qsLiw6xxiPrRNzdtYLt423wnoGR0zLwmF34FoXykG%2Bw9UIDPl1az6veWEMTHqHTPqyV9uXJGA2&X-Amz-Signature=92ee001c5113dc12673c02e38e9e5b54ffb102001ac564db02a5c177255cccb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4JFONE3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1Kb29bJbPlkMsj7WfsxlRIdp%2BRzFDV77dqPGSxpIcTwIhAM1ueSUs2dKeDConKzpJX6JXmI%2FPJD%2FC%2BYiaD6tUGpU1KogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFzuCxCG38UGtHph4q3ANdOSQ%2Frpj3e%2F2jdEf72IEGDYFT1wg0GolYAOooCpWHhxsDwENyjK0M9Npl5pK1se9v2L4mVD4WVOLoXMJ8BHch%2B4%2BbYONtcniSGhwqn9LWYF5gVf%2B0hIarkorggoisIaMVVaPbGBr%2Bzus3zI%2FihOVtkjiQrgAfYL%2Fv4CL4epzLfDvHi%2FpBgPyYPRCdt7jTOE%2Biw2Z1lo6mgMQkvHaNI8SlNJUeJkXFJiRGt%2BDRUfndKldhL927pnDzuax%2Bu8JJ%2BFdSH477uuvErdx0DHFg5FvEjrk00Wqh84gawClfFwYCIWQ3aZOQEpXB8JWNcuuNJ%2F19LTnFAugg0g6wkbcnKFoyq4z4BC1ZRtsLh6x%2BpTjKjd0y8zDmJHBd0KDtktPlWXq99H9yY7COScqSShJEhi2gje3Ho9yJbCn8%2BAeYtGYNYxSGiBZ4c3WawJk7tTcoSeALyeZnHx529oKvL0yMh7u9Gum4j%2FP%2BOETf%2BMoNpuU3G6EYtX6PcMdGECdJT9Eipqxs97Ck9B%2Bvbviqy0qnpDkD%2FMEhuRZkssB5DxH84ExY3sZ1%2FxP6PnGE%2FN2lgabmZYTjqY%2F%2BNe6o93XdK1S9N2NtjUFTO3TL%2ByuakozjnurP%2BVOC6KMzi8LQ5dXF0jDPouy8BjqkAbwGlB1O5EWKMm4hQ%2FxIIY2dpjldpZtEA9BegyUEeu1hZ%2FhW9THBDG5Twz2XEqqKis8loNNrv6%2FXwe2Xnx9T7HvS4LBD39iEglN8uAoliMwa4e2OSXxxMgsQX18CdAnw%2FT%2FFlBf3AlbJAIpCj6qsLiw6xxiPrRNzdtYLt423wnoGR0zLwmF34FoXykG%2Bw9UIDPl1az6veWEMTHqHTPqyV9uXJGA2&X-Amz-Signature=b1823efb31912693b4020c00cffe1a8867c85ce0216f8367a74f691cf4ace00e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
