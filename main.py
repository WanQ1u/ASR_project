import logging

logging.basicConfig(
    filename="app.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def read_audio(file_path):
    logging.info("开始读取音频：%s", file_path)

    try:
        f = open(file_path, "rb")
        data = f.read()

        logging.info("音频读取成功，大小：%d bytes", len(data))
        return data

    except FileNotFoundError:
        logging.exception("音频文件不存在")

    except PermissionError:
        logging.exception("没有权限读取音频文件")

    finally:
        if "f" in locals():
            f.close()
            logging.info("音频文件已关闭")

    return None


audio_data = read_audio("audio.wav")

if audio_data is not None:
    print("音频读取成功")
else:
    print("音频读取失败")