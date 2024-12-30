import json


# ? user defined methods & functions
def load_videos_list():
    try:
        with open("yvm.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_video_helper(videos):
    with open("yvm.txt", "w") as file:
        json.dump(videos, file)


def list_videos(videos):
    print(f"\n{'*' * 30}\n")
    for index, video in enumerate(videos, start=1):
        print(f"{index} : {video['name']}, {video['time']}")
    print(f"\n{'*' * 30} \n\n")


def add_videos(videos):
    name = input("Enter video name : ")
    time = input("Enter watch time : ")
    videos.append({"name": name, "time": time})
    save_video_helper(videos)
    print("\nSuccess: video saved in file yvm.txt")


def update_videos(videos):
    list_videos(videos)
    user_index = int(input("Enter the number of video to be updated : "))
    if 0 < user_index <= len(videos):
        name = input("Enter new name : ")
        time = input("Enter new time : ")
        videos[user_index - 1]["name"] = name
        videos[user_index - 1]["time"] = time
        print("\nsuccess: video updated\n")
        save_video_helper(videos)
        list_videos(videos)
    else:
        print("\nerror: invalid input\n")
        update_videos(videos)


def delete_videos(videos):
    list_videos(videos)
    user_index = int(input("Enter number of video to be deleted : "))
    if 0 < user_index <= len(videos):
        del videos[user_index - 1]
        save_video_helper(videos)
        print("\nsuccess: video deleted\n")
        list_videos(videos)
    else:
        print("\nerror: invalid input\n")
        delete_videos(videos)


# main function | Entry point
def main():
    videos = load_videos_list()
    while True:
        print(f"\n{'-'*28}\n   Youtube Videos Manager\n{'-'*28}")
        print(
            "\nSelect an option below\n1. List all videos available\n2. Add a new video\n3. Update a Youtube video\n4. Delete a Youtube video\n0. Exit the program\n"
        )
        choice = input("Enter option number : ")

        match choice:
            case "0":
                print("Program exited successfully, Developer Afnan\n\n")
                break
            case "1":
                list_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case _:
                print("error: invalid input")


if __name__ == "__main__":
    main()
