

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=f67d4dac5ea95c53f80eaa3676266ce111d0d411253227cc0405c01a22c4b806&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KNJP6KB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9HMrp%2BZT9rpT6%2BkJTp0L1kdIGEg66jG%2BMQ82AwaE25QIgWTQ3LCf7sz6aU5ClozE49I6N9pCzDMv4%2FwhHEHi%2B3gUqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIoiTYPLbu6VsYe3CrcA6VBm0gyKUTirHBMsqtIr9NvcTAJHNJROZFDToOWIgnZsrK88vhrFFK1sCcTkFnkusS4A8ud393jpWq4RagqHtYglTEG6Dv8dRTgSJ5ThGigKJKFN2K3ftBnfsBCPqt9q%2B2P1Py31nJI%2FhpgeYYEvmRdhOpwJbC0bXjJH7O9S2FVUjY%2BMzHps5GR9KFp5S3j4mw%2FyMFeawPqDVNExSJh39AVWwMezQ%2By0dj2t8C5C21TjnPI8bSK2ncsCbGhXu%2F4OpKhHHbg%2Fe600k1%2F3J249GDb4v5Rh6KifEQpEb2PuL1X41bK%2Fg2IvPE7FAQjb4j0VEj%2FP90EinNSfUx%2FXqTnQDl8jdOGppf9nzRiv6AzXqagO66XFlk5f5WVuS3ZRShY1sLnhYkaMGGAEl7OtD6%2FbOYH4rhEnJnmci70k8WDPAWn88jB4vg8q6schTekTMoMIKzgAUQHr%2F0oVrCcml4ZRABbX72sTep2vUSdiWlrVmUpjTDFEmC1SPIgBMm3FWm0o5dwlUFSP2rULJr3SJOMG%2F3nNCGzZ0FugBn5qGznbb3qvHXvLlCSVMyRggOpMrAmPWV6DCaQW4EJYSnhi0yVJ%2BFIIqiqcmX9wCflqKvi7f9nhiZkQOkhnhkIdTlZMNzR8LwGOqUBApZGz8tZ8r4kaMfkRxodnhFi0qKigrmg7TftwsP%2BQNg1fvRp9AJCQyEr%2Fq2L%2FRqBY7Q9olLxXdDO2uRikb0dULynUH%2B0ggmHpsALjtRZ%2BhvffpM1oftS%2F6gb2h%2FD7mQuqdyjvmvYqvSsTKZQhPOVfxC1yMBjodgGXo9fyfxrkN%2BShE5PFYruF80tP1XHx8i9aK6CmKL2xZKMJ6iosWXlxWBiyWvB&X-Amz-Signature=317cc3e00cf284fbab1f6f3e4f790419284f08c75f169a55caba2239ef5f51c1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KNJP6KB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9HMrp%2BZT9rpT6%2BkJTp0L1kdIGEg66jG%2BMQ82AwaE25QIgWTQ3LCf7sz6aU5ClozE49I6N9pCzDMv4%2FwhHEHi%2B3gUqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIoiTYPLbu6VsYe3CrcA6VBm0gyKUTirHBMsqtIr9NvcTAJHNJROZFDToOWIgnZsrK88vhrFFK1sCcTkFnkusS4A8ud393jpWq4RagqHtYglTEG6Dv8dRTgSJ5ThGigKJKFN2K3ftBnfsBCPqt9q%2B2P1Py31nJI%2FhpgeYYEvmRdhOpwJbC0bXjJH7O9S2FVUjY%2BMzHps5GR9KFp5S3j4mw%2FyMFeawPqDVNExSJh39AVWwMezQ%2By0dj2t8C5C21TjnPI8bSK2ncsCbGhXu%2F4OpKhHHbg%2Fe600k1%2F3J249GDb4v5Rh6KifEQpEb2PuL1X41bK%2Fg2IvPE7FAQjb4j0VEj%2FP90EinNSfUx%2FXqTnQDl8jdOGppf9nzRiv6AzXqagO66XFlk5f5WVuS3ZRShY1sLnhYkaMGGAEl7OtD6%2FbOYH4rhEnJnmci70k8WDPAWn88jB4vg8q6schTekTMoMIKzgAUQHr%2F0oVrCcml4ZRABbX72sTep2vUSdiWlrVmUpjTDFEmC1SPIgBMm3FWm0o5dwlUFSP2rULJr3SJOMG%2F3nNCGzZ0FugBn5qGznbb3qvHXvLlCSVMyRggOpMrAmPWV6DCaQW4EJYSnhi0yVJ%2BFIIqiqcmX9wCflqKvi7f9nhiZkQOkhnhkIdTlZMNzR8LwGOqUBApZGz8tZ8r4kaMfkRxodnhFi0qKigrmg7TftwsP%2BQNg1fvRp9AJCQyEr%2Fq2L%2FRqBY7Q9olLxXdDO2uRikb0dULynUH%2B0ggmHpsALjtRZ%2BhvffpM1oftS%2F6gb2h%2FD7mQuqdyjvmvYqvSsTKZQhPOVfxC1yMBjodgGXo9fyfxrkN%2BShE5PFYruF80tP1XHx8i9aK6CmKL2xZKMJ6iosWXlxWBiyWvB&X-Amz-Signature=3653b52d836d99101367b9f08edcdec2cff94463809c8ed4b9992779139bdd67&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KNJP6KB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9HMrp%2BZT9rpT6%2BkJTp0L1kdIGEg66jG%2BMQ82AwaE25QIgWTQ3LCf7sz6aU5ClozE49I6N9pCzDMv4%2FwhHEHi%2B3gUqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIoiTYPLbu6VsYe3CrcA6VBm0gyKUTirHBMsqtIr9NvcTAJHNJROZFDToOWIgnZsrK88vhrFFK1sCcTkFnkusS4A8ud393jpWq4RagqHtYglTEG6Dv8dRTgSJ5ThGigKJKFN2K3ftBnfsBCPqt9q%2B2P1Py31nJI%2FhpgeYYEvmRdhOpwJbC0bXjJH7O9S2FVUjY%2BMzHps5GR9KFp5S3j4mw%2FyMFeawPqDVNExSJh39AVWwMezQ%2By0dj2t8C5C21TjnPI8bSK2ncsCbGhXu%2F4OpKhHHbg%2Fe600k1%2F3J249GDb4v5Rh6KifEQpEb2PuL1X41bK%2Fg2IvPE7FAQjb4j0VEj%2FP90EinNSfUx%2FXqTnQDl8jdOGppf9nzRiv6AzXqagO66XFlk5f5WVuS3ZRShY1sLnhYkaMGGAEl7OtD6%2FbOYH4rhEnJnmci70k8WDPAWn88jB4vg8q6schTekTMoMIKzgAUQHr%2F0oVrCcml4ZRABbX72sTep2vUSdiWlrVmUpjTDFEmC1SPIgBMm3FWm0o5dwlUFSP2rULJr3SJOMG%2F3nNCGzZ0FugBn5qGznbb3qvHXvLlCSVMyRggOpMrAmPWV6DCaQW4EJYSnhi0yVJ%2BFIIqiqcmX9wCflqKvi7f9nhiZkQOkhnhkIdTlZMNzR8LwGOqUBApZGz8tZ8r4kaMfkRxodnhFi0qKigrmg7TftwsP%2BQNg1fvRp9AJCQyEr%2Fq2L%2FRqBY7Q9olLxXdDO2uRikb0dULynUH%2B0ggmHpsALjtRZ%2BhvffpM1oftS%2F6gb2h%2FD7mQuqdyjvmvYqvSsTKZQhPOVfxC1yMBjodgGXo9fyfxrkN%2BShE5PFYruF80tP1XHx8i9aK6CmKL2xZKMJ6iosWXlxWBiyWvB&X-Amz-Signature=2966286be36732333cec39ddd33006d67d8369d3485466cf86b40be62dbbec05&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KNJP6KB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9HMrp%2BZT9rpT6%2BkJTp0L1kdIGEg66jG%2BMQ82AwaE25QIgWTQ3LCf7sz6aU5ClozE49I6N9pCzDMv4%2FwhHEHi%2B3gUqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIoiTYPLbu6VsYe3CrcA6VBm0gyKUTirHBMsqtIr9NvcTAJHNJROZFDToOWIgnZsrK88vhrFFK1sCcTkFnkusS4A8ud393jpWq4RagqHtYglTEG6Dv8dRTgSJ5ThGigKJKFN2K3ftBnfsBCPqt9q%2B2P1Py31nJI%2FhpgeYYEvmRdhOpwJbC0bXjJH7O9S2FVUjY%2BMzHps5GR9KFp5S3j4mw%2FyMFeawPqDVNExSJh39AVWwMezQ%2By0dj2t8C5C21TjnPI8bSK2ncsCbGhXu%2F4OpKhHHbg%2Fe600k1%2F3J249GDb4v5Rh6KifEQpEb2PuL1X41bK%2Fg2IvPE7FAQjb4j0VEj%2FP90EinNSfUx%2FXqTnQDl8jdOGppf9nzRiv6AzXqagO66XFlk5f5WVuS3ZRShY1sLnhYkaMGGAEl7OtD6%2FbOYH4rhEnJnmci70k8WDPAWn88jB4vg8q6schTekTMoMIKzgAUQHr%2F0oVrCcml4ZRABbX72sTep2vUSdiWlrVmUpjTDFEmC1SPIgBMm3FWm0o5dwlUFSP2rULJr3SJOMG%2F3nNCGzZ0FugBn5qGznbb3qvHXvLlCSVMyRggOpMrAmPWV6DCaQW4EJYSnhi0yVJ%2BFIIqiqcmX9wCflqKvi7f9nhiZkQOkhnhkIdTlZMNzR8LwGOqUBApZGz8tZ8r4kaMfkRxodnhFi0qKigrmg7TftwsP%2BQNg1fvRp9AJCQyEr%2Fq2L%2FRqBY7Q9olLxXdDO2uRikb0dULynUH%2B0ggmHpsALjtRZ%2BhvffpM1oftS%2F6gb2h%2FD7mQuqdyjvmvYqvSsTKZQhPOVfxC1yMBjodgGXo9fyfxrkN%2BShE5PFYruF80tP1XHx8i9aK6CmKL2xZKMJ6iosWXlxWBiyWvB&X-Amz-Signature=1b4d49c3e384e1bf697557ecdcd426db755feba8123b0df1e003487f3ae545af&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KNJP6KB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9HMrp%2BZT9rpT6%2BkJTp0L1kdIGEg66jG%2BMQ82AwaE25QIgWTQ3LCf7sz6aU5ClozE49I6N9pCzDMv4%2FwhHEHi%2B3gUqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIoiTYPLbu6VsYe3CrcA6VBm0gyKUTirHBMsqtIr9NvcTAJHNJROZFDToOWIgnZsrK88vhrFFK1sCcTkFnkusS4A8ud393jpWq4RagqHtYglTEG6Dv8dRTgSJ5ThGigKJKFN2K3ftBnfsBCPqt9q%2B2P1Py31nJI%2FhpgeYYEvmRdhOpwJbC0bXjJH7O9S2FVUjY%2BMzHps5GR9KFp5S3j4mw%2FyMFeawPqDVNExSJh39AVWwMezQ%2By0dj2t8C5C21TjnPI8bSK2ncsCbGhXu%2F4OpKhHHbg%2Fe600k1%2F3J249GDb4v5Rh6KifEQpEb2PuL1X41bK%2Fg2IvPE7FAQjb4j0VEj%2FP90EinNSfUx%2FXqTnQDl8jdOGppf9nzRiv6AzXqagO66XFlk5f5WVuS3ZRShY1sLnhYkaMGGAEl7OtD6%2FbOYH4rhEnJnmci70k8WDPAWn88jB4vg8q6schTekTMoMIKzgAUQHr%2F0oVrCcml4ZRABbX72sTep2vUSdiWlrVmUpjTDFEmC1SPIgBMm3FWm0o5dwlUFSP2rULJr3SJOMG%2F3nNCGzZ0FugBn5qGznbb3qvHXvLlCSVMyRggOpMrAmPWV6DCaQW4EJYSnhi0yVJ%2BFIIqiqcmX9wCflqKvi7f9nhiZkQOkhnhkIdTlZMNzR8LwGOqUBApZGz8tZ8r4kaMfkRxodnhFi0qKigrmg7TftwsP%2BQNg1fvRp9AJCQyEr%2Fq2L%2FRqBY7Q9olLxXdDO2uRikb0dULynUH%2B0ggmHpsALjtRZ%2BhvffpM1oftS%2F6gb2h%2FD7mQuqdyjvmvYqvSsTKZQhPOVfxC1yMBjodgGXo9fyfxrkN%2BShE5PFYruF80tP1XHx8i9aK6CmKL2xZKMJ6iosWXlxWBiyWvB&X-Amz-Signature=7114c9d480e62096a11d612eedd99bc53621ffba0aa81268b8fdd8bed40b5916&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=aba6ad0b5d1a0347728a72cff6890b7d01f6afb0564886dc66d873414941f769&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=461e765bcab4535660b5ebcd74d4eec19f5ed6f41bbd6894af9a9fd8c554134a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=bef618302f563369760e146a03541a71a543a22cb34dced3f14f4b27b84062f0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=5389a3214d14099bea4e8506e684e4a1447036e557d38ef991a14754723af7a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=d6a9f00dd251f7c81331128f30a54c960994ce31986f014778221aceece62518&X-Amz-SignedHeaders=host&x-id=GetObject)
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


