

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDHHRERK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCB6%2BJ6LWAtMG7yq78%2FHKy%2BSxkcemINW%2FHUV%2BKOZQex%2FgIgDOwqxDhi6ZgOmHGhNzCDbmBxAk%2FbvVQmX8ayEot0euwqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB55%2FT0zNtHMgP9FoCrcA3A%2FPDt%2Fd8I36oA4WlOhW31A0K2qNUaS6xdsvdKl1A%2FRRAEfmxr4bGW0OClvmxtFRPH2vyUFFgQt2ics5ZriIsJSf4XCxmzna8mjgLyhzNHxxAhAqRXWvlSdIqU6Dw%2BciQCpGfi5ciyh7jgxaX5gzzUzKLA0pmZTtV3g7V4C9SMva4skkqLX%2FcYDA%2BvqP9%2FHHonHhu9WGKmdU30VCB8pT0LcgkgQzsFfvUJcuQQr9ifyXVsIaCeL64eKEUURpgJBV1x%2BCQ%2BKUuI0WISQJbhj4me0d3he9ti%2B7xBDe8OR8bTEXBRF4rsvHR6eBwCGU%2FSNo1TYXvvjgyu5nXm7o73V9s6oTlrnKXMr%2FKyFHqzDCjGAT3805sZ03GjkE79aunmuVXhuWM2kG%2BfrHGFBRsxHzDpalziIUWji8tjCzsIZ2Lly09LYdy6D9NF0dlzmnRmQ%2BoPp3FWwhsQ0RlYBW0mM%2F6vZOPSGPWs13MrYSGhrWI9qh9uofugY3YFJt1UqZ0il37n6c8n5Lsnv3jBNkY%2BSA0gzP6teYV0RG9i4mIRYOpxTfj0uuYevsc3nQTqw58Hj2eP0Ywd6hR5XTib5lToKsPEZMwPqUYFPnZyAgsBGYj651qEjAUIz1Qb7X%2Fb4MPf06bwGOqUB6QdnpAMEGVpZy7duHj5dFLrVQcMW%2Bgfs4bLemI6Kx%2BbQv5kxJTg1d6acCp1Q2x2MX4PPWUr8fhuVVk5H65HHfmrID8wfUssGnbuDRNmv9PgreJqZ3x67nJT8joJWjW%2BlQV9rEzJLvXV2DSvqiyBAqgFRsS58VUFVnaPqvRlf1Zeh50idVut1jv8vzvD6Sj2prOYqSsN2U%2Ftj%2Fyz5UOLpLpYZGJaG&X-Amz-Signature=da1fbf534e13e1055a0ba6c79ddbaea866371433c059677b7d2865fd1ad20bda&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHYFIPOS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDXEiShJwuLdCERlR5oJhbXy7obqF3j9Umdq6V%2F93dDYAiAwctCbnc2he7wnN2EsQ4GOm25oSrW6gjugk%2Fhwh2b1iyqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiu88p%2FGY6Ry%2BlawXKtwDlRQYi5vmt6LMpxbAyihABo73J%2BR8v%2FskN%2FmB3lTogJk3eMUzpfHzbsSx9uZT99wHLmtv4rys3qzeUtuZACw1xq6t38srkFa73pj5vO8ALpZkoi2Yqdg3oQew2ENPx2ge5zRTgVR%2FQ%2BtniA3X%2Bhvf8H7wMzDPLcFq9X%2Bce6zk6TAZMAyltQ3127D%2Fmw53dWvC%2FFBMwULrrtojLRoyIb2H4k2fg7tZAjw2aEHgTYN9X%2BWu6ZSTV%2FIwxkCmMc56ID42A0Xm8%2FhZlY4SO2PCFz16Hid3sUSOxuaMU3ozDhVacsOMQdCMWXWhTNbVyJouniHyhbWkplRBMCVvPksJ4N4mNZ2%2FcHWiVnzt5amQ6hFzefp530c4j9q%2BthsjOrpZXlr0ZzpRYgcRT5xvsVu8Qh78539C%2BsjujjDii5ovuRF3RDBHZkvf4jEX0M0u9no09vQVxCSHPWpVeYYPivxUaFkJUnIopa2SLg3%2BFfqYtFFbMNC5yeAZ2svMRC3c9JFsNLfnIEgOTaqlTI9WWFpaxtA1KcS8xvnEi57q%2FVKrww7MseNF7BwGO%2FwWJ3s4kt7gY17ZaYRlat8tGxPe0ZigqKTFFqZIlCUm%2FjbQdbGMSbF%2F02b9VPuhOdsb4kk47kMw4PTpvAY6pgGc3Pq7GyAmy%2FoQICEDup4Dl6GKoXhlHenzGQtZLjRCc37zujbguaj0wcEtRuXbiFTYZJo2S0kVax%2B1YpcRfH26KhtpoWMylsqEcB0ker1qNcOC6kRcgv1aI7XuB6Ybo9LdsZB8XR41umstsb5LOdPiqoD%2F58khmZOfQMcuvoVOtQFj8bN5z%2FCBdnZVzGlisO%2Fa%2BIAyEEC3Os7bc2hK3Z7wBg0YhUx%2F&X-Amz-Signature=102c841f822ee7bfd1cbf74edfc1b5b20f52f426d80f8f4ffc7fef1245262638&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHYFIPOS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDXEiShJwuLdCERlR5oJhbXy7obqF3j9Umdq6V%2F93dDYAiAwctCbnc2he7wnN2EsQ4GOm25oSrW6gjugk%2Fhwh2b1iyqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiu88p%2FGY6Ry%2BlawXKtwDlRQYi5vmt6LMpxbAyihABo73J%2BR8v%2FskN%2FmB3lTogJk3eMUzpfHzbsSx9uZT99wHLmtv4rys3qzeUtuZACw1xq6t38srkFa73pj5vO8ALpZkoi2Yqdg3oQew2ENPx2ge5zRTgVR%2FQ%2BtniA3X%2Bhvf8H7wMzDPLcFq9X%2Bce6zk6TAZMAyltQ3127D%2Fmw53dWvC%2FFBMwULrrtojLRoyIb2H4k2fg7tZAjw2aEHgTYN9X%2BWu6ZSTV%2FIwxkCmMc56ID42A0Xm8%2FhZlY4SO2PCFz16Hid3sUSOxuaMU3ozDhVacsOMQdCMWXWhTNbVyJouniHyhbWkplRBMCVvPksJ4N4mNZ2%2FcHWiVnzt5amQ6hFzefp530c4j9q%2BthsjOrpZXlr0ZzpRYgcRT5xvsVu8Qh78539C%2BsjujjDii5ovuRF3RDBHZkvf4jEX0M0u9no09vQVxCSHPWpVeYYPivxUaFkJUnIopa2SLg3%2BFfqYtFFbMNC5yeAZ2svMRC3c9JFsNLfnIEgOTaqlTI9WWFpaxtA1KcS8xvnEi57q%2FVKrww7MseNF7BwGO%2FwWJ3s4kt7gY17ZaYRlat8tGxPe0ZigqKTFFqZIlCUm%2FjbQdbGMSbF%2F02b9VPuhOdsb4kk47kMw4PTpvAY6pgGc3Pq7GyAmy%2FoQICEDup4Dl6GKoXhlHenzGQtZLjRCc37zujbguaj0wcEtRuXbiFTYZJo2S0kVax%2B1YpcRfH26KhtpoWMylsqEcB0ker1qNcOC6kRcgv1aI7XuB6Ybo9LdsZB8XR41umstsb5LOdPiqoD%2F58khmZOfQMcuvoVOtQFj8bN5z%2FCBdnZVzGlisO%2Fa%2BIAyEEC3Os7bc2hK3Z7wBg0YhUx%2F&X-Amz-Signature=45fc4f3a1d74d6f20a51675928d9a8575da5d6e4d8f4b93dc066f1f3f68e53df&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHYFIPOS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDXEiShJwuLdCERlR5oJhbXy7obqF3j9Umdq6V%2F93dDYAiAwctCbnc2he7wnN2EsQ4GOm25oSrW6gjugk%2Fhwh2b1iyqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiu88p%2FGY6Ry%2BlawXKtwDlRQYi5vmt6LMpxbAyihABo73J%2BR8v%2FskN%2FmB3lTogJk3eMUzpfHzbsSx9uZT99wHLmtv4rys3qzeUtuZACw1xq6t38srkFa73pj5vO8ALpZkoi2Yqdg3oQew2ENPx2ge5zRTgVR%2FQ%2BtniA3X%2Bhvf8H7wMzDPLcFq9X%2Bce6zk6TAZMAyltQ3127D%2Fmw53dWvC%2FFBMwULrrtojLRoyIb2H4k2fg7tZAjw2aEHgTYN9X%2BWu6ZSTV%2FIwxkCmMc56ID42A0Xm8%2FhZlY4SO2PCFz16Hid3sUSOxuaMU3ozDhVacsOMQdCMWXWhTNbVyJouniHyhbWkplRBMCVvPksJ4N4mNZ2%2FcHWiVnzt5amQ6hFzefp530c4j9q%2BthsjOrpZXlr0ZzpRYgcRT5xvsVu8Qh78539C%2BsjujjDii5ovuRF3RDBHZkvf4jEX0M0u9no09vQVxCSHPWpVeYYPivxUaFkJUnIopa2SLg3%2BFfqYtFFbMNC5yeAZ2svMRC3c9JFsNLfnIEgOTaqlTI9WWFpaxtA1KcS8xvnEi57q%2FVKrww7MseNF7BwGO%2FwWJ3s4kt7gY17ZaYRlat8tGxPe0ZigqKTFFqZIlCUm%2FjbQdbGMSbF%2F02b9VPuhOdsb4kk47kMw4PTpvAY6pgGc3Pq7GyAmy%2FoQICEDup4Dl6GKoXhlHenzGQtZLjRCc37zujbguaj0wcEtRuXbiFTYZJo2S0kVax%2B1YpcRfH26KhtpoWMylsqEcB0ker1qNcOC6kRcgv1aI7XuB6Ybo9LdsZB8XR41umstsb5LOdPiqoD%2F58khmZOfQMcuvoVOtQFj8bN5z%2FCBdnZVzGlisO%2Fa%2BIAyEEC3Os7bc2hK3Z7wBg0YhUx%2F&X-Amz-Signature=02af6c92d3abeacf812cf0df5b5df67c3bd3d4171ebccea458e28598f7b732ff&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHYFIPOS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDXEiShJwuLdCERlR5oJhbXy7obqF3j9Umdq6V%2F93dDYAiAwctCbnc2he7wnN2EsQ4GOm25oSrW6gjugk%2Fhwh2b1iyqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiu88p%2FGY6Ry%2BlawXKtwDlRQYi5vmt6LMpxbAyihABo73J%2BR8v%2FskN%2FmB3lTogJk3eMUzpfHzbsSx9uZT99wHLmtv4rys3qzeUtuZACw1xq6t38srkFa73pj5vO8ALpZkoi2Yqdg3oQew2ENPx2ge5zRTgVR%2FQ%2BtniA3X%2Bhvf8H7wMzDPLcFq9X%2Bce6zk6TAZMAyltQ3127D%2Fmw53dWvC%2FFBMwULrrtojLRoyIb2H4k2fg7tZAjw2aEHgTYN9X%2BWu6ZSTV%2FIwxkCmMc56ID42A0Xm8%2FhZlY4SO2PCFz16Hid3sUSOxuaMU3ozDhVacsOMQdCMWXWhTNbVyJouniHyhbWkplRBMCVvPksJ4N4mNZ2%2FcHWiVnzt5amQ6hFzefp530c4j9q%2BthsjOrpZXlr0ZzpRYgcRT5xvsVu8Qh78539C%2BsjujjDii5ovuRF3RDBHZkvf4jEX0M0u9no09vQVxCSHPWpVeYYPivxUaFkJUnIopa2SLg3%2BFfqYtFFbMNC5yeAZ2svMRC3c9JFsNLfnIEgOTaqlTI9WWFpaxtA1KcS8xvnEi57q%2FVKrww7MseNF7BwGO%2FwWJ3s4kt7gY17ZaYRlat8tGxPe0ZigqKTFFqZIlCUm%2FjbQdbGMSbF%2F02b9VPuhOdsb4kk47kMw4PTpvAY6pgGc3Pq7GyAmy%2FoQICEDup4Dl6GKoXhlHenzGQtZLjRCc37zujbguaj0wcEtRuXbiFTYZJo2S0kVax%2B1YpcRfH26KhtpoWMylsqEcB0ker1qNcOC6kRcgv1aI7XuB6Ybo9LdsZB8XR41umstsb5LOdPiqoD%2F58khmZOfQMcuvoVOtQFj8bN5z%2FCBdnZVzGlisO%2Fa%2BIAyEEC3Os7bc2hK3Z7wBg0YhUx%2F&X-Amz-Signature=28f5d7308a95937fbe42095070b225bee43cf36596e6c065ec5eaf445727e5ef&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHYFIPOS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDXEiShJwuLdCERlR5oJhbXy7obqF3j9Umdq6V%2F93dDYAiAwctCbnc2he7wnN2EsQ4GOm25oSrW6gjugk%2Fhwh2b1iyqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiu88p%2FGY6Ry%2BlawXKtwDlRQYi5vmt6LMpxbAyihABo73J%2BR8v%2FskN%2FmB3lTogJk3eMUzpfHzbsSx9uZT99wHLmtv4rys3qzeUtuZACw1xq6t38srkFa73pj5vO8ALpZkoi2Yqdg3oQew2ENPx2ge5zRTgVR%2FQ%2BtniA3X%2Bhvf8H7wMzDPLcFq9X%2Bce6zk6TAZMAyltQ3127D%2Fmw53dWvC%2FFBMwULrrtojLRoyIb2H4k2fg7tZAjw2aEHgTYN9X%2BWu6ZSTV%2FIwxkCmMc56ID42A0Xm8%2FhZlY4SO2PCFz16Hid3sUSOxuaMU3ozDhVacsOMQdCMWXWhTNbVyJouniHyhbWkplRBMCVvPksJ4N4mNZ2%2FcHWiVnzt5amQ6hFzefp530c4j9q%2BthsjOrpZXlr0ZzpRYgcRT5xvsVu8Qh78539C%2BsjujjDii5ovuRF3RDBHZkvf4jEX0M0u9no09vQVxCSHPWpVeYYPivxUaFkJUnIopa2SLg3%2BFfqYtFFbMNC5yeAZ2svMRC3c9JFsNLfnIEgOTaqlTI9WWFpaxtA1KcS8xvnEi57q%2FVKrww7MseNF7BwGO%2FwWJ3s4kt7gY17ZaYRlat8tGxPe0ZigqKTFFqZIlCUm%2FjbQdbGMSbF%2F02b9VPuhOdsb4kk47kMw4PTpvAY6pgGc3Pq7GyAmy%2FoQICEDup4Dl6GKoXhlHenzGQtZLjRCc37zujbguaj0wcEtRuXbiFTYZJo2S0kVax%2B1YpcRfH26KhtpoWMylsqEcB0ker1qNcOC6kRcgv1aI7XuB6Ybo9LdsZB8XR41umstsb5LOdPiqoD%2F58khmZOfQMcuvoVOtQFj8bN5z%2FCBdnZVzGlisO%2Fa%2BIAyEEC3Os7bc2hK3Z7wBg0YhUx%2F&X-Amz-Signature=4234eb2f4b4e5ed36ecc97697d87be40b279b4c784d88ae044499031a100b76d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDHHRERK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCB6%2BJ6LWAtMG7yq78%2FHKy%2BSxkcemINW%2FHUV%2BKOZQex%2FgIgDOwqxDhi6ZgOmHGhNzCDbmBxAk%2FbvVQmX8ayEot0euwqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB55%2FT0zNtHMgP9FoCrcA3A%2FPDt%2Fd8I36oA4WlOhW31A0K2qNUaS6xdsvdKl1A%2FRRAEfmxr4bGW0OClvmxtFRPH2vyUFFgQt2ics5ZriIsJSf4XCxmzna8mjgLyhzNHxxAhAqRXWvlSdIqU6Dw%2BciQCpGfi5ciyh7jgxaX5gzzUzKLA0pmZTtV3g7V4C9SMva4skkqLX%2FcYDA%2BvqP9%2FHHonHhu9WGKmdU30VCB8pT0LcgkgQzsFfvUJcuQQr9ifyXVsIaCeL64eKEUURpgJBV1x%2BCQ%2BKUuI0WISQJbhj4me0d3he9ti%2B7xBDe8OR8bTEXBRF4rsvHR6eBwCGU%2FSNo1TYXvvjgyu5nXm7o73V9s6oTlrnKXMr%2FKyFHqzDCjGAT3805sZ03GjkE79aunmuVXhuWM2kG%2BfrHGFBRsxHzDpalziIUWji8tjCzsIZ2Lly09LYdy6D9NF0dlzmnRmQ%2BoPp3FWwhsQ0RlYBW0mM%2F6vZOPSGPWs13MrYSGhrWI9qh9uofugY3YFJt1UqZ0il37n6c8n5Lsnv3jBNkY%2BSA0gzP6teYV0RG9i4mIRYOpxTfj0uuYevsc3nQTqw58Hj2eP0Ywd6hR5XTib5lToKsPEZMwPqUYFPnZyAgsBGYj651qEjAUIz1Qb7X%2Fb4MPf06bwGOqUB6QdnpAMEGVpZy7duHj5dFLrVQcMW%2Bgfs4bLemI6Kx%2BbQv5kxJTg1d6acCp1Q2x2MX4PPWUr8fhuVVk5H65HHfmrID8wfUssGnbuDRNmv9PgreJqZ3x67nJT8joJWjW%2BlQV9rEzJLvXV2DSvqiyBAqgFRsS58VUFVnaPqvRlf1Zeh50idVut1jv8vzvD6Sj2prOYqSsN2U%2Ftj%2Fyz5UOLpLpYZGJaG&X-Amz-Signature=579898e96fde448c93b038d0b08c5a46b6ef305dd18af3c5e2bda3e713e655fd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDHHRERK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCB6%2BJ6LWAtMG7yq78%2FHKy%2BSxkcemINW%2FHUV%2BKOZQex%2FgIgDOwqxDhi6ZgOmHGhNzCDbmBxAk%2FbvVQmX8ayEot0euwqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB55%2FT0zNtHMgP9FoCrcA3A%2FPDt%2Fd8I36oA4WlOhW31A0K2qNUaS6xdsvdKl1A%2FRRAEfmxr4bGW0OClvmxtFRPH2vyUFFgQt2ics5ZriIsJSf4XCxmzna8mjgLyhzNHxxAhAqRXWvlSdIqU6Dw%2BciQCpGfi5ciyh7jgxaX5gzzUzKLA0pmZTtV3g7V4C9SMva4skkqLX%2FcYDA%2BvqP9%2FHHonHhu9WGKmdU30VCB8pT0LcgkgQzsFfvUJcuQQr9ifyXVsIaCeL64eKEUURpgJBV1x%2BCQ%2BKUuI0WISQJbhj4me0d3he9ti%2B7xBDe8OR8bTEXBRF4rsvHR6eBwCGU%2FSNo1TYXvvjgyu5nXm7o73V9s6oTlrnKXMr%2FKyFHqzDCjGAT3805sZ03GjkE79aunmuVXhuWM2kG%2BfrHGFBRsxHzDpalziIUWji8tjCzsIZ2Lly09LYdy6D9NF0dlzmnRmQ%2BoPp3FWwhsQ0RlYBW0mM%2F6vZOPSGPWs13MrYSGhrWI9qh9uofugY3YFJt1UqZ0il37n6c8n5Lsnv3jBNkY%2BSA0gzP6teYV0RG9i4mIRYOpxTfj0uuYevsc3nQTqw58Hj2eP0Ywd6hR5XTib5lToKsPEZMwPqUYFPnZyAgsBGYj651qEjAUIz1Qb7X%2Fb4MPf06bwGOqUB6QdnpAMEGVpZy7duHj5dFLrVQcMW%2Bgfs4bLemI6Kx%2BbQv5kxJTg1d6acCp1Q2x2MX4PPWUr8fhuVVk5H65HHfmrID8wfUssGnbuDRNmv9PgreJqZ3x67nJT8joJWjW%2BlQV9rEzJLvXV2DSvqiyBAqgFRsS58VUFVnaPqvRlf1Zeh50idVut1jv8vzvD6Sj2prOYqSsN2U%2Ftj%2Fyz5UOLpLpYZGJaG&X-Amz-Signature=ecf5395ce45cfb177ec1a0cd4f1be0ba24a5ab75957ca524e7f43b3b25ca2377&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDHHRERK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCB6%2BJ6LWAtMG7yq78%2FHKy%2BSxkcemINW%2FHUV%2BKOZQex%2FgIgDOwqxDhi6ZgOmHGhNzCDbmBxAk%2FbvVQmX8ayEot0euwqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB55%2FT0zNtHMgP9FoCrcA3A%2FPDt%2Fd8I36oA4WlOhW31A0K2qNUaS6xdsvdKl1A%2FRRAEfmxr4bGW0OClvmxtFRPH2vyUFFgQt2ics5ZriIsJSf4XCxmzna8mjgLyhzNHxxAhAqRXWvlSdIqU6Dw%2BciQCpGfi5ciyh7jgxaX5gzzUzKLA0pmZTtV3g7V4C9SMva4skkqLX%2FcYDA%2BvqP9%2FHHonHhu9WGKmdU30VCB8pT0LcgkgQzsFfvUJcuQQr9ifyXVsIaCeL64eKEUURpgJBV1x%2BCQ%2BKUuI0WISQJbhj4me0d3he9ti%2B7xBDe8OR8bTEXBRF4rsvHR6eBwCGU%2FSNo1TYXvvjgyu5nXm7o73V9s6oTlrnKXMr%2FKyFHqzDCjGAT3805sZ03GjkE79aunmuVXhuWM2kG%2BfrHGFBRsxHzDpalziIUWji8tjCzsIZ2Lly09LYdy6D9NF0dlzmnRmQ%2BoPp3FWwhsQ0RlYBW0mM%2F6vZOPSGPWs13MrYSGhrWI9qh9uofugY3YFJt1UqZ0il37n6c8n5Lsnv3jBNkY%2BSA0gzP6teYV0RG9i4mIRYOpxTfj0uuYevsc3nQTqw58Hj2eP0Ywd6hR5XTib5lToKsPEZMwPqUYFPnZyAgsBGYj651qEjAUIz1Qb7X%2Fb4MPf06bwGOqUB6QdnpAMEGVpZy7duHj5dFLrVQcMW%2Bgfs4bLemI6Kx%2BbQv5kxJTg1d6acCp1Q2x2MX4PPWUr8fhuVVk5H65HHfmrID8wfUssGnbuDRNmv9PgreJqZ3x67nJT8joJWjW%2BlQV9rEzJLvXV2DSvqiyBAqgFRsS58VUFVnaPqvRlf1Zeh50idVut1jv8vzvD6Sj2prOYqSsN2U%2Ftj%2Fyz5UOLpLpYZGJaG&X-Amz-Signature=4c6b76104e1c00374694a4f168b3eff560e3fd132a224a1a09fb08fc546e45b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDHHRERK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCB6%2BJ6LWAtMG7yq78%2FHKy%2BSxkcemINW%2FHUV%2BKOZQex%2FgIgDOwqxDhi6ZgOmHGhNzCDbmBxAk%2FbvVQmX8ayEot0euwqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB55%2FT0zNtHMgP9FoCrcA3A%2FPDt%2Fd8I36oA4WlOhW31A0K2qNUaS6xdsvdKl1A%2FRRAEfmxr4bGW0OClvmxtFRPH2vyUFFgQt2ics5ZriIsJSf4XCxmzna8mjgLyhzNHxxAhAqRXWvlSdIqU6Dw%2BciQCpGfi5ciyh7jgxaX5gzzUzKLA0pmZTtV3g7V4C9SMva4skkqLX%2FcYDA%2BvqP9%2FHHonHhu9WGKmdU30VCB8pT0LcgkgQzsFfvUJcuQQr9ifyXVsIaCeL64eKEUURpgJBV1x%2BCQ%2BKUuI0WISQJbhj4me0d3he9ti%2B7xBDe8OR8bTEXBRF4rsvHR6eBwCGU%2FSNo1TYXvvjgyu5nXm7o73V9s6oTlrnKXMr%2FKyFHqzDCjGAT3805sZ03GjkE79aunmuVXhuWM2kG%2BfrHGFBRsxHzDpalziIUWji8tjCzsIZ2Lly09LYdy6D9NF0dlzmnRmQ%2BoPp3FWwhsQ0RlYBW0mM%2F6vZOPSGPWs13MrYSGhrWI9qh9uofugY3YFJt1UqZ0il37n6c8n5Lsnv3jBNkY%2BSA0gzP6teYV0RG9i4mIRYOpxTfj0uuYevsc3nQTqw58Hj2eP0Ywd6hR5XTib5lToKsPEZMwPqUYFPnZyAgsBGYj651qEjAUIz1Qb7X%2Fb4MPf06bwGOqUB6QdnpAMEGVpZy7duHj5dFLrVQcMW%2Bgfs4bLemI6Kx%2BbQv5kxJTg1d6acCp1Q2x2MX4PPWUr8fhuVVk5H65HHfmrID8wfUssGnbuDRNmv9PgreJqZ3x67nJT8joJWjW%2BlQV9rEzJLvXV2DSvqiyBAqgFRsS58VUFVnaPqvRlf1Zeh50idVut1jv8vzvD6Sj2prOYqSsN2U%2Ftj%2Fyz5UOLpLpYZGJaG&X-Amz-Signature=79ece1034001f0eeba1b5ffe54871765ce85c19d287d309f45abc8ff8ca3df8a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDHHRERK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCB6%2BJ6LWAtMG7yq78%2FHKy%2BSxkcemINW%2FHUV%2BKOZQex%2FgIgDOwqxDhi6ZgOmHGhNzCDbmBxAk%2FbvVQmX8ayEot0euwqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB55%2FT0zNtHMgP9FoCrcA3A%2FPDt%2Fd8I36oA4WlOhW31A0K2qNUaS6xdsvdKl1A%2FRRAEfmxr4bGW0OClvmxtFRPH2vyUFFgQt2ics5ZriIsJSf4XCxmzna8mjgLyhzNHxxAhAqRXWvlSdIqU6Dw%2BciQCpGfi5ciyh7jgxaX5gzzUzKLA0pmZTtV3g7V4C9SMva4skkqLX%2FcYDA%2BvqP9%2FHHonHhu9WGKmdU30VCB8pT0LcgkgQzsFfvUJcuQQr9ifyXVsIaCeL64eKEUURpgJBV1x%2BCQ%2BKUuI0WISQJbhj4me0d3he9ti%2B7xBDe8OR8bTEXBRF4rsvHR6eBwCGU%2FSNo1TYXvvjgyu5nXm7o73V9s6oTlrnKXMr%2FKyFHqzDCjGAT3805sZ03GjkE79aunmuVXhuWM2kG%2BfrHGFBRsxHzDpalziIUWji8tjCzsIZ2Lly09LYdy6D9NF0dlzmnRmQ%2BoPp3FWwhsQ0RlYBW0mM%2F6vZOPSGPWs13MrYSGhrWI9qh9uofugY3YFJt1UqZ0il37n6c8n5Lsnv3jBNkY%2BSA0gzP6teYV0RG9i4mIRYOpxTfj0uuYevsc3nQTqw58Hj2eP0Ywd6hR5XTib5lToKsPEZMwPqUYFPnZyAgsBGYj651qEjAUIz1Qb7X%2Fb4MPf06bwGOqUB6QdnpAMEGVpZy7duHj5dFLrVQcMW%2Bgfs4bLemI6Kx%2BbQv5kxJTg1d6acCp1Q2x2MX4PPWUr8fhuVVk5H65HHfmrID8wfUssGnbuDRNmv9PgreJqZ3x67nJT8joJWjW%2BlQV9rEzJLvXV2DSvqiyBAqgFRsS58VUFVnaPqvRlf1Zeh50idVut1jv8vzvD6Sj2prOYqSsN2U%2Ftj%2Fyz5UOLpLpYZGJaG&X-Amz-Signature=8ee8cca94552f2d63e536248c5d5344d028c66dc73d939db065e7b50fa433176&X-Amz-SignedHeaders=host&x-id=GetObject)
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


