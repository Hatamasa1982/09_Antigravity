# 【実践】Antigravityと作る！GAS×Gemini APIで完全自動の名刺管理アプリを開発してみた

## こんな方には役立つ記事です
* GAS（Google Apps Script）に触れたことがある方
* Gemini API に触れたことがある方
* AppSheetに触れたことがある方

※ GAS、AppSheet、Google AI Studioについて、ほとんど知識がない方には少し難しい内容かもしれません。ですが、記事の後半に「コピペで動くコード」も公開しています！

---

## はじめに
みなさん、こんにちは。
日々の業務で増え続ける「名刺」の管理、どうしていますか？

私自身、これまでの名刺の管理方法はいくつか変遷してきました。
昔は **Evernote** を使用し、その次は **OneNote** へ移行。昨年、Google Workspace（GWS）を契約したタイミングで「新しく何か作ろう！」と思い立つも、結局ほったらかしに……。

そんな状態から脱却すべく、過去に少しだけ触ったことのあるノーコードツール「AppSheet」を使って、名刺管理アプリを作りたいと一念発起しました。自分が「使いこなせている」ツールではないため、今回はAIアシスタントの「**Antigravity**」に相談しながら、二人三脚で開発してみました。

## なぜ「AppSheet」を選んだのか？
世の中には便利な名刺管理のSaaSがたくさんあります。しかし、「特定のアプリだと、いつかサービス終了などで使わなくなった時が不安だ」「不要な機能のない自社専用のシンプルなものが欲しい」という思いがありました。

その点、AppSheetであれば、データ自体は**Googleスプレッドシート**と**Googleドライブ**に直接保存されます。これなら、もし将来アプリ自体を使わなくなってもデータは確実に手元に残るため、今後さまざまな形に応用が利きます。「Googleアカウントを今後使わなくなることは多分ないだろう」というのが最大の決め手でした。

## アプリの大まかな仕様と「標準機能」を使わなかった理由
今回作成した仕組みは、非常にシンプルです。

1. **スキャンして保存**: 名刺画像をスキャンし、Googleドライブのフォルダに保存。
2. **スプシでデータ抽出**: スプレッドシートを開き、上部に追加した専用メニューから「読み込みボタン」を押すだけで、画像から必要事項を抽出。
3. **AppSheetで確認**: スマホのAppSheetアプリからきれいな画面で確認。
4. 
5. 実は最初、AppSheetの機能だけで完結させようとしましたが、以下の理由でやめました。

* **なぜカメラ機能を使わないのか？**
  AppSheetのカメラで写真を撮ることはできても、スキャンアプリのように「名刺のサイズに合わせてきれいに自動で切り取る（クロップする）」機能がありませんでした。一方で、Googleドライブアプリの標準スキャン機能はとても優秀です。そのまま目的のフォルダに保存できるため、撮影にはGoogleドライブを使うことにしました。

* **なぜAppSheetのOCR（文字認識）を使わないのか？**
  AppSheetには、画像を読み取る「OCR」機能もありますが、試してみると日本の名刺のようにレイアウトがバラバラな画像から要素を正確に抽出し、分類するには、現状まだ期待には程遠い精度でした。

結果として、AppSheetはあくまで「見やすくするための閲覧用ビューワー」と割り切り、データ抽出の肝となる部分は **「GAS」** と **「Gemini API」** を使うことで圧倒的な精度を実現したのです。

---

## 実録！AIとのペアプロ開発体験記

ここからは、実際にAIエージェント「Antigravity」とどのようにアプリを作っていったかの体験記をお届けします。

### 第1章：AIとの相談で一気にベースを作る
アプリのデータベースとなるスプレッドシートを用意する際、AIが大活躍してくれました。
**「名刺管理アプリを作りたいんだけど、会社名や氏名などが入ったCSVのベースを作ってくれない？」** と相談しただけで、管理項目を備えたCSVファイルを一瞬で生成してくれました。

私はそのCSVをダウンロードして、Googleスプレッドシートとして保存するだけ。これをAppSheetに読み込ませるだけで大枠ができあがり、面倒な初期設定が劇的に楽になりました。

### 第2章：最強の提案「GAS × Gemini API」
AppSheetの標準OCRで挫折しそうになっていた私に、AIから画期的な提案がありました。
**「AppSheetのOCR機能はオフにして、裏側のGASで最新のAI『Gemini』に画像を読ませる専用メニューを作りませんか？圧倒的な知能でデータを完璧に抽出し、ファイル名も一目でわかるように自動でリネームできます！」**

### 第3章：いざ実装！…そしてエラーとの格闘
この強力なプランに惹かれ、いざ実装へ。Google AI StudioでGemini APIキーを取得し、AIが書いてくれたGASコードを貼り付けて実行しました。
しかし、ここで真っ赤なエラーが連発します。「404 Not Found」や「1日の無料枠の上限に達しました（Resource Exhausted）」などなど……。

実は、AIが「常に最新モデルを使う」という設定にしてくれていたため、制限の厳しい出たばかりの最新AI（Gemini 3 Flashなど）に繋がってしまい、すぐに無料枠の制限がかかっていたのです（笑）。
しかし、この時も **「このエラーが出たよ」と画面をそのまま渡すだけで、「これが原因ですね、大量の無料枠がある超高速・軽量最新モデル（Gemini Flash Lite）に変更しましょう！」と一緒に原因究明とコードのブラッシュアップをしてくれました。**

### 第4章：魔法の瞬間（実りある結果）
エラーを乗り越え、ついにテスト実行の時。
スマホのGoogleドライブから名刺をスキャンして保存し、スプレッドシートの上部に追加された「🌟名刺管理 ＞ 📥 新着スキャン画像の読み込み」メニューをクリックして作動させます。

すると数秒後……。
**会社名、氏名、部署、電話番号、住所といったすべての項目に、寸分の狂いもなく完璧なデータが自動入力されました！**

さらに、Googleドライブの画像フォルダを覗くと、適当な英数字だったファイル名たちが **`株式会社〇〇_山田太郎_表.jpg`** という、誰が見ても分かるファイル名にきれいに自動リネームされていました。感動の瞬間です！

---

## 実践チュートリアル：コピペで作れる魔法のコード

私と同じように「AppSheetのOCR精度に不満がある」「画像ファイル名を綺麗に管理したい」という方に向けて、完成した構成とコードを公開します。

### 事前準備
1. スプレッドシート名：「名刺データ」（1行目に「名刺（表面）」「会社名」「氏名」「部署・役職」「代表電話」「携帯電話」「ファックス」「メールアドレス1」「メールアドレス2」「郵便番号」「住所」の列を用意）
2. Googleドライブに名刺画像を保存するための専用フォルダ（例：`名刺データ_Images`）を作成し、その「フォルダID」（URLの最後の文字列）を控えておく。※AppSheet上でこのフォルダの画像を読み込めるようにしておく。
3. AppSheet標準のOCR（Intelligence機能）はオンにしていると競合するため、消しておくこと。
4. Google AI Studioから「Gemini APIキー」を取得しておく。
5. スプレッドシートの「拡張機能」 ＞ 「Apps Script」を開き、デフォルトのコードを全て消す。

### GASのコード

白紙の画面に以下のコードをすべてコピペします。
**※セキュリティのためにスクリプトプロパティや別ファイル（`000_global.gs`など）でAPIキーを管理している場合は、11行目・12行目を適宜書き換えてください。初心者のため、ここでは直接コード内に貼り付ける形で説明しています。**

```javascript
// 1. スプレッドシートを開いたときに上部に専用メニューを追加する
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🌟名刺管理')
    .addItem('📥 新着スキャン画像の読み込み', 'processFolderScansLite')
    .addToUi();
}

function processFolderScansLite() {
  const ui = SpreadsheetApp.getUi();
  
  // ★ APIキーとターゲットフォルダのIDをここに設定します ★
  const apiKey = "YOUR_API_KEY_HERE"; 
  const targetFolderId = "YOUR_TARGET_FOLDER_ID_HERE";
  // ★ =============================================== ★
  
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("名刺データ");
  if (!sheet) {
    ui.alert("エラー", "「名刺データ」という名前のシートが見つかりません。", ui.ButtonSet.OK);
    return;
  }
  
  // 指定のフォルダを取得
  let folder;
  try {
    folder = DriveApp.getFolderById(targetFolderId);
  } catch(e) {
    ui.alert("エラー", "フォルダIDが正しくありません。\n設定を確認してください。", ui.ButtonSet.OK);
    return;
  }
  
  const files = folder.getFiles();
  let processedCount = 0;
  
  // 見出し行のデータ（列のインデックス）を取得
  const headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
  
  // ここからフォルダ内の全画像を1つずつチェック
  while (files.hasNext()) {
    const file = files.next();
    const fileName = file.getName();
    
    // 画像の名前の最後に「_表.jpg」や「_表.jpeg」などが付いている場合は「処理済」とみなして無視する
    if (fileName.match(/_表\.[a-zA-Z]+$/)) {
      continue;
    }
    
    // 画像ファイル以外（PDFなど）は無視する
    const mimeType = file.getMimeType();
    if (!mimeType.startsWith('image/')) {
      continue;
    }

    try {
      // 1. 画像データをBase64に変換
      const base64Data = Utilities.base64Encode(file.getBlob().getBytes());
      
      // 2. Gemini APIの呼び出し（大容量無料枠の gemini-flash-lite-latest を使用）
      const url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent?key=" + apiKey.trim();
      const payload = {
        "contents": [{
          "parts": [
            {
              "text": "以下の日本の名刺画像から情報を抽出してJSON形式で出力してください。見つからない場合は空文字にしてください。キーは必ず以下を使用すること: company, department, name, phone, mobile, fax, email1, email2, zip, address。余計な説明や```jsonなどの表記は絶対に入れず、JSONの中身だけを返してください。"
            },
            {
              "inlineData": { 
                "mimeType": mimeType,
                "data": base64Data
              }
            }
          ]
        }]
      };
      
      const options = {
         "method": "post",
         "contentType": "application/json",
         "payload": JSON.stringify(payload),
         "muteHttpExceptions": true 
      };
      
      const response = UrlFetchApp.fetch(url, options);
      if(response.getResponseCode() !== 200) {
         console.error("Gemini APIエラー (" + fileName + "): " + response.getContentText());
         continue; 
      }
      
      const result = JSON.parse(response.getContentText());
      const jsonText = result.candidates[0].content.parts[0].text.trim().replace(/^```(?:json)?|```$/g, "").trim();
      const ocrData = JSON.parse(jsonText);
      
      // 3. ファイル名の変更（リネーム）
      const cleanCompany = (ocrData.company || '会社不明').replace(/[/\\?%*:|"<>]/g, '-');
      const cleanName = (ocrData.name || '氏名不明').replace(/[/\\?%*:|"<>]/g, '-');
      // 元の拡張子を保持する
      const extension = fileName.split('.').pop();
      const newFileName = `${cleanCompany}_${cleanName}_表.${extension}`;
      file.setName(newFileName);
      
      // 4. 新しい行としてスプレッドシートに追加するデータの準備
      const newRowData = new Array(headers.length).fill("");
      
      // ▼ ここがAppSheetで画像を表示させるための「相対パス」の魔法です！ ▼
      const fieldMapping = {
        "名刺（表面）": "名刺データ_Images/" + newFileName,
        "会社名": ocrData.company || "",
        "氏名": ocrData.name || "",
        "部署・役職": ocrData.department || "",
        "代表電話": ocrData.phone || "",
        "携帯電話": ocrData.mobile || "",
        "ファックス": ocrData.fax || "",
        "メールアドレス1": ocrData.email1 || "",
        "メールアドレス2": ocrData.email2 || "",
        "郵便番号": ocrData.zip || "",
        "住所": ocrData.address || ""
      };
      
      if (headers.indexOf("ID") >= 0) {
        fieldMapping["ID"] = Utilities.getUuid();
      }
      
      for (const [headerName, value] of Object.entries(fieldMapping)) {
        const idx = headers.indexOf(headerName);
        if (idx !== -1) {
          newRowData[idx] = value;
        }
      }
      
      // スプレッドシートの一番下に行ごと追加
      sheet.appendRow(newRowData);
      processedCount++;
      
      // 連続でAPIを叩きすぎないように、1回ごとに3秒（3000ミリ秒）のお休みを入れる
      Utilities.sleep(3000);
      
    } catch(e) {
      console.error("エラー (" + fileName + "): " + e.toString());
    }
  }
  
  if (processedCount > 0) {
    ui.alert("処理完了", `${processedCount} 件の名刺画像を読み込みました！`, ui.ButtonSet.OK);
  } else {
    ui.alert("お知らせ", "新しく読み込む画像は見つかりませんでした。\n（名前が「_表」で終わっていない画像が対象です）", ui.ButtonSet.OK);
  }
}
```

### 最終セットアップと実行
1. スクリプトの保存が終わったら、一度スプレッドシートの画面を再読み込み（リロード）してください。
2. スプレッドシートの上部に **「🌟名刺管理」** という専用メニューが出現します。
3. その中の「📥 新着スキャン画像の読み込み」をクリックします。
4. 初回のみ「承認が必要です」という警告が出るので、ご自身のアカウントを選択し「詳細 → 安全ではないページへ移動 → 許可」の順に進めて権限を許可します（これが出たら、もう一度メニューから実行し直してください）。

これで設定は完了です。名刺をスキャンしてフォルダに保存したあと、このメニューからボタンをポチッと押すだけで、AppSheetと連動する完璧な名刺データが自動生成されます！

## まとめ：AIエージェントのいる開発の楽しさ
ブランクのある状態の私でも、AIと「ここはどう設定する？」と壁打ちしながら進めることで、全く迷うことなく開発ができました。

さらに、プログラミング（GAS）と生成AI（Gemini API）の連携で困ったときも、「このエラーが出たよ」と出力画面を渡すだけで「これが原因だね、こう直そう！」と一緒になって原因を究明できたことは、まるで優秀なエンジニアと仕事をしているような新鮮で感動的な体験でした。

市販の有料名刺アプリに負けない**自社専用・自分専用の強力なツール**を作りたい方は、ぜひこのノウハウを活用して、名刺管理の煩わしさから解放されてみてください！
