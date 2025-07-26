import os

from moviepy import VideoFileClip
from colorama import Fore

def extract_extention(file: str) -> str:
    base, extention = os.path.splitext(file)
    return base, extention

def convert_to_mp4(file: str, output_file: str) -> None:
    try:
        video = VideoFileClip(file)
        video.write_videofile(output_file, codec="libx264")
    except Exception as e:
        print(Fore.RED + f"Encountered an error converting the file: {e}")

def change_file_extention(base_file: str) -> str:
    return base_file + ".mp4"

def main() -> None:
    current_working_dir: str = os.getcwd()
    files_in_dir: list[str] = os.listdir(current_working_dir)

    DESIRED_EXTENTION: str = ".webm"

    for file_in_dir in files_in_dir:
        base, extention = extract_extention(file=file_in_dir)
        if extention == DESIRED_EXTENTION:
            output_file: str = change_file_extention(base_file=base)
            convert_to_mp4(file=file_in_dir, output_file=output_file)
            os.remove(file_in_dir)
    
    print(Fore.GREEN + "Done.")


if __name__ == '__main__':
    main()
