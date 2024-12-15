
class VideoEncoder:
    def encode(self, video_path):
        print(f"Encoding video from {video_path}...")
        return "encoded_video.mp4"

class StorageService:
    def save(self, file_path):
        print(f"Saving {file_path} to storage...")
        return "https://service.com/videos/encoded_video.mp4"

class NotificationService:
    def notify_user(self, user_id, video_url):
        print(f"Notifying user {user_id} about video: {video_url}")


class VideoStreamingFacade:
    def __init__(self):
        self.encoder = VideoEncoder()
        self.storage = StorageService()
        self.notification = NotificationService()

    def upload_and_notify(self, video_path, user_id):
        
        encoded_video = self.encoder.encode(video_path)
        video_url = self.storage.save(encoded_video)
        self.notification.notify_user(user_id, video_url)
        print("Video upload and notification process completed.")

if __name__ == "__main__":
    
    facade = VideoStreamingFacade()

    print("Starting video upload process...")
    facade.upload_and_notify("raw_video.mp4", user_id=12345)
