

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTADDK4P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDeXtqYKOVG6QLtbQ490GaX2BSw%2Fa6MfVPju%2FD%2FGeos9AIgWzQpBIeH182hECZovdsxaSryeJkizoZR%2Be5ZhzuJZ7Aq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJ1r20UgIrS2g35qlircAzC6fTw2BC5IRrjCZPUtjBvv515dJ%2FOx0lWsxYyGh5%2F%2BH3XmGxXVfxbK31CyIA0P%2BCQ89wnG%2Bak5kxKjfNFsaPLeO6AI4Qz08wm9UwoX%2BhuJyFYiCDQHmbN4vuAhjMhKbo5SbGYHCOB%2B95tvExfjFW6swl6sBOZhkIaSZmH5wLh5pDeJAWzoAQ4IVFS%2Fv%2BIwlz06IhSYPd5KkkmUqCDZ%2FJH%2F4P63eTxAudD8aAr8xCOHXOV8%2B1Qr0ZiV%2Bpr2EhetHFyjdXliLgIAEK5vxejuYSuWTGcCjnQwioHwJuozQkklwZD2c4lhojs9O8Hk6Oa3bnUwFHJgvdK9Aj3nceHdGRzL6AHLcHiz52qgoAZJFI1ZJoWmJ6139VTtD1fviCIiCd8DtXuhNNyhnVFX11QDfshY0sxdHOF4tqDWk9bENbPaWOd1TIkZpM%2BXQWqiumKTatS2MHYVaEa78ASZSjNNF09AuQle06UCCABsCckQjsgbS01D9G%2Bbw8Y64AsRfkmZ8G71aYOvAHvws%2BWoUI08Gaiv37qA1FSTuqtz7qeCx2bZut%2BT%2BqopkL7r0aFezKvkic%2F5RCO2DLaAzrgFN8sQXehSUUfu9ZsqR%2BvDIWXjGWg1Q8XPLwQAE5Utl2zCMISck70GOqUBb14lqd5kIsXHIlUGpmRX0PbUyha6shZ3XhToK1it1vBbzG83YbTwSE11MI4uHpN7KXpajqGM6Rikc%2FbZxbQMnNCPVx84hYuVp0Q11jSvP5aidZNlWxgQqPfOqLmX%2Bi4S3lhD4nWLVieYI8TFcmHOI%2FDOzn9gjrv8wLBFNk98TwwfJzzW268LxLL3RBKKCv8JlzkmdRDvA8qYiXT536DZfTmLq%2BTl&X-Amz-Signature=55dda3e3efae51c8d2b0c673c9f91a519641eacd61306de2e527b9f59051d72a&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO2GTPLN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIBjsO9S2h%2FveMA6vcwRcWEFoYd8NieAxDGQ7dasyUnnDAiEA%2BtRizGb897MDktzY7jVJs3OR4iN66VbdkggPrWESk00q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDG8gAnt8iWpEsmOBhyrcA8tp%2Br2x6mYu9C7TEqTn6Eo2hLnxaHA29hyGM3%2FfsNxkgJfUWMxTicbWyuwoLzsG2ArRz3TY1jiesIeudr%2BiNfSTnGF20E3qNiEWc%2FUwcqIFHwbffMYAMPh5YTcqUKUBR6aBJ0YVMWIj13yMxN12EgJdRgZmKyaH4bMSe6GB4IxcE%2BLDY0FtXZMr%2BvsHqea4SzLIuYQH2268SDn8OVkIdDIRSj8WqbnWy9IyvIk3Dgstm%2F9Q%2FYcB6bdOoYUhmLWWIi8c3pjn7g%2B%2F4i68mZWhZr31nV%2B6Ki9zWKii1W%2Fj%2FHODqluXn8VA9ji7r55owlhe88ogK%2FTk701oyQJixBFK3bzCRJfR4qSIslua50s4koSHWk7Z0cbECPq%2FpQdX5Gdzd9o3Kwr9dCEVB3mNyx7FvglzkROeIcY8qko5vlmDyL6q%2FS%2B%2FlQl3m%2FNqD4O7qEu3phoUOFiKFNgZfSSS2uWtRKSjn%2Bh%2Fg6qKXKevsqAmzXrxu5DzoVcfW2zdn6ZciguMQzM94elYN28OezHL6ZRrayBVRvsCcl6sO8A6QYCN8IBDDD5uhrjBQvwbmZbTfsVbsH5iCCrwDXIdTO8K77fclcfWQFYfNQXsUAulZNN5Ibp3Jw11qj5uLAldJbmFMPmbk70GOqUB3nD1iamR8gX8AtVyhVyo1E1adVWTO27snfLC1tnB9%2F7%2FXpmITN8ah7Eua7YWBoba4563K14380uVoiRBxDAK%2BhCMm9bZu44y7GFGUVJRIU42Dw2R8R34F%2B5k0M0NJzRQ1qnW8fnS0UFV8dtesu0co1wRl%2BxFOsXnMzrKitlAI7ht28IbV4l%2Be%2FymPW%2FM%2FQKSRGiuplr8Vho3UdfqWzc8z91MXpxK&X-Amz-Signature=df6debdcea09553346137f66b6aa4774c992179198e92d91d61d64993ac17e42&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO2GTPLN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIBjsO9S2h%2FveMA6vcwRcWEFoYd8NieAxDGQ7dasyUnnDAiEA%2BtRizGb897MDktzY7jVJs3OR4iN66VbdkggPrWESk00q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDG8gAnt8iWpEsmOBhyrcA8tp%2Br2x6mYu9C7TEqTn6Eo2hLnxaHA29hyGM3%2FfsNxkgJfUWMxTicbWyuwoLzsG2ArRz3TY1jiesIeudr%2BiNfSTnGF20E3qNiEWc%2FUwcqIFHwbffMYAMPh5YTcqUKUBR6aBJ0YVMWIj13yMxN12EgJdRgZmKyaH4bMSe6GB4IxcE%2BLDY0FtXZMr%2BvsHqea4SzLIuYQH2268SDn8OVkIdDIRSj8WqbnWy9IyvIk3Dgstm%2F9Q%2FYcB6bdOoYUhmLWWIi8c3pjn7g%2B%2F4i68mZWhZr31nV%2B6Ki9zWKii1W%2Fj%2FHODqluXn8VA9ji7r55owlhe88ogK%2FTk701oyQJixBFK3bzCRJfR4qSIslua50s4koSHWk7Z0cbECPq%2FpQdX5Gdzd9o3Kwr9dCEVB3mNyx7FvglzkROeIcY8qko5vlmDyL6q%2FS%2B%2FlQl3m%2FNqD4O7qEu3phoUOFiKFNgZfSSS2uWtRKSjn%2Bh%2Fg6qKXKevsqAmzXrxu5DzoVcfW2zdn6ZciguMQzM94elYN28OezHL6ZRrayBVRvsCcl6sO8A6QYCN8IBDDD5uhrjBQvwbmZbTfsVbsH5iCCrwDXIdTO8K77fclcfWQFYfNQXsUAulZNN5Ibp3Jw11qj5uLAldJbmFMPmbk70GOqUB3nD1iamR8gX8AtVyhVyo1E1adVWTO27snfLC1tnB9%2F7%2FXpmITN8ah7Eua7YWBoba4563K14380uVoiRBxDAK%2BhCMm9bZu44y7GFGUVJRIU42Dw2R8R34F%2B5k0M0NJzRQ1qnW8fnS0UFV8dtesu0co1wRl%2BxFOsXnMzrKitlAI7ht28IbV4l%2Be%2FymPW%2FM%2FQKSRGiuplr8Vho3UdfqWzc8z91MXpxK&X-Amz-Signature=b1204b07a2c2d97d46941881e07a81045fe9f2f25a6f78d35f8980105af41d9e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO2GTPLN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIBjsO9S2h%2FveMA6vcwRcWEFoYd8NieAxDGQ7dasyUnnDAiEA%2BtRizGb897MDktzY7jVJs3OR4iN66VbdkggPrWESk00q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDG8gAnt8iWpEsmOBhyrcA8tp%2Br2x6mYu9C7TEqTn6Eo2hLnxaHA29hyGM3%2FfsNxkgJfUWMxTicbWyuwoLzsG2ArRz3TY1jiesIeudr%2BiNfSTnGF20E3qNiEWc%2FUwcqIFHwbffMYAMPh5YTcqUKUBR6aBJ0YVMWIj13yMxN12EgJdRgZmKyaH4bMSe6GB4IxcE%2BLDY0FtXZMr%2BvsHqea4SzLIuYQH2268SDn8OVkIdDIRSj8WqbnWy9IyvIk3Dgstm%2F9Q%2FYcB6bdOoYUhmLWWIi8c3pjn7g%2B%2F4i68mZWhZr31nV%2B6Ki9zWKii1W%2Fj%2FHODqluXn8VA9ji7r55owlhe88ogK%2FTk701oyQJixBFK3bzCRJfR4qSIslua50s4koSHWk7Z0cbECPq%2FpQdX5Gdzd9o3Kwr9dCEVB3mNyx7FvglzkROeIcY8qko5vlmDyL6q%2FS%2B%2FlQl3m%2FNqD4O7qEu3phoUOFiKFNgZfSSS2uWtRKSjn%2Bh%2Fg6qKXKevsqAmzXrxu5DzoVcfW2zdn6ZciguMQzM94elYN28OezHL6ZRrayBVRvsCcl6sO8A6QYCN8IBDDD5uhrjBQvwbmZbTfsVbsH5iCCrwDXIdTO8K77fclcfWQFYfNQXsUAulZNN5Ibp3Jw11qj5uLAldJbmFMPmbk70GOqUB3nD1iamR8gX8AtVyhVyo1E1adVWTO27snfLC1tnB9%2F7%2FXpmITN8ah7Eua7YWBoba4563K14380uVoiRBxDAK%2BhCMm9bZu44y7GFGUVJRIU42Dw2R8R34F%2B5k0M0NJzRQ1qnW8fnS0UFV8dtesu0co1wRl%2BxFOsXnMzrKitlAI7ht28IbV4l%2Be%2FymPW%2FM%2FQKSRGiuplr8Vho3UdfqWzc8z91MXpxK&X-Amz-Signature=64ed293c7ae5b20f2f6e058616008ff26cc72821d0242a8db3e988b4ec6cd105&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO2GTPLN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIBjsO9S2h%2FveMA6vcwRcWEFoYd8NieAxDGQ7dasyUnnDAiEA%2BtRizGb897MDktzY7jVJs3OR4iN66VbdkggPrWESk00q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDG8gAnt8iWpEsmOBhyrcA8tp%2Br2x6mYu9C7TEqTn6Eo2hLnxaHA29hyGM3%2FfsNxkgJfUWMxTicbWyuwoLzsG2ArRz3TY1jiesIeudr%2BiNfSTnGF20E3qNiEWc%2FUwcqIFHwbffMYAMPh5YTcqUKUBR6aBJ0YVMWIj13yMxN12EgJdRgZmKyaH4bMSe6GB4IxcE%2BLDY0FtXZMr%2BvsHqea4SzLIuYQH2268SDn8OVkIdDIRSj8WqbnWy9IyvIk3Dgstm%2F9Q%2FYcB6bdOoYUhmLWWIi8c3pjn7g%2B%2F4i68mZWhZr31nV%2B6Ki9zWKii1W%2Fj%2FHODqluXn8VA9ji7r55owlhe88ogK%2FTk701oyQJixBFK3bzCRJfR4qSIslua50s4koSHWk7Z0cbECPq%2FpQdX5Gdzd9o3Kwr9dCEVB3mNyx7FvglzkROeIcY8qko5vlmDyL6q%2FS%2B%2FlQl3m%2FNqD4O7qEu3phoUOFiKFNgZfSSS2uWtRKSjn%2Bh%2Fg6qKXKevsqAmzXrxu5DzoVcfW2zdn6ZciguMQzM94elYN28OezHL6ZRrayBVRvsCcl6sO8A6QYCN8IBDDD5uhrjBQvwbmZbTfsVbsH5iCCrwDXIdTO8K77fclcfWQFYfNQXsUAulZNN5Ibp3Jw11qj5uLAldJbmFMPmbk70GOqUB3nD1iamR8gX8AtVyhVyo1E1adVWTO27snfLC1tnB9%2F7%2FXpmITN8ah7Eua7YWBoba4563K14380uVoiRBxDAK%2BhCMm9bZu44y7GFGUVJRIU42Dw2R8R34F%2B5k0M0NJzRQ1qnW8fnS0UFV8dtesu0co1wRl%2BxFOsXnMzrKitlAI7ht28IbV4l%2Be%2FymPW%2FM%2FQKSRGiuplr8Vho3UdfqWzc8z91MXpxK&X-Amz-Signature=dd625566fd587146035af0ab075aee8f2bfbc4864e49d019072809e506ea0a8c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO2GTPLN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIBjsO9S2h%2FveMA6vcwRcWEFoYd8NieAxDGQ7dasyUnnDAiEA%2BtRizGb897MDktzY7jVJs3OR4iN66VbdkggPrWESk00q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDG8gAnt8iWpEsmOBhyrcA8tp%2Br2x6mYu9C7TEqTn6Eo2hLnxaHA29hyGM3%2FfsNxkgJfUWMxTicbWyuwoLzsG2ArRz3TY1jiesIeudr%2BiNfSTnGF20E3qNiEWc%2FUwcqIFHwbffMYAMPh5YTcqUKUBR6aBJ0YVMWIj13yMxN12EgJdRgZmKyaH4bMSe6GB4IxcE%2BLDY0FtXZMr%2BvsHqea4SzLIuYQH2268SDn8OVkIdDIRSj8WqbnWy9IyvIk3Dgstm%2F9Q%2FYcB6bdOoYUhmLWWIi8c3pjn7g%2B%2F4i68mZWhZr31nV%2B6Ki9zWKii1W%2Fj%2FHODqluXn8VA9ji7r55owlhe88ogK%2FTk701oyQJixBFK3bzCRJfR4qSIslua50s4koSHWk7Z0cbECPq%2FpQdX5Gdzd9o3Kwr9dCEVB3mNyx7FvglzkROeIcY8qko5vlmDyL6q%2FS%2B%2FlQl3m%2FNqD4O7qEu3phoUOFiKFNgZfSSS2uWtRKSjn%2Bh%2Fg6qKXKevsqAmzXrxu5DzoVcfW2zdn6ZciguMQzM94elYN28OezHL6ZRrayBVRvsCcl6sO8A6QYCN8IBDDD5uhrjBQvwbmZbTfsVbsH5iCCrwDXIdTO8K77fclcfWQFYfNQXsUAulZNN5Ibp3Jw11qj5uLAldJbmFMPmbk70GOqUB3nD1iamR8gX8AtVyhVyo1E1adVWTO27snfLC1tnB9%2F7%2FXpmITN8ah7Eua7YWBoba4563K14380uVoiRBxDAK%2BhCMm9bZu44y7GFGUVJRIU42Dw2R8R34F%2B5k0M0NJzRQ1qnW8fnS0UFV8dtesu0co1wRl%2BxFOsXnMzrKitlAI7ht28IbV4l%2Be%2FymPW%2FM%2FQKSRGiuplr8Vho3UdfqWzc8z91MXpxK&X-Amz-Signature=2c8e1a892eebd8b0e3026ac0fd1fac8adc36032b567df73dc962e3d13f34cee8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTADDK4P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDeXtqYKOVG6QLtbQ490GaX2BSw%2Fa6MfVPju%2FD%2FGeos9AIgWzQpBIeH182hECZovdsxaSryeJkizoZR%2Be5ZhzuJZ7Aq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJ1r20UgIrS2g35qlircAzC6fTw2BC5IRrjCZPUtjBvv515dJ%2FOx0lWsxYyGh5%2F%2BH3XmGxXVfxbK31CyIA0P%2BCQ89wnG%2Bak5kxKjfNFsaPLeO6AI4Qz08wm9UwoX%2BhuJyFYiCDQHmbN4vuAhjMhKbo5SbGYHCOB%2B95tvExfjFW6swl6sBOZhkIaSZmH5wLh5pDeJAWzoAQ4IVFS%2Fv%2BIwlz06IhSYPd5KkkmUqCDZ%2FJH%2F4P63eTxAudD8aAr8xCOHXOV8%2B1Qr0ZiV%2Bpr2EhetHFyjdXliLgIAEK5vxejuYSuWTGcCjnQwioHwJuozQkklwZD2c4lhojs9O8Hk6Oa3bnUwFHJgvdK9Aj3nceHdGRzL6AHLcHiz52qgoAZJFI1ZJoWmJ6139VTtD1fviCIiCd8DtXuhNNyhnVFX11QDfshY0sxdHOF4tqDWk9bENbPaWOd1TIkZpM%2BXQWqiumKTatS2MHYVaEa78ASZSjNNF09AuQle06UCCABsCckQjsgbS01D9G%2Bbw8Y64AsRfkmZ8G71aYOvAHvws%2BWoUI08Gaiv37qA1FSTuqtz7qeCx2bZut%2BT%2BqopkL7r0aFezKvkic%2F5RCO2DLaAzrgFN8sQXehSUUfu9ZsqR%2BvDIWXjGWg1Q8XPLwQAE5Utl2zCMISck70GOqUBb14lqd5kIsXHIlUGpmRX0PbUyha6shZ3XhToK1it1vBbzG83YbTwSE11MI4uHpN7KXpajqGM6Rikc%2FbZxbQMnNCPVx84hYuVp0Q11jSvP5aidZNlWxgQqPfOqLmX%2Bi4S3lhD4nWLVieYI8TFcmHOI%2FDOzn9gjrv8wLBFNk98TwwfJzzW268LxLL3RBKKCv8JlzkmdRDvA8qYiXT536DZfTmLq%2BTl&X-Amz-Signature=657c44cd74d9c8435e294a00871c42f32a25d48e594a389842930c158024055c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTADDK4P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDeXtqYKOVG6QLtbQ490GaX2BSw%2Fa6MfVPju%2FD%2FGeos9AIgWzQpBIeH182hECZovdsxaSryeJkizoZR%2Be5ZhzuJZ7Aq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJ1r20UgIrS2g35qlircAzC6fTw2BC5IRrjCZPUtjBvv515dJ%2FOx0lWsxYyGh5%2F%2BH3XmGxXVfxbK31CyIA0P%2BCQ89wnG%2Bak5kxKjfNFsaPLeO6AI4Qz08wm9UwoX%2BhuJyFYiCDQHmbN4vuAhjMhKbo5SbGYHCOB%2B95tvExfjFW6swl6sBOZhkIaSZmH5wLh5pDeJAWzoAQ4IVFS%2Fv%2BIwlz06IhSYPd5KkkmUqCDZ%2FJH%2F4P63eTxAudD8aAr8xCOHXOV8%2B1Qr0ZiV%2Bpr2EhetHFyjdXliLgIAEK5vxejuYSuWTGcCjnQwioHwJuozQkklwZD2c4lhojs9O8Hk6Oa3bnUwFHJgvdK9Aj3nceHdGRzL6AHLcHiz52qgoAZJFI1ZJoWmJ6139VTtD1fviCIiCd8DtXuhNNyhnVFX11QDfshY0sxdHOF4tqDWk9bENbPaWOd1TIkZpM%2BXQWqiumKTatS2MHYVaEa78ASZSjNNF09AuQle06UCCABsCckQjsgbS01D9G%2Bbw8Y64AsRfkmZ8G71aYOvAHvws%2BWoUI08Gaiv37qA1FSTuqtz7qeCx2bZut%2BT%2BqopkL7r0aFezKvkic%2F5RCO2DLaAzrgFN8sQXehSUUfu9ZsqR%2BvDIWXjGWg1Q8XPLwQAE5Utl2zCMISck70GOqUBb14lqd5kIsXHIlUGpmRX0PbUyha6shZ3XhToK1it1vBbzG83YbTwSE11MI4uHpN7KXpajqGM6Rikc%2FbZxbQMnNCPVx84hYuVp0Q11jSvP5aidZNlWxgQqPfOqLmX%2Bi4S3lhD4nWLVieYI8TFcmHOI%2FDOzn9gjrv8wLBFNk98TwwfJzzW268LxLL3RBKKCv8JlzkmdRDvA8qYiXT536DZfTmLq%2BTl&X-Amz-Signature=384aba510af2e60fb59bbeb51e50ea3ae98146fd4bb216010fcdef77c00bb02c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTADDK4P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDeXtqYKOVG6QLtbQ490GaX2BSw%2Fa6MfVPju%2FD%2FGeos9AIgWzQpBIeH182hECZovdsxaSryeJkizoZR%2Be5ZhzuJZ7Aq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJ1r20UgIrS2g35qlircAzC6fTw2BC5IRrjCZPUtjBvv515dJ%2FOx0lWsxYyGh5%2F%2BH3XmGxXVfxbK31CyIA0P%2BCQ89wnG%2Bak5kxKjfNFsaPLeO6AI4Qz08wm9UwoX%2BhuJyFYiCDQHmbN4vuAhjMhKbo5SbGYHCOB%2B95tvExfjFW6swl6sBOZhkIaSZmH5wLh5pDeJAWzoAQ4IVFS%2Fv%2BIwlz06IhSYPd5KkkmUqCDZ%2FJH%2F4P63eTxAudD8aAr8xCOHXOV8%2B1Qr0ZiV%2Bpr2EhetHFyjdXliLgIAEK5vxejuYSuWTGcCjnQwioHwJuozQkklwZD2c4lhojs9O8Hk6Oa3bnUwFHJgvdK9Aj3nceHdGRzL6AHLcHiz52qgoAZJFI1ZJoWmJ6139VTtD1fviCIiCd8DtXuhNNyhnVFX11QDfshY0sxdHOF4tqDWk9bENbPaWOd1TIkZpM%2BXQWqiumKTatS2MHYVaEa78ASZSjNNF09AuQle06UCCABsCckQjsgbS01D9G%2Bbw8Y64AsRfkmZ8G71aYOvAHvws%2BWoUI08Gaiv37qA1FSTuqtz7qeCx2bZut%2BT%2BqopkL7r0aFezKvkic%2F5RCO2DLaAzrgFN8sQXehSUUfu9ZsqR%2BvDIWXjGWg1Q8XPLwQAE5Utl2zCMISck70GOqUBb14lqd5kIsXHIlUGpmRX0PbUyha6shZ3XhToK1it1vBbzG83YbTwSE11MI4uHpN7KXpajqGM6Rikc%2FbZxbQMnNCPVx84hYuVp0Q11jSvP5aidZNlWxgQqPfOqLmX%2Bi4S3lhD4nWLVieYI8TFcmHOI%2FDOzn9gjrv8wLBFNk98TwwfJzzW268LxLL3RBKKCv8JlzkmdRDvA8qYiXT536DZfTmLq%2BTl&X-Amz-Signature=53b4521ccfecced3ef649ae6126db53c1ad6475302163805f1d0035d1f592347&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTADDK4P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDeXtqYKOVG6QLtbQ490GaX2BSw%2Fa6MfVPju%2FD%2FGeos9AIgWzQpBIeH182hECZovdsxaSryeJkizoZR%2Be5ZhzuJZ7Aq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJ1r20UgIrS2g35qlircAzC6fTw2BC5IRrjCZPUtjBvv515dJ%2FOx0lWsxYyGh5%2F%2BH3XmGxXVfxbK31CyIA0P%2BCQ89wnG%2Bak5kxKjfNFsaPLeO6AI4Qz08wm9UwoX%2BhuJyFYiCDQHmbN4vuAhjMhKbo5SbGYHCOB%2B95tvExfjFW6swl6sBOZhkIaSZmH5wLh5pDeJAWzoAQ4IVFS%2Fv%2BIwlz06IhSYPd5KkkmUqCDZ%2FJH%2F4P63eTxAudD8aAr8xCOHXOV8%2B1Qr0ZiV%2Bpr2EhetHFyjdXliLgIAEK5vxejuYSuWTGcCjnQwioHwJuozQkklwZD2c4lhojs9O8Hk6Oa3bnUwFHJgvdK9Aj3nceHdGRzL6AHLcHiz52qgoAZJFI1ZJoWmJ6139VTtD1fviCIiCd8DtXuhNNyhnVFX11QDfshY0sxdHOF4tqDWk9bENbPaWOd1TIkZpM%2BXQWqiumKTatS2MHYVaEa78ASZSjNNF09AuQle06UCCABsCckQjsgbS01D9G%2Bbw8Y64AsRfkmZ8G71aYOvAHvws%2BWoUI08Gaiv37qA1FSTuqtz7qeCx2bZut%2BT%2BqopkL7r0aFezKvkic%2F5RCO2DLaAzrgFN8sQXehSUUfu9ZsqR%2BvDIWXjGWg1Q8XPLwQAE5Utl2zCMISck70GOqUBb14lqd5kIsXHIlUGpmRX0PbUyha6shZ3XhToK1it1vBbzG83YbTwSE11MI4uHpN7KXpajqGM6Rikc%2FbZxbQMnNCPVx84hYuVp0Q11jSvP5aidZNlWxgQqPfOqLmX%2Bi4S3lhD4nWLVieYI8TFcmHOI%2FDOzn9gjrv8wLBFNk98TwwfJzzW268LxLL3RBKKCv8JlzkmdRDvA8qYiXT536DZfTmLq%2BTl&X-Amz-Signature=35f298feea789f8905e608f3e1fb04a92aa2068f7c9bf952f6c7a2f81a617e6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTADDK4P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDeXtqYKOVG6QLtbQ490GaX2BSw%2Fa6MfVPju%2FD%2FGeos9AIgWzQpBIeH182hECZovdsxaSryeJkizoZR%2Be5ZhzuJZ7Aq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJ1r20UgIrS2g35qlircAzC6fTw2BC5IRrjCZPUtjBvv515dJ%2FOx0lWsxYyGh5%2F%2BH3XmGxXVfxbK31CyIA0P%2BCQ89wnG%2Bak5kxKjfNFsaPLeO6AI4Qz08wm9UwoX%2BhuJyFYiCDQHmbN4vuAhjMhKbo5SbGYHCOB%2B95tvExfjFW6swl6sBOZhkIaSZmH5wLh5pDeJAWzoAQ4IVFS%2Fv%2BIwlz06IhSYPd5KkkmUqCDZ%2FJH%2F4P63eTxAudD8aAr8xCOHXOV8%2B1Qr0ZiV%2Bpr2EhetHFyjdXliLgIAEK5vxejuYSuWTGcCjnQwioHwJuozQkklwZD2c4lhojs9O8Hk6Oa3bnUwFHJgvdK9Aj3nceHdGRzL6AHLcHiz52qgoAZJFI1ZJoWmJ6139VTtD1fviCIiCd8DtXuhNNyhnVFX11QDfshY0sxdHOF4tqDWk9bENbPaWOd1TIkZpM%2BXQWqiumKTatS2MHYVaEa78ASZSjNNF09AuQle06UCCABsCckQjsgbS01D9G%2Bbw8Y64AsRfkmZ8G71aYOvAHvws%2BWoUI08Gaiv37qA1FSTuqtz7qeCx2bZut%2BT%2BqopkL7r0aFezKvkic%2F5RCO2DLaAzrgFN8sQXehSUUfu9ZsqR%2BvDIWXjGWg1Q8XPLwQAE5Utl2zCMISck70GOqUBb14lqd5kIsXHIlUGpmRX0PbUyha6shZ3XhToK1it1vBbzG83YbTwSE11MI4uHpN7KXpajqGM6Rikc%2FbZxbQMnNCPVx84hYuVp0Q11jSvP5aidZNlWxgQqPfOqLmX%2Bi4S3lhD4nWLVieYI8TFcmHOI%2FDOzn9gjrv8wLBFNk98TwwfJzzW268LxLL3RBKKCv8JlzkmdRDvA8qYiXT536DZfTmLq%2BTl&X-Amz-Signature=ed96166195f507a89b9b74f2ba7ca2e30156c21f44dffc3eac2fdc7349a1eca6&X-Amz-SignedHeaders=host&x-id=GetObject)
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


