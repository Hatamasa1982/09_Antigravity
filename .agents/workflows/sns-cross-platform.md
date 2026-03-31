---
description: 1つのアイディアから5つのSNSへ一気に展開する横展開ワークフロー
---

# 目的
1つの「マスターアイディア」を元に、YouTube、note、メルマガ、X、Instagramの5つのプラットフォーム向けにコンテンツを自動展開し、画像生成と保存までを行うワークフローです。

# 前提条件
このワークフローの実行時は、必ず以下のファイルを参照してビジネスの方向性や各SNSに最適化された書き方を適用してください。

- **ビジネスルール**: 
  - `g:\マイドライブ\09.Antigravity\.agents\rules\mybusiness.md`
- **各SNSスキル**:
  - YouTube台本生成: `g:\マイドライブ\09.Antigravity\.agents\skills\youtube-skill\SKILL.md`
  - note記事生成: `g:\マイドライブ\09.Antigravity\.agents\skills\note-skill\SKILL.md`
  - メルマガ生成: `g:\マイドライブ\09.Antigravity\.agents\skills\newsletter-skill\SKILL.md`
  - X投稿生成: `g:\マイドライブ\09.Antigravity\.agents\skills\x-skill\SKILL.md`
  - Instagram生成: `g:\マイドライブ\09.Antigravity\.agents\skills\instagram-skill\SKILL.md`

---

## ステップ1: マスターアイディアの入力
- ユーザーに対して、今回の発信の軸となる「マスターアイディア（テーマ、伝えたいメッセージ、または元となる文章）」の入力を促してください。
- ユーザーから回答があるまで待機します。

## ステップ2: ルールとスキルの参照
- ユーザーからマスターアイディアが入力されたら、前提条件に記載されている`mybusiness.md`と、5つの各SNSの`SKILL.md`ファイルを読み込み、内容を把握してください。

## ステップ3: コンテンツと画像の作成
対象となる5つのSNSそれぞれのコンテンツを作成し、画像も生成します。

1. **テキストコンテンツの作成**
   - 上記のスキルとルールに基づき、以下の5つのテキストを生成してください。
     - YouTubeの台本
     - noteの記事
     - メルマガの本文
     - Xの投稿文
     - Instagramのフィード用テキスト

2. **図解画像の作成 (NanoBananaProを使用)**
   - 画像生成機能（NanoBananaPro）を使用して、Instagramのフィードに最適な図解画像を作成してください。
   - **画像サイズ**: アスペクト比 4:5
   - **構成（合計5枚）**:
     - 表紙 × 1枚
     - 内容（図解や解説） × 3枚
     - CTA（Call To Action：行動喚起） × 1枚

## ステップ4: フォルダ作成と保存
- 今日の日付を含む新しいフォルダ（例: `YYYYMMDD_アイディア名`）を作成してください。
- ステップ3で作成した各SNSのテキストコンテンツ（Markdown形式等）と、生成した5枚の画像データを、作成したフォルダ内に保存してください。
- 保存が完了したら、保存先フォルダのパスをユーザーに報告して終了します。
