

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MRK5SXI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjM20Rr9qu06o5E4bewd1%2B5Luf5OnsXEUnhvYpR7%2FItAiEA4%2BLytM44vbP1odeEKL1gSIlFW5WJ5aIQ7p%2BHz7sOtCcqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBY0kC4M20zxFBPwBCrcA1c650dQ5vidnhWbskw7Xw7J5GkRaTJDob5PTjlx6A7yg3107VieE8BJOq5lo%2BhzmNsF27jLakbSNlKPOcwZJWHNmy2QiSo3am1yeFu2ZGdBZPCKQVbr4bJbVwrBu78vqQs1dlUh9ssADAAEaxkPmhEgf5OOAWa8hIcHOIDaEevWrgXwnVuX%2FIuFOypfh60T2FpJUPLyxKCD%2BGGfzXTQRoKcHIosy64cww4xDaL%2FxRlj0P270pmae5IM3g0EzDYbbYeXg1Sl3AZ5x4VQ3kZo%2FUyLbWtSnkKA0iyU2YVTtkor565uODWDAQ8Nx2ArexVL3LARK5r6ZJVXxEpbelxVuhC6a5QxxoMIy30VaHN0zG0jtqOQRFHP7dRLg07iBq4hGX97koxsTDPcYyvED3t3xnQgZoGh70IwwzBLpm16ETHszWTh0mD0vnVNI3wT1M3llAkda7DfvBMJ38CmNCdjL2EZUnXkyotL2zA3NGYHSgDe%2FGQXJhBaJqGC%2BRej4PYbhb%2Bph35mSApg8LtIhGjyDjV3RsMe5iCaHi1wQUJidvMyc4fkc4zHa3vq7wM%2FgwZEtQ2UNTtV4Dv%2Fe8H6RxcSCH4kesp6YHy0F0o8pnj727qxbRna2uitGwkTV7BHMO69%2BLwGOqUBKtv%2Bpcam42W8kv1Rv0p%2BGjc0cmKhvaGlBeJRpi85RLTtSc88JIGKA6TiKbCpoc4e9aED6AUSj0qwSxrxyBW1izP%2F9Up5O4uiMluegw7exFobMnXfwuh0F9AqqY4%2BF3IdBuDOwI2sL%2FsvkuF%2F%2FsOTBKC7NZOqWNCFHEZJEZa3P7A6ivrX8MHplupc%2FWyPOvHAEi2M9LFQMX0aJYp9aBKZf%2BrFf%2BJ7&X-Amz-Signature=cdfcee87eac8ffc5dd694d53ba7968a91edf9663a3fb7a9fc309c863446ab609&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MRK5SXI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjM20Rr9qu06o5E4bewd1%2B5Luf5OnsXEUnhvYpR7%2FItAiEA4%2BLytM44vbP1odeEKL1gSIlFW5WJ5aIQ7p%2BHz7sOtCcqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBY0kC4M20zxFBPwBCrcA1c650dQ5vidnhWbskw7Xw7J5GkRaTJDob5PTjlx6A7yg3107VieE8BJOq5lo%2BhzmNsF27jLakbSNlKPOcwZJWHNmy2QiSo3am1yeFu2ZGdBZPCKQVbr4bJbVwrBu78vqQs1dlUh9ssADAAEaxkPmhEgf5OOAWa8hIcHOIDaEevWrgXwnVuX%2FIuFOypfh60T2FpJUPLyxKCD%2BGGfzXTQRoKcHIosy64cww4xDaL%2FxRlj0P270pmae5IM3g0EzDYbbYeXg1Sl3AZ5x4VQ3kZo%2FUyLbWtSnkKA0iyU2YVTtkor565uODWDAQ8Nx2ArexVL3LARK5r6ZJVXxEpbelxVuhC6a5QxxoMIy30VaHN0zG0jtqOQRFHP7dRLg07iBq4hGX97koxsTDPcYyvED3t3xnQgZoGh70IwwzBLpm16ETHszWTh0mD0vnVNI3wT1M3llAkda7DfvBMJ38CmNCdjL2EZUnXkyotL2zA3NGYHSgDe%2FGQXJhBaJqGC%2BRej4PYbhb%2Bph35mSApg8LtIhGjyDjV3RsMe5iCaHi1wQUJidvMyc4fkc4zHa3vq7wM%2FgwZEtQ2UNTtV4Dv%2Fe8H6RxcSCH4kesp6YHy0F0o8pnj727qxbRna2uitGwkTV7BHMO69%2BLwGOqUBKtv%2Bpcam42W8kv1Rv0p%2BGjc0cmKhvaGlBeJRpi85RLTtSc88JIGKA6TiKbCpoc4e9aED6AUSj0qwSxrxyBW1izP%2F9Up5O4uiMluegw7exFobMnXfwuh0F9AqqY4%2BF3IdBuDOwI2sL%2FsvkuF%2F%2FsOTBKC7NZOqWNCFHEZJEZa3P7A6ivrX8MHplupc%2FWyPOvHAEi2M9LFQMX0aJYp9aBKZf%2BrFf%2BJ7&X-Amz-Signature=03121b5ef72d35db9ce7275a70de5a7bcd2ec82d3fc3f7dfc341ef915bb86588&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MRK5SXI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjM20Rr9qu06o5E4bewd1%2B5Luf5OnsXEUnhvYpR7%2FItAiEA4%2BLytM44vbP1odeEKL1gSIlFW5WJ5aIQ7p%2BHz7sOtCcqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBY0kC4M20zxFBPwBCrcA1c650dQ5vidnhWbskw7Xw7J5GkRaTJDob5PTjlx6A7yg3107VieE8BJOq5lo%2BhzmNsF27jLakbSNlKPOcwZJWHNmy2QiSo3am1yeFu2ZGdBZPCKQVbr4bJbVwrBu78vqQs1dlUh9ssADAAEaxkPmhEgf5OOAWa8hIcHOIDaEevWrgXwnVuX%2FIuFOypfh60T2FpJUPLyxKCD%2BGGfzXTQRoKcHIosy64cww4xDaL%2FxRlj0P270pmae5IM3g0EzDYbbYeXg1Sl3AZ5x4VQ3kZo%2FUyLbWtSnkKA0iyU2YVTtkor565uODWDAQ8Nx2ArexVL3LARK5r6ZJVXxEpbelxVuhC6a5QxxoMIy30VaHN0zG0jtqOQRFHP7dRLg07iBq4hGX97koxsTDPcYyvED3t3xnQgZoGh70IwwzBLpm16ETHszWTh0mD0vnVNI3wT1M3llAkda7DfvBMJ38CmNCdjL2EZUnXkyotL2zA3NGYHSgDe%2FGQXJhBaJqGC%2BRej4PYbhb%2Bph35mSApg8LtIhGjyDjV3RsMe5iCaHi1wQUJidvMyc4fkc4zHa3vq7wM%2FgwZEtQ2UNTtV4Dv%2Fe8H6RxcSCH4kesp6YHy0F0o8pnj727qxbRna2uitGwkTV7BHMO69%2BLwGOqUBKtv%2Bpcam42W8kv1Rv0p%2BGjc0cmKhvaGlBeJRpi85RLTtSc88JIGKA6TiKbCpoc4e9aED6AUSj0qwSxrxyBW1izP%2F9Up5O4uiMluegw7exFobMnXfwuh0F9AqqY4%2BF3IdBuDOwI2sL%2FsvkuF%2F%2FsOTBKC7NZOqWNCFHEZJEZa3P7A6ivrX8MHplupc%2FWyPOvHAEi2M9LFQMX0aJYp9aBKZf%2BrFf%2BJ7&X-Amz-Signature=6ede7cc7f27b1c1b46b5b9109fff635acc59875a838d31ba96ae72c7f5a9cc67&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MRK5SXI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjM20Rr9qu06o5E4bewd1%2B5Luf5OnsXEUnhvYpR7%2FItAiEA4%2BLytM44vbP1odeEKL1gSIlFW5WJ5aIQ7p%2BHz7sOtCcqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBY0kC4M20zxFBPwBCrcA1c650dQ5vidnhWbskw7Xw7J5GkRaTJDob5PTjlx6A7yg3107VieE8BJOq5lo%2BhzmNsF27jLakbSNlKPOcwZJWHNmy2QiSo3am1yeFu2ZGdBZPCKQVbr4bJbVwrBu78vqQs1dlUh9ssADAAEaxkPmhEgf5OOAWa8hIcHOIDaEevWrgXwnVuX%2FIuFOypfh60T2FpJUPLyxKCD%2BGGfzXTQRoKcHIosy64cww4xDaL%2FxRlj0P270pmae5IM3g0EzDYbbYeXg1Sl3AZ5x4VQ3kZo%2FUyLbWtSnkKA0iyU2YVTtkor565uODWDAQ8Nx2ArexVL3LARK5r6ZJVXxEpbelxVuhC6a5QxxoMIy30VaHN0zG0jtqOQRFHP7dRLg07iBq4hGX97koxsTDPcYyvED3t3xnQgZoGh70IwwzBLpm16ETHszWTh0mD0vnVNI3wT1M3llAkda7DfvBMJ38CmNCdjL2EZUnXkyotL2zA3NGYHSgDe%2FGQXJhBaJqGC%2BRej4PYbhb%2Bph35mSApg8LtIhGjyDjV3RsMe5iCaHi1wQUJidvMyc4fkc4zHa3vq7wM%2FgwZEtQ2UNTtV4Dv%2Fe8H6RxcSCH4kesp6YHy0F0o8pnj727qxbRna2uitGwkTV7BHMO69%2BLwGOqUBKtv%2Bpcam42W8kv1Rv0p%2BGjc0cmKhvaGlBeJRpi85RLTtSc88JIGKA6TiKbCpoc4e9aED6AUSj0qwSxrxyBW1izP%2F9Up5O4uiMluegw7exFobMnXfwuh0F9AqqY4%2BF3IdBuDOwI2sL%2FsvkuF%2F%2FsOTBKC7NZOqWNCFHEZJEZa3P7A6ivrX8MHplupc%2FWyPOvHAEi2M9LFQMX0aJYp9aBKZf%2BrFf%2BJ7&X-Amz-Signature=6f94d556f8165b85a233b2c586696541f0d0e63652bcfb41a61715009550bfba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MRK5SXI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjM20Rr9qu06o5E4bewd1%2B5Luf5OnsXEUnhvYpR7%2FItAiEA4%2BLytM44vbP1odeEKL1gSIlFW5WJ5aIQ7p%2BHz7sOtCcqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBY0kC4M20zxFBPwBCrcA1c650dQ5vidnhWbskw7Xw7J5GkRaTJDob5PTjlx6A7yg3107VieE8BJOq5lo%2BhzmNsF27jLakbSNlKPOcwZJWHNmy2QiSo3am1yeFu2ZGdBZPCKQVbr4bJbVwrBu78vqQs1dlUh9ssADAAEaxkPmhEgf5OOAWa8hIcHOIDaEevWrgXwnVuX%2FIuFOypfh60T2FpJUPLyxKCD%2BGGfzXTQRoKcHIosy64cww4xDaL%2FxRlj0P270pmae5IM3g0EzDYbbYeXg1Sl3AZ5x4VQ3kZo%2FUyLbWtSnkKA0iyU2YVTtkor565uODWDAQ8Nx2ArexVL3LARK5r6ZJVXxEpbelxVuhC6a5QxxoMIy30VaHN0zG0jtqOQRFHP7dRLg07iBq4hGX97koxsTDPcYyvED3t3xnQgZoGh70IwwzBLpm16ETHszWTh0mD0vnVNI3wT1M3llAkda7DfvBMJ38CmNCdjL2EZUnXkyotL2zA3NGYHSgDe%2FGQXJhBaJqGC%2BRej4PYbhb%2Bph35mSApg8LtIhGjyDjV3RsMe5iCaHi1wQUJidvMyc4fkc4zHa3vq7wM%2FgwZEtQ2UNTtV4Dv%2Fe8H6RxcSCH4kesp6YHy0F0o8pnj727qxbRna2uitGwkTV7BHMO69%2BLwGOqUBKtv%2Bpcam42W8kv1Rv0p%2BGjc0cmKhvaGlBeJRpi85RLTtSc88JIGKA6TiKbCpoc4e9aED6AUSj0qwSxrxyBW1izP%2F9Up5O4uiMluegw7exFobMnXfwuh0F9AqqY4%2BF3IdBuDOwI2sL%2FsvkuF%2F%2FsOTBKC7NZOqWNCFHEZJEZa3P7A6ivrX8MHplupc%2FWyPOvHAEi2M9LFQMX0aJYp9aBKZf%2BrFf%2BJ7&X-Amz-Signature=ebfbbe826c02fda4770648fd3ea17cf26d9a96076120d43e8d2ea8ddf527ab29&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MRK5SXI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjM20Rr9qu06o5E4bewd1%2B5Luf5OnsXEUnhvYpR7%2FItAiEA4%2BLytM44vbP1odeEKL1gSIlFW5WJ5aIQ7p%2BHz7sOtCcqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBY0kC4M20zxFBPwBCrcA1c650dQ5vidnhWbskw7Xw7J5GkRaTJDob5PTjlx6A7yg3107VieE8BJOq5lo%2BhzmNsF27jLakbSNlKPOcwZJWHNmy2QiSo3am1yeFu2ZGdBZPCKQVbr4bJbVwrBu78vqQs1dlUh9ssADAAEaxkPmhEgf5OOAWa8hIcHOIDaEevWrgXwnVuX%2FIuFOypfh60T2FpJUPLyxKCD%2BGGfzXTQRoKcHIosy64cww4xDaL%2FxRlj0P270pmae5IM3g0EzDYbbYeXg1Sl3AZ5x4VQ3kZo%2FUyLbWtSnkKA0iyU2YVTtkor565uODWDAQ8Nx2ArexVL3LARK5r6ZJVXxEpbelxVuhC6a5QxxoMIy30VaHN0zG0jtqOQRFHP7dRLg07iBq4hGX97koxsTDPcYyvED3t3xnQgZoGh70IwwzBLpm16ETHszWTh0mD0vnVNI3wT1M3llAkda7DfvBMJ38CmNCdjL2EZUnXkyotL2zA3NGYHSgDe%2FGQXJhBaJqGC%2BRej4PYbhb%2Bph35mSApg8LtIhGjyDjV3RsMe5iCaHi1wQUJidvMyc4fkc4zHa3vq7wM%2FgwZEtQ2UNTtV4Dv%2Fe8H6RxcSCH4kesp6YHy0F0o8pnj727qxbRna2uitGwkTV7BHMO69%2BLwGOqUBKtv%2Bpcam42W8kv1Rv0p%2BGjc0cmKhvaGlBeJRpi85RLTtSc88JIGKA6TiKbCpoc4e9aED6AUSj0qwSxrxyBW1izP%2F9Up5O4uiMluegw7exFobMnXfwuh0F9AqqY4%2BF3IdBuDOwI2sL%2FsvkuF%2F%2FsOTBKC7NZOqWNCFHEZJEZa3P7A6ivrX8MHplupc%2FWyPOvHAEi2M9LFQMX0aJYp9aBKZf%2BrFf%2BJ7&X-Amz-Signature=66467e59bb203f729442961087099556ccda45928fb2009546961c1fa7ebbbf5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MRK5SXI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjM20Rr9qu06o5E4bewd1%2B5Luf5OnsXEUnhvYpR7%2FItAiEA4%2BLytM44vbP1odeEKL1gSIlFW5WJ5aIQ7p%2BHz7sOtCcqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBY0kC4M20zxFBPwBCrcA1c650dQ5vidnhWbskw7Xw7J5GkRaTJDob5PTjlx6A7yg3107VieE8BJOq5lo%2BhzmNsF27jLakbSNlKPOcwZJWHNmy2QiSo3am1yeFu2ZGdBZPCKQVbr4bJbVwrBu78vqQs1dlUh9ssADAAEaxkPmhEgf5OOAWa8hIcHOIDaEevWrgXwnVuX%2FIuFOypfh60T2FpJUPLyxKCD%2BGGfzXTQRoKcHIosy64cww4xDaL%2FxRlj0P270pmae5IM3g0EzDYbbYeXg1Sl3AZ5x4VQ3kZo%2FUyLbWtSnkKA0iyU2YVTtkor565uODWDAQ8Nx2ArexVL3LARK5r6ZJVXxEpbelxVuhC6a5QxxoMIy30VaHN0zG0jtqOQRFHP7dRLg07iBq4hGX97koxsTDPcYyvED3t3xnQgZoGh70IwwzBLpm16ETHszWTh0mD0vnVNI3wT1M3llAkda7DfvBMJ38CmNCdjL2EZUnXkyotL2zA3NGYHSgDe%2FGQXJhBaJqGC%2BRej4PYbhb%2Bph35mSApg8LtIhGjyDjV3RsMe5iCaHi1wQUJidvMyc4fkc4zHa3vq7wM%2FgwZEtQ2UNTtV4Dv%2Fe8H6RxcSCH4kesp6YHy0F0o8pnj727qxbRna2uitGwkTV7BHMO69%2BLwGOqUBKtv%2Bpcam42W8kv1Rv0p%2BGjc0cmKhvaGlBeJRpi85RLTtSc88JIGKA6TiKbCpoc4e9aED6AUSj0qwSxrxyBW1izP%2F9Up5O4uiMluegw7exFobMnXfwuh0F9AqqY4%2BF3IdBuDOwI2sL%2FsvkuF%2F%2FsOTBKC7NZOqWNCFHEZJEZa3P7A6ivrX8MHplupc%2FWyPOvHAEi2M9LFQMX0aJYp9aBKZf%2BrFf%2BJ7&X-Amz-Signature=df31b06a72405475aeb2941083ea6b1cda96f52ab55e3ee703bb267b55987dbb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MRK5SXI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjM20Rr9qu06o5E4bewd1%2B5Luf5OnsXEUnhvYpR7%2FItAiEA4%2BLytM44vbP1odeEKL1gSIlFW5WJ5aIQ7p%2BHz7sOtCcqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBY0kC4M20zxFBPwBCrcA1c650dQ5vidnhWbskw7Xw7J5GkRaTJDob5PTjlx6A7yg3107VieE8BJOq5lo%2BhzmNsF27jLakbSNlKPOcwZJWHNmy2QiSo3am1yeFu2ZGdBZPCKQVbr4bJbVwrBu78vqQs1dlUh9ssADAAEaxkPmhEgf5OOAWa8hIcHOIDaEevWrgXwnVuX%2FIuFOypfh60T2FpJUPLyxKCD%2BGGfzXTQRoKcHIosy64cww4xDaL%2FxRlj0P270pmae5IM3g0EzDYbbYeXg1Sl3AZ5x4VQ3kZo%2FUyLbWtSnkKA0iyU2YVTtkor565uODWDAQ8Nx2ArexVL3LARK5r6ZJVXxEpbelxVuhC6a5QxxoMIy30VaHN0zG0jtqOQRFHP7dRLg07iBq4hGX97koxsTDPcYyvED3t3xnQgZoGh70IwwzBLpm16ETHszWTh0mD0vnVNI3wT1M3llAkda7DfvBMJ38CmNCdjL2EZUnXkyotL2zA3NGYHSgDe%2FGQXJhBaJqGC%2BRej4PYbhb%2Bph35mSApg8LtIhGjyDjV3RsMe5iCaHi1wQUJidvMyc4fkc4zHa3vq7wM%2FgwZEtQ2UNTtV4Dv%2Fe8H6RxcSCH4kesp6YHy0F0o8pnj727qxbRna2uitGwkTV7BHMO69%2BLwGOqUBKtv%2Bpcam42W8kv1Rv0p%2BGjc0cmKhvaGlBeJRpi85RLTtSc88JIGKA6TiKbCpoc4e9aED6AUSj0qwSxrxyBW1izP%2F9Up5O4uiMluegw7exFobMnXfwuh0F9AqqY4%2BF3IdBuDOwI2sL%2FsvkuF%2F%2FsOTBKC7NZOqWNCFHEZJEZa3P7A6ivrX8MHplupc%2FWyPOvHAEi2M9LFQMX0aJYp9aBKZf%2BrFf%2BJ7&X-Amz-Signature=99d033e55431dbe09bffceaf37ad5634be27c2f98c2977b581c2f275191a5bfb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MRK5SXI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjM20Rr9qu06o5E4bewd1%2B5Luf5OnsXEUnhvYpR7%2FItAiEA4%2BLytM44vbP1odeEKL1gSIlFW5WJ5aIQ7p%2BHz7sOtCcqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBY0kC4M20zxFBPwBCrcA1c650dQ5vidnhWbskw7Xw7J5GkRaTJDob5PTjlx6A7yg3107VieE8BJOq5lo%2BhzmNsF27jLakbSNlKPOcwZJWHNmy2QiSo3am1yeFu2ZGdBZPCKQVbr4bJbVwrBu78vqQs1dlUh9ssADAAEaxkPmhEgf5OOAWa8hIcHOIDaEevWrgXwnVuX%2FIuFOypfh60T2FpJUPLyxKCD%2BGGfzXTQRoKcHIosy64cww4xDaL%2FxRlj0P270pmae5IM3g0EzDYbbYeXg1Sl3AZ5x4VQ3kZo%2FUyLbWtSnkKA0iyU2YVTtkor565uODWDAQ8Nx2ArexVL3LARK5r6ZJVXxEpbelxVuhC6a5QxxoMIy30VaHN0zG0jtqOQRFHP7dRLg07iBq4hGX97koxsTDPcYyvED3t3xnQgZoGh70IwwzBLpm16ETHszWTh0mD0vnVNI3wT1M3llAkda7DfvBMJ38CmNCdjL2EZUnXkyotL2zA3NGYHSgDe%2FGQXJhBaJqGC%2BRej4PYbhb%2Bph35mSApg8LtIhGjyDjV3RsMe5iCaHi1wQUJidvMyc4fkc4zHa3vq7wM%2FgwZEtQ2UNTtV4Dv%2Fe8H6RxcSCH4kesp6YHy0F0o8pnj727qxbRna2uitGwkTV7BHMO69%2BLwGOqUBKtv%2Bpcam42W8kv1Rv0p%2BGjc0cmKhvaGlBeJRpi85RLTtSc88JIGKA6TiKbCpoc4e9aED6AUSj0qwSxrxyBW1izP%2F9Up5O4uiMluegw7exFobMnXfwuh0F9AqqY4%2BF3IdBuDOwI2sL%2FsvkuF%2F%2FsOTBKC7NZOqWNCFHEZJEZa3P7A6ivrX8MHplupc%2FWyPOvHAEi2M9LFQMX0aJYp9aBKZf%2BrFf%2BJ7&X-Amz-Signature=93f8b4f1ae09af6366df01d721acdd3a09b51b01a425f7f5f68fddaa9a0b89af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JXY4Q3U%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEeB98IMwxpChVR9%2Fm9WV0fqR9RhwLbOutD6Io8Q9B4cAiAFPq7EqHUDi1l1rJhHezNnHgKVXZ6U7Ib6kaRuMLkzJyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRv3U%2F%2FdI7hDS1KXYKtwDv394gq%2ByjL%2Bgsoxxlc1uM2fNPrh3dN6bZZqB0f1%2FImzh1%2BWmlUC%2Fs95v38GClyIFCsgUUh9itucft3H5xyyxFCJ1VR9SpAncHfAPS3EkikK48qhGvaygeaNlMQ2QfKb50aMjEaYJsXT8SZLhoQ3sisE%2BMEk5x2PaNAWsIQwFK3OHc%2Bwet8Cox3o%2FdJV6DFRepgzZUIW31bW7CAuJvuncaGPy1Zt%2BEvpoCpaFXrehzx8h0ZlladRVSJ1Z0J1Y7gBayvMy4BsVuagblF9PR9GeTyfU%2BXHfAIKKofVuPbX%2FMaVT0Vyr45HMmZEjHBmTuGCG91UE3Ie9hRjZ%2FqchPlXLG8jYZxGlyblUX%2BhfXxENBH%2F8j9Px4qD0rF55zV9bMlNmiip04MDAcyorHTmLGXu249I%2Fj7LBAYmQMPj6KaM7eTZKcTlq%2FzmpgPRyLWv3BghXIdQE492N%2FJaEFuGzSdo86YJAxVRzq3Bfy%2B9qTau1oCqdnQoREw6NO6uhHeUbW%2B4%2FZhGJXew4NJjxuG%2BdIXXrbu5c0foftGjHtmDKZOnlz%2FWCQcyem7ajOdBFU1GLOJI3iiK5klPxziKd6Q8p6duqOkxm9hABS35nTHXL%2FG4LrH5g2sAEZBvc2Wb4rqcwjsj4vAY6pgHvU80YMQH%2B%2FNmiUvwpOMt6Mq9dtl2htfiHDPmCxGT43c3mgPfEvRDOsLUocS8Im20mtZ5HR9INZ1mUZIMhegG%2FznmX7sDPyOYkcOZ7QAFQa2%2FL9jYbWWAmgMaGoc7ztVSyhrskqDsnxHLeWvfBOasPzOOXSyT8YVMwB1tH9iHMA6B20q%2FmILMDQa254rkU9WLt2ntdXRLUMcosuD509fNIWKlPD1Df&X-Amz-Signature=1e137c344ff6f311b706411a73c158693eae88329e6f41dce7d2198d071b2c37&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JXY4Q3U%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEeB98IMwxpChVR9%2Fm9WV0fqR9RhwLbOutD6Io8Q9B4cAiAFPq7EqHUDi1l1rJhHezNnHgKVXZ6U7Ib6kaRuMLkzJyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRv3U%2F%2FdI7hDS1KXYKtwDv394gq%2ByjL%2Bgsoxxlc1uM2fNPrh3dN6bZZqB0f1%2FImzh1%2BWmlUC%2Fs95v38GClyIFCsgUUh9itucft3H5xyyxFCJ1VR9SpAncHfAPS3EkikK48qhGvaygeaNlMQ2QfKb50aMjEaYJsXT8SZLhoQ3sisE%2BMEk5x2PaNAWsIQwFK3OHc%2Bwet8Cox3o%2FdJV6DFRepgzZUIW31bW7CAuJvuncaGPy1Zt%2BEvpoCpaFXrehzx8h0ZlladRVSJ1Z0J1Y7gBayvMy4BsVuagblF9PR9GeTyfU%2BXHfAIKKofVuPbX%2FMaVT0Vyr45HMmZEjHBmTuGCG91UE3Ie9hRjZ%2FqchPlXLG8jYZxGlyblUX%2BhfXxENBH%2F8j9Px4qD0rF55zV9bMlNmiip04MDAcyorHTmLGXu249I%2Fj7LBAYmQMPj6KaM7eTZKcTlq%2FzmpgPRyLWv3BghXIdQE492N%2FJaEFuGzSdo86YJAxVRzq3Bfy%2B9qTau1oCqdnQoREw6NO6uhHeUbW%2B4%2FZhGJXew4NJjxuG%2BdIXXrbu5c0foftGjHtmDKZOnlz%2FWCQcyem7ajOdBFU1GLOJI3iiK5klPxziKd6Q8p6duqOkxm9hABS35nTHXL%2FG4LrH5g2sAEZBvc2Wb4rqcwjsj4vAY6pgHvU80YMQH%2B%2FNmiUvwpOMt6Mq9dtl2htfiHDPmCxGT43c3mgPfEvRDOsLUocS8Im20mtZ5HR9INZ1mUZIMhegG%2FznmX7sDPyOYkcOZ7QAFQa2%2FL9jYbWWAmgMaGoc7ztVSyhrskqDsnxHLeWvfBOasPzOOXSyT8YVMwB1tH9iHMA6B20q%2FmILMDQa254rkU9WLt2ntdXRLUMcosuD509fNIWKlPD1Df&X-Amz-Signature=ba4e5e7b0cf192dc9a035bdfe865776b7afea7e6f140491183e5cc4a5e43e16a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
