

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655N6UDUE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQD1zOix%2FfPfw7U%2B1gDTFooebqo8Wj8fP10cB8O7PN13fwIhAP14kSQe38%2FFlx7VmTxNO7ugag08%2Fj5xn5Bc8AQJejD4Kv8DCDcQABoMNjM3NDIzMTgzODA1IgyJzbyeonIoTMLr55sq3AMP1H%2BP0VyFPTG3UqjXo2Zbvg8GE0njqU9WiIN1H4wp5LNI29v8FNWbm4edy1bGrppf3lTtPchrDAS5kkEb43YFmwP0QeBYekdBVh1F8n5Jyd9MsFh4EjYdUJXdxh1OGhUyA7tf6wSRvFF0XEEKvJk9FSyu8R45QulVwubW1mp%2Bw4%2FvU8BMGWLg6OkyTJ0vOi1JL4Lz%2FftR0kg%2BklfRxVwShKjxN6N2fDSn3A9IT7yY1MkEkH%2FSv0N31EJCgBjFgWwBLJgy8UVmX4brvpimycinawiaRz3udMyrrIK26ZRTnevQHcZy74%2BNlM78wbWGeIGN8OfxoSUCk4TZBIwUMbcDHIueQx%2BqMhQUBrMvT9HYsmfzLmfcmoYpDNh0PD1KUeN6YPBrzrj04EIPQL3%2BR9WMNaXwonKdgSNiFQVU9Kgvu7P4quHCHjv%2BF8eLlOYXiir6Ixkp%2Be%2Fz7B1EN%2ByzhjgNhW%2B74K0xgKc7zlm94Rkz3PnKildmVrPQoH0CtdmH%2B6fUIgb6HgDm4xoKjyTabs2mu3%2B98shXxqFe0ATacQinIqzJipvHJ%2Fp4yWw9%2BQ0FHAzUbs4CpGw1SW8pXG1fuRSzRrfoKHLnrwApgkyJHaTW4iyAxm4Vw%2BXdGBBqKjDblIq9BjqkAcXQ%2BFOl%2B%2FX3a7%2FDquoX4izxzJ3etD86%2BqllZjy6xZC8kbf4McE20ErfrIhb46UExL93Cs%2BYcblPqIkLoEpiwAeGtSFmw8TE9B%2BvN9Ty4d3M67phW0d7o%2FV7sH8%2FPWJbdFAOmw2H5QLJ9lpy%2Fj1bh4Dffee9oFqdhLqNHKH5oeM9eXchPh8fRicMQ7zw5mZVhbGxuD6umt4g2nN7XiQeMOsfKnh5&X-Amz-Signature=1b370d4f21ae69493a13cef366fb31ba34130febcafb538973f3b5aad82ba73c&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXOYJSCT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDW%2F0B894g9uMIt7g2Kn0b3X43QO4SUQ8ZjwBBFJaXJ%2BQIgbMCITr1wabcFPrOxZuxZNf%2F%2FM7OfX54I%2BkUS1abI9l8q%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDMY14E3kDaMeiKHHqCrcA4XXPrwYDAh3RcqUccXrob6FblNx4bayQi0HfAiG%2B08eWQc51EOP5w6PINTXFbubrvHii06B5gEn7G%2FISYm%2BnTpyCzNw%2BH1DMKUNVdXrA98jTdz2vxf6aFl1huR%2Fgf%2FLGM511%2B1Pw10ujKfPBQ6OTd6TrjISRlQaJqs4HDYoSnqFHpap%2F%2FmWBl%2BmrUyUloP%2FDLCUK4jsxP33alocqtBY0YjJ17%2BNOOMge9UkjRv%2Fxf7YvSlozOSDHPak7MkQnepNo4y5DLgGbwnfO7TOcFG4yQifEjolPqp9UCsmm02ixflnpFke%2BKPLyNj%2B%2FUu0Bfcl1NpQOo85aYkHbSru4vpY5T01oymlPe8Kg0uILZ2Viuwhjhtyi8BE%2F4RCatjUvemefFTqcBmEi1siaNj2x98dnV3I5AlFiNkuomlEGC8x%2Fd14kh%2B6lrGPMKZV5hp0%2BoiI4KdUFIT8wEwUsYvsRML3p76a3NFG0mwb7R2xCRsGIzw7iDMIqsU45cItLQfifp3SWov9iNmvXVMrwP9AZ7X5JTr7ODyuQCkmwmmILbdje7CHQiYhN8272DMjgvULRKqAEdQNhzbrYu9v4A14%2Fx3WdSzOJ8A05WmP8%2BK2%2BQlbE12O94fVLDsorYEzEPadMJaUir0GOqUB1SOTECStGE3AoItZqCFt%2FZ3vJ%2FQ%2BoFjinxz0mAs2RmE88U9GdGmmUdBSMcYwX5dVrkDzF9qrqM6GZU6ET35aPUgo8S6oiuKJGsM8iYB%2BAO9Hy1Qj%2FL973irmrZqwOc4gXBY05PSVt4HJ8FLZXUchXtX%2FEwhz3aQPzfLFBxO3RrPjheYg5HhZWwRhkgI3tgfrvWlIYRqQUMJbJdmZaLtGKrlbJZgS&X-Amz-Signature=0e72af1096803e8fc75e54a4a3ba39c1cf855addffb349cffb53bdcdbde6d06e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXOYJSCT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDW%2F0B894g9uMIt7g2Kn0b3X43QO4SUQ8ZjwBBFJaXJ%2BQIgbMCITr1wabcFPrOxZuxZNf%2F%2FM7OfX54I%2BkUS1abI9l8q%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDMY14E3kDaMeiKHHqCrcA4XXPrwYDAh3RcqUccXrob6FblNx4bayQi0HfAiG%2B08eWQc51EOP5w6PINTXFbubrvHii06B5gEn7G%2FISYm%2BnTpyCzNw%2BH1DMKUNVdXrA98jTdz2vxf6aFl1huR%2Fgf%2FLGM511%2B1Pw10ujKfPBQ6OTd6TrjISRlQaJqs4HDYoSnqFHpap%2F%2FmWBl%2BmrUyUloP%2FDLCUK4jsxP33alocqtBY0YjJ17%2BNOOMge9UkjRv%2Fxf7YvSlozOSDHPak7MkQnepNo4y5DLgGbwnfO7TOcFG4yQifEjolPqp9UCsmm02ixflnpFke%2BKPLyNj%2B%2FUu0Bfcl1NpQOo85aYkHbSru4vpY5T01oymlPe8Kg0uILZ2Viuwhjhtyi8BE%2F4RCatjUvemefFTqcBmEi1siaNj2x98dnV3I5AlFiNkuomlEGC8x%2Fd14kh%2B6lrGPMKZV5hp0%2BoiI4KdUFIT8wEwUsYvsRML3p76a3NFG0mwb7R2xCRsGIzw7iDMIqsU45cItLQfifp3SWov9iNmvXVMrwP9AZ7X5JTr7ODyuQCkmwmmILbdje7CHQiYhN8272DMjgvULRKqAEdQNhzbrYu9v4A14%2Fx3WdSzOJ8A05WmP8%2BK2%2BQlbE12O94fVLDsorYEzEPadMJaUir0GOqUB1SOTECStGE3AoItZqCFt%2FZ3vJ%2FQ%2BoFjinxz0mAs2RmE88U9GdGmmUdBSMcYwX5dVrkDzF9qrqM6GZU6ET35aPUgo8S6oiuKJGsM8iYB%2BAO9Hy1Qj%2FL973irmrZqwOc4gXBY05PSVt4HJ8FLZXUchXtX%2FEwhz3aQPzfLFBxO3RrPjheYg5HhZWwRhkgI3tgfrvWlIYRqQUMJbJdmZaLtGKrlbJZgS&X-Amz-Signature=84dcc488c122e81e586fab53c96222156253ec12d6911e2afecc82ccf1a34064&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXOYJSCT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDW%2F0B894g9uMIt7g2Kn0b3X43QO4SUQ8ZjwBBFJaXJ%2BQIgbMCITr1wabcFPrOxZuxZNf%2F%2FM7OfX54I%2BkUS1abI9l8q%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDMY14E3kDaMeiKHHqCrcA4XXPrwYDAh3RcqUccXrob6FblNx4bayQi0HfAiG%2B08eWQc51EOP5w6PINTXFbubrvHii06B5gEn7G%2FISYm%2BnTpyCzNw%2BH1DMKUNVdXrA98jTdz2vxf6aFl1huR%2Fgf%2FLGM511%2B1Pw10ujKfPBQ6OTd6TrjISRlQaJqs4HDYoSnqFHpap%2F%2FmWBl%2BmrUyUloP%2FDLCUK4jsxP33alocqtBY0YjJ17%2BNOOMge9UkjRv%2Fxf7YvSlozOSDHPak7MkQnepNo4y5DLgGbwnfO7TOcFG4yQifEjolPqp9UCsmm02ixflnpFke%2BKPLyNj%2B%2FUu0Bfcl1NpQOo85aYkHbSru4vpY5T01oymlPe8Kg0uILZ2Viuwhjhtyi8BE%2F4RCatjUvemefFTqcBmEi1siaNj2x98dnV3I5AlFiNkuomlEGC8x%2Fd14kh%2B6lrGPMKZV5hp0%2BoiI4KdUFIT8wEwUsYvsRML3p76a3NFG0mwb7R2xCRsGIzw7iDMIqsU45cItLQfifp3SWov9iNmvXVMrwP9AZ7X5JTr7ODyuQCkmwmmILbdje7CHQiYhN8272DMjgvULRKqAEdQNhzbrYu9v4A14%2Fx3WdSzOJ8A05WmP8%2BK2%2BQlbE12O94fVLDsorYEzEPadMJaUir0GOqUB1SOTECStGE3AoItZqCFt%2FZ3vJ%2FQ%2BoFjinxz0mAs2RmE88U9GdGmmUdBSMcYwX5dVrkDzF9qrqM6GZU6ET35aPUgo8S6oiuKJGsM8iYB%2BAO9Hy1Qj%2FL973irmrZqwOc4gXBY05PSVt4HJ8FLZXUchXtX%2FEwhz3aQPzfLFBxO3RrPjheYg5HhZWwRhkgI3tgfrvWlIYRqQUMJbJdmZaLtGKrlbJZgS&X-Amz-Signature=a84dec4f1e96680f973c3df0603204842cac1f6b4bd725a9e8d0556ef74f8ce1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXOYJSCT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDW%2F0B894g9uMIt7g2Kn0b3X43QO4SUQ8ZjwBBFJaXJ%2BQIgbMCITr1wabcFPrOxZuxZNf%2F%2FM7OfX54I%2BkUS1abI9l8q%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDMY14E3kDaMeiKHHqCrcA4XXPrwYDAh3RcqUccXrob6FblNx4bayQi0HfAiG%2B08eWQc51EOP5w6PINTXFbubrvHii06B5gEn7G%2FISYm%2BnTpyCzNw%2BH1DMKUNVdXrA98jTdz2vxf6aFl1huR%2Fgf%2FLGM511%2B1Pw10ujKfPBQ6OTd6TrjISRlQaJqs4HDYoSnqFHpap%2F%2FmWBl%2BmrUyUloP%2FDLCUK4jsxP33alocqtBY0YjJ17%2BNOOMge9UkjRv%2Fxf7YvSlozOSDHPak7MkQnepNo4y5DLgGbwnfO7TOcFG4yQifEjolPqp9UCsmm02ixflnpFke%2BKPLyNj%2B%2FUu0Bfcl1NpQOo85aYkHbSru4vpY5T01oymlPe8Kg0uILZ2Viuwhjhtyi8BE%2F4RCatjUvemefFTqcBmEi1siaNj2x98dnV3I5AlFiNkuomlEGC8x%2Fd14kh%2B6lrGPMKZV5hp0%2BoiI4KdUFIT8wEwUsYvsRML3p76a3NFG0mwb7R2xCRsGIzw7iDMIqsU45cItLQfifp3SWov9iNmvXVMrwP9AZ7X5JTr7ODyuQCkmwmmILbdje7CHQiYhN8272DMjgvULRKqAEdQNhzbrYu9v4A14%2Fx3WdSzOJ8A05WmP8%2BK2%2BQlbE12O94fVLDsorYEzEPadMJaUir0GOqUB1SOTECStGE3AoItZqCFt%2FZ3vJ%2FQ%2BoFjinxz0mAs2RmE88U9GdGmmUdBSMcYwX5dVrkDzF9qrqM6GZU6ET35aPUgo8S6oiuKJGsM8iYB%2BAO9Hy1Qj%2FL973irmrZqwOc4gXBY05PSVt4HJ8FLZXUchXtX%2FEwhz3aQPzfLFBxO3RrPjheYg5HhZWwRhkgI3tgfrvWlIYRqQUMJbJdmZaLtGKrlbJZgS&X-Amz-Signature=fcdd06a2e01880bb01686e1b7993f9e10b244b4b8a9234f3802277d4110cc835&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXOYJSCT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDW%2F0B894g9uMIt7g2Kn0b3X43QO4SUQ8ZjwBBFJaXJ%2BQIgbMCITr1wabcFPrOxZuxZNf%2F%2FM7OfX54I%2BkUS1abI9l8q%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDMY14E3kDaMeiKHHqCrcA4XXPrwYDAh3RcqUccXrob6FblNx4bayQi0HfAiG%2B08eWQc51EOP5w6PINTXFbubrvHii06B5gEn7G%2FISYm%2BnTpyCzNw%2BH1DMKUNVdXrA98jTdz2vxf6aFl1huR%2Fgf%2FLGM511%2B1Pw10ujKfPBQ6OTd6TrjISRlQaJqs4HDYoSnqFHpap%2F%2FmWBl%2BmrUyUloP%2FDLCUK4jsxP33alocqtBY0YjJ17%2BNOOMge9UkjRv%2Fxf7YvSlozOSDHPak7MkQnepNo4y5DLgGbwnfO7TOcFG4yQifEjolPqp9UCsmm02ixflnpFke%2BKPLyNj%2B%2FUu0Bfcl1NpQOo85aYkHbSru4vpY5T01oymlPe8Kg0uILZ2Viuwhjhtyi8BE%2F4RCatjUvemefFTqcBmEi1siaNj2x98dnV3I5AlFiNkuomlEGC8x%2Fd14kh%2B6lrGPMKZV5hp0%2BoiI4KdUFIT8wEwUsYvsRML3p76a3NFG0mwb7R2xCRsGIzw7iDMIqsU45cItLQfifp3SWov9iNmvXVMrwP9AZ7X5JTr7ODyuQCkmwmmILbdje7CHQiYhN8272DMjgvULRKqAEdQNhzbrYu9v4A14%2Fx3WdSzOJ8A05WmP8%2BK2%2BQlbE12O94fVLDsorYEzEPadMJaUir0GOqUB1SOTECStGE3AoItZqCFt%2FZ3vJ%2FQ%2BoFjinxz0mAs2RmE88U9GdGmmUdBSMcYwX5dVrkDzF9qrqM6GZU6ET35aPUgo8S6oiuKJGsM8iYB%2BAO9Hy1Qj%2FL973irmrZqwOc4gXBY05PSVt4HJ8FLZXUchXtX%2FEwhz3aQPzfLFBxO3RrPjheYg5HhZWwRhkgI3tgfrvWlIYRqQUMJbJdmZaLtGKrlbJZgS&X-Amz-Signature=84b284003eca3d397dcd93e61cdd4293a8097d0ec6dc884a35a8eae0223335b0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655N6UDUE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQD1zOix%2FfPfw7U%2B1gDTFooebqo8Wj8fP10cB8O7PN13fwIhAP14kSQe38%2FFlx7VmTxNO7ugag08%2Fj5xn5Bc8AQJejD4Kv8DCDcQABoMNjM3NDIzMTgzODA1IgyJzbyeonIoTMLr55sq3AMP1H%2BP0VyFPTG3UqjXo2Zbvg8GE0njqU9WiIN1H4wp5LNI29v8FNWbm4edy1bGrppf3lTtPchrDAS5kkEb43YFmwP0QeBYekdBVh1F8n5Jyd9MsFh4EjYdUJXdxh1OGhUyA7tf6wSRvFF0XEEKvJk9FSyu8R45QulVwubW1mp%2Bw4%2FvU8BMGWLg6OkyTJ0vOi1JL4Lz%2FftR0kg%2BklfRxVwShKjxN6N2fDSn3A9IT7yY1MkEkH%2FSv0N31EJCgBjFgWwBLJgy8UVmX4brvpimycinawiaRz3udMyrrIK26ZRTnevQHcZy74%2BNlM78wbWGeIGN8OfxoSUCk4TZBIwUMbcDHIueQx%2BqMhQUBrMvT9HYsmfzLmfcmoYpDNh0PD1KUeN6YPBrzrj04EIPQL3%2BR9WMNaXwonKdgSNiFQVU9Kgvu7P4quHCHjv%2BF8eLlOYXiir6Ixkp%2Be%2Fz7B1EN%2ByzhjgNhW%2B74K0xgKc7zlm94Rkz3PnKildmVrPQoH0CtdmH%2B6fUIgb6HgDm4xoKjyTabs2mu3%2B98shXxqFe0ATacQinIqzJipvHJ%2Fp4yWw9%2BQ0FHAzUbs4CpGw1SW8pXG1fuRSzRrfoKHLnrwApgkyJHaTW4iyAxm4Vw%2BXdGBBqKjDblIq9BjqkAcXQ%2BFOl%2B%2FX3a7%2FDquoX4izxzJ3etD86%2BqllZjy6xZC8kbf4McE20ErfrIhb46UExL93Cs%2BYcblPqIkLoEpiwAeGtSFmw8TE9B%2BvN9Ty4d3M67phW0d7o%2FV7sH8%2FPWJbdFAOmw2H5QLJ9lpy%2Fj1bh4Dffee9oFqdhLqNHKH5oeM9eXchPh8fRicMQ7zw5mZVhbGxuD6umt4g2nN7XiQeMOsfKnh5&X-Amz-Signature=c268181af919f63db0a53978ba26296b1178c0b7489583c10de7f7969aba69ac&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655N6UDUE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQD1zOix%2FfPfw7U%2B1gDTFooebqo8Wj8fP10cB8O7PN13fwIhAP14kSQe38%2FFlx7VmTxNO7ugag08%2Fj5xn5Bc8AQJejD4Kv8DCDcQABoMNjM3NDIzMTgzODA1IgyJzbyeonIoTMLr55sq3AMP1H%2BP0VyFPTG3UqjXo2Zbvg8GE0njqU9WiIN1H4wp5LNI29v8FNWbm4edy1bGrppf3lTtPchrDAS5kkEb43YFmwP0QeBYekdBVh1F8n5Jyd9MsFh4EjYdUJXdxh1OGhUyA7tf6wSRvFF0XEEKvJk9FSyu8R45QulVwubW1mp%2Bw4%2FvU8BMGWLg6OkyTJ0vOi1JL4Lz%2FftR0kg%2BklfRxVwShKjxN6N2fDSn3A9IT7yY1MkEkH%2FSv0N31EJCgBjFgWwBLJgy8UVmX4brvpimycinawiaRz3udMyrrIK26ZRTnevQHcZy74%2BNlM78wbWGeIGN8OfxoSUCk4TZBIwUMbcDHIueQx%2BqMhQUBrMvT9HYsmfzLmfcmoYpDNh0PD1KUeN6YPBrzrj04EIPQL3%2BR9WMNaXwonKdgSNiFQVU9Kgvu7P4quHCHjv%2BF8eLlOYXiir6Ixkp%2Be%2Fz7B1EN%2ByzhjgNhW%2B74K0xgKc7zlm94Rkz3PnKildmVrPQoH0CtdmH%2B6fUIgb6HgDm4xoKjyTabs2mu3%2B98shXxqFe0ATacQinIqzJipvHJ%2Fp4yWw9%2BQ0FHAzUbs4CpGw1SW8pXG1fuRSzRrfoKHLnrwApgkyJHaTW4iyAxm4Vw%2BXdGBBqKjDblIq9BjqkAcXQ%2BFOl%2B%2FX3a7%2FDquoX4izxzJ3etD86%2BqllZjy6xZC8kbf4McE20ErfrIhb46UExL93Cs%2BYcblPqIkLoEpiwAeGtSFmw8TE9B%2BvN9Ty4d3M67phW0d7o%2FV7sH8%2FPWJbdFAOmw2H5QLJ9lpy%2Fj1bh4Dffee9oFqdhLqNHKH5oeM9eXchPh8fRicMQ7zw5mZVhbGxuD6umt4g2nN7XiQeMOsfKnh5&X-Amz-Signature=e5211fef688dd5ca68cf5ed0e0b483105ff1171eb1a83fbd68fd1e2391674112&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655N6UDUE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQD1zOix%2FfPfw7U%2B1gDTFooebqo8Wj8fP10cB8O7PN13fwIhAP14kSQe38%2FFlx7VmTxNO7ugag08%2Fj5xn5Bc8AQJejD4Kv8DCDcQABoMNjM3NDIzMTgzODA1IgyJzbyeonIoTMLr55sq3AMP1H%2BP0VyFPTG3UqjXo2Zbvg8GE0njqU9WiIN1H4wp5LNI29v8FNWbm4edy1bGrppf3lTtPchrDAS5kkEb43YFmwP0QeBYekdBVh1F8n5Jyd9MsFh4EjYdUJXdxh1OGhUyA7tf6wSRvFF0XEEKvJk9FSyu8R45QulVwubW1mp%2Bw4%2FvU8BMGWLg6OkyTJ0vOi1JL4Lz%2FftR0kg%2BklfRxVwShKjxN6N2fDSn3A9IT7yY1MkEkH%2FSv0N31EJCgBjFgWwBLJgy8UVmX4brvpimycinawiaRz3udMyrrIK26ZRTnevQHcZy74%2BNlM78wbWGeIGN8OfxoSUCk4TZBIwUMbcDHIueQx%2BqMhQUBrMvT9HYsmfzLmfcmoYpDNh0PD1KUeN6YPBrzrj04EIPQL3%2BR9WMNaXwonKdgSNiFQVU9Kgvu7P4quHCHjv%2BF8eLlOYXiir6Ixkp%2Be%2Fz7B1EN%2ByzhjgNhW%2B74K0xgKc7zlm94Rkz3PnKildmVrPQoH0CtdmH%2B6fUIgb6HgDm4xoKjyTabs2mu3%2B98shXxqFe0ATacQinIqzJipvHJ%2Fp4yWw9%2BQ0FHAzUbs4CpGw1SW8pXG1fuRSzRrfoKHLnrwApgkyJHaTW4iyAxm4Vw%2BXdGBBqKjDblIq9BjqkAcXQ%2BFOl%2B%2FX3a7%2FDquoX4izxzJ3etD86%2BqllZjy6xZC8kbf4McE20ErfrIhb46UExL93Cs%2BYcblPqIkLoEpiwAeGtSFmw8TE9B%2BvN9Ty4d3M67phW0d7o%2FV7sH8%2FPWJbdFAOmw2H5QLJ9lpy%2Fj1bh4Dffee9oFqdhLqNHKH5oeM9eXchPh8fRicMQ7zw5mZVhbGxuD6umt4g2nN7XiQeMOsfKnh5&X-Amz-Signature=214cb1a52cc1eed83a4a17642773fac7ba1752e68a52b9c4e8179e53c56f3a51&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655N6UDUE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQD1zOix%2FfPfw7U%2B1gDTFooebqo8Wj8fP10cB8O7PN13fwIhAP14kSQe38%2FFlx7VmTxNO7ugag08%2Fj5xn5Bc8AQJejD4Kv8DCDcQABoMNjM3NDIzMTgzODA1IgyJzbyeonIoTMLr55sq3AMP1H%2BP0VyFPTG3UqjXo2Zbvg8GE0njqU9WiIN1H4wp5LNI29v8FNWbm4edy1bGrppf3lTtPchrDAS5kkEb43YFmwP0QeBYekdBVh1F8n5Jyd9MsFh4EjYdUJXdxh1OGhUyA7tf6wSRvFF0XEEKvJk9FSyu8R45QulVwubW1mp%2Bw4%2FvU8BMGWLg6OkyTJ0vOi1JL4Lz%2FftR0kg%2BklfRxVwShKjxN6N2fDSn3A9IT7yY1MkEkH%2FSv0N31EJCgBjFgWwBLJgy8UVmX4brvpimycinawiaRz3udMyrrIK26ZRTnevQHcZy74%2BNlM78wbWGeIGN8OfxoSUCk4TZBIwUMbcDHIueQx%2BqMhQUBrMvT9HYsmfzLmfcmoYpDNh0PD1KUeN6YPBrzrj04EIPQL3%2BR9WMNaXwonKdgSNiFQVU9Kgvu7P4quHCHjv%2BF8eLlOYXiir6Ixkp%2Be%2Fz7B1EN%2ByzhjgNhW%2B74K0xgKc7zlm94Rkz3PnKildmVrPQoH0CtdmH%2B6fUIgb6HgDm4xoKjyTabs2mu3%2B98shXxqFe0ATacQinIqzJipvHJ%2Fp4yWw9%2BQ0FHAzUbs4CpGw1SW8pXG1fuRSzRrfoKHLnrwApgkyJHaTW4iyAxm4Vw%2BXdGBBqKjDblIq9BjqkAcXQ%2BFOl%2B%2FX3a7%2FDquoX4izxzJ3etD86%2BqllZjy6xZC8kbf4McE20ErfrIhb46UExL93Cs%2BYcblPqIkLoEpiwAeGtSFmw8TE9B%2BvN9Ty4d3M67phW0d7o%2FV7sH8%2FPWJbdFAOmw2H5QLJ9lpy%2Fj1bh4Dffee9oFqdhLqNHKH5oeM9eXchPh8fRicMQ7zw5mZVhbGxuD6umt4g2nN7XiQeMOsfKnh5&X-Amz-Signature=74625aef10ef463fa204f3407383170004995e19bd121be79c1566378e56e127&X-Amz-SignedHeaders=host&x-id=GetObject)
### Video Sequences
A **video** can be viewed as a sequence of multiple **images** or **frames**.
### Image Formats
Common image file formats include:
- **JPEG** (Joint Photographic Expert Group)
- **PNG** (Portable Network Graphics)
These formats compress and reduce file sizes while maintaining image quality.
### Image Processing Libraries in Python
#### Pillow (PIL)
Pillow is a widely used Python library for image manipulation.
- To load an image:
```python
from PIL import Image
img = Image.open('image.png')
```
- **Attributes** of a Pillow image:
	- `format`: The file format (e.g., PNG, JPEG).
	- `size`: The dimensions of the image (width x height).
	- `mode`: The color space (e.g., RGB, L for grayscale).
#### Example: Converting to Gray-Scale
- Convert an image to **gray-scale**:
```python
gray_img = img.convert('L')
gray_img.show()
```
#### Example: Quantization
- **Quantize** an image to reduce the number of intensity levels:
```python
quantized_img = img.quantize(colors=16)
quantized_img.show()
```
#### OpenCV
**OpenCV** is a powerful library for **computer vision** with more functionality than PIL.
- Import OpenCV:
```python
import cv2
```
- Load an image:
```python
img = cv2.imread('image.png')
```
- **Attributes** of an OpenCV image:
	- OpenCV represents images as **NumPy arrays**.
	- The **color channels** are ordered as **BGR** (blue, green, red) instead of **RGB**.
#### Example: Color Space Conversion
- Convert from **BGR to RGB**:
```python
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```
- Convert to **gray-scale**:
```python
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
#### Example: Saving an Image
- Save an image using OpenCV:
```python
cv2.imwrite('output.png', img)
```
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655N6UDUE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQD1zOix%2FfPfw7U%2B1gDTFooebqo8Wj8fP10cB8O7PN13fwIhAP14kSQe38%2FFlx7VmTxNO7ugag08%2Fj5xn5Bc8AQJejD4Kv8DCDcQABoMNjM3NDIzMTgzODA1IgyJzbyeonIoTMLr55sq3AMP1H%2BP0VyFPTG3UqjXo2Zbvg8GE0njqU9WiIN1H4wp5LNI29v8FNWbm4edy1bGrppf3lTtPchrDAS5kkEb43YFmwP0QeBYekdBVh1F8n5Jyd9MsFh4EjYdUJXdxh1OGhUyA7tf6wSRvFF0XEEKvJk9FSyu8R45QulVwubW1mp%2Bw4%2FvU8BMGWLg6OkyTJ0vOi1JL4Lz%2FftR0kg%2BklfRxVwShKjxN6N2fDSn3A9IT7yY1MkEkH%2FSv0N31EJCgBjFgWwBLJgy8UVmX4brvpimycinawiaRz3udMyrrIK26ZRTnevQHcZy74%2BNlM78wbWGeIGN8OfxoSUCk4TZBIwUMbcDHIueQx%2BqMhQUBrMvT9HYsmfzLmfcmoYpDNh0PD1KUeN6YPBrzrj04EIPQL3%2BR9WMNaXwonKdgSNiFQVU9Kgvu7P4quHCHjv%2BF8eLlOYXiir6Ixkp%2Be%2Fz7B1EN%2ByzhjgNhW%2B74K0xgKc7zlm94Rkz3PnKildmVrPQoH0CtdmH%2B6fUIgb6HgDm4xoKjyTabs2mu3%2B98shXxqFe0ATacQinIqzJipvHJ%2Fp4yWw9%2BQ0FHAzUbs4CpGw1SW8pXG1fuRSzRrfoKHLnrwApgkyJHaTW4iyAxm4Vw%2BXdGBBqKjDblIq9BjqkAcXQ%2BFOl%2B%2FX3a7%2FDquoX4izxzJ3etD86%2BqllZjy6xZC8kbf4McE20ErfrIhb46UExL93Cs%2BYcblPqIkLoEpiwAeGtSFmw8TE9B%2BvN9Ty4d3M67phW0d7o%2FV7sH8%2FPWJbdFAOmw2H5QLJ9lpy%2Fj1bh4Dffee9oFqdhLqNHKH5oeM9eXchPh8fRicMQ7zw5mZVhbGxuD6umt4g2nN7XiQeMOsfKnh5&X-Amz-Signature=f19dcad0b4e28384affb4f09f87fed5579c3bb4a05db156e5f331a51550d8dda&X-Amz-SignedHeaders=host&x-id=GetObject)
### Working with Color Channels
Using **slices**, individual color channels (e.g., **blue**, **green**, **red**) can be extracted:
```python
blue_channel = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel = img[:, :, 2]
```
Each channel can then be processed or analyzed separately.
#### Conversion between PIL and NumPy Arrays
PIL images can be easily converted to **NumPy arrays** for further processing:
```python
import numpy as np
np_img = np.array(img)
```
This conversion is particularly useful when integrating with **OpenCV** and performing advanced operations.
### Conclusion
Both **PIL** and **OpenCV** are essential tools for handling and processing digital images in Python. Each has its strengths:
- **PIL** is simple and great for basic tasks.
- **OpenCV** offers more advanced capabilities for **computer vision** applications.
___


