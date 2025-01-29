

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QTXO67M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI%2BUoyt4QBn8Ub80qX43QuN5EmC5fRgqxU67TVjIaMLgIhAKXvRPZO47e4JZzSYaj4xGypLc2z9WhE0wnIXD4dttibKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOoUlq5lMGGqzlkSIq3APyLZH0EphJubQdtj8ckq5Psi4vx3XqNP9rqnWyQgJL24dbC6i%2FLjjohNrhuZSZIcVADHRJwhGmLN1noVox%2BGFXUKCuHsMjS%2FjuCn%2FTA6%2BZcOeG5ViBj%2FlchwSttYBW%2FTgDFGL8HntED49preU%2BCdAxqvP%2BJESg4Z%2F49EnMONePDFGH5LAzjJ%2BKwuu%2BDdArCPKo9Id6uCSUSWwJ0%2Fwt3smu97PpEGkQNW4fYJ%2Fxed8Y%2FWPhFN1yMk7Rb0ohSxw9QKT%2BPn97XNNbZ2RZVB0j66JJnFGGaOZdAxrxMA8Hl%2FJz1RXbQTH%2B865ibUtIfjXZ6wUEwIr3Id3hTd11DcTooHbIEs7hcaOZtCv7MoJK88ME9K1%2FSK8otN7FKOTZdznO8SjU57PHdwzqbtO%2F1LD2tUx7RAfRHoYQ%2B2AV%2F%2BBxCYIh4%2BOYMhMRecDwXfD%2FrGkBL%2B2Uzxpwvc0onq7evq5eqh2qzZ8w3Rq21Rr7Cb82hvzV0c%2FmRtCtpJ9ZBvGBwBainc9V9i4kUoFw8wuZq5d2wv8qrMzGG0I3U6SwK7MGsTjg8jL0xVeyzf3ct5EroPYnKfObSX5YKsTPRZdB102cPQnAKd6oMvnqvKcAd42YMpbA1flgFTJ%2F3%2F1d3qc0djDb5%2Bi8BjqkASQhBa196IHo8Uxfg3uerjS%2F0x9lgbBliPDXE6p5nDSFfWjyQ%2BDinLuV6GpLZBPZQeRLUc%2F2PTWFNhTL3f%2Fc0GtsTzscxt66NCyCxzTvgvqtAN4owysGMLE%2FWMOH2%2FO2ViYQlvm%2Bgk1LS8%2Fx9%2BDuWV%2FX2w4y7atC5b8ie%2BfsEbIgNvyrzKauf5bT1mduSCcxHWPjwt6hsWFH4t%2FS%2Fgkvn%2BXMDMzR&X-Amz-Signature=3a56e8591dd410bbfb0000ec796074e5d2d12f8107f7b2fe2199d4691e5b38d9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QTXO67M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI%2BUoyt4QBn8Ub80qX43QuN5EmC5fRgqxU67TVjIaMLgIhAKXvRPZO47e4JZzSYaj4xGypLc2z9WhE0wnIXD4dttibKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOoUlq5lMGGqzlkSIq3APyLZH0EphJubQdtj8ckq5Psi4vx3XqNP9rqnWyQgJL24dbC6i%2FLjjohNrhuZSZIcVADHRJwhGmLN1noVox%2BGFXUKCuHsMjS%2FjuCn%2FTA6%2BZcOeG5ViBj%2FlchwSttYBW%2FTgDFGL8HntED49preU%2BCdAxqvP%2BJESg4Z%2F49EnMONePDFGH5LAzjJ%2BKwuu%2BDdArCPKo9Id6uCSUSWwJ0%2Fwt3smu97PpEGkQNW4fYJ%2Fxed8Y%2FWPhFN1yMk7Rb0ohSxw9QKT%2BPn97XNNbZ2RZVB0j66JJnFGGaOZdAxrxMA8Hl%2FJz1RXbQTH%2B865ibUtIfjXZ6wUEwIr3Id3hTd11DcTooHbIEs7hcaOZtCv7MoJK88ME9K1%2FSK8otN7FKOTZdznO8SjU57PHdwzqbtO%2F1LD2tUx7RAfRHoYQ%2B2AV%2F%2BBxCYIh4%2BOYMhMRecDwXfD%2FrGkBL%2B2Uzxpwvc0onq7evq5eqh2qzZ8w3Rq21Rr7Cb82hvzV0c%2FmRtCtpJ9ZBvGBwBainc9V9i4kUoFw8wuZq5d2wv8qrMzGG0I3U6SwK7MGsTjg8jL0xVeyzf3ct5EroPYnKfObSX5YKsTPRZdB102cPQnAKd6oMvnqvKcAd42YMpbA1flgFTJ%2F3%2F1d3qc0djDb5%2Bi8BjqkASQhBa196IHo8Uxfg3uerjS%2F0x9lgbBliPDXE6p5nDSFfWjyQ%2BDinLuV6GpLZBPZQeRLUc%2F2PTWFNhTL3f%2Fc0GtsTzscxt66NCyCxzTvgvqtAN4owysGMLE%2FWMOH2%2FO2ViYQlvm%2Bgk1LS8%2Fx9%2BDuWV%2FX2w4y7atC5b8ie%2BfsEbIgNvyrzKauf5bT1mduSCcxHWPjwt6hsWFH4t%2FS%2Fgkvn%2BXMDMzR&X-Amz-Signature=cb66774ae5a482d217f10d4f8a0868d6d26584515e4a20a7c8622c9fc68ddcd5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QTXO67M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI%2BUoyt4QBn8Ub80qX43QuN5EmC5fRgqxU67TVjIaMLgIhAKXvRPZO47e4JZzSYaj4xGypLc2z9WhE0wnIXD4dttibKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOoUlq5lMGGqzlkSIq3APyLZH0EphJubQdtj8ckq5Psi4vx3XqNP9rqnWyQgJL24dbC6i%2FLjjohNrhuZSZIcVADHRJwhGmLN1noVox%2BGFXUKCuHsMjS%2FjuCn%2FTA6%2BZcOeG5ViBj%2FlchwSttYBW%2FTgDFGL8HntED49preU%2BCdAxqvP%2BJESg4Z%2F49EnMONePDFGH5LAzjJ%2BKwuu%2BDdArCPKo9Id6uCSUSWwJ0%2Fwt3smu97PpEGkQNW4fYJ%2Fxed8Y%2FWPhFN1yMk7Rb0ohSxw9QKT%2BPn97XNNbZ2RZVB0j66JJnFGGaOZdAxrxMA8Hl%2FJz1RXbQTH%2B865ibUtIfjXZ6wUEwIr3Id3hTd11DcTooHbIEs7hcaOZtCv7MoJK88ME9K1%2FSK8otN7FKOTZdznO8SjU57PHdwzqbtO%2F1LD2tUx7RAfRHoYQ%2B2AV%2F%2BBxCYIh4%2BOYMhMRecDwXfD%2FrGkBL%2B2Uzxpwvc0onq7evq5eqh2qzZ8w3Rq21Rr7Cb82hvzV0c%2FmRtCtpJ9ZBvGBwBainc9V9i4kUoFw8wuZq5d2wv8qrMzGG0I3U6SwK7MGsTjg8jL0xVeyzf3ct5EroPYnKfObSX5YKsTPRZdB102cPQnAKd6oMvnqvKcAd42YMpbA1flgFTJ%2F3%2F1d3qc0djDb5%2Bi8BjqkASQhBa196IHo8Uxfg3uerjS%2F0x9lgbBliPDXE6p5nDSFfWjyQ%2BDinLuV6GpLZBPZQeRLUc%2F2PTWFNhTL3f%2Fc0GtsTzscxt66NCyCxzTvgvqtAN4owysGMLE%2FWMOH2%2FO2ViYQlvm%2Bgk1LS8%2Fx9%2BDuWV%2FX2w4y7atC5b8ie%2BfsEbIgNvyrzKauf5bT1mduSCcxHWPjwt6hsWFH4t%2FS%2Fgkvn%2BXMDMzR&X-Amz-Signature=d038a114952868c121d48c94bc8af4219377798fc711521ca705421e084b7611&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QTXO67M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI%2BUoyt4QBn8Ub80qX43QuN5EmC5fRgqxU67TVjIaMLgIhAKXvRPZO47e4JZzSYaj4xGypLc2z9WhE0wnIXD4dttibKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOoUlq5lMGGqzlkSIq3APyLZH0EphJubQdtj8ckq5Psi4vx3XqNP9rqnWyQgJL24dbC6i%2FLjjohNrhuZSZIcVADHRJwhGmLN1noVox%2BGFXUKCuHsMjS%2FjuCn%2FTA6%2BZcOeG5ViBj%2FlchwSttYBW%2FTgDFGL8HntED49preU%2BCdAxqvP%2BJESg4Z%2F49EnMONePDFGH5LAzjJ%2BKwuu%2BDdArCPKo9Id6uCSUSWwJ0%2Fwt3smu97PpEGkQNW4fYJ%2Fxed8Y%2FWPhFN1yMk7Rb0ohSxw9QKT%2BPn97XNNbZ2RZVB0j66JJnFGGaOZdAxrxMA8Hl%2FJz1RXbQTH%2B865ibUtIfjXZ6wUEwIr3Id3hTd11DcTooHbIEs7hcaOZtCv7MoJK88ME9K1%2FSK8otN7FKOTZdznO8SjU57PHdwzqbtO%2F1LD2tUx7RAfRHoYQ%2B2AV%2F%2BBxCYIh4%2BOYMhMRecDwXfD%2FrGkBL%2B2Uzxpwvc0onq7evq5eqh2qzZ8w3Rq21Rr7Cb82hvzV0c%2FmRtCtpJ9ZBvGBwBainc9V9i4kUoFw8wuZq5d2wv8qrMzGG0I3U6SwK7MGsTjg8jL0xVeyzf3ct5EroPYnKfObSX5YKsTPRZdB102cPQnAKd6oMvnqvKcAd42YMpbA1flgFTJ%2F3%2F1d3qc0djDb5%2Bi8BjqkASQhBa196IHo8Uxfg3uerjS%2F0x9lgbBliPDXE6p5nDSFfWjyQ%2BDinLuV6GpLZBPZQeRLUc%2F2PTWFNhTL3f%2Fc0GtsTzscxt66NCyCxzTvgvqtAN4owysGMLE%2FWMOH2%2FO2ViYQlvm%2Bgk1LS8%2Fx9%2BDuWV%2FX2w4y7atC5b8ie%2BfsEbIgNvyrzKauf5bT1mduSCcxHWPjwt6hsWFH4t%2FS%2Fgkvn%2BXMDMzR&X-Amz-Signature=2d29ef7bff9704a9df7be8f1d9fc06824b7b5277f72b6351c002c634dd5b05c6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QTXO67M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI%2BUoyt4QBn8Ub80qX43QuN5EmC5fRgqxU67TVjIaMLgIhAKXvRPZO47e4JZzSYaj4xGypLc2z9WhE0wnIXD4dttibKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOoUlq5lMGGqzlkSIq3APyLZH0EphJubQdtj8ckq5Psi4vx3XqNP9rqnWyQgJL24dbC6i%2FLjjohNrhuZSZIcVADHRJwhGmLN1noVox%2BGFXUKCuHsMjS%2FjuCn%2FTA6%2BZcOeG5ViBj%2FlchwSttYBW%2FTgDFGL8HntED49preU%2BCdAxqvP%2BJESg4Z%2F49EnMONePDFGH5LAzjJ%2BKwuu%2BDdArCPKo9Id6uCSUSWwJ0%2Fwt3smu97PpEGkQNW4fYJ%2Fxed8Y%2FWPhFN1yMk7Rb0ohSxw9QKT%2BPn97XNNbZ2RZVB0j66JJnFGGaOZdAxrxMA8Hl%2FJz1RXbQTH%2B865ibUtIfjXZ6wUEwIr3Id3hTd11DcTooHbIEs7hcaOZtCv7MoJK88ME9K1%2FSK8otN7FKOTZdznO8SjU57PHdwzqbtO%2F1LD2tUx7RAfRHoYQ%2B2AV%2F%2BBxCYIh4%2BOYMhMRecDwXfD%2FrGkBL%2B2Uzxpwvc0onq7evq5eqh2qzZ8w3Rq21Rr7Cb82hvzV0c%2FmRtCtpJ9ZBvGBwBainc9V9i4kUoFw8wuZq5d2wv8qrMzGG0I3U6SwK7MGsTjg8jL0xVeyzf3ct5EroPYnKfObSX5YKsTPRZdB102cPQnAKd6oMvnqvKcAd42YMpbA1flgFTJ%2F3%2F1d3qc0djDb5%2Bi8BjqkASQhBa196IHo8Uxfg3uerjS%2F0x9lgbBliPDXE6p5nDSFfWjyQ%2BDinLuV6GpLZBPZQeRLUc%2F2PTWFNhTL3f%2Fc0GtsTzscxt66NCyCxzTvgvqtAN4owysGMLE%2FWMOH2%2FO2ViYQlvm%2Bgk1LS8%2Fx9%2BDuWV%2FX2w4y7atC5b8ie%2BfsEbIgNvyrzKauf5bT1mduSCcxHWPjwt6hsWFH4t%2FS%2Fgkvn%2BXMDMzR&X-Amz-Signature=f44ef074158336ee45fce874754e4d898f0e2d14a7e4447654971a4793e68755&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QTXO67M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI%2BUoyt4QBn8Ub80qX43QuN5EmC5fRgqxU67TVjIaMLgIhAKXvRPZO47e4JZzSYaj4xGypLc2z9WhE0wnIXD4dttibKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOoUlq5lMGGqzlkSIq3APyLZH0EphJubQdtj8ckq5Psi4vx3XqNP9rqnWyQgJL24dbC6i%2FLjjohNrhuZSZIcVADHRJwhGmLN1noVox%2BGFXUKCuHsMjS%2FjuCn%2FTA6%2BZcOeG5ViBj%2FlchwSttYBW%2FTgDFGL8HntED49preU%2BCdAxqvP%2BJESg4Z%2F49EnMONePDFGH5LAzjJ%2BKwuu%2BDdArCPKo9Id6uCSUSWwJ0%2Fwt3smu97PpEGkQNW4fYJ%2Fxed8Y%2FWPhFN1yMk7Rb0ohSxw9QKT%2BPn97XNNbZ2RZVB0j66JJnFGGaOZdAxrxMA8Hl%2FJz1RXbQTH%2B865ibUtIfjXZ6wUEwIr3Id3hTd11DcTooHbIEs7hcaOZtCv7MoJK88ME9K1%2FSK8otN7FKOTZdznO8SjU57PHdwzqbtO%2F1LD2tUx7RAfRHoYQ%2B2AV%2F%2BBxCYIh4%2BOYMhMRecDwXfD%2FrGkBL%2B2Uzxpwvc0onq7evq5eqh2qzZ8w3Rq21Rr7Cb82hvzV0c%2FmRtCtpJ9ZBvGBwBainc9V9i4kUoFw8wuZq5d2wv8qrMzGG0I3U6SwK7MGsTjg8jL0xVeyzf3ct5EroPYnKfObSX5YKsTPRZdB102cPQnAKd6oMvnqvKcAd42YMpbA1flgFTJ%2F3%2F1d3qc0djDb5%2Bi8BjqkASQhBa196IHo8Uxfg3uerjS%2F0x9lgbBliPDXE6p5nDSFfWjyQ%2BDinLuV6GpLZBPZQeRLUc%2F2PTWFNhTL3f%2Fc0GtsTzscxt66NCyCxzTvgvqtAN4owysGMLE%2FWMOH2%2FO2ViYQlvm%2Bgk1LS8%2Fx9%2BDuWV%2FX2w4y7atC5b8ie%2BfsEbIgNvyrzKauf5bT1mduSCcxHWPjwt6hsWFH4t%2FS%2Fgkvn%2BXMDMzR&X-Amz-Signature=bf2be250ba18ca0a90b6a946019dd6a83575b1662a4c9c051664db4af2ff54aa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QTXO67M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI%2BUoyt4QBn8Ub80qX43QuN5EmC5fRgqxU67TVjIaMLgIhAKXvRPZO47e4JZzSYaj4xGypLc2z9WhE0wnIXD4dttibKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOoUlq5lMGGqzlkSIq3APyLZH0EphJubQdtj8ckq5Psi4vx3XqNP9rqnWyQgJL24dbC6i%2FLjjohNrhuZSZIcVADHRJwhGmLN1noVox%2BGFXUKCuHsMjS%2FjuCn%2FTA6%2BZcOeG5ViBj%2FlchwSttYBW%2FTgDFGL8HntED49preU%2BCdAxqvP%2BJESg4Z%2F49EnMONePDFGH5LAzjJ%2BKwuu%2BDdArCPKo9Id6uCSUSWwJ0%2Fwt3smu97PpEGkQNW4fYJ%2Fxed8Y%2FWPhFN1yMk7Rb0ohSxw9QKT%2BPn97XNNbZ2RZVB0j66JJnFGGaOZdAxrxMA8Hl%2FJz1RXbQTH%2B865ibUtIfjXZ6wUEwIr3Id3hTd11DcTooHbIEs7hcaOZtCv7MoJK88ME9K1%2FSK8otN7FKOTZdznO8SjU57PHdwzqbtO%2F1LD2tUx7RAfRHoYQ%2B2AV%2F%2BBxCYIh4%2BOYMhMRecDwXfD%2FrGkBL%2B2Uzxpwvc0onq7evq5eqh2qzZ8w3Rq21Rr7Cb82hvzV0c%2FmRtCtpJ9ZBvGBwBainc9V9i4kUoFw8wuZq5d2wv8qrMzGG0I3U6SwK7MGsTjg8jL0xVeyzf3ct5EroPYnKfObSX5YKsTPRZdB102cPQnAKd6oMvnqvKcAd42YMpbA1flgFTJ%2F3%2F1d3qc0djDb5%2Bi8BjqkASQhBa196IHo8Uxfg3uerjS%2F0x9lgbBliPDXE6p5nDSFfWjyQ%2BDinLuV6GpLZBPZQeRLUc%2F2PTWFNhTL3f%2Fc0GtsTzscxt66NCyCxzTvgvqtAN4owysGMLE%2FWMOH2%2FO2ViYQlvm%2Bgk1LS8%2Fx9%2BDuWV%2FX2w4y7atC5b8ie%2BfsEbIgNvyrzKauf5bT1mduSCcxHWPjwt6hsWFH4t%2FS%2Fgkvn%2BXMDMzR&X-Amz-Signature=7889f60cf41ee94fdc79161698894157ea7cac0b520e6a7b6ebd2e1795d8e6d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QTXO67M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI%2BUoyt4QBn8Ub80qX43QuN5EmC5fRgqxU67TVjIaMLgIhAKXvRPZO47e4JZzSYaj4xGypLc2z9WhE0wnIXD4dttibKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOoUlq5lMGGqzlkSIq3APyLZH0EphJubQdtj8ckq5Psi4vx3XqNP9rqnWyQgJL24dbC6i%2FLjjohNrhuZSZIcVADHRJwhGmLN1noVox%2BGFXUKCuHsMjS%2FjuCn%2FTA6%2BZcOeG5ViBj%2FlchwSttYBW%2FTgDFGL8HntED49preU%2BCdAxqvP%2BJESg4Z%2F49EnMONePDFGH5LAzjJ%2BKwuu%2BDdArCPKo9Id6uCSUSWwJ0%2Fwt3smu97PpEGkQNW4fYJ%2Fxed8Y%2FWPhFN1yMk7Rb0ohSxw9QKT%2BPn97XNNbZ2RZVB0j66JJnFGGaOZdAxrxMA8Hl%2FJz1RXbQTH%2B865ibUtIfjXZ6wUEwIr3Id3hTd11DcTooHbIEs7hcaOZtCv7MoJK88ME9K1%2FSK8otN7FKOTZdznO8SjU57PHdwzqbtO%2F1LD2tUx7RAfRHoYQ%2B2AV%2F%2BBxCYIh4%2BOYMhMRecDwXfD%2FrGkBL%2B2Uzxpwvc0onq7evq5eqh2qzZ8w3Rq21Rr7Cb82hvzV0c%2FmRtCtpJ9ZBvGBwBainc9V9i4kUoFw8wuZq5d2wv8qrMzGG0I3U6SwK7MGsTjg8jL0xVeyzf3ct5EroPYnKfObSX5YKsTPRZdB102cPQnAKd6oMvnqvKcAd42YMpbA1flgFTJ%2F3%2F1d3qc0djDb5%2Bi8BjqkASQhBa196IHo8Uxfg3uerjS%2F0x9lgbBliPDXE6p5nDSFfWjyQ%2BDinLuV6GpLZBPZQeRLUc%2F2PTWFNhTL3f%2Fc0GtsTzscxt66NCyCxzTvgvqtAN4owysGMLE%2FWMOH2%2FO2ViYQlvm%2Bgk1LS8%2Fx9%2BDuWV%2FX2w4y7atC5b8ie%2BfsEbIgNvyrzKauf5bT1mduSCcxHWPjwt6hsWFH4t%2FS%2Fgkvn%2BXMDMzR&X-Amz-Signature=35cc91745da28a5f677a908600c12b299f2c90edf2617520a090d1e11706f291&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QTXO67M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI%2BUoyt4QBn8Ub80qX43QuN5EmC5fRgqxU67TVjIaMLgIhAKXvRPZO47e4JZzSYaj4xGypLc2z9WhE0wnIXD4dttibKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOoUlq5lMGGqzlkSIq3APyLZH0EphJubQdtj8ckq5Psi4vx3XqNP9rqnWyQgJL24dbC6i%2FLjjohNrhuZSZIcVADHRJwhGmLN1noVox%2BGFXUKCuHsMjS%2FjuCn%2FTA6%2BZcOeG5ViBj%2FlchwSttYBW%2FTgDFGL8HntED49preU%2BCdAxqvP%2BJESg4Z%2F49EnMONePDFGH5LAzjJ%2BKwuu%2BDdArCPKo9Id6uCSUSWwJ0%2Fwt3smu97PpEGkQNW4fYJ%2Fxed8Y%2FWPhFN1yMk7Rb0ohSxw9QKT%2BPn97XNNbZ2RZVB0j66JJnFGGaOZdAxrxMA8Hl%2FJz1RXbQTH%2B865ibUtIfjXZ6wUEwIr3Id3hTd11DcTooHbIEs7hcaOZtCv7MoJK88ME9K1%2FSK8otN7FKOTZdznO8SjU57PHdwzqbtO%2F1LD2tUx7RAfRHoYQ%2B2AV%2F%2BBxCYIh4%2BOYMhMRecDwXfD%2FrGkBL%2B2Uzxpwvc0onq7evq5eqh2qzZ8w3Rq21Rr7Cb82hvzV0c%2FmRtCtpJ9ZBvGBwBainc9V9i4kUoFw8wuZq5d2wv8qrMzGG0I3U6SwK7MGsTjg8jL0xVeyzf3ct5EroPYnKfObSX5YKsTPRZdB102cPQnAKd6oMvnqvKcAd42YMpbA1flgFTJ%2F3%2F1d3qc0djDb5%2Bi8BjqkASQhBa196IHo8Uxfg3uerjS%2F0x9lgbBliPDXE6p5nDSFfWjyQ%2BDinLuV6GpLZBPZQeRLUc%2F2PTWFNhTL3f%2Fc0GtsTzscxt66NCyCxzTvgvqtAN4owysGMLE%2FWMOH2%2FO2ViYQlvm%2Bgk1LS8%2Fx9%2BDuWV%2FX2w4y7atC5b8ie%2BfsEbIgNvyrzKauf5bT1mduSCcxHWPjwt6hsWFH4t%2FS%2Fgkvn%2BXMDMzR&X-Amz-Signature=36dffd663104aa621c13e0bb69cdc8bfd796d45e55553a4b1d83bc8f7465919c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX4IGKT7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJHBsi83bLhNfZQ9XOgNforl3tZhDW35z0AokRa%2FrQGwIganfN%2ByN2vZM37TN2Hr1njd30rmnmbHjkEOYLqyQokZ8qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNq4SJlWdVryWvZQLCrcA3YPjhFEvk3buL3TpXO%2B2bbacuW095K7CVebWkZVYVkb9vo%2Bdrjv4%2BI7D4Trm%2FS%2BLCDaMhGqmOWjeeqajsxgkwI9cgIcTRevuClEQDH3zHbSzPnMMLtWzfgXZOl8DiohlyrInqZiUjCLPQH4rZ2EKdaM9Kq3o4AYw3jD4tXatbrWnEwNo%2FiQ2OInOvWXTFTMiHzRBACDvEeBS%2FBvfu7QdZtMEXjL2YxPIvnL2vRYqVoGz%2FCq%2FJHTiW%2FMO4zxSIpuYw3UNtDnohZHRIzOFYv58CQ4dzOcEy9UmTewzeSliPNOcWhaNzTPgpUm0sEXR6QMbKC5AZcit5bp8rRxyIMQEa778oIcwwqH9caDoF3WVY%2BeZCKmzv2o066Elgogi9kgGbEaqjF7CNRwd%2Fn4BJ3i5cqHaox5%2BIMhieLaIbLjf5w%2BXL6RNc6rW%2FoddgSQ1EpDON9ifZQr3KOvy1dClvs3WqlzqtrPFlT0Irf%2FdHkGfaaTl5uIsJW0vLBshNv9XML2x1CD6PwHE%2Ff043hbVcIJWr4DcBZyVWyRWL%2F%2FISmWisDtnNIbJ4IOA6zbaqm4pyZoxc%2BSRkUaOLdoU6RC2sz5hG3vpqN74AbnFQRty%2FYptRWDWYCodxB6wf3uF5BxMKLn6LwGOqUBcozFPPnNZh%2FRIeqUqmYVj7rHur3q9q0IU4Y%2BsjkgH4W%2BCVu%2ByYEy%2FxgH%2BybsDs5KSLifIqlvOlziP7z%2F5DEq2BNeDJDlBFacQZKG5kdWPloF8dDpm4PS%2Bm2gu9QEbBIaiU8aEaOjrVkObQxeL%2BNZ5HEYniQJ%2B68loII1snS50%2FJnqaTMPFzZ0msHG9A9RO%2FQc5hm5mBREtfhmJZNHx7parFI8hkn&X-Amz-Signature=e14b97e65990f164fc61039e361b95be76dbcdcb67115a9144b02d545327319a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX4IGKT7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJHBsi83bLhNfZQ9XOgNforl3tZhDW35z0AokRa%2FrQGwIganfN%2ByN2vZM37TN2Hr1njd30rmnmbHjkEOYLqyQokZ8qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNq4SJlWdVryWvZQLCrcA3YPjhFEvk3buL3TpXO%2B2bbacuW095K7CVebWkZVYVkb9vo%2Bdrjv4%2BI7D4Trm%2FS%2BLCDaMhGqmOWjeeqajsxgkwI9cgIcTRevuClEQDH3zHbSzPnMMLtWzfgXZOl8DiohlyrInqZiUjCLPQH4rZ2EKdaM9Kq3o4AYw3jD4tXatbrWnEwNo%2FiQ2OInOvWXTFTMiHzRBACDvEeBS%2FBvfu7QdZtMEXjL2YxPIvnL2vRYqVoGz%2FCq%2FJHTiW%2FMO4zxSIpuYw3UNtDnohZHRIzOFYv58CQ4dzOcEy9UmTewzeSliPNOcWhaNzTPgpUm0sEXR6QMbKC5AZcit5bp8rRxyIMQEa778oIcwwqH9caDoF3WVY%2BeZCKmzv2o066Elgogi9kgGbEaqjF7CNRwd%2Fn4BJ3i5cqHaox5%2BIMhieLaIbLjf5w%2BXL6RNc6rW%2FoddgSQ1EpDON9ifZQr3KOvy1dClvs3WqlzqtrPFlT0Irf%2FdHkGfaaTl5uIsJW0vLBshNv9XML2x1CD6PwHE%2Ff043hbVcIJWr4DcBZyVWyRWL%2F%2FISmWisDtnNIbJ4IOA6zbaqm4pyZoxc%2BSRkUaOLdoU6RC2sz5hG3vpqN74AbnFQRty%2FYptRWDWYCodxB6wf3uF5BxMKLn6LwGOqUBcozFPPnNZh%2FRIeqUqmYVj7rHur3q9q0IU4Y%2BsjkgH4W%2BCVu%2ByYEy%2FxgH%2BybsDs5KSLifIqlvOlziP7z%2F5DEq2BNeDJDlBFacQZKG5kdWPloF8dDpm4PS%2Bm2gu9QEbBIaiU8aEaOjrVkObQxeL%2BNZ5HEYniQJ%2B68loII1snS50%2FJnqaTMPFzZ0msHG9A9RO%2FQc5hm5mBREtfhmJZNHx7parFI8hkn&X-Amz-Signature=119f604dcc9ff98569bd0983a061b187bed453a5047eba532133ecefb19dd7d7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
