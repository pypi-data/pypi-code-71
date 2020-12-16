

#
##  Paranoid Pirate worker
#
#   Author: Daniel Lundin <dln(at)eintr(dot)org>
#

from random import randint
import time
from binascii import hexlify

import zmq

HEARTBEAT_LIVENESS = 5
HEARTBEAT_INTERVAL = 5
INTERVAL_INIT = 1
INTERVAL_MAX = 32

#  Paranoid Pirate Protocol constants
PPP_READY = b"\x01"      # Signals worker is ready
PPP_HEARTBEAT = b"\x02"  # Signals worker heartbeat

service = b"count"

def worker_socket(context, poller):
    """Helper function that returns a new configured socket
       connected to the Paranoid Pirate queue"""
    worker = context.socket(zmq.DEALER) # DEALER

    poller.register(worker, zmq.POLLIN)
    worker.connect("tcp://localhost:5556")
    worker.send_multipart([PPP_READY, service])
    return worker

context = zmq.Context(1)
poller = zmq.Poller()

liveness = HEARTBEAT_LIVENESS
interval = INTERVAL_INIT

heartbeat_at = time.time() + HEARTBEAT_INTERVAL

worker = worker_socket(context, poller)
cycles = 0
while True:
    socks = dict(poller.poll(HEARTBEAT_INTERVAL * 1000))

    # Handle worker activity on backend
    if socks.get(worker) == zmq.POLLIN:
        #  Get message
        #  - 3-part envelope + content -> request
        #  - 1-part HEARTBEAT -> heartbeat
        frames = worker.recv_multipart()
        print(frames)
        if not frames:
            break # Interrupted

        if len(frames) == 4:
            # Simulate various problems, after a few cycles
            cycles += 1
            # if cycles > 3 and randint(0, 5) == 0:
            #     print("I: Simulating a crash")
            #     break
            if cycles > 3 and randint(0, 5) == 0:
                print("I: Simulating CPU overload")
                time.sleep(3)
            print("Request from: {}, sequence: {}".format(hexlify(frames[0]), frames[3]))
            client = frames.pop(0)
            response = [client, b"count"] + frames

            print("I: Normal reply. frames: {}".format(response))
            worker.send_multipart(response)
            liveness = HEARTBEAT_LIVENESS
            time.sleep(1)  # Do some heavy work
        elif len(frames) == 1 and frames[0] == PPP_HEARTBEAT:
            print("I: Queue heartbeat")
            liveness = HEARTBEAT_LIVENESS
        else:
            print("E: Invalid message: %s" % frames)
        interval = INTERVAL_INIT
    else:
        liveness -= 1
        if liveness == 0:
            print("W: Heartbeat failure, can't reach queue")
            print("W: Reconnecting in %0.2fs…" % interval)
            time.sleep(interval)

            if interval < INTERVAL_MAX:
                interval *= 2
            poller.unregister(worker)
            worker.setsockopt(zmq.LINGER, 0)
            worker.close()
            worker = worker_socket(context, poller)
            liveness = HEARTBEAT_LIVENESS
    if time.time() > heartbeat_at:
        heartbeat_at = time.time() + HEARTBEAT_INTERVAL
        print("I: Worker heartbeat")
        worker.send_multipart([PPP_HEARTBEAT, service])
