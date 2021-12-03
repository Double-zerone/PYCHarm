#正则表达式
"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re #正则表达式包

i=re.search(r"(\d+?)","python996icu").group(1)
print(i)

def main():
    QQacct=input("请输入QQ号:")
    qqAcctObject=re.compile(r'^[1-9]\d{4,11}$')#compile(pattern, flags=0)	编译正则表达式返回正则表达式对象

    if not re.match(qqAcctObject,QQacct):
        print("qq号不合规")
    else:
        print('666666')
main()
