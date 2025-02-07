

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZCM3WR7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQD8ycYEylOIxZgVtH1P%2FYMupC4vj9fLAYo1XBueH9AUEAIgI5eWj%2BRHsm9279QZEJJ8CMYiTtYMSRNZgYmvaEpHmEIq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDGbdfWBgBSgoEgsZQyrcA0pE8elZuUT6J7U%2F3pJMV9QDXw7jVjUSzbAK514vP6g%2Ft9kvFJ3Di%2B2ty98K9zXfWanp7Oj80%2Bp9SivqasjAkXrA%2BgcdqU6mH5pa%2FiKv0ImugOu9FvwbfXxFVAMaxTTvZHFV63d%2Fx852VTu%2F%2FoadfmWFLbFLBAEBUov1POnZucWSrvndOjddbo65VBiOqkZw5Whzk8C8QWMLiG6H8H1aMTqptte%2BS4epaLDtymDYX7s4m7Y5IDg2sUzbDMAT0eGhCYRhbKIfMt53sVMROnO9PlHqRyv5ll2PWdAIKrYLd23ORsi80po1QhD%2Fjt71K%2Bt8PtbQaU%2FUfB8KN%2Fq6MGizmGa%2BaDpStfnMQJ8aSC3tKAzfm3xreF7MlZ0qchGQaMkK%2FxkhriKzhFs8ivqUNknL7OWVJMvViyInJKHE9U%2Bl26QE8RVjJNbdBpSalFNd61ZImqWW3IcF42aPX%2BcqWqbBcVSgix%2FAnCR91TMsO4PZDrvHDKHyIvHqLBr7vCzxWfPJR7vWl%2F4YcOv8RJvzZGdgYcRFp6Zh5vb0yGXAOohn9WdbGkhihO98sp1zzssIqq0F5NiAhaRKAlCC5a4jHKix9YOoUhs5gwVUYm%2B%2Bl7tFvWfcbFENloKOzmD1AHhbMOjSmb0GOqUBCVJBs71%2FBe%2Bh1440hThEk%2FNkCAvtOTZnrGnUXfs27hXjmima8gu0RgSxXLuU0XBBpeb6Chpu0JK3inPFR1mRzACB0WELCiWUjnBB1SZDyIKBJW6L5V35BK4hwBxu0mdhcVJnR0%2FQYiEYnHsrNiTpTmSdSNHgSx6Rvoucac7dphz%2B9Ow%2FqB9SccXrr%2Bw8QUJsKd2WpPJ1Q4iHPvAJYj%2BlupgVKdca&X-Amz-Signature=f312200009a94d8e8aa8ff57057be3373b6178855c24da70c0ccbd75de820350&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYS2JHNA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDUnJGaXz8ORtL0kz5HKO6EimxKr7xqTdsvO5lOljhYuwIhAJ6bRXavkKwnhNQ1%2B20YmclnDfhKBIQGJdD79o9OWkm7Kv8DCH0QABoMNjM3NDIzMTgzODA1IgwMU4dm8bnjE%2F5GV8Mq3ANQImd8%2BU8qYM1EnGhVRcHKY%2Bd3vPESPpSBrynzrGlceyi5Ii%2B7ZFzbsCT1SiWU6cYJSPJyS5VHoUQjHp%2FrUaS0HycZ93GBMOYrlGU9hh4k9HcUMKnnlKlsG3ABKvPkUI689PaFt1J6s%2F7kkNAC32qI2cQqPn%2B5qGp0s6xb54qEF37YQ46tCgTPovLLeGT5SqncErm%2FrwGh5CVBA2pfCY5jFcwp3XIGOCwI2WBTCcyH4Rewf9xFdJ7eFlIxD7cpovWOlaFpluBFpwd1JRTfG1kKkoE9mvupSwMwG0g1j6veOTbujGlNRkEhq6bBbX2xRwaGKcFZyE4Fd2gtBszLWK%2FIybzUMxcScCADS1orUsDONu%2Fg2YJCLFxmPfSykdEj5JJVcQMyKV9l%2F2dz5qonu0esFyqE9dzPPpqcenxAo6oTm2t7cGv0yVjakAxMHHFLSIxzmXoX08AeuJEqQU1vD7gkOW0oq7P7JajgcE2AobWhZhY%2BRqYGlNE8DJFlDHfyxUdlmGarlK5ubdcrgOk5sLhKPXH5iLq01SvNTMTWkG0yg0QTBVCHVoV1HREzGHnK%2Bfn7xhe21s4lEjJbVPBCbbRVpSPtFQjWBxtlSOPl0bbU6ukDZ3kHvEa8dUeNODD60pm9BjqkAVn%2FUHHmBnqFBr5hntCgr7r9iEbElZm5Kz%2B%2Fnp9K%2Bsloygpn4kSxEAvhnY3QKUe4PnzSoJNGJf8sIZfU6RGPj8tFeEvN5U%2FB3OQogHfhHi8IgJpnKMR%2BHJqVzoVa9B1TP%2FyQY76FgHaK5sdyhf57PO9zQV%2BvPCxX36qJ3Qcm5UDH%2BF%2Bt%2Ft9Nzb%2BSvTq8jb9p%2FXeINVim2bc9Xa15izebUeMV7%2B41&X-Amz-Signature=921f2e342692bd75e2f846991955446e22109d8cc6a5070a5456d95a06df04c2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYS2JHNA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDUnJGaXz8ORtL0kz5HKO6EimxKr7xqTdsvO5lOljhYuwIhAJ6bRXavkKwnhNQ1%2B20YmclnDfhKBIQGJdD79o9OWkm7Kv8DCH0QABoMNjM3NDIzMTgzODA1IgwMU4dm8bnjE%2F5GV8Mq3ANQImd8%2BU8qYM1EnGhVRcHKY%2Bd3vPESPpSBrynzrGlceyi5Ii%2B7ZFzbsCT1SiWU6cYJSPJyS5VHoUQjHp%2FrUaS0HycZ93GBMOYrlGU9hh4k9HcUMKnnlKlsG3ABKvPkUI689PaFt1J6s%2F7kkNAC32qI2cQqPn%2B5qGp0s6xb54qEF37YQ46tCgTPovLLeGT5SqncErm%2FrwGh5CVBA2pfCY5jFcwp3XIGOCwI2WBTCcyH4Rewf9xFdJ7eFlIxD7cpovWOlaFpluBFpwd1JRTfG1kKkoE9mvupSwMwG0g1j6veOTbujGlNRkEhq6bBbX2xRwaGKcFZyE4Fd2gtBszLWK%2FIybzUMxcScCADS1orUsDONu%2Fg2YJCLFxmPfSykdEj5JJVcQMyKV9l%2F2dz5qonu0esFyqE9dzPPpqcenxAo6oTm2t7cGv0yVjakAxMHHFLSIxzmXoX08AeuJEqQU1vD7gkOW0oq7P7JajgcE2AobWhZhY%2BRqYGlNE8DJFlDHfyxUdlmGarlK5ubdcrgOk5sLhKPXH5iLq01SvNTMTWkG0yg0QTBVCHVoV1HREzGHnK%2Bfn7xhe21s4lEjJbVPBCbbRVpSPtFQjWBxtlSOPl0bbU6ukDZ3kHvEa8dUeNODD60pm9BjqkAVn%2FUHHmBnqFBr5hntCgr7r9iEbElZm5Kz%2B%2Fnp9K%2Bsloygpn4kSxEAvhnY3QKUe4PnzSoJNGJf8sIZfU6RGPj8tFeEvN5U%2FB3OQogHfhHi8IgJpnKMR%2BHJqVzoVa9B1TP%2FyQY76FgHaK5sdyhf57PO9zQV%2BvPCxX36qJ3Qcm5UDH%2BF%2Bt%2Ft9Nzb%2BSvTq8jb9p%2FXeINVim2bc9Xa15izebUeMV7%2B41&X-Amz-Signature=e82349da31215550706802f61cc28c63f1690ebb9125a94e59bf39d6cd1bbf32&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYS2JHNA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDUnJGaXz8ORtL0kz5HKO6EimxKr7xqTdsvO5lOljhYuwIhAJ6bRXavkKwnhNQ1%2B20YmclnDfhKBIQGJdD79o9OWkm7Kv8DCH0QABoMNjM3NDIzMTgzODA1IgwMU4dm8bnjE%2F5GV8Mq3ANQImd8%2BU8qYM1EnGhVRcHKY%2Bd3vPESPpSBrynzrGlceyi5Ii%2B7ZFzbsCT1SiWU6cYJSPJyS5VHoUQjHp%2FrUaS0HycZ93GBMOYrlGU9hh4k9HcUMKnnlKlsG3ABKvPkUI689PaFt1J6s%2F7kkNAC32qI2cQqPn%2B5qGp0s6xb54qEF37YQ46tCgTPovLLeGT5SqncErm%2FrwGh5CVBA2pfCY5jFcwp3XIGOCwI2WBTCcyH4Rewf9xFdJ7eFlIxD7cpovWOlaFpluBFpwd1JRTfG1kKkoE9mvupSwMwG0g1j6veOTbujGlNRkEhq6bBbX2xRwaGKcFZyE4Fd2gtBszLWK%2FIybzUMxcScCADS1orUsDONu%2Fg2YJCLFxmPfSykdEj5JJVcQMyKV9l%2F2dz5qonu0esFyqE9dzPPpqcenxAo6oTm2t7cGv0yVjakAxMHHFLSIxzmXoX08AeuJEqQU1vD7gkOW0oq7P7JajgcE2AobWhZhY%2BRqYGlNE8DJFlDHfyxUdlmGarlK5ubdcrgOk5sLhKPXH5iLq01SvNTMTWkG0yg0QTBVCHVoV1HREzGHnK%2Bfn7xhe21s4lEjJbVPBCbbRVpSPtFQjWBxtlSOPl0bbU6ukDZ3kHvEa8dUeNODD60pm9BjqkAVn%2FUHHmBnqFBr5hntCgr7r9iEbElZm5Kz%2B%2Fnp9K%2Bsloygpn4kSxEAvhnY3QKUe4PnzSoJNGJf8sIZfU6RGPj8tFeEvN5U%2FB3OQogHfhHi8IgJpnKMR%2BHJqVzoVa9B1TP%2FyQY76FgHaK5sdyhf57PO9zQV%2BvPCxX36qJ3Qcm5UDH%2BF%2Bt%2Ft9Nzb%2BSvTq8jb9p%2FXeINVim2bc9Xa15izebUeMV7%2B41&X-Amz-Signature=7703797aba8a90831ee70ce0ae4faa87cc9e6c5dd4058dd5c07d1e3677026a51&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYS2JHNA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDUnJGaXz8ORtL0kz5HKO6EimxKr7xqTdsvO5lOljhYuwIhAJ6bRXavkKwnhNQ1%2B20YmclnDfhKBIQGJdD79o9OWkm7Kv8DCH0QABoMNjM3NDIzMTgzODA1IgwMU4dm8bnjE%2F5GV8Mq3ANQImd8%2BU8qYM1EnGhVRcHKY%2Bd3vPESPpSBrynzrGlceyi5Ii%2B7ZFzbsCT1SiWU6cYJSPJyS5VHoUQjHp%2FrUaS0HycZ93GBMOYrlGU9hh4k9HcUMKnnlKlsG3ABKvPkUI689PaFt1J6s%2F7kkNAC32qI2cQqPn%2B5qGp0s6xb54qEF37YQ46tCgTPovLLeGT5SqncErm%2FrwGh5CVBA2pfCY5jFcwp3XIGOCwI2WBTCcyH4Rewf9xFdJ7eFlIxD7cpovWOlaFpluBFpwd1JRTfG1kKkoE9mvupSwMwG0g1j6veOTbujGlNRkEhq6bBbX2xRwaGKcFZyE4Fd2gtBszLWK%2FIybzUMxcScCADS1orUsDONu%2Fg2YJCLFxmPfSykdEj5JJVcQMyKV9l%2F2dz5qonu0esFyqE9dzPPpqcenxAo6oTm2t7cGv0yVjakAxMHHFLSIxzmXoX08AeuJEqQU1vD7gkOW0oq7P7JajgcE2AobWhZhY%2BRqYGlNE8DJFlDHfyxUdlmGarlK5ubdcrgOk5sLhKPXH5iLq01SvNTMTWkG0yg0QTBVCHVoV1HREzGHnK%2Bfn7xhe21s4lEjJbVPBCbbRVpSPtFQjWBxtlSOPl0bbU6ukDZ3kHvEa8dUeNODD60pm9BjqkAVn%2FUHHmBnqFBr5hntCgr7r9iEbElZm5Kz%2B%2Fnp9K%2Bsloygpn4kSxEAvhnY3QKUe4PnzSoJNGJf8sIZfU6RGPj8tFeEvN5U%2FB3OQogHfhHi8IgJpnKMR%2BHJqVzoVa9B1TP%2FyQY76FgHaK5sdyhf57PO9zQV%2BvPCxX36qJ3Qcm5UDH%2BF%2Bt%2Ft9Nzb%2BSvTq8jb9p%2FXeINVim2bc9Xa15izebUeMV7%2B41&X-Amz-Signature=c1259c87cdf9d72bf52f3409bb7ca7d343320cf9334938e0e5724e4693c5c812&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYS2JHNA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDUnJGaXz8ORtL0kz5HKO6EimxKr7xqTdsvO5lOljhYuwIhAJ6bRXavkKwnhNQ1%2B20YmclnDfhKBIQGJdD79o9OWkm7Kv8DCH0QABoMNjM3NDIzMTgzODA1IgwMU4dm8bnjE%2F5GV8Mq3ANQImd8%2BU8qYM1EnGhVRcHKY%2Bd3vPESPpSBrynzrGlceyi5Ii%2B7ZFzbsCT1SiWU6cYJSPJyS5VHoUQjHp%2FrUaS0HycZ93GBMOYrlGU9hh4k9HcUMKnnlKlsG3ABKvPkUI689PaFt1J6s%2F7kkNAC32qI2cQqPn%2B5qGp0s6xb54qEF37YQ46tCgTPovLLeGT5SqncErm%2FrwGh5CVBA2pfCY5jFcwp3XIGOCwI2WBTCcyH4Rewf9xFdJ7eFlIxD7cpovWOlaFpluBFpwd1JRTfG1kKkoE9mvupSwMwG0g1j6veOTbujGlNRkEhq6bBbX2xRwaGKcFZyE4Fd2gtBszLWK%2FIybzUMxcScCADS1orUsDONu%2Fg2YJCLFxmPfSykdEj5JJVcQMyKV9l%2F2dz5qonu0esFyqE9dzPPpqcenxAo6oTm2t7cGv0yVjakAxMHHFLSIxzmXoX08AeuJEqQU1vD7gkOW0oq7P7JajgcE2AobWhZhY%2BRqYGlNE8DJFlDHfyxUdlmGarlK5ubdcrgOk5sLhKPXH5iLq01SvNTMTWkG0yg0QTBVCHVoV1HREzGHnK%2Bfn7xhe21s4lEjJbVPBCbbRVpSPtFQjWBxtlSOPl0bbU6ukDZ3kHvEa8dUeNODD60pm9BjqkAVn%2FUHHmBnqFBr5hntCgr7r9iEbElZm5Kz%2B%2Fnp9K%2Bsloygpn4kSxEAvhnY3QKUe4PnzSoJNGJf8sIZfU6RGPj8tFeEvN5U%2FB3OQogHfhHi8IgJpnKMR%2BHJqVzoVa9B1TP%2FyQY76FgHaK5sdyhf57PO9zQV%2BvPCxX36qJ3Qcm5UDH%2BF%2Bt%2Ft9Nzb%2BSvTq8jb9p%2FXeINVim2bc9Xa15izebUeMV7%2B41&X-Amz-Signature=1f2e5ee3129af97ec75dca4b324e3595363acbd037c9cefb599bac5037d4dc34&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZCM3WR7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQD8ycYEylOIxZgVtH1P%2FYMupC4vj9fLAYo1XBueH9AUEAIgI5eWj%2BRHsm9279QZEJJ8CMYiTtYMSRNZgYmvaEpHmEIq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDGbdfWBgBSgoEgsZQyrcA0pE8elZuUT6J7U%2F3pJMV9QDXw7jVjUSzbAK514vP6g%2Ft9kvFJ3Di%2B2ty98K9zXfWanp7Oj80%2Bp9SivqasjAkXrA%2BgcdqU6mH5pa%2FiKv0ImugOu9FvwbfXxFVAMaxTTvZHFV63d%2Fx852VTu%2F%2FoadfmWFLbFLBAEBUov1POnZucWSrvndOjddbo65VBiOqkZw5Whzk8C8QWMLiG6H8H1aMTqptte%2BS4epaLDtymDYX7s4m7Y5IDg2sUzbDMAT0eGhCYRhbKIfMt53sVMROnO9PlHqRyv5ll2PWdAIKrYLd23ORsi80po1QhD%2Fjt71K%2Bt8PtbQaU%2FUfB8KN%2Fq6MGizmGa%2BaDpStfnMQJ8aSC3tKAzfm3xreF7MlZ0qchGQaMkK%2FxkhriKzhFs8ivqUNknL7OWVJMvViyInJKHE9U%2Bl26QE8RVjJNbdBpSalFNd61ZImqWW3IcF42aPX%2BcqWqbBcVSgix%2FAnCR91TMsO4PZDrvHDKHyIvHqLBr7vCzxWfPJR7vWl%2F4YcOv8RJvzZGdgYcRFp6Zh5vb0yGXAOohn9WdbGkhihO98sp1zzssIqq0F5NiAhaRKAlCC5a4jHKix9YOoUhs5gwVUYm%2B%2Bl7tFvWfcbFENloKOzmD1AHhbMOjSmb0GOqUBCVJBs71%2FBe%2Bh1440hThEk%2FNkCAvtOTZnrGnUXfs27hXjmima8gu0RgSxXLuU0XBBpeb6Chpu0JK3inPFR1mRzACB0WELCiWUjnBB1SZDyIKBJW6L5V35BK4hwBxu0mdhcVJnR0%2FQYiEYnHsrNiTpTmSdSNHgSx6Rvoucac7dphz%2B9Ow%2FqB9SccXrr%2Bw8QUJsKd2WpPJ1Q4iHPvAJYj%2BlupgVKdca&X-Amz-Signature=ac8f52f9283f96c2a0c4a08294ee6454401a34dbe6a8bb16fa246855cb42cfdb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZCM3WR7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQD8ycYEylOIxZgVtH1P%2FYMupC4vj9fLAYo1XBueH9AUEAIgI5eWj%2BRHsm9279QZEJJ8CMYiTtYMSRNZgYmvaEpHmEIq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDGbdfWBgBSgoEgsZQyrcA0pE8elZuUT6J7U%2F3pJMV9QDXw7jVjUSzbAK514vP6g%2Ft9kvFJ3Di%2B2ty98K9zXfWanp7Oj80%2Bp9SivqasjAkXrA%2BgcdqU6mH5pa%2FiKv0ImugOu9FvwbfXxFVAMaxTTvZHFV63d%2Fx852VTu%2F%2FoadfmWFLbFLBAEBUov1POnZucWSrvndOjddbo65VBiOqkZw5Whzk8C8QWMLiG6H8H1aMTqptte%2BS4epaLDtymDYX7s4m7Y5IDg2sUzbDMAT0eGhCYRhbKIfMt53sVMROnO9PlHqRyv5ll2PWdAIKrYLd23ORsi80po1QhD%2Fjt71K%2Bt8PtbQaU%2FUfB8KN%2Fq6MGizmGa%2BaDpStfnMQJ8aSC3tKAzfm3xreF7MlZ0qchGQaMkK%2FxkhriKzhFs8ivqUNknL7OWVJMvViyInJKHE9U%2Bl26QE8RVjJNbdBpSalFNd61ZImqWW3IcF42aPX%2BcqWqbBcVSgix%2FAnCR91TMsO4PZDrvHDKHyIvHqLBr7vCzxWfPJR7vWl%2F4YcOv8RJvzZGdgYcRFp6Zh5vb0yGXAOohn9WdbGkhihO98sp1zzssIqq0F5NiAhaRKAlCC5a4jHKix9YOoUhs5gwVUYm%2B%2Bl7tFvWfcbFENloKOzmD1AHhbMOjSmb0GOqUBCVJBs71%2FBe%2Bh1440hThEk%2FNkCAvtOTZnrGnUXfs27hXjmima8gu0RgSxXLuU0XBBpeb6Chpu0JK3inPFR1mRzACB0WELCiWUjnBB1SZDyIKBJW6L5V35BK4hwBxu0mdhcVJnR0%2FQYiEYnHsrNiTpTmSdSNHgSx6Rvoucac7dphz%2B9Ow%2FqB9SccXrr%2Bw8QUJsKd2WpPJ1Q4iHPvAJYj%2BlupgVKdca&X-Amz-Signature=4ae397c54e1e2d3ba8b70c110bcf043af6f20d29a101e5e35db46d86eb39a31f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZCM3WR7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQD8ycYEylOIxZgVtH1P%2FYMupC4vj9fLAYo1XBueH9AUEAIgI5eWj%2BRHsm9279QZEJJ8CMYiTtYMSRNZgYmvaEpHmEIq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDGbdfWBgBSgoEgsZQyrcA0pE8elZuUT6J7U%2F3pJMV9QDXw7jVjUSzbAK514vP6g%2Ft9kvFJ3Di%2B2ty98K9zXfWanp7Oj80%2Bp9SivqasjAkXrA%2BgcdqU6mH5pa%2FiKv0ImugOu9FvwbfXxFVAMaxTTvZHFV63d%2Fx852VTu%2F%2FoadfmWFLbFLBAEBUov1POnZucWSrvndOjddbo65VBiOqkZw5Whzk8C8QWMLiG6H8H1aMTqptte%2BS4epaLDtymDYX7s4m7Y5IDg2sUzbDMAT0eGhCYRhbKIfMt53sVMROnO9PlHqRyv5ll2PWdAIKrYLd23ORsi80po1QhD%2Fjt71K%2Bt8PtbQaU%2FUfB8KN%2Fq6MGizmGa%2BaDpStfnMQJ8aSC3tKAzfm3xreF7MlZ0qchGQaMkK%2FxkhriKzhFs8ivqUNknL7OWVJMvViyInJKHE9U%2Bl26QE8RVjJNbdBpSalFNd61ZImqWW3IcF42aPX%2BcqWqbBcVSgix%2FAnCR91TMsO4PZDrvHDKHyIvHqLBr7vCzxWfPJR7vWl%2F4YcOv8RJvzZGdgYcRFp6Zh5vb0yGXAOohn9WdbGkhihO98sp1zzssIqq0F5NiAhaRKAlCC5a4jHKix9YOoUhs5gwVUYm%2B%2Bl7tFvWfcbFENloKOzmD1AHhbMOjSmb0GOqUBCVJBs71%2FBe%2Bh1440hThEk%2FNkCAvtOTZnrGnUXfs27hXjmima8gu0RgSxXLuU0XBBpeb6Chpu0JK3inPFR1mRzACB0WELCiWUjnBB1SZDyIKBJW6L5V35BK4hwBxu0mdhcVJnR0%2FQYiEYnHsrNiTpTmSdSNHgSx6Rvoucac7dphz%2B9Ow%2FqB9SccXrr%2Bw8QUJsKd2WpPJ1Q4iHPvAJYj%2BlupgVKdca&X-Amz-Signature=9ebd7b6e2b83bb47aa538abab1eb138841867f637c700196c54ae6a70dfd1387&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZCM3WR7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQD8ycYEylOIxZgVtH1P%2FYMupC4vj9fLAYo1XBueH9AUEAIgI5eWj%2BRHsm9279QZEJJ8CMYiTtYMSRNZgYmvaEpHmEIq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDGbdfWBgBSgoEgsZQyrcA0pE8elZuUT6J7U%2F3pJMV9QDXw7jVjUSzbAK514vP6g%2Ft9kvFJ3Di%2B2ty98K9zXfWanp7Oj80%2Bp9SivqasjAkXrA%2BgcdqU6mH5pa%2FiKv0ImugOu9FvwbfXxFVAMaxTTvZHFV63d%2Fx852VTu%2F%2FoadfmWFLbFLBAEBUov1POnZucWSrvndOjddbo65VBiOqkZw5Whzk8C8QWMLiG6H8H1aMTqptte%2BS4epaLDtymDYX7s4m7Y5IDg2sUzbDMAT0eGhCYRhbKIfMt53sVMROnO9PlHqRyv5ll2PWdAIKrYLd23ORsi80po1QhD%2Fjt71K%2Bt8PtbQaU%2FUfB8KN%2Fq6MGizmGa%2BaDpStfnMQJ8aSC3tKAzfm3xreF7MlZ0qchGQaMkK%2FxkhriKzhFs8ivqUNknL7OWVJMvViyInJKHE9U%2Bl26QE8RVjJNbdBpSalFNd61ZImqWW3IcF42aPX%2BcqWqbBcVSgix%2FAnCR91TMsO4PZDrvHDKHyIvHqLBr7vCzxWfPJR7vWl%2F4YcOv8RJvzZGdgYcRFp6Zh5vb0yGXAOohn9WdbGkhihO98sp1zzssIqq0F5NiAhaRKAlCC5a4jHKix9YOoUhs5gwVUYm%2B%2Bl7tFvWfcbFENloKOzmD1AHhbMOjSmb0GOqUBCVJBs71%2FBe%2Bh1440hThEk%2FNkCAvtOTZnrGnUXfs27hXjmima8gu0RgSxXLuU0XBBpeb6Chpu0JK3inPFR1mRzACB0WELCiWUjnBB1SZDyIKBJW6L5V35BK4hwBxu0mdhcVJnR0%2FQYiEYnHsrNiTpTmSdSNHgSx6Rvoucac7dphz%2B9Ow%2FqB9SccXrr%2Bw8QUJsKd2WpPJ1Q4iHPvAJYj%2BlupgVKdca&X-Amz-Signature=817e68a101c27e1e5b7d3087d960eca0b2b9cc6b89e55c5bad51dde1455a1098&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZCM3WR7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQD8ycYEylOIxZgVtH1P%2FYMupC4vj9fLAYo1XBueH9AUEAIgI5eWj%2BRHsm9279QZEJJ8CMYiTtYMSRNZgYmvaEpHmEIq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDGbdfWBgBSgoEgsZQyrcA0pE8elZuUT6J7U%2F3pJMV9QDXw7jVjUSzbAK514vP6g%2Ft9kvFJ3Di%2B2ty98K9zXfWanp7Oj80%2Bp9SivqasjAkXrA%2BgcdqU6mH5pa%2FiKv0ImugOu9FvwbfXxFVAMaxTTvZHFV63d%2Fx852VTu%2F%2FoadfmWFLbFLBAEBUov1POnZucWSrvndOjddbo65VBiOqkZw5Whzk8C8QWMLiG6H8H1aMTqptte%2BS4epaLDtymDYX7s4m7Y5IDg2sUzbDMAT0eGhCYRhbKIfMt53sVMROnO9PlHqRyv5ll2PWdAIKrYLd23ORsi80po1QhD%2Fjt71K%2Bt8PtbQaU%2FUfB8KN%2Fq6MGizmGa%2BaDpStfnMQJ8aSC3tKAzfm3xreF7MlZ0qchGQaMkK%2FxkhriKzhFs8ivqUNknL7OWVJMvViyInJKHE9U%2Bl26QE8RVjJNbdBpSalFNd61ZImqWW3IcF42aPX%2BcqWqbBcVSgix%2FAnCR91TMsO4PZDrvHDKHyIvHqLBr7vCzxWfPJR7vWl%2F4YcOv8RJvzZGdgYcRFp6Zh5vb0yGXAOohn9WdbGkhihO98sp1zzssIqq0F5NiAhaRKAlCC5a4jHKix9YOoUhs5gwVUYm%2B%2Bl7tFvWfcbFENloKOzmD1AHhbMOjSmb0GOqUBCVJBs71%2FBe%2Bh1440hThEk%2FNkCAvtOTZnrGnUXfs27hXjmima8gu0RgSxXLuU0XBBpeb6Chpu0JK3inPFR1mRzACB0WELCiWUjnBB1SZDyIKBJW6L5V35BK4hwBxu0mdhcVJnR0%2FQYiEYnHsrNiTpTmSdSNHgSx6Rvoucac7dphz%2B9Ow%2FqB9SccXrr%2Bw8QUJsKd2WpPJ1Q4iHPvAJYj%2BlupgVKdca&X-Amz-Signature=d7226d77f6e4b6e9a7741b376214fbf44bdc66cae9a5f799505c0c2e877352a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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


