

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TH2E5ZT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBu5BNjyFOrf9LljuWaDskocj%2B9Q32A9EF%2BRD7xu4QPiAiBQHCMfCR9l1eCv0DHM7sHdsjA8m49uEirSiS5D6sa1VSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxX8JGh9YMNE4JAqwKtwDxhUkn%2BBwKuRPKm67Gd3hhvrSEYqr1tchtJ0WjqvoFWBLlNTfRhi%2B%2BrAEZNTO1bxnvlwRsMc4mzyTUIb%2BTeYytbZKfsKccSEiFedvSx0gjeppTxplIE27FnOozjsDXK4SD%2FG4MoQ9jI6fsfIYnymPb64XfHRoK5RCCI5FJY2si%2Bm6Wa4VHyKzGEydUQyClqdINskdHACaHqZ9LCPVv9%2B31A2JKAiy4lPcmM9vtwJQwFEkCx7AzcSW2VNF21Tr9i0y7fP%2FVBbsjkSqQx205lcAOENifBU2SWWmyBmca7slKiMyUCqFbdI9anKqn5FjwMZN8%2BR%2FVPFq%2FOCmDX9bev%2Fhxt%2BU25h5m5iqk3%2F9dvvGRt3kTH1dG%2FwDtls9YQuhmyQ89sfBxr0tNar9NyNgs5iIR45cWg0QpMJRT1UdVH4Fa4iIOIn2hapXDxg5xSkpDUaePIsXwwOe68EFGwHvtis6eoKnyqJ8wW59zgI0iNUjtLfrBau5AcCr5BImzDGecW95bgA69gtDYlDkzRVE1zKTmPEpySp2na897qcy2h%2FpmRBONkkCxUMFCvBqdTP0EbZj%2B4xsoDpppM0yXTh%2F6Q0zNZ25bNeEGvvpYDaISRe3FpI8lbo%2Fnc1%2BKhbIKAMw6YbsvAY6pgGE%2FuQhlQcB%2BIQgaMB5uyI%2F7O9OyGV%2Fb9829pLmgX6xmYsZWkOZVXFH5y3uK9h0%2Fr6R%2F8pHkTwN5qhHm9Jcz1ZTrX6xED6TpeK6N%2BZdcCWuu6eVNIAQGSuwZ38tN%2Fxbq3wCTeM8ZL5g0ZYBF8ve3lFtyUwx9Tpkns%2Budjyrv8mK3%2BKymhCV63v%2FT2n3HaW7w4YQ1nkUb2yEAg7Rh5rS%2BqfASZlg9sEo&X-Amz-Signature=11f1c8b8edde99df3488d58667bd1275a60bc9d60697b8587e0e781f8072da95&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI7PGYJE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJ1o597HEixRDx5lTifYZoZRY3eHtYlEs6ULdKSff0FgIgGNuNhlmwrVjOb7xQ9aamhQhYG5xjM%2Fw2DblMEZ7s9KYqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDpufejfguBRjBnC8ircA0Dao6CMezmdTYhLe3Ge%2FmPkwG%2FuqNi%2BJWGrJvRATCTRTgQpFqhDLO6cqkBWs6CDq9X63Csu51s%2F2NT%2BWGnf37XgzjwvlBdH%2B9sChy8dcm3ElZJt2ifmXA8bf3ooczUjwxpJnieeSQDC5mMgQiNAyNwZusJBSilMtOAaoLhvo2uP6%2B5DJi%2FHLMR%2BSbJH4Ej1z7h7nt5F9vWL9ON3jEIPPCpXiDthTNJ3DbJpfULWSGzH6TDFtnUhbbLz9CXw%2BhIhAND8C%2BqXyDoyChowsZeYR7StlxuU0di9XqZjJLeb4CYU%2B43YZWLcPbCmhLcOAzP6UT9F10DSXYtEd%2F%2BS3zXQiNQCjZUxbO3XLBZkcHFm2tl9uVdmyfFwISNu%2FOgVoHmtzzb1VcI%2FFOVegaGabMRj2rurqXPN9%2FXNVW8CEMdsVXvGoIPdHTYIZ9oeRF17y7qDIm5Y3JFtS0%2FS4WdG5sq2csWyK%2FrXH5FbFVJK1Ridwxzy7x0Ca7DYRziDQUTo1jte90COaO0CW3ne3vzbGqJUGWyfA4haJqcQ9Ds90y4khx0C7qAK0jGlNPfdTxeK%2F%2F%2BjDAPggoxWjzKnm4UJkSiaV52eqZOl9FIAA0DeqbXST4UD0JFR%2F6aHqM0uC%2F%2B4MOWG7LwGOqUBN8wLsQAkpAi2cgd6Rh8PuGt6qEya%2B52F02F6r6eATodDAFVP%2F7%2FcimrqxvzCwKpmg3pjvHthAK83Eh66qEWjpQgpG1JUDSvpBhP09ufkVUd1Xwc%2FMO%2BuqxDD7iG4fwCy3RUSnKzG%2FwbECTQM7CDxTx%2FcixVwiNmiHOGRfRd5w28He%2FOH3X3wlMEcZudbFw6HYI%2B1XP1dmN9zrLGmhcEokqLXNmN6&X-Amz-Signature=57a9b5cd0712052f193842f7a8b44baa88a8f55de5444271bbd8418b5ad465b7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI7PGYJE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJ1o597HEixRDx5lTifYZoZRY3eHtYlEs6ULdKSff0FgIgGNuNhlmwrVjOb7xQ9aamhQhYG5xjM%2Fw2DblMEZ7s9KYqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDpufejfguBRjBnC8ircA0Dao6CMezmdTYhLe3Ge%2FmPkwG%2FuqNi%2BJWGrJvRATCTRTgQpFqhDLO6cqkBWs6CDq9X63Csu51s%2F2NT%2BWGnf37XgzjwvlBdH%2B9sChy8dcm3ElZJt2ifmXA8bf3ooczUjwxpJnieeSQDC5mMgQiNAyNwZusJBSilMtOAaoLhvo2uP6%2B5DJi%2FHLMR%2BSbJH4Ej1z7h7nt5F9vWL9ON3jEIPPCpXiDthTNJ3DbJpfULWSGzH6TDFtnUhbbLz9CXw%2BhIhAND8C%2BqXyDoyChowsZeYR7StlxuU0di9XqZjJLeb4CYU%2B43YZWLcPbCmhLcOAzP6UT9F10DSXYtEd%2F%2BS3zXQiNQCjZUxbO3XLBZkcHFm2tl9uVdmyfFwISNu%2FOgVoHmtzzb1VcI%2FFOVegaGabMRj2rurqXPN9%2FXNVW8CEMdsVXvGoIPdHTYIZ9oeRF17y7qDIm5Y3JFtS0%2FS4WdG5sq2csWyK%2FrXH5FbFVJK1Ridwxzy7x0Ca7DYRziDQUTo1jte90COaO0CW3ne3vzbGqJUGWyfA4haJqcQ9Ds90y4khx0C7qAK0jGlNPfdTxeK%2F%2F%2BjDAPggoxWjzKnm4UJkSiaV52eqZOl9FIAA0DeqbXST4UD0JFR%2F6aHqM0uC%2F%2B4MOWG7LwGOqUBN8wLsQAkpAi2cgd6Rh8PuGt6qEya%2B52F02F6r6eATodDAFVP%2F7%2FcimrqxvzCwKpmg3pjvHthAK83Eh66qEWjpQgpG1JUDSvpBhP09ufkVUd1Xwc%2FMO%2BuqxDD7iG4fwCy3RUSnKzG%2FwbECTQM7CDxTx%2FcixVwiNmiHOGRfRd5w28He%2FOH3X3wlMEcZudbFw6HYI%2B1XP1dmN9zrLGmhcEokqLXNmN6&X-Amz-Signature=94a8bccd7087d9584b32178e9d29510ecae03efbf7f4a22d6d859e980588f0c7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI7PGYJE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJ1o597HEixRDx5lTifYZoZRY3eHtYlEs6ULdKSff0FgIgGNuNhlmwrVjOb7xQ9aamhQhYG5xjM%2Fw2DblMEZ7s9KYqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDpufejfguBRjBnC8ircA0Dao6CMezmdTYhLe3Ge%2FmPkwG%2FuqNi%2BJWGrJvRATCTRTgQpFqhDLO6cqkBWs6CDq9X63Csu51s%2F2NT%2BWGnf37XgzjwvlBdH%2B9sChy8dcm3ElZJt2ifmXA8bf3ooczUjwxpJnieeSQDC5mMgQiNAyNwZusJBSilMtOAaoLhvo2uP6%2B5DJi%2FHLMR%2BSbJH4Ej1z7h7nt5F9vWL9ON3jEIPPCpXiDthTNJ3DbJpfULWSGzH6TDFtnUhbbLz9CXw%2BhIhAND8C%2BqXyDoyChowsZeYR7StlxuU0di9XqZjJLeb4CYU%2B43YZWLcPbCmhLcOAzP6UT9F10DSXYtEd%2F%2BS3zXQiNQCjZUxbO3XLBZkcHFm2tl9uVdmyfFwISNu%2FOgVoHmtzzb1VcI%2FFOVegaGabMRj2rurqXPN9%2FXNVW8CEMdsVXvGoIPdHTYIZ9oeRF17y7qDIm5Y3JFtS0%2FS4WdG5sq2csWyK%2FrXH5FbFVJK1Ridwxzy7x0Ca7DYRziDQUTo1jte90COaO0CW3ne3vzbGqJUGWyfA4haJqcQ9Ds90y4khx0C7qAK0jGlNPfdTxeK%2F%2F%2BjDAPggoxWjzKnm4UJkSiaV52eqZOl9FIAA0DeqbXST4UD0JFR%2F6aHqM0uC%2F%2B4MOWG7LwGOqUBN8wLsQAkpAi2cgd6Rh8PuGt6qEya%2B52F02F6r6eATodDAFVP%2F7%2FcimrqxvzCwKpmg3pjvHthAK83Eh66qEWjpQgpG1JUDSvpBhP09ufkVUd1Xwc%2FMO%2BuqxDD7iG4fwCy3RUSnKzG%2FwbECTQM7CDxTx%2FcixVwiNmiHOGRfRd5w28He%2FOH3X3wlMEcZudbFw6HYI%2B1XP1dmN9zrLGmhcEokqLXNmN6&X-Amz-Signature=7819e2f91e12a01c62ed94f052061c36440a88236ceed53c2b01b4708199009c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI7PGYJE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJ1o597HEixRDx5lTifYZoZRY3eHtYlEs6ULdKSff0FgIgGNuNhlmwrVjOb7xQ9aamhQhYG5xjM%2Fw2DblMEZ7s9KYqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDpufejfguBRjBnC8ircA0Dao6CMezmdTYhLe3Ge%2FmPkwG%2FuqNi%2BJWGrJvRATCTRTgQpFqhDLO6cqkBWs6CDq9X63Csu51s%2F2NT%2BWGnf37XgzjwvlBdH%2B9sChy8dcm3ElZJt2ifmXA8bf3ooczUjwxpJnieeSQDC5mMgQiNAyNwZusJBSilMtOAaoLhvo2uP6%2B5DJi%2FHLMR%2BSbJH4Ej1z7h7nt5F9vWL9ON3jEIPPCpXiDthTNJ3DbJpfULWSGzH6TDFtnUhbbLz9CXw%2BhIhAND8C%2BqXyDoyChowsZeYR7StlxuU0di9XqZjJLeb4CYU%2B43YZWLcPbCmhLcOAzP6UT9F10DSXYtEd%2F%2BS3zXQiNQCjZUxbO3XLBZkcHFm2tl9uVdmyfFwISNu%2FOgVoHmtzzb1VcI%2FFOVegaGabMRj2rurqXPN9%2FXNVW8CEMdsVXvGoIPdHTYIZ9oeRF17y7qDIm5Y3JFtS0%2FS4WdG5sq2csWyK%2FrXH5FbFVJK1Ridwxzy7x0Ca7DYRziDQUTo1jte90COaO0CW3ne3vzbGqJUGWyfA4haJqcQ9Ds90y4khx0C7qAK0jGlNPfdTxeK%2F%2F%2BjDAPggoxWjzKnm4UJkSiaV52eqZOl9FIAA0DeqbXST4UD0JFR%2F6aHqM0uC%2F%2B4MOWG7LwGOqUBN8wLsQAkpAi2cgd6Rh8PuGt6qEya%2B52F02F6r6eATodDAFVP%2F7%2FcimrqxvzCwKpmg3pjvHthAK83Eh66qEWjpQgpG1JUDSvpBhP09ufkVUd1Xwc%2FMO%2BuqxDD7iG4fwCy3RUSnKzG%2FwbECTQM7CDxTx%2FcixVwiNmiHOGRfRd5w28He%2FOH3X3wlMEcZudbFw6HYI%2B1XP1dmN9zrLGmhcEokqLXNmN6&X-Amz-Signature=4183c578db3403bc2cc3daeabbe985a725d5363c8f2355e78766e0ea0b1c281e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI7PGYJE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJ1o597HEixRDx5lTifYZoZRY3eHtYlEs6ULdKSff0FgIgGNuNhlmwrVjOb7xQ9aamhQhYG5xjM%2Fw2DblMEZ7s9KYqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDpufejfguBRjBnC8ircA0Dao6CMezmdTYhLe3Ge%2FmPkwG%2FuqNi%2BJWGrJvRATCTRTgQpFqhDLO6cqkBWs6CDq9X63Csu51s%2F2NT%2BWGnf37XgzjwvlBdH%2B9sChy8dcm3ElZJt2ifmXA8bf3ooczUjwxpJnieeSQDC5mMgQiNAyNwZusJBSilMtOAaoLhvo2uP6%2B5DJi%2FHLMR%2BSbJH4Ej1z7h7nt5F9vWL9ON3jEIPPCpXiDthTNJ3DbJpfULWSGzH6TDFtnUhbbLz9CXw%2BhIhAND8C%2BqXyDoyChowsZeYR7StlxuU0di9XqZjJLeb4CYU%2B43YZWLcPbCmhLcOAzP6UT9F10DSXYtEd%2F%2BS3zXQiNQCjZUxbO3XLBZkcHFm2tl9uVdmyfFwISNu%2FOgVoHmtzzb1VcI%2FFOVegaGabMRj2rurqXPN9%2FXNVW8CEMdsVXvGoIPdHTYIZ9oeRF17y7qDIm5Y3JFtS0%2FS4WdG5sq2csWyK%2FrXH5FbFVJK1Ridwxzy7x0Ca7DYRziDQUTo1jte90COaO0CW3ne3vzbGqJUGWyfA4haJqcQ9Ds90y4khx0C7qAK0jGlNPfdTxeK%2F%2F%2BjDAPggoxWjzKnm4UJkSiaV52eqZOl9FIAA0DeqbXST4UD0JFR%2F6aHqM0uC%2F%2B4MOWG7LwGOqUBN8wLsQAkpAi2cgd6Rh8PuGt6qEya%2B52F02F6r6eATodDAFVP%2F7%2FcimrqxvzCwKpmg3pjvHthAK83Eh66qEWjpQgpG1JUDSvpBhP09ufkVUd1Xwc%2FMO%2BuqxDD7iG4fwCy3RUSnKzG%2FwbECTQM7CDxTx%2FcixVwiNmiHOGRfRd5w28He%2FOH3X3wlMEcZudbFw6HYI%2B1XP1dmN9zrLGmhcEokqLXNmN6&X-Amz-Signature=8c45f5dd5f94dee7127a51ad3afc33f5678a44af00f2e9143ed1d4e05803010d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TH2E5ZT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBu5BNjyFOrf9LljuWaDskocj%2B9Q32A9EF%2BRD7xu4QPiAiBQHCMfCR9l1eCv0DHM7sHdsjA8m49uEirSiS5D6sa1VSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxX8JGh9YMNE4JAqwKtwDxhUkn%2BBwKuRPKm67Gd3hhvrSEYqr1tchtJ0WjqvoFWBLlNTfRhi%2B%2BrAEZNTO1bxnvlwRsMc4mzyTUIb%2BTeYytbZKfsKccSEiFedvSx0gjeppTxplIE27FnOozjsDXK4SD%2FG4MoQ9jI6fsfIYnymPb64XfHRoK5RCCI5FJY2si%2Bm6Wa4VHyKzGEydUQyClqdINskdHACaHqZ9LCPVv9%2B31A2JKAiy4lPcmM9vtwJQwFEkCx7AzcSW2VNF21Tr9i0y7fP%2FVBbsjkSqQx205lcAOENifBU2SWWmyBmca7slKiMyUCqFbdI9anKqn5FjwMZN8%2BR%2FVPFq%2FOCmDX9bev%2Fhxt%2BU25h5m5iqk3%2F9dvvGRt3kTH1dG%2FwDtls9YQuhmyQ89sfBxr0tNar9NyNgs5iIR45cWg0QpMJRT1UdVH4Fa4iIOIn2hapXDxg5xSkpDUaePIsXwwOe68EFGwHvtis6eoKnyqJ8wW59zgI0iNUjtLfrBau5AcCr5BImzDGecW95bgA69gtDYlDkzRVE1zKTmPEpySp2na897qcy2h%2FpmRBONkkCxUMFCvBqdTP0EbZj%2B4xsoDpppM0yXTh%2F6Q0zNZ25bNeEGvvpYDaISRe3FpI8lbo%2Fnc1%2BKhbIKAMw6YbsvAY6pgGE%2FuQhlQcB%2BIQgaMB5uyI%2F7O9OyGV%2Fb9829pLmgX6xmYsZWkOZVXFH5y3uK9h0%2Fr6R%2F8pHkTwN5qhHm9Jcz1ZTrX6xED6TpeK6N%2BZdcCWuu6eVNIAQGSuwZ38tN%2Fxbq3wCTeM8ZL5g0ZYBF8ve3lFtyUwx9Tpkns%2Budjyrv8mK3%2BKymhCV63v%2FT2n3HaW7w4YQ1nkUb2yEAg7Rh5rS%2BqfASZlg9sEo&X-Amz-Signature=19c9665a753635d587884a433ae7d458d2e3d8cb7ec2f278194c9879de7b499f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TH2E5ZT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBu5BNjyFOrf9LljuWaDskocj%2B9Q32A9EF%2BRD7xu4QPiAiBQHCMfCR9l1eCv0DHM7sHdsjA8m49uEirSiS5D6sa1VSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxX8JGh9YMNE4JAqwKtwDxhUkn%2BBwKuRPKm67Gd3hhvrSEYqr1tchtJ0WjqvoFWBLlNTfRhi%2B%2BrAEZNTO1bxnvlwRsMc4mzyTUIb%2BTeYytbZKfsKccSEiFedvSx0gjeppTxplIE27FnOozjsDXK4SD%2FG4MoQ9jI6fsfIYnymPb64XfHRoK5RCCI5FJY2si%2Bm6Wa4VHyKzGEydUQyClqdINskdHACaHqZ9LCPVv9%2B31A2JKAiy4lPcmM9vtwJQwFEkCx7AzcSW2VNF21Tr9i0y7fP%2FVBbsjkSqQx205lcAOENifBU2SWWmyBmca7slKiMyUCqFbdI9anKqn5FjwMZN8%2BR%2FVPFq%2FOCmDX9bev%2Fhxt%2BU25h5m5iqk3%2F9dvvGRt3kTH1dG%2FwDtls9YQuhmyQ89sfBxr0tNar9NyNgs5iIR45cWg0QpMJRT1UdVH4Fa4iIOIn2hapXDxg5xSkpDUaePIsXwwOe68EFGwHvtis6eoKnyqJ8wW59zgI0iNUjtLfrBau5AcCr5BImzDGecW95bgA69gtDYlDkzRVE1zKTmPEpySp2na897qcy2h%2FpmRBONkkCxUMFCvBqdTP0EbZj%2B4xsoDpppM0yXTh%2F6Q0zNZ25bNeEGvvpYDaISRe3FpI8lbo%2Fnc1%2BKhbIKAMw6YbsvAY6pgGE%2FuQhlQcB%2BIQgaMB5uyI%2F7O9OyGV%2Fb9829pLmgX6xmYsZWkOZVXFH5y3uK9h0%2Fr6R%2F8pHkTwN5qhHm9Jcz1ZTrX6xED6TpeK6N%2BZdcCWuu6eVNIAQGSuwZ38tN%2Fxbq3wCTeM8ZL5g0ZYBF8ve3lFtyUwx9Tpkns%2Budjyrv8mK3%2BKymhCV63v%2FT2n3HaW7w4YQ1nkUb2yEAg7Rh5rS%2BqfASZlg9sEo&X-Amz-Signature=aec9e2f15223d4630b67562609287edc5dc9eb8081c4eb20ecba5d3b1a6ae7d9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TH2E5ZT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBu5BNjyFOrf9LljuWaDskocj%2B9Q32A9EF%2BRD7xu4QPiAiBQHCMfCR9l1eCv0DHM7sHdsjA8m49uEirSiS5D6sa1VSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxX8JGh9YMNE4JAqwKtwDxhUkn%2BBwKuRPKm67Gd3hhvrSEYqr1tchtJ0WjqvoFWBLlNTfRhi%2B%2BrAEZNTO1bxnvlwRsMc4mzyTUIb%2BTeYytbZKfsKccSEiFedvSx0gjeppTxplIE27FnOozjsDXK4SD%2FG4MoQ9jI6fsfIYnymPb64XfHRoK5RCCI5FJY2si%2Bm6Wa4VHyKzGEydUQyClqdINskdHACaHqZ9LCPVv9%2B31A2JKAiy4lPcmM9vtwJQwFEkCx7AzcSW2VNF21Tr9i0y7fP%2FVBbsjkSqQx205lcAOENifBU2SWWmyBmca7slKiMyUCqFbdI9anKqn5FjwMZN8%2BR%2FVPFq%2FOCmDX9bev%2Fhxt%2BU25h5m5iqk3%2F9dvvGRt3kTH1dG%2FwDtls9YQuhmyQ89sfBxr0tNar9NyNgs5iIR45cWg0QpMJRT1UdVH4Fa4iIOIn2hapXDxg5xSkpDUaePIsXwwOe68EFGwHvtis6eoKnyqJ8wW59zgI0iNUjtLfrBau5AcCr5BImzDGecW95bgA69gtDYlDkzRVE1zKTmPEpySp2na897qcy2h%2FpmRBONkkCxUMFCvBqdTP0EbZj%2B4xsoDpppM0yXTh%2F6Q0zNZ25bNeEGvvpYDaISRe3FpI8lbo%2Fnc1%2BKhbIKAMw6YbsvAY6pgGE%2FuQhlQcB%2BIQgaMB5uyI%2F7O9OyGV%2Fb9829pLmgX6xmYsZWkOZVXFH5y3uK9h0%2Fr6R%2F8pHkTwN5qhHm9Jcz1ZTrX6xED6TpeK6N%2BZdcCWuu6eVNIAQGSuwZ38tN%2Fxbq3wCTeM8ZL5g0ZYBF8ve3lFtyUwx9Tpkns%2Budjyrv8mK3%2BKymhCV63v%2FT2n3HaW7w4YQ1nkUb2yEAg7Rh5rS%2BqfASZlg9sEo&X-Amz-Signature=ee6b95b1ce72a746ea00cb805dd1ffde731b30c918de3b0c618ae2a283b48b9f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TH2E5ZT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBu5BNjyFOrf9LljuWaDskocj%2B9Q32A9EF%2BRD7xu4QPiAiBQHCMfCR9l1eCv0DHM7sHdsjA8m49uEirSiS5D6sa1VSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxX8JGh9YMNE4JAqwKtwDxhUkn%2BBwKuRPKm67Gd3hhvrSEYqr1tchtJ0WjqvoFWBLlNTfRhi%2B%2BrAEZNTO1bxnvlwRsMc4mzyTUIb%2BTeYytbZKfsKccSEiFedvSx0gjeppTxplIE27FnOozjsDXK4SD%2FG4MoQ9jI6fsfIYnymPb64XfHRoK5RCCI5FJY2si%2Bm6Wa4VHyKzGEydUQyClqdINskdHACaHqZ9LCPVv9%2B31A2JKAiy4lPcmM9vtwJQwFEkCx7AzcSW2VNF21Tr9i0y7fP%2FVBbsjkSqQx205lcAOENifBU2SWWmyBmca7slKiMyUCqFbdI9anKqn5FjwMZN8%2BR%2FVPFq%2FOCmDX9bev%2Fhxt%2BU25h5m5iqk3%2F9dvvGRt3kTH1dG%2FwDtls9YQuhmyQ89sfBxr0tNar9NyNgs5iIR45cWg0QpMJRT1UdVH4Fa4iIOIn2hapXDxg5xSkpDUaePIsXwwOe68EFGwHvtis6eoKnyqJ8wW59zgI0iNUjtLfrBau5AcCr5BImzDGecW95bgA69gtDYlDkzRVE1zKTmPEpySp2na897qcy2h%2FpmRBONkkCxUMFCvBqdTP0EbZj%2B4xsoDpppM0yXTh%2F6Q0zNZ25bNeEGvvpYDaISRe3FpI8lbo%2Fnc1%2BKhbIKAMw6YbsvAY6pgGE%2FuQhlQcB%2BIQgaMB5uyI%2F7O9OyGV%2Fb9829pLmgX6xmYsZWkOZVXFH5y3uK9h0%2Fr6R%2F8pHkTwN5qhHm9Jcz1ZTrX6xED6TpeK6N%2BZdcCWuu6eVNIAQGSuwZ38tN%2Fxbq3wCTeM8ZL5g0ZYBF8ve3lFtyUwx9Tpkns%2Budjyrv8mK3%2BKymhCV63v%2FT2n3HaW7w4YQ1nkUb2yEAg7Rh5rS%2BqfASZlg9sEo&X-Amz-Signature=a63752497bf7e9fc02bf4db6cd695c8af978539f2de110603bde5fd4264e209a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TH2E5ZT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBu5BNjyFOrf9LljuWaDskocj%2B9Q32A9EF%2BRD7xu4QPiAiBQHCMfCR9l1eCv0DHM7sHdsjA8m49uEirSiS5D6sa1VSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxX8JGh9YMNE4JAqwKtwDxhUkn%2BBwKuRPKm67Gd3hhvrSEYqr1tchtJ0WjqvoFWBLlNTfRhi%2B%2BrAEZNTO1bxnvlwRsMc4mzyTUIb%2BTeYytbZKfsKccSEiFedvSx0gjeppTxplIE27FnOozjsDXK4SD%2FG4MoQ9jI6fsfIYnymPb64XfHRoK5RCCI5FJY2si%2Bm6Wa4VHyKzGEydUQyClqdINskdHACaHqZ9LCPVv9%2B31A2JKAiy4lPcmM9vtwJQwFEkCx7AzcSW2VNF21Tr9i0y7fP%2FVBbsjkSqQx205lcAOENifBU2SWWmyBmca7slKiMyUCqFbdI9anKqn5FjwMZN8%2BR%2FVPFq%2FOCmDX9bev%2Fhxt%2BU25h5m5iqk3%2F9dvvGRt3kTH1dG%2FwDtls9YQuhmyQ89sfBxr0tNar9NyNgs5iIR45cWg0QpMJRT1UdVH4Fa4iIOIn2hapXDxg5xSkpDUaePIsXwwOe68EFGwHvtis6eoKnyqJ8wW59zgI0iNUjtLfrBau5AcCr5BImzDGecW95bgA69gtDYlDkzRVE1zKTmPEpySp2na897qcy2h%2FpmRBONkkCxUMFCvBqdTP0EbZj%2B4xsoDpppM0yXTh%2F6Q0zNZ25bNeEGvvpYDaISRe3FpI8lbo%2Fnc1%2BKhbIKAMw6YbsvAY6pgGE%2FuQhlQcB%2BIQgaMB5uyI%2F7O9OyGV%2Fb9829pLmgX6xmYsZWkOZVXFH5y3uK9h0%2Fr6R%2F8pHkTwN5qhHm9Jcz1ZTrX6xED6TpeK6N%2BZdcCWuu6eVNIAQGSuwZ38tN%2Fxbq3wCTeM8ZL5g0ZYBF8ve3lFtyUwx9Tpkns%2Budjyrv8mK3%2BKymhCV63v%2FT2n3HaW7w4YQ1nkUb2yEAg7Rh5rS%2BqfASZlg9sEo&X-Amz-Signature=73ee300422cab3fff289694121216ab88e543747f42ac97453cffea0f18a900a&X-Amz-SignedHeaders=host&x-id=GetObject)
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


