import os

from moviepy import VideoFileClip
from colorama import Fore

def extract_extention(file: str) -> str:
    """
    extracts the file extention from the given file as a parameter
    and returns the extention and the base file

    :example >>> python3 script_path.py
    :returns >>> file/path/and/name .extention
    """
    base, extention = os.path.splitext(file)
    return base, extention


def convert_to_mp4(file: str, output_file: str) -> None:
    """
    converts from a .webm file to a .mp4 file it takes in
    a file and an output file

    :param file = the file which must be a .webm
    :param output_file = the output file which must be a .mp4
    """
    try:
        video = VideoFileClip(file)
        video.write_videofile(output_file, codec="libx264")
    except Exception as e:
        print(Fore.RED + f"Encountered an error converting the file: {e}")


def change_file_extention(base_file: str) -> str:
    """
    changes the extention of a .webm file to .mp4 file so that it gets saves successfully
    with a new name, the output of this function will be used for the convert_to_mp4 function
    as the output_file paramameter

    :param base_file = gets the base file that comes from the function extract_extention which is the file without the extention

    and then once it gets the file it adds to it .mp4 as an extention
    """
    return base_file + ".mp4"


def main() -> None:
    """
    gets the current working directory and lists all the files inside of it
    then it extracts the extention and checks if it is equal to .webm

    if it is we will change the file_extention to .mp4 from .webm
    and then we will convert the file and delete the file that was converted
    """
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
