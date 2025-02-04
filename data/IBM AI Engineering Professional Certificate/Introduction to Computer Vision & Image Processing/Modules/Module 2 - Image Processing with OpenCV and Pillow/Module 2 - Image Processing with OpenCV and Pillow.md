

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLVN2ZUB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIGJRSdoB2Yg46NyxuAGzls2pYNcrkMiZ3x1P0%2FnZnzNTAiEAtjLsct5q9hTbADOhUgmNW5J8udjZoF3HddySbEBWxkEq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBNq9TnTfRRID30DtSrcA5tMHjJ4rfolGZgLMTzDZgN5MlOBUwIaIKGUqkUD8YbWr8DVBnIB7eJhY8cXrxc2%2FfQYNpwiQ%2FvynD0rFHzj%2B1BiRWqLWfEhux7iQSFemZxn3dZPKboKGCoKWe4BEqXNU27KSn2hyPnMIPDz%2FDrGhzAropJDKreAg%2FfP6v4P4QTEXbyS%2BQNRrBOrCSTXKupTpY2jD0Ra9H7CnxuCK5h%2BWMBPzSX8R3Pt8GIutGhVB9Hfs8TN4vuMckN7%2FMf6bH%2B%2FQX60JVLhpWnfwL94Y%2B71ZHbucivdyWWyzwZF4fABcQcX0nLZZKhrNaNaBQA%2FCEKGvRi5NzYwoz2WZDW5hFNqbMHUsawiYY%2B%2BBCvjDazqkg2%2Biy489QZU%2Bdmipy%2FooEccL4ZxrsSoqQysW4fUe6dq%2FkW%2F7ciQUQlQwcdMUQt92uNHixJBfr6Fa7%2F%2Fi49hegiDqlTbULki6%2F5RAYpIHyCbo9jKjmyU%2FCXPotWNkI40S1u4YPR04CreJpvJeF62rIXZa4nNOOM52d4%2FD8VwF46aBJZdLdxjdhYdw7%2B0N3WCRPay9VweXaFmIOII5QyEj0%2FChb%2Fgatw3gSmFz6ESN1Mxnn7e1UXM4%2F%2F4Pc08x%2FfhLx%2FmIQ6TRZfyXSm1OR5AMMj9ib0GOqUB2Nu6gXlzdykg5LmuWYD5JfGLo67qEtsCaNoLrU7wqNp0FhqwbatiYiCO2MCZ61xySRkAqC8UBI7H8M%2BjrkCbS51mxoLhlBESQBnuiEMvQaa0dk9HFx%2BznJ6BSpQuJQWIZPvMsnvUbwhEWC4XcR%2F0leGExEG12UPKtToiWuhCNmdYtPvEOWD4%2BEzj4HwKMOhlgJpl0WhiODNRrjYyFqHiPHcc4JU%2F&X-Amz-Signature=c7e68df3d5315e2f1f4cfc1c846e404f433bc947984764134b88daf1d8a02f14&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BA3HREE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIBhPlJB8Z2FDogkbEAsh2fyW5t8QN6ZjHWBS5F7rj%2BG2AiAO7LnI8NFxYPDzRwfuHXnG1L%2FDJ1Do2FmrbsycPu%2BETCr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMvC0Sbyfxzv0Xhcz6KtwD3tYUx2X8mzJOaOYE8W3UdLOyauvg1T70AKYLUHJAikKrpEsRnGDZ%2BhvXjmH0Z5Z2EUFyvaFg%2Ft9ZBEl%2F6tVImhSf3Jjh2BSAqmuV5Sr4mAJbT66sk2Cv4yCsvLFtxXSteZEFmYK0mDcm7eMd2L%2FkvshggjsmJ0MOy5BpuTqy6vgjcFgOL3VVwrPHlBAEgxg%2F8kpBectkyUgUYXrMwjoZkTQEMCQgJjiPV4UAyezRjuqC6iy77eidrJvxpN2KKHq28fqIXa9uUruaRAfCWFzB3aY62yBXFP0O5X6hqMx4yvVB1RbjzjTzmfs5U8G3aYHvlrNPNpgGPJoWXsDEC3FqFSSwXYSNvYI99F6ScQ4T3yImPGHuBxp%2FME03EQp5WL8czt972no2XeAfz9B3dBLUlNHOesCe%2FbxQ2Ijqx2V%2FBsGRB2ZmsUSl33yuEcl2Gaqh0DU%2FRuhTgRq6GfEkAwIG4wOusoyL43MMTjI2A9UlRDpiWdTcfVgCUqoNzn6IrXk8zbchhJ2IE%2FDA6FwQ0HFwCKgZSoVRqJtdgvI%2Fl5%2Fe2wxgM2d%2BuBRBuuIxK4Omp12FckkTtTHsxX4ndqRxEeWS4iwGRCpGhRlzzG%2Fg%2B%2FTnb5ousdNN0xGkAJ2flUcwgv2JvQY6pgHunakYaydloFEWxyHZNHbfWjPAw1dq0S3WhUbvOLjoPc33G5JIksgAvsefO%2FF38pn6aROF6A7c4KJWhT8EUDDmMJjD%2BoI81A9pLymlpwKJ3aU3lgYH4Y27lFTgaSaXl6tfZsLFectH0wcm7ZMnlZM2JMMi1PRCE7aOqeuuvrNZ7PrmG%2Fo%2FDRqXx5%2BY3Y%2FAdHQNF8HaL3%2Fos1Jg1fEbzCjzlLTcF5Ak&X-Amz-Signature=7f005417d1d767cf94ad144cb67ac0ee356115c2f3431d455b05f491fc8fb01c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BA3HREE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIBhPlJB8Z2FDogkbEAsh2fyW5t8QN6ZjHWBS5F7rj%2BG2AiAO7LnI8NFxYPDzRwfuHXnG1L%2FDJ1Do2FmrbsycPu%2BETCr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMvC0Sbyfxzv0Xhcz6KtwD3tYUx2X8mzJOaOYE8W3UdLOyauvg1T70AKYLUHJAikKrpEsRnGDZ%2BhvXjmH0Z5Z2EUFyvaFg%2Ft9ZBEl%2F6tVImhSf3Jjh2BSAqmuV5Sr4mAJbT66sk2Cv4yCsvLFtxXSteZEFmYK0mDcm7eMd2L%2FkvshggjsmJ0MOy5BpuTqy6vgjcFgOL3VVwrPHlBAEgxg%2F8kpBectkyUgUYXrMwjoZkTQEMCQgJjiPV4UAyezRjuqC6iy77eidrJvxpN2KKHq28fqIXa9uUruaRAfCWFzB3aY62yBXFP0O5X6hqMx4yvVB1RbjzjTzmfs5U8G3aYHvlrNPNpgGPJoWXsDEC3FqFSSwXYSNvYI99F6ScQ4T3yImPGHuBxp%2FME03EQp5WL8czt972no2XeAfz9B3dBLUlNHOesCe%2FbxQ2Ijqx2V%2FBsGRB2ZmsUSl33yuEcl2Gaqh0DU%2FRuhTgRq6GfEkAwIG4wOusoyL43MMTjI2A9UlRDpiWdTcfVgCUqoNzn6IrXk8zbchhJ2IE%2FDA6FwQ0HFwCKgZSoVRqJtdgvI%2Fl5%2Fe2wxgM2d%2BuBRBuuIxK4Omp12FckkTtTHsxX4ndqRxEeWS4iwGRCpGhRlzzG%2Fg%2B%2FTnb5ousdNN0xGkAJ2flUcwgv2JvQY6pgHunakYaydloFEWxyHZNHbfWjPAw1dq0S3WhUbvOLjoPc33G5JIksgAvsefO%2FF38pn6aROF6A7c4KJWhT8EUDDmMJjD%2BoI81A9pLymlpwKJ3aU3lgYH4Y27lFTgaSaXl6tfZsLFectH0wcm7ZMnlZM2JMMi1PRCE7aOqeuuvrNZ7PrmG%2Fo%2FDRqXx5%2BY3Y%2FAdHQNF8HaL3%2Fos1Jg1fEbzCjzlLTcF5Ak&X-Amz-Signature=a7269df59d7bc81f08c6d8b9dda729b4189b5aa29090e34f9e99f3092b7da42a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BA3HREE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIBhPlJB8Z2FDogkbEAsh2fyW5t8QN6ZjHWBS5F7rj%2BG2AiAO7LnI8NFxYPDzRwfuHXnG1L%2FDJ1Do2FmrbsycPu%2BETCr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMvC0Sbyfxzv0Xhcz6KtwD3tYUx2X8mzJOaOYE8W3UdLOyauvg1T70AKYLUHJAikKrpEsRnGDZ%2BhvXjmH0Z5Z2EUFyvaFg%2Ft9ZBEl%2F6tVImhSf3Jjh2BSAqmuV5Sr4mAJbT66sk2Cv4yCsvLFtxXSteZEFmYK0mDcm7eMd2L%2FkvshggjsmJ0MOy5BpuTqy6vgjcFgOL3VVwrPHlBAEgxg%2F8kpBectkyUgUYXrMwjoZkTQEMCQgJjiPV4UAyezRjuqC6iy77eidrJvxpN2KKHq28fqIXa9uUruaRAfCWFzB3aY62yBXFP0O5X6hqMx4yvVB1RbjzjTzmfs5U8G3aYHvlrNPNpgGPJoWXsDEC3FqFSSwXYSNvYI99F6ScQ4T3yImPGHuBxp%2FME03EQp5WL8czt972no2XeAfz9B3dBLUlNHOesCe%2FbxQ2Ijqx2V%2FBsGRB2ZmsUSl33yuEcl2Gaqh0DU%2FRuhTgRq6GfEkAwIG4wOusoyL43MMTjI2A9UlRDpiWdTcfVgCUqoNzn6IrXk8zbchhJ2IE%2FDA6FwQ0HFwCKgZSoVRqJtdgvI%2Fl5%2Fe2wxgM2d%2BuBRBuuIxK4Omp12FckkTtTHsxX4ndqRxEeWS4iwGRCpGhRlzzG%2Fg%2B%2FTnb5ousdNN0xGkAJ2flUcwgv2JvQY6pgHunakYaydloFEWxyHZNHbfWjPAw1dq0S3WhUbvOLjoPc33G5JIksgAvsefO%2FF38pn6aROF6A7c4KJWhT8EUDDmMJjD%2BoI81A9pLymlpwKJ3aU3lgYH4Y27lFTgaSaXl6tfZsLFectH0wcm7ZMnlZM2JMMi1PRCE7aOqeuuvrNZ7PrmG%2Fo%2FDRqXx5%2BY3Y%2FAdHQNF8HaL3%2Fos1Jg1fEbzCjzlLTcF5Ak&X-Amz-Signature=ecdb983f9fe8280318ef44abf33655fe7d651ad5f787bf96c30b99c32a5d1345&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BA3HREE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIBhPlJB8Z2FDogkbEAsh2fyW5t8QN6ZjHWBS5F7rj%2BG2AiAO7LnI8NFxYPDzRwfuHXnG1L%2FDJ1Do2FmrbsycPu%2BETCr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMvC0Sbyfxzv0Xhcz6KtwD3tYUx2X8mzJOaOYE8W3UdLOyauvg1T70AKYLUHJAikKrpEsRnGDZ%2BhvXjmH0Z5Z2EUFyvaFg%2Ft9ZBEl%2F6tVImhSf3Jjh2BSAqmuV5Sr4mAJbT66sk2Cv4yCsvLFtxXSteZEFmYK0mDcm7eMd2L%2FkvshggjsmJ0MOy5BpuTqy6vgjcFgOL3VVwrPHlBAEgxg%2F8kpBectkyUgUYXrMwjoZkTQEMCQgJjiPV4UAyezRjuqC6iy77eidrJvxpN2KKHq28fqIXa9uUruaRAfCWFzB3aY62yBXFP0O5X6hqMx4yvVB1RbjzjTzmfs5U8G3aYHvlrNPNpgGPJoWXsDEC3FqFSSwXYSNvYI99F6ScQ4T3yImPGHuBxp%2FME03EQp5WL8czt972no2XeAfz9B3dBLUlNHOesCe%2FbxQ2Ijqx2V%2FBsGRB2ZmsUSl33yuEcl2Gaqh0DU%2FRuhTgRq6GfEkAwIG4wOusoyL43MMTjI2A9UlRDpiWdTcfVgCUqoNzn6IrXk8zbchhJ2IE%2FDA6FwQ0HFwCKgZSoVRqJtdgvI%2Fl5%2Fe2wxgM2d%2BuBRBuuIxK4Omp12FckkTtTHsxX4ndqRxEeWS4iwGRCpGhRlzzG%2Fg%2B%2FTnb5ousdNN0xGkAJ2flUcwgv2JvQY6pgHunakYaydloFEWxyHZNHbfWjPAw1dq0S3WhUbvOLjoPc33G5JIksgAvsefO%2FF38pn6aROF6A7c4KJWhT8EUDDmMJjD%2BoI81A9pLymlpwKJ3aU3lgYH4Y27lFTgaSaXl6tfZsLFectH0wcm7ZMnlZM2JMMi1PRCE7aOqeuuvrNZ7PrmG%2Fo%2FDRqXx5%2BY3Y%2FAdHQNF8HaL3%2Fos1Jg1fEbzCjzlLTcF5Ak&X-Amz-Signature=39a114009f543472b43402731670594005d1dad28f8189aa92fdb8928c21bf1a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BA3HREE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIBhPlJB8Z2FDogkbEAsh2fyW5t8QN6ZjHWBS5F7rj%2BG2AiAO7LnI8NFxYPDzRwfuHXnG1L%2FDJ1Do2FmrbsycPu%2BETCr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMvC0Sbyfxzv0Xhcz6KtwD3tYUx2X8mzJOaOYE8W3UdLOyauvg1T70AKYLUHJAikKrpEsRnGDZ%2BhvXjmH0Z5Z2EUFyvaFg%2Ft9ZBEl%2F6tVImhSf3Jjh2BSAqmuV5Sr4mAJbT66sk2Cv4yCsvLFtxXSteZEFmYK0mDcm7eMd2L%2FkvshggjsmJ0MOy5BpuTqy6vgjcFgOL3VVwrPHlBAEgxg%2F8kpBectkyUgUYXrMwjoZkTQEMCQgJjiPV4UAyezRjuqC6iy77eidrJvxpN2KKHq28fqIXa9uUruaRAfCWFzB3aY62yBXFP0O5X6hqMx4yvVB1RbjzjTzmfs5U8G3aYHvlrNPNpgGPJoWXsDEC3FqFSSwXYSNvYI99F6ScQ4T3yImPGHuBxp%2FME03EQp5WL8czt972no2XeAfz9B3dBLUlNHOesCe%2FbxQ2Ijqx2V%2FBsGRB2ZmsUSl33yuEcl2Gaqh0DU%2FRuhTgRq6GfEkAwIG4wOusoyL43MMTjI2A9UlRDpiWdTcfVgCUqoNzn6IrXk8zbchhJ2IE%2FDA6FwQ0HFwCKgZSoVRqJtdgvI%2Fl5%2Fe2wxgM2d%2BuBRBuuIxK4Omp12FckkTtTHsxX4ndqRxEeWS4iwGRCpGhRlzzG%2Fg%2B%2FTnb5ousdNN0xGkAJ2flUcwgv2JvQY6pgHunakYaydloFEWxyHZNHbfWjPAw1dq0S3WhUbvOLjoPc33G5JIksgAvsefO%2FF38pn6aROF6A7c4KJWhT8EUDDmMJjD%2BoI81A9pLymlpwKJ3aU3lgYH4Y27lFTgaSaXl6tfZsLFectH0wcm7ZMnlZM2JMMi1PRCE7aOqeuuvrNZ7PrmG%2Fo%2FDRqXx5%2BY3Y%2FAdHQNF8HaL3%2Fos1Jg1fEbzCjzlLTcF5Ak&X-Amz-Signature=3c105003e22ce08392ddf4bfe35b4e0d5c0daaec5f9d2ad7f05c5b6bd735c001&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLVN2ZUB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIGJRSdoB2Yg46NyxuAGzls2pYNcrkMiZ3x1P0%2FnZnzNTAiEAtjLsct5q9hTbADOhUgmNW5J8udjZoF3HddySbEBWxkEq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBNq9TnTfRRID30DtSrcA5tMHjJ4rfolGZgLMTzDZgN5MlOBUwIaIKGUqkUD8YbWr8DVBnIB7eJhY8cXrxc2%2FfQYNpwiQ%2FvynD0rFHzj%2B1BiRWqLWfEhux7iQSFemZxn3dZPKboKGCoKWe4BEqXNU27KSn2hyPnMIPDz%2FDrGhzAropJDKreAg%2FfP6v4P4QTEXbyS%2BQNRrBOrCSTXKupTpY2jD0Ra9H7CnxuCK5h%2BWMBPzSX8R3Pt8GIutGhVB9Hfs8TN4vuMckN7%2FMf6bH%2B%2FQX60JVLhpWnfwL94Y%2B71ZHbucivdyWWyzwZF4fABcQcX0nLZZKhrNaNaBQA%2FCEKGvRi5NzYwoz2WZDW5hFNqbMHUsawiYY%2B%2BBCvjDazqkg2%2Biy489QZU%2Bdmipy%2FooEccL4ZxrsSoqQysW4fUe6dq%2FkW%2F7ciQUQlQwcdMUQt92uNHixJBfr6Fa7%2F%2Fi49hegiDqlTbULki6%2F5RAYpIHyCbo9jKjmyU%2FCXPotWNkI40S1u4YPR04CreJpvJeF62rIXZa4nNOOM52d4%2FD8VwF46aBJZdLdxjdhYdw7%2B0N3WCRPay9VweXaFmIOII5QyEj0%2FChb%2Fgatw3gSmFz6ESN1Mxnn7e1UXM4%2F%2F4Pc08x%2FfhLx%2FmIQ6TRZfyXSm1OR5AMMj9ib0GOqUB2Nu6gXlzdykg5LmuWYD5JfGLo67qEtsCaNoLrU7wqNp0FhqwbatiYiCO2MCZ61xySRkAqC8UBI7H8M%2BjrkCbS51mxoLhlBESQBnuiEMvQaa0dk9HFx%2BznJ6BSpQuJQWIZPvMsnvUbwhEWC4XcR%2F0leGExEG12UPKtToiWuhCNmdYtPvEOWD4%2BEzj4HwKMOhlgJpl0WhiODNRrjYyFqHiPHcc4JU%2F&X-Amz-Signature=2f122a02fdd39f61628761060b707d58f3a814046418b385e4050da933ea8863&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLVN2ZUB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIGJRSdoB2Yg46NyxuAGzls2pYNcrkMiZ3x1P0%2FnZnzNTAiEAtjLsct5q9hTbADOhUgmNW5J8udjZoF3HddySbEBWxkEq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBNq9TnTfRRID30DtSrcA5tMHjJ4rfolGZgLMTzDZgN5MlOBUwIaIKGUqkUD8YbWr8DVBnIB7eJhY8cXrxc2%2FfQYNpwiQ%2FvynD0rFHzj%2B1BiRWqLWfEhux7iQSFemZxn3dZPKboKGCoKWe4BEqXNU27KSn2hyPnMIPDz%2FDrGhzAropJDKreAg%2FfP6v4P4QTEXbyS%2BQNRrBOrCSTXKupTpY2jD0Ra9H7CnxuCK5h%2BWMBPzSX8R3Pt8GIutGhVB9Hfs8TN4vuMckN7%2FMf6bH%2B%2FQX60JVLhpWnfwL94Y%2B71ZHbucivdyWWyzwZF4fABcQcX0nLZZKhrNaNaBQA%2FCEKGvRi5NzYwoz2WZDW5hFNqbMHUsawiYY%2B%2BBCvjDazqkg2%2Biy489QZU%2Bdmipy%2FooEccL4ZxrsSoqQysW4fUe6dq%2FkW%2F7ciQUQlQwcdMUQt92uNHixJBfr6Fa7%2F%2Fi49hegiDqlTbULki6%2F5RAYpIHyCbo9jKjmyU%2FCXPotWNkI40S1u4YPR04CreJpvJeF62rIXZa4nNOOM52d4%2FD8VwF46aBJZdLdxjdhYdw7%2B0N3WCRPay9VweXaFmIOII5QyEj0%2FChb%2Fgatw3gSmFz6ESN1Mxnn7e1UXM4%2F%2F4Pc08x%2FfhLx%2FmIQ6TRZfyXSm1OR5AMMj9ib0GOqUB2Nu6gXlzdykg5LmuWYD5JfGLo67qEtsCaNoLrU7wqNp0FhqwbatiYiCO2MCZ61xySRkAqC8UBI7H8M%2BjrkCbS51mxoLhlBESQBnuiEMvQaa0dk9HFx%2BznJ6BSpQuJQWIZPvMsnvUbwhEWC4XcR%2F0leGExEG12UPKtToiWuhCNmdYtPvEOWD4%2BEzj4HwKMOhlgJpl0WhiODNRrjYyFqHiPHcc4JU%2F&X-Amz-Signature=662c91bebff7550fa9d3299d337a9db8e08f9ffcbb4e7ba80b90627b2290926a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLVN2ZUB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIGJRSdoB2Yg46NyxuAGzls2pYNcrkMiZ3x1P0%2FnZnzNTAiEAtjLsct5q9hTbADOhUgmNW5J8udjZoF3HddySbEBWxkEq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBNq9TnTfRRID30DtSrcA5tMHjJ4rfolGZgLMTzDZgN5MlOBUwIaIKGUqkUD8YbWr8DVBnIB7eJhY8cXrxc2%2FfQYNpwiQ%2FvynD0rFHzj%2B1BiRWqLWfEhux7iQSFemZxn3dZPKboKGCoKWe4BEqXNU27KSn2hyPnMIPDz%2FDrGhzAropJDKreAg%2FfP6v4P4QTEXbyS%2BQNRrBOrCSTXKupTpY2jD0Ra9H7CnxuCK5h%2BWMBPzSX8R3Pt8GIutGhVB9Hfs8TN4vuMckN7%2FMf6bH%2B%2FQX60JVLhpWnfwL94Y%2B71ZHbucivdyWWyzwZF4fABcQcX0nLZZKhrNaNaBQA%2FCEKGvRi5NzYwoz2WZDW5hFNqbMHUsawiYY%2B%2BBCvjDazqkg2%2Biy489QZU%2Bdmipy%2FooEccL4ZxrsSoqQysW4fUe6dq%2FkW%2F7ciQUQlQwcdMUQt92uNHixJBfr6Fa7%2F%2Fi49hegiDqlTbULki6%2F5RAYpIHyCbo9jKjmyU%2FCXPotWNkI40S1u4YPR04CreJpvJeF62rIXZa4nNOOM52d4%2FD8VwF46aBJZdLdxjdhYdw7%2B0N3WCRPay9VweXaFmIOII5QyEj0%2FChb%2Fgatw3gSmFz6ESN1Mxnn7e1UXM4%2F%2F4Pc08x%2FfhLx%2FmIQ6TRZfyXSm1OR5AMMj9ib0GOqUB2Nu6gXlzdykg5LmuWYD5JfGLo67qEtsCaNoLrU7wqNp0FhqwbatiYiCO2MCZ61xySRkAqC8UBI7H8M%2BjrkCbS51mxoLhlBESQBnuiEMvQaa0dk9HFx%2BznJ6BSpQuJQWIZPvMsnvUbwhEWC4XcR%2F0leGExEG12UPKtToiWuhCNmdYtPvEOWD4%2BEzj4HwKMOhlgJpl0WhiODNRrjYyFqHiPHcc4JU%2F&X-Amz-Signature=0ef6dcb9db0776266b7c77e5dc3f42a0fc85d3632fafc8afea66b695ae5959b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLVN2ZUB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIGJRSdoB2Yg46NyxuAGzls2pYNcrkMiZ3x1P0%2FnZnzNTAiEAtjLsct5q9hTbADOhUgmNW5J8udjZoF3HddySbEBWxkEq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBNq9TnTfRRID30DtSrcA5tMHjJ4rfolGZgLMTzDZgN5MlOBUwIaIKGUqkUD8YbWr8DVBnIB7eJhY8cXrxc2%2FfQYNpwiQ%2FvynD0rFHzj%2B1BiRWqLWfEhux7iQSFemZxn3dZPKboKGCoKWe4BEqXNU27KSn2hyPnMIPDz%2FDrGhzAropJDKreAg%2FfP6v4P4QTEXbyS%2BQNRrBOrCSTXKupTpY2jD0Ra9H7CnxuCK5h%2BWMBPzSX8R3Pt8GIutGhVB9Hfs8TN4vuMckN7%2FMf6bH%2B%2FQX60JVLhpWnfwL94Y%2B71ZHbucivdyWWyzwZF4fABcQcX0nLZZKhrNaNaBQA%2FCEKGvRi5NzYwoz2WZDW5hFNqbMHUsawiYY%2B%2BBCvjDazqkg2%2Biy489QZU%2Bdmipy%2FooEccL4ZxrsSoqQysW4fUe6dq%2FkW%2F7ciQUQlQwcdMUQt92uNHixJBfr6Fa7%2F%2Fi49hegiDqlTbULki6%2F5RAYpIHyCbo9jKjmyU%2FCXPotWNkI40S1u4YPR04CreJpvJeF62rIXZa4nNOOM52d4%2FD8VwF46aBJZdLdxjdhYdw7%2B0N3WCRPay9VweXaFmIOII5QyEj0%2FChb%2Fgatw3gSmFz6ESN1Mxnn7e1UXM4%2F%2F4Pc08x%2FfhLx%2FmIQ6TRZfyXSm1OR5AMMj9ib0GOqUB2Nu6gXlzdykg5LmuWYD5JfGLo67qEtsCaNoLrU7wqNp0FhqwbatiYiCO2MCZ61xySRkAqC8UBI7H8M%2BjrkCbS51mxoLhlBESQBnuiEMvQaa0dk9HFx%2BznJ6BSpQuJQWIZPvMsnvUbwhEWC4XcR%2F0leGExEG12UPKtToiWuhCNmdYtPvEOWD4%2BEzj4HwKMOhlgJpl0WhiODNRrjYyFqHiPHcc4JU%2F&X-Amz-Signature=b7347f50080d07bb6b3ff08d8b9c019a471fe1051262924aa2a2887323b260a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLVN2ZUB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIGJRSdoB2Yg46NyxuAGzls2pYNcrkMiZ3x1P0%2FnZnzNTAiEAtjLsct5q9hTbADOhUgmNW5J8udjZoF3HddySbEBWxkEq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBNq9TnTfRRID30DtSrcA5tMHjJ4rfolGZgLMTzDZgN5MlOBUwIaIKGUqkUD8YbWr8DVBnIB7eJhY8cXrxc2%2FfQYNpwiQ%2FvynD0rFHzj%2B1BiRWqLWfEhux7iQSFemZxn3dZPKboKGCoKWe4BEqXNU27KSn2hyPnMIPDz%2FDrGhzAropJDKreAg%2FfP6v4P4QTEXbyS%2BQNRrBOrCSTXKupTpY2jD0Ra9H7CnxuCK5h%2BWMBPzSX8R3Pt8GIutGhVB9Hfs8TN4vuMckN7%2FMf6bH%2B%2FQX60JVLhpWnfwL94Y%2B71ZHbucivdyWWyzwZF4fABcQcX0nLZZKhrNaNaBQA%2FCEKGvRi5NzYwoz2WZDW5hFNqbMHUsawiYY%2B%2BBCvjDazqkg2%2Biy489QZU%2Bdmipy%2FooEccL4ZxrsSoqQysW4fUe6dq%2FkW%2F7ciQUQlQwcdMUQt92uNHixJBfr6Fa7%2F%2Fi49hegiDqlTbULki6%2F5RAYpIHyCbo9jKjmyU%2FCXPotWNkI40S1u4YPR04CreJpvJeF62rIXZa4nNOOM52d4%2FD8VwF46aBJZdLdxjdhYdw7%2B0N3WCRPay9VweXaFmIOII5QyEj0%2FChb%2Fgatw3gSmFz6ESN1Mxnn7e1UXM4%2F%2F4Pc08x%2FfhLx%2FmIQ6TRZfyXSm1OR5AMMj9ib0GOqUB2Nu6gXlzdykg5LmuWYD5JfGLo67qEtsCaNoLrU7wqNp0FhqwbatiYiCO2MCZ61xySRkAqC8UBI7H8M%2BjrkCbS51mxoLhlBESQBnuiEMvQaa0dk9HFx%2BznJ6BSpQuJQWIZPvMsnvUbwhEWC4XcR%2F0leGExEG12UPKtToiWuhCNmdYtPvEOWD4%2BEzj4HwKMOhlgJpl0WhiODNRrjYyFqHiPHcc4JU%2F&X-Amz-Signature=e2c57a0f0e360d6c63360e22dbb3838a5b8c3fc0a393b20f142b14e594e04359&X-Amz-SignedHeaders=host&x-id=GetObject)
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


