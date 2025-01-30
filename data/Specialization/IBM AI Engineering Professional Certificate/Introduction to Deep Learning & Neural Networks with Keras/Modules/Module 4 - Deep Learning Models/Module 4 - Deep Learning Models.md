

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAIQZEAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyGA9bSdvPIGQWoEC%2B%2BkzXKivAppNYy2Tu3b0qjsRefAIhAKK9m%2FipVjPkoCyRyb5Xm8NGBZ%2FJigtUCrI7prfZ6CxyKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2bfBVbakOhWp3GfYq3AO8B5838pVaWUN3%2FtySEvknfum7OAJDfzbMjP7GYerHt0gETqAoLjUbmj9C8OAdmreFIV5zHURYCMZWMX5sPS4hZC0MI9Ao5KTmNyWAww%2Bs2nbtOsiR2v4%2FqwWK%2BKvdCOYjMd8rZSq3whkk%2B%2BNE%2BWNzgbHpPyicxCV%2BfGfhhEAzy%2BHtRX6BhPxS2z%2B3%2FkQeRRzb0J%2BvqCKfWRg3NTXWnz53cnrt%2B8bLk%2FhV%2BBPEnMU895m6IFDXUWqhzbaOuIaMVvMl1bwM1TrF4tfpBzv11LLxfiwZGysAPlieZ7p27AIRNlf8yZQV7JAK%2BwEgkdqWwW6pxjRmQ7p8nBkFyyeOtmFWEMt5kKFP%2B%2FxBAXyMlgR%2FDXGSURoTvuZfrq3uFcRzkO3Mzz%2F%2B5viOv9WA%2F4uefc74cVc6TCzNVEdDsVGgpTozHlw45mny8u6bzjDN%2FJN8i%2BNY6EFrTwSs3lEJ58M0BNCcwtUsUFo%2Fb0nnG98zFlWil2GGAnyh8i6%2FKiFPvCmKgjv%2BKrMhvGNwJu2rIVyvCGOGP5wbmPYG%2BVMUN61PGHuXHrzqeCEfov%2ByJWIs844SCrFFm5V%2FzRUvf4yJ5hR6NAYTQp2iYwOxSsj%2FbQ%2Bl1dzOMuAnbnouGXXgAqIXyzDnouy8BjqkAVXAgk60m1eTnzMLroloky%2Fsy6X2cdF1lzLfupuAIL7PB3pP3PvGxqzXZK2FYXvu6qAa1yfUYZ%2B22zeYcMDUnWtG459%2F%2BrnvwjXlNELJU4gkt%2FTT81ZvqznZAD%2Bbl0NZFPvlm0vHLnt42%2BTWhR%2FWQLRtge9IrtonEdOWWlLJx3fs3fBxWyICceclGb0a97IRKcDRklKB6WuMMc%2F7QyctLyy2iw2H&X-Amz-Signature=24ecac46c263d9d43b42ff1bd93678eb77a78e499cf6483a521c945d6a1ed90f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAIQZEAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyGA9bSdvPIGQWoEC%2B%2BkzXKivAppNYy2Tu3b0qjsRefAIhAKK9m%2FipVjPkoCyRyb5Xm8NGBZ%2FJigtUCrI7prfZ6CxyKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2bfBVbakOhWp3GfYq3AO8B5838pVaWUN3%2FtySEvknfum7OAJDfzbMjP7GYerHt0gETqAoLjUbmj9C8OAdmreFIV5zHURYCMZWMX5sPS4hZC0MI9Ao5KTmNyWAww%2Bs2nbtOsiR2v4%2FqwWK%2BKvdCOYjMd8rZSq3whkk%2B%2BNE%2BWNzgbHpPyicxCV%2BfGfhhEAzy%2BHtRX6BhPxS2z%2B3%2FkQeRRzb0J%2BvqCKfWRg3NTXWnz53cnrt%2B8bLk%2FhV%2BBPEnMU895m6IFDXUWqhzbaOuIaMVvMl1bwM1TrF4tfpBzv11LLxfiwZGysAPlieZ7p27AIRNlf8yZQV7JAK%2BwEgkdqWwW6pxjRmQ7p8nBkFyyeOtmFWEMt5kKFP%2B%2FxBAXyMlgR%2FDXGSURoTvuZfrq3uFcRzkO3Mzz%2F%2B5viOv9WA%2F4uefc74cVc6TCzNVEdDsVGgpTozHlw45mny8u6bzjDN%2FJN8i%2BNY6EFrTwSs3lEJ58M0BNCcwtUsUFo%2Fb0nnG98zFlWil2GGAnyh8i6%2FKiFPvCmKgjv%2BKrMhvGNwJu2rIVyvCGOGP5wbmPYG%2BVMUN61PGHuXHrzqeCEfov%2ByJWIs844SCrFFm5V%2FzRUvf4yJ5hR6NAYTQp2iYwOxSsj%2FbQ%2Bl1dzOMuAnbnouGXXgAqIXyzDnouy8BjqkAVXAgk60m1eTnzMLroloky%2Fsy6X2cdF1lzLfupuAIL7PB3pP3PvGxqzXZK2FYXvu6qAa1yfUYZ%2B22zeYcMDUnWtG459%2F%2BrnvwjXlNELJU4gkt%2FTT81ZvqznZAD%2Bbl0NZFPvlm0vHLnt42%2BTWhR%2FWQLRtge9IrtonEdOWWlLJx3fs3fBxWyICceclGb0a97IRKcDRklKB6WuMMc%2F7QyctLyy2iw2H&X-Amz-Signature=0d5a9f1570e9cec64f0348717782f63680b55a8194267ee0fdd2aff566557a85&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAIQZEAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyGA9bSdvPIGQWoEC%2B%2BkzXKivAppNYy2Tu3b0qjsRefAIhAKK9m%2FipVjPkoCyRyb5Xm8NGBZ%2FJigtUCrI7prfZ6CxyKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2bfBVbakOhWp3GfYq3AO8B5838pVaWUN3%2FtySEvknfum7OAJDfzbMjP7GYerHt0gETqAoLjUbmj9C8OAdmreFIV5zHURYCMZWMX5sPS4hZC0MI9Ao5KTmNyWAww%2Bs2nbtOsiR2v4%2FqwWK%2BKvdCOYjMd8rZSq3whkk%2B%2BNE%2BWNzgbHpPyicxCV%2BfGfhhEAzy%2BHtRX6BhPxS2z%2B3%2FkQeRRzb0J%2BvqCKfWRg3NTXWnz53cnrt%2B8bLk%2FhV%2BBPEnMU895m6IFDXUWqhzbaOuIaMVvMl1bwM1TrF4tfpBzv11LLxfiwZGysAPlieZ7p27AIRNlf8yZQV7JAK%2BwEgkdqWwW6pxjRmQ7p8nBkFyyeOtmFWEMt5kKFP%2B%2FxBAXyMlgR%2FDXGSURoTvuZfrq3uFcRzkO3Mzz%2F%2B5viOv9WA%2F4uefc74cVc6TCzNVEdDsVGgpTozHlw45mny8u6bzjDN%2FJN8i%2BNY6EFrTwSs3lEJ58M0BNCcwtUsUFo%2Fb0nnG98zFlWil2GGAnyh8i6%2FKiFPvCmKgjv%2BKrMhvGNwJu2rIVyvCGOGP5wbmPYG%2BVMUN61PGHuXHrzqeCEfov%2ByJWIs844SCrFFm5V%2FzRUvf4yJ5hR6NAYTQp2iYwOxSsj%2FbQ%2Bl1dzOMuAnbnouGXXgAqIXyzDnouy8BjqkAVXAgk60m1eTnzMLroloky%2Fsy6X2cdF1lzLfupuAIL7PB3pP3PvGxqzXZK2FYXvu6qAa1yfUYZ%2B22zeYcMDUnWtG459%2F%2BrnvwjXlNELJU4gkt%2FTT81ZvqznZAD%2Bbl0NZFPvlm0vHLnt42%2BTWhR%2FWQLRtge9IrtonEdOWWlLJx3fs3fBxWyICceclGb0a97IRKcDRklKB6WuMMc%2F7QyctLyy2iw2H&X-Amz-Signature=74e460c2f74946537bef5aca6da60fcdac80302824d4e46ce582e246009d7fe7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAIQZEAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyGA9bSdvPIGQWoEC%2B%2BkzXKivAppNYy2Tu3b0qjsRefAIhAKK9m%2FipVjPkoCyRyb5Xm8NGBZ%2FJigtUCrI7prfZ6CxyKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2bfBVbakOhWp3GfYq3AO8B5838pVaWUN3%2FtySEvknfum7OAJDfzbMjP7GYerHt0gETqAoLjUbmj9C8OAdmreFIV5zHURYCMZWMX5sPS4hZC0MI9Ao5KTmNyWAww%2Bs2nbtOsiR2v4%2FqwWK%2BKvdCOYjMd8rZSq3whkk%2B%2BNE%2BWNzgbHpPyicxCV%2BfGfhhEAzy%2BHtRX6BhPxS2z%2B3%2FkQeRRzb0J%2BvqCKfWRg3NTXWnz53cnrt%2B8bLk%2FhV%2BBPEnMU895m6IFDXUWqhzbaOuIaMVvMl1bwM1TrF4tfpBzv11LLxfiwZGysAPlieZ7p27AIRNlf8yZQV7JAK%2BwEgkdqWwW6pxjRmQ7p8nBkFyyeOtmFWEMt5kKFP%2B%2FxBAXyMlgR%2FDXGSURoTvuZfrq3uFcRzkO3Mzz%2F%2B5viOv9WA%2F4uefc74cVc6TCzNVEdDsVGgpTozHlw45mny8u6bzjDN%2FJN8i%2BNY6EFrTwSs3lEJ58M0BNCcwtUsUFo%2Fb0nnG98zFlWil2GGAnyh8i6%2FKiFPvCmKgjv%2BKrMhvGNwJu2rIVyvCGOGP5wbmPYG%2BVMUN61PGHuXHrzqeCEfov%2ByJWIs844SCrFFm5V%2FzRUvf4yJ5hR6NAYTQp2iYwOxSsj%2FbQ%2Bl1dzOMuAnbnouGXXgAqIXyzDnouy8BjqkAVXAgk60m1eTnzMLroloky%2Fsy6X2cdF1lzLfupuAIL7PB3pP3PvGxqzXZK2FYXvu6qAa1yfUYZ%2B22zeYcMDUnWtG459%2F%2BrnvwjXlNELJU4gkt%2FTT81ZvqznZAD%2Bbl0NZFPvlm0vHLnt42%2BTWhR%2FWQLRtge9IrtonEdOWWlLJx3fs3fBxWyICceclGb0a97IRKcDRklKB6WuMMc%2F7QyctLyy2iw2H&X-Amz-Signature=2bfe1996f82e89fd0f89b23061d8717ac504d03078bdd737edd6c4777ac7cf24&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAIQZEAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyGA9bSdvPIGQWoEC%2B%2BkzXKivAppNYy2Tu3b0qjsRefAIhAKK9m%2FipVjPkoCyRyb5Xm8NGBZ%2FJigtUCrI7prfZ6CxyKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2bfBVbakOhWp3GfYq3AO8B5838pVaWUN3%2FtySEvknfum7OAJDfzbMjP7GYerHt0gETqAoLjUbmj9C8OAdmreFIV5zHURYCMZWMX5sPS4hZC0MI9Ao5KTmNyWAww%2Bs2nbtOsiR2v4%2FqwWK%2BKvdCOYjMd8rZSq3whkk%2B%2BNE%2BWNzgbHpPyicxCV%2BfGfhhEAzy%2BHtRX6BhPxS2z%2B3%2FkQeRRzb0J%2BvqCKfWRg3NTXWnz53cnrt%2B8bLk%2FhV%2BBPEnMU895m6IFDXUWqhzbaOuIaMVvMl1bwM1TrF4tfpBzv11LLxfiwZGysAPlieZ7p27AIRNlf8yZQV7JAK%2BwEgkdqWwW6pxjRmQ7p8nBkFyyeOtmFWEMt5kKFP%2B%2FxBAXyMlgR%2FDXGSURoTvuZfrq3uFcRzkO3Mzz%2F%2B5viOv9WA%2F4uefc74cVc6TCzNVEdDsVGgpTozHlw45mny8u6bzjDN%2FJN8i%2BNY6EFrTwSs3lEJ58M0BNCcwtUsUFo%2Fb0nnG98zFlWil2GGAnyh8i6%2FKiFPvCmKgjv%2BKrMhvGNwJu2rIVyvCGOGP5wbmPYG%2BVMUN61PGHuXHrzqeCEfov%2ByJWIs844SCrFFm5V%2FzRUvf4yJ5hR6NAYTQp2iYwOxSsj%2FbQ%2Bl1dzOMuAnbnouGXXgAqIXyzDnouy8BjqkAVXAgk60m1eTnzMLroloky%2Fsy6X2cdF1lzLfupuAIL7PB3pP3PvGxqzXZK2FYXvu6qAa1yfUYZ%2B22zeYcMDUnWtG459%2F%2BrnvwjXlNELJU4gkt%2FTT81ZvqznZAD%2Bbl0NZFPvlm0vHLnt42%2BTWhR%2FWQLRtge9IrtonEdOWWlLJx3fs3fBxWyICceclGb0a97IRKcDRklKB6WuMMc%2F7QyctLyy2iw2H&X-Amz-Signature=75bad0da8276912d18979e9ad8bb0483ac201f9e8c494e81889a0d9eb428a110&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAIQZEAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyGA9bSdvPIGQWoEC%2B%2BkzXKivAppNYy2Tu3b0qjsRefAIhAKK9m%2FipVjPkoCyRyb5Xm8NGBZ%2FJigtUCrI7prfZ6CxyKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2bfBVbakOhWp3GfYq3AO8B5838pVaWUN3%2FtySEvknfum7OAJDfzbMjP7GYerHt0gETqAoLjUbmj9C8OAdmreFIV5zHURYCMZWMX5sPS4hZC0MI9Ao5KTmNyWAww%2Bs2nbtOsiR2v4%2FqwWK%2BKvdCOYjMd8rZSq3whkk%2B%2BNE%2BWNzgbHpPyicxCV%2BfGfhhEAzy%2BHtRX6BhPxS2z%2B3%2FkQeRRzb0J%2BvqCKfWRg3NTXWnz53cnrt%2B8bLk%2FhV%2BBPEnMU895m6IFDXUWqhzbaOuIaMVvMl1bwM1TrF4tfpBzv11LLxfiwZGysAPlieZ7p27AIRNlf8yZQV7JAK%2BwEgkdqWwW6pxjRmQ7p8nBkFyyeOtmFWEMt5kKFP%2B%2FxBAXyMlgR%2FDXGSURoTvuZfrq3uFcRzkO3Mzz%2F%2B5viOv9WA%2F4uefc74cVc6TCzNVEdDsVGgpTozHlw45mny8u6bzjDN%2FJN8i%2BNY6EFrTwSs3lEJ58M0BNCcwtUsUFo%2Fb0nnG98zFlWil2GGAnyh8i6%2FKiFPvCmKgjv%2BKrMhvGNwJu2rIVyvCGOGP5wbmPYG%2BVMUN61PGHuXHrzqeCEfov%2ByJWIs844SCrFFm5V%2FzRUvf4yJ5hR6NAYTQp2iYwOxSsj%2FbQ%2Bl1dzOMuAnbnouGXXgAqIXyzDnouy8BjqkAVXAgk60m1eTnzMLroloky%2Fsy6X2cdF1lzLfupuAIL7PB3pP3PvGxqzXZK2FYXvu6qAa1yfUYZ%2B22zeYcMDUnWtG459%2F%2BrnvwjXlNELJU4gkt%2FTT81ZvqznZAD%2Bbl0NZFPvlm0vHLnt42%2BTWhR%2FWQLRtge9IrtonEdOWWlLJx3fs3fBxWyICceclGb0a97IRKcDRklKB6WuMMc%2F7QyctLyy2iw2H&X-Amz-Signature=c47637aaceef87f965c7e76efdab2d74d688e90504335b0f09e5465d20b1c5a6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAIQZEAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyGA9bSdvPIGQWoEC%2B%2BkzXKivAppNYy2Tu3b0qjsRefAIhAKK9m%2FipVjPkoCyRyb5Xm8NGBZ%2FJigtUCrI7prfZ6CxyKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2bfBVbakOhWp3GfYq3AO8B5838pVaWUN3%2FtySEvknfum7OAJDfzbMjP7GYerHt0gETqAoLjUbmj9C8OAdmreFIV5zHURYCMZWMX5sPS4hZC0MI9Ao5KTmNyWAww%2Bs2nbtOsiR2v4%2FqwWK%2BKvdCOYjMd8rZSq3whkk%2B%2BNE%2BWNzgbHpPyicxCV%2BfGfhhEAzy%2BHtRX6BhPxS2z%2B3%2FkQeRRzb0J%2BvqCKfWRg3NTXWnz53cnrt%2B8bLk%2FhV%2BBPEnMU895m6IFDXUWqhzbaOuIaMVvMl1bwM1TrF4tfpBzv11LLxfiwZGysAPlieZ7p27AIRNlf8yZQV7JAK%2BwEgkdqWwW6pxjRmQ7p8nBkFyyeOtmFWEMt5kKFP%2B%2FxBAXyMlgR%2FDXGSURoTvuZfrq3uFcRzkO3Mzz%2F%2B5viOv9WA%2F4uefc74cVc6TCzNVEdDsVGgpTozHlw45mny8u6bzjDN%2FJN8i%2BNY6EFrTwSs3lEJ58M0BNCcwtUsUFo%2Fb0nnG98zFlWil2GGAnyh8i6%2FKiFPvCmKgjv%2BKrMhvGNwJu2rIVyvCGOGP5wbmPYG%2BVMUN61PGHuXHrzqeCEfov%2ByJWIs844SCrFFm5V%2FzRUvf4yJ5hR6NAYTQp2iYwOxSsj%2FbQ%2Bl1dzOMuAnbnouGXXgAqIXyzDnouy8BjqkAVXAgk60m1eTnzMLroloky%2Fsy6X2cdF1lzLfupuAIL7PB3pP3PvGxqzXZK2FYXvu6qAa1yfUYZ%2B22zeYcMDUnWtG459%2F%2BrnvwjXlNELJU4gkt%2FTT81ZvqznZAD%2Bbl0NZFPvlm0vHLnt42%2BTWhR%2FWQLRtge9IrtonEdOWWlLJx3fs3fBxWyICceclGb0a97IRKcDRklKB6WuMMc%2F7QyctLyy2iw2H&X-Amz-Signature=866d0d81ec0115a8b2ccf534071e66b4171b0e2495c3704a9fc3fe2bf12051d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAIQZEAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyGA9bSdvPIGQWoEC%2B%2BkzXKivAppNYy2Tu3b0qjsRefAIhAKK9m%2FipVjPkoCyRyb5Xm8NGBZ%2FJigtUCrI7prfZ6CxyKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2bfBVbakOhWp3GfYq3AO8B5838pVaWUN3%2FtySEvknfum7OAJDfzbMjP7GYerHt0gETqAoLjUbmj9C8OAdmreFIV5zHURYCMZWMX5sPS4hZC0MI9Ao5KTmNyWAww%2Bs2nbtOsiR2v4%2FqwWK%2BKvdCOYjMd8rZSq3whkk%2B%2BNE%2BWNzgbHpPyicxCV%2BfGfhhEAzy%2BHtRX6BhPxS2z%2B3%2FkQeRRzb0J%2BvqCKfWRg3NTXWnz53cnrt%2B8bLk%2FhV%2BBPEnMU895m6IFDXUWqhzbaOuIaMVvMl1bwM1TrF4tfpBzv11LLxfiwZGysAPlieZ7p27AIRNlf8yZQV7JAK%2BwEgkdqWwW6pxjRmQ7p8nBkFyyeOtmFWEMt5kKFP%2B%2FxBAXyMlgR%2FDXGSURoTvuZfrq3uFcRzkO3Mzz%2F%2B5viOv9WA%2F4uefc74cVc6TCzNVEdDsVGgpTozHlw45mny8u6bzjDN%2FJN8i%2BNY6EFrTwSs3lEJ58M0BNCcwtUsUFo%2Fb0nnG98zFlWil2GGAnyh8i6%2FKiFPvCmKgjv%2BKrMhvGNwJu2rIVyvCGOGP5wbmPYG%2BVMUN61PGHuXHrzqeCEfov%2ByJWIs844SCrFFm5V%2FzRUvf4yJ5hR6NAYTQp2iYwOxSsj%2FbQ%2Bl1dzOMuAnbnouGXXgAqIXyzDnouy8BjqkAVXAgk60m1eTnzMLroloky%2Fsy6X2cdF1lzLfupuAIL7PB3pP3PvGxqzXZK2FYXvu6qAa1yfUYZ%2B22zeYcMDUnWtG459%2F%2BrnvwjXlNELJU4gkt%2FTT81ZvqznZAD%2Bbl0NZFPvlm0vHLnt42%2BTWhR%2FWQLRtge9IrtonEdOWWlLJx3fs3fBxWyICceclGb0a97IRKcDRklKB6WuMMc%2F7QyctLyy2iw2H&X-Amz-Signature=ee4a274ead50a39d46a34a87b8088b2d3b347f28076efae07087dd1c3bb3e15c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAIQZEAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyGA9bSdvPIGQWoEC%2B%2BkzXKivAppNYy2Tu3b0qjsRefAIhAKK9m%2FipVjPkoCyRyb5Xm8NGBZ%2FJigtUCrI7prfZ6CxyKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2bfBVbakOhWp3GfYq3AO8B5838pVaWUN3%2FtySEvknfum7OAJDfzbMjP7GYerHt0gETqAoLjUbmj9C8OAdmreFIV5zHURYCMZWMX5sPS4hZC0MI9Ao5KTmNyWAww%2Bs2nbtOsiR2v4%2FqwWK%2BKvdCOYjMd8rZSq3whkk%2B%2BNE%2BWNzgbHpPyicxCV%2BfGfhhEAzy%2BHtRX6BhPxS2z%2B3%2FkQeRRzb0J%2BvqCKfWRg3NTXWnz53cnrt%2B8bLk%2FhV%2BBPEnMU895m6IFDXUWqhzbaOuIaMVvMl1bwM1TrF4tfpBzv11LLxfiwZGysAPlieZ7p27AIRNlf8yZQV7JAK%2BwEgkdqWwW6pxjRmQ7p8nBkFyyeOtmFWEMt5kKFP%2B%2FxBAXyMlgR%2FDXGSURoTvuZfrq3uFcRzkO3Mzz%2F%2B5viOv9WA%2F4uefc74cVc6TCzNVEdDsVGgpTozHlw45mny8u6bzjDN%2FJN8i%2BNY6EFrTwSs3lEJ58M0BNCcwtUsUFo%2Fb0nnG98zFlWil2GGAnyh8i6%2FKiFPvCmKgjv%2BKrMhvGNwJu2rIVyvCGOGP5wbmPYG%2BVMUN61PGHuXHrzqeCEfov%2ByJWIs844SCrFFm5V%2FzRUvf4yJ5hR6NAYTQp2iYwOxSsj%2FbQ%2Bl1dzOMuAnbnouGXXgAqIXyzDnouy8BjqkAVXAgk60m1eTnzMLroloky%2Fsy6X2cdF1lzLfupuAIL7PB3pP3PvGxqzXZK2FYXvu6qAa1yfUYZ%2B22zeYcMDUnWtG459%2F%2BrnvwjXlNELJU4gkt%2FTT81ZvqznZAD%2Bbl0NZFPvlm0vHLnt42%2BTWhR%2FWQLRtge9IrtonEdOWWlLJx3fs3fBxWyICceclGb0a97IRKcDRklKB6WuMMc%2F7QyctLyy2iw2H&X-Amz-Signature=cdf6b9501f120ed25e5af172e7426c6ca2e6ed3990cb284578c216f3fef3016d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKAT2NLA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F4%2FD0QaW%2BCu%2BYyfgucoX8Hcpgzu3ttXsJDUZf9iGe8wIgNpfyqad3QlWA3LzyMvCOAGFiMPI9d8p40hT0sjwAJYwqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx9FmPb0JWZy%2BmPeSrcAzRQnOegAusrMknnaVwL%2B4L%2F3oAAd%2FXg327eFHOMNhaUbu%2FbBH8sL1LQbrml9SoJCUhMxMYnuXXlZ0wF%2BBWejwMIKNFBq%2F8wqHl1fxykC62XV13dBvsRRt6XFlfXQHCblMPMiKVHe3PbLyJPakDzLU6xvz6dzNOBpsLT%2FbpjK3Zs91XJmHj5BB8Aw%2ByUcR1xiYWkcn26zAELK7h3TFyVB9QNyTpd4hkWq3D8tvHyEAT30iorgIK7Bfe%2BJfEzs6E0J6MH9N9yHd1LjnRPRXwB0VlX25rXSD8HEIiwOMnJdZJ%2FD%2BWHkishRypvcK29HBceQzqDCRGa%2BrtY%2Bn%2FYgrkavgosrRs747eRlXwWAx61p2BjHLA%2BnGqnB%2F6VqOwoXGBaj%2BHTTdwBKaYjZGgjChWZtCUWmbomIqzxHgjY5rt3%2B3DUsqYqY7M3%2BWozg3Ap%2F8NdrrhIjLQe3VI2W9jKwCB%2BiWUTqc80mpNO5iZEDV96Lb5aN8sn55x%2BBzcI8RywIz26Ow7bAY9B2ZM7cG9jjuPLETXZjKCY3ke4Ho%2Fn9dLosAbcfO4RO%2F59OURUVyH%2Fs5HHPTiiGOQ%2BYRuPzzY4tQ71f%2FtF8ss1N96a5YyL9IFviNobehlILv%2F%2FNtbW0usfMNmi7LwGOqUBRgWHkJT82Ru4FE7ERGJSZFyIExL%2BWE3S%2Bcm6jMUb4ADzbP8TT8eAqv7Gwzh53vc3BiiJP%2Fhd81JO61xScPdP0oc2qguR2H9TC6Be%2BqdGB7QmF1Lf%2BS%2FHZu5h8wK1wS3PvA%2FM9M0lQXVP4QGgerI0IL9Z57NTyZuzZVH5s65lbx7wXta6lAsxuUYCZzbeeJJgpnqMDWXsat99%2FKD6VZoVJ8SLcqBs&X-Amz-Signature=ea6cddca8b638068e7a05446da6b0c7beb3e0de535addd9f01b32f48e11eab4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKAT2NLA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F4%2FD0QaW%2BCu%2BYyfgucoX8Hcpgzu3ttXsJDUZf9iGe8wIgNpfyqad3QlWA3LzyMvCOAGFiMPI9d8p40hT0sjwAJYwqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx9FmPb0JWZy%2BmPeSrcAzRQnOegAusrMknnaVwL%2B4L%2F3oAAd%2FXg327eFHOMNhaUbu%2FbBH8sL1LQbrml9SoJCUhMxMYnuXXlZ0wF%2BBWejwMIKNFBq%2F8wqHl1fxykC62XV13dBvsRRt6XFlfXQHCblMPMiKVHe3PbLyJPakDzLU6xvz6dzNOBpsLT%2FbpjK3Zs91XJmHj5BB8Aw%2ByUcR1xiYWkcn26zAELK7h3TFyVB9QNyTpd4hkWq3D8tvHyEAT30iorgIK7Bfe%2BJfEzs6E0J6MH9N9yHd1LjnRPRXwB0VlX25rXSD8HEIiwOMnJdZJ%2FD%2BWHkishRypvcK29HBceQzqDCRGa%2BrtY%2Bn%2FYgrkavgosrRs747eRlXwWAx61p2BjHLA%2BnGqnB%2F6VqOwoXGBaj%2BHTTdwBKaYjZGgjChWZtCUWmbomIqzxHgjY5rt3%2B3DUsqYqY7M3%2BWozg3Ap%2F8NdrrhIjLQe3VI2W9jKwCB%2BiWUTqc80mpNO5iZEDV96Lb5aN8sn55x%2BBzcI8RywIz26Ow7bAY9B2ZM7cG9jjuPLETXZjKCY3ke4Ho%2Fn9dLosAbcfO4RO%2F59OURUVyH%2Fs5HHPTiiGOQ%2BYRuPzzY4tQ71f%2FtF8ss1N96a5YyL9IFviNobehlILv%2F%2FNtbW0usfMNmi7LwGOqUBRgWHkJT82Ru4FE7ERGJSZFyIExL%2BWE3S%2Bcm6jMUb4ADzbP8TT8eAqv7Gwzh53vc3BiiJP%2Fhd81JO61xScPdP0oc2qguR2H9TC6Be%2BqdGB7QmF1Lf%2BS%2FHZu5h8wK1wS3PvA%2FM9M0lQXVP4QGgerI0IL9Z57NTyZuzZVH5s65lbx7wXta6lAsxuUYCZzbeeJJgpnqMDWXsat99%2FKD6VZoVJ8SLcqBs&X-Amz-Signature=9a79e72684498a5a22e937c3f0b23032759b8415322aabfb8d1b071d25ee8ad4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
