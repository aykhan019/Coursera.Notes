

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSGJGQLE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIFq%2FWdvJm%2F7gkoSjUvIDp9TYGcfZIfm1qIYbjEiv52LIAiEAxyqlW7JDwdmycUrCmRc77BctT5EsBmWh8%2FAEVQkKM%2FUq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDHDaX7uGgNslB48PkCrcA8OaLG9D5vclF5zQqWeTEpW8wJ5jokwAqWKzhhsUx%2Fv%2BiTB7E8xiXBwtRhUk1SNYOJ%2Fv2MB6thlX6aDv6kXoXjeMr89JbMRaw9qiYNUs54%2BnYrogHTHnoDEv259Vzw2wBUQNDVB60H%2FLvpZKJo5f6rT55301zpQgGs4KCQeAQ7eaDNagNXBije7rgtTznr5bSnkgOUCg41pEWbJnNcZ8ZUI1PVKZHuIs3RlRnYRFA3jZ5XzPfRhyJSPfG%2FjCfdUH1I3ZcJukH%2F4fKQnB1dYuGTIHGuoaDuHQhgRUx9W1tlXAN%2FzGOLga%2BnWfxidD8sHeFTGSOuwSEVAu9kVN9ScrpPX%2FmmGwxWB%2FQZsFuWYXXX5KExZpJcJWm4QlY58YWKQqs5XhUbsJ637MWgo47pTumRhvBEmfmSCUTdBwE64aEYWt%2FRSveISLweBHWBypJ14JK8zJoQfSxpHeSZjcrWC1qOJ8wYd5lw5261abZa%2F%2Bsa1eHbevo8Bsq8KJ0mYF3na5WwJKmdIml1OzkQxS%2BD%2BavkKR8Lb1Mby%2BnvveOaRp686oK44yR0xWgPbg%2FJO362nW9IVX9NAexIHYhzT1zi4JK0hY4gfSUHGihthAaHI8qSE5uq8JLIa3LLKytuj8MM3Nhb0GOqUB2%2B1xhFMA%2B7f89JBQ%2BZON4rvgXQZpwTK2Oop6k8le94il%2FTSp40BKD5G6uWluGPauf%2BYXWQuQ91E6VDpPiZjEngfswCHBALzel7hCWqUK%2FBosdlDbk99hHDAlcqJN%2BNONdE%2BULEw4ZimLqZXEiov1WJzkd%2BK%2F4fsyJhJ5%2FHjH67NikYUGuIVwWFPEkBwJAkRsvcpV1dDmt0QFkR9eZt1IpVkCLCnT&X-Amz-Signature=c98976accf318fec03f19db33eeaf6259b9cfb1ac2abf9f7391da946c4a95dc9&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645AFX35M%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFerGr0SFdDv8bYrGyUkYGzkmqrKIe99%2B%2FArj%2F8RWRsnAiBdmhfZl50uHIHpAmlhEI3rRlKeAPruj7D2caocGRkv4Sr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMG1WbxmC5HtaX5dyCKtwDnQbewlYbPOWlMryoEc6I1aRSJha8yxAAhPaIkRRypf7rkPqo3KaZ134Cys91pNn14gVZ8HeIiry52sTnfhDuZ0Kg8wIQWt8nBD68hdIBVe7NC%2BDg%2Bw8QWz04kiHN9pPedmPTylbE7PoBE5Y69hycp3U5tozylLP13zLj91kKHyM5LofkoJBf%2BDhCPsj15a%2FKGORk6MNeN81vPvaXOF%2FCvf1xWs%2B56Aiz3eF43msUGAvh%2BM6ugk3rO%2FLtYUOKQkwLdSV0WOubgOKjuCYSoxjeQU2utl2Jkt8cnT7oxOwklZXGxJYH21fuK%2B7E2Nh7IbaQJd%2BNqNY%2FYNBJJSCPS1Ii0fTi0Bzmxqw6%2BT9wtQAYz%2F77jO58Gleww9ZZ0qWF%2B%2BZ0Dv%2BxInRiORvXxnmTKCSPfVPUP6PTV8RI7D3kQH2fMVR5Or7pwyaQ9nPbZsEBUbRsT5E6Op%2BGudzcAwqkl5HZPz9%2BLQHdrjeB9SrcTqAJmzZpkmRVz8Vn4%2Fjv8s%2F%2Bvq5ll658fqn39WzBN1LZqcdEDL87RmCJ8CYyaoOYzb86lVEwQpyLVwtKsVQtU0iLSf%2BpL3uOLDZvG7jI0eXkau6wrfuvH4eqTAEOhJeptHiwWZhR8pl8PjwuVII1G1Mw58yFvQY6pgEyx6YXrI0n1aB8oGyBXSmQgFRks1%2F8QDx2NDSmguh9UqPhzoDBuGPcHrBfCMnAxnOxH7C3%2BM2QskZhcOVNV5fgkJ51DYPaMz82yEVZiTy0sB4IZgMuTpbh52ZAJ6HXcDIneI%2B3qX65XCM0nF6iTT6t2VEGD%2BaSwLZscTaqV7BrsYIdh5dwFJyw0rm%2BPbsmoFIL6iDOriSFqH84lxV2OiqTIdj9MXFp&X-Amz-Signature=4a173c8845c32ab8cc0aba1c8a7158b8b85e9184aeb683f6ab0e6c9994c5acb1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645AFX35M%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFerGr0SFdDv8bYrGyUkYGzkmqrKIe99%2B%2FArj%2F8RWRsnAiBdmhfZl50uHIHpAmlhEI3rRlKeAPruj7D2caocGRkv4Sr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMG1WbxmC5HtaX5dyCKtwDnQbewlYbPOWlMryoEc6I1aRSJha8yxAAhPaIkRRypf7rkPqo3KaZ134Cys91pNn14gVZ8HeIiry52sTnfhDuZ0Kg8wIQWt8nBD68hdIBVe7NC%2BDg%2Bw8QWz04kiHN9pPedmPTylbE7PoBE5Y69hycp3U5tozylLP13zLj91kKHyM5LofkoJBf%2BDhCPsj15a%2FKGORk6MNeN81vPvaXOF%2FCvf1xWs%2B56Aiz3eF43msUGAvh%2BM6ugk3rO%2FLtYUOKQkwLdSV0WOubgOKjuCYSoxjeQU2utl2Jkt8cnT7oxOwklZXGxJYH21fuK%2B7E2Nh7IbaQJd%2BNqNY%2FYNBJJSCPS1Ii0fTi0Bzmxqw6%2BT9wtQAYz%2F77jO58Gleww9ZZ0qWF%2B%2BZ0Dv%2BxInRiORvXxnmTKCSPfVPUP6PTV8RI7D3kQH2fMVR5Or7pwyaQ9nPbZsEBUbRsT5E6Op%2BGudzcAwqkl5HZPz9%2BLQHdrjeB9SrcTqAJmzZpkmRVz8Vn4%2Fjv8s%2F%2Bvq5ll658fqn39WzBN1LZqcdEDL87RmCJ8CYyaoOYzb86lVEwQpyLVwtKsVQtU0iLSf%2BpL3uOLDZvG7jI0eXkau6wrfuvH4eqTAEOhJeptHiwWZhR8pl8PjwuVII1G1Mw58yFvQY6pgEyx6YXrI0n1aB8oGyBXSmQgFRks1%2F8QDx2NDSmguh9UqPhzoDBuGPcHrBfCMnAxnOxH7C3%2BM2QskZhcOVNV5fgkJ51DYPaMz82yEVZiTy0sB4IZgMuTpbh52ZAJ6HXcDIneI%2B3qX65XCM0nF6iTT6t2VEGD%2BaSwLZscTaqV7BrsYIdh5dwFJyw0rm%2BPbsmoFIL6iDOriSFqH84lxV2OiqTIdj9MXFp&X-Amz-Signature=735c5ea5f53074f773f372cfe3ca44567dd6bf15802544336d3bc843ec8f6703&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645AFX35M%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFerGr0SFdDv8bYrGyUkYGzkmqrKIe99%2B%2FArj%2F8RWRsnAiBdmhfZl50uHIHpAmlhEI3rRlKeAPruj7D2caocGRkv4Sr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMG1WbxmC5HtaX5dyCKtwDnQbewlYbPOWlMryoEc6I1aRSJha8yxAAhPaIkRRypf7rkPqo3KaZ134Cys91pNn14gVZ8HeIiry52sTnfhDuZ0Kg8wIQWt8nBD68hdIBVe7NC%2BDg%2Bw8QWz04kiHN9pPedmPTylbE7PoBE5Y69hycp3U5tozylLP13zLj91kKHyM5LofkoJBf%2BDhCPsj15a%2FKGORk6MNeN81vPvaXOF%2FCvf1xWs%2B56Aiz3eF43msUGAvh%2BM6ugk3rO%2FLtYUOKQkwLdSV0WOubgOKjuCYSoxjeQU2utl2Jkt8cnT7oxOwklZXGxJYH21fuK%2B7E2Nh7IbaQJd%2BNqNY%2FYNBJJSCPS1Ii0fTi0Bzmxqw6%2BT9wtQAYz%2F77jO58Gleww9ZZ0qWF%2B%2BZ0Dv%2BxInRiORvXxnmTKCSPfVPUP6PTV8RI7D3kQH2fMVR5Or7pwyaQ9nPbZsEBUbRsT5E6Op%2BGudzcAwqkl5HZPz9%2BLQHdrjeB9SrcTqAJmzZpkmRVz8Vn4%2Fjv8s%2F%2Bvq5ll658fqn39WzBN1LZqcdEDL87RmCJ8CYyaoOYzb86lVEwQpyLVwtKsVQtU0iLSf%2BpL3uOLDZvG7jI0eXkau6wrfuvH4eqTAEOhJeptHiwWZhR8pl8PjwuVII1G1Mw58yFvQY6pgEyx6YXrI0n1aB8oGyBXSmQgFRks1%2F8QDx2NDSmguh9UqPhzoDBuGPcHrBfCMnAxnOxH7C3%2BM2QskZhcOVNV5fgkJ51DYPaMz82yEVZiTy0sB4IZgMuTpbh52ZAJ6HXcDIneI%2B3qX65XCM0nF6iTT6t2VEGD%2BaSwLZscTaqV7BrsYIdh5dwFJyw0rm%2BPbsmoFIL6iDOriSFqH84lxV2OiqTIdj9MXFp&X-Amz-Signature=3b070ba8205fabcaad508585b8a5a5228d7cccbff4225f5b1910c72e267493e8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645AFX35M%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFerGr0SFdDv8bYrGyUkYGzkmqrKIe99%2B%2FArj%2F8RWRsnAiBdmhfZl50uHIHpAmlhEI3rRlKeAPruj7D2caocGRkv4Sr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMG1WbxmC5HtaX5dyCKtwDnQbewlYbPOWlMryoEc6I1aRSJha8yxAAhPaIkRRypf7rkPqo3KaZ134Cys91pNn14gVZ8HeIiry52sTnfhDuZ0Kg8wIQWt8nBD68hdIBVe7NC%2BDg%2Bw8QWz04kiHN9pPedmPTylbE7PoBE5Y69hycp3U5tozylLP13zLj91kKHyM5LofkoJBf%2BDhCPsj15a%2FKGORk6MNeN81vPvaXOF%2FCvf1xWs%2B56Aiz3eF43msUGAvh%2BM6ugk3rO%2FLtYUOKQkwLdSV0WOubgOKjuCYSoxjeQU2utl2Jkt8cnT7oxOwklZXGxJYH21fuK%2B7E2Nh7IbaQJd%2BNqNY%2FYNBJJSCPS1Ii0fTi0Bzmxqw6%2BT9wtQAYz%2F77jO58Gleww9ZZ0qWF%2B%2BZ0Dv%2BxInRiORvXxnmTKCSPfVPUP6PTV8RI7D3kQH2fMVR5Or7pwyaQ9nPbZsEBUbRsT5E6Op%2BGudzcAwqkl5HZPz9%2BLQHdrjeB9SrcTqAJmzZpkmRVz8Vn4%2Fjv8s%2F%2Bvq5ll658fqn39WzBN1LZqcdEDL87RmCJ8CYyaoOYzb86lVEwQpyLVwtKsVQtU0iLSf%2BpL3uOLDZvG7jI0eXkau6wrfuvH4eqTAEOhJeptHiwWZhR8pl8PjwuVII1G1Mw58yFvQY6pgEyx6YXrI0n1aB8oGyBXSmQgFRks1%2F8QDx2NDSmguh9UqPhzoDBuGPcHrBfCMnAxnOxH7C3%2BM2QskZhcOVNV5fgkJ51DYPaMz82yEVZiTy0sB4IZgMuTpbh52ZAJ6HXcDIneI%2B3qX65XCM0nF6iTT6t2VEGD%2BaSwLZscTaqV7BrsYIdh5dwFJyw0rm%2BPbsmoFIL6iDOriSFqH84lxV2OiqTIdj9MXFp&X-Amz-Signature=2dcdcb246496fc4542b83c4aa8e7f2010baf57b23fa4504daba3f487f037ff81&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645AFX35M%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFerGr0SFdDv8bYrGyUkYGzkmqrKIe99%2B%2FArj%2F8RWRsnAiBdmhfZl50uHIHpAmlhEI3rRlKeAPruj7D2caocGRkv4Sr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMG1WbxmC5HtaX5dyCKtwDnQbewlYbPOWlMryoEc6I1aRSJha8yxAAhPaIkRRypf7rkPqo3KaZ134Cys91pNn14gVZ8HeIiry52sTnfhDuZ0Kg8wIQWt8nBD68hdIBVe7NC%2BDg%2Bw8QWz04kiHN9pPedmPTylbE7PoBE5Y69hycp3U5tozylLP13zLj91kKHyM5LofkoJBf%2BDhCPsj15a%2FKGORk6MNeN81vPvaXOF%2FCvf1xWs%2B56Aiz3eF43msUGAvh%2BM6ugk3rO%2FLtYUOKQkwLdSV0WOubgOKjuCYSoxjeQU2utl2Jkt8cnT7oxOwklZXGxJYH21fuK%2B7E2Nh7IbaQJd%2BNqNY%2FYNBJJSCPS1Ii0fTi0Bzmxqw6%2BT9wtQAYz%2F77jO58Gleww9ZZ0qWF%2B%2BZ0Dv%2BxInRiORvXxnmTKCSPfVPUP6PTV8RI7D3kQH2fMVR5Or7pwyaQ9nPbZsEBUbRsT5E6Op%2BGudzcAwqkl5HZPz9%2BLQHdrjeB9SrcTqAJmzZpkmRVz8Vn4%2Fjv8s%2F%2Bvq5ll658fqn39WzBN1LZqcdEDL87RmCJ8CYyaoOYzb86lVEwQpyLVwtKsVQtU0iLSf%2BpL3uOLDZvG7jI0eXkau6wrfuvH4eqTAEOhJeptHiwWZhR8pl8PjwuVII1G1Mw58yFvQY6pgEyx6YXrI0n1aB8oGyBXSmQgFRks1%2F8QDx2NDSmguh9UqPhzoDBuGPcHrBfCMnAxnOxH7C3%2BM2QskZhcOVNV5fgkJ51DYPaMz82yEVZiTy0sB4IZgMuTpbh52ZAJ6HXcDIneI%2B3qX65XCM0nF6iTT6t2VEGD%2BaSwLZscTaqV7BrsYIdh5dwFJyw0rm%2BPbsmoFIL6iDOriSFqH84lxV2OiqTIdj9MXFp&X-Amz-Signature=2b0efc357a43303f1fae7ebeb4c666c09d7054db477581edfc82a99d02aac260&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSGJGQLE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIFq%2FWdvJm%2F7gkoSjUvIDp9TYGcfZIfm1qIYbjEiv52LIAiEAxyqlW7JDwdmycUrCmRc77BctT5EsBmWh8%2FAEVQkKM%2FUq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDHDaX7uGgNslB48PkCrcA8OaLG9D5vclF5zQqWeTEpW8wJ5jokwAqWKzhhsUx%2Fv%2BiTB7E8xiXBwtRhUk1SNYOJ%2Fv2MB6thlX6aDv6kXoXjeMr89JbMRaw9qiYNUs54%2BnYrogHTHnoDEv259Vzw2wBUQNDVB60H%2FLvpZKJo5f6rT55301zpQgGs4KCQeAQ7eaDNagNXBije7rgtTznr5bSnkgOUCg41pEWbJnNcZ8ZUI1PVKZHuIs3RlRnYRFA3jZ5XzPfRhyJSPfG%2FjCfdUH1I3ZcJukH%2F4fKQnB1dYuGTIHGuoaDuHQhgRUx9W1tlXAN%2FzGOLga%2BnWfxidD8sHeFTGSOuwSEVAu9kVN9ScrpPX%2FmmGwxWB%2FQZsFuWYXXX5KExZpJcJWm4QlY58YWKQqs5XhUbsJ637MWgo47pTumRhvBEmfmSCUTdBwE64aEYWt%2FRSveISLweBHWBypJ14JK8zJoQfSxpHeSZjcrWC1qOJ8wYd5lw5261abZa%2F%2Bsa1eHbevo8Bsq8KJ0mYF3na5WwJKmdIml1OzkQxS%2BD%2BavkKR8Lb1Mby%2BnvveOaRp686oK44yR0xWgPbg%2FJO362nW9IVX9NAexIHYhzT1zi4JK0hY4gfSUHGihthAaHI8qSE5uq8JLIa3LLKytuj8MM3Nhb0GOqUB2%2B1xhFMA%2B7f89JBQ%2BZON4rvgXQZpwTK2Oop6k8le94il%2FTSp40BKD5G6uWluGPauf%2BYXWQuQ91E6VDpPiZjEngfswCHBALzel7hCWqUK%2FBosdlDbk99hHDAlcqJN%2BNONdE%2BULEw4ZimLqZXEiov1WJzkd%2BK%2F4fsyJhJ5%2FHjH67NikYUGuIVwWFPEkBwJAkRsvcpV1dDmt0QFkR9eZt1IpVkCLCnT&X-Amz-Signature=db6c511078f4cc4d22ef4403d13a2f8894fe07554072d30d867268085682c49e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSGJGQLE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIFq%2FWdvJm%2F7gkoSjUvIDp9TYGcfZIfm1qIYbjEiv52LIAiEAxyqlW7JDwdmycUrCmRc77BctT5EsBmWh8%2FAEVQkKM%2FUq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDHDaX7uGgNslB48PkCrcA8OaLG9D5vclF5zQqWeTEpW8wJ5jokwAqWKzhhsUx%2Fv%2BiTB7E8xiXBwtRhUk1SNYOJ%2Fv2MB6thlX6aDv6kXoXjeMr89JbMRaw9qiYNUs54%2BnYrogHTHnoDEv259Vzw2wBUQNDVB60H%2FLvpZKJo5f6rT55301zpQgGs4KCQeAQ7eaDNagNXBije7rgtTznr5bSnkgOUCg41pEWbJnNcZ8ZUI1PVKZHuIs3RlRnYRFA3jZ5XzPfRhyJSPfG%2FjCfdUH1I3ZcJukH%2F4fKQnB1dYuGTIHGuoaDuHQhgRUx9W1tlXAN%2FzGOLga%2BnWfxidD8sHeFTGSOuwSEVAu9kVN9ScrpPX%2FmmGwxWB%2FQZsFuWYXXX5KExZpJcJWm4QlY58YWKQqs5XhUbsJ637MWgo47pTumRhvBEmfmSCUTdBwE64aEYWt%2FRSveISLweBHWBypJ14JK8zJoQfSxpHeSZjcrWC1qOJ8wYd5lw5261abZa%2F%2Bsa1eHbevo8Bsq8KJ0mYF3na5WwJKmdIml1OzkQxS%2BD%2BavkKR8Lb1Mby%2BnvveOaRp686oK44yR0xWgPbg%2FJO362nW9IVX9NAexIHYhzT1zi4JK0hY4gfSUHGihthAaHI8qSE5uq8JLIa3LLKytuj8MM3Nhb0GOqUB2%2B1xhFMA%2B7f89JBQ%2BZON4rvgXQZpwTK2Oop6k8le94il%2FTSp40BKD5G6uWluGPauf%2BYXWQuQ91E6VDpPiZjEngfswCHBALzel7hCWqUK%2FBosdlDbk99hHDAlcqJN%2BNONdE%2BULEw4ZimLqZXEiov1WJzkd%2BK%2F4fsyJhJ5%2FHjH67NikYUGuIVwWFPEkBwJAkRsvcpV1dDmt0QFkR9eZt1IpVkCLCnT&X-Amz-Signature=8e5253b460667f7887a5cb83fce924115f997045d1ba36bca095f9bc26dfc0c1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSGJGQLE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIFq%2FWdvJm%2F7gkoSjUvIDp9TYGcfZIfm1qIYbjEiv52LIAiEAxyqlW7JDwdmycUrCmRc77BctT5EsBmWh8%2FAEVQkKM%2FUq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDHDaX7uGgNslB48PkCrcA8OaLG9D5vclF5zQqWeTEpW8wJ5jokwAqWKzhhsUx%2Fv%2BiTB7E8xiXBwtRhUk1SNYOJ%2Fv2MB6thlX6aDv6kXoXjeMr89JbMRaw9qiYNUs54%2BnYrogHTHnoDEv259Vzw2wBUQNDVB60H%2FLvpZKJo5f6rT55301zpQgGs4KCQeAQ7eaDNagNXBije7rgtTznr5bSnkgOUCg41pEWbJnNcZ8ZUI1PVKZHuIs3RlRnYRFA3jZ5XzPfRhyJSPfG%2FjCfdUH1I3ZcJukH%2F4fKQnB1dYuGTIHGuoaDuHQhgRUx9W1tlXAN%2FzGOLga%2BnWfxidD8sHeFTGSOuwSEVAu9kVN9ScrpPX%2FmmGwxWB%2FQZsFuWYXXX5KExZpJcJWm4QlY58YWKQqs5XhUbsJ637MWgo47pTumRhvBEmfmSCUTdBwE64aEYWt%2FRSveISLweBHWBypJ14JK8zJoQfSxpHeSZjcrWC1qOJ8wYd5lw5261abZa%2F%2Bsa1eHbevo8Bsq8KJ0mYF3na5WwJKmdIml1OzkQxS%2BD%2BavkKR8Lb1Mby%2BnvveOaRp686oK44yR0xWgPbg%2FJO362nW9IVX9NAexIHYhzT1zi4JK0hY4gfSUHGihthAaHI8qSE5uq8JLIa3LLKytuj8MM3Nhb0GOqUB2%2B1xhFMA%2B7f89JBQ%2BZON4rvgXQZpwTK2Oop6k8le94il%2FTSp40BKD5G6uWluGPauf%2BYXWQuQ91E6VDpPiZjEngfswCHBALzel7hCWqUK%2FBosdlDbk99hHDAlcqJN%2BNONdE%2BULEw4ZimLqZXEiov1WJzkd%2BK%2F4fsyJhJ5%2FHjH67NikYUGuIVwWFPEkBwJAkRsvcpV1dDmt0QFkR9eZt1IpVkCLCnT&X-Amz-Signature=506a0e5c2eaf2413622ebfe4afe27eb860f10ecb451d8cef7752fca841d06153&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSGJGQLE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIFq%2FWdvJm%2F7gkoSjUvIDp9TYGcfZIfm1qIYbjEiv52LIAiEAxyqlW7JDwdmycUrCmRc77BctT5EsBmWh8%2FAEVQkKM%2FUq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDHDaX7uGgNslB48PkCrcA8OaLG9D5vclF5zQqWeTEpW8wJ5jokwAqWKzhhsUx%2Fv%2BiTB7E8xiXBwtRhUk1SNYOJ%2Fv2MB6thlX6aDv6kXoXjeMr89JbMRaw9qiYNUs54%2BnYrogHTHnoDEv259Vzw2wBUQNDVB60H%2FLvpZKJo5f6rT55301zpQgGs4KCQeAQ7eaDNagNXBije7rgtTznr5bSnkgOUCg41pEWbJnNcZ8ZUI1PVKZHuIs3RlRnYRFA3jZ5XzPfRhyJSPfG%2FjCfdUH1I3ZcJukH%2F4fKQnB1dYuGTIHGuoaDuHQhgRUx9W1tlXAN%2FzGOLga%2BnWfxidD8sHeFTGSOuwSEVAu9kVN9ScrpPX%2FmmGwxWB%2FQZsFuWYXXX5KExZpJcJWm4QlY58YWKQqs5XhUbsJ637MWgo47pTumRhvBEmfmSCUTdBwE64aEYWt%2FRSveISLweBHWBypJ14JK8zJoQfSxpHeSZjcrWC1qOJ8wYd5lw5261abZa%2F%2Bsa1eHbevo8Bsq8KJ0mYF3na5WwJKmdIml1OzkQxS%2BD%2BavkKR8Lb1Mby%2BnvveOaRp686oK44yR0xWgPbg%2FJO362nW9IVX9NAexIHYhzT1zi4JK0hY4gfSUHGihthAaHI8qSE5uq8JLIa3LLKytuj8MM3Nhb0GOqUB2%2B1xhFMA%2B7f89JBQ%2BZON4rvgXQZpwTK2Oop6k8le94il%2FTSp40BKD5G6uWluGPauf%2BYXWQuQ91E6VDpPiZjEngfswCHBALzel7hCWqUK%2FBosdlDbk99hHDAlcqJN%2BNONdE%2BULEw4ZimLqZXEiov1WJzkd%2BK%2F4fsyJhJ5%2FHjH67NikYUGuIVwWFPEkBwJAkRsvcpV1dDmt0QFkR9eZt1IpVkCLCnT&X-Amz-Signature=3d7ce8d2879f998a414c7c9f5c1e71dae481dec13764dc5e448c910a0bb4cef5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSGJGQLE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIFq%2FWdvJm%2F7gkoSjUvIDp9TYGcfZIfm1qIYbjEiv52LIAiEAxyqlW7JDwdmycUrCmRc77BctT5EsBmWh8%2FAEVQkKM%2FUq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDHDaX7uGgNslB48PkCrcA8OaLG9D5vclF5zQqWeTEpW8wJ5jokwAqWKzhhsUx%2Fv%2BiTB7E8xiXBwtRhUk1SNYOJ%2Fv2MB6thlX6aDv6kXoXjeMr89JbMRaw9qiYNUs54%2BnYrogHTHnoDEv259Vzw2wBUQNDVB60H%2FLvpZKJo5f6rT55301zpQgGs4KCQeAQ7eaDNagNXBije7rgtTznr5bSnkgOUCg41pEWbJnNcZ8ZUI1PVKZHuIs3RlRnYRFA3jZ5XzPfRhyJSPfG%2FjCfdUH1I3ZcJukH%2F4fKQnB1dYuGTIHGuoaDuHQhgRUx9W1tlXAN%2FzGOLga%2BnWfxidD8sHeFTGSOuwSEVAu9kVN9ScrpPX%2FmmGwxWB%2FQZsFuWYXXX5KExZpJcJWm4QlY58YWKQqs5XhUbsJ637MWgo47pTumRhvBEmfmSCUTdBwE64aEYWt%2FRSveISLweBHWBypJ14JK8zJoQfSxpHeSZjcrWC1qOJ8wYd5lw5261abZa%2F%2Bsa1eHbevo8Bsq8KJ0mYF3na5WwJKmdIml1OzkQxS%2BD%2BavkKR8Lb1Mby%2BnvveOaRp686oK44yR0xWgPbg%2FJO362nW9IVX9NAexIHYhzT1zi4JK0hY4gfSUHGihthAaHI8qSE5uq8JLIa3LLKytuj8MM3Nhb0GOqUB2%2B1xhFMA%2B7f89JBQ%2BZON4rvgXQZpwTK2Oop6k8le94il%2FTSp40BKD5G6uWluGPauf%2BYXWQuQ91E6VDpPiZjEngfswCHBALzel7hCWqUK%2FBosdlDbk99hHDAlcqJN%2BNONdE%2BULEw4ZimLqZXEiov1WJzkd%2BK%2F4fsyJhJ5%2FHjH67NikYUGuIVwWFPEkBwJAkRsvcpV1dDmt0QFkR9eZt1IpVkCLCnT&X-Amz-Signature=fe10a58101d144c47ce4c273224a8f49127f5e3e3bf1bf8a047c73613e2fd65b&X-Amz-SignedHeaders=host&x-id=GetObject)
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


