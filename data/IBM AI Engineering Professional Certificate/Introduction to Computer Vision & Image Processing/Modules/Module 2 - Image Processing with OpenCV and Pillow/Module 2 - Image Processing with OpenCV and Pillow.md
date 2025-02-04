

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RXRXNPW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIA%2F8gSi9D9KfzPLS14D%2B9ZZO8kMGsHcTbgXTUDPKhY5OAiB2lAeH01Dj0GTj4zOZ%2FiNp53iI4lTsKPIcwht%2FWqBgiCr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMLHh9yD75zTKDaPlGKtwD3eiRYuQCfEwZknDdBzaOIJrx%2BKGftb%2BPJ5YW0V9IN8usAclpw5ZccmeFEvOc8BSs9FbJxwYUlyavAtn2%2BskubsaCJeJzei3rTlE07OpGwVpo5%2FRj6HlkKkgSCqldfAGwgsCNfvkRMdSUKjtkl5brxHNXL7DSdJwoMRBiRPwOmIAojUPFdM7x47daYg1VAZJ3AXvq9HAi2Y8nKof6FUZ5Qkyl8WVtI5TDq2JWmcwE%2BLxi8ZY%2BiDFJHcJ1%2Bw446UB95Q4RimyKypLgBQC1Lh4ZUl%2F1Uol0DBZXwLmioqfGOPdNQpmI7d9LNQ59VEvdsf2tcAFVWfAiaqRzWIoWjnIY0gDkx%2BFPJajMFdPU7Gk3ZQuOaeY15KIO0jcNn952ogvPo7Mg6xwbQFWchshPAAiva8y2G46JHC8eOeSgZ3ryDCFsNwmePMVATMkqIxdihbZBKRTvX1aWPkak%2F%2B7bkK7Y2QSdrVrZWJlvzBUgIMOV3oq4VFbarZy3hEVCEYiYQL%2F%2Bp%2BYAG9F8zTaXjEBrkEOE3NoLja4ffg6OgNe1A0DHOVFMzDgvBAwLgbsMsU6gX%2B%2F05j4pn0LAg87fxpKvsZ91UimQ%2BAAKbN41CKYYNsBYqItKos6O1x7pIl5ZKlowl72IvQY6pgHCnLOL3%2BKaNk58gmPqC8i%2FaQtTOKQM%2FGBKqEirARONEdugVMP5bPzlcm7uHpzzzvFISowpKpYyc2LgWYYuPhPMG0iXzRFXv5ARWVAk40WLyM%2B%2Bx5J68esxrm1ymwx3l6frYmkT7aHoCvYtUec9GJOPBbh9yqz4GY5U5fgoi6bP19JGUMICJ14XiwAiwvFPPdlgPfQY47%2BgJ4JTgpmVPHN91GgrJO7X&X-Amz-Signature=2dfba074241c5f02d095f89d634f2667ec45a0abbe3b52acd621c08567fd4941&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I3EBDQZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBDwUFXCmbQL86UVfAn0mVXzjdL4rShqzFflVd8E88lSAiAC3KcpxFH6j%2BK1hn5y1Xxf9kyrozTIKp1kBeiqNz9NaSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMaISuObQpewoKsgmVKtwD9s2BYze0O2wxMojMViAuM0loZtE0t259dx4I58xu5ZTDpSsvV6RPTijm%2F8BKuaXksz%2FKavh%2F6uuHySOVzqBZYH3o9safcp6X46uoUfn0551B%2BgTuXhtrlutSnNCRsWgxOtZAg%2BuKb4taj99WM1gk38jOs7z%2BS2NmjQnSAufeLLunr4ufXxCgGAZiC9Hf22FgOCJNvxbVL3R9yit5oo5ExwVfflxFu5%2Bc90AKnHYouER5zsbhssrDz79r79ZXHftM0T9t90P0ecdoVDytaoPwCCB9fqYn%2FU57B80Y7PdLp9Z7ilrUYuxgYauAwXjIQfO92BLqGQHE6mSwMr5sBaWCViY7Zb6L%2FB1NcAfJQFio5O0QNf6Gue33WNEbp%2FoFZCIlJTfJDhJjKyR2vwXqvxL2%2FzTL%2Br3IXhppBV9x8qz8fuyxT19iR%2Bupj7z2aMr1wW24hVFQPgABSmzaZxSGPRVhIoYRbTVvmfmcRqeUrQv5YMYKgF2rpkU87%2Fpl54LZ3Xvr1Tj9BEGEfKQkQeDe0qh6lSWjl6UazSy9X16nRk2ggrydyELHkLNC8C1MFo7Jub0b4Oy9iJiWJHqsCkfPLk2EqBdpdTZspg6Qe1QhffhW0IS0N44fSff98D7lWVMwjr2IvQY6pgH3rekMH1XWflt%2FkjRGB7jHL%2BQ7eeyJj3bof1OrClbAvR8tC37TybKs35bvxz5CgMnr6zsbv1soM1Z%2BA8nchXkHXJwXt%2BEmRQbZTnOdyYAE3X6fGx7pMwhubS4mj0gyvDZuUScibMtWmHoLpbDDaC4D7MJWQKGDYkLGXgmnbfigf7jEi65rQGmV23G6EXg88gh1LtK9RnUfFVc4eZtKIT8FE3ai62hb&X-Amz-Signature=9da140d8f6724235bf9ca5ccf7da3cf670f468619f848c13a17bb16594fa03e0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I3EBDQZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBDwUFXCmbQL86UVfAn0mVXzjdL4rShqzFflVd8E88lSAiAC3KcpxFH6j%2BK1hn5y1Xxf9kyrozTIKp1kBeiqNz9NaSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMaISuObQpewoKsgmVKtwD9s2BYze0O2wxMojMViAuM0loZtE0t259dx4I58xu5ZTDpSsvV6RPTijm%2F8BKuaXksz%2FKavh%2F6uuHySOVzqBZYH3o9safcp6X46uoUfn0551B%2BgTuXhtrlutSnNCRsWgxOtZAg%2BuKb4taj99WM1gk38jOs7z%2BS2NmjQnSAufeLLunr4ufXxCgGAZiC9Hf22FgOCJNvxbVL3R9yit5oo5ExwVfflxFu5%2Bc90AKnHYouER5zsbhssrDz79r79ZXHftM0T9t90P0ecdoVDytaoPwCCB9fqYn%2FU57B80Y7PdLp9Z7ilrUYuxgYauAwXjIQfO92BLqGQHE6mSwMr5sBaWCViY7Zb6L%2FB1NcAfJQFio5O0QNf6Gue33WNEbp%2FoFZCIlJTfJDhJjKyR2vwXqvxL2%2FzTL%2Br3IXhppBV9x8qz8fuyxT19iR%2Bupj7z2aMr1wW24hVFQPgABSmzaZxSGPRVhIoYRbTVvmfmcRqeUrQv5YMYKgF2rpkU87%2Fpl54LZ3Xvr1Tj9BEGEfKQkQeDe0qh6lSWjl6UazSy9X16nRk2ggrydyELHkLNC8C1MFo7Jub0b4Oy9iJiWJHqsCkfPLk2EqBdpdTZspg6Qe1QhffhW0IS0N44fSff98D7lWVMwjr2IvQY6pgH3rekMH1XWflt%2FkjRGB7jHL%2BQ7eeyJj3bof1OrClbAvR8tC37TybKs35bvxz5CgMnr6zsbv1soM1Z%2BA8nchXkHXJwXt%2BEmRQbZTnOdyYAE3X6fGx7pMwhubS4mj0gyvDZuUScibMtWmHoLpbDDaC4D7MJWQKGDYkLGXgmnbfigf7jEi65rQGmV23G6EXg88gh1LtK9RnUfFVc4eZtKIT8FE3ai62hb&X-Amz-Signature=537efd7a2cc4cb50665e9e778e21179f682204f402c6cd58d434d4b839b81262&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I3EBDQZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBDwUFXCmbQL86UVfAn0mVXzjdL4rShqzFflVd8E88lSAiAC3KcpxFH6j%2BK1hn5y1Xxf9kyrozTIKp1kBeiqNz9NaSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMaISuObQpewoKsgmVKtwD9s2BYze0O2wxMojMViAuM0loZtE0t259dx4I58xu5ZTDpSsvV6RPTijm%2F8BKuaXksz%2FKavh%2F6uuHySOVzqBZYH3o9safcp6X46uoUfn0551B%2BgTuXhtrlutSnNCRsWgxOtZAg%2BuKb4taj99WM1gk38jOs7z%2BS2NmjQnSAufeLLunr4ufXxCgGAZiC9Hf22FgOCJNvxbVL3R9yit5oo5ExwVfflxFu5%2Bc90AKnHYouER5zsbhssrDz79r79ZXHftM0T9t90P0ecdoVDytaoPwCCB9fqYn%2FU57B80Y7PdLp9Z7ilrUYuxgYauAwXjIQfO92BLqGQHE6mSwMr5sBaWCViY7Zb6L%2FB1NcAfJQFio5O0QNf6Gue33WNEbp%2FoFZCIlJTfJDhJjKyR2vwXqvxL2%2FzTL%2Br3IXhppBV9x8qz8fuyxT19iR%2Bupj7z2aMr1wW24hVFQPgABSmzaZxSGPRVhIoYRbTVvmfmcRqeUrQv5YMYKgF2rpkU87%2Fpl54LZ3Xvr1Tj9BEGEfKQkQeDe0qh6lSWjl6UazSy9X16nRk2ggrydyELHkLNC8C1MFo7Jub0b4Oy9iJiWJHqsCkfPLk2EqBdpdTZspg6Qe1QhffhW0IS0N44fSff98D7lWVMwjr2IvQY6pgH3rekMH1XWflt%2FkjRGB7jHL%2BQ7eeyJj3bof1OrClbAvR8tC37TybKs35bvxz5CgMnr6zsbv1soM1Z%2BA8nchXkHXJwXt%2BEmRQbZTnOdyYAE3X6fGx7pMwhubS4mj0gyvDZuUScibMtWmHoLpbDDaC4D7MJWQKGDYkLGXgmnbfigf7jEi65rQGmV23G6EXg88gh1LtK9RnUfFVc4eZtKIT8FE3ai62hb&X-Amz-Signature=e3abe6d71bcb6abedbd03c8431f2b0e554674f55b93431469ae1019f556563dd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I3EBDQZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBDwUFXCmbQL86UVfAn0mVXzjdL4rShqzFflVd8E88lSAiAC3KcpxFH6j%2BK1hn5y1Xxf9kyrozTIKp1kBeiqNz9NaSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMaISuObQpewoKsgmVKtwD9s2BYze0O2wxMojMViAuM0loZtE0t259dx4I58xu5ZTDpSsvV6RPTijm%2F8BKuaXksz%2FKavh%2F6uuHySOVzqBZYH3o9safcp6X46uoUfn0551B%2BgTuXhtrlutSnNCRsWgxOtZAg%2BuKb4taj99WM1gk38jOs7z%2BS2NmjQnSAufeLLunr4ufXxCgGAZiC9Hf22FgOCJNvxbVL3R9yit5oo5ExwVfflxFu5%2Bc90AKnHYouER5zsbhssrDz79r79ZXHftM0T9t90P0ecdoVDytaoPwCCB9fqYn%2FU57B80Y7PdLp9Z7ilrUYuxgYauAwXjIQfO92BLqGQHE6mSwMr5sBaWCViY7Zb6L%2FB1NcAfJQFio5O0QNf6Gue33WNEbp%2FoFZCIlJTfJDhJjKyR2vwXqvxL2%2FzTL%2Br3IXhppBV9x8qz8fuyxT19iR%2Bupj7z2aMr1wW24hVFQPgABSmzaZxSGPRVhIoYRbTVvmfmcRqeUrQv5YMYKgF2rpkU87%2Fpl54LZ3Xvr1Tj9BEGEfKQkQeDe0qh6lSWjl6UazSy9X16nRk2ggrydyELHkLNC8C1MFo7Jub0b4Oy9iJiWJHqsCkfPLk2EqBdpdTZspg6Qe1QhffhW0IS0N44fSff98D7lWVMwjr2IvQY6pgH3rekMH1XWflt%2FkjRGB7jHL%2BQ7eeyJj3bof1OrClbAvR8tC37TybKs35bvxz5CgMnr6zsbv1soM1Z%2BA8nchXkHXJwXt%2BEmRQbZTnOdyYAE3X6fGx7pMwhubS4mj0gyvDZuUScibMtWmHoLpbDDaC4D7MJWQKGDYkLGXgmnbfigf7jEi65rQGmV23G6EXg88gh1LtK9RnUfFVc4eZtKIT8FE3ai62hb&X-Amz-Signature=93ea46f7ff1dacfe61bc8e7436463ffcb87c80fbe1beb073ac8a177a0dd4998f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I3EBDQZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBDwUFXCmbQL86UVfAn0mVXzjdL4rShqzFflVd8E88lSAiAC3KcpxFH6j%2BK1hn5y1Xxf9kyrozTIKp1kBeiqNz9NaSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMaISuObQpewoKsgmVKtwD9s2BYze0O2wxMojMViAuM0loZtE0t259dx4I58xu5ZTDpSsvV6RPTijm%2F8BKuaXksz%2FKavh%2F6uuHySOVzqBZYH3o9safcp6X46uoUfn0551B%2BgTuXhtrlutSnNCRsWgxOtZAg%2BuKb4taj99WM1gk38jOs7z%2BS2NmjQnSAufeLLunr4ufXxCgGAZiC9Hf22FgOCJNvxbVL3R9yit5oo5ExwVfflxFu5%2Bc90AKnHYouER5zsbhssrDz79r79ZXHftM0T9t90P0ecdoVDytaoPwCCB9fqYn%2FU57B80Y7PdLp9Z7ilrUYuxgYauAwXjIQfO92BLqGQHE6mSwMr5sBaWCViY7Zb6L%2FB1NcAfJQFio5O0QNf6Gue33WNEbp%2FoFZCIlJTfJDhJjKyR2vwXqvxL2%2FzTL%2Br3IXhppBV9x8qz8fuyxT19iR%2Bupj7z2aMr1wW24hVFQPgABSmzaZxSGPRVhIoYRbTVvmfmcRqeUrQv5YMYKgF2rpkU87%2Fpl54LZ3Xvr1Tj9BEGEfKQkQeDe0qh6lSWjl6UazSy9X16nRk2ggrydyELHkLNC8C1MFo7Jub0b4Oy9iJiWJHqsCkfPLk2EqBdpdTZspg6Qe1QhffhW0IS0N44fSff98D7lWVMwjr2IvQY6pgH3rekMH1XWflt%2FkjRGB7jHL%2BQ7eeyJj3bof1OrClbAvR8tC37TybKs35bvxz5CgMnr6zsbv1soM1Z%2BA8nchXkHXJwXt%2BEmRQbZTnOdyYAE3X6fGx7pMwhubS4mj0gyvDZuUScibMtWmHoLpbDDaC4D7MJWQKGDYkLGXgmnbfigf7jEi65rQGmV23G6EXg88gh1LtK9RnUfFVc4eZtKIT8FE3ai62hb&X-Amz-Signature=af3530ef7d754a69aeb74e2f600b48dd27aa563513cca64b83a9259cf0fe0bff&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RXRXNPW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIA%2F8gSi9D9KfzPLS14D%2B9ZZO8kMGsHcTbgXTUDPKhY5OAiB2lAeH01Dj0GTj4zOZ%2FiNp53iI4lTsKPIcwht%2FWqBgiCr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMLHh9yD75zTKDaPlGKtwD3eiRYuQCfEwZknDdBzaOIJrx%2BKGftb%2BPJ5YW0V9IN8usAclpw5ZccmeFEvOc8BSs9FbJxwYUlyavAtn2%2BskubsaCJeJzei3rTlE07OpGwVpo5%2FRj6HlkKkgSCqldfAGwgsCNfvkRMdSUKjtkl5brxHNXL7DSdJwoMRBiRPwOmIAojUPFdM7x47daYg1VAZJ3AXvq9HAi2Y8nKof6FUZ5Qkyl8WVtI5TDq2JWmcwE%2BLxi8ZY%2BiDFJHcJ1%2Bw446UB95Q4RimyKypLgBQC1Lh4ZUl%2F1Uol0DBZXwLmioqfGOPdNQpmI7d9LNQ59VEvdsf2tcAFVWfAiaqRzWIoWjnIY0gDkx%2BFPJajMFdPU7Gk3ZQuOaeY15KIO0jcNn952ogvPo7Mg6xwbQFWchshPAAiva8y2G46JHC8eOeSgZ3ryDCFsNwmePMVATMkqIxdihbZBKRTvX1aWPkak%2F%2B7bkK7Y2QSdrVrZWJlvzBUgIMOV3oq4VFbarZy3hEVCEYiYQL%2F%2Bp%2BYAG9F8zTaXjEBrkEOE3NoLja4ffg6OgNe1A0DHOVFMzDgvBAwLgbsMsU6gX%2B%2F05j4pn0LAg87fxpKvsZ91UimQ%2BAAKbN41CKYYNsBYqItKos6O1x7pIl5ZKlowl72IvQY6pgHCnLOL3%2BKaNk58gmPqC8i%2FaQtTOKQM%2FGBKqEirARONEdugVMP5bPzlcm7uHpzzzvFISowpKpYyc2LgWYYuPhPMG0iXzRFXv5ARWVAk40WLyM%2B%2Bx5J68esxrm1ymwx3l6frYmkT7aHoCvYtUec9GJOPBbh9yqz4GY5U5fgoi6bP19JGUMICJ14XiwAiwvFPPdlgPfQY47%2BgJ4JTgpmVPHN91GgrJO7X&X-Amz-Signature=b10e6db07b453684b1d6ab28ab6884fa4483b21493753028d87926476d002352&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RXRXNPW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIA%2F8gSi9D9KfzPLS14D%2B9ZZO8kMGsHcTbgXTUDPKhY5OAiB2lAeH01Dj0GTj4zOZ%2FiNp53iI4lTsKPIcwht%2FWqBgiCr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMLHh9yD75zTKDaPlGKtwD3eiRYuQCfEwZknDdBzaOIJrx%2BKGftb%2BPJ5YW0V9IN8usAclpw5ZccmeFEvOc8BSs9FbJxwYUlyavAtn2%2BskubsaCJeJzei3rTlE07OpGwVpo5%2FRj6HlkKkgSCqldfAGwgsCNfvkRMdSUKjtkl5brxHNXL7DSdJwoMRBiRPwOmIAojUPFdM7x47daYg1VAZJ3AXvq9HAi2Y8nKof6FUZ5Qkyl8WVtI5TDq2JWmcwE%2BLxi8ZY%2BiDFJHcJ1%2Bw446UB95Q4RimyKypLgBQC1Lh4ZUl%2F1Uol0DBZXwLmioqfGOPdNQpmI7d9LNQ59VEvdsf2tcAFVWfAiaqRzWIoWjnIY0gDkx%2BFPJajMFdPU7Gk3ZQuOaeY15KIO0jcNn952ogvPo7Mg6xwbQFWchshPAAiva8y2G46JHC8eOeSgZ3ryDCFsNwmePMVATMkqIxdihbZBKRTvX1aWPkak%2F%2B7bkK7Y2QSdrVrZWJlvzBUgIMOV3oq4VFbarZy3hEVCEYiYQL%2F%2Bp%2BYAG9F8zTaXjEBrkEOE3NoLja4ffg6OgNe1A0DHOVFMzDgvBAwLgbsMsU6gX%2B%2F05j4pn0LAg87fxpKvsZ91UimQ%2BAAKbN41CKYYNsBYqItKos6O1x7pIl5ZKlowl72IvQY6pgHCnLOL3%2BKaNk58gmPqC8i%2FaQtTOKQM%2FGBKqEirARONEdugVMP5bPzlcm7uHpzzzvFISowpKpYyc2LgWYYuPhPMG0iXzRFXv5ARWVAk40WLyM%2B%2Bx5J68esxrm1ymwx3l6frYmkT7aHoCvYtUec9GJOPBbh9yqz4GY5U5fgoi6bP19JGUMICJ14XiwAiwvFPPdlgPfQY47%2BgJ4JTgpmVPHN91GgrJO7X&X-Amz-Signature=2eecdf34d4bc0b945eb11a6210d1000df54460939df205ddd5b898e5d9367a80&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RXRXNPW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIA%2F8gSi9D9KfzPLS14D%2B9ZZO8kMGsHcTbgXTUDPKhY5OAiB2lAeH01Dj0GTj4zOZ%2FiNp53iI4lTsKPIcwht%2FWqBgiCr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMLHh9yD75zTKDaPlGKtwD3eiRYuQCfEwZknDdBzaOIJrx%2BKGftb%2BPJ5YW0V9IN8usAclpw5ZccmeFEvOc8BSs9FbJxwYUlyavAtn2%2BskubsaCJeJzei3rTlE07OpGwVpo5%2FRj6HlkKkgSCqldfAGwgsCNfvkRMdSUKjtkl5brxHNXL7DSdJwoMRBiRPwOmIAojUPFdM7x47daYg1VAZJ3AXvq9HAi2Y8nKof6FUZ5Qkyl8WVtI5TDq2JWmcwE%2BLxi8ZY%2BiDFJHcJ1%2Bw446UB95Q4RimyKypLgBQC1Lh4ZUl%2F1Uol0DBZXwLmioqfGOPdNQpmI7d9LNQ59VEvdsf2tcAFVWfAiaqRzWIoWjnIY0gDkx%2BFPJajMFdPU7Gk3ZQuOaeY15KIO0jcNn952ogvPo7Mg6xwbQFWchshPAAiva8y2G46JHC8eOeSgZ3ryDCFsNwmePMVATMkqIxdihbZBKRTvX1aWPkak%2F%2B7bkK7Y2QSdrVrZWJlvzBUgIMOV3oq4VFbarZy3hEVCEYiYQL%2F%2Bp%2BYAG9F8zTaXjEBrkEOE3NoLja4ffg6OgNe1A0DHOVFMzDgvBAwLgbsMsU6gX%2B%2F05j4pn0LAg87fxpKvsZ91UimQ%2BAAKbN41CKYYNsBYqItKos6O1x7pIl5ZKlowl72IvQY6pgHCnLOL3%2BKaNk58gmPqC8i%2FaQtTOKQM%2FGBKqEirARONEdugVMP5bPzlcm7uHpzzzvFISowpKpYyc2LgWYYuPhPMG0iXzRFXv5ARWVAk40WLyM%2B%2Bx5J68esxrm1ymwx3l6frYmkT7aHoCvYtUec9GJOPBbh9yqz4GY5U5fgoi6bP19JGUMICJ14XiwAiwvFPPdlgPfQY47%2BgJ4JTgpmVPHN91GgrJO7X&X-Amz-Signature=98c76a727af0a516eb2504f0bd0273d9200c5ef6775673585cdeb16e2d98c518&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RXRXNPW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIA%2F8gSi9D9KfzPLS14D%2B9ZZO8kMGsHcTbgXTUDPKhY5OAiB2lAeH01Dj0GTj4zOZ%2FiNp53iI4lTsKPIcwht%2FWqBgiCr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMLHh9yD75zTKDaPlGKtwD3eiRYuQCfEwZknDdBzaOIJrx%2BKGftb%2BPJ5YW0V9IN8usAclpw5ZccmeFEvOc8BSs9FbJxwYUlyavAtn2%2BskubsaCJeJzei3rTlE07OpGwVpo5%2FRj6HlkKkgSCqldfAGwgsCNfvkRMdSUKjtkl5brxHNXL7DSdJwoMRBiRPwOmIAojUPFdM7x47daYg1VAZJ3AXvq9HAi2Y8nKof6FUZ5Qkyl8WVtI5TDq2JWmcwE%2BLxi8ZY%2BiDFJHcJ1%2Bw446UB95Q4RimyKypLgBQC1Lh4ZUl%2F1Uol0DBZXwLmioqfGOPdNQpmI7d9LNQ59VEvdsf2tcAFVWfAiaqRzWIoWjnIY0gDkx%2BFPJajMFdPU7Gk3ZQuOaeY15KIO0jcNn952ogvPo7Mg6xwbQFWchshPAAiva8y2G46JHC8eOeSgZ3ryDCFsNwmePMVATMkqIxdihbZBKRTvX1aWPkak%2F%2B7bkK7Y2QSdrVrZWJlvzBUgIMOV3oq4VFbarZy3hEVCEYiYQL%2F%2Bp%2BYAG9F8zTaXjEBrkEOE3NoLja4ffg6OgNe1A0DHOVFMzDgvBAwLgbsMsU6gX%2B%2F05j4pn0LAg87fxpKvsZ91UimQ%2BAAKbN41CKYYNsBYqItKos6O1x7pIl5ZKlowl72IvQY6pgHCnLOL3%2BKaNk58gmPqC8i%2FaQtTOKQM%2FGBKqEirARONEdugVMP5bPzlcm7uHpzzzvFISowpKpYyc2LgWYYuPhPMG0iXzRFXv5ARWVAk40WLyM%2B%2Bx5J68esxrm1ymwx3l6frYmkT7aHoCvYtUec9GJOPBbh9yqz4GY5U5fgoi6bP19JGUMICJ14XiwAiwvFPPdlgPfQY47%2BgJ4JTgpmVPHN91GgrJO7X&X-Amz-Signature=b4e1d809215d1e1570f134aec09c282af91f1c1ee965b2755b30857ab4c578dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RXRXNPW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIA%2F8gSi9D9KfzPLS14D%2B9ZZO8kMGsHcTbgXTUDPKhY5OAiB2lAeH01Dj0GTj4zOZ%2FiNp53iI4lTsKPIcwht%2FWqBgiCr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMLHh9yD75zTKDaPlGKtwD3eiRYuQCfEwZknDdBzaOIJrx%2BKGftb%2BPJ5YW0V9IN8usAclpw5ZccmeFEvOc8BSs9FbJxwYUlyavAtn2%2BskubsaCJeJzei3rTlE07OpGwVpo5%2FRj6HlkKkgSCqldfAGwgsCNfvkRMdSUKjtkl5brxHNXL7DSdJwoMRBiRPwOmIAojUPFdM7x47daYg1VAZJ3AXvq9HAi2Y8nKof6FUZ5Qkyl8WVtI5TDq2JWmcwE%2BLxi8ZY%2BiDFJHcJ1%2Bw446UB95Q4RimyKypLgBQC1Lh4ZUl%2F1Uol0DBZXwLmioqfGOPdNQpmI7d9LNQ59VEvdsf2tcAFVWfAiaqRzWIoWjnIY0gDkx%2BFPJajMFdPU7Gk3ZQuOaeY15KIO0jcNn952ogvPo7Mg6xwbQFWchshPAAiva8y2G46JHC8eOeSgZ3ryDCFsNwmePMVATMkqIxdihbZBKRTvX1aWPkak%2F%2B7bkK7Y2QSdrVrZWJlvzBUgIMOV3oq4VFbarZy3hEVCEYiYQL%2F%2Bp%2BYAG9F8zTaXjEBrkEOE3NoLja4ffg6OgNe1A0DHOVFMzDgvBAwLgbsMsU6gX%2B%2F05j4pn0LAg87fxpKvsZ91UimQ%2BAAKbN41CKYYNsBYqItKos6O1x7pIl5ZKlowl72IvQY6pgHCnLOL3%2BKaNk58gmPqC8i%2FaQtTOKQM%2FGBKqEirARONEdugVMP5bPzlcm7uHpzzzvFISowpKpYyc2LgWYYuPhPMG0iXzRFXv5ARWVAk40WLyM%2B%2Bx5J68esxrm1ymwx3l6frYmkT7aHoCvYtUec9GJOPBbh9yqz4GY5U5fgoi6bP19JGUMICJ14XiwAiwvFPPdlgPfQY47%2BgJ4JTgpmVPHN91GgrJO7X&X-Amz-Signature=33045258db0e8da40f3b3f154c3500473f8d6193bb7783fe0f9c4126a715c84e&X-Amz-SignedHeaders=host&x-id=GetObject)
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


