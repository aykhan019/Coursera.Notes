

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S77OMCFJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUwuj2nMP%2BvBt2PhvjipI6qadLWCmFtsmNR1QGNN3H3AiB%2BkdZMyrjH0gGVOssooZH%2BHAgotPrPxVC9WE4qhdUc6CqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIrC2%2B%2BqDPZ30tVShKtwDOuE0a64kSijGTjZKoPPzRoK3Yre8cB2nJO2AyfR6U2w5aX00hsWRVzTNc%2Bu9%2BmxsfqfJf1YRli6zxNYxBLpXx7dr8tdDwG6W1x9WbfakQoiChq0QT%2BYn5zOBqW11srDJR793bVPhEzIDx8dgAUcE1Ka%2BzeC6sy245e%2FQCfE5HBInizqJmzXowJAdgOk%2FEO8maQEx53DG4B%2FcRgF93Zyn4fchbueNTNbDZOYzGkUEdL7BO1WnJyY45yYMSCD5%2B4fRlPjudmfB5TE9gvUkp1%2BuoYKSmGZ2WKILehI%2F1myqQZwDs%2Fksali83JMyeDsfDkeZWE4qg7ng%2FV%2BowdKr7hoVzWRsbSuU17YMExG0%2BCVdi8XnlZrGwFqFLRWocb7frej6fOQg9a9KdTWrA9caKjdqD0b5eV6OvM59mqKMCYSghYClydggx0cK1%2B0FAGiT%2FUk5HUqLxaW58Fr%2FJjWu9W2hxe5Oy5JzjCq2eBzpyyQW0Bxok02shGr5C6xKBQX4cmr2hXHcyP5k3gvKEm5IUQ7B9kUzNlBvVlC4Z1CzAELh5feWVhQ%2Bwpy54UBqRg8k3JV5XlcgGUECPG%2B0yLfinmLr5NfKnB5WrDlTxSuI6h6hTReDiZcgaSF%2BjmdyToAwt%2FLuvAY6pgHME71KFdOmgWBlFKSvHK%2FiS4lg3ur5CV8HpB%2B%2FUd1xiSulILNjhFY9zHCnz%2F2mz3yOm6PlXM9qJJqZqnFHZ%2F%2BNs2EcTIo20%2FtEE4o3qNw3GwjX3fNZO%2BsbOKUeugWLveLAvoqZXhukNtMZ5D1fo%2Bcvsx4E9mDlJOVIibYmi36bVpPfhsOI%2FwaKHs4kJ3kU6IU5DTgJczzDI6yhdbc8693mFZdZZMT1&X-Amz-Signature=97cdd3c563c496dbde0132c8a2ae2e1d1554f96dcf9a03c90d6f063e68e9e8ad&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZH2AGZL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyG33dvEzIlqlrtiFQTE%2FlGo2ss2eL1ou32bTs6hfh3gIhAMITf0rgjdvdcKplLOaiG7OqDCDrAu21d7UrEkBMf02jKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwOGd%2Fa1q5PLmeCmQMq3AOKfJ0pKUu3x1onP37FTzGWpTX9CZGavSK3yczEn1edm0px9C9ruPhd9gq9L%2FgJ7NbNretxj3HfFzGZYlMhPh2WtH4HueZFOqlJpggYQwHsXPz8NjWdZqYzMJVV7LuBNibTSIkIY1qUO1xw94YeofGbmYNc4Q1qcsW8yMnenT09NFv5DD9FI6mVltGa7hVQuAKlDLoY%2BV%2BJ3g2D6kmejyEvbz8d5rdY70f7WZCUY6ZBG2cM0H9dt0LNiqHLK3ES3KnO3Z3Y8AMe8dyHNwZEw5B3al2uUgwVgWkXbgMbOk9yY1m%2BoQDENr1S2Uqas%2BeNUWHyXTV0BRFx%2FdSecsJV9H4LbIFDYcCli96KFO6IEeMCrd9azh%2F3hf26ExAgC9sW7vN389TQ2rr%2Fc6YfeHKKS4QeEEepIC3Wz9To5DvcssC57FS%2BedJVOuGewfrQ1aPY%2BXU83pestcnY6LdIeAeQTkBAblC6%2BeEvvorCxzIbJ7DizycPYzhgnNuJcf0x%2BEwDC%2FAn4U7m23NFoV1fVcifg9%2FZ426RnzChaAUTStqk5scBLbG3edpYQa2a%2B95dOMYWJAt7dFXkpqUcscOJf72WhDWuUTweCcOoBI3Rur5Io6hoJoogOZWRGbJhcfkjYzCC8%2B68BjqkAaypsjUOLXP%2BiHy051OWcLBP5%2BYD%2BT0Ya1DjY7HypBVWQLQhP1LzO%2BpwTV64Z1I5XsUxqLQT9rZ4f88%2Fui%2FG6eDM2MJ%2BIc%2Feq1Sl6SxDpZ5kcgIUmYVFd7Pmg34HrgGvMSHHNCsR9LFyDL5z0CsCefHuKDnNbJSftNsv4hABpwEFJo%2Fcl6vog4%2B5jThac3YXB0Vc%2BWwVkxnW0MltqGycJvc6IT5f&X-Amz-Signature=e858e7b7f49a18a22d78a9a0dab7c67f0dd5c033ac1f72e7f948c5900843156e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZH2AGZL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyG33dvEzIlqlrtiFQTE%2FlGo2ss2eL1ou32bTs6hfh3gIhAMITf0rgjdvdcKplLOaiG7OqDCDrAu21d7UrEkBMf02jKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwOGd%2Fa1q5PLmeCmQMq3AOKfJ0pKUu3x1onP37FTzGWpTX9CZGavSK3yczEn1edm0px9C9ruPhd9gq9L%2FgJ7NbNretxj3HfFzGZYlMhPh2WtH4HueZFOqlJpggYQwHsXPz8NjWdZqYzMJVV7LuBNibTSIkIY1qUO1xw94YeofGbmYNc4Q1qcsW8yMnenT09NFv5DD9FI6mVltGa7hVQuAKlDLoY%2BV%2BJ3g2D6kmejyEvbz8d5rdY70f7WZCUY6ZBG2cM0H9dt0LNiqHLK3ES3KnO3Z3Y8AMe8dyHNwZEw5B3al2uUgwVgWkXbgMbOk9yY1m%2BoQDENr1S2Uqas%2BeNUWHyXTV0BRFx%2FdSecsJV9H4LbIFDYcCli96KFO6IEeMCrd9azh%2F3hf26ExAgC9sW7vN389TQ2rr%2Fc6YfeHKKS4QeEEepIC3Wz9To5DvcssC57FS%2BedJVOuGewfrQ1aPY%2BXU83pestcnY6LdIeAeQTkBAblC6%2BeEvvorCxzIbJ7DizycPYzhgnNuJcf0x%2BEwDC%2FAn4U7m23NFoV1fVcifg9%2FZ426RnzChaAUTStqk5scBLbG3edpYQa2a%2B95dOMYWJAt7dFXkpqUcscOJf72WhDWuUTweCcOoBI3Rur5Io6hoJoogOZWRGbJhcfkjYzCC8%2B68BjqkAaypsjUOLXP%2BiHy051OWcLBP5%2BYD%2BT0Ya1DjY7HypBVWQLQhP1LzO%2BpwTV64Z1I5XsUxqLQT9rZ4f88%2Fui%2FG6eDM2MJ%2BIc%2Feq1Sl6SxDpZ5kcgIUmYVFd7Pmg34HrgGvMSHHNCsR9LFyDL5z0CsCefHuKDnNbJSftNsv4hABpwEFJo%2Fcl6vog4%2B5jThac3YXB0Vc%2BWwVkxnW0MltqGycJvc6IT5f&X-Amz-Signature=0608ef96266fca7f5e159053775e464472f1e9dcd929e3a0e3b433b3ee5b7a07&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZH2AGZL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyG33dvEzIlqlrtiFQTE%2FlGo2ss2eL1ou32bTs6hfh3gIhAMITf0rgjdvdcKplLOaiG7OqDCDrAu21d7UrEkBMf02jKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwOGd%2Fa1q5PLmeCmQMq3AOKfJ0pKUu3x1onP37FTzGWpTX9CZGavSK3yczEn1edm0px9C9ruPhd9gq9L%2FgJ7NbNretxj3HfFzGZYlMhPh2WtH4HueZFOqlJpggYQwHsXPz8NjWdZqYzMJVV7LuBNibTSIkIY1qUO1xw94YeofGbmYNc4Q1qcsW8yMnenT09NFv5DD9FI6mVltGa7hVQuAKlDLoY%2BV%2BJ3g2D6kmejyEvbz8d5rdY70f7WZCUY6ZBG2cM0H9dt0LNiqHLK3ES3KnO3Z3Y8AMe8dyHNwZEw5B3al2uUgwVgWkXbgMbOk9yY1m%2BoQDENr1S2Uqas%2BeNUWHyXTV0BRFx%2FdSecsJV9H4LbIFDYcCli96KFO6IEeMCrd9azh%2F3hf26ExAgC9sW7vN389TQ2rr%2Fc6YfeHKKS4QeEEepIC3Wz9To5DvcssC57FS%2BedJVOuGewfrQ1aPY%2BXU83pestcnY6LdIeAeQTkBAblC6%2BeEvvorCxzIbJ7DizycPYzhgnNuJcf0x%2BEwDC%2FAn4U7m23NFoV1fVcifg9%2FZ426RnzChaAUTStqk5scBLbG3edpYQa2a%2B95dOMYWJAt7dFXkpqUcscOJf72WhDWuUTweCcOoBI3Rur5Io6hoJoogOZWRGbJhcfkjYzCC8%2B68BjqkAaypsjUOLXP%2BiHy051OWcLBP5%2BYD%2BT0Ya1DjY7HypBVWQLQhP1LzO%2BpwTV64Z1I5XsUxqLQT9rZ4f88%2Fui%2FG6eDM2MJ%2BIc%2Feq1Sl6SxDpZ5kcgIUmYVFd7Pmg34HrgGvMSHHNCsR9LFyDL5z0CsCefHuKDnNbJSftNsv4hABpwEFJo%2Fcl6vog4%2B5jThac3YXB0Vc%2BWwVkxnW0MltqGycJvc6IT5f&X-Amz-Signature=591dc2bd5114d587a1bcf49c3e4a72efbc22b8dd525753627e6516d2eb2caef9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZH2AGZL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyG33dvEzIlqlrtiFQTE%2FlGo2ss2eL1ou32bTs6hfh3gIhAMITf0rgjdvdcKplLOaiG7OqDCDrAu21d7UrEkBMf02jKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwOGd%2Fa1q5PLmeCmQMq3AOKfJ0pKUu3x1onP37FTzGWpTX9CZGavSK3yczEn1edm0px9C9ruPhd9gq9L%2FgJ7NbNretxj3HfFzGZYlMhPh2WtH4HueZFOqlJpggYQwHsXPz8NjWdZqYzMJVV7LuBNibTSIkIY1qUO1xw94YeofGbmYNc4Q1qcsW8yMnenT09NFv5DD9FI6mVltGa7hVQuAKlDLoY%2BV%2BJ3g2D6kmejyEvbz8d5rdY70f7WZCUY6ZBG2cM0H9dt0LNiqHLK3ES3KnO3Z3Y8AMe8dyHNwZEw5B3al2uUgwVgWkXbgMbOk9yY1m%2BoQDENr1S2Uqas%2BeNUWHyXTV0BRFx%2FdSecsJV9H4LbIFDYcCli96KFO6IEeMCrd9azh%2F3hf26ExAgC9sW7vN389TQ2rr%2Fc6YfeHKKS4QeEEepIC3Wz9To5DvcssC57FS%2BedJVOuGewfrQ1aPY%2BXU83pestcnY6LdIeAeQTkBAblC6%2BeEvvorCxzIbJ7DizycPYzhgnNuJcf0x%2BEwDC%2FAn4U7m23NFoV1fVcifg9%2FZ426RnzChaAUTStqk5scBLbG3edpYQa2a%2B95dOMYWJAt7dFXkpqUcscOJf72WhDWuUTweCcOoBI3Rur5Io6hoJoogOZWRGbJhcfkjYzCC8%2B68BjqkAaypsjUOLXP%2BiHy051OWcLBP5%2BYD%2BT0Ya1DjY7HypBVWQLQhP1LzO%2BpwTV64Z1I5XsUxqLQT9rZ4f88%2Fui%2FG6eDM2MJ%2BIc%2Feq1Sl6SxDpZ5kcgIUmYVFd7Pmg34HrgGvMSHHNCsR9LFyDL5z0CsCefHuKDnNbJSftNsv4hABpwEFJo%2Fcl6vog4%2B5jThac3YXB0Vc%2BWwVkxnW0MltqGycJvc6IT5f&X-Amz-Signature=f3708880ec62c4b3feaef1b4b9cda09ee29ce4a91fd114f33d39a491b176a3e4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZH2AGZL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyG33dvEzIlqlrtiFQTE%2FlGo2ss2eL1ou32bTs6hfh3gIhAMITf0rgjdvdcKplLOaiG7OqDCDrAu21d7UrEkBMf02jKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwOGd%2Fa1q5PLmeCmQMq3AOKfJ0pKUu3x1onP37FTzGWpTX9CZGavSK3yczEn1edm0px9C9ruPhd9gq9L%2FgJ7NbNretxj3HfFzGZYlMhPh2WtH4HueZFOqlJpggYQwHsXPz8NjWdZqYzMJVV7LuBNibTSIkIY1qUO1xw94YeofGbmYNc4Q1qcsW8yMnenT09NFv5DD9FI6mVltGa7hVQuAKlDLoY%2BV%2BJ3g2D6kmejyEvbz8d5rdY70f7WZCUY6ZBG2cM0H9dt0LNiqHLK3ES3KnO3Z3Y8AMe8dyHNwZEw5B3al2uUgwVgWkXbgMbOk9yY1m%2BoQDENr1S2Uqas%2BeNUWHyXTV0BRFx%2FdSecsJV9H4LbIFDYcCli96KFO6IEeMCrd9azh%2F3hf26ExAgC9sW7vN389TQ2rr%2Fc6YfeHKKS4QeEEepIC3Wz9To5DvcssC57FS%2BedJVOuGewfrQ1aPY%2BXU83pestcnY6LdIeAeQTkBAblC6%2BeEvvorCxzIbJ7DizycPYzhgnNuJcf0x%2BEwDC%2FAn4U7m23NFoV1fVcifg9%2FZ426RnzChaAUTStqk5scBLbG3edpYQa2a%2B95dOMYWJAt7dFXkpqUcscOJf72WhDWuUTweCcOoBI3Rur5Io6hoJoogOZWRGbJhcfkjYzCC8%2B68BjqkAaypsjUOLXP%2BiHy051OWcLBP5%2BYD%2BT0Ya1DjY7HypBVWQLQhP1LzO%2BpwTV64Z1I5XsUxqLQT9rZ4f88%2Fui%2FG6eDM2MJ%2BIc%2Feq1Sl6SxDpZ5kcgIUmYVFd7Pmg34HrgGvMSHHNCsR9LFyDL5z0CsCefHuKDnNbJSftNsv4hABpwEFJo%2Fcl6vog4%2B5jThac3YXB0Vc%2BWwVkxnW0MltqGycJvc6IT5f&X-Amz-Signature=484bab11c7eca4f09fafcf90e56776e5e74c8d35fa9b935a624ba03b031062b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S77OMCFJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUwuj2nMP%2BvBt2PhvjipI6qadLWCmFtsmNR1QGNN3H3AiB%2BkdZMyrjH0gGVOssooZH%2BHAgotPrPxVC9WE4qhdUc6CqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIrC2%2B%2BqDPZ30tVShKtwDOuE0a64kSijGTjZKoPPzRoK3Yre8cB2nJO2AyfR6U2w5aX00hsWRVzTNc%2Bu9%2BmxsfqfJf1YRli6zxNYxBLpXx7dr8tdDwG6W1x9WbfakQoiChq0QT%2BYn5zOBqW11srDJR793bVPhEzIDx8dgAUcE1Ka%2BzeC6sy245e%2FQCfE5HBInizqJmzXowJAdgOk%2FEO8maQEx53DG4B%2FcRgF93Zyn4fchbueNTNbDZOYzGkUEdL7BO1WnJyY45yYMSCD5%2B4fRlPjudmfB5TE9gvUkp1%2BuoYKSmGZ2WKILehI%2F1myqQZwDs%2Fksali83JMyeDsfDkeZWE4qg7ng%2FV%2BowdKr7hoVzWRsbSuU17YMExG0%2BCVdi8XnlZrGwFqFLRWocb7frej6fOQg9a9KdTWrA9caKjdqD0b5eV6OvM59mqKMCYSghYClydggx0cK1%2B0FAGiT%2FUk5HUqLxaW58Fr%2FJjWu9W2hxe5Oy5JzjCq2eBzpyyQW0Bxok02shGr5C6xKBQX4cmr2hXHcyP5k3gvKEm5IUQ7B9kUzNlBvVlC4Z1CzAELh5feWVhQ%2Bwpy54UBqRg8k3JV5XlcgGUECPG%2B0yLfinmLr5NfKnB5WrDlTxSuI6h6hTReDiZcgaSF%2BjmdyToAwt%2FLuvAY6pgHME71KFdOmgWBlFKSvHK%2FiS4lg3ur5CV8HpB%2B%2FUd1xiSulILNjhFY9zHCnz%2F2mz3yOm6PlXM9qJJqZqnFHZ%2F%2BNs2EcTIo20%2FtEE4o3qNw3GwjX3fNZO%2BsbOKUeugWLveLAvoqZXhukNtMZ5D1fo%2Bcvsx4E9mDlJOVIibYmi36bVpPfhsOI%2FwaKHs4kJ3kU6IU5DTgJczzDI6yhdbc8693mFZdZZMT1&X-Amz-Signature=ffb34a63ab868dcdb05065ffb500e214fb48b98256fbc50a7c9973a1a7d0275d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S77OMCFJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUwuj2nMP%2BvBt2PhvjipI6qadLWCmFtsmNR1QGNN3H3AiB%2BkdZMyrjH0gGVOssooZH%2BHAgotPrPxVC9WE4qhdUc6CqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIrC2%2B%2BqDPZ30tVShKtwDOuE0a64kSijGTjZKoPPzRoK3Yre8cB2nJO2AyfR6U2w5aX00hsWRVzTNc%2Bu9%2BmxsfqfJf1YRli6zxNYxBLpXx7dr8tdDwG6W1x9WbfakQoiChq0QT%2BYn5zOBqW11srDJR793bVPhEzIDx8dgAUcE1Ka%2BzeC6sy245e%2FQCfE5HBInizqJmzXowJAdgOk%2FEO8maQEx53DG4B%2FcRgF93Zyn4fchbueNTNbDZOYzGkUEdL7BO1WnJyY45yYMSCD5%2B4fRlPjudmfB5TE9gvUkp1%2BuoYKSmGZ2WKILehI%2F1myqQZwDs%2Fksali83JMyeDsfDkeZWE4qg7ng%2FV%2BowdKr7hoVzWRsbSuU17YMExG0%2BCVdi8XnlZrGwFqFLRWocb7frej6fOQg9a9KdTWrA9caKjdqD0b5eV6OvM59mqKMCYSghYClydggx0cK1%2B0FAGiT%2FUk5HUqLxaW58Fr%2FJjWu9W2hxe5Oy5JzjCq2eBzpyyQW0Bxok02shGr5C6xKBQX4cmr2hXHcyP5k3gvKEm5IUQ7B9kUzNlBvVlC4Z1CzAELh5feWVhQ%2Bwpy54UBqRg8k3JV5XlcgGUECPG%2B0yLfinmLr5NfKnB5WrDlTxSuI6h6hTReDiZcgaSF%2BjmdyToAwt%2FLuvAY6pgHME71KFdOmgWBlFKSvHK%2FiS4lg3ur5CV8HpB%2B%2FUd1xiSulILNjhFY9zHCnz%2F2mz3yOm6PlXM9qJJqZqnFHZ%2F%2BNs2EcTIo20%2FtEE4o3qNw3GwjX3fNZO%2BsbOKUeugWLveLAvoqZXhukNtMZ5D1fo%2Bcvsx4E9mDlJOVIibYmi36bVpPfhsOI%2FwaKHs4kJ3kU6IU5DTgJczzDI6yhdbc8693mFZdZZMT1&X-Amz-Signature=450731c34f76e237e4f302125a13e79c8f57cb615b184cf56c2049218582c5b2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S77OMCFJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUwuj2nMP%2BvBt2PhvjipI6qadLWCmFtsmNR1QGNN3H3AiB%2BkdZMyrjH0gGVOssooZH%2BHAgotPrPxVC9WE4qhdUc6CqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIrC2%2B%2BqDPZ30tVShKtwDOuE0a64kSijGTjZKoPPzRoK3Yre8cB2nJO2AyfR6U2w5aX00hsWRVzTNc%2Bu9%2BmxsfqfJf1YRli6zxNYxBLpXx7dr8tdDwG6W1x9WbfakQoiChq0QT%2BYn5zOBqW11srDJR793bVPhEzIDx8dgAUcE1Ka%2BzeC6sy245e%2FQCfE5HBInizqJmzXowJAdgOk%2FEO8maQEx53DG4B%2FcRgF93Zyn4fchbueNTNbDZOYzGkUEdL7BO1WnJyY45yYMSCD5%2B4fRlPjudmfB5TE9gvUkp1%2BuoYKSmGZ2WKILehI%2F1myqQZwDs%2Fksali83JMyeDsfDkeZWE4qg7ng%2FV%2BowdKr7hoVzWRsbSuU17YMExG0%2BCVdi8XnlZrGwFqFLRWocb7frej6fOQg9a9KdTWrA9caKjdqD0b5eV6OvM59mqKMCYSghYClydggx0cK1%2B0FAGiT%2FUk5HUqLxaW58Fr%2FJjWu9W2hxe5Oy5JzjCq2eBzpyyQW0Bxok02shGr5C6xKBQX4cmr2hXHcyP5k3gvKEm5IUQ7B9kUzNlBvVlC4Z1CzAELh5feWVhQ%2Bwpy54UBqRg8k3JV5XlcgGUECPG%2B0yLfinmLr5NfKnB5WrDlTxSuI6h6hTReDiZcgaSF%2BjmdyToAwt%2FLuvAY6pgHME71KFdOmgWBlFKSvHK%2FiS4lg3ur5CV8HpB%2B%2FUd1xiSulILNjhFY9zHCnz%2F2mz3yOm6PlXM9qJJqZqnFHZ%2F%2BNs2EcTIo20%2FtEE4o3qNw3GwjX3fNZO%2BsbOKUeugWLveLAvoqZXhukNtMZ5D1fo%2Bcvsx4E9mDlJOVIibYmi36bVpPfhsOI%2FwaKHs4kJ3kU6IU5DTgJczzDI6yhdbc8693mFZdZZMT1&X-Amz-Signature=48f34269c0f4d14bc0a4a03453420b028285663721753a45c7434ab178913fc6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S77OMCFJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUwuj2nMP%2BvBt2PhvjipI6qadLWCmFtsmNR1QGNN3H3AiB%2BkdZMyrjH0gGVOssooZH%2BHAgotPrPxVC9WE4qhdUc6CqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIrC2%2B%2BqDPZ30tVShKtwDOuE0a64kSijGTjZKoPPzRoK3Yre8cB2nJO2AyfR6U2w5aX00hsWRVzTNc%2Bu9%2BmxsfqfJf1YRli6zxNYxBLpXx7dr8tdDwG6W1x9WbfakQoiChq0QT%2BYn5zOBqW11srDJR793bVPhEzIDx8dgAUcE1Ka%2BzeC6sy245e%2FQCfE5HBInizqJmzXowJAdgOk%2FEO8maQEx53DG4B%2FcRgF93Zyn4fchbueNTNbDZOYzGkUEdL7BO1WnJyY45yYMSCD5%2B4fRlPjudmfB5TE9gvUkp1%2BuoYKSmGZ2WKILehI%2F1myqQZwDs%2Fksali83JMyeDsfDkeZWE4qg7ng%2FV%2BowdKr7hoVzWRsbSuU17YMExG0%2BCVdi8XnlZrGwFqFLRWocb7frej6fOQg9a9KdTWrA9caKjdqD0b5eV6OvM59mqKMCYSghYClydggx0cK1%2B0FAGiT%2FUk5HUqLxaW58Fr%2FJjWu9W2hxe5Oy5JzjCq2eBzpyyQW0Bxok02shGr5C6xKBQX4cmr2hXHcyP5k3gvKEm5IUQ7B9kUzNlBvVlC4Z1CzAELh5feWVhQ%2Bwpy54UBqRg8k3JV5XlcgGUECPG%2B0yLfinmLr5NfKnB5WrDlTxSuI6h6hTReDiZcgaSF%2BjmdyToAwt%2FLuvAY6pgHME71KFdOmgWBlFKSvHK%2FiS4lg3ur5CV8HpB%2B%2FUd1xiSulILNjhFY9zHCnz%2F2mz3yOm6PlXM9qJJqZqnFHZ%2F%2BNs2EcTIo20%2FtEE4o3qNw3GwjX3fNZO%2BsbOKUeugWLveLAvoqZXhukNtMZ5D1fo%2Bcvsx4E9mDlJOVIibYmi36bVpPfhsOI%2FwaKHs4kJ3kU6IU5DTgJczzDI6yhdbc8693mFZdZZMT1&X-Amz-Signature=af1d567db36d8039da2e49714044dcc23a78d2aacc5827bc9cb9f64d97fa5cd3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S77OMCFJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUwuj2nMP%2BvBt2PhvjipI6qadLWCmFtsmNR1QGNN3H3AiB%2BkdZMyrjH0gGVOssooZH%2BHAgotPrPxVC9WE4qhdUc6CqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIrC2%2B%2BqDPZ30tVShKtwDOuE0a64kSijGTjZKoPPzRoK3Yre8cB2nJO2AyfR6U2w5aX00hsWRVzTNc%2Bu9%2BmxsfqfJf1YRli6zxNYxBLpXx7dr8tdDwG6W1x9WbfakQoiChq0QT%2BYn5zOBqW11srDJR793bVPhEzIDx8dgAUcE1Ka%2BzeC6sy245e%2FQCfE5HBInizqJmzXowJAdgOk%2FEO8maQEx53DG4B%2FcRgF93Zyn4fchbueNTNbDZOYzGkUEdL7BO1WnJyY45yYMSCD5%2B4fRlPjudmfB5TE9gvUkp1%2BuoYKSmGZ2WKILehI%2F1myqQZwDs%2Fksali83JMyeDsfDkeZWE4qg7ng%2FV%2BowdKr7hoVzWRsbSuU17YMExG0%2BCVdi8XnlZrGwFqFLRWocb7frej6fOQg9a9KdTWrA9caKjdqD0b5eV6OvM59mqKMCYSghYClydggx0cK1%2B0FAGiT%2FUk5HUqLxaW58Fr%2FJjWu9W2hxe5Oy5JzjCq2eBzpyyQW0Bxok02shGr5C6xKBQX4cmr2hXHcyP5k3gvKEm5IUQ7B9kUzNlBvVlC4Z1CzAELh5feWVhQ%2Bwpy54UBqRg8k3JV5XlcgGUECPG%2B0yLfinmLr5NfKnB5WrDlTxSuI6h6hTReDiZcgaSF%2BjmdyToAwt%2FLuvAY6pgHME71KFdOmgWBlFKSvHK%2FiS4lg3ur5CV8HpB%2B%2FUd1xiSulILNjhFY9zHCnz%2F2mz3yOm6PlXM9qJJqZqnFHZ%2F%2BNs2EcTIo20%2FtEE4o3qNw3GwjX3fNZO%2BsbOKUeugWLveLAvoqZXhukNtMZ5D1fo%2Bcvsx4E9mDlJOVIibYmi36bVpPfhsOI%2FwaKHs4kJ3kU6IU5DTgJczzDI6yhdbc8693mFZdZZMT1&X-Amz-Signature=efe4a95a8a5497d2126d9882990f684041e401f018ee29a967fc75bb6454aede&X-Amz-SignedHeaders=host&x-id=GetObject)
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


