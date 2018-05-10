/*
	封装常用方法
		* 要使函数的功能更加强大,需要配合参数和返回值使用
		* 常用封装
			* 随机颜色
			* 随机数字
 */

function randomColor(){
	var r = parseInt(Math.random()*256);
	var g = parseInt(Math.random()*256);
	var b = parseInt(Math.random()*256);

	return 'rgb('+r+','+g+','+b+')'
}

// 先用
// randomColor();//rgb(255,0,0)

/**
 * [获取某一范围内的随机整数]
 * @return {[type]} [description]
 */
function randomNumber(min,max){
	return parseInt(Math.random()*(max-min+1)+min)
}

// randomNumber(10,20);//18