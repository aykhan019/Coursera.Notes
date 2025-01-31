

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYZ2M3LK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHRYlc6JCIOseTT3IigJFRx%2BrB4S560PavS9Rh0hTwCHAiEAy3Ka9D4enIWfrMJrizQYUIfoebrGpJ4gF1pE503JtE4qiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEESK4kxXbVmNR90MCrcA8suKW4k0UZKpBL8SAwRSTknTwrPhG2c99w7s6oMm8G3DkxuNxTBan%2BATy%2FJQmwgdZ8enasVpNDG3mpcQthxyLGv6AWWtfvQ1PwfEwF0QGtt5XWYeFBm5Hay4w35BKFq6yp%2F8VfDfZSSIW86447amkG479pl%2B0VsVkod2Em4dELyEFEVc3S5OD%2B93emO%2BnMgiWHsXp%2FwyaK%2BKZIDLBplBlMANn12WyQpx2%2F%2F%2BpCNi2xtmUGJojVm5dfrk1fJjywWN5XJA2%2Bj1TwsA8NxXf5EY01TRkx3lwvaPZG16%2Bm0ibfKKZsyjm%2FKjAmddTFwJO75xA3sz%2BEos%2BdxWpn7hSp4suQq7hfVEVvnbVoKi8NfNlvLLjyyvDoZRf8kM%2BQzbzAqRT%2FB54c7OBJZ8rmaE%2BD45Tj4rN7GxA%2BoJdKkcZzcSVefaaEowTX3i3D7ngnlmAkEWHELemgyMOTm%2BAdN5CAFmCKArhTLK%2FGIyVahn%2F2CFyRPLL13GeWp9v8aJWiF2Gtxv6EXggL5CIlVxrc9c05%2Bl7taNxWlTzVDcCBYcyiixiN3Z3ub5ZIuSKMp0T7N04RmUAm2yycfO3Qi%2BiidSpSdgDt%2BOGqNXBXja9h7yhi6cr12BB3mmmKoVMnV%2FBeZMIPt8bwGOqUBRgisCTOWioNYZSZjnrsCne6PeZKU3zEQMOYuuzRwNbhjnAG641jXvUBmdHf54MW29on4JTKp7m0yJ1REgJhPrHQHFPUQ70jcVr2EkjerZ4m9lUv7%2BtrzBmXv%2FQMGQCsLdjZTr4jdoelZPAR4MEW3Fzq%2F1%2BU3Cl59TpYThzDYVkEo1VJR5Fk3JNJNTmk0SbQQesvzzx8URrC981QJTAMundMSeGhp&X-Amz-Signature=deaedce4873b58c9a041eaf9662af74e868170b276937b31c1a1416e0e4f09ee&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R5H5FU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMc6xVb6nt48rFxvNX3qMiJxQAnpv6PcwkS4D6vdhm8gIhAOwdZeZ2zQhRlepPEGwm4gRsLiWlm8mzF2OUci4rsM0WKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXo%2FMrYicPrQE5hZUq3AONnSShFYJWKCvdgGd0Lj2VwNteN5I6tO9BdMXWd%2BSEUNYV3s%2BjdDhDNZBfnNOg8NWC%2FDf6e%2BQlPBchqjZCHLKSSEcKxviVldPudAUe%2BAiUFheHrtCCHo4mB13nAlLfSJVJ2WoCWr1LxtL2CmnR6JRR2pbymhYWURg4PkMaWmswCzWP8QApqtylQR26myemzrORDZKIJXhj%2FqoTPsWVTgWLGf0VU4wa8SMWzxmoL0jfn%2Br6NZShBtd%2B9%2BOamPYE7kFcCbEL94qJfWecH6atqmk2hvDHuNrEzU3%2FnUaSeRZ%2B0LU5djmvkAD5JX3Uu3az%2F2O%2Br08Tr433B74zvPxtdLrpeEhPp2voHabuIhj6vEDX45EhD5pF7e6t%2B0k%2BfBPlTUnBi8orrP%2FH43nOSrSwylSTwGsaK4tQ5ssfHyZ4yihwbuylYiB%2FRlvFDSDkN0XAPBToNn41oqZ9AsyXQQxan2mwGglHd3r9PMYuLRI9s1UBNAjyHN%2FYFxsgOlU3bnE8CEiFVV60TY1icl%2BeWf6MgcORq6e5uU7VBId4%2BUuQl%2FB0wTto1lmvkCKCX8t3IjChahDzEE9UxM0JzzrguBc3syMNJ%2FrMRJjBvoPpxobW3eQSIP%2BGOGhs6w1mPWDIcDCF4vG8BjqkASeTVoHuq83EyUdVo6wrvj6IKMPLKwOEmVYJAqXmxniU2yEBp4Xmv8ugbc8qhW%2Fqv8RqzxjMbZ0eS8FGKArDsgoyf7p%2FKoXGFY9zI22rKZeDUHWIuroOGl8DS9bqqLw%2FZ9%2FA3m%2FENp60lJBKp73eYcjq%2FpkKXx7x4bz%2FjksPkOb7tIQkJiDuL8Y%2BlvY7zfSQBq9MAkyZhcma1dVKCtqjzIadP3ix&X-Amz-Signature=e9eb3df0ebf6d98c27c044fdafd85fb7b2de7cd96610f4c76a96a62a0c849420&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R5H5FU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMc6xVb6nt48rFxvNX3qMiJxQAnpv6PcwkS4D6vdhm8gIhAOwdZeZ2zQhRlepPEGwm4gRsLiWlm8mzF2OUci4rsM0WKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXo%2FMrYicPrQE5hZUq3AONnSShFYJWKCvdgGd0Lj2VwNteN5I6tO9BdMXWd%2BSEUNYV3s%2BjdDhDNZBfnNOg8NWC%2FDf6e%2BQlPBchqjZCHLKSSEcKxviVldPudAUe%2BAiUFheHrtCCHo4mB13nAlLfSJVJ2WoCWr1LxtL2CmnR6JRR2pbymhYWURg4PkMaWmswCzWP8QApqtylQR26myemzrORDZKIJXhj%2FqoTPsWVTgWLGf0VU4wa8SMWzxmoL0jfn%2Br6NZShBtd%2B9%2BOamPYE7kFcCbEL94qJfWecH6atqmk2hvDHuNrEzU3%2FnUaSeRZ%2B0LU5djmvkAD5JX3Uu3az%2F2O%2Br08Tr433B74zvPxtdLrpeEhPp2voHabuIhj6vEDX45EhD5pF7e6t%2B0k%2BfBPlTUnBi8orrP%2FH43nOSrSwylSTwGsaK4tQ5ssfHyZ4yihwbuylYiB%2FRlvFDSDkN0XAPBToNn41oqZ9AsyXQQxan2mwGglHd3r9PMYuLRI9s1UBNAjyHN%2FYFxsgOlU3bnE8CEiFVV60TY1icl%2BeWf6MgcORq6e5uU7VBId4%2BUuQl%2FB0wTto1lmvkCKCX8t3IjChahDzEE9UxM0JzzrguBc3syMNJ%2FrMRJjBvoPpxobW3eQSIP%2BGOGhs6w1mPWDIcDCF4vG8BjqkASeTVoHuq83EyUdVo6wrvj6IKMPLKwOEmVYJAqXmxniU2yEBp4Xmv8ugbc8qhW%2Fqv8RqzxjMbZ0eS8FGKArDsgoyf7p%2FKoXGFY9zI22rKZeDUHWIuroOGl8DS9bqqLw%2FZ9%2FA3m%2FENp60lJBKp73eYcjq%2FpkKXx7x4bz%2FjksPkOb7tIQkJiDuL8Y%2BlvY7zfSQBq9MAkyZhcma1dVKCtqjzIadP3ix&X-Amz-Signature=b88fa079b0b3e70f990f480e60440bf616897ad64e1159655a60e8028d546e71&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R5H5FU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMc6xVb6nt48rFxvNX3qMiJxQAnpv6PcwkS4D6vdhm8gIhAOwdZeZ2zQhRlepPEGwm4gRsLiWlm8mzF2OUci4rsM0WKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXo%2FMrYicPrQE5hZUq3AONnSShFYJWKCvdgGd0Lj2VwNteN5I6tO9BdMXWd%2BSEUNYV3s%2BjdDhDNZBfnNOg8NWC%2FDf6e%2BQlPBchqjZCHLKSSEcKxviVldPudAUe%2BAiUFheHrtCCHo4mB13nAlLfSJVJ2WoCWr1LxtL2CmnR6JRR2pbymhYWURg4PkMaWmswCzWP8QApqtylQR26myemzrORDZKIJXhj%2FqoTPsWVTgWLGf0VU4wa8SMWzxmoL0jfn%2Br6NZShBtd%2B9%2BOamPYE7kFcCbEL94qJfWecH6atqmk2hvDHuNrEzU3%2FnUaSeRZ%2B0LU5djmvkAD5JX3Uu3az%2F2O%2Br08Tr433B74zvPxtdLrpeEhPp2voHabuIhj6vEDX45EhD5pF7e6t%2B0k%2BfBPlTUnBi8orrP%2FH43nOSrSwylSTwGsaK4tQ5ssfHyZ4yihwbuylYiB%2FRlvFDSDkN0XAPBToNn41oqZ9AsyXQQxan2mwGglHd3r9PMYuLRI9s1UBNAjyHN%2FYFxsgOlU3bnE8CEiFVV60TY1icl%2BeWf6MgcORq6e5uU7VBId4%2BUuQl%2FB0wTto1lmvkCKCX8t3IjChahDzEE9UxM0JzzrguBc3syMNJ%2FrMRJjBvoPpxobW3eQSIP%2BGOGhs6w1mPWDIcDCF4vG8BjqkASeTVoHuq83EyUdVo6wrvj6IKMPLKwOEmVYJAqXmxniU2yEBp4Xmv8ugbc8qhW%2Fqv8RqzxjMbZ0eS8FGKArDsgoyf7p%2FKoXGFY9zI22rKZeDUHWIuroOGl8DS9bqqLw%2FZ9%2FA3m%2FENp60lJBKp73eYcjq%2FpkKXx7x4bz%2FjksPkOb7tIQkJiDuL8Y%2BlvY7zfSQBq9MAkyZhcma1dVKCtqjzIadP3ix&X-Amz-Signature=d9ac4f079346af0315b10ef84c2a8bd450a3cc54804385dfb7ae05ce81906a16&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R5H5FU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMc6xVb6nt48rFxvNX3qMiJxQAnpv6PcwkS4D6vdhm8gIhAOwdZeZ2zQhRlepPEGwm4gRsLiWlm8mzF2OUci4rsM0WKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXo%2FMrYicPrQE5hZUq3AONnSShFYJWKCvdgGd0Lj2VwNteN5I6tO9BdMXWd%2BSEUNYV3s%2BjdDhDNZBfnNOg8NWC%2FDf6e%2BQlPBchqjZCHLKSSEcKxviVldPudAUe%2BAiUFheHrtCCHo4mB13nAlLfSJVJ2WoCWr1LxtL2CmnR6JRR2pbymhYWURg4PkMaWmswCzWP8QApqtylQR26myemzrORDZKIJXhj%2FqoTPsWVTgWLGf0VU4wa8SMWzxmoL0jfn%2Br6NZShBtd%2B9%2BOamPYE7kFcCbEL94qJfWecH6atqmk2hvDHuNrEzU3%2FnUaSeRZ%2B0LU5djmvkAD5JX3Uu3az%2F2O%2Br08Tr433B74zvPxtdLrpeEhPp2voHabuIhj6vEDX45EhD5pF7e6t%2B0k%2BfBPlTUnBi8orrP%2FH43nOSrSwylSTwGsaK4tQ5ssfHyZ4yihwbuylYiB%2FRlvFDSDkN0XAPBToNn41oqZ9AsyXQQxan2mwGglHd3r9PMYuLRI9s1UBNAjyHN%2FYFxsgOlU3bnE8CEiFVV60TY1icl%2BeWf6MgcORq6e5uU7VBId4%2BUuQl%2FB0wTto1lmvkCKCX8t3IjChahDzEE9UxM0JzzrguBc3syMNJ%2FrMRJjBvoPpxobW3eQSIP%2BGOGhs6w1mPWDIcDCF4vG8BjqkASeTVoHuq83EyUdVo6wrvj6IKMPLKwOEmVYJAqXmxniU2yEBp4Xmv8ugbc8qhW%2Fqv8RqzxjMbZ0eS8FGKArDsgoyf7p%2FKoXGFY9zI22rKZeDUHWIuroOGl8DS9bqqLw%2FZ9%2FA3m%2FENp60lJBKp73eYcjq%2FpkKXx7x4bz%2FjksPkOb7tIQkJiDuL8Y%2BlvY7zfSQBq9MAkyZhcma1dVKCtqjzIadP3ix&X-Amz-Signature=0efebb808b78263d8f759d3097e433607fe23ee11b0ed2facb747ff4fb69c9ff&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R5H5FU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMc6xVb6nt48rFxvNX3qMiJxQAnpv6PcwkS4D6vdhm8gIhAOwdZeZ2zQhRlepPEGwm4gRsLiWlm8mzF2OUci4rsM0WKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXo%2FMrYicPrQE5hZUq3AONnSShFYJWKCvdgGd0Lj2VwNteN5I6tO9BdMXWd%2BSEUNYV3s%2BjdDhDNZBfnNOg8NWC%2FDf6e%2BQlPBchqjZCHLKSSEcKxviVldPudAUe%2BAiUFheHrtCCHo4mB13nAlLfSJVJ2WoCWr1LxtL2CmnR6JRR2pbymhYWURg4PkMaWmswCzWP8QApqtylQR26myemzrORDZKIJXhj%2FqoTPsWVTgWLGf0VU4wa8SMWzxmoL0jfn%2Br6NZShBtd%2B9%2BOamPYE7kFcCbEL94qJfWecH6atqmk2hvDHuNrEzU3%2FnUaSeRZ%2B0LU5djmvkAD5JX3Uu3az%2F2O%2Br08Tr433B74zvPxtdLrpeEhPp2voHabuIhj6vEDX45EhD5pF7e6t%2B0k%2BfBPlTUnBi8orrP%2FH43nOSrSwylSTwGsaK4tQ5ssfHyZ4yihwbuylYiB%2FRlvFDSDkN0XAPBToNn41oqZ9AsyXQQxan2mwGglHd3r9PMYuLRI9s1UBNAjyHN%2FYFxsgOlU3bnE8CEiFVV60TY1icl%2BeWf6MgcORq6e5uU7VBId4%2BUuQl%2FB0wTto1lmvkCKCX8t3IjChahDzEE9UxM0JzzrguBc3syMNJ%2FrMRJjBvoPpxobW3eQSIP%2BGOGhs6w1mPWDIcDCF4vG8BjqkASeTVoHuq83EyUdVo6wrvj6IKMPLKwOEmVYJAqXmxniU2yEBp4Xmv8ugbc8qhW%2Fqv8RqzxjMbZ0eS8FGKArDsgoyf7p%2FKoXGFY9zI22rKZeDUHWIuroOGl8DS9bqqLw%2FZ9%2FA3m%2FENp60lJBKp73eYcjq%2FpkKXx7x4bz%2FjksPkOb7tIQkJiDuL8Y%2BlvY7zfSQBq9MAkyZhcma1dVKCtqjzIadP3ix&X-Amz-Signature=c47ed651da324a056811088f11e385f2dc72e5aad40b62f0cb465e57caf038b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYZ2M3LK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHRYlc6JCIOseTT3IigJFRx%2BrB4S560PavS9Rh0hTwCHAiEAy3Ka9D4enIWfrMJrizQYUIfoebrGpJ4gF1pE503JtE4qiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEESK4kxXbVmNR90MCrcA8suKW4k0UZKpBL8SAwRSTknTwrPhG2c99w7s6oMm8G3DkxuNxTBan%2BATy%2FJQmwgdZ8enasVpNDG3mpcQthxyLGv6AWWtfvQ1PwfEwF0QGtt5XWYeFBm5Hay4w35BKFq6yp%2F8VfDfZSSIW86447amkG479pl%2B0VsVkod2Em4dELyEFEVc3S5OD%2B93emO%2BnMgiWHsXp%2FwyaK%2BKZIDLBplBlMANn12WyQpx2%2F%2F%2BpCNi2xtmUGJojVm5dfrk1fJjywWN5XJA2%2Bj1TwsA8NxXf5EY01TRkx3lwvaPZG16%2Bm0ibfKKZsyjm%2FKjAmddTFwJO75xA3sz%2BEos%2BdxWpn7hSp4suQq7hfVEVvnbVoKi8NfNlvLLjyyvDoZRf8kM%2BQzbzAqRT%2FB54c7OBJZ8rmaE%2BD45Tj4rN7GxA%2BoJdKkcZzcSVefaaEowTX3i3D7ngnlmAkEWHELemgyMOTm%2BAdN5CAFmCKArhTLK%2FGIyVahn%2F2CFyRPLL13GeWp9v8aJWiF2Gtxv6EXggL5CIlVxrc9c05%2Bl7taNxWlTzVDcCBYcyiixiN3Z3ub5ZIuSKMp0T7N04RmUAm2yycfO3Qi%2BiidSpSdgDt%2BOGqNXBXja9h7yhi6cr12BB3mmmKoVMnV%2FBeZMIPt8bwGOqUBRgisCTOWioNYZSZjnrsCne6PeZKU3zEQMOYuuzRwNbhjnAG641jXvUBmdHf54MW29on4JTKp7m0yJ1REgJhPrHQHFPUQ70jcVr2EkjerZ4m9lUv7%2BtrzBmXv%2FQMGQCsLdjZTr4jdoelZPAR4MEW3Fzq%2F1%2BU3Cl59TpYThzDYVkEo1VJR5Fk3JNJNTmk0SbQQesvzzx8URrC981QJTAMundMSeGhp&X-Amz-Signature=6cb9cf954836c58fa868a90b62179c6cefc117497fec096a62fc641739d64dd1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYZ2M3LK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHRYlc6JCIOseTT3IigJFRx%2BrB4S560PavS9Rh0hTwCHAiEAy3Ka9D4enIWfrMJrizQYUIfoebrGpJ4gF1pE503JtE4qiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEESK4kxXbVmNR90MCrcA8suKW4k0UZKpBL8SAwRSTknTwrPhG2c99w7s6oMm8G3DkxuNxTBan%2BATy%2FJQmwgdZ8enasVpNDG3mpcQthxyLGv6AWWtfvQ1PwfEwF0QGtt5XWYeFBm5Hay4w35BKFq6yp%2F8VfDfZSSIW86447amkG479pl%2B0VsVkod2Em4dELyEFEVc3S5OD%2B93emO%2BnMgiWHsXp%2FwyaK%2BKZIDLBplBlMANn12WyQpx2%2F%2F%2BpCNi2xtmUGJojVm5dfrk1fJjywWN5XJA2%2Bj1TwsA8NxXf5EY01TRkx3lwvaPZG16%2Bm0ibfKKZsyjm%2FKjAmddTFwJO75xA3sz%2BEos%2BdxWpn7hSp4suQq7hfVEVvnbVoKi8NfNlvLLjyyvDoZRf8kM%2BQzbzAqRT%2FB54c7OBJZ8rmaE%2BD45Tj4rN7GxA%2BoJdKkcZzcSVefaaEowTX3i3D7ngnlmAkEWHELemgyMOTm%2BAdN5CAFmCKArhTLK%2FGIyVahn%2F2CFyRPLL13GeWp9v8aJWiF2Gtxv6EXggL5CIlVxrc9c05%2Bl7taNxWlTzVDcCBYcyiixiN3Z3ub5ZIuSKMp0T7N04RmUAm2yycfO3Qi%2BiidSpSdgDt%2BOGqNXBXja9h7yhi6cr12BB3mmmKoVMnV%2FBeZMIPt8bwGOqUBRgisCTOWioNYZSZjnrsCne6PeZKU3zEQMOYuuzRwNbhjnAG641jXvUBmdHf54MW29on4JTKp7m0yJ1REgJhPrHQHFPUQ70jcVr2EkjerZ4m9lUv7%2BtrzBmXv%2FQMGQCsLdjZTr4jdoelZPAR4MEW3Fzq%2F1%2BU3Cl59TpYThzDYVkEo1VJR5Fk3JNJNTmk0SbQQesvzzx8URrC981QJTAMundMSeGhp&X-Amz-Signature=35300e70ca155bc6817af4324cedbeb6e371250ea7fae3405dfbf8f973f5933a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYZ2M3LK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHRYlc6JCIOseTT3IigJFRx%2BrB4S560PavS9Rh0hTwCHAiEAy3Ka9D4enIWfrMJrizQYUIfoebrGpJ4gF1pE503JtE4qiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEESK4kxXbVmNR90MCrcA8suKW4k0UZKpBL8SAwRSTknTwrPhG2c99w7s6oMm8G3DkxuNxTBan%2BATy%2FJQmwgdZ8enasVpNDG3mpcQthxyLGv6AWWtfvQ1PwfEwF0QGtt5XWYeFBm5Hay4w35BKFq6yp%2F8VfDfZSSIW86447amkG479pl%2B0VsVkod2Em4dELyEFEVc3S5OD%2B93emO%2BnMgiWHsXp%2FwyaK%2BKZIDLBplBlMANn12WyQpx2%2F%2F%2BpCNi2xtmUGJojVm5dfrk1fJjywWN5XJA2%2Bj1TwsA8NxXf5EY01TRkx3lwvaPZG16%2Bm0ibfKKZsyjm%2FKjAmddTFwJO75xA3sz%2BEos%2BdxWpn7hSp4suQq7hfVEVvnbVoKi8NfNlvLLjyyvDoZRf8kM%2BQzbzAqRT%2FB54c7OBJZ8rmaE%2BD45Tj4rN7GxA%2BoJdKkcZzcSVefaaEowTX3i3D7ngnlmAkEWHELemgyMOTm%2BAdN5CAFmCKArhTLK%2FGIyVahn%2F2CFyRPLL13GeWp9v8aJWiF2Gtxv6EXggL5CIlVxrc9c05%2Bl7taNxWlTzVDcCBYcyiixiN3Z3ub5ZIuSKMp0T7N04RmUAm2yycfO3Qi%2BiidSpSdgDt%2BOGqNXBXja9h7yhi6cr12BB3mmmKoVMnV%2FBeZMIPt8bwGOqUBRgisCTOWioNYZSZjnrsCne6PeZKU3zEQMOYuuzRwNbhjnAG641jXvUBmdHf54MW29on4JTKp7m0yJ1REgJhPrHQHFPUQ70jcVr2EkjerZ4m9lUv7%2BtrzBmXv%2FQMGQCsLdjZTr4jdoelZPAR4MEW3Fzq%2F1%2BU3Cl59TpYThzDYVkEo1VJR5Fk3JNJNTmk0SbQQesvzzx8URrC981QJTAMundMSeGhp&X-Amz-Signature=8d02594c6ec30b390321f048394dab546024f7756af6759b415681d953ec0e2b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYZ2M3LK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHRYlc6JCIOseTT3IigJFRx%2BrB4S560PavS9Rh0hTwCHAiEAy3Ka9D4enIWfrMJrizQYUIfoebrGpJ4gF1pE503JtE4qiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEESK4kxXbVmNR90MCrcA8suKW4k0UZKpBL8SAwRSTknTwrPhG2c99w7s6oMm8G3DkxuNxTBan%2BATy%2FJQmwgdZ8enasVpNDG3mpcQthxyLGv6AWWtfvQ1PwfEwF0QGtt5XWYeFBm5Hay4w35BKFq6yp%2F8VfDfZSSIW86447amkG479pl%2B0VsVkod2Em4dELyEFEVc3S5OD%2B93emO%2BnMgiWHsXp%2FwyaK%2BKZIDLBplBlMANn12WyQpx2%2F%2F%2BpCNi2xtmUGJojVm5dfrk1fJjywWN5XJA2%2Bj1TwsA8NxXf5EY01TRkx3lwvaPZG16%2Bm0ibfKKZsyjm%2FKjAmddTFwJO75xA3sz%2BEos%2BdxWpn7hSp4suQq7hfVEVvnbVoKi8NfNlvLLjyyvDoZRf8kM%2BQzbzAqRT%2FB54c7OBJZ8rmaE%2BD45Tj4rN7GxA%2BoJdKkcZzcSVefaaEowTX3i3D7ngnlmAkEWHELemgyMOTm%2BAdN5CAFmCKArhTLK%2FGIyVahn%2F2CFyRPLL13GeWp9v8aJWiF2Gtxv6EXggL5CIlVxrc9c05%2Bl7taNxWlTzVDcCBYcyiixiN3Z3ub5ZIuSKMp0T7N04RmUAm2yycfO3Qi%2BiidSpSdgDt%2BOGqNXBXja9h7yhi6cr12BB3mmmKoVMnV%2FBeZMIPt8bwGOqUBRgisCTOWioNYZSZjnrsCne6PeZKU3zEQMOYuuzRwNbhjnAG641jXvUBmdHf54MW29on4JTKp7m0yJ1REgJhPrHQHFPUQ70jcVr2EkjerZ4m9lUv7%2BtrzBmXv%2FQMGQCsLdjZTr4jdoelZPAR4MEW3Fzq%2F1%2BU3Cl59TpYThzDYVkEo1VJR5Fk3JNJNTmk0SbQQesvzzx8URrC981QJTAMundMSeGhp&X-Amz-Signature=9485a0e132f24948dde7340ca77fb61d75c1b086c10bd4b4901acca28f833e34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYZ2M3LK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHRYlc6JCIOseTT3IigJFRx%2BrB4S560PavS9Rh0hTwCHAiEAy3Ka9D4enIWfrMJrizQYUIfoebrGpJ4gF1pE503JtE4qiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEESK4kxXbVmNR90MCrcA8suKW4k0UZKpBL8SAwRSTknTwrPhG2c99w7s6oMm8G3DkxuNxTBan%2BATy%2FJQmwgdZ8enasVpNDG3mpcQthxyLGv6AWWtfvQ1PwfEwF0QGtt5XWYeFBm5Hay4w35BKFq6yp%2F8VfDfZSSIW86447amkG479pl%2B0VsVkod2Em4dELyEFEVc3S5OD%2B93emO%2BnMgiWHsXp%2FwyaK%2BKZIDLBplBlMANn12WyQpx2%2F%2F%2BpCNi2xtmUGJojVm5dfrk1fJjywWN5XJA2%2Bj1TwsA8NxXf5EY01TRkx3lwvaPZG16%2Bm0ibfKKZsyjm%2FKjAmddTFwJO75xA3sz%2BEos%2BdxWpn7hSp4suQq7hfVEVvnbVoKi8NfNlvLLjyyvDoZRf8kM%2BQzbzAqRT%2FB54c7OBJZ8rmaE%2BD45Tj4rN7GxA%2BoJdKkcZzcSVefaaEowTX3i3D7ngnlmAkEWHELemgyMOTm%2BAdN5CAFmCKArhTLK%2FGIyVahn%2F2CFyRPLL13GeWp9v8aJWiF2Gtxv6EXggL5CIlVxrc9c05%2Bl7taNxWlTzVDcCBYcyiixiN3Z3ub5ZIuSKMp0T7N04RmUAm2yycfO3Qi%2BiidSpSdgDt%2BOGqNXBXja9h7yhi6cr12BB3mmmKoVMnV%2FBeZMIPt8bwGOqUBRgisCTOWioNYZSZjnrsCne6PeZKU3zEQMOYuuzRwNbhjnAG641jXvUBmdHf54MW29on4JTKp7m0yJ1REgJhPrHQHFPUQ70jcVr2EkjerZ4m9lUv7%2BtrzBmXv%2FQMGQCsLdjZTr4jdoelZPAR4MEW3Fzq%2F1%2BU3Cl59TpYThzDYVkEo1VJR5Fk3JNJNTmk0SbQQesvzzx8URrC981QJTAMundMSeGhp&X-Amz-Signature=5fa8b4d46f22b2e3fbf06302cbd9e16f09020f4624981bd9d06a6ad2c15b9379&X-Amz-SignedHeaders=host&x-id=GetObject)
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


