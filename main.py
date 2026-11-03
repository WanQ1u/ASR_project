import logging

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# 配置日志
logging.basicConfig(
    filename="app.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def read_audio(file_path):
    logging.info("开始读取音频：%s", file_path)

    try:
        # 以二进制模式打开音频文件
        with open(file_path, "rb") as f:
            data = f.read()

        logging.info("音频读取成功，大小：%d bytes", len(data))
        return data

    except FileNotFoundError:
        logging.exception("音频文件不存在")
        return None

    except PermissionError:
        logging.exception("没有权限读取音频文件")
        return None

    finally:
        logging.info("音频读取操作结束")


# 调用函数
audio_path = BASE_DIR / "audio.wav"
audio_data = read_audio(audio_path)

if audio_data is not None:
    print("音频读取成功")
else:
    print("音频读取失败")