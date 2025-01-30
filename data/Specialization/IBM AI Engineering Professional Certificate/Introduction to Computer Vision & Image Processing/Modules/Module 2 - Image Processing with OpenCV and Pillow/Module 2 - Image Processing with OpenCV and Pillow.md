

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZXYP6PK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE5gtnuX%2BLRmJXk9z03qy0GhMLJuNEuWp6eeTUfk9fh%2BAiAZeYdPV%2BEkLVi0lC46OQPsnjYi1cbet3SJLk0qPT2u9yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe8NvZipCghBsC7pWKtwDxQ3UYQtSLYNhnTxRXs1UucLaU1onpxWYQFt85uXfuJf7DZaRUB7BqT7LNLvJN3fsMzIvhnWD%2FEkcZeLCngi4IHK7PzSVXNvJCQj9RbPjOIAy51iCscabjnmUesqUHSiVB%2Bs5y7PGkcCKXVp4VXmAYtCXXKCg9M0827jSIkL%2FjQ06vOLp%2FgC54agb%2B5fIWREG5Jtso%2BjU1cEtln8FyaUvikHyNZgLipIQtpbOEB7jgcHDz1GI9EWBP0vzeAkaUoy6Zd50CWr2enYzjuCLf4u2CyytPjfgWMZQzoLO0uWpKIXo4iDlcEsTTrjebjbtNm5t1XDuoq9IiA70OLMq3ylEf4frKyURPrpznagqEwm7ZeOYnEjdbylKef5hTAdmHr56KE6Iy6K%2BIwsrrQIy6DLmWFOK9IyBN1WyDmpf4OQh0sFdObaa94RfWxroQi7IN4SPzF7wF%2F87L9a%2F6cwvFhX21jK3iMinxqzcsKJQUTl%2FBzWMvfQZ2z36BMJCaaCX5Mm245pSqi7u4mZOXfJK2uzZv8cimutQbxRCx%2BDjPBaBQ7%2BDu4r84dbJLiPy4%2BddDkMTmj9yC2YrAjtpMOfDM9VpZ7y2hTbj%2Blrs%2BG8tZWvr23nSf2m1Cg6fz%2BNG%2FNMwxtjuvAY6pgFiysrGjJj0g9VouyN9iMPZtDKTXbZqNIWV2snAL9J7CbY8YjhYrCJ64PDpHrIu%2FtCntiV%2Fnj4rvq2nuTOXc8Z0X7KEp%2BlxrK8ws5GzM%2Fj9Ph4Ec8OMLyhvp3rPQX%2BFkzkjxNAUYGa3gKuYtj01ZXyPbv5%2BRpyMZTRc7%2FtGhXoloT5KueU8eGAMToA0hL2EOX7UMMrMerL%2FRx651a52Jy7PpjH5SN2f&X-Amz-Signature=aadb0483e2c64e589eb5e96be94b9746121ce0525c0c996ba1c6c075b881d18b&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WPUKNDS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwrzpD283LDXxj5gupah0OBvk2JnHBfXGvVovaVG2XYAiAVXEdZY%2F%2BF4VVTbtxihvm7f76WhtpTvkRtaDCm2GgH6yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYhGu5fDPbTXPvW3%2BKtwD3e4Yd8OmLIALhfw16%2F8v3gri3U6KA7xVPUTD4f%2FLcrlVLDv%2BXTO9dqSkqTVVx0%2F2bEiOHwXuzguVeU%2BeVaNGJsS7huI7CaPDsMY6S0tj5CCca4BrE6F4Cxvcoougfpe%2FlkAWuIjOv8gqBlruYB1r5GQhqOTRTwrJT8vRcFrGYzVR%2BDRHK48yzJtc1mkRGwLvR9RXAGDK%2BJnL2PVaXjO%2BlGFzLxuRIAvF%2BJaDLnANhMepaqJ6Aq%2F9hUevh6ZaEkrQIgZMR%2BYPDdBDRXNiFm7fnydcq%2BX1JGVJNedYtkMvjhU3hLcVBzFyx9JWETE0Ds6IAgSQb8xWb7LynvzdJN34mRp60nAkFKEBwBc7aVt%2Bwayz845TcQdGodTvjTN6LUG0yItUQrEBDM9JemxjrgofY5Y7gX6CgIesn%2F8%2FItTwAfS6LE%2Fs6ACsVszRpt6vWiSYyGxkVQ5SkH7K5TUU9a9aPkBEjH9gScYcPWxrWGkrGQBTzcyZbr%2BsvYmI1KWIuxKuIDAW%2BCK2%2Fa5RWIaPWTqY5HRGmYl%2B%2F5fwImbzdY7wt0iLR4KdV8LjsA3pYhSQf43dXBzpQonLbAKCettJrexxh%2FTwkwz6zCs%2FZjecS0MRZw%2F%2F5RVExoJn9JapZ%2F8w5dbuvAY6pgHehhFvIF4pSbNNDy5KccWziRJQL9zUwO1Mk%2BMGcGTi8W5igaQiKzXH1N3fn5iYfTzMeebAtSZD89%2FW8j9KRGG5s1VCoEGWWAFkn6AUXe%2Fg%2FYEpJPEJ3%2F5WkoGCy22PDpvX%2BIcFlTfDdudX%2F72GaeKgQXE5Nh2Qj8cz9sZyOv77ci1Ma%2FX8D5%2BNsArh5kkIo71%2BJ5aGn7lVQCbkmorZ%2F%2Fy2bMcdJC%2B8&X-Amz-Signature=191b96d0418bc963a92fc15380c6c185af0e0bc5d8b6bc327d3b3832912715df&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WPUKNDS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwrzpD283LDXxj5gupah0OBvk2JnHBfXGvVovaVG2XYAiAVXEdZY%2F%2BF4VVTbtxihvm7f76WhtpTvkRtaDCm2GgH6yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYhGu5fDPbTXPvW3%2BKtwD3e4Yd8OmLIALhfw16%2F8v3gri3U6KA7xVPUTD4f%2FLcrlVLDv%2BXTO9dqSkqTVVx0%2F2bEiOHwXuzguVeU%2BeVaNGJsS7huI7CaPDsMY6S0tj5CCca4BrE6F4Cxvcoougfpe%2FlkAWuIjOv8gqBlruYB1r5GQhqOTRTwrJT8vRcFrGYzVR%2BDRHK48yzJtc1mkRGwLvR9RXAGDK%2BJnL2PVaXjO%2BlGFzLxuRIAvF%2BJaDLnANhMepaqJ6Aq%2F9hUevh6ZaEkrQIgZMR%2BYPDdBDRXNiFm7fnydcq%2BX1JGVJNedYtkMvjhU3hLcVBzFyx9JWETE0Ds6IAgSQb8xWb7LynvzdJN34mRp60nAkFKEBwBc7aVt%2Bwayz845TcQdGodTvjTN6LUG0yItUQrEBDM9JemxjrgofY5Y7gX6CgIesn%2F8%2FItTwAfS6LE%2Fs6ACsVszRpt6vWiSYyGxkVQ5SkH7K5TUU9a9aPkBEjH9gScYcPWxrWGkrGQBTzcyZbr%2BsvYmI1KWIuxKuIDAW%2BCK2%2Fa5RWIaPWTqY5HRGmYl%2B%2F5fwImbzdY7wt0iLR4KdV8LjsA3pYhSQf43dXBzpQonLbAKCettJrexxh%2FTwkwz6zCs%2FZjecS0MRZw%2F%2F5RVExoJn9JapZ%2F8w5dbuvAY6pgHehhFvIF4pSbNNDy5KccWziRJQL9zUwO1Mk%2BMGcGTi8W5igaQiKzXH1N3fn5iYfTzMeebAtSZD89%2FW8j9KRGG5s1VCoEGWWAFkn6AUXe%2Fg%2FYEpJPEJ3%2F5WkoGCy22PDpvX%2BIcFlTfDdudX%2F72GaeKgQXE5Nh2Qj8cz9sZyOv77ci1Ma%2FX8D5%2BNsArh5kkIo71%2BJ5aGn7lVQCbkmorZ%2F%2Fy2bMcdJC%2B8&X-Amz-Signature=b2b7261ea67d363ceacd0bcb5acb18ee396f5214c0a7b6c343ae76db11e39c2a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WPUKNDS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwrzpD283LDXxj5gupah0OBvk2JnHBfXGvVovaVG2XYAiAVXEdZY%2F%2BF4VVTbtxihvm7f76WhtpTvkRtaDCm2GgH6yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYhGu5fDPbTXPvW3%2BKtwD3e4Yd8OmLIALhfw16%2F8v3gri3U6KA7xVPUTD4f%2FLcrlVLDv%2BXTO9dqSkqTVVx0%2F2bEiOHwXuzguVeU%2BeVaNGJsS7huI7CaPDsMY6S0tj5CCca4BrE6F4Cxvcoougfpe%2FlkAWuIjOv8gqBlruYB1r5GQhqOTRTwrJT8vRcFrGYzVR%2BDRHK48yzJtc1mkRGwLvR9RXAGDK%2BJnL2PVaXjO%2BlGFzLxuRIAvF%2BJaDLnANhMepaqJ6Aq%2F9hUevh6ZaEkrQIgZMR%2BYPDdBDRXNiFm7fnydcq%2BX1JGVJNedYtkMvjhU3hLcVBzFyx9JWETE0Ds6IAgSQb8xWb7LynvzdJN34mRp60nAkFKEBwBc7aVt%2Bwayz845TcQdGodTvjTN6LUG0yItUQrEBDM9JemxjrgofY5Y7gX6CgIesn%2F8%2FItTwAfS6LE%2Fs6ACsVszRpt6vWiSYyGxkVQ5SkH7K5TUU9a9aPkBEjH9gScYcPWxrWGkrGQBTzcyZbr%2BsvYmI1KWIuxKuIDAW%2BCK2%2Fa5RWIaPWTqY5HRGmYl%2B%2F5fwImbzdY7wt0iLR4KdV8LjsA3pYhSQf43dXBzpQonLbAKCettJrexxh%2FTwkwz6zCs%2FZjecS0MRZw%2F%2F5RVExoJn9JapZ%2F8w5dbuvAY6pgHehhFvIF4pSbNNDy5KccWziRJQL9zUwO1Mk%2BMGcGTi8W5igaQiKzXH1N3fn5iYfTzMeebAtSZD89%2FW8j9KRGG5s1VCoEGWWAFkn6AUXe%2Fg%2FYEpJPEJ3%2F5WkoGCy22PDpvX%2BIcFlTfDdudX%2F72GaeKgQXE5Nh2Qj8cz9sZyOv77ci1Ma%2FX8D5%2BNsArh5kkIo71%2BJ5aGn7lVQCbkmorZ%2F%2Fy2bMcdJC%2B8&X-Amz-Signature=52c0b8f1af98a36146b3ea4981f6c83d6164cdc96bb0307148c98edf0facf5aa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WPUKNDS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwrzpD283LDXxj5gupah0OBvk2JnHBfXGvVovaVG2XYAiAVXEdZY%2F%2BF4VVTbtxihvm7f76WhtpTvkRtaDCm2GgH6yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYhGu5fDPbTXPvW3%2BKtwD3e4Yd8OmLIALhfw16%2F8v3gri3U6KA7xVPUTD4f%2FLcrlVLDv%2BXTO9dqSkqTVVx0%2F2bEiOHwXuzguVeU%2BeVaNGJsS7huI7CaPDsMY6S0tj5CCca4BrE6F4Cxvcoougfpe%2FlkAWuIjOv8gqBlruYB1r5GQhqOTRTwrJT8vRcFrGYzVR%2BDRHK48yzJtc1mkRGwLvR9RXAGDK%2BJnL2PVaXjO%2BlGFzLxuRIAvF%2BJaDLnANhMepaqJ6Aq%2F9hUevh6ZaEkrQIgZMR%2BYPDdBDRXNiFm7fnydcq%2BX1JGVJNedYtkMvjhU3hLcVBzFyx9JWETE0Ds6IAgSQb8xWb7LynvzdJN34mRp60nAkFKEBwBc7aVt%2Bwayz845TcQdGodTvjTN6LUG0yItUQrEBDM9JemxjrgofY5Y7gX6CgIesn%2F8%2FItTwAfS6LE%2Fs6ACsVszRpt6vWiSYyGxkVQ5SkH7K5TUU9a9aPkBEjH9gScYcPWxrWGkrGQBTzcyZbr%2BsvYmI1KWIuxKuIDAW%2BCK2%2Fa5RWIaPWTqY5HRGmYl%2B%2F5fwImbzdY7wt0iLR4KdV8LjsA3pYhSQf43dXBzpQonLbAKCettJrexxh%2FTwkwz6zCs%2FZjecS0MRZw%2F%2F5RVExoJn9JapZ%2F8w5dbuvAY6pgHehhFvIF4pSbNNDy5KccWziRJQL9zUwO1Mk%2BMGcGTi8W5igaQiKzXH1N3fn5iYfTzMeebAtSZD89%2FW8j9KRGG5s1VCoEGWWAFkn6AUXe%2Fg%2FYEpJPEJ3%2F5WkoGCy22PDpvX%2BIcFlTfDdudX%2F72GaeKgQXE5Nh2Qj8cz9sZyOv77ci1Ma%2FX8D5%2BNsArh5kkIo71%2BJ5aGn7lVQCbkmorZ%2F%2Fy2bMcdJC%2B8&X-Amz-Signature=23611c1760da2a25440e7d612ccde320ce34be3c3004ecf4889e1e3e42eee3b1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WPUKNDS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwrzpD283LDXxj5gupah0OBvk2JnHBfXGvVovaVG2XYAiAVXEdZY%2F%2BF4VVTbtxihvm7f76WhtpTvkRtaDCm2GgH6yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYhGu5fDPbTXPvW3%2BKtwD3e4Yd8OmLIALhfw16%2F8v3gri3U6KA7xVPUTD4f%2FLcrlVLDv%2BXTO9dqSkqTVVx0%2F2bEiOHwXuzguVeU%2BeVaNGJsS7huI7CaPDsMY6S0tj5CCca4BrE6F4Cxvcoougfpe%2FlkAWuIjOv8gqBlruYB1r5GQhqOTRTwrJT8vRcFrGYzVR%2BDRHK48yzJtc1mkRGwLvR9RXAGDK%2BJnL2PVaXjO%2BlGFzLxuRIAvF%2BJaDLnANhMepaqJ6Aq%2F9hUevh6ZaEkrQIgZMR%2BYPDdBDRXNiFm7fnydcq%2BX1JGVJNedYtkMvjhU3hLcVBzFyx9JWETE0Ds6IAgSQb8xWb7LynvzdJN34mRp60nAkFKEBwBc7aVt%2Bwayz845TcQdGodTvjTN6LUG0yItUQrEBDM9JemxjrgofY5Y7gX6CgIesn%2F8%2FItTwAfS6LE%2Fs6ACsVszRpt6vWiSYyGxkVQ5SkH7K5TUU9a9aPkBEjH9gScYcPWxrWGkrGQBTzcyZbr%2BsvYmI1KWIuxKuIDAW%2BCK2%2Fa5RWIaPWTqY5HRGmYl%2B%2F5fwImbzdY7wt0iLR4KdV8LjsA3pYhSQf43dXBzpQonLbAKCettJrexxh%2FTwkwz6zCs%2FZjecS0MRZw%2F%2F5RVExoJn9JapZ%2F8w5dbuvAY6pgHehhFvIF4pSbNNDy5KccWziRJQL9zUwO1Mk%2BMGcGTi8W5igaQiKzXH1N3fn5iYfTzMeebAtSZD89%2FW8j9KRGG5s1VCoEGWWAFkn6AUXe%2Fg%2FYEpJPEJ3%2F5WkoGCy22PDpvX%2BIcFlTfDdudX%2F72GaeKgQXE5Nh2Qj8cz9sZyOv77ci1Ma%2FX8D5%2BNsArh5kkIo71%2BJ5aGn7lVQCbkmorZ%2F%2Fy2bMcdJC%2B8&X-Amz-Signature=1c07293aa3c0a364421daec61fd111e8bd6812368b26d86940634058e176cdbe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZXYP6PK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE5gtnuX%2BLRmJXk9z03qy0GhMLJuNEuWp6eeTUfk9fh%2BAiAZeYdPV%2BEkLVi0lC46OQPsnjYi1cbet3SJLk0qPT2u9yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe8NvZipCghBsC7pWKtwDxQ3UYQtSLYNhnTxRXs1UucLaU1onpxWYQFt85uXfuJf7DZaRUB7BqT7LNLvJN3fsMzIvhnWD%2FEkcZeLCngi4IHK7PzSVXNvJCQj9RbPjOIAy51iCscabjnmUesqUHSiVB%2Bs5y7PGkcCKXVp4VXmAYtCXXKCg9M0827jSIkL%2FjQ06vOLp%2FgC54agb%2B5fIWREG5Jtso%2BjU1cEtln8FyaUvikHyNZgLipIQtpbOEB7jgcHDz1GI9EWBP0vzeAkaUoy6Zd50CWr2enYzjuCLf4u2CyytPjfgWMZQzoLO0uWpKIXo4iDlcEsTTrjebjbtNm5t1XDuoq9IiA70OLMq3ylEf4frKyURPrpznagqEwm7ZeOYnEjdbylKef5hTAdmHr56KE6Iy6K%2BIwsrrQIy6DLmWFOK9IyBN1WyDmpf4OQh0sFdObaa94RfWxroQi7IN4SPzF7wF%2F87L9a%2F6cwvFhX21jK3iMinxqzcsKJQUTl%2FBzWMvfQZ2z36BMJCaaCX5Mm245pSqi7u4mZOXfJK2uzZv8cimutQbxRCx%2BDjPBaBQ7%2BDu4r84dbJLiPy4%2BddDkMTmj9yC2YrAjtpMOfDM9VpZ7y2hTbj%2Blrs%2BG8tZWvr23nSf2m1Cg6fz%2BNG%2FNMwxtjuvAY6pgFiysrGjJj0g9VouyN9iMPZtDKTXbZqNIWV2snAL9J7CbY8YjhYrCJ64PDpHrIu%2FtCntiV%2Fnj4rvq2nuTOXc8Z0X7KEp%2BlxrK8ws5GzM%2Fj9Ph4Ec8OMLyhvp3rPQX%2BFkzkjxNAUYGa3gKuYtj01ZXyPbv5%2BRpyMZTRc7%2FtGhXoloT5KueU8eGAMToA0hL2EOX7UMMrMerL%2FRx651a52Jy7PpjH5SN2f&X-Amz-Signature=3050aabcba95e6ba0f6ad975a16b5002800585cb22469b023578b411a9d8f490&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZXYP6PK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE5gtnuX%2BLRmJXk9z03qy0GhMLJuNEuWp6eeTUfk9fh%2BAiAZeYdPV%2BEkLVi0lC46OQPsnjYi1cbet3SJLk0qPT2u9yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe8NvZipCghBsC7pWKtwDxQ3UYQtSLYNhnTxRXs1UucLaU1onpxWYQFt85uXfuJf7DZaRUB7BqT7LNLvJN3fsMzIvhnWD%2FEkcZeLCngi4IHK7PzSVXNvJCQj9RbPjOIAy51iCscabjnmUesqUHSiVB%2Bs5y7PGkcCKXVp4VXmAYtCXXKCg9M0827jSIkL%2FjQ06vOLp%2FgC54agb%2B5fIWREG5Jtso%2BjU1cEtln8FyaUvikHyNZgLipIQtpbOEB7jgcHDz1GI9EWBP0vzeAkaUoy6Zd50CWr2enYzjuCLf4u2CyytPjfgWMZQzoLO0uWpKIXo4iDlcEsTTrjebjbtNm5t1XDuoq9IiA70OLMq3ylEf4frKyURPrpznagqEwm7ZeOYnEjdbylKef5hTAdmHr56KE6Iy6K%2BIwsrrQIy6DLmWFOK9IyBN1WyDmpf4OQh0sFdObaa94RfWxroQi7IN4SPzF7wF%2F87L9a%2F6cwvFhX21jK3iMinxqzcsKJQUTl%2FBzWMvfQZ2z36BMJCaaCX5Mm245pSqi7u4mZOXfJK2uzZv8cimutQbxRCx%2BDjPBaBQ7%2BDu4r84dbJLiPy4%2BddDkMTmj9yC2YrAjtpMOfDM9VpZ7y2hTbj%2Blrs%2BG8tZWvr23nSf2m1Cg6fz%2BNG%2FNMwxtjuvAY6pgFiysrGjJj0g9VouyN9iMPZtDKTXbZqNIWV2snAL9J7CbY8YjhYrCJ64PDpHrIu%2FtCntiV%2Fnj4rvq2nuTOXc8Z0X7KEp%2BlxrK8ws5GzM%2Fj9Ph4Ec8OMLyhvp3rPQX%2BFkzkjxNAUYGa3gKuYtj01ZXyPbv5%2BRpyMZTRc7%2FtGhXoloT5KueU8eGAMToA0hL2EOX7UMMrMerL%2FRx651a52Jy7PpjH5SN2f&X-Amz-Signature=c3621c14849139fc2b839000b256db49079fdb52188ffaa9ab0622837605523b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZXYP6PK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE5gtnuX%2BLRmJXk9z03qy0GhMLJuNEuWp6eeTUfk9fh%2BAiAZeYdPV%2BEkLVi0lC46OQPsnjYi1cbet3SJLk0qPT2u9yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe8NvZipCghBsC7pWKtwDxQ3UYQtSLYNhnTxRXs1UucLaU1onpxWYQFt85uXfuJf7DZaRUB7BqT7LNLvJN3fsMzIvhnWD%2FEkcZeLCngi4IHK7PzSVXNvJCQj9RbPjOIAy51iCscabjnmUesqUHSiVB%2Bs5y7PGkcCKXVp4VXmAYtCXXKCg9M0827jSIkL%2FjQ06vOLp%2FgC54agb%2B5fIWREG5Jtso%2BjU1cEtln8FyaUvikHyNZgLipIQtpbOEB7jgcHDz1GI9EWBP0vzeAkaUoy6Zd50CWr2enYzjuCLf4u2CyytPjfgWMZQzoLO0uWpKIXo4iDlcEsTTrjebjbtNm5t1XDuoq9IiA70OLMq3ylEf4frKyURPrpznagqEwm7ZeOYnEjdbylKef5hTAdmHr56KE6Iy6K%2BIwsrrQIy6DLmWFOK9IyBN1WyDmpf4OQh0sFdObaa94RfWxroQi7IN4SPzF7wF%2F87L9a%2F6cwvFhX21jK3iMinxqzcsKJQUTl%2FBzWMvfQZ2z36BMJCaaCX5Mm245pSqi7u4mZOXfJK2uzZv8cimutQbxRCx%2BDjPBaBQ7%2BDu4r84dbJLiPy4%2BddDkMTmj9yC2YrAjtpMOfDM9VpZ7y2hTbj%2Blrs%2BG8tZWvr23nSf2m1Cg6fz%2BNG%2FNMwxtjuvAY6pgFiysrGjJj0g9VouyN9iMPZtDKTXbZqNIWV2snAL9J7CbY8YjhYrCJ64PDpHrIu%2FtCntiV%2Fnj4rvq2nuTOXc8Z0X7KEp%2BlxrK8ws5GzM%2Fj9Ph4Ec8OMLyhvp3rPQX%2BFkzkjxNAUYGa3gKuYtj01ZXyPbv5%2BRpyMZTRc7%2FtGhXoloT5KueU8eGAMToA0hL2EOX7UMMrMerL%2FRx651a52Jy7PpjH5SN2f&X-Amz-Signature=2f9838f51fc6f64c67e3d6e31cbb523e0151f7a046696ed5eaf9660bf1d86925&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZXYP6PK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE5gtnuX%2BLRmJXk9z03qy0GhMLJuNEuWp6eeTUfk9fh%2BAiAZeYdPV%2BEkLVi0lC46OQPsnjYi1cbet3SJLk0qPT2u9yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe8NvZipCghBsC7pWKtwDxQ3UYQtSLYNhnTxRXs1UucLaU1onpxWYQFt85uXfuJf7DZaRUB7BqT7LNLvJN3fsMzIvhnWD%2FEkcZeLCngi4IHK7PzSVXNvJCQj9RbPjOIAy51iCscabjnmUesqUHSiVB%2Bs5y7PGkcCKXVp4VXmAYtCXXKCg9M0827jSIkL%2FjQ06vOLp%2FgC54agb%2B5fIWREG5Jtso%2BjU1cEtln8FyaUvikHyNZgLipIQtpbOEB7jgcHDz1GI9EWBP0vzeAkaUoy6Zd50CWr2enYzjuCLf4u2CyytPjfgWMZQzoLO0uWpKIXo4iDlcEsTTrjebjbtNm5t1XDuoq9IiA70OLMq3ylEf4frKyURPrpznagqEwm7ZeOYnEjdbylKef5hTAdmHr56KE6Iy6K%2BIwsrrQIy6DLmWFOK9IyBN1WyDmpf4OQh0sFdObaa94RfWxroQi7IN4SPzF7wF%2F87L9a%2F6cwvFhX21jK3iMinxqzcsKJQUTl%2FBzWMvfQZ2z36BMJCaaCX5Mm245pSqi7u4mZOXfJK2uzZv8cimutQbxRCx%2BDjPBaBQ7%2BDu4r84dbJLiPy4%2BddDkMTmj9yC2YrAjtpMOfDM9VpZ7y2hTbj%2Blrs%2BG8tZWvr23nSf2m1Cg6fz%2BNG%2FNMwxtjuvAY6pgFiysrGjJj0g9VouyN9iMPZtDKTXbZqNIWV2snAL9J7CbY8YjhYrCJ64PDpHrIu%2FtCntiV%2Fnj4rvq2nuTOXc8Z0X7KEp%2BlxrK8ws5GzM%2Fj9Ph4Ec8OMLyhvp3rPQX%2BFkzkjxNAUYGa3gKuYtj01ZXyPbv5%2BRpyMZTRc7%2FtGhXoloT5KueU8eGAMToA0hL2EOX7UMMrMerL%2FRx651a52Jy7PpjH5SN2f&X-Amz-Signature=9084063337ddc14feb85129d58aa3a12cace4ea11f674ea59192c1146e2f0afe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZXYP6PK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE5gtnuX%2BLRmJXk9z03qy0GhMLJuNEuWp6eeTUfk9fh%2BAiAZeYdPV%2BEkLVi0lC46OQPsnjYi1cbet3SJLk0qPT2u9yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe8NvZipCghBsC7pWKtwDxQ3UYQtSLYNhnTxRXs1UucLaU1onpxWYQFt85uXfuJf7DZaRUB7BqT7LNLvJN3fsMzIvhnWD%2FEkcZeLCngi4IHK7PzSVXNvJCQj9RbPjOIAy51iCscabjnmUesqUHSiVB%2Bs5y7PGkcCKXVp4VXmAYtCXXKCg9M0827jSIkL%2FjQ06vOLp%2FgC54agb%2B5fIWREG5Jtso%2BjU1cEtln8FyaUvikHyNZgLipIQtpbOEB7jgcHDz1GI9EWBP0vzeAkaUoy6Zd50CWr2enYzjuCLf4u2CyytPjfgWMZQzoLO0uWpKIXo4iDlcEsTTrjebjbtNm5t1XDuoq9IiA70OLMq3ylEf4frKyURPrpznagqEwm7ZeOYnEjdbylKef5hTAdmHr56KE6Iy6K%2BIwsrrQIy6DLmWFOK9IyBN1WyDmpf4OQh0sFdObaa94RfWxroQi7IN4SPzF7wF%2F87L9a%2F6cwvFhX21jK3iMinxqzcsKJQUTl%2FBzWMvfQZ2z36BMJCaaCX5Mm245pSqi7u4mZOXfJK2uzZv8cimutQbxRCx%2BDjPBaBQ7%2BDu4r84dbJLiPy4%2BddDkMTmj9yC2YrAjtpMOfDM9VpZ7y2hTbj%2Blrs%2BG8tZWvr23nSf2m1Cg6fz%2BNG%2FNMwxtjuvAY6pgFiysrGjJj0g9VouyN9iMPZtDKTXbZqNIWV2snAL9J7CbY8YjhYrCJ64PDpHrIu%2FtCntiV%2Fnj4rvq2nuTOXc8Z0X7KEp%2BlxrK8ws5GzM%2Fj9Ph4Ec8OMLyhvp3rPQX%2BFkzkjxNAUYGa3gKuYtj01ZXyPbv5%2BRpyMZTRc7%2FtGhXoloT5KueU8eGAMToA0hL2EOX7UMMrMerL%2FRx651a52Jy7PpjH5SN2f&X-Amz-Signature=c24e5f6fa8018c17a95f95d66718768f4ae75de92c8156d80dfe98c58b6a9b76&X-Amz-SignedHeaders=host&x-id=GetObject)
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


