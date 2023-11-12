import logging
import queue
import threading
import time

from src.web.analyse import fetch_trend


class UpdateTrendThread(threading.Thread):
    def __init__(self, q: queue.Queue):
        threading.Thread.__init__(self)
        self._q = q

    def run(self):
        while True:
            try:
                item = self._q.get(block=False)

                # None stops thread
                if item is None:
                    return

                logging.debug("updating trend from worker")

                fetch_trend(item)
            except queue.Empty:
                pass

            time.sleep(1)


update_trend_queue = queue.Queue()
update_trend_thread = UpdateTrendThread(update_trend_queue)
update_trend_thread.start()
