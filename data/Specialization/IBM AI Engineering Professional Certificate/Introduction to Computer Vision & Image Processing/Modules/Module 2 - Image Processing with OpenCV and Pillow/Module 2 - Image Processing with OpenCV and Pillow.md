

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSYRBOA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIEZCe6Rvo4r9AUm2AGscsIeumLnnsDkgufyyFneCLS66AiBXwxDStOzCwtXvBB4d3TOSd9PYLmmG6vqYF2WjI2fQeCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV%2Byb1FTd%2BiXIPHMYKtwDXQPpw52ShJqdM%2BweIeMV9F0H6wt45J%2FkZLmvWArD0x8dwXdsYZbYVlPAR9QDO%2FY%2BMBmOWwKDxqqXlwpiMvJyqvTpXi9b5XxpvDERyEh6LFdcUmjnMxUwLmPZDOgvDnR3grU1k%2BqMSJTibuWJVTAFJpxfnWIAv5sC5B2Y7YIasPPmhUVOhi5SdjmKuSe5zLXRYtiitguPpwQL1KmhXyJ6N20%2BYgpjJ29Tb6dBvhUF4UOrw38eJALyRjIXBTcErXnuKD98fl0cwyffVgUPhoz4DSYWDci8Joir8vYBaX4YFj47eAG3CygwJjLZnoDpUdQ%2BtjCqYYGRl96uM394WB7pORBmoG%2F1BITbrQc8XpDWtbO%2FXLb8Sx4rsr%2Bt9fzGFiDAApGza9RJpSkyE3p9fA6askays5oOEsBCGlI1%2F1j0ANeSbgkYGsmZBIP027rFauoScLe%2Fe92dGNxfi5cB7kInoYLVeVf6LGO7U6Xbn%2F%2F4T%2BaUPw2r8favuTSBRM3k4voO6PWFlqLh1Me2mSmheaYa9khRMRFuEkb0lomhTdinX%2FU9Y%2BTI27OIeSCFWIiR7NX2qAPbfRrFI3BBwIUnuKsMvXDvp4pDF1kTFLrfSvj4akkESQRdIMd8rLE6krIwp%2BjlvAY6pgEL1xsSuUQfHeKKczU3mS%2BOF2hyW5U%2BbWWo%2F9dUNXQWApjrbUdCN2csZWhgh0zzOa8AzK3WDDZSXi%2FIUEU0SUX14VAw9B1XAlvG483cKdEJIEVMqZyhno%2Fvqax4Phr1u8o7yOYNiPsUUTK4%2F8TBiOkjEyFng6JjVhmykqTzW47BRRcDBpb%2B6G4WZGiw%2B06tg%2BI0Fkt0054B7cW9vEGbBa%2BOAEvZ4K4A&X-Amz-Signature=2a8009b09ddb09f50772afd0fc2e21b8fd9e385c4e357f0e8025c3acbe3b4d6d&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOLRWK3R%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIDZNaqevd3QLfcv354zCcX5%2BSQ%2F%2BZmKyF9dFCui4lUolAiEAs%2FA%2FqB3msxmd%2BrwDsJx0JHIefXjuxXKxtg08grHn2SgqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMH0TuRKu0CeWRFE3SrcA%2F5SUvdrFpl4x2lMqdmNLeXEm%2FXuNZOMxZElHJ0hFFrrilXPVsWcE0F%2BrUl7YkU8j3NE%2FjQ7DZ%2Br6PTyIr%2BlZLTl6lM%2FE9W4BfgFxIHeu4kSgThJOLuelCYZu%2BsHpqE5kf9%2FtK8ngDQXVAgp0E96iOgm82Yj0E7tyE8BGtBD0I1t0uLhf%2FjUbuHWFw%2BdPaMl%2B7ReCm2jyE7KdjQ4BOWC1exh%2FsTTfQnUyKmDFiDlXPxXMAu%2FYJonDD6Lj9fawX4LWpvis3t%2FGJvXBORoWRZTondbzDQeN%2FjsKOV4uVqPSxlu%2F%2FVNOIkt3QVXr4x6A6zveOXU1F1X0Ir9DdwbqQfVUaeG6gRLKWyjbXDoyTB9qk31ZE6hOKqScoi3H7rU2m9RUE8lDvKFoNwESJaf9r2Df2tgcfOV7amed92e0pgtc0u8vOByPLTuiY5yDH6l%2BuSJ8YrpXL5iYrqVpZl1C9AnSsswFXiD8i0FBz0GCdRkCUzLMOTRFXPL4070ShDIve%2Foj672YbYORykzfT5t5K7Xsbiiq609yNC3anRS3xGb07F%2FXal7vjcmjo0Xdj%2BkECbulxpIM0FdFUNTrJEEh8Z%2BCfT9y0jHv7jaxUMfxB5N5TBsVD0NUXkjBVCkd4ocMNjn5bwGOqUBPyQyKCMjG4V1TCiaeKhzixsp6ml%2BFyUfd0PeL2dssyvKooWNc2LJgX1cx2p5I9qq5DU%2BjkQGXj9tgSd36%2Fel01WdXFXOwQpOjWWpMjoGrkdc%2FOeMPqSDXMi0zy0sEu6iyyFVLIoFMLXrKLNCDeC6UdI6AJpnHgrC1xsa2cSnhoBmp%2FFZxuMH4IWt0sOgEcsup2Pkb6AdC6CAeQmyv%2BzfL%2FHASZbH&X-Amz-Signature=3f0d226e99ec7acb740ab0b2f636823bd788402a58a1c3bf1cd772cbb9330802&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOLRWK3R%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIDZNaqevd3QLfcv354zCcX5%2BSQ%2F%2BZmKyF9dFCui4lUolAiEAs%2FA%2FqB3msxmd%2BrwDsJx0JHIefXjuxXKxtg08grHn2SgqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMH0TuRKu0CeWRFE3SrcA%2F5SUvdrFpl4x2lMqdmNLeXEm%2FXuNZOMxZElHJ0hFFrrilXPVsWcE0F%2BrUl7YkU8j3NE%2FjQ7DZ%2Br6PTyIr%2BlZLTl6lM%2FE9W4BfgFxIHeu4kSgThJOLuelCYZu%2BsHpqE5kf9%2FtK8ngDQXVAgp0E96iOgm82Yj0E7tyE8BGtBD0I1t0uLhf%2FjUbuHWFw%2BdPaMl%2B7ReCm2jyE7KdjQ4BOWC1exh%2FsTTfQnUyKmDFiDlXPxXMAu%2FYJonDD6Lj9fawX4LWpvis3t%2FGJvXBORoWRZTondbzDQeN%2FjsKOV4uVqPSxlu%2F%2FVNOIkt3QVXr4x6A6zveOXU1F1X0Ir9DdwbqQfVUaeG6gRLKWyjbXDoyTB9qk31ZE6hOKqScoi3H7rU2m9RUE8lDvKFoNwESJaf9r2Df2tgcfOV7amed92e0pgtc0u8vOByPLTuiY5yDH6l%2BuSJ8YrpXL5iYrqVpZl1C9AnSsswFXiD8i0FBz0GCdRkCUzLMOTRFXPL4070ShDIve%2Foj672YbYORykzfT5t5K7Xsbiiq609yNC3anRS3xGb07F%2FXal7vjcmjo0Xdj%2BkECbulxpIM0FdFUNTrJEEh8Z%2BCfT9y0jHv7jaxUMfxB5N5TBsVD0NUXkjBVCkd4ocMNjn5bwGOqUBPyQyKCMjG4V1TCiaeKhzixsp6ml%2BFyUfd0PeL2dssyvKooWNc2LJgX1cx2p5I9qq5DU%2BjkQGXj9tgSd36%2Fel01WdXFXOwQpOjWWpMjoGrkdc%2FOeMPqSDXMi0zy0sEu6iyyFVLIoFMLXrKLNCDeC6UdI6AJpnHgrC1xsa2cSnhoBmp%2FFZxuMH4IWt0sOgEcsup2Pkb6AdC6CAeQmyv%2BzfL%2FHASZbH&X-Amz-Signature=f3cc6e744f5a27d1ce7120473e2c25003d936c3098c60025aa05251503b01a12&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOLRWK3R%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIDZNaqevd3QLfcv354zCcX5%2BSQ%2F%2BZmKyF9dFCui4lUolAiEAs%2FA%2FqB3msxmd%2BrwDsJx0JHIefXjuxXKxtg08grHn2SgqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMH0TuRKu0CeWRFE3SrcA%2F5SUvdrFpl4x2lMqdmNLeXEm%2FXuNZOMxZElHJ0hFFrrilXPVsWcE0F%2BrUl7YkU8j3NE%2FjQ7DZ%2Br6PTyIr%2BlZLTl6lM%2FE9W4BfgFxIHeu4kSgThJOLuelCYZu%2BsHpqE5kf9%2FtK8ngDQXVAgp0E96iOgm82Yj0E7tyE8BGtBD0I1t0uLhf%2FjUbuHWFw%2BdPaMl%2B7ReCm2jyE7KdjQ4BOWC1exh%2FsTTfQnUyKmDFiDlXPxXMAu%2FYJonDD6Lj9fawX4LWpvis3t%2FGJvXBORoWRZTondbzDQeN%2FjsKOV4uVqPSxlu%2F%2FVNOIkt3QVXr4x6A6zveOXU1F1X0Ir9DdwbqQfVUaeG6gRLKWyjbXDoyTB9qk31ZE6hOKqScoi3H7rU2m9RUE8lDvKFoNwESJaf9r2Df2tgcfOV7amed92e0pgtc0u8vOByPLTuiY5yDH6l%2BuSJ8YrpXL5iYrqVpZl1C9AnSsswFXiD8i0FBz0GCdRkCUzLMOTRFXPL4070ShDIve%2Foj672YbYORykzfT5t5K7Xsbiiq609yNC3anRS3xGb07F%2FXal7vjcmjo0Xdj%2BkECbulxpIM0FdFUNTrJEEh8Z%2BCfT9y0jHv7jaxUMfxB5N5TBsVD0NUXkjBVCkd4ocMNjn5bwGOqUBPyQyKCMjG4V1TCiaeKhzixsp6ml%2BFyUfd0PeL2dssyvKooWNc2LJgX1cx2p5I9qq5DU%2BjkQGXj9tgSd36%2Fel01WdXFXOwQpOjWWpMjoGrkdc%2FOeMPqSDXMi0zy0sEu6iyyFVLIoFMLXrKLNCDeC6UdI6AJpnHgrC1xsa2cSnhoBmp%2FFZxuMH4IWt0sOgEcsup2Pkb6AdC6CAeQmyv%2BzfL%2FHASZbH&X-Amz-Signature=2422d3305dd7dd36b23594f05b58231f50758ea8955737a1f1f43f1608b6f220&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOLRWK3R%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIDZNaqevd3QLfcv354zCcX5%2BSQ%2F%2BZmKyF9dFCui4lUolAiEAs%2FA%2FqB3msxmd%2BrwDsJx0JHIefXjuxXKxtg08grHn2SgqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMH0TuRKu0CeWRFE3SrcA%2F5SUvdrFpl4x2lMqdmNLeXEm%2FXuNZOMxZElHJ0hFFrrilXPVsWcE0F%2BrUl7YkU8j3NE%2FjQ7DZ%2Br6PTyIr%2BlZLTl6lM%2FE9W4BfgFxIHeu4kSgThJOLuelCYZu%2BsHpqE5kf9%2FtK8ngDQXVAgp0E96iOgm82Yj0E7tyE8BGtBD0I1t0uLhf%2FjUbuHWFw%2BdPaMl%2B7ReCm2jyE7KdjQ4BOWC1exh%2FsTTfQnUyKmDFiDlXPxXMAu%2FYJonDD6Lj9fawX4LWpvis3t%2FGJvXBORoWRZTondbzDQeN%2FjsKOV4uVqPSxlu%2F%2FVNOIkt3QVXr4x6A6zveOXU1F1X0Ir9DdwbqQfVUaeG6gRLKWyjbXDoyTB9qk31ZE6hOKqScoi3H7rU2m9RUE8lDvKFoNwESJaf9r2Df2tgcfOV7amed92e0pgtc0u8vOByPLTuiY5yDH6l%2BuSJ8YrpXL5iYrqVpZl1C9AnSsswFXiD8i0FBz0GCdRkCUzLMOTRFXPL4070ShDIve%2Foj672YbYORykzfT5t5K7Xsbiiq609yNC3anRS3xGb07F%2FXal7vjcmjo0Xdj%2BkECbulxpIM0FdFUNTrJEEh8Z%2BCfT9y0jHv7jaxUMfxB5N5TBsVD0NUXkjBVCkd4ocMNjn5bwGOqUBPyQyKCMjG4V1TCiaeKhzixsp6ml%2BFyUfd0PeL2dssyvKooWNc2LJgX1cx2p5I9qq5DU%2BjkQGXj9tgSd36%2Fel01WdXFXOwQpOjWWpMjoGrkdc%2FOeMPqSDXMi0zy0sEu6iyyFVLIoFMLXrKLNCDeC6UdI6AJpnHgrC1xsa2cSnhoBmp%2FFZxuMH4IWt0sOgEcsup2Pkb6AdC6CAeQmyv%2BzfL%2FHASZbH&X-Amz-Signature=77d75ec6013edd6d2ef03d4b3afae92c1548aa80e2e7565fc5c5f816fdabfc00&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOLRWK3R%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIDZNaqevd3QLfcv354zCcX5%2BSQ%2F%2BZmKyF9dFCui4lUolAiEAs%2FA%2FqB3msxmd%2BrwDsJx0JHIefXjuxXKxtg08grHn2SgqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMH0TuRKu0CeWRFE3SrcA%2F5SUvdrFpl4x2lMqdmNLeXEm%2FXuNZOMxZElHJ0hFFrrilXPVsWcE0F%2BrUl7YkU8j3NE%2FjQ7DZ%2Br6PTyIr%2BlZLTl6lM%2FE9W4BfgFxIHeu4kSgThJOLuelCYZu%2BsHpqE5kf9%2FtK8ngDQXVAgp0E96iOgm82Yj0E7tyE8BGtBD0I1t0uLhf%2FjUbuHWFw%2BdPaMl%2B7ReCm2jyE7KdjQ4BOWC1exh%2FsTTfQnUyKmDFiDlXPxXMAu%2FYJonDD6Lj9fawX4LWpvis3t%2FGJvXBORoWRZTondbzDQeN%2FjsKOV4uVqPSxlu%2F%2FVNOIkt3QVXr4x6A6zveOXU1F1X0Ir9DdwbqQfVUaeG6gRLKWyjbXDoyTB9qk31ZE6hOKqScoi3H7rU2m9RUE8lDvKFoNwESJaf9r2Df2tgcfOV7amed92e0pgtc0u8vOByPLTuiY5yDH6l%2BuSJ8YrpXL5iYrqVpZl1C9AnSsswFXiD8i0FBz0GCdRkCUzLMOTRFXPL4070ShDIve%2Foj672YbYORykzfT5t5K7Xsbiiq609yNC3anRS3xGb07F%2FXal7vjcmjo0Xdj%2BkECbulxpIM0FdFUNTrJEEh8Z%2BCfT9y0jHv7jaxUMfxB5N5TBsVD0NUXkjBVCkd4ocMNjn5bwGOqUBPyQyKCMjG4V1TCiaeKhzixsp6ml%2BFyUfd0PeL2dssyvKooWNc2LJgX1cx2p5I9qq5DU%2BjkQGXj9tgSd36%2Fel01WdXFXOwQpOjWWpMjoGrkdc%2FOeMPqSDXMi0zy0sEu6iyyFVLIoFMLXrKLNCDeC6UdI6AJpnHgrC1xsa2cSnhoBmp%2FFZxuMH4IWt0sOgEcsup2Pkb6AdC6CAeQmyv%2BzfL%2FHASZbH&X-Amz-Signature=c37b9c3f2d820fbea97bb64eacb393c5f35bf8ec51c7f57ad34da5c47a9b82b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSYRBOA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIEZCe6Rvo4r9AUm2AGscsIeumLnnsDkgufyyFneCLS66AiBXwxDStOzCwtXvBB4d3TOSd9PYLmmG6vqYF2WjI2fQeCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV%2Byb1FTd%2BiXIPHMYKtwDXQPpw52ShJqdM%2BweIeMV9F0H6wt45J%2FkZLmvWArD0x8dwXdsYZbYVlPAR9QDO%2FY%2BMBmOWwKDxqqXlwpiMvJyqvTpXi9b5XxpvDERyEh6LFdcUmjnMxUwLmPZDOgvDnR3grU1k%2BqMSJTibuWJVTAFJpxfnWIAv5sC5B2Y7YIasPPmhUVOhi5SdjmKuSe5zLXRYtiitguPpwQL1KmhXyJ6N20%2BYgpjJ29Tb6dBvhUF4UOrw38eJALyRjIXBTcErXnuKD98fl0cwyffVgUPhoz4DSYWDci8Joir8vYBaX4YFj47eAG3CygwJjLZnoDpUdQ%2BtjCqYYGRl96uM394WB7pORBmoG%2F1BITbrQc8XpDWtbO%2FXLb8Sx4rsr%2Bt9fzGFiDAApGza9RJpSkyE3p9fA6askays5oOEsBCGlI1%2F1j0ANeSbgkYGsmZBIP027rFauoScLe%2Fe92dGNxfi5cB7kInoYLVeVf6LGO7U6Xbn%2F%2F4T%2BaUPw2r8favuTSBRM3k4voO6PWFlqLh1Me2mSmheaYa9khRMRFuEkb0lomhTdinX%2FU9Y%2BTI27OIeSCFWIiR7NX2qAPbfRrFI3BBwIUnuKsMvXDvp4pDF1kTFLrfSvj4akkESQRdIMd8rLE6krIwp%2BjlvAY6pgEL1xsSuUQfHeKKczU3mS%2BOF2hyW5U%2BbWWo%2F9dUNXQWApjrbUdCN2csZWhgh0zzOa8AzK3WDDZSXi%2FIUEU0SUX14VAw9B1XAlvG483cKdEJIEVMqZyhno%2Fvqax4Phr1u8o7yOYNiPsUUTK4%2F8TBiOkjEyFng6JjVhmykqTzW47BRRcDBpb%2B6G4WZGiw%2B06tg%2BI0Fkt0054B7cW9vEGbBa%2BOAEvZ4K4A&X-Amz-Signature=47399e4773f4d505840b96715c7a521aa41ade7681a15d0d78207829d3bb2d2b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSYRBOA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIEZCe6Rvo4r9AUm2AGscsIeumLnnsDkgufyyFneCLS66AiBXwxDStOzCwtXvBB4d3TOSd9PYLmmG6vqYF2WjI2fQeCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV%2Byb1FTd%2BiXIPHMYKtwDXQPpw52ShJqdM%2BweIeMV9F0H6wt45J%2FkZLmvWArD0x8dwXdsYZbYVlPAR9QDO%2FY%2BMBmOWwKDxqqXlwpiMvJyqvTpXi9b5XxpvDERyEh6LFdcUmjnMxUwLmPZDOgvDnR3grU1k%2BqMSJTibuWJVTAFJpxfnWIAv5sC5B2Y7YIasPPmhUVOhi5SdjmKuSe5zLXRYtiitguPpwQL1KmhXyJ6N20%2BYgpjJ29Tb6dBvhUF4UOrw38eJALyRjIXBTcErXnuKD98fl0cwyffVgUPhoz4DSYWDci8Joir8vYBaX4YFj47eAG3CygwJjLZnoDpUdQ%2BtjCqYYGRl96uM394WB7pORBmoG%2F1BITbrQc8XpDWtbO%2FXLb8Sx4rsr%2Bt9fzGFiDAApGza9RJpSkyE3p9fA6askays5oOEsBCGlI1%2F1j0ANeSbgkYGsmZBIP027rFauoScLe%2Fe92dGNxfi5cB7kInoYLVeVf6LGO7U6Xbn%2F%2F4T%2BaUPw2r8favuTSBRM3k4voO6PWFlqLh1Me2mSmheaYa9khRMRFuEkb0lomhTdinX%2FU9Y%2BTI27OIeSCFWIiR7NX2qAPbfRrFI3BBwIUnuKsMvXDvp4pDF1kTFLrfSvj4akkESQRdIMd8rLE6krIwp%2BjlvAY6pgEL1xsSuUQfHeKKczU3mS%2BOF2hyW5U%2BbWWo%2F9dUNXQWApjrbUdCN2csZWhgh0zzOa8AzK3WDDZSXi%2FIUEU0SUX14VAw9B1XAlvG483cKdEJIEVMqZyhno%2Fvqax4Phr1u8o7yOYNiPsUUTK4%2F8TBiOkjEyFng6JjVhmykqTzW47BRRcDBpb%2B6G4WZGiw%2B06tg%2BI0Fkt0054B7cW9vEGbBa%2BOAEvZ4K4A&X-Amz-Signature=651b8d1a096e8c29ada197ccbef6826f30503adb6c288bba6a06e9e396f5d3cb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSYRBOA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIEZCe6Rvo4r9AUm2AGscsIeumLnnsDkgufyyFneCLS66AiBXwxDStOzCwtXvBB4d3TOSd9PYLmmG6vqYF2WjI2fQeCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV%2Byb1FTd%2BiXIPHMYKtwDXQPpw52ShJqdM%2BweIeMV9F0H6wt45J%2FkZLmvWArD0x8dwXdsYZbYVlPAR9QDO%2FY%2BMBmOWwKDxqqXlwpiMvJyqvTpXi9b5XxpvDERyEh6LFdcUmjnMxUwLmPZDOgvDnR3grU1k%2BqMSJTibuWJVTAFJpxfnWIAv5sC5B2Y7YIasPPmhUVOhi5SdjmKuSe5zLXRYtiitguPpwQL1KmhXyJ6N20%2BYgpjJ29Tb6dBvhUF4UOrw38eJALyRjIXBTcErXnuKD98fl0cwyffVgUPhoz4DSYWDci8Joir8vYBaX4YFj47eAG3CygwJjLZnoDpUdQ%2BtjCqYYGRl96uM394WB7pORBmoG%2F1BITbrQc8XpDWtbO%2FXLb8Sx4rsr%2Bt9fzGFiDAApGza9RJpSkyE3p9fA6askays5oOEsBCGlI1%2F1j0ANeSbgkYGsmZBIP027rFauoScLe%2Fe92dGNxfi5cB7kInoYLVeVf6LGO7U6Xbn%2F%2F4T%2BaUPw2r8favuTSBRM3k4voO6PWFlqLh1Me2mSmheaYa9khRMRFuEkb0lomhTdinX%2FU9Y%2BTI27OIeSCFWIiR7NX2qAPbfRrFI3BBwIUnuKsMvXDvp4pDF1kTFLrfSvj4akkESQRdIMd8rLE6krIwp%2BjlvAY6pgEL1xsSuUQfHeKKczU3mS%2BOF2hyW5U%2BbWWo%2F9dUNXQWApjrbUdCN2csZWhgh0zzOa8AzK3WDDZSXi%2FIUEU0SUX14VAw9B1XAlvG483cKdEJIEVMqZyhno%2Fvqax4Phr1u8o7yOYNiPsUUTK4%2F8TBiOkjEyFng6JjVhmykqTzW47BRRcDBpb%2B6G4WZGiw%2B06tg%2BI0Fkt0054B7cW9vEGbBa%2BOAEvZ4K4A&X-Amz-Signature=e4330d54da41600a2ca0dff140f577ee43d3ceae2f2fb042268984a713775c64&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSYRBOA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIEZCe6Rvo4r9AUm2AGscsIeumLnnsDkgufyyFneCLS66AiBXwxDStOzCwtXvBB4d3TOSd9PYLmmG6vqYF2WjI2fQeCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV%2Byb1FTd%2BiXIPHMYKtwDXQPpw52ShJqdM%2BweIeMV9F0H6wt45J%2FkZLmvWArD0x8dwXdsYZbYVlPAR9QDO%2FY%2BMBmOWwKDxqqXlwpiMvJyqvTpXi9b5XxpvDERyEh6LFdcUmjnMxUwLmPZDOgvDnR3grU1k%2BqMSJTibuWJVTAFJpxfnWIAv5sC5B2Y7YIasPPmhUVOhi5SdjmKuSe5zLXRYtiitguPpwQL1KmhXyJ6N20%2BYgpjJ29Tb6dBvhUF4UOrw38eJALyRjIXBTcErXnuKD98fl0cwyffVgUPhoz4DSYWDci8Joir8vYBaX4YFj47eAG3CygwJjLZnoDpUdQ%2BtjCqYYGRl96uM394WB7pORBmoG%2F1BITbrQc8XpDWtbO%2FXLb8Sx4rsr%2Bt9fzGFiDAApGza9RJpSkyE3p9fA6askays5oOEsBCGlI1%2F1j0ANeSbgkYGsmZBIP027rFauoScLe%2Fe92dGNxfi5cB7kInoYLVeVf6LGO7U6Xbn%2F%2F4T%2BaUPw2r8favuTSBRM3k4voO6PWFlqLh1Me2mSmheaYa9khRMRFuEkb0lomhTdinX%2FU9Y%2BTI27OIeSCFWIiR7NX2qAPbfRrFI3BBwIUnuKsMvXDvp4pDF1kTFLrfSvj4akkESQRdIMd8rLE6krIwp%2BjlvAY6pgEL1xsSuUQfHeKKczU3mS%2BOF2hyW5U%2BbWWo%2F9dUNXQWApjrbUdCN2csZWhgh0zzOa8AzK3WDDZSXi%2FIUEU0SUX14VAw9B1XAlvG483cKdEJIEVMqZyhno%2Fvqax4Phr1u8o7yOYNiPsUUTK4%2F8TBiOkjEyFng6JjVhmykqTzW47BRRcDBpb%2B6G4WZGiw%2B06tg%2BI0Fkt0054B7cW9vEGbBa%2BOAEvZ4K4A&X-Amz-Signature=27eea5f6f019ba531638e74c900559de81ceb413b5dd7a04b096cbd9a7146d77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSYRBOA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIEZCe6Rvo4r9AUm2AGscsIeumLnnsDkgufyyFneCLS66AiBXwxDStOzCwtXvBB4d3TOSd9PYLmmG6vqYF2WjI2fQeCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV%2Byb1FTd%2BiXIPHMYKtwDXQPpw52ShJqdM%2BweIeMV9F0H6wt45J%2FkZLmvWArD0x8dwXdsYZbYVlPAR9QDO%2FY%2BMBmOWwKDxqqXlwpiMvJyqvTpXi9b5XxpvDERyEh6LFdcUmjnMxUwLmPZDOgvDnR3grU1k%2BqMSJTibuWJVTAFJpxfnWIAv5sC5B2Y7YIasPPmhUVOhi5SdjmKuSe5zLXRYtiitguPpwQL1KmhXyJ6N20%2BYgpjJ29Tb6dBvhUF4UOrw38eJALyRjIXBTcErXnuKD98fl0cwyffVgUPhoz4DSYWDci8Joir8vYBaX4YFj47eAG3CygwJjLZnoDpUdQ%2BtjCqYYGRl96uM394WB7pORBmoG%2F1BITbrQc8XpDWtbO%2FXLb8Sx4rsr%2Bt9fzGFiDAApGza9RJpSkyE3p9fA6askays5oOEsBCGlI1%2F1j0ANeSbgkYGsmZBIP027rFauoScLe%2Fe92dGNxfi5cB7kInoYLVeVf6LGO7U6Xbn%2F%2F4T%2BaUPw2r8favuTSBRM3k4voO6PWFlqLh1Me2mSmheaYa9khRMRFuEkb0lomhTdinX%2FU9Y%2BTI27OIeSCFWIiR7NX2qAPbfRrFI3BBwIUnuKsMvXDvp4pDF1kTFLrfSvj4akkESQRdIMd8rLE6krIwp%2BjlvAY6pgEL1xsSuUQfHeKKczU3mS%2BOF2hyW5U%2BbWWo%2F9dUNXQWApjrbUdCN2csZWhgh0zzOa8AzK3WDDZSXi%2FIUEU0SUX14VAw9B1XAlvG483cKdEJIEVMqZyhno%2Fvqax4Phr1u8o7yOYNiPsUUTK4%2F8TBiOkjEyFng6JjVhmykqTzW47BRRcDBpb%2B6G4WZGiw%2B06tg%2BI0Fkt0054B7cW9vEGbBa%2BOAEvZ4K4A&X-Amz-Signature=1186ea851c3838b098a660dc313c4010cdca9403fbd683953306ede593d218bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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


