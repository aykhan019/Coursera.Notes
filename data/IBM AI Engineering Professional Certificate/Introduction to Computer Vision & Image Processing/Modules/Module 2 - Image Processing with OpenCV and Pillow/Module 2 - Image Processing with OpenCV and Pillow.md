

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QYV6IUN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDEUAuJTYDttNkduNV90ER9jwptLHnluPENB7fve%2BR5YQIgQfsS%2Fgn3EwSCx7aIe3g9YzCTXophtTwmdNT7Kj7oNKYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMx%2Bf4phixn4HtcFjircAy2vLa8Zge12uReKVIdNprCx5gXt8XwwSR9uTrbYbVovmcghzK0TEOY8qOAOXU5HTTPgFqFrQUjO82pEwOtcyQwGv1sx6Q8jQTR%2FvEQonazdNPFqPaHVaT8a3Z4tbXCK0%2BolbpUB1UYaP6K2lP%2F3cxvjdLgnzt7Ja0xT4xPnG7v18dvK0tXiSa2RtcS14IlUjIzCmtXQof7pPCoijzZ6hqnAhFuyFku9QG1ScoBgFPmeRW%2Fmfd2ISpHTZ2L%2BU5LfYUKExJ4WHQxrBJDHG91TwTv71JAmKXIWrQkweX7dveuw9TpkjccKv4KHq1bnlp5yXGgWP03w0X7tsTKihnLTOUhbV0CSFppNBWGaHb0dUEQlyehFG87LdW1naqxfUCuMycgRVO6PftquFG7b3131HvGTrbxrNWVQpUX3YsPP1ZJlGxAabeYWkls4IUgmvNPOgYiB9Dx1ZDxymdDVocanhdkJXEOFJ4wId2iFXV6epeDmMBSM7pKKF9eq9h1nUFMLAa0MEPgGrZQqxg7LAHBC3J9XNlgmZ%2B0IKNdxiJluFg3TSSuef7DUXCqiIGYuQaaWx26%2BBx0BHGYf9SkQo75CrKT6aVQbTEhTU1VYmv0TMOLf0sd2TdFdwDVbxNw9MLP5i70GOqUBjaf4%2BB7QfBZs6Q07kCcUkRCtVo6buUAz07MbK3hgt0ObCANYWuH5wF7gix%2BRc45YLYd3RR4OrR%2F13XZF2BTLKZZkRMen33HbxFvAot8ZUQ8EcK2bdM%2ByL5dOkfhT%2FqxxNPgNO2cIQBY977yFwFhAPx%2BYC1LhWfTWJ8wrJG29SuUU5%2FRs2uupJ85USWhO6%2FGPDmOYuQhAgVeh1x2y4bKyR%2BbZJUxO&X-Amz-Signature=66f1bb2958e0567d7f7fa567436622bc6c6166986f1bcd3eaf1fc3b0f45bc8fb&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIPPKLE2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQC5GpzKkwMRJzWXoZSXaaM2Nzvot%2BjQ6uF4QvVMN%2FgMgwIhAKizvMr%2FZ8as%2FyvTc0oenn9v5cfOFUPNri%2FIUEagIJRYKv8DCD8QABoMNjM3NDIzMTgzODA1IgzR7e0NLE0lhjXehSMq3AP%2FCjRrkCdP0NKTk21s6R%2FS9M7oq5n%2B%2BD2lu8UF3ZvRw9jf7GRwwCg3xbjEKphQwp4Ll9tStLzv9MnC7BBzn3cgk8qUyCKN6frh5jKHk5lg%2FuBmrje2vSjI8Y5w8f25Xyo5GzN%2BxBbfnVdQsJfI46MxWsx2r3lfqIZSfCeuOOiZOlFl7k3krp0PgfM7zFvAF%2BFKBgo11MqAIEXl6mlS0LqZjerHxzB5RAEut3u2WOe2cRGDCeFoJfRG6nP3mKR4KA4Q0YQXP3ZgFWHDLRVh9CPphNJtVRWSbkHqlWeBpuEH4Cz7kpmEzUlRxAqiO6F0GcoAgOZsIGm4wjQGMJB1pTuHmaWylEemXJzz9WXInsIkkzTnnb0yaqtQ46S%2BR8wUx3uyBtHglQLWjH6greHYeVD3LHFBSzyHIwdWWoFbUhl%2Bwn%2F%2Fa53dluzi1GufS%2BP525H%2BYHZTy1rTWQuPFCCAHLZudCrJYtxYQB3RebWQa5REHZ%2F2nFdfSEw%2FMNGZsdpfKm%2F8tle057v8XYa8fKW1DcmNbFMu1u4jU4BGDAjdsr0U%2FPHVp9bCcv9Ulr4f5rahWz2pbXQFDoR4eJD3VWj0ST4lz0MZX6aPS9kjc5zyzc2BPq7CgbmlNOJYTISivDCP%2Bou9BjqkAQKm1mpKRl1cWo2oRGqw326pgRVcCiEhmub%2FX93vYIwN%2F2KcDpoTSMHIALnfhV0qdewPsZqJR%2BnetSQlSIjqmDn3vEcK3GP%2F8g5Je6bKEjlegMijBCE8e0fXehilLL00J2kqAUu5A5q1f1m9NEFsEB2niASAzJaOFHqcw2pfGZhPw5I2EQkv%2F4hQsj4XPkgQvwtB41NF1Utjd5XFRd2I1n%2BrKkyP&X-Amz-Signature=8e2db70c61058357c82ee3dff8e3bbc7e9a7f758367e88c73595e6183fd18d73&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIPPKLE2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQC5GpzKkwMRJzWXoZSXaaM2Nzvot%2BjQ6uF4QvVMN%2FgMgwIhAKizvMr%2FZ8as%2FyvTc0oenn9v5cfOFUPNri%2FIUEagIJRYKv8DCD8QABoMNjM3NDIzMTgzODA1IgzR7e0NLE0lhjXehSMq3AP%2FCjRrkCdP0NKTk21s6R%2FS9M7oq5n%2B%2BD2lu8UF3ZvRw9jf7GRwwCg3xbjEKphQwp4Ll9tStLzv9MnC7BBzn3cgk8qUyCKN6frh5jKHk5lg%2FuBmrje2vSjI8Y5w8f25Xyo5GzN%2BxBbfnVdQsJfI46MxWsx2r3lfqIZSfCeuOOiZOlFl7k3krp0PgfM7zFvAF%2BFKBgo11MqAIEXl6mlS0LqZjerHxzB5RAEut3u2WOe2cRGDCeFoJfRG6nP3mKR4KA4Q0YQXP3ZgFWHDLRVh9CPphNJtVRWSbkHqlWeBpuEH4Cz7kpmEzUlRxAqiO6F0GcoAgOZsIGm4wjQGMJB1pTuHmaWylEemXJzz9WXInsIkkzTnnb0yaqtQ46S%2BR8wUx3uyBtHglQLWjH6greHYeVD3LHFBSzyHIwdWWoFbUhl%2Bwn%2F%2Fa53dluzi1GufS%2BP525H%2BYHZTy1rTWQuPFCCAHLZudCrJYtxYQB3RebWQa5REHZ%2F2nFdfSEw%2FMNGZsdpfKm%2F8tle057v8XYa8fKW1DcmNbFMu1u4jU4BGDAjdsr0U%2FPHVp9bCcv9Ulr4f5rahWz2pbXQFDoR4eJD3VWj0ST4lz0MZX6aPS9kjc5zyzc2BPq7CgbmlNOJYTISivDCP%2Bou9BjqkAQKm1mpKRl1cWo2oRGqw326pgRVcCiEhmub%2FX93vYIwN%2F2KcDpoTSMHIALnfhV0qdewPsZqJR%2BnetSQlSIjqmDn3vEcK3GP%2F8g5Je6bKEjlegMijBCE8e0fXehilLL00J2kqAUu5A5q1f1m9NEFsEB2niASAzJaOFHqcw2pfGZhPw5I2EQkv%2F4hQsj4XPkgQvwtB41NF1Utjd5XFRd2I1n%2BrKkyP&X-Amz-Signature=a9077a3bd56c613440a0888143bebe0cb3ca41c5f28d21060f4f6439915ed636&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIPPKLE2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQC5GpzKkwMRJzWXoZSXaaM2Nzvot%2BjQ6uF4QvVMN%2FgMgwIhAKizvMr%2FZ8as%2FyvTc0oenn9v5cfOFUPNri%2FIUEagIJRYKv8DCD8QABoMNjM3NDIzMTgzODA1IgzR7e0NLE0lhjXehSMq3AP%2FCjRrkCdP0NKTk21s6R%2FS9M7oq5n%2B%2BD2lu8UF3ZvRw9jf7GRwwCg3xbjEKphQwp4Ll9tStLzv9MnC7BBzn3cgk8qUyCKN6frh5jKHk5lg%2FuBmrje2vSjI8Y5w8f25Xyo5GzN%2BxBbfnVdQsJfI46MxWsx2r3lfqIZSfCeuOOiZOlFl7k3krp0PgfM7zFvAF%2BFKBgo11MqAIEXl6mlS0LqZjerHxzB5RAEut3u2WOe2cRGDCeFoJfRG6nP3mKR4KA4Q0YQXP3ZgFWHDLRVh9CPphNJtVRWSbkHqlWeBpuEH4Cz7kpmEzUlRxAqiO6F0GcoAgOZsIGm4wjQGMJB1pTuHmaWylEemXJzz9WXInsIkkzTnnb0yaqtQ46S%2BR8wUx3uyBtHglQLWjH6greHYeVD3LHFBSzyHIwdWWoFbUhl%2Bwn%2F%2Fa53dluzi1GufS%2BP525H%2BYHZTy1rTWQuPFCCAHLZudCrJYtxYQB3RebWQa5REHZ%2F2nFdfSEw%2FMNGZsdpfKm%2F8tle057v8XYa8fKW1DcmNbFMu1u4jU4BGDAjdsr0U%2FPHVp9bCcv9Ulr4f5rahWz2pbXQFDoR4eJD3VWj0ST4lz0MZX6aPS9kjc5zyzc2BPq7CgbmlNOJYTISivDCP%2Bou9BjqkAQKm1mpKRl1cWo2oRGqw326pgRVcCiEhmub%2FX93vYIwN%2F2KcDpoTSMHIALnfhV0qdewPsZqJR%2BnetSQlSIjqmDn3vEcK3GP%2F8g5Je6bKEjlegMijBCE8e0fXehilLL00J2kqAUu5A5q1f1m9NEFsEB2niASAzJaOFHqcw2pfGZhPw5I2EQkv%2F4hQsj4XPkgQvwtB41NF1Utjd5XFRd2I1n%2BrKkyP&X-Amz-Signature=679abb9b40fd5b513936e4409b2e0393bde305ea464063662a496884218182d6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIPPKLE2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQC5GpzKkwMRJzWXoZSXaaM2Nzvot%2BjQ6uF4QvVMN%2FgMgwIhAKizvMr%2FZ8as%2FyvTc0oenn9v5cfOFUPNri%2FIUEagIJRYKv8DCD8QABoMNjM3NDIzMTgzODA1IgzR7e0NLE0lhjXehSMq3AP%2FCjRrkCdP0NKTk21s6R%2FS9M7oq5n%2B%2BD2lu8UF3ZvRw9jf7GRwwCg3xbjEKphQwp4Ll9tStLzv9MnC7BBzn3cgk8qUyCKN6frh5jKHk5lg%2FuBmrje2vSjI8Y5w8f25Xyo5GzN%2BxBbfnVdQsJfI46MxWsx2r3lfqIZSfCeuOOiZOlFl7k3krp0PgfM7zFvAF%2BFKBgo11MqAIEXl6mlS0LqZjerHxzB5RAEut3u2WOe2cRGDCeFoJfRG6nP3mKR4KA4Q0YQXP3ZgFWHDLRVh9CPphNJtVRWSbkHqlWeBpuEH4Cz7kpmEzUlRxAqiO6F0GcoAgOZsIGm4wjQGMJB1pTuHmaWylEemXJzz9WXInsIkkzTnnb0yaqtQ46S%2BR8wUx3uyBtHglQLWjH6greHYeVD3LHFBSzyHIwdWWoFbUhl%2Bwn%2F%2Fa53dluzi1GufS%2BP525H%2BYHZTy1rTWQuPFCCAHLZudCrJYtxYQB3RebWQa5REHZ%2F2nFdfSEw%2FMNGZsdpfKm%2F8tle057v8XYa8fKW1DcmNbFMu1u4jU4BGDAjdsr0U%2FPHVp9bCcv9Ulr4f5rahWz2pbXQFDoR4eJD3VWj0ST4lz0MZX6aPS9kjc5zyzc2BPq7CgbmlNOJYTISivDCP%2Bou9BjqkAQKm1mpKRl1cWo2oRGqw326pgRVcCiEhmub%2FX93vYIwN%2F2KcDpoTSMHIALnfhV0qdewPsZqJR%2BnetSQlSIjqmDn3vEcK3GP%2F8g5Je6bKEjlegMijBCE8e0fXehilLL00J2kqAUu5A5q1f1m9NEFsEB2niASAzJaOFHqcw2pfGZhPw5I2EQkv%2F4hQsj4XPkgQvwtB41NF1Utjd5XFRd2I1n%2BrKkyP&X-Amz-Signature=0aa7ba417d8c920fdb8dfe10c6c7d0655df62e7924f47f5f74209a34b98da748&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIPPKLE2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQC5GpzKkwMRJzWXoZSXaaM2Nzvot%2BjQ6uF4QvVMN%2FgMgwIhAKizvMr%2FZ8as%2FyvTc0oenn9v5cfOFUPNri%2FIUEagIJRYKv8DCD8QABoMNjM3NDIzMTgzODA1IgzR7e0NLE0lhjXehSMq3AP%2FCjRrkCdP0NKTk21s6R%2FS9M7oq5n%2B%2BD2lu8UF3ZvRw9jf7GRwwCg3xbjEKphQwp4Ll9tStLzv9MnC7BBzn3cgk8qUyCKN6frh5jKHk5lg%2FuBmrje2vSjI8Y5w8f25Xyo5GzN%2BxBbfnVdQsJfI46MxWsx2r3lfqIZSfCeuOOiZOlFl7k3krp0PgfM7zFvAF%2BFKBgo11MqAIEXl6mlS0LqZjerHxzB5RAEut3u2WOe2cRGDCeFoJfRG6nP3mKR4KA4Q0YQXP3ZgFWHDLRVh9CPphNJtVRWSbkHqlWeBpuEH4Cz7kpmEzUlRxAqiO6F0GcoAgOZsIGm4wjQGMJB1pTuHmaWylEemXJzz9WXInsIkkzTnnb0yaqtQ46S%2BR8wUx3uyBtHglQLWjH6greHYeVD3LHFBSzyHIwdWWoFbUhl%2Bwn%2F%2Fa53dluzi1GufS%2BP525H%2BYHZTy1rTWQuPFCCAHLZudCrJYtxYQB3RebWQa5REHZ%2F2nFdfSEw%2FMNGZsdpfKm%2F8tle057v8XYa8fKW1DcmNbFMu1u4jU4BGDAjdsr0U%2FPHVp9bCcv9Ulr4f5rahWz2pbXQFDoR4eJD3VWj0ST4lz0MZX6aPS9kjc5zyzc2BPq7CgbmlNOJYTISivDCP%2Bou9BjqkAQKm1mpKRl1cWo2oRGqw326pgRVcCiEhmub%2FX93vYIwN%2F2KcDpoTSMHIALnfhV0qdewPsZqJR%2BnetSQlSIjqmDn3vEcK3GP%2F8g5Je6bKEjlegMijBCE8e0fXehilLL00J2kqAUu5A5q1f1m9NEFsEB2niASAzJaOFHqcw2pfGZhPw5I2EQkv%2F4hQsj4XPkgQvwtB41NF1Utjd5XFRd2I1n%2BrKkyP&X-Amz-Signature=473b3f61b4a98d53bf9d7bc00c80565bfc57c8028d3d0a8b9e6fcc34a2a443e3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QYV6IUN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDEUAuJTYDttNkduNV90ER9jwptLHnluPENB7fve%2BR5YQIgQfsS%2Fgn3EwSCx7aIe3g9YzCTXophtTwmdNT7Kj7oNKYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMx%2Bf4phixn4HtcFjircAy2vLa8Zge12uReKVIdNprCx5gXt8XwwSR9uTrbYbVovmcghzK0TEOY8qOAOXU5HTTPgFqFrQUjO82pEwOtcyQwGv1sx6Q8jQTR%2FvEQonazdNPFqPaHVaT8a3Z4tbXCK0%2BolbpUB1UYaP6K2lP%2F3cxvjdLgnzt7Ja0xT4xPnG7v18dvK0tXiSa2RtcS14IlUjIzCmtXQof7pPCoijzZ6hqnAhFuyFku9QG1ScoBgFPmeRW%2Fmfd2ISpHTZ2L%2BU5LfYUKExJ4WHQxrBJDHG91TwTv71JAmKXIWrQkweX7dveuw9TpkjccKv4KHq1bnlp5yXGgWP03w0X7tsTKihnLTOUhbV0CSFppNBWGaHb0dUEQlyehFG87LdW1naqxfUCuMycgRVO6PftquFG7b3131HvGTrbxrNWVQpUX3YsPP1ZJlGxAabeYWkls4IUgmvNPOgYiB9Dx1ZDxymdDVocanhdkJXEOFJ4wId2iFXV6epeDmMBSM7pKKF9eq9h1nUFMLAa0MEPgGrZQqxg7LAHBC3J9XNlgmZ%2B0IKNdxiJluFg3TSSuef7DUXCqiIGYuQaaWx26%2BBx0BHGYf9SkQo75CrKT6aVQbTEhTU1VYmv0TMOLf0sd2TdFdwDVbxNw9MLP5i70GOqUBjaf4%2BB7QfBZs6Q07kCcUkRCtVo6buUAz07MbK3hgt0ObCANYWuH5wF7gix%2BRc45YLYd3RR4OrR%2F13XZF2BTLKZZkRMen33HbxFvAot8ZUQ8EcK2bdM%2ByL5dOkfhT%2FqxxNPgNO2cIQBY977yFwFhAPx%2BYC1LhWfTWJ8wrJG29SuUU5%2FRs2uupJ85USWhO6%2FGPDmOYuQhAgVeh1x2y4bKyR%2BbZJUxO&X-Amz-Signature=1f0727b06eb041ecbc73742a00b10c0996b50d1439665de12f6d7dda02007718&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QYV6IUN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDEUAuJTYDttNkduNV90ER9jwptLHnluPENB7fve%2BR5YQIgQfsS%2Fgn3EwSCx7aIe3g9YzCTXophtTwmdNT7Kj7oNKYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMx%2Bf4phixn4HtcFjircAy2vLa8Zge12uReKVIdNprCx5gXt8XwwSR9uTrbYbVovmcghzK0TEOY8qOAOXU5HTTPgFqFrQUjO82pEwOtcyQwGv1sx6Q8jQTR%2FvEQonazdNPFqPaHVaT8a3Z4tbXCK0%2BolbpUB1UYaP6K2lP%2F3cxvjdLgnzt7Ja0xT4xPnG7v18dvK0tXiSa2RtcS14IlUjIzCmtXQof7pPCoijzZ6hqnAhFuyFku9QG1ScoBgFPmeRW%2Fmfd2ISpHTZ2L%2BU5LfYUKExJ4WHQxrBJDHG91TwTv71JAmKXIWrQkweX7dveuw9TpkjccKv4KHq1bnlp5yXGgWP03w0X7tsTKihnLTOUhbV0CSFppNBWGaHb0dUEQlyehFG87LdW1naqxfUCuMycgRVO6PftquFG7b3131HvGTrbxrNWVQpUX3YsPP1ZJlGxAabeYWkls4IUgmvNPOgYiB9Dx1ZDxymdDVocanhdkJXEOFJ4wId2iFXV6epeDmMBSM7pKKF9eq9h1nUFMLAa0MEPgGrZQqxg7LAHBC3J9XNlgmZ%2B0IKNdxiJluFg3TSSuef7DUXCqiIGYuQaaWx26%2BBx0BHGYf9SkQo75CrKT6aVQbTEhTU1VYmv0TMOLf0sd2TdFdwDVbxNw9MLP5i70GOqUBjaf4%2BB7QfBZs6Q07kCcUkRCtVo6buUAz07MbK3hgt0ObCANYWuH5wF7gix%2BRc45YLYd3RR4OrR%2F13XZF2BTLKZZkRMen33HbxFvAot8ZUQ8EcK2bdM%2ByL5dOkfhT%2FqxxNPgNO2cIQBY977yFwFhAPx%2BYC1LhWfTWJ8wrJG29SuUU5%2FRs2uupJ85USWhO6%2FGPDmOYuQhAgVeh1x2y4bKyR%2BbZJUxO&X-Amz-Signature=e147b9c54f975a07ed329726d3c088fea52d572f8cb882cbcbca8789580ca717&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QYV6IUN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDEUAuJTYDttNkduNV90ER9jwptLHnluPENB7fve%2BR5YQIgQfsS%2Fgn3EwSCx7aIe3g9YzCTXophtTwmdNT7Kj7oNKYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMx%2Bf4phixn4HtcFjircAy2vLa8Zge12uReKVIdNprCx5gXt8XwwSR9uTrbYbVovmcghzK0TEOY8qOAOXU5HTTPgFqFrQUjO82pEwOtcyQwGv1sx6Q8jQTR%2FvEQonazdNPFqPaHVaT8a3Z4tbXCK0%2BolbpUB1UYaP6K2lP%2F3cxvjdLgnzt7Ja0xT4xPnG7v18dvK0tXiSa2RtcS14IlUjIzCmtXQof7pPCoijzZ6hqnAhFuyFku9QG1ScoBgFPmeRW%2Fmfd2ISpHTZ2L%2BU5LfYUKExJ4WHQxrBJDHG91TwTv71JAmKXIWrQkweX7dveuw9TpkjccKv4KHq1bnlp5yXGgWP03w0X7tsTKihnLTOUhbV0CSFppNBWGaHb0dUEQlyehFG87LdW1naqxfUCuMycgRVO6PftquFG7b3131HvGTrbxrNWVQpUX3YsPP1ZJlGxAabeYWkls4IUgmvNPOgYiB9Dx1ZDxymdDVocanhdkJXEOFJ4wId2iFXV6epeDmMBSM7pKKF9eq9h1nUFMLAa0MEPgGrZQqxg7LAHBC3J9XNlgmZ%2B0IKNdxiJluFg3TSSuef7DUXCqiIGYuQaaWx26%2BBx0BHGYf9SkQo75CrKT6aVQbTEhTU1VYmv0TMOLf0sd2TdFdwDVbxNw9MLP5i70GOqUBjaf4%2BB7QfBZs6Q07kCcUkRCtVo6buUAz07MbK3hgt0ObCANYWuH5wF7gix%2BRc45YLYd3RR4OrR%2F13XZF2BTLKZZkRMen33HbxFvAot8ZUQ8EcK2bdM%2ByL5dOkfhT%2FqxxNPgNO2cIQBY977yFwFhAPx%2BYC1LhWfTWJ8wrJG29SuUU5%2FRs2uupJ85USWhO6%2FGPDmOYuQhAgVeh1x2y4bKyR%2BbZJUxO&X-Amz-Signature=8707f2878363341083f82e4a5441b6c2495b957dd0f6c9e142c84bcdcd0d529d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QYV6IUN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDEUAuJTYDttNkduNV90ER9jwptLHnluPENB7fve%2BR5YQIgQfsS%2Fgn3EwSCx7aIe3g9YzCTXophtTwmdNT7Kj7oNKYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMx%2Bf4phixn4HtcFjircAy2vLa8Zge12uReKVIdNprCx5gXt8XwwSR9uTrbYbVovmcghzK0TEOY8qOAOXU5HTTPgFqFrQUjO82pEwOtcyQwGv1sx6Q8jQTR%2FvEQonazdNPFqPaHVaT8a3Z4tbXCK0%2BolbpUB1UYaP6K2lP%2F3cxvjdLgnzt7Ja0xT4xPnG7v18dvK0tXiSa2RtcS14IlUjIzCmtXQof7pPCoijzZ6hqnAhFuyFku9QG1ScoBgFPmeRW%2Fmfd2ISpHTZ2L%2BU5LfYUKExJ4WHQxrBJDHG91TwTv71JAmKXIWrQkweX7dveuw9TpkjccKv4KHq1bnlp5yXGgWP03w0X7tsTKihnLTOUhbV0CSFppNBWGaHb0dUEQlyehFG87LdW1naqxfUCuMycgRVO6PftquFG7b3131HvGTrbxrNWVQpUX3YsPP1ZJlGxAabeYWkls4IUgmvNPOgYiB9Dx1ZDxymdDVocanhdkJXEOFJ4wId2iFXV6epeDmMBSM7pKKF9eq9h1nUFMLAa0MEPgGrZQqxg7LAHBC3J9XNlgmZ%2B0IKNdxiJluFg3TSSuef7DUXCqiIGYuQaaWx26%2BBx0BHGYf9SkQo75CrKT6aVQbTEhTU1VYmv0TMOLf0sd2TdFdwDVbxNw9MLP5i70GOqUBjaf4%2BB7QfBZs6Q07kCcUkRCtVo6buUAz07MbK3hgt0ObCANYWuH5wF7gix%2BRc45YLYd3RR4OrR%2F13XZF2BTLKZZkRMen33HbxFvAot8ZUQ8EcK2bdM%2ByL5dOkfhT%2FqxxNPgNO2cIQBY977yFwFhAPx%2BYC1LhWfTWJ8wrJG29SuUU5%2FRs2uupJ85USWhO6%2FGPDmOYuQhAgVeh1x2y4bKyR%2BbZJUxO&X-Amz-Signature=91049bda6b0cc8719f7c34844d117eed6b47181f0ed38e91f534570bcd5c5fbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QYV6IUN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDEUAuJTYDttNkduNV90ER9jwptLHnluPENB7fve%2BR5YQIgQfsS%2Fgn3EwSCx7aIe3g9YzCTXophtTwmdNT7Kj7oNKYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMx%2Bf4phixn4HtcFjircAy2vLa8Zge12uReKVIdNprCx5gXt8XwwSR9uTrbYbVovmcghzK0TEOY8qOAOXU5HTTPgFqFrQUjO82pEwOtcyQwGv1sx6Q8jQTR%2FvEQonazdNPFqPaHVaT8a3Z4tbXCK0%2BolbpUB1UYaP6K2lP%2F3cxvjdLgnzt7Ja0xT4xPnG7v18dvK0tXiSa2RtcS14IlUjIzCmtXQof7pPCoijzZ6hqnAhFuyFku9QG1ScoBgFPmeRW%2Fmfd2ISpHTZ2L%2BU5LfYUKExJ4WHQxrBJDHG91TwTv71JAmKXIWrQkweX7dveuw9TpkjccKv4KHq1bnlp5yXGgWP03w0X7tsTKihnLTOUhbV0CSFppNBWGaHb0dUEQlyehFG87LdW1naqxfUCuMycgRVO6PftquFG7b3131HvGTrbxrNWVQpUX3YsPP1ZJlGxAabeYWkls4IUgmvNPOgYiB9Dx1ZDxymdDVocanhdkJXEOFJ4wId2iFXV6epeDmMBSM7pKKF9eq9h1nUFMLAa0MEPgGrZQqxg7LAHBC3J9XNlgmZ%2B0IKNdxiJluFg3TSSuef7DUXCqiIGYuQaaWx26%2BBx0BHGYf9SkQo75CrKT6aVQbTEhTU1VYmv0TMOLf0sd2TdFdwDVbxNw9MLP5i70GOqUBjaf4%2BB7QfBZs6Q07kCcUkRCtVo6buUAz07MbK3hgt0ObCANYWuH5wF7gix%2BRc45YLYd3RR4OrR%2F13XZF2BTLKZZkRMen33HbxFvAot8ZUQ8EcK2bdM%2ByL5dOkfhT%2FqxxNPgNO2cIQBY977yFwFhAPx%2BYC1LhWfTWJ8wrJG29SuUU5%2FRs2uupJ85USWhO6%2FGPDmOYuQhAgVeh1x2y4bKyR%2BbZJUxO&X-Amz-Signature=caaa3a6c69f092627089d36877bf7d50278585409a8c6207fb319ce0ae6c558b&X-Amz-SignedHeaders=host&x-id=GetObject)
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


