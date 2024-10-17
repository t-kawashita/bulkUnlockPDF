
---
title: [【Qiita】pythonで複数のPDFファイルを一括で保護解除](https://qiita.com/t-kawashita/items/bec9dfff34080c80099d)
---
複数のPDFファイルの保護を一括で解除するツールを作成したので、ソース公開します。
(python初心者がとりあえず動くもの作っただけなので綺麗なソースではありませんが…)

## 1.ツール作成を思い立った背景
* 公式HPからダウンロードできる国家試験の過去問PDFは大抵の場合が保護付き。
* 学習過程でマーカーを付けたり、ファイル結合や編集を行いたい場面が多々あり、保護が邪魔。

## 2.ツールの目的
* 開催回、科目、問題/解答毎に別ファイルになっているPDFの保護解除を一括で行う
* 1ファイルずつ手作業で保護解除はしたくない。

# 3.ツールの仕様
* 実行ツールと同じディレクトリ内のPFDファイルを全て保護解除して保存する
* 動作環境はWindows10
* pythonで作成

## 3.1 ツール実行
1. ツール(exeファイル)を保護解除したいPDFファイルと同一ディレクトリに格納
![before_bulkUnlockPDF.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2388674/74489afd-0ee9-1344-0ee0-3b972562cab4.png)

2. 実行中の様子
![r_ulkUnlockPDF.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2388674/0a54dc2d-877b-109c-4108-aca5b1978426.png)"～完了"の文字が出たら[X]ボタンで閉じる

3. フォルダ「unlockPdf」が作成され、配下に保護解除済みPDFが出力された
![after_bulkUnlockPDF.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2388674/bf41cef5-cae3-bd7e-10fc-eebe94c9c07d.png)
全ファイルが保護解除済み、これでPDFが編集できます:laughing:
