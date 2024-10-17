import os,sys,glob
from pikepdf import Pdf

#カレントディレクトリに出力用のディレクトリ作成(ない場合のみ)
dirNm = "/unlockPdf"
if not os.path.exists(os.getcwd() + dirNm):
    os.makedirs(os.getcwd() + dirNm)

#カレントディレクトリ内のPDFファイルを取得してループ
files = glob.glob(os.getcwd() + "\*.pdf")
for file in files:
	pdffile = Pdf.open(file,password="")
	newPdf = Pdf.new()
	newPdf.pages.extend(pdffile.pages)
	saveFileNm = os.getcwd() + dirNm + "/" + os.path.basename(file)
	#出力済みフォルダに同名ファイルがない場合、PDF保護解除ファイルを出力
	if not os.path.exists(saveFileNm):
		newPdf.save(saveFileNm)
		print(saveFileNm + "を出力しました。")
	else:
		print(saveFileNm + "は既に存在します。")

#終了メッセージ出力
input("PDFの保護解除完了")
