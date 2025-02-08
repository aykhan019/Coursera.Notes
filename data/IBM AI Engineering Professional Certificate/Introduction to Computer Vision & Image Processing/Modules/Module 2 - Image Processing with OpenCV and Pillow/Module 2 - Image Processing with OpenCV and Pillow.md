

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBZY3GO7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB8ZepcHwrFEJbXlmD5lIFG%2Bpz6Q%2BrWchfKSj4gm%2FT5BAiADD40tw8O43xryLbMqbYmOnXmWhsRVGk%2FWZfjP7t%2FTqCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM308kt%2BBgmeG%2BDCh5KtwDLo43CsnjP1xGcVl%2FDuyIEBnI4l0c5aF9julEiNsScMn%2BS6ec7x9uP35Xm%2BXAs71Tx2oQImZZOvNoGsWgHa27u7BrH%2BwCuSGaFUXwsdvDfL%2BrwlemElbD86f8WC58L0M061MX6luTcyuHcke9C8b2Hnk%2F3HbZMVjpX35eK8TxbmIlE3aDbX0bIR%2Bq3wvl%2BdCvbLm1AH0k%2BBGfwaACIGgATwxFYahdAdwb0lqY3G8uFMswZQSA1AUB20B%2BAlU82sSXerEIMJCnpKVl3ZQoi3pgNm57vXcCF42bV9S%2BFzp%2BithvtjB5L2MA2MALOmvjN0XYpUoBzA3jeYiGmPr08B3qSFmZsmaLmIyvxxxUIgxh5GoZN5NRkwwIl6%2FJDM2iAuSRvw2LenmYkuv53NyGTda0BN9s7sL0JCMouVe8TLYLJAEw3mywzqUIKXxVGML7tJYxjkh4F3WB%2F7S3Bg9FextNqs%2F0qaKtZYT9BEN8oualJbmxnRkOgltM5UTffEjeFIwaSqHMLyQPk9JuZ0DAM5U9%2FhGKCvmoJeo3XaiAWpzGV%2B2FR6uQbxwOOrS58TzigITGeEARNlO90S1ZuDOQt%2FSDlEATmbAbbRq42A3crhOczS3jEC%2FKnyM01qH6oPkwprKbvQY6pgGbvsWangJTs9hV2YWls8cEAw4NQh4h8lz40HRh1EyK1eQC9MBb0LkJ2%2BRUwuDt%2FreEkFZt8CAUA9gLDQoFEbmyJxWxjzn6ajhMOTlfITBdR3eNptYMMwi3uBfNmHeosZORf6fwPpTMyIQE8CtEcY88e9GQv1rL5Pb59w2kgjX85RYXmD7QdMT6FChnct9qfIUr01op2UNVEBpvFAot2GB2MWQbqQHe&X-Amz-Signature=843f0c6eb1130897fe8752930051c0e3d14656f9065cad53b7e60a15d6d348eb&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6UMHLMN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIHX%2BvMwROyA8MlrPVowktieofJ4zGqcA51GGY6TA1KWSAiEA5FOlSV4G04DB%2BCu%2BEBm%2FPIq1Z8XFNguJAb2DQvqyx70qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIUVLOKAsn0sjO%2FE0ircA2ZMnMAaUHdyEVE4dpYrh2TzoxtccM8IYwVdEryoEdMB%2FbbbrqiS6QPiQyCkLJA4TsMPJqsOKfaT51mSwlMm96N%2BeOD67I8uTp0aOjbmHvBOLctPwpppPRwEIM17n0osW788cV%2B442ICFYIjQmEQgzDzsw3dwG54us92pewL4fNAAXUXPZMVO59lmGIUGOpSkUf29DdP9CSAKQOceXyZd4lQgo59DejVxXApfhU%2FIorliHiyKF8T3%2BR6yQOrxqHTa6ac6YqYhYEzY6huh2hQQFOoZpQxuXAVDm3cj0tix31R%2BEnkTw6I%2BLiePooSTTBXQuueHjA7oUZx5FLscYUTS36nzRgA15%2BzZ4hGXsJjv3wc6m%2BeoQ%2FBCWDNWQgZwUhNF0JZ9akANivY%2BijGsPnMP6qvCdQExoq5VwPFTXv1RZQydX%2BRHldE7u3kCPiFMc%2FiOjoBcEFMB8G5JCz9a89lhPN1jWA%2BXeZk2mn0wW16yVTxe34qg%2Bklnas5SnPtp6SoBIwuTFvysxt88XdhulkXuhjDXSMfybJb97C6qO6rdE4iectPqh5KA3h6wxjZpPBUv1xpr8mZbCqzvf%2FIc9qeOfONsFWlDpuZqTrsJfNAKLHpMDmYEKbIkh1XIpsvMNCym70GOqUBpz2wYeRLdbl6bDo9mvOUSXNbEMjuxohABnM9d9Td9AhisYu%2Bjje3Arp%2B0WvKvI0vqeKtQW9RBueXEFY5PeWvG4wKx3z8Fbe3uxzoZUVMTEdyAWCyfcc7LLkOOWIRyzqAclPVh4KYCYCzPTr2XtoLI%2BAgCI55%2BRRSb3YSs8z8jtEydF6VN511fS3JoksubVKO36pyBJ4yFqtPgwbbthmxR9xURPGR&X-Amz-Signature=53e38fc8830ebfa46cdc14df4c833f0426295cd49ff339bdb8e1266447cfb308&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6UMHLMN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIHX%2BvMwROyA8MlrPVowktieofJ4zGqcA51GGY6TA1KWSAiEA5FOlSV4G04DB%2BCu%2BEBm%2FPIq1Z8XFNguJAb2DQvqyx70qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIUVLOKAsn0sjO%2FE0ircA2ZMnMAaUHdyEVE4dpYrh2TzoxtccM8IYwVdEryoEdMB%2FbbbrqiS6QPiQyCkLJA4TsMPJqsOKfaT51mSwlMm96N%2BeOD67I8uTp0aOjbmHvBOLctPwpppPRwEIM17n0osW788cV%2B442ICFYIjQmEQgzDzsw3dwG54us92pewL4fNAAXUXPZMVO59lmGIUGOpSkUf29DdP9CSAKQOceXyZd4lQgo59DejVxXApfhU%2FIorliHiyKF8T3%2BR6yQOrxqHTa6ac6YqYhYEzY6huh2hQQFOoZpQxuXAVDm3cj0tix31R%2BEnkTw6I%2BLiePooSTTBXQuueHjA7oUZx5FLscYUTS36nzRgA15%2BzZ4hGXsJjv3wc6m%2BeoQ%2FBCWDNWQgZwUhNF0JZ9akANivY%2BijGsPnMP6qvCdQExoq5VwPFTXv1RZQydX%2BRHldE7u3kCPiFMc%2FiOjoBcEFMB8G5JCz9a89lhPN1jWA%2BXeZk2mn0wW16yVTxe34qg%2Bklnas5SnPtp6SoBIwuTFvysxt88XdhulkXuhjDXSMfybJb97C6qO6rdE4iectPqh5KA3h6wxjZpPBUv1xpr8mZbCqzvf%2FIc9qeOfONsFWlDpuZqTrsJfNAKLHpMDmYEKbIkh1XIpsvMNCym70GOqUBpz2wYeRLdbl6bDo9mvOUSXNbEMjuxohABnM9d9Td9AhisYu%2Bjje3Arp%2B0WvKvI0vqeKtQW9RBueXEFY5PeWvG4wKx3z8Fbe3uxzoZUVMTEdyAWCyfcc7LLkOOWIRyzqAclPVh4KYCYCzPTr2XtoLI%2BAgCI55%2BRRSb3YSs8z8jtEydF6VN511fS3JoksubVKO36pyBJ4yFqtPgwbbthmxR9xURPGR&X-Amz-Signature=b342310aa0c92e618b95325e9eddf77c9c065394516f0f84e86844a543ec9bba&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6UMHLMN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIHX%2BvMwROyA8MlrPVowktieofJ4zGqcA51GGY6TA1KWSAiEA5FOlSV4G04DB%2BCu%2BEBm%2FPIq1Z8XFNguJAb2DQvqyx70qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIUVLOKAsn0sjO%2FE0ircA2ZMnMAaUHdyEVE4dpYrh2TzoxtccM8IYwVdEryoEdMB%2FbbbrqiS6QPiQyCkLJA4TsMPJqsOKfaT51mSwlMm96N%2BeOD67I8uTp0aOjbmHvBOLctPwpppPRwEIM17n0osW788cV%2B442ICFYIjQmEQgzDzsw3dwG54us92pewL4fNAAXUXPZMVO59lmGIUGOpSkUf29DdP9CSAKQOceXyZd4lQgo59DejVxXApfhU%2FIorliHiyKF8T3%2BR6yQOrxqHTa6ac6YqYhYEzY6huh2hQQFOoZpQxuXAVDm3cj0tix31R%2BEnkTw6I%2BLiePooSTTBXQuueHjA7oUZx5FLscYUTS36nzRgA15%2BzZ4hGXsJjv3wc6m%2BeoQ%2FBCWDNWQgZwUhNF0JZ9akANivY%2BijGsPnMP6qvCdQExoq5VwPFTXv1RZQydX%2BRHldE7u3kCPiFMc%2FiOjoBcEFMB8G5JCz9a89lhPN1jWA%2BXeZk2mn0wW16yVTxe34qg%2Bklnas5SnPtp6SoBIwuTFvysxt88XdhulkXuhjDXSMfybJb97C6qO6rdE4iectPqh5KA3h6wxjZpPBUv1xpr8mZbCqzvf%2FIc9qeOfONsFWlDpuZqTrsJfNAKLHpMDmYEKbIkh1XIpsvMNCym70GOqUBpz2wYeRLdbl6bDo9mvOUSXNbEMjuxohABnM9d9Td9AhisYu%2Bjje3Arp%2B0WvKvI0vqeKtQW9RBueXEFY5PeWvG4wKx3z8Fbe3uxzoZUVMTEdyAWCyfcc7LLkOOWIRyzqAclPVh4KYCYCzPTr2XtoLI%2BAgCI55%2BRRSb3YSs8z8jtEydF6VN511fS3JoksubVKO36pyBJ4yFqtPgwbbthmxR9xURPGR&X-Amz-Signature=252990f4bfc8a376bc9803df593fd0881659d094cb414eda110f580ab552526d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6UMHLMN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIHX%2BvMwROyA8MlrPVowktieofJ4zGqcA51GGY6TA1KWSAiEA5FOlSV4G04DB%2BCu%2BEBm%2FPIq1Z8XFNguJAb2DQvqyx70qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIUVLOKAsn0sjO%2FE0ircA2ZMnMAaUHdyEVE4dpYrh2TzoxtccM8IYwVdEryoEdMB%2FbbbrqiS6QPiQyCkLJA4TsMPJqsOKfaT51mSwlMm96N%2BeOD67I8uTp0aOjbmHvBOLctPwpppPRwEIM17n0osW788cV%2B442ICFYIjQmEQgzDzsw3dwG54us92pewL4fNAAXUXPZMVO59lmGIUGOpSkUf29DdP9CSAKQOceXyZd4lQgo59DejVxXApfhU%2FIorliHiyKF8T3%2BR6yQOrxqHTa6ac6YqYhYEzY6huh2hQQFOoZpQxuXAVDm3cj0tix31R%2BEnkTw6I%2BLiePooSTTBXQuueHjA7oUZx5FLscYUTS36nzRgA15%2BzZ4hGXsJjv3wc6m%2BeoQ%2FBCWDNWQgZwUhNF0JZ9akANivY%2BijGsPnMP6qvCdQExoq5VwPFTXv1RZQydX%2BRHldE7u3kCPiFMc%2FiOjoBcEFMB8G5JCz9a89lhPN1jWA%2BXeZk2mn0wW16yVTxe34qg%2Bklnas5SnPtp6SoBIwuTFvysxt88XdhulkXuhjDXSMfybJb97C6qO6rdE4iectPqh5KA3h6wxjZpPBUv1xpr8mZbCqzvf%2FIc9qeOfONsFWlDpuZqTrsJfNAKLHpMDmYEKbIkh1XIpsvMNCym70GOqUBpz2wYeRLdbl6bDo9mvOUSXNbEMjuxohABnM9d9Td9AhisYu%2Bjje3Arp%2B0WvKvI0vqeKtQW9RBueXEFY5PeWvG4wKx3z8Fbe3uxzoZUVMTEdyAWCyfcc7LLkOOWIRyzqAclPVh4KYCYCzPTr2XtoLI%2BAgCI55%2BRRSb3YSs8z8jtEydF6VN511fS3JoksubVKO36pyBJ4yFqtPgwbbthmxR9xURPGR&X-Amz-Signature=05d52615afb673b0f008ffd0e865109869eccb551857a67d5a612af178b67564&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6UMHLMN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIHX%2BvMwROyA8MlrPVowktieofJ4zGqcA51GGY6TA1KWSAiEA5FOlSV4G04DB%2BCu%2BEBm%2FPIq1Z8XFNguJAb2DQvqyx70qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIUVLOKAsn0sjO%2FE0ircA2ZMnMAaUHdyEVE4dpYrh2TzoxtccM8IYwVdEryoEdMB%2FbbbrqiS6QPiQyCkLJA4TsMPJqsOKfaT51mSwlMm96N%2BeOD67I8uTp0aOjbmHvBOLctPwpppPRwEIM17n0osW788cV%2B442ICFYIjQmEQgzDzsw3dwG54us92pewL4fNAAXUXPZMVO59lmGIUGOpSkUf29DdP9CSAKQOceXyZd4lQgo59DejVxXApfhU%2FIorliHiyKF8T3%2BR6yQOrxqHTa6ac6YqYhYEzY6huh2hQQFOoZpQxuXAVDm3cj0tix31R%2BEnkTw6I%2BLiePooSTTBXQuueHjA7oUZx5FLscYUTS36nzRgA15%2BzZ4hGXsJjv3wc6m%2BeoQ%2FBCWDNWQgZwUhNF0JZ9akANivY%2BijGsPnMP6qvCdQExoq5VwPFTXv1RZQydX%2BRHldE7u3kCPiFMc%2FiOjoBcEFMB8G5JCz9a89lhPN1jWA%2BXeZk2mn0wW16yVTxe34qg%2Bklnas5SnPtp6SoBIwuTFvysxt88XdhulkXuhjDXSMfybJb97C6qO6rdE4iectPqh5KA3h6wxjZpPBUv1xpr8mZbCqzvf%2FIc9qeOfONsFWlDpuZqTrsJfNAKLHpMDmYEKbIkh1XIpsvMNCym70GOqUBpz2wYeRLdbl6bDo9mvOUSXNbEMjuxohABnM9d9Td9AhisYu%2Bjje3Arp%2B0WvKvI0vqeKtQW9RBueXEFY5PeWvG4wKx3z8Fbe3uxzoZUVMTEdyAWCyfcc7LLkOOWIRyzqAclPVh4KYCYCzPTr2XtoLI%2BAgCI55%2BRRSb3YSs8z8jtEydF6VN511fS3JoksubVKO36pyBJ4yFqtPgwbbthmxR9xURPGR&X-Amz-Signature=086b16072a28f0507924fae0d09dd571cd07ae875366caf061512a1b01f4f77b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBZY3GO7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB8ZepcHwrFEJbXlmD5lIFG%2Bpz6Q%2BrWchfKSj4gm%2FT5BAiADD40tw8O43xryLbMqbYmOnXmWhsRVGk%2FWZfjP7t%2FTqCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM308kt%2BBgmeG%2BDCh5KtwDLo43CsnjP1xGcVl%2FDuyIEBnI4l0c5aF9julEiNsScMn%2BS6ec7x9uP35Xm%2BXAs71Tx2oQImZZOvNoGsWgHa27u7BrH%2BwCuSGaFUXwsdvDfL%2BrwlemElbD86f8WC58L0M061MX6luTcyuHcke9C8b2Hnk%2F3HbZMVjpX35eK8TxbmIlE3aDbX0bIR%2Bq3wvl%2BdCvbLm1AH0k%2BBGfwaACIGgATwxFYahdAdwb0lqY3G8uFMswZQSA1AUB20B%2BAlU82sSXerEIMJCnpKVl3ZQoi3pgNm57vXcCF42bV9S%2BFzp%2BithvtjB5L2MA2MALOmvjN0XYpUoBzA3jeYiGmPr08B3qSFmZsmaLmIyvxxxUIgxh5GoZN5NRkwwIl6%2FJDM2iAuSRvw2LenmYkuv53NyGTda0BN9s7sL0JCMouVe8TLYLJAEw3mywzqUIKXxVGML7tJYxjkh4F3WB%2F7S3Bg9FextNqs%2F0qaKtZYT9BEN8oualJbmxnRkOgltM5UTffEjeFIwaSqHMLyQPk9JuZ0DAM5U9%2FhGKCvmoJeo3XaiAWpzGV%2B2FR6uQbxwOOrS58TzigITGeEARNlO90S1ZuDOQt%2FSDlEATmbAbbRq42A3crhOczS3jEC%2FKnyM01qH6oPkwprKbvQY6pgGbvsWangJTs9hV2YWls8cEAw4NQh4h8lz40HRh1EyK1eQC9MBb0LkJ2%2BRUwuDt%2FreEkFZt8CAUA9gLDQoFEbmyJxWxjzn6ajhMOTlfITBdR3eNptYMMwi3uBfNmHeosZORf6fwPpTMyIQE8CtEcY88e9GQv1rL5Pb59w2kgjX85RYXmD7QdMT6FChnct9qfIUr01op2UNVEBpvFAot2GB2MWQbqQHe&X-Amz-Signature=53389528e0977165d315deb81e3152591480d10dd89bd9e8560558238cc44a5a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBZY3GO7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB8ZepcHwrFEJbXlmD5lIFG%2Bpz6Q%2BrWchfKSj4gm%2FT5BAiADD40tw8O43xryLbMqbYmOnXmWhsRVGk%2FWZfjP7t%2FTqCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM308kt%2BBgmeG%2BDCh5KtwDLo43CsnjP1xGcVl%2FDuyIEBnI4l0c5aF9julEiNsScMn%2BS6ec7x9uP35Xm%2BXAs71Tx2oQImZZOvNoGsWgHa27u7BrH%2BwCuSGaFUXwsdvDfL%2BrwlemElbD86f8WC58L0M061MX6luTcyuHcke9C8b2Hnk%2F3HbZMVjpX35eK8TxbmIlE3aDbX0bIR%2Bq3wvl%2BdCvbLm1AH0k%2BBGfwaACIGgATwxFYahdAdwb0lqY3G8uFMswZQSA1AUB20B%2BAlU82sSXerEIMJCnpKVl3ZQoi3pgNm57vXcCF42bV9S%2BFzp%2BithvtjB5L2MA2MALOmvjN0XYpUoBzA3jeYiGmPr08B3qSFmZsmaLmIyvxxxUIgxh5GoZN5NRkwwIl6%2FJDM2iAuSRvw2LenmYkuv53NyGTda0BN9s7sL0JCMouVe8TLYLJAEw3mywzqUIKXxVGML7tJYxjkh4F3WB%2F7S3Bg9FextNqs%2F0qaKtZYT9BEN8oualJbmxnRkOgltM5UTffEjeFIwaSqHMLyQPk9JuZ0DAM5U9%2FhGKCvmoJeo3XaiAWpzGV%2B2FR6uQbxwOOrS58TzigITGeEARNlO90S1ZuDOQt%2FSDlEATmbAbbRq42A3crhOczS3jEC%2FKnyM01qH6oPkwprKbvQY6pgGbvsWangJTs9hV2YWls8cEAw4NQh4h8lz40HRh1EyK1eQC9MBb0LkJ2%2BRUwuDt%2FreEkFZt8CAUA9gLDQoFEbmyJxWxjzn6ajhMOTlfITBdR3eNptYMMwi3uBfNmHeosZORf6fwPpTMyIQE8CtEcY88e9GQv1rL5Pb59w2kgjX85RYXmD7QdMT6FChnct9qfIUr01op2UNVEBpvFAot2GB2MWQbqQHe&X-Amz-Signature=aaca72593021dacbd0c25f7b023adf8aaba2c1ec1aae7680da0f77c5719c3c77&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBZY3GO7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB8ZepcHwrFEJbXlmD5lIFG%2Bpz6Q%2BrWchfKSj4gm%2FT5BAiADD40tw8O43xryLbMqbYmOnXmWhsRVGk%2FWZfjP7t%2FTqCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM308kt%2BBgmeG%2BDCh5KtwDLo43CsnjP1xGcVl%2FDuyIEBnI4l0c5aF9julEiNsScMn%2BS6ec7x9uP35Xm%2BXAs71Tx2oQImZZOvNoGsWgHa27u7BrH%2BwCuSGaFUXwsdvDfL%2BrwlemElbD86f8WC58L0M061MX6luTcyuHcke9C8b2Hnk%2F3HbZMVjpX35eK8TxbmIlE3aDbX0bIR%2Bq3wvl%2BdCvbLm1AH0k%2BBGfwaACIGgATwxFYahdAdwb0lqY3G8uFMswZQSA1AUB20B%2BAlU82sSXerEIMJCnpKVl3ZQoi3pgNm57vXcCF42bV9S%2BFzp%2BithvtjB5L2MA2MALOmvjN0XYpUoBzA3jeYiGmPr08B3qSFmZsmaLmIyvxxxUIgxh5GoZN5NRkwwIl6%2FJDM2iAuSRvw2LenmYkuv53NyGTda0BN9s7sL0JCMouVe8TLYLJAEw3mywzqUIKXxVGML7tJYxjkh4F3WB%2F7S3Bg9FextNqs%2F0qaKtZYT9BEN8oualJbmxnRkOgltM5UTffEjeFIwaSqHMLyQPk9JuZ0DAM5U9%2FhGKCvmoJeo3XaiAWpzGV%2B2FR6uQbxwOOrS58TzigITGeEARNlO90S1ZuDOQt%2FSDlEATmbAbbRq42A3crhOczS3jEC%2FKnyM01qH6oPkwprKbvQY6pgGbvsWangJTs9hV2YWls8cEAw4NQh4h8lz40HRh1EyK1eQC9MBb0LkJ2%2BRUwuDt%2FreEkFZt8CAUA9gLDQoFEbmyJxWxjzn6ajhMOTlfITBdR3eNptYMMwi3uBfNmHeosZORf6fwPpTMyIQE8CtEcY88e9GQv1rL5Pb59w2kgjX85RYXmD7QdMT6FChnct9qfIUr01op2UNVEBpvFAot2GB2MWQbqQHe&X-Amz-Signature=b92ea0626a11f90b1588be972fd9735192de0ff8d75e4c27b2bf153e300f5dc5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBZY3GO7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB8ZepcHwrFEJbXlmD5lIFG%2Bpz6Q%2BrWchfKSj4gm%2FT5BAiADD40tw8O43xryLbMqbYmOnXmWhsRVGk%2FWZfjP7t%2FTqCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM308kt%2BBgmeG%2BDCh5KtwDLo43CsnjP1xGcVl%2FDuyIEBnI4l0c5aF9julEiNsScMn%2BS6ec7x9uP35Xm%2BXAs71Tx2oQImZZOvNoGsWgHa27u7BrH%2BwCuSGaFUXwsdvDfL%2BrwlemElbD86f8WC58L0M061MX6luTcyuHcke9C8b2Hnk%2F3HbZMVjpX35eK8TxbmIlE3aDbX0bIR%2Bq3wvl%2BdCvbLm1AH0k%2BBGfwaACIGgATwxFYahdAdwb0lqY3G8uFMswZQSA1AUB20B%2BAlU82sSXerEIMJCnpKVl3ZQoi3pgNm57vXcCF42bV9S%2BFzp%2BithvtjB5L2MA2MALOmvjN0XYpUoBzA3jeYiGmPr08B3qSFmZsmaLmIyvxxxUIgxh5GoZN5NRkwwIl6%2FJDM2iAuSRvw2LenmYkuv53NyGTda0BN9s7sL0JCMouVe8TLYLJAEw3mywzqUIKXxVGML7tJYxjkh4F3WB%2F7S3Bg9FextNqs%2F0qaKtZYT9BEN8oualJbmxnRkOgltM5UTffEjeFIwaSqHMLyQPk9JuZ0DAM5U9%2FhGKCvmoJeo3XaiAWpzGV%2B2FR6uQbxwOOrS58TzigITGeEARNlO90S1ZuDOQt%2FSDlEATmbAbbRq42A3crhOczS3jEC%2FKnyM01qH6oPkwprKbvQY6pgGbvsWangJTs9hV2YWls8cEAw4NQh4h8lz40HRh1EyK1eQC9MBb0LkJ2%2BRUwuDt%2FreEkFZt8CAUA9gLDQoFEbmyJxWxjzn6ajhMOTlfITBdR3eNptYMMwi3uBfNmHeosZORf6fwPpTMyIQE8CtEcY88e9GQv1rL5Pb59w2kgjX85RYXmD7QdMT6FChnct9qfIUr01op2UNVEBpvFAot2GB2MWQbqQHe&X-Amz-Signature=55c621a5f9799e7dc415d82965008be8853b39c4cb88d9a923c8a2869b5c8cd4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBZY3GO7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB8ZepcHwrFEJbXlmD5lIFG%2Bpz6Q%2BrWchfKSj4gm%2FT5BAiADD40tw8O43xryLbMqbYmOnXmWhsRVGk%2FWZfjP7t%2FTqCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM308kt%2BBgmeG%2BDCh5KtwDLo43CsnjP1xGcVl%2FDuyIEBnI4l0c5aF9julEiNsScMn%2BS6ec7x9uP35Xm%2BXAs71Tx2oQImZZOvNoGsWgHa27u7BrH%2BwCuSGaFUXwsdvDfL%2BrwlemElbD86f8WC58L0M061MX6luTcyuHcke9C8b2Hnk%2F3HbZMVjpX35eK8TxbmIlE3aDbX0bIR%2Bq3wvl%2BdCvbLm1AH0k%2BBGfwaACIGgATwxFYahdAdwb0lqY3G8uFMswZQSA1AUB20B%2BAlU82sSXerEIMJCnpKVl3ZQoi3pgNm57vXcCF42bV9S%2BFzp%2BithvtjB5L2MA2MALOmvjN0XYpUoBzA3jeYiGmPr08B3qSFmZsmaLmIyvxxxUIgxh5GoZN5NRkwwIl6%2FJDM2iAuSRvw2LenmYkuv53NyGTda0BN9s7sL0JCMouVe8TLYLJAEw3mywzqUIKXxVGML7tJYxjkh4F3WB%2F7S3Bg9FextNqs%2F0qaKtZYT9BEN8oualJbmxnRkOgltM5UTffEjeFIwaSqHMLyQPk9JuZ0DAM5U9%2FhGKCvmoJeo3XaiAWpzGV%2B2FR6uQbxwOOrS58TzigITGeEARNlO90S1ZuDOQt%2FSDlEATmbAbbRq42A3crhOczS3jEC%2FKnyM01qH6oPkwprKbvQY6pgGbvsWangJTs9hV2YWls8cEAw4NQh4h8lz40HRh1EyK1eQC9MBb0LkJ2%2BRUwuDt%2FreEkFZt8CAUA9gLDQoFEbmyJxWxjzn6ajhMOTlfITBdR3eNptYMMwi3uBfNmHeosZORf6fwPpTMyIQE8CtEcY88e9GQv1rL5Pb59w2kgjX85RYXmD7QdMT6FChnct9qfIUr01op2UNVEBpvFAot2GB2MWQbqQHe&X-Amz-Signature=1da74d820fd40626f5e5f093ff834e8625e378301efa563b8f20e6a11ba9edb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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


