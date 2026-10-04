import concurrent.futures
import os
import urllib.request

URL = os.environ.get(
    "TARGET_URL",
    "http://prodpai-alb-684626271.us-east-1.elb.amazonaws.com/",
)


def spam():
    while True:
        try:
            urllib.request.urlopen(URL, timeout=2)
        except Exception:
            pass


def main(workers=50):
    print(f"Load testing {URL} ... Press Ctrl+C to stop.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for _ in range(workers):
            executor.submit(spam)


if __name__ == "__main__":
    main()