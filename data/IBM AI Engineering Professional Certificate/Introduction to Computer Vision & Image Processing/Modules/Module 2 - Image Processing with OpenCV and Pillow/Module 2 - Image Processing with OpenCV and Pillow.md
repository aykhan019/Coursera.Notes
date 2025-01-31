

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3I22ZX6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPTPqJWRiNp8edouwrwJvhgvYGeACQEYTh%2B2ngsfWbhAiBrLhxQQZej5i5jVbs4RBk9jbbry0ih5yyE8yKrgm0lJSqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuCkwSw9pZiEwe8okKtwD1nomGR4EvstUOXC77a18Zh3C4kl1h6UHxBBknnQ76mCdtkKlL2WSUfYBco6fJuOysOsr4awTkgz2Abb12xgpXApmK%2FD3ckleTPxno7%2FKmNSz%2BDWKxGcugeHC6Wl527txAr5F4GSJ9BevSaHKbmiUKjoSDGBDJhVFL2JnsAGv5KtUzJvNzBHbOWV8r7udxIU5cKMeJyFRi04U2Vn%2FztPL%2FwyHzvzZWR0LrEJc6f5%2Fc%2FkEscuA%2FCmngyWV7tO8vzLy10QYPfld7vFIlCIu9h44WSv4rde5QJHbnKlUz%2FMzVrwbOcspk1UPkpCdY9BX2OMJKuZ7DfL%2BuHgAylaLU%2B%2BdSaSSDdemQfx%2BkfxpGa06K%2FM3O5awxxjLUrRm%2BhTHlz7xbIwEUeiW9IMmNMzXDoB%2F8k5%2F6FOQFeUpYFFw6ny9u2nDfeRNVC5k52MOqy5b8fOVy3DedB2TkQsKpYFGs0ZOqAb2JAUTYR63pKqXNi%2F2oKXd3701Bt9y2LR3eOPq%2FqRhKEsq06N1JMPaRDbsL4m8kr4u%2B%2FW%2FsNj2IP7a6t%2FDmWUFWyYMegsk8YIAa%2FZ7IOnnLHERqKRq8ED4VUPtlXJOOlZtJogGNOKT%2BngFH7nIO5f5Lvelqcr6l7wciRAw6o%2FzvAY6pgFFmnvVBfhtgH%2B2%2B6hjoin%2BJUjTwF3k8licE%2BmhGa1zJZfrSy4U6zPZpbwOzw1hKkqk8xCoZo3Zl8t4r6ke36g0jxBcfQaF2wCVWCbAxePtRhj141gTYnRyy10Bgf9l1J8EmJ6aOnsh0%2BWD17po6hwqFWevRXaZI0KSX404JQ87jzQwQfX1UBIz1AEBORAoRm8Fh4cBm1cDeJcoVdn7hcCGwha%2F%2BL1l&X-Amz-Signature=1cb6731c2ed7e26d3298df5df206487d69b8d7f714904129850e66a096db4b84&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCAYVAW3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGBHcNe6Dk3hDNkXeQm4d4Feha87qeK8KVIxeijUAw6vAiEAjUfkbmqdbvcJdkCTAWhFw3BWXsdGlWKHHHzGhgk3vzwqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE8fgpMkew5B40KcSSrcA%2BND%2BqSamgI0lnARkbh%2F56naoopcaSDs7DweEL%2BSSBPT9gJJtWHBxLRYMh08uGQVafamj7Iop%2FJM%2B1rCZns%2B3DWwfKvBdlSck2pmWoedMIA%2BjbSyFUgUSI8w2CHh9wVBNLf5pruyTQ3Ci%2BJzf1ykkQMMUHfk6opV%2FYMEt%2Btaqc8O%2FIa4n9hEoyJr2SU94twzit6ZQueMwOXQxhL61BNwVCdu1%2FPgp57f%2BMOLdeyB%2BrJolNuF0uFh4H9K6WQPERCyHqu%2BfZZLanUg6pRrPDNO9dTfKY2Y0oNgHYGQjpk1NECFov4yuPb%2FCsAdff4Z96YeaIzM%2BLpXEGJowbq0lFVlWD4vCqV7HZAX6m8R6Znhp1diBPh8W57lFtQ22si5%2BRjGS6zHS3eSsCwUQC31Fbh42w%2BE0aPp2kg%2FzwbzdhHjrKuSqwsEppKi%2FC3vMSUScO%2Bs7KfzUK5pdAh7%2FIggdlDLV%2BWbpXo53Pe6f%2Fvek58FPTnbZwJUQwiXTEBY4%2BdGmjFkjr%2BmLs59V0MFFOoBtZi4cra0sFYFI2lhAJswxGXyc0plswoDVYwuMFctaizqyT%2F8Awac6hNS7F5L5YaMgVyE59reX2dTOeMoW5vF9kPQgTSGgSwq7RaV%2BU953%2BwyMLqP87wGOqUBxREIxI3rJDeTL17%2B8AegBRwDzaVtxnCjjfsXKPW%2FUSTZrFkvss7SQsVv%2B7TpR4MDnZlSYUvCiwQs2vxs%2FIXpdMW3UlY8SOIbuUJoa9nwi7HhdD98SR%2BtFe3ADLzq3549vb3SsYcScGcjKMOibRVLYkH%2BR%2FTL%2FXk4BTwQN8FmNVuPQo0bCEP0k%2F9BfVeH0YMSOaPymjMqpUHXv%2BN2k2vK4pn0M9RT&X-Amz-Signature=c90c24dd1504295786dd7b133fd02bd1a58c5b1a792edf0b670c261a7c455561&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCAYVAW3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGBHcNe6Dk3hDNkXeQm4d4Feha87qeK8KVIxeijUAw6vAiEAjUfkbmqdbvcJdkCTAWhFw3BWXsdGlWKHHHzGhgk3vzwqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE8fgpMkew5B40KcSSrcA%2BND%2BqSamgI0lnARkbh%2F56naoopcaSDs7DweEL%2BSSBPT9gJJtWHBxLRYMh08uGQVafamj7Iop%2FJM%2B1rCZns%2B3DWwfKvBdlSck2pmWoedMIA%2BjbSyFUgUSI8w2CHh9wVBNLf5pruyTQ3Ci%2BJzf1ykkQMMUHfk6opV%2FYMEt%2Btaqc8O%2FIa4n9hEoyJr2SU94twzit6ZQueMwOXQxhL61BNwVCdu1%2FPgp57f%2BMOLdeyB%2BrJolNuF0uFh4H9K6WQPERCyHqu%2BfZZLanUg6pRrPDNO9dTfKY2Y0oNgHYGQjpk1NECFov4yuPb%2FCsAdff4Z96YeaIzM%2BLpXEGJowbq0lFVlWD4vCqV7HZAX6m8R6Znhp1diBPh8W57lFtQ22si5%2BRjGS6zHS3eSsCwUQC31Fbh42w%2BE0aPp2kg%2FzwbzdhHjrKuSqwsEppKi%2FC3vMSUScO%2Bs7KfzUK5pdAh7%2FIggdlDLV%2BWbpXo53Pe6f%2Fvek58FPTnbZwJUQwiXTEBY4%2BdGmjFkjr%2BmLs59V0MFFOoBtZi4cra0sFYFI2lhAJswxGXyc0plswoDVYwuMFctaizqyT%2F8Awac6hNS7F5L5YaMgVyE59reX2dTOeMoW5vF9kPQgTSGgSwq7RaV%2BU953%2BwyMLqP87wGOqUBxREIxI3rJDeTL17%2B8AegBRwDzaVtxnCjjfsXKPW%2FUSTZrFkvss7SQsVv%2B7TpR4MDnZlSYUvCiwQs2vxs%2FIXpdMW3UlY8SOIbuUJoa9nwi7HhdD98SR%2BtFe3ADLzq3549vb3SsYcScGcjKMOibRVLYkH%2BR%2FTL%2FXk4BTwQN8FmNVuPQo0bCEP0k%2F9BfVeH0YMSOaPymjMqpUHXv%2BN2k2vK4pn0M9RT&X-Amz-Signature=53775b56270edca2490df8e92a49d1b1719cf8d3fa559fc12753918075c742f8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCAYVAW3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGBHcNe6Dk3hDNkXeQm4d4Feha87qeK8KVIxeijUAw6vAiEAjUfkbmqdbvcJdkCTAWhFw3BWXsdGlWKHHHzGhgk3vzwqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE8fgpMkew5B40KcSSrcA%2BND%2BqSamgI0lnARkbh%2F56naoopcaSDs7DweEL%2BSSBPT9gJJtWHBxLRYMh08uGQVafamj7Iop%2FJM%2B1rCZns%2B3DWwfKvBdlSck2pmWoedMIA%2BjbSyFUgUSI8w2CHh9wVBNLf5pruyTQ3Ci%2BJzf1ykkQMMUHfk6opV%2FYMEt%2Btaqc8O%2FIa4n9hEoyJr2SU94twzit6ZQueMwOXQxhL61BNwVCdu1%2FPgp57f%2BMOLdeyB%2BrJolNuF0uFh4H9K6WQPERCyHqu%2BfZZLanUg6pRrPDNO9dTfKY2Y0oNgHYGQjpk1NECFov4yuPb%2FCsAdff4Z96YeaIzM%2BLpXEGJowbq0lFVlWD4vCqV7HZAX6m8R6Znhp1diBPh8W57lFtQ22si5%2BRjGS6zHS3eSsCwUQC31Fbh42w%2BE0aPp2kg%2FzwbzdhHjrKuSqwsEppKi%2FC3vMSUScO%2Bs7KfzUK5pdAh7%2FIggdlDLV%2BWbpXo53Pe6f%2Fvek58FPTnbZwJUQwiXTEBY4%2BdGmjFkjr%2BmLs59V0MFFOoBtZi4cra0sFYFI2lhAJswxGXyc0plswoDVYwuMFctaizqyT%2F8Awac6hNS7F5L5YaMgVyE59reX2dTOeMoW5vF9kPQgTSGgSwq7RaV%2BU953%2BwyMLqP87wGOqUBxREIxI3rJDeTL17%2B8AegBRwDzaVtxnCjjfsXKPW%2FUSTZrFkvss7SQsVv%2B7TpR4MDnZlSYUvCiwQs2vxs%2FIXpdMW3UlY8SOIbuUJoa9nwi7HhdD98SR%2BtFe3ADLzq3549vb3SsYcScGcjKMOibRVLYkH%2BR%2FTL%2FXk4BTwQN8FmNVuPQo0bCEP0k%2F9BfVeH0YMSOaPymjMqpUHXv%2BN2k2vK4pn0M9RT&X-Amz-Signature=d6c87e827ac8df13b657c922200e66c8cb2c70b014b40fac28c685ce6babf1e5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCAYVAW3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGBHcNe6Dk3hDNkXeQm4d4Feha87qeK8KVIxeijUAw6vAiEAjUfkbmqdbvcJdkCTAWhFw3BWXsdGlWKHHHzGhgk3vzwqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE8fgpMkew5B40KcSSrcA%2BND%2BqSamgI0lnARkbh%2F56naoopcaSDs7DweEL%2BSSBPT9gJJtWHBxLRYMh08uGQVafamj7Iop%2FJM%2B1rCZns%2B3DWwfKvBdlSck2pmWoedMIA%2BjbSyFUgUSI8w2CHh9wVBNLf5pruyTQ3Ci%2BJzf1ykkQMMUHfk6opV%2FYMEt%2Btaqc8O%2FIa4n9hEoyJr2SU94twzit6ZQueMwOXQxhL61BNwVCdu1%2FPgp57f%2BMOLdeyB%2BrJolNuF0uFh4H9K6WQPERCyHqu%2BfZZLanUg6pRrPDNO9dTfKY2Y0oNgHYGQjpk1NECFov4yuPb%2FCsAdff4Z96YeaIzM%2BLpXEGJowbq0lFVlWD4vCqV7HZAX6m8R6Znhp1diBPh8W57lFtQ22si5%2BRjGS6zHS3eSsCwUQC31Fbh42w%2BE0aPp2kg%2FzwbzdhHjrKuSqwsEppKi%2FC3vMSUScO%2Bs7KfzUK5pdAh7%2FIggdlDLV%2BWbpXo53Pe6f%2Fvek58FPTnbZwJUQwiXTEBY4%2BdGmjFkjr%2BmLs59V0MFFOoBtZi4cra0sFYFI2lhAJswxGXyc0plswoDVYwuMFctaizqyT%2F8Awac6hNS7F5L5YaMgVyE59reX2dTOeMoW5vF9kPQgTSGgSwq7RaV%2BU953%2BwyMLqP87wGOqUBxREIxI3rJDeTL17%2B8AegBRwDzaVtxnCjjfsXKPW%2FUSTZrFkvss7SQsVv%2B7TpR4MDnZlSYUvCiwQs2vxs%2FIXpdMW3UlY8SOIbuUJoa9nwi7HhdD98SR%2BtFe3ADLzq3549vb3SsYcScGcjKMOibRVLYkH%2BR%2FTL%2FXk4BTwQN8FmNVuPQo0bCEP0k%2F9BfVeH0YMSOaPymjMqpUHXv%2BN2k2vK4pn0M9RT&X-Amz-Signature=839c6f7f33c30357b20e0eacc03ab6d3a5e8acc6d9c19c534d6db1bf6d7bc165&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCAYVAW3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGBHcNe6Dk3hDNkXeQm4d4Feha87qeK8KVIxeijUAw6vAiEAjUfkbmqdbvcJdkCTAWhFw3BWXsdGlWKHHHzGhgk3vzwqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE8fgpMkew5B40KcSSrcA%2BND%2BqSamgI0lnARkbh%2F56naoopcaSDs7DweEL%2BSSBPT9gJJtWHBxLRYMh08uGQVafamj7Iop%2FJM%2B1rCZns%2B3DWwfKvBdlSck2pmWoedMIA%2BjbSyFUgUSI8w2CHh9wVBNLf5pruyTQ3Ci%2BJzf1ykkQMMUHfk6opV%2FYMEt%2Btaqc8O%2FIa4n9hEoyJr2SU94twzit6ZQueMwOXQxhL61BNwVCdu1%2FPgp57f%2BMOLdeyB%2BrJolNuF0uFh4H9K6WQPERCyHqu%2BfZZLanUg6pRrPDNO9dTfKY2Y0oNgHYGQjpk1NECFov4yuPb%2FCsAdff4Z96YeaIzM%2BLpXEGJowbq0lFVlWD4vCqV7HZAX6m8R6Znhp1diBPh8W57lFtQ22si5%2BRjGS6zHS3eSsCwUQC31Fbh42w%2BE0aPp2kg%2FzwbzdhHjrKuSqwsEppKi%2FC3vMSUScO%2Bs7KfzUK5pdAh7%2FIggdlDLV%2BWbpXo53Pe6f%2Fvek58FPTnbZwJUQwiXTEBY4%2BdGmjFkjr%2BmLs59V0MFFOoBtZi4cra0sFYFI2lhAJswxGXyc0plswoDVYwuMFctaizqyT%2F8Awac6hNS7F5L5YaMgVyE59reX2dTOeMoW5vF9kPQgTSGgSwq7RaV%2BU953%2BwyMLqP87wGOqUBxREIxI3rJDeTL17%2B8AegBRwDzaVtxnCjjfsXKPW%2FUSTZrFkvss7SQsVv%2B7TpR4MDnZlSYUvCiwQs2vxs%2FIXpdMW3UlY8SOIbuUJoa9nwi7HhdD98SR%2BtFe3ADLzq3549vb3SsYcScGcjKMOibRVLYkH%2BR%2FTL%2FXk4BTwQN8FmNVuPQo0bCEP0k%2F9BfVeH0YMSOaPymjMqpUHXv%2BN2k2vK4pn0M9RT&X-Amz-Signature=06ce65a9b5fa6fa176b65e5643496a3c289578858fb4dcbc0c543820085ed1c0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3I22ZX6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPTPqJWRiNp8edouwrwJvhgvYGeACQEYTh%2B2ngsfWbhAiBrLhxQQZej5i5jVbs4RBk9jbbry0ih5yyE8yKrgm0lJSqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuCkwSw9pZiEwe8okKtwD1nomGR4EvstUOXC77a18Zh3C4kl1h6UHxBBknnQ76mCdtkKlL2WSUfYBco6fJuOysOsr4awTkgz2Abb12xgpXApmK%2FD3ckleTPxno7%2FKmNSz%2BDWKxGcugeHC6Wl527txAr5F4GSJ9BevSaHKbmiUKjoSDGBDJhVFL2JnsAGv5KtUzJvNzBHbOWV8r7udxIU5cKMeJyFRi04U2Vn%2FztPL%2FwyHzvzZWR0LrEJc6f5%2Fc%2FkEscuA%2FCmngyWV7tO8vzLy10QYPfld7vFIlCIu9h44WSv4rde5QJHbnKlUz%2FMzVrwbOcspk1UPkpCdY9BX2OMJKuZ7DfL%2BuHgAylaLU%2B%2BdSaSSDdemQfx%2BkfxpGa06K%2FM3O5awxxjLUrRm%2BhTHlz7xbIwEUeiW9IMmNMzXDoB%2F8k5%2F6FOQFeUpYFFw6ny9u2nDfeRNVC5k52MOqy5b8fOVy3DedB2TkQsKpYFGs0ZOqAb2JAUTYR63pKqXNi%2F2oKXd3701Bt9y2LR3eOPq%2FqRhKEsq06N1JMPaRDbsL4m8kr4u%2B%2FW%2FsNj2IP7a6t%2FDmWUFWyYMegsk8YIAa%2FZ7IOnnLHERqKRq8ED4VUPtlXJOOlZtJogGNOKT%2BngFH7nIO5f5Lvelqcr6l7wciRAw6o%2FzvAY6pgFFmnvVBfhtgH%2B2%2B6hjoin%2BJUjTwF3k8licE%2BmhGa1zJZfrSy4U6zPZpbwOzw1hKkqk8xCoZo3Zl8t4r6ke36g0jxBcfQaF2wCVWCbAxePtRhj141gTYnRyy10Bgf9l1J8EmJ6aOnsh0%2BWD17po6hwqFWevRXaZI0KSX404JQ87jzQwQfX1UBIz1AEBORAoRm8Fh4cBm1cDeJcoVdn7hcCGwha%2F%2BL1l&X-Amz-Signature=ec66b2de27a85f8bfd8a6ef50053446a9f81b298ab4c4ab69e043c48ce3c3a08&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3I22ZX6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPTPqJWRiNp8edouwrwJvhgvYGeACQEYTh%2B2ngsfWbhAiBrLhxQQZej5i5jVbs4RBk9jbbry0ih5yyE8yKrgm0lJSqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuCkwSw9pZiEwe8okKtwD1nomGR4EvstUOXC77a18Zh3C4kl1h6UHxBBknnQ76mCdtkKlL2WSUfYBco6fJuOysOsr4awTkgz2Abb12xgpXApmK%2FD3ckleTPxno7%2FKmNSz%2BDWKxGcugeHC6Wl527txAr5F4GSJ9BevSaHKbmiUKjoSDGBDJhVFL2JnsAGv5KtUzJvNzBHbOWV8r7udxIU5cKMeJyFRi04U2Vn%2FztPL%2FwyHzvzZWR0LrEJc6f5%2Fc%2FkEscuA%2FCmngyWV7tO8vzLy10QYPfld7vFIlCIu9h44WSv4rde5QJHbnKlUz%2FMzVrwbOcspk1UPkpCdY9BX2OMJKuZ7DfL%2BuHgAylaLU%2B%2BdSaSSDdemQfx%2BkfxpGa06K%2FM3O5awxxjLUrRm%2BhTHlz7xbIwEUeiW9IMmNMzXDoB%2F8k5%2F6FOQFeUpYFFw6ny9u2nDfeRNVC5k52MOqy5b8fOVy3DedB2TkQsKpYFGs0ZOqAb2JAUTYR63pKqXNi%2F2oKXd3701Bt9y2LR3eOPq%2FqRhKEsq06N1JMPaRDbsL4m8kr4u%2B%2FW%2FsNj2IP7a6t%2FDmWUFWyYMegsk8YIAa%2FZ7IOnnLHERqKRq8ED4VUPtlXJOOlZtJogGNOKT%2BngFH7nIO5f5Lvelqcr6l7wciRAw6o%2FzvAY6pgFFmnvVBfhtgH%2B2%2B6hjoin%2BJUjTwF3k8licE%2BmhGa1zJZfrSy4U6zPZpbwOzw1hKkqk8xCoZo3Zl8t4r6ke36g0jxBcfQaF2wCVWCbAxePtRhj141gTYnRyy10Bgf9l1J8EmJ6aOnsh0%2BWD17po6hwqFWevRXaZI0KSX404JQ87jzQwQfX1UBIz1AEBORAoRm8Fh4cBm1cDeJcoVdn7hcCGwha%2F%2BL1l&X-Amz-Signature=d929f5d686203247bc75e27ec85db06ff4dcdf680f3c54c53506cdd32d5966e8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3I22ZX6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPTPqJWRiNp8edouwrwJvhgvYGeACQEYTh%2B2ngsfWbhAiBrLhxQQZej5i5jVbs4RBk9jbbry0ih5yyE8yKrgm0lJSqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuCkwSw9pZiEwe8okKtwD1nomGR4EvstUOXC77a18Zh3C4kl1h6UHxBBknnQ76mCdtkKlL2WSUfYBco6fJuOysOsr4awTkgz2Abb12xgpXApmK%2FD3ckleTPxno7%2FKmNSz%2BDWKxGcugeHC6Wl527txAr5F4GSJ9BevSaHKbmiUKjoSDGBDJhVFL2JnsAGv5KtUzJvNzBHbOWV8r7udxIU5cKMeJyFRi04U2Vn%2FztPL%2FwyHzvzZWR0LrEJc6f5%2Fc%2FkEscuA%2FCmngyWV7tO8vzLy10QYPfld7vFIlCIu9h44WSv4rde5QJHbnKlUz%2FMzVrwbOcspk1UPkpCdY9BX2OMJKuZ7DfL%2BuHgAylaLU%2B%2BdSaSSDdemQfx%2BkfxpGa06K%2FM3O5awxxjLUrRm%2BhTHlz7xbIwEUeiW9IMmNMzXDoB%2F8k5%2F6FOQFeUpYFFw6ny9u2nDfeRNVC5k52MOqy5b8fOVy3DedB2TkQsKpYFGs0ZOqAb2JAUTYR63pKqXNi%2F2oKXd3701Bt9y2LR3eOPq%2FqRhKEsq06N1JMPaRDbsL4m8kr4u%2B%2FW%2FsNj2IP7a6t%2FDmWUFWyYMegsk8YIAa%2FZ7IOnnLHERqKRq8ED4VUPtlXJOOlZtJogGNOKT%2BngFH7nIO5f5Lvelqcr6l7wciRAw6o%2FzvAY6pgFFmnvVBfhtgH%2B2%2B6hjoin%2BJUjTwF3k8licE%2BmhGa1zJZfrSy4U6zPZpbwOzw1hKkqk8xCoZo3Zl8t4r6ke36g0jxBcfQaF2wCVWCbAxePtRhj141gTYnRyy10Bgf9l1J8EmJ6aOnsh0%2BWD17po6hwqFWevRXaZI0KSX404JQ87jzQwQfX1UBIz1AEBORAoRm8Fh4cBm1cDeJcoVdn7hcCGwha%2F%2BL1l&X-Amz-Signature=46d62995f5b79f1e9d408ff56e1e6d4c49ecf02d770e106f077038eb1c8752b3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3I22ZX6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPTPqJWRiNp8edouwrwJvhgvYGeACQEYTh%2B2ngsfWbhAiBrLhxQQZej5i5jVbs4RBk9jbbry0ih5yyE8yKrgm0lJSqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuCkwSw9pZiEwe8okKtwD1nomGR4EvstUOXC77a18Zh3C4kl1h6UHxBBknnQ76mCdtkKlL2WSUfYBco6fJuOysOsr4awTkgz2Abb12xgpXApmK%2FD3ckleTPxno7%2FKmNSz%2BDWKxGcugeHC6Wl527txAr5F4GSJ9BevSaHKbmiUKjoSDGBDJhVFL2JnsAGv5KtUzJvNzBHbOWV8r7udxIU5cKMeJyFRi04U2Vn%2FztPL%2FwyHzvzZWR0LrEJc6f5%2Fc%2FkEscuA%2FCmngyWV7tO8vzLy10QYPfld7vFIlCIu9h44WSv4rde5QJHbnKlUz%2FMzVrwbOcspk1UPkpCdY9BX2OMJKuZ7DfL%2BuHgAylaLU%2B%2BdSaSSDdemQfx%2BkfxpGa06K%2FM3O5awxxjLUrRm%2BhTHlz7xbIwEUeiW9IMmNMzXDoB%2F8k5%2F6FOQFeUpYFFw6ny9u2nDfeRNVC5k52MOqy5b8fOVy3DedB2TkQsKpYFGs0ZOqAb2JAUTYR63pKqXNi%2F2oKXd3701Bt9y2LR3eOPq%2FqRhKEsq06N1JMPaRDbsL4m8kr4u%2B%2FW%2FsNj2IP7a6t%2FDmWUFWyYMegsk8YIAa%2FZ7IOnnLHERqKRq8ED4VUPtlXJOOlZtJogGNOKT%2BngFH7nIO5f5Lvelqcr6l7wciRAw6o%2FzvAY6pgFFmnvVBfhtgH%2B2%2B6hjoin%2BJUjTwF3k8licE%2BmhGa1zJZfrSy4U6zPZpbwOzw1hKkqk8xCoZo3Zl8t4r6ke36g0jxBcfQaF2wCVWCbAxePtRhj141gTYnRyy10Bgf9l1J8EmJ6aOnsh0%2BWD17po6hwqFWevRXaZI0KSX404JQ87jzQwQfX1UBIz1AEBORAoRm8Fh4cBm1cDeJcoVdn7hcCGwha%2F%2BL1l&X-Amz-Signature=fd5dc041a0d71991e1cc4671299927622c827c8e9359bc4ef0fcfbd8da4d2eb4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3I22ZX6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPTPqJWRiNp8edouwrwJvhgvYGeACQEYTh%2B2ngsfWbhAiBrLhxQQZej5i5jVbs4RBk9jbbry0ih5yyE8yKrgm0lJSqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuCkwSw9pZiEwe8okKtwD1nomGR4EvstUOXC77a18Zh3C4kl1h6UHxBBknnQ76mCdtkKlL2WSUfYBco6fJuOysOsr4awTkgz2Abb12xgpXApmK%2FD3ckleTPxno7%2FKmNSz%2BDWKxGcugeHC6Wl527txAr5F4GSJ9BevSaHKbmiUKjoSDGBDJhVFL2JnsAGv5KtUzJvNzBHbOWV8r7udxIU5cKMeJyFRi04U2Vn%2FztPL%2FwyHzvzZWR0LrEJc6f5%2Fc%2FkEscuA%2FCmngyWV7tO8vzLy10QYPfld7vFIlCIu9h44WSv4rde5QJHbnKlUz%2FMzVrwbOcspk1UPkpCdY9BX2OMJKuZ7DfL%2BuHgAylaLU%2B%2BdSaSSDdemQfx%2BkfxpGa06K%2FM3O5awxxjLUrRm%2BhTHlz7xbIwEUeiW9IMmNMzXDoB%2F8k5%2F6FOQFeUpYFFw6ny9u2nDfeRNVC5k52MOqy5b8fOVy3DedB2TkQsKpYFGs0ZOqAb2JAUTYR63pKqXNi%2F2oKXd3701Bt9y2LR3eOPq%2FqRhKEsq06N1JMPaRDbsL4m8kr4u%2B%2FW%2FsNj2IP7a6t%2FDmWUFWyYMegsk8YIAa%2FZ7IOnnLHERqKRq8ED4VUPtlXJOOlZtJogGNOKT%2BngFH7nIO5f5Lvelqcr6l7wciRAw6o%2FzvAY6pgFFmnvVBfhtgH%2B2%2B6hjoin%2BJUjTwF3k8licE%2BmhGa1zJZfrSy4U6zPZpbwOzw1hKkqk8xCoZo3Zl8t4r6ke36g0jxBcfQaF2wCVWCbAxePtRhj141gTYnRyy10Bgf9l1J8EmJ6aOnsh0%2BWD17po6hwqFWevRXaZI0KSX404JQ87jzQwQfX1UBIz1AEBORAoRm8Fh4cBm1cDeJcoVdn7hcCGwha%2F%2BL1l&X-Amz-Signature=0348c1b9f5977b0c3d651b010f9ffc46ff1689b7f46c4bcace83cd36b11f222c&X-Amz-SignedHeaders=host&x-id=GetObject)
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


