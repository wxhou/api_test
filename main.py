#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import subprocess


def main():
    """主函数"""

    cmd_all = (
        "pytest",
        # "source venv/bin/activate",
        # "pytest --html=report.html --self-contained-html --alluredir allure-results --clean-alluredir",
        # "cp config/environment.properties allure-results",
        # "allure generate allure-results -c -o allure-report",
        # "allure open allure-report"
    )
    for cmd in cmd_all:
        subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    main()
