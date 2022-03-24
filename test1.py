"""
 * Project name(项目名称)：Python_pass语句
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/24 
 * Time(创建时间)： 20:18
 * Version(版本): 1.0
 * Description(描述)： pass 是 Python 中的关键字，用来让解释器跳过此处，什么都不做。
 """

if __name__ == '__main__':
    age = int(input("请输入你的年龄："))
    if age < 12:
        print("婴幼儿")
    elif 12 <= age < 18:
        print("青少年")
    elif 18 <= age < 30:
        print("成年人")
    elif 30 <= age < 50:
        pass
    else:
        print("老年人")
