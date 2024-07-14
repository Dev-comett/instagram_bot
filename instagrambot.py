from instagrambot import Bot
import os

def post_image(image_path, caption, username, password):
    bot = Bot()
    bot.login(username=username, password=password)
    bot.upload_photo(image_path, caption=caption)
    bot.logout()

def post_video(video_path, thumbnail_path, caption, username, password):
    bot = Bot()
    bot.login(username=username, password=password)
    bot.upload_video(video_path, thumbnail=thumbnail_path, caption=caption)
    bot.logout()

# Example usage
if __name__ == "__main__":
    username = "your_instagram_username"
    password = "your_instagram_password"

    image_path = "path_to_your_image.jpg"
    video_path = "path_to_your_video.mp4"
    thumbnail_path = "path_to_your_thumbnail.jpg"
    caption = "Your caption here"


    



    # Post an image
    post_image(image_path, caption, username, password)

    # Post a video
    post_video(video_path, thumbnail_path, caption, username, password)
