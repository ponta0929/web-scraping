実行環境
＊Proxy
	現状考慮してないのでProxy設定等は行っていません

＊Python実行環境
	Python : 3.6.3
	Anaconda : 3.5.0.1
	
	インストールモジュール
		下記モジュールを使っています
		モジュールがインストールされていない場合、
		pip installにより下記モジュールをインストールしてください
			logging
			datetime
			time
			webdriver
			json
			
＊ブラウザ環境
	Chromeのヘッドレスモードで起動するため、下記をインストールしてください
	・Chrome
		ヘッドレスモードが使用可能なバージョンをインストールしてください

	・Selenium WebDriverのChrome用ドライバ
		下記からダウンロードします
		http://chromedriver.storage.googleapis.com/index.html?path=2.40/
		Zipファイルを展開後、展開したフォルダのchromedriverまでの絶対パスを
		本モジュールの
			conf/setting.json > "chrome_driver_path"
			に設定してください

機能
＊指定したパス以下のコンテンツを取得する機能（実装途中）
	conf/setting.jsonの"TARGET"項目以下に設定されたDOMに対してデータを取得します。
	指定はXPATHにて指定してください
	
＊ログ出力機能
	log以下のファイルにその日のログを出力します

＊DBへのコンテンツの登録機能（未実装）
	distフォルダにJSONデータを出力して代用中

＊自動実行機能（未実装）