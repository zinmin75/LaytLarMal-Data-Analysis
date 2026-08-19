import time
from apscheduler.schedulers.background import BackgroundScheduler

from weather_collector import collect_weather_data


def start_scheduler():
    print("Starting the automated weather scheduler...")

    collect_weather_data()

    scheduler = BackgroundScheduler()

    scheduler.add_job(collect_weather_data, "cron", minute=5)  # interval, date

    scheduler.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping the weather scheduler...")
        scheduler.shutdown()


start_scheduler()
