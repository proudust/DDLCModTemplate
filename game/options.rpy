

# ゲーム名
# _() で囲うことで、翻訳対象になります。
define config.name = "DDLC Mod Template"

# True ならメインメニューにタイトルを表示、False なら非表示
define gui.show_name = True

# Mod のバージョン
define config.version = "1.1.2"

# about スクリーンに表示される文字列
define gui.about = _("")

# 実行ファイル名とディレクトリ名で使用される短い名前
# 英数字のみ、スペース禁止、コロン禁止、セミコロン禁止
define build.name = "DDLCModTemplate"

# 上から順に効果音、BGM、ボイスを使用するなら True
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

# ゲームメニューの BGM
define config.main_menu_music = audio.t1

# ゲームメニューの前後に使用するトランジション
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# ロード時に使用するトランジション
define config.after_load_transition = None

# ゲーム終了時に使用するトランジション
define config.end_game_transition = Dissolve(.5)

# ダイアログの表示タイミングの制御
#   show - 常に表示
#   hide - ダイアログが存在する場合のみ
#   auto - scene ステートメント の前に隠し、ダイアログが表示されるときに表示します
#
# これは"window <type>" ステートメントで変更できます
define config.window = "auto"

# ダイアログの表示に使用するトランジション
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# 文字表示速度の初期値
# 0 なら一瞬
# 0 以上なら 1 秒あたりに表示する文字数
default preferences.text_cps = 50

# オート待ち時間の初期値 (0 ~ 30 の間で設定)
default preferences.afm_time = 15

# ボリュームの初期値
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

# セーブデータの保存ディレクトリ名
# ディレクトリの場所は以下の通り
#   Windows: %AAPDATA%\RenPy\
#   Mac: $HOME/Libary/RenPy/
#   Linux: $HOME/.renpy/
#
# 文字列の定数である必要があります
define config.save_directory = "DDLC_Mod_Template"

# タスクバーやドックに表示されるアイコン
define config.window_icon = "gui/window_icon.png"

# True ならスキップ可能、False なら不可
define config.allow_skipping = True

# True ならオートセーブを有効、False なら無効
define config.has_autosave = False

# True なら終了時にオートセーブ、False ならしない
define config.autosave_on_quit = False

# 使用するオートセーブ数
define config.autosave_slots = 0

# 使用するレイヤーの宣言
# 変更しないように
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

# その他の変更する必要のないもの
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"


init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014')
        s = s.replace(' - ', u'\u2014')
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)



# ビルド設定

init python:

    # ファイルパターン:
    # file patterns are case-insensitive and matched against the path relative to the
    # base directory, with and without a leading /. If multiple patterns match
    # the first is used.
    #
    # /  : ディレクトリの区切り
    # *  : / 以外の任意の文字列
    # ** : / を含む任意の文字列
    #
    # 例
    # *.txt - ルートディレクトリの全ての .txt ファイル
    # game/**.ogg - game ディレクトリとそのサブディレクトリ内の全ての .ogg ファイル
    # **.psd - プロジェクト内の全ての .psd ファイル
    #
    # ビルド結果から除外したいファイルには None を指定します。
    #

    # 配布用
    build.package(build.directory_name + "Mod", 'zip', build.name, description='DDLC Compatible Mod')

    # 新しい rpa ファイルの宣言
    build.archive("scripts", build.name)
    build.archive("mod_assets", build.name)
    build.archive("submods", build.name)

    # rpa ファイルに入れるファイルを宣言
    build.classify("game/mod_assets/**"," mod_assets")
    build.classify("game/submods/**", "submods")
    build.classify('game/**.rpyc', "scripts")
    build.classify('game/advanced_scripts/**', "scripts")
    build.classify('game/original_story_scripts/**', "scripts")

    # 無視するファイル
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa', None)

    # zip に入れるファイル
    build.classify('README.html', build.name)

    # Doki Doki Mod Manager 用のメタデータファイル
    build.classify('ddmm-mod.json', build.name)

    # ドキュメントとしてマーク
    build.documentation('README.html')

    build.include_old_themes = False
