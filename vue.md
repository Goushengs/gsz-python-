### 1、创建变量

- var
- let
- const

#### const

```js
const num = 10;
num = 20;  // 报错
const arr = [1, 2, 3];
arr.push(4);         // 正确
arr = [1, 2, 3, 4];  // 报错
const obj = { a: 1 }
obj.a = 20;        // 正确
obj = { a: 20 }    // 报错
```

### 2、对象简写

ES6 中针对对象，提供了两种情况的简写：

- **对象属性的简写**：对象的值是一个变量，且键和值是同一个单词时，冒号和值可以省略；
- **对象方法的简写**：对象的值，是一个函数，冒号和 `function` 可以省略；

#### 对象属性的简写

```js
const name = "zhangsan"
const student = {
    // name: name,
    // 简写
    name
}
```

#### 对象方法的简写

```js
const student = {
    sayHello: function() {
        console.log('hello');
    },
    // 简写
    sayHello() {
        console.log('hello');
    }
}
```

### 3、箭头函数

基础语法：

```js
const foo = function() {
    return 'hello'
}
// 箭头函数
const foo = () => {
    return 'hello'
}
```

普通函数变成箭头函数：去掉 `function`，在 `()` 和 `{}` 加上 `=>`。

#### 简写

箭头函数的简写分为两种情况：

- 当小括号中**只有一个**形参时，`()` 可以省略；
- 当函数体内只有一句 `return` 语句时，可以将函数的 `{}` 和 `return` 一起省略；

```js
// 未简写的箭头函数
const foo = (a) => {
    return a;
}
// 省略小括号
const foo = a => {
    return a;
}
// 省略大括号和 return
const foo = a => a;

const foo = a => console.log(a);
const foo = a => {
    console.log(a);
}
```

### 4、解构赋值

解构赋值主要针对数组和对象：

#### 数组解构

```js
const arr = [1, 2, 3];
const [a, b, c] = arr;
```

#### 对象解构

```js
const student = { name: '张三', age: 20, gender: '男' };
const { name: a, age: b, gender: c } = student;
const { name: name, age: age, gender: gender } = student;
// 简写
const { name, age, gender } = student;
```

对象在解构时，赋值符左右两边，对象的**键必须保持一致**，值可以是任意变量。

### 5、扩展运算符

扩展运算符通常用于数组或对象。

#### 应用场景

1. 当需要对数组或对象进行复制，同时在复制后得到一个新地址：

```js
const arr = [1, 2, 3];
// const newArr = arr;  // 同一个地址
const newArr = [...arr];  // 新地址
const obj = { a: 1, b: 2 };
const newObj = {...obj}
```

1. 当需要往数组或对象中添加新数据，同时改变原地址：

```js
let arr = [1, 2, 3];
arr = [...arr, 4, 5, 6, 7];
let obj = { a: 1, b: 2 };
obj = { ...obj, c: 3, d: 4 }
```

JS 中所有的数据分为两个大类：

- 基础（基本）数据：Number、String、Boolean、Null、Undefined、Symbol（ES6）
- 引用（复杂）数据：Object

### 存储方式

在内存中，将内存空间分为了两个区域：栈和堆。

基础数据的值都是保存在栈空间中，而引用数据的值，保存在堆空间中，但是，堆里面的每一条数据，都有一个对应的引用地址。而所有的引用地址，也是保存在栈内存中。

![image-20210907111456143](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210907111456.png)

```js
let arr = [1, 2, 3];
let newArr = arr;   // 将 arr 的地址复制给了 newArr
arr[0] = 'a';
console.log(newArr);   // [ 'a', 2, 3 ]

let arr = [1, 2, 3];
let newArr = [...arr];  // 将一个新的引用地址赋值给 newArr
arr[0] = 'a';
console.log(newArr); // [1, 2, 3]
```

### 框架和库

#### 库

库，就是一组特定方法的集合。例如 jQuery，是一个 JS 库，主要封装了许多关于阶段操作的方法。

#### 框架

框架，针对我们的项目，提供了一整套的解决方案。

#### 区别

框架和库的区别在于“控制权”上，使用库时，控制权在开发者手上，我们可以自己来决定使用哪几个库。使用框架时，控制权在框架身上，开发者需要按照框架的规则来写代码。

#### 前端主流框架

现在前端主流的框架主要有三个：

- Angular：2009 年，现在是 Chrome 的技术团队在进行维护；
- React：2013 年，现在是 Facebook 的技术团队在进行维护；
- Vue.js：2014 年，现在是尤雨溪团队的进行维护；

### 概念

Vue (读音 /vjuː/，类似于 **view**) 是一套用于构建用户界面的**渐进式框架**。

#### 安装 Vue CLI

Vue 的官方提供了多种安装方式，我们直接选择 Vue CLI 来创建和管理 Vue 项目。

#### 1、查看 Vue CLI 版本

在终端中任意路径，输入以下命令，查看 Vue CLI 版本：

```
vue --versionvue -V# @vue/cli 4.5.13
```

如果是 2.x 或者 2.x 以下的版本，需要将旧版本卸载后，再重新安装最新版本。

#### 2、安装 Vue CLI

如果没有安装过 Vue CLI，或者安装的是 3.x 或更高版本，可以直接在终端任意路径中执行以下命令下载最新版本：

```
npm install -g @vue/cli
```

![image-20210907120950789](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210907120950.png)

#### 创建 Vue.js 项目

在终端中定位到需要存放项目的目录，然后执行以下命令创建项目：

```
vue create 项目名称
```

##### 1、选择安装模式

```js
Vue CLI v4.5.13
? Please pick a preset: (Use arrow keys)
  Default ([Vue 2] babel, eslint)
  Default (Vue 3) ([Vue 3] babel, eslint)
> Manually select features
```

##### 2、选择安装插件

```js
? Check the features needed for your project: 
 ( ) Choose Vue version
>(*) Babel
 ( ) TypeScript
 ( ) Progressive Web App (PWA) Support        
 ( ) Router
 ( ) Vuex
 ( ) CSS Pre-processors
 ( ) Linter / Formatter
 ( ) Unit Testing
 ( ) E2E Testing
```

##### 3、选择插件配置文件位置

```
? Where do you prefer placing config for Babel, ESLint, etc.? (Use arrow keys)
> In dedicated config files
  In package.json
```

##### 4、是否保存供以后使用

```js
? Save this as a preset for future projects? (y/N) n
```

##### 5、创建成功

```js
 Successfully created project vue-demo.
 Get started with the following commands:
 $ cd vue-demo
 $ npm run serve
```

##### 6、启动项目

在终端中进入到项目的根目录路径，执行以下命令启动项目：

```
npm run serve
```

出现以下提示，则表示项目启动成功：

```js
DONE  Compiled successfully in 3621ms                             下午2:08:17
  App running at:
  - Local:   http://localhost:8080/
  - Network: http://192.168.40.69:8080/
  Note that the development build is not optimized.
  To create a production build, run npm run build.
```

`http://localhost:8080/` 就是项目的访问地址。

### 组件的概念

组件，component。我们可以把组成页面的结构，例如：头部、侧边栏、内容区域、底部等，拆分成一个一个的组件。每一个结构都对应一个单独的组件，这些组件通过各种方式，组合到一起，又可以构成一个完整的页面。

#### Vue.js 组件的分类

根据组件的作用范围，可以分为全局组件和局部组件。

- 全局组件：可以作用于任何 Vue 实例对象范围内；
- 局部组件：只能作用于当前 Vue 实例对象范围内；

#### 单文件组件

单文件组件，指的就是所有以 `.vue` 为后缀名的文件，每一个文件，都是一个单独的组件。

建议：组件名首字母大写。

每一个单文件组件，都是由三部分组成：

- `<template>`：组件的结构，类似 HTML；
- `<script>`：组件的逻辑处理，包括数据、事件等；
- `<style>`：组件的样式；

说明：`<template>` 是必选的，`<script>`、`<style>` 是可选的。

#### 组件的嵌套

##### 1、引入组件

在父组件中引入子组件：

```js
<script>
// 1. 引入
import HelloWorld from "./components/HelloWorld.vue";
export default {
};
</script>
```

##### 2、注册组件

```js
<script>
// 1. 引入
import HelloWorld from "./components/HelloWorld.vue";
export default {
    // 2. 注册子组件（配置）
    components: {
        HelloWorld: HelloWorld,
    },
};
</script>
```

##### 3、渲染组件

```js
<template>
    <div>
        <h1>Hello</h1>
        <!-- 3. 渲染子组件 -->
        <HelloWorld></HelloWorld>
    </div>
</template>
```

### 1、Vue 实例

> 每个 Vue 应用都是通过用 `Vue` 函数创建一个新的 **Vue 实例**开始的。

在通过 Vue CLI 创建的项目中，在 `main.js` 中创建了 Vue 实例：

```js
// 引入 Vue，获取 Vue 函数
import Vue from 'vue';
import App from './App.vue'  // 引入 App.vue 组件
// 创建 Vue 实例
new Vue({
  render: h => h(App),  // 渲染 App.vue 组件
}).$mount('#app') // 将渲染好的组件添加到 id=app 的元素中
```

### 2、数据

每一个组件对象身上，都有一个 `data` 属性，用来设置当前组件所需要的数据。

语法结构：

```js
export default {
    data() {
        return {
            // 数据
            name: '张三',
            message: 'Hello World',
            // ...
        };
    },
}
```

注意：Vue 实例的 data，可以是对象，也可以是函数，但是**组件的 data，只能是函数**。

### 3、模板语法

Vue 中提供了模板语法 `{{}}` 来渲染数据：

```js
<template>
    <div>
        <h2>基础语法</h2>
        <h3>{{name}}</h3>
        <h4>{{message}}</h4>
        <h1>{{message}} {{name}}</h1>
        <h1>{{message + ' ' + name}}</h1>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                // 数据
                name: "张三",
                message: "Hello",
            };
        },
    };
</script>
```

`{{}}` 中可以设置任意的 JS 表达式。

### 4、事件

Vue 中给标签身上提供了一个特殊属性 `v-on` 用来设置事件监听：

```js
<button v-on:click="name = '李四'">按钮</button>
```

`v-on` 可以简写成 `@`。

```js
<button @click="name = '李四'">按钮</button>
```

### 指令

Vue 中给所有的标签提供了一些以 `v-` 开头的特殊属性，称之为“指令”。

#### v-text 和 v-html

```js
<template>
    <div>
        <h1>{{msg}} world</h1>
        <h1 v-text="msg">world</h1>
        <h1 v-html="msg">world</h1>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                msg: '<a href="#">hello</a>'
            }
        },
    }
</script>
```

总结：`{{}}`和 `v-text`、`v-html` 三者都可以渲染动态数据，他们的区别在于：

1. `{{}}` 不会覆盖标签中的原内容，而 `v-text`、`v-html` 会覆盖；
2. `v-html` 可以解析数据中的 HTML 标签，而 `{{}}`、`v-text` 无法解析；

#### v-show

v-show 根据指令值的 true 或 false，来控制元素节点的显示或隐藏。当值为 false，元素身上会添加一个 `display: none` 属性来实现隐藏效果。

```js
<template>
    <div>
        <h1 v-show="isShow">world</h1>
        <button @click="isShow = !isShow">显示/隐藏</button>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                isShow: true
            }
        },
    }
</script>
```

v-show 需要的是一个布尔值，但是如果给定不是布尔值，会自动转换为布尔值。

转换规则：除了 0、null、undefined、NaN、””、false 六个以外，其他数据转换后都为 true。

#### v-bind

v-bind 指令用来给元素添加一个或多个动态属性。

```js
<template>
    <div>
        <a v-bind:href="link">百度一下</a>
    </div>
</template>
<script>
export default {
    data() {
        return {
            link: 'https://www.baidu.com'
        }
    },
}
</script>
```

`v-bind` 指令可以简写 `:`。

```
<a :href="link">百度一下</a>
```

#### 动态渲染图片

动态渲染网络图片，可以直接通过 v-bind 渲染：

```js
<template>
    <img :src="img_src" alt />
</template>
<script>
    export default {
        data() {
            return {
                img_src: 'http://www.woniuxy.com/page/img/logo-500px.png',
            };
        },
    };
</script>
```

动态渲染本地图片，需要先将本地图片通过 `require()` 方法将图片加载进来，然后再进行动态渲染：

```js
<template>
    <img :src="img_src" alt="">
</template>
<script>
    export default {
        data() {
            return {
                img_src: require('../../assets/logo.png')
            };
        },
    };
</script>
```

### 列表渲染

#### v-for

Vue 中提供了 `v-for` 指令来实现列表渲染。语法结构如下：

```js
<div v-for="(item, index) in Array"></div>
```

其中，`item` 为变量名，用来接收数组中的每一项，`index` 也是变量名，用来接收数组项的下标，`Array` 为数组名。

当不需要 `index` 时可以不写：

```js
<div v-for="item in Array"></div>
```

例如，将学生数组渲染为无序列表：

```js
<template>
    <ul>
        <li v-for="item in students">
            {{item.name}}
        </li>
    </ul>
</template>
<script>
    export default {
        data() {
            return {
                students: [
                    { _id: 1, name: "张三" },
                    { _id: 2, name: "李四" },
                    { _id: 3, name: "王五" },
                ],
            };
        },
    };
</script>
```

#### key

Vue 中要求，每一个通过 `v-for` 循环产生的元素身上，都必须添加一个**唯一且固定不变**的 key 属性。

```js
<template>
    <ul>
        <li v-for="item in students" v-bind:key="item._id">
            {{item.name}}
        </li>
    </ul>
</template>
```

#### template

Vue 中还提供了一个 `<template>` 标签来搭配 v-for 使用。

`<template>` 是一个虚拟标签，当页面渲染成功后， `<template>` 不会显示在节点中。

```js
<template v-for="item in students">
    <span :key="item._id">{{item._id}}</span>
    <span :key="item._id + 'a'">{{item.name}}</span>
</template>
```

注意：`key` 属性不能设置在 `<template>` 身上，只能设置在内部的真实节点上。还要保证内部节点之间的 key 不重复。

#### v-for 遍历其他数据

v-for 除了可以遍历数组外，还可以遍历对象、字符串、数字：

```js
<p v-for="(value, key, index) in students[0]" :key="value">
    {{value}} {{key}} {{index}}
</p>
<p v-for="(item ,index) in students[0].name" :key="item">
    {{item}} {{index}}
</p>
<p v-for="item in 4" :key="item">
    {{item}}
</p>
```

Vue 中提供了三个指令来实现条件渲染：

- `v-if`
- `v-else`
- `v-else-if`

```js
<template>
    <div>
        <h1 v-if="isOK">第一个h1</h1>
        <h1 v-else-if="true">第二个h1</h1>
        <h1 v-else>第三个h1</h1>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                isOK: true
            }
        },
    }
</script>
```

### template

v-if 也可以搭配 `<template>` 使用。

```js
<tmeplate v-if="false">
    <p>1</p>
    <p>2</p>
    <p>3</p>
</tmeplate>
```

### v-if 和 v-show

v-if 和 v-show 都可以用来控制元素节点的显示和隐藏。区别在于：

- v-if 是真正的条件**渲染**，当条件为 false 时，v-if 对应的节点不会渲染；
- v-show 是通过 css 来控制元素是否显示，当条件为 false 时，v-show 对应的节点会先渲染，然后再添加 display: none 隐藏元素；

当条件切换比较频繁的时候，用 v-show，当条件变化不多的时候，用 v-if。

### v-if 和 v-for

v-if 和 v-for 在同一个元素身上使用时，v-for 的优先级更高。但是，不建议在同一个元素身上使用时 v-if 和 v-for 。

解决办法：

- 将其中一个指令设置在 `<template>` 中；
- 计算属性；

### class 与 style 绑定

每一个单文件组件的 `style` 中，都可以通过 css 设置样式。但是， `<style>` 中的样式默认都是全局样式，会作用于 Vue 应用中的所有组件。

#### 局部样式

在 `<style>` 身上添加一个 `scoped` 属性，就可以让 `<style>` 中的样式变成局部样式，只作用于当前组件。

```
<style scoped>h1 {    background-color: burlywood;    color: #fff;}</style>
```

#### 外部样式

在组件中，可以通过 `@import` 引入外部样式：

```
<style>@import './common.css';</style>
```

注意：通过以上方式引入的外部样式，永远都是全局样式。

#### 局部的外部样式

```
<style scoped src="./common.css"></style>
```

#### scss

如果要在单文件组件的 style 中设置 scss，需要给 `<style>` 添加 `lang="scss"` 属性：

```js
<style scoped lang="scss">   
div {        
    h1 {            
    color: red;        
    }    
    }
    </style>
```

#### 动态 class 和 style 绑定

Vue 中给 class 和 style 提供了对象和数组的语法来实现样式的动态绑定。

##### 动态绑定 class

```js
<div :class="{ active: true, done: false }"></div>
```

对象的键是我们需要使用的 class 名，值的 true 或 false，决定了 class 能够生效。

##### 动态绑定 style

```js
<div :style="{ width: w, height: h + 'px'}"></div>
data() {    
    return {        
        w: '100px',        
        h: '100'    
    }}
```

### 事件处理

#### 事件处理方法

Vue 中给每一个组件提供了一个 `methods`，用来设置组件的方法：

```js
export default {
    methods: {
        方法名1() {
            // ...
        },
        方法名2() {
            // ...
        }
    }
}
```

#### this

<script> 中的 this 指向当前组件对象，因此，在 JS 中，如果要访问数据或方法等，都需要通过 this 进行访问：

```js
export default {
    data() {
        return {
            num: 1,
        };
    },
    methods: {
        increment() {
            this.num++;
        }
    },
}
```

#### 事件传参

```js
<template>
    <div>
        <button @click="increment(10)">+10</button>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                num: 1,
            };
        },
        methods: {
            increment(newNum) {
                this.num += newNum;
            },
        },
    };
</script>
```

#### 事件修饰符

```
<a href="http://www.baidu.com" @click.prevent="linkEvent">链接</a><a href="http://www.baidu.com" @click.prevent.stop="linkEvent">链接</a><a href="http://www.baidu.com" @click.prevent>链接</a>
```

#### 按键修饰符

```
<input type="text" @keyup.enter="linkEvent">
```

#### 事件对象（扩展）

在事件方法调用时没加小括号的情况下，事件方法的第一个参数默认就是事件对象：

```js
<button @click="clickEvent">
    按钮
</button>
```

```js
export default {
    methods: {
        clickEvent(event) {
            console.log(event)
        }
    }
}
```

如果调用事件方法时加了小括号，就需要我们手动传递 `$event` 对象：

```js
<button @click="clickEvent(10, $event)">
    按钮
</button>
```

```js
export default {
    methods: {
        clickEvent(num, event) {
            console.log(event)
        }
    }
}
```

#### 扩展

获取输入框的值，可以通过 `ref` 属性给元素取名字：

```js
<input type="text" ref="add">
```

在 JS 中，可以通过 `this.$refs.add` 获取到当前这个节点，如果要获取输入框节点的内容：

```js
this.$refs.add.value;
```

### 计算属性

#### 基础语法

每一个组件都有一个 `computed` 属性，用来设置计算属性：

```js
export default {
    computed: {
        计算属性名1() {
            return 计算属性值1
        },
        计算属性名2() {
            return 计算属性值2
        },
        // ...
    }
}
```

例子：

```js
<template>
    <h1>{{sum}}</h1>
</template>
<script>
    export default {
        data() {
            return {
                num1: 10,
                num2: 20,
            };
        },
        computed: {
            sum() {
                return this.num1 + this.num2;
            },
        },
    };
</script>
```

当我们需要对 data 中的数据做一些操作来得到一条新数据，同时不会修改 data 中的原数据。这种情况下就可以使用计算属性。

#### 计算属性的缓存

```js
<template>
    <div>
        <h1>{{sum}}</h1>
        <h1>{{sum}}</h1>
        <h1>{{getSum()}}</h1>
        <h1>{{getSum()}}</h1>
    </div>
</template>
<script>
export default {
    data() {
        return {
            num1: 10,
            num2: 20,
        };
    },
    computed: {
        sum() {
            console.log('计算属性');
            return this.num1 + this.num2;
        },
    },
    methods: {
        getSum() {
            console.log('方法');
             return this.num1 + this.num2;
        }
    }
};
</script>
```

计算属性能够实现的效果，实际上 methods 方法也能实现。但是区别在于：当计算属性和方法都多次使用时，计算属性只会执行一次，而方法使用几次就执行几次。

这是因为计算属性具有缓存的功能，当第一次使用计算属性将结果计算出来后，计算属性会把结果缓存下来，后续使用时都直接从缓存中读取结果。只有当计算属性依赖的原数据发生改变时，计算属性才会重新计算。

#### get 和 set

计算属性实际上是一个对象，不是方法。计算属性的完整写法：

```js
export default {
    computed: {
        计算属性名: {
            get() {
                return 计算属性值;
            }
        }
    }
}
```

默认情况下，计算属性只有 get，没有 set，因此不能修改计算属性。如果需要修改计算属性，需要手动给计算属性添加 set 方法：

```js
export default {
    computed: {
        计算属性名: {
            get() {
                return 计算属性值;
            },
            set(修改的值) {
                // 修改计算属性 get 中依赖的原数据
            }
        }
    }
}
```

注意：计算属性永远都不能修改它本身，我们 set 方法中修改的应该计算属性所依赖的原数据。

### 侦听器

#### 基础语法

```js
export default {
    watch: {
        侦听的属性名(新值, 旧值) {
            // ...
        }
    }
}
```

当 watch 侦听的数据发生变化时，就会执行对应的方法。

#### 侦听引用类型数据

默认情况下，watch 是侦听引用数据的地址是否发生改变。当引用数据的地址没有改变时，watch 侦听不到内部数据的变化。

解决方案有两个：

- 单独侦听某一个属性的变化
- 深度侦听

#### 单独侦听某一个属性的变化

```js
<template>
    <div>
        <h1>{{student}}</h1>
        <button @click="student.name = '李四'">修改</button>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                student: {
                    name: "张三",
                },
            };
        },
        watch: {
            'student.name'() {
                console.log("学生姓名发生变化了");
            },
        }
    };
</script>
```

#### 深度侦听

```js
<template>
    <div>
        <h1>{{student}}</h1>
        <button @click="student.name = '李四'">修改</button>
        <button @click="student = { name: '李四' }">修改</button>
    </div>
</template>
<script>
export default {
    data() {
        return {
            student: {
                name: "张三",
            },
        };
    },
    watch: {
        student: {
            handler() {
                console.log("学生发生变化了");
            },
            deep: true
        },
    },
};
</script>
```

#### 立即侦听

立即侦听指的是数据首次渲染时，也会执行一次侦听器：

```js
export default {
    data() {
        return {
            student: {
                name: "张三",
            },
        };
    },
    watch: {
        student: {
            handler() {
                console.log("学生发生变化了");
            },
            immediate: true
        },
    },
};
```

### 表单输入绑定

Vue 中提供了 v-model 来实现表单元素的双向数据绑定。

#### 输入框

```js
<template>
    <input type="text" v-model="msg">
</template>
<script>
    export default {
        data() {
            return {
                msg: 'hello'
            }
        }
    }
</script>
```

在输入框中，v-model 和 value 同时设置时，value 会被忽略。

v-model 的原理：

```js
<template>
    <input type="text" ref="newMsg" :value="msg" @input="inputEvent">
</template>
<script>
    export default {
        data() {
            return {
                msg: 'hello'
            }
        },
        methods: {
            inputEvent() {
                this.msg = this.$refs.newMsg.value;
            }
        }
    }
</script>
```

#### 复选框

复选框搭配 v-model 使用分为了两种情况：

- 想要获取复选框的选中状态，true 或者 false；
- 想要获取被选中的复选框的内容；

##### 获取选中状态

```js
<template>
    <input type="checkbox" v-model="isAgree">我已阅读并同意以上协议
</template>
<script>
export default {
    data() {
        return {
            isAgree: false,
        }
    }
}
</script>
```

##### 获取选中的内容

如果要获取用户选中的复选框的内容，需要将内容添加到复选框的 value 属性中。

```js
<template>
    <div>
        <input type="checkbox" value="吃饭" v-model="likes">吃饭
        <input type="checkbox" value="睡觉" v-model="likes">睡觉
        <input type="checkbox" value="打豆豆" v-model="likes">打豆豆
    </div>
</template>
<script>
export default {
    data() {
        return {
            likes: ["睡觉"],
        }
    }
}
</script>
```

#### 单选框

```js
<template>
    <div>
        <input type="radio" value="男" v-model="gender">男
        <input type="radio" value="女" v-model="gender">女
    </div>
</template>
<script>
    export default {
        data() {
            return {
                gender: '男',
            }
        }
    }
</script>
```

#### 下拉列表

```js
<template>
    <div>
        <select v-model="city">
            <option value="四川">四川</option>
            <option value="云南">云南</option>
            <option value="贵州">贵州</option>
        </select>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                city: '四川'
            }
        }
    }
</script>
```

说明：v-model 默认获取 options 的 value 值，但是当 option 没有 value 属性时，则回去 option 中的文本内容。

### 数据变更检测

所有设置在组件 data 中的数据，都会加入到响应式系统中。当数据发生变化时，系统会自动检测到数据的改变，然后同时去更新页面。

但是，响应式系统在检测引用数据时，是通过地址的改变来识别数据是否发生改变，也就意味着，如果只改变了引用数据内部的值，没有改变引用数据的地址，那么响应式系统就检测不到这种变化，页面也就不会更新。

针对引用数据的一些常用方法，例如数组的 `push`、`splice`，对象属性的修改等，虽然这些方法操作数据时也不会改变数据的地址，但是 Vue 针对这些方法做了额外的处理，因此，这几个方法即使没有改变引用数据的地址，页面也会更新。

但是，数组和对象仍然一些操作是 Vue 不能检测的。

#### 数组

Vue 不能检测以下数组的变动：

1. 通过下标操作数组的元素
2. 对数组长度的操作

解决方案：

```js
export default {
    data() {
        return {
            students: [
                '张三', '李四'
            ]
        }
    },
    methods: {
        handleStudents() {
            // this.students[0] = '王五';  // 无法识别
            // this.students.length = 0;  // 无法识别
            // 能识别
            // this.students.splice(0, 1, '王五');
            // this.$set(this.students, 0, '王五');
            this.students = [];
            console.log(this.students);
        }
    }
}
```

#### 对象

Vue 不能检测以下对象的变动：

- 对象属性的增加
- 对象属性的删除

```js
export default {
    data() {
        return {
            person: {
                name: '张三'
            }
        }
    },
    methods: {
        handlePerson() {
            // this.person.age = 20;    // 不能识别
            // delete this.person.name; // 不能识别
            // 能识别
            // this.$set(this.person, 'age', 20);
            this.person = {
                ...this.person,
                age: 20
            }
            console.log(this.person);
        }
    }
}
```

### 生命周期

组件的生命周期，指的就是组件从创建、到渲染、到更新，最后到销毁的整个过程。

Vue 在组件的生命周期的过程中，提供了 8 个生命周期函数：

| 阶段         | 函数          | 描述                 | 备注                   |
| :----------- | :------------ | :------------------- | :--------------------- |
| 组件创建阶段 | beforeCreate  | 组建创建前           | 不能访问 data 数据     |
| 组件创建阶段 | created       | 组建创建完成         | 发送网络请求           |
| 组件挂载阶段 | beforeMount   | 组件挂载（渲染）前   |                        |
| 组件挂载阶段 | mounted       | 组件挂载（渲染）完成 | 发送网络请求           |
| 组件更新阶段 | beforeUpdate  | 组件更新前           | 建议不要修改 data      |
| 组件更新阶段 | updated       | 组件更新完成         | 建议不要修改 data      |
| 组件销毁阶段 | beforeDestroy | 组件销毁前           |                        |
| 组件销毁阶段 | destroyed     | 组件销毁完成         | 组件数据、事件等都无效 |

```js
export default {
    data() {
        return {
            msg: "hello",
        };
    },
    beforeCreate() {
        console.log("组建创建前", this.msg);
    },
    created() {
        console.log("组件创建完成", this.msg);
    },
    beforeMount() {
        console.log("组件挂载（渲染）前");
    },
    mounted() {
        console.log("组件挂载（渲染）完成");
    },
    beforeUpdate() {
        console.log("组件更新前");
    },
    updated() {
        console.log("组件更新完成");
    },
    beforeDestroy() {
        console.log('组件销毁前');
    },
    destroyed() {
        console.log('组件销毁完成');
    },
};
```

### Prop 基础语法

每一个组件都有一个`props`属性用来接收外部传递的数据：

```vue
export default {      
   props: []
}
```

数组中用来定义需要接收的数据名称。例如`Child.vue`组件要接收`name`和`age`两条数据：

```vue
// Child.vue
export default {      
    props: ['name', 'age']
}
```

组件中通过`props`接收到的数据，可以直接通过`this`进行访问：

```vue
<template>
        <h1>姓名：{{name}}，年龄：{{age}}</h1>
</template>
<script>
export default {
      mounted() {
          console.log(this.name, this.age);
    }
}
</script>
```

**注意：Vue 中规定，通过`props`获取到的值，可以访问，但是不能修改。**

### 给 Prop 传递数据

通过自定义属性的方式，从组件外部给组件内部传递数据：

```
<Child name="张三" age="18"></Child>
```

自定义属性的属性名，需要跟组件内部`props`定义的数据名称一致。

#### 数据类型

在通过自定义属性给 props 传递数据时，我们需要考虑数据的不同类型。例如：

```vue
<template>
        <Child name="张三" age="18" bool="true" ary="[1, 2, 3]" obj="{ a: 1 }" msg="msg"></Child>
</template>
<script>
export default {
      data() {
        return {
                        msg: 'Hello'
        }
    }
}
</script>
```

以上代码中，传递的六条数据实际上全都是字符串，并没有什么数字、布尔值、数组、对象，`msg`属性传递的值也是一个`"msg"`字符串，并不是`"Hello"`。

如果我们希望传递真正的数字、布尔值、数组、对象，或者是 data 中的数据，就需要通过`v-bind`将这些属性变成动态属性：

```vue
<Child name="张三" :age="18" :bool="true" :ary="[1, 2, 3]" :obj="{ a: 1 }" :msg="msg"></Child>
```

简单来说，就是**在给 props 传递数据时，除了普通字符串以外，其他数据全都需要通过`v-bind`指令来进行传递。**

### 自定义事件

父组件将自己的方法，通过自定义事件的方式，将方法传递给子组件，子组件中通过 `$emit()` 来触发父亲传递的自定义事件。

父组件设置自定义事件：

```vue
<template>
    <div>
        <h1>{{ num }}</h1>
        <Child @fatherEvent="increment"></Child>
    </div>
</template>
<script>
import Child from "./Child.vue";
export default {
    components: {
        Child,
    },
    data() {
        return {
            num: 1,
        };
    },
    methods: {
        increment() {
            this.num++;
        },
    },
};
</script>
```

子组件触发自定义事件：

```vue
<template>
    <button @click="$emit('fatherEvent')">+1</button>
</template>
```

#### 应用场景

1. 子组件想要修改父组件的数据；
2. 子组件给父组件传值；

当子组件想要传递数据给父组件时，也可以使用自定义事件。

父组件设置自定义事件，并设置形参接收数据：

```vue
<template>
    <div>
        <h1>{{ num }}</h1>
        <Child @fatherEvent="increment"></Child>
    </div>
</template>
<script>
import Child from "./Child.vue";
export default {
    components: {
        Child,
    },
    data() {
        return {
            num: 1,
        };
    },
    methods: {
        increment(newNum) {
            this.num = newNum;
        },
    },
};
</script>
```

子组件触发自定义事件，并传值给父组件：

```vue
<template>
    <button @click="$emit('fatherEvent', 100)">+1</button>
</template>
```

#### 面试题

Vue 中如何实现父子组件之间的传值：

- 父传子：props
- 子传父：自定义事件

#### 事件总线

事件总线，用来实现非父子组件之间的传值。

##### 原理

1. 通过 `new Vue()` 创建一个新的 Vue 实例对象，作为事件总线；
2. 接收数据的组件，给事件总线绑定事件；
3. 传递数据的组件，给触发事件总线的方法

##### 创建事件总线

创建一个 `bus.js` 文件，通过以下代码来创建事件总线：

```js
import Vue from 'vue';
const bus = new Vue();
export default bus;
```

##### 触发事件

```js
<template>
    <button @click="toB">按钮</button>
</template>
<script>
    import bus from "./bus.js";
    export default {
        data() {
            return {
                num: 1,
            };
        },
        methods: {
            toB() {
                bus.$emit('getData', this.num);
            },
        },
    };
</script>
```

### 动态组件

基础语法：

```js
<component :is="currentTab"></component>
```

其中，`currentTab` 是 data 中的数据，保存的是当前要显示的组件名称。

注意：动态组件在切换过程中，组件都会不断的进行销毁和重建。

##### keep-alive

在某些情况下，我们希望动态组件在切换时能够保持状态，不销毁。所以，可以使用 `<keep-alive>` 将动态组件包裹起来：

```js
<keep-alive>
    <component :is="currentTab"></component>
</keep-alive>
```

##### 生命周期函数

被 keep-alive 包裹的组件，会新增两个生命周期函数：

- activated：进入组件时执行
- deactivated：离开组件时执行

##### 属性

- include：和属性名匹配成功的组件都会被缓存；
- exclude：和属性名匹配成功的组件都不会被缓存；

```js
<keep-alive :include="/Tab(A|B)/" exclude="TabC">
    <component :is="currentTab"></component>
</keep-alive>
```

### 插槽

Vue 中，提供了 `<slot>` 插槽标签。在组件中，就可以通过 `<slot>` 标签占位，父组件就可以向 `<slot>` 传递内容。

##### 基础语法

在子组件中通过 `<slot>` 设置插槽：

```js
<template>
    <div>
        <h3>子组件</h3>
        <slot></slot>
    </div>
</template>
```

在父组件中，可以向插槽传递内容：

```js
<template>
    <div>
        <Child>
            <p>这是传递给插槽的内容</p>
            <p>这是传递给插槽的内容</p>
            <p>这是传递给插槽的内容</p>
        </Child>
    </div>
</template>
```

##### 后备内容（默认值）

后备内容，指的就是插槽的默认值，当使用子组件时，没有给插槽传递内容，子组件就可以渲染插槽的默认值：

```js
<template>
    <div>
        <h3>子组件</h3>
        <slot>
            <p>这是插槽的默认值</p>
        </slot>
    </div>
</template>
```

##### 具名插槽（插槽命名）

当子组件中有多个插槽时，为了区分它们，需要通过 `name` 属性给插槽进行命名：

```js
<template>
    <div>
        <h3>子组件</h3>
        <slot name="title"></slot>
        <slot name="content"></slot>
    </div>
</template>
```

后续，在父组件中，向对应的插槽中传递内容时，需要通过 `v-slot:插槽名称` 指令来指定插槽名称。

注意：`v-slot` 指令只能在组件或 `template` 身上使用。

```js
<template>
    <Child>
        <template v-slot:title>
            <h2>传递的文章标题</h2>
        </template>
        <template #content>
            <p>传递的文章内容</p>
            <p>传递的文章内容</p>
            <p>传递的文章内容</p>
            <p>传递的文章内容</p>
            <p>传递的文章内容</p>
        </template>
    </Child>
</template>
```

`v-slot:` 简写为 `#`。

##### 作用域插槽

当数据在子组件中，我们需要在子组件中对数据进行渲染，但是渲染数据的节点由父组件来决定。这种情况下，就需要使用作用域插槽。

子组件中设置 `<slot>` 和数据，同时在 `<slot>` 身上通过自定义属性将子组件数据传递给父组件。：

```js
<template>
    <div>
        <h3>子组件</h3>
        <slot :contentList="contentList"></slot>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                contentList: ["文章列表1", "文章列表2", "文章列表3"],
            };
        },
    };
</script>
```

在父组件中，使用子组件时，可以通过 `v-slot` 指令来接受子组件传递出来的数据：

```js
<template>
    <div>
        <Child v-slot="slotProps">
            <ul>
                <li v-for="item in slotProps.contentList" :key="item">{{item}}</li>
            </ul>
        </Child>
        <Child v-slot="slotProps">
            <ol>
                <li v-for="item in slotProps.contentList" :key="item">{{item}}</li>
            </ol>
        </Child>
    </div>
</template>
```

##### 具名插槽和作用域插槽

当一个 `<slot>` 既是作用域插槽，同时还有 name 命名，在使用时，可以通过以下方式设置：

```js
<Child>
    <template v-slot:title>
        <h2>传递的文章标题</h2>
    </template>
    <template v-slot:content="slotProps">
        <ul>
            <li v-for="item in slotProps.contentList" :key="item">{{item}}</li>
        </ul>
    </template>
</Child>
```

### 创建 Vue.js 全家桶项目

在终端中定位到需要存放项目的目录，然后执行以下命令创建项目：

```
vue create 项目名称
```

##### 1、选择安装模式

```
Vue CLI v4.5.13? Please pick a preset: (Use arrow keys)  Default ([Vue 2] babel, eslint)  Default (Vue 3) ([Vue 3] babel, eslint)> Manually select features
```

##### 2、选择安装插件

```
? Check the features needed for your project: ( ) Choose Vue version (*) Babel ( ) TypeScript ( ) Progressive Web App (PWA) Support (*) Router (*) Vuex>(*) CSS Pre-processors ( ) Linter / Formatter ( ) Unit Testing ( ) E2E Testing
```

##### 3、选择路由模式

```
? Use history mode for router? (Requires proper server setup for index fallback in production) (Y/n) n
```

##### 4、选择 CSS 预处理器

```
? Pick a CSS pre-processor (PostCSS, Autoprefixer and CSS Modules are supported by default): (Use arrow keys)> Sass/SCSS (with dart-sass)  Sass/SCSS (with node-sass)  Less  Stylus
```

##### 5、选择插件配置文件位置

```
? Where do you prefer placing config for Babel, ESLint, etc.? (Use arrow keys)> In dedicated config files  In package.json
```

##### 6、是否保存供以后使用

```
? Save this as a preset for future projects? (y/N) y? Save preset as: Vue-All
```

如果要删除配置可以在以下文件中将对应配置代码删除：

![image-20210914121317001](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210914121924.png)

##### 7、创建成功

```
  Successfully created project vue-demo.  Get started with the following commands: $ cd vue-demo $ npm run serve
```

##### 8、启动项目

在终端中进入到项目的根目录路径，执行以下命令启动项目：

```
npm run serve
```

出现以下提示，则表示项目启动成功：

```
 DONE  Compiled successfully in 3621ms                             下午2:08:17  App running at:  - Local:   http://localhost:8080/  - Network: http://192.168.40.69:8080/  Note that the development build is not optimized.  To create a production build, run npm run build.
```

`http://localhost:8080/` 就是项目的访问地址。

### 路由基础配置

##### 基础配置

Vue Router 的配置都是在 `src/router/index.js` 文件中进行。

```js
import Vue from 'vue' // 引入 Vue 
import VueRouter from 'vue-router' // 引入路由
Vue.use(VueRouter)
const routes = [
    //... 路由配置
]
// 创建路由实例对象
const router = new VueRouter({
    routes: routes  
})
// 暴露路由对象
export default router
```

暴露的路由对象，会在 `main.js` 中引入并注入到 Vue 实例中：

```js
// ...
// 引入路由实例对象
import router from './router'
new Vue({
    router, // 将路由对象挂载到 Vue 实例上，后续在任何组件中都可以通过 $router 访问路由对象
    // ...
}).$mount('#app')
```

##### 路由对象配置

在 `src/router/index.js` 文件中，有一个 `routes` 的变量，保存了一个数组：

```js
const routes = [
    //... 路由配置
]
```

这个数组，是路由的核心配置，整个 Vue 应用中所有页面的路由配置，都在该数组中进行。

例如，我们需要配置登录和注册两个页面的路由：

```js
import Login from '../views/login/Login.vue'
import Register from '../views/register/Register.vue'
const routes = [
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    }
]
```

其中：

- `path`：用来设置浏览器 `#` 后面的路径
- `name` ：路由名称
- `component`：路径匹配成功后要加载的组件

##### 路由出口

当浏览器的路径和路由对象的 `path` 匹配成功，对应的 `component` 会加载进来，但是组件最终渲染的位置，还需要通过路由出口 `<router-view>` 来设置：

```js
<template>
    <div id="app">
        <!-- 路由出口：设置路径匹配成功后组件的渲染位置 -->
        <router-view />
    </div>
</template>
```

### 路由跳转

Vue Router 路由跳转分为两种方式：

- 标签跳转
- 事件跳转

##### 标签跳转

```js
<router-link to="/register">没有账号？去注册</router-link>
```

##### 事件跳转

```js
export default {
    methods: {
        register() {
            // 跳转
            this.$router.push('/login');
        },
    },
};
```

##### 重定向

重定向是指可以将某一个 path 直接重定向到另一个 path。

例如，将 `/` 重定向到 `/login`：

```js
const routes = [
    {
        path: '/',
        redirect: '/login' // 重定向
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    // ...
]
```

以上代码表示，当用户访问 `/` 路径时，会直接跳转到 `/login`。

##### 通用路由

通用路由，是指任何路径都能匹配的路由：

```js
const routes = [
    // ...
    {
        path: '*',
        name: 'Error',
        component: Error
    }
]
```

通常我们用来渲染错误提示组件。即当页面路径和任何一个路由 path 都不匹配时，就进入通用路由，渲染错误提示页面给用户以提示：

```js
<template>
    <div>
        <h1>页面走丢了...</h1>
        <p>5秒之后跳转到首页</p>
    </div>
</template>
```

### 路由模式

Vue Router 的路由分为两种模式：

- history
- hash：路径上带有 `#`

```js
const router = new VueRouter({
    routes: routes,  // 路由配置
    mode: 'history'
})
```

不设置 `mode` 时，默认是 `hash` 模式。

### 路由懒加载

懒加载，指的就是路由所对应的组件，只有等到浏览器路径和 path 匹配成功后，才开始加载：

```js
const routes = [
    //...
    {
        path: '*',
        name: 'Error',
        component: () => import('../views/404/Error.vue')
    }
]
```

通常，用户访问率比较高，页面比较复杂的组件，采用传统的加载方式。用户访问率比较低，页面比较简单的组件，采用路由懒加载。

路由懒加载也可以写成以下形式：

```js
const Error = () => import('../views/404/Error.vue');
const routes = [
    // ...
    {
        path: '*',
        name: 'Error',
        component: Error
    }
]
```

### 嵌套路由

嵌套路由，指的是可以在路由对象中再嵌套一个子路由。每一个路由对象都有一个 `children` 属性用来设置嵌套路由。

##### 配置嵌套路由

例如，在首页 Home 中想要添加两个子路由，学生列表和学生新增：

```js
import Home from '../views/home/Home.vue'
import StudentsList from '../components/students/StudentsList.vue'
import StudentsAdd from '../components/students/StudentsAdd.vue'
const routes = [
    // ...
    {
        path: '/home',
        name: 'Home',
        component: Home,
        // 嵌套路由
        children: [
            {
                // 子路由的 path 不要加 /
                path: 'studentsList', 
                name: 'StudentsList',
                component: StudentsList,
            },
            {
                path: 'studentsAdd', 
                name: 'StudentsAdd',
                component: StudentsAdd
            }
        ]
    },
    // ...
]
```

子路由对象的属性和父路由对象的属性一致，但是需要注意：**子路由的 path 中不能添加 /**。

##### 嵌套路由出口

父路由中嵌套的子路由，意味着父组件中要渲染子组件，因此，我们还需要在父路由对应的组件中，设置子路由的路由出口：

```js
<template>
    <div>
        <header>
            <h1>蜗牛学苑学生管理系统</h1>
        </header>
        <main>
            <aside>
                <!-- 左侧菜单 -->
            </aside>
            <section>
                <!-- 渲染子路由组件 -->
                <router-view />
            </section>
        </main>
    </div>
</template>
```

##### 嵌套路由跳转

嵌套路由在跳转时，不管是用标签还是事件跳转，都需要设置完成的跳转路径：

```js
<aside>
    <!-- 左侧菜单 -->
    <dl>
        <dt>学生管理</dt>
        <dd><router-link to="/home/studentsAdd">新增学生</router-link></dd>
        <dd><router-link to="/home/studentsList">学生列表</router-link></dd>
    </dl>
</aside>
```

### axios 基本使用

##### 安装

```
npm i axios --save
```

##### 基本语法

##### 引入

在需要使用 axios 的组件中引入 axios：

```
import axios from 'axios';
```

##### 发送请求

```js
axios({
    url: '路径',
    method: 'GET',
    params: {
        // 参数
    }
})
axios({
    url: '路径',
    method: 'POST',
    data: {
        // 参数
    }
})
```

案例：

```js
import axios from "axios";
export default {
    data() {
        return {
            studentsData: [],
        };
    },
    created() {
        // 发送获取学生数据
        this.getStudents();
    },
    methods: {
        async getStudents() {
            const res = await axios({
                url: "http://47.98.128.191:3000/students/getStudents",
                method: "GET",
            });
            if(res.data.code) {
                this.studentsData = res.data.data.rows
            }
        },
    },
};
```

##### 全局配置

axios 的全局配置，通常都在 `main.js` 中来进行配置。

##### axios 基础路径

```js
import axios from 'axios';
axios.defaults.baseURL = 'http://47.98.128.191:3000'
```

##### 全局挂载

我们可以将 axios 对象挂载到 Vue 实例上：

```
Vue.prototype.$axios = axios;
```

后续在组件中再次使用 axios 时，就可以直接通过 `this` 访问：

```js
export default {
       // ...
    methods: {
        async getStudents() {
            const res = await this.$axios({
                url: "/students/getStudents",
                method: "GET",
            });
            // ...
        },
    },
};
```

### 动态路由

动态路由，指的就是路由的 path 中，有一部分内容是动态不固定的。

例如：

```
/home/studentsUpdate/001
/home/studentsUpdate/002
/home/studentsUpdate/003
```

以上三个路径对应的是一个路由，数字部分就是路由 path 中不固定的内容。

##### 配置动态路由

动态路由在 `/src/router/index.js` 中配置时也和普通路由不一样：

```js
const routes = [
    {
        // ...
        // 嵌套路由
        children: [
            // ...
            {
                // 动态路由
                path: 'studentsUpdate/:_id',
                name: 'StudentsUpdate',
                component: StudentsUpdate
            }
        ]
    },
    //...
]
```

path 中动态的部分，需要通过 `/:变量名` 来进行匹配，例如上例中的 `/:_id`。

##### 获取动态路由的参数

动态路由中，动态部分的数据，可以在组件中通过两种方式来获取：

- `this.$route.params`
- props

##### this.$route.params

我们可以在组件创建完成时，就获取路由中的数据：

```js
export default {
    created() {
        console.log(this.$route.params)
    },
};
```

#### props

如果要在组件中通过 props 来获取动态路由的数据，需要在配置路由时添加一个 `props: true` 的属性：

```js
const routes = [
    {
        // ...
        // 嵌套路由
        children: [
            // ...
            {
                // 动态路由
                path: 'studentsUpdate/:_id',
                props: true,
                name: 'StudentsUpdate',
                component: StudentsUpdate
            }
        ]
    },
    //...
]
```

然后在组件中，用 props 来接收数据：

```js
export default {
    props: ['_id'],
    created() {
        console.log(this._id);
    }
}
```

### 路由扩展

##### router-link 属性

router-link 除了常用的 to 属性外，还有一些其他的属性：

##### tag

用来设置 router-link 渲染后的标签：

```js
<router-link tag="button"></router-link>
```

##### replace

当该属性的值为 true 时，路由跳转后，新的路由记录会替代掉当前组件的路由记录。

```js
<router-link :replace="true"></router-link>
```

##### active-class

用来设置被激活的 router-link 的 class：

```js
<router-link active-class="active"></router-link>
```

##### 路由跳转

##### router-link

```js
<router-link :to="{ path: '/register' }">没有账号？去注册</router-link>
<router-link :to="{ name: 'Register' }">没有账号？去注册</router-link>
```

##### this.$router

push 方法除了可以传递字符串外，也可以传递对象：

```js
this.$router.push({ path: '/register'})
this.$router.push({ name: 'Register'})
```

除了 push 实现路由跳转外，还有其他方法：

```js
this.$router.replace('/register')
this.$router.go(1);
```

##### 路由传参 query

动态路由可以实现路由之间的传参，还可以使用 query。

跳转时，在路径后面用 `?` 分割参数：

```js
<router-link to="/register?_id=001">没有账号？去注册</router-link>
<router-link :to="{ path: '/register', query: { _id: 001 } }">没有账号？去注册</router-link>
```

在组件中接收时，可以通过 `this.$route.query`：

```js
export default {    created() {        console.log(this.$route.query._id)    }}
```

注意：query 传参跟动态路由无关，因此在配置路由时不需要配置成动态路由。

### 路由元信息

##### 基础语法

在路由配置文件中，每一个路由对象除了基本属性（path、name、component）外，还可以添加一个 meta 属性。

```js
const routes = [
    {
        children: [
            {
                path: 'studentsList',
                name: 'StudentsList',
                component: StudentsList,
                // 路由元信息
                meta: {
                    // 添加任意属性
                }
            },
        ]
    }
]
```

##### meta 搭配 keep-alive

`<keep-alive>` 除了可以包裹动态组件外，也可以用来包裹 `<router-view />`：

```js
<keep-alive>    
    <router-view />
  </keep-alive>
```

被 `<keep-alive>` 包裹的组件都会缓存，不会再销毁和重建，也就表示，所有从 `<router-view />` 渲染的组件都会被缓存。

如果我们希望，一部分路由组件会缓存，一部分路由组件不会缓存时，就可以通过 meta 去标记路由对象，由此来区分缓存和不缓存的路由：

```js
const routes = [
    {
        // ...
        // 嵌套路由
        children: [
            {
                // 子路由的 path 不要加 /
                path: 'studentsList',
                name: 'StudentsList',
                component: StudentsList,
                meta: {
                    isKeepAlive: false  // 不缓存
                }
            },
            {
                path: 'studentsAdd',
                name: 'StudentsAdd',
                component: StudentsAdd,
                meta: {
                    isKeepAlive: true // 缓存
                }
            },
            {
                // 动态路由
                path: 'studentsUpdate/:_id',
                props: true,
                name: 'StudentsUpdate',
                component: StudentsUpdate,
                meta: {
                    isKeepAlive: true  // 缓存
                }
            }
        ]
    },
    // ...
]
```

在渲染 `<router-view/>` 时，根据 meta 进行判断：

```js
<keep-alive>    
<router-view v-if="$route.meta.isKeepAlive" /></keep-alive>
<router-view v-if="!$route.meta.isKeepAlive" />
```

### 导航守卫

导航，路由正在发生变化。导航守卫，当路由发生变化时，可以通过守卫来控制路由的跳转或取消跳转。

##### 导航守卫分类

Vue 中的导航守卫根据作用范围，分为三类：

- 全局守卫
- 路由独享守卫
- 组件内的守卫

##### 全局守卫

##### 全局前置守卫

全局守卫中，有一个全局前置守卫。进入任意一个路由之前，都会触发该守卫函数：

```js
// 全局前置守卫
router.beforeEach((to, from, next) => {
    if (to.path == '/home') {
        const token = localStorage.token;
        if (token) {
            // 有 token
            next();
        } else {
            alert('你还未登录，请先登录');
            next('/login');
        }
    } else {
        next();
    }
})
```

##### 路由独享守卫

```js
const routes = [
    {
        path: '/home',
        name: 'Home',
        component: Home,
        // 路由独享守卫
        beforeEnter: (to, from, next) => {
            const token = localStorage.token;
            if (token) {
                // 有 token
                next();
            } else {
                alert('你还未登录，请先登录');
                next('/login');
            }
        }
    }
]
```

##### 组件内的守卫

###### 离开组件时

```js
export default {
    beforeRouteLeave(to, from, next) {
         if (this.student.name || this.student.age) {
            const isLeave = confirm('你还有数据未提交，确认离开吗？');
            if(isLeave) {
                next();
            }
        } else {
            next();
        }
    },
}
```

### API 的封装

API 的封装，指的是对 Vue 项目中所有的 axios 请求做一个统一管理，也就是把所有的 axios 请求放到一个文件中来进行管理。

##### 目录创建

在 `src` 目录中创建一个 `http` 目录，考虑到 axios 请求可以根据数据类型来分类管理，因此，在 `http` 目录中再创建一个 `modules` 目录，用来存放所有的请求模块。例如：学生请求模块（students.js）、班级请求模块（classes.js）…

##### 请求模块封装

学生请求模块代码如下：

```js
import axios from 'axios';
// 学生对象用来保存所有关于学生的请求
const students = {
    // 获取学生
    getStudents: function (params) {
        // 发送请求
        return axios({
            url: '/students/getStudents',
            method: 'GET',
            params
        })
    },
    // 删除学生
    deleteStudents: function (_id) {
        return axios({
            url: '/students/deleteStudents',
            method: 'DELETE',
            data: _id
        })
    }
}
export default students;
```

##### 模块汇总

由于某些组件中需要使用多个模块中的请求，所以，当把所有的请求划分成模块后，我们还需要再用一个对象将所有的模块做一个汇总。

在 `http` 目录中创建一个 api.js，在该文件中引入所有的请求模块对象：

```js
// 汇总所有的模块请求
import students from './modules/students.js'
import classes from './modules/classes.js'
import subjects from './modules/subjects.js'
const api = {
    students, classes, subjects
}
export default api;
```

最后将 api.js 文件在 `main.js` 中引入，并将 api 对象挂载在全局：

```js
import api from '@/http/api.js'
Vue.prototype.$api = api;
```

##### 组件调用 api 接口

因为 api 对象已经挂载到了全局，因此在组件中，可以直接通过 `this.$api` 访问：

```js
export default {
    methods: {
        async getStudents() {
            // 通过 this.$api 访问
            const res = await this.$api.students.getStudents({
                ...this.pageData,
            });
            // ...           
        },
    }
}
```

### Vuex基本使用

Vuex 是一个专为 Vue.js 应用程序开发的**状态管理模式**。也可以称之为“状态机”。

Vuex 可以看作是就一个数据仓库，Vuex 中可以用来管理公共数据，管理指的是可以存，还可以修改。

##### 安装

1. `npm i vuex`
2. `vue add vuex  # 会自动生成配置代码`

##### 配置

在 `src/store/index.js` 文件中，对 Vuex 进行配置，最后将配置好的仓库对象，暴露给 `main.js` 中引入，并做一个全局的挂载。

##### state 和 mutations

###### 仓库中配置 state 和 mutations

state 用于保存任意数据，mutations 用于设置修改 state 的方法。

```js
export default new Vuex.Store({
    // 保存数据
    state: {
        count: 0,
    },
    // 修改数据的方法
    mutations: {
        increment(state) {
            state.count++;
        },
        decrement(state) {
            state.count--;
        },
        // payload 用于接收外部传递的数据
        inputCount(state, payload) {
            state.count = payload;
        }
    },
})
```

说明：

1. mutations 中的方法，第一个参数永远都是 state，第二个参数，用于接收外部传递的数据；
2. mutations 是唯一一个修改 state 途径；

##### 组件中使用 state 和 mutations

1）state

组件中可以通过 `this.$store.state` 访问 state 中的数据，通常我们会将这个数据交给组件的 computed：

```js
export default {
    computed: {
        count() {
            return this.$store.state.count;
        }
    }
};
```

渲染时就直接使用计算属性即可：

```js
<h3>计数器：{{count}}</h3>
```

##### mutations

如果要修改 state，需要从组件中调用 mutations 中的方法，来实现 state 的修改：

```js
<template>
    <div>
        <h3>计数器：{{count}}</h3>
        <button @click="$store.commit('decrement')">-1</button>
        <button @click="increment">+1</button>
    </div>
</template>
<script>
export default {
    computed: {
        count() {
            return this.$store.state.count;
        }
    },
    methods: {
        increment() {
            // 触发 mutations 的方法
            this.$store.commit('increment');
        }
    }
};
</script>
```

还可以往 mutations 的方法中传值：

```js
<template>
    <div>
        <h3>计数器：{{count}}</h3>
        <input type="text" v-model.lazy="num">
    </div>
</template>
<script>
    export default {
        data() {
            return {
                num: ''
            }
        },
        watch: {
            num() {
                this.$store.commit('inputCount', this.num);
            }
        },
        computed: {
            count() {
                return this.$store.state.count;
            }
        },
    };
</script>
```

##### getters

getters 的作用类似于组件中的 computed。

##### 仓库中配置 getters

```js
export default new Vuex.Store({
    // 保存数据
    state: {
        count: 1,
    },
    // 计算属性：从 state 中得到一条新数据
    getters: {
        sum(state) {
            return state.count + state.count;
        }
    }
})
```

##### 组件中使用 getters

```js
export default {
    computed: {
        sum() {
            return this.$store.getters.sum
        }
    }
}
```

##### actions

##### 仓库中配置 actions

1）设置 actions 中的方法

```js
export default new Vuex.Store({
    // 异步方法
    actions: {
        // 获取学生数据
        async getStudentsAsync(context) {
            // 调用封装的 api 发送请求
            const { data } = await $api.students.getStudents();
        }
    }
})
```

说明：

1. actions 中的方法用来发送异步请求；
2. actions 中的方法默认第一个参数都是 context（仓库对象），第二个参数用来接收外部传递的数据；

##### 组件中调用 actions

在组件中调用 actions 的方法，通过 `dispatch()`：

```js
export default {
    created() {
        this.getStudents();
    },
    methods: {
        getStudents() {
            // 调用 actions 的方法
            this.$store.dispatch('getStudentsAsync');
        }
    }
}
```

##### actions 调 mutations

由于 actions 中不能修改 state，如果要修改 state，需要在 actions 中去调用 mutations 的方法，将数据传给 mutations，让 mutations 去修改 state：

```js
export default new Vuex.Store({
    // 保存数据
    state: {
        studentsData: []
    },
    mutations: {
        GET_STUDENTS(state, payload) {
            state.studentsData = payload;
        }
    },
    // 异步方法
    actions: {
        // 获取学生数据
        async getStudentsAsync(context) {
            // 调用封装的 api 发送请求
            const { data } = await $api.students.getStudents();
            // 将数据保存到 state:先调用 mutations 的方法，将数据传给 mutations
            if(data.code) {
                context.commit('GET_STUDENTS', data.data.rows);
            }
        }
    }
})
```

##### 辅助函数

辅助函数，就是辅助我们在组件中能够更方便的获取仓库中的数据和方法。

Vuex 中提供了四个辅助函数：

- `mapState`
- `mapGetters`
- `mapMutations`
- `mapActions`

##### 引入

```js
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex';
```

##### 使用

mapState 和 mapGetters 都是用于获取数据的，因此，这两个方法都是在 computed 中调用，将仓库中的 state 和 getters，转换为组件自己的计算属性：

```js
export default {
    computed: {
        ...mapState(['数据名1', '数据名2', '数据名3']),
        ...mapGetters(['数据名1', '数据名2', '数据名3']),
    }
}
```

mapMutations 和 mapActions 都是用于获取方法的，因此，这两个方法都是在 methods 中调用，将仓库中的 mutations 的方法和 actions 的方法，转换为组件自己的方法：

```js
export default {
    methods: {
        ...mapMutations(['方法名1', '方法名2', '方法名3']),
        ...mapActions(['方法名1', '方法名2', '方法名3']),
    }
}
```

### 模块化

模块化是指，可以通过 `modules` 属性将仓库划分成多个小模块。

##### 创建目录

在 store 中创建一个 modules 目录，用来存放所有的仓库模块，例如：学生模块、班级模块…

##### 配置模块

以学生模块为例，我们在 modules 中创建一个 students.js：

```js
import $api from '@/http/api.js'
export default {
    // 解决命名空间冲突
    namespaced: true,
    state: {
        studentsData: [],
        total: 0,
        pages: 0
    },
    mutations: {
        GET_STUDENTS(state, payload) {
            state.studentsData = payload.rows;
            state.total = payload.total;
            state.pages = payload.pages;
        }
    },
    // 异步方法
    actions: {
        // 获取学生数据
        async getStudentsAsync(context, payload) {
            // 调用封转的 api
            const { data } = await $api.students.getStudents(payload);
            // 将数据保存到 state:先调用 mutations 的方法，将数据传给 mutations
            if (data.code) {
                context.commit('GET_STUDENTS', data.data);
            }
        }
    },
}
```

说明：

1. 模块中的属性和仓库中的属性一致，用法一致；
2. 模块对象中要添加一个 `namespaced: true` 解决命名冲突问题；

##### 引入仓库模块

模块配置完成后，需要在主仓库 `store/index.js` 中引入后才能生效：

```js
// ..
import students from './modules/students.js'
import counter from './modules/counter.js'
// ...
// 创建一个仓库实例对象
export default new Vuex.Store({
    // 模块化
    modules: {
        counter,
        students
    }
})
```

##### 组件中获取辅助函数

如果仓库进行了模块划分，组件中获取辅助函数的方式需要发生改变：

```js
import { createNamespacedHelpers } from "vuex";
const { mapState, mapActions } = createNamespacedHelpers("students");
```

辅助函数获取成功后，使用方式和之前一致。

如果在一个组件中，要获取多个模块的辅助函数：

```js
const { mapState, mapActions } = createNamespacedHelpers("students");
const { mapState: classesState, mapActions: classesActions } = createNamespacedHelpers("classes");
```

### 新增班级流程

我们以新增班级功能为例，来梳理组件搭配 Router 和 Vuex 的完整开发流程。

### 创建组件

找到对应的目录，创建一个新增班级的组件 `ClassesAdd.vue`，并完成组件的静态页面节点。

参考代码：

```
<template>    <div>        <h3>新增班级</h3>        <div>            <label>班级名称：</label>            <input type="text" />        </div>        <div>            <button>确认新增</button>        </div>    </div></template>
```

### 配置路由

新增班级的组件创建成功后，需要在浏览器中将组件显示出来。因此，需要在路由配置中添加该组件对应的路由。

找到 `/src/router/index.js` 文件，在首页的子路由中添加“新增班级”的路由。

参考代码：

```
import ClassesAdd from '../components/classes/ClassesAdd.vue';const routes = [    {        path: '/home',        name: 'Home',        component: Home,        children: [            // ...其他子路由            {                path: 'classesAdd',                name: 'ClassesAdd',                component: ClassesAdd,            }        ]    }]
```

配置完成后，可以尝试在浏览器中切换 `http://localhost:8080/home/classesList` 路径，看能否显示新增班级组件。

### 路由跳转

确认新增班级组件渲染无误后，再在首页菜单中添加对应的“新增班级”的跳转链接：

```
<dl>    <dt>班级管理</dt>    <dd>        <router-link to="/home/classesAdd">新增班级</router-link>    </dd>    <dd>        <router-link to="/home/classesList">班级列表</router-link>    </dd></dl>
```

### 事件处理

组件能够成功渲染后，回到组件中。

如果组件中的功能，需要添加事件，就在静态页面的基础之上，设置组件的事件，包括事件中需要获取的一些页面数据。

例如新增班级功能，需要给【新增】按钮添加点击事件，并在事件中获取输入框用户输入的值。

参考代码：

```
<template>    <div>        <h3>新增班级</h3>        <div>            <label>班级名称：</label>            <input type="text" v-model.lazy="classes.name" />        </div>        <div>            <button @click="addClasses">确认新增</button>        </div>    </div></template><script>    export default {        data() {            return {                classes: {                    name: "",                },            };        },        methods: {            addClasses() {                console.log('获取输入框数据', this.classes.name);            },        },    };</script>
```

### 发送请求

当事件成功触发，且能正确获取到输入框的值以后，开始准备发送请求。

发送请求的流程为：**组件调仓库，仓库调 API**。

但是，代码的书写流程需要反着来，因此我们需要先去 `http` 目录中设置“新增班级”的请求 API。

#### 1、配置请求 API

找到 `/http/modules/classes.js` 文件（没有就自己新建），在该文件中添加“新增班级”的请求方法：

```
import axios from 'axios';const classes = {    // 获取班级数据    // ...    // 新增班级    addClasses(data) {        return axios({            url: '/classes/addClasses',            method: 'POST',            data: data        })    }}export default classes;
```

说明：data 形参用于接收后续传递过来的新班级数据。

#### 2、汇总请求 API

请求方法配置好后，查看一下 `http/api.js` 文件中，是否有将该请求模块进行汇总，若没有，则参考以下代码将班级模块汇总到 API 中：

```
// 汇总所有的模块请求// ...import classes from './modules/classes.js'const api = {     // ...     classes}export default api;
```

#### 3、配置仓库 actions

API 完成后，下一步开始配置仓库。

因为仓库做了模块化处理，所以需要找到班级对应的 `store/module/classes.js` 班级模块文件（如果没有则自己创建）。然后在 `actions` 属性中配置“新增班级”的异步方法：

```
import $api from '@/http/api.js'export default {    namespaced: true,    // ...    actions: {        // ...其他异步方法        // 新增班级        async addClassesAsync(context, payload) {            // 调用 api 的方法，并将新班级数据 payload 传递给 api            const { data } = await $api.classes.addClasses(payload);            // 输出后端返回的请求结果            console.log(data);        }    }}
```

说明：payload 是用来接收组件传递的新班级数据，并同时传递给 api 中封装的方法。

#### 4、组件调用仓库 actions

API 和仓库都配置完成后，回到组件中，在组件的方法中调用仓库的方法。

##### 1）获取辅助函数

组件要操作仓库，首先需要获取都辅助函数：

```js
import { createNamespacedHelpers } from "vuex";
const { mapActions } = createNamespacedHelpers("classes");
```

##### 2）获取仓库方法

通过辅助函数获取仓库中定义好的 actions 方法：

```js
export default {
    // ...
    methods: {
        // addClassesAsync 是仓库中 actions 的方法的名字
        ...mapActions(["addClassesAsync"]),
        //...
    },
};
```

##### 3）执行 actions 的方法

通过辅助函数获取到 `addClassesAsync` 方法后，就可以在组件自己的方法调用该方法：

```js
export default {
    data() {
        return {
            classes: {
                name: "",
            },
        };
    },
    methods: {
        ...mapActions(["addClassesAsync"]),
        async addClasses() {
            // 调用 actions 的方法，同时将班级数据传递给 actions
            this.addClassesAsync(this.classes);
        },
    },
};
```

到此，组件调仓库，仓库调 API 流程完成。

#### 5、处理请求结果

在页面上点击新增按钮，触发组件的新增事件，组件调仓库，仓库调 API，最终在仓库的 actions 中输出请求结果。当确认结果无误后，将仓库中拿到的结果返回给组件：

```js
import $api from '@/http/api.js'
export default {
    //...
    actions: {
        //...
        async addClassesAsync(context, payload) {
            const { data } = await $api.classes.addClasses(payload);
            // 数据返回给“新增班级”组件
            return data;
        }
    }
}
```

由于 actions 中的方法是通过 `async` 定义的异步方法，因此在组件中接收该方法的返回值时，需要通过 await 来接收。

新增班级组件代码如下：

```js
export default {
    data() {
        return {
            classes: {
                name: "",
            },
        };
    },
    methods: {
        ...mapActions(["addClassesAsync"]),
        async addClasses() {
            // 通过 await 接收仓库 return 的结果
            const data = await this.addClassesAsync(this.classes);
            if (data.code) {
                alert("班级新增成功");
                this.classes = {}; // 清空输入框
                this.$router.push('/home/classesList');
            }
        },
    },
};
```

### axios 的封装

在项目中，很多 axios 请求都需要有相同的配置，例如 url 的基础路径、请求头添加 token 等。

axios 中提供的解决方案有两种：

1. `axios.defaults` 进行统一配置
2. 设置 axios 的拦截器

##### axios.defaults

```js
axios.defaults.baseURL = 'http://47.98.128.191:3000';
```

### 拦截器

axios 中的拦截器分为两种：请求拦截器、响应拦截器。

- 请求拦截器的作用，就是在请求发送到后端去之前，将请求拦截下来。
- 响应拦截器的作用，就是在后端响应结果达到前端之前，将响应拦截下来。

考虑到拦截器的配置代码比较多，因此我们建议大家单独创建一个 JS 文件来对 axios 拦截器进行配置。例如 `http/axios.js`。配置完成后，在 `main.js` 中引入执行该文件即可：

```js
// 运行以下文件，给 axios 添加拦截器
import '@/http/axios.js';
```

#### 请求拦截器

在请求拦截器中给所有的 axios 请求头中添加 token：

```js
import axios from 'axios'
axios.interceptors.request.use((config) => {
    // 请求拦截成功
    // 1. 获取本地存储中的 token
    const token = localStorage.token;
    // 2. 将 token 添加到请求头
    config.headers.Authorization = token;
    // 3. 让请求继续发往后端
    return config;
}, (err) => {
    // 请求拦截失败
    return Promise.reject(err);
});
```

#### 响应拦截器

当后端返回一些报错信息时，如果要对这些信息进行处理，就可以在 axios 的响应拦截器来实现：

```js
import router from '@/router';
// 响应拦截器
axios.interceptors.response.use((res) => {
    // 响应成功时
    return res;
}, (err) => {
    // 响应失败时
    if (err && err.response && err.response.status) {
        switch (err.response.status) {
            case 401:
                alert('身份认证失败，请重新登录');
                // 跳转到登录页面
                router.push('/login');
                break;
            case 404:
                err.message = '资源找不到'
                break;
            case 500:
                err.message = '服务器错误';
                break;
            default:
                err.message = '网络出错';
        }
    } else {
        err.message = '网络出错';
    }
    return Promise.reject(err);
})
```

### 身份认证流程

##### 登录

首先实现基本的登录功能，前端发送登录请求，后端返回登录结果。

登录成功时将 token 保存在本地存储中：

```js
<template>
    <div>
        <h1>用户登录</h1>
        <div>
            <label>账号：</label>
            <input type="text" v-model.lazy="users.username" />
        </div>
        <div>
            <label>密码：</label>
            <input type="text" v-model.lazy="users.password" />
        </div>
        <button @click="login">登录</button>
        <router-link to="/register">没有账号？去注册</router-link>
    </div>
</template>
<script>
import { createNamespacedHelpers } from "vuex";
const { mapActions } = createNamespacedHelpers("users");
export default {
    data() {
        return {
            users: {
                username: "",
                password: "",
            },
        };
    },
    methods: {
        ...mapActions(["loginAsync"]),
        async login() {
            // 发送登录请求
            const data = await this.loginAsync(this.users);
            console.log(data);
            if(data.code) {
                alert('登录成功');
                localStorage.token = data.token;
                this.$router.push("/home");
            } else {
                alert('账号或密码错误，登录失败')
            }
        },
    },
};
</script>
```

##### 导航守卫验证身份

在进入 Home 首页的导航守卫中，验证本地是否有 token。

- 如果没有 token，直接提示未登录请先登录，然后通过 `next('/login')` 跳转到登录页；
- 如果有 token，通过 getUserInfo 请求将 token 发送到后端验证 token 是否过期：

```js
const routes = [
    {
        path: '/home',
        name: 'Home',
        component: Home,
        // 路由独享守卫
        beforeEnter: async (to, from, next) => {
            const token = localStorage.token;
            if (token) {
                // 判断 token 是否过期
                // 发送“获取用户信息”的请求，将 token 携带到后端验证有效期
                const { data } = await $api.users.getUserInfo();
                if (data.code) {
                    next();
                }
            } else {
                alert('你还未登录，请先登录');
                next('/login');
            }
        },
    }
]
```

##### 请求头添加 token

如果单独给每一个请求单独添加 token 会很麻烦，因此我们考虑使用请求拦截器，直接给所有 axios 请求统一添加 token。

参考[《axios 封装》](http://www.woniuxy.com/sc/toNote/9570-457)笔记，创建 axios 拦截器的封装文件，通过封装 axios 给所有的请求头添加 token。

##### 处理错误信息

当验证到用户的 token 已经失效时，后端会返回 401 的报错，我们需要在 axios 的响应拦截器中处理错误信息，给用户相关提示，并跳转到登录页面。

具体代码参考[《axios 封装》](http://www.woniuxy.com/sc/toNote/9570-457)笔记。

##### 保存并渲染用户

在 Home 的导航守卫中，当 token 验证成功，后端会返回用户信息。我们可以将用户信息保存到 state 中，方便其他组件的使用。

在 `store/index` 中设置用户信息初始值以及修改用户信息的方法：

```js
export default new Vuex.Store({
    state: {
        userInfo: null
    },
    mutations: {
        GET_USER_INFO(state, payload) {
            state.userInfo = payload;
        }
    },
    // 模块化
    modules: {
        //...
    }
})
```

在导航守卫中，引入 store 仓库对象，触发 mutations 的方法：

```js
import store from '@/store';
const routes = [
    {
        path: '/home',
        name: 'Home',
        component: Home,
        // 路由独享守卫
        beforeEnter: async (to, from, next) => {
            const token = localStorage.token;
            if (token) {
                // 判断 token 是否过期
                // 发送“获取用户信息”的请求，将 token 携带到后端验证有效期
                const { data } = await $api.users.getUserInfo();
                if (data.code) {
                    // 通过仓库对象调用 mutations 的方法,将用户信息保存到 state 中
                    store.commit('GET_USER_INFO', data.data);
                    next();
                }
            } else {
                alert('你还未登录，请先登录');
                next('/login');
            }
        },
    }
]
```

最后在组件中获取仓库 state 渲染即可：

```js
<div>
    <span>欢迎你：</span>
    <strong>{{$store.state.userInfo.username}}</strong>
</div>
```

### Vue3 基础语法

#### 一、组件嵌套

在 Vue3 中，通过 `import` 引入子组件后，不需要再经过 `components` 属性配置：

```js
<template>
    <HelloWorld></HelloWorld>
</template>
<script>
import HelloWorld from "./components/HelloWorld.vue";
</script>
```

#### 二、Fragment

Vue3.0 中引入了类似于 React 中的 Fragment 组件功能，即 `<template>` 中的内容不再需要根节点包裹：

```js
<template>
    <h1>Hello Vue3.0</h1>
    <h1>Hello Vite</h1>
</template>
```

#### 三、setup

为了开始使用组合式 API，我们首先需要一个可以实际使用它的地方。在 Vue 组件中，我们将此位置称为 `setup`。

在 Vue3.0 正式版中 setup 的使用语法如下：

```js
<script>
export default {
      setup() {
    }
}
</script>
```

在 Vue3.0 的新提案中 setup 的语法更新如下：

```js
<script setup>
</script>
```

#### 四、reactive 数据

在 Vue3.0 中，通过 reactive 方法来设置组件的初始数据：

```js
<script setup>
import { reactive } from "vue";
const state = reactive({
    todos: [
        { _id: 1, value: "学习 HTML", done: false },
        { _id: 2, value: "学习 CSS", done: true },
        { _id: 3, value: "学习 JS", done: false },
    ],
});
</script>
```

访问数据都通过 `state` 对象进行访问：

```js
<template>
    <ul>
        <li v-for="item in state.todos" :key="item._id">{{item.value}}</li>
    </ul>
</template>
```

#### 五、computed 计算属性

Vue3.0 中，计算属性还是通过 `computed` 来设置，但是语法上同 Vue2.0 有一些区别：

```js
<script setup>
import { computed } from "vue";
const 计算属性名 = computed(
    () => {
        return 计算属性的值
    }
);
</script>
```

例如我们要统计 TodoList 中代办事项的完成数：

```js
<template>
    <span>{{doneTotal}}/{{total}}</span>
</template>
<script setup>
import { computed, reactive } from "vue";
const state = reactive({
    todos: [
        { _id: 1, value: "学习 HTML", done: false },
        { _id: 2, value: "学习 CSS", done: true },
        { _id: 3, value: "学习 JS", done: false },
    ]
});
// 计算属性
const total = computed(
    () => state.todos.length
);
const doneTotal = computed(
    () => state.todos.filter((item) => item.done).length
);
</script>
```

#### 五、事件方法

Vue3.0 中设置事件监听的方式还是和 Vue2.x 一样：

```js
<input type="text" v-model="state.todo"/>
<button @click="addTodo">新增</button>
```

但是在 `<script>` 中设置事件处理函数的方式发生了改变：

```js
<script setup>
import { reactive } from "vue";
const state = reactive({
    todo: "",
    todos: [
        { _id: 1, value: "学习 HTML", done: false },
        { _id: 2, value: "学习 CSS", done: true },
        { _id: 3, value: "学习 JS", done: false },
    ],
    newId: 4,
});
// 事件处理函数
const addTodo = () => {
    state.todos.push({
        _id: state.newId++,
        value: state.todo.value,
        done: false,
    });
};
</script>
```

#### 六、watch 侦听器

Vue3.0 中 `watch` 的语法发生了改变：

```js
<script setup>
// 引入 watch
import { watch } from "vue";
watch(
    () => 需要侦听的数据,
    (新值, 旧值) => {
        // 数据发生改变时执行该方法
    }
)    
</script>
```

例如在 Todolist 中，我们想要侦听输入框的值 `todo` 的变化，当该值发生改变时，触发 `addTodo` 方法：

```js
<script setup>
import { reactive, watch } from "vue";
const state = reactive({
    todo: '',
    // ... 其他数据
});
const addTodo = () => {
    // ...
};
watch(
    () => state.todo,
    () => {
        addTodo();
    }
);
</script>
```

#### 七、watchEffect

Vue3.0 中，除了保留 `watch` 侦听器外，还新增了一个 `watchEffect`，可以在响应式地跟踪其依赖项时立即运行一个函数，并在更改依赖项时重新运行它。

```js
<script setup>
import { watchEffect } from "vue";
const addTodo = () => {
    // ...
};
watchEffect(() => {
    addTodo();
});
</script>
```

watch 和 watchEffect 对比，watchEffect 的特点如下：

- 只需要接收一个回调函数作为参数；
- 回调函数会在页面首次渲染时执行一次；
- 只要回调函数中依赖的数据发生改变，该回调函数就会重新执行；
- 无法追踪到变化前后的值；

#### 八、生命周期函数

Vue3.0 中的生命周期函数是在 Vue2.x 的生命周期函数前面加上`on`：

```js
<script setup>
    import { onMounted } from "vue";  
    onMounted(() => {    
        console.log("onMounted");
    });
</script>
```

下表包含在 setup 内部调用生命周期钩子：

| 选项式 API        | Hook inside `setup` |
| :---------------- | :------------------ |
| `beforeCreate`    | Not needed          |
| `created`         | Not needed          |
| `beforeMount`     | `onBeforeMount`     |
| `mounted`         | `onMounted`         |
| `beforeUpdate`    | `onBeforeUpdate`    |
| `updated`         | `onUpdated`         |
| `beforeUnmount`   | `onBeforeUnmount`   |
| `unmounted`       | `onUnmounted`       |
| `errorCaptured`   | `onErrorCaptured`   |
| `renderTracked`   | `onRenderTracked`   |
| `renderTriggered` | `onRenderTriggered` |

### Vue3 使用路由

#### 一、下载 Vue Router

通过以下命令在 Vue3.0 项目中下载最新版本的 Vue Router：

```js
npm install vue-router@next
```

#### 二、配置路由

在 `src` 目录中创建 `router/index.js` 文件，作为路由的入口配置文件：

```js
import { createRouter, createWebHistory } from "vue-router";
const routes = [
    {
        // 路由对象
    }
]
export default createRouter({
    history: createWebHistory(),
    routes
})
```

#### 三、全局注入路由

在 `main.js` 中引入路由对象：

```js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
createApp(App).use(router).mount('#app')
```

#### 四、组件中使用路由

Vue3.0 中的路由，在模板中还是可以使用 `<router-link>` 和 `<router-view>` 组件 ，但是在 `setup` 中的使用有所不同。

##### 1、获取路由示例对象

```js
<script setup>
    import { useRouter } from "vue-router";
    // 实例化路由
    const router = useRouter();
</script>
```

##### 2、获取当前路由信息对象

```js
<script setup>
    import { useRoute } from "vue-router";
    // 当前路由信息对象
    const route = useRoute();
</script><script setup>    import { useRoute } from "vue-router";    // 当前路由信息对象    const route = useRoute();</script>
```

### Vue3 使用 Vuex

#### 一、下载 Vuex

通过以下命令在 Vue3.0 项目中下载最新版本的 Vuex：

```
npm i vuex@next
```

#### 二、配置状态机

在 `src` 目录中创建 `store/index.js` 文件，作为状态机的入口配置文件：

```js
import { createStore } from 'vuex';
export default createStore({
    state: {
    },
    mutations: {
    },
    actions: {
    },
    modules: {
    }                       
})
```

#### 三、全局注入状态机

在 `main.js` 中引入状态机对象：

```js
import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
createApp(App).use(store).mount('#app')
```

#### 四、组件中使用状态机

```js
<script setup>
import { useStore } from "vuex";
const store = useStore();
onMounted(() => {
    console.log(store.state.num)
});
</script>
```

### ElementUI 安装

##### 创建 Vue.js 项目

首先需要先创建好一个 Vue.js 项目，然后在项目中单独引入 ElementUI。

##### 引入 ElementUI

在项目根目录中，执行以下命令：

```
vue add element
```

该命令会帮我们自动下载 ElementUI 依赖包，同时会自动生成 ElementUI 的基础配置文件和代码。

##### 1、引入方式

```
? How do you want to import Element? (Use arrow keys)> Fully import  Import on demand
```

- `Fully import`：完整引入
- `Import on demand`：按需引入，指的就是自己要使用某一个组件时自己单独去引入该组件

##### 2、SCSS 变量文件

```
? Do you wish to overwrite Element's SCSS variables? (y/N) y
```

##### 3、选择区域

```
? Choose the locale you want to load (Use arrow keys)> zh-CN  zh-TW  af-ZA  ar  bg  ca  cs-CZ
```

##### 注意事项

如果安装失败的可以检查以下 Nodejs 的版本号，太高或太低都行，建议最低 12.x，最高采用目前 Nodejs 官方的 LTS 稳定版，例如下图中的 v14.17.6：

#### 样式穿透

如果要在 `<style>` 中使用样式穿透，需要先添加 `scoped` 属性。

```
<style scoped></style>
```

样式穿透的语法有三种：

- `>>>`：只作用于 CSS
- `::v-deep`：只作用于 Sass
- `/deep/`：只作用于 Less

示例代码：

```js
<style scoped>
    .el-menu >>> {
        border-right: none;
    }
</style>
<style scoped lang="scss">
    .el-menu ::v-deep {
        border-right: none;
    }
</style>
```

## mixins 混入

混入，实际上就是一个对象。该对象可以拥有所有组件的属性，例如：data、computed、watch…

因此，可以使用 mixins 混入对象来提取多个组件之间的公共 JS 代码。

### 基础语法

```js
const myMixins = {
    data() {
        return {
            // ...
        }
    },
    computed: {
        // ...
    },
    watch: {
        // ...
    }
}
```

##### 组件配置混入对象

每一个组件对象都有一个 mixins 属性，来配置混入对象：

```js
export default {
    mixins: [myMixins]
}
```

设置了混入对象后，组件还是可以继续设置自己的 data、computed 等。最终解析时，会将混入对象的属性和组件自身的属性进行合并。

#### 案例代码

我们以列表渲染功能为例，来封装一个混入对象。

#### 1、创建目录

在 `src` 目录中创建一个 `mixins` 目录，用来存放所有项目中需要用到的混入对象。

在 `mixins` 中创建一个 `list.js`，用来配置列表混入对象。

#### 2、创建混入对象

```js
    data() {
        return {
            pageData: {
                pageSize: 5,
                currentPage: 1
            }
        }
    },
    created() {
        this.getDataAsync(this.pageData);
    },
    computed: {
        ...mapState(["rows", "pages", "total"]),
    },
    methods: {
        ...mapActions(["getDataAsync", "deleteDataByIdAsync"]), 
        async handleDelete(_id) {
            const res = await this.deleteDataByIdAsync({ _id });
            if (res.code) {
                this.$message({
                    message: "数据删除成功",
                    type: "success",
                });
                this.getDataAsync(this.pageData);
            } else {
                this.$message.error(res.message);
            }
        },
    }
}
```

#### 3、封装混入对象

针对当前列表功能来说，我们在混入对象中使用到了 `mapState` 等辅助函数，因此，还需要将获取辅助函数的代码也设置在混入对象的文件中：

```js
import { createNamespacedHelpers } from "vuex";
const { mapActions, mapState } = createNamespacedHelpers('students');
const listMixins = {
    // ...
}
```

但是，不同列表组件中使用的仓库模块名是不一样的，因此我们只能将混入对象封装到一个函数中，然后不同的仓库模块名通过传参来进行处理：

```js
import { createNamespacedHelpers } from "vuex";
function listMixins(params) {
    const { mapActions, mapState } = createNamespacedHelpers(params);
    return {
        data() {
            return {
                // ...
            }
        },
        // ....
    }
}
```

#### 4、组件使用混入对象

组件中，引入混入对象的函数，并调用获取到函数的返回值，调用时传递对应的模块名：

```js
import list from "@/mixins/list.js";
export default {
    mixins: [list("students")],
};
```

## 自定义指令

Vue 中除了内置的指令外，我们还可以自己定义指令。

### 指令分类

自定义指令分为全局和局部：

#### 全局指令

全局指令可以作用于所有组件：

```js
Vue.directive('指令名', {
    // 指令配置
})
```

#### 局部指令

局部指令只作用于当前组件：

```js
export default {
    directives: {
        指令名: {
            // 指令配置
        }
    }
}
```

### 钩子函数

一个指令定义对象可以提供如下几个钩子函数 (均为可选)：

- `bind`：只调用一次，指令第一次绑定到元素时调用。在这里可以进行一次性的初始化设置。
- `inserted`：被绑定元素插入父节点时调用（仅保证父节点存在，但不一定已被插入文档中）。
- `update`：所在组件的 VNode 更新时调用，**但是可能发生在其子 VNode 更新之前**。指令的值可能发生了改变，也可能没有。但是你可以通过比较更新前后的值来忽略不必要的模板更新 (详细的钩子函数参数见下)。
- `componentUpdated`：指令所在组件的 VNode **及其子 VNode** 全部更新后调用。
- `unbind`：只调用一次，指令与元素解绑时调用。

我们可以在钩子函数中定义指令的内容：

```js
Vue.directive('指令名', {
      bind (el, binding, vnode, oldVnode) {
        // 指令内容
    },
    inserted (el, binding, vnode, oldVnode) {
        // 指令内容
    },
      // ...
})
```

参数说明：

- `el`：指令所绑定的元素，可以用来直接操作 DOM。
- `binding`：一个对象，包含指令的相关信息，例如：指令名称、指令的绑定值等。
- `vnode`：Vue 编译生成的虚拟节点。
- `oldVnode`：上一个虚拟节点，仅在 `update` 和 `componentUpdated` 钩子中可用。

### 案例：权限判断

在 `src` 中创建一个 `directives` 目录，用来存放项目中所有的自定义指令，然后在其中创建一个 `auth.js`，用来配置权限判断的全局指令：

```js
import Vue from 'vue'
import store from '@/store';
// 全局指令
Vue.directive('auth', {
    inserted: (el) => {
        // 判断用户权限
        if (store.state.userInfo.auth != 1) {
            // el.parentElement.removeChild(el);
            el.setAttribute('disabled', true);
            // 添加禁用样式
            el.classList.add('is-disabled');
        }
    }
})
```

说明：

- `auth` 是指令的名字，在元素身上使用时，直接通过 `v-auth` 使用；
- `inserted` 是自定义指令提供的钩子函数，当元素被插入到父节点的时候调用。

最后，在 `main.js` 中引入该文件：

```js
import '@/directives/auth.js';
```

指令生效后，在指定节点身上使用即可：

```js
<button v-auth>删除</button>
```

### Echarts

#### 下载

```
npm i echarts --save
```

#### 引入

```
import * as echarts from 'echarts'
```

#### 使用 Echarts

##### 1、初始化 Echarts 实例对象

先在 HTML 中创建一个节点，用来绘制图标：

```js
<div class="myCharts"></div>
.myCharts {
    width: 300px;
    height: 300px;
}
```

在 `mounted` 中，获取节点的原生 JS 对象：

```js
export default {
    mounted() {
        const myChartsNode = document.querySelector(".myCharts");
    }
}
```

初始化 Echarts 对象：

```js
export default {
    mounted() {
        const myChartsNode = document.querySelector(".myCharts");
        // 初始化 Echarts 对象
        const myCharts = echarts.init(myChartsNode);
    }
}
```

#### 2、设置数据

```js
export default {
    data() {
        return {
            options: {
                title: {
                    text: "ECharts 入门示例",
                },
                tooltip: {},
                xAxis: {
                    data: [
                        "衬衫",
                        "羊毛衫",
                        "雪纺衫",
                        "裤子",
                        "高跟鞋",
                        "袜子",
                    ],
                },
                yAxis: {},
                series: [
                    {
                        name: "销量",
                        type: "bar",
                        data: [5, 20, 36, 10, 10, 20],
                    },
                ],
            },
        }
    }
}
```

#### 3、绘制数据

在 Echarts 身上，提供了一个 `setOption()` 用来绘制数据：

```js
export default {
    mounted() {
        const myChartsNode = document.querySelector(".myCharts");
        // 初始化 Echarts 对象
        const myCharts = echarts.init(myChartsNode);
        myCharts.setOption(this.options)
    }
}
```

注意：当数据发生改变时，需要重新绘制图表。

### Vue 处理跨域

在项目根目录创建一个 Vue 项目的配置文件：`vue.config.js`。在该文件中，可以进行前端跨域的配置。

### 基础配置

```js
module.exports = {
    // 开发服务器
    devServer: {
        // 代理
        proxy: 'http://47.98.128.191:3000'
    }
}
```

以上配置就表示，会将当前项目中所有的请求都转发到 `proxy` 设置的服务器。也就是说，使用以上配置，我们不需要给 axios 配置基础路径。

### 指定请求路径

某些情况下，我们的项目的服务器不止一个，可能就需要一部分请求转到一个 A 服务器，一部分请求转发到 B 服务器。因此，还可以指定请求路径来进行 proxy 代理转发。

```js
module.exports = {
    // 开发服务器
    devServer: {
        // 代理
        proxy: {
            '/api': {
                target: 'http://47.98.128.191:3000',
                changeOrigin: true, // 是否跨域
                pathRewrite: {  // 重写路径
                    '^/api': ''
                }
            },
            '/v1': {
                // .....
            }
        }
    }
}
```

以上配置表示，将所有以 `/api` 开头的请求转发到 `target` 对应的服务器。请求转发到服务器之后，会将 `/api` 重写为空字符串。

##### 路径别名配置

```js
module.exports = {
    // 路径别名配置
    configureWebpack: {
        resolve: {
            alias: {
                '@api': '@/http/api.js',
                "@cpn": "@/components"
            }
        }
    }
}
```

### 响应式原理

### 一、数据劫持

Vue 的底层，会将 data 中的数据劫持下来，对它们进行处理，将 data 对象中的所有数据变为响应式数据。

#### 1、Object.defineProperty() 基本语法

`Object.defineProperty()` 方法可以为对象的属性添加 `get()` 和 `set()` 方法。当使用数据时，就会触发对应的 `get()` 方法，当修改数据时就会触发对应的 `set()` 方法。

例如：

```js
const data = { name: '张三' };
let value = data.name;
Object.defineProperty(data, 'name', {
    get() {
        console.log('name 属性被访问了');
        return value;
    },
    set(newVal) {
        console.log('name 属性被修改成了' + newVal);
        value = newVal;
    }
})
Object.proxy()
```

#### 2、封装函数

```js
function defineReactive(data, key, value = data[key]) {
    Object.defineProperty(data, key, {
        get() {
            console.log(`${key} 属性被访问了`);
            return value;
        },
        set(newVal) {
            console.log(`${key} 属性被修改成了 ${newVal}`);
            value = newVal;
        }
    })
}
```

#### 3、创建 Observer 类

由于我们要批量处理 Vue 实例中 data 对象中所有属性，因此我们还会创建一个 Observer 的类来批量处理所有的属性：

```js
class Observer {
    constructor(data) {
        this.$data = data;
        this.walk();
    }
    walk() {
        const keys = Object.keys(this.$data);
        keys.forEach(key => {
            defineReactive(this.$data, key);
        })
    }
}
```

在 Vue 中调用 Observer 类，并传递 data：

```js
class Vue {
    constructor(option) {
        this.$data = option.data();
        // 处理 data 上数据
        new Observer(this.$data);
    }
}
```

#### 4、处理 Vue 实例的属性

处理 Vue 实例的 `$data` 属性要处理，Vue 实例本身也拥有 data 中的所有数据：

```js
class Vue {
    constructor(option) {
        this.$data = option.data();
        this.proxy();
        // 处理 data 上数据
        new Observer(this.$data);
    }
    // 将 this.$data 对象上所有的属性添加到 this 身上
    proxy() {
        Object.keys(this.$data).forEach(key => {
            defineReactive(this, key, this.$data[key]);
        })
    }
}
```

#### 二、发布订阅模式（收集依赖）

##### 1、Dep

data 中的每一条数据都有一个 Dep。

##### 2、Watcher

每一条数据，只要在一个节点中使用了，就有一个对应的 Watcher 负责收集该数据与该节点之间的关系。

## 小程序

### 1、注册开发者账号

在《微信公共平台》注册一个开发者账号。

### 2、微信开发者工具

在《微信开放文档》的工具中，找到开发者工具的下载地址，下载稳定版。

### 3、创建小程序项目

在创建项目时，AppID 填写自己账号的 AppID（在微信公共平台中查看）。后端服务选择“不使用云服务”。

### 全局配置

全局配置，即作用于整个小程序的配置：

#### 1、pages

配置小程序页面路径：

```js
{
    "pages": [
        "pages/home/home",
        "pages/mine/mine"
    ]
}
```

#### 2、窗口配置

```js
{
    "window": {
        "navigationBarBackgroundColor": "#646dc7",
        "navigationBarTitleText": "蜗牛商城",
        "navigationBarTextStyle": "white"
    }
}
```

#### 3、tabBar 配置

```
{    "tabBar": {    }}
```

#### 页面配置

页面配置，是只作用于当前页面的配置。

例如设置某一个页面的顶部导航栏：

```js
{
    "navigationBarBackgroundColor": "#646dc7",
    "navigationBarTitleText": "蜗牛商城",
    "navigationBarTextStyle": "white"
}
```

小程序中提供了一套自己的 `.wxml` 和 `.wxss` 来编写小程序的静态页面。

### 1、WXML

其中 `.wxml` 是页面结构，等同于我们以前学习的 HTML，但是小程序中提供了一套自己的标签，称之为“组件”：

![image-20210926145852160](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210926145852.png)

#### 常用组件

- `view`：视图容器，等同于 HTML 中的 `div`；
- `text`：文本，小程序中所有的文字内容都需要设置在 `text` 中；
- `image`：图片，等同于 HTML 中的 `img`；
- `navigator`：链接，等同于 HTML 中的 `a`；
- …

#### 滑块容器

小程序中还提供了 `swiper` 和 `swiper-item` 两个组件，搭配使用可以实现一个基本的轮播图：

```js
<view class="swiper-container">
    <swiper autoplay circular interval="3000" duration="1000">
        <swiper-item>
            <image class="swiper-image" src="/static/images/banner1.png"></image>
        </swiper-item>
        <swiper-item>
            <image class="swiper-image" src="/static/images/banner2.png"></image>
        </swiper-item>
        <swiper-item>
            <image class="swiper-image" src="/static/images/banner3.png"></image>
        </swiper-item>
    </swiper>
</view>
```

### 2、WXSS

`.wxss` 是小程序中用来设置页面样式的文件。用于和 CSS 一致。

但是需要注意，由于小程序开发要考虑不同大小的手机屏幕，所有长度单位使用的是 `rpx`。小程序中 `750rpx` 是全屏宽度。

例如我们给上面的轮播图添加一些样式：

```js
.swiper-container {
    padding: 20rpx;
}
.swiper-container > swiper {
    height: 300rpx;
}
.swiper-image {
    width: 100%;
    height: 100%;
    border-radius: 10rpx;
}
```

### 发送网络请求

```js
Page({
    onLoad: function (options) {
        wx.request({
            url: 'https://api-hmugo-web.itheima.net/api/public/v1/home/swiperdata',
            method: 'GET',
            success(res) {
                console.log(res)
            }
        })
    },
})
```

### 服务器域名校验

#### 设置不校验域名

在小程序开发者工具中按照下图配置，可以不校验服务器域名：

![image-20210926153143981](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210926153144.png)

#### 配置合法域名

登录小程序管理后台，在“开发管理”中找到“开发设置”，然后找到下图位置，开始配置域名：

![image-20210926152243179](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210926152243.png)

将服务器的域名配置进去，保存并提交：

![image-20210926153355739](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210926153355.png)

配置完成后重启一下小程序开发者工具。

### 数据渲染

### 1、设置初始数据

每一个页面 的 `.js` 文件中，都有一个 data 属性，用来设置当前页面的初始数据：

```js
Page({
    /**
     * 页面的初始数据
     */
    data: {
        swiperData: []
    }
}
```

### 2、修改 data 数据

小程序中修改 data 中的数据，必须通过 `this.setData()` 来进行修改：

```js
Page({
    data: {
        swiperData: []
    },
    onLoad: function (options) {
        wx.request({
            // ....
            success: (res) => {
                // 修改 data
                this.setData({
                    swiperData: res.data.message
                });
            }
        })
    },
}
```

### 3、访问 data

在 JS 文件中，如果要访问 data，需要通过 `this.data.属性名` 进行访问：

```js
Page({
    data: {
        swiperData: []
    },
    onLoad: function (options) {
        wx.request({
            // ....
            success: (res) => {
                this.setData({
                    swiperData: res.data.message
                });
                // 访问 data
                console.log(this.data.swiperData);
            }
        })
    },
}
```

### 4、数据渲染

#### 数据绑定

小程序中的数据绑定分为两种情况：

- 数据渲染为普通文本
- 数据渲染为组件属性

##### 数据渲染为普通文本

```
<text>{{ msg }}</text>
```

##### 数据渲染为组件属性

```
<image src="{{item.image_src}}"></image>
```

#### 列表渲染

小程序中提供了 `wx:for` 来实现列表渲染：

```js
<swiper>
    <swiper-item wx:for="{{swiperData}}"></swiper-item>
</swiper>
```

其中，swiperData 是数组名。

默认数组的当前项的下标变量名默认为 `index`，数组当前项的变量名默认为 `item`。

```js
<swiper>
    <swiper-item wx:for="{{swiperData}}">
        <image src="{{item.image_src}}"></image>
    </swiper-item>
</swiper>
```

##### wx:key

小程序中列表渲染的元素也需要设置唯一的 key 值。需要注意的是：

- wx:key 的值不需要 `{{}}`；
- wx:key 的值可以直接设置属性名，不需要 `item.` 进行设置。

```js
<swiper>
    <swiper-item wx:for="{{swiperData}}" wx:key="goods_id">
        <image src="{{item.image_src}}"></image>
    </swiper-item>
</swiper>
```

#### 条件渲染

```js
<view wx:if="{{length > 5}}"> 1 </view>
<view wx:elif="{{length > 2}}"> 2 </view>
<view wx:else> 3 </view>
```

#### block

等同于 Vue 中的 template，是一个虚拟的不存在的标签。

### 事件分类

小程序中的事件分为两个大类：

- 冒泡事件：当一个子组件上的事件被触发后，该事件会向父节点传递。
- 非冒泡事件：当一个子组件上的事件被触发后，该事件不会向父节点传递。

WXML的冒泡事件列表：

| 类型        | 触发条件                                                     | 最低版本                                                     |
| :---------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| touchstart  | 手指触摸动作开始                                             |                                                              |
| touchmove   | 手指触摸后移动                                               |                                                              |
| touchcancel | 手指触摸动作被打断，如来电提醒，弹窗                         |                                                              |
| touchend    | 手指触摸动作结束                                             |                                                              |
| tap         | 手指触摸后马上离开                                           |                                                              |
| longpress   | 手指触摸后，超过350ms再离开，如果指定了事件回调函数并触发了这个事件，tap事件将不被触发 | [1.5.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

其中，tap 事件就等同于 PC 端的 click 事件。

### 绑定事件

小程序中绑定事件的方式有两种：

- `bind`：不会阻止事件冒泡
- `catch`：会阻止事件冒泡

```
<button bindtap="sayHello">按钮</button>
```

其中，sayHello 是事件方法名。

### 事件传参

小程序中如果要进行事件传参，有两种方式：

- H5 的自定义属性
- mark

#### H5 的自定义属性

将需要传递的参数通过 `data-属性名` 设置成组件的自定义属性，例如：

```
<view bindtap="changeCategory" data-id="{{item.cat_id}}"></view>
```

在事件方法中通过 evnet 对象来接收参数：

```js
Page({
    changeCategory(event) {
        console.log(event.currentTarget.dataset.id)
    }
})
```

#### mark

将需要传递的参数通过 `mark:属性名` 设置在组件身上：

```js
<view bindtap="changeCategory" mark:id="{{item.cat_id}}"></view>
```

在事件方法中通过 evnet 对象来接收参数：

```js
Page({
    changeCategory(event) {
        console.log(event.mark.id)
    }
})
```

### 自定义组件

### 创建组件

首先在项目根目录找到 `components` 目录（没有就自己创建），在该目录中新建一个组件文件夹，例如：`floorItem`。然后，在组件文件夹中右键选择【新建 Component】，输入与文件夹同名的组件名，完成组件的创建。

![image-20210927121240271](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210927121240.png)

每一个组件也是由 `.wxml`、`.wxss`、`.js`、`.json` 四个同名文件组成。

### 引入组件

页面或自定义组件中想要使用其他自定义组件，需要先在 `.json` 文件中配置组件名称和路径：

```js
{
    "usingComponents": {
        "floorItem": "/components/floorItem/floorItem"
    }
}
```

引入完成后，就可以在 `.wxml` 文件中使用组件了：

```
<floorItem></floorItem>
```

### 组件传值

小程序的组件传值和 Vue 类似，都是通过自定义属性进行传递：

```
<floorItem item="{{item}}"></floorItem>
```

组件中通过 `properties` 属性接收外部传递的数据：

```js
Component({
    properties: {
        item: Object
    }
})
```

组件接收到数据后，就可以直接通过属性名使用数据了。

```
<image src="{{item.image_src}}"></image>
```

### 生命周期

小程序中的生命周期分为四个大类：

- 页面的生命周期
- 组件的生命周期
- 小程序的生命周期
- 组件所在页面的生命周期

#### 页面的生命周期

| 生命周期函数 | 参数    | 描述                     |
| :----------- | :------ | :----------------------- |
| onLoad       | options | 在页面加载时执行         |
| onReady      | 无      | 在页面初次渲染完成时执行 |
| onShow       | 无      | 在页面显示时执行         |
| onHide       | 无      | 在页面隐藏时执行         |
| onUnload     | 无      | 在页面卸载时执行         |

```
Page({    onLoad: function(options) {        // ...    }})
```

#### 组件的生命周期

| 生命周期函数 | 描述                           |
| :----------- | :----------------------------- |
| created      | 在组件创建完成时执行           |
| attached     | 当组件进入页面时执行           |
| ready        | 当组件在视图中渲染完成时执行   |
| moved        | 当组件被移动到另一个位置时执行 |
| detached     | 当组件从页面中移除时执行       |

```js
Component({
    // 2.2.3 版本以下
    attached: function() {
        // ...
    },
    // 2.2.3 版本以上
    lifetimes: {
        attached: function() {
            // ...
        }
    }
})
```

#### 小程序的生命周期

小程序的生命周期是在 `app.js` 中定义。

| 生命周期函数 | 描述                                       |
| :----------- | :----------------------------------------- |
| onLaunch     | 在小程序初始化完成时执行（全局只触发一次） |
| onShow       | 在小程序启动、或从后台进入前台时执行       |
| onHide       | 在小程序隐藏、或从前台进入后台时执行       |

```
App({    onLaunch: function() {        // ...    }})
```

#### 组件所在页面的生命周期

| 生命周期函数 | 描述                       |
| :----------- | :------------------------- |
| show         | 组件所在页面显示时执行     |
| hide         | 组件所在页面隐藏时执行     |
| resize       | 组件所在页面尺寸改变时执行 |

```js
Component({
    pageLifetimes: {
        show: function() {
            // ...
        }
    }
})
```

### 页面跳转

#### 一、navigator

微信小程序中提供了一个 `<navigator>` 标签来实现页面跳转，其中 `url` 属性用来设置跳转的页面路径：

```
<navigator url="/pages/list/list">跳转</navigator>
```

#### 二、路由方法

除了直接通过标签跳转外，小程序中还提供了路由方法来实现跳转。

| 方法                | 说明                                                         |
| :------------------ | :----------------------------------------------------------- |
| `wx.navigateTo()`   | 保留当前页面，跳转到应用内的某个页面。但是不能跳到 tabbar 页面。 |
| `wx.switchTab()`    | 跳转到 tabBar 页面，并关闭其他所有非 tabBar 页面             |
| `wx.reLaunch()`     | 关闭所有页面，打开到应用内的某个页面                         |
| `wx.redirectTo()`   | 关闭当前页面，跳转到应用内的某个页面。但是不允许跳转到 tabbar 页面。 |
| `wx.navigateBack()` | 关闭当前页面，返回上一页面或多级页面。                       |

示例代码：

```js
wx.navigateTo({
    url: '/pages/list/list'
})
```

其他更多方法参数说明参考官网：`https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.switchTab.html`。

#### 三、页面传值

微信小程序中，还可以通过页面跳转来实现页面与页面间的传值。

##### 1、路径传值

在跳转路径的末尾用 `?` 分割页面路径与参数。参数的格式为 `参数名=参数值`，多个参数之间用 `&` 符号分割。

**示例代码：**

```js
<navigator url="/pages/home/home?id=1">跳转wx.navigateTo({
      url: '/pages/list/list?id=1&name=woniu'
})
```

##### 2、接收参数

在页面的 `onLoad` 生命周期函数中，可以通过 `options` 形参来接收其他页面传递的数据：

```js
Page({
    onLoad(options) {
        console.log(options);  // { id: 1, name: 'woniu' }
    }
})
```

### 小程序授权登录

### 1、授权获取用户信息

```
Page({    // 获取用户信息    getUserProfile() {        // 弹出一个用户信息的授权窗口        wx.getUserProfile({            desc: '用于展示用户信息', // 必填            success: res => {                console.log(res.userInfo);            },            fail: err => {                console.log('err', err);            }        })    }})
```

#### 前端保存用户信息

如果需要在前端保存用户信息，可以保存在本地存储，也可以保存在 `app.js` 全局变量中。

##### 本地存储

```
wx.setStorage({    key: 'userInfo',    data: res.userInfo})
```

##### 全局变量

```
getApp().globalData.userInfo = res.userInfo;
```

### 2、小程序登录流程

#### 1）获取 code

```js
Page({
    getCode() {
        wx.login({
            success: res => {
                console.log(res.code);
            }
        })
    }
})
```

#### 2）获取 token

```js
Page({
    getToken(code) {
        wx.request({
            url: 'http://47.98.128.191:3001/users/wxLogin',
            method: 'POST',
            data: {
                code, // 必选
                appId: 'wxded7871137340bad',
                appSecret: 'ea4b3f9de9ff080cbe2029d045f20e8c',
                userInfo: getApp().globalData.userInfo
            },
            success: res => {
                console.log(res);
            }
        })
    },
})
```

参数说明：

- code：必选参数，前端发送 code 给后端，后端通过 code 去微信服务器换取用户的 openid；
- appId：练习时的必选参数，实际开发中不需要。开发者的 AppId，获取方式参考下图。
- appSecret：练习时的必选参数，实际开发中不需要。开发者的 AppSecret，获取方式参考下图。
- userInfo：用户信息，以后根据项目需求选择是否传递。

![image-20210928104730135](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210928105731.png)

### 3、渲染用户信息

当获取到后端返回的 token 后，将 token 保存在本地存储中，然后返回上一个页面。例如个人中心，渲染用户信息：

```js
Page({
    getToken(code) {
        wx.request({
            url: 'http://47.98.128.191:3001/users/wxLogin',
            method: 'POST',
            data: {
                code, // 必选
                appId: 'wxded7871137340bad',
                appSecret: 'ea4b3f9de9ff080cbe2029d045f20e8c',
                userInfo: getApp().globalData.userInfo
            },
            success: ({ data }) => {
                if (data.code) {
                    // 保存 token
                    wx.setStorage({
                        key: 'user_token',
                        data: data.token
                    })
                    // 返回上一个页面
                    wx.navigateBack({
                        delta: 1,
                    })
                }
            }
        })
    }
})
```

在个人中心页面，获取全局的用户信息，并进行渲染：

```js
Page({
    data: {
        userInfo: null
    },
    getGlobalUserInfo() {
        // 获取全局的用户信息
        const userInfo = getApp().globalData.userInfo;
        if(userInfo) {
            this.setData({
                userInfo: userInfo
            });
        }
    },
    onShow: function () {
        this.getGlobalUserInfo();
    }
}
```

条件渲染：

```js
<view wx:if="{{userInfo}}" class="userInfo">
    <view class="avatar">
        <image src="{{userInfo.avatarUrl}}"></image>
    </view>
    <text>{{userInfo.nickName}}</text>
</view>
<view wx:else class="userInfo">
    <view class="avatar">
        <image src="/static/images/default.jpg"></image>
    </view>
    <navigator url="/pages/login/login">未登录</navigator>
</view>
```

### 4、判断用户状态

如果用户授权登录过，后续再进入小程序就不需要再登录了。

因此，通常在一进入小程序时，我们就需要对用户的状态进行判断，判断一下用户是否登录过。

在 `app.js` 的 `onLaunch` 函数中，向服务器发起请求，获取用户信息：

```js
App({
    onLaunch() {
        // 判断用户之前是否有授权登录过
        // 发送请求，将 token 发送给后端，来获取用户信息
        this.getUserInfo();
    },
    getUserInfo() {
        const token = wx.getStorageSync('user_token');
        if (token) {
            wx.request({
                url: 'http://47.98.128.191:3001/users/getUserInfo',
                header: {
                    Authorization: token
                },
                success: ({data}) => {
                    if(data.code) {
                        this.globalData.userInfo = data.userInfo;
                    }
                }
            })
        }
    },
    globalData: {
        userInfo: null
    }
})
```

### 云开发

云开发提供的功能包括：

- 云服务器
- 云数据库
- 云存储
- 云函数
- …

### 云数据库

从云开发控制台中可以直接操作云数据库：

![image-20210928160756760](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210928160756.png)

增删改查都可以直接从云开发控制台操作。

#### 数据库权限

为了后续能在小程序中操作数据库，我们需要设置一下集合的权限：

![image-20210928161721027](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210928161721.png)

我们将安全规则自定义为：

```js
{
  "read": true,
  "write": true
}
```

### 小程序操作云数据库

除了可以在云开发控制台中操作数据库外，小程序中也可以通过代码来操作数据库。

#### 1、初始化

```js
// 获取云端数据库对象
const db = wx.cloud.database();
// 获取集合对象
const todos = db.collection('todos');
Page({
})
```

#### 2、获取数据

```js
Page({
    onLoad: function (options) {
        this.getTodos();
    },
    async getTodos() {
        const res = await todos.get();
        console.log(res);
    },
}
```

### 云函数

#### 1、新建云函数

![image-20210928174043487](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210928174043.png)

输入云函数名称，完成创建。

#### 2、修改云函数

云函数的核心文件是 `index.js`：

```js
// 云函数入口文件
const cloud = require('wx-server-sdk')
cloud.init()
// 数据库初始化
const db = cloud.database();
const todos = db.collection('todos');
// 云函数入口函数
exports.main = async (event, context) => {
    return await todos.doc(event._id).update({
        data: {
            done: event.done
        }
    })
}
```

云函数中也可以操作云数据库。

注：云函数发生改变后，需要重新上传部署。

![image-20210928174237020](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210928174237.png)

#### 3、调用云函数

```js
Page({
    async doneChange(event) {
        // 调用云函数
        const res = await wx.cloud.callFunction({
            name: 'doneChange',  // 云函数名称
            data: {   // 传递给云函数的参数
                _id: event.mark.id,
                done: event.detail.value
            }
        });
    }
})
```

### 扩展

#### 设置 switch 样式

```js
/* 设置复选框 未选中的样式 */
switch .wx-checkbox-input {
    border-radius: 50%;
    height: 40rpx;
    width: 40rpx;
}
/* 选中的样式 */
switch .wx-checkbox-input.wx-checkbox-input-checked {
    border: 1px solid red;
}
/* 选中后的勾勾的样式 */
switch .wx-checkbox-input.wx-checkbox-input-checked::before {
    color: red;
}
```

## uni-app

uni-app 是一个使用 Vue.js 开发所有前端应用的框架，开发者编写一套代码，可发布到 iOS、Android、Web（响应式）、以及各种小程序（微信/支付宝/百度/头条/QQ/快手/钉钉/淘宝）、快应用等多个平台。

### 准备工作

#### 安装 HBuilderX

官方推荐的 uni-app 开发者工具。

#### 小程序开发环境配置

如果要使用 uni-app 开发微信小程序，需要在电脑上安装微信开发者工具。

#### 安卓开发环境配置

安卓开发，需要在电脑上安装 JDK，需要有一个安卓手机，没有安卓手机的也可以在电脑上安装安卓模拟器。

##### 安装 JDK

JDK 是 Java 语言的软件开发工具包，主要用于移动设备、嵌入式设备上的 java 应用程序。它包含了 JAVA 的运行环境（ JVM+Java 系统类库）和 JAVA 工具。

说明：建议安装 JDK8 版本。

##### 配置 Java 环境变量

打开电脑中的【高级系统设置】-【高级】-【环境变量】-【系统变量】-【新建】，在弹出的新建窗口中进行如下配置：

![image-20210719104733727](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210719104733.png)

注意：【变量值】配置的是你们自己电脑中 JDK 安装的路径。

继续打开【高级系统设置】-【高级】-【环境变量】-【系统变量】-【path】，在已有的 path 后面新增以下配置：

```
%JAVA_HOME%\bin
```

![image-20210715162303981](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210715162304.png)

##### 检查 JDK 安装配置是否成功

在终端任意路径中输入 `java` 和 `javac`：

![image-20210715162627717](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210715162627.png)

`java` 和 `javac` 都出现类似以上提示，则表示安装配置成功。

说明：若输入 `javac` 提示没有该命令，则说明以上两个环境变量配置有误。

##### 安卓真机连接步骤

- 数据线连接电脑和安卓手机
- 打开手机的【开发者选项】，百度搜索各自手机型号如何找到该配置
- 在【开发者选项】中，选择【允许 USB 调试】
- 后续连接成功后，如果再弹出提示问“是否允许连接、调试”等，都选择允许。

uni-app 中的生命周期函数分为三类：

- 应用的生命周期
- 页面的生命周期
- 组件的生命周期

#### 一、应用生命周期

应用生命周期是指关于当前整个应用程序的生命周期，这一类生命周期函数只能在`App.vue`中实现监听。

`uni-app`支持如下应用生命周期函数：

| 函数名               | 说明                                                         |
| :------------------- | :----------------------------------------------------------- |
| onLaunch             | 当`uni-app`初始化完成时触发（全局只触发一次）                |
| onShow               | 当`uni-app`启动，或从后台进入前台显示                        |
| onHide               | 当`uni-app`从前台进入后台                                    |
| onError              | 当`uni-app`报错时触发                                        |
| onUniNViewMessage    | 对`nvue`页面发送的数据进行监听，可参考 [nvue 向 vue 通讯](https://uniapp.dcloud.io/nvue-api?id=communication) |
| onUnhandledRejection | 对未处理的Promise拒绝事件监听函数（2.8.1+）                  |
| onPageNotFound       | 页面不存在监听函数                                           |
| onThemeChange        | 监听系统主题变化                                             |

示例代码如下：

```
<script>    // 只能在App.vue里监听应用的生命周期    export default {        onLaunch: function() {            console.log('App Launch')        },        onShow: function() {            console.log('App Show')        },        onHide: function() {            console.log('App Hide')        }    }</script>
```

#### 二、页面生命周期

页面生命周期是指关于`pages`目录中页面的生命周期函数。

`uni-app` 支持如下页面生命周期函数：

| 函数名                              | 说明                                                         | 平台差异说明                                                 | 最低版本 |
| :---------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :------- |
| onInit                              | 监听页面初始化，其参数同onLoad参数，为上个页面传递的数据，参数类型为Object（用于页面传参），触发时机早于onLoad | 百度小程序                                                   | 3.1.0+   |
| onLoad                              | 监听页面加载，其参数为上个页面传递的数据，参数类型为Object（用于页面传参），参考[示例](https://uniapp.dcloud.io/api/router?id=navigateto) |                                                              |          |
| onShow                              | 监听页面显示。页面每次出现在屏幕上都触发，包括从下级页面点返回露出当前页面 |                                                              |          |
| onReady                             | 监听页面初次渲染完成。注意如果渲染速度快，会在页面进入动画完成前触发 |                                                              |          |
| onHide                              | 监听页面隐藏                                                 |                                                              |          |
| onUnload                            | 监听页面卸载                                                 |                                                              |          |
| onResize                            | 监听窗口尺寸变化                                             | App、微信小程序                                              |          |
| onPullDownRefresh                   | 监听用户下拉动作，一般用于下拉刷新，参考[示例](https://uniapp.dcloud.io/api/ui/pulldown) |                                                              |          |
| onReachBottom                       | 页面滚动到底部的事件（不是scroll-view滚到底），常用于下拉下一页数据。具体见下方注意事项 |                                                              |          |
| onTabItemTap                        | 点击tab时触发，参数为Object，具体见下方注意事项              | 微信小程序、支付宝小程序、百度小程序、H5、App（自定义组件模式） |          |
| onShareAppMessage                   | 用户点击右上角分享                                           | 微信小程序、百度小程序、字节跳动小程序、支付宝小程序         |          |
| onPageScroll                        | 监听页面滚动，参数为Object                                   | nvue暂不支持                                                 |          |
| onNavigationBarButtonTap            | 监听原生标题栏按钮点击事件，参数为Object                     | App、H5                                                      |          |
| onBackPress                         | 监听页面返回，返回event = {from:backbutton、 navigateBack} ，backbutton表示来源是左上角返回按钮或android返回键；navigateBack表示来源是uni.navigateBack；详细说明及使用：[onBackPress 详解](http://ask.dcloud.net.cn/article/35120)。支付宝小程序只有真机能触发，只能监听非navigateBack引起的返回，不可阻止默认行为。 | app、H5、支付宝小程序                                        |          |
| onNavigationBarSearchInputChanged   | 监听原生标题栏搜索输入框输入内容变化事件                     | App、H5                                                      | 1.6.0    |
| onNavigationBarSearchInputConfirmed | 监听原生标题栏搜索输入框搜索事件，用户点击软键盘上的“搜索”按钮时触发。 | App、H5                                                      | 1.6.0    |
| onNavigationBarSearchInputClicked   | 监听原生标题栏搜索输入框点击事件                             | App、H5                                                      | 1.6.0    |
| onShareTimeline                     | 监听用户点击右上角转发到朋友圈                               | 微信小程序                                                   | 2.8.1+   |
| onAddToFavorites                    | 监听用户点击右上角收藏                                       | 微信小程序                                                   | 2.8.1+   |

#### 三、组件生命周期

`uni-app`组件支持的生命周期，与vue标准组件的生命周期相同。这里没有页面级的onLoad等生命周期：

| 函数名        | 说明                                                         | 平台差异说明 |
| :------------ | :----------------------------------------------------------- | :----------- |
| beforeCreate  | 在实例初始化之后被调用。[详见](https://cn.vuejs.org/v2/api/#beforeCreate) |              |
| created       | 在实例创建完成后被立即调用。[详见](https://cn.vuejs.org/v2/api/#created) |              |
| beforeMount   | 在挂载开始之前被调用。[详见](https://cn.vuejs.org/v2/api/#beforeMount) |              |
| mounted       | 挂载到实例上去之后调用。[详见](https://cn.vuejs.org/v2/api/#mounted) 注意：此处并不能确定子组件被全部挂载，如果需要子组件完全挂载之后在执行操作可以使用`$nextTick`[Vue官方文档](https://cn.vuejs.org/v2/api/#Vue-nextTick) |              |
| beforeUpdate  | 数据更新时调用，发生在虚拟 DOM 打补丁之前。[详见](https://cn.vuejs.org/v2/api/#beforeUpdate) | 仅H5平台支持 |
| updated       | 由于数据更改导致的虚拟 DOM 重新渲染和打补丁，在这之后会调用该钩子。[详见](https://cn.vuejs.org/v2/api/#updated) | 仅H5平台支持 |
| beforeDestroy | 实例销毁之前调用。在这一步，实例仍然完全可用。[详见](https://cn.vuejs.org/v2/api/#beforeDestroy) |              |
| destroyed     | Vue 实例销毁后调用。调用后，Vue 实例指示的所有东西都会解绑定，所有的事件监听器会被移除，所有的子实例也会被销毁。[详见](https://cn.vuejs.org/v2/api/#destroyed) |              |

### 地图功能

#### 一、map 组件

uni-app 中提供了`<map>`地图组件来用于展示地图。

```
<map class="map"></map>
```

uni-app 中`<map>`组件的默认大小是 300*150，可以通过 CSS 来改变其大小，例如：

```
.map {      width: 750rpx;      height: 750rpx;}
```

#### 二、设置地图中心位置

uni-app 中给`<map>`组件提供了`longitude`和`latitude`属性来设置中心点的经纬度坐标：

```js
<template>
    <map class="map" :latitude="latitude" :longitude="longitude"></map>
</template>
<script>
export default {
    data() {
        return {
            latitude: 39.909,
            longitude: 116.39742,
        }
    }
}
</script>
```

#### 三、获取坐标

uni-app 中提供了`uni.getLocation`方法用来获取用户的位置坐标：

```js
export default {
    data() {
        return {
            latitude: 39.909,
            longitude: 116.39742,
        }
    },
    onLoad: function() {
        uni.getLocation({
            type: 'gcj02',
            success: (res) => {
                this.latitude = res.latitude;
                this.longitude = res.longitude;
            }
        });
    },
}
```

但是在小程序中，获取用户位置需要取得用户授权。

**获取微信小程序位置授权**

在 HBuilder 中打开`manifest.json`文件，选择【微信小程序配置】-【位置接口】，其中描述信息会展示在小程序界面，用来提示用户小程序获取地理位置的原因是什么。

![image-20210405185746209](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210405185746.png)

点击【确定】后地图就能定位到用户当前的地理位置。

注意：电脑模拟器定位大部分时候都不准，可以在手机上查看实际定位效果。

#### 四、标记点

`<map>`组件的 markers 属性可以用来绘制地图标记点：

```js
<template>
        <map class="map" :latitude="latitude" :longitude="longitude" :markers="covers"></map>
</template>
<script>
export default {
    data() {
        return {
            latitude: 39.909,
            longitude: 116.39742,
            covers: [{
                latitude: 39.909,
                longitude: 116.39742,
                iconPath: '../../../static/location.png'
            }, {
                latitude: 39.90,
                longitude: 116.39,
                iconPath: '../../../static/location.png'
            }]
        }
    }
}
</script>
```

markers 的属性值是一个数组，包含所有需要标记的点的相关信息。

### 腾讯地图

#### 一、创建密钥

##### 1、登录账号

进入腾讯地图位置服务官网：`https://lbs.qq.com/`，点击官网右上角【登录】，微信扫码登录即可。

##### 2、进入开发文档

参考下图从官网首页进入微信小程序的开发使用文档：

![image-20210405142234500](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210405142258.png)

##### 3、申请密钥

要在应用中使用腾讯地图，首先需要先针对当前应用申请密钥。

![image-20210405142507189](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210405142507.png)

点击【申请密钥】进到“应用管理”界面，选择【+创建应用】，输入项目名称，选择项目类型，例如：

![image-20210405143233656](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210405143233.png)

项目创建成功后，选择【添加key】：

![image-20210405151546706](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210405151546.png)

- key 名称：建议使用“应用名 + 应用场景”命名，例如：【滴滴打车-司机端】；
- 描述：描述将要应用于哪种具体业务场景，例如：路线规划、获取用户位置；
- 授权 APP ID：微信小程序 ID（从微信小程序后台获取）；

#### 二、下载 SDK

回到微信小程序 SDK 的开发文档首页，根据提示下载 JavaScriptSDK v1.2：

![image-20210405152353108](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210405152353.png)

将 SDK 文件解压后，放到项目的 utils 目录中。

#### 三、安全域名设置

要从小程序中调用腾讯地图 API，还需要在小程序的管理后台中将腾讯地图地址的设置为合法域名：

![image-20210405160641702](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210405160641.png)

将腾讯地图的域名 `https://apis.map.qq.com` 添加为 request 合法域名：

![image-20210405160850566](https://woniumd.oss-cn-hangzhou.aliyuncs.com/web/jianglan/20210405160850.png)

#### 四、引入腾讯地图 SDK

在需要使用地图功能的页面中通过以下代码引入腾讯地图 SDK：

```js
import QQMapWX from '@/utils/qqmap-wx-jssdk.min.js';
```

#### 五、实例化 API 核心类

在`onLoad`生命周期函数中调用构造函数`QQMapWX`来实例化 sdk 核心，将前面申请到的 key 添加到`key`属性中：

```js
export default {
    onLoad: function () {
        // 实例化API核心类
        let qqmapsdk = new QQMapWX({
              key: '申请的key'
        });
    },
}
```

#### 六、获取位置描述

腾讯地图中提供了`reverseGeocoder()`方法来获取用户当前地理位置的描述信息：

```js
export default {
    onLoad: function() {
          // 实例化API核心类
        // ...
        qqmapsdk.reverseGeocoder({
            success: (res) => { //成功后的回调
                  console.log(res.result);
            },
            fail: function(error) {
                  console.error(error);
            },
        })
    },
}
```