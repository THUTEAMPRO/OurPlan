## 依赖
	+ Python2


## 安装


	先安装python2，将其配置进环境变量。然后进入工程目录在命令行里执行：

	
	cd manage
	
	pip install .


## 运行
	进入工程目录执行
	python start.py


然后打开用浏览器打开网页 http://127.0.0.1:8080`


## 模块
	每个文件夹里的util.py文件负责该目录下其他py文件的依赖。
	+ ./routes
		这个文件夹用来存放定位到某一html页面的url定位。
		example.py中给出了基本的写法示例
	+ ./api

		这个文件夹用来存放可调用的API。一方面，api可以在内部供python代码直接调用，
		另一方面,在__init__.py中实现了api_impl的decorate，包裹api的实现函数使其可通过url远程调用。
		简单起见，api的实现返回都为dict，远程调用时的url参数以及post的json格式的参数可转化成函数参数。
	+ ./static
		这个文件夹里的是些静态的文件，包括静态的html页面，javascript，css，
		可直接用"/"+文件路径（不带static）的url定位到具体的某个文件
	+ ./templates
		这个文件夹是用来放jinja2渲染的模板的，flask自带jinja2的调用函数render_template
		在/routes/example.py中的example_render的函数可看到其示例用法。
	+ ./server

		__init__.py中的代码会将flask的app按照配置实例化，同时连接数据库。
	+ ./common

		config.py文件中写的是工程配置，
		util.py中实现了一个自动import目录下所有py文件的函数
	+ ./model


		这个文件夹里的代码负责将数据库里的数据对象化。
		目前仅有user.py用来测试flask_login的功能。
	+ ./manage
		这个文件夹用来放一些管理的脚本
	+ ./tests
		用来存放测试代码，还没写。。。

## 