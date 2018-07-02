color1では、赤、青、黄の三色を検出して、表示させる。
方法としては、HSVに変換して、色の色相のmaskを作ってそれに伴った色を検出させる。
参考URL:https://www.blog.umentu.work/python3-opencv3で指定した色のみを抽出して表示する【動画/　など
元の画像　youtubeリンク:https://youtu.be/gVgb4XLHWjk
赤だけ取り出す　youtubeリンク:https://youtu.be/bjr461NDhXc
黄色だけ取り出す　youtubeリンク:https://youtu.be/hQ0wD7ZgGus
青だけ取り出す　youtubeリンク:https://youtu.be/-N2uGED_vBw

filterでは、どれくらいの大きさの平均値フィルタを作ったらどうなるのかを変化させながら表示させる。
画像をぼかしたりするときに役に立つ。
参考URL:https://algorithm.joho.info/programming/python/opencv-averaging-filter-py/　など
youtubeリンク:https://youtu.be/p_QEyw3ygOY

gammaでは、ガンマ変換を使って画像の変化の様子を実装した。
ガンマの値を変化させるとそれに伴って画像が明るくなったり、暗くなったりする。
参考URL:https://www.blog.umentu.work/python-opencv3でガンマ変換gamma-conversion-2/　など
youtubeリンク:https://youtu.be/p8tZ1UtKNy0
