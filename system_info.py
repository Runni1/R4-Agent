import psutil
import platform
import shutil

def get_system_info():
    try:
        # CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)

        # RAM usage
        ram = psutil.virtual_memory()
        ram_used = round(ram.used / (1024**3), 2)
        ram_total = round(ram.total / (1024**3), 2)
        ram_percent = ram.percent

        # Disk usage
        disk = shutil.disk_usage("/")
        disk_used = round(disk.used / (1024**3), 2)
        disk_total = round(disk.total / (1024**3), 2)
        disk_percent = round((disk.used / disk.total) * 100, 2)

        # System info
        system = platform.system()
        version = platform.release()

        # Formatting output
        result = (
            f"🔧 **System Information**\n"
            f"• Sistem Operasi : {system} {version}\n\n"
            f"🧠 **CPU**\n"
            f"• Penggunaan CPU : {cpu_usage}%\n\n"
            f"💾 **RAM**\n"
            f"• RAM Terpakai : {ram_used} GB dari {ram_total} GB ({ram_percent}%)\n\n"
            f"📦 **Storage**\n"
            f"• Storage Terpakai : {disk_used} GB dari {disk_total} GB ({disk_percent}%)"
        )

        return result

    except Exception as e:
        return f"Terjadi kesalahan saat mengambil info sistem: {e}"
