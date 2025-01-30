

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ7RKMSB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3iKOqmYckwG2dlQkGmh8pD5YswxRGLHXUClOhyTnRRAiBNubJyFGT3pHV6VoREiFLjrCQ8b3gN5O97HiS88W%2FMDSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7p7HfOFDK8MMbBktKtwDVIHq8xj%2F2qCV73xhg0sfqy0TGmhje5NoQ6ZfZ7oknOFlpW%2BJamgEjLYFV4Y6fdXIuihNZbgaZjkvu43T3ijJdVzx2nVEfOYk4GxDjOjd2oWIqLLxEdXDpMlKhmlKn7240Ji9ocfxZF9pSMHugjU11yAhGhxgj5eqtTxu8YZ9zspkpQUG5IZ6ZHMSkLhS%2Fpluf38kOkz4YpVZ3mvmukNY4LQWkhXOHg7%2F0Y1GrnGbiYrnVhPMAjB%2Fn%2BXwUbWJLxS2zwyD6KC7PI7LoVn%2BNyVh2L0cvEUKwDc2awk031XQn0pNHndku%2BpZTQX%2BEPybqtS4jaTjrK8aGLwU8mmeIUlAvYNV%2F4AirvvbimZzpkKObghAjBoD1dFKqCkkQIt5j%2FwBG2EXxOMuYpJ9omCUyBw4MJlVmrN8Ho5wA5kgnVQTPtRKZgg7N5aYlGO4wguStD%2F%2F%2FCu%2BQWS8XFE1WCGuE1X8nwWi2QrM0gcDmePSXyyXzuIc2FAgj5qznv%2FT2y85c4j5dj2DAoHGm3e89ohZutZyarVp5RVbqhGHfYWkQSE8YilcXyJhdrYpCsN%2BAKrVlpQb1MMw8LS%2BcmtDPl63%2FPrFNPIZrSSSUC6x7nofbA4UgpAAXrBqMmGtcs%2BRflkwyPrtvAY6pgEw5vPn4ayZ1irj8aelLpNxdHJMFhfOBTO9JQZc1GSeyPDkeWV0K4h%2BwCeuLcxr0LOwXQpv1VaczN4ORLVHqqPa4kX5qkuKqRPtsCA3j25418iDtLostZWUoVUpRd3Y5VpJoVu4SnPAaUECh6iASoShDKeYxWLyi87ho3Eu4t0GUGWlmrS2NWMBmSHV%2FNWhT1Zco7949nY7cMeMRa1J%2FjIFJkhYfDCz&X-Amz-Signature=56c5453708f88e47d5ada8698ee7dff989d0a200f036c4f70a7ae82c4aac8a27&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5BLDPD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyoqF0c7pyXY%2FNY0hmrwt6rXOgW0OqSvV42uX04eUnqAIgDB0RNwDx8NlvkxA%2FWgpJnAhDid0tbNCyKLNFsjd9mzIqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsa6bon3bYvAfsFlSrcA5rMHDiuoenW%2BTeG1tUeSZQj5%2Ba%2B8ZjwsSVLYQiG8Jmu%2BgnN9RaZAIyM1QMqbyRMu3PKIe6Fa%2BwZjvofshPvEiGT3zcbGWdgy2VXtseoMFYfwlK7tA4LgiCo0Z1S%2B86PzRW6MJ6n9mSzxbTX4LQQQ3UxX6QppBQbxh7bU229nUD4xydz%2BKY5VWw48s2GUiXGJcoU60BzCP9MLd9tdTd5QAlRJLonKZ4prLElWRxNNJ%2B2QCWibZcwrevY%2F2GIAH5S6P6650Z1OcFypJd0q9PSRPyXjTn1YuBClBsr0CX%2BM%2FZxiiwF%2FCo3Bmn%2FrKBbSmnbxdSNdEHfznjz4cg%2F625Xs9Ee84uCRW9f9CrEFXcDrZwfySy5xNHstvb8Y50C4poDMKqLxx6NZV%2BS47gf5H2GOiU5iraohTNu%2BQnbd17Q7QtRTeakTWMN9ki5keVN6A19K4wb0c%2Frr%2BYonJSJrqV7QZlZnUhgnEdzN1vQwqlWYlBsXYVQ1T78OKZcz7ec3xUkXA3S8zG7S7BL5DGcDHxLpXcxWlmtUOQKrOlEuiykAVPmImDmBh4fGEJ2BcRYS%2FzcQ1kazYS7%2B%2F20lxiaFSfXX%2BXgAfhS3Ukc%2Bexi3rEzT794Hhn6kNeyq76YVYDsMMP67bwGOqUBon5x5ww4sdt6%2FsdqtQHaV4Lj8%2BIW%2BjAhTDUh%2FT5Ptw8kdcsPwzj5YpmbGZEhiSaT5prbcajFfJ3WRBAGPhP6gPQRkSVEVXOIX875F%2BsAu%2BlV7ETXn6IHEVAURCKYvlO%2FWN9m%2B%2B6lCfkTYzqRtSNjfl51%2FJz4uU6SBMlk7M2HOEzjFlUcr5fJudv4lKPpCS5z5rXzOM96gYI5ZFTrm93KH6s0xxe0&X-Amz-Signature=5fea0eb131bd27471469fbde4f38a39eb28aa97f42a57b5d81e38eb613a798fb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5BLDPD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyoqF0c7pyXY%2FNY0hmrwt6rXOgW0OqSvV42uX04eUnqAIgDB0RNwDx8NlvkxA%2FWgpJnAhDid0tbNCyKLNFsjd9mzIqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsa6bon3bYvAfsFlSrcA5rMHDiuoenW%2BTeG1tUeSZQj5%2Ba%2B8ZjwsSVLYQiG8Jmu%2BgnN9RaZAIyM1QMqbyRMu3PKIe6Fa%2BwZjvofshPvEiGT3zcbGWdgy2VXtseoMFYfwlK7tA4LgiCo0Z1S%2B86PzRW6MJ6n9mSzxbTX4LQQQ3UxX6QppBQbxh7bU229nUD4xydz%2BKY5VWw48s2GUiXGJcoU60BzCP9MLd9tdTd5QAlRJLonKZ4prLElWRxNNJ%2B2QCWibZcwrevY%2F2GIAH5S6P6650Z1OcFypJd0q9PSRPyXjTn1YuBClBsr0CX%2BM%2FZxiiwF%2FCo3Bmn%2FrKBbSmnbxdSNdEHfznjz4cg%2F625Xs9Ee84uCRW9f9CrEFXcDrZwfySy5xNHstvb8Y50C4poDMKqLxx6NZV%2BS47gf5H2GOiU5iraohTNu%2BQnbd17Q7QtRTeakTWMN9ki5keVN6A19K4wb0c%2Frr%2BYonJSJrqV7QZlZnUhgnEdzN1vQwqlWYlBsXYVQ1T78OKZcz7ec3xUkXA3S8zG7S7BL5DGcDHxLpXcxWlmtUOQKrOlEuiykAVPmImDmBh4fGEJ2BcRYS%2FzcQ1kazYS7%2B%2F20lxiaFSfXX%2BXgAfhS3Ukc%2Bexi3rEzT794Hhn6kNeyq76YVYDsMMP67bwGOqUBon5x5ww4sdt6%2FsdqtQHaV4Lj8%2BIW%2BjAhTDUh%2FT5Ptw8kdcsPwzj5YpmbGZEhiSaT5prbcajFfJ3WRBAGPhP6gPQRkSVEVXOIX875F%2BsAu%2BlV7ETXn6IHEVAURCKYvlO%2FWN9m%2B%2B6lCfkTYzqRtSNjfl51%2FJz4uU6SBMlk7M2HOEzjFlUcr5fJudv4lKPpCS5z5rXzOM96gYI5ZFTrm93KH6s0xxe0&X-Amz-Signature=49aae52afe4155748396d8da55f62c2c1f5996bf262900e68ef2fd9b3de9bee4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5BLDPD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyoqF0c7pyXY%2FNY0hmrwt6rXOgW0OqSvV42uX04eUnqAIgDB0RNwDx8NlvkxA%2FWgpJnAhDid0tbNCyKLNFsjd9mzIqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsa6bon3bYvAfsFlSrcA5rMHDiuoenW%2BTeG1tUeSZQj5%2Ba%2B8ZjwsSVLYQiG8Jmu%2BgnN9RaZAIyM1QMqbyRMu3PKIe6Fa%2BwZjvofshPvEiGT3zcbGWdgy2VXtseoMFYfwlK7tA4LgiCo0Z1S%2B86PzRW6MJ6n9mSzxbTX4LQQQ3UxX6QppBQbxh7bU229nUD4xydz%2BKY5VWw48s2GUiXGJcoU60BzCP9MLd9tdTd5QAlRJLonKZ4prLElWRxNNJ%2B2QCWibZcwrevY%2F2GIAH5S6P6650Z1OcFypJd0q9PSRPyXjTn1YuBClBsr0CX%2BM%2FZxiiwF%2FCo3Bmn%2FrKBbSmnbxdSNdEHfznjz4cg%2F625Xs9Ee84uCRW9f9CrEFXcDrZwfySy5xNHstvb8Y50C4poDMKqLxx6NZV%2BS47gf5H2GOiU5iraohTNu%2BQnbd17Q7QtRTeakTWMN9ki5keVN6A19K4wb0c%2Frr%2BYonJSJrqV7QZlZnUhgnEdzN1vQwqlWYlBsXYVQ1T78OKZcz7ec3xUkXA3S8zG7S7BL5DGcDHxLpXcxWlmtUOQKrOlEuiykAVPmImDmBh4fGEJ2BcRYS%2FzcQ1kazYS7%2B%2F20lxiaFSfXX%2BXgAfhS3Ukc%2Bexi3rEzT794Hhn6kNeyq76YVYDsMMP67bwGOqUBon5x5ww4sdt6%2FsdqtQHaV4Lj8%2BIW%2BjAhTDUh%2FT5Ptw8kdcsPwzj5YpmbGZEhiSaT5prbcajFfJ3WRBAGPhP6gPQRkSVEVXOIX875F%2BsAu%2BlV7ETXn6IHEVAURCKYvlO%2FWN9m%2B%2B6lCfkTYzqRtSNjfl51%2FJz4uU6SBMlk7M2HOEzjFlUcr5fJudv4lKPpCS5z5rXzOM96gYI5ZFTrm93KH6s0xxe0&X-Amz-Signature=3190f4a4048bdcf0818522b362fda2678988d02284c0b76a34e60bbef7b02a90&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5BLDPD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyoqF0c7pyXY%2FNY0hmrwt6rXOgW0OqSvV42uX04eUnqAIgDB0RNwDx8NlvkxA%2FWgpJnAhDid0tbNCyKLNFsjd9mzIqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsa6bon3bYvAfsFlSrcA5rMHDiuoenW%2BTeG1tUeSZQj5%2Ba%2B8ZjwsSVLYQiG8Jmu%2BgnN9RaZAIyM1QMqbyRMu3PKIe6Fa%2BwZjvofshPvEiGT3zcbGWdgy2VXtseoMFYfwlK7tA4LgiCo0Z1S%2B86PzRW6MJ6n9mSzxbTX4LQQQ3UxX6QppBQbxh7bU229nUD4xydz%2BKY5VWw48s2GUiXGJcoU60BzCP9MLd9tdTd5QAlRJLonKZ4prLElWRxNNJ%2B2QCWibZcwrevY%2F2GIAH5S6P6650Z1OcFypJd0q9PSRPyXjTn1YuBClBsr0CX%2BM%2FZxiiwF%2FCo3Bmn%2FrKBbSmnbxdSNdEHfznjz4cg%2F625Xs9Ee84uCRW9f9CrEFXcDrZwfySy5xNHstvb8Y50C4poDMKqLxx6NZV%2BS47gf5H2GOiU5iraohTNu%2BQnbd17Q7QtRTeakTWMN9ki5keVN6A19K4wb0c%2Frr%2BYonJSJrqV7QZlZnUhgnEdzN1vQwqlWYlBsXYVQ1T78OKZcz7ec3xUkXA3S8zG7S7BL5DGcDHxLpXcxWlmtUOQKrOlEuiykAVPmImDmBh4fGEJ2BcRYS%2FzcQ1kazYS7%2B%2F20lxiaFSfXX%2BXgAfhS3Ukc%2Bexi3rEzT794Hhn6kNeyq76YVYDsMMP67bwGOqUBon5x5ww4sdt6%2FsdqtQHaV4Lj8%2BIW%2BjAhTDUh%2FT5Ptw8kdcsPwzj5YpmbGZEhiSaT5prbcajFfJ3WRBAGPhP6gPQRkSVEVXOIX875F%2BsAu%2BlV7ETXn6IHEVAURCKYvlO%2FWN9m%2B%2B6lCfkTYzqRtSNjfl51%2FJz4uU6SBMlk7M2HOEzjFlUcr5fJudv4lKPpCS5z5rXzOM96gYI5ZFTrm93KH6s0xxe0&X-Amz-Signature=5d57663b7b09c5da55c4f3962c4b8e8d420e872445101c1893880df9c12a2e49&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5BLDPD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyoqF0c7pyXY%2FNY0hmrwt6rXOgW0OqSvV42uX04eUnqAIgDB0RNwDx8NlvkxA%2FWgpJnAhDid0tbNCyKLNFsjd9mzIqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsa6bon3bYvAfsFlSrcA5rMHDiuoenW%2BTeG1tUeSZQj5%2Ba%2B8ZjwsSVLYQiG8Jmu%2BgnN9RaZAIyM1QMqbyRMu3PKIe6Fa%2BwZjvofshPvEiGT3zcbGWdgy2VXtseoMFYfwlK7tA4LgiCo0Z1S%2B86PzRW6MJ6n9mSzxbTX4LQQQ3UxX6QppBQbxh7bU229nUD4xydz%2BKY5VWw48s2GUiXGJcoU60BzCP9MLd9tdTd5QAlRJLonKZ4prLElWRxNNJ%2B2QCWibZcwrevY%2F2GIAH5S6P6650Z1OcFypJd0q9PSRPyXjTn1YuBClBsr0CX%2BM%2FZxiiwF%2FCo3Bmn%2FrKBbSmnbxdSNdEHfznjz4cg%2F625Xs9Ee84uCRW9f9CrEFXcDrZwfySy5xNHstvb8Y50C4poDMKqLxx6NZV%2BS47gf5H2GOiU5iraohTNu%2BQnbd17Q7QtRTeakTWMN9ki5keVN6A19K4wb0c%2Frr%2BYonJSJrqV7QZlZnUhgnEdzN1vQwqlWYlBsXYVQ1T78OKZcz7ec3xUkXA3S8zG7S7BL5DGcDHxLpXcxWlmtUOQKrOlEuiykAVPmImDmBh4fGEJ2BcRYS%2FzcQ1kazYS7%2B%2F20lxiaFSfXX%2BXgAfhS3Ukc%2Bexi3rEzT794Hhn6kNeyq76YVYDsMMP67bwGOqUBon5x5ww4sdt6%2FsdqtQHaV4Lj8%2BIW%2BjAhTDUh%2FT5Ptw8kdcsPwzj5YpmbGZEhiSaT5prbcajFfJ3WRBAGPhP6gPQRkSVEVXOIX875F%2BsAu%2BlV7ETXn6IHEVAURCKYvlO%2FWN9m%2B%2B6lCfkTYzqRtSNjfl51%2FJz4uU6SBMlk7M2HOEzjFlUcr5fJudv4lKPpCS5z5rXzOM96gYI5ZFTrm93KH6s0xxe0&X-Amz-Signature=ddca8df293f13218153c9f8ebb2f840016954578fd26aef1598ca0ae4e28c966&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ7RKMSB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3iKOqmYckwG2dlQkGmh8pD5YswxRGLHXUClOhyTnRRAiBNubJyFGT3pHV6VoREiFLjrCQ8b3gN5O97HiS88W%2FMDSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7p7HfOFDK8MMbBktKtwDVIHq8xj%2F2qCV73xhg0sfqy0TGmhje5NoQ6ZfZ7oknOFlpW%2BJamgEjLYFV4Y6fdXIuihNZbgaZjkvu43T3ijJdVzx2nVEfOYk4GxDjOjd2oWIqLLxEdXDpMlKhmlKn7240Ji9ocfxZF9pSMHugjU11yAhGhxgj5eqtTxu8YZ9zspkpQUG5IZ6ZHMSkLhS%2Fpluf38kOkz4YpVZ3mvmukNY4LQWkhXOHg7%2F0Y1GrnGbiYrnVhPMAjB%2Fn%2BXwUbWJLxS2zwyD6KC7PI7LoVn%2BNyVh2L0cvEUKwDc2awk031XQn0pNHndku%2BpZTQX%2BEPybqtS4jaTjrK8aGLwU8mmeIUlAvYNV%2F4AirvvbimZzpkKObghAjBoD1dFKqCkkQIt5j%2FwBG2EXxOMuYpJ9omCUyBw4MJlVmrN8Ho5wA5kgnVQTPtRKZgg7N5aYlGO4wguStD%2F%2F%2FCu%2BQWS8XFE1WCGuE1X8nwWi2QrM0gcDmePSXyyXzuIc2FAgj5qznv%2FT2y85c4j5dj2DAoHGm3e89ohZutZyarVp5RVbqhGHfYWkQSE8YilcXyJhdrYpCsN%2BAKrVlpQb1MMw8LS%2BcmtDPl63%2FPrFNPIZrSSSUC6x7nofbA4UgpAAXrBqMmGtcs%2BRflkwyPrtvAY6pgEw5vPn4ayZ1irj8aelLpNxdHJMFhfOBTO9JQZc1GSeyPDkeWV0K4h%2BwCeuLcxr0LOwXQpv1VaczN4ORLVHqqPa4kX5qkuKqRPtsCA3j25418iDtLostZWUoVUpRd3Y5VpJoVu4SnPAaUECh6iASoShDKeYxWLyi87ho3Eu4t0GUGWlmrS2NWMBmSHV%2FNWhT1Zco7949nY7cMeMRa1J%2FjIFJkhYfDCz&X-Amz-Signature=8919813a10edbd819b8e24af704eb8fc3e2e8c705b6b6e3158890bb776eb8a9f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ7RKMSB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3iKOqmYckwG2dlQkGmh8pD5YswxRGLHXUClOhyTnRRAiBNubJyFGT3pHV6VoREiFLjrCQ8b3gN5O97HiS88W%2FMDSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7p7HfOFDK8MMbBktKtwDVIHq8xj%2F2qCV73xhg0sfqy0TGmhje5NoQ6ZfZ7oknOFlpW%2BJamgEjLYFV4Y6fdXIuihNZbgaZjkvu43T3ijJdVzx2nVEfOYk4GxDjOjd2oWIqLLxEdXDpMlKhmlKn7240Ji9ocfxZF9pSMHugjU11yAhGhxgj5eqtTxu8YZ9zspkpQUG5IZ6ZHMSkLhS%2Fpluf38kOkz4YpVZ3mvmukNY4LQWkhXOHg7%2F0Y1GrnGbiYrnVhPMAjB%2Fn%2BXwUbWJLxS2zwyD6KC7PI7LoVn%2BNyVh2L0cvEUKwDc2awk031XQn0pNHndku%2BpZTQX%2BEPybqtS4jaTjrK8aGLwU8mmeIUlAvYNV%2F4AirvvbimZzpkKObghAjBoD1dFKqCkkQIt5j%2FwBG2EXxOMuYpJ9omCUyBw4MJlVmrN8Ho5wA5kgnVQTPtRKZgg7N5aYlGO4wguStD%2F%2F%2FCu%2BQWS8XFE1WCGuE1X8nwWi2QrM0gcDmePSXyyXzuIc2FAgj5qznv%2FT2y85c4j5dj2DAoHGm3e89ohZutZyarVp5RVbqhGHfYWkQSE8YilcXyJhdrYpCsN%2BAKrVlpQb1MMw8LS%2BcmtDPl63%2FPrFNPIZrSSSUC6x7nofbA4UgpAAXrBqMmGtcs%2BRflkwyPrtvAY6pgEw5vPn4ayZ1irj8aelLpNxdHJMFhfOBTO9JQZc1GSeyPDkeWV0K4h%2BwCeuLcxr0LOwXQpv1VaczN4ORLVHqqPa4kX5qkuKqRPtsCA3j25418iDtLostZWUoVUpRd3Y5VpJoVu4SnPAaUECh6iASoShDKeYxWLyi87ho3Eu4t0GUGWlmrS2NWMBmSHV%2FNWhT1Zco7949nY7cMeMRa1J%2FjIFJkhYfDCz&X-Amz-Signature=6b1a497a79deaf6ddc53a130b4b9474adbf0bfc2cbd5d3fe22ac163734ea8362&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ7RKMSB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3iKOqmYckwG2dlQkGmh8pD5YswxRGLHXUClOhyTnRRAiBNubJyFGT3pHV6VoREiFLjrCQ8b3gN5O97HiS88W%2FMDSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7p7HfOFDK8MMbBktKtwDVIHq8xj%2F2qCV73xhg0sfqy0TGmhje5NoQ6ZfZ7oknOFlpW%2BJamgEjLYFV4Y6fdXIuihNZbgaZjkvu43T3ijJdVzx2nVEfOYk4GxDjOjd2oWIqLLxEdXDpMlKhmlKn7240Ji9ocfxZF9pSMHugjU11yAhGhxgj5eqtTxu8YZ9zspkpQUG5IZ6ZHMSkLhS%2Fpluf38kOkz4YpVZ3mvmukNY4LQWkhXOHg7%2F0Y1GrnGbiYrnVhPMAjB%2Fn%2BXwUbWJLxS2zwyD6KC7PI7LoVn%2BNyVh2L0cvEUKwDc2awk031XQn0pNHndku%2BpZTQX%2BEPybqtS4jaTjrK8aGLwU8mmeIUlAvYNV%2F4AirvvbimZzpkKObghAjBoD1dFKqCkkQIt5j%2FwBG2EXxOMuYpJ9omCUyBw4MJlVmrN8Ho5wA5kgnVQTPtRKZgg7N5aYlGO4wguStD%2F%2F%2FCu%2BQWS8XFE1WCGuE1X8nwWi2QrM0gcDmePSXyyXzuIc2FAgj5qznv%2FT2y85c4j5dj2DAoHGm3e89ohZutZyarVp5RVbqhGHfYWkQSE8YilcXyJhdrYpCsN%2BAKrVlpQb1MMw8LS%2BcmtDPl63%2FPrFNPIZrSSSUC6x7nofbA4UgpAAXrBqMmGtcs%2BRflkwyPrtvAY6pgEw5vPn4ayZ1irj8aelLpNxdHJMFhfOBTO9JQZc1GSeyPDkeWV0K4h%2BwCeuLcxr0LOwXQpv1VaczN4ORLVHqqPa4kX5qkuKqRPtsCA3j25418iDtLostZWUoVUpRd3Y5VpJoVu4SnPAaUECh6iASoShDKeYxWLyi87ho3Eu4t0GUGWlmrS2NWMBmSHV%2FNWhT1Zco7949nY7cMeMRa1J%2FjIFJkhYfDCz&X-Amz-Signature=95f1f5cfec9332dba4febbdc87d9fc77b019f08381dd6e8b9f9acce7c6ebe58e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ7RKMSB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3iKOqmYckwG2dlQkGmh8pD5YswxRGLHXUClOhyTnRRAiBNubJyFGT3pHV6VoREiFLjrCQ8b3gN5O97HiS88W%2FMDSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7p7HfOFDK8MMbBktKtwDVIHq8xj%2F2qCV73xhg0sfqy0TGmhje5NoQ6ZfZ7oknOFlpW%2BJamgEjLYFV4Y6fdXIuihNZbgaZjkvu43T3ijJdVzx2nVEfOYk4GxDjOjd2oWIqLLxEdXDpMlKhmlKn7240Ji9ocfxZF9pSMHugjU11yAhGhxgj5eqtTxu8YZ9zspkpQUG5IZ6ZHMSkLhS%2Fpluf38kOkz4YpVZ3mvmukNY4LQWkhXOHg7%2F0Y1GrnGbiYrnVhPMAjB%2Fn%2BXwUbWJLxS2zwyD6KC7PI7LoVn%2BNyVh2L0cvEUKwDc2awk031XQn0pNHndku%2BpZTQX%2BEPybqtS4jaTjrK8aGLwU8mmeIUlAvYNV%2F4AirvvbimZzpkKObghAjBoD1dFKqCkkQIt5j%2FwBG2EXxOMuYpJ9omCUyBw4MJlVmrN8Ho5wA5kgnVQTPtRKZgg7N5aYlGO4wguStD%2F%2F%2FCu%2BQWS8XFE1WCGuE1X8nwWi2QrM0gcDmePSXyyXzuIc2FAgj5qznv%2FT2y85c4j5dj2DAoHGm3e89ohZutZyarVp5RVbqhGHfYWkQSE8YilcXyJhdrYpCsN%2BAKrVlpQb1MMw8LS%2BcmtDPl63%2FPrFNPIZrSSSUC6x7nofbA4UgpAAXrBqMmGtcs%2BRflkwyPrtvAY6pgEw5vPn4ayZ1irj8aelLpNxdHJMFhfOBTO9JQZc1GSeyPDkeWV0K4h%2BwCeuLcxr0LOwXQpv1VaczN4ORLVHqqPa4kX5qkuKqRPtsCA3j25418iDtLostZWUoVUpRd3Y5VpJoVu4SnPAaUECh6iASoShDKeYxWLyi87ho3Eu4t0GUGWlmrS2NWMBmSHV%2FNWhT1Zco7949nY7cMeMRa1J%2FjIFJkhYfDCz&X-Amz-Signature=6f3a806f9b61aa493f2ff2c037b6e5c9b2a58a106a6dff61d86cbe8f49dca41a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ7RKMSB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3iKOqmYckwG2dlQkGmh8pD5YswxRGLHXUClOhyTnRRAiBNubJyFGT3pHV6VoREiFLjrCQ8b3gN5O97HiS88W%2FMDSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7p7HfOFDK8MMbBktKtwDVIHq8xj%2F2qCV73xhg0sfqy0TGmhje5NoQ6ZfZ7oknOFlpW%2BJamgEjLYFV4Y6fdXIuihNZbgaZjkvu43T3ijJdVzx2nVEfOYk4GxDjOjd2oWIqLLxEdXDpMlKhmlKn7240Ji9ocfxZF9pSMHugjU11yAhGhxgj5eqtTxu8YZ9zspkpQUG5IZ6ZHMSkLhS%2Fpluf38kOkz4YpVZ3mvmukNY4LQWkhXOHg7%2F0Y1GrnGbiYrnVhPMAjB%2Fn%2BXwUbWJLxS2zwyD6KC7PI7LoVn%2BNyVh2L0cvEUKwDc2awk031XQn0pNHndku%2BpZTQX%2BEPybqtS4jaTjrK8aGLwU8mmeIUlAvYNV%2F4AirvvbimZzpkKObghAjBoD1dFKqCkkQIt5j%2FwBG2EXxOMuYpJ9omCUyBw4MJlVmrN8Ho5wA5kgnVQTPtRKZgg7N5aYlGO4wguStD%2F%2F%2FCu%2BQWS8XFE1WCGuE1X8nwWi2QrM0gcDmePSXyyXzuIc2FAgj5qznv%2FT2y85c4j5dj2DAoHGm3e89ohZutZyarVp5RVbqhGHfYWkQSE8YilcXyJhdrYpCsN%2BAKrVlpQb1MMw8LS%2BcmtDPl63%2FPrFNPIZrSSSUC6x7nofbA4UgpAAXrBqMmGtcs%2BRflkwyPrtvAY6pgEw5vPn4ayZ1irj8aelLpNxdHJMFhfOBTO9JQZc1GSeyPDkeWV0K4h%2BwCeuLcxr0LOwXQpv1VaczN4ORLVHqqPa4kX5qkuKqRPtsCA3j25418iDtLostZWUoVUpRd3Y5VpJoVu4SnPAaUECh6iASoShDKeYxWLyi87ho3Eu4t0GUGWlmrS2NWMBmSHV%2FNWhT1Zco7949nY7cMeMRa1J%2FjIFJkhYfDCz&X-Amz-Signature=5a4e1b99c713e55cab476b62e1921373c4e5e3c8f8bb544ccac394f5a42afe32&X-Amz-SignedHeaders=host&x-id=GetObject)
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


