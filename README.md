# MOD部へようこそ！

DDLC Mod テンプレートを使用すると、Doki Doki Literature Club 用 MOD の作成を簡単に始めることができます。  
作成の際は [Team Salvato's IP Guidelines](http://teamsalvato.com/ip-guidelines/) を遵守するようにしてください。  

### 使い方
以下の手順に従って、テンプレートを使用する準備をしてください。

1. [Ren'Py SDK version 6.99.12](https://www.renpy.org/release/6.99.12)をダウンロードします。
   *(注: DDLC は他のバージョンの Ren'Py SDK で生成された .rpyc ファイルと互換性はありません。)*
2. [releases](https://github.com/proudust/DDLCModTemplate/releases) から最新の安定版、または [Use this template](https://github.com/proudust/DDLCModTemplate/generate) から新しいリポジトリを作成してください。
3. ファイルを Ren'Py のプロジェクトディレクトリに置きます。 (インストール時に選択します)
4. DDLC 本体を[ダウンロード](http://ddlc.moe)し、中の`audio.rpa`・`images.rpa`・`fonts.rpa` をテンプレートの game フォルダに移動します。(`scripts.rpa` は移動しないでください。)
5. Ren'Py でプロジェクトをコンパイルし、起動します。
6. Ren'Py メニューに移動して、"配布物のビルド" を選択します。 "DDLC Compatible Mod" にチェックを入れてビルドしてください。この操作で、配布用の zip ファイルを生成できます。

### テンプレートの機能
1. DDLC 本編のセーブデータをインポートします。これは元のゲームには影響*しません*。
2. MOD 用のビルド設定があらかじめ用意されています。Ren'Py のおかげで Windows・Mac・Linux 共用の MOD を簡単に配布できます。
3. Mod のインストール手順とガイド。ゲームを実行することで、モニカによる簡単な説明を受けることができます。
4. 初回ロード時の警告文。ガイドラインにより実装が義務付けられています。
5. カスタマイズ可能！あなたの作成したいアイデアの出発点として使用してください。

## DDLC-Toolkit

私たちは [DDLC-Toolkit](https://github.com/GarnetSunset/DDLC-Toolkit) のサブモジュールであることを誇りに思います。
