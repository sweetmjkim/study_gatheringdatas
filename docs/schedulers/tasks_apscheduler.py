# import pymongo
# import requests
from apscheduler.schedulers.background import BackgroundScheduler
# import time

# 주기적으로 실행할 함수
# from docs.beatifulsoups import feature
from sample_function import message_print, job_print
if __name__ == '__main__':
    scheduler = BackgroundScheduler()

    # 주기적으로 실행할 작업 등록 (예: 1시간마다)
    # trigger:정해진 시간 간격마다 실행, seconds:시간 간격
    # , coalesce:다수 작업 예약시 단 한 번만 실행, max_instances:동시 실행 작업 인스턴스 최대 수
    # scheduler.add_job(feature, trigger='interval', seconds=2, coalesce=True, max_instances=1)
    scheduler.add_job(message_print, trigger='interval', seconds=2, coalesce=True, max_instances=1)
    scheduler.add_job(job_print, trigger='interval', seconds=2, coalesce=True, max_instances=1)

    scheduler.start()

    # 무한 루프 (응답 지속 기다림.)
    while True:
        pass
    
    # try:
    #     # 무한 루프를 사용하여 메인 프로그램이 종료되지 않도록 함
    #     while True:
    #         time.sleep(1)
    #         pass
    # except (KeyboardInterrupt, SystemExit):
    #     # 프로그램이 종료될 때 스케줄러도 함께 종료
    #     scheduler.shutdown()    