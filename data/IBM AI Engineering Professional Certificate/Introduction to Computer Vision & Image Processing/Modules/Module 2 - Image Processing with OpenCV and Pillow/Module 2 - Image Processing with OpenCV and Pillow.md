

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQ5R6HQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHr%2BIqRxamM8WRzbVZLurZgbBZXXYLeNpJmcFVI1o3mwAiEAtx8lPb%2BeyYYHD%2FlKpg4e3anAR6chyUv%2BjcB2NYWxk9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEj4UJtr5lX8jLyfGSrcA9iYp1nMpjz1YBbxozSN8U4jwI3kqkSZWNwmXMOEv9gizwhcaRKp2BowXCJaVZ6dDAHpsjKq0fz66KTzc837K4E3oMumeymOCfkz%2FZy%2FsQi79DptSDV%2BcBXpdYvMzYvsgFbPFuY%2Biy9E%2Br7vD6m3Aid6BPgqwDz6%2BbhtFppHr7ZmF%2FEQnQYAPqWRxmzrl2coefszuoWVIkm5k7avqT50ga7WnjIe%2FCH%2BwrGkkZ7jSpRYG7ounrRDa1HbAurwd2PmRsxFW6ODSYc23N7Vgv%2FCVqRN0KxMkixvw5jxZgbWkBRcwBoXeobPgBbH1Sc%2FzjmQKX8Q8a%2ByL3WP2KcSpYPoIagamCltC4WkMfkblynoo%2FTiO3TCJGMj9qbryKkGICYc8wbpu25dY4kuMr%2Bans8smJcLzpS8AY6nOrW%2Fg%2FlPWZswoWH9GemlaJTOllSedhjRWi%2F%2BoBsLwgWmaDGqTz99qGG9BQUkGIgbROcquXjfWiEgFX34A2sN2DDyFwNn10dEgRabKcdD7enQKSSPkxKrp%2FLCB6n5xnSTeMeuu6R9TcxaNmgHqLSZWV%2FttaMUiE3K3RQQoaEi4B5EJSKQMkGacHB7vGYh%2Fjw8pJdim6BFvOAgaRKUK2MqPO7qDVxpML%2Bk97wGOqUB%2Bw32S1p4Ge4zuwPyo2iz%2FZ5EOqEC6KJkFQfd%2FwkFACnSrgpj2oLBlx4jmH3Mw5kDN8rUTHM1QMMdMqmfAzjETehp5enFmaVhKU8mIqFz0cdSewKa%2FkW5B25lbt9ckSn8sQ9FJLbQ0MeItzb1k5BWKOclDFC5s1eyrZ9S7HA3o6w0tq5NDJpgt6K3xPBDd%2BuLQLDaWPvh9O9Gav5sUeu7%2FXv9V9uR&X-Amz-Signature=d8e456ab7cbc2c2cc5b8be59878cc945967f457158bf4addd1842e30ceff7eda&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIUQRTGM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBjJA8QE0k%2F5g8hTWhvZgMmu1PwGrpXtecsndGjDXdzlAiA1TBhZv9R%2F%2FHGrOt2Huj8HgvXn8RAZqivjfNyQTYppyCqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiKywszNcRPbUc9YAKtwD%2FtPKMK9dkHeLhQGYijtCKxH0MgtyxjftCZgu7Ctfbwxp3d4mztut1oH6GyVPsSqLadWav7e6bKaAISkmdOcafqEKOpE459HQ9hIEzmHhSvxhGcPKPQ2QUxFMTMlep7XVu4W0seyxvH2C7Z1Rhdxbeg705YvNN3NLbMe%2BiSpbJd9Dc2M1vFB0JeWidcZDbuG5vKtkWCYBlVEdAzxY5GzsCkJ%2Bf7Z8WoBf1VzxGL%2Bmq4bGnmpLZRN4wHU7aJ39gDMNX0XD1b6H6uR3o5J0aD4Ag226qjqiFyJ%2BAowHx3jdKkC935%2BEiQLcRJHc%2FH%2FLqxrznp6AAdokMbglAkhcnHHzsFxeECuO5P5pFzgcV1tul5QHdvvQOn5mHs5lW2hhAI%2B%2BsfuCwtLMnKC%2F1jdSpyR8vVfaNtP0i2Sk1immkPBEeFJoBwnl15tmwuYftGgoO853QaL50LTCTJK6oLiKU0Am8srmQ1CavFXGK%2FOTuKEJ5nD5R7ESkAR%2Ft9rjo%2BV6%2FSgc8uDyS7di4xWbRhqp8cxuUyskoHtT1SMWBkn6WQT6iooa7PyuG0BhcRN73frDao6RPLNl%2FNT2l1TLv8MHEHvOjwKYEWjUDBLOeAbY5%2BzfnaaAuOyAIV45nCYY3FYwysz3vAY6pgELnWelsCI6fw25qCmnKpDB9LWXlMCM4hgPCgWrfIgCHWFiWaMut0ttkGmqV41cz3%2FCOej1DsloF4qU1RJXs%2BdcThT3g2xFtq0RIM9HkjdGaBgxZ8OBgBwR2nZ0dMdSQEtWHhwcb3yTFLUNmfU0YWz1iQFCKHRA0Zb5amHUb1YFosjJIakzG1L2F5M64q9y%2B%2Fpt6uJO4y7yDiRybf0Sg6M5vWlIlafz&X-Amz-Signature=0710b00b077c28f022a08b39d0420d2324bf35bfa7e52aba79c4bbbd7c8bfca7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIUQRTGM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBjJA8QE0k%2F5g8hTWhvZgMmu1PwGrpXtecsndGjDXdzlAiA1TBhZv9R%2F%2FHGrOt2Huj8HgvXn8RAZqivjfNyQTYppyCqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiKywszNcRPbUc9YAKtwD%2FtPKMK9dkHeLhQGYijtCKxH0MgtyxjftCZgu7Ctfbwxp3d4mztut1oH6GyVPsSqLadWav7e6bKaAISkmdOcafqEKOpE459HQ9hIEzmHhSvxhGcPKPQ2QUxFMTMlep7XVu4W0seyxvH2C7Z1Rhdxbeg705YvNN3NLbMe%2BiSpbJd9Dc2M1vFB0JeWidcZDbuG5vKtkWCYBlVEdAzxY5GzsCkJ%2Bf7Z8WoBf1VzxGL%2Bmq4bGnmpLZRN4wHU7aJ39gDMNX0XD1b6H6uR3o5J0aD4Ag226qjqiFyJ%2BAowHx3jdKkC935%2BEiQLcRJHc%2FH%2FLqxrznp6AAdokMbglAkhcnHHzsFxeECuO5P5pFzgcV1tul5QHdvvQOn5mHs5lW2hhAI%2B%2BsfuCwtLMnKC%2F1jdSpyR8vVfaNtP0i2Sk1immkPBEeFJoBwnl15tmwuYftGgoO853QaL50LTCTJK6oLiKU0Am8srmQ1CavFXGK%2FOTuKEJ5nD5R7ESkAR%2Ft9rjo%2BV6%2FSgc8uDyS7di4xWbRhqp8cxuUyskoHtT1SMWBkn6WQT6iooa7PyuG0BhcRN73frDao6RPLNl%2FNT2l1TLv8MHEHvOjwKYEWjUDBLOeAbY5%2BzfnaaAuOyAIV45nCYY3FYwysz3vAY6pgELnWelsCI6fw25qCmnKpDB9LWXlMCM4hgPCgWrfIgCHWFiWaMut0ttkGmqV41cz3%2FCOej1DsloF4qU1RJXs%2BdcThT3g2xFtq0RIM9HkjdGaBgxZ8OBgBwR2nZ0dMdSQEtWHhwcb3yTFLUNmfU0YWz1iQFCKHRA0Zb5amHUb1YFosjJIakzG1L2F5M64q9y%2B%2Fpt6uJO4y7yDiRybf0Sg6M5vWlIlafz&X-Amz-Signature=badfcb8da3d9d8d78f6e7ee048d665a2e45032868f375822a2e968fb4858990d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIUQRTGM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBjJA8QE0k%2F5g8hTWhvZgMmu1PwGrpXtecsndGjDXdzlAiA1TBhZv9R%2F%2FHGrOt2Huj8HgvXn8RAZqivjfNyQTYppyCqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiKywszNcRPbUc9YAKtwD%2FtPKMK9dkHeLhQGYijtCKxH0MgtyxjftCZgu7Ctfbwxp3d4mztut1oH6GyVPsSqLadWav7e6bKaAISkmdOcafqEKOpE459HQ9hIEzmHhSvxhGcPKPQ2QUxFMTMlep7XVu4W0seyxvH2C7Z1Rhdxbeg705YvNN3NLbMe%2BiSpbJd9Dc2M1vFB0JeWidcZDbuG5vKtkWCYBlVEdAzxY5GzsCkJ%2Bf7Z8WoBf1VzxGL%2Bmq4bGnmpLZRN4wHU7aJ39gDMNX0XD1b6H6uR3o5J0aD4Ag226qjqiFyJ%2BAowHx3jdKkC935%2BEiQLcRJHc%2FH%2FLqxrznp6AAdokMbglAkhcnHHzsFxeECuO5P5pFzgcV1tul5QHdvvQOn5mHs5lW2hhAI%2B%2BsfuCwtLMnKC%2F1jdSpyR8vVfaNtP0i2Sk1immkPBEeFJoBwnl15tmwuYftGgoO853QaL50LTCTJK6oLiKU0Am8srmQ1CavFXGK%2FOTuKEJ5nD5R7ESkAR%2Ft9rjo%2BV6%2FSgc8uDyS7di4xWbRhqp8cxuUyskoHtT1SMWBkn6WQT6iooa7PyuG0BhcRN73frDao6RPLNl%2FNT2l1TLv8MHEHvOjwKYEWjUDBLOeAbY5%2BzfnaaAuOyAIV45nCYY3FYwysz3vAY6pgELnWelsCI6fw25qCmnKpDB9LWXlMCM4hgPCgWrfIgCHWFiWaMut0ttkGmqV41cz3%2FCOej1DsloF4qU1RJXs%2BdcThT3g2xFtq0RIM9HkjdGaBgxZ8OBgBwR2nZ0dMdSQEtWHhwcb3yTFLUNmfU0YWz1iQFCKHRA0Zb5amHUb1YFosjJIakzG1L2F5M64q9y%2B%2Fpt6uJO4y7yDiRybf0Sg6M5vWlIlafz&X-Amz-Signature=692d9a790a99d01298efd984d0644855e3d406e52f0003ab35aada902a24bf9e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIUQRTGM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBjJA8QE0k%2F5g8hTWhvZgMmu1PwGrpXtecsndGjDXdzlAiA1TBhZv9R%2F%2FHGrOt2Huj8HgvXn8RAZqivjfNyQTYppyCqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiKywszNcRPbUc9YAKtwD%2FtPKMK9dkHeLhQGYijtCKxH0MgtyxjftCZgu7Ctfbwxp3d4mztut1oH6GyVPsSqLadWav7e6bKaAISkmdOcafqEKOpE459HQ9hIEzmHhSvxhGcPKPQ2QUxFMTMlep7XVu4W0seyxvH2C7Z1Rhdxbeg705YvNN3NLbMe%2BiSpbJd9Dc2M1vFB0JeWidcZDbuG5vKtkWCYBlVEdAzxY5GzsCkJ%2Bf7Z8WoBf1VzxGL%2Bmq4bGnmpLZRN4wHU7aJ39gDMNX0XD1b6H6uR3o5J0aD4Ag226qjqiFyJ%2BAowHx3jdKkC935%2BEiQLcRJHc%2FH%2FLqxrznp6AAdokMbglAkhcnHHzsFxeECuO5P5pFzgcV1tul5QHdvvQOn5mHs5lW2hhAI%2B%2BsfuCwtLMnKC%2F1jdSpyR8vVfaNtP0i2Sk1immkPBEeFJoBwnl15tmwuYftGgoO853QaL50LTCTJK6oLiKU0Am8srmQ1CavFXGK%2FOTuKEJ5nD5R7ESkAR%2Ft9rjo%2BV6%2FSgc8uDyS7di4xWbRhqp8cxuUyskoHtT1SMWBkn6WQT6iooa7PyuG0BhcRN73frDao6RPLNl%2FNT2l1TLv8MHEHvOjwKYEWjUDBLOeAbY5%2BzfnaaAuOyAIV45nCYY3FYwysz3vAY6pgELnWelsCI6fw25qCmnKpDB9LWXlMCM4hgPCgWrfIgCHWFiWaMut0ttkGmqV41cz3%2FCOej1DsloF4qU1RJXs%2BdcThT3g2xFtq0RIM9HkjdGaBgxZ8OBgBwR2nZ0dMdSQEtWHhwcb3yTFLUNmfU0YWz1iQFCKHRA0Zb5amHUb1YFosjJIakzG1L2F5M64q9y%2B%2Fpt6uJO4y7yDiRybf0Sg6M5vWlIlafz&X-Amz-Signature=13db202275ab0ab5880b74144c4178092cc81ddae6f9547a2d48a3b1588cf56d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIUQRTGM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBjJA8QE0k%2F5g8hTWhvZgMmu1PwGrpXtecsndGjDXdzlAiA1TBhZv9R%2F%2FHGrOt2Huj8HgvXn8RAZqivjfNyQTYppyCqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiKywszNcRPbUc9YAKtwD%2FtPKMK9dkHeLhQGYijtCKxH0MgtyxjftCZgu7Ctfbwxp3d4mztut1oH6GyVPsSqLadWav7e6bKaAISkmdOcafqEKOpE459HQ9hIEzmHhSvxhGcPKPQ2QUxFMTMlep7XVu4W0seyxvH2C7Z1Rhdxbeg705YvNN3NLbMe%2BiSpbJd9Dc2M1vFB0JeWidcZDbuG5vKtkWCYBlVEdAzxY5GzsCkJ%2Bf7Z8WoBf1VzxGL%2Bmq4bGnmpLZRN4wHU7aJ39gDMNX0XD1b6H6uR3o5J0aD4Ag226qjqiFyJ%2BAowHx3jdKkC935%2BEiQLcRJHc%2FH%2FLqxrznp6AAdokMbglAkhcnHHzsFxeECuO5P5pFzgcV1tul5QHdvvQOn5mHs5lW2hhAI%2B%2BsfuCwtLMnKC%2F1jdSpyR8vVfaNtP0i2Sk1immkPBEeFJoBwnl15tmwuYftGgoO853QaL50LTCTJK6oLiKU0Am8srmQ1CavFXGK%2FOTuKEJ5nD5R7ESkAR%2Ft9rjo%2BV6%2FSgc8uDyS7di4xWbRhqp8cxuUyskoHtT1SMWBkn6WQT6iooa7PyuG0BhcRN73frDao6RPLNl%2FNT2l1TLv8MHEHvOjwKYEWjUDBLOeAbY5%2BzfnaaAuOyAIV45nCYY3FYwysz3vAY6pgELnWelsCI6fw25qCmnKpDB9LWXlMCM4hgPCgWrfIgCHWFiWaMut0ttkGmqV41cz3%2FCOej1DsloF4qU1RJXs%2BdcThT3g2xFtq0RIM9HkjdGaBgxZ8OBgBwR2nZ0dMdSQEtWHhwcb3yTFLUNmfU0YWz1iQFCKHRA0Zb5amHUb1YFosjJIakzG1L2F5M64q9y%2B%2Fpt6uJO4y7yDiRybf0Sg6M5vWlIlafz&X-Amz-Signature=bcdfe875c43bd5f9dfc657576c5ce00ee8071576e57e8b971f380f52473165a9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQ5R6HQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHr%2BIqRxamM8WRzbVZLurZgbBZXXYLeNpJmcFVI1o3mwAiEAtx8lPb%2BeyYYHD%2FlKpg4e3anAR6chyUv%2BjcB2NYWxk9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEj4UJtr5lX8jLyfGSrcA9iYp1nMpjz1YBbxozSN8U4jwI3kqkSZWNwmXMOEv9gizwhcaRKp2BowXCJaVZ6dDAHpsjKq0fz66KTzc837K4E3oMumeymOCfkz%2FZy%2FsQi79DptSDV%2BcBXpdYvMzYvsgFbPFuY%2Biy9E%2Br7vD6m3Aid6BPgqwDz6%2BbhtFppHr7ZmF%2FEQnQYAPqWRxmzrl2coefszuoWVIkm5k7avqT50ga7WnjIe%2FCH%2BwrGkkZ7jSpRYG7ounrRDa1HbAurwd2PmRsxFW6ODSYc23N7Vgv%2FCVqRN0KxMkixvw5jxZgbWkBRcwBoXeobPgBbH1Sc%2FzjmQKX8Q8a%2ByL3WP2KcSpYPoIagamCltC4WkMfkblynoo%2FTiO3TCJGMj9qbryKkGICYc8wbpu25dY4kuMr%2Bans8smJcLzpS8AY6nOrW%2Fg%2FlPWZswoWH9GemlaJTOllSedhjRWi%2F%2BoBsLwgWmaDGqTz99qGG9BQUkGIgbROcquXjfWiEgFX34A2sN2DDyFwNn10dEgRabKcdD7enQKSSPkxKrp%2FLCB6n5xnSTeMeuu6R9TcxaNmgHqLSZWV%2FttaMUiE3K3RQQoaEi4B5EJSKQMkGacHB7vGYh%2Fjw8pJdim6BFvOAgaRKUK2MqPO7qDVxpML%2Bk97wGOqUB%2Bw32S1p4Ge4zuwPyo2iz%2FZ5EOqEC6KJkFQfd%2FwkFACnSrgpj2oLBlx4jmH3Mw5kDN8rUTHM1QMMdMqmfAzjETehp5enFmaVhKU8mIqFz0cdSewKa%2FkW5B25lbt9ckSn8sQ9FJLbQ0MeItzb1k5BWKOclDFC5s1eyrZ9S7HA3o6w0tq5NDJpgt6K3xPBDd%2BuLQLDaWPvh9O9Gav5sUeu7%2FXv9V9uR&X-Amz-Signature=baff8ee3910eda93f076f4d7923410e2c03de410492404fd14e8329d72f5bf61&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQ5R6HQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHr%2BIqRxamM8WRzbVZLurZgbBZXXYLeNpJmcFVI1o3mwAiEAtx8lPb%2BeyYYHD%2FlKpg4e3anAR6chyUv%2BjcB2NYWxk9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEj4UJtr5lX8jLyfGSrcA9iYp1nMpjz1YBbxozSN8U4jwI3kqkSZWNwmXMOEv9gizwhcaRKp2BowXCJaVZ6dDAHpsjKq0fz66KTzc837K4E3oMumeymOCfkz%2FZy%2FsQi79DptSDV%2BcBXpdYvMzYvsgFbPFuY%2Biy9E%2Br7vD6m3Aid6BPgqwDz6%2BbhtFppHr7ZmF%2FEQnQYAPqWRxmzrl2coefszuoWVIkm5k7avqT50ga7WnjIe%2FCH%2BwrGkkZ7jSpRYG7ounrRDa1HbAurwd2PmRsxFW6ODSYc23N7Vgv%2FCVqRN0KxMkixvw5jxZgbWkBRcwBoXeobPgBbH1Sc%2FzjmQKX8Q8a%2ByL3WP2KcSpYPoIagamCltC4WkMfkblynoo%2FTiO3TCJGMj9qbryKkGICYc8wbpu25dY4kuMr%2Bans8smJcLzpS8AY6nOrW%2Fg%2FlPWZswoWH9GemlaJTOllSedhjRWi%2F%2BoBsLwgWmaDGqTz99qGG9BQUkGIgbROcquXjfWiEgFX34A2sN2DDyFwNn10dEgRabKcdD7enQKSSPkxKrp%2FLCB6n5xnSTeMeuu6R9TcxaNmgHqLSZWV%2FttaMUiE3K3RQQoaEi4B5EJSKQMkGacHB7vGYh%2Fjw8pJdim6BFvOAgaRKUK2MqPO7qDVxpML%2Bk97wGOqUB%2Bw32S1p4Ge4zuwPyo2iz%2FZ5EOqEC6KJkFQfd%2FwkFACnSrgpj2oLBlx4jmH3Mw5kDN8rUTHM1QMMdMqmfAzjETehp5enFmaVhKU8mIqFz0cdSewKa%2FkW5B25lbt9ckSn8sQ9FJLbQ0MeItzb1k5BWKOclDFC5s1eyrZ9S7HA3o6w0tq5NDJpgt6K3xPBDd%2BuLQLDaWPvh9O9Gav5sUeu7%2FXv9V9uR&X-Amz-Signature=368257d1c79aa16de264fe1b44ed6f14984c9b6812a82916d6708cf2a89a5379&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQ5R6HQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHr%2BIqRxamM8WRzbVZLurZgbBZXXYLeNpJmcFVI1o3mwAiEAtx8lPb%2BeyYYHD%2FlKpg4e3anAR6chyUv%2BjcB2NYWxk9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEj4UJtr5lX8jLyfGSrcA9iYp1nMpjz1YBbxozSN8U4jwI3kqkSZWNwmXMOEv9gizwhcaRKp2BowXCJaVZ6dDAHpsjKq0fz66KTzc837K4E3oMumeymOCfkz%2FZy%2FsQi79DptSDV%2BcBXpdYvMzYvsgFbPFuY%2Biy9E%2Br7vD6m3Aid6BPgqwDz6%2BbhtFppHr7ZmF%2FEQnQYAPqWRxmzrl2coefszuoWVIkm5k7avqT50ga7WnjIe%2FCH%2BwrGkkZ7jSpRYG7ounrRDa1HbAurwd2PmRsxFW6ODSYc23N7Vgv%2FCVqRN0KxMkixvw5jxZgbWkBRcwBoXeobPgBbH1Sc%2FzjmQKX8Q8a%2ByL3WP2KcSpYPoIagamCltC4WkMfkblynoo%2FTiO3TCJGMj9qbryKkGICYc8wbpu25dY4kuMr%2Bans8smJcLzpS8AY6nOrW%2Fg%2FlPWZswoWH9GemlaJTOllSedhjRWi%2F%2BoBsLwgWmaDGqTz99qGG9BQUkGIgbROcquXjfWiEgFX34A2sN2DDyFwNn10dEgRabKcdD7enQKSSPkxKrp%2FLCB6n5xnSTeMeuu6R9TcxaNmgHqLSZWV%2FttaMUiE3K3RQQoaEi4B5EJSKQMkGacHB7vGYh%2Fjw8pJdim6BFvOAgaRKUK2MqPO7qDVxpML%2Bk97wGOqUB%2Bw32S1p4Ge4zuwPyo2iz%2FZ5EOqEC6KJkFQfd%2FwkFACnSrgpj2oLBlx4jmH3Mw5kDN8rUTHM1QMMdMqmfAzjETehp5enFmaVhKU8mIqFz0cdSewKa%2FkW5B25lbt9ckSn8sQ9FJLbQ0MeItzb1k5BWKOclDFC5s1eyrZ9S7HA3o6w0tq5NDJpgt6K3xPBDd%2BuLQLDaWPvh9O9Gav5sUeu7%2FXv9V9uR&X-Amz-Signature=38a7977aacd33171945ee7401600e7544ea4754a500c2654ae118eda3f458f33&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQ5R6HQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHr%2BIqRxamM8WRzbVZLurZgbBZXXYLeNpJmcFVI1o3mwAiEAtx8lPb%2BeyYYHD%2FlKpg4e3anAR6chyUv%2BjcB2NYWxk9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEj4UJtr5lX8jLyfGSrcA9iYp1nMpjz1YBbxozSN8U4jwI3kqkSZWNwmXMOEv9gizwhcaRKp2BowXCJaVZ6dDAHpsjKq0fz66KTzc837K4E3oMumeymOCfkz%2FZy%2FsQi79DptSDV%2BcBXpdYvMzYvsgFbPFuY%2Biy9E%2Br7vD6m3Aid6BPgqwDz6%2BbhtFppHr7ZmF%2FEQnQYAPqWRxmzrl2coefszuoWVIkm5k7avqT50ga7WnjIe%2FCH%2BwrGkkZ7jSpRYG7ounrRDa1HbAurwd2PmRsxFW6ODSYc23N7Vgv%2FCVqRN0KxMkixvw5jxZgbWkBRcwBoXeobPgBbH1Sc%2FzjmQKX8Q8a%2ByL3WP2KcSpYPoIagamCltC4WkMfkblynoo%2FTiO3TCJGMj9qbryKkGICYc8wbpu25dY4kuMr%2Bans8smJcLzpS8AY6nOrW%2Fg%2FlPWZswoWH9GemlaJTOllSedhjRWi%2F%2BoBsLwgWmaDGqTz99qGG9BQUkGIgbROcquXjfWiEgFX34A2sN2DDyFwNn10dEgRabKcdD7enQKSSPkxKrp%2FLCB6n5xnSTeMeuu6R9TcxaNmgHqLSZWV%2FttaMUiE3K3RQQoaEi4B5EJSKQMkGacHB7vGYh%2Fjw8pJdim6BFvOAgaRKUK2MqPO7qDVxpML%2Bk97wGOqUB%2Bw32S1p4Ge4zuwPyo2iz%2FZ5EOqEC6KJkFQfd%2FwkFACnSrgpj2oLBlx4jmH3Mw5kDN8rUTHM1QMMdMqmfAzjETehp5enFmaVhKU8mIqFz0cdSewKa%2FkW5B25lbt9ckSn8sQ9FJLbQ0MeItzb1k5BWKOclDFC5s1eyrZ9S7HA3o6w0tq5NDJpgt6K3xPBDd%2BuLQLDaWPvh9O9Gav5sUeu7%2FXv9V9uR&X-Amz-Signature=ddad774788b0348addecd26df7dfee17f64a991430d78003b71ca73cecc73e8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQ5R6HQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHr%2BIqRxamM8WRzbVZLurZgbBZXXYLeNpJmcFVI1o3mwAiEAtx8lPb%2BeyYYHD%2FlKpg4e3anAR6chyUv%2BjcB2NYWxk9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEj4UJtr5lX8jLyfGSrcA9iYp1nMpjz1YBbxozSN8U4jwI3kqkSZWNwmXMOEv9gizwhcaRKp2BowXCJaVZ6dDAHpsjKq0fz66KTzc837K4E3oMumeymOCfkz%2FZy%2FsQi79DptSDV%2BcBXpdYvMzYvsgFbPFuY%2Biy9E%2Br7vD6m3Aid6BPgqwDz6%2BbhtFppHr7ZmF%2FEQnQYAPqWRxmzrl2coefszuoWVIkm5k7avqT50ga7WnjIe%2FCH%2BwrGkkZ7jSpRYG7ounrRDa1HbAurwd2PmRsxFW6ODSYc23N7Vgv%2FCVqRN0KxMkixvw5jxZgbWkBRcwBoXeobPgBbH1Sc%2FzjmQKX8Q8a%2ByL3WP2KcSpYPoIagamCltC4WkMfkblynoo%2FTiO3TCJGMj9qbryKkGICYc8wbpu25dY4kuMr%2Bans8smJcLzpS8AY6nOrW%2Fg%2FlPWZswoWH9GemlaJTOllSedhjRWi%2F%2BoBsLwgWmaDGqTz99qGG9BQUkGIgbROcquXjfWiEgFX34A2sN2DDyFwNn10dEgRabKcdD7enQKSSPkxKrp%2FLCB6n5xnSTeMeuu6R9TcxaNmgHqLSZWV%2FttaMUiE3K3RQQoaEi4B5EJSKQMkGacHB7vGYh%2Fjw8pJdim6BFvOAgaRKUK2MqPO7qDVxpML%2Bk97wGOqUB%2Bw32S1p4Ge4zuwPyo2iz%2FZ5EOqEC6KJkFQfd%2FwkFACnSrgpj2oLBlx4jmH3Mw5kDN8rUTHM1QMMdMqmfAzjETehp5enFmaVhKU8mIqFz0cdSewKa%2FkW5B25lbt9ckSn8sQ9FJLbQ0MeItzb1k5BWKOclDFC5s1eyrZ9S7HA3o6w0tq5NDJpgt6K3xPBDd%2BuLQLDaWPvh9O9Gav5sUeu7%2FXv9V9uR&X-Amz-Signature=ee04014aff31ccf1022e370d3ebb5140889cef2dac346d1e4e6f5006c5c3a6a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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


