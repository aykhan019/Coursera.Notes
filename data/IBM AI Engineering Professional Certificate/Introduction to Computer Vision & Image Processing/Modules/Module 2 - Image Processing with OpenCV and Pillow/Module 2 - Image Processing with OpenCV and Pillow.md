

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXI6XEOF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCvDN619U1H1vh4r%2FTXKbszr63s2XtJt%2B97lPJvAmcQbwIgWs1NB7ucaDL73XqMkk8NqYiJTdB3a35RPEPnaah%2FyjIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO7JjMMMltb90XE2rircA8aOhSEaaOSnKzeTHMi6%2B8oXU%2F1SzyCKUXPq1msoY49wMGjKGg6Hk4WbKptmGKHVlzXyC%2FWdWah0laj4uDzyErPl%2BFv4nHdUJbnh7KjvqOa4CRarnXbHnP1CzKyGs2gj4bJlqDWDjPa4AnlWfhooSnrxIJuRu5cxBKzZdu%2FTjHnEjSHKMOpKzSEJDL7zdbi970lCzQxszyBu0DfC0Ad3Pg0UqH6VBjEWzBPxTxYGpyU99UnxpIFHVscBFJjVrlt5me83Ue2RS%2BUQTgvnLi8TlblrUCm6F3aE38YrhLpdpU2SnInTjbJH3GEawr4JxjRTIU87bMtSXUKpjOJ2trLHhKIveE0OoRqz0SiD3KiJ4DL3WFqWFWZZcKlZYel3dcCJ6Mqbcq%2BTgfegDe4guBoTeIOqzw1JKNC82GILo0%2B5Onms4QiKyWcYtBK8%2Bdyjf4s1KjY8WmW7BHn09yMjWcl8G8qGX1cMUHAU%2BeBYYq9l06neaicfs8ixfq83CrcoiYIDXdMWsZF66stbWhIfwCIp%2Bt0vF1ELLhBn%2F9eB%2BZnML930TAWvW7JtKur1540BvzT6wPSM8wGFC%2FMTosk1nRT%2FRJgviNtcl0iMs%2B7Ke1Z4%2BUBWH%2FzxkEWPzitocr7tMPWOnL0GOqUB%2BjHujZPBPSKPv7sIdOfa4oYHnawd0F%2FvDKZLaLtX22T8Mmo9CWpwXA64InNO5Jj1jw%2F23i1bhUE5aeQ7PlO%2FuYRlHXivDmkLijO%2FHD4fgNMe8NAb8SnhigmHVb8VYQFBndH%2FHMPn7%2BrHujnTc3QQD4EJ6DFShrTxIRoDgESEpfLAYzxTdWlxUXgvzrH9p%2Bgl3y8Jp6K%2Fc6Ea8T75ppT2YFdpQ6lY&X-Amz-Signature=f656bd16229ff2714113b6f97c13852289d7f931ad25f2650d3306c414f5f76e&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRNSM5UI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHzzDV6iPCc%2FZ63SZscfMv1u27zipg9leRfI3Q8bMwLEAiEAnzBRPVVZ0amKSoFkNlqzkk3JcjlFwc%2F%2FVGKIEdf3KfUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGaG3hq%2BjkXvp%2FSGvyrcA7bkjp%2FcLG%2BrjAKrPZEnTDz1ZIS5k%2FC28uu9lO%2BpNY8EkttHPINTZKKnRBEikP7AYP6oTn%2FvenEaWKZ6VlyJwurbbprrM33wrhSn10xxQqEdY8DK7xEggwBX1i1CXzoNMtmzBLXaT8qLpGqkLd66yIjn%2FIWNrY0Os37ksqXG0c5engGj7hPk6LaUo56ZuVs0RdZ457q93GGIx6QONBYrQhWakJPWDYZGWziNtbGrQYOkjR%2Bk1GMLjXKG6Qrfet92qdKuthP1sbTPRfa0sXyYs7QdeRyWtxvVa9GtX3RenFPS%2FeXY4%2FZAoi2AvL%2FqU%2BegkLMR5uUxByBh9tKy%2FV6oX3KF2TONIqdpZ38D9e0xJWd21RnLLvg9RUidqW8G6GIc9lkDgoNTqZNvz%2FZRj0GJoAg01tRIvbjkR%2FN0bbf%2BSHn6gDh%2BrP1sNB%2B%2BoP5QP9H08hqnnq46XQFgXHjMhjPRGB75bKq5lYUbG3XLO0CnD9isztNto9EDWMnZpQsceHCKqHY%2B5pA%2FUAQTNyDq2WkyiC21U3cMFEERVbsB%2BGzHTlC5LmuxXVR8a1bdBs%2BZI1muTPoJwwBZ7wkCFcnyv8ojz0fg7IcUc4rUKVMSask9vrZ4SMeWVXeNgvpvTdWvMIqOnL0GOqUBnxxSLPAKv4abAzJ6FX2ric1zi8Yt1sYk%2BpgiU8PqjGQ2lEuO1ZGYLbvljq2Pxo0U9zHBtl%2BxssL4ZTq1iD9WohwOLvHkGHfgvOu9CF9XBBITRPLL5Qj29RpoWfq5Uy4XhUoYkysChi1ncDh962btPbLwa4sR8x8BRaaYsVBZojP3tEq4Wx3k6GQvX%2Bno4hTMdYpRoN7Gx7QPSmEtF%2BOZM4sF5Xur&X-Amz-Signature=68fd825775e5040aa075ac848e64b64d1b4085d656025a7cd6c11008ede5432f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRNSM5UI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHzzDV6iPCc%2FZ63SZscfMv1u27zipg9leRfI3Q8bMwLEAiEAnzBRPVVZ0amKSoFkNlqzkk3JcjlFwc%2F%2FVGKIEdf3KfUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGaG3hq%2BjkXvp%2FSGvyrcA7bkjp%2FcLG%2BrjAKrPZEnTDz1ZIS5k%2FC28uu9lO%2BpNY8EkttHPINTZKKnRBEikP7AYP6oTn%2FvenEaWKZ6VlyJwurbbprrM33wrhSn10xxQqEdY8DK7xEggwBX1i1CXzoNMtmzBLXaT8qLpGqkLd66yIjn%2FIWNrY0Os37ksqXG0c5engGj7hPk6LaUo56ZuVs0RdZ457q93GGIx6QONBYrQhWakJPWDYZGWziNtbGrQYOkjR%2Bk1GMLjXKG6Qrfet92qdKuthP1sbTPRfa0sXyYs7QdeRyWtxvVa9GtX3RenFPS%2FeXY4%2FZAoi2AvL%2FqU%2BegkLMR5uUxByBh9tKy%2FV6oX3KF2TONIqdpZ38D9e0xJWd21RnLLvg9RUidqW8G6GIc9lkDgoNTqZNvz%2FZRj0GJoAg01tRIvbjkR%2FN0bbf%2BSHn6gDh%2BrP1sNB%2B%2BoP5QP9H08hqnnq46XQFgXHjMhjPRGB75bKq5lYUbG3XLO0CnD9isztNto9EDWMnZpQsceHCKqHY%2B5pA%2FUAQTNyDq2WkyiC21U3cMFEERVbsB%2BGzHTlC5LmuxXVR8a1bdBs%2BZI1muTPoJwwBZ7wkCFcnyv8ojz0fg7IcUc4rUKVMSask9vrZ4SMeWVXeNgvpvTdWvMIqOnL0GOqUBnxxSLPAKv4abAzJ6FX2ric1zi8Yt1sYk%2BpgiU8PqjGQ2lEuO1ZGYLbvljq2Pxo0U9zHBtl%2BxssL4ZTq1iD9WohwOLvHkGHfgvOu9CF9XBBITRPLL5Qj29RpoWfq5Uy4XhUoYkysChi1ncDh962btPbLwa4sR8x8BRaaYsVBZojP3tEq4Wx3k6GQvX%2Bno4hTMdYpRoN7Gx7QPSmEtF%2BOZM4sF5Xur&X-Amz-Signature=4f4caa92b79feedf55712555f82af528c2bb60e894899516be46041d34054598&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRNSM5UI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHzzDV6iPCc%2FZ63SZscfMv1u27zipg9leRfI3Q8bMwLEAiEAnzBRPVVZ0amKSoFkNlqzkk3JcjlFwc%2F%2FVGKIEdf3KfUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGaG3hq%2BjkXvp%2FSGvyrcA7bkjp%2FcLG%2BrjAKrPZEnTDz1ZIS5k%2FC28uu9lO%2BpNY8EkttHPINTZKKnRBEikP7AYP6oTn%2FvenEaWKZ6VlyJwurbbprrM33wrhSn10xxQqEdY8DK7xEggwBX1i1CXzoNMtmzBLXaT8qLpGqkLd66yIjn%2FIWNrY0Os37ksqXG0c5engGj7hPk6LaUo56ZuVs0RdZ457q93GGIx6QONBYrQhWakJPWDYZGWziNtbGrQYOkjR%2Bk1GMLjXKG6Qrfet92qdKuthP1sbTPRfa0sXyYs7QdeRyWtxvVa9GtX3RenFPS%2FeXY4%2FZAoi2AvL%2FqU%2BegkLMR5uUxByBh9tKy%2FV6oX3KF2TONIqdpZ38D9e0xJWd21RnLLvg9RUidqW8G6GIc9lkDgoNTqZNvz%2FZRj0GJoAg01tRIvbjkR%2FN0bbf%2BSHn6gDh%2BrP1sNB%2B%2BoP5QP9H08hqnnq46XQFgXHjMhjPRGB75bKq5lYUbG3XLO0CnD9isztNto9EDWMnZpQsceHCKqHY%2B5pA%2FUAQTNyDq2WkyiC21U3cMFEERVbsB%2BGzHTlC5LmuxXVR8a1bdBs%2BZI1muTPoJwwBZ7wkCFcnyv8ojz0fg7IcUc4rUKVMSask9vrZ4SMeWVXeNgvpvTdWvMIqOnL0GOqUBnxxSLPAKv4abAzJ6FX2ric1zi8Yt1sYk%2BpgiU8PqjGQ2lEuO1ZGYLbvljq2Pxo0U9zHBtl%2BxssL4ZTq1iD9WohwOLvHkGHfgvOu9CF9XBBITRPLL5Qj29RpoWfq5Uy4XhUoYkysChi1ncDh962btPbLwa4sR8x8BRaaYsVBZojP3tEq4Wx3k6GQvX%2Bno4hTMdYpRoN7Gx7QPSmEtF%2BOZM4sF5Xur&X-Amz-Signature=196833f1bd19e7b2de027553c259cd4858d6c84680d697c0ef2d47e1ab147856&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRNSM5UI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHzzDV6iPCc%2FZ63SZscfMv1u27zipg9leRfI3Q8bMwLEAiEAnzBRPVVZ0amKSoFkNlqzkk3JcjlFwc%2F%2FVGKIEdf3KfUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGaG3hq%2BjkXvp%2FSGvyrcA7bkjp%2FcLG%2BrjAKrPZEnTDz1ZIS5k%2FC28uu9lO%2BpNY8EkttHPINTZKKnRBEikP7AYP6oTn%2FvenEaWKZ6VlyJwurbbprrM33wrhSn10xxQqEdY8DK7xEggwBX1i1CXzoNMtmzBLXaT8qLpGqkLd66yIjn%2FIWNrY0Os37ksqXG0c5engGj7hPk6LaUo56ZuVs0RdZ457q93GGIx6QONBYrQhWakJPWDYZGWziNtbGrQYOkjR%2Bk1GMLjXKG6Qrfet92qdKuthP1sbTPRfa0sXyYs7QdeRyWtxvVa9GtX3RenFPS%2FeXY4%2FZAoi2AvL%2FqU%2BegkLMR5uUxByBh9tKy%2FV6oX3KF2TONIqdpZ38D9e0xJWd21RnLLvg9RUidqW8G6GIc9lkDgoNTqZNvz%2FZRj0GJoAg01tRIvbjkR%2FN0bbf%2BSHn6gDh%2BrP1sNB%2B%2BoP5QP9H08hqnnq46XQFgXHjMhjPRGB75bKq5lYUbG3XLO0CnD9isztNto9EDWMnZpQsceHCKqHY%2B5pA%2FUAQTNyDq2WkyiC21U3cMFEERVbsB%2BGzHTlC5LmuxXVR8a1bdBs%2BZI1muTPoJwwBZ7wkCFcnyv8ojz0fg7IcUc4rUKVMSask9vrZ4SMeWVXeNgvpvTdWvMIqOnL0GOqUBnxxSLPAKv4abAzJ6FX2ric1zi8Yt1sYk%2BpgiU8PqjGQ2lEuO1ZGYLbvljq2Pxo0U9zHBtl%2BxssL4ZTq1iD9WohwOLvHkGHfgvOu9CF9XBBITRPLL5Qj29RpoWfq5Uy4XhUoYkysChi1ncDh962btPbLwa4sR8x8BRaaYsVBZojP3tEq4Wx3k6GQvX%2Bno4hTMdYpRoN7Gx7QPSmEtF%2BOZM4sF5Xur&X-Amz-Signature=408857074c702afbdba1900c928a14c051c9155eb2a7c663684f005173f50ab8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRNSM5UI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHzzDV6iPCc%2FZ63SZscfMv1u27zipg9leRfI3Q8bMwLEAiEAnzBRPVVZ0amKSoFkNlqzkk3JcjlFwc%2F%2FVGKIEdf3KfUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGaG3hq%2BjkXvp%2FSGvyrcA7bkjp%2FcLG%2BrjAKrPZEnTDz1ZIS5k%2FC28uu9lO%2BpNY8EkttHPINTZKKnRBEikP7AYP6oTn%2FvenEaWKZ6VlyJwurbbprrM33wrhSn10xxQqEdY8DK7xEggwBX1i1CXzoNMtmzBLXaT8qLpGqkLd66yIjn%2FIWNrY0Os37ksqXG0c5engGj7hPk6LaUo56ZuVs0RdZ457q93GGIx6QONBYrQhWakJPWDYZGWziNtbGrQYOkjR%2Bk1GMLjXKG6Qrfet92qdKuthP1sbTPRfa0sXyYs7QdeRyWtxvVa9GtX3RenFPS%2FeXY4%2FZAoi2AvL%2FqU%2BegkLMR5uUxByBh9tKy%2FV6oX3KF2TONIqdpZ38D9e0xJWd21RnLLvg9RUidqW8G6GIc9lkDgoNTqZNvz%2FZRj0GJoAg01tRIvbjkR%2FN0bbf%2BSHn6gDh%2BrP1sNB%2B%2BoP5QP9H08hqnnq46XQFgXHjMhjPRGB75bKq5lYUbG3XLO0CnD9isztNto9EDWMnZpQsceHCKqHY%2B5pA%2FUAQTNyDq2WkyiC21U3cMFEERVbsB%2BGzHTlC5LmuxXVR8a1bdBs%2BZI1muTPoJwwBZ7wkCFcnyv8ojz0fg7IcUc4rUKVMSask9vrZ4SMeWVXeNgvpvTdWvMIqOnL0GOqUBnxxSLPAKv4abAzJ6FX2ric1zi8Yt1sYk%2BpgiU8PqjGQ2lEuO1ZGYLbvljq2Pxo0U9zHBtl%2BxssL4ZTq1iD9WohwOLvHkGHfgvOu9CF9XBBITRPLL5Qj29RpoWfq5Uy4XhUoYkysChi1ncDh962btPbLwa4sR8x8BRaaYsVBZojP3tEq4Wx3k6GQvX%2Bno4hTMdYpRoN7Gx7QPSmEtF%2BOZM4sF5Xur&X-Amz-Signature=56927f0d362c44b0484173a1c87f7912be17257dec49c71fc9e0a19ffdfd6571&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXI6XEOF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCvDN619U1H1vh4r%2FTXKbszr63s2XtJt%2B97lPJvAmcQbwIgWs1NB7ucaDL73XqMkk8NqYiJTdB3a35RPEPnaah%2FyjIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO7JjMMMltb90XE2rircA8aOhSEaaOSnKzeTHMi6%2B8oXU%2F1SzyCKUXPq1msoY49wMGjKGg6Hk4WbKptmGKHVlzXyC%2FWdWah0laj4uDzyErPl%2BFv4nHdUJbnh7KjvqOa4CRarnXbHnP1CzKyGs2gj4bJlqDWDjPa4AnlWfhooSnrxIJuRu5cxBKzZdu%2FTjHnEjSHKMOpKzSEJDL7zdbi970lCzQxszyBu0DfC0Ad3Pg0UqH6VBjEWzBPxTxYGpyU99UnxpIFHVscBFJjVrlt5me83Ue2RS%2BUQTgvnLi8TlblrUCm6F3aE38YrhLpdpU2SnInTjbJH3GEawr4JxjRTIU87bMtSXUKpjOJ2trLHhKIveE0OoRqz0SiD3KiJ4DL3WFqWFWZZcKlZYel3dcCJ6Mqbcq%2BTgfegDe4guBoTeIOqzw1JKNC82GILo0%2B5Onms4QiKyWcYtBK8%2Bdyjf4s1KjY8WmW7BHn09yMjWcl8G8qGX1cMUHAU%2BeBYYq9l06neaicfs8ixfq83CrcoiYIDXdMWsZF66stbWhIfwCIp%2Bt0vF1ELLhBn%2F9eB%2BZnML930TAWvW7JtKur1540BvzT6wPSM8wGFC%2FMTosk1nRT%2FRJgviNtcl0iMs%2B7Ke1Z4%2BUBWH%2FzxkEWPzitocr7tMPWOnL0GOqUB%2BjHujZPBPSKPv7sIdOfa4oYHnawd0F%2FvDKZLaLtX22T8Mmo9CWpwXA64InNO5Jj1jw%2F23i1bhUE5aeQ7PlO%2FuYRlHXivDmkLijO%2FHD4fgNMe8NAb8SnhigmHVb8VYQFBndH%2FHMPn7%2BrHujnTc3QQD4EJ6DFShrTxIRoDgESEpfLAYzxTdWlxUXgvzrH9p%2Bgl3y8Jp6K%2Fc6Ea8T75ppT2YFdpQ6lY&X-Amz-Signature=73dc7097f9c756cf077b07fce3e00f50ee3b9d2eb94a92d1788769d478e047a8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXI6XEOF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCvDN619U1H1vh4r%2FTXKbszr63s2XtJt%2B97lPJvAmcQbwIgWs1NB7ucaDL73XqMkk8NqYiJTdB3a35RPEPnaah%2FyjIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO7JjMMMltb90XE2rircA8aOhSEaaOSnKzeTHMi6%2B8oXU%2F1SzyCKUXPq1msoY49wMGjKGg6Hk4WbKptmGKHVlzXyC%2FWdWah0laj4uDzyErPl%2BFv4nHdUJbnh7KjvqOa4CRarnXbHnP1CzKyGs2gj4bJlqDWDjPa4AnlWfhooSnrxIJuRu5cxBKzZdu%2FTjHnEjSHKMOpKzSEJDL7zdbi970lCzQxszyBu0DfC0Ad3Pg0UqH6VBjEWzBPxTxYGpyU99UnxpIFHVscBFJjVrlt5me83Ue2RS%2BUQTgvnLi8TlblrUCm6F3aE38YrhLpdpU2SnInTjbJH3GEawr4JxjRTIU87bMtSXUKpjOJ2trLHhKIveE0OoRqz0SiD3KiJ4DL3WFqWFWZZcKlZYel3dcCJ6Mqbcq%2BTgfegDe4guBoTeIOqzw1JKNC82GILo0%2B5Onms4QiKyWcYtBK8%2Bdyjf4s1KjY8WmW7BHn09yMjWcl8G8qGX1cMUHAU%2BeBYYq9l06neaicfs8ixfq83CrcoiYIDXdMWsZF66stbWhIfwCIp%2Bt0vF1ELLhBn%2F9eB%2BZnML930TAWvW7JtKur1540BvzT6wPSM8wGFC%2FMTosk1nRT%2FRJgviNtcl0iMs%2B7Ke1Z4%2BUBWH%2FzxkEWPzitocr7tMPWOnL0GOqUB%2BjHujZPBPSKPv7sIdOfa4oYHnawd0F%2FvDKZLaLtX22T8Mmo9CWpwXA64InNO5Jj1jw%2F23i1bhUE5aeQ7PlO%2FuYRlHXivDmkLijO%2FHD4fgNMe8NAb8SnhigmHVb8VYQFBndH%2FHMPn7%2BrHujnTc3QQD4EJ6DFShrTxIRoDgESEpfLAYzxTdWlxUXgvzrH9p%2Bgl3y8Jp6K%2Fc6Ea8T75ppT2YFdpQ6lY&X-Amz-Signature=d5f4f6a503161959854162aedc162b1041baccbc4517e110fa1e08531da6bd3a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXI6XEOF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCvDN619U1H1vh4r%2FTXKbszr63s2XtJt%2B97lPJvAmcQbwIgWs1NB7ucaDL73XqMkk8NqYiJTdB3a35RPEPnaah%2FyjIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO7JjMMMltb90XE2rircA8aOhSEaaOSnKzeTHMi6%2B8oXU%2F1SzyCKUXPq1msoY49wMGjKGg6Hk4WbKptmGKHVlzXyC%2FWdWah0laj4uDzyErPl%2BFv4nHdUJbnh7KjvqOa4CRarnXbHnP1CzKyGs2gj4bJlqDWDjPa4AnlWfhooSnrxIJuRu5cxBKzZdu%2FTjHnEjSHKMOpKzSEJDL7zdbi970lCzQxszyBu0DfC0Ad3Pg0UqH6VBjEWzBPxTxYGpyU99UnxpIFHVscBFJjVrlt5me83Ue2RS%2BUQTgvnLi8TlblrUCm6F3aE38YrhLpdpU2SnInTjbJH3GEawr4JxjRTIU87bMtSXUKpjOJ2trLHhKIveE0OoRqz0SiD3KiJ4DL3WFqWFWZZcKlZYel3dcCJ6Mqbcq%2BTgfegDe4guBoTeIOqzw1JKNC82GILo0%2B5Onms4QiKyWcYtBK8%2Bdyjf4s1KjY8WmW7BHn09yMjWcl8G8qGX1cMUHAU%2BeBYYq9l06neaicfs8ixfq83CrcoiYIDXdMWsZF66stbWhIfwCIp%2Bt0vF1ELLhBn%2F9eB%2BZnML930TAWvW7JtKur1540BvzT6wPSM8wGFC%2FMTosk1nRT%2FRJgviNtcl0iMs%2B7Ke1Z4%2BUBWH%2FzxkEWPzitocr7tMPWOnL0GOqUB%2BjHujZPBPSKPv7sIdOfa4oYHnawd0F%2FvDKZLaLtX22T8Mmo9CWpwXA64InNO5Jj1jw%2F23i1bhUE5aeQ7PlO%2FuYRlHXivDmkLijO%2FHD4fgNMe8NAb8SnhigmHVb8VYQFBndH%2FHMPn7%2BrHujnTc3QQD4EJ6DFShrTxIRoDgESEpfLAYzxTdWlxUXgvzrH9p%2Bgl3y8Jp6K%2Fc6Ea8T75ppT2YFdpQ6lY&X-Amz-Signature=7a05a056eaaae4b3daf686334fb973e5a0b5fad5774faa93dbcc6b9e8b5f39b3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXI6XEOF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCvDN619U1H1vh4r%2FTXKbszr63s2XtJt%2B97lPJvAmcQbwIgWs1NB7ucaDL73XqMkk8NqYiJTdB3a35RPEPnaah%2FyjIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO7JjMMMltb90XE2rircA8aOhSEaaOSnKzeTHMi6%2B8oXU%2F1SzyCKUXPq1msoY49wMGjKGg6Hk4WbKptmGKHVlzXyC%2FWdWah0laj4uDzyErPl%2BFv4nHdUJbnh7KjvqOa4CRarnXbHnP1CzKyGs2gj4bJlqDWDjPa4AnlWfhooSnrxIJuRu5cxBKzZdu%2FTjHnEjSHKMOpKzSEJDL7zdbi970lCzQxszyBu0DfC0Ad3Pg0UqH6VBjEWzBPxTxYGpyU99UnxpIFHVscBFJjVrlt5me83Ue2RS%2BUQTgvnLi8TlblrUCm6F3aE38YrhLpdpU2SnInTjbJH3GEawr4JxjRTIU87bMtSXUKpjOJ2trLHhKIveE0OoRqz0SiD3KiJ4DL3WFqWFWZZcKlZYel3dcCJ6Mqbcq%2BTgfegDe4guBoTeIOqzw1JKNC82GILo0%2B5Onms4QiKyWcYtBK8%2Bdyjf4s1KjY8WmW7BHn09yMjWcl8G8qGX1cMUHAU%2BeBYYq9l06neaicfs8ixfq83CrcoiYIDXdMWsZF66stbWhIfwCIp%2Bt0vF1ELLhBn%2F9eB%2BZnML930TAWvW7JtKur1540BvzT6wPSM8wGFC%2FMTosk1nRT%2FRJgviNtcl0iMs%2B7Ke1Z4%2BUBWH%2FzxkEWPzitocr7tMPWOnL0GOqUB%2BjHujZPBPSKPv7sIdOfa4oYHnawd0F%2FvDKZLaLtX22T8Mmo9CWpwXA64InNO5Jj1jw%2F23i1bhUE5aeQ7PlO%2FuYRlHXivDmkLijO%2FHD4fgNMe8NAb8SnhigmHVb8VYQFBndH%2FHMPn7%2BrHujnTc3QQD4EJ6DFShrTxIRoDgESEpfLAYzxTdWlxUXgvzrH9p%2Bgl3y8Jp6K%2Fc6Ea8T75ppT2YFdpQ6lY&X-Amz-Signature=2947706852f30bc4ea10efd3f1cb7103e2a7364410fb2adfae6c1f13b3d95227&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXI6XEOF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCvDN619U1H1vh4r%2FTXKbszr63s2XtJt%2B97lPJvAmcQbwIgWs1NB7ucaDL73XqMkk8NqYiJTdB3a35RPEPnaah%2FyjIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO7JjMMMltb90XE2rircA8aOhSEaaOSnKzeTHMi6%2B8oXU%2F1SzyCKUXPq1msoY49wMGjKGg6Hk4WbKptmGKHVlzXyC%2FWdWah0laj4uDzyErPl%2BFv4nHdUJbnh7KjvqOa4CRarnXbHnP1CzKyGs2gj4bJlqDWDjPa4AnlWfhooSnrxIJuRu5cxBKzZdu%2FTjHnEjSHKMOpKzSEJDL7zdbi970lCzQxszyBu0DfC0Ad3Pg0UqH6VBjEWzBPxTxYGpyU99UnxpIFHVscBFJjVrlt5me83Ue2RS%2BUQTgvnLi8TlblrUCm6F3aE38YrhLpdpU2SnInTjbJH3GEawr4JxjRTIU87bMtSXUKpjOJ2trLHhKIveE0OoRqz0SiD3KiJ4DL3WFqWFWZZcKlZYel3dcCJ6Mqbcq%2BTgfegDe4guBoTeIOqzw1JKNC82GILo0%2B5Onms4QiKyWcYtBK8%2Bdyjf4s1KjY8WmW7BHn09yMjWcl8G8qGX1cMUHAU%2BeBYYq9l06neaicfs8ixfq83CrcoiYIDXdMWsZF66stbWhIfwCIp%2Bt0vF1ELLhBn%2F9eB%2BZnML930TAWvW7JtKur1540BvzT6wPSM8wGFC%2FMTosk1nRT%2FRJgviNtcl0iMs%2B7Ke1Z4%2BUBWH%2FzxkEWPzitocr7tMPWOnL0GOqUB%2BjHujZPBPSKPv7sIdOfa4oYHnawd0F%2FvDKZLaLtX22T8Mmo9CWpwXA64InNO5Jj1jw%2F23i1bhUE5aeQ7PlO%2FuYRlHXivDmkLijO%2FHD4fgNMe8NAb8SnhigmHVb8VYQFBndH%2FHMPn7%2BrHujnTc3QQD4EJ6DFShrTxIRoDgESEpfLAYzxTdWlxUXgvzrH9p%2Bgl3y8Jp6K%2Fc6Ea8T75ppT2YFdpQ6lY&X-Amz-Signature=0114021700dd8997da1b4b94204579e6ada0063664dedafa9900a303ddeefa41&X-Amz-SignedHeaders=host&x-id=GetObject)
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


