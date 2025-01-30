

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SITLIRNA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH6mLA5CmNt2Pyo5EVi%2BpsMPnyidFqOy84XIXnjkJnejAiAXeT6X2Edad6hRpww1nhqYR6oi0G8gK2GK%2BPrq0P1ovSqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG6m3DrJJUEIrYPuUKtwDNdOcv5Muh5q2tHzGV%2BD5iueFqJwzQJzsqmLxbtyuPh%2BoovMi2NiB0OgfLY6q1NqIxNRC3IMgp7qqR8LuPwdxKsVCoLb8MuwkU1WKH%2FM2f0e4nxYjgUqoc3cWFaTzSE0kgf66F5kJEnoDgRNcv6n9SM6fR4w7q8Gek1MCXx%2FnqiKCzYF48tYT8PMoY7zbBYkJjrXflipfgN8yfieNF8e74tC07z5L65qGyp5WlZ8JneTuBkLgcl5NBEdjGHzkHn5JrXo%2BlprGdhXV6bR%2BNvBxqpZ5ZMvc0wE3oKHpumJlSQQsd%2BBlvP%2BsEtv4EcGGyE82dbIeSgVHj6lx6QCMbNwACmEnZWRyy0xlpAj4W80kLE7YJ8SuB%2Fu9J%2B%2BpnNbgYtOBV8Z%2Bu3DeV2qqAC43Msnf9biCsozj%2BmS%2F4TYpcbiO2mb9pGhtn68WGvKVx6dTPgyV8zqw8pA5GR9ahIb8aoKY1%2BMIVWNIlwi24qbmUp3ldXqvFy0g%2FPfk1%2FxCwhwbDlxjj%2BLlrTX88HlT0IVWHba9s9ydoH5IJiY8o5UPaugRC%2FetnNG6PHBlbHS5KOYHOXJTak5mhAQ2tMujSJiBZ5JpAnxE3eAznZwM8v%2BlVDGEroK4tFY9IXjoEOHQXOIwzuHvvAY6pgEQ3i5MDDYUeZlmkeUa9l3XXaJSakfYzdJ%2FgZ2a%2F%2BSqcpiGBqhutND%2BDcw5S0Ec%2BhE3cwEI0x0V%2B6KeGYkuWMK%2F5xzyp925DMRcd5co6LiF8o2zdWfCKVfwcUmwZzkPN7vmsCi4cHOMeaAkAPv3pCDmuD5mmnoD3prhTsDqfSNfKKevcfGU%2FfmDL0R3VO4k2rtGfLvplG8BAESQ6WXHiTBetx0UM7hT&X-Amz-Signature=e8750b61a24407f01f3f695eab74251b9ea9557716703237633fda344bfe917c&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDLBJJJ4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6a86haIbcmi29r6Ppm97PkFKv4EhXnZjCCpprBEcMdQIgNvV2Rlk2J5ODNoAgH21Rc1Tx8jaP2qPZ2m7Mr1bHY%2FMqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAr5S25w2ULRthGHaircA8xTQQKyJBiiVjGJq%2BlWtUFdSLKLyqcm5U25%2F7uitgQb9OWA6I90CDH%2ByT9gMfaCH0BGcccCRO3l4%2BaC14u30Ic%2BrvTDyCRgTxEfjvGHvTxAq%2B3C%2FrwObNDpDmkvSv3SxR794ZqG%2FUgyB3JsEtuEn7FeLeHIUeiYaHyeF%2FVHmL9KeHSUz%2FqcKgwfT1KntvOaHPP05qnI1PMCv09yf77M8nSTuDklmeBo1mGSmPYtJedpw41rpHwhmSvKG%2BD4a3BEayLJ8XMfPAq87MIGsyqgL77Xpmr6kvnHmWb1ssHB3y5SUcH8y0PD1Db979qcwyuvL%2FbFA6XPJmyizatEjRBJz9tlO2JIrnXi5jMLAyJRwFJeldrTEC95IODWUP%2BV0QmOetAdMXJvjvbiv298VWxO89tFwCapBPm7edxeb%2B0pmrTYBcv5lAMXue3ET8JGYw8t9%2BB0y3UtPqERkXCw9XFnQtM9lbfBJHV0BHty0vunISYdKuIB3JjXdI7OArZMXovN1s2W%2BEwVMI0g%2FBY0NUFidKYTZcBqg0kjFYKRsy9P0HP%2BtDq1MlspIBwwNnyZ9uO5%2BUGouXHdAAfBZX6pBhm0XyXoo009I71i7tVeRzbbkGDYRFEApX6hOr3gbn7tMIvh77wGOqUBRLZzvoKLBWIbATpFS9TnPtH9FGhz9V9THK9ZlotkRHNt9Ne3sc8EkXsLeOvPavoDVqYaftkoZ1azFeROsAr1dR4195UYWcuPYiK%2B%2FyRV58MdrkUK%2FR9LB%2B1%2BSue7u9uSzohNSphGNzjU5Jm9a4h3v2vRJf7EzpPzwjMOj766NRKd%2F%2Fx85Al1k7al8PE%2B%2Bb2nV4Jm9GGgk17STRcLYEzso05c9i1K&X-Amz-Signature=fa33546c12b0a607b054c1b9e33a568e38f4e73f893d4277b9b724ed84afdd31&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDLBJJJ4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6a86haIbcmi29r6Ppm97PkFKv4EhXnZjCCpprBEcMdQIgNvV2Rlk2J5ODNoAgH21Rc1Tx8jaP2qPZ2m7Mr1bHY%2FMqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAr5S25w2ULRthGHaircA8xTQQKyJBiiVjGJq%2BlWtUFdSLKLyqcm5U25%2F7uitgQb9OWA6I90CDH%2ByT9gMfaCH0BGcccCRO3l4%2BaC14u30Ic%2BrvTDyCRgTxEfjvGHvTxAq%2B3C%2FrwObNDpDmkvSv3SxR794ZqG%2FUgyB3JsEtuEn7FeLeHIUeiYaHyeF%2FVHmL9KeHSUz%2FqcKgwfT1KntvOaHPP05qnI1PMCv09yf77M8nSTuDklmeBo1mGSmPYtJedpw41rpHwhmSvKG%2BD4a3BEayLJ8XMfPAq87MIGsyqgL77Xpmr6kvnHmWb1ssHB3y5SUcH8y0PD1Db979qcwyuvL%2FbFA6XPJmyizatEjRBJz9tlO2JIrnXi5jMLAyJRwFJeldrTEC95IODWUP%2BV0QmOetAdMXJvjvbiv298VWxO89tFwCapBPm7edxeb%2B0pmrTYBcv5lAMXue3ET8JGYw8t9%2BB0y3UtPqERkXCw9XFnQtM9lbfBJHV0BHty0vunISYdKuIB3JjXdI7OArZMXovN1s2W%2BEwVMI0g%2FBY0NUFidKYTZcBqg0kjFYKRsy9P0HP%2BtDq1MlspIBwwNnyZ9uO5%2BUGouXHdAAfBZX6pBhm0XyXoo009I71i7tVeRzbbkGDYRFEApX6hOr3gbn7tMIvh77wGOqUBRLZzvoKLBWIbATpFS9TnPtH9FGhz9V9THK9ZlotkRHNt9Ne3sc8EkXsLeOvPavoDVqYaftkoZ1azFeROsAr1dR4195UYWcuPYiK%2B%2FyRV58MdrkUK%2FR9LB%2B1%2BSue7u9uSzohNSphGNzjU5Jm9a4h3v2vRJf7EzpPzwjMOj766NRKd%2F%2Fx85Al1k7al8PE%2B%2Bb2nV4Jm9GGgk17STRcLYEzso05c9i1K&X-Amz-Signature=ef5b7620aab25bf55e926bb4810f8b7d857458fbf9fc36641715f88736c4e292&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDLBJJJ4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6a86haIbcmi29r6Ppm97PkFKv4EhXnZjCCpprBEcMdQIgNvV2Rlk2J5ODNoAgH21Rc1Tx8jaP2qPZ2m7Mr1bHY%2FMqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAr5S25w2ULRthGHaircA8xTQQKyJBiiVjGJq%2BlWtUFdSLKLyqcm5U25%2F7uitgQb9OWA6I90CDH%2ByT9gMfaCH0BGcccCRO3l4%2BaC14u30Ic%2BrvTDyCRgTxEfjvGHvTxAq%2B3C%2FrwObNDpDmkvSv3SxR794ZqG%2FUgyB3JsEtuEn7FeLeHIUeiYaHyeF%2FVHmL9KeHSUz%2FqcKgwfT1KntvOaHPP05qnI1PMCv09yf77M8nSTuDklmeBo1mGSmPYtJedpw41rpHwhmSvKG%2BD4a3BEayLJ8XMfPAq87MIGsyqgL77Xpmr6kvnHmWb1ssHB3y5SUcH8y0PD1Db979qcwyuvL%2FbFA6XPJmyizatEjRBJz9tlO2JIrnXi5jMLAyJRwFJeldrTEC95IODWUP%2BV0QmOetAdMXJvjvbiv298VWxO89tFwCapBPm7edxeb%2B0pmrTYBcv5lAMXue3ET8JGYw8t9%2BB0y3UtPqERkXCw9XFnQtM9lbfBJHV0BHty0vunISYdKuIB3JjXdI7OArZMXovN1s2W%2BEwVMI0g%2FBY0NUFidKYTZcBqg0kjFYKRsy9P0HP%2BtDq1MlspIBwwNnyZ9uO5%2BUGouXHdAAfBZX6pBhm0XyXoo009I71i7tVeRzbbkGDYRFEApX6hOr3gbn7tMIvh77wGOqUBRLZzvoKLBWIbATpFS9TnPtH9FGhz9V9THK9ZlotkRHNt9Ne3sc8EkXsLeOvPavoDVqYaftkoZ1azFeROsAr1dR4195UYWcuPYiK%2B%2FyRV58MdrkUK%2FR9LB%2B1%2BSue7u9uSzohNSphGNzjU5Jm9a4h3v2vRJf7EzpPzwjMOj766NRKd%2F%2Fx85Al1k7al8PE%2B%2Bb2nV4Jm9GGgk17STRcLYEzso05c9i1K&X-Amz-Signature=c3335f8a112961a3194b1318f87417c1314cb481550110fb24c5e428031815ed&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDLBJJJ4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6a86haIbcmi29r6Ppm97PkFKv4EhXnZjCCpprBEcMdQIgNvV2Rlk2J5ODNoAgH21Rc1Tx8jaP2qPZ2m7Mr1bHY%2FMqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAr5S25w2ULRthGHaircA8xTQQKyJBiiVjGJq%2BlWtUFdSLKLyqcm5U25%2F7uitgQb9OWA6I90CDH%2ByT9gMfaCH0BGcccCRO3l4%2BaC14u30Ic%2BrvTDyCRgTxEfjvGHvTxAq%2B3C%2FrwObNDpDmkvSv3SxR794ZqG%2FUgyB3JsEtuEn7FeLeHIUeiYaHyeF%2FVHmL9KeHSUz%2FqcKgwfT1KntvOaHPP05qnI1PMCv09yf77M8nSTuDklmeBo1mGSmPYtJedpw41rpHwhmSvKG%2BD4a3BEayLJ8XMfPAq87MIGsyqgL77Xpmr6kvnHmWb1ssHB3y5SUcH8y0PD1Db979qcwyuvL%2FbFA6XPJmyizatEjRBJz9tlO2JIrnXi5jMLAyJRwFJeldrTEC95IODWUP%2BV0QmOetAdMXJvjvbiv298VWxO89tFwCapBPm7edxeb%2B0pmrTYBcv5lAMXue3ET8JGYw8t9%2BB0y3UtPqERkXCw9XFnQtM9lbfBJHV0BHty0vunISYdKuIB3JjXdI7OArZMXovN1s2W%2BEwVMI0g%2FBY0NUFidKYTZcBqg0kjFYKRsy9P0HP%2BtDq1MlspIBwwNnyZ9uO5%2BUGouXHdAAfBZX6pBhm0XyXoo009I71i7tVeRzbbkGDYRFEApX6hOr3gbn7tMIvh77wGOqUBRLZzvoKLBWIbATpFS9TnPtH9FGhz9V9THK9ZlotkRHNt9Ne3sc8EkXsLeOvPavoDVqYaftkoZ1azFeROsAr1dR4195UYWcuPYiK%2B%2FyRV58MdrkUK%2FR9LB%2B1%2BSue7u9uSzohNSphGNzjU5Jm9a4h3v2vRJf7EzpPzwjMOj766NRKd%2F%2Fx85Al1k7al8PE%2B%2Bb2nV4Jm9GGgk17STRcLYEzso05c9i1K&X-Amz-Signature=71a7432e66089119671da5df0bcd5d08dc7d980677f14b7b54d616a1476757cd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDLBJJJ4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6a86haIbcmi29r6Ppm97PkFKv4EhXnZjCCpprBEcMdQIgNvV2Rlk2J5ODNoAgH21Rc1Tx8jaP2qPZ2m7Mr1bHY%2FMqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAr5S25w2ULRthGHaircA8xTQQKyJBiiVjGJq%2BlWtUFdSLKLyqcm5U25%2F7uitgQb9OWA6I90CDH%2ByT9gMfaCH0BGcccCRO3l4%2BaC14u30Ic%2BrvTDyCRgTxEfjvGHvTxAq%2B3C%2FrwObNDpDmkvSv3SxR794ZqG%2FUgyB3JsEtuEn7FeLeHIUeiYaHyeF%2FVHmL9KeHSUz%2FqcKgwfT1KntvOaHPP05qnI1PMCv09yf77M8nSTuDklmeBo1mGSmPYtJedpw41rpHwhmSvKG%2BD4a3BEayLJ8XMfPAq87MIGsyqgL77Xpmr6kvnHmWb1ssHB3y5SUcH8y0PD1Db979qcwyuvL%2FbFA6XPJmyizatEjRBJz9tlO2JIrnXi5jMLAyJRwFJeldrTEC95IODWUP%2BV0QmOetAdMXJvjvbiv298VWxO89tFwCapBPm7edxeb%2B0pmrTYBcv5lAMXue3ET8JGYw8t9%2BB0y3UtPqERkXCw9XFnQtM9lbfBJHV0BHty0vunISYdKuIB3JjXdI7OArZMXovN1s2W%2BEwVMI0g%2FBY0NUFidKYTZcBqg0kjFYKRsy9P0HP%2BtDq1MlspIBwwNnyZ9uO5%2BUGouXHdAAfBZX6pBhm0XyXoo009I71i7tVeRzbbkGDYRFEApX6hOr3gbn7tMIvh77wGOqUBRLZzvoKLBWIbATpFS9TnPtH9FGhz9V9THK9ZlotkRHNt9Ne3sc8EkXsLeOvPavoDVqYaftkoZ1azFeROsAr1dR4195UYWcuPYiK%2B%2FyRV58MdrkUK%2FR9LB%2B1%2BSue7u9uSzohNSphGNzjU5Jm9a4h3v2vRJf7EzpPzwjMOj766NRKd%2F%2Fx85Al1k7al8PE%2B%2Bb2nV4Jm9GGgk17STRcLYEzso05c9i1K&X-Amz-Signature=f2e2adcfea75a7505311210bacd063de972521d7186bd758fbf5d9de92628594&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SITLIRNA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH6mLA5CmNt2Pyo5EVi%2BpsMPnyidFqOy84XIXnjkJnejAiAXeT6X2Edad6hRpww1nhqYR6oi0G8gK2GK%2BPrq0P1ovSqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG6m3DrJJUEIrYPuUKtwDNdOcv5Muh5q2tHzGV%2BD5iueFqJwzQJzsqmLxbtyuPh%2BoovMi2NiB0OgfLY6q1NqIxNRC3IMgp7qqR8LuPwdxKsVCoLb8MuwkU1WKH%2FM2f0e4nxYjgUqoc3cWFaTzSE0kgf66F5kJEnoDgRNcv6n9SM6fR4w7q8Gek1MCXx%2FnqiKCzYF48tYT8PMoY7zbBYkJjrXflipfgN8yfieNF8e74tC07z5L65qGyp5WlZ8JneTuBkLgcl5NBEdjGHzkHn5JrXo%2BlprGdhXV6bR%2BNvBxqpZ5ZMvc0wE3oKHpumJlSQQsd%2BBlvP%2BsEtv4EcGGyE82dbIeSgVHj6lx6QCMbNwACmEnZWRyy0xlpAj4W80kLE7YJ8SuB%2Fu9J%2B%2BpnNbgYtOBV8Z%2Bu3DeV2qqAC43Msnf9biCsozj%2BmS%2F4TYpcbiO2mb9pGhtn68WGvKVx6dTPgyV8zqw8pA5GR9ahIb8aoKY1%2BMIVWNIlwi24qbmUp3ldXqvFy0g%2FPfk1%2FxCwhwbDlxjj%2BLlrTX88HlT0IVWHba9s9ydoH5IJiY8o5UPaugRC%2FetnNG6PHBlbHS5KOYHOXJTak5mhAQ2tMujSJiBZ5JpAnxE3eAznZwM8v%2BlVDGEroK4tFY9IXjoEOHQXOIwzuHvvAY6pgEQ3i5MDDYUeZlmkeUa9l3XXaJSakfYzdJ%2FgZ2a%2F%2BSqcpiGBqhutND%2BDcw5S0Ec%2BhE3cwEI0x0V%2B6KeGYkuWMK%2F5xzyp925DMRcd5co6LiF8o2zdWfCKVfwcUmwZzkPN7vmsCi4cHOMeaAkAPv3pCDmuD5mmnoD3prhTsDqfSNfKKevcfGU%2FfmDL0R3VO4k2rtGfLvplG8BAESQ6WXHiTBetx0UM7hT&X-Amz-Signature=0f3b917061e06d877b9224cfca62a37bb897aad4abe76cbdfa253a3b7633a53f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SITLIRNA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH6mLA5CmNt2Pyo5EVi%2BpsMPnyidFqOy84XIXnjkJnejAiAXeT6X2Edad6hRpww1nhqYR6oi0G8gK2GK%2BPrq0P1ovSqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG6m3DrJJUEIrYPuUKtwDNdOcv5Muh5q2tHzGV%2BD5iueFqJwzQJzsqmLxbtyuPh%2BoovMi2NiB0OgfLY6q1NqIxNRC3IMgp7qqR8LuPwdxKsVCoLb8MuwkU1WKH%2FM2f0e4nxYjgUqoc3cWFaTzSE0kgf66F5kJEnoDgRNcv6n9SM6fR4w7q8Gek1MCXx%2FnqiKCzYF48tYT8PMoY7zbBYkJjrXflipfgN8yfieNF8e74tC07z5L65qGyp5WlZ8JneTuBkLgcl5NBEdjGHzkHn5JrXo%2BlprGdhXV6bR%2BNvBxqpZ5ZMvc0wE3oKHpumJlSQQsd%2BBlvP%2BsEtv4EcGGyE82dbIeSgVHj6lx6QCMbNwACmEnZWRyy0xlpAj4W80kLE7YJ8SuB%2Fu9J%2B%2BpnNbgYtOBV8Z%2Bu3DeV2qqAC43Msnf9biCsozj%2BmS%2F4TYpcbiO2mb9pGhtn68WGvKVx6dTPgyV8zqw8pA5GR9ahIb8aoKY1%2BMIVWNIlwi24qbmUp3ldXqvFy0g%2FPfk1%2FxCwhwbDlxjj%2BLlrTX88HlT0IVWHba9s9ydoH5IJiY8o5UPaugRC%2FetnNG6PHBlbHS5KOYHOXJTak5mhAQ2tMujSJiBZ5JpAnxE3eAznZwM8v%2BlVDGEroK4tFY9IXjoEOHQXOIwzuHvvAY6pgEQ3i5MDDYUeZlmkeUa9l3XXaJSakfYzdJ%2FgZ2a%2F%2BSqcpiGBqhutND%2BDcw5S0Ec%2BhE3cwEI0x0V%2B6KeGYkuWMK%2F5xzyp925DMRcd5co6LiF8o2zdWfCKVfwcUmwZzkPN7vmsCi4cHOMeaAkAPv3pCDmuD5mmnoD3prhTsDqfSNfKKevcfGU%2FfmDL0R3VO4k2rtGfLvplG8BAESQ6WXHiTBetx0UM7hT&X-Amz-Signature=8ed1bbc1cab638af4ecccef0151b0c5c4796d4d134b6fc9763ddce508273d66f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SITLIRNA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH6mLA5CmNt2Pyo5EVi%2BpsMPnyidFqOy84XIXnjkJnejAiAXeT6X2Edad6hRpww1nhqYR6oi0G8gK2GK%2BPrq0P1ovSqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG6m3DrJJUEIrYPuUKtwDNdOcv5Muh5q2tHzGV%2BD5iueFqJwzQJzsqmLxbtyuPh%2BoovMi2NiB0OgfLY6q1NqIxNRC3IMgp7qqR8LuPwdxKsVCoLb8MuwkU1WKH%2FM2f0e4nxYjgUqoc3cWFaTzSE0kgf66F5kJEnoDgRNcv6n9SM6fR4w7q8Gek1MCXx%2FnqiKCzYF48tYT8PMoY7zbBYkJjrXflipfgN8yfieNF8e74tC07z5L65qGyp5WlZ8JneTuBkLgcl5NBEdjGHzkHn5JrXo%2BlprGdhXV6bR%2BNvBxqpZ5ZMvc0wE3oKHpumJlSQQsd%2BBlvP%2BsEtv4EcGGyE82dbIeSgVHj6lx6QCMbNwACmEnZWRyy0xlpAj4W80kLE7YJ8SuB%2Fu9J%2B%2BpnNbgYtOBV8Z%2Bu3DeV2qqAC43Msnf9biCsozj%2BmS%2F4TYpcbiO2mb9pGhtn68WGvKVx6dTPgyV8zqw8pA5GR9ahIb8aoKY1%2BMIVWNIlwi24qbmUp3ldXqvFy0g%2FPfk1%2FxCwhwbDlxjj%2BLlrTX88HlT0IVWHba9s9ydoH5IJiY8o5UPaugRC%2FetnNG6PHBlbHS5KOYHOXJTak5mhAQ2tMujSJiBZ5JpAnxE3eAznZwM8v%2BlVDGEroK4tFY9IXjoEOHQXOIwzuHvvAY6pgEQ3i5MDDYUeZlmkeUa9l3XXaJSakfYzdJ%2FgZ2a%2F%2BSqcpiGBqhutND%2BDcw5S0Ec%2BhE3cwEI0x0V%2B6KeGYkuWMK%2F5xzyp925DMRcd5co6LiF8o2zdWfCKVfwcUmwZzkPN7vmsCi4cHOMeaAkAPv3pCDmuD5mmnoD3prhTsDqfSNfKKevcfGU%2FfmDL0R3VO4k2rtGfLvplG8BAESQ6WXHiTBetx0UM7hT&X-Amz-Signature=c3131c40a23d5b6a08b16cfaeb550fdace4ed9d9212f8a1da4a36f8c24b29e3b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SITLIRNA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH6mLA5CmNt2Pyo5EVi%2BpsMPnyidFqOy84XIXnjkJnejAiAXeT6X2Edad6hRpww1nhqYR6oi0G8gK2GK%2BPrq0P1ovSqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG6m3DrJJUEIrYPuUKtwDNdOcv5Muh5q2tHzGV%2BD5iueFqJwzQJzsqmLxbtyuPh%2BoovMi2NiB0OgfLY6q1NqIxNRC3IMgp7qqR8LuPwdxKsVCoLb8MuwkU1WKH%2FM2f0e4nxYjgUqoc3cWFaTzSE0kgf66F5kJEnoDgRNcv6n9SM6fR4w7q8Gek1MCXx%2FnqiKCzYF48tYT8PMoY7zbBYkJjrXflipfgN8yfieNF8e74tC07z5L65qGyp5WlZ8JneTuBkLgcl5NBEdjGHzkHn5JrXo%2BlprGdhXV6bR%2BNvBxqpZ5ZMvc0wE3oKHpumJlSQQsd%2BBlvP%2BsEtv4EcGGyE82dbIeSgVHj6lx6QCMbNwACmEnZWRyy0xlpAj4W80kLE7YJ8SuB%2Fu9J%2B%2BpnNbgYtOBV8Z%2Bu3DeV2qqAC43Msnf9biCsozj%2BmS%2F4TYpcbiO2mb9pGhtn68WGvKVx6dTPgyV8zqw8pA5GR9ahIb8aoKY1%2BMIVWNIlwi24qbmUp3ldXqvFy0g%2FPfk1%2FxCwhwbDlxjj%2BLlrTX88HlT0IVWHba9s9ydoH5IJiY8o5UPaugRC%2FetnNG6PHBlbHS5KOYHOXJTak5mhAQ2tMujSJiBZ5JpAnxE3eAznZwM8v%2BlVDGEroK4tFY9IXjoEOHQXOIwzuHvvAY6pgEQ3i5MDDYUeZlmkeUa9l3XXaJSakfYzdJ%2FgZ2a%2F%2BSqcpiGBqhutND%2BDcw5S0Ec%2BhE3cwEI0x0V%2B6KeGYkuWMK%2F5xzyp925DMRcd5co6LiF8o2zdWfCKVfwcUmwZzkPN7vmsCi4cHOMeaAkAPv3pCDmuD5mmnoD3prhTsDqfSNfKKevcfGU%2FfmDL0R3VO4k2rtGfLvplG8BAESQ6WXHiTBetx0UM7hT&X-Amz-Signature=77c4116f5ea5fc3077c2d6c93d276b1f116e10cab62cd4588d2f7292371aa924&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SITLIRNA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH6mLA5CmNt2Pyo5EVi%2BpsMPnyidFqOy84XIXnjkJnejAiAXeT6X2Edad6hRpww1nhqYR6oi0G8gK2GK%2BPrq0P1ovSqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG6m3DrJJUEIrYPuUKtwDNdOcv5Muh5q2tHzGV%2BD5iueFqJwzQJzsqmLxbtyuPh%2BoovMi2NiB0OgfLY6q1NqIxNRC3IMgp7qqR8LuPwdxKsVCoLb8MuwkU1WKH%2FM2f0e4nxYjgUqoc3cWFaTzSE0kgf66F5kJEnoDgRNcv6n9SM6fR4w7q8Gek1MCXx%2FnqiKCzYF48tYT8PMoY7zbBYkJjrXflipfgN8yfieNF8e74tC07z5L65qGyp5WlZ8JneTuBkLgcl5NBEdjGHzkHn5JrXo%2BlprGdhXV6bR%2BNvBxqpZ5ZMvc0wE3oKHpumJlSQQsd%2BBlvP%2BsEtv4EcGGyE82dbIeSgVHj6lx6QCMbNwACmEnZWRyy0xlpAj4W80kLE7YJ8SuB%2Fu9J%2B%2BpnNbgYtOBV8Z%2Bu3DeV2qqAC43Msnf9biCsozj%2BmS%2F4TYpcbiO2mb9pGhtn68WGvKVx6dTPgyV8zqw8pA5GR9ahIb8aoKY1%2BMIVWNIlwi24qbmUp3ldXqvFy0g%2FPfk1%2FxCwhwbDlxjj%2BLlrTX88HlT0IVWHba9s9ydoH5IJiY8o5UPaugRC%2FetnNG6PHBlbHS5KOYHOXJTak5mhAQ2tMujSJiBZ5JpAnxE3eAznZwM8v%2BlVDGEroK4tFY9IXjoEOHQXOIwzuHvvAY6pgEQ3i5MDDYUeZlmkeUa9l3XXaJSakfYzdJ%2FgZ2a%2F%2BSqcpiGBqhutND%2BDcw5S0Ec%2BhE3cwEI0x0V%2B6KeGYkuWMK%2F5xzyp925DMRcd5co6LiF8o2zdWfCKVfwcUmwZzkPN7vmsCi4cHOMeaAkAPv3pCDmuD5mmnoD3prhTsDqfSNfKKevcfGU%2FfmDL0R3VO4k2rtGfLvplG8BAESQ6WXHiTBetx0UM7hT&X-Amz-Signature=b9b50e0509230743cb2d9a8d8f7aa9e1add771089b69f124c7cd65da879d4782&X-Amz-SignedHeaders=host&x-id=GetObject)
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


