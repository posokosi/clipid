import pyperclip
import time
import re

def main():
    print("監視開始… (Ctrl+Cで終了)")
    last_clip = pyperclip.paste()
    last_result = None
    

    try:
        while True:
            current = pyperclip.paste()

            if current != last_clip and current != last_result:
                last_clip = current
                result = re.match("^[0-9]+$", current)

                if result:
                    id = result.group()
                    last_result = id
                    
                    with open("id.txt", "w") as o:
                        print(f"ID: {id}", file=o)

                    print("IDをテキストファイルに出力しました。")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n監視を終了しました。")

if __name__ == "__main__":
    main()
