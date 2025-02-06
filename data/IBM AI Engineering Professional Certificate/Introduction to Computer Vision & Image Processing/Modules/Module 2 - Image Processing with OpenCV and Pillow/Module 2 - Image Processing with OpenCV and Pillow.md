

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCPZA3ZB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDApyZV5kOs4rzJD%2Fy8DqgCKBHUK7AK5CnTMSAvoPCCHQIgFKWxHbAKx1dixcFpMJzvx%2F0XiKs%2FqDSyv3V%2BlS1SvPcq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDO0L5%2FFW%2F56gOT1fJircA0JskgsXaxJ88Ro0GX4OwvtJlpuBHMr5N2Ot2fQdyk343S0WasltUMeub5ZfExgKIJoES3WiMRwYXHB%2FFGKJS3yQOC5UbV%2FyCxMDn0O4oAF8fCDnQAMughKghk%2FhxsLg0gPiHurZt7zuHhU6uiyQR9OT84MLQXeKpDT68wrSZp8mHN4xOXIOn7xl%2FhPX2v9%2B7TeW%2FsqDCHqymucg94Gqt3uaz4YctmIoad%2BFu939sWqMMCp%2FPi%2F9buCswHobeObqBt%2FIkINhsljNwy9behEWJ7cN2Ds1PKBfd%2FaItCNCSmlr4zHPhHKO0M%2Bs6mkgMzQGSv%2FikpoJi9UAswOYVX1qQ4nLVnYRwUCHBbXPtVv%2FfrWx4l%2F3VWHsklXPBGAEO88pGE26J9CwkJ7sgWOWrGozaAExD3Z62hP%2Bthl8i%2FiTy0mvD0GO59z1GPoyX5EBEY25JreWkYDBMNX3jPvwCz%2ByvzwQ1fUfC2ypWETLu13zN1L1SDuib1tCCxQA9E%2F28luuBPXUtK7sO0JKHuo2JYsz8W7Nqni4BrQZ6SBN9P%2FfkxBjQExcVwxR4A%2BLU%2FRDUP%2BbUGAbEge5ZJoZTqW%2F8s1zUjTj5nQeiIol99HXNGovvXGkQJ%2FdmVb9WmG8s8zIMMb9lL0GOqUB18zMSxjFNitvIOSFnkelt%2FYNjQyCTyrrh3Bmoukp3%2B7u2fhEQK58CkBLNP1jjsgJi3faRpDoXmEVayhnpremtwGlWNE%2FoBd7LKnf7f33SNEkswjA5sfEuXpAnkD7xMCFeb%2B%2BQHCvppMiNqU%2F9IqXw%2F1QF7qp5rEHl4%2F1RzT1E6qxM10EfTSTedkf5ncNNCb3sveVValTSEz8avRN07c%2BYPE%2BqS5D&X-Amz-Signature=6f53c27f0ed42d95e52513ac251564e0ad351b21bf9bc143800a1215451654a7&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YEVMWW7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIFTuQVErZaL2323Nycmrp%2FeA2dC3MfmlK2%2FAX8P2KxZYAiA%2FkFwuWm8%2FC5a8%2BmFQ94GGsECgU45nQQjub3PUSKKipCr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMM2IPE%2F1EAb5i%2BNc9KtwDC8VwtugPZWMqZOksK1UO%2FZAawjPH3oONgHLwgS0BWnRjXmbvyyr3ryhaF6dKA1%2FDS3P%2By%2FnAT9aNKDkAouYw9WaA2AUDpuZuqlpZ7E9FJplOtnHwGqNRfk4v4LPELuyPAAJKjpJzedQZFSebsSYXWZiav2jmzlVtQexyJF2HL6jWjwZc5OTwU291PHOE5BHd9j0kBxu%2FtObh7WyU9RBz7TkETHOPWoHbVvXIU5nC8TB0O1E%2Fn1uN7QpMXm5TuQJ%2FTaFIkHtmGxD0GfYm6ftVfPfhiVXLINdenDLtXEvUMRfd5lFQVJI2%2BY5ukLLviXBAa2knd3ArecETDXclhb5LKRE7NlUlNYQ5fHwU5Lsk2k1Lt5vC1UZMHwnriYzxmhSzlWGc%2Fakwv2jgXxkh5dkEh4EJkgU2YDM1M1H88BoGRWlkvaOEzoOtX6tcnN0JpDqAnVYglZ1Zinc4jfr1S2Mv39e%2FYAXDRKmp%2BJeN1T%2FfL87DofJfqhGVrfzT1m63cwC70OmrAAWTe80E6a4Vo4DEKtNXXh%2FtqZh5OvDmnLHX45FnLwpnB2oZ6t0ith0OKvecbh3pLvVgP0%2BXcU7WFp7a5Sc9j12jZzxc8V9dgY45a7wE116ZgJdGAtZi0powi%2F2UvQY6pgGHT7QpizzcnEIzvi5Afka3exL14Y8JCgJtqe9yKpDCjOJWsHAdCyXR%2FFzS%2BuNp3Bp3EZ2qMnjClFTaHaooUGwN5X8ZBJpDI4soFW0F3WSk3Mn1od70QtKvSvT2uf%2Fxy5a7ettkXFRV4cSJFk18H4hhm8ysYiO4KUH9aXgQsKm%2Bhl4GjSl7Yww01gFuSpmBgsZ3HvkDvSbVxqrhGhLodVv0icJFMaSr&X-Amz-Signature=6b36109366662f5882b3ead79be6e54e12702552a6891dd136572cc50fff36a1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YEVMWW7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIFTuQVErZaL2323Nycmrp%2FeA2dC3MfmlK2%2FAX8P2KxZYAiA%2FkFwuWm8%2FC5a8%2BmFQ94GGsECgU45nQQjub3PUSKKipCr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMM2IPE%2F1EAb5i%2BNc9KtwDC8VwtugPZWMqZOksK1UO%2FZAawjPH3oONgHLwgS0BWnRjXmbvyyr3ryhaF6dKA1%2FDS3P%2By%2FnAT9aNKDkAouYw9WaA2AUDpuZuqlpZ7E9FJplOtnHwGqNRfk4v4LPELuyPAAJKjpJzedQZFSebsSYXWZiav2jmzlVtQexyJF2HL6jWjwZc5OTwU291PHOE5BHd9j0kBxu%2FtObh7WyU9RBz7TkETHOPWoHbVvXIU5nC8TB0O1E%2Fn1uN7QpMXm5TuQJ%2FTaFIkHtmGxD0GfYm6ftVfPfhiVXLINdenDLtXEvUMRfd5lFQVJI2%2BY5ukLLviXBAa2knd3ArecETDXclhb5LKRE7NlUlNYQ5fHwU5Lsk2k1Lt5vC1UZMHwnriYzxmhSzlWGc%2Fakwv2jgXxkh5dkEh4EJkgU2YDM1M1H88BoGRWlkvaOEzoOtX6tcnN0JpDqAnVYglZ1Zinc4jfr1S2Mv39e%2FYAXDRKmp%2BJeN1T%2FfL87DofJfqhGVrfzT1m63cwC70OmrAAWTe80E6a4Vo4DEKtNXXh%2FtqZh5OvDmnLHX45FnLwpnB2oZ6t0ith0OKvecbh3pLvVgP0%2BXcU7WFp7a5Sc9j12jZzxc8V9dgY45a7wE116ZgJdGAtZi0powi%2F2UvQY6pgGHT7QpizzcnEIzvi5Afka3exL14Y8JCgJtqe9yKpDCjOJWsHAdCyXR%2FFzS%2BuNp3Bp3EZ2qMnjClFTaHaooUGwN5X8ZBJpDI4soFW0F3WSk3Mn1od70QtKvSvT2uf%2Fxy5a7ettkXFRV4cSJFk18H4hhm8ysYiO4KUH9aXgQsKm%2Bhl4GjSl7Yww01gFuSpmBgsZ3HvkDvSbVxqrhGhLodVv0icJFMaSr&X-Amz-Signature=ff11997c8758d469fba3d56e685ac3e2bf7d2017128533366d71b9d0b580d899&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YEVMWW7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIFTuQVErZaL2323Nycmrp%2FeA2dC3MfmlK2%2FAX8P2KxZYAiA%2FkFwuWm8%2FC5a8%2BmFQ94GGsECgU45nQQjub3PUSKKipCr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMM2IPE%2F1EAb5i%2BNc9KtwDC8VwtugPZWMqZOksK1UO%2FZAawjPH3oONgHLwgS0BWnRjXmbvyyr3ryhaF6dKA1%2FDS3P%2By%2FnAT9aNKDkAouYw9WaA2AUDpuZuqlpZ7E9FJplOtnHwGqNRfk4v4LPELuyPAAJKjpJzedQZFSebsSYXWZiav2jmzlVtQexyJF2HL6jWjwZc5OTwU291PHOE5BHd9j0kBxu%2FtObh7WyU9RBz7TkETHOPWoHbVvXIU5nC8TB0O1E%2Fn1uN7QpMXm5TuQJ%2FTaFIkHtmGxD0GfYm6ftVfPfhiVXLINdenDLtXEvUMRfd5lFQVJI2%2BY5ukLLviXBAa2knd3ArecETDXclhb5LKRE7NlUlNYQ5fHwU5Lsk2k1Lt5vC1UZMHwnriYzxmhSzlWGc%2Fakwv2jgXxkh5dkEh4EJkgU2YDM1M1H88BoGRWlkvaOEzoOtX6tcnN0JpDqAnVYglZ1Zinc4jfr1S2Mv39e%2FYAXDRKmp%2BJeN1T%2FfL87DofJfqhGVrfzT1m63cwC70OmrAAWTe80E6a4Vo4DEKtNXXh%2FtqZh5OvDmnLHX45FnLwpnB2oZ6t0ith0OKvecbh3pLvVgP0%2BXcU7WFp7a5Sc9j12jZzxc8V9dgY45a7wE116ZgJdGAtZi0powi%2F2UvQY6pgGHT7QpizzcnEIzvi5Afka3exL14Y8JCgJtqe9yKpDCjOJWsHAdCyXR%2FFzS%2BuNp3Bp3EZ2qMnjClFTaHaooUGwN5X8ZBJpDI4soFW0F3WSk3Mn1od70QtKvSvT2uf%2Fxy5a7ettkXFRV4cSJFk18H4hhm8ysYiO4KUH9aXgQsKm%2Bhl4GjSl7Yww01gFuSpmBgsZ3HvkDvSbVxqrhGhLodVv0icJFMaSr&X-Amz-Signature=ca43f07eb7c2e26843cad9a9895ea31389b2e44189949765e4aa08d3cfa35f41&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YEVMWW7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIFTuQVErZaL2323Nycmrp%2FeA2dC3MfmlK2%2FAX8P2KxZYAiA%2FkFwuWm8%2FC5a8%2BmFQ94GGsECgU45nQQjub3PUSKKipCr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMM2IPE%2F1EAb5i%2BNc9KtwDC8VwtugPZWMqZOksK1UO%2FZAawjPH3oONgHLwgS0BWnRjXmbvyyr3ryhaF6dKA1%2FDS3P%2By%2FnAT9aNKDkAouYw9WaA2AUDpuZuqlpZ7E9FJplOtnHwGqNRfk4v4LPELuyPAAJKjpJzedQZFSebsSYXWZiav2jmzlVtQexyJF2HL6jWjwZc5OTwU291PHOE5BHd9j0kBxu%2FtObh7WyU9RBz7TkETHOPWoHbVvXIU5nC8TB0O1E%2Fn1uN7QpMXm5TuQJ%2FTaFIkHtmGxD0GfYm6ftVfPfhiVXLINdenDLtXEvUMRfd5lFQVJI2%2BY5ukLLviXBAa2knd3ArecETDXclhb5LKRE7NlUlNYQ5fHwU5Lsk2k1Lt5vC1UZMHwnriYzxmhSzlWGc%2Fakwv2jgXxkh5dkEh4EJkgU2YDM1M1H88BoGRWlkvaOEzoOtX6tcnN0JpDqAnVYglZ1Zinc4jfr1S2Mv39e%2FYAXDRKmp%2BJeN1T%2FfL87DofJfqhGVrfzT1m63cwC70OmrAAWTe80E6a4Vo4DEKtNXXh%2FtqZh5OvDmnLHX45FnLwpnB2oZ6t0ith0OKvecbh3pLvVgP0%2BXcU7WFp7a5Sc9j12jZzxc8V9dgY45a7wE116ZgJdGAtZi0powi%2F2UvQY6pgGHT7QpizzcnEIzvi5Afka3exL14Y8JCgJtqe9yKpDCjOJWsHAdCyXR%2FFzS%2BuNp3Bp3EZ2qMnjClFTaHaooUGwN5X8ZBJpDI4soFW0F3WSk3Mn1od70QtKvSvT2uf%2Fxy5a7ettkXFRV4cSJFk18H4hhm8ysYiO4KUH9aXgQsKm%2Bhl4GjSl7Yww01gFuSpmBgsZ3HvkDvSbVxqrhGhLodVv0icJFMaSr&X-Amz-Signature=75bd90a28a4bdb49fa7dcbe0e6ffd3a5f21b8ef66f80387dd8539ba211ad4b5b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YEVMWW7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIFTuQVErZaL2323Nycmrp%2FeA2dC3MfmlK2%2FAX8P2KxZYAiA%2FkFwuWm8%2FC5a8%2BmFQ94GGsECgU45nQQjub3PUSKKipCr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMM2IPE%2F1EAb5i%2BNc9KtwDC8VwtugPZWMqZOksK1UO%2FZAawjPH3oONgHLwgS0BWnRjXmbvyyr3ryhaF6dKA1%2FDS3P%2By%2FnAT9aNKDkAouYw9WaA2AUDpuZuqlpZ7E9FJplOtnHwGqNRfk4v4LPELuyPAAJKjpJzedQZFSebsSYXWZiav2jmzlVtQexyJF2HL6jWjwZc5OTwU291PHOE5BHd9j0kBxu%2FtObh7WyU9RBz7TkETHOPWoHbVvXIU5nC8TB0O1E%2Fn1uN7QpMXm5TuQJ%2FTaFIkHtmGxD0GfYm6ftVfPfhiVXLINdenDLtXEvUMRfd5lFQVJI2%2BY5ukLLviXBAa2knd3ArecETDXclhb5LKRE7NlUlNYQ5fHwU5Lsk2k1Lt5vC1UZMHwnriYzxmhSzlWGc%2Fakwv2jgXxkh5dkEh4EJkgU2YDM1M1H88BoGRWlkvaOEzoOtX6tcnN0JpDqAnVYglZ1Zinc4jfr1S2Mv39e%2FYAXDRKmp%2BJeN1T%2FfL87DofJfqhGVrfzT1m63cwC70OmrAAWTe80E6a4Vo4DEKtNXXh%2FtqZh5OvDmnLHX45FnLwpnB2oZ6t0ith0OKvecbh3pLvVgP0%2BXcU7WFp7a5Sc9j12jZzxc8V9dgY45a7wE116ZgJdGAtZi0powi%2F2UvQY6pgGHT7QpizzcnEIzvi5Afka3exL14Y8JCgJtqe9yKpDCjOJWsHAdCyXR%2FFzS%2BuNp3Bp3EZ2qMnjClFTaHaooUGwN5X8ZBJpDI4soFW0F3WSk3Mn1od70QtKvSvT2uf%2Fxy5a7ettkXFRV4cSJFk18H4hhm8ysYiO4KUH9aXgQsKm%2Bhl4GjSl7Yww01gFuSpmBgsZ3HvkDvSbVxqrhGhLodVv0icJFMaSr&X-Amz-Signature=74bdbe990805a5bb8ff566ad53ef434a075a1d330b4d94d62c1e6305902f33e4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCPZA3ZB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDApyZV5kOs4rzJD%2Fy8DqgCKBHUK7AK5CnTMSAvoPCCHQIgFKWxHbAKx1dixcFpMJzvx%2F0XiKs%2FqDSyv3V%2BlS1SvPcq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDO0L5%2FFW%2F56gOT1fJircA0JskgsXaxJ88Ro0GX4OwvtJlpuBHMr5N2Ot2fQdyk343S0WasltUMeub5ZfExgKIJoES3WiMRwYXHB%2FFGKJS3yQOC5UbV%2FyCxMDn0O4oAF8fCDnQAMughKghk%2FhxsLg0gPiHurZt7zuHhU6uiyQR9OT84MLQXeKpDT68wrSZp8mHN4xOXIOn7xl%2FhPX2v9%2B7TeW%2FsqDCHqymucg94Gqt3uaz4YctmIoad%2BFu939sWqMMCp%2FPi%2F9buCswHobeObqBt%2FIkINhsljNwy9behEWJ7cN2Ds1PKBfd%2FaItCNCSmlr4zHPhHKO0M%2Bs6mkgMzQGSv%2FikpoJi9UAswOYVX1qQ4nLVnYRwUCHBbXPtVv%2FfrWx4l%2F3VWHsklXPBGAEO88pGE26J9CwkJ7sgWOWrGozaAExD3Z62hP%2Bthl8i%2FiTy0mvD0GO59z1GPoyX5EBEY25JreWkYDBMNX3jPvwCz%2ByvzwQ1fUfC2ypWETLu13zN1L1SDuib1tCCxQA9E%2F28luuBPXUtK7sO0JKHuo2JYsz8W7Nqni4BrQZ6SBN9P%2FfkxBjQExcVwxR4A%2BLU%2FRDUP%2BbUGAbEge5ZJoZTqW%2F8s1zUjTj5nQeiIol99HXNGovvXGkQJ%2FdmVb9WmG8s8zIMMb9lL0GOqUB18zMSxjFNitvIOSFnkelt%2FYNjQyCTyrrh3Bmoukp3%2B7u2fhEQK58CkBLNP1jjsgJi3faRpDoXmEVayhnpremtwGlWNE%2FoBd7LKnf7f33SNEkswjA5sfEuXpAnkD7xMCFeb%2B%2BQHCvppMiNqU%2F9IqXw%2F1QF7qp5rEHl4%2F1RzT1E6qxM10EfTSTedkf5ncNNCb3sveVValTSEz8avRN07c%2BYPE%2BqS5D&X-Amz-Signature=53b4e1671e9c564d49a3f528b0b141f1f37f223b474469162e4a7a6c03cb058b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCPZA3ZB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDApyZV5kOs4rzJD%2Fy8DqgCKBHUK7AK5CnTMSAvoPCCHQIgFKWxHbAKx1dixcFpMJzvx%2F0XiKs%2FqDSyv3V%2BlS1SvPcq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDO0L5%2FFW%2F56gOT1fJircA0JskgsXaxJ88Ro0GX4OwvtJlpuBHMr5N2Ot2fQdyk343S0WasltUMeub5ZfExgKIJoES3WiMRwYXHB%2FFGKJS3yQOC5UbV%2FyCxMDn0O4oAF8fCDnQAMughKghk%2FhxsLg0gPiHurZt7zuHhU6uiyQR9OT84MLQXeKpDT68wrSZp8mHN4xOXIOn7xl%2FhPX2v9%2B7TeW%2FsqDCHqymucg94Gqt3uaz4YctmIoad%2BFu939sWqMMCp%2FPi%2F9buCswHobeObqBt%2FIkINhsljNwy9behEWJ7cN2Ds1PKBfd%2FaItCNCSmlr4zHPhHKO0M%2Bs6mkgMzQGSv%2FikpoJi9UAswOYVX1qQ4nLVnYRwUCHBbXPtVv%2FfrWx4l%2F3VWHsklXPBGAEO88pGE26J9CwkJ7sgWOWrGozaAExD3Z62hP%2Bthl8i%2FiTy0mvD0GO59z1GPoyX5EBEY25JreWkYDBMNX3jPvwCz%2ByvzwQ1fUfC2ypWETLu13zN1L1SDuib1tCCxQA9E%2F28luuBPXUtK7sO0JKHuo2JYsz8W7Nqni4BrQZ6SBN9P%2FfkxBjQExcVwxR4A%2BLU%2FRDUP%2BbUGAbEge5ZJoZTqW%2F8s1zUjTj5nQeiIol99HXNGovvXGkQJ%2FdmVb9WmG8s8zIMMb9lL0GOqUB18zMSxjFNitvIOSFnkelt%2FYNjQyCTyrrh3Bmoukp3%2B7u2fhEQK58CkBLNP1jjsgJi3faRpDoXmEVayhnpremtwGlWNE%2FoBd7LKnf7f33SNEkswjA5sfEuXpAnkD7xMCFeb%2B%2BQHCvppMiNqU%2F9IqXw%2F1QF7qp5rEHl4%2F1RzT1E6qxM10EfTSTedkf5ncNNCb3sveVValTSEz8avRN07c%2BYPE%2BqS5D&X-Amz-Signature=1778b027d8d04dcea419cf38ef180b37c8e2e01e1ef30ff4af76fe3bfabd2394&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCPZA3ZB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDApyZV5kOs4rzJD%2Fy8DqgCKBHUK7AK5CnTMSAvoPCCHQIgFKWxHbAKx1dixcFpMJzvx%2F0XiKs%2FqDSyv3V%2BlS1SvPcq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDO0L5%2FFW%2F56gOT1fJircA0JskgsXaxJ88Ro0GX4OwvtJlpuBHMr5N2Ot2fQdyk343S0WasltUMeub5ZfExgKIJoES3WiMRwYXHB%2FFGKJS3yQOC5UbV%2FyCxMDn0O4oAF8fCDnQAMughKghk%2FhxsLg0gPiHurZt7zuHhU6uiyQR9OT84MLQXeKpDT68wrSZp8mHN4xOXIOn7xl%2FhPX2v9%2B7TeW%2FsqDCHqymucg94Gqt3uaz4YctmIoad%2BFu939sWqMMCp%2FPi%2F9buCswHobeObqBt%2FIkINhsljNwy9behEWJ7cN2Ds1PKBfd%2FaItCNCSmlr4zHPhHKO0M%2Bs6mkgMzQGSv%2FikpoJi9UAswOYVX1qQ4nLVnYRwUCHBbXPtVv%2FfrWx4l%2F3VWHsklXPBGAEO88pGE26J9CwkJ7sgWOWrGozaAExD3Z62hP%2Bthl8i%2FiTy0mvD0GO59z1GPoyX5EBEY25JreWkYDBMNX3jPvwCz%2ByvzwQ1fUfC2ypWETLu13zN1L1SDuib1tCCxQA9E%2F28luuBPXUtK7sO0JKHuo2JYsz8W7Nqni4BrQZ6SBN9P%2FfkxBjQExcVwxR4A%2BLU%2FRDUP%2BbUGAbEge5ZJoZTqW%2F8s1zUjTj5nQeiIol99HXNGovvXGkQJ%2FdmVb9WmG8s8zIMMb9lL0GOqUB18zMSxjFNitvIOSFnkelt%2FYNjQyCTyrrh3Bmoukp3%2B7u2fhEQK58CkBLNP1jjsgJi3faRpDoXmEVayhnpremtwGlWNE%2FoBd7LKnf7f33SNEkswjA5sfEuXpAnkD7xMCFeb%2B%2BQHCvppMiNqU%2F9IqXw%2F1QF7qp5rEHl4%2F1RzT1E6qxM10EfTSTedkf5ncNNCb3sveVValTSEz8avRN07c%2BYPE%2BqS5D&X-Amz-Signature=f6f9ddecb2dad7e2da3ceed8e62cd8d8a751eda7246e15d5d6ca8176b4f094b3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCPZA3ZB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDApyZV5kOs4rzJD%2Fy8DqgCKBHUK7AK5CnTMSAvoPCCHQIgFKWxHbAKx1dixcFpMJzvx%2F0XiKs%2FqDSyv3V%2BlS1SvPcq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDO0L5%2FFW%2F56gOT1fJircA0JskgsXaxJ88Ro0GX4OwvtJlpuBHMr5N2Ot2fQdyk343S0WasltUMeub5ZfExgKIJoES3WiMRwYXHB%2FFGKJS3yQOC5UbV%2FyCxMDn0O4oAF8fCDnQAMughKghk%2FhxsLg0gPiHurZt7zuHhU6uiyQR9OT84MLQXeKpDT68wrSZp8mHN4xOXIOn7xl%2FhPX2v9%2B7TeW%2FsqDCHqymucg94Gqt3uaz4YctmIoad%2BFu939sWqMMCp%2FPi%2F9buCswHobeObqBt%2FIkINhsljNwy9behEWJ7cN2Ds1PKBfd%2FaItCNCSmlr4zHPhHKO0M%2Bs6mkgMzQGSv%2FikpoJi9UAswOYVX1qQ4nLVnYRwUCHBbXPtVv%2FfrWx4l%2F3VWHsklXPBGAEO88pGE26J9CwkJ7sgWOWrGozaAExD3Z62hP%2Bthl8i%2FiTy0mvD0GO59z1GPoyX5EBEY25JreWkYDBMNX3jPvwCz%2ByvzwQ1fUfC2ypWETLu13zN1L1SDuib1tCCxQA9E%2F28luuBPXUtK7sO0JKHuo2JYsz8W7Nqni4BrQZ6SBN9P%2FfkxBjQExcVwxR4A%2BLU%2FRDUP%2BbUGAbEge5ZJoZTqW%2F8s1zUjTj5nQeiIol99HXNGovvXGkQJ%2FdmVb9WmG8s8zIMMb9lL0GOqUB18zMSxjFNitvIOSFnkelt%2FYNjQyCTyrrh3Bmoukp3%2B7u2fhEQK58CkBLNP1jjsgJi3faRpDoXmEVayhnpremtwGlWNE%2FoBd7LKnf7f33SNEkswjA5sfEuXpAnkD7xMCFeb%2B%2BQHCvppMiNqU%2F9IqXw%2F1QF7qp5rEHl4%2F1RzT1E6qxM10EfTSTedkf5ncNNCb3sveVValTSEz8avRN07c%2BYPE%2BqS5D&X-Amz-Signature=799c077a154d49cdb98bb4e50aa42eddbb7ea92ee107904b53968164cdfeaa91&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCPZA3ZB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDApyZV5kOs4rzJD%2Fy8DqgCKBHUK7AK5CnTMSAvoPCCHQIgFKWxHbAKx1dixcFpMJzvx%2F0XiKs%2FqDSyv3V%2BlS1SvPcq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDO0L5%2FFW%2F56gOT1fJircA0JskgsXaxJ88Ro0GX4OwvtJlpuBHMr5N2Ot2fQdyk343S0WasltUMeub5ZfExgKIJoES3WiMRwYXHB%2FFGKJS3yQOC5UbV%2FyCxMDn0O4oAF8fCDnQAMughKghk%2FhxsLg0gPiHurZt7zuHhU6uiyQR9OT84MLQXeKpDT68wrSZp8mHN4xOXIOn7xl%2FhPX2v9%2B7TeW%2FsqDCHqymucg94Gqt3uaz4YctmIoad%2BFu939sWqMMCp%2FPi%2F9buCswHobeObqBt%2FIkINhsljNwy9behEWJ7cN2Ds1PKBfd%2FaItCNCSmlr4zHPhHKO0M%2Bs6mkgMzQGSv%2FikpoJi9UAswOYVX1qQ4nLVnYRwUCHBbXPtVv%2FfrWx4l%2F3VWHsklXPBGAEO88pGE26J9CwkJ7sgWOWrGozaAExD3Z62hP%2Bthl8i%2FiTy0mvD0GO59z1GPoyX5EBEY25JreWkYDBMNX3jPvwCz%2ByvzwQ1fUfC2ypWETLu13zN1L1SDuib1tCCxQA9E%2F28luuBPXUtK7sO0JKHuo2JYsz8W7Nqni4BrQZ6SBN9P%2FfkxBjQExcVwxR4A%2BLU%2FRDUP%2BbUGAbEge5ZJoZTqW%2F8s1zUjTj5nQeiIol99HXNGovvXGkQJ%2FdmVb9WmG8s8zIMMb9lL0GOqUB18zMSxjFNitvIOSFnkelt%2FYNjQyCTyrrh3Bmoukp3%2B7u2fhEQK58CkBLNP1jjsgJi3faRpDoXmEVayhnpremtwGlWNE%2FoBd7LKnf7f33SNEkswjA5sfEuXpAnkD7xMCFeb%2B%2BQHCvppMiNqU%2F9IqXw%2F1QF7qp5rEHl4%2F1RzT1E6qxM10EfTSTedkf5ncNNCb3sveVValTSEz8avRN07c%2BYPE%2BqS5D&X-Amz-Signature=4281efc040b33efdfe8aca9b047a9150e2c30bb66932df38740f0eabcb2e4a2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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


