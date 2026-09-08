import yt_dlp as ydl
def main():
    with ydl.YoutubeDL({"outtmpl": f"100293.%(ext)s"}) as dlr:
        dlr.download("https://cdn4.telesco.pe/file/63b616f86c.mp4?token=nBRk9CxaD3ghGy8eEhlM2TpjUTUry_V3wk2lg38JW--GB9DlCy5n-_xqLmvm6B2AyRYBrqZWlcbKkD9AucRd0pQOM5HaZ5ykK29eWn8Td5Vr1_6cruqRvaKBLkaAiXwZi4KrCZ_Zjg8VOV8NrEZj-Mwqi-rGZPBahrYDFR2-FZ3X_IaPWzgkveqBKfnv5jevlWew_XPwd6lZIDhnnYy_LCILyBjirql-U5d8Pik1gLX_3sJ7ckdfejShS_EQHj3EyybotSqjZT-K_HyVyMJV4a14YVWxlZAQgFA5Vr_1XTQOEyc0vwtMtTmZtpDKQfCVjZqCbUkuKH4nsDohVLLSnw")


if __name__ == "__main__":
    main()
