# Database oriented Youtube Videos List Management Program

# ? database connection initialization
import sqlite3

myConnection = sqlite3.connect("yvm.db")
myCursor = myConnection.cursor()
myCursor.execute(
    "CREATE TABLE IF NOT EXISTS videos(id INTEGER PRIMARY KEY, name TEXT NOT NULL, time TEXT NOT NULL, channel TEXT NOT NULL)"
)


# ? user defined functions
def show_videos():
    found = False
    myCursor.execute("SELECT * FROM videos")
    for row in myCursor.fetchall():
        found = True
        print(f"{row[0]}. Video Title: {row[1]}, Time: {row[2]}, Channel: {row[3]}")
    if not found:
        print("\nNo data found!\nFirst, add something\n")


def add_video():
    name = input("\nEnter name of video : ")
    time = input("Enter the watch time : ")
    channel = input("Enter source channel : ")

    myCursor.execute(
        "INSERT INTO videos (name, time, channel) VALUES (?, ?, ?)",
        (name, time, channel),
    )
    myConnection.commit()
    print("\nsuccess: video info. added!\n")


def update_video():
    show_videos()
    video_id = int(input("\nEnter the number of video item : "))
    new_name = input("Enter new name : ")
    new_time = input("Enter new time : ")
    new_channel = input("Enter new channel name : ")

    myCursor.execute(
        "UPDATE videos SET name=?, time=?, channel=? WHERE id=?",
        (new_name, new_time, new_channel, video_id),
    )
    myConnection.commit()
    print("\nsuccess: data updated\n")


def delete_video():
    show_videos()
    video_id = int(input("\nEnter number of video item : "))
    myCursor.execute("DELETE FROM videos WHERE id=?", (video_id,))
    myConnection.commit()
    print("\nsuccess: video item deleted\n")


# ? main method | entry point
def main():
    while True:
        print("\nYoutube Manager\n")
        print("1. Show all videos")
        print("2. Add a video")
        print("3. Update video")
        print("4. Delete videos")
        print("0. Exit the app")

        choice = input("\nEnter a choice : ")

        match choice:
            case "0":
                print("\nProgram exited successfully\n")
                break
            case "1":
                show_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                delete_video()
            case _:
                print("\nerror: invalid input\n")


if __name__ == "__main__":
    main()
