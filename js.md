

------

## JavaScript简介

### 为什么是JavaScript

#### 编程语言

- php
- java
- c++
- c#
- python
- go
- ruby
- golang
- swift
- 易
- JavaScript
- typescript

#### JavaScript 优点

- 相对于java或c语言，入门简单
- 能够结合HTML和css实现动态页面，java需要学习特定的javaweb技术才能实现。
- JavaScript 逻辑难度相比于java，要低一些。
- 新行业，机会大于java

#### JavaScript 简要发展历史

- 95年由布兰登花10天搞出来的第一版。目前已经暴露了一些底层设计不足，后续由typescript来接替
- 网景公司将JavaScript1.1提交给了ECMA，作为语言标准规范。后续的JavaScript由ECMA来负责，所以又称为ECMAScript。
- 重要版本
  - 99年发布的ECMAScript 3. 全球普及的第一个JavaScript版本。
  - 09年发布了ECMAScript 5.中国普及的第一个版本，包括现在部分项目仍在用。（教学版本）
  - 15年发布了ECMAScript 2015.后续是每年更新一个版本。每年的版本只是一些修改，没有大改，所以我们统称2015以后的版本为ES6。
- 兼容问题
  - ES5，全系兼容
  - ES6.谷歌或火狐2015后的版本。ie全系不支持es6.只有edge12及以上才支持。

#### 数据存储单位

```
大小关系：bit < byte < kb < GB < TB<.....
```

- 位(bit)：   1bit 可以保存一个 0 或者 1 （最小的存储单位）
- 字节(Byte)：1B = 8b
- 千字节(KB)：1KB = 1024B
- 兆字节(MB)：1MB = 1024KB
- 吉字节(GB):  1GB = 1024MB
- 太字节(TB):  1TB = 1024GB

#### JavaScript 组成 (理解)

- ECMA只是负责了JavaScript的核心语法，关于浏览器部分或后端部分是不负责的。即单纯是ECMAScript是不能在浏览器中使用。具体的浏览器部分是每个浏览器厂商自己负责。
- 一个完整的JavaScript是由三部分组成
  - ECMAScript：核心语法
  - DOM：负责网页内容的交互(指body标签部分)
  - BOM：负责浏览器窗口本身的交互。如刷新、前进后退、跳转页面，打开新标签页等。
- 其中DOM和BOM由浏览器厂商负责，所以不同的厂商会有兼容性问题。

#### 浏览器环境

##### 在HTML页面中使用JavaScript

- 第一种：

  - 通过`script`标签来书写JavaScript代码。书写后打开页面会立即执行`<script>`中的代码

  ```js
  <script>   JavaScript 代码</script>
  ```

  - 页面上可以有多个`<script>`,具体的执行顺序是按照从上往下依次执行。
  - 建议 `<script>js代码</script>`尽量放在`</body>`之前

  ```js
  <body>    页面主要内容    <script>       JavaScript 代码    </script></body>
  ```

- 第二种：引入js文件

  - 我们可以吧要执行的代码写在以`.js`为后缀的文件里面，通过`<script src>`来引入

  ```js
  <script src="js文件地址"></script>
  ```

  - 一个页面可以引入多个js文件，每个js文件都需要单独的`script`来引入。

  - 打开页面时浏览器会按照`<script src>`的书写位置来一次引入js文件并立即执行js文件中的代码

  - 例子：

    ```js
    index.js: console.log('来自 index.js');index.html:<script src="index.js"></script>
    ```

### 注释

#### 单行注释

- `//`:单行注释

  ```js
  // :这一行的内容都是注释这里的内容不是注释
  ```

#### 多行注释

`/* */`:多行注释

```js
/*这里的内容都是注释这里还是注释*/这里不是注释
```

#### 文档注释：特殊的多行注释

```js
/**一般是对页面中的代码进行进一步的说明解析。*/
```

### 输入与输出

#### 输出

##### 控制台输出

- `cosole.log()`

  ```js
  console.log("要输出的内容");例子：console.log('hello world');//输出Helloworldconsole.log("hello world");//输出Helloworld
  ```

  - 引号可以是单引号或双引号。必须是英文状态下的。

##### 弹窗输出

- `alert()`:弹窗进行输出

  ```js
  alert("要输出的内容");例子：弹窗显示hello worldalert("hello  world");
  ```

##### 页面上输出

- `document.write()`;

  ```js
  document.write("要输出的内容");例子：输出helloworlddocument.write("hello world");
  ```

  - 如果要输出的是HTML标签的代码本身。那么JavaScript会将其解析为一个真正的标签并显示在页面上。

  ```js
  //页面上显示为一个超链接        
  document.write("<a href='http://www.baidu.com'>百度一下</a>");
  ```

#### 输入

##### prompt :获取用户输入的文字

- 概念：可以获取用户通过键盘书写的文字

- 语法

  ```js
  prompt("提示性文字");
  例子： 页面上会显示已输入框，并提示请输入您的银行卡和密码prompt("请输入您的银行卡和密码")；
  ```

- 配合输出

  ```js
  //思考：输出用户输入的信息alert(prompt('请输入您的银行卡和密码'));
  ```

- 练习

  ```js
  1. 尝试用页面上和弹窗两种方式来输出通过prompt输入的内容
  2. 执行console.log("1"+2); 有什么效果
  3. 执行console.log(1+2); 有什么效果
  ```

### 数据类型

#### 生活中的数据

- 工资：3500
- 年龄：:23
- 姓名：邓乃文
- 出生日期: 1900-01-03
- 地址：成都高新区孵化园园区5号楼
- 商品数据：商品名称、商品价格、商品描述、库存

#### 数据分类

- JavaScript有7种数据类型，把数据归纳于两种类型：基本数据类型和引用数据类型

- 基本数据类型：

  - Number: 表示数字。比如 12 2.4 -4.5

    ```js
    数字:  12  -23  0.5  -90 -0.5字符串："34"  "-90"  "6.7"
    ```

- String：又名字符串，用来表示文本。比如”邓乃文”、”张三”

  - 程序中的文本都是用一对引号包围起来，单/双引号都可以。

    ```js
    字符串："张三"   "成都高新区孵化园园区5号楼"  ""  "123"
    ```

- Boolean:布尔型。表示逻辑上的正确或错误。

  - 该数据类型只有两个取值： `true`或`false`
  - `true`:表示逻辑上的正确：比如`1 < 2`
  - `false`:表示逻辑上的错误:比如：`1 == 2`

- Symbol:ES6新增的基本数据类型。表示数据的唯一性，通常用于对象的属性中。

- NULL：表示某个变量或对象为空。

- undefined：表示某变量未定义。

- 引用数据类型：除了基本数据以外的数据类型
  - Object：表示对象。对象数据类型是程序中最重要的数据类型。并在在JavaScript中，数组和函数本质上也是属于对象。

#### 数字型范围

JavaScript中数值的最大和最小值

- 最大值：Number.MAX_VALUE，这个值为： 1.7976931348623157e+308

- 最小值：Number.MIN_VALUE，这个值为：5e-32

#### 数字型三个特殊值

- Infinity ，代表无穷大，大于任何数值

- -Infinity ，代表无穷小，小于任何数值

- NaN ，Not a number，代表一个非数值

#### isNaN

用来判断一个变量是否为非数字的类型，返回 true 或者 false

   ![](E:\qiand\07-10 JavaScript网页编程\01-JavaScript基础语法资料\JavaScript基础第01天\4-笔记\images\图片17.png)

#### 数据类型的转换

##### 字符串转为数字

- `Number`:可以将一个字符串尝试转为数字，如果给的是非数字，那么会输出`NaN`

  ```js
  var 变量名 = Number(待转换的字符串);
  例子：var num1 = Number("123");
  var num2 = Number("-12.3");
  var num3 = Number("abc");
  document.write(num1); 123
  document.write(num2); -12.3
  document.write(num3); NaN
  ```

  - Number也可以将非字符串类型转为数字，比如`true`会转为1,`false`会转为0

- `parseInt`:将一个字符串尝试转为数字，不保留小数。非数字的字符串会输出`NaN`:

  ```js
  var 变量名 = parseInt(待转换的字符串);
  例子：var num1 = parseInt("123");
  var num2 = parseInt("-12.3");
  var num3 = parseInt("abc");
  document.write(num1); 123
  document.write(num2); -12
  document.write(num3); NaN
  ```

- `parseFloat`:将一个字符串转为带小数的数字。如果是非数字，也是会输出`NaN`.

  ```js
  var 变量名 = parseFloat(待转换的字符串);
  例子：
  var num1 = parseFloat("123");
  var num2 = parseFloat("-12.3");
  var num3 = parseFloat("abc");
  document.write(num1); 123
  document.write(num2); -12.3
  document.write(num3); NaN
  ```

##### 数字转字符串

- `toString`

  ```js
  var 变量名= 数字.toString();
  例子；
  var num = 11;
  var str = num.toString();
  str =>"11"
  ```

##### 数字保留指定位数的小数点

- `toFixed`:能够指定某个数字保留几位小数,会四舍五入。

  ```js
  var 变量名= 数字.toFixed(小数点的位数);
  例子：保留一位小数
  var num =1.674;
  var num1 = num.toFixed(1);
  document.write(num1);// 1.7
  ```

#### 字符串转义符

​		类似HTML里面的特殊字符，字符串中也有特殊字符，我们称之为转义符。

​		转义符都是 \ 开头的，常用的转义符及其说明如下：

| 转义符 | 解释说明                          |
| ------ | --------------------------------- |
| \n     | 换行符，n   是   newline   的意思 |
| \ \    | 斜杠   \                          |
| \'     | '   单引号                        |
| \"     | ”双引号                           |
| \t     | tab  缩进                         |
| \b     | 空格 ，b   是   blank  的意思     |





##### 练习

```js
a)用户输入两个数字，用变量进行保存并转为数字
i.获取他们相加之和并去掉小数点并输出
ii.获取他们相乘之积并进行四舍五入，不保留小数点
iii.分别获取数字的字符串形式并进行拼接并输出
```

### 变量

#### 变量的概念

- 概念：变量是程序中用于保存一个数据的容器。通过变量的方式，可以实现某个数据可以重复的进行使用。
- 作用
  - 能够重复的使用数据

#### 变量的使用

##### 定义变量

```js
var  变量名 = 要保存的数据;
```

- 变量定义一次，可以多次使用。
- 变量一旦定义，那么该变量就会指向所保存的数据。如果使用了变量，在程序实际运行时，程序会读取变量里保存的数据并进行操作。
- 变量都需要`先定义，再使用`

##### 使用变量

- 用变量名来代替所保存的数据

  ```js
  例子：用户输入一个数字并保存到变量里，完成该数和5的加法和减法结果
  var num1 =prompt("请输入数字");
  document.write(num1 + 5);
  document.write(num1 - 5);
  ```

##### 修改变量

- 无需重新定义变量。直接修改变量的数据即可

  ```js
  var demo = 1; console.log(demo);// 1
  //修改
  demo = 3;
  console.log(demo);// 3
  ```

#### 变量名的命名规范

##### 命名规范

- 变量名只能包含数字、字母、$、_
- 变量名不能以数字开头
- 变量名尽量见词达意。比如totalCount、music.切忌 a1 bb ccc

##### 练习

```
1. 用户输入3次，定义3个变量来分别接受输入的数字，之后获取3个数字相加和相减的结果
```

### 运算符

#### 基本概念

- 运算符：能够实现数学运算的一些特殊符号的统称。
- 分类
  - 算术运算符
  - 赋值运算符
  - 关系运算符
  - 逻辑运算符
  - 位运算符

#### 算术运算符

##### 5个算术运算符

- `+`:加
- `-`:减
- `*`:乘
- `/`:除
- `%`:余

##### + 和- 对于字符串的处理

- 如果+号两边有一个是字符串，那么最终进行的是字符串拼接在一起，形成一个大的字符串。比如

  ```
  1 +"2"  等同于  "12""abc" + "de" 等同于 "abcde"
  ```

- 如果`-`号两边有其中一个是字符串，那么JavaScript会尝试将字符串转为数字，并进行减法运算。如果无法转为数字，则直接输出结果`NaN`:not a number 表示非数字

  ```
  "1" -"2"  等同于 1 -2 == -1"1" -"abc" 等同于 NaN
  ```

#### 赋值运算符

- 能够快捷对变量进行数学运算并重新赋值。

#### 常见运算符

- =：将`=`右边表达式的结果赋给`=`左边 的变量

  ```js
   var num1 = 2;  //num1 自加 5  //修改变量的数据,等于以前的数据+5  
   num1 = num1 +5 ;// 等同于 2 +5
  ```

- +=:在变量的原来数据基础之上加上某个数据
- -=
- /=
- *=
- %=

```js
var num =  2; 
num = num +5;   =>  num +=5;
num = num -5;   =>  num -=5;
num = num /5;   =>  num /=5;
num = num *5;   =>  num *=5;
num = num %5;   =>  num %=5;
```

##### ++ —

- ++: 变量数据自增1

  - 基本语法

    ```js
    var num = 1;
    num++; //num保存的数据+1
    document.write(num);//2
    ```

- —：变量数据自减1

  - 基础语法

    ```js
    var num = 1;
    num--; //num保存的数据+1document.write(num);//0
    ```

- 当一个表达式中有多个++ 或—时，结果会有所不同

  ```js
  var num =1;
  var num2 = num + num++ - num--;
  document.write(num2);
  ```

  - ++ 或—出现在变量名后面的话是先读取变量旧的数据再进行++或—
  - ++ 或—出现在变量名前面的话是先执行再读取。即一直获取的是新的数据

  ```js
  var num =2 ;
  document.write(num - --num  + ++num);//3 //  2   - 1   + 2
  var num = 2;
  document.write(--num + --num + ++num);//2 6 //    1   + 0 +1
  ```

#### 关系运算符

- 概念：能够描述数据之间的关系，一般是指数字之间的 大小关系

- 分类

  - `==`:用于比较两个数据是否相等，会得到布尔型的数据作为输出。正确会得到`true`.错误会得到`false`.

    - `==`只会判断数值是否一样，不区分数字或字符串数据类型

      ```js
      1=="1"  =>true
      ```

  - `>`:大于符号。比较`>`符号左边的数据是否大于右边的数据。返回的是布尔型数据。

  - `<`:小于符号。比较`<`符号左边的数据是否小于右边的数据。返回的是布尔型数据。

  - `>=`:大于或等于符号。比较`>=`符号左边的数据是否大于或等于右边的数据。返回的是布尔型数据。

  - `<=`:小于或等于符号。比较`<=`符号左边的数据是否小于或等于右边的数据。返回的是布尔型数据

  - `!=`:不等于符号。比较`!=`符号左边的数据是否不等于右边的数据。返回的是布尔型数据

  - `===`:判断两个数据是否一样，同时也要求数据类型也一样。

    ```js
      var num1 = 3;  
      var num2 = 3;  //关系  
      var result1 =  num1 == num2;    
      var result2 =  num1 > num2;    
      var result3 =  num1 < num2;    
      var result4 =  num1 >= num2;    
      var result5 =  num1 <= num2;    
      var result6 =  num1 != num2;    
      document.write(result1 + "<br>");// true  
      document.write(result2 + "<br>");// false  
      document.write(result3 + "<br>");// false   
      document.write(result4 + "<br>");// true  
      document.write(result5 + "<br>");// true   
      document.write(result6 + "<br>");// false  //== 与===   
      var str1 = "1";  
      var str2 = 1;  
      document.write(str1 == str2);// true  
      document.write(str1 === str2);//false
    ```

#### 逻辑运算符

- 概念：能够完成多条件的判断。比如同时大于0并且小于10

- 分类

  - `&&`:and符号，表示需要同时满足`&&`左边和右边的条件，才为true，否则为false。

  - `||` :or符号，即或者。表示`||`符号左边和右边的条件满足其一则为true，除非两个都不满足，为false。

  - `!`:取反符号。 即本来的结果是true，加上`!`后为false

    \```js
    // !
    var num = 1;
    var result = num >10;
    document.write(!result);
    document.write(!(num > 10));
    // ||:需求：判断某个数字是否是大于10 的正数或小于0的负数
    var num = -9;
    document.write(num >10 || num < 0);

```js
  //&&：需求：判断某个数字是否是小于10的正数 （0~10）  
  // 分析：数字 <10 并且  数字>0  
  var num = 45;  
  document.write(num < 10 &&  num >0);  
  document.write(num > 0);```
```

#### 三目运算符

- 又称条件运算符、三元运算符，是一个针对简单`if-else`更快捷的语法，能够减少代码量

- 语法

  ```js
  要判断的表达式  ? 结果1 :  结果2; 
  例子：if-else ：
  if( score >=60){     
  document.write('及格');  
  }else{      
  document.write('不及格');  
  }
  三目： 
  score >=60  ?  document.write('及格') : document.write('不及格');
  ```

- 流程

  - 执行要判断的表达式，如果执行的结果为true，则执行? 后面的代码。如果为false，则执行`:`后的代码.

- 注意点

  - 针对简单的`if-else`结构，不适用于`if-else if-else`.因为三目运算符只支持2个分支。

#### 运算符优先级

![image-20210912185348865](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912185348865.png)





##### 练习

```js
练习：用户输入两个数，并转为数字i.分别得到大于0的比较结结果  
var num1 = Number(prompt('请输入一个数字')); 
var num2 = Number(prompt('请输入一个数字'));  
document.write(num1 > 0);  
document.write(num2 > 0);
ii.分别得到这两个数字是不是小于10的正整数.   
// 大于0   整数   
num1 =num1.toFixed(0);  
num2 =num2.toFixed(0);   
document.write(num1 > 0 && num1 <10);  
document.write(num2 > 0 && num2 <10);
```

### 模板字符串

#### 背景

- 如果需要再一段字符串中拼接一个变量的值，那么一般需要通过`+`来进行连接

  ```js
   var name = '张三';  
   var age = 12;  
   var sex = "男"; // 
   document.write("我的名字是,年龄为,性别为"); 
   document.write("我的名字是" + name + ",年龄为" + age +"性别为" + sex);
  ```

- 不便之处

  - 如果有多个变量，需要很多个+号，不方便书写

#### 模板字符串(ES6)

##### 概念

- ES6提供的一种直接能够在字符串中使用变量或简单表达式的语法，用于替代传统用`+`来拼接变量和字符串。

##### 语法

- 模板字符串用一对反单引号``来包围。
- 字符串中可以用`${变量或表达式}`来在字符串中使用变量

```js
var name = '张三';
var age = 12;
var sex = "男";
var str = `我的名字是${name},年龄为${age},我的性别是${sex}`;
document.write(str);
```

##### 模板字符串中的表达式

```js
 var num1 = 1; 
 var num2 = 2; 
 document.write(`${num1}+${num2}的结果为${num1 + num2}`);
```

### if

#### 控制结构基本概念

- 控制结构是指代码执行顺序不同于

  ```js
  从上往下
  ```

  直接执行的顺序。

  - 其中可能会有根据某个逻辑的判断来执行不同的代码(登录成功或失败)，或者代码需要重复的执行的不同的代码执行顺序。

- 分类

  - 分支
    - if
    - switch
  - 循环
    - for
    - while
    - do…while

#### 分支

- 分支结构是指代码执行顺序会受某个条件的影响，根据条件的不同结果来执行不同的代码
  - 例如登录。登录成功和不成功是执行的不同的 代码。
- 无论根据某个条件生成了多少个分支，最终代码只能执行其中一个分支。
- 具体的代码语法结构
  - if
  - switch

#### if -else

- 概念：根据某个表达式的正确与否，来执行不同的代码

- 语法

  ```js
  if(需要判断的条件){    
  条件为true时会执行的一段代码}
  else{    
  条件为false时会执行的一段代码
  }
  例子：根据用户输入的两个数，进行比较大小
  var num1 = Number(prompt('请输入第一个数'));
  var num2 =Number( prompt('请输入第二个数'));
  if(num1 > num2){  //true  
  document.write(`${num1} 大于了${num2}`);    
  }else{  //false  
  document.write(`${num2} 大于了${num1}`);
  }
  ```

- 流程

  1. 判断`if()`的条件是否为true
  2. 如果为true，那么执行if(){}里的代码，如果为false，会执行`else{}`里的代码
  3. if结构执行完毕,会执行if结构下面的剩余代码

#### if-elseif - else

- 概念：if-else 的升级版。因为if-else只能处理两个分支的情况，超过两个分支需要使用if-else if-else

- 语法

  ```js
  if(条件1){    
      当条件1为true时要执行的代码}else 
  if(条件2){    
      当条件1为false并且条件2为true时要执行的代码     
  }...else if(条件N)
  {    
      前面条件都不满足，条件N满足时要执行的代码  }
  else{    
      当所有条件都为false时要执行的代码}
  ```

- 流程

  1. 当条件1满足，那么执行if(条件1){}里的代码，执行后if结构结束。如果不满足，执行第二步
  2. 继续判断条件2，如果满足，则执行`else if（）{}`里的代码，执行后结束if结构。不满足则执行第三步
  3. 如果还有其他`else if`继续进行判断。中间有一个分支满足，则执行对应分支里的代码，执行后退出if结构。如果都不满足，则执行第四步
  4. 执行`else{}`里的代码,执行后if结构结束

### switch

#### 概念

- 当存在多个分支，并且每个分支是`固定值`时，用`switch`语法会比`if`结构代码会更加精简和整齐。

#### 语法

```js
switch(需要判断的数据){   
case 值1: 当数据为值1时要执行的代码;break;     
case 值2: 当数据为值2时要执行的代码;break;     
case 值3: 当数据为值3时要执行的代码;break;    
...    
case 值n: 当数据为值n时要执行的代码;break;         
以上case都没有匹配上的一个默认选项。类似于else。    
default:            
case都不匹配时要执行的代码; break;
}
```

#### if和switch的比较

- if和switch都是分支结构，用于判断等情况。
- if更适用于判断数值不明确，比如大于、小于等情况
- switch适用于固定数值的时候，比如等于多少之类的。比如星期几等。
- 不清楚时直接用if结构

### for

#### 循环结构

#### 三种结构

- for
- while
- do…while

#### for

##### 概念

- 用于重复执行代码的循环结构

##### 语法

```js
for(初始代码;循环继续的条件;循环次数自增或自减){    
需要循环执行的代码}例子：执行10次输出语句
for(var index = 10;index <=20;index++){    
document.write(`抄写了一遍笔记<br>`);
}
```

##### for流程

- 以输出10次抄写笔记为例
  1. 先执行一次初始代码：即定义了循环变量`index`并赋值为1
  2. 判断循环继续条件是否为true。如果为true，则执行第三步，
     `否则退出循环结构`，即不再循环。该例子要判断的条件为`index <=10`.
  3. 执行一次`{}`里的所有代码，例子中执行一次输出语句
  4. 执行一次循环变量自增或自减。该例子循环变量就是index，执行了`index++`。执行后回到第二步.

##### 解题流程

- 先分析题意中需要重复执行的部分。并得出循环变量的起始值和结束值。
- 再写for循环

##### 注意点

- for循环中只写需要重复执行的代码，不要在`{}`里面写输出语句之类的，应该是在循环结束后再看输出结果

##### 练习：

```js
1. 输出1到500
2. 计算从1加到10 的和
3. 计算从100加到500的和
4. 计算从1乘到10的积 √
5. 输出100内的所有偶数 √
6. 输出100内的所有能被5整除的数字
7. 输出100到999之间的所有水仙花数 √
8. 输出100到999之间的所有位相同的数字(即 111 222 333...999)
9. 用户输入一个数，判断是否是质数(质数：只能被1和本身整除) √
10.输出100内的所有质数
11.猜数字游戏：系统随机生成一个1000内的随机数，用户输入数字进行猜测，如果大了则提示大了，小了则提示小了。直到相等则游戏结束。结束后输出游戏的猜测次数
12.鸡兔一共15只，一共40只脚，用程序求得鸡兔数量
13.计算x的y次方。x和y由用户输入 √
14.组合问题: 用一元兑换1分、2分、5分的硬币，兑换数量为50枚，问可以有多少种组合的方式 √
15.抓球问题：有红球5个，黑球7个、白球9个。随机取出12个，求所有的取球方式并输出方式数量
16.根据用户输入的行数打印一个菱形
17.输入多次每次输入一个数字，使用循环求出最大值与最小值，输入0时结束
18.输出所有位数加起来等于6的三位数。比如123：1+2+3=6
19.有个人每天都会买苹果，第一天买1个，第二天买2个，第三天买4个。第二天买的数量是前一天的2倍。每个苹果6元，问购买总金额不超过100的最大苹果总数量
```

##### 计算从1加到10的和

```js
 /*需求：1+2+3+4+5+6+7+8+9+10重复的 
 做加法运算
 第一次：0+1第二次：(0+1)+2 第三次: (0+1+2) +3第四次: (0+1+2+3) +4...
 第十次：(0+1+2+3...+9)+10*/ v
 ar sum = 0;//保存以前加法的结果，即累加的和
for(var index = 1;index <=10;index++){//    sum=  sum + index;    sum+=index;}document.write(sum);
```

### break&continue

------

#### break

##### 概念

- 能够在循环中使用，用于提前结束整个循环代码，

##### 语法

```js
在循环体里进行使用。例子：
for(var i=0;i<10;i++){            
    if(i>4){                
        break;/*终止循环 */          
    }           
    document.write(i);}
```

#### continue

##### 概念

- 是循环中的 关键字，具有跳过当前次循环的 作用。

##### 作用

- `continue`能够跳过当前循环体里还未执行的代码，继续下一次循环

##### 语法

- 在循环`{}`里使用continue

```js
for(){    continue;}
```

##### break和continue的区别

- break用于提前结束整个循环过程，而continue只是跳过循环过程中的某一次循环。

### do…while

#### 概念

- 也是属于循环结构中的一种。

#### 语法

```
do{    要重复执行的代码}while(循环继续条件);
```

#### 流程

1. 先执行一次`{}`里的代码
2. 判断循环继续条件是否为true，为true则退回第一步，为false 退出`do..while`结构。

#### 特点

- 先执行再判断

#### 和for、while的比较

- do…while和for、while一样，都是属于循环结构
- 各自语法不同
- do…while 更适用于需要先执行一次再判断的情况。while和for适用先判断 再执行的情况

### while 循环

#### 概念

- while跟for一样，都是用于循环的语法结构

#### 语法

```js
while(循环继续条件){    //要循环执行的代码}
```

#### 流程

1. 先判断循环继续条件是否为true，为true进入第二步。为false则直接退出while结构，循环结束
2. 执行一次`{}`里的代码，执行后退回第一步

#### 跟for的区别

- 语法不同，一个用while，一个是for
- 侧重点不同：while关心的是是否满足了循环条件，不关心次数。而for循环是由专门的语法来设置循环次数
- 能用for循环的必定能够用while循环，能够用while循环也能用for循环来解决。

### 数组

#### 数组基础

##### 概念

- 数组。即数据的”仓库”，用于保存和管理多个数据

- 官方定义：数组是一堆有序数据的集合。数组中的 每个数据都有专属的 编号—`下标`,来保证可以快速查找数组中的某个数据

- 例子：生活中的仓库以及通过分类和编号来完成快速检索：

  ![img](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/dengnaiwen/20210707155701.jpeg)

  ![仓库](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/dengnaiwen/20210707155654.jpeg)

##### 下标

- 概念：本质是一个数字，`数组中的每个数据都有一个下标`，指代某个数据在数组中的位置。
- 特点：数组中第一个数据的下标为0，第二个数据的下标为1，依次递增，第N的数据的下标为N-1。数组的最后一个数据的下标为`数组变量名.length-1`

#### 数组的定义

```js
1. 定义一个空的数组第一种方式-数组字面量形式: 
var 变量名 = [];
第二种方式:var 变量名 = new Array();
2. 定义带有默认数据的数组第一种方式：
var 变量名= [数据1,数据2,数据3...,数据n];
第二种方式:
var 变量名 = new Array(数据1,数据2,数据3,...,数据n);
例子： 
var arr1 = [];
var arr2 = new Array("张三",12,true);//带有3个默认数据的数组
var arr3 = [1,2,3,4,5];//带有5个数据的数组，
```

#### 数组的基本使用

```js
示例：var  bags  =["顺丰","圆通","顺丰","申通","东风"];
```

- 获取数组的长度:指数组中数据的个数

  ```js
  数组变量名.length;例子： console.log(bags.length);//5
  ```

- 获取某个指定下标的 数据

  ```js
  通过数据的下标来获取：数组变量名[下标]例子：document.write(bags[2]);//第3个数据   顺丰
  ```

- 修改某个数据

  ```js
  通过数据的下标来修改：数组变量名[下标] = 新数据; 例子：将下标为2的数据改为韵达bags[2] ="韵达";
  ```

- 添加数据

  ```js
  在数组的末尾添加数据数组变量名[新下标] = 数据;数组变量名[数组变量名.length] = 新数据例子：bags[5] ="邮政";
  ```

- 删除数据：删除数组中的最后一个数据

  ```js
  数组变量名.length--;例子： bags.length--;document.write(bags.length);//4
  ```

- 遍历数组: 通过循环来获取数组中的每一个数据

```js
// bags[0]// bags[1]// bags[2]// bags[3]// bags[4]
for(var i=0;i<=bags.length-1;i++){  
    document.write(bags[i]+"<br>");
}
```

##### 练习

```js
1.完成快递仓库的数据管理    
1-1. 在仓库中追加多个快递:顺丰、圆通、韵达、韵达、百世、滴答、顺丰、顺丰    
1-2. 输出所有的快递    
1-3. 删除最后一个快递并输出该快递    
1-4. 仓库中有几个快递    
1-55. 扩展：倒序输出快递    
1-6. 扩展：仓库中有几个顺丰快递，几个韵达快递2.随机点名：定义一个数组，数组里保存多个名字，实现页面随机输出一个名字功能3.获取某个长度不大于6的数组的动态和数组。所谓动态和数组是指数组里的每个数据都是原数组对应位置及之前的数据之和。比如      
Var arr = [1,2,4,5]     
那么arr的动态和数组为[1,3,7,12]      
解析:   [1,1+2,1+2+4,1+2+4+5]
4. 判断数组中是否包含了某个数据，输出false或true5.输出某个数据在数组中的位置，没有则输出-16.随机生成一个电话号码(11位，第一位必须是1)
```

#### 二维数组

##### 概念

- 一维数组：是指数组里的数据都是基本类型的数据，不包含数组本身。

  ```js
  var arr =[1,"张三",true,2];
  ```

- 二维数组：是指一个数组里的每个数据都是一个一维数组。

  ```js
  var arr1 = [1,"张三",true,2];
  var arr2 = [2,3,1,4];
  var arr3 = ['admin','ad123'];
  二维数组：
  var arr = [arr1,arr2,arr3];或
  var arr = [    [1,"张三",true,2],    [2,3,1,4],    ['admin','ad123']];
  ```

##### 基本使用

- 示例二维数组

  ```js
  var students = [    ['李云龙',35,'男','独立团'],    
                  ['二营长',25,'男','二营'],       
                  ['翠花',25,'女','二营']];
  ```

- 获取指定下标的数据

  ```js
  1. 获取某个一维数组数组变量名[下标] 
  2. 获取某个一维数组中的某个数据数组变量名[下标][一维数组中的 下标]
  例子：
  1. 获取二营长的所在一维数组 students[1]
  2. 获取二营长字符串本身。students[1][0]
  ```

- 修改指定下标的数据

  ```js
  1. 修改某个一维数组数组变量名[下标] = 新一维数组
  2. 修改某个一维数组中的某个数据数组变量名[下标][一维数组中的下标] = 新数据例子： 
  1. 将二营长所在一维数组改为["周星星",35,'男','威龙中学'];students[1] = ["周星星",35,'男','威龙中学'];
  2. 将周星星改为9527students[1][0] ="9527";
  ```

- 添加数据

  ```js
  1. 末尾添加一个新的一维数组 数组变量名[数组变量名.length] =新一维数组 数组变量名.push(新一维数组);
  2. 二维数组中的 某个一维数组末尾添加一个数据二维数组变量名[下标].push(新的数据)
  例子： 
  1. 二维数组追加['白晶晶',23,'女','盘丝洞'];  
  students.push(['白晶晶',23,'女','盘丝洞']);
  2. 白晶晶一维数组中追加微信: 10086  
  students[students.length-1].push('10086');
  ```

- 删除末尾数据

  ```js
  1. 删除最后一个一维数组 二维数组变量名.pop() 或 二维数组变量名.length--;
  2. 删除指定一维数组中的最后一个数据 二维数组变量名[一维数组下标].pop(); 或  二维数组变量名[一维数组下标].length--;
  ```

- 获取数组长度

  ```js
  数组变量名.length;//有多少个一维数组
  ```

- 总结

  - 如果是直接对二维数组进行增删查改，方式跟以前的是一致的。
  - 如果是操作二维数组里的某个一维数组时，方式就在二维数组变量名后多了个`[下标]`

### 数组常用函数

#### API 基础概念

- API(应用编程接口- application programming interface)。软件层面上已经写好的，开发人员可以直接进行使用的代码。比如 `Math.random()`、`Number()、parseInt()、parseFloat()`等代码，每一个都是一个api。无需知道原理，直接进行使用。
- JavaScript已经内置了很多api，用于快速完成针对数组的常见操作，比如添加删除数据、倒序存放，排序等。

#### 数组相关API(ES3)

- push:追加
- pop:删除末尾数据
- unshift:开头添加
- shift:删除开头的数据
- join:拼接成字符串
- splice：数组指定位置的插入和删除
- slice：获取数组的一部分
- sort：数组排序
- indexOf：获取数据第一次出现下标
- lastIndexOf：获取数据最后一次出现下标
- includes：是否有某个数据

#### 数组常用API

##### push

- 在数组末尾添加一个或多个数据

  ```
  语法： 数组变量名.push(数据1,数据2,数据n);
  例子： 
  var arr = [1,2,3,4];1. 追加 2   
  arr.push(2);2.追加 张三  李四arr.push("张三","李四");
  ```

##### pop

- 删除数组最后一个数据。可以用变量接收被删除的数据。

  ```js
  语法： 数组变量名.pop();
  例子：
  var arr = [1,2,3,4];
  1. 直接删除最后一个数据arr.pop(); 
  2. 直接删除最后一个数据并将被删除的 数据保存到变量中以便后续使用var elem = arr.pop();
  ```

##### unshift

- 在数组开头添加一个或多个数据

  ```js
  语法： 
  数组变量名.unshift(数据1,数据2,数据n);
  例子： 
  var arr = [1,2,3,4];
  1. 开头添加 2   
  arr.unshift(2);//[2,1,2,3,4]
  2.开头添加 张三  李四arr.unshift("张三","李四");//["张三","李四",1,2,3,4]
  ```

##### shift

- 删除开头的第一个数据。也可以用变量保存被删除的数据。

  ```js
  语法： 数组变量名.shift();
  例子：
  var arr = [1,2,3,4];
  1. 直接删除开头一个数据arr.shift(); 
  2. 直接删除开头一个数据并将被删除的 数据保存到变量中以便后续使用
  var elem = arr.shift();
  ```

##### join

- 按照某个连接符号，将数组里所有的数据连接成一个字符串,不影响原数组

  ```js
  语法： 数组变量名.join(连接字符);
  例子： 
  var arr = [1,2,3,4];
  1. 按照逗号将数组连接成一个字符串 
  var str = arr.join();// "1,2,3,4"
  2. 按照-将数组连接成一个字符串 
  var str = arr.join("-");// "1-2-3-4"
  ```

##### splice

- 指定位置进行插入数据或删除数据

  ```js
  语法：数组变量名.splice(插入或删除的开始下标,要删除数据的个数,要插入的数据1，要插入的数据2，...,要插入的数据n);
  例子：
  var arr =[1,2,3,4];
  1. 从下标1开始删除，删除2个 ，不插入 arr.splice(1,2);//[1,4]
  2. 删除数据3，并追加5 和6  
  arr.splice(2,1,5,6);//[1,2,5,6,4];3. 在下标为2处追加5 和6   arr.splice(2,0,5,6);//[1,2,5,6,3,4];
  ```

- 如果只是插入，那么会在指定下标之前插入数据

##### slice

- 获取数组中的 一部分。会把开始下标到结束下标为止的数据组成一个新数组，可以用变量来获取该新数组。

- 新数组不包含结束下标对应的数据

  ```js
  数组变量名.slice(开始下标，结束下标)
  例子：
  var arr =[1,2,3,4];
  1. 得到[2,3]
  var newArr = arr.slice(1,3);
  ```

##### sort

- 完成对数组的排序。默认是按照字母或数字的自然顺序来进行排序，对字符串比较友好，但如果是纯数字排序，则会有问题。

  ```js
  1. 按照字母顺序进行排序： 数组变量名.sort();
  2. 按照大小进行升序数组变量名.sort((a,b)=>a-b);
  3. 按照大小进行降序数组变量名.sort((a,b)=>b-a);
  4. 数组随机排序数组变量名.sort((a,b)=>Math.random()-0.5);
  ```

  - 原理：数字排序是借助了以一个函数作为排序规则其中的a或b是指的数组中的相邻的两个数据，a-b意味着进行升序排序。b-a意味着降序。

##### reverse

- 实现数组的倒序存放

  ```js
  语法： 数组变量名.reverse();例子：
  var arr =[1,2,3,4];
  1. 倒序存放
  arr.reverse();document.write(arr);
  ```

##### indexOf

- 找到某个数据在数组中第一次出现的下标，没有则为-1

  ```js
  语法 数组变量名.indexOf(数据)
  例子：找到数据2的第一次出现的下标
  var arr =[1,2,3,4];
  var i = arr.indexOf(2);
  var x= arr.indexOf(6);
  document.write(i,x);1 -1
  ```

##### lastIndexOf

- 找到某个数据在数组中最后一次出现的下标，没有则为-1

  ```js
  语法 数组变量名.lastIndexOf(数据)
  var arr =[1,2,3,4];
  例子：找到数据2的最后一次出现的下标
  var arr =[1,2,3,4,2,3];
  var i = arr.lastIndexOf(2);
  var x= arr.lastIndexOf(6);
  document.write(i,x);4 -1
  ```

##### includes

- 判断数组是否有某个数据，得到true或false

  ```js
  语法： 数组变量名.includes(数据);
  例子：
  var arr =[1,2,3,4];
  var result = arr.includes(6);
  document.write(result);//false
  ```

#### 检测是否为数组

- instanceof 运算符

  - instanceof 可以判断一个对象是否是某个构造函数的实例

    ```js
    var arr = [1, 23];
    var obj = {};
    console.log(arr instanceof Array); // true
    console.log(obj instanceof Array); // false
    ```

- Array.isArray()

  - Array.isArray()用于判断一个对象是否为数组，isArray() 是 HTML5 中提供的方法

    ```js
    var arr = [1, 23];
    var obj = {};
    console.log(Array.isArray(arr));   // true
    console.log(Array.isArray(obj));   // false
    ```

#### 添加删除数组元素的方法

##### 练习

```js
定义一个成绩数组[45,12,89,92,53,76,89,61]，完成以下题目，每个小问独立。
1.数组开头添加78
2.数组中追加34、89、90
3.删除第一个数据
4.删除最低分，并在同样的位置插入56、67
5.将数组转为字符串 进行输出，成绩间以”-”分割
6.获取第一次和最后一次出现89的下标
7.所有分数+5分
8.获取所有不及格的分数,得到一个新数组
9.获取最高分以及最低分
```

### 编程技巧

#### 快速实现字符串转为数字

```js
 var num = "123" - 0; //123
```

#### 开关变量

- 如果需要手动控制循环，那可以在循环外面定义一个布尔型的变量。

  ```js
  var isOver = false;while(isOver ==false){}
  ```

  - 只要程序中间某个地方将`isOver`改为true，就可以达到控制循环的的目的

#### 在数组中判断是否有某数据，或者找某数据时

- 定义一个开关变量来处理

  ```js
   // 判断数组中是否包含了某个数据，输出false或true        
   var arr  = [1,4,3,2,6,9];        
   var num = 5;        
   var result = false;//定义开关变量，用于保存是否有该数据，默认假设没有。        
   //判断数组中是否有4 ,        
   //思路；获取数组中的每个数据，依次进行判断        
   for(var i=0;i<arr.length;i++){           
   if(num == arr[i]){               
   //找到了，结果为true               
   result = true;           
   }       
   }      
   document.write(result);
  ```

## 函数

### 目录

- 函数基础
  - 函数概念
  - 函数定义和基本使用
- 函数参数
  - 形式参数
  - 实际参数
  - 区别和联系
- 函数返回值
- arguments
- 箭头函数

### 函数基础

#### 背景

- 如何获取不同数组的最大值并进行处理

  ```js
   // 需求：如何获取不同数组的最大值
  var arr1 =[3,2,1,6,4];
  var arr2 =[2,1,7,5,6];
  var arr3 =[1,2,7,8,3];
  //获取arr1最大值
  var max1 =arr1[0];
  //假设第一个数据是最大值
  //遍历数组，依次进行比较，把更大的赋给max
  for(var i=0;i<arr1.length;i++){    
      if(max1 <arr1[i])
          max1 =arr1[i];   
  }}
  document.write(max1);
  //获取arr2最大值
  var max2 =arr2[0];//假设第一个数据是最大值//遍历数组，依次进行比较，把更大的赋给max
  for(var i=0;i<arr2.length;i++){    
      if(max2 <arr2[i]){
          max2 =arr2[i];    
      }
  }
  document.write(max2);
  //获取arr3最大值
  var max3 =arr3[0];//假设第一个数据是最大值//遍历数组，依次进行比较，把更大的赋给max
  for(var i=0;i<arr3.length;i++){    
      if(max3 <arr3[i]){max3 =arr3[i];    
                       }
  }
  document.write(max3);//
  ```

  - 问题：针对不同数据的同一个操作，往往会导致代码重复，效率不高 —函数

#### 函数概念

- 函数是一段代码的容器。一个函数可以包含一段代码。函数里的代码可以多次使用

#### 作用

- 可以多次执行函数里的代码

#### 定义和使用

- 定义一个函数

  ```js
  function 函数名(){    被包含的一段代码}
  ```

- 使用(调用)函数

  ```js
  函数名();
  ```

  - 每调用一次函数，都会执行一次函数里的所有代码
  - 函数可以多次调用

- 例子

  ```js
  function demo(){    
  document.write("demo函数执行");
  }
  demo(); // 输出demo函数执行
  demo(); // 输出demo函数执行
  ```

#### 函数名的规范

- 建议函数名只包含字母、数字、_、$
- 见词达义。
- 不能以数字开头
- 建议以小驼峰风格命名
  - 大驼峰：所有单词的首字母大写，其他全小写。比如GetArrayMax。一般适用于类名等
  - 小驼峰:除了首个单词全小写以外，其他单词首字母大写，其他字母小写。比如getArrayMax. 一般适用于函数

#### 函数参数

##### 背景

- 目前函数可以解决了重复调用代码的问题，但是函数目前不能够对不同的数据进行处理。

  ```js
  var arr1 =[3,2,1,6,4];
  var arr2 =[2,1,7,5,6];
  var arr3 =[1,2,7,8,3];
  function getArrayMax(){    
  var max1 =arr1[0];//假设第一个数据是最大值    
  //遍历数组，依次进行比较，把更大的赋给max    
  for(var i=0;i<arr1.length;i++){        
  if(max1 <arr1[i]){            
  max1 =arr1[i];       
  }    
  }   
  document.write(max1);
  }
  getArrayMax();//6
  getArrayMax();//6
  getArrayMax();//6
  ```

  - 每次都是一样的结果。

##### 参数

- 概念：参数是函数专用的一种机制，能够实现函数去处理不同的数据

- 原理：函数可以通过形式参数和实际参数的协同工作，能够将需要处理的数据从函数外传入到函数体`{}`里面进行处理。

- 目的：为了将函数外面的数据传入到函数体里进行处理

- 分类：

  - 形式参数
    - 是写在函数定义时`()`里的变量，形式参数只能在函数体里使用，并且形式参数里的数据来自于实际参数
  - 实际参数
    - 是写在`函数调用时()`里的具体的数据或函数外已定义的变量。会在调用时将实际参数的数据赋给形式参数。
  - 形式参数和实际参数的联系和区别
    - 形式参数和实际参数是一起工作的 。在函数调用时，我们将需要处理的数据通过实际参数传递给形式参数，在函数体里去处理形式参数。

- 参数例子

  ```js
  function 函数名(形式参数){    
  在这里可以使用形式参数}函数名(实际参数);
  例子：
  var data =6;function demo(num){    
  num =实际参数；
  }
  demo(5); // num=5
  demo(data);//num =6
  ```

#### 函数返回值

##### 背景

- 一般情况下，我们在函数中处理后的变量是不能直接在函数调用后进行使用的。需要搭配返回值才可以实现。

##### 概念

- 函数返回值是指可以在函数体中通过特殊关键字`return`来获取函数体里处理的数据

##### 语法

```js
function 函数名(){   
return 要返回的数据;
}
在函数调用后用变量来接收
var 变量名 = 函数名();
例子：// 1 
function 榨汁(fruit){    
var result = `${fruit}汁`;    
return result;
}
var 杯子 = 榨汁("苹果");//2
function add(a,b){    
var sum = a +b;    
return sum;
}
var total = add(5,4);
document.write(total);//9
```

##### 特点

- 一个函数在执行`return`后会立即结束函数，如果return后还有函数的 代码每执行，则不管。

- return不一定在最后一行。比如说对函数传进来的参数做验证。

  ```js
  /例子：验证水仙花数的时候，必须保证是一个三位数
  function isFlowerNumber(num){    
  if(num <100 || num >999){     
  return false;    
  }    
  var ge = num %10;     
  var shi  = parseInt(num/10%10);     
  var bai = parseInt(num/100);    
  if(ge *ge *ge +shi*shi*shi + bai*bai*bai ==num){         
  return true;    
  }else{        
  return false;    
  }
  }
  ```

##### 练习

```js
1. 定义一个函数，传入一个数字，用于判断是否是质数，并输出结果
2. 定义一个函数，传入一个数字，用于判断是否是水仙花数，并输出结果
3. 定义一个函数，传入一个数组，判断数组是否存在小于0的数据，并输出结果
4. 定义一个函数，传入2个数字start和end，获取从start累加到end的和并输出
```

#### arguments

- 背景

  - 在函数中需要传入不定数量的参数时，形式参数就不确定要写多少个。—-arguments

- 概念：

  - JavaScript独有的用于实现处理不定数量参数的机制。

- 特点

  - arguments在函数中会表现为一个数组，本质上arguments是一个对象，可以以数组的方式来进行操作。
  - 函数调用时传入的所有实际参数都会保存在arguments，参数在arguments中的顺序跟调用时传入的顺序保持一致。
  - 在开发中arguments只能在函数体里直接使用，无需定义。

- 使用

  ```js
  function demo(){    console.log(arguments);//[1,2,3]}demo(1,2,3);
  ```

- 获取每一个实际参数

  - 对arguments进行遍历

    ```js
    for(var i=0;i<arguments.length;i++){    arguments[i]}
    ```

#### 箭头函数

- 背景

  - 当调用某些函数时，需要将其他的某个函数作为参数来进行使用，那么在这种情况下，普通函数的定义方式会显得整体的函数代码比较繁琐。——箭头函数进行优化

- 概念

  - 箭头函数是ES6提供的一种新的定义函数的语法，比普通语法更加简洁。

- 语法

  ```js
  1. 箭头函数
  var 函数名 = (形式参数)=>{    
  函数体里的代码}
  2. 普通函数function 函数名(形式参数){    函数体里的代码}
  ```

- 特点

  - 如果箭头函数只需要一个形式参数，那么包裹形式参数的`()`可以省略不写
  - 如果函数体里只有一句`return`代码，那么包裹函数体的代码的`{}`以及`return`关键字可以省略不写

- 应用

  - 箭头函数在数组中api 的应用

    ```js
    var arr=[12,34,43,78,89];
    arr.sort((a,b)=>a-b);
    等同于
    arr.sort(function(a,b){    return a-b});
    ```

### 冒泡排序

#### 概念和特点

- 冒泡排序是针对数组的一种经典入门排序算法。

#### 特点

- 理解较易
- 性能较低

#### 算法详情

##### 原理

- 完整的冒泡排序分为多次排序过程。每次的排序过程会将未排序的最大的数字通过相邻数据进行比较及交换位置的方式 来放置到末尾

##### 具体过程

```js
var arr =[4,1,2,6,5,8,7,3];
第一次排序过程，将8放在末尾：  
1. 4和1比较，4>1 交换  [1,4,2,6,5,8,7,3];  
2. 4和2比较，4>2 交换 [1,2,4,6,5,8,7,3];  
3. 4和6比较  4<6 不交换 [1,2,4,6,5,8,7,3];  
4. 6和5比较  6>5 交换 [1,2,4,5,6,8,7,3];  
5. 6和8比较  6<8 不交换 [1,2,4,5,6,8,7,3];  
6. 8和7比较  8>7 交换 [1,2,4,5,6,7,8,3];  
7. 8和3比较  8>3 交换 [1,2,4,5,6,7,3,8];
第二次排序过程，将7放在倒数第二位：  
1. 1和2比较，1<2 不交换  [1,2,4,5,6,7,3,8];  
2. 2和4比较，2<4 不交换 [1,2,4,5,6,7,3,8];  
3. 4和5比较  4<5 不交换 [1,2,4,5,6,7,3,8];  
4. 5和6比较  5<6 不交换 [1,2,4,5,6,7,3,8];  
5. 6和7比较  6<7 不交换 [1,2,4,5,6,7,3,8];  
6. 7和3比较  7>3 交换[1,2,4,5,6,3,7,8];
第三次排序过程，将6放在倒数第三位：  
1. 1和2比较，1<2 不交换 [1,2,4,5,6,3,7,8];  
2. 2和4比较，2<4 不交换 [1,2,4,5,6,3,7,8]; 
3. 4和5比较  4<5 不交换 [1,2,4,5,6,3,7,8];  
4. 5和6比较  5<6 不交换 [1,2,4,5,6,3,7,8];  
5. 6和3比较  6>3 交换  [1,2,4,5,3,6,7,8];。。。一共需要length-1次排序过程。
```

#### 代码

```js
var arr =[4,1,2,6,5,8,7,3];        //冒泡排序        
for(var i=0;i<arr.length-1;i++){            
    //第i次排序过程            
    for(var j=0;j<arr.length-1;j++){                
        //前一个位置的数据大于了后一个位置的数据，进行交换                
        if(arr[j]>arr[j+1]){                    
            // 交换                    
            var temp = arr[j];//使用临时变量把旧的数据保存下来                    
            arr[j] = arr[j+1];                    
            arr[j+1] =temp;//把旧的数据赋给另一个位置                
        }           
    }      
}document.write(arr);
```

### JavaScript内置api

#### 目录

- String
  - **charAt**:通过下标获取字符串里的某个字符
  - concat:多个字符串拼接
  - **substr**：获取字符串中的一部分
  - **subString**:获取字符串中的一部分
  - slice:获取字符串中的一部分
  - **split**：根据某个分割符号，将字符串转为字符串数组
  - indexOf：查找某个字符在字符串中第一次出现的下标
  - lastIndexOf:查找某个字符在字符串中最后一次出现的下标
  - **replace/All**：完成字符串中某些字符的替换
  - trim：消除字符串两端的空白字符
  - startsWith：判断某字符串是否以某些字符开头
  - endsWith：判断某字符串是否以某些字符结尾
  - **for…of**：ES6提供的用于遍历字符串
- Math
  - min：获取 几个数据的最小值
  - max：获取 几个数据的最大值
  - floor：向下取整。获取最接近并不大于某个数字的整数
  - ceil：向上取整。获取最接近并大于某个数字的整数
  - round：获取某个数字的四舍五入后的数值
  - pow：计算x的y次方
  - sqrt：计算某个数字的开平方后的数值 。
- Date
  - 获取日期对象
    - new Date()
  - 获取毫秒数
    - getTime()
  - 获取年月日时分秒
    - getFullYear
    - getMonth
    - getDate
    - getHours
    - getMinutes
    - getSeconds
  - 获取年月日时分秒
    - setFullYear
    - setMonth
    - setDate
    - setHours
    - setMinutes
    - setSeconds
  - 获取星期几
    - getDay:0~6 0表示星期天，1~6分别表示星期1到星期6
- Array(ES5）
  - forEach：用于数组的快速遍历，用于替代传统的for循环遍历
  - filter：遍历数组，同时筛选出满足条件的数据，返回一个新数组
  - map：遍历数组，同时会将每次遍历处理后的数据加入新数组中，并返回。
  - some：遍历数组，如果数组中有一个数据满足指定条件，那么some方法返回true，否则返回false
  - every：遍历数组，如果数组中所有数据满足指定条件，那么every方法返回true，否则返回false
  - reduce：一种用于数组的累计 快捷操作，能够快速得到一个累计的数值，比如数组数据累加，累积等。

### String

##### 概念

- JavaScript针对字符串的常规操作内置了很多实用的api，方便开发人员使用，提高开发效率

#### 常用api

- ##### charAt:根据下标找到字符串中对应的字符

  ```js
  字符串.charAt(下标)例子:
  var str = "hello world";
  console.log(str.charAt(0)); 'h'
  console.log(str.charAt(6)); 'w' ,在程序中空格也是一个字符
  ```

- ##### concat:多个字符串拼接

  ```js
  字符串.concat(字符串1,字符串2,...,字符串N);
  例子：
  var str = "hello";
  var newStr = str.concat(' woniu','xy');
  console.log(newStr);"hello woniuxy"
  ```

- 获取字符串中的一部分

  - ##### substr

    ```js
    字符串.substr(子字符串的开始下标,子字符串的长度);
    例子:
    var str = "hello woniuxy";
    获取woniuvar 
    newStr = str.substr(6,5);
    ```

    - 如果要获取的子字符串是从中间直接到末尾，那么第二个参数可以省略不写

  - ##### substring

    ```js
    字符串.substring(子字符串的开始下标,子字符串的结束下标(不包含));
    例子:
    var str = "hello woniuxy";获取woniuvar 
    newStr = str.substring(6,11);
    ```

    - 如果要获取的子字符串是从中间直接到末尾，那么第二个参数可以省略不写

  - ##### slice

    ```js
    字符串.slice(子字符串的开始下标,子字符串的结束下标(不包含));
    例子:
    var str = "hello woniuxy";获取woniuvar 
    newStr = str.slice(6,11);
    ```

    - 不推荐,避免跟数组的slice搞混

- ##### indexOf：查找某个字符在字符串中第一次出现的下标,没有找到则返回-1。 同时也可以指定开始查找的位置，默认为0。

  ```js
  字符串.indexOf('字符');
  字符串.indexOf('字符',开始查找下标);
  例子： 
  var str = "hello woniuxy";
  var index = str.indexOf('w');// 6
  var index = str.indexOf('a');// -1
  ```

- ##### lastIndexOf:查找某个字符在字符串中最后一次出现的下标，,没有找到则返回-1

  ```js
  字符串.lastIndexOf('字符');
  例子： 
  var str = "hello woniuxy";
  var index = str.lastIndexOf('o');// 7
  var index = str.lastIndexOf('a');// -1
  ```

- ##### split:根据某个分割符号，将字符串转为字符串数组。

  ```js
  字符串.split('分割符号');
  var str = "1,2,3,4,5,6";
  var arr = str.split(",");
  console.log(arr);//["1","2","3","4","5","6"];
  ```

- ##### replace/replaceAll:替换字符串中的单个/某些字符

  ```js
  1. 替换找到的第一个字符字符串.replace('旧字符','新字符'); 
  2. 替换所有找到的字符字符串.replaceAll('旧字符','新字符'); 
  例子：将空格变为%
      var str ="we are family";
  var newStr = str.replace(' ','%');
  console.log(newStr);"we%are family";
  ```

- ##### for…of(ES6)：遍历字符串

  ```js
  for(var 字符变量名 of 字符串){    
      //每次遍历会将一个字符赋给字符变量
  }
  例子：
  var str ="we are family";
  for(var ch of str){    
      console.log(ch)
  }
  ```

- ##### startsWith:以什么开头,返回true或false

  ```js
  字符串.startsWith("字符");
  例子:var str ="we are family";
  console.log(str.startsWith('we'));true
  console.log(str.startsWith('w'));true
  console.log(str.startsWith('e'));false
  console.log(str.startsWith('we are family'));true
  ```

- ##### endsWith:以什么结尾。返回true或false

  ```js
  字符串.endsWith("字符");
  例子:
  var str ="we are family";
  console.log(str.endsWith('ly'));true
  console.log(str.endsWith('y'));true
  console.log(str.endsWith('mi'));false
  console.log(str.endsWith('family'));true
  ```

- ##### trim:消除两端空白

  ```js
  字符串.trim();例子：
  var str = "   he llo   ";
  console.log(str.trim());
  ```

##### JavaScript中的字符串的特点

- JavaScript中字符串虽然本身不是数组，但是每个字符串也都有length属性，以及可以通过下标来得到指定位置的字符。

  ```js
  var str = "hello";for(var i=0;i<str.length;i++){    str[i]}
  ```

### Array（ES5）

#### 概念

- 提供了很多实用的api

- 针对ES5的数组api的一般使用格式

  ```js
  数组变量名.函数名(function(value,index,array){   
  //每次遍历都会将遍历的数据拿到该函数中并执行一次    
  //value :当前遍历的数组中的数据   
  //index:当前遍历数据在数组中的下标    
  // array:当前正在遍历的数组本身，一般很少用    
  //没有使用的参数可以省略    
  console.log(value,index,array);    
  });
  ```

#### 常用api

- ##### forEach：用于数组的快速遍历，用于替代传统的for循环遍历

  ```js
  var arr = [23,43,12,90,79,45];
  arr.forEach(function(value,index,array){   
      console.log(value,index,array);  
  });
  ```

- ##### filter：遍历数组，同时筛选出满足条件的数据，返回一个新数组

  ```js
  var arr = [23,43,12,90,79,45];//找到所有及格的成绩
  var newArr = arr.filter(function(value,index,array){    
      //满足条件的数据用return返回true即可    
      if(value>=60){        
          return true;    
      }else{        
          return false;  
      }    //return value >=60;
  });
  console.log(newArr);[90,79];
  ```

- ##### map：遍历数组，同时会将每次遍历处理后的数据加入新数组中，并返回。

  ```js
  数组变量名.map(function(value,index,array){   
  会将return 后的数据放入新数组中})；
  例子：数组里的所有数据+5 
  var arr = [23,43,12,90,79,45];
  var newArr = arr.map(function(value,index,array){  
  return  value +5;
  })；
  console.log(newArr);
  //箭头函数
  var newArr =arr.map(value=>value+5);
  ```

  - 会对数组的每个数据进行处理，并把处理后的数据放入新数组中

- ##### some：遍历数组，如果数组中有一个数据满足指定条件，那么some方法返回true，否则返回false

  ```js
  数组变量名.some(function(value,index,array){   
      需要将判断的结果进行return，只要数组遍历过程中有一个是return的true，那么some会返回true。只有所有遍历的数据都return false，最终some 才返回false})；例子：判断是否有人不及格
  var arr = [23,43,12,90,79,45];
  var result = arr.some(function(value,index,array){  return  value <60;})；console.log(result);//true
  ```

- ##### every：遍历数组，如果数组中所有数据满足指定条件，那么every方法返回true，否则返回false

  ```js
  数组变量名.every(function(value,index,array){   
      需要将判断的结果进行return，只要数组遍历过程中有一个是return的true，那么some会返回true。只有所有遍历的数据都return false，最终some 才返回false})；
  例子：判断是否所有人都及格
  var arr = [23,43,12,90,79,45];
  var result = arr.every(function(value,index,array){  return  value >= 60;})；console.log(result);//false
  ```

- ##### reduce：一种用于数组的累计 快捷操作，能够快速得到一个累计的数值，比如数组数据累加，累积等。

  ```js
  数组变量名.reduce(function(data,value,index,array){    
      data是遍历上一个数据之后累计的值，当处理完当前遍历数据之后需要return一个新的数据，该数据会作为下一个遍历数据的data。最终reduce函数会返回最后一个遍历数据的return值。});
  例子:完成数组的累加。即求数组所有数据的之和//箭头函数/
  var total = arr.reduce((data,value)=>data+value,0);//普通函数
  var total = arr.reduce(function(data,value){    
      return data +value;},0);/*         
      解析：         
      第一次遍历：手动的初始值0作为遍历的第一个数据的data值，return 0+ 23               
      return后的数据0+23作为遍历的第二个数据的data值         
      第二次遍历：data的值为0+23                
      return后的数据23+43作为遍历的第三个数据的data值         
      第三次遍历：data的值为23+43                
      return后的数据23+43+12作为遍历的第四个数据的data值             ...         
      第6次遍历：data的值为 23+43+12+90+79                     
      return后的数据23+43+12+90+79 + 45作为reduce函数的返回值         */
  ```

### Math

#### 概念

- JavaScript为了方便进行数学的常规运算，内置了很多的 api来进行使用

#### 常用api

- ##### min：获取 几个数据的最小值

  ```js
  Math.min(数字1,数字2,数字3,...,数字n);例子：
  var num = Math.min(3,2,1,6,-9);
  console.log(num);//-9数组的最小值
  var arr =[3,4,1,5,6];
  var min = Math.min(...arr);
  ```

- ##### max：获取 几个数据的最大值

  ```js
  Math.max(数字1,数字2,数字3,...,数字n);例子：
  var num = Math.max(3,2,1,6,-9);
  console.log(num);//6数组的最大值
  var arr =[3,4,1,5,6];
  var min = Math.max(...arr);//6
  ```

- ##### floor：向下取整。获取最接近并不大于某个数字的整数

  ```js
  Math.floor(数字);
  例子：
  var num = Math.floor(4.3);
  console.log(num);//4
  ```

- ##### ceil：向上取整。获取最接近并不小于某个数字的整数

  ```js
  Math.ceil(数字);
  例子：
  var num = Math.ceil(4.3);
  var num1 = Math.ceil(4);
  console.log(num);//5console.log(num1);//4
  ```

- ##### round：获取某个数字的四舍五入后的数值

  ```js
  Math.round(数字);例子：
  var num1 = Math.round(4.4);
  var num2 = Math.round(4.5);
  var num3 = Math.round(-11.5);
  var num4 = Math.round(-11.7);
  console.log(num3);//-11
  console.log(num4);//-12
  console.log(num1);//4
  console.log(num2);//5
  ```

- ##### pow：计算x的y次方

  ```js
  Math.pow(底数，指数);例子：
  var num1 = Math.pow(2,3);//2的3次方
  var num2 = Math.pow(3,4);//3的4次方
  var num3 = Math.pow(3,-2);//3的-2次方
  console.log(num1);//8
  console.log(num2);//   1/9
  ```

- ##### sqrt：计算某个数字的开平方后的数值 。

  ```js
  Math.sqrt(数字);例子：
  var num = Math.sqrt(9);
  console.log(num);//3
  ```

### Date

#### 概念

- JavaScript提供了最基础的日期的api。比如获取和设置某个时间的年月日时分秒。

#### 常用api

- 设置日期对象

  ```js
  1. new Date() 指代的是当前时间
  var 变量名 = new Date();//保存了当前时间
  ```

- 获取/设置年月日时分秒

  - 获取
    - getYears()
    - getMouth();
    - getDate()
    - getHours();
    - getMinutes();
    - getSeconds();
  - 设置
    - setYears(年份)
    - setMouth(月份);
    - setDate(日期)
    - setHours(小时);
    - setMinutes(分钟数);
    - setSeconds(秒);

  ```js
  var time = new Date();获取
  var year = time.getFullYear();
  var month = time.getMonth(); 0~11 0表示1月
  var day = time.getDate()
  var hours = time.getHours();
  var minutes = time.getMinutes();
  var seconds = time.getSeconds();
  console.log(year,month+1,day,...,seconds);
  ```

- 获取某个时间点的毫秒数

  - getTime():获取从1970年1月1日0时0分0秒到指定时间的毫秒数

    ```js
    时间日期对象名.getTime();
    例子：获取当前时间的毫秒数
    var now = new Date();
    var time = now.getTime();
    console.log(time);
    ```

- 获取星期几

  ```js
  日期对象变量名.getDay();  0~6:0表示星期天 例子：今天是星期几
  var time = new Date();
  var day = time.getDay();
  console.log(day);//2    星期2
  ```

- 自定义时间输出格式

  ```js
  //按照指定格式输出//如：YYYY-MM-DD HHSS  对应  2021-09-23 12:34:14
  function getTime(str,date){    
      // 
      var now = new Date();    
      var now = date;    
      str = str.replaceAll(/YYYY/g,now.getFullYear());    
      str = str.replaceAll(/MM/g,now.getMonth()+1);    
      str = str.replaceAll(/DD/g,now.getDate());    
      str = str.replaceAll(/HH/g,now.getHours());    
      str = str.replaceAll(/mm/g,now.getMinutes());    
      str = str.replaceAll(/SS/g,now.getSeconds());    
      return str;
  }
  例子：
  console.log( getTime("YYYY/MM/DD HH/mm/SS",new Date()));
  ```

#### 堆栈

- 堆栈空间分配区别：

　　1、栈（操作系统）：由操作系统自动分配释放存放函数的参数值、局部变量的值等。其操作方式类似于数据结构中的栈；

简单数据类型存放到栈里面

　　2、堆（操作系统）：存储复杂类型(对象)，一般由程序员分配释放，若程序员不释放，由垃圾回收机制回收。

![](E:\qiand\07-10 JavaScript网页编程\01-JavaScript基础语法资料\JavaScript基础第06天\4-笔记\images\图片11.png)

- 简单数据类型的存储方式

  ​		值类型变量的数据直接存放在变量（栈空间）中

![](E:\qiand\07-10 JavaScript网页编程\01-JavaScript基础语法资料\JavaScript基础第06天\4-笔记\images\图片12.png)

- 复杂数据类型的存储方式

  ​		引用类型变量（栈空间）里存放的是地址，真正的对象实例存放在堆空间中



##### 练习

```js
String;
1.用户输入一串数字，设法在每个数字之间插入[2个随机字母(大小写)，并输出整个字符串   1792     1yu7gk9jk2     forof 
2.实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy replace
3.字符串解析,现有一字符串,"卡巴斯基#杀毒软件#免费版#俄罗斯#",解析出每个元素
4."那车水马龙的人世间,那样地来 那样地去,太匆忙"最后一次和第一次出现"那"的位置
5.判断输入的字符串是否是 .java 结束
6.某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换
7.定义一个函数，传入一个字符串，用于删除最后一位,并返回删除后的字符串
8.给定一个字符串,判断该字符串中是否包含某个子串.如果包含,求出子串的所有出现位置.如:"abcbcbabcb34bcbd"中,"bcb"子串的出现位置为: 1,7,12.字符串和子串均由用户输入 indexOf()
9. 一段文本，以空格分割，各个单词首字母大写。比如”html css javascript” =>”Html Css Javascript”;  需学习字符串的toUpperCase():将某个字符或字符串转为大写。
10. 统计字符串中每个字符的个数.比如：”acddcca”;   输出[[‘a’,2],[‘d’,2],[‘c’,3]]
11. 用户输入一段文字，判断是否是一张图片的路径(要求至少支持jpg和png)
12. 判断某个字符串是否是回文 （即正序和倒序是一样的，比如abcba)
Math: 1.定义一个函数，用于生成一个100内的随机正整数并返回
2.定义一个函数，可以传入多个数字，返回这些数字的最大值。
Date:
1. 计算自己已经活了多少天Array:一、定义一个成绩数组[45,12,89,92,53,76,89,61]，完成以下题目
1.获取不及格分数的总和
2.是否有不及格的分数
3.是否所有成绩都及格
4.查找所有的不及格的分数
5.获取总成绩
6.所有及格的分数减5分，返回一个新数组，该操作对原数组没影响 map二、定义一个二维数组，完成以下题目：
var  arr = [[‘张三’,12,’男’],[‘李四’,45,’男’],[‘王五’,30,’女’],[‘如花’,18,’女’],[‘9527’,26,’男’]]
1.获取所有的女生
2.获取年龄的总和
3.判断是否有未成年
4.判断是否都成年
5.所有女生减5岁，所有男生加5岁
6.按年龄对数组进行排序
```

## 原生对象

### 概念

- 原生对象是JavaScript中专门用于描述复合型数据的数据类型(即对象).
- 复合型数据是指本身是一个整体，内部包含了很多个具体的数据。比如学生包含姓名、年龄、性别等。商品数据有商品编号、价格、库存、描述、销量等
- 对象中的属性
  - 属性来源于生活。比如学生，姓名、年龄、性别是每个学生都有的特征，而特征在程序中就称为属性。
    - 比如说武器。武器的暴击率、攻击速度、移速都是武器的一个属性。

### 基本操作

#### 定义

```js
1. 定义一个空的对象var 对象变量名 = {};
2. 定义一个带有默认一些数据的对象
var 对象变量名 = {    
    属性名1:属性值1,    
    属性名2:属性值2,    
    属性名3:属性值3,   
    ...    
    属性名N:属性值N
};
例子：
1. 学生var student1 = {    
    name:'张三',    
    age:12,,    
    sex:'男'}
1. 武器：var weapon = {    
    speed:'30%',    
    damage:"20%",    
    atk:100
};
```

#### 使用

- 示例

  ```js
  var student = {   
      number:'001',    
      name:'张三',   
      age:12,   
      sex:'男',    
      class:'三年二班'
  }
  ```

- 获取对象中的某个属性

  ```js
  1.对象变量名.属性名2.对象属性名['属性名']例子：获取学生对象的姓名并输出
  console.log(student.name);
  console.log(student['name']);
  ```

- 设置对象中的某个属性(修改和添加)

  - 如果是对已经有的属性进行操作，就是修改，如果是不存在，那么就是添加属性

  ```js
  1.对象变量名.属性名 = 新属性值;
  2.对象属性名['属性名'] =新属性值;
  例子：
  修改学生姓名为李四，并添加身高为180cm
  student.name="李四";
  student.height= '180cm';
  console.log(student);
  ```

### 对象数组

#### 概念

- 一个数组里的每个数据都是一个对象的，我们称该数组为对象数组。

#### 对象遍历

##### 遍历

- 概念：获取每一个数据

```js
数组遍历：得到数组中的每一个数据   
for 对象遍历：得到对象中的每个属性名   
for in字符串遍历：得到字符串中的每一个字符 
for of
var obj ={   
    name:'zs',    
    age:12,    
    sex:'男'}
//对象遍历
for(var key in obj){    
    console.log(key,obj[key]);
    //属性名 属性值
}
```

##### 练习

```js
1.用对象来描述以下三个商品对象，之后再添加 
商品分类属性  
001 卫龙辣条  5.9   好吃又不贵    
002 乐事薯片  9.9   好吃还不贵  
003 AD钙奶   6      好吃真不贵
2.思考：是否可以将对象放入数组中，对数组进行遍历得到的是什么3.将以上3个对象放入数组中，并利用价格从低到高完成数组的排序
```

# BOM

## 目录

- window对象
  - 常用属性
    - innerWidth
    - innerHeight
  - 常用方法
    - comfirm
    - close
    - open
- 四大内置对象
  - location
    - 跳转页面
      - href
      - assign
      - replace
    - 刷新
      - reload
    - 实现页面之间数据传递
      - 使用表单提交数据后，在提交的页面用location.search获取数据，再配合字符串的api来提取数据
  - history(使用)
    - 前进
    - 后退
  - navigator(使用)
    - userAgent
  - screen(了解)
- 定时器
  - 延时
  - 间隔
- BOM和DOM是能够用JavaScript去操作浏览器页面以及控制页面的内容。

## BOM

![image-20210912192432140](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912192432140.png)

![image-20210912192449405](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912192449405.png)

### 概念

- BOM-browser-object-model（浏览器对象模型）。指的是JavaScript为了能够操作浏览器页面本身，将浏览器每个页面都抽象成一个`window原生对象`，并且window对象里面提供了一系列的api来让开发人员可以控制浏览器页面，比如新建、关闭浏览器页面、前进、后退、刷新、跳转等操作。
- 学习BOM即学习window对象以及其提供的api

### window

#### 概念

- window对象是每个HTML页面都有的一个内置原生对象，它负责了整个页面的所有操作。其内部的api能够让开发人员能够操作页面本身。

- 使用window对象

  ```js
  console.log(window);
  ```

- 当使用window对象里的属性或函数时，可以省略`window.`前缀

  ```js
  window.alert()window.prompt();
  window.innerWidth简写alert();
  prompt();
  innerWidth
  ```

### window对象常用属性

- innerWidth:获取页面的宽度

- innerHeight：获取页面首屏的高度

  ```js
  console.log(innerWidth,innerHeight);
  ```

### window对象常用函数

- alert

- prompt

- comfirm:确认框

  - 页面上会弹出一个确认框，最终函数会返回true(确认)或者false(取消)

  ```js
  var result = confirm('是否支付88888元购买迪迦');console.log(result);// true或false
  ```

- close:关闭当前页面

  ```js
  window.close();
  ```

- open:打开一个新的浏览器标签页

  ```js
  window.open('页面地址','_blank','特性字符串');
  例子：打开新页面，指向百度，尺寸为宽300 高150 ，距离页面顶部为200，距离页面左边为100 window.open('http://www.baidu.com','_blank','width=300,height=150,top=200,left=100');
  ```

- setTimeout

- setInterval

- clearTimeout

- clearInterval

### 四大内置对象

#### location

- 概念：location是window对象的一个属性，其属性值是一个对象，里面包含了一系列api能够实现跳转、刷新页面等

  ```js
  console.log(window.location);
  ```

- 属性

  - hash:页面地址中#部分的内容

  - host：页面地址中的主机全称，本地指localhost

  - **href**：完整的页面地址

    - 改变href属性也会有跳转页面的效果

      ```js
      location.href="http:www.baidu.com";//回跳到百度页面
      ```

- **search**：表单提交页面时提交的数据部分

  ```js
  地址：http://127.0.0.1:5500/%E7%AC%AC%E4%BA%8C%E5%91%A8/day03/03-BOMsid%20%E5%86%85%E7%BD%AE%E5%AF%B9%E8%B1%A1.html?username=dengnaiwen&pass=fdsvconsole.log(location.search);//?username=dengnaiwen&pass=fdsv
  ```

- protocol：地址的协议
- port：页面所在服务器的端口号
- hostname：主机名字
- pashname：页面的路径部分
- origin：当前页面是来自于哪个网站，指来源网站

- 函数

  - reload():页面的刷新

  - assign():页面的跳转

  - replace():页面的跳转

    ```js
    刷新
    location.reload();
    跳转
    location.assign('要跳转的页面地址');
    location.replace('要跳转的页面地址');
    ```

  - assign是会生成一条历史记录，而replace是不会生成历史记录

- 转换地址中的中文

  ```js
  var str = decodeURIComponent(页面地址);
  console.log(str);//地址中的中文可以正常显示
  ```

#### history

- 概念：也是window对象的一个属性，本质上也是一个原生对象，负责页面的前进和后退功能

- 常用函数

  - go(数字):根据数字来实现前进或后退的功能，数字为正，则表示前进指定页数。为负则表示后退指定页数

  - forward():前进一页

  - back():后退一页

    ```js
    1.前进一页history.go(1);
    history.forward;
    2. 后退一页history.go(-1);
    history.back();
    例子：
        <button onclick="history.forward()">前进一步</button>
    <button onclick="history.go(2)">前进两步</button>
    <button onclick="history.back();">后退一步</button>
    ```

#### navigator

- 概念：navigator是作为window的一个属性，本身也是一个原生对象。该对象包含了浏览器版本的相关信息。

- 常用属性

  - userAgent:获取当前浏览器的版本信息

    ```js
    console.log(navigator.userAgent);
    ```

#### screen

- 概念：保存了关于屏幕方面的信息

  ```js
  console.log(screen);
  ```

### 定时器

#### 概念

- JavaScript能够实现在一段时间之后执行指定的代码。
- 根据是否重复执行分为延时定时器以及间隔定时器。
- JavaScript中使用特定的函数来实现定时器功能

#### 延时定时器

- 概念：在指定一段时间之后执行一次代码，执行之后定时器结束。JavaScript使用`setTimeout`来指定延时定时器

- 语法

  ```js
  setTimeout(function(){    延时后要执行的代码},延时时间);例子：两秒后输出自拍setTimeout(function(){    alert('自拍');},2000)
  ```

  - 延时时间以毫秒为单位。一秒=1000毫秒。

- 暂停延时定时器

  - clearTimeout

    ```js
    clearTimeout(定时器的标识符)
    ```

    - 定时器的标识符类似于每一个定时器的id，由`setTimeout`的返回值来提供

      ```js
      例子：暂停定时器
      var timer = setTimeout(function(){    
          alert('自拍');},2000) ;
      暂停
      clearTimeout(timer);
      ```

#### 间隔定时器

- 概念：`每隔一段时间后`就会执行一次 指定的代码。

- 语法

  ```js
  setInterval(function(){
  每隔一段时间都会执行的代码
  },间隔时间);
  例子：每隔2s输出数据
  setInterval(function(){
  console.log(“1”)
  },2000);
  ```

```js
  - 间隔时间一样以毫秒为单位- 暂停间隔定时器  
      - clearInterval    
 clearInterval(间隔定时器的标识符)；    
 例子：    
 var timer = setInterval(function(){       
     console.log("1")   
 },2000);    
//暂停   
clearInterval(timer);
```

#### 定时器应用

- 实时显示时间

  ```js
  function getTime(str, date) {    
      var now = date;    
      str = str.replaceAll(/YYYY/g, now.getFullYear());    
      str = str.replaceAll(/MM/g, now.getMonth() + 1);    
      str = str.replaceAll(/DD/g, now.getDate());    
      str = str.replaceAll(/HH/g, now.getHours());    
      str = str.replaceAll(/mm/g, now.getMinutes());    
      str = str.replaceAll(/SS/g, now.getSeconds());    
      return str;
  }
  var str = getTime("YYYY/MM/DD HHSS",new Date());
  document.write(str);
  //间隔
  setInterval(function(){    location.reload();},1000);
  ```

# DOM

## 目录

- 获取HTML标签
  - document.querySelector & document.querySelectorAll
- 修改HTML标签内容
  - innerHTML
  - innerText
  - value
- 修改HTML标签的属性
  - setAttribute()
  - getAttribute()
- 添加标签
  - document.createElement
  - appendChild
- 删除标签
  - removeChild
- 常见操作流程
  - 如何修改一个HTML标签的内容
  - 如何添加标签到body中
  - 如何删除某个标签里的子标签
  - 如何获取多个标签并批量操作

![image-20210912192229209](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912192229209.png)

## DOM

### dom 概念

- 背景：通过HTML+css只能实现一个静态页面，即没有任何的数据交互，比如数据切换，登录、注册等功能实现。这些功能可以通过JavaScript的dom技术来实现

- 概念：DOM-document object model-文档对象模型。JavaScript会把页面的所有标签整合成一个document对象，document对象里面包含了一系列的api可以用来操作页面上的所有标签。比如对HTML标签的CRUD(增删查改)以及修改css、添加用户交互等操作。

- 每个页面都内置了一个document对象

  ```js
  console.log(document);
  ```

- 在JavaScript中，每个页面上已存在的标签，通过dom api获取之后，会以一个对象的方式存在。

### DOM树

![1550731974575](E:\qiand\07-10 JavaScript网页编程\02-WebAPI编程资料\Web APIs-day01\4-笔记\images\1550731974575.png)

DOM树 又称为文档树模型，把文档映射成树形结构，通过节点对象对其处理，处理的结果可以加入到当前的页面。

- 文档：一个页面就是一个文档，DOM中使用document表示
- 节点：网页中的所有内容，在文档树中都是节点（标签、属性、文本、注释等），使用node表示
- 标签节点：网页中的所有标签，通常称为元素节点，又简称为“元素”，使用element表示



### document对象

- 常用属性

  - **body**: 快捷获取页面的body标签
  - **documentElement**:快捷获取页面`<html>`标签
  - title:获取页面的标题文本
  - URL:获取页面的完整地址

  ```js
  console.log(document.body);
  console.log(document.documentElement);
  console.log(document.title);
  console.log(document.URL);
  ```

- api

  - 获取指定HTML标签
    - querySelector
    - querySelectorAll
  - 获取/设置 指定HTML标签的某个属性
    - setAttribute
    - getAttribute
  - 添加HTML标签
    - createElement
    - appenChild
  - 删除
    - removeChild

### DOM基础操作

#### 根据ID获取

```js
语法：document.getElementById(id)
作用：根据ID获取元素对象
参数：id值，区分大小写的字符串
返回值：元素对象 或 null
```

#### 根据标签名获取元素

语法：document.getElementsByTagName('标签名') 或者 element.getElementsByTagName('标签名') 
作用：根据标签名获取元素对象
参数：标签名
返回值：元素对象集合（伪数组，数组元素是元素对象）

#### H5新增获取元素方式

![image-20210912190137911](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912190137911.png)

#### 最新获取HTML标签

- `querySelector`:获取一个标签

  - 通过css选择器来获取标签

  ```js
  var 标签变量名 = document.querySelector("css选择器");
  例子：
  1. 获取页面上id为box的标签
  var elem = document.querySelector("#box");
  2. 获取页面上class为item的第一个标签
  var elem = document.querySelector(".item");
  3. 获取页面上的第一个div标签
  var elem = document.querySelector("div");
  4. 获取id为box的第一个子标签
  var elem = document.querySelector("#box :first-child");
  ```

- `querySelectorAll`：获取满足条件的所有标签

  - 通过css选择器来获取标签
  - 返回的是包含找到所有标签的NodeList集合(类数组对象)。那怕没有找到数据，都会返回NodeList集合

  ```js
  var 标签变量名 = document.querySelectorAll("css选择器");
  例子：
  1. 获取所有class为item 的标签
  var elems = document.querySelectorAll(".item");
  2. 获取所有的button标签
  var elems = document.querySelectorAll("button");
  ```

  - NodeList 可以像数组一样使用for以及forEach来完成遍历，但是不是使用数组的其他api，比如filter、map、join等。

  ```js
  例子：HTML：
      <button >更改图片</button>
  <button onclick="randomImg()">随机图片</button>
  JavaScript：
  //获取所有的button标签
  var buttons = document.querySelectorAll("button");
  //输出buttons里的每个button标签
  //1. 
  forfor(var i=0;i<buttons.length;i++){   
      console.log(buttons[i]);}
  //2. 
  forEachbuttons.forEach(b=>{    console.log(b);});
  ```

#### 获取/设置标签的内容

- 流程

  - 先通过`querySelector\All`获取要操作的标签
  - 再通过`innerHTML、innerText、value`来进行操作

- innerHTML

  - 获取标签内部的所有内容，包括子标签代码本身。

    ```js
    1. 获取标签变量名.innerHTML2. 设置标签变量名.innerHTML = 新内容;
    ```

    - 设置innerHTML时，会将所有的旧子标签给覆盖掉。

- innerText

  - 获取或设置标签的内容

    ```js
    1. 获取标签变量名.innerText2. 设置标签变量名.innerText = 新内容;
    ```

    - innerText获取时会获取所有子标签的文本内容
    - 设置innerText时，只会原样输出，即纯文本输出，不会将文本转为标签

- value

  - 针对表单元素，比如input、select等

    ```js
    1. 获取标签变量名.value2. 设置标签变量名.value = 新内容;
    ```

- innerHTML、innerText、value的区别

  - value是针对input等表单元素，而innerHTML和innerText是针对`<标签名></标签名>`.
  - innerHTML 获取的是标签内部的所有代码文本，而innerText是获取的是标签里面的 文本。
  - 设置innerHTML时，如果有HTML代码，在页面会解析成真正的HTML标签，而innerText直接作为纯文本显示在页面上

- 应用

  - value是用于表单元素

  - 如果设置标签里的文本用innerText，如果要设置标签内部的子标签，用innerHTML

    ```js
    html:
    <p id="msg"></p>
    js; 
    var p = ocument.querySelector("#msg");
    1. 设置纯文本
    p.innerText = "id1.jpg";
    2. 设置内部的子标签
    p.innerHTML = '<span >1.jpg</span>';
    ```

#### 获取/设置HTML标签的属性

- 获取

  - getAttribute

    ```js
    1. 获取标签 
    var 标签变量名 = document.querySelector("css选择器");
    2. 通过标签来使用api
    var 变量 =标签变量名.getAttribute('属性名');
    例子： 获取图片的地址并输出
        <img src="img/id1.jpg" alt="" id="img">
        var img = document.querySelector("#img");
          var  src = img.getAttribute('src');
          console.log(src);
    ```

- 设置

  - setAttribute

    ```js
    1. 获取标签 
    var 标签变量名 = document.querySelector("css选择器");
    2. 通过标签来使用api
    var 变量 =标签变量名.setAttribute('属性名',"属性值");
    例子： 设置图片的地址为id2.jpg
    <img src="img/id1.jpg" alt="" id="img">
      var img = document.querySelector("#img");
    var  src = img.setAttribute('src',"id2.jpg");
    ```

#### 添加标签

- 相关api

  - document.createElement
  - appendChild
  - insertBefore

- 流程

  - 先用`document.createElement`再程序中新建一个标签
  - 再用`appendChild或insertBefore`将新标签作为页面已存在标签的子标签放置在页面上

- 新建一个标签

  ```js
  var 新标签变量名 = document.createElement("标签名");
  例子：新建一个div标签
  var newDiv= document.createElement("div");
  ```

  - 通过标签名来告诉程序要新建哪一种标签

- 放置在页面上:appendChild

  ```js
  父标签变量名.appendChild(新标签变量名);
  例子：将新的div作为body标签的最后一个子标签放置在页面上
  var newDiv= document.createElement("div");
  document.body.apendChild(newDiv);
  ```

  - 父标签必须是页面已存在的标签

- 放置在页面上：insertBefore

  ```js
  父标签变量名.insertBefore(新标签,兄弟标签);把新标签作为其父标签的子标签并放在指定兄弟标签之前例如：
  var father = document.querySelector('#box');
  var brother = document.querySelector('#box img:nth-child(2)');
  father.insertBefore(newImg,brother);
  ```

- 例子(appendChild)：新建一个img标签，地址为`img/id1.jpg`,把新标签作为id为box的标签的最后一个子标签

  ```js
  1. 新建
  var newImg = document.createElement("img");
  2. 设置新标签newImg.setAttribute('src',"img/id1.jpg");
  3. 显示在页面中var father = document.querySelector("#box");
  father.appendChild(newImg);
  ```

- 例子(insertBefore):在3张图片中插入一张图片

  ```js
  html:
  <div id="box">        
      <img src="img/id1.jpg" alt="">       
          <img src="img/id3.jpg" alt="">        
              <img src="img/id4.jpg" alt="">
   </div>
  //在id3之前插入id2
  // 新建一个img
  var newImg = document.createElement("img");
  // 设置新标签的样式或属性
  newImg.setAttribute('src','img/id2.jpg');
  // 3 找到父和兄弟
  var father = document.querySelector('#box');
  var brother = document.querySelector('#box img:nth-child(2)');
  father.insertBefore(newImg,brother);
  ```

#### 删除标签

- 流程

  - 找到需要删除的标签及其父标签
  - 其父标签调用`removeChild`完成删除

- 相关 api

  - removeChild

    ```js
    父标签变量名.removeChild(待删除的标签)
    ```

- 例子：删除id为box标签下的第一个img子标签

  ```js
  1. 待删除的标签
  var img = document.querySelector("#box img");
  2. 其父标签
  var div = document.querySelector("#box");
  3. 删除
  div.removeChild(img);
  ```

- 扩展：批量删除

  - 先用queryselectorAll 找到需要删除的标签，利用forEach遍历依次依次调用`removeChild`进行删除

  ```js
  var imgs = document.querySelectorAll("#box img");
  var box = document.querySelectorAll("#box");
  imgs.forEach(img=>{    box.removeChild(img);});
  ```

#### 扩展

##### 设置点击代码

```js
<button onclick="demo(this);">点击一下，有惊喜</button>
function demo(elem){    
    elem指的就是被点击的标签本身，即button    
    alert('惊不惊喜意不意外');   
    alert('你以为一个弹框就结束了？？？');
}
```

- onclick 可以运用在任意标签上
- 如果是在标签里通过`onclick`来设置点击代码，那么onclick指定的函数可以传递实际参数`this`，在函数体中通过形式参数来接收，this指的是`被点击的标签本身`。

#### eval

- 概念：用于将一个字符串作为JavaScript代码并执行，最终返回执行的结果

- 语法

  ```js
  var 变量名  = eval(字符串);//例子：计算1+2 
  var result = eval('1+2');
  console.log(result);//3例子：弹框显示hello 
  eval('alert("hello")');
  ```

## DOM进阶

### 目录

- 修改css
  - getComputedStyle()
- 获取父、兄弟、子标签
  - firstElementChild：第一个子HTML标签
  - lastElementChild：最后一个子HTML标签
  - previousElementSibling:前一个兄弟HTML标签
  - nextElementSibling：下一个兄弟HTML标签
  - children：获取所有的直接子标签
  - parentElement：获取其父标签
- 事件
- 正则表达式

### 修改CSS

#### 获取某标签的指定css

- 通过`window.getComputedStyle()`来获取某个标签的css属性

  ```js
  var css对象名 = getComputedStyle(标签变量名,null);获取指定css属性值： css对象名.具体css属性名
  ```

  - 获取到的css对象包含了该标签所有css属性的取值

- 例子

  ```js
  1. 获取id为box的标签的背景颜色和文本颜色
  var box = document.querySelector('#box');
  2. 获取css对象
  var style = getComputedStyle(box,null);
  3. 获取指定css属性
  console.log(style.color);
  console.log(style.backgroundColor);
  ```

#### 修改标签的指定css

```js
1. 获取标签
2. 利用style来修改css标签变量名.style.css属性名= 新css属性值
例子：将id为box的标签的文本颜色改为红色，背景颜色改为绿色
var box = document.querySelector("#box");
box.style.color = "red";
box.style.backgroundColor ="green";
box.style.width = "200px";
box.style.cssFloat = "left";
```

- 在JavaScript中，float是一个关键字。如果要修改float css，就使用`cssFloat`
- 如果一个css属性由多个单词构成，那么在js中每个单词之间的-去掉，并后面的单词首字母大写。比如`backgroundColor`

#### JavaScript中的动画

- 原理：`不间断的修改标签的css属性`来达到动画效果。具体来讲配合间隔定时器，每次都去改变标签的css属性，比如margin、top可以实现移动动画，改变opacity可以实现淡入淡出动画。

- 例子：实现简单的向下的移动动画

  - 每次先获取旧的`margin-top`并转为数字，然后再+=3px(自己确定几px)。
  - 利用间隔定时器不断执行。基本流畅（1秒执行30次），纵享丝滑（1秒60次）

  ```js
  <div id="result"></div>
  setInterval(() => {    
      var div = document.querySelector("#result");    
      //实现向下移动动画   
      //先获取div旧的 margin-top，在基础之上进行修改    
      var style = getComputedStyle(div,null);    
      //获取旧的top并提取数值部分，去掉px字符    
      var oldTop = parseInt(style.marginTop);    
      //修改css   
      div.style.marginTop = oldTop -2+"px";}, 16.7);
  ```

#### 获取父、子、兄弟标签

- firstElementChild：第一个子HTML标签

  ```js
  标签变量名.firstElementChild;
  ```

- lastElementChild：最后一个子HTML标签

  ```js
  标签变量名.lastElementChild;
  ```

- previousElementSibling:前一个兄弟HTML标签

  ```js
  标签变量名.previousElementSibling
  ```

- nextElementSibling：下一个兄弟HTML标签

  ```js
  标签变量名.nextElementSibling
  ```

- children：获取所有的直接子标签

  ```js
  标签变量名.children
  ```

- parentElement：获取其父标签

  ```js
  标签变量名.parentElement
  ```

![image-20210912190518475](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912190518475.png)



## DOM事件

### 目录

- 事件分类
  - 基础
    - **load\***：资源加载完毕后执行，一般用于页面加载和图片加载
    - **resize\***：页面尺寸发生变化时执行
  - 鼠标
    - **mousemove\***:鼠标在指定标签中移动
    - mouseenter
    - mouseleave
    - mousewheel
    - DOMMouseWheel
  - 键盘
    - keydown
    - **keyup\***
    - keypress
  - 焦点
    - **focus\***
    - **blur\***
  - 文本
    - **change\***
  - 移动端
    - touchstart
    - touchend
    - touchmove
- 事件流*
  - 冒泡
  - 捕获
- **事件执行阶段\***
- 事件处理程序
  - DOM0级
  - DOM2级(使用)
    - addEventListener
    - removeEventListener
- event**对象**
- **事件委托\***

### 事件基础及分类

#### 事件概念

- 事件指用户跟页面的所有交互动作的统称。比如点击事件、鼠标移动事件、输入框获取焦点事件、失去焦点事件、键盘输入等事件。
- 目的：能够在用户触发某个事件时能够执行指定的JavaScript代码。

#### 事件分类

- 基础

  - **load\***：资源加载完毕后执行，一般用于页面加载和图片加载

    ```js
    //利用js指定load
    var img = document.querySelector(‘img’);
    //指定load事件
    img.onload = function(){
    
    alert('图片加载完成');
    }
    ```

~~~js
//页面加载完执行
window.onload = function(){    
//页面加载完成后触发。    
alert('页面上的所有标签都以加载完毕，可以用js来获取标签并进行操作')    
var img = document.querySelector('img');    
console.log(img);
}
```
~~~

- **resize\***：页面尺寸发生变化时执行,用window对象来指定事件

  ```js
  window.onresize = function(){     console.log('页面尺寸发生变化');}
  ```

- 鼠标

  - **mousemove\***:鼠标在指定标签中移动

  - mouseenter：鼠标移动到标签里触发

  - mouseleave：鼠标移出标签时触发

  - mousewheel：滚动滚轮时触发，部分浏览器支持

  - DOMMouseScroll：滚动滚轮时触发，部分浏览器支持

  - click

  - dblclick：双击

    ```js
    var div = document.querySelector('div');
    //鼠标在div里移动时不断触发
    div.onmousemove = function(){   
        console.log('鼠标在div里移动')}
    //鼠标在body里移动时不断触发
    document.body.onmousemove = function(){    
        console.log('鼠标在body里移动')}
    //mouseenter  
    mouseleavediv.onmouseenter = function(){    
        console.log('进去了');
    }
    div.onmouseleave = function(){   
        console.log('出去了');
    }
    //谷歌滚动
    document.body.onmousewheel = function(){    
        console.log('滚动吧');}
    //兼容火狐
    document.body.addEventListener('DOMMouseScroll',function(){    
        console.log('滚动吧')
    });
    //双击div
    div.ondblclick = function(){    
        console.log("div被双击了，666")
    }
    ```

- 常见的鼠标事件

- ![image-20210912190414759](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912190414759.png)

- 键盘

  - keydown:按下键帽时触发。如果说该是给input设置的，获取的是input修改之前的 数据

  - **keyup\***：松开键帽时触发。如果说该是给input设置的，获取的是input修改之后的 数据

  - keypress：即将释放键帽时触发。如果说该是给input设置的，获取的是input修改之前的 数据

    ```js
    var input = document.querySelector("input");
    //keydown
    input.onkeydown = function(){
        console.log('keydown',input.value);
    }
    //keypress
    input.onkeypress = function(){
        console.log('keypress',input.value);
    }
    //keyup
    input.onkeyup= function(){
        console.log('keyup',input.value);
    }
    ```

  ```js
  <script>
          // 常用的键盘事件
          //1. keyup 按键弹起的时候触发 
          document.addEventListener('keyup', function() {
              console.log('我弹起了');
          })
  
          //3. keypress 按键按下的时候触发  不能识别功能键 比如 ctrl shift 左右箭头啊
          document.addEventListener('keypress', function() {
                  console.log('我按下了press');
          })
          //2. keydown 按键按下的时候触发  能识别功能键 比如 ctrl shift 左右箭头啊
          document.addEventListener('keydown', function() {
                  console.log('我按下了down');
          })
          // 4. 三个事件的执行顺序  keydown -- keypress -- keyup
      </script>
  ```

  ![image-20210912192111940](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912192111940.png)

  ##### **使用keyCode属性判断用户按下哪个键**

  ```js
   <script>
          // 键盘事件对象中的keyCode属性可以得到相应键的ASCII码值
          document.addEventListener('keyup', function(e) {
              console.log('up:' + e.keyCode);
              // 我们可以利用keycode返回的ASCII码值来判断用户按下了那个键
              if (e.keyCode === 65) {
                  alert('您按下的a键');
              } else {
                  alert('您没有按下a键')
              }
          })
          document.addEventListener('keypress', function(e) {
              // console.log(e);
              console.log('press:' + e.keyCode);
          })
      </script>
  ```

  

- 

- 焦点

  - **focus\***:当某个标签获取鼠标焦点 时触发。一般是给input使用。

  - **blur\***：当某个标签失去鼠标焦点 时触发。一般是给input使用。

    ```js
    <style>
        input{
            outline: none;
            transition: all .5s;
            border : 1px solid #ccc;
            box-shadow : 0 0  10px #ccc;
        }
        .active{
            border : 1px solid green;
            box-shadow : 0 0  10px green;
        }
        </style>
    用户名：<input type="text" id="username">密码：<input type="text">
        <script>
    var userinput = document.querySelector("#username");
    userinput.onfocus  =function(){
        userinput.setAttribute('class','active');
    }
    userinput.onblur  =function(){
        userinput.setAttribute('class','');
    }
    </script>
    ```

- 文本

  - **change\***:当下拉列表选项切换时触发，一般用于获取实时的下拉菜单的选中选项

    ```js
    <select name="" id="nation">
            <option value="china">中国</option>
            <option value="canada">加拿大</option>
            <option value="usa">美国</option>
    </select>
    <script>
    var select = document.querySelector('#nation');
    select.onchange  = function(){
        //输出选中选项的value值
        console.log(select.value);
    }
    </script>
    ```

- 移动端
  - touchstart
  - touchend
  - touchmove

### 事件流

#### 背景

- 当点击一个子标签时，其父标签是否也算被点击了？
- 90年代，当时w3c处理该问题时，有两种不同的解决方案。以ie为首的浏览器厂商提出方案：都算点击，但是事件的触发顺序是由具体的子标签开始，一直到到祖先标签。而以网景公司为首的则认为都算点击。但是应该从祖先标签开始，一直到真正被点击的具体子标签。w3c最终都采用了。这两种决定事件在触发时的执行顺序的方案统称为两种事件流方案。

#### 概念

- 事件流是指的当事件触发时，事件在父子标签之间触发的顺序。
- 按照流向不同，分为了两种事件流：冒泡和捕获。

#### 冒泡

- 指当事件触发时，应该是具体触发事件的子标签先执行事件，再父标签执行该事件，一直到祖先标签执行后，结束。 子->父

- 完整路线：具体的子标签->父标签->爷爷标签->body->html->document->window

  ```js
  <ul>
          <li>
              <p>
                  <span>这是一个span标签</span>
                  <a href="#">百度一下</a>
                  <span>这是另一个span标签</span>
              </p>
          </li>
  </ul>
  ```

  - 点击a标签： a->p->li->ul->body->html->document->window

#### 捕获

- 指当事件触发时，应该是祖先标签先执行事件，再一直到具体触发事件的子标签执行后，结束。 父->子

  ```js
   <ul>
          <li>
              <p>
                  <span>这是一个span标签</span>
                  <a href="#">百度一下</a>
                  <span>这是另一个span标签</span>
              </p>
          </li>
  </ul>
  ```

  - 点击a标签：window->document->html->body->ul->li->p->a

### 事件处理程序

#### 概念

- 当某个事件被触发时要执行的函数本身就是事件处理程序，即要执行的js代码。

#### 分类

- DOM0级

  - on+事件名.比如onclick

  ```js
  例子：给body添加一个dom0级处理程序
  1. 标签上
  <body onclick="要执行的代码"></body>
  2. 通过js
  document.body.onclick = function(){
      事件处理程序代码
  }
  ```

  - dom0级只支持冒泡，不支持捕获。

- DOM2级

  - 添加事件处理程序

    ```js
    标签变量名.addEventListener("事件名",事件处理程序,是否捕获处理);
    例子：给body设置点击事件，输出hello
    document.body.addEventListener("click",handler,true);//捕获处理，
    function handler(){
        console.log('hello');
    }
    ```

    - 如果为false，则表示冒泡处理，false为默认值。

  - 删除事件处理程序

    ```js
    标签变量名.removeEventListener("事件名",事件处理程序,是否捕获处理);
    例子：给body删除设置的点击事件
    document.body.removeEventListener("click",handler,true);//捕获处理，
    ```

![image-20210912191531084](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912191531084.png)

### 事件执行阶段（一个事件的生命周期）

#### 概念

- 事件执行阶段指的是目前的浏览器中一个事件触发的完整执行流程
- 一个完整的事件执行阶段分为3个部分，也称为三个阶段

#### 流程

- 第一阶段(捕获阶段)：一个事件触发时会执行一次捕获流程。即由祖先标签一直执行，到具体的子标签结束。
- 第二阶段(事件目标):包含了第一阶段的结束，也包含了第三阶段的开始，处于这个阶段，即事件在真正触发事件的子标签执行。
- 第三阶段(冒泡阶段)。即由具体的子标签一直到祖先标签。

### event对象

#### 概念

- 在触发事件的时候，我们往往需要知道事件发生在页面的那个位置，触发事件的是哪个标签等相关信息。
- JavaScript在每次事件触发时会自动创建一个专属的event对象，该对象里包含了该事件的相关信息。该对象会直接作为实际参数传入事件处理程序中，开发人员则需要定义形式参数接收，即可使用。

#### 使用

- 在事件处理程序中定义形式参数来接收：

  ```js
  document.body.addEventListener('click',function(event){   
      console.log(event);
  })
  ```

#### event对象常用属性或函数

- **target**:真正触发事件的具体子标签，在事件执行阶段中不会改变
- currentTarget:当前正在冒泡或捕获阶段的触发标签，这个会随着事件执行阶段的流程而发生改变。
- **clientX**:触发事件时鼠标相对于页面左上角的x坐标
- **clientY**:触发事件时鼠标相对于页面左上角的Y坐标
- offsetX:触发事件时鼠标相对于标签的x轴偏移量
- offsetY:触发事件时鼠标相对于标签的Y轴偏移量
- pageX;触发事件时鼠标相对于页面左上角的x坐标
- pageY:触发事件时鼠标相对于页面左上角的Y坐标，包含了页面滚动条的高度
- **preventDefault**():取消标签的默认行为。一般针对于超链接和表单元素。

### 事件委托

#### 背景

- 对于一个复杂的页面，可能会有大量的标签需要设置事件代码，比如点击、焦点等，那么js中就会有大量的事件代码，造成js代码量太大。优化代码量—-事件委托

#### 概念

- 是指运用了事件冒泡以及event对象的`target`属性来达到简化事件代码的一个编程技巧。

#### 使用

- 给需要设置事件的标签其父标签或祖先标签设置事件代码，利用`event.target`来判断当前真正的触发事件标签，再执行对应的事件处理程序的代码。

#### 作用

- 减少事件的定义代码
- 统一管理事件代码，方便维护

#### 例子

```js
html:
 <div>
        <img src="img/id1.jpg" alt="" class="good-img">
        <p class="good-title">最爱干花花瓶</p>
        <p class="good-price">￥998</p>
 </div>
javascript:
直接给父标签设置事件，内部通过e.target具体是哪个标签执行事件
document.querySelector('div').addEventListener('click',function(e){
    var classname = e.target.getAttribute('class');
    switch (classname) {
        case "good-img":
            console.log('img被点击了')
            break;
        case "good-price":
            console.log('第二个p被点击了')
            break;
        case "good-title":
            console.log('第一个p被点击了')
            break;
    }   
})
```

### 事件对象的属性和方法

![image-20210912191753484](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912191753484.png)

##### e.target 和 this 的区别

-  this 是事件绑定的元素（绑定这个事件处理函数的元素） 。

-  e.target 是事件触发的元素。

> ```
> 常情况下terget 和 this是一致的，
> 但有一种情况不同，那就是在事件冒泡时（父子元素有相同事件，单击子元素，父元素的事件处理函数也会被触发执行），
> 	这时候this指向的是父元素，因为它是绑定事件的元素对象，
> 	而target指向的是子元素，因为他是触发事件的那个具体元素对象。
> ```

```js
    <div>123</div>
    <script>
        var div = document.querySelector('div');
        div.addEventListener('click', function(e) {
            // e.target 和 this指向的都是div
            console.log(e.target);
            console.log(this);

        });
    </script>
```

事件冒泡下的e.target和this

```js
    <ul>
        <li>abc</li>
        <li>abc</li>
        <li>abc</li>
    </ul>
    <script>
        var ul = document.querySelector('ul');
        ul.addEventListener('click', function(e) {
              // 我们给ul 绑定了事件  那么this 就指向ul  
              console.log(this); // ul

              // e.target 触发了事件的对象 我们点击的是li e.target 指向的就是li
              console.log(e.target); // li
        });
    </script>
```



### 删除事件（解绑事件）

![image-20210912191041631](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912191041631.png)

```js
<div>1</div>
    <div>2</div>
    <div>3</div>
    <script>
        var divs = document.querySelectorAll('div');
        divs[0].onclick = function() {
            alert(11);
            // 1. 传统方式删除事件
            divs[0].onclick = null;
        }
        // 2. removeEventListener 删除事件
        divs[1].addEventListener('click', fn) // 里面的fn 不需要调用加小括号
        function fn() {
            alert(22);
            divs[1].removeEventListener('click', fn);
        }
        // 3. detachEvent
        divs[2].attachEvent('onclick', fn1);

        function fn1() {
            alert(33);
            divs[2].detachEvent('onclick', fn1);
        }
    </script>
```

##### 删除事件兼容性解决方案

![image-20210912191138926](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912191138926.png)



#### 练习

```
事件基础1. 书写一个含有两个输入框的页面。 进行书写格式验证。用户名是6位数字，密码是6~10的字符。可以利用焦点事件或keyup事件添加边框给用户及时的反馈
```

## 正则表达式

#### 目录

- 基本使用
- 正则表达式函数
  - **test**
  - exec
- 正则表达式语法
  - 基础语法
  - 进阶语法
- 正则表达式模式
- 正则表达式在字符串中的应用
  - split
  - replace
  - match

### 正则表达式概念

#### 概念

- 是指一种特殊的字符串，本身是按照一定语法进行书写。能够作为指定的要求去验证其他的数据（字符串）是否满足。即正则表达式是用来描述数据要满足的要求。

#### 作用

- 快速验证数据是否满足指定的条件

#### 使用流程

- 分析数据要满足的要求，并根据要求书写出对应的正则表达式。比如说手机号必须是11位数字。
- 再调用正则表达式的`test或exec`函数来判断数据是否满足正则表达式。

#### 定义语法

```
var 正则表达式变量名 = /正则表达式语法/;//使用正则表达式变量名.test(要测试的数据);//返回布尔型
```

#### 正则表达式的特点

1. 灵活性、逻辑性和功能性非常的强。
2. 可以迅速地用极简单的方式达到字符串的复杂控制。
3. 对于刚接触的人来说，比较晦涩难懂。比如：^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$
4. 实际开发,一般都是直接复制写好的正则表达式. 但是要求会使用正则表达式并且根据实际情况修改正则表达式.   比如用户名:   /^[a-z0-9_-]{3,16}$/

### 正则表达式语法

#### 基础语法

- ```js
  []:匹配组，用于匹配[]中的任意其中一个
  [0-9]:匹配任意一个数字
  [0-9][0-9]:匹配连续的两个数字
  [a-z]:匹配任意一个小写字母
  [A-Z]:匹配任意一个大写字母
  [a-zA-Z]:匹配任意一个字母
  [0-9a-zA-Z]:匹配任意一个数字或字母
  {m,n}:前面的组匹配指定的次数
  {1,4}:表示前面的组长度至少为1，最多为4
  {3}:表示前面的组长度为3
  {1,}:表示前面的组长度至少为1
  {,5}:表示前面的组长度最多为5
  ^：表示以….开头
  $：表示以….结束
  如果^和$同时使用，那么就意味着判断的是整个数据。
  ```

#### 进阶语法

- `\w`：等同于`[0-9a-zA-Z_]`
- `\d`: 等同于`[0-9]`
- `+`: 等同于`{1,}`,表示至少一次
- `?`：等同于`{0,1}`，表示最多1次
- `*`：等同于`{0,}`,任意次数

#### 正则表达式 模式

- 概念：正则表达式面对不同的 情况可以采用不同的模式，比如是否考虑大小写、是否全局检索等。

- 分类

  - u: 只会匹配最近的满足的数据，默认。
  - g：全局匹配，会找到满足条件的所有数据
  - i：不区分大小写

- 设置正则表达式模式

  ```js
  var reg = /正则表达式/模式;
  //检索字符中的所有手机号-全局模式
  var phones  ="13899999999 13799999999 13699999999";
  var reg = /[0-9]{11}/g;
  ```

#### 正则表达式在字符串中的应用

- match

  - 用于判断并返回字符串中满足正则表达式的数据.

    ```js
    语法： 字符串.match(正则表达式);
    例子：
    var phones  ="13899999999 13799999999 13699999999";
    var datas = phones.match(/[0-9]{11}/g);
    console.log(datas);// ["13899999999", "13799999999", "13699999999"]
    ```

- split

  - split支持分隔符是一个正则表达式

    ```js
    var str = "张三$李四**王五####赵六";
    var reg = /[$*#]+/;
    var arr = str.split(reg);
    console.log(arr);//["张三", "李四", "王五", "赵六"]
    ```

- replace

  - 支持旧的字符是正则表达式,完成复杂的字符替换

    ```js
    var str = "张三1李四2王五aaa赵六000田七G王霸";
    //数字和字母替换成空格
    var reg = /[0-9a-zA-Z]+/g;
    var result = str.replace(reg,' ');
    console.log(result);//张三 李四 王五 赵六 田七 王霸
    ```

#### startsWith() 和 endsWith()

- startsWith()：表示参数字符串是否在原字符串的头部，返回布尔值

- endsWith()：表示参数字符串是否在原字符串的尾部，返回布尔值

  ```js
  let str = 'Hello world!';
  str.startsWith('Hello') // true 
  str.endsWith('!')       // true
  
  ```

  

##### 练习

```js
1. 匹配QQ号： 5~11位，全数字
2. 匹配手机号：11位数字，第一位必须是1，第二位是3-9，其他都是数字
3. 匹配密码：6~16位，以大写字母开头，只包含数字和字母
```

## JQuery

### 目录

- JQuery基础使用
  - 下载及引入
- JQuery 基本操作
  - 获取HTML标签: `$("css选择器")`
  - 修改HTML标签内容 :`val()` 、 `html()`、 `text()`
  - 获取/修改HTML标签属性:`prop()`、`removeProp()`
  - 添加:`append()` 、 `before()`
  - 删除:`remove()`
  - 修改css :`css()`
- jQuery 进阶
  - 获取子标签: `find()`、 `children()`
  - 获取父标签：`parent()` 、 `parents()`
  - 获取兄弟标签: `prev()`、 `next()`
- jQuery HTML 标签 数组
  - 获取第一个或最后一个 : `first()` 、 `last()`
  - 获取第i个: `eq(i)`
  - 对数组进行遍历:`each()`
- jQuery 事件
  - `on`
- jQuery 动画
  - 快捷动画: `fadeIn()`、 `fadeOut()` 、 `slideDown()` `slideUp()`
  - 自定义动画：`animate()`
- jQuery其他函数
  - 快捷隐藏/显示：`hide()`、 `show()`
  - 追加/删除指定class: `addClass()` 、 `removeClass()`

### jQuery 基础使用

#### 背景

- 原生DOM操作的不便之处：
  - 单词太多，太长
  - 遍历不方便
  - 操作不便：css 获取子、兄弟
  - 动画 需要自己写

#### 概念

- jQuery 是第三方的JavaScript函数库。本质上jQuery是一个js文件，里面写好了`大量的函数`，可以直接使用

#### 作用

- 用于优化 DOM 代码

#### 引入

- 下载jQueryjs文件，通过`<script>`引入到页面上。先引入jQuery，再使用里面的函数
- 版本
  - 目前国内最新的用的是3.5.1.国外是4.x，jQuery从2.0开始，就不再支持ie低版本(8)。
  - jQuery是前端页面交互的过渡东西，后期会切换到vue或React

#### 注意点

- 如果使用了jQuery，用jQuery操作的 标签对象就不能再使用原生的属性或函数。

- dom标签转为jQuery标签

  ```html
  var $变量名 = $(dom元素);
  ```

### jQuery 基础操作

#### 获取HTML标签

```js
$("css选择器")；
例子； 
1. 获取id为box的标签
$("#box");
2. 获取class为item的所有标签
$('.item');
3. 获取id为box下的所有奇数的p标签
$('#box p:nth-child(2n-1)');
```

- jquery会自动根据找到的数量来判断是否转为数组。

#### 修改HTML标签的内容

- html()

  ```js
  1. 获取jQuery标签
  2. 
  获取：$变量名.html()
  设置：$变量名.html(新内容);
  例子： 
  var $box = $('#box');
  获取： var text= $box.html();
  设置： $box.html('<h1>新内容</h1>');
  ```

- text()

  ```html
  1. 获取jQuery标签
  2. 
  获取：$变量名.text()
  设置：$变量名.text(新内容);
  例子：
  例子： 
  var $box = $('#box');
  获取： var text= $box.text();
  设置： $box.text('<h1>新内容</h1>');
  ```

- val()

  ```js
  1. 获取jQuery标签
  2. 
  获取：$变量名.val()
  设置：$变量名.val(新内容);
  例子；
  var $input = $('#user');
  获取：var text = $input.val();//字符串
  设置： $input.val("234");
  ```

#### 修改HTML标签的属性

- prop()

  ```js
  获取: $变量名.prop('属性名');
  设置: $变量名.prop('属性名',"属性值");
  例子： 修改id为box的标签，class为box
  var $box  =$('#box');
  $box.prop('class','box');
  获取id属性
  var id = $box.prop('id');
  ```

- removeProp():删除某个属性

  ```js
  $变量名.removeProp('属性名');
  例子：删除id为box的标签的class属性
  $("#box").removeProp("class");
  ```

#### 添加HTML标签

- 追加：append()

  ```js
  $父标签变量名.append($新标签);
  1. 先新增标签
  var $newDiv = $('<div id="box"></div>');
  2. 设置新标签的属性、内容
  $newDiv.prop('id','box');
  3. 加入到父标签中并作为最后一个子标签
  $('body').append($newDiv);
  ```

- 插入: before()

  ```js
  $兄弟标签.before($新标签);
  例子：吧新的p标签插入到#box下的第一个子标签之前
  var $newP = $(`<p class='item'>第0个标签</p>`);
  var $brother =$('#box p:first-child');
  $brother.before($newP);
  ```

#### 删除HTML标签

- remove()

  ```js
  $待删除标签.remove();
  例子：删除所有class为item 的p标签
  $('.item').remove();
  ```

#### 修改css

- css()

  ```js
  获取： 
  $变量名.css("属性名")；
  设置单个css属性:
  $变量名.css('属性名','属性值');
  设置多个css属性
  $变量名.css({
      css属性名1: 属性值1,
      css属性名2: 属性值2,
      ...
      css属性名n: 属性值n
  });
  例子：
  1.修改p标签的文本颜色为红色
  $('.item:first-child').css('color','red');
  2.修改p标签的文本为红色，背景为黄绿色
  $('.item:last-child').css({
      color:'red',
      backgroundColor:'yellowgreen'
  })
  3.获取 #box的高度
  var height = $('#box').css('height');
  console.log(height);
  ```

#### Jquery获取子、父、兄弟标签

##### 获取父标签

- parent():找到某个标签的直接父标签

  ```js
  var $父标签变量名 = $变量名.parent();
  例子：找到id为box的其父标签
  var $father = $('#box').parent();
  ```

- parents():通过css选择器，找到满足要求的祖先元素

  ```js
  $祖先变量名 = $变量名.parents("css选择器");
  例子：找到id为span-demo的其id为box的祖先标签，
  $('#span-demo').parents('#box');
  ```

##### 获取兄弟标签

- prev():l找到其上一个兄弟标签

  ```js
  $变量名.prev();
  ```

- next():找到其下一个兄弟标签

  ```js
  $变量名.next();
  ```

- siblings():找到满足指定条件的兄弟标签

  - 通过css选择器

    ```js
    $变量名.siblings("css选择器");
    ```

  - 找到所有的兄弟标签(不包括自己)

    ```js
    $变量名.siblings();
    ```

#### 获取子标签

- children ():获取其标签的所有直接子标签

  ```js
  var childs = $变量名.children();
  例子：
  var $items = $("#box").children();
  console.log($items);
  ```

- find()：根据css选择器来查找符合条件的后代标签

  ```js
  var childs = $变量名.find("css选择器");
  例子：
  var $span = $('#box').find('#span-demo');
  console.log($span);
  ```

#### jQuery 遍历

##### each

- 用于jQuery标签的遍历

  ```js
  $变量名.each(function(index,elem){
      index是当前遍历元素的下标
      elem是指当前遍历的标签(原生DOM)
  })
  ```

##### eq

- 拿到遍历jQuery标签的指定下标的那个

  ```js
  $变量名.eq(下标);
  //遍历
  var $ps = $('#box p');
  for(var i=0;i<$ps.length;i++){
      console.log($ps.eq(i));
  }
  ```

##### first() & last()

- 拿到遍历数据的第一个和最后一个

  ```js
  $变量名.first() ;
  $变量名.last();
  等同于 
  $变量名.eq(0) 和 $变量名.eq($变量名.length-1)
  ```

##### index()

- 指拿到某个遍历数据在数组中的下标

  ```js
  $变量名.index();
  ```

#### Jquery 事件

##### on()

- 借助了事件委托给某个标签设置事件处理程序。事件处理程序中，可以用`$（this）`指代触发事件的jQuery标签

  ```js
  $祖先标签变量名.on('事件名','设置事件的标签css选择器',事件处理程序);
  例子：给id为box的标签设置点击事件
  $('body').on('click','#box',function(e){
      id为box 的标签发生点击事件时要执行的代码
  });
  例子2：点击p标签，显示对应的文本
  $('#box').on('click','p',function(){
      $(this):触发事件的标签,当前例子就指的是p标签
      alert($(this).text());
  });
  ```

#### jquery 动画

##### 快捷动画

- 淡入&淡出

  - fadeIn():淡入，支持动画持续时间，以毫秒为单位

  - fadeOut()：淡出，支持动画持续时间，以毫秒为单位

    ```js
    $变量名.fadeIn(动画持续时间)
    $变量名.fadeOut(动画持续时间)
    例子：
    $('div').fadeIn(2000);
    $('div').fadeOut(3000);
    ```

- 下滑上拉

  - slideDown():下滑,支持动画持续时间，以毫秒为单位

  - slideUp():上拉,支持动画持续时间，以毫秒为单位

    ```js
    $变量名.slideDown(动画持续时间)
    $变量名.slideUp(动画持续时间);
    例子：
    $('div').slideDown(3000)
    $('div').slideUp(3000);
    ```

##### 自定义动画

- animate():自定义动画。动画的持续时间以毫秒为单位

  ```js
  $变量名.animate({
      css属性名1:css属性值1,
      css属性名2:css属性值2,
      ...
      css属性名n:css属性值n
  },动画的持续时间);
  例子：2s内，div宽度为300px，高度为300px，并且向右移动300px
  $('div').animate({
      width:'300px',
      height:'300px',
      transform:"translateX(300px)"
  },2000)
  ```

##### 动画结束代码

- 在动画执行结束后执行指定的代码。可以用于快捷动画和自定义动画。

- 即动画函数调用时添加一个function实际参数作为动画结束后要执行的函数。

  ```js
  例子：在id为box的标签3s淡入后将标签文本内容改为动画执行完毕
  $("#box").fadeIn(3000，function(){
      $(this).text('动画执行完毕');
  })；
  ```

###### 练习

```js
1. dom表格的优化
2. 购物车的优化
3. 倒计时和雪花飘飘的优化
4. 淡入淡出轮播图
5. todolist
```

## 本地存储

### 目录

- localStorage*
  - setItem
  - getItem
  - removeItem
  - clear
- sessionStorage
  - setItem
  - getItem
  - removeItem
  - clear
- 本地存储字符串和对象之间的转换*
  - JSON.parse()
  - JSON.stringify

### 概念

- HTML5 提供了一系列的api，能够让我们将页面上的数据保存到本地并管理。

### 分类

- 根据保存时间的不同，将本地存储的api分成两类：`localStorage`和`sessionStorage`

### 特点

- `localStorage` 的保存期限是永久
- `sessionStorage`的保存期限是直到标签页关闭。

### localStorage

#### 常用api

- setItem:将数据以`属性名:属性值`的形式保存到本地

- getItem：以`属性名`来读取保存的数据

- removeItem：根据`属性名`来删除对应的数据

- clear：清空所有的数据

  ```js
  1. 保存数据
  localStorage.setItem("属性名","属性值") ;
  2. 获取数据
  localStorage.getItem("属性名") ;
  3. 删除数据
  localStorage.removeItem("属性名");
  4. 清空
  localStorage.clear();
  ```

### sessionStorage

#### 常用api

- setItem:将数据以`属性名:属性值`的形式保存到本地

- getItem：以`属性名`来读取保存的数据

- removeItem：根据`属性名`来删除对应的数据

- clear：清空所有的数据

  ```js
  1. 保存数据
  sessionStorage.setItem("属性名","属性值") ;
  2. 获取数据
  sessionStorage.getItem("属性名") ;
  3. 删除数据
  sessionStorage.removeItem("属性名");
  4. 清空
  sessionStorage.clear();
  ```

#### 对象和本地存储字符串之间的转换

- JSON.parse():可以将对象的字符串格式转为真正的对象
- JSON.stringify()：可以将对象格式转为字符串格式

```js
var str = "{name: '13999999999', pass: '123456'}";
//转为对象
var obj = JSON.parse(str);
var obj2 = {
    age:12,
    sex:'男'
}
//转为字符串
var str2 = JSON.stringify(obj2);"{age:12,sex:'男'}";
```

#### 本地存储处理对象数据

- 如果是保存到本地
  - 那么先将对象用`JSON.stringify`转为字符串，再利用`setItem`保存到本地
- 如是读取本地数据
  - 那么先利用`getitem`将字符串读取出来，再利用`JSON.parse`转为对象后进行使用

# canvas

## 目录

- canvas基础
  - 画布
  - 画笔
  - 路径
  - canvas中的 坐标系
  - 一般流程
- 基础api
  - 线条
    - moveTo:将画笔移动到画布指定位置
    - lineTo:从画笔当前位置到指定位置勾勒出一条子路径
    - stroke():绘制所有勾勒的子路径
    - beginPath:开始绘制子路径
    - closePath:结束绘制子路径并将第一条子路径和最后一条子路径进行闭合处理
    - lineWidth:绘制线条的宽度
    - strokeStyle:绘制线条的颜色
  - 弧形(曲线)
    - arc:勾勒出一段弧线
    - fill():对闭合图形进行填充
    - fillStyle:使用fill时使用的填充颜色
  - 其他
    - clearRect:清理画布的指定区域。类似于擦黑板，清理痕迹。
- 应用
  - 奔驰车标
  - loading动画
  - 其他综合例子：粒子动画、星空穿梭等

## canvas基础

### 概念

- HTML5为了页面能够实现复杂的动画，新增了canvas 绘制图形技术。指的是利用了`<canvas></canvas>`以及JavaScript 配套的相应api来实现页面绘制图形的目的。
- canvas绘图技术再搭配JavaScript 定时器可以实现酷炫动画效果

### 画布

- 指的是页面中的`<canvas>`标签，每个`<canvas>`标签都可以理解为一个画布。每个画布都有一个专属的画笔。

- 画布有自己的宽高属性来设置尺寸。切忌用css设置尺寸。允许JavaScript来修改尺寸

  ```
  <canvas width="500" height="400" ></canvas>
  ```

### 画笔

- 指JavaScript为某个`"画布"`提供的一个对象。该对象里包含了用于绘制图形所需要的一系列的api。即我们获取画笔之后，通过调用对应的api能够在画布上进行绘制。

### 路径

- 完整路径：
  - 一条完整的路径可以看出一个闭合的图形。一个完整路径由多条子路径构成。每条子路径可以理解为图形的某一边。
- 子路径：
  - 是具体的一个线条，多条子路径可以闭合成为一条完整的路径。每条子路径可以由画笔来进行绘制。

### canvas中的坐标系

- 画布是通过其左上角作为原点:`(0,0)`。分为x轴和y轴。x轴是原点向右为正。y轴是原点向下为正。
- 因为画笔提供的很多api是根据画布坐标来使用的。

### 一般使用流程

```js
获取画笔之前需要先获取画布：
HTML：
<canvas id="demo"></canvas>
JavaScript：
1. 获取画布
var canvas = document.querySelector('#demo');
2. 获取该画布专属画笔
var ctx = canvas.getContext('2d');
3. 调用画笔的对应api来进行绘制
ctx.函数名();
```

### 基础api

#### 线条

```js
1. 获取画布
var canvas = document.querySelector('#demo');
2. 获取该画布专属画笔
var ctx = canvas.getContext('2d');
```

- moveTo:将画笔移动到画布指定位置

  ```js
  画笔变量名.moveTo(x,y);
  例子： 将画笔移动到(200,100)处
  ctx.moveTo(200,100);
  ```

- lineTo:从画笔当前位置到指定位置勾勒出一条子路径,。只是勾勒线条，不包括绘制本身。

  ```js
  画笔变量名.lineTo(x,y);
  例如：从(200,100)到(200,200)处勾勒出一个线条
  ctx.moveTo(200,100);
  ctx.lineTo(200,200);
  ```

- stroke():绘制所有勾勒的子路径

  ```js
  画笔变量名.stroke();
  例子；从(200,100)到(200,200)处绘制一个线条
  ctx.moveTo(200,100);
  ctx.lineTo(200,200);
  ctx.stroke();
  ```

- beginPath:开始绘制子路径

  ```js
  画笔变量名.beginPath();
  ```

  - 开始勾勒线条之前调用，程序会记录画笔的子路径的 勾勒情况。勾勒完最后一条子路径后，使用`closePath`来闭合子路径。

- closePath:结束绘制子路径并将第一条子路径和最后一条子路径进行闭合处理

  ```js
  画笔变量名.closePath();
  ```

  - 调用`closePath()`后会将第一条子路径和最后一条子路径进行闭合，形成一个闭合的完整路径，即闭合图形。之后再调用`stroke()`来绘制图形

- lineWidth:绘制线条的宽度

  ```js
  画笔变量名.lineWidth =数值;
  例子：将线条的宽度设置为5px
  ctx.lineWidth = 5;
  ```

- strokeStyle:绘制线条的颜色

  ```js
  画笔变量名.strokeStyle ="颜色";
  例子：将线条的颜色设置为红色
  ctx.strokeStyle ="red";
  ```

#### 弧形

- arc:能够勾勒出一个弧形的子路径

  ```js
  画笔变量名.arc(圆心的x坐标,圆心的y坐标,弧形的半径,弧形的开始角度，弧形的结束角度，是否逆时针);
  例子；从0度到90度形成一条顺时针的一段弧形
  ctx.arc(200,200,50,0,Math.PI/2);
  ctx.stroke();
  ```

  - 360度是以`Math.PI*2`来表示。180度即`Math.PI`.1度为`Math.PI/180`
  - 默认顺时针，如果想要逆时针。arc末尾加一个实际参数`true`

#### 其他api

- fillStyle：指定填充颜色
- fill():用于填充某个闭合图形。

```js
画笔变量名.fillStyle = '颜色';
画笔变量名.fill();
例子：
ctx.fillStyle = "red";
ctx.fill();
```

- clearRect:清理画布的指定区域，即清理绘制痕迹

  ```js
  画笔变量名.clearRect(清理区域的左上角的x坐标,清理区域的左上角的y坐标,清理区域的宽度,清理区域的高度);
  例子：清理整个画布
  ctx.clearRect(0,0,canvas.width,canvas.height)
  ```

#### 应用

#### loading

- 思路：利用定时器不断的去绘制一段弧形来达到loading的效果

- 流程：

  - 先构建一个4分之1 的圆
  - 定义两个变量表示开始角度和结束角度，并赋予初始值。
  - 利用间隔定时器不断产生4分之一圆然后开始和结束角度每次自增。但保持开始和结束角度增量一致。即两者之间的差值固定的

  ```js
  var oneAngle = Math.PI/180;
  var start = 0;
  var end = 90;
  var timer =setInterval(() => {
      //清理画布之前的绘制痕迹
      ctx.clearRect(0,0,canvas.getAttribute('width'),canvas.getAttribute('height'));
      ctx.beginPath();
      ctx.arc(150,150,30,start *oneAngle,end*oneAngle);
      ctx.stroke();
      //开始和结束角度自增
      start +=4;
      end +=4;
  }, 10);
  setTimeout(() => {
      clearInterval(timer);
      canvas.style.display = "none";
  }, 3000);
  ```

## HTML 拖拽

### 目录

- 拖拽流程

### 概念

- html5 提供了原生的拖拽相关api，由JavaScript支持。

### 具体流程

- 给拖拽标签添加HTML标签属性`darggable=true`.

  - 表示该元素可以被拖拽

- 给放置元素设置`dragover`事件，该事件中只有一句代码，即取消默认行为

  - 表示取消某标签不可为放置元素，即执行事件后该元素可以作为放置元素

  ```js
  标签变量名.addEventListener('dragover',function(e){
      e.preventDefault();
  });
  ```

- 当某标签有放置元素资格后，就可以设置`drop`事件。该事件是拖拽标签释放时会触发

  ```js
  标签变量名.addEventListener('drop',function(e){
              console.log('drop事件触发')
  });
  ```

  - 会在drop事件里面进行两个标签之间的顺序切换

- 实现拖拽效果

  - 给拖拽标签设置`dragstart`事件，并通过`event.dataTransfer`设置数据，表示谁被拖拽了。该数据可以在另一个标签中的`drop`事件中拿到该数据

    ```js
    拖拽标签变量名.addEventListener('dragstart',function(e){
          //设置数据，表示谁被拖拽了。
          e.dataTransfer.setData('class','item1');
    });
    ```

  - 给放置标签中的`drop`事件中获取数据，并真正实现标签的交换效果

    ```js
    标签变量名.addEventListener('drop',function(e){
        var data = e.dataTransfer.getData('class');//item1
        //根据拿到的数据找到被拖拽的标签，并实现放置标签和拖拽标签之间的交换
    });
    ```

## 移动端

### 目录

- 移动端基础概念
- 屏幕与像素
  - 物理像素
  - 逻辑像素
- 视口
  - 布局视口
  - 视觉视口
  - 理想视口
- 移动端页面开发
  - 相对单位
  - 开发技巧

### 移动端基础概念

#### 什么是移动端开发

- 专门针对移动设备来进行开发页面的一整套技术。
- 移动设备主要包含了手机和平板两个平台。

#### 为什么不直接使用响应式布局

- 响应式布局是通过针对不同设备书写不同css代码来实现。为了兼容不同宽度的设备会导致css代码很多。
- 很多在pc端能够展示的内容在移动端无法展示或用户体验不好
  - 王者荣耀

### 屏幕与像素

#### 屏幕的概念和尺寸

#### 基础概念

- 手机屏幕大小是按英寸来展示说明。一英寸约等于2.54厘米.
- 一般说手机是6.1英寸，是指手机屏幕对角线的长度为6.1英寸

#### 像素

- 1像素指一个发光点，每个像素都可以表示一种颜色。

#### 设备物理像素

- 一般了解的手机分辨率就是指的设备物理像素。指的是手机上发光点的数量。分辨率越高，手机屏幕越能展示更清晰的画面。

#### 设备逻辑像素

- 因为现在手机普遍分辨率越来越高，导致如果直接用该分辨率在手机上展示pc端页面，会出现文字图片很小，无法看清。
- 逻辑像素是指的手机一个屏幕的css分辨率。是为了能够更好的展示移动端页面
  - 比如iPhone 12 Promax 的设备逻辑像素为：428 X 926 。指的css中的428就是100%屏幕宽度。926就是首屏的100%高度。

#### 设备独立像素比-dpi

- 指的物理分辨率和逻辑像素分辨率的比值：

  ```
  dpi = 物理分辨率宽度 / 逻辑像素宽度
  ```

  - 比如：iPhone 12 Promax dpi为 ： 1284 ：428 =3

### 视口类型

#### 视口

- 指的是手机屏幕上展示内容的区域，

#### 布局视口

- 随着移动端的流行，需要再手机上能够正常显示pc端，很多厂商就默认了手机的100%宽度是980px，也有的是1024px，

#### 视觉视口

- 指的就是屏幕的宽度部分。

#### 理想视口

- 指的是无论哪一种屏幕，哪一种分辨率，同样的内容的展示效果是一致的。理想视口的空间区域 就是指的设备逻辑像素区域。

- 每个屏幕的设备逻辑像素不一样，即每个设备的理想视口区域也是不一样的。

- 常见的手机理想视口宽度

  - 主要：360 375 411 414
  - 部分：320 420 480

- 常见的平板理想宽度

  - 1024 768

- 页面指定理想视口

  - 在`<head></head>`标签中,追加一个`<meta>`标签

    ```js
    <meta name="viewport" content="width=device-width, initial-scale=1.0,user-scalable=no">
    ```

  - <meta>: 写在<head>标签中，用于完成页面的相关配置。比如设置字符编码集

  - `name=viewport`:设置视口，如果没有设置视口。默认页面用的布局视口。

  - `content`:设置时具体 哪一种视口。其中`width=device-width`,设置100%宽度等于该设备的逻辑像素

  - `initial-scale`:设置页面的初始缩放比例为1

  - `user-scalable=no`:设置页面不可缩放，可选。yes即页面可以缩放。

### 移动端开发技巧

#### 移动端常用相对单位

- em：是相对单位，具体的1em，等于父标签的font-size大小。如果父标签没有font-size，会继续往上面找，都没有的话直接使用默认值，一般为16px。

  ```js
  html :
  <p>这是p标签里的内容 <span>span里的 内容</span></p>
  css:
  body{
      font-size: 20px;
  }
  p{
      font-size: 2em;//40px
  }
  span{
      font-size: 2em;//80px
  }
  ```

- rem:相对单位，是只相对于`<html>`标签的`font-size`，跟父标签的font-size无关。

  ```js
  html :
  <p>这是p标签里的内容 <span>span里的 内容</span></p>
  CSS:
  html{
      font-size: 25px;
  }
  span{
      /* font-size: 2em; */
      font-size: 2rem;//50px
  }
  ```

- vw

  - 相对于视口的宽度而言。1vw等于视口区域的1%宽度。视口一般指的是手机屏幕用于展示数据的那部分空间。

- vh

  - 相对于视口的宽度而言。1vh等于视口区域的1%高度。视口一般指的是手机屏幕用于展示数据的那部分空间。

#### 移动端页面开发技巧

- 整体把控
  - 使用理想视口
  - 整体标签的宽高以及字体以rem为主，百分比为辅
  - padding和margin也可以用rem
  - 列表、导航可以用弹性布局。
- 具体细节
  - 文字：正文0.24rem 标题 0.26rem
  - margin或padding:0.3rem左右
  - 高度：视情况而定

## 数据交互

### ajax

#### 概念

- ajax指的是利用JavaScript向服务器发送数据请求并得到服务器响应的数据。

  ![数据交互](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/dengnaiwen/20210728101515.png)

#### 作用

- 实现动态的网页。页面展示的数据都来自于网络(服务器)

#### 流程

- 利用jQuery提供的`$.ajax()`来发送请求，并在`success`函数中对从服务器拿到的数据进行处理：利用dom将数据展示在页面上

#### ajax语法(jQuery)

```js
$.ajax({
    url:'拿数据的网络地址',
    success:function(data){
        ajax拿到数据后会自动调用success函数，并把数据作为实际参数传过来，我们只需要定义形式参数来接收
        console.log(data);//data就是获取的数据
    }
}); 
console.log('这段代码可能会比success先执行，因为网络有延迟');
```

## 百度地图

### 目录

- 百度地图账号注册及基本使用
- 常见操作
  - 设置点击事件
  - 获取某个地点坐标
  - 根据某个坐标添加标注
  - 根据地址反向解析坐标

### 基本操作

#### 使用百度地图

- 登录百度地图开发平台
- 创建应用-获取应用密钥-ak
  - 在创建应用时选择浏览器端
- 访问百度地图例子页面，复制代码放入在自己页面中，替换密钥，用live server打开。
  - 可以使用css来控制显示百度地图标签的尺寸位置等。

#### 常用操作

#### 设置点击事件

#### 获取某个地点坐标

#### 根据某个坐标添加标注

#### 根据地址解析坐标

