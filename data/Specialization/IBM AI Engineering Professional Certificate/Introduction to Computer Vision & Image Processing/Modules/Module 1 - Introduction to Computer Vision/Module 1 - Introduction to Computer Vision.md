

# Module 1: Introduction to Computer Vision
## Introduction to Computer Vision
### Course Overview
In this course, you will be introduced to the field of computer vision, including its applications, specialized methods, and techniques. You will learn to implement these techniques using Python.
#### Learning Objectives
- Understand what computer vision is.
- Apply and use computer vision algorithms with Python and OpenCV.
- Create custom classifiers for business problems.
- Build a web app to classify images.
#### Exclusions
- How computer vision works in detail.
- How neural networks or deep learning work.
- In-depth math and statistics.
### What is Computer Vision?
Computer vision involves providing computers with the ability to see and understand images. For example, while humans can instantly recognize and interpret images, computers cannot do so without assistance.
### Industry Impact
Computer vision is making significant waves in various industries due to its ability to improve efficiency and effectiveness. Key areas where computer vision is adopted include:
- **Automation**: Reducing manual tasks and making processes faster and more convenient.
- **Cost Efficiency**: Lowering expenses and making technologies more accessible.
- **Scalability**: Enabling scalable solutions for various applications.
#### Groundbreaking Change
Self-driving cars are a notable example of computer vision's impact, automating driving and potentially saving lives.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d2ff3738-322b-4bed-b884-e286566efb94/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241031T051605Z&X-Amz-Expires=3600&X-Amz-Signature=26240fa2ddadaef9f3a5e2070799ff93a53f368f3f5424d2baeffe4658789e56&X-Amz-SignedHeaders=host&x-id=GetObject)
### Applications Across Industries
Computer vision has transformative applications in multiple sectors, including:
- **Automotive**
- **Manufacturing**
- **Human Resources**
- **Insurance**
- **Healthcare**
#### Case Study: ADNOC
ADNOC (Abu Dhabi National Oil Company) produces around 3 million barrels of oil and 10.5 billion cubic feet of raw gas daily. Traditionally, classifying rock samples was labor-intensive. By using IBM Watson for analyzing high-resolution rock images, ADNOC can classify up to 25,000 thin-section rock images per day, significantly saving time and resources.
![merlin_190903830_f0aa9789-8002-4443-889b-cf52a2291890-articleLarge.webp](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00c2a896-0042-4cbe-a1e6-6bcda9bea64c/merlin_190903830_f0aa9789-8002-4443-889b-cf52a2291890-articleLarge.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241031T051605Z&X-Amz-Expires=3600&X-Amz-Signature=029a2f8bbf00378a84d1ab1901cf29bb434215d3ba16ae89c0b02d75fdcea58a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Case Study: Knockri
In the HR sector, Knockri, a Canadian startup, is revolutionizing hiring with an AI video soft skill assessment tool. By leveraging computer vision, machine learning, and data science, Knockri quantifies soft skills and assists in early candidate assessments, streamlining the hiring process for large companies.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f485c63-f28c-48ae-b5ae-758411aae60b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241031T051605Z&X-Amz-Expires=3600&X-Amz-Signature=456a220279f7a309efcfa9e0636e5c5b7b8f9a3c876a9b4a18b1d5f1ebee4fb2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
Computer vision is rapidly transforming industries by enhancing automation, cost-efficiency, and scalability. Its applications are broad, impacting everything from oil classification to hiring processes.
___
## Applications of Computer Vision
### Overview
In this section, we explore various applications of computer vision and discuss how you can develop your own applications.
### Searching Through Videos
One common challenge is searching through videos to find specific scenes. Traditionally, this requires fast-forwarding and manual searching. IBM has addressed this by tagging videos with keywords based on the objects present in each scene.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6611b4b5-7716-4238-9394-371b7f97dd8d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241031T051605Z&X-Amz-Expires=3600&X-Amz-Signature=59ca2da7557b9cca967960d89d9131ca5797d906eb575d9a9adeefe22ee563a7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Security and Object Recognition
Imagine a security company needing to find a suspect in a blue van among hours of footage. With computer vision and object recognition, this task becomes manageable and efficient, eliminating the need for extensive manual searching.
### Maintenance of Electric Towers
Electric towers require regular maintenance to check for rust and structural defects. Manually inspecting each tower is time-consuming and costly. Instead, high-resolution images can be taken from different angles, which are then analyzed using computer vision.
#### Custom Image Classifiers
By dividing high-resolution images into smaller segments, you can develop custom image classifiers. These classifiers can detect the presence of metal versus non-metal objects and assess the level of rust.
- **Metal Classifier**: Identifies metal structures in images.
- **Rust Classifier**: Determines the rust level based on predefined criteria, such as:
	- **Grade 1 Rust**: Minimal rust
	- **Grade 6 Rust**: Severe rust
This approach can save significant costs for industries like insurance by automating the analysis of thousands or millions of images.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/16d9e2cd-921b-4673-9544-fd20224f176c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241031T051605Z&X-Amz-Expires=3600&X-Amz-Signature=131a54cc6d42559384c9cce78aeff26086e356b3b958cb8719bf70833c2cc78c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Insurance Claims Processing
Computer vision can also streamline the processing of insurance claims by automatically classifying damage, such as hail or ice pellet damage from storms. This improves efficiency and accuracy, reducing the time and cost associated with claim processing.
### Summary
This section highlights the diverse applications of computer vision, demonstrating how it can enhance efficiency and reduce costs across various industries, from security and maintenance to insurance.
___
## Active Research in Computer Vision
### Overview
This section covers recent advancements and ongoing research in the field of computer vision over the past decade.
### Object Detection
Researchers at Facebook are focusing on detecting objects in images. Accurate and efficient object detection is crucial for making meaningful inferences from images and video streams. This capability is particularly important for applications such as self-driving cars, where real-time object detection from camera feeds is necessary to avoid obstacles and prevent collisions.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4abd25e4-e758-4223-b0a0-c40adde5fd3d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241031T051605Z&X-Amz-Expires=3600&X-Amz-Signature=ec2a96379cb533a62fd0b92c94859353b041d0b825b5f2bc72cd72219ff6651e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Image to Image Translation
Image to image translation involves converting an image from one representation to another. For example, transforming an image of a horse into a zebra or changing the scene of an image from summer to winter. Researchers at UC Berkeley are working on techniques for this kind of transformation, allowing for significant modifications in image content.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4c69140-8edb-4b9c-9a3e-3ea01fdcda90/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241031T051605Z&X-Amz-Expires=3600&X-Amz-Signature=c1bf592094e639ae63828879032b36bd82a2235f83e7f9af620ea66f691b2470&X-Amz-SignedHeaders=host&x-id=GetObject)
### Motion Transfer
The "Everybody Dance Now" project demonstrates computer vision techniques for motion transfer. This project allows the dance moves of a person in a video to be transferred to another person, enabling the target to perform the same dance moves as the original subject.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e5b2060e-a889-4469-90bd-3920e03b6e3d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45GO43JXI4%2F20241031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241031T051605Z&X-Amz-Expires=3600&X-Amz-Signature=780493595bbbac37f04a234c8ba35f4a78af079bb31baa1061fb423b01aa9a01&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
Recent research in computer vision includes advancements in object detection, image to image translation, and motion transfer. These innovations are enhancing the capabilities of computer vision systems and expanding their applications in various domains.
___
## Generating Ideas for Computer Vision Applications
### Introduction
This section encourages the exploration of potential computer vision applications by starting with existing problems and considering how computer vision can provide solutions.
### Identifying Existing Problems
Instead of beginning with a specific computer vision solution, it can be more effective to start by identifying problems that could be addressed. Here are some examples across various industries:
#### Medicine
One of the most challenging and time-consuming tasks in medicine is training doctors to accurately detect cancer. Developing computer vision tools that can assist in diagnosing cancer from medical images could help alleviate this problem.
#### Driving
Driving requires constant visual attention, and mistakes can have severe consequences. Additionally, long-distance drivers are at risk of falling asleep at the wheel. Computer vision could be used to develop systems that monitor driver alertness and provide warnings if necessary.
#### Security and Surveillance
In the security and surveillance industry, searching for a suspect across hours of footage is time-consuming. Computer vision can automate this process by efficiently identifying and tracking suspects. Additionally, detecting dangerous goods in X-rays at airports is challenging, and computer vision could improve the accuracy of these detections.
#### Manufacturing
In manufacturing, ensuring the quality of thousands of products is labor-intensive. Computer vision could be employed to automate quality control processes and detect defects in real-time.
#### Insurance and Work Safety
For insurance, evaluating damage from car accidents is a complex task that involves assessing the make, model, and year of the vehicle. Computer vision could streamline this process. Additionally, ensuring that construction workers wear appropriate safety gear is crucial for work safety, and computer vision can help in monitoring compliance.
### Personal and Everyday Problems
Consider problems you face in daily life or at work, and think about how computer vision could provide solutions:
- **Finding Receipts**: Computer vision could help in organizing and searching receipts for returns or exchanges.
- **Plant Identification**: Identify and track the growth of plants in your backyard using computer vision.
- **Rodent Problems**: Monitor and address rodent issues, such as raccoons rummaging through garbage bins.
### Summary
Exploring potential applications of computer vision involves identifying real-world problems and considering how technology can offer solutions. Think about challenges in your life, work, or industry to generate innovative ideas for computer vision applications.
___
