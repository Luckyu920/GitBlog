# -*- coding: utf-8 -*-
import argparse
import os
import re
import time
from datetime import datetime, timedelta, timezone
import markdown
from feedgen.feed import FeedGenerator
from github import Github
from lxml.etree import CDATA
from marko.ext.gfm import gfm as marko

WORK_DIR = "test"

def format_time(time):
    return str(time)[:10]

def write_file(file_name,file_content, dir_name=WORK_DIR):
    # print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # time.strftime("%Y%m%d%H%M%S", time.localtime())
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  # 构建了 UTC 的当前时间
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  # 将时区转化为东八区的时间
    md_name = os.path.join(
        dir_name,"charge_log.md"
    )
    time_str=bj_dt.strftime('%Y-%m-%d %H:%M:%S')
    with open(md_name, "a+") as f:
        # f.write(f"# 充电记录\n\n")
        f.write(f"## {time_str}，{file_name}，当前电量：{file_content}\n")

if __name__ == "__main__":
    if not os.path.exists(WORK_DIR):
        os.mkdir(WORK_DIR)
    parser = argparse.ArgumentParser()
    parser.add_argument("msg", help="message")
    parser.add_argument(
        "--title", help="title", default=None, required=False
    )
    options = parser.parse_args()
    # main(options.github_token, options.repo_name, options.issue_number)
    write_file(options.title,options.msg)
