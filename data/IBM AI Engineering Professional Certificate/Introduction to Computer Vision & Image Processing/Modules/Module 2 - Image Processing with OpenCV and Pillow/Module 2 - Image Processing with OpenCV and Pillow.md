

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVPRW3SU%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDvQppcOkudycBrn0Npl9M1xcQcNk5NOW%2Fwj%2BsROefWjAIgKns%2BEUIWBeRPd4dT%2BOb5nue81ytDDWLEn%2FcBHGgN3esq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDHsdKSrsEsObvMNQOSrcA41iPQg%2B1O1v9qCUvMVCOz0UBODWVhBoD1SzDjGDaBrOAZUlkU3Tc5Ohxor16W0Rzd6rcFcKzmllfRFyDs13cnR8GpuXIi3gEcHwwNtB%2FgnKJHU6tLdRIrnudDH8gBsXkwFFgUuZ02bjuxGStPsHoAhQ1o1OXZ2WCrTfOMSe%2FzwUu6Ays1yfEYpDTTF%2FVRXlMcHDr%2BPqC%2F4bsIcVxQtNzapwMH38chVkIc8VclTiqK2WiScyNBIXxIwSfED6iRaWnEcfjwz15LysXvB7WLVRcpcqD457KC51cvn9QPsYktQj40VkFZUMMGaBfZ3Ab0rAHWydvBR%2BSwFB762Wh9GIXnNY5skrCfHXSh1vO7MvY79kFgkw1SKYJO7bJNI8JxOybvie8anb1hnWYZk2lZ9W%2BvWyJuC%2FCElnxXvyOUhGdE31FU0r3sw9exPCiWmKjGEqu0Ih7i9DmyvnJmXu2tM9HMI4sBr5Hrq%2FFMfSaNBSDgqVjW4JmnqAK4NtgXPoUfiP16hpRXB7qa%2BJrx4%2FVC%2FPEASSo%2BLFTBHxFtT8l2iYcZGl6gIrsF%2BOyydlITbhFcD9B%2B3yItbTOe7LXG83LJNqVJOZeL%2FUL4R%2F500s3ueyLocgdn2YT2zi2LQ6E%2FbYMOTkxL0GOqUBQOY%2Fgdu8IzII9PJRxAd5iYqFVS5Iil0QP%2FLaFI7u0FVAFKHyLe0yXu7JKy37TMTqYZu8ptx8r4QhS2gg8%2FN7V2%2BTblDXRMFUq5UZXB63wad1V73otmSp%2BUXPfKuoh%2F2DTzDZdJg%2FNdll9LfM%2BPs46l3LNrQudta0Xuo7TtBUf8O7Mj8zhqBkZCOWIfc0GLkR%2FiGKqwzWOV5UXHOavqN1DIP34O3s&X-Amz-Signature=640753909fe299870588343ea909e571eceeb0598a10b583ebbcf4212de0c9a7&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYDH4ITM%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCjGuZ%2B94h3YKAKa04RTEFZ2Mf4Am8vMzhjnPAxpg8rMQIhAIUSP8P9GN1DVbJ9cKcs6e4VAxmRiQKRy%2FiV57x1vF%2FKKv8DCFIQABoMNjM3NDIzMTgzODA1IgxtrZ3nLJH26dDrg%2Fcq3APVg%2FbOMHXQaYjeoCtJR6c70b6dAMS6hAAO4Y1MrPATlunDd%2Bn%2B23L0daljLrumOweBH10dFN0teMJmz%2FzHjBHBb4mmSs0R9GuxE%2BsD4%2BXL4tZn9nof8cNFmQGzCzttBzuKSiJJfMT%2BwKpbKxu0jckdihoLgWjge%2B3XwFOGCfYN1A2ymYuRevMNxXHt%2FXbYPJ1soT8eHYxtiou8E%2FUJishm2y2DSZ5DdyfJ2dYSmnYWnc7JDU71HlywTpjvSC1oMK7aLZ98hwda9FQJ%2BEXuDRWatEA7Wlw8%2FT4%2BW0tCqPdBtTAatc6%2FC7tLK%2BYZvIJLmXmWqBT%2FbCGSXnzHNt3XZI1LTVtJnLrrqYNDZqogfsZ7f3XkBw1kPiGriJ1tTyv8JC8qbvqalnJRJmfoq032TRRj%2BfEiOQ83Nj0yxc78AXD%2FGx2RpyflQRKnQVcMPR2I19iRAJiDyUXW6FJKZtIJKhBHJ2qW0jPiJJriHrzRjqZShD%2BGZGo7jaujEDCJc%2FOAy3jY2IrqqMaVqANGco5hAgZZVYKimcMQmABPGl2W%2BBHzdPAX%2BeQONf0WJg4%2BjdsCsMTW2EhIJ1a4TLH3uhU7qqVo4%2FvWJDMUxuY58HTzTM9mUGnoKbL1iwUQ4tcSsjDB5MS9BjqkAUOYr3PjCGL89Yz2Cf%2B%2F9FaqwKBGcEarYWHHyrIn0tDTSvxVfvjajDrXueuaZEZr4dagINYk0%2BjaaCGQvDxJ%2F91YLnJ%2Bnn9c3i3mm%2BIpCz1VpdcbIplYqKdN5U5LUKl54Je7DcvfxoqmgK9WhnHl8Z85%2BCFy6OUICRDYIrWD3YpbkAxWzkTNC4xz9i98wCv7BfrrU9ooeTrXz7tnEXhYPs3b6YN2&X-Amz-Signature=5a20eb950d41e899c4d25f8b446e6b3247892d99285d34f53684bde01f083984&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYDH4ITM%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCjGuZ%2B94h3YKAKa04RTEFZ2Mf4Am8vMzhjnPAxpg8rMQIhAIUSP8P9GN1DVbJ9cKcs6e4VAxmRiQKRy%2FiV57x1vF%2FKKv8DCFIQABoMNjM3NDIzMTgzODA1IgxtrZ3nLJH26dDrg%2Fcq3APVg%2FbOMHXQaYjeoCtJR6c70b6dAMS6hAAO4Y1MrPATlunDd%2Bn%2B23L0daljLrumOweBH10dFN0teMJmz%2FzHjBHBb4mmSs0R9GuxE%2BsD4%2BXL4tZn9nof8cNFmQGzCzttBzuKSiJJfMT%2BwKpbKxu0jckdihoLgWjge%2B3XwFOGCfYN1A2ymYuRevMNxXHt%2FXbYPJ1soT8eHYxtiou8E%2FUJishm2y2DSZ5DdyfJ2dYSmnYWnc7JDU71HlywTpjvSC1oMK7aLZ98hwda9FQJ%2BEXuDRWatEA7Wlw8%2FT4%2BW0tCqPdBtTAatc6%2FC7tLK%2BYZvIJLmXmWqBT%2FbCGSXnzHNt3XZI1LTVtJnLrrqYNDZqogfsZ7f3XkBw1kPiGriJ1tTyv8JC8qbvqalnJRJmfoq032TRRj%2BfEiOQ83Nj0yxc78AXD%2FGx2RpyflQRKnQVcMPR2I19iRAJiDyUXW6FJKZtIJKhBHJ2qW0jPiJJriHrzRjqZShD%2BGZGo7jaujEDCJc%2FOAy3jY2IrqqMaVqANGco5hAgZZVYKimcMQmABPGl2W%2BBHzdPAX%2BeQONf0WJg4%2BjdsCsMTW2EhIJ1a4TLH3uhU7qqVo4%2FvWJDMUxuY58HTzTM9mUGnoKbL1iwUQ4tcSsjDB5MS9BjqkAUOYr3PjCGL89Yz2Cf%2B%2F9FaqwKBGcEarYWHHyrIn0tDTSvxVfvjajDrXueuaZEZr4dagINYk0%2BjaaCGQvDxJ%2F91YLnJ%2Bnn9c3i3mm%2BIpCz1VpdcbIplYqKdN5U5LUKl54Je7DcvfxoqmgK9WhnHl8Z85%2BCFy6OUICRDYIrWD3YpbkAxWzkTNC4xz9i98wCv7BfrrU9ooeTrXz7tnEXhYPs3b6YN2&X-Amz-Signature=102d504470a08bfa533683eab27dc9f9cdeeda4f3cad87b28b544c974420abb0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYDH4ITM%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCjGuZ%2B94h3YKAKa04RTEFZ2Mf4Am8vMzhjnPAxpg8rMQIhAIUSP8P9GN1DVbJ9cKcs6e4VAxmRiQKRy%2FiV57x1vF%2FKKv8DCFIQABoMNjM3NDIzMTgzODA1IgxtrZ3nLJH26dDrg%2Fcq3APVg%2FbOMHXQaYjeoCtJR6c70b6dAMS6hAAO4Y1MrPATlunDd%2Bn%2B23L0daljLrumOweBH10dFN0teMJmz%2FzHjBHBb4mmSs0R9GuxE%2BsD4%2BXL4tZn9nof8cNFmQGzCzttBzuKSiJJfMT%2BwKpbKxu0jckdihoLgWjge%2B3XwFOGCfYN1A2ymYuRevMNxXHt%2FXbYPJ1soT8eHYxtiou8E%2FUJishm2y2DSZ5DdyfJ2dYSmnYWnc7JDU71HlywTpjvSC1oMK7aLZ98hwda9FQJ%2BEXuDRWatEA7Wlw8%2FT4%2BW0tCqPdBtTAatc6%2FC7tLK%2BYZvIJLmXmWqBT%2FbCGSXnzHNt3XZI1LTVtJnLrrqYNDZqogfsZ7f3XkBw1kPiGriJ1tTyv8JC8qbvqalnJRJmfoq032TRRj%2BfEiOQ83Nj0yxc78AXD%2FGx2RpyflQRKnQVcMPR2I19iRAJiDyUXW6FJKZtIJKhBHJ2qW0jPiJJriHrzRjqZShD%2BGZGo7jaujEDCJc%2FOAy3jY2IrqqMaVqANGco5hAgZZVYKimcMQmABPGl2W%2BBHzdPAX%2BeQONf0WJg4%2BjdsCsMTW2EhIJ1a4TLH3uhU7qqVo4%2FvWJDMUxuY58HTzTM9mUGnoKbL1iwUQ4tcSsjDB5MS9BjqkAUOYr3PjCGL89Yz2Cf%2B%2F9FaqwKBGcEarYWHHyrIn0tDTSvxVfvjajDrXueuaZEZr4dagINYk0%2BjaaCGQvDxJ%2F91YLnJ%2Bnn9c3i3mm%2BIpCz1VpdcbIplYqKdN5U5LUKl54Je7DcvfxoqmgK9WhnHl8Z85%2BCFy6OUICRDYIrWD3YpbkAxWzkTNC4xz9i98wCv7BfrrU9ooeTrXz7tnEXhYPs3b6YN2&X-Amz-Signature=03f66a9449333da825fc621514bcc36e724483e40f131fe29a3e02b1812b5598&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYDH4ITM%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCjGuZ%2B94h3YKAKa04RTEFZ2Mf4Am8vMzhjnPAxpg8rMQIhAIUSP8P9GN1DVbJ9cKcs6e4VAxmRiQKRy%2FiV57x1vF%2FKKv8DCFIQABoMNjM3NDIzMTgzODA1IgxtrZ3nLJH26dDrg%2Fcq3APVg%2FbOMHXQaYjeoCtJR6c70b6dAMS6hAAO4Y1MrPATlunDd%2Bn%2B23L0daljLrumOweBH10dFN0teMJmz%2FzHjBHBb4mmSs0R9GuxE%2BsD4%2BXL4tZn9nof8cNFmQGzCzttBzuKSiJJfMT%2BwKpbKxu0jckdihoLgWjge%2B3XwFOGCfYN1A2ymYuRevMNxXHt%2FXbYPJ1soT8eHYxtiou8E%2FUJishm2y2DSZ5DdyfJ2dYSmnYWnc7JDU71HlywTpjvSC1oMK7aLZ98hwda9FQJ%2BEXuDRWatEA7Wlw8%2FT4%2BW0tCqPdBtTAatc6%2FC7tLK%2BYZvIJLmXmWqBT%2FbCGSXnzHNt3XZI1LTVtJnLrrqYNDZqogfsZ7f3XkBw1kPiGriJ1tTyv8JC8qbvqalnJRJmfoq032TRRj%2BfEiOQ83Nj0yxc78AXD%2FGx2RpyflQRKnQVcMPR2I19iRAJiDyUXW6FJKZtIJKhBHJ2qW0jPiJJriHrzRjqZShD%2BGZGo7jaujEDCJc%2FOAy3jY2IrqqMaVqANGco5hAgZZVYKimcMQmABPGl2W%2BBHzdPAX%2BeQONf0WJg4%2BjdsCsMTW2EhIJ1a4TLH3uhU7qqVo4%2FvWJDMUxuY58HTzTM9mUGnoKbL1iwUQ4tcSsjDB5MS9BjqkAUOYr3PjCGL89Yz2Cf%2B%2F9FaqwKBGcEarYWHHyrIn0tDTSvxVfvjajDrXueuaZEZr4dagINYk0%2BjaaCGQvDxJ%2F91YLnJ%2Bnn9c3i3mm%2BIpCz1VpdcbIplYqKdN5U5LUKl54Je7DcvfxoqmgK9WhnHl8Z85%2BCFy6OUICRDYIrWD3YpbkAxWzkTNC4xz9i98wCv7BfrrU9ooeTrXz7tnEXhYPs3b6YN2&X-Amz-Signature=1f7f42db3e2811e1f8a626cf3db68d5348274a6bc213a3aaf630035e1cc6cd78&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYDH4ITM%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCjGuZ%2B94h3YKAKa04RTEFZ2Mf4Am8vMzhjnPAxpg8rMQIhAIUSP8P9GN1DVbJ9cKcs6e4VAxmRiQKRy%2FiV57x1vF%2FKKv8DCFIQABoMNjM3NDIzMTgzODA1IgxtrZ3nLJH26dDrg%2Fcq3APVg%2FbOMHXQaYjeoCtJR6c70b6dAMS6hAAO4Y1MrPATlunDd%2Bn%2B23L0daljLrumOweBH10dFN0teMJmz%2FzHjBHBb4mmSs0R9GuxE%2BsD4%2BXL4tZn9nof8cNFmQGzCzttBzuKSiJJfMT%2BwKpbKxu0jckdihoLgWjge%2B3XwFOGCfYN1A2ymYuRevMNxXHt%2FXbYPJ1soT8eHYxtiou8E%2FUJishm2y2DSZ5DdyfJ2dYSmnYWnc7JDU71HlywTpjvSC1oMK7aLZ98hwda9FQJ%2BEXuDRWatEA7Wlw8%2FT4%2BW0tCqPdBtTAatc6%2FC7tLK%2BYZvIJLmXmWqBT%2FbCGSXnzHNt3XZI1LTVtJnLrrqYNDZqogfsZ7f3XkBw1kPiGriJ1tTyv8JC8qbvqalnJRJmfoq032TRRj%2BfEiOQ83Nj0yxc78AXD%2FGx2RpyflQRKnQVcMPR2I19iRAJiDyUXW6FJKZtIJKhBHJ2qW0jPiJJriHrzRjqZShD%2BGZGo7jaujEDCJc%2FOAy3jY2IrqqMaVqANGco5hAgZZVYKimcMQmABPGl2W%2BBHzdPAX%2BeQONf0WJg4%2BjdsCsMTW2EhIJ1a4TLH3uhU7qqVo4%2FvWJDMUxuY58HTzTM9mUGnoKbL1iwUQ4tcSsjDB5MS9BjqkAUOYr3PjCGL89Yz2Cf%2B%2F9FaqwKBGcEarYWHHyrIn0tDTSvxVfvjajDrXueuaZEZr4dagINYk0%2BjaaCGQvDxJ%2F91YLnJ%2Bnn9c3i3mm%2BIpCz1VpdcbIplYqKdN5U5LUKl54Je7DcvfxoqmgK9WhnHl8Z85%2BCFy6OUICRDYIrWD3YpbkAxWzkTNC4xz9i98wCv7BfrrU9ooeTrXz7tnEXhYPs3b6YN2&X-Amz-Signature=37f403d3119c02b73ee12d90d95addc228365d6aa0ce7da4a6364919e67a5b73&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVPRW3SU%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDvQppcOkudycBrn0Npl9M1xcQcNk5NOW%2Fwj%2BsROefWjAIgKns%2BEUIWBeRPd4dT%2BOb5nue81ytDDWLEn%2FcBHGgN3esq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDHsdKSrsEsObvMNQOSrcA41iPQg%2B1O1v9qCUvMVCOz0UBODWVhBoD1SzDjGDaBrOAZUlkU3Tc5Ohxor16W0Rzd6rcFcKzmllfRFyDs13cnR8GpuXIi3gEcHwwNtB%2FgnKJHU6tLdRIrnudDH8gBsXkwFFgUuZ02bjuxGStPsHoAhQ1o1OXZ2WCrTfOMSe%2FzwUu6Ays1yfEYpDTTF%2FVRXlMcHDr%2BPqC%2F4bsIcVxQtNzapwMH38chVkIc8VclTiqK2WiScyNBIXxIwSfED6iRaWnEcfjwz15LysXvB7WLVRcpcqD457KC51cvn9QPsYktQj40VkFZUMMGaBfZ3Ab0rAHWydvBR%2BSwFB762Wh9GIXnNY5skrCfHXSh1vO7MvY79kFgkw1SKYJO7bJNI8JxOybvie8anb1hnWYZk2lZ9W%2BvWyJuC%2FCElnxXvyOUhGdE31FU0r3sw9exPCiWmKjGEqu0Ih7i9DmyvnJmXu2tM9HMI4sBr5Hrq%2FFMfSaNBSDgqVjW4JmnqAK4NtgXPoUfiP16hpRXB7qa%2BJrx4%2FVC%2FPEASSo%2BLFTBHxFtT8l2iYcZGl6gIrsF%2BOyydlITbhFcD9B%2B3yItbTOe7LXG83LJNqVJOZeL%2FUL4R%2F500s3ueyLocgdn2YT2zi2LQ6E%2FbYMOTkxL0GOqUBQOY%2Fgdu8IzII9PJRxAd5iYqFVS5Iil0QP%2FLaFI7u0FVAFKHyLe0yXu7JKy37TMTqYZu8ptx8r4QhS2gg8%2FN7V2%2BTblDXRMFUq5UZXB63wad1V73otmSp%2BUXPfKuoh%2F2DTzDZdJg%2FNdll9LfM%2BPs46l3LNrQudta0Xuo7TtBUf8O7Mj8zhqBkZCOWIfc0GLkR%2FiGKqwzWOV5UXHOavqN1DIP34O3s&X-Amz-Signature=03e27171b47b6402b9728fa60e1579964b1e48b29e553806670d65c4c9c31f39&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVPRW3SU%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDvQppcOkudycBrn0Npl9M1xcQcNk5NOW%2Fwj%2BsROefWjAIgKns%2BEUIWBeRPd4dT%2BOb5nue81ytDDWLEn%2FcBHGgN3esq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDHsdKSrsEsObvMNQOSrcA41iPQg%2B1O1v9qCUvMVCOz0UBODWVhBoD1SzDjGDaBrOAZUlkU3Tc5Ohxor16W0Rzd6rcFcKzmllfRFyDs13cnR8GpuXIi3gEcHwwNtB%2FgnKJHU6tLdRIrnudDH8gBsXkwFFgUuZ02bjuxGStPsHoAhQ1o1OXZ2WCrTfOMSe%2FzwUu6Ays1yfEYpDTTF%2FVRXlMcHDr%2BPqC%2F4bsIcVxQtNzapwMH38chVkIc8VclTiqK2WiScyNBIXxIwSfED6iRaWnEcfjwz15LysXvB7WLVRcpcqD457KC51cvn9QPsYktQj40VkFZUMMGaBfZ3Ab0rAHWydvBR%2BSwFB762Wh9GIXnNY5skrCfHXSh1vO7MvY79kFgkw1SKYJO7bJNI8JxOybvie8anb1hnWYZk2lZ9W%2BvWyJuC%2FCElnxXvyOUhGdE31FU0r3sw9exPCiWmKjGEqu0Ih7i9DmyvnJmXu2tM9HMI4sBr5Hrq%2FFMfSaNBSDgqVjW4JmnqAK4NtgXPoUfiP16hpRXB7qa%2BJrx4%2FVC%2FPEASSo%2BLFTBHxFtT8l2iYcZGl6gIrsF%2BOyydlITbhFcD9B%2B3yItbTOe7LXG83LJNqVJOZeL%2FUL4R%2F500s3ueyLocgdn2YT2zi2LQ6E%2FbYMOTkxL0GOqUBQOY%2Fgdu8IzII9PJRxAd5iYqFVS5Iil0QP%2FLaFI7u0FVAFKHyLe0yXu7JKy37TMTqYZu8ptx8r4QhS2gg8%2FN7V2%2BTblDXRMFUq5UZXB63wad1V73otmSp%2BUXPfKuoh%2F2DTzDZdJg%2FNdll9LfM%2BPs46l3LNrQudta0Xuo7TtBUf8O7Mj8zhqBkZCOWIfc0GLkR%2FiGKqwzWOV5UXHOavqN1DIP34O3s&X-Amz-Signature=e6dd8cf47a4b575b39cb42fc9d74d2fdcf690e4c6f1a3ffe9016b29b4ab3883f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVPRW3SU%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDvQppcOkudycBrn0Npl9M1xcQcNk5NOW%2Fwj%2BsROefWjAIgKns%2BEUIWBeRPd4dT%2BOb5nue81ytDDWLEn%2FcBHGgN3esq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDHsdKSrsEsObvMNQOSrcA41iPQg%2B1O1v9qCUvMVCOz0UBODWVhBoD1SzDjGDaBrOAZUlkU3Tc5Ohxor16W0Rzd6rcFcKzmllfRFyDs13cnR8GpuXIi3gEcHwwNtB%2FgnKJHU6tLdRIrnudDH8gBsXkwFFgUuZ02bjuxGStPsHoAhQ1o1OXZ2WCrTfOMSe%2FzwUu6Ays1yfEYpDTTF%2FVRXlMcHDr%2BPqC%2F4bsIcVxQtNzapwMH38chVkIc8VclTiqK2WiScyNBIXxIwSfED6iRaWnEcfjwz15LysXvB7WLVRcpcqD457KC51cvn9QPsYktQj40VkFZUMMGaBfZ3Ab0rAHWydvBR%2BSwFB762Wh9GIXnNY5skrCfHXSh1vO7MvY79kFgkw1SKYJO7bJNI8JxOybvie8anb1hnWYZk2lZ9W%2BvWyJuC%2FCElnxXvyOUhGdE31FU0r3sw9exPCiWmKjGEqu0Ih7i9DmyvnJmXu2tM9HMI4sBr5Hrq%2FFMfSaNBSDgqVjW4JmnqAK4NtgXPoUfiP16hpRXB7qa%2BJrx4%2FVC%2FPEASSo%2BLFTBHxFtT8l2iYcZGl6gIrsF%2BOyydlITbhFcD9B%2B3yItbTOe7LXG83LJNqVJOZeL%2FUL4R%2F500s3ueyLocgdn2YT2zi2LQ6E%2FbYMOTkxL0GOqUBQOY%2Fgdu8IzII9PJRxAd5iYqFVS5Iil0QP%2FLaFI7u0FVAFKHyLe0yXu7JKy37TMTqYZu8ptx8r4QhS2gg8%2FN7V2%2BTblDXRMFUq5UZXB63wad1V73otmSp%2BUXPfKuoh%2F2DTzDZdJg%2FNdll9LfM%2BPs46l3LNrQudta0Xuo7TtBUf8O7Mj8zhqBkZCOWIfc0GLkR%2FiGKqwzWOV5UXHOavqN1DIP34O3s&X-Amz-Signature=588604cb1ea65d6a67e64f84d9c71fb2e2566c447d052c70e0744abb46808d18&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVPRW3SU%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDvQppcOkudycBrn0Npl9M1xcQcNk5NOW%2Fwj%2BsROefWjAIgKns%2BEUIWBeRPd4dT%2BOb5nue81ytDDWLEn%2FcBHGgN3esq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDHsdKSrsEsObvMNQOSrcA41iPQg%2B1O1v9qCUvMVCOz0UBODWVhBoD1SzDjGDaBrOAZUlkU3Tc5Ohxor16W0Rzd6rcFcKzmllfRFyDs13cnR8GpuXIi3gEcHwwNtB%2FgnKJHU6tLdRIrnudDH8gBsXkwFFgUuZ02bjuxGStPsHoAhQ1o1OXZ2WCrTfOMSe%2FzwUu6Ays1yfEYpDTTF%2FVRXlMcHDr%2BPqC%2F4bsIcVxQtNzapwMH38chVkIc8VclTiqK2WiScyNBIXxIwSfED6iRaWnEcfjwz15LysXvB7WLVRcpcqD457KC51cvn9QPsYktQj40VkFZUMMGaBfZ3Ab0rAHWydvBR%2BSwFB762Wh9GIXnNY5skrCfHXSh1vO7MvY79kFgkw1SKYJO7bJNI8JxOybvie8anb1hnWYZk2lZ9W%2BvWyJuC%2FCElnxXvyOUhGdE31FU0r3sw9exPCiWmKjGEqu0Ih7i9DmyvnJmXu2tM9HMI4sBr5Hrq%2FFMfSaNBSDgqVjW4JmnqAK4NtgXPoUfiP16hpRXB7qa%2BJrx4%2FVC%2FPEASSo%2BLFTBHxFtT8l2iYcZGl6gIrsF%2BOyydlITbhFcD9B%2B3yItbTOe7LXG83LJNqVJOZeL%2FUL4R%2F500s3ueyLocgdn2YT2zi2LQ6E%2FbYMOTkxL0GOqUBQOY%2Fgdu8IzII9PJRxAd5iYqFVS5Iil0QP%2FLaFI7u0FVAFKHyLe0yXu7JKy37TMTqYZu8ptx8r4QhS2gg8%2FN7V2%2BTblDXRMFUq5UZXB63wad1V73otmSp%2BUXPfKuoh%2F2DTzDZdJg%2FNdll9LfM%2BPs46l3LNrQudta0Xuo7TtBUf8O7Mj8zhqBkZCOWIfc0GLkR%2FiGKqwzWOV5UXHOavqN1DIP34O3s&X-Amz-Signature=4cc6d50810106c5b6056cca2e1556cb5149ea96d946d2b857b8ee5066e5e7457&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVPRW3SU%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDvQppcOkudycBrn0Npl9M1xcQcNk5NOW%2Fwj%2BsROefWjAIgKns%2BEUIWBeRPd4dT%2BOb5nue81ytDDWLEn%2FcBHGgN3esq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDHsdKSrsEsObvMNQOSrcA41iPQg%2B1O1v9qCUvMVCOz0UBODWVhBoD1SzDjGDaBrOAZUlkU3Tc5Ohxor16W0Rzd6rcFcKzmllfRFyDs13cnR8GpuXIi3gEcHwwNtB%2FgnKJHU6tLdRIrnudDH8gBsXkwFFgUuZ02bjuxGStPsHoAhQ1o1OXZ2WCrTfOMSe%2FzwUu6Ays1yfEYpDTTF%2FVRXlMcHDr%2BPqC%2F4bsIcVxQtNzapwMH38chVkIc8VclTiqK2WiScyNBIXxIwSfED6iRaWnEcfjwz15LysXvB7WLVRcpcqD457KC51cvn9QPsYktQj40VkFZUMMGaBfZ3Ab0rAHWydvBR%2BSwFB762Wh9GIXnNY5skrCfHXSh1vO7MvY79kFgkw1SKYJO7bJNI8JxOybvie8anb1hnWYZk2lZ9W%2BvWyJuC%2FCElnxXvyOUhGdE31FU0r3sw9exPCiWmKjGEqu0Ih7i9DmyvnJmXu2tM9HMI4sBr5Hrq%2FFMfSaNBSDgqVjW4JmnqAK4NtgXPoUfiP16hpRXB7qa%2BJrx4%2FVC%2FPEASSo%2BLFTBHxFtT8l2iYcZGl6gIrsF%2BOyydlITbhFcD9B%2B3yItbTOe7LXG83LJNqVJOZeL%2FUL4R%2F500s3ueyLocgdn2YT2zi2LQ6E%2FbYMOTkxL0GOqUBQOY%2Fgdu8IzII9PJRxAd5iYqFVS5Iil0QP%2FLaFI7u0FVAFKHyLe0yXu7JKy37TMTqYZu8ptx8r4QhS2gg8%2FN7V2%2BTblDXRMFUq5UZXB63wad1V73otmSp%2BUXPfKuoh%2F2DTzDZdJg%2FNdll9LfM%2BPs46l3LNrQudta0Xuo7TtBUf8O7Mj8zhqBkZCOWIfc0GLkR%2FiGKqwzWOV5UXHOavqN1DIP34O3s&X-Amz-Signature=75096470763e566eac40e302c689d30a214a5411ba7668cba9d2729e06d37b95&X-Amz-SignedHeaders=host&x-id=GetObject)
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


