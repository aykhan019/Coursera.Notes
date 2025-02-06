

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC7M3L54%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIDIP15yXKGLTYioNl%2FnvKF4LjYbLLYQ7j6Amze4hd6nkAiBXydnicxxin%2Fg9xNE7M40Uq5WT0TL6PtHbUVR8HsikFyr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMNglEfSqY9JAMuP9vKtwDuGdaxd3a3SAtO0JjYl4IKugWt46OqeTC0t1sSAkf%2FpZu6RtmZ7sHKQmaR1yCgG%2FZNPPylBMTL6FslGsNzLhA9VXnsXLMvgL0m3HD51FhkZEDbP0PciSSdwW3sVdto8DJKfREY6%2BaQcbPo%2FprfbrMOUhPA%2Bk02xFJ%2BxN41%2B%2FLpJ2tFryfx51EjqDKdgvCW48SyY11tT5GRhgg3eR2vjqbwGZWhBnWgF5Ubrg9s9rpw2Vqg0q69vUMq%2BmoOPMpqG9gg%2Bkzw7IzC0nTUw40DuPx7xEes%2BjS3m8Dn9PZfbgeZfYhuE%2FMzu6jO3h%2BqPQiULUDya3Mvp7c2kRQ6XteS5oZPTR6viSwQ7jQPAXvMumPY3EhW0159vcWpLSkJF8zwkfvnvolDbUBPQ8MPzGWO9oLk8Zaxcsn%2F1gcaW3jBzVFALpE%2B%2BKAq8eK38XOtMn257ZUGdiiAjKNOzm8iUvUD1eRlFcQdquI%2Fl4Ef1%2BwFlTzW0d0siydboqQ9Xkf2BGZGRUP920hm1cGZLeUTj3rK6R0fs0YR9odf0FyxcOVhANkHNfcC3qb1htu1QuKvIxVk7UsVavFqVtP8jRAqrRjAMa1V0jf5FUtloMKP51xfrhShVuwJWuCxygrgRtU%2F3wwmrWRvQY6pgEcJFjqe02UafpuZS3KG%2BbmY%2ByxMMLPSjPyt1Bi1C%2FMWYvTvHBEH7s4ENitga6fl8ONg2UOtFa5NCPwB%2Bw%2BPhDuzWBg3s8hoVvPiKPwR7l%2FPw0%2Bs%2BSzC53HRxdTLwVKEH15%2BpQv8QOq3jbR6KpMwrF%2B0xpgyxh1hOfmAtnJrnk5Bg2k6cm2%2BQFBvQIIS%2F8foioEYPxKg9lM7sls%2F122Er1JHKrPnIpw&X-Amz-Signature=743108b0d293f63a8bdd59ed6c8f4531bd28239de42985a435fddce39eabf3e0&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQLL6WZ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIC%2BPu3WfncUMoP%2Beww0Q8nApyp46hBnn5Eqs%2B4mDH1eGAiAl21wC8G5G30QfCCTXJ7oQb4Xe3H088hYiBAbO1enC%2Bir%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMThVSOHgPoaVZQOl8KtwDVFyW85%2BZk4sefJdDQrX7TixUT0x1F4YWr0RmBWFE0VwcJKQUeDhj9aCA6s3DfcK1Nno1x0G8zD0gs4rIgvRP4cc6QVDqv49XoNwPoFkoIZz1xZl5XgDGv86UdRMS4F3NKqN%2BCRkDZmqdavh9CqyLAbXWqX%2F5qeO9Z91WHz0aX3ABg51ly0bp7C9qTeV0zR5zUFHAv5h7c72Bj5d8%2FER8%2FOKP7nwkTmZKmtr6eDEDAfgj2w12r7%2BcE1VxNLB%2BYVpQEsKyZ%2BsjSy8tT5f2tNxDgbtkadMbKAmaG4T0%2BOoQyNcQkcokqXPqr6vAj%2FEt6WNyryed3jD2s9e2Z6NTlHO9q108ve8I%2Bt7b92bFanEfqE8Zv1LJ8OVJnXn5Do4%2FsEp2zw4swp6ZMb4UcPgGmReK7VmD8fOs9yVvuSdDcpST%2B9DIScOKe0E8kqehaZq87GUyEPcL%2Fckxzd4cFHFYpXl7kKNGASU%2BnbGNs0vtonZ4jVsj0Jqq026ogGVfqldQJOArerEhG5dphrigjzY5Muv76nfiHK7RC0T8US%2F8aCKle%2Fupd2hVkbpCssF%2FBteqNHvu3Z0FjmX6U4QEs9h84PjNxzAhIIYhhB4YHbpnADd%2FUj8q4Z7js0Qzy%2F0ARN4w47SRvQY6pgGGHX9G2dz9WyW0Oi83T52tTKUarOwGAvw7KDEwcIrlK%2B7TvLbnGVGQpkeCFg5XkGWwPQBTvb9srUa6iUS%2FPL4iK7j8BCPkqShouMW0ezixeNYx6rASsHvIAPBEMmSakBiW7IxwQN%2BkXS5dO0u8F%2BJ1zmKpXq7T0nZsI52wCldfD4s5iiqsTgD3CSlp3esDShaJYqLf8%2BltXqTcCOMgCwS8bBKDwNy9&X-Amz-Signature=af379af8f064cf1af5f796658a7a94b51cb4facd7cfc56c3580c729008ece89a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQLL6WZ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIC%2BPu3WfncUMoP%2Beww0Q8nApyp46hBnn5Eqs%2B4mDH1eGAiAl21wC8G5G30QfCCTXJ7oQb4Xe3H088hYiBAbO1enC%2Bir%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMThVSOHgPoaVZQOl8KtwDVFyW85%2BZk4sefJdDQrX7TixUT0x1F4YWr0RmBWFE0VwcJKQUeDhj9aCA6s3DfcK1Nno1x0G8zD0gs4rIgvRP4cc6QVDqv49XoNwPoFkoIZz1xZl5XgDGv86UdRMS4F3NKqN%2BCRkDZmqdavh9CqyLAbXWqX%2F5qeO9Z91WHz0aX3ABg51ly0bp7C9qTeV0zR5zUFHAv5h7c72Bj5d8%2FER8%2FOKP7nwkTmZKmtr6eDEDAfgj2w12r7%2BcE1VxNLB%2BYVpQEsKyZ%2BsjSy8tT5f2tNxDgbtkadMbKAmaG4T0%2BOoQyNcQkcokqXPqr6vAj%2FEt6WNyryed3jD2s9e2Z6NTlHO9q108ve8I%2Bt7b92bFanEfqE8Zv1LJ8OVJnXn5Do4%2FsEp2zw4swp6ZMb4UcPgGmReK7VmD8fOs9yVvuSdDcpST%2B9DIScOKe0E8kqehaZq87GUyEPcL%2Fckxzd4cFHFYpXl7kKNGASU%2BnbGNs0vtonZ4jVsj0Jqq026ogGVfqldQJOArerEhG5dphrigjzY5Muv76nfiHK7RC0T8US%2F8aCKle%2Fupd2hVkbpCssF%2FBteqNHvu3Z0FjmX6U4QEs9h84PjNxzAhIIYhhB4YHbpnADd%2FUj8q4Z7js0Qzy%2F0ARN4w47SRvQY6pgGGHX9G2dz9WyW0Oi83T52tTKUarOwGAvw7KDEwcIrlK%2B7TvLbnGVGQpkeCFg5XkGWwPQBTvb9srUa6iUS%2FPL4iK7j8BCPkqShouMW0ezixeNYx6rASsHvIAPBEMmSakBiW7IxwQN%2BkXS5dO0u8F%2BJ1zmKpXq7T0nZsI52wCldfD4s5iiqsTgD3CSlp3esDShaJYqLf8%2BltXqTcCOMgCwS8bBKDwNy9&X-Amz-Signature=ff5af080f9b26756b6ce7db758cfd9978696b7f162149c210837aae0f3ae2848&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQLL6WZ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIC%2BPu3WfncUMoP%2Beww0Q8nApyp46hBnn5Eqs%2B4mDH1eGAiAl21wC8G5G30QfCCTXJ7oQb4Xe3H088hYiBAbO1enC%2Bir%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMThVSOHgPoaVZQOl8KtwDVFyW85%2BZk4sefJdDQrX7TixUT0x1F4YWr0RmBWFE0VwcJKQUeDhj9aCA6s3DfcK1Nno1x0G8zD0gs4rIgvRP4cc6QVDqv49XoNwPoFkoIZz1xZl5XgDGv86UdRMS4F3NKqN%2BCRkDZmqdavh9CqyLAbXWqX%2F5qeO9Z91WHz0aX3ABg51ly0bp7C9qTeV0zR5zUFHAv5h7c72Bj5d8%2FER8%2FOKP7nwkTmZKmtr6eDEDAfgj2w12r7%2BcE1VxNLB%2BYVpQEsKyZ%2BsjSy8tT5f2tNxDgbtkadMbKAmaG4T0%2BOoQyNcQkcokqXPqr6vAj%2FEt6WNyryed3jD2s9e2Z6NTlHO9q108ve8I%2Bt7b92bFanEfqE8Zv1LJ8OVJnXn5Do4%2FsEp2zw4swp6ZMb4UcPgGmReK7VmD8fOs9yVvuSdDcpST%2B9DIScOKe0E8kqehaZq87GUyEPcL%2Fckxzd4cFHFYpXl7kKNGASU%2BnbGNs0vtonZ4jVsj0Jqq026ogGVfqldQJOArerEhG5dphrigjzY5Muv76nfiHK7RC0T8US%2F8aCKle%2Fupd2hVkbpCssF%2FBteqNHvu3Z0FjmX6U4QEs9h84PjNxzAhIIYhhB4YHbpnADd%2FUj8q4Z7js0Qzy%2F0ARN4w47SRvQY6pgGGHX9G2dz9WyW0Oi83T52tTKUarOwGAvw7KDEwcIrlK%2B7TvLbnGVGQpkeCFg5XkGWwPQBTvb9srUa6iUS%2FPL4iK7j8BCPkqShouMW0ezixeNYx6rASsHvIAPBEMmSakBiW7IxwQN%2BkXS5dO0u8F%2BJ1zmKpXq7T0nZsI52wCldfD4s5iiqsTgD3CSlp3esDShaJYqLf8%2BltXqTcCOMgCwS8bBKDwNy9&X-Amz-Signature=bebdb8ed76a5b29d9dc60ba8df07b0d6811f82139c50268bb821abb57445c6ef&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQLL6WZ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIC%2BPu3WfncUMoP%2Beww0Q8nApyp46hBnn5Eqs%2B4mDH1eGAiAl21wC8G5G30QfCCTXJ7oQb4Xe3H088hYiBAbO1enC%2Bir%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMThVSOHgPoaVZQOl8KtwDVFyW85%2BZk4sefJdDQrX7TixUT0x1F4YWr0RmBWFE0VwcJKQUeDhj9aCA6s3DfcK1Nno1x0G8zD0gs4rIgvRP4cc6QVDqv49XoNwPoFkoIZz1xZl5XgDGv86UdRMS4F3NKqN%2BCRkDZmqdavh9CqyLAbXWqX%2F5qeO9Z91WHz0aX3ABg51ly0bp7C9qTeV0zR5zUFHAv5h7c72Bj5d8%2FER8%2FOKP7nwkTmZKmtr6eDEDAfgj2w12r7%2BcE1VxNLB%2BYVpQEsKyZ%2BsjSy8tT5f2tNxDgbtkadMbKAmaG4T0%2BOoQyNcQkcokqXPqr6vAj%2FEt6WNyryed3jD2s9e2Z6NTlHO9q108ve8I%2Bt7b92bFanEfqE8Zv1LJ8OVJnXn5Do4%2FsEp2zw4swp6ZMb4UcPgGmReK7VmD8fOs9yVvuSdDcpST%2B9DIScOKe0E8kqehaZq87GUyEPcL%2Fckxzd4cFHFYpXl7kKNGASU%2BnbGNs0vtonZ4jVsj0Jqq026ogGVfqldQJOArerEhG5dphrigjzY5Muv76nfiHK7RC0T8US%2F8aCKle%2Fupd2hVkbpCssF%2FBteqNHvu3Z0FjmX6U4QEs9h84PjNxzAhIIYhhB4YHbpnADd%2FUj8q4Z7js0Qzy%2F0ARN4w47SRvQY6pgGGHX9G2dz9WyW0Oi83T52tTKUarOwGAvw7KDEwcIrlK%2B7TvLbnGVGQpkeCFg5XkGWwPQBTvb9srUa6iUS%2FPL4iK7j8BCPkqShouMW0ezixeNYx6rASsHvIAPBEMmSakBiW7IxwQN%2BkXS5dO0u8F%2BJ1zmKpXq7T0nZsI52wCldfD4s5iiqsTgD3CSlp3esDShaJYqLf8%2BltXqTcCOMgCwS8bBKDwNy9&X-Amz-Signature=42566bfb788a62b59fc0fd6742301d0974707dfe4e50de6fb991732e73b1a0ab&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQLL6WZ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIC%2BPu3WfncUMoP%2Beww0Q8nApyp46hBnn5Eqs%2B4mDH1eGAiAl21wC8G5G30QfCCTXJ7oQb4Xe3H088hYiBAbO1enC%2Bir%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMThVSOHgPoaVZQOl8KtwDVFyW85%2BZk4sefJdDQrX7TixUT0x1F4YWr0RmBWFE0VwcJKQUeDhj9aCA6s3DfcK1Nno1x0G8zD0gs4rIgvRP4cc6QVDqv49XoNwPoFkoIZz1xZl5XgDGv86UdRMS4F3NKqN%2BCRkDZmqdavh9CqyLAbXWqX%2F5qeO9Z91WHz0aX3ABg51ly0bp7C9qTeV0zR5zUFHAv5h7c72Bj5d8%2FER8%2FOKP7nwkTmZKmtr6eDEDAfgj2w12r7%2BcE1VxNLB%2BYVpQEsKyZ%2BsjSy8tT5f2tNxDgbtkadMbKAmaG4T0%2BOoQyNcQkcokqXPqr6vAj%2FEt6WNyryed3jD2s9e2Z6NTlHO9q108ve8I%2Bt7b92bFanEfqE8Zv1LJ8OVJnXn5Do4%2FsEp2zw4swp6ZMb4UcPgGmReK7VmD8fOs9yVvuSdDcpST%2B9DIScOKe0E8kqehaZq87GUyEPcL%2Fckxzd4cFHFYpXl7kKNGASU%2BnbGNs0vtonZ4jVsj0Jqq026ogGVfqldQJOArerEhG5dphrigjzY5Muv76nfiHK7RC0T8US%2F8aCKle%2Fupd2hVkbpCssF%2FBteqNHvu3Z0FjmX6U4QEs9h84PjNxzAhIIYhhB4YHbpnADd%2FUj8q4Z7js0Qzy%2F0ARN4w47SRvQY6pgGGHX9G2dz9WyW0Oi83T52tTKUarOwGAvw7KDEwcIrlK%2B7TvLbnGVGQpkeCFg5XkGWwPQBTvb9srUa6iUS%2FPL4iK7j8BCPkqShouMW0ezixeNYx6rASsHvIAPBEMmSakBiW7IxwQN%2BkXS5dO0u8F%2BJ1zmKpXq7T0nZsI52wCldfD4s5iiqsTgD3CSlp3esDShaJYqLf8%2BltXqTcCOMgCwS8bBKDwNy9&X-Amz-Signature=e7d3ffb6626a5ab5fe9b6d9cdbf842106d2edd9cbca767f0743b162a5597f336&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC7M3L54%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIDIP15yXKGLTYioNl%2FnvKF4LjYbLLYQ7j6Amze4hd6nkAiBXydnicxxin%2Fg9xNE7M40Uq5WT0TL6PtHbUVR8HsikFyr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMNglEfSqY9JAMuP9vKtwDuGdaxd3a3SAtO0JjYl4IKugWt46OqeTC0t1sSAkf%2FpZu6RtmZ7sHKQmaR1yCgG%2FZNPPylBMTL6FslGsNzLhA9VXnsXLMvgL0m3HD51FhkZEDbP0PciSSdwW3sVdto8DJKfREY6%2BaQcbPo%2FprfbrMOUhPA%2Bk02xFJ%2BxN41%2B%2FLpJ2tFryfx51EjqDKdgvCW48SyY11tT5GRhgg3eR2vjqbwGZWhBnWgF5Ubrg9s9rpw2Vqg0q69vUMq%2BmoOPMpqG9gg%2Bkzw7IzC0nTUw40DuPx7xEes%2BjS3m8Dn9PZfbgeZfYhuE%2FMzu6jO3h%2BqPQiULUDya3Mvp7c2kRQ6XteS5oZPTR6viSwQ7jQPAXvMumPY3EhW0159vcWpLSkJF8zwkfvnvolDbUBPQ8MPzGWO9oLk8Zaxcsn%2F1gcaW3jBzVFALpE%2B%2BKAq8eK38XOtMn257ZUGdiiAjKNOzm8iUvUD1eRlFcQdquI%2Fl4Ef1%2BwFlTzW0d0siydboqQ9Xkf2BGZGRUP920hm1cGZLeUTj3rK6R0fs0YR9odf0FyxcOVhANkHNfcC3qb1htu1QuKvIxVk7UsVavFqVtP8jRAqrRjAMa1V0jf5FUtloMKP51xfrhShVuwJWuCxygrgRtU%2F3wwmrWRvQY6pgEcJFjqe02UafpuZS3KG%2BbmY%2ByxMMLPSjPyt1Bi1C%2FMWYvTvHBEH7s4ENitga6fl8ONg2UOtFa5NCPwB%2Bw%2BPhDuzWBg3s8hoVvPiKPwR7l%2FPw0%2Bs%2BSzC53HRxdTLwVKEH15%2BpQv8QOq3jbR6KpMwrF%2B0xpgyxh1hOfmAtnJrnk5Bg2k6cm2%2BQFBvQIIS%2F8foioEYPxKg9lM7sls%2F122Er1JHKrPnIpw&X-Amz-Signature=f2b18c5565de240bc9f875c8cb64d9a66a6631a2f3b0bdfbcab8145b49a2fac1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC7M3L54%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIDIP15yXKGLTYioNl%2FnvKF4LjYbLLYQ7j6Amze4hd6nkAiBXydnicxxin%2Fg9xNE7M40Uq5WT0TL6PtHbUVR8HsikFyr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMNglEfSqY9JAMuP9vKtwDuGdaxd3a3SAtO0JjYl4IKugWt46OqeTC0t1sSAkf%2FpZu6RtmZ7sHKQmaR1yCgG%2FZNPPylBMTL6FslGsNzLhA9VXnsXLMvgL0m3HD51FhkZEDbP0PciSSdwW3sVdto8DJKfREY6%2BaQcbPo%2FprfbrMOUhPA%2Bk02xFJ%2BxN41%2B%2FLpJ2tFryfx51EjqDKdgvCW48SyY11tT5GRhgg3eR2vjqbwGZWhBnWgF5Ubrg9s9rpw2Vqg0q69vUMq%2BmoOPMpqG9gg%2Bkzw7IzC0nTUw40DuPx7xEes%2BjS3m8Dn9PZfbgeZfYhuE%2FMzu6jO3h%2BqPQiULUDya3Mvp7c2kRQ6XteS5oZPTR6viSwQ7jQPAXvMumPY3EhW0159vcWpLSkJF8zwkfvnvolDbUBPQ8MPzGWO9oLk8Zaxcsn%2F1gcaW3jBzVFALpE%2B%2BKAq8eK38XOtMn257ZUGdiiAjKNOzm8iUvUD1eRlFcQdquI%2Fl4Ef1%2BwFlTzW0d0siydboqQ9Xkf2BGZGRUP920hm1cGZLeUTj3rK6R0fs0YR9odf0FyxcOVhANkHNfcC3qb1htu1QuKvIxVk7UsVavFqVtP8jRAqrRjAMa1V0jf5FUtloMKP51xfrhShVuwJWuCxygrgRtU%2F3wwmrWRvQY6pgEcJFjqe02UafpuZS3KG%2BbmY%2ByxMMLPSjPyt1Bi1C%2FMWYvTvHBEH7s4ENitga6fl8ONg2UOtFa5NCPwB%2Bw%2BPhDuzWBg3s8hoVvPiKPwR7l%2FPw0%2Bs%2BSzC53HRxdTLwVKEH15%2BpQv8QOq3jbR6KpMwrF%2B0xpgyxh1hOfmAtnJrnk5Bg2k6cm2%2BQFBvQIIS%2F8foioEYPxKg9lM7sls%2F122Er1JHKrPnIpw&X-Amz-Signature=46bb1c2bfb8e3d7abe1c44e73aab3bf585d92467aeaf5880f584231efae0be7a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC7M3L54%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIDIP15yXKGLTYioNl%2FnvKF4LjYbLLYQ7j6Amze4hd6nkAiBXydnicxxin%2Fg9xNE7M40Uq5WT0TL6PtHbUVR8HsikFyr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMNglEfSqY9JAMuP9vKtwDuGdaxd3a3SAtO0JjYl4IKugWt46OqeTC0t1sSAkf%2FpZu6RtmZ7sHKQmaR1yCgG%2FZNPPylBMTL6FslGsNzLhA9VXnsXLMvgL0m3HD51FhkZEDbP0PciSSdwW3sVdto8DJKfREY6%2BaQcbPo%2FprfbrMOUhPA%2Bk02xFJ%2BxN41%2B%2FLpJ2tFryfx51EjqDKdgvCW48SyY11tT5GRhgg3eR2vjqbwGZWhBnWgF5Ubrg9s9rpw2Vqg0q69vUMq%2BmoOPMpqG9gg%2Bkzw7IzC0nTUw40DuPx7xEes%2BjS3m8Dn9PZfbgeZfYhuE%2FMzu6jO3h%2BqPQiULUDya3Mvp7c2kRQ6XteS5oZPTR6viSwQ7jQPAXvMumPY3EhW0159vcWpLSkJF8zwkfvnvolDbUBPQ8MPzGWO9oLk8Zaxcsn%2F1gcaW3jBzVFALpE%2B%2BKAq8eK38XOtMn257ZUGdiiAjKNOzm8iUvUD1eRlFcQdquI%2Fl4Ef1%2BwFlTzW0d0siydboqQ9Xkf2BGZGRUP920hm1cGZLeUTj3rK6R0fs0YR9odf0FyxcOVhANkHNfcC3qb1htu1QuKvIxVk7UsVavFqVtP8jRAqrRjAMa1V0jf5FUtloMKP51xfrhShVuwJWuCxygrgRtU%2F3wwmrWRvQY6pgEcJFjqe02UafpuZS3KG%2BbmY%2ByxMMLPSjPyt1Bi1C%2FMWYvTvHBEH7s4ENitga6fl8ONg2UOtFa5NCPwB%2Bw%2BPhDuzWBg3s8hoVvPiKPwR7l%2FPw0%2Bs%2BSzC53HRxdTLwVKEH15%2BpQv8QOq3jbR6KpMwrF%2B0xpgyxh1hOfmAtnJrnk5Bg2k6cm2%2BQFBvQIIS%2F8foioEYPxKg9lM7sls%2F122Er1JHKrPnIpw&X-Amz-Signature=ec41ef1cbfb8a44e6e9f290dda69741f2da5efdda7ec4e2c021781bd52dbc6ef&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC7M3L54%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIDIP15yXKGLTYioNl%2FnvKF4LjYbLLYQ7j6Amze4hd6nkAiBXydnicxxin%2Fg9xNE7M40Uq5WT0TL6PtHbUVR8HsikFyr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMNglEfSqY9JAMuP9vKtwDuGdaxd3a3SAtO0JjYl4IKugWt46OqeTC0t1sSAkf%2FpZu6RtmZ7sHKQmaR1yCgG%2FZNPPylBMTL6FslGsNzLhA9VXnsXLMvgL0m3HD51FhkZEDbP0PciSSdwW3sVdto8DJKfREY6%2BaQcbPo%2FprfbrMOUhPA%2Bk02xFJ%2BxN41%2B%2FLpJ2tFryfx51EjqDKdgvCW48SyY11tT5GRhgg3eR2vjqbwGZWhBnWgF5Ubrg9s9rpw2Vqg0q69vUMq%2BmoOPMpqG9gg%2Bkzw7IzC0nTUw40DuPx7xEes%2BjS3m8Dn9PZfbgeZfYhuE%2FMzu6jO3h%2BqPQiULUDya3Mvp7c2kRQ6XteS5oZPTR6viSwQ7jQPAXvMumPY3EhW0159vcWpLSkJF8zwkfvnvolDbUBPQ8MPzGWO9oLk8Zaxcsn%2F1gcaW3jBzVFALpE%2B%2BKAq8eK38XOtMn257ZUGdiiAjKNOzm8iUvUD1eRlFcQdquI%2Fl4Ef1%2BwFlTzW0d0siydboqQ9Xkf2BGZGRUP920hm1cGZLeUTj3rK6R0fs0YR9odf0FyxcOVhANkHNfcC3qb1htu1QuKvIxVk7UsVavFqVtP8jRAqrRjAMa1V0jf5FUtloMKP51xfrhShVuwJWuCxygrgRtU%2F3wwmrWRvQY6pgEcJFjqe02UafpuZS3KG%2BbmY%2ByxMMLPSjPyt1Bi1C%2FMWYvTvHBEH7s4ENitga6fl8ONg2UOtFa5NCPwB%2Bw%2BPhDuzWBg3s8hoVvPiKPwR7l%2FPw0%2Bs%2BSzC53HRxdTLwVKEH15%2BpQv8QOq3jbR6KpMwrF%2B0xpgyxh1hOfmAtnJrnk5Bg2k6cm2%2BQFBvQIIS%2F8foioEYPxKg9lM7sls%2F122Er1JHKrPnIpw&X-Amz-Signature=7f64102bb6fdd328672e9b047e48f2dafe499d019e27e2b9bd11ece970933bf7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC7M3L54%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIDIP15yXKGLTYioNl%2FnvKF4LjYbLLYQ7j6Amze4hd6nkAiBXydnicxxin%2Fg9xNE7M40Uq5WT0TL6PtHbUVR8HsikFyr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMNglEfSqY9JAMuP9vKtwDuGdaxd3a3SAtO0JjYl4IKugWt46OqeTC0t1sSAkf%2FpZu6RtmZ7sHKQmaR1yCgG%2FZNPPylBMTL6FslGsNzLhA9VXnsXLMvgL0m3HD51FhkZEDbP0PciSSdwW3sVdto8DJKfREY6%2BaQcbPo%2FprfbrMOUhPA%2Bk02xFJ%2BxN41%2B%2FLpJ2tFryfx51EjqDKdgvCW48SyY11tT5GRhgg3eR2vjqbwGZWhBnWgF5Ubrg9s9rpw2Vqg0q69vUMq%2BmoOPMpqG9gg%2Bkzw7IzC0nTUw40DuPx7xEes%2BjS3m8Dn9PZfbgeZfYhuE%2FMzu6jO3h%2BqPQiULUDya3Mvp7c2kRQ6XteS5oZPTR6viSwQ7jQPAXvMumPY3EhW0159vcWpLSkJF8zwkfvnvolDbUBPQ8MPzGWO9oLk8Zaxcsn%2F1gcaW3jBzVFALpE%2B%2BKAq8eK38XOtMn257ZUGdiiAjKNOzm8iUvUD1eRlFcQdquI%2Fl4Ef1%2BwFlTzW0d0siydboqQ9Xkf2BGZGRUP920hm1cGZLeUTj3rK6R0fs0YR9odf0FyxcOVhANkHNfcC3qb1htu1QuKvIxVk7UsVavFqVtP8jRAqrRjAMa1V0jf5FUtloMKP51xfrhShVuwJWuCxygrgRtU%2F3wwmrWRvQY6pgEcJFjqe02UafpuZS3KG%2BbmY%2ByxMMLPSjPyt1Bi1C%2FMWYvTvHBEH7s4ENitga6fl8ONg2UOtFa5NCPwB%2Bw%2BPhDuzWBg3s8hoVvPiKPwR7l%2FPw0%2Bs%2BSzC53HRxdTLwVKEH15%2BpQv8QOq3jbR6KpMwrF%2B0xpgyxh1hOfmAtnJrnk5Bg2k6cm2%2BQFBvQIIS%2F8foioEYPxKg9lM7sls%2F122Er1JHKrPnIpw&X-Amz-Signature=192f715cae71d62b089b8d9fd0f8b0697137608b595bbcfc19787c0fd0fece01&X-Amz-SignedHeaders=host&x-id=GetObject)
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


