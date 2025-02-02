

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665OSLTK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9jtkSKMJSwDYnBGK%2FrrTNWMLAv3ePHZCLYXM80HKLHgIgZypn5VYSd%2BZT9TnveygPhDwttfjRVKyX1oi1siv0yw0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFSAc%2F%2FD6YcZ%2BNB2CrcAzooz3Q8WFAbBGPC7InzpCFhkAXdd2deilE4W5QHQtaWUL5U9Dhq17cL8AN3lDSAtj%2Bn3DF4X4cEIiTI0PWJlC5yhRHbsBf77k3TsUH5hw5TbKfHwzNZDvRHKC1LaEXpRM%2BjbgYBX%2FLT6np1dCXlPB35bSXj34EDJhcorqP%2FkxjiHLsZCaHIM7DOI0ucPhD9SE9oxZEys11gwpEsAjayGORX1JKX7Yq0EOMfNMFU1NUkVUjWistO0qmr6rNgijR%2BjQmUSvGriOB4NZBtr1fjbKT8314P0v6mYwst5QHMDEl0oXHB3BLl4CZsS5BlDMdzoiaVwD%2FN3y9FCPLv5SEB3bZEXDzwDU5xfkOA%2Bocf3rCQsGTURKeOBxHIN5PMyq2CNju6HpLLl%2BzQbC2NSmzU5z5pgFGDm9RUkZ79r%2BX7w05VaNJIstH73lWiyBWOY27uUVlQQLrhLCCRWEteVmYdrJibwsX53hIcQs0g2EwGElEznvqwBbgfhz7k9l6n48uWcAGjgDKEcZb9VEtdxBfvKaldIAN2JBGdyr24J6QV%2FPSc%2FSlRgpwfq4Vb2DJpF8NNeufOhEZ%2Bd4G4kXq4X7k6Zwo7NfFMd%2FfBJlB4Cd%2BcrZ2jgQz5yow38VmAHLh%2BMKSc%2FLwGOqUBRUUCV1HYAavEOWO59WaM2Psjzfrbd38XT5%2BftFckV1tcA%2BjQp2lnbSys6MEiXW6B4Gme1wje9%2FHlCIx1pm%2FTpBnVN4bJJlDyEOnOwKdOpuCll1BkdrB7BfG0cv8NVIt8QdUIGZV1J0zDzO1BG01n08nneUSQ5iLFiybj9baAyorpBzAStwBfN2pElcY6Zknz3liDQDWB%2BM3KH8UZG67g2rnQuQR6&X-Amz-Signature=cf4e1b6df7ee528978262a811eca346c071cb156b8fbb56090bd986cb5e4846f&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7YD7EUO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJwmwu%2BVGw5p%2BQWidcPD99WAwtwQNtyeWLtBiz%2BBpDQQIhAPbfqXuooxaSVCdYhVl5xLhKSU9824bGo8iiL1xmnkMJKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwm8uCKbgzT0lHj%2FTQq3ANEdcKnGce2eoS%2BVE0vPcUc5tF2gRDAO9oguETs5TFAlhe3J85cF84y1uwx6tnywB1a5ygVrKImffNBm8Xplzleond8eVtsxTTuKOFL4sBXpdrW6yY%2BfktkQz0jH9GwNe5ss8eit4Rk5Am8861rWWUCnxT2Ty1eW7NkPSj%2F5IcKzOBUZVrt4yw69skMz5x59lwYvY987F53Xdm%2B%2BC%2BDM3RHhWoooPW7P4SvCsvfe%2FioWXoPzVX2Ffq5eXJ6WMuG%2FKHhauH8FzxkR80nr2KZgpJLONiP8UwxbnQe%2B9igzhBl%2BJksipYilm4BsjGCz5S2A72iGaOQQXa%2FsmxpRDbUQq60NzkEf%2BHb%2BmcJfV6iCiL3sbsBKBuORK2XYyjzF8zdcc3XhaNOzOmZOLzAWbAUytDG08fY9QTCd%2F7DmJlOL8KbuqS4O07SdlJyy6v9woVeB10JiEqqgIuCOOK0bc17yAof8jvODg%2BkNysGNjQKQKOO6miC98DkYGHJBe1a0W1prD2lU3AS0K2PMb0k8bXRp0EKB5HELE75kEFRAEh7v5FINIz8q1Vv%2BlHTp8UuD852d92dYxtwelkix7LgClpOnj8r39PhG7sq62KznExeBvBBOL5VgsQGT6oV2aFGoTD6m%2Fy8BjqkAXAHNbnMxTi8k62NAW0dHJBtQK4aRKqvrOhkgn4OBYU%2BWIHLcExgCA6oZHd8QGsSgsQSaA56bwkHtM2mv4FKS4xLj3lvR9btMrHHj5NkZwXnXH8JKkgw6K9eNQ%2BUgc6oLmO%2FVmKlTjdZgcKYPIfk7Gt5VaQr84w420ouHhD8CT%2F2%2FHitMJwVAioPxRz%2Fs69fbKaevUuSb%2F4JObrfs3Fpvo8BUzhH&X-Amz-Signature=1ebcbc163b468ba83db2f6129cedead52ec513abb1ff50305e2589e50d500a03&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7YD7EUO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJwmwu%2BVGw5p%2BQWidcPD99WAwtwQNtyeWLtBiz%2BBpDQQIhAPbfqXuooxaSVCdYhVl5xLhKSU9824bGo8iiL1xmnkMJKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwm8uCKbgzT0lHj%2FTQq3ANEdcKnGce2eoS%2BVE0vPcUc5tF2gRDAO9oguETs5TFAlhe3J85cF84y1uwx6tnywB1a5ygVrKImffNBm8Xplzleond8eVtsxTTuKOFL4sBXpdrW6yY%2BfktkQz0jH9GwNe5ss8eit4Rk5Am8861rWWUCnxT2Ty1eW7NkPSj%2F5IcKzOBUZVrt4yw69skMz5x59lwYvY987F53Xdm%2B%2BC%2BDM3RHhWoooPW7P4SvCsvfe%2FioWXoPzVX2Ffq5eXJ6WMuG%2FKHhauH8FzxkR80nr2KZgpJLONiP8UwxbnQe%2B9igzhBl%2BJksipYilm4BsjGCz5S2A72iGaOQQXa%2FsmxpRDbUQq60NzkEf%2BHb%2BmcJfV6iCiL3sbsBKBuORK2XYyjzF8zdcc3XhaNOzOmZOLzAWbAUytDG08fY9QTCd%2F7DmJlOL8KbuqS4O07SdlJyy6v9woVeB10JiEqqgIuCOOK0bc17yAof8jvODg%2BkNysGNjQKQKOO6miC98DkYGHJBe1a0W1prD2lU3AS0K2PMb0k8bXRp0EKB5HELE75kEFRAEh7v5FINIz8q1Vv%2BlHTp8UuD852d92dYxtwelkix7LgClpOnj8r39PhG7sq62KznExeBvBBOL5VgsQGT6oV2aFGoTD6m%2Fy8BjqkAXAHNbnMxTi8k62NAW0dHJBtQK4aRKqvrOhkgn4OBYU%2BWIHLcExgCA6oZHd8QGsSgsQSaA56bwkHtM2mv4FKS4xLj3lvR9btMrHHj5NkZwXnXH8JKkgw6K9eNQ%2BUgc6oLmO%2FVmKlTjdZgcKYPIfk7Gt5VaQr84w420ouHhD8CT%2F2%2FHitMJwVAioPxRz%2Fs69fbKaevUuSb%2F4JObrfs3Fpvo8BUzhH&X-Amz-Signature=6dc5b600ccae0cc55031927c512dd5b454a9b834218ffc20ba6cde6807225f54&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7YD7EUO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJwmwu%2BVGw5p%2BQWidcPD99WAwtwQNtyeWLtBiz%2BBpDQQIhAPbfqXuooxaSVCdYhVl5xLhKSU9824bGo8iiL1xmnkMJKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwm8uCKbgzT0lHj%2FTQq3ANEdcKnGce2eoS%2BVE0vPcUc5tF2gRDAO9oguETs5TFAlhe3J85cF84y1uwx6tnywB1a5ygVrKImffNBm8Xplzleond8eVtsxTTuKOFL4sBXpdrW6yY%2BfktkQz0jH9GwNe5ss8eit4Rk5Am8861rWWUCnxT2Ty1eW7NkPSj%2F5IcKzOBUZVrt4yw69skMz5x59lwYvY987F53Xdm%2B%2BC%2BDM3RHhWoooPW7P4SvCsvfe%2FioWXoPzVX2Ffq5eXJ6WMuG%2FKHhauH8FzxkR80nr2KZgpJLONiP8UwxbnQe%2B9igzhBl%2BJksipYilm4BsjGCz5S2A72iGaOQQXa%2FsmxpRDbUQq60NzkEf%2BHb%2BmcJfV6iCiL3sbsBKBuORK2XYyjzF8zdcc3XhaNOzOmZOLzAWbAUytDG08fY9QTCd%2F7DmJlOL8KbuqS4O07SdlJyy6v9woVeB10JiEqqgIuCOOK0bc17yAof8jvODg%2BkNysGNjQKQKOO6miC98DkYGHJBe1a0W1prD2lU3AS0K2PMb0k8bXRp0EKB5HELE75kEFRAEh7v5FINIz8q1Vv%2BlHTp8UuD852d92dYxtwelkix7LgClpOnj8r39PhG7sq62KznExeBvBBOL5VgsQGT6oV2aFGoTD6m%2Fy8BjqkAXAHNbnMxTi8k62NAW0dHJBtQK4aRKqvrOhkgn4OBYU%2BWIHLcExgCA6oZHd8QGsSgsQSaA56bwkHtM2mv4FKS4xLj3lvR9btMrHHj5NkZwXnXH8JKkgw6K9eNQ%2BUgc6oLmO%2FVmKlTjdZgcKYPIfk7Gt5VaQr84w420ouHhD8CT%2F2%2FHitMJwVAioPxRz%2Fs69fbKaevUuSb%2F4JObrfs3Fpvo8BUzhH&X-Amz-Signature=a65272c115bd0746f18080ea4d9ae4f0999fbe8d5889432668c6a76f7d28839f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7YD7EUO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJwmwu%2BVGw5p%2BQWidcPD99WAwtwQNtyeWLtBiz%2BBpDQQIhAPbfqXuooxaSVCdYhVl5xLhKSU9824bGo8iiL1xmnkMJKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwm8uCKbgzT0lHj%2FTQq3ANEdcKnGce2eoS%2BVE0vPcUc5tF2gRDAO9oguETs5TFAlhe3J85cF84y1uwx6tnywB1a5ygVrKImffNBm8Xplzleond8eVtsxTTuKOFL4sBXpdrW6yY%2BfktkQz0jH9GwNe5ss8eit4Rk5Am8861rWWUCnxT2Ty1eW7NkPSj%2F5IcKzOBUZVrt4yw69skMz5x59lwYvY987F53Xdm%2B%2BC%2BDM3RHhWoooPW7P4SvCsvfe%2FioWXoPzVX2Ffq5eXJ6WMuG%2FKHhauH8FzxkR80nr2KZgpJLONiP8UwxbnQe%2B9igzhBl%2BJksipYilm4BsjGCz5S2A72iGaOQQXa%2FsmxpRDbUQq60NzkEf%2BHb%2BmcJfV6iCiL3sbsBKBuORK2XYyjzF8zdcc3XhaNOzOmZOLzAWbAUytDG08fY9QTCd%2F7DmJlOL8KbuqS4O07SdlJyy6v9woVeB10JiEqqgIuCOOK0bc17yAof8jvODg%2BkNysGNjQKQKOO6miC98DkYGHJBe1a0W1prD2lU3AS0K2PMb0k8bXRp0EKB5HELE75kEFRAEh7v5FINIz8q1Vv%2BlHTp8UuD852d92dYxtwelkix7LgClpOnj8r39PhG7sq62KznExeBvBBOL5VgsQGT6oV2aFGoTD6m%2Fy8BjqkAXAHNbnMxTi8k62NAW0dHJBtQK4aRKqvrOhkgn4OBYU%2BWIHLcExgCA6oZHd8QGsSgsQSaA56bwkHtM2mv4FKS4xLj3lvR9btMrHHj5NkZwXnXH8JKkgw6K9eNQ%2BUgc6oLmO%2FVmKlTjdZgcKYPIfk7Gt5VaQr84w420ouHhD8CT%2F2%2FHitMJwVAioPxRz%2Fs69fbKaevUuSb%2F4JObrfs3Fpvo8BUzhH&X-Amz-Signature=cf4e69010621806c50a14805f2db068753e3a27b0bac0168c641d14ad508494b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7YD7EUO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJwmwu%2BVGw5p%2BQWidcPD99WAwtwQNtyeWLtBiz%2BBpDQQIhAPbfqXuooxaSVCdYhVl5xLhKSU9824bGo8iiL1xmnkMJKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwm8uCKbgzT0lHj%2FTQq3ANEdcKnGce2eoS%2BVE0vPcUc5tF2gRDAO9oguETs5TFAlhe3J85cF84y1uwx6tnywB1a5ygVrKImffNBm8Xplzleond8eVtsxTTuKOFL4sBXpdrW6yY%2BfktkQz0jH9GwNe5ss8eit4Rk5Am8861rWWUCnxT2Ty1eW7NkPSj%2F5IcKzOBUZVrt4yw69skMz5x59lwYvY987F53Xdm%2B%2BC%2BDM3RHhWoooPW7P4SvCsvfe%2FioWXoPzVX2Ffq5eXJ6WMuG%2FKHhauH8FzxkR80nr2KZgpJLONiP8UwxbnQe%2B9igzhBl%2BJksipYilm4BsjGCz5S2A72iGaOQQXa%2FsmxpRDbUQq60NzkEf%2BHb%2BmcJfV6iCiL3sbsBKBuORK2XYyjzF8zdcc3XhaNOzOmZOLzAWbAUytDG08fY9QTCd%2F7DmJlOL8KbuqS4O07SdlJyy6v9woVeB10JiEqqgIuCOOK0bc17yAof8jvODg%2BkNysGNjQKQKOO6miC98DkYGHJBe1a0W1prD2lU3AS0K2PMb0k8bXRp0EKB5HELE75kEFRAEh7v5FINIz8q1Vv%2BlHTp8UuD852d92dYxtwelkix7LgClpOnj8r39PhG7sq62KznExeBvBBOL5VgsQGT6oV2aFGoTD6m%2Fy8BjqkAXAHNbnMxTi8k62NAW0dHJBtQK4aRKqvrOhkgn4OBYU%2BWIHLcExgCA6oZHd8QGsSgsQSaA56bwkHtM2mv4FKS4xLj3lvR9btMrHHj5NkZwXnXH8JKkgw6K9eNQ%2BUgc6oLmO%2FVmKlTjdZgcKYPIfk7Gt5VaQr84w420ouHhD8CT%2F2%2FHitMJwVAioPxRz%2Fs69fbKaevUuSb%2F4JObrfs3Fpvo8BUzhH&X-Amz-Signature=00cb630bdbcd3b70e026579c6974b1b79a6087d09043a0b14c27518ce8e38054&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665OSLTK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9jtkSKMJSwDYnBGK%2FrrTNWMLAv3ePHZCLYXM80HKLHgIgZypn5VYSd%2BZT9TnveygPhDwttfjRVKyX1oi1siv0yw0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFSAc%2F%2FD6YcZ%2BNB2CrcAzooz3Q8WFAbBGPC7InzpCFhkAXdd2deilE4W5QHQtaWUL5U9Dhq17cL8AN3lDSAtj%2Bn3DF4X4cEIiTI0PWJlC5yhRHbsBf77k3TsUH5hw5TbKfHwzNZDvRHKC1LaEXpRM%2BjbgYBX%2FLT6np1dCXlPB35bSXj34EDJhcorqP%2FkxjiHLsZCaHIM7DOI0ucPhD9SE9oxZEys11gwpEsAjayGORX1JKX7Yq0EOMfNMFU1NUkVUjWistO0qmr6rNgijR%2BjQmUSvGriOB4NZBtr1fjbKT8314P0v6mYwst5QHMDEl0oXHB3BLl4CZsS5BlDMdzoiaVwD%2FN3y9FCPLv5SEB3bZEXDzwDU5xfkOA%2Bocf3rCQsGTURKeOBxHIN5PMyq2CNju6HpLLl%2BzQbC2NSmzU5z5pgFGDm9RUkZ79r%2BX7w05VaNJIstH73lWiyBWOY27uUVlQQLrhLCCRWEteVmYdrJibwsX53hIcQs0g2EwGElEznvqwBbgfhz7k9l6n48uWcAGjgDKEcZb9VEtdxBfvKaldIAN2JBGdyr24J6QV%2FPSc%2FSlRgpwfq4Vb2DJpF8NNeufOhEZ%2Bd4G4kXq4X7k6Zwo7NfFMd%2FfBJlB4Cd%2BcrZ2jgQz5yow38VmAHLh%2BMKSc%2FLwGOqUBRUUCV1HYAavEOWO59WaM2Psjzfrbd38XT5%2BftFckV1tcA%2BjQp2lnbSys6MEiXW6B4Gme1wje9%2FHlCIx1pm%2FTpBnVN4bJJlDyEOnOwKdOpuCll1BkdrB7BfG0cv8NVIt8QdUIGZV1J0zDzO1BG01n08nneUSQ5iLFiybj9baAyorpBzAStwBfN2pElcY6Zknz3liDQDWB%2BM3KH8UZG67g2rnQuQR6&X-Amz-Signature=8d0674beb000d18b92bcbefa34b7f216099b4cb865fe551f58cc514b8799698e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665OSLTK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9jtkSKMJSwDYnBGK%2FrrTNWMLAv3ePHZCLYXM80HKLHgIgZypn5VYSd%2BZT9TnveygPhDwttfjRVKyX1oi1siv0yw0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFSAc%2F%2FD6YcZ%2BNB2CrcAzooz3Q8WFAbBGPC7InzpCFhkAXdd2deilE4W5QHQtaWUL5U9Dhq17cL8AN3lDSAtj%2Bn3DF4X4cEIiTI0PWJlC5yhRHbsBf77k3TsUH5hw5TbKfHwzNZDvRHKC1LaEXpRM%2BjbgYBX%2FLT6np1dCXlPB35bSXj34EDJhcorqP%2FkxjiHLsZCaHIM7DOI0ucPhD9SE9oxZEys11gwpEsAjayGORX1JKX7Yq0EOMfNMFU1NUkVUjWistO0qmr6rNgijR%2BjQmUSvGriOB4NZBtr1fjbKT8314P0v6mYwst5QHMDEl0oXHB3BLl4CZsS5BlDMdzoiaVwD%2FN3y9FCPLv5SEB3bZEXDzwDU5xfkOA%2Bocf3rCQsGTURKeOBxHIN5PMyq2CNju6HpLLl%2BzQbC2NSmzU5z5pgFGDm9RUkZ79r%2BX7w05VaNJIstH73lWiyBWOY27uUVlQQLrhLCCRWEteVmYdrJibwsX53hIcQs0g2EwGElEznvqwBbgfhz7k9l6n48uWcAGjgDKEcZb9VEtdxBfvKaldIAN2JBGdyr24J6QV%2FPSc%2FSlRgpwfq4Vb2DJpF8NNeufOhEZ%2Bd4G4kXq4X7k6Zwo7NfFMd%2FfBJlB4Cd%2BcrZ2jgQz5yow38VmAHLh%2BMKSc%2FLwGOqUBRUUCV1HYAavEOWO59WaM2Psjzfrbd38XT5%2BftFckV1tcA%2BjQp2lnbSys6MEiXW6B4Gme1wje9%2FHlCIx1pm%2FTpBnVN4bJJlDyEOnOwKdOpuCll1BkdrB7BfG0cv8NVIt8QdUIGZV1J0zDzO1BG01n08nneUSQ5iLFiybj9baAyorpBzAStwBfN2pElcY6Zknz3liDQDWB%2BM3KH8UZG67g2rnQuQR6&X-Amz-Signature=f5e62e0e1df2f2672091e37c2ecc5832928369629e1f2be652fac1a158511947&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665OSLTK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9jtkSKMJSwDYnBGK%2FrrTNWMLAv3ePHZCLYXM80HKLHgIgZypn5VYSd%2BZT9TnveygPhDwttfjRVKyX1oi1siv0yw0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFSAc%2F%2FD6YcZ%2BNB2CrcAzooz3Q8WFAbBGPC7InzpCFhkAXdd2deilE4W5QHQtaWUL5U9Dhq17cL8AN3lDSAtj%2Bn3DF4X4cEIiTI0PWJlC5yhRHbsBf77k3TsUH5hw5TbKfHwzNZDvRHKC1LaEXpRM%2BjbgYBX%2FLT6np1dCXlPB35bSXj34EDJhcorqP%2FkxjiHLsZCaHIM7DOI0ucPhD9SE9oxZEys11gwpEsAjayGORX1JKX7Yq0EOMfNMFU1NUkVUjWistO0qmr6rNgijR%2BjQmUSvGriOB4NZBtr1fjbKT8314P0v6mYwst5QHMDEl0oXHB3BLl4CZsS5BlDMdzoiaVwD%2FN3y9FCPLv5SEB3bZEXDzwDU5xfkOA%2Bocf3rCQsGTURKeOBxHIN5PMyq2CNju6HpLLl%2BzQbC2NSmzU5z5pgFGDm9RUkZ79r%2BX7w05VaNJIstH73lWiyBWOY27uUVlQQLrhLCCRWEteVmYdrJibwsX53hIcQs0g2EwGElEznvqwBbgfhz7k9l6n48uWcAGjgDKEcZb9VEtdxBfvKaldIAN2JBGdyr24J6QV%2FPSc%2FSlRgpwfq4Vb2DJpF8NNeufOhEZ%2Bd4G4kXq4X7k6Zwo7NfFMd%2FfBJlB4Cd%2BcrZ2jgQz5yow38VmAHLh%2BMKSc%2FLwGOqUBRUUCV1HYAavEOWO59WaM2Psjzfrbd38XT5%2BftFckV1tcA%2BjQp2lnbSys6MEiXW6B4Gme1wje9%2FHlCIx1pm%2FTpBnVN4bJJlDyEOnOwKdOpuCll1BkdrB7BfG0cv8NVIt8QdUIGZV1J0zDzO1BG01n08nneUSQ5iLFiybj9baAyorpBzAStwBfN2pElcY6Zknz3liDQDWB%2BM3KH8UZG67g2rnQuQR6&X-Amz-Signature=a43db74a0fd1f5fab3e2223baf380681a63fe0ed10f031ef92ed8f85c8468627&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665OSLTK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9jtkSKMJSwDYnBGK%2FrrTNWMLAv3ePHZCLYXM80HKLHgIgZypn5VYSd%2BZT9TnveygPhDwttfjRVKyX1oi1siv0yw0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFSAc%2F%2FD6YcZ%2BNB2CrcAzooz3Q8WFAbBGPC7InzpCFhkAXdd2deilE4W5QHQtaWUL5U9Dhq17cL8AN3lDSAtj%2Bn3DF4X4cEIiTI0PWJlC5yhRHbsBf77k3TsUH5hw5TbKfHwzNZDvRHKC1LaEXpRM%2BjbgYBX%2FLT6np1dCXlPB35bSXj34EDJhcorqP%2FkxjiHLsZCaHIM7DOI0ucPhD9SE9oxZEys11gwpEsAjayGORX1JKX7Yq0EOMfNMFU1NUkVUjWistO0qmr6rNgijR%2BjQmUSvGriOB4NZBtr1fjbKT8314P0v6mYwst5QHMDEl0oXHB3BLl4CZsS5BlDMdzoiaVwD%2FN3y9FCPLv5SEB3bZEXDzwDU5xfkOA%2Bocf3rCQsGTURKeOBxHIN5PMyq2CNju6HpLLl%2BzQbC2NSmzU5z5pgFGDm9RUkZ79r%2BX7w05VaNJIstH73lWiyBWOY27uUVlQQLrhLCCRWEteVmYdrJibwsX53hIcQs0g2EwGElEznvqwBbgfhz7k9l6n48uWcAGjgDKEcZb9VEtdxBfvKaldIAN2JBGdyr24J6QV%2FPSc%2FSlRgpwfq4Vb2DJpF8NNeufOhEZ%2Bd4G4kXq4X7k6Zwo7NfFMd%2FfBJlB4Cd%2BcrZ2jgQz5yow38VmAHLh%2BMKSc%2FLwGOqUBRUUCV1HYAavEOWO59WaM2Psjzfrbd38XT5%2BftFckV1tcA%2BjQp2lnbSys6MEiXW6B4Gme1wje9%2FHlCIx1pm%2FTpBnVN4bJJlDyEOnOwKdOpuCll1BkdrB7BfG0cv8NVIt8QdUIGZV1J0zDzO1BG01n08nneUSQ5iLFiybj9baAyorpBzAStwBfN2pElcY6Zknz3liDQDWB%2BM3KH8UZG67g2rnQuQR6&X-Amz-Signature=667439cf0f1158a9a4540623bbc2a3065c9536ff3dad29f7703b4202e1a47101&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665OSLTK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9jtkSKMJSwDYnBGK%2FrrTNWMLAv3ePHZCLYXM80HKLHgIgZypn5VYSd%2BZT9TnveygPhDwttfjRVKyX1oi1siv0yw0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFSAc%2F%2FD6YcZ%2BNB2CrcAzooz3Q8WFAbBGPC7InzpCFhkAXdd2deilE4W5QHQtaWUL5U9Dhq17cL8AN3lDSAtj%2Bn3DF4X4cEIiTI0PWJlC5yhRHbsBf77k3TsUH5hw5TbKfHwzNZDvRHKC1LaEXpRM%2BjbgYBX%2FLT6np1dCXlPB35bSXj34EDJhcorqP%2FkxjiHLsZCaHIM7DOI0ucPhD9SE9oxZEys11gwpEsAjayGORX1JKX7Yq0EOMfNMFU1NUkVUjWistO0qmr6rNgijR%2BjQmUSvGriOB4NZBtr1fjbKT8314P0v6mYwst5QHMDEl0oXHB3BLl4CZsS5BlDMdzoiaVwD%2FN3y9FCPLv5SEB3bZEXDzwDU5xfkOA%2Bocf3rCQsGTURKeOBxHIN5PMyq2CNju6HpLLl%2BzQbC2NSmzU5z5pgFGDm9RUkZ79r%2BX7w05VaNJIstH73lWiyBWOY27uUVlQQLrhLCCRWEteVmYdrJibwsX53hIcQs0g2EwGElEznvqwBbgfhz7k9l6n48uWcAGjgDKEcZb9VEtdxBfvKaldIAN2JBGdyr24J6QV%2FPSc%2FSlRgpwfq4Vb2DJpF8NNeufOhEZ%2Bd4G4kXq4X7k6Zwo7NfFMd%2FfBJlB4Cd%2BcrZ2jgQz5yow38VmAHLh%2BMKSc%2FLwGOqUBRUUCV1HYAavEOWO59WaM2Psjzfrbd38XT5%2BftFckV1tcA%2BjQp2lnbSys6MEiXW6B4Gme1wje9%2FHlCIx1pm%2FTpBnVN4bJJlDyEOnOwKdOpuCll1BkdrB7BfG0cv8NVIt8QdUIGZV1J0zDzO1BG01n08nneUSQ5iLFiybj9baAyorpBzAStwBfN2pElcY6Zknz3liDQDWB%2BM3KH8UZG67g2rnQuQR6&X-Amz-Signature=d7176cfe63e78013b80dd3c545f3e4716834f821f2a070dddfbbe15e121da075&X-Amz-SignedHeaders=host&x-id=GetObject)
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


