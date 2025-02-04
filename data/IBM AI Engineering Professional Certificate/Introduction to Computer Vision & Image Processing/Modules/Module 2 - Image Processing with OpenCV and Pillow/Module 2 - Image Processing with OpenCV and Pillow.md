

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623KFPRI6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD8UO636D0MLW579N%2FGSCjBSOrvmlYrqjC76R5FjFAnWAIhAO43WiCgZyFRRcy1uNk1M4LFRMsmPniuW69gFgTVNe6ZKv8DCDEQABoMNjM3NDIzMTgzODA1Igw4rU%2FZM8W1i%2FxQxZEq3APFRVJbtQ4fV8%2BBZaPZhf3WjDvzwONsl7kslBj%2FtGE1VdVOrY29oWx2nN7CPlQygt13PUd%2BsCSWgIfpYBcpSiV7kpJSulCvlTGS%2Fj9MFh9gQ5rCf4xa1OjU1%2BLiJfqiIaIbBHtj%2BSXBkTteqOtAItzmfXLBuw0kCXC%2Fzk6L5Ot6x0I%2F2IAowabLfERraoMviwEc8oaCEzFNemaH%2BLeI9zX68QcxGIuxHap8wEVj30w6DqpGNud7gnR0BxWFwVgqNUrvDYhIAkl1aVcJ12SA%2BxlYpNAzxvqHSOqMJb0%2FfHlZQX0dm39NvJ2RSeIv57U%2BC08PAuLxsMoan7gmxtYWcREQSCFLAphkIAQsrXnyit06BZx5AliSzKAzJn6Q95CbL3GMiLaCsH0MKIlwZbeq9XQM6CZlj0XuBGWzc%2BbEwYqveHznUxnueBaCUccoeGr9m0HMLKfU9bVyiwMoJXDZa%2B9yTz4WTZXBg3HgR1fss9Q5E1kgWbgMgDhz9%2F5vXuez4qtxErv81bMAeadP63uOWQs9Y8xaE91kV2a7VnuQ5ru0dXr37Ux%2Fo5XNC7072soyEm6VtXR2YxMP8kmkXn3c%2FU9%2BvxcerzJDIDfAUsu6U4qsSJqTIchCjiqLkG%2Fa4TDF5oi9BjqkAVsTUoCZ69e5qgmS2twNU1y%2FRUwBnF%2BNN9W56PzVZGNjqDe6os6yxsEbuBd7GU9OeLesC9t9E7EFdd3pKYnTbqE08leADY4BkekiuSyVuNviWnSI1swBpUHua25L4htusa61BUFfARg6hp8hRgI9%2BefF1GFKZ0FuGN0N4pqffjIkLwUPzEJgYs64GorTJkiEH2ShcdLvCDCxHBPplmx4%2BSFSNBTB&X-Amz-Signature=1cb6772dbfbd737853d51f10572585f4dc1699fcbd592001c506d2eb70716dee&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMN3ZJDS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCICbc1uM3i3dL59cip1Q8HRNHfDUTx6QkAsGll49CG%2Bt%2BAiB90K%2FSQyXxqVI%2FEwwVL9hu%2B2yiQX%2Fk2fcRe7uSbsP7hir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIM8Qa3OKx91Aw16N9BKtwDkD%2FD%2BST3KLUzNQ6I17ZAhogTYGt%2B8g2UgqyfOPx%2FN8zLZ9KxoRVV5yucsViwA9Ql2XJmhaDjCwAZIqUVNeNv1dygbhk1p8c8a6YiQKTXVcLrB%2BesGPu8jy75dFm7TcvO%2FcH1%2BJ%2FRepnC%2BPtdkEgrY7njIAZbwLv9nBs3IIPEEkRCJkkrUjgNKyyLnQS7bSE8qc1TfuY%2BzODpt9oUdGNO757RC18f2C3zVhIHbaW9SEPPB8%2F4MHi3ZUnjELUKFyWhFm%2F96jsGz26SwaE3u0QwUYK%2FknHkPUZiXXNxb4FVN3%2FyBCNSByRTqwStivaffscFSa8e7sq1vImJC1hmFR6WLVdy9KU%2FVO7F61S1SOSePiVmIPCVWIPOBlp41LmCxPFuWJWoZawOIsVl38b9KaAvOSmWFqnINUT4jG1OZ5pNSnaVc0T%2BJV0FY%2BEC2GV0z9uLk2gmKWMXyw79wnwvXf%2FcnEtbfKWw%2BFgYigtVHvc9pUZ2%2B6O7Qs9HlV4yJICsyAKx%2BJ%2BgAFmmcGjn1seGByQU4lV9rEDwnl6Wa9lZyizspFCyJQtURjE34YUzUcAB6Shaw8Pu8mKv5ZBGSf0m3qzbbIey%2BHV%2BtotylK3kpPPax5q%2BtlmCoDpnfu59jV8wneeIvQY6pgHNscZY9RUJD1RCy%2F7HPv9bs2jQjvDKUJF0q06xSTcOjELx6GVzVg%2FMY%2F5TySmUvYrZJWSnC1tfwwBjhdozY3uNy37Y06JTvcfE%2BX5bh537JX%2FOZLDsK2%2FwF%2FIRT%2FZg%2BsjeD5gHdQchFxnh2egjBBCDADmZlyHKosdqoMHKaWVBtPZ8iMVe9Tuof%2BwC3%2B%2BCFzYCkXJq1TkAOSn0LzT1EdoNNqyxQulB&X-Amz-Signature=165c28f5345a07d2ea6f856b35c75ffad3d8a13478184ee13a6dcf537c07d476&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMN3ZJDS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCICbc1uM3i3dL59cip1Q8HRNHfDUTx6QkAsGll49CG%2Bt%2BAiB90K%2FSQyXxqVI%2FEwwVL9hu%2B2yiQX%2Fk2fcRe7uSbsP7hir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIM8Qa3OKx91Aw16N9BKtwDkD%2FD%2BST3KLUzNQ6I17ZAhogTYGt%2B8g2UgqyfOPx%2FN8zLZ9KxoRVV5yucsViwA9Ql2XJmhaDjCwAZIqUVNeNv1dygbhk1p8c8a6YiQKTXVcLrB%2BesGPu8jy75dFm7TcvO%2FcH1%2BJ%2FRepnC%2BPtdkEgrY7njIAZbwLv9nBs3IIPEEkRCJkkrUjgNKyyLnQS7bSE8qc1TfuY%2BzODpt9oUdGNO757RC18f2C3zVhIHbaW9SEPPB8%2F4MHi3ZUnjELUKFyWhFm%2F96jsGz26SwaE3u0QwUYK%2FknHkPUZiXXNxb4FVN3%2FyBCNSByRTqwStivaffscFSa8e7sq1vImJC1hmFR6WLVdy9KU%2FVO7F61S1SOSePiVmIPCVWIPOBlp41LmCxPFuWJWoZawOIsVl38b9KaAvOSmWFqnINUT4jG1OZ5pNSnaVc0T%2BJV0FY%2BEC2GV0z9uLk2gmKWMXyw79wnwvXf%2FcnEtbfKWw%2BFgYigtVHvc9pUZ2%2B6O7Qs9HlV4yJICsyAKx%2BJ%2BgAFmmcGjn1seGByQU4lV9rEDwnl6Wa9lZyizspFCyJQtURjE34YUzUcAB6Shaw8Pu8mKv5ZBGSf0m3qzbbIey%2BHV%2BtotylK3kpPPax5q%2BtlmCoDpnfu59jV8wneeIvQY6pgHNscZY9RUJD1RCy%2F7HPv9bs2jQjvDKUJF0q06xSTcOjELx6GVzVg%2FMY%2F5TySmUvYrZJWSnC1tfwwBjhdozY3uNy37Y06JTvcfE%2BX5bh537JX%2FOZLDsK2%2FwF%2FIRT%2FZg%2BsjeD5gHdQchFxnh2egjBBCDADmZlyHKosdqoMHKaWVBtPZ8iMVe9Tuof%2BwC3%2B%2BCFzYCkXJq1TkAOSn0LzT1EdoNNqyxQulB&X-Amz-Signature=04f28e426c27f06a2cea8ef60beb6a719436e7ce549d41ef42cf5a619719315a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMN3ZJDS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCICbc1uM3i3dL59cip1Q8HRNHfDUTx6QkAsGll49CG%2Bt%2BAiB90K%2FSQyXxqVI%2FEwwVL9hu%2B2yiQX%2Fk2fcRe7uSbsP7hir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIM8Qa3OKx91Aw16N9BKtwDkD%2FD%2BST3KLUzNQ6I17ZAhogTYGt%2B8g2UgqyfOPx%2FN8zLZ9KxoRVV5yucsViwA9Ql2XJmhaDjCwAZIqUVNeNv1dygbhk1p8c8a6YiQKTXVcLrB%2BesGPu8jy75dFm7TcvO%2FcH1%2BJ%2FRepnC%2BPtdkEgrY7njIAZbwLv9nBs3IIPEEkRCJkkrUjgNKyyLnQS7bSE8qc1TfuY%2BzODpt9oUdGNO757RC18f2C3zVhIHbaW9SEPPB8%2F4MHi3ZUnjELUKFyWhFm%2F96jsGz26SwaE3u0QwUYK%2FknHkPUZiXXNxb4FVN3%2FyBCNSByRTqwStivaffscFSa8e7sq1vImJC1hmFR6WLVdy9KU%2FVO7F61S1SOSePiVmIPCVWIPOBlp41LmCxPFuWJWoZawOIsVl38b9KaAvOSmWFqnINUT4jG1OZ5pNSnaVc0T%2BJV0FY%2BEC2GV0z9uLk2gmKWMXyw79wnwvXf%2FcnEtbfKWw%2BFgYigtVHvc9pUZ2%2B6O7Qs9HlV4yJICsyAKx%2BJ%2BgAFmmcGjn1seGByQU4lV9rEDwnl6Wa9lZyizspFCyJQtURjE34YUzUcAB6Shaw8Pu8mKv5ZBGSf0m3qzbbIey%2BHV%2BtotylK3kpPPax5q%2BtlmCoDpnfu59jV8wneeIvQY6pgHNscZY9RUJD1RCy%2F7HPv9bs2jQjvDKUJF0q06xSTcOjELx6GVzVg%2FMY%2F5TySmUvYrZJWSnC1tfwwBjhdozY3uNy37Y06JTvcfE%2BX5bh537JX%2FOZLDsK2%2FwF%2FIRT%2FZg%2BsjeD5gHdQchFxnh2egjBBCDADmZlyHKosdqoMHKaWVBtPZ8iMVe9Tuof%2BwC3%2B%2BCFzYCkXJq1TkAOSn0LzT1EdoNNqyxQulB&X-Amz-Signature=00872f14666beae8fdabe251054dec6ae8d6e4a9ad80f2169e2cf76de335188a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMN3ZJDS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCICbc1uM3i3dL59cip1Q8HRNHfDUTx6QkAsGll49CG%2Bt%2BAiB90K%2FSQyXxqVI%2FEwwVL9hu%2B2yiQX%2Fk2fcRe7uSbsP7hir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIM8Qa3OKx91Aw16N9BKtwDkD%2FD%2BST3KLUzNQ6I17ZAhogTYGt%2B8g2UgqyfOPx%2FN8zLZ9KxoRVV5yucsViwA9Ql2XJmhaDjCwAZIqUVNeNv1dygbhk1p8c8a6YiQKTXVcLrB%2BesGPu8jy75dFm7TcvO%2FcH1%2BJ%2FRepnC%2BPtdkEgrY7njIAZbwLv9nBs3IIPEEkRCJkkrUjgNKyyLnQS7bSE8qc1TfuY%2BzODpt9oUdGNO757RC18f2C3zVhIHbaW9SEPPB8%2F4MHi3ZUnjELUKFyWhFm%2F96jsGz26SwaE3u0QwUYK%2FknHkPUZiXXNxb4FVN3%2FyBCNSByRTqwStivaffscFSa8e7sq1vImJC1hmFR6WLVdy9KU%2FVO7F61S1SOSePiVmIPCVWIPOBlp41LmCxPFuWJWoZawOIsVl38b9KaAvOSmWFqnINUT4jG1OZ5pNSnaVc0T%2BJV0FY%2BEC2GV0z9uLk2gmKWMXyw79wnwvXf%2FcnEtbfKWw%2BFgYigtVHvc9pUZ2%2B6O7Qs9HlV4yJICsyAKx%2BJ%2BgAFmmcGjn1seGByQU4lV9rEDwnl6Wa9lZyizspFCyJQtURjE34YUzUcAB6Shaw8Pu8mKv5ZBGSf0m3qzbbIey%2BHV%2BtotylK3kpPPax5q%2BtlmCoDpnfu59jV8wneeIvQY6pgHNscZY9RUJD1RCy%2F7HPv9bs2jQjvDKUJF0q06xSTcOjELx6GVzVg%2FMY%2F5TySmUvYrZJWSnC1tfwwBjhdozY3uNy37Y06JTvcfE%2BX5bh537JX%2FOZLDsK2%2FwF%2FIRT%2FZg%2BsjeD5gHdQchFxnh2egjBBCDADmZlyHKosdqoMHKaWVBtPZ8iMVe9Tuof%2BwC3%2B%2BCFzYCkXJq1TkAOSn0LzT1EdoNNqyxQulB&X-Amz-Signature=a2ff860fee0b3d5d9908538a27592c4c2e7e62fd2a9f3d23086a49e2cb54dbca&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMN3ZJDS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCICbc1uM3i3dL59cip1Q8HRNHfDUTx6QkAsGll49CG%2Bt%2BAiB90K%2FSQyXxqVI%2FEwwVL9hu%2B2yiQX%2Fk2fcRe7uSbsP7hir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIM8Qa3OKx91Aw16N9BKtwDkD%2FD%2BST3KLUzNQ6I17ZAhogTYGt%2B8g2UgqyfOPx%2FN8zLZ9KxoRVV5yucsViwA9Ql2XJmhaDjCwAZIqUVNeNv1dygbhk1p8c8a6YiQKTXVcLrB%2BesGPu8jy75dFm7TcvO%2FcH1%2BJ%2FRepnC%2BPtdkEgrY7njIAZbwLv9nBs3IIPEEkRCJkkrUjgNKyyLnQS7bSE8qc1TfuY%2BzODpt9oUdGNO757RC18f2C3zVhIHbaW9SEPPB8%2F4MHi3ZUnjELUKFyWhFm%2F96jsGz26SwaE3u0QwUYK%2FknHkPUZiXXNxb4FVN3%2FyBCNSByRTqwStivaffscFSa8e7sq1vImJC1hmFR6WLVdy9KU%2FVO7F61S1SOSePiVmIPCVWIPOBlp41LmCxPFuWJWoZawOIsVl38b9KaAvOSmWFqnINUT4jG1OZ5pNSnaVc0T%2BJV0FY%2BEC2GV0z9uLk2gmKWMXyw79wnwvXf%2FcnEtbfKWw%2BFgYigtVHvc9pUZ2%2B6O7Qs9HlV4yJICsyAKx%2BJ%2BgAFmmcGjn1seGByQU4lV9rEDwnl6Wa9lZyizspFCyJQtURjE34YUzUcAB6Shaw8Pu8mKv5ZBGSf0m3qzbbIey%2BHV%2BtotylK3kpPPax5q%2BtlmCoDpnfu59jV8wneeIvQY6pgHNscZY9RUJD1RCy%2F7HPv9bs2jQjvDKUJF0q06xSTcOjELx6GVzVg%2FMY%2F5TySmUvYrZJWSnC1tfwwBjhdozY3uNy37Y06JTvcfE%2BX5bh537JX%2FOZLDsK2%2FwF%2FIRT%2FZg%2BsjeD5gHdQchFxnh2egjBBCDADmZlyHKosdqoMHKaWVBtPZ8iMVe9Tuof%2BwC3%2B%2BCFzYCkXJq1TkAOSn0LzT1EdoNNqyxQulB&X-Amz-Signature=4f8ef8c2cad5774a536fa5e4e1c6630f34e1d27d0b0832b9e5c7716ca868d5de&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623KFPRI6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD8UO636D0MLW579N%2FGSCjBSOrvmlYrqjC76R5FjFAnWAIhAO43WiCgZyFRRcy1uNk1M4LFRMsmPniuW69gFgTVNe6ZKv8DCDEQABoMNjM3NDIzMTgzODA1Igw4rU%2FZM8W1i%2FxQxZEq3APFRVJbtQ4fV8%2BBZaPZhf3WjDvzwONsl7kslBj%2FtGE1VdVOrY29oWx2nN7CPlQygt13PUd%2BsCSWgIfpYBcpSiV7kpJSulCvlTGS%2Fj9MFh9gQ5rCf4xa1OjU1%2BLiJfqiIaIbBHtj%2BSXBkTteqOtAItzmfXLBuw0kCXC%2Fzk6L5Ot6x0I%2F2IAowabLfERraoMviwEc8oaCEzFNemaH%2BLeI9zX68QcxGIuxHap8wEVj30w6DqpGNud7gnR0BxWFwVgqNUrvDYhIAkl1aVcJ12SA%2BxlYpNAzxvqHSOqMJb0%2FfHlZQX0dm39NvJ2RSeIv57U%2BC08PAuLxsMoan7gmxtYWcREQSCFLAphkIAQsrXnyit06BZx5AliSzKAzJn6Q95CbL3GMiLaCsH0MKIlwZbeq9XQM6CZlj0XuBGWzc%2BbEwYqveHznUxnueBaCUccoeGr9m0HMLKfU9bVyiwMoJXDZa%2B9yTz4WTZXBg3HgR1fss9Q5E1kgWbgMgDhz9%2F5vXuez4qtxErv81bMAeadP63uOWQs9Y8xaE91kV2a7VnuQ5ru0dXr37Ux%2Fo5XNC7072soyEm6VtXR2YxMP8kmkXn3c%2FU9%2BvxcerzJDIDfAUsu6U4qsSJqTIchCjiqLkG%2Fa4TDF5oi9BjqkAVsTUoCZ69e5qgmS2twNU1y%2FRUwBnF%2BNN9W56PzVZGNjqDe6os6yxsEbuBd7GU9OeLesC9t9E7EFdd3pKYnTbqE08leADY4BkekiuSyVuNviWnSI1swBpUHua25L4htusa61BUFfARg6hp8hRgI9%2BefF1GFKZ0FuGN0N4pqffjIkLwUPzEJgYs64GorTJkiEH2ShcdLvCDCxHBPplmx4%2BSFSNBTB&X-Amz-Signature=93731dc552dbc0b46cace57119a2f266148d90f474877d194c818f29fab53b71&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623KFPRI6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD8UO636D0MLW579N%2FGSCjBSOrvmlYrqjC76R5FjFAnWAIhAO43WiCgZyFRRcy1uNk1M4LFRMsmPniuW69gFgTVNe6ZKv8DCDEQABoMNjM3NDIzMTgzODA1Igw4rU%2FZM8W1i%2FxQxZEq3APFRVJbtQ4fV8%2BBZaPZhf3WjDvzwONsl7kslBj%2FtGE1VdVOrY29oWx2nN7CPlQygt13PUd%2BsCSWgIfpYBcpSiV7kpJSulCvlTGS%2Fj9MFh9gQ5rCf4xa1OjU1%2BLiJfqiIaIbBHtj%2BSXBkTteqOtAItzmfXLBuw0kCXC%2Fzk6L5Ot6x0I%2F2IAowabLfERraoMviwEc8oaCEzFNemaH%2BLeI9zX68QcxGIuxHap8wEVj30w6DqpGNud7gnR0BxWFwVgqNUrvDYhIAkl1aVcJ12SA%2BxlYpNAzxvqHSOqMJb0%2FfHlZQX0dm39NvJ2RSeIv57U%2BC08PAuLxsMoan7gmxtYWcREQSCFLAphkIAQsrXnyit06BZx5AliSzKAzJn6Q95CbL3GMiLaCsH0MKIlwZbeq9XQM6CZlj0XuBGWzc%2BbEwYqveHznUxnueBaCUccoeGr9m0HMLKfU9bVyiwMoJXDZa%2B9yTz4WTZXBg3HgR1fss9Q5E1kgWbgMgDhz9%2F5vXuez4qtxErv81bMAeadP63uOWQs9Y8xaE91kV2a7VnuQ5ru0dXr37Ux%2Fo5XNC7072soyEm6VtXR2YxMP8kmkXn3c%2FU9%2BvxcerzJDIDfAUsu6U4qsSJqTIchCjiqLkG%2Fa4TDF5oi9BjqkAVsTUoCZ69e5qgmS2twNU1y%2FRUwBnF%2BNN9W56PzVZGNjqDe6os6yxsEbuBd7GU9OeLesC9t9E7EFdd3pKYnTbqE08leADY4BkekiuSyVuNviWnSI1swBpUHua25L4htusa61BUFfARg6hp8hRgI9%2BefF1GFKZ0FuGN0N4pqffjIkLwUPzEJgYs64GorTJkiEH2ShcdLvCDCxHBPplmx4%2BSFSNBTB&X-Amz-Signature=11829735ce1fd7047a89601738f66f78ff4f3118a8483d5a81a6ffb1309b239c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623KFPRI6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD8UO636D0MLW579N%2FGSCjBSOrvmlYrqjC76R5FjFAnWAIhAO43WiCgZyFRRcy1uNk1M4LFRMsmPniuW69gFgTVNe6ZKv8DCDEQABoMNjM3NDIzMTgzODA1Igw4rU%2FZM8W1i%2FxQxZEq3APFRVJbtQ4fV8%2BBZaPZhf3WjDvzwONsl7kslBj%2FtGE1VdVOrY29oWx2nN7CPlQygt13PUd%2BsCSWgIfpYBcpSiV7kpJSulCvlTGS%2Fj9MFh9gQ5rCf4xa1OjU1%2BLiJfqiIaIbBHtj%2BSXBkTteqOtAItzmfXLBuw0kCXC%2Fzk6L5Ot6x0I%2F2IAowabLfERraoMviwEc8oaCEzFNemaH%2BLeI9zX68QcxGIuxHap8wEVj30w6DqpGNud7gnR0BxWFwVgqNUrvDYhIAkl1aVcJ12SA%2BxlYpNAzxvqHSOqMJb0%2FfHlZQX0dm39NvJ2RSeIv57U%2BC08PAuLxsMoan7gmxtYWcREQSCFLAphkIAQsrXnyit06BZx5AliSzKAzJn6Q95CbL3GMiLaCsH0MKIlwZbeq9XQM6CZlj0XuBGWzc%2BbEwYqveHznUxnueBaCUccoeGr9m0HMLKfU9bVyiwMoJXDZa%2B9yTz4WTZXBg3HgR1fss9Q5E1kgWbgMgDhz9%2F5vXuez4qtxErv81bMAeadP63uOWQs9Y8xaE91kV2a7VnuQ5ru0dXr37Ux%2Fo5XNC7072soyEm6VtXR2YxMP8kmkXn3c%2FU9%2BvxcerzJDIDfAUsu6U4qsSJqTIchCjiqLkG%2Fa4TDF5oi9BjqkAVsTUoCZ69e5qgmS2twNU1y%2FRUwBnF%2BNN9W56PzVZGNjqDe6os6yxsEbuBd7GU9OeLesC9t9E7EFdd3pKYnTbqE08leADY4BkekiuSyVuNviWnSI1swBpUHua25L4htusa61BUFfARg6hp8hRgI9%2BefF1GFKZ0FuGN0N4pqffjIkLwUPzEJgYs64GorTJkiEH2ShcdLvCDCxHBPplmx4%2BSFSNBTB&X-Amz-Signature=da8854e3dfa60852c5c5012189b952362d1159fe6ccc1d2b2f50da0041addecf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623KFPRI6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD8UO636D0MLW579N%2FGSCjBSOrvmlYrqjC76R5FjFAnWAIhAO43WiCgZyFRRcy1uNk1M4LFRMsmPniuW69gFgTVNe6ZKv8DCDEQABoMNjM3NDIzMTgzODA1Igw4rU%2FZM8W1i%2FxQxZEq3APFRVJbtQ4fV8%2BBZaPZhf3WjDvzwONsl7kslBj%2FtGE1VdVOrY29oWx2nN7CPlQygt13PUd%2BsCSWgIfpYBcpSiV7kpJSulCvlTGS%2Fj9MFh9gQ5rCf4xa1OjU1%2BLiJfqiIaIbBHtj%2BSXBkTteqOtAItzmfXLBuw0kCXC%2Fzk6L5Ot6x0I%2F2IAowabLfERraoMviwEc8oaCEzFNemaH%2BLeI9zX68QcxGIuxHap8wEVj30w6DqpGNud7gnR0BxWFwVgqNUrvDYhIAkl1aVcJ12SA%2BxlYpNAzxvqHSOqMJb0%2FfHlZQX0dm39NvJ2RSeIv57U%2BC08PAuLxsMoan7gmxtYWcREQSCFLAphkIAQsrXnyit06BZx5AliSzKAzJn6Q95CbL3GMiLaCsH0MKIlwZbeq9XQM6CZlj0XuBGWzc%2BbEwYqveHznUxnueBaCUccoeGr9m0HMLKfU9bVyiwMoJXDZa%2B9yTz4WTZXBg3HgR1fss9Q5E1kgWbgMgDhz9%2F5vXuez4qtxErv81bMAeadP63uOWQs9Y8xaE91kV2a7VnuQ5ru0dXr37Ux%2Fo5XNC7072soyEm6VtXR2YxMP8kmkXn3c%2FU9%2BvxcerzJDIDfAUsu6U4qsSJqTIchCjiqLkG%2Fa4TDF5oi9BjqkAVsTUoCZ69e5qgmS2twNU1y%2FRUwBnF%2BNN9W56PzVZGNjqDe6os6yxsEbuBd7GU9OeLesC9t9E7EFdd3pKYnTbqE08leADY4BkekiuSyVuNviWnSI1swBpUHua25L4htusa61BUFfARg6hp8hRgI9%2BefF1GFKZ0FuGN0N4pqffjIkLwUPzEJgYs64GorTJkiEH2ShcdLvCDCxHBPplmx4%2BSFSNBTB&X-Amz-Signature=0d09464006d82ecbab8172d0d31640e44ab781a9b7840130c787ce4a29faa281&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623KFPRI6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD8UO636D0MLW579N%2FGSCjBSOrvmlYrqjC76R5FjFAnWAIhAO43WiCgZyFRRcy1uNk1M4LFRMsmPniuW69gFgTVNe6ZKv8DCDEQABoMNjM3NDIzMTgzODA1Igw4rU%2FZM8W1i%2FxQxZEq3APFRVJbtQ4fV8%2BBZaPZhf3WjDvzwONsl7kslBj%2FtGE1VdVOrY29oWx2nN7CPlQygt13PUd%2BsCSWgIfpYBcpSiV7kpJSulCvlTGS%2Fj9MFh9gQ5rCf4xa1OjU1%2BLiJfqiIaIbBHtj%2BSXBkTteqOtAItzmfXLBuw0kCXC%2Fzk6L5Ot6x0I%2F2IAowabLfERraoMviwEc8oaCEzFNemaH%2BLeI9zX68QcxGIuxHap8wEVj30w6DqpGNud7gnR0BxWFwVgqNUrvDYhIAkl1aVcJ12SA%2BxlYpNAzxvqHSOqMJb0%2FfHlZQX0dm39NvJ2RSeIv57U%2BC08PAuLxsMoan7gmxtYWcREQSCFLAphkIAQsrXnyit06BZx5AliSzKAzJn6Q95CbL3GMiLaCsH0MKIlwZbeq9XQM6CZlj0XuBGWzc%2BbEwYqveHznUxnueBaCUccoeGr9m0HMLKfU9bVyiwMoJXDZa%2B9yTz4WTZXBg3HgR1fss9Q5E1kgWbgMgDhz9%2F5vXuez4qtxErv81bMAeadP63uOWQs9Y8xaE91kV2a7VnuQ5ru0dXr37Ux%2Fo5XNC7072soyEm6VtXR2YxMP8kmkXn3c%2FU9%2BvxcerzJDIDfAUsu6U4qsSJqTIchCjiqLkG%2Fa4TDF5oi9BjqkAVsTUoCZ69e5qgmS2twNU1y%2FRUwBnF%2BNN9W56PzVZGNjqDe6os6yxsEbuBd7GU9OeLesC9t9E7EFdd3pKYnTbqE08leADY4BkekiuSyVuNviWnSI1swBpUHua25L4htusa61BUFfARg6hp8hRgI9%2BefF1GFKZ0FuGN0N4pqffjIkLwUPzEJgYs64GorTJkiEH2ShcdLvCDCxHBPplmx4%2BSFSNBTB&X-Amz-Signature=a7ace3138d261467f564b2a5a474bc5a57e3d952604c4e90f8bb6888b786bf96&X-Amz-SignedHeaders=host&x-id=GetObject)
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


