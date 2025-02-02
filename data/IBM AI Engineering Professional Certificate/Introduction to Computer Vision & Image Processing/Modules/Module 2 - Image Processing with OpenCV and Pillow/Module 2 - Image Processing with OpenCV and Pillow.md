

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAEIQ2SH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFUd0ghyh2l0dAT%2FVq2IHV4xu7N7TJY62byydY1IV4uAiEAnhc%2Fl%2FR0%2FIQ%2FqGEo3VIdtNTo830H%2F16XFkiBvor%2FZpAqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPH%2F7tEeAJq%2Bmu2vkSrcA%2F68c7L6YukymbhTKPQW2twx4OLw2K%2FEvocvUj1KXaTB%2F39HkZ8MldCkqsbzH7HWa3JZSYophM%2Fm2p01c29kVIIhwYD59llQgBYRSP%2B32zKcMkr8w8SVOzpoLwbV%2Bb8A72C8s3jkNPeqzfZdVBvN4T%2B5saDom0DWAled3EWNoN51NVQWXk80Dpv1W7I231RXOmnG6kidxNPn4sKCZ3G97A36fLrBvYiEE5MJiEBigwt4yPTvnlgpmZ5GXUqa7fmvivdHcsA0sxig3Jx3pEZlc0q%2BAn7YIYdoP1fM4Yd99CHl9GNWH4oIgv1blC0K3m1HiSjzZ7v7v%2FheWj1NlQZASzOVLslH5DfIOoN4m6JMq7KyOq87WcWG0WLxodogFitz3ERo3IZQhm4PR%2BMMe8KjxIcTJpGpHjoE6cgPiorHZUbMemyIml%2FgYd4doIlVZy3pKm913aCYBI1wsAOW9xC4WzhwDYmjHo%2FbkW0JutmYRIo0xeeQdX99bQ72qABrthokqpiPF8Y%2BXETsDzP7YBcOC3ft1Unl5DdkkaYdXN%2FOpyGN8BEboqqIjlb7L4O5sadEQ5QwIfhj2fQyExPy9ytEGZA%2FFhzJ%2BChQlg35yaoTaHwwTO6eDGAxyMsGIMoTMKfk%2F7wGOqUB1ebdktl9n3vaLUYvciHIpBImYopri3WnpQqsgQwh2sCPaXYn%2Blgu9ifAdqgk6TvwIuJOyNxDmN7LGQKpxQcSlrazZm8bQZ6DG0p1Zss3jkLBZHHFlkgABSwvWpTU5klrR%2FGZkRdHbFImpxEWRusvZgAzuNaaPCTD7Qr5G8kUw5l%2BP7A5FpEAMqF90UobnvqXlnb0yG9SHwNHuOINIXHcgCtcVsFI&X-Amz-Signature=75b43d970f062bc43a777746b8ed3661e8be8714b8f1eddba52896a99164c102&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=83f1e779a01361b4107e3dbbc4785c0f307b0d9ff84d2ea412a4bf896b58cfda&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=c98704df175145f1362d02f070ac9767d48cfeb02811a9981015fe4b60702f41&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=473d8b4160baf6219ecf61d4ade8f1e2c3ecbcdc0ea0f953568f457e30ec7210&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=979957a2568b4b1ee9a3b0d54cfab66c7ceecf9e1d00ecedd6211a6f568d9b35&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=5a1e32fd3b965cc1d2641ce7b4bea90e56b23ade272cba6a28d82e0f373b8399&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAEIQ2SH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFUd0ghyh2l0dAT%2FVq2IHV4xu7N7TJY62byydY1IV4uAiEAnhc%2Fl%2FR0%2FIQ%2FqGEo3VIdtNTo830H%2F16XFkiBvor%2FZpAqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPH%2F7tEeAJq%2Bmu2vkSrcA%2F68c7L6YukymbhTKPQW2twx4OLw2K%2FEvocvUj1KXaTB%2F39HkZ8MldCkqsbzH7HWa3JZSYophM%2Fm2p01c29kVIIhwYD59llQgBYRSP%2B32zKcMkr8w8SVOzpoLwbV%2Bb8A72C8s3jkNPeqzfZdVBvN4T%2B5saDom0DWAled3EWNoN51NVQWXk80Dpv1W7I231RXOmnG6kidxNPn4sKCZ3G97A36fLrBvYiEE5MJiEBigwt4yPTvnlgpmZ5GXUqa7fmvivdHcsA0sxig3Jx3pEZlc0q%2BAn7YIYdoP1fM4Yd99CHl9GNWH4oIgv1blC0K3m1HiSjzZ7v7v%2FheWj1NlQZASzOVLslH5DfIOoN4m6JMq7KyOq87WcWG0WLxodogFitz3ERo3IZQhm4PR%2BMMe8KjxIcTJpGpHjoE6cgPiorHZUbMemyIml%2FgYd4doIlVZy3pKm913aCYBI1wsAOW9xC4WzhwDYmjHo%2FbkW0JutmYRIo0xeeQdX99bQ72qABrthokqpiPF8Y%2BXETsDzP7YBcOC3ft1Unl5DdkkaYdXN%2FOpyGN8BEboqqIjlb7L4O5sadEQ5QwIfhj2fQyExPy9ytEGZA%2FFhzJ%2BChQlg35yaoTaHwwTO6eDGAxyMsGIMoTMKfk%2F7wGOqUB1ebdktl9n3vaLUYvciHIpBImYopri3WnpQqsgQwh2sCPaXYn%2Blgu9ifAdqgk6TvwIuJOyNxDmN7LGQKpxQcSlrazZm8bQZ6DG0p1Zss3jkLBZHHFlkgABSwvWpTU5klrR%2FGZkRdHbFImpxEWRusvZgAzuNaaPCTD7Qr5G8kUw5l%2BP7A5FpEAMqF90UobnvqXlnb0yG9SHwNHuOINIXHcgCtcVsFI&X-Amz-Signature=bf24f23562f1839893f37e9ac303b17235d129c7c7a93f9fa22c4c992a0144f4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAEIQ2SH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFUd0ghyh2l0dAT%2FVq2IHV4xu7N7TJY62byydY1IV4uAiEAnhc%2Fl%2FR0%2FIQ%2FqGEo3VIdtNTo830H%2F16XFkiBvor%2FZpAqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPH%2F7tEeAJq%2Bmu2vkSrcA%2F68c7L6YukymbhTKPQW2twx4OLw2K%2FEvocvUj1KXaTB%2F39HkZ8MldCkqsbzH7HWa3JZSYophM%2Fm2p01c29kVIIhwYD59llQgBYRSP%2B32zKcMkr8w8SVOzpoLwbV%2Bb8A72C8s3jkNPeqzfZdVBvN4T%2B5saDom0DWAled3EWNoN51NVQWXk80Dpv1W7I231RXOmnG6kidxNPn4sKCZ3G97A36fLrBvYiEE5MJiEBigwt4yPTvnlgpmZ5GXUqa7fmvivdHcsA0sxig3Jx3pEZlc0q%2BAn7YIYdoP1fM4Yd99CHl9GNWH4oIgv1blC0K3m1HiSjzZ7v7v%2FheWj1NlQZASzOVLslH5DfIOoN4m6JMq7KyOq87WcWG0WLxodogFitz3ERo3IZQhm4PR%2BMMe8KjxIcTJpGpHjoE6cgPiorHZUbMemyIml%2FgYd4doIlVZy3pKm913aCYBI1wsAOW9xC4WzhwDYmjHo%2FbkW0JutmYRIo0xeeQdX99bQ72qABrthokqpiPF8Y%2BXETsDzP7YBcOC3ft1Unl5DdkkaYdXN%2FOpyGN8BEboqqIjlb7L4O5sadEQ5QwIfhj2fQyExPy9ytEGZA%2FFhzJ%2BChQlg35yaoTaHwwTO6eDGAxyMsGIMoTMKfk%2F7wGOqUB1ebdktl9n3vaLUYvciHIpBImYopri3WnpQqsgQwh2sCPaXYn%2Blgu9ifAdqgk6TvwIuJOyNxDmN7LGQKpxQcSlrazZm8bQZ6DG0p1Zss3jkLBZHHFlkgABSwvWpTU5klrR%2FGZkRdHbFImpxEWRusvZgAzuNaaPCTD7Qr5G8kUw5l%2BP7A5FpEAMqF90UobnvqXlnb0yG9SHwNHuOINIXHcgCtcVsFI&X-Amz-Signature=56057730d0b0cce32094a839a0a26fe4726f60570d4bb84dd610873ab9fcd4bf&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAEIQ2SH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFUd0ghyh2l0dAT%2FVq2IHV4xu7N7TJY62byydY1IV4uAiEAnhc%2Fl%2FR0%2FIQ%2FqGEo3VIdtNTo830H%2F16XFkiBvor%2FZpAqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPH%2F7tEeAJq%2Bmu2vkSrcA%2F68c7L6YukymbhTKPQW2twx4OLw2K%2FEvocvUj1KXaTB%2F39HkZ8MldCkqsbzH7HWa3JZSYophM%2Fm2p01c29kVIIhwYD59llQgBYRSP%2B32zKcMkr8w8SVOzpoLwbV%2Bb8A72C8s3jkNPeqzfZdVBvN4T%2B5saDom0DWAled3EWNoN51NVQWXk80Dpv1W7I231RXOmnG6kidxNPn4sKCZ3G97A36fLrBvYiEE5MJiEBigwt4yPTvnlgpmZ5GXUqa7fmvivdHcsA0sxig3Jx3pEZlc0q%2BAn7YIYdoP1fM4Yd99CHl9GNWH4oIgv1blC0K3m1HiSjzZ7v7v%2FheWj1NlQZASzOVLslH5DfIOoN4m6JMq7KyOq87WcWG0WLxodogFitz3ERo3IZQhm4PR%2BMMe8KjxIcTJpGpHjoE6cgPiorHZUbMemyIml%2FgYd4doIlVZy3pKm913aCYBI1wsAOW9xC4WzhwDYmjHo%2FbkW0JutmYRIo0xeeQdX99bQ72qABrthokqpiPF8Y%2BXETsDzP7YBcOC3ft1Unl5DdkkaYdXN%2FOpyGN8BEboqqIjlb7L4O5sadEQ5QwIfhj2fQyExPy9ytEGZA%2FFhzJ%2BChQlg35yaoTaHwwTO6eDGAxyMsGIMoTMKfk%2F7wGOqUB1ebdktl9n3vaLUYvciHIpBImYopri3WnpQqsgQwh2sCPaXYn%2Blgu9ifAdqgk6TvwIuJOyNxDmN7LGQKpxQcSlrazZm8bQZ6DG0p1Zss3jkLBZHHFlkgABSwvWpTU5klrR%2FGZkRdHbFImpxEWRusvZgAzuNaaPCTD7Qr5G8kUw5l%2BP7A5FpEAMqF90UobnvqXlnb0yG9SHwNHuOINIXHcgCtcVsFI&X-Amz-Signature=7451d1de24d50dcd92e51b0ff4f8d4374e67ce5e51b8cef8f1a821a8b1777212&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAEIQ2SH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFUd0ghyh2l0dAT%2FVq2IHV4xu7N7TJY62byydY1IV4uAiEAnhc%2Fl%2FR0%2FIQ%2FqGEo3VIdtNTo830H%2F16XFkiBvor%2FZpAqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPH%2F7tEeAJq%2Bmu2vkSrcA%2F68c7L6YukymbhTKPQW2twx4OLw2K%2FEvocvUj1KXaTB%2F39HkZ8MldCkqsbzH7HWa3JZSYophM%2Fm2p01c29kVIIhwYD59llQgBYRSP%2B32zKcMkr8w8SVOzpoLwbV%2Bb8A72C8s3jkNPeqzfZdVBvN4T%2B5saDom0DWAled3EWNoN51NVQWXk80Dpv1W7I231RXOmnG6kidxNPn4sKCZ3G97A36fLrBvYiEE5MJiEBigwt4yPTvnlgpmZ5GXUqa7fmvivdHcsA0sxig3Jx3pEZlc0q%2BAn7YIYdoP1fM4Yd99CHl9GNWH4oIgv1blC0K3m1HiSjzZ7v7v%2FheWj1NlQZASzOVLslH5DfIOoN4m6JMq7KyOq87WcWG0WLxodogFitz3ERo3IZQhm4PR%2BMMe8KjxIcTJpGpHjoE6cgPiorHZUbMemyIml%2FgYd4doIlVZy3pKm913aCYBI1wsAOW9xC4WzhwDYmjHo%2FbkW0JutmYRIo0xeeQdX99bQ72qABrthokqpiPF8Y%2BXETsDzP7YBcOC3ft1Unl5DdkkaYdXN%2FOpyGN8BEboqqIjlb7L4O5sadEQ5QwIfhj2fQyExPy9ytEGZA%2FFhzJ%2BChQlg35yaoTaHwwTO6eDGAxyMsGIMoTMKfk%2F7wGOqUB1ebdktl9n3vaLUYvciHIpBImYopri3WnpQqsgQwh2sCPaXYn%2Blgu9ifAdqgk6TvwIuJOyNxDmN7LGQKpxQcSlrazZm8bQZ6DG0p1Zss3jkLBZHHFlkgABSwvWpTU5klrR%2FGZkRdHbFImpxEWRusvZgAzuNaaPCTD7Qr5G8kUw5l%2BP7A5FpEAMqF90UobnvqXlnb0yG9SHwNHuOINIXHcgCtcVsFI&X-Amz-Signature=44ad046561994f35dbf1f4b0695a260f352e7549d25e73552bd2e4aec19dc332&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAEIQ2SH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFUd0ghyh2l0dAT%2FVq2IHV4xu7N7TJY62byydY1IV4uAiEAnhc%2Fl%2FR0%2FIQ%2FqGEo3VIdtNTo830H%2F16XFkiBvor%2FZpAqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPH%2F7tEeAJq%2Bmu2vkSrcA%2F68c7L6YukymbhTKPQW2twx4OLw2K%2FEvocvUj1KXaTB%2F39HkZ8MldCkqsbzH7HWa3JZSYophM%2Fm2p01c29kVIIhwYD59llQgBYRSP%2B32zKcMkr8w8SVOzpoLwbV%2Bb8A72C8s3jkNPeqzfZdVBvN4T%2B5saDom0DWAled3EWNoN51NVQWXk80Dpv1W7I231RXOmnG6kidxNPn4sKCZ3G97A36fLrBvYiEE5MJiEBigwt4yPTvnlgpmZ5GXUqa7fmvivdHcsA0sxig3Jx3pEZlc0q%2BAn7YIYdoP1fM4Yd99CHl9GNWH4oIgv1blC0K3m1HiSjzZ7v7v%2FheWj1NlQZASzOVLslH5DfIOoN4m6JMq7KyOq87WcWG0WLxodogFitz3ERo3IZQhm4PR%2BMMe8KjxIcTJpGpHjoE6cgPiorHZUbMemyIml%2FgYd4doIlVZy3pKm913aCYBI1wsAOW9xC4WzhwDYmjHo%2FbkW0JutmYRIo0xeeQdX99bQ72qABrthokqpiPF8Y%2BXETsDzP7YBcOC3ft1Unl5DdkkaYdXN%2FOpyGN8BEboqqIjlb7L4O5sadEQ5QwIfhj2fQyExPy9ytEGZA%2FFhzJ%2BChQlg35yaoTaHwwTO6eDGAxyMsGIMoTMKfk%2F7wGOqUB1ebdktl9n3vaLUYvciHIpBImYopri3WnpQqsgQwh2sCPaXYn%2Blgu9ifAdqgk6TvwIuJOyNxDmN7LGQKpxQcSlrazZm8bQZ6DG0p1Zss3jkLBZHHFlkgABSwvWpTU5klrR%2FGZkRdHbFImpxEWRusvZgAzuNaaPCTD7Qr5G8kUw5l%2BP7A5FpEAMqF90UobnvqXlnb0yG9SHwNHuOINIXHcgCtcVsFI&X-Amz-Signature=c34995eb2237465b7a96387ca034d118987cae0b480a67d5d66aa29a66dadd50&X-Amz-SignedHeaders=host&x-id=GetObject)
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


