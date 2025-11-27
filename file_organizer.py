import os
import shutil

# Klasifikasi ekstensi
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
    "Music": [".mp3", ".wav", ".m4a"],
    "APK": [".apk"],
    "Archives": [".zip", ".rar", ".7z"],
}

def smart_organize(path):
    """
    Mengorganisir file ke subfolder berdasarkan kategorinya.
    """
    try:
        if not os.path.exists(path):
            return f"Folder '{path}' tidak ditemukan."

        moved = 0

        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)

            if os.path.isdir(file_path):
                continue

            ext = os.path.splitext(filename)[1].lower()

            for category, extensions in CATEGORIES.items():
                if ext in extensions:
                    target_folder = os.path.join(path, category)

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    shutil.move(file_path, os.path.join(target_folder, filename))
                    moved += 1
                    break

        if moved == 0:
            return "Tidak ada file yang dapat diorganisir."

        return f"Berhasil merapikan {moved} file ke folder kategori masing-masing."

    except Exception as e:
        return f"Terjadi error: {e}"
