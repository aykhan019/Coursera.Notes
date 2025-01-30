

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAURQK25%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuvn8wOn7b83ZWyABXYVwyEImZ9NJ279AhZ%2F%2F8cXGXdAiBchxxzYO1a4hRodR5GNFZt5KHgrHG3Xu%2FZHSxUWopjRCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOLWMm09JiXAVI94sKtwDVQ3Y0Yd%2Fh3Ljp0uspbbxypJc69tIZhJOA0rFbjqBrlvm7H2VAq5JW5ROsQZ2E1jx1EfMs0eDtiAu5vYZkQKY0%2B57Xs18dmND9NRPquwQZhHmGVbfQhV4dVjVH7Bk3h16Bh%2Fjh5GIEsYvXAqeQfhkUsLUgL9rpkZkXZxuxsj1oHNSwijQIEVZ0m8749D0FARLl1L4ec3qGyL3v8f0K72mdVSA184EgGk8lmN6HYU2Xrv3OL%2F8lrMDMQkGHhPuyrxzz0m4dUDOTvDrxJJTUqAHDs0TP4TNDF%2BxCCCM9gfZ%2BeQacAoycCpWnSujPkawoi4KbiM5x8cKDbHCyu2OU2uK6TKAItaHYVRgGjjDGd51oL4KThfCfmWIAEKvVWVGr%2F1eZtzSTLWPTFbyNhnA8vr9mdkGcWf5hJoh7MqnAMcUgXZgpZh%2FSstM5LZBxHr%2B5WxH8JEhG6iaSOrHhrd3S47ULUqpwpPiTx%2BnFTGZDdUolESzzmMo7uvpovc%2FF4ZEb%2Fhs5UlYxUjHTiCOCsl6pHWL1B09mPaTX541P28GDHjbVCCsnHTKg8%2BPsYPk177Hqg8R3AuYH55YqQdC%2F0Y4EHhTYGIHyA5FTRWf4vLGE0gTQaKpzHG9uwtabElqH0ow2rHrvAY6pgGJ0DToRIZ84al3Kao%2Bq079K%2FVVYpIxCE3uCTZmF%2FmQ2FPdcOiIPY1f3zvtMcE5z19P2QHWNOZbZWX%2BN7KZpU%2BpxbSW7nac%2F9x4iVgnq0c2lLMHXoDC5JYnE7zXRrxYDJUsSQsvo%2B5kTGbeRZs0FW4q8CWOFKJrOdR10hpxn%2FitLU0CCjMuS3PjK0CLBfUzWrMXB419q%2BDQ7KawDjgfU6amhEP%2BvIQz&X-Amz-Signature=bde2f81ab3889ff04c32fc505ab62bcdbe61f30a8a268f71c0dde2762d4bdaf3&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EKCWNS5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEwaeu0PT0WXb%2F0ECbMoCtkxv8PGbbHoKL3HrmlVW1o2AiEAy9uHJNDsNVccQx%2FaVVn%2B0P2Wce4In0yT2jwO7BJYknYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFakl%2BjpYmPT0vVpvSrcA969Z933ng8q9EBoT%2BS5c%2Fqvy%2FfMR3TYuCbB13z%2BQLZsQr0hsMz22rfVMMYDi9Z5pL8X77oFRe1DQZsE8MuIPpBPDrZr2agLAeGublnd%2B%2BYXpijzBtKjtPH44OcUnvCdyKeDz6IUA96gJgKgcmItxktRkQ1skN%2FTmHgMBw20%2FFbaUq2wRuvQgIRXxiqA5OijZps8nFNAtJTnNl2teNHTiy4BaB%2F0YSILU8tPI2K2JuBs416CZEQnYGpbHD14n1qf4bOzZqtIsm6yiO18uitOQQ9j74XAjXiLHDH5vylrAXX2wmF%2Bte057D2NYTwnT1g7k3UlXmgNuV44qLvuucqHPQtryIigRDcmningFCq9Qp%2FMVw7e%2BtckUsFm9FdjOKElMd8Y6ffyzI1V4JjsTSA5t8IKD4Gy3gAKIqyncefKqFkHz5zkOjgM7Apsc%2BOx4ZgkeO0j4jML73AC5iQpO%2FGZqEACw4vMiykb1MwHMof7eqv0LnNucUMapECX020Vq7QKLkwDobpX3n0G2qj7rPAquqbImpvHayYGQ2hUaQQ2Sj8qoeoFThAp9T9sHp9zO2TTeDVDDWXjFE1g13L0mhhkkEXwupF5fGSeglrDjHZaDERcYTSWHWUvTAwh60JrMI6y67wGOqUBUxSHBkXlnzbirlXIkk1aEsMmDIJwbcF1vK2U1XpmFq7EKaVRz0y9o314tdvq8OYvat3WZuYwoyWWhq32E69fakkEcwJEBw%2BGQAoi9sJ08D86wwuRcE18IRIDF6b7NDZzp3o54QqNckLIxa7K%2BCzLOn3%2F0dwjWXRFhYUynanlwI0u9ec2UNbC8XBzLYfiYP%2BCLWwEY4vuL6Y2EDpXApFYHtjL73dm&X-Amz-Signature=171720330b4530c0be79c5564e7ae6148339cb5235175a1280230e486d176e60&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EKCWNS5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEwaeu0PT0WXb%2F0ECbMoCtkxv8PGbbHoKL3HrmlVW1o2AiEAy9uHJNDsNVccQx%2FaVVn%2B0P2Wce4In0yT2jwO7BJYknYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFakl%2BjpYmPT0vVpvSrcA969Z933ng8q9EBoT%2BS5c%2Fqvy%2FfMR3TYuCbB13z%2BQLZsQr0hsMz22rfVMMYDi9Z5pL8X77oFRe1DQZsE8MuIPpBPDrZr2agLAeGublnd%2B%2BYXpijzBtKjtPH44OcUnvCdyKeDz6IUA96gJgKgcmItxktRkQ1skN%2FTmHgMBw20%2FFbaUq2wRuvQgIRXxiqA5OijZps8nFNAtJTnNl2teNHTiy4BaB%2F0YSILU8tPI2K2JuBs416CZEQnYGpbHD14n1qf4bOzZqtIsm6yiO18uitOQQ9j74XAjXiLHDH5vylrAXX2wmF%2Bte057D2NYTwnT1g7k3UlXmgNuV44qLvuucqHPQtryIigRDcmningFCq9Qp%2FMVw7e%2BtckUsFm9FdjOKElMd8Y6ffyzI1V4JjsTSA5t8IKD4Gy3gAKIqyncefKqFkHz5zkOjgM7Apsc%2BOx4ZgkeO0j4jML73AC5iQpO%2FGZqEACw4vMiykb1MwHMof7eqv0LnNucUMapECX020Vq7QKLkwDobpX3n0G2qj7rPAquqbImpvHayYGQ2hUaQQ2Sj8qoeoFThAp9T9sHp9zO2TTeDVDDWXjFE1g13L0mhhkkEXwupF5fGSeglrDjHZaDERcYTSWHWUvTAwh60JrMI6y67wGOqUBUxSHBkXlnzbirlXIkk1aEsMmDIJwbcF1vK2U1XpmFq7EKaVRz0y9o314tdvq8OYvat3WZuYwoyWWhq32E69fakkEcwJEBw%2BGQAoi9sJ08D86wwuRcE18IRIDF6b7NDZzp3o54QqNckLIxa7K%2BCzLOn3%2F0dwjWXRFhYUynanlwI0u9ec2UNbC8XBzLYfiYP%2BCLWwEY4vuL6Y2EDpXApFYHtjL73dm&X-Amz-Signature=06f006d024221d5f77cfa22a2a8016c4ef8f9a768367ffa7c535dfcb236e64c9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EKCWNS5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEwaeu0PT0WXb%2F0ECbMoCtkxv8PGbbHoKL3HrmlVW1o2AiEAy9uHJNDsNVccQx%2FaVVn%2B0P2Wce4In0yT2jwO7BJYknYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFakl%2BjpYmPT0vVpvSrcA969Z933ng8q9EBoT%2BS5c%2Fqvy%2FfMR3TYuCbB13z%2BQLZsQr0hsMz22rfVMMYDi9Z5pL8X77oFRe1DQZsE8MuIPpBPDrZr2agLAeGublnd%2B%2BYXpijzBtKjtPH44OcUnvCdyKeDz6IUA96gJgKgcmItxktRkQ1skN%2FTmHgMBw20%2FFbaUq2wRuvQgIRXxiqA5OijZps8nFNAtJTnNl2teNHTiy4BaB%2F0YSILU8tPI2K2JuBs416CZEQnYGpbHD14n1qf4bOzZqtIsm6yiO18uitOQQ9j74XAjXiLHDH5vylrAXX2wmF%2Bte057D2NYTwnT1g7k3UlXmgNuV44qLvuucqHPQtryIigRDcmningFCq9Qp%2FMVw7e%2BtckUsFm9FdjOKElMd8Y6ffyzI1V4JjsTSA5t8IKD4Gy3gAKIqyncefKqFkHz5zkOjgM7Apsc%2BOx4ZgkeO0j4jML73AC5iQpO%2FGZqEACw4vMiykb1MwHMof7eqv0LnNucUMapECX020Vq7QKLkwDobpX3n0G2qj7rPAquqbImpvHayYGQ2hUaQQ2Sj8qoeoFThAp9T9sHp9zO2TTeDVDDWXjFE1g13L0mhhkkEXwupF5fGSeglrDjHZaDERcYTSWHWUvTAwh60JrMI6y67wGOqUBUxSHBkXlnzbirlXIkk1aEsMmDIJwbcF1vK2U1XpmFq7EKaVRz0y9o314tdvq8OYvat3WZuYwoyWWhq32E69fakkEcwJEBw%2BGQAoi9sJ08D86wwuRcE18IRIDF6b7NDZzp3o54QqNckLIxa7K%2BCzLOn3%2F0dwjWXRFhYUynanlwI0u9ec2UNbC8XBzLYfiYP%2BCLWwEY4vuL6Y2EDpXApFYHtjL73dm&X-Amz-Signature=7e4895c3823180e7843346d30101635713d977297a151b61bc109b385058a471&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EKCWNS5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEwaeu0PT0WXb%2F0ECbMoCtkxv8PGbbHoKL3HrmlVW1o2AiEAy9uHJNDsNVccQx%2FaVVn%2B0P2Wce4In0yT2jwO7BJYknYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFakl%2BjpYmPT0vVpvSrcA969Z933ng8q9EBoT%2BS5c%2Fqvy%2FfMR3TYuCbB13z%2BQLZsQr0hsMz22rfVMMYDi9Z5pL8X77oFRe1DQZsE8MuIPpBPDrZr2agLAeGublnd%2B%2BYXpijzBtKjtPH44OcUnvCdyKeDz6IUA96gJgKgcmItxktRkQ1skN%2FTmHgMBw20%2FFbaUq2wRuvQgIRXxiqA5OijZps8nFNAtJTnNl2teNHTiy4BaB%2F0YSILU8tPI2K2JuBs416CZEQnYGpbHD14n1qf4bOzZqtIsm6yiO18uitOQQ9j74XAjXiLHDH5vylrAXX2wmF%2Bte057D2NYTwnT1g7k3UlXmgNuV44qLvuucqHPQtryIigRDcmningFCq9Qp%2FMVw7e%2BtckUsFm9FdjOKElMd8Y6ffyzI1V4JjsTSA5t8IKD4Gy3gAKIqyncefKqFkHz5zkOjgM7Apsc%2BOx4ZgkeO0j4jML73AC5iQpO%2FGZqEACw4vMiykb1MwHMof7eqv0LnNucUMapECX020Vq7QKLkwDobpX3n0G2qj7rPAquqbImpvHayYGQ2hUaQQ2Sj8qoeoFThAp9T9sHp9zO2TTeDVDDWXjFE1g13L0mhhkkEXwupF5fGSeglrDjHZaDERcYTSWHWUvTAwh60JrMI6y67wGOqUBUxSHBkXlnzbirlXIkk1aEsMmDIJwbcF1vK2U1XpmFq7EKaVRz0y9o314tdvq8OYvat3WZuYwoyWWhq32E69fakkEcwJEBw%2BGQAoi9sJ08D86wwuRcE18IRIDF6b7NDZzp3o54QqNckLIxa7K%2BCzLOn3%2F0dwjWXRFhYUynanlwI0u9ec2UNbC8XBzLYfiYP%2BCLWwEY4vuL6Y2EDpXApFYHtjL73dm&X-Amz-Signature=2f18bfe826966b2ab1aad75eb39cf861b9fdaab32b9438cce713d8e02305e0f8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EKCWNS5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEwaeu0PT0WXb%2F0ECbMoCtkxv8PGbbHoKL3HrmlVW1o2AiEAy9uHJNDsNVccQx%2FaVVn%2B0P2Wce4In0yT2jwO7BJYknYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFakl%2BjpYmPT0vVpvSrcA969Z933ng8q9EBoT%2BS5c%2Fqvy%2FfMR3TYuCbB13z%2BQLZsQr0hsMz22rfVMMYDi9Z5pL8X77oFRe1DQZsE8MuIPpBPDrZr2agLAeGublnd%2B%2BYXpijzBtKjtPH44OcUnvCdyKeDz6IUA96gJgKgcmItxktRkQ1skN%2FTmHgMBw20%2FFbaUq2wRuvQgIRXxiqA5OijZps8nFNAtJTnNl2teNHTiy4BaB%2F0YSILU8tPI2K2JuBs416CZEQnYGpbHD14n1qf4bOzZqtIsm6yiO18uitOQQ9j74XAjXiLHDH5vylrAXX2wmF%2Bte057D2NYTwnT1g7k3UlXmgNuV44qLvuucqHPQtryIigRDcmningFCq9Qp%2FMVw7e%2BtckUsFm9FdjOKElMd8Y6ffyzI1V4JjsTSA5t8IKD4Gy3gAKIqyncefKqFkHz5zkOjgM7Apsc%2BOx4ZgkeO0j4jML73AC5iQpO%2FGZqEACw4vMiykb1MwHMof7eqv0LnNucUMapECX020Vq7QKLkwDobpX3n0G2qj7rPAquqbImpvHayYGQ2hUaQQ2Sj8qoeoFThAp9T9sHp9zO2TTeDVDDWXjFE1g13L0mhhkkEXwupF5fGSeglrDjHZaDERcYTSWHWUvTAwh60JrMI6y67wGOqUBUxSHBkXlnzbirlXIkk1aEsMmDIJwbcF1vK2U1XpmFq7EKaVRz0y9o314tdvq8OYvat3WZuYwoyWWhq32E69fakkEcwJEBw%2BGQAoi9sJ08D86wwuRcE18IRIDF6b7NDZzp3o54QqNckLIxa7K%2BCzLOn3%2F0dwjWXRFhYUynanlwI0u9ec2UNbC8XBzLYfiYP%2BCLWwEY4vuL6Y2EDpXApFYHtjL73dm&X-Amz-Signature=d102eaf72757223ac496d9f67a56b00f124e7ae771227dba009ca37dfc0d7718&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAURQK25%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuvn8wOn7b83ZWyABXYVwyEImZ9NJ279AhZ%2F%2F8cXGXdAiBchxxzYO1a4hRodR5GNFZt5KHgrHG3Xu%2FZHSxUWopjRCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOLWMm09JiXAVI94sKtwDVQ3Y0Yd%2Fh3Ljp0uspbbxypJc69tIZhJOA0rFbjqBrlvm7H2VAq5JW5ROsQZ2E1jx1EfMs0eDtiAu5vYZkQKY0%2B57Xs18dmND9NRPquwQZhHmGVbfQhV4dVjVH7Bk3h16Bh%2Fjh5GIEsYvXAqeQfhkUsLUgL9rpkZkXZxuxsj1oHNSwijQIEVZ0m8749D0FARLl1L4ec3qGyL3v8f0K72mdVSA184EgGk8lmN6HYU2Xrv3OL%2F8lrMDMQkGHhPuyrxzz0m4dUDOTvDrxJJTUqAHDs0TP4TNDF%2BxCCCM9gfZ%2BeQacAoycCpWnSujPkawoi4KbiM5x8cKDbHCyu2OU2uK6TKAItaHYVRgGjjDGd51oL4KThfCfmWIAEKvVWVGr%2F1eZtzSTLWPTFbyNhnA8vr9mdkGcWf5hJoh7MqnAMcUgXZgpZh%2FSstM5LZBxHr%2B5WxH8JEhG6iaSOrHhrd3S47ULUqpwpPiTx%2BnFTGZDdUolESzzmMo7uvpovc%2FF4ZEb%2Fhs5UlYxUjHTiCOCsl6pHWL1B09mPaTX541P28GDHjbVCCsnHTKg8%2BPsYPk177Hqg8R3AuYH55YqQdC%2F0Y4EHhTYGIHyA5FTRWf4vLGE0gTQaKpzHG9uwtabElqH0ow2rHrvAY6pgGJ0DToRIZ84al3Kao%2Bq079K%2FVVYpIxCE3uCTZmF%2FmQ2FPdcOiIPY1f3zvtMcE5z19P2QHWNOZbZWX%2BN7KZpU%2BpxbSW7nac%2F9x4iVgnq0c2lLMHXoDC5JYnE7zXRrxYDJUsSQsvo%2B5kTGbeRZs0FW4q8CWOFKJrOdR10hpxn%2FitLU0CCjMuS3PjK0CLBfUzWrMXB419q%2BDQ7KawDjgfU6amhEP%2BvIQz&X-Amz-Signature=345f21fd7b0215662a8fa93ad5842829c711b4c1595ec633f4bf44f5d48e1a95&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAURQK25%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuvn8wOn7b83ZWyABXYVwyEImZ9NJ279AhZ%2F%2F8cXGXdAiBchxxzYO1a4hRodR5GNFZt5KHgrHG3Xu%2FZHSxUWopjRCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOLWMm09JiXAVI94sKtwDVQ3Y0Yd%2Fh3Ljp0uspbbxypJc69tIZhJOA0rFbjqBrlvm7H2VAq5JW5ROsQZ2E1jx1EfMs0eDtiAu5vYZkQKY0%2B57Xs18dmND9NRPquwQZhHmGVbfQhV4dVjVH7Bk3h16Bh%2Fjh5GIEsYvXAqeQfhkUsLUgL9rpkZkXZxuxsj1oHNSwijQIEVZ0m8749D0FARLl1L4ec3qGyL3v8f0K72mdVSA184EgGk8lmN6HYU2Xrv3OL%2F8lrMDMQkGHhPuyrxzz0m4dUDOTvDrxJJTUqAHDs0TP4TNDF%2BxCCCM9gfZ%2BeQacAoycCpWnSujPkawoi4KbiM5x8cKDbHCyu2OU2uK6TKAItaHYVRgGjjDGd51oL4KThfCfmWIAEKvVWVGr%2F1eZtzSTLWPTFbyNhnA8vr9mdkGcWf5hJoh7MqnAMcUgXZgpZh%2FSstM5LZBxHr%2B5WxH8JEhG6iaSOrHhrd3S47ULUqpwpPiTx%2BnFTGZDdUolESzzmMo7uvpovc%2FF4ZEb%2Fhs5UlYxUjHTiCOCsl6pHWL1B09mPaTX541P28GDHjbVCCsnHTKg8%2BPsYPk177Hqg8R3AuYH55YqQdC%2F0Y4EHhTYGIHyA5FTRWf4vLGE0gTQaKpzHG9uwtabElqH0ow2rHrvAY6pgGJ0DToRIZ84al3Kao%2Bq079K%2FVVYpIxCE3uCTZmF%2FmQ2FPdcOiIPY1f3zvtMcE5z19P2QHWNOZbZWX%2BN7KZpU%2BpxbSW7nac%2F9x4iVgnq0c2lLMHXoDC5JYnE7zXRrxYDJUsSQsvo%2B5kTGbeRZs0FW4q8CWOFKJrOdR10hpxn%2FitLU0CCjMuS3PjK0CLBfUzWrMXB419q%2BDQ7KawDjgfU6amhEP%2BvIQz&X-Amz-Signature=c7d0e2f9c9e2cd5d11f0277d6058e715d45b57ce89043aaea22a9a12483fef82&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAURQK25%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuvn8wOn7b83ZWyABXYVwyEImZ9NJ279AhZ%2F%2F8cXGXdAiBchxxzYO1a4hRodR5GNFZt5KHgrHG3Xu%2FZHSxUWopjRCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOLWMm09JiXAVI94sKtwDVQ3Y0Yd%2Fh3Ljp0uspbbxypJc69tIZhJOA0rFbjqBrlvm7H2VAq5JW5ROsQZ2E1jx1EfMs0eDtiAu5vYZkQKY0%2B57Xs18dmND9NRPquwQZhHmGVbfQhV4dVjVH7Bk3h16Bh%2Fjh5GIEsYvXAqeQfhkUsLUgL9rpkZkXZxuxsj1oHNSwijQIEVZ0m8749D0FARLl1L4ec3qGyL3v8f0K72mdVSA184EgGk8lmN6HYU2Xrv3OL%2F8lrMDMQkGHhPuyrxzz0m4dUDOTvDrxJJTUqAHDs0TP4TNDF%2BxCCCM9gfZ%2BeQacAoycCpWnSujPkawoi4KbiM5x8cKDbHCyu2OU2uK6TKAItaHYVRgGjjDGd51oL4KThfCfmWIAEKvVWVGr%2F1eZtzSTLWPTFbyNhnA8vr9mdkGcWf5hJoh7MqnAMcUgXZgpZh%2FSstM5LZBxHr%2B5WxH8JEhG6iaSOrHhrd3S47ULUqpwpPiTx%2BnFTGZDdUolESzzmMo7uvpovc%2FF4ZEb%2Fhs5UlYxUjHTiCOCsl6pHWL1B09mPaTX541P28GDHjbVCCsnHTKg8%2BPsYPk177Hqg8R3AuYH55YqQdC%2F0Y4EHhTYGIHyA5FTRWf4vLGE0gTQaKpzHG9uwtabElqH0ow2rHrvAY6pgGJ0DToRIZ84al3Kao%2Bq079K%2FVVYpIxCE3uCTZmF%2FmQ2FPdcOiIPY1f3zvtMcE5z19P2QHWNOZbZWX%2BN7KZpU%2BpxbSW7nac%2F9x4iVgnq0c2lLMHXoDC5JYnE7zXRrxYDJUsSQsvo%2B5kTGbeRZs0FW4q8CWOFKJrOdR10hpxn%2FitLU0CCjMuS3PjK0CLBfUzWrMXB419q%2BDQ7KawDjgfU6amhEP%2BvIQz&X-Amz-Signature=4e3928235b271754b68268c7e352114a6e6832d11a367371c45a1a17dad9f46e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAURQK25%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuvn8wOn7b83ZWyABXYVwyEImZ9NJ279AhZ%2F%2F8cXGXdAiBchxxzYO1a4hRodR5GNFZt5KHgrHG3Xu%2FZHSxUWopjRCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOLWMm09JiXAVI94sKtwDVQ3Y0Yd%2Fh3Ljp0uspbbxypJc69tIZhJOA0rFbjqBrlvm7H2VAq5JW5ROsQZ2E1jx1EfMs0eDtiAu5vYZkQKY0%2B57Xs18dmND9NRPquwQZhHmGVbfQhV4dVjVH7Bk3h16Bh%2Fjh5GIEsYvXAqeQfhkUsLUgL9rpkZkXZxuxsj1oHNSwijQIEVZ0m8749D0FARLl1L4ec3qGyL3v8f0K72mdVSA184EgGk8lmN6HYU2Xrv3OL%2F8lrMDMQkGHhPuyrxzz0m4dUDOTvDrxJJTUqAHDs0TP4TNDF%2BxCCCM9gfZ%2BeQacAoycCpWnSujPkawoi4KbiM5x8cKDbHCyu2OU2uK6TKAItaHYVRgGjjDGd51oL4KThfCfmWIAEKvVWVGr%2F1eZtzSTLWPTFbyNhnA8vr9mdkGcWf5hJoh7MqnAMcUgXZgpZh%2FSstM5LZBxHr%2B5WxH8JEhG6iaSOrHhrd3S47ULUqpwpPiTx%2BnFTGZDdUolESzzmMo7uvpovc%2FF4ZEb%2Fhs5UlYxUjHTiCOCsl6pHWL1B09mPaTX541P28GDHjbVCCsnHTKg8%2BPsYPk177Hqg8R3AuYH55YqQdC%2F0Y4EHhTYGIHyA5FTRWf4vLGE0gTQaKpzHG9uwtabElqH0ow2rHrvAY6pgGJ0DToRIZ84al3Kao%2Bq079K%2FVVYpIxCE3uCTZmF%2FmQ2FPdcOiIPY1f3zvtMcE5z19P2QHWNOZbZWX%2BN7KZpU%2BpxbSW7nac%2F9x4iVgnq0c2lLMHXoDC5JYnE7zXRrxYDJUsSQsvo%2B5kTGbeRZs0FW4q8CWOFKJrOdR10hpxn%2FitLU0CCjMuS3PjK0CLBfUzWrMXB419q%2BDQ7KawDjgfU6amhEP%2BvIQz&X-Amz-Signature=b3be6599342ba20cb792381e133d19673dcd4a2988afa63be225f63e8966cc29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAURQK25%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuvn8wOn7b83ZWyABXYVwyEImZ9NJ279AhZ%2F%2F8cXGXdAiBchxxzYO1a4hRodR5GNFZt5KHgrHG3Xu%2FZHSxUWopjRCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOLWMm09JiXAVI94sKtwDVQ3Y0Yd%2Fh3Ljp0uspbbxypJc69tIZhJOA0rFbjqBrlvm7H2VAq5JW5ROsQZ2E1jx1EfMs0eDtiAu5vYZkQKY0%2B57Xs18dmND9NRPquwQZhHmGVbfQhV4dVjVH7Bk3h16Bh%2Fjh5GIEsYvXAqeQfhkUsLUgL9rpkZkXZxuxsj1oHNSwijQIEVZ0m8749D0FARLl1L4ec3qGyL3v8f0K72mdVSA184EgGk8lmN6HYU2Xrv3OL%2F8lrMDMQkGHhPuyrxzz0m4dUDOTvDrxJJTUqAHDs0TP4TNDF%2BxCCCM9gfZ%2BeQacAoycCpWnSujPkawoi4KbiM5x8cKDbHCyu2OU2uK6TKAItaHYVRgGjjDGd51oL4KThfCfmWIAEKvVWVGr%2F1eZtzSTLWPTFbyNhnA8vr9mdkGcWf5hJoh7MqnAMcUgXZgpZh%2FSstM5LZBxHr%2B5WxH8JEhG6iaSOrHhrd3S47ULUqpwpPiTx%2BnFTGZDdUolESzzmMo7uvpovc%2FF4ZEb%2Fhs5UlYxUjHTiCOCsl6pHWL1B09mPaTX541P28GDHjbVCCsnHTKg8%2BPsYPk177Hqg8R3AuYH55YqQdC%2F0Y4EHhTYGIHyA5FTRWf4vLGE0gTQaKpzHG9uwtabElqH0ow2rHrvAY6pgGJ0DToRIZ84al3Kao%2Bq079K%2FVVYpIxCE3uCTZmF%2FmQ2FPdcOiIPY1f3zvtMcE5z19P2QHWNOZbZWX%2BN7KZpU%2BpxbSW7nac%2F9x4iVgnq0c2lLMHXoDC5JYnE7zXRrxYDJUsSQsvo%2B5kTGbeRZs0FW4q8CWOFKJrOdR10hpxn%2FitLU0CCjMuS3PjK0CLBfUzWrMXB419q%2BDQ7KawDjgfU6amhEP%2BvIQz&X-Amz-Signature=019a1158bca2d5488f687fa9f6f785cf48f597cd8280adfb520130c773ce89a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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


