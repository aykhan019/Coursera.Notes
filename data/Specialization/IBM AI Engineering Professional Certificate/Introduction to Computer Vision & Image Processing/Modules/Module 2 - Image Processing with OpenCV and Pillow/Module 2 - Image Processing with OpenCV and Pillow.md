

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666WY7T7H%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4%2B0%2B9LemfzWXtbnTMDWCJDtnNmKwrCblMCsedChiitAiBS4pFyo3rAXTgC%2BD471ngJnlR3q5FTZtx9U4fBxLJP9SqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtJUt19zBCx3VW5iMKtwDRv7GDGAv2t%2BQGxZhysczcW6asN4E9jh5UxoB%2FIfUGAh8xX8At1YTvWmAbw0R8FNUO9Twx2dWcrt3k3HyZOruMTo6%2BKjBhr3T%2BnRK7a5vAzLrLUbWBgyIvfGMGQV0BlL4SAXvsi8zWzbSyslpqncDJH9FHeheBG2%2ByB5Z2vKD3tmkcVBtfySaBQ3hysP7lV5g4BSqLnE223g%2FfE7hNz5HGg1B79dMVik8ze8gW%2BVxKpn0bdJ2Z2pF7Zy5cnlN2RR9JUgtLOtcH%2FaxWShCiYaDENE40Lk477UzGhbNUcYSfVVWbhsCWfiiZNBcTvGKVShjOYAEOqg6yGtlglDrBD0MQc%2FQ2sFCi40ls%2BhKqwIgSEqaS2HUTysG8RCkAUPL75wAT2MACQ5NQkoAR3n5x39OHLbDVlXC0EsNMrBNpu8ekAG8NueeQqIzwjc1vY6FDiTyHqQOUHr3oW8E4CjsxTmHhHWHswpOWe2%2BZ3CEvbUZneDCF7lanqM1HcAp8BtaLEwbnz9DFIR9gqTJxqebA3EdPxfMBcjH5S37sBJUvHh2Icl2hQE0Euj8BAWvX3JcqzJ9Uh6EsqhLTDH03%2FF%2FKaqt74v5bJcoVoBy0wBJxZLby8Jbush9vX5rpLbigIAwi5fuvAY6pgHBn6uazqtVRvOPfg%2F6%2BXRD0p4YJ0lFXqceuw9mBdkMR8zSWH6y31jWrmdY%2FTgCJDkOK5uHZXBooxHDd6tb8b3MbG5tEChocfK8IRnTaRG9dqC%2BkcDE3EQPPGPjVeLPly3QfOG8wEkRcnIA85rvN%2B%2FCW%2Bm8LgdwdEpPVCwSYsMf6HAnrvl61GwZS1ZntiAqIxkgGGmeliVaxUeXbmkfJBtSkRWIwp%2F0&X-Amz-Signature=a76c3ab4d1d1d408dfd2a7e37606a0e2f85f4266175c143a791de136915270a7&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPSFFVKZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCR92hvwydNM26dz8q2aUeZtt%2BB7KSUtwrXWuzObo7CYwIhALs%2FrzVr6IALWnmHjzy4RmI4WovVmjQwMgJN3wgpjZxpKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxziaqqsDxOonHlX7Eq3AP0YvAcB1O%2F8T6CjZzGdMu9QdDx22zJqRBE5Sqd%2FQX44BXtmqvn6Ie0zIUW33Qo%2FmD3n4F1h1LeOY8vxNfG5n%2BhCV1s7W5t3RVCY4XMeF1MsqsHT5TPue93y0bi%2FL%2BK7NuN%2Fg00X7LezXC5FeIXul9hd%2BSx8Yej9shpzWpctPmw%2BuAZVDr99FvmauaKm06Z%2BMQngGkkQ5baV%2BpVSNbRInhaWd%2FoP2qeMWp2xJVZluyIdhNPJIFVImirvUE5VoVnjhewUlkiTL9k6tP%2BF5QLjB5zd1Rm4AHoLbRFi34J414U1gJXWeP3d%2F0T5hirZd%2F8g0MANhwvCI3rcQuoSpd%2Fj1oqcczxXZl8ADKYnuAXhL%2BTMcV8lyxC51g%2BZshLK5WvGiuULM5zR9iQMkCs8jJbTnNZMItaK3q6MoSbWjRXYJo9Rbhyl%2Bc%2Bfcxtbj3sGLFBjqGant6%2BuQNvOsBEBOcuvtt%2BwMU8B38cu9tNMEpatzI02CZCkoW%2BF9d5K2Yxq33oSLwgHgel1OCoeL3PDjvFPGZalVOWqe7bw5awcAQjzbAUdklQ63x75qQzqs7o6tBPru0FNBNnI4NGtwi44kN5cPROZP5bFaYJe%2Fpy6uyF9N02hqj%2FSJh2hC3tr3EdTjD%2Blu68BjqkASes8XdYkVSfizLBPZn4KmgohZzkwJas6VZ%2BZ4SJn7MtRacWUGiyQE9A45deGNmtsWolfbhopWtD%2BNe9SPk5kKG2GJKtinrj3IuKuxGafOi5zqR16msd5qJn%2B9Ebjjn6Tq8%2Fe3sb0BOsS5bDYaxMQF%2BDmwh6qAdT5vE3RcuSsQQfIb6BxkjLVlw3JhPRrP76emaKhKvjbhggFZGTEkCjIE%2Bxoir0&X-Amz-Signature=92c911857b22c8b3150e5596ce1d36fa0258cd7e874771dcabf182eb9699de61&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPSFFVKZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCR92hvwydNM26dz8q2aUeZtt%2BB7KSUtwrXWuzObo7CYwIhALs%2FrzVr6IALWnmHjzy4RmI4WovVmjQwMgJN3wgpjZxpKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxziaqqsDxOonHlX7Eq3AP0YvAcB1O%2F8T6CjZzGdMu9QdDx22zJqRBE5Sqd%2FQX44BXtmqvn6Ie0zIUW33Qo%2FmD3n4F1h1LeOY8vxNfG5n%2BhCV1s7W5t3RVCY4XMeF1MsqsHT5TPue93y0bi%2FL%2BK7NuN%2Fg00X7LezXC5FeIXul9hd%2BSx8Yej9shpzWpctPmw%2BuAZVDr99FvmauaKm06Z%2BMQngGkkQ5baV%2BpVSNbRInhaWd%2FoP2qeMWp2xJVZluyIdhNPJIFVImirvUE5VoVnjhewUlkiTL9k6tP%2BF5QLjB5zd1Rm4AHoLbRFi34J414U1gJXWeP3d%2F0T5hirZd%2F8g0MANhwvCI3rcQuoSpd%2Fj1oqcczxXZl8ADKYnuAXhL%2BTMcV8lyxC51g%2BZshLK5WvGiuULM5zR9iQMkCs8jJbTnNZMItaK3q6MoSbWjRXYJo9Rbhyl%2Bc%2Bfcxtbj3sGLFBjqGant6%2BuQNvOsBEBOcuvtt%2BwMU8B38cu9tNMEpatzI02CZCkoW%2BF9d5K2Yxq33oSLwgHgel1OCoeL3PDjvFPGZalVOWqe7bw5awcAQjzbAUdklQ63x75qQzqs7o6tBPru0FNBNnI4NGtwi44kN5cPROZP5bFaYJe%2Fpy6uyF9N02hqj%2FSJh2hC3tr3EdTjD%2Blu68BjqkASes8XdYkVSfizLBPZn4KmgohZzkwJas6VZ%2BZ4SJn7MtRacWUGiyQE9A45deGNmtsWolfbhopWtD%2BNe9SPk5kKG2GJKtinrj3IuKuxGafOi5zqR16msd5qJn%2B9Ebjjn6Tq8%2Fe3sb0BOsS5bDYaxMQF%2BDmwh6qAdT5vE3RcuSsQQfIb6BxkjLVlw3JhPRrP76emaKhKvjbhggFZGTEkCjIE%2Bxoir0&X-Amz-Signature=ad696dfbc41858f551dc6b62694e77271a7f20f7a43504a528a475733f63c407&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPSFFVKZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCR92hvwydNM26dz8q2aUeZtt%2BB7KSUtwrXWuzObo7CYwIhALs%2FrzVr6IALWnmHjzy4RmI4WovVmjQwMgJN3wgpjZxpKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxziaqqsDxOonHlX7Eq3AP0YvAcB1O%2F8T6CjZzGdMu9QdDx22zJqRBE5Sqd%2FQX44BXtmqvn6Ie0zIUW33Qo%2FmD3n4F1h1LeOY8vxNfG5n%2BhCV1s7W5t3RVCY4XMeF1MsqsHT5TPue93y0bi%2FL%2BK7NuN%2Fg00X7LezXC5FeIXul9hd%2BSx8Yej9shpzWpctPmw%2BuAZVDr99FvmauaKm06Z%2BMQngGkkQ5baV%2BpVSNbRInhaWd%2FoP2qeMWp2xJVZluyIdhNPJIFVImirvUE5VoVnjhewUlkiTL9k6tP%2BF5QLjB5zd1Rm4AHoLbRFi34J414U1gJXWeP3d%2F0T5hirZd%2F8g0MANhwvCI3rcQuoSpd%2Fj1oqcczxXZl8ADKYnuAXhL%2BTMcV8lyxC51g%2BZshLK5WvGiuULM5zR9iQMkCs8jJbTnNZMItaK3q6MoSbWjRXYJo9Rbhyl%2Bc%2Bfcxtbj3sGLFBjqGant6%2BuQNvOsBEBOcuvtt%2BwMU8B38cu9tNMEpatzI02CZCkoW%2BF9d5K2Yxq33oSLwgHgel1OCoeL3PDjvFPGZalVOWqe7bw5awcAQjzbAUdklQ63x75qQzqs7o6tBPru0FNBNnI4NGtwi44kN5cPROZP5bFaYJe%2Fpy6uyF9N02hqj%2FSJh2hC3tr3EdTjD%2Blu68BjqkASes8XdYkVSfizLBPZn4KmgohZzkwJas6VZ%2BZ4SJn7MtRacWUGiyQE9A45deGNmtsWolfbhopWtD%2BNe9SPk5kKG2GJKtinrj3IuKuxGafOi5zqR16msd5qJn%2B9Ebjjn6Tq8%2Fe3sb0BOsS5bDYaxMQF%2BDmwh6qAdT5vE3RcuSsQQfIb6BxkjLVlw3JhPRrP76emaKhKvjbhggFZGTEkCjIE%2Bxoir0&X-Amz-Signature=dc364dcc387950114eeac3c4ca758db4626693a035236e2a8667ea3d724f7cc8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPSFFVKZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCR92hvwydNM26dz8q2aUeZtt%2BB7KSUtwrXWuzObo7CYwIhALs%2FrzVr6IALWnmHjzy4RmI4WovVmjQwMgJN3wgpjZxpKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxziaqqsDxOonHlX7Eq3AP0YvAcB1O%2F8T6CjZzGdMu9QdDx22zJqRBE5Sqd%2FQX44BXtmqvn6Ie0zIUW33Qo%2FmD3n4F1h1LeOY8vxNfG5n%2BhCV1s7W5t3RVCY4XMeF1MsqsHT5TPue93y0bi%2FL%2BK7NuN%2Fg00X7LezXC5FeIXul9hd%2BSx8Yej9shpzWpctPmw%2BuAZVDr99FvmauaKm06Z%2BMQngGkkQ5baV%2BpVSNbRInhaWd%2FoP2qeMWp2xJVZluyIdhNPJIFVImirvUE5VoVnjhewUlkiTL9k6tP%2BF5QLjB5zd1Rm4AHoLbRFi34J414U1gJXWeP3d%2F0T5hirZd%2F8g0MANhwvCI3rcQuoSpd%2Fj1oqcczxXZl8ADKYnuAXhL%2BTMcV8lyxC51g%2BZshLK5WvGiuULM5zR9iQMkCs8jJbTnNZMItaK3q6MoSbWjRXYJo9Rbhyl%2Bc%2Bfcxtbj3sGLFBjqGant6%2BuQNvOsBEBOcuvtt%2BwMU8B38cu9tNMEpatzI02CZCkoW%2BF9d5K2Yxq33oSLwgHgel1OCoeL3PDjvFPGZalVOWqe7bw5awcAQjzbAUdklQ63x75qQzqs7o6tBPru0FNBNnI4NGtwi44kN5cPROZP5bFaYJe%2Fpy6uyF9N02hqj%2FSJh2hC3tr3EdTjD%2Blu68BjqkASes8XdYkVSfizLBPZn4KmgohZzkwJas6VZ%2BZ4SJn7MtRacWUGiyQE9A45deGNmtsWolfbhopWtD%2BNe9SPk5kKG2GJKtinrj3IuKuxGafOi5zqR16msd5qJn%2B9Ebjjn6Tq8%2Fe3sb0BOsS5bDYaxMQF%2BDmwh6qAdT5vE3RcuSsQQfIb6BxkjLVlw3JhPRrP76emaKhKvjbhggFZGTEkCjIE%2Bxoir0&X-Amz-Signature=456fd28675b5ef0e79fac2f75b49d4c87b8f9bb7b5117ef86f9a7a64a98e875d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPSFFVKZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCR92hvwydNM26dz8q2aUeZtt%2BB7KSUtwrXWuzObo7CYwIhALs%2FrzVr6IALWnmHjzy4RmI4WovVmjQwMgJN3wgpjZxpKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxziaqqsDxOonHlX7Eq3AP0YvAcB1O%2F8T6CjZzGdMu9QdDx22zJqRBE5Sqd%2FQX44BXtmqvn6Ie0zIUW33Qo%2FmD3n4F1h1LeOY8vxNfG5n%2BhCV1s7W5t3RVCY4XMeF1MsqsHT5TPue93y0bi%2FL%2BK7NuN%2Fg00X7LezXC5FeIXul9hd%2BSx8Yej9shpzWpctPmw%2BuAZVDr99FvmauaKm06Z%2BMQngGkkQ5baV%2BpVSNbRInhaWd%2FoP2qeMWp2xJVZluyIdhNPJIFVImirvUE5VoVnjhewUlkiTL9k6tP%2BF5QLjB5zd1Rm4AHoLbRFi34J414U1gJXWeP3d%2F0T5hirZd%2F8g0MANhwvCI3rcQuoSpd%2Fj1oqcczxXZl8ADKYnuAXhL%2BTMcV8lyxC51g%2BZshLK5WvGiuULM5zR9iQMkCs8jJbTnNZMItaK3q6MoSbWjRXYJo9Rbhyl%2Bc%2Bfcxtbj3sGLFBjqGant6%2BuQNvOsBEBOcuvtt%2BwMU8B38cu9tNMEpatzI02CZCkoW%2BF9d5K2Yxq33oSLwgHgel1OCoeL3PDjvFPGZalVOWqe7bw5awcAQjzbAUdklQ63x75qQzqs7o6tBPru0FNBNnI4NGtwi44kN5cPROZP5bFaYJe%2Fpy6uyF9N02hqj%2FSJh2hC3tr3EdTjD%2Blu68BjqkASes8XdYkVSfizLBPZn4KmgohZzkwJas6VZ%2BZ4SJn7MtRacWUGiyQE9A45deGNmtsWolfbhopWtD%2BNe9SPk5kKG2GJKtinrj3IuKuxGafOi5zqR16msd5qJn%2B9Ebjjn6Tq8%2Fe3sb0BOsS5bDYaxMQF%2BDmwh6qAdT5vE3RcuSsQQfIb6BxkjLVlw3JhPRrP76emaKhKvjbhggFZGTEkCjIE%2Bxoir0&X-Amz-Signature=c93cd615ef87e6a3e04de98ffdfa442ff0b639ce7509d53769b2c1887300890f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666WY7T7H%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4%2B0%2B9LemfzWXtbnTMDWCJDtnNmKwrCblMCsedChiitAiBS4pFyo3rAXTgC%2BD471ngJnlR3q5FTZtx9U4fBxLJP9SqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtJUt19zBCx3VW5iMKtwDRv7GDGAv2t%2BQGxZhysczcW6asN4E9jh5UxoB%2FIfUGAh8xX8At1YTvWmAbw0R8FNUO9Twx2dWcrt3k3HyZOruMTo6%2BKjBhr3T%2BnRK7a5vAzLrLUbWBgyIvfGMGQV0BlL4SAXvsi8zWzbSyslpqncDJH9FHeheBG2%2ByB5Z2vKD3tmkcVBtfySaBQ3hysP7lV5g4BSqLnE223g%2FfE7hNz5HGg1B79dMVik8ze8gW%2BVxKpn0bdJ2Z2pF7Zy5cnlN2RR9JUgtLOtcH%2FaxWShCiYaDENE40Lk477UzGhbNUcYSfVVWbhsCWfiiZNBcTvGKVShjOYAEOqg6yGtlglDrBD0MQc%2FQ2sFCi40ls%2BhKqwIgSEqaS2HUTysG8RCkAUPL75wAT2MACQ5NQkoAR3n5x39OHLbDVlXC0EsNMrBNpu8ekAG8NueeQqIzwjc1vY6FDiTyHqQOUHr3oW8E4CjsxTmHhHWHswpOWe2%2BZ3CEvbUZneDCF7lanqM1HcAp8BtaLEwbnz9DFIR9gqTJxqebA3EdPxfMBcjH5S37sBJUvHh2Icl2hQE0Euj8BAWvX3JcqzJ9Uh6EsqhLTDH03%2FF%2FKaqt74v5bJcoVoBy0wBJxZLby8Jbush9vX5rpLbigIAwi5fuvAY6pgHBn6uazqtVRvOPfg%2F6%2BXRD0p4YJ0lFXqceuw9mBdkMR8zSWH6y31jWrmdY%2FTgCJDkOK5uHZXBooxHDd6tb8b3MbG5tEChocfK8IRnTaRG9dqC%2BkcDE3EQPPGPjVeLPly3QfOG8wEkRcnIA85rvN%2B%2FCW%2Bm8LgdwdEpPVCwSYsMf6HAnrvl61GwZS1ZntiAqIxkgGGmeliVaxUeXbmkfJBtSkRWIwp%2F0&X-Amz-Signature=f941ff88580b5205d23f46f47328d57e93fd9fc5574ac014cd9b0ad0c5ca8b7e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666WY7T7H%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4%2B0%2B9LemfzWXtbnTMDWCJDtnNmKwrCblMCsedChiitAiBS4pFyo3rAXTgC%2BD471ngJnlR3q5FTZtx9U4fBxLJP9SqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtJUt19zBCx3VW5iMKtwDRv7GDGAv2t%2BQGxZhysczcW6asN4E9jh5UxoB%2FIfUGAh8xX8At1YTvWmAbw0R8FNUO9Twx2dWcrt3k3HyZOruMTo6%2BKjBhr3T%2BnRK7a5vAzLrLUbWBgyIvfGMGQV0BlL4SAXvsi8zWzbSyslpqncDJH9FHeheBG2%2ByB5Z2vKD3tmkcVBtfySaBQ3hysP7lV5g4BSqLnE223g%2FfE7hNz5HGg1B79dMVik8ze8gW%2BVxKpn0bdJ2Z2pF7Zy5cnlN2RR9JUgtLOtcH%2FaxWShCiYaDENE40Lk477UzGhbNUcYSfVVWbhsCWfiiZNBcTvGKVShjOYAEOqg6yGtlglDrBD0MQc%2FQ2sFCi40ls%2BhKqwIgSEqaS2HUTysG8RCkAUPL75wAT2MACQ5NQkoAR3n5x39OHLbDVlXC0EsNMrBNpu8ekAG8NueeQqIzwjc1vY6FDiTyHqQOUHr3oW8E4CjsxTmHhHWHswpOWe2%2BZ3CEvbUZneDCF7lanqM1HcAp8BtaLEwbnz9DFIR9gqTJxqebA3EdPxfMBcjH5S37sBJUvHh2Icl2hQE0Euj8BAWvX3JcqzJ9Uh6EsqhLTDH03%2FF%2FKaqt74v5bJcoVoBy0wBJxZLby8Jbush9vX5rpLbigIAwi5fuvAY6pgHBn6uazqtVRvOPfg%2F6%2BXRD0p4YJ0lFXqceuw9mBdkMR8zSWH6y31jWrmdY%2FTgCJDkOK5uHZXBooxHDd6tb8b3MbG5tEChocfK8IRnTaRG9dqC%2BkcDE3EQPPGPjVeLPly3QfOG8wEkRcnIA85rvN%2B%2FCW%2Bm8LgdwdEpPVCwSYsMf6HAnrvl61GwZS1ZntiAqIxkgGGmeliVaxUeXbmkfJBtSkRWIwp%2F0&X-Amz-Signature=b8862ada4cca68a5996a984d49104e278e4527111aa61c17ebed2a72b0abebcb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666WY7T7H%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4%2B0%2B9LemfzWXtbnTMDWCJDtnNmKwrCblMCsedChiitAiBS4pFyo3rAXTgC%2BD471ngJnlR3q5FTZtx9U4fBxLJP9SqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtJUt19zBCx3VW5iMKtwDRv7GDGAv2t%2BQGxZhysczcW6asN4E9jh5UxoB%2FIfUGAh8xX8At1YTvWmAbw0R8FNUO9Twx2dWcrt3k3HyZOruMTo6%2BKjBhr3T%2BnRK7a5vAzLrLUbWBgyIvfGMGQV0BlL4SAXvsi8zWzbSyslpqncDJH9FHeheBG2%2ByB5Z2vKD3tmkcVBtfySaBQ3hysP7lV5g4BSqLnE223g%2FfE7hNz5HGg1B79dMVik8ze8gW%2BVxKpn0bdJ2Z2pF7Zy5cnlN2RR9JUgtLOtcH%2FaxWShCiYaDENE40Lk477UzGhbNUcYSfVVWbhsCWfiiZNBcTvGKVShjOYAEOqg6yGtlglDrBD0MQc%2FQ2sFCi40ls%2BhKqwIgSEqaS2HUTysG8RCkAUPL75wAT2MACQ5NQkoAR3n5x39OHLbDVlXC0EsNMrBNpu8ekAG8NueeQqIzwjc1vY6FDiTyHqQOUHr3oW8E4CjsxTmHhHWHswpOWe2%2BZ3CEvbUZneDCF7lanqM1HcAp8BtaLEwbnz9DFIR9gqTJxqebA3EdPxfMBcjH5S37sBJUvHh2Icl2hQE0Euj8BAWvX3JcqzJ9Uh6EsqhLTDH03%2FF%2FKaqt74v5bJcoVoBy0wBJxZLby8Jbush9vX5rpLbigIAwi5fuvAY6pgHBn6uazqtVRvOPfg%2F6%2BXRD0p4YJ0lFXqceuw9mBdkMR8zSWH6y31jWrmdY%2FTgCJDkOK5uHZXBooxHDd6tb8b3MbG5tEChocfK8IRnTaRG9dqC%2BkcDE3EQPPGPjVeLPly3QfOG8wEkRcnIA85rvN%2B%2FCW%2Bm8LgdwdEpPVCwSYsMf6HAnrvl61GwZS1ZntiAqIxkgGGmeliVaxUeXbmkfJBtSkRWIwp%2F0&X-Amz-Signature=f30d363020329e69efcd65ed4c0a4fbc87a018440e7e1fa9838245125863e76c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666WY7T7H%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4%2B0%2B9LemfzWXtbnTMDWCJDtnNmKwrCblMCsedChiitAiBS4pFyo3rAXTgC%2BD471ngJnlR3q5FTZtx9U4fBxLJP9SqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtJUt19zBCx3VW5iMKtwDRv7GDGAv2t%2BQGxZhysczcW6asN4E9jh5UxoB%2FIfUGAh8xX8At1YTvWmAbw0R8FNUO9Twx2dWcrt3k3HyZOruMTo6%2BKjBhr3T%2BnRK7a5vAzLrLUbWBgyIvfGMGQV0BlL4SAXvsi8zWzbSyslpqncDJH9FHeheBG2%2ByB5Z2vKD3tmkcVBtfySaBQ3hysP7lV5g4BSqLnE223g%2FfE7hNz5HGg1B79dMVik8ze8gW%2BVxKpn0bdJ2Z2pF7Zy5cnlN2RR9JUgtLOtcH%2FaxWShCiYaDENE40Lk477UzGhbNUcYSfVVWbhsCWfiiZNBcTvGKVShjOYAEOqg6yGtlglDrBD0MQc%2FQ2sFCi40ls%2BhKqwIgSEqaS2HUTysG8RCkAUPL75wAT2MACQ5NQkoAR3n5x39OHLbDVlXC0EsNMrBNpu8ekAG8NueeQqIzwjc1vY6FDiTyHqQOUHr3oW8E4CjsxTmHhHWHswpOWe2%2BZ3CEvbUZneDCF7lanqM1HcAp8BtaLEwbnz9DFIR9gqTJxqebA3EdPxfMBcjH5S37sBJUvHh2Icl2hQE0Euj8BAWvX3JcqzJ9Uh6EsqhLTDH03%2FF%2FKaqt74v5bJcoVoBy0wBJxZLby8Jbush9vX5rpLbigIAwi5fuvAY6pgHBn6uazqtVRvOPfg%2F6%2BXRD0p4YJ0lFXqceuw9mBdkMR8zSWH6y31jWrmdY%2FTgCJDkOK5uHZXBooxHDd6tb8b3MbG5tEChocfK8IRnTaRG9dqC%2BkcDE3EQPPGPjVeLPly3QfOG8wEkRcnIA85rvN%2B%2FCW%2Bm8LgdwdEpPVCwSYsMf6HAnrvl61GwZS1ZntiAqIxkgGGmeliVaxUeXbmkfJBtSkRWIwp%2F0&X-Amz-Signature=487bc15ae2e3d134c060b81306cf59ebe12fba41c0bdde0c87fe6e40d1fc32ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666WY7T7H%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4%2B0%2B9LemfzWXtbnTMDWCJDtnNmKwrCblMCsedChiitAiBS4pFyo3rAXTgC%2BD471ngJnlR3q5FTZtx9U4fBxLJP9SqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtJUt19zBCx3VW5iMKtwDRv7GDGAv2t%2BQGxZhysczcW6asN4E9jh5UxoB%2FIfUGAh8xX8At1YTvWmAbw0R8FNUO9Twx2dWcrt3k3HyZOruMTo6%2BKjBhr3T%2BnRK7a5vAzLrLUbWBgyIvfGMGQV0BlL4SAXvsi8zWzbSyslpqncDJH9FHeheBG2%2ByB5Z2vKD3tmkcVBtfySaBQ3hysP7lV5g4BSqLnE223g%2FfE7hNz5HGg1B79dMVik8ze8gW%2BVxKpn0bdJ2Z2pF7Zy5cnlN2RR9JUgtLOtcH%2FaxWShCiYaDENE40Lk477UzGhbNUcYSfVVWbhsCWfiiZNBcTvGKVShjOYAEOqg6yGtlglDrBD0MQc%2FQ2sFCi40ls%2BhKqwIgSEqaS2HUTysG8RCkAUPL75wAT2MACQ5NQkoAR3n5x39OHLbDVlXC0EsNMrBNpu8ekAG8NueeQqIzwjc1vY6FDiTyHqQOUHr3oW8E4CjsxTmHhHWHswpOWe2%2BZ3CEvbUZneDCF7lanqM1HcAp8BtaLEwbnz9DFIR9gqTJxqebA3EdPxfMBcjH5S37sBJUvHh2Icl2hQE0Euj8BAWvX3JcqzJ9Uh6EsqhLTDH03%2FF%2FKaqt74v5bJcoVoBy0wBJxZLby8Jbush9vX5rpLbigIAwi5fuvAY6pgHBn6uazqtVRvOPfg%2F6%2BXRD0p4YJ0lFXqceuw9mBdkMR8zSWH6y31jWrmdY%2FTgCJDkOK5uHZXBooxHDd6tb8b3MbG5tEChocfK8IRnTaRG9dqC%2BkcDE3EQPPGPjVeLPly3QfOG8wEkRcnIA85rvN%2B%2FCW%2Bm8LgdwdEpPVCwSYsMf6HAnrvl61GwZS1ZntiAqIxkgGGmeliVaxUeXbmkfJBtSkRWIwp%2F0&X-Amz-Signature=61021981e160f2b7269998ab1e0446fd34f0057010b1f98d4ba7d8767984e934&X-Amz-SignedHeaders=host&x-id=GetObject)
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


