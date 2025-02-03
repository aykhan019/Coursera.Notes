

# Module 1: Introduction to Neural Networks and Deep Learning
## Deep Learning: Recent Advances and Applications
Deep learning has emerged as one of the most exciting fields in data science, with recent advancements leading to groundbreaking applications that were once considered nearly impossible. This note explores some of these remarkable applications and provides insights into why deep learning is currently experiencing such rapid growth.
### Color Restoration
Color restoration is a fascinating application where grayscale images are automatically transformed into color. Researchers in Japan developed a system using Convolutional Neural Networks (CNNs) to achieve this. The system takes grayscale images and adds color to them, bringing them to life. This technology demonstrates the impressive capabilities of deep learning in image processing.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/de1ebdcc-ed41-4a91-9f79-4632dc723c89/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QOCQ3XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQD%2B%2BAiBTXgVQeD1JcKrQ7cnY0F6muqYxBey3g91daIn3gIgAtM%2FIzIB1tiqcM0IigIMMw%2F7QTynBhtnNmBxKJMQn1Eq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDNAYqAHyDYvGIiC3qyrcA9SyODnKU6rvrNvFuD1lBW9aJsyfcwoPyxap6dLh7xiEZu5jdvyWSKMTw2q2V6r4kEplYvhHpFM4%2Bw4A%2FsTIisEQe211xcaNhsZQ41qLh5lDwxkBj5NB9umLRVzCot1Pye7y4tdKKLGiVzOdF7KbSnVOC6dHApQI9Ytkmow0GIXO%2FR4wZKKfPf%2Ff6%2BDx65bXSrXax4JJlCdCKLTOn7G%2FTc1Cufhrq1Ywnx4ArQUBzZtbDMG2yHhvJXWkKH0C053Ymm%2Bx1eYYWG7yvEUV%2F%2BIHaN8jufpu7gVpNG%2B1uHf0pCbzP41D224v%2BIQS2qASDQalnSlk2bGtQ0UMZ4YPg26bSDpB9v5J%2FiQdJ1d3R0QsKGhMFfKFcBDySUZ8%2FT8fvRp3SJRTZAZO%2BkQx2mkHolxc2U0z03qNluG%2BSGzMaQsMngmJiXdoDCeNH28YHCOi0JEfGTh%2BYHRTqAuE%2Fy0%2FLJJLD8w0HPracBSKFwktKm3LI8BBTjPaa65L5DEiId94OV6k%2FPC81CWTYkh4J%2BAaA06hg9iJ10kaInXR1R14bwBhAqSNOPMex53ApC4B93sULxzV20Cf3AbzX0aZYXBbF830GJZ4P6nBsVEBgboX5RTt%2BmDSNMMmRifWpqXeTy0hMIy9hL0GOqUBKTOyoH5rYfuv7J6Eycdg9HiHYO1ztggWM4TfvPr%2F5hd%2BUTLRSrplPlqodZCx4YIqq%2FehxRMrIPsvflETsTdXRTjP6F4LL5HLMadfApUOF82JHmYs3P9%2FhIrHRkjNcptUlPkAZdZp4gFINF9PEHuCLCJEfVfCJfbZbI5C6jZ3WqX1btyOnW0Cq%2FJpLDPimgCD6rqu7lcSjA70kE2AqWkWJarCgPnf&X-Amz-Signature=b8eeae6bb87ad87cbda877b7f0b46cc824ca52437f12a35308b72c6a3018ae1e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Speech Enactment
Speech enactment involves synthesizing audio clips with video and synchronizing lip movements with the spoken words. A notable advancement in this area was achieved by researchers at the University of Washington, who trained a Recurrent Neural Network (RNN) on a large dataset of video clips featuring a single person. Their system, demonstrated with a video of former President Barack Obama, produces realistic results where lip movements match the audio accurately.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93a191f0-d690-489c-86db-10d8d79d6eb6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QOCQ3XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQD%2B%2BAiBTXgVQeD1JcKrQ7cnY0F6muqYxBey3g91daIn3gIgAtM%2FIzIB1tiqcM0IigIMMw%2F7QTynBhtnNmBxKJMQn1Eq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDNAYqAHyDYvGIiC3qyrcA9SyODnKU6rvrNvFuD1lBW9aJsyfcwoPyxap6dLh7xiEZu5jdvyWSKMTw2q2V6r4kEplYvhHpFM4%2Bw4A%2FsTIisEQe211xcaNhsZQ41qLh5lDwxkBj5NB9umLRVzCot1Pye7y4tdKKLGiVzOdF7KbSnVOC6dHApQI9Ytkmow0GIXO%2FR4wZKKfPf%2Ff6%2BDx65bXSrXax4JJlCdCKLTOn7G%2FTc1Cufhrq1Ywnx4ArQUBzZtbDMG2yHhvJXWkKH0C053Ymm%2Bx1eYYWG7yvEUV%2F%2BIHaN8jufpu7gVpNG%2B1uHf0pCbzP41D224v%2BIQS2qASDQalnSlk2bGtQ0UMZ4YPg26bSDpB9v5J%2FiQdJ1d3R0QsKGhMFfKFcBDySUZ8%2FT8fvRp3SJRTZAZO%2BkQx2mkHolxc2U0z03qNluG%2BSGzMaQsMngmJiXdoDCeNH28YHCOi0JEfGTh%2BYHRTqAuE%2Fy0%2FLJJLD8w0HPracBSKFwktKm3LI8BBTjPaa65L5DEiId94OV6k%2FPC81CWTYkh4J%2BAaA06hg9iJ10kaInXR1R14bwBhAqSNOPMex53ApC4B93sULxzV20Cf3AbzX0aZYXBbF830GJZ4P6nBsVEBgboX5RTt%2BmDSNMMmRifWpqXeTy0hMIy9hL0GOqUBKTOyoH5rYfuv7J6Eycdg9HiHYO1ztggWM4TfvPr%2F5hd%2BUTLRSrplPlqodZCx4YIqq%2FehxRMrIPsvflETsTdXRTjP6F4LL5HLMadfApUOF82JHmYs3P9%2FhIrHRkjNcptUlPkAZdZp4gFINF9PEHuCLCJEfVfCJfbZbI5C6jZ3WqX1btyOnW0Cq%2FJpLDPimgCD6rqu7lcSjA70kE2AqWkWJarCgPnf&X-Amz-Signature=87762b7316cb62d797670c67dda2cfe19c5bd5ff9d6f3ea5ac2ba88144736b99&X-Amz-SignedHeaders=host&x-id=GetObject)
The system can also extract audio from one video and sync it with lip movements in another, showcasing the versatility of this technology.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0acad1f2-660b-42b0-a6a5-271476be67f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QOCQ3XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQD%2B%2BAiBTXgVQeD1JcKrQ7cnY0F6muqYxBey3g91daIn3gIgAtM%2FIzIB1tiqcM0IigIMMw%2F7QTynBhtnNmBxKJMQn1Eq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDNAYqAHyDYvGIiC3qyrcA9SyODnKU6rvrNvFuD1lBW9aJsyfcwoPyxap6dLh7xiEZu5jdvyWSKMTw2q2V6r4kEplYvhHpFM4%2Bw4A%2FsTIisEQe211xcaNhsZQ41qLh5lDwxkBj5NB9umLRVzCot1Pye7y4tdKKLGiVzOdF7KbSnVOC6dHApQI9Ytkmow0GIXO%2FR4wZKKfPf%2Ff6%2BDx65bXSrXax4JJlCdCKLTOn7G%2FTc1Cufhrq1Ywnx4ArQUBzZtbDMG2yHhvJXWkKH0C053Ymm%2Bx1eYYWG7yvEUV%2F%2BIHaN8jufpu7gVpNG%2B1uHf0pCbzP41D224v%2BIQS2qASDQalnSlk2bGtQ0UMZ4YPg26bSDpB9v5J%2FiQdJ1d3R0QsKGhMFfKFcBDySUZ8%2FT8fvRp3SJRTZAZO%2BkQx2mkHolxc2U0z03qNluG%2BSGzMaQsMngmJiXdoDCeNH28YHCOi0JEfGTh%2BYHRTqAuE%2Fy0%2FLJJLD8w0HPracBSKFwktKm3LI8BBTjPaa65L5DEiId94OV6k%2FPC81CWTYkh4J%2BAaA06hg9iJ10kaInXR1R14bwBhAqSNOPMex53ApC4B93sULxzV20Cf3AbzX0aZYXBbF830GJZ4P6nBsVEBgboX5RTt%2BmDSNMMmRifWpqXeTy0hMIy9hL0GOqUBKTOyoH5rYfuv7J6Eycdg9HiHYO1ztggWM4TfvPr%2F5hd%2BUTLRSrplPlqodZCx4YIqq%2FehxRMrIPsvflETsTdXRTjP6F4LL5HLMadfApUOF82JHmYs3P9%2FhIrHRkjNcptUlPkAZdZp4gFINF9PEHuCLCJEfVfCJfbZbI5C6jZ3WqX1btyOnW0Cq%2FJpLDPimgCD6rqu7lcSjA70kE2AqWkWJarCgPnf&X-Amz-Signature=1646d2d1260b24a48817f44b5b6be7c2c9ba8b9416f1224d4bfbb2041a6d7fb7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Automatic Handwriting Generation
Alex Graves from the University of Toronto designed an algorithm using RNNs for automatic handwriting generation. This algorithm can rewrite text in highly realistic cursive handwriting across various styles. Users can input text and either select a specific handwriting style or let the algorithm choose one randomly.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f465b5fe-6e89-4df1-9bda-c23bd9e0e9fe/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QOCQ3XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQD%2B%2BAiBTXgVQeD1JcKrQ7cnY0F6muqYxBey3g91daIn3gIgAtM%2FIzIB1tiqcM0IigIMMw%2F7QTynBhtnNmBxKJMQn1Eq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDNAYqAHyDYvGIiC3qyrcA9SyODnKU6rvrNvFuD1lBW9aJsyfcwoPyxap6dLh7xiEZu5jdvyWSKMTw2q2V6r4kEplYvhHpFM4%2Bw4A%2FsTIisEQe211xcaNhsZQ41qLh5lDwxkBj5NB9umLRVzCot1Pye7y4tdKKLGiVzOdF7KbSnVOC6dHApQI9Ytkmow0GIXO%2FR4wZKKfPf%2Ff6%2BDx65bXSrXax4JJlCdCKLTOn7G%2FTc1Cufhrq1Ywnx4ArQUBzZtbDMG2yHhvJXWkKH0C053Ymm%2Bx1eYYWG7yvEUV%2F%2BIHaN8jufpu7gVpNG%2B1uHf0pCbzP41D224v%2BIQS2qASDQalnSlk2bGtQ0UMZ4YPg26bSDpB9v5J%2FiQdJ1d3R0QsKGhMFfKFcBDySUZ8%2FT8fvRp3SJRTZAZO%2BkQx2mkHolxc2U0z03qNluG%2BSGzMaQsMngmJiXdoDCeNH28YHCOi0JEfGTh%2BYHRTqAuE%2Fy0%2FLJJLD8w0HPracBSKFwktKm3LI8BBTjPaa65L5DEiId94OV6k%2FPC81CWTYkh4J%2BAaA06hg9iJ10kaInXR1R14bwBhAqSNOPMex53ApC4B93sULxzV20Cf3AbzX0aZYXBbF830GJZ4P6nBsVEBgboX5RTt%2BmDSNMMmRifWpqXeTy0hMIy9hL0GOqUBKTOyoH5rYfuv7J6Eycdg9HiHYO1ztggWM4TfvPr%2F5hd%2BUTLRSrplPlqodZCx4YIqq%2FehxRMrIPsvflETsTdXRTjP6F4LL5HLMadfApUOF82JHmYs3P9%2FhIrHRkjNcptUlPkAZdZp4gFINF9PEHuCLCJEfVfCJfbZbI5C6jZ3WqX1btyOnW0Cq%2FJpLDPimgCD6rqu7lcSjA70kE2AqWkWJarCgPnf&X-Amz-Signature=3809658744978f39c3ec9548890467a0aa9f7400934ed317d6146af54dd120b2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Other Applications
Deep learning encompasses a wide range of applications, including:
- **Automatic Machine Translation**: Using CNNs to translate text in images in real-time.
- **Sound Addition to Silent Movies**: Employing deep learning models to select appropriate sounds from a pre-recorded database to match scenes in silent films.
- **Object Classification and Self-Driving Cars**: Classifying objects in images and enabling autonomous driving.
### The Rise of Neural Networks
Despite the long history of neural networks, their recent surge in popularity can be attributed to advancements in technology and the availability of large datasets. These improvements have unlocked new possibilities and applications, making neural networks and deep learning more relevant than ever.
### Summary
Deep learning has revolutionized numerous fields with its applications, from color restoration and speech enactment to handwriting generation and beyond. The continuous advancements in neural networks are driving these innovations and opening up new avenues for research and development.
*Additional Notes*: To fully grasp the potential of deep learning, further exploration into neural network specifics and deep learning techniques is essential.
___
## Neural Networks: Biological Inspiration and Artificial Implementation
Deep learning algorithms draw inspiration from the way neurons and neural networks function in the human brain. Understanding this biological basis helps illuminate how artificial neural networks process information and learn.
### Biological Neurons: Structure and Function
Neurons are the fundamental units of the brain, responsible for processing and transmitting information through electrical impulses. The study of neurons began with the pioneering work of Santiago Ramón y Cajal, who is considered the father of modern neuroscience.
#### Structure of a Biological Neuron
- **Dendrites**: Branch-like structures extending from the soma, responsible for receiving electrical impulses from other neurons.
- **Soma**: The main body of the neuron, which contains the **nucleus.**
- **Axon**: A long, slender projection that transmits electrical impulses away from the soma.
- **Synapses (Terminal Buttons)**: The endings of the axon, which pass the impulses (short electrical signals that carries information) to the dendrites of adjacent neurons.
#### Functioning of a Biological Neuron
Neurons receive electrical impulses through dendrites, process these impulses in the soma, and transmit the processed information through the axon to other neurons via synapses. Learning in the brain occurs by reinforcing certain neural connections through repeated activation, which strengthens these connections and makes them more likely to produce a desired outcome.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0dd23e6a-8e6b-4b90-ab92-b198a36f7f9e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QOCQ3XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQD%2B%2BAiBTXgVQeD1JcKrQ7cnY0F6muqYxBey3g91daIn3gIgAtM%2FIzIB1tiqcM0IigIMMw%2F7QTynBhtnNmBxKJMQn1Eq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDNAYqAHyDYvGIiC3qyrcA9SyODnKU6rvrNvFuD1lBW9aJsyfcwoPyxap6dLh7xiEZu5jdvyWSKMTw2q2V6r4kEplYvhHpFM4%2Bw4A%2FsTIisEQe211xcaNhsZQ41qLh5lDwxkBj5NB9umLRVzCot1Pye7y4tdKKLGiVzOdF7KbSnVOC6dHApQI9Ytkmow0GIXO%2FR4wZKKfPf%2Ff6%2BDx65bXSrXax4JJlCdCKLTOn7G%2FTc1Cufhrq1Ywnx4ArQUBzZtbDMG2yHhvJXWkKH0C053Ymm%2Bx1eYYWG7yvEUV%2F%2BIHaN8jufpu7gVpNG%2B1uHf0pCbzP41D224v%2BIQS2qASDQalnSlk2bGtQ0UMZ4YPg26bSDpB9v5J%2FiQdJ1d3R0QsKGhMFfKFcBDySUZ8%2FT8fvRp3SJRTZAZO%2BkQx2mkHolxc2U0z03qNluG%2BSGzMaQsMngmJiXdoDCeNH28YHCOi0JEfGTh%2BYHRTqAuE%2Fy0%2FLJJLD8w0HPracBSKFwktKm3LI8BBTjPaa65L5DEiId94OV6k%2FPC81CWTYkh4J%2BAaA06hg9iJ10kaInXR1R14bwBhAqSNOPMex53ApC4B93sULxzV20Cf3AbzX0aZYXBbF830GJZ4P6nBsVEBgboX5RTt%2BmDSNMMmRifWpqXeTy0hMIy9hL0GOqUBKTOyoH5rYfuv7J6Eycdg9HiHYO1ztggWM4TfvPr%2F5hd%2BUTLRSrplPlqodZCx4YIqq%2FehxRMrIPsvflETsTdXRTjP6F4LL5HLMadfApUOF82JHmYs3P9%2FhIrHRkjNcptUlPkAZdZp4gFINF9PEHuCLCJEfVfCJfbZbI5C6jZ3WqX1btyOnW0Cq%2FJpLDPimgCD6rqu7lcSjA70kE2AqWkWJarCgPnf&X-Amz-Signature=0267855e059b480d391db571972c5d339cc5307ab0cf44eec210cdd41a3f6b8d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Artificial Neurons: Mimicking the Brain
Artificial neurons are modeled after biological neurons, incorporating similar components and processes:
- **Artificial Dendrites**: Receive input data from other neurons.
- **Artificial Soma**: Functions as the processing unit where inputs (analogous to electrical impulses) are combined.
- **Artificial Axon**: Transmits the processed data to other neurons.
- **Artificial Synapse**: The connection point where the output of one neuron becomes the input to another.
#### Learning in Artificial Neural Networks
The learning process in artificial neural networks closely resembles that of the brain. Through repeated activation and adjustment, the connections between artificial neurons are strengthened, enabling the network to produce more accurate outputs given specific inputs.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/21c84c18-4b2b-4801-9395-3704469dc902/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QOCQ3XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQD%2B%2BAiBTXgVQeD1JcKrQ7cnY0F6muqYxBey3g91daIn3gIgAtM%2FIzIB1tiqcM0IigIMMw%2F7QTynBhtnNmBxKJMQn1Eq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDNAYqAHyDYvGIiC3qyrcA9SyODnKU6rvrNvFuD1lBW9aJsyfcwoPyxap6dLh7xiEZu5jdvyWSKMTw2q2V6r4kEplYvhHpFM4%2Bw4A%2FsTIisEQe211xcaNhsZQ41qLh5lDwxkBj5NB9umLRVzCot1Pye7y4tdKKLGiVzOdF7KbSnVOC6dHApQI9Ytkmow0GIXO%2FR4wZKKfPf%2Ff6%2BDx65bXSrXax4JJlCdCKLTOn7G%2FTc1Cufhrq1Ywnx4ArQUBzZtbDMG2yHhvJXWkKH0C053Ymm%2Bx1eYYWG7yvEUV%2F%2BIHaN8jufpu7gVpNG%2B1uHf0pCbzP41D224v%2BIQS2qASDQalnSlk2bGtQ0UMZ4YPg26bSDpB9v5J%2FiQdJ1d3R0QsKGhMFfKFcBDySUZ8%2FT8fvRp3SJRTZAZO%2BkQx2mkHolxc2U0z03qNluG%2BSGzMaQsMngmJiXdoDCeNH28YHCOi0JEfGTh%2BYHRTqAuE%2Fy0%2FLJJLD8w0HPracBSKFwktKm3LI8BBTjPaa65L5DEiId94OV6k%2FPC81CWTYkh4J%2BAaA06hg9iJ10kaInXR1R14bwBhAqSNOPMex53ApC4B93sULxzV20Cf3AbzX0aZYXBbF830GJZ4P6nBsVEBgboX5RTt%2BmDSNMMmRifWpqXeTy0hMIy9hL0GOqUBKTOyoH5rYfuv7J6Eycdg9HiHYO1ztggWM4TfvPr%2F5hd%2BUTLRSrplPlqodZCx4YIqq%2FehxRMrIPsvflETsTdXRTjP6F4LL5HLMadfApUOF82JHmYs3P9%2FhIrHRkjNcptUlPkAZdZp4gFINF9PEHuCLCJEfVfCJfbZbI5C6jZ3WqX1btyOnW0Cq%2FJpLDPimgCD6rqu7lcSjA70kE2AqWkWJarCgPnf&X-Amz-Signature=900e2345f4960630596133047c013d3e1e72328ab26cc35145819ee798e2f41f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
Neural networks, both biological and artificial, operate on the principle of processing inputs and transmitting outputs through interconnected neurons. The design of artificial neurons, inspired by the structure and function of biological neurons, allows deep learning models to emulate the learning processes of the human brain. Understanding this connection between biology and artificial intelligence provides a foundation for further exploration into the workings of neural networks.
*Additional Notes*: The detailed understanding of both biological and artificial neurons is essential for grasping the complexities of deep learning models and their applications. Further study on how these artificial systems learn and adapt will be covered in subsequent videos.
___
## Mathematical Formulation of Neural Networks
### Introduction
This note discusses the mathematical formulation of neural networks, focusing on the concepts of forward propagation, backpropagation, and activation functions. The emphasis here is on forward propagation, explained through a step-by-step example using numerical values.
### Structure of a Neural Network
#### Neuron Resemblance
- Artificial neurons are designed to resemble biological neurons.
- **Layers in a Neural Network**:
	- **Input Layer**: The first layer that feeds input into the network.
	- **Output Layer**: The final layer that provides the output of the network.
	- **Hidden Layers**: Layers between the input and output layers.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/5e6fffd9-92d0-419c-8e5d-3ad04d1b89bd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QOCQ3XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQD%2B%2BAiBTXgVQeD1JcKrQ7cnY0F6muqYxBey3g91daIn3gIgAtM%2FIzIB1tiqcM0IigIMMw%2F7QTynBhtnNmBxKJMQn1Eq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDNAYqAHyDYvGIiC3qyrcA9SyODnKU6rvrNvFuD1lBW9aJsyfcwoPyxap6dLh7xiEZu5jdvyWSKMTw2q2V6r4kEplYvhHpFM4%2Bw4A%2FsTIisEQe211xcaNhsZQ41qLh5lDwxkBj5NB9umLRVzCot1Pye7y4tdKKLGiVzOdF7KbSnVOC6dHApQI9Ytkmow0GIXO%2FR4wZKKfPf%2Ff6%2BDx65bXSrXax4JJlCdCKLTOn7G%2FTc1Cufhrq1Ywnx4ArQUBzZtbDMG2yHhvJXWkKH0C053Ymm%2Bx1eYYWG7yvEUV%2F%2BIHaN8jufpu7gVpNG%2B1uHf0pCbzP41D224v%2BIQS2qASDQalnSlk2bGtQ0UMZ4YPg26bSDpB9v5J%2FiQdJ1d3R0QsKGhMFfKFcBDySUZ8%2FT8fvRp3SJRTZAZO%2BkQx2mkHolxc2U0z03qNluG%2BSGzMaQsMngmJiXdoDCeNH28YHCOi0JEfGTh%2BYHRTqAuE%2Fy0%2FLJJLD8w0HPracBSKFwktKm3LI8BBTjPaa65L5DEiId94OV6k%2FPC81CWTYkh4J%2BAaA06hg9iJ10kaInXR1R14bwBhAqSNOPMex53ApC4B93sULxzV20Cf3AbzX0aZYXBbF830GJZ4P6nBsVEBgboX5RTt%2BmDSNMMmRifWpqXeTy0hMIy9hL0GOqUBKTOyoH5rYfuv7J6Eycdg9HiHYO1ztggWM4TfvPr%2F5hd%2BUTLRSrplPlqodZCx4YIqq%2FehxRMrIPsvflETsTdXRTjP6F4LL5HLMadfApUOF82JHmYs3P9%2FhIrHRkjNcptUlPkAZdZp4gFINF9PEHuCLCJEfVfCJfbZbI5C6jZ3WqX1btyOnW0Cq%2FJpLDPimgCD6rqu7lcSjA70kE2AqWkWJarCgPnf&X-Amz-Signature=43b77140c1bd0cab20f9fd6938fe86eb11b0aefd4e9ab4b91f12aee8d4fbc4bd&X-Amz-SignedHeaders=host&x-id=GetObject)
### Forward Propagation
#### Definition
Forward propagation is the process through which data passes through the layers of neurons in a neural network, moving from the input layer to the output layer.
### Mathematical Formulation
#### Single Neuron Example
Consider a neuron with two inputs, $ x_1  $ and $ x_2 $, and corresponding weights $ w_1 $ and $ w_2 $. The neuron computes a weighted sum of the inputs and adds a bias term $ b $ to produce an output.
**Mathematical Expression**:
$$ z = w_1 \cdot x_1 + w_2 \cdot x_2 + b $$
The output of the neuron, $ a $, is the result of applying an activation function to $ z $.
$$ a = \sigma(z) $$
where $ \sigma(z) $ is the sigmoid activation function.

**Example Calculation**
Given the following values:
- $ x_1 = 0.1 $
- $ w_1 = 0.15 $
- $ b_1 = 0.4 $
**Step 1: Compute **$ z $
$$ z = w_1 \cdot x_1 + b_1 = 0.15 \cdot 0.1 + 0.4 = 0.415 $$
**Step 2: Apply Sigmoid Function**
$$ \sigma(z) = \frac{1}{1 + e^{-z}} = \frac{1}{1 + e^{-0.415}} \approx 0.6023 $$
#### Multiple Neurons Example
For a network with two neurons:
- The output from the first neuron, $ a_1=0.6023 $, becomes the input to the second neuron.
- Given $ w_2 $ and $ b_2 $, the output of the second neuron is computed in the same way.
**Example Calculation for the Second Neuron**
Given:
- $ w_2 = 0.25 $
- $ b_2 = 0.5 $
**Step 1: Compute **$ z_2 $
$$ z_2 = w_2 \cdot a_1 + b_2 = 0.25 \cdot 0.6023 + 0.5 = 0.6506 $$
**Step 2: Apply Sigmoid Function**
$$ a_2 = \sigma(z_2) \approx 0.7153 $$
This is the predicted output for the given input.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c4b922-6cf5-4a71-95cf-068db25c64b9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QOCQ3XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQD%2B%2BAiBTXgVQeD1JcKrQ7cnY0F6muqYxBey3g91daIn3gIgAtM%2FIzIB1tiqcM0IigIMMw%2F7QTynBhtnNmBxKJMQn1Eq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDNAYqAHyDYvGIiC3qyrcA9SyODnKU6rvrNvFuD1lBW9aJsyfcwoPyxap6dLh7xiEZu5jdvyWSKMTw2q2V6r4kEplYvhHpFM4%2Bw4A%2FsTIisEQe211xcaNhsZQ41qLh5lDwxkBj5NB9umLRVzCot1Pye7y4tdKKLGiVzOdF7KbSnVOC6dHApQI9Ytkmow0GIXO%2FR4wZKKfPf%2Ff6%2BDx65bXSrXax4JJlCdCKLTOn7G%2FTc1Cufhrq1Ywnx4ArQUBzZtbDMG2yHhvJXWkKH0C053Ymm%2Bx1eYYWG7yvEUV%2F%2BIHaN8jufpu7gVpNG%2B1uHf0pCbzP41D224v%2BIQS2qASDQalnSlk2bGtQ0UMZ4YPg26bSDpB9v5J%2FiQdJ1d3R0QsKGhMFfKFcBDySUZ8%2FT8fvRp3SJRTZAZO%2BkQx2mkHolxc2U0z03qNluG%2BSGzMaQsMngmJiXdoDCeNH28YHCOi0JEfGTh%2BYHRTqAuE%2Fy0%2FLJJLD8w0HPracBSKFwktKm3LI8BBTjPaa65L5DEiId94OV6k%2FPC81CWTYkh4J%2BAaA06hg9iJ10kaInXR1R14bwBhAqSNOPMex53ApC4B93sULxzV20Cf3AbzX0aZYXBbF830GJZ4P6nBsVEBgboX5RTt%2BmDSNMMmRifWpqXeTy0hMIy9hL0GOqUBKTOyoH5rYfuv7J6Eycdg9HiHYO1ztggWM4TfvPr%2F5hd%2BUTLRSrplPlqodZCx4YIqq%2FehxRMrIPsvflETsTdXRTjP6F4LL5HLMadfApUOF82JHmYs3P9%2FhIrHRkjNcptUlPkAZdZp4gFINF9PEHuCLCJEfVfCJfbZbI5C6jZ3WqX1btyOnW0Cq%2FJpLDPimgCD6rqu7lcSjA70kE2AqWkWJarCgPnf&X-Amz-Signature=75cb8510349f83cbc19142cb71ea52ed01e511bf4659de37b0d066c71972d89f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Activation Functions
#### Importance
- Activation functions introduce non-linearity into the network, enabling it to learn and perform complex tasks.
- Without an activation function, a neural network behaves like a linear regression model and can only make straight-line predictions because it combines inputs in a simple, linear way. This limits the network to solving problems where the relationship between inputs and outputs is straightforward. An activation function adds the ability to capture more complex, curved patterns, making the network capable of handling more complicated tasks.
#### Sigmoid Function
- The sigmoid function is commonly used as an activation function.
- It maps any real-valued number into a value between 0 and 1.
- It helps to decide whether a neuron should be activated (closer to 1) or not (closer to 0), allowing the network to handle complex patterns and make decisions.
$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$
### Summary
- Forward propagation involves computing the weighted sum of inputs, adding a bias, and applying an activation function to generate an output.
- This process is repeated for each neuron in the network.
- The final output of the network is obtained by propagating data through all the layers.
#### Key Points
- **Input Layer**: Feeds data into the network.
- **Hidden Layers**: Process data using weights, biases, and activation functions.
- **Output Layer**: Produces the final prediction.

*Additional Notes*: 
**Forward propagation** is like passing information through a neural network to make a prediction. It starts with the input data, moves through the network's layers (where each layer processes the data a bit more), and ends with an output or prediction.
**Backward propagation** is the process of improving the network by learning from its mistakes. After making a prediction, the network checks how far off it was from the correct answer, then goes back through the layers and adjusts the connections (weights and biases) to make better predictions in the future. This process is repeated many times to help the network learn.
___
