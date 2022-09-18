## ES6简介与变量使用

### ES6简介

ES6，全称ECMAScript6.0，是JavaScript的版本标准，是2015年6月发布的。

ES6的出世是补全了ES5的不足之处（如：增加了类的概念）更好的完善了编程的特性和功能。

![image-20210727093507636](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210727093513.png)

### ECMAScript的背景

JavaScript 是大家所了解的语言名称，但是这个语言名称是商标（ Oracle 公司注册的商标）。因此，JavaScript 的正式名称是 ECMAScript 。ECMA（European computer manufactures association，欧洲计算机制造联合会）**以下我们简称ES6**

### ES6环境搭建

现在各大浏览器都支持ES6的编译，主要有如下：

- Chrome谷歌浏览器
- Firefox火狐浏览器
- Safari
- Opera
- 微软浏览器（Edge）

**备注：IE7-11不支持**

### ES6变量

#### 01.创建变量和赋值

ES6新增了JavaScript的两个重要关键字：`let`和`const`，来创建变量。语法结构如下：

```js
let 变量名 = 变量值；const 变量名 = 变量值；
```

和之前Javascript创建变量`var 变量= 变量值`一致，如下：

```js
var a = 1;
let b = 2;
const c = 3;
console.log(a);//1
console.log(b);//2
console.log(c);//3
```

#### 02.变量的初始值

```js
var a;
let b;
const c;
a = 1;b = 2;c = 3;
console.log(a);//1
console.log(b);//2
console.log(c);//Uncaught SyntaxError: Missing initializer in const declaration
```

**结论：**var和let可以**‘先定义后使用’**，const不行，必须定义和赋值一并完成，因为const称为“常量”。

#### 03.变量的作用域

**“作用域”**就是变量的使用范围以及可执行范围，变量在这个范围内可以使用和运行，超过这个范围就不行了。

`var`的作用域是所在函数使用范围，如果没有函数就往外传递，直至到最外层（windows）。

```js
function foo() {    
    var a = 10;    
    console.log(a);//10
}
foo()
console.log(a);//a is not defined
```

示例说明：超过作用域范围就无法调用a了。

`let`和`const`的作用域是在包含他的**大括号**里，超过大括号就不能执行了。

```js
function foo() {    
    if(true){        
        let a = 1;       
        const b = 2       
        console.log(a);//1       
        console.log(b);//2    
    }    
    console.log(a);//a is not defined    
    console.log(b);//由于上面报错，所以不执行了
}
foo();
```

#### 04.变量的提升

**变量提升：**在所有的 JS 代码正式执行之前，浏览器会将所有的代码先解析一边，在解析的过程中，找到所有通过 `var` 创建的变量，将这些变量的声明（创建）提升到当前作用域的头部，然后才开始正式执行代码。

原始代码：

```js
console.log(a);//undefinedvar a = 1;
```

变量提升后的代码：

```js
var a;console.log(a);//undefineda = 1;
```

**代码说明：**变量提升后代码就变成了“先定义后使用”。

注意：只是提升变量声明，不是变量赋值。

### ES6函数操作

#### 函数定义分类

##### **函数分为两种形式**

声明式函数：

```js
function name(params) {}
```

函数表达式：

```js
var foo = function(){}
```

#### 函数提升

声明式函数，具有函数提升操作。函数表达式没有函数提升操作。

原始代码：

```js
foo();
function foo() {    
console.log("hello");
}
```

提升后的代码：

```js
function foo() {    
console.log("hello");
}
foo();
```

代码说明：函数提升同样会在代码运行前完成代码的提升操作。所以两段代码的运行结构都是hello，正常执行。

#### 函数和变量的名称冲突

当我们 var 创建的变量和声明式函数重名时，两个都会发生提升，**当变量没有赋值时**，变量优先级低于函数。因此**重名后会留下函数**。

看示例：

```js
console.log(a)
var a = 1;
function a() 
{    
console.log("hello");
}
console.log(a)
```

变量提升和声明式函数同时提升后：

```js
var a;function a() {   
console.log("hello");
}
console.log(a)//输出a()函数本身a = 1;
console.log(a)//1
```

代码说明：变量提升和声明式函数同时提升后，a只代表函数。所以输出a函数本身，之后给a赋值了，a就是变量了。所以输出1.

#### 函数的默认值

##### 01.定义默认值

我们可以在原先定义的函数上设置行参默认值。

- 当该形参接收到实参时，就使用实参。
- 当形参没有接收到实参时，就可以使用默认值。

```js
function fn(name,age=17){ 
console.log(name+","+age);
}
fn("Amy",18);  // Amy,18
fn("Amy","");  // Amy,
fn("Amy");     // Amy,17
```

注意：使用函数默认参数时，不允许有同名参数。

```js
// 不报错
function fn(name,name){
 console.log(name);
}
// 报错
//SyntaxError: Duplicate parameter name not allowed in this context
function fn(name,name,age=17){
 console.log(name+","+age);
}
```

##### 02.null传值

只有在未传递参数，或者参数为 undefined 时，才会使用默认参数，null 值被认为是有效的值传递。

```js
function fn(name,age=17){
    console.log(name+","+age);
}
fn("Amy",null); // Amy,null
```

##### 03.函数的暂时性死区

函数参数默认值存在暂时性死区，在函数参数默认值表达式中，还未初始化赋值的参数值无法作为其他参数的默认值。

可以调用：

```js
function f(x,y=x){
    console.log(x,y);
}
f(1);  // 1 1
```

不可以调用：

```js
function f(x=y){//y没有赋值
    console.log(x);
}
f();  // ReferenceError: y is not defined
```

#### ES6不定参数

##### 01.不定参数的书写

不定参数用来表示不确定参数个数，形如，…变量名，由…加上一个具名参数标识符组成。具名参数只能放在参数组的最后，并且有且只有一个不定参数。不定参数获取数据后会放置在一个**数组**里

```js
function f(...values){
    console.log(values.length);
}
f(1,2);      //2
f(1,2,3,4);  //4
```

##### 02.不定参数与设定参数

当一个函数出现不定参数和具体参数时，需要把具体参数写在前面，不定参数写在后面

```js
function f(a,b,...values){
    console.log(values);//[]
}
f(1,2); //[]
f(1,2,3,4);  //[3,4]
```

##### 03不定参数没有默认值

```js
function f(a,b,...values=[1,2]){
    console.log(values);//Rest parameter may not have a default initializer
}
f(1,2);
```

#### ES6箭筒函数

##### 01.箭头函数书写

箭头函数提供了一种更加简洁的函数书写方式。基本语法是：

```js
(参数1，参数2) => 函数体
//等价于
function funName(参数1，参数2){
    函数体
}
```

##### 02.函数表达式

当箭头函数有多个形参时，要用 **()** 括起来。如果只有一个形参可以不用括号，也可以加上。

一个形参

```js
var f = v => v;//省略了（）
//等价于
var f = function(a){
 return a;
}
f(1);  //1
```

多个形参

```js
var f = (a,b) => {
 let result = a+b;
 return result;
}
f(6,2);  // 8
```

##### 03.执行语句

当箭头函数的函数体有多条语句时，写法与基本函数一致。如果只有一条语句时就可以省略**return**和**{}**

多条函数体

```js
var f = (a,b) => {
 let result = a+b;
 return result;
}
f(6,2);  // 8
```

单条函数体

```js
var f = (a,b) => a+b
console.log(f(6,2));   // 8
```

##### 04.返回值

当箭头函数要返回对象的时候，为了区分于代码块，要用 **()** 将对象包裹起来

```js
// 报错
var f = (id,name) => {id: id, name: name};
f(6,2);  // SyntaxError: Unexpected token :
// 不报错
var f = (id,name) => ({id: id, name: name});
f(6,2);  // {id: 6, name: 2}
```

##### 05.this

箭头函数里面没有 this 对象，此时的 this 是外层的 this 对象，即 Window

```js
var a =20;
function foo(){
    let a = 10;
    let b = ()=>{
        console.log(this.a);
    }
    b();
}
foo();//20
```

说明：从this往外找最接近它的funciton，哪个对象调用这个function，this就是它，一直往上找不到就是window

##### 06箭头函数的运用示例

回调函数

```js
// 回调函数
var Person = {
    'age': 18,
    'sayHello': function () {
      setTimeout(function () {
        console.log(this.age);
      });
    }
};
var age = 20;
Person.sayHello();  // 20
var Person1 = {
    'age': 18,
    'sayHello': function () {
      setTimeout(()=>{
        console.log(this.age);
      });
    }
};
var age = 20;
Person1.sayHello();  // 18
```

### ES6数组操作

#### 数组的遍历

数组中除了for，while外还可以通过以下几种方式进行遍历

##### 01.forEach

```js
const arr = [10, 20, 30, 40];
arr.forEach(function(item, index) {
    console.log(item);  // 数组的每一项
    console.log(index); // 每一项的下标
})
// 简写
arr.forEach(item => {
    console.log(item);  // 数组的每一项
})
```

##### 02.map()

map可以在不破坏原数组的同时获取一个满足条件的新数组

```js
const arr = [10, 20, 30, 40];
const newArr = arr.map(function(item, index) {
    return item * 2;
});
console.log(newArr);// [20, 40, 60, 80]
```

##### 03.filter()

filter从原数组中筛选出满足条件的新数组

```js
const arr = [10, 20, 30, 40];
const newArr = arr.filter(function (item, index) {
    return item > 20;
})
// 简写
const newArr = arr.filter(item => item > 20);
console.log(newArr);
```

##### 04.some()

some可以通过 return 设置判断条件，当数组中有一项满足条件时，some 方法返回 true，如果所有项都不满足条件，则返回 false

```js
const arr = [10, 20, 30, 40];
var newArr = arr.some(function(item, index) {
    //return item > 20
    return item == 20
})
console.log(newArr);//true 表示数组中有满足条件的数据
//简写
console.log(arr.some(item => item > 30));
```

##### 05.every()

every可以通过 return 设置判断条件，当数组中有一项不满足条件时，every 方法返回 false。只有所有项都满足条件，才返回 true。

```js
const arr = [10, 20, 30, 40];
var newArr = arr.every(function(item, index) {
    return item > 30
})
console.log(newArr);//false，有一项不满足就返回false
//简写
arr.every(item => item > 30);
```

##### 06.reduce()

reduce 中的函数，接收两个形参，如下：

```js
const arr = [10, 20, 30, 40];
arr.reduce(function(item, next) {
    //...
})
```

其中，`item` 在第一次循环时，接收到的是数组中的第一项，从第二次循环开始，`item` 接收到的是**上一次循环**的返回值。`next` 就依次接收数组的下一项。

在 reduce 的函数中，语法要求需要通过 `return` 设置返回值，作为下一次循环的第一个参数：

```js
const arr = [10, 20, 30, 40];
var newArr = arr.reduce(function(item, next) {
    return item + next
})
console.log(newArr);//100
// 简写
const result = arr.reduce((item, next) => item + next);
```

通常，reduce 方法用于计算数组中每一项之和。（也可以是乘积）-累积值

#### 创建数组

##### Array.of()

```js
console.log(Array.of(1, 2, 3, 4)); // [1, 2, 3, 4]
```

参数值可以不同类型

```js
console.log(Array.of(1, '2', true)); // [1, '2', true]
```

### ES6数组与对象

#### 对象字面量

##### 01.属性的简洁表示法

ES6允许对象的属性直接写变量，这时候属性名是变量名，属性值是变量值。

```js
const age = 12;
const name = "tom";
const person = {age, name};
person   //{age: 12, name: "tom"}
//等同于
const person = {age: age, name: name}
```

##### 02.方法名与也可以缩写

```js
const person = {
  sayHi(){
    console.log("Hi");
  }
}
person.sayHi();  //"Hi"
//等同于
const person = {
  sayHi:function(){
    console.log("Hi");
  }
}
person.sayHi();//"Hi"
```

##### 03.属性名表达式

ES6运行用表达式作为属性名，但是一定要将表达式放在方括号内。

```js
const obj = {
 ["he"+"llo"](){
   return "Hi";
  }
}
obj.hello();  //"Hi"
```

#### 对象的扩展运算符

拓展运算符（…）用于取出参数对象所有可遍历属性然后拷贝到当前对象。

##### 01.基础用法

```js
let person = {name: "Amy", age: 15};
let someone = { ...person };
someone;  //{name: "Amy", age: 15}
```

合并两个对象

```js
let age = {age: 15};
let name = {name: "Amy"};
let person = {...age, ...name};
person;  //{age: 15, name: "Amy"}
```

自定义的属性和拓展运算符对象里面属性的相同的时候：**自定义的属性在拓展运算符后面，则拓展运算符对象内部同名的属性将被覆盖掉。**

```js
let person = {name: "Amy", age: 15};
let someone = { ...person, name: "Mike", age: 17};
someone;  //{name: "Mike", age: 17}
```

##### 02.默认值设置

自定义的属性在拓展运算度前面，则变成设置新对象默认属性值。

```js
let person = {name: "Amy", age: 15};
let someone = {name: "Mike", age: 17, ...person};
someone;  //{name: "Amy", age: 15}
```

#### 解构赋值

##### 01.解构赋值

赋值符左右两侧的数据结构保持一致，然后将右侧的数据赋值给左侧的变量。
数组

```js
// 解构赋值
const [a, b, c] = [1, 2, 3];
console.log(a); // 1
console.log(b); // 2
console.log(c); // 3
```

对象

```js
const { name: a, age: b } = {  name: 'zhangsan', age: 20 };
console.log(a, b);
const { name: name, age: age } = {  name: 'zhangsan', age: 20 };
// 简写
const { name, age } = {  name: 'zhangsan', age: 20 };
console.log(name, age);
```

##### 02.解构默认值

```js
const [a, b, c, d = 4] = [1, 2, 3, 5];
console.log(d);
const { a, b, c = 'hello' } = { a: 1, b: 2 };
console.log(c);
```

解构赋值的默认值和函数参数的默认值：

```js
function foo({a = 1, b = 2} = {}) {
    console.log(a, b);
}
foo();
```

### ES6Set和Map

Set 和 Map，是 ES6 中新增的两种数据结构

#### SET

Set 结构类似于数组，但是 Set 中的每一个元素都是唯一的。

```js
const s = new Set([1, 2, 3, 3, 1, '1', '2']);
console.log(s);  // [1, 2, 3, '1', '2']
```

通常用 Set 来实现数组的去重。

```js
const arr = [1, 2, 3, 3, 4, 4, 4];
cosnt newArr = new Set(arr);
```

#### MAP

Map 对象保存键值对。任何值(对象或者原始值) 都可以作为一个键或一个值。

key是字符串

```js
var myMap = new Map();
var keyString = "myString"; 
myMap.set(keyString, "关联值");
console.log(myMap);//Map(1) {"myString" => "关联值"}
console.log(myMap.get(keyString)); //关联值
console.log(myMap.get("myString"));//关联值
```

## 面向对象

### 编程模式

编程过程中编程方式分为2种：

- 面向过程
- 面向对象

面向过程是顺序执行的一种方式，代码按设计和运行流程一步一步向下运行

```
function 打开冰箱门() {    //.. }function 把大象装进冰箱() {    // ...}function 关闭冰箱门() {    // ...}打开冰箱门();把大象装进冰箱();关闭冰箱门();
```

面向对象是一种编程思想，是把所有行为和特性先归并到隶属的对象上，再进一步的调用编程模式

```
const 冰箱 = {}const 大象 = {}冰箱.开门 = function() {    // ...}冰箱.关门 = function() {    // ...}大象.进入冰箱 = function() {}冰箱.开门();大象.进入冰箱();冰箱.关门();
```

### 类的概念

#### 01.类的简介

类，是一组属性和方法相同的对象的集合，对象属于类。**“世间一切节对象”**

#### 02.创建对象

可以通过**构造函数**创建对象

构造函数是创建对象的特殊函数，在创建对象时调用，调用时用new关键字，建议首字母大写。

```js
function Student() {
}
const s = new Student();
console.log(s);
```

`s` 就是一个通过 `Student` 函数构造出来的一个对象。

### 03.设置对象的属性

对象的属性是通过this关键字设置，在function内部创建

```js
function Student(name) {
    this.name = name;
    this.age = 20;
    this.gender = '男';
}
const s = new Student('张三');
const s1 = new Student('李斯');
console.log(s);//Student {name: "张三", age: 20, gender: "男"}
console.log(s1);//Student {name: "李斯", age: 20, gender: "男"}
```

**说明：**每个属性在生成后都是归属每个对象，即每个对象有单独的自己的属性

### 04.设置对象的方法

对象所有的方法，都设置在函数的 prototype 属性上。

```js
function Student(name) {
    this.name = name;
    this.age = 20;
    this.gender = '男';
}
//类名..prototype.方法名
Student.prototype.study = function() {
    console.log('学习...');
}
Student.prototype.sleep = function() {
    console.log('睡觉...');
}
```

调用方法时，还是通过 `对象.方法名()` 调用即可

```js
function Student(name) {
    this.name = name;
    this.age = 20;
    this.gender = '男';
}
//类名..prototype.方法名
Student.prototype.study = function() {
    console.log('学习...');
}
Student.prototype.sleep = function() {
    console.log('睡觉...');
}
const s = new Student('张三');
const s1 = new Student('李斯');
s.study();//学习...
s1.sleep();//睡觉...
```

也可以在定义类的时候同时定义方法

```js
function Student(name) {
    this.name = name;
    this.age = 20;
    this.gender = '男';
    this.study = function() {
        console.log('学习...');
    };
    this.sleep = function() {
        console.log('睡觉...');
    }
}
const s = new Student('张三');
const s1 = new Student('李斯');
s.study();//学习...
s1.sleep();//睡觉...
```

### Class

在ES6中，class (类)作为对象的模板被引入，可以通过 class 关键字定义类

class 的本质是 function

#### 类的使用

#### 01.类的定义

ES6 中新增的用于创建类的方式 —— Class

#### 02.类的创建

把原来function关键字转换成Class，直接在Class类中定义

```js
class Juicer {
    constructor(name, width, height) {
        // 属性
        this.name = name
        this.width = width;
        this.height = height;
    }
    // 方法
    open() {
        console.log('open');
    }
    close() {
        console.log('close');
    }
}
```

#### 03.调用类

通过调用类得到实例对象

```
// 实例对象const bingxiang = new Juicer('冰箱', 1000, 2000);
```

#### 04.访问对象的属性和方法

```
bingxiang.open();bingxiang.close();console.log(bingxiang.name);
```

#### class类的构造函数

class的构造函数是需要使用constructor来定义

```js
class Example{
    constructor(val) {
        this.a = val;
    }
}
```

注意，类名不能重复声明

```js
class Example{}
class Example{}
//Uncaught SyntaxError: Identifier 'Example' has already been
```

##### 类的提升

类定义不会被提升，这意味着，必须在访问前对类进行定义，否则就会报错。

##### 静态方法和属性

class 本身的属性，即直接定义在类内部的属性（ Class.propname ），不需要实例化

```js
class Example {
// 新提案
    static a = 2;
    static foo(){
        console.log("静态方法")
    }
}
// 目前可行写法
console.log(Example.a); //2
Example.foo(); //静态方法
Example.foo;//（无返回）
```

### 继承

面向对象三大特性：封装、继承、多态。

#### Class的继承

类之间可以有一种关系称为子类和父类关系，子类里面的属性和方法来源于父类的，这种子父关系，我们称为“Class的继承”。同时子类还可以拥有自己的属性和方法。

#### 创建一个父类

```js
class Father {
    //构造函数
    constructor() {
        this.name = 'tom'
    }
    //方法
    sayHello() {
        console.log('hello');
    }
}
```

通过`extends`继承父类来创建一个子类,同时还可以设置自己的属性和方法：

```js
class Child extends Father {
    constructor() {
        super();//调用父类的构造函数
        this.age = 12;
    }
    homework() {
        console.log('写作业');
    }
}
```

继承后的子类实例，可以拥有父类的属性和方法：

```js
const f1 = new Father();
const c1 = new Child();
console.log(f1);
console.log(c1);
c1.sayHello();
```

#### call()

- call()可以调用函数
- call()可以修改this的指向,使用call()的时候 参数一是修改后的this指向,参数2,参数3..使用逗号隔开连接

```js
function fn(x, y) {
     console.log(this);
     console.log(x + y);
}
  var o = {
  	name: 'andy'
  };
  fn.call(o, 1, 2);//调用了函数此时的this指向了对象o,
```

![image-20210912193539548](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912193539548.png)

#### 子构造函数继承父构造函数中的属性

1. 先定义一个父构造函数
2. 再定义一个子构造函数
3. 子构造函数继承父构造函数的属性(使用call方法)

```js
// 1. 父构造函数
 function Father(uname, age) {
   // this 指向父构造函数的对象实例
   this.uname = uname;
   this.age = age;
 }
  // 2 .子构造函数 
function Son(uname, age, score) {
  // this 指向子构造函数的对象实例
  3.使用call方式实现子继承父的属性
  Father.call(this, uname, age);
  this.score = score;
}
var son = new Son('刘德华', 18, 100);
console.log(son);
```

#### 借用原型对象继承方法

1. 先定义一个父构造函数

2. 再定义一个子构造函数

3. 子构造函数继承父构造函数的属性(使用call方法)

   ```js
   // 1. 父构造函数
   function Father(uname, age) {
     // this 指向父构造函数的对象实例
     this.uname = uname;
     this.age = age;
   }
   Father.prototype.money = function() {
     console.log(100000);
    };
    // 2 .子构造函数 
     function Son(uname, age, score) {
         // this 指向子构造函数的对象实例
         Father.call(this, uname, age);
         this.score = score;
     }
   // Son.prototype = Father.prototype;  这样直接赋值会有问题,如果修改了子原型对象,父原型对象也会跟着一起变化
     Son.prototype = new Father();
     // 如果利用对象的形式修改了原型对象,别忘了利用constructor 指回原来的构造函数
     Son.prototype.constructor = Son;
     // 这个是子构造函数专门的方法
     Son.prototype.exam = function() {
       console.log('孩子要考试');
   
     }
     var son = new Son('刘德华', 18, 100);
     console.log(son);
   ```

   ![image-20210912193731522](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912193731522.png)

#### Object.defineProperty

Object.defineProperty设置或修改对象中的属性

```js
Object.defineProperty(对象，修改或新增的属性名，{
		value:修改或新增的属性的值,
		writable:true/false,//如果值为false 不允许修改这个属性值
		enumerable: false,//enumerable 如果值为false 则不允许遍历
        configurable: false  //configurable 如果为false 则不允许删除这个属性 属性是否可以被删除或是否可以再次修改特性
})	
```



### 构造函数原型prototype

构造函数通过原型分配的函数是所有对象所共享的。

JavaScript 规定，每一个构造函数都有一个prototype 属性，指向另一个对象。注意这个prototype就是一个对象，这个对象的所有属性和方法，都会被构造函数所拥有。

我们可以把那些不变的方法，直接定义在 prototype 对象上，这样所有对象的实例就可以共享这些方法。

```js
function Star(uname, age) {
    this.uname = uname;
    this.age = age;
}
Star.prototype.sing = function() {
	console.log('我会唱歌');
}
var ldh = new Star('刘德华', 18);
var zxy = new Star('张学友', 19);
ldh.sing();//我会唱歌
zxy.sing();//我会唱歌
```

### 对象原型

对象都会有一个属性 __proto__ 指向构造函数的 prototype 原型对象，之所以我们对象可以使用构造函数 prototype 原型对象的属性和方法，就是因为对象有 __proto__ 原型的存在。
__proto__对象原型和原型对象 prototype 是等价的
__proto__对象原型的意义就在于为对象的查找机制提供一个方向，或者说一条路线，但是它是一个非标准属性，因此实际开发中，不可以使用这个属性，它只是内部指向原型对象 prototype

![image-20210912193040926](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912193040926.png)

### constructor构造函数

对象原型（ __proto__）和构造函数（prototype）原型对象里面都有一个属性 constructor 属性 ，constructor 我们称为构造函数，因为它指回构造函数本身。
constructor 主要用于记录该对象引用于哪个构造函数，它可以让原型对象重新指向原来的构造函数。
一般情况下，对象的方法都在构造函数的原型对象中设置。如果有多个对象的方法，我们可以给原型对象采取对象形式赋值，但是这样就会覆盖构造函数原型对象原来的内容，这样修改后的原型对象 constructor  就不再指向当前构造函数了。此时，我们可以在修改后的原型对象中，添加一个 constructor 指向原来的构造函数。

#### 原型链

每一个实例对象又有一个__proto__属性，指向的构造函数的原型对象，构造函数的原型对象也是一个对象，也有__proto__属性，这样一层一层往上找就形成了原型链。

![image-20210912193133976](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912193133976.png)

#### 构造函数实例和原型对象三角关系

1.构造函数的prototype属性指向了构造函数原型对象
2.实例对象是由构造函数创建的,实例对象的__proto__属性指向了构造函数的原型对象
3.构造函数的原型对象的constructor属性指向了构造函数,实例对象的原型的constructor属性也指向了构造函数

![image-20210912193202658](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912193202658.png)

#### 原型链和成员的查找机制

任何对象都有原型对象,也就是prototype属性,任何原型对象也是一个对象,该对象就有__proto__属性,这样一层一层往上找,就形成了一条链,我们称此为原型链;

当访问一个对象的属性（包括方法）时，首先查找这个对象自身有没有该属性。
如果没有就查找它的原型（也就是 __proto__指向的 prototype 原型对象）。
如果还没有就查找原型对象的原型（Object的原型对象）。
依此类推一直找到 Object 为止（null）。
__proto__对象原型的意义就在于为对象成员查找机制提供一个方向，或者说一条路线。

#### 原型对象中this指向

构造函数中的this和原型对象的this,都指向我们new出来的实例对象

```js
function Star(uname, age) {
    this.uname = uname;
    this.age = age;
}
var that;
Star.prototype.sing = function() {
    console.log('我会唱歌');
    that = this;
}
var ldh = new Star('刘德华', 18);
// 1. 在构造函数中,里面this指向的是对象实例 ldh
console.log(that === ldh);//true
// 2.原型对象函数里面的this 指向的是 实例对象 ldh
```

### this操作

![image-20210912194012847](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912194012847.png)

#### 全局中的this

当 this 不在任何函数内部时，this 始终是指向全局对象。

```js
console.log(this);//window
```

说明：在浏览器中，全局对象时window

#### 普通函数中的this

普通函数：指的是直接通过 `函数名()` 调用的函数，都是普通函数。

普通函数外部没有任何其他内容，this始终是指向全局对象。

```js
function foo() {
    console.log(this);
}
foo();//window
window.foo();//window
const bar = function() {
    console.log(this);//window
}
bar();
```

#### 对象中的this

对象方法：指的是通过 `对象.方法名()` 调用的函数，都是对象的方法。

对象方法中的 this，始终是指向调用该方法的对象。

```
const student = {
    a : 100,
    sayName() {
        console.log(this);
    }
}
 student.sayName();//{a: 100, sayName: ƒ}   student对象
```

示例2：

```js
const student = {
    name: 'student',
    sayName() {
        console.log(this);
    }
}
const person = {
    name: 'person'
};
person.sayName = student.sayName;
person.sayName();
```

显示的是person

#### 事件方法中的this

事件方法：指的就是各类事件的事件处理函数。onclick…

事件方法中的 this，始终是指向绑定该事件的元素节点。

```js
<div class="outer">hello</div>
<script>
const outer = document.querySelector('.outer');
// 事件源
outer.onclick = function() {
    console.log(this);//<div class="outer">hello</div>
}
```

### 改变函数内部 this 指向

#### call方法

call()方法调用一个对象。简单理解为调用函数的方式，但是它可以改变函数的 this 指向

应用场景:  经常做继承. 

```js
var o = {
	name: 'andy'
}
 function fn(a, b) {
      console.log(this);
      console.log(a+b)
};
fn(1,2)// 此时的this指向的是window 运行结果为3
fn.call(o,1,2)//此时的this指向的是对象o,参数使用逗号隔开,运行结果为3
```

![image-20210912194100859](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912194100859.png)

#### apply方法

apply() 方法调用一个函数。简单理解为调用函数的方式，但是它可以改变函数的 this 指向。

应用场景:  经常跟数组有关系

```js
var o = {
	name: 'andy'
}
 function fn(a, b) {
      console.log(this);
      console.log(a+b)
};
fn()// 此时的this指向的是window 运行结果为3
fn.apply(o,[1,2])//此时的this指向的是对象o,参数使用数组传递 运行结果为3
```

![image-20210912194136721](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912194136721.png)

####  bind方法

bind() 方法不会调用函数,但是能改变函数内部this 指向,返回的是原函数改变this之后产生的新函数

如果只是想改变 this 指向，并且不想调用这个函数的时候，可以使用bind

应用场景:不调用函数,但是还想改变this指向

```js
 var o = {
 name: 'andy'
 };

function fn(a, b) {
	console.log(this);
	console.log(a + b);
};
var f = fn.bind(o, 1, 2); //此处的f是bind返回的新函数
f();//调用新函数  this指向的是对象o 参数使用逗号隔开
```

![image-20210912194219506](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912194219506.png)

#### call、apply、bind三者的异同

共同点 : 都可以改变this指向

不同点:

- call 和 apply  会调用函数, 并且改变函数内部this指向.
- call 和 apply传递的参数不一样,call传递参数使用逗号隔开,apply使用数组传递
- bind  不会调用函数, 可以改变函数内部this指向.

应用场景

1. call 经常做继承. 
2. apply经常跟数组有关系.  比如借助于数学对象实现数组最大值最小值
3. bind  不调用函数,但是还想改变this指向. 比如改变定时器内部的this指向. 

### 严格模式

#### 什么是严格模式

JavaScript 除了提供正常模式外，还提供了严格模式（strict mode）。ES5 的严格模式是采用具有限制性 JavaScript变体的一种方式，即在严格的条件下运行 JS 代码。

严格模式在 IE10 以上版本的浏览器中才会被支持，旧版本浏览器中会被忽略。

严格模式对正常的 JavaScript 语义做了一些更改： 

1.消除了 Javascript 语法的一些不合理、不严谨之处，减少了一些怪异行为。

2.消除代码运行的一些不安全之处，保证代码运行的安全。

3.提高编译器效率，增加运行速度。

4.禁用了在 ECMAScript 的未来版本中可能会定义的一些语法，为未来新版本的 Javascript 做好铺垫。比如一些保留字如：class,enum,export, extends, import, super 不能做变量名

#### 开启严格模式

严格模式可以应用到整个脚本或个别函数中。因此在使用时，我们可以将严格模式分为为脚本开启严格模式和为函数开启严格模式两种情况。

- 情况一 :为脚本开启严格模式

  - 有的 script 脚本是严格模式，有的 script 脚本是正常模式，这样不利于文件合并，所以可以将整个脚本文件放在一个立即执行的匿名函数之中。这样独立创建一个作用域而不影响其他
    script 脚本文件。

```js
(function (){
  //在当前的这个自调用函数中有开启严格模式，当前函数之外还是普通模式
　　　　"use strict";
       var num = 10;
　　　　function fn() {}
})();
//或者 
<script>
  　"use strict"; //当前script标签开启了严格模式
</script>
<script>
  			//当前script标签未开启严格模式
</script>
```

情况二: 为函数开启严格模式

- 要给某个函数开启严格模式，需要把“use strict”;  (或 'use strict'; ) 声明放在函数体所有语句之前。

  ```js
  function fn(){
  　　"use strict";
  　　return "123";
  } 
  //当前fn函数开启了严格模式
  ```

  #### 严格模式中的变化

  严格模式对 Javascript 的语法和行为，都做了一些改变。

  ```js
  'use strict'
  num = 10 
  console.log(num)//严格模式后使用未声明的变量
  --------------------------------------------------------------------------------
  var num2 = 1;
  delete num2;//严格模式不允许删除变量
  --------------------------------------------------------------------------------
  function fn() {
   console.log(this); // 严格模式下全局作用域中函数中的 this 是 undefined
  }
  fn();  
  ---------------------------------------------------------------------------------
  function Star() {
  	 this.sex = '男';
  }
  // Star();严格模式下,如果 构造函数不加new调用, this 指向的是undefined 如果给他赋值则 会报错.
  var ldh = new Star();
  console.log(ldh.sex);
  ----------------------------------------------------------------------------------
  setTimeout(function() {
    console.log(this); //严格模式下，定时器 this 还是指向 window
  }, 2000);  
  ```

### 高阶函数

高阶函数是对其他函数进行操作的函数，它接收函数作为参数或将函数作为返回值输出。

![](E:\qiand\07-10 JavaScript网页编程\04-JavaScript高级资料\JavaScript 高级_day03\4-笔记\images\img2.png)

此时fn 就是一个高阶函数

函数也是一种数据类型，同样可以作为参数，传递给另外一个参数使用。最典型的就是作为回调函数。

同理函数也可以作为返回值传递回来

### 构造函数（类）

构造函数：指的就是通过 `new 函数名()` 调用的函数。

构造函数中的 this，始终是指向 new 出来的实例对象。

```js
function Person() {
    this.name = 'zhangsan'
}
Person.prototype.sayName = function() {
    console.log(this);
}
const p = new Person();
console.log(p.name);//zhangsan
p.sayName();//Person {name: "zhangsan"}
```

#### 箭头函数中this

由于箭头函数中没有 this，因此当我们在箭头函数中使用 this 时，实际上使用的是箭头函数父级的 this。

```js
const student = {
    name: 'student',
    sayName() {
        console.log('1:',this);
        const foo = () => {
            console.log('2:',this);
        }
        foo();
    }
}
const person = {
    name: 'person'
};
person.sayName = student.sayName;
person.sayName();
```

说明：

对象.方法名 指调用(复制)整个方法的代码

对象.方法名() 指定执行这个方法的代码

### 闭包

闭包，指的就是内存中的某一个变量对象，在该销毁（程序不再使用或已经完成使用）的时候，由于其他地方（函数外）还需要使用它的数据，导致该变量对象没有销毁，因此，变量与使用它的函数之间，形成了闭包。这个函数，也称为闭包函数。

闭包（closure）指有权访问另一个函数作用域中变量的函数。简单理解就是 ，一个作用域可以访问另外一个函数内部的局部变量。 

![image-20210912194710103](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912194710103.png)

```js
function foo() {
    var a = 2;
    function bar() {
        console.log(a);
    };
    return bar;
}
const bar = foo();
bar();
```

#### 变量的作用域复习

变量根据作用域的不同分为两种：全局变量和局部变量。

1. 函数内部可以使用全局变量。
2. 函数外部不可以使用局部变量。
3. 当函数执行完毕，本作用域内的局部变量会销毁。

#### 闭包的作用

```js
function fn() {
   var num = 10;
   function fun() {
       console.log(num);
 	}
    return fun;
 }
var f = fn();
f();
```



#### 闭包的优缺点

1. 缺点：滥用闭包会导致内存浪费
2. 优点：延长了变量的作用时间

执行函数

1.变量不是我的

2.只能我用

这个变量和我就是闭包关系。

普通函数

1.这个是大家的变量（全局）

2.我和其他人都能用

### 同步与异步

#### 概念

同步：指的是在同一个时间段内，只能做一件事情，必须等到上一件事情完成后，才能进行下一件事情；

异步：指的是在同一个时间段内，可能同时处理多件事情，也就意味着上一件事情没有完成，并不影响下一件事情的进行；

#### 事件队列

JavaScript 是一门单线程语言。因此，JS 中的异步永远也无法做到在同一个时间点内同时做多件事情，但是 JS 中是可以通过“事件队列”的方式来处理异步。

当它遇到了window的setTimeout和setInterval这样的异步任务，js都默默地先不执行这些回调，而是继续向下执行其他js脚本，等到所有js脚本都解析执行完了，再执行回调。

#### 多回调操作

浏览器是多线程的，js执行线程只是它多个线程中的一个。

当js的执行线程看到了setTimeout，浏览器马上会调用**其他线程**把这个函数中的回调扔到浏览器的事件队列中，事件队列是先入先出的队列。

那么在js执行线程执行完所有脚本空闲的时候，事件队列中的事件回调，会一个一个被拿出来执行。

浏览器有一个内部大消息循环Event Loop（事件循环），会轮询事件队列并处理事件。

```js
console.log("this ");
setTimeout(() => {
    console.log(" is ");
}, 0);
console.log(" jsCode");
//输出 this jsCode is
```

### Ajax

AJAX，Asynchronous JavaScript and XML。它可以实现**与服务端的异步通信**，**局部刷新页面**。

#### AJAX 工作步骤

#### 1. 创建核心对象

创建 XMLHttpRequest 核心对象,后续所有的功能，都是由这个核心对象提供的。

```js
const xhr = new XMLHttpRequest();
```

#### 2. 打开连接

打开浏览器（客户端）与服务端之间的连接。

```js
xhr.open(type, url, isAsync);
```

- type：请求类型（GET、POST…）
- url：前后端连接的路径
- isAsync：是否异步，默认为 true

#### 3. 发送请求

浏览器向服务端发送请求

```js
xhr.send();
```

#### 4. 接收并处理服务端返回的结果

当 readystate 发生改变时，会触发以下事件：

```js
xhr.onreadystatechange = function() {
    if(xhr.readyState === 4 && xhr.status === 200) {
           console.log(xhr.responseText)
    }
}
```

- readystate 用来表示后端的处理进度：

  0：请求未初始化，`xhr.send()` 还未调用；

  1：服务器连接建立，`xhr.send()` 已调用，正在发送请求；

  2：请求已接收，`xhr.send()` 执行完成；

  3：请求处理中

  4：请求已完成

- status 状态码，用来表示请求状态的：

  200：表示成功

  ##### 案例演示

  在线数据接口调用：http://jsonplaceholder.typicode.com/ Jsonplaceholder的测试数据

  http://jsonplaceholder.typicode.com/users可以获取10条用户数据

  ```js
  [
    {
      "id": 1,
      "name": "Leanne Graham",
      "username": "Bret",
      "email": "Sincere@april.biz",
      "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
          "lat": "-37.3159",
          "lng": "81.1496"
        }
      },
      "phone": "1-770-736-8031 x56442",
      "website": "hildegard.org",
      "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
      }
    },
    {
      "id": 2,
      "name": "Ervin Howell",
      "username": "Antonette",
      "email": "Shanna@melissa.tv",
      "address": {
        "street": "Victor Plains",
        "suite": "Suite 879",
        "city": "Wisokyburgh",
        "zipcode": "90566-7771",
        "geo": {
          "lat": "-43.9509",
          "lng": "-34.4618"
        }
      },
      "phone": "010-692-6593 x09125",
      "website": "anastasia.net",
      "company": {
        "name": "Deckow-Crist",
        "catchPhrase": "Proactive didactic contingency",
        "bs": "synergize scalable supply-chains"
      }
    }
     //...
  ]
  ```

  Ajax获取数据

  ```js
  function ajaxGetData(data) {
              var { type, url, isAsync } = data;
              const xhr = new XMLHttpRequest();
              xhr.open(type = "GET", url, isAsync = true);
              xhr.send();
              xhr.onreadystatechange = function () {
                  if (xhr.readyState === 4 && xhr.status === 200) {
                      console.log(JSON.parse(xhr.responseText))
                  }
              }
          }
          ajaxGetData({
              url:"http://jsonplaceholder.typicode.com/users"
          })
  ```

### Promise

#### 异步解决方案的发展

**回调函数：**将一个函数作为参数进行传递，该函数则为回调函数。

**Promise：**ES6提供了Promise对象来更好的解决异步操作。

**async await：**

#### 回调地狱

回调地狱，指的就是回调函数不断进行嵌套，例如

```js
$.ajax({
    url: './data/students.json',
    data: { name },
    success(res) {
        console.log(res[0].classId);
        $.ajax({
            url: './data/classes.json',
            data: { id: res[0].classId },
            success(res) {
                console.log(res[0]);
                $.ajax({
                    url: './data/classes.json',
                    data: { id: res[0].classId },
                    success(res) {
                        console.log(res[0]);
                    }
                })
            }
        })
    }
})
```

为了解决回调地狱的问题，在 ES6 中新增了 Promise。

#### Promise 基本语法

```js
new Promise((resolve, reject) => {
    // 异步代码
    // 如果异步代码请求成功
    resolve();
    // 如果异步代码请求失败
    reject();
})
```

Ajax示例

```js
function ajaxGetData(url) {
    const p = new Promise((resolve, reject) => {
        // 异步代码
        $.ajax({
            url,
            success(res) {
                //console.log(res);
                // 如果异步代码请求成功
                resolve(res);
            }
        })
    })
    return p;
}
ajaxGetData("http://jsonplaceholder.typicode.com/users").then(res=>{
    console.log('then',res);
})
```

**代码说明：**每一个 Promise 对象都有一个 then，该方法又接收一个函数作为参数，该函数的形参就可以用来接收 resolve 传递出来的数据。

关系（操作）

1.一定要有一个promise对象 const p = new promise()

2.一定要有异步程序的处理ajax

3.异步程序在成功回调和失败回调时候，不自己处理，直接传值给固定参数resolve,reject

4.函数调用点接受promise对象并完成.then和catch的函数处理（resolve，reject会自行完成then和catch的回调）

#### Promise对象的三种状态

- pending：等待中

- fulfilled：已成功，调用了 resolve 方法

- rejected：已失败，调用了 reject 方法

  示例

  ```js
  function ajax(URL) {
      return new Promise(function (resolve, reject) {
          var req = new XMLHttpRequest(); 
          req.open('GET', URL, true);
          req.onload = function () {
          if (req.status === 200) { 
                  resolve(req.responseText);
              } else {
                  reject(new Error(req.statusText));
              } 
          };
          req.onerror = function () {
              reject(new Error(req.statusText));
          };
          req.send(); 
      });
  }
  var URL = "http://jsonplaceholder.typicode.com/users"; 
  ajax(URL).then(function (value){
      console.log(JSON.parse(value)); 
  }).catch(function (error){
      document.write('错误：' + error); 
  });
  ```

### async和awaite

async 和 await，是 ES7 新增的内容，号称是异步的终极解决方法。

#### asnyc

async，用来定义一个异步函数。

```js
async function foo() {
    console.log('foo');
}
foo();
console.log('end');
```

**异步函数：**是指函数内部主要用来处理异步代码，不是函数本身变成了异步代码。

异步函数与普通函数的区别在于，异步函数的**返回值是一个 Pormise 对象**，而真正 return 的内容，作为了 Promsie 对象中 resolve 的数据。

#### await

await，用来**等待**一个异步处理结果。

从代码上来看，通常用于等待一个 Promise 对象：

```js
async function foo() {
const res = await new Promise((resolve, reject) => {
    // 异步代码
    $.ajax({
        url: 'http://jsonplaceholder.typicode.com/users',
        success(res) {
            resolve(res);
        }
    })
});
console.log('res', res);
}
foo();
```

注意：await 只能在 async 函数内部使用。

### 内置对象

#### Data

```js
const dt = new Date();
console.log(dt);
const year = dt.getFullYear();
console.log(year + '年');
const month = dt.getMonth()
console.log(month + 1 + '月');
const date = dt.getDate();
console.log(date + '号');
const day = dt.getDay();
console.log('星期' + day);
const hours = dt.getHours();
console.log(hours + '小时');
const minutes = dt.getMinutes();
console.log(minutes + '分');
const seconds = dt.getSeconds();
console.log(seconds + '秒');
```

#### JSON

```js
const students = [
    { name: 'zhangsan' }
]
const studentsJSON = '[ { "name": "zhangsan" } ]';
JSON.parse(studentsJSON);
JSON.stringify();
```

### 深拷贝和浅拷贝

深拷贝和浅拷贝，主要针对的是引用数据类型。

浅拷贝，指的就是拷贝的数据的地址，当其中一个数据发生改变时，另一个数据会受到影响。（引用传值）

```js
const arr = [12, 3, 3];
const arr1 = arr;
arr1[0] = 1;
```

深拷贝，指的就是拷贝的是数据的值，而不是地址，最终拷贝后的两条数据，值是一样的，但是地址是不一样的。

```js
const arr = [12, 3, 3];
const arr1 = [...arr];
```

还可以借助 JSON 对象的方法来实现深拷贝：

```js
const arr = [12, 3, 3];
const arr1 = JSON.parse(JSON.stringify(arr));
```

### for…in 和 for…of

#### for…in（ES5）

for…in 用于遍历对象：

```js
const obj = {
    name: 'zhangsan', age: '20', gender: '男'
}
for(let key in obj) {
    console.log(obj[key])
}
```

#### for…of（ES6）

for…of 用于遍历数组：

```js
const arr = [10, 20, 30];
for(let item of arr) {
    console.log(item);
}
```

### 递归

#### 什么是递归

**递归：**如果一个函数在内部可以调用其本身，那么这个函数就是递归函数。简单理解:函数内部自己调用自己, 这个函数就是递归函数

**注意：**递归函数的作用和循环效果一样，由于递归很容易发生“栈溢出”错误（stack overflow），所以必须要加退出条件return。

#### 利用递归求1~n的阶乘

```js
//利用递归函数求1~n的阶乘 1 * 2 * 3 * 4 * ..n
 function fn(n) {
     if (n == 1) { //结束条件
       return 1;
     }
     return n * fn(n - 1);
 }
 console.log(fn(3));
```

![image-20210912194849654](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210912194849654.png)

#### 利用递归求斐波那契数列

```js
// 利用递归函数求斐波那契数列(兔子序列)  1、1、2、3、5、8、13、21...
// 用户输入一个数字 n 就可以求出 这个数字对应的兔子序列值
// 我们只需要知道用户输入的n 的前面两项(n-1 n-2)就可以计算出n 对应的序列值
function fb(n) {
  if (n === 1 || n === 2) {
        return 1;
  }
  return fb(n - 1) + fb(n - 2);
}
console.log(fb(3));
```

#### 利用递归遍历数据

```js
// 我们想要做输入id号,就可以返回的数据对象
 var data = [{
   id: 1,
   name: '家电',
   goods: [{
     id: 11,
     gname: '冰箱',
     goods: [{
       id: 111,
       gname: '海尔'
     }, {
       id: 112,
       gname: '美的'
     },

            ]

   }, {
     id: 12,
     gname: '洗衣机'
   }]
 }, {
   id: 2,
   name: '服饰'
}];
//1.利用 forEach 去遍历里面的每一个对象
 function getID(json, id) {
   var o = {};
   json.forEach(function(item) {
     // console.log(item); // 2个数组元素
     if (item.id == id) {
       // console.log(item);
       o = item;
       return o;
       // 2. 我们想要得里层的数据 11 12 可以利用递归函数
       // 里面应该有goods这个数组并且数组的长度不为 0 
     } else if (item.goods && item.goods.length > 0) {
       o = getID(item.goods, id);
     }
   });
   return o;
}
```



### Node.JS

#### 概念

Node.js 是一个基于 Chrome V8 引擎的 JavaScript 运行时。Chrome V8 引擎：就是谷歌浏览器厂商开发的一款 JS 引擎，取名“V8”。 V8 引擎是现在公认的解析 JS 代码最快的 JS 引擎。

在 Nodejs 中，引入了 Chrome V8 引擎，就意味着，我们可以在 Nodejs 中去写 JavaScript 代码。

#### Chrome V8引擎

所有的浏览器的内核分为了两类：

- 渲染引擎：负责解析 HTML 和 CSS 代码
- JS 引擎：负责解析 JavaScript 代码

#### 运行时

运行时，指的就是代码的运行环境。

简单来说，Nodejs 就是一个 JavaScript 代码的运行环境。

#### 安装

从 Nodejs 官网去下载对应版本的安装包，安装包的类型是 `.msi`。Nodejs 可以选择安装在任意盘符中。

官网：http://nodejs.cn/

![image-20210729140854236](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210729140854.png)

安装完成后，在终端中输入以下命令来查看 Nodejs 的版本

```
node -vv14.16.1
```

同时检查npm命令，是否也安装好了，npm命令是在装node的时候一并安装的

```
npm -v7.20.2
```

在电脑里新建一个空文件夹，里面新建一个firstNode.js文件，打开编写如下代码：

![image-20210729141935310](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210729141935.png)

在同目录下运行cmd打开终端，打入运行代码`node firstNode.js`

![image-20210729142047073](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210729142047.png)

最终可以在终端显示Hello world

**Node安装成功，并且可以运行程序**

### 终端操作

windows 自带的终端工具，和 VScode 中集成的终端工具，功能是一样的，我们在实际开发中，可以任意选择使用哪一种。

windows 自带的终端工具打开方式：`win + r` 键，输入 `cmd`。

#### 切换路径

**进入下一级目录**

```
cd 目录名
```

**返回上一级目录**

```
cd ..
```

**进入指定目录**

```
cd 目录的绝对路径
```

通常目录的绝对路径可以粘贴复制，也可以直接将文件目录拖入终端中，会自动生成该目录的绝对路径。

还可以根据下图，执行在指定路径打开 cmd 工具：

![image-20210729142827365](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210729142827.png)

#### 快捷键操作

**终端快捷键**

**Tab 自动补全**

不管是文件还是文件夹，名称输入一部分后按下 `Tab` 键后会自动补完整名称。

**查找命令的历史记录**

通过键盘上上下箭头按键，可以查找所有输入过的命令的历史记录。

### 服务器和数据库

#### 服务器通讯过程

![image-20210729152742087](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210729152742.png)

#### 一次完整的 HTTP 事务

描述一次完整的 HTTP 事务，指的就是“用户在浏览器的地址栏中输入 URL 按下回车后，发生了什么？”

##### 1. 域名解析

域名，简单理解为某一个网站的网址。域名解析，指的就是对域名的单词进行解析，找到该域名所对应的服务器的 IP 地址。

**IP 地址**

每一台计算机都有一个唯一的 IP 地址，我们可以通过 IP 地址找到对应的计算机。

查看本机 IP 地址的方式，在终端任意路径中输入以下命令：

```
ipconfig
```

终端显示

![image-20210729153101994](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210729153102.png)

上图中红框中的地址就是本机电脑的 IP 地址。

##### 2. 建立连接

有了 IP 地址后，接下来就需要建立浏览器与服务器之间的连接。

为了保证双方连接的安全性，需要经过“三次握手”来建立连接：

1. 浏览器向服务器发送消息：我想要给你发送请求，你现在处于正常工作状态吗？
2. 服务器给浏览器回消息：我当前是正常的工作状态，你可以给我发送请求。
3. 浏览器向服务器发送消息：好的，我知道了，那我要准备想你发送请求了。

当三次握手完成后，浏览器与服务器之间成功的建立连接。

##### 3. 浏览器发送请求

当双方连接成功后，浏览器将请求发送给服务器，请求服务器将页面代码返回给浏览器。

##### 4. 服务端处理请求

服务器接收到请求后，开始处理请求，并将处理结果返回给浏览器。

##### 5. 断开连接

为了确保数据传递的安全性和完整性，在浏览器和服务器断开连接之前，需要经过“四次挥手”：

1. 浏览器向服务器发送消息：我的数据传输完成了，我想要断开连接了。
2. 服务端向浏览器发消息：你先等一下，我还有数据没有传输完毕。
3. 服务端向浏览器发消息：我现在数据也传输完成了，可以断开连接了。
4. 浏览器向服务器发送消息：好的，我知道了，我要准备断开连接了。

当四次挥手完成之后，浏览器和服务器之间断开连接。

##### 6. 渲染页面

浏览器解析代码，渲染页面。

### 模块化

模块化，将每一个 JS 文件都看作是一个独立的模块，每一个模块都有一个独立的作用域，模块与模块之间，默认情况下不能进行数据的访问。

#### 暴露

一个模块如果想要将内部的数据分享给其他模块使用，需要通过以下代码将数据暴露出去：一个JS文件

```
module.exports.num = 100;module.exports = {    num： 100}
```

#### 引入

一个模块如果想要使用其他模块的数据，需要通过以下代码将数据引入进来： 另一个JS文件

```
const 变量名 = require('引入的模块路径');
```

调用 require 方法后，就可以获取到对应模块暴露的对象。

通常我们可以通过解构赋值的方式直接获取到引入的数据，解构意味着变量名里外要一样

例如：

```
const { num } = require('./a.js')
```

注意：引入的路径，如果是同级关系，路径必须加 `./`。

#### CommonJS

CommonJS，是 JavaScript 在 Nodejs 总需要遵循的服务端规范。也就意味着，CommonJS 规范的语法，都只能在服务端 Nodejs 中使用，不能在浏览器中使用。

### npm

npm，Node.js Package Manager，Nodejs 的包（模块）管理工具。

#### 安装下载

npm 会随着 Nodejs 一并安装。

可以通过以下命令查看 npm 的版本号：

```
npm -v
```

如果没有查看到版本号，说明本机中没有安装 npm，就需要重新安装 Nodejs。

#### 下载包

由于 npm 的服务器在国外，因此我们为了下载速度快，建议设置一下淘宝镜像，在终端执行以下命令：

```js
npm install -g cnpm -registry=https://registry.npm.taobao.org
```

全局下载，就以为在本地电脑的任意目录中都可以使用该功能。

```js
npm install -g 包名称
# 简写
npm i -g 包名称
```

局部下载，在指定路径中执行以下命令，局部下载包，下载成功后，该依赖包的功能只能在当前路径范围内使用。

```js
npm install 包名称 --save
# 简写
npm i 包名称 --save
```

### 创建Express项目

#### 安装Express

#### 安装项目生成器

首先确保本机中安装了 express 的项目生成器，如果没有安装，可以通过以下命令进行全局安装：

```
npm install -g express-generator
```

#### 创建 express 项目

将终端路径定位到想要创建项目的目录中，然后执行以下命令创建 express 服务器项目：

```
express 项目名称
```

#### 下载依赖包

在终端中通过 `cd 项目名称` 进入到项目根目录路径中，然后执行以下命令下载项目所有依赖包：

```
npm i
```

#### 启动项目

在项目根目录路径中执行以下命令启动项目：

```
npm start
```

#### 访问项目

在浏览器中通过 `IP:端口` 方法服务器，如果是自己访问自己，IP 可以写成 `localhost`。每一个人访问自己的 express 服务器时，都可以通过 `localhost:3000` 来访问。

默认端口是3000

### Express项目结构

#### 目录结构

- `node_modules`：存放所有通过 npm 下载的项目依赖包，在执行 `npm install` 时该文件会自动生成。
- `package.json`：项目说明文件，里面包含项目的一些基本信息，例如：项目名称、项目版本、项目依赖包等。
- `package-lock.json`：项目说明文件，里面包含了整个项目所有依赖包的完整信息，在执行 `npm install` 时该文件会自动生成。
- `bin/www`：创建服务器，运行该文件可以启动服务器。
- `routes`：该目录中的所有 JS 文件，都是用来**配置**后端**路由**，处理前端发送过来的请求。
- `views`：后端模板引擎，在后端处理页面节点和数据的渲染。
- `public`：用来存放静态资源，其实就是前端代码，包括 HTML、CSS、JS、图片、字体等。
- `app.js`：服务端项目的入口文件，用于配置服务器。

#### 更换项目启动方式

将 `app.js` 文件的最后一行代码更换为以下代码：

```
app.listen(3000, () => console.log('3000 端口服务器启动成功'));
```

更改完成后，项目的启动命令，从 `npm start` 更换为以下命令：

```
node app.js
```

后续再关闭服务器，就只需要 `ctrl + c` 就可以了。

#### 第三方组件服务器管理

#### nodemon

电脑性能好一点的，可以选择安装 `nodemon` 插件，来帮助我们自动重启服务器。

全局安装：

```
npm i -g nodemon
```

安装完成后，以后启动项目想要通过插件启动，就使用以下命令：

```
nodemon app.js
```

该插件是根据代码保存来识别是否重启，所以建议将 VSCode 的自动保存关闭。

### 前后端交互流程

#### 前端发送请求

前端在对应的页面中，发送 AJAX 请求

在Express的public里新建一个login.html表单页面,Js部分书写如下代码

```js
$('#loginBtn').click(function() {
    const username = $('#username').val();
    const password = $('#password').val();
    $.ajax({
        // 前后端接口
        url: '/users/login',
        type: 'POST',
        data: {
            username, password
        },
        success(res) {
            console.log('后端返回结果：', res);
        }
    })
})
```

其中，URL 需要跟后端进行匹配，匹配成功后，才能成功的将请求发送到后端。

在以后的开发中，URL 接口可以从接口文档中去查找，或者找后端程序员要。现阶段，URL 需要我们自己定义。

URL 命名的规则，由一级接口和二级接口组成。其中，一级接口用来表示要操作的数据名称，二级接口用来表示对该数据的具体操作。例如

- 用户的登录：`/users/login`
- 新增学生：`/students/addStudents`

#### 后端分发请求

##### 一级接口匹配

前端发送的请求，首先需要在 `app.js` 中进行一级接口的匹配：

```js
// ...
var indexRouter = require('./routes/index.js');
var usersRouter = require('./routes/users');
// ...
app.use('/', indexRouter);
app.use('/users', usersRouter);// ...var indexRouter = require('./routes/index.js');var usersRouter = require('./routes/users');// ...app.use('/', indexRouter);app.use('/users', usersRouter);
```

当 AJAX 请求的一级接口和后端匹配成功后，进入到对应的 JS 文件，例如登录接口`/users/login` 匹配到 `/users`，然后进入 `./routes/users.js` 文件中。

##### 二级接口和请求类型匹配

```js
router.post('/login', function(req, res, next) {
      console.log('进入登录接口');
});
```

当请求类型和二级接口匹配成功后，就会执行对应的回调函数。我们就可以在函数中对当前的请求进行处理。

#### 返回结果给前端

后端请求处理完成后，需要将处理结果返回给前端：

```js
router.post('/login', function(req, res, next) {
      // 处理登录请求 ...
      // 后端发送处理结果给前端
      res.send({
          message: '登录成功',
          code: 200
      });
});
```

说明：通常后端发回给前端的数据至少要包含两个信息：

- 请求结果的文字描述
- 请求结果的数字描述

#### 前端处理请求结果

最后，`res.send` 方法返回的值，会发送到前端 AJAX 的 success 方法的参数 `res` 中去。

```js
$.ajax({
    // 前后端接口
    url: '/users/login',
    type: 'POST',
    data: {
        username, password
    },
    success(res) {
        console.log('后端返回结果：', res);
        if(res.code == 200) {
            alert('恭喜你，登录成功')
        } else {
            alert('账号或密码错误，登录失败')
        }
    }
})
```

#### 总代码

public目录下login.html（需要在js文件中先导入JQuery）

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <script src="./js/jquery.min.js"></script>
</head>
<body>
    用户名：<input type="text" id="username"> 
    密码：<input type="text" id="password"> 
    <button id="loginBtn">提交</button>
    <script>
        $("#loginBtn").click(function(){
            const username = $("#username").val();
            const password = $("#password").val();
            $.ajax({
                url:"/users/login",
                type:'post',
                 data:{username,password},
                success(res){
                    console.log('后端返回结果',res);
                }
            })
        })
    </script>
</body>
</html>
```

routes目录里users.js

```js
var express = require('express');
var router = express.Router();
/* GET users listing. */
router.post('/login', function(req, res, next) {
    console.log(req.body.username,req.body.password);
    res.send({
        code:200,
        message:'登录成功'
    })
});
module.exports = router;
```

特别注意post和get的接受方式

app.js

```js
var usersRouter = require('./routes/users');
app.use('/users', usersRouter);

```

呈现效果

![image-20210731181203210](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210731181203.png)

![image-20210731181213653](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210731181213.png)

### MongoDB

#### 数据库的分类

关系型数据库：MySQL，SQLServer

非关系型数据库Nosql：MongoDB

关系型和非关系型数据库的主要差异是数据存储的方式。关系型数据天然就是表格式的，因此存储在数据表的行和列中

与其相反，非关系型数据不适合存储在数据表的行和列中，而是大块组合在一起。非关系型数据通常存储在数据集中，就像文档、键值对或者图结构

#### 安装

官方网站下载 https://www.mongodb.com/try/download

#### 下载图形化管理工具

http://www.navicat.com.cn/download/navicat-premium

下载注册机进行破解

#### mongoose

在 Nodejs 的 Express 的项目中，我们使用 mongoose 的插件来操作 MongoDB 数据库。

在项目根目录中执行以下命令局部安装 mongoose：

```
npm i mongoose --save
```

#### 连接数据库

将 Express 与 MongoDB 服务器中的某一个数据库关联起来。

在 `app.js` 中设置以下代码，来连接数据库：

```js
var logger = require('morgan');
//连接数据库-start
const mongoose = require('mongoose');
// 数据库地址
const dbURL = 'mongodb://localhost:27017/woniuxy'
mongoose.connect(dbURL, { useNewUrlParser: true, useUnifiedTopology: true })
mongoose.connection.on('connected', () => console.log(dbURL + ' 数据库连接成功'));
//连接数据库-end
var studentsRouter = require('./routes/students');
var usersRouter = require('./routes/users');
```

其中，dbURL 中的 `woniuxy` 是要连接的数据库名称，以后根据情况自行更改。连接的数据库可以是不存在，后续在使用会自动创建出来。

27017是mongodb的默认数据库端口

`{ useNewUrlParser: true, useUnifiedTopology: true }`是兼容参数

`mongoose.connection.on`是连接绑定事件，`connected`是连接后的系统触发事件。

#### 集合配置

当我们通过代码想要去操作一个集合中的数据时，需要先进行以下配置：

设置数据结构

```js
var express = require('express');
var router = express.Router();
//配置数据结构
const { Schema, model } = require('mongoose');
//Schema是数据结构对象
const usersSchema = new Schema({
    username: String,
    password: String
}, { versionKey: false });
//设置数据模型
const usersModel = model('usersModel', usersSchema, 'users');
/**
 * model三个参数
 * userModel:程序中需要用到的模型名称
 * userSchema:数据结构对象名称
 * users:数据中对应集合的名称
 */
/* GET users listing. */
router.post('/login', function(req, res, next) {
    //console.log(req.body.username,req.body.password);
```

数据模型参数说明：

- `'usersModel'`：模型名称，自定义的字符串

- `usersSchema`：数据结构 Schema 的对象名称

- `'users'`：在数据库集合的名称

  { versionKey: false } 是自动徐桥版本关键字段_id

### MpongDB数据库操作

#### 数据操作

所有的数据操作方法，都是数据模型提供的

#### 按条件查询数据

执行代码写在route文件夹的users.js里

```js
/* GET users listing. */
router.post('/login',async function(req, res, next) {
    //前端发送过来的账户和密码
    //console.log(req.body.username,req.body.password);
    const {username,password} = req.body;
    console.log(username,password);
    const result = await usersModel.find({username, password});
    console.log(result);
    if(result.length >0){
        res.send({
            code:200,
            message:'登录成功'
        })
    }else{
        res.send({
            code:500,
            message:'登录失败'
        })
    }
});
```

所有数据方法返回的都是promise对象，可以使用await和async来异步操作

```
await usersModel.find({ username: '1', password: '1' })
```

`find()` 可以接收一个对象作为参数，该对象就是我们的查询条件。

#### 查询所有数据

```
await usersModel.find()
```

#### 关联查询

```js
// 并列关联
await studentsModel
    .find()
    .populate('classesId')
    .populate('teachersId')
// 嵌套关联
await studentsModel
    .find()
    .populate({
        path: 'classesId',
        populate: {
            path: 'teachersId'
        }
    })
```

#### 新增数据

```
await usersModel.create({ username: '2', password: '2' })
```

执行代码写在route文件夹的users.js里

```js
router.post('/register', async function(req, res, next) {
    //console.log(req.body.username,req.body.password);
    const data = req.body; // 如果接受get req.query
    //数据模型
    const result =  await usersModel.create(data);
    console.log('注册结果:',result);//会返回给我一个新注册记录的ID
    res.send({
        code:200,
        message:'登录成功'
    })
});
```

#### 按条件删除数据

```js
await usersModel.deleteOne({ _id: '60b9f146270853224c3b0a63' })
await usersModel.deleteMany({ username: '1' })//username=1的记录全部清楚掉
const result = await usersModel.deleteMany({ age:{ $gte:15 } })//代表age>=15 全部删除
```

`deleteOne()` 可以接收一个对象作为参数，该对象就是我们要删除的数据的条件。

#### 按条件修改数据

```js
await usersModel.updateOne({_id: '60b9f146270853224c3b0a63'}, { username: 'zhangsan', password: '123' })
const result = await usersModel.updateOne({username:"zhangsan"}, { password: '125' });
```

`updateOne()` 接收两个对象作为参数，第一个对象是查询条件，第二个对象的要修改的新数据。

说明：当没有修改的时候result返回没有{ n: 1, nModified: 0, ok: 1 } 修改值为0

### MVC架构模式

**架构模式主要分为两种：**

- MVC：Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，一种软件设计典范
- 三层架构：界面层（User Interface layer）、业务逻辑层（Business Logic Layer）、数据访问层（Data access layer）

#### 目录结构

##### models

在项目根目录创建一个 `models` 文件，用来管理所有关于数据相关配置代码。每一个类型的数据对应一个 js 文件，例如：

- 用户的数据模型：`models/usersModel.js`
- 学生的数据模型：`models/studentsModel.js`

在以上这些文件中，都用来进行数据结构和数据模型的配置，例如：

```js
const { Schema, model } = require('mongoose');
const usersSchema = new Schema({
    username: String,
    password: String
}, { versionKey: false });
// 配置数据模型
module.exports.usersModel = model('usersModel', usersSchema, 'users');
```

##### controllers

在项目根目录创建一个 `controllers` 文件，用来管理所有业务逻辑和数据操作的代码。每一个类型的数据的操作对应一个 js 文件，例如：

- 用户的业务：`controllers/usersConroller.js`
- 学生的业务：`controllers/students.js`

在以上这些文件中，都是用来处理请求的业务逻辑和对数据的操作

```js
// 引入模型
const { usersModel } = require('../models/usersModel')
async function login(req, res, next) {
    // 处理登录请求
    // 1. 接收前端发送到后端的数据（账号密码）
    const data = req.body;
    // console.log('前端发送的账号密码：', data);  // { username: 123, userpass: 123 }
    // 2. 在数据库中查询是否有该条数据
    const result = await usersModel.find(data);
    // const result = await usersModel.find({ username: data.username, password: data.userpass });
    // console.log('数据库查询的结果：', result);
    if (result.length > 0) {
        // 后端发送处理结果给前端
        res.send({
            message: '登录成功',
            code: 200
        });
    } else {
        // 后端发送处理结果给前端
        res.send({
            message: '登录失败',
            code: 500
        });
    }
}
async function register(req, res, next) {
    // ...    
}
// 暴露方法给 routes 中使用
module.exports = {
    login, register
}
```

##### routes

routes 目录作为我们的 V 层，主要用于和前端进行交互，匹配前端的接口。

```js
var express = require('express');
var router = express.Router();
// 引入 controller
const { login, register } = require('../controllers/users')
router.post('/login', login);
router.post('/register', register);
module.exportrouter;
```

### MVC分页

#### 分页规则

分页可以是后端的根据分页要求做的返回，也可以是前端获取全部数据根据分页要求的截取操作。

#### 操作步骤

##### 01.设定网页html标签

在index.html里找到分页位置，添加id

```js
<div class="content-row" style="text-align: center;">
    <button>首页</button>
    <button>上一页</button>
    <button id="nextPage">下一页</button>
    <button id='lastPage'>尾页</button>
</div>
```

##### 02,js代码设定

在js文件夹students.js中设定 全局变量

```js
//分页数据
const pageData = {
    currentPage:1, //当前页
    pageSize:3,//每页显示条数
    total:0,//总页数
    pages:0//总条数
}
```

##### 03.获取学员getStudents方法

ajax data传参给服务器，并设置返回总条数，总页数

```js
//搜索和全部获取列表合并操作
function getStudents() {
    return new Promise((resolve, reject) => {
        //请求数据
        $.ajax({
            url: '/students/getStudents',
            type: 'GET',
            data: {
                ...searchData,
                //分页数据
                currentPage:pageData.currentPage,
                pageSize:pageData.pageSize
            },
            success({ code, data }) {
                if (code == 200) {
                    //resolve(data);
                    //获取到的翻页数据放到全局上面去
                    pageData.total = data.total;//总条数
                    pageData.pages = data.pages;//总页数
                    resolve(data.result);
                }
            }
        })
    })
}
```

##### 04.服务器controller获取数据并查询

结构数据

```js
//解构数据
const { type, value, currentPage, pageSize } = data;
```

查询数据

```js
 result = await studentsModel.find().limit(pageSize - 0).skip((currentPage - 1) * pageSize);
```

### MV模糊查询

模糊查询就是让搜索功能可以只输入一部分的查询功能

#### 模糊查询原理

利用**正则表达式**来完成搜索功能的查找

已学生模块搜索为例：修改controller里的students.js代码

原先的精确查找

```js
result = await studentsModel.find({ [data.type]: value });
```

现在改成

```js
result = await studentsModel.find({ [data.type]: { $regex: value, $options: '$i' } })
```

再配合上分页

```js
 result = await studentsModel.find({ [data.type]: { $regex: value, $options: '$i' } }).limit(pageSize - 0).skip((currentPage - 1) * pageSize);
```

完整代码:

```js
async function getStudents(req, res, next) {
    try {
        //和搜索合并后的操作
        const data = req.query;
        console.log(data);
        //分页
        //解构数据
        const { type, value, currentPage, pageSize } = data;
        //做翻页时需要使用，获取总条数
        //const total = await studentsModel.countDocuments();//mongoose提供的方法，依然返回Promist对象
        //分页后显示总条数
        const total = await studentsModel.countDocuments({ [data.type]: { $regex: value, $options: '$i' } });
         //计算总页数
         const pages = Math.ceil(total / pageSize);
        //[data.type]：如果对象的key是变量，就需要用[]括起来
        let result = "";
        // console.log('data:', data)
        result = await studentsModel.find({ [data.type]: { $regex: value, $options: '$i' } }).limit(pageSize - 0).skip((currentPage - 1) * pageSize);
/*
//空字符串包含在所有字符串中
        if (value) {//搜索，传值
            //精确查找
            //result = await studentsModel.find({ [data.type]: value });
            //正则模糊查询
            //$options: '$i' 忽略大小写
            result = await studentsModel.find({ [data.type]: { $regex: value, $options: '$i' } });
        } else {
            //获取所有
            //result = await studentsModel.find();
            //获取部分数据<limit></limit>
            result = await studentsModel.find().limit(pageSize - 0).skip((currentPage - 1) * pageSize);
            console.log('result:', result);
        }
*/
        //搜搜全部数据
        //const result = await studentsModel.find()
        res.send({
            message: '获取学生数据成功！',
            code: 200,
            data: { result, total, pages }
        })
    } catch (error) {
        console.log('error', error);
        res.send({
            message: '获取学生数据失敗',
            code: 500,
            data: []
        })
    }
}
```

### MVC获取渲染专业

#### 项目需求

在项目操作过程中，在添加学生界面，修改“学生班级”改为“学生专业”字段，并在打开时自动加载显示可选学生，如图：

![image-20210803145343921](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210803145350.png)

#### 操作步骤

##### 01.public/js 文件夹新增subjects.js文件

```js
//获取所有专业
//getSubjects();
showSubjects();
async function showSubjects(){
    const subjectsData = await getSubjects();
    renderSubjects(subjectsData);
}
//数据获取
function getSubjects(){
   return  new Promise((resolve,reject)=>{
        $.ajax({
            url:'/subjects/getSubjects',
            success(res){
                //console.log('专业数据',res);
                if(res.code == 200){
                    resolve(res.data)
                }
            }
        })
    })
}
//渲染页面
function renderSubjects(data){
    const html = data.map(item=>(`<option value="${item._id}">${item.name}</option>`)).join('');
    $('#addSubjects').html(html);    
}
```

##### 02.后端服务器app.js增加一级目录配置

```js
const subjectsRouter = require('./routes/subjects')
app.use('/subjects', subjectsRouter);
```

##### 03.在controller目录下新增subjects.js文件

```js
const {subjectsModel} =  require('../models/subjectsModel');
 async function getSubjects(req, res, next) {
     const result = await subjectsModel.find();
     res.send({
         message:'专业数据获取成功',
         code:200,
         data:result
     })
}
module.exports = {
    getSubjects
}
```

##### 04.在Model文件夹下新增subjectsModel.js文件

```js
//引入mongoose
const { Schema, model } = require('mongoose');
//创建数据结构
const subjectsSchema = new Schema({
    name: String,
}, { versionKey: false })
//创建模型对象
const subjectsModel = model('subjectsModel', subjectsSchema, 'subjects')
//暴露模块
module.exports = {
    subjectsModel
}
```

##### 05.在route目录下新增subjects.js

```js
var express = require('express');
var router = express.Router();
const {getSubjects} = require('../controllers/subjects');
/* GET home page. */
router.get('/getSubjects', getSubjects);
module.exports = router;
```

### MVC学生和专业关联

在学员列表显示时需要关联专业选项。这时就需要设计到多集合联查，如图效果

![image-20210803171522792](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210803171522.png)

#### 制作过程

**以学员查询为例：在Controller中的students.js修改代码**

```js
  //populate用于关联查询
result = await studentsModel.find({ [data.type]: { $regex: value, $options: '$i' } }).populate('subjectsId')
        .limit(pageSize - 0).skip((currentPage - 1) * pageSize);
```

在查询代码中添加.populate()方法，需要的参数“subjectsId”是数据库关联的字段名称

**确保studentsModel代码的关联代码的存在**

```js
const studentsSchema = new Schema({
    name: String,
    age: String,
    gender: String,
    //关联专业ID
    subjectsId:{
        type: Schema.Types.ObjectId,//指定类型
        ref:'subjectsModel' //关联集合的模型名称，这个名称就是subjectsModel中const subjectsModel = model('subjectsModel', subjectsSchema, 'subjects') 的第一个参数
    }   
}, { versionKey: false })
```

**渲染页面(可以判断数据是否存在）**

```js
//渲染数据 提取出
function renderStudents(data) {
    const html = data.map(item => (`
              <tr>
                  <td>${item._id} </td>
                  <td>${item.name}</td>
                  <td>${item.age}</td>
                  <td>${item.gender}</td>
                  <td>${item.subjectsId?item.subjectsId.name:"暂无"}</td>
                  <td></td>
                  <td></td>
                  <td>
                      <a href="#" data-id="${item._id}" class="deleteBtn">刪除</a>
                      <a href="#/studentsUpdate" data-id="${item._id}" class="updateBtn">修改</a>
                  </td>
              </tr>
          `)).join('')
    $('#studentsTb').html(html)
    //显示页面总数
    $('#total').text(pageData.total);
}
```

### MVC新增班级关联专业

#### 新增班级制作流程

设定数据库班级集合的名称为:classes

##### 01.新建model（classesModel.js）

```js
const { Schema, model } = require('mongoose');
const classesSchema = new Schema({
    name:String,
    subjectsId:{
        type:Schema.Types.ObjectId,
        ref:'subjectsModel'
    }
}, { versionKey: false });
// 配置数据模型
const classesModel = model('classesModel', classesSchema, 'classes');
//module.exports.classesModel = classesModel;
module.exports = {
    classesModel
}
```

说明：班级关联学科subjectsModel，所以添加subjectsId关联字段

##### 02.修改html页面

```js
  <!-- 新增班级 -->
                <div class="section-content form-content" id="classesAdd">
                    <h2>新增班级</h2>
                    <div class="content">
                        <div class="content-info">
                            <h3>新增数据</h3>
                            <div>
                                <div>
                                    <div class="content-row">
                                        <label>班级名称：</label>
                                        <input class="form-input" type="text" id="addClassesName">
                                    </div>
                                    <div class="content-row">
                                        <label>所属专业：</label>
                                        <select id="selectSubjects">
                                        </select>
                                    </div>
                                    <div class="content-row" style="margin-top: 50px;">
                                        <label></label>
                                        <button class="blue" id="addClassesBtn">确认新增</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
```

##### 03.新建js（classes.js）

```js
//新增班级
$('#addClassesBtn').click(function(){
    const name = $('#addClassesName').val();
    const subjectsId = $("#selectSubjects").val();
    $.ajax({
        url:'/classes/addClasses',
        type:'post',
        data:{
            name,subjectsId
        },
        success(res){
            console.log('新增班级结果：',res);            
        }
    })
})
```

##### 04.配置app.js一级标签

```js
const classesRouter = require('./routes/classes')
app.use('/classes', classesRouter);
```

##### 05.新建controller（classes.js）

```js
const { classesModel } = require('../models/classesModel');
async function addClasses(req, res, next) {
    console.log(req.body);
    const result = await classesModel.create(req.body);
    res.send({
        code:200,
        message:'班级新增成功'
    })
}
module.exports = {
    addClasses
}
```

##### 06.操作演示

![image-20210803192047251](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210803192047.png)

数据库

![image-20210803192104611](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210803192104.png)

前端数据获取

![image-20210803192128998](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210803192129.png)

### MVC专业和班级联动

#### 操作流程

##### 01.index.html页面修改

在新增学员板块里面修改代码

```js
<div class="content-row">
    <label>选择专业：</label>
    <select class="form-input" id='addSubjects'>
    </select>
</div>
<div class="content-row">
    <label>选择班级：</label>
    <select class="form-input" id='addClasses'>
    </select>
</div>
```

分别设置两个ID：addSubjects，addClasses

##### 02.在classesModel里添加subjectId

```js
const { Schema, model } = require('mongoose');
const classesSchema = new Schema({
    name:String,
    subjectsId:{
        type:Schema.Types.ObjectId,
        ref:'subjectsModel'
    }
}, { versionKey: false });
// 配置数据模型
const classesModel = model('classesModel', classesSchema, 'classes');
//module.exports.classesModel = classesModel;
module.exports = {
    classesModel
}
```

##### 03.在controller里的students.js增加

```js
     result = await studentsModel.find({ [data.type]: { $regex: value, $options: '$i' } })
        .populate('subjectsId')
        .populate('classesId')
        .limit(pageSize - 0)
        .skip((currentPage - 1) * pageSize);
```

##### 04.在public的js里的students.js

渲染显示学生数据时绑定学员数据

```js
//渲染数据 提取出
function renderStudents(data) {
    const html = data.map(item => (`
              <tr>
                  <td>${item._id} </td>
                  <td>${item.name}</td>
                  <td>${item.age}</td>
                  <td>${item.gender}</td>
                  <td>${item.subjectsId?item.subjectsId.name:"暂无"}</td>
                  <td>${item.classesId?item.classesId.name:"暂无"}</td>
                  <td></td>
                  <td>
                      <a href="#" data-id="${item._id}" class="deleteBtn">刪除</a>
                      <a href="#/studentsUpdate" data-id="${item._id}" class="updateBtn">修改</a>
                  </td>
              </tr>
          `)).join('')
    $('#studentsTb').html(html)
    //显示页面总数
    $('#total').text(pageData.total);
}//渲染数据 提取出function renderStudents(data) {    const html = data.map(item => (`              <tr>                  <td>${item._id} </td>                  <td>${item.name}</td>                  <td>${item.age}</td>                  <td>${item.gender}</td>                  <td>${item.subjectsId?item.subjectsId.name:"暂无"}</td>                  <td>${item.classesId?item.classesId.name:"暂无"}</td>                  <td></td>                  <td>                      <a href="#" data-id="${item._id}" class="deleteBtn">刪除</a>                      <a href="#/studentsUpdate" data-id="${item._id}" class="updateBtn">修改</a>                  </td>              </tr>          `)).join('')    $('#studentsTb').html(html)    //显示页面总数    $('#total').text(pageData.total);}
```

### 图片上传

图片上传，实际就是本机电脑中的图片复制一份上传到服务器中。

例如我们用 express 搭建的服务器，上传图片时，就是将本地的图片复制到 express 项目的 public 目录中。

#### 前端处理

##### 01.提供文件选择功能

html 中通过以下标签，可以打开文件选择框：

```
<input type="file" id="uploadImages"/>
```

##### 02.设置 change 事件

```js
$('#uploadImages').change(function() {   
console.log('图片上传');
})
```

##### 03.获取用户选择的图片信息

```js
$('#uploadImages').change(function (e) {    
const files = e.target.files;    console.log(files);
})
```

注意：只有原生 DOM 节点上，才能通过 `files` 属性获取图片信息。

![image-20210806221407900](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210806221408.png)

#### 04.处理图片数据的格式

```js
const fd = new FormData();fd.append('file', files[0]);
```

需要将图片信息添加到表单对象中，然后再将表单对象发送给后端。

#### 05.通过 ajax 发送表单对象

```js
$.ajax({
    url: '/images/uploadImages',
    type: 'POST',
    data: fd,
    contentType: false,
    processData: false,
    cache: false,
    success(res) {
        console.log('上传结果', res);
    }
})
```

`contentType`、`processData` 等属性，都是为了让 jQuery 的 ajax 不要对 data 中的数据格式做额外的处理。

#### 后端处理

##### 01.下载 multer

图片上传需要用到 multer 的插件，所以需要先在项目中局部安装该插件：

```
npm i multer --save
```

##### 02.上传图片

```js
const { uploadFiles } = require('../utils/handleFiles')
router.post('/uploadImages', function (req, res, next) {
    // 图片上传
    uploadFiles({
        // 图片上传成功后的存储路径
        path: './public/assets',
        // key: 'file',
        // size: 1000
    });
});
```

##### 03.获取上传成功后的图片信息

```js
router.post('/uploadImages', function (req, res, next) {
    // 图片上传
    const uploadImages = uploadFiles({
        // 图片上传成功后的存储路径
        path: './public/assets',
        // key: 'file',
        // size: 1000
    });
    uploadImages(req, res, (error) => {
        if(error) {
            console.log('图片上传失败', error);
        } else {
            console.log('图片上传成功');
            // 输出上传成功后的图片信息
            console.log(req.files);
        }
    });
});
```

##### 04. 后端返回图片信息给前端

```js
uploadImages(req, res, (error) => {
    if(error) {
        console.log('图片上传失败', error);
    } else {
        console.log('图片上传成功');
        // 输出上传成功后的图片信息
        console.log(req.files);
        res.send({
            message: '图片上传成功',
            code: 200,
            data: './assets/' + req.files[0].filename
        })
    }
});
```

##### 5. 前端接收到数据后渲染图片

```js
$.ajax({
    url: '/images/uploadImages',
    type: 'POST',
    data: fd,
    contentType: false,
    processData: false,
    cache: false,
    success(res) {
        if(res.code == 200) {
            $('#images').attr('src', res.data);
        }
    }
})
```

### 身份认证

身份认证，在项目中某一些页面需要用户登录后才能进行访问，因此，在进入这些页面之前，需要对用户的身份进行认证，需要判断用户是否有登录。

实现身份认证的方式主要有两种：

- cookie 和 session
- localStorage 和 JWT（jsonwebtoken）

#### 身份认证的流程

![image-20210807094403894](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210807094410.png)

#### 1. 前端发送登录请求

#### 2. 后端处理登录请求，判断用户是否登录成功

#### 3. 判断登录成功后，后端生成 token

需要使用以下插件来生成 token：

```
npm i jsonwebtoken --save
```

下载成功后，引入该模块，调用方法生成 token：(可以放在controller的比如user.js中，即登录成功时)

```js
const jwt = require('jsonwebtoken');
//登录成功操作里
// 生成 token
const token = jwt.sign(
    { user: result[0] }, //  用户信息
    'hello',  // 密钥，任意字符串
    { expiresIn: 10 } // 设置有效期
)
```

#### 4. 后端将 token 返回给前端

```js
// 后端发送处理结果给前端
res.send({
    message: '登录成功',
    code: 200,
    token: 'Bearer ' + token
});
```

说明：因为我们使用的后端 token 的验证插件，验证规则要求 token 前必须拼接一个 `'Bearer '` 字符串。

#### 5. 前端保存 token

```js
$.ajax({
    // 前后端接口
    url: '/users/login',
    type: 'POST',
    data: {
        username, password
    },
    success(res) {
        console.log('后端返回结果：', res);
        if(res.code == 200) {
            localStorage.token = res.token;
            alert('恭喜你，登录成功')
        } else {
            alert('账号或密码错误，登录失败')
        }
    }
})
```

#### 6. 验证本地是否有 token

先在js文件夹下创建一个auth.js文件夹

在index.html中引入auth.js，需要放在jquery引入后。但在其他js引入之前

```js
<script src="./js/jquery.min.js"></script>
    <!-- 引入token验证文件 -->
    <script src="./js/auth.js"></script>
    <!-- 左侧菜单点击事件 -->
    <script src="./js/sidebar.js"></script>
    <script src="./js/subjects.js"></script>
    <script src="./js/students.js"></script>
    <script src="./js/classes.js"></script>
    <script src="./js/images.js"></script>
```

进入到需要登录的页面时，需要先判断本地存储中是否有 token：auth.js里面编写如下代码

```js
const token = localStorage.token;
if(token) {
    // 本地有 token
} else {
    alert('你还未登录，请先登录');
    location.href = "../login.html";
}
```

#### 7. 发送 token 到后端，验证 token

如果前端的本地存储中有 token，接下来就需要通过 ajax 将 token 发送到后端，让后端来验证 token 的有效期。

token 需要通过“请求头”发送给后端：

修改autho.js代码

```js
const token = localStorage.token;
if(token) {
    $.ajax({
        url: '/users/getUserInfo',
        type: 'POST',
        headers: {
            'Authorization': token
        },
        success(res) {
            console.log('用户信息', res);
        }
    })
} else {
    alert('你还未登录，请先登录');
    location.href = "../login.html";
}
```

#### 8. 后端验证 token，下载验证插件

express 的后端中，用到的 token 验证插件是 `express-jwt`，因此，执行以下命令下载该插件：

```
npm i express-jwt --save
```

#### 9. 配置 token 的验证规则

在 `./utils` 目录中，创建一个 `auth.js` 文件，用来配置 token 的验证信息：

```js
const expressJWT = require('express-jwt');
const jwtAuth = expressJWT({
    secret: 'hello',
    algorithms: ['HS256'], // 设置 jwt 的算法
    // 设置为 false，表示如果不带 token 的请求，不进行验证
    // 设置为 true，表示请求带不带 token 都要验证，如果不带 token 的请求，直接验证失败
    credentialsRequired: false
}).unless({
    // 不需要进行验证的接口
    path: ['/users/login', '/users/register']
})
module.exports = jwtAuth;
```

#### 10. 应用验证规则

在 app.js 中引入前面配置好的验证规则，应用该规则，让其生效：

```js
const jwtAuth = require('./utils/auth')
// 让 token 验证规则生效
// 一级接口之前
app.use(jwtAuth);
app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/students', studentsRouter);
app.use('/subjects', subjectsRouter);
app.use('/classes', classesRouter);
app.use('/images', imagesRouter);
```

#### 11. 前端处理 401 报错

当后端验证失败时，会直接返回 401 的报错，前端 ajax 通过对 401 的判断，来跳转登录页面：

在js文件夹中的auth.js

```js
$.ajax({
    url: '/users/getUserInfo',
    type: 'POST',
    headers: {
        'Authorization': token
    },
    success(res) {
        console.log('用户信息', res);
    },
    error(err) {
        if(err.status == 401) {
            alert('登录已过期，请重新登录');
            location.href = "../login.html";
        }
    }
})
```

#### 12. token 验证成功，解码 token

当后端验证成功时，ajax 请求会继续往后执行，我们就可以在后端继续处理请求。例如：获取用户信息。

```js
function getUserInfo(req, res) {
    // 获取请求头中的 token,拆分字符串把之前拼接的去掉
    const token = req.get('Authorization').split(' ')[1];
    // 解码 token
    const { user } = jwt.verify(token, 'hello');
    res.send({
        message: '用户信息获取成功',
        code: 200,
        data: user
    })
}
```

#### 13. 统一给所有 ajax 添加 token

在登录成功后，用户发送的每一个 ajax 请求，我们依然要去验证用户的身份信息，确保在使用过程中 token 没有过期，一旦过期，也会随时提示用户重新登录。 代码加在JS的auth.js里

```js
// 统一给ajax添加请求头
const token = localStorage.token;
if (token) {
    $.ajaxSetup({
        headers: {
            'Authorization': token
        },
        error(err) {
            if (err.status == 401) {
                alert('登录已过期，请重新登录');
                location.href = "../login.html";
            }
        }
    })
} else {
    alert('你还未登录，请先登录');
    location.href = "./login.html";
}
```

最终JS下的auth.js代码如下：

```js
// 统一给ajax添加请求头
const token = localStorage.token;
if (token) {
    $.ajaxSetup({
        headers: {
            'Authorization': token
        },
        error(err) {
            if (err.status == 401) {
                alert('登录已过期，请重新登录');
                location.href = "../login.html";
            }
        }
    })
} else {
    alert('你还未登录，请先登录');
    location.href = "./login.html";
}
$.ajax({
    url: '/users/getUserInfo',
    type: 'POST',
    headers: {
        'Authorization': token
    },
    success(res) {
        console.log('用户信息', res);
        if (res.code == 200) {
            $('#username').text(res.data.username);
        }
    }
})
```

问题来了：如果一个页面有几个JS调用的话，如果不通过会有好几处的401返回，原因是好几处都直接调用了方法。现在解决这个问题的方法可以是，把函数的调用全部放到auth.js的ajax里面来，

这里有的代码有

在JS文件夹里的students.js里的showStudents();

在JS文件夹里的subjects.js里的showSubjects();

最终JS文件夹下auth.js的文件的代码为：

```js
// 统一给ajax添加请求头
const token = localStorage.token;
if (token) {
    $.ajaxSetup({
        headers: {
            'Authorization': token
        },
        error(err) {
            if (err.status == 401) {
                alert('登录已过期，请重新登录');
                location.href = "../login.html";
            }
        }
    })
} else {
    alert('你还未登录，请先登录');
    location.href = "./login.html";
}
$.ajax({
    url: '/users/getUserInfo',
    type: 'POST',
    headers: {
        'Authorization': token
    },
    success(res) {
        console.log('用户信息', res);
        if (res.code == 200) {
            $('#username').text(res.data.username);
            showSubjects();
            showStudents();
        }
    }
})
```

#### 14. 常量优化处理

考虑到后端在生成 token、验证 token、解码 token 三个地方都用到了同一个密钥字符串，为了确保这三者的一致性，我们通常会将该字符串作为一个常量单独进行保存。

例如，在项目根目录创建一个 `utils/const.js` 文件，将密钥字符串保存在常量中：

```
const TOKEN_SECRET = 'hello';
module.exports = {    TOKEN_SECRET}
```

后续，在所有需要使用该字符串的地方引入使用即可。

例如，配置 token 验证规则时：

```js
const expressJWT = require('express-jwt');
const { TOKEN_SECRET } = require('./const')
const jwtAuth = expressJWT({
    secret: TOKEN_SECRET,
    //...
}).unless({
    // ....
})
module.exports = jwtAuth;
```

### RESTful

RESTful，翻译过来理解“表现层状态转换”。简单来说，就是换一种风格去设置前后端接口。

> 在 RESTful 这种设计风格中，要求“用 URL 去描述资源，用 HTTP 请求类型来描述操作。”

例如：

```
获取学生GET  /students/getStudentsGET  /students新增学生POST  /students/addStudentsPOST  /students
```

#### 请求类型

- GET：获取资源
- POST：新增资源
- PUT：修改资源
- DELETE：删除资源

例如：

```
修改学生PUT  /students删除学生DELETE  /students
```

#### 请求参数带 id

通常，ajax 发送参数都是通过 data 发送的，但是在 restful 中，参数中的 id 需要通过 url 去发送，其他参数还是通过 data 进行发送。

例如，根据 id 获取学生信息，学生 id 是 `001`：

```
GET  /students/001
```

express 的后端在匹配带 id 的接口时，需要通过 `/:变量名` 来匹配前端的 ajax 接口。

```
router.get('/:_id', getStudentsById);
```

在接收参数时，需要通过 `req.params` 来接收。

#### 返回值

restful 要求后端在返回给前端的数据中，必须是一个对象，对象中包含关于当前这次请求的描述信息：

```
{    message: '学生数据获取成功'}
```

对象中还必须包含一个状态码：

```
{    message: '学生数据获取成功',    code: 200}
```

### 前端模块化

#### 模块化特点

不使用模块化开发的缺点：

1. 在一个 HTML 文件中，引入多个 JS 文件时，需要考虑 JS 文件引入顺序；

2. 每个 JS 文件中的全局变量或函数可能会出现命名冲突；

   前端从 ES6 开始原生支持模块化。在 ES6 之前，前端想要使用模块化开发，就需要引入其他的插件。

#### 没有模块化编程

没有模块化时需要`<script>`导入所有JS文件到，由于在一个全局作用域范围内，所以都使用，但也出现了命名冲突问题

主页面

```js
<script src="./a.js"></script><script src="./b.js"></script>
```

#### 模块化开发

模块化后主文件只需要导入一个`js`文件

```js
<!DOCTYPE html><html lang="en"><head>    <script src="./index.js" type="module"></script></head><body></body></html>
```

##### 01.设置开发类型

在 HTML 中引入 JS 文件时，添加 type 属性，将该 JS 文件设置为模块：

```js
<script src="./a.js" type="module"></script>
```

注：在使用模块化语法时，页面需要通过服务器访问。可以在VSCode中安装Live Server来测试开发

##### 02.在 JS 模块中引入其他文件

```js
import './index.css';import './index.scss';import {a,b} from'./a.js';import data from './b.js';
```

说明：css和scss文件需要后续做配置才能完成

##### 03.模块内数据的暴露

默认情况下，模块内的数据只能在模块内使用，如果其他模块要使用该数据，需要先将数据暴露出去：

**通过 export 暴露多条数据**

```js
export const b     = 10;export function foo() {    
console.log('b.js foo');
}// ...
```

也可以通过export default暴露一条数据

```js
const b = 10;function foo() {    
console.log('b.js foo');
}
export default { b, foo };
```

#### 模块内引入其他模块的数据

**引入 export 暴露的多条数据**

当通过 export 暴露多条数据，在引入时，通过以下方法：

```
import { b, foo } from './b.js'
```

**说明：（在export单变量暴露时） 大括号必须写，同时大括号内部的属性名，必须和暴露时的名字一致。语法规定**

如果要重命名，可以通过 `as`：

```
import { b as num, foo } from './b.js'
```

**引入 export default 暴露的一条数据**

```js
import num from './b.js';
const { b, foo } = num;
```

**export default 暴露数据时，在引入时，不能用大括号，只能使用一个变量名做对象接受数据，命名也可以任意命名。**

### 跨域

#### 域

可以理解为要请求或访问的地址。一个完整的域，由三部分组成：

- 协议：http、https

- IP：例如：192.168.12.12

- 端口：例如 3000

  当多个地址之间，这三部分如果一致，则为同一个域，但是三者中有一个不一致，则为不同的域。

例如，以下两个地址为同一个域：

```
http://localhost:3000/index.htmlhttp://localhost:3000/students/getStudents
```

以下两个地址，为不同的域：

```
http://localhost:3000/index.htmlhttp://localhost:3001/students/getStudents
```

跨域，指的是在一个域中，发送请求去访问另一个域。

#### 同源策略

同源策略，是浏览器端的一个安全策略，该策略规定在浏览器中，只能同源（域）之间进行访问，不允许跨域。

#### 跨域的解决方案

- JSONP
- CORS
- 代理服务器

##### JSONP

jQuery 针对 ajax 的跨域问题，进行了封装处理，可以通过配置 JSONP 来实现 **GET** 的跨域请求。

在前端发送 ajax 请求时，添加以下属性：

```js
$.ajax({
    // ...
    dataType: 'jsonp',
    // ...
})
```

在 express 后端返回数据时，通过以下方式：

```js
res.jsonp({
    message: '数据获取成功',
    code: 200
})
```

原理：在 HTML 标签中，`<script>`、`<link>`、`<img>` 等标签是天生就支持跨域的。JSONP 的原理，利用的就是 `<script>` 来向后端发送请求。

##### CORS

可以在服务端通过 CORS 的方式来设置允许跨域请求： app.js

```js
// ...
var app = express();
// 设置 CORS 允许跨域
var allowCrossDomain = function (req, res, next) {
  // 设置允许哪一个源（域）可以进行跨域访问，* 表示所有源
  res.header("Access-Control-Allow-Origin", "*");
  // 设置允许跨域访问的请求头
  res.header("Access-Control-Allow-Headers", "X-Requested-With,Origin,Content-Type,Accept,Authorization");
  // 设置允许跨域访问的请求类型
  res.header("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE");
  // 设置允许 cookie 发送到服务器 
  res.header('Access-Control-Allow-Credentials', 'true');
  next();
};
app.use(allowCrossDomain); // 使用该中间件
// ...
```

##### 代理服务器

代理服务器的原理就是将前端资源都放在代理服务器，前端所有的请求都访问代理服务器，在代理服务器后端再转发请求去访问真正的目标服务器：

![image-20210806220808674](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210806220814.png)

注：同源策略只存在于浏览器端，因此服务器与服务器之间是可以进行跨域访问的。

### 版本控制系统

#### 版本控制分类

- 集中式版本控制系统：SVN
- 分布式版本控制系统：GIT

#### Git安装

淘宝镜像下载地址：`https://npm.taobao.org/mirrors/git-for-windows/`

Git 可以安装在 C 盘以外的其他盘，安装过程中直接下一步即可。

#### 查看版本

可以在终端中输入以下命令查看 git 版本：

```js
git --version
# git version 2.32.0.windows.1

```

#### 初始化配置

```js
git config --global user.name "youName"
git config --global user.email "youName@gmail.com"
```

#### Git 工作流程

![image-20210728175558443](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210728175558.png)

# Git使用操作

## 注册码云账号

进入码云官网`https://gitee.com/`注册一个账号。

## 创建远程仓库

在码云中新建一个远程仓库：

![image-20210728184814129](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210728184814.png)

进入新建仓库页面

![image-20210728184856306](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210728184856.png)

![image-20210728184919359](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210728184919.png)

添加.gitignore时随便选一个就可以

### 克隆远程仓库

获取远程仓库地址

![image-20210728185118608](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210728185118.png)

进入仓库->点击克隆/下载->选择HTTPS->单击复制

进入本地一个空文件夹（英文命名），在本地控制台克隆远程仓库，生成一个本地仓库：

```
git clone https://gitee.com/cshj586/woniuguanlixitong.git
```

![image-20210728185545640](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210728185545.png)

打开文件夹

![image-20210728185619563](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210728185619.png)

文件夹中有一个.git隐藏文件夹，这个就是.git本地仓库。管理本目录下所有文件。本文件夹就叫做**“工作区”**

#### 工作流程

**1.在工作区写代码**

**2.将工作区的代码保存到暂存区**

在 Git 终端中，将路径定位到项目根目录，执行以下命令：

```
git add .
```

表示将所有发生改变的文件都保存到暂存区。

**3. 将暂存区代码提交到本地仓库**

在项目根目录，执行以下命令：

```
git commit -m '提交日志...'
```

将代码保存到本地仓库，并填写提交日志。系统会自动生成历史记录

4.查看历史记录

```
git log
```

系统会显示当前的历史记录list

![image-20210729094812350](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210729094812.png)

**4.可以在任何状态下查看本地管理状态**

```
git status
```

如果已经add和commit，则系统会提示没有变化的文字

![image-20210729095026038](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210729095026.png)

如果有**增加或修改未add**，则系统会提示红色字体

![image-20210729095217149](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210729095217.png)

当完成add命令后，新文件或修改过的就变成了绿色，这时表示**文件已经在暂存区还没保存提交到仓库**

![image-20210729095518434](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210729095518.png)

在执行commit命令就可以完成本地仓库的保存。

**5.将本地仓库的代码推送到远程仓库**

在项目根目录，执行以下命令：

```
git push
```

在第一次往远程仓库推送代码时，会弹出弹窗提示输入码云的账号密码。

### Git分支

#### 概念

在团队开发中，整个项目会保存在一个主分支（`master`）中，但是，每个组员在进行开发时，都在子分支中进行开发。

![image-20210729095853393](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210729095853.png)

#### 创建子分支

```
git checkout -b branchName
```

`branchName`就是我们要创建的子分支的名称。子分支创建成功后，会将主分支的所有代码复制过来。后续再进行代码更改，两个分支就不会再同步了。

**查看分支**

```
git branch
```

**切换分支**

```
git checkout branchName
```

branchName是分支的名称

**查看远程地址名称**

```
git remote -v
```

#### 新建远程分支名称

```
git remote add upstream https://github.com/user1/repository.git
```

**移除远程分支名称**

```
git remote remove myremote
```

**2.在工作区写代码**

**3. 将工作区的代码保存到暂存区**

在 Git 终端中，将路径定位到项目根目录，执行以下命令

```
git add .
```

表示将所有发生改变的文件都保存到暂存区。

**4. 将暂存区代码提交到本地仓库**

在项目根目录，执行以下命令：

```
git commit -m '提交日志...'
```

将代码保存到本地仓库后，才有项目版本的历史记录。

**5. 将本地仓库的代码推送到远程子分支**

```
git push origin sub
```

`sub` 是远程子分支的名字，该子分支如果不存在，会自动创建。

注意sub要与本地分支同名

**6. 切换分支**

在切换分支前，**一定确保当前分支的代码是经过 `add` 和 `commit` 的保存。**

```
git checkout master
```

**7. 个人功能开发完成，共享代码**

#### 子分支开发步骤

当个人的功能在子分支上开发完成，想要将自己的代码共享给组员时，需要经过以下几步：

**将子分支代码合并到主分支**

首先先切换到主分支：

```
git checkout master
```

执行合并命令：

```
git merge sub
```

**拉取远程 master 上组员的代码**

```
git pull
```

**检查代码**

经过以上两步，本地 master 中既有自己的代码，也有组员的代码，因此，需要检查代码合并后是否有问题。

CONFLICT 冲突

**推送代码到远程 master**

确定本地代码合并后没有问题，就可以将本地 master 的代码推送到远程的 master：

```
git push
```

**继续开发**

将本地 master 代码合并到本地子分支

先切换到本地子分支：

```
git checkout sub
```

将本地 master 的代码合并到本地子分支

```
git merge master
```

合并完成后，本地子分支中也有组员的代码了，就可以继续开发了。

**版本回退**

首先，可以查看所有保存的版本：

```
git log
```

找到要回退的版本 Id，然后执行以下命令：

```
git reset --hard 14fef9940284385af334620bd43854a625d06c4e
```

### Git 项目管理详细流程

#### 1. 创建远程仓库

组长创建一个码云的远程仓库，开通小组内所有成员的权限。

#### 2. 组长克隆远程仓库

组长将远程仓库克隆下来后：

1. 配置 `.gitignore` 文件。
2. 进行项目初始化配置，包括 `package.json` 文件的生成、webpack 的配置、依赖包的下载、项目内文件夹的创建。

#### 3. 组长推送项目

将项目初始化配置完成后，组件需要经过以下几步，将项目的初始配置代码上传到远程仓库：

1. 暂存

   ```
   git add .
   ```

2. 提交

   ```
   git commit -m '提交日志'
   ```

3. 推送

   ```
   git push
   ```

#### 4. 组员克隆远程仓库

```
git clone 仓库地址
```

#### 5. 创建子分支

从第五步开始，组员和组长的操作一致。

```
git checkout -b 子分支名称
```

#### 6. 写代码

如果是新项目，就直接开始写自己的代码。

如果项目已经有一些写好的代码了，就自己将自己的代码拷贝到本地的仓库文件目录中去。

#### 7. 保存代码

将自己的代码保存到自己的本地仓库中：

1. 暂存

   ```
   git add .
   ```

2. 提交

   ```
   git commit -m '提交日志'
   ```

注：这一步是在自己的子分支中进行。

#### 8. 推送代码

当一个功能完成后：

1. 先将自己本地的子分支代码推送到自己的远程子分支：

```
git push origin 子分支名称
```

1. 切换到本地主分支

```
git checkout master
```

1. 将本地子分支的代码合并到本地主分支

```
git merge 子分支名称
```

1. 拉取远程主分支

```
git pull
```

1. 拉取完成后，检查代码是否有问题。没问题后，重新保存一次，执行第 7 步骤。
2. 推送到远程主分支

```
git push origin sub
```

#### 9. 继续写代码

切换回本地子分支

```
git checkout 子分支名称
```

将本地主分支的代码合并到本地子分支：

```
git merge master
```

确认代码没问题后，继续写代码了。

后续就在第 7、8、9 三个步骤中循环操作。

#### 10. 补充

如果在 Git 使用过程中，终端中出现无法输入命令的界面，可以按 `:q` 或 `:wq` 退出当前界面。

### webpack基本使用

#### 概念

webpack前端资源构建工具。它包含的功能：

1. 可以将浏览器不能识别的代码转换为能识别的代码（例如：ES6、Sass、Less）；
2. 将多个同类型文件，合并成一个文件；
3. 对代码进行压缩优化处理；

#### 前后端分离开发

前端通过 webpack 来管理项目，后端通过 exprss 来开发项目。分别创建两个不同项目的文件夹，分离开发。

#### 01. 项目初始化

创建一个空文件夹作为项目根目录（例如：`property-projects`），在终端中定位到项目根目录，然后执行以下命令，对项目进行初始化：

```
npm init -y
```

说明：项目初始化的目的，就是为了在项目根目录生成 `package.json` 项目说明文件。

#### 02.局部安装 webpack

在终端中定位到项目根目录，然后执行以下命令：

```
npm i webpack webpack-cli -D
```

说明：`-D` 表示当前依赖包，只在项目开发阶段使用，项目生产阶段就不需要了。

#### 03.搭建项目结构

在项目根目录创建一个 `src` 文件夹，后续所有的项目代码都在该目录中进行开发。例如：

![image-20210728172803653](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/caoshengjie/20210728172803.png)

每个页面建立一个JS文件夹，放入此html页面需要用的所有js，引入时是要引入一个主js就可以了。如：

```js
<head>   
<title>Document</title>    
<script src="./js/login//login.js">
</script>
</head>
```

或者

```js
<head>    
<title>Document</title>    
<script type="module">        
import data from './js/login/login.js';        
console.log(data.b);    
</script>
</head>
```

#### 4. 创建 webpack 的配置文件

在项目根目录创建 `webpack.config.js` 文件，作为 webpack 的配置文件：

```
module.exports = {    // ...}
```

后续所有关于 webpack 的配置代码，都在该对象中进行

#### 5. 设置打包模式

webpack 的打包模式分为两种：

- 开发模式：`development`，会开启 debug 模式，代码不会压缩
- 生产模式：`production`，会开启性能优化的功能，代码会进行压缩

我们可以通过 `mode` 属性来选择对应的打包模式：

```
module.exports = {    mode: 'development'}
```

#### 6. 配置入口文件

webpack 提供了 `entry` 属性，用来配置每一个 HTML 页面的入口 JS 文件(即HTML导入的唯一的js文件路径)

```js
module.exports = {    
mode: 'development',    
entry: {        
index: './src/js/index/index.js',        
login: './src/js/login/login.js',        
register: './src/js/register/register.js',        
// ...    
}}
```

说明：前（紫色）index 是指定打包后的文件名，一般同名就可以了。后路径是真正的文件所在路径

#### 7. 配置出口文件

出口文件：指的就是打包完成后的文件。webpack 提供了 `output` 属性，用来配置打包后的出口文件

```js
const path = require('path');
module.exports = {    // ...    
output: {        
// 设置打包后的代码存储路径        
path: path.resolve(__dirname, 'dist'),        
// 设置打包后的文件名        
filename: 'js/[name].js'   
}}
```

#### 8. 执行打包命令

在项目根目录执行以下命令，查看打包结果：

```
npx webpack
```

**完成**

### webpack常用配置

webpack 默认只能处理 JS 代码，如果我们需要处理 HTML、CSS 等其他代码，就需要下载额外的插件来进行配置。

#### 打包HTML

##### 1. 下载插件

```
cnpm i html-webpack-plugin -D
```

##### 2. 引入插件

```
const HtmlWebpackPlugin = require('html-webpack-plugin')
```

##### 3. 配置插件

webpack 中提供了 `plugins` 属性，用来进行所有的插件配置：

```js
const HtmlWebpackPlugin = require('html-webpack-plugin');
module.exports = {
    // ...
    plugins: [
        new HtmlWebpackPlugin({
            template: './src/index.html', // 设置要打包的源文件 HTML 的路径
            filename: './index.html', // 设置打包后的文件路径和文件名
            chunks: ['login']  // 当前 HTML 文件中引入的 JS 的名字 
        })
       // ...
    ]
}
```

还可以写all来代替名字

```js
new HtmlWebpackPlugin({
    template: './src/index.html', 
    filename: './index.html',
    chunks: 'all'
})
```

#### 打包CSS

我们在项目的 `src/css` 中创建自己的 css 文件，然后在对应的 JS 中，通过 `import` 引入 CSS

```
import '../../css/common.css';
```

##### 1. 下载插件

```
npm i mini-css-extract-plugin css-loader style-loader -D
```

##### 2. 引入插件

```
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
```

##### 3. 配置插件

webpack 提供了 `module` 属性，用来配置 loader：

```js
// ...
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
module.exports = {
    // ...
    plugins: [
        // ...
        new MiniCssExtractPlugin({
            // 打包后的 css 路径和文件名
            filename: './css/[name].css'
        })
    ],
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: [MiniCssExtractPlugin.loader, 'css-loader']
            }
        ]
    }
}
```

#### 打包 SCSS

在 `src/css` 目录中，创建自己的 scss 文件，然后在对应的 JS 文件中引入：

```
import '../../css/index/index.scss';
```

##### 1. 下载插件

```
cnpm i sass-loader node-sass -D
```

如果下载失败，就将两个插件分开下载。

node-sass 通过以下命令单独下载：

```
npm i node-sass -D --sass_binary_site=https://npm.taobao.org/mirrors/node-sass
```

##### 2. 配置插件

```js
module.exports = {
    // ...
    module: {
        rules: [
            // 打包 css 
            // ...
            // 打包 scss
            {
                test: /\.scss$/i,
                use: ['style-loader', 'css-loader', 'sass-loader']
            }
        ]
    }
}
```

#### 打包图片

##### 1. 下载依赖包

```
npm i url-loader file-loader html-withimg-loader -D
```

##### 2. 配置插件

```js
// ...
module.exports = {
    // ...
    module: {
        rules: [
              //.. 
            // css 中的图片
            {
                test: /\.(png|jpg|jpeg|gif)$/i,
                use: [
                    {
                        loader: 'url-loader',
                        options: {
                            limit: 1024 * 8, // 8kb 以下的图片采用 base64 进行处理
                            outputPath: './images/',  // 打包后图片的存储路径
                            esModule: false
                        }
                    }
                ]
            },
            // html 中的图片
            {
                test: /\.html$/i,
                use: ['html-withimg-loader']
            }
        ]
    }
}
```

#### 开发服务器

##### **1.下载插件**

```
cnpm i webpack-dev-server -D
```

##### **2.启动服务器**

```
npx webpack serve
```

在启动服务器后，会自动帮我们打包项目代码

该插件会开启一个端口号为8080的服务器

通过服务器打包的代码，是不会在项目中生成实际目录，而是打包在内存中。我们通过访问服务器地址就可以访问打包后的效果。

##### **3.其他配置**

webpack 还提供了 `devServer` 属性用来配置服务器：

```js
module.exports = {
    devServer: {
        port: 8888,
        open: true, // 启动服务器时自动打开页面
        hot: true, // 热更新
        proxy: {
            '/': {
                target: 'http://localhost:3000'  // 后端服务器地址
            }
        }
    }
}
```

### 变量对象

在执行上下文创建时，在执行上下文内部还是创建一个变量对象。

变量对象在创建的过程中，变量对象会做以下三件事情：

1. 查找当前上下文中的所有形参（全局没有形参，不考虑这一步）
2. 查找当前上下文中所有的声明式函数；
3. 查找当前上下文中所有通过 `var` 声明的变量；

找到以上所有的数据后，保存在变量对象中。

示例：

```js
function foo(a) {
    console.log(b);
    var b = 2;
    console.log(b);
    function bar() {
        console.log(3);
    }
}
foo(1)
```

![image-20210601155452136](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210601155452.png)

### 作用域链

在创建执行上下文时，除了要生成变量对象以外，同时还会建立作用域链。

作用域链，实际上是由一系列的变量对象的组成。这条链条的开端，一定自己的变量对象，这条链条的末尾，一定是全局的变量对象。

```js
var food = '巧克力de味';
function eat() {
    console.log('吃' + food);
}
function foo() {
    var food = '味的巧克力';
    eat();
}
foo();
```

作用域链的第一个变量对象，是当前变量对象。后续所有的下一个，都是前一个变量对象创建时所在的执行上下文中的变量对象。

