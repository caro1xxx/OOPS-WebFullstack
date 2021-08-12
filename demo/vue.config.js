const webpack = require("webpack")
module.exports = {
	// // 配置插件参数
	configureWebpack: {
		plugins: [
			// 配置 jQuery 插件的参数
			new webpack.ProvidePlugin({
				$: 'jquery',
				jQuery: 'jquery',
				'window.jQuery': 'jquery',
				Popper: ['popper.js', 'default']
			})
		]
	}
}

// module.exports = {
// 	devServer: {
// 	  proxy: 'http://localhost:8002'
// 	//   proxy: 'http://81.68.105.198:8002'
// 	}
//   }

  module.exports = {
	assetsDir: 'static',// 静态资源打包输出目录 (js, css, img, fonts)，相应的url路径也会改变
  };


  module.exports = {
	assetsDir: 'static',// 静态资源打包输出目录 (js, css, img, fonts)，相应的url路径也会改变
  };
  