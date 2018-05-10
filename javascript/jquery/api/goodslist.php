<?php
	/*
		后端BE
			* 数据库操作
			* 设计数据库
			* 增删改查
			* 业务逻辑
			* 编写数据接口(前后端分离)
			* 请求类型
				* get
				* post
				* delete
				* put	
		服务器根目录
	 */
	

	// 连接数据库
	// 配置参数
	$servername = 'localhost';
	$username = 'root';
	$password = '';
	$database = 'jiaoxue';

	//连接数据库
	$conn = new mysqli($servername,$username,$password,$database);

	// 设置编码
	$conn->set_charset('utf8');


	// 检测连接
	if($conn->connect_error){
		die('连接失败'.$conn->connect_error);
	}


	// 数据库操作
	$sql = "select * from goods order by price*1 desc";

	// 获取查询结果
	$result = $conn->query($sql);

	//使用查询结果
	//数组
	$row = $result->fetch_all(MYSQLI_ASSOC);

	echo json_encode($row,JSON_UNESCAPED_UNICODE);

?>