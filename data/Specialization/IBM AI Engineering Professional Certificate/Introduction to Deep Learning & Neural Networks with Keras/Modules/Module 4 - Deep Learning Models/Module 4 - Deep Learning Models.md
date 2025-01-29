

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PJ2GSX2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZkclLlBARyXr%2BiM%2Bd3Z5onsJb4ynFKvGPoWKeiZy9XgIgbL588Lok%2FoMsUZje87H%2B5x%2Fk4rdbBeUSaCrddsmNJdMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3LJ%2FuDhRmvK4YIWircAyHGML0I9DLluqkkf%2BeuBAEMvNhryEXMkrlxOxv%2B80C5OdFhDuNljEPHBCxgEoWuyHpBd9lb%2BJJBqwzMlTvDSsDjmHuLYR8mh%2FSUP7mmFaiKBuGm%2BDdIGV6EVmBpZj2MwAAvQIqRuwGZEfELbqelMFhpqeb%2Fd8885JPuMN6HlCLYHCWyjIaeK9TiyykIRVt7hnYCtxSUFu3VXHp%2BEzDWfibayqwUctzNthrE7oU38DDnPTo47T5veLFF%2FviyhbT3YESY4fvt09g5DjvgkXAiB4EJbo1afg%2BXd9hSmYRZfDyG8M0n72jgo50NaiesVzMbTSN77idwmAx2ujSPQX5KgtAtHSBYm2AhevHk350hEIDdMDCcLpJYuIvmVBKYYblGhzAFqmWZmbs41VXbn2j2Iz59fmrxdBJFJ1yKvHUCFoSpXJ50Ql7VhR5ImOMJpVzQ76yVkWlT61LB6mCotylTiJf70SXHDd0WFZcADFkMtMshNAyQcGdKLYNy0ZCXIk4c7c6vmoZ8tjleZCB%2BchTvmZ6WUKJOQSoQ1zImJKbjGe93U9KB44znFdUzo9%2FKAggbXu%2BPO4UaCJuLvJucfcojaQf6e%2B1%2B6Eo3NMRbBirk4Tx0%2FbzzFnsKXsR5LvI4MP6o6rwGOqUByR6sU078RVD1AhJvI29cy95gkF79%2B2E5ABP0tGuuAD7f9O3qGuNFa3TgJ9ILJPdTiwJrlQ2%2FXLpYGoEC8aR02kfSGuw6jhNJ3jYBpecooZbT8oqU1nzCFTto7er2yAK2wNfUcWh7s8rd9BKBBvGedA4eOct6fIKO3NAdZnD8nbbI87QYmLfBRyUaa3UiZ79aTreI6fuHMpL30vsB4%2BM11lBkm7JU&X-Amz-Signature=3f479e54013a1ba6868163ad65515810374f6c5cfc5a9bb36dff8634c6465314&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PJ2GSX2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZkclLlBARyXr%2BiM%2Bd3Z5onsJb4ynFKvGPoWKeiZy9XgIgbL588Lok%2FoMsUZje87H%2B5x%2Fk4rdbBeUSaCrddsmNJdMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3LJ%2FuDhRmvK4YIWircAyHGML0I9DLluqkkf%2BeuBAEMvNhryEXMkrlxOxv%2B80C5OdFhDuNljEPHBCxgEoWuyHpBd9lb%2BJJBqwzMlTvDSsDjmHuLYR8mh%2FSUP7mmFaiKBuGm%2BDdIGV6EVmBpZj2MwAAvQIqRuwGZEfELbqelMFhpqeb%2Fd8885JPuMN6HlCLYHCWyjIaeK9TiyykIRVt7hnYCtxSUFu3VXHp%2BEzDWfibayqwUctzNthrE7oU38DDnPTo47T5veLFF%2FviyhbT3YESY4fvt09g5DjvgkXAiB4EJbo1afg%2BXd9hSmYRZfDyG8M0n72jgo50NaiesVzMbTSN77idwmAx2ujSPQX5KgtAtHSBYm2AhevHk350hEIDdMDCcLpJYuIvmVBKYYblGhzAFqmWZmbs41VXbn2j2Iz59fmrxdBJFJ1yKvHUCFoSpXJ50Ql7VhR5ImOMJpVzQ76yVkWlT61LB6mCotylTiJf70SXHDd0WFZcADFkMtMshNAyQcGdKLYNy0ZCXIk4c7c6vmoZ8tjleZCB%2BchTvmZ6WUKJOQSoQ1zImJKbjGe93U9KB44znFdUzo9%2FKAggbXu%2BPO4UaCJuLvJucfcojaQf6e%2B1%2B6Eo3NMRbBirk4Tx0%2FbzzFnsKXsR5LvI4MP6o6rwGOqUByR6sU078RVD1AhJvI29cy95gkF79%2B2E5ABP0tGuuAD7f9O3qGuNFa3TgJ9ILJPdTiwJrlQ2%2FXLpYGoEC8aR02kfSGuw6jhNJ3jYBpecooZbT8oqU1nzCFTto7er2yAK2wNfUcWh7s8rd9BKBBvGedA4eOct6fIKO3NAdZnD8nbbI87QYmLfBRyUaa3UiZ79aTreI6fuHMpL30vsB4%2BM11lBkm7JU&X-Amz-Signature=2dc9422f6d304f6cf46289d034a56a1a0427abcb108a80fc50b43dcb2cc19a35&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PJ2GSX2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZkclLlBARyXr%2BiM%2Bd3Z5onsJb4ynFKvGPoWKeiZy9XgIgbL588Lok%2FoMsUZje87H%2B5x%2Fk4rdbBeUSaCrddsmNJdMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3LJ%2FuDhRmvK4YIWircAyHGML0I9DLluqkkf%2BeuBAEMvNhryEXMkrlxOxv%2B80C5OdFhDuNljEPHBCxgEoWuyHpBd9lb%2BJJBqwzMlTvDSsDjmHuLYR8mh%2FSUP7mmFaiKBuGm%2BDdIGV6EVmBpZj2MwAAvQIqRuwGZEfELbqelMFhpqeb%2Fd8885JPuMN6HlCLYHCWyjIaeK9TiyykIRVt7hnYCtxSUFu3VXHp%2BEzDWfibayqwUctzNthrE7oU38DDnPTo47T5veLFF%2FviyhbT3YESY4fvt09g5DjvgkXAiB4EJbo1afg%2BXd9hSmYRZfDyG8M0n72jgo50NaiesVzMbTSN77idwmAx2ujSPQX5KgtAtHSBYm2AhevHk350hEIDdMDCcLpJYuIvmVBKYYblGhzAFqmWZmbs41VXbn2j2Iz59fmrxdBJFJ1yKvHUCFoSpXJ50Ql7VhR5ImOMJpVzQ76yVkWlT61LB6mCotylTiJf70SXHDd0WFZcADFkMtMshNAyQcGdKLYNy0ZCXIk4c7c6vmoZ8tjleZCB%2BchTvmZ6WUKJOQSoQ1zImJKbjGe93U9KB44znFdUzo9%2FKAggbXu%2BPO4UaCJuLvJucfcojaQf6e%2B1%2B6Eo3NMRbBirk4Tx0%2FbzzFnsKXsR5LvI4MP6o6rwGOqUByR6sU078RVD1AhJvI29cy95gkF79%2B2E5ABP0tGuuAD7f9O3qGuNFa3TgJ9ILJPdTiwJrlQ2%2FXLpYGoEC8aR02kfSGuw6jhNJ3jYBpecooZbT8oqU1nzCFTto7er2yAK2wNfUcWh7s8rd9BKBBvGedA4eOct6fIKO3NAdZnD8nbbI87QYmLfBRyUaa3UiZ79aTreI6fuHMpL30vsB4%2BM11lBkm7JU&X-Amz-Signature=a5d2d9b8e410391b7483f42fc23e05df9abc3cfd5b7176c4b771ba57dfb73be9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PJ2GSX2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZkclLlBARyXr%2BiM%2Bd3Z5onsJb4ynFKvGPoWKeiZy9XgIgbL588Lok%2FoMsUZje87H%2B5x%2Fk4rdbBeUSaCrddsmNJdMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3LJ%2FuDhRmvK4YIWircAyHGML0I9DLluqkkf%2BeuBAEMvNhryEXMkrlxOxv%2B80C5OdFhDuNljEPHBCxgEoWuyHpBd9lb%2BJJBqwzMlTvDSsDjmHuLYR8mh%2FSUP7mmFaiKBuGm%2BDdIGV6EVmBpZj2MwAAvQIqRuwGZEfELbqelMFhpqeb%2Fd8885JPuMN6HlCLYHCWyjIaeK9TiyykIRVt7hnYCtxSUFu3VXHp%2BEzDWfibayqwUctzNthrE7oU38DDnPTo47T5veLFF%2FviyhbT3YESY4fvt09g5DjvgkXAiB4EJbo1afg%2BXd9hSmYRZfDyG8M0n72jgo50NaiesVzMbTSN77idwmAx2ujSPQX5KgtAtHSBYm2AhevHk350hEIDdMDCcLpJYuIvmVBKYYblGhzAFqmWZmbs41VXbn2j2Iz59fmrxdBJFJ1yKvHUCFoSpXJ50Ql7VhR5ImOMJpVzQ76yVkWlT61LB6mCotylTiJf70SXHDd0WFZcADFkMtMshNAyQcGdKLYNy0ZCXIk4c7c6vmoZ8tjleZCB%2BchTvmZ6WUKJOQSoQ1zImJKbjGe93U9KB44znFdUzo9%2FKAggbXu%2BPO4UaCJuLvJucfcojaQf6e%2B1%2B6Eo3NMRbBirk4Tx0%2FbzzFnsKXsR5LvI4MP6o6rwGOqUByR6sU078RVD1AhJvI29cy95gkF79%2B2E5ABP0tGuuAD7f9O3qGuNFa3TgJ9ILJPdTiwJrlQ2%2FXLpYGoEC8aR02kfSGuw6jhNJ3jYBpecooZbT8oqU1nzCFTto7er2yAK2wNfUcWh7s8rd9BKBBvGedA4eOct6fIKO3NAdZnD8nbbI87QYmLfBRyUaa3UiZ79aTreI6fuHMpL30vsB4%2BM11lBkm7JU&X-Amz-Signature=a9fac53432874be8d3372b17b30b421e6c2b8a9bc560858e3eb40992776e0af3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PJ2GSX2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZkclLlBARyXr%2BiM%2Bd3Z5onsJb4ynFKvGPoWKeiZy9XgIgbL588Lok%2FoMsUZje87H%2B5x%2Fk4rdbBeUSaCrddsmNJdMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3LJ%2FuDhRmvK4YIWircAyHGML0I9DLluqkkf%2BeuBAEMvNhryEXMkrlxOxv%2B80C5OdFhDuNljEPHBCxgEoWuyHpBd9lb%2BJJBqwzMlTvDSsDjmHuLYR8mh%2FSUP7mmFaiKBuGm%2BDdIGV6EVmBpZj2MwAAvQIqRuwGZEfELbqelMFhpqeb%2Fd8885JPuMN6HlCLYHCWyjIaeK9TiyykIRVt7hnYCtxSUFu3VXHp%2BEzDWfibayqwUctzNthrE7oU38DDnPTo47T5veLFF%2FviyhbT3YESY4fvt09g5DjvgkXAiB4EJbo1afg%2BXd9hSmYRZfDyG8M0n72jgo50NaiesVzMbTSN77idwmAx2ujSPQX5KgtAtHSBYm2AhevHk350hEIDdMDCcLpJYuIvmVBKYYblGhzAFqmWZmbs41VXbn2j2Iz59fmrxdBJFJ1yKvHUCFoSpXJ50Ql7VhR5ImOMJpVzQ76yVkWlT61LB6mCotylTiJf70SXHDd0WFZcADFkMtMshNAyQcGdKLYNy0ZCXIk4c7c6vmoZ8tjleZCB%2BchTvmZ6WUKJOQSoQ1zImJKbjGe93U9KB44znFdUzo9%2FKAggbXu%2BPO4UaCJuLvJucfcojaQf6e%2B1%2B6Eo3NMRbBirk4Tx0%2FbzzFnsKXsR5LvI4MP6o6rwGOqUByR6sU078RVD1AhJvI29cy95gkF79%2B2E5ABP0tGuuAD7f9O3qGuNFa3TgJ9ILJPdTiwJrlQ2%2FXLpYGoEC8aR02kfSGuw6jhNJ3jYBpecooZbT8oqU1nzCFTto7er2yAK2wNfUcWh7s8rd9BKBBvGedA4eOct6fIKO3NAdZnD8nbbI87QYmLfBRyUaa3UiZ79aTreI6fuHMpL30vsB4%2BM11lBkm7JU&X-Amz-Signature=58192a1c11ab68e7d1f4097e8c44ac7c76adaf2cb7dbd6903642e2c454dd1b1d&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PJ2GSX2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZkclLlBARyXr%2BiM%2Bd3Z5onsJb4ynFKvGPoWKeiZy9XgIgbL588Lok%2FoMsUZje87H%2B5x%2Fk4rdbBeUSaCrddsmNJdMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3LJ%2FuDhRmvK4YIWircAyHGML0I9DLluqkkf%2BeuBAEMvNhryEXMkrlxOxv%2B80C5OdFhDuNljEPHBCxgEoWuyHpBd9lb%2BJJBqwzMlTvDSsDjmHuLYR8mh%2FSUP7mmFaiKBuGm%2BDdIGV6EVmBpZj2MwAAvQIqRuwGZEfELbqelMFhpqeb%2Fd8885JPuMN6HlCLYHCWyjIaeK9TiyykIRVt7hnYCtxSUFu3VXHp%2BEzDWfibayqwUctzNthrE7oU38DDnPTo47T5veLFF%2FviyhbT3YESY4fvt09g5DjvgkXAiB4EJbo1afg%2BXd9hSmYRZfDyG8M0n72jgo50NaiesVzMbTSN77idwmAx2ujSPQX5KgtAtHSBYm2AhevHk350hEIDdMDCcLpJYuIvmVBKYYblGhzAFqmWZmbs41VXbn2j2Iz59fmrxdBJFJ1yKvHUCFoSpXJ50Ql7VhR5ImOMJpVzQ76yVkWlT61LB6mCotylTiJf70SXHDd0WFZcADFkMtMshNAyQcGdKLYNy0ZCXIk4c7c6vmoZ8tjleZCB%2BchTvmZ6WUKJOQSoQ1zImJKbjGe93U9KB44znFdUzo9%2FKAggbXu%2BPO4UaCJuLvJucfcojaQf6e%2B1%2B6Eo3NMRbBirk4Tx0%2FbzzFnsKXsR5LvI4MP6o6rwGOqUByR6sU078RVD1AhJvI29cy95gkF79%2B2E5ABP0tGuuAD7f9O3qGuNFa3TgJ9ILJPdTiwJrlQ2%2FXLpYGoEC8aR02kfSGuw6jhNJ3jYBpecooZbT8oqU1nzCFTto7er2yAK2wNfUcWh7s8rd9BKBBvGedA4eOct6fIKO3NAdZnD8nbbI87QYmLfBRyUaa3UiZ79aTreI6fuHMpL30vsB4%2BM11lBkm7JU&X-Amz-Signature=d72317c33b4a67f287a5a56432090203f5c501a69fc147505373e762d3195bde&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PJ2GSX2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZkclLlBARyXr%2BiM%2Bd3Z5onsJb4ynFKvGPoWKeiZy9XgIgbL588Lok%2FoMsUZje87H%2B5x%2Fk4rdbBeUSaCrddsmNJdMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3LJ%2FuDhRmvK4YIWircAyHGML0I9DLluqkkf%2BeuBAEMvNhryEXMkrlxOxv%2B80C5OdFhDuNljEPHBCxgEoWuyHpBd9lb%2BJJBqwzMlTvDSsDjmHuLYR8mh%2FSUP7mmFaiKBuGm%2BDdIGV6EVmBpZj2MwAAvQIqRuwGZEfELbqelMFhpqeb%2Fd8885JPuMN6HlCLYHCWyjIaeK9TiyykIRVt7hnYCtxSUFu3VXHp%2BEzDWfibayqwUctzNthrE7oU38DDnPTo47T5veLFF%2FviyhbT3YESY4fvt09g5DjvgkXAiB4EJbo1afg%2BXd9hSmYRZfDyG8M0n72jgo50NaiesVzMbTSN77idwmAx2ujSPQX5KgtAtHSBYm2AhevHk350hEIDdMDCcLpJYuIvmVBKYYblGhzAFqmWZmbs41VXbn2j2Iz59fmrxdBJFJ1yKvHUCFoSpXJ50Ql7VhR5ImOMJpVzQ76yVkWlT61LB6mCotylTiJf70SXHDd0WFZcADFkMtMshNAyQcGdKLYNy0ZCXIk4c7c6vmoZ8tjleZCB%2BchTvmZ6WUKJOQSoQ1zImJKbjGe93U9KB44znFdUzo9%2FKAggbXu%2BPO4UaCJuLvJucfcojaQf6e%2B1%2B6Eo3NMRbBirk4Tx0%2FbzzFnsKXsR5LvI4MP6o6rwGOqUByR6sU078RVD1AhJvI29cy95gkF79%2B2E5ABP0tGuuAD7f9O3qGuNFa3TgJ9ILJPdTiwJrlQ2%2FXLpYGoEC8aR02kfSGuw6jhNJ3jYBpecooZbT8oqU1nzCFTto7er2yAK2wNfUcWh7s8rd9BKBBvGedA4eOct6fIKO3NAdZnD8nbbI87QYmLfBRyUaa3UiZ79aTreI6fuHMpL30vsB4%2BM11lBkm7JU&X-Amz-Signature=9b6527611f47bd9e5cc42dc882bb98b6cf57143ddc0d3a17d7bd05da7004ba08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PJ2GSX2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZkclLlBARyXr%2BiM%2Bd3Z5onsJb4ynFKvGPoWKeiZy9XgIgbL588Lok%2FoMsUZje87H%2B5x%2Fk4rdbBeUSaCrddsmNJdMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3LJ%2FuDhRmvK4YIWircAyHGML0I9DLluqkkf%2BeuBAEMvNhryEXMkrlxOxv%2B80C5OdFhDuNljEPHBCxgEoWuyHpBd9lb%2BJJBqwzMlTvDSsDjmHuLYR8mh%2FSUP7mmFaiKBuGm%2BDdIGV6EVmBpZj2MwAAvQIqRuwGZEfELbqelMFhpqeb%2Fd8885JPuMN6HlCLYHCWyjIaeK9TiyykIRVt7hnYCtxSUFu3VXHp%2BEzDWfibayqwUctzNthrE7oU38DDnPTo47T5veLFF%2FviyhbT3YESY4fvt09g5DjvgkXAiB4EJbo1afg%2BXd9hSmYRZfDyG8M0n72jgo50NaiesVzMbTSN77idwmAx2ujSPQX5KgtAtHSBYm2AhevHk350hEIDdMDCcLpJYuIvmVBKYYblGhzAFqmWZmbs41VXbn2j2Iz59fmrxdBJFJ1yKvHUCFoSpXJ50Ql7VhR5ImOMJpVzQ76yVkWlT61LB6mCotylTiJf70SXHDd0WFZcADFkMtMshNAyQcGdKLYNy0ZCXIk4c7c6vmoZ8tjleZCB%2BchTvmZ6WUKJOQSoQ1zImJKbjGe93U9KB44znFdUzo9%2FKAggbXu%2BPO4UaCJuLvJucfcojaQf6e%2B1%2B6Eo3NMRbBirk4Tx0%2FbzzFnsKXsR5LvI4MP6o6rwGOqUByR6sU078RVD1AhJvI29cy95gkF79%2B2E5ABP0tGuuAD7f9O3qGuNFa3TgJ9ILJPdTiwJrlQ2%2FXLpYGoEC8aR02kfSGuw6jhNJ3jYBpecooZbT8oqU1nzCFTto7er2yAK2wNfUcWh7s8rd9BKBBvGedA4eOct6fIKO3NAdZnD8nbbI87QYmLfBRyUaa3UiZ79aTreI6fuHMpL30vsB4%2BM11lBkm7JU&X-Amz-Signature=b490a5172a2cdc9a7269651c3d163fdd1f2d532561a636274aa08808f86cc8b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PJ2GSX2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZkclLlBARyXr%2BiM%2Bd3Z5onsJb4ynFKvGPoWKeiZy9XgIgbL588Lok%2FoMsUZje87H%2B5x%2Fk4rdbBeUSaCrddsmNJdMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3LJ%2FuDhRmvK4YIWircAyHGML0I9DLluqkkf%2BeuBAEMvNhryEXMkrlxOxv%2B80C5OdFhDuNljEPHBCxgEoWuyHpBd9lb%2BJJBqwzMlTvDSsDjmHuLYR8mh%2FSUP7mmFaiKBuGm%2BDdIGV6EVmBpZj2MwAAvQIqRuwGZEfELbqelMFhpqeb%2Fd8885JPuMN6HlCLYHCWyjIaeK9TiyykIRVt7hnYCtxSUFu3VXHp%2BEzDWfibayqwUctzNthrE7oU38DDnPTo47T5veLFF%2FviyhbT3YESY4fvt09g5DjvgkXAiB4EJbo1afg%2BXd9hSmYRZfDyG8M0n72jgo50NaiesVzMbTSN77idwmAx2ujSPQX5KgtAtHSBYm2AhevHk350hEIDdMDCcLpJYuIvmVBKYYblGhzAFqmWZmbs41VXbn2j2Iz59fmrxdBJFJ1yKvHUCFoSpXJ50Ql7VhR5ImOMJpVzQ76yVkWlT61LB6mCotylTiJf70SXHDd0WFZcADFkMtMshNAyQcGdKLYNy0ZCXIk4c7c6vmoZ8tjleZCB%2BchTvmZ6WUKJOQSoQ1zImJKbjGe93U9KB44znFdUzo9%2FKAggbXu%2BPO4UaCJuLvJucfcojaQf6e%2B1%2B6Eo3NMRbBirk4Tx0%2FbzzFnsKXsR5LvI4MP6o6rwGOqUByR6sU078RVD1AhJvI29cy95gkF79%2B2E5ABP0tGuuAD7f9O3qGuNFa3TgJ9ILJPdTiwJrlQ2%2FXLpYGoEC8aR02kfSGuw6jhNJ3jYBpecooZbT8oqU1nzCFTto7er2yAK2wNfUcWh7s8rd9BKBBvGedA4eOct6fIKO3NAdZnD8nbbI87QYmLfBRyUaa3UiZ79aTreI6fuHMpL30vsB4%2BM11lBkm7JU&X-Amz-Signature=b107049256be8f5fc63ae87310e4e6ae1218e447d382b247deebe086a7f2b445&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3BWX5SL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBT5pb%2F9z%2F4xBZ0J1Dd%2FSbR5DJo35oQGTft%2FFczGSQY%2BAiA2ODpVR9cx3eYZ8EQTqFzA1G%2Bh46FrQyys0iKbp9%2Ff2CqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTsNIuBDcOUjreFfXKtwDpX9RqVatzMRgmoUgFzG1UQNOS2c4GGzzNyJDIIElU5XAJ%2BDf%2Bub37jsHNDRoIfOkheoKtHYul57dptNl9DU2o6TDIOCP3XoDHztSRrdhpSkz8wA%2FJpYPaChKQP5N2xnncEZwFJqAlGVAE%2BA3RZIZgCzpiK0TkwXcK2LOeF4Skchv27%2BVLZ%2FR4MwLTgY4XpTFT44WUDbrJEAcQNQiVnhffLSQEugq0R7JmhSk9QHHEooH7cim94RZw3H83uL8YLEWMXwfA5YazpWLv4B6PIHKLj2vatHoW1OQG8M8Qo5nPBCpyYHGkJ5tzc7fsETRyxrfHXYQG9ltwT13FOk62LKzYag4xMhwsDkNOcT38dFW4QGH7AX8OPZ8qarWsC99sJ%2BEO03w2LF%2BQYI9aJB6Lf%2FwoGa80zeKe0KJRc4jDsKOBsIciamuoE4XKpQKEGyDOywsKV3avOV6ffjG0J3nHmPUovOiDdA2u6rTGmdlAKlyQPNN2ifEEYktWj5WvEzcSodeHhIiCkyjfK%2BVmIijFFSgoTFTWO%2FZ%2BnYJZW1I4SBEKLQEyoWq8FG87tSX1MGOLIZz6vGPXHVIeMp2CpugoSMX2rqFEv%2BvLO7Q%2BHUL0t0k8bpo23OFO7j7NqDLInkwzqnqvAY6pgGlxx92SaTI372%2BmvqoypRTX30Ox8ymHu4yDH2nYG1Th3lTxuMh4Sq1Y90jq3PHF0bPxnB6yhOrZiqDxp8i9pfu6qSC%2BLnBuejRdxIza1fHa0xhhiRR9Btt1ZcmOZTZKovg1OkwaqZuFcZJAtxsyaZnYO78RyJrNrm%2BOH%2FUGHv9urIyb7cJK1y1Fk%2FFMZgcINlJY7e7KVTxfItXbnozsfZ16Mxk8ehV&X-Amz-Signature=8dcbb2701c24236a1b4f32aaa693c94f0464261a53710811f01f60aa8a592c46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3BWX5SL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBT5pb%2F9z%2F4xBZ0J1Dd%2FSbR5DJo35oQGTft%2FFczGSQY%2BAiA2ODpVR9cx3eYZ8EQTqFzA1G%2Bh46FrQyys0iKbp9%2Ff2CqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTsNIuBDcOUjreFfXKtwDpX9RqVatzMRgmoUgFzG1UQNOS2c4GGzzNyJDIIElU5XAJ%2BDf%2Bub37jsHNDRoIfOkheoKtHYul57dptNl9DU2o6TDIOCP3XoDHztSRrdhpSkz8wA%2FJpYPaChKQP5N2xnncEZwFJqAlGVAE%2BA3RZIZgCzpiK0TkwXcK2LOeF4Skchv27%2BVLZ%2FR4MwLTgY4XpTFT44WUDbrJEAcQNQiVnhffLSQEugq0R7JmhSk9QHHEooH7cim94RZw3H83uL8YLEWMXwfA5YazpWLv4B6PIHKLj2vatHoW1OQG8M8Qo5nPBCpyYHGkJ5tzc7fsETRyxrfHXYQG9ltwT13FOk62LKzYag4xMhwsDkNOcT38dFW4QGH7AX8OPZ8qarWsC99sJ%2BEO03w2LF%2BQYI9aJB6Lf%2FwoGa80zeKe0KJRc4jDsKOBsIciamuoE4XKpQKEGyDOywsKV3avOV6ffjG0J3nHmPUovOiDdA2u6rTGmdlAKlyQPNN2ifEEYktWj5WvEzcSodeHhIiCkyjfK%2BVmIijFFSgoTFTWO%2FZ%2BnYJZW1I4SBEKLQEyoWq8FG87tSX1MGOLIZz6vGPXHVIeMp2CpugoSMX2rqFEv%2BvLO7Q%2BHUL0t0k8bpo23OFO7j7NqDLInkwzqnqvAY6pgGlxx92SaTI372%2BmvqoypRTX30Ox8ymHu4yDH2nYG1Th3lTxuMh4Sq1Y90jq3PHF0bPxnB6yhOrZiqDxp8i9pfu6qSC%2BLnBuejRdxIza1fHa0xhhiRR9Btt1ZcmOZTZKovg1OkwaqZuFcZJAtxsyaZnYO78RyJrNrm%2BOH%2FUGHv9urIyb7cJK1y1Fk%2FFMZgcINlJY7e7KVTxfItXbnozsfZ16Mxk8ehV&X-Amz-Signature=34e205de9d5bec6d231fae32e8814c4e9e18161d8553fdd7185800f1799db857&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
