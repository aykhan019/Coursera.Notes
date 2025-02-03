

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBESR6ES%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F1G8rhY4EdtgQJyaRb5uqCv5ZbkSqbgovpazkKz5TYAIgFDciReMK1LMeP8Fv8c5V4E9B0kuX3KNxO3VAcLZtU%2Bgq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDChAPpqHmFETHHAQRircA3TvwqTra1XPGXrHugC0i3TBXVX8DcH5TaSPMPrJFOTtUz8ZDIii6OqFmbVJdCoe%2BIoEFZlZy3F5Z2BVLHz9xG3xOV4iNGGxy59O2MeUq75PynSQ7udoL3XA5f4IYEwBiytHLu17AdyKnteFvaTAC%2F2r86pxMP2fM8eoCod1tg8qlUWqR79nPHmWa4POcswpVp9RYqN5paCQNoLT4mSB1HhPNOmUKqatbA25lnoGupVVtvPZaPDDghp6bJIGbbL2RxqNiLMsyzmkovOIlSNPHvlvmFWtuVelRorF07QVVl09XXrRnKsyQlrYatoodTmZVoDWhenBopBYKpskvAj5Qkws9dWQFSfCOAvs7iwuFaVaNb2Q6Cdwv%2B9%2FAygY6Jo1QgcYmPmbm%2Bs9uraOrjENbV24RvG4OLaC9Jl%2BElGNKSMu0NC0yk4QCJzFjldio6f3F0Q09YTYOdWRrcdqcS5y5%2Fu9A2%2FsWTfkw6hGQsO5NjBTr%2FIpURXTQlYD%2BN%2FgyhrcbbMRKCbSkMjVPjLa99Ql1Wg4aDRnfNtg86dYr7U6v8Vp3aiF%2Bu45REOZ7L%2B6nuOV2JP%2FuJwCxHlasKKISezQsNkt9Q0bnTEoadjZhtpDlC5waekwDUkTNA2uqF%2BrMK6Ng70GOqUBqZ4yGZnEAY4Hu8uZfV6Tynno7MmpH28CH8wVYXQjuSrFvHTWsXrWd8qbnlMYojQvCPvgd%2BjzZ5vY1YOv8ZDtSok4tAuIlHcTilkSDYVqDkRtnOLb%2Fa1rJat%2FZ6KGYc2lIg%2BxRvnu7yGV7Kl3HlTI8h4Up8BAMg5Gq6CsHxxZcFOabZEpp3hsZPUNOHpu0081TURBGy3%2FucclRGhNuh2V8O6cH76b&X-Amz-Signature=812a0d8d3f482fe50a17992c1955120d5597ebdd8f02ec6bb5f2e2d7ec7625d1&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM6QYCEE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD00gtDzmsMPwBJGFaJf8S9IY4ttdbiK0PJR4N2qzUF1wIgcrYRzTzXrXCK%2B2coLLyriX61geRkdCLl0%2Fw5B81boGwq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDEElS%2BjXoUgUJRTl6CrcA6PE5GIsuZzBDHgRtd4U%2FyDh2EU0vOXcASbIRUDjfEaf8oKw2q38UbCVocRsF%2FnNkkzgX8%2FdPgNrwX699fp68k%2BkMqQNDww94Z6fUIGrnNnvSJzEG5FwsPMIJotjm%2FKmCrH1pEnxokhaEd1QlgRbR93WntNpEtFg0r8WiTOhsVWkMwRLDGyntRYU%2BRKWzI9Ax937wcAWasMsWkjOsWi6o%2FkAWcC1KbyinE%2BbbOFtPQLwF9w8H%2BOV7aoCw1COVmG3TxkVh2%2BW%2BTXZ09Mloe0op%2FS%2FgvR%2BzWeyLeKJkGq0CZMaNbyySjfiB4Fu5DTbNmMApgUpqZyU0QQVPUPQV5InAX2XJq2dZyMp6vzAi2ZBqKQn%2F1ZuvRLgwAKuPXPB7SCvQFSQKNkhbSSMC%2FQEFNnEo34xzjEa%2B6IIZTqLfigDYjQErLdJaSVBliRZNO02gT873mC0gz82MylJpb%2BqwUkcJ8D1wU7orbX%2FKUToo2TA90RQRnMOfKIMlGQ5E5QnGf5LhPCAVb0ogXmhnNJ5oA8du8R%2BecNVz0QiAmSF4jbkuqI6%2F%2FYhAdLa9CnPwNsz3ohZduPcZusq4AZlbIRHFwN9SXpuwTL6CIDn%2BDa1ejQAglOU9UfYSqk5eXg3IqVvMP%2BNg70GOqUBUIdD7Ckmpen7cULDdEjTsfZOaNyq21Xc6DJ1lPq8jGwubaDReejBaHsKgvDNI%2FJ9AKpupeLPDJD%2F1MDANa%2BkNt3oHWcLT15aHkA7%2BY4Ut14Uxerq0OWB%2BXNMgxIxrRUjg0fWIvLnWAcYxA5Z8sv3HOsZTTt8gmTpVcGlBTUC1uBap94bEcfhn3K%2FqKVNtEJeAfTKQ0oEPBOETFXMjKZJW9lbusSv&X-Amz-Signature=da618800e927b738693f9f5a7c4e82fee1a93739f1fa264ce0f776fe006a5941&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM6QYCEE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD00gtDzmsMPwBJGFaJf8S9IY4ttdbiK0PJR4N2qzUF1wIgcrYRzTzXrXCK%2B2coLLyriX61geRkdCLl0%2Fw5B81boGwq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDEElS%2BjXoUgUJRTl6CrcA6PE5GIsuZzBDHgRtd4U%2FyDh2EU0vOXcASbIRUDjfEaf8oKw2q38UbCVocRsF%2FnNkkzgX8%2FdPgNrwX699fp68k%2BkMqQNDww94Z6fUIGrnNnvSJzEG5FwsPMIJotjm%2FKmCrH1pEnxokhaEd1QlgRbR93WntNpEtFg0r8WiTOhsVWkMwRLDGyntRYU%2BRKWzI9Ax937wcAWasMsWkjOsWi6o%2FkAWcC1KbyinE%2BbbOFtPQLwF9w8H%2BOV7aoCw1COVmG3TxkVh2%2BW%2BTXZ09Mloe0op%2FS%2FgvR%2BzWeyLeKJkGq0CZMaNbyySjfiB4Fu5DTbNmMApgUpqZyU0QQVPUPQV5InAX2XJq2dZyMp6vzAi2ZBqKQn%2F1ZuvRLgwAKuPXPB7SCvQFSQKNkhbSSMC%2FQEFNnEo34xzjEa%2B6IIZTqLfigDYjQErLdJaSVBliRZNO02gT873mC0gz82MylJpb%2BqwUkcJ8D1wU7orbX%2FKUToo2TA90RQRnMOfKIMlGQ5E5QnGf5LhPCAVb0ogXmhnNJ5oA8du8R%2BecNVz0QiAmSF4jbkuqI6%2F%2FYhAdLa9CnPwNsz3ohZduPcZusq4AZlbIRHFwN9SXpuwTL6CIDn%2BDa1ejQAglOU9UfYSqk5eXg3IqVvMP%2BNg70GOqUBUIdD7Ckmpen7cULDdEjTsfZOaNyq21Xc6DJ1lPq8jGwubaDReejBaHsKgvDNI%2FJ9AKpupeLPDJD%2F1MDANa%2BkNt3oHWcLT15aHkA7%2BY4Ut14Uxerq0OWB%2BXNMgxIxrRUjg0fWIvLnWAcYxA5Z8sv3HOsZTTt8gmTpVcGlBTUC1uBap94bEcfhn3K%2FqKVNtEJeAfTKQ0oEPBOETFXMjKZJW9lbusSv&X-Amz-Signature=5e99f419c6760f8d9700e0059f86a78d6c185dd052fe20e0e4cc5fbe3bcfa54c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM6QYCEE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD00gtDzmsMPwBJGFaJf8S9IY4ttdbiK0PJR4N2qzUF1wIgcrYRzTzXrXCK%2B2coLLyriX61geRkdCLl0%2Fw5B81boGwq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDEElS%2BjXoUgUJRTl6CrcA6PE5GIsuZzBDHgRtd4U%2FyDh2EU0vOXcASbIRUDjfEaf8oKw2q38UbCVocRsF%2FnNkkzgX8%2FdPgNrwX699fp68k%2BkMqQNDww94Z6fUIGrnNnvSJzEG5FwsPMIJotjm%2FKmCrH1pEnxokhaEd1QlgRbR93WntNpEtFg0r8WiTOhsVWkMwRLDGyntRYU%2BRKWzI9Ax937wcAWasMsWkjOsWi6o%2FkAWcC1KbyinE%2BbbOFtPQLwF9w8H%2BOV7aoCw1COVmG3TxkVh2%2BW%2BTXZ09Mloe0op%2FS%2FgvR%2BzWeyLeKJkGq0CZMaNbyySjfiB4Fu5DTbNmMApgUpqZyU0QQVPUPQV5InAX2XJq2dZyMp6vzAi2ZBqKQn%2F1ZuvRLgwAKuPXPB7SCvQFSQKNkhbSSMC%2FQEFNnEo34xzjEa%2B6IIZTqLfigDYjQErLdJaSVBliRZNO02gT873mC0gz82MylJpb%2BqwUkcJ8D1wU7orbX%2FKUToo2TA90RQRnMOfKIMlGQ5E5QnGf5LhPCAVb0ogXmhnNJ5oA8du8R%2BecNVz0QiAmSF4jbkuqI6%2F%2FYhAdLa9CnPwNsz3ohZduPcZusq4AZlbIRHFwN9SXpuwTL6CIDn%2BDa1ejQAglOU9UfYSqk5eXg3IqVvMP%2BNg70GOqUBUIdD7Ckmpen7cULDdEjTsfZOaNyq21Xc6DJ1lPq8jGwubaDReejBaHsKgvDNI%2FJ9AKpupeLPDJD%2F1MDANa%2BkNt3oHWcLT15aHkA7%2BY4Ut14Uxerq0OWB%2BXNMgxIxrRUjg0fWIvLnWAcYxA5Z8sv3HOsZTTt8gmTpVcGlBTUC1uBap94bEcfhn3K%2FqKVNtEJeAfTKQ0oEPBOETFXMjKZJW9lbusSv&X-Amz-Signature=3f07067107798365f0ad5ac40f72c55530926b147a23901f7092933f5fda5e52&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM6QYCEE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD00gtDzmsMPwBJGFaJf8S9IY4ttdbiK0PJR4N2qzUF1wIgcrYRzTzXrXCK%2B2coLLyriX61geRkdCLl0%2Fw5B81boGwq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDEElS%2BjXoUgUJRTl6CrcA6PE5GIsuZzBDHgRtd4U%2FyDh2EU0vOXcASbIRUDjfEaf8oKw2q38UbCVocRsF%2FnNkkzgX8%2FdPgNrwX699fp68k%2BkMqQNDww94Z6fUIGrnNnvSJzEG5FwsPMIJotjm%2FKmCrH1pEnxokhaEd1QlgRbR93WntNpEtFg0r8WiTOhsVWkMwRLDGyntRYU%2BRKWzI9Ax937wcAWasMsWkjOsWi6o%2FkAWcC1KbyinE%2BbbOFtPQLwF9w8H%2BOV7aoCw1COVmG3TxkVh2%2BW%2BTXZ09Mloe0op%2FS%2FgvR%2BzWeyLeKJkGq0CZMaNbyySjfiB4Fu5DTbNmMApgUpqZyU0QQVPUPQV5InAX2XJq2dZyMp6vzAi2ZBqKQn%2F1ZuvRLgwAKuPXPB7SCvQFSQKNkhbSSMC%2FQEFNnEo34xzjEa%2B6IIZTqLfigDYjQErLdJaSVBliRZNO02gT873mC0gz82MylJpb%2BqwUkcJ8D1wU7orbX%2FKUToo2TA90RQRnMOfKIMlGQ5E5QnGf5LhPCAVb0ogXmhnNJ5oA8du8R%2BecNVz0QiAmSF4jbkuqI6%2F%2FYhAdLa9CnPwNsz3ohZduPcZusq4AZlbIRHFwN9SXpuwTL6CIDn%2BDa1ejQAglOU9UfYSqk5eXg3IqVvMP%2BNg70GOqUBUIdD7Ckmpen7cULDdEjTsfZOaNyq21Xc6DJ1lPq8jGwubaDReejBaHsKgvDNI%2FJ9AKpupeLPDJD%2F1MDANa%2BkNt3oHWcLT15aHkA7%2BY4Ut14Uxerq0OWB%2BXNMgxIxrRUjg0fWIvLnWAcYxA5Z8sv3HOsZTTt8gmTpVcGlBTUC1uBap94bEcfhn3K%2FqKVNtEJeAfTKQ0oEPBOETFXMjKZJW9lbusSv&X-Amz-Signature=612d773fff32cd4271ecb38d55d71135da78acd15c1843c735a7e56f27b88f6d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM6QYCEE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD00gtDzmsMPwBJGFaJf8S9IY4ttdbiK0PJR4N2qzUF1wIgcrYRzTzXrXCK%2B2coLLyriX61geRkdCLl0%2Fw5B81boGwq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDEElS%2BjXoUgUJRTl6CrcA6PE5GIsuZzBDHgRtd4U%2FyDh2EU0vOXcASbIRUDjfEaf8oKw2q38UbCVocRsF%2FnNkkzgX8%2FdPgNrwX699fp68k%2BkMqQNDww94Z6fUIGrnNnvSJzEG5FwsPMIJotjm%2FKmCrH1pEnxokhaEd1QlgRbR93WntNpEtFg0r8WiTOhsVWkMwRLDGyntRYU%2BRKWzI9Ax937wcAWasMsWkjOsWi6o%2FkAWcC1KbyinE%2BbbOFtPQLwF9w8H%2BOV7aoCw1COVmG3TxkVh2%2BW%2BTXZ09Mloe0op%2FS%2FgvR%2BzWeyLeKJkGq0CZMaNbyySjfiB4Fu5DTbNmMApgUpqZyU0QQVPUPQV5InAX2XJq2dZyMp6vzAi2ZBqKQn%2F1ZuvRLgwAKuPXPB7SCvQFSQKNkhbSSMC%2FQEFNnEo34xzjEa%2B6IIZTqLfigDYjQErLdJaSVBliRZNO02gT873mC0gz82MylJpb%2BqwUkcJ8D1wU7orbX%2FKUToo2TA90RQRnMOfKIMlGQ5E5QnGf5LhPCAVb0ogXmhnNJ5oA8du8R%2BecNVz0QiAmSF4jbkuqI6%2F%2FYhAdLa9CnPwNsz3ohZduPcZusq4AZlbIRHFwN9SXpuwTL6CIDn%2BDa1ejQAglOU9UfYSqk5eXg3IqVvMP%2BNg70GOqUBUIdD7Ckmpen7cULDdEjTsfZOaNyq21Xc6DJ1lPq8jGwubaDReejBaHsKgvDNI%2FJ9AKpupeLPDJD%2F1MDANa%2BkNt3oHWcLT15aHkA7%2BY4Ut14Uxerq0OWB%2BXNMgxIxrRUjg0fWIvLnWAcYxA5Z8sv3HOsZTTt8gmTpVcGlBTUC1uBap94bEcfhn3K%2FqKVNtEJeAfTKQ0oEPBOETFXMjKZJW9lbusSv&X-Amz-Signature=99d7d66157e1885174d081f77cd5f37c100fb738e4015a425549f94bd7726060&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBESR6ES%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F1G8rhY4EdtgQJyaRb5uqCv5ZbkSqbgovpazkKz5TYAIgFDciReMK1LMeP8Fv8c5V4E9B0kuX3KNxO3VAcLZtU%2Bgq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDChAPpqHmFETHHAQRircA3TvwqTra1XPGXrHugC0i3TBXVX8DcH5TaSPMPrJFOTtUz8ZDIii6OqFmbVJdCoe%2BIoEFZlZy3F5Z2BVLHz9xG3xOV4iNGGxy59O2MeUq75PynSQ7udoL3XA5f4IYEwBiytHLu17AdyKnteFvaTAC%2F2r86pxMP2fM8eoCod1tg8qlUWqR79nPHmWa4POcswpVp9RYqN5paCQNoLT4mSB1HhPNOmUKqatbA25lnoGupVVtvPZaPDDghp6bJIGbbL2RxqNiLMsyzmkovOIlSNPHvlvmFWtuVelRorF07QVVl09XXrRnKsyQlrYatoodTmZVoDWhenBopBYKpskvAj5Qkws9dWQFSfCOAvs7iwuFaVaNb2Q6Cdwv%2B9%2FAygY6Jo1QgcYmPmbm%2Bs9uraOrjENbV24RvG4OLaC9Jl%2BElGNKSMu0NC0yk4QCJzFjldio6f3F0Q09YTYOdWRrcdqcS5y5%2Fu9A2%2FsWTfkw6hGQsO5NjBTr%2FIpURXTQlYD%2BN%2FgyhrcbbMRKCbSkMjVPjLa99Ql1Wg4aDRnfNtg86dYr7U6v8Vp3aiF%2Bu45REOZ7L%2B6nuOV2JP%2FuJwCxHlasKKISezQsNkt9Q0bnTEoadjZhtpDlC5waekwDUkTNA2uqF%2BrMK6Ng70GOqUBqZ4yGZnEAY4Hu8uZfV6Tynno7MmpH28CH8wVYXQjuSrFvHTWsXrWd8qbnlMYojQvCPvgd%2BjzZ5vY1YOv8ZDtSok4tAuIlHcTilkSDYVqDkRtnOLb%2Fa1rJat%2FZ6KGYc2lIg%2BxRvnu7yGV7Kl3HlTI8h4Up8BAMg5Gq6CsHxxZcFOabZEpp3hsZPUNOHpu0081TURBGy3%2FucclRGhNuh2V8O6cH76b&X-Amz-Signature=50f7ec66a7a9e03607a67698b8f43d77a5ae55cbe3254cc117744cd7b12d4899&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBESR6ES%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F1G8rhY4EdtgQJyaRb5uqCv5ZbkSqbgovpazkKz5TYAIgFDciReMK1LMeP8Fv8c5V4E9B0kuX3KNxO3VAcLZtU%2Bgq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDChAPpqHmFETHHAQRircA3TvwqTra1XPGXrHugC0i3TBXVX8DcH5TaSPMPrJFOTtUz8ZDIii6OqFmbVJdCoe%2BIoEFZlZy3F5Z2BVLHz9xG3xOV4iNGGxy59O2MeUq75PynSQ7udoL3XA5f4IYEwBiytHLu17AdyKnteFvaTAC%2F2r86pxMP2fM8eoCod1tg8qlUWqR79nPHmWa4POcswpVp9RYqN5paCQNoLT4mSB1HhPNOmUKqatbA25lnoGupVVtvPZaPDDghp6bJIGbbL2RxqNiLMsyzmkovOIlSNPHvlvmFWtuVelRorF07QVVl09XXrRnKsyQlrYatoodTmZVoDWhenBopBYKpskvAj5Qkws9dWQFSfCOAvs7iwuFaVaNb2Q6Cdwv%2B9%2FAygY6Jo1QgcYmPmbm%2Bs9uraOrjENbV24RvG4OLaC9Jl%2BElGNKSMu0NC0yk4QCJzFjldio6f3F0Q09YTYOdWRrcdqcS5y5%2Fu9A2%2FsWTfkw6hGQsO5NjBTr%2FIpURXTQlYD%2BN%2FgyhrcbbMRKCbSkMjVPjLa99Ql1Wg4aDRnfNtg86dYr7U6v8Vp3aiF%2Bu45REOZ7L%2B6nuOV2JP%2FuJwCxHlasKKISezQsNkt9Q0bnTEoadjZhtpDlC5waekwDUkTNA2uqF%2BrMK6Ng70GOqUBqZ4yGZnEAY4Hu8uZfV6Tynno7MmpH28CH8wVYXQjuSrFvHTWsXrWd8qbnlMYojQvCPvgd%2BjzZ5vY1YOv8ZDtSok4tAuIlHcTilkSDYVqDkRtnOLb%2Fa1rJat%2FZ6KGYc2lIg%2BxRvnu7yGV7Kl3HlTI8h4Up8BAMg5Gq6CsHxxZcFOabZEpp3hsZPUNOHpu0081TURBGy3%2FucclRGhNuh2V8O6cH76b&X-Amz-Signature=0d6f5fd02d9148896fe006ba4dbfcf702664c76cae328dd8903c250ea5fca5bc&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBESR6ES%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F1G8rhY4EdtgQJyaRb5uqCv5ZbkSqbgovpazkKz5TYAIgFDciReMK1LMeP8Fv8c5V4E9B0kuX3KNxO3VAcLZtU%2Bgq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDChAPpqHmFETHHAQRircA3TvwqTra1XPGXrHugC0i3TBXVX8DcH5TaSPMPrJFOTtUz8ZDIii6OqFmbVJdCoe%2BIoEFZlZy3F5Z2BVLHz9xG3xOV4iNGGxy59O2MeUq75PynSQ7udoL3XA5f4IYEwBiytHLu17AdyKnteFvaTAC%2F2r86pxMP2fM8eoCod1tg8qlUWqR79nPHmWa4POcswpVp9RYqN5paCQNoLT4mSB1HhPNOmUKqatbA25lnoGupVVtvPZaPDDghp6bJIGbbL2RxqNiLMsyzmkovOIlSNPHvlvmFWtuVelRorF07QVVl09XXrRnKsyQlrYatoodTmZVoDWhenBopBYKpskvAj5Qkws9dWQFSfCOAvs7iwuFaVaNb2Q6Cdwv%2B9%2FAygY6Jo1QgcYmPmbm%2Bs9uraOrjENbV24RvG4OLaC9Jl%2BElGNKSMu0NC0yk4QCJzFjldio6f3F0Q09YTYOdWRrcdqcS5y5%2Fu9A2%2FsWTfkw6hGQsO5NjBTr%2FIpURXTQlYD%2BN%2FgyhrcbbMRKCbSkMjVPjLa99Ql1Wg4aDRnfNtg86dYr7U6v8Vp3aiF%2Bu45REOZ7L%2B6nuOV2JP%2FuJwCxHlasKKISezQsNkt9Q0bnTEoadjZhtpDlC5waekwDUkTNA2uqF%2BrMK6Ng70GOqUBqZ4yGZnEAY4Hu8uZfV6Tynno7MmpH28CH8wVYXQjuSrFvHTWsXrWd8qbnlMYojQvCPvgd%2BjzZ5vY1YOv8ZDtSok4tAuIlHcTilkSDYVqDkRtnOLb%2Fa1rJat%2FZ6KGYc2lIg%2BxRvnu7yGV7Kl3HlTI8h4Up8BAMg5Gq6CsHxxZcFOabZEpp3hsZPUNOHpu0081TURBGy3%2FucclRGhNuh2V8O6cH76b&X-Amz-Signature=44028676b9265f78026b95a550f298ae243009012ada28686bcbebec1304883b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBESR6ES%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F1G8rhY4EdtgQJyaRb5uqCv5ZbkSqbgovpazkKz5TYAIgFDciReMK1LMeP8Fv8c5V4E9B0kuX3KNxO3VAcLZtU%2Bgq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDChAPpqHmFETHHAQRircA3TvwqTra1XPGXrHugC0i3TBXVX8DcH5TaSPMPrJFOTtUz8ZDIii6OqFmbVJdCoe%2BIoEFZlZy3F5Z2BVLHz9xG3xOV4iNGGxy59O2MeUq75PynSQ7udoL3XA5f4IYEwBiytHLu17AdyKnteFvaTAC%2F2r86pxMP2fM8eoCod1tg8qlUWqR79nPHmWa4POcswpVp9RYqN5paCQNoLT4mSB1HhPNOmUKqatbA25lnoGupVVtvPZaPDDghp6bJIGbbL2RxqNiLMsyzmkovOIlSNPHvlvmFWtuVelRorF07QVVl09XXrRnKsyQlrYatoodTmZVoDWhenBopBYKpskvAj5Qkws9dWQFSfCOAvs7iwuFaVaNb2Q6Cdwv%2B9%2FAygY6Jo1QgcYmPmbm%2Bs9uraOrjENbV24RvG4OLaC9Jl%2BElGNKSMu0NC0yk4QCJzFjldio6f3F0Q09YTYOdWRrcdqcS5y5%2Fu9A2%2FsWTfkw6hGQsO5NjBTr%2FIpURXTQlYD%2BN%2FgyhrcbbMRKCbSkMjVPjLa99Ql1Wg4aDRnfNtg86dYr7U6v8Vp3aiF%2Bu45REOZ7L%2B6nuOV2JP%2FuJwCxHlasKKISezQsNkt9Q0bnTEoadjZhtpDlC5waekwDUkTNA2uqF%2BrMK6Ng70GOqUBqZ4yGZnEAY4Hu8uZfV6Tynno7MmpH28CH8wVYXQjuSrFvHTWsXrWd8qbnlMYojQvCPvgd%2BjzZ5vY1YOv8ZDtSok4tAuIlHcTilkSDYVqDkRtnOLb%2Fa1rJat%2FZ6KGYc2lIg%2BxRvnu7yGV7Kl3HlTI8h4Up8BAMg5Gq6CsHxxZcFOabZEpp3hsZPUNOHpu0081TURBGy3%2FucclRGhNuh2V8O6cH76b&X-Amz-Signature=a93d34f5b66256b771a74907d2a257a9f2b77728ece876c0d4463da008a4718b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBESR6ES%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F1G8rhY4EdtgQJyaRb5uqCv5ZbkSqbgovpazkKz5TYAIgFDciReMK1LMeP8Fv8c5V4E9B0kuX3KNxO3VAcLZtU%2Bgq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDChAPpqHmFETHHAQRircA3TvwqTra1XPGXrHugC0i3TBXVX8DcH5TaSPMPrJFOTtUz8ZDIii6OqFmbVJdCoe%2BIoEFZlZy3F5Z2BVLHz9xG3xOV4iNGGxy59O2MeUq75PynSQ7udoL3XA5f4IYEwBiytHLu17AdyKnteFvaTAC%2F2r86pxMP2fM8eoCod1tg8qlUWqR79nPHmWa4POcswpVp9RYqN5paCQNoLT4mSB1HhPNOmUKqatbA25lnoGupVVtvPZaPDDghp6bJIGbbL2RxqNiLMsyzmkovOIlSNPHvlvmFWtuVelRorF07QVVl09XXrRnKsyQlrYatoodTmZVoDWhenBopBYKpskvAj5Qkws9dWQFSfCOAvs7iwuFaVaNb2Q6Cdwv%2B9%2FAygY6Jo1QgcYmPmbm%2Bs9uraOrjENbV24RvG4OLaC9Jl%2BElGNKSMu0NC0yk4QCJzFjldio6f3F0Q09YTYOdWRrcdqcS5y5%2Fu9A2%2FsWTfkw6hGQsO5NjBTr%2FIpURXTQlYD%2BN%2FgyhrcbbMRKCbSkMjVPjLa99Ql1Wg4aDRnfNtg86dYr7U6v8Vp3aiF%2Bu45REOZ7L%2B6nuOV2JP%2FuJwCxHlasKKISezQsNkt9Q0bnTEoadjZhtpDlC5waekwDUkTNA2uqF%2BrMK6Ng70GOqUBqZ4yGZnEAY4Hu8uZfV6Tynno7MmpH28CH8wVYXQjuSrFvHTWsXrWd8qbnlMYojQvCPvgd%2BjzZ5vY1YOv8ZDtSok4tAuIlHcTilkSDYVqDkRtnOLb%2Fa1rJat%2FZ6KGYc2lIg%2BxRvnu7yGV7Kl3HlTI8h4Up8BAMg5Gq6CsHxxZcFOabZEpp3hsZPUNOHpu0081TURBGy3%2FucclRGhNuh2V8O6cH76b&X-Amz-Signature=dbd52698d2ab62b23ccf17e6e8819fef451165db646e74055946583796001977&X-Amz-SignedHeaders=host&x-id=GetObject)
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


